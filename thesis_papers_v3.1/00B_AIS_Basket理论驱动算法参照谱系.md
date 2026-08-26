# AIS Basket 理论驱动算法参照谱系

> **现行映射提示（2026-08-15）。** 本文件只承担 AIS Basket 理论—算法先例与当前设计的映射，不定义题位或写作授权；后者仅以 `00F_现行题位与设计稿授权.md` 及当前 `01/02/03` 正文为准。现行三条算法链是 EUMN（实际返回 → 冻结五维透明门 → 逐充分义务束的来源约束 OT/F → 残余一次补取或 ACT-NOW → post-reacquisition F/传输 → 有界行动序列、约束与证据引用 → 无 raw-return 通道的共享冻结 executor → 外部 Y）、OIWG（**DEMOTE / DESIGN-ONLY / NO-RUN**）与 AVEP（class-conditioned prior/world likelihood → Bayes → 有界 OtherBranch → $g_e^{FB}$ → distributional CQL）。配方族、one-more scout 和 repair-tier 在本文中出现时均只能是历史否决对象或强边界，不得再写成当前 P1/P3。

## 一、用途与判定标准

本文件不替代 Xiao et al. 两篇 ISR 论文的逐段写作模板。ACAA 与 DSDL 仍然承担段落句法、句间推进、引用责任和理论—方法—实证闭环的逐段回读责任。本文件只回答另一个问题：AIS Senior Scholars' Basket 中，哪些论文真正让理论进入了算法内部，以及三篇 Coding Agent 论文能够借鉴什么。

本文把“理论驱动”分成四级。

1. **A级：理论改变算法的规范决策。** 理论直接改变目标函数、候选排序、搜索、停止、可行域或最终行动，且能产生与通用预测目标方向不同的行为。
2. **B级：理论创造计算对象或结构。** 理论决定必须显式构造何种图、状态、潜变量、任务层级或损失项，普通端到端模型不会自然得到同一对象。
3. **C级：理论选择架构或特征。** 理论说明应输入哪些信号、分开哪些模态或如何组织模块，但核心损失和决策规则仍较通用。
4. **D级：理论只解释变量或评价结果。** 算法在不知道该理论时仍会自然采用同一做法。此类论文可以借鉴写作或测量，不足以支持 v3.1 的算法独特性。

一篇论文只有同时回答以下问题，才进入三篇论文的核心方法参照：理论新造了什么计算对象，改变了哪一条信息流或可行域，推出了什么反直觉行为，以及是否存在针对该理论机制的中间量检查和专门消融。

| 代表论文 | 理论进入算法的位置 | 理论产生的非显然实现 | 对 v3.1 的主要作用 |
| --- | --- | --- | --- |
| Mookerjee and Dos Santos 1993 | 目标、候选选择、停止、最终行动 | 信息能降低熵仍可因不改善决策价值而拒绝 | P1 残余补取/ACT-NOW 与 P3 实验/纠正行动的规范边界；不为其专属状态背书 |
| GOAL 2007 | 主动取得样本的排序 | 有意不优化总体预测误差，只取得可能改变行动的标签 | P1 补取必须改变 post-reacquisition F/U/Y，P3 分支必须改变尾行动排序 |
| Hosanagar 2011 | 源集合、等待终止、展示数量 | 用户效用和多类成本联合决定查询与停止，并由命题压缩搜索 | P1 一次来源补取与 P3 实验/终止的强规范基线；旧 FIT-USE 仅为历史 |
| Mookerjee and Mannino 2000 | 输入、停止与行动的均值—风险目标 | 风险不只报告，而同时改写取得和终端行动 | P3 distributional CQL 的先例与边界；理论增量必须来自 $g_e^{FB}$ 而非“使用尾险”本身 |
| DLDE-MAB 2023 | 组合可行域、表示和辅助损失 | 行为理论维度成为硬覆盖约束与 SMART/健康结果监督 | 理论必须进入公式、算法框与逐项消融的写法 |
| X-IM 2020 | 缺陷诊断与系统组件 | 缺失和冗余使用不同修复对象，不把所有错误压成一分 | P1 实际返回—来源命题—忠实度缺口—补取部件逐项对应的同理论边界 |
| Conversational Dashboards 2023 | effective-use 构念与设计要求 | 透明交互、表征忠实度和知情行动分层，而非压成总体使用分 | P1 的 T→F→U 构念边界与 P3 反馈控制起点；不直接推出 OT、补取或策略网络 |
| G-FINDER 2024 | 中间表示与结构评分 | 论证理论产生 signed triangle 与结构平衡分数 | P2 OIWG 的 claim–evidence–warrant 计算对象参照；旧 RFGP 的关系证书只属历史 |
| GDCM 2025 | 表示几何与正则项 | 原型、差异化与结果相关性分别进入空间和损失 | 已否决 FIT-USE 的历史结构化-loss 参照，不再为 OIWG 背书 |
| TheoryOn 2020 / Schema 2024 | 标签本体、任务顺序与激活搜索 | 理论先规定有序产物和情境激活，再选择相应模型 | TheoryOn 约束 OIWG 的 claim schema；Schema 只用于低成本 offline screen，不构成第二候选 |
| Shaft and Vessey 2006 | 机制预测而非算法 | 软件理解更多在认知失配时反而降低修改绩效 | 已否决 FIT-USE 的历史 coding-domain 预测 |

