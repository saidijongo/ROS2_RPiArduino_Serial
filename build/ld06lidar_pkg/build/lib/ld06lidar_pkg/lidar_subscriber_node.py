import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')
        self.subscription = self.create_subscription(
            Range,
            'lidar_data',
            self.lidar_data_callback,
            10)
        self.subscription  # prevent unused variable warning

    def lidar_data_callback(self, msg):
        self.get_logger().info('Received Lidar Data: %f' % msg.range)

def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber)
    lidar_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
