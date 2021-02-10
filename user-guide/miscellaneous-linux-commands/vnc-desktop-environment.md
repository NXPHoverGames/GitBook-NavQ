# VNC desktop environment

## Intro

If you've ever run into a situation where you need to view a raw stream from the NavQ's Google Coral Camera, or need to run a lightweight GUI application on NavQ, you can do so using the guide below.

## Instructions

### Installation

You can run the commands below to start a VNC server on your NavQ.

```text
# Credit to: https://www.vandorp.biz/2012/01/installing-a-lightweight-lxdevnc-desktop-environment-on-your-ubuntudebian-vps/#.YCQEGS1h3O4
# Install X, LXDE, VPN programs

apt-get install xorg lxde-core tightvncserver

# Start VNC to create config file

tightvncserver :1

# Then stop VNC

tightvncserver -kill :1

# Edit config file to start session with LXDE:

nano ~/.vnc/xstartup

# Add this at the bottom of the file:
lxterminal &
/usr/bin/lxsession -s LXDE &

# Restart VNC

tightvncserver :1
```

### Connecting

You can use TightVNC to connect. You'll want to use the IP address of your NavQ at port 5901.



