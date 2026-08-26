# 从 AIS 机制反向搜索 coding-agent 广义安全新题

## 0. 审查任务、截止日与证据边界

本文件执行一次由 AIS Senior Scholars' Basket 全文出发的理论机制反向搜索。检索不是先选一个 coding-agent 题目，再为它寻找相似术语，而是先在原文中核定构念的分析单位、前因、关系方向、结果与适用边界，再检查该机制能否在 coding-agent 广义安全情境中形成不可替代的内部状态、非交换运算、学习目标或行动约束。检索截止日为 2026 年 8 月 16 日。

本次使用 `otero-open-api` 的只读接口。按技能协议先调用 `/journals`，确认当前开放库包含 11 种 Basket 期刊；随后只用 `/articles` 检索，并回到本地 MinerU 全文逐节阅读。API 结果字段按 `fields` 层解析。没有调用写接口，也没有把搜索摘要当成理论证据。Basket 论文的参考文献链继续用于定位原理论与后续机制论文；coding-agent 技术近邻则回读论文 HTML、正式项目页或公开仓库所披露的方法、数据与评价部分。

本文件是内部选题审计，不是正式论文正文。文中对两个最强机制所作的模型化尝试属于钢人化反证，不代表已经训练模型或运行实验。所有候选性能、效应量与显著性均为空；不存在可以写成“结果表明”的候选实验结果。

### 0.1 必须先承认的先验状态

`00A`、`00B` 与 `00E` 已经把 C1–C27 的直接覆盖、理论错置、数据不可识别和通用替代反证逐项冻结。当前只有 C3 达到 **DESIGN-FROZEN / RESULTS PENDING**；固定 pre-cutover PostgreSQL 迁移中的主动缓解期权格仍处在其锁定版独立审计轨道。反向搜索不能通过改名重新引入 mindfulness/HRO、TMS、real options、control、agency、accountability、resilience、task–technology fit 或这些理论已经否决的动作结构。

### 0.2 终局答案

**保留的新机制候选数为 0。**

反向搜索得到两个值得进入最强红队的机制簇：情境完整性，以及数字化过程漂移。二者都具有比一般“风险感知”更清楚的结构。情境完整性把信息流写成角色、信息类型与传输原则的关系元组；过程漂移把反复行动写成有向图，并以保留窗口中的边形成、强化和消解产生非线性结构变化。然而，阅读全文和最新直接工作后，两者都触发终止条件。

情境完整性已经被 AgentSCOPE 的 Privacy Flow Graph、CI-Work、PiSAs、PrivacyLens 系列与其他 agent 隐私 benchmark 直接操作化。把仓库、issue、日志与工具调用换成这些基准中的企业资料或个人资料后，输入、输出、信息流图、visibility matrix、appropriateness label、utility–privacy 结果和控制动作均保持不变。coding agent 可以被删除。若进一步输出授权投影、provenance filter、能力 restriction 或 redaction，又回到 C6、C7 与 C13 已覆盖的 provenance、权限和作用域执行。

数字化过程漂移拥有明确的有向边与历史窗口更新，但原理论故意研究没有外部干预和绩效反馈的内生变化。漂移可能有益也可能有害，复杂性 burst 不是安全损害标签，理论不能告诉控制器该保留哪一条边、删除哪一条边或选择哪一个 coding action。其 2021 年方法论文还把有向图明确定位为 Gregor Level 1 的分析基础，而非 design-and-action theory。同信息的 temporal graph、process-mining detector、world model 或 POMDP 可以精确复现其状态更新；TACT 又已经在 coding-agent 轨迹上直接学习 overthinking/overacting drift axes 并进行 forward-hook 干预。

因此，本轮没有形成 CONDITIONAL 题目，也没有向三篇系列加入新题位。这个结论不是“没有找到好名字”，而是理论层级、直接覆盖、coding-agent 删除和等参数通用反证同时没有通过。

## 1. 实际阅读范围与检索可追溯性

### 1.1 本轮完整回读的项目材料

下列项目材料已从头到尾回读，并作为本文件的先验约束。

| 材料 | 本次使用方式 |
|---|---|
| `00A_广义安全概念边界与系列选题论证.md` | 固定广义安全边界、现行系列状态、C1–C27 的题位历史和 coding-agent 删除门 |
| `00B_内部选题与可行性审计.md` | 逐项冻结已否决理论、直接近邻、数据条件、通用替代与撤题条件 |
| `00E_直接近邻与数据资源核验台账.md` | 核对 benchmark、公开资产、直接工件与截至 2026 年 8 月的更新 |
| `00F_逐段双ISR写作与引用审计协议.md` | 使用 `source_function_code`、`candidate_function_code`、完整功能链与五类编辑动作 |
| `00W_肖帅勇两篇ISR源行句段主键Manifest.md` | 只使用可解析的真实段落键与句键；不把解析成功当成功能同位 |
| `00D_目标博士论文系列组织逻辑借鉴.md` | 检查总体张力、三个独立决策对象与系列共同结果的组织逻辑 |
| 目标浙江大学博士论文相关主文 | 回读摘要、目录、总体研究问题、三个子研究关系、方法框架、创新与结论；只借鉴系列组织，不迁移其内容 |
| 肖帅勇老师 ACAA 与 DSDL 两篇 ISR 全文 | 回读引言、理论—算法映射、训练与评价段落；本文件末尾按精确主键登记功能对照 |

目标博士论文给出的可复用组织原则是：三个研究可共享一个长期组织张力和结果对象，但情境变化必须改变决策对象、可见状态、作用时点与算法行动；前一研究可以提供知识，不能成为后一研究成立的前置模块。本次 0 候选意味着不能为了补齐三篇而把一个已覆盖的 privacy controller 或 trajectory detector硬塞入系列。

### 1.2 Basket 全文阅读账

下表区分完整主文回读与定向机制核验，避免把搜索命中或局部定位夸大为“阅读全文”。

| 论文 | DOI | 阅读范围 | 本次承担的责任 |
|---|---|---|---|
| Li, Luo, Sarathy, & Xu, *Contextual Integrity and Personal Health Information Sharing in Online Social Networks*, JAIS 2024 | `10.17705/1jais.00892` | 主文从摘要至结论完整回读 | 核定 CI 的原分析单位、情境元组、norm/value 路径、披露意向结果和因果边界 |
| Pentland, Liu, Kremser, & Hærem, *The Dynamics of Drift in Digitized Processes*, MISQ 2020 | `10.25300/misq/2020/14458` | 主文与 Appendix A simulation 完整回读 | 核定 `L/M/V/R`、历史矩阵、边更新、复杂性与 phase change，确认无外部绩效反馈 |
| Pentland, Vaast, & Ryan Wolf, *Theorizing Process Dynamics with Directed Graphs*, MISQ 2021 | `10.25300/misq/2021/15360` | 主文完整回读 | 沿参考链核定有向图是 Level 1 分析基础、不是安全行动算子 |
| Burton-Jones & Grange, *From Use to Effective Use*, ISR 2013 | `10.1287/isre.1120.0444` | 主文完整回读 | 核定 transparent interaction、representational fidelity、informed action 是 user–system–task 的有效使用构念 |
| Strong et al., *A Theory of Organization-EHR Affordance Actualization*, JAIS 2014 | `10.17705/1jais.00353` | 主文完整回读 | 核定 affordance 是具体技术与目标行动者的关系，actualization 是个体/组织行动旅程 |
| Rosenkranz, Vranešić, & Holten, *Boundary Interactions and Motors of Change in Requirements Elicitation*, JAIS 2014 | `10.17705/1jais.00364` | 主文完整回读 | 核定 boundary complexity、object capacity、broker ability、teleological/dialectical motors 与 shared understanding |
| Salovaara, Lyytinen, & Penttinen, Digital HRO, MISQ 2019 | `10.25300/MISQ/2019/14577` | 主文完整回读 | 复核 digital core、improvement/anticipation layer 与人类 pragmatic control 的层级 |
| Butler & Gray, Reliability–Mindfulness, MISQ 2006 | `10.2307/25148728` | 主文完整回读 | 复核个体 mindfulness 与组织 mindfulness 不可互换 |
| Tim, Pan, Bahri, & Fauzi, digital resilience, JAIS 2023 | `10.17705/1jais.00842` | 主文完整回读 | 复核组织层抗冲击、恢复与重组能力，未给低层行动语法 |
| Sein & Santhanam, Goal-Directed Error Recovery, ISR 1999 | `10.1287/isre.10.3.276` | 主文完整回读 | 复核人类 novice/expert 的目标层错误恢复与学习结果 |
| Najjar et al., IS incident recovery, EJIS 2022 | `10.1080/0960085X.2020.1869915` | 主文完整回读 | 复核组织 incident recovery 活动、角色与服务结果 |
| Benaroch, proactive risk mitigation with real options, ISR 2018 | `10.1287/isre.2017.0714` | 主文完整回读 | 复核 mitigation、wait、exercise/non-exercise 的投资单位，防止再次泛化 |

另外，TMS、control alignment、delegation/agency、TTF、accountability、media synchronicity、information-processing fit、workaround 与 escalation 的原论文模型、构念定义、假设方向和 limitations 段已逐项核对；其在本项目中的全部否决责任则通过 `00A/00B/00E` 完整回读。它们没有被当作未搜索到的新机制重新进入漏斗。

### 1.3 Otero 反向检索词与引用链

Otero 检索词按机制而非应用名组织。检索实际覆盖下列组别。

