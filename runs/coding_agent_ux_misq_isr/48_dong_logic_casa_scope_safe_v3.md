# 编程智能体态势感知研究：选题背景与问题提出

> 本稿为第三版独立写作稿，仅覆盖第 1.1 节。相较于前稿，本稿收缩研究承诺，将编程智能体态势感知严格界定为个体用户的主观体验，不将其等同于客观任务知识、实际监督行为、客观掌控能力或软件结果正确性。

## 第 1 章 绪论

## 1.1 选题背景与问题提出

### 1.1.1 研究背景

作为数字产品、数字服务和组织信息基础设施的生产活动，软件开发在现代经济运行和企业价值创造中发挥着重要作用。随着生成式人工智能具备理解自然语言、生成程序和调用开发工具的能力，人工智能在软件开发中的应用已经由局部代码补全扩展到需求分析、缺陷修复、代码重构、测试和维护等多类活动。麦肯锡全球研究院对 63 类生成式人工智能用例的分析表明，软件工程是生成式人工智能潜在经济价值最集中的四类企业职能之一；人工智能对软件工程生产率的直接影响可能相当于该职能年度支出的 20% 至 45%（McKinsey Global Institute, 2023）。麦肯锡后续对近 300 名上市公司高级管理者的调查发现，超过 90% 的受访软件团队已经在重构、现代化改造和测试等活动中使用人工智能，受访团队平均每周节省约 6 小时（McKinsey & Company, 2025）。在由辅助生成向代理执行演进的市场中，Gartner 估计企业编程智能体市场截至 2026 年 4 月的年化规模约为 98 亿至 110 亿美元（Gartner, 2026a）。作为代表性产品之一，OpenAI 报告 Codex 在 2026 年 6 月的每周活跃用户已超过 500 万，较同年 2 月桌面应用发布时增长六倍以上（OpenAI, 2026a）。上述资料分别来自咨询机构调查、市场估计和厂商使用数据，不能据此推断编程智能体必然改善所有软件开发任务，但这些资料共同说明，企业和个体用户正在投入大量资源尝试把人工智能的任务执行能力转化为软件开发收益。因此，编程智能体已成为具有明确实践规模和潜在商业影响的研究情境。

编程智能体是能够接受用户提出的软件开发目标，在一定权限边界内获取项目情境、规划任务步骤、调用开发工具、修改软件制品、检查执行结果并继续调整行动的能动型信息系统。它与传统开发工具之间的关键区别，不在于是否使用人工智能生成代码，而在于系统能否在用户没有逐步指定每个操作的情况下，围绕任务目标形成连续行动。Baird 与 Maruping（2021）指出，传统信息系统使用研究通常把技术制品视为等待人类操作的被动工具，而能动型信息系统能够在不确定条件下接受任务并采取行动，由此使人机关系由直接使用扩展到任务委托。编程智能体把这种变化带入软件开发活动：用户可以提出缺陷修复或代码重构目标，由系统读取项目、修改多个文件、执行命令和测试，再把过程或结果交还用户判断。Robbes 等（2026）根据代码提交和合并请求中的可识别痕迹分析 129,134 个 GitHub 项目，估计编程智能体的项目采用率已达到 15.85% 至 22.60%，且采用范围覆盖不同成熟程度、编程语言和主题的项目。Gartner 进一步预测，到 2027 年，在采用智能体编程的工程团队中，超过 65% 将不再把集成开发环境视为必不可少的工作入口，开发控制、治理与验证将进一步转移到自动化平台（Gartner, 2026b）。这些变化表明，编程智能体并不只是提高代码输入速度的新工具，而是在改变用户参与软件开发任务的方式。

