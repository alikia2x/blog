---
title: Passing Props in React Function Components
date: 2024-06-02T02:58:02+08:00
draft: false
summary: Recently discovered a subtle detail about passing props in React
cover:
    image: '/img/react.jpg'
    relative: true
    hidden: false
---

Recently, while developing with React, I discovered a subtle detail that's easy to overlook, now sharing with you.

When using function components, we usually define some props, but it's important to be aware of potential issues when passing them.

## Example

Let's look at a function component:

```jsx
const Search = (query, engine) => {
    ...
}
export default OneSearch;
```

When using this component, you might do:

```html
<Search query={query} engine={engine} />
```

At first glance, everything seems normal, but if you closely examine the function component's definition, you'll notice a small detail in the parameter passing: `(query, engine)`.

Actually, we should write it like this: `({ query, engine })`.

## Resaon

Why? Because in React, component parameters are passed as a **JavaScript object**. When defining a function component, we can write the parameters as `(props)` or any other name, like `(foo)`. When referencing the component, JSX packages the parameter names and values into a JavaScript object and passes it as an argument to the component. props is just a conventional name, and you can use this name to access the passed parameters.

Another way to write it is `({ query, engine })`, where the parameter becomes an object, and JavaScript syntax allows you to directly access the properties within this object.

However, if you use `(query, engine)`, the situation is different. Query as the first parameter actually receives a React-packaged object that looks like this:

```json
{
    query: ...,
    engine: ...
}
```

And writing it this way **won't throw an error** because in JavaScript functions, regardless of whether you pass enough parameters, too many, or too few, JavaScript won't throw an error (at least in major browser implementations).

In other languages, this would cause an error. Python would throw a `TypeError` at runtime, and compiled languages like C/C++ wouldn't even pass the compile. But JavaScript allows this behavior without any warnings! If you pass too many parameters, it assigns them to the function parameters in order; if you pass too few, it does the same. What if the function references a parameter that wasn't passed? That parameter's value will be `undefined`, and that's it. Just an `undefined`, with no warnings.

## Conclusion

Therefore, when defining React components, it is recommended to use `(props)` or `({ prop1, prop2 })` to avoid potential issues.
