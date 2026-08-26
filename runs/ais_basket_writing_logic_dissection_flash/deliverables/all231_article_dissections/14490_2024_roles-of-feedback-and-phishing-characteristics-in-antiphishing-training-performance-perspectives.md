# Roles of Feedback and Phishing Characteristics in Antiphishing Training Performance: Perspectives of Goal Setting and Skill Acquisition

- 作者：Shihe Pan; Dong-Heon Kwak; Jungwon Kuem; Sung S. Kim
- 年份 / 期刊：2024 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00854
- 源文件：14490_2024_roles-of-feedback-and-phishing-characteristics-in-antiphishing-training-performance-perspectives.md
- 论文主类型：multi_method_or_multi_study_program
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.85

## 文章级论证概况

- 核心问题：在反钓鱼培训中，反馈特征（类型、数量）、钓鱼邮件特征（线索显著性）和个体感知检测效能如何共同影响培训行为与绩效（决策回避与检测准确率），以及这些因素之间存在怎样的情境与交互效应？

- 制品与设计：本文的核心实验材料是反钓鱼培训反馈信息：对比基于示例的反馈（example-based feedback）与基于正念/抽象提醒的反馈（mindful feedback）；同时操纵反馈信息量（低 vs 高）和钓鱼邮件线索显著性（低 vs 高）。所有实验通过网页问卷和钓鱼邮件测验完成，邮件中的链接可悬停查看但不能点击。

- 客观结果：在链接嵌入型邮件情境下，示例式反馈比正念式反馈带来更高的检测准确率和更少的决策回避；感知检测效能显著降低决策回避并提高检测准确率；反馈数量本身无显著主效应，但与钓鱼线索显著性交互影响检测准确率；补充实验表明反馈类型的效果受邮件类型（链接嵌入 vs 无链接）调节。

- 核心贡献：作者声称以目标设定理论与技能获得理论为基础，构建并检验了一个同时包含反馈特征、钓鱼特征和感知检测效能的系统性模型；率先同时考察决策回避与检测准确率，揭示反馈类型的情境效应、感知检测效能与反馈类型的交互，以及反馈数量与钓鱼线索显著性的交互。

- 整篇论证链：论文从钓鱼攻击造成巨额损失和组织普遍提供安全意识培训这一现实出发，指出现有反钓鱼培训研究存在四个缺口：只关注检测准确率而忽视决策回避、反馈类型的情境效应不明、感知检测效能的直接效应未定、反馈特征与钓鱼特征/自我效能的交互缺乏检验。作者用目标设定理论把反馈、任务复杂性和自我效能整合为关键构念，用技能获得理论解释为什么具体、可程序化的示例式反馈应优于抽象的正念式反馈。四个网络实验依次检验：主效应（H1）、感知检测效能及其与反馈类型的交互（H2/H3）、反馈数量与线索显著性的主效应和交互（H4-H6），以及反馈类型在不同邮件类型下的边界（实验4）。结果支持大部分假设，但也显示反馈数量无主效应、感知检测效能的交互仅边缘显著；讨论据此返回理论，提出决策回避与检测准确率具有不同机制，并把边界条件声明为重要设计知识。

## 类型与写作弧线判定

- 论文主类型判定：该文不是单一理论推导制品实验、benchmark或现场平台实验，而是由四个不同设计的在线实验加操纵检验共同累积证据：实验1建立主效应，实验2检验个体与消息层面的自我效能机制，实验3检验消息层面交互，实验4补充边界条件；不同实验采用不同在线样本和不同分析方法，属于多研究程序型论证。

- 主导写作弧线判定：写作弧线从现实损失和文献缺口出发，引入目标设定理论和技能获得理论，提出研究模型和假设，设计四个实验，最后在讨论中把实证结果返回理论贡献、边界条件和实践启示，形成问题—理论—设计—检验—回到理论的闭环。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：四阶段按假设覆盖范围递进：实验1验证反馈类型主效应；实验2在重复测量设计中加入感知检测效能及其与反馈类型的交互；实验3转向反馈数量与钓鱼线索显著性的主效应和交互；实验4作为事后边界检验，引入无链接邮件类型，考察示例式反馈优势的适用边界。每个后续实验都承接前一个实验留下的未解问题。

### studies_or_phases

#### 1. 实验1：反馈类型对决策回避与检测准确率的主效应

- order：1

- name_cn：实验1：反馈类型对决策回避与检测准确率的主效应

- question_cn：在链接嵌入型邮件情境下，示例式反馈是否比正念式反馈更能减少决策回避并提高检测准确率（H1a/H1b）？

- inputs_and_setting_cn：130名Amazon Mechanical Turk美国参与者；基于网页的钓鱼测验；先完成预备测验，接受示例式或正念式反馈，再完成六封新邮件的正式测验。

- designed_or_compared_object_cn：反馈类型：示例式反馈（展示真实钓鱼邮件中的伪造链接并说明检测方法）对正念式反馈（提醒用户停下来思考、不要盲目行动）。

- baseline_control_or_counterfactual_cn：正念式反馈组作为参照，源于已有正念培训材料；控制变量包括年龄、性别、先前钓鱼经历、邮件负荷、预备测验准确率和三类应对方式。

##### objective_metrics

1. 决策回避：每封邮件选择跳过记为1，做出判断记为0，汇总0-6

2. 检测准确率：错误-1、跳过0、正确1，汇总-6到+6

- analysis_method_cn：ANCOVA；效果量报告partial η²；VIF多重共线性检验；非回应偏差检验；G*Power功效分析。

- main_result_cn：示例式反馈组的决策回避显著低于正念式反馈组（M=0.15 vs 0.46），检测准确率显著更高（M=4.10 vs 1.28），H1a和H1b获得支持；检测准确率的效果量为大效应。

- argumentative_role_cn：建立核心主张：在链接嵌入型邮件这一常见情境下，具体示例式反馈优于抽象正念式反馈。

- remaining_uncertainty_cn：未涉及个体效能、消息层面特征和反馈数量的作用；也未检验反馈类型在非链接邮件中的效果。

- link_to_next_phase_cn：实验2在相同反馈类型比较中加入感知检测效能，以考察个体差异及反馈类型与效能的交互。

##### evidence_pointers

1. 4.1.1 Treatment

2. 4.1.6 Results and Discussion

3. Table 3

4. Appendix C

#### 2. 实验2：感知检测效能及其与反馈类型的交互

- order：2

- name_cn：实验2：感知检测效能及其与反馈类型的交互

- question_cn：感知检测效能是否直接减少决策回避并提高检测准确率（H2a/H2b）？感知检测效能对检测准确率的效果是否在示例式反馈组更强（H3b）？

- inputs_and_setting_cn：110名来自Esearch.com在线样本的美国参与者；单因素重复测量设计，反馈类型为组间变量，感知检测效能和反应时为消息层重复测量；每人在正式测验中评价四封邮件并逐封报告感知检测效能。

- designed_or_compared_object_cn：反馈类型操纵同实验1；感知检测效能为消息层测量变量；比较不同反馈组中效能-结果关系。

- baseline_control_or_counterfactual_cn：正念式反馈组为基线；嵌套模型从仅含处理变量逐步加入效能、应对方式和人口控制变量。

##### objective_metrics

1. 决策回避：二元变量

2. 检测准确率：有序三分类变量（-1/0/1）

3. 感知检测效能：4条目7点量表

4. 反应时

- analysis_method_cn：广义估计方程（GEE）处理嵌套重复测量；针对决策回避使用QIC/QICC模型拟合；针对检测准确率使用Wald检验；CFA构念效度。

- main_result_cn：感知检测效能显著负向影响决策回避、显著正向影响检测准确率，H2a/H2b支持；反馈类型与感知检测效能的交互对检测准确率边缘显著（p=0.08），H3b边缘支持；反馈类型对决策回避的交互不显著。

- argumentative_role_cn：证明感知检测效能是独立于应对方式的关键决定因素，并初步表明示例式反馈有助于把效能转化为准确率。

- remaining_uncertainty_cn：尚未检验反馈数量、钓鱼线索显著性和二者交互；检测准确率的效能交互仅为边缘显著，需要谨慎解释。

- link_to_next_phase_cn：实验3把焦点从反馈类型转向反馈数量，并引入消息层面的钓鱼线索显著性，检验认知资源有限性如何调节训练效果。

##### evidence_pointers