## 二、最强的理论—算法先例

### 2.1 系统价值直接改变候选选择、停止和最终行动

Mookerjee and Dos Santos（1993，ISR，DOI: https://doi.org/10.1287/isre.4.2.111）是最强的 A 级先例。本地全文 `26627_1993_inductive-expert-system-design-maximizing-system-value.md` 第145–169行先把归纳算法拆成输入选择、停止和分类三个相互关联的决策，再指出信息量或准确率不能代表系统价值。第177–179行把信息取得策略与最终决策规则放入同一棵决策树，以最终决策收益减信息成本为目标。第193–225行先计算立即停止时的最小期望分类成本，再计算取得每个候选输入后的边际成本改善，并用单位取得成本的改善量排序。第227–233行据此形成明确停止条件和叶节点行动。正文后面的反例进一步展示，一个输入可以降低熵却恶化系统价值。

这里最值得借鉴的不是“把成本加进 loss”，而是理论同时重写信息取得、停止与最终行动三个接口。对现行 P1，它要求未匹配义务残余只有在预计补取能改善 post-reacquisition 忠实度与后续软件行动时才应压过 ACT-NOW；对现行 P3，它要求候选实验与 ReturnToEdit、Submit、Handoff 放在同一长期后果账中。需要主动承认，价值减成本、成本式停止和短视 VOI 早已存在，不能作为 EUMN 或 AVEP 的新颖性主张；两篇的专属对象分别是来源约束忠实度残余和反事实反馈分支。

Saar-Tsechansky and Provost（2007，ISR，DOI: https://doi.org/10.1287/isre.1070.0111）把同一逻辑推进到主动学习。本地全文 `04562_2007_decision-centric-active-learning-of-binary-outcome-models.md` 第99–119行指出，降低统计预测误差并不保证改变最终行动。第121–147行依据行动、失败、不行动和取得成本推出任务特定的决策无差异阈值，并说明即使概率估计很不准确，只要它仍导出正确行动，继续提高精度也可能浪费成本。第149–185行据此把采样分数改成“距离行动改变尚需多大概率移动”，而不是通用不确定性；第303–312行再除以非均匀取得成本。其结论明确报告，方法有时牺牲总体概率估计精度，却产生更好的经营决策。

这篇论文提供了一个应写进 v3.1 的判定标准：如果理论机制只提高 Recall、F1 或校准，却没有系统性改变最终编辑或交付行动，它还不是决策中心算法。P1 必须证明残余补取相对 ACT-NOW 改变 post-reacquisition F、U 与固定预算软件结果，P2 必须证明 signed closure 进入 hunk 生成并产生普通 completed-patch pools 外的新正确解，P3 必须证明 $g_e^{FB}$ 相对信息增益或 direct-Q 改变实验与尾行动排序，并让真实软件后果承担最终责任。

Hosanagar（2011，ISR，User-Centric Operational Decision Making in Distributed Information Retrieval，DOI: https://doi.org/10.1287/isre.1100.0287）是与检索最直接的 A 级先例。本地全文 `12618_2011_usercentric-operational-decision-making-in-distributed-information-retrieval.md` 第49–65行把查询哪些 IR 服务器、等待响应多久和展示哪些结果联合成用户效用问题，而不是三个独立启发式。第83–87行把等待、访问和处理结果的认知成本纳入同一规范模型。第221–270行使用户实际处理的文档数量内生，并以文档效用减评价成本、查询费和等待成本形成随机混合整数目标；第276–287行由边际收益与等待成本推出源选择和终止条件；第308–314行再用结构命题把 $2^N$ 个源集合缩成排序后的可执行搜索。第365–376行给出等待、认知或访问成本升高时源集合缩小且更早停止的方向性预测。

