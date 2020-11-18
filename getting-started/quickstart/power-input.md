# Power input

## Power input specification

The NavQ can take a voltage of 5V to 20V.

The board may also be powered via USB- which also has a 20V max input rating.

{% hint style="warning" %}
Note that while the voltage regulator on the external JST-JH power connector has absolute max rating is 26V. According to the schematics, there is a 20V TVS Diode \(PTVS20VS1UR\) at that input before the regulator \(MP8759GD\), with a breakdown voltage of 22.2V to 24.5V according to the datasheet. 

Any experimentation above 20V input should take this into account and be done at your own risk. 
{% endhint %}

###  Power input protection

There is some, but limited power input protection on board. Given this is typically for USB-C application, it may not be sufficient in harsh operating environments. You may want to provide some additional reverse polarity protection, over-current, or DC-DC conversion/isolation from the battery if you expect to be experimenting outside the HoverGames normal operating range or treating it harshly.

### Battery supply protection

Please monitor your LiPo battery carefully for **undervoltage** conditions. If left connected, the NavQ and HoverGames drone will completely drain your LiPo battery and could cause permanent damage to your battery. There are no undervoltage disconnect provisions built in.

#### Low battery monitor

A simple solution to undervoltage protection may be to add a hobby grade low battery monitor alarm. These sound a loud alarm when any cell goes below a user set threshold voltage. The LED display will also show the individual cell voltage and total pack voltage. This plugs into the balance connector of the LiPo battery. They are inexpensive and available at hobby stores or online at typical outlets. Here are some examples:

![](../../.gitbook/assets/image%20%2835%29.png)

* Amazon - "[Battery Voltage Checker Alarm](https://www.amazon.com/PACK-Battery-Voltage-Checker-Alarm/dp/B00XQ91ECA/ref=sr_1_7?crid=2MKAGP9RB7BQ5&dchild=1&keywords=lipo+battery+monitor&qid=1596208190&sprefix=lipo+battery+mon%2Caps%2C169&sr=8-7)"
* Amazon - "[Battery Voltage Monitor Low Voltage](https://www.amazon.com/CAMWAY-Battery-Voltage-Monitor-Low-Voltage/dp/B07QQQ1XKX/ref=sr_1_10?crid=2MKAGP9RB7BQ5&dchild=1&keywords=lipo+battery+monitor&qid=1596208230&sprefix=lipo+battery+mon%2Caps%2C169&sr=8-10)"

