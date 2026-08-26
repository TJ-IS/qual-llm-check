# Feedback at scale: designing for accurate and timely practical digital skills evaluation

- 作者：Gabriele Piccoli; Joaquin Rodriguez; Biagio Palese; Marcin Lukasz Bartosiak
- 年份 / 期刊：2020 / European Journal of Information Systems
- DOI：10.1080/0960085x.2019.1701955
- 源文件：12330_2020_feedback-at-scale-designing-for-accurate-and-timely-practical-digital-skills-evaluation.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.78

## 文章级论证概况

- 核心问题：如何设计一个能够大规模提供准确、及时、实用数字技能表现反馈的社会技术制品，使其同时满足可扩展性、反馈有效性与可靠性，以及促进学习者行为参与的要求？

- 制品与设计：一个社会技术反馈系统，包含自定义学习者应用、基于Python的自动评分引擎、开放实验室人工辅导以及经过迭代设计的练习作业。核心设计特征包括：按技能分块的练习（chunking）、结构化起始文件、无截止日期的快速反馈循环、不计入最终成绩的自愿提交、仅以考试衡量掌握程度、AWS云托管与Lambda无服务器架构、基于XML解析的评分引擎和多答案键（multiple keys）。

- 客观结果：评分引擎对Excel和Word作业的评价速度比人工评分快两个数量级以上（秒级对分钟级）；在第二次迭代中Excel与Word的误报率分别约1.15%和3.64%，漏报率分别约0.46%和3.45%；第三次迭代在310名学习者的大规模部署中误报率分别为0.69%和3.20%，漏报率分别为2.44%和1.92%；练习提交完成率从第一次迭代的较低水平提高到第二次平均53.78%、第三次平均58.62%，平均分块完成率从63.68%提升至75.12%。

- 核心贡献：作者声称是面向“大规模反馈”问题类别的改进型知识贡献（improvement knowledge contribution），以证明性演示（proof-by-demonstration）方式提出5条元需求、14条设计原则及具体设计特征，说明只有将教学优先级、作业设计与自动化测量协同整合的社会技术制品才能实现可扩展、准确且及时的数字技能表现反馈。

- 整篇论证链：文章从全球数字技能需求旺盛与教育“大众化”导致班级规模扩大、反馈质量下降这一现实问题出发，指出现有商业课程产品依赖浏览器模拟、缺乏真实应用环境且不能兼顾规模与反馈质量。作者以干预理论为内核理论，将其三条原则转化为收集有效有用信息、赋予学习者自由知情选择、促进内部承诺的元需求与设计原则，并在真实大学入门信息系统中进行三轮设计-构建-评价循环。第一轮试点暴露出任务真实性与评分可靠性之间的权衡以及学习者完成率低的问题；第二轮通过分块作业、结构化起始文件、快速反馈循环改进，并以人工评分者和专家建立的地面真值为基准，证明评分引擎在速度和准确性上优于人工评分，同时完成率大幅提升；第三轮将评分引擎重构为AWS Lambda无服务器架构，在310名学习者的大规模场景中复现了可扩展性、有效性和参与度提升。讨论部分返回干预理论与ST制品视角，声称贡献是改进型设计知识，并指出社会要素的可扩展性、因果归因和学习成果提升仍有待未来研究。

## 类型与写作弧线判定

- 论文主类型判定：文章遵循DSRM过程模型，从问题识别、目标定义、设计开发、演示、评价到沟通，核心贡献是元需求、设计原则和设计特征，并以自然主义评价作为主要证据，属于典型的设计科学研究而不是行为实验或纯计算benchmark。

- 主导写作弧线判定：文章主线是：从干预理论和文献中提炼元需求与设计原则，据此构建社会技术制品，经过多轮评价反馈修正，最终以MR/DP/DF表格和讨论形式输出可复用设计知识；三段迭代被组织为要求→构建→评价→改进的循环，而不是单一理论检验或现象-机制-现场干预的弧线。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：第一阶段是解决方案定义与设计知识推导，将干预理论转化为MR和DP并评估商业产品；第二阶段是第一轮试点构建与自然主义部署，揭示真实性与可靠性/完成率之间的矛盾；第三阶段是第二轮重新设计与系统的地面真值评价，验证评分引擎相对人工评分的速度与准确性优势并观察完成率提升；第四阶段是第三轮无服务器重构与310人大规模部署，复现并强化三项目标证据，最终进入讨论提炼边界与未来研究。四个阶段相互衔接：第一阶段设定设计空间，第二阶段暴露出必须解决的缺陷，第三阶段证明改进方案有效并建立评价方法论，第四阶段测试边界和可扩展性。

### studies_or_phases

#### 1. 解决方案定义与设计原则推导阶段

- order：1

- name_cn：解决方案定义与设计原则推导阶段

- question_cn：干预理论及反馈文献如何转化为大规模数字技能反馈系统的元需求和设计原则？现有商业产品能否满足这些要求？

- inputs_and_setting_cn：干预理论（Argyris）、反馈干预元分析、形成性评价与自我调节学习文献，以及作者对SIMnet和MindTap等商业产品的教学使用与评价经验。

- designed_or_compared_object_cn：生成MR1-MR5、DP1.1-DP5.3，并决定放弃商业模拟环境，自建评分引擎。

- baseline_control_or_counterfactual_cn：以商业课程产品（浏览器模拟型）作为对照，指出其不符合干预理论和真实学习需求。

##### objective_metrics

（空）

- analysis_method_cn：理论驱动的推导和定性评估商业产品；按Walls等人的设计理论结构组织MR和DP。

- main_result_cn：形成5条元需求和14条设计原则，明确需要自建ST制品以同时实现任务真实、评价可靠、评价有效。

- argumentative_role_cn：为后面的制品构建提供设计知识与可追溯的理论基础，并界定问题类别的解空间。

- remaining_uncertainty_cn：这些MR和DP能否在实际课堂中产生预期的可扩展性、有效性和行为参与效果。

- link_to_next_phase_cn：需要构建并部署一个初始ST制品来检验MR和DP的可行性并发现问题。

##### evidence_pointers

1. Section 4 Solution definition

2. Section 5 Design: requirements and design principles

3. Table 1 MR/DP/DF mapping

#### 2. 第一轮试点迭代：初始ST制品部署与诊断

- order：2

- name_cn：第一轮试点迭代：初始ST制品部署与诊断

- question_cn：基于初始MR/DP构建的ST制品在真实学期课堂中能否实现设计目标？存在哪些问题？

- inputs_and_setting_cn：一个大学入门信息系统课程，约34名学习者的真实学期环境；6个Excel和3个Word练习作业；通过电子邮件每周提交并由人工/半自动方式反馈。

- designed_or_compared_object_cn：初始版本ST制品：完整的场景化作业、每周反馈、作业不计入最终成绩、正式考试衡量掌握程度。

- baseline_control_or_counterfactual_cn：没有外部对照组；以本学期的完成率趋势、出勤率、课程评价和期末问卷作为内部基准。

##### objective_metrics

1. 每次作业按时提交率

2. 课堂出勤率

3. 课程正式评价分数

4. 期末问卷中关于作业长度的意见比例

- analysis_method_cn：自然主义试点部署、每周研究团队审查、量化完成率统计和问卷分析。

- main_result_cn：出勤高、课程评价尚可，但作业完成率从Word 1的69.44%持续下降到Excel 5的3.45%；81.5%的受访者认为作业应该更短；发现真实任务在连续文件中会产生复合错误，造成真实性与评分可靠性之间的权衡。

- argumentative_role_cn：证明仅靠初始设计不能实现学习者参与目标，暴露了任务过大、反馈周期太长的问题，并形成下一轮设计的具体动因。

- remaining_uncertainty_cn：分块、更快的反馈和结构化起始文件是否能提高完成率，同时保持任务真实性和评价准确性。

