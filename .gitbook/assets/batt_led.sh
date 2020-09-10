#!/usr/bin/env bash
bash -c "source /opt/ros/noetic/setup.sh && roslaunch mavros px4.launch fcu_url:='/dev/ttymxc2:921600' &" 
bash -c "sleep 5"
bash -c "source /opt/ros/noetic/setup.sh && python3 /home/navq/batt_led.py &"
