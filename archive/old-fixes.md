# Old Fixes

## Old Fixes \[Archive\]

{% hint style="info" %}
These fixes are common for older versions. If you don't run into issues with the sections stated below, you shouldn't need to use these fixes.
{% endhint %}

### WiFi

Currently the image does not include connman due to a bug in the build system. Also, for connman to work, it requires a package called `dhcpc5`. To install `connman` and `dhcpc5`, connect your NavQ to the internet using ethernet, and run the following:

```text
$ sudo apt install connman dhcpc5
```

Use the quick start guide to connect to WiFi once you're finished installing those packages.

#### resolv.conf

There is an issue with `resolv.conf` that prevents you from connecting to the internet on WiFi due to an incorrect DNS setup. To fix this, edit `/etc/resolv.conf` by removing the current nameserver IP and replacing it with `8.8.8.8`.



### Setting the \`dialout\` and \`video\` usergroups

By default, the `navq` user on the HoverGames-Demo image is not in the `dialout` and `video` groups. If your user is not in those groups, you will not have control of the camera nor the UART port for communication to the FMUK66. To fix this, run the following commands:

```text
$ sudo usermod -a -G dialout $USER
$ sudo usermod -a -G video $USER
$ logout
```

It is necessary to log out to ensure that the Linux kernel knows that your user is part of those user groups.



### V4L2SRC & Gstreamer

In the current build, there is an issue with ldconfig which causes the v4l2src driver to not be found. To fix this, run the following commands:

```text
$ export LD_LIBRARY_PATH=/usr/lib >> ~/.bashrc
$ source ~/.bashrc
```

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