相较于编程智能体的代理执行方式，在用户亲自选择操作、修改代码并观察执行结果的开发活动中，用户意图、用户行动与工作空间变化之间的联系通常更为直接。编程智能体承担连续行动后，这种联系被部分转化为间接联系：用户知道自己委托了什么，却未必持续知道系统采取了哪些步骤、项目发生了哪些变化、当前结果意味着什么，以及哪些不确定性仍然存在。这使用户难以仅凭自己的直接操作经历形成对任务状态的认识。Dhanorkar 等（2026）对 17 名有经验开发者的访谈发现，开发者对软件智能体的应对贯穿事前设置、共同规划、实时查看和事后审查等阶段，同时普遍面临难以充分审查智能体生成代码的问题。为控制投入，开发者有时以智能体计划或测试通过作为实际行动和代码正确性的替代线索，但研究者指出，这些做法更接近在现实约束下形成的足够使用的判断，而非完备检验（Dhanorkar et al., 2026）。Stack Overflow（2025）的调查显示，87% 的受访者担忧人工智能代理提供信息的准确性，81% 担忧数据安全与隐私；在更广泛的开发人工智能使用中，45% 的受访者把调试人工智能生成代码耗时列为主要挫折。Watanabe 等（2025）对 567 个编程智能体参与生成的代码合并请求进行分析，发现其中 83.8% 最终被合并，但已合并请求中仍有 45.1% 在合并前需要人工修改。上述研究并不直接测量用户的态势感知，却共同指向一个值得检验的用户体验问题：当软件变化越来越多地由编程智能体间接造成时，用户是否感觉自己仍然看得清任务正在发生什么，可能成为系统是否易于理解、易于判断和易于继续交互的重要方面。

自动化研究为理解这一用户体验问题提供了理论依据。Taylor（1990）指出，自动化技术改变了人类操作者的角色，使传统上以降低工作负荷为中心的系统评价不足以描述操作者在不确定环境中的体验与判断；为此，他把态势感知界定为与任务安全、迅速和有效实施有关的事件、因素和变量的知识、认知与预期，并发展了主观态势感知评定技术。Endsley（1995a）从动态决策角度进一步指出，态势感知为后续判断和行动提供信息基础，系统设计、任务复杂性、工作负荷和自动化程度均可能影响其形成。Endsley 与 Kiris（1995）的自动化导航实验发现，较低的态势感知与自动化失效后的决策迟缓相对应，说明当操作者由直接执行者转变为自动化系统使用者时，对当前状态的认识可能成为其判断和接管的重要条件。van de Merwe 等（2024）对智能体透明度、态势感知、心理负荷和操作者绩效进行系统综述后发现，在人类需要响应智能体建议或承担监督角色的任务中，提高自动化透明度总体上有助于态势感知和操作者绩效，而不必然增加心理负荷。这些研究表明，在系统代替用户连续行动的情境中，用户对任务态势的主观掌握并非附带体验，而是值得被系统设计与用户研究单独考察的心理状态。

本研究将这一心理状态初步称为编程智能体态势感知，简称 CASA。CASA 是指用户在一次具体的编程智能体任务中，对自己已经掌握了判断任务进展与结果所需的智能体行动、软件制品变化、任务约束和可能后续影响的主观程度判断。当 CASA 较高时，用户主观上认为自己能够说明任务当前处于什么状态、智能体实施了哪些关键行动、这些行动对项目意味着什么，以及尚有哪些事项需要关注；当 CASA 较低时，用户主观上感到任务过程、软件变化或后续影响仍不清楚。该构念描述的是用户感觉自己了解多少，而不是用户实际上知道多少。因此，较高的 CASA 不保证用户关于代码、测试或风险的判断客观正确，也不证明用户实施了充分审查，更不等同于用户真正控制了智能体。Endsley 等（1998）对主观 SART 与客观 SAGAT 的直接比较支持了这种区分：SART 与主观信心、简单主观态势评价和主观绩效评价相关，但与基于任务问题正确率的 SAGAT 并不相关。这一结果也意味着，主观态势评价可能与一般任务信心接近；CASA 的量表项目因而必须具有明确的任务内容指向，并在后续验证中检验其与任务信心的区分效度。对本研究而言，主观评价与客观正确性之间的差异不是需要掩盖的测量缺陷，而是确定研究对象边界的依据，即 CASA 旨在描述编程智能体使用过程中用户对自身任务掌握状况的主观体验，而不替代客观代码审查或任务正确性评价。

