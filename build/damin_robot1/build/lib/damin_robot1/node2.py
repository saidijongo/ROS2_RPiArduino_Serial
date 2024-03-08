#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Node2(Node):
    def __init__(self):
        super().__init__('node2')

        self.get_logger().info("Jongo Node 2 started")

def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
