---
description: '[WORK IN PROGRESS]'
---

# Flash SD card/eMMC with Linux image

## Preparing the image

The HoverGames images come as a .bz2 compressed archive. To decompress this image, you'll need to use a program like 7zip on Windows, use the bunzip2 command on Linux, or double click the archive on Mac.

## Flashing the image to eMMC or SD card using UUU

NXP has a tool for flashing i.MX hardware called UUU \(Universal Update Utility\). You can download UUU from here:

{% embed url="https://github.com/NXPmicro/mfgtools/releases" %}

If you're on Windows, you'll want to download the `uuu.exe` file, and if you're on Linux, you'll want to download the `uuu` file.

You'll also want to download the image file. It is hosted here:

{% embed url="https://www.hovergames.com/EULA" %}

As well as the bootloader file:

{% hint style="warning" %}
NOTE: This file is only needed for flashing with UUU to the eMMC/SD Card. If you want to flash your SD Card with dd or Win32DiskImager, this file is not needed.
{% endhint %}

{% embed url="https://drive.google.com/file/d/1AYRxy-okiu8\_9\_9EmC5DWbCq-hZk2PKw/view?usp=sharing" %}



### Step 1

Flip the DIP switches on your NavQ to put it into USB flashing mode. Here is an image that shows how to do so:

![](../../.gitbook/assets/image%20%2844%29.png)

{% hint style="info" %}
Once you're done flashing, you can use this image to select the boot mode: eMMC or SD card.
{% endhint %}

### Step 2

Connect your NavQ using the included USB-C cable to your computer. You should recieve a message on your computer that it has been connected. To make sure the NavQ is connected, you can run the UUU program with the `-lsusb` flag and you should see an output similar to this:

```text
Linux
-----
$ ./uuu -lsusb

Windows
-------
$ .\uuu.exe -lsusb

Output
------
uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.3.191-0-g4fe24b9

Connected Known USB Devices
        Path     Chip    Pro     Vid     Pid     BcdVersion
        ==================================================
        2:7      MX8MM   SDP:    0x1FC9 0x0134   0x0101
```

### Step 3

You can flash both the SD card and the eMMC using this tool. The keyword for flashing the SD card is `sd_all`, while the keyword for flashing the eMMC is `emmc_all`. The command to flash your board is outlined below:

```text
Linux
-----
$ ./uuu -b emmc_all <.bin-flash_navq> <.wic.bz2 OR .img>

Windows
-------
$ .\uuu.exe -b emmc_all <.bin-flash_navq> <.wic.bz2 OR .img>
```

After a few moments, your board should be flashed. Unplug your NavQ from power, reset the DIP switches to the desired boot device, and you're good to go!

## Flashing the image to SD card using dd or Win32DiskImager

To flash the image, you'll need to use `dd` on Linux/Mac or `Win32DiskImager` on Windows. 

### Linux

{% hint style="info" %}
Replace the X in "/dev/sdX" with the letter of your SD card in linux. You can use a program like "GParted" or "Disks" to find the letter of your SD card.
{% endhint %}

```text
$ sudo dd if=<path to .wic file> of=/dev/sdX bs=1M status=progress
```

### Mac

{% hint style="info" %}
Replace the X in "/dev/rdiskX" with the number of your SD card in Mac. You can use `diskutil list` to find the number of your SD Card.
{% endhint %}

```text
$ sudo diskutil unmountDisk /dev/rdiskX
$ sudo dd if=<path to .wic file> of=/dev/rdiskX bs=1m
```

### Windows

Download Win32DiskImager:

{% embed url="https://sourceforge.net/projects/win32diskimager/" %}

Open the program and select your SD card and .wic file, then click "Write".

