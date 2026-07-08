# 高适配文献二次审阅：Coding Agent UX 核心机会

说明：本文件只审 `consensus_inclusion_strict_analysis.md` 中被标为 `高适配` 的 65 篇。审阅目标不是再次确认“能不能类比”，而是筛出对 coding agent 同时具有高重要性、高独特性和高概念开发价值的少数 UX 方向。判断仍基于 CSV 中的标题、摘要、关键词和前一轮复判摘要，未做全文精读。

## 我的总体判断

65 篇高适配里，真正适合作为 coding-agent-specific UX 主概念的不是泛泛的 `trust`、`explanation`、`flow`、`algorithm aversion`。这些都太容易变成旧概念换场景。

更有价值的是：coding agent 作为能读代码、改文件、跑命令、产生多步副作用的代理，把这些旧概念重新组合成了几个更独特的问题：

1. 开发者把行动交给 agent，但仍要为结果负责。
2. agent 产出的代码看似完整，却很难被充分验证。
3. 开发者必须判断 agent 能做什么、何时该接管、何时该放手。
4. 失败不是一次性建议错误，而是可以污染代码库、打断节奏并需要共同修复。
5. 长期使用会改变开发者的角色、技能感和专业身份。

我建议先把研究主线压到前三个，后两个作为扩展或边界条件。

## 最值得优先推进的 6 个方向

| 优先级 | 候选方向 | 简短定义 | 重要性 | 独特性 | 概念/量表开发价值 | 我的建议 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | 残余责任下的委托 | 开发者让 coding agent 执行任务，但仍感到自己必须理解、解释、承担和修复其结果 | 极高 | 极高 | 极高 | 最适合作为主概念或总框架 |
| 2 | 代理输出的可验证性缺口 | agent 生成的代码、diff、命令结果和解释是否让开发者真的能判断正确性 | 极高 | 极高 | 极高 | 可作为独立核心构念，也可作为方向 1 的关键维度 |
| 3 | 代理能力边界感 | 开发者对 agent 在当前仓库、任务、上下文中的能力边界和失败模式的判断能力 | 极高 | 高 | 极高 | 很适合解释信任校准和委托质量 |
| 4 | 可修复的代理协作 | 当 agent 误解需求、改坏代码或走偏时，开发者能否低成本定位、回滚、纠正并继续协作 | 高 | 高 | 高 | 适合做交互质量和失败恢复概念 |
| 5 | 监督节奏与心流保护 | agent 的请求、通知、审批和状态更新是否在正确时机进入开发者注意力 | 高 | 中高 | 中高 | 重要 UX 点，但更像机制或设计变量 |
| 6 | 开发者角色与专业身份重构 | coding agent 使开发者从直接编码者转向委托者、审查者、协调者或责任承担者时的身份体验 | 高 | 中高 | 高 | 长期研究很有价值，短期量表开发需小心不要泛化成 AI threat |

## 方向 1：残余责任下的委托

这是我认为最有希望的主线。它不是普通的 delegation，也不是普通的 trust。coding agent 的独特性在于：用户把实际行动交给 agent，agent 能改动真实代码库并产生可提交成果，但最终责任、解释压力和风险后果仍落在开发者身上。

可以考虑的概念名：

- 残余责任下的委托
- Accountable Delegation to Coding Agents
- Responsible Agentic Delegation
- 委托-责任张力

为什么重要：

- 直接影响开发者愿不愿意让 agent 做更大任务。
- 直接影响代码质量、安全风险、review 深度、merge 决策。
- 解释了为什么“省时间”同时可能带来“更累的责任感”。

为什么独特：

- 传统软件工具通常不主动行动，责任边界相对清楚。
- 普通聊天机器人通常不直接修改生产性工件。
- 决策支持系统可以给建议，但 coding agent 会生成可运行、可提交、可破坏的代码。

可能维度：

- 委托边界清晰度：我是否知道哪些任务可以交给 agent。
- 残余责任感：agent 写的代码出错时，我是否觉得仍然是我的责任。
- 可拥有感：我是否能把 agent 产出理解并“认领”为自己的工作。
- 责任不对称感：agent 行动越多，我承担越多解释和修复压力。
- 接管准备度：我是否知道何时暂停、回滚或亲自处理。

代表文献锚点：

- #51 `The next generation of research on IS use`，代理性 IS artifact 的委托理论。
- #6 `When Algorithms Delegate to Humans`，算法向人反向委托。
- #67 `Direct and indirect information system use`，间接使用和保留责任。
- #100 `Increasing accountability through user-interface design artifacts`，界面设计如何增强问责感。
- #144 `The contradictory structure of systems development methodologies`，责任参与矛盾。
- #193 `A role theory perspective on end-user development`，用户/开发者角色转换。
- #199 `Decision support systems: Directed and nondirected change`，限制性和引导性。

