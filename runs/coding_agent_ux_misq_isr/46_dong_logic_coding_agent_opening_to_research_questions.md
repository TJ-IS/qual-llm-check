# 编码代理任务主观态势觉察研究：绪论开篇至研究问题

> 写作状态：用于讨论的第一轮严格仿写稿。正文仅覆盖 Dong 论文第 1.1 节的功能范围，即“选题背景与问题提出”至研究问题；概念定义、研究意义、文献综述和概念开发暂不展开。
>
> 仿写原则：逐段对应 Dong 的论证功能、证据功能和问题推进方式，但不复制其原文措辞，也不强行保留仅适用于社会化商务的市场收入图、交易关系变量和多主体商业逻辑。

## 第 1 章 绪论

## 1.1 选题背景与问题提出

### 1.1.1 研究背景

作为数字产品、业务流程和社会基础设施的生产活动，软件开发在现代经济与组织运行中扮演着重要角色。与此同时，生成式人工智能的快速发展正在使软件开发进入由人工智能广泛参与的新阶段。早期智能开发工具主要承担语法检查、代码搜索和局部自动补全等辅助工作；以大语言模型为基础的新一代工具则能够根据自然语言要求生成函数、解释代码、编写测试、修改程序并辅助调试，从而把人工智能的作用范围扩展到软件开发生命周期中的多类任务。Gartner 在 2024 年发布的预测显示，企业软件工程师使用 AI 代码助手的比例将由 2023 年初不足 10% 上升至 2028 年的 75%；该机构对 598 名全球受访者的调查还显示，63% 的组织已经在试点、部署或使用 AI 代码助手（Gartner, 2024）。Stack Overflow 对来自 177 个国家和地区的 49,000 余名开发者开展的 2025 年开发者调查则显示，84% 的受访者正在使用或计划使用人工智能工具参与开发，高于 2024 年的 76%（Stack Overflow, 2025a）。这些数据虽然不能证明人工智能必然改善软件工程绩效，却共同说明，人工智能参与软件开发已经由局部实验迅速转变为具有广泛现实影响的开发实践。

大语言模型驱动的代码生成技术为软件开发创造了新的可能性，也拓展了人工智能参与开发活动的范围。最初受到广泛关注的 AI 编程助手主要嵌入集成开发环境，根据程序员正在编辑的代码提供单行或代码块建议。既有研究发现，程序员使用这类工具时主要存在两种交互模式：在“加速模式”中，程序员知道下一步应当做什么，并利用助手更快完成操作；在“探索模式”中，程序员尚不确定解决路径，借助助手生成和比较可能方案（Barke et al., 2023）。随着模型推理、工具调用和长上下文能力的发展，人工智能不再只是等待用户逐条接受建议的代码补全器。Claude Code 被描述为能够读取代码库、跨文件修改代码、运行测试并交付提交的 agentic coding system（Anthropic, 2026）；GitHub 允许用户把 issue 或自然语言任务委托给 coding agent，由其异步实施改动、创建 pull request，并在完成后请求用户审查（GitHub, 2026）；Codex 则支持用户将长期任务交给一个或多个代理并行执行，随后查看执行过程和代码差异（OpenAI, 2026）。这些产品资料属于厂商对系统功能的说明，不能作为效果证据，但它们清楚地表明了开发工具形态的变化：人工智能正在由“提出代码建议”转向“接受开发任务并对代码库采取连续行动”。

