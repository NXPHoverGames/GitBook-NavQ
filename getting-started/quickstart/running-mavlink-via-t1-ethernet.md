---
description: T1 Ethernet between FMUK66 and NavQ
---

# Running MavLink via T1 Ethernet

## Prerequisit

To run an T1 ethernet connection between FMUK66 and NavQ the [RDDRONE-T1ADAPT](../../navq-add-on-modules/100baset1-2-wire-automotive-ethernet-media-converter.md) media converter is needed.

## Setting a fixed IP to use eth for FMU communication

Since there is no DHCP on a drone and **FMUK66** has a fixed IP of **10.0.0.2** we need to set a fixed IP on the NavQ for eth0 to be able to communicate via ethernet to FMUK66. Suggestion is to use **10.0.0.3** for **navq**. 

connman is used for setting the network . To force connman to use a fixed IP in case of no DHCP is available the following file needs to be created.

Important is that you had a DHCP cable connection before otherwise connman will not register the network.

```text
~$ sudo nano /var/lib/connman/ethernet.config
```

```text
[global]
Name = Ethernet_config
Description = Ethernet fixed IP setting

[service_onboard_ethernet]
Type = ethernet
IPv4 = 10.0.0.3/255.255.255.0/10.0.0.3
```

 The IP4 settings are ownIP/netmask/router. 10.0.0.3 is set as router since no other device is there.

## Setting up FMUK66 for mavlink over T1 ethernet

T1 ethernet is supported by PX4 on FMUK66 with latest master.  
To enable FMUK66 sending mavlink telemetry via UDP to a specific IP is done by setting up the following file on the FMUK66 SDcard:

 _/etc/extras.txt_ 

```text
mavlink start -x -u 14551 -o 14551 -r 200000 -t 10.0.0.3 -m onboard
```

10.0.0.3 is the IP address of navq on the vehicle.Description of the mavlink start parameters on [https://dev.px4.io/v1.9.0/en/middleware/modules\_communication.html](https://dev.px4.io/v1.9.0/en/middleware/modules_communication.html)   
Additionally the **MAV\_BROADCAST** parameter on the FMU needs to be set to 2 - only multicast.

Distributing MavLink data can be done by installing [mavlink-router](installing-mavlink-router.md) on NavQ.

