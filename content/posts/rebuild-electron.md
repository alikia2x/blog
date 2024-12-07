---
title: Electron 应用报错 Compiled against a different Node.js version 如何解决
date: 2024-12-07T22:53:18+08:00
draft: false
summary: 有时候 Electron 应用启动时会遇到 ... was Compiled against a different Node.js version using NODE_MODULE_VERSION xxx. This version of Node.js requires NODE_MODULE_VERSION xxx. Please try re-compiling or re-installing the module 的报错，该如何解决呢
tags:
    - Electron
    - 前端
    - Node.js
---

好吧我承认是水了一篇博客。

参考 [Stackoverflow](https://stackoverflow.com/a/52796884/21100709)，

解决方案如下：

1. 将 `electron-build` 安装为开发依赖
2. 删掉整个 `node_modules` 和软件包管理器的版本锁定文件（如 `packages-lock.json`）
3. 重新使用包管理器安装依赖
4. 运行 electron-build:
    - macOS 和 Linux 用户直接执行 `./node_modules/.bin/electron-rebuild`
    - Windows 用户执行 `.\node_modules\.bin\electron-rebuild.cmd`