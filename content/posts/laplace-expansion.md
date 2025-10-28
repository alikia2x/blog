---
title: 行列式的拉普拉斯展开推导-学习笔记
date: 2025-10-28T20:08:30+08:00
draft: false
math: true
summary: 你可能用拉普拉斯展开的方式计算过矩阵的行列式。可是，为什么要这样算呢？
---

## 置换
有限集 $ S $ 上的置换 $ \sigma $ 是一个从 $ S $ 到 $ S $ 的 **双射**。

### 置换的表示方法

一个置换可以直观地用两行来表示，其中第一行是原像，第二行是对应的像，例如:
 
$\begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 3 & 1 \end{pmatrix} \Rightarrow \sigma(1)=2$，$\sigma(3)=1$，$\sigma(2)=3$

如果它是一个“轮换”，那么也可以用单行来表示。例如 $(1\ 2\ 3)$ 表示 $ 1 \to 2 $，$ 2 \to 3 $，$ 3 \to 1 $，也即 $\sigma(1)=2$，$\sigma(2)=3$，$\sigma(3)=1$。


### 置换的乘法

设 $ S = \{1,2,3\} $，例如 $ \sigma = \begin{pmatrix} 1 & 2 & 3  \\\\ 2 & 3 & 1 \end{pmatrix} $，$ \tau = \begin{pmatrix} 1 & 2 & 3  \\\\ 3 & 1 & 2 \end{pmatrix} $，则 $ \sigma \circ \tau = \begin{pmatrix} 1 & 2 & 3  \\\\ 1 & 2 & 3 \end{pmatrix} $

> 推导：$ 1 \xrightarrow{\tau} 3 \xrightarrow{\sigma} 1 $；$ 3 \xrightarrow{\tau} 2 \xrightarrow{\sigma} 3 $；$ 2 \xrightarrow{\tau} 1 \xrightarrow{\sigma} 2 $）。

置换乘法需 **从右向左应用** 置换，置换 $ \sigma $ 和 $ \tau $ 的乘积为 $ \sigma \circ \tau $。

### 置换的奇偶性与符号
- **对换**：仅交换集合中两个元素，其余元素不变的置换，记为 $ (i\ j) $（交换 $ i $ 和 $ j $）。
  例如，对于 $ S = \{1,2,3\} $，$ (1\ 2) = \begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 1 & 3 \end{pmatrix} $。
- **置换的分解**：任何置换都可以分解成有限个对换的乘积。
- **奇偶性**：尽管置换的分解方式不唯一，但所有分解中对换的个数的奇偶性唯一，这个奇偶性称作置换的 **奇偶性**。
- **符号**：置换的符号 $ \text{sgn}(\sigma) $ 是一个函数：
  $$
  \text{sgn}(\sigma) = \begin{cases}
  +1 & \text{如果}\ \sigma\text{为偶置换} \\\\
  -1 & \text{如果}\ \sigma\text{为奇置换}
  \end{cases}
  $$
  恒等置换为 **偶置换**，对换为 **奇置换**。


## 群
对于集合 $ S \neq \emptyset $ 和 $ S $ 上的运算 $ \cdot $，构成的代数结构 $ (S, \cdot) $ 满足 4 条 **群公理**，则称 $ (S, \cdot) $ 是一个群：

1. **封闭性**：$ \forall a,b \in S $，$ a \cdot b \in S $
2. **结合律**：$ \forall a,b,c \in S $，$ (a \cdot b) \cdot c = a \cdot (b \cdot c) $
3. **单位元**：$ \exists e \in S $，$ \forall a \in S $，$ e \cdot a = a \cdot e = a $
4. **逆元**：$ \forall a \in S $，$ \exists b \in S $，$ a \cdot b = b \cdot a = e $，称 $ b $ 为 $ a $ 的逆元，记为 $ a^{-1} $

若 $ (S, \cdot) $ 为群，$ T $ 为 $ S $ 的非空子集，且 $ (T, \cdot) $ 也是群，则 $ (T, \cdot) $ 是 $ (S, \cdot) $ 的 **子群**。

集合 $ S $ 上所有置换关于置换的乘法，构成一个群；该群的任意一个子群即为一个 **置换群**。


## 逆序数
例如，一个置换 $ \sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 1 & 2 & 4 \end{pmatrix} $，计算其逆序数：
看其像序列 $ (3, 5, 2, 1, 4) $，对于其中每个元素：
- $ 3 $：其右侧且比 $ 3 $ 小的数有 $ 2 $ 个（$ 1, 2 $），贡献 $ 2 $；
- $ 5 $：其右侧且比 $ 5 $ 小的数有 $ 3 $ 个（$ 1, 2, 4 $），贡献 $ 3 $；
- $ 2 $：其右侧且比 $ 2 $ 小的数有 $ 1 $ 个（$ 1 $），贡献 $ 1 $；
- $ 1 $：其右侧且比 $ 1 $ 小的数有 $ 0 $ 个，贡献 $ 0 $；
- $ 4 $：其右侧且比 $ 4 $ 小的数有 $ 0 $ 个，贡献 $ 0 $；
该置换的逆序数为 $ 2 + 3 + 1 + 0 + 0 = 6 $。

**逆序数的奇偶性即为置换的奇偶性**。

## 莱布尼茨公式
行列式可以用莱布尼茨公式通过 **对称群** 来定义：
$$
\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \cdot \prod_{k = 1}^n a_{k, \sigma(k)}
$$
其中，$ S_n $ 是 $ n $ 次 **对称群**，这个群包含集合 $ S = \{x \mid 1 \leq x \leq n, x \in \mathbb{N}^*\} $ 上所有可能的置换 $ \sigma $。

