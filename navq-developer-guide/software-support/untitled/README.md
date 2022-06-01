# ROS1

## ROS on NavQ

![](<../../../.gitbook/assets/image (16).png>)

ROS on NavQ will allow you to interface with sensors, control your drone using MAVROS, and more. To get started, follow the install guide below and then continue to the next sections.

{% hint style="info" %}
**NOTE: ROS1 support is good, but the Mobile Robotics team at NXP's focus is on ROS2. There is a lot more documentation on ROS1 than ROS2, but ROS2 may be easier to use in the long run. We suggest that you do not cross-polinate with ROS, i.e. only use ROS1 or ROS2, not both. Keep in mind that any documentation under the ROS1 section is for ROS1 only, and vice versa.**
{% endhint %}

## Install guide by OS

### HoverGames-Demo image

{% hint style="info" %}
NOTE: HoverGames participants should be using the Demo image. If you flashed your NavQ with the image from the HoverGames website, or if you're using the image that came installed on the SD Card included in your kit, you're using the Demo image.&#x20;
{% endhint %}

{% hint style="warning" %}
When you install ROS Noetic on your NavQ, make sure to install the base version of ROS and not the desktop version. If you install the desktop version, critical gstreamer packages for NavQ can be overwritten and therefore become non-functional.
{% endhint %}

To install ROS, you need to be on the Demo image. You can follow the guide for installing ROS Noetic Ninjemys at [http://wiki.ros.org/noetic/Installation/Ubuntu](http://wiki.ros.org/noetic/Installation/Ubuntu)

### HoverGames-BSP image

{% hint style="info" %}
If you're using NavQ comercially and are running the HoverGames-BSP image, you'll follow these steps.
{% endhint %}

ROS Melodic is automatically installed on the HoverGames-BSP image. It includes MAVROS by default. You will need to do a little bit of setup, though, once you first boot your image.

Run the following commands to enable ROS on the HoverGames-BSP image:

```
$ sudo rosdep init
$ rosdep update
$ source /opt/ros/melodic/setup.bash
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

You'll also want to download the following script and run it to install GPS geoids:

```
$ wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
$ chmod a+x ./install_geographiclib_datasets.sh
$ ./install_geographiclib_datasets.sh
```

Now, you can continue with the ROS tutorials for setting up a build environment and installing your first package. We will go over this in the [next section](untitled.md).
