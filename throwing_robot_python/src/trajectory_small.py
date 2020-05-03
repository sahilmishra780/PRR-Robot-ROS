#!/usr/bin/env python
import rospy
import math
import numpy as np
import time
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from math import sin,cos,atan2,sqrt,fabs
import subprocess


def trajectory():

	rospy.init_node('throw_the_ball', anonymous=True)
	
	# Define publisher
	pub2 = rospy.Publisher('/throwing_robot/joint2_position_controller/command', Float64, queue_size=10)
	pub3 = rospy.Publisher('/throwing_robot/joint3_position_controller/command', Float64, queue_size=10)
	pub4 = rospy.Publisher('/throwing_robot/joint4_position_controller/command', Float64, queue_size=10)
	
	# Small Trajectory
	value2 = np.linspace(-0.5*math.pi,0.45*math.pi,100)
	value3 = np.linspace(0,0.5*math.pi,100)
	# Define rate	
	print('Simulating the throwing motion......................')
	rate = rospy.Rate(200)
	i = 0
	while (not rospy.is_shutdown()) and i<len(value2):
		pub2.publish(value2[i])
		pub3.publish(value3[i])
		if i > 84:
			pub4.publish(0.04)
		i = i + 1 
		rate.sleep()
	
	time.sleep(5)

if __name__ == '__main__':
	try: trajectory()
	except rospy.ROSInterruptException: pass