---
title: 使用 mDNS 和 Caddy 在本地部署带域名和 HTTPS 的服务
date: 2025-12-13T00:22:08+08:00
draft: false
summary: 本文将介绍如何结合 **mDNS**（多播 DNS）和 **Caddy** 服务器，在局域网内为你的服务分配合适的域名，并自动启用 HTTPS。这样，无论是在同一网络下的 Mac、iPhone 还是 iPad 上，你都能像访问互联网上的网站一样，通过自定义域名安全、方便地访问本地服务。
---

在本地开发或搭建服务时，你是否觉得每次都输入 `localhost:端口` 或 `192.168.x.x` 的 IP 地址有些繁琐？能否给本地服务一个像 `my-service.local` 这样的自定义域名，并且还配上安全的 HTTPS 访问？答案是肯定的。

本文将介绍如何结合 **mDNS**（多播 DNS）和 **Caddy** 服务器，在局域网内为你的服务分配合适的域名，并自动启用 HTTPS。这样，无论是在同一网络下的 Mac、iPhone 还是 iPad 上，你都能像访问互联网上的网站一样，通过自定义域名安全、方便地访问本地服务。

> 本文环境与测试范围：方法已在 macOS、iOS、iPadOS 上验证通过，其他操作系统（如 Windows、Linux）或设备可能需要进行适配。

## 原理简介

整个方案主要分为两步：

1. **使用 mDNS 广播域名**：通过 Python 脚本，在局域网内声明并广播你想要的域名（如 `my-service.local`），将其指向本机（或指定设备）的 IP 地址。这样，局域网内的其他设备就能通过该域名直接访问到你的服务。
2. **使用 Caddy 提供 HTTPS 反向代理**：Caddy 是一个现代化的 web 服务器，它能自动为本地域名申请并配置 HTTPS（使用自签名证书），同时将请求反向代理到你实际运行的服务（比如 `localhost:8080`）。

下面，我们分步实现。

## 第一步：配置 mDNS 广播域名

我们使用 Python 的 `zeroconf` 库来实现 mDNS 广播。如果你的 Python 环境尚未安装此库，可以通过 `pip install zeroconf` 安装。

将以下脚本保存为 `broadcast.py`，并根据你的网络情况修改配置部分。

```python
import socket
import time
import sys
import logging
from typing import List

# 尝试导入 zeroconf，如果未安装则提示
try:
    from zeroconf import Zeroconf, ServiceInfo, IPVersion
except ImportError:
    print("错误: 请先安装 zeroconf 库。运行: pip install zeroconf")
    sys.exit(1)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def broadcast_aliases(target_ip: str, hostnames: List[str]):
    """
    广播多个域名指向同一个IP
    """
    # 初始化 Zeroconf 对象
    zc = Zeroconf(ip_version=IPVersion.V4Only)
    infos = []

    try:
        # 将 IP 字符串转换为字节流 (mDNS 需要 bytes 格式的地址)
        ip_bytes = socket.inet_aton(target_ip)

        for i, hostname in enumerate(hostnames):
            # 确保域名以 .local. 结尾
            if not hostname.endswith(".local"):
                full_hostname = f"{hostname}.local."
            else:
                if not hostname.endswith("."):
                    full_hostname = f"{hostname}."
                else:
                    full_hostname = hostname

            # 去掉 .local. 后缀作为服务实例名称的一部分，避免重复
            short_name = full_hostname.replace(".local.", "")
            
            # 我们需要注册一个服务（例如 HTTP），并将其关联到我们想要的“虚拟主机名”
            # mDNS 主要是服务发现，但副作用是它会解析关联的 server 域名
            service_type = "_http._tcp.local."
            service_name = f"Service-{short_name}.{service_type}"
            
            info = ServiceInfo(
                service_type,
                service_name,
                addresses=[ip_bytes],
                port=80, # 端口不重要，我们主要是为了广播主机名
                properties={'desc': f'Broadcast for {short_name}'},
                server=full_hostname # 这里是关键：指定这个服务由哪个“主机名”提供
            )

            logger.info(f"正在广播: {full_hostname} -> {target_ip}")
            zc.register_service(info)
            infos.append(info)

        logger.info("服务已启动。按 Ctrl+C 停止广播...")
        
        # 保持脚本运行
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("正在停止广播...")
    except Exception as e:
        logger.error(f"发生错误: {e}")
    finally:
        # 清理并注销服务
        for info in infos:
            zc.unregister_service(info)
        zc.close()
        logger.info("广播已结束。")

if __name__ == "__main__":
    # --- 配置区域 ---
    
    # 1. 设置你想指向的 IP 地址
    # 请替换为你的本机局域网 IP，例如 "192.168.1.100"
    # 建议配合路由器的 DHCP 静态 IP 分配功能，或者可以编写代码动态获取本机 IP
    TARGET_IP = "192.168.1.1" 

    # 2. 设置你想声明的域名列表（不需要加 .local，脚本会自动处理，也可以加）
    MY_HOSTNAMES = [
        "my-service",
        # 你可以添加更多别名，例如 "api.local", "test.local"
    ]

    # --- 开始运行 ---
    print(f"目标 IP: {TARGET_IP}")
    broadcast_aliases(TARGET_IP, MY_HOSTNAMES)
```

