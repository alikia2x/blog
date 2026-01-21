---
title: The Dark Side of Vibe Coding
date: 2026-01-21T22:08:02+08:00
draft: false
summary: How KiloCode's "Helpful" update drained my credits and exposed Silicon Valley's hype machine
---

As a student scraping by on a tight budget, I rely on tools like AI coding agents to boost my productivity without breaking the bank. So when I noticed mysterious charges on my OpenRouter account—calls to the Codestral model I *never* intentionally used—I panicked. Was my API key leaked? Had I been hacked? After rotating keys and digging through logs, the culprit emerged: **KiloCode**, the popular open-source coding extension I'd been using in VS Code.

A recent update had quietly flipped their "chat autocomplete" feature to "on" by default, triggering automatic API requests every time I typed in the prompt box. No warning, no opt-in prompt, just silent deductions from my precious credits.

This wasn't just a glitch; it was a symptom of a larger problem plaguing the tech world: **"vibe coding."** Coined by AI luminary Andrej Karpathy in early 2025, vibe coding promised a revolutionary way to build software—letting AI handle the grunt work while developers "vibe" through high-level ideas, accepting suggestions with minimal scrutiny. It sounded liberating, but in practice, it's become a euphemism for sloppy, hype-driven development that prioritizes speed and buzz over user experience, security, and basic ethics. KiloCode's PR #4723 exemplifies this arrogance, and it's time we call it out.


## The Sneaky Update: A One-Line Change with Real Consequences

Let's break down what happened. Three weeks ago, KiloCode [released version 4.141.1](https://github.com/Kilo-Org/kilocode/releases/tag/v4.141.1), including a [pull request](https://github.com/Kilo-Org/kilocode/pull/4723/) that changed a single line in a file. Using a nullish coalescing operator, they swapped the default value for chat autocomplete from `false` to `true`. If you hadn't manually configured it before (like me), boom—enabled. It will start firing off requests to models like Codestral via your configured provider, racking up costs without a peep.

I first spotted the issue in my OpenRouter dashboard: odd Codestral calls traced back to KiloCode. I mistook the autocompletions for interference from another extension, Windsurf, assuming it was treating the input box as code. Wrong. This "feature" was burning my credits on suggestions I didn't want or need—annoying interruptions that often felt irrelevant or half-baked. And get this: the commit was submitted by a bot, reviewed by a human who apparently didn't flag the UX implications. In the world of vibe coding, where everything's about rapid iteration and "moving fast," user consent is an afterthought.

This isn't isolated. Developers across the industry report similar frustrations with AI tools quietly consuming resources. For instance, Claude Code users with Pro subscriptions have [complained](https://github.com/anthropics/claude-code/issues/7719) about unexpected API credit deductions, with no clear UX warnings or preferences to default to subscription limits. OpenAI's prepaid credits have expired without usage, [leaving users feeling cheated](https://community.openai.com/t/paid-credits-expired-wth/1041718).


## Vibe Coding: From Buzzword to Bubble Burst

Vibe coding exploded in 2025 as Silicon Valley's latest obsession. [Karpathy described](https://x.com/karpathy/status/1886192184808149383) it as "fully give in to the vibes": prompt AI in natural language, auto-accept outputs, copy-paste errors until it works, and forget the code exists. Startups touted it as democratizing software, with tools like KiloCode leading the charge—boasting 1M+ users, 20 trillion tokens processed, and integrations with models from Anthropic to xAI. But the hype masked [deep flaws](https://qz.com/ai-vibe-coding-software-development).

Critics, including [Andrew Ng](https://www.klover.ai/andrew-ng-pushes-back-ai-vibe-coding-hard-work-not-hype), called it out early: vibe coding isn't effortless genius; it's hard work misrepresented as casual vibes, leading to overhyped expectations and subpar results. In production, technical debt piles up from unmaintainable code, with [reports](https://www.datapro.news/p/the-vibe-coding-headache) of increased bugs, code cloning, and reduced reuse. There're also [studies](https://www.veracode.com/blog/genai-code-security-report/) show AI models introduced risky security vulnerability in about 50% of the code.

Vibe coding's "build fast" ethos encourages defaults like chat autocomplete, assuming users want AI everywhere. [But just as one founder says](https://www.datapro.news/p/the-vibe-coding-headache#the-startup-graveyard), it's not suitable beyond MVPs—it can't innovate or handle unique problems without human oversight.

The fallout? A "rise and fall" narrative, with traffic to vibe coding sites slumping by late 2025 as reality set in. Even Karpathy [admitted](https://x.com/karpathy/status/1977758204139331904) his one of his latest project was "basically entirely hand-written" because AI agents "just didn't work well enough." Silicon Valley's vibe coders—those high-paid engineers in hoodies—treat users like beta testers, pushing features that "feel right" without considering real-world impacts. For them, it's just a "default value" tweak; for us, it's lost money and trust.


## The Broader Phenomenon: Arrogance in the AI Hype Cycle

This isn't just about KiloCode; it's systemic. Traditional services would face backlash for silent deductions—think banks or utilities. But in AI's Wild West, it's normalized. Execs like Anthropic's Dario Amodei [predicted](https://www.freepressjournal.in/tech/were-6-12-months-away-from-ai-doing-everything-software-engineers-do-anthropic-ceos-terrifying-prediction) AI would handle "most" engineering by mid-2025, shifting humans to editors. Yet, as [Miguel Grinberg](https://blog.miguelgrinberg.com/post/why-generative-ai-coding-tools-and-agents-do-not-work-for-me) argues, these tools don't actually make devs faster—they introduce hallucinations, context losses, and inefficiencies.

Security is another casualty. AI code often mishandles passwords and introduces flaws that traditional coding avoids. And for open-source projects like KiloCode, the "community-driven" label doesn't excuse poor decisions. Their GitHub is active, but where's the user feedback loop on cost-incurring features?

Vibe coding's arrogance disregards users' assets, treating us as data points in their growth metrics. If this were a bank auto-enabling a fee-based service, regulators would pounce. Why the double standard for tech?


## A Call for Change: Prioritize Users Over Vibes

KiloCode devs, if you're reading: **Own this.** Make opt-in mandatory for features that affect user's credits, and add prominent notifications. Broader industry: **Ditch the hype.** AI can assist coding, but not at the expense of ethics or UX. As [Addy Osmani warns](https://addyo.substack.com/p/vibe-coding-is-not-an-excuse-for), vibe coding isn't an excuse for low-quality work—it's a reminder to blend AI with rigor.

I'm sticking with AI tools, but thoughtfully—no more blind vibes. If we demand better, maybe Silicon Valley will listen. Until then, check your settings, monitor your dashboards, and don't let the hype burn your budget.
