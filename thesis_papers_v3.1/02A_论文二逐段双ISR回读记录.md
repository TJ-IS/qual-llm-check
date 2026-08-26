# 论文二逐段双 ISR 回读记录

本记录与 02_观察性干预warrant闭合的补丁生成.md 的 P01–P50 一一对应。ACAA 指 Chen et al.（2024）“Attending to Customer Attention”，权威全文为 database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md；DSDL 指 Chen et al.（2023）“A Theory-Driven Deep Learning Method for Voice Chat-Based Customer Response Prediction”，权威全文为 database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md。下列均为两份 Markdown 的物理行；回读只迁移句子功能和论证推进，不迁移其领域内容或措辞。现稿对应 00F 授权的完整可否决设计，现行治理状态仍为 DEMOTE / NO-RUN；截至写作时仍未运行，经验贡献尚未成立。

## P01

- **唯一科学功能：** 摘要建立“高价值补丁结果—补丁级分数压缩—理论中间状态—训练工件—生成期动作—外部证据—未运行边界”的完整承诺链。
- **ACAA 物理行与原段功能：** 第 29 行。S1 交代常用直接指标；S2 说明指标的预测失效；S3 引入 customer attention；S4 分解多粒度指标；S5 给出专门神经机制；S6 汇报终端与表示结果。
- **DSDL 物理行与原段功能：** 第 27 行。S1 建立业务机会；S2 锁定预测任务；S3 并置理论构念与深度模型；S4 列出三项理论学习责任；S5–S7 分别承担预测、协同表示和解释证据。
- **当前段 S1–S7：** S1 定位仓库补丁可靠性；S2 指出 patch-level score 压缩；S3 引入 Toulmin 与结构平衡并命名 OIWG；S4 列标签、损失和边界更新；S5 说明最弱 claim 进入生成；S6 交代 SWE-Gym/RACE 证据链；S7 明确未运行与零结果事实。
- **引用责任：** Toulmin、结构平衡的详细来源后置于理论段；摘要中的数据集只承担设计材料身份，不借用其结果为本文背书。
- **理论—算法映射：** claim–evidence–warrant→三类节点；结构平衡→signed triangle；未闭合 claim→hunk-boundary decode。
- **最强替代：** 普通等预算 beam 加 posthoc verifier；若它在同一 pool 内复制结果，摘要承诺失败。
- **回读修改：** 采用两篇来源的“构念先于组件”顺序，删除效果形容词和任何自有数值，末句加入资产缺失与尚未运行的事实。

## P02

- **唯一科学功能：** 从仓库级代理扩展建立补丁正确性的外部决策杠杆。
- **ACAA 物理行与原段功能：** 第 39 行。S1 定位评论渠道；S2 连接购买意愿；S3 推出销售预测潜力；S4 说明经营价值；S5 以传统变量对比凸显独特信息。
- **DSDL 物理行与原段功能：** 第 35 行。S1 建立数字互动模式；S2–S3 说明互动能力；S4 连接机会；S5 收束经营结果。
- **当前段 S1–S5：** S1 定位代理的软件行动身份；S2 说明功能添加的多重正确性；S3 用 RACE 给出任务规模与可执行结果；S4 用 SWE-RPG 给出隐含需求瓶颈；S5 连接返工、审查和交付风险。
- **引用责任：** Jimenez et al. 承担真实仓库任务背景；Liu et al. 承担 RACE 规模与报告范围；Zhou et al. 承担 SWE-RPG 的需求诊断。
- **理论—算法映射：** 外部软件结果被固定为最终杠杆，防止中间 edge F1 取代 patch correctness。
- **最强替代：** 只改善需求解释或中间推理的诊断器；它若不改变 patch 与官方结果，不足以回答本段。
- **回读修改：** 像 ACAA/DSDL 一样把技术扩展落到可分配的组织后果，未提前介绍图模型。

## P03

- **唯一科学功能：** 展开 issue→多 hunk→测试观察→搜索选择的现实生成流程。
- **ACAA 物理行与原段功能：** 第 41 行。S1 给出纳入全部评论的直接方案；S2 用有限感知说明偏差；S3–S5 从数据处理解释不足；S6 从模型区分解释不足。
- **DSDL 物理行与原段功能：** 第 37 行。先界定业务情境，再按参与者和操作次序展开流程，最后说明过程能力。
- **当前段 S1–S5：** S1 给出任务起点；S2 说明 hunk 与 coalition；S3 说明可见测试的多义通过；S4 区分 likelihood、test feedback 与 verifier；S5 收束三类对象未被联合表示。
- **引用责任：** 本段描述一般工作流，不使用文献数值；后续文献段分别支持三类方法能力。
- **理论—算法映射：** 现实流程直接产生 claim、hunk/coalition、test 三类节点及生成时点。
- **最强替代：** patch–test 二元矩阵；若它足以表达全部流程差异，三元图没有必要。
- **回读修改：** 采用 DSDL 的过程叙述和 ACAA 的直接方案转折，把问题从抽象“理解不足”落到三个明确压缩位置。

## P04

- **唯一科学功能：** 从可见通过、似然与 verifier 的直接指标推导“方向错误”而非普通精度不足。
- **ACAA 物理行与原段功能：** 第 45 行。S1–S2 归纳已有价值指标；S3 区分内容指标与影响；S4–S5 用偏好异质解释差异；S6 以冲突发现收束。
- **DSDL 物理行与原段功能：** 第 43 行。S1 列相近预测任务；S2 提出能力缺口；S3–S4 从信息前提与数据形态解释不适配。
- **当前段 S1–S5：** S1 给出三种直接代理；S2 用 RACE 的失败类型建立断层；S3 引入测试增强与共演化；S4 指出其 patch-level 压缩；S5 提出“更多通过却留下负/空 claim”的反向目标。
- **引用责任：** Liu et al. 支持 apply-success/test-fail 的推理差异；Li、Nashid、Ahmed 分别支持约束共演化与 issue-to-test 能力。
- **理论—算法映射：** 方向错误→REFUTE 与 hard-negative margin，而不是仅增加正 coverage。
- **最强替代：** 更多或更好测试；若测试增强本身消除方向错误，signed loss 不具独立作用。
- **回读修改：** 按 ACAA 的“直接指标—冲突机制”组织，避免笼统宣称现有研究失败。

## P05