**运行与说明**:
1. 将 `TARGET_IP` 改为你的本机在局域网中的 IP 地址（可在系统设置中查看）。
2. 在 `MY_HOSTNAMES` 列表中添加你想要的域名（推荐使用 `.local` 顶级域，这是 mDNS 的标准做法）。
3. 在终端运行 `python broadcast.py` 启动广播。只要脚本在运行，局域网内的其他设备就能通过 `my-service.local` 等域名解析到你的 IP。
4. 你可以按 `Ctrl+C` 停止广播。

## 第二步：配置 Caddy 作为 HTTPS 网关

Caddy 服务器的优势在于配置简单且能自动管理 HTTPS。首先，请确保你已经[安装 Caddy](https://caddyserver.com/docs/install)。

创建一个名为 `Caddyfile` 的配置文件（无后缀），内容如下：

```text
my-service.local {
    reverse_proxy localhost:8080
}
```

这个配置告诉 Caddy：
* 监听对 `my-service.local` 的请求。
* 自动为这个域名启用 HTTPS（使用自签名证书）。
* 将所有请求转发（反向代理）到本机 `8080` 端口运行的实际服务。

请将 `localhost:8080` 替换为你服务的实际地址和端口。

## 第三步：启动 Caddy 服务

在终端中，切换到 `Caddyfile` 所在目录，运行以下命令启动 Caddy：

```bash
caddy start
```

Caddy 会读取同目录下的 `Caddyfile` 并开始在后台运行。你也可以使用 `caddy stop` 停止服务，或使用 `caddy run` 在前台运行并查看日志。

现在，在同一局域网内的设备上，你已经可以通过 `https://my-service.local` 访问你的服务了。但首次访问时，浏览器会提示“不安全连接”，这是因为我们使用的是 Caddy 自动生成的自签名证书，需要手动信任。

## 第四步（可选）：信任自签名根证书（以 iOS 为例）

Caddy 会自动在宿主机安装并信任其根证书，但如果你需要用其它设备（如 iPhone）访问，就需要在该设备上信任此证书。

1.  **找到根证书**：
    *   **在运行 Caddy 的 Mac 上**：证书通常位于 `$HOME/Library/Application Support/Caddy/pki/authorities/local/root.crt`。
    *   你也可以参考 Caddy 官方文档关于[自动 HTTPS](https://caddyserver.com/docs/automatic-https) 的部分确认路径。

2.  **安装证书**：
    将 `root.crt` 文件通过 AirDrop 发送到你的设备。在设备上点击该文件，系统会提示你“安装描述文件”。前往“设置” > “通用” > “VPN 与设备管理”，找到并安装该证书描述文件。接着，进入“设置” > “通用” > “关于本机” > “证书信任设置”，找到并开启对你刚刚安装的根证书的完全信任。

完成这些步骤后，刷新页面或重新访问 `https://my-service.local`，你将看到一个带有安全锁标志的、完全受信任的 HTTPS 连接。

## 最终效果

至此，你已经成功搭建了一个本地服务，它不仅拥有一个易于记忆的自定义域名（如 `my-service.local`），还配备了自动管理的 HTTPS 加密。无论是开发测试、内网工具分享，还是家庭媒体中心，这套方案都能显著提升访问体验的便捷性和安全性。

你可以自由扩展 `Caddyfile`，配置多个不同的域名指向不同的本地服务端口，轻松管理你的整个本地开发环境。
