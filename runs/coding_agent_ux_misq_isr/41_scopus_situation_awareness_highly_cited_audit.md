# Scopus 检索：Situation Awareness 的主流含义与高引经典文献

本文件记录 2026-07-09 在 Scopus 中对 `situation awareness` / `situational awareness` 的精确短语检索结果。检索字段使用 Scopus 的 `Article title, Abstract, Keywords` 和更严格的 `Article title` 两种口径；排序使用 `Cited by (highest)`。

## 检索口径

- 数据库：Scopus Documents Search
- 检索方式：精确短语，使用双引号
- 字段口径 1：`Article title, Abstract, Keywords`
- 字段口径 2：`Article title`
- 排序：`Cited by (highest)`
- 说明：Scopus 页面显示结果列表为前 2000 条可浏览记录，但总命中数高于 2000 时仍显示总数。

## 命中量

| 检索词 | 字段 | Scopus 命中量 |
| --- | --- | ---: |
| `"situation awareness"` | Article title, Abstract, Keywords | 11,385 |
| `"situational awareness"` | Article title, Abstract, Keywords | 20,198 |
| `"situation awareness"` | Article title | 3,397 |
| `"situational awareness"` | Article title | 3,030 |

## 先说结论：它到底是在做什么

Scopus 高引结果显示，`situation awareness` 的核心传统来自 human factors / cognitive engineering，主要研究人在动态、复杂、高风险系统中如何保持对当前情境的正确理解，并据此作出及时决策。这个传统最核心的问题不是“用户喜不喜欢系统”，也不是一般的“信任系统”，而是：

- 人是否注意到关键状态、事件和变化；
- 人是否理解这些状态对当前目标意味着什么；
- 人是否能预测状态接下来会如何发展；
- 系统设计、自动化程度、工作负荷、压力、复杂性、显示界面和训练如何影响这种觉察；
- 一旦觉察下降，人是否会出现 out-of-the-loop、接管困难、判断变慢、错误增加等问题；
- 如何用 SAGAT、SART、行为测量、生理测量、眼动或任务中断查询等方法测量它。

也就是说，SA 的经典对象是“动态系统中的操作者认知状态”。它后来被大量迁移到不同应用：团队协作、航空/驾驶/麻醉、网络安全、应急管理、社交媒体危机信息抽取、IoT、电网、自动驾驶、自治船舶等。

对我们来说，最关键的一点是：SA 在经典文献里已经被视为一个可定义、可测量、可被系统设计影响、并能解释行为表现的构念。这非常适合作为 coding agent UX 概念开发的基础概念。但是，不能照搬，因为 coding agent 情境中的“situation”不是外部物理环境或仪表盘指标，而是 agent 正在改变代码库、调用工具、推进任务、产生风险和未来影响的动态任务状态。

## `"situation awareness"`：标题+摘要+关键词，高引前列

这个口径会包含真正的 SA 核心文献，也会包含一些只是摘要中提到 SA 的高引跨领域论文。

| 排名 | 文献 | 年份 | 来源 | Scopus 被引 | 判断 |
| ---: | --- | ---: | --- | ---: | --- |
| 1 | Endsley, `Toward a theory of situation awareness in dynamic systems` | 1995 | Human Factors | 7,400 | 核心经典；SA 理论模型 |
| 2 | Dey, `Understanding and using context` | 2001 | Personal and Ubiquitous Computing | 4,132 | context-aware computing 经典；不是 SA 核心文献 |
| 3 | Endsley, `Measurement of situation awareness in dynamic systems` | 1995 | Human Factors | 1,686 | 核心经典；SA 测量 |
| 4 | Endsley & Kiris, `The out-of-the-loop performance problem and level of control in automation` | 1995 | Human Factors | 1,131 | 核心经典；自动化导致 SA 下降和接管问题 |
| 5 | Edgar et al., `Principles and prospects for single-pixel imaging` | 2019 | Nature Photonics | 1,013 | 光学成像综述；SA 只是应用场景 |
| 6 | Gutwin & Greenberg, `A descriptive framework of workspace awareness for real-time groupware` | 2002 | CSCW | 959 | workspace awareness 经典；邻近概念，不是 SA 主线 |
| 7 | Endsley & Kaber, `Level of automation effects on performance, situation awareness and workload in a dynamic control task` | 1999 | Ergonomics | 909 | 核心；自动化水平、SA、工作负荷、表现 |
| 8 | Endsley, `Situation Awareness Global Assessment Technique (SAGAT)` | 1988 | NAECON Proceedings | 879 | 核心；SAGAT 测量方法 |
| 9 | Fletcher et al., `Anaesthetists' non-technical skills (ANTS)` | 2003 | British Journal of Anaesthesia | 824 | 医疗非技术技能；SA 是技能维度之一 |
| 10 | Endsley, `From Here to Autonomy` | 2017 | Human Factors | 777 | 核心；自动化/自治系统监督与 SA |