这篇论文仍是旧 FIT-USE、现行 P1 与现行 P3 的新颖性边界：旧 P2 不能声称首次做效用驱动的 source selection，P1 不能把“一次成本敏感来源补取”本身当作贡献，P3 也不能声称首次联合实验取得与终止。Hosanagar 的关键可分性来自服务器贡献相加、结果按既定方式展示和用户效用模型；EUMN 只有在实际返回经来源约束 OT 形成的未匹配义务残余能够产生普通相似度/直接-Y 补取器没有的 ACT-NOW 与 post-reacquisition 行动差异时才越过该边界，AVEP 则必须依靠运行 likelihood、Bayes 分支和尾行动差距越过静态源选择。OIWG 不做源选择，不得把 claim–hunk–test 工件写成 service router、set packing 或 online stop 的换名版本。

Mookerjee and Mannino（2000，ISR，DOI: https://doi.org/10.1287/isre.11.2.137.11777）进一步说明风险不能只放在报告表。本地全文 `26363_2000_mean-risk-trade-offs-in-inductive-expert-systems.md` 第338–346行再次将算法拆成输入选择、停止和分类；第348–411行用同时包含取得成本与分类成本均值、方差的 mean-risk measure 重写三者；第413–423行再证明可分性以避免组合爆炸。现行 P3 已让回报分布和下尾风险进入 experiment、ReturnToEdit、Submit 与 Handoff 的共同排序，因此可以把该文作为规范先例；也正因如此，“使用 distributional critic/CVaR”不能成为新颖性。AVEP 必须证明 world likelihood → Bayes → $g_e^{FB}$ 所产生的分支—尾行动方向冲突，超过同一分位 critic 的 plain distributional CQL、mean-value CQL 与 flat POMDP。

### 2.2 理论直接生成硬约束、辅助任务与组合优化

Agarwal et al.（2023，ISR，DLDE-MAB，DOI: https://doi.org/10.1287/isre.2022.1191）是“理论写进实现 trick”的最接近先例。本地全文 `28562_2023_spoiled-for-choice-personalized-recommendation-for-healthcare-decisions-a-multiarmed-bandit-appr.md` 第51–85行由行为健康、社会认知与 SMART 框架推出动态、多序列、结果反馈和多维需求。第89–97行把这些要求一一映射到神经情境表示、辅助健康结果损失和理论引导的多样化约束。第99–130行没有仅把理论维度当特征，而是要求推荐集合在每个健康管理维度至少选择一个项目；第132–180行把 Thompson sampling 后的选臂改成受这些覆盖约束限制的二元组合优化。第226–263行又把健康结果反馈和 SMART 属性变成独立监督损失。第324–338行逐项删除约束、用户表示和项目表示。

这篇论文给三篇 v3.1 的最低实现标准是：理论至少应改变一次模型的可行域、内部监督或决策操作，而不能只给输入变量命名。P1 的来源约束 OT、独立监督的未匹配义务残余、一次补取/ACT-NOW 与 post-reacquisition F→U/Y，P2 的 signed warrant 状态、closure loss 与 hunk-level 条件生成，P3 的关系 world likelihood、Bayesian 反事实分支、$g_e^{FB}$ 动作张量与 distributional CQL，都必须能在公式、算法框、机制标签和等参数消融中逐项指出。

### 2.3 理论创造普通模型不会主动发明的计算对象

G-FINDER（2024，ISR，DOI: https://doi.org/10.1287/isre.2020.0097）是 B 级强先例。本地全文 `27953_2024_explainable-deep-learning-for-false-information-identification-an-argumentation-theory-approach.md` 第75–83行先用 Toulmin 论证模型说明 claim、evidence 与 warrant 的缺口，再指出理论本身尚未给出计算设计。第85–110行借结构平衡理论和指称理论，把 warrant 变成带符号的三节点词网络及平衡条件。第114–149行再把句子分解、实体识别、三元组、符号边与平衡分数接入 ML/DL。这里理论不是给 embedding 增加一个名称，而是创造了 signed triangle 这个黑箱文本分类器不会自然构造的中间对象。

对旧 RFGP 的历史借鉴曾是“关系见证必须可检查”，但 typed witness path、AND 证书与 broken-chain 扰动既未由表征理论逻辑推出，也未通过现象门，现已退出论文一主设计。这个否决仍保留一条通用纪律：理论创造的中间结构必须可单独测量，且必须和等参数通用模型比较，不能仅凭命名获得解释权。

