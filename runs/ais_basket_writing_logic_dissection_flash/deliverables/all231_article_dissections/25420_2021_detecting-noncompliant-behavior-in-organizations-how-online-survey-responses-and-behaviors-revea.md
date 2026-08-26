# Detecting Noncompliant Behavior in Organizations: How Online Survey Responses and Behaviors Reveal Risk

- 作者：Jeffrey L. Jenkins; Joseph S. Valacich; Aaron F. Zimbelman; Mark F. Zimbelman
- 年份 / 期刊：2021 / Journal of Management Information Systems
- DOI：10.1080/07421222.2021.1962600
- 源文件：25420_2021_detecting-noncompliant-behavior-in-organizations-how-online-survey-responses-and-behaviors-revea.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.85

## 文章级论证概况

- 核心问题：组织能否通过在线问卷中的回答内容与鼠标移动行为，低成本、大规模地评估员工的不合规风险？

- 制品与设计：嵌入鼠标追踪的Qualtrics在线问卷：包含“什么行为构成不合规/作弊”的合规定义题与“对不合规行为应施加何种后果”的后果适当性题；用自定义JavaScript毫秒级记录鼠标坐标，计算实际移动路径与理想响应轨迹之间的附加距离，并用人口统计确认题作为个人基线将偏差z-score标准化；题目顺序随机化并作为控制变量。

- 客观结果：在950名MTurk参与者中，405人被客观判定为提前查看答案（不合规）。不合规者在合规定义题上显著更宽松（β=-0.83, p<0.001），在后果适当性题上显著更宽松（β=-2.04, p<0.001）；在合规定义题上鼠标偏移显著更大（β=1.13, p<0.05），但在后果题上鼠标偏移无显著差异（β=-0.10, p>0.05）。将回答与鼠标偏差联合输入基础逻辑回归，测试集准确率72.79%，AUC=0.718，敏感性0.644，特异性0.792；10折交叉验证AUC=0.748。

- 核心贡献：首次在学术上实证检验实务审讯中“询问后果适当性能揭示违规者”的策略；提出并验证认知失调会通过更宽松的回答和鼠标轨迹偏移表现出来；将回答内容与鼠标行为联合作为非侵入、低成本、可规模化的不合规风险评估工具，并扩展了鼠标追踪与认知失调研究。

- 整篇论证链：作者先以巨额罚款和少数员工违规造成巨大损失来建立现实紧迫性，再指出自我报告问卷因社会期望和恐惧而不准确，从而形成对低成本合规风险评估工具的需求。随后引入认知失调理论与反应激活模型，提出不合规者在回答“什么构成不合规”和“后果多严重才适当”这两类问题时，会因内心冲突而给出更宽松的回答并出现更大的鼠标移动偏差。为验证这一机制，作者设计了一个有真实金钱激励、且可匿名查看答案的在线能力测试，客观区分了作弊者与未作弊者；随后用线性混合效应模型检验四个假设，发现三个支持、一个不支持；为弥补模型解释力较低的问题，作者进一步用基础逻辑回归将回答与鼠标偏差联合用于分类，并报告了可接受的判别性能；最终在讨论中把“更宽松回答+异常鼠标移动”联合模式解释为认知失调的证据，并据此提出组织风险评估工具与多项理论贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心不是从需求出发迭代构建信息系统，而是从认知失调理论、反应激活模型和亚运动模型推导出可检验的问卷问题类型与鼠标偏移指标，再通过真实行为实验检验这些理论预测，最后用分类模型证明其实际工具价值。

- 主导写作弧线判定：全文遵循“现实问题—理论机制—设计/测量—实验检验—回到理论解释贡献”的弧线：先以合规代价引出问题，以CD和RAM推导假设，设计特殊问卷与鼠标偏差测量，用在线实验和分类模型检验，最后在讨论中把结果重新连接到认知失调理论并界定边界。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：预测试确保主实验可行且能诱发足够作弊；主实验获得基于真实行为的客观不合规标签；探索性分析验证鼠标运动符合亚运动模型；线性混合效应模型检验四个假设；补充稳健性分析排除措辞、聚合和残差分布等替代解释；逻辑回归分类模型将统计差异转化为实际风险判别力，并用假设审计情景说明管理收益。这些阶段先从内部有效性走向统计可靠性，再从统计可靠性走向实用价值。

### studies_or_phases

#### 1. 方法论预测试与作弊诱发调整

- order：1

- name_cn：方法论预测试与作弊诱发调整

- question_cn：如何确保能准确追踪作弊行为并诱发出足够数量的自愿作弊样本？

- inputs_and_setting_cn：5轮预测试，共95名参与者；在MTurk/在线环境测试能力测试题、报酬结构和指导语措辞。

- designed_or_compared_object_cn：比较不同报酬方案和指令措辞对作弊率与追踪准确性的影响。

- baseline_control_or_counterfactual_cn：不同预测试版本之间的迭代对比，没有正式对照组。

##### objective_metrics

1. 作弊行为追踪成功率

2. 作弊发生率

- analysis_method_cn：迭代式预测试与描述性检查。

- main_result_cn：最终确定了能够准确追踪作弊并提高参与者作弊倾向的方法流程。

- argumentative_role_cn：确保主实验的内部有效性和足够的非合规样本量。

- remaining_uncertainty_cn：未提供正式统计推断，不知道效应大小。

- link_to_next_phase_cn：为大规模主实验提供成熟的方法流程。

##### evidence_pointers

1. Method 中 Pilot Tests 小节

#### 2. 在线能力测试实验与客观不合规测量

- order：2

- name_cn：在线能力测试实验与客观不合规测量

- question_cn：在有真实金钱激励和机会的情况下，参与者是否会自愿选择不合规，并在后续问卷中表现出不同回答和鼠标行为？

- inputs_and_setting_cn：950名MTurk参与者；5道改编GMAT能力题；Qualtrics问卷；个性化答案链接；0-10量表合规题和后果题；人口统计确认基准题。

- designed_or_compared_object_cn：设计作弊机会与激励结构；随机化题序；比较后续被客观判定为作弊者与未作弊者。

- baseline_control_or_counterfactual_cn：未作弊者作为对照组；随机化题目顺序；人口统计确认题作为个人鼠标移动基线。

##### objective_metrics

1. 是否提前点击查看答案（二值）

2. 合规题宽松度（0-10）

3. 后果题宽松度（0-10）

4. 鼠标移动附加距离

- analysis_method_cn：受控在线实验；通过定制链接和JavaScript隐形记录行为；描述统计。

- main_result_cn：405人被分类为不合规，533人合规；描述性统计显示不合规者在回答和部分移动指标上有差异。

- argumentative_role_cn：生成基于真实行为的客观因变量，使后续因果推断成为可能。

- remaining_uncertainty_cn：描述性差异未经过统计推断；存在个体异质性噪声。

- link_to_next_phase_cn：为探索性运动模型检验和假设检验提供数据。

##### evidence_pointers

1. Method 全部

2. Appendix D 描述统计

#### 3. 鼠标运动亚运动模型探索性检验

- order：3

- name_cn：鼠标运动亚运动模型探索性检验

- question_cn：鼠标轨迹数据是否符合随机优化亚运动模型所预言的初始移动后纠正性子运动？

- inputs_and_setting_cn：主实验鼠标轨迹x-y坐标与时间戳。

- designed_or_compared_object_cn：计算每个移动点相对x轴的角度、角度变化、z分数；与显著性阈值1.645比较。

- baseline_control_or_counterfactual_cn：无干预；只是检验数据与理论模型的拟合。

##### objective_metrics

1. 每次连续移动中显著角度变化的次数

- analysis_method_cn：角度变化z-score检验。

- main_result_cn：平均出现1.46次显著角度变化（SD=1.65），支持亚运动模型。

- argumentative_role_cn：在正式假设前论证鼠标偏移指标的神经运动学基础，为使用RAM解释偏差提供依据。

- remaining_uncertainty_cn：只支持基础运动模型，不涉及认知失调。

