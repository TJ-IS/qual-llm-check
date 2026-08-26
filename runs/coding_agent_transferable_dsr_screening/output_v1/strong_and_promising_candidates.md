# Strong and promising candidates

Completed: 1832 / 1832
Retained: 287

## strong_candidate: Predicting employee absenteeism for cost effective interventions

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113539
- Source outcome: Cost Improvement Score (CIS) and Return On Investment (ROI) of an intervention campaign
- Coding-agent outcome: 编码代理变更的干预成本效益（autonomous-change intervention cost-effectiveness）
- Decision: 该文属于'design_oriented_build_evaluate'：实际构建并评估了面向员工缺勤干预的决策支持系统。理论到设计强度为强：Elkan的成本敏感学习理论直接推导了误分类成本矩阵、DMECC决策阈值和CIS/ROI评估指标。评估结果CIS/ROI是定量测量的、领域构成性的结果，其含义嵌入比利时病假法规和健康干预情境。该结果可向编码代理迁移：将缺勤风险预测映射为代理变更风险预测，将健康干预映射为人工审查/验证干预，形成'代理变更干预成本效益'这一强编码代理特定结果，具备非替代性。因此判定为strong_candidate。
- Confidence: 0.9

## strong_candidate: Inverse Transparency and the Quest for Empowerment through the Design of Digital Workplace Technologies

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00879
- Source outcome: Inverse transparency (bidirectional transparency/access visibility)
- Coding-agent outcome: 智能体逆向透明度（agentic inverse transparency）：用户可查看并控制编码智能体对代码库、数据和工具的访问与操作
- Decision: 该文是明确的设计科学研究（DSR），采用Peffers等人的流程，以Stewardship Theory为内核理论并显式推导DR/DP/DF，定性评估了逆向透明度、自我决定和管家行为等结果。其中'逆向透明度'在源领域具有领域构成性意义（工作场所数据权力、反监视、员工赋能），且可以强映射到编码智能体：自主智能体对代码库/数据/工具的不可见访问需要'智能体逆向透明度'这一设计目标。因此满足强候选条件。
- Confidence: 0.9

## strong_candidate: Sustainability Design Principles for a Wildlife Management Analytics System: An Action Design Research

- Year/journal: 2021 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1811786
- Source outcome: Anticipating affordances: identify threat of poaching on wildlife; identify threat of human-wildlife conflict on wildlife
- Coding-agent outcome: 代码变更前的风险预判与计划调整能力
- Decision: 该文采用明确的elaborated action design research方法，实际构建并两轮迭代一个野生动物管理分析系统（WMAS），并通过workshop和访谈进行前后对比评估，属于explicit design science。Affordance theory和Chandra的设计原则模板直接用于推导设计原则，theory-to-design强度为strong。在评估结果中，“anticipating affordances”（识别偷猎与人兽冲突威胁）是领域构成性的：其利益相关者、风险、操作化都依赖野生动物保护地管理。将该结果向编码智能体迁移时，可形成“代码变更前风险预判与计划调整能力”：智能体自主多步修改、工具副作用、测试反馈等条件使该结果的定义、机制和测量均与静态IDE/普通聊天机器人有实质区别，非替代性强。因此整体为strong_candidate，target_match=true。
- Confidence: 0.87

## strong_candidate: Digital Institutionalization: The Case of E-Prescribing

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00845
- Source outcome: Quality of e-prescriptions (compliance with the exchange contract / errors)
- Coding-agent outcome: 变更契约合规性（agent生成代码变更的质量与合法性）
- Decision: 该文是明确的行动设计研究（ADR）：构建并评估了电子处方交换契约（NEF）这一干预；Speech Act Theory直接塑造了构成性规则和通信行为设计，Institutional Theory与Legitimacy Theory塑造了交换契约、自动校验、反馈机制及设计原则，theory-to-design强度为强。核心被评估结果——电子处方实体质量/合规性（错误率从98.6%降至0.9%）——在医疗处方制度语境中具有领域构成性含义，并能通过“将验证从下游网关推向创建点”的机制映射到编码智能体的变更契约合规性（如agent生成PR/commit的规则符合率），该映射依赖agent的多步规划、仓库级上下文、工具副作用、测试反馈与自我修正等独特条件，因此为strong_candidate。第二候选合法性转移为中等，但不影响总体判断。
- Confidence: 0.86

## strong_candidate: An Activity Theory Approach to Leak Detection and Mitigation in Patient Health Information (PHI)

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00687
- Source outcome: PHI leak detection and mitigation
- Coding-agent outcome: 编码智能体敏感信息泄漏的检测与缓解
- Decision: 该文是显式设计科学研究（应用 Hevner 等 2004 的 DSR 方法），活动理论从设计需求、构件映射到访问控制模型特征和检测/缓解机制，理论到设计链条强；评估了具有医疗领域特异性的 PHI 泄漏检测与缓解结果；将该机制映射到编码智能体的工具调用和信息流泄漏场景具有强非替代性，因此构成 strong candidate。
- Confidence: 0.85

## strong_candidate: The Phishing Funnel Model: A Design Artifact to Predict User Susceptibility to Phishing Websites

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2020.0973
- Source outcome: Phishing susceptibility (final funnel stage)
- Coding-agent outcome: 编码代理对恶意/欺骗性开发指令的易感性（有害行动漏斗遍历）
- Decision: 该文是明确的设计科学研究：PFM 工件由 TAM、PMT、HITLSF 直接推导变量设计，并在两个纵向现场实验中评估了预测性能、干预效果和成本效益。其核心结果“用户对钓鱼网站的易感性/漏斗遍历”是领域构成性的；可将其机制迁移到编码代理对恶意/欺骗性开发指令的易感性及干预校准，且该迁移依赖代理的自主多步执行、工具副作用和人类监督交接，非静态 IDE/普通聊天机器人可替代。因此为 strong_candidate，target_match=true。
- Confidence: 0.85

## strong_candidate: Explainability and fairness of RegTech for regulatory enforcement: Automated monitoring of consumer complaints

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113782
- Source outcome: Consumer complaint outcome: monetary compensation paid to consumer
- Coding-agent outcome: 编码智能体待审查变更的人类监督优先级（triage）质量
- Decision: 该论文是显式设计科学研究（explicit_design_science），遵循Hevner/Peffers DSR范式，提出并评估了设计原则和特征。信息诊断性理论被明确用作核心理论来推导可解释的分类特征（DP1），理论到设计的联系强。评价的核心结果——预测消费者投诉是否导致金钱赔偿（以及基于置信度排序的监管人工筛查lift值）——是金融监管执法情境中领域构成性的结果。该结果和“高置信度案例优先人工处理”机制可以迁移到编码智能体：智能体产生的自治代码变更需要人类审阅者进行triage，用置信度和诊断性变更说明来优先检查高风险变更，且该triage对象在静态IDE/普通聊天机器人中不存在，因此编码智能体特异性强。故评为strong_candidate。
- Confidence: 0.85

## strong_candidate: The Design of a System for Online Psychosocial Care: Balancing Privacy and Accountability in Sensitive Online Healthcare Environments

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00717
- Source outcome: Sustained audit practice (privacy breach auditing)
- Coding-agent outcome: 编码代理敏感/受限操作的可审计正当性
- Decision: 该文是明确的设计科学研究（DSR），构建并自然主义评估了U-CARE软件系统；AOCM、RBAC/MVC、信息问责和涌现的ToS理论对设计原则、动作日志架构和'打破玻璃'机制有直接生成性作用。最有前景的源结果是'持续审计实践'，其意义和操作化高度依赖心理社会护理中的患者敏感数据、伦理审查和医疗问责语境。该结果的问责信息流与打破玻璃机制可迁移到编码代理场景，形成'代理敏感/受限操作的可审计正当性'，依赖代理的自主多步执行、真实环境副作用、委派监督等非替代性条件，因此判定为强候选。
- Confidence: 0.85

## strong_candidate: Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17381
- Source outcome: Completeness of task-relevant information collection across fragmented online channels (landscape coverage)
- Coding-agent outcome: 仓库级任务相关上下文覆盖率（避免局部最优的自主信息搜集）
- Decision: 该文是明确的设计科学/计算设计研究：设计和实现了HealthSense社交倾听平台，并通过数据实验、用户实验和事件检测实验进行了评估。活动理论和上下文信息质量理论对元需求和具体设计元素具有强生成性作用。最具转移潜力的结果“碎片化渠道中的任务相关信息完整性/景观覆盖”在源域中被情境化为公共卫生3.0下的稀疏动态在线渠道问题，并可通过“图传播与隧道潜力”机制映射到编码代理的仓库级上下文覆盖，该机制依赖代理的自主多步探索和仓库副作用，移除代理条件会显著改变定义与测量，因此是强候选。
- Confidence: 0.85

## strong_candidate: Design principles for learning analytics information systems in higher education

- Year/journal: 2021 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1816144
- Source outcome: Student engagement with learning (via lecture recording interaction events)
- Coding-agent outcome: 人类开发者对自主智能体工作的有效干预（校准式监督）
- Decision: 该论文是显式的设计科学研究（DSR），采用Peffers et al. (2007)方法论，构建并评估了一套设计原则和可操作原型；干预理论（Argyris 1970）被明确用作kernel theory，从有效/有用信息、自由知情选择、内在承诺三条原理推导出设计原则，理论到设计的映射强。评估中，学生参与度（LTR交互事件）作为量化结果展示了系统支持的讲师干预效果，且该结果具有教育领域的情境化含义。将该理论/设计机制迁移到编码智能体，可形成'校准式监督/有效人工干预'这一强智能体特定设计目标：智能体自主多步执行、有环境副作用、可能产生隐蔽错误，需要向开发者提供可行动、及时、可理解的信息支持其干预。编码反事实（静态IDE或聊天机器人）会消除该目标的意义，因此智能体特异性强。虽然源结果变量与学生参与度是下游指标，但机制迁移明确，整体为强候选。
- Confidence: 0.82

## strong_candidate: FairPlay: Detecting and Deterring Online Customer Misbehavior

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1035
- Source outcome: Customer repeat violation (Re_Violation)
- Coding-agent outcome: 自主编码代理的规范违反复发率
- Decision: 该文采用设计科学与实验结合的方法，明确构建并评估了FairPlay检测框架和三种基于规范理论的干预策略；焦点规范理论、社会身份理论和威慑理论直接指导了干预消息的设计，理论到设计的联系强；评估结果不仅是检测性能，还包括在品牌社区情境中具有领域构成性的'重复违规'结果，可转化为编码代理的规范违反复发目标，并利用代理的自主多步操作、真实副作用和工具使用等独特条件，非静态IDE或普通聊天机器人可替代。因此判定为strong_candidate。
- Confidence: 0.82

## strong_candidate: Peak cubes in service operations: Bringing multidimensionality into decision support systems

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113442
- Source outcome: Customer dissatisfaction manifested in service churn / defection detection performance
- Coding-agent outcome: 多维峰值-末端失败态势下的人类监督者不满与放弃继续委托（delegation abandonment）
- Decision: 该文属于 design-oriented build/evaluate：构建了 peak cube 模型与算法，并用 24,000 个预测模型和 AUROC 进行了系统评估。peak-end rule 等理论直接生成 peak cube 的特征设计与预期机制，理论到设计链路强。评估的 customer dissatisfaction/churn 预测 outcome 在 B2B 物流服务场景中具有 context-specific 的操作化（多维服务失败时间序列、无契约流失）。向编码智能体迁移时，可将该机制重构为：agent 多步轨迹末端出现多维失败峰值会导致人类监督者不满/放弃继续委托，这依赖于自主多步执行、真实仓库副作用、执行反馈和交接等 coding-agent 特有条件，非替代性强。因此判定为 strong candidate。
- Confidence: 0.82

## strong_candidate: Designing Attentive Information Dashboards

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00732
- Source outcome: Attentional resource allocation (performance)
- Coding-agent outcome: 编码智能体在仓库探索/修改中的'注意力资源再分配'——即在持续多步任务中对先前覆盖不足的仓库区域(文件、模块、测试、依赖)进行补偿性关注
- Decision: 这项研究是显式DSR:作者给出两条基于理论的设计原则,实例化为实时眼动VAF的专注型仪表盘,并在92人受控实验中评估。理论到设计链条清晰(注意力有限/人信息处理理论+眼-心假设导出MR1-MR4和DP1/DP2)。三个被评估结果(注意资源分配、注意转移率、注意资源管理)都在仪表盘数据探索情境中有具体操作化。其中'注意资源再分配'可机制化迁移到编码智能体:智能体的上下文与迭代预算有限,容易在仓库探索中偏向先接触区域而忽略相关文件;源文'监测注意分配->个性化反馈->后续重新分配'的设计机制可转化为'记录智能体对仓库工件的覆盖->反馈覆盖率/相关性->后续迭代补偿探索'。该结果依赖编码智能体的仓库级上下文、自主多步规划和工具调用,去掉代理条件后不再成立,故为强候选。
- Confidence: 0.82

## strong_candidate: Tapping into the wealth of employees’ ideas: Design principles for a digital intrapreneurship platform

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2020.103287
- Source outcome: User control over the system's representations of one's own innovation contributions (user control mechanisms in DP1′–DP3′) 
- Coding-agent outcome: 开发者对编码代理仓库级操作的可见性控制与变更接受权
- Decision: 该文是明确的显性设计科学研究（ADR），构建并评估了数字内创业平台；STS理论作为内核理论系统地用于推导五项设计原则，理论到设计的连接是强/显性的。评价中一个重要结果——用户对自身想法可见性和修改的控制——源领域含义具有组织创新/监视风险的特定上下文，并且能够通过STS平衡机制迁移到编码代理的“开发者对代理仓库级操作的可见性控制与变更接受权”，该迁移依赖代理的自主多步执行、真实副作用、动态人机委派等独特条件，非静态IDE或普通聊天机器人可替代。因此判定为strong_candidate，target_match=true。
- Confidence: 0.82

## strong_candidate: A method for resolving organisation‐enterprise system misfits: An action research study in a pluralistic organisation

- Year/journal: 2023 / Information Systems Journal
- DOI: 10.1111/isj.12433
- Source outcome: Resolution of Org-ES misfits (effective diagnosis and resolution)
- Coding-agent outcome: 委托任务与编码智能体行为之间的错配修复（agent-task misfit resolution）
- Decision: 该文采用行动研究方法构建并评估了一个组织-企业系统错配诊断与解决的方法，属于设计导向的构建-评估研究。理论到设计的关系强：affordance/affordance actualization、用户参与和变更代理人理论直接生成了方法的诊断语言、参与原则和变更代理人编排机制。评价证据同时包含临床流程定量指标和定性访谈，且这些指标嵌入新生儿听力筛查这一具有公共健康与患者安全意义的领域，满足源域情境特异性。候选中最佳的迁移是将“Org-ES misfit 解决”迁移为“编码智能体委托任务-行为错配修复”：源理论机制（实际化/部分实际化/非实际化诊断与 affordance 重组）可重新实例化为对智能体工具调用、仓库改动和自主规划能力的诊断与重组，且该结果依赖编码智能体特有的自主多步、真实副作用、概率性错误和仓库级上下文，具备强非替代性。综合判断为强候选。
- Confidence: 0.82

## strong_candidate: Balancing Affordances and Constraints: Designing Enterprise Social Media for Organizational Knowledge Work

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/16499
- Source outcome: Digital interruptions
- Coding-agent outcome: 自主编码代理引发的注意力干扰负荷
- Decision: 该文属于'design_oriented_build_evaluate'：构建了一个计算性主体建模来模拟ESM设计特征（互动性、可见性）、员工态度（透明度偏好、干扰耐受度）与知识工作绩效之间的关系，并通过超过55万个模拟运行进行系统评估。理论（transactive memory, communication visibility, affordances/constraints, digital interruptions）以中等强度直接塑造了模型中的设计特征与机制。至少有一个被评估的结果（数字干扰）在来源语境中是contextualized，且转移方案具有强编码代理非替代性：自主编码代理因其仓库副作用、多步自治和异步操作，会产生类似'数字干扰'的人类注意力负担，而其'透明度偏好/互动性'配置可直接对应代理的外发互动频率。最佳候选结果的编码代理特定性为strong，机制转移有据，故判定为strong_candidate。
- Confidence: 0.82

## strong_candidate: Behaviorally Measuring Usability by Analyzing Users’ Mouse Movement Efficiency

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17900
- Source outcome: Mouse movement efficiency (MME)
- Coding-agent outcome: 智能体行动轨迹效率（agentic trajectory efficiency）——上下文干扰的行为指标
- Decision: 该论文是设计导向的构建-评估研究：构建了一套基于 BCT 和 RAM 理论的鼠标移动效率测量方法，并在四个研究中定量验证其能测量可用性并区分系统组件。理论到设计的联系是强式的（BCT 提供注意干扰机制，RAM 将干扰映射到运动轨迹偏差，直接定义 MME 指标）。评价结果 MME 和组件可用性排序均具有领域情境化的操作化。向编码智能体的迁移是分析性推断：将人类的运动轨迹效率类比为智能体的动作轨迹效率，用于检测上下文干扰和诊断仓库组件“可用性”，该结果、机制和测量均依赖编码智能体的自主多步规划、仓库级上下文和工具副作用，因此非替代性为强。综合判定为 strong_candidate。
- Confidence: 0.82

## strong_candidate: Dealing with Complexity in Design Science Research: A Methodology Using Design Echelons

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/16700
- Source outcome: Consistency between problem understanding and solution design
- Coding-agent outcome: 问题-方案一致性保持度（issue-to-design traceability in agentic code changes）
- Decision: 该文是显式DSR研究，构建并评估了eDSR方法论；等级多级系统理论直接导出设计梯队概念和五类梯队，属于强理论-设计关联。至少一个被评估的结果（问题理解与方案设计的一致性）在源域中有语境化含义，并且可以映射为编码智能体特有设计目标（问题-方案一致性保持度），该目标依赖agent的自主多步执行、仓库级上下文、可执行工件生成和概率性错误等特征，去除agent条件后目标定义、机制和度量都将实质性改变。故判为strong_candidate。
- Confidence: 0.82

## strong_candidate: Explainable Deep Learning for False Information Identification: An Argumentation Theory Approach

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0097
- Source outcome: Task accuracy (human FII task performance)
- Coding-agent outcome: 基于论证结构的代码变更审查准确率
- Decision: 该文明确采用设计科学方法，构建了 G-FINDER 这一理论驱动的人工制品，Toulmin 模型、结构平衡理论和指称理论共同导出具体设计原则和实现，理论到设计的关联是显式的。实验评估包含人类在 FII 任务上的准确率（SBTX 显著提升），该结果具有语境界定性和特定操作化。将该论证-证据一致性机制迁移到编码代理的变更审查场景，可形成“论证式代码变更审查准确率”这一编码代理特有目标，依赖代理的仓库级上下文、执行反馈、人-代理委托等关键条件，非静态 IDE 或普通聊天机器人可替代。因此判定为 strong_candidate。
- Confidence: 0.82

## strong_candidate: Improving Students’ Argumentation Skills Using Dynamic Machine-Learning–Based Modeling

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0615
- Source outcome: Objective quality of argumentation
- Coding-agent outcome: 代码变更的证据支撑完备性（supported-change ratio）
- Decision: 该文是明确的设计科学研究，构建并评估了基于ML的动态论证建模系统 ArgueLearn；设计由社会认知理论和 Toulmin 论证理论强驱动；评估结果'客观论证质量'具有源域特定性，并能通过'代码变更作为主张、测试/需求/日志作为前提'这一映射转化为编码代理特有的设计目标，因此构成 strong candidate。
- Confidence: 0.82

## strong_candidate: The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18531
- Source outcome: Security warning disregard
- Coding-agent outcome: 自主编码代理对安全关键警告的遵从/不忽视
- Decision: 论文属于design-oriented build/evaluate：它设计并实例化了两种安全警告干预（视觉独特性和交互模式独特性），并通过现场实验和fMRI实验进行评估。理论到设计的链路强：双过程习惯化理论和图式理论直接推导出H1-H3及具体设计特征。最有力的结果“安全警告忽视”是领域构成性结果，在网络安全语境中有明确的风险和操作性定义。在编码代理迁移中，该结果能被重新定义为“自主编码代理对安全关键警告的遵从”，依赖代理的自主多步执行、工具副作用和人的监督/授权等独特条件，且源理论-设计机制（通过区分常规通知与安全关键消息来减少泛化忽视）可映射为编码代理的差异化工交互设计。因此判定为strong_candidate。
- Confidence: 0.82

## strong_candidate: Animation as a dynamic visualization technique for improving process model comprehension

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103478
- Source outcome: process model comprehension
- Coding-agent outcome: 编码智能体执行轨迹理解（coding-agent trace comprehension）
- Decision: 该论文构建并实验评估了一个自适应动画环境（design_oriented_build_evaluate）；认知负荷理论、多媒体学习理论、认知维度框架和专业技能反转效应被明确用于推导设计原则（信号、注意力引导、低/高交互性），并具体落实到动画的视觉与交互特征；主要结果变量“过程模型理解”以BPMN行为语义的迁移任务测量，具有领域构成性；可将其理论与设计机制转化为“编码智能体轨迹理解”这一智能体特定设计目标，因为智能体的多步骤自主执行、工具副作用和自纠错为动态可视化提供了独特对象，静态IDE或普通聊天机器人无法替代。因此判定为strong_candidate。
- Confidence: 0.8

## strong_candidate: Designing Personalized Treatment Plans for Breast Cancer

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1002
- Source outcome: average radiation dose to organs at risk (breast/lung/heart) as indicator of radiation-induced adverse effects
- Coding-agent outcome: 编辑副作用足迹（edit blast radius / collateral exposure）最小化下的目标达成
- Decision: 该文明确采用设计科学范式构建并评价了预测+优化联合框架（explicit_design_science）；TCP放射生物学模型作为kernel theory直接塑造了预测模型和优化目标（theory-to-design strong）；核心结果'平均辐射剂量/辐射诱发副作用风险'是放疗领域特有且定量评价的结果（domain_constitutive）。虽然文章不涉及编码智能体，但从'预测患者反应+在目标约束下最小化副作用暴露'的机制可以转化为编码智能体的'目标达成约束下最小化编辑副作用足迹'设计目标，且该目标在静态IDE/聊天机器人条件下不成立，具有强编码智能体特异性。
- Confidence: 0.8

## strong_candidate: Fall Detection with Wearable Sensors: A Hierarchical Attention-based Convolutional Neural Network Approach

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1990617
- Source outcome: Explainability (hierarchical attention weights)
- Coding-agent outcome: 自治代码修改的分层归因可审查性（hierarchical attribution transparency of autonomous code changes）
- Decision: 该文明确采用计算设计科学范式，构建并评估了HACNN人工制品；'层次注意力机制'和'CNN/表征学习'对模型架构和可解释性目标有直接设计作用。被评估的注意力权重可解释性在跌倒检测领域具有情境化操作化（传感器轴/位置/跌倒类型），且可映射为编码智能体对仓库级多步代码修改的分层归因透明性，移除智能体条件后该结果无意义。因此为strong_candidate。F-measure虽被评估但属通用性能，不用于转移。
- Confidence: 0.8

## strong_candidate: Making green power purchase agreements more predictable and reliable for companies

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113514
- Source outcome: Energy prediction reliability for the buyer / REP forward behavior (quantity adjustment δ*)
- Coding-agent outcome: 编码智能体的前瞻承诺校准（forward commitment calibration）
- Decision: 论文属于model-driven DSS，构建并评估了‘双赢PPA结构决策树’这一决策支持工件；其设计结合了随机网络演算（SNC）推导的储能容量约束和激励定价分析，理论到设计为中等偏强。被评估的结果‘买方得到的预测可靠性’通过δ*相对TEC量化，具有PPA领域构成性意义。该结果可迁移为编码智能体的前瞻承诺校准：在多步委派、仓库级产物和测试反馈条件下，惩罚/奖励结算和有界自验证缓冲机制可激励智能体做出可验证的承诺。因此判定为strong candidate。
- Confidence: 0.8

## strong_candidate: Will Humans-in-the-Loop Become Borgs? Merits and Pitfalls of Working with AI

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/16553
- Source outcome: Unique human knowledge (UHK)
- Coding-agent outcome: 开发者独特知识保持度（Agent 辅助编码下的互补知识保留）
- Decision: 源论文属于设计导向的构建-评估研究：它设计了两种可操作的 AI 建议干预（显示 AI 置信度、基于 r_h 的个性化建议），并用三个实验和模拟评估。理论到设计链条强：UHK 模型与 Diversity Prediction Theorem 直接导出个性化建议的设计阈值和群体绩效假设。UHK 是定量评估且具有情境化含义；向编码智能体的迁移通过'开发者独特知识保持度'这一结局成立，其定义、风险和测量依赖于智能体自主多步生成代码、仓库级上下文和概率性错误等独特条件，满足非替代性测试。因此综合判断为强候选；同时保留众包准确率作为次级候选。
- Confidence: 0.8

## strong_candidate: Achieving a Balance Between Privacy Protection and Data Collection: A Field Experimental Examination of a Theory-Driven Information Technology Solution

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1045
- Source outcome: disclosure behavior (actual information disclosure behavior)
- Coding-agent outcome: 开发者对编码代理的受控授权披露行为（仓库访问、敏感数据/凭据、执行操作许可）
- Decision: 该文属构建-评估型设计研究（design-oriented build-and-evaluate），以正义理论强驱动地设计了“协商+主动推荐”隐私政策应用，并通过现场实验评估了隐私担忧、披露意愿与实际披露行为等结果。其中“实际披露行为”在移动银行情境下被情境化操作化（数量+敏感度加权），其理论-设计机制（程序/交互/分配正义分别对应隐私声明、协商、主动推荐）可迁移至编码代理的访问授权与自治治理，形成强编码代理特异性的“受控授权披露”目标，因此总体判定为强候选。
- Confidence: 0.8

## strong_candidate: Managing Congestion in a Matching Market via Demand Information Disclosure

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2022.1148
- Source outcome: Congestion (attention toward high-demand peers)
- Coding-agent outcome: 拥塞感知的代码修改目标选择（congestion-aware code-module targeting）
- Decision: 文章属于设计导向的构建-评估研究：实际设计并评估了约会App中需求信息披露的多种UI干预。理论-设计联动强：观察学习、容量信号、框架效应等理论被明确用于推导设计的容量/流行度提示特征。评估结果包括拥挤缓解和匹配效率，属于情境化而非完全泛化的结果。最强的编码代理转移是“拥塞感知的代码修改目标选择”，其依赖自主多步规划、仓库级上下文、真实副作用和多方代理协调等代理特有特征，且在移除代理条件后结果定义和机制都会发生实质改变，因此非替代性强。综合判断为strong_candidate。
- Confidence: 0.8

## strong_candidate: Wearable Sensor-Based Chronic Condition Severity Assessment: An Adversarial Attention-Based Deep Multisource Multitask Learning Approach

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15763
- Source outcome: Model interpretability via attention weights (source-level contribution transparency)
- Coding-agent outcome: 证据来源归因透明性（source-attribution transparency of autonomous code changes）
- Decision: 该文明确采用计算设计科学范式，构建并严格评估AADMML框架；注意力机制、对抗学习、多任务学习和多源学习等被具名使用并直接形成Stage 1-4的设计机制。评价结果包括PD特异性严重度评估、注意力权重解释性和早期PD识别经济效益，均具有领域构成性/情境化意义。最具迁移潜力的是注意力权重带来的来源归因透明性：在编码智能体中可重新实例化为对多证据来源贡献的透明归因，支持人类审查自治代码修改；如果去掉智能体自治性、仓库级副作用和概率性错误生成等条件，该设计目标不再成立。因此为强候选，需人工复核。
- Confidence: 0.8

## strong_candidate: Bringing Machine Learning Systems into Clinical Practice: A Design Science Approach to Explainable Machine Learning-Based Clinical Decision Support Systems

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00820
- Source outcome: Explainability
- Coding-agent outcome: 编程代理行为与变更的可解释性/可审查性（developer-perceived explainability of agent plans and repository changes）
- Decision: 本文是明确的设计科学研究：采用两轮 DSR，提出五条设计原则并实例化为 RadiologyAI 原型，通过 6 名放射科医生 walk-throughs 和 45 名放射科医生实验进行评价。认知努力视角、可用性文献和 XAI 解释本体论对设计原则有明确的生成性作用（theory-to-design strong）。评估结果中'可解释性'虽用通用量表测量，但在临床高风险决策中具有情境化意义（逐例验证错误输出、患者安全与医生责任）。该机制可扩展到编程代理：设计原则映射为代理计划/行为的解释分层、按需展示、心智对齐和确定性证据，产生'代理行为可解释性/可审查性'这一强编码代理特异性结果，因此目标匹配。'认知努力'作为第二候选特异性较弱，不改变整体判断。
- Confidence: 0.8

## strong_candidate: Patient health locus of control: the design of information systems for patient-provider interactions

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2088416
- Source outcome: patient engagement
- Coding-agent outcome: 开发者在智能体辅助编码中的内化责任与认知投入
- Decision: 该文是明确的行动设计研究(eADR)，明确构建并评估了LOC评估与参与两套信息系统；LOC理论及多种控制理论直接产生设计需求与干预措施，理论到设计链条强；被评估的结果（患者参与）具有医疗领域特定的含义和操作化，属领域构成性结果；将其机制迁移到编码智能体，可形成'开发者在智能体辅助编码中的内化责任与认知投入'这一强编码智能体特异性设计目标，因此保留为强候选。
- Confidence: 0.8

## strong_candidate: Longitudinal Impact of Preference Biases on Recommender Systems’ Performance

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0133
- Source outcome: Rating inflation (submitted vs. ground-truth rating gap)
- Coding-agent outcome: 编码代理反馈膨胀抗性（acceptance/feedback inflation resistance）
- Decision: 论文虽未标注设计科学研究，但构建并评估了纵向推荐仿真测试台和两种去偏方法，属于 design_oriented_build_evaluate；偏好偏差/锚定构念直接生成了用户反馈模型和去偏设计（theory-to-design strong）；'rating inflation'是与推荐反馈回路高度情境化的被评估结果，可经由机制迁移为编码代理特有的'接受反馈膨胀抗性'设计目标，并通过独立验证和显示信息校准进行观察。因此满足 strong_candidate 条件。
- Confidence: 0.8

## strong_candidate: Ephemeral State-Dependent Recommendation for Digital Content

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.664
- Source outcome: Demand spillover (overall, focal_category, other_categories)
- Coding-agent outcome: 非目标代码模块的正向溢出效应（beneficial non-targeted spillover）
- Decision: 该论文以构建-评估方式提出了状态依赖的数字内容推荐框架并进行了大规模随机现场实验；设计由液态消费理论和一致性理论明确驱动，理论到设计链路强；评价结果包含阅读率/阅读时间和跨类别溢出等情境化结果。其中'非目标模块溢出'可扩展到编码代理的仓库级副作用，具有强的编码代理非可替代性，因此判定为强候选。
- Confidence: 0.8

## strong_candidate: Push It Cross the Finish Line—Designing Online Interfaces to Induce Choice Closure at the Postdecision Prepurchase Stage

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0085
- Source outcome: Perceived choice closure
- Coding-agent outcome: 编码代理的方案/计划选择闭合
- Decision: 论文属于设计导向的构建-评估研究：在模拟电商网站上设计并实现了直接/社会强化界面线索，并用四项受控实验评估其对认知失调、选择闭合、满意度和购买意愿的影响；认知失调理论与自我证明理论明确推导了设计要求和预期机制，理论-设计联结强。被评估的“感知选择闭合”在电商决策后-购买前情境中具有情境化含义，且能通过外部证明机制迁移为编码代理的“方案选择闭合”设计目标：抑制自主代理在选定方案后的反复切换与过早放弃。该迁移依赖编码代理的自主多步规划、仓库级工件修改、工具副作用与执行反馈等独特条件，因此非可替代；候选结果具备强编码代理特异性。
- Confidence: 0.8

## strong_candidate: Bringing transparency and trustworthiness to loot boxes with blockchain and smart contracts

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113508
- Source outcome: Trustworthiness (of a loot box mechanism)
- Coding-agent outcome: 编码代理执行的可验证忠实性/可审计信任
- Decision: 该文是明确的设计科学研究（DSRF/Peffers），构建了智能合约算法和以太坊DApp原型并进行了评估；决策理论和Pedersen区块链采用模型对设计目标和区块链方案选择有实质性但中等强度的引导作用。最有力的结果候选是“战利品箱机制的可信性（可验证忠实执行）”，其源域含义高度特定于披露概率合规与玩家-厂商-监管关系，且向编码代理转移时对应“可验证忠实执行/可审计信任”这一强编码代理特异性设计目标，因此达到strong_candidate标准。
- Confidence: 0.78