1. 4.2.1 Treatment

2. 4.2.6 Generalized Estimating Equations

3. Table 4

4. Figure 3

#### 3. 实验3：反馈数量与钓鱼线索显著性的作用

- order：3

- name_cn：实验3：反馈数量与钓鱼线索显著性的作用

- question_cn：示例式反馈数量是否影响决策回避和检测准确率（H4a/H4b）？钓鱼线索显著性是否正向影响检测准确率（H5b）？反馈数量是否增强线索显著性对准确率的影响（H6b）？

- inputs_and_setting_cn：274名Amazon Mechanical Turk美国参与者（排除操纵检验失败者后）；2×2混合设计，反馈数量为组间变量，钓鱼线索显著性为组内变量；正式测验包含六封邮件，其中三封低线索显著、三封高线索显著。

- designed_or_compared_object_cn：反馈数量：低数量只说明伪造链接一个技巧，高数量说明伪造链接、伪造域名、泛称问候、紧迫语气等多个技巧；钓鱼线索显著性：低显著性仅含伪造链接，高显著性同时含伪造链接、可疑域名和另一类线索。

- baseline_control_or_counterfactual_cn：低反馈数量组和低线索显著性邮件作为参照；GEE嵌套模型逐步加入变量。

##### objective_metrics

1. 决策回避：二元

2. 检测准确率：有序三分类

3. 感知检测效能：消息层测量

4. 反应时

- analysis_method_cn：GEE；操纵检验用卡方检验；CFA；VIF；交互图。

- main_result_cn：反馈数量对决策回避和检测准确率均无显著主效应，H4未支持；钓鱼线索显著性正向影响检测准确率，H5支持；反馈数量与线索显著性的交互显著，线索显著性效应在高反馈数量条件下更强，H6支持。

- argumentative_role_cn：说明反馈数量不是越多越好，其作用通过交互机制出现；线索显著性作为任务复杂度反映确实影响绩效。

- remaining_uncertainty_cn：仍未知反馈类型在不同邮件类型（尤其无链接邮件）下是否保持优势；长期效果和真实邮件客户端行为未测。

- link_to_next_phase_cn：实验4作为事后补充，直接检验反馈类型×邮件类型，以明确实验1结论的边界。

##### evidence_pointers

1. 4.3.1 Treatment

2. 4.3.5 Manipulation Check

3. 4.3.7 Generalized Estimating Equations

4. Table 5

5. Figure 4

#### 4. 实验4：反馈类型与邮件类型的交互边界

- order：4

- name_cn：实验4：反馈类型与邮件类型的交互边界

- question_cn：示例式反馈相对正念式反馈的效果是否依赖邮件类型（链接嵌入 vs 无链接）？在遇到没有链接的新型钓鱼邮件时，示例式反馈是否仍占优？

- inputs_and_setting_cn：138名来自Clickworker.com的美国参与者；2×2组间设计：反馈类型（示例式 vs 正念式）×邮件类型（链接嵌入 vs 无链接）；正式测验六封邮件中三封钓鱼、三封合法。

- designed_or_compared_object_cn：反馈类型同前；邮件类型：链接嵌入邮件使用伪造/真实链接，无链接邮件通过伪造发件人、回复/电话诱导来钓鱼。

- baseline_control_or_counterfactual_cn：链接嵌入邮件与正念式反馈为参照；同时使用更严格的防机器人、注意力和先前测验经验筛选。

##### objective_metrics

1. 决策回避：选择“我不知道是否为钓鱼”记为1

2. 检测准确率：错误-1、不知道0、正确1

3. 感知检测效能：平均到个体层

4. 反应时

- analysis_method_cn：双因素ANCOVA；Bonferroni校正的事后比较；操纵检验；CFA。

- main_result_cn：反馈类型与邮件类型对决策回避和检测准确率均有显著交互：链接嵌入邮件下示例式反馈准确率显著更高；无链接邮件下两反馈组准确率无显著差异，且示例式反馈反而导致更多决策回避。

- argumentative_role_cn：为H1的核心结论设定边界条件，防止把示例式反馈优势过度泛化到所有钓鱼邮件。

- remaining_uncertainty_cn：只考察短期在线测验；未考察其他钓鱼形式（附件、下载等）、长期保持和真实点击行为。

- link_to_next_phase_cn：不再进入新的实验阶段；结果汇入讨论部分作为设计知识和理论边界。

##### evidence_pointers

1. 4.4.1 Treatment

2. 4.4.5 Manipulation Check

3. 4.4.7 Analysis of Covariance

4. Table 6

5. Figure 5

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 钓鱼攻击利用个体检测经验不足，需向员工提供反馈

2. GAP: 对何种反馈更有效知之甚少

3. RQ_OR_OBJECTIVE: 列出四个研究目标

4. THEORY_INTRO: 引入目标设定理论、技能获得理论和反钓鱼文献

5. STUDY_OVERVIEW: 四个实验、652名美国被试、三个在线样本库

6. RESULT: 示例式反馈优于抽象反馈；感知检测效能重要；反馈数量与线索显著性交互

7. CONTRIBUTION: 理论驱动模型与交互机制

### introduction_moves

1. CONTEXT: 钓鱼导致巨额损失、数据泄露第一原因

2. PRACTICAL_STAKES: 80%组织受攻击、损失超24亿美元

3. PRIOR_KNOWLEDGE: 已有训练研究改善检测能力

4. LIMITATION: 只关注检测准确率而忽略决策回避

5. GAP: 决策回避行为尚不清楚

6. WHY_GAP_MATTERS: 决策回避造成潜在收益损失

7. LIMITATION: 反馈类型情境效应未明

8. GAP: 反馈特征与钓鱼特征/自我效能的交互缺乏研究

9. RQ_OR_OBJECTIVE: 四项研究目标

10. THEORY_INTRO: 目标设定与技能获得理论

11. STUDY_OVERVIEW: 四个实验与样本来源

12. RESULT: 核心发现预览

13. CONTRIBUTION: 四点理论贡献定位

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 反钓鱼文献分成预测因素与外部干预两流

2. LIMITATION: 规则式训练未限定具体格式，情境效果未知

3. PRIOR_KNOWLEDGE: 示例式训练已在Google钓鱼检测测试中出现且更具体

4. THEORY_INTRO: 目标设定理论把目标、反馈、任务复杂性和自我效能联系起来

5. THEORY_PROPOSITION: 反馈特征、任务复杂性、自我效能是绩效决定因素

6. THEORY_INTRO: 技能获得理论三阶段：陈述性知识、知识编译、程序性知识

7. MECHANISM: 直接线索降低认知负荷，促进程序化

8. GAP: 感知检测效能直接影响训练结果尚未确定

### artifact_design_moves

1. REQUIREMENT: 反馈应把抽象指导转化为具体可操作步骤

2. DESIGN_FEATURE: 示例式反馈展示真实钓鱼邮件、伪造链接和悬停提示

3. DESIGN_FEATURE: 正念式反馈提供“停下思考”类抽象提醒

4. DESIGN_FEATURE: 低反馈数量仅说明一个技巧，高反馈数量说明多个线索

5. DESIGN_FEATURE: 低线索显著性邮件仅含伪造链接，高线索显著性邮件叠加可疑域名和紧迫语气等线索

6. DESIGN_FEATURE: 实验4无链接邮件采用假装公司通知并诱导回复/打电话的方式

7. METHOD_JUSTIFICATION: 邮件HTML修改以支持悬停链接但不允许点击

8. BENCHMARK_OR_CONTRAST: 正念式反馈和低数量/低显著性作为参照条件

### evaluation_moves

1. STUDY_OVERVIEW: Table 2列出四个实验的假设、设计、样本、变量和分析方法

2. METHOD_JUSTIFICATION: 在线实验可避免现场实验的道德问题且高效

3. METHOD_JUSTIFICATION: 非回应偏差检验和在线数据质量控制

4. METHOD_JUSTIFICATION: GEE适用于重复有序/二元结果的嵌套结构

5. METHOD_JUSTIFICATION: 操纵检验验证反馈类型和反馈数量感知差异

6. RESULT: 各实验以F统计量、p值、效应量、OR值报告结果

7. ROBUSTNESS_OR_BOUNDARY_TEST: 实验4以新邮件类型检验边界

8. BOUNDARY_CONDITION: 反馈数量无主效应但交互显著，说明效果依赖上下文