- **唯一科学功能：** 以三类能力边界精确定义本文必须超越的结果。
- **ACAA 物理行与原段功能：** 第 85 行总领缺口，分别指出数据能力与差异化建模不足，再由比较表定位方法。
- **DSDL 物理行与原段功能：** 第 75 行总领情境缺口，从复杂数据和理论—深度学习合成两方面收束。
- **当前段 S1–S5：** S1 宣布三能力群；S2 归纳多 hunk/关系化生成；S3 归纳 subset/minimization；S4 归纳 verifier；S5 定义生成期新 patch 的窄缺口。
- **引用责任：** 五项最新生成工作、IBugFinder、TRIM、SpecRover 与 SWE-Gym 分别只承担真实能力边界，不被描述为弱方法。
- **理论—算法映射：** “生成而非排序”预先约束 hunk-boundary decoder 和 completed-patch-pool 评价。
- **最强替代：** MultiFixer/SynFix 类关系生成器与最强 verifier 的组合。
- **回读修改：** 将优先权防御改成能力分工，末句用可观察新 patch 结果收束。

## P06

- **唯一科学功能：** 用 Toulmin 结构定义 claim、observation、implementation backing 与 warrant 的非同一关系。
- **ACAA 物理行与原段功能：** 第 47 行以行为过程维度定位构念并从遗漏阶段推出新理论对象。
- **DSDL 物理行与原段功能：** 第 45 行引出理论指导，定位 satisfaction，并连接 experience、expectation 与 disconfirmation。
- **当前段 S1–S5：** S1 引出 Toulmin；S2 定义 claim 和 executable evidence；S3 明确 hunk 是 backing 而非字面 warrant；S4 说明孤立通过不足；S5 推出三类对象。
- **引用责任：** Toulmin 1958 承担论证角色的原始定义；任何软件因果主张均未交给该理论承担。
- **理论—算法映射：** 理论角色→typed node ontology 与 claim–test、coalition–test、coalition–claim 三边。
- **最强替代：** 把 claim 文本拼接到 patch encoder；该做法没有角色分离和边责任。
- **回读修改：** 依据 DSDL 的“构念—邻接构念—关系”写法，显式消除“hunk 就是 warrant”的概念偷换。

## P07

- **唯一科学功能：** 从结构平衡推导有符号三角及其与普通目标相反的搜索方向。
- **ACAA 物理行与原段功能：** 第 49–51 行先分解粒度，再归纳四项注意方向并提出研究问题。
- **DSDL 物理行与原段功能：** 第 47–49 行从构念动态、异质与多视图属性推出专门表示。
- **当前段 S1–S5：** S1 引入结构平衡与 G-FINDER；S2 定义三边；S3 给出正乘积闭合；S4 给出负乘积或缺边；S5 推出自然硬负例和反向搜索。
- **引用责任：** Cartwright and Harary 承担结构平衡原始关系约束；Lee and Ram 承担 Toulmin、指称与结构平衡如何形成 signed triangle 的直接 IS 先例。
- **理论—算法映射：** balance sign product→triangle loss；最弱负/空 claim→decode priority。
- **最强替代：** sign-agnostic GNN；其保持节点和参数但移除方向。
- **回读修改：** 像 ACAA/DSDL 一样在同段完成“理论属性—计算对象—行为后果”，未把 GNN 名称当理论贡献。

## P08

- **唯一科学功能：** 以四个递进问题锁定现象、可学习性、生成新颖性与外部归因。
- **ACAA 物理行与原段功能：** 第 51、53 行先归纳构念指标，再提出如何利用构念的 RQ 并预告方法回应。
- **DSDL 物理行与原段功能：** 第 49、51 行由数据结构提出跨视图 RQ，再由潜变量标签困难提出理论驱动学习 RQ。
- **当前段 S1–S4：** S1 询问自然 signed-joint 频率；S2 询问仓库留出边学习；S3 询问 pool 外新正确 patch；S4 询问官方结果及 edge 破坏归因。
- **引用责任：** 本段不增加新引文；问题中的术语均已由 P05–P07 的文献和理论承担。
- **理论—算法映射：** 四个 RQ 分别对应 W 现象门、edge head、decoder、neutralization/rewire。
- **最强替代：** 只报告 F1 或 visible FTP 的研究问题集合。
- **回读修改：** 将原本可能分散的多个算法问题压缩为从存在性到外部软件结果的单链。

## P09

- **唯一科学功能：** 用一条端到端前向链概览 OIWG 的五项工件。
- **ACAA 物理行与原段功能：** 第 53、55 行从理论指标进入 DTV-AMI，两类组件逐项实现指标并连接数据与结果。
- **DSDL 物理行与原段功能：** 第 53 行命名 DSDL，列出三个协同组件，再交代预测与解释证据。
- **当前段 S1–S5：** S1 constructor/alignment；S2 atomizer/runner；S3 graph/heads/recurrence；S4 joint training；S5 constrained decode 与 abstain。
- **引用责任：** 本段只总览已定义对象，组件来源和实现细节后置。
- **理论—算法映射：** 五步严格按 claim→observation→signed state→learning→action 排列。
- **最强替代：** 生成后才构图的解释器；它无法影响 S5 的 token 分布。
- **回读修改：** 采用两篇 ISR “一理论属性一机制”的鸟瞰方式，移除数据泄漏与算力细节。

## P10

- **唯一科学功能：** 交代训练、外测、封存次序、立章责任和当前未执行事实。
- **ACAA 物理行与原段功能：** 第 55 行先展开组件，再以案例数据和两类结果完成经验承诺。
- **DSDL 物理行与原段功能：** 第 53 行在方法总览后依次承担预测、理论表示和解释证据。
- **当前段 S1–S5：** S1 分配 SWE-Gym；S2 分配 SWE-RPG；S3 分配 RACE 20+80 与 hidden PTP；S4 给出四项同时成立的章节责任；S5 说明资产缺失与设计口径。
- **引用责任：** Pan 和 Zhou 只支持公开资产身份；RACE 的可见性责任由 Liu et al. 及后文协议定义共同承担。
- **理论—算法映射：** 训练 edge supervision 与最终 official outcome 分离，防止理论标签和终端结果循环。
- **最强替代：** 在同题 gold patch 或 hidden PTP 上训练；该方案被泄漏边界排除。
- **回读修改：** 用“待执行设计”替代来源中的经验结果预告，并在正文不用内部治理标签而完整陈述事实。

## P11

- **唯一科学功能：** 按终端评价、训练环境与中间需求参照三项能力组织公开 benchmark。
- **ACAA 物理行与原段功能：** 第 61、71 行分别说明评论影响机制和从传统变量到评论数据的预测能力。
- **DSDL 物理行与原段功能：** 第 63、69 行按量化特征、多模态数据和深度学习能力累积相关研究。
- **当前段 S1–S4：** S1 SWE-bench/SWE-Gym；S2 RACE；S3 SWE-RPG；S4 汇总外部结果与中间诊断双层基础。
- **引用责任：** 四个 benchmark 的规模、任务和公开能力均由其原始论文承担。
- **理论—算法映射：** benchmark 能力决定 train/diagnose/test 三分，而不决定模型机制。
- **最强替代：** 只在 SWE-bench 最终 pass/fail 上评价；它缺少现象和归因材料。
- **回读修改：** 采用能力积累而非逐篇否定，明确中间 GT 不是部署输入。