- link_to_next_phase_cn：分析指出作业过重和反馈速度低是低完成率的原因，因此推动第二轮采用分块、结构化起始文件和快速反馈循环。

##### evidence_pointers

1. Section 7.1 First iteration

2. Table 2 Assignment completion rate (Pilot implementation)

3. Section 7.1 weekly meetings and survey sentence

#### 3. 第二轮迭代：重新设计与正式评价

- order：3

- name_cn：第二轮迭代：重新设计与正式评价

- question_cn：分块作业、结构化起始文件、无截止日期快速反馈能否提升完成率？评分引擎能否在有效性和可靠性上达到或超过人工评分者？

- inputs_and_setting_cn：真实学期课堂中的学习者；重设计的ST制品；期末考试中的Excel（27个任务/50个评价元素）和Word（14个任务/25个评价元素）；3名教学助理担任人工评分者，另1名专家建立地面真值。

- designed_or_compared_object_cn：第二轮ST制品：作业分块、每个分块提供上一分块答案键的副本作为起始文件、应用内drop-file提交、24小时内反馈、可选多次提交。

- baseline_control_or_counterfactual_cn：人工评分者的评分速度和准确性作为基准；专家逐文件重评构建的地面真值作为绝对标准；与第一轮完成率进行跨轮比较。

##### objective_metrics

1. 评分引擎与人工评分者平均评分时间

2. 与地面真值相比的任务评价正确率

3. 误报率、漏报率、总错误数

4. 评分不一致数

5. 作业提交完成率和差分

- analysis_method_cn：自然主义总结性评价；专家建立地面真值；将评分引擎与三名人工评分者逐任务比较；量化完成率和分块完成率。

- main_result_cn：评分引擎Excel平均3.61秒/文件而人工平均637.8秒/文件；评分引擎Excel任务正确率98.38%而人工为93%-96%；误报率不高于3.64%、漏报率不高于3.45%；完成率平均53.78%，比第一轮平均提高27.54个百分点。

- argumentative_role_cn：第一次用严格的地面真值证据证明自动评分引擎在速度和准确性上优于人工评分，同时证明重新设计提升了学习者参与，支撑“三目标可达”的核心主张。

- remaining_uncertainty_cn：班级规模仍小；评分流程需要人工干预；快反馈和分块对完成率提升的独立作用无法分离；是否能扩展到更大规模尚不清楚。

- link_to_next_phase_cn：高可靠性使流程可以进一步自动化，因此第三轮将评分引擎重构为无服务器架构，并在310人规模上复现评价。

##### evidence_pointers

1. Section 7.2.4 Scalability

2. Section 7.2.5 Validity and reliability

3. Tables 3 and 4

4. Table 5 Assignment completion rate (Second iteration)

#### 4. 第三轮迭代：无服务器重构与大规模自然主义评价

- order：4

- name_cn：第三轮迭代：无服务器重构与大规模自然主义评价

- question_cn：将评分引擎重构为AWS Lambda无服务器架构并在约310名学习者的真实课程中部署后，可扩展性、有效性和学习者参与是否仍能保持或改善？

- inputs_and_setting_cn：310名选课学生、4个课程班次；重新架构后的ST制品；考试文件数量为Word 5,727个评价要素、Excel 8,608个评价要素；5名评分者，其中3名曾参与第二轮评价。

- designed_or_compared_object_cn：第三轮ST制品：AWS S3触发Lambda进行评分、JSON格式反馈即时写入MongoDB、近实时结果可见；引入多个答案键处理边缘情形；未增加新MR或DP。

- baseline_control_or_counterfactual_cn：以第二轮结果作为跨迭代基准；人工评分者的速度作为可扩展性对照；专家地面真值作为准确性标准。

##### objective_metrics

1. 评分引擎平均评分时间

2. 总错误率、误报率、漏报率

3. 完成率和平均分块完成率

4. 可靠性抽查中不一致数

- analysis_method_cn：大规模自然主义总结性评价；专家建立地面真值；只用正确率最高的评分者重评；对5个最不一致任务做针对性可靠性分析。

- main_result_cn：评价时间仍以秒计；Excel总错误率3.13%，Word总错误率5.12%；误报率分别为0.69%和3.20%，漏报率分别为2.44%和1.92%；完成率平均58.62%，比第一轮平均提高32.39个百分点；平均分块完成率升至75.12%，标准差从21.43%降至4.69%。

- argumentative_role_cn：证明ST制品在接近十倍的规模扩大下没有性能退化，反而略有提升，从而强化外部有效性和可扩展性主张；同时说明无需新设计原则即可实现规模优化。

- remaining_uncertainty_cn：开放实验室等社会要素的可扩展性没有正式测量；无法因果分离分块与快速反馈的作用；未测量学习掌握程度是否真正提高；对不同数字技能领域的迁移性仍是推测。

- link_to_next_phase_cn：这些未决问题被转入讨论与未来研究，支撑关于设计边界、未来数字助推和学习成果评价的建议。

##### evidence_pointers

1. Section 7.3 Third iteration

2. Tables 6 and 7

3. Section 7.3.2 Validity and reliability

4. Section 7.3.3 Completion rate

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 数字技能需求和教育大众化压力

2. GAP: 需要可扩展的准确及时反馈系统

3. RQ_OR_OBJECTIVE: 提出MR/DP并设计ST制品

4. RESULT: 可扩展性、有效性和行为参与三目标证据

5. CONTRIBUTION: 教学优先、作业设计与自动测量的协同

### introduction_moves

1. CONTEXT: 数字技能定义和劳动力需求统计

2. PRACTICAL_STAKES: 中技能岗位对数字技能的高要求与自动化替代风险

3. PHENOMENON: 教育大众化导致班级规模扩大

4. PRIOR_KNOWLEDGE: 班级规模与学习成果负相关，反馈质量下降

5. GAP: 需要设计可扩展且准确及时的反馈系统

6. RQ_OR_OBJECTIVE: 本文目标

7. RESULT: 两数量级速度提升、误差低于人工、参与提升

8. CONTRIBUTION: ST制品与技术核心不足、需要三要素整合

9. STUDY_OVERVIEW: 论文结构

### theory_and_knowledge_moves

1. THEORY_INTRO: 引入干预理论

2. THEORY_PROPOSITION: 三条干预原则

3. MECHANISM: 三条原则相互依赖，信息→选择→承诺

4. PRIOR_KNOWLEDGE: 反馈类型与反馈干预元分析

5. PRIOR_KNOWLEDGE: 形成性评价和自我调节学习

6. THEORY_PROPOSITION: 进步原则和小胜利理论

### artifact_design_moves

1. REQUIREMENT: 从理论推导MR1-MR5与DP1-DP5

2. LIMITATION: 商业产品浏览器模拟的缺陷

3. DESIGN_FEATURE: 学习者应用的MEAN/AWS与响应式设计

4. DESIGN_FEATURE: 评分引擎的Python/XML解析与多答案键

5. DESIGN_FEATURE: 分块作业与结构化起始文件

6. DESIGN_FEATURE: 快速反馈循环和无截止日期提交

### evaluation_moves

1. METHOD_JUSTIFICATION: DSRM和自然主义总结性评价

2. RESULT: 第一轮低完成率与真实-可靠权衡

3. RESULT: 第二轮评分引擎速度与准确性优于人工

4. RESULT: 第二轮完成率提升

5. RESULT: 第三轮大规模复现

6. RESULT: 第三轮完成率和分块完成率改善

### discussion_and_contribution_moves

1. CONTRIBUTION: 改进型知识贡献和证明性演示

2. BOUNDARY_CONDITION: 社会要素可扩展性未测

3. LIMITATION_AND_FUTURE: 无法分离分块与快反馈效果

