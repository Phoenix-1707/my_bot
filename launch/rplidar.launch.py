import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            output='screen',
            parameters=[{
                'serial_port': 'pci-0000:05:00.4-usb-0:2:1.0-port0',
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'DenseBoost'
                }]
        )
    ])