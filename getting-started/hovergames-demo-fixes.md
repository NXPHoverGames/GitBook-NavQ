---
description: Ensure your NavQ is working correctly with these fixes
---

# HoverGames-Demo Bugs/Fixes

## Overview

Currently, the HoverGames-Demo image is in a beta state. Over time we will be improving the image by fixing bugs and including even more software so that it's more of an out-of-the-box experience. Here are some of the current fixes at the moment to get a working system.

{% hint style="info" %}
These fixes are for the build on 7/24/2020. This page will be updated for each new release.
{% endhint %}

## Quick Workarounds

* WiFi sometimes does not automatically connect to the last WiFi network after reboot.
  * Workaround: Open connmanctl, run `disable wifi`, and reconnect using the instructions in the Quick Start Guide.

## Setting timezone

Setting the timezone on your NavQ is necessary to ensure the `apt` package manager works. First, you'll need to locate the correct timezone file at `/usr/share/zoneinfo`. There should be a folder for your country and a file in that folder for the closest city to you.

```text
$ rm -f /etc/localtime
$ ln -sf /usr/share/zoneinfo/<country>/<city> /etc/localtime
```

For example, if you're in Central Time USA, you'd use the following commands:

```text
$ rm -f /etc/localtime
$ ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime
```

Now, you can run `sudo apt update` and `sudo apt upgrade` to get your system up to date.

