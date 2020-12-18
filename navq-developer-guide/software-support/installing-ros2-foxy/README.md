# ROS2

![](../../../.gitbook/assets/image%20%2857%29.png)

## ROS2 Foxy Fitzroy Install Guide

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

