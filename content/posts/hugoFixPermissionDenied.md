---
title: Hugo 解决生成时权限问题
date: 2024-02-22T01:57:02+08:00
draft: false
tags:
    - 快查
    - Linux
---

在使用 `hugo` 命令生成时，可能会遇到类似下面的报错：

***Error: error copying static files: chmod /path/to/your/blog operation not permitted.***

***Error: error copying static files: chtimes /path/to/your/blog: operation not permitted.***

这时，我们只需将命令改为 `hugo --noChmod --noTimes`，即可解决问题。
