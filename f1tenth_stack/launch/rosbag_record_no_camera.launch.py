from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('topics', default_value=['/ackermann_cmd /clicked_point /clock /commands/motor/brake /commands/motor/current /commands/motor/duty_cycle /commands/motor/position /commands/motor/speed /commands/servo/position /diagnostics /drive /joy /joy/set_feedback /laser_status /odom /parameter_events /rosout /scan /teleop /tf /tf_static'], description='Topics to record'),
        ExecuteProcess(cmd=['ros2', 'bag', 'record', LaunchConfiguration('topics')], shell=True),
    ])
