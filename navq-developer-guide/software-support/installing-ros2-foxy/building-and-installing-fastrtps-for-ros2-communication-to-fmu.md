# Building and Installing FastRTPS for ROS2 communication to FMU

## FastRTPS and the microRTPS Agent

FastRTPS and the microRTPS agent are needed on NavQ in order to bridge uORB topics from PX4 to ROS2 on NavQ over a UART or UDP connection. Follow the guide below to build and install these packages.

{% hint style="info" %}
**NOTE: FastRTPS and PX4 ROS Com work differently from MAVROS \(ROS1\). PX4 ROS Com subscribes to uORB topics rather than MAVLINK messages. See below for a diagram of how microRTPS and PX4 ROS Com works.**
{% endhint %}

![](../../../.gitbook/assets/image%20%2860%29.png)

Follow the link below for more details on microRTPS and PX4 ROS Com:

{% embed url="https://docs.px4.io/master/en/middleware/micrortps.html" %}

## Installing FastRTPS and PX4 ROS Com on NavQ

### Prerequisites

```text
~$ sudo apt update
~$ sudo apt install cmake python3-pip gradle python3-colcon-common-extensions gradle
~$ pip3 install --user pyros-genmsg
```

### FastRTPS installation

First, we will install the FastRTPS project from eProsima. Use the following commands below to do so:

```text
~$ mkdir src && cd src
~/src$ git clone --recursive https://github.com/eProsima/Fast-RTPS.git -b 1.8.x FastRTPS-1.8.2
~/src$ cd FastRTPS-1.8.2
~/src/FastRTPS-1.8.2$ mkdir build
~/src/FastRTPS-1.8.2$ cd build 
~/src/FastRTPS-1.8.2/build$ cmake -DTHIRDPARTY=ON -DSECURITY=ON .. 
~/src/FastRTPS-1.8.2/build$ make 
~/src/FastRTPS-1.8.2/build$ sudo make install
```

```text
cd ~/src
~/src$ git clone --recursive https://github.com/eProsima/Fast-RTPS-Gen.git -b v1.0.4 Fast-RTPS-Gen
~/src$ cd Fast-RTPS-Gen
~/src$ unset TERM
~/src/Fast-RTPS-Gen$ ./gradlew assemble
~/src/Fast-RTPS-Gen$ sudo su
~/src/Fast-RTPS-Gen# ./gradlew install
~/src/Fast-RTPS-Gen# exit
~/src/Fast-RTPS-Gen$
```

### px4\_ros\_com installation

Next, we will build and install the necessary software that will allow us to use ROS2 to communicate with the microRTPS bridge. First, run the following commands:

```text
$ cd ~/
~$ mkdir -p ~/px4_ros_com_ros2/src

~$ git clone https://github.com/PX4/px4_ros_com.git ~/px4_ros_com_ros2/src/px4_ros_com
~$ git clone https://github.com/PX4/px4_msgs.git ~/px4_ros_com_ros2/src/px4_msgs
```

{% hint style="danger" %}
**URGENT**: Building px4\_ros\_com requires a lot of ram. Enabling a swap disk is highly recommended. This will take up 1GB of space on your storage medium.
{% endhint %}

Run the following commands to enable a 1GB swapfile:

```text
$ sudo fallocate -l 1G /swapfile
$ sudo chmod 600 /swapfile
$ sudo mkswap /swapfile
$ sudo swapon /swapfile
$ sudo vim /etc/fstab
Insert: /swapfile swap swap defaults 0 0
$ sudo swapon --show
(make sure swap is active)
```

Now, build the workspace:

{% hint style="info" %}
This will take a long time to build on NavQ. In our experience, it takes anywhere from 45 minutes to an hour. Make sure you have a stable connection to NavQ over UART or SSH, and do not let the NavQ lose power!
{% endhint %}

```text
~$ ./px4_ros_com_ros2/src/px4_ros_com/scripts/build_ros2_workspace.bash
```

### Sourcing ROS2 bash files

In order to run all of your specific ROS2 software successfully, you must source the install/setup.bash files in each of your ROS2 workspace folders. Add the following lines to your .bashrc to do so:

```text
source /opt/ros/foxy/setup.bash
source ~/px4_ros_com_ros2/install/setup.bash
```

## Next steps

Continue to the next page to set up a `systemd` service that will automatically start the micrortps agent on your NavQ. The guide will also cover how to automatically start the client on the FMU.