| 机制组 | Otero 查询词 |
|---|---|
| 理论进入计算 | `theory-driven deep learning`；`theory-guided machine learning` |
| 信息表示与行动 | `representational fidelity informed action`；`effective use representation theory` |
| 知识边界 | `knowledge boundaries transfer translate transform`；`boundary objects syntactic semantic pragmatic`；`boundary interactions requirements elicitation` |
| 沟通顺序 | `media synchronicity conveyance convergence`；`temporal rhythms entrainment coordination` |
| 需求—能力 | `information processing requirements capacity fit`；`task technology fit performance` |
| 组织变化 | `organizational routines generative system safety`；`affordance actualization process sequence`；`routine drift digitized processes` |
| 风险反应 | `workaround consequences intentions`；`escalation of commitment negative information` |
| 责任与隐私 | `responsibility accountability algorithmic action`；`contextual integrity privacy transmission principle`；`communication privacy management boundary turbulence` |
| 学习与耦合 | `organizational learning exploration exploitation safety`；`loose coupling tight coupling interactive complexity` |

引用链回读形成两条关键路径。

1. `Contextual Integrity and Personal Health Information Sharing` 把 Nissenbaum 的 CI 引入 OSN 健康信息披露，进一步指向规范识别与技术 enforcement 文献；2024–2026 的 agent privacy work 已把相同五元参数直接变为 benchmark schema、flow graph 和 visibility label。
2. `The Dynamics of Drift in Digitized Processes` 的边形成/消解机制进一步指向 `Theorizing Process Dynamics with Directed Graphs`。后者明确区分测量 change 的有向图与解释 why 的 grand theory/mechanism/motor，说明图本身不能替代安全规范或行动方向。

### 1.4 最新技术全文与公开资产核验

| 工作 | 已核对内容 | 对反向候选的约束 |
|---|---|---|
| CI-Work, arXiv:2604.21308 | risk model、five flow directions、essential/sensitive set、trajectory simulator、leakage/violation/conveyance、125 seeds/1,000 entries 与数据链接 | 企业 agent 已直接使用 CI 组织 dense retrieval 和 privacy–utility 评价 |
| AgentSCOPE, arXiv:2603.04902 | Privacy Flow Graph、五个 CI 参数、user/agent/tool/recipient 边、62 个 live multi-tool 场景、八个监管领域、每阶段 ground truth | “把 agent 中间工具流写成 CI 图”已被逐字占据 |
| PiSAs, arXiv:2607.05318 | appropriate/inappropriate attribute、user visibility matrix、output/inter-agent/memory spillage、共享 agent topology | 角色可见性与跨用户泄漏已有双标签和系统级评价 |
| AgentSecBench, arXiv:2605.26269 | trusted/untrusted channel、policy projection、instruction/retrieval/capability games、paired benign controls、Qwen3 开源模型 | enforceable privacy/authority 已有 observation/action projection 与 noninterference 基线 |
| TACT, arXiv:2605.05980 | step labels、OT/OA/CAL hidden states、mean-difference axes、orthogonalization、forward hook、SWE-bench/Terminal-Bench/CLAW-Eval splits | coding-agent drift detection 和 forward intervention 已有直接、可复现的表示路线 |
| SABER, arXiv:2606.01317 | Docker stateful workspace、shell/event/delta evidence、final-state harm、公开仓库 | 可提供 operational harm 结果，但不赋予过程漂移理论安全方向 |
| HINTBench, arXiv:2604.13954 | 629 条长轨迹、risk detection/localization/type labels | 可训练 generic trajectory risk model，不能把 drift complexity 变成理论专属监督 |
| Tang et al., arXiv:2605.29442 | 20,574 个真实 coding-agent sessions、七类 misalignment、developer correction、damage locus | 证明真实失败与项目/外部状态后果；观察性 pushback 不是 edge-level 安全反事实 |
| Wink, arXiv:2602.17037；AgentRx, arXiv:2602.02475 | production misbehavior intervention；115 条失败轨迹 critical-step 诊断 | drift/trajectory diagnosis 已有强近邻，新增题不能只是 detector 或自然语言纠偏 |

技术预印本承担直接覆盖与 benchmark 事实，不替代 Basket 理论来源。凡未取得可核细节的搜索命中没有进入撤题理由。

## 2. 资格门：什么才算一个可保留的反向候选

一个机制只有同时满足以下七项，才可从“理论有趣”升级为题目。

1. **MEC。** 原理论在正确分析单位上给出有方向关系、非交换更新或结构约束，而不只是变量清单、结果解释或管理建议。
2. **MAP。** coding-agent 情境必须保留原构念的行动者、对象、时间与结果责任；不能把人类认知或组织容量静默改成模型 hidden state。
3. **ALG。** 理论状态必须进入 forward、loss 或 action，并在冲突情境下规定与通用方法不同的选择。
4. **监督可识别。** 训练样本和标签不能由研究者先写理论规则再让模型复述；需要真实执行、可信标注或可隔离的反事实结果。
5. **coding-agent 不可删除。** 删除 repository read/write、代码修改、shell/tool execution 和软件验证后，任务应失去其核心输入、动作或损害。
6. **外部安全结果。** 改善必须表现为真实泄漏、破坏、不可逆行动、错误批准或任务可靠性结果，而不是仅改善构念分类准确率。
7. **generic 反证。** 在同数据、同参数、同动作、同预算下，匿名 Transformer、temporal graph、POMDP/world model 或通用约束策略不得在预注册等效界内复制关键能力。

“理论使研究者想到一种 feature”不等于 MEC→MAP→ALG。一个理论元组适合作为 dataset schema，也不等于它产生独立算法。

## 3. C1–C27 的禁止返回边界

本节不是重复全部旧审计，而是把反向检索最容易误入的门压缩为不可移动的约束。

| 禁止返回的结构 | 已冻结原因 | 本轮相关机制不得如何改名 |
|---|---|---|
| C1/C1′/C1″ 状态义务、未来选项、故障后授权 | LoopsBench/政策近邻、paired world 缺口、matched-state POMDP、授权理论层级 | 不得用“过程惯例”“漂移边”“适应性 option”恢复 |
| C2 TMS 协调 | expertise/credibility/coordination 归因与标签不可识别；generic graph/POMDP | 不得用 boundary broker、knowledge fit 或 multi-agent memory 改名 |
| C3 固定批准点序贯取证 | 唯一冻结题；固定 escalation/action，可信绑定、grounding repair、真人 unsafe approval | 任何 human shared understanding、evidence sequence、second reviewer 都必须证明不共享中心动作 |
| C4 post-harm compensation | RAC、Mnemosyne、DART、NOMS、PASE 与旧案终局覆盖 | 不得用 resilience、routine repair、recovery affordance 重开 |
| C5–C9 verifier/provenance/permission/rollback/escalation | 直接 benchmark 与系统工件密集 | CI policy、flow filter 或 ask/deny 不得重新命名为新理论算法 |
| C10–C18 structural erosion、test control、audit capture、scope、monitor、ownership、skill、verification debt、release | 直接理论/技术所有者、反事实缺口、coding-agent 删除或无界行动 | 不得用 effective use、accountability、affordance、process conformance 恢复 |
| C19 reviewer allocation | reviewer expertise/load/fatigue/deferral 已覆盖，且与 C3 第二审核者冲突 | 不得用 TMS 或 boundary matching 改名 |
| C21 concurrent repo drift | state control、premise invalidation、semantic merge、generic temporal graph 已覆盖 | “process drift”必须证明不同对象与不同动作，否则直接落入 C21 |
| C22–C27 scaffold fit、common cause、data applicability、license、disclosure、strategic contracts | 单位错置、直接组件、joint truth 缺失、coding-agent 删除、generic SMDP/博弈 | 不得把 fit、agency、accountability、real options 或 control 当作新名字 |

## 4. 理论机制全漏斗

### 4.1 既有否决理论的原构念复核

| 理论 | 原分析单位与关系方向 | 原结果 | 为何不能进入新题 |
|---|---|---|---|
| reliability–mindfulness / Digital HRO | 人或组织对异常、运行与专长的注意；Digital HRO 的 pragmatic control 位于人类高层 | 稳定情境下控制结果变异、异常时保持可靠运行 | 不给 action grammar、edge order 或 loss；把五面向做成 tensor 是层级迁移；HRO human control 还会与 C3 重叠 |
| digital resilience | 组织或生态在中断中的吸收、恢复、适应与重组 | 业务连续性与转型能力 | 是组织能力和结果路径，不规定 coding-agent 每步安全动作；已在 C4 终审失败 |
| TMS | 团队成员形成 who-knows-what、cognition-based trust 与 task–knowledge coordination；绩效反馈影响后期调整 | 虚拟团队绩效 | 团队行为构念不能直接成为 subagent hidden tensor；其输入可由 generic allocation/graph 模型复制；属于 C2/C19 |
| real options | 投资者为未来权利支付 premium，在 uncertainty 展开后 wait、mitigate、exercise 或 abandon | 项目投资风险与价值 | 只在主动缓解期权格的严格迁移单位中仍受审；不能泛化到所有安全 defer/stop；C1′ 已被 two-stage POMDP 反证 |
| IS control alignment | 系统开发项目中的 formal/informal、behavior/outcome/clan/self control 组合及其 alignment | 项目绩效、控制有效性 | 组织控制 portfolio 不是模型动作语法；变成 constraint weights 即 generic control policy |
| delegation/agency | 人、代理人与患者之间的授权、目标、信息不对称与责任关系 | 委托结果、使用与责任分配 | 缺少真实 principal utility 与反事实 agent response；进入 contract/action 时落入 C27 或权限 C7 |
| accountability | 可追责关系、记录、解释、answerability 与 sanction 条件 | 责任认定、合法性与治理结果 | audit log/attribution 是 substrate；理论没有推出哪条代码、命令或证据应先执行 |
| TTF / information-processing fit | 个体任务需求与技术能力的 fit 影响利用和感知绩效；组织 processing requirement–capacity fit 类似 | 使用、个人绩效或组织协调 | fit 是诊断关系，不是有方向更新；同输入的匹配网络即可计算；把安全失败叫 misfit 不产生新动作 |

