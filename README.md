# ros-noetic-sas-robot-kinematics

## Installation on Ubuntu 20.04 x64 LTS

### 1. Pre-requisites

```shell
sudo apt update && sudo apt upgrade -y
sudo apt install qt5-default git terminator cmake python3-pip libeigen3-dev mesa-common-dev libglu1-mesa-dev curl jq -y
python3 -m pip install scipy
```

### 2. [DQ Robotics library](https://dqrobotics.github.io/) (development PPA)

```shell
sudo add-apt-repository ppa:dqrobotics-dev/development -y
sudo apt-get update
sudo apt-get install libdqrobotics*
```

```shell
python3 -m pip install --user --pre dqrobotics
```

### 3. [ROS Noetic Ninjemys](http://wiki.ros.org/noetic/Installation/Ubuntu)

```shell
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-noetic-ros-base ros-noetic-pybind11-catkin -y
```

```shell
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

### 4. Catkin tools

```shell
sudo python3 -m pip install git+https://github.com/catkin/catkin_tools.git
```

### 5. [qpOASES](https://github.com/coin-or/qpOASES)
```shell
cd ~/Downloads
git clone https://github.com/coin-or/qpOASES.git
cd qpOASES
sed -i -e 's/option(BUILD_SHARED_LIBS "If ON, build shared library instead of static" OFF)/option(BUILD_SHARED_LIBS "If ON, build shared library instead of static" ON)/g' CMakeLists.txt
mkdir build
cd build
cmake ..
make -j20
sudo make install
sudo ldconfig
```


## [Install SmartArmStack](https://github.com/SmartArmStack/smart_arm_stack_researchonly/releases/tag/v22.11.8150150)

```shell
wget https://raw.githubusercontent.com/SmartArmStack/smart_arm_stack/main/install.sh
sh install.sh
```

## Clone this repository

```shell
cd ~/catkin_ws/src
git clone https://github.com/AISciencePlatform/aisp_ros_control_template.git
```

## Set the enviroment variables for your particular system


|Variable| Meaning |
|---|---|
|`VREP_IP`|CoppeliaSim's computer IP.|
|`ROBOT_1_JSON_PATH`|Usually `/home/user_name/catkin_ws/src/aisp_ros_control_template/robots/aisp_cobotta_robot_1.json`|
|`ROBOT_2_JSON_PATH`|Usually `/home/user_name/catkin_ws/src/aisp_ros_control_template/robots/aisp_cobotta_robot_2.json`|
|`ROBOT_3_JSON_PATH`|Usually `/home/user_name/catkin_ws/src/aisp_ros_control_template/robots/aisp_vs050_robot_1.json`|
|`ROBOT_4_JSON_PATH`|Usually `/home/user_name/catkin_ws/src/aisp_ros_control_template/robots/aisp_vs050_robot_2.json`|

Example:

In this example the user is 'ubuntu' and the aisp_ros_control_template folder is in '/home/ubuntu/catkin_ws/src/aisp_ros_control_template'. Furthermore, the CoppeliaSim scene is on the same computer.

```shell
echo "export VREP_IP=127.0.0.1" >> ~/.bashrc
echo 'export ROBOT_1_JSON_PATH="/home/ubuntu/catkin_ws/src/aisp_ros_control_template/robots/aisp_cobotta_robot_1.json"' >> ~/.bashrc
echo 'export ROBOT_2_JSON_PATH="/home/ubuntu/catkin_ws/src/aisp_ros_control_template/robots/aisp_cobotta_robot_2.json"'  >> ~/.bashrc
echo 'export ROBOT_3_JSON_PATH="/home/ubuntu/catkin_ws/src/aisp_ros_control_template/robots/aisp_vs050_robot_1.json"' >> ~/.bashrc
echo 'export ROBOT_4_JSON_PATH="/home/ubuntu/catkin_ws/src/aisp_ros_control_template/robots/aisp_vs050_robot_2.json"'  >> ~/.bashrc
```



### Open the CoppeliaSim scene

Follow the instructions [here](https://github.com/AISciencePlatform/aisp_coppeliasim_scenes/blob/main/README.md) to set up CoppeliaSim and open the scene.

![Screenshot 2022-11-10 125810](https://user-images.githubusercontent.com/23158313/200997347-1e8ea0d3-edbf-434e-ba22-19b27415e537.png)

### Start the simulation

###

Open a new terminal and type:

```shell
cd ~/catkin_ws/
source devel/setup.bash
roslaunch aisp_ros_control_template run_simulation.launch --screen
```

###

Open a new terminal and type:

```shell
cd ~/catkin_ws/
source devel/setup.bash
rosrun aisp_ros_control_template aisp_kinematic_control_example.py
```
