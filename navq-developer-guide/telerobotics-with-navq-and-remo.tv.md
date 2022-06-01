---
description: '[WORK IN PROGRESS]'
---

# Telerobotics with NavQ and Remo.TV

## What is telerobotics?

Telerobotics is a platform in which robots can be controlled over the internet. A good example of this is Twitch Plays. Twitch Plays allows users to play games on a stream by giving commands through Twitch Chat.&#x20;

Now you may be wondering, "Well Twitch Plays isn't controlling a robot, that's a video game!" and you'd be correct. There is an alternative for robotics though! It's called Remo.TV, and we have written a module for the NavQ to be supported on the site.

Remo.TV is a website where anyone can log in and control robots over the internet. With NavQ, your family and friends can easily control your HoverGames Drone or NXP Cup Rover through Remo.TV. Below we have written a guide for you to set up your drone or rover with the service.

{% hint style="warning" %}
This guide is written for an NXP Cup Car with PX4. You can follow this guide for other robots, but you will need to create your own hardware file to work with your setup. To do this, follow Remo.TV's documentation. You can start by visiting the front page of their website:
{% endhint %}

{% embed url="https://remo.tv" %}

## Setting up Remo.TV on NavQ

### Dependencies and repos

To set up Remo.TV on NavQ, we are going to have to install a few packages. Lets install those now:

{% hint style="info" %}
The steps below come from the README on the official remotv GitHub repository: [https://github.com/remotv/controller](https://github.com/remotv/controller)
{% endhint %}

Install dependencies:

```
$ sudo apt update
$ sudo apt upgrade -y
$ sudo apt install ffmpeg python-serial python-dev libgnutls28-dev espeak python-smbus python-pip git
```

Download RemoTV from GitHub:

```
$ git clone https://github.com/remotv/controller.git ~/remotv
```

Install Python dependencies:

```
$ sudo python -m pip install -r ~/remotv/requirements.txt
```

Open RemoTV and copy the sample config file:

```
$ cd remotv
$ cp controller.sample.conf controller.conf
```

And your RemoTV is cloned and ready for configuration! Next we will set up our configuration file.

### Configurating the Configuration

To get Remo.TV to work on your robot, you'll need to set up the configuration file to work with NavQ. Open the controller.conf file that we copied earlier for editing. Below you will see each field that needs to be edited for the configuration file.

### \[robot] Section

| Config field | Value                              |
| ------------ | ---------------------------------- |
| owner=       | Set this as your Remo.TV username. |
| robot\_key=  | Set this as your Remo.TV API key.  |
| type=        | navq                               |

### \[camera] Section

| Config field      | Value |
| ----------------- | ----- |
| x\_res=           | 640   |
| y\_res=           | 480   |
| video\_framerate= | 30    |

## Setting up controls on Remo.TV

Log into your Remo.TV account and go to your robot. The screen should look like this:

![](<../.gitbook/assets/image (60).png>)

At the bottom, there is a movement tab. For the NXP Cup car, you'll want to press the (edit buttons) text and paste this code into that window:

```
[
  {
    "break": "line",
    "label": "movement"
  },
  {
    "label": "forward",
    "command": "f",
    "hot_key": "w"
  },
  {
    "label": "stop",
    "command": "s",
    "hot_key": "s"
  },
  {
    "label": "reverse",
    "command": "x",
    "hot_key": "x"
  },
  {
    "label": "left",
    "command": "l",
    "hot_key": "a"
  },
  {
    "label": "right",
    "command": "r",
    "hot_key": "d"
  }
]
```

This will set up your controls to be compatible with the example navq hardware file.

## Running the Remo.TV controller

Once you have set up the software, you can run the controller by going into the `controller` directory and running:

```
$ python3 controller.py
```

Your robot should start streaming to Remo.TV!
