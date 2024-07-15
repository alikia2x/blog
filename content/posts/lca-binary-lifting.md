---
title: 使用倍增法实现LCA（最近公共祖先）查询
date: 2024-07-15T22:24:16+08:00
draft: false
summary: 暑假来临，寒寒参加OI集训，今日学到了如何使用倍增法查找一颗树的LCA（最近公共祖先），故在此分享。
categories: 算法
tags:
    - OI
    - 算法
    - LCA
    - 倍增
---

**题目背景：洛谷模板题[P3379 【模板】最近公共祖先（LCA）](https://www.luogu.com.cn/problem/P3379)**

## 代码实现

> 由于代码中的注释已经很详尽了……就不做过多解释啦(=ﾟωﾟ)ﾉ

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// MAXN 为最大节点数量
const int MAXN = 700000;
// LOG 为 `log2(MAXN)` 的近似值，
// 在算法中作为倍增时所需要的循环次数。
const int LOG = 20;

// 树节点由链表实现
struct TreeNode {
    int val;
    vector< TreeNode * > children;
};

// 树的基本信息
int N, M, S;
vector< int > tree[MAXN];
int parent[MAXN][LOG]; // 倍增法中的父节点
int depth[MAXN];       // 每个节点的深度

// DFS 预处理每个节点的父节点和深度
void dfs(int node, int par) {
    // 将当前节点的直接父节点设置为 par
    parent[node][0] = par;
    // 循环计算每个节点的 2^i 个祖先
    for (int i = 1; i < LOG; ++i) {
        // 确保当前节点的第 2^(i-1) 个祖先存在
        if (parent[node][i - 1] != -1) {
            // 节点 node 的第 2^i 个祖先是：
            // 其第 2^(i-1) 个祖先的第 2^(i-1) 个祖先。
            parent[node][i] = parent[parent[node][i - 1]][i - 1];
        } else {
            // 如果当前节点的第 2^(i-1) 个祖先不存在，
            // 那么 2^i 个祖先也不存在，设置为 -1。
            parent[node][i] = -1;
        }
    }
    // 遍历当前节点的每个子节点，递归调用 dfs 计算子节点的深度和倍增表。
    for (int child : tree[node]) {
        if (child != par) {
            depth[child] = depth[node] + 1;
            dfs(child, node);
        }
    }
}

// 利用倍增法查找两个节点的最近公共祖先
int lca(int u, int v) {
    // 确保 u 是更深的节点
    if (depth[u] < depth[v]) {
        swap(u, v);
    }
    // 计算两个节点的深度差
    int diff = depth[u] - depth[v];
    // 将两个节点拉平到同一深度
    for (int i = 0; i < LOG; ++i) {
        // 使用二进制提升法将 u 提升到和 v 同一深度：
        // diff >> i 检查 diff 的第 i 位是否为1
        if ((diff >> i) & 1) {
            // 如果为1，将 u 提升到其第 2^i 个祖先
            u = parent[u][i];
        }
    }
    // 如果拉到同深度后，节点已经相等，
    // 则说明该深度对应的节点就已经是 LCA
    if (u == v) {
        return u;
    }
    // 否则，则将它们一起提升，直到相等。
    for (int i = LOG - 1; i >= 0; --i) {
        // 如果 u 和 v 的第 2^i 个祖先不同
        // 则同时将 u 和 v 提升到它们的第 2^i 个祖先。
        if (parent[u][i] != parent[v][i]) {
            u = parent[u][i];
            v = parent[v][i];
        }
    }
    // 最终返回 u 和 v 的直接父节点：
    // parent[u][0] 或 parent[v][0]
    // 即为最近公共祖先。
    return parent[u][0];
}

int main() {
    // 数据输入及建树
    cin >> N >> M >> S;

    for (int i = 0; i < N - 1; ++i) {
        int x, y;
        cin >> x >> y;
        // 由于我们使用邻接表来存储树结构
        // 因此是无向图，故需要同时添加
        // x->y 与 y->x 的连接
        tree[x].push_back(y);
        tree[y].push_back(x);
    }

    // 初始化 parent 数组
    fill(parent[0], parent[0] + MAXN * LOG, -1);
    // S 在题目中为根结点，其深度为0。
    depth[S] = 0;
    // 调用 DFS 预处理整个树，从根节点开始。
    dfs(S, -1);

    // 查询及返回
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        cout << lca(a, b) << endl;
    }

    return 0;
}
```