这种变化正在改变个体用户参与软件开发的方式。在传统编程活动中，用户通常直接编写或修改代码，并通过编译、运行和测试逐步观察自己行为的结果；在代码推荐工具中，用户仍然以直接操作者身份推进任务，只是在局部位置决定是否采纳系统建议。使用 coding agent 时，用户则可以用自然语言描述目标、提供约束和授予工具权限，由 agent 自主读取项目、形成计划、调用终端或外部工具、修改多个制品、运行验证，并根据结果继续迭代。用户的工作因而不再局限于“亲自执行”，而开始包括任务界定、资源授权、过程监督、例外处理和成果验收。Baird 与 Maruping（2021）指出，传统 IS use 研究通常赋予人类行动者以首要地位，并把信息系统视为等待使用的被动工具；agentic IS artifacts 却能够在不确定条件下发起行动并承担被委托的任务，因此需要从“使用工具”进一步转向“向具有能动性的信息系统委托任务”来理解人机关系。Coding agent 正是这一变化在软件开发领域中的集中体现。它并未使人类退出开发活动，而是重新分配了人和技术制品在行动、判断与监督中的角色。

本研究所称的 coding agent，是指能够接受用户以目标形式表达的软件开发任务，并在一定权限和边界内自主获取代码库情境、规划步骤、调用开发工具、修改软件制品、检查执行结果和继续调整行动的 agentic IS artifact。该概念强调的不是系统能否生成代码文本，而是系统能否围绕任务目标形成跨步骤的“感知—规划—行动—观察”循环。因而，coding agent 并不是传统编程工具与生成式对话界面的简单相加，也不能被等同为更长的自动补全。传统开发工具、AI 编程助手和 coding agent 在用户目标、系统行动方式、人机分工和用户监督对象等方面存在实质差异，如表 1-1 所示。传统开发工具主要提高用户直接执行编程行为的效率；AI 编程助手主要向用户提供可选择的局部生成结果；coding agent 则可以在用户没有逐步指定每一个操作的情况下，把抽象目标转化为一系列会改变项目状态的行动。因此，对 coding agent 用户体验的理解，需要在既有编程工具和 AI 辅助编程研究的基础上，进一步解释任务委托、持续行动和结果监督相互结合所形成的新型开发活动。

表 1-1 传统开发工具、AI 编程助手与 coding agent 的比较

| 比较维度 | 传统开发工具 | AI 编程助手 | Coding agent |
| --- | --- | --- | --- |
| 用户输入的典型形式 | 具体命令、代码和直接操作 | 当前代码上下文、提示词和局部请求 | 任务目标、约束、项目规则和反馈 |
| 系统的主要作用 | 支持用户执行既定操作 | 生成解释、代码片段或局部建议 | 规划并执行跨步骤开发任务 |
| 行动发起与推进 | 主要由用户逐步发起 | 用户发起，系统提出可采纳建议 | 用户委托后，系统可连续选择和执行行动 |
| 对工作空间的影响 | 用户直接造成并即时观察 | 通常由用户接受后造成局部改变 | 可跨文件、工具和阶段造成累积性改变 |
| 用户的核心角色 | 直接操作者 | 操作者兼建议评估者 | 委托者、监督者、干预者与验收者 |
| 用户需要掌握的对象 | 自己的操作及其结果 | 建议内容是否适合当前代码 | agent 做了什么、为何这样做、当前结果、未决风险及下一步影响 |
| 代表性研究或资料 | 一般软件工程与工具使用研究 | Vaithilingam et al. (2022); Barke et al. (2023); Mozannar et al. (2024) | Baird & Maruping (2021); GitHub (2026); Watanabe et al. (2025) |

Coding agent 所体现的任务委托和连续行动能力，使其具有潜在的实践价值。Stack Overflow（2025a）的调查显示，在工作中使用 AI agent 的软件开发者中，84% 将其用于软件开发；在 agent 用户中，约 70% 认同 agent 减少了特定开发任务所需时间，69% 认同其提高了个人生产率。然而，这些数据反映的是用户报告的采用与感知结果，而不是 coding agent 的普遍因果效果。对真实开发活动的研究呈现出更复杂的图景。Watanabe 等（2025）分析了 157 个开源项目中由 Claude Code 参与生成的 567 个 pull requests，发现其中 83.8% 最终被合并，但已合并的 pull requests 中有 45.1% 在合并前仍需要额外修改，尤其涉及缺陷修复、文档和项目特定规范。Becker 等（2025）针对 16 名熟悉各自代码库的资深开源开发者开展随机对照实验，共观察 246 个真实任务；参与者事前预计 AI 会使自己快 24%，事后仍认为快 20%，实际测量却显示当时的 AI 工具使任务完成时间增加 19%。后一结果具有特定样本、工具代际和任务情境限制，不能外推为 AI 编程普遍无效，但用户感知与客观任务结果之间的偏差表明，是否采用 agent、是否感觉省力或是否相信任务已经完成，并不足以说明用户实际上掌握了 agent 所造成的项目状态。

