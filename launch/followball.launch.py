from launch import LaunchDescription
from launch_ros.actions import Node

import os

from ament_index_python import get_package_share_directory

def generate_launch_description():
    ball_tracker_params = os.path.join(get_package_share_directory('articubot_one'), "config", "ball_tracker_params_example.yaml")

    detect_ball_node = Node(package="ball_tracker",
                        executable="detect_ball",
                        parameters=[ball_tracker_params],
                        remappings=[("image_in", "camera/image_raw")])
    
    detect_ball_3d_node = Node(package="ball_tracker",
                        executable="detect_ball_3d",
                        parameters=[ball_tracker_params])
    
    follow_ball_node = Node(package="ball_tracker",
                        executable="follow_ball",
                        parameters=[ball_tracker_params],
                        remappings=[("cmd_vel", "cmd_vel_tracker")])

    return LaunchDescription([
        detect_ball_node,
        detect_ball_3d_node,
        follow_ball_node
    ])