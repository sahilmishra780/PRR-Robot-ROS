#!/bin/bash
echo Initializing robot and ball configuration ...........
rostopic pub -1 /throwing_robot/joint3_position_controller/command std_msgs/Float64 "data: 1.2"
rostopic pub -1 /throwing_robot/joint2_position_controller/command std_msgs/Float64 "data: -2"