Coding agent 同时具有“软件开发系统”和“代理性行动者”两方面属性。一方面，它必须在具有依赖关系、隐含规范、构建配置、测试约束和历史决策的软件项目中产生可维护的软件制品；另一方面，它能够代替用户实施一连串具有状态后果的行动，而这些行动可能发生在多个文件、终端命令、依赖项和验证环节之中。前一属性意味着 agent 产出不能只以语言流畅性或表面可运行性判断，后一属性意味着用户需要理解的对象不再只是一个静态建议，而是一个正在展开、可能偏离预期并持续改变工作空间的行动过程。现有实践也暴露了这两方面属性的张力。Stack Overflow（2025a, 2025b）发现，46% 的开发者不信任 AI 输出的准确性，45% 把调试 AI 生成代码耗时视为主要挫折；在关于 AI agents 的专项问题中，87% 的受访者担忧 agent 提供信息的准确性，81% 担忧数据安全与隐私。OpenAI（2026）在介绍多 agent 开发界面时也把核心挑战表述为如何大规模地指挥、监督和协作，并明确指出既有 IDE 与终端界面并非为这种工作方式而设计。由此可见，coding agent 的现实价值不仅取决于它“能做多少”，也取决于个体用户能否在 agent 扩大行动范围和提高行动速度的同时，维持对任务状态及其后果的充分把握。

由于 coding agent 的发展依托于生成式人工智能，同时又深度嵌入软件开发的任务、工具与工作空间，从概念层面研究 coding agent 用户体验，需要同时检验其“代理性行动”与“软件制品改变”的联合影响。换言之，需要回答：用户如何知道 agent 正在处理什么、已经采取了哪些行动以及这些行动如何改变项目？用户如何判断当前结果是否满足原始目标与项目约束？当 agent 在后台运行、跨文件修改或频繁请求批准时，哪些界面与交互条件能够帮助用户形成对任务态势的充分掌握，哪些条件又会使用户仅仅产生“似乎已经完成”的主观确信？这些问题不能只通过模型基准得分、生成代码正确率或最终任务时间得到解释，因为这些指标不直接描述用户在委托、监督和验收过程中对当前任务状态的主观掌握。本研究因此从个体用户视角出发，拟以 Taylor（1990）的主观 situation awareness 及其 Situational Awareness Rating Technique（SART）为基础概念，探索 coding agent 情境中用户对任务态势的主观觉察，进而解释这一用户体验如何形成、如何测量以及为何会影响后续判断与行为。

### 1.1.2 问题提出

Coding agent 作为一种新兴的软件开发工具形态，已经引起产业界和研究者的广泛关注。然而，当前 coding agent 的发展仍主要由模型能力、产品功能和开发实践推动，关于个体用户如何持续理解和监督 agent 行动的理论研究尚处于起步阶段。已有 AI 辅助编程研究主要考察代码建议的有用性、采纳、信任、可用性、生产率和程序正确性。例如，Vaithilingam 等（2022）发现，Copilot 未必改善任务完成时间或成功率，但多数参与者仍愿意在日常编程中使用它；参与者在理解、编辑和调试生成代码方面遇到的困难会妨碍任务解决。Barke 等（2023）区分了程序员使用代码生成模型的加速与探索模式。Mozannar 等（2024）进一步识别了程序员与代码推荐系统交互时的活动和时间成本。这些研究为理解“系统给出建议、用户决定是否采纳”的辅助式交互提供了重要基础，但 coding agent 所要求的用户活动已经扩展为“用户给出目标、系统跨步骤行动、用户在有限注意下监督并验收结果”。当系统从局部建议者转变为能够改变工作空间的行动者时，研究对象也从单次输出评价扩展到用户对整个任务进展、项目变化和潜在后果的持续掌握。

