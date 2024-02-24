---
title: Add a user to grop on Linux
date: 2024-02-22T01:46:49+08:00
draft: false
summary: usermod -a -G group user
tags:
    - Lookup
    - Linux
---

## Add user to group

For example, add user `alikia` to group `git`:

```bash
usermod -a -G alikia git
```

## Change a User's Primary Group

While a user account can be part of multiple groups, one of the groups is always the "primary group" and the others are "secondary groups". The user's login process and files and folders the user creates will be assigned to the primary group.

For example, set the primary group of user `user1` to `group1` :

```bash
usermod -g group1 user1
```

## View the Groups a User Account is Assigned To

To view the groups the current user account is assigned to, run the `groups` command. You'll see a list of groups.

Add argument after `groups` to specify which user's group you want to view, eg:

```text
alikia@alikia2x:~$ groups
alikia sudo
```

> Example 1: The user `alikia` is assigned to `alikia` and `sudo` groups.

```text
alikia@alikia2x:~$ groups git
git : git alikia
```

> Example 2: The user `git` is assigned to `git` and `alikia` groups.

## Reference

\[1\] [How-To Geek](https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/)
