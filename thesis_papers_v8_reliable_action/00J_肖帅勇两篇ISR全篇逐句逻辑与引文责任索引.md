# 肖帅勇两篇 ISR 全篇逐句逻辑与引文责任索引

## 1. 文件用途与覆盖边界

本文件逐段记录肖帅勇老师两篇 ISR 主文从摘要到结论的句子功能、句间关系和引文责任。它与 `00C_肖帅勇两篇ISR写作结构图.md` 的分工不同。`00C` 解释两篇论文的整体节奏和理论—算法闭环，本文件负责防止正式写作时只对照段落标题而忽略句子怎样推进、引文怎样承担论证。

句子功能沿用 `00F_逐段双ISR写作与引用审计协议.md` 的代码。引文责任分为事实背景、经验关系、理论机制、方法能力、研究边界和结果解释。这里只释义原文的学术功能，不复制原句。源文件中的每个正文行通常对应一个排版段落；公式、图题、表格和算法步骤另作论证单元处理。每个逻辑段的源行集合和语法句主键由 `00W_肖帅勇两篇ISR源行句段主键Manifest.md` 统一冻结；一个语法句中的多个功能分句用 `a/b` 区分，不改变原句计数。

当前完成状态如下。状态为“已索引”只表示本文件已完成逐句功能和引文责任分析，不表示在线附录已经获得。

| 论文 | 部分 | 状态 |
|---|---|---|
| ACAA | 摘要、引言、文献综述、理论与设计理由 | 已索引 |
| ACAA | 方法 | 已索引 |
| ACAA | 经验评价、贡献、结论 | 已在 `00M_ACAA实证贡献与结论逐句逻辑索引.md` 完成逐句索引 |
| ACAA | 尾注 1–12 | 本文第 8 节已按 12 个编号、17 个语法句完成功能与引文责任索引 |
| ACAA | Figure 1–7 图像、在线附录 A–I | 本地缺失，已记录每个图形接口与附录出口，不声称视觉核验或附录阅读 |
| DSDL | 摘要至结论、尾注 | 已在 `00K_DSDL全篇逐句逻辑与引文责任索引.md` 完成全篇逐句索引 |
| DSDL | 在线附录 A–I、Figure 1–3 图像 | 本地缺失，已记录证据边界，不声称阅读或视觉核验 |

## 2. ACAA 摘要

### ACAA-A0，原文第 29 行

| 句号 | 功能 | 与前句关系 | 引文或证据责任 |
|---|---|---|---|
| S1 | ACK+LIM | 先承认 helpful review 研究，再限定其常用测量停留在 review-level quantitative indicators | 摘要不列引文；责任在正文第 2.1 节由 helpfulness 文献承担 |
| S2 | MEC+LIM | 解释简单指标为什么未必带来准确预测，提出信息质量、需求和产品属性持续变化 | 摘要不列引文；正文由异质偏好与动态效应文献支撑 |
| S3 | MEC+GAP | 用“更受注意的评论更影响购买与销售”把测量限制转成替代机制 | 属于研究立场，后由信息处理理论与经验文献展开 |
| S4 | MAP | 把 customer attention 分解到四个粒度，并给出四个可计算指标 | 这是本文概念化，不借既有文献替代原创责任 |
| S5 | ALG | 将四个指标落实为专门设计的 neural attention artifact | 是方法承诺，后文公式与算法承担可复现责任 |
| S6 | RES | 交代大样本酒店销售情境、两个评价层面和相对强基线结果 | 只回报本文经验结果，不借外部引用支撑 |

句序为“已知研究—测量限制—替代机制—概念状态—算法工件—累积证据”。摘要没有先说模型结构，也没有把经验结果写成单一准确率。

## 3. ACAA 引言

### ACAA-I1，原文第 39 行

句序是“信息渠道—购买影响—销售预测机会—组织价值—相对传统数据的新视角”。

| 句号 | 功能 | 逻辑推进 | 引文责任 |
|---|---|---|---|
| S1 | CXT | 建立 reviews 连接顾客与产品的日常信息情境 | Yin et al. 2014 支撑评论作为信息渠道 |
| S2 | IMP | 把信息渠道推进为购买意愿后果 | Forman et al. 2008 与 Li et al. 2019 支撑评论影响购买意愿 |
| S3 | GAP | 由购买影响导出预测未来销售的机会 | Zhu and Zhang 2010 支撑评论与销售关系，不承担本文方法有效性 |
| S4 | IMP | 说明 sales prediction 对运营配置与价值创造的重要性 | Yu et al. 2012 支撑运营研究与实践价值 |
| S5 | LIM+CXT | 对比产品内部和市场环境变量，说明评论带来顾客需求视角 | Tsoumakas 2019 界定传统预测特征；句子自身完成相对定位 |

### ACAA-I2，原文第 41 行

句序是“看似直接的全量输入—有限注意造成偏差—承认已有预测尝试—数据使用不足—未用语义与图像—模型等权处理”。同一个 limited-attention 机制把数据和模型缺陷连接起来。