### discussion_and_contribution_moves

1. RESULT: Table 7汇总四个实验假设结果

2. CONTRIBUTION: 目标设定理论整合三类因素

3. CONTRIBUTION: 决策回避与检测准确率机制不同

4. CONTRIBUTION: 技能获得理论解释示例式反馈优势

5. CONTRIBUTION: 感知检测效能直接作用与交互

6. CONTRIBUTION: 反馈数量作为调节变量

7. BOUNDARY_CONDITION: 更多反馈并非总是更好，低数量对高难度钓鱼更有利

8. LIMITATION_AND_FUTURE: 在线测验、美国样本、短期效果、仅链接钓鱼等限制

9. LIMITATION_AND_FUTURE: 未来可检验组合反馈、其他钓鱼特征、长期学习与真实情境

10. BOUNDARY_CONDITION: 结论仅适用于链接嵌入型钓鱼邮件范围

## 理论/知识到设计的翻译

### 知识/理论基础

1. 目标设定理论（Locke & Latham, 2002）

2. 技能获得理论（Anderson, 1982, 1987）

3. 反钓鱼训练文献（Jensen et al., 2017; Nguyen et al., 2021a; Wang et al., 2016, 2017等）

4. 反馈干预与认知负荷研究（Kluger & DeNisi, 1996; Kanfer & Ackerman, 1989; Lam et al., 2011）

- 理论—设计耦合：direct

- 耦合判定理由：目标设定理论和技能获得理论前瞻性地决定了核心构念、操纵条件和假设方向：技能获得理论直接推出示例式反馈与正念式反馈的对比；认知资源有限性推出反馈数量与线索显著性交互；自我效能期望逻辑推出感知检测效能的效应。实验中的操纵和测量均由这些理论命题转化而来，并由后续实验直接检验。

- 理论到设计翻译链：目标设定理论把反钓鱼培训目标拆解为反馈、任务复杂性和自我效能三类决定因素；技能获得理论进一步说明具体示例比抽象指导更易从陈述性知识转化为程序性知识；由此反馈类型被设计为示例式（具体、可直接应用）对正念式（抽象、提醒注意）；反馈数量被设计为信息细节多少；任务复杂性被操作为钓鱼线索显著性；自我效能被测量为感知检测效能。实验通过比较这些设计差异来检验理论命题。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：技能获得理论：具体、带直接线索的反馈能减少认知努力，帮助陈述性知识编译为程序性知识。

- mechanism_cn：直接线索使学习者把认知资源集中在关键动作上，降低程序化难度。

- design_requirement_cn：反钓鱼反馈应包含具体的检测步骤和实际钓鱼邮件示例，而非只有抽象建议。

- artifact_choice_cn：示例式反馈：展示真实钓鱼邮件，标注伪造链接并要求悬停查看网址；正念式反馈：只提醒“停下、思考、检查”等抽象原则。

- evaluated_contrast_cn：示例式 vs 正念式反馈在链接嵌入邮件中的效果。

- objective_result_cn：实验1、2、4中示例式反馈在链接嵌入邮件下提高检测准确率并减少决策回避；实验4显示对无链接邮件无此优势。

##### evidence_pointers

1. 3.1 H1

2. 4.1.1 Treatment

3. 4.1.6 Results

4. Table 3

5. Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：目标设定理论：自我效能/期望会提升努力投入，从而提高任务绩效。

- mechanism_cn：高感知检测效能使个体更愿意做判断、投入认知资源，从而减少跳过并提高准确率。

- design_requirement_cn：培训评价中需要测量个体对每条邮件的感知检测效能，并考察反馈是否帮助效能转化为绩效。

- artifact_choice_cn：每条邮件后测量感知检测效能；反馈类型作为可能调节效能-绩效关系的条件。

- evaluated_contrast_cn：高 vs 低感知检测效能，以及效能与反馈类型的交互。

- objective_result_cn：感知检测效能显著降低决策回避并提高检测准确率；与反馈类型对准确率的交互边缘显著。

##### evidence_pointers

1. 3.1 H2/H3

2. 4.2.3 Experimental Procedures

3. 4.2.6 GEE

4. Table 4

#### 3. 3

- theory_or_knowledge_claim_cn：任务复杂度理论：线索越少、越隐蔽，需要越多认知资源，任务绩效越差。

- mechanism_cn：高线索显著性的邮件更容易被识别；低线索显著性邮件需要更多注意和推理。

- design_requirement_cn：实验材料必须操纵线索显著性，以检验任务复杂度对训练结果的影响。

- artifact_choice_cn：低线索显著性邮件仅包含伪造链接；高线索显著性邮件叠加伪造域名、紧迫语气、语法错误或泛称问候。

- evaluated_contrast_cn：低 vs 高钓鱼线索显著性的邮件。

- objective_result_cn：线索显著性正向影响检测准确率，对决策回避无显著作用。

##### evidence_pointers

1. 3.2 H5

2. 4.3.1 Treatment

3. 4.3.7 GEE

4. Table 5

#### 4. 4

- theory_or_knowledge_claim_cn：认知资源与反馈数量研究：更多反馈不一定更好；程序性知识充足时，外围线索才能被识别。

- mechanism_cn：低数量反馈只形成少量核心规则；高数量反馈提供更多可对线索的规则，使线索显著性发挥更大作用。

- design_requirement_cn：反馈数量应作为操纵变量，并与线索显著性共同考察，而非只检验主效应。

- artifact_choice_cn：低反馈数量只讲伪造链接一个技巧；高反馈数量同时讲解伪造链接、伪造域名、泛称问候和紧迫语气等技巧。

- evaluated_contrast_cn：低 vs 高反馈数量，以及反馈数量×线索显著性交互。

- objective_result_cn：反馈数量无主效应；交互显著，高数量反馈下线索显著性对准确率的影响更强。

##### evidence_pointers

1. 3.2 H4/H6

2. 4.3.1 Treatment

3. 4.3.7 GEE

4. Table 5

#### 5. 5

- theory_or_knowledge_claim_cn：技能获得理论的情境性：学会检测伪造链接的程序性知识不能自动迁移到无链接邮件。

- mechanism_cn：示例式反馈编码的是与链接相关的具体规则，面对新类型邮件时缺少对应程序性知识，甚至可能增加不确定性。

- design_requirement_cn：需要检验反馈类型在不同邮件类型中的边界，避免把链接情境结论泛化。

- artifact_choice_cn：增加无链接钓鱼邮件：伪造公司通知、诱导回复或拨打电话。

- evaluated_contrast_cn：反馈类型×邮件类型（链接嵌入 vs 无链接）的交互。

- objective_result_cn：示例式反馈仅在链接嵌入邮件中提高准确率；无链接邮件中两反馈组准确率无差异，且示例式反馈导致更多决策回避。

##### evidence_pointers

1. 4.4.1 Treatment

2. 4.4.7 ANCOVA

3. Table 6

4. Figure 5

## 评价逻辑

### evaluation_modes

1. 受控在线实验（不同组间/组内/混合设计）

2. 操纵检验（pilot研究、卡方检验、事后ANOVA）

3. ANCOVA

4. 广义估计方程（GEE）

5. 确认性因子分析与构念效度检验

6. 功效分析与非回应偏差检验

7. VIF多重共线性检验

8. 交互效应图与OR/效果量解读

- why_these_evaluations_cn：研究假设涉及因果性和消息层/个体层嵌套结构，因此需要多轮受控实验而不是单一调查；GEE用于处理重复测量的二元/有序结果；操纵检验确保反馈类型和反馈数量确实被感知为不同；实验4的边界设计防止把链接情境结论过度推广。

- benchmark_and_contrast_chain_cn：正念式反馈作为来自已有文献的基准条件，示例式反馈作为理论预测的更优条件；低反馈数量和低线索显著性作为参照水平；实验1-3在链接嵌入邮件基线中累积证据，实验4引入无链接邮件作为反事实边界，从而把‘示例式反馈更优’转化为‘在链接嵌入邮件且规则可迁移的范围内更优’。

### claim_evidence_ledger

#### 1. 示例式反馈优于正念式反馈（链接嵌入邮件下）

- claim_cn：示例式反馈优于正念式反馈（链接嵌入邮件下）

- evidence_cn：实验1 H1a/H1b显著；实验4链接邮件条件下准确率显著更高；效果量达中到大。

- supported：是

