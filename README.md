# meen612_robot
Course project for MEEN 612
<br><br>
Rviz launch:<br>
`` roslaunch throwing_robot throwing_robot_rviz.launch``<br>
<br><br>
Gazebo launch:<br>
``roslaunch throwing_robot_gazebo throwing_robot.launch ``
<br><br>
Joint Position Controller launch:<br>
``roslaunch throwing_robot_control throwing_robot_control.launch ``
<br><br>
Publish Commands:<br>
``rostopic pub -1 /throwing_robot/joint1_position_controller/command std_msgs/Float64 "data: 0.3"``<br>
``rostopic pub -1 /throwing_robot/joint2_position_controller/command std_msgs/Float64 "data: 0.5"``<br>
``rostopic pub -1 /throwing_robot/joint3_position_controller/command std_msgs/Float64 "data: 2"``