- link_to_next_phase_cn：支持在H1b/H2b中将移动偏差解释为认知竞争的结果。

##### evidence_pointers

1. Analysis 第一段

#### 4. 线性混合效应模型假设检验（H1a–H2b）

- order：4

- name_cn：线性混合效应模型假设检验（H1a–H2b）

- question_cn：不合规是否导致对合规定义和后果适当性的回答更宽松，并在回答合规题和后果题时鼠标偏移更大？

- inputs_and_setting_cn：合规题/后果题回答、鼠标偏差z分数、作弊二值、题目顺序；每题作为随机效应。

- designed_or_compared_object_cn：比较作弊者与非作弊者；运动指标使用稳健线性混合效应模型处理非正态残差。

- baseline_control_or_counterfactual_cn：非作弊者作为对照组；题序作为控制变量；每题随机效应吸收题目间差异。

##### objective_metrics

1. β系数

2. t值

3. p值

4. 条件/边际r平方

- analysis_method_cn：线性混合效应模型；稳健LMM；汇总结果表。

- main_result_cn：H1a支持（β=-0.83）；H2a支持（β=-2.04）；H1b支持（β=1.13）；H2b不支持（β=-0.10，p>0.05）。

- argumentative_role_cn：直接检验认知失调理论推导出的行为预测，建立非合规对回答与移动的组间效应。

- remaining_uncertainty_cn：部分模型r平方较低，需评估实际预测价值；H2b未支持说明后果题上的移动信号弱。

- link_to_next_phase_cn：低r平方促使进行分类精度分析，检验实用价值。

##### evidence_pointers

1. 表1-表5

2. Analysis 第二至最后段

#### 5. 补充与稳健性分析

- order：5

- name_cn：补充与稳健性分析

- question_cn：主要结果是否稳健于不同的作弊自报措辞、回答聚合方式和鼠标偏差变换？

- inputs_and_setting_cn：主实验数据；语言操作（neutral vs hard self-report）、平均答题得分、对数转换偏差。

- designed_or_compared_object_cn：比较不同自报措辞条件；比较传统平均回归vs项目级LMM；比较log变换vs原始偏差。

- baseline_control_or_counterfactual_cn：不同分析规格互为稳健性对照。

##### objective_metrics

1. 定性一致的显著性模式

2. 质变的p值方向

- analysis_method_cn：替代回归、对数变换、条件比较。

- main_result_cn：语言条件无差异；平均回归、log变换结果定性一致。

- argumentative_role_cn：排除主要结果由措辞、聚合层次或残差分布造成的可能性。

- remaining_uncertainty_cn：稳健性分析不能提高r平方；H2b仍不显著。

- link_to_next_phase_cn：稳健性确认后进入更接近应用的分类模型。

##### evidence_pointers

1. Notes 7, 8, 11

#### 6. 逻辑回归分类模型与资源分配情景

- order：6

- name_cn：逻辑回归分类模型与资源分配情景

- question_cn：将回答宽松度与鼠标偏移联合，能否在个体层面识别不合规风险并带来管理收益？

- inputs_and_setting_cn：参与者的合规/后果回答和合规/后果题鼠标偏差；80%训练/20%测试；10折交叉验证。

- designed_or_compared_object_cn：基础逻辑回归（无调参）预测不合规二值；与随机审计反事实比较。

- baseline_control_or_counterfactual_cn：随机审计作为反事实；80/20测试和10折CV验证性能。

##### objective_metrics

1. 准确率

2. AUC

3. 敏感性

4. 特异性

- analysis_method_cn：逻辑回归；10折交叉验证；假设性审计情景运算。

- main_result_cn：测试集准确率72.79%，AUC=0.718，敏感性0.644，特异性0.792；10折CV AUC=0.748；假设情景下可识别2.58倍不合规案例并少用15.1%审计资源。

- argumentative_role_cn：把组间统计差异转化为可操作的风险评估绩效，回应“实际意义”的疑问。

- remaining_uncertainty_cn：未做消融分析以分离回答和移动各自贡献；未在真实组织中测试；广泛采用可能改变工具效力。

- link_to_next_phase_cn：在讨论中将分类效用与理论机制结合，提出未来研究。

##### evidence_pointers

1. Classification Accuracy 小节

2. 图6

3. Note 13

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. RQ_OR_OBJECTIVE

4. THEORY_INTRO

5. HYPOTHESIS_OR_PROPOSITION

6. STUDY_OVERVIEW

7. RESULT

8. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PHENOMENON

3. PRACTICAL_STAKES

4. LIMITATION

5. WHY_GAP_MATTERS

6. RQ_OR_OBJECTIVE

7. THEORY_INTRO

8. MECHANISM

9. STUDY_OVERVIEW

10. RESULT

11. CONTRIBUTION

12. BOUNDARY_CONDITION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. GAP

3. THEORY_INTRO

4. THEORY_PROPOSITION

5. MECHANISM

6. HYPOTHESIS_OR_PROPOSITION

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. METHOD_JUSTIFICATION

4. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. RESULT

2. CONTRIBUTION

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 认知失调理论（Festinger, 1957; Harmon-Jones & Mills）

2. 反应激活模型（RAM, Welsh & Elliott 2004）

3. 随机优化亚运动模型（Meyer et al. 1988）

4. 工作场所越轨文献（Griffin & O'Leary-Kelly 2004）

5. 实务审讯技术（Inbau et al. 2001）

6. 鼠标追踪测量文献（Jenkins et al. 2017, 2019; Freeman et al. 2011）

- 理论—设计耦合：direct

- 耦合判定理由：理论前瞻性地决定了问卷的两类问题（合规定义题、后果适当性题）和鼠标偏移这一核心行为指标；认知失调与RAM被直接转化为具体测量设计和假设。鼠标追踪技术来自既有研究，但只是使能工具，不削弱理论到设计的直接关系。

- 理论到设计翻译链：认知失调理论 → 不合规者面对自身行为与信念冲突时会修改信念 → 设计要求问“什么构成不合规”和“后果应多严重” → 生成合规题与后果题；RAM/亚运动模型 → 竞争性认知会并行启动多个动作程序 → 设计要求记录实际移动路径与理想路径的距离 → 生成鼠标偏差指标并用控制题标准化；实务审讯主张 → 违规者倾向给出宽松后果 → 加入后果问题并首次实证；最后将回答宽松度与鼠标偏差联合作为分类特征，检验实际判别力。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：认知失调理论：行为与信念冲突会产生心理不适，个体倾向修改信念以减少不适。

- mechanism_cn：不合规者被问“什么行为算违规”时，会潜意识调整定义，使自己的行为看起来更可接受。

- design_requirement_cn：问卷必须包含对具体越轨行为进行合规/违规判定的题目。

- artifact_choice_cn：合规定义题（Appendix B），例如“提前查看答案是否算作弊”，0-10量表。

- evaluated_contrast_cn：客观作弊者与未作弊者的回答宽松度。

- objective_result_cn：H1a支持，β=-0.83，p<0.001。

##### evidence_pointers

1. 表1

2. Appendix B

#### 2. 2

- theory_or_knowledge_claim_cn：认知失调与恐惧被惩罚会促使违规者对后果态度更宽松。

- mechanism_cn：不合规者因害怕被抓住及后果，在评价惩罚时倾向选择更宽松的后果以降低恐惧。

- design_requirement_cn：问卷必须包含对潜在非合规后果适当性的评价题目。

- artifact_choice_cn：后果适当性题（Appendix C），例如“被举报、任务被拒、无奖金、被拉黑”的适当性，0-10量表。

- evaluated_contrast_cn：作弊者与未作弊者对后果适当性的评分。

- objective_result_cn：H2a支持，β=-2.04，p<0.001。

##### evidence_pointers

1. 表2

2. Appendix C

#### 3. 3

- theory_or_knowledge_claim_cn：反应激活模型（RAM）：多个具有行动潜势的刺激会并行启动动作程序，导致手部轨迹偏离理想路径。

