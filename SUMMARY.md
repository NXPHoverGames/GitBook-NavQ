# Table of contents

* [NavQ](README.md)
* [NavQ and HoverGames](untitled/README.md)
  * [NavQ Examples with NXPHoverGames Drone](untitled/navq-examples-with-nxphovergames-drone.md)
  * [Current HW SW status](untitled/current-hw-sw-status.md)
* [Hardware Overview](hardware-overview/README.md)
  * [Pinouts and Connector info](hardware-overview/pinouts-and-connector-info.md)
  * [Schematics](hardware-overview/schematics.md)
* [Disclaimers](disclaimers.md)
* [Revisions and Errata](revisions-and-errata.md)
* [NavQ add on modules](navq-add-on-modules/README.md)
  * [RDDRONE-T1ADAPT](navq-add-on-modules/100baset1-2-wire-automotive-ethernet-media-converter.md)
  * [5" LCD panel module](navq-add-on-modules/5-lcd-panel-module.md)
  * [LTE Cat M1 modem](navq-add-on-modules/lte-cat-m1-modem.md)
* [Ordering Info](ordering-info.md)

## Getting Started

* [Quick start Guide](getting-started/quickstart/README.md)
  * [Power input](getting-started/quickstart/power-input.md)
  * [Power Cables](getting-started/quickstart/power-cables.md)
  * [Downloading & Flashing the HoverGames-Demo Linux Image](getting-started/quickstart/flash-sd-card-with-linux-image.md)
  * [Expand space on SD card/eMMC](getting-started/quickstart/expand-space-on-sd-card.md)
  * [Serial root console](getting-started/quickstart/serial-root-console.md)
  * [Mounting NavQ on HoverGames Drone](getting-started/quickstart/mounting-navq-on-hovergames-drone.md)
* [HoverGames-Demo Bugs/Fixes](getting-started/hovergames-demo-fixes.md)

## User Guide

* [Nano Editor](user-guide/nano-editor.md)
* [Setting the NavQ hostname](user-guide/proposal-for-hostname.md)
* [MavLink Specific details](user-guide/mavlink-specific-details/README.md)
  * [mavlink-router](user-guide/mavlink-specific-details/installing-mavlink-router.md)
  * [Running MavLink over T1 Ethernet](user-guide/mavlink-specific-details/running-mavlink-via-t1-ethernet.md)
* [Miscellaneous Linux Commands](user-guide/miscellaneous-linux-commands/README.md)
  * [GPS Time](user-guide/miscellaneous-linux-commands/gps-time.md)
  * [Linux: Get the core temperature](user-guide/miscellaneous-linux-commands/linux-get-the-core-temperature.md)

## NavQ Developer Guide

* [Building a Linux image for NavQ](navq-developer-guide/building-a-linux-image-for-navq.md)
* [Communication Protocols](navq-developer-guide/communication-protocols/README.md)
  * [GPIO](navq-developer-guide/communication-protocols/controlling-gpio-in-linux-on-navq.md)
  * [SPI](navq-developer-guide/communication-protocols/spi.md)
  * [I2C](navq-developer-guide/communication-protocols/i2c/README.md)
    * [Battery LED w/ Teensy LC](navq-developer-guide/communication-protocols/i2c/battery-led-w-teensy-lc.md)
  * [CAN](navq-developer-guide/communication-protocols/can-communication.md)
* [Software Support](navq-developer-guide/software-support/README.md)
  * [Package Management](navq-developer-guide/software-support/package-management.md)
  * [ROS1](navq-developer-guide/software-support/untitled/README.md)
    * [Controlling your drone from NavQ using MAVROS](navq-developer-guide/software-support/untitled/untitled.md)
  * [ROS2](navq-developer-guide/software-support/installing-ros2-foxy/README.md)
    * [Building and Installing FastRTPS for ROS2 communication to FMU](navq-developer-guide/software-support/installing-ros2-foxy/building-and-installing-fastrtps-for-ros2-communication-to-fmu.md)
    * [Auto-start microRTPS client/agent on FMU/NavQ](navq-developer-guide/software-support/installing-ros2-foxy/autostart-micrortps-client-via-systemd-on-navq.md)
    * [Detecting AprilTags with ROS2](navq-developer-guide/software-support/installing-ros2-foxy/detecting-apriltags-with-ros2.md)
  * [GStreamer](navq-developer-guide/software-support/gstreamer/README.md)
    * [Streaming Video to QGroundControl using NavQ over WiFi](navq-developer-guide/software-support/gstreamer/streaming-video-to-qgroundcontrol-using-navq-over-wifi.md)
    * [Ad-Hoc Streaming using Mobile Hotspot](navq-developer-guide/software-support/gstreamer/ad-hoc-streaming-using-mobile-hotspot.md)
  * [OpenCV](navq-developer-guide/software-support/opencv.md)
  * [pyeIQ](navq-developer-guide/software-support/pyeiq.md)
  * [Gazebo](navq-developer-guide/software-support/gazebo.md)

---

* [HoverGames Gitbook](https://nxp.gitboook.io/hovergames)
* [HoverGames](https://www.hovergames.com)

## Archive

* [Old Fixes](archive/old-fixes.md)
* [Developer Quick Start Guide](archive/developer-quick-start-guide.md)
* [Flashing the NavQ with 18.04 rootfs \(internal\)](archive/flashing-the-navq-with-ubuntu-18.04-rootfs.md)