#### 2. 感知检测效能直接降低决策回避并提高检测准确率

- claim_cn：感知检测效能直接降低决策回避并提高检测准确率

- evidence_cn：实验2和实验3的GEE结果均显著，且控制了应对方式等变量。

- supported：是

#### 3. 反馈类型调节感知检测效能与准确率的关系

- claim_cn：反馈类型调节感知检测效能与准确率的关系

- evidence_cn：实验2交互项p=0.08，作者报告为边缘支持。

- supported：marginal

#### 4. 反馈数量有主效应

- claim_cn：反馈数量有主效应

- evidence_cn：实验3中H4a/H4b均不显著；加入交互后主效应消失。

- supported：否

#### 5. 钓鱼线索显著性正向影响检测准确率，且受反馈数量调节

- claim_cn：钓鱼线索显著性正向影响检测准确率，且受反馈数量调节

- evidence_cn：实验3中H5和H6显著，交互图和OR值显示高数量组更陡。

- supported：是

#### 6. 示例式反馈优势具有邮件类型边界

- claim_cn：示例式反馈优势具有邮件类型边界

- evidence_cn：实验4显著交互：无链接邮件下优势消失，甚至增加决策回避。

- supported：是

- internal_validity_strategy_cn：随机分配、操纵检验、非回应偏差检验、严格数据清洗（重复IP/位置/出生日期、美国地理位置、完成度）、注意力检查、防机器人技术、使用金钱激励使参与者认真作答、控制重要协变量、VIF检验。

- external_validity_strategy_cn：使用三个不同在线样本库（MTurk、Esearch.com、Clickworker.com），邮件内容基于真实公司和常见钓鱼手法，HTML交互方式模拟邮件客户端，使用金钱激励模拟现实后果；但仍是短时在线测验而非真实邮箱环境。

- what_is_not_actually_tested_cn：未直接测量技能获得理论中的认知过程（陈述性到程序性知识的编译）；未检验长期保持和真实点击或回复行为；只覆盖基于伪造链接的钓鱼邮件，未覆盖附件下载、密码重置等更广钓鱼形式；实验在在线问卷中进行，而非自然工作场景。

## 贡献闭环

- technical_claim_cn：在链接嵌入型邮件测验中，示例式反馈比正念式反馈带来更高的检测准确率和更少的决策回避。

- artifact_claim_cn：反馈的具体性（示例式、直接展示伪造链接并说明检测方法）是改进绩效的关键设计特征；反馈数量则不是简单越多越好，而是通过与线索显著性交互发挥作用。

- mechanism_claim_cn：示例式反馈通过降低认知负荷、促进陈述性知识向程序性知识转化，使学习者更容易应用反钓鱼技巧；感知检测效能通过提高努力和降低犹豫影响决策回避与准确率。

- boundary_claim_cn：上述优势仅适用于链接嵌入型钓鱼邮件；遇到无链接的新型钓鱼邮件时，示例式反馈并不提高准确率，甚至会增加决策回避；结论还受美国样本、短期训练和在线测验情境限制。

- reusable_design_knowledge_cn：反钓鱼培训反馈应使用具体示例而不仅是抽象提醒；应针对目标钓鱼邮件类型设计反馈内容；反馈信息量应与任务复杂度匹配，基础培训不应一开始就提供过多技巧；当面对高难度低线索邮件时，少量但扎实的规则可能更有效。

- theoretical_contribution_cn：把目标设定理论引入反钓鱼培训，同时考察决策回避与检测准确率；用技能获得理论解释反馈类型情境效应；证明感知检测效能在控制应对方式后仍具直接效应；揭示反馈数量作为调节变量而非简单主因；连接自我效能与技能获得视角。

- how_discussion_closes_intro_gap_cn：讨论的每个理论贡献分别对应引言四个缺口：引入决策回避结果变量、明确反馈类型情境、检验感知检测效能直接效应、揭示反馈与钓鱼特征的交互；实验4则回应外部有效性担忧，主动声明边界。

- overclaim_or_unsupported_leaps_cn：H3b只在边缘显著水平上获得支持，但在贡献部分被描述为理论与实证连接；H4未获支持后转用交互效应解释，存在事后合理化风险；技能获得机制未被直接测量，而是从行为结果推断；决策回避与检测准确率的低相关被用于断言不同机制，但没有正式的机制分析或中介检验。

## 句级写作动作图谱

### 1. Introduction P1 S1

- order：1

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：成功的钓鱼攻击给组织造成巨大财务和数据损失。

- rhetorical_function_cn：开篇建立高重要性议题。

- depends_on_cn：无

- sets_up_cn：为后续说明培训必要性做铺垫。

- evidence_pointer：Introduction para 1

### 2. Introduction P1 S2-S4

- order：2

- section：Introduction

- locator：Introduction P1 S2-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：钓鱼是数据泄露首要原因，2021年约80%组织受攻击，损失超24亿美元。

- rhetorical_function_cn：用统计数据强化现实紧迫性。

- depends_on_cn：上一句的损失陈述。

- sets_up_cn：为组织需要系统评估培训项目提供理由。

- evidence_pointer：Introduction para 1

### 3. Introduction P1 S5-S6

- order：3

- section：Introduction

- locator：Introduction P1 S5-S6

- move_code：PRACTICAL_STAKES

- paraphrase_cn：组织常提供安全意识材料和反馈，但这些项目需要IT部门投入大量资源，因此需要系统分析有效性。

- rhetorical_function_cn：把宏观问题转向组织培训实践。

- depends_on_cn：前面的损失数据。

- sets_up_cn：为文献回顾和缺口分析限定范围。

- evidence_pointer：Introduction P1

### 4. Introduction P2 S1-S2

- order：4

- section：Introduction

- locator：Introduction P2 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究表明反钓鱼训练能帮助人们区分合法与钓鱼邮件，并列举相关实证。

- rhetorical_function_cn：承认领域已有积累，避免无中生有。

- depends_on_cn：组织培训背景。

- sets_up_cn：为接下来指出缺口提供基线。

- evidence_pointer：Introduction P2

### 5. Introduction P3 S1

- order：5

- section：Introduction

- locator：Introduction P3 S1

- move_code：LIMITATION

- paraphrase_cn：此前研究主要把检测准确率作为结果变量。

- rhetorical_function_cn：指出结果变量单一。

- depends_on_cn：先概述已有研究。

- sets_up_cn：引出决策回避缺口。

- evidence_pointer：Introduction P3 S1

### 6. Introduction P3 S2-S3

- order：6

- section：Introduction

- locator：Introduction P3 S2-S3

- move_code：GAP

- paraphrase_cn：对个体决定不回复邮件这类常见决策回避行为知之甚少。

- rhetorical_function_cn：正式声明第一个研究缺口。

- depends_on_cn：检测准确率单一关注。

- sets_up_cn：为把决策回避纳入理论模型提供依据。

- evidence_pointer：Introduction P3 S2-S3

### 7. Introduction P3 S4

- order：7

- section：Introduction

- locator：Introduction P3 S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：决策回避会损失与他人互动的潜在收益，是不确定性下的普遍现象。

- rhetorical_function_cn：解释为什么决策回避值得研究。

- depends_on_cn：缺口陈述。

- sets_up_cn：为第二个结果变量提供理论重要性。

- evidence_pointer：Introduction P3 S4

### 8. Introduction P4 S1-S2

- order：8

- section：Introduction

- locator：Introduction P4 S1-S2

- move_code：LIMITATION

- paraphrase_cn：已有研究试图比较反馈类型在不同情境下的有效性，但知识仍不足。

- rhetorical_function_cn：指出反馈类型的情境效应未明。

- depends_on_cn：文献回顾。

- sets_up_cn：引出第二个研究目标。

- evidence_pointer：Introduction P4

### 9. Introduction P5 S1-S2

- order：9

- section：Introduction

- locator：Introduction P5 S1-S2

- move_code：LIMITATION

- paraphrase_cn：已有研究发现自我效能影响反钓鱼动机，但感知检测效能是否能直接影响训练结果仍不确定。

- rhetorical_function_cn：指出第三个缺口。

- depends_on_cn：前两个缺口。

- sets_up_cn：为后续把感知检测效能设为关键构念做铺垫。

- evidence_pointer：Introduction P5

### 10. Introduction P6 S1-S2

- order：10

- section：Introduction

- locator：Introduction P6 S1-S2

