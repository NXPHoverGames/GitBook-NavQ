# Autostart micrortps client via systemd on NavQ

{% hint style="info" %}
**The instruction below assumes that you have successfully executed** [**Installing ROS2 foxy**](installing-ros2-foxy.md)
{% endhint %}

Generate a start up script for the micrortps client under _/usr/local/bin_

```text
sudo nano /usr/local/bin/start_micrortps_agent.sh
```

with content

```text
#!/bin/bash
## startup script for micro_rtps_agent
## agent will communicate to FMUK66 via UDP
## FMUK66 IPv4 addr = 10.0.0.2 
##
## Author: Gerald Peklar <gerald.peklar@nxp.com>  

source /opt/ros/foxy/setup.bash
source ~/px4_ros_com_ros2/install/setup.bash

micrortps_agent -t UDP -i 10.0.0.2
```

Save the file and exit nano.  
Make the file executable

```text
sudo chmod +x /usr/local/bin/start_micrortps_agent.sh
```

Generate a systemd service file to start the startup script at boot

```text
sudo nano /etc/systemd/system/micrortps_agent.service
```

with content

```text
[Unit]
Description=PX4 micrortps service
After=network.target

[Service]
Restart=always
TimeoutStartSec=10
User=navq
Group=navq
WorkingDirectory=~
ExecStart=/usr/local/bin/start_micrortps_agent.sh

[Install]
WantedBy=multi-user.target
```

Save the file and exit nano.  
Check if the process starts 

```text
sudo systemctl start micrortps_agent.service
sudo systemctl status micrortps_agent.service
```

You should see an state _active \(running\),_ quit with &lt;q&gt;  
Enable the systemd service file finally to be active at boot

```text
sudo systemctl enable micrortps_agent.service
```

 

