# 论文二逐段双 ISR 回读记录

本文件只记录正文实质段的最终对应关系。每块以 `S1...Sn` 严格对应该段按句号、问号或叹号划分的自然句，不以分号扩句；物理行号以冻结的本地 ACAA 与 DSDL Markdown 全文为准，每个正文段只保留一个当前审计块。

## 摘要

### 摘要—01—“自主编码代理能够”

- 严格 S 句（5句）：S1=界定可执行与语义连续性的冲突；S2=给出五维契约及三类 identifiability；S3=限定封闭 IR、可拒绝编译器和辅助头；S4=定义 canonical 序列训练及 ordinary-test+存在量词 PATCH 门，并规定 unknown/refuted 只使所属 bundle 失败；S5=冻结三类 family 隔离、评价层与结果责任。
- 引文功能与权威责任：摘要不配置作者—年份引文；所有现状、理论和方法责任在正文中由同行评议与官方 benchmark 来源承担。句5明确尚无结果，避免把设计写成发现。
- ACAA 回读：物理行29（正文行）。该行依次完成既有简化测量的局限、构念分解、专用深度学习方法和实证评价，是“冲突—构念—工件—证据”的摘要压缩。
- DSDL 回读：物理行27（正文行）。该行把理论构念、复杂数据、三个专用机制以及预测和解释证据串成一条链。
- 回读后修改：摘要把终端门统一为“全部 ordinary tests 通过且存在任一完整 bundle 通过才 PATCH”，unknown/refuted 仅否决其所属 bundle，ordinary tests 未全过、没有可通过 bundle 或编译域外均 abstain；末句仍保留研究设计责任。

## 1. 引言

### 引言—01—“组织越来越依赖”

- 严格 S 句（4句）：S1=建立流水线信息质量—系统使用—组织收益链；S2=界定用途依赖的数据质量；S3=用表征理论说明可运行但失真的行动后果；S4=收束到语义连续性的研究价值。
- 引文功能与权威责任：句1为 S，由 JMIS 的 IS 成功模型和数据仓库信息质量实证承担；句2为 D，由 JMIS/CACM 经典数据质量研究承担；句3为 D+C，由 ISR 表征理论承担；句4是前述证据的研究定位，不另引新事实。
- ACAA 回读：物理行39（正文行）。该行从信息渠道的组织价值推进到预测和运营价值，而非先介绍模型。
- DSDL 回读：物理行35、39（正文行）。行35建立数字化场景与商业机会，行39把预测能力落到有限资源下的行动配置。
- 回读后修改：把开头从“LLM 能生成 SQL”上移到信息质量—知情行动—组织收益链，并明确技术成功可能放大错误行动，形成 IS 问题而非单纯代码正确性问题。

### 引言—02—“大型语言模型驱动”

- 严格 S 句（4句）：S1=说明 coding-agent 能力跃迁；S2=界定数据工程相对一般代码任务的额外复杂性；S3=补充端到端数据密集 benchmark；S4=把技术变化落到跨下游决策的信息风险。
- 引文功能与权威责任：句1为 S，由 ICLR/NeurIPS 真实仓库 benchmark 与 agent 论文承担；句2为 S+C，由 Spider 2.0、ELT-Bench、DAComp 承担；句3为 S，由 KramaBench 和 ICML 2026 CoDA-Bench 承担；句4为问题推论。
- ACAA 回读：物理行41（正文行）。该行先承认现有研究能力，再分别从数据和模型侧限定其不足。
- DSDL 回读：物理行37、41（正文行）。行37具体描述新商业模式的参与者和流程，行41再指出该模式独有的数据挑战。
- 回读后修改：将 benchmark 按“通用 repo issue→企业 SQL workflow→端到端 pipeline/data discovery”递进，而非堆砌排行榜；末句明确为何这些能力会改变组织风险边界。

### 引言—03—“真正危险的补丁”

- 严格 S 句（5句）：S1=提出固定快照上的静默语义失真；S2=以 filter、aggregate 和 join 具体化 population/grain/multiplicity；S3=具体化 missingness meaning；S4=具体化 event/valid/availability time；S5=归纳结构检查与五维语义的错位。
- 引文功能与权威责任：句2为 D+C，由关系模型和数据库 provenance 原始研究承担；句3为 D，由 missing-data 经典理论承担；句4为 D+C，由 temporal database 权威来源承担；句1、5把定义应用到固定快照补丁。
- ACAA 回读：物理行43、45（正文行）。行43从决策机制推出应关注的对象，行45用相互冲突的例子证明简单指标不足。
- DSDL 回读：物理行43（正文行）。该行把相邻任务与焦点任务逐项比较，指出数据可得性和数据形式的根本不兼容。
- 回读后修改：没有用“semantic error”作抽象口号，而是逐类给出可执行但会改变决策含义的反例；末句明确共同的可见性冲突。

### 引言—04—“三类直觉方案”

- 严格 S 句（6句）：S1=总领三种替代；S2=限定 grammar 的保证对象；S3=限定 contract/proof 的形式化前提；S4=限定 CEGIS 与事后 verifier 的介入时点；S5=加入 PACT 并界定生成后检测、测试合成和提示增强的覆盖；S6=以 Verified 错误反驳 verifier-as-truth。
- 引文功能与权威责任：S2 为 M+C，由约束解码来源承担；S3 为 M，由程序逻辑与 contract 原始文献承担；S4 为 M+C，由 program synthesis 权威文献承担；S5 为 S+G，由 pipeline verifier、测试框架与 PACT 一手稿承担；S6 为 E+C，由 ELT-Bench-Verified 承担。
- ACAA 回读：物理行47、87（正文行）。行47说明只覆盖后续阶段的指标为何遗漏前置机制；行87逐项指出通用算子与理论指标的不兼容。
- DSDL 回读：物理行51（正文行）。该行比较两个直觉方向，指出缺少中间标签与黑箱重构之间的矛盾，再导向专用学习目标。
- 回读后修改：把“现有方法不行”拆为保证对象、介入时点和 oracle 可靠性三类限制，并纳入 PACT 的函数级 contract-adherence 边界；没有把 grammar、proof、PACT 或 verifier 写成失败方法。

### 引言—05—“本研究据此把”

- 严格 S 句（4句）：S1=把生成问题重述为中间表征；S2=连接表征理论、规则测量与 uncertainty；S3=从两篇 ISR 提取 theory-driven artifact 证据路径；S4=提出固定快照、五维状态、proof 与 abstention 均入界的 RQ。
- 引文功能与权威责任：句2为 D，由 ISR 表征理论与 DSS rule-based measurement 承担；句3为 M，由两篇 ISR 设计科学实证承担；句4是由冲突和理论共同导出的研究问题。
- ACAA 回读：物理行49、53（正文行）。行49完成构念分层并提出 RQ，行53将指标一一对应到专用机制。
- DSDL 回读：物理行45、47（正文行）。行45引入理论机制，行47把理论对象、数据缺失和专用表示连到 RQ。
- 回读后修改：明确研究不是让模型“理解语义”的泛化愿望，而是在 fixed snapshot 下学习生成时 Z/proof state，并对完整候选另估 `bar Z/s_Z`；RQ 同时规定单位、处理方式、终端输出与 abstention。