- move_code：GAP

- paraphrase_cn：反馈特征如何与钓鱼特征及个体效能交互仍不清楚。

- rhetorical_function_cn：指出综合交互缺口。

- depends_on_cn：前三个缺口。

- sets_up_cn：为研究模型加入交互假设。

- evidence_pointer：Introduction P6

### 11. Introduction P7 S1

- order：11

- section：Introduction

- locator：Introduction P7 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：明确提出四项研究目标，覆盖决定因素、反馈类型情境、感知检测效能影响和交互效应。

- rhetorical_function_cn：给出论文研究问题清单。

- depends_on_cn：四个缺口。

- sets_up_cn：为研究模型和实验设计提供路线图。

- evidence_pointer：Introduction P7 S1

### 12. Introduction P7 S2-S3

- order：12

- section：Introduction

- locator：Introduction P7 S2-S3

- move_code：THEORY_INTRO

- paraphrase_cn：引入目标设定理论和技能获得理论，说明它们将用于解释反馈、钓鱼特征和自我效能对训练结果的影响。

- rhetorical_function_cn：确定理论透镜。

- depends_on_cn：研究目标。

- sets_up_cn：为后续理论背景和假设做引导。

- evidence_pointer：Introduction P7 S2-S3

### 13. Introduction P8 S1

- order：13

- section：Introduction

- locator：Introduction P8 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：用652名美国被试开展四项实验，样本来自三个在线平台。

- rhetorical_function_cn：预告实证设计。

- depends_on_cn：模型提出。

- sets_up_cn：让读者期待后续方法部分。

- evidence_pointer：Introduction P8 S1

### 14. Introduction P8 S2-S4

- order：14

- section：Introduction

- locator：Introduction P8 S2-S4

- move_code：RESULT

- paraphrase_cn：预报告结果：示例式反馈在链接嵌入邮件中优于抽象反馈，但新邮件类型下不可持续；感知检测效能重要；反馈数量与线索显著性有交互。

- rhetorical_function_cn：提前给出核心发现。

- depends_on_cn：四项实验完成。

- sets_up_cn：为贡献声明提供直接证据。

- evidence_pointer：Introduction P8

### 15. Introduction P9 S1-S5

- order：15

- section：Introduction

- locator：Introduction P9 S1-S5

- move_code：CONTRIBUTION

- paraphrase_cn：概括四点贡献：同时研究决策回避与准确率、反馈类型情境、感知检测效能与反馈类型的交互、反馈数量与线索显著性交互。

- rhetorical_function_cn：建立贡献定位。

- depends_on_cn：结果预览。

- sets_up_cn：为讨论部分的理论贡献做预埋。

- evidence_pointer：Introduction P9

### 16. 2.1 P1

- order：16

- section：Theoretical Background 2.1

- locator：2.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：总结反钓鱼文献的两个方向：预测绩效因素和外部干预效果。

- rhetorical_function_cn：梳理已有知识谱系。

- depends_on_cn：引言中的文献缺口。

- sets_up_cn：说明本研究属于外部干预/训练反馈方向。

- evidence_pointer：2.1 Antiphishing Literature

### 17. 2.1 P2-P3

- order：17

- section：Theoretical Background 2.1

- locator：2.1 P2-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：介绍正念式与规则式训练的已有比较，指出过度学习假设未被支持。

- rhetorical_function_cn：聚焦本研究最相关的反馈类型文献。

- depends_on_cn：两大文献方向。

- sets_up_cn：为引入第三种示例式反馈提供过渡。

- evidence_pointer：2.1 P2-P3

### 18. 2.1 P4-P5

- order：18

- section：Theoretical Background 2.1

- locator：2.1 P4-P5

- move_code：LIMITATION

- paraphrase_cn：规则式训练没有限定格式，在试错式/游戏式培训情境中的效果未知；示例式反馈更具体，已被Google类测验使用。

- rhetorical_function_cn：说明现有反馈类型分类不足。

- depends_on_cn：正念/规则式训练比较。

- sets_up_cn：为论文提出的示例式反馈概念和H1做基础。

- evidence_pointer：2.1 P4-P5

### 19. 2.2 P1

- order：19

- section：Theoretical Background 2.2

- locator：2.2 P1

- move_code：THEORY_INTRO

- paraphrase_cn：引入目标设定理论，指出其可识别影响实际绩效的构念和机制，适用于反钓鱼培训。

- rhetorical_function_cn：说明选择目标设定理论的原因。

- depends_on_cn：此前对训练结果的关注。

- sets_up_cn：为后续反馈、任务复杂性、自我效能三小节提供框架。

- evidence_pointer：2.2 Goal-Setting Theory

### 20. 2.2.1 P1-P3

- order：20

- section：Theoretical Background 2.2.1

- locator：2.2.1 P1-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：反馈被广泛视为促进参与和绩效的重要因素，反钓鱼训练中也常用反馈。

- rhetorical_function_cn：建立反馈重要性的文献基础。

- depends_on_cn：目标设定理论。

- sets_up_cn：为反馈特征缺口做铺垫。

- evidence_pointer：2.2.1 Feedback Characteristics

### 21. 2.2.1 P4

- order：21

- section：Theoretical Background 2.2.1

- locator：2.2.1 P4

- move_code：GAP

- paraphrase_cn：缺乏对反馈特征如何系统影响反钓鱼行为的检验。

- rhetorical_function_cn：定位本研究切入的反馈类型和数量变量。

- depends_on_cn：反馈有效性综述。

- sets_up_cn：为反馈类型和数量假设提供依据。

- evidence_pointer：2.2.1 P4

### 22. 2.2.2 P1-P3

- order：22

- section：Theoretical Background 2.2.2

- locator：2.2.2 P1-P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：任务复杂性是影响训练和绩效的重要任务特征；高复杂性需要更多认知资源。

- rhetorical_function_cn：把一般任务复杂性理论引入反钓鱼。

- depends_on_cn：目标设定理论的任务特征分支。

- sets_up_cn：为钓鱼线索显著性的定义和假设提供基础。

- evidence_pointer：2.2.2 Phishing Characteristics

### 23. 2.2.2 P4

- order：23

- section：Theoretical Background 2.2.2

- locator：2.2.2 P4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：定义钓鱼线索显著性为邮件中线索的明显程度，并称其对反钓鱼行为重要而少被研究。

- rhetorical_function_cn：引入核心消息层构念。

- depends_on_cn：任务复杂性论述。

- sets_up_cn：为H5和H6做理论铺垫。

- evidence_pointer：2.2.2 P4

### 24. 2.2.3 P1-P2

- order：24

- section：Theoretical Background 2.2.3

- locator：2.2.3 P1-P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：自我效能是成就情境任务绩效的重要预测因素；已有反钓鱼研究涉及效能与过度自信、应对适应性。

- rhetorical_function_cn：介绍自我效能已有证据。

- depends_on_cn：目标设定理论。

- sets_up_cn：为指出直接效应未知做铺垫。

- evidence_pointer：2.2.3 Self-Efficacy

### 25. 2.2.3 P2

- order：25

- section：Theoretical Background 2.2.3

- locator：2.2.3 P2

- move_code：LIMITATION

- paraphrase_cn：尽管已有发现，感知检测效能对决策回避和检测准确率的直接效应仍不清楚。

- rhetorical_function_cn：声明第四个文献缺口。

- depends_on_cn：自我效能综述。

- sets_up_cn：为H2假设提供动机。

- evidence_pointer：2.2.3 P2

### 26. 2.3 P1-P2

- order：26

- section：Theoretical Background 2.3

- locator：2.3 P1-P2

- move_code：THEORY_INTRO

- paraphrase_cn：介绍技能获得理论的三个阶段：陈述性知识、知识编译、程序性知识。

- rhetorical_function_cn：引入第二个理论透镜。

- depends_on_cn：目标设定理论框架。

- sets_up_cn：为解释示例式反馈优势提供机制。

- evidence_pointer：2.3 Skill Acquisition Theory

### 27. 2.3 P3

- order：27

- section：Theoretical Background 2.3

- locator：2.3 P3

- move_code：MECHANISM

- paraphrase_cn：学习者认知容量有限，反馈等组织干预应帮助其有效获取、整合和应用认知技能。

- rhetorical_function_cn：把技能获得理论连接到培训设计。

- depends_on_cn：三阶段理论。

