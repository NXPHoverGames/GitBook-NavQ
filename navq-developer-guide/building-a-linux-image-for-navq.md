# Building a Linux image for NavQ

## HoverGames-Linux Distros

We have two separate Linux distributions that you can build for NavQ. There are pros and cons to both.

## \[1\] HoverGames-BSP

The HoverGames-BSP image is based on NXP's Yocto BSP for i.MX 8M Mini. This distro is not as easy to use, and requires much more effort to get a working system, but currently it is the only system that is allowed for use if you want to use NavQ commercially. If you need tight integration and a small system that has only the packages you need installed on it, or if you're a company looking to use the NavQ in production, this is the one for you.

## \[2\] HoverGames-Demo

The HoverGames-Demo image comes with the APT package manager as well as some other pre-installed software specific to i.MX 8M Mini. This distro is the easiest to use due to it's great compatibility with pre-existing binaries coming from official repositories. You can install ROS, OpenCV, and more on this image just as you would on a normal desktop computer. This makes the Demo image great for quick development and iteration. To use this image, you must agree to a Demo license stating that you will not use NavQ comercially with this distribution.

## Building the Linux images for NavQ

### Prerequisites

#### Recommended Specs

You'll need to use a computer with Ubuntu 18.04 installed, and we recommend a high amount of cores + RAM to build these images in a decent time frame. You will also need a large HDD or SSD \(&gt;500GB\) to store the build files. A table of recommended specs are below:

| Component | Recommended Hardware |
| :--- | :--- |
| CPU | Recent 6-core Intel i-Series or AMD Ryzen processor with HyperThreading or SMT \(Simultaneous Multi-Threading\) |
| RAM | 16GB DDR4 or more |
| Storage | 500GB SSD recommended, HDD will suffice but will be slow |
| Operating System | Ubuntu 18.04 \(Not 20.04!\) |

#### Install Yocto build tools

Follow the guide at Yocto's [website](https://www.yoctoproject.org/docs/2.4.2/yocto-project-qs/yocto-project-qs.html) to install the necessary build tools for Ubuntu/Debian, or just install the list of packages below:

```text
$ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib \
     build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
     xz-utils debianutils iputils-ping libsdl1.2-dev xterm
```

### Running the build script

We have a GitHub repo with instructions for both the HoverGames-BSP and HoverGames-Demo images. The BSP image can be built using the `master` branch, whereas the Demo image can be built using the `demo` branch. The link to the repo is below.

{% embed url="https://github.com/NXPmicro/meta-nxp-hovergames" %}