Agentic technology 运用于软件开发，促进了开发活动分工的变化。那么，coding agent 是如何把用户目标转化为软件制品变化的？用户又是依靠哪些信息，在何种交互过程中监督这些变化并决定继续、干预、批准或接管的？回答这些问题，研究者需要考虑 coding agent 如何使用户同时实现“委托执行”和“保持监督”两个相互依赖但可能相互冲突的目标。一方面，用户之所以采用 agent，是为了减少逐步编码和操作所需的直接投入；另一方面，用户仍需要对进入代码库的改变作出判断，并通常承担任务结果的实际责任。现有研究已经讨论了一些适用于一般 AI 或传统人机交互情境的通用感知，例如信任、感知有用性、感知易用性、透明度和控制感。这些概念有助于解释用户是否愿意依赖系统、是否认为系统有价值或是否感觉能够干预系统，却不能独立回答用户是否认为自己已经掌握了“agent 当前做了什么、改变了什么、为何出现当前结果以及接下来可能发生什么”这一组任务状态问题。信任可以在缺乏充分了解时仍然很高或很低；控制感可以来自暂停和撤销能力，却不保证用户知道应当何时使用这些能力；透明度描述系统是否提供信息，也不等同于用户是否把分散信息整合为可支持任务判断的认识。因此，研究 coding agent 不能只把既有通用用户感知直接移植到新工具上，还需要识别代理性开发活动所要求的特定主观任务状态。

Taylor（1990）提出的主观 situation awareness 为分析上述问题提供了一个有依据的概念起点。Taylor 在航空自动化改变操作员角色的背景下，把 situation awareness 理解为与安全、迅速且有效完成任务有关的事件、因素和变量的知识、认知与预期，并通过 SART 让操作者对自身态势觉察进行主观评定。这个概念起点与本研究的个体用户体验目标相符：本研究关心的不是系统事实上展示了多少日志，也不仅是用户回答任务真值问题的客观准确率，而是用户在一次具体 coding-agent 任务中，主观上认为自己是否掌握了足以监督和验收该任务的状态。然而，Taylor 的原始构念内容来自飞行员对航空任务的理解，其常用测量内容围绕注意需求、注意资源和理解展开。Coding agent 所创造的任务态势则分布于自然语言要求、agent 计划、跨文件修改、工具执行、测试证据、权限边界和后续软件影响之中；它既不是单一视觉显示问题，也不是用户亲自操作动态系统时的传统态势觉察问题。因此，SART 不能被不加检验地直接套用于 coding agent。需要通过 coding agent 用户的实际经验重新识别：Taylor 主观 SA 的哪些核心含义在该情境中仍然成立，哪些航空任务内容不再适用，以及 agent 自主行动和软件制品变化带来了哪些必须补充的新内容。

上述概念问题具有直接的实践后果。Coding agent 若不能把自身行动和项目变化转化为用户能够掌握的任务态势，用户可能需要反复检查 diff、日志、测试和文件状态，抵消自动执行节省的精力；也可能在没有充分理解的情况下批准结果，使隐藏的范围偏移、约束违反或不完整验证进入后续开发流程。反之，若界面以高频、低诊断价值的权限请求打断用户，用户可能逐渐形成机械批准，而不是获得更充分的任务掌握。GitHub（2026）要求 coding agent 在完成任务后提交 pull request 并请求用户审查，同时对生成代码进行安全扫描，这说明人类验收和可审计性仍然是现实工作流的组成部分。Watanabe 等（2025）的实证结果表明，大量 agent-assisted pull requests 在合并前仍需人工修改；Stack Overflow（2025a）的调查则同时呈现了较高的感知效率收益与广泛的准确性担忧。实践真正需要解决的因而不是简单地增加或减少 agent 自主性，而是帮助用户在合理注意投入下形成与任务需要相匹配的主观态势觉察，并识别这种觉察何时与客观任务状态一致、何时只是过度自信或过度怀疑。