### 引言—06—“研究拟形成三项”

- 严格 S 句（5句）：S1=总领相互约束的贡献；S2=加入 contract partial identification 的理论边界；S3=映射封闭 IR、递归状态、bar Z/s_Z、proof 和偏好序列；S4=定义盲 evaluator、完整 identified bundle 成功门、无完整 bundle 的主指标排除与 coverage 保留；S5=把贡献绑定显式反馈的等预算增量。
- 引文功能与权威责任：句3为 M，由 ISR/MISQ 设计科学原始及权威发展文献承担；其他句是本研究拟检验的贡献，不引用不存在的结果。
- ACAA 回读：物理行55、318（正文行）。行55把每个构念对应到机制，行318按概念、方法和经验知识分层陈述贡献。
- DSDL 回读：物理行53、315（正文行）。行53汇总工件部件与证据，行315把主要贡献限定为 theory-driven methodological artifact。
- 回读后修改：贡献仍按“理论扩展—计算映射—确认性比较”三层组织，但补入 partial identification、完整 identified bundle 的存在门、无完整 bundle 的 coverage 责任和 auxiliary-only 反证；末句只在显式 feedback 产生等预算增量时承认机制，没有使用结果词。

## 2. 文献综述

### 文献综述—01—“代码生成研究已经”

- 严格 S 句（6句）：S1=界定代码生成向 repository editing 演进；S2=区分 token 生成与仓库任务；S3=综述三类神经修复；S4=说明参数高效适配；S5=指出测试代理的过拟合风险；S6=把风险限定到数据流水线语义。
- 引文功能与权威责任：句1为 S，由 SWE-bench 与 RepoBench 承担；句2为 S，由 Transformer 与 RepoBench 承担；句3为 S，由旗舰软件工程修复论文承担；句4为 M，由 RepairLLaMA 承担；句5为 C，由 program-repair 权威综述承担；句6提出本研究焦点。
- ACAA 回读：物理行69（标题行）、73（正文行）。标题定位预测方法研究流；行73按方法与信息类型综合经验工作，并保留信息之间的相互作用。
- DSDL 回读：物理行65（标题行）、69（正文行）。行69先综述多模态深度方法，再把黑箱与人工语义标注作为共同局限。
- 回读后修改：按“任务尺度—修复范式—参数适配—正确性代理”组织，而非按年代罗列；末句只提出数据语义的额外风险，不提前声称 SC-Coder 优效。

### 文献综述—02—“数据代理 benchmark”

- 严格 S 句（7句）：S1=引入相邻 benchmark；S2=评价 ELT-Bench 及其 Verified 纠错；S3=概括企业 SQL、dbt 和 repository 编辑；S4=加入 ADE-bench/DataClawEval 的 sandbox 与跨引擎外测；S5=区分 Krama 与 CoDA 的终端行动；S6=给出 annotation-error 证据；S7=锁定节点级五维回馈缺口。
- 引文功能与权威责任：S2 为 E+C；S3—S5 为 S+E，分别由 benchmark 论文或官方仓库承担；S6 为 C+E；S7 是对任务单位、行动和评价对象的交集判断。
- ACAA 回读：物理行61、71、85（正文行）。行61围绕信息质量组织影响机制，行71比较数据形态，行85从综述交集收束研究空缺。
- DSDL 回读：物理行57、63、75（正文行）。行57铺开场景文献，行63综合常用数据与方法，行75只保留与焦点方法相交的两项缺口。
- 回读后修改：新增 ADE-bench 与 DataClawEval 的真实外测入口，并明确 CoDA 是分析代码—最终答案而非 repo patch；仍只把共同缺口写成缺少节点级回馈状态，不按排行榜贬低资源。

### 文献综述—03—“IS 数据质量研究”

- 严格 S 句（5句）：S1=提出质量并非单维准确；S2=对照 consumer-based 与 ontological 传统；S3=说明情境化诊断测量；S4=给出 rule-based measurement 的谓词—capacity—uncertainty 结构；S5=提取尺度、分解和 unknown 三项纪律。
- 引文功能与权威责任：句1—2为 D，由 JMIS 与 CACM 奠基文献承担；句3为 M，由 AIMQ/CACM 方法承担；句4—5为 D+M，由 DSS 2019 原始框架承担。
- ACAA 回读：物理行91、93、100（正文行）。行91说明 design rationale 的责任，行93从理论过程确定构念位置，行100解释为何既有指标不能替代焦点指标。
- DSDL 回读：物理行83、85、89（正文行）。三行依次完成构念分解、形成机制和可计算任务归约。
- 回读后修改：将五维契约的理论根基写成“表征缺陷+用途依赖+规则测量”，并把 ordinal、hierarchical、uncertain 三项性质明确保留到后续模型，而非把理论压成一个总质量分数。

### 文献综述—04—“数据库研究提供了”

- 严格 S 句（6句）：S1=转入数据库可执行基础；S2=对应 grain 与 join lineage；S3=限定 cardinality estimation；S4=综述四类质量检测修复；S5=补充 GNN 质量工件；S6=界定 evaluator/基线与生成时状态学习的边界。
- 引文功能与权威责任：句2为 M，由 ICDE/TKDE/PODS provenance 与依赖文献承担；句3为 C+M，由 VLDB/学习型 cardinality 研究承担；句4为 S+M，由 SIGMOD/VLDB/KDD 工具承担；句5为 S，由 EDBT 直接近邻承担。
- ACAA 回读：物理行106、108（正文行）。行106从理论事实推出必要指标，行108对照通用兼容函数并导向专用算子。
- DSDL 回读：物理行91、93（正文行）。两行把构念的每个测量困难对应到特征、模板、注意机制和学习目标。
- 回读后修改：将数据库技术分别绑定到具体契约，而非笼统称为 data quality；末句明确生成时回馈的是 Z/proof state，完整候选的 `s_Z` 只承担校准诊断，不把不确定性写成证明。

### 文献综述—05—“结构化代码生成提供”