4. LIMITATION_AND_FUTURE: 评分引擎无法先验验证

5. BOUNDARY_CONDITION: 精确性与灵活性权衡、练习与考试配置不同

6. CONTRIBUTION: MR/DP可作为其他数字技能反馈系统的设计基础

## 理论/知识到设计的翻译

### 知识/理论基础

1. Intervention theory (Argyris, 1970)

2. Feedback literature (Hattie & Timperley, 2007; Kluger & DeNisi, 1996)

3. Formative assessment and self-regulated learning (Nicol & Macfarlane-Dick, 2006; Sadler, 1998)

4. Progress principle and small wins (Amabile & Kramer, 2011; Weick, 1984)

5. Design science research (Gregor & Hevner, 2013; Walls et al., 1992; Meth et al., 2015)

- 理论—设计耦合：partial

- 耦合判定理由：干预理论和反馈文献直接塑造了MR/DP以及教育层面的设计选择（不计分作业、自由选择、即时反馈、分块作业、开放实验室），但评分引擎的核心技术路线（XML解析、Python函数库、AWS Lambda、多答案键）主要来自工程约束、迭代试错和已有软件设计知识，而非干预理论推导；评价验证的是制品层面的三项目标，并没有直接检验干预理论的心理机制。因此是部分耦合而非完全前瞻性决定。

- 理论到设计翻译链：干预理论的有效有用信息原则→准确记录行为与表现、避免误报漏报→MR1/MR4→评分引擎、活动日志、即时反馈→地面真值比较中误报漏报率低；自由知情选择原则→不能将行为与学习混淆、学习者自我负责→MR2/MR3→作业不计入成绩、考试单独衡量、自愿提交→无成绩激励下完成率仍提升；内部承诺与进步原则→小胜利、可管理的真实任务→MR5→分块作业、结构化起始文件、现实任务→平均分块完成率提升；反馈文献→任务型、情境化、即时反馈→MR4/DP4→drop-file快速反馈和“实践结果”页面→第三次迭代中近实时反馈与完成率提高相关。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：干预理论：有效信息必须可验证且影响结果，有用信息必须可操作。

- mechanism_cn：准确的成绩与行为数据能使学生理解当前表现与目标差距并采取行动。

- design_requirement_cn：MR1：准确记录学习者行为与表现；MR4：尽快并情境化提供反馈。

- artifact_choice_cn：DF1/DF2个体化登录与活动日志；DF3/DF4自定义Python评分；DF10/DF11近实时与情境化反馈页面。

- evaluated_contrast_cn：评分引擎与人工评分者在地面真值上的误报漏报比较；第一轮到第三轮的反馈延迟从每周/24小时缩短到近实时。

- objective_result_cn：误报率最低0.69%、漏报率最低0.46%，评分引擎优于每位人工评分者；第三次迭代近实时反馈伴随更高完成率。

##### evidence_pointers

1. Section 5.1 MR1/DP1

2. Section 6.2 Grading engine

3. Section 7.2.5 Tables 3-4

4. Section 7.3.2 Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：干预理论：自由知情选择要求客户对干预有控制感；反馈文献表明任务型反馈优于导向自我的等级反馈。

- mechanism_cn：让作业与成绩脱钩、提供自愿反馈可以避免外部压力并促进自我调节学习。

- design_requirement_cn：MR2：不混淆行为与学习；MR3：让学习者成为自我负责单元并最大化控制。

- artifact_choice_cn：DF5作业提交被评价但不影响总分；DF6只有考试衡量掌握；DF7/DF8/DF9技能进阶、自动反馈和资源指引。

- evaluated_contrast_cn：在完全没有作业成绩激励的条件下观察完成率；与第一轮低完成率进行跨迭代对比。

- objective_result_cn：完成率仍从第一轮平均约26%左右上升到第二轮53.78%和第三轮58.62%，说明设计而非成绩激励驱动参与。

##### evidence_pointers

1. Section 5.2 MR2/MR3

2. Section 6.1 DF5/DF6

3. Section 7.2.6 Table 5

4. Section 7.3.3 Table 7

#### 3. 3

- theory_or_knowledge_claim_cn：干预理论：内部承诺来自对行动和结果的控制感；进步原则和小胜利理论认为可控的小成功产生前进动力。

- mechanism_cn：将大作业拆成一次可完成的小块，使学习者看到即时进展并保持持续努力。

- design_requirement_cn：MR5：培养学习者的进步感；DP5.1真实、DP5.2可管理、DP5.3范围有限。

- artifact_choice_cn：DF12真实任务；DF13分块作业；DF14结构化起始文件。

- evaluated_contrast_cn：第一轮大型作业与第二轮分块作业的完成率和分块完成率；第一轮“作业太长”问卷与第二轮问卷。

- objective_result_cn：第二轮平均每作业完成率53.78%，第三轮平均58.62%；平均分块完成率从63.68%升至75.12%，且变异性大幅下降。

##### evidence_pointers

1. Section 5.3 MR5/DP5

2. Section 7.2.1 DF13

3. Section 7.2.2 DF14

4. Tables 5 and 7

#### 4. 4

- theory_or_knowledge_claim_cn：反馈文献：任务层反馈和形成性反馈比导向自我的评价更能提升学习；即时反馈有利于自我调节。

- mechanism_cn：即时、逐任务、可解释的反馈让学习者在错误后立即重试，减少认知负荷和拖延。

- design_requirement_cn：MR4：尽快情境化反馈；MR3：为自愿提交的所有作业提供反馈。

- artifact_choice_cn：DF8逐任务自动反馈；DF10近实时评价（第二轮的24小时，第三轮的近实时）；DF11连接技能目标的反馈解释。

- evaluated_contrast_cn：第二轮24小时反馈与第三轮Lambda近实时反馈之间的完成率和分块完成率差异。

- objective_result_cn：第三轮完成率平均提升4.85个百分点，平均分块完成率从63.68%升到75.12%，但作者承认无法分离快反馈与分块效果。

##### evidence_pointers

1. Section 5.2 MR4/DP4

2. Section 7.2.3 Fast-cycle feedback

3. Section 7.3.3 Table 7

4. Section 8.4 Learners' engagement

## 评价逻辑

### evaluation_modes

1. 自然主义总结性评价（summative naturalistic evaluation）

2. 基于专家地面真值的准确性验证

3. 人工评分者作为基准的对比评价

4. 跨轮次重复指标追踪

5. 从34人到310人的大规模现场部署评价

- why_these_evaluations_cn：因为文章目标是证明ST制品在实际教育环境中同时实现可扩展性、有效性/可靠性和行为参与，所以必须采用真实学期课堂中的自然主义评价；可扩展性和准确性需要可量化的时间与错误率；由于人工评分是传统反馈方式，将评分引擎与人工评分者在地面真值上对比能证明自动化的价值；迭代DSR要求每轮结束后重新测量同一组指标以形成改进证据。

- benchmark_and_contrast_chain_cn：第一轮以自身完成率下降趋势作为问题诊断基准；第二轮引入人工评分者作为传统反馈的行为基线，并用专家重评构建地面真值作为绝对正确标准，评分引擎与每位人工评分者逐任务对比；同时以第一轮完成率作为跨迭代行为基线。第三轮以第二轮结果作为基线，并在更大规模上复现相同指标，形成从“初始失败→方案改进→正式基准→规模化复现”的累积证据链。

### claim_evidence_ledger

1. 技术主张：评分引擎比人工更快更准。证据：第二轮和第三轮评分时间对比、表3-4和表6中的地面真值错误率。

2. 制品主张：分块、起始文件和快速反馈共同提升完成率。证据：跨轮完成率提高和问卷比例，但缺少消融或随机对照，只能算关联而非因果。

3. 机制主张：干预理论和进步原则通过增进控制感和进步感影响行为。证据：间接来自完成率变化，没有直接测量内部承诺或主观控制感。

