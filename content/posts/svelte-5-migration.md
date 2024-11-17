---
title: Svelte 5 迁移与踩坑指南
date: 2024-11-17T20:11:00+08:00
draft: false
summary: Svelte 5发布了。这个万众瞩目的新兴前端框架，终于变成了React和Vue的形状。该如何从4.x迁移到Svelte 5版本呢？这里是我的踩坑指南。
tags:
    - Svelte
    - 前端
    - 踩坑
categories: 开发
---

## 「符文」——并不神秘的咒语

Svelte 5引入的Runes为开发者提供了一种全新的、细粒度的响应式编程方式，通过`$state`、`$derived`和`$effect`等API，让Svelte的响应式系统更加灵活和强大。

当然，代价是——以前符合直觉的写法消失了，它变得更像React了。

**例子**

Before: 
```html
<script>
	let count = 0;
    let doubleCount = 0;
    $: doubleCount = count * 2;
</script>

<button on:click={() => count++}>
	clicks: {count}, doubled: {doubleCount}
</button>
```

After: 
```html
<script>
	let count = $state(0);
    let doubleCount = $derived(count * 2);
</script>

<button onclick={() => count++}>
	clicks: {count}, doubled: {doubleCount}
</button>
```

详情可参见[这篇博客](https://svelte.dev/docs/svelte/what-are-runes)。

## 二选一

当我初看[Svelte 5 migration guide](https://svelte.dev/docs/svelte/v5-migration-guide)时，我粗略的看见了类似mix, old, new之类的字眼，
便相当然的认为Svelte 5可以在一个组件内同时使用新旧语法。

但是，我错了。

因为原文是：

> Svelte 5 still supports the old Svelte 4 syntax, and you can mix and match **components** using the new syntax with **components** using the old and vice versa.

也就是说，**如果你要使用新的符文语法，那么该组件内的所有旧语法都必须迁移到新语法**。

如果组件比较复杂，有较多的状态和属性，就可能得费点事了。

不过好在：

1. 起码它还兼容旧的语法。
2. API的更改不是特别复杂，因此你只要few-shots来给出一些examples，就可以用LLM代你完成。

## 不那么靠谱的迁移脚本

正如前文所说，Svelte 5的API其实变化没有那么大，更多是一些形式上的更改，因此官方贴心的提供了[迁移脚本](https://svelte.dev/docs/svelte/v5-migration-guide#Migration-script)。

但非常遗憾，这个脚本似乎并不支持TypeScript。

而[本次迁移的项目](https://github.com/alikia2x/aquavox)的所有核心部分全部使用了TypeScript，因此这个迁移脚本运行后只是在所有的文件第一行留下了 `Unexpected token` 的错误。
