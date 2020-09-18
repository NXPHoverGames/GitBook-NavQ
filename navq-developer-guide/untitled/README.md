# ROS/ROS2

## ROS on NavQ

![](../../.gitbook/assets/image%20%2818%29.png)

ROS on NavQ will allow you to interface with sensors, control your drone using MAVROS, and more. To get started, follow the install guide below and then continue to the next sections.

## Install guide by OS

### HoverGames-Demo image

#### ROS 1 Install Guide \(Noetic\)

To install ROS, you need to be on the Demo image. You can follow the guide for installing ROS Noetic Ninjemys at [http://wiki.ros.org/noetic/Installation/Ubuntu](http://wiki.ros.org/noetic/Installation/Ubuntu)

#### ROS 2 Install Guide \(Foxy\)

To install ROS2,  you'll also need to be on the Demo image. You can follow the guide for installing ROS 2 Foxy Fitzroy at [https://index.ros.org/doc/ros2/Installation/Foxy/](https://index.ros.org/doc/ros2/Installation/Foxy/)

### HoverGames-BSP image

ROS Melodic is automatically installed on the HoverGames-BSP image. It includes MAVROS by default. You will need to do a little bit of setup, though, once you first boot your image.

Run the following commands to enable ROS on the HoverGames-BSP image:

```text
$ sudo rosdep init
$ rosdep update
$ source /opt/ros/melodic/setup.bash
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

You'll also want to download the following script and run it to install GPS geoids:

```text
$ wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
$ chmod a+x ./install_geographiclib_datasets.sh
$ ./install_geographiclib_datasets.sh
```

Now, you can continue with the ROS tutorials for setting up a build environment and installing your first package. We will go over this in the [next section](untitled.md).

