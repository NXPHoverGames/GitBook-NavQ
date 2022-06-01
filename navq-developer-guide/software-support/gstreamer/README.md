# GStreamer

![](<../../../.gitbook/assets/image (27).png>)

{% hint style="success" %}
There is an NXP community user guide for gstreamer available here:\
[https://community.nxp.com/t5/i-MX-Processors-Knowledge-Base/i-MX-8-GStreamer-User-Guide/ta-p/1098942](https://community.nxp.com/t5/i-MX-Processors-Knowledge-Base/i-MX-8-GStreamer-User-Guide/ta-p/1098942)
{% endhint %}

### Taking a picture

To take a picture on your NavQ using GStreamer, run the following command:

```
$ gst-launch-1.0 -v v4l2src num-buffers=1 ! jpegenc ! filesink location=capture1.jpeg
```

To take video, you can run the following pipeline:

```
$ gst-launch-1.0 v4l2src ! 'video/x-raw,width=1920,height=1080,framerate=30/1' ! vpuenc_h264 ! avimux ! filesink location='/home/navq/video.avi'
```



