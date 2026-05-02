import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from collections import deque
import numpy as np

class SignalAnalyzer(Node):

	def __init__(self):
		super().__init__('signal_analyzer')

		self.subscription = self.create_subscription(
			Float32,
			'/acoustic_signal',
			self.analyze_signal,
			10
		)

		self.signal_buffer = deque(maxlen=20)
		self.get_logger().info('Signal Analyzer Ready')

	def analyze_signal(self,msg):
		self.signal_buffer.append(msg.data)

		if len(self.signal_buffer) < 10:
			return

		signal_array = np.array(self.signal_buffer)
		mean = np.mean(signal_array)
		std = np.std(signal_array)
		latest = signal_array[-1]

		if latest > mean +(1.5*std) or latest < mean -(1.5*std):
			self.get_logger().warn('POTENTIAL HEARTBEAT DETECTED')
		else:
			self.get_logger().error(f'NO HEARTBEAT DETECTED | Background Noise. Mean: {mean:.3f}')


def main():
	rclpy.init()
	node = SignalAnalyzer()
	rclpy.spin(node)
	rclpy.shutdown()
