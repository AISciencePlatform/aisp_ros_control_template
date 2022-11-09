cmake_minimum_required(VERSION 3.1)
project(aisp_ros_control_template)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    sas_datalogger
    sas_common
    sas_conversions
    sas_clock
    sas_robot_driver
    sas_robot_kinematics
    sas_robot_kinematics_constrained_multiarm
    )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
    #INCLUDE_DIRS include
    #LIBRARIES cobotta_kinematics
    CATKIN_DEPENDS 
    roscpp 
    rospy
    sas_datalogger
    sas_common
    sas_conversions
    sas_clock
    sas_robot_driver
    sas_robot_kinematics
    sas_robot_kinematics_constrained_multiarm
    #  DEPENDS system_lib
    )