- 严格 S 句（5句）：S1=总领三个结构化生成工具族；S2=综述 text-to-SQL；S3=界定约束解码；S4=界定 synthesis/CEGIS/property testing；S5=说明可复用能力与不可替代的契约识别对象。
- 引文功能与权威责任：句2为 S，由 EMNLP/NeurIPS 数据集承担；句3为 M，由 PICARD 与 grammar decoding 承担；句4为 M，由 SyGuS、CEGIS 与 QuickCheck 原始文献承担；句5为 C+G。
- ACAA 回读：物理行79、81（正文行）。行79定义通用 attention 并解释可借用能力；行81明确“customer attention”不等于神经 attention。
- DSDL 回读：物理行67、71（正文行）。行67界定通用方法范围，行71说明为何针对理论对象修改学习方向。
- 回读后修改：明确 grammar、synthesis、testing 是三个不同保证层；仿照 ACAA 的构念—算子区分，强调“语义契约”不等于“语法约束”。

### 文献综述—06—“参数高效微调与”

- 严格 S 句（5句）：S1=引入参数高效训练与偏好工具；S2=说明 LoRA/QLoRA 的本地适配意义；S3=定义 DPO；S4=把偏好限定到同快照 property-world 支配；S5=分工 SFT/DPO 并排除 grammar-invalid 廉价负例。
- 引文功能与权威责任：句2为 M，由 ICLR/NeurIPS LoRA 与 QLoRA 承担；句3为 M，由 NeurIPS DPO 承担；句4—5是本研究的适配与边界。
- ACAA 回读：物理行126、173、220（正文行）。行126由设计理据导出组件，行173说明组件如何进入训练，行220把表示聚合到终端 loss。
- DSDL 回读：物理行99、187、221（正文行）。行99汇总专用机制，行187解释无中间真值时如何构造学习信号，行221引出联合目标。
- 回读后修改：把 DPO 偏好严格绑定为同任务、同快照、同 property worlds 下的契约支配；删除“LLM judge preference”等弱标签，并阻止 grammar-invalid 候选支配训练信号。

### 文献综述—07—“最接近本研究的”

- 严格 S 句（6句）：S1=定位 contract/verification 直接近邻；S2=概括 pipeline verifier、测试与 Verified；S3=界定 PACT 的函数级契约遵守；S4=界定 Chava 的 trust-carrying data object 与 obligation algebra；S5=把差异收窄为 repo-level IR 状态递归及同总预算比较；S6=设置 feedback 消融反证。
- 引文功能与权威责任：S2 为 S+E，由直接验证论文与 Verified benchmark 承担；S3 由 PACT 的 OpenReview 一手稿承担并保留其 withdrawn submission 状态；S4 由 Chava 的匿名 AIWare submission 承担，不写成已同行评议事实；S5—S6 是本研究的边界与可证伪承诺。
- ACAA 回读：物理行100、108、126（正文行）。行100从相邻内容指标中划出特定理论对象，行108把对象差异转为专用机制，行126由理论理据与方法挑战共同推出组件。
- DSDL 回读：物理行89、93、99（正文行）。行89归结理论任务，行93逐一应对测量困难，行99把理论挑战汇总为三个可计算机制。
- 回读后修改：新增 PACT 与 Chava 后删除宽泛“首次携带契约”主张；增量只剩 predicate state 是否真实反馈下一 IR 节点，并以 auxiliary-only、verifier-after-generation 和同总 FLOPs 作为反证。

### 文献综述—08—“这一边界也把”

- 严格 S 句（5句）：S1=提出与经典方法的边界；S2=逐项说明 CEGIS、grammar 与数据修复的保证对象；S3=说明 SC-Coder 复用 grammar/worlds/proof/CEGIS；S4=给出完整形式规范下 CEGIS 占优的退出条件；S5=限定为规范部分可观测且多解的静态任务。
- 引文功能与权威责任：句2为 D+M，由各方法原始或旗舰论文承担；句3为本研究机制边界；句4为可反驳的退出条件；句5为外部效度边界。
- ACAA 回读：物理行79、81、108（正文行）。行79先解释通用 attention 的能力，行81明示理论构念与神经算子不同，行108只在通用机制不足处设计专用兼容函数。
- DSDL 回读：物理行67、71、93（正文行）。行67界定通用机器学习，行71把通用对比学习按动态满意构念改造，行93为每项不可观测构念配置专用机制。
- 回读后修改：采用“复用通用工具—限定保证—指出专用学习对象”的写法；明确完整形式规范下 CEGIS 可以淘汰 SC-Coder，避免以深度模型天然优越为前提。

### 理论基础—01—“表征理论把信息”

- 严格 S 句（5句）：S1=陈述母理论链条；S2=共同界定 fixed domain 与 patch relation representation；S3=限制非人格化解释；S4=给出五维操作化与 artifact action；S5=排除测试代理和隐藏激活替代忠实度。
- 引文功能与权威责任：句1为 D，由 ISR 表征理论承担；句2—4是情境映射；句5是理论—测量边界。
- ACAA 回读：物理行87、91、93（正文行）。行91要求设计理据回答构念如何产生、为何充分、怎样指导机制，行93把过程阶段映射到研究对象；行87警惕通用算子与情境构念不兼容。
- DSDL 回读：物理行79、83、85（正文行）。行83界定焦点构念及属性，行85给出构念的形成链而非直接拿终端标签替代。
- 回读后修改：明确 domain、representation、artifact action 三者，且只把可验证的补丁关系映射为表征；未将代理拟人化，也未把隐藏激活直接命名为忠实度。

### 理论基础—02—“五类契约对应五”

- 严格 S 句（5句）：S1=总领五类失真；S2=依次定义五维；S3=限定可执行最小集合；S4=证明维度不可互换；S5=规定 not-applicable 与 unknown 的聚合纪律。
- 引文功能与权威责任：句1为 D，由 ontological data quality 与 rule-based measurement 承担；句2—3为 D+M，由关系模型、provenance、missing-data 与 temporal-database 奠基工作承担；句4—5是区分效度与聚合条件。
- ACAA 回读：物理行93、100、102（正文行）。行93先定过程与粒度框架，行100限定指标范围，行102逐项从理论推出独立指标。
- DSDL 回读：物理行83、85、89（正文行）。行83区分满意度属性，行85给出不同前因，行89再规定聚合而非先用单分数覆盖各构件。
- 回读后修改：逐维给出可执行含义，并明确不是完备数据质量本体；新增 not-applicable 规则，防止未知维度在聚合时被当成已满足。

### 理论基础—03—“对节点 v、叶谓词”

