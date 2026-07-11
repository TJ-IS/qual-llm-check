# 结合 Chen 2024 与 Dong Thesis 的 CADU 概念开发逻辑

> **已废弃 / superseded.** 这份文件保留为一次误走方向的记录。用户已明确指出：我们不是要用 usability 作为主构念，而是要为“协同/协调负担”寻找基础概念，并从该基础概念出发进行 coding-agent-specific 的改造。后续应回到 coordination cost / coordination burden in managing interdependencies、software project coordination、artifact-based coordination、technology-enabled coordination affordances 与 IS delegation 之间的关系。

## 1. 为什么还要结合 Dong thesis

上一版已经按 Chen et al. (2024 MISQ) 把主线修正为：

> 以 usability 为基础概念，发展 coding-agent delegation usability。

但你说得对，只模仿 Chen 还不够。Dong thesis 的第 3 章也是一个很典型的“基于已有广义概念发展情境化构念”的做法。

Dong thesis 的基础概念是：

**技术可供性 / IT affordance**

它发展的情境化构念是：

**社会化商务技术可供性 / IT affordance in online social commerce**

它的关键写法不是“社会化商务是新场景，所以造一个新概念”，而是：

1. 先说明 IT affordance 已经是 IS 领域解释技术与用户行为关系的重要广义概念；
2. 再说明社会化商务既不是传统电商，也不是普通社交媒体；
3. 因此已有 affordance 维度不能完全覆盖社会化商务中“社交 + 购物”双重目标；
4. 最后发展社会化商务技术可供性，识别维度并量表化。

对应到我们这里，应该写成：

1. usability 是 IS/HCI 中解释用户能否通过系统达成目标的重要广义概念；
2. coding agent 既不是传统 IDE，也不是代码补全，也不是普通聊天 AI；
3. 因此已有 usability/ease of use 维度不能完全覆盖“委托 agent 在代码库中行动”的体验；
4. 最后发展 **coding-agent delegation usability**，识别维度并量表化。

## 2. 两篇参考文献给我们的不同启发

| 参考 | 它基于哪个广义概念 | 它怎样改造 | 对我们的启发 |
| --- | --- | --- | --- |
| Chen et al. 2024 MISQ | usability | 从一般 usability 发展 voice-interaction usability，并用 CPT 组织维度 | 我们应从 usability 发展 coding-agent delegation usability |
| Dong thesis | IT affordance | 从一般 IT affordance 发展 social commerce IT affordance，并用用户目标 + 技术能力解释维度 | 我们应说明每个 CADU 维度如何连接用户的委托编程目标与 coding agent 的技术能力 |

所以，我们现在不应该只说：

> CADU 是一个 coding-agent-specific UX 构念。

而应该说：

> CADU 是对 usability 这一广义概念的情境化发展；它借鉴 Dong thesis 的 affordance 逻辑，将每个 usability 维度解释为 coding agent 技术能力支持开发者完成委托编程目标的方式。

## 3. Dong thesis 的“基础概念改造”写法

Dong thesis 的概念开发段落有几个关键动作。

### 3.1 先承认已有广义概念有用

Dong 没有否定技术可供性，反而说技术可供性很适合解释 IT 功能与用户目标行为之间的关系。

我们也应该这样写：

> Usability remains a natural and important concept for understanding users' experiences with coding agents, because coding agents are ultimately evaluated by whether users can accomplish programming goals effectively, efficiently, and satisfactorily.

也就是说，我们不是推翻 usability，而是承认它是基础。

### 3.2 再指出新情境让旧概念不够

Dong 指出，社会化商务有“商务性”和“社交性”双重属性，既有 affordance 维度不能完全覆盖。

我们对应写：

> Coding-agent use has a dual nature: it is both software tool use and agentic task delegation. Users do not merely operate an interface; they delegate programming goals to an agentic IS artifact that can autonomously plan actions, invoke tools, modify code, and return control to users for approval, verification, or recovery. Therefore, existing usability dimensions developed for websites, mobile applications, or direct-manipulation software cannot fully capture this context.

### 3.3 然后定义情境化构念

Dong 定义社会化商务技术可供性时，把“用户目标”和“技术支持”放在一起。

我们也应该在 CADU 定义中同时放入：

- 用户目标：完成具体编程任务；
- 技术对象：能自主行动的 coding agent；
- 交互方式：委托而非直接操作；
- 关键情境：mutable codebase；
- 评价结果：有效、有效率、可承受、可恢复地达成目标。

建议定义：

> **Coding-agent delegation usability** refers to the extent to which developers perceive that they can accomplish programming goals effectively, efficiently, and manageably by delegating a concrete coding task to a coding agent, whose autonomous actions, permission handoffs, codebase changes, and recovery paths remain articulable, traceable, governable, inspectable, and recoverable within a mutable software artifact.