把 CASA 作为用户体验构念具有特定而有限的研究价值。首先，信任描述用户是否愿意接受系统的脆弱性风险，感知控制描述用户是否认为自己能够影响系统，透明度描述系统是否提供有关其内部状态或行动的信息；这些概念均不能直接表示用户主观上是否已经把分散的信息整合为对当前编程任务的充分认识。其次，编程智能体界面可以提供计划、日志、代码差异、测试结果和权限请求，但提供更多信息并不必然使用户感觉更了解任务；信息可能过于分散、缺少关联，也可能通过高频提示增加交互负担。CASA 因而可以作为评价界面信息是否支持用户形成任务理解的近端体验指标，而不是以信息数量替代用户体验。最后，CASA 可能与用户的感知控制、任务信心、交互负担、依赖判断和持续使用意愿有关，但这些关系需要后续研究检验，不能在研究背景中预先断言。基于上述边界，本研究不试图解释编程智能体全部商业价值，也不声称 CASA 决定实际监督质量，而是聚焦于发展和测量这一特定用户体验，并考察少数理论上相关的前因与后果。这样的研究可以为编程智能体产品提供比模型能力和任务完成率更接近用户体验的评价依据，也可以帮助设计者判断行动呈现、变化汇总和交互反馈是否使用户获得适当的主观任务认识。

### 1.1.2 问题提出

编程智能体的快速发展已经引起研究者和实践者的广泛关注，但相关研究主要由模型能力评价、软件制品分析和产品实践推动，针对个体用户主观体验的理论积累仍然有限。已有人工智能编程研究主要关注代码建议的采纳、可用性、信任、生产率和程序正确性。例如，Vaithilingam 等（2022）发现，使用代码生成工具未必改善参与者的任务完成时间或成功率，但多数参与者仍愿意使用该工具，同时在理解、编辑和调试生成代码方面存在困难。Barke 等（2023）把程序员使用代码生成模型的交互区分为加速模式和探索模式。Mozannar 等（2024）则识别了用户与代码推荐系统交互时的常见活动及其时间成本。这些研究为理解人工智能提供代码建议时的用户体验奠定了基础，但没有直接回答当系统围绕任务目标持续采取行动时，用户如何主观判断自己是否仍然掌握当前任务态势。

现有通用用户感知也不能代替 CASA。用户可以信任一个自己并不充分了解的系统，也可以因为不信任而反复检查一个实际上已经充分解释的结果；因此，信任与主观任务掌握并非同一心理判断。用户可以拥有暂停、撤销和修改权限，却仍然不知道何时需要使用这些权限；因此，感知控制也不等于 CASA。系统可以完整展示日志和代码差异，但用户未必能够从中形成对任务状态和后续影响的整体认识；因此，系统透明度是可能影响 CASA 的技术条件，而不是 CASA 本身。若不区分这些概念，研究就可能把用户愿不愿意依赖、能不能干预、系统提供了多少信息以及用户感觉自己了解多少混为一谈，从而无法准确解释编程智能体特有的间接行动体验。

Taylor（1990）的主观态势感知为发展 CASA 提供了单一且明确的概念基础，但其原有内容不能直接套用。Taylor 的研究对象是航空任务中的操作者，其构念内容由飞行员对注意需求、注意资源和任务理解的经验引出。编程智能体用户面对的态势内容则分布在任务要求、智能体计划、代码与配置变化、工具执行、测试证据、权限边界和潜在软件影响之中。更重要的是，编程智能体不仅呈现外部环境信息，而且主动造成需要用户理解的新状态；用户需要认识的是一个非人行动者如何改变软件工作空间。因此，本研究需要保留 Taylor 关于知识、认知与预期的主观判断内核，同时通过编程智能体用户的经验材料重新识别构念内容与维度。该过程属于对既有主观态势感知在新型代理开发情境中的情境化发展，而不是把航空量表改写几个名词后直接使用。

