---
description: Options and cables for powering the NavQ
---

# Power Cables

## Power input specification

The NavQ can accept up to \(&lt;&lt;TODO&gt;&gt; Check if 20V or 24V is the chip spec\) Volt power input directly. This is based on USB-C specification components on board. 

### Power input protection

There is some, but limited power input protection on board. Given this is typcially for USB-C application, it may not be sufficient in harsh operating environments. You may want to provide some additional reverse polarity protection, overcurrent, or DCDC conversion/isolation from the battery if you expect to be experimenting outside the HoverGames normal operating range or treating it harshly.

### Battery supply protection

Please monitor your Lipo battery carefully for **undervoltage** conditions. If left connected, the NavQ and HoverGames drone will completely drain your LiPo battery and could cause permanent damage to your battery. There are no undervoltage disconnect provisions built in.

#### Low battery monitor

A simple solution to undervoltage protection may be to add a hobby grade low battery monitor alarm. These sound a loud alarm when any cell goes below a user set threshold voltage. The LED display will also show the individual cell voltage and total pack voltage. This plugs into the balance connector of the LiPo battery. They are inexpensive and available at hobby stores or online at typical outlets. Here are some examples:

![](../../.gitbook/assets/image%20%2835%29.png)

* Amazon - "[Battery Voltage Checker Alarm](https://www.amazon.com/PACK-Battery-Voltage-Checker-Alarm/dp/B00XQ91ECA/ref=sr_1_7?crid=2MKAGP9RB7BQ5&dchild=1&keywords=lipo+battery+monitor&qid=1596208190&sprefix=lipo+battery+mon%2Caps%2C169&sr=8-7)"
* Amazon - "[Battery Voltage Monitor Low Voltage](https://www.amazon.com/CAMWAY-Battery-Voltage-Monitor-Low-Voltage/dp/B07QQQ1XKX/ref=sr_1_10?crid=2MKAGP9RB7BQ5&dchild=1&keywords=lipo+battery+monitor&qid=1596208230&sprefix=lipo+battery+mon%2Caps%2C169&sr=8-10)"

## NavQ Cables

The NavQ ships with several cables. They allow for several configurations when powering the NavQ

#### USB-C

When working on the bench you may wish to power the NavQ from USB-C input cable. This cable is provided. It would also be possible to power the NavQ while on a drone from a separate USB-C battery pack like those for Cell phone power. 

{% hint style="warning" %}
Please note that some USB-C ports on charging adapters and particularly on unpowered Hubs may not supply enough current to run the NavQ and all the peripherals. If you notice a booting failure, please first try powering from an external battery or known high power USB-C charger or power supply.
{% endhint %}

### Drone power cable supply

![JST-GH Power input cable connector \(USB-C connector also available on other side of board\)](../../.gitbook/assets/image%20%2834%29.png)

![JST-GH Power input cable connector](../../.gitbook/assets/image%20%2832%29.png)

![3-way splitter-extender \(optional\), XT60 adapter and &quot;bullet&quot; adapter provided](../../.gitbook/assets/image%20%2831%29.png)

![Choose XT60 or Bullet connectors for powering your NavQ](../../.gitbook/assets/image%20%2833%29.png)