4. 边界主张：该系统适用于入门IS课程中Excel/Word数字技能评价，且可推广到一般“大规模反馈”问题类。证据：单校单课程现场部署，虽规模达310人，但社会要素可扩展性没有测量。

5. 设计知识：MR/DP/DF组合是可复用处方。证据：表1的映射和三轮评价结果，但未在其他技能领域或机构复现。

6. 理论贡献：将干预理论操作化为反馈系统设计知识。证据：理论到MR/DP的推导链条完整，但未对理论命题本身做实证检验。

- internal_validity_strategy_cn：采用专家重评同一批文件建立地面真值，用一个高精度评分者逐项复核，解决评分标准不确定性问题；评分引擎与人工评分者评价的是同一批考试文件、同一任务集和同一评分键；通过随机/分工方式避免文件选择偏差；对可靠性采用同一文档多人/多次比较和关键不一致任务专项审查。

- external_validity_strategy_cn：在真实学期课程中部署而非实验室；考试任务来自真实教学评估；第三轮扩大到310名学习者和4个班次；用自然主义评价补充了实验室评价缺失的现实约束；多次迭代在不同学期和不同学习群体上复现。

- what_is_not_actually_tested_cn：没有直接检验干预理论中的心理机制（如内部承诺、自由知情选择感知）；没有随机对照组或消融设计，无法分离分块、起始文件和快速反馈各自的贡献；没有测量学习者在数字技能掌握水平上的最终提升；没有正式测量开放实验室等社会要素的容量极限；没有将MR/DP推广到Word/Excel之外的其他数字技能。

## 贡献闭环

- technical_claim_cn：自定义自动评分引擎比人工评分者在实用数字技能任务上更快且更准确，可以支撑大规模反馈。

- artifact_claim_cn：将教学优先、作业设计和自动化测量协同整合的ST制品实现了可扩展性、反馈有效性/可靠性和学习者参与三项目标。

- mechanism_claim_cn：干预理论的有效信息、自由选择和内部承诺以及进步原则/小胜利是设计影响行为的机制；完成率提升被解释为这些机制的结果。

- boundary_claim_cn：当前验证限于微软Excel/Word数字技能和大学入门IS课程场景，但对更广泛的大规模反馈问题类别提供处方知识；社会要素（开放实验室）的可扩展性边界尚未确定。

- reusable_design_knowledge_cn：5条元需求、14条设计原则和对应设计特征（MR1-MR5、DP1.1-DP5.3、DF1-DF14），以及任务设计需要平衡真实性与可评价性的经验规则。

- theoretical_contribution_cn：属于Gregor和Hevner所称的改进型知识贡献：为已知问题开发新解决方案；将干预理论操作化到数字技能评价制品中，并强调ST制品由技术核心与人工专家协同构成，而不是单纯算法改进。

- how_discussion_closes_intro_gap_cn：讨论部分回到引言中教育大众化和数字技能需求的问题，声称所提出的MR/DP是面对更大规模数字技能培训的“行动基础”；指出商业现成方案无法兼顾真实性与反馈质量，而本研究的ST制品提供了可扩展的替代路径；同时用边界条件和未来研究对冲了“一次性性能结果”的风险。

- overclaim_or_unsupported_leaps_cn：将完成率提升归因于分块和快反馈属于设计层面的相关性推断而非因果证明；从单校Excel/Word场景推广到“数据可视化、机器学习”等更广数字技能缺乏实证；声称“积极影响学习者行为”主要基于提交率而非学习成果；开放实验室的社会可扩展性没有测量，却仍强调ST制品的整体可扩展性。

## 句级写作动作图谱

### 1. P1 S1-S4

- order：1

- section：Introduction

- locator：P1 S1-S4

- move_code：CONTEXT

- paraphrase_cn：Drucker预测知识技术人员增长，日常活动数字化要求个人获得更多数字技能；数字技能定义被引用。

- rhetorical_function_cn：从宏观趋势建立数字技能重要性。

- depends_on_cn：无，文章起点。

- sets_up_cn：为后文“需要在规模上培养数字技能”提供社会背景。

- evidence_pointer：Introduction P1

### 2. P1 S5-S7

- order：2

- section：Introduction

- locator：P1 S5-S7

- move_code：PRACTICAL_STAKES

- paraphrase_cn：中技能岗位的数字密集程度很高，2016年美国2700万招聘信息中82%要求数字技能；自动化可能造成大规模工作替代，学习新技能是应对之道。

- rhetorical_function_cn：用劳动力数据说明数字技能缺失的现实后果。

- depends_on_cn：承接数字技能重要性。

- sets_up_cn：说明解决数字技能培养问题的紧迫性。

- evidence_pointer：Introduction P1

### 3. P2 S1-S4

- order：3

- section：Introduction

- locator：P2 S1-S4

- move_code：PHENOMENON

- paraphrase_cn：教育大众化导致班级规模增大、MOOC和VLE兴起，教学效率和体验受损。

- rhetorical_function_cn：从社会趋势转向教育现场的具体现象。

- depends_on_cn：前一句对数字技能需求的铺垫。

- sets_up_cn：引出“可扩展反馈”问题。

- evidence_pointer：Introduction P2

### 4. P2 S5-S10

- order：4

- section：Introduction

- locator：P2 S5-S10

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究显示大班与学习掌握负相关；原因是匿名化、互动减少、反馈质量降低；反馈定义和反馈系统目标被引用。

- rhetorical_function_cn：借文献建立“大班损伤反馈”的既有共识。

- depends_on_cn：需要前文的现象作为经验锚点。

- sets_up_cn：为“需要面向大规模反馈的新设计”提供理论基础。

- evidence_pointer：Introduction P2

### 5. P3 S1-S5

- order：5

- section：Introduction

- locator：P3 S1-S5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文报告一个社会技术制品的设计、实施和评价，目标是解决数字技能掌握反馈的大规模提供问题。

- rhetorical_function_cn：正式提出研究目标。

- depends_on_cn：前文关于数字技能和反馈质量下降的问题。

- sets_up_cn：说明论文将采用DSR而非行为实验。

- evidence_pointer：Introduction P3

### 6. P3 S6-S10

- order：6

- section：Introduction

- locator：P3 S6-S10

- move_code：RESULT

- paraphrase_cn：预披露三个结果：评分速度比人工快两个数量级、误报漏报率低于人工（3.65%以下）、学习者对可选练习的参与提升。

- rhetorical_function_cn：提前给出核心证据，吸引读者并锚定贡献。

- depends_on_cn：研究目标句。

- sets_up_cn：后面评价部分以此三目标为结构。

- evidence_pointer：Introduction P3

### 7. P4-P5

- order：7

- section：Introduction

- locator：P4-P5

- move_code：CONTRIBUTION

- paraphrase_cn：制品是多轮设计-构建-评价的结果，包含IT核心、专家和设计好的学习反馈资源；核心观点是仅靠评分引擎不够，需要教学优先、作业设计和测量协同；贡献定位为改进型知识贡献。

- rhetorical_function_cn：声明贡献的性质和范围。

- depends_on_cn：前面提出的目标和结果。

- sets_up_cn：为“ST制品”这一关键概念铺垫。

- evidence_pointer：Introduction P4-P5

### 8. P6

- order：8

- section：Introduction

- locator：P6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：说明文章结构：问题与动机、内核理论与DSR方法、设计与开发、正式评价、讨论。

- rhetorical_function_cn：提供全文路线图。

- depends_on_cn：已完成贡献声明。

- sets_up_cn：指示读者进入理论部分。

- evidence_pointer：Introduction P6

### 9. P1 S1-S2

- order：9

- section：Theoretical foundations

- locator：P1 S1-S2

- move_code：THEORY_INTRO

