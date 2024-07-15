---
title: Implementing LCA (Lowest Common Ancestor) Query Using Binary Lifting
date: 2024-07-15T22:24:16+08:00
draft: false
categories: Algorithms
summary: Here's a implemention of finding LCA in C++ with detailed comments to help you understand this algorithm.
math: true
tags:
    - OI
    - Algorithms
    - LCA
    - Binary Lifting
---

## Problem: Lowest Common Ancestor (LCA)

### Problem Description

As stated, given a rooted multi-way tree, find the lowest common ancestor of two specified nodes.

### Input Format

The first line contains three positive integers $!N, M, S!$, representing the number of nodes in the tree, the number of queries, and the root node's index, respectively.

The next $!N-1!$ lines each contain two positive integers $!x!$ and $!y!$, indicating that there is a direct connection between nodes $!x!$ and $!y!$ (it is guaranteed that the data forms a tree).

The next $!M!$ lines each contain two positive integers $!a!$ and $!b!$, representing a query for the lowest common ancestor of nodes $!a!$ and $!b!$.

### Output Format

The output contains $!M!$ lines, each containing a positive integer, which is the result for each query in order.

### Example #1

#### Input #1

```plaintext
5 5 4
3 1
2 4
5 1
1 4
2 4
3 2
3 5
1 2
4 5
```

#### Output #1

```plaintext
4
4
1
4
4
```

### Data Range

For $!30 \\% !$ of the data, $!N \leq 10!$, $!M \leq 10!$.

For $!70 \%!$ of the data, $!N \leq 10000!$, $!M \leq 10000!$.

For $!100 \%!$ of the data, $!1 \leq N, M \leq 500000!$, $!1 \leq x, y, a, b \leq N!$, **not guaranteed** $!a \neq b!$.

## Code Implementation

> Since the comments in the code are already very detailed... I won't explain much further.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// MAXN is the maximum number of nodes
const int MAXN = 700000;
// LOG is an approximation of `log2(MAXN)`,
// used as the number of iterations needed for binary lifting.
const int LOG = 20;

// Tree nodes implemented as linked lists
struct TreeNode {
    int val;
    vector< TreeNode * > children;
};

// Basic information of the tree
int N, M, S;
vector< int > tree[MAXN];
int parent[MAXN][LOG]; // Parent nodes for binary lifting
int depth[MAXN];       // Depth of each node

// DFS preprocesses each node's parent and depth
void dfs(int node, int par) {
    // Set the direct parent of the current node to par
    parent[node][0] = par;
    // Loop to calculate each node's 2^i-th ancestor
    for (int i = 1; i < LOG; ++i) {
        // Ensure the 2^(i-1)-th ancestor of the current node exists
        if (parent[node][i - 1] != -1) {
            // The 2^i-th ancestor of node is:
            // the 2^(i-1)-th ancestor of its 2^(i-1)-th ancestor.
            parent[node][i] = parent[parent[node][i - 1]][i - 1];
        } else {
            // If the 2^(i-1)-th ancestor of the current node doesn't exist,
            // then the 2^i-th ancestor also doesn't exist, set to -1.
            parent[node][i] = -1;
        }
    }
    // Traverse each child of the current node, recursively call dfs to
    // calculate the child's depth and binary lifting table.
    for (int child : tree[node]) {
        if (child != par) {
            depth[child] = depth[node] + 1;
            dfs(child, node);
        }
    }
}

// Use binary lifting to find the lowest common ancestor of two nodes
int lca(int u, int v) {
    // Ensure u is the deeper node
    if (depth[u] < depth[v]) {
        swap(u, v);
    }
    // Calculate the depth difference between the two nodes
    int diff = depth[u] - depth[v];
    // Raise both nodes to the same depth
    for (int i = 0; i < LOG; ++i) {
        // Use binary lifting to raise u to the same depth as v:
        // diff >> i checks if the i-th bit of diff is 1
        if ((diff >> i) & 1) {
            // If it is 1, raise u to its 2^i-th ancestor
            u = parent[u][i];
        }
    }
    // If nodes are equal after raising to the same depth,
    // the node at this depth is already the LCA
    if (u == v) {
        return u;
    }
    // Otherwise, raise both together until they are equal.
    for (int i = LOG - 1; i >= 0; --i) {
        // If the 2^i-th ancestors of u and v are different,
        // raise both u and v to their respective 2^i-th ancestors.
        if (parent[u][i] != parent[v][i]) {
            u = parent[u][i];
            v = parent[v][i];
        }
    }
    // Finally, return the direct parent of u and v:
    // parent[u][0] or parent[v][0]
    // which is the lowest common ancestor.
    return parent[u][0];
}

int main() {
    // Data input and tree construction
    cin >> N >> M >> S;

    for (int i = 0; i < N - 1; ++i) {
        int x, y;
        cin >> x >> y;
        // Since we use an adjacency list to store the tree structure
        // it is an undirected graph, so we need to add both
        // x->y and y->x connections
        tree[x].push_back(y);
        tree[y].push_back(x);
    }

    // Initialize the parent array
    fill(parent[0], parent[0] + MAXN * LOG, -1);
    // S is the root node in the problem, its depth is 0.
    depth[S] = 0;
    // Call DFS to preprocess the entire tree, starting from the root node.
    dfs(S, -1);

    // Query and return results
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        cout << lca(a, b) << endl;
    }

    return 0;
}
```
