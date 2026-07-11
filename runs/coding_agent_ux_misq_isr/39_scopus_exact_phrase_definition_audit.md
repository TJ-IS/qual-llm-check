# Scopus 精确短语检索与候选概念定义审计

## 1. 为什么需要这次审计

38 号文档把 `workspace awareness` 重新推回首选候选，但这个判断过快。它主要基于我们对 coding agent 使用痛点的直觉贴合，而没有充分检查：

1. `workspace awareness` 在关键定义文献中到底是什么意思；
2. Scopus 最新文献中这个词实际被怎样使用；
3. 它和其他候选概念相比，是否真的更适合作为 coding agent 概念开发的唯一基础概念。

本次审计使用登录后的 Scopus，按用户提醒采用精确短语检索，即在检索词外加英文双引号。

## 2. Scopus 检索方式

Scopus 页面：Documents search  
字段：Article title, Abstract, Keywords  
排序：Date newest  
检索形式：`"phrase"`，例如 `"workspace awareness"`

这等价于在题名、摘要和关键词中检索完整短语，而不是把词拆开。

## 3. 精确短语检索结果概览

| 精确短语 | Scopus documents found | 最新摘要中的主要语义 | 对 coding agent 的初步判断 |
| --- | ---: | --- | --- |
| `"workspace awareness"` | 162 | CSCW/HCI 中的共享空间、协作者行动、AR/VR/robotics、hybrid work、social presence / connectedness | 有关，但不是纯粹 coding-agent-specific；不能轻率作为唯一基础概念 |
| `"situation awareness"` | 11,385 | 搜救、网络安全、医疗、驾驶、机器人、决策支持等动态任务状态理解 | 太通用，但定义和测量最成熟，适合迁移为 coding-agent task-state awareness |
| `"mutual understanding"` | 7,395 | 医疗、教育、跨代沟通、应急协作、组织沟通等非常宽泛的相互理解 | 过宽，且容易滑向人-agent 双边理解，不适合直接作为核心 |
| `"common ground"` | 22,852 | 语言学、沟通、伦理、跨学科协商、协作分析等 | 适合解释 prompt/context grounding，但不是代码工作状态觉察 |
| `"transactive memory system"` | 631 | 团队/组织中谁知道什么、知识分布、专业性、可信度、协调 | 适合解释用户知道 agent 擅长什么，不适合解释当前 agent 正在改什么 |
| `"shared mental model"` | 1,341 | 团队成员对角色、流程、责任和沟通的相似理解 | 偏团队层和相似性测量，不适合作为 individual-level 主构念 |
| `"process visibility"` | 180 | 平台共创、流程透明、协作过程可见性、组织/平台开发 | 更像设计属性或前因，不是用户认知状态本身 |
| `"activity awareness"` | 347 | 大量被 physical activity / health awareness 污染，也有协作活动觉察 | 短语不干净，不适合做基础概念 |
| `"collaborative context awareness"` | 18 | context-aware applications、robotics、USAR/cobot 等 | 文献太少，且多是系统能力，不是用户体验构念 |
| `"agent awareness"` | 116 | 多数指 agent 自身意识/感知、智能体能力或心理学实验 | 不适合我们要测的用户体验 |
| `"automation transparency"` | 140 | 自动化/技术透明度、区块链、自动化系统信息呈现 | 重要但更像系统设计属性，不是用户形成的认知状态 |

## 4. workspace awareness：定义和最新用法

### 4.1 关键定义文献

Gutwin and Greenberg 的经典框架把 workspace awareness 定义为：

> the up-to-the-moment understanding of another person's interaction with the shared workspace

这个定义有三个关键限定：

1. 它是 **understanding**，不是系统信息呈现本身；
2. 它关注 **another person's interaction**，不是所有任务状态；
3. 它依附于 **shared workspace**，不是一般情境理解。

在同一框架中，作者进一步说明 WA 涉及知道他人在哪里工作、正在做什么、接下来会做什么；这些信息用于协调行动、管理耦合、围绕任务沟通、预期他人行动和寻找帮助机会。

