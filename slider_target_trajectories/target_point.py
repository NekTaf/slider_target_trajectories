# target_publisher.py
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry     # changed
from rclpy.qos import QoSPresetProfiles

from .config import TargetTrajectoriesCfg

class TargetPoint(Node):
    def __init__(self):
        super().__init__('target_point')


        self.msg = Odometry()
        self.msg.header.frame_id = TargetTrajectoriesCfg.frame

        self.msg.pose.pose.position.x = TargetTrajectoriesCfg.target_x
        self.msg.pose.pose.position.y = TargetTrajectoriesCfg.target_y
        self.msg.pose.pose.position.z = 0.0

        self.msg.twist.twist.linear.x = 0.0
        self.msg.twist.twist.linear.y = 0.0
        self.msg.twist.twist.linear.z = 0.0

        self.publisher_ = self.create_publisher(
            Odometry,
            'target_point',
            QoSPresetProfiles.get_from_short_key('system_default')
        )
        
        self.timer = self.create_timer(1.0 / TargetTrajectoriesCfg.publish_frequency, self._tick)

    def _tick(self):
        self.msg.header.stamp = self.get_clock().now().to_msg()
        self.publisher_.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)
    node = TargetPoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
