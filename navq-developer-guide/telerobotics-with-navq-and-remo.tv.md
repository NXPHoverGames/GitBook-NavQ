---
description: '[WORK IN PROGRESS]'
---

# Telerobotics with NavQ and Remo.TV

## What is telerobotics?

Telerobotics is a platform in which robots can be controlled over the internet. A good example of this is Twitch Plays. Twitch Plays allows users to play games on a stream by giving commands through Twitch Chat. 

Now you may be wondering, "Well Twitch Plays isn't controlling a robot, that's a video game!" and you'd be correct. There is an alternative for robotics though! It's called Remo.TV, and we have written a module for the NavQ to be supported on the site.

Remo.TV is a website where anyone can log in and control robots over the internet. With NavQ, your family and friends can easily control your HoverGames Drone or NXP Cup Rover through Remo.TV. Below we have written a guide for you to set up your drone or rover with the service.

## Setting up Remo.TV on NavQ

### Dependencies and repos

To set up Remo.TV on NavQ, we are going to have to install a few packages. Lets install those now:

{% hint style="info" %}
The steps below come from the README on the official remotv GitHub repository: [https://github.com/remotv/controller](https://github.com/remotv/controller)
{% endhint %}

Install dependencies:

```text
$ sudo apt update
$ sudo apt upgrade -y
$ sudo apt install ffmpeg python-serial python-dev libgnutls28-dev espeak python-smbus python-pip git
```

Download RemoTV from GitHub:

```text
$ git clone https://github.com/remotv/controller.git ~/remotv
```

Install Python dependencies:

```text
$ sudo python -m pip install -r ~/remotv/requirements.txt
```

Open RemoTV and copy the sample config file:

```text
$ cd remotv
$ cp controller.sample.conf controller.conf
```

And your RemoTV is cloned and ready for configuration! Next we will set up our configuration file.

### Configurating the Configuration