对 P2 OIWG，G-FINDER 的可借之处更窄也更强：Toulmin 的 claim、evidence 与 warrant 要求补丁解释不能只剩“这个 patch 通过了测试”，而应显式表示“哪条行为主张由哪个测试观察、哪组 hunk 在冻结执行器下使该观察成立”。结构平衡只提供 signed triangle 的计算启发，不能把 hunk rollback 升格为语义因果证明。OIWG 的 **claim–hunk–test observed-interventional warrant closure** 将 claim–test 作为部署可见输入上的预冻结语义对齐，将 hunk–test 作为实际回滚/coalition 执行的观察效应，将 hunk–claim 作为模型预测的支持或冲突边；只有三边一致才形成可训练的 observed warrant。若同样结果可由普通 hunk ablation、multi-hunk delta debugging 或通用 verifier 复制，G-FINDER 只能保留为解释类比，不能支撑理论专属性。

GDCM（2025，ISR，DOI: https://doi.org/10.1287/isre.2020.0494）展示理论如何成为表示几何与正则项。本地全文 `27974_2025_guided-diverse-concept-miner-gdcm-uncovering-relevant-constructs-for-managerial-insights-from-te.md` 第139–175行把可解释、差异化和结果相关性分别落实为共享语义空间、稀疏/多样性正则与结果分类损失。第177–211行依据原型理论让词、文档和可学习概念原型处于同一空间，第213–229行增加稀疏和概念间排斥，第231–255行再用管理结果约束概念相关性。理论因此同时决定了潜变量的几何含义和多个损失项。

这篇论文曾启发旧 FIT-USE 把任务需求与服务能力放入同轴空间，并对供给不足、供给过量和 A→R→U 层级施加结构约束。该路线已判 NO-GO；这些对象现在只作为“理论可以进入表示几何与损失、但仍可能缺少决策杠杆”的历史反例，不能移植到新论文二。

### 2.4 理论规定知识结构、激活顺序和模型管线

Schema-guided knowledge-aware learning（2024，JMIS）是 B 级先例。本地全文 `16424_2024_knowledge-aware-learning-framework-based-on-schema-theory-to-complement-large-learning-models.md` 第128–158行先指出把外部知识当附加向量忽略了结构、任务相关激活和知识利用过程，再将 schema theory 拆成知识取得、结构化表示、情境激活和任务利用四个 meta-requirement。第169–195行把知识组织成概念—关系图，以任务语料相对于一般语料的关系权重激活局部 schema，并在不足时进行拓扑扩展。第197–205行再以 GCN 与 BiLSTM 合并激活知识和焦点文本。第306–314行分别删除激活、GCN 与 BiLSTM。

这篇论文曾对旧 FIT-USE 提供“目录成员需要语义、任务只激活相关能力”的直接启发。旧路线已经否决；对 OIWG，Schema 框架最多支持在 20 题 offline screen 中检验 issue 与 visible FTP 能否形成稳定 claim schema，其频次激活不能为 hunk 干预效应、signed edge 或补丁正确性背书。

TheoryOn（2020，MISQ，DOI: https://doi.org/10.25300/MISQ/2020/15323）则展示理论如何决定标签空间和任务先后。本地全文 `12584_2020_theoryon-a-design-framework-and-system-for-unlocking-behavioral-knowledge-through-ontology-learn.md` 第51–90行把理论实例界定为构念、关系和状态构成的本体，并依据 ontology layer cake 规定假设、构念、理论关系和同义关系的有序输出。第92–128行据此把通用文本挖掘拆成规则/分类、序列标注、关系抽取和同义识别等不同任务。理论先定义“必须产出什么以及何者是何者的前提”，模型才选择相应架构。

对 OIWG，TheoryOn 的可迁移责任是先冻结 claim 本体、claim–test 对齐、hunk 干预标签与闭合判断的先后关系，再选择模型；它不推出 signed edge，也不证明 rollback 的语义因果性。对旧 FIT-USE 的取得—表征—使用类比仅保留为历史记录。

### 2.5 同一表征理论的直接先例

