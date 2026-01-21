---
title: Serving Local Services with Custom Domains & HTTPS Using mDNS + Caddy
date: 2025-12-13T00:22:08+08:00
draft: false
summary: Combine mDNS (via a tiny Python script) with Caddy to give your local services friendly `.local` domain names and automatic HTTPS — no manual hosts-file edits, no port numbers in the browser, and a proper padlock on Apple devices (and many others).
---

Tired of typing `http://localhost:4321` or `http://192.168.5.77:8080` every time you want to check your dev server, home media app, or side-project dashboard? What if you could just open `https://dash.local`, `https://media-box.local`, or whatever name feels natural — with a valid-looking HTTPS connection and no scary security warnings (after a one-time trust step)?

You can — and the combination of **mDNS** (multicast DNS) + **Caddy** makes it surprisingly clean, especially in Apple-heavy households or small offices.

> Tested and working smoothly on macOS, iOS, iPadOS. Windows and Linux clients usually need either Avahi or manual `/etc/hosts` entries (or you can run the same mDNS broadcaster there too).

## How It Works — High Level

1. A short Python script uses the `zeroconf` library to advertise one or more `.local` hostnames and point them at your machine’s LAN IP.  
   Any mDNS-aware device on the same network (most modern ones) will resolve those names automatically.

2. Caddy listens for HTTPS traffic on those names, generates & uses its own locally-trusted self-signed certificate (via its internal CA), and reverse-proxies the requests to whatever port your real app is running on.

That’s it — memorable domain + encrypted transport + no port in the URL.

## Step 1 — Broadcast the .local Name(s) with mDNS

Install the dependency if you haven’t already:

```bash
pip install zeroconf
```

Save the following as `broadcast-names.py` (or whatever name you like):

```python
import socket
import time
import logging
from typing import List
from zeroconf import Zeroconf, ServiceInfo, IPVersion

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(message)s")
logger = logging.getLogger("mDNS")

def advertise_hostnames(target_ip: str, hostnames: List[str]):
    zc = Zeroconf(ip_version=IPVersion.V4Only)
    services = []

    try:
        ip_bytes = socket.inet_aton(target_ip)

        for name in hostnames:
            # Normalize to full .local. form
            if not name.endswith(".local"):
                fqdn = f"{name}.local."
            elif not name.endswith("."):
                fqdn = f"{name}."
            else:
                fqdn = name

            short = fqdn.replace(".local.", "")

            # Advertise a dummy _http._tcp service — the important part is the 'server' field
            info = ServiceInfo(
                type_="_http._tcp.local.",
                name=f"{short}._http._tcp.local.",
                addresses=[ip_bytes],
                port=80,                        # port is mostly ignored here
                properties={b"desc": f"mDNS alias for {short}"},
                server=fqdn,
            )

            logger.info(f"Advertising  {fqdn}  →  {target_ip}")
            zc.register_service(info)
            services.append(info)

        logger.info("Names are now being advertised. Press Ctrl+C to stop.")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("Shutting down…")
    except Exception as exc:
        logger.error(f"Something went wrong: {exc}")
    finally:
        for svc in services:
            zc.unregister_service(svc)
        zc.close()
        logger.info("Cleaned up.")

if __name__ == "__main__":
    # ──────────────── Customize here ────────────────
    MY_IP = "192.168.1.42"               # ← your LAN IP
    NAMES = [
        "dash",
        "media",
        # "grafana", "prometheus", etc.
    ]
    # ───────────────────────────────────────────────

    print(f"Advertising from IP: {MY_IP}")
    advertise_hostnames(MY_IP, NAMES)
```

**Quick usage:**

- Update `MY_IP` (check with `ifconfig` / `ipconfig` / Settings → Network)
- Add as many friendly names as you want in `NAMES`
- Run:  `python broadcast-names.py`

Leave the terminal open (or daemonize it later if you prefer).

## Step 2 — Let Caddy Handle HTTPS & Proxying

Install Caddy if you haven’t: https://caddyserver.com/docs/install

Create a file named `Caddyfile` (no extension) next to wherever you want to run it:

```caddy
dash.local {
    reverse_proxy localhost:4321
}

media.local {
    reverse_proxy 127.0.0.1:9000
}
```

That’s literally all you need for most cases. Caddy will:

- Bind to :443 (and :80 → redirect)
- Generate a self-signed cert from its internal CA
- Trust that CA automatically on the host machine (macOS usually does this seamlessly)
- Forward traffic to the backend you specified

Start it:

```bash
caddy run    # foreground, nice logs
# or
caddy start  # background
```

## Step 3 — Trust the Certificate on Other Devices (One-Time)

On the machine running Caddy everything “just works” in most browsers.

For phones, tablets, other computers:

1. Locate Caddy’s root CA certificate  
   Typical location on macOS:  
   `~/Library/Application Support/Caddy/pki/authorities/local/root.crt`

2. Transfer it to the target device (AirDrop, email, etc.)

3. **iOS/iPadOS**:
   - Tap the .crt file → Install profile
   - Go to Settings → General → VPN & Device Management → install the profile
   - Then Settings → General → About → Certificate Trust Settings → enable full trust for the new CA

4. **Other platforms** — import the cert into the system trust store (slightly different steps per OS/browser).

After that one-time setup, `https://dash.local` should show a green padlock with no warnings.

## Bonus Tips

- Want the mDNS script to auto-detect your IP? Use `socket.getaddrinfo(socket.gethostname(), None)` or the `netifaces` / `ifaddr` package.
- Multiple machines? Run the broadcaster + Caddy on each, just use different `.local` names.
- Need subdomains (`api.dash.local`)? Some mDNS implementations are picky; test carefully or stick to flat names.
- Production at-home services? Consider a real domain + Tailscale / Headscale + DNS-01 challenge for publicly valid certs — but for pure-LAN that’s usually overkill.

Enjoy the civilized internet-feeling experience on your local network.