# Expand space on SD card/eMMC

## Easy-to-use script

We have created an easy-to-use script to resize the flashed image on your device. Since the image is smaller than the storage device, it is not properly expanded when first flashed. You can run the following script to expand the filesystem.

{% hint style="info" %}
This script should be in the home folder of the `demo` image. If it isn't there, or if you lost it and need it, it is linked below.
{% endhint %}

{% file src="../../.gitbook/assets/resizedisk.sh" %}

To run the script, run the following commands for the boot device you're currently using:

_**For eMMC:**_

```text
$ sudo ./resizeDisk.sh eMMC
```

_**For SD card:**_

```text
$ sudo ./resizeDisk.sh sd
```

### Making the script executable

The script should be executable when it is included in the image. If it isn't, then you'll need to make it executable by running the following command:

```text
$ chmod a+x ./resizeDisk.sh
```

## Running out of space

{% hint style="info" %}
If you don't want to use the script, you can run the commands below.
{% endhint %}

You may run into an issue where you run out of space on the eMMC or SD card when installing ROS. To expand the rootfs partition, follow these steps:

{% hint style="warning" %}
If you're on the eMMC, you'll use **/dev/mmcblk2**. If you're on an SD card, use **/dev/mmcblk1**. By default the NavQ boots from the included SD card in your kit.
{% endhint %}

```text
$ sudo fdisk /dev/mmcblk1

Command (m for help): p

Device           Boot      Start   End      Blocks   Size   Id  System
/dev/mmcblk1p1   *         16384   186775   170392   83.2M  c   W95 FAT32 (LBA)
/dev/mmcblk1p2             196608  <end>   <blocks>  <size> 83  Linux

Command (m for help): d
Partition number (1,2, default 2): 2

Partition 2 has been deleted.

Command (m for help): p

Device           Boot      Start   End      Blocks   Size   Id  System
/dev/mmcblk1p1   *         16384   186775   170392   83.2M  c   W95 FAT32 (LBA)
   
Command (m for help): n
Partition type
   e   extended
   p   primary partition (1-4)
Select (default p): p
Partition number (1-4, default 1): 2
First sector (2048-30621695, default 2048): 196608
Last sector, +sectors or +size{K,M,G} (2048-30621695, default 30621695): <press enter for default>

Created a new partition 2 of type 'Linux' and of size 14.5 GiB.
Partition #2 contains a ext4 signature.

Do you want to remove the signature? [Y]es/[N]o: n

Command (m for help): p

Device           Boot      Start   End      Blocks   Size   Id  System
/dev/mmcblk1p1   *         16384   186775   170392   83.2M  c   W95 FAT32 (LBA)
/dev/mmcblk1p2             196608  30621695 39425088 14.5G  83  Linux

Command (m for help): w
The partition table has been altered!
```

Once you're done with those steps, run this command:

```text
$ sudo resize2fs /dev/mmcblk1p2
```

and reboot. You should now be able to install ROS Melodic without size issues.

### Commands for fdisk

If you prefer to just see the commands, these are the commands you need to run in fdisk in order to resize your disk.

```text
d <enter>
2 <enter>
n <enter>
p <enter>
2 <enter>
196608 <enter>
<enter>
n <enter>
w <enter>
<fdisk should exit>

$ sudo resize2fs /dev/mmcblk2p2 <enter> (FOR eMMC)
$ sudo resize2fs /dev/mmcblk1p2 <enter> (FOR SD CARD)
```