现有 situation awareness 文献也提示，主观态势觉察不能被自动解释为客观正确性。Endsley 等（1998）直接比较 SART 与 SAGAT 后发现，SART 与主观信心、简单主观 SA 和主观绩效评价高度相关，却与基于任务冻结提问的客观 SAGAT 得分不相关。这一结果一方面支持把 SART 理解为具有独立意义的主观用户体验，另一方面也要求研究者明确区分“用户感觉自己掌握了任务态势”与“用户关于任务真值的判断事实上准确”。Coding agent 情境尤其可能放大这种分离：流畅的进度叙述、成功的测试摘要或看似完整的代码差异可能提高用户的主观把握，却未必暴露遗漏的需求、未执行的验证或跨文件副作用。因此，本研究既需要发展能够描述 coding agent 特定任务内容的主观 SA 构念，也需要在后续研究中用适当的客观任务状态指标检验其校准边界。

基于以上分析，本研究旨在解决以下研究问题：

（1）在 coding agent 参与的软件开发活动中，个体用户需要掌握哪些与 agent 行动、软件制品变化、任务约束和后续影响有关的态势内容，才能监督和验收一次具体任务？

（2）如何以 Taylor（1990）的主观 situation awareness 为唯一基础概念，发展 coding agent 任务主观态势觉察构念？该构念包含哪些具体维度，应当如何测量？

（3）Coding agent 的任务特征、行动特征与界面设计如何影响用户的任务主观态势觉察？

（4）Coding agent 任务主观态势觉察如何影响用户的批准、干预、接管和依赖行为，以及任务绩效与软件结果？用户的主观态势觉察与客观任务状态之间的校准在上述关系中发挥什么作用？

---

## 与 Dong 开篇的逐段逻辑映射（供审稿，不属于论文正文）

| Dong 原文中的论证动作 | 本稿对应位置 | 对应证据的功能 | 处理说明 |
| --- | --- | --- | --- |
| 从电子商务的经济重要性与增长切入 | 研究背景第 1 段：软件开发的重要性与 AI 工具扩散 | Gartner、Stack Overflow 用于证明现象规模与趋势 | 保留“母领域 + 技术扩散”的动作；未虚构 coding agent 市场收入 |
| 新技术为母领域创造机会并改变运作方式 | 第 2 段：从代码补全到跨步骤行动 | Barke et al. 说明旧交互；Anthropic、GitHub、OpenAI 说明新功能 | 厂商资料只证明产品能力主张，不证明效果 |
| 新技术改变个体日常活动并催生新情境 | 第 3 段：从直接编码到委托、监督与验收 | Baird & Maruping 提供 agentic IS 的理论依据 | 对应 Dong 的“社会媒体改变活动方式”，但改为个体开发活动 |
| 定义新情境，并强调不是两类旧事物简单相加 | 第 4 段与表 1-1 | 三类工具比较用于建立 coding agent 边界 | 严格保留该论证动作，因为 coding agent 确有独立行动循环 |
| 用市场/实践数据表明新情境具有潜在影响力 | 第 5 段：采用、感知收益与客观效果分歧 | Stack Overflow、Watanabe et al.、Becker et al. | 不设置缺乏可靠口径的“市场规模图”；用采用和现场研究替代 |
| 展开新情境的复合属性 | 第 6 段：软件开发系统 + 代理性行动者 | 调查、实证研究与产品界面资料 | 对应社会化商务的双重属性，但内容完全来自 coding agent 情境 |
| 从复合属性提出 why/how 和实践价值 | 第 7 段：为何需要研究用户对任务态势的掌握 | Taylor/SART 作为后续概念入口 | 此处只提出研究方向，不提前宣布最终维度 |
| 指出实践发展快于理论研究 | 问题提出第 1 段 | AI 辅助编程研究与 coding agent 任务结构比较 | 保留 Dong 的“实践推动、理论起步”动作，并具体说明已有研究研究了什么 |
| 说明通用技术特征/感知无法解释特定目标 | 问题提出第 2 段 | trust、control、transparency 的边界分析 | 对应 Dong 对通用设计准则和 TAM 感知的批评，但不把它们混为基础概念 |
| 引入唯一基础概念并说明为何不能直接套用 | 问题提出第 3 段 | Taylor (1990) 的定义与 SART 开发情境 | 这是本研究与 Dong“由既有广义概念发展情境化构念”的核心对应 |
| 用现实后果说明问题为何重要 | 问题提出第 4 段 | GitHub 审查流程、Watanabe et al.、Stack Overflow | 对应 Dong 对交易与平台管理问题的实践论证，但聚焦个体监督与验收 |
| 进一步明确测量和效标边界 | 问题提出第 5 段 | Endsley et al. (1998) 的 SART–SAGAT 比较 | Dong 原文没有完全对应句；这是避免把主观 SA 写成客观正确性的必要补充 |
| 提出研究问题 | 四个研究问题 | 分别对应内容识别、概念/量表、前因、后果与校准 | 未仿写 Dong 与本研究无关的买卖关系形成问题 |