## strong_candidate: Designing Online Virtual Advisors to Encourage Customer Self-disclosure: A Theoretical Model and an Empirical Test

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1962595
- Source outcome: intentions to self-disclose
- Coding-agent outcome: 开发者向编码代理的任务相关约束与意图披露意愿（持续、迭代的上下文披露）
- Decision: 该文属于'design_oriented_build_evaluate'：设计并实例化了带三类设计元素的虚拟顾问，并进行了受试者间实验评估。理论到设计的强度为strong：社会交换理论、Al-Natour和Benbasat的交互中心框架、言语行为理论被用于推导设计线索和披露意图的前因机制。最佳结果'intentions to self-disclose'被定量测量，其语境化为健康/皮肤护理中的敏感个人信息披露，具有情境特异性。向编码代理的迁移是well-justified：开发者对任务约束和意图的持续披露是编码代理自治、多步、仓库级操作和工具副作用下的关键设计目标，且源文的设计-感知-关系-披露机制可映射为'代理解释为何/如何利用用户披露的信息+表达性回应→透明/响应→信任/互依→更多披露'。因此达到strong_candidate标准。
- Confidence: 0.78

## strong_candidate: Designing for the future in the age of pandemics: a future-ready design research (FRDR) process

- Year/journal: 2021 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1863751
- Source outcome: perceived privacy / privacy preservation
- Coding-agent outcome: 权限边界合规与私有数据保护（编码代理的责任自主性）
- Decision: 本文为显式设计科学研究：提出FRDR流程指南并实例化疫情暴发分析系统，在评估中测度建模准确率、感知隐私、用户信心、可持续性等结果。理论到设计的映射为强：futures research和technology affordance直接导出具体设计指南。至少一个评估结果（隐私保护）具有领域构成性，并在编码代理转移中展现出强非可替代性：编码代理的自主工具使用与仓库副作用使“权限边界合规与私有数据保护”成为必要且可测的结果。因此为strong_candidate。
- Confidence: 0.78

## strong_candidate: Handling the Efficiency–Personalization Trade-Off in Service Robotics: A Machine-Learning Approach

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870391
- Source outcome: Preference estimation (user preference model for driving configurations)
- Coding-agent outcome: 开发者偏好保真度（Developer Preference Fidelity）
- Decision: 文章明确采用设计科学研究，构建并评估了一个基于DoL框架的LSTM构件；DoL框架、人本设计、效率-个性化权衡等理论/构念直接塑造了构件架构和动态权衡机制。偏好估计被量化评估且具有自动驾驶情境的操作化含义，并可迁移为‘开发者偏好保真度’这一编码代理相关设计目标；动态权衡处理虽只被数学命题评价，但其‘干预敏感的自主性校准’迁移依赖代理的多步、有副作用的仓库级行为，具备强非替代性。因此属于strong_candidate。
- Confidence: 0.78

## strong_candidate: Leveraging Multisource Heterogeneous Data for Financial Risk Prediction: A Novel Hybrid-Strategy-Based Self-Adaptive Method

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/16118
- Source outcome: Earlier prediction of financial risks
- Coding-agent outcome: 编码智能体轨迹早期的任务失败/缺陷风险预测
- Decision: 源论文是明确的设计科学研究（explicit_design_science），构建并评估了HSB_RS人工制品；机器学习偏差理论和ER规则均直接参与设计需求与机制推导，theory-to-design强度为strong；评估中“更早预测金融风险且性能稳定”是可量化的、领域构成性的结果，且可迁移为编码智能体特有的“轨迹早期任务失败/缺陷风险预测”，具有强编码智能体特异性与可辩护的机制迁移，因此作为strong_candidate。
- Confidence: 0.78

## strong_candidate: Providing more regular road signs infrastructure updates for connected driving: A crowdsourced approach with clustering and confidence level

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113443
- Source outcome: Road sign existence confidence level (time-aware confidence level)
- Coding-agent outcome: 证据支撑的代码变更存在置信度
- Decision: 该文属于'设计导向的构建-评估'研究：提出并实现了基于众包的云平台和路标整合算法，并用真实场数据进行了两个实验。理论到设计链条明确：贝叶斯推理和指数老化直接塑造了置信度计算公式，属于强理论驱动。最核心的被评估结果'路标存在置信度'是领域构成性的，其操作化依赖GPS噪声、摄像头误检/漏检、航向和路标半衰期。向编码代理迁移时，该机制可转化为'基于测试/执行正负证据和证据时效的代码变更存在置信度'，这一结果在静态IDE或普通聊天机器人情境下会失去意义，因此编码代理非可替代性较强，迁移强度为强。第一个候选结果最适合作为设计目标。
- Confidence: 0.78

## strong_candidate: Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063549
- Source outcome: Adversarial robustness (performance ratio robustness)
- Coding-agent outcome: 编码代理对对抗性指令/仓库上下文扰动的鲁棒性（性能比值）
- Decision: 来源论文属于明确的设计科学研究：以TTAT为内核理论推导两个元需求及具体设计原则，构建并评估了ARText系统。评估的核心结果‘对抗鲁棒性’通过性能比值和性能-扰动曲线在垃圾评论/垃圾邮件检测中操作化，具有预测分析决策场景的上下文特异性。该理论-设计机制可迁移至编码代理场景：将编码代理视为受对抗指令/仓库上下文影响的生成式代理，用源论文的同构评估-增强框架设计新鲁棒性目标，且该目标依赖编码代理的委托目标追求、仓库级上下文、工具副作用和概率性工件生成等条件，因此满足非替代性检验。
- Confidence: 0.78

## strong_candidate: Designing a Framework for Digital KYC Processes Built on Blockchain-Based Self-Sovereign Identity

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2021.103553
- Source outcome: Privacy (need-to-know and data minimization)
- Coding-agent outcome: 最小化上下文访问（Need-to-Know Context Minimization）
- Decision: 该文是明确的DSR构建-评估研究，设计了基于区块链SSI的eKYC框架并用专家访谈评价；SSI、need-to-know原则和数据最小化作为理论/原则在一定程度上指导了设计需求，因此theory-to-design强度为中等。隐私结果在源领域是情境化的（GDPR、金融身份、选择性披露），其need-to-know/数据最小化机制可转化为编码代理特有的'最小化上下文访问'结果，且该结果在静态IDE或聊天机器人场景中会失去意义，具备强编码代理特异性。因此整体为strong_candidate。
- Confidence: 0.78

## strong_candidate: Standardize or Let a Thousand Flowers Bloom? Interface Design Coordination between Software Platforms and Hosted Apps

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16484
- Source outcome: Grouping perception
- Coding-agent outcome: 开发者对编码代理与代码库/工作流的整合知觉（agent-repository coherence perception）
- Decision: 该论文是设计导向的构建与评估研究：开发并随机部署了八个版本的app界面以操纵三个理论驱动的设计属性。theory of basic Gestalts被明确用于推导设计原则（相似性、嵌入性、同步性）及对分组知觉的假设，trust transference和synergistic specificity用于推导下游使用行为。分组知觉在随机现场实验中被定量评估且具有平台生态情境化含义。向编码代理的迁移有明确机制：编码代理的自主多步执行、仓库副作用和动态人类委托使“整合知觉”和“委托深度”成为与静态IDE或普通聊天机器人不同质的编码代理特定设计目标。
- Confidence: 0.78

## strong_candidate: Designing Digital Platforms for Social Justice: Empowering End Users Through the Dataswyft Platform

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2024/18334
- Source outcome: end user data control (meta-requirement MR2; perceived control)
- Coding-agent outcome: 委托方对编码代理动作与数据流的控制权（delegator action/data sovereignty）
- Decision: 该文是明确的设计科学研究（explicit DSR），构建并评估了Dataswyft平台作为设计理论的例示；Fraser的异常正义理论对元需求和设计原则有强生成性作用；至少两个评价结果（个人数据控制、隐私安全）具有源域情境特异性，且可映射为编码代理特有的设计目标（委托方对代理动作/数据流的控制权、代理运行中的数据保密性），非静态IDE或普通聊天机器人可比。因此标记为强候选并纳入人工复审。
- Confidence: 0.78

## strong_candidate: Dynamic Bayesian Network–Based Product Recommendation Considering Consumers’ Multistage Shopping Journeys: A Marketing Funnel Perspective

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0277
- Source outcome: Identification of invisible psychological stages and latent interests (psychological dynamics identification)
- Coding-agent outcome: 编码体任务阶段透明性（任务进展阶段的可识别性）
- Decision: 源文明确以设计科学分类定位（Gregor and Hevner 2013），构建了MS-DBN人工物并做了大规模真实数据评估；营销漏斗理论直接导出隐阶段层、阶段转移和兴趣收敛约束，理论到设计的线索强。虽然主评估指标HR@10/NDCG@10是通用结果，但候选结果2“消费者心理阶段与潜兴趣的识别”是领域构成性的、经过可视化和统计检验的评估目标，并且其理论-设计机制可迁移为编码体任务阶段透明性：自主多步编码体存在被委派目标、阶段规划、执行反馈和人工监督等条件，去掉这些条件后目标失去意义。因此按整体决策规则判为strong_candidate。
- Confidence: 0.78

## strong_candidate: Fairness of Ratemaking for Catastrophe Insurance: Lessons from Machine Learning

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.1195
- Source outcome: Disparate impact against racial minorities and lower-income policy holders
- Coding-agent outcome: 多智能体编程贡献的公平风险/信用归属（fair risk/credit attribution among coding-agent contributions）
- Decision: 该文属于构建并评估人工制品的研究（设计出 Shapley value 风险附加费分配方法与 FAST-SV 算法），理论到设计的链接强（公理化方法、Shapley value、actuarial fairness 直接导出设计公理与唯一机制）；经验评估中的'对少数族裔/低收入保单持有人的系统性费率差异'是领域构成性结果，且其机制（次可加风险负担的公平分配）可映射为编码智能体场景中多智能体贡献的公平风险/信用归属，后者依赖仓库级副作用、多智能体协调与可执行产物等编码智能体特有条件。因此判定为 strong_candidate。
- Confidence: 0.78

## strong_candidate: Website Localization Strategies to Promote Global E-Commerce: The Moderating Role of Individualism and Collectivism

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2022/15542
- Source outcome: perceived website localization (PWL)
- Coding-agent outcome: 感知的仓库/项目本地化（perceived repository localization）
- Decision: 该文明确自述贡献于设计科学研究，使用consumer-company identification作为kernel theory推导三种网站本地化策略，并通过美中在线实验构建和评估了实验网站工件；理论到设计映射强(strong)，且被评估的核心结果perceived website localization具有情境特异性的跨国文化身份含义（contextualized）。将其迁移到编码智能体，可形成“感知的仓库本地化”这一智能体特定设计目标，依赖仓库级上下文、多步自主修改、可执行工件等核心智能体条件，移除智能体条件会实质改变结果定义、测量与设计机制，故为strong_candidate。
- Confidence: 0.78

## strong_candidate: Guided Diverse Concept Miner (GDCM): Uncovering Relevant Constructs for Managerial Insights from Text

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2020.0494
- Source outcome: Relevance of mined concepts to the managerial outcome Y / concept importance for conversion
- Coding-agent outcome: 行为概念对编码任务结果的引导相关性（outcome-guided relevance of agent behavior concepts）
- Decision: 该文属于设计导向的构建-评估研究：GDCM 算法是一个被构建并被系统评估的文本挖掘工件。原型理论、Gardenfors 概念空间等理论直接导出了算法的嵌入、多样性正则和分类损失设计，理论到设计链路强。评估中包含多个量化结果，其中“概念对管理结果 Y 的相关重要性”在源领域中被具体化为在线评论-转化场景和 Garvin 产品维度，属于领域情境化的结果。该结果可迁移为编码智能体“行为概念对任务结果的引导相关性”，依赖编码智能体的多步规划、工具副作用、测试反馈等独特条件；若替换为静态 IDE 或普通聊天机器人，该结果的定义、机制和测量都会实质性改变，因此编码智能体特异性强。整体符合 strong_candidate。
- Confidence: 0.78

## strong_candidate: Constructing continuity across the organisational culture boundary in a highly virtual work environment

- Year/journal: 2021 / Information Systems Journal
- DOI: 10.1111/isj.12293
- Source outcome: synthesis of symbolic and pragmatic components of organisational culture
- Coding-agent outcome: 代理-仓库规范综合（agent-repository normative synthesis）：编码智能体在自主多步代码修改中保持声明性项目规范与具体代码行为之间的连续性
- Decision: 该文是明确的行动设计研究（ADR），构建并评估了数字组织文化手册；ODT、符号-实践文化观、SECI、知识可视化和参与式设计共同导出DP1-DP3和工件特征，理论到设计的路径强。后续访谈和反馈循环定性评估了‘符号-实践文化综合/连续性’这一结果，其结果在高度虚拟组织文化领域中具有情境特异性。该机制可迁移为编码智能体的‘代理-仓库规范综合’：来源的连续性设计可转化为自主多步代理的规范工件设计，依赖代理的目标追求、仓库级上下文、工具副作用和异步工作等特征；若移除代理条件，候选结果会退化为普通规范检查或问答。因此为强候选。
- Confidence: 0.76

## strong_candidate: Augmenting Social Bot Detection with Crowd-Generated Labels

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1136
- Source outcome: social bot detection performance (precision, recall, F1, AUC)
- Coding-agent outcome: 基于评审反馈可信度加权的代理异常变更检测性能（识别需要干预的代理生成变更）
- Decision: 该文构建并评估了一个融合人群反馈的社交机器人检测系统（design_oriented_build_evaluate）；言语行为理论被直接用于设计特征矩阵和可信度加权机制（theory_to_design_strength=strong）；社交机器人检测性能是语境化结果，且其'言语行为加权的人群反馈'机制可迁移到编码代理评审反馈的加权与异常变更检测，形成强非替代性的编码代理设计目标。
- Confidence: 0.76

## strong_candidate: Feedback Loops in Machine Learning: A Study on the Interplay of Continuous Updating and Human Discrimination

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00853
- Source outcome: Algorithmic discrimination (gender gap in positive predictions/statistical parity; gender gap in false-negative error rates)
- Coding-agent outcome: 编码代理在持续更新中的选择性反馈歧视漂移
- Decision: 该论文属于'设计导向的构建与评估'：作者构建并运行了基于经验数据的持续更新ML仿真，并系统评估了算法歧视和经济效率两个结果。其设计机制由算法反馈回路、选择性标签和品味歧视等理论/构念实质性塑造（理论到设计强度为中等）。最优结果'算法歧视'在源领域具有领域构成性，因为其意义依赖于贷款决策中的选择性标签和受保护群体的信贷配给风险。向编码代理迁移时，选择性反馈/人类评审偏见机制可以对应到代理基于评审接受的代码变更进行持续学习的情境，形成'编码代理选择性反馈歧视漂移'这一强特异性的设计目标：移除代理的自主仓库操作和持续学习条件后，该目标不再成立。因此判定为强候选目标。
- Confidence: 0.76

## strong_candidate: When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0053
- Source outcome: Self-reported variety-seeking level / product variety level (measurement validity of Variety_Seeking)
- Coding-agent outcome: 代码变更多样性校准质量（Exploration Calibration Quality）
- Decision: 论文明确构建并评估了两套设计化框架（多样性寻求测量框架和个性化意外推荐框架），属于 build-and-evaluate 类型；多样寻求理论和意外性概念明确指导了设计要求和效用函数机制；被评估的一个结果（多样性寻求测量效度）具有领域情境特异性，且其理论-设计机制能够迁移到编码智能体特有的“代码变更多样性校准”目标，该目标依赖自主多步修改、仓库级上下文、工具副作用和测试反馈等智能体条件，而非静态IDE或普通聊天机器人所能替代。因此判定为强候选，但迁移部分为本文分析性推断，而非源论文声称。
- Confidence: 0.76

## strong_candidate: 1 + 1 > 2? Information, Humans, and Machines

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0305
- Source outcome: Active rethinking / reconsideration
- Coding-agent outcome: 开发者对编码智能体生成补丁的主动再思考与纠错率
- Decision: 该论文虽未使用正式设计科学标签，但确实构建并评估了一个理论驱动的干预系统（两阶段人机协作审批流程+机器解释呈现），属于design_oriented_build_evaluate。双过程推理理论被明确且直接地用于推导两个处理条件（信息复杂性和机器解释），理论到设计链条强。评价结果中‘主动再思考’被量化和机制性地识别，且其含义在小额贷款信贷特征情境下具有语境特定性。将其迁移到编码智能体场景时，可形成一个编码智能体特有的设计目标：通过大规模补丁与结构化变更理由激发人类开发者的系统2复查，识别生成式幻觉导致的跨依赖错误；这依赖于智能体的仓库级自主生成、工具副作用和概率性错误等独特条件，具有强非替代性。第二个候选（性别偏差缓解）迁移中等，不影响总体判断。
- Confidence: 0.76

## strong_candidate: Fake News and True News Assessment: The Persuasive Effect of Discursive Evidence in Judging Veracity

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17542
- Source outcome: Aggregate veracity judgment
- Coding-agent outcome: 开发者对编码智能体代码变更正确性的判断准确率（证据支持下的真实性判断）
- Decision: 该文采用实验方式构建并评估了话语证据这一干预，属于设计导向的构建-评估研究（非显式DSR但配置了实质干预）。理论驱动强：ELM和Reactance理论直接推导了证据非规范性、证据强度、启动批判思维等设计特征。评估结果中，聚合真实性判断、双向真实性、克服先前倾向都是情境化/领域构成性的量化结果。最有希望的迁移是将“话语证据支持的真实性判断”重新情境化为“开发者对编码智能体变更正确性的证据支持判断”，该迁移依赖编码智能体的自主多步修改、概率性错误生成、工具副作用和人类监督等独特条件，因此非可替代性较强。综合判断为strong_candidate。
- Confidence: 0.76

## strong_candidate: Incorporating the Time-Order Effect of Feedback in Online Auction Markets through a Bayesian Updating Model

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15324
- Source outcome: Trust
- Coding-agent outcome: 对编码智能体的校准信任与监督强度
- Decision: 该文实际构建并评估了一个理论驱动的贝叶斯更新信誉模型（design_oriented_build_evaluate），代表性启发式、信息不对称理论和EGII清晰塑造了模型设计（含时间顺序系数λ），属于strong theory-to-design。评估结果中价格溢价具有领域构成性，信任是情境化且有强编码智能体转移潜力；尤其是信任可转化为'编码智能体的校准信任与监督强度'，依赖自主多步执行、存储库副作用和测试反馈等编码智能体特有条件，满足非可替代性测试，因此判定为strong_candidate。
- Confidence: 0.75

## strong_candidate: Validating the coevolutionary principles of business and IS alignment via agent-based modeling

- Year/journal: 2021 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1801360
- Source outcome: Misalignment
- Coding-agent outcome: 意图-代码库对齐度（delegated-goal-to-repository alignment）
- Decision: 该论文构建并评估了一个ABM仿真人工物，属于design_oriented_build_evaluate；CAS理论和协同进化理论以及三条协同进化原则被明确用于指导ABM的行为规则设计，theory-to-design强度为strong；核心评估结果'Misalignment'是业务-IS对齐领域特有的构念，具有源领域构成性。将'业务域'映射为用户委托目标、'IS域'映射为代码库状态后，'意图-代码库对齐度'依赖编码代理的自主多步编辑、仓库级上下文和工具执行等专属 affordances，具有强编码代理特异性，因此整体判定为strong_candidate。
- Confidence: 0.75

## strong_candidate: Digital nudging for technical debt management at Credit Suisse

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2088413
- Source outcome: Technical debt levels (overall TD index and per-type TD index changes)
- Coding-agent outcome: 自主编码代理的技术债审慎度（TD-conscious autonomous code modification）/ 编码代理引入或遗留的技术债水平
- Decision: 该文是明确的DSR研究：设计并实现了一个TDM nudge（Tableau仪表盘+数据处理器），基于助推理论和六个心理效应构建了八个设计元素，并通过访谈、焦点小组、前后测问卷和一年后TD水平追踪进行了评估。TD水平（总体及四类TD指数变化）是领域构成性结果，其含义与度量完全依赖软件开发领域。该结果向编码代理的迁移具有较强非替代性：自主编码代理的多步规划、仓库规模上下文、工具副作用和自我纠错能力使'非约束性选择架构'可以嵌入代理决策循环，用以调节代理在快速交付与长期可维护性之间的now-vs-later权衡，并以仓库级TD指标直接观测。因此评为strong_candidate。
- Confidence: 0.75

## strong_candidate: Sensing the Future: A Design Framework for Context-Aware Predictive Systems

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00821
- Source outcome: Cost of forecasting errors (COST_FE)
- Coding-agent outcome: 自主代码修改后果预测误差的不对称代价（代价加权的误判成本）
- Decision: 论文明确采用设计科学研究方法，构建并评估了CAPS框架这一设计工件；理论到设计的链条清晰（Hevner DSR 和 Shmueli & Koppius 预测建模流程直接塑造了CAPS的步骤）；评估的核心结果“预测误差成本”具有高度的领域构成性，其计算依赖海洋船舶发动机备件售后市场的特定关系与运营参数；该结果可明确迁移为编码代理的“自主代码修改后果预测误差的不对称代价”，依赖自主多步规划、仓库级副作用、测试反馈等编码代理专属条件，因此构成强候选。
- Confidence: 0.75

## strong_candidate: Beyond Complements and Substitutes: A Graph Neural Network Approach for Collaborative Retail Sales Forecasting

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0773
- Source outcome: Product relation identification precision and comprehensiveness
- Coding-agent outcome: 仓库工件依赖关系识别的精确性与鲁棒性（dependency-relation identification robustness）
- Decision: 来源论文是显式的设计科学研究（computational design research / theory-guided design），明确构建了 CL4RSF/MS2RSF 工件并进行了系统实验评估；CCCDT 理论到需求再到解决方案的链路清晰（Table 1, Figure 1），理论-设计强度为 strong。在评估结果中，‘产品关系识别的精确性与全面性’具有领域构成性含义（零售消费选择与跨品类效应），并且到编码代理的转换成立：仓库工件依赖识别的鲁棒性/精确性是一个新的编码代理设计目标，其测量（精确率/召回率、跨运行一致性、伪依赖抑制）和机制（鲁棒性损失+对比损失引导图学习）都依赖编码代理的仓库级上下文、执行反馈和多步行动，移除代理条件后该结果的意义与测量发生根本变化，因此 coding-agent specificity 为 strong。综合判定为 strong_candidate。
- Confidence: 0.75

## strong_candidate: Redefining profit metrics for boosting student retention in higher education

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113493
- Source outcome: Net savings / profit of a retention campaign (Maximum Profit, MP)
- Coding-agent outcome: 代理动作/生成变更的选择性验证与人工审查的净价值(预期净收益)
- Decision: 论文构建并评估了一个新的利润驱动学生辍学预测性能度量(design_oriented_build_evaluate);该度量直接源自利润驱动分类框架和CLV/SLV理论构念,并显式引入γ、σ以刻画教育情境;评估了留校活动的净收益(MP)和最优目标比例α;其中净收益是高等教育/学生保留情境下的域构成性结果。将其机制映射到编码代理:可用预期净价值决定对代理生成的代码变更进行选择性验证/人工审查,这依赖代理的自主多步行动、仓库规模上下文、工具副作用和概率性错误生成等特征,移除这些条件后度量失去意义,因此是强非替代性迁移。整体为strong_candidate。
- Confidence: 0.74

## strong_candidate: Combining Crowd and Machine Intelligence to Detect False News on Social Media

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16526
- Source outcome: Early detection of false news
- Coding-agent outcome: 代理错误轨迹的早期检测与提前中止/交接
- Decision: 该文是设计导向的构建-评估研究（CAND/CLNAM），以智慧众包和在线去抑制效应为明确设计前提，并在Weibo/Twitter上定量评估了虚假新闻检测、早期检测和抗操纵鲁棒性。其中“早期检测”结果在源领域具有领域构成性，其机制——用稀疏的弱群体信号经贝叶斯可信度聚合尽早推断真伪——可迁移为编码代理的“错误轨迹早期检测与提前中止/交接”设计目标，依赖代理的多步规划、工具副作用和反馈自纠错等独特条件，非替代性较强。因此判定为强候选。
- Confidence: 0.74

## strong_candidate: Cross-Lingual Cybersecurity Analytics in the International Dark Web with Adversarial Deep Representation Learning

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16618
- Source outcome: Cross-lingual hacker asset detection performance (accuracy, F1, AUC)
- Coding-agent outcome: 低资源编程语言/框架下的跨语言安全敏感代码检测与自主修复效果
- Decision: 该文明确采用 computational design science paradigm，构建并评估了 CLHAD/ADREL 这一新 IT 人工物；GAN/对抗学习与跨语言知识迁移等命名理论/理论构念直接塑造了 ADREL 的架构和预期迁移机制，theory-to-design 为 strong。核心结局“跨语言黑客资产检测性能”以 Accuracy/F1/AUC 定量评估，且其含义依赖暗网黑客资产、低资源语言和黑客行话误译等源领域特有情境，属于 domain_constitutive。向编码智能体迁移时，可将对抗域不变表示机制用于低资源编程语言/框架的安全敏感代码识别与自主修复，结局的测量依赖多步编辑、测试反馈与自我纠错，去除智能体条件会实质改变结局定义和测量方式，因此 coding-agent specificity 为 strong，整体达到 strong_candidate。
- Confidence: 0.74

## strong_candidate: Explaining Data-Driven Decisions made by AI Systems: The Counterfactual Approach

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16749
- Source outcome: Decision-level explanatory faithfulness
- Coding-agent outcome: 编码代理行为的最小因果反事实可解释性
- Decision: 论文构建并评估了反事实解释框架/EBE算法这一设计型人工制品；理论构念'反事实因果解释'直接决定了'因果且不可约'的设计要求和基于成本偏好的搜索机制；评估结果中最具迁移价值的产出是'决策层面的解释忠实性'。该产出对编码代理可重述为'代理代码修改的最小因果反事实可解释性'：编码代理的多步自主行动、仓库级依赖、工具副作用和概率性生成使这一解释问题具有强非替代性。因此评定为强候选。
- Confidence: 0.74

## strong_candidate: Building data management capabilities to address data protection regulations: Learnings from EU-GDPR

- Year/journal: 2023 / Journal of Information Technology
- DOI: 10.1177/02683962221141456
- Source outcome: Common ground between legal and data management practice
- Coding-agent outcome: 自主代码修改的合规要求可追溯性（regulatory-requirement traceability of autonomous code modifications）
- Decision: 该文是显式DSR研究（遵循Peffers等人过程，工件为GDPR数据管理能力模型），RBV与RCM概念直接塑造了能力模型的结构（资源类型、能力分组、CR到CCR的翻译机制）；模型经过多家企业演示、专家访谈和Likert量表评估。最有前景的被评估结果是法律与数据管理实践之间的“共同理解”，在GDPR问责、同意、删除等情境下具有情境化含义。该机制可迁移为编码agent的“自主代码修改的合规要求可追溯性”：由自主多步修改、仓库级上下文、工具副作用与概率性生成等agent条件驱动，静态IDE或聊天机器人无法替代，因此判定为strong_candidate。
- Confidence: 0.74

## strong_candidate: Pricing in Nonconvex Markets: How to Price Electricity in the Presence of Demand Response

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1139
- Source outcome: make-whole payments (MWP)
- Coding-agent outcome: 隐藏人工修正负担（make-whole burden of coding agents）
- Decision: 该文是设计导向的build-and-evaluate研究：构建了PBE-A/PE-A定价规则这一数学优化工件，并用IEEE RTS-96实验进行了量化评估。竞争均衡理论和市场设计需求（效率、个体理性、预算平衡、无嫉妒）强有力地转化为设计原理与模型目标（最小化make-whole payments、惩罚式稳定），theory-to-design强度为强。核心结果make-whole payments是电力市场/非凸市场特有的域构成性结果，其测量和利益相关者关系高度依赖该领域。将其转移为编码代理的'隐藏人工修正负担'时，代理的委托目标追求、自主多步迭代、可执行相互依赖产物等条件使该结果在非代理环境下显著改变，因此具备强编码代理特异性和可辩护的机制转移。综合判断为strong_candidate。
- Confidence: 0.74

## strong_candidate: Showcase: A Data-Driven Dashboard for Federal Criminal Sentencing

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00796
- Source outcome: Transparency
- Coding-agent outcome: 自主代码变更的可溯源透明度
- Decision: 该文是显式设计科学研究（DSR），构建了ShowCase仪表盘并通过Venable等框架的专家访谈进行评价。理论（penal theory、organizational context theory、social bonds theory、triangulation design theory）明确且强有力地指导了界面结构、特征与预期机制。评估的透明度结果在量刑领域具有领域构成性意义，并且可以强有力地迁移为编码代理特有的“自主代码变更可溯源透明度”设计目标：该结果的定义、测量与风险都依赖编码代理的自主多步行动、工具副作用和仓库级影响，静态IDE或普通聊天机器人无法替代。因此判定为strong_candidate。
- Confidence: 0.74

## strong_candidate: Supporting Community First Responders in Aging in Place: An Action Design for a Community-Based Smart Activity Monitoring System

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/18446
- Source outcome: Community first responders’ situational awareness (SA)
- Coding-agent outcome: 编码智能体的代码库情境感知（Codebase Situational Awareness）
- Decision: 这是一项明确的行动设计研究（ADR），构建并评估了SEMS人工制品；以情境感知（SA）理论为生成框架，从三个SA层次推导出四条设计原则，理论到设计证据充分。核心结果'社区急救者的情境感知'是源领域特定的（独居老年人远程监测、非专业志愿者、误报风险、家庭传感器物理环境），其意义和操作化高度依赖源领域。该结果可迁移为编码智能体特有的代码库情境感知目标，利用智能体的自主多步规划、仓库范围上下文、工具反馈闭环和变更副作用管理等能力，理论机制（DP1-DP4）映射为智能体的感知、理解、预测设计原则，且若替换为静态IDE或普通聊天机器人则该设计机制失去意义。故判定为强候选。
- Confidence: 0.74

## strong_candidate: Responsible cognitive digital clones as decision-makers: a design science research study

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2073278
- Source outcome: Precision of imitation / donor–clone correspondence (DP0 Turing principle)
- Coding-agent outcome: 开发者偏好保真度（Developer Preference Fidelity）
- Decision: 该文是明确的 DSR 研究，使用 DSRM 构建了 Pi-Mind agent，并通过 proof of concept、proof of value、proof of use 进行了评估；设计原则 DP0–DP3 由图灵测试、数字孪生、认知克隆、启发式与偏见等理论构造直接生成（理论到设计链明确，至少为 moderate）。最佳结果候选“供体-克隆一致性/模仿精度”是领域构成性结果，且可映射为编码代理的“开发者偏好保真度”，该映射依赖自主多步规划、仓库级修改、概率性错误生成和动态人机委派等编码代理特有条件，非静态 IDE 或普通聊天机器人可替代。因此判定为 strong_candidate / target_match=true。
- Confidence: 0.73

## strong_candidate: A Prescriptive Analytics Framework for Optimal Policy Deployment Using Heterogeneous Treatment Effects

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15684
- Source outcome: Expected total utility from prescriptions (HTE-EST utility, compared with ATE and uplift modeling)
- Coding-agent outcome: 预算约束下的编码代理干预部署净效用（agentic intervention deployment utility）
- Decision: 论文构建并评估了一个处方分析框架（design_oriented_build_evaluate），潜在结果框架和 CATE/HTE 理论直接塑造了 HTE-EST 的设计与估计机制（theory_to_design_strength=strong）。主要被评估结果'预算约束下处方策略产生的期望总效用'在献血/推荐营销案例中有领域特定的收益-成本操作化（contextualized）。将其迁移到编码代理时，可形成'预算约束下编码代理干预部署净效用'这一候选目标，其机制依赖代理的自主多步执行、仓库级修改、工具副作用和测试反馈等条件，替换为静态IDE/聊天机器人后机制与测量均瓦解，因此具有强编码代理特异性。整体满足强候选规则。
- Confidence: 0.72

## strong_candidate: Assessing the Unacquainted: Inferred Reviewer Personality and Review Helpfulness

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/14375
- Source outcome: future review helpfulness (predicted)
- Coding-agent outcome: 早期痕迹驱动的代理委派权限（Delegation Warrant from Early Traces）
- Decision: 该文明确以设计科学视角构建 IT 人工物（深度学习人格推断模型 + 集成预测模型），Big Five 人格理论及知识分享/说服力/意见领袖机制清晰指导了特征选择与预测模型设计，理论到设计的连接为强；评估结果包括 Yelp 评论有用性这一情境化结果。将其‘从早期痕迹预测未来有用性’的设计模式迁移到编码代理场景，可形成编码代理特有的‘早期痕迹驱动的委派权限’设计目标，该目标依赖代理的自主多步执行、仓库级副作用、动态人机委派等核心条件，因此非替代性较强。
- Confidence: 0.72

