#!/usr/bin/env python3

'''
import rclpy
from rclpy.node import Node

class Node1(Node):
    def __init__(self):
        super().__init__('node1')

        self.get_logger().info("Udated Node 1 started")

def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    #rclpy.spin(node)
    #rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
'''

#added callback_timer()
'''

import rclpy
from rclpy.node import Node

class Node1(Node):
    def __init__(self):
        super().__init__('node1')

        #self.get_logger().info("Udated Node 1 started")
        self.create_timer(2.0, self.callback_timer)

    def callback_timer(self):
        self.get_logger().info("MCU RS485")


def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    #rclpy.spin(node)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

'''
#callback, counter added


import rclpy
from rclpy.node import Node

class Node1(Node):
    def __init__(self):
        super().__init__('node1')

        #self.get_logger().info("Udated Node 1 started")

        self.counter_ = 0
        self.create_timer(2.0, self.callback_timer)

    def callback_timer(self):
        self.get_logger().info("Motor running..." + str(self.counter_))
        self.counter_+=1


def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    #rclpy.spin(node)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
