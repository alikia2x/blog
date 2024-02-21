---
title: 搭建一个 Hugo 站点作为个人博客
date: 2024-02-22T02:01:53+08:00
draft: false
---

> 本页面不断更新，反映本站的搭建及维护流程。

## 安装

参考 [Hugo 官方教程](https://gohugo.io/installation/)

### [Debian / Ubuntu](https://gohugo.io/installation/linux/#debian)

使用如下命令在 Debian 系发行版安装 Hugo：

```bash
sudo apt install hugo
```

然而，实际部署时发现 apt 安装的似乎不是最新版……

此时在 [GitHub Releases](https://github.com/gohugoio/hugo/releases/latest) 页面下载最新的 `.deb` 包，再 `sudo apt install` 下载下来的包即可。

### [macOS](https://gohugo.io/installation/macos/)

如果使用 [Homebrew](https://brew.sh/)，那么非常简单，只需

```bash
brew install hugo
```

### 其他系统

~~自生自灭吧~~

可以参考[官方文档](https://gohugo.io/installation)

## 初始化

使用 [PaperMod](https://github.com/adityatelange/hugo-PaperMod/) 主题，也是本站所用的主题。

这一步我后来发现在本地执行比较好（如果你要跟着后面的教程配置 Git 的远程提交的话）

```bash
hugo new site blog
cd blog
git init
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
echo "theme: 'PaperMod'" >> hugo.toml
```

之后，建议在 `hugo.toml` 中修改一下基本的信息。

## 配置 Git

目前，寒寒发现相对方便的使用 Hugo 的方式为：在任意地方编辑，使用 Git 提交到服务器，服务器执行对应 Hook 以进行文件的拷贝及 Hugo 静态网页的生成。

因此，我们要配置好 Git:

1. `sudo adduser git`，添加对应用户
2. 将自己的公钥（通常位于本地机器 `~/.ssh/id_rsa.pub`）写入到`/home/git/.ssh/authorized_keys`文件中，一行一个。
3. `sudo chown -R git:git /path/to/your/repo.git` 确保 git 有访问权限。
4. 修改 `/etc/passwd` 文件，找到 git 开头的那一行，将最后的 `/bin/bash` 改为 `/usr/bin/git-shell`，改完后该行类似  
`git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell`  

5. `git clone --bare blog /path/to/your/repo.git` 创建一个裸仓库，作为服务器 git 仓库。
6. **在本地之前 Hugo 初始化的目录执行**： `git remote add myServer ssh://git@host:port/path/to/your/repo.git`，添加远程存储库。
7. `git push -f` 强制推送一下。
8. 配置 Hooks：这可是灵魂o(｀ω´ )o～在服务器的 git 裸仓库下的 `hooks` 目录，创建一个 `post-receive` 文件，写入如下内容：

```bash
#!/bin/sh

git --work-tree=/path/to/your/blog --git-dir=//path/to/your/repo.git/ checkout -f

cd /path/to/your/blog
hugo --noTimes --noChmod
```

其中，`/path/to/your/blog` 为服务器端博客的位置（我觉得，应该提前创建好会比较好？），其下的 `public` 目录将会是 nginx 等服务器软件的根目录。

### `.gitignore`的配置

Copy time!

```text
# Generated files by hugo
/public/
/resources/_gen/
/assets/jsconfig.json
hugo_stats.json

# Temporary lock file while building
/.hugo_build.lock
```

## 设置服务器软件

刚刚……已经说了，根目录就在服务器端博客目录下的 `public` 目录。只要执行一遍 `hugo`，就会有该目录。

之后，只要本地向服务器推送 Git 仓库，仓库的钩子就会自动拷贝文件到博客的目录，并执行 `hugo` 以生成静态文件。
