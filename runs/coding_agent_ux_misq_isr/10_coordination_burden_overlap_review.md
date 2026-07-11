# 代理委托协调负担：已有概念重合风险检索分析

## 结论先行

如果概念叫“协调负担”并且定义得很宽，它与已有概念高度重合，不适合作为一个强新概念。

它至少会被以下概念部分吸收：

- coordination cost / coordination burden；
- technostress / work overload；
- interruption overload；
- warning or approval fatigue；
- interaction effort；
- cognitive load；
- verification burden；
- supervisory control / automation monitoring；
- IS delegation 的 coordination mechanism。

但如果把它严格限定为 **coding-agent delegation 中，用户为了协调 agent 的自主行动、代码变更、审批交还、验证和接管所承受的任务级负担**，它仍有研究价值。更合适的定位不是“完全新概念”，而是：

**从 IS delegation 的 coordination mechanism 发展出的 coding-agent-specific 二阶构念或情境化构念。**

## 与已有概念的重合风险

| 已有概念 | 代表文献/来源 | 已覆盖内容 | 与“代理委托协调负担”的重合 | 是否完全覆盖 |
| --- | --- | --- | --- | --- |
| IS delegation coordination | Baird & Maruping 2021 MISQ | 委托中的 appraisal、distribution、coordination | 直接覆盖“委托后需要协调”这一理论母体 | 不完全。它是机制框架，不是用户感知负担 |
| Distributed delegation | Stelmaszak et al. 2025 MISQ | 多算法、多人的 collective hybrid appraisal/distribution/coordination | 覆盖多主体委托和混合协调 | 不完全。研究对象是 Uber 平台层面的委托机制，不是个体 coding UX |
| Productive delegation / metaknowledge | Fügener et al. 2022 ISR | 人类是否能正确判断自己和 AI 的能力并委托 | 覆盖委托质量和能力判断 | 不完全。关注“委托给谁”，较少关注委托后的持续协调负担 |
| Delegation willingness dynamics | Liu et al. 2025 MISQ | 人对 AI 的动态委托意愿和绩效反馈循环 | 覆盖委托意愿变化 | 不完全。不是负担构念 |
| Coordination cost | 组织经济学、IS 外包/协作文献 | 协调活动造成的成本 | 词面高度重合 | 不完全。多为组织/交易/流程层面，不是个体 UX |
| Technostress / work overload | Ayyagari et al. 2011 MISQ; Pflügner et al. 2024 MISQ | 技术特征造成工作过载、角色模糊、压力 | 覆盖“额外负担/压力” | 不完全。太宽，不解释 agent 委托结构 |
| Interruption overload | Chen & Karahanna 2018 MISQ | 技术中断造成过载、心理转换 | 覆盖审批/通知打断 | 不完全。只覆盖中断后果，不覆盖变更、验证、接管协调 |
| Warning fatigue / habituation | Vance et al. 2025 MISQ | 高频普通通知导致关键警告被忽视 | 覆盖 approval fatigue | 不完全。只覆盖通知习惯化，不覆盖整体协作协调 |
| Verification burden | AI coding/HCI 新近文献 | 检查 AI 产出的负担 | 覆盖 review、测试和代码验证 | 不完全。只覆盖产出验证，不覆盖任务目标、行动轨迹、审批交还 |
| Interaction effort / cognitive load | HCI/AI collaboration 文献 | 使用系统需要的交互努力和认知资源 | 覆盖“费劲” | 不完全。太一般，不含 delegation coordination 的结构 |

## 核心风险

### 风险 1：它可能只是 technostress 的一个压力源

Technostress 文献已经有 work overload、role ambiguity、complexity、intrusiveness 等维度。Coding agent 的协调负担可以被解释为一种新的 technostressor：

agent 增加了用户需要处理的信息、审批、验证和角色不清。

如果我们只是说“用 coding agent 让我更累、更复杂、更有压力”，那就没有新概念贡献。

### 风险 2：它可能只是 interruption overload + warning fatigue

用户提到的 approval fatigue 很容易被中断和警告疲劳文献覆盖。MISQ 的 warning fog 文章已经说明，频繁普通通知会导致用户对关键警告习惯化忽视。

如果我们的概念只研究 approval 太多导致机械点击，那么应该直接用 approval fatigue / warning habituation，不必开发新构念。

### 风险 3：它可能只是 verification burden

coding agent 的主要痛点之一是验证 AI 生成代码。若概念写成“我需要检查 agent 的代码，所以负担大”，那就是 verification burden。

新构念必须覆盖验证之外的协调活动，例如目标对齐、行动追踪、审批分流、接管时机和失败修复。

### 风险 4：它可能只是 IS delegation 的 coordination mechanism

Baird & Maruping 2021 已经把 coordination 放进 IS delegation 框架。如果我们只是说“coding agent 委托后需要协调”，那只是应用旧框架。