## P12

- **唯一科学功能：** 定位测试增强、意图推断和 verifier 对 OIWG 的替代威胁。
- **ACAA 物理行与原段功能：** 第 71、79 行先说明新数据能力，再解释 attention 的权重、搜索与解释功能。
- **DSDL 物理行与原段功能：** 第 69、71 行从多模态深度方法进入理论构念和对比学习能力。
- **当前段 S1–S4：** S1 issue-to-test；S2 code/test coevolution；S3 intent reviewer 与 verifier；S4 定义可复制收益时的降格含义。
- **引用责任：** Nashid、Ahmed、Li、Ruan、Pan 分别承担对应系统的实际能力。
- **理论—算法映射：** 这些方法被映射为 test augmentation 或 posthoc selection 对照，不被混入 signed decoder。
- **最强替代：** Agent-CoEvo-style 搜索加 SpecRover/SWE-Gym verifier。
- **回读修改：** 把“现有方法没有”改为“已有能力在哪个时点作决策”，使缺口由生成时点建立。

## P13

- **唯一科学功能：** 证明关系图和 multi-hunk generation 已是强 prior，从而排除图拓扑式伪贡献。
- **ACAA 物理行与原段功能：** 第 85、87 行先总括缺口，再把一般 compatibility 的情境不适配翻译为专门运算。
- **DSDL 物理行与原段功能：** 第 75、77–79 行从理论—数据合成缺口进入个性化、动态和多视图能力。
- **当前段 S1–S5：** S1 MultiMend；S2 MultiFixer；S3 SynFix/CascadeFix；S4 SiblingRepair；S5 排除图和多 hunk 本身的新颖性。
- **引用责任：** 每项方法只按其论文报告的结构与任务描述，不把 Defects4J 结果直接外推到 RACE。
- **理论—算法映射：** 既有 relation graph 作为 sign-agnostic strong baseline；本文新增责任被限制为 natural signs、joint component、closure loss 和 generation。
- **最强替代：** SynFix-style relation graph 与 MultiFixer-style coordinator–proposer。
- **回读修改：** 将五项工作写成累积能力，末句才精确收束差异。

## P14

- **唯一科学功能：** 将 rollback、powerset 与 minimization 降为标签生产和强基线。
- **ACAA 物理行与原段功能：** 第 87 行从一般函数的情境不适配逐项推导必要设计差异。
- **DSDL 物理行与原段功能：** 第 75、79 行从缺口进入具体多视图和理论满意度能力。
- **当前段 S1–S4：** S1 IBugFinder；S2 TRIM；S3 RACE file ablation；S4 明确贡献排除和失败条件。
- **引用责任：** Xin et al. 承担 powerset、divisibility 和八关系；Mathai et al. 承担 trajectory minimization/DD-Hunk；Liu et al. 承担 file ablation。
- **理论—算法映射：** partial-patch matrix 只产生观察边和 relation status，不进入贡献句。
- **最强替代：** IBugFinder exhaustive subset 与 TRIM-style ddmin。
- **回读修改：** 用 prior-art 的已实现能力划线，避免把工程复杂度误写成理论贡献。

## P15

- **唯一科学功能：** 从 Basket 理论驱动先例建立本文必须同时改变本体、结构、损失和推断的标准。
- **ACAA 物理行与原段功能：** 第 91、118 行先说明设计理据，再以理论—挑战—方案表汇总专门机制。
- **DSDL 物理行与原段功能：** 第 83、95、99 行从理论构念和动态形成机制推导方法责任，并汇总三项组件。
- **当前段 S1–S5：** S1 TheoryOn；S2 G-FINDER；S3 ACAA；S4 DSDL；S5 将先例压缩为可计算缺口。
- **引用责任：** Li、Lee and Ram、两篇 Chen 分别承担本体、signed triangle、注意机制、动态状态与损失的直接先例。
- **理论—算法映射：** 先例共同约束 labels/graph/loss/decode 四处改变，不能只加 theory feature。
- **最强替代：** 普通 patch scorer 加 claim embedding。
- **回读修改：** 使用 ACAA/DSDL 的“理论属性—专门运算”收束，避免借 Basket 论文为软件效果背书。

## P16

- **唯一科学功能：** 形式化可见输入、claim/test 规范边、coalition backing 与闭合含义。
- **ACAA 物理行与原段功能：** 第 91 行确定研究目标、设计理据和四项理论指标责任。
- **DSDL 物理行与原段功能：** 第 83 行把满意度连接结果并分解信息、传递与属性来源。
- **当前段 S1–S5：** S1 定义输入；S2 定义 claim；S3 定义 claim/test 边；S4 定义 hunk/coalition；S5 定义 closure 且重申 backing 不等于 warrant。
- **引用责任：** 本段符号是本文设计；概念责任回指 Toulmin，不声称形式等价。
- **理论—算法映射：** 领域角色直接决定 typed input tensors 和输出对象。
- **最强替代：** candidate×test 矩阵，缺少 claim 与 coalition 两个层次。
- **回读修改：** 先定义理论对象再给符号，保留语义边界句防止形式化越权。

## P17

- **唯一科学功能：** 用 theory-first ontology 固定 claim schema、mandatory mask 与不可观察状态。
- **ACAA 物理行与原段功能：** 第 93、95 行从过程先决作用推进到集合、子集、个体和元素粒度。
- **DSDL 物理行与原段功能：** 第 85 行定义 expectation、experience、disconfirmation 及方向后推出建模要求。
- **当前段 S1–S5：** S1 给 schema；S2 定义 mandatory；S3 定义 unresolved/unobserved；S4 划定 gold 禁区；S5 说明标签与终止条件被改变。
- **引用责任：** Li et al. 支持“本体先于模型”的设计范式；字段与 mask 是本文可证伪实现。
- **理论—算法映射：** claim ontology→constructor output、loss mask、terminal/abstain state。
- **最强替代：** 自由文本 rationale；它没有互斥状态和终止语义。
- **回读修改：** 将“无标签”拆成 MISSING、UNRESOLVED、UNOBSERVED，避免把认识缺失编码为负边。

## P18

