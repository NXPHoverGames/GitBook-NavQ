#Copyright 2016 Open Source Robotics Foundation, Inc.
#
#Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CameraInfo


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(CameraInfo, 'camera_info', 10)
        timer_period = 0.066  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.msg = CameraInfo()
        self.msg.height = 640
        self.msg.width = 480
        self.msg.distortion_model = "plumb_bob"
        self.msg.d = [0.038385, -0.042656, 0.000869, -0.002758, 0.000000]
        self.msg.k = [445.448888, 0.000000, 317.524152, 0.000000, 444.667306, 241.555012, 0.000000, 0.000000, 1.000000]

    def timer_callback(self):
        self.publisher_.publish(self.msg)
        self.get_logger().info('Publishing: "%s"' % self.msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
