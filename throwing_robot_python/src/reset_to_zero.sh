#!/bin/bash
echo Resetting robot and ball to zero configuration ...........
rostopic pub -1 /throwing_robot/joint3_position_controller/command std_msgs/Float64 "data: 0"
rostopic pub -1 /throwing_robot/joint2_position_controller/command std_msgs/Float64 "data: 0"
rostopic pub -1 /throwing_robot/joint4_position_controller/command std_msgs/Float64 "data: 0"
rosservice call /gazebo/set_model_state '{model_state: { model_name: ball, pose: { position: { x: 0, y: 0 ,z: 0 }, orientation: {x: 0, y: 0, z: 0.08, w: 0} }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , reference_frame: finger_1 } }'