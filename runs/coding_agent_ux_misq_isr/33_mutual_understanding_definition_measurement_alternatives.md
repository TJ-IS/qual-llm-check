# Mutual understanding：定义、测量与备选概念

## 1. 文献里的 mutual understanding 是什么

在 IS 协作语境中，**mutual understanding** 可以概括为：

> 协作双方或多方对彼此的目标、角色、知识、约束、行动含义和任务情境形成足够一致、可用的理解，使协作能够协调推进。

这个概念在我们的 database 中真实存在。最关键的是：

- Jenkin, Chan, and Sabherwal (2019, MISQ), **Mutual Understanding in Information Systems Development: Changes Within and Across Projects**；
- Rai et al. (2008, MISQ), **Cocreating understanding and value in distributed work**；
- Benlian and Haffke (2016, JSIS), **Does mutuality matter? Examining the bilateral nature and effects of CEO-CIO mutual understanding**；
- Johnson and Lederer (2010, I&M), **CEO/CIO mutual understanding, strategic alignment, and the contribution of IS to the organization**。

这些文献共同说明：mutual understanding 不是“我单方面看懂你”，而是协作关系中形成某种可共同使用的理解结构。它与 sensemaking、sensegiving、perspective-taking、perceptual congruence、shared/common understanding 等概念紧密相关。

## 2. 文献里通常怎么测 mutual understanding

文献里大致有三类测量逻辑。

### 2.1 匹配双方认知的 dyadic measurement

CEO/CIO mutual understanding 这类研究会收集双方数据：

- A 对某事项的看法；
- B 对同一事项的看法；
- A 以为 B 怎么看；
- B 以为 A 怎么看。

然后计算：

- actual agreement：双方真实看法是否一致；
- perceived agreement：一方认为双方是否一致；
- perceptual accuracy：一方是否准确理解另一方；
- dyadic congruence：双方理解是否匹配。

这种方法很严谨，但不能直接照搬到 coding agent，因为 agent 不能像人类被访者一样可靠填写问卷。我们不能声称 agent 有可测的主观心理理解。

### 2.2 过程型 qualitative / longitudinal measurement

MISQ 2019 和 MISQ 2008 更强调过程：

- mutual understanding 会随项目阶段变化；
- sensegiving、sensemaking、sensedemanding、sensebreaking 等活动会形成、修复或破坏理解；
- artifact、planning、control、stakeholder engagement 会影响理解形成。

这种方法对我们很重要，因为 coding agent 使用也是 task episode 过程：用户给目标，agent 行动，用户纠正，agent 吸收或不吸收，代码状态变化，双方理解可能形成或断裂。

### 2.3 单方感知的 perceived understanding

在无法取得双方对称数据时，可以从一方感知测量：

> 我是否感到对方理解了我的目标、约束和当前情境；我是否理解对方的行动；我是否感到双方对任务状态和下一步有一致理解。

这最适合 coding agent。我们不测 agent 的真实心理理解，而测：

> 开发者是否感知到自己和 agent 建立了足以共同推进任务的工作性相互理解。

## 3. 我们的新构念具体定义

建议构念名：

**编码代理工作性相互理解**

英文：

**Coding-Agent Working Mutual Understanding**

定义：

> 开发者在一次具体编程任务中，与 coding agent 协作时，感知到自己与 agent 对任务目标、代码上下文、约束边界、当前进展和下一步行动形成了足以共同推进任务的工作性理解的程度。

这里的关键词是 **working**。

它的意思是：我们不声称 agent 像人一样真的理解；我们只测用户是否感到 agent 的语言、行动、代码修改、测试选择和纠偏反应表现出一种可工作的、足以共同完成任务的理解。

## 4. 和原 mutual understanding 的区别

| 原 mutual understanding | Coding-agent working mutual understanding |
| --- | --- |
| 协作双方通常是人 | 一方是开发者，另一方是 agentic coding artifact |
| 可以假设双方有社会认知和主观理解 | 不能假设 agent 有人类式理解，只能看行动表现 |
| 理解主要通过语言、互动、角色认知、perspective-taking 表现 | 理解通过 prompt response、tool calls、diff、tests、error recovery、constraint following 表现 |
| 任务状态由双方协作推进 | agent 的自主行动会直接改变代码状态 |
| 可以做 dyadic survey | 更适合 task-episode 的 developer-perceived measurement |

## 5. 建议测量方式

### 5.1 测量对象

建议使用 task episode：

> 请回想你最近一次使用 coding agent 完成真实编程任务的经历。这里的 coding agent 是指能够读取或修改项目代码、运行命令或测试、并进行多步行动的 AI 编程代理。请根据这次具体任务回答以下问题。

7 点李克特：

1 = 非常不同意，7 = 非常同意。

### 5.2 构念结构

建议先按二阶形成式构念处理：

- 二阶构念：coding-agent working mutual understanding；
- 一阶维度：任务意图理解、代码上下文理解、约束边界理解、过程状态理解、后续行动理解、纠偏吸收理解；
- 一阶维度可以用反映式题项测量；
- 二阶由一阶维度形成，因为这些理解方面不一定高度相关。

如果 Reddit 和访谈显示这些维度高度共同变化，也可以后续改成反映式二阶或单维构念。

## 6. 初始题项池

### 6.1 任务意图理解

- 这个 agent 似乎理解我真正想完成的任务目标。
- 这个 agent 的行动体现出它理解我的最终意图。
- 我感觉自己和这个 agent 在朝同一个任务目标推进。

