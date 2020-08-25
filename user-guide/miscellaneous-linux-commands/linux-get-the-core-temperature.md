# Linux: Get the core temperature

The i.MX 8M Mini parts are rated 0C to +95C. We do not expect they will need any additional heat-sinking, especially while flying, but you can monitor the core temperature with the following command:

`cat /sys/class/thermal/thermal_zone0/temp` 

