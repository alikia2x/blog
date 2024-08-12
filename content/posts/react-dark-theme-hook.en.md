---
title: How to Elegantly Detect if the User's System Has Dark Mode Enabled
date: 2024-08-13T00:35:18+08:00
draft: false
summary: In modern web development, dark mode not only reduces eye strain but also provides a more comfortable reading experience at night. So, how can we elegantly detect if the user has enabled dark mode in a React application?
---

In modern web development, providing an interface that adapts to the user's system preferences has become increasingly important. Especially with dark mode, it not only reduces eye strain but also offers a more comfortable reading experience at night. So, how can we elegantly detect if the user has enabled dark mode in a React application?

## Code Implementation

Below is a custom React Hook implementation that can help us detect if the user's system has enabled dark mode:

```javascript
import { useState, useEffect } from 'react';

export default function useDarkTheme() {
    const [darkMode, setDarkMode] = useState(false);

    useEffect(() => {
        const colorSchemeQueryList = window.matchMedia('(prefers-color-scheme: dark)');
        setDarkMode(colorSchemeQueryList.matches);

        const handleChange = () => {
            setDarkMode(colorSchemeQueryList.matches);
        };

        colorSchemeQueryList.addEventListener('change', handleChange);

        return () => {
            colorSchemeQueryList.removeEventListener('change', handleChange);
        };
    }, []);

    return darkMode;
}
```

This Hook listens for changes in the `prefers-color-scheme` media query to update the `darkMode` state in real-time. You can use this Hook in any React component to get the current dark mode status and adjust your UI accordingly.

## Using an Existing Library

To simplify the development process, you can directly use our packaged npm library `@alikia/dark-theme-hook`. This library includes the implementation of the above Hook and provides type definitions, making it convenient for use in TypeScript projects.

Installation methods are as follows:

```bash
# Using npm
npm install @alikia/dark-theme-hook
# Using yarn
yarn add @alikia/dark-theme-hook
# Using pnpm
pnpm i @alikia/dark-theme-hook
# Using bun
bun add @alikia/dark-theme-hook
```

Then, import and use it in your React component:

```javascript
import useDarkTheme from '@alikia/dark-theme-hook';

function MyComponent() {
    const isDarkMode = useDarkTheme();

    return (
        <div>
            <h1>Dark Mode Detection</h1>
            <p>Dark mode is {isDarkMode ? 'enabled' : 'disabled'}.</p>
        </div>
    );
}

export default MyComponent;
```

By using this library, you can easily implement dark mode detection and response in your React project, enhancing the user experience.
