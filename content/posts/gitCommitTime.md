---
title: Git 提交时间修改完全指南
date: 2024-02-14T00:37:13+08:00
draft: false
tags:
    - 快查
---

## 问题简述 & 解决方案

如果你发现你的 `git log` 中的提交日期与GitHub上显示的不同，那么，

```bash
git filter-branch --env-filter 'export GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"'
git push -f
```

搞定。

## 背景

有时候，在进行变基 (rebase)等操作后，我们会发现 `git log` 中显示的提交事件和 GitHub 上显示的有所不同。
比如，如下 `git log`:

```text
commit 01c9fdea5badfb43fdf5f134f0134c2be2b70ad6 (HEAD -> main, tag: 1.1.0, origin/main)
Author: alikia2x <ziwen243@outlook.com>
Date:   Tue Feb 13 20:42:36 2024 +0800

    [fea] Version 1.1.0, done for index page
    with i18n, accessibility, dark mode support.

commit a1efe659bea99a2ab4a5f4606f444982e4e18a4b (tag: 1.0.0)
Author: alikia2x <ziwen243@outlook.com>
Date:   Sun Feb 11 17:47:37 2024 +0800

    [ver] Initial Commit, Version 1.0.0
```

在 [GitHub](https://github.com/alikia2x/WonderDays/commits/main/) 上的显示如下：
![Image](/GitHubCommitTime.png)

在2月11日和13日的两次提交，在经过变基等操作后在GitHub上显示为两次均在13日提交。

## 参考

[[1] GitHub Discussion](https://github.com/orgs/community/discussions/22695)