## strong_candidate: From conflicts and confusion to doubts: Examining review inconsistency for fake review detection

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113513
- Source outcome: Fake OCR detection performance (accuracy, precision, recall, F-score)
- Coding-agent outcome: 代理工作真实性/可信度检测（检出不可靠、虚假或‘貌似正确实则错误’的代理产出）
- Decision: 该文实际构建并评估了包含三类评审不一致性特征的虚假评论检测系统（design_oriented_build_evaluate）；Truth-Default Theory、态度-行为一致性理论和泄漏理论对不一致性特征的类型学与设计有清晰但非正式的塑造作用（moderate）；被评估的结果是领域情境化的虚假评论检测性能；该结果可通过‘不一致性作为真实性信号’机制迁移到编码代理，识别代理产出的虚假/不可靠内容，且该迁移依赖编码代理的多步自主性、工具副作用和概率生成等独特条件，非替代性较强。
- Confidence: 0.72

## strong_candidate: Improving intention to back projects with effective designs of progress presentation in crowdfunding campaign sites

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113573
- Source outcome: Intention to back a project
- Coding-agent outcome: 继续授权/认可自主编码代理工作的意愿（delegation continuation intention）
- Decision: 该文构建并评估了模拟众筹网页中进度条设计变体，属设计导向的构建-评估研究；S-O-R、运动效应理论、视觉搜索理论等将设计特征（动态、颜色、额外信息）具体映射到用户感知和意向，theory-to-design明确；评价结果为定量测量。其中“支持意向”在众筹中具有领域特定含义，可经S-O-R机制迁移为“继续授权编码代理工作的意向”，该结果依赖编码代理的自主多步执行、工具副作用和动态委托等独特条件，因此构成强候选。
- Confidence: 0.72

## strong_candidate: Inferring multi-stage risk for online consumer credit services: An integrated scheme using data augmentation and model enhancement

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113611
- Source outcome: multi-stage credit risk (grace/delinquency/default)
- Coding-agent outcome: 编码智能体行为后果的多阶段风险分级与分级干预
- Decision: 该文明确以设计科学研究框架定位，构建并评估了多阶段信用风险画像方案（explicit_design_science）；Big Five人格理论与SHAP/博弈论对特征设计、模型增强和可解释模块有可追踪的设计作用（moderate）；核心结果'多阶段信用风险推断'在信贷领域具有领域构成性含义，且可转化为编码智能体特有结果'行为后果的多阶段风险分级与分级干预'，该转化依赖自主多步执行、工具副作用和人工监督/中断等编码智能体条件，非静态IDE或普通聊天机器人可替代，因此判定为strong_candidate。
- Confidence: 0.72

## strong_candidate: Reversing a relationship spiral: From vicious to virtuous cycles in <scp>IT</scp> outsourcing

- Year/journal: 2021 / Information Systems Journal
- DOI: 10.1111/isj.12309
- Source outcome: Inter-organisational trust
- Coding-agent outcome: 人机协作中的信任校准与委托螺旋状态
- Decision: 该文是设计导向的'构建-评估'研究：作者设计了CSD干预（协作式流程再设计+协作式KPI）并通过行动研究和系统动力学仿真评估其效果；理论（系统动力学增强回路、信任理论）明确指导了干预设计，theory-to-design强度为强；评估的'组织间信任'结果在源领域具有情境化操作化（信任与供应商投资空间、微观管理、激励错配形成特定螺旋），并且可映射到编码代理的'信任校准与委托螺旋'这一强代理特定结果，机制迁移可辩护。因此达到strong_candidate。
- Confidence: 0.72

## strong_candidate: <scp>Context‐aware</scp> user profiles to improve media synchronicity for individuals with severe motor disabilities

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12337
- Source outcome: Support communication across a range of conversational participants, both familiar and unfamiliar (Design Requirement 5 / DR5)
- Coding-agent outcome: 熟悉度校准的自主性(familiarity-calibrated autonomy)
- Decision: 本文是显式设计科学研究(DSRM),构建并评估了融入情境感知用户画像的AAC系统原型。MST虽然主要用于事后论证设计原则,但对媒体能力(速度、符号集、可排练性、适应性)到设计原则的映射清晰,故theory-to-design为中强。评价产出包括量化速度改进和定性设计需求达成;DR5'支持与熟悉/不熟悉沟通伙伴交流'在源领域是domain-constitutive,且向编码智能体转移为'熟悉度校准的自主性'具有强编码智能体特异性:依赖委托目标追求、多步规划、仓库级副作用等条件。因此为strong_candidate。
- Confidence: 0.72

## strong_candidate: Disclosure decisions and the moderating effects of privacy feedback and choice

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113717
- Source outcome: Disclosure Intention
- Coding-agent outcome: 透明反馈下的编码代理授权意愿（delegation/access authorization willingness）
- Decision: 源论文属于设计导向的构建与评估：基于正义理论设计并实例化了隐私反馈功能，在YouH原型中操纵反馈与选择权，并用PLS和MGA评估了披露意愿等结果。正义理论到设计特征存在明确的可追溯链路，属于strong。披露意愿在移动电商隐私语境下具有情境化含义，且可被重新定义为编码代理中的授权意愿；该转移依赖代理的自主多步执行、仓库级访问和真实环境副作用等编码代理特有条件，因此具有强非替代性。综合判断为strong_candidate。
- Confidence: 0.72

## strong_candidate: Incorporating FAT and privacy aware AI modeling approaches into business decision making frameworks

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113715
- Source outcome: Coverage (dataset coverage under accountability)
- Coding-agent outcome: 可靠操作覆盖率（confident task coverage / abstention behavior）
- Decision: 该文属于design-oriented build-evaluate：构建并实例化了基于FAT框架的可解释AI/ML亲和力预测模型，并在隐私受限数据集上进行了系统评估（RMSE基准、覆盖率、透明性变量数、分区公平性一致性）。FAT/Shin-Park概念模型被直接用于推导模型选择（GLM）、数据分区（公平性）和覆盖率/准确率权衡（问责性），theory-to-design强度为强。评估结果中‘覆盖率’‘透明性’‘公平性’均具有来源域特定操作化，且可分别映射至coding agent的‘可靠操作覆盖率/弃权行为’‘行动计划透明性’和‘跨代码库一致性鲁棒性’，其中‘覆盖率’的转移机制最强、最依赖agent的自主多步执行与测试反馈。因此整体判定为strong_candidate。
- Confidence: 0.72

## strong_candidate: scenario modeling for government big data governance decision-making: Chinese experience with public safety services

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2022.103622
- Source outcome: GBDG problem identification (speed and detailed presentation of problems)
- Coding-agent outcome: 编码智能体的仓库问题识别完备性
- Decision: 该文明确采用设计科学研究范式，构建了模型驱动的GBDG场景元模型和基于ABC理论的实例化机制，并在两个真实公共安全案例中评估了问题识别、方案设计和效果感知等结果。ABC理论对实例化机制有清晰的设计作用，理论到设计的联系强。最佳候选结果“GBDG问题识别”在源域具有情境化含义，且可映射为编码智能体在仓库中系统识别根因和约束的问题识别完备性；映射依赖编码智能体的自主多步规划、仓库规模上下文、工具副作用和测试反馈等条件，去除这些条件后结果不再成立，因此具有强编码智能体特异性。故整体判定为strong_candidate。
- Confidence: 0.72

## strong_candidate: A Theory-Driven Deep Learning Method for Voice Chat–Based Customer Response Prediction

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1196
- Source outcome: customer response prediction performance
- Coding-agent outcome: 编码代理委托任务早期成功/失败预测（delegated coding task outcome prediction）
- Decision: 源论文属于设计导向的构建-评估研究：构建了 DSDL 深度学习方法并进行了大规模实证评估；期望不一致理论、信息/属性满意度理论和动态累积满意度理论被明确用于推导设计需求与机制（Table 1），理论与设计关联强。其评估的核心结果“客户响应预测性能”具有邀请-到店领域的情境化操作定义。该结果可迁移为编码代理的“委托任务早期成功/失败预测”：期望不一致理论的多步动态差异机制可映射到代理计划-执行-测试反馈循环，且该机制依赖编码代理特有的自主多步执行、仓库变更和测试反馈等条件，非静态IDE或通用聊天机器人可替代。因此判定为目标匹配的强候选。
- Confidence: 0.72

## strong_candidate: How AI-Based Systems Can Induce Reflections: The Case of AI-Augmented Diagnostic Work

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16773
- Source outcome: Machine-induced reflection depth / reflective practice (reflection growth modes)
- Coding-agent outcome: 智能体引发的人类开发者代码变更反思深度
- Decision: 该文不是正式DSR论文，但实际构建了ML CDSS原型和两阶段反思实习场，并对其交互效果进行了多源评估，属于design_oriented_build_evaluate。反思实践理论、认知失调理论和双环学习理论对‘先个人判断、后ML冲突输入’的设计机制有清晰但非完全形式化的指导作用，故理论到设计强度为moderate。核心结果‘机器引发的反思深度’通过言语协议定性评估，并且在医学诊断任务中具有领域特定操作化，属contextualized。将该机制迁移到编码智能体场景时，agent自主生成冲突方案、执行测试并产生仓库级副作用，使开发者在合并前产生挑战/深度失调式反思，测量和机制均依赖智能体特有的自主多步、可执行产物和测试反馈条件，coding-agent特异性为strong。因此该论文是强候选。诊断准确率、自我感知能力等结果为辅助候选，迁移强度较低。
- Confidence: 0.72

## strong_candidate: Learning not to take the bait: a longitudinal examination of digital training methods and overlearning on phishing susceptibility

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2021.1931494
- Source outcome: Phishing susceptibility (mock phishing test scores)
- Coding-agent outcome: 编码代理对欺骗性或注入式指令的易感性（'不上钩'能力）
- Decision: 该文属于设计导向的构建-评估研究：作者构建了数字反钓鱼培训干预（规则式、正念式、对照）并加入过度学习操作，随后用邮件识别测试和两轮模拟钓鱼邮件进行纵向评估。正念理论、过度学习/技能保持理论和双过程理论均明确塑造了培训设计并产生了可检验的因果机制。最重要的结局'钓鱼易感性'在源域中是领域构成性的，且其设计机制可类推为编码代理对注入式/欺骗性指令的'不上钩'能力，依赖代理的自主工具调用、仓库级上下文和副作用行动等独特条件，因此具有强编码代理特异性。反应偏向（过度谨慎）也是一个高潜力的编码代理校准结局。整体判断为strong_candidate。
- Confidence: 0.72

## strong_candidate: Integrated Decision Support for Disaster Risk Management: Aiding Preparedness and Response Decisions in Wildfire Management

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0118
- Source outcome: Risk control under low-probability high-consequence scenarios (tail risk mitigation)
- Coding-agent outcome: 自主编码代理的低概率高影响失败控制（agentic tail-risk control）
- Decision: 该论文属于明确的设计科学研究：明确引用设计科学范式并提炼设计原则，构建了DRM分析框架及乌拉圭野火管理实例化（预测+规范模块），并通过基线对比、VSS、10折交叉验证进行评估。理论到设计的联系强：Lookahead approximation（Powell 2019）、概率风险评估和期望后悔（Szego 2002）直接塑造了模型结构、风险约束和设计原则。评估结果中，对低概率高后果情景的尾部风险控制具有领域构成性，且可迁移为编码代理特有的'自主多步仓库修改的低概率高影响失败控制'，该迁移依赖编码代理独特的自主规划、仓库级上下文、工具副作用和概率性错误生成等条件，非替代性检验通过。因此判定为强候选。
- Confidence: 0.72

## strong_candidate: Proactive Resource Request for Disaster Response: A Deep Learning-Based Optimization Model

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0125
- Source outcome: Average percentage of fulfilled future demands
- Coding-agent outcome: 前瞻性代码需求预覆盖率
- Decision: 源论文明确属于计算设计科学研究（自述computational genre of design science research并提出设计原则），构建了CNM-TPP+PRR的深度学习预测与随机优化方法，并用真实数据（2021河南洪灾微博需求）和仿真进行评估，build-and-evaluate成立。理论到设计强度为moderate：剥夺成本理论和时间点过程理论明确塑造了CSD学习目标、指数成本函数、贪心算法和前瞻性请求设计。被评估结果'未来需求前瞻性满足比例'是情境化的（灾难响应中的非平稳需求、运输能力约束、生命攸关），并能通过'预测未来代码需求事件+在有界行动预算内前瞻性执行预防性动作'的机制迁移为编码代理特定的'前瞻性代码需求预覆盖率'；该结果依赖代理的自主多步规划、仓库级上下文、工具执行与测试反馈，静态IDE/聊天机器人不可替代，因此判为strong_candidate，target_match=true。
- Confidence: 0.72

## strong_candidate: Qualitative Cusp Catastrophe Multi-Agent Simulation Model to Explore Abrupt Changes in Online Impulsive Buying Behavior

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00832
- Source outcome: Sudden/abrupt changes in group-level online impulsive buying (OIB) behavior
- Coding-agent outcome: 多智能体编程团队中不安全/不合规代码修改的级联突变风险
- Decision: 该文构建并评估了基于突变论+QSIM+ABM的多智能体仿真模型，属于设计导向的构建-评估研究；突变论、QSIM、社会影响理论等直接塑造了模型设计，理论到设计强度为强。评估的群体OIB突变结果具有领域构成性。最佳候选结果（群体OIB突变）可迁移为多智能体编程场景中'不安全代码修改的级联突变风险'，依赖编码智能体的自主多步规划、工具副作用、测试反馈和智能体间协调，非静态IDE或通用聊天机器人可替代，因此满足编码智能体非替代性。
- Confidence: 0.72

## strong_candidate: An Empirical Study of Strategic Opacity in Crowdsourced Evaluations

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17441
- Source outcome: Allocation of effort toward legitimate vs. illegitimate activities (effort ratio)
- Coding-agent outcome: 评价博弈鲁棒性：编码智能体在“真实任务改进”与“博弈评价机制”之间的努力分配
- Decision: 该文通过随机现场实验和受控实验实现并评估了众包评价中的战略模糊策略，属于design_oriented_build_evaluate；战略模糊理论（Ederer et al. 2018）明确指导了不透明评价规则的设计（theory-to-design moderate）；核心结果“合法/非法努力分配”在源领域有众包投票操纵的特定操作化（contextualized），并能迁移为编码智能体的“评价博弈鲁棒性”，依赖自主多步执行、测试反馈、仓储修改等智能体专属条件，因此满足strong_candidate条件。投票操纵发生率作为第二候选同样有力；参与率为通用结果，不构成迁移。
- Confidence: 0.72

## strong_candidate: And No One Gets the Short End of the Stick: A Blockchain-Based Approach to Solving the Two-Sided Opportunism Problem in Interorganizational Information Sharing

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0065
- Source outcome: Information Sharing Intention (High-Sensitivity Data)
- Coding-agent outcome: 委托者授予编码智能体高敏感性仓库上下文访问权的意愿
- Decision: 该文是明确的DSR研究（DSRM, Peffers et al. 2007），构建并实例化了区块链工件，三条设计原则由交易成本经济学中的机会主义（信息窃取和信息操纵）直接推导，理论-设计联系强。评价产出包含经定量测量的信息分享意向（尤其高敏感数据），其含义在机床租赁领域被具体化为对敏感生产数据泄露与操纵风险的缓解，属于contextualized。将该产出迁移到编码智能体场景可形成'委托者授予编码智能体高敏感性仓库访问权的意愿'，该结果依赖编码智能体的代理目标追求、仓库级上下文、工具使用副作用等非替代性条件，且源设计机制（私有数据集合+非可逆函数+联合治理）可映射为沙箱化访问、可验证执行摘要和联合审批策略。迁移强度为strong，因此判定为strong_candidate。
- Confidence: 0.72

## strong_candidate: Design Principles for Information Categorization Quality in Crowdsourced Crisis Mapping Platforms

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/16610
- Source outcome: Information categorization quality (plausibly accurate categorization)
- Coding-agent outcome: 任务解读合理性（plausible task interpretation / plan alignment）
- Decision: 该文是显式设计科学研究：以sensemaking为kernel theory推导四项设计原则并实例化模板，通过三项实验定量评估分类质量（无ground truth下的合理性一致性）。分类质量在危机地图场景中具有领域构成性（受害者RFH、专家基线、一线救援行动）。其设计机制可迁移为编码代理的‘任务解读合理性’：代理面对模糊request时提取需求线索并聚合issue/测试/日志等上下文，形成结构化任务报告，再开展多步修改；移去代理条件会使该结果失去定义与测量基础。因此符合strong_candidate。
- Confidence: 0.72

## strong_candidate: Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0379
- Source outcome: NumPhoto / NumFace (photo-based self-disclosure)
- Coding-agent outcome: 开发者向编码代理披露高敏感性上下文（high-sensitivity context disclosure）
- Decision: 该文是设计导向的构建-评估研究（无正式DSR标签）：在真实约会平台实施短暂照片共享UI，并开展大规模随机田野实验与在线实验。理论-设计关联为中等强度：社交隐私担忧框架/CPM直接塑造了短暂共享的机制（自动消失、防下载/转发），并作为中介机制被检验。评估结果包括受试者披露个人照片数量（含人脸）、匹配数和接收者消息数，均为定量测量。最有希望的转移是'开发者对编码代理的高敏感性上下文披露'：若代理上下文采用短暂共享设计，可降低开发者对数据收集/传播/身份滥用的担忧，从而缓解代理因缺乏上下文导致的冷启动。该结果对编码代理具有强特异性，因为代理有持久记忆、工具副作用和生成可执行工件的能力；删除这些条件会基本改变设计机制。因此保留为strong_candidate供人工复核。
- Confidence: 0.72

## strong_candidate: HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0202
- Source outcome: Interpretability of hierarchical contextual situations
- Coding-agent outcome: 编码代理分层情境的粒度化透明度（Granular Contextual Situation Transparency for Coding Agents）
- Decision: 来源论文是构建并评估HyperCARS人工制品的build-and-evaluate工作；设计的每一步（双曲空间、层次聚类、松耦合）均由双曲几何、情境层级观和松耦合原则推导，theory-to-design为强；解释性结果用SHAP/IDS在原始上下文变量上量化评估，是情境化设计目标。转移到编码代理时，可将‘分层情境可解释/透明’再概念化为‘人类监督者可理解的多粒度任务情境路径’，依赖代理的委派目标、自主执行和仓库副作用等独特条件，移除代理条件后机制与度量均失效，因此具备强coding-agent特异性。
- Confidence: 0.72

## strong_candidate: RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17339
- Source outcome: Adversarial robustness (operationalized as evasion rate reduction under RL-RO, with FPR constraint)
- Coding-agent outcome: 编码代理对仓库上下文注入的对抗鲁棒性（adversarial robustness against repository-context injection）
- Decision: 该文是明确的计算设计科学研究（computational design science），构建并实例化了RADAR工件；RO和RL理论直接产生r-VAC与RL-RO的设计特征，理论到设计的链条清晰且强；评估结果（逃避率降低、FPR约束）在恶意软件对抗攻防领域具有领域构成性含义，且基于功能性保持的顺序攻击测量。最佳候选结果‘对抗鲁棒性’可经由minimax对抗博弈与顺序攻击仿真机制转移为编码代理特有的‘仓库上下文注入下的对抗鲁棒性’，该结果在删除编码代理条件后会失去定义、机制和测量意义，故编码代理特异性为强。第二个候选结果FPR作为监督假中断率提供支持性转移，特异性中等。总体为强候选。
- Confidence: 0.72

## strong_candidate: A Deep Learning Approach for Recognizing Activity of Daily Living (ADL) for Senior Care: Exploiting Interaction Dependency and Temporal Patterns

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15574
- Source outcome: HL-ADL sequence quality (ABLD/Accuracy)
- Coding-agent outcome: 自主开发会话的子任务边界保真度（Subtask-Boundary Fidelity of Autonomous Development Sessions）
- Decision: 来源论文明确采用计算设计科学范式，构建并严格评估了分层的 ADL 识别框架（explicit_design_science，build_and_evaluate=true）。理论到设计：ADL 层级框架直接指导三阶段架构和'分解为可解释中间特征'的设计原则，强度为 moderate。结果：HL-ADL 序列质量（ABLD/Accuracy）是量化评估结果，且其操作化（活动块边界、持续时间）具有领域特定含义（contextualized）。编码代理迁移：将 ADL 层级机制映射为'将委派目标分解为子任务/操作并评估代理动作序列的块级结构保真度'，依赖自主多步规划、仓库副作用、测试反馈等代理专属条件，删除代理条件后该结果无定义，故 coding-agent specificity 为 strong，迁移机制可辩护。因此整体判定为 strong_candidate，target_match=true。
- Confidence: 0.7

## strong_candidate: A dynamic simulation approach to support the evaluation of cyber risks and security investments in SMEs

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113580
- Source outcome: Damage from Attacks / cyber losses
- Coding-agent outcome: 自主编码行为导致的不可逆副作用/安全事件损失暴露
- Decision: 该文是设计导向的构建-评估研究：作者构建了SMECRA工具并应用于三个SME场景。System Dynamics和NIST框架对模型变量、反馈结构和调查问卷具有直接的生成性作用，属强理论到设计映射。评价结果'网络攻击损失'在源域中通过攻击率、检测/缓解能力、脆弱性感知和反馈环被操作化，具有语境特异性。将其重新定义为'自主编码行为导致的安全损失暴露'，依赖代理的自主工具使用、仓库副作用和概率性产物生成，且移除代理条件后机制会消失，因此构成强编码代理特定转用。故选为strong_candidate。
- Confidence: 0.7

## strong_candidate: Designing Payment Contracts for Healthcare Services to Induce Information Sharing: The Adoption and the Value of Health Information Exchanges (HIEs)

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/14809
- Source outcome: First-best solution (socially optimal HIE adoption, provider efforts, and patient switching behavior)
- Coding-agent outcome: 多智能体编码终局结果问责一致性（episode-level outcome accountability alignment across coding agents）
- Decision: 该文属于'design_oriented_build_evaluate'：设计并分析了一种新的EBP支付合同，并通过严格的博弈论命题和数值分析评估其效果。理论到设计的联系是强的：道德风险/激励理论和外部性理论直接导出EBP的多边性和顺序依赖特征。评估结果中，'first-best solution'是情境化的核心设计目标，且能够通过机制迁移转化为编码智能体特有的'终局结果问责一致性'目标，该目标依赖多智能体协调、可执行产物和测试反馈等编码智能体条件，不具备静态IDE或聊天机器人可替代性。因此判定为strong_candidate。
- Confidence: 0.7

## strong_candidate: Dynamic, Multidimensional, and Skillset-Specific Reputation Systems for Online Work

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2020.0972
- Source outcome: Identification of 'nonperfect' workers / prediction of underperformers
- Coding-agent outcome: 编码代理静默失败风险（silent-failure risk）的动态识别与预警
- Decision: 该文构建并评估了HMM-W2V声誉框架，属于设计导向的搭建-评估研究；三个设计原则明确源于声誉通胀/归因/静态性这三个构造，并有Schmidt & Hunter正态分布作为聚合机制的理论依据，theory-to-design为moderate。评估结果中，“nonperfect worker识别”是一个有情境化操作化的结果（依赖在线劳动市场的评分膨胀和动态技能），向编码代理迁移时具有强非替代性：代理的概率生成、自主多步执行、测试反馈等条件使得“静默失败风险识别”成为一个新的、可观察的编码代理设计目标。因此整体判断为strong_candidate。
- Confidence: 0.7

## strong_candidate: A Design Theory for Energy and Carbon Management Systems in the Supply Chain The Quest for Innovation in Information Systems Research: Recognizing, Stimulating, and Promoting Novel and Useful Knowledge

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00725
- Source outcome: Energy and carbon measurement
- Coding-agent outcome: 编码代理动作级能耗与碳足迹的核算与透明报告
- Decision: 论文是显式设计科学研究，构建了ECMS设计理论并在四个组织两轮实例化与评估；设计需求、组件和设计原则直接由信息流分类、功能可供性和Gregor & Jones设计理论塑造；评价产出‘能源与碳测量’和‘环境敏感决策与实践’均具有领域特定含义。将‘能源与碳测量’机制迁移到编码代理的动作级能耗/碳足迹核算，依赖代理自主多步工具执行与仓库副作用，具备强非可替代性，因此为strong_candidate。
- Confidence: 0.7

## strong_candidate: Discovering Emerging Threats in the Hacker Community: A Nonparametric Emerging Topic Detection Framework

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15642
- Source outcome: Emerging threat detection effectiveness
- Coding-agent outcome: 自主编码代理新发失败/风险模式的早期检测
- Decision: 该文是明确的设计科学研究，构建并评估了NPETD框架；HDP与贝叶斯因子检验作为命名理论构念直接塑造了设计要件与机制；评价结果中包含网络安全领域特有的新兴威胁检测效能（quantitatively measured, domain_constitutive）。将该机制迁移到编码代理，可形成自主编码代理新发失败/风险模式早期检测这一代理特有设计目标，且去除代理条件后其定义、数据流、机制和测量均发生实质变化，因此判定为strong_candidate。
- Confidence: 0.7

## strong_candidate: Peer-to-Peer Loan Fraud Detection: Constructing Features from Transaction Data

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16103
- Source outcome: Fraud detection performance (accuracy, recall, precision, F score, AUC)
- Coding-agent outcome: 基于行为痕迹的自主编码代理违规/恶意行为检测性能
- Decision: 该文是明确的设计科学研究（explicit design science），使用设计科学方法论构建了P2P借贷欺诈检测特征工件，并将欺诈三角理论及其扩展（能力、诚信、机会）直接转化为五类行为特征设计，理论到设计的证据明确且强度为强；评估环节使用两个真实平台数据集对多个机器学习分类器进行了定量评估，评估指标虽然是通用分类指标，但在P2P借贷欺诈检测场景中具有情境化含义（标签来自平台黑名单、特征针对借款过程）。将其转移到编码代理时，可提出“基于行为痕迹的自主编码代理违规/恶意行为检测性能”这一设计目标：源论文的机制（从交易数据构造行为特征以检测欺诈）可类比为从代理工具调用轨迹构造行为特征以检测偏离委托目标的行为，且该依赖代理的多步工具使用、仓库副作用和权限边界，非一般IDE或聊天机器人可替代，因此编码代理特异性强。虽然需要将人类欺诈概念重构为代理-意图一致性（边界条件扩展），但机制迁移可辩护，整体候选成立。
- Confidence: 0.7

## strong_candidate: Lead complementor involvement in the design of platform boundary resources: A case study of BMW's onboard apps

- Year/journal: 2023 / Information Systems Journal
- DOI: 10.1111/isj.12449
- Source outcome: Enhancement of boundary resource design (API abstraction, app release management, SDK contribution routines)
- Coding-agent outcome: coding-agent边界资源设计质量（工具/权限/上下文/反馈边界）
- Decision: 该文是设计导向的行动研究，实际构建并评价了BMW车载app平台的boundary resources改进（API抽象、发布管理工具、SDK贡献流程/指南），符合design_oriented_build_evaluate。Lead user theory和boundary resources model对设计机制有明确的生成性作用，theory-to-design强度为strong。评价的‘enhanced boundary resource design’是平台生态领域特有结果，不是通用绩效。将该理论-设计机制映射到coding-agent的工具/权限/上下文/反馈边界资源设计，可形成依赖agent自主执行、真实仓库副作用和人类监督交接的定制化设计目标，非替代性检验通过。因此列为strong_candidate，留待人工复审。
- Confidence: 0.7

## strong_candidate: Motion Sensor–Based Fall Prevention for Senior Care: A Hidden Markov Model with Generative Adversarial Network Approach

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2023.1203
- Source outcome: Fall prevention success (protective-device triggering with sufficient lead time)
- Coding-agent outcome: 自主编码代理的灾难性动作预防（在不可逆破坏发生前以足够提前时间触发干预）
- Decision: 该文明确采用计算设计科学范式，构建并评估了HMM-GAN+逻辑回归的跌倒预防构件；HMM、熵GAN和EM等命名理论/构造明确指导了构件设计（状态转移矩阵、代理似然、EM实例）；核心评估结果'以足够提前时间触发保护装置以预防跌倒'是领域构成性结果。将该结果迁移到编码代理时，可形成'在不可逆代码破坏发生前以足够提前时间触发干预'的设计目标，该目标依赖代理的自主多步执行、真实环境副作用、产物可执行性和概率性错误生成等特征，非静态IDE或普通聊天机器人所能替代，故为强候选。
- Confidence: 0.7

## strong_candidate: Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/18573
- Source outcome: Semantic correspondence of PICO text fragments (F1_BERT/BERTScore)
- Coding-agent outcome: 意图语义保真度（语义对应机制的编码代理版本）
- Decision: 源文是明确的design science研究：构建并评估FastSR；compositionality theory（及sensemaking）明确导出DR1-DR4并映射到具体设计组件；评估结果中至少一个结果是domain_constitutive/contextualized且有强编码代理非替代性，即PICO片段语义对应机制可转移到编码智能体的意图语义保真度。因此判定为strong candidate。
- Confidence: 0.7

## strong_candidate: Real-Time Sales Data, Streamer Improvisation, and Sales Performance: Evidence From Live Stream Selling

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18627
- Source outcome: Data-driven improvisation in promotional, linguistic, and presentational pace tactics
- Coding-agent outcome: 实时反馈驱动的策略即兴质量（adaptive plan improvisation）
- Decision: 该论文是一个面向设计的构建-评估型现场实验：在淘宝直播上实现了'提供实时销售数据仪表盘'这一IT工件设计，并随机化评估其效果。理论（即兴理论、双过程理论）实质性塑造了设计机制（实时数据替代缺失的受众反馈，促成主播即兴调整策略），虽然未明示设计原则，但属于中等强度。被评估的中介结果'主播销售战术即兴'（催促、情感词、语速、直播时长）具有领域情境化操作化；将该机制转移至编码智能体可形成'实时反馈驱动的策略即兴质量'这一编码体特定结果，其定义、测量和机制在静态IDE或通用聊天机器人中均会失效，具有强非替代性。因此满足强候选模式。
- Confidence: 0.7

## strong_candidate: A Prescriptive Analytics Method for Cost Reduction in Clinical Decision Making

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/14372
- Source outcome: cost reduction in clinical decision making (expected total cost)
- Coding-agent outcome: 自主代码变更的期望总成本（含验证投资成本与缺陷/返工期望成本）
- Decision: 论文构建并评估了ICSL方法（显式设计科学），理论（Prospect Theory, Regret Theory）实质性地塑造了包含投资决策和概率性成本的方法设计；被评估的结果“临床决策总成本/成本降低”是情境化的，且其机制可映射到编码代理的验证投资与代码变更接受决策，形成具有强代理特异性的设计目标。因此为strong_candidate。
- Confidence: 0.68

## strong_candidate: Explore for a day? Generating personalized itineraries that fit spatial heterogeneity of tourist attractions

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103557
- Source outcome: Tourist utility (u)
- Coding-agent outcome: 用户目标对齐的代理任务效用
- Decision: 该文构建并实地评估了一个两阶段启发式行程推荐算法（设计导向的构建-评估研究）；命名理论（边际效用递减、审美疲劳）通过式(2)明确塑造了效用目标函数和停留时间优化这一核心设计特征，因此理论-设计链接为中等；主结果'游客效用'以配对t检验进行量化评估，其操作化依赖旅游景点空间异质性、出入口和时间窗，属于情境化结果；将其迁移为'用户目标对齐的编码代理任务效用'时，依赖编码代理的仓库级上下文、多步规划和带副作用的工具使用等独特条件，非静态IDE或普通聊天机器人可替代，因此构成强候选。
- Confidence: 0.68

## strong_candidate: Tun-OCM: A model-driven approach to support database tuning decision making

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113538
- Source outcome: Traceability/auditability of DB tuning decisions (provenance of tuning decisions)
- Coding-agent outcome: 自主编程代理修改的可审计溯源与责任追踪
- Decision: Tun-OCM属于设计导向的构建-评估工作：明确构建本体概念模型并通过真实ENEM场景测试。CM-OPL/CM Task Ontology/ISO 10007等理论直接塑造了模型的配置识别、版本控制和变更控制设计，理论到设计强度为强。模型产生的可审计溯源结果是在数据库调优领域情境化的定性评估结果，具有领域特定操作化。将其迁移到编码代理场景时，可形成'代理修改的可审计溯源与责任追踪'这一编码代理特有的设计目标：代理的自主多步操作和仓库副作用使该溯源需求比手动开发更关键，因此编码代理特异性强。综合判断为strong_candidate。
- Confidence: 0.68

