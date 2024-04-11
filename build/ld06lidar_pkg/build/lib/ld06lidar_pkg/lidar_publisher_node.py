import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

class LidarPublisher(Node):
    def __init__(self):
        super().__init__('lidar_publisher')
        self.publisher_ = self.create_publisher(Range, 'lidar_data', 10)
        self.timer = self.create_timer(1, self.publish_lidar_data)

    def publish_lidar_data(self):
        lidar_msg = Range()
        lidar_msg.header.frame_id = 'lidar_frame'
        lidar_msg.radiation_type = Range.INFRARED
        lidar_msg.field_of_view = 0.2
        lidar_msg.min_range = 0.1
        lidar_msg.max_range = 30.0
        lidar_msg.range = 10.0
        self.publisher_.publish(lidar_msg)
        self.get_logger().info('Publishing Lidar Data')

def main(args=None):
    rclpy.init(args=args)
    lidar_publisher = LidarPublisher()
    rclpy.spin(lidar_publisher)
    lidar_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