- mechanism_cn：合规题会同时激活“客观回答”和“更宽松回答”，大脑并行编程两个反应，直到抑制后选择。

- design_requirement_cn：需要以高时间精度连续记录鼠标坐标，计算实际距离与理想轨迹距离之差。

- artifact_choice_cn：Qualtrics中嵌入自定义JavaScript，毫秒级记录x-y坐标与时间戳；计算附加距离并z-score标准化。

- evaluated_contrast_cn：作弊者与未作弊者在合规题上的鼠标偏移z分数。

- objective_result_cn：H1b支持，β=1.13，p<0.05。

##### evidence_pointers

1. 表3

2. Mouse Movement Measurement 小节

#### 4. 4

- theory_or_knowledge_claim_cn：RAM同样适用于后果题：对“客观应得后果”与“希望获得的宽松后果”的竞争会引起鼠标偏移。

- mechanism_cn：后果题本应激活更多认知竞争，从而使不合规者鼠标偏移更大。

- design_requirement_cn：后果题也必须记录同样的鼠标偏移指标。

- artifact_choice_cn：后果适当性题嵌入鼠标追踪，计算与合规题相同的偏差指标。

- evaluated_contrast_cn：作弊者与未作弊者在后果题上的鼠标偏移z分数。

- objective_result_cn：H2b未支持，β=-0.10，p>0.05。

##### evidence_pointers

1. 表4

#### 5. 5

- theory_or_knowledge_claim_cn：实务审讯技术（Inbau et al.）推测，有罪者更可能认为宽松后果是适当的，但从未被实证检验。

- mechanism_cn：询问后果适当性能作为识别违规者的访谈策略。

- design_requirement_cn：将后果适当性问题纳入检测问卷，并提供首次实证检验。

- artifact_choice_cn：后果适当性题与合规题一起用于后续分类模型。

- evaluated_contrast_cn：回答宽松度与鼠标偏差联合后的分类性能。

- objective_result_cn：逻辑回归准确率72.79%，AUC=0.718，敏感性0.644，特异性0.792。

##### evidence_pointers

1. Classification Accuracy 小节

#### 6. 6

- theory_or_knowledge_claim_cn：回答内容与鼠标行为分别只在某种程度上反映认知失调，联合能提供更稳健的信号。

- mechanism_cn：同时出现更宽松回答和异常鼠标移动，既能证明认知失调存在，也能排除单纯人格特质或纯运动噪声的解释。

- design_requirement_cn：分类模型应同时使用回答与鼠标偏差作为预测特征。

- artifact_choice_cn：逻辑回归模型同时纳入合规/后果回答与合规/后果题鼠标偏差。

- evaluated_contrast_cn：模型在保留样本上的判别性能，与随机审计情景对比。

- objective_result_cn：在假设的10万员工、1%不合规情景中，模型可识别644例而非250例，并少用15.1%审计资源。

##### evidence_pointers

1. Classification Accuracy 小节

2. Discussion 中审计情景

## 评价逻辑

### evaluation_modes

1. 受控在线实验：真实金钱激励下观察自愿作弊行为，客观区分合规/不合规

2. 探索性数据-理论拟合检验：角度变化z-score支持亚运动模型

3. 线性混合效应模型：检验回答宽松度假设（H1a/H2a）

4. 稳健线性混合效应模型：检验鼠标偏移假设（H1b/H2b），处理非正态残差

5. 稳健性分析：不同自报措辞、平均聚合、log变换

6. 逻辑回归分类：80/20训练测试与10折交叉验证，报告准确率、AUC、敏感性、特异性

7. 假设性审计资源配置情景：将模型指标翻译为管理收益

- why_these_evaluations_cn：实验提供基于客观行为的因果证据；混合模型建立组间统计差异；稳健性分析排除方法学替代解释；分类模型解决低r平方带来的“实际意义”问题；假设审计情景把AUC和敏感性/特异性转化为管理者可理解的资源节省。

- benchmark_and_contrast_chain_cn：首先以人口统计确认题作为个人鼠标移动基线，对目标题偏差做z-score；再以未作弊者为天然对照组，检验作弊者的回答和移动差异；分类阶段用80/20保留样本和10折交叉验证验证泛化；最后用随机审计作为反事实，说明模型在资源分配上的增量价值。

### claim_evidence_ledger

#### 1. 不合规者会对合规定义给出更宽松回答。

- claim_cn：不合规者会对合规定义给出更宽松回答。

- evidence_cn：表1线性混合效应模型显示β=-0.83，p<0.001。

- verdict_cn：supported

#### 2. 不合规者会对非合规后果给出更宽松回答。

- claim_cn：不合规者会对非合规后果给出更宽松回答。

- evidence_cn：表2线性混合效应模型显示β=-2.04，p<0.001。

- verdict_cn：supported

#### 3. 不合规者在合规定义题上有更大鼠标偏移。

- claim_cn：不合规者在合规定义题上有更大鼠标偏移。

- evidence_cn：表3稳健线性混合效应模型显示β=1.13，p<0.05。

- verdict_cn：supported

#### 4. 不合规者在后果题上有更大鼠标偏移。

- claim_cn：不合规者在后果题上有更大鼠标偏移。

- evidence_cn：表4显示β=-0.10，p>0.05。

- verdict_cn：not supported

#### 5. 回答和鼠标偏差联合可用于识别不合规风险。

- claim_cn：回答和鼠标偏差联合可用于识别不合规风险。

- evidence_cn：逻辑回归测试集准确率72.79%，AUC=0.718；10折CV AUC=0.748。

- verdict_cn：supported at aggregate level, but no ablation for each predictor

#### 6. 鼠标偏差加回答能证明认知失调的存在。

- claim_cn：鼠标偏差加回答能证明认知失调的存在。

- evidence_cn：H1a、H1b、H2a同时显著，H2b不显著；作者用联合模式作为支持性论证。

- verdict_cn：partially supported, because H2b weakens consequence-movement link

#### 7. 工具可帮助组织更有效分配审计/培训资源。

- claim_cn：工具可帮助组织更有效分配审计/培训资源。

- evidence_cn：基于敏感性0.644、特异性0.792的假设审计情景计算。

- verdict_cn：illustrative based on model metrics, not tested in field

- internal_validity_strategy_cn：使用客观、非侵入的作弊分类（定制链接点击记录）；随机化题序；用人口统计确认题标准化个体鼠标差异；加入题目随机效应和题序控制变量；通过预测试保证作弊诱发力；使用稳健模型处理非正态残差；多种稳健性分析。

- external_validity_strategy_cn：MTurk参与者有真实金钱激励和较高任务历史筛选；作弊机会与真实组织中的违规激励相似；结果被表述为适用于低成本大规模在线问卷的一般技术；通过假设审计情景说明可扩展性。

- what_is_not_actually_tested_cn：未在真实企业员工和真实法规合规情境中现场部署；未做消融分析以分离回答与鼠标偏差各自贡献；H2b对应的后果题移动机制未获支持，作者将其解释为失调较低但未直接测量失调；未检验工具被广泛知晓后的博弈、威慑或反应性效应；未检验完全理性化或极端人格人群中该方法的有效性。

## 贡献闭环

- technical_claim_cn：一种嵌入鼠标追踪的在线问卷结合回答宽松度与鼠标偏移，能以约72.79%准确率、AUC=0.718识别不合规者。

- artifact_claim_cn：由认知失调理论推导出的“合规定义题+后果适当性题”以及鼠标偏移指标，是导致识别能力提升的可识别设计部分；但未通过消融实验单独确认每个预测因子的贡献。

- mechanism_claim_cn：不合规者因认知失调而修改对合规和后果的信念，表现为更宽松回答；同时RAM导致鼠标轨迹偏离，因此鼠标偏移可作为失调的在线行为痕迹。

- boundary_claim_cn：该机制适用于经历部分合理化的大多数不合规者，而非极端人格或完全合理化者；后果题的移动指标边界较弱，H2b不支持。