## strong_candidate: An interface between natural language and abstract argumentation frameworks for real-time debate analysis

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113694
- Source outcome: Traceable and transparent argumentation chain (traceability/transparency of the debate)
- Coding-agent outcome: 可追溯、可质疑（contestable）的编码代理决策论证链
- Decision: 该文属于设计导向的构建-评估研究：作者实际构建了ADM模型、AIPA工具和WebAIPA应用，并通过两个案例进行了质性评估。理论到设计的联系强：Dung的抽象论证框架和bipolar框架直接决定了以攻击图、扩展语义、状态判定为核心的设计机制。被评估的结果'论据链可追溯透明'具有情境化含义，且该结果可迁移为编码代理特有的'可追溯、可质疑的决策论证链'：该迁移依赖代理自主多步规划、工具副作用、测试反馈与人类监督等编码代理专属条件，替换为静态IDE或普通聊天工具后该结果失去意义。因此总体判定为strong candidate。
- Confidence: 0.68

## strong_candidate: How Do Recommender Systems Lead to Consumer Purchases? A Causal Mediation Analysis of a Field Experiment

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1074
- Source outcome: Consideration set size (breadth)
- Coding-agent outcome: 候选方案集广度（candidate solution set breadth）
- Decision: 该文采用设计导向的构建-评估模式：实际部署并随机实验评估了协同过滤推荐系统。考虑集理论、搜索成本理论和卷入-承诺理论提供了从推荐系统到购买结果的因果中介机制，虽未严格形式化为设计原则，但理论对中介机制和测量有清晰引导，故theory-to-design为moderate。核心评估结果‘考虑集广度/深度’是消费者决策领域特有构念，且可迁移为编码agent的‘候选方案集广度/评估深度’，该迁移依赖编码agent的多步自主规划、仓库级上下文、工具调用与测试反馈等非替代性条件，因此为strong/promising中的strong_candidate。
- Confidence: 0.68

## strong_candidate: My Real Avatar has a Doctor Appointment in the Wepital: A System for Persistent, Efficient, and Ubiquitous Medical Care

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2022.103706
- Source outcome: Telepresence
- Coding-agent outcome: 代理工作区临场感（agent-workspace telepresence）
- Decision: 本文使用显式设计科学研究方法（design science），构建并实验评估了 wepital/真实替身原型；Theory of Affordances 和媒体同步性/自然性理论明确指导了设计需求与特征，并评估了 telepresence 等结果。Telepresence 作为源结果具有医疗虚拟门诊的语境化含义，并可经由 affordance/media-design 机制转化为编码代理工作区临场感（开发者对代理在仓库/执行环境中的多步、有副作用操作的可感知在场），该转移在概念上依赖自主多步迭代、工具副作用、人机监督等编码代理独特条件，因此 target_match=true。
- Confidence: 0.68

## strong_candidate: Repairing Integrity-Based Trust Violations in Ascription Disputes for Potential E-Commerce Customers

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15679
- Source outcome: Perceived integrity of the accused seller
- Coding-agent outcome: 编程代理的诚信信任修复（agent integrity trust repair in ascription disputes）
- Decision: 论文采用设计导向的构建-评估模式：提出了基于归因理论和认知感觉框架的两种信任修复干预（再归因+稳定性归因；披露实质性补偿），并通过四个实验进行评估。理论到设计的链接是显式的（理论推导出具体回应策略）。评估结果中“对卖家诚信的感知”是领域构成的，在C2C电商在线评价和归因争议中具有特定含义和操作化。该结果向编程代理的转移是强非替代性的：编程代理的自主执行、工具副作用和概率性错误使‘用户将失败归因为代理欺骗’这一现象成为核心问题，而来源理论可直接指导代理的再归因和稳定性归因设计。因此为strong_candidate。
- Confidence: 0.68

## strong_candidate: Speaking things into existence: Ontological foundations of identity representation and management

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12330
- Source outcome: Institutional identity of digital institutional entities
- Coding-agent outcome: 智能体生成工作产物的机构身份/制度性落地（institutional grounding of agent-generated artifacts）
- Decision: 文章虽以Research Opinion形式发表，但实际构建并比较了两个概念建模产物（图4与图7），属于design_oriented_build_evaluate。Searle言语行为理论、Frege指称理论、Habermas三世界观直接塑造了机构实体、分类规则、标识符等建模设计，theory-to-design强度为strong。最核心的被评估结果——机构身份——在源域中是domain_constitutive的，且可强映射到编码智能体场景：agent自主生成的代码产物需要制度性身份以获得可再识别性、权利/权限边界和跨上下文可归责性；该迁移依赖编码智能体的委托、多步自主、仓库级副作用等独特条件，非静态IDE或普通聊天机器人可替代。故总体判定为strong_candidate。
- Confidence: 0.68

## strong_candidate: Ambivalence Is Better than Indifference: A Behavioral and Neurophysiological Assessment of Ambivalence in Online Environments

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17123
- Source outcome: Perceivable difference in ambivalence for ambivalent vs. indifferent information (H5)
- Coding-agent outcome: 混合信号与缺失信号的可区分度（反馈表征保真度）
- Decision: 该论文构建并评估了一种双变量信息表征干预（bivariate representation），属于设计导向的构建-评估研究；其设计直接源于'态度双变量结构'理论，且负性偏差理论和拓展-建构理论参与了假设推导，理论-设计链路清晰。至少两个被评估结果（矛盾/冷漠可感知差异、矛盾信息下的购买决策）在源领域具有情境化含义，并能通过双通道反馈表征设计迁移到编码智能体的混合验证信号场景，迁移机制具体且不可替代性高。因此该论文作为编码智能体设计目标的理论驱动设计科学来源是强候选。
- Confidence: 0.68

## strong_candidate: Designing Conversational Dashboards for Effective Use in Crisis Response

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00801
- Source outcome: Transparent interaction
- Coding-agent outcome: 开发者对自主编码代理工作状态的透明交互（可审查性）
- Decision: 文章是明确的 DSR，以 TEU 为核心理论并结合可供性和 enactive learning 推导出 MR/DP；构建并实例化了对话式危机仪表盘，并用 271 人行为实验评估了透明交互及其对效率和有效性的影响。透明交互虽是 TEU 通用构念，但在危机应对和普通公众情境中被具体化；将其向编码代理迁移时，可形成‘开发者对自主编码代理工作状态的透明交互（可审查性）’这一编码代理特异设计目标，机制来自 TEU 的适应与学习，测量可类比导航路径比，且去除编码代理条件会实质改变该目标。因此判定为 strong_candidate。
- Confidence: 0.68

## strong_candidate: Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17171
- Source outcome: Misclassification cost (MC)
- Coding-agent outcome: 代码变更的模块归属错误成本
- Decision: 该文属于显式设计科学研究（论文自我定位为计算型设计科学），构建并评估了DeepIA这一人工制品。三类专家知识和层次约束作为命名构念直接驱动了动态行业表示与层次分配的设计。评估结果包括领域具体的“误分类成本”（基于NAICS行业和有效税率），该结果可被重新实例化为编码智能体场景下的“代码变更模块归属错误成本”，其定义、机制和度量都依赖编码智能体特有的仓库规模自主修改、依赖敏感上下文和工具副作用，非静态IDE或通用聊天机器人可替代。因此判定为strong_candidate。
- Confidence: 0.68

## strong_candidate: Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1191
- Source outcome: recommendation diversity distribution alignment (Jensen-Shannon divergence)
- Coding-agent outcome: 编码代理制品/行动维度多样性对齐度
- Decision: 源论文是显式设计科学论文，构建并评估了DLDE-MAB推荐框架；理论到设计链条强（社会认知自我调节理论/目标设置SMART理论直接塑造了多样性约束和项目表征）；评估结果包含领域具体化的多样性分布对齐（JSD）和健康结果指标。其中多样性分布对齐可迁移到编码代理的“制品/行动维度多样性”目标，且依赖编码代理的自主规划、仓库级制品生成和工具副作用等非替代性条件，因此构成强候选。
- Confidence: 0.68

## strong_candidate: A field experiment on ISP training designs for enhancing employee information security compliance

- Year/journal: 2025 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2024.2359460
- Source outcome: Actual ISP compliance behavior (spear-phishing click behavior)
- Coding-agent outcome: 编码智能体对嵌入式指令注入/任务劫持的抵抗能力（prompt-injection resistance）
- Decision: 该文属于设计导向的建构-评估研究：实质性再设计了三种ISP培训干预并在现场实验中评估；转移培训模型、PMT和GDT清晰指导了培训设计中的威胁/威慑论证操纵；实际钓鱼点击行为是领域构成性的量化结局。该结局可类比迁移为编码智能体的提示注入抵抗，涉及智能体在仓库规模上下文中自主使用工具并产生副作用的独特条件，非静态IDE或普通聊天机器人可比，因此构成强候选。
- Confidence: 0.68

## strong_candidate: Different but the Same? An Event-Driven Approach to Determine Probabilities of Data Duplication

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18178
- Source outcome: Reliability of determined duplicate probabilities
- Coding-agent outcome: 事件归因的代码工件重复概率校准性（calibrated event-attributed duplication probability for code artifacts）
- Decision: 来源论文为设计导向的构建-评估研究（构建事件驱动重复检测概率模型并在7个数据集上系统评估），理论到设计链条明确：概率论和数据质量/实体表示理论直接形成概率空间与事件模式设计，Fellegi-Sunter框架作为避免错误假设的需求来源。评估结果包括重复概率的可靠性（校准性）和跨数据集迁移的F1，其中“事件归因的重复概率可靠性”在源领域具有语境特定含义。该机制可分析性地映射到编码智能体：将代码工件对视为实体对，将并行分支复制、跨模块重实现等agentic事件视为重复相关事件，设计可校准的事件归因代码重复概率。该迁移依赖编码智能体独有的仓库级、多步骤、可执行工件修改等条件，静态IDE或普通聊天机器人无法替代，因此判定为strong_candidate。
- Confidence: 0.68

## strong_candidate: Probing Digital Footprints and Reaching for Inherent Preferences: A Cause-Disentanglement Approach to Personalized Recommendations

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0181
- Source outcome: inherent preference-oriented recommendation
- Coding-agent outcome: 意图忠实性（intent-faithful code action）
- Decision: 该文构建并评估了DISC推荐方法（因果图+解纠缠表征学习），显式引用设计科学与kernel theory；理论到设计关联强。主要评估结果‘固有偏好导向推荐’具有领域情境化定义，并通过反事实干预测试在真实数据上量化验证。该结果可迁移为编码智能体的‘意图忠实性’设计目标：智能体在多步仓库任务中需区分用户真实意图与显著性/从众线索，这与静态IDE或普通聊天机器人有本质区别，非替代性测试成立，因此为强候选。
- Confidence: 0.68

## strong_candidate: Authority and consensus in group decision making with fallible individuals

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113670
- Source outcome: Expected opportunity loss (EOL) from group erroneous decisions
- Coding-agent outcome: 代码变更接受架构的期望机会损失（Code-change Acceptance EOL）
- Decision: 作者构建了ABM仿真模型，将有界理性个体错误聚合到 authority/consensus × star/tree/full 组织结构中，并以量化EOL评价；EOL在源情境中被具体化为遗漏/委托错误的机会损失并受时间折现影响。该理论-设计机制可映射到编码智能体：LLM的"有界理性式"幻觉导致补丁级委托/遗漏错误，组织可通过权威审批 vs 多智能体共识及通信拓扑控制错误率，以最小化代码变更接受的期望机会损失；该目标依赖自主生成可执行代码、仓库级上下文和测试反馈等智能体条件，移除后不成立。
- Confidence: 0.66

## strong_candidate: Bidding on a Peer-to-Peer Energy Market: An Exploratory Field Study

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1098
- Source outcome: allocative efficiency (balancing of local renewable supply and demand)
- Coding-agent outcome: 多智能体编码任务分配/协调效率
- Decision: 来源论文属于设计导向的构建-评估研究（设计、实现并实地部署了区块链P2P能源交易平台），采用双向拍卖等市场设计理论来塑造核心机制（理论-设计强度为中等），并评估了分配效率/本地供需平衡这一领域构成性结果。将该机制映射到多智能体编码任务分配可形成强编码智能体特异性的设计目标：以拍卖方式匹配任务与智能体能力/负载，减少冲突与重复劳动。虽然来源论文没有显式使用设计科学研究标签，且理论-设计链接并不完全显式，但完整模式成立，因此判定为strong_candidate。
- Confidence: 0.66

## strong_candidate: Avoiding the Diffusion of Responsibility in Social Networking Groups: A Field Experiment on Responses to Online Help-Request Referrals

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00781
- Source outcome: Endorsing
- Coding-agent outcome: 多智能体编码协作中的公开责任声明/承诺可见性
- Decision: 论文属于设计导向的构建-评估研究：在微信SNG中设计并实施真实HRR干预，使用TMR强驱动设计变量（请求个性化、关系亲近度），并定量评估感知责任、帮助和背书行为。其中最可迁移的结果是背书行为：其意义依赖群组公共可见性与多责任主体，可映射到多智能体编码协作中的公开责任声明/承诺可见性，且该结果在静态IDE或普通聊天机器人中无法成立，具有强编码智能体特异性。TMR的I-E和I-P链接机制可转化为显式任务指派和角色所有权设计原则。整体形成强候选。
- Confidence: 0.66

## strong_candidate: From Detractors to Enhancers: Harnessing the Power of Ad Customization for User Engagement on Media Websites

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00907
- Source outcome: Ad quantity customization choice (AQC option selected)
- Coding-agent outcome: 智能体自主权限边界选择行为（autonomy-boundary choice）
- Decision: 文章实际构建并现场评估了AQC界面（design_oriented_build_evaluate），心理赋权理论以中等强度连接到了AQC的设计特征与预期作用机制；其中AQC选择行为（无广告/减少广告/常规广告）是在该广告内容领域中构成性、被定量评估的结果，并可通过“机制转移”映射到编码智能体特有的自主权限边界选择结果，具有强非替代性。因此符合强候选标准。
- Confidence: 0.66

## strong_candidate: Privacy Concerns and Data Donations: Do Societal Benefits Matter?

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/16853
- Source outcome: Data donation decision (Amount of data donation)
- Coding-agent outcome: 编码代理仓库访问授权（delegation access scope）
- Decision: 该文虽非正式DSR，但明确构建并评估了两个数据捐赠应用原型，属于设计导向的构建-评估；隐私计算和共情-利他理论强驱动了应用特征（隐私控制、社会效益线索）的设计；评估结果是数据捐赠量，其情境化含义依赖医学/COVID-19数据捐赠的健康敏感性与社会收益；该理论-设计机制可迁移为编码代理的权限委托决策，且依赖编码代理的自主多步执行、仓库规模上下文和副作用等特征，因此为强候选。
- Confidence: 0.66

## strong_candidate: A comparison of features in a crowdsourced phishing warning system

- Year/journal: 2021 / Information Systems Journal
- DOI: 10.1111/isj.12318
- Source outcome: Adherence to warning recommendations
- Coding-agent outcome: 对编码智能体风险警告的校准式批准/遵循
- Decision: 该研究构建了一个模拟众包反钓鱼警告系统并进行了438人的受控实验，属于design-oriented build-and-evaluate；自动化信任与众包理论明确导出四个警告设计特征并假设其对遵循、焦虑、判断准确率的影响，theory-to-design为strong；‘遵循警告建议’作为评估结果具有领域情境化含义，且其‘准确率披露影响自动化信任与依赖’的机制可迁移到编码智能体场景——开发者面对自治、多步、有副作用的代码修改时需要对智能体风险警告形成校准式批准/干预，该结果在静态IDE或普通聊天机器人中不成立，因此具备强编码智能体特异性。
- Confidence: 0.65

## strong_candidate: An assisted approach to business process redesign

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113749
- Source outcome: Interactive integration of domain knowledge (DO4)
- Coding-agent outcome: 自主代码修改中的校准式领域知识检查点（calibrated domain-knowledge checkpoints）
- Decision: 论文为显式设计科学研究，构建了 ABPR 概念、参考架构和原型并完成多轮评估；Parasuraman 自动化层级模型和 Reijers & Limam Mansar 重构模式对设计特征（AL1-4、模式支持）有可追踪的生成作用，theory-to-design 为 moderate；DO4‘领域知识交互整合’作为设计目标被专家访谈系统评估，且在 BPR 语境下具有领域特定含义；其向编码智能体的迁移（校准式领域知识检查点）依赖代理式多步规划、仓库副作用、概率性错误生成等独特条件，移除编码智能体后机制和测量都会改变，因此 coding-agent specificity 为 strong，整体达到 strong_candidate 标准。
- Confidence: 0.65

## strong_candidate: Can ChatGPT Perform a Grounded Theory Approach to Do Risk Analysis? An Empirical Study

- Year/journal: 2024 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2024.2415772
- Source outcome: Data saturation result (emergence of no new subcategories; 'No appropriate label' occurrences)
- Coding-agent outcome: 自主代码代理的探索/测试饱和判断（Exploration and Test Saturation）
- Decision: 源论文构建并评估了一个设计化干预（ChatGPT执行的扎根理论方法，含提示模式和评价指标），属于design_oriented_build_evaluate；系统扎根理论明确指导了步骤、提示和评价指标设计，theory-to-design为strong；数据饱和检验是一个领域构成性且被混合评估的结果，且可向编码代理的'探索/测试饱和判断'迁移，非替代性强（依赖自主多步探索、执行反馈和停止决策）。因此满足strong_candidate条件。最佳候选为数据饱和检验结果。
- Confidence: 0.65

## strong_candidate: A strategic decision-making architecture toward hybrid teams for dynamic competitive problems

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113490
- Source outcome: Team performance / quality of partitioned decisions
- Coding-agent outcome: 多编码代理任务分解的协调质量（decomposition coherence / partition quality）
- Decision: 该文属于 design_oriented_build_evaluate：实际构建了混合团队战略决策架构并进行了计算评估。理论到设计链路强：博弈论/微分博弈直接形成自适应决策机制，MPC 提供滚动求解，LSTM 提供数据驱动奖励模型。被评估的团队绩效（分区质量）在源域中有情境化操作化（Starcraft II 对抗性奖励、黑箱目标失配），且可映射为多编码代理任务分解协调质量这一编码代理特定设计目标；去掉编码代理条件会改变结果定义和测量，因此非替代性成立。综合判断为 strong_candidate。
- Confidence: 0.64

## strong_candidate: Social Collaboration Analytics Framework: A framework for providing business intelligence on collaboration in the digital workplace

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113587
- Source outcome: Actionable insights into collaboration and the use of ECS
- Coding-agent outcome: 编码智能体协作行为的可解释可操作洞察（human-observable agentic trace insight）
- Decision: 该文是明确的设计科学研究（DSR），构建并评估了 Social Collaboration Analytics Framework 及其实例化仪表板；理论到设计的联结为中等强度（workspace awareness 维度构成 SCAF 的分析透镜，ECS user typology 指导指标选择）；至少一个被评估的结果（对 ECS 协作的可操作洞察）在源领域具有情境化/领域构成式意义；将其转移到编码智能体的“人类可观察的智能体行为洞察”在机制和测量上依赖 agentic coding 条件，非可替换为静态 IDE 或普通聊天机器人。因此满足 strong_candidate。
- Confidence: 0.64

## strong_candidate: A framework for applying <scp>ethics‐by‐design</scp> to decision support systems for emergency management

- Year/journal: 2023 / Information Systems Journal
- DOI: 10.1111/isj.12350
- Source outcome: Precaution
- Coding-agent outcome: 自主代码变更的前置风险遏制（precautionary containment before irreversible coding-agent actions）
- Decision: 本文属于design-oriented build-evaluate：构建了ethics-by-design框架并在S-HELP中实例化，且通过三个情景和问卷进行了总结性评价。理论到设计的链接是显式的：伦理价值（源自VSD、ethics-by-design、ethical impact assessment等）被转换为系统设计原则（Table 2）。Precaution/Transparency作为被评价的伦理价值在应急管理领域具有领域构成性或强情境化意义。向编码智能体迁移时，Precaution机制（行动前评估风险/历史知识与建模）可转化为'自主代码变更的前置风险遏制'，这是一个依赖智能体自主多步执行、真实仓库副作用、测试反馈等条件的设计目标，移除agentic条件后该目标会消失。因此判定为strong_candidate。
- Confidence: 0.64

## strong_candidate: Conversation Analytics: Can Machines Read Between the Lines in Real-Time Strategic Conversations?

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0415
- Source outcome: Next-quarter earnings surprise (standardized analyst forecast error, SAFE)
- Coding-agent outcome: 编码代理任务失败的隐性预测性信号（agent hidden-failure predictability）
- Decision: 该文属于design_oriented_build_evaluate：构建了回避度和不连贯度两个ML测量工具并进行了验证和应用。理论到设计的连接为moderate：Crawford-Sobel信息传递理论、管理层模糊化假设、欺骗心理学等明确了构造的操作化方向（主题不匹配、句间不连贯）和预期结果机制。评估结果（下一季度盈余惊喜）是领域构成性的，且可迁移为编码代理隐式故障预测目标，依赖代理的多步执行、概率性文本生成和人类监督交接等独特条件，非替换为静态IDE或普通聊天机器人所能保持。因此判定为strong_candidate。
- Confidence: 0.64

## strong_candidate: Customer Acquisition via Explainable Deep Reinforcement Learning

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0529
- Source outcome: attention weight task relevance / intrinsic explainability of RL decisions
- Coding-agent outcome: 前瞻性操作聚焦可验证性（validated forward-planning focus of autonomous code modifications）
- Decision: 该文属于 build-and-evaluate 型设计研究：提出并实例化 DRQN-attention 模型，用真实数字银行数据评估。Q-learning、POMDP/DRQN 和注意力机制等命名理论/构念直接塑造了模型结构与预期机制，属于强理论到设计映射。评估结果中，“注意力权重任务相关性/内在可解释性”可被界定为情境化结果，“注意力导出的广告渠道选择有效性”是领域构成性结果；两者均可通过机制迁移映射到编码智能体的“前瞻性操作聚焦可验证性”和“注意力导出修改目标/工具选择有效性”。该迁移依赖编码智能体的仓库级上下文、自主多步迭代、工具副作用和测试反馈等非替代性条件，因此构成强候选。
- Confidence: 0.64

## strong_candidate: Activity awareness, social presence, and motivation in distributed virtual teams

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2020.103425
- Source outcome: Activity awareness (perceived awareness of the activities of others)
- Coding-agent outcome: 编码代理活动意识（Agent Activity Awareness）——人类监督者对自主编码代理当前工作状态的感知
- Decision: 该文属于design_oriented_build_evaluate：在实验性协作系统中构建并配置了一个活动状态指示器UI元素，并在受控实验中评价其对感知活动意识、社会临场感、工作意愿和忠诚的影响。Group process theory明显用于推导设计假设（H1-H6），形成从理论到设计特征再到结果机制的完整链条。最有力的结果是感知活动意识：该构念在分布式虚拟团队情境中被具体操作化，且可转化为编码代理场景中的“代理活动意识”，依赖代理自主多步规划、工具使用和异步工作等独特条件，去除这些条件后测量和机制不再成立，故判定为strong_candidate。
- Confidence: 0.62

## strong_candidate: Autoencoders for strategic decision support

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113422
- Source outcome: Dimension-level feedback
- Coding-agent outcome: 智能体代码变更的维度级偏差画像（可审查性）
- Decision: 论文属于构建-评估型研究：提出并实现了自编码器战略决策支持框架，并通过四种实验评估。最优区分度/同侪常态理论虽非正式设计科学，但直接导出‘是否/如何/多大程度偏离同侪’的粒度反馈需求，自编码器重建误差作为实现机制。核心结果‘维度级反馈’在战略决策领域具有情境化含义，可映射为编码智能体的‘变更集维度级偏差画像’，依赖仓库级上下文、多步带副作用变更、概率性错误、人类监督/交接等代理特有条件；移除代理条件后结果与测量会失效，因此是强候选。
- Confidence: 0.62

## strong_candidate: First, Do No Harm: Predictive Analytics to Reduce In-Hospital Adverse Events

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1990619
- Source outcome: Number of adverse events prevented (N. AEs Prevented)
- Coding-agent outcome: 可预防的智能体诱发损害（agent-induced harms）的减少
- Decision: 源文是显式设计科学研究（explicit DSR），构建并评估了SALT这一预测图模型。设计由患者安全文献中的潜在贡献因素、IOM的AE定义等理论性构造驱动，理论到设计链条明确（GLMM对应潜在因素、ARMA-ARCH对应演化轨迹、多任务学习对应多类AE）。At least one evaluated outcome（可预防AE数量）是领域构成性的，且能通过'潜在因素-多类别风险预测-前置预警'机制映射到编码智能体的可预防智能体诱发损害，该映射依赖编码智能体自主多步修改、工具副作用、可执行制品等非替代性条件。因此列为strong_candidate。
- Confidence: 0.62

## strong_candidate: Long-term multi-criteria improvement planning

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113606
- Source outcome: Z(p): number of possible bottlenecks (bottleneck risk of a path)
- Coding-agent outcome: 依赖感知的代理化改进步骤排序中的瓶颈规避
- Decision: 论文构建并实例化了多准则长期改进规划框架及软件（MCDMBM），并在ARWU案例中评估，虽未使用正式DSR标签，但属于design_oriented_build_evaluate。抗变革理论和瓶颈机制被明确转化为单准则步骤、运营变化惩罚Φ*、瓶颈惩罚Z*和Assumption 3等设计特征。评估结果中‘瓶颈风险Z(p)’是语境化的改进规划目标，并可映射为编码智能体的依赖感知步骤排序中的瓶颈规避；该映射依赖编码智能体的自主多步规划、仓库级依赖上下文、工具副作用和测试反馈等独特条件，去除代理条件后不成立。因此判定为strong_candidate，target_match=true。
- Confidence: 0.62

## strong_candidate: A Robust Inference Method for Decision-Making in Networks

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15992
- Source outcome: False negative rate and statistical power
- Coding-agent outcome: 依赖感知缺失下的必要修改遗漏率（false negative avoidance for repo-wide changes）
- Decision: 来源论文构建并评估了一个明确的方法性人工物（鲁棒MLE推断方法），属于design_oriented_build_evaluate；感知差距、Thomas定理、认知社会结构等理论（或理论构念）实质性地塑造了设计需求与机制（不确定性集合、极大极小估计），理论-设计强度为moderate；三个评估结果中，至少‘假阴性率/统计功效’在来源语境中是contextualized，且到编码智能体的迁移具有强非替代性：自主编码智能体在仓库级多步修改中需要依赖感知来避免漏改关键文件，鲁棒检验机制可转化为不确定性感知的规划与验证机制。综合判定为strong_candidate。
- Confidence: 0.62

## strong_candidate: A deep recurrent neural network approach to learn sequence similarities for user-identification

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113718
- Source outcome: User re-identification accuracy (dual-choice success rate)
- Coding-agent outcome: 编码智能体行为痕迹归属识别（agent trace attribution）
- Decision: 该文属于‘design_oriented_build_evaluate’：作者构建并开源了TL-RNN框架，并通过三个实证任务（双选再识别、多用户分配、活跃用户数估计）评估其性能。LSTM和三元组损失作为命名理论构念，直接塑造了网络架构和嵌入学习机制，理论到设计的连接可追踪但属于算法层面而非正式IS理论，因此theory_to_design_strength为moderate。结果变量‘用户再识别准确率’在行为追踪、共享账号和隐私语境下有具体操作化和利害关系，属于contextualized。将这一机制迁移到编码智能体时，可以从多步骤、带仓库副作用的工具调用序列中学习主体行为签名，用于智能体痕迹归属、多智能体会话分配和未知主体数量估计，这依赖于编码智能体特有的自主迭代、工具副作用和异步协作条件；去除该条件后迁移不成立。综合判断为strong_candidate，需要人工复核以确认算法理论构念的可接受性和迁移的生态效度。
- Confidence: 0.62

## strong_candidate: Algorithmic Assortative Matching on a Digital Social Medium

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2022.1135
- Source outcome: Overall more segregated social environment (community polarization/segregation between high- and low-activity teams)
- Coding-agent outcome: 智能体-代码库生态的发展分化（assortativity-induced agent-repository divergence）
- Decision: 该论文明确构建并现场部署了一套ML驱动的正向同配匹配系统，并通过时间切换现场实验评估其效果；设计直接源于Becker的 assortative matching 理论和超模/互补生产技术理论，属于设计导向的构建-评估研究。评价结果中至少有一个领域构成性/情境化结果——算法同配导致的社区隔离/极化——可作为强编码智能体特定的设计目标：它可以通过agent能力预测与仓库健康度分类的分配机制，迁移到防止编码智能体生态两极分化。候选结果的定义、机制、度量均依赖编码智能体的自治性、仓库级副作用与持久迭代，因此具有强非替代性。
- Confidence: 0.62

## strong_candidate: An explanatory machine learning framework for studying pandemics: The case of COVID-19 emergency department readmissions

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113730
- Source outcome: SHAP importance scores / individual-level risk factor identification
- Coding-agent outcome: 编码代理失败风险的实例级因子归因
- Decision: 源论文构建并评估了探索-预测-解释的ML框架/临床决策支持系统，具备build-and-evaluate特征；合作博弈论(SHAP)与演化搜索(GA)对设计有可追踪的生成作用；个体级风险因子归因结果经过定量计算、稳健性检验和临床比对，具有领域特定含义；该机制可迁移到编码代理的实例级失败原因归因，且依赖代理的多步轨迹、仓库副作用和执行反馈等独特条件，因此构成强候选。
- Confidence: 0.62

## strong_candidate: Data misrepresentation detection for insurance underwriting fraud prevention

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113798
- Source outcome: conditional premium fraud risk / premium fraud risk score
- Coding-agent outcome: 编码代理自我报告失真风险（coding-agent misrepresentation risk）
- Decision: 论文属于设计导向的构建-评估研究：构建了基于条件密度估计的保险承保数据虚报检测/保费欺诈风险评分方法，并在真实车险数据上进行了案例评估。机会-动机框架清晰地塑造了“条件保费欺诈风险”的目标定义和Z/X变量划分，理论到设计的强度为中度。主要结果“保费欺诈风险评分”的语义和操作化高度依赖保险承保领域，属于domain-constitutive；其机会-动机机制可以转化为编码代理自我报告失真风险这一新结果，且与编码代理的自主多步执行、工具副作用、概率性幻觉等条件强相关，具有strong的编码代理特异性和可辩护的机制迁移。因此判定为strong_candidate。
- Confidence: 0.62

## strong_candidate: Designing a Thrifty Approach for SME Business Continuity: Practices for Transparency of the Design Process

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00771
- Source outcome: Embeddedness (commitment to and awareness of BC)
- Coding-agent outcome: 对自主编码代理的监督正念（mindful oversight of autonomous coding agents）
- Decision: 该文是显式DSR研究，构建并评估了面向SME的节俭式BC管理方法；集体正念和社会技术系统理论被明确用于推导元需求和设计特征（强理论-设计连接）。评估中，嵌入性（BC意识与承诺）是领域构成性的、被定性质性评估的结果，且可基于'基础设施可见性产生正念'机制转化为编码代理特有的'监督正念'结果：代理的多步自主仓库级操作和概率性错误使该结果具有非替代性。因此符合strong_candidate标准。
- Confidence: 0.62

## strong_candidate: Multiple objective metaheuristics for feature selection based on stakeholder requirements in credit scoring

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113714
- Source outcome: Stakeholder data requirement values (Expected Maximum Profit, cardinality, affordability, reliability, collectability)
- Coding-agent outcome: 面向利益相关者需求的多目标代码/工件/动作选择质量
- Decision: 该文属于设计导向的构建-评估研究：提出并实现了两个新算法NSBGOA和SelCrossMut NSBGOA，并以Systems Engineering stakeholder requirement definition process为基础，将利益相关者数据需求量化为目标函数，进行了基于柬埔寨替代数据信用评分的实证评估。理论到设计链条明确（需求定义 -> 需求值矩阵 -> 目标函数 -> 算法设计），且评估了具有领域情境性的利益相关者需求目标值（利润、特征数量、可负担性、可靠性、可采集性）及多目标平衡。最佳候选结果可转化为编码代理的多目标工件/动作选择设计目标，其非可替代性依赖于代理的仓库级多步修改、工具副作用和测试反馈等编码代理特有条件。
- Confidence: 0.62

## strong_candidate: Skipping class: improving human-driven data exploration and querying through instances

- Year/journal: 2022 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1869507
- Source outcome: Effective use in query formulation (query formulation performance)
- Coding-agent outcome: 仓库级变更/查询计划的步骤完整性与忠实度
- Decision: 该文属于design_oriented_build_evaluate：作者构建并实例化了实例导向的schema-free数据表示，并在两个实验中将其与类导向表示对比评估。理论到设计的连接强：Cognitive Schema Theory和锚定启发式明确用于推导表示设计原则（去除预定类别、让用户按需构建自身schema）。至少一个被评估结果（query formulation performance）具有来源领域特定操作化，并且可映射到编码代理特有的“仓库级变更/查询计划步骤完整性与忠实度”结果：代理的自主多步规划、仓库级上下文、工具副作用和概率生成使它可能被现有包/类分解所锚定；实例级表示作为设计干预可以降低这种锚定。因此形成具辩护力的机制转移，属于strong_candidate。
- Confidence: 0.62

