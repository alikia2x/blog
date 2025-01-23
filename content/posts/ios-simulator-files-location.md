---
title: 如何找到iOS 模拟器中文件 App 中保存的文件？
date: 2025-01-23T20:28:02+08:00
draft: false
summary: 在 iOS 应用的开发调试过程中，我们会使用模拟器。那么当我们使用模拟器中的文件 App 时，里面的本机文件该怎么导出呢？实际上它们都保存在你 Mac 的本地磁盘中，下面就来教你如何找到它~
tags:
    - iOS
    - macOS
    - 快查
categories: 开发
---

运行下面这条命令：

`xcrun simctl listapps booted | grep "group.com.apple.FileProvider.LocalStorage"`

然后你可以看到类似下面的输出

```
            "group.com.apple.FileProvider.LocalStorage" = "file:///Users/alikia/Library/Developer/CoreSimulator/Devices/F56510E0-CE31-453E-8AB6-0C3CCDC9DC74/data/Containers/Shared/AppGroup/1EF10788-0FEF-46D2-806A-3E0BFF21D998/";
```

把后面那段路径加上`File Provider Storage`，也就是完整路径：`/Users/alikia/Library/Developer/CoreSimulator/Devices/F56510E0-CE31-453E-8AB6-0C3CCDC9DC74/data/Containers/Shared/AppGroup/1EF10788-0FEF-46D2-806A-3E0BFF21D998/File Provider Storage/`

打开 Finder，按下 `Shift + Command + G`，粘贴路径，然后就找到啦~

![](/img/iOSSimulatorFileAppLocation.png)