- reusable_design_knowledge_cn：在设计风险评估问卷时，应同时询问违规定义与后果适当性两类问题；鼠标偏移需要以个人控制题做z-score标准化；回答内容与鼠标行为应联合使用而非单独使用。

- theoretical_contribution_cn：扩展了认知失调理论到组织合规检测情境，说明认知失调可通过不自然鼠标轨迹被在线观测；首次实证检验了实务审讯中“询问后果”策略；为IS研究提供了将鼠标追踪作为实际行为测量的新路径。

- how_discussion_closes_intro_gap_cn：开篇以巨额罚款和自报缺陷构造对低成本合规评估的需求；讨论部分先重述发现，然后用“更宽松回答+鼠标偏移同时出现”论证认知失调机制，以排除人格特质单独解释；接着用首项实证证据、鼠标追踪文献扩展、气候调查应用和经济监控方式等贡献点，把结果回接到开篇的组织风险评估问题。

- overclaim_or_unsupported_leaps_cn：（1）从MTurk作弊情境向企业法规不合规推广存在情境跳跃；（2）H2b未获支持，但讨论仍将后果题回答的宽松作为认知失调证据，缺少独立的失调测量；（3）没有消融分析，无法证明哪些具体特征驱动分类性能；（4）“低成本、可扩展”基于假设情景，未报告部署成本；（5）“首次实证检验”依赖对实务文献的解读，属于声称性贡献而非实质性新机制。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：确保组织和法律合规是困难且高风险的。

- rhetorical_function_cn：开篇建立问题的重要性和现实背景。

- depends_on_cn：无。

- sets_up_cn：为引出检测非合规风险的必要性做铺垫。

- evidence_pointer：摘要第一句

### 2. P1 S2-S3

- order：2

- section：Abstract

- locator：P1 S2-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：低估不合规会导致巨额罚款、声誉损失和业务损失。

- rhetorical_function_cn：把抽象问题转成具体后果，强化现实紧迫性。

- depends_on_cn：依赖前面对合规重要性的陈述。

- sets_up_cn：说明评估不合规具有高价值。

- evidence_pointer：摘要第二至三句

### 3. P2

- order：3

- section：Abstract

- locator：P2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：探索能否通过智能在线问卷监控用户回答和鼠标移动来评估不合规。

- rhetorical_function_cn：用一句话声明全文核心研究目标。

- depends_on_cn：依赖前面对风险和代价的背景。

- sets_up_cn：引出理论预测和实验设计。

- evidence_pointer：摘要第二段

### 4. P3

- order：4

- section：Abstract

- locator：P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：提出不合规者比合规者在合规定义和后果问题上经历更多认知失调。

- rhetorical_function_cn：首次引入理论机制。

- depends_on_cn：核心目标提出后需要理论框架。

- sets_up_cn：为后续假设和测量提供机制基础。

- evidence_pointer：摘要第三段

### 5. P4

- order：5

- section：Abstract

- locator：P4

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：预测认知失调会影响问卷回答以及回答时的鼠标移动。

- rhetorical_function_cn：把理论机制转化为可检验的预测性主张。

- depends_on_cn：依赖认知失调理论命题。

- sets_up_cn：提示后面的实验设计和假设。

- evidence_pointer：摘要第四段

### 6. P5

- order：6

- section：Abstract

- locator：P5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在自愿为金钱收益而作弊的个体中收集数据检验假设。

- rhetorical_function_cn：预告研究类型和样本来源。

- depends_on_cn：需要可观察的合规/不合规群体。

- sets_up_cn：建立证据来源的可信性。

- evidence_pointer：摘要第五段

### 7. P6

- order：7

- section：Abstract

- locator：P6

- move_code：RESULT

- paraphrase_cn：两类问题回答和鼠标移动可以联合作为低成本、可扩展的评估工具。

- rhetorical_function_cn：给出主要结果与应用结论。

- depends_on_cn：依赖实验证据。

- sets_up_cn：为摘要中的贡献声明提供依据。

- evidence_pointer：摘要第六段

### 8. P1 S1

- order：8

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：组织会因少数员工不遵守法律和法规而面临严重后果。

- rhetorical_function_cn：从组织层面建立真实世界问题。

- depends_on_cn：无。

- sets_up_cn：为合规评估工具需求做铺垫。

- evidence_pointer：引言第一句

### 9. P1 S2-P2 S1

- order：9

- section：Introduction

- locator：P1 S2-P2 S1

- move_code：PHENOMENON

- paraphrase_cn：举例说明FCPA、反洗钱等法规下组织被重罚，如空客近40亿美元、SEC调查西门子等。

- rhetorical_function_cn：用真实案例让非合规风险可视化。

- depends_on_cn：依赖合规法规背景。

- sets_up_cn：强化“必须做点什么”的紧迫性。

- evidence_pointer：引言第一至第二段

### 10. P2 S3-S4

- order：10

- section：Introduction

- locator：P2 S3-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：大型跨国组织中确保合规很困难，需要先评估合规以战略分配培训、审计等资源。

- rhetorical_function_cn：从“问题严重”转向“需要评估工具”。

- depends_on_cn：前面的罚款案例。

- sets_up_cn：引出问卷自我报告及其缺陷。

- evidence_pointer：引言第二段后半

### 11. P2 S5

- order：11

- section：Introduction

- locator：P2 S5

- move_code：LIMITATION

- paraphrase_cn：问卷自我报告常因社会期望偏差和披露后果恐惧而不准确。

- rhetorical_function_cn：指出现有常见工具的关键局限。

- depends_on_cn：前面提到问卷作为评估手段。

- sets_up_cn：为技术替代方案创造缺口。

- evidence_pointer：引言第二段倒数第二句

### 12. P2 S6

- order：12

- section：Introduction

- locator：P2 S6

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：鉴于非合规的巨大成本，改进合规评估的技术创新具有显著潜在收益。

- rhetorical_function_cn：解释缺口值得解决的原因。

- depends_on_cn：前面的成本和局限。

- sets_up_cn：引出本研究的理论和设计。

- evidence_pointer：引言第二段末句

### 13. P3 S1

- order：13

- section：Introduction

- locator：P3 S1

- move_code：THEORY_INTRO

- paraphrase_cn：基于认知失调理论和工作场所越轨背景，预测不合规者会对合规定义和后果持有更宽松信念。

- rhetorical_function_cn：将问题纳入理论框架。

- depends_on_cn：前面确立的检测需求。

- sets_up_cn：为H1a/H2a等假设提供理论来源。

- evidence_pointer：引言第三段第一句

### 14. P3 S2

- order：14

- section：Introduction

- locator：P3 S2

- move_code：MECHANISM

- paraphrase_cn：认知失调理论认为个体会以减少信念和行为冲突的方式缓解心理不适。

- rhetorical_function_cn：解释为什么会产生更宽松回答。

- depends_on_cn：理论引入。

- sets_up_cn：使宽松答案成为可预期的结果。

- evidence_pointer：引言第三段第二句

### 15. P3 S3

- order：15

- section：Introduction

- locator：P3 S3

- move_code：THEORY_INTRO

- paraphrase_cn：同时结合反应激活模型，预测认知失调的解除会影响相关的鼠标移动。

- rhetorical_function_cn：引入第二个理论支撑行为测量。

- depends_on_cn：前面对认知失调的解释。

- sets_up_cn：为鼠标偏差假设提供机制。

- evidence_pointer：引言第三段末句

### 16. P4 S1

- order：16

- section：Introduction

- locator：P4 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为检验假设，研究者设计了一个参与者既有动机又有机会作弊的研究。

- rhetorical_function_cn：从理论转入方法并预告研究设置。

- depends_on_cn：理论预测需要实证检验。

- sets_up_cn：说明后文实验设计的核心逻辑。

- evidence_pointer：引言第四段第一句

### 17. P4 S2-S3

- order：17

- section：Introduction

- locator：P4 S2-S3