- 严格 S 句（5句）：S1=定义 M 次 Z、bar Z 与 D；S2=定义原始样本标准差 s_Z 并排除缩放、U head、后验和置信下界解释；S3=以静态 evaluator truth Q 规定 development 选 c_U、DPO 后 family-cluster conformal 校准及其交换性边界；S4=规定 capacity 与 hard necessary；S5=限定排序/abstention 用途并禁止分数提升 unknown。
- 引文功能与权威责任：S2 由 dataset-shift uncertainty 研究承担方法边界；S3 由 conformal prediction 权威综述承担校准逻辑；S4 由 rule-based data-quality 原始论文承担；其余为本研究的精确测量约定。
- ACAA 回读：物理行112、116、120（正文/表题行）。行112把方向明确的理论指标映射为权重方向，行116区分连续变化与通用融合，行120把指标集中列示以防构件混写。
- DSDL 回读：物理行170、176、187（正文/公式行）。行170解释属性权重，行176把 disconfirmation 显式张量化，行187在缺少直接真值时说明代理监督的理论依据。
- 回读后修改：把满足预测改为 `bar Z`、不稳定性改为未缩放的 `s_Z`，静态 evaluator truth 固定为 `Q`，删除 U head、[0,1] rescaling 与 lower-bound 说法；`c_U` 与 capacity 符号分离，并把 conformal 责任放在 DPO 后独立 calibration families。

### 理论基础—04—“契约携带生成的机制”

- 严格 S 句（5句）：S1=以公式给出 evidence→contract→连续 state recurrence，并规定 stable predicate_id、每个 RelNode 前插入、attention-only 状态、主 2×2 的 M_contract 全真及外部 proof 仅在完整候选后运行；S2=区分显式反馈与末端过滤/辅助预测；S3=提出匹配参数、FLOPs 和 calls 的 feedback 命题；S4=提出外部严格 DPO 与双层外切分命题；S5=规定中间—终端连接的反证条件。
- 引文功能与权威责任：本段是理论综合与研究命题，不借引文声称结果；其方法成分已由上一节原始文献界定。
- ACAA 回读：物理行126、128、130（正文/标题行）。行126由理论理据和方法挑战导出机制集合，行130按数据流顺序解释框架，并区分直接输出与中间表示用途。
- DSDL 回读：物理行99、101、103（正文/表格行）。行99逐项对应理论挑战与机制，行103以“理论基础—挑战—方案”矩阵防止组件无来由。
- 回读后修改：主实验的反馈只剩 stable predicate state token 进入下一 RelNode attention，`M_contract` 固定全真且生成期不调用外部 proof；外部 executor 只负责完整候选标签与 gate，避免把不可得 oracle 混进 recurrence。

### 方法—01—“一个训练或评价”

- 严格 S 句（6句）：S1=定义不可拆分 unit；S2=列出 snapshot、输入和唯一内部序列；S3=限定对外 patch/abstain 并禁止任意代码与 evaluator 修改；S4=收窄支持 artifact 与 DSL；S5=冻结跨篇独立 checkpoint 和外部标签；S6=枚举一般 Python/dbt 与动态任务的 Unsupported 边界。
- 引文功能与权威责任：本段是工件协议定义，不需要外部引文代替可复现约束。
- ACAA 回读：物理行128、130、132（标题/正文行）。行130从输入预处理到组件再到输出按顺序给出系统范围，行132转入可独立复现的首个输入模块。
- DSDL 回读：物理行105、107、109（正文/标题行）。行105先界定经验任务单位，行109列明输入、分段、特征、模块与最终输出。
- 回读后修改：在原 unit 与独立 checkpoint 基础上进一步把内部动作锁为 canonical IR/edit slots，外部只接受编译 patch 或带原因 abstain；将一般 Python、UDF、macro、hook 和动态任务明列为域外。

### 方法—02—“Contract bundle 由”

- 严格 S 句（8句）：S1=规定契约证据独立于模型；S2=冻结 source authority、provenance roots/hash 与独立证据规则，同实现派生物只算一源；S3=逐维列出叶谓词；S4=以 stable predicate_id 区分 scope/frontier、proof、identifiability 与 N/A；S5=规定双人提取、第三人按规则裁决及冲突 unresolved；S6=保存 set-valued bundles，定义完整独立识别集合 B_id，并把 C_common 降为报告量；S7=以存在一个完整 B_id bundle 且全部 necessary leaves satisfied 为主真值，无完整 bundle 排除 success 分母但保留 coverage；S8=由独立盲 evaluator 按 bundle 构造 worlds、报告 root/hash 和分歧并排除同源 oracle 自证。
- 引文功能与权威责任：本段把前述理论与数据库判定器转成标注协议；具体谓词的技术来源已在文献综述承担。
- ACAA 回读：物理行91、93、100（正文行）。行91要求说明指标怎样诱导及为何充分，行93按过程定位证据，行100明确被纳入和留给通用方法的信息。
- DSDL 回读：物理行83、89、93（正文行）。行83按理论属性拆构念，行89把构件聚合为任务，行93在个体信息缺失时保留专门估计路径而非伪造真值。
- 回读后修改：把证据独立性落实为 source-authority、provenance roots 与 hash，并规定同实现派生物不构成两源；新增 scope/frontier、完整 identified bundle 集 `B_id` 与存在量词 success gate，`C_common` 只报告，无完整 bundle 仍进入 unsupported/abstention coverage。

### 方法—03—“模型不直接生成”

- 严格 S 句（7句）：S1=完整产生 Program/Backend/ArtifactKind/Edit 与七类递归 RelExpr；S2=穷举 NamedExpr/Key/Order/Agg/Win/Expr/Pred/Type、typed literals 及函数 whitelist；S3=封闭 TestSpec/ConfigSpec/EditSlot/TypedPayload 与 lexical terminals，并规定 String 仅为 escaped typed literal；S4=逐算子冻结 schema/type rules 和 Unsupported 条件；S5=用稳定拓扑序及确定 tie-break 定义唯一 canonical sequence；S6=以显式 Backend/backend_revision 给出 SQL/dbt/DataFrame 编译映射；S7=不主张 soundness，只报告 closed-domain tested semantic conformance、coverage 与 Unsupported。
- 引文功能与权威责任：本段为工件结构定义；关系与约束语法的理论来源已在前文承担，本段不虚构实现结果。
- ACAA 回读：物理行130、132、136（正文/标题/图题行）。行130按输入、并行表示、机制和输出组织架构；标题与图题使模块边界可定位。
- DSDL 回读：物理行109、111、115（正文/标题/图题行）。行109依照真实处理顺序列出分段、表示、角色拆分、机制和预测，不以抽象框图替代数据流。
- 回读后修改：补齐 Backend、ArtifactKind、EditSlot、TypedPayload、`Type`、symbol/path/hash lexical terminals 与 backend revision，并统一 `cast(Type,Expr)`、`Null(Type)`，明确 String 只能是 typed literal；保证措辞降为 closed-domain tested semantic conformance，不再把有限测试称为 soundness。

### 方法—04—“每个 proof obligation”