## 方向 2：代理输出的可验证性缺口

这个方向可能是最 coding-agent-specific 的 UX 概念。核心不是“我信不信 agent”，而是“我是否真的有能力、有线索、有时间验证 agent 做了什么”。

可以考虑的概念名：

- 代理输出可验证性缺口
- Perceived Verifiability of Agentic Code Output
- Verification Tractability
- Agentic Verification Burden

为什么重要：

- coding agent 最大的现实风险常常不是完全不能用，而是“看起来能用，但不确定哪里有问题”。
- 开发者可能为了省力而降低审查深度，或者因为难以验证而不敢委托。
- 它连接代码质量、安全、学习、信任校准和责任归属。

为什么独特：

- 代码正确性有潜在 bug、边界条件、架构一致性、长期维护性等隐性维度。
- agent 可能一次性生成跨文件 diff，验证成本不一定低于手写。
- 解释、测试、日志、命令记录、diff 粒度都变成 UX 的一部分。

可能维度：

- 输出透明度：我是否看得懂 agent 改了什么。
- 验证证据充分性：测试、日志、解释是否足以支持判断。
- 隐性风险感知：我是否担心看不见的 bug 或架构副作用。
- 验证成本：检查 agent 产出是否比自己做还费劲。
- 警觉校准：我是否既不过度怀疑，也不过度放松。
- 误报/漏报权衡：我是否能区分值得深查的问题和无害噪音。

代表文献锚点：

- #2 在线医疗建议评价，用户难以区分专家建议质量，依赖启发式。
- #53 AI 辅助诊断中的元认知监控缺陷。
- #92 竞争方案评价中的双过程认知。
- #95 产品不确定性，可迁移为代码输出不确定性。
- #113 vigilant interaction，可迁移为监督和验证中的警惕互动。
- #156 人类能否检测数据错误，信号检测框架。
- #159 欺骗敏感性、检测成功率和误报权衡。
- #175 user calibration，信心与质量匹配。
- #198 决策辅助可能导致努力节省而非质量提升。
- #204 vigilant EIS，警觉性设计理论。

## 方向 3：代理能力边界感

这个方向关注开发者是否知道 agent 在当前具体任务里“何时强、何时弱、为什么弱”。它比一般 trust 更细，因为 coding agent 的能力高度依赖仓库上下文、任务类型、测试覆盖、工具权限、提示质量和历史步骤。

可以考虑的概念名：

- 代理能力边界感
- Agent Capability Boundary Sense
- Delegation Metaknowledge
- Task-Agent Fit Awareness

为什么重要：

- 好的委托首先依赖“知道什么该委托”。
- 很多失败不是 agent 完全差，而是任务-agent fit 判断错。
- 它能解释为什么同一个 agent 在不同开发者手中表现差异很大。

为什么独特：

- coding agent 不是单一功能工具，它在不同仓库、语言、测试环境、权限边界下表现不同。
- agent 的能力不是静态产品属性，而是由上下文窗口、工具链、任务拆解和交互历史共同塑造。
- 开发者需要判断的不只是“AI 准不准”，而是“这个 agent 此刻是否能安全推进这类代码任务”。

可能维度：

- 任务适配判断：我是否知道哪些任务适合 agent。
- 失败模式知识：我是否知道 agent 容易在哪些地方犯错。
- 上下文充分性感知：我是否知道 agent 是否掌握足够代码上下文。
- 接管阈值：我是否知道什么时候停止让 agent 继续。
- 性能反馈学习：我是否会根据近期表现更新委托策略。

代表文献锚点：

- #54 productive delegation，委托 AI 时的元知识缺陷。
- #56 AI know-what 与专家 know-how 脱节。
- #45 autonomous tools 的 unknowability 和 liminal experience。
- #166 mental models and proficiency。
- #184 编程作为多问题空间中的科学发现，表征转换困难。
- #18 性能信息如何帮助人类调整行为。
- #39 用户根据 robo-advisor 近期表现调整使用。
- #82 信任期望失验和使用成熟度。
- #180 用户预期现实性。

## 方向 4：可修复的代理协作

这个方向不把失败看成一次性错误，而看成一个协作过程：agent 误解需求、改错文件、跑偏方案、引入 bug 后，开发者能不能快速定位问题、让 agent 理解失败原因、回滚或继续推进。

可以考虑的概念名：

- 可修复的代理协作
- Repairable Agentic Collaboration
- Collaborative Debugging with Coding Agents
- Agentic Repairability

为什么重要：

- coding agent 的实际体验很大程度上取决于失败后能不能修回来。
- 高质量 repair 能降低验证成本和挫败感。
- repair 过程也是开发者学习 agent 能力边界的关键来源。

