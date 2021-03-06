---
description: '[WIP]'
---

# Battery LED w/ Teensy LC

## Introduction

This "Project Guide" is written to show some of the capabilites of NavQ. In conjunction with a Teensy LC and a strip of WS2812B LEDs, you can add a forward-facing battery indicator light to your drone.

![The battery on my drone is quite low!](../../../.gitbook/assets/pic.jpg)

## Prerequisites

### Software

The software needed to run this project on your NavQ is as follows:

1. ROS Noetic
2. MAVROS

You can install this software using the guides here:

{% page-ref page="../../software-support/untitled/" %}

{% page-ref page="../../software-support/untitled/untitled.md" %}

### Hardware

The hardware needed is the same as the hardware from the I2C guide here:

{% page-ref page="./" %}

## Code

At the moment, we're just going to paste the code here, and a more detailed guide will be written later.

### Teensy code

This code should be uploaded to the Teensy using the Arduino IDE. 

{% file src="../../../.gitbook/assets/batt\_led.zip" caption="Teensy batt\_led code" %}

### NavQ code

The ROS node should be placed in the home folder \('/home/navq/'\)

{% file src="../../../.gitbook/assets/batt\_led.py" caption="ROS node" %}

The service file should be located in /etc/systemd/system/.

{% file src="../../../.gitbook/assets/batt\_led.service" caption="\"systemd\" service file" %}

The Launch script should be located in /usr/local/bin/.

{% file src="../../../.gitbook/assets/batt\_led.sh" caption="Launch script" %}

### Making the ROS node run on boot

Once all of the necessary files are placed in their respective directories, you need to make the systemd service run at boot. To do this, run in the terminal:

```text
$ sudo systemctl enable batt_led
```

