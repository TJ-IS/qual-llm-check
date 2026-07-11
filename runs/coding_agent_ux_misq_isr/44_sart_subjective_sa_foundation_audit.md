# SART 主观态势觉察基础审计：作为 Coding Agent 概念开发的唯一理论起点

## 1. 审计目的

此前关于 coding agent 的 SA 讨论以 Endsley 的三层模型和 SAGAT 为主要叙述入口。这条路线能够清楚说明“真实 SA”如何用任务真值检验，却容易把 coding agent 用户体验误写为一个视觉显示或界面信息呈现问题。用户的实际困难不只在于是否看见信息，也在于：在一个由 agent、代码、命令、测试、任务约束和责任边界共同组成的复杂协作任务中，用户主观上是否感到自己仍知道、理解并能预期那些会影响安全、有效任务完成的事情。

因此，后续 thesis 应把 **Taylor 对主观 situation awareness 的建构及其 SART（Situational Awareness Rating Technique）原始研究**作为唯一的概念发展起点。SART 不是第二个与 SA 并列的理论，而是 Taylor 对“人如何主观地估计自己在动态、监督式任务中的 SA”所作的原始操作化工作。Endsley 的三层 SA、SAGAT 和后来的测量比较文献保留为**校准与效度文献**：它们帮助我们避免把主观觉察误写为与任务真值完全一致的客观 SA；它们不再作为 coding agent 概念定义的主导话语。

本审计回答五个问题：

1. Taylor 的原始 SART 文献究竟从什么问题出发、如何定义 SA？
2. SART 的构成、版本和计算方式有哪些容易被误写的地方？
3. 为什么 SART 比以视觉 display 为中心的 SA 测量更适合作为 coding agent UX 概念开发的起点？
4. 什么内容可以迁移，什么内容不能直接迁移？
5. 这会如何改变 thesis 的概念定义、Reddit 编码和量表开发设计？

## 2. 原始文献与证据等级

| 证据 | 文献 | 在本研究中的作用 | 证据等级 |
| --- | --- | --- | --- |
| SART 原始工作 | Taylor (1990), *Situational Awareness Rating Technique (SART): The Development of a Tool for Aircrew Systems Design*, AGARD-CP-478, pp. 3/1-3/17 | 主观 SA 的概念起点、构念引出方法、SART 的来源 | 核心 |
| SART 应用评价 | Selcon & Taylor (1990), *Evaluation of the SART as a Tool for Aircrew Systems Design*, AGARD-CP-478, pp. 5/1-5/8 | 说明 SART 的设计评价用途 | 核心补充 |
| 主客观比较 | Endsley et al. (1998), *A Comparative Analysis of SAGAT and SART for Evaluations of Situation Awareness* | 区分 SART 的主观 SA 与任务真值意义的 SA | 核心校准 |
| 方法综述 | Salmon et al. (2006), *Situation Awareness Measurement: A Review of Applicability for C4i Environments* | 说明复杂人 - 技术系统中单一 SA 测量法不足，推荐多方法 | 核心校准 |
| SART 量表单 | 本地 `source_pdfs_sa/sart_scale_notes.pdf` | 提供常见简化 SART 题项的直接例证 | 辅助；不可替代原始文献 |

### 2.1 Taylor (1990) 的原始问题不是“让人看见更多视觉信息”

Taylor 的工作产生于航空系统自动化改变空勤人员角色的背景。传统人因工程常把问题表述为降低或管理 operator workload；但自动化使人从持续操纵者变成需要在不确定条件下适应、判断和决策的监督者。原始研究关心的不是某一显示器是否更清晰，而是：**空勤人员自己如何理解 situation awareness，以及能否把这种主观理解变成用于系统设计的测量工具。**

可访问的原始工作再版摘要显示，Taylor 的研究采用三阶段知识引出程序：scenario generation、construct elicitation 和 construct structure validation。研究团队用固定协议的半结构访谈和 Personal Construct/Repertory Grid Technique，与 84 名 Test and Operational Royal Air Force aircrew 共同引出与 SA 有关的情境和个人构念，并对构念/情境评分进行主成分分析和 varimax rotation。这个程序的重要性远大于它最后得到的量表条目：SART 的起点是任务参与者对“何时我觉得自己知道局面”的解释，不是研究者预设一组视觉特征。

Taylor 对 SA 的表述可概括为：

> **SA 是对影响任务安全、迅速和有效执行的事件、因素与变量的知识、认知和预期。**

这一定义有四个对 coding agent 至关重要的特征。

