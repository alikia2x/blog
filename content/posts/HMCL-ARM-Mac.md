---
title: 如何在ARM Mac上使用HMCL玩Minecraft
date: 2024-01-14T01:53:08+08:00
draft: false
tags:
  - Mac
---

## 下载JDK

在[azul.com](https://www.azul.com/downloads/?os=macos&architecture=arm-64-bit&package=jdk#zulu)上下载为ARM Mac构建的Java 17 JDK

安装完成后，可以通过运行命令 `/usr/libexec/java_home -V` 来查看系统中安装的所有 Java 的版本，如：

```shell
/usr/libexec/java_home -V
Matching Java Virtual Machines (4):
    21.0.1 (arm64) "Oracle Corporation" - "Java SE 21.0.1" /Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home
    17.0.9 (arm64) "Azul Systems, Inc." - "Zulu 17.46.19" /Library/Java/JavaVirtualMachines/zulu-17.jdk/Contents/Home
    11.0.16.1 (arm64) "Microsoft Build of OpenJDK" - "Microsoft Build of OpenJDK 11" /Library/Java/JavaVirtualMachines/microsoft-11.jdk/Contents/Home
    1.8.0_302 (x86_64) "Eclipse Temurin" - "Eclipse Temurin 8" /Library/Java/JavaVirtualMachines/temurin-8.jdk/Contents/Home
/Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home
```

如果你的系统中有多个 Java 版本，这里都会显示出来，其中 17.0.1 这一行就是之前安装的 Zulu JDK 17。我们可以通过修改 `~/.zshrc` 来设置 `JAVA_HOME` 环境变量，改变系统默认的 Java 版本。

将下面的内容添加到 `~/.zshrc` 末尾。

```shell
export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-17.jdk/Contents/Home
```

执行`. ~/.zshrc`并重启终端，设置生效。

执行`java --version`，即可查看当前java版本，例如：

```shell
java --version
openjdk 17.0.9 2023-10-17 LTS
OpenJDK Runtime Environment Zulu17.46+19-CA (build 17.0.9+8-LTS)
OpenJDK 64-Bit Server VM Zulu17.46+19-CA (build 17.0.9+8-LTS, mixed mode, sharing)
```

## 下载HMCL

在HMCL的[Releases页面](https://github.com/huanghongxun/HMCL/releases)，下载启动器（jar），如[HMCL-3.5.5.jar](https://github.com/huanghongxun/HMCL/releases/download/release-3.5.5/HMCL-3.5.5.jar)

新建一个目录，用于存放文件，如`~/Games/Minecraft`，将启动器放在该目录下。

```shell
mkdir -p ~/Games/Minecraft/
mv ~/Downloads/HMCL.jar ~/Games/Minecraft
cd ~/Games/Minecraft
java -jar HMCL.jar # 打开HMCL
```

## 将HMCL打包成App

创建一个文件夹`HMCL.app`，在其中创建一个bash脚本，内容为：

```bash
#!/bin/bash
java \-jar launcherLocation/HMCL.jar
```

将`launcherLocation`替换为你存放启动器的位置，保存
并在同目录下创建一个`Contents`目录，在  `Contents`中创建`info.plist`，写入以下内容

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<plist version="1.0">
 <dict>
   <key>CFBundleExecutable</key>
   <string>HMCL</string>
   <key>CFBundleGetInfoString</key>
   <string>HMCL 3.5.5</string>
   <key>CFBundleVersion</key>
   <string>3.5.5</string>
   <key>CFBundleShortVersionString</key>
   <string>3.5</string>
 </dict>
</plist>

```

版本什么的，可以随便写写，无所谓。

怎么给它添加一个好看的图标呢？  
首先，我们可以在[macOSicons](https://macosicons.com)网站上，找一个喜欢的图标（顺便安利一下这个网站，上面有很多制作精美的macOS应用图标，全部都是免费下载），将它下载下来，选中文件并拷贝（`command+c`)  
接下来右键你的`.app`文件，选中`Get Info`（“显示简介”），之后选中窗口左上角一个有着“空白App图标”的圆角矩形，它会附有一个蓝色的边框（如图），此时，按下`command+v`（粘贴），图标更换成功。

![给HMCL添加图标](/HMCLAddIcon.png)

最后，将制作好的`.app`拖到`Applications`文件夹（如图），你就可以在启动台看到它啦～

![Applications文件夹下的HMCL](/HMCLinApplications.png)

最后，愉快的玩耍吧～

![HMCL主页面](/HMCL-Main.png)
