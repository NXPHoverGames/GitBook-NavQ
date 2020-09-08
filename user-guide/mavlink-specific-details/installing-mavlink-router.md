---
description: mavlink-router routes MavLink data dynamically between several end nodes
---

# mavlink-router

## Introduction

To be able to have several end nodes communicating via mavlink simultaneously we need to set up [mavlink-router](https://github.com/intel/mavlink-router) on the NavQ.  
  
The end nodes can be 

* A process for onboard control running on NavQ.
* A QGroundControl \(QGC\) computer the NavQ connects to via a data link such as WiFi.
* Other mavlink enabled peripherals on the vehicle.
* Another program running on the same remote PC as QGC

## Installation and compiling mavlink router

To install and compile `mavlink router` follow the steps below \(internet access required on your NavQ\)

1\) Connect to NavQ console via ssh / serial

2\) Type the following commands

```text
~$ mkdir src
~$ cd src
~/src$ git clone https://github.com/intel/mavlink-router.git
~/src$ cd mavlink-router 
~/src/mavlink-router$ git submodule update --init --recursive
~/src/mavlink-router$ ./autogen.sh && ./configure CFLAGS='-g -O2' --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib --prefix=/usr
~/src/mavlink-router$ make
~/src/mavlink-router$ sudo make install
```

## Mavlink-router configuration

Configuration of `mavlink router` is done via a single configuration file  ``_`/etc/mavlink-router/main.conf`_  
This file needs to be created from scratch. An example configuration file is available in the mavlink-router sources - [https://github.com/intel/mavlink-router/blob/master/examples/config.sample](https://github.com/intel/mavlink-router/blob/master/examples/config.sample) 

{% hint style="danger" %}
As of today the mavlink-router _make install_ does not create the /etc/mavlink-router directory and main.conf file.  
Therefore please use the following commands to create the directory and file initially.

~$ sudo mkdir /etc/mavlink-router

~$ sudo touch /etc/mavlink-router/main.conf
{% endhint %}

### Setup the config file with minimal configuration 

```text
~$ sudo nano /etc/mavlink-router/main.conf
```

```text
#Mavlink router configuration navq
#
[General]
TcpServerPort=5760
ReportStats=false
MavlinkDialect=auto

[UartEndpoint FMUuart]
Device=/dev/ttymxc2
Baud=921600

[UdpEndpoint FMUeth]
Mode = Eavesdropping
Address = 0.0.0.0
Port = 14551

[UdpEndpoint QGConMobile]
Mode = Normal
Address = 192.168.43.1
Port = 14550
```

{% hint style="info" %}
The configuration above assumes that the NavQ gets mavlink data from FMU either via UART3 \(/dev/ttymxc2\) or UDP.  
If you use UART please set on the FMU the corresponding serial port to 921600Bd.  
For this the SER\_TELx\_BAUD \(x = number of telemetry port\) parameter needs to be adjusted to 921600 8N.  
If you use lower speed QGroundControl might fail to load parameters.
{% endhint %}

  
You can leave out the unused connection.  
Via the `UdpEndpoint QGConMobile` section the mavlink stream is forwarded to a QGC computer/mobile device assuming it has 192.168.43.1 and NavQ is connected to this network via e.g. WiFi. 

### Enabling auto-start of mavlink-router

Enable the auto-start of `mavlink-router` via `systemd` and start it 

```text
~$ sudo systemctl enable mavlink-router
~$ sudo systemctl start mavlink-router
```

### Checking status of mavlink-router

You can check the status of mavlink router using the command 

```text
~$ sudo systemctl status mavlink-router
```