第一，它以**任务后果**界定相关性。不是所有信息都要被知道，只有会影响安全、迅速和有效完成任务的事件、因素与变量才是 SA 内容。第二，它包含 knowledge、cognition 和 anticipation，因而不是单纯“看见”或“记住”状态。第三，它是由任务参与者主观报告的 state estimation，允许研究者研究人在复杂情境中对自己是否“掌握局面”的体验。第四，它发生在自动化改变人类角色的监督式工作中，与 coding agent 的用户位置具有结构上的相似性。

### 2.2 SART 的版本差异必须在 thesis 中如实处理

关于 SART，最常见但不严谨的写法是简单说“它有 10 个七点题项”。这句话无法准确对应所有版本。

Endsley et al.（1998）在直接比较 SART 与 SAGAT 的研究中，将 SART 说明为一个基于 operator 主观意见的 SA 测量；该版本包含 14 个与 SA 相关的组成，要求操作者在双极量表上判断三类内容：对资源的 demand、对资源的 supply、以及对 situation 的 understanding。后续的常用简化表单常把 10 个具体元素归入三个高阶部分：

| SART 高阶部分 | 常见具体元素 | 在原航空语境中的含义 |
| --- | --- | --- |
| Attentional demand | instability、complexity、variability | 情境变化与相互关联程度对注意力造成的需求 |
| Attentional supply | arousal、concentration、division of attention、spare mental capacity | 操作者可动用和分配的注意资源 |
| Understanding | information quantity、information quality、familiarity | 操作者得到并理解信息、以及对情境的熟悉程度 |

一些版本还纳入三个高阶部分的全局判断和/或一个整体 SA judgement；这解释了文献中 10、13 与 14 个组成并存的现象。本地 `sart_scale_notes.pdf` 是一个两页、九个具体题项的教学表单，其中没有 information quality，因此不能被当作 Taylor 原始量表的完整权威版本。正式 thesis 必须做到：

- 不把“十题版”称作所有 SART 版本的原始形式；
- 在方法章节说明采用的是哪一版、保留了哪些元素、为什么；
- 不把 SART 的计算公式误当作 SA 的概念定义；
- 任何改写后的 coding-agent 项目都应被称为新开发量表，而不是“直接使用 SART”。

常见的 SART 评分约定是：

> **Subjective SA = Understanding - (Attentional Demand - Attentional Supply)**

这个公式具有直观吸引力：理解增加主观 SA，任务需求相对可用注意资源越高，主观 SA 越低。但它也暴露一个理论风险：SART 将主观理解、任务负荷和注意资源放在同一计算结构里。这种做法适合系统设计评价，却不能自动说明这三者是同一潜变量的不可分割组成。对 coding agent 来说，agent 自主性、代码复杂度和审批频率很可能先改变 attentional demand/supply，再影响用户对情境的理解与预测；因此这些内容未必都属于新构念的内涵。

## 3. SART 与视觉型 SA 测量的关键差异

### 3.1 SART 的对象是人的主观情境估计，而不是 display 本身

SART 通常在任务或试验后填写。它不要求研究者事先穷举所有“正确的”环境元素，也不要求受试者透过一个视觉仪表盘完成特定搜索。它问的是操作者如何评价当时的情境不稳定性、复杂性、注意资源和理解程度。因此，它可用于真实工作、模拟任务和不同领域的设计比较。Endsley et al.（1998）也明确将它描述为 operator subjective opinion-based measure。

这与 coding agent 更相称。coding-agent task 的关键信息不集中在单一界面，也不主要是视觉空间对象。它散布在自然语言需求、agent 的计划与消息、终端命令、文件树、diff、测试、依赖、错误输出、Git history、权限请求和用户自己的架构知识中。即使所有信息以文本或 GUI 形式出现，真正困难仍是用户能否把它们组织成“对完成当前任务最重要的事件、因素和变量”的认识。SART 的主观、任务导向、注意资源取向更贴近这一问题。

### 3.2 但 SART 不等于 coding-agent-specific 构念

SART 的优势不意味着可以直接把 aircraft 换成 agent。其具体组成来自空勤任务与空勤人员构念。coding agent 情境至少带来五项需要重新开发的差异：

1. **情境元素异质且可执行。** 空勤任务中的威胁、航迹和平台状态，与代码制品、命令、测试、配置和 agent 行动不同；后者会直接改变可执行系统。
2. **用户面对的是非人类协作行动者。** agent 不只是信息显示或自动控制模块，它会选择、修订和继续行动。用户必须理解的既是代码状态，也是 agent 当前行动和可能的下一步。
3. **责任与授权是事件驱动的。** 用户会在权限请求、diff 审查、测试失败、计划变化和异步完成通知等节点作出继续、拒绝、纠偏或接管的判断。
4. **可逆性不等于低风险。** Git 回滚、测试和 sandbox 可能降低风险，却不能保证用户理解改动的架构、依赖、数据或安全后果。
5. **注意资源可能是前因而非内容。** 在 agent task 中，审批负荷、日志冗余和多任务切换可能影响主观 SA；但把它们直接并入构念，会掩盖“工作状态证据支持如何降低负荷并提高理解”的机制。