### 6.2 代码上下文理解

- 这个 agent 的修改体现出它理解相关代码上下文。
- 这个 agent 能把当前代码库的结构和依赖纳入它的行动。
- 这个 agent 的决策符合当前项目代码的实际状态。

### 6.3 约束边界理解

- 这个 agent 理解我为任务设定的限制和边界。
- 这个 agent 能避免触碰我不希望它修改的部分。
- 这个 agent 的行动体现出它理解哪些风险需要避免。

### 6.4 过程状态理解

- 我感觉自己和这个 agent 都清楚当前任务已经进展到哪里。
- 这个 agent 的后续行动能反映最近发生的代码修改或测试结果。
- 在任务推进中，这个 agent 能保持对当前状态的理解。

### 6.5 后续行动理解

- 我感觉自己和这个 agent 对下一步该做什么有一致理解。
- 这个 agent 提出的下一步行动符合当前任务状态。
- 这个 agent 的行动顺序让我觉得它理解任务应该如何推进。

### 6.6 纠偏吸收理解

- 当我纠正这个 agent 时，它后续行动能体现出它理解了我的纠正。
- 这个 agent 能把我的反馈纳入后续代码修改。
- 我不需要反复解释同一个约束或纠正同一个偏差。

## 7. 区分效度对象

后续应与以下概念区分：

| 概念 | 为什么相近 | 为什么不同 |
| --- | --- | --- |
| trust | 理解可能影响信任 | 信任是是否愿意依赖；mutual understanding 是是否形成可共同推进任务的理解 |
| perceived control | 理解不足会降低掌控感 | 控制是能否影响过程和结果；相互理解是双方是否对任务状态和行动方向形成一致理解 |
| usability | 理解好会让工具更好用 | usability 是使用效率和易用性；working mutual understanding 是协作理解状态 |
| transparency/readability | 过程可见有助于理解 | 可见性是信息属性；mutual understanding 是协作关系状态 |
| cognitive load | 理解不足可能增加负荷 | cognitive load 是认知资源消耗；mutual understanding 是可工作的共同理解是否形成 |
| verification burden | 理解不足会增加验证 | 验证负担是检查输出；mutual understanding 是更上游的协作理解状态 |

## 8. 备选基础概念

### 8.1 Shared understanding

Database 命中较多，且与 mutual understanding 很接近。

优点：

- 名称更适合单方感知；
- 不强迫 agent 具有人类式双边理解；
- 可以自然表达“我和 agent 是否共享任务理解”。

缺点：

- 比 mutual understanding 更容易滑向群体共识或团队共同认知；
- “mutual” 更能体现人与人协作迁移到人-agent协作时的断裂。

判断：

> 很强备选。如果担心 mutual 过度暗示 agent 心理状态，可以改用 **working shared understanding with coding agents**。

### 8.2 Common ground

优点：

- 是沟通协作中非常经典的基础概念；
- 适合研究 prompt、澄清、上下文维持、对话 grounding；
- 很能解释“agent 和我不在同一个上下文里”。

缺点：

- 在我们的 database 中命中少于 mutual/shared understanding；
- 更偏对话和沟通，不一定覆盖代码行动、测试、diff、接管。

判断：

> 如果研究重点是 prompt/clarification/context grounding，common ground 可能比 mutual understanding 更精确。但若要覆盖 coding agent 的代码行动，mutual understanding 更宽。

### 8.3 Transactive memory

优点：

- database 命中很多；
- 能解释“用户知道 agent 知道什么、擅长什么、能做什么”；
- 很适合研究任务分配、能力边界、何时委托。

缺点：

- 核心是“谁知道什么”，不是“我们是否对当前任务形成共同理解”；
- 更适合解释 delegation/appraisal，而不是协作过程中的理解断裂。

判断：

> 适合作为前因或相邻构念，不如 mutual understanding 适合作为主基础概念。

### 8.4 Shared mental model / team cognition

优点：

- 和协作协调、团队表现高度相关；
- 能解释对任务、角色、流程的共同认知结构。

缺点：

- 容易落到 team-level；
- “mental model” 更强烈暗示 agent 有内部心理模型，迁移风险比 mutual understanding 更高。

判断：

> 不建议作为主基础概念。

### 8.5 Collaboration quality / teamwork quality

优点：

- 很直观，和协作体验直接相关；
- 可以覆盖沟通、协调、支持、冲突等多个方面。

缺点：

- 过宽，更像结果评价；
- 不容易提出 coding agent 真正独特的机制。

判断：

> 不适合作为主基础概念，可以作为结果变量。

### 8.6 Collaborative repair

优点：

- database 中有 2026 MISQ chatbot 文章；
- 非常适合人-agent interaction breakdown；
- 与 agent 出错后的共同修复高度相关。

缺点：

- 太窄，只覆盖 breakdown repair；
- 不覆盖正常协作过程中的任务意图、代码上下文、边界和下一步理解。

判断：

> 如果研究主题缩小到“coding agent 出错后如何共同修复”，它很好；但作为总构念基础太窄。

## 9. 当前建议

最推荐：

> **mutual understanding → coding-agent working mutual understanding**

最强备选：

> **shared understanding → coding-agent working shared understanding**

如果你担心 mutual understanding 对 agent 的“相互性”要求太强，可以把主构念名从：

> coding-agent working mutual understanding

改成：

> coding-agent working shared understanding

但基础概念仍可以和 mutual understanding 文献对话，因为 shared/common/mutual understandings 在 ISD 和 distributed work 文献中经常一起出现。