为什么独特：

- 聊天机器人 repair 多是语义澄清，coding agent repair 还涉及代码状态、测试结果、diff、回滚和上下文恢复。
- 错误可能累积在仓库里，修复不仅是“重新回答”，而是恢复工作路径。

代表文献锚点：

- #10 customer-chatbot collaborative repair strategies。
- #25 machine-induced reflection。
- #33 XAI 对用户信息处理和心智模型的影响。
- #105 技术事件触发的自动/调整型使用模式。
- #141 新手和专家对解释类型的差异化使用。
- #149 knowledge-based system explanations。
- #162 intelligent systems explanations。
- #177 explanation facilities and user acceptance。

## 方向 5：监督节奏与心流保护

这个方向适合做 coding agent 交互设计研究。关键问题不是“有没有中断”，而是 agent 何时请求审批、何时汇报状态、何时要求用户提供上下文、何时应静默推进。

可以考虑的概念名：

- 监督节奏适配
- Supervisory Flow Alignment
- Agentic Interruption Fit
- Developer Attention Governance

为什么重要：

- 编程高度依赖深度工作和问题空间保持。
- agent 如果频繁、不合时宜地打断，会破坏心流和上下文记忆。
- agent 如果完全不打断，又可能在错误方向上越走越远。

为什么独特：

- coding agent 的中断常常带有行动后果：审批命令、确认方案、解释失败、请求权限。
- 这不是普通通知，而是“监督一个正在行动的合作者”的注意力调度。

代表文献锚点：

- #20 IT-mediated interruptions and flow。
- #36 AI assistant 的主动信息提供、打断感和交互模式。
- #66 中断过载、心理转换和任务闭合。
- #75 中断时机与认知负荷。
- #117 awareness displays and coordination。
- #142 cognitive support for real-time dynamic decision making，监控与控制的注意力竞争。
- #30 warning habituation，可作为警告/审批疲劳的支撑。

## 方向 6：开发者角色与专业身份重构

这个方向偏长期、偏职业体验，但很有现实意义。coding agent 不只是帮助写代码，它会改变开发者觉得自己“在做什么”和“凭什么是专业开发者”。

可以考虑的概念名：

- 开发者角色重构
- Developer Role Re-authoring
- Agentic Professional Identity Work
- Coding Agent-Induced Expertise Reconfiguration

为什么重要：

- 影响开发者采纳、抵制、学习动机和职业焦虑。
- 解释为什么同样的效率提升，有人觉得被增强，有人觉得被削弱。
- 连接长期技能保持、知识侵蚀和专业自主感。

为什么独特：

- coding 是高度身份化的专业实践，agent 介入的是开发者核心能力而不是边缘工具。
- 开发者可能从直接生成代码转向定义任务、监督过程、审查结果和承担责任。

代表文献锚点：

- #5 professional identity work。
- #42 humans-in-the-loop and loss of unique knowledge。
- #48 intelligent system knowledge empowerment and adaptation。
- #59 physicians' face loss dilemma in CDSS use。
- #132 expert technological frames and identity。
- #138 mindshift learning。
- #164 task change and intrinsic motivation。
- #190 fairness perception and resistance to change。
- #193 role theory and end-user development。

## 我会降权的高适配方向

这些条目仍有参考价值，但我不建议把它们作为核心概念本身：

- 泛化的算法厌恶/欣赏：#4、#15。可作为信任校准背景，但不是 coding agent 独有。
- 泛化的 AI trust：#17、#126、#179。除非改造成“行动责任下的信任”，否则容易太宽。
- 泛化的期望、习惯、使用成熟度：#82、#120、#180。可解释使用变化，但独特性不足。
- 泛化的认知偏差：#12、#44、#74。适合放入验证/委托机制，不适合单独成为主概念。
- 泛化的解释质量：#149、#162、#177。适合服务“可验证性”和“可修复性”，不宜停留在 explanation 本身。

## 最推荐的研究切入

如果目标是开发新的概念和量表，我建议优先考虑一个总概念加两个核心维度：

总概念：残余责任下的代理委托体验

核心维度：

1. 可验证性缺口：开发者是否能有效判断 agent 产出是否正确、安全、可维护。
2. 能力边界感：开发者是否知道何时、如何、把什么任务委托给 agent。
3. 责任可拥有感：开发者是否能理解、解释并承担 agent 的代码改动。
4. 可修复性：agent 失败后是否容易定位、回滚、纠正和恢复协作。

这条线比单独研究 trust 更有 coding agent 味道。它也比单独研究 flow 或 explanation 更容易回答“为什么这是 coding agent 特有的重要 UX 问题”：因为这里同时出现了代理行动、代码副作用、验证困难和开发者残余责任。

