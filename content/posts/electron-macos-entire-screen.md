---
title: macOS 上如何让程序完全占据整个屏幕（覆盖Dock和菜单栏）
date: 2024-11-24 23:23:00
draft: false
tags:
    - Mac
    - 前端
    - Electron
categories: 开发
---

最近在开发一个[rewind](https://www.rewind.ai/)替代品，我给它起名叫[openrewind](https://github.com/alikia2x/openrewind?tab=readme-ov-file).

这个项目是fork自一个名为[openrecall](https://github.com/openrecall/openrecall)的项目的。但由于fork的原项目实在太烂，
因此我决定直接重构项目，使用Electron驱动，顺便还改了个名字，~~更好地蹭rewind的热度~~

Rewind的回溯功能可以在不进入macOS原生全屏模式下，让整个窗口覆盖Dock和屏幕顶部的菜单栏。而我们也想复刻这个沉浸式的回溯效果。

![](/img/rewind-fullscreen.jpg)

但是却有一个问题：  
覆盖Dock似乎比较简单，但想要覆盖顶部菜单栏似乎是一件不可能的事——因为你发现自己甚至都不能把窗口移动到菜单栏所占据的那一部分空间。

![](/img/electron-failed-fullscreen.jpg)

而如果在Electron文档中搜索，你似乎找不到有什么选项可以做到这一点。

因此，我为这个功能寻找了两个小时，终于在一篇苹果关于[OpenGL](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_fullscreen/opengl_cgl.html)编程的古早文档中找到了进入全屏的方法。

核心代码是

```objc
NSWindow *fullScreenWindow = [[NSWindow alloc] initWithContentRect: mainDisplayRect styleMask:NSBorderlessWindowMask backing:NSBackingStoreBuffered defer:YES];
[fullScreenWindow setLevel:NSMainMenuWindowLevel+1];
```

其中，从直觉上看实现的关键似乎是窗口的level。

于是在[Issue #8153](https://github.com/electron/electron/issues/8153)和[Pull #8487](https://github.com/electron/electron/pull/8487)中，我找到了自定义Electron窗口level的方法。

在`setAlwaysOnTop`方法的第三个参数中，传入一个相对增量，则代表了你想在选定的窗口等级预设上增加多少级。

在这里，我们设置为在main-menu的基础上再加1，也就实现了`NSMainMenuWindowLevel+1`

```js
mainWindow.setAlwaysOnTop(true, 'main-menu', 1);
```

但是尝试过后——并没有生效啊？

于是我将目光放到了`NSBorderlessWindowMask`上。在Xcode中新建了刚刚苹果文档的示例后，它提示我这个东西已经标记弃用，取而代之的则是`NSWindowStyleMaskBorderless`.

我抱着试一试的心态在Electron代码库中检索了这个属性，并惊喜地发现它真的存在——对应的源码是这样

```objc
if (!rounded_corner && !has_frame())
    styleMask = NSWindowStyleMaskBorderless;
```

似乎，只要不是`rounded_corner`，且没有`frame`，就可以成功了。

由于我们已经设置`frame: false,`，因此只要在`BrowserWindow`的创建中加上`roundedCorners: false`，就可以实现啦~

![](/img/electron-fullscreen.jpg)
