# ROS2

![](../../../.gitbook/assets/image%20%2857%29.png)

## ROS2 Foxy Fitzroy Install Guide

{% hint style="info" %}
**NOTE: ROS2 is new, but we suggest you use it over ROS1, as ROS1 will be deprecated in the near future. You may run into issues with the ROS2 section of this Gitbook. If you have any issues with the guide, please email landon.haugh@nxp.com if external, or use Teams/Email if internal.  
  
MAVROS is not compatible with ROS2. MicroRTPS and PX4 ROS Com are the MAVROS equivalent for ROS2.**
{% endhint %}

Follow the guide at the link below to install ROS2 Foxy Fitzroy on your NavQ running the Demo image.

{% embed url="https://index.ros.org/doc/ros2/Installation/Foxy/Linux-Install-Debians/\#setup-sources" %}

{% hint style="warning" %}
**Note 1:** at _Setup Sources_ step you might get an error message by curl. To avoid this, run the following commands:
{% endhint %}

```text
sudo rm -rf /usr/lib/libcurl*
sudo apt install curl
```

{% hint style="warning" %}
**Note 2:** at _Install ROS2 package_ step, run the `ros-foxy-ros-base` installer, as the Desktop tools are not needed on NavQ:
{% endhint %}

```text
sudo apt install ros-foxy-ros-base
```

## 