因此，后续要开发的不是“Coding-Agent SART”。更准确的表述是：

> 本研究以 Taylor（1990）所建构的、面向复杂自动化监督任务的主观 situation awareness 为唯一概念起点；通过 coding agent 用户叙述重新识别那些影响用户安全、迅速、有效完成任务的事件、因素和变量；再根据经验结构决定哪些属于 coding-agent subjective SA，哪些应被定位为其前因或后果。

## 4. 主观 SA 与客观 SA：为什么两个都需要，但地位不同

### 4.1 1998 年直接比较的结论

Endsley et al.（1998）在飞行模拟 display evaluation 中同时使用 SART 和 SAGAT。两种方法对显示设计变化都表现出一定敏感性，却没有彼此相关。SART 与简单主观 SA、SA 充分性、confidence 和主观 performance 高度相关；SAGAT 则通过冻结时对具体任务情境的查询、并与当时 simulation 真值对照，显示一些与 SART 不同甚至相反的 SA 变化。例如，参与者可能觉得 display 提高了理解，却在某些 threat location 或 future projection 问题上表现更差。

该结果不能被简化为“SART 无效”。它说明 SART 测量的是用户对自己情境掌握的主观估计，这个估计会影响用户选择谨慎还是大胆地行动，但它不保证用户客观上知道自己遗漏了什么。对 coding agent 来说，恰恰需要保留这个区分：用户觉得“我已经懂了、可以批准”本身具有 UX 和行为意义；但是研究不能据此断言用户真的知道 agent 改了哪些关键文件、测试是否覆盖限制，或批准后有什么风险。

### 4.2 对 coding agent 研究的测量定位

基于 Taylor 的 SART 传统，拟开发的主观构念应暂称为：

> **编码代理任务主观态势觉察**（provisional English label: *perceived coding-agent task situation awareness*）。

它是用户在一个具体 agent task episode 后，对自己是否拥有完成该任务所需的相关知识、认知和预期的主观判断程度。其高低是连续的，而不是 0/1 分类：用户可以在某些状态内容上高度觉察、在另一些上很低；总分是否合理、是否存在多个维度，须由后续数据决定。

客观任务真值的测量不用于重新定义主观构念，而用于提供三类效度证据：

1. **校准证据：** 高主观 SA 是否通常伴随更准确的任务状态判断；何种情况下两者脱节？
2. **诊断证据：** 用户主观上觉得“掌握了”却漏掉了什么；是 action state、change impact 还是 future consequence？
3. **行为效标：** 主客观 SA 的组合是否比任一单独指标更好预测审批准确、及时接管和过度依赖？

Salmon et al.（2006）对 17 种 SA 测量方法的回顾也得出相似方法论结论：在复杂的人 - 技术系统中，没有一种通用技术可以充分测量所有 SA 方面，多方法组合更可取。coding agent 的研究因而不应在“自评”与“客观探针”之间二选一，而应清楚指定各自测什么。

## 5. 对 thesis 概念定义的直接改写

旧定义把 CAWSA 表述为用户对 agent 行动、代码状态、工具结果、任务约束和后续风险进行感知、理解和预测的程度。该定义过度贴近 Endsley 的三层叙事，也让主观测量与客观状态混在一起。依据 Taylor/SART，建议把 thesis 中的工作定义改为：

> **编码代理任务主观态势觉察，是指用户在一次具体 coding-agent 编程任务中，对自己是否拥有安全、迅速且有效地界定、监督和完成该任务所需的、关于相关 agent 行动、代码制品变化、工具执行结果、任务约束及后续影响的知识、认知和预期的主观判断程度。**

这个定义有意保留五项内容：

- **主观判断：** 对应 SART 的直接理论起点；
- **具体任务：** 避免写成稳定人格、泛化熟悉度或普遍 AI 态度；
- **安全、迅速、有效完成任务：** 继承 Taylor 的任务相关性判准，而不是追求知道一切；
- **界定、监督和完成：** 表达 coding agent 中用户并非纯操作者，而是委托与残余责任承担者；
- **知识、认知和预期：** 继承 Taylor 的核心，而不先把它等同于固定三维度。

它不包括：agent 的真实能力、用户对 agent 的信任、用户拥有的控制权限、界面是否透明、用户一般编码能力、客观正确性或最终任务绩效。它们分别可以是前因、后果、替代解释或客观效标。

## 6. 对 Reddit 二手数据概念开发的直接改写