- paraphrase_cn：干预理论提供总体框架，解释干预者如何帮助客户提升解决问题和决策的有效性。

- rhetorical_function_cn：引入内核理论。

- depends_on_cn：引言中说到的“Grounded in intervention theory”。

- sets_up_cn：后面的MR全部从该理论推导。

- evidence_pointer：Section 2 P1

### 10. P1 S3-S6

- order：10

- section：Theoretical foundations

- locator：P1 S3-S6

- move_code：THEORY_PROPOSITION

- paraphrase_cn：干预理论的三原则：有效有用信息、自由知情选择、内部承诺。

- rhetorical_function_cn：陈述理论关键命题。

- depends_on_cn：理论引入。

- sets_up_cn：成为五条元需求的结构来源。

- evidence_pointer：Section 2 P1

### 11. P2

- order：11

- section：Theoretical foundations

- locator：P2

- move_code：MECHANISM

- paraphrase_cn：三原则相互依赖：信息支撑选择、选择结果补充信息、正面结果强化内部承诺。

- rhetorical_function_cn：解释理论内部机制，为设计中的反馈循环提供逻辑。

- depends_on_cn：三原则定义。

- sets_up_cn：MR4的“即时反馈”和“行为数据记录”具有理论依据。

- evidence_pointer：Section 2 P2

### 12. P1 S1-S3

- order：12

- section：Methodology

- locator：P1 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用DSRM流程模型，设计科学研究本质是循环搜索问题空间，评价反馈回设计阶段。

- rhetorical_function_cn：为三轮迭代提供方法论合法性。

- depends_on_cn：理论部分结束。

- sets_up_cn：后文按迭代组织评价。

- evidence_pointer：Section 3 P1

### 13. P2

- order：13

- section：Methodology

- locator：P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：报告跨越三次迭代：第一次试点、第二次基于MR/DP的重新设计、第三次310名用户的规模部署。

- rhetorical_function_cn：预告评价部分的三个阶段。

- depends_on_cn：DSRM过程模型。

- sets_up_cn：为7.1-7.3三小节提供框架。

- evidence_pointer：Section 3 P2

### 14. P3-P4

- order：14

- section：Methodology

- locator：P3-P4

- move_code：REQUIREMENT

- paraphrase_cn：每轮使用自然主义总结性评价，并定义可扩展性、可靠性、有效性，以及误报和漏报。

- rhetorical_function_cn：将抽象的“有效性”操作化为可指标化的定义。

- depends_on_cn：设计科学评价文献。

- sets_up_cn：评价部分中的指标和表格。

- evidence_pointer：Section 3 P3-P4

### 15. P1-P2

- order：15

- section：Solution definition

- locator：P1-P2

- move_code：REQUIREMENT

- paraphrase_cn：根据干预理论，反馈系统必须收集有效有用信息并支持自由选择；问题类别要求可扩展到任意数量学习者。

- rhetorical_function_cn：将理论进一步翻译为解决方案空间条件。

- depends_on_cn：理论三原则。

- sets_up_cn：引出三个具体要求：真实任务、可靠评价、有效评价。

- evidence_pointer：Section 4 P1-P2

### 16. P3

- order：16

- section：Solution definition

- locator：P3

- move_code：LIMITATION

- paraphrase_cn：商业产品在浏览器模拟中教学，学生不在真实软件中操作，限制了技能掌握和概念理解，也会导致公式化学习和试错策略。

- rhetorical_function_cn：论证为什么不能直接购买现成解决方案。

- depends_on_cn：已确立的三项要求。

- sets_up_cn：自建评分引擎和技术核心。

- evidence_pointer：Section 4 P3

### 17. P4

- order：17

- section：Solution definition

- locator：P4

- move_code：GAP

- paraphrase_cn：因现有商业产品无法满足要求，作者决定设计自建方案以在真实Office应用中自动评估学习者作业。

- rhetorical_function_cn：澄清制品创新空间。

- depends_on_cn：商业产品缺陷。

- sets_up_cn：第五节MR/DP。

- evidence_pointer：Section 4 P4

### 18. Section 5 intro

- order：18

- section：Design: requirements and design principles

- locator：Section 5 intro

- move_code：REQUIREMENT

- paraphrase_cn：干预理论三原则为MR和DP提供总体架构，DP是用于创建同类制品的设计知识。

- rhetorical_function_cn：将理论转化为设计知识产出的合法性框架。

- depends_on_cn：干预理论和DSR方法。

- sets_up_cn：后续MR1-MR5的逐条推导。

- evidence_pointer：Section 5 intro

### 19. Section 5.1 P1-P2

- order：19

- section：Design: requirements and design principles

- locator：Section 5.1 P1-P2

- move_code：REQUIREMENT

- paraphrase_cn：有效信息必须影响结果且独立于结果；有用信息必须可行动；因此系统需要记录表现和行为数据。

- rhetorical_function_cn：为MR1提供理论依据。

- depends_on_cn：干预理论的有效信息原则。

- sets_up_cn：MR1及DP1.1-DP1.4。

- evidence_pointer：Section 5.1

### 20. After MR1

- order：20

- section：Design: requirements and design principles

- locator：After MR1

- move_code：REQUIREMENT

- paraphrase_cn：MR1要求准确记录行为与表现，DP1.1到DP1.4分别指向作业完成数据、学习资源使用、可靠测量和有效测量。

- rhetorical_function_cn：将抽象元需求分解为可操作设计原则。

- depends_on_cn：理论的有效信息原则。

- sets_up_cn：对应表1中的设计特征。

- evidence_pointer：Section 5.1 MR1/DP1

### 21. Section 5.2 P1

- order：21

- section：Design: requirements and design principles

- locator：Section 5.2 P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：自由知情选择要求避免用分数诱导学习，而是让学生对学习结果有控制感。

- rhetorical_function_cn：说明为什么作业不能影响成绩。

- depends_on_cn：干预理论第二原则。

- sets_up_cn：MR2和MR3。

- evidence_pointer：Section 5.2 P1

### 22. Section 5.2 P2

- order：22

- section：Design: requirements and design principles

- locator：Section 5.2 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：反馈元分析表明任务层反馈能提升表现，而导向自我的等级和表扬会削弱效果。

- rhetorical_function_cn：从反馈文献佐证“作业不计分但仍给反馈”的设计。

- depends_on_cn：Kluger和DeNisi、Hattie和Timperley等文献。

- sets_up_cn：MR2中“不混淆行为与学习”的要求。

- evidence_pointer：Section 5.2 P2

### 23. Section 5.2 P3

- order：23

- section：Design: requirements and design principles

- locator：Section 5.2 P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：形成性评价应视学习者为自我调节实体，反馈与评价分离并与学习目标紧密关联。

- rhetorical_function_cn：引入自我调节学习文献，支持自愿提交和考试独立衡量。

- depends_on_cn：形成性评价文献。

- sets_up_cn：MR3和DP3.1-DP3.3。

- evidence_pointer：Section 5.2 P3

### 24. MR2/MR3/MR4 block

- order：24

- section：Design: requirements and design principles

- locator：MR2/MR3/MR4 block

- move_code：REQUIREMENT

- paraphrase_cn：MR2要求不将行为与学习混为一谈；MR3要求学习者自我负责并最大化控制；MR4要求情境化、即时反馈。

- rhetorical_function_cn：集中输出由理论推导出的元需求。

- depends_on_cn：理论原则和反馈文献。

- sets_up_cn：对应DF5-DF11。

- evidence_pointer：Section 5.2 MR2-MR4

### 25. Section 5.3 P1-P2

- order：25

- section：Design: requirements and design principles

- locator：Section 5.3 P1-P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：内部承诺来自控制感和目标进展；进步原则和小胜利理论认为可控的小成功推动持续努力。

- rhetorical_function_cn：为MR5提供理论依据。