这些理论没有因为反向搜索而得到新证据。后文也不再用相近术语把它们包装成候选。

### 4.2 新检索线的初筛

| 机制 | 表面上可算法化的结构 | 一级淘汰理由 |
|---|---|---|
| representation theory / effective use | transparent interaction→representational fidelity→informed action 的层级 | 原单位是使用系统的人在任务中的有效使用；aggregate construct 不能规定 coding agent 的安全动作；删除 coding 身份后仍成立 |
| affordance actualization | 技术—行动者关系、依赖的 affordance bundle、actualization journey | relational ontology 和组织变迁解释，不提供唯一 action；若把 dependency diagram 神经化，等同 generic DAG |
| boundary interaction | boundary complexity、boundary-object capacity、broker ability 随 brokering situation 改变 | 要观测人的 situation model 与 shared understanding；与 TMS/C3 重叠；没有离线可识别的 broker/action 反事实 |
| media synchronicity | conveyance 与 convergence 对媒介能力的不同需要 | 人类沟通 fit；最多建议何时异步/同步或换媒介，属于 C3 界面/互动设计 |
| workaround / escalation of commitment | 局部适应、沉没成本与负面信息反馈 | 解释人类/组织为何继续或绕过，不给 coding-agent 独立状态；选择 stop/continue 是 C9 或 generic sequential control |
| organizational learning | exploration/exploitation、feedback 与 routine change | 一般 RL 直接拥有同一关系；安全方向来自外部 reward，不来自 IS 机制 |
| communication privacy management | privacy boundary ownership、co-ownership 与 turbulence | 强人际披露与关系单位；做成 access policy 即回到权限/隐私控制，coding-agent 可删除 |
| contextual integrity | sender/recipient/subject/data type/transmission principle 的关系元组 | 进入最强红队，但 agent CI 直接工作已精确覆盖 |
| digitized-process drift | action graph、variation、retention、edge formation/dissolution、complexity burst | 进入最强红队，但没有 harm direction，且 generic graph 与 TACT 直接覆盖 |

初筛后没有第三个机制值得进入算法钢人化。其余机制不是“贡献小”，而是原理论本身不能承担 forward/loss/action 的责任。

## 5. 最强红队一：情境完整性

### 5.1 原机制的合法边界

Li 等人的 JAIS 论文将隐私理解为信息流是否符合特定社会情境中的规范，而不是个人是否拥有抽象的完全控制。其核心单位是一个信息流。一个 flow 至少包含信息主体、发送者、接收者、信息类型和 transmission principle；角色关系、平台、情境目标与价值决定某个 flow 是否合适。

该论文的实际经验模型不是一个自动执行 policy。它研究 OSN 用户关于个人健康信息的 normative belief 与 disclosure intention。技术控制、法律控制、community norm、personal benefit 和 altruistic value 经由 personal privacy norm 影响披露意向。其样本是 513 名人类用户的调查数据。论文承认 legislative control 的路径出现意外负向关系，并讨论 suppressor 和因果识别限制。

CI 中最有方向性的命题是，交换 sender 与 recipient、改变 transmission principle 或改变情境目的，会改变同一内容是否适当。这是一种非对称关系。然而，“某个 flow 在何种情境合适”仍需要外部规范、法律、用户授权或人工判断。理论不会从文本本身生成组织 policy，也不保证已有规范总是正确。原文反而允许当 novel flow 更好实现普遍或情境价值时，偏离既有规范可以被正当化。

### 5.2 coding-agent 的真实安全映射

若钢人化，研究对象可以定义为 coding agent 在完成 issue、调试、CI 与部署任务时，跨 repository、shell、package registry、日志、ticket、chat 和外部 API 传播敏感或越界信息。

潜在损害包括把 secret 写入 patch/commit/PR，把一个客户的日志交给另一个客户，把内部 vulnerability detail 发往公开 issue，在 tool query 中过度提交源代码，或把本来只应暂存于 agent memory 的信息带入子代理消息。风险发生在 retrieval query、tool response、memory write、subagent transfer、code generation、commit/PR output 与 external API call 等多个时点。

推断时可见任务、调用者、目标 repository、角色、工具 schema、可访问文档、数据 provenance、历史 flow 和候选 action。不可见或不确定的是组织中未形式化的规范、数据主体的真实预期、用户授权是否仍有效、一个 code fragment 是否可反推出敏感业务逻辑，以及将来谁会读取生成物。

正常动作包括最小化 query、只读检索、局部摘要、生成不含 secret 的 patch 和在批准范围内发送结果。风险动作包括 over-query、跨 tenant 检索、将敏感 observation 拼入 prompt、向未授权 recipient 发送内容和把机密写入持久 artifact。纠正动作包括 redaction、query narrowing、recipient-specific rendering、provenance projection、capability restriction、quarantine、请求授权和停止。

这些损害真实且重要；问题不因情境重要而自动成为新论文。接下来必须检查 CI 是否产生直接工作没有拥有的算法算子。

### 5.3 MEC→MAP→ALG 的最强尝试

#### MEC

理论要求每条信息边保留关系元组

`q_t = (subject_t, sender_t, recipient_t, data_type_t, transmission_principle_t, context_t, value_t)`。

同一信息 `x` 的 `sender→recipient` 与 `recipient→sender` 不可交换；同一 recipient 下，“为修复缺陷而临时访问”与“公开发布”也不可交换。将信息是否敏感压成 content-only label 会系统性丢失这两个方向。

#### MAP

对 coding-agent trajectory 建立时变 Privacy Flow Graph。节点是 user、agent、subagent、repository、tool、memory、external service 与 downstream recipient；边是 query、observation、write、message、patch、commit 或 API payload。每条边带 CI 元组、source hash、action hash、生命周期与可见角色集合。

#### ALG

若强行做到算法级，最低工件如下。

- 输入。任务文本、repository/issue/log 片段、工具 schema、调用者与 recipient role、provenance、历史 flow graph、候选低层动作。
- 文本张量。`H_t∈R^{n_t×d}`，由代码—自然语言联合编码器产生；每个 token 带 provenance、tenant、artifact type 与 intended recipient embedding。
- flow 张量。`F_t∈R^{m_t×(d_q+d_s)}`，每条历史或候选边串接五个 CI 参数、context/value embedding、content summary 和 source/action hash。
- visibility 张量。`V_t∈{0,1}^{u×a}`，记录用户/角色对 atomic attribute 的许可可见性；`N_t∈{0,1}^{a}` 记录当前任务所需属性。
- 架构。heterogeneous flow-graph Transformer 编码 `H_t/F_t/V_t`；一个 counterfactual action decoder 对 `retrieve(q)`、`retrieve_narrow(q')`、`redact(S)`、`send(r,p)`、`ask(scope)`、`quarantine` 与 `stop` 进行执行后信息流 rollout。
- 输出。每个候选动作的 task utility、appropriateness violation、visibility violation、persistent exposure 与 action cost 分布，并输出一个具体低层动作，不输出自然语言政策建议。
- 监督。scenario-level appropriate/inappropriate attribute、visibility matrix、per-stage flow labels、实际执行后的 secret exposure、任务 oracle 与 human norm adjudication。
- 损失。`L=L_action+λ1L_appropriateness+λ2L_visibility+λ3L_flow_contrast+λ4L_utility+λ5L_calibration`。其中 `L_flow_contrast` 对同一内容、不同 recipient/transmission principle 的 paired flow 强制不同 margin。
- 推断。先在 shadow tool 上展开 candidate flow，再选择满足风险预算且保留最高任务效用的 action；若规范 posterior 不确定才执行 `ask(scope)`。
- checkpoint。代码—文本 encoder、flow-graph encoder、counterfactual transition head、action policy 与 calibration map 分开保存。
- 可运行数据。CI-Work、AgentSCOPE、PiSAs 与可许可的 coding workspace 合成实例可提供 schema；SABER/CLAWS 类容器可提供最终状态与工具行为；敏感内容必须合成或来自授权隔离环境。
- 划分。按 organization/domain/repository/recipient topology 留出；同一 scenario template、原始文档与改写不得跨 split；生成器 prompt、judge 与 hidden policy manifest 固定。
- 算力。以 7B–14B 开源代码模型 LoRA 加 100M–400M flow graph/world head 为最低主工件；8×80GB GPU 级别完成多分支 rollout 训练，单卡只能做小模型 feasibility，不足以与最强开源 agent 公平比较。

这个设计确实比 content classifier、prompt rule 或 top-k filter 更硬。它仍然没有通过独立贡献门。

### 5.4 直接覆盖反证

AgentSCOPE 已经把 agent execution 拆成 user、agent、external tool 与 downstream recipient 之间的显式信息边。每条边精确标注 sender、recipient、subject、data type 与 transmission principle，组成 Privacy Flow Graph；benchmark 进一步区分 over-query、over-return 与 over-disclosure，并在中间阶段提供 ground truth。拟议的 `F_t` 不是一个尚未出现的理论张量，而是这一工作已经公开的图 schema 的可训练扩展。

CI-Work 已经把企业 agent 轨迹写成 `H={(a_t,o_t)}`，将累积检索条目分为 task-essential set 与 context-sensitive set，并同时报告 leakage、violation 和 conveyance。五种上下左右/外部 flow direction、dense retrieval 和 privacy–utility trade-off 直接覆盖“组织角色改变同一内容的 appropriateness”。