- **唯一科学功能：** 给出 signed triangle 的观测符号、预测责任与平衡公式。
- **ACAA 物理行与原段功能：** 第 102、104 行从理论指标推出具体 attention 方向和运算。
- **DSDL 物理行与原段功能：** 第 91、93 行从信息/传递、多视图和无个人信息困难推出专门表示与对比目标。
- **当前段 S1–S5：** S1 定义 coalition/test 观察效应；S2 定义责任与平衡量；S3 解释正平衡；S4 解释负/缺失；S5 比较 all-positive coverage。
- **引用责任：** Cartwright–Harary 与 Lee–Ram 承担结构平衡来源；具体三元变量是本文操作化。
- **理论—算法映射：** sign product→balance loss 和 signed message feature。
- **最强替代：** sign-agnostic graph 及 all-positive claim coverage。
- **回读修改：** 公式前后均给变量语义，明确 MISSING 不进入正负乘积。

## P19

- **唯一科学功能：** 限定观察性干预的解释范围并保留联合、替代和基础设施状态。
- **ACAA 物理行与原段功能：** 第 106、108 行从异质偏好与冗余推出语义多样和互补注意。
- **DSDL 物理行与原段功能：** 第 93、95 行从隐含状态与动态累积推出交错表示和双向稀疏。
- **当前段 S1–S5：** S1 限定冻结条件；S2 列出不可排除原因；S3 固定边与关系状态；S4 定义 joint/substitutable；S5 把监督与官方语义结果分离。
- **引用责任：** Xin/Mathai 的 partial-patch 研究支持限制；语义因果否定由本文识别边界承担。
- **理论—算法映射：** coalition hyperedge 与 status head 处理 single-hunk 不能表达的关系。
- **最强替代：** generic hunk ablation/IBugFinder matrix。
- **回读修改：** 删除任何“证明 claim 成立”的措辞，统一改为 frozen-execution observed effect。

## P20

- **唯一科学功能：** 把理论转成四条可独立否决的预测。
- **ACAA 物理行与原段功能：** 第 110、112 行从 voting signal 推导权重方向和具体注意实现。
- **DSDL 物理行与原段功能：** 第 95 行把动态满意度映射到片段聚合与双向约束，并汇总理论—挑战—方案链。
- **当前段 S1–S4：** S1 自然负边/W；S2 edge learnability；S3 pool 外新 patch；S4 neutralization/rewire/sign-shuffle。
- **引用责任：** 命题阈值后置于实验；本段只给方向，不暗示结果。
- **理论—算法映射：** 每一命题对应现象、模型、行动、归因一个独立证据层。
- **最强替代：** 只做性能对比而不检查中间机制。
- **回读修改：** 每句写明失败时退化为何物，使理论不可通过事后解释逃避。

## P21

- **唯一科学功能：** 以表格闭合理论要求、计算对象、专门运算和最强反事实。
- **ACAA 物理行与原段功能：** 第 118 行汇总专门机制需求，并用表连接理论理据、方法挑战和方案。
- **DSDL 物理行与原段功能：** 第 95、99、103 行把理论基础、挑战、学习能力与组件逐项对齐。
- **当前段 S1–S5：** S1 labels；S2 representation；S3 learning；S4 inference；S5 规定四层与 official outcome 同时成立。
- **引用责任：** 表内无新增经验主张；替代物均由 P12–P14 的原始工作承担。
- **理论—算法映射：** 每行一个理论对象、一个运算和一个等参数或等输入反事实。
- **最强替代：** all-positive、sign-agnostic、independent ablation、posthoc verifier 的组合。
- **回读修改：** 移除模块营销语，把复杂性是否必要交给反事实和官方结果共同裁决。

## P22

- **唯一科学功能：** 定义部署输入输出、共享维度、可训练模块和最终 checkpoint 的端到端契约。
- **ACAA 物理行与原段功能：** 第 126 行由理论理据和挑战推出统一框架，再列四项注意机制的实现。
- **DSDL 物理行与原段功能：** 第 99 行连接理论分析与方法目标，列出三项学习能力并映射统一深度框架。
- **当前段 S1–S5：** S1 输入与 patch/abstain/state 输出；S2 7B base 与预注册替换；S3 LoRA/graph/GRU 规格；S4 hunk 边界注入；S5 合并可独立推断 checkpoint。
- **引用责任：** Qwen 起点只承担可行实现选择，不构成效果先验；模型 revision 必须由未来 manifest 给出。
- **理论—算法映射：** 理论状态位于语言模型下一 hunk 的 cross-attention，而非外置解释模块。
- **最强替代：** 同 base/LoRA 和参数量的 generic graph generator。
- **回读修改：** 按两篇来源的能力次序组织架构，并加入本地可训练、可加载这一实物责任。

## P23

- **唯一科学功能：** 把 gold-free claim 构造落实为有监督本地模型、schema mask 与可见 test aligner。
- **ACAA 物理行与原段功能：** 第 130 行依次定义预处理、预训练嵌入、平行表示、专门机制和下游用途。
- **DSDL 物理行与原段功能：** 第 109 行按分段、多视图特征、偏好模板、双路序列和最终输出形成前向链。
- **当前段 S1–S5：** S1 明确非提示词；S2 定义外部/弱监督；S3 finite-state schema；S4 biaffine aligner；S5 禁止 RACE reasoning 训练。
- **引用责任：** Zhou et al. 只支持公开 requirement-clarification 资产；弱对齐规则是本文实现责任。
- **理论—算法映射：** TheoryOn 式 ontology→有限状态输出；claim/test 规范关系→biaffine edge。
- **最强替代：** prompt-only claim extraction 或自由 rationale。
- **回读修改：** 增加 source span 和 unresolved 强约束，使 gold-free 可被机械检查。

## P24

- **唯一科学功能：** 将自然 patch 原子化、完整 coalition 与部署时无 rollback 的边界写成可执行算法。
- **ACAA 物理行与原段功能：** 第 134 行按应用实例、字段、有效单元、时序组织与实例形成展开预处理。
- **DSDL 物理行与原段功能：** 第 109、113 行先形成逐步计算链，再以双轨记录保持角色分离。
- **当前段 S1–S6：** S1 自然候选；S2 unified diff 与合并；S3 J≤4 全枚举；S4 J>4 不截断；S5 hunk/coalition 表示；S6 部署只编码 singleton 与由 frozen autoregressive pointer head 逐槽产生的至多 16 个 prefix coalition。
- **引用责任：** Xin/Mathai 承担 subset/minimization prior；具体 atomizer 规则需未来代码与测试固定。
- **理论—算法映射：** joint/substitutable→coalition hyperedge；observed intervention→训练 runner。
- **最强替代：** single-hunk ablation 与 IBugFinder exhaustive subset。
- **回读修改：** 将 J>4 明确为不可识别而非有利截断，并把部署 coalition 限为 hidden-state-only pointer top-16、递增成员 ID 与确定性破平，堵住选择性标签和部署 powerset 两个漏洞。

