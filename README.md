# 2.0tenth_sw_stack
An updated Software Stack for ROS2 Humble and the updated 2.0Tenth platform
i.e. a custom build upgrade of the F1Tenth platform

## Installation Pre-Requisites
The ZED SDK must be pre-installed for a succesful build
https://www.stereolabs.com/en-gr/developers

## ROS2 Humble Build
1. Create your workspace folder
2. Create a src folder
3. Run `colcon build` on the empty folder to initialize
5. Clone the repository into the src folder
6. Run `rosdep update`
7. Run `rodep install --from-paths src -i -y`
8. Run `colcon build`

The build should be succesfully completed

## Tips 

Don't forget to `source /opt/ros/humble/setup.bash` if not 
in your `.bashrc` file.
Also `source install/setup.bash` on your workspace after the 
succesful build 

In a clean Ubuntu 22.04 some ROS packages might be required. 
Make sure to read the build errors and address them accordingly. 

e.g. On a clean Ubuntu 22.04 asio_cmake_module was missing. 
It can be simply installed through `sudo apt install ros_hubmle_asio_cmake_module`

## Launch Files
There are 4 useful `.launch` files which can be used for testing

1. `ros2 launch f1tenth_stack f1_tenth_gui.launch.py` -> Launches the control and sensors stack
stack together with RViz in order to visualize the sensor input
2. `ros2 launch f1tenth_stack f1_tenth_remote.launch.py` -> Launches the control and sensors stack only.
Helpful for testing the car. 
3. `ros2 launch f1tenth_stack rosbag_record.launch.py` -> Records all topics published in ROS bag format.
Requires either 1 or 2 running already.
4. `ros2 launch f1tenth_stack rosbag_record_no_camera.launch.py` -> Records all other topics except the camera. 