X-IM（2020，JAIS，DOI: https://doi.org/10.17705/1jais.00626）仍是论文一需要对话的表征理论边界。本地全文 `08372_2020_x-im-framework-to-overcome-semantic-heterogeneity-across-xbrl-filings.md` 第77–95行先枚举 representation theory 的构念缺失、过量、冗余和过载，再论证在 XBRL 场景中真正成立的是缺失与冗余，其他两项不应被机械照搬。第97–114行分别用投资者本体修补缺失、用标签和 designative metadata 消解冗余，并把两种缺陷形成两套设计原则。第116–142行再让每套原则对应独立假设和系统组件。它支持“先诊断适用的表征失真，再给每类失真配置可定位部件”，却没有推出来源约束 OT、未匹配义务残余、来源能力预测或一次补取策略；这些必须由当前 Coding Agent 情境的构念映射、独立标签和方向性检验另行成立。

它提供了非常适合 P1 的写作和设计纪律：先从实际工具返回而非条件名称出发，区分透明取得缺口与返回内容形成的表征忠实度缺口；再让当前来源命题、任务累计命题和机器可见任务义务通过来源约束传输形成双层 F；最后只让仍未被忠实覆盖的高必要度义务成为补取残余。现行设计必须分别检查返回来源恢复、四维忠实度、监督残余、来源能力预测、ACT-NOW 校准和 post-reacquisition F 的行动传导。旧 one-MSC、共同核、替代组、完整关系路径与 broken-chain 都是历史否决对象，不得由 X-IM 的一般表征论述恢复。

## 三、理论模型转为可执行算法的近期 ISR 范式

Consumer Acquisition for Recommender Systems（2024，ISR，DOI: https://doi.org/10.1287/isre.2023.1229）不是三篇所用的同一理论，但它的论证结构特别接近目标博士论文。本地全文 `28682_2024_consumer-acquisition-for-recommender-systems-a-theoretical-framework-and-empirical-evaluations.md` 第95–147行先定义市场主体、顺序依赖的系统价值、网络外部性、激励和参与成本，再把下一对象写成相对当前已实现序列的边际效用。第165–217行说明不可直接观察的系统价值如何通过性能变化、排列和估计得到。第227–266行用定理消去不影响下一对象排序的变量，最终得到可执行算法。

这篇文章值得模仿的是“规范模型—可观察量—识别/估计—定理化简—算法—实证”的单链，而不是在理论和模型之间跳步。三篇 v3.1 都应说明：理论里的抽象量如何从公开 benchmark 生成，哪些量可直接观察，哪些需要配对分支估计，哪些只作为代理，以及理论结构是否能化简搜索或校准。

## 四、写作框架强但算法独特性较弱的先例

DeepVoice（2023，MISQ，DOI: https://doi.org/10.25300/MISQ/2022/17062）第67–103行采用 kernel theory → meta-requirement → metadesign → testable hypothesis 的清晰表格，把 vocal/verbal 分流、时间序列和模态一致性映射为两阶段 LSTM；第105–121行以等维变换避免一种模态压过另一种，再融合两个序列。它很适合借鉴设计科学的写作组织，但 LSTM 与 MSE 本身并非只有该理论才能想到，因此只能作为 C 级架构参照，不能作为 v3.1 “非该理论不可得”的最高标准。

Finding Useful Solutions in Online Knowledge Communities（2020，ISR，DOI: https://doi.org/10.1287/isre.2019.0911）曾为旧论文二提供“相关 thread 不等于 useful solution”的概念桥梁。其知识采纳模型把 usefulness 拆成论证质量和来源可信度，再形成多组可计算特征并交给常规分类器；论文还逐维加入理论特征并与 CNN/LSTM 比较。它因此改变了目标标签、特征本体和层级任务，但没有改变分类损失、搜索或取得决策，属于 C 级而非 A 级先例。FIT-USE 已被否决；对新论文二，这篇论文只继续划定底线：若 claim、hunk 与 test 最终只是若干特征，输出仍是普通 patch score 或 beam rerank，理论驱动程度仍没有越过这类工作。

Conversational Dashboards for Effective Use（2023，JAIS，DOI: https://doi.org/10.17705/1jais.00801）把 transparent interaction、representational fidelity 和 informed action 转为自然语言访问、模态选择和 onboarding 等界面原则，但实证主要测量 transparent interaction，未完整识别后两层。它支持 P1 将 T、F、U 分层并让软件结果保持为独立后果，也支持 P3 把反馈后的判断修正与纠正行动分开；它不能直接为来源约束 OT、残余补取、signed warrant、$g_e^{FB}$ 或 distributional CQL 背书。

Dialectic decision support 等 TTF 应用更多用任务—技术匹配解释系统效果，而没有让 TTF 改变算法公式、搜索或损失。这是论文二必须主动越过的弱范式。