- 严格 S 句（6句）：S1=给每个义务定义三类 scope 与 applicability frontier；S2=规定 frontier 前为 N/A，之后只预测 attention state 且 prefix 不调用外部 verifier；S3=逐算子给出 population/missingness/join/grain/time/schema 义务；S4=把完整 Program 后的静态与数据依赖义务分配给外部 verifier/盲 worlds；S5=规定 terminal unknown/refuted 仅使所属 bundle 失败，但 PATCH 仍同时要求候选级 G_test=1 与存在其他 H_b=1；S6=允许预测影响生成但禁止其自行 discharge。
- 引文功能与权威责任：句4为 M，由 property testing、SyGuS 与 provenance 原始工作承担；其余是本研究 proof interface。
- ACAA 回读：物理行102、108、112（正文行）。三行均按“理论性质—方法挑战—定向机制”逐指标展开，而非用一个共享黑箱替代。
- DSDL 回读：物理行91、93、101（正文/表题行）。行91和93分别把信息内容、属性、期望、经验与 disconfirmation 的困难映射到不同处理机制；表题集中显示对应关系。
- 回读后修改：保留 scope/frontier 但把外部 verifier 后移到完整 Program；生成期仅使用预测 state，terminal unknown/refuted 只否决所属 bundle，不能否决已经满足的另一完整 bundle，但 ordinary-test gate `G_test=1` 仍是 PATCH 的共同必要条件。

### 方法—05—“`SC-Coder-7B` 冻结”

- 严格 S 句（7句）：S1=冻结 Qwen revision、量化、七类 projection 的逐维 LoRA 账本及 100,925,440 参数；S2=说明 causal decoder 是唯一 canonical IR decoder；S3=以 stable predicate_id 绑定 variable-predicate scorer 并给出 h/e 交互和 Z/proof 方程；S4=显式给出 W_F/b_F 形状并逐矩阵闭合 1,857,797 个辅助参数及 102,783,237 总数；S5=规定每个 RelNode 前的 predicted state 仅入 attention、四格 M_contract 全真、gold 仅进 loss、外部 proof 仅进完整候选 gate；S6=固定 M=16 并把 dropout FLOPs 入账；S7=定义 SFT/DPO checkpoint 关系和复现实例。
- 引文功能与权威责任：句1为 M，由 LoRA/QLoRA 承担参数高效适配原理；具体规模和 checkpoint 是本研究预注册设计。
- ACAA 回读：物理行126、130、141（正文行）。行126枚举理论驱动组件，行130交代共享主干与机制位置，行141把输入 padding 与 mask 落到训练前处理。
- DSDL 回读：物理行99、109、120（正文行）。行99列出三个专用机制，行109给出它们在主干上的连接次序，行120明确训练输入 mask。
- 回读后修改：LoRA 只按正文已给出的七类 projection 维度展开，不另加 GQA/basis-decomposed 术语；辅助模块闭合到 102,783,237，主 2×2 的 state 只进 attention 且不读取生成时不可得的外部 proof。

### 方法—06—“监督阶段预先定义”

- 严格 S 句（7句）：S1=定义四格共同 `R_base` 与 supervision-on 的 `R_sup`，使 s 只切 L_Z/L_proof；S2=限定 operator/slot 为唯一 canonical sequence likelihood 并排除 patch/action；S3=限定 L_Z 仅用 fully independently identified 且已适用的静态二元标签 Q；S4=定义候选级 ordinary-test indicator G_test、完整候选 proof CE，并以冻结 tokenizer 和 PATCH/ABSTAIN 多 token sequence score 实现要求 G_test=1 的无新增参数 pre-conformal task-action loss；S5=规定 feedback 只切 predicted/null state tokens，四格 contract mask 全真；S6=删除 L_U/binned L_cal 并分离 development、DPO 后 calibration、confirmatory；S7=把 Brier/NLL/ECE 降为评价。
- 引文功能与权威责任：句3的 proper loss 由 scoring-rule 原始综述承担，句7的校准评价由 Brier 与现代 calibration 工作承担；其余是本研究 loss 的精确定义。
- ACAA 回读：物理行212、218、220（正文行）。行212定义自适应组合，行218解释可学习权重，行220明确终端聚合、loss 与场景理据。
- DSDL 回读：物理行211、219、221（正文行）。行211给出正则责任，行219解释可学习权重怎样联结黑箱预测与理论量，行221汇总整体优化目标。
- 回读后修改：task-action 移入四格共同 `R_base`，s 只切 L_Z/L_proof；action 以冻结字符串的多 token sequence score实现、无新增参数，标签在 conformal 前由完整候选 compiler、`G_test=1` 与 proof 共同生成，feedback 不再控制任何 proof mask。

### 方法—07—“困难负例只从可”

- 严格 S 句（5句）：S1=仅在闭包内 canonical IR 上列出单一类型保持变异；S2=规定负例必须 compiler→Patch、ordinary-test hard 且在 blind isolated world 违例；S3=规定正例也 compiler→Patch 且满足一个完整 B_id bundle；S4=剔除不可反解析、多维、语法、underidentified、不同 snapshot/compiler 或 evaluator-error 样本；S5=保存正负 canonical 序列、确定性 patches、双 family id/hash、首错和 traces。
- 引文功能与权威责任：句2为 M，由 mutation/metamorphic testing 综述承担；其余是本研究 hard-negative 协议。
- ACAA 回读：物理行173、179、185（正文/公式行）。行173把三个理论指标同时写入训练过程，随后的公式逐项保持输入来源。
- DSDL 回读：物理行187、189、195（正文行）。行187说明无直接中间标签时如何由理论关系构造对比信号，行189防止局部异质性破坏累计构念，行195明确标签极性与各正则责任。
- 回读后修改：把负例限制为封闭 grammar 的单一变异，并要求正负候选在同一 snapshot 都由 compiler 产生 Patch；正例须满足一个完整 B_id bundle，双 family id 与 generator/mutation hashes 冻结，使 DPO 标签与输出序列可一一复算。

### 方法—08—“DPO 阶段只令”

- 严格 S 句（6句）：S1=定义 `y=Canon(IR,slots)`、排除 action/surface patch、SFT reference 与 beta=0.1；S2=规定两个候选都在同 snapshot compiler→Patch 且共享外部标注；S3=定义 feasible-first 严格偏序并要求至少一个 necessary 或 advisory 维严格改善；S4=给出 supervision off/on 在两种 feedback 下的 `L_DPO+0.2R_base/R_sup`，四格共同保留 task-action；S5=切断 proof 自评与 calibration，把 task-action 限为 preference 外共同辅助监督，并规定终端由 `G_test·max_b H_b` hard rule 决定；S6=规定 DPO 后重算 bar Z/s_Z、重拟合 conformal并外切三类 families 及组合。
- 引文功能与权威责任：句1为 M，由 DPO 原始论文承担；支配、标签与切分规则是本研究约束。
- ACAA 回读：物理行220、224、228（正文行）。行220解释终端目标与替代聚合的差异，行224给出完整训练顺序，行228把数据边界落实到经验单位。
- DSDL 回读：物理行221、225、229（正文/公式/标题行）。整体 objective 在公式处冻结后才进入经验评价，保持训练目标与评价数据边界。
- 回读后修改：DPO sequence 仍不含 action，但 retention 改为四格共同 `R_base`、on 格 `R_sup`，保证 s 只切 Z/proof；task-action 是要求 `G_test=1` 的 pre-conformal 共同辅助 loss，终端由候选级 `G_test·max_{b∈B_id}H_b` hard rule 决定。