PiSAs 已经对每个 attribute 同时标注任务 appropriateness 与合法可见用户集合，并评价 output、inter-agent communication 和 memory 的跨用户 spillage。拟议的 `V_t` 与 `N_t` 已有直接数据结构，multi-agent topology 与 persistent memory 也不再是 coding-agent 新增。

AgentSecBench 把 application policy 表示为 authorized observation 与 capability projection，区分 prompt annotation 与真正关闭 model-visible channel 的 enforcement，并用 paired adversarial/benign execution 测量 confidentiality 与 capability integrity。只要情境规范被形式化为可执行 policy，provenance projection、least-privilege gating、output validation 和 noninterference 已经是强基线；新设计不能以“理论指导 redaction”绕过。

这些工作并非只共享“隐私”一词。它们拥有同一 flow unit、相同角色条件、相同 intermediate boundary、相同 visibility/necessity label、相同 privacy–utility 外部结果和同类执行动作。把数据源换成 source code、CI log 或 vulnerability report 是重要领域实例，却不是独立算法类。

### 5.5 coding-agent 删除检验

进行以下删除操作。

1. 将 repository/issue/log 换成 email/calendar/CRM/health record。
2. 将 patch/commit/PR 换成 report/message/ticket update。
3. 保留 user、agent、tool、memory、recipient、visibility matrix、CI tuple、appropriateness label 与 action projection。
4. 保留 over-query、over-return、over-disclosure、redact、narrow、ask、send 与 stop。

删除后，模型输入、关键张量、训练损失、推断动作和主要 privacy–utility 指标完全成立。coding agent 只是一个应用域。若为通过删除门而把损害改成“secret 被写入可执行代码后触发供应链事件”，核心新增监督来自 software-security taint/provenance 与执行 oracle，CI 只负责 recipient/context label，仍不能承担新算法主体。

### 5.6 等参数通用反证

构造 `Generic-Flow` 基线：使用同参数量、同 heterogeneous graph、同 CI 元组字段但将字段匿名为 `r1…r7`；保留同一 counterfactual transition head、同一 action set、同一 risk/utility loss，只删除所有理论名称和专门分支。它可以学习同一个 conditional function

`π(a_t | H_t,F_t,V_t,N_t,history)`。

CI 候选唯一的不可交换性来自有向角色字段与 paired labels。Generic-Flow 同样接收这些字段，也同样能学习 `sender→recipient ≠ recipient→sender`。若候选要求手工 hard-code CI 规则才赢，增益来自 policy injection，不是可训练理论机制；若不 hard-code，理论模型与匿名模型函数类相同。

进一步的强基线包括 equal-parameter relational Transformer、constrained distributional POMDP、AgentSecBench projection stack、content+provenance IFC、retrieval minimization 与 recipient-specific output validator。必须在 held-out organization/domain 中同时减少 actual leakage、保持 task success 并降低 unnecessary refusal。现有证据没有说明 CI architecture 能超越这些基线的函数表达能力。

### 5.7 可识别性与外部结果反证

CIAS 类数据可识别“人们认为 flow 是否合适”，但 coding repository 中有两个额外问题。

- 组织规范常由 policy、contract、law 与 role owner 共同决定。若把完整规范给模型，任务退回 policy execution；若不给，单次 trajectory 无法识别真实授权。
- 合成 benchmark 的 essential/sensitive label 常由研究者或 LLM 先写。模型学习这些标签可以提高 benchmark 分数，却不能证明现实组织中的损害下降。

严谨评价必须把实际 secret disclosure、unauthorized external write、cross-tenant exposure 与 task completion 作为主要结果，而不能只用 norm classification。AgentSecBench、AgentSCOPE 与 PiSAs 已经朝这一方向建立可执行评价。coding-specific adaptation 仍可作为 benchmark 或 empirical paper，但不足以承担一篇理论驱动算法论文。

### 5.8 C1–C27、C3 与迁移题边界

CI 若采取 pre-generation filtering、provenance projection 或 capability restriction，落入 C6/C7/C13。若采取不确定时询问批准，落入 C9；若由真人逐步形成共享理解，又共享 C3 的 fixed approval、evidence sequence 和 grounding repair。若把 CI 用于 pre-cutover 数据访问，迁移题已经拥有固定 action lattice，CI 只能是外生 policy constraint，不能新增一个题位。

与 C3 的唯一区别本可在于 CI 的主要结果是未经授权的信息流，而 C3 的主要结果是 fixed high-impact action 的真人 unsafe approval。可是 CI 直接工作已经覆盖其独立结果，不能为了系列关系再把它并入 C3。

### 5.9 终判

**NO-GO / REMOVED。**

情境完整性是合法的理论，也是 agent 隐私的重要评价框架。本候选失败不源于理论不严肃，而是 theory-to-benchmark 和 theory-to-flow-graph 的关键迁移已经被直接完成；剩余控制被 provenance、permission 与 generic relational policy 吸收；coding-agent 删除失败。未来可使用 CI 为 C3 或其他实验定义 privacy boundary，但不得将 `CI tuple + graph Transformer + redaction policy` 作为独立论文重新提出。

## 6. 最强红队二：数字化过程漂移

### 6.1 原机制的合法边界

Pentland 等人把 digitized process 表示为有向图。节点是行动词表中的 event，边是一个行动后紧接另一个行动的 sequential relation，边权是转移频次或概率。过程复杂性用 source 到 sink 的简单路径数表示。

2020 年论文通过 simulation 研究内生 drift。四个关键设计量是 action lexicon size `L`、modularity `M`、variation probability `V` 和 retained history `R`。每次 process iteration 形成一条 path；`L×L` 历史矩阵 `H_t` 保存最近 `R` 条 path 的相邻行动计数。variation 可能形成新边，历史窗口中的选择性 reinforcement 与 forgetting 使边保留或消解。由于 graph density 与 simple-path count 的非线性关系，少量重边的出现或消失可以触发 complexity burst、phase change 和新的 dominant path。

这个机制确有结构和时间顺序。`A→B` 与 `B→A` 是不同边；先形成边、再让它进入 retention window，与从未形成该边产生不同 future path set。`L/M/V/R` 改变 average complexity、phase-change likelihood 和 magnitude 的方向也在 simulation 中有明确命题。

然而原文同时固定三条边界。

1. 分析限于没有 external intervention 或 performance feedback 的 endogenous change。
2. drift 可能有益，也可能有害；learning/adaptation 与 drift into disaster 都符合机制。
3. 复杂性、phase change 和 accumulated structural change 是结果，不是 safety loss。理论没有给出哪个 path 更正确、更安全或更符合用户目标。

2021 年有向图论文进一步将 `P(V,E)` 与 `Δ(V,E)_t` 定位为分析和测量 process dynamics 的基础。作者明确称它接近 Gregor Level 1 theory；解释 signal/noise 还需要其他理论、访谈或现场信息。该论文也指出 directed graph 不表示 concurrency、control flow、resource stocks 或 executable process semantics。

### 6.2 coding-agent 的真实安全映射

钢人化研究可把一次 coding-agent session 看成行动序列。节点词表包括 `inspect_issue`、`search_code`、`read_file`、`edit_code`、`edit_config`、`install_dependency`、`run_test`、`run_shell`、`commit`、`deploy`、`ask_user` 与 `stop`。边表示实际相邻行动，跨 session 的窗口记录某 repository/harness/model 反复形成的 routine。

真实损害可能是 agent 逐渐形成“读一个文件后立即大范围修改”“测试失败后反复改配置”“未验证便安装依赖”“在错误积累后扩大 shell 探索”等路径。复杂性 burst 可能表现为工具链扩张、分支反复、上下文污染和未验证行动相互放大。Tang 等人的真实 session 分析、SABER、HINTBench、Agent Meltdowns 与 TACT 都证明长轨迹中存在实际的 misalignment、overacting、operational harm 与 failure propagation。

风险时点是在下一次行动提交前。可见状态包括 task、repository、当前 diff、工具历史、test evidence、action graph 与近若干 trajectories；隐藏状态包括真实 bug cause、hidden tests、future dependency effect 和用户未写明约束。正常动作是读、局部改、执行区分性验证和停止；风险动作是过早修改、无证据扩展工具、重复无信息行动和高影响命令；纠正动作可以是补充观测、撤销未提交编辑、缩小动作、执行 verifier、请求用户澄清或停止。

问题是真实的。失败发生在从 graph dynamics 跳到 safety direction 的一步。

### 6.3 MEC→MAP→ALG 的最强尝试

#### MEC

保留 action lexicon、directed adjacency、retention window、variation、reinforcement/forgetting 和 modularity。理论预测接近临界密度时，局部 edge change 会引发超线性的 path-complexity change。因而控制器不应只给单步 risk score，而应预测候选 action 加边后对未来可达路径集合的边际作用。

#### MAP

对每个 repository/harness/model 建立多尺度 action graph。session 内图追踪当前任务，跨 session 图追踪 routine drift；代码、配置、依赖和验证动作各属一个 module。将候选下一行动实例化为可能新增、强化或弱化的 edge，并展开 graph density、simple-path count、dominant path 与 module crossing 的后果。

#### ALG

最低可训练工件如下。