- depends_on_cn：内部承诺原则和进步原则。

- sets_up_cn：MR5和DP5.1-DP5.3。

- evidence_pointer：Section 5.3 P1-P2

### 26. Section 5.3 last P

- order：26

- section：Design: requirements and design principles

- locator：Section 5.3 last P

- move_code：REQUIREMENT

- paraphrase_cn：作业必须可管理；太简单或太难都会限制可行动反馈并阻碍小胜利。

- rhetorical_function_cn：将进步原则转化为“作业可管理”的具体设计要求。

- depends_on_cn：小胜利理论。

- sets_up_cn：第二轮的分块设计。

- evidence_pointer：Section 5.3 last paragraph

### 27. Section 6 intro P1

- order：27

- section：Demonstration: artefact development and implementation

- locator：Section 6 intro P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：开发过程中必须让作业结构与反馈系统协同；团队成员分别构建技能清单和熟悉商业产品，并迭代测试作业。

- rhetorical_function_cn：说明制品构建的协同过程，为“三要素协同”主张提供过程证据。

- depends_on_cn：MR/DP。

- sets_up_cn：具体的评分引擎和作业设计描述。

- evidence_pointer：Section 6 intro

### 28. Section 6 intro P2

- order：28

- section：Demonstration: artefact development and implementation

- locator：Section 6 intro P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：示例：Excel条件格式因评分引擎难以区分多个规则，团队修改任务描述，保证一个单元格区域最多只有一个条件格式规则，从而在保留教学目标的同时保证自动评分可行性。

- rhetorical_function_cn：用具体例子说明“任务设计与评分引擎协同”的微观机制。

- depends_on_cn：开发中的测试案例。

- sets_up_cn：指出真实性与可评性之间的设计权衡。

- evidence_pointer：Section 6 intro P2

### 29. Section 6 intro P3

- order：29

- section：Demonstration: artefact development and implementation

- locator：Section 6 intro P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：技术核心由学习者应用和评分引擎组成，设计特征被识别并汇总在表1中。

- rhetorical_function_cn：正式引入DF概念并与MR/DP连接。

- depends_on_cn：Meth等人的DF定义。

- sets_up_cn：6.1和6.2的技术细节。

- evidence_pointer：Section 6 intro P3

### 30. Section 6.1 P1-P2

- order：30

- section：Demonstration: artefact development and implementation

- locator：Section 6.1 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：学习者应用基于MEAN栈和AWS，响应式设计，支持多设备；自建方案使团队能同时控制技能识别、练习框架、评价方式和数据文件结构。

- rhetorical_function_cn：描述IT前端的核心设计特征。

- depends_on_cn：自制解决方案的必要性论证。

- sets_up_cn：DF1、DF2、DF12等条目落地。

- evidence_pointer：Section 6.1 P1-P2

### 31. Section 6.1 final P

- order：31

- section：Demonstration: artefact development and implementation

- locator：Section 6.1 final P

- move_code：DESIGN_FEATURE

- paraphrase_cn：应用通过Slack账号登录、GA记录行为、文件时间戳记录完成数据；提交后评分引擎评价并在“实践结果”中显示逐任务得分。

- rhetorical_function_cn：具体说明MR1和MR4如何被实现为界面功能。

- depends_on_cn：DF1/DF2/DF8。

- sets_up_cn：结果页面的图示和用户体验描述。

- evidence_pointer：Section 6.1 final paragraph

### 32. Section 6.2 P1-P2

- order：32

- section：Demonstration: artefact development and implementation

- locator：Section 6.2 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：评分引擎用Python解析Word/Excel压缩XML，以答案键为基准，在XML层级匹配学生工作而非只看输出结果，并通过参数和多个答案键处理等效解。

- rhetorical_function_cn：解释核心测量技术及其设计选择。

- depends_on_cn：DF3/DF4。

- sets_up_cn：后面准确性评价的技术基础。

- evidence_pointer：Section 6.2 P1-P2

### 33. Section 6.2 final P

- order：33

- section：Demonstration: artefact development and implementation

- locator：Section 6.2 final P

- move_code：DESIGN_FEATURE

- paraphrase_cn：评分引擎不是完整在线学习系统，而是ST制品的一个组件；开放实验室专家基于引擎标记的问题进行针对性帮助。

- rhetorical_function_cn：强调社会要素与IT核心的协同。

- depends_on_cn：ST制品概念和DF9。

- sets_up_cn：可扩展性讨论中的开放实验室部分。

- evidence_pointer：Section 6.2 final paragraph

### 34. Section 7.1 P1-P2

- order：34

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.1 P1-P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：第一轮试点包含6个Excel和3个Word作业，采用翻转课堂，每周邮件提交和每周反馈；作业不计入成绩，只有考试计入。

- rhetorical_function_cn：描述第一轮的设计与部署方式。

- depends_on_cn：MR2/DP2。

- sets_up_cn：第一轮评价结果。

- evidence_pointer：Section 7.1 P1-P2

### 35. Section 7.1 P3

- order：35

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.1 P3

- move_code：RESULT

- paraphrase_cn：周会分析揭示真实性与可靠性权衡；例如外部数据导入、嵌套IF拼写错误会导致后续任务复合错误。

- rhetorical_function_cn：用具体错误案例解释为什么连续大任务不可行。

- depends_on_cn：第一轮试点数据。

- sets_up_cn：模块化分块的动因。

- evidence_pointer：Section 7.1 P3

### 36. Section 7.1 P4-P5

- order：36

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.1 P4-P5

- move_code：RESULT

- paraphrase_cn：出勤和课程评价较高，但作业完成率持续下降；22/27受访者认为更短作业会更有效。

- rhetorical_function_cn：呈现第一轮的主要失败证据。

- depends_on_cn：完成率表和问卷。

- sets_up_cn：论证需要重新设计作业粒度。

- evidence_pointer：Section 7.1 P4-P5; Table 2

### 37. Transition after 7.1

- order：37

- section：Evaluation: iterative deployment and assessment

- locator：Transition after 7.1

- move_code：TRANSITION

- paraphrase_cn：根据DSR原则，作者从第一轮结果出发迭代制品设计。

- rhetorical_function_cn：在迭代之间建立逻辑连接。

- depends_on_cn：第一轮诊断。

- sets_up_cn：第二轮重新设计的三个措施。

- evidence_pointer：Section 7.1 final sentence

### 38. Section 7.2 P1

- order：38

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.2 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：第二轮重新设计采用分块作业、结构化起始文件和快速反馈循环。

- rhetorical_function_cn：预告第二轮设计方案。

- depends_on_cn：第一轮诊断。

- sets_up_cn：7.2.1-7.2.3详细描述。

- evidence_pointer：Section 7.2 P1

### 39. Section 7.2.1

- order：39

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.2.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：分块将每个作业拆成平均4.33个块，每块平均9.54个任务，而第一轮每作业平均35.66个任务；学生可以独立提交、跳过或多次练习特定块。

- rhetorical_function_cn：说明分块设计的具体形态和学习者控制机制。

- depends_on_cn：小胜利/进步原则。

- sets_up_cn：完成率提升的结果。

- evidence_pointer：Section 7.2.1; Figure 5

### 40. Section 7.2.2

- order：40

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.2.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：每个分块提供结构化起始文件，该文件是上一分块的答案键副本；这样隔离复合错误并减少误报漏报。

- rhetorical_function_cn：解释结构化起始文件的设计原理。

- depends_on_cn：第一轮真实-可靠权衡。

- sets_up_cn：可靠性和有效性结果。

- evidence_pointer：Section 7.2.2

### 41. Section 7.2.3

- order：41

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.2.3

- move_code：DESIGN_FEATURE

- paraphrase_cn：快速反馈循环采用drop-file上传，24小时内返回结果，学生可多次提交同一分块并收到每次反馈。