这个列表说明：如果不限制标题，Scopus 的高引结果会混入 context-aware computing、workspace awareness、single-pixel imaging 等邻近或应用性文献。它们有参考价值，但不应误认为 SA 概念本身的经典根基。

## `"situation awareness"`：只检索标题，高引经典更清晰

| 排名 | 文献 | 年份 | 来源 | Scopus 被引 | 主要贡献 |
| ---: | --- | ---: | --- | ---: | --- |
| 1 | Endsley, `Toward a theory of situation awareness in dynamic systems` | 1995 | Human Factors | 7,400 | 建立 SA 作为动态系统中人类决策的理论模型，讨论注意、工作记忆、心理模型、目标导向行为、工作负荷、压力、系统复杂性、自动化和设计特征如何影响 SA。 |
| 2 | Endsley, `Measurement of situation awareness in dynamic systems` | 1995 | Human Factors | 1,686 | 系统讨论 SA 的经验测量方法，重点验证任务中断后查询操作者 SA 的方法，即 SAGAT 类思路。 |
| 3 | Endsley & Kaber, `Level of automation effects on performance, situation awareness and workload in a dynamic control task` | 1999 | Ergonomics | 909 | 研究不同自动化水平如何影响表现、SA 和工作负荷，说明自动化不是越高越好，人的参与方式会影响 SA 和失败后的恢复。 |
| 4 | Endsley, `Situation Awareness Global Assessment Technique (SAGAT)` | 1988 | NAECON Proceedings | 879 | 提出 SAGAT，目标是为飞行员/驾驶舱界面设计提供客观 SA 测量。 |
| 5 | Kaber & Endsley, `The effects of level of automation and adaptive automation on human performance, situation awareness and workload in a dynamic control task` | 2004 | Theoretical Issues in Ergonomics Science | 677 | 进一步研究人本自动化、自动化水平和 adaptive automation 对 SA、表现和工作负荷的影响。 |
| 6 | de Winter et al., `Effects of adaptive cruise control and highly automated driving on workload and situation awareness` | 2014 | Transportation Research Part F | 656 | 自动驾驶/辅助驾驶综述；高度自动化可能降低工作负荷，但若用户转向非驾驶任务，SA 会恶化。 |
| 7 | Parasuraman, Sheridan & Wickens, `Situation Awareness, Mental Workload, and Trust in Automation` | 2008 | Journal of Cognitive Engineering and Decision Making | 626 | 明确把 SA、mental workload、trust in automation 当作可操作化且彼此不同的认知工程构念。 |
| 8 | Yin et al., `Using social media to enhance emergency situation awareness` | 2012 | IEEE Intelligent Systems | 541 | 用 NLP 和数据挖掘从灾害/危机 Twitter 消息中抽取 SA 信息。 |
| 9 | Salas et al., `Situation awareness in team performance` | 1995 | Human Factors | 517 | 把 SA 从个体拓展到团队表现、测量和训练。 |
| 10 | Endsley, `Situation awareness misconceptions and misunderstandings` | 2015 | Journal of Cognitive Engineering and Decision Making | 515 | 回应对 Endsley 模型的批评，并比较 individual/team SA、distributed SA、sensemaking 等模型。 |

严格标题检索说明，真正的高引经典集中在四条主线：