- 输入。任务、repository state、diff、tool schema、最近 `R` 条 action paths、当前证据、候选参数化 action。
- 动作编码。`X_t∈R^{L×d}` 表示 typed action nodes，`A_t∈R^{L×L×c}` 表示 directed edge count/probability、age、repository/module 与 outcome channels。
- 历史张量。`H_t∈N^{R×L×L}` 保存每条 retained trajectory 的 directly-follows matrix；`Z_t∈R^{L×d_z}` 为 temporal graph encoder 状态。
- 架构。temporal graph network 预测每个候选 action 对 edge update、未来 path sample、test/task outcome 与 harm outcome 的分布；distributional policy 在 `inspect/edit/test/ask/stop` 与参数化 shell/tool action 中选择。
- 输出。`ΔE_t`、future graph、complexity burst probability、task success、operational harm、steps/cost，并执行一个真实 action。
- 监督。SWE-bench/Terminal-Bench/CLAW-Eval trajectories 提供 task outcome；SABER 提供 final-state harm；HINTBench 提供 step localization；TACT 的 OT/OA/CAL 标签可作辅助监督；真实 session 只作外测，不能把 developer pushback 当完整 harm truth。
- 损失。`L=L_transition+λ1L_task+λ2L_harm+λ3L_calibration+λ4L_cost+λ5L_graph`；`L_graph` 预测 observed edge formation/dissolution 与 path-complexity change。
- 推断动作。若一个 action 的 task value 高但 predicted harm 或 irreversible module crossing 超预算，则在更低风险的 evidence action、scoped edit、ask 或 stop 中选择；不以“复杂度高”自动拒绝。
- checkpoint。action tokenizer、temporal graph encoder、transition/world head、harm head、policy 与 calibration 独立保存。
- 划分。按 repository、issue family、harness、model family 与时间切分；同一 issue 的 agent/model replicas 不得跨 split；历史 graph 只使用当时可见路径。
- 算力。7B–14B open code backbone 加 200M–500M temporal graph/world head，至少 8×80GB GPU 和大规模容器分支执行；需要保存每次 action、state hash、test/harm oracle 与 generator version manifest。

这是一项可运行的 trajectory world-model 研究。它不是过程漂移理论独有的算法。

### 6.4 理论方向缺失

设两个 matched states 的 action graph、retention window 与候选 edge 完全相同。世界 A 中新边 `edit_config→run_test` 修复了此前无法验证的环境，复杂性 burst 增加了成功路径；世界 B 中同一边掩盖了代码缺陷并破坏部署。过程漂移理论对两世界给出相同的 edge update、density 与 path count。安全选择只能依赖外部 task/harm oracle、repository semantics 或 policy constraint。

这不是一个需要更多数据便会消失的小问题。原理论为保持内生性主动排除了 performance feedback，所以不能从其命题推出“降低 variation”“压低 complexity”“恢复 dominant path”恒为安全。将 harm head 接到 graph encoder 后，真正决定 action 的是一般后果预测；drift tensor 只是可能有用的 feature。

再考虑顺序冲突。候选可以声称 `inspect→edit` 比 `edit→inspect` 安全。该方向来自 coding task 的 evidence semantics，而不是 drift theory；原理论只知道两条路径不同，不知道哪个先后更好。若用 hidden test 与 state damage label 学习方向，generic sequence model拥有同一监督。

### 6.5 直接覆盖反证

TACT 已经明确研究 coding-agent drift，把每一步标为 overthinking、overacting 或 calibrated，抽取 hidden-state mean-difference axes，在 transformer forward pass 的 `</think>` token 上进行 gated/capped steering。它在 SWE-bench Verified、Terminal-Bench 2.0 与 CLAW-Eval 上使用 disjoint axis-train/axis-val/eval splits，并保存每层 axis、centroid 与 threshold。新的“学习 drift 表示并在动作前干预”不能忽略这一直接工件。

Wink 在 production coding trajectories 中检测 misbehavior 并给予 targeted correction。AgentRx 定位 critical failure step。HINTBench 评价长轨迹 risk localization。SABER 以最终 workspace state 评价 harm。Tang 等人又提供真实开发者纠正和 damage locus。把这些标签合并到 temporal graph world model 是合理工程，但核心能力已经由 trajectory diagnosis、risk localization、activation steering 与 operational safety evaluation 分别覆盖。

Pentland 等人的 2021 论文自己也把 process mining、drift detection、variation analysis 和 directed graph measurement 视为既有方法岛。新题若只报告 graph complexity 能提前预测失败，属于新的 empirical predictor；若由 graph world model选择行动，算法主体是一般 model-based control。

### 6.6 coding-agent 删除检验

将节点词表换成临床记录、采购、保险理赔、机器人流程或 enterprise API 动作，保留 action graph、history window、variation、modularity、edge reinforcement、complexity burst、task outcome 与 harm outcome，整个模型和 loss 仍成立。事实上原理论明确追求跨 human/material agents 的一般 digitized process，并不把行动者身份写入机制。

若加入 AST、repository dependency graph 与 executable test 才让 coding 变得不可删除，新增不可删除部分来自软件语义和执行验证，不来自 process drift。该候选会转为 repository world model 或 coding-agent trajectory safety，必须与 LoopsBench、TACT、SABER、C21 repo drift 和通用世界模型比较；理论贡献不能靠名字保留。

### 6.7 等参数通用反证

构造 `Generic-TGWM`：输入完全相同的 `X_t/A_t/H_t`、repository state、candidate action 与 outcome labels，使用同参数 temporal graph encoder 和 distributional transition/policy head，只把 `variation/modularity/retention` 字段匿名为 learned graph statistics，不加入 drift-specific proposition loss。

原候选的 forward 是

`Z_t = TGNN(X_t,A_t,H_t);  p(s_{t+1},y_h,y_u|Z_t,a_t);  π=argmax_a E[U-λH-C]`。

Generic-TGWM 的函数类相同。`L_graph` 只重建下一张图，是一般 transition auxiliary loss；path count 与 density 可作为匿名 deterministic features直接输入。理论模型没有一个通用模型不能表达的非交换 operator。若删除 graph features 性能下降，只证明过程历史有用，不证明 Pentland drift 机制不可替代。

还必须比较 equal-parameter Transformer over raw action sequence、temporal GNN、process-conformance detector + policy、distributional POMDP、recurrent state-space world model 与 TACT-style activation intervention。候选没有理由预期在 matched input/action 条件下越过这些基线的等效界。

### 6.8 可识别性、划分与泄漏

公开数据可以监督 next edge、task success、某些 harm 和 step localization，不能自然监督“该 edge 是由 routine drift 机制而非 task composition、model update、harness change 或 repository difficulty 导致”。跨 session 图尤其受严重混杂：模型版本、system prompt、tool availability 与任务分布同时变化。

真实 production 数据的 developer pushback 只观察可见并被纠正的 misalignment。静默失败、用户放弃和看似成功的潜在损害缺失；同一 state 选择另一个 action 的反事实也不存在。容器中可执行 branching 能改善 action-outcome supervision，但此时学到的是 world model，不是组织 routine 的 causal drift。

任何可行实验都必须按时间与 model/harness version 双重留出，禁止将同一 issue 或同一 base trajectory 的 counterfactual branches 分到不同集合，冻结 tool schema 与 oracle，并报告 task、harm、refusal/inaction、step、latency 和 compute Pareto。做到这些能产生可靠工程研究，不能解除理论反证。

### 6.9 C1–C27、C3 与迁移题边界

若过程漂移研究的是 repository 前提在并发更改中失效，落入 C21；若研究长期义务和验证路径，落入 C1/C17；若输出 canary、rollout、rollback 与 stop，落入 C18 和迁移题；若以用户纠正建立 common ground，落入 C3。将 scope 缩成“同一 coding session 的 overacting”又被 TACT 直接覆盖。

主动缓解期权格的 episode、typed mitigation slots、defer/exercise/abandon 与 data-corruption/SLO oracle 已固定。process graph 可以作为迁移模型的 observation feature，但不得另起一个以相同 rollout、stop 与 rollback 为中心动作的题目。

### 6.10 终判

**NO-GO / REMOVED。**

数字化过程漂移提供了优秀的观察语言和可计算的结构指标，却没有提供安全方向。其有向图更新可被 generic temporal graph 精确实现，coding-agent 身份由原理论主动删除，最新 coding 直接工作又已拥有 drift label、hidden-state representation 与 inference-time intervention。未来可将 graph drift 作为 C3 或迁移实验的描述性诊断，不得声称它独立产生安全行动策略。

## 7. 其余机制为什么没有升级为候选

### 7.1 representation theory 与 effective use

Burton-Jones 与 Grange 的三维构念存在层级关系。transparent interaction 使用户不受 surface/physical structure 阻碍地取得 representation；representational fidelity 要求用户实际取得的 representation 足够忠实地反映 task-relevant domain；informed action 要求用户利用忠实 representation 改善其状态。论文明确把它们写成 user–system–task interaction 中的 use，而不是系统内部的三个模块。

把 coding agent 的 observation 叫 representation、把 state estimator 叫 fidelity、把 action policy 叫 informed action，只是重命名 perception–world model–policy。理论没有规定 fidelity tensor 的元素、belief update 的方向、risk loss 或何种 action 在冲突时优先。若把 hidden test 作为 fidelity label，真正监督来自执行 oracle；若没有 oracle，construct 不可识别。故不进入最强红队。

### 7.2 affordance actualization

Strong 等人的理论有真实的依赖结构。affordance 是具体技术与具有特定目标和能力的行动者之间的 action possibility；actualization 是个体为实现潜力而采取的行动；组织 actualization 由多个 individual journeys 与 immediate concrete outcomes 涌现。affordance bundle 中还存在先行 affordance 的 concrete outcome 为后续 affordance创造条件的依赖。

这能帮助描述 coding agent、tool、repository 与组织目标的关系，却没有为算法提供可枚举的 affordance 真值。由研究者为每个 tool 写“可查询、可修改、可部署”的 affordance DAG，再训练策略遵守依赖，是由 ontology 产生标签。匿名 typed action DAG 拥有同一 forward。组织目标 alignment 与 human actualization 又需要现场过程数据，不能由 container outcome 无损替代。若以能力选择/工具配置为动作，落入 C22；若以 delegation 为动作，落入 C27。