| 句号 | 功能 | 逻辑推进 | 引文责任 |
|---|---|---|---|
| S1 | ACK | 由既有 review–sales 关系构造最直接的全量输入方案 | Chevalier and Mayzlin 2006、Forman et al. 2008、Zhu and Zhang 2010、van Nguyen et al. 2020 共同证明关系已知，不证明全量输入最优 |
| S2 | MEC+LIM | 有限注意意味着只有少量评论被感知和内化，因此全量输入会偏离真实处理 | Li and Hitt 2008、Moe and Schweidel 2012 支撑选择性处理；Qahri-Saremi and Montazemi 2019 支撑无用评论存在 |
| S3 | ACK+LIM | 承认已有 review-based sales prediction，再转入其适用边界 | Yu et al. 2012、van Nguyen et al. 2020 证明直接工作存在 |
| S4 | LIM | 将第一类边界收束为把非结构化评论量化使用 | 这是对前述方法的归纳，需要由被评述原文而非综述标签承担 |
| S5 | ACK+GAP | 已研究 valence、extremity、votes，但文本语义和图像预测价值不足 | Sahoo et al. 2018 支撑已研究变量；“不足”由后续综述和比较表承担 |
| S6 | LIM | 第二类边界是模型未有效区分评论 | 本文的问题诊断，后续 attention 文献与 compatibility-function 分析必须闭合 |

### ACAA-I3，原文第 43 行

| 句号 | 功能 | 逻辑推进 | 引文责任 |
|---|---|---|---|
| S1 | MEC | 把销售结果重新锚定于购买意愿及评论传递的经验和意见 | Sahoo et al. 2018 支撑购买意愿与评论信息的关系 |
| S2 | MEC | 加入“评论被认真阅读”这一必要处理条件 | 本句是行为机制推论，后续 limited-attention 和信息处理理论承担支撑 |
| S3 | MEC | 将处理强度转成评论对购买与销售的相对预测力 | 理论预期，不以经验结果口吻出现 |
| S4 | GAP | 把机制收束为两项可研究问题：什么评论获注意、是否更能预测 | 无新增引文；由前三句推出 |

### ACAA-I4，原文第 45 行

句序是“既有构念—共识—承认诊断价值—异质偏好边界—同内容可被相反评价—经验冲突”。它没有因为提出 customer attention 就否定 helpfulness 文献。

| 句号 | 功能 | 引文责任 |
|---|---|---|
| S1 | ACK | Wang and Strong 1996、Liu et al. 2020、Forman et al. 2008 分别界定 information quality、argument quality、review helpfulness 三条传统路径 |
| S2 | ACK | Filieri et al. 2018、Yin et al. 2020 支撑 helpfulness 与感知质量及购买意愿的共识 |
| S3 | ACK+LIM | Filieri 2015 支撑 content indicators 的诊断价值；后半句只限定其对整个顾客群注意的稳定性 |
| S4 | MEC | Moe and Schweidel 2012 支撑偏好异质性，解释为何内容风格不能稳定吸引注意 |
| S5 | MEC | 将异质偏好具体化为同一内容的差异评价；不另加装饰性引文 |
| S6 | CON | Lee et al. 2008 与 Berger et al. 2010 支撑负面评论的相反销售效应；Fink et al. 2018 支撑长度与 helpfulness 的相反关系 |

### ACAA-I5，原文第 47 行

| 句号 | 功能 | 逻辑推进 | 引文责任 |
|---|---|---|---|
| S1 | MAP | 用 temporal 与 spatial 两维组织浏览行为 | 属于本文框架起点 |
| S2 | MAP | 说明两维共同描述阶段和粒度迁移 | 解释上句的结构作用 |
| S3 | MEC | 从过程维引入 message learning 与 information processing | Riley 1954、McGuire 1968 负责两阶段信息处理理论来源 |
| S4 | DEF | 明确定义 reception 与 yielding | Kuan et al. 2015 等后续文献帮助情境化，但定义责任主要来自理论原文 |
| S5 | ACK+LIM | 承认 content-based helpfulness 解释 yielding，却未解释 reception | Weathers et al. 2015 支撑 yielding；Kuan et al. 2015 支撑 diagnosticity 评价 |
| S6 | MEC | 在评论过载下否定对全部评论逐一诊断的现实性 | 是 limited-attention 机制推论 |
| S7 | MEC | 将选择性处理具体化为只注意子集 | 与 S6 因果展开 |
| S8 | ACK | 用读者不会遍历全部评论的发现校验机制 | Kuan et al. 2015 提供直接经验支撑 |
| S9 | GAP | 导出 reception attention 必须进入 sales prediction | 由 S3–S8 推出，不再堆新引用 |

### ACAA-I6，原文第 49 行

| 句号 | 功能 | 逻辑推进 | 引文责任 |
|---|---|---|---|
| S1 | MAP | 从空间维提出 review set、subset、review、element 四层 | 本文概念化 |
| S2 | CXT | 用 top-down 浏览示例说明全层下钻 | 情境说明，不需借引文制造权威 |
| S3 | CXT+CON | 用 bottom-up 示例说明路径不只有单向下钻 | 形成与 S2 的互补情境 |
| S4 | RQ | 将 process–granularity 框架收束为 RQ1 | 前三句已经给足问题结构后才提出 RQ |

### ACAA-I7，原文第 51 行

| 句号 | 功能 | 引文责任 |
|---|---|---|
| S1 | MAP | 总览四层与四种 attention indicator 的对应关系 |
| S2 | MEC+MAP | Groves and Thompson 1970 支撑 dual-process，引出 holistic-set 层的动态 timeliness |
| S3 | MEC+MAP | Li and Hitt 2008、Moe and Schweidel 2012 支撑 selection effect 与偏好异质性，引出 topic-level diversity |
| S4 | ACK+MAP | Mudambi and Schuff 2010、Kuan et al. 2015、Salehan and Kim 2016 支撑 helpfulness votes 的普遍性与注意作用 |
| S5 | CXT+MAP | 说明单条评论含文本和图像，建立 element-level interaction 对象 |
| S6 | MEC+MAP | Petty and Cacioppo 1986 提供 elaboration likelihood 机制，引出文本与图像非对称注意 |

