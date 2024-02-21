---
title: Linux下开启交换分区
date: 2024-01-14 01:02:21
draft: false
tags:
    - 快查
    - Linux
---

没有废话，只有代码：

```shell
cd /
sudo touch swap
sudo dd if=/dev/zero of=/swap bs=1M count=4096
sudo mkswap /swap
sudo swapon /swap
sudo chmod 0600 /swap
```

这段命令会在根目录下创建/swap，其大小为4GB，可以根据需要修改为合适的大小。
