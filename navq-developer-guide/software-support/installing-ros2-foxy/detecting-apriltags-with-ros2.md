---
description: '[WORK IN PROGRESS]'
---

# Detecting AprilTags with ROS2

## Overview

{% hint style="danger" %}
NOTE: This guide is currently a work in progress. Some details may not be finished. 
{% endhint %}

In this section, we will guide you through the process needed to detect AprilTags on your NavQ. There are a few things that need to be done to accomplish this:

1. Install ROS2 image tools
2. Build and install AprilTag detection nodes
3. Calibrate the camera on your NavQ using a checkerboard pattern
4. Run!

## Prerequisites

Before we start, you will need a few things:

### Checkerboard

To create a checkerboard for camera calibration, download this PDF: [https://www.mrpt.org/downloads/camera-calibration-checker-board\_9x7.pdf](https://www.mrpt.org/downloads/camera-calibration-checker-board_9x7.pdf)

### Desktop Setup

In order to calibrate the camera, you will need to set up your NavQ with a mouse, keyboard, and monitor. Use the included microUSB hub and HDMI connector to do so.

## Installing required ROS2 software

Install the following packages with the `apt` package manager by running the commands below:

```text
$ sudo apt install ros-foxy-cv-bridge \
ros-foxy-image-tools \
ros-foxy-image-transport \
ros-foxy-image-transport-plugins \
ros-foxy-image-pipeline \
ros-foxy-camera-calibration-parsers \
ros-foxy-camera-info-manager \
ros-foxy-launch-testing-ament-cmake 
```

Once that is finished, move on to the next step.

## Calibrating the camera

{% hint style="info" %}
This section is a consolidation of the specific commands for the NavQ. If you run into any issues with this section of the guide, email landon.haugh@nxp.com and refer to the official guide: [https://navigation.ros.org/tutorials/docs/camera\_calibration.html](https://navigation.ros.org/tutorials/docs/camera_calibration.html)
{% endhint %}

Hook up your NavQ to a monitor with the provided HDMI cord and connect a USB mouse + keyboard through the included microUSB hub. Open the terminal by clicking the icon at the top left of the screen and open the bash shell by running:

```text
$ bash
```

Have your printed checkerboard ready in a well lit environment and run the camera calibration software by running the following commands:

```text
# Start publishing camera images to ROS2 topic /camera/image_raw
$ ros2 run image_tools cam2image --ros-args -p device_id:=0 -p width:=640 -p height:=480 -r /image:=/camera/image_raw > /dev/null 2>&1 &
# Start the camera calibration software
$ ros2 run camera_calibration cameracalibrator --size 7x9 --square 0.02
```

Now use the link in the note above to run through calibarating the camera.

## Detecting AprilTags

### Building apriltag\_msgs

A prerequisite for the `apriltag_ros` node is `apriltag_msgs`. Clone the repo and build it by running these commands:

```text
$ git clone https://github.com/christianrauch/apriltag_msgs
$ cd apriltag_msgs
$ colcon build
```

Make sure to source the install/setup.bash file so that apriltag\_msgs can see it when being built.

### Building the apriltag\_ros node

First, in order to detect AprilTags, we need to build the `apriltag_ros` node written by christianrauch. You can clone his repository by using this git repo:

```text
$ git clone https://github.com/christianrauch/apriltag_ros
```

To make his repo work with ROS2 Foxy, you will need to make a small change in the CMakeLists.txt file. Go to line 26 in that file and delete the `apriltag::` token in the `AprilTagNode apriltag::apriltag` part.

Next, you'll want to save that file and run `colcon build` in the apriltag\_ros folder. Once it is done building, you'll want to source the install/setup.bash file. Add this line to your .bashrc:

```text
source /home/navq/<apriltag_ros folder>/install/setup.bash
```

### Creating a new package to concatenate camera information to each camera frame

In order to make the apriltag\_ros node work, we need to make sure that camera info messages are being sent in sync with each camera frame published by the image\_tools `cam2image` node. We have written an example node that does just that. You can download it here:

{% hint style="info" %}
Coming soon
{% endhint %}

You will need to replace the matricies in the node file to match your camera calibration parameters. Once you have done that, make sure to build and install the node and source the install/setup.bash file.