- rhetorical_function_cn：说明反馈即时性如何实现。

- depends_on_cn：MR4和DP4。

- sets_up_cn：完成率和参与度结果。

- evidence_pointer：Section 7.2.3

### 42. Section 7.2.4

- order：42

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.2.4

- move_code：RESULT

- paraphrase_cn：三名人工评分者平均评一个Excel考试文件需637.8秒，评分引擎只需3.61秒，速度差超过两个数量级。

- rhetorical_function_cn：用直接计时数据证明可扩展性。

- depends_on_cn：第二轮评价程序。

- sets_up_cn：第三轮“近实时大规模反馈”论证。

- evidence_pointer：Section 7.2.4

### 43. Section 7.2.5 P1

- order：43

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.2.5 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用专家重评所有文件建立地面真值，以保证人工评分者和评分引擎的比较有一个绝对正确标准。

- rhetorical_function_cn：说明为什么地面真值是可信的。

- depends_on_cn：评价有效性的需要。

- sets_up_cn：表3和表4中的错误率。

- evidence_pointer：Section 7.2.5 P1

### 44. Section 7.2.5 P2-P3

- order：44

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.2.5 P2-P3

- move_code：RESULT

- paraphrase_cn：评分引擎在Excel中任务正确率98.38%、Word中92.87%，高于所有人工评分者；误报漏报率在Excel和Word均不超过3.65%。

- rhetorical_function_cn：给出准确性证据。

- depends_on_cn：地面真值。

- sets_up_cn：证明“有效反馈”目标达成。

- evidence_pointer：Section 7.2.5; Tables 3 and 4

### 45. Section 7.2.6

- order：45

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.2.6

- move_code：RESULT

- paraphrase_cn：第二轮平均每作业完成率53.78%，比第一轮平均高27.54个百分点，改善在原本最低的作业上最明显。

- rhetorical_function_cn：证明重新设计提升了学习者参与。

- depends_on_cn：第一轮完成率基线。

- sets_up_cn：第三轮的进一步改善。

- evidence_pointer：Section 7.2.6; Table 5

### 46. Section 7.3 P1-P2

- order：46

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.3 P1-P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：第三轮不新增MR或DP，而是把评分引擎重构为AWS Lambda，无服务器触发，提交后近实时返回JSON反馈；部署到310名用户四个班次。

- rhetorical_function_cn：描述第三轮的技术变化和规模。

- depends_on_cn：第二轮的高可靠性。

- sets_up_cn：第三轮评价结果。

- evidence_pointer：Section 7.3 P1-P2

### 47. Section 7.3.1

- order：47

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.3.1

- move_code：RESULT

- paraphrase_cn：大规模评价中评分引擎仍以秒级完成Word和Excel文件，而人工评分者平均需要5分25秒，进一步说明自动化评价的可扩展性。

- rhetorical_function_cn：复现可扩展性主张。

- depends_on_cn：第三轮部署数据。

- sets_up_cn：讨论中关于技术核心可无限扩展但社会要素待测的区分。

- evidence_pointer：Section 7.3.1

### 48. Section 7.3.2

- order：48

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.3.2

- move_code：RESULT

- paraphrase_cn：第三轮总错误率Word 5.12%、Excel 3.13%，误报率低于3.2%、漏报率低于2.44%；引入多个答案键后，效果稳定且略微改善。

- rhetorical_function_cn：证明规模扩大不降低有效性。

- depends_on_cn：地面真值程序和多个答案键。

- sets_up_cn：讨论中关于评分引擎优势的解释。

- evidence_pointer：Section 7.3.2; Table 6

### 49. Section 7.3.3

- order：49

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.3.3

- move_code：RESULT

- paraphrase_cn：第三轮完成率平均58.62%，比第一轮高32.39个百分点，比第二轮高4.85个百分点；平均分块完成率升至75.12%，标准差显著下降。

- rhetorical_function_cn：证明快反馈和分块在更大规模上仍伴随参与提升。

- depends_on_cn：第二轮完成率基线和第三轮数据。

- sets_up_cn：回答“反馈百分比是否可比”的挑战。

- evidence_pointer：Section 7.3.3; Table 7

### 50. Section 7.3.3 last P

- order：50

- section：Evaluation: iterative deployment and assessment

- locator：Section 7.3.3 last P

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：作者主动回应“第一轮提交一个作业等价于第二轮提交全部分块”的质疑，用分块完成率数据和第一轮存在不完整提交的证据说明反馈百分比是合理的。

- rhetorical_function_cn：保护完成率指标不被削弱。

- depends_on_cn：第二轮和第三轮平均分块完成率。

- sets_up_cn：讨论部分的谨慎表述。

- evidence_pointer：Section 7.3.3 final paragraph

### 51. Section 8 intro

- order：51

- section：Discussion

- locator：Section 8 intro

- move_code：CONTRIBUTION

- paraphrase_cn：再次声明这是改进型知识贡献，并以证明性演示方式证明三项目标。

- rhetorical_function_cn：在讨论开头重新锚定贡献类型。

- depends_on_cn：全部评价结果。

- sets_up_cn：分节讨论每个目标的边界。

- evidence_pointer：Section 8 intro

### 52. Section 8.1

- order：52

- section：Discussion

- locator：Section 8.1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：技术核心可近乎无限扩展，但开放实验室等社会要素的容量可能随学习者数量线性增长，因此社会可扩展性是开放问题。

- rhetorical_function_cn：主动划定贡献边界。

- depends_on_cn：ST制品概念和第三轮部署。

- sets_up_cn：未来研究建议。

- evidence_pointer：Section 8.1

### 53. Section 8.2 P1

- order：53

- section：Discussion

- locator：Section 8.2 P1

- move_code：MECHANISM

- paraphrase_cn：评分引擎优势来自直接读取XML表示和处理速度；它比人工评分者更能检查所有单元格和效率性操作，例如一次删除25个超链接而不是逐个删除。

- rhetorical_function_cn：解释为什么自动评分不仅快而且更准。

- depends_on_cn：表3-6的准确性证据。

- sets_up_cn：关于效率性数字元技能的讨论。

- evidence_pointer：Section 8.2 P1

### 54. Section 8.2 P2

- order：54

- section：Discussion

- locator：Section 8.2 P2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：评分引擎无法在作业实施前先验验证任务；未来需要研究严格匹配与灵活评价的最优组合。

- rhetorical_function_cn：指出知识的边界和下一步研究。

- depends_on_cn：评分引擎的规则本质。

- sets_up_cn：多答案键与先验答案生成方法的提议。

- evidence_pointer：Section 8.2 P2

### 55. Section 8.3

- order：55

- section：Discussion

- locator：Section 8.3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：精确性与灵活性存在权衡；练习等形成性评价可以严格匹配，考试等总结性评价应更灵活；设计还可把重复性任务作为单个加权任务，以鼓励数字化元技能而不是惩罚小错误。

- rhetorical_function_cn：把评价结果转化为可复用的设计权衡知识。

- depends_on_cn：第二轮和第三轮的误差分析。

- sets_up_cn：关于数字元技能框架的未来研究。

- evidence_pointer：Section 8.3

### 56. Section 8.4

- order：56

- section：Discussion

- locator：Section 8.4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者承认数据无法分离分块与快速反馈各自的效应，未来需要通过行为科学范式做控制实验；同时指出分块层面的绝对完成率仍不高，可考虑数字助推。

- rhetorical_function_cn：诚实交代因果归因限制，并引出未来方向。

- depends_on_cn：跨迭代完成率分析。

- sets_up_cn：下一节关于更广泛数字技能掌握的研究议程。

- evidence_pointer：Section 8.4

### 57. Section 8.5

- order：57

- section：Discussion

- locator：Section 8.5

- move_code：CONTRIBUTION

