# Package Management

To use the package manager \(`apt`\) on the Demo image, you'll need to change your timezone.

First, you'll need to locate the correct timezone file at `/usr/share/zoneinfo`. There should be a folder for your country and a file in that folder for the closest city to you.

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



