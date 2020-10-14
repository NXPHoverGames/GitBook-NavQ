# Streaming Video to QGroundControl using NavQ over WiFi

## Prerequisites

### Devices required

In this guide, we need a few things:

1. NavQ Companion Computer mounted with Google Coral Camera attached
2. Laptop/Phone with QGroundControl Installed
3. Both NavQ and mobile device connected to the same WiFi network

### Setting up QGroundControl

In QGroundControl, click the Q logo in the top left, and configure the video section as seen in the image below:  


![](../../../.gitbook/assets/image%20%2842%29.png)

This will set up your QGroundControl instance to receive the UDP video stream from the NavQ.

### Connecting your NavQ to your router and getting IPs

Follow the WiFi setup guide using `connman` in the Quick Start guide to connect your NavQ to the same router as your mobile device. You will need to use the serial console to do this. Once you have your NavQ connected, you can run `ifconfig` in the serial console to find the IP address of your NavQ.

![Your IP address should be next to &apos;inet&apos; under &apos;wlan0&apos; if connected over WiFi.](../../../.gitbook/assets/image%20%2839%29.png)

You can SSH into the NavQ to run the GStreamer pipeline once you have the IP.

## Running the GStreamer pipeline

With your NavQ on, SSH into it by using the IP address you noted when connected to the serial console. Once you're successfully SSHed in, you should note the IP address that you logged in from as seen here:

![](../../../.gitbook/assets/image%20%2838%29.png)

This is the IP of your computer that you should be sending the video stream to.

To run the GStreamer pipeline, run the following command:

```text
$ sudo gst-launch-1.0 v4l2src ! video/x-raw,width=640,height=480,framerate=30/1 ! vpuenc_h264 bitrate=500 ! rtph264pay ! udpsink host=xxx.xxx.xxx.xxx port=5600 sync=false
```

{% hint style="info" %}
Make sure to replace the 'xxx.xxx.xxx.xxx' with the IP you noted when first SSHing into the NavQ.
{% endhint %}

Once you run that command, you should be able to see the video stream from your NavQ on QGroundControl!

![NavQ Streaming over UDP to QGroundControl](../../../.gitbook/assets/image%20%2843%29.png)