- sets_up_cn：为假设中的直接线索降低认知负荷提供依据。

- evidence_pointer：2.3 P3

### 28. 3.1 P1-P2

- order：28

- section：Research Model and Hypotheses 3.1

- locator：3.1 P1-P2

- move_code：MECHANISM

- paraphrase_cn：带直接线索的反馈能减少认知努力、提高注意力；示例式反馈包含具体术语和操作指南，更容易应用到链接判断。

- rhetorical_function_cn：解释为何示例式反馈优于正念式反馈。

- depends_on_cn：技能获得理论。

- sets_up_cn：推演H1a/H1b。

- evidence_pointer：3.1 Feedback Type and Perceived Detection Efficacy

### 29. 3.1 P3-P4

- order：29

- section：Research Model and Hypotheses 3.1

- locator：3.1 P3-P4

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H1a：示例式反馈比正念式反馈减少决策回避；H1b：示例式反馈提高检测准确率。

- rhetorical_function_cn：给出第一个假设对。

- depends_on_cn：技能获得机制。

- sets_up_cn：为实验1提供检验目标。

- evidence_pointer：3.1 H1

### 30. 3.1 P5-P6

- order：30

- section：Research Model and Hypotheses 3.1

- locator：3.1 P5-P6

- move_code：MECHANISM

- paraphrase_cn：感知检测效能与期望一致，使人更愿意投入认知资源，从而减少回避并提高准确率。

- rhetorical_function_cn：解释自我效能到结果的因果链。

- depends_on_cn：目标设定理论中的期望概念。

- sets_up_cn：提出H2a/H2b。

- evidence_pointer：3.1 P5-P6

### 31. 3.1 P6

- order：31

- section：Research Model and Hypotheses 3.1

- locator：3.1 P6

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H2a和H2b：感知检测效能负向影响决策回避、正向影响检测准确率。

- rhetorical_function_cn：给出个体效能假设。

- depends_on_cn：期望机制。

- sets_up_cn：为实验2设置检验目标。

- evidence_pointer：3.1 H2

### 32. 3.1 P7-P8

- order：32

- section：Research Model and Hypotheses 3.1

- locator：3.1 P7-P8

- move_code：MECHANISM

- paraphrase_cn：示例式反馈更易将知识程序化并释放认知资源，而正念式反馈难以提供具体操作，因此示例式反馈会强化感知检测效能向准确率的转化。

- rhetorical_function_cn：把两种反馈类型与自我效能连接。

- depends_on_cn：技能获得和H2机制。

- sets_up_cn：提出H3b。

- evidence_pointer：3.1 P7-P8

### 33. 3.1 H3b

- order：33

- section：Research Model and Hypotheses 3.1

- locator：3.1 H3b

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H3b：反馈类型与感知检测效能交互，示例式反馈条件下效能对准确率的正向作用更强。

- rhetorical_function_cn：给出跨层交互假设。

- depends_on_cn：机制推断。

- sets_up_cn：为实验2的GEE交互模型提供目标。

- evidence_pointer：3.1 H3b

### 34. 3.2 P1-P2

- order：34

- section：Research Model and Hypotheses 3.2

- locator：3.2 P1-P2

- move_code：MECHANISM

- paraphrase_cn：反馈数量代表信息的充分性；更多示例式反馈可提供更多可应用的程序性知识，因此应减少回避并提高准确率。

- rhetorical_function_cn：提出反馈数量的主效应逻辑。

- depends_on_cn：反馈研究和技能获得理论。

- sets_up_cn：提出H4a/H4b。

- evidence_pointer：3.2 P1-P2

### 35. 3.2 H4

- order：35

- section：Research Model and Hypotheses 3.2

- locator：3.2 H4

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H4a和H4b：示例式反馈数量负向影响决策回避、正向影响检测准确率。

- rhetorical_function_cn：给出反馈数量主效应假设。

- depends_on_cn：反馈信息充分性论述。

- sets_up_cn：为实验3检验反馈数量主效应。

- evidence_pointer：3.2 H4

### 36. 3.2 P3-P4

- order：36

- section：Research Model and Hypotheses 3.2

- locator：3.2 P3-P4

- move_code：MECHANISM

- paraphrase_cn：线索显著性高的邮件识别所需认知资源少，因此准确率更高。

- rhetorical_function_cn：把任务复杂性与邮件线索操作化连接。

- depends_on_cn：任务复杂性理论。

- sets_up_cn：提出H5b。

- evidence_pointer：3.2 P3-P4

### 37. 3.2 H5-H6

- order：37

- section：Research Model and Hypotheses 3.2

- locator：3.2 H5-H6

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H5b和H6b：线索显著性正向影响准确率；反馈数量正向调节这一关系。

- rhetorical_function_cn：给出消息层主效应与交互假设。

- depends_on_cn：认知资源有限性。

- sets_up_cn：为实验3设置具体检验目标。

- evidence_pointer：3.2 H5-H6

### 38. 4 P1-P2

- order：38

- section：Methods 4

- locator：4 P1-P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：Table 2总结四项实验各自检验的假设、设计、样本、变量和分析方法；所有实验共用预备测验-反馈-正式测验流程。

- rhetorical_function_cn：给出全文实证蓝图。

- depends_on_cn：研究模型。

- sets_up_cn：为后续四个实验详细介绍铺路。

- evidence_pointer：Methods 4, Table 2

### 39. 4 P3

- order：39

- section：Methods 4

- locator：4 P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用Qualtrics文本图形题并修改HTML，使参与者可悬停查看链接但不能点击跳转。

- rhetorical_function_cn：解释实验材料如何模拟邮件客户端且保证安全。

- depends_on_cn：网页问卷设计。

- sets_up_cn：为操纵反馈和邮件类型提供技术基础。

- evidence_pointer：4 P3

### 40. 4 P4-P5

- order：40

- section：Methods 4

- locator：4 P4-P5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用三个在线样本库并执行严格数据清洗、注意力与防机器人程序。

- rhetorical_function_cn：增强外部效度和内部效度。

- depends_on_cn：在线实验设计。

- sets_up_cn：为各实验样本有效性和非回应偏差检验做铺垫。

- evidence_pointer：4 P4-P5

### 41. 4.1.1 Treatment

- order：41

- section：Experiment 1

- locator：4.1.1 Treatment

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：实验1把参与者随机分到示例式反馈组或正念式反馈组，正念式反馈来自已有训练材料，作为参照条件。

- rhetorical_function_cn：建立反馈类型比较的基准。

- depends_on_cn：文献中的正念训练材料。

- sets_up_cn：为ANCOVA结果比较提供对照组。

- evidence_pointer：4.1.1 Treatment

### 42. 4.1.5 Manipulation Check

- order：42

- section：Experiment 1

- locator：4.1.5 Manipulation Check

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用133名MTurk参与者的pilot研究验证示例式反馈被感知为需要更少思考。

- rhetorical_function_cn：确保反馈类型操纵有效。

- depends_on_cn：实验材料设计。

- sets_up_cn：为实验1结果的可解释性提供基础。

- evidence_pointer：4.1.5 Manipulation Check

### 43. 4.1.6 Results and Discussion

- order：43

- section：Experiment 1

- locator：4.1.6 Results and Discussion

- move_code：RESULT

- paraphrase_cn：ANCOVA显示示例式反馈组决策回避显著更低，H1a支持。

- rhetorical_function_cn：报告第一个假设结果。

- depends_on_cn：操纵检验和ANCOVA模型。

- sets_up_cn：与后文实验2/4的决策回避结果形成对比。

- evidence_pointer：Table 3

### 44. 4.1.6 Results and Discussion

- order：44

- section：Experiment 1

- locator：4.1.6 Results and Discussion

- move_code：RESULT

- paraphrase_cn：ANCOVA显示示例式反馈组检测准确率显著更高且效果量大，H1b支持。

- rhetorical_function_cn：报告第二个假设结果。

- depends_on_cn：操纵检验和ANCOVA模型。

- sets_up_cn：为实验4的边界检验提供待限定结论。

- evidence_pointer：Table 3

### 45. 4.2 P1

- order：45

- section：Experiment 2

- locator：4.2 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验2在相同反馈类型比较中加入感知检测效能及其与反馈类型的交互。

- rhetorical_function_cn：交代实验2承接实验1未回答的个体效能问题。

- depends_on_cn：实验1主效应。