### 方法—09—“推理时模型在固定”

- 严格 S 句（7句）：S1=定义 canonical 候选、compiler、候选级 ordinary-test indicator G_test 与逐 bundle 隔离执行顺序；S2=以 bundle 内全部 necessary proof 与 conformal 单值集合定义 H_b，并以 `G_test·max_b H_b=1` 明确输出资格及 C_common 非 gate；S3=定义叶分数 q_p、bundle 分数 r_b=min 与候选 r=max，限定预测/校准责任；S4=区分无 B_id、G_test=0 与所有 bundle 失败的 abstain，并保留 coverage；S5=定义 gate 后 r/advisory 排序；S6=匹配 compiler policy、ordinary-test/完整-bundle gate、worlds、calls 和 FLOPs并限定可主张增量；S7=把 dropout、修复和失败编译入账后锁定 patch/abstain 动作域。
- 引文功能与权威责任：句3为 M，由 conformal 与 selective classification 原始工作承担；其余是本研究 action policy。
- ACAA 回读：物理行220、224、226（正文/标题行）。行220说明从表示到终端输出的聚合，行224给出实际推理前向与训练流程，之后才进入评价。
- DSDL 回读：物理行219、221、227（正文行）。行219解释中间量如何与终端预测结合，行227同时说明预测与中间评估的两个输出责任。
- 回读后修改：以 `G_test·max_{b∈B_id}H_b=1` 明确定义 ordinary-test+完整 identified bundle 的 proof/conformal hard gate，并把 `C_common` 降为报告量；聚合固定为叶 `q_p`、bundle `r_b=min`、候选 `r=max`，G_test=0 或无完整 bundle 均不能输出 PATCH且保留 abstention coverage。

### 数据与评价—01—“经验材料优先来自”

- 严格 S 句（7句）：S1=说明 public replayable task 原则；S2=限定 data-eng/ELT-Verified 训练池与 Spider/DAComp 上下文角色；S3=把 CoDA/Krama 降为 discovery stress test；S4=冻结 ADE-bench/DataClawEval 外测并把 Unsupported 留在分母；S5=先做 census，以可重放、编译支持、B_id 非空定义 success eligibility，无完整 bundle 仍保留 coverage/action；S6=限定 TPC worlds 用途；S7=冻结许可证、artifact hash、证据 roots/hash、B_id/C_common、IR 与日志字段。
- 引文功能与权威责任：句2—4为 E，由各 benchmark 论文与官方仓库分别承担；句5—7是本研究可执行筛选与复现协议。
- ACAA 回读：物理行226、228、230（标题/正文行）。行228精确说明任务、样本、时间边界和数据模态，之后再进入实验。
- DSDL 回读：物理行229、231、233（标题/正文行）。行231定义 instance、纳入流程、标签窗口和时期；行233说明派生子集逻辑。
- 回读后修改：把任务纳入改成先做全量 census，再用 `main_success_eligible` 区分完整 B_id bundle；无完整 bundle 不进确认性 success 分母但仍进入 abstention coverage/action 样本，并冻结证据 provenance-root hashes。

### 数据与评价—02—“切分在生成 mutation”

- 严格 S 句（7句）：S1=把 repo split 提前到派生前，冻结 ancestry closure、token-5gram MinHash Jaccard=0.80 与 clone 配置 hash；S2=给出五角色比例及确认性禁用项；S3=独立划分 mutation/generator families 与组合，并冻结 source/config/seed-bank hashes；S4=分开 development、DPO 后 calibration、confirmatory；S5=规定所有派生物、模板及同 provenance root 不得跨折；S6=由盲 evaluator 在冻结后生成、hash 并密封 worlds；S7=冻结 parser/compiler/container/clone/split/generator/evaluator hashes 并保留完全外测。
- 引文功能与权威责任：本段是预注册切分协议，不以外部引文代替具体防泄漏规则。
- ACAA 回读：物理行228、230、232（正文/标题行）。数据段先冻结时期与实例，主实验段再定义任务和多时间跨度数据集。
- DSDL 回读：物理行231、233、235（正文/标题行）。行231冻结标签窗口，行233说明所有派生子集都来自同一已界定总体，然后进入实验。
- 回读后修改：把 repository family 的 clone 合并规则冻结为可复算的 token-5gram MinHash Jaccard=0.80，并记录 detector/config hash；mutation/property-generator 的 source、config、seed-bank 与 confirmatory hidden generator 均按 family 冻结 hash，同 provenance root 也不得跨折。

### 数据与评价—03—“主比较在同一”

- 严格 S 句（7句）：S1=定义 supervision×feedback 的配对 2×2、参数/token 控制及架构外基线；S2=精确列出四格 SFT/DPO loss，四格共同保留 base action 且 s 只切 Z/proof；S3=规定 f 只切 predicted/null state tokens、四格 mask 全真，并把 mask-only 降为次级消融；S4=冻结三个训练 seed，在所有 families/四格共享设计并明确 seed×family crossed；S5=列出基线并共享逐 bundle worlds、完整 B_id gate、compiler/calls；S6=允许 repair/CEGIS 读取完整候选反馈并匹配 k/calls/FLOPs 或报告双 frontier；S7=限定 gate 前主张、交互项、次级消融和额外信息单列规则。
- 引文功能与权威责任：句5中的代理/修复参照由旗舰论文承担；其余为公平比较协议。
- ACAA 回读：物理行230、232、234（标题/正文行）。行232说明实验目的与输入因素，行234在共享 GRU 主干下比较兼容函数与多模态机制。
- DSDL 回读：物理行235、237、239（标题/正文行）。行237按通用主干、multiview、attention 与 contrastive 四类基线覆盖每项组件，行239冻结重复运行与实现披露。
- 回读后修改：四格改为共同 `R_base`、on 格 `R_sup`，所以 s 只切 Z/proof；f 只切 predicted/null state tokens，contract mask 在主实验恒为全真，seed 与 family 明确 crossed，mask-only 单列次级消融。

### 数据与评价—04—“主要终点是 complete-bundle”