## P25

- **唯一科学功能：** 定义 signed warrant graph 的节点、边字段与训练/部署可见性差异。
- **ACAA 物理行与原段功能：** 第 143、153、159 行从输入、掩码和注意张量进入专门权重，并解释训练行为。
- **DSDL 物理行与原段功能：** 第 132、144 行由频率与顺序构造矩阵，再分别解释位置含义。
- **当前段 S1–S5：** S1 节点域；S2 静态边；S3 动态边及元数据；S4 predicted/observed 分离；S5 排除 reference-derived nodes。
- **引用责任：** 图字段是本文规格；RACE 可见性由 Liu et al. 原 benchmark 和冻结协议共同承担。
- **理论—算法映射：** claim/evidence/backing 角色→typed graph；missing/observed→独立 edge metadata。
- **最强替代：** candidate×test matrix 与普通 relation graph。
- **回读修改：** 显式加入 observed/predicted 标志，避免训练矩阵在部署中泄漏。

## P26

- **唯一科学功能：** 实现 type、direction、sign、observability 与 missing 语义分离的图消息传递。
- **ACAA 物理行与原段功能：** 第 173、175 行从双路表示进入协调训练，由成员关系和互补性推出专门 attention。
- **DSDL 物理行与原段功能：** 第 148、150、152 行构造双路网络、角色条件情形和跨序列 query-key 匹配。
- **当前段 S1–S5：** S1 类型投影；S2 typed signed attention 公式；S3 双向传播；S4 coalition 层；S5 保存可破坏机制参数。
- **引用责任：** attention 是通用运算，不作为理论贡献；关系字段来自前述理论映射。
- **理论—算法映射：** sign 与 epistemic missing 使用不同 embedding，防止“不知道=反驳”。
- **最强替代：** 同层数同参数 sign-agnostic message passing。
- **回读修改：** 给出完整张量责任并保留等参数替换接口。

## P27

- **唯一科学功能：** 将三类边、coalition 状态和 claim responsibility 变成独立监督头。
- **ACAA 物理行与原段功能：** 第 212、218、220 行定义输入输出、权重语义与最终训练目标。
- **DSDL 物理行与原段功能：** 第 156、158 行分别定义 expectation/experience 投影及权重角色。
- **当前段 S1–S6：** S1 edge-head input；S2 三分类公式；S3 status head 与 INFRA mask；S4 pointer proposal 的 teacher-forced joint/substitute targets；S5 responsibility head；S6 class balance 和逐类报告。
- **引用责任：** 分类本体由理论与执行定义承担，不用 hidden outcome 监督。
- **理论—算法映射：** SUPPORT/REFUTE/MISSING→softmax；joint/substitute→status head 与 bounded coalition proposal；signed backing→responsibility。
- **最强替代：** binary support/not-support 或把 MISSING 当 negative。
- **回读修改：** 将 INFRA 从语义类移为 execution mask；让 observed joint/substitute 监督部署 pointer；要求逐类指标防止 macro-F1 掩盖负边。

## P28

- **唯一科学功能：** 定义生成过程中可被后续 refute 重新打开的 claim closure 状态。
- **ACAA 物理行与原段功能：** 第 175、184、187 行从成员关系计算冗余、互补和最终权重。
- **DSDL 物理行与原段功能：** 第 156、187 行从理论投影形成动态潜变量，并由终端标签间接学习。
- **当前段 S1–S6：** S1 定义有界预测 coalition 集；S2 support aggregate；S3 refute/missing；S4 GRU 与 q 公式；S5 closed 标签；S6 比较非单调 recurrence 与累计 coverage。
- **引用责任：** closure 公式是本文推导；其结构理据来自 Toulmin/structural balance。
- **理论—算法映射：** warrant closure→claim-wise recurrent state；反驳→可逆转状态。
- **最强替代：** 单调 minimum-claim coverage。
- **回读修改：** 增加 joint coalition 只有共同出现后才闭合，并把公式中的全子集改成 P24 的有界预测集合，防止 independent-hunk shortcut 与部署时隐含 powerset。

## P29

- **唯一科学功能：** 把语言生成、边、结构平衡、闭合、硬负例与 hunk 动作写成联合训练目标。
- **ACAA 物理行与原段功能：** 第 220、224 行从表示聚合到预测损失和反向传播算法。
- **DSDL 物理行与原段功能：** 第 187、205、207–211 行由隐含理论状态进入对比与联合目标，并解释正则项。
- **当前段 S1–S5：** S1 总损失；S2 LM/edge 与 status+pointer；S3 balance/closure；S4 decode imitation；S5 仓库留出选择与多指标检查。
- **引用责任：** 所有 loss 为本文方法承诺；不借两篇 ISR 的效果，只借“构念进入目标”的设计逻辑。
- **理论—算法映射：** 三角→balance；mandatory claim→closure/hole；最弱状态→decode loss。
- **最强替代：** 相同训练数据的 plain LM、direct edge model 和 equal-param generic graph。
- **回读修改：** 不预写 lambda 数值，规定只能在 repo-held-out dev 选取并同时检查四类责任。

## P30

- **唯一科学功能：** 把“visible gain 但 refuted/unclosed”编码为自然 ranking hard negative，并定义公平替代。
- **ACAA 物理行与原段功能：** 第 175、187 行从互补关系计算专门权重并逐项解释参数。
- **DSDL 物理行与原段功能：** 第 189、192、195 行从属性/片段异质推导双向稀疏目标和参数作用。
- **当前段 S1–S4：** S1 定义 hard-negative 情形；S2 margin 公式；S3 gold 前配对；S4 两个 equal-param 替代及失败含义。
- **引用责任：** hard-negative 现象只由自然 visible matrix 定义，不使用 PTP。
- **理论—算法映射：** 方向错误→pairwise margin；理论复杂性→等参数替换消融。
- **最强替代：** all-positive GNN 与 direct three-class graph。
- **回读修改：** 加入同任务配对与 gold-before seal，避免用结果后挑选难例。

## P31

- **唯一科学功能：** 把最弱 claim 状态落实为下一 hunk token 分布与等预算 beam score。
- **ACAA 物理行与原段功能：** 第 212、220 行由双路表示和变化权重形成逐时点预测，再聚合最终目标。
- **DSDL 物理行与原段功能：** 第 199、205 行由理论生成的表示形成预测，并解释累计构念含义。
- **当前段 S1–S5：** S1 focus 公式；S2 cross-attention；S3 beam score；S4 仅 hunk boundary 更新；S5 等预算公平性与新 hash 来源。
- **引用责任：** decoder 是本文工件；beam 公平条件由实验协议承担。
- **理论—算法映射：** weakest-unclosed/refuted claim→focus attention 与 closure penalty。
- **最强替代：** ordinary/diverse/test-augmented beam 和完成后 reranker。
- **回读修改：** 明确 hunk 内标准 expansion、边界后才更新，保证训练原子和推断动作一致。

