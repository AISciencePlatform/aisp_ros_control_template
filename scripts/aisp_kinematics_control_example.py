#!/bin/python3
# Murilo Marques Marinho at the University of Tokyo.
# Author: Murilo M. Marinho, email: murilo@g.ecc.u-tokyo.ac.jp
import time
from dqrobotics import *  # Despite what PyCharm might say, this is very much necessary or DQs will not be recognized
import rospy
from sas_robot_kinematics import RobotKinematicsInterface

rospy.init_node('aisp_kinematics_control_example', disable_signals=True)
try:

    arm_interface_list = [RobotKinematicsInterface('/arm1_kinematics'),
                          RobotKinematicsInterface('/arm2_kinematics'),
                          RobotKinematicsInterface('/arm3_kinematics'),
                          RobotKinematicsInterface('/arm4_kinematics')]

    # Wait for all interfaces to be enabled
    all_interfaces_enabled = False
    while not all_interfaces_enabled:
        all_interfaces_enabled = True
        for arm_interface in arm_interface_list:
            if not arm_interface.is_enabled():
                all_interfaces_enabled = False
                break
        time.sleep(0.001)

    # Read initial values of each interface
    arm_counter = 1
    for arm_interface in arm_interface_list:
        print("****************************")
        print("***Initial info for arm {}***".format(arm_counter))
        print("****************************")
        print(arm_interface.get_pose())
        print(arm_interface.get_reference_frame())
        arm_counter = arm_counter + 1

    # Move each arm on their end-effectors' reference frame
    arm_counter = 1
    for arm_interface in arm_interface_list:
        print("Moving arm {}...".format(arm_counter))
        x = arm_interface.get_pose()
        xd = x * (1 + 0.5 * E_ * i_ * 0.1)
        arm_interface.send_desired_pose(xd)
        arm_interface.send_desired_interpolator_speed(0.1)
        arm_counter = arm_counter + 1

except KeyboardInterrupt:
    print("Interrupted by user")