### 7.3 boundary interaction 与 motors of change

Rosenkranz、Vranešić 与 Holten 的 brokering situation 同时包含参与者知识、共同知识、shared understanding、knowledge-boundary complexity、boundary-object capacity 与 broker ability。边界可以是 syntactic、semantic 或 pragmatic；boundary object 的容量不足会导致 dialectical crisis，容量过高又可能因时间成本触发 teleological simplification。更换 broker 或 boundary object 会改变后续共享理解，因此过程具有方向与非交换性。

这是本轮第三强的理论结构，但它没有进入算法红队，原因有三。

1. 原单位是不同 community of practice 的人类 stakeholder 在 requirements elicitation 中形成 situation-model alignment。把 agent 与 repository 分别当 stakeholder 会把无心理状态的 artifact 错当 actor。
2. 若保留 developer、reviewer 与 agent，shared understanding、clarification、repair 和 boundary object sequence 与 C3 的 common-ground 机制直接重叠。
3. 公开 issue/PR 对话没有同一 boundary state 下替换 broker/object 的反事实安全结果。训练一个 broker/object recommender 退化为 C19 allocation 或 generic matching/communication policy。

该理论可用于解释 C3 的边界条件，不能形成独立题目。

### 7.4 media synchronicity、communication privacy management 与 temporal entrainment

这些理论含有时间或边界关系，但主要分析人类沟通。media synchronicity 区分 conveyance 和 convergence 过程，并把 transmission velocity、parallelism、symbol sets、rehearsability 与 reprocessability 连接到沟通表现；communication privacy management 关注 disclosure boundary、co-ownership 与 boundary turbulence；temporal entrainment 关注群体节奏协调。

将它们用于 coding-agent approval 会改变展示方式、交互节奏或是否同步沟通，中心结果仍是人的理解、负担与批准，属于 C3 的 human oversight 环境。若删除人类，它们失去原构念单位；若把人类保留，独立题会共享 C3 的 intervention 与 outcome。故只可作为边界条件或实验 moderator。

### 7.5 workaround、escalation、organizational learning 与 loose coupling

workaround 与 escalation 解释行动者为何绕开正式流程或在负面信息下继续承诺。coding agent 并不存在未经设计即可观察的沉没成本感知、身份维护或政治动机；用 token/step cost 代替这些构念是层级错置。organizational learning 的 exploration/exploitation 和 feedback relation 直接被 RL/world model 包含。loose/tight coupling 与 interactive complexity 可描述系统风险，却没有推出代码修改、权限或 tool action 的唯一方向。

这些理论最多提供现象解释、风险分层或实验 heterogeneity。它们不能承担独立可训练决策能力。

## 8. 两个最强机制的并排终审

| 门 | 情境完整性 | 数字化过程漂移 |
|---|---|---|
| 真实损害 | secret/cross-tenant/unauthorized information flow | 长轨迹 overacting、错误扩张、workspace/project/external harm |
| 原理论分析单位 | 人类社会情境中的 information flow 与 disclosure norm | digitized process 的 action pattern 与 graph change |
| 最强理论结构 | directed role tuple、transmission principle、context/value | directed edge、retention、variation、reinforcement/forgetting、phase change |
| 能否形成结构张量 | 能，flow graph 与 visibility matrix | 能，temporal action graph 与 history matrix |
| 是否产生安全方向 | 由外部 norm/policy/authorization 决定 | 否；drift/complexity 可益可害 |
| 最强直接覆盖 | AgentSCOPE、CI-Work、PiSAs、AgentSecBench | TACT、Wink、AgentRx、HINTBench、SABER |
| coding-agent 删除 | 失败；换成 enterprise/personal agent 任务保持不变 | 失败；原理论本来跨一般 digitized process |
| equal-parameter generic | relational graph/policy 可复制 | temporal graph/world model 可复制 |
| 与旧题冲突 | C6/C7/C9/C13；人类互动时与 C3 重叠 | C1/C17/C18/C21；stop/rollback 时与迁移题重叠 |
| 终判 | NO-GO | NO-GO |

两个机制都能产生“好看的张量”，但张量存在不是理论算法资格。CI 的元组已经被直接技术工作采用，drift 的图更新又没有 safety direction。一个是 direct coverage 失败，一个是 normative direction 与 generic proof 双重失败。

## 9. 对三篇系列与现行题位的影响

### 9.1 不新增第三篇或替代题位

当前总体主线仍不能诚实宣称已有三篇。C3 保持其既有状态；主动缓解期权格继续由其独立锁定审计决定。0 候选不会改变任何旧题的状态，也不会把 CI 或 process drift 降格成“先写一篇 benchmark paper 再升级”的预留题。

### 9.2 可以合法复用但不能主张的资产

- CI tuple、Privacy Flow Graph、visibility matrix 可以成为未来实验的 privacy boundary 与 evaluation slice。
- process directed graph、edge-change 和 complexity trace 可以成为失败分析、可视化或 distribution-shift diagnostic。
- effective use、affordance actualization 与 boundary interaction 可以帮助解释 field findings 或界定 human/organizational boundary。
- 这些元素均不能作为新论文主要理论算法贡献，也不能在标题中通过“context-aware”“drift-aware”恢复。

### 9.3 与博士论文组织逻辑的关系

目标博士论文的三个研究之所以形成系列，不是因为每篇都复用一个术语，而是相同总体张力在不同情境中产生不同决策对象、状态与算法。反向搜索若保留 CI privacy controller，会把总体张力从可靠高影响行动切换为一般 agent 信息流；保留 process drift controller，又会与现有 trajectory/release/migration 动作混叠。二者不能只凭“也属于广义安全”成为同一 thesis 的独立子研究。

真正的新题必须同时与 C3 的真人固定批准点、迁移题的 pre-cutover mitigation lattice 和 C1–C27 的已覆盖动作错开。它还要拥有独立 harm、独立可执行 action space、独立 training checkpoint 和独立外部结果。当前两条线都不满足。

## 10. 理论机制反向搜索的最终可复查命题

1. Otero Basket 中存在能够自然描述 coding-agent 风险的理论，不代表存在能够自然控制 coding-agent 行动的理论。
2. 原构念的关系方向必须在迁移后保留。把人类 privacy norm、shared understanding 或 organizational capability 改成模型 hidden state，不是无损映射。
3. 有向图、元组或依赖结构只是 ALG 的必要载体，不自动成为理论独有算子。
4. 如果安全方向来自 hidden test、policy、human label 或 executable harm oracle，就必须把理论责任限定到它实际产生的部分，不能把整个 policy 称为 theory-driven。
5. direct technical work 已经使用同一 theory schema 时，领域适配必须产生新的不可删除行动与结果，而不能只换数据源。
6. equal-parameter generic model 若接收同一关系字段和监督，就有权学习相同非对称性；理论模型必须给出额外、可检验而非手工注入的计算限制。
7. 0 个候选是本轮检索的有效结果。没有证据时不应把机制漏斗转成选题生产线。

## 11. 肖帅勇老师 ISR 句段功能对照

### 11.1 使用口径

本节只比较学术功能，不复制肖老师原句。`source_anchor` 必须来自 `00W`。`source_function_code` 和 `candidate_function_code` 使用 `00F` 的代码：`CXT/IMP/DEF/ACK/LIM/MEC/CON/GAP/RQ/MAP/ALG/EVAL/RES/CONB/BND`。解析到真实句键不等于功能同位；没有同位功能时明确写“无锚点”。每一项链均完整写为 `PRE→SRC_NEW/CAND_NEW→REL→CIT→NEXT→RESULT`，其中 `RESULT` 只取保留、改写、拆分、合并、删除。

### 11.2 逐单元功能审计