这说明 `workspace awareness` 的经典核心是：

> 用户对人类协作者如何与共享工作空间互动的即时理解。

### 4.2 Scopus 最新摘要显示的实际用法

Scopus 最新结果显示，`workspace awareness` 仍主要围绕共享空间和协作行动，但具体语境发生了扩展。

2026 年 CHI 结果包括 co-located AR industrial robot programming，关注多用户如何在共享 workspace 中协调、维护 awareness、协商 control。

2026 年 CHI 另有 human-agent collaboration research platform。摘要把 human-human collaboration 中的 process visibility 和 workspace awareness 作为出发点，并指出 LLM agent collaboration 需要检验这些 CSCW 原则是否延续、改变或失效。这个结果和我们高度相关，但它不是 workspace awareness 的定义文献，而是把 WA 作为人机协作研究平台的理论背景之一。

2025 年 CSCW 结果明确出现 hybrid office work：远程在家员工缺少 office dynamics / workspace awareness，会产生 isolation，并妨碍沟通。相关设计用 information displays 呈现办公室活动，以提升 social presence 和 contextual sensemaking。

2025 年 CHI 的 LiteCo 也明确把 home office 中缺少同事位置、presence 和 intentions 视为 WA 缺失，并用 ambient display 增强 WA 和 social connectedness。

其他最新结果集中在 collaborative AR、VR shared perspective、cross-virtuality geospatial analysis、human-robot close interaction 等空间协作场景。

### 4.3 对我们意味着什么

用户的提醒是对的：Scopus 最新文献中，`workspace awareness` 的一条重要使用线索已经和 hybrid work、远程在场、孤立感、social connectedness 相关。这不是说 WA 完全等于“不孤独”，但它确实经常被用于解释远程员工缺少办公室动态和同事在场信息的问题。

因此，如果我们把 `workspace awareness` 作为唯一基础概念，会有两个风险：

1. 审稿人可能会把它理解为 CSCW/HCI 中的共享空间/协作者在场/社交连接问题，而不是 coding agent 监督问题；
2. 它的经典定义对象是 “another person”，而 coding agent 是 autonomous, tool-using, code-changing agent。我们需要迁移的幅度很大。

更稳妥的处理方式是：

> `workspace awareness` 可以作为相邻理论，用来提醒我们关注 shared code workspace、agent action traces、diff visibility、tool execution visibility；但它暂时不应作为唯一基础概念。

## 5. 其他候选概念的定义适配性

### 5.1 situation awareness

经典 SA 定义关注个体在动态任务环境中对相关元素的感知、理解和预测。它不是社会在场，也不是协作者关系，而是 task-state cognition。

Scopus 检索显示它极其宽泛，最新结果涉及搜救、网络安全、医疗、自动驾驶、机器人等。这说明它不是 coding-agent-specific，但也说明它的定义适合动态任务状态迁移。

对我们最有价值的不是直接写 `situation awareness`，而是迁移为：

> coding-agent task-state awareness / agent-mediated coding situation awareness

也就是用户能否在 coding agent 编程任务中感知 agent 正在做什么、理解代码和工具状态变化的意义、预测继续授权后的影响。

### 5.2 mutual understanding

`mutual understanding` 在 Scopus 中非常宽泛，最新文献可以是精神科培训中的代际理解，也可以是应急响应协作。IS 文献中它常用于 stakeholder / CEO-CIO / business-IT 之间的理解对齐。

它的问题是：定义重心在双方理解是否对齐，而 coding agent 场景里最关键的不一定是“我和 agent 是否互相理解”，而是“我是否理解 agent 已经如何改变任务状态，以及下一步会如何改变”。

因此它适合作为 prompt/context alignment 的背景，不适合作为主基础概念。

### 5.3 common ground

`common ground` 的定义核心是共同知识、共同信念、共同假设，以及通过 grounding 过程确认沟通足以继续。

它对 coding agent 有明显价值：用户和 agent 是否共享任务目标、约束、上下文、术语和 referents。但它仍然主要解释沟通基础，而不是 agent 改代码后的 task state awareness。