- sets_up_cn：为GEE分析设置目标。

- evidence_pointer：4.2

### 46. 4.2.6 Generalized Estimating Equations

- order：46

- section：Experiment 2

- locator：4.2.6 Generalized Estimating Equations

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：GEE适用于处理重复测量的二元/有序结果嵌套在个体中的数据结构。

- rhetorical_function_cn：解释统计方法选择。

- depends_on_cn：数据层级结构。

- sets_up_cn：为多层次假设检验提供合法依据。

- evidence_pointer：4.2.6 GEE

### 47. 4.2.6 Model 4

- order：47

- section：Experiment 2

- locator：4.2.6 Model 4

- move_code：RESULT

- paraphrase_cn：感知检测效能与决策回避显著负相关，H2a支持。

- rhetorical_function_cn：报告个体效能对回避行为的作用。

- depends_on_cn：GEE模型。

- sets_up_cn：为实验3中再次验证PDE作用提供一致性。

- evidence_pointer：Table 4 Model 4

### 48. 4.2.6 Model 5

- order：48

- section：Experiment 2

- locator：4.2.6 Model 5

- move_code：RESULT

- paraphrase_cn：感知检测效能显著正向影响检测准确率；反馈类型×感知检测效能交互边缘显著，H2b支持、H3b边缘支持。

- rhetorical_function_cn：报告效能主效应和交互效应。

- depends_on_cn：GEE Model 5。

- sets_up_cn：支持讨论中关于反馈帮助效能程序化的论点，但需谨慎。

- evidence_pointer：Table 4 Model 5

### 49. 4.3 P1

- order：49

- section：Experiment 3

- locator：4.3 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验3用2×2混合设计考察反馈数量与钓鱼线索显著性的作用和交互。

- rhetorical_function_cn：把研究重点从反馈类型转向反馈数量与消息特征。

- depends_on_cn：实验2未覆盖的反馈数量。

- sets_up_cn：为H4-H6检验提供设计蓝图。

- evidence_pointer：4.3

### 50. 4.3.5 Manipulation Check

- order：50

- section：Experiment 3

- locator：4.3.5 Manipulation Check

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：反馈数量操纵通过卡方检验成功；对线索显著性不设操纵检验，以避免问题本身引导被试注意线索。

- rhetorical_function_cn：解释操纵检验设计选择，尤其是为何不为线索显著性设置问题。

- depends_on_cn：实验3操纵设计。

- sets_up_cn：为排除操纵无效解释提供依据。

- evidence_pointer：4.3.5 Manipulation Check

### 51. 4.3.7 Model 3-4

- order：51

- section：Experiment 3

- locator：4.3.7 Model 3-4

- move_code：RESULT

- paraphrase_cn：反馈数量对决策回避和准确率均无主效应，H4不支持；交互模型显示线索显著性效应被反馈数量调节。

- rhetorical_function_cn：报告未支持的主效应和被支持的交互。

- depends_on_cn：GEE Model 3-4。

- sets_up_cn：为讨论中“更多反馈并非总是更好”提供实证依据。

- evidence_pointer：Table 5

### 52. 4.3.7 Model 4

- order：52

- section：Experiment 3

- locator：4.3.7 Model 4

- move_code：RESULT

- paraphrase_cn：线索显著性显著正向影响检测准确率；反馈数量与线索显著性交互显著，H5b和H6b支持。

- rhetorical_function_cn：报告消息层主效应与交互结果。

- depends_on_cn：GEE Model 4。

- sets_up_cn：为图4交互说明和实际建议提供证据。

- evidence_pointer：Table 5 Model 4

### 53. 4.4 P1

- order：53

- section：Experiment 4

- locator：4.4 P1

- move_code：TRANSITION

- paraphrase_cn：实验1只检验了链接嵌入邮件，但无链接钓鱼邮件同样常见，因此需要检验反馈类型是否在不同邮件类型下效果不同。

- rhetorical_function_cn：解释为什么需要补充第四个实验。

- depends_on_cn：实验1的结论和现实钓鱼形式多样性。

- sets_up_cn：为2×2边界设计提供理由。

- evidence_pointer：4.4 P1

### 54. 4.4 P1-P2

- order：54

- section：Experiment 4

- locator：4.4 P1-P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验4采用2×2组间设计：反馈类型×邮件类型（链接嵌入 vs 无链接）。

- rhetorical_function_cn：给出事后检验研究设计。

- depends_on_cn：前三个实验的边界问题。

- sets_up_cn：为ANCOVA结果提供结构。

- evidence_pointer：4.4 P1-P2

### 55. 4.4.7 ANCOVA

- order：55

- section：Experiment 4

- locator：4.4.7 ANCOVA

- move_code：RESULT

- paraphrase_cn：反馈类型与邮件类型对决策回避和检测准确率均有显著交互；示例式反馈优势仅出现在链接嵌入邮件中，在无链接邮件中消失甚至增加回避。

- rhetorical_function_cn：报告边界检验结果。

- depends_on_cn：2×2设计。

- sets_up_cn：为讨论中的边界条件和实践建议提供核心证据。

- evidence_pointer：Table 6

### 56. 5.1 Summary of Findings

- order：56

- section：Discussion 5.1

- locator：5.1 Summary of Findings

- move_code：RESULT

- paraphrase_cn：Table 7汇总四个实验的假设支持情况，并逐项解释主效应、交互和边界。

- rhetorical_function_cn：把分散的实验结果整合为整体结论。

- depends_on_cn：四个实验结果。

- sets_up_cn：为理论贡献部分提供统一证据基线。

- evidence_pointer：5.1, Table 7

### 57. 5.2 Theoretical Contributions P1

- order：57

- section：Discussion 5.2

- locator：5.2 Theoretical Contributions P1

- move_code：CONTRIBUTION

- paraphrase_cn：基于目标设定理论，首次把反馈特征、任务特征和自我效能一致地整合到反钓鱼培训结果模型。

- rhetorical_function_cn：把结果提升为对理论的整合贡献。

- depends_on_cn：实证支持。

- sets_up_cn：为后续更多细化理论贡献提供总体定位。

- evidence_pointer：5.2 P1

### 58. 5.2 Theoretical Contributions P2

- order：58

- section：Discussion 5.2

- locator：5.2 Theoretical Contributions P2

- move_code：CONTRIBUTION

- paraphrase_cn：决策回避与检测准确率的机制不同：前者更多由主观感知决定，后者由客观标准决定；二者相关很低，因此需要同时研究。

- rhetorical_function_cn：强调结果变量的区分性贡献。

- depends_on_cn：四个实验的相关和相关模式。

- sets_up_cn：为未来研究把二者分开建模提供依据。

- evidence_pointer：5.2 P2

### 59. 5.2 Theoretical Contributions P3

- order：59

- section：Discussion 5.2

- locator：5.2 Theoretical Contributions P3

- move_code：CONTRIBUTION

- paraphrase_cn：用技能获得理论证明示例式反馈更有效地把陈述性知识转化为程序性知识，至少对链接嵌入型邮件成立。

- rhetorical_function_cn：把核心实证差异归入技能获得理论。

- depends_on_cn：实验1和实验4结果。

- sets_up_cn：为组织具体化指导建议提供理论支持。

- evidence_pointer：5.2 P3

### 60. 5.2 Theoretical Contributions P4-P5

- order：60

- section：Discussion 5.2

- locator：5.2 Theoretical Contributions P4-P5

- move_code：CONTRIBUTION

- paraphrase_cn：感知检测效应对训练结果有直接作用，且其作用受反馈类型调节；这一结果连接了自我效能与技能获得视角。

- rhetorical_function_cn：补充自我效能直接效应和跨视角贡献。

- depends_on_cn：实验2结果。

- sets_up_cn：为实践中的效能培养提供理由。

- evidence_pointer：5.2 P4-P5

### 61. 5.2 Theoretical Contributions P6

- order：61

- section：Discussion 5.2

- locator：5.2 Theoretical Contributions P6

- move_code：CONTRIBUTION

- paraphrase_cn：反馈数量不是简单主因，而是调节线索显著性效应；这是首次揭示该交互。

- rhetorical_function_cn：强调反馈数量研究的增量贡献。

- depends_on_cn：实验3结果。

- sets_up_cn：为实践中的“不要过量信息”建议做铺垫。

- evidence_pointer：5.2 P6

### 62. 5.3 Practical Contributions P1-P2

