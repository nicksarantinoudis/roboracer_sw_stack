# f1tenth_2.0_sw_stack
An updated F1Tenth Software Stack for ROS2 Humble

## Installation Pre-Requisite
The ZED SDK must be pre-installed for a succesful build
https://www.stereolabs.com/en-gr/developers

### ROS2 Build
1. Create a folder
2. Run `colcon build` on the empty folder to initialize
3. Create a src folder
4. Clone the repository into the src folder
5. Run 'rosdep update'
6. Run 'rodep install --from-paths src -i -y
7. Run 'colcon build'
