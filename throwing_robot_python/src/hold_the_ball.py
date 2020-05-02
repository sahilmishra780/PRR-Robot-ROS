#!/usr/bin/env python
import rospy
import math
import numpy as np
import time
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from math import sin,cos,atan2,sqrt,fabs


def hold_the_ball():

	rospy.init_node('hold_the_ball', anonymous=False)
	
	# Define publisher
	pub1 = rospy.Publisher('/throwing_robot/joint4_position_controller/command', Float64, queue_size=10)

	# Define rate	
	rate = rospy.Rate(200)
	while (not rospy.is_shutdown()):
		pub1.publish(0.0)
		rate.sleep()


if __name__ == '__main__':
	try: hold_the_ball()
	except rospy.ROSInterruptException: pass