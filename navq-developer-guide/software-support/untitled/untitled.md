# Controlling your drone from NavQ using MAVROS

## MAVLink / MAVROS

![](<../../../.gitbook/assets/image (18).png>)

The 8MMNavQ can control your HoverGames drone by communicating with the RDDRONE-FMUK66 over MAVROS. A UART cable will be included in the kit that connects the UART3 port on the 8MMNavQ to the TELEM2 port on the RDDRONE-FMUK66.

{% hint style="info" %}
**NOTE: This page is for ROS1 only. MAVLINK and MAVROS are deprecated for ROS2 applications. ROS2 uses microRTPS and PX4 ROS Com in place of MAVROS.**
{% endhint %}

{% hint style="danger" %}
**NOTICE**: When running the off-board script, make sure that you confirm the landing zone for your drone in QGroundControl. The local position parameter in the offboard ROS node is set to x:0, y:0, z:2, which means it will hover at 2 meters above its landing zone. If the drone takes off from a position away from its landing zone, it will _quickly_ return to its landing zone and hover 2 meters above it. This is especially important to note if you turn the drone on indoors and then place it somewhere outside to take off. We don't want your drone to smack into a building!
{% endhint %}

## Prerequisites

### Set up TELEM2 on the FMU

Connect to your FMU over USB and open QGroundControl. Navigate to Settings -> Parameters -> MAVLink and set these parameters:

![](<../../../.gitbook/assets/image (19).png>)

Also, you'll need to make sure that the settings in Settings -> Parameters -> Serial look like this:

![](<../../../.gitbook/assets/image (20).png>)

## Offboard control guide

### MAVROS Offboard node example

A coding guide for the ROS node we will be using is located at the link below.

{% embed url="https://dev.px4.io/v1.9.0/en/ros/mavros_offboard.html" %}

This guide will help you install the ROS node outlined in the MAVROS Offboard Example.&#x20;

### Setting up your development environment

To start, you'll want to make sure that you have already set up a development environment for ROS. ROS has a guide on how to get a catkin workspace set up in the link below.

{% embed url="http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment" %}

Once you've completed that tutorial, you'll maybe want to add an extra line to your `~/.bashrc` so that your `devel/setup.bash` is always sourced when you open a new terminal:

```
$ echo "source /home/<user>/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

This will ensure that your development environment is properly set up when you open a new shell.

### Installing MAVROS specific packages

Follow the "binary installation" guide on the page below to install the necessary MAVROS packages from apt.

{% hint style="warning" %}
Make sure to use 'noetic' in place of 'kinetic' in the commands they give you on this page. Also, you do NOT need to follow the "Source Installation" section of the guide.
{% endhint %}

{% embed url="https://dev.px4.io/master/en/ros/mavros_installation.html#binary-installation-debian--ubuntu" %}

### Creating a new package

To create our first ROS package, we will want to navigate to our catkin workspace's `src` folder and run the following command:

```
$ catkin_create_pkg offb roscpp mavros_msgs geometry_msgs
```

This command will create a new package folder named `offb` and will add the dependencies `roscpp`, `mavros_msgs`, and `geometry_msgs` to the 'CMakeLists.txt' and 'package.xml' files. Next, you'll want to take the code from the PX4 MAVROS example and create a file named offb\_node.cpp in the `src/` folder in the `offb` package. Your directory structure should now look like this:

```
navq@imx8mmnavq:~/catkin_ws/src/offb$ tree
.
├── CMakeLists.txt
├── include
│   └── offb
├── package.xml
└── src
    └── offb_node.cpp

3 directories, 3 files
navq@imx8mmnavq:~/catkin_ws/src/offb$
```

### Editing CMakeLists

In order to build your ROS package, you'll need to make some edits to CMakeLists.txt so the catkin build system knows where your source files are. Two edits need to be made.&#x20;

The first edit is to add your executable to CMakeLists. Your executable should be named offb\_node.cpp. Uncomment line 136 to add it:

```
136 add_executable(${PROJECT_NAME}_node src/offb_node.cpp)
```

The second edit is link your target libraries (roscpp, mavros\_msgs, and geographic\_msgs). Uncomment lines 149-151 to do so:

```
149 target_link_libraries(${PROJECT_NAME}_node
150   ${catkin_LIBRARIES}
151 )
```

And that's all you need to do for now to set up your workspace!

### Building your ROS node

To build your ROS node, return to the root of your `catkin_ws/` directory and run:

```
$ catkin_make && catkin_make install
```

### Running your ROS node

To run our ROS node, we need to make sure that MAVROS is running. On the NavQ, run the following command:

```
$ roslaunch mavros px4.launch fcu_url:='/dev/ttymxc2:921600' &
```

This will start `roscore` and the `mavros` node with a pointer to the UART port `/dev/ttymxc2` at a 921600 baud rate. To run the ROS node we created, run the following in an ssh terminal:

```
$ rosrun offb offb_node &
```

and your drone should take off to an altitude of 2 meters!
