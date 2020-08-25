---
description: Suggested proposal for the hostname of NavQ
---

# Setting the NavQ hostname



Since several NavQs might be present in a Wifi Network it's essential to set an unique hostname to determine which one is the correct NavQ you want to connect to.

To change the hostname you need to modify _`/etc/hostname`_ . We suggest the following format:

```text
navq-[Vehicle Mavlink SysID]
```

e.g. If Mavlink SysID is 10 the NavQ should be named **navq-10**

### **Adjusting the hostname with nano**

```text
~$ sudo nano /etc/hostname
```

```text
navq-10
```

### Adjusting the hostname with echo command

```text
~$ sudo echo navq-10 > /etc/hostname
```

After a reboot the new hostname will be visible on the network.

