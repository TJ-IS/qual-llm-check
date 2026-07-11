# 代理性代码状态脱节感：文献迁移依据

## 候选构念

中文暂定：代理性代码状态脱节感

英文暂定：Perceived Agentic Codebase State Drift

## 定义

代理性代码状态脱节感是指：在 coding agent 自主或半自主地读取、修改、运行和迭代代码之后，开发者感到当前代码库的实际状态，已经偏离自己对任务实现路径、修改范围、代码行为和风险位置的心理表征的程度。

更简单地说，它测量的是：

agent 把代码库推进到了一个状态，但开发者是否还跟得上这个状态。

## 为什么这个概念值得单独发展

这个概念不是把 trust、delegation、explainability 或 code review 换到 coding agent 情境里。它抓住的是 coding agent 产生的新问题：

传统工具或决策支持系统通常给用户信息、建议或局部功能支持；coding agent 会连续读取代码、修改文件、运行命令、根据结果继续修复，并把代码库推进到一个新状态。于是，开发者面对的不是“我要不要相信一个建议”，而是“代码库现在已经被 agent 改成了什么状态，我是否还能跟得上”。

这个问题对实践很重要，因为只要开发者跟不上代码状态，就会直接影响 review 时间、bug 发现率、merge 信心、回滚/重做行为、后续委托范围和责任焦虑。

## 相关文献信息

| 编号 | 标题 | 年份 | 期刊 |
| ---: | --- | --- | --- |
| #184 | Why Is Programming (Sometimes) so Difficult? Programming as Scientific Discovery in Multiple Problem Spaces | 1997 | Information Systems Research |
| #45 | The Unknowability of Autonomous Tools and the Liminal Experience of Their Use | 2021 | Information Systems Research |
| #51 | The next generation of research on is use: A theoretical framework of delegation to and from agentic is artifacts | 2021 | MIS Quarterly: Management Information Systems |
| #53 | Augmenting medical diagnosis decisions? An investigation into physicians' decision-making process with artificial intelligence | 2021 | Information Systems Research |
| #54 | Cognitive Challenges in Human-Artificial Intelligence Collaboration: Investigating the Path Toward Productive Delegation | 2022 | Information Systems Research |
| #10 | OVERCOMING BREAKDOWNS IN CUSTOMER-CHATBOT INTERACTION: DESIGN AND IMPACT OF COLLABORATIVE REPAIR STRATEGIES | 2026 | MIS Quarterly: Management Information Systems |
| #156 | Can humans detect errors in data? impact of base rates, incentives, and goals | 1997 | MIS Quarterly: Management Information Systems |
| #159 | Inducing sensitivity to deception in order to improve decision making performance: A field study | 2002 | MIS Quarterly: Management Information Systems |
| #175 | A Theory of Decision Support System Design for User Calibration | 1996 | Information Systems Research |
| #198 | The use of information in decision making: An experimental investigation of the impact of computer-based decision aids | 1992 | MIS Quarterly: Management Information Systems |
| #30 | THE FOG OF WARNINGS: HOW NON-SECURITY-RELATED NOTIFICATIONS DIMINISH THE EFFICACY OF SECURITY WARNINGS | 2025 | MIS Quarterly: Management Information Systems |
| #117 | Awareness displays and social motivation for coordinating communication | 2008 | Information Systems Research |
| #142 | Cognitive Support for Real-Time Dynamic Decision Making | 2001 | Information Systems Research |

## 文献迁移链条

### #184 Why Is Programming (Sometimes) so Difficult? Programming as Scientific Discovery in Multiple Problem Spaces (1997, Information Systems Research)

原文摘要主要讲什么：

这篇文章把编程看作在多个问题空间中的搜索和发现活动。它区分了规则空间、实例空间和表征空间。程序员会在规则空间中形成假设，在实例空间中测试这些假设，并在任务变困难或出现替代表征时改变自己的问题表征。文章通过新程序编写、理解既有程序、复用旧程序三个实证研究说明，编程困难很大一部分来自程序员需要在多个表征之间切换。

