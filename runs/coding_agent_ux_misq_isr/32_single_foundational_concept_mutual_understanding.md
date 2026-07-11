# 单一基础概念版：从 mutual understanding 到 coding-agent working mutual understanding

## 1. 方法纠偏

这版严格按 Chen et al. (2024 MISQ) 的概念开发逻辑写：

> 一个基础概念 + 一个新情境 + 说明原概念为什么不够 + 发展情境化构念和量表。

Chen et al. 的基础概念是：

> usability

他们发展的是：

> voice-interaction usability

我们现在的基础概念只保留一个：

> **mutual understanding**

我们要发展的情境化构念暂定为：

> **coding-agent working mutual understanding**

中文暂译：

> **编码代理工作性相互理解**

这里的重点不是 overload、trust、control、usability 或 workload，而是：

> 人与人协作中，协作能顺利推进很大程度依赖双方形成相互理解；但 coding agent 既像协作者一样行动，又不像人类协作者那样形成、维护和表达理解。因此，我们需要发展一个 coding-agent-specific 的“工作性相互理解”构念。

## 2. database 中的概念存在性

`mutual understanding` 在 `database/ALL_AIS_Basket_11.csv` 中是真实出现过的概念。

相关命中包括：

| 文献 | 年份 | 期刊 | DOI | 对我们的作用 |
| --- | ---: | --- | --- | --- |
| **Mutual understanding in information systems development: Changes within and across projects** | 2019 | MIS Quarterly | `10.25300/MISQ/2019/13980` | 直接以 mutual understanding 为核心概念，研究其如何变化、如何由 sensegiving/sensemaking 形成、如何影响项目成功 |
| **Cocreating understanding and value in distributed work** | 2008 | MIS Quarterly | `10.2307/25148839` | 研究分布式工作中 shared/common/mutual understandings 如何通过 sensegiving、sensedemanding、sensebreaking 被共同创造 |
| **Does mutuality matter? Examining the bilateral nature and effects of CEO-CIO mutual understanding** | 2016 | Journal of Strategic Information Systems | `10.1016/j.jsis.2016.01.001` | 强调 mutual understanding 的双边性、perspective-taking 和 collaboration quality |
| **CEO/CIO mutual understanding, strategic alignment, and the contribution of IS to the organization** | 2010 | Information and Management | `10.1016/j.im.2010.01.002` | 说明 mutual understanding 可通过双方视角测量 |
| **Us and them: A social capital perspective on the relationship between the business and IT departments** | 2011 | European Journal of Information Systems | `10.1057/ejis.2011.4` | 说明不同群体因理解差异造成协作困难，mutual understanding 与感知表现相关 |

这里我们只借鉴 **mutual understanding 作为人际协作基础概念**，不把这些文章中的层级、场景或结果变量照搬过来。

## 3. 基础概念：mutual understanding

在人际协作中，**mutual understanding** 指协作双方对彼此的目标、角色、知识、约束、行动含义和任务情境形成足够一致、可用的理解，使协作能够顺利推进。

它通常包含三个核心意思：

1. 我理解你在做什么、为什么这样做；
2. 你理解我想要什么、担心什么、受到什么约束；
3. 我们对当前任务情境形成了足够一致的工作理解。

Mutual understanding 不是 trust。Trust 是我是否愿意依赖你；mutual understanding 是我们是否理解彼此和共同任务。

Mutual understanding 也不是 control。Control 是我是否能影响过程和结果；mutual understanding 是双方是否能基于相互理解协调行动。

Mutual understanding 也不是 readability。Readability 是信息或行动是否容易看懂；mutual understanding 是看懂之后，双方是否形成了可共同推进任务的理解。

## 4. 为什么 mutual understanding 适用于 coding agent

Coding agent 使用不是单纯工具操作。用户通常会给 agent 一个编程目标，agent 读取项目上下文、规划步骤、修改代码、运行命令、反馈结果，并在需要时请求用户确认。

这种过程非常像协作：

- 用户希望 agent 理解自己的任务意图；
- 用户需要理解 agent 的行动路径；
- 用户希望 agent 知道哪些代码、约束和风险不能碰；
- 用户需要判断 agent 是否仍然和自己在“同一个任务理解”里；
- agent 的下一步行动取决于双方目前形成的工作理解。

因此，mutual understanding 可以作为 coding agent 协作体验的基础概念。

## 5. 为什么原有 mutual understanding 不够

虽然 mutual understanding 适用，但不能直接照搬。真正需要开发新构念的原因在这里。

