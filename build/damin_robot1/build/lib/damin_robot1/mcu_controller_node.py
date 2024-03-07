
#!/usr/bin/env python3

''' 
import rclpy
from rclpy.node import Node 

class mcuNode(Node):
    def __init__(self):
        super().__init__("mcu1")
        self.get_logger().info("DaminRobot improves people's lives")


def main(args=None):
    rclpy.init(args=args)
    #creating nodes

    rclpy.shutdown()

if __name__== '__main__':
    main()

'''


import rclpy
from rclpy.node import Node
import serial

class ArduinoControlNode(Node):
    def __init__(self):
        super().__init__('arduino_control_node')
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

    def send_command_to_arduino(self, command):
        self.ser.write(command.encode())

def main(args=None):
    rclpy.init(args=args)
    arduino_node = ArduinoControlNode()
    
    # Send commands to Arduino
    arduino_node.send_command_to_arduino('1')  # Turn on LED
    arduino_node.send_command_to_arduino('0')  # Turn off LED

    rclpy.shutdown()

if __name__ == '__main__':
    main()