以 $ n=3 $ 为例，$ S_3 $ 包含如下 6 个置换：
- 对换：$ (1,2) $、$ (1,3) $、$ (2,3) $
- 3-轮换：$ (1\ 2\ 3) $、$ (1\ 3\ 2) $
- 恒等置换


根据莱布尼茨公式，我们可以得到 **拉普拉斯展开**。

例如，将其按第 $ r $ 行展开：
$$
\det(A) = \sum_{j = 1}^n a_{rj} C_{rj}, \quad C_{rj} = (-1)^{r+j} \det(M_{rj})
$$
其中 $ M_{rj} $ 是删去 $ r $ 行 $ j $ 列得到的 $ n-1 $ 阶方阵。

**证明过程**：
- 先将置换按 $ \sigma(r)=j $ 分组（选择 $ r $ 行 $ j $ 列），则
$$
\det(A) = \sum_{j = 1}^n \sum_{\substack{\sigma \in S_n \\\\ \sigma(r)= j}} \text{sgn}(\sigma) \prod_{k = 1}^n a_{k, \sigma(k)}
$$
- 对于固定的 $ j $，在内外层每一项都有 $ a_{rj} $，将其提出：
$$
\det(A) = \sum_{j = 1}^n a_{rj} \sum_{\substack{\sigma \in S_n \\\\ \sigma(r)= j}} \text{sgn}(\sigma) \prod_{\substack{k = 1 \\\\ k \neq r}}^n a_{k, \sigma(k)}
$$
- 令集合 $ T = \{1,2,\dots,r-1,r+1,\dots,n\} $（记作 $ T $），置换 $ \sigma $ 在 $ T $ 上的限制为 $ \tau $，即 $ \sigma(1),\sigma(2),\dots,\sigma(r-1),\sigma(r+1),\dots,\sigma(n) $ 可写作 $ \tau $，则上述内层和可写成：
$$
\sum_{\tau} \text{sgn}(\sigma) \prod_{\substack{k = 1 \\\\ k \neq r}}^n a_{k, \tau(k)}
$$
- 又因为 $ \text{sgn}(\sigma) = (-1)^{r+j} \text{sgn}(\tau) $，故上式可写成：
$$
(-1)^{r+j} \sum_{\tau} \text{sgn}(\tau) \prod_{\substack{k = 1 \\\\ k \neq r}}^n a_{k, \tau(k)}
$$
而 $ \sum_{\tau} \text{sgn}(\tau) \prod_{\substack{k=1 \\ k \neq r}}^n a_{k, \tau(k)} $ 即为 $ \det(M_{rj}) $ 的定义式，因此拉普拉斯展开得证。

> 按理论来说，我们应当将 $ \tau $ 上的元素重新排列，得到一个定义在集合 $ S = \{1,2,\dots,n\} $ 的置换。但重新排列并不改变逆序数，因而不会改变“符号”（数字的相对大小不变）。

最后，我们便可以得到 $\det(A) = \sum_{j=1}^n a_{ij} (-1)^{i+j} M_{ij}$，这便是拉普拉斯展开。

#### 关于 $\text{sgn}(\sigma) = \text{sgn}(\tau) \cdot (-1)^{i+j}$ 的证明：
考虑定义在集合 $S = \{1, 2, \dots, n\}$ 上的置换：

$$
\sigma = \begin{pmatrix} 1 & \dots & i & \dots & n \\\\ \sigma(1) & \dots & \sigma(i)=j & \dots & \sigma(n) \end{pmatrix}
$$

去除 $\begin{pmatrix}i \\\\ j\end{pmatrix}$ 这一列，得到的就是 $\tau$。

看置换的第 2 行，我们设 $j$ 左侧比 $j$ 大的数有 $x$ 个，而 $j$ 左侧比 $j$ 小的数有 $y$ 个。根据逆序数的计算方法：
- 删去 $j$ 这一列后，$j$ 左侧的数在统计逆序数时，因 $j$ 的移除，对逆序数的贡献会少 $x$；
- $j$ 本身因被移除，对逆序数的贡献会减少“在 $j$ 右侧比 $j$ 小的数的个数”，也就是 $y$。
因此，去除 $j$ 对逆序数的影响为 $-(x + y)$，对符号的影响为 $(-1)^{-(x + y)}$。

又因为在 $j$ 左侧比 $j$ 小的数的个数，是在 $j$ 左侧的数的总数 $i - 1$ 减去在 $j$ 左侧比 $j$ 大的数的个数 $x$，即 $i - 1 - x$；比 $j$ 小的数的个数，是在 $j$ 左侧和右侧比 $j$ 小的数的个数之和，即 $i - 1 - x + y$。同时，因第 2 行的所有数都在 $S$ 中，不难得出比 $j$ 小的数有 $j - 1$ 个，即 $j - 1 = i - 1 - x + y \Rightarrow i - j = x - y$。

小学二年级的时候，我们学过：$\forall a, b \in \mathbb{Z}$，$a + b \equiv a - b \pmod{2}$，即 $b \equiv -b \pmod{2}$。因此，$i + j$、$i - j$、$x + y$、$x - y$、$-(x + y)$ 的奇偶性均一致，故 $(-1)^{-(x + y)} = (-1)^{i + j}$。

所以我们可得 $\text{sgn}(\sigma) = (-1)^{-(x + y)} \text{sgn}(\tau) = (-1)^{i + j} \text{sgn}(\tau)$。