| 本文件单元 | source_anchor | source_function_code | candidate_function_code | 完整功能链 | RESULT |
|---|---|---|---|---|---|
| 0 审查任务与边界 | DSDL-I1-S01–S05 | CXT→IMP | CXT→BND | `PRE=长期Goal的理论反向搜索→SRC_NEW=从数字化商业变化推进到管理对象/CAND_NEW=从Otero机制搜索推进到资格边界→REL=同为情境收束但本文件是内部审计→CIT=Otero协议与00A/00B/00E→NEXT=先验状态→RESULT=改写` | 改写 |
| 0.1 先验状态 | 无锚点 | BND | BND | `PRE=审查范围→SRC_NEW=无正式论文同位锚点/CAND_NEW=冻结C1–C27及现行题位→REL=内部治理材料不得移入论文正文→CIT=00A/00B/00E→NEXT=终局答案→RESULT=保留` | 保留 |
| 0.2 终局 0 候选 | 无锚点 | RES | RES→BND | `PRE=先验约束→SRC_NEW=肖文无撤题型结果段/CAND_NEW=报告零候选及两条终止原因→REL=仅内部选题结果→CIT=后续两项全文反证→NEXT=阅读账→RESULT=保留` | 保留 |
| 1.1 项目材料 | ACAA-M0-S01–S02 | ACK→MAP | ACK→BND | `PRE=终判需要可追溯来源→SRC_NEW=回收理论与方法结构/CAND_NEW=登记完整回读材料与各自责任→REL=证据前置而非方法贡献→CIT=本地文件与SHA主键层→NEXT=全文阅读账→RESULT=合并` | 合并 |
| 1.2 Basket 阅读账 | DSDL-L1-S01–S08 | CXT→IMP | ACK→MEC | `PRE=材料层→SRC_NEW=建立文献流及其业务结果/CAND_NEW=按全文范围建立机制证据流→REL=同为文献责任但候选强调审计状态→CIT=DOI与Otero全文→NEXT=查询词→RESULT=保留` | 保留 |
| 1.3 查询词与引用链 | ACAA-L11-S01–S08 | GAP→ACK | GAP→ACK | `PRE=已读全文→SRC_NEW=系统组织直接与邻近文献/CAND_NEW=按机制组织查询并沿两条引用链回读→REL=功能同位于文献边界建立→CIT=Otero检索与参考链全文→NEXT=技术近邻→RESULT=保留` | 保留 |
| 1.4 技术近邻 | DSDL-I5-S01–S04 | GAP | GAP→ACK | `PRE=IS机制来源→SRC_NEW=用对象和数据结构证明旧方法失配/CAND_NEW=用unit/graph/labels/actions证明直接同位→REL=反向使用近邻证成无新增空间→CIT=AgentSCOPE/CI-Work/PiSAs/TACT等全文→NEXT=资格门→RESULT=保留` | 保留 |
| 2 资格门 | 无锚点 | BND | BND | `PRE=证据来源→SRC_NEW=无正式论文同位锚点/CAND_NEW=冻结MEC到generic七道资格门→REL=内部选择规则→CIT=用户完成标准与00F→NEXT=C1–C27边界→RESULT=保留` | 保留 |
| 3 禁止返回边界 | 无锚点 | BND | BND | `PRE=一般资格→SRC_NEW=无正式论文同位锚点/CAND_NEW=把旧题终判变成不可移动约束→REL=仅内部防重复→CIT=00A/00B/00E及各终审→NEXT=理论全漏斗→RESULT=保留` | 保留 |
| 4.1 已否决理论 | DSDL-L8-S01–S05 | CON→GAP | CON→BND | `PRE=旧题边界→SRC_NEW=综合理论挑战并导向方法需求/CAND_NEW=复核原单位并阻止换名返回→REL=候选不再制造新GAP→CIT=原理论全文→NEXT=新机制初筛→RESULT=改写` | 改写 |
| 4.2 新机制初筛 | DSDL-T7-S01–S05 | MEC→MAP | MEC→GAP | `PRE=旧理论退出→SRC_NEW=把理论命题连到当前方法挑战/CAND_NEW=把每个机制连到可算法结构及一级否决→REL=同为理论筛选但结果为淘汰→CIT=六篇Basket全文→NEXT=CI红队→RESULT=拆分` | 拆分 |
| 5.1 CI 原机制 | DSDL-I6-S01–S05 | MEC | DEF→MEC→LIM | `PRE=初筛入围→SRC_NEW=以理论建立不可替代中间状态/CAND_NEW=定义flow元组、方向与人类披露边界→REL=只有构念关系同位，行动单位不同→CIT=Li等JAIS全文→NEXT=安全映射→RESULT=保留` | 保留 |
| 5.2 CI 安全映射 | DSDL-I4-S01–S08 | GAP→MAP | CXT→IMP→MAP | `PRE=原理论→SRC_NEW=从信息缺口推进到可观测对话信号/CAND_NEW=从信息流风险推进到agent可见/隐藏状态和动作→REL=同为观测机会但安全结果不同→CIT=CI与agent隐私工作→NEXT=MEC到ALG→RESULT=保留` | 保留 |
| 5.3 CI 算法钢人 | DSDL-M2-S01–S08 | ALG | MAP→ALG | `PRE=理论与场景→SRC_NEW=端到端口述数据流及组件职责/CAND_NEW=口述flow graph张量、world rollout与低层动作→REL=功能同位，不复制具体结构→CIT=模型定义与公开benchmark→NEXT=直接覆盖→RESULT=保留` | 保留 |
| 5.3 CI 输入标签 | DSDL-M4-S01–S06 | MAP→EVAL | MAP→EVAL | `PRE=总体工件→SRC_NEW=定义原始样本、标签和过滤/CAND_NEW=定义attribute/visibility/flow/action outcome及split→REL=数据责任同位→CIT=AgentSCOPE/PiSAs schema→NEXT=loss与动作→RESULT=保留` | 保留 |
| 5.3 CI 非对称表示 | DSDL-M14-S01–S08 | ALG | MEC→ALG | `PRE=CI关系元组→SRC_NEW=跨角色Q/K/V形成专门非对称匹配/CAND_NEW=sender/recipient/transmission principle形成有向flow encoding→REL=共享非对称关系功能但对象不同→CIT=CI原理论与PFG→NEXT=generic反证→RESULT=改写` | 改写 |
| 5.4 CI 直接覆盖 | DSDL-I5-S01–S04 | GAP | GAP→RES | `PRE=最强工件→SRC_NEW=按对象/数据失配建立研究空白/CAND_NEW=按同unit/label/action证明空白已被占据→REL=同一审查功能、相反结论→CIT=四项直接全文→NEXT=coding删除→RESULT=保留` | 保留 |
| 5.5 CI coding删除 | 无锚点 | BND | BND | `PRE=直接覆盖→SRC_NEW=无肖文同位锚点/CAND_NEW=用跨域替换保持I/O/loss/action证明可删除→REL=内部独立性反证→CIT=AgentSCOPE/CI-Work/PiSAs→NEXT=generic反证→RESULT=保留` | 保留 |
| 5.6 CI generic反证 | DSDL-I9-S01–S07 | GAP→ALG | ALG→BND | `PRE=coding删除→SRC_NEW=并置理论路径与黑箱路径并给出联合解/CAND_NEW=给匿名等参数模型同字段同监督的精确复制→REL=同为理论与generic关系审查但结论相反→CIT=函数类与基线定义→NEXT=可识别性→RESULT=保留` | 保留 |
| 5.7 CI 可识别性 | DSDL-M19-S01–S02 | CON→ALG | CON→EVAL | `PRE=函数类反证→SRC_NEW=无中间真值时用外部结果弱监督/CAND_NEW=指出规范未给或完整给定时分别不可识别/退化→REL=同为监督边界→CIT=CI调查限制与benchmark生成法→NEXT=边界冲突→RESULT=保留` | 保留 |
| 5.8–5.9 CI 边界与终判 | DSDL-Z3_6-S01–S11 | LIM→BND | BND→RES | `PRE=识别失败→SRC_NEW=在结尾集中限定适用边界/CAND_NEW=定位C6/C7/C9/C13/C3并撤题→REL=边界功能同位，撤题动作仅内部→CIT=00A/00B/00E→NEXT=drift红队→RESULT=合并` | 合并 |
| 6.1 drift 原机制 | DSDL-I6-S01–S05 | MEC | DEF→MEC→LIM | `PRE=第二机制入围→SRC_NEW=理论给出方向差中间状态/CAND_NEW=定义L/M/V/R、H与edge dynamics并同时保留无feedback边界→REL=同为机制定义但drift无安全方向→CIT=Pentland等2020/2021全文→NEXT=安全映射→RESULT=保留` | 保留 |
| 6.2 drift 安全映射 | DSDL-I7-S01–S08 | MAP→RQ | CXT→IMP→MAP | `PRE=原图机制→SRC_NEW=从不可观测状态形成RQ和表示/CAND_NEW=把action path映射到coding harm时点与动作→REL=同为构念到任务映射→CIT=TACT/SABER/Tang等→NEXT=算法钢人→RESULT=保留` | 保留 |
| 6.3 drift 算法钢人 | DSDL-M0-S01–S03 | MAP→ALG | MAP→ALG | `PRE=问题映射→SRC_NEW=将理论挑战收束为工件能力/CAND_NEW=将edge update与harm world model收束为张量/损失/动作→REL=功能同位→CIT=原simulation与技术数据→NEXT=方向反证→RESULT=保留` | 保留 |
| 6.3 drift 历史张量 | DSDL-M10-S01–S12 | ALG | MEC→ALG | `PRE=总架构→SRC_NEW=公开理论中间张量的构造规则/CAND_NEW=公开H_t、A_t、edge age与history window→REL=同为结构张量语义化→CIT=Pentland simulation appendix→NEXT=loss和policy→RESULT=改写` | 改写 |
| 6.4 方向缺失 | DSDL-M17_18-S01–S04 | MEC→ALG | MEC→BND | `PRE=有向graph张量→SRC_NEW=理论规定不可交换的F-E方向/CAND_NEW=构造同graph不同harm世界证明drift没有方向→REL=以肖文真正有方向机制作为反证标尺→CIT=Pentland原文无feedback/益害双可能→NEXT=直接覆盖→RESULT=保留` | 保留 |
| 6.5 drift 直接覆盖 | ACAA-I5-S01–S09 | GAP→RQ→ALG | GAP→RES | `PRE=理论方向失败→SRC_NEW=由直接近邻不足推出算法研究问题/CAND_NEW=由TACT等直接工件证明detector/intervention已占据→REL=相反结论的同功能审查→CIT=TACT/Wink/AgentRx/HINTBench/SABER→NEXT=coding删除→RESULT=保留` | 保留 |
| 6.6 drift coding删除 | 无锚点 | BND | BND | `PRE=直接近邻→SRC_NEW=无肖文同位锚点/CAND_NEW=用临床/采购/流程替换保持graph机制→REL=内部对象必要性反证→CIT=Pentland跨域定义→NEXT=generic反证→RESULT=保留` | 保留 |
| 6.7 drift generic反证 | DSDL-M21-S01–S05 | ALG | ALG→BND | `PRE=对象删除→SRC_NEW=理论序列进入深度预测并保留方向约束/CAND_NEW=展示匿名TGWM使用同函数类精确复制→REL=同为前向责任审计、结论相反→CIT=候选函数与baseline manifest→NEXT=可识别性→RESULT=保留` | 保留 |
| 6.8 drift 泄漏与划分 | DSDL-E4-S01–S06 | EVAL→BND | EVAL→BND | `PRE=generic反证→SRC_NEW=给数据分割、复现和附录出口/CAND_NEW=冻结repo/issue/model/time隔离与branch leakage→REL=评价责任同位→CIT=技术benchmark与manifest→NEXT=旧题边界→RESULT=保留` | 保留 |
| 6.9–6.10 drift 边界与终判 | ACAA-P7-2-S01–S08 | LIM→BND | BND→RES | `PRE=识别与泄漏→SRC_NEW=结论限定外推和未来研究/CAND_NEW=定位C1/C17/C18/C21/C3/迁移并撤题→REL=边界同位、撤题仅内部→CIT=全部终审→NEXT=其余机制→RESULT=合并` | 合并 |
| 7.1–7.5 其余机制 | DSDL-L3-S01–S07 | CON→GAP | MEC→BND | `PRE=两条最强线退出→SRC_NEW=综述近邻并界定不足/CAND_NEW=逐一核原单位后在一级门淘汰→REL=同为理论筛选但不制造伪GAP→CIT=五组Basket全文→NEXT=并排终审→RESULT=拆分` | 拆分 |
| 8 并排终审 | ACAA-P6-1-S01–S09 | CONB→BND | CONB→RES | `PRE=单线终判→SRC_NEW=综合理论方法与证据贡献/CAND_NEW=并排比较十道资格门并确认零候选→REL=综合功能相近，候选是内部selection result→CIT=前述全文证据→NEXT=系列影响→RESULT=保留` | 保留 |
| 9 系列影响 | DSDL-C3-S01–S04 | CONB | CONB→BND | `PRE=零候选→SRC_NEW=回收方法/理论贡献与情境价值/CAND_NEW=说明不改变C3/迁移且不强凑thesis→REL=同为贡献边界但无新贡献可宣称→CIT=目标博士论文与现行审计→NEXT=最终命题→RESULT=改写` | 改写 |
| 10 可复查命题 | DSDL-Z3_6-S01–S11 | LIM→BND | BND | `PRE=系列影响→SRC_NEW=集中报告局限与未来边界/CAND_NEW=冻结反向搜索的七条可复查规则→REL=边界功能同位→CIT=本文件全部证据→NEXT=句段审计→RESULT=保留` | 保留 |
| 12 引用核验与 13 机械审计 | 无锚点 | ACK→BND | ACK→BND | `PRE=功能审计→SRC_NEW=无正式正文同位锚点/CAND_NEW=记录元数据、读取范围与文件唯一性→REL=内部证据管理→CIT=DOI/API/本地机械检查→NEXT=交付→RESULT=保留` | 保留 |

