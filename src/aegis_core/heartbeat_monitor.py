import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random
import math

class HeartbeatMonitor(Node):

	def __init__(self):
		super().__init__('heartbeat_monitor')

		self.publisher = self.create_publisher(Float32,'/acoustic_signal',10)

		self.timer = self.create_timer(1.0,self.read_acoustic_sensor)

		self.time_elapsed = 0.0
		self.get_logger().info('Heartbeat Monitor Node Started')

	def read_acoustic_sensor(self):

		self.time_elapsed += 1.0

		heartbeat_freq = 1.2
		signal_strength = math.sin(2*math.pi*heartbeat_freq*self.time_elapsed)

		noise = random.gauss(0,0.3)
		raw_signal = signal_strength + noise

		msg = Float32()
		msg.data = float(raw_signal)
		self.publisher.publish(msg)

		self.get_logger().info(f'Acoustic Signal:{raw_signal:.4f}')

def main():
	rclpy.init()
	node = HeartbeatMonitor()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()

