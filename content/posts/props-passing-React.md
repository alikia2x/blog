---
title: Props 在 React 函数组件的传递
date: 2024-02-01T21:49:18+08:00
draft: false
summary: 最近在使用 React 进行开发时，发现了一个关于 props 容易被忽视的细节
cover:
    image: '/img/react.jpg'
    relative: true
    hidden: false
---

最近在使用 React 进行开发时，发现了一个容易被忽视的细节，特此分享。

在使用函数组件时，我们通常会定义一些 props，但要注意在传参的时候存在一些潜在的问题。

## 例子

让我们来看一个函数组件：

```jsx
const Search = (query, engine) => {
    ...
}
export default OneSearch;
```

在引用这个组件时，可能会这样写：

```html
<Search query={query} engine={engine} />
```

表面上看起来一切正常，但如果仔细观察函数组件的定义，会发现一个小小的细节，就在传参的地方：`(query, engine)`

实际上，我们希望应该是这样：`({ query, engine })`

## 原因

为什么呢？因为在 React 中，组件的参数是作为一个 JavaScript 对象传递的。在定义函数组件时，我们可以将参数写作 `(props)` 或者其他任何名字，比如 `(foo)`。而在引用组件时，JSX 会将传递的参数名和值打包成一个 JavaScript 对象，作为实参传递给组件。`props` 只是一个约定俗称的名字，你可以通过这个名字来访问传递过来的参数。

另一种写法是 `({ query, engine })`，此时形参变成了一个对象，而 JavaScript 语法允许你通过这种形式直接访问对象中的属性。

但是，如果你采用 `(query, engine)` 这种写法，情况就不同了。`query` 作为第一个形参，实际上接受的是一个 React 打包的对象，长这样：

```json
{
    query: ...,
    engine: ...
}
```

而且！这样子写是不会报错的，因为 JS 里的函数，调用参数无论传够了还是没够，甚至是多了，JavaScript 都不报错。（至少在主流浏览器实现上是这样）

这种逆天写法，换其他语言早就开始叫了，Python 会在运行时爆个 TypeError，编译型语言像 C/C++没等你运行编译器就先开始叫唤了，编译都过不去。

但 JavaScript 允许这种行为发生而没有任何提示！你参数传多了，就会按照实参的顺序依次给到形参（如果调用时没有指定哪个实参要给到哪个形参的话），剩下的就不管；你传少了，还是这样。函数里面要是引用没给到实参的形参咋办？那么你引用的那个形参的值就是 `undefined`，没了。就一个 `undefined`，甚至警告都不会有。

## 总结

因此，在定义 React 组件时，建议采用 `(props)` 或者 `({ prop1, prop2 })` 的形式，以避免潜在的问题。