- 严格 S 句（6句）：S1=把主终点限定到 B_id 非空任务、候选 G_test=1 及存在完整 H_b bundle，并把无完整 bundle留在 coverage；S2=拆开五维、定位、identifiability、C_common 与逐 bundle match；S3=分别评价 bar Z 与 raw s_Z；S4=以静态 evaluator truth Q 给出 K_cal≥9、family-max A_j、有限样本 k/q、Gamma 及非 proof 责任；S5=区分 eligible/all-task coverage 与成本；S6=规定 family 为最高独立单位，先聚合 family×seed×cell，再用 crossed seed effect 与 family bootstrap/层级模型。
- 引文功能与权威责任：句3由 calibration 与 uncertainty 研究承担预测量评价，句4由 conformal 权威综述承担有限样本校准逻辑；其余为本研究测量协议。
- ACAA 回读：物理行234、236、238（正文行）。主比较在预测终点之外单独检验 representation quality，且对输入与下游协议保持一致。
- DSDL 回读：物理行237、239、241（正文/标题行）。行237同时检验终端预测与理论中间量，行239明确重复、稳健指标与统计比较后才进入结果。
- 回读后修改：静态 evaluator truth 统一记为 `Q`，并补齐 `K_cal≥9`、family maxima、`k=ceil((K_cal+1)(1−alpha))` 与 `q=A_(k)`；seed 不再嵌套于 family，而以跨所有 families 的 crossed fixed effect进入层级模型。

### 数据与评价—05—“机制检验不从终端”

- 严格 S 句（6句）：S1=分开测量 predicted state/attention、完整候选 proof 与首错，并排除 prefix proof/mask；S2=比较四格下一算子分布与交互，把 mask-only 降为次级消融；S3=列出 repo/schema/mutation/generator/组合/Verified 稳健性；S4=在 ADE/DataClaw 全集报告外测并做污染审计；S5=比较 reference、描述性 C_common、逐 bundle 与 B_id-existence match；S6=以 feedback-off 和等 calls/FLOPs 的 rerank/repair 反证。
- 引文功能与权威责任：句3为 E+C，由 Verified 与 annotation-error 研究承担；其余为本研究机制检验协议。
- ACAA 回读：物理行238、240、242（正文行）。行238独立检验中间 representation，行240—242把各输入机制分实验后再检验组合增量。
- DSDL 回读：物理行239、241、243（正文/标题行）。行239预先列示主、稳健、解释和个案分析；结果段再按数据形态检验终端表现。
- 回读后修改：机制证据只把 predicted state token/attention 放进主 2×2，外部 proof 延后到完整候选，mask-only 单列次级消融；set-valued 诊断仍区分 reference/C_common/逐 bundle/B_id-existence。

### 贡献—01—“第一项理论贡献是”

- 严格 S 句（5句）：S1=定位可反驳的工件形成状态；S2=说明母理论并给出 independent evidence→partial contract→recurrent state→action 链；S3=界定 bar Z 与 s_Z 的不同认识地位；S4=列出识别、反馈、校准和等预算四类失效条件；S5=把贡献绑定构念与机制证据。
- 引文功能与权威责任：句2为 D，由 ISR 表征理论承担；其余是情境延伸与边界。
- ACAA 回读：物理行318、320、321（正文/图题/图像行）。行318将概念分解、方法工件与经验洞见分开陈述，行320—321给出中间机制的独立证据位置。
- DSDL 回读：物理行315、317、319（正文/图题行）。行315以理论驱动学习策略界定方法贡献，随后才转向管理洞见和中间构念图示。
- 回读后修改：理论延伸除固定工件阶段外，加入 contract partial identification；bar Z 是 identified leaf 的预测，s_Z 仅为 adapter 路径分散；新增“状态没有真正反馈”这一中央失效条件。

### 贡献—02—“第二项贡献是一个”

- 严格 S 句（4句）：S1=列出 canonical IR/state/bar Z-s_Z/proof/action/DPO/compiler 映射；S2=连接 design-science 并分开模块责任；S3=限定封闭 DSL 与 grammar/compiler/executor/CEGIS/repair 分工；S4=把增量限定到匹配 calls/FLOPs 的 gate 前质量、可观测性和拒答。
- 引文功能与权威责任：句2为 D+M，由 DSS/ISR/MISQ design-science 奠基工作承担；其余为工件贡献边界。
- ACAA 回读：物理行318、324、326（正文/图像相邻行）。行318把理论概念化、方法 artifact 和设计科学工具贡献分层，未用模型组件数量代替贡献。
- DSDL 回读：物理行315、321、323（正文/图像相邻行）。行315把专用学习策略、方法工具与经验洞见分开，避免一个“更准”覆盖全部贡献。
- 回读后修改：补齐 canonical sequence、可拒绝 compiler、递归状态和严格 DPO 的映射，并把程序合成范围明限于 relational subset/closed DataFrame DSL；等预算同时指 verifier calls 与总 FLOPs。

### 贡献—03—“第三项贡献是面向”

- 严格 S 句（6句）：S1=提出 property-centered protocol；S2=用独立 provenance roots、B_id、描述性 C_common、候选 G_test 与盲 evaluator 定义 ordinary-test+完整 bundle 验收；S3=限定 B_id 非空主指标、ordinary-test gate、逐 bundle 存在门、partial 敏感性与无完整 bundle coverage；S4=说明 compiler/ordinary-test/proof/首错/反例/未决证据；S5=列出独立核验、重放、DSL 和未来后果边界；S6=把角色限为静态关系变换候选与验收层。
- 引文功能与权威责任：句2为 E+C，由 Verified 与 annotation-error 研究承担；其余是本研究协议和实践边界。
- ACAA 回读：物理行318、328、329（正文/图题/图像行）。贡献段把经验洞见限定到可观测注意模式，并用专用机制图支持，不泛化为所有决策场景。
- DSDL 回读：物理行317、329、331（正文行）。管理洞见独立成段并由两类可读分析承担，提示实践主张不能只依赖终端预测。
- 回读后修改：用候选级 `G_test=1` 与 `B_id` 的完整 bundle 存在门替代交集 gate，`C_common` 仅作报告；ordinary tests 未全过或无完整 bundle 均不得 PATCH，后者排除确认性 success 分母但保留 coverage，实践输出继续提供 compiler、ordinary-test 与 proof evidence。

### 局限—01—“本研究至少有五项”

- 严格 S 句（7句）：S1=总领五项不可消除边界；S2=说明五维 underidentification、B_id 为空的主指标退出与 coverage 保留；S3=说明有限 worlds；S4=说明封闭 IR 的一般 Python/Jinja 覆盖损失；S5=说明三层 family holdout 的生态迁移与预训练污染边界；S6=说明 raw s_Z 与 family conformal 的交换性边界；S7=规定 identifiability、eligible/all-task coverage、unknown、外测 abstention 和区间报告。
- 引文功能与权威责任：句3为 C，由 program-repair 正确性综述承担；其余是本研究外部效度与测量限制。
- ACAA 回读：物理行344、348、350（标题/正文行）。行348按跨域、数据要求、遗漏因素、参数情境性和表示粒度逐项限制可部署性。
- DSDL 回读：物理行339、343、345（正文/标题行）。行343明确跨域属性、数据覆盖、调参过拟合和行为后果均未由预测实验解决。
- 回读后修改：局限明确 `B_id` 为空时退出确认性 success 分母但仍保留 coverage，并把外切分纠正为 repository/mutation/generator 三层；域外 Unsupported、underidentified tasks 与 family-wise conformal 边界均不以筛样隐藏。