### 11.3 本次从肖老师写作逻辑得到的约束

DSDL-I6 到 I9 的关键不是先贴一个理论名，而是让理论先产生期望、体验与 `F-E` 的有方向关系，再使该关系进入张量、损失和预测。由此，drift 的 `A→B` 有向边虽然是结构，却没有 `F-E` 那样可由原理论判断正负的安全方向；不能因“有向”便视为功能同位。

DSDL-M14 到 M23 又显示，理论机制需要逐层承担 Q/K/V 关系、理论中间状态、弱监督方向、联合目标与最终输出的责任。CI 的 flow tuple 可以进入表示，但直接 agent work 已经拥有同一图和标签；匿名 relational model 又能读取同字段。若不能指出额外 forward restriction，理论只是 schema，不是 DSDL 式算法责任。

ACAA 与 DSDL 都用直接近邻的任务对象、数据结构和现有方法责任建立 gap。本文件反向执行同一逻辑：若近邻已经拥有同 unit、label、action 与 outcome，就必须删除 gap，而不是强调应用域差别。零候选因此是严格学习该逻辑的结果。

## 12. 引用、元数据与原文证据核验

### 12.1 Basket 核心来源

| 来源 | 支持的本文件主张 | 原文证据位置/核验状态 |
|---|---|---|
| [Li et al. 2024](https://doi.org/10.17705/1jais.00892) | CI 元组、norm/value、personal privacy norm→disclosure intention、人类调查单位 | 本地主文完整回读；模型、假设、结果与 limitation 已核 |
| [Pentland et al. 2020](https://doi.org/10.25300/misq/2020/14458) | drift 的 `L/M/V/R`、历史矩阵、边形成/消解、phase change、无 external feedback、益害不定 | 本地主文与 Appendix A 完整回读 |
| [Pentland et al. 2021](https://doi.org/10.25300/misq/2021/15360) | directed graph 与 `Δ(V,E)` 的 diachronic measurement、Level 1 分析定位、signal/noise 需理论解释 | 本地主文完整回读 |
| [Burton-Jones & Grange 2013](https://doi.org/10.1287/isre.1120.0444) | effective use 三维构念、user–system–task 单位、层级关系 | 本地主文完整回读 |
| [Strong et al. 2014](https://doi.org/10.17705/1jais.00353) | relational affordance、individual/organizational actualization、affordance dependency | 本地主文完整回读 |
| [Rosenkranz et al. 2014](https://doi.org/10.17705/1jais.00364) | brokering situation、boundary complexity/object capacity、teleological/dialectical motor | 本地主文完整回读 |
| [Benaroch 2018](https://doi.org/10.1287/isre.2017.0714) | proactive mitigation 与 wait/exercise/non-exercise 的原投资单位 | 本地主文完整回读；只用于防止 real-options 泛化 |
| [Salovaara et al. 2019](https://doi.org/10.25300/MISQ/2019/14577) | Digital HRO 分层与人类 pragmatic control | 本地主文完整回读；沿用 01Z 的层级终判 |

### 12.2 技术直接来源

| 来源 | 支持的本文件主张 | 核验状态 |
|---|---|---|
| [CI-Work](https://arxiv.org/abs/2604.21308) | enterprise flows、essential/sensitive set、privacy–utility、trajectory simulator | 论文 HTML 的 abstract、risk model、construction、simulation、metrics、statistics 与实验段已回读；代码链接已定位 |
| [AgentSCOPE](https://arxiv.org/abs/2603.04902) | PFG 五参数、intermediate boundary、62 场景/八领域/per-stage truth | 论文 HTML 的 framework、benchmark 与评价段已回读 |
| [PiSAs](https://arxiv.org/abs/2607.05318) | dual CI annotations、visibility matrix、output/message/memory spillage | 论文 HTML 的 problem、scenario construction、metrics、systems 与 limitations 已回读 |
| [AgentSecBench](https://arxiv.org/abs/2605.26269) | policy projection、noninterference、retrieval confidentiality/capability integrity、benign controls | 论文 HTML 的 formal view、benchmark、defense 与 limitations 已回读 |
| [TACT](https://arxiv.org/abs/2605.05980) | OT/OA/CAL labels、hidden axes、forward hook、splits、coding benchmarks | 论文 HTML 的 method、equations、data/splits、baselines、results 与 limitations 已回读 |
| [SABER](https://arxiv.org/abs/2606.01317) | stateful coding workspace 与 final-state operational harm | 论文正文的 benchmark/task/evidence/outcome 与公开仓库信息已回读 |
| [HINTBench](https://arxiv.org/abs/2604.13954) | intrinsic long-horizon risk detection/localization/type | 论文摘要、任务与数据规模已核；不承担细节性算法撤题 |
| [Tang et al. 2026](https://arxiv.org/abs/2605.29442) | 真实 coding-agent misalignment、developer pushback 与 damage locus | 论文方法、结果、outcome appendix 与 limitation 已回读 |
| [AgentRx](https://www.microsoft.com/en-us/research/publication/agentrx-diagnosing-ai-agent-failures-from-execution-trajectories/) | 115 条失败轨迹与 critical-step diagnosis | 官方论文页与论文方法已回读 |

所有技术工作均按预印本或正式项目的实际状态表述。没有用搜索摘要承担模型细节；只有 HINTBench 在本文件承担数据规模与任务存在性，不承担候选撤题的核心理论责任。

### 12.3 引文强度边界

- 本文件关于“情境完整性候选已经直接覆盖”的判断由至少三项独立 agent CI 全文和一项 formal security benchmark 共同承担，不由 Li 等人的人类调查单独承担。
- 本文件关于“process drift 没有安全方向”的判断直接来自 Pentland 等人对 endogenous/no-feedback、beneficial-or-harmful 的明示边界，并由 2021 年 Level 1 定位加强，不是从 TACT 的存在倒推。
- TACT 的性能数字不用于声称本地能够复现或必然优于新模型；它只证明 drift representation 与 forward intervention 已是直接技术工件。
- 未运行本候选实验，所以本文没有候选性能表、显著性、effect size 或“我们发现”类句子。

## 13. 最终机械审计

### 13.1 文件范围

本任务只允许新建 `02B_从AIS机制反向搜索新题.md`。创建前已确认目标不存在。所有正文写入均通过 `apply_patch` 完成；没有修改 `00A/00B/00E/00F/00W`、目标博士论文、肖老师全文或任何既有终审文件。

### 13.2 内容机械门

- 保留候选计数固定为 `0`，文件中没有伪造 CONDITIONAL 题。
- 两个最强机制均包含 MEC→MAP→ALG、I/O、张量、监督、loss、推断动作、checkpoint、算力、splits、leakage、外部结果、coding-agent 删除与 equal-parameter generic 反证。
- 所有 C3 与主动缓解期权格的中心动作边界已经单独核对。
- 所有句段审计行同时含 `source_function_code`、`candidate_function_code`、完整链与五类编辑动作。
- 正式实验未运行，未写候选实证结果。
- 最终 SHA-256 不写入文件自身，避免 self-hash 不动点；由交付回执报告。

### 13.3 终局状态

**AIS 机制反向搜索完成。新题数 0；两条最强线均终局 NO-GO。**