1. SA 理论定义：动态系统中的人类决策和情境理解。
2. SA 测量：SAGAT、SART、主观/客观/行为/生理等方法。
3. 自动化与 out-of-the-loop：自动化提高表现的同时可能降低操作者 SA。
4. 团队和应用扩展：团队 SA、驾驶、医疗、应急社媒、网络安全等。

## `"situational awareness"`：标题+摘要+关键词，高引前列

这个词形在 Scopus 中更偏应用化，很多高引论文把它当作某个领域的信息处理或监测目标。

| 排名 | 文献 | 年份 | 来源 | Scopus 被引 | 判断 |
| ---: | --- | ---: | --- | ---: | --- |
| 1 | Vieweg et al., `Microblogging during two natural hazards events` | 2010 | CHI Proceedings | 1,226 | 应急社媒；Twitter 信息如何贡献危机 SA |
| 2 | Borghini et al., `Measuring neurophysiological signals in aircraft pilots and car drivers` | 2014 | Neuroscience and Biobehavioral Reviews | 1,204 | 驾驶/飞行员工作负荷、疲劳、困倦与 SA 的生理测量 |
| 3 | Choi et al., `Consensus-based decentralized auctions for robust task allocation` | 2009 | IEEE Transactions on Robotics | 1,064 | 多自主体任务分配；SA 指 fleet 中情境信息一致性 |
| 4 | Wang et al., `Research on Resilience of Power Systems under Natural Disasters` | 2016 | IEEE Transactions on Power Systems | 1,062 | 电力系统灾害韧性；SA 是监测与恢复能力 |
| 5 | Benjamin et al., `The Rapid Refresh` | 2016 | Monthly Weather Review | 1,021 | 天气同化与预报系统；SA 是实时决策支持目标 |
| 6 | Neshenko et al., `Demystifying IoT Security` | 2019 | IEEE Communications Surveys and Tutorials | 766 | IoT 安全；SA 是运营网络安全能力 |
| 7 | Bedi et al., `Review of Internet of Things in Electric Power and Energy Systems` | 2018 | IEEE Internet of Things Journal | 755 | IoT+能源系统；SA 是实时监测和智能控制能力 |
| 8 | Imran et al., `Processing social media messages in Mass Emergency` | 2016 | ACM Computing Surveys | 741 | 大规模应急社媒处理；研究从 SA 信息抽取走向决策和响应支持 |
| 9 | Pallotta et al., `Vessel pattern knowledge discovery from AIS data` | 2013 | Entropy | 659 | 海事 SA；从 AIS 数据中发现模式、检测异常、预测路线 |

这说明 `situational awareness` 更容易指向“某领域中的信息抽取/监测/态势图景”，而不是严格的人因构念。

## `"situational awareness"`：只检索标题，高引应用文献

| 排名 | 文献 | 年份 | 来源 | Scopus 被引 | 主要贡献 |
| ---: | --- | ---: | --- | ---: | --- |
| 1 | Vieweg et al., `Microblogging during two natural hazards events` | 2010 | CHI Proceedings | 1,226 | 分析自然灾害中的 Twitter 现场信息，识别哪些内容可贡献 emergency SA。 |
| 2 | Stanton et al., `Situational awareness and safety` | 2001 | Safety Science | 401 | 把 SA 应用于 safety-critical domains，比较 three-level model、interactive sub-systems approach、perceptual cycle 等理论。 |
| 3 | MacEachren et al., `SensePlace2` | 2011 | IEEE VAST | 323 | 地理可视分析系统，用 GeoTwitter 支持危机管理和决策领域的 SA。 |
| 4 | Verma et al., `Natural Language Processing to the Rescue?` | 2011 | ICWSM | 299 | 用 NLP 识别大规模应急中的 situational-awareness tweets。 |
| 5 | Franke & Brynielsson, `Cyber situational awareness` | 2014 | Computers and Security | 289 | cyber SA 系统综述，梳理网络安全领域的 SA 文献。 |
| 6 | Thombre et al., `Sensors and AI Techniques for Situational Awareness in Autonomous Ships` | 2022 | IEEE T-ITS | 261 | 自治船舶中的传感器融合和 AI 感知系统综述。 |
| 7 | Huang & Xiao, `Geographic situational awareness` | 2015 | ISPRS IJGI | 258 | 将灾害社媒信息分类到灾害管理阶段，支持应急管理者识别阶段转移。 |
| 8 | Kirschbaum & Stanley, `Satellite-Based Assessment of Rainfall-Triggered Landslide Hazard` | 2018 | Earth's Future | 247 | 近实时滑坡风险评估，用于灾害 SA。 |
| 9 | Lakkaraju et al., `NVisionIP` | 2004 | VizSEC/DMSEC Workshop | 227 | 用 NetFlow 可视化网络状态，提升安全分析师的 cyber SA。 |
| 10 | Taylor, `Situational Awareness Rating Technique (SART)` | 2017 | Book chapter | 225 | SART 主观测量工具；Scopus 中显示为 2017 章节记录，但理论源头更早。 |

