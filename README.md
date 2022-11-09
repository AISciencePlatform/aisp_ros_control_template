# ros-noetic-sas-robot-kinematics

## Installation on Ubuntu 20.04 x64 LTS

### 1. Pre-requisites

```shell
sudo apt update && sudo apt upgrade -y
sudo apt install git terminator cmake python3-pip libeigen3-dev mesa-common-dev libglu1-mesa-dev curl jq -y
python3 -m pip install scipy
```

### 2. [DQ Robotics library](https://dqrobotics.github.io/) (development PPA)

```shell
sudo add-apt-repository ppa:dqrobotics-dev/development -y
sudo apt-get update
sudo apt-get install libdqrobotics*
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


## Set the enviroment variables for your particular system


|Variable| Meaning |
|---|---|
|`VREP_IP`|CoppeliaSim's computer IP. Usually Master-PC IP.|
|`ROBOT_1_JSON_PATH`|Usually `/home/moonshot/git/moonshot_robot_pc/catkin_ws/src/moonshot_control/robots/aisp_cobotta_robot_1.json`|
|`ROBOT_2_JSON_PATH`|Usually `/home/moonshot/git/moonshot_robot_pc/catkin_ws/src/moonshot_control/robots/aisp_cobotta_robot_2.json`|
|`ROBOT_3_JSON_PATH`|Usually `/home/moonshot/git/moonshot_robot_pc/catkin_ws/src/moonshot_control/robots/aisp_vs050_robot_1.json`|
|`ROBOT_4_JSON_PATH`|Usually `/home/moonshot/git/moonshot_robot_pc/catkin_ws/src/moonshot_control/robots/aisp_vs050_robot_2.json`|

Example:
```shell
echo "export VREP_IP=127.0.0.1" >> ~/.bashrc
echo 'export ROBOT_1_JSON_PATH="/home/moonshot/git/moonshot_robot_pc/catkin_ws/src/moonshot_control/robots/aisp_cobotta_robot_1.json"' >> ~/.bashrc
echo 'export ROBOT_2_JSON_PATH="/home/moonshot/git/moonshot_robot_pc/catkin_ws/src/moonshot_control/robots/aisp_cobotta_robot_2.json"'  >> ~/.bashrc
echo 'export ROBOT_3_JSON_PATH="/home/moonshot/git/moonshot_robot_pc/catkin_ws/src/moonshot_control/robots/aisp_vs050_robot_1.json"' >> ~/.bashrc
echo 'export ROBOT_4_JSON_PATH="/home/moonshot/git/moonshot_robot_pc/catkin_ws/src/moonshot_control/robots/aisp_vs050_robot_2.json"'  >> ~/.bashrc
```