### ACAA-I8，原文第 53 行

| 句号 | 功能 | 逻辑推进 | 引文责任 |
|---|---|---|---|
| S1 | MAP | 回收四个指标，防止 RQ2 引入新构念 | 本文概念化 |
| S2 | RQ | 以 multimodal reviews 的现实普及导出如何利用 customer attention | 普及性由尾注来源承担；RQ 由前文推导 |
| S3 | ALG | 首次命名 DTV-AMI，并限定到 multimodal review sales prediction | 工件在机制与 RQ 后出现 |
| S4 | ALG | 将工件拆为 DTV 与 AMI，并使四种机制各有归属 | 方法责任，后续公式必须逐项兑现 |

### ACAA-I9，原文第 55 行

| 句号 | 功能 | 逻辑推进 | 引文责任 |
|---|---|---|---|
| S1 | ALG | 先概括 DTV 应突出 timely、diverse、voted reviews | 回应 I7 的三项指标 |
| S2 | ALG+MEC | 用顾客陆续到达说明为何每个 review point 都可能是起点 | 情境机制决定递归扫描方式 |
| S3 | ALG | 重申动态扫描中的三种权重行为 | 与 S1–S2 合并为 DTV 的推断动作 |
| S4 | ALG | 说明 AMI 在每个 review point 学习 text–image tradeoff | 回应 element-level 理论机制 |
| S5 | CONB | 回收 DTV-AMI 如何让 multimodal reviews 发挥预测力 | 不增加新功能 |
| S6 | RES | 交代酒店数、文本数、图像数、相对基线结论及其理论解释 | 全部是本文运行结果；不能由外部引文替代 |

## 4. ACAA 文献综述

### ACAA-L1，原文第 61 行

句序是“reviews 为什么影响销售—信息质量异质性限定—helpfulness 作为中介—helpfulness 的感知定义—对需求与销售的预期后果”。Wang and Strong 1996、Kang and Zhou 2017 支撑 product-specific opinions 对购买的作用；Mudambi and Schuff 2010 支撑质量异质性；Filieri et al. 2018 支撑 helpfulness 的中介地位；Yin et al. 2014 界定 helpfulness；Berger et al. 2010、Sahoo et al. 2018 支撑销售后果。引用沿着因果链分工，没有一串来源共同装饰同一个宽泛判断。

### ACAA-L2，原文第 63 行

S1 用 Mudambi and Schuff 2010、Kuan et al. 2015、Lee et al. 2018、Ma et al. 2018 划定 determinants 与 prediction 两类 helpfulness 研究。S2 用 Forman et al. 2008 说明 source credibility、helpfulness 与 sales 的正向关系。S3 用 Zhu and Zhang 2010 引入产品与顾客特征的调节，直接削弱简单 helpfulness 指标的普适性。S4 用 Kuan et al. 2015 给出 voted reviews 诊断价值高却与销售负相关的冲突。段落从研究规模推进到两条与朴素指标不一致的证据，为后文 customer attention 留出空间。

### ACAA-L3，原文第 65 行

S1 以 Buschken and Allenby 2016 说明文本能承载属性—偏好匹配。S2 以 Sahoo et al. 2018 说明评分接近时文本价值更强。S3 同样引用 Sahoo et al. 2018，但作用变为说明既有研究仍把文本量化成长短和 helpful fraction。S4 用 Berger et al. 2010 说明负面文本通过提高 awareness 也可增加购买。S5 用 Archak et al. 2011 将文本相对 numeric indicators 的选择解释力收束出来。段落既证明文本有价值，又同步展示既有利用方式的限制。

### ACAA-L4，原文第 67 行

S1 以 Li and Xie 2020 概括图像的信息、美学和自我呈现价值。S2 用 Zhang and Mao 2012 把一般图像价值落到产品评价。S3 的 Karimi and Wang 2017 研究 profile images，作用只是说明视觉装饰影响 helpfulness。S4 的 Ma et al. 2018 转向 customer-generated images 的 helpfulness 价值。S5 沿用 Ma et al. 2018 给出 image-only cues 不充分的边界。S6 用 Wu et al. 2021 表明 images 增加诊断性且 hybrid reviews 优于 text-only，由此自然导向 multimodal interaction，而非简单宣称图像越多越好。

### ACAA-L5，原文第 71 行

S1 以 Tsoumakas 2019 界定 retailer 与 macro-market 传统特征。S2 用 Wu and Brynjolfsson 2015 指出这些变量只能间接且不稳定地反映需求。S3 由 reviews 的诊断价值提出顾客需求视角。S4–S6 分别用 Yu et al. 2010、Chen et al. 2017、Archak et al. 2011 证明评论质量与情感、文本相对评分、属性偏好学习能够提高销售解释与预测。段落的引用顺序完成“传统数据边界—替代数据机制—三条经验支持”。

### ACAA-L6，原文第 73 行

Zhao et al. 2019 支撑文本可预测 customer-base satisfaction；van Nguyen et al. 2020 支撑 sentiment 与 votes 的 demand prediction；Li et al. 2019 同时支撑 numeric 和 text 的有效性，并进一步支撑二者交互；Lee and Choeh 2020 支撑 helpfulness 的 moderation。该段扩展 reviews 可进入模型的变量和交互，却仍主要描述已有研究已经做到什么。

### ACAA-L7，原文第 75 行

