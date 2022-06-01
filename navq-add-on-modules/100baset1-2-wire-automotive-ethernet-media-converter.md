---
description: 100BaseT1 2-Wire Automotive Ethernet media converter
---

# RDDRONE-T1ADAPT



![RDDRONE-T1ADAPT TOP view](<../.gitbook/assets/image (14).png>)

![RDDRONE-T1ADAPT Bottom view - USB-C alternative power input connector](<../.gitbook/assets/image (15).png>)

{% hint style="success" %}
Additional RDDRONE-T1ADAPT media converter details can be found here:\
[https://nxp.gitbook.io/rddrone-t1adapt/](https://nxp.gitbook.io/rddrone-t1adapt/)
{% endhint %}

### TJA110x 2-Wire Ethernet

NXP's TJA1101 is an Ethernet PHY that provides a two-wire 100BaseT1 Ethernet interface. The Ethernet MAC side of this interface is not unusual, and the traffic on the line is "regular Ethernet"

NXP's Flight controller for Mobile Robotics -  RDDRONE-FMUK66 includes a 2-wire Ethernet interface on board. In order to connect this with the  8MMNavQ this media converter can be used. The RDDRONE-T1ADAPT is also useful when connecting to other experimental modules such as V2X or an Automotive 5/10 port switch.

### Connecting the RDDRONE-T1ADAPT

On RDDRONE-T1ADAPT power is supplied via a 3 pin JST-GH connector. There is a matching 3 pin JST-GH connector on the 8MMNavQ. A simple 1:1 cable is used. Optionally a USB-C cable can be used to provide power (only) connection.\
\
A 2 pin JST-GH connector is used for connecting Ethernet between this board and another - such as the RDDRONE-FMUK66. A simple 1:1 cable is used.

There are also locations marked on the bottom side of the board for soldering in wires for both power and 2-wire Ethernet\


### RDDDRONE-T1ADAPT Software

There is a small NXP LPC processor on board to configure the back to back PHYs and manage setup and LEDs. This board comes pre-programmed and there is no user software required. Contact hovergames@nxp.com or your local NXP representative if there is a specific need to access the software.

![](<../.gitbook/assets/100baset1-media converter.jpg>)



![Engineering Sample - 100BaseT1 Ethernet media converter](https://firebasestorage.googleapis.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M-CCnxDe4dTvAz3QmDw%2Fuploads%2FQn9OJoZo7duYxYO3DU53%2Ffile.jpeg?alt=media)

