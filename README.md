# PRR robot with 2-finger end effector to throw object
Course project for MEEN 612, Sping 2020
<br>
Objective: Design a robot capable of throwing objects into different targets. Simulate using ROS and Gazebo.
<br>
Texas A&M University
<br><br>
Launch robot in Rviz:<br>
`` roslaunch throwing_robot throwing_robot_rviz.launch``
<br><br>
Launch robot in Gazebo:<br>
``roslaunch throwing_robot_gazebo throwing_robot.launch ``
<br><br>
Launch Joint Position Controller:<br>
``roslaunch throwing_robot_control throwing_robot_control.launch ``
<br><br>
Move robot via CLI:<br>
``rostopic pub -1 /throwing_robot/joint1_position_controller/command std_msgs/Float64 "data: 0.3"``<br>
``rostopic pub -1 /throwing_robot/joint2_position_controller/command std_msgs/Float64 "data: 0.5"``<br>
``rostopic pub -1 /throwing_robot/joint3_position_controller/command std_msgs/Float64 "data: 2"``<br>

## Run Throwing Simulation:<br>
In a new terminal<br>
``roslaunch throwing_robot_gazebo throwing_robot.launch``
<br><br>
Now in a new terminal <br>
``roslaunch throwing_robot_control throwing_robot_control.launch``
<br><br>
Unpause the simulation in Gazebo and in a new terminal run<br>
``rosrun throwing_robot_python simulate_throw.sh``
