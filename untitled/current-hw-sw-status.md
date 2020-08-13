---
description: Rolling updates on the status of hardware and software
---

# Current HW SW status

## Hardware

* 5/10/2020 - Production Hardware in manufacturing

## Software

As of July 17 2020:

* &lt;u&gt; 20.04 image is fully working with package manager, ROS, UART, WiFi, etc.

As of July 8 2020:

* An &lt;u&gt; 19.10 image was built and tested with the Google Coral camera. A picture was successfully taken using this image. A working image with the following features should be finished Soon™:
  * Gstreamer + OpenCV w/ working camera
  * UART communication to NXP RDDRONE-FMUK66 for Offboard control using MAVROS \(not from\)
  * WiFi connection for communication with NavQ
    * Would enable streaming video back to base station for processing as well as creating in-house user interfaces for controlling the HoverGames drone

As of July 7 2020:

* NXP Yocto Debian image 
* 3rd party &lt;u&gt;-like image
  * Works, can install ROS/OpenCV, but most hardware doesn't work \(camera, hdmi, etc\)
* 3rd party Debian image
* EmCraft Linux image
  * Works, has desktop, has OpenCV/Gstreamer, no ROS 