要有贡献，必须说明 coding agent 中的 coordination 形成了可测的个体 UX 负担，并且这种负担由 agent 的自主行动、代码库副作用、审批交还和验证责任共同构成。

## 仍然可能成立的窄定义

如果要保留这个方向，建议不要叫宽泛的“协调负担”，而叫：

**编码代理委托协调负担**

英文：

**Perceived Coordination Burden in Coding-Agent Delegation**

定义：

编码代理委托协调负担是指：开发者在将软件开发任务部分委托给 coding agent 后，为了持续对齐任务目标、理解 agent 自主行动及其代码变更、处理审批与注意力交还、验证关键产出并决定是否接管或修复，而感到需要付出的额外认知与交互成本。

这个定义必须包含五个要素：

1. 委托后发生，而不是一般使用压力；
2. agent 有自主行动，而不是普通工具；
3. 行动会改变代码库，而不是只给建议；
4. 用户需要处理审批/注意力交还，而不是只看结果；
5. 用户需要在协调中做接管、修复、继续委托等决策。

## 可能维度

### 1. 目标对齐负担

用户需要反复确认 agent 是否仍在朝原任务目标推进。

### 2. 行动追踪负担

用户需要理解 agent 做了哪些步骤，以及这些步骤如何影响代码库。

### 3. 审批分流负担

用户需要区分哪些 approval 是例行的，哪些是关键风险节点。

### 4. 验证整合负担

用户需要把 diff、测试、日志和解释整合起来判断是否接受产出。

### 5. 接管/修复决策负担

用户需要判断何时继续让 agent 做，何时暂停、接管、回滚或重新指示。

## 与关键文献的关系

### Baird & Maruping 2021 MISQ

该文提出 agentic IS artifacts 使 IS use 需要转向 IS delegation，并提出 delegation 的 appraisal、distribution、coordination 机制。我们的构念不是替代它，而是把 coordination 机制转化为 coding-agent 场景下的个体感知负担。

### Fügener et al. 2022 ISR

该文通过实验研究 human-AI productive delegation，发现人类委托 AI 的问题不是算法厌恶，而是缺乏 metaknowledge，无法正确评估自己和 AI 的能力。它支持“委托不是单纯 trust”的前提，但它的重心是委托决策质量，不是委托后的持续协调负担。

### Liu et al. 2025 MISQ

该文研究 human-AI delegation willingness 的动态反馈循环。它说明 delegation 可以作为动态行为状态研究，而不一定是静态量表。我们的构念可以作为影响委托意愿动态变化的中介或前因。

### Stelmaszak et al. 2025 MISQ

该文提出 distributed delegation，强调 collective hybrid appraisal、distribution、coordination。它说明委托协调在复杂算法系统中已经是重要理论对象，但研究层次偏平台/多主体机制。我们的方向若要成立，应转到个体开发者面对 coding agent 的协调体验。

### Ayyagari et al. 2011 MISQ / Pflügner et al. 2024 MISQ

Technostress 文献构成最大重合风险。我们需要避免把构念写成一般工作过载或技术复杂性，而应明确 coding-agent delegation 的结构性负担。

### Chen & Karahanna 2018 MISQ / Vance et al. 2025 MISQ

中断和警告疲劳文献解释 approval fatigue，但只能覆盖协调负担中的审批分流负担这一部分。

### AI coding agent 新近实践文献

新近 AI coding agent 讨论中已经出现 approval fatigue、verification burden、human coordination burden 等术语。例如对 Claude Code 的 source-level 分析指出 approval fatigue 会使交互式确认作为安全机制不可靠；这支持现实重要性，但也提示“负担”相关概念正在快速出现，必须谨慎命名。

## 最终判断

“代理委托协调负担”不是一个完全干净的新概念。

它的优点：

- 有坚实的 IS delegation 理论来源；
- 能解释 CLI 看不清改动、approval fatigue、验证成本、接管困难等现实痛点；
- 比掌控感更靠前，掌控感可作为后果；
- 比单一 verification burden 或 interruption overload 更综合。

它的缺点：

- 与 technostress、coordination cost、interruption overload、verification burden 重合较高；
- 如果定义不够窄，会显得只是旧概念拼接；
- 更像情境化二阶构念，而不是完全独立的新理论概念。

因此，若目标是“强概念开发”，它不是最理想候选。若目标是“基于 IS delegation 开发 coding-agent-specific UX 构念并量表化”，它是可行但要谨慎定位的候选。

我建议的定位是：

**不是开发全新理论原子概念，而是开发一个 coding-agent-specific 的二阶构念：Perceived Coordination Burden in Coding-Agent Delegation。**

它的理论贡献应该写成：

> 将 IS delegation 的 coordination mechanism 个体化、体验化，并说明在 coding agent 场景中，协调负担由自主行动、代码库副作用、审批交还、验证整合和接管修复共同构成。