S1 把综述转向动态效应。Scholz et al. 2018 支撑 user-generated content 效应会随新内容变化及相应层级模型；Lu et al. 2018 支撑 review characteristics 的 helpfulness 效应随时间变化；Yu et al. 2012 支撑 sales prediction 中使用 time series。段落承认 temporal modeling 已存在，避免把“动态”本身冒充本文创新。

### ACAA-L8，原文第 79 行

S1–S3 用 Vaswani et al. 2017、Chaudhari et al. 2019、Bahdanau et al. 2014、Xu et al. 2015 建立 attention 的领域普及、历史来源和加权定义。S4 把一般机制连接到 RQ2。S5–S6 用 Galassi et al. 2019 说明从输入中选择任务相关部分，并类比选择性浏览。S7–S8 说明 attention weight 的可解释用途，Graves et al. 2014、Vaswani et al. 2017、Bahdanau et al. 2014 仅负责列举 compatibility functions。S9 由选择能力与可解释性导出专门设计的可能。这里的类比尚不是理论证明，真正的 incompatibility 留到研究缺口与第 3 节完成。

### ACAA-L9，原文第 81 行

Li et al. 2018 支撑 attention 对 stream sequence 在空间、时间和语义局部依赖上的能力与效率。随后两句把该能力收束为本情境的可行方法，并明确 customer attention 与 neural attention 不同。最后一句限定前者只是后者的设计动机，从而避免用同名术语制造虚假的理论等价。

### ACAA-L10，原文第 85 行

S1 是综述收束句。S2 用 Forman et al. 2008、Berger et al. 2010、Kuan et al. 2015 承认 reviews 与 sales 的潜力，再指出 unstructured text 和尤其 images 的预测仍不足。S3 指出现有方法把文本量化且不区分评论。S4 用 Liu et al. 2019 承认 review-content causal effects 已被拆解，再把缺口限定为 richer multimodal information 的利用。S5 把比较表作为缺口证据接口。两个 gap 分别对应数据表示与评论差异化，尚未涉及新 attention calculation。

### ACAA-L11，原文第 87 行

S1 提出第三个、也是最直接的算法缺口：既有 compatibility functions 与理论指标不相容。S2 用 Graves et al. 2014、Luong et al. 2015 说明 affinity-based functions 会偏好与 query 高相关的 keys。S3 由该计算倾向推出无法按顾客接收和处理方式使用评论。S4 规定 semantic diversity 需要突出 nonredundant、complementary keys；S5 规定 timeliness 与 voting 需要提高近期和有票评论权重；S6 规定 multimodal interaction 需要 review-specific text–image tradeoff；S7 回收这些要求是 DTV-AMI 的设计科学贡献；S8 用 appendix comparison 承担直接方法差异核验。该段最值得模仿之处是指出通用算法会朝哪个方向算错，再逐项导出专用计算动作。

## 5. ACAA 理论、设计理由与方法挑战

### ACAA-T1，原文第 91 行

S1 重申研究目标。S2 用 Hevner et al. 2004 定位 design science paradigm，并以 Gregor and Hevner 2013 说明 design rationale 对 artifact design/evaluation 和贡献成立的重要性。S3 声明四个指标源于 process–granularity framework。S4 提出本节的三项责任：指标怎样导出、为何足以代表注意、怎样指导机制设计。该段相当于理论节的验收合同，后续每个机制必须完成三项而非只给定义。

### ACAA-T2，原文第 93 行

S1 用图概括 process 与 granularity 两维。S2 依据 Riley 1954 与 McGuire 1968 建立 reception 和 yielding 两阶段，并以 Kuan et al. 2015 将其情境化到 review processing。S3 把本研究责任限定到 reception attention 对选择真正影响购买意愿的评论之作用。理论引用负责阶段机制，本文负责研究边界。

#### ACAA-F1，Figure 1 论证接口（L97–98）

Figure 1 的学术责任是把 T2 的 reception/yielding 过程维与 T3 的 set–subset–review–element 粒度维组成一张设计理由图，使四个 attention indicators 能被定位到具体浏览节点。源文 L97 仅保留图题，L98 仅保留 API 附件路径；文件头为 `images_downloaded: false`。因此，可以核对正文赋予该图的导航任务，不能声称检查了图中的轴、层级、箭头、标签或空间对应。

### ACAA-T3，原文第 95 行

七句依次沿真实界面路径建立 holistic set、recent temporal subset、topic subset、single review、text/image element，再说明这些选择发生在细读内容之前。段内没有外部引用，责任是把抽象 granularity 变成可观察工作流，而非再堆概念来源。最后一句“largely content free”直接为下一段排除 content-based indicators 提供接口。

### ACAA-T4，原文第 100 行

S1 用 Wang and Strong 1996、Liu et al. 2020、Wang et al. 2021 承认 yielding-stage content indicators 的丰富积累。S2 以偏好异质性解释为何本文转向 reception-stage content-free attention。S3 将异质性具体成长度、效价、主客观等相反风格。S4 指出无法稳定认定某种内容风格总获注意。S5 说明 content-free indicators 可在统一 attention framework 中定位 influential reviews。S6 保留标准 deep learning 对内容本身的处理责任，避免把 reception 机制扩张为全能解释。末句引出四组“理论机制—算法选择”。

<a id="acaa-t5ab"></a>

### ACAA-T5a/T5b，原文第 102、104 行

