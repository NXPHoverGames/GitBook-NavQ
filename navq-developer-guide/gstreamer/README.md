# GStreamer

![](../../.gitbook/assets/image%20%2829%29.png)

### Taking a picture

To take a picture on your NavQ using GStreamer, run the following command:

```text
$ gst-launch-1.0 -v v4l2src num-buffers=1 ! jpegenc ! filesink location=capture1.jpeg
```

To take video, you can run the following pipeline:

```text
$ gst-launch-1.0 v4l2src ! 'video/x-raw,width=1920,height=1080,framerate=30/1' ! vpuenc_h264 ! avimux ! filesink location='/home/navq/video.avi'
```





