---
description: Ensure your NavQ is working correctly with these fixes
---

# HoverGames-Demo Bugs/Fixes

## Overview

Currently, the HoverGames-Demo image is in a beta state. Over time we will be improving the image by fixing bugs and including even more software so that it's more of an out-of-the-box experience. Here are some of the current fixes at the moment to get a working system.

{% hint style="info" %}
These fixes are for the build on 7/24/2020. This page will be updated for each new release.
{% endhint %}

## Quick Workarounds

* Bluetooth is not working due to an issue with hciuart.service.
  * Workaround: No workaround at the moment.
* WiFi sometimes does not automatically connect to the last WiFi network after reboot.
  * Workaround: Open connmanctl, run `disable wifi`, and reconnect using the instructions in the Quick Start Guide.

## Linux Device Tree

Currently the patches for the linux device tree in our build system are not working. To fix hardware issues like the camera, HDMI, and WiFi, you'll need to replace the \*.dtb file on the boot partition of your SD card. You'll need the following file to follow the steps below:

{% file src="../.gitbook/assets/imx8mm-cube.dtb" caption="imx8mm-cube.dtb" %}

### Steps

1. Insert your SD card into your computer
2. Open the `boot` partition that is mounted by default.
3. Drag and drop the `imx8mm-cube.dtb` file into the boot partition.
4. Boot your NavQ. Quickly connect to it using a serial monitor such as PuTTY.
5. Press `Enter` repeatedly after it boots to bring up the `u-boot=>` prompt.
6. In the `u-boot=>` prompt, run the following commands:

```text
u-boot=>setenv fdt_file imx8mm-cube.dtb
u-boot=>saveenv
u-boot=>boot
```

Once you have completed these steps, you should be good to go until you reflash your SD card with a new image.

## Setting timezone

Setting the timezone on your NavQ is necessary to ensure the `apt` package manager works. First, you'll need to locate the correct timezone file at `/usr/share/zoneinfo`. There should be a folder for your country and a file in that folder for the closest city to you.

```text
$ rm -f /etc/localtime
$ ln -sf /usr/share/zoneinfo/<country>/<city> /etc/localtime
```

For example, if you're in Central Time USA, you'd use the following commands:

```text
$ rm -f /etc/localtime
$ ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime
```

Now, you can run `sudo apt update` and `sudo apt upgrade` to get your system up to date.

