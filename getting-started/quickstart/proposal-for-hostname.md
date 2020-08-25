---
description: this is a proposal for the hostname of NavQ
---

# Proposal for hostname



Since several NavQs might be present in a Wifi Network it's essential to set an unique hostname to determine the "right" navq one likes to connect to.

Modify _/etc/hostname_ with a unique host name. Proposal is to use

```text
navq-[Vehicle Mavlink SysID]
```

e.g. if Mavlink SysID is 10 the navq should be named **navq-10**

## **setting the hostname**

I'm in favour of the editor nano. Install nano with \(internet access required\).

```text
~$ sudo apt install nano
```

#### **adjust the hostname with nano**

```text
~$ sudo nano /etc/hostname
```

```text
navq-10
```

#### adjust the hostname with echo command

```text
~$ sudo echo navq-10 > /etc/hostname
```

After a reboot the new hostname will be visible on the network.