## strong_candidate: Assuring quality and waiting time in real-time spatial crowdsourcing

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113869
- Source outcome: Average reputation value of selected workers (β)
- Coding-agent outcome: 编码代理补丁可靠性声誉（agent patch-reliability reputation）
- Decision: 该文构建并评估了TP-TASC工件（LightGBM预测+启发式任务分配），属于design_oriented_build_evaluate；声誉机制这一理论性构念以中等强度直接塑造了分配目标和算法优先级；被评估的'被选工人平均声誉'在源域是情境化的质量代理，且可迁移为'编码代理补丁可靠性声誉'，该迁移依赖代理的自主多步修改、测试反馈与仓库副作用等编码代理特有条件，具有强非替代性。因此保留为强候选。编码代理迁移为分析推断，并非源文作者的主张。
- Confidence: 0.62

## strong_candidate: Fun Shopping: A Randomized Field Experiment on Gamification

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1147
- Source outcome: Exploration effect (RatioNewStore)
- Coding-agent outcome: 仓库级探索广度（repository exploration breadth）
- Decision: 论文构建并评估了一个基于位置技术的游戏化购物干预（design_oriented_build_evaluate），SDT 与 SCT 明确塑造了徽章和排行榜的设计特征且预测了作用机制（理论-设计连接强）。最佳结果候选为探索效应（RatioNewStore），其在购物中心情境中有领域特定的操作化，并且可被映射为编码智能体的仓库级探索广度；该转移依赖智能体的自主多步规划、仓库级上下文和工具使用等独特条件，故具备强非替代性。次佳候选为撤除干预后的行为持续性，转移中等。整体符合 strong_candidate。
- Confidence: 0.62

## strong_candidate: Reidentification Risk in Panel Data: Protecting for<i>k</i>-Anonymity

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1169
- Source outcome: sno-unicity (snowballing unicity)
- Coding-agent outcome: 编码智能体操作日志的 sno-unicity / 轨迹级重识别风险
- Decision: 该论文属于设计导向的构建-评估研究（未标注 DSR 但构建并评估了 k-MM 方法和 sno-unicity 度量）；k-anonymity 和 l-diversity 理论直接生成了优化约束，理论到设计的关系强。最佳结果候选 sno-unicity 是纵向面板数据特有的重识别风险度量，具有情境化含义；其向编码智能体操作日志的转移依赖多步自主、仓库级副作用、工具调用等智能体特有条件，且 k-MM 的最小扰动机制可被重放为日志匿名化设计原则，因此达到 strong_candidate 标准。
- Confidence: 0.62

## strong_candidate: The Attraction Effect in Crowdfunding

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1152
- Source outcome: Choice of the target (high) reward / likelihood of choosing the higher-priced reward
- Coding-agent outcome: 编码智能体在候选代码方案选项集中的目标方案采纳率（decoy-augmented target solution selection）
- Decision: 该论文属于设计导向的构建-评价研究：作者设计并实例化了数字奖励菜单（加入价格或质量诱饵），通过七个在线实验和一个Kickstarter实地研究进行评价。Salience theory明确且直接用于推导诱饵设计原则和假设，属于强理论到设计。主要结果“选择高价目标奖励的可能性”被定量测量，且在众筹奖励菜单情境中被具体操作化，属于情境化结果。将该结果迁移到编码智能体时，可以形成“候选代码方案选项集中的目标方案采纳率”这一新的设计目标，依赖于智能体自主生成多个可执行工件、多步迭代、测试反馈等独特条件，非静态IDE或普通聊天机器人可替代，因此转移具有较强的非替代性和机制可辩护性。综合判定为strong_candidate。
- Confidence: 0.62

## strong_candidate: Human-Centered Design and Evaluation of a NeuroIS Tool for Flow Support

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00855
- Source outcome: Retrospective biofeedback effectiveness (non-disruption of flow)
- Coding-agent outcome: 编码代理执行连续性保持（任务流不被打断）
- Decision: 该论文是显式设计科学研究，从心流理论、IT中介中断研究、自我调节理论、香农-韦弗传播模型等推导出元需求与设计原则，并通过实验室实验和现场研究评价了原型。最具迁移力的候选结果是“回顾式生物反馈避免打断心流”（DP5）：其源端机制（心流中自我反思丧失，实时反馈会破坏心流）领域特定且被定性质性评价；转移为编码代理时，可形成“执行连续性保持”这一编码代理特有设计目标，依赖自主多步执行、工具副作用、异步委托等代理条件，移除代理条件后该设计机制失去对象，因此满足非替代性。故判定为strong_candidate。
- Confidence: 0.62

## strong_candidate: Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models

- Year/journal: 2024 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2024.2340827
- Source outcome: Robustness to incomplete/noisy knowledge graphs
- Coding-agent outcome: 委托目标对齐的仓库知识鲁棒性（imperfect repository context robustness）
- Decision: 源论文是明确的DSR研究：使用设计科学研究方法和ISDT，以Schema Theory为kernel theory推导元需求与元设计，并实例化为知识感知学习框架。理论到设计的连接为强。三个被评估结果中，学习有效性和学习效率偏通用，而「对不完整/噪声知识图谱的鲁棒性」具有上下文特定操作化（ConceptNet三元组缺失/噪声下的F1保留），且其机制（基于TF-IDF式边权重的图式激活）可迁移到coding agent：在仓库级上下文中，代理需根据委托目标激活最相关的知识图式，以在噪声或不完整仓库信息下保持目标对齐的补丁质量。该迁移依赖代理的委托目标追求、多步规划、仓库级上下文、工具副作用和测试反馈等，去除agentic编码条件会实质性改变结果定义和度量方式，故为强编码智能体特异性。保留为strong_candidate。
- Confidence: 0.62

## strong_candidate: Managing attention: more mindful team decision-making

- Year/journal: 2024 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2118627
- Source outcome: Errors (Mindfulness Breakdowns in Contributing and Representing)
- Coding-agent outcome: 自主编码代理的上下文整合失误（context-integration breakdown errors）
- Decision: 该文构建了MOA过程这一流程干预并设计实验评估；正念理论、注意力管理、认知负荷理论和媒体同步性理论直接导出了分阶段设计的机制和预期结果。最有迁移潜力的评估结果是'正念断裂错误'（贡献断裂和表征断裂），它具备情境化操作化，且可被重新定义为编码代理在自主修改时忽略仓库/测试/反馈的上下文整合错误；删除代理条件后，该结果的测量和机制均不再成立。因此符合strong_candidate。
- Confidence: 0.62

## strong_candidate: Roles of Feedback and Phishing Characteristics in Antiphishing Training Performance: Perspectives of Goal Setting and Skill Acquisition

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00854
- Source outcome: Decision avoidance (DAV)
- Coding-agent outcome: 编码代理的过早放弃/不当决策回避（premature delegation / autonomy avoidance）
- Decision: 文章虽然没有正式使用设计科学研究标签，但实际构建并评估了反钓鱼培训的反馈干预（示例型/正念型反馈、反馈量），属于design_oriented_build_evaluate；目标设定理论和技能习得理论明确指导了反馈设计并预测结果机制；决策回避（DAV）被定量评估且具有领域特定操作化，且可迁移为编码代理的‘过早放弃/不当决策回避’这一代理特有结果，移除代理条件后定义、机制和测量均实质改变，因此具备强候选资格。
- Confidence: 0.62

## strong_candidate: Uncovering the Neural Processes of Privacy: A Neurally Informed Behavioral Intervention to Protect Information Privacy

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0550
- Source outcome: Willingness to disclose private information
- Coding-agent outcome: 编码代理的隐私风险校准行动选择
- Decision: 该论文是设计导向的构建-评估研究：基于fMRI发现设计并测试了神经知情的行为干预（改变披露决策时风险与收益信息的呈现时序），理论（隐私计算、有界注意、邻近性、选择架构）到设计（Hypothesis 2）的链条明确，且评估了领域特定的结果（愿意披露信息、侵入性权重、隐私保护）。最可迁移的结果是“决策时刻风险显著化”机制：在编码代理执行高风险工具调用前即时呈现风险信息，可形成新的编码代理设计目标——风险校准行动选择。该目标依赖代理的自主多步决策、工具副作用和仓库级上下文，非静态IDE/普通聊天机器人可替代。因此为强候选。
- Confidence: 0.62

## strong_candidate: Fast Forecasting of Unstable Data Streams for On-Demand Service Platforms

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0130
- Source outcome: SMAPE/RMSE forecast performance (with and without forecast-breakdown detection)
- Coding-agent outcome: 自主編碼智能體在環境漂移下的性能崩潰恢復力（performance-breakdown resilience）
- Decision: 本文明確採用 Hevner et al. (2004) 的設計科學方法，建構並評估了 FFUDS 框架（explicit_design_science）。設計由多個具名理論/建構直接驅動：forecast breakdown、Pesaran-Timmermann 預測組合、Luo-Song 可再生估計、Killick PELT，均具體轉化為框架的偵測、組合與快速更新機制，理論到設計連結顯著（strong）。評估結果包括 SMAPE/RMSE 預測績效、經濟損失、計算時間與成本，其中在『不穩定串流中的預測崩潰偵測與組合』脈絡下的準確度屬於 contextualized 結果；將其遷移至編碼智能體的『環境漂移下的性能崩潰恢復力』具備強編碼代理特異性（非替代性），因為它依賴自主多步執行、測試/執行回饋、儲存庫層級脈絡與動態委派。因此整體決策為 strong_candidate，target_match=true。
- Confidence: 0.62

## strong_candidate: How Product Display Orientation Affects Customers’ Choice Satisfaction in Online Purchase: A Choice Closure Perspective

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0575
- Source outcome: choice satisfaction
- Coding-agent outcome: 开发者对编码智能体自主实施选择的承诺/委托闭合（delegation closure）
- Decision: 该文为设计导向的构建与评估研究：设计和操纵了电商产品展示方向与最终性提示的实验界面，并基于选择闭合理论与水平展示优势提出并检验了设计假设。核心结果（选择满意度）在源域中具有情境化意义（购买决定后、使用前的满意度，且与订单取消成本挂钩）。该理论与设计机制能够通过“充分比较→选择闭合→减少事后后悔”映射到编码智能体场景中的开发者委托承诺和返工问题，且对智能体自主委派、多步骤计划和人机交接等条件具有强非替代性。因此判定为strong_candidate，但迁移强度属于中等，需结合人机交互理论进一步细化。
- Confidence: 0.62

## strong_candidate: Sourcing product innovation intelligence from online reviews

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113751
- Source outcome: Usefulness to the innovation process
- Coding-agent outcome: 属性映射对齐的代理代码修改有效性（attribute-aligned code modification quality）
- Decision: 该文属于设计导向的构建与评估研究：构建了基于属性映射框架的在线评论创新机会优先级排序技术，并通过经理有用性评分和对比实验进行评估。属性映射框架对设计有强生成作用（定义compliments/feature requests/irritators类别与标注/排序目标）。主要评估结果'对创新过程的有用性'具有领域情境化操作化（由资深经理针对具体产品属性评定）。该理论-设计机制可迁移到编码代理：代理可从用户反馈构建属性图并据此规划、执行、验证代码改动，形成'属性映射对齐的代码修改有效性'这一编码代理特有结果，非静态IDE或聊天机器人可替代。因此判定为strong_candidate。
- Confidence: 0.58

## strong_candidate: A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114100
- Source outcome: False positive trading signals / number of trading signals
- Coding-agent outcome: 虚假或非必要的自主代码修改（spurious autonomous code modifications）
- Decision: 该文构建并评估了一个混合交易决策支持系统（design_oriented_build_evaluate），未经正式DSR标签；RL/MDP和Policy Gradient等理论构造直接驱动了状态空间设计和基于动作概率的交易量调节机制（theory-to-design moderate）。被评估结果“虚假交易信号/信号数量”在交易语境中具有领域构成性，并可通过置信度门控机制转移到编码代理的“虚假/非必要自主代码修改”上；该转移依赖编码代理的自主多步修改、仓库副作用、测试反馈等非可替代条件，因此为强候选。最佳转移为候选1。
- Confidence: 0.58

## strong_candidate: Human Behavior Mining: A Framework for Theorizing About mHealth Behavior Using Digital Trace Data

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00938
- Source outcome: Reciprocal relationships and interdependencies between SCT-based mHealth feature use and physical activity behavior
- Coding-agent outcome: 编码代理的自适应目标-反馈互惠性（adaptive goal-feedback reciprocity）
- Decision: 该文属于设计导向的构建-评估研究：构建了HBM框架和基于SCT的mHealth应用实例并进行了实证评估；SCT以中等强度导出了应用功能、行为活动操作化和动态关系假设；被评估的核心结果——SCT动态互惠关系——在mHealth/身体活动语境下具有语境化含义；将其机制映射到编码代理的自适应目标-反馈互惠性具有强编码代理特异性，且过程挖掘/预测方法可直接类比到代理行为日志分析。因此，保留为强候选。
- Confidence: 0.55

## promising_candidate: Bayesian Stackelberg games for cyber-security decision support

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113599
- Source outcome: security risk / expected security risk
- Coding-agent outcome: 护栏组合下的期望残余风险（针对部分可观察的编码代理多步动作路径）
- Decision: 来源论文满足 design_oriented_build_evaluate：构建并评估了网络安全决策支持系统；Stackelberg/Bayesian Stackelberg 博弈论和 HMM 对预防/在线优化设计有直接生成作用；评估的期望安全风险在攻击图-多阶段攻击语境下是领域构成性结果。向编码代理的转移是机制类比：将代理的多步代码修改建模为隐藏状态下的风险路径，护栏组合作为在线防御控制组合。该转移有明确的编码代理非替代性，但尚属概念扩展，缺少经验验证，因此判为 promising_candidate 供人工复核。
- Confidence: 0.78

## promising_candidate: Designing Effective Mobile Health Apps: Does Combining Behavior Change Techniques Really Create Synergies?

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1912936
- Source outcome: mHealth use (extent of use)
- Coding-agent outcome: 人类对编码智能体的持续委托（delegation continuity / continued delegation）
- Decision: 该文是明确的设计科学研究（explanatory design theorizing），保护动机理论和社会上行比较理论被强有力地转化为具体mHealth设计特征和假设，并通过现场实验定量评价。主要评价结果'mHealth use'虽被领域化地操作为压力缓解训练次数，但本质仍是通用的系统使用/采纳构念；向编码智能体的转换需要将其重新定义为'人类对智能体的持续委托'，并引入人机信任/监督理论，因此源域结果到编码智能体目标之间的环节属于中等强度而非无争议。综合为 promising_candidate，保留人工复核。
- Confidence: 0.78

## promising_candidate: Identifying comparable entities from online question-answering contents

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103449
- Source outcome: Comparable entity identification
- Coding-agent outcome: 任务相关可比较代码实体覆盖度
- Decision: 该文是显式设计科学研究，构建并评估了ICQA工件；采用激活扩散/联想网络理论直接推导比较网络设计，theory-to-design强；评估的可比实体识别是领域构成性结果。将'可比实体识别'扩展到编码智能体的'任务相关可比较代码实体覆盖度'有明确机制（共现+距离→比较网络→修改计划覆盖），且依赖智能体的委托目标、仓库级上下文和多步修改等特有条件，但该迁移仍带有较多类比性，且操作化需额外人工基准，因此定为promising_candidate供人工复核。
- Confidence: 0.78

## promising_candidate: Improving the state-tracking ability of corona dashboards

- Year/journal: 2021 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2021.1907235
- Source outcome: state-tracking ability
- Coding-agent outcome: 代码智能体的状态跟踪保真度（state-tracking fidelity）
- Decision: 论文是明确的设计科学研究（Peffers et al., 2007），并用表示理论（Weber, 1997）从状态跟踪四个条件演绎出四项设计原则，理论到设计的联系强；案例研究定性评估了设计原则的重要性、可行动性与效果。然而，论文没有实例化一个新型仪表板，也没有测量实现后的状态跟踪结果，而是通过专家对设计原则的估计来评价，因此‘已评估的结果产物’这一环节是间接的。状态跟踪能力对代码智能体的迁移在机制上强（内部状态模型 vs 真实仓库状态），但受制于源侧未实例化的局限，故判为 promising_candidate 供人工复核。
- Confidence: 0.75

## promising_candidate: Spline-rule ensemble classifiers with structured sparsity regularization for interpretable customer churn modeling

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113523
- Source outcome: Model interpretability
- Coding-agent outcome: 变更集一致性（change-set coherence）
- Decision: 本文构建并评估了新算法SRE-SGL，属于design-oriented build-evaluate；其设计受可解释性构念驱动（将依赖同一变量的项分组并用稀疏组lasso避免冲突/冗余），但可解释性并非形式化理论，因此theory-to-design为中等；评估结果‘模型可解释性’在客户流失管理情境中被具体化为无冲突项、紧凑模型、变量重要性/偏依赖图，属于情境化结果；该结果可经构念扩展迁移为编码代理的‘变更集一致性/可审查性’目标，严重依赖代理的自主多步规划、仓库级上下文和工具副作用，具备强编码代理特异性，但机制仍需人工审查实验验证，故列为promising而非strong。
- Confidence: 0.75

## promising_candidate: Contextual Targeting in mHealth Apps: Harnessing Weather Information and Message Framing to Increase Physical Activity

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0119
- Source outcome: Achievement of the daily 10,000-step exercise goal
- Coding-agent outcome: 用户对编码智能体生成的负面诊断性反馈的建设性处理与行动采纳（如错误报告、构建失败解释、安全警告）
- Decision: 该文属于构建设计并评估的现场实验研究（非正式DSR标签），理论（mood-as-resource vs mood congruity、prospect theory）实质性地驱动了天气×消息框架的干预设计与评估，源结果'10,000步目标达成'在mHealth领域具有领域构成性。但其最有希望的编码智能体迁移——根据执行状态调整负面诊断框架以促进用户建设性反馈处理——是源理论到编码情境的机制迁移推理，源论文未涉及编码智能体，且替代性检验为中等强度，因此列为 promising_candidate 供人工复核而非 strong_candidate。
- Confidence: 0.75

## promising_candidate: Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0204
- Source outcome: Balancing-market commitment fulfillment / penalty avoidance
- Coding-agent outcome: 自主编码代理的变更承诺履约率与仓库完整性保持
- Decision: 该文是明确的设计科学研究，构建了FleetPower DSS并通过仿真评估。理论到设计的强度为中等（智能市场、多产品资源、市场分配概念确实塑造了系统架构，但推导较隐晦）。最佳结果候选是平衡市场承诺履约/罚则规避，其在源域中具有情境化操作化，且可映射到编码代理的变更承诺履约与仓库完整性保持；但该映射属于机制迁移和类比，需要结合CI/测试反馈边界条件，因此整体为promising_candidate而非strong_candidate。
- Confidence: 0.74

## promising_candidate: Improving the Design of Information Security Messages by Leveraging the Effects of Temporal Distance and Argument Nature

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00697
- Source outcome: Protection motivation
- Coding-agent outcome: 对编码智能体发起的安全相关代码变更的校准型委托接受（calibrated delegation acceptance）
- Decision: 该文属于 design_oriented_build_evaluate：实际构建并操纵了恐惧诉求消息（时间距离 × 论证性质）并进行了两次在线实验评估；CLT 与 PMT 对消息设计有明确、可追溯的生成性作用（strong theory-to-design），且保护动机是量化评估的情境化结果。但保护动机至编码智能体的迁移是机制类比——从“人类执行安全行为意图”转向“人类对智能体安全变更的校准型委托接受”，该迁移虽具有较强编码智能体特异性，但仍存在源结果（意图）与目标结果（委托决策）之间的概念距离，因此评为 promising_candidate 供人工深入审阅。
- Confidence: 0.72

## promising_candidate: The Effect of Risk Representation Using Colors and Symbols in Business Process Models on Operational Risk Management Performance

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00676
- Source outcome: Control improvement
- Coding-agent outcome: 编码代理自主变更计划的防护控制改进能力（guardrail improvement identification）
- Decision: 源论文属于设计导向的构建-评估研究：作者实际构造了颜色和符号两种BPMN风险/控制表示变体并通过交叉实验评估；理论到设计的链条清晰（dual-process theory、cognitive load theory、color-in-context theory、theory of effective visual notations），且至少三个结果变量（风险理解、控制理解、控制改进）被量化评估。其“控制改进”结果在源领域具有上下文特定含义，并可映射为编码代理场景中的“防护控制改进识别”这一候选设计目标；该映射依赖编码代理的自主多步执行、工具副作用和人类监督关系，但在代理计划界面上的视觉线索机制仍需进一步实证，且颜色/符号效应可能带有一般信息可视化普遍性，故整体定为promising_candidate而非strong_candidate。
- Confidence: 0.72

## promising_candidate: A regulatory control framework for decentrally governed DLT systems: Action design research

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2021.103555
- Source outcome: Residual risk outcomes (reduction in probability/consequence of DLT-related risks)
- Coding-agent outcome: 人类监督控制点保留度（对编码智能体自治行动的可见、可停止、可回滚程度）
- Decision: 该文是明确的参与式行动设计研究，构建并评估了DRC框架；去中心化治理、监管、ISO31000风险管理和Gregor设计原则模式对框架结构和设计原则有实质性影响，但理论到设计的链路部分隐含在专家共同设计中，故为中等。被评估的结果主要是专家对框架相关性/质量的感知，实际的风险降低结果是计划性设计目标而非充分实证评估。尽管如此，其‘控制点被替代并重新配置控制’的机制可较强地迁移到编码智能体的人类监督控制点保留问题，因此保留为promising_candidate供人工审查，而非strong_candidate。
- Confidence: 0.72

## promising_candidate: It's not just about accuracy: An investigation of the human factors in users' reliance on anti-phishing tools

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113846
- Source outcome: User reliance on anti-phishing tool predictions
- Coding-agent outcome: 开发人员对编码智能体自主改动/建议的校准依赖（calibrated reliance on coding-agent actions）
- Decision: 该文构建并评估了一个实验性反钓鱼工具，满足design_oriented_build_evaluate；信任/不信任理论对设计变量（准确率、透明度、频率）有中等强度的指导；主要结果‘用户对工具预测的依赖’虽在反钓鱼情境中有具体操作化，但本质上是通用自动化依赖构念，源情境特定性仅为contextualized而非domain_constitutive；向编码智能体的迁移机制清晰且具备强非替代性，但源设计与理论到设计的连接均为中等，且工具本身是实验刺激而非正式设计科学贡献，因此保留为promising_candidate供人工复核，而非strong_candidate。
- Confidence: 0.72

## promising_candidate: The multidimensional nature of privacy risks: Conceptualisation, measurement and implications for digital services

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12386
- Source outcome: Freedom-related privacy risk
- Coding-agent outcome: 开发者在编码代理委托中的决策自主性保持（抗隐性操纵）
- Decision: 文章构建并评估了多维隐私风险测量工具，并通过实验展示了设计特征（隐私仪表盘、支付中介）可定向缓解特定风险维度，满足design_oriented_build_evaluate的基本模式。但理论到设计的关系为中等强度：风险理论主要塑造了测量构念和实验假设，而非正式设计原则；且最可迁移的结果（自由相关风险→开发者在编码代理委托中的决策自主性）需要明显的构念扩展和理论组合。因此保留为promising_candidate供人工复核，而非strong_candidate。
- Confidence: 0.72

## promising_candidate: Design Principles for Platform-Enabled Knowledge Commons with an Expository Instantiation

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00824
- Source outcome: Artifact sustainability (continued patronage/revitalization)
- Coding-agent outcome: 多智能体共享代码/工件公共资源的可持续性
- Decision: 本文是明确的DSR研究, 理论到设计连接强(Ostrom commons理论及其DPs -> PEKC DPs -> Service-Symphony特征). 最佳结局'知识公共资源可持续性/持续用户参与'通过Google Analytics评估, 具有领域情境性. 向编码代理的'多代理共享代码公共资源可持续性'迁移机制可辩护, 但需将知识公共资源类比为代码公共资源, 且源文未评估代码代理场景; 这是关键的中等强度链接. 因此不是strong_candidate, 而应保留为promising_candidate供人工复核.
- Confidence: 0.72

## promising_candidate: Diversity Preference-Aware Link Recommendation for Online Social Networks

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1174
- Source outcome: Diversity Preference Matching Score (DPMS)
- Coding-agent outcome: 代码变更多样性偏好匹配度（DPMS-Code）
- Decision: 源论文属于显式设计科学研究：明确提出计算类型的设计科学贡献，构建并评估了DPA-LR方法；理论基础（同质性/异质性、人格化多样性偏好、维度级偏好）直接导出设计需求（个性化、维度级优化）和预期机制（满足偏好→更高接受率），theory-to-design强度为强。DPMS是源领域特有且被定量评估的结果（domain_constitutive）。编码智能体迁移方面，可将“多样性偏好匹配”迁移为“代码变更多样性偏好匹配”，并依赖自主多步修改、仓库级上下文、工具副作用等智能体特征；但该迁移仍有较强类比性，且“变更分布”目标可能与正确性/最小化修改原则冲突，因此编码侧特异性与迁移强度为中等。整体模式成立但迁移链接为中等强度，值得人工全文复核。
- Confidence: 0.72

## promising_candidate: ROLEX: A Novel Method for Interpretable Machine Learning Using Robust Local Explanations

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17141
- Source outcome: Human interpretability / comprehensibility of patient-level explanations
- Coding-agent outcome: 代理任务级变更的开发者可审查性（Developer Reviewability of Agent's Task-level Changes）
- Decision: 该文是明确的设计科学研究：构建了ROLEX算法和原型界面并进行了定量（局部忠实度）和定性（专家访谈）评估。理论到设计的链接为中等：XAI框架、Menlo Report受益原则和解释性调试原则确实影响了方法目标和界面设计，但核心算法机制主要由技术缺陷驱动。最强候选结果是‘患者级解释的可理解性’，其源域意义是情境化的（医患沟通、个性化医疗），向编码代理转移为‘开发者对代理任务级变更的可审查性’，利用了代理的自主多步执行、仓库副作用和委托-监督等独特条件，具有强非替代性。但源文对该结果的评估主要是感知性的，且转移需实质性概念扩展，因此整个模式虽可行但关键环节为中等强度，适合人工全文复核。
- Confidence: 0.72

## promising_candidate: Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17062
- Source outcome: financial risk prediction accuracy (out-of-sample volatility forecast)
- Coding-agent outcome: 自主代码变更的声明-行为一致性风险（plan-action congruence risk）预测
- Decision: 来源论文是明确的设计科学研究：以 Mehrabian 沟通模型为内核理论，推导元需求/元设计，实例化 DeepVoice 并评估了财务风险预测精度和经济效用。财务风险预测是领域构成性结果；可以映射为编码智能体的“声明-行为一致性风险预测”，但该映射需要将财务风险重构为自主代码变更风险，且来源论文未涉及编码智能体，因此该转移属于中等强度的机制转移，值得人工复核而非直接作为强候选。
- Confidence: 0.72

## promising_candidate: Rethinking Gamification Failure: A Model and Investigation of Gamified System Maladaptive Behaviors

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0284
- Source outcome: gamified system maladaptive behaviors (GSMB)
- Coding-agent outcome: 编码智能体的目标误适应/奖励黑客行为（agent maladaptive behavior / reward hacking）
- Decision: 论文构建并评估了实验性游戏化系统，并明确评估了GSMB和任务绩效；GST和SDT对设计问题构念及实验操纵有可追踪影响，但该影响主要表现为实验条件操纵而非正式设计科学中的设计原则/需求推导，因此theory-to-design强度为moderate。GSMB是领域构成性的，且到编码智能体奖励黑客行为的迁移具有强非替代性；但设计类型是design_oriented_build_evaluate而非formal DSR，且关键theory-to-design链接为moderate，故保留为promising_candidate供人工复核，不设target_match。
- Confidence: 0.72

## promising_candidate: Effects of Idea Set Partitioning on Selection Quality: An Exploratory Eye-Tracking Study of Information Processing

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00958
- Source outcome: Idea novelty (novelty of selected ideas)
- Coding-agent outcome: 编码智能体所生成/采用的候选代码方案的新颖性-可行性选择质量
- Decision: 论文采用设计导向的构建-评估实验（数字助推分区干预），理论到设计为中等强度（数字助推/选择架构、一般可评价性理论推导假设）。评价结果‘所选想法的新颖性’具有语境化意义，并可通过边界条件扩展迁移到编码智能体候选代码方案的选择质量；但迁移依赖人-智能体类比，且源论文不是正式DSR，编码智能体特异性为中等，因此判定为 promising_candidate 而非 strong_candidate。
- Confidence: 0.72

## promising_candidate: How to Assign Scarce Resources Without Money: Designing Information Systems that are Efficient, Truthful, and (Pretty) Fair

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2020.0959
- Source outcome: justified envy
- Coding-agent outcome: 多智能体代码任务分配中的可辩护不公平/正当嫉妒
- Decision: 该文是明确的设计科学研究：构建并评估了RESPCT匹配机制；理论（TTC、策略证明/效率/无嫉妒、扩展席位TTC）直接指导了算法设计；评估的'正当嫉妒'结果在匹配领域具有领域构成性。将其转移到编码智能体场景时，可以概念化为多智能体代码任务分配中的可辩护不公平或申报真实性，但该转移依赖将学生偏好替换为开发者/用户偏好或智能体能力申报，且不直接涉及代码生成过程本身，因此编码智能体特异性为中等。整体为promising_candidate，需人工复核其编码智能体非替代性。
- Confidence: 0.7

## promising_candidate: Welfare Properties of Profit Maximizing Recommender Systems: Theory and Results from a Randomized Experiment

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/14971
- Source outcome: Consumer Surplus (CS)
- Coding-agent outcome: 委托方福利损耗（用户监督收益损耗）
- Decision: 论文设计了‘Good Deals’推荐菜单随机化实验并模拟多种推荐系统，属于设计导向的构建-评估；理论模型（价格弹性、消费者剩余/福利）明确塑造了实验设计与模拟对比，但理论-设计连接中等（实验主要是识别参数，而非测试设计原则）。消费者剩余是情境化的量化结果，向编码智能体的‘委托方福利损耗’转移具有强机制基础和强编码智能体特异性。由于设计科学属性非正式且理论-设计强度为中等，而非完美，故判定为promising_candidate而非strong_candidate。
- Confidence: 0.7

## promising_candidate: Visual analytics of set data for knowledge discovery and member selection support

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113635
- Source outcome: Reconstruction error of member compositions (inverse problem accuracy)
- Coding-agent outcome: 目标到多步代码变更计划的组合保真度（goal-to-plan compositional fidelity）
- Decision: 该文是设计导向的构建-评估研究，构建了基于流形网络模型的可视分析系统并定量评估了前向预测和逆向重构。理论到设计的线索存在但偏技术性（流形假设、VA范式、GMM），不能算强DSR理论驱动；最有希望的源结果是成员组合重构误差，具有集合数据/团队选择语境的具体化，但其本质仍是模型内部技术指标。向编码代理迁移可提出“目标到多步代码变更计划的组合保真度”，且该目标依赖代理的自主多步规划、仓储级上下文、可执行产物等特有条件，迁移机制可辩护。然而由于理论来源强度中等、源结果未被用户层面实证评估、迁移仍需大量概念化，整体判定为promising而非strong。
- Confidence: 0.7

## promising_candidate: Removing order effects from human-classified datasets: A machine learning method to improve decision making systems

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113891
- Source outcome: order effect / order-effect bias
- Coding-agent outcome: 编码代理的上下文顺序鲁棒性（顺序效应消除）
- Decision: 该文是明确的设计科学研究，构建并评估了OERM工件；量子概率理论以中等强度影响了工件设计（文本二分、f(A)/f(B)比较、均衡分割点）。评估的结果变量'顺序效应'是情境化的、量化的设计目标，而非通用绩效指标。向编码代理的迁移（上下文顺序鲁棒性）依赖编码代理特有的自主多步计划、仓库级上下文、工具副作用和测试反馈等条件，且不是表面类比。但迁移的关键环节是外推性的：源论文关于人类分类者的量子认知机制和文档语料库验证不能直接保证LLM代理存在同样的顺序效应；这一不确定使完整证据链尚属'promising'而非'strong'，值得人工全文评审。
- Confidence: 0.7

