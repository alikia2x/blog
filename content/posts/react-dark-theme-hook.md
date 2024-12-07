---
title: 如何在React中检测系统是否开启暗黑模式
date: 2024-08-13T00:35:18+08:00
draft: false
summary: 在现代Web开发中，暗黑模式不仅能够减少眼睛的疲劳，还能在夜间提供更加舒适的阅读体验。那么，如何在React应用中优雅地检测用户是否启用了暗黑模式呢？
---

在现代 Web 开发中，为用户提供一个适应其系统偏好的界面变得越来越重要。特别是暗黑模式（Dark Mode），它不仅能够减少眼睛的疲劳，还能在夜间提供更加舒适的阅读体验。那么，如何在 React 应用中优雅地检测用户是否启用了暗黑模式呢？

## 代码实现

下面是一个自定义 React Hook 的实现，它可以帮助我们检测用户的系统是否启用了暗黑模式：

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

这个 Hook 通过监听 `prefers-color-scheme` 媒体查询的变化来实时更新 `darkMode` 状态。你可以在任何 React 组件中使用这个 Hook 来获取当前的暗黑模式状态，并据此调整你的 UI。

## 直接使用现有库

为了简化开发流程，你可以直接使用我们已经打包好的 npm 库 `@alikia/dark-theme-hook`。这个库包含了上述 Hook 的实现，并且提供了类型定义，方便你在 TypeScript 项目中使用。

安装方法如下：

```bash
使用 npm 
npm install @alikia/dark-theme-hook
# 使用 yarn
yarn add @alikia/dark-theme-hook
# 使用 pnpm
pnpm i @alikia/dark-theme-hook
# 使用 bun
bun add @alikia/dark-theme-hook
```

然后在你的 React 组件中导入并使用它：

```javascript
import useDarkTheme from '@alikia/dark-theme-hook';

function MyComponent() {
    const isDarkMode = useDarkTheme();

    return (
        <div>
            <h1>暗黑模式检测</h1>
            <p>暗黑模式 {isDarkMode ? '已启用' : '未启用'}。</p>
        </div>
    );
}

export default MyComponent;
```

通过使用这个库，你可以轻松地在你的 React 项目中实现暗黑模式的检测和响应，提升用户体验。