它给我们的原始概念：

- 编程不是简单输入代码，而是持续形成、测试和调整心理表征。
- 程序员需要把规则、实例和表征空间整合起来。
- 表征转换本身是认知困难来源。

为什么不能直接照搬：

这篇文章默认程序员自己在推进编程过程。即使使用工具，程序员仍然是主要的问题空间搜索者和表征更新者。coding agent 改变了这个前提：agent 可以先行生成实现、修改多处代码、运行测试并继续修复。也就是说，代码状态可能已经被 agent 推进，但开发者自己的问题表征并没有同步经历同样的搜索和转换过程。

迁移到 coding agent 后的新问题：

过去的问题是“程序员在多个问题空间中转换表征为什么困难”；现在的问题是“agent 已经推进了代码实现，但开发者的表征空间是否跟得上”。这正是代理性代码状态脱节感的核心。

对新构念的贡献：

#184 提供了最重要的认知基础：我们为什么可以把“跟不上代码状态”视为一个构念。因为编程的核心不是只看最终代码，而是形成对代码状态、实现路径和问题空间的心理表征。coding agent 的独特之处在于，它可能让最终代码状态先于开发者表征形成。

### #45 The Unknowability of Autonomous Tools and the Liminal Experience of Their Use (2021, Information Systems Research)

原文摘要主要讲什么：

这篇文章研究半导体设计师使用传统设计工具和自主设计工具时的体验差异。传统工具中，人类设计师大体知道输入会产生什么输出；自主工具则能独立学习和执行新行动，其输入-输出关系在人类看来事前和事后都难以完全知道。研究发现，使用自主工具时，设计师会经历一种阈限状态：互动充满模糊性、持续涌现，并沿着多条设计轨迹推进。

它给我们的原始概念：

- 自主工具的输入-输出关系可能不可知。
- 用户体验会从确定的工具使用转向模糊、涌现、多轨迹的阈限体验。
- 自主工具挑战了既有人类-技术能动性理论。

为什么不能直接照搬：

这篇文章讲的是 autonomous tools 的不可知性和阈限体验，重点在设计工具输出的不可预测和用户体验的 liminal 状态。coding agent 的场景更具体也更强：agent 不只是产生不可知输出，而是在真实代码库中持续行动，形成新的代码库状态。开发者的困难不只是“输出不可知”，而是“当前工作区已经变了，我是否还知道代码库处于什么状态”。

迁移到 coding agent 后的新问题：

自主工具文献能解释为什么用户会感到模糊和涌现，但不能充分解释代码库状态变化带来的表征落后。coding agent 的关键不是单次输出不可知，而是连续行动后造成的 state drift。

对新构念的贡献：

#45 支持我们把 agentic coding 视为自主工具使用的强版本；但新构念把焦点从“不可知性体验”进一步收紧到“开发者心理表征与 agent 推进后的代码库状态之间的脱节”。

### #51 The next generation of research on is use: A theoretical framework of delegation to and from agentic is artifacts (2021, MIS Quarterly)

原文摘要主要讲什么：

这篇文章指出传统 IS use 理论把信息系统当作被动工具，强调人类能动性。但新一代 agentic IS artifacts 不再只是等待人类使用，它们可以主动行动、在不确定要求下承担任务、追求结果。因此作者提出用 delegation 作为理解人和 agentic IS artifact 关系的基础框架，并强调 agent 属性和委托机制，如评估、分配和协调。

它给我们的原始概念：

- IS artifact 从被动工具变成 agentic artifact。
- 人和系统的关系需要从 use 转向 delegation。
- agent 可以主动承担任务和追求结果。

为什么不能直接照搬：

这篇文章很好地解释了为什么 coding agent 不是普通工具，而是可被委托的 agentic artifact。但 delegation 框架主要解释任务如何分配、协调和评估，并不直接描述 agent 执行任务之后，工作对象状态如何变化，以及人类是否还保持对该状态的心理表征。

