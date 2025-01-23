---
title: Open swap on Linux
date: 2024-01-14 01:02:21
draft: false
summary: Quick tutorial to enable swap on Linux
tags:
    - Lookup
    - Linux
---

```shell
cd /
sudo touch swap
sudo dd if=/dev/zero of=/swap bs=1M count=4096
sudo mkswap /swap
sudo swapon /swap
sudo chmod 0600 /swap
```

These commands will create a 4GB swapfile at /swap. You can modify the parameters as needed.