- move_code：RESULT

- paraphrase_cn：客观观察到是否作弊，并发现回答宽松度与鼠标移动在合规和不合规者间存在差异；联合在逻辑回归中有识别效用。

- rhetorical_function_cn：在引言就给出主要结果，建立文章竞争力。

- depends_on_cn：依赖后面实验。

- sets_up_cn：为贡献声明提供结果支撑。

- evidence_pointer：引言第四段后半

### 18. P5

- order：18

- section：Introduction

- locator：P5

- move_code：CONTRIBUTION

- paraphrase_cn：声称首次实证检验实务文献中“询问后果”的推测，并引入和检验一种新的访谈策略。

- rhetorical_function_cn：在引言明确与众不同的贡献。

- depends_on_cn：前面的结果和文献。

- sets_up_cn：为后文贡献部分做预告。

- evidence_pointer：引言第五段

### 19. P6 S1-S2

- order：19

- section：Introduction

- locator：P6 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：研究还贡献于行为追踪和职场越轨及欺骗文献，表明认知失调可以通过更宽松回答和鼠标偏差推断。

- rhetorical_function_cn：从“工具”贡献扩展到“理论”贡献。

- depends_on_cn：前面的核心发现。

- sets_up_cn：引出“回答+移动”联合推断机制的核心逻辑。

- evidence_pointer：引言第六段

### 20. P6 S3-P7

- order：20

- section：Introduction

- locator：P6 S3-P7

- move_code：MECHANISM

- paraphrase_cn：单独异常鼠标移动或单独宽松回答都不足以证明认知失调，二者同时出现才能排除人格特质解释。

- rhetorical_function_cn：说明联合测量的认识论价值，保护机制推断。

- depends_on_cn：两个信号的独立可观察性。

- sets_up_cn：为讨论中的机制贡献提供逻辑框架。

- evidence_pointer：引言第六至七段

### 21. P1-P2

- order：21

- section：Literature Review

- locator：P1-P2

- move_code：CONTEXT

- paraphrase_cn：现代企业需遵守大量法律，例如FCPA、反洗钱、内幕交易等，整个企业都要合规，小违规也可能带来大额罚款。

- rhetorical_function_cn：在文献综述中重新界定问题范围。

- depends_on_cn：引言中的合规问题。

- sets_up_cn：引出对检测技术的需求。

- evidence_pointer：文献综述第一至二段

### 22. P2 空客例子

- order：22

- section：Literature Review

- locator：P2 空客例子

- move_code：PRACTICAL_STAKES

- paraphrase_cn：空客约13.5万人中约100人行为导致巨额罚款，说明少数人可造成巨大损失。

- rhetorical_function_cn：用比例对比强调小群体风险。

- depends_on_cn：前文法规背景。

- sets_up_cn：说明需要能识别少数不合规个体的工具。

- evidence_pointer：文献综述第二段

### 23. P3

- order：23

- section：Literature Review

- locator：P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：工作场所越轨文献长期研究越轨行为的类型、前因和减少方法。

- rhetorical_function_cn：总结已有文献基础。

- depends_on_cn：无需依赖前文。

- sets_up_cn：指出已有文献侧重前因而非技术检测。

- evidence_pointer：文献综述第三段

### 24. P3 末

- order：24

- section：Literature Review

- locator：P3 末

- move_code：GAP

- paraphrase_cn：用技术检测可能的职场越轨这一目标尚未被充分研究。

- rhetorical_function_cn：明确研究缺口。

- depends_on_cn：前面总结的已有文献。

- sets_up_cn：为本文定位提供缺口。

- evidence_pointer：文献综述第三段末

### 25. P4

- order：25

- section：Literature Review

- locator：P4

- move_code：GAP

- paraphrase_cn：已有研究呼吁低成本、可扩展、易部署的合规风险评估机制，并已开始探索虚拟访谈和在线问答；先前研究用了非常不自然的鼠标移动界面识别隐藏信息。

- rhetorical_function_cn：缩小缺口到具体技术路线。

- depends_on_cn：前面对检测需求的论述。

- sets_up_cn：说明本研究将技术迁移到常见问卷格式。

- evidence_pointer：文献综述第四段

### 26. P5

- order：26

- section：Literature Review

- locator：P5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究在常见的在线问卷格式中测量鼠标移动，检验其能否作为自愿恶意行为后的风险指标。

- rhetorical_function_cn：把文献缺口转成本文目标。

- depends_on_cn：前面对已有技术的总结。

- sets_up_cn：为理论发展做铺垫。

- evidence_pointer：文献综述第五段

### 27. P1 S1-S2

- order：27

- section：Mouse Tracking as a Scientific Methodology

- locator：P1 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：认知和神经科学已表明精细运动控制受认知和情绪影响，鼠标追踪由此成为客观测量决策和心理过程的科学方法。

- rhetorical_function_cn：为鼠标追踪建立科学合法性。

- depends_on_cn：本文需要鼠标移动作为数据来源。

- sets_up_cn：后续理论机制和移动指标有据可依。

- evidence_pointer：Mouse Tracking 第一段

### 28. P2

- order：28

- section：Mouse Tracking as a Scientific Methodology

- locator：P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有大量鼠标追踪研究预测决策冲突、态度形成、种族偏见掩饰、反应困难、反应确定性、动态认知竞争、情绪反应和欺骗等。

- rhetorical_function_cn：列举鼠标追踪的广泛应用以说明成熟度。

- depends_on_cn：前面鼠标追踪是科学方法的声明。

- sets_up_cn：为把鼠标追踪用于合规检测建立类比基础。

- evidence_pointer：Mouse Tracking 第二段

### 29. P3 与图3

- order：29

- section：Mouse Tracking as a Scientific Methodology

- locator：P3 与图3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：鼠标追踪能补充调查法，例如Jenkins et al.用其测量社会期望偏差，并将响应偏差作为调节变量使模型解释力接近翻倍。

- rhetorical_function_cn：提供与本文最接近的先例，说明回答+移动联合有效。

- depends_on_cn：前面的鼠标追踪文献。

- sets_up_cn：为本文同时分析回答和鼠标偏差提供直接先例。

- evidence_pointer：Mouse Tracking 第三段

### 30. P1

- order：30

- section：Theoretical Foundations of Mouse Tracking

- locator：P1

- move_code：THEORY_INTRO

- paraphrase_cn：随机优化亚运动模型认为手部移动不是完美直线，而是由初始移动和之后若干校正性亚运动构成。

- rhetorical_function_cn：引入解释鼠标偏移的基础运动模型。

- depends_on_cn：鼠标追踪需要运动理论支持。

- sets_up_cn：为“偏离理想响应轨迹”提供理论依据。

- evidence_pointer：Theoretical Foundations 第一段

### 31. P2-P3

- order：31

- section：Theoretical Foundations of Mouse Tracking

- locator：P2-P3

- move_code：THEORY_INTRO

- paraphrase_cn：反应激活模型指出，所有具有行动潜势的刺激都会影响动作输出，多个潜在反应会并行启动并导致手部偏离。

- rhetorical_function_cn：引入认知竞争如何转化为运动偏差的核心机制。

- depends_on_cn：前面的亚运动模型。

- sets_up_cn：为认知失调引起的回答竞争与鼠标偏移建立桥梁。

- evidence_pointer：Theoretical Foundations 第二至三段

### 32. P1-P3

- order：32

- section：How Noncompliance Influences Questionnaire Responses and Mouse Tracking

- locator：P1-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：对不合规的极端反应包括完全无失调的人格特质或完全合理化，但这两种极端较少；多数人会在部分合理化后经历信念-行为冲突。

- rhetorical_function_cn：明确理论适用范围并排除极端情况。

- depends_on_cn：前面理论讨论。

- sets_up_cn：为认知失调机制设定边界条件。

- evidence_pointer：How Noncompliance 第一至三段

### 33. P4

- order：33

- section：How Noncompliance Influences Questionnaire Responses and Mouse Tracking

