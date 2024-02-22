---
title: 第二课 配置Python环境
date: 2022-07-25 01:05:57
tags:
- python教程
- 计算机
---

## **Windows 系统**

> 本章适用于 Windows 操作系统。通常来说，如果你使用的不是 Mac 电脑，那么你的电脑大概率运行的是 Windows 操作系统。

### Python 的版本

**Python 分为两个主要的大版本，Python2 与 Python3。
Python3 有更新的特性，但其与 Python2 不兼容。
网络上的部分资料和程序仍是基于 Python2 编写，请仔细辨别。它们大概率无法在 Python3 环境中运行
本教程使用 Python3.11.0 作为演示。**

### 镜像下载

所谓 *镜像*，实际上是一个和源服务器内容保持一致的高速服务器
由于很多项目使用人数遍布世界各地，因此每个地区的人们为了能够享受到更高的下载速度，就搞出了「镜像」这个玩意
往往，选择合适的镜像能让你的下载速度提升很多。因此我强烈建议你使用镜像下载（因为笔者曾经在官网用 10KB/s 的速度，耗时半小时却下载了一个版本不合适的安装包）
这里推荐一个 [国内比较快的镜像](https://registry.npmmirror.com/binary.html?path=python/)
打开之后，你大概会看到很多文件夹，分别对应了 Python 的各个版本
点击你需要的版本后，会看到如下界面  

> 如果你是 64 位系统，请点击 *python-3.11.0-amd64.exe* 以下载
> 如果你是 32 位系统，请点击 *python-3.11.0.exe* 以下载

![镜像网站下载界面](/img/Screen4.png)

### 官网下载

当然，也可以从 Python 的官方网站下载 Python 安装包。
Python 的官方网站是 [python.org](https://python.org)
进入网站后，你将看到如下界面
点击 [Downloads](https://www.python.org/downloads/)（图中用白色方框圈起来的地方)
![Python 官方网站](/img/Screen5.png)  

点击 *Downloads* 后，你会来到另一个界面，点击 [*Download Python 3.11.0*](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)。默认情况下，你会直接下载到适合你电脑系统的版本。

![Python 官网下载界面](/img/Screen6.png)

### 安装

下载完成后，双击安装包，开始安装。

1. 勾选 *Add Python 3.11 to PATH* 后，点击 *Customize installation*
![安装界面](/img/Screen11.png)
2. 接下来，点击 *Next*
![第二步](/img/Screen12.png)
3. 点击 *Browse*，选择合适的安装位置，然后点击 *Install*
![第三步](/img/Screen13.png)
4. 当出现 *Setup was successful* 时，表明安装成功
![完成](/img/Screen15.png)

### 确认安装

接下来，我们需要做一些操作来确保你的电脑上成功安装了 Python

打开 **开始** 菜单，并在其中寻找 Python

如果可以在开始菜单中找到 Python，点击 IDLE，当你看到包含 Python 的输出时，则表示安装成功。

## **Linux 系统**

大多数 Linux 系统的发行版已经内置了 Python，你可以在终端键入 **python** 命令来验证你的系统是否安装 python。如果出现报错或发现输出的版本为 Python2，你可以试着输入 **python3** 命令。

如果你的 Linux 中没有 Python3，你可以试着用自己发行版内置的包管理器安装

比如在 Debain 及其衍生系统（如 Ubuntu）中，可以输入

```bash
sudo apt install python3
```

在 RedHat 及其衍生系统（如 CentOS）中，可以输入

```bash
sudo yum install python3
```

## **MacOS**

> 此节改自 [Python 官方文档](https://docs.python.org/zh-cn/3/using/mac.html)

在运行 macOS 的 Mac 上的 Python 原则上与在其他 Unix 平台上的 Python 非常相似，但有一些额外的特性，如 IDE 和包管理器。

macOS 从 10.8 版开始就由苹果预装了 Python 2.7 。你也可以从 Python 网站 ([https://www.python.org](https://www.python.org/)) 安装最新的 Python 3 版本。 那里有当前的 Python 的 “通用二进制” 版本，它可以在 Mac 的新 Intel 和传统的 PPC CPU 上运行。

你安装后会得到：

- 一个 `Python 3.11` 文件夹在你的 `Applications` 文件夹中。 在这里你可以找到 IDLE，它是为官方 Python 发行版标准组成部分的开发环境；以及 PythonLauncher，它负责处理在 Finder 中双击 Python 脚本的操作。
- 框架 `/Library/Frameworks/Python.framework` ，包括 Python 可执行文件和库。安装程序此位置添加到 shell 路径。 要卸载 MacPython ，你可以简单地移除这三个项目。 Python 可执文件的符号链接放在 /usr/local/bin/ 中。

Apple 提供的 Python 版本分别安装在 `/System/Library/Frameworks/Python.framework` 和 `/usr/bin/python` 中。 你永远不应修改或删除这些内容，因为它们由 Apple 控制并由 Apple 或第三方软件使用。 请记住，如果你选择从  python.org 安装较新的 Python 版本，那么你的计算机上将安装两个不同但都有用的 Python  ，因此你的路径和用法与你想要执行的操作一致非常重要。