## 对 coding agent 概念开发的意义

Scopus 检索支持以下判断：

1. `situation awareness` 可以作为基础概念，因为它有高引理论、测量方法、前因/后果研究和自动化场景。
2. 最适合我们对话的不是应急社媒或 cyber SA 应用文献，而是 Endsley 的动态系统传统、自动化/out-of-the-loop 文献，以及 Parasuraman/Sheridan/Wickens 对 SA、工作负荷、trust in automation 的区分。
3. `workspace awareness` 可以作为邻近概念，但 Scopus 高引列表显示它更偏 groupware 中对他人行动和共享空间的 awareness；它不是 SA 主线，也不是 coding agent 情境最稳的基础概念。
4. `situational awareness` 在应用文献中常被用作“信息抽取/监测/态势图景”的目标，特别是危机、灾害、网络安全、IoT、电网和海事。这些应用能帮我们想设计场景，但不适合作为个体 UX 构念的唯一理论根基。
5. 对 coding agent 而言，最自然的迁移方式是从“动态系统中的操作者 SA”转到“编程代理任务中的用户 task-state awareness”。用户需要感知 agent 已经做了什么，理解这些行动对代码库和任务目标意味着什么，并预测继续批准、暂停、回滚或介入会造成什么影响。

## 推荐后续引用主线

如果论文要写概念开发，建议优先围绕以下文献建理论背景：

- Endsley 1995 `Toward a theory of situation awareness in dynamic systems`：基础定义和模型。
- Endsley 1995 `Measurement of situation awareness in dynamic systems`：测量合法性和方法。
- Endsley 1988 `SAGAT`：经典客观测量技术。
- Endsley & Kiris 1995 `The out-of-the-loop performance problem and level of control in automation`：自动化导致 SA 下降与接管问题。
- Endsley & Kaber 1999 / Kaber & Endsley 2004：自动化水平、adaptive automation、SA、工作负荷、表现。
- Parasuraman, Sheridan & Wickens 2008：SA、mental workload、trust in automation 是不同但相关的构念。
- Endsley 2017 `From Here to Autonomy`：自治系统监督中的 automation conundrum。
- Salas et al. 1995：如果未来考虑人-agent-team 或团队开发场景，可补充 team SA。
- Stanton et al. 2001：如果需要讨论不同 SA 理论传统，可补充 safety/three-level/perceptual-cycle 对照。

## 暂定概念判断

基于本次 Scopus 检索，我建议不要把我们的构念叫成宽泛的 `situational awareness`，因为这个词在应用文献中已经非常泛化，容易落到“信息监测/态势图”的工程目标。更好的做法是：

- 基础概念：situation awareness
- 迁移对象：coding agent 使用情境
- 新概念方向：coding-agent task-state awareness
- 核心差异：coding agent 的 situation 不是外部环境，而是 agent-mediated code task state，包括 agent 行动、代码变更、工具运行、任务进展、风险证据和未来影响。

这样写的好处是，既能借助 SA 高引经典文献的理论和测量基础，又能清楚说明为什么 coding agent 情境需要开发新的、更具体的 individual-level UX 构念。