中文：

> **编码代理委托可用性**是指，开发者感知到自己能够通过将具体编程任务委托给 coding agent，以有效、有效率且可承受的方式完成编程目标的程度；这种可用性取决于 agent 的自主行动、权限交还、代码库变更和恢复路径是否能在可变代码库中被表达、追踪、治理、检视和恢复。

### 3.4 定义后要说“单靠定义还不够”

Dong thesis 明确写到：虽然已经定义了社会化商务技术可供性，但单从定义还不能充分理解其内涵组成，需要继续识别维度。

我们也应该照这个句式：

> Although this definition specifies the scope of coding-agent delegation usability, the definition alone is insufficient to reveal its internal structure. Because delegating programming work to a coding agent involves multiple user-agent-codebase activities, including task specification, agent action tracking, permission handoff, codebase inspection, and takeover/recovery, it is necessary to identify the dimensions that constitute this context-specific usability construct.

## 4. Dong-style 的核心：每个维度都要写“用户意向 + 技术能力”

Dong thesis 的表 3-2 很关键。它不是只给维度名，而是对每个维度写：

- 定义；
- 用户意向；
- 技术能力；
- 功能举例；
- IT 特征。

这一点我们必须模仿。否则 CADU 会像抽象的 UX 词，缺少技术对象和行为目标。

下面是 CADU 的 Dong-style 初步维度表。

| CADU 维度 | 定义 | 用户意向 | coding agent 技术能力 | 功能/机制例子 | 来源概念 |
| --- | --- | --- | --- | --- | --- |
| 委托意图可表达性 | 用户能否清楚表达任务目标、边界、上下文、约束和验收标准 | 把“我要 agent 做什么、不要做什么、做到什么算完成”说清楚 | 支持任务范围设定、上下文投喂、文件/目录约束、验收条件表达 | plan mode、scope selector、context files、acceptance criteria、do-not-touch list | usability 中的 ease of use；IS delegation 中的 rights/responsibilities distribution |
| 代理行动可追踪性 | 用户能否理解 agent 做了什么、为什么做、做到哪一步 | 跟上 agent 的多步行动，判断它是否仍在正确路径上 | 支持计划展示、命令日志、文件访问记录、中间决策解释、进度状态 | action log、stepwise plan、command transcript、reasoning summary、progress checkpoint | feedback、visibility、communication visibility、workspace awareness |
| 权限交还可治理性 | 用户能否有效处理 agent 发起的审批、权限请求、继续/停止判断 | 分流普通请求与高风险请求，决定让 agent 继续、限制或停止 | 支持权限分级、风险提示、审批批处理、自主性调节、策略配置 | risk-tiered approvals、approval batching、autonomy slider、policy rules、pause/continue controls | user control、interruption overload、warning habituation、human-AI delegation |
| 代码库状态可检视性 | 用户能否检查和理解 agent 对代码库造成的变更及其影响 | 判断代码改了哪里、为什么改、会不会影响其他模块，是否可合入 | 支持 diff、测试、依赖影响、行为变化、模块影响的可视化与整合 | semantic diff、test summary、impact analysis、dependency map、changed-behavior summary | artifact-based coordination、software coordination、verification、feedback |
| 接管恢复可操作性 | 用户能否在 agent 偏离或失败时暂停、接管、回滚、修复或重启任务 | 在风险或失败时重新获得任务进程的可操作性 | 支持 checkpoint、rollback、partial accept/reject、state summary、handover brief、repair suggestions | checkpoints、git restore、branch sandbox、takeover summary、repair plan | recoverability、error recovery、supervisory control、residual responsibility |

这个表非常重要。它让每个维度都不是“我觉得怎么样”的抽象感受，而是：

> 某种 coding agent 技术能力，如何支持开发者完成某类委托编程目标，并因此构成 coding-agent delegation usability 的一部分。

## 5. 从 Dong thesis 看，我们是否应该改成 affordance 构念？

这是需要认真讨论的。

### 5.1 可选路线 A：CADU 作为主构念，affordance 作为维度解释逻辑

这是我目前推荐的路线。

主构念：

**Coding-Agent Delegation Usability**

基础概念：

**usability**

理论框架：

**IS delegation / coordination**

维度解释方式：

借鉴 Dong thesis 的 affordance 逻辑，用“用户意向 + 技术能力”说明每个维度。

优点：

- 最像 Chen 2024；
- 直接是用户体验构念；
- 能和 TAM、UTAUT、MUG、generic usability 比较；
- perceived control、approval fatigue、continued delegation willingness 都能作为后果；
- 不会把研究变成纯设计特征或平台功能研究。