### 5.1 人与人协作中的理解通常假设双方都有社会认知能力

在人际协作中，mutual understanding 通常依赖 perspective-taking、sensemaking、sensegiving、澄清、追问、解释和纠错。

Coding agent 可以生成解释和行动，但它是否真的“理解”用户意图、代码语义和风险边界并不等同于人类理解。用户面对的是一种功能性的、行为上表现出来的理解，而不是可确认的心理理解。

所以，在 coding agent 情境中，mutual understanding 必须从“双方心理上相互理解”改造成：

> 用户感知到 agent 的行动、反馈和修正是否表现出一种足以共同推进任务的工作性理解。

### 5.2 Coding agent 的理解通过代码行动表现出来

人类协作者可以通过语言、表情、追问和讨论表现理解。

Coding agent 的理解更多通过行动表现：

- 它改了哪些文件；
- 它运行了哪些命令；
- 它是否保留了用户指定的边界；
- 它是否把错误修到正确位置；
- 它是否在测试失败后采取合理下一步；
- 它是否把代码库当前状态纳入后续行动。

因此，coding-agent mutual understanding 不是纯对话理解，而是 **action-manifested understanding**。

### 5.3 代码库状态会持续改变共同理解

在人际协作中，共同任务情境会变化；但 coding agent 的特殊之处是，它自己的行动会直接改变代码库状态。

用户和 agent 之间的“相互理解”必须不断跟随代码状态更新：

- 刚才修改了什么；
- 修改是否改变了原任务边界；
- 测试结果是否推翻了前面的假设；
- 新错误是否意味着要重新理解问题；
- agent 是否仍然理解当前最新状态。

传统 mutual understanding 没有充分处理这种由 agent 自主行动不断改变的代码状态。

### 5.4 用户需要判断 agent 是否仍在“同一个理解”里

Coding agent 常见问题不是完全没理解，而是阶段性偏移：

- 开始理解对了，后面跑偏；
- 局部理解对了，整体任务错了；
- 代码语法改对了，但业务意图错了；
- 修了测试，但破坏了设计约束；
- 能解释自己做了什么，但用户仍无法确认它是否理解真正目标。

因此，coding agent 情境中的关键体验是：

> 用户是否感到自己和 agent 仍然共享一个可工作的任务理解。

这是我们要捕捉的独特东西。

## 6. 新构念定义

**编码代理工作性相互理解**是指：

> 开发者在一次具体编程任务中，与 coding agent 协作时，感知到自己与 agent 对任务目标、代码上下文、约束边界、当前进展和下一步行动形成了足以共同推进任务的工作性理解的程度。

英文定义：

> **Coding-agent working mutual understanding** refers to the extent to which a developer perceives that they and a coding agent have established a workable shared understanding of the task goal, code context, constraint boundaries, current progress, and appropriate next actions during a concrete programming task episode.

这个构念强调的是 **workable shared understanding**，不是声称 agent 有人类式理解。

## 7. 构念高低怎么理解

这是一个连续构念。

高 coding-agent working mutual understanding：

- 用户觉得 agent 明白自己的真实任务意图；
- 用户能理解 agent 为什么采取当前行动；
- agent 的代码修改体现出它理解当前代码上下文；
- agent 能维持用户设定的边界和约束；
- 当用户纠正 agent 时，agent 能把纠正纳入后续行动；
- 用户觉得自己和 agent 对“现在做到哪里、下一步该做什么”有一致理解。

低 coding-agent working mutual understanding：

- 用户觉得 agent 只是在表面执行指令；
- agent 的行动让用户怀疑它误解了任务；
- agent 改动代码但没有体现对上下文的理解；
- agent 忽视用户前面设定的限制；
- 用户纠正后，agent 仍然重复类似偏差；
- 用户经常需要重新解释当前状态和目标。

## 8. 初步维度：只从 mutual understanding 扩展

这些维度只从 mutual understanding 的核心内涵扩展，不引入其他基础概念。

| 维度 | 定义 | 与 mutual understanding 的关系 |
| --- | --- | --- |
| 任务意图理解 | 用户感知 agent 是否理解自己真正想完成什么 | 对目标的相互理解 |
| 代码上下文理解 | 用户感知 agent 是否理解相关代码、依赖和已有设计 | 对任务情境的相互理解 |
| 约束边界理解 | 用户感知 agent 是否理解哪些文件、行为、风险或设计不能破坏 | 对协作边界的相互理解 |
| 过程状态理解 | 用户感知自己和 agent 是否都清楚当前做到哪里、哪些假设已经改变 | 对当前进展的相互理解 |
| 后续行动理解 | 用户感知自己和 agent 是否对下一步该做什么形成一致判断 | 对行动方向的相互理解 |
| 纠偏吸收理解 | 用户感知 agent 是否能理解并吸收用户的纠正、限制和反馈 | 对协作修正的相互理解 |

