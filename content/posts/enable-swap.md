---
title: Linux 下开启交换分区
date: 2024-01-14 01:02:21
draft: false
summary: 在 Linux 上开启交换分区 (swap) 的简明教程。
tags:
    - 快查
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

这段命令会在根目录下创建/swap，其大小为4GB，可以根据需要修改为合适的大小。
