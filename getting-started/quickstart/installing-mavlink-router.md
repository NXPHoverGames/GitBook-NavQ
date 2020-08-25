---
description: mavlink-router routes MavLink data dynamically between several end nodes
---

# Installing mavlink-router



To be able to have several end nodes communicating via mavlink we need to set up [mavlink-router](https://github.com/intel/mavlink-router) on the navq.End nodes can be 

* a process for onboard control running on navq.
* a QGC computer the navq connects to via wifi.
* other mavlink enabled peripherals on the vehicle.

### Compile and installation of mavlink router

is done with the following steps on the navq \(internet access required\)

Connect to navq console via ssh / serial

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

###  Mavlink-router configuration

Configuration of mavlink router is done via a single configuration file expected as _/etc/mavlink-router/main.conf_  
This file needs to be created from scratch. An example configuration file is available in the mavlink-router sources - [https://github.com/intel/mavlink-router/blob/master/examples/config.sample](https://github.com/intel/mavlink-router/blob/master/examples/config.sample) 

#### Setup the config file with minimal configuration 

```text
~$ sudo nano /etc/mavlink-router/main.conf
```

```text
#Mavlink router configuration navq
#
[General]
TcpServerPort=5790
ReportStats=false
MavlinkDialect=auto

[UartEndpoint FMUuart]
Device=/dev/ttymxc2
Baud=155200

[UdpEndpoint FMUeth]
Mode = Eavesdropping
Address = 0.0.0.0
Port = 14551

[UdpEndpoint QGConMobile]
Mode = Normal
Address = 192.168.43.1
Port = 14550
```

The configuration above assumes that the navq gets mavlink data from FMU either via UART3 \(/dev/ttymxc2\) or UDP.  
You can leave out the unused connection.  
Via the UdpEndpoint QGConMobile section the mavlink stream is forwarded to a QGC computer/mobile device assuming it has 192.168.43.1 and navq is connected to this network via e.g. wifi. 

### Enabling autostart of mavlink-router

Enable the autostart of mavlink-router via systemd and start it 

```text
~$ sudo systemctl enable mavlink-router
~$ sudo systemctl start mavlink-router
```

 Finally you can check the status of mavlink router via 

```text
~$ sudo systemctl status mavlink-router
```

