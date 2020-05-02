#!/bin/bash
rosrun throwing_robot_python initialize_robot.sh
rosrun throwing_robot_python trajectory.py
rosrun throwing_robot_python reset_to_zero.sh