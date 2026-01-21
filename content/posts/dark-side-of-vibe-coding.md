---
title: “氛围编码”的代价：当 AI 开发者的傲慢烧掉我的账户余额
date: 2026-01-21T22:08:02+08:00
draft: false
summary: KiloCode 的一次“贴心”更新，不仅烧光了我的 OpenRouter 额度，更撕开了硅谷所谓“氛围编程”虚假繁荣的遮羞布。
---

作为一名穷学生，我习惯利用 AI 编程助手来提升效率，同时小心翼翼地平衡开支。然而最近，我的 OpenRouter 账户出现了一系列神秘扣费——大量调用 Codestral 模型的记录赫然在目，而我从未主动选过这个模型。

我的第一反应是：API Key 泄露了？被黑了？在反复重置密钥、翻遍运行日志后，我终于抓到了真凶：我一直信任的 VS Code 开源插件——**KiloCode**。

在最近的一次更新中，KiloCode 悄无声息地将“对话框自动补全”功能设为了默认开启。这意味着，只要我在输入框里敲下任何一个字符，它都会在后台触发 API 请求。没有预警，没有二次确认，只有账单金额在无声无息地跳动。

这并非偶然的代码问题，它是当下席卷技术圈的“氛围编程（Vibe Coding）”乱象的一个缩影。这个词由 AI 专家 Andrej Karpathy 在 2025 年初提出，描绘了一种极具诱惑力的未来：开发者只需通过自然语言描述构思，让 AI 搞定琐碎的底层逻辑，自己在一种轻松的“氛围”中完成创作。

听起来很美好，但在实践中，“氛围编码”正演变成“浮躁开发”的遮羞布——它推崇盲目追求速度与热度，却将用户体验、安全和基本的职业道德弃之脑后。KiloCode 的 PR #4723 正是这种傲慢的典型体现。  
是时候撕开这层糖衣了。

## “背刺”用户的静默更新

让我们看看究竟发生了什么。三周前，KiloCode 发布了 [v4.141.1 版本](https://github.com/Kilo-Org/kilocode/releases/tag/v4.141.1)。在 [PR #4723](https://github.com/Kilo-Org/kilocode/pull/4723/) 中，开发者修改了一行配置代码，将自动补全功能的默认值从 `false` 翻转成了 `true`。

如果你像我一样从未手动调整过该项设置，系统就会默认你已“授权”。从此，每当你试图输入指令，它都会自作聪明地向 Codestral 发送请求，吞噬你的余额，吐出一堆你根本不需要的低质建议。更荒唐的是，这起改动是由机器人提交、人类开发者匆匆过审的。在崇尚“快速迭代”的氛围编码世界里，用户的知情权和财产安全似乎成了微不足道的“阻碍”。

这种乱象在 AI 圈并非孤例。不少 Claude Code Pro 订阅用户也曾[吐槽](https://github.com/anthropics/claude-code/issues/7719)过，插件在没有明确交互提示的情况下消耗了大量 API 额度；而 OpenAI 的预充值余额因过期被清零，更是引发了广泛的[消费者不满](https://community.openai.com/t/paid-credits-expired-wth/1041718)。

## 从噱头到泡沫：“氛围”背后的技术债

“氛围编码”在 2025 年风靡硅谷。Karpathy [曾称其为](https://x.com/karpathy/status/1886192184808149383)“完全沉浸在氛围中”：用自然语言提示，自动接受输出，哪里报错补哪里。KiloCode 借此东风号称拥有百万级用户、处理了 20 万亿 Token，成为了行业领头羊。

然而，过度吹捧掩盖了[致命缺陷](https://qz.com/ai-vibe-coding-software-development)。吴恩达等学者[早就泼过冷水](https://www.klover.ai/andrew-ng-pushes-back-ai-vibe-coding-hard-work-not-hype)：编程是一项严谨的工作，所谓的“氛围”往往是以牺牲质量为代价的。在生产环境中，这种模式会导致难以维护的“屎山”代码激增。据[相关调研](https://www.datapro.news/p/the-vibe-coding-headache)显示，AI 生成的代码中 Bug 率和重复率大幅攀升，且估计大约 [50% 的 AI 生成代码](https://www.veracode.com/blog/genai-code-security-report/)存在安全漏洞。

这种“快餐式”的开发价值观，理所当然地认为用户也想要“AI 无处不在”，于是便有了类似 KiloCode 这种侵入式的默认设置。但正如有创业者[总结](https://www.datapro.news/p/the-vibe-coding-headache#the-startup-graveyard)的那样：氛围编码能做出好看的MV），但它无法处理真正的技术创新。

2025 年底，这类站点的流量暴跌，标志着现实终于撞碎了幻觉。连 Karpathy 本人也[坦言](https://x.com/karpathy/status/1977758204139331904)，他近期的项目基本回归了手写，因为目前的 AI Agent 表现实在“不够稳健”。


## 警惕 AI 狂热下的集体傲慢

如果一家银行敢在不通知用户的情况下默认开启某项收费服务，监管部门早就上门了。但在 AI 领域，这种对用户资产的漠视却被美化成了“拥抱变革”。

Anthropic 首席执行官 Dario Amodei 曾[预测](https://www.freepressjournal.in/tech/were-6-12-months-away-from-ai-doing-everything-software-engineers-do-anthropic-ceos-terrifying-prediction)，AI 到 2025 年中将取代大部分工程工作。然而现实是，正如开发者 [Miguel Grinberg](https://blog.miguelgrinberg.com/post/why-generative-ai-coding-tools-and-agents-do-not-work-for-me) 所言，这些工具往往因幻觉、上下文丢失和低效，反而拖慢了人类的步伐。

所谓的“氛围开发者”们穿着高薪卫衣，把用户当作大型 Beta 测试的耗材。对他们来说，这只是改个默认参数的小事；对我们来说，这是真金白银的损失和对信任的践踏。

## 让编程回归严谨，而非盲从“氛围”

致该领域的所有开发者：请正视你们的责任。任何涉及用户资产的功能，必须强制执行“选择性加入（Opt-in）”。

而对于整个行业：请停止收割智商税。AI 是辅助编程的利器，但不应以牺牲伦理和体验为代价。正如 [Addy Osmani 所警告的](https://addyo.substack.com/p/vibe-coding-is-not-an-excuse-for)，“氛围编码”绝不是产出低质量作品的借口。

我会继续使用 AI 工具，但不会再盲目追逐所谓的“氛围”。如果你也是开发者，请检查你的设置，监控你的账户，别让硅谷的傲慢烧空了你的钱包。