## 五、对三篇 v3.1 的具体迁移

### 5.1 论文一：忠实度残余必须真正改写一次取得与行动链

P1 当前的理论实现链是：每个受控分支的**实际工具返回** → 冻结来源卡生成器形成当前与累计来源命题 → 与 F 参数分离且先独立训练、随后整体冻结的五维 T 栈 → 固定等权、停止梯度的合取透明门把归一基础来源质量收缩为总量不超过 1 且不再归一化的有效行质量 → 对每个部署可见充分义务束分别求解来源约束 OT，并以冻结最小残余规则实现替代束的 OR 语义 → 双层忠实度状态 $\widetilde z_c^F$ 与所选束的未匹配残余 $\widehat{\mathbf d}_c$ → 基于部署可见来源能力和成本的一次目标补取或零分 ACT-NOW → 若补取则读取真实新返回、重算全部束及 post-reacquisition F/传输 → 从最终传输解码有界行动序列、可见约束槽和带未归一质量的证据引用 → 只接收共同任务/基础仓库状态与该三元计划的共享冻结 executor → 独立 $Y/C$ 软件结果。共同起点不接收条件编号；F/U 与 executor 都不能直接读取 raw return、未门控命题池或条件可见上下文，且全部透明门为零时条件特异内容增量与证据槽必须精确为零。没有补取价值时，理论要求显式拒绝取得而非总选一个来源。有效使用理论并不逻辑蕴含分栈合取门、逐束 OT、一次补取或三元计划，这些是 Coding Agent 情境化设计猜想，必须由方向冲突、强替代和 paired neutralization 共同否证或支持。

非显然实现不只是“把 residual 当特征”。训练/开发期登记探针产生独立监督残余 $\bar{\mathbf d}_c$、真实来源能力 $\bar{\boldsymbol\kappa}_v$、实耗和补取后残余；部署能力头则只能读节点、来源类型和接口元数据，主测试不得预跑全部候选。指针标签由独立监督的残余减少减真实成本定义，模型自己的 OT 输出不能自我充当真值。补取后的 F 与配对证据引用才进入 U/executor；post-F neutralization 也必须把该状态对应的证据引用一并交换或清空。Y/C 只读停止梯度的 F/U 状态作诊断，不能倒逼构念栈或替代共享 executor 的真实结果。

representation theory、X-IM 与 effective use 支持来源—表征—行动的分层责任；Mookerjee、GOAL 与 Hosanagar 只支持“取得必须改变行动价值且可选择不取得”的规范方向。它们都没有自动推出上述来源约束传输、独立残余标签或 post-reacquisition 重算。ContextBench、SWEzze、RepoShapley 与 Context-as-a-Tool 已覆盖探索—利用缺口、充分压缩、联盟效用和主动上下文管理；普通相似度、直接-Y 补取、交叉注意、flat-history Transformer 与等参数通用模型若能复制补取选择和固定预算软件结果，EUMN 就只能降为测量模型，不能保留算法章节身份。

### 5.2 论文二历史路线：匹配、有效使用与 refinement proof 均不再授权

非线性 TTF、Burton-Jones and Grange、TheoryOn、GDCM、Schema 框架与 Shaft and Vessey 曾约束 FIT-USE 的需求—能力双编码、方向性失配和 A→R→U 层级；FIT-USE 已因服务并集缺少 headroom 判 NO-GO。随后提出的 query-only refinement-proof program 又因 Python 动态语义与 generic provenance/equality guard 可复制判 formulation-level NO-GO。上述理论与实现记录只保留为否决谱系，不能通过换名进入新 P2。

### 5.3 论文二 OIWG：观察性干预 warrant 闭合

OIWG 的现行设计链是：部署可见 issue/FTP → 原子行为 claim → claim–test 支持边 → patch hunk/coalition 回滚的 test 效应 → signed claim–hunk–test triangle → 未闭合 claim 状态 → 约束式 hunk-level 解码。理论必须同时改变四处：表示从 patch/test 二元矩阵改为带正负边的三元 warrant 图；标签区分 `INDIVIDUAL_WITNESS`、`JOINT_ONLY`、`SUBSTITUTABLE` 与 `NON_IDENTIFIABLE`；损失同时惩罚未闭合 mandatory claim、失衡 triangle 与“FTP 通过但 hunk 对 claim 无可观察支撑”的硬负例；搜索在每个 hunk 边界优先修复最弱未闭合 claim，并禁止把未闭合状态当作终止解。普通 patch likelihood、更多 visible FTP 或更短 diff 因而可能与该搜索方向相反。