## promising_candidate: A simulation-based risk interdependency network model for project risk assessment

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113602
- Source outcome: total risk propagation loss (TRPL)
- Coding-agent outcome: 智能体变更的级联回归风险损失（cascading regression risk loss of agentic code changes）
- Decision: 该文是设计导向的构建-评估研究，而非形式化DSR：构建了ISM+MCS的RIN决策支持模型并用两个案例定量评估。设计由“风险相互依赖/风险传播”构念和经典P-I风险模型驱动，但缺乏正式理论框架，理论到设计的链接为中等强度而非强。最有希望的待转移结果是TRPL，可构念扩展为“智能体变更的级联回归风险损失”，依托仓库级依赖上下文、多步自主迭代和真实副作用等智能体特有条件，非替代性较强。由于理论-设计强度仅为中等，且源结果属于情境化而非领域构成性，故定为promising_candidate供人工复审，而非strong_candidate。
- Confidence: 0.68

## promising_candidate: Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113632
- Source outcome: expected profit
- Coding-agent outcome: 信息价值感知的代码探索/验证充分性（value-of-information-calibrated information sufficiency）
- Decision: 该文是明确的‘构建-评估’型方法论文：构建了CMMN→MDP的信息采集优化方法及运行时推荐工具，并用量化的真实报价案例证明其可行性。理论到设计的联系主要来自MDP这一优化模型/数学框架，而非行为或组织理论，因此理论驱动强度为中等而非强；评价结果‘期望利润’虽有领域化的操作化，但抽象上是通用经济指标。将‘信息价值驱动的探索/停止’机制迁移到编码代理具备较强特异性和可辩护性。由于理论驱动强度和结果语境特异性存在一定的中等/间接环节，保留为promising candidate供人工复核，而非strong candidate。
- Confidence: 0.68

## promising_candidate: Detecting Noncompliant Behavior in Organizations: How Online Survey Responses and Behaviors Reveal Risk

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1962600
- Source outcome: Answer leniency on compliance questions (H1a)
- Coding-agent outcome: 智能体权限边界违规的自评宽松度
- Decision: 来源论文是“设计导向的构建与评估”：构建了带鼠标追踪的在线问卷和逻辑回归分类模型，并做了实证评估。理论（认知失调+RAMS）到设计特征的链条清晰，来源结果（合规定义宽松度、鼠标偏差、非合规风险分类）具有领域特定意义。不过，将来源机制迁移到编码智能体时面临关键推断障碍：认知失调是人类心理机制，LLM没有信念-行为冲突；迁移依赖类比和额外对齐理论，证据链不够直接。因此列为待人工复核的promising_candidate，而非strong_candidate。
- Confidence: 0.68

## promising_candidate: Estimating the Impact of “Humanizing” Customer Service Chatbots

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1015
- Source outcome: Information disclosure milestones (sensitive information disclosure)
- Coding-agent outcome: 编码代理的敏感上下文/权限披露意愿（授权与信息共享校准）
- Decision: 该文属于设计导向的构建-评估研究：部署了可随机组合拟人化特征的聊天机器人并进行了田野实验。CASA和SIP等理论确实影响了社交临场感、延迟、幽默等特征的设计，但这种影响属于中等强度的文献驱动设计，而非显式的设计科学原则推导。三个候选中，转化率过于通用；报价敏感性虽然情境特异但转移依赖较强类比；敏感信息披露的转移最具编码代理特异性，即用户的仓库级上下文/权限披露校准，但源文将披露作为探索性机制，且未涉及编码代理的授权边界与副作用。整体模式合理但关键环节（理论到设计的强度、转移的稳健性）仍为中等，因此保留为promising_candidate供人工复审。
- Confidence: 0.68

## promising_candidate: Linking Exploits from the Dark Web to Known Vulnerabilities for Proactive Cyber Threat Intelligence: An Attention-based Deep Structured Semantic Model

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15392
- Source outcome: Exploit-vulnerability linkage accuracy/ranking performance
- Coding-agent outcome: 委托任务-代码变更语义对齐度（task-to-code semantic alignment / intent grounding）
- Decision: 该文是显式计算设计科学研究，明确构建并评估了EVA-DSSM和DVSM两个设计制品。设计由DSSM和注意力机制等理论/技术构念显式驱动，但理论到设计的强度为中等（依赖算法/技术构念而非成熟的社会科学理论）。最有希望的评估结果是exploit-vulnerability链接性能，其源领域特定性较强，并可机制性地迁移为编码智能体的“任务-代码语义对齐度”设计目标；但该迁移是新构念，缺乏源文实证支持，需要进一步的适配与验证。因此不评为strong_candidate，而保留为promising_candidate供人工审阅。
- Confidence: 0.68

## promising_candidate: Scratch my back and I'll scratch yours: The impact of user effort and recommendation agent effort on perceived recommendation agent quality

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2021.103571
- Source outcome: Perceived RA quality
- Coding-agent outcome: 感知编码代理质量与努力互惠（perceived coding-agent quality / effort reciprocity）
- Decision: 该文构建并评估了推荐代理实验原型，社会交换理论、CASA和互惠规范确实塑造了RA努力可见性与用户努力设计，属于design_oriented_build_evaluate且理论-设计联结强。被评价的感知RA质量虽在推荐代理情境下操作化，但本质上接近服务/系统质量，源领域特异性仅达到“情境化”；向编码代理迁移时，可见代理努力（计划、工具调用、测试）与开发者委托投入的互惠机制具有较强编码代理特异性，但由于结果构念的通用性和缺乏真实代理设计验证，整体判定为promising而非strong。
- Confidence: 0.68

## promising_candidate: Developing human/AI interactions for chat-based customer services: lessons learned from the Norwegian government

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2096490
- Source outcome: Affordance discovery / perception (action possibilities perceived by service agents)
- Coding-agent outcome: 编码智能体可供性发现（coding-agent affordance discovery）
- Decision: 本文采用临床研究/行动导向研究，设计了基于可供性理论的‘敏化’干预并定性评估，属于 design_oriented_build_evaluate；理论到设计链接强（可供性理论直接指导干预设计），但可供性发现作为结果其领域特异性仅达到 contextualized 而非 domain_constitutive，且转移到编码智能体需要将通用可供性发现机制具体化为委派、监控、上下文提炼等编码智能体特有可供性。因此整体为 promising_candidate，值得人工复审，而非 strong_candidate。
- Confidence: 0.68

## promising_candidate: Empowering Users with Narratives: Examining the Efficacy of Narratives for Understanding Data-Oriented Conceptual Models

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1141
- Source outcome: Domain understanding (cardinality constraint semantics)
- Coding-agent outcome: 人类监督者对代码代理拟变更的语义理解（agential code-change comprehension）
- Decision: 论文构建了数据叙事补充这一人工制品，并基于认知负荷理论和叙事故事属性进行设计，通过两个实验定量评估了对概念模型基数约束的理解（受试者正确率）。该结果在源领域具有情境化特异性（数据建模语义），且可启示编码代理领域中的人类监督理解能力提升。但是，源研究与编码代理之间仍有一层推理跳跃：源的被解释对象是静态ER图，而转移后被解释对象是代理的自主代码变更；因此编码代理特异性虽强，但转移机制尚未被源文献直接验证，属于promising_candidate而非strong_candidate。
- Confidence: 0.68

## promising_candidate: Conceptualization and Measurement of Voice-Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17525
- Source outcome: voice-interaction usability
- Coding-agent outcome: 编码代理的合作互动可用性（delegated coding-agent cooperative interaction usability）
- Decision: 论文构建并验证了语音交互可用性概念框架与量表，CPT理论对维度划分和题项设计有明确生成作用，属于设计导向的构建-评价研究。最佳候选结果’语音交互可用性’具有强领域特定性，并能通过CPT机制迁移为编码代理合作互动可用性，且非可替代性较强。但源论文的’设计物’是测量量表而非改变可用性的系统干预，评价的是构念有效性和预测关系，而非干预后的领域结果；这一间接链接使完整证据链略有不足，因此保留为promising而非strong。
- Confidence: 0.68

## promising_candidate: How Artifact-Based and Authority-Based Coordination Affect Propagation Costs in Open Source Software Development

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/18021
- Source outcome: Propagation costs
- Coding-agent outcome: 智能体生成代码变更的传播成本（agent-induced change propagation costs）
- Decision: 论文构建并评估了一个计算模型，理论（预测性知识、open superposition、mirroring hypothesis）到模型设计有清晰可追踪的机制，传播成本是领域构成性的量化结果，且可以映射为编码智能体特有的“智能体生成代码变更的传播成本”。但关键前提（是否属于设计科学研究/设计取向的构建-评估）存在争议：该计算模型更像解释性仿真而非面向利益相关者的设计制品。因此完整模式虽可行，但设计类型这一重要环节不够确定，宜人工复核。
- Confidence: 0.68

## promising_candidate: A probabilistic Bayesian inference model to investigate injury severity in automobile crashes

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113557
- Source outcome: Injury severity level (No injury / Minor injury / Major injury)
- Coding-agent outcome: 编码智能体行动所致严重不良系统后果的概率化严重性评估
- Decision: 该文构建并评估了基于BBN的概率推断模型、Web模拟器和系统级分类法，属于design-oriented build-evaluate；贝叶斯网络、互信息和缺失数据理论对设计有实质但偏方法论的塑造作用，因此理论-设计强度为moderate。源域结果“伤害严重度”是领域构成性的且被定量评估。向编码智能体的迁移需要将人身伤害严重性扩展为仓库/系统严重风险，机制上可用BBN做概率风险估计与what-if监督支持，但源文没有编码智能体证据，迁移链条存在一个重要的间接环节，因此未达到strong_candidate，保留为promising_candidate供人工复核。
- Confidence: 0.66

## promising_candidate: Measuring service quality based on customer emotion: An explainable AI approach

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114051
- Source outcome: Perceived service quality (low-quality service call detection)
- Coding-agent outcome: 用户对编码代理委托工作的感知服务质量（感知委托服务质量）
- Decision: 该文是理论导向的设计科学/构建-评估研究：明确引用设计科学范式，基于情绪动态理论和SERVQUAL设计特征与标注，构建并评估了自动服务质量测量IT工件；其结果'感知服务质量'在呼叫中心情境中是情境化的，且可映射为'用户对编码代理委托工作的感知服务质量'。但编码代理特异性为中等级别：源论文依赖客户语音情绪动态，而编码代理情境下需要将信号迁移到用户文本反馈，并需在定义和测量上重新情境化以避免退化为通用满意度；因此整体判定为promising_candidate而非strong_candidate。
- Confidence: 0.66

## promising_candidate: A social mechanism for task-oriented crowdsourcing recommendations

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113449
- Source outcome: Satisfaction with contribution
- Coding-agent outcome: 人类对自主编码代理生成代码变更的验收率
- Decision: 该文是设计导向的构建-评估研究：实现并实验评估了整合贡献者偏好、历史表现与社会影响的任务型众包推荐机制。社会影响理论对设计有中等程度作用（moderate）。最可迁移的已评估结果是'对贡献的满意度/验收'，在编码代理场景可重定位为人类对代理生成代码变更的验收率，具有较强的编码代理非替代性。但源理论到该结果的因果链较间接，且源结果构念整体仍偏推荐系统通用度量，尚不足以作为强候选；因此列为promising_candidate，需人工全文复核。目标匹配为否。
- Confidence: 0.65

## promising_candidate: DarkNetExplorer (DNE): Exploring dark multi-layer networks beyond the resolution limit

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113537
- Source outcome: Detection of 'small' and 'good' covert communities
- Coding-agent outcome: 目标相关依赖社区的选择质量（Goal-Relevant Dependency Community Selection）
- Decision: 该文属于设计导向的构建与评估：实现了DNE算法并在三个真实暗网上与基线比较。理论到设计的联系为中等：随机游走、Sageman枢纽启发式和渐近Surprise确实塑造了算法特征，但没有显式设计科学框架或正式设计原则。源文结果'小且好的隐蔽社区'具有领域语境化意义，且'识别隐蔽头目'是领域构成性结果。向编码智能体的迁移有真实机制——将多层随机游走+无分辨率限制聚类映射为仓库依赖社区选择和枢纽觉察——但需要较大概念适配，且源文没有任务语义或执行反馈，因此迁移强度为中等而非强。综合判断为promising_candidate，建议人工复核。
- Confidence: 0.65

## promising_candidate: How Do Individuals Understand Multiple Conceptual Modeling Scripts?

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00750
- Source outcome: Domain understanding (problem-solving performance)
- Coding-agent outcome: 多源仓库理解中的跨源整合可靠性（cross-source integration reliability in repository understanding）
- Decision: 该文是设计导向的实验研究：构建了系统操纵本体重叠（OO）和组合本体完整性（COC）的UML脚本组合并进行了实验评估，理论到设计的链路清晰（表示理论、Recker & Green理论、认知负荷理论），核心结果'领域理解'是情境化的且定量测量。向编码智能体的迁移有明确机制：将人类多脚本整合中的适度重叠原则映射为智能体多源仓库上下文的整合与冗余控制。但该迁移依赖于人类认知负荷与LLM上下文限制之间的类比，且原文并非关于软件工件或编码代理，因此编码智能体特异性为中等，属于promising_candidate而非strong_candidate。
- Confidence: 0.65

## promising_candidate: A Warning Approach to Mitigating Bandwagon Bias in Online Ratings: Theoretical Analysis and Experimental Investigations

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00817
- Source outcome: Reduced bandwagon bias (greater DDAR in bias-induced groups)
- Coding-agent outcome: 上下文从众偏差缓解（生成代码向仓库主流模式/提示锚点的不当靠近）
- Decision: 该论文是设计导向的构建-评估研究：基于FCM和价值理论设计了风险提示+排名任务警告策略，并通过四个实验评估其对在线评分从众偏差和过度修正的缓解。理论到设计的映射明确。结果变量DDAR具有领域构成性。向编码代理迁移时，可将FCM的偏差纠正机制转化为提示层面的预检-校准设计原则，形成两个候选结果：上下文从众偏差缓解和去偏提示的校准式纠正。迁移依赖编码代理特有的仓库级上下文、自主生成代码和可执行副作用等条件，非静态IDE或普通聊天机器人可替代。但由于FCM是人类心理模型，迁移属于边界条件扩展，尚待实证，因此评为promising_candidate而非strong_candidate。
- Confidence: 0.65

