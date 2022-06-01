---
description: Connecting to the root console on NavQ using the USB--UART adapter
---

# Serial root console

The root console will allow monitoring of the board from initial boot. Since modern PCs don't tend to include serial ports anymore, a small FTDI USB-UART adapter is provided to convert the serial port to USB.

## Hardware connection

* Plug the 6 pin JST-GH cable from the  USB-UART converter into NavQ connector "UART2/I2C2"
* Plug the USB-UART into your pc like you would a dongle or memory stick
  * Your PC operating system should respond right away when it recognizes the USB-UART. On windows it will play a "usb connect sound"
  * There should be a red light illuminated on the USB-UART board (even when not plugged into the NAvQ)
* Follow the terminal configuration below and power on the NavQ

{% hint style="warning" %}
Troubleshooting Tip: If the COM port does not show in Device Manager or you don't hear the "usb connect sound" double check that the USB-C connector is fully plugged in and seated into the USB-UART adapter board.
{% endhint %}

{% hint style="warning" %}
Troubleshooting Tip: If the USB UART is not detected on your PC, in some instances you may need to download FDTI USB-UART driver software. It can be found here: [https://www.ftdichip.com/Drivers/D2XX.htm](https://www.ftdichip.com/Drivers/D2XX.htm)
{% endhint %}

## Terminal software connection

A terminal program will be required to communicate over the serial console. The following example is for a Windows 10 PC using the terminal program [PuTTY](https://www.chiark.greenend.org.uk/\~sgtatham/putty/latest.html).

{% hint style="success" %}
Default NavQ terminal settings are: 115200 Baud, N, 8, 1  (no Parity, no flow control)
{% endhint %}

In Windows 10 use Device manager to determine which COM port is assigned to the FTDI USB-UART serial adapter. The open PuTTY window shown below is the root console of the NavQ.

![In Windows 10,  Device manager can be used to determine which COM port is assigned](<../../.gitbook/assets/image (4).png>)

### Configuring PuTTY

There are several options for a terminal program that can be used. This example is for PuTTY on a Windows PC. Other programs and other hosts can be used.\
&#x20;\
Example using PuTTY to connect to the serial console via a USB-UART adapter. In this example the COM port was determined above by looking at Windows 10 Device manager.&#x20;

![Default baud rate is 115200](<../../.gitbook/assets/image (6).png>)

![You may also want to configure the serial console to turn off flow control](<../../.gitbook/assets/image (7).png>)
