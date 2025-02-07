---
title: USACO 2024 十二月铜组参赛记
date: 2024-12-15T13:25:00+08:00
draft: false
summary: 报名参加了USACO 2024的十二月月赛，并成功满分晋级。特此分享题解与感想~
math: true
tags:
    - OI
    - USACO
---

## Problem 1

原题：

![Problem 1](/img/usaco-24-dec-bronze/Problem1.png)

简单分析一下题目，大概是这样的：

给定T组数据，对于每一组数据 $T_{i}$ ，你需要找出 $[1,T_{i}]$ 内的所有自然数中，链式四舍五入和直接四舍五入结果不同的数的个数。

四舍五入的要求：

四舍五入到大于 $T_{i}$ 的最小的10的整数次幂 (设为 $10^b$)，例如 12372 会被舍入到 $10^5 (100,000)$ 的级别，即 $b=5$.

> 实际上，最终的四舍五入结果要么是 $10^b$，要么是0.

其中，两种四舍五入的方法解释如下：

- 链式四舍五入: 先舍入到 $10^1$，再舍入到 $10^2$，以此类推直到 $10^b$.
- 直接四舍五入：直接舍入到 $10^b$.

我看完题，就决定直接找规律了……

仔细想一想，如果链式四舍五入和直接四舍五入有区别，那么只能是链式四舍五入使得最高位的4变为了5，进而在最后一步舍入时变为 $10^b$ 而不是0. （因为此时在直接四舍五入方法下，由于最高位是4，因而最终舍入结果为0）

那么，什么样的数字满足这个条件呢？

我从简单的三位数、四位数入手（这也是样例中给出的数据处在的范围），

发现在所有的三位数中，445~499 都会使得两种方法舍入结果不同。

而对于四位数，则是 4445~4999.

因此，总结出规律：在 $n$ 位数中，舍入结果不同的数字区间始于（包含端点）：

$$
4 \times \left( \sum_{i=1}^{n-1} 10^i \right) + 5
$$

结束于（包含端点）：


$$
4 \times 10^{n-1} + 9 \times \left( \sum_{i=0}^{n-2} 10^i \right)
$$

也就是说，对于给定的 $T_{i}$，我们只需要统计位数小于 $T_{i}$ 的所有数中，满足条件的数的个数，然后计算和 $T_{i}$ 相同位数的数。将两者加和，即是答案。这个处理流程的时间复杂度为常数 $O(1)$.

总共 $T$ 组数据，总时间复杂度为 $O(T)$.

## 实例

比如，给定数字 4567，我们发现它是四位数，那我们就先统计一位数、两位数和三位数中，满足条件（舍入结果不同）的数的个数，

发现：

1. 一位数中没有这样的数，个数为 $0$.
2. 两位数中45~49满足条件，个数为 
    $$ 
    \begin{aligned}
    N &= 49-45+1 \\\\ &= 49-(45-1) \\\\ &= 49-44 \\\\ &= 5 
    \end{aligned}
    $$
3. 三位数中445~499满足条件，个数为
    $$ 
    \begin{aligned}
    N &= 499-445+1 \\\\ &= 499-(445-1) \\\\ &= 499-444 \\\\ &= 55
    \end{aligned}
    $$

对于四位数，由于 $ 4567 < 4999 $，我们只应计算 $[4445, 4567]$ 这个区间，个数为

$$
\begin{aligned}
N &= 4567-4445+1 \\\\
&= 4567-(4445-1) \\\\
&= 4567-4444 \\\\
&= 123 
\end{aligned}
$$

因此，答案为 $0+5+56+123=184$.

## 照着例子设计程序

从上面的例子中，我们其实可以发现：

一位数、两位数、三位数……$N$位数中，满足条件的数的个数是固定的，

- 一位数有 0 个
- 两位数有 5 个
- 三位数有 55 个
- 四位数有 555 个
- 五位数有 5555 个
- 六位数有 55555 个
- ...

因此，我们只需要预处理出这些数，把它预先打表成一个前缀和的常数数组，那么我们在计算位数小于 $T_{i}$ 的数中满足条件的数的个数时，直接查表即可。

这个常数表就是这样:

```python
# accu stands for accumulate
accu = [0,0,0,5,60,615,6170,61725,617280,6172835,61728390,617283945]
```

索引下标为当前数字的位数，对应的数组元素为累计到`当前位数-1`的数中，满足条件的数的个数。

剩下就没什么难度了。
我推荐用Python写，因为对于类似
$4 \times \left( \sum_{i=0}^{n-2} 10^i \right) + 5$
这种数字（前面n-1位是4，个位数是5）的构建，
Python直接用字符串拼接再转成 int 类型即可，
统计位数什么的也可以直接转成 str 然后统计字符串长度，
相当方便。

参考代码如下:

```python
accu = [0,0,0,5,60,615,6170,61725,617280,6172835,61728390,617283945]

def solve():
    # 输入数字
    inp = input()
    # 统计位数
    digits = len(inp)
    # 获得位数比 inp 小的数字中满足条件的数的个数
    ld = accu[digits]
    # 计算和 inp 相同位数的数中满足条件的数的个数
    curr = max(0, min(int('4' + '9'*(digits - 1)), int(inp)) - int('4' * digits))
    # 输出答案，结果即为两者之和
    print(ld+curr)

T = int(input())
for i in range(T):
    solve()

```