因此它更适合解释前因：

> 更好的 prompt grounding / context grounding 会提高用户对 agent-mediated coding state 的理解。

### 5.4 transactive memory system

TMS 的核心是团队如何编码、存储和检索分布式知识，尤其是知道谁知道什么、谁可靠、如何协调调用知识。

迁移到 coding agent 时，它可以解释：

- 用户是否知道 agent 擅长哪些任务；
- 用户是否知道哪些知识应交给 agent、哪些自己保留；
- 用户是否相信 agent 在特定领域的知识可靠。

但它不直接解释用户在一个具体 task episode 中是否看懂 agent 的行动、diff、测试和风险。因此不适合作为我们当前主构念。

### 5.5 shared mental model

SMM 最新 Scopus 摘要仍典型地测量团队成员对角色、责任和沟通流程的相似理解。它的 measurement 通常是 team-level similarity / alignment，而不是单个用户对 agent-mediated work state 的认知状态。

如果用于 coding agent，它很容易变成“用户和 agent 是否有相似 mental model”，这在人-agent场景里理论和测量都比较难。因此不适合作为主基础概念。

### 5.6 process visibility / transparency / explainability

这些概念很有实践价值，但它们更像设计属性：

- 系统是否显示过程；
- 是否解释行动原因；
- 是否暴露信息；
- 是否让用户能追踪执行。

它们可以作为前因影响我们的核心构念，但不应替代核心构念。因为我们要测的不是界面显示了多少，而是用户是否形成了可操作理解。

## 6. 修正后的建议

我现在修正 38 号文档的判断：

> 不建议把 `workspace awareness` 作为唯一基础概念。

更合适的选择是：

> **基础概念：situation awareness**  
> **新构念暂定名：coding-agent task-state awareness / 编码代理任务状态觉察**

更明确的定义草案：

> 编码代理任务状态觉察是指，用户在一次 coding-agent 编程任务中，对 agent 行动、代码工件状态、工具执行结果、任务约束和后续影响所形成的可操作认知状态。它表现为用户能否识别当前发生了什么，理解这些变化对任务目标、代码语义、约束和风险的意义，并预测继续授权或介入后任务状态可能如何变化。

这个定义比 `coding-agent workspace awareness` 更稳，原因是：

1. 它的基础概念 SA 本身就是 individual-level 的动态任务状态认知；
2. 它能自然吸收 coding agent 中的 code workspace、diff、terminal、test、approval 等元素；
3. 它不容易被误读为 hybrid work 中的 social connectedness 或办公室在场；
4. 它能把 control、trust、approval fatigue、verification burden 放在后果或边界变量中，而不是混进构念定义。

## 7. workspace awareness 以后怎么用

`workspace awareness` 不应被丢掉，但应降级为相邻文献，作用是帮助我们具体化 coding agent 情境中的 shared code workspace：

- agent action trace；
- modified files / symbols；
- command and tool execution history；
- diff visibility；
- test and verification state；
- approval context；
- next-step impact.

换句话说，WA 可以帮助我们解释 **SA 在 coding agent 情境中具体要觉察哪些 workspace elements**，但它不适合单独承担 foundational concept 的角色。

## 8. 下一步

下一步应该做两件事：

1. 继续用 Scopus 精确短语和经典定义文献核查 `situation awareness` 在 IS/HCI 中如何被迁移，尤其是 dashboards、cybersecurity、automation、human-agent collaboration；
2. 从 Reddit coding agent 评论中编码自然语言证据，看用户抱怨是否确实集中在 task-state awareness 缺失：看不清改动、无法判断下一步、审批缺上下文、验证负担过高、接管困难。

如果 Reddit 数据支持这个方向，我们的概念开发叙事就可以是：

> 传统 SA 解释了动态任务中个体如何感知、理解和预测任务状态；coding agent 把这个动态任务状态变成由 autonomous agent 行动、代码工件变化、工具执行结果和审批边界共同构成的 agent-mediated coding state。因此需要开发 coding-agent task-state awareness 来刻画用户是否能对这种新型任务状态形成可操作理解。

