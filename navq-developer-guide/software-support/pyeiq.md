---
description: Python framework for eIQ on i.MX
---

# pyeIQ

{% hint style="warning" %}
This page is a work in progress.  
NOTE - THIS WILL NOT WORK ON NAVQ!!  
  
UPDATED 12/03/2020 - Updated with notes that this will not work as-is for NavQ using 8M Mini. Apologies for any confusion.  
  
These notes are here only for reference advanced developers.  
The 8M Mini does not have any NN acceleration and can only run using the processor cores.  
{% endhint %}

{% hint style="danger" %}
pyeIQ is not targeted at the i.MX Mini processor, but it may still work albeit with much lower performance than if an accelerator was available. We expect to use this more with the upcoming i.MX 8M Plus that includes a 2.25 TOPS neural net accelerator.
{% endhint %}

  
Please refer to the following pyeIQ documentation:

[https://pyeiq.dev/](https://pyeiq.dev/)

Note that eIQ support is only included on imx-image-full-imx8mpevk.wic pre-built image \[1\]. \*\*\* THIS IMAGE is only for 8M Plus!

Please take a look on switch\_image application, we are using TFLite 2.1.0. This application offers a graphical interface for users to run an object classification demo using either CPU or NPU.

\# pyeiq --run switch\_image

We also have a TFLite example out of pyeIQ, please refer to instructions below. Details can be found on i.MX Linux User's Guide \[2\].

\# cd /usr/bin/tensorflow-lite-2.1.0/examples

\# ./label\_image -m mobilenet\_v1\_1.0\_224\_quant.tflite -i grace\_hopper.bmp -l labels.txt

The i.MX Linux User's Guide \[2\] also provides instructions on how to get our latest Linux BSP \[1\] up and running. \*\*\* NOTE FOR 8M Plus only!

\[1\]: [https://www.nxp.com/webapp/sps/download/license.jsp?colCode=L5.4.47\_2.2.0\_MX8MP-BETA2&appType=file1&DOWNLOAD\_ID=null](https://www.nxp.com/webapp/sps/download/license.jsp?colCode=L5.4.47_2.2.0_MX8MP-BETA2&appType=file1&DOWNLOAD_ID=null)

\[2\]: [https://www.nxp.com/docs/en/user-guide/IMX\_LINUX\_USERS\_GUIDE.pdf](https://www.nxp.com/docs/en/user-guide/IMX_LINUX_USERS_GUIDE.pdf)

