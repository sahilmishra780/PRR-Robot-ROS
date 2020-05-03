#!/bin/bash
rostopic pub -1 /throwing_robot/joint1_position_controller/command std_msgs/Float64 "data: -0.45"
rosrun throwing_robot_python initialize_robot.sh
rosrun throwing_robot_python trajectory_large.py
rosrun throwing_robot_python reset_to_zero.sh
rostopic pub -1 /throwing_robot/joint1_position_controller/command std_msgs/Float64 "data: 0"
rostopic pub -1 /throwing_robot/joint1_position_controller/command std_msgs/Float64 "data: 0.45"
rosrun throwing_robot_python initialize_robot.sh
rosrun throwing_robot_python trajectory_small.py
rosrun throwing_robot_python reset_to_zero.sh