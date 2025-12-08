from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
import os
from datetime import datetime
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([

        DeclareLaunchArgument('target_x', default_value='0.0', description=''),
        DeclareLaunchArgument('target_y', default_value='0.0', description=''),

        Node(
            package='slider_target_trajectories',  
            executable='target_point',
            name='target_point',
            parameters=[{
                'frame_id': 'world',
                'publish_rate': 10.0,
                'target_x': LaunchConfiguration('target_x'),
                'target_y': LaunchConfiguration('target_y'),
            }],
        )
        
    ])
