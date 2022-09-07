---
description: >-
  NavQ Linux companion computer platform with Vision for Mobile Robotics based
  on NXP i.MX 8M Mini SOC. Found at: https://nxp.gitbook.io/8mmnavq/
---

# NavQ

{% hint style="warning" %}
NavQ was used in HoverGames2 program and this document is supporting information. However it was not commercialized. The [NavQPlus (NavQ+](https://nxp.gitbook.io/8mpnavq/)) is the replacement upgraded version of NavQ available on NXP.com and through global distributors.

Note that some software and information here is still completely relevant to NavQPlus\
\
NavQ may also be referred to as: 8MMNavQ, MR-8MMNavQ or RDDRONE-8MMNavQ
{% endhint %}

![NavQ Mounted on HoverGames drone](<.gitbook/assets/image (37).png>)

{% hint style="success" %}
Also take a look at some of our other Gitbooks:

* [8M Plus NavQ](https://app.gitbook.com/o/-L9GLsni4p7csCR7QCJ8/s/-MQsLUVVC7cJOe9aVARC/) - newer supported version, available on NXP.com
* [HoverGames](https://app.gitbook.com/o/-L9GLsni4p7csCR7QCJ8/s/-L9GLtb-Tz\_XaKbQu-Al/) challenges
* [HoverGames Drone](https://nxp.gitbook.io/hovergames/)
* [NXP Cup](https://app.gitbook.com/o/-L9GLsni4p7csCR7QCJ8/s/-L9GLtaxrQtBdBRsFIJB/) - car/buggy racing series
* [UCANS32K146 UAVCAN/CAN Node](https://app.gitbook.com/o/-L9GLsni4p7csCR7QCJ8/s/-M7FJ\_hQKd8L0MNgduui/)
* [UCANS32K UAVCAN Node](https://nxp.gitbook.io/ucans32k146/)
* [RDDRONE-BMS772 Battery Management System](https://nxp.gitbook.io/rddrone-bms772/)


{% endhint %}

The 8MMNavQ is a small purpose built experimental Linux computer based on the [NXP i.MX 8M Mini SOC](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-processors:IMX8-SERIES). It is focused on the common needs of Mobile Robotics systems.

The system is built as a stack of boards, the top board being a SOM (system on module) containing the Processor, memory and other components with strict layout requirements, and where the secondary boards are relatively inexpensive (often 4 layer boards) and allows for versions with customization to be easily built.

\
This is a new set of boards and software enablement and will undergo several iterations. Our intent is to provide a "friendly Linux" with typical packages and additional tools included rather than the typical highly optimized and stripped down Linux found in deeply embedded products.

{% hint style="warning" %}
Please check for Linux updates regularly. Feedback and needs will be incorporated and updated as much as possible and reasonable.
{% endhint %}

{% hint style="success" %}
There is a [discussion forum here for questions specifically about NavQ](https://community.nxp.com/community/mobilerobotics/hovergames-drone-challenge/navq-8mmnavq-discussion)

And a general [HoverGames forum](https://community.nxp.com/community/mobilerobotics/hovergames-drone-challenge) here.
{% endhint %}

![](.gitbook/assets/IMG\_20200428\_181758.jpg)

The 8MMNavQ features:

1. NXP i.MX 8M Mini SOM with LPDDR4 DRAM and eMMC Flash.
2. A secondary board with SDCARD, Networking, MIPI-CSI (Camera) and MIPI-DSI (Display) interfaces
   * MIPI-DSI to HDMI converter
   * A Google Coral camera module
3. A third HGI (HoverGames Interposer board) with common interfaces and specific drone and rover interfaces which follow PX4 standards.

## Applications

The NavQ is suitable for many purposes, including generic robots and various vision systems.

* Drones, QuadCopters, Unmanned Aircraft, VTOL
* Rovers
* Road going Delivery Vehicles
* Robotic Lawnmowers
* Robotic Vacuum
* Flying vehicles (PX4)
* DIYRobotCars
* Marine vessels
* Camera and Vision processing modules
* Time of Flight (TOF) Cameras
* AI/ML inference
* Cellular gateway
* Vision systems in other applications
  * e.g a hospital bed monitor that detects if a patient is sitting up or at risk of falling out of bed.

Two specific complete developer tool examples are the [NXP HoverGames Drone](https://nxp.gitbook.io/hovergames), and the NXP-CUP car.

{% hint style="info" %}
The NavQ was prepared with the intention of working with and supporting the NXP HoverGames Drone program
{% endhint %}

### Software

The intent of the 8MMNavQ in HoverGames is to enable participants with a solution that allows them to harness common robotics packages and libraries such as:

* ROS
* OpenCV
* GStreamer
* Tensorflow
* pyeIQ
* And more!

The 8MMNavQ runs linux with a package manager, so you should be able to install the packages that you need to complete your projects successfully and efficiently.

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)\
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
