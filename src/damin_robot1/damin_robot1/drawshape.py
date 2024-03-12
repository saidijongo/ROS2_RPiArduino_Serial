#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawShapeNode(Node):
    
    def __init__(self):
        super().__init__('New_Shape')
        self.cmd_vel_pub =self.create_publisher(Twist, '/turtle1/cmd_vel',10)
        self.timer = self.create_timer(0, self.send_values)
        self.get_logger().info("Shape node running..")

    def send_values(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z =1.0
        self.cmd_vel_pub.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = DrawShapeNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#source /opt/ros/humble/setup.bash
#source ~/ros2_ws/install/setup.bash
#ls /opt/ros/humble/local/lib/python3.10/dist-packages/geometry_msgs
