# PWM \(Onboard RGB LED\)

## Controlling PWM on NavQ

The PWM chips are tied to the onboard LED on NavQ. There are three PWM chips: `pwmchip0`, `pwmchip1`, and `pwmchip2`. Each of these "chips" have one PWM line attached to them: `pwm0`. To use these PWM lines, you will need to use the sysfs interface.

## Using the sysfs interface to control the onboard LED

{% hint style="info" %}
Currently, you must be root to access these PWM chips. In the future we will use a udev rules file to change the permissions. This will allow the `navq` user to write to the psuedofiles for these chips.
{% endhint %}

### Step 1

Log into the `root` user on NavQ by running this command:

```text
$ sudo su -
<enter password>
```

### Step 2

Navigate to /sys/class/pwm and run the following commands:

```text
$ echo 0 > pwmchip0/export
$ echo 0 > pwmchip1/export
$ echo 0 > pwmchip2/export
```

### Step 3

Now that our PWM lines are exported for each chip, we can change the duty cycle of the PWM lines and enable them. The default frequency is 2730667 Hz. For a 50% duty cycle, we will use half of this number: 1365333. Apply this duty cycle to each chip by running the following commands:

```text
$ echo 1365333 > pwmchip0/pwm0/duty_cycle
$ echo 1365333 > pwmchip1/pwm0/duty_cycle
$ echo 1365333 > pwmchip2/pwm0/duty_cycle
```

### Step 4

We will now enable each line. The colors for each chip are as follows:

`pwmchip0`: RED

`pwmchip1`: GREEN

`pwmchip2`: BLUE

To enable the colors, run the following commands:

```text
$ echo 1 > pwmchip0/pwm0/enable
$ echo 1 > pwmchip1/pwm0/enable
$ echo 1 > pwmchip2/pwm0/enable
```

Running these commands in succession should enable the LEDs in a RED, GREEN, BLUE pattern until you reach a white LED.

## Controlling the onboard LEDs programmatically

{% hint style="info" %}
Comnig soon
{% endhint %}

