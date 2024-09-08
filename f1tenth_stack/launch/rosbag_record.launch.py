from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('topics', default_value=['/ackermann_cmd /clicked_point /clock /commands/motor/brake /commands/motor/current /commands/motor/duty_cycle /commands/motor/position /commands/motor/speed /commands/servo/position /diagnostics /drive /joy /joy/set_feedback /laser_status /odom /parameter_events /rosout /scan /teleop /tf /tf_static /zed/joint_states /zed/plane /zed/plane_marker /zed/robot_description /zed/zed_node/confidence/confidence_map /zed/zed_node/depth/camera_info /zed/zed_node/depth/depth_info /zed/zed_node/depth/depth_registered /zed/zed_node/disparity/disparity_image /zed/zed_node/point_cloud/cloud_registered /zed/zed_node/rgb/camera_info /zed/zed_node/rgb/image_rect_color'], description='Topics to record'),
        ExecuteProcess(cmd=['ros2', 'bag', 'record', LaunchConfiguration('topics')], shell=True),
    ])
