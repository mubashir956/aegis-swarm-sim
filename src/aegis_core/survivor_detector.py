import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32
from nav_msgs.msg import Odometry
import json
import math
from datetime import datetime

class SurvivorDetector(Node):

    def __init__(self):
        super().__init__('survivor_detector')

        # Subscribe to acoustic signal from heartbeat monitor
        self.acoustic_sub = self.create_subscription(
            Float32, '/acoustic_signal',
            self.acoustic_callback, 10)

        # Subscribe to robot position
        self.odom_sub = self.create_subscription(
            Odometry, '/odom',
            self.odom_callback, 10)

        # Publish confirmed detections
        self.survivor_pub = self.create_publisher(
            String, '/aegis/survivor_detected', 10)

        # Robot state
        self.robot_x = 0.0
        self.robot_y = 0.0

        # Signal buffer for pattern detection
        self.signal_buffer = []
        self.buffer_size = 20

        # Detection state
        self.confirmed_survivors = []
        self.cooldown = 0
        self.detection_count = 0

        self.get_logger().info('AEGIS Survivor Detector ONLINE')
        self.get_logger().info(
            'Method: Acoustic heartbeat + proximity')

    def odom_callback(self, msg):
        self.robot_x = msg.pose.pose.position.x
        self.robot_y = msg.pose.pose.position.y

    def acoustic_callback(self, msg):
        # Cooldown between detections
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        # Build signal buffer
        self.signal_buffer.append(msg.data)
        if len(self.signal_buffer) > self.buffer_size:
            self.signal_buffer.pop(0)

        if len(self.signal_buffer) < self.buffer_size:
            return

        # Analyze signal pattern
        import numpy as np
        signal = self.signal_buffer
        mean = sum(signal) / len(signal)
        std = (sum((x - mean)**2 for x in signal)
               / len(signal)) ** 0.5
        latest = signal[-1]

        # Heartbeat detected if signal exceeds threshold
        heartbeat_detected = (
            latest > mean + 1.5 * std or
            latest < mean - 1.5 * std
        )

        if not heartbeat_detected:
            return

        # Check if already found survivor near here
        already_found = False
        for s in self.confirmed_survivors:
            dist = math.sqrt(
                (s['x'] - self.robot_x)**2 +
                (s['y'] - self.robot_y)**2)
            if dist < 1.0:
                already_found = True
                break

        if already_found:
            return

        # New survivor confirmed!
        self.detection_count += 1
        survivor = {
            'id': self.detection_count,
            'x': round(self.robot_x, 2),
            'y': round(self.robot_y, 2),
            'confidence': round(
                min(1.0, abs(latest - mean) / std / 3), 3),
            'timestamp': datetime.now().isoformat(),
            'detection_method': 'acoustic_heartbeat',
            'unit': 'crawler_1'
        }

        self.confirmed_survivors.append(survivor)

        msg_out = String()
        msg_out.data = json.dumps(survivor)
        self.survivor_pub.publish(msg_out)

        self.get_logger().warn(
            f'\n'
            f'╔══════════════════════════════════╗\n'
            f'║  SURVIVOR #{self.detection_count} DETECTED          ║\n'
            f'║  Position: ({self.robot_x:.1f}, {self.robot_y:.1f})      ║\n'
            f'║  Method: Acoustic Heartbeat      ║\n'
            f'║  Confidence: {survivor["confidence"]:.1%}           ║\n'
            f'║  Total found: {len(self.confirmed_survivors)}                 ║\n'
            f'╚══════════════════════════════════╝'
        )

        # Set cooldown to avoid duplicate detections
        self.cooldown = 1


def main():
    rclpy.init()
    node = SurvivorDetector()
    rclpy.spin(node)
    rclpy.shutdown()
