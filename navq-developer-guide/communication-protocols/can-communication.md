---
description: '[WIP] A guide on communicating over CAN/SLCAN using NavQ and UCANS32K146'
---

# CAN

## Introduction

If you're thinking about using the CAN protocol on your drone, this guide will walk you through using our UCANS32K146 to create a CAN interface.

Since there isn't a native CAN bus on the NavQ, we can use a protocol called SLCAN to communicate CAN messages across a UART connection. We have built a binary for the UCANS32K146 that acts as an SLCAN transfer layer. This means that we can add a CAN bus to NavQ by just connecting the UCANS32K146 to the UART3 port.

![Diagram of setup](<../../.gitbook/assets/image (55).png>)

## Setting up SLCAN on NavQ

{% hint style="info" %}
SLCAN support is enabled in the October image coming out this month.
{% endhint %}

To enable SLCAN on NavQ, run these commands:

```
$ sudo modprobe slcan
$ sudo slcand -o -t sw -s8 /dev/ttymxc2 -S 115200
$ sudo ip link set up slcan0
```

Now you can use SocketCAN or python-can to send and recieve CAN messages over the slcan0 interface. As an example, here is how to send a CAN message from the command line:

```
$ cansend slcan0 123#deadbeef
```

## Flashing your UCANS32K146 with the SLCAN conversion binary

{% hint style="info" %}
This binary is not yet available. This page will be updated with a link to the binary when it is ready.
{% endhint %}

Follow the guide at the link below to flash the SLCAN binary to your UCAN board:

{% embed url="https://nxp.gitbook.io/nxpmobilerobotics/flashing-guide/flashing-hovergames-boards" %}