- order：62

- section：Discussion 5.3

- locator：5.3 Practical Contributions P1-P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：实践上鼓励使用示例式反馈来应对链接嵌入型钓鱼，但更多反馈并非总是更好；低数量反馈对高难度、低线索钓鱼更有利。

- rhetorical_function_cn：把结果转成可操作设计知识。

- depends_on_cn：实验1/3/4结果。

- sets_up_cn：为未来长时训练研究留下问题。

- evidence_pointer：5.3

### 63. 5.4 Limitations and Future Research Directions

- order：63

- section：Discussion 5.4

- locator：5.4 Limitations and Future Research Directions

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：承认在线测验、美国样本、短期效果、仅链接钓鱼、反馈材料较短、未控变量等限制。

- rhetorical_function_cn：保护结论不被过度泛化。

- depends_on_cn：全文证据范围。

- sets_up_cn：为未来研究给出方向。

- evidence_pointer：5.4

### 64. 5.4 Future Research Directions

- order：64

- section：Discussion 5.4

- locator：5.4 Future Research Directions

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来可检验示例式与正念式反馈组合使用、其他钓鱼特征、长期重复训练以及社会/任务/物理情境因素。

- rhetorical_function_cn：扩展研究议程。

- depends_on_cn：当前边界。

- sets_up_cn：为后续学者提供明确起点。

- evidence_pointer：5.4 Future

### 65. 5.5 Concluding Remarks

- order：65

- section：Discussion 5.5

- locator：5.5 Concluding Remarks

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：总结指出反馈与钓鱼特征如何在各种攻击类型下影响决策回避和准确率仍需更多研究，希望模型有助于后续研究。

- rhetorical_function_cn：以开放性问题收束全文。

- depends_on_cn：理论模型与实证结果。

- sets_up_cn：强调研究问题的持续重要性。

- evidence_pointer：5.5

## 写作技术

- gap_construction_cn：引言用四个并列的“缺口”段落制造需求，每个缺口都从已有研究的局限性出发，并以“对……知之甚少/不清楚”句式收束；随后立即用四项研究目标逐一对应，形成强路标。

- signposting_cn：目标清单、Table 2实验总结、每个实验开头的问题陈述、Figure 2流程、Table 7结果汇总，使读者始终知道当前证据在整体论证中的位置。

- transition_logic_cn：每个实验结尾或下一实验开头说明上一实验未解决的问题：实验1留下个体与消息层面问题，实验2留下反馈数量问题，实验3留下邮件类型边界问题，实验4再回到反馈类型边界。

- claim_evidence_rhythm_cn：先提出理论假设，再用操作方法说明如何操纵，然后用表格报告统计量，最后用交互图和解释性段落把数字转换为机制语言；对未支持假设不回避，而是转用交互解释。

- benchmark_narrative_cn：正念式反馈作为来自已有文献的参照，示例式反馈作为新设计，读者可自然理解为“新条件是否打败旧标准”；低数量/低显著性作为参照水平；实验4把链接嵌入作为基线，无链接作为反事实边界。

- theory_return_cn：讨论部分的六个理论贡献均重新连接到引言缺口：决策回避、反馈类型情境、感知检测效能、交互效应；并把统计结果升华为快照式的机制差异。

- contribution_positioning_cn：用“few researchers / first to / theory-driven model”等定位语，在已有反钓鱼文献、目标设定理论和技能获得理论之间建立增量空间，而不是宣称完全开辟新领域。

- novelty_protection_cn：通过实验4的边界检验主动展示结论适用条件，防止“示例式反馈总是更好”的一次性印象；同时把未支持的H4解释为“反馈数量依赖情境”，使整体故事不是由所有假设都成立来支撑，而是由交互机制支撑。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用损失数据和培训实践说明现实重要性，并枚举文献缺口。

- research_job_cn：系统回顾反钓鱼训练文献，识别结果变量、反馈类型、自我效能和交互四类缺口。

- required_evidence_cn：有权威行业报告和可引用的近期反钓鱼研究。

- transition_to_next_cn：“因此本文目标如下……”将缺口转化为研究目标。

#### 2. 2

- step：2

- writing_job_cn：选择并介绍理论，把理论构念映射到变量。

- research_job_cn：用目标设定理论组织反馈、任务复杂性、自我效能；用技能获得理论解释具体反馈优势。

- required_evidence_cn：理论原文和已有反钓鱼应用，足以支撑构念选择。

- transition_to_next_cn：理论背景后直接进入研究模型与假设。

#### 3. 3

- step：3

- writing_job_cn：逐条提出假设并给出机制解释。

- research_job_cn：把每个理论命题转化为可操纵/可测量的变量和预期方向。

- required_evidence_cn：每个假设有明确的理论链条：理论命题→机制→变量关系。

- transition_to_next_cn：“Table 2总结了四项实验……”承接假设检验。

#### 4. 4

- step：4

- writing_job_cn：设计并报告实验操纵与测量，并在主实验前进行操纵检验。

- research_job_cn：制作反馈材料、邮件刺激、量表；运行pilot/操纵检验。

- required_evidence_cn：操纵检验显著，参与者确实感知到条件差异。

- transition_to_next_cn：确认操纵有效后再进入主实验。

#### 5. 5

- step：5

- writing_job_cn：按假设逐层安排多个实验，每个实验填补上一实验的未知。

- research_job_cn：先测验主效应，再加入个体/消息层面变量和交互，最后补充边界。

- required_evidence_cn：前一个实验的结果提供下一实验必须控制或扩展的基线。

- transition_to_next_cn：“仍不清楚……因此实验N……”的过渡句式。

#### 6. 6

- step：6

- writing_job_cn：用适合嵌套数据的统计模型分析并报告效应量。

- research_job_cn：使用GEE/ANCOVA等方法，报告p值、OR、效果量和交互图。

- required_evidence_cn：模型诊断（VIF）、样本量功效、非回应偏差不超过可接受范围。

- transition_to_next_cn：结果汇总表后进入讨论。

#### 7. 7

- step：7

- writing_job_cn：讨论部分把结果返回理论，强调边界条件和实际设计知识。

- research_job_cn：说明哪些假设支持、哪些不支持，并把不支持的结果转化为情境依赖洞见。

- required_evidence_cn：每个理论贡献都能指向具体实验和表/图。

- transition_to_next_cn：总结后列出局限性并给出未来方向。

### most_transferable_moves_cn

1. 用现实损失数据开场并快速过渡到组织培训实践

2. 以四个并列缺口组织引言，让研究目标一一对应

3. 把理论构念直接转化为实验操纵和测量，而不是只做事后解释

4. 设立一个来自已有文献的基准条件（正念式反馈）来衬托新条件

5. 在主实验前运行操纵检验并用pilot验证材料感知

6. 用多个实验逐层累积证据，最后加一个边界实验

7. 在讨论中把未支持假设重释为情境依赖而非失败

8. 用边界条件和局限性限制结论，避免过度泛化

### resource_intensive_or_nonstandard_parts_cn

1. 四个在线实验需要使用三个不同付费样本库并给予金钱激励

2. 制作接近真实邮件的HTML交互材料需要技术投入

3. 严格数据清洗、防机器人、注意力检查、非回应偏差检验需要较多资源

4. 操纵检验和每个实验单独的CFA会增加时间和被试成本

5. 实验4增加边界条件意味着样本量与实验轮次要翻倍

### what_not_to_copy_superficially_cn

1. 不能只把反馈文字命名为“示例式”而不展示具体钓鱼邮件并解释检测步骤

2. 不能在没有操纵检验的情况下声称两组反馈被感知为不同

3. 不能只报告交互显著而不给出主效应不显著的解释与交互图

4. 不能把边缘显著的H3b表述为强支持

5. 不能在没有实验4这类边界检验时声称示例式反馈普遍优于正念式反馈

6. 不能忽略在线实验与真实现场行为的差异而宣称现实有效性

- single_best_description_of_the_routine_cn：用理论把反钓鱼培训反馈拆成可比较的设计差异，再用多个在线实验从主效应、个体和消息层面交互到边界条件逐层闭合论证，最后把结果升华为理论机制和务实设计原则。

## 分析边界

全文文本可读，但附录中的邮件截图和部分图表仅以图片形式存在，未能逐字识别；locator以章节和段落为主，不提供精确页码；实验4的补充性原判断基于正文陈述。
