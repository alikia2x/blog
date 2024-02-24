---
title: Linux 将某用户添加到组
date: 2024-02-22T01:46:49+08:00
draft: false
summary: usermod -a -G group user
tags:
    - 快查
    - Linux
---

## 将用户添加到组

例如，欲将 `git` 用户添加到 `alikia` 组中，使得 `git` 能够访问 `alikia` 组拥有的文件，则可以执行

```bash
usermod -a -G alikia git
```

## 设置用户的“主要组”

虽然用户可以属于多个组，但其中一个组始终是“主要组”，其他组是“次要组”。用户的登录过程以及用户创建的文件和文件夹将被分配到主要组。

欲更改某用户的主要组，可以执行：

```bash
usermod -g group user
```

这个命令将用户 `user` 的主要组修改为 `group` .

## 查看用户分配到的组

要查看当前用户分配到的组，执行 `groups` 命令。

`groups` 命令后可以跟参数，表示查看对应用户属于哪个组。

例如：

```text
alikia@alikia2x:~$ groups
alikia sudo
```

表明当前用户 `alikia` 被分配到 `alikia` 和 `sudo` 两个组。

```text
alikia@alikia2x:~$ groups git
git : git alikia
```

表明用户 `git` 被分配到 `git` 和 `alikia` 两个组。