第 102 行先用 Groves and Thompson 1970 区分快速自动与缓慢有意识过程，Luo et al. 2018 提供简单环境线索例子，Wixted 2007 支撑认知阈值；随后把旧评论与新评论置于不同处理机会，导出 timeliness indicator。第 104 行不再重复理论，而依次规定每个 review point 可作 query、需要 global matching、utility 随时间衰减、权重需随 chronological order 更新，最后给出“近期权重大、随时间衰减”的专用动作。两段形成严格的 MEC→MAP→ALG 配对。

<a id="acaa-t6ab"></a>

### ACAA-T6a/T6b，原文第 106、108 行

第 106 行以 Li and Hitt 2008 支撑 posting/reading selection effect，以 Moe and Schweidel 2012 支撑 preference differentiation；再沿“作者各强调不同属性—读者各取所需—群体共同突出互补评论”导出 semantic diversity。第 108 行先指出 affinity compatibility 会聚集互相关评论并造成 redundancy，再规定每个 query 应注意与其 incompatible/complementary 的评论，最后导出专用 diversity attention。理论机制与通用算法的错误方向在这一对段落中最清楚。

<a id="acaa-t7ab"></a>

### ACAA-T7a/T7b，原文第 110、112 行

第 110 行把单条评论层的 helpfulness、diagnosticity 和 persuasion 连接到购买决策，Mudambi and Schuff 2010、Yin et al. 2014/2021 支撑 votes 是普遍 helpfulness signal，Kuan et al. 2015、Gang and Taeho 2019 支撑 voted review 更吸引注意。第 112 行只保留一个计算要求：票数更高则 attention 更强，并将其转成权重鼓励机制。理论责任较窄，因此后续必须用独立消融证明它不是普通额外 feature。

<a id="acaa-t8ab"></a>

### ACAA-T8a/T8b，原文第 114、116 行

第 114 行先区分文本意见与图像场景线索，Yu et al. 2012、Yin et al. 2021、Ma et al. 2018、Li and Xie 2020 分别承担两种模态功能；Petty and Cacioppo 1986 与 O’Keefe 2008 定义 central/peripheral routes；Cook and Lalljee 1972、Muller et al. 2004 提供 substitution 与 complementarity 的相反证据；由此推出 text–image preference 随 review 而变。第 116 行将该变化转成 per-review adaptive weighting，并用 Ramachandram and Taylor 2017 区分 time-step-level interaction 与普通 modality-level fusion。引文既支撑机制，也承担直接方法边界。

### ACAA-T9，原文第 118 行及表 1

S1 将四项推导收束为 specialized attention 的必要性。S2 说明表 1 按 indicator、granularity、theory、challenge、solution 对齐，表格因此是理论责任矩阵而非装饰。S3 承认 Kuan et al. 2015、Liu et al. 2020 已概念研究部分指标，再把贡献限定为由这些指标设计 attention mechanisms。表 1 的每一行都要求后续算法出现相应计算对象；任何一行只有理论名而无 challenge/action 即未闭合。

表 1 的抽取完整性边界需单独保留。L122 中 Semantic diversity 行的 `Granularity level` 单元格是空白，而正文 T6a/T6b 可推知其涉及 review-subset/query 关系。本索引不把正文推知静默回填成“表中已写明”；该空格可能来自抽取或出版版式，待 PDF 视觉核对。

## 6. ACAA 方法

### ACAA-M0，原文第 126 行

S1 将表 1 的理论理由与 methodological challenges 明确设为方法的因。它不重新论证指标，而说明为什么需要 DTV 与 AMI。S2 按理论节的原顺序列出 timeliness、semantic diversity、voting awareness 和 adaptive multimodal interaction，形成方法节的兑现清单。句序只有“理论合同—工件责任”，没有重复引言贡献口号。

### ACAA-M1，原文第 130 行

| 句号 | 功能 | 推进作用 |
|---|---|---|
| S1 | ALG | 以 Figure 2 给读者一个全局定位 |
| S2 | ALG | 第一步是文本/图像预处理与 pretrained embedding |
| S3 | ALG+MEC | 由 review stream 的性质选择平行 GRU，分别产生两种序列表示 |
| S4 | ALG | 再把 DTV 与 AMI 嵌入 base model，保持理论模块后置于通用表征 |
| S5 | ALG+BND | 区分直接 prediction output 与可供 downstream model 使用的 representation，限定 artifact 的两种输出用途 |

该段只讲处理顺序，不在 overview 中塞公式。GRU 的选择理由来自输入的时序性质，而不是因为模型流行。

#### ACAA-F2，Figure 2 论证接口（L136–137）

Figure 2 的责任是把 M1 口述的 preprocessing/embedding、平行 GRU、DTV、AMI 与 prediction/representation 两类输出放在同一总体架构中。L136 是图题，L137 只有 API 附件路径；本地无图像。因此，M1 的五句可支持流程责任的文本索引，不支持对图中模块连线、张量标注、顺序或视觉强调的独立核对。

### ACAA-M2，原文第 134 行

本段以酒店合作任务说明 data collection，而没有把单一案例说成普遍数据生成过程。S1 解释为便于呈现，在酒店月度 occupancy 场景实例化方法；S2 宣告后续清洗步骤；S3 收集 quantitative、text、image 三类 review data；S4 说明每条评论的 text、images、votes、date 字段；S5 设定最短文本过滤；S6 明确 pure-image 与 plain-text 也可进入模型；S7 以预测月前固定时间窗、按时间排序形成三种模态组合的 review sequence；S8 排除过短序列与 occupancy 为零实例。所有句子承担样本进入模型的可复现规则，没有理论包装。酒店集团身份和案例合作是本文事实，不能由外部引文替代。