## promising_candidate: Champions for Social Good: How Can We Discover Social Sentiment and Attitude-Driven Patterns in Prosocial Communication?

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00810
- Source outcome: Social informedness (of UNHCR champions' followers)
- Coding-agent outcome: 委托人对编码代理自主工作的知情度（delegator informedness about the coding agent's delegated work）
- Decision: 该文是显式设计科学研究：构建并实例化了五步设计科学数据分析框架，提出了社会知情度理论并用P1-P4命题将其与分析构念相连，评估了情感、态度和外联结果。源结果（社会知情度）具有难民危机领域构成性，且可机制化迁移为'委托人对编码代理自主工作的知情度'这一编码代理设计目标。但由于理论到框架设计的联系为中等强度、社会知情度仅为代理指标而非框架直接产生的效果，迁移仍需额外概念重构，故判定为promising_candidate而非strong_candidate。
- Confidence: 0.65

## promising_candidate: On the Same Page? What Users Benefit from a Desktop View on Mobile Devices

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1140
- Source outcome: Decision accuracy (decision inaccuracy)
- Coding-agent outcome: 目标/需求一致的代码修改准确性
- Decision: 该文构建并评估了移动IA与桌面IA两种信息架构的在线实验平台，属于design_oriented_build_evaluate；努力-准确性框架对IA操作化及假设具有明确的生成性作用，但主要体现为对预测机制的理论锚定而非正式设计原则推导，理论-设计联系为moderate。主要结果决策准确性有情境化操作化（偏好一致的WADD距离），向coding agent的转移是可信的机制转移（信息架构影响自主修改的目标一致性），但源理论针对人类认知努力，agent上下文/计算资源是其边界扩展，且源结果本身比较接近通用决策准确性，因此整体是promising_candidate而非strong_candidate。
- Confidence: 0.65

## promising_candidate: Predicting online customer purchase: The integration of customer characteristics and browsing patterns

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114105
- Source outcome: Purchase behavior (session-level purchase conversion)
- Coding-agent outcome: 编码代理任务完成率（委托开发目标的成功达成）
- Decision: 论文构建并评估了整合RFM客户特征与图指标浏览模式的会话级购买预测模型和K-means会话级细分，属于design_oriented_build_evaluate；AIDA、IFT、图理论和RFM对设计有中等程度的引导，但理论到具体设计要求的链接不够完整，也未采用正式DSR方法。购买转化和会话级细分在电商语境下具有具体意义，且可以映射到编码代理的任务完成率预测和行为模式细分，依赖自主多步、工具副作用、验证反馈等代理特有条件。由于理论驱动强度为中等、设计类型非显式DSR、转移机制主要基于类比，完整源模式尚未达到strong_candidate，故保留为promising_candidate供人工复核。
- Confidence: 0.65

## promising_candidate: Ruckus in the Rentals, Seeking New Arrangements: Remedying the Impact of Home-Sharing on Urban Noise

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/18049
- Source outcome: Noise_Complaints (urban noise externality)
- Coding-agent outcome: 代码仓库'噪音'遏制（agentic unintended-change containment）
- Decision: 该文通过经验研究建立'房产使用增加城市噪音、空间/时间集中通过威慑机制减弱这一效应'，并提出和仿真评估了一个排名助推算法（设计导向的构建与评估）。理论到设计为中等强度（威慑理论和信息供给启发了助推算法）；源结果'噪音投诉'具有领域构成性，且可以转移到编码代理的'仓库外部性遏制'这一新结果上，机制为非替代性的编码代理场景所特有（自主多步修改和测试反馈）。但源论文不是正式设计科学研究，艺术件仅为仿真，转移为类比性中等强度，故列为promising_candidate供人工审核。
- Confidence: 0.65

## promising_candidate: Exploring the value of IoT data as an enabler of the transformation towards servitization: an action design research approach

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2046515
- Source outcome: Product-in-use insights / exploitative business insights
- Coding-agent outcome: 代码/制品在用洞见（runtime-grounding artifact-in-use insight）
- Decision: 该文是明确的ADR设计研究（explicit_design_science），构建并评估了整合ERP/IoT数据的PSP。理论到设计的联系为中等：RBV主要作为价值论证视角，blackboxing/product-in-use模型更直接地塑造了设计原则。被评价的'产品在用洞见'具有来源领域特殊性，可向编码智能体的'运行时制品在用洞见'做有机制的迁移，但需要较多概念重构和运行可观测性假设；同时论文对结果的评价以质性访谈为主，理论机制尚不精细。因此判定为promising_candidate，保留人工复核，不设为strong_candidate。
- Confidence: 0.64

## promising_candidate: Analytics with digital-twinning: A decision support system for maintaining a resilient port

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113496
- Source outcome: Port resilience level R(s)
- Coding-agent outcome: 资源中断下的编码代理韧性（coding-agent resource-disruption resilience）
- Decision: 该文属于 design_oriented_build_evaluate：实际构建并评估了数字孪生 DSS。韧性理论/构造和 OCBA 方法共同塑造了恢复分析与韧性分析模块，但理论到设计的连接是中等强度而非显式设计科学推导。被评估的港口韧性是领域构成性结果，且可被重新语境化为编码代理在资源中断下的任务韧性，具有较强代理特异性；但源文无任何编码代理内容，且数字孪生-OCBA 机制向代理沙箱的迁移需要额外概念构建和验证。因此判为 promising_candidate，保留人工复核，不设为 target_match。
- Confidence: 0.63

## promising_candidate: Irrationality-Aware Human Machine Collaboration: Mitigating Alterfactual Irrationality in Copy Trading

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0591
- Source outcome: follow rate-loss rate curve under contraction
- Coding-agent outcome: 自主行动预算下的缺陷率（defect rate at autonomy budget）
- Decision: 该文是设计导向的构建-评估研究：提出 IA-HMC 框架、RXGBoost 正则化方法和 contraction 方法并在跟单交易数据上定量评估。理论到设计为中等强度：bounded rationality、IIA、source credibility、salience theory 影响了 alterfactual irrationality 的定义和两类正则项的设计，但损失函数的形式化与理论之间的距离仍需人工判断。最优候选 outcome 是 follow rate-loss rate 权衡，具有领域构成性，且到 coding agent 的'自主行动预算下缺陷率'映射机制清晰、非替代性强。不过由于源论文完全不涉及 coding agent，整个转移依赖我们的分析推断，加之理论-设计链接为中等，故评为 promising_candidate 而非 strong_candidate。
- Confidence: 0.63

## promising_candidate: A group decision-making approach for exploring trends in the development of the healthcare industry in Taiwan

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113447
- Source outcome: Influential weight and priority ranking of MHDTs
- Coding-agent outcome: 影响感知的代码改动优先级（Influence-aware change prioritization）
- Decision: 本文是一个设计导向的构建-评估研究：构建并评估了修改版 Z-DEMATEL 决策模型，Z-numbers 和 DEMATEL 对设计有明确的生成性作用，评估结果为医疗健康发展趋势的影响权重、排序和因果网络。最有希望的转移是利用 DEMATEL 的影响权重/因果识别机制，为编码智能体设计‘影响感知的代码改动优先级’或‘因果变更识别’目标，这依赖仓库规模上下文、自主多步规划、可执行工件的相互依赖以及测试反馈等智能体特性。但源结果在方法上仍是通用 MCDM 权重，且论文未涉及代码仓库或软件工程，转移需要新的操作化和验证，因此不是 strong_candidate，而应作为 promising_candidate 供人工复审。
- Confidence: 0.62

## promising_candidate: A new approximate belief rule base expert system for complex system modelling

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113558
- Source outcome: Interpretability
- Coding-agent outcome: 自主代码修改的基于证据的可追溯性（evidential traceability）
- Decision: 该文是面向构建-评估的正式建模研究：提出了 ABRB 专家系统并用锂电池健康状态案例评估；其设计受 BRB/ER、互信息、D-S 规则等正式理论约束，从理论到结构机制可追踪。但并非显式 IS 设计科学研究，理论到设计的性质是形式化建模而非行为/设计理论驱动，主要量化结果是通用 MSE。最有希望的迁移是将'信念分布输出/可解释性'机制映射为编码代理修改的可追溯证据，但来源对可解释性的评估偏定性，迁移强度为中等，因此保留为 promising_candidate 供人工全文复审。
- Confidence: 0.62

## promising_candidate: Choosing Response Strategies in Social Media Crisis Communication: An Evolutionary Game Theory Perspective

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2020.103371
- Source outcome: Netizens' condemnation and transmission strategy (T strategy) proportion
- Coding-agent outcome: 维护者对编码代理行为的负面反应/拒绝率
- Decision: 该文构建并评估了一个基于进化博弈论的社会媒体危机沟通演化博弈模型，进化博弈论和有限理性对模型设计有强生成作用；源端结果如T策略比例具有领域构成性。向编码代理迁移时，可将'维护者负面反应/拒绝率'作为候选设计目标，机制映射有一定合理性。但源文属于形式模型仿真，并非设计科学的实证干预评价，'设计-结果'链条存在明显间接性，故列为 promising_candidate 而非 strong_candidate。
- Confidence: 0.62

## promising_candidate: DMN4DQ: When data quality meets DMN

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113450
- Source outcome: Recommendation on the potential usability of a data record (BR.DUD)
- Coding-agent outcome: 编码代理产出物的可用性推荐（Use/Revise/Discard gate recommendation）
- Decision: 该论文是设计导向的构建-评估研究：设计了DMN4DQ方法、DMN决策表层级和dmn4spark工具，并用真实数据集评估了数据可用性推荐、质量评估等级和根因诊断。理论（数据质量情境依赖、测量-评估分离、数据质量维度模型）确实塑造了设计，但理论到设计多为概念框架层面的中等强度映射，而非严格的设计理论推导。源结果'数据可用性推荐'具有情境化操作化，可迁移为编码代理产出物的Use/Revise/Discard门控推荐，且编码代理特异性较强（依赖委托目标、仓库级副作用、概率性错误等）。但转移需要较大的概念适配，源域并非代码/代理域，故整体评为promising_candidate而非strong_candidate，值得人工全文复核。
- Confidence: 0.62

## promising_candidate: Design Principles for Robust Fraud Detection:  The Case of Stock Market Manipulations

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00657
- Source outcome: Automated identification of suspicious documents (suspicious vs. non-suspicious classification recall/precision)
- Coding-agent outcome: 高风险代码变更的校准升级/人工接管（calibrated escalation of suspicious code changes）
- Decision: 该文是明确的设计科学研究：提出设计需求/原则/特征，并构建五类分类器；营销、金融经济学和集成学习理论对设计特征有直接生成作用；核心结果“面对欺诈者countermeasures的鲁棒性”被定量评估且具有源领域情境化含义。编码侧迁移最具潜力的是“高风险变更的校准升级/人工接管”（候选2），它依赖编码智能体的自主工具操作、权限边界和人机交接，非替代性较强；但源核心理论（营销/金融）到这一编码目标的映射是间接的，需要结合软件正确性证据和人机协作理论重新接地。因此整体为 promising_candidate，而非 strong_candidate。
- Confidence: 0.62

## promising_candidate: Designing Promotional Incentives to Embrace Social Sharing: Evidence from Field and Online Experiments

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15352
- Source outcome: Sender's Successful Referral
- Coding-agent outcome: 编码代理的可验证委托/交接成功率（Verifiable Delegation Handoff Success）
- Decision: 该文属于设计导向的构建与评估研究（设计并实例化了促销激励邮件并进行了现场/在线实验评估），而非形式化设计科学研究；理论（社会形象、感知专属感等）对设计维度和假设有生成作用，但缺少显式设计原则，故理论-设计强度为中等。被评估的结果中‘成功推荐’具有情境化含义，且可映射到多代理编码系统中的‘委托/交接成功’，但该迁移依赖对人类亲社会动机的类比，尚未达到强可辩护的机制迁移。因此整体为 promising_candidate，需要人工全文复审以决定是否纳入目标库。
- Confidence: 0.62

## promising_candidate: Establishing a frame of reference for measuring disaster resilience

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113406
- Source outcome: Predicted disaster resilience (R)
- Coding-agent outcome: 基于显式参照系的编码代理韧性（Coding-Agent Resilience with Explicit Frame of Reference）
- Decision: 该文构建并评估了一个改进的韧性测量模型，利用韧性三角和MTPD/MBCO等构造推导阈值参数，并在Sandy案例中定量计算三个维度的韧性值。源结果'韧性值'具有领域情境化含义，可类比迁移到编码代理作为基于显式参照系的韧性度量。但理论到设计强度为中等，且转移依赖测量类比而非经过检验的因果设计机制，韧性构造本身并非编码代理独有，因此不足以判定为强候选，但值得人工全文复核。
- Confidence: 0.62

## promising_candidate: Mitigating the Adverse Effect of Monetary Incentives on Voluntary Contributions Online

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870385
- Source outcome: Contribution quality (transcription error rate; WError and CError)
- Coding-agent outcome: 自主代码修改的语义正确性与质量保持（激励/目标委托下的质量鲁棒性）
- Decision: 源论文属于design_oriented_build_evaluate：它提出并随机评估了目标设定与挑战寻求两种干预策略，且理论到设计链条清晰（self-perception/motivation crowding解释问题，goal-setting theory和挑战寻求构念直接形成干预消息）。被评估的贡献质量是情境化的结果，并具备可迁移到编码代理的潜力。但论文不是正式DSR，且迁移依赖将人类内在动机/利他归因机制类比为LLM代理对提示与奖励框架的注意力调节，机制强度为中等，因此列为promising_candidate而非strong_candidate。
- Confidence: 0.62

## promising_candidate: Neighbor-aware review helpfulness prediction

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113581
- Source outcome: Review helpfulness prediction accuracy
- Coding-agent outcome: 上下文校准的代码变更有用性评估（neighbor-aware code-change helpfulness assessment）
- Decision: 论文构建并评估了 NAP 端到端模型，属于 design_oriented_build_evaluate；顺序偏差/社会影响和同化-对比效应为模型设计提供了中等强度的理论到设计映射。被评估的结果（评论有帮助性预测准确率及邻居上下文效应）具有评论平台的情境特异性。向编码智能体的迁移是清晰但需要重构的：将'显示序列中的邻居评论'重解释为'仓库/会话中相互依赖的代码变更'，可形成上下文校准的代码变更有用性评估。由于理论到设计的链接为中等且迁移为推断性扩展，而非源论文直接证据，定为 promising_candidate 供人工复核。
- Confidence: 0.62

## promising_candidate: The Effectiveness of Social Norms in Fighting Fake News on Social Media

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870389
- Source outcome: fake news reporting behavior (amount of reported fake news)
- Coding-agent outcome: 编码代理对可疑代码变更（潜在错误、幻觉依赖、高风险操作）的校准化标记/上报行为
- Decision: 该文属于‘design_oriented_build_evaluate’：构建并评估了一个社交媒体信息流原型中的社会规范消息设计；规范焦点理论和社会规范理论对设计特征（应然性文本、描述性举报计数）有明确且强的生成作用；主要结果‘虚假新闻举报行为’是领域构成性的。不过，向编码代理的迁移需要较大概念跳跃：从‘人类用户在界面中受社会规范影响而举报’变为‘LLM编码代理在提示/协议规范下标记自身生成的可疑变更’。虽然该结果具有编码代理特异性（自治多步、仓库副作用、概率性错误），但社会规范理论作用于机器代理的机制尚属类比/边界扩展，迁移强度为中等。因此整体为promising_candidate而非strong_candidate。
- Confidence: 0.62

## promising_candidate: An Ontology of Emotion Process to Support Sentiment Analysis

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00749
- Source outcome: Ability to identify customers' appraisals and affect regarding a product
- Coding-agent outcome: 基于评价-情感区分的编码智能体行动准备（校准的自动修复/解释/回滚/升级决策）
- Decision: 论文是显式设计科学研究，Frijda情绪过程理论和Russell/Scherer维度理论强驱动本体、词典和原型设计，多级评估存在。但正式评估主要落在通用感知构念（有用性、帮助性、深入分析支持）上，源域特异性不足。唯一较有希望的候选是设计层面评价的‘识别客户评价与情感’能力，可类比迁移为编码智能体基于评价-情感区分来选择行动准备/升级，但该迁移是跨域类比，且源论文未评估响应策略的实际效果，因此按规则判为promising而非strong；target_match=false。
- Confidence: 0.62

## promising_candidate: Cognitive Challenges in Human–Artificial Intelligence Collaboration: Investigating the Path Toward Productive Delegation

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1079
- Source outcome: Delegation performance / joint classification accuracy under delegation and inversion
- Coding-agent outcome: 编码代理与人类开发者之间的校准式任务委托/交接质量（calibrated delegation and handoff）
- Decision: 文章构建并评估了人类-AI双向委托机制（delegation/inversion及strategy explained/enforced），符合design_oriented_build_evaluate的宽泛定义；元知识与实例级互补性理论确实塑造了设计。但文章本质是行为实验而非正式设计科学研究，理论对具体设计特征的生成作用为中等；最值得迁移的结果是委托/交接绩效，可映射为编码代理与开发者的校准式任务委托，具有强编码代理特异性。由于设计类型和理论-设计链存在一定模糊性，判为promising_candidate供人工复核。
- Confidence: 0.62

## promising_candidate: Comparing low sensory enabling (<scp>LSE</scp>) and high sensory enabling (<scp>HSE</scp>) virtual product presentation modes in e‐commerce

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12382
- Source outcome: Perceived diagnosticity
- Coding-agent outcome: 代理产出可诊断性（perceived diagnosticity of agent-generated work products）
- Decision: 该文属于设计导向的构建-评估研究：作者实际构建了LSE和HSE两种虚拟产品展示模式并开展实验评估。理论（态度理论、线索累加理论、重复学习与记忆、Sheridan临场感决定因素）以中等等强度指导了设计和假设推导。最适合迁移的已评估结果是感知诊断性：其源域含义和操作化具有情境特异性，且可被重新阐释为'编码代理产出可诊断性'，该迁移依赖代理的多步工件生产、仓库级上下文和执行反馈等代理特有条件。但由于源文并未使用设计科学方法论，理论到设计的连接多为假设推导而非显式设计原则，且感知诊断性迁移需要'感官线索→信息线索'的概念转换，因此完整的迁移链条尚需人工全文复核，定为promising_candidate而非strong_candidate。
- Confidence: 0.62

## promising_candidate: Designing Core-Selecting Payment Rules: A Computational Search Approach

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2022.1108
- Source outcome: INCENTIVES_M,f
- Coding-agent outcome: 编码智能体的代理目标忠实度（规格博弈抵抗）
- Decision: 本文是明确的机制设计构建-评估研究，理论到设计链路强（核心约束、VCG、BNE、Shapley 值均直接塑造设计框架与规则选择），且有一个领域构成性结果——INCENTIVES 度量。将该激励度量转移到编码智能体的'规格博弈抵抗'是合理但有条件的：需要将拍卖支付规则类比为奖励/验证规则，将错误报告类比为智能体偏离用户意图。这一转移依赖编码智能体的多步自主性、可执行构件、测试反馈和概率性伪正确产物等特征，具有较强非替代性，但源理论到 LLM 对齐的类比需要额外结合 AI 对齐理论，因此不能认定为强候选，保留为 promising_candidate 供人工评审。
- Confidence: 0.62

## promising_candidate: Developing a Composite Measure to Represent Information Flows in Networks: Evidence from a Stock Market

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1066
- Source outcome: AbnReturn (abnormal returns)
- Coding-agent outcome: 编码代理场景下的‘异常回归风险’（unexpected post-change behavioral deviation）
- Decision: 源文是明确的设计科学研究，构建了EAC度量并在股票市场中用异常收益等结果变量做了大规模预测评估；理论（特征向量中心性、有限注意力、共注意）对设计有可见但在形式化设计原则层面较间接的作用。异常收益是金融领域构成性结果，具备源域特异性。将其机制迁移到编码代理的‘残余回归风险’在逻辑上成立，但代理特异性为中等：若不结合代理的自主上下文分配和验证干预，EAC式指标会退化为普通缺陷预测/共变更分析。因此判定为 promising_candidate 而非 strong_candidate。
- Confidence: 0.62

## promising_candidate: Do You Really Know if It’s True? How Asking Users to Rate Stories Affects Belief in Fake News on Social Media

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1090
- Source outcome: Believability of news headlines
- Coding-agent outcome: 生成代码的认知校准（calibrated epistemic certainty in generated code）——降低未经证实的确定性
- Decision: 该论文设计并实验评估了自指式评分提示这一界面干预，理论（双加工理论、自传体记忆检索、感觉正确性）到设计机制的路径清晰，并在行为（believability）和神经（EEG额叶激活）层面进行了评估。最有希望的结果“降低对虚假新闻的相信”具有领域特定含义，且可类比映射到编码智能体的“生成代码认知校准/降低未经证实的确定性”，该映射依赖编码智能体特有的概率生成、工具执行和测试反馈等条件，因此具有非替代性。然而，这一转移本质上是将人类认知理论类推至基础模型智能体，文章本身并未涉及AI，转移强度的证据链为中等，因此标为 promising_candidate 而非 strong_candidate。
- Confidence: 0.62

## promising_candidate: Helping at NASA: Guidelines for using process consultation to develop impactful research

- Year/journal: 2022 / Information and Organization
- DOI: 10.1016/j.infoandorg.2022.100388
- Source outcome: Trust (as outcome and enabler of engaged scholarship)
- Coding-agent outcome: 对自主编码智能体的校准信任（calibrated trust in autonomous coding agents）
- Decision: 本文并非正式DSR，但描述了过程咨询干预并进行了定性评估，属于设计导向的构建-评估。过程咨询和参与式学术为干预设计提供了中等强度的理论-设计连接。结果方面，信任和感知帮助在NASA语境中有情境化含义。向编码智能体的转移是类比性的：过程咨询的“联合诊断、逐步建立信任、传递自助能力”可映射到智能体与开发者的委托-监督关系，构成有潜力的编码智能体设计目标。然而，理论到设计与转移到AI的路径至少有两个环节是中等强度或类比性的，未达到强候选标准，但值得人工全文复核。
- Confidence: 0.62

## promising_candidate: Heuristics and sensitivity analyses to guide replenishment decisions for red blood cells with random transfer

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113685
- Source outcome: Wastage rate
- Coding-agent outcome: 过期/冲突工件弃置率（stale-artifact discard rate）
- Decision: 该文属于设计导向的构建-评估：构建了两种考虑随机转移的补货启发式，并基于Nahmias/Pierskalla库存理论、base stock策略和critical ratio进行了理论到设计的明确推导；模拟评估了总成本、服务水平和浪费率。浪费率是情境化的领域结果，且可迁移为编码代理的‘过期/冲突工件弃置率’：编码代理在自主多步骤生成可执行工件时面临来自其他代理/外部提交的随机转移，源文的库存启发式机制可指导代理在生成/验证规划中纳入外部变更分布。但该迁移需要将物理库存概念重新解释为代码仓库状态，且源文并未涉及软件代理，因此整体为promising_candidate而非strong_candidate。
- Confidence: 0.62

## promising_candidate: Multi-Party Certification on Blockchain and Its Impact in the Market for Lemons

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063555
- Source outcome: proportion of lemons sold (and peaches sold)
- Coding-agent outcome: 被接受的柠檬型编码智能体变更比例
- Decision: 这是一项经济模型+实验室市场实验研究，构建了 CarMarket/CarCerti 并评估了市场结果，因此属于 design_oriented_build_evaluate；信号理论、柠檬市场理论、社会技术工件框架和锚定效应对多主体认证这一干预及其信号 fit 机制有清晰但非正式的塑造作用，故 theory-to-design 为 moderate。评估结果中，柠檬/桃子交易比例、买卖双方相对收益等是领域情境化结果。向编码智能体迁移时，可形成“智能体输出质量信号 fit/柠檬型变更比例”等设计目标，并依赖概率性幻觉、仓库副作用等独特条件；但来源不是正式 DSR，且信号 fit 未直接测量，迁移需人工确认，因此为 promising_candidate 而非 strong_candidate。
- Confidence: 0.62

## promising_candidate: That's interesting: An examination of interest theory and self‐determination in organisational cybersecurity training

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12374
- Source outcome: Actual learning effort (EFF)
- Coding-agent outcome: 编码代理在委派软件开发任务中的校准化持久努力（calibrated effortful persistence）
- Decision: 论文构建并评估了一个基于Web的网络安全培训程序，属于design_oriented_build_evaluate；SDT与兴趣理论对培训特征（自主性按钮、反馈、最优挑战）有一定的设计作用，但证据部分隐含，理论到设计强度为moderate；实际学习努力（EFF）在源领域被情境化为复杂网络安全培训中的坚持性，其到“编码代理校准化持久努力”的迁移依赖于代理的多步迭代、工具使用和测试反馈等特定条件，具备中等强度的非替代性；但多个环节（理论到设计、源结果特定性、跨本体映射）仍需要人工审阅，因此列为promising_candidate而非strong_candidate。
- Confidence: 0.62

## promising_candidate: When Constructs Become Obsolete: A Systematic Approach to Evaluating and Updating Constructs for Information Systems Research

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15516
- Source outcome: IT Innovative Use (Innovative Use of IT)
- Coding-agent outcome: 编码代理创新型使用（Agentic Innovative Use）
- Decision: 该文是一种构念更新/方法论文，虽不属正式设计科学研究，但构建了新的ITSE构念与量表并进行了实证评估，属于design-oriented build-and-evaluate。理论（自我效能理论、身份理论）对构念设计有强影响。最有希望的转化结果是‘编码代理创新型使用’：来源中的创新型IT使用具有情境化意义，转移到编码代理场景后，代理的自主多步规划和工具副作用创造了新的创新维度；该转移具有较强代理特异性，但源论文没有设计代理系统本身而只是测量构念，因此设计机制映射为中等强度。综合判断为promising_candidate，而非strong_candidate，需要人工全文审查以确认能否形成真正的编码代理设计目标。
- Confidence: 0.62

## promising_candidate: Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1125
- Source outcome: diff_strength (increase in password strength)
- Coding-agent outcome: 反馈后代码修订的鲁棒性提升（feedback-triggered code-revision robustness）
- Decision: 源论文是明确的设计科学研究，ELM到设计要素的映射强，评价结果在密码安全领域具有情境特异性；候选结果“反馈后修订鲁棒性”依赖编码代理的自主多步、测试反馈和自我修正能力，非静态工具可替代。但由于ELM从人类说服向代理推理的迁移属于类比式扩展，重要证据链为中等强度，故保留为promising_candidate供人工复核。
- Confidence: 0.62

## promising_candidate: Cost-based analysis of the impact of data completeness and representational consistency

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114044
- Source outcome: P_correct (percentage of participants finding correct solutions)
- Coding-agent outcome: 编码代理任务解决率（在受仓库数据质量影响下能否成功完成多步编码任务）
- Decision: 论文属设计导向的构建-评估：构建三个集成数据库并实验评估；成本式数据质量框架（fitness for use）中等程度地为结果指标和实验设计提供依据；结果变量（解决能力、时间、数据质量问题查询数）在数据集成质量评估情境中有情境化含义，并可通过'解决编码任务的成本'机制转换到编码代理。由于理论-设计联系与结果情境化均偏中等而非强，且无显式DSR标签，判定为promising_candidate而非strong_candidate。
- Confidence: 0.62

## promising_candidate: Customer Complaint Avoidance: A Randomized Field Experiment of Platform Governance Based on Value Co-Creation and Appropriation

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17000
- Source outcome: complaints (verified customer complaints)
- Coding-agent outcome: 编码代理的用户投诉预防（user-complaint avoidance in delegated coding tasks）
- Decision: 来源论文构建了提醒消息这一治理人工物并进行了随机现场实验评估，价值共创与价值获取理论明确驱动消息特征与假设（theory-to-design 强）；结果变量为经验证的顾客投诉，操作化与 P2P 租赁平台领域紧密相关。最可行的迁移是将该治理消息机制重新实例化为编码代理生态中的“用户投诉预防”设计目标，但其迁移依赖于将人类动机理论结合到 LLM/代理激励设计中，故编码代理特异性强但迁移证据为推断性，因此保留为 promising_candidate 供人工复核。
- Confidence: 0.62

## promising_candidate: Design Theory for Societal Digital Transformation: The Case of Digital Global Health

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00816
- Source outcome: visibility of the whole / data of the whole (DP5)
- Coding-agent outcome: 仓库级变更与影响的完整可见性（全貌/未表征部分）
- Decision: 该文是明确的设计理论/设计原则研究（explicit_design_science），基于25年DHIS2/HISP干预案例；Zuboff informate、知识公地、复杂性理论等推动具体设计原则（如DP5全貌可见性）。但其评估多为质性与历史叙事，缺乏正式结果测量；转移至编码智能体需要对'全貌可见性'做实质性概念扩展（从人群覆盖到仓库级变更影响），因此整体评为 promising_candidate 而非 strong_candidate。最佳结果候选为'全貌可见性'。
- Confidence: 0.62

## promising_candidate: Optional Verification and Signaling in Online Matching Markets: Evidence from a Randomized Field Experiment

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1194
- Source outcome: verify (verification opt-in decision)
- Coding-agent outcome: 智能体可审计性/可验证性的可选采用
- Decision: 论文属于设计导向的搭建并评估（可选手机号验证机制），信号理论对设计有强指导作用，且有定量评估结果（验证采纳、消息收/发、匹配）。来源域结果具有婚恋匹配市场的语境特定性。最有希望的迁移是将‘可选、可见、有成本的验证作为可信信号’机制扩展到编码智能体的可审计性采用，依赖智能体自主多步执行、工具副作用和概率性错误等特有条件；但这一迁移属于推断性重构，源文没有任何编码智能体内容，且‘手机号验证-PII分享’与‘执行痕迹审计’之间的类比需要额外的理论边界扩展。因此保留为promising_candidate供人工复核，而非strong_candidate。
- Confidence: 0.62

## promising_candidate: Pushing Yourself Harder: The Effects of Mobile Touch Modes on Users’ Self-Regulation

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1155
- Source outcome: self-regulation
- Coding-agent outcome: 开发者在委派编码代理时的自我调节：抵制接受貌似合理但有缺陷的代理输出，坚持验证与约束保持
- Decision: 该文属于‘设计导向的构建-评估’研究：作者构建了三种移动实验应用并操纵力感应触控模式，基于具身认知理论提出并检验了按压增强自我调节的假设，理论到设计联结强，结果在健康领域中具有情境化的操作化。然而，向编码代理的迁移较弱：源机制依赖人类身体的力觉体验，迁移至编码代理界面只能通过‘承诺动作’或‘确认仪式’的类比实现，编码代理特异性为中等而非强。因此保留为 promising_candidate 供人工复审，而不判为 strong_candidate。
- Confidence: 0.62

## promising_candidate: The Decoy Effect and Recommendation Systems

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1197
- Source outcome: No-choice option selection likelihood
- Coding-agent outcome: 用户对智能体变更集的整体接受度/委托持续性（避免‘诱饵式’低价值编辑）
- Decision: 该文构建并评估了一个推荐系统平台中的诱饵干预，属设计导向的构建-评估研究；说服理论为个性化/非个性化条件下的假设提供了中等强度的理论-设计关联。评估结果（no-choice、感知系统可靠性）在推荐情境中有情境化意义，且可映射到编码智能体中‘避免低拟合诱饵编辑以保持用户对变更集的接受/委托持续性’这一候选设计目标。但来源是消费选择的实验而非正式设计科学，且编码智能体迁移需要结合人机委托与软件工程情境的进一步理论化，因此保留为 promising_candidate。
- Confidence: 0.62

## promising_candidate: Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17316
- Source outcome: Explainability of exploit labeling (self-attention token weights)
- Coding-agent outcome: 自主代码修改的可审查性/理由保真度 (rationale fidelity of autonomous code changes)
- Decision: 该文是明确的计算设计科学研究，构建并严格评估了DTL-EL人工制品；DTL和自注意力机制确实塑造了设计特征（预初始化、层迁移、注意力），但理论到设计主要来自算法/数学框架而非行为或组织理论，属于中等强度。评估结果中最有迁移价值的是exploit标注的可解释性，可映射为编码智能体自主代码修改的可审查性/理由保真度，但其机制是将神经注意力重新解释为智能体的依赖追踪，属于有依据但需要边界扩展的转换。其他两个结果（目标域标注F1、误分类成本）也有迁移潜力，但编码智能体特异性或机制链路为中等。因此整体是promising candidate，而非strong candidate。
- Confidence: 0.62

## promising_candidate: Delays in Information Presentation Lead to Brain State Switching, Which Degrades User Performance, and There May Not Be Much We Can Do about It

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17680
- Source outcome: Brain state switching (during delay and during task following delay)
- Coding-agent outcome: 代理任务状态连续性（task-set continuity across execution-feedback delays）
- Decision: 该文并非正式设计科学研究，但Study 2构建并评估了四种延迟填充干预，符合设计导向的构建-评估模式；理论到设计的追溯较强（脑状态切换、默认模式网络和任务切换理论指导干预设计）。最具领域特异性的评估结果是脑状态切换（fMRI/t-SNE量化），可类比迁移为编码代理在异步工具反馈延迟中的任务状态连续性目标。然而，源文属于神经科学机制研究，设计干预未在代理场景验证，且脑机制到LLM代理的迁移本质上是类比，因此判定为promising而非strong。
- Confidence: 0.62

## promising_candidate: Encouraging Eco-driving with Post-trip Visualized Storytelling: An Experiment Combining Eye-Tracking and a Driving Simulator

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0332
- Source outcome: eco-driving behaviors
- Coding-agent outcome: 自主编码代理的编辑平稳性与运行稳定性
- Decision: 源论文采用构建-评估范式，基于建构水平理论与心理建构一致性设计了行程后可视化叙事干预，并在驾驶模拟器+眼动实验中定量评估了生态驾驶行为、态度及可行性与可欲性中介；源侧证据完整（design_oriented_build_evaluate，theory_to_design=strong）。最有前景的迁移是将“生态驾驶行为”重新实例化为“自主编码代理的编辑平稳性/运行稳定性”，或将以可行性/可欲性为中介的叙事机制迁移到人类监督者的代理变更校准；两者均具备较强代理特异性，但源理论基于人类心理，迁移到LLM代理需要额外的提示/记忆工程与实证检验，因此定为 promising_candidate 供人工全文复核。
- Confidence: 0.62

## promising_candidate: Generativity and Profitability on B2B Innovation Platforms: A Simulation-based Theory Development

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17710
- Source outcome: Generativity (of partners on-platform; total and average)
- Coding-agent outcome: 可集成生成性（integration-preserving generativity）
- Decision: 本文是仿真驱动的理论开发，构建并评估了一个 ABM 仿真模型，因此可视为设计导向的构建-评估研究；但未使用正式设计科学标签，且理论到设计的连接是中等强度（理论塑造仿真模型变量而非真实平台设计原则）。最有希望的成果是“生成性”，它在来源语境中是 B2B 创新平台的特定构念，迁移到编码代理需要扩展为“可集成生成性”，依赖委派目标追求、仓库级修改、工具执行和测试反馈等代理特定能力。该迁移机制合理但属于类比延伸，且需要实证校准，因此不能判定为强候选，但值得人工全文审查。
- Confidence: 0.62

## promising_candidate: Interleaved Design for E-Learning: Theory, Design, and Empirical Findings

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17206
- Source outcome: Reduction of learning performance disparities between weak and strong learners
- Coding-agent outcome: 弱/强编码代理在交错任务委派下的能力差距缩减
- Decision: 源论文是明确的设计科学研究：以认知负荷理论为内核理论，相关交错设计从理论到元需求、元设计、系统实例化和现场实验的链条完整；评估结果包括整体学习绩效和强弱学习者绩效差距缩减。绩效差距缩减是一个有领域语境的评估结果，且可以映射到“弱/强编码代理在相关交错任务委派下能力差距缩减”这一编码代理特异设计目标。但该迁移依赖从人类工作记忆/认知负荷到模型上下文窗口的类比，且源论文不涉及AI代理，因此编码代理特异性为中等而非极强。为了保证筛选准确，保留为 promising_candidate 供人工复审，而非 strong_candidate。
- Confidence: 0.62

## promising_candidate: Navigating the Digital Terrain of Prosocial Disclosures and Likability

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17700
- Source outcome: digital reaction of likes
- Coding-agent outcome: 编码代理工作汇报中的功劳归因校准与谦逊披露（calibrated credit attribution and humble disclosure）
- Decision: 该论文以attribution theory为核心，通过现场数据和实验评估了亲社会披露消息模板的不同设计特征（自我努力、提及他人、表达感谢、赞助商声誉）对点赞的影响；理论-设计链条强，结果likes是情境化的。但它不是形式化设计科学研究，且对编码代理的迁移依赖机制类比：将'受众对亲社会披露者的likability归因'映射为'开发者对编码代理工作汇报的信任/功劳归因'。编码代理特异性为中等而非强，因此保留为候选而非强候选。
- Confidence: 0.62

## promising_candidate: Study on the quality evaluation of mobile social media health information and the relationship with health information dissemination

- Year/journal: 2024 / Information & Management
- DOI: 10.1016/j.im.2024.103927
- Source outcome: Value of health information content
- Coding-agent outcome: 编码智能体变更提案的决策信息完整性/风险透明性
- Decision: 该文构建并实证检验了移动社交媒体健康信息质量评价体系，属于design_oriented_build_evaluate；ELM/用户感知理论和信源可信度模型为指标维度提供了中等强度的设计依据；'内容价值'维度是领域性较强的被评价结果，可映射为编码智能体变更提案的决策信息完整性/风险透明性。但源文的'设计'是测量工具而非干预型设计，理论到设计的链路部分隐含，且编码智能体转移是完全推断性的，尚未达到强候选标准，因此保留为promising_candidate供人工复核。
- Confidence: 0.62

## promising_candidate: The Contingent Effects of IS Certifications on the Trustworthiness of Websites

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00836
- Source outcome: Perceived trustworthiness (swift trustworthiness/trusting beliefs)
- Coding-agent outcome: 编程智能体的校准信任/可信赖感知
- Decision: 该文不是正式设计科学研究，但实际构建并操纵了网站设计（含/不含IS认证），并通过在线实验和现场实验评估了感知可信度和用户注册，符合design_oriented_build_evaluate。swift trust理论和认知吝啬鬼概念为IS认证的权变效应提供了明确机制，但理论主要用于推导假设而非设计原则，属于moderate。感知可信度是情境化结果，能够映射到编程智能体的信任校准；用户注册可迁移为对智能体产出的采纳/委托行为。不过，信任构念本身较通用，且来源论文未直接检验低于临界点时认证对注册的影响，因此整体为promising_candidate，需要人工复核。
- Confidence: 0.62

## promising_candidate: The information content of financial statement fraud risk: An ensemble learning approach

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2024.114231
- Source outcome: Future operational efficiency (Operational Efficiency t+1 to t+3)
- Coding-agent outcome: 代码库可持续运行健康度（sustainable repository operational health）
- Decision: 文章构建并评估了一个事前财务舞弊风险指数（design_oriented_build_evaluate），Baucus和Misangyi等理论确实指导了特征设计和“为什么/如何/如何表现”框架，但理论到集成学习算法与指数口径的链条部分隐含，故 theory_to_design 为 moderate。主要评估结果“未来运营效率”是情境化且有量化测量的公司运营构念，具备向编码代理迁移的潜力：可将“舞弊风险→持续运营低效”机制重构为“代理产物完整性风险→代码库可持续运行健康度”，依赖概率生成和仓库级副作用等独特代理能力。但源论文的“舞弊”涉故意性，代理误导是非故意的功能性伪真，且源结果为相关证据而非因果干预，迁移需进一步概念适配，因此定为 promising_candidate 而非 strong_candidate。
- Confidence: 0.62

## promising_candidate: Understanding decentralization of decision-making power in proof-of-stake blockchains: an agent-based simulation approach

- Year/journal: 2024 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2125840
- Source outcome: Decentralisation of decision-making power
- Coding-agent outcome: 代码变更决策权分散度（decentralization of code-change decision-making authority）
- Decision: 论文构建并实证验证了一个PoS区块链的ABM仿真模型，属于design_oriented_build_evaluate；CAS框架确实塑造了仿真模型结构，但理论到具体设计原则的链接是中等强度而非显式设计科学；核心结果变量'决策权去中心化'是领域构成性的且被定量评估。该结果到编码代理领域（代码变更决策权分散度）有可辩护但需要理论组合的迁移，因此整体模式合理但存在关键环节为中等强度，值得人工全文复核，而非直接作为strong_candidate。
- Confidence: 0.62

## promising_candidate: Weighted doubly robust learning: An uplift modeling technique for estimating mixed treatments' effect

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114060
- Source outcome: Treatment attribution
- Coding-agent outcome: 编程智能体动作级因果贡献归因
- Decision: 该文是 build-and-evaluate 的方法论文，构造了 WDRL 算法并做了合成/工业数据实验；Shapley value 与潜在结果框架确实塑造了处理归因的设计机制，但理论到设计的连接多为算法层而非形式化设计原则，强度为 moderate。最有希望的源结果是‘混合处理归因’（识别最有效营销处理），其含义和操作化依赖营销域顾客/收入语境，属于 contextualized。向编程智能体的迁移是：将多步智能体轨迹中的动作/工具视为非互斥混合处理，用 Shapley 归因和双重稳健估计估计每个动作对任务成功的边际贡献；该迁移依赖自主多步规划、仓库副作用、测试反馈等编码智能体特有条件，具有较强特异性但毕竟是对营销处理归因的重解释，且源论文未涉及代码领域，故评为 promising_candidate 供人工复核，而非 strong_candidate。
- Confidence: 0.62

## promising_candidate: Algorithms to the Rescue: Market Mechanisms for Consensual Trading of Unbiased Individual Data

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2024.1115
- Source outcome: Sample bias (B)
- Coding-agent outcome: 委托代码修改的覆盖代表性/覆盖偏差（coverage representativeness of delegated code changes）
- Decision: 该文是一个典型的‘构建-评估’型算法/机制设计研究：设计了RSP市场机制（第二补偿拍卖+相邻配对随机抽样），并用机制设计理论、k-anonymity和抽样理论指导设计，通过理论命题、仿真和真实数据集进行评价，理论到设计的链路强。最具转移潜力的结果是‘样本偏差’，其领域含义是隐私顾虑驱动的自我选择偏差，属于contextualized。然而，将该机制转移到编码代理场景需要显著边界扩展：把编码代理类比为拥有私有难度/不确定性的战略参与者，并把‘无偏数据样本’重构为‘委托代码修改的覆盖代表性’。该转移在机理上可辩护，但不是直接映射，且缺少对代理策略性报告的实证基础，因此整体为promising_candidate而非strong_candidate。
- Confidence: 0.62

## promising_candidate: Augmented Reality at Work: Attention Management and Its Impact on Work Performance

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18944
- Source outcome: Work attentiveness
- Coding-agent outcome: 开发者对自主编码智能体工作流的监督专注度（oversight attentiveness）
- Decision: 该文是设计导向的实地实验：作者配置了AR作业卡vs手机信息呈现的干预，并以分心理论和双任务干扰理论形成假设和实验操控。评价结果包括工作专注度、视觉绩效和动作绩效，均量化评估，且在飞机维修情境中有情境化操作化。最有希望的转移是把“工作专注度”重新情境化为“开发者对自主编码智能体工作流的监督专注度”，借助编码智能体的自主多步工作、动态人机交接和异步工作等独特条件，设计周边状态呈现以减少注意切换。但源文非正式设计科学研究，理论到设计主要体现为实验操控而非设计原则，且从人类视觉注意机制到人-AI监督界面的映射需要额外理论补充，因此整体为promising_candidate而非strong_candidate。
- Confidence: 0.62

## promising_candidate: Healthcare Cost Prediction for Heterogeneous Patient Profiles Using Deep Learning Models with Administrative Claims Data

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0643
- Source outcome: Overpayment and underpayment (payment discrepancy) reduction
- Coding-agent outcome: 复杂度校准的委托交付偏差（complexity-calibrated delivery discrepancy）
- Decision: 该文是面向设计、构建并评估的ISR论文：提出了通道式深度学习和多通道熵指数，并在支付偏差和高需求患者预测偏差上进行了量化评估。其理论到设计的联系属于中等强度——'sociotechnical considerations'和异质性构念确实塑造了设计，但没有严格形式化的命名理论。最可迁移的结果是'超额/不足支付'这一领域构成性结果，可被机制化迁移为编码代理的'复杂度校准的委托交付偏差'，且该结果依赖自主多步、仓库级操作等编码代理条件。由于理论链条偏松散、编码代理结果需大量概念重构，归为promising_candidate而非strong_candidate，保留人工复核。
- Confidence: 0.62

## promising_candidate: Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0358
- Source outcome: PEAD prediction performance (explained variance, EV)
- Coding-agent outcome: 编码代理目标漂移预测（Goal-Drift Prediction for Coding Agents）
- Decision: 该文是明确的设计型构建-评估研究（explicit design science），构建并评估了MTL预测框架（FinAux+GradPerp+MQT）。理论到设计存在较清晰但非完全显式的中等强度链接（MTL理论、PEAD机制、梯度加权方法）。最佳结果候选为PEAD预测性能（EV），其源领域特异性为contextualized，向编码代理的'目标漂移预测'转化具有强编码代理特异性和中等可辩护机制，但该转化需要重要的概念扩展和类比推理，且源论文未涉及编码代理。由于理论到设计强度为moderate、转移强度为moderate而非strong，整体为需人工复审的promising_candidate，而非strong_candidate。
- Confidence: 0.62

## promising_candidate: Socialize More, Pay Less: Randomized Field Experiments on Social Pricing

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1089
- Source outcome: Reciprocity in social bargaining interactions
- Coding-agent outcome: 多编码代理间的互惠帮助交换（含间接互惠）
- Decision: 该文属于设计导向的构建-评估研究：作者设计并随机田野实验评估了社交定价/社交砍价机制。理论（社会资本、社会美元效应、社会污名、社会比较、互惠）在一定程度上塑造了机制假设与实验2的异质性规则，属于中等强度理论到设计。评估结果中，利润为通用指标不可迁移；购买频率可迁移但编码代理特异性中等；互惠行为具有较强编码代理特异性（多代理帮助交换和间接互惠）。然而，源论文是营销领域田野实验而非IS设计科学研究，互惠是机制性/混合证据而非核心设计目标，且将人类互惠迁移到人工代理需要边界条件扩展，故整体为 promising_candidate 而非 strong_candidate。
- Confidence: 0.61

## promising_candidate: An approach to modelling complex ICT4D investment problems: towards a solution-oriented framework and data analytics methodology

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2021.1992306
- Source outcome: Relative efficiency of conversion (DEA efficiency score)
- Coding-agent outcome: 编码代理的委托目标→已验证代码变更的转化效率
- Decision: 该文构建并应用了一个面向ICT4D投资问题的理论框架与数据分析方法论，属于设计导向的构建-评估研究；NGA理论明显塑造了框架和命题，理论-设计强度为强。已评估的结果（如DEA转化效率、Malmquist生产率增长来源、ICT能力）具有领域情境性。最有前景的转化是将“转换效率”重构为编码代理的“委托目标→已验证代码变更的转化效率”，并借鉴NGA-效率分解机制指导代理评估与投资决策。但该转化需要较多类比推理，且源工件是分析方法论而非可直接部署的系统，因此编码代理特有性和机制迁移的强度为中等，需要人工全文评审确认。
- Confidence: 0.61

## promising_candidate: Measuring Brand Favorability Using Large-Scale Social Media Data

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1030
- Source outcome: Brand favorability score (model-based, adjusted for user positivity bias)
- Coding-agent outcome: 校准后的编码智能体能力/任务成功率估计
- Decision: 该文构建并评估了一个品牌好感度测量框架（概率图模型+分块MCMC），属于设计导向的构建-评估研究。设计受“方向性/正性反应偏误”理论构念驱动，强度为moderate。主要被评估结果（经用户正性偏误校正的品牌好感度）在品牌营销情境中有具体操作化并与BrandZ外部真值对照，源域特异性为contextualized。向编码智能体迁移时，可将用户正性偏误映射为智能体的乐观自述偏差、品牌好感度映射为经校准的任务成功率/能力度量，机制上有可辩护的对应关系，但该迁移需要实质性的概念重建，且非替代性为中等而非强。因此整体为promising_candidate，而非strong_candidate。
- Confidence: 0.6

## promising_candidate: Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870388
- Source outcome: OUD treatment barriers
- Coding-agent outcome: 编码智能体对隐性任务阻断约束的自主识别（latent task-blocking constraint detection）
- Decision: 该文是明确的计算设计科学研究：作者构建并评估了 SINDEL IT 工件，并在 Hevner 设计科学框架下提出设计原则；Distributional Hypothesis 和形态学/隐语研究对相似性网络设计有实质但不完全显式的生成作用（moderate）。被评估的结果——OUD 治疗障碍——具有领域构成性，不是通用绩效指标。将其迁移到编码智能体可以形成‘隐性任务阻断约束识别’这一新结果，且该结果依赖智能体的自主规划、仓库副作用和人工交接，非替代性较强；但该迁移属于概念类比，源文没有涉及 agent 行为，转换机制尚需结合 agent 规划与权限理论验证，故整体判为 promising_candidate 而非 strong_candidate。
- Confidence: 0.6

## promising_candidate: A critical assessment of consumer reviews: A hybrid NLP-based methodology

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113799
- Source outcome: Helpfulness (count of helpful votes)
- Coding-agent outcome: 智能体生成代码变更的可审查性/评审有用性（review helpfulness of agent-generated code changes）
- Decision: 源文章确实构建并评估了理论驱动的NLP预测方法论，Shannon熵和Dual Process Theory到预测变量设计之间有明确可追溯关系，评价结果变量‘helpfulness votes’具有电商领域特定性。但文章并非正式设计科学研究，更接近经验建模研究；向编码智能体‘可审查性’的迁移是合理且较有前景的类比迁移，但源文与代码/智能体无关，需要额外理论与实证支持，故评为promising_candidate而非strong_candidate。
- Confidence: 0.6

## promising_candidate: Comprehensive helpfulness of online reviews: A dynamic strategy for ranking reviews by intrinsic and extrinsic helpfulness

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113859
- Source outcome: Evaluation criteria for ranking results (EC1-EC6)
- Coding-agent outcome: 代理生成代码变更的公平及时审查排序
- Decision: 论文属于设计导向的构建与评估（非正式DSR），构建了ICH-ECH模型和DTAHR动态排名模型，并用JD.com真实数据的仿真实验评估。棘轮/马太效应作为理论construct对DTAHR的时间奖励设计有生成性作用，但理论-设计联系为中等而非强；评估指标EC1-EC6高度依赖在线评论领域。向编码代理转移时可形成'代理生成代码变更的公平及时审查排序'这一目标，但该目标的编码代理特异性为中等（代码PR队列也存在于人类开发者），且源文机制未经代码审查场景验证。因此保留为promising_candidate供人工复审，不判定为strong_candidate。
- Confidence: 0.6

## promising_candidate: Mitigating Risk Selection in Healthcare Entitlement Programs: A Beneficiary-Level Competitive Bidding Approach

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1062
- Source outcome: Beneficiary enrollment with MCO / care coordination access
- Coding-agent outcome: 仓库级必要任务的全覆盖度（包括困难/高风险代码修改）
- Decision: 该文是明确的设计导向构建-评估研究：提出了受益人级竞标/混合支付机制，并从拍卖理论与风险选择理论导出设计，用解析证明与20,000次数值模拟评估。风险选择消除与受益人全覆盖是healthcare领域特有且被量化的结果。编码代理迁移中，“困难任务全覆盖/防任务回避”具备强编码代理特异性，但迁移依赖对代理自利目标的人为假设，因此转移强度为中等。综合判断属于promising_candidate，需要人工复核机制可移植性。
- Confidence: 0.6

## promising_candidate: Social influence-based contrast language analysis framework for clinical decision support systems

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113813
- Source outcome: Early depression detection
- Coding-agent outcome: 基于对比行为轨迹的编码智能体早期失败/质量风险检测
- Decision: 该文是设计导向的构建-评估研究：提出了社会影响对比语言分析框架并用真实Facebook数据评估早期抑郁检测性能，社会影响理论直接影响了网络对比特征的设计，理论到设计强度中等。源结果'早期抑郁检测'具有领域构成性，且可类比迁移到编码智能体轨迹失败风险检测，但两个关键环节偏间接：一是社会影响理论从人类心理机制到计算网络权重的操作化较松散；二是从抑郁检测到智能体失败检测属于跨领域机制迁移，缺乏源文献直接支持。因此保留为promising_candidate供人工复核，而非strong_candidate。
- Confidence: 0.6

## promising_candidate: Estimating Life Cycle Sales of Technology Products with Frequent Repeat Purchases: A Fractional Calculus-Based Approach

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1131
- Source outcome: Adoption trend recovery (GDMR-sales procedure)
- Coding-agent outcome: 智能体事件流中的新颖进展-重复返工分解系数
- Decision: 论文构建并评价了GDMR这一预测模型，属于design_oriented_build_evaluate；Bass模型和Tarasov记忆概念确实塑造了模型形式，理论-设计联系为中等。最有迁移价值的评价结果是'仅凭销售数据恢复采纳趋势'，该结果具有扩散理论领域特异性；对编码智能体可类比为'从事件流中分离新颖进展与重复返工'，依赖自主迭代和测试反馈等代理性条件。但该迁移为类比推理，且源文并非正式设计科学研究、不涉及编码智能体，因此作为promising candidate人工复核。
- Confidence: 0.6

## promising_candidate: Discovery of Technological Innovation Systems: Implications for Predicting Future Innovation

- Year/journal: 2024 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2023.2301172
- Source outcome: Future innovation quantity (future patenting volume, FP)
- Coding-agent outcome: 焦点代码模块的未来开发活力/变更需求（focal-module change demand）
- Decision: 该文是明确的设计科学研究（explicit_design_science），构建并评估了TIS发现框架。理论到设计的强度为中等：技术溢出理论被明确称为kernel theory并指导创新指标构造与验证，但核心主题建模/相关度设计更多来自TIS和生态系统概念，理论对构件特征的生成作用不完全。至少一个评估结果（未来创新数量/质量）是领域构成的（domain_constitutive），并可转译为编码智能体的特定目标（如焦点模块未来变更需求）。然而，源文是预测/发现型工件，并未声称设计能改变未来创新；向智能体主动干预机制转译属于较强的分析性外推，因此存在一个重要的中等强度链接，评为promising_candidate而非strong_candidate。
- Confidence: 0.6

## promising_candidate: Customer Engagement Prediction on Social Media: A Graph Neural Network Method

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0281
- Source outcome: targeting cost-effectiveness and reduced customer annoyance from unsuccessful targeting
- Coding-agent outcome: 智能体自主干预的误报最小化与开发者厌烦避免（选择性自主行动）
- Decision: 该文是明确的AI设计研究/设计科学取向：构建并评估了GACE模型，且同质性、品牌忠诚、品牌亲和等理论/构念直接驱动了元路径设计，理论到设计联系强。源结局'顾客参与预测性能'和'减少误触达带来的厌烦成本'在社交媒体营销情境中具有语境化含义。然而，向编码智能体的迁移需要较强分析性类比：将消费者参与/品牌忠诚映射为开发者对智能体变更的接受度，或将精准营销门控映射为智能体自主干预门控。这一链路有防御性但非直接，且源评估指标多为通用预测性能，因此不达strong_candidate，但值得人工全文复核。
- Confidence: 0.6

## promising_candidate: In Search of a “Style:” Capturing the Collective Identity of Social Movements Based on Digital Trace Data

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00951
- Source outcome: Collective identity online (style)
- Coding-agent outcome: 多编码代理系统的集体风格持续性（Collective Style Persistence）
- Decision: 该论文构建并评估了一个理论驱动的测量框架（White风格的二元概念化），属于设计导向的构建-评估研究，理论-设计联系强。被评估的核心结果‘在线集体身份（风格）’具有领域构成性。然而，将这一社会运动理论转移到编码代理需要较大的概念重构（将集体身份转换为多代理系统的集体风格持续性），且源文框架是测量工具而非干预设计，因此转移机制虽可辩护但仍有中等程度的间接性和类比跳跃，值得人工全文审查。
- Confidence: 0.6

## promising_candidate: Learning Personalized Privacy Preference from Public Data

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0318
- Source outcome: Personalized privacy preference (IUIPC score)
- Coding-agent outcome: 自主编码代理的隐私边界遵从度
- Decision: 该文构建了从公开社交媒体数据预测个性化隐私偏好的框架并评估了预测表现；理论（隐私计算、人格、风险偏好等）确实指导了特征设计，属于中等强度的 theory-to-design。隐私偏好本身是情境化结果，并可初步映射到编码代理的隐私边界遵从目标，但映射需要显著概念调整，且源论文未涉及代理设计，因此整体模式尚属合理但关键链接偏弱/间接，保留为 promising 供人工复核。
- Confidence: 0.6

## promising_candidate: Mitigating Bias in Hate Speech Detection With a Small Number of Expert Annotations: A Prompt-Based Learning Approach

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18416
- Source outcome: Statistical parity (Avg SP) / cross-group bias mitigation
- Coding-agent outcome: 跨代码风格群体的公平性 / 错误修改偏差（false-edit bias）
- Decision: 该文是明确的设计科学研究，构建并评估了一个两阶段仇恨言论检测框架，且评价了跨群体公平性（Avg SP/分群体FPR）这一领域构成性结果。但理论到设计的联系为中等：社会认同理论与民族语言认同理论主要为问题框架提供依据，并未直接推导对比学习/prompt的具体机制。向编码代理的迁移（跨代码风格公平性）合理且具代理特异性，但包含类比性推断，需人工复核。
- Confidence: 0.6

## promising_candidate: The Impact of Situational Achievement Goals on Online Learning Behavior: Results from Field Experiments

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0353
- Source outcome: Engagement
- Coding-agent outcome: 编码代理的自主多步目标导向坚持与努力分配
- Decision: 论文以成就目标理论为基础设计并实地评估了三种情境成就目标干预，设计-理论链接强、有因果评估；但被评估的结果（参与度、成绩）在源域中属于通用教育/IS结果，源特殊性不足。向编码代理的转移通过'情境目标框架塑造自主多步代理的努力分配'具有机制可能性，但依赖从人类动机理论到LLM行为的类比，因此整体记为promising_candidate，需人工复核。
- Confidence: 0.6

## promising_candidate: Walrasian Pricing for Combinatorial Markets with Compact-Bidding Languages: An Application to Truckload Transportation

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0676
- Source outcome: Residual envy (ε_c; deviation from Walrasian equilibrium)
- Coding-agent outcome: 编码智能体任务分配中的残余嫉妒/分配后悔（residual envy in multi-agent coding-task allocation）
- Decision: 源论文是明确的设计-构建-评估研究（虽然没有使用 DSR 标签），构建了 IDP 定价机制并通过 630 个实例的模拟评估；理论到设计的关联很强，因为瓦尔拉斯均衡、个体理性、强预算平衡等经济学构念直接决定机制要求和算法设计。三个候结果中，残余嫉妒是最有迁移潜力的领域情境化结果：它在源领域有具体操作化（承运商对车道包的偏好偏离），且源机制（IDP+团割）可以映射到多智能体编码任务分配中的稳定性设计。但是，将编码智能体建模为具有效用函数的经济行动者是需要额外假设的分析推断，源论文没有任何编码代理内容；因此编码智能体特异性为中等，而非强。总节省和货主剩余的迁移较弱或中等。综合判断为 promising_candidate，保留供人工全文审查，不设为 target_match。
- Confidence: 0.6

## promising_candidate: Constructing information technology (IT) portfolios to achieve enterprise strategic goals in multi-business unit firms

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103525
- Source outcome: Weight score / strategic option focus (W^(ITPP))
- Coding-agent outcome: 编码代理任务组合的战略对齐权重
- Decision: 该论文属于design_oriented_build_evaluate：构建并检验了DEA/P ITPM模型和仿真；战略对齐/matching perspective对权重分数设计有明确但部分隐性的影响，theory-to-design为moderate。最可迁移的结果是“权重分数/战略选项焦点”，其来源域含义与多业务单元企业战略对齐相关，属于contextualized。向编码代理迁移时，可将其重新定义为“编码代理任务组合的战略对齐权重”，并使用代理特有的token/工具/迭代/概率错误等投入产出进行DEA/P校准，但该迁移的代理非替代性为moderate而非strong，且源论文并未将权重分数作为独立验证的结果变量。因此完整模式成立但关键环节中等，适合人工全文复核，而非直接判定为strong_candidate。
- Confidence: 0.58

## promising_candidate: Dynamic self-organizing feature map-based models applied to bankruptcy prediction

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113576
- Source outcome: F2-measure (accuracy weighted toward failed firms)
- Coding-agent outcome: 高代价智能体失败轨迹的早期识别与优先召回（high-cost agent failure trajectory detection）
- Decision: 论文确实构建并评估了动态自组织特征映射模型（design_oriented_build_evaluate），并从'破产是持续过程/存在原型失败过程'的理论观点推导出用三年财务轨迹分割样本并估计原型序列的设计机制，理论到设计的强度为中等。其 F2 指标因金融机构不对称错分类成本而有情境化含义，且可以类比迁移为编码智能体对高代价失败轨迹的早期识别。但源文没有显式设计科学框架，评价结果主要还是预测准确性指标；迁移依赖机制类比而非源文直接证据，因此列为 promising_candidate 供人工复核。
- Confidence: 0.58

## promising_candidate: Interventions for Improving Professional Networking for Women: Experimental Evidence from the IT Sector

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15620
- Source outcome: Number of New Contacts Met
- Coding-agent outcome: 非冗余代码上下文整合广度
- Decision: 该文是设计导向的构建-评估研究（现场实验），理论到设计的链条强：搜索/社会壁垒框架和结构洞、社会身份理论直接派生出Search List与Social List两个干预，并量化评估了多个结果。最有希望的迁移是“搜索壁垒→非互惠推荐→代码仓库中非冗余上下文的自主探索→非冗余上下文整合广度”，但这一迁移依赖从人际网络到代码上下文的隐喻重建，且源结果与候选结果不同构。因此不是strong_candidate，但值得人工复评。
- Confidence: 0.58

## promising_candidate: Telecom traffic pumping analytics via explainable data science

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113559
- Source outcome: Legal success of fraud claims (all lawsuits granted / fraud declared in court)
- Coding-agent outcome: 自主代码改动的外部可问责性/可申辩性（contestable accountability of autonomous code modifications）
- Decision: 该文构建并评估了一个可解释的电信流量泵欺诈检测DSS（design_oriented_build_evaluate），并报告了'诉讼全部胜诉'和'约500万美元损失减少'两个有情境特异性的结果。可解释性/XAI作为设计需求对CART规则提取有清晰但非形式化的引导作用，no-free-lunch定理和Laffont-Tirole接入费经济学更多是问题框架而非严格设计理论，因此theory-to-design为中等。法律可问责性向编码代理自主代码修改的可申辩性转移有一定非替代性，但依赖类比；人为活动通胀检测的转移更有编码代理特异性，但源文章未涉及该领域。整体模式合理但关键链接（理论驱动强度、转移机制）中等或间接，故判为promising_candidate而非strong_candidate。
- Confidence: 0.58

## promising_candidate: Warm-Glow Giving, Hedonism, and Their Influence on Muslim User Engagement on Loan-Based Crowdfunding Platforms

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00665
- Source outcome: Amount to lend (ATL)
- Coding-agent outcome: 代理委托范围/授权规模（scope of delegated autonomy）
- Decision: 该文是设计导向的构建-评估研究：基于温暖之光与享乐主义两种利己理论，构建并评估了三种众筹平台设计；理论到设计追踪清晰，且ATL结果具有领域构成性。但向编码代理的迁移属于跨领域类比：将‘借贷金额’映射为‘委托范围/授权规模’需要结合人-代理委托文献，且宗教规范与软件开发专业规范的类比尚需进一步证实。因此列为promising_candidate供人工复核，而非strong_candidate。
- Confidence: 0.58

## promising_candidate: Designing financial education applications for development: applying action design research in Cambodian countryside

- Year/journal: 2022 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2021.1978341
- Source outcome: Learners' positive experience / perceived ease and enjoyment with the tablet application
- Coding-agent outcome: 对编码代理的知情委托与校准性信任（informed delegation and calibrated trust in a coding agent）
- Decision: 该文是明确的 ADR 设计科学研究：构建并评估了 CAFE 平板应用，并提炼了设计原则。理论到设计的联系为中等强度（ADR、Agile、UX 方法显著塑造了设计和迭代过程，但对结果机制的因果解释较隐晦）。被评估成果中，财务能力具有域构成性但与应用归因不明，且无法迁移；学习者积极体验和培训者自信具有情境化含义，可迁移到编码代理的校准性信任和自我效能感/审查责任，但迁移属于分析性推断且需要边界条件界定。整体模式虽完整但迁移连接为中等强度，需要人工全文复核，因此评为 promising_candidate 而非 strong_candidate。
- Confidence: 0.58

## promising_candidate: Adopting and integrating cyber-threat intelligence in a commercial organisation

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2088414
- Source outcome: Directedness of cyber defence behaviour (reactive/undirected -> proactive/directed)
- Coding-agent outcome: 防御型编码代理的行为指向性（directedness of agent defense actions）
- Decision: 该文属设计导向的构建与评估（临床行动研究），构建了CTI-as-a-service并企业级实施；理论到设计联系明确（军事情报质量属性推导设计原则、possibilistic风险框架指导关键性评级重定），评估了网络安全防御姿态、防御行为指向性、漏洞修复优先级等情境化结果。这些结果可向编码代理迁移，尤其是'防御行为指向性'这一结果与代理自主多步动作序列高度相关，但迁移需要将人类组织的'reluctant combatant'、信任与风险接受机制转译为代理的验证/权限/奖励设计，且源文以定性证据为主，因此整体为promising_candidate而非strong_candidate。
- Confidence: 0.58

## promising_candidate: Responding to Online Reviews in Competitive Markets: A Controlled Diffusion Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16163
- Source outcome: Optimal response effort / management response strategy (u_i^*)
- Coding-agent outcome: 校准式自主纠错努力（calibrated autonomous corrective effort）
- Decision: 该文建构并估计了一个受控扩散/随机最优控制模型（design_oriented_build_evaluate），oblivious equilibrium、beg to differ effect 和平方根努力模型确实影响了模型设计，理论到设计的映射为中等强度。最优回应努力和在线评分在旅游平台在线评论竞争情境中有情境化意义。向编码智能体的迁移（校准式自主纠错努力、声誉轨迹）具有机制基础，但源文并非正式DSR、理论到设计部分依赖行为机制类比、编码智能体非替代性仍属中等，因此评为 promising_candidate 而非 strong_candidate，值得人工全文复核。
- Confidence: 0.58

## promising_candidate: Development Trajectory of Blockchain Platforms: The Role of Multirole

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0243
- Source outcome: Blockchain platform development trajectory (adoption/abandonment population dynamics measured via token price)
- Coding-agent outcome: 开发者对编码代理的校准化委托轨迹（calibrated delegation trajectory）
- Decision: 论文确实构建并评估了一个理论驱动的参数化人工物（模型），Metcalfe定律、SIS和TAM对模型设计有明确作用；但被评价的核心结果是模型拟合精度（通用性能），而更有领域特异性的“发展轨迹”是模型匹配/预测的对象而非设计干预所产生的结局变量。向编码代理迁移“校准化委托轨迹”有较强机制合理性，但源侧结局与干预的关系仍不完整，因此保留为promising而非strong。
- Confidence: 0.58

## promising_candidate: BRM: A methodology for improving the practical relevance of belief-based information technology usage theories

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103488
- Source outcome: Supporting-service functionality (SSF)
- Coding-agent outcome: 编码代理“全流程支持功能”的可分解感知（decomposed support-functionality beliefs for coding agents）
- Decision: 本文是一个构建并验证方法（BRM）的设计导向研究，理论（Fishbein和Ajzen的信念形成理论）对方法设计有强驱动作用；其评价结果SSF是一个情境化的用户信念构念。向编码代理的转移机制（把宽泛能力/可信信念分解为关于代理可观察行为的描述性信念）有防御性和非替代性，但源论文是方法论示范而非IT人工物设计，且SSF的电商操作化需要实质重构，因此整体为promising candidate而非strong candidate。
- Confidence: 0.57

## promising_candidate: Can financial incentives help with the struggle for security policy compliance?

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103447
- Source outcome: Clicking on phishing links
- Coding-agent outcome: 编码智能体对嵌入恶意指令/提示注入的安全遵从性（抵抗不安全的自动执行）
- Decision: 来源论文不是正式设计科学研究，但设计并评估了财务激励干预，且Prospect theory强驱动了损失/收益框架设计，理论-设计联系强；被评估的结果（点击钓鱼链接、怀疑后不点击）具有领域情境化意义。然而，将基于人类损失厌恶的财务激励迁移到编码智能体需要类比式再概念化（如奖励塑形、非对称惩罚），转移机制和非可替代性为中等强度，因此不构成strong_candidate，但值得人工全文审阅。
- Confidence: 0.55

## promising_candidate: Classifying the ideational impact of Information Systems review articles: A content-enriched deep learning approach

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113432
- Source outcome: Ideational impact of IT business value (ITBV) review articles
- Coding-agent outcome: 代理代码变更中的'观念性采纳与延伸'（ideational uptake of design concepts in agent-generated code changes）
- Decision: 该论文属于设计导向的构建-评估研究（构建Deep-CENIC并评估），非正式设计科学。理论到设计的链接为中等：观念性影响理论定义了分类目标和编码方案，但特征工程与深度学习架构主要借鉴既有引文分类文献。存在领域构成性的结果（ITBV领域的观念性影响），并给出了量化与定性评估。映射到编码代理时，'观念性采纳与延伸'作为候选目标具有较强代理特异性（自主迭代、自修正、仓库级依赖），但该映射属于类比的边界扩展，且源论文未涉及软件工程。因此不是强候选，但值得人工复核，判定为promising_candidate。
- Confidence: 0.55

## promising_candidate: The research-practice gap as a pragmatic knowledge boundary

- Year/journal: 2021 / Information and Organization
- DOI: 10.1016/j.infoandorg.2020.100334
- Source outcome: practitioner assessments of OT/IS research (non-contradictory/constructive)
- Coding-agent outcome: 编码代理产出的可构造评估性（constructive assessability of agent-generated changes）
- Decision: 文章以 Carlile 知识边界和 boundary object 理论指导设计了一个两页理论摘要作为干预，并通过定性 vignettes 评估了实践者对理论的评估、研究利用和交互专长，满足 design_oriented_build_evaluate 的基本模式。其理论到设计的路径清晰但偏中等强度：边界对象设计主要服务于研究目的，而非正式设计科学原则；结果均为定性评估且具备 source-domain 特异性。向编码代理迁移时，'可构造评估性'和'交互专长'能借助概率生成、多步自主规划、仓库级副作用等代理特有条件形成强非替代性设计目标。但鉴于该文自称为概念性论文、干预作为研究工具、且理论到设计的推导部分隐含，保留为 promising_candidate 供人工全文复核，不设为 strong_candidate。
- Confidence: 0.55

## promising_candidate: A decision analytic approach for social distancing policies during early stages of COVID-19 pandemic

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113630
- Source outcome: Peak hospitalization volume and peak timing (time bought)
- Coding-agent outcome: 自主编码代理干预放松后的缺陷反弹峰值负荷与到达时间（Rebound failure-wave peak load and time-to-peak）
- Decision: 该文属于设计导向的构建与评估：作者构建了年龄结构分室仿真模型和决策分析框架，并通过大量计算实验评估社交隔离触发阈值、封闭时长和分阶段重开策略。理论（分室流行病模型、R(t)与Proposition 1）对政策设计有中等但清晰的塑造作用。评估结果（住院高峰/时机、死亡率、累计发病率）高度领域具体。最强的编码代理迁移是把“干预时机与分阶段放宽”机制映射到自主编码代理的监督/审查策略与“解除限制后的缺陷反弹峰”这一新结果；但该映射主要是类比，源文没有软件证据，因此整体为需人工复审的候选而非强匹配。
- Confidence: 0.55

## promising_candidate: Evaluating the Effectiveness of Marketing Campaigns for Malls Using a Novel Interpretable Machine Learning Model

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1078
- Source outcome: increase in customer traffic / customer traffic lift
- Coding-agent outcome: 编码代理干预资源-成功率响应曲线与资源分配有效性
- Decision: 该文构建并评估了 GANNM，符合设计导向的构建-评估模式；营销活动分类理论（体验/销售激励、时机）以中等强度影响响应曲线特征设计，商场客流提升是领域构成性结果。但对编码代理的最有希望迁移（干预资源-成功率响应曲线）仍需将营销活动类别映射为代理干预类别，并验证 GANNM 机制在代理运行数据上的适用性，因此属于 promising 而非 strong。
- Confidence: 0.55

## promising_candidate: How to elicit and cease herding behaviour? On the effectiveness of a warning message as a debiasing decision support system

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113652
- Source outcome: Herding behaviour (choice of the herded option)
- Coding-agent outcome: 编码智能体对流行度/同伴信号的选择性遵从（popularity-conformity bias in code generation）
- Decision: 论文属于设计导向的构建-评估研究：作者开发并实际运行了两个 DSS（同伴信息模拟工具和警告信息去偏 DSS），并用随机对照试验评估了羊群行为和被警告后的去偏效果。理论（羊群偏差、去偏技术分类）对设计特征有清晰但不完全形式化的引导作用，可评为 moderate。源结果'羊群行为'在金融决策语境下具有领域特定含义（消费者福利、商业操纵、金融风险），属于 contextualized。向编码智能体迁移时，羊群偏差可类比扩展为'流行度/同伴信号遵从偏差'，并可在智能体规划/代码审查中设计去偏警告机制；但源理论针对人类决策者，LLM 的流行度遵从只是类比性扩展，因此编码智能体特异性与源-迁移机制均存在中等程度的间接性。综上，完整模式基本成立但有一个重要环节（编码智能体迁移机制）为中等强度，适合人工复核，故判为 promising_candidate 而非 strong_candidate。
- Confidence: 0.55

## promising_candidate: Co-evolution of neural architectures and features for stock market forecasting: A multi-objective decision perspective

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114015
- Source outcome: Balanced error across pre-COVID and within-COVID market regimes (E_pr, E_cv)
- Coding-agent outcome: 跨代码任务/代码库体制的均衡成功率（regime-balanced task success）
- Decision: 该文属于design-oriented build-and-evaluate：构建了多目标协同进化神经架构搜索框架并进行了系统评估。理论到设计链路由bias-variance权衡、Pareto多目标优化和MCDM偏好理论支撑，但属于算法/统计学习理论，而非IS核心理论，且部分设计选择（如浅层限制）是经验性的，链条为中等强度。最具迁移潜力的结果是跨市场体制的均衡预测误差，它是情境化的（COVID市场断点和防数据窥探），并且映射到编码代理的“跨代码任务体制均衡成功率”有合理机制，但源论文未涉及代码任务，体制定义和测量需大幅重新设计，非替代性中等。因此构成promising candidate而非strong candidate。
- Confidence: 0.55

## promising_candidate: Could Gamification Designs Enhance Online Learning Through Personalization? Lessons from a Field Experiment

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1123
- Source outcome: SRL engagement
- Coding-agent outcome: 编码智能体的自我调节工作流参与度（planning-monitoring-reflection engagement）
- Decision: 来源论文是设计导向的现场实验：SRL 理论、目标定向理论和游戏化个性化原则强驱动了游戏化反馈设计，并定量评估了 SRL 参与度、学习效率和测试成绩。SRL 参与度可被重新定义为编码智能体的规划-监控-反思工作流参与度，操作化依赖智能体的多步自主执行与反馈迭代，编码侧非替代性较强；但源理论基于人类动机与目标定向，向无内在动机的智能体迁移需要重要的边界条件重构，因此不是强候选，保留人工复核。
- Confidence: 0.55

## promising_candidate: Depicting Risk Profile over Time: A Novel Multiperiod Loan Default Prediction Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17491
- Source outcome: Identifiability and discriminability (case analysis)
- Coding-agent outcome: 失败步骤可识别性（Failure-Step Identifiability）与轨迹风险判别力（Trajectory Risk Discriminability）
- Decision: 源论文是显式设计科学研究，构建并多层面评估了HACS；mixture cure/split hazard模型与概率单调性显著塑造了“if-and-when”混合建模和单调概率框架，但若干设计选择属于方法性/算法性而非强理论生成，故 theory-to-design 强度评为 moderate；最可迁移的结果是 case analysis 中的可识别性/可判别性，在编码智能体场景可重新实例化为“失败步骤可识别性”，依赖自主多步迭代、可执行制品、测试反馈和人机委托等条件，具有较强非替代性。但由于源论文是预测模型而非智能体控制/人机交互设计，且编码智能体映射需要额外的失败状态界定，整体证据链仍有一个重要环节偏间接，因此评为 promising_candidate 供人工复核，不设 target_match。
- Confidence: 0.55

## promising_candidate: Interpretable cost-sensitive regression through one-step boosting

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114024
- Source outcome: Interpretability of cost-sensitivity via bootstrapping
- Coding-agent outcome: 代码智能体成本敏感行为的可解释属性归因
- Decision: 该文构建并评估了OSB算法（设计导向的构建-评估），使用了boosting、M-estimation、非对称成本函数等明确理论构造，理论-设计关联中等。评价的核心指标AMC是通用成本加权误差，编码智能体迁移较弱；而bootstrap可解释性具有较具体的编码智能体含义（将仓库特征与智能体过度/不足修改行为相关联），但该迁移属于构造扩展而非直接机制迁移，且源文并非DSR。总体可作为promising candidate供人工复核。
- Confidence: 0.55

## promising_candidate: Positively Fearful: Activating the Individual’s HERO Within to Explain Volitional Security Technology Adoption

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00793
- Source outcome: actual volitional adoption of security technologies
- Coding-agent outcome: 开发者对编码代理安全防护机制的自愿采纳
- Decision: 该论文属于设计导向的构建与评估研究（设计了基于PsyCap的大恐惧诉求视频并评估），理论到设计的联系较强（PsyCap和FAM明确驱动信息设计）。主要结果（安全技术自愿采纳及其意图）是具体情境化的但不是领域构成性的；向编码代理的转移需将“威胁”重新定义为代理自主风险，并转化为对代理安全护栏的自愿采纳。这种转移机制有一定合理性，但安全采纳的通用性使得编码代理特异性为中等，且源论文未探讨AI代理。因此判定为 promising_candidate 而非 strong_candidate。
- Confidence: 0.55

## promising_candidate: Real-Effort Incentives in Online Labor Markets: Punishments and Rewards for Individuals and Groups

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/15166
- Source outcome: effort (tag count)
- Coding-agent outcome: 多智能体协作编码中的实质贡献完整性（free-riding-resistant substantive contribution）
- Decision: 该文属于设计导向的实验干预研究：使用公共物品博弈/搭便车理论设计了外生的个体/群体奖惩干预，并以协作图像标注实验评估了真实努力（tag count）等结果。源结果具有领域情境性，且可映射到多代理编码协作中的'实质贡献完整性'这一设计目标。但论文未使用DSR方法论，理论主要驱动实验假设而非可复用设计原则，且从人类经济激励到无内在效用的编码代理的系统映射存在明显的边界条件差异，因此保留为 promising_candidate 供人工复审，而非 strong_candidate。
- Confidence: 0.55

## promising_candidate: Beyond Risk: A Measure of Distribution Uncertainty

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0089
- Source outcome: firm-level crash risk (NCSKEW/DUVOL)
- Coding-agent outcome: 代码智能体的灾难性变更风险（repository-breaking change risk）
- Decision: 该文属于设计取向的构建-评估研究（构建HD度量并在模拟和金融数据中评估），理论到设计链接为中等强度；崩盘风险是领域构成性结果，且向编码智能体灾难性变更风险的转移具有可辩护机制和强编码特异性。但该文不是正式的DSR论文，且HD对崩盘风险的系数方向需要重新解释才能用于编码智能体，因此整体为promising而非strong。
- Confidence: 0.55

## promising_candidate: Mobile Advertising in Distracted Environments: Exploring the Impact of Distractions on Dual-Task Interference

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17758
- Source outcome: Ad engagement / interrupt effectiveness
- Coding-agent outcome: 自主编码代理对关键中断的加工与响应有效性
- Decision: 论文以定制App构造动态任务-中断-环境实验，属于设计化实证研究；DTI、有限注意、分割注意、相关性-可及性理论直接推导了广告时机、一致性和距离三种设计操作，理论到设计链路中等；评估的ad engagement具有源域特定含义；向编码代理的迁移有可辩护机制但属于类比迁移，代理端操作化和测量需重构，故列为promising。
- Confidence: 0.55

## promising_candidate: Review credibility as a safeguard against fakery: the case of Amazon

- Year/journal: 2022 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2021.1886613
- Source outcome: Credibility of product reviews (product information credibility)
- Coding-agent outcome: 可验证信号锚定的编程智能体输出可信度
- Decision: 文章构建并验证了一种基于平台验证信号量化评论可信度的方法，属于设计导向的构建-评估；Yale态度改变模型和来源可信度理论为可信度构念和信号选择提供了中等强度的理论支撑。源文的核心结果“用累积的可信度信号对抗虚假内容”可迁移到编程智能体：用测试、构建、执行和人工确认等验证信号累积生成结果的可信度，以防范看似合理但错误的代码产物。由于源文并非正式DSR，理论到设计的推导为中等偏弱，且“可信度”首先是所提方法的输出指标而非典型结果变量，因此保留为promising candidate供人工复核，而非strong candidate。
- Confidence: 0.48

## promising_candidate: Trust calibration of automated security IT artifacts: A multi-domain study of phishing-website detection tools

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2020.103394
- Source outcome: Calibrated trust in the detector
- Coding-agent outcome: 对编码代理的校准信任（calibrated trust in coding agents）
- Decision: 源文具备设计导向的构建与评估特征：自建检测工具并操作化信任校准器显示；ATR理论到设计特征的映射强；最佳结果“校准信任”具有领域情境化含义，且到编码代理的迁移机制可辩护。但由于源文中的检测工具主要是实验载体而非独立的设计科学贡献，设计属性存在一定主观性，因此定为 promising_candidate 供人工全文复核。
- Confidence: 0.45

## promising_candidate: Optimal Joint Assortment for an Omni-Channel Retailer

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0596
- Source outcome: Customer coverage continuity (patchy coverage)
- Coding-agent outcome: 代码库修改覆盖连续性（避免补丁空洞）
- Decision: 本文是面向全渠道零售商的优化建模研究，属于design_oriented_build_evaluate；定位选择模型对选品/定价设计有清晰但非DSR标签的设计作用；最有希望的已评估结果是'顾客覆盖连续性/补丁空洞'，该结果在编码代理场景中可类比为'代码库修改覆盖连续性'，但因来源领域与代码依赖空间差异大，非替代性仅为中等。整体为promising_candidate，需要人工全文复核。
- Confidence: 0.45

## promising_candidate: “My Name is Alexa. What’s Your Name?” The Impact of Reciprocal Self-Disclosure on Post-Interaction Trust in Conversational Agents

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00839
- Source outcome: Post-interaction trust in CA
- Coding-agent outcome: 对编码智能体的事后委托信任（post-delegation trust）
- Decision: 本文属于设计导向的构建-评估研究（定制开发了文本和语音CA并进行了两个随机实验），理论（三因子拟人化理论、认知/情感信任基础）对CA的互惠自我披露操纵和结果测量有清晰但不完全显式的设计作用；核心结果“事后信任”是具有情境特异性的评估结果，且可迁移为编码智能体的委托信任。然而，来源理论到设计原则的链接并非正式设计科学中的需求到原理映射，且编码智能体迁移中自披露机制对专业编码场景的适用性仍存在不确定性，因此判定为 promising_candidate 而非 strong_candidate。
- Confidence: 0.45