### 5.2 可选路线 B：开发 Coding-Agent Delegation Affordances

也可以更像 Dong thesis，主构念改成：

**Coding-Agent Delegation Affordances**

定义：

> 开发者感知到 coding agent 的技术功能能够支持其完成委托编程活动的可能性。

可能维度：

- task-specification affordance；
- action-tracing affordance；
- permission-governance affordance；
- codebase-inspection affordance；
- takeover-recovery affordance。

优点：

- 和 Dong thesis 完全同构；
- 更偏设计和功能；
- 便于解释“什么工具能力影响用户体验”。

缺点：

- 它更像 CADU 的前因，而不是 UX 本身；
- 用户原来关心的是 coding agent 体验和重要 UX 议题，affordance 可能太偏技术能力；
- 后续还需要再解释 affordances 如何影响 perceived control、fatigue、continued use 等。

### 5.3 我的建议

主论文不要把主构念改成 affordance。更稳的是：

> 主构念采用 Chen-style 的 **Coding-Agent Delegation Usability**，维度识别和解释采用 Dong-style 的 **user intention + technology capability**。

这样我们同时获得两篇参考的优点：

- Chen 让我们有清楚的 UX 基础概念和量表开发路径；
- Dong 让我们把维度和具体技术能力、用户目标绑定起来。

## 6. 应该模仿 Dong thesis 怎么讲“旧概念不够”

Dong thesis 的写法不是泛泛说“旧概念不能解释新场景”。它有三层：

1. 现有广义概念重要；
2. 新情境有特殊目标和活动；
3. 旧维度不能完整覆盖这些目标和活动。

我们可以写成：

> Prior IS research has developed mature concepts such as usability, perceived ease of use, and user satisfaction to explain users' experiences with information systems. These concepts are useful because coding agents are still evaluated by whether they help users accomplish programming goals. However, coding-agent use differs from traditional IS use because the user delegates a task to an agentic IS artifact that can autonomously act on a mutable codebase. In this context, usability is no longer only a matter of interface operation, response clarity, or ease of learning. It also depends on whether users can articulate delegation goals, trace agent actions, govern permission handoffs, inspect codebase state changes, and recover or take over when necessary. Existing usability dimensions do not fully capture these activities; thus, a context-specific conceptualization and measurement of coding-agent delegation usability is needed.

这段话就同时像 Chen 和 Dong。

## 7. 应该模仿 Dong thesis 怎么讲“维度不是随便来的”

Dong thesis 的维度来自三处：

1. 现有文献中的 affordance 维度；
2. 访谈和小组讨论中的用户/专家表达；
3. 社会化商务实际活动分析。

我们也应该写：

CADU 维度来自三处：

1. **现有文献**：usability、ease of use、feedback、visibility、user control、recoverability、IS delegation、coordination、communication visibility、artifact-based coordination；
2. **用户材料**：Reddit 评论、访谈、真实工具使用日志、diff/审批提示；
3. **coding agent 活动分析**：任务委托、计划执行、工具调用、代码修改、审批交还、测试验证、接管恢复。

然后每个维度都要说明它和旧概念的关系：

| CADU 维度 | 继承了什么旧概念 | 为什么要重新命名/重新定义 |
| --- | --- | --- |
| 委托意图可表达性 | ease of use, task specification, delegation distribution | coding agent 的“输入”不是简单操作，而是把任务边界、上下文和责任分配给 agent |
| 代理行动可追踪性 | feedback, visibility, transparency, communication visibility | 用户需要追踪的是 agentic action trajectory，不是单一界面反馈或人际消息 |
| 权限交还可治理性 | user control, interruption management, warning design | coding agent 的控制发生在多次权限交还中，用户要判断风险而不是只操作按钮 |
| 代码库状态可检视性 | verification, artifact-based coordination, software review | agent 的输出是可变代码库状态，不是静态文本答案或页面反馈 |
| 接管恢复可操作性 | recoverability, error recovery, takeover, supervisory control | 用户要从 agent 已经推进过的任务状态中恢复，而不是简单撤销一个界面错误 |

## 8. Dong-style 的研究程序如何嵌入我们的计划

### 8.1 问题形成

文献已经有 usability、ease of use、trust、control、technostress、coordination 等概念，但 coding agent 作为 agentic IS artifact 带来了新型 user-agent-codebase 关系。现有概念无法完整描述用户通过委托 agent 完成编程任务时的可用性。

### 8.2 问题建议

提出 **Coding-Agent Delegation Usability** 作为情境化构念，用来描述用户对 coding agent 委托编程任务可用性的感知。