### ACAA-M3，原文第 139 行

S1 从收集转向 training matrices。S2 指出 text 与 review 一一对应，而 images 可能一对多，提出具体形状问题。S3 通过方格拼接把同一 review 的多图变成 holistic image，从而与 text 对齐。S4 说明 stacking 同时保留单图扫描与联合信息。该段的学术功能是解决多模态对齐，不把普通预处理冒充理论贡献；Online Appendix B 只承担例图接口，本地未取得时不能声称视觉检查。

### ACAA-M4，原文第 141 行

S1 先定义 padding mask 的一般用途，并用 Vaswani et al. 2017、Devlin et al. 2018 证明它是 attention/BERT 的标准操作。S2 宣告两阶段。S3 用 Dwarampudi and Reddy 2019 说明 padding/truncation 的标准动作。S4 用 Song et al. 2020 说明 mask 排除人工 padded values。段落先建立通用技术基线，为下一段只解释“本模型如何特殊化”腾出空间。

### ACAA-M5，原文第 143–159 行与公式 1–3

第 143 行的句序是“引入标准 self-attention—定义 input sequence—定义 mask—定义 K/V/Q—定义动态权重—给出 scaled multiplicative compatibility”。Vaswani et al. 2017 只负责标准 self-attention 来源，不能支撑本文专用机制。公式 1–2 把 query–key affinity 与 softmax weight 写成可复现 baseline。第 153 行再引入 mask，公式 3 将 `m_i` 加入 softmax；第 159 行定义 padded 位置为负无穷、其余为零，并解释结果。该单元的作用是给后文“现有 affinity calculation 朝错误方向”提供精确对照，而非展示公式数量。

### ACAA-M6，原文第 161 行

| 句号 | 功能 | 推进作用 |
|---|---|---|
| S1 | ALG | 声明本情境采用 bilevel mask |
| S2 | ALG | review level 处理 text/image modality missing，使两条序列可进入 multimodal model |
| S3 | ALG | hotel-month level 处理不同 review-sequence lengths |
| S4 | ALG | 报告预处理后的 text 与 image sequence 符号和形状，作为后续 embedding 输入 |

两层 mask 对应两个不同缺失结构，不能在新论文中仿照成没有数据结构依据的“两阶段模块”。

<a id="acaa-m7"></a>

### ACAA-M7，原文第 163–167 行

第 163 行先声明把两种序列映射到 embedding space，再解释 pretrained feed-forward transformations 可作为 embedding features。第 165 行以 Devlin et al. 2018 支撑 BERT，并给出 classification-token 的 768 维 text matrix。第 167 行以 Simonyan and Zisserman 2014 支撑 VGG-16 的视觉表征能力，并给出最后隐藏层的 4,096 维 image matrix。引用负责标准 encoder 的能力和来源；矩阵形状负责下游复现。两种 encoder 不是本文理论贡献。

### ACAA-M8，原文第 171 行

S1 说明需要在同一 multimodal model 中协调两条序列。S2 因两模态已有各自 encoder，后续只利用共同 time-sequence property，并用 Cho et al. 2014 支撑 GRU。S3 形成 text/image 两个 GRU。S4 解释每个 GRU 如何按 time step 递归训练。S5 以一个时点说明 cell state、gates 与预测。S6 给出两条 hidden-state sequences 的符号和形状。句序从共同结构性质导出 base model，再把输出接口交给 DTV；没有先讲专用机制后再补 base representation。

### ACAA-M9，原文第 173 行

S1 说明 DTV-AMI 通过 DTV 与 AMI 协同两个 GRU。S2 明确两机制逐项回应 Table 1 的挑战。S3 把 DTV 责任限定为 timeliness、diversity、voting 三项 review-level sequence delivery。S4 枚举 DTV 输入为两条 GRU embedding sequences、release dates 和 votes，并给形状。理论状态在这里变成真实输入张量，而不是只在模块名称出现。

#### ACAA-F3，Figure 3 论证接口（L191–192）

Figure 3 的图题将其定位为 proposed DTV 结构图。结合 M9–M12 的文本，该图应承担从 GRU hidden-state sequences、dates 和 votes 到 diversity score、time decay、voting awareness 与最终 review weights 的计算导航。L191 只有图题，L192 只有 API 附件路径，本地没有图像。因此，这一功能是由正文和公式接口确定，不是对图中节点、箭头、张量尺寸或运算顺序的视觉核对。

### ACAA-M10a，原文第 175 行

S1 以 Vaswani et al. 2017 为 common attention baseline，指出直接、无差别 query–key matching 与本文目标不同。S2 说明 DTV 使用 key–key interrelationships 与 query complementarity。S3 用 Tian et al. 2017 支撑 L2 norm 可度量 vector diversity。S4 预告模型应提高 less-redundant review 的权重。该段延续第 87 行的“通用计算方向错误”，并把理论要求缩成可验算的两个条件：complementary to query 与 nonredundant among keys。

### ACAA-M10b，原文第 177–187 行与公式 4–5

公式 4 先计算每个 key 对其余 keys 的平均 redundancy；公式 5 组合 redundancy normalization、inverse matching compatibility 与 regularization。L187 随后共七个语法句。S1 定义 `r_j` 的信息含义。S2 在一个 `whereas` 复句内分别解释指数项的归一化责任和 L2 inverse matching 突出 complementary keys 的责任。S3 说明 `w_j` 与 `lambda` 如何形成自适应 query 并缓解过拟合。S4 诊断单独 `f(q,k)` 不能产生同时处理 interkey redundancy 的 diverse query。S5 作出独立的【ALG】动作：因此以 `r` 调整 `f(q,k)`。这一句是“限制诊断→实际计算修正”的关键接口，不得并入 S4。S6 定义最终 `beta` 为面向 query 的 diversity-score distribution。S7 给出可观察行为标准：同时互补且不冗余的 keys 获更大权重。公式后的文字不是重复符号，而是逐项建立机制可解释性和消融对象。