迁移到 coding agent 后的新问题：

coding agent 的委托不是停在“任务交给 agent”。委托之后，agent 会改变代码库。开发者需要面对一个被代理推进后的 codebase state。旧 delegation 理论可以解释为什么任务被交出去，却不能解释为什么开发者在 agent 做完后需要重新追上代码状态。

对新构念的贡献：

#51 提供 agentic artifact 的理论入口；代理性代码状态脱节感则补上 delegation 后的认知后果：当 agentic artifact 真正行动并改变工件时，人类是否仍与工件状态同步。

### #53 Augmenting medical diagnosis decisions? An investigation into physicians' decision-making process with artificial intelligence (2021, Information Systems Research)

原文摘要主要讲什么：

这篇文章研究医生使用 AI 辅助诊断时如何评价 AI 建议。相比规则系统，AI 系统不透明、错误更难预测，因此用户更难判断建议正确性以及是否接受或拒绝。作者通过 think-aloud、访谈和问卷识别医生的决策模式，并提出 AI 建议评估中的元认知过程：医生需要监控自己的推理，也要监控系统建议；元认知不足会导致错误决策。

它给我们的原始概念：

- AI 建议的不透明和错误不可预测带来认知挑战。
- 用户需要自我监控和系统监控。
- 接受或拒绝 AI 建议不仅是信任问题，也是元认知问题。

为什么不能直接照搬：

医疗诊断 AI 提供的是建议，医生决定接受或拒绝；建议不会自动改写一个持续维护的工件。coding agent 则会把建议落实为文件修改、命令执行和代码状态变化。开发者不是单纯评估“这个建议对不对”，而是要理解“agent 已经把代码库改成了什么状态，以及我是否还能追踪它”。

迁移到 coding agent 后的新问题：

元认知监控在 coding agent 中不只是 self-monitoring 和 system-monitoring，还包括 state-monitoring：开发者要监控 agent 行动后的代码状态是否仍在自己的心理模型中。

对新构念的贡献：

#53 说明 AI 辅助决策中需要监控系统和自己；代理性代码状态脱节感则进一步指出，在 agentic programming 中还需要监控代码库状态与开发者心理表征之间是否同步。

### #54 Cognitive Challenges in Human-Artificial Intelligence Collaboration: Investigating the Path Toward Productive Delegation (2022, Information Systems Research)

原文摘要主要讲什么：

这篇文章研究人在分类任务中如何向 AI 委托任务。结果显示，人和 AI 合作可能超过单独 AI，但这种提升主要发生在 AI 把任务委托给人时；人把任务委托给 AI 时表现不好。原因不是算法厌恶，参与者甚至欣赏 AI 支持，而是缺乏 metaknowledge：他们不能正确评估自己和 AI 的能力，因此做出糟糕委托。

它给我们的原始概念：

- 人类委托 AI 的失败不一定来自不信任，而可能来自缺乏元知识。
- productive delegation 需要知道自己和 AI 分别擅长什么。
- 算法欣赏也不能保证良好委托。

为什么不能直接照搬：

分类任务的委托对象是相对离散的 task item；coding agent 委托的是嵌入代码库、可能跨步骤推进的开发任务。即使开发者知道 agent 大体擅长什么，也可能在 agent 连续修改后跟不上代码状态。元知识解释“该不该委托”，但不能完全解释“委托后代码状态是否仍可被人类追踪”。

迁移到 coding agent 后的新问题：

coding agent 中的委托元知识需要扩展为状态跟踪能力：不仅知道 agent 适合做什么，还要知道 agent 做完后代码库处于什么状态、偏离从哪里发生、哪些风险点需要检查。

对新构念的贡献：

#54 支持我们把问题从 trust 转向能力判断；代理性代码状态脱节感进一步说明，即使委托发生了，关键 UX 问题可能出现在 agent 行动后的状态理解阶段。

