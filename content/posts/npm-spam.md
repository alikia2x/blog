---
title: 关于npm中滥用行为和批量垃圾包的详细报告
date: 2024-08-14T03:31:38+08:00
draft: false
summary: 本报告详细介绍了npm社区中普遍存在的恶意活动和垃圾包的滥用情况。
---

**重要提示：我们仍在调查此事件。请持续关注最新动态。**

## 更新

> 关于此事件的实时更新。

[(可能是) 根本原因](https://www.web3isgoinggreat.com/single/teaxyz-causes-open-source-software-spam-problems-again)
[另一份报告](https://blog.phylum.io/digital-detritus-unintended-consequences-of-open-source-sustainability-platforms/)

> 然而，这并不能解释上述许多 SEO 行为。此外，我们发现许多包与 tea.xyz 没有任何活动相关，例如 [@diotoborg/esse-accusantium-ratione](https://www.npmjs.com/package/@diotoborg/esse-accusantium-ratione)

---

本报告全面分析了 npm 社区中近期的恶意活动和垃圾包滥用情况。它着重于这些行为的模式及其对 npm 生态系统的影响。

> 本文中“垃圾”一词是英文 "spam" 的等效表述。

## 恶意活动

### 无意义内容

观察到大量包包含无用的代码或功能。这些包不为开发者提供任何价值。这种无意义内容增加了用户查找和使用真正有用包的难度。

### 随机账户

观察到创建了大量无意义的用户名账户。这些账户通常与随机生成的组织相关联，以避免命名空间冲突。这种做法使识别和管理垃圾邮件来源的任务变得复杂。

### 关键词堆砌

垃圾包经常在其 `package.json` 文件中包含大量无关关键词以操纵搜索结果。例如，从 "uuid validate" 的搜索结果在 [Web Archive](https://web.archive.org/web/20240813180911/https://www.npmjs.com/search?q=uuid%20validate) 上的存档来看，发现垃圾包 [@dramaorg/psychic-couscous](https://www.npmjs.com/package/@dramaorg/psychic-couscous) 包含超过 700 个关键词。这种策略干扰了 npm 搜索算法，导致搜索结果用户几乎无法找到相关包。

### 模板化的内容

许多垃圾包的内容遵循有限的几种模板。包括：

- **空包**：如 [@kazaferixm/api-light](https://www.npmjs.com/package/@kazaferixm/api-light) 不包含实际代码。
- **固定模板**：如 [@diotoborg/dolores-praesentium-assumenda](https://www.npmjs.com/package/@diotoborg/dolores-praesentium-assumenda) 使用固定模板生成内容。这种方法在其他垃圾包如 [@micromint1npm/aperiam-perferendis-suscipit](https://www.npmjs.com/package/@micromint1npm/aperiam-perferendis-suscipit) 中也很明显。

### 相互依赖

垃圾包经常在同一垃圾组织内相互创建依赖，以人为提升其搜索排名。例如，来自垃圾组织 [@diotoborg](https://www.npmjs.com/org/diotoborg) 的包平均有 29 个对同一组织其他包的依赖。这种相互依赖导致包如 [@diotoborg/dolores-praesentium-assumenda](https://www.npmjs.com/package/@diotoborg/dolores-praesentium-assumenda) 被多达 580 个其他垃圾包引用，显著影响搜索结果。

### 从流行包复制 README 文件

一些垃圾包复制知名包的 README 文件。例如，[@diotoborg/ratione-error-odio](https://www.npmjs.com/package/@diotoborg/ratione-error-odio) 的 README 与 [pnpm](https://www.npmjs.com/package/pnpm) 相同。

## 示例

一个值得注意的案例是包 [@diotoborg/dolores-praesentium-assumenda](https://www.npmjs.com/package/@diotoborg/dolores-praesentium-assumenda)，其 README 与 [@patrtorg/illum-sapiente-quos](https://www.npmjs.com/package/@patrtorg/illum-sapiente-quos) 不同。[@patrtorg/illum-sapiente-quos](https://www.npmjs.com/package/@patrtorg/illum-sapiente-quos) 的 README 复制自 [fast-xml-parser](https://www.npmjs.com/package/fast-xml-parser)，进一步说明了垃圾包发布者使用的误导性做法。

## 对 npm 社区的影响

### 搜索结果质量

垃圾包操纵搜索排名的行为严重影响了搜索结果的可靠性。这使得开发者无法有效找到他们需要的包。

### 潜在的基础设施压力

大量创建垃圾包及其相互依赖可能对 npm 的基础设施造成不当压力。这可能会降低 npm 性能和可靠性。

## 违反 npm 条款

观察到的活动违反了 npm 开源条款的几个部分：

1. **可接受使用**

    - **部分：** [可接受使用](https://docs.npmjs.com/policies/open-source-terms#acceptable-use)
    - **条款：** "账户和内容必须遵守可接受使用政策，不应破坏 npm 注册表的完整性。"
    - **原因：** 创建和分发包含误导内容的垃圾包违反了维护安全友好环境的准则。

2. **可接受内容**

    - **部分：** [可接受内容](https://docs.npmjs.com/policies/open-source-terms#acceptable-content)
    - **条款：** "npm 管理员保留删除被认为不可接受内容的权利。"
    - **原因：** 使用误导性包名和内容操纵搜索结果符合不可接受内容的条件。

3. **友好无骚扰空间**

    - **部分：** [友好无骚扰空间](https://docs.npmjs.com/policies/conduct#friendly-harassment-free-space)
    - **条款：** "垃圾邮件、钓鱼和其他寻求关注的行为是不被容忍的。"
    - **原因：** 故意创建垃圾包以操纵搜索结果和误导用户是一种垃圾邮件行为。

4. **可接受使用的执行**
    - **部分：** [可接受使用的执行](https://docs.npmjs.com/policies/open-source-terms#enforcement-of-acceptable-use)
    - **条款：** "npm 可能会调查并追究违规行为至最大限度。"
    - **原因：** 这些活动的规模和影响证明了 npm 调查和潜在执行行动的必要性。

## 垃圾包发布者

以下是一些被识别参与垃圾包活动的发布者：

```text
vanthuanbt26
erboladaiorg76
quochoanglm58
diotobtea
luongconghieufomo
micromint1npm
diotoborg
womorg
hishprorg
patrtorg
devtea2026
npmtuanmap
taktikorg
erboladaiorg
zitterorg
```

## 结论

本报告概述的恶意活动对 npm 社区构成了重大威胁。需要立即采取有效措施以维护 npm 注册表的完整性和安全性。
