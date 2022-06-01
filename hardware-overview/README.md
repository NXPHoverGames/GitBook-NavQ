# Hardware Overview

## NavQ SOM

The SOM includes the processor, RAM, memory, and WiFi chip for the NavQ.

![](<../.gitbook/assets/IMG\_4105 (1).jpg>)

### Summary

The NavQ SOM (System on Module) contains the brains of the NavQ. On this board, we have our i.MX 8M Mini processor, 2GB of LPDDR4 memory, 16GB of eMMC flash storage, and a QCA9377 WiFi AC + BT 5.0 chip. There are connectors on the bottom of this board that allow for modularity.

### Components

| Name                       | Details                                 |
| -------------------------- | --------------------------------------- |
| NXP i.MX 8M Mini Processor | Quad ARM Cortex-A53, Cortex-M4 @ 1.8GHz |
| LPDDR4 Memory              | 2GB                                     |
| eMMC Flash                 | 16GB                                    |
| Qualcomm WiFi/BT           | 802.11ac + BT 5.0                       |

### Dimensions

The NavQ's dimensions are 3" W x 2" L x 7/16" H.&#x20;

## Media Board

![](../.gitbook/assets/IMG\_4108.jpeg)

### **Summary**

The Media Board consists of an SD Card slot, MIPI connectors for a camera serial interface as well as a display serial interface, and a PCIe connector.&#x20;

### **Components**

| **Name**     | Details                               |
| ------------ | ------------------------------------- |
| SD Card slot | MicroSD card compatible               |
| MIPI CSI     | Google Coral Camera connection        |
| MIPI DSI     | MIPI to HDMI adapter for full desktop |

Image of Google Coral Camera + MIPI to HDMI Adapter:

![](../.gitbook/assets/IMG\_4109.jpeg)

### Google Coral Camera Dimensions

The Google Coral Camera dimensions are 25mm x 25mm, as shown in the tech specs here:&#x20;

[https://coral.ai/products/camera/#description](https://coral.ai/products/camera/#description)

## Hovergames Interposer Board (HGI)

![](../.gitbook/assets/IMG\_4110.jpg)

### Summary

The HoverGames Interposer Board (HGI) is the final board in the stack and has a multitude of I/O for your needs in HoverGames. Connect sensors, switches, and LEDs to the NavQ using the HGI to drastically improve your drone system, and even control your drone using NavQ using offboard control with MAVROS.

### Components

| Name                          | Details                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------- |
| UART                          | 3 UART ports for serial communication through JST-GH connectors.                |
| USB-C                         | Powers the board and serves as an interface for flashing new firmware.          |
| MicroUSB                      | Connect USB devices to this port such as keyboards and mice. USB hub included.  |
| SPI                           | JST-GH connector for SPI interface.                                             |
| Hirose IX Industrial Ethernet | IX Industrial ethernet cable is included.                                       |
| 2 Wire Automotive Ethernet    | JST-GH connector for 2-wire ethernet as well as GPIO.                           |
| JTAG                          | Pads are available for JTAG. You may solder your own JTAG connector.            |
| Boot Mode Switches            | You can use these switches to boot from eMMC or SD card, or boot into fastboot. |
| GPIO                          | Through-hole points for GPIO headers.                                           |
| RGB LED                       | WS2811 RGB LED available for status                                             |
