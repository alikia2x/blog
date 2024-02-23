---
title: Bash 获取当前用户名
date: 2024-02-23 18:45:38
draft: false
tags:
    - 快查
    - Mac
---

| 系统版本 | 使用的命令 |
| --- | --- |
| macOS 14 (Sonoma) | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` |
| macOS 13 (Ventura) | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` |
| macOS 12 (Monterey) | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` |
| macOS 11 (Big Sur) | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` |
| macOS 10.15 (Catalina) | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` |
| macOS 10.14 (Mojave) | `sudo killall -HUP mDNSResponder` |
| macOS 10.13 (High Sierra) | `sudo killall -HUP mDNSResponder` |
| macOS 10.12 (Sierra) | `sudo killall -HUP mDNSResponder` |
| OS X 10.11 (El Capitan) | `sudo killall -HUP mDNSResponder` |
| OS X 10.10 (Yosemite) | `sudo discoveryutil udnsflushcaches` |
| OS X 10.9 (Mavericks) | `sudo killall -HUP mDNSResponder` |
| OS X 10.8 (Mountain Lion) | `sudo killall -HUP mDNSResponder` |
| Mac OS X 10.7 (Lion) | `sudo killall -HUP mDNSResponder` |
| Mac OS X 10.6 (Snow Leopard) | `sudo dscacheutil -flushcache` |
| Mac OS X 10.5 (Leopard) | `sudo lookupd -flushcache` |
| Mac OS X 10.4 (Tiger) | `lookupd -flushcache` |