CASA 的研究范围还需要作进一步限定。本研究关注的是具有高低程度差异的个体心理构念，而不是用户是否完成监督的二元行为。研究可以考察行动可观察性、变化汇总质量、反馈整合程度、任务复杂性和用户经验等选定因素是否与 CASA 相关，但不承诺穷尽所有影响因素。研究也可以检验 CASA 与感知控制、任务信心、交互负担、依赖判断或持续使用意愿等选定结果之间的关系，但不能由主观量表直接推断实际代码质量、客观任务知识或真实监督有效性。只有在后续研究另外设置客观任务指标时，才能进一步讨论用户主观判断与客观状态之间是否一致。通过这些限定，本研究所提出的问题能够与构念开发、量表验证和后续个体层实证研究保持一致。

基于以上分析，本研究旨在解决以下研究问题：

（1）编程智能体使用过程中，用户主观上需要掌握哪些与智能体行动、软件制品变化、任务约束和可能后续影响有关的内容？

（2）如何以 Taylor 的主观态势感知为基础发展 CASA 构念？CASA 包含哪些具体维度，应当如何测量，并如何与任务信心、信任、感知控制和系统透明度等相邻概念相区分？

（3）在限定的编程智能体任务情境中，行动可观察性、反馈整合程度、任务复杂性和用户经验等选定因素与 CASA 存在怎样的关系？

（4）CASA 与用户的感知控制、任务信心、交互负担、依赖判断和持续使用意愿等选定结果存在怎样的关系？

---

## 与 Dong 开篇的论证逻辑对应

本说明用于审查写作逻辑，不属于论文正文。

| Dong 的论证动作 | 本稿对应内容 | 收缩或调整理由 |
| --- | --- | --- |
| 先证明母领域和新情境具有经济规模与实践价值 | 研究背景第 1 段 | 保留市场与采用证据，但明确数据来源边界，不把市场增长写成研究将解释的因变量 |
| 说明新技术如何改变母领域的运作方式 | 第 2 段 | 只比较传统开发工具与编程智能体，不再加入边界混淆的人工智能编程助手类别或比较表 |
| 说明个体用户的活动方式发生变化 | 第 3 段 | 把直接操作转为间接行动作为核心变化，并立即导向用户是否看得清任务态势的问题 |
| 证明新情境值得形成独立研究对象 | 第 3–4 段 | 由开发者经验、自动化理论和态势感知实证共同支撑，而非仅用产品功能宣布其独特性 |
| 定义新情境及其核心特征 | 第 2 段 | 将核心特征限定为系统围绕目标连续行动，避免用是否生成代码作边界 |
| 从实践价值逐步引出研究关注点 | 第 3–6 段 | 商业价值只用于说明情境重要性，研究关注点逐步收敛为主观任务态势体验 |
| 指出现有通用概念不足 | 问题提出第 2 段 | 分别解释信任、感知控制和透明度为何不能替代 CASA |
| 引入唯一基础概念并说明迁移必要性 | 问题提出第 3 段 | 以 Taylor 的主观态势感知为唯一基础，明确航空内容为何不能直接套用 |
| 形成可由论文回答的研究问题 | 问题提出第 4 段及四个研究问题 | 仅承诺内容识别、构念和量表开发、选定前因与选定后果，不承诺解释全部商业价值或实际监督质量 |

## 表述边界与潜在攻击点审计

| 容易受到质疑的表述 | 本稿处理 | 研究边界 |
| --- | --- | --- |
| 本研究解释编程智能体商业价值如何实现 | 删除 | 商业价值只用于证明研究情境重要；论文不以企业商业价值为待解释结果 |
| CASA 使用户实现有效监督 | 删除 | CASA 是主观心理状态，不等于监督行为或监督有效性 |
| 高 CASA 代表用户真正了解任务 | 明确否定 | 高 CASA 只代表用户认为自己了解；客观知识需要独立测量 |
| CASA 提高软件质量和任务绩效 | 不作预断 | 主观量表不能直接支持此结论，除非后续另设客观指标 |
| 研究所有影响 CASA 的因素 | 收缩为选定因素 | 前因限定为后续模型明确纳入的任务、系统和用户变量 |
| 研究 CASA 的所有后果 | 收缩为选定结果 | 后果限定为个体层用户体验、心理判断和使用意愿变量 |
| 人工智能编程助手与编程智能体构成清晰三分法 | 删除 | 不建立可能因产品形态连续变化而失效的工具分类表 |
| SART 可以直接测量 CASA | 明确否定 | 只继承主观态势感知内核，具体内容和项目必须重新发展与验证 |