## P32

- **唯一科学功能：** 定义 EOS、ABSTAIN、部署步骤、审计输出与“真生成”判据。
- **ACAA 物理行与原段功能：** 第 220、224 行给出终端聚合、损失与完整训练/推断流程。
- **DSDL 物理行与原段功能：** 第 205、227 行把动态理论状态带入最终预测并说明优化产物。
- **当前段 S1–S6：** S1 EOS 门；S2 abstain；S3 六步推断；S4 禁止 powerset/matrix；S5 manifest；S6 cross-attention 先于 token 的生成判据。
- **引用责任：** 本段不声称 correctness guarantee；官方正确性后置 hidden evaluator。
- **理论—算法映射：** unclosed state→terminal action；focus state→pre-token generation。
- **最强替代：** posthoc verifier；其只能在 completed pool 中选择。
- **回读修改：** 加入无矩阵部署和输出 trace，使机制既不泄漏也可核查。

## P33

- **唯一科学功能：** 定义四阶段训练、仓库留出 checkpoint 选择与 RACE 零更新。
- **ACAA 物理行与原段功能：** 第 220、224 行把理论表示聚合为预测目标并通过训练算法联合学习。
- **DSDL 物理行与原段功能：** 第 205、207–211、227 行连接理论表示、联合目标与最终训练产物。
- **当前段 S1–S5：** S1 constructor；S2 graph/edge；S3 joint generator；S4 calibration；S5 多基线开发改善与 RACE 禁训。
- **引用责任：** SWE-RPG/SWE-Gym 的数据身份由原文承担；训练阶段是本文预注册。
- **理论—算法映射：** ontology、observed edges、joint loss、decision thresholds 分阶段但最终合并。
- **最强替代：** 下载作者模型或只训练 verifier；二者没有本地 theory-conditioned generator。
- **回读修改：** 要求真实 checkpoint、validation curve 和 hash，避免“理论模型”只存在于文字。

## P34

- **唯一科学功能：** 列出可复算、可继续训练的完整算法与数据工件。
- **ACAA 物理行与原段功能：** 第 224 行说明完整反向传播、算法步骤和组件更新。
- **DSDL 物理行与原段功能：** 第 219、227 行说明参数协同学习并同时产出理论表示和预测。
- **当前段 S1–S5：** S1 模型与 schema 包；S2 data/hash；S3 tensor/parameter export；S4 deterministic seed/hash；S5 排除提示词/API/解释记录。
- **引用责任：** 本段为复现责任，不含经验引文。
- **理论—算法映射：** 每个理论对象都有持久化 schema、weight、trace 或 threshold。
- **最强替代：** 仅发布 prompts、结果 CSV 或远程 API recipe。
- **回读修改：** 增加每层 artifact identity，使训练、推断和评价可独立重放。

## P35

- **唯一科学功能：** 界定 SWE-Gym、SWE-RPG 和 RACE 的训练/审计/外测分工与 family 隔离。
- **ACAA 物理行与原段功能：** 第 228、232 行先说明案例数据时期、规模和模态，再形成比较数据集与时间窗。
- **DSDL 物理行与原段功能：** 第 231、233 行定义实例、情境、标签、时间范围并构造分层数据集。
- **当前段 S1–S5：** S1 SWE-Gym 资产；S2 family 去重/RACE 排除；S3 SWE-RPG 责任；S4 version/license/hash；S5 污染时停止外测。
- **引用责任：** Pan/Zhou 提供公开规模和内容；overlap audit 是本文责任。
- **理论—算法映射：** edge learning 与 claim learning使用外部训练源，RACE 只承担独立 outcome。
- **最强替代：** 同仓库或同题 gold fine-tuning。
- **回读修改：** 将仓库去重前置到训练清单，避免任务级随机划分伪装外推。

## P36

- **唯一科学功能：** 固定自然候选选择、重复执行、三分类规则与 synthetic 排除。
- **ACAA 物理行与原段功能：** 第 232 行依据预测任务的动态性质构造一致比较数据与观测窗口。
- **DSDL 物理行与原段功能：** 第 233 行先定义全样本和子集，再依据类别与长度形成可比较支持。
- **当前段 S1–S6：** S1 K=4/top2；S2 全 coalition/双重复；S3 support；S4 refute；S5 missing；S6 natural-only 与消融边界。
- **引用责任：** 标签定义来自本文冻结协议；IBugFinder/TRIM 只支持为何要有 subset 强基线。
- **理论—算法映射：** 自然 fail→pass/pass→fail→signed supervision；不可识别→MISSING/INFRA。
- **最强替代：** gold patch deletion、manual bypass 或 synthetic negatives。
- **回读修改：** 明确候选按 beam rank 前置选择，堵住依据结果换位的选择偏差。

## P37

- **唯一科学功能：** 固定 RACE 20+80 分配和从主输出到 hidden evaluator 的不可逆封存顺序。
- **ACAA 物理行与原段功能：** 第 232 行先固定主任务、变量与三个时间窗，使比较单位在结果前确定。
- **DSDL 物理行与原段功能：** 第 231、233 行先定义实例与时间范围，再形成比较数据集。
- **当前段 S1–S5：** S1 SHA 分配；S2 20/80 责任；S3 主 claims/pools/traces seal；S4 visible matrix→W→neutralization seal；S5 20题 reasoning 仅后验 audit。
- **引用责任：** RACE asset identity 由 Liu et al.；split/seal 是本文预注册，不宣称已经生成 manifest。
- **理论—算法映射：** observation matrix 只在主生成后出现，确保 predicted edge 真正驱动部署。
- **最强替代：** 看过 hidden outcome 后选择 neutralization 或调阈值。
- **回读修改：** 将封存顺序写成单向事件链，消除 attribution 反向泄漏。

## P38

- **唯一科学功能：** 用白名单明确 claim、edge label、selection 与 official result 的信息防火墙。
- **ACAA 物理行与原段功能：** 第 134 行按数据字段、有效单元和实例形成固定可训练输入。
- **DSDL 物理行与原段功能：** 第 113 行界定共同样本前提、结果标签与双轨记录。
- **当前段 S1–S4：** S1 部署可见输入；S2 gold/hidden 禁区；S3 hidden 只判 outcome；S4 matrix 只 post-seal audit/target，部署读预测边。
- **引用责任：** benchmark 字段含义由 RACE；额外白名单和隔离由本文承担。
- **理论—算法映射：** claim-test 是可见规范，hunk-test observed matrix 是训练/审计，hunk-claim 是部署预测。
- **最强替代：** reference-derived changed-file/hunk supervision 或 hidden verifier。
- **回读修改：** 末句用三源分离概括防火墙，避免把 gold-free 只写成口号。