- locator：P4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：认知失调理论的核心命题是，信念与行为冲突时个体试图修改信念或行为以减少不适。

- rhetorical_function_cn：概括理论核心，供假设推导。

- depends_on_cn：前面的心理冲突描述。

- sets_up_cn：引出“不合规者修改信念”的具体预测。

- evidence_pointer：How Noncompliance 第四段

### 34. P5

- order：34

- section：How Noncompliance Influences Questionnaire Responses and Mouse Tracking

- locator：P5

- move_code：MECHANISM

- paraphrase_cn：当问不合规者什么构成违规时，他们会潜意识调整定义使其行为更不容易被判定为违规。

- rhetorical_function_cn：把理论命题翻译到具体问卷情境。

- depends_on_cn：认知失调理论。

- sets_up_cn：为H1a/H1b提供机制。

- evidence_pointer：How Noncompliance 第五段

### 35. H1a-H1b

- order：35

- section：How Noncompliance Influences Questionnaire Responses and Mouse Tracking

- locator：H1a-H1b

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H1a：不合规导致对合规定义的回答更宽松；H1b：不合规导致回答合规题时鼠标偏移更大。

- rhetorical_function_cn：正式产出第一对假设。

- depends_on_cn：前面的认知失调与RAM机制。

- sets_up_cn：为后续统计检验提供目标。

- evidence_pointer：How Noncompliance 假设段落

### 36. P6

- order：36

- section：How Noncompliance Influences Questionnaire Responses and Mouse Tracking

- locator：P6

- move_code：MECHANISM

- paraphrase_cn：多个潜在回答同时捕获注意时，大脑会并行编程多个动作反应，导致鼠标在最终选择前发生偏移。

- rhetorical_function_cn：解释H1b的微观机制。

- depends_on_cn：RAM。

- sets_up_cn：为移动指标的解释提供理论依据。

- evidence_pointer：How Noncompliance 第六段

### 37. H2a-H2b前段

- order：37

- section：How Noncompliance Influences Questionnaire Responses and Mouse Tracking

- locator：H2a-H2b前段

- move_code：GAP

- paraphrase_cn：询问潜在后果在实务访谈中一直被建议，但从未被实证检验。

- rhetorical_function_cn：为后果问题引入独立的实务缺口。

- depends_on_cn：前面合规定义题的理论推导。

- sets_up_cn：引出H2a/H2b。

- evidence_pointer：How Noncompliance 后果问题前段

### 38. H2a-H2b

- order：38

- section：How Noncompliance Influences Questionnaire Responses and Mouse Tracking

- locator：H2a-H2b

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H2a：不合规导致对后果适当性的回答更宽松；H2b：不合规导致回答后果题时鼠标偏移更大。

- rhetorical_function_cn：正式产出第二对假设。

- depends_on_cn：认知失调、害怕后果及RAM。

- sets_up_cn：后续表2、表4分别检验。

- evidence_pointer：How Noncompliance 假设段落

### 39. 末段

- order：39

- section：How Noncompliance Influences Questionnaire Responses and Mouse Tracking

- locator：末段

- move_code：MECHANISM

- paraphrase_cn：联合回答与鼠标移动能排除单独信号时的歧义，从而更可靠地推断认知失调。

- rhetorical_function_cn：把两对假设连接成综合机制主张。

- depends_on_cn：H1和H2的预测。

- sets_up_cn：为讨论中联合数据的解释做铺垫。

- evidence_pointer：How Noncompliance 末段

### 40. P1

- order：40

- section：Method

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用在线能力测试，给参与者现金激励和作弊机会，同时不公开阻止作弊，以模拟现实中的违规激励。

- rhetorical_function_cn：解释实验设计为何能诱发真实不合规行为。

- depends_on_cn：需要比较合规/不合规群体。

- sets_up_cn：为后文客观作弊测量做铺垫。

- evidence_pointer：Method 第一段

### 41. P2

- order：41

- section：Method

- locator：P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：五道改编GMAT题均配有答案链接，但指导语明确要求提交后才可查看，并要求每题至少停留30秒。

- rhetorical_function_cn：创造标准化且可诱发的违规机会。

- depends_on_cn：Method第一段的激励结构。

- sets_up_cn：为个性化链接追踪作弊提供条件。

- evidence_pointer：Method 第二段

### 42. P3

- order：42

- section：Method

- locator：P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：答案链接按参与者个性化，只有点击查看答案才算作弊，从而客观、非侵入地识别违规者。

- rhetorical_function_cn：说明作弊检测机制和判定标准。

- depends_on_cn：前面提供的答案链接。

- sets_up_cn：确立后续比较的分组变量。

- evidence_pointer：Method 第三段

### 43. P4

- order：43

- section：Method

- locator：P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：测试后向参与者显示成绩和奖励，并提醒不应提前查看答案，使不合规行为更突出。

- rhetorical_function_cn：增强随后的认知失调触发条件。

- depends_on_cn：客观作弊测量。

- sets_up_cn：让随后的合规/后果题更可能引发失调。

- evidence_pointer：Method 第四段

### 44. P5-P6

- order：44

- section：Method

- locator：P5-P6

- move_code：DESIGN_FEATURE

- paraphrase_cn：合规题询问哪些行为算作弊，后果题询问各后果有多适当，均使用0-10量表。

- rhetorical_function_cn：具体描述两类核心问卷题。

- depends_on_cn：前面理论推导。

- sets_up_cn：为后续因变量操作化提供依据。

- evidence_pointer：Method 第五至六段

### 45. P7

- order：45

- section：Method

- locator：P7

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：随机化合规题和后果题的回答顺序，并在分析中作为控制变量。

- rhetorical_function_cn：控制顺序效应以保证内部有效性。

- depends_on_cn：两类题目的存在。

- sets_up_cn：后续模型中的Order变量。

- evidence_pointer：Method 第七段

### 46. P8

- order：46

- section：Method

- locator：P8

- move_code：DESIGN_FEATURE

- paraphrase_cn：用人口统计确认题作为所有参与者共同的基准题，计算相对鼠标偏差。

- rhetorical_function_cn：建立个人化基线以消除个体和设备差异。

- depends_on_cn：前面完成人口统计题。

- sets_up_cn：为鼠标偏差的z-score标准化做准备。

- evidence_pointer：Method 第八段

### 47. Mouse Movement Measurement

- order：47

- section：Method

- locator：Mouse Movement Measurement

- move_code：DESIGN_FEATURE

- paraphrase_cn：用Qualtrics内嵌JavaScript记录毫秒级鼠标坐标，计算实际移动距离与理想响应轨迹距离之差作为偏差。

- rhetorical_function_cn：具体化鼠标移动的核心因变量。

- depends_on_cn：前面基准题设计。

- sets_up_cn：为H1b/H2b提供操作定义。

- evidence_pointer：Method 鼠标移动测量段

### 48. Mouse Movement Measurement 末段

- order：48

- section：Method

- locator：Mouse Movement Measurement 末段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用控制题的均值和标准差计算目标题的z分数，以过滤设备、生理和人口等因素带来的噪声。

- rhetorical_function_cn：说明标准化方法为何合理。

- depends_on_cn：前面个人基线题。

- sets_up_cn：为后续统计模型的相对偏差解释提供依据。

- evidence_pointer：Mouse Movement Measurement 末段

### 49. Pilot Tests

- order：49

- section：Method

- locator：Pilot Tests

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：经过五轮共95人的预测试，调整报酬和指导语以确保作弊追踪准确并提高作弊率。

- rhetorical_function_cn：说明方法经过了验证和优化。

- depends_on_cn：前面实验设计。

- sets_up_cn：增强主实验结果的可靠性。

- evidence_pointer：Method 预测试段

### 50. Participants

- order：50

- section：Method

- locator：Participants

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：招募950名有较高质量历史的MTurk参与者，设置基础报酬和按正确题目数支付的绩效报酬，所有完成者都获得报酬。

- rhetorical_function_cn：描述样本规模和激励，支持结果可信性。