这仍只是 **DEMOTE / DESIGN-ONLY / NO-RUN** 的设计候选，不是 conditional GO。`00F` 允许把 OIWG 写成完整、可执行且可否决的研究设计，但不授权启动训练、生成 checkpoint 或陈述经验贡献。single-hunk rollback 只能说明某 hunk 对某冻结 patch/test execution 的观察必要性，不能证明该 hunk 在语义上导致 claim 成立；hunk 交互、替代实现、偶然覆盖和测试缺口都必须保留。[IBugFinder](https://doi.org/10.1145/3660828) 已枚举 multi-hunk patch 的 partial-patch 子集并研究八类 hunk 关系，[TRIM](https://arxiv.org/abs/2607.18161) 已用 trajectory-guided minimization 与 DD-Hunk 做反事实删改，因此 rollback、powerset 与 ddmin 在本题只能生产标签，不能成为算法贡献。`schema-slot` 只是在 RACE-Bench Lite 上检查 issue+visible FTP 能否在不看 Gold Patch、Reference Reasoning、PTP 或官方结果时形成稳定 claim 的低成本 offline screen，不是第二个章节候选。

最大退化风险是所有 triangle 都只有正边：这时所谓 warrant closure 只是普通 minimum-claim coverage。80 题只能使用预冻结普通生成器产生的自然 agent patches 识别稳定的 `SUPPORT|REFUTE|MISSING`；正边可来自自然成功候选，计入机制门的负/拮抗边必须来自自然失败候选，`MISSING` 则表示无可识别效应，绝不能并入负类。synthetic rewire/sign-shuffle 只能作机制破坏消融，不能制造现象。暂存资格要求至少 25/80 题在**同一 claim/test** 下出现两个以上共同必要 hunk，而不是多个独立 claim 各自由单个 hunk 覆盖；至少 20/80 且横跨至少 4 个仓库出现稳定正边与负/拮抗边。机制层 `W` 不是两个任务标签的宽松交集：一题只有在**同一个 claim/test 分量**中同时存在上述 joint-necessary hunk 和自然 `SUPPORT+REFUTE/ANTAGONISTIC` 时才计入，门槛为至少 16/80 且覆盖至少 4 个仓库。仓库 held-out 三分类 macro-F1 至少 0.75；相对 generic minimum-claim coverage 与同参数图模型至少多解决 5/80，其中至少 3 个必须在 PTP 解锁前封存的同分量 edge-neutralization 后失去 official resolved；至少 8 个新增正确解不在任何 baseline completed-patch pool，其中至少 5 个的具体 hash 或对应选择必须被同分量 neutralization 消除。rewire 与 sign-shuffle 在 `W` 内各消掉至少一半增益，最强 posthoc verifier 仍不能追到只差 2 题以内。至少 64/80 个完整干预单元才具有否决资格；不足时记 INCONCLUSIVE。升格时未完成单元固定留在 80 分母且不算成功；KILL 时则全部按最有利于理论的潜在 `W`、自然负边与结果优势处理，只有这种保守界仍触发否决条件才可 KILL。其他未过升格门只维持 DEMOTE。设计稿可在这些门前完整落文；任何训练、经验结果、checkpoint 或章节贡献升格仍必须等待 `00F` 所保留的 pre-gate，失败则直接记为 NO-CANDIDATE。

### 5.4 论文三：反馈分支必须在执行前改写尾行动排序

P3 当前的理论实现链是：已持久化补丁快照上的任务义务—差分—实验触达图 → 类别与当前任务/补丁汇总发生交互的初始诊断 belief → 关系 world checkpoint 学习 $p_\theta(o\mid z,e,G_t)$ → 对每个候选实验枚举规范观测 likelihood，并把尾部结果用保持事件后验质量的 OtherBranch 合并 → 用同一概率模型形成 counterfactual Bayesian posterior $b^{e,o}$ → 计算义务差距变化 $\Delta d^{e,o}$ 与慢速目标 critic 上停止梯度的 Submit/ReturnToEdit/Handoff tail-action-gap → 概率聚合为候选特异的 $g_e^{FB}$ → 融入实验 action embedding → policy checkpoint 以 distributional CQL 在真实实验、ReturnToEdit、Submit 与 Handoff 之间学习序贯价值。每状态候选实验和每实验分支分别受冻结的 $E_{\max}$、$O_{\max}$ 约束，合并质量、近似误差和物理运行账必须随结果报告。

理论产生的方向冲突是：两个实验即使具有相同信息增益，也可能因其可能反馈把下一步推向不同的正确或危险尾行动而具有相反价值。因此 $g_e^{FB}$ 不是日志汇总或额外注意力，而是在动作执行前显式预演“观测—判断修正—目标差距—尾行动排序”；慢速目标 critic 与 stop-gradient 又避免 policy 用自己的即时输出循环定义输入。Mookerjee 1993、GOAL 与 Hosanagar 提供信息必须改变行动的规范边界，Mookerjee and Mannino 2000 已覆盖风险进入行动目标，故 AVEP 不能以 VOI、Bayes、CQL 或尾险本身主张新颖性。

现行强替代必须至少包括相同动作与预算的 flat-history POMDP、mean-value IQL/CQL、plain distributional CQL、no-branch-summary、同参数 direct-Q、IG-only、固定验证清单，以及 $T^3$/AReW、Agentic Rubrics、RETRACE 与 BCF 等直接威胁。只有关系 likelihood 与 Bayes 修正成立、IG 排序和 branch-tail 排序出现足够方向冲突、$g_e^{FB}$ 优于并在 neutralization 后失去其 held-family regret 增量，且该增量传到等墙钟软件结果，理论才带来“非该视角不易想到”的算法能力；否则 AVEP 应被 generic controller 否决。

## 六、应模仿的逐段论证动作

除继续逐段回读 ACAA 与 DSDL 外，每个理论驱动方法段还应完成以下五句功能。

1. **失败句。** 指出现有通用算法在何种具体情境下产生理论上错误的行为，而不只说性能不足。
2. **理论句。** 只陈述能够约束算法的理论命题，并清楚标出理论原文的适用边界。
3. **映射句。** 把理论实体与 Coding Agent 中的任务、服务、证据、行动或成本逐一对应。
4. **实现句。** 给出被理论改变的计算对象、约束、损失、搜索或停止规则，并解释为什么普通替代模型不会自动满足它。
5. **证伪句。** 立即给出方向性机制预测、等参数替代、组件消融和理论应失效的边界样本。

实证段不能只报告删除组件后总指标下降。至少同时报告理论中间量是否按预期变化、通用同参数替代能否复制该变化、理论最有利样本与理论边界样本是否出现预注册异质性，以及最终行动指标是否与相关性或预测精度发生理论预期的偏离。

## 七、最终借鉴次序

三篇写作仍以 ACAA 与 DSDL 为第一层逐段模板。算法内生机制的第二层参照按以下顺序使用。

- P1 先回读 Burton-Jones and Grange 与 Conversational Dashboards，冻结透明取得—表征忠实度—知情行动的构念边界；再回读 X-IM，落实表征缺口到来源约束 OT、残余与部件诊断；最后用 Mookerjee 1993、GOAL 2007 与 Hosanagar 约束一次补取/ACT-NOW 的行动价值。DLDE-MAB 只提供“理论进入监督、可行域和逐项消融”的实现范式，不替 EUMN 推导具体张量。
- P2 先回读 G-FINDER 的 Toulmin/结构平衡操作化与 TheoryOn 的标签本体，再以 DSDL/ACAA 对齐理论—标签—loss—hunk 条件生成—新 patch—official outcome 单链。IBugFinder、TRIM、test augmentation、多位置生成和 posthoc verifier 是必须先压过的直接技术边界；非线性 TTF、Shaft and Vessey、Hosanagar、Schema 与 GDCM 只保留为旧路线或弱实现边界。该顺序不改变 OIWG 的 **DEMOTE / DESIGN-ONLY / NO-RUN** 身份。
- P3 先回读 Burton-Jones and Grange 的反馈控制边界，再用 Mookerjee 1993、GOAL 2007 与 Hosanagar 规定信息何时值得取得，并用 Mookerjee and Mannino 2000 约束风险必须进入真实行动目标；最后借 Consumer Acquisition 2024 的“规范模型—可观察量—估计—算法”单链组织 world likelihood → Bayes → $g_e^{FB}$ → distributional CQL。Mean-Risk 是现行强先例而非可声称的新颖模块，$T^3$/AReW、Agentic Rubrics、RETRACE、BCF 与 flat POMDP 承担更直接的否决责任。

弱例只用于划定底线：理论若只负责特征命名、模型选择或结果解释，不能写成 v3.1 的理论驱动算法贡献。