### #10 OVERCOMING BREAKDOWNS IN CUSTOMER-CHATBOT INTERACTION: DESIGN AND IMPACT OF COLLABORATIVE REPAIR STRATEGIES (2026, MIS Quarterly)

原文摘要主要讲什么：

这篇文章研究客户服务 chatbot 的交互 breakdown。传统上，breakdown 的修复负担往往落在用户或 chatbot 单方身上，使交互变成挫败的猜谜游戏。作者设计并实验评估了 customer 和 chatbot 共同修复 breakdown 的策略，发现协同修复可以提高问题解决率，并缓解 breakdown 对客户结果的负面影响。

它给我们的原始概念：

- breakdown 是人机交互中的常见失败。
- 修复不应只由一方承担，可以设计为协作过程。
- repair strategy 会影响失败后的用户结果。

为什么不能直接照搬：

chatbot breakdown 主要是会话理解失败；coding agent breakdown 常常表现为代码状态偏移。agent 可能已经改错文件、引入回归、选择错误实现路径或在多步修复中越走越远。此时用户首先要做的不是重新表达一句话，而是恢复对代码库状态和行动轨迹的理解。

迁移到 coding agent 后的新问题：

coding agent 的 repair 需要先解决 state re-alignment：开发者要知道当前代码状态是什么、哪里偏离、能否回滚、如何继续。这比对话修复更复杂，因为错误已经沉淀进代码工件。

对新构念的贡献：

#10 支持“失败后的协同修复”是重要人机交互议题；代理性代码状态脱节感解释了 coding agent 中 repair 为什么更难：修复对象不是对话，而是被 agent 改变后的代码状态。

### #156 Can humans detect errors in data? impact of base rates, incentives, and goals (1997, MIS Quarterly)

原文摘要主要讲什么：

这篇文章挑战“人类通常不善于发现数据错误”的观点。作者基于信号检测理论、任务绩效理论、努力-准确性决策理论以及目标和激励理论，提出并实验检验错误检测命题。结果显示，明确的错误检测目标和激励能够改善错误检测表现。

它给我们的原始概念：

- 错误检测不是固定能力，而受目标、激励和任务条件影响。
- 检测行为可以通过设计和管理条件改变。
- 错误检测与努力、准确性和信号识别有关。

为什么不能直接照搬：

数据错误检测面对的是较稳定的数据项；coding agent 生成的错误可能隐藏在跨文件变更、架构假设、边界条件、测试缺口和未来维护风险中。更重要的是，开发者是否能检测错误取决于他是否先理解当前代码状态。如果已经产生状态脱节，错误检测会从“找错”变成“先重新建立代码状态模型”。

迁移到 coding agent 后的新问题：

错误检测理论可解释检测绩效，但 coding agent 场景需要加入前置条件：开发者是否与代码库状态同步。状态脱节可能是错误检测失败的重要前因。

对新构念的贡献：

#156 支持后果侧：代理性代码状态脱节感应当影响 bug 发现率、误报、验证时间和验证努力。

### #159 Inducing sensitivity to deception in order to improve decision making performance: A field study (2002, MIS Quarterly)

原文摘要主要讲什么：

这篇文章研究如何诱导专业人员对数据操纵或欺骗保持敏感。结果发现，数据质量警告能提高检测成功率；警告加即时培训能进一步提高检测成功率，但会增加误报。检测成功率提升会提高任务准确性并增加解题时间；误报增加则降低准确性。

它给我们的原始概念：

- 提高警觉性有收益，也有误报成本。
- 警告和即时训练会改变检测行为。
- 检测成功、误报、任务准确性和时间之间存在权衡。

为什么不能直接照搬：

coding agent 中的问题不只是对“欺骗/错误”更敏感。开发者可能不知道该在哪里敏感：风险位置本身可能因为 agent 多步修改而不清楚。如果开发者跟不上代码状态，警告可能增加焦虑和误报，但未必帮助定位真正风险。

迁移到 coding agent 后的新问题：