## P39

- **唯一科学功能：** 把四个 RQ 映射到现象、学习、生成与终端分析单位。
- **ACAA 物理行与原段功能：** 第 234、236 行先区分预测与表示责任，再按数据视图组织评价。
- **DSDL 物理行与原段功能：** 第 237、239 行区分终端预测与理论构念质量，并定义重复、指标与补充分析。
- **当前段 S1–S5：** S1 四类问题；S2 phenomenon unit；S3 learning/generation/outcome units；S4 各 RQ 指标；S5 80 分母与 repo cluster。
- **引用责任：** 单位和指标为预注册设计，不含经验结论。
- **理论—算法映射：** W、edge、decoder trace、official resolved 各拥有独立观察层。
- **最强替代：** 只以 task resolved 作为全部机制的单一代理。
- **回读修改：** 按两篇 ISR 的分层证据方式给每个问题唯一单位，防止层级混合。

## P40

- **唯一科学功能：** 建立包含最新直接威胁、复现身份和无矛盾算力账的完整强基线集合。
- **ACAA 物理行与原段功能：** 第 234 行按基础网络、兼容函数、注意头和多模态能力逐层选择对照。
- **DSDL 物理行与原段功能：** 第 237 行按基础序列、多视图、注意与对比学习能力组织十二个对照。
- **当前段 S1–S8：** S1 能力覆盖；S2 SWE-RPG 仅诊断；S3 current artifacts 均未忠实落地；S4 future faithful replacement rule；S5 以 G01–G15、P01–P03 与 V01 逐一锁定 19 个不可合并身份；S6 明确 G13、G14 与 G15 的主模型、生成期机制和归因责任；S7 将不超过 4,800+240 hashes、1,520 official method—task 单元与不超过 6,720 jobs 固定为现行前瞻容量账，并保留失败/缺失状态；S8 将旧 6,400 账限定为历史下限。
- **引用责任：** SWE-RPG、Agent-CoEvo、SynFix、CascadeFix、MultiFixer、SiblingRepair、IBugFinder、TRIM 的能力由各自原文承担；style 版本必须列差异。
- **理论—算法映射：** 每个理论组件都有同输入、同预算或同参数替代；最新方法检验通用关系/多 hunk 能否复制结果。
- **最强替代：** Agent-CoEvo-style + SynFix/MultiFixer-style + strongest verifier 的组合。
- **回读修改：** 新增 required eight，并发现原 15-method/6,400 账不能容纳四个独立生成臂；正文现以 19 个 ID 逐项给出类型与责任，使 15 个生成臂、3 个后处理器和 1 个 verifier 可由表格直接复算，再将 19/1,520/不超过 6,720 固定为现行前瞻容量账，把旧数记为历史下限，未修改 00D/00E。

## P41

- **唯一科学功能：** 把章节规模贡献压缩为同分量 W、可学习性、新生成、外部结果和机制归因的八项共同责任。
- **ACAA 物理行与原段功能：** 第 236、238 行分别比较预测与下游表示质量，使构念和终端证据共同承担结论。
- **DSDL 物理行与原段功能：** 第 239 行规定主辅指标、重复比较、显著性、敏感性和解释分析。
- **当前段 S1–S10：** S1 定义 W；S2 说明八项共同作用；S3–S10 依次给 25/80 joint、20/80 signs、16/80 W、F1 .75、+5/80 official 与3归因、8 novel 与5归因、两类破坏、verifier gap。
- **引用责任：** 阈值来自冻结设计，不由既有论文效果反推；所有自有计数仍为空。
- **理论—算法映射：** occurrence→learnability→generation→outcome→mechanism destruction 完整闭合。
- **最强替代：** generic coverage/graph 和 verifier 均写进数值门，不能只作弱比较。
- **回读修改：** 明确全过只恢复进一步研究资格，不把有界 80 题筛查写成完成章节。

## P42

- **唯一科学功能：** 定义 PTP 前 targeted neutralization 与逐构件消融的无泄漏归因。
- **ACAA 物理行与原段功能：** 第 290、292 行从训练机制参数返回理论 attention 模式并作构件比较。
- **DSDL 物理行与原段功能：** 第 299、301 行按理论主体组织重要性并比较动态构念演化。
- **当前段 S1–S5：** S1 seal timing；S2 same-component target selection；S3 same-budget neutralized decode；S4 outcome/patch attribution split；S5 seven ablations and intermediate-first checks。
- **引用责任：** 归因流程是本文预注册；不引用 hidden outcome 或结果后解释。
- **理论—算法映射：** signed component→targeted neutralization；triangle topology→rewire/shuffle；decode role→rerank replacement。
- **最强替代：** task-level random ablation 或看到 PTP 后选 edge。
- **回读修改：** 把归因臂计入生成预算，且要求 outcome-level resolved 真正消失，堵住只消 hash 的弱归因。

## P43

- **唯一科学功能：** 固定聚类推断、64/80 有效性、最有利理论补全和永久否决条件。
- **ACAA 物理行与原段功能：** 第 244 行规定独立运行、主辅指标与实现报告，使比较可重复。
- **DSDL 物理行与原段功能：** 第 239 行规定重复、稳健指标、显著性、参数与敏感性分析。
- **当前段 S1–S7：** S1 intervals/bootstrap；S2 Holm/hash unit；S3 64/80 validity；S4 continue-side missing failure；S5 kill-side favorable imputation；S6 CP/equivalence/no-new-patch conditions；S7 zero-negative 80/80 and no threshold drift。
- **引用责任：** Holm 1979 承担多重比较；其余是冻结统计映射。
- **理论—算法映射：** 不可识别不是负标签，也不能被方便地当作失败；不同决策方向使用相反保守补全。
- **最强替代：** complete-case analysis、换题补抽或点估计直接否决。
- **回读修改：** 保留 exact W 20% 和 equivalence [-.025,.025]；明确其他门失败只是不重新立章。

## P44

