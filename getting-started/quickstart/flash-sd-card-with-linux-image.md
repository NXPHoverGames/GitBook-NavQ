# Downloading & Flashing the HoverGames-Demo Linux Image

## Preparing the image

The HoverGames images come as a .bz2 compressed archive. To decompress this image, you'll need to use a program like 7zip on Windows, use the bunzip2 command on Linux, or double click the archive on Mac.

## Flashing the image to eMMC or SD card using UUU

### Downloading UUU

NXP has a tool for flashing i.MX hardware called UUU (Universal Update Utility). You can download UUU from here:

{% hint style="info" %}
It is recommended to download the "Latest Release", not the "Pre-Release" at the top of the page.
{% endhint %}

{% embed url="https://github.com/NXPmicro/mfgtools/releases" %}

If you're on Windows, you'll want to download the `uuu.exe` file, and if you're on Linux, you'll want to download the `uuu` file.

### Downloading the Linux image

You must agree to all of the applicable licenses and agreements at the following link before downloading the Linux software. It is hosted here:

{% embed url="https://www.hovergames.com/EULA" %}

### Downloading the bootloader

{% hint style="warning" %}
NOTE: This file is only needed for flashing with UUU to the eMMC/SD Card. If you want to flash your SD Card with dd or Win32DiskImager, this file is not needed.
{% endhint %}

{% embed url="https://drive.google.com/file/d/1AYRxy-okiu8_9_9EmC5DWbCq-hZk2PKw/view?usp=sharing" %}

### Step 1

Flip the DIP switches on your NavQ to put it into USB flashing mode (boot from USB in the image below). Here is an image that shows how to do so:

![](<../../.gitbook/assets/image (43).png>)

{% hint style="info" %}
Once you're done flashing, you can use this image to select the boot mode: eMMC or SD card.
{% endhint %}

### Step 2

Connect your NavQ using the included USB-C cable to your computer. You should recieve a message on your computer that it has been connected. To make sure the NavQ is connected, you can run the UUU program with the `-lsusb` flag and you should see an output similar to this:

```
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

{% hint style="info" %}
There are advantages and disadvantages to each storage medium. eMMC is faster, but is locked to 16GB size and is non-removable. SD cards can be of any size you like and are removable, but they are quite a bit slower.
{% endhint %}

```
Linux
-----
$ ./uuu -b [emmc_all|sd_all] <.bin-flash_navq> <.wic.bz2 OR .img>

Windows
-------
$ .\uuu.exe -b [emmc_all|sd_all] <.bin-flash_navq> <.wic.bz2 OR .img>
```

After a few moments, your board should be flashed. Unplug your NavQ from power, reset the DIP switches to the desired boot device, and you're good to go!

## Flashing the image to SD card using dd or Win32DiskImager

To flash the image, you'll need to use `dd` on Linux/Mac or `Win32DiskImager` on Windows.&#x20;

### Linux

{% hint style="info" %}
Replace the X in "/dev/sdX" with the letter of your SD card in linux. You can use a program like "GParted" or "Disks" to find the letter of your SD card.
{% endhint %}

```
$ sudo dd if=<path to .wic file> of=/dev/sdX bs=1M status=progress
```

### Mac

{% hint style="info" %}
Replace the X in "/dev/rdiskX" with the number of your SD card in Mac. You can use `diskutil list` to find the number of your SD Card.
{% endhint %}

```
$ sudo diskutil unmountDisk /dev/rdiskX
$ sudo dd if=<path to .wic file> of=/dev/rdiskX bs=1m
```

### Windows

Download Win32DiskImager:

{% embed url="https://sourceforge.net/projects/win32diskimager/" %}

{% hint style="info" %}
Currently the HoverGames-Demo Linux image is packaged as a .img file. In future releases, it may be packaged as a .wic.bz2 file. If it is packaged as a .wic.bz2 file, you'll want to extract the .bz2 file before flashing using Win32DiskImager.
{% endhint %}

Open the program and select your SD card. Choose the .wic OR .img file, then click "Write".