在 agentic coding 中，警觉性必须建立在状态理解上。没有状态同步，更多警告可能只会造成审查疲劳或误报。

对新构念的贡献：

#159 帮助我们预测状态脱节的后果：高脱节可能导致两种坏结果，要么漏掉关键 bug，要么到处怀疑、误报增加、review 时间上升。

### #175 A Theory of Decision Support System Design for User Calibration (1996, Information Systems Research)

原文摘要主要讲什么：

这篇文章提出 DSS 用户校准设计理论，目标是让用户对决策的信心与决策质量匹配。它整合校准、决策和 DSS 文献，提出系统需要具备 expressiveness、visibility、inquirability 等属性，以支持用户达到更好的校准。

它给我们的原始概念：

- 好的系统设计应帮助用户信心与结果质量相匹配。
- 可见性、表达性、可询问性是支持校准的重要属性。
- 用户校准是设计问题，不只是个人偏差。

为什么不能直接照搬：

coding agent 的校准对象不是单个决策信心，而是对当前代码库状态的理解是否匹配真实状态。开发者可能对 agent 产物很有信心，却没有真正理解代码状态；也可能没有信心但其实状态很清楚。因此需要从 confidence-quality calibration 扩展到 representation-state calibration。

迁移到 coding agent 后的新问题：

开发者需要校准的不是“我这个决策质量如何”，而是“我以为代码库处于什么状态”和“代码库实际处于什么状态”之间的匹配。

对新构念的贡献：

#175 提供设计启发：行动轨迹可见性、可询问性、状态摘要、风险定位可能降低代理性代码状态脱节感。

### #198 The use of information in decision making: An experimental investigation of the impact of computer-based decision aids (1992, MIS Quarterly)

原文摘要主要讲什么：

这篇文章质疑“决策支持系统会让用户处理更多信息并提升决策质量”的传统假设。基于行为决策理论，作者认为用户可能更重视节省努力而不是提高决策质量。实验结果显示，使用决策辅助的被试并没有比不用辅助者使用更多信息；总体上，被试表现出努力最小化倾向。

它给我们的原始概念：

- 工具支持可能带来努力节省，而不是质量提升。
- 用户会在准确性和努力之间做权衡。
- DSS 效果取决于用户如何实际使用信息。

为什么不能直接照搬：

coding agent 更容易诱发努力节省：代码已经生成了，测试可能也跑了，开发者有动机快速接受。但如果开发者没有经历实现路径和状态变化，他节省的可能正是建立代码状态表征的努力。

迁移到 coding agent 后的新问题：

努力节省在这里不只是“少看信息”，而是“跳过对 agent 推进后代码状态的重新建模”。这会提高状态脱节感，并影响 review 和 merge。

对新构念的贡献：

#198 帮助解释为什么代理性代码状态脱节感可能在高自动化工具中被放大：agent 让产物更快出现，也让用户更容易跳过理解过程。

### #30 THE FOG OF WARNINGS: HOW NON-SECURITY-RELATED NOTIFICATIONS DIMINISH THE EFFICACY OF SECURITY WARNINGS (2025, MIS Quarterly)

原文摘要主要讲什么：

这篇文章研究用户为什么忽视安全警告。它提出并验证“习惯化泛化”：用户习惯忽视普通通知后，会把这种习惯迁移到安全警告，即使他们意识上能区分两者。实验显示，通过视觉或交互方式区分警告和普通通知，可以缓解这种泛化。

它给我们的原始概念：

- 高频低价值通知会让用户对重要警告也习惯性忽视。
- 警告设计需要避免和普通通知混同。
- 注意力和警觉性会被界面模式塑造。

为什么不能直接照搬：

coding agent 中的提示不是普通安全警告，而是状态同步和监督节点：agent 请求权限、报告测试失败、提醒风险、要求确认实现方向。若这些提示泛滥，开发者可能忽略真正能帮助他同步代码状态的关键信息。

迁移到 coding agent 后的新问题：