- **唯一科学功能：** 建立多维物理账、训练硬件计划和当前零资产/零执行事实。
- **ACAA 物理行与原段功能：** 第 244 行固定运行、指标和实现信息，保证每种设置可比较。
- **DSDL 物理行与原段功能：** 第 239 行同时交代重复、主辅指标、实现参数和敏感性。
- **当前段 S1–S5：** S1 event ledger；S2 不超过 6,720 的容量与 B_gen,total；S3 planned GPU form；S4 debug/training/infra dimensions；S5 enumerated missing assets and zero jobs。
- **引用责任：** 资源向量和硬件是设计估算责任，不冒充实测；实测值必须后续由 median/P95 给出。
- **理论—算法映射：** theory arms 的额外资源逐次收费，防止用更多 search budget 伪装机制收益。
- **最强替代：** 只报 GPU-hours 或把 deterministic jobs 与异质生成成本硬相加。
- **回读修改：** 未虚构 container-hour、GPU-hour 或货币数；明确现行工作区无法启动。

## P45

- **唯一科学功能：** 预先规定结果表、机制图与三种失败解释，防止结果后改故事。
- **ACAA 物理行与原段功能：** 第 242、244 行从多类表示协同进入独立运行与主辅结果报告。
- **DSDL 物理行与原段功能：** 第 243、249 行按数据条件汇总终端结果，再用独立下游能力评价表示。
- **当前段 S1–S5：** S1 five tables/two figures；S2 phenomenon/edge；S3 pools/outcome；S4 trace/frontier；S5 F1-only/new-only/no-ablation interpretation。
- **引用责任：** 本段只定义未来报告位，不填任何样本、效应或图。
- **理论—算法映射：** 每个图表对应 P20 一项命题和 P21 一行设计要求。
- **最强替代：** 只展示最佳 resolved 表或挑成功案例。
- **回读修改：** 结果解释在运行前固定，并把无归因外部增益判为非理论来源。

## P46

- **唯一科学功能：** 说明何种证据下论证理论才可能形成新的生成式 IS 计算单位。
- **ACAA 物理行与原段功能：** 第 318 行先概念化 customer attention，再分解指标、方法工件和经验认识三类贡献。
- **DSDL 物理行与原段功能：** 第 315 行以理论驱动方法为主贡献，列学习策略、工具价值和经验认识。
- **当前段 S1–S5：** S1 conditional opening；S2 Toulmin role as state；S3 balance directions；S4 joint/neutralization outcome link 与 ACAA/DSDL 类比；S5 failure invalidates contribution。
- **引用责任：** Chen 2024/2023 只承担“理论改变中间状态和机制”的参照，不为本文效果背书。
- **理论—算法映射：** claim/backing/observation 和 sign closure 只有在可训练、可破坏、可外化时才成为贡献。
- **最强替代：** 完成后自然语言 explanation 或普通 coverage state。
- **回读修改：** 全段使用条件式，不把设计完成写成理论贡献已成立。

## P47

- **唯一科学功能：** 集中陈述条件性方法/实践贡献，并用数值门回答“小题大做”。
- **ACAA 物理行与原段功能：** 第 318、335 行由方法工件进入需求理解、适配与平台应用含义。
- **DSDL 物理行与原段功能：** 第 315、329、331 行从学习机制进入工具价值、行动聚焦与理论—预测协同。
- **当前段 S1–S4：** S1 local generator identity；S2 four theory changes and artifacts；S3 practical outputs；S4 +5/80/8 hashes/attribution as complexity justification。
- **引用责任：** 阈值来自预注册，不写预期达到；应用含义明确依赖条件成立。
- **理论—算法映射：** label/graph/loss/decode 四处改变都对应一个可交付 artifact。
- **最强替代：** claim feature、dashboard 或 verifier；若只剩这些则不成章。
- **回读修改：** 直接写出“一两个重排任务=小题大做”，避免复杂模型自证贡献。

## P48

- **唯一科学功能：** 用观察单位、时点、输出和 checkpoint 划清三篇论文。
- **ACAA 物理行与原段功能：** 第 335 行从工具价值展开不同应用情境与使用责任。
- **DSDL 物理行与原段功能：** 第 331 行说明理论构念与预测协同如何产生不同洞见与行动价值。
- **当前段 S1–S5：** S1 P1 unit/output、一次补取或 ACT-NOW，以及首行动前冻结的 open-loop 计划边界；S2 P2 unit/input/output；S3 P3 在真实观测后重算动作的 closed-loop snapshot/action；S4 shared-only interfaces；S5 explicit exclusions。
- **引用责任：** 本段由系列现行定义承担，不使用外部文献。
- **理论—算法映射：** 本文只在 pre-patch generation 以 warrant state 改变 edit action。
- **最强替代：** source selection/router、online stop/test selection/handoff 的换名。
- **回读修改：** 写明 P1 只做一次证据补取且验证/提交至多属于事前冻结的 open-loop 骨架，P3 才在补丁持久化后依据真实观测重算实验/停止/转交；同时明确不加载相邻 checkpoint，避免系列共享理论被误作模型依赖。

## P49

- **唯一科学功能：** 集中界定因果、测试覆盖、coalition 上限、任务外推、监督与基线实现边界。
- **ACAA 物理行与原段功能：** 第 348 行按情境、数据跨度、模态、外部信息、参数和粒度集中讨论适用边界。
- **DSDL 物理行与原段功能：** 第 343 行按领域属性、数据覆盖、参数协同和后续行动讨论限制。
- **当前段 S1–S5：** S1 observed-not-causal；S2 visible/hidden roles；S3 J≤4/RACE scope；S4 claim/style bias；S5 80-screen needs independent confirmation。
- **引用责任：** 局限由设计本身推出，不以未来研究口号稀释。
- **理论—算法映射：** 每个限制对应 MISSING/UNOBSERVED/NON_IDENTIFIABLE/style 标志或外推边界。
- **最强替代：** 更强 test generation/multi-hunk agent/verifier 未来可能完全复制。
- **回读修改：** 将局限集中于一段，正文其他位置只保留必要识别边界。

## P50

- **唯一科学功能：** 以理论对象、四处算法改变、公开证据链、零结果事实和独立论文条件收束。
- **ACAA 物理行与原段功能：** 第 346 行回到研究对象，概括构念、机制与经验结果。
- **DSDL 物理行与原段功能：** 第 337、339 行重申理论驱动方法、应用任务和实际结果。
- **当前段 S1–S5：** S1 design identity；S2 labels/graph/loss/decode；S3 public train+RACE test；S4 current no assets/no findings；S5 new correct action as sole chapter condition。
- **引用责任：** 结论不新增文献、不复述任何自有结果。
- **理论—算法映射：** 从 Toulmin/structural balance 到 patch action 的完整链只以未来证据成立。
- **最强替代：** 所有前述 equal-budget/equal-parameter generation、minimization 与 verifier。
- **回读修改：** 将来源的结果式收束改成明确可证成/可否决的将来口径，并保留“未运行”事实。
