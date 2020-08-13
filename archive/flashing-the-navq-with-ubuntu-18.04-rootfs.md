# Flashing the NavQ with &lt;u&gt; 18.04 rootfs \(internal\)

## Grabbing necessary files

### Download Ubuntu rootfs + bootloader

You will need to download the Ubuntu 18.04 rootfs files from this link:

[LINK](http://yb2.am.freescale.net/internal-only/desktop-alb/18.04-rootfs/) 

{% hint style="danger" %}
**NOTE: NXP Internal. Only NXP employees currently have access to this link.**
{% endhint %}

The two files you will need from this link are located in the `im8mmevk/` folder:

* imx-boot-imx8mmevk-ds.bin-flash\_evk
* imx-image-multimedia-ubumtu-imx8mmevk-20200611102300.rootfs.sdcard.bz2

You will need to extract the .bz2 file using 7zip on Windows or `bzip2 -d <filename>` on Linux.

### Download UUU

UUU is a tool used for flashing i.MX8 boards. You can download UUU for Windows or Linux using the link below:

[LINK](https://github.com/NXPmicro/mfgtools/releases/tag/uuu_1.2.135)

## Preparing the board

### Setting DIP switches

In order to flash the NavQ using UUU, you'll have to change the DIP switches to the following configuration:

![](../.gitbook/assets/image%20%2810%29.png)

### Powering the board

Power the board over USB-C as normal. You'll also want to connect to the USB-C/UART adapter and pull up a serial console \(with baud rate 115200\) to watch the serial output while flashing in case there are any errors.

## Flashing the board

### Using UUU to flash the board

\(NOTE: This has only been tested on Windows 10\)

Open CMD on Windows as administrator and change your directory to where you stored the uuu.exe, boot, and ubuntu rootfs files that you downloaded at the beginning of this guide. Then, plug the NavQ in with the correct DIP switch configuration and run the following command in the CMD:

```text
.\uuu.exe -b emmc_all imx-boot-imx8mmevk-ds.bin-flash_evk imx-image-multimedia-ubumtu-imx8mmevk-20200611102300.rootfs.sdcard
```

Your eMMC should now be flashed with the Ubuntu 18.04 rootfs. After this step, it still won't boot, so there are a few more steps to get it to boot.

### Adding correct NavQ DTB file

\(NOTE: You must have an SD card that you can boot from or you can't perform these steps.\)

Boot from the SD card and run the following commands to mount the eMMC boot partition:

```text
cd /mnt/
mkdir boot
sudo mount /dev/mmcblk2p1 /mnt/boot
```

Your eMMC boot partition should now be mounted. Next, you'll need to connect your NavQ over ethernet to your computer or router. Use an FTP client \(I used FileZilla\) to FTP into the NavQ, and then place the following file in /mnt/boot:

{% file src="../.gitbook/assets/imx8mm-navq.dtb" caption="imx8mm-navq.dtb" %}

This is a Device Tree Blob \(dtb\) file that tells Linux what the device tree looks like. \(WiFi does not work with this .dtb, a new one with WiFi working will be provided soon\). Once you've successfully copied over the .dtb file, you'll need to unmount the boot partition:

```text
sudo umount /dev/mmcblk2p1
```

Now you can change the DIP switches to boot from eMMC and reboot by running `reboot` in the serial console.

### Configure U-Boot to use new .dtb file

Once the NavQ starts booting from the eMMC, you'll want to press enter repeatedly until you get to the U-Boot console prompt. Once you're in the U-Boot prompt, you'll need to run the following commands:

```text
setenv fdt_file imx8mm-navq.dtb
saveenv
boot
```

Your NavQ should then boot into the Ubuntu rootfs.

The default username and password for this image is:

```text
Username: bluebox
Password: bluebox
```

Whala! You're done!