公式 5 还有一个不能静默修正的源文异常。L184 分母的求和索引是 `u`，但指数项仍显示 `exp(-r_j)`，按归一化语义应当检查是否为 `exp(-r_u)`。本索引仅记录异常与待核对方向，在未查出版 PDF/代码前不改写原公式。

### ACAA-M11，原文第 189–198 行与公式 6

第 189 行先把理论要求压缩成 time-decaying term，再用 Ahmed et al. 2011、Chen et al. 2009 支撑 exponential decay 对动态用户兴趣和序贯行为的适用，随后引入强度参数 `eta`，最后说明它怎样与 normalized diversity score 组合。公式 6 给出完整权重。第 198 行定义时间差、归一化区间和首末评论的边界值，并以“近期权重更高、沿时间呈衰减”收束为可观察行为。引用只支撑 decay function 的方法合理性，不替代 customer-attention 理论。

### ACAA-M12，原文第 200–208 行与公式 7

第 200 行用 exponential function 和 `gamma` 将 voting effect 设为 nonlinear，再说明与 time term 共同调整 diversity score。公式 7 把三项责任写入同一 attention weight。第 206 行定义 votes、最大 votes 和 relative popularity，并明确 more-voted reviews 权重更高。第 208 行先解释 `eta/gamma` 的强度和交互，再提出旧评论累积 votes 更多、投票吸引力抵抗 time decay 的相反作用，最后回收 DTV 能容纳这种 interplay。这里不是三项独立分数相加后结束，而是专门讨论两个现实信号方向冲突。

### ACAA-M13，原文第 210 行

S1 将 diversity、timeliness、voting 合并成 normalized comprehensive review weighting。S2 用该权重乘 value matrix，得到每个 time step 的 representation 并给出形状。该段是 DTV 的输出接口，必须能被后续 AMI 和实验中的 representation evaluation 使用。L210 的符号责任存在抽取/原文异常：先将 `hat alpha` 定义为 normalized `tilde alpha`，随后文字说用 `tilde alpha` 加权 V，但给出的表示公式又使用 `hat alpha`。实现前必须查 PDF 或代码确认应当进入 value weighting 的张量，不得把本索引的语义概括当成符号已统一。

### ACAA-M14，原文第 212–218 行与公式 8

第 212 行先给 text/image DTV representations 和预测向量，再声明 AMI 通过 review-specific relative-importance threshold 融合。公式 8 用 `xi_i` 与 `1-xi_i` 在每个 time step 对两模态加权。第 218 行解释 output-layer weight、adaptive vector 和 `xi_i` 的 tradeoff 含义，并把结果收束为单条 review 的 text/image 作用可变。该机制对应 theory section 的 review-element granularity，不是普通一次性 modality concatenation。

### ACAA-M15，原文第 220 行

S1 以所有 time-step predictions 的 global average 形成最终输出，并用 MSE 优化。S2 用 Wang et al. 2016、Lei et al. 2018 界定 attention RNN 的 ex ante representation pooling，再把本文区分为 ex post prediction fusion，并提出较少信息损失的理由。S3 回到顾客间歇到达与每个 review point 可作浏览起点的真实情境，为方法差异提供行为依据。段落顺序是“输出—直接方法边界—情境机制回扣”。

### ACAA-M16，原文第 224 行

七句依次说明：Online Appendix C 的训练流程图；从 raw reviews 得到 text/image/date/vote/label sequences；BERT/VGG embedding 进入两个 GRU；DTV 加在 hidden states；AMI 作为 adaptive fusion 与 bimodal GRU 联合训练；各 time-step predictions 平均；backprop 同时更新 neuron weights、attention weights 和 `xi`。该段把前述所有张量按真实训练顺序闭合。附录图未在本地取得，因此只能核验主文所述流程，不能声称逐框检查 Figure C1。

## 7. ACAA 经验评价、贡献与结论索引的衔接

ACAA 第 226—348 行的经验评价、贡献与结论已在 `00M_ACAA实证贡献与结论逐句逻辑索引.md` 逐句展开。该文件覆盖 27 个正文段落、128 个原文语法句、表 2—5 与图 4—7，并逐句区分表中客观数值、统计检验、作者解释和理论回收。L228 现按五句索引，L310 现按六句索引；两处一增一减，因而该范围总计仍为 128 句，但每个句界已与源文一一对应。ACAA 主文 L29–L348 共 397 个语法句，段落主键与分节计数见 `00W`。

在线附录 A–I 均未在本地取得。其接口分别包括：附录 A 的直接方法差异比较，B 的图像预处理例图，C 的训练流程，D 的描述统计，E 的 MAE 结果，F 的实现细节，G 的 Tukey–Kramer 比较，H 的额外探索分析，I 的消融结果。对应句子只记录附录在论证中的出口功能，不把作者对附录的转述写成已经独立核验的事实。Figure 1–7 也只有图题/附件路径，不在可视核对范围。`00M` 另行保留原文中 voting/timeliness 术语错位、`1−ξ` 字符解析和 AC-sel/AC-self 命名不一致等源文本异常；本文件另保留 L122 空单元格、L184 归一化分母与 L210 `hat/tilde` 不一致。正式模仿和算法实现均不得复制或静默“修好”这些异常。