Taylor 的原始构念引出程序和 Chen et al.（2024）的二手评论编码可以形成一个更严格的组合。两者共同点是：先从使用者叙述中发现“什么让他们觉得自己掌握或没有掌握任务”，再以理论整理，而不是由研究者先决定量表结构。差异在于，Taylor 使用访谈与 repertory grid；本研究使用公开二手文本，因而必须补足情境、反例和编码审计。

建议的编码问题应从原来的“用户是否感知、理解、预测”改为更贴近 Taylor 的问法：

1. 在该任务片段中，用户认为哪些 agent 行动、代码变化、执行结果、约束或后续影响会决定任务能否安全、迅速、有效完成？
2. 用户在哪些时刻明确表示自己“知道、理解、能预期、能判断”或相反地“不知道、看不懂、无法判断、不敢继续”？
3. 用户把这种主观掌握或缺失归因于什么：状态证据、任务复杂性、agent 自主性、经验、信任、界面、审批要求还是其他因素？
4. 用户在主观掌握不足时做了什么：检查、询问、限制权限、运行测试、拒绝、接管、回滚、放弃或盲目批准？
5. 哪些表达应归入主观 SA，哪些仅仅是对 agent 的喜欢、信任、控制资源、工作量或性能评价？

选择性编码时，Taylor 的 demand-supply-understanding 不是预设维度，而是三个检查视角：用户是否描述了任务需求与变化；用户是否描述了注意资源、信息处理和交互负担；用户是否描述了对相关状态的理解和预期。若 coding agent 数据显示某些范畴是必需的，例如“对 agent 行动边界的预期”，研究者应说明它为何是 SART 核心在新情境的扩展；若某些范畴如一般任务负荷只影响理解而不构成主观 SA，则应把它放在前因位置。

## 7. 对量表开发的直接改写

量表开发必须模仿 SART 的逻辑，不是其表面措辞。

1. **构念引出。** 用 Reddit 编码识别用户自发的任务相关构念；必要时再以访谈补充缺失的负例或沉默体验。
2. **结构验证。** 以独立样本的 Q-sort、认知访谈和探索性因子分析检查这些构念是否能够稳定区分，并与 Taylor 的 demand/supply/understanding 进行理论比较。
3. **题项开发。** 题项必须使用 task episode 锚定语句，如“在刚才的任务中”，并测量用户的主观掌握，而不是问界面有没有某个功能。
4. **多方法校准。** 与 CA-SAGAT 式任务真值探针、审批/接管行为和相邻构念量表共同收集，判断主观 SA 的校准程度和增量解释力。
5. **版本透明。** 无论最终是否借用 SART 的任何维度或公式，都必须在论文中明确：本量表由 coding agent 用户经验和 Taylor 的主观 SA 起点发展而来，不能宣称是原 SART 的简单改写或跨情境直接验证。

## 8. 结论：新的 thesis 写作定位

后续 thesis 应采用如下叙事主线：

> Coding agent 并不首先提出一个“看得见多少”的视觉界面问题，而提出一个复杂自动化监督问题：用户在把任务交给会行动的 agent 后，是否仍主观地认为自己掌握了安全、迅速、有效完成任务所需的关键事件、因素与变量。Taylor 的 SART 是对这一主观 SA 问题最适合的原始理论和方法起点。coding agent 的独特性在于，关键情境不再是飞行环境，而是 agent 行动、可执行代码制品、工具结果、任务约束与后续影响的耦合；因而 SART 必须通过用户叙述重新发展，而不能直接翻译。Endsley/SAGAT 则用于揭示主观掌握与任务真值何时一致、何时脱节。

## 9. 参考文献与原始链接

- Taylor, R. M. (1990). *Situational awareness rating technique (SART): The development of a tool for aircrew systems design*. In *Situational Awareness in Aerospace Operations* (AGARD-CP-478, pp. 3/1-3/17). NATO Advisory Group for Aerospace Research and Development. Bibliographic record: https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=200902086278278429
- Selcon, S. J., & Taylor, R. M. (1990). Evaluation of the situational awareness rating technique (SART) as a tool for aircrew systems design. In *Situational Awareness in Aerospace Operations* (AGARD-CP-478, pp. 5/1-5/8). NATO AGARD.
- Endsley, M. R., Selcon, S. J., Hardiman, T. D., & Croft, D. G. (1998). A comparative analysis of SAGAT and SART for evaluations of situation awareness. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 42*(1), 82-86. https://doi.org/10.1177/154193129804200119
- Salmon, P., Stanton, N., Walker, G., & Green, D. (2006). *Situation awareness measurement: A review of applicability for C4i environments*. Brunel University. Local source: `source_pdfs_sa/salmon_2006_sa_measurement_review.pdf`.