## 本节参考文献

- Anthropic. (2026). *Claude Code: Anthropic's agentic coding system*. https://www.anthropic.com/product/claude-code
- Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. *MIS Quarterly, 45*(1), 315–341. https://doi.org/10.25300/MISQ/2021/15882
- Barke, S., James, M. B., & Polikarpova, N. (2023). Grounded Copilot: How programmers interact with code-generating models. *Proceedings of the ACM on Programming Languages, 7*(OOPSLA1), 85–111. https://doi.org/10.1145/3586030
- Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. *arXiv*. https://doi.org/10.48550/arXiv.2507.09089
- Endsley, M. R., Selcon, S. J., Hardiman, T. D., & Croft, D. G. (1998). A comparative analysis of SAGAT and SART for evaluations of situation awareness. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 42*(1), 82–86. https://doi.org/10.1177/154193129804200119
- Gartner. (2024, April 11). *Gartner says 75% of enterprise software engineers will use AI code assistants by 2028*. https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028
- GitHub. (2026). *About third-party coding agents*. GitHub Docs. https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents
- Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E. (2024). Reading between the lines: Modeling user behavior and costs in AI-assisted programming. In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3613904.3641936
- OpenAI. (2026, February 2; updated March 4). *Introducing the Codex app*. https://openai.com/index/introducing-the-codex-app/
- Stack Overflow. (2025a). *2025 Stack Overflow Developer Survey: AI*. https://survey.stackoverflow.co/2025/ai
- Stack Overflow. (2025b, July 29). *Stack Overflow's 2025 Developer Survey reveals trust in AI at an all time low*. https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
- Taylor, R. M. (1990). Situational awareness rating technique (SART): The development of a tool for aircrew systems design. In *Situational Awareness in Aerospace Operations (AGARD-CP-478)* (pp. 3/1–3/17). NATO–AGARD.
- Vaithilingam, P., Zhang, T., & Glassman, E. L. (2022). Expectation vs. experience: Evaluating the usability of code generation tools powered by large language models. In *CHI Conference on Human Factors in Computing Systems Extended Abstracts*. https://doi.org/10.1145/3491101.3519665
- Watanabe, M., Li, H., Kashiwa, Y., Reid, B., Iida, H., & Hassan, A. E. (2025). On the use of agentic coding: An empirical study of pull requests on GitHub. *arXiv*. https://doi.org/10.48550/arXiv.2509.14745
