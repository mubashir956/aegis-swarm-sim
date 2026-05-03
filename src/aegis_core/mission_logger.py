import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import os
from datetime import datetime

class MissionLogger(Node):

    def __init__(self):
        super().__init__('mission_logger')

        self.sub = self.create_subscription(
            String, '/aegis/survivor_detected',
            self.log_event, 10)

        log_dir = os.path.expanduser(
            '~/aegis-swarm-sim/docs/mission_logs/')
        os.makedirs(log_dir, exist_ok=True)

        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.log_file = os.path.join(log_dir, f'mission_{ts}.json')
        self.events = []

        self.get_logger().info(f'Mission Logger → {self.log_file}')

    def log_event(self, msg):
        event = json.loads(msg.data)
        self.events.append(event)

        with open(self.log_file, 'w') as f:
            json.dump({
                'mission_start': self.events[0]['timestamp'],
                'total_survivors': len(self.events),
                'detections': self.events
            }, f, indent=2)

        self.get_logger().info(
            f'Logged Survivor #{event["id"]} → {self.log_file}')


def main():
    rclpy.init()
    node = MissionLogger()
    rclpy.spin(node)
    rclpy.shutdown()