## 本节参考文献

- Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. *MIS Quarterly, 45*(1), 315–341. https://doi.org/10.25300/MISQ/2021/15882
- Barke, S., James, M. B., & Polikarpova, N. (2023). Grounded Copilot: How programmers interact with code-generating models. *Proceedings of the ACM on Programming Languages, 7*(OOPSLA1), 85–111. https://doi.org/10.1145/3586030
- Dhanorkar, S., Passi, S., & Vorvoreanu, M. (2026). Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents. *arXiv*. https://doi.org/10.48550/arXiv.2606.05391
- Endsley, M. R. (1995a). Toward a theory of situation awareness in dynamic systems. *Human Factors, 37*(1), 32–64. https://doi.org/10.1518/001872095779049543
- Endsley, M. R., & Kiris, E. O. (1995). The out-of-the-loop performance problem and level of control in automation. *Human Factors, 37*(2), 381–394. https://doi.org/10.1518/001872095779064555
- Endsley, M. R., Selcon, S. J., Hardiman, T. D., & Croft, D. G. (1998). A comparative analysis of SAGAT and SART for evaluations of situation awareness. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 42*(1), 82–86. https://doi.org/10.1177/154193129804200119
- Gartner. (2026a). Leading in enterprise AI coding agents requires more than product momentum. https://www.gartner.com/en/articles/enterprise-ai-coding-agent-market
- Gartner. (2026b, May 20). Gartner says the market for enterprise AI coding agents is entering a new phase of expansion and competitive realignment. https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-says-the-market-for-enterprise-ai-coding-agents-is-entering-a-new-phase-of-expansion-and-competitive-realignment
- McKinsey & Company. (2025). Unlocking the value of AI in software development. https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/unlocking-the-value-of-ai-in-software-development
- McKinsey Global Institute. (2023). The economic potential of generative AI: The next productivity frontier. https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier
- Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E. (2024). Reading between the lines: Modeling user behavior and costs in AI-assisted programming. In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3613904.3641936
- OpenAI. (2026a, June 2). Codex is becoming a productivity tool for everyone. https://openai.com/index/codex-for-knowledge-work/
- Robbes, R., Matricon, T., Degueule, T., Hora, A., & Zacchiroli, S. (2026). Agentic much? Adoption of coding agents on GitHub. *arXiv*. https://doi.org/10.48550/arXiv.2601.18341
- Stack Overflow. (2025). 2025 Stack Overflow Developer Survey: AI. https://survey.stackoverflow.co/2025/ai
- Taylor, R. M. (1990). Situational awareness rating technique: The development of a tool for aircrew systems design. In *Situational Awareness in Aerospace Operations, AGARD-CP-478* (pp. 3/1–3/17). NATO–AGARD.
- Vaithilingam, P., Zhang, T., & Glassman, E. L. (2022). Expectation vs. experience: Evaluating the usability of code generation tools powered by large language models. In *CHI Conference on Human Factors in Computing Systems Extended Abstracts*. https://doi.org/10.1145/3491101.3519665
- van de Merwe, K., Mallam, S., & Nazir, S. (2024). Agent transparency, situation awareness, mental workload, and operator performance: A systematic literature review. *Human Factors, 66*(1), 180–208. https://doi.org/10.1177/00187208221077804
- Watanabe, M., Li, H., Kashiwa, Y., Reid, B., Iida, H., & Hassan, A. E. (2025). On the use of agentic coding: An empirical study of pull requests on GitHub. *arXiv*. https://doi.org/10.48550/arXiv.2509.14745
