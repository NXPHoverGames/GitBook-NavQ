---
description: T1 Ethernet between FMUK66 and NavQ
---

# Running MavLink over T1 Ethernet

## Prerequisite

The RDDRONE-FMUK66 has a two wire 100BaseT1 Ethernet interface on board. The 8mmNavQ board does not include T1 Ethernet however an adapter may be used. To run the T1 Ethernet connection between FMUK66 and NavQ use a separate [RDDRONE-T1ADAPT](../../navq-add-on-modules/100baset1-2-wire-automotive-ethernet-media-converter.md) media converter.  


{% hint style="success" %}
The 8mpNavQ or "NavQPlus" will have two Ethernet interfaces. it is planned that one of these interfaces will natively be configured as 100BaseT1 
{% endhint %}

## Setting a fixed IP to use Ethernet for FMU communication

It is not recommended to use DHCP in a vehicle such as a drone, since you generally don't want the network to change without knowing about the explicit details.  Therefore since there is no DHCP and **FMUK66** by default has a fixed IP of **10.0.0.2,** we need to set a fixed IP on the NavQ for `eth0` to be able to communicate via Ethernet to FMUK66. 

{% hint style="info" %}
It is suggested to use IP address **10.0.0.3** for **navq**. 
{% endhint %}

### connman connection manager 

The linux program `connman` is used for configuring the network settings . To force `connman` to use a fixed IP \( as in case when no DHCP is available\) the following file needs to be created.

{% hint style="warning" %}
It is important is that you have a Ethernet cable connection before, otherwise connman will not register the network.
{% endhint %}

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

 The IP4 settings are in the order of  ownIP/netmask/router. Note that 10.0.0.3 is set as router since in this particular hardware configuration no other device is there.

## Setting up FMUK66 for mavlink over T1 Ethernet

T1 Ethernet is supported by PX4 on FMUK66 with latest master.

{% hint style="info" %}
To enable the RDDRONE-FMUK66 mavlink telemetry via UDP sending to a specific IP you must add the following file on the FMUK66 SDcard:

 _/etc/extras.txt_ 
{% endhint %}

```text
set +e
mavlink start -x -u 14551 -o 14551 -r 200000 -t 10.0.0.3 -m onboard
set -e
```

In the example configuration above, 10.0.0.3 is the IP address of NavQ on the vehicle.  
  
More detailed description of the mavlink start parameters can be found here: [https://dev.px4.io/v1.9.0/en/middleware/modules\_communication.html](https://dev.px4.io/v1.9.0/en/middleware/modules_communication.html) 

  
Additionally the **MAV\_BROADCAST** parameter on the FMU needs to be set to "2 - only multicast".

{% hint style="info" %}
Distributing MavLink data can be done by installing [mavlink-router](installing-mavlink-router.md) on NavQ.
{% endhint %}