- depends_on_cn：前面的实验结构。

- sets_up_cn：为描述统计和后续分析提供样本基础。

- evidence_pointer：Method 参与者段

### 51. 第一段

- order：51

- section：Analysis

- locator：第一段

- move_code：RESULT

- paraphrase_cn：探索性分析显示，参与者每次连续移动平均出现1.46次显著角度变化，支持亚运动模型。

- rhetorical_function_cn：在假设检验前验证运动理论前提。

- depends_on_cn：鼠标轨迹数据和亚运动模型。

- sets_up_cn：为鼠标偏移的认知竞争解释提供数据支持。

- evidence_pointer：Analysis 第一段

### 52. 第二段

- order：52

- section：Analysis

- locator：第二段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用线性混合效应模型，将每个问题作为随机效应，并加入是否作弊和题序作为预测变量。

- rhetorical_function_cn：说明统计模型如何控制题目差异和顺序。

- depends_on_cn：实验数据层级结构。

- sets_up_cn：为表1-4的检验做准备。

- evidence_pointer：Analysis 第二段

### 53. H1a结果/表1

- order：53

- section：Analysis

- locator：H1a结果/表1

- move_code：RESULT

- paraphrase_cn：不合规对合规定义题回答宽松度的影响显著，β=-0.83，p<0.001。

- rhetorical_function_cn：报告第一个假设检验结果。

- depends_on_cn：线性混合效应模型。

- sets_up_cn：支撑回答信号的有效性。

- evidence_pointer：表1

### 54. H2a结果/表2

- order：54

- section：Analysis

- locator：H2a结果/表2

- move_code：RESULT

- paraphrase_cn：不合规对后果题回答宽松度的影响显著，β=-2.04，p<0.001。

- rhetorical_function_cn：报告第二个回答假设的支持结果。

- depends_on_cn：后果题数据。

- sets_up_cn：支撑后果问题作为检测信号。

- evidence_pointer：表2

### 55. H1a/H1b r平方后

- order：55

- section：Analysis

- locator：H1a/H1b r平方后

- move_code：TRANSITION

- paraphrase_cn：由于模型r平方较低，作者声明需要补充分析来检验实际意义。

- rhetorical_function_cn：为引入分类模型做过渡。

- depends_on_cn：前面的低r平方结果。

- sets_up_cn：引出Classification Accuracy部分。

- evidence_pointer：表1后、表3后

### 56. H1b结果/表3

- order：56

- section：Analysis

- locator：H1b结果/表3

- move_code：RESULT

- paraphrase_cn：不合规显著增加合规题鼠标偏移，β=1.13，p<0.05。

- rhetorical_function_cn：报告移动假设的支持结果。

- depends_on_cn：稳健线性混合效应模型。

- sets_up_cn：支撑鼠标移动作为失调指标。

- evidence_pointer：表3

### 57. H2b结果/表4

- order：57

- section：Analysis

- locator：H2b结果/表4

- move_code：RESULT

- paraphrase_cn：不合规对后果题鼠标偏移的影响不显著，β=-0.10，p>0.05。

- rhetorical_function_cn：报告唯一未获支持的假设。

- depends_on_cn：后果题鼠标数据。

- sets_up_cn：为后果失调可能较低和未来研究做铺垫。

- evidence_pointer：表4

### 58. 表5前

- order：58

- section：Analysis

- locator：表5前

- move_code：RESULT

- paraphrase_cn：汇总所有假设：H1a、H1b、H2a支持，H2b不支持。

- rhetorical_function_cn：给出概括性结果总览。

- depends_on_cn：表1-4。

- sets_up_cn：转入分类精度分析。

- evidence_pointer：表5

### 59. 第一段

- order：59

- section：Classification Accuracy

- locator：第一段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择未调参的基础逻辑回归，目的是获得保守的性能估计。

- rhetorical_function_cn：解释为什么采用简单模型，增强结果可信度。

- depends_on_cn：前面的低r平方。

- sets_up_cn：为分类结果和未来改进留出空间。

- evidence_pointer：Classification Accuracy 第一段

### 60. 第二段

- order：60

- section：Classification Accuracy

- locator：第二段

- move_code：RESULT

- paraphrase_cn：测试集准确率72.79%，AUC=0.718，敏感性0.644，特异性0.792。

- rhetorical_function_cn：报告模型整体判别性能。

- depends_on_cn：80/20训练测试划分。

- sets_up_cn：用于资源分配情景计算。

- evidence_pointer：Classification Accuracy 第二段

### 61. 第三段

- order：61

- section：Classification Accuracy

- locator：第三段

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在10万员工、1%不合规的假设组织中，该模型可识别644例而非随机审计的250例，并少用15.1%审计资源。

- rhetorical_function_cn：将分类指标翻译为管理者可见的收益。

- depends_on_cn：敏感性、特异性值。

- sets_up_cn：支撑“低成本高收益工具”的贡献主张。

- evidence_pointer：Classification Accuracy 第三段

### 62. 第四段

- order：62

- section：Classification Accuracy

- locator：第四段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：加入更多鼠标指标如其他距离度量、面部表情或皮电反应可能进一步提高准确率。

- rhetorical_function_cn：承认当前指标的局限并提供改进方向。

- depends_on_cn：当前只用了单一鼠标指标。

- sets_up_cn：为讨论中的未来研究铺垫。

- evidence_pointer：Classification Accuracy 第四段

### 63. P1

- order：63

- section：Discussion

- locator：P1

- move_code：RESULT

- paraphrase_cn：总结发现：不合规者在合规定义和后果上更宽松，在合规题上鼠标偏移更大，表明认知失调并支持风险评估工具。

- rhetorical_function_cn：讨论开始前重述核心结果。

- depends_on_cn：假设检验和分类结果。

- sets_up_cn：为具体贡献点提供结果基础。

- evidence_pointer：Discussion 第一段

### 64. Contribution to Research and Practice 第一点

- order：64

- section：Discussion

- locator：Contribution to Research and Practice 第一点

- move_code：CONTRIBUTION

- paraphrase_cn：本文把鼠标移动与认知情绪过程相连，新颖之处是在信息技术的使用情境中联合考察非合规对回答和鼠标移动的影响。

- rhetorical_function_cn：定位为对鼠标追踪文献的扩展。

- depends_on_cn：联合数据结果。

- sets_up_cn：为IS研究使用实际行为测量提供示范。

- evidence_pointer：Discussion 贡献部分第一点

### 65. Contribution 第二点

- order：65

- section：Discussion

- locator：Contribution 第二点

- move_code：CONTRIBUTION

- paraphrase_cn：研究表明鼠标追踪能揭示认知失调现象，非合规组因需要调和自身行为与回答而出现更大失调。

- rhetorical_function_cn：把结果回接到理论机制。

- depends_on_cn：H1a、H1b、H2a的联合模式。

- sets_up_cn：说明理论贡献并非事后包装。

- evidence_pointer：Discussion 贡献部分第二点

### 66. Contribution 第三点

- order：66

- section：Discussion

- locator：Contribution 第三点

- move_code：CONTRIBUTION

- paraphrase_cn：过去研究大多分别看待“回答什么”与“如何回答”，本文显示二者可联合提供更准确的风险评估。

- rhetorical_function_cn：突出方法上的联合创新。

- depends_on_cn：回答+移动同时变化的实证结果。

- sets_up_cn：为回答与鼠标信号融合的设计知识提供支撑。

- evidence_pointer：Discussion 贡献部分第三点

### 67. Contribution 第四点

- order：67

- section：Discussion

- locator：Contribution 第四点

- move_code：CONTRIBUTION

- paraphrase_cn：首次为审讯实务中“违规者更可能认为宽松后果适当”的主张提供实证支持，并揭示其认知机制。

- rhetorical_function_cn：把“首次实证检验”作为具体学术贡献。

- depends_on_cn：后果题回答的显著差异。

- sets_up_cn：与引言中的实务缺口形成闭环。

