# GPIO

## Controlling GPIO through the command line

There are several GPIO pins on the various JST-GH connectors on NavQ. To control these GPIO pins, follow the instructions below.

### Exporting GPIO pins

In order to use GPIO pins, we need to export them in Linux first. To do this, we need to know the GPIO number for the pin we want to access. We can compute this number using the following formula:

```
gpio_number = ((gpio_bank - 1) * 32) + gpio_pin
```

For example, if we want to access the `GPIO1_IO12` pin on the UART4/I2C/GPIO connector, we would find that the GPIO number is:

```
gpio_number = ((1 - 1) * 32) + 12
gpio_number = (0) + 12
gpio_number = 12
```

If you want to find out what pins correspond to what GPIO numbers, we have tables in the `Hardware Overview/Pinouts and Connector` info section here:

{% content-ref url="../../hardware-overview/pinouts-and-connector-info.md" %}
[pinouts-and-connector-info.md](../../hardware-overview/pinouts-and-connector-info.md)
{% endcontent-ref %}

Once you know the GPIO number of the pin you want to access, exporting the pin for use is easy. All you have to do is echo the pin number to `/sys/class/gpio/export`. For example, if we were to export `GPIO1_IO12`, we would run the following in our NavQ console:

```
$ sudo echo 12 > /sys/class/gpio/export
```

{% hint style="warning" %}
Currently we have not created a specific user group to control GPIO pins, so you must be root to export/control pins. If someone in the community would like to submit a process for greating a GPIO user group, please make a post on our hackster.io page and we will add it to the demo image. :)
{% endhint %}

### Changing the pin direction

Next, we will want to change the direction of the GPIO pin for our specific use case. There are two options: `in` and `out`. To do this for `GPIO1_IO12`, you can run the following in your NavQ console:

```
$ sudo echo in > /sys/class/gpio/gpio12/direction
$ sudo echo out > /sys/class/gpio/gpio12/direction
```

### Reading or Writing the GPIO pin value

To read or write a value to the GPIO pin, we will follow a similar process to changing the pin direction. A pseudo file named `value` is created at `/sys/class/gpio/gpioXXX/value` that holds a 1 or a 0. If you   echoed `out` to the GPIO direction file, you can control the pin. To control the `GPIO1_IO12` pin, just run the following in your NavQ console:

```
$ sudo echo 0 > /sys/class/gpio/gpio12/value
$ sudo echo 1 > /sys/class/gpio/gpio12/value
```

If you echoed `in` to the GPIO direction file, you can read the value file and find the current state of the pin. To do this for the GPIO1\_IO12 pin, you can run the following in your NavQ console:

```
$ sudo cat /sys/class/gpio/gpio12/value
// a 0 or a 1 should be printed to your console
```

## Controlling GPIO programmatically (in C)

### Prerequisites

1. Create new group called `gpio`&#x20;

```
$ sudo groupadd gpio
$ sudo usermod -aG gpio navq
```

&#x20; 2\. Create new udev rules file

Create a file at /etc/udev/rules.d/99-gpio.rules and add the following to it:

```
SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 220 /sys/class/gpio/export /sys/class/gpio/unexport'"
SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"
```

This will allow you to access the GPIO pseudofiles without being root.

### Source Code

{% hint style="info" %}
Source code coming soon
{% endhint %}