### 8.3 发展

结合三类材料发展维度：

- Top11 文献中的基础概念；
- Reddit / 访谈 / 工具日志中的用户表达；
- coding agent task episode 的活动分析。

### 8.4 评估

模仿 Dong：

- 专家小组讨论维度是否完整；
- 开放式卡片分类检验维度是否自然聚合；
- Q-sort 检验题项和维度匹配；
- EFA/CFA 或 PLS-SEM 检验一阶反映式、二阶形成式结构；
- 与旧概念比较区分效度和增量解释力。

### 8.5 结论

形成 CADU 的定义、维度、测量题项和后续实证模型基础。

## 9. 根据 Dong thesis，CADU 更适合形成式二阶构念

Dong thesis 把社会化商务技术可供性作为二阶形成式构念，因为六个一阶维度共同形成整体 affordance，任何一个维度改变都会改变构念内涵。

CADU 也应如此：

- 委托意图可表达性高，不代表代码库状态可检视性高；
- 代理行动可追踪性高，不代表权限交还可治理性高；
- 代码库状态可检视性高，不代表接管恢复容易；
- 五个维度共同形成 coding-agent delegation usability。

因此建议：

- 二阶 CADU：形成式；
- 五个一阶维度：反映式；
- 每个一阶维度 3-5 个最终题项；
- 初始题项池至少 40-60 个；
- 同时开发 3-5 个 global CADU items，用于二阶构念验证。

## 10. Dong-style 初始题项生成方式

Dong thesis 的题项常用句式是：

> The OSC platform allows/enables/provides/informs/helps me...

我们可以对应生成 CADU 的题项语言：

### 委托意图可表达性

- The coding agent allows me to clearly specify the boundaries of the coding task.
- The coding agent enables me to communicate which files or modules should not be changed.
- The coding agent helps me express the acceptance criteria for the task.

### 代理行动可追踪性

- The coding agent allows me to keep track of the actions it has taken during the task.
- The coding agent provides enough information for me to understand why it changed particular files.
- The coding agent helps me understand how its intermediate steps relate to my original task.

### 权限交还可治理性

- The coding agent helps me distinguish routine permission requests from risky ones.
- The coding agent enables me to decide when it should continue, pause, or ask for my input.
- The coding agent provides enough context for me to make approval decisions.

### 代码库状态可检视性

- The coding agent allows me to inspect how its changes affect the current codebase.
- The coding agent helps me understand the implications of its code changes across files or modules.
- The coding agent provides enough evidence for me to judge whether its changes can be accepted.

### 接管恢复可操作性

- The coding agent enables me to recover the task state when its work goes wrong.
- The coding agent allows me to take over the task without losing track of what has already been done.
- The coding agent helps me revert, repair, or redirect its work when necessary.

这些只是 Dong-style 句式示范，不应作为最终题项。最终题项必须来自 Reddit、访谈、专家评估和卡片分类。

## 11. 现在的最佳研究定位

综合 Chen 和 Dong，我建议我们把项目写成：

> 本研究以 usability 为基础概念，借鉴 IS delegation 与 coordination 理论，发展 coding-agent delegation usability 这一情境化 UX 构念。与传统软件可用性不同，coding agent 的可用性不是直接操作界面的容易程度，而是用户能否通过委托 agentic IS artifact，在可变代码库中有效表达任务意图、追踪代理行动、治理权限交还、检视代码库状态并接管恢复任务。我们将使用 Reddit 用户评论和访谈材料识别维度，并通过多轮量表开发验证该构念的信度、效度和相对旧模型的增量解释力。

这句话里：

- **usability** 是广义基础概念；
- **coding-agent delegation usability** 是情境化新构念；
- **IS delegation / coordination** 是理论组织框架；
- **用户意向 + 技术能力** 是 Dong-style 维度解释逻辑；
- **Reddit + 访谈 + 量表开发** 是方法路径。

## 12. 下一步应更新哪些文件

建议把项目文档调整成三份核心文件：

1. `CADU_construct_definition.md`
   - 正式定义；
   - 与 usability、ease of use、control、trust、technostress、affordance 的边界；
   - 说明 CADU 是二阶形成式构念。

2. `CADU_foundational_gap_table.md`
   - 仿 Chen 的 Table 1/Table 2；
   - 仿 Dong 的“旧维度与新情境对照”；
   - 列出旧 usability/affordance/control/visibility/recoverability 维度为何不足。

3. `CADU_dimension_development_protocol.md`
   - 仿 Dong 的维度识别流程；
   - 文献 + Reddit + 访谈 + 专家小组；
   - 每个候选维度必须写用户意向、技术能力、功能例子、来源概念。