警告习惯化不是最终概念，而是代理性代码状态脱节感的前因之一：如果 agent 的状态提示和审批请求设计不当，开发者会错过关键状态变化，导致更高脱节。

对新构念的贡献：

#30 支持设计前因：提示分级、风险突出、低价值通知过滤等设计可以影响开发者是否跟得上 agent 推进的代码状态。

### #117 Awareness displays and social motivation for coordinating communication (2008, Information Systems Research)

原文摘要主要讲什么：

这篇文章研究 awareness displays 如何帮助远程协作者协调沟通时机。实验发现，展示远程协作者工作负载的信息可以减少打断，但效果取决于沟通者是否有动机关心对方；高信息量 display 会损害查看者任务绩效，而抽象的负载显示更合适，因为它支持更好时机而不过载。

它给我们的原始概念：

- 状态显示可以支持协作协调。
- 信息越多不一定越好，抽象状态显示可能更有效。
- awareness display 影响打断时机和任务负荷。

为什么不能直接照搬：

原文关注人与人之间的沟通协调；coding agent 中需要协调的是人和代理行动，以及开发者对代码状态的同步。显示更多 agent 细节不一定降低脱节，可能反而增加负荷；关键是提供恰当抽象层次的代码状态和 agent 行动摘要。

迁移到 coding agent 后的新问题：

我们需要的不是一般 awareness，而是 codebase state awareness：开发者是否知道 agent 已经把代码库推进到哪里、下一步风险在哪里、哪些变化需要人类注意。

对新构念的贡献：

#117 提供重要设计启发：降低状态脱节不等于把所有 agent 行动细节都展示出来，而是要找到合适的信息抽象层次。

### #142 Cognitive Support for Real-Time Dynamic Decision Making (2001, Information Systems Research)

原文摘要主要讲什么：

这篇文章研究实时动态任务中决策者如何分配注意力资源。动态决策包含两个重叠活动：监控关键系统变量，以及生成、评估、选择行动。二者竞争同一注意力资源。研究发现，某些认知支持不但不提升表现，反而可能降低表现，说明实时动态决策支持设计非常困难，需要理解底层认知过程。

它给我们的原始概念：

- 动态任务中监控和控制会竞争注意力。
- 更多认知支持不一定更好。
- 实时决策支持必须理解用户如何监控系统状态。

为什么不能直接照搬：

coding agent 使用具有动态性：开发者既要自己思考实现，又要监控 agent 的行动和代码状态。传统动态决策研究关注系统变量；coding agent 中的关键变量是代码库状态、agent 行动轨迹、任务目标和风险位置。

迁移到 coding agent 后的新问题：

开发者需要在“直接编码/思考”和“监控 agent 推进代码状态”之间分配注意力。状态脱节可能正是监控资源不足或支持设计不当的结果。

对新构念的贡献：

#142 支持机制侧：代理性代码状态脱节感可能来自监控与控制注意力竞争；它也提示，简单增加提示和解释不一定有用，可能加重负担。

## 汇总：为什么这些文献支持发展新概念

这些文献共同给出三条逻辑：

1. 编程本身依赖开发者对问题空间和代码状态的心理表征（#184）。
2. 自主/代理性工具会主动推进任务，并使输入-输出和行动轨迹变得更难完全预知（#45, #51）。
3. AI 辅助和决策支持文献说明，用户需要监控、校准、检测错误、管理注意力和避免努力节省，但这些文献多处理建议、数据或一般系统状态，而不是 agent 连续改变真实代码库后的 codebase state（#53, #54, #156, #159, #175, #198, #30, #117, #142）。

因此，coding agent 情境要求我们把焦点从：

- 是否信任 AI；
- 是否愿意委托 AI；
- AI 是否解释清楚；
- 用户是否能检测错误；
- 用户是否被打断；

推进到一个更具体的新问题：

开发者的心理表征是否仍然跟得上由 agent 推进后的代码库状态。

这就是“代理性代码状态脱节感”作为新构念的理论空间。