- evidence_pointer：Discussion 贡献部分第四点

### 68. Contribution 第五点

- order：68

- section：Discussion

- locator：Contribution 第五点

- move_code：CONTRIBUTION

- paraphrase_cn：年度氛围调查等组织问卷中加入鼠标追踪可帮助揭示职场越轨和不愿报告的受害者。

- rhetorical_function_cn：扩展应用场景至组织气候调查。

- depends_on_cn：鼠标追踪作为可嵌入问卷的行为测量。

- sets_up_cn：为未来应用提供方向。

- evidence_pointer：Discussion 贡献部分第五点

### 69. Contribution 第六点

- order：69

- section：Discussion

- locator：Contribution 第六点

- move_code：CONTRIBUTION

- paraphrase_cn：为大型组织提供低成本监控非合规风险的路径，同时承认广泛采用可能带来知晓效应或威慑效应。

- rhetorical_function_cn：给出实践贡献并提前设置边界。

- depends_on_cn：分类精度与审计情景。

- sets_up_cn：引出未来研究。

- evidence_pointer：Discussion 贡献部分第六点

### 70. 全文末段

- order：70

- section：Conclusion

- locator：全文末段

- move_code：CONTRIBUTION

- paraphrase_cn：提出联合分析员工回答与鼠标移动的新方法，为低成本可扩展的非合规风险评估提供基础研究。

- rhetorical_function_cn：收束全文，回到最初的合规风险问题。

- depends_on_cn：全文所有结果和讨论。

- sets_up_cn：无，作为最终声明。

- evidence_pointer：Conclusion 第一段

## 写作技术

- gap_construction_cn：先以巨额罚款和空客、SEC案例制造现实代价；再指出自我报告问卷因社会期望和恐惧而不准确；接着说明已有鼠标追踪研究只在非常不自然的界面中识别隐藏信息，未在常见问卷中用于自愿非合规；最后用“实务审讯中问后果策略从未被实证检验”这一可操作缺口收窄研究空间。

- signposting_cn：摘要用“propose/predict/collect/results”预告路径；引言末用“current study demonstrates”声明贡献；Method开头用“To test our hypotheses”转入实验；Analysis用“Prior to analyzing hypotheses”和“Next”区分探索性与正式检验；Discussion用编号“First, Second...”组织贡献。

- transition_logic_cn：从宏观代价到评估需求；从自我报告局限到技术机会；从既有鼠标追踪到理论机制；从理论预测到具体方法；从低r平方自然过渡到分类精度；从分类精度引申到资源分配情景；从H2b未获支持转向未来研究。

- claim_evidence_rhythm_cn：几乎每个理论主张后紧跟可检验假设；每个假设后直接给出表格与统计量；对低r平方不回避，而是立即用分类模型补足实际意义；最后用假设计算把分类指标翻译为管理收益。

- benchmark_narrative_cn：将人口统计确认题作为个人鼠标移动基线，把目标题偏差z-score化；以未作弊者为天然对照组；分类中使用80/20保留样本和10折交叉验证；用随机审计作为反事实来展示模型增量价值。

- theory_return_cn：讨论中把“更宽松回答+更大鼠标偏移”的联合模式重新解释为认知失调存在的证据；用H2b不显著说明后果题上的失调可能较低，从而保留理论边界；同时把鼠标偏差本身定位为认知失调的在线行为痕迹。

- contribution_positioning_cn：贡献定位为“首次”实证检验实务主张、扩展鼠标追踪文献、为IS提供实际行为测量方法、增加问卷的风险评估能力；避免停留在“我们造了一个工具”的工程叙述。

- novelty_protection_cn：通过同时检验回答与鼠标行为并论证单一信号无法区分认知失调与人格特质，防止结果被解释为单纯群体差异；用朴素逻辑回归和交叉验证证明性能并非调参所得；用假设审计情景说明除统计显著之外还有实际管理价值；用H2b未支持展示对结果的诚实报告。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用具体罚款或处罚案例建立“少数人不合规会造成巨额损失”的现实问题。

- research_job_cn：选定一个合规问题领域并收集可量化的损失证据。

- required_evidence_cn：至少一个权威罚款/调查案例和法规依据。

- transition_to_next_cn：从“问题严重”转向“需要评估以分配资源”。

#### 2. 2

- step：2

- writing_job_cn：批评现有自报问卷的偏差，并引用已有技术只能用于非自然界面。

- research_job_cn：系统检索显示现有检测工具局限。

- required_evidence_cn：自我报告偏差文献和先前的鼠标追踪研究。

- transition_to_next_cn：从缺口转入理论解释。

#### 3. 3

- step：3

- writing_job_cn：引入一个能解释目标行为的理论，并把理论命题翻译成具体问题类型和测量指标。

- research_job_cn：选择认知失调/激励/冲突类理论，推导回答与行为指标假设。

- required_evidence_cn：理论命题与至少两对假设。

- transition_to_next_cn：“为检验假设，我们进行了实验。”

#### 4. 4

- step：4

- writing_job_cn：描述能客观获得真实行为标签的实验设置，包括激励、机会、追踪和不显著阻止违规。

- research_job_cn：设计并预测试非侵入式违规追踪机制，确保样本量足以出现违规者。

- required_evidence_cn：客观判定违规的规则和预测试结果。

- transition_to_next_cn：从数据收集转向统计模型。

#### 5. 5

- step：5

- writing_job_cn：先使用混合模型检验理论预测，再使用简单分类模型检验实际判别力；用保留样本和交叉验证报告性能。

- research_job_cn：运行多层次统计模型和朴素分类器，计算判效指标。

- required_evidence_cn：假设检验统计量、AUC、敏感性、特异性。

- transition_to_next_cn：从统计显著性转向实际应用价值。

#### 6. 6

- step：6

- writing_job_cn：在讨论中把联合信号重新解释为理论机制证据，并列出对文献和实务的具体贡献。

- research_job_cn：对比单信号与联合信号的含义，承认未支持假设并给出边界。

- required_evidence_cn：讨论中的机制论证和清晰贡献列表。

- transition_to_next_cn：用结论重申风险评估工具价值并指向未来研究。

### most_transferable_moves_cn

1. 用巨额罚款实例开头，快速建立实践紧迫性

2. 用“自我报告不准”制造技术缺口

3. 把理论机制直接翻译为问卷题目和移动指标

4. 设计客观、非侵入的真实行为标签

5. 用个人基准题标准化鼠标偏差

6. 低r平方后立即转向分类模型证明实际价值

7. 用假设审计情景说明管理收益

8. 用“联合信号排除人格解释”保护机制贡献

### resource_intensive_or_nonstandard_parts_cn

1. 在线实验中创建可追踪的个性化答案链接和作弊机会

2. 编写并预测试嵌入问卷的自定义JavaScript鼠标追踪代码

3. 招募大量有较高质量历史且愿参与在线任务的MTurk样本

4. 五轮预测试优化支付和指导语

5. 需要IRB伦理审批并处理参与者作弊的伦理问题

### what_not_to_copy_superficially_cn

1. 不要只贴“认知失调”标签就测量鼠标偏差，必须设计能触发失调的问题并证明对照组差异

2. 不要只有组间显著性而无分类性能，否则低r平方可能削弱实际意义

3. 不要把模型效果归因于单一特征而不做消融/比较

4. 不要轻易声称“首次实证”，必须确保文献检索充分

5. 不要把MTurk实验结论直接等同于真实组织合规情境，需要明确边界

- single_best_description_of_the_routine_cn：用真实激励诱发可客观验证的不合规，把认知失调理论翻译成两类问卷题和鼠标偏差指标，先证明组间统计差异，再用朴素逻辑回归把差异翻译成风险排查效率。

## 分析边界

OCR导致部分图片和数学符号不完整，但对正文、表格和附录的核心论证影响有限；未看到图1-6图像内容，不改变论证链判断；引文编号可能存在OCR噪声（如参考文献中少数格式混乱），不影响实质分析。
