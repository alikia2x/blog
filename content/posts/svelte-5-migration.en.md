---
title: Svelte 5 migration guide
date: 2024-11-17T20:11:00+08:00
draft: false
summary: Svelte 5 has been released. This highly anticipated emerging front-end framework has finally taken on the form of React and Vue. Here is my migration process and thoughts.
tags:
    - Svelte
    - Front-end
categories: Dev
---

## "Runes" – Not a mysterious incantation

Svelte 5 introduces Runes, providing developers with a new, fine-grained approach to reactive programming. Through APIs like `$state`, `$derived`, and `$effect`, Svelte's reactive system has become more flexible and powerful.

Of course, the trade-off is that the previously intuitive syntax has disappeared, making it more akin to React.

**Example**

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

For more details, refer to [this blog post](https://svelte.dev/docs/svelte/what-are-runes).

## Either-or

When I first glanced at the [Svelte 5 migration guide](https://svelte.dev/docs/svelte/v5-migration-guide), I vaguely noticed terms like "mix," "old," and "new," and assumed that Svelte 5 allowed the simultaneous use of both old and new syntax within a single component.

However, I was mistaken.

The original text states:

> Svelte 5 still supports the old Svelte 4 syntax, and you can mix and match **components** using the new syntax with **components** using the old and vice versa.

This means that **if you want to use the new runes syntax, all old syntax within that component must be migrated to the new syntax**.

If the component is complex, with numerous states and properties, this could be quite a task.

Fortunately:

1. At least it still supports the old syntax.
2. The API changes are not overly complex, so you can provide a few examples and use an LLM to handle the migration for you.

## The not-so-reliable migration script

As mentioned earlier, the API changes in Svelte 5 leads to a mild migration complexity, mostly involving formal adjustments. Therefore, the official documentation kindly provides a [migration script](https://svelte.dev/docs/svelte/v5-migration-guide#Migration-script).

Unfortunately, this script **does not seem to support TypeScript**.

And since [the project being migrated](https://github.com/alikia2x/aquavox) uses TypeScript for all its core components, running the migration script merely resulted in an `Unexpected token` error on the first line of every file.
