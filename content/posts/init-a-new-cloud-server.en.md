---
title: Init your new Ubuntu server (PostgreSQL + Redis + Deno/Node.js)
date: 2025-04-06T19:12:00+08:00
draft: false
summary: Provisioning a fresh cloud server for modern web development. This post walks through setting up PostgreSQL, Redis, and your favorite runtimes like Deno and bun.
tags:
    - DevOps
    - Server Setup
    - Linux
categories: Dev
---

## A clean slate

Starting fresh on a cloud server feels great—no clutter, no surprises, just you and a terminal.

This guide sets up a typical fullstack-ready environment: PostgreSQL, Redis, Node.js (with a side of Bun) or Deno, and good DevOps ergonomics with ZSH and some security basics.

In this blog, the commands without `sudo` prefix are executed under the root user by default. 
But once everything is ready, it may be safer to use your newly created user for future operations.

## Basic essentials

First, get your system up to date and grab a few basics.

```bash
apt update
apt upgrade -y
apt install -y curl wget vim git screen
```

These are the bare minimums. You’ll be using them a lot.


## Locking down SSH

Let’s tweak some basic security. Edit your SSH config:

```bash
vim /etc/ssh/sshd_config
```

Look for:

- `Port` – change it to something custom
- `PermitRootLogin` – switch this to `prohibit-password` or `no`

Run this on **your computer** if you don't have a SSH keypair:

```bash
ssh-keygen -t ed25519
cat .ssh/id_ed25519.pub
```

Copy the public key in the `cat` output, create the file `.ssh/authorized_keys` **on your server** and paste the key:

```bash
vim .ssh/authorized_keys
# Paste the key
# For example:
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL7Zk5I9svfvcKv0ZAMaCTD5MjW9wAHwl2I+DQboqd1Y username@yourcomputer
```

Then reload SSH:

```bash
systemctl restart ssh
reboot
```

Why? Because bots are real and they’re relentless.


## A new user, a new hostname

```bash
vim /etc/hostname # change to a one you like
adduser newuser
usermod -aG newuser
```

Create a user to actually work with—best practice is to avoid `root` as much as possible.


## Shell vibes: ZSH + Oh My Zsh

For a friendlier shell:

```bash
apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Then for your new user:

```bash
su newuser
chsh -s $(which zsh)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Update your `.zshrc`:

```bash
vim ~/.zshrc
```

Add:

```bash
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"

plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

alias ll='ls -alh'
alias la='ls -a'
alias c='clear'
```

Then install the extra plugins:

```bash
cd ~/.oh-my-zsh/custom/plugins
git clone https://github.com/zsh-users/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions
cd
source ~/.zshrc
```

A pleasant shell experience is underrated.


## Basic brute-force protection (Fail2ban)

Install and configure:

```bash
apt install -y fail2ban
systemctl start fail2ban
systemctl enable fail2ban
```

Custom config:

```bash
vim /etc/fail2ban/jail.local
```

Paste this:

```
[sshd]
enabled = true
port = 37192
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
findtime = 60
bantime = 3600
ignoreip = 127.0.0.1
```

Then:

```bash
systemctl restart fail2ban
```

This helps keep SSH brute-force attempts at bay.


## PostgreSQL

Add the PostgreSQL repo:

```bash
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
apt update
apt install postgresql-17
```

Then start and enable:

```bash
systemctl start postgresql
systemctl enable postgresql
```

Configure:

```bash
su - postgres
psql
```

In the prompt:

```sql
ALTER USER postgres WITH PASSWORD 'password';
CREATE USER user; -- Change it to a username you like
ALTER USER user WITH PASSWORD 'password';
\q
```

Then:

```bash
systemctl restart postgresql
```

Now your DB is ready.


## Redis

Simple and solid key-value store:

```bash
apt install -y redis-server
systemctl start redis-server
systemctl enable redis-server
```


## Nginx

Web server + reverse proxy:

```bash
apt install -y nginx
systemctl start nginx
systemctl enable nginx
```

You’ll set up actual sites/configs later, but this gets you going.

## Bun & Deno

Two modern runtimes worth having.

```bash
su newuser
sudo apt install unzip
sudo curl -fsSL https://deno.land/install.sh | sh
sudo curl -fsSL https://bun.sh/install | bash
```

They play nicely together.


## UFW – Because default deny is your friend

Enable and configure:

```bash
systemctl start ufw
systemctl enable ufw
ufw enable
```

Then allow only what you need:

```bash
ufw allow 80    # HTTP
ufw allow 443   # HTTPS
ufw allow 22 # Change it to the custom SSH port you specified
```


## Final thoughts

This setup doesn’t cover *everything*, but it gives you a sane, secure, and solid foundation to build on. From here, you can layer on Docker, CI/CD, SSL with Let's Encrypt, and deploy your apps however you like.