## 8. ACAA 尾注 1–12 的逐句功能与引文责任

ACAA 尾注位于 L352–L374，共 12 个编号、17 个语法句。尾注不计入 L29–L348 的 397 个主文句，但它们承担构念定义、方法来源和实现边界，因此必须独立索引。

1. **N1，L352，1 句。** S1 依 McGuire (1968)、Petty and Cacioppo (1986) 与 Li and Hitt (2008) 给出 customer attention 的本文定义，即顾客愿意且有能力注意评论。三条引文承担核心构念的理论来源，不承担 DTV-AMI 的经验效果。
2. **N2，L354，1 句。** S1 说明用 timeliness 与 helpfulness votes 描绘注意时，还容纳两者的交互。无外部引文；该句限定 M12 不能把两信号当作完全独立。
3. **N3，L356，1 句。** S1 借 Ngiam et al. (2011) 的 multimodal-data 概念，将 multimodal reviews 限定为同时包含定量指标、文本和图像的评论。Ngiam et al. 承担多模态对象的概念来源，不承担本文特定数据实现的有效性。
4. **N4，L358，2 句。** S1 说明 sales-prediction 文献中 sales 常操作化为 revenue 或 product-sales ranking。S2 转入本案例，说明应合作酒店集团要求以月度入住率作为可行动 sales-performance metric。这是领域术语边界和案例任务边界，不是效果证据。
5. **N5，L360，1 句。** S1 定义 affinity-based compatibility functions，即 key 与 target query 越接近，对应输入获得越大注意。无外部引文；该定义服务于 T6b/M10a 对普通 affinity 计算方向的批评。
6. **N6，L362，2 句。** S1 把 attention query 回译为顾客的信息检索操作。S2 定义每个 target query 从对应 review point 出发并向更多评论扩展。该注为 global query 和 ex-post fusion 提供情境语义，无外部引文。
7. **N7，L364，2 句。** S1 声明用 GRU 作为多模态评论序列的 base model。S2 以 Fu et al. (2016) 支持 GRU 的 gated-memory 全局序列表示能力，以及它与 LSTM 性能可比而更高效的方法选择理由。该引文只承担基础架构选择，不承担专用 attention mechanisms 的贡献。
8. **N8，L366，1 句。** S1 说明四种注意权重在 hotel level 随对象学习，因而不同酒店产生不同权重，并把适用范围延伸到连锁与独立酒店。这是作者的适用性说明，不是跨酒店外部效度已获验证的证据。
9. **N9，L368，1 句。** S1 区分 trainable deep representations 与 fixed features，并说明 keys、values 和 queries 可面向不同 query 动态优化。该句承担张量可训练性与推断时动态性的实现边界。
10. **N10，L370，2 句。** S1 定义一个 instance 为一个 hotel-month 对应的 text sequence 和 image sequence。S2 说明不同 hotel-month 的双模态序列经 padding 后对齐。两句共同承担训练样本单位和 batch 张量对齐责任。
11. **N11，L372，2 句。** S1 宣告 embedding features 与 representation features 的区分。S2 将前者定义为网络输入，后者定义为深度表示学习后的 neuron outputs。该区分直接限定实验 2 的 representation-learning 评价对象。
12. **N12，L374，1 句。** S1 报告作者的经验测试选择：序列多模态模型直接预测时，ex-post fusion 优于 ex-ante fusion；把表示交给下游预测器时，ex-ante 反而更好。该句是作者报告的方法选择依据，本地主文没有对应数值表或试验细节，不得改写为已独立复现的结果。

## 9. DSDL 全篇索引的衔接

DSDL 第 27—343 行的 76 个逻辑自然段、396 个语法句、11 个公式、7 张表、3 组图、四项实验、解释性分析、贡献、局限与结论已在 `00K_DSDL全篇逐句逻辑与引文责任索引.md` 完成逐句功能和引文责任分析；第 351—363 行尾注也已纳入。原 Markdown 在该范围有 87 个 prose blocks，其中 L109 和 L269 是以 Figure/Table 开头的正文而非图表题；从 87 块到 76 段的全部合并规则已在 `00W` 冻结。该文件逐段记录问题建立、理论状态、张量运算、损失责任、结果证据、作者解释与适用边界，并明确区分主文声称的附录结果和本项目已独立核验的内容。

DSDL 在线附录 A–I 未在项目中找到，Figure 1–3 只有 `images_downloaded: false` 条件下的附件占位。L77/L79、L251/L265 的逻辑段被分页或浮动表格切断；L124、L132、L148、L156、L195、L224 还存在集合符号、张量形状、状态描述、范数或损失正负号疑点。正式算法复现和写作对照必须以这些缺失与源文本异常为边界，不得把 OCR/MinerU 断词或公式损坏当作肖帅勇老师的写作与建模习惯。

## 10. 完成口径

至此，ACAA 与 DSDL 两篇可获得主文均已完成从摘要到结论的逐段逐语法句索引，ACAA 的 12 条尾注和 DSDL 的 7 条尾注也已纳入。该完成状态只覆盖已实际取得的 Markdown 文本、可读表格与公式接口；它不扩张到两篇缺失的在线附录和图像视觉内容，也不把明示的符号/抽取异常当作已由出版 PDF 或代码核实。可复现的段落、句子、公式、浮动对象、尾注和图像状态主键以 `00W` 为准。