- paraphrase_cn：MR和DP可作为多种数字技能反馈系统的设计基础；教育组织需要同时投资技术组件和社会组件。

- rhetorical_function_cn：把贡献从单一Office技能扩展到更大的问题类别。

- depends_on_cn：全部研究和讨论。

- sets_up_cn：结论。

- evidence_pointer：Section 8.5

## 写作技术

- gap_construction_cn：从全球数字技能需求和劳动力数据出发，把“反馈质量随班级规模下降”作为既有共识，再论证商业产品只能满足模拟练习而不能提供真实、可规模化的反馈，从而把缺口定位为“现有制品不能满足反馈规模与质量兼备”的问题，而不是单纯“没人研究”。

- signposting_cn：摘要直接给出三目标；引言预告两个数量级速度、低于人工的错误率和行为参与提升；方法论预告三轮迭代；评价部分每轮用明确小标题（Scalability、Validity and reliability、Completion rate）重复同一组指标，形成强路标。

- transition_logic_cn：每轮结束都用评价结果的内在矛盾驱动下一轮：第一轮低完成率→需要分块和更快反馈；第二轮高可靠性→可以自动化并扩大规模；第三轮大规模成功→进入边界与未来研究。段落间常用“Given...”“Our analysis indicated...”“The results... thus...”等逻辑链。

- claim_evidence_rhythm：先给出MR/DP的处方性主张，再用“The results indicate...”“The evaluation suggests...”“Table X shows...”的格式逐项给出指标；在解释结果时又回到设计特征，形成“设计要求→制品特征→客观结果→机制解释”的节奏。

- benchmark_narrative_cn：不设置抽象的SOTA模型，而是把人工评分者作为最自然的行为基线，把专家地面真值作为绝对正确标准；通过“速度对比”和“准度对比”的双重benchmark，把评分引擎置于传统人工反馈的替代位置，再通过跨轮完成率差分形成行为基准。

- theory_return_cn：讨论部分没有停留在性能数字，而是回到干预理论的有效信息、自由选择和内部承诺，把完成率提升解释为设计增强控制感和进步感的结果；同时用ST制品概念强调社会组件不可或缺，从而把结果与理论命题重新绑定。

- contribution_positioning_cn：明确使用“improvement knowledge contribution”“proof-by-demonstration”“meta-requirements and design principles”等DSR术语，把论文置于Gregor和Hevner的分类框架中，既避免宣称新理论，也不让贡献退化为单个系统的技术报告。

- novelty_protection_cn：通过三条策略防止贡献退化为一次性性能结果：一是强调ST制品而非单纯算法；二是提炼MR/DP/DF三层可复用知识；三是主动指出未测边界（社会可扩展性、因果分离、学习成果），以诚实限制换取一般化可信度。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用宏观社会趋势和统计数据建立问题重要性，并把一般问题收缩为“大规模反馈”问题类。

- research_job_cn：识别目标场景中的具体利益相关者、关键缺口和现有制品不足。

- required_evidence_cn：劳动力统计、班级规模与学习成果文献、商业产品评价资料。

- transition_to_next_cn：证明现有方法不满足要求，需要新的设计知识。

#### 2. 2

- step：2

- writing_job_cn：引入内核理论，逐条推导元需求和设计原则，并建立MR/DP/DF映射表。

- research_job_cn：选取能够指导设计选择的理论，形成可追踪的设计知识链条。

- required_evidence_cn：理论命题与设计原则之间的一一对应逻辑，以及每项DP对应的具体DF。

- transition_to_next_cn：从设计知识转向具体制品构建。

#### 3. 3

- step：3

- writing_job_cn：描述第一轮原型构建和试点部署，说明环境、参与者、反馈流程和初始设计选择。

- research_job_cn：在小规模真实环境中部署初始制品，收集日志、完成率、问卷和观察。

- required_evidence_cn：试点期完成率数据、用户反馈、开发过程中的错误案例。

- transition_to_next_cn：用诊断性结果指出初步设计的缺陷。

#### 4. 4

- step：4

- writing_job_cn：展示重新设计的具体措施，并解释每一措施对应哪条MR/DP/DF。

- research_job_cn：基于第一轮问题，进行分块、结构化起始文件、反馈加速等设计修改。

- required_evidence_cn：设计修改与问题之间的因果对应，以及用户感知改善（问卷）。

- transition_to_next_cn：通过正式评价证明改进有效。

#### 5. 5

- step：5

- writing_job_cn：采用地面真值、人工基准和跨轮完成率指标进行正式评价，并用表格报告速度、错误率和行为指标。

- research_job_cn：设计可复现的评价协议：专家重评、独立评分者、同一任务集、时间记录。

- required_evidence_cn：评分引擎与人工评分者在地面真值上的对比、完成率差分。

- transition_to_next_cn：若评价结果支持目标，则进行更大规模部署测试边界。

#### 6. 6

- step：6

- writing_job_cn：报告第三轮的架构优化和规模部署，强调指标没有退化。

- research_job_cn：将系统重构为可弹性扩展的架构，在更大用户规模上复现评价。

- required_evidence_cn：大规模错误率、秒级评价时间、完成率和一致性指标。

- transition_to_next_cn：回到理论和文献，提炼边界条件。

#### 7. 7

- step：7

- writing_job_cn：讨论贡献类型、边界条件和未来研究，主动承认未测项。

- research_job_cn：把结果提升为可复用设计知识，并识别仍需行为科学验证的机制。

- required_evidence_cn：MR/DP/DF汇总、边界证据、未来研究逻辑。

- transition_to_next_cn：结束全文，给读者留下可操作的设计原则清单。

### most_transferable_moves_cn

1. 用MR/DP/DF三层映射把理论转化为设计知识，并直接用一个汇总表展示；

2. 用“地面真值+人工评分者”作为自动评价系统的基准，而不是只报绝对准确率；

3. 每轮评价重复同一组指标，方便读者做跨轮差分；

4. 主动用具体错误案例解释设计权衡，如条件格式和嵌套IF；

5. 在讨论中先声明贡献类型，再划边界，再给未来研究。

### resource_intensive_or_nonstandard_parts_cn

1. 自定义评分引擎需要能够解析Office XML格式并编写针对具体任务的通用函数，工程量较高；

2. 三轮真实学期课程部署需要长期进入教学现场，且涉及大量学生数据和多名教学助理；

3. 建立地面真值要求高技能专家逐文件重评全部考试文件，成本较高；

4. AWS Lambda、云存储和MongoDB基础设施需要经费与开发能力；

5. 开放实验室人工辅导资源是ST制品的一部分，复现时不能只复制软件。

### what_not_to_copy_superficially_cn

1. 不能只画MR/DP表格而不展示从理论到设计特征的推导证据；

2. 不能只报告完成率提升而不提供跨轮基线和分块完成率，否则会犯可比性错误；

3. 不能把完成率等价于学习掌握，文中作者也承认没有测最终掌握程度；

4. 不能把分块和快反馈说成因果效果，除非做了消融或随机对照；

5. 不能把单校、Office场景直接推广到所有数字技能，必须像作者一样用边界条件保护贡献。

- single_best_description_of_the_routine_cn：以理论推导出元需求与设计原则，用三轮“构建-诊断-重设计-再评价”的真实课堂部署，将自动评分引擎与人工评分、地面真值、跨轮完成率比较，最终把一次性系统证据还原为可复用的ST反馈系统设计知识。

## 分析边界

全文文字完整，但部分图表为图片OCR，代码截图的细节无法精确核对；研究人数和部分指标需从表格推测（如第一轮完成率百分比反推学生数）；无法访问在线仓库验证评分引擎代码；地面真值仅由一名专家建立，文中并未讨论其自身可能的偏差；对轮次之间完成率差异的因果归因作者自己也承认不充分。