### 结论—01—“本研究提出一种针对”

- 严格 S 句（4句）：S1=重述固定 snapshot 与封闭关系域；S2=概括 state attention、主实验全真 contract mask、完整候选 proof、Compile_b、候选级 G_test、`G_test·max_b H_b=1` gate 与 bundle-local unknown；S3=概括 independent roots/hash、描述性 C_common、闭包测试、三层切分、与 family crossed 的三 seed、外测及公平责任；S4=声明尚无结果并列完整 bundle、tested semantic conformance/coverage、feedback 增量和 finite-sample family-wise 校准条件。
- 引文功能与权威责任：结论不新增引文或结果，全部主张回扣正文已定义设计。
- ACAA 回读：物理行344、346、348（标题/正文行）。行346按概念、指标、机制、经验评价收束，行348紧接适用限制。
- DSDL 回读：物理行337、339、343（标题/正文行）。行339简洁重述 artifact 与经验责任，行343立即限制跨域和数据要求。
- 回读后修改：结论统一为只有 `G_test=1` 且任一 `H_b=1` 才 PATCH、unknown/refuted 只否决所属 bundle；主实验不再读取 proof mask，seed 与 family crossed，编译责任改称 closed-domain tested semantic conformance。

## 成稿机械核验与冻结

- 双 ISR 覆盖：正文参考文献前共有 38 个实质段、216 个严格 S 句，本文件共有 38 个唯一段落块且声明句数合计同为 216；每块各含一条 ACAA 和 DSDL 回读记录，共 76 条。重新读取两篇本地全文确认：ACAA 100 次行引用覆盖 58 个唯一物理行，DSDL 100 次覆盖 60 个唯一物理行，所指行均在界且非空。
- 引文：77 篇独立文献；author-year 机械匹配正文使用率 100%；其中 arXiv-only 8 篇。全文 216 句中 68 个引文句、71 个引用组，即 31.5%/32.9%；分节“引文句/引用组”比例依次为摘要 0.0%/0.0%、引言 60.7%/60.7%、文献综述 60.0%/66.7%、理论与设计理据 30.0%/30.0%、方法 11.9%/11.9%、数据与评价 21.2%/21.2%、贡献 20.0%/20.0%、局限 14.3%/14.3%、结论 0.0%/0.0%，均按 `00` 的同一分句与引用组口径复算。
- 文献组合：Basket 或同等权威 IS 来源仍为 9 篇，旗舰数据库、软件工程或机器学习方法超过 10 篇；直接近邻扩为 Spider 2.0、DAComp、ELT-Bench、ELT-Bench-Verified、CoDA-Bench、KramaBench、data-eng-bench、ADE-bench、DataClawEval、DQuaG、Veena（2026）、Gargouri and Reza（2026）、Jin et al.（2026）、PACT 与 Chava，共 15 项。
- 元数据：Spider 2.0 固定为 Lei et al. 2025a（ICLR 2025），DAComp 固定为 Lei et al. 2025b；PACT 明记为 ICLR 2026 withdrawn submission，Chava 明记为 submitted-to-AIWare 的匿名稿，ADE-bench 明记官方 GitHub 工件，DataClawEval 明记 arXiv:2607.28033，均不冒充已同行评议成果。
- 隐藏 micro-pilot：Full 训练前只在 pilot role 运行 30-task generation micro-pilot；主 success eligible 单元必须可由固定 container 重放、`B_id` 非空，并在盲 property worlds 上接受 `G_test=1` 且至少一个完整 bundle 的全部 necessary leaves，`B_id` 为空者仍保留 action/coverage。Canonical IR/edit slots→`Compile_b→Patch|Unsupported`、候选级 ordinary-test indicator G_test、单维 hard negative、完整候选后的外部 Z/proof labels、predicted-state attention feedback 与要求 `G_test=1` 的独立 pre-conformal task-level PATCH/ABSTAIN 必须端到端产出；任何调试、mutation template 或 property-generator template 不得进入 calibration、confirmatory 或外测 families。
- 实施判据：确认性比较必须在同一 canonical typed IR 下执行 node supervision×state feedback 的三 seed 配对 2×2；四格 SFT/DPO 均保留 `R_base=L_op+L_slot+L_task-action`，on 格使用 `R_sup=R_base+L_Z+L_proof`，使 s 只切 Z/proof，feedback 只切换 predicted/null state tokens，`M_contract` 恒为全真且只共享 `M_type`。Surface/grammar、mask-only、verifier-after-generation、generate–verify–repair、classical CEGIS 与 best-of-k 另列，底模 revision、训练 token、可训练参数、k、完整 bundle gate、verifier calls 和总模型 FLOPs 匹配或并列 frontier；统计先在 family×seed×cell 聚合，再以 repository family 为最高独立单位并把三个 seed 作为跨 family 的 crossed effect。
- 正文禁项：机械扫描未发现段落 marker、No-Go、内部资源门、跨篇 registry、正文审计话语或论文编号治理表述；success oracle 使用候选级 `G_test=1` 与完整 B_id bundle 的存在门且交集只报告，DPO sequence 未含 action，四格 retention 均含要求 G_test=1 的 pre-conformal task-action 而仅 off-cell 不含 Z/proof，连续 S 只进入 attention且不生成布尔 mask。静态 evaluator truth 只写作 `Q`，满足预测只写作 Z 或 `bar Z`，不稳定性只写作原始 `s_Z`，候选聚合固定为 `q_p→r_b=min→r=max`，未出现 `Z−κU`、选择性支持域或 terminal unknown 概率豁免。
- SHA-256 冻结：正文 raw bytes=`3910AF614CB852BB2368FFC176BD440626265B47F92E7F933297F444013170C0`；02A canonical UTF-8/LF=`0BC3908955CAFDE588FC85DC8CD110ED7B80BEC0706161F015E2D118AF033F03`；ACAA raw bytes=`22874E02E5DE71421110476BFC4B8E15FC80F86A1175D81A4FA3FCE7DF746239`；DSDL raw bytes=`1954CA69FF5750C7C8A0CD594C7772FABE9B9F69F84F253120D39DFC85259A2B`。02A canonical hash 的复算规则是先把本行 `02A canonical UTF-8/LF=` 后的 64 位十六进制值替换为 64 个 `0`，再将全文换行规范为 LF、以无 BOM UTF-8 编码后计算 SHA-256；该规则避免自引用 raw hash 不可能稳定的问题。