这些维度后续必须通过 Reddit 评论和访谈检验，不应一开始写死。

## 9. 和 Chen et al. 的对应关系

| Chen et al. (2024) | 我们的研究 |
| --- | --- |
| 基础概念：usability | 基础概念：mutual understanding |
| 新情境：voice interaction with smart products | 新情境：coding-agent collaboration in programming task episodes |
| 为什么原概念适用：voice interaction 仍然涉及用户通过产品实现目标 | 为什么原概念适用：coding agent 使用涉及用户和 agent 共同推进任务，需要相互理解 |
| 为什么原概念不够：voice input/output、人机对话、拟人化改变 usability 结构 | 为什么原概念不够：agentic code action、代码状态变化、非人类理解、纠偏吸收改变 mutual understanding 结构 |
| 新构念：voice-interaction usability | 新构念：coding-agent working mutual understanding |
| 数据作用：用户评论发现维度 | 数据作用：Reddit 评论发现 coding-agent working mutual understanding 的维度 |
| 后续验证：多轮量表开发和竞争模型比较 | 后续验证：多轮量表开发，并与 trust、control、usability 等相邻构念区分 |

## 10. Reddit 编码应如何服务这个单一基础概念

Reddit 编码不应泛泛寻找所有 coding agent UX 主题，而应围绕：

> 用户是否在描述自己和 coding agent 是否形成了足以共同推进任务的工作性相互理解？

优先关注这些表达：

- 用户说 agent 没懂真正意图；
- 用户说 agent 表面执行但方向错了；
- 用户说 agent 忘了或忽视前面约束；
- 用户说 agent 改了代码但不理解代码库；
- 用户说自己看不懂 agent 为什么这样做；
- 用户说需要不断重新解释上下文；
- 用户说纠正 agent 后它能或不能吸收反馈；
- 用户说 agent 和自己像不在同一个任务状态里；
- 用户说 agent 能接住自己的意图并继续推进。

这些都应被解释为 mutual understanding 在 coding agent 情境中的形成、断裂或修复。

## 11. 为什么这个概念重要

这个概念重要，不是因为名字新，而是因为它能解释 coding agent 的实际价值能否实现。

在真实使用中，coding agent 的生产率收益取决于它是否能和用户保持工作性相互理解：

- 如果 agent 理解任务意图和代码上下文，用户可以放心让它推进；
- 如果 agent 不能维持边界理解，用户会频繁干预；
- 如果用户看不懂 agent 的行动理由，相互理解会断裂；
- 如果 agent 不能吸收纠偏，用户会停止委托；
- 如果双方对当前状态和下一步形成一致理解，用户才可能获得真正的协作收益。

因此，它可能影响：

- perceived control；
- trust calibration；
- continued delegation intention；
- takeover frequency；
- process satisfaction；
- productivity realization；
- willingness to use more autonomous coding agents。

这些都是后续模型变量，不是基础概念。

## 12. 当前最稳理论表述

英文：

> We build on mutual understanding as the single foundational concept. Prior IS research shows that mutual understanding among collaborators is crucial for coordinating work, aligning interpretations, and achieving successful outcomes. We argue that this concept is relevant but insufficient for coding-agent collaboration because coding agents are agentic artifacts that appear to collaborate through autonomous code-related actions, yet they do not form, maintain, or express understanding in the same way human collaborators do. We therefore conceptualize coding-agent working mutual understanding as a context-specific UX construct that captures the extent to which developers perceive that they and a coding agent have established a workable shared understanding of the task goal, code context, constraint boundaries, current progress, and appropriate next actions during a concrete programming task episode.

中文：

> 本研究以 mutual understanding 作为唯一基础概念。既有 IS 研究表明，相互理解对于协作者协调工作、对齐解释并获得成功结果至关重要。我们认为，这一概念适用于 coding agent 协作，但不能直接照搬，因为 coding agent 是一种通过自主代码行动表现出协作能力的 agentic artifact，却不像人类协作者那样形成、维持和表达理解。因此，我们提出编码代理工作性相互理解，用来描述开发者在具体编程任务中，感知自己与 coding agent 对任务目标、代码上下文、约束边界、当前进展和合适下一步形成了足以共同推进任务的工作性理解的程度。

