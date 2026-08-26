# AI-Augmented Content Validation in Behavioral Research: Development and Evaluation of the RATER System

- 作者：Jean-Charles Pillet; Kai R. Larsen; David Dobolyi; Magno Queiroz; Abram Handler; Jan Ketil Arnulf; Rajeev Sharma
- 年份 / 期刊：2026 / MIS Quarterly
- DOI：10.25300/misq/2025/18946
- 源文件：27656_2026_ai-augmented-content-validation-in-behavioral-research-development-and-evaluation-of-the-rater-s.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.82

## 文章级论证概况

- 核心问题：如何构建一个免费、可复制、领域无关的AI系统来辅助行为研究中的内容效度评估，弥补传统内容验证成本高、执行少、不可复制的缺口。

- 制品与设计：设计与实现RATER系统（www.contval.org），包括两个模型：RATER_C（基于DeBERTa-v3-large的监督概率分类器，输出项目-定义匹配概率）和RATER_D（基于GPT-4o等微调生成模型，模拟Hinkin & Tracey评分者的1-7分评级分布）。系统以模块化Web界面开放，支持用户上传量表模板、选择模型、获得对应性/区分性/代表性结果。

- 客观结果：离线benchmark中RATER_C在33,304个测试实例上AUC=0.911、macro F1=0.782；Study 1在858个后训练论文项目对中准确率92%；Study 2与408名人类评分者的H&T评分一致性达88%，线性混合模型显著；Study 3优于BRASS Bot；Study 5用softmax实现多维构念代表性评估；Study 6专家可用性平均6.6/7、有用性5.7/7；外部信任量表案例中RATER_C与专家排序相关0.97，而H&T相关0.03。

- 核心贡献：作者声称五点贡献：领域无关的高性能内容效度模型；大规模benchmark数据集与方法；首个针对多维构念的代表性计算途径；真实场景适用性检查；开源透明可复制的平台。整体目标是把内容验证的成本效益方程转向利于常规执行，提升行为研究测量质量。

- 整篇论证链：文章从内容效度在量表开发中的关键性与执行不足的矛盾切入，指出现行人工流程昂贵、耗时、不可复制且受限于人类认知，并缺乏对代表性的形式化评估。作者将内容效度三重标准（对应性、区分性、代表性）作为设计需求，将任务类比为语义解析，采用监督微调构建分类器与分布两类模型，以大规模跨学科语料和人类评分数据训练。通过六个渐进的效度研究，先以作者标注验证RATER_C的区分能力，再以H&T人类评分验证生态效度，再对比BRASS，再形成“62启发式”阈值，再以softmax延伸代表性，最后通过专家适用性检查确认实用价值；外部信任量表案例进一步显示RATER能补充传统人类方法。整体论证从算法性能逐步升级到设计知识与理论贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章按设计科学范式构建并评估了RATER工件：从需求与设计原则出发（内容效度三重标准和表1的挑战-需求映射），经过模型构建、离线benchmark、多项准则效度研究、适用性检查，最终提炼出可选择的设计知识（62启发式、代表性softmax方法）。评价体系采用Larsen等人2025设计科学效度框架和Rosemann与Vessey的applicability check。虽然包含多个研究，但它们都服务于同一个制品的构建与评价。

- 主导写作弧线判定：文章开头建立的核心是内容验证实践表现缺口（内容验证被广泛视为关键却极少执行、成本高且不可复制），随后引出RATER制品，以大规模benchmark和六个研究作为主要证据，最终将结论一般化为开源平台、benchmark基础设施和可复用的设计知识。整体弧线符合性能缺口—制品—benchmark—一般化设计知识。

## 研究开展程序

- study_or_phase_count：9

- 研究阶段总序列：九个阶段呈阶梯式累积：阶段1建模与离线benchmark确立计算基础；阶段2以训练后论文作者标注验证第一层准则效度；阶段3以人类H&T评分者验证生态效度；阶段4与BRASS对比排除通用LLM替代解释；阶段5提出阈值启发式使用户可解释输出；阶段6扩展代表性维度补足理论缺口；阶段7通过专家适用性检查证明现实可用性；阶段8以独立团队信任量表案例展示外部生态效度与互补性；阶段9做可读性稳健性分析并界定边界条件。每一阶段解决前一阶段遗留的不确定性，并引入新的更严格或更贴近实践的准则。

### studies_or_phases

#### 1. 离线训练数据构建与模型基准测试

- order：1

- name_cn：离线训练数据构建与模型基准测试

- question_cn：哪些微调语言模型架构能够在项目文本与构念定义对应性预测上达到最优性能，并保持可接受的校准与计算成本？

- inputs_and_setting_cn：来自8个学科2443篇期刊论文的287,426个项目-定义配对（41,572意图配对/245,854非意图配对）；另从8篇JAP/AMJ文章中选取858对项目-定义对，其中467对经Prolific 408名评分者执行H&T 1-7分评级；微调15个分类器与13个分布模型，使用Hugging Face、unsloth、vLLM与固定随机种子。

- designed_or_compared_object_cn：比较15种BERT类/自回归分类器（ALBERT、BERT、DeBERTa等）与13种生成式分布模型（Llama 3/3.1/3.3、Phi-4、Qwen2.5、GPT-3.5 Turbo、GPT-4o等）的微调版本。

- baseline_control_or_counterfactual_cn：使用未微调的对应基础模型作为微调增量对照（见表3）；按文章级划分训练/验证/测试集（约80/10/10），防止同文章项目泄漏。

##### objective_metrics

1. ROC AUC

2. macro F1

3. Expected Calibration Error (ECE)

- analysis_method_cn：固定学习率与epoch超参数网格搜索；以验证集AUC为优化目标；比较微调前后delta；根据AUC排序；从性能与计算需求权衡选择模型。

- main_result_cn：DeBERTa-v3-large成为最佳分类器（AUC .911, mF1 .782, ECE .076），GPT-4o为最佳闭源分布模型，Qwen2.5-32B为最佳开源分布模型；微调普遍提升AUC但校准下降；分类器组整体优于分布模型且资源需求低。

- argumentative_role_cn：建立整个RATER系统的计算基础：证明监督微调可以实现高精度内容效度预测，并选出后续所有研究使用的RATER_C与RATER_D。

- remaining_uncertainty_cn：基准测试集内的表现不能保证对训练后发表的新量表同样有效；也不清楚人类评分者参照下的表现。

- link_to_next_phase_cn：以选出的RATER_C模型进入后续六项标准效度研究，用训练后论文和人类评分作为外部准则。

##### evidence_pointers

1. Table 2

2. Table 3

3. Model Evaluation section

#### 2. 研究1：RATER_C对管理/心理学论文作者标注的准则效度检验

- order：2

- name_cn：研究1：RATER_C对管理/心理学论文作者标注的准则效度检验

- question_cn：RATER_C在训练后发表的论文项目中，能否区分意图构念对与非意图构念对？

- inputs_and_setting_cn：8篇训练后发表文章产生的858对项目-定义对（159意图/699非意图），这些数据正用于RATER_D微调，但未被RATER_C训练看到。

- designed_or_compared_object_cn：RATER_C分类概率与作者申报的意图/非意图构念关系（ground truth）。

- baseline_control_or_counterfactual_cn：以最高概率匹配构念作为决策规则；与随机机会比较；实际使用t检验比较意图/非意图均值差异。

##### objective_metrics

1. 意图与非意图分布均值差

2. 准确率92%

3. F1=0.78

4. Cohen's kappa=0.73

- analysis_method_cn：配对t检验（比较平均概率）；混淆矩阵、F1、kappa。

- main_result_cn：意图对均值0.63显著高于非意图对0.097（p<0.001）；92%准确率；kappa=0.73显示实质性一致。

- argumentative_role_cn：提供第一层准则效度（criterion efficacy validity）：RATER_C能够对面训练后的新构念项目做出正确区分，证明领域无关性。

- remaining_uncertainty_cn：作者标注可能不等于真实人类判断；需要与独立人类评分者比较。

- link_to_next_phase_cn：研究2使用人类H&T评分者作为更生态的外部准则。

##### evidence_pointers

1. Study 1 section

2. Table 4

#### 3. 研究2：RATER_C与人类H&T评分的一致性检验

- order：3

- name_cn：研究2：RATER_C与人类H&T评分的一致性检验

- question_cn：RATER_C的概率输出是否显著预测人类H&T评分者的逐项对应性评分？

- inputs_and_setting_cn：来自同8篇文章的467对项目-定义对；Prolific平台408名参与者，平均每个项目102名评分者，执行H&T 7点评分。

- designed_or_compared_object_cn：RATER_C概率分数与人类平均H&T评分；以及以最高分数判定构念的人机一致性。

- baseline_control_or_counterfactual_cn：无人工干预；使用随机截距线性混合模型控制来源文章效应。

##### objective_metrics

1. pseudo-R²_m=0.43

2. pseudo-R²_c=0.48

3. 准确率88%

4. F1=0.82

5. kappa=0.73

- analysis_method_cn：线性混合效应模型（H&T评分 ~ RATER_C评分 + (1|Source)），似然比检验；混淆矩阵。

- main_result_cn：分类器概率显著预测H&T评分（F(1,464.03)=364.91, p<0.001）；88%人机一致。

- argumentative_role_cn：建立生态效度（ecological validity）：RATER_C的语义判断与当前黄金标准人类评分者一致，可作为人类评分的低成本代理。

- remaining_uncertainty_cn：H&T本身可能存在上下文依赖或评分者噪声；尚未与专门工具对比。

- link_to_next_phase_cn：研究3将RATER_C与现有通用LLM工具BRASS直接比较，支持优于现有制品的主张。

##### evidence_pointers

1. Study 2 section

2. Table 5

#### 4. 研究3：RATER_C与BRASS Bot的基准对比

- order：4

- name_cn：研究3：RATER_C与BRASS Bot的基准对比

- question_cn：相对于已有的通用量表开发LLM系统BRASS，RATER_C在内容效度任务上的表现如何？

- inputs_and_setting_cn：从33,304实例测试集中抽样3,303个项目/定义对；BRASS-Claude-2在poe.com平台，需订阅$20/月；定制脚本半自动调用BRASS。

- designed_or_compared_object_cn：RATER_C与BRASS Bot在相同任务上的AUC、macro F1、ECE。

- baseline_control_or_counterfactual_cn：BRASS作为现有准则制品；BRASS使用1-5评分，以5分为匹配阈值。

##### objective_metrics

1. AUC: RATER .911 vs BRASS .793

2. mF1: .782 vs .702

3. ECE: .076 vs .336

- analysis_method_cn：用代表性子集评估BRASS；与其他模型相同的按对预测任务设置。

- main_result_cn：RATER_C在所有指标上优于BRASS。

- argumentative_role_cn：证明专用、微调、透明的系统优于通用商业聊天机器人系统，排除仅靠LLM通用能力的解释。

- remaining_uncertainty_cn：BRASS为通用工具，并非专为内容效度优化；且子集抽样有限。

- link_to_next_phase_cn：既然能区分意图/非意图与优于现有工具，后续研究帮助用户解释分数并扩展代表性维度。

##### evidence_pointers

1. Study 3 section

2. Table 6

#### 5. 研究4：提出“62启发式”阈值以支持对应性与区分性判断

- order：5

- name_cn：研究4：提出“62启发式”阈值以支持对应性与区分性判断

- question_cn：研究者应如何解释RATER_C分数，以决定哪些项目具有足够的对应性与区分性？

- inputs_and_setting_cn：用于早期基准测试的大型holdout集（33,304测试实例）。

- designed_or_compared_object_cn：对意图构念与非意图构念RATER_C分数的均值分布。

- baseline_control_or_counterfactual_cn：以均值作为阈值；与Type I/II错误平衡论证对照。

##### objective_metrics

1. 意图对均值0.620

2. 非意图对均值0.061

- analysis_method_cn：描述性均值比较；基于清晰论证设定启发式。

- main_result_cn：提出对应性阈值≥0.620、区分性阈值≤0.062（62启发式），并强调这是模型特定的临时指导而非硬规则。

- argumentative_role_cn：把模型输出转化为研究者可操作的决定规则，为在线系统提供默认标记阈值。

- remaining_uncertainty_cn：阈值缺乏正式经验检验；不同决策规则会改变阈值。

- link_to_next_phase_cn：研究5继续扩展第三个维度代表性；阈值启发式也集成到Web界面。

##### evidence_pointers

1. Study 4 section

#### 6. 研究5：用softmax将RATER_C扩展到多维构念代表性评估

- order：6

- name_cn：研究5：用softmax将RATER_C扩展到多维构念代表性评估

- question_cn：能否利用RATER_C分数为多维构念的代表性提供计算化评估？

- inputs_and_setting_cn：MacKenzie等人（2011）关于trustworthiness的三个子维度（benevolence, integrity, ability）与三个示例项目的说明性数据。

- designed_or_compared_object_cn：RATER_C对应分数经softmax归一化后的维度比例 vs MacKenzie等人报告的人工比例。

- baseline_control_or_counterfactual_cn：MacKenzie等人的虚构人工评分为传统方法参照。

##### objective_metrics

1. 每个维度的softmax比例

- analysis_method_cn：softmax归一化；逐项比较表7中两方法对三个项目的判断。

- main_result_cn：RATER_C指出该三项目量表对benevolence代表性不足（5%），而MacKenzie等人的数字显示三个维度约各占三分之一；两者对能力与诚信一致。

- argumentative_role_cn：首次为代表性提供计算路径，补足内容效度三标准中的缺口。

- remaining_uncertainty_cn：仅适用于多维构念；未提供单维构念代表性问题。

- link_to_next_phase_cn：研究6检验真实用户是否愿意使用这样的系统。

##### evidence_pointers

1. Study 5 section

2. Table 7

#### 7. 研究6：专家适用性检查与用户体验评价

- order：7

- name_cn：研究6：专家适用性检查与用户体验评价

- question_cn：高水平的构念验证专家如何评价RATER系统的易用性、有用性与使用意向？

- inputs_and_setting_cn：7名来自欧洲和美国的非本项目外部专家；一次1小时培训；至少一周使用www.contval.org；按Venkatesh等人问卷测量。

- designed_or_compared_object_cn：系统使用体验；定性评论。

- baseline_control_or_counterfactual_cn：无对照组；以专家预期和反馈为参照。

##### objective_metrics

1. 易用性μ=6.6/7

2. 有用性μ=5.7/7

3. 使用意向μ=5.3/7

- analysis_method_cn：描述性统计与主题式定性分析。

- main_result_cn：专家认为系统易用且有用，但有保留；只有2/7此前系统执行内容验证；用户担心无法理解底层语义分析。

- argumentative_role_cn：提供设计科学中的applicability check，证明系统在真实研究者中的相关性、可接受性与准备度；反馈促使界面改进与引入阈值。

- remaining_uncertainty_cn：样本小，未测量实际后续使用；定量意图低于易用性。

- link_to_next_phase_cn：下一节展示一个独立团队真实使用案例，将适用性延伸到外部研究过程。

##### evidence_pointers

1. Study 6 section

#### 8. 外部使用案例：信任量表内容效度评估

- order：8

- name_cn：外部使用案例：信任量表内容效度评估

- question_cn：在一个独立研究者团队的量表验证项目中，RATER_C与传统H&T程序的结果如何比较？

- inputs_and_setting_cn：Vitari等人（2025）的6个信任相关量表，56个项目、10个定义（6种现有信任定义、1个新定义、3个轨道构念）；H&T由313名Prolific参与者完成，平均每项54人，成本约$2,000；随后同一团队使用RATER_C分析相同数据；作者又邀请5名专家对一组项目排序。

- designed_or_compared_object_cn：RATER_C输出与人类H&T平均分数；同时与专家项目排序对比。

- baseline_control_or_counterfactual_cn：H&T程序作为现行人工标准；5名专家排序作为独立基准。

##### objective_metrics

1. 信任构念对应性得分

2. RATER与专家排序相关性 .97

3. H&T与专家排序相关性 .03

- analysis_method_cn：直接比较表8中两方法得分；计算专家排序与RATER/H&T分数的相关；双尾配对t检验。

- main_result_cn：总体上两方法在多数构念上收敛，但也出现分歧：如T2项H&T认为测量隐私控制而RATER和专家认为不是；T4项H&T认为测量信任而RATER/专家认为否；RATER与专家排序相关0.97，而H&T相关0.03。

- argumentative_role_cn：提供外部生态效度与互补性证据：RATER能指出H&T可能被语境污染等问题，并为迭代修订（如删除“and communicate”、撰写基于Leventhal子维度的新项目）提供即时反馈。

- remaining_uncertainty_cn：单个领域案例；专家排序仅5个项目，统计效力有限。

- link_to_next_phase_cn：随后讨论与限制部分探讨模型边界（如可读性影响）与未来方向。

##### evidence_pointers

1. Illustration section

2. Table 8

3. Table 9

#### 9. 稳健性分析：可读性对模型正确性的影响

- order：9

- name_cn：稳健性分析：可读性对模型正确性的影响

- question_cn：项目与定义的语言可读性是否影响RATER_C的预测正确性？

- inputs_and_setting_cn：33,304个测试实例的Flesch Reading Ease分数（定义与项目拼接计算）。

- designed_or_compared_object_cn：模型正确性在高、低可读性条件下的差异。

- baseline_control_or_counterfactual_cn：无干预；以χ²检验关联。

##### objective_metrics

1. χ²(1)=77.94

2. p<0.001

3. 低可读性时准确率约85%，高可读性超过93%

- analysis_method_cn：卡方检验；系统增加可读性警告功能。

- main_result_cn：可读性显著预测正确性；为此在RATER系统中加入Flesch分数≤25的可调警告，操作化MacKenzie等人的易读性建议。

- argumentative_role_cn：界定边界条件：模型对复杂语法/句法敏感；同时提供缓解措施，增强设计知识的实用性。

- remaining_uncertainty_cn：只考察了可读性，未涉及其他表面语言特征。

- link_to_next_phase_cn：直接引入Limitations and Future Work中的单维代表性、开源模型更新等议题。

##### evidence_pointers

1. Limitations and Future Work section

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 内容验证是量表开发核心但常被跳过

2. PRACTICAL_STAKES: 成本高且需要专家阻碍执行

3. RQ_OR_OBJECTIVE: 引入RATER系统

4. THEORY_INTRO: 以心理测量理论为指导

5. DESIGN_FEATURE: 两类AI模型与开放平台

6. STUDY_OVERVIEW: 六项研究确认准确性可靠性有用性

7. CONTRIBUTION: 提升行为研究测量效度

### introduction_moves

1. CONTEXT: 内容验证受到多学科关注并指导量表开发

2. THEORY_INTRO: 内容效度三重标准——对应性、区分性、代表性

3. LIMITATION: 手工流程虽多但出版研究很少执行（19-26%）

4. PRACTICAL_STAKES: 忽视内容效度阻碍科学进展

5. LIMITATION: 成本、时间、认知、可复制性是主要原因

6. RQ_OR_OBJECTIVE: 提出AI辅助方法覆盖新编、改编和现有量表

7. CONTRIBUTION: 宣称最高性能内容效度模型

8. DESIGN_FEATURE: 开源平台、RATER_C与RATER_D

9. CONTRIBUTION: 透明可复制benchmark，邀请未来模型超越

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: item sorting与item rating两种主导方法

2. THEORY_INTRO: 定义对应性与定义区分性概念

3. MECHANISM: 高对应/低区分产生污染，低对应/高区分产生缺陷

4. LIMITATION: 代表性没有正式程序

5. PRIOR_KNOWLEDGE: 内容验证转向语义化、非专家评分者、短量表

6. MECHANISM: 内容验证类似语义解析任务

7. LIMITATION: 现有流程的五大挑战

8. GAP: 新方法应利用AI突破人类认知与资源限制

9. REQUIREMENT: 表1将挑战映射为自动工具需求

### artifact_design_moves

1. METHOD_JUSTIFICATION: 监督学习优于无监督；微调小模型可超越大模型

2. DESIGN_FEATURE: 概率分类器与分布模型两种输出

3. METHOD_JUSTIFICATION: 跨八学科语料构建287K配对数据

4. METHOD_JUSTIFICATION: 文章级划分避免泄漏

5. METHOD_JUSTIFICATION: 用八篇文章与人类H&T数据微调分布模型

6. METHOD_JUSTIFICATION: 网格搜索微调15分类器与13分布模型

7. BENCHMARK_OR_CONTRAST: 以AUC/F1/ECE评价模型

8. RESULT: 选择DeBERTa-v3-large为RATER_C，GPT-4o为RATER_D

9. DESIGN_FEATURE: Web界面模块化，支持用户设置阈值

### evaluation_moves

1. STUDY_OVERVIEW: 六项汇总性准则效度研究

2. HYPOTHESIS_OR_PROPOSITION: RATER_C应能区分意图与非意图

3. RESULT: t检验显著，准确率92%

4. HYPOTHESIS_OR_PROPOSITION: RATER_C应与人类H&T评分一致

5. METHOD_JUSTIFICATION: 线性混合模型控制来源随机效应

6. RESULT: 显著预测H&T，人机一致88%

7. TRANSITION: 研究1/2提供准则效度与生态效度

8. RESULT: RATER_C优于BRASS

9. DESIGN_FEATURE: 提出62启发式阈值

10. RESULT: softmax实现代表性评估

11. RESULT: 专家适用性检查认可易用性与有用性

### discussion_and_contribution_moves

1. CONTRIBUTION: 领域无关模型优于Fyffe等人专用模型与BRASS

2. CONTRIBUTION: 大规模benchmark数据集与方法

3. CONTRIBUTION: 首个多维代表性计算途径

4. CONTRIBUTION: 适用性检查证明现实相关

5. CONTRIBUTION: 开源透明可复制平台

6. BOUNDARY_CONDITION: 对可读性敏感并加入警告

7. LIMITATION_AND_FUTURE: 单维代表性尚未解决

8. CONTRIBUTION: RATER使内容验证更易执行，提升测量质量

## 理论/知识到设计的翻译

### 知识/理论基础

1. 心理测量理论中的内容效度三重标准（correspondence, distinctiveness, representativeness）

2. Hinkin & Tracey (1999)的项目评级程序

3. Anderson & Gerbing (1991)项目分类程序

4. Colquitt et al. (2019)的definitional correspondence/distinctiveness

5. MacKenzie et al. (2011)的构念测量与验证流程

6. 监督学习、BERT/GPT系列语言模型与语义解析任务

7. Larsen et al. (2025)设计科学效度框架

- 理论—设计耦合：direct

- 耦合判定理由：内容效度理论的三重标准与H&T评级程序直接规定了系统的输出形式和评价维度：RATER_C输出匹配概率用于对应性/区分性，RATER_D输出1-7评分用于模拟H&T评分者，代表性用softmax归一化；六项研究均直接检验这些理论要求。虽然具体LLM架构选择来自NLP工程，但制品的核心设计特征由心理测量理论前瞻性决定。

- 理论到设计翻译链：内容效度三重标准（对应性、区分性、代表性）→ 语义匹配概率与人类评审分布机制 → 要求系统能够快速输出项目-定义匹配分数、覆盖所有轨道构念、聚合为维度代表性 → 设计RATER_C分类器与RATER_D生成分布模型 → 在Web界面中提供对应性、区分性、代表性三项输出 → 通过Study 1-6和信任量表案例检验每一条设计映射。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：每个项目应反映其意图构念的定义（correspondence）

- mechanism_cn：项目文本与构念定义之间存在可计算的语义匹配概率

- design_requirement_cn：模型输出项目-定义匹配概率，并可由用户解释

- artifact_choice_cn：RATER_C：微调DeBERTa-v3-large概率分类器

- evaluated_contrast_cn：意图构念对 vs 非意图构念对的概率分布

- objective_result_cn：意图对均值0.63 vs 非意图对0.097；准确率92%

##### evidence_pointers

1. Study 1

2. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：项目应避免与无关构念定义重叠（distinctiveness）

- mechanism_cn：对每个项目可与多个非意图定义计算匹配概率，低分表示区分性高

- design_requirement_cn：系统应允许加入所有轨道构念并输出每个定义的概率，而不只是两个对照定义

- artifact_choice_cn：RATER_C提供对所有定义的得分矩阵

- evaluated_contrast_cn：非意图构念定义得分的分布与意图得分的差异

- objective_result_cn：非意图对均值0.061；62启发式规定非意图得分≤0.062为高区分

##### evidence_pointers

1. Study 4

2. Study 1 t-test

#### 3. 3

- theory_or_knowledge_claim_cn：量表项目集应共同覆盖构念内容域（representativeness）

- mechanism_cn：多维构念的各子维度应按比例得到项目覆盖；可对每个维度的得分归一化衡量占比

- design_requirement_cn：系统能对多个子维度输出对应分数并聚合为代表性指标

- artifact_choice_cn：RATER_C分数结合softmax归一化

- evaluated_contrast_cn：RATER_C与MacKenzie等人说明性人工评分在三个trustworthiness子维度上的比例

- objective_result_cn：RATER_C显示benevolence占比5%，而人工评分约为32%；识别代表性不足

##### evidence_pointers

1. Study 5

2. Table 7

#### 4. 4

- theory_or_knowledge_claim_cn：H&T程序使用评分者在1-7量表上逐对评估项目与定义匹配

- mechanism_cn：生成式LLM可充当合成评分者，产生评分分布

- design_requirement_cn：提供一个分布模型，输出1-7分Likert评分，可生成Colquitt等人指标

- artifact_choice_cn：RATER_D：微调GPT-4o / Qwen2.5-32B等生成模型

- evaluated_contrast_cn：微调后 vs 未微调模型的AUC/F1/ECE

- objective_result_cn：微调提升AUC；RATER_D在benchmark中接近RATER_C，但计算成本更高

##### evidence_pointers

1. Table 2

2. Table 3

#### 5. 5

- theory_or_knowledge_claim_cn：人类认知限制与资源成本抑制内容验证执行

- mechanism_cn：AI模型不受项目数量增加影响，迭代成本低

- design_requirement_cn：免费、快速、可复制、无需项目专用工程的在线平台

- artifact_choice_cn：公开Web系统www.contval.org，开放权重，模块化模型接入

- evaluated_contrast_cn：外部专家的可用性/有用性评分；独立团队真实项目

- objective_result_cn：易用性6.6/7，有用性5.7/7；外部案例与H&T结果总体一致且能补充

##### evidence_pointers

1. Study 6

2. Illustration section

## 评价逻辑

### evaluation_modes

1. 离线benchmark

2. 准则效度检验（criterion validity）

3. 人类评分者一致性检验

4. 与现有计算制品对比

5. 阈值启发式分析

6. 代表性扩展演示

7. 用户适用性检查

8. 外部现场/案例应用

9. 稳健性分析（可读性）

- why_these_evaluations_cn：设计科学工件需要从内部一致性、外部准则和实际可用性三个层面累积证据：先以大规模holdout与微调增量证明模型本身可靠，再用训练后文章作者标注证明领域外泛化，再用人类H&T评分证明与黄金标准一致，再与BRASS对比证明相对优势，然后通过阈值与代表性演示把输出变成设计知识，最后通过专家适用性检查与独立团队案例证明真实可推广。

- benchmark_and_contrast_chain_cn：基准链条为：大测试集（33,304实例）→ 训练后论文样本（858对）→ H&T人类评分（467对）→ BRASS有限子集（3,303对）→ 代表性演示（MacKenzie三项目）→ 专家工作流（56项信任量表）。每一步对照物从算法机会基线逐步升级为人类专家、现有工具和真实研究项目，使证据从“模型能工作”上升到“模型对科学实践有用”。

### claim_evidence_ledger

1. 技术主张：RATER_C优于其他模型/BRASS→证据：Table 2、Table 6的AUC/F1/ECE；强支持。

2. 制品主张：RATER_C能区分意图/非意图对应→证据：Study 1 t检验、准确率；强支持。

3. 制品主张：RATER_C与人类H&T评分一致→证据：Study 2 LMM、准确率；强支持。

4. 机制主张：内容验证等价于语义解析，模型学到的是语义匹配→证据：间接来自跨领域性能和可读性边界；弱到中等。

5. 边界主张：领域无关、免费、可复制→证据：八学科训练、开源平台、Study 6；部分支持，但未覆盖所有领域。

6. 设计知识：62启发式、softmax代表性→证据：Study 4/5演示；中等支持，需社区验证。

7. 理论贡献：提供代表性计算途径→证据：说明性演示；初步，非全面验证。

- internal_validity_strategy_cn：文章级划分训练/测试避免同源泄漏；使用训练后发表的文章作为外部样本；固定随机种子；在H&T对比中使用随机截距控制来源文章；预先注册ground truth为作者申报或人类均分；在BRASS对比中使用相同预测输入设置。

- external_validity_strategy_cn：训练数据跨八学科；测试样本含训练后论文；外部专家小组覆盖欧洲与美国；独立团队使用真实信任量表项目；公开平台与benchmark允许其他研究者再检验。

- what_is_not_actually_tested_cn：阈值启发式（62）没有经过正式决策效用检验；代表性方法仅用说明性三项目示例；未测量RATER使用前后对量表最终质量/发表结果的影响；专家排序只需5个项目，相关值不稳定；与BRASS比较仅抽样子集且版本可能过时；未验证用户对评分指标的心理测量可信度的理解。

## 贡献闭环

- technical_claim_cn：RATER_C/RATER_D在内容效度预测任务上达到目前最高公开性能；RATER_C在AUC/F1/ECE上优于所有对比分布模型和BRASS Bot。

- artifact_claim_cn：RATER系统作为可免费使用的Web平台，提供对对应性、区分性和代表性的自动评估；RATER_C是高效可复制的分类器，RATER_D可模拟人类H&T评分者。

- mechanism_claim_cn：信息机制是语义对齐：项目文本与构念定义之间的概率匹配，等价于对语义解析任务进行监督学习；内容效度任务与语义解析任务存在结构相似。

- boundary_claim_cn：系统领域无关、跨八学科、无需专用GPU即可使用RATER_C；但对复杂语法/句法可读性敏感；代表性方法目前仅适用于多维构念。

- reusable_design_knowledge_cn：（1）以“62启发式”作为模型特定阈值的实例，强调社区共识形成；（2）用softmax将对应概率聚合为维度代表性比例的方法；（3）以文章级分割构造大规模配对语料的评估范式；（4）模块化模型接入与Kaggle竞赛机制，便于未来模型比较。

- theoretical_contribution_cn：将当代LLM的语义能力引入心理测量学内容效度流程；把“代表性”从一个讨论性概念转化为可计算输出；用设计科学效度框架将AI工具纳入构念验证研究。

- how_discussion_closes_intro_gap_cn：讨论重新回到引言中“内容验证虽有大量程序但研究者很少执行”的缺口，指出RATER降低了成本、时间与技能门槛，使内容验证成为可迭代、可复制、低成本的标准步骤；同时开放benchmark使未来研究者能持续提高性能，避免一次性成果。

- overclaim_or_unsupported_leaps_cn：“最高性能”主张仅基于所选模型池和测试集；“领域无关”推断基于过训练学科但未覆盖所有行为场景；代表性方法用人为说明性项目而非真实心理测量学示范；专家排序相关0.97基于5个点，结论不稳健；将H&T在T2/T4的错误解释归因于H&T局限，可能过度解读。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：内容验证是量表开发中确保测量工具捕捉目标构念的关键步骤。

- rhetorical_function_cn：开门见山定位研究对象——内容效度对行为研究测量的基础性作用。

- depends_on_cn：无。

- sets_up_cn：为后文指出这一关键步骤却很少被执行制造张力。

- evidence_pointer：Abstract

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：但由于需要昂贵数据收集和专门专家，研究者很少执行这一核心步骤。

- rhetorical_function_cn：点明问题后果与原因，建立现实操作性缺口。

- depends_on_cn：依赖前句对内容验证重要性的陈述。

- sets_up_cn：引出需要低成本、易用的替代工具。

- evidence_pointer：Abstract

### 3. Abstract P2 S1

- order：3

- section：Abstract

- locator：Abstract P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者提出RATER，一个免费网页系统，帮助科学家、评审和学生获得内容效度的快速可靠洞察。

- rhetorical_function_cn：宣布本文核心制品与目标受众。

- depends_on_cn：依赖缺口陈述。

- sets_up_cn：后续介绍系统构成与验证。

- evidence_pointer：Abstract

### 4. Abstract P2 S2

- order：4

- section：Abstract

- locator：Abstract P2 S2

- move_code：THEORY_INTRO

- paraphrase_cn：系统以心理测量理论为指导，评估项目是否对应目标构念、是否区别于其他构念、是否充分代表内容域。

- rhetorical_function_cn：给出设计背后的理论锚点。

- depends_on_cn：承接RATER系统的介绍。

- sets_up_cn：为RATER_C/D的输出标准提供理论依据。

- evidence_pointer：Abstract

### 5. Abstract P3 S1

- order：5

- section：Abstract

- locator：Abstract P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统使用两个独特AI模型，利用来自2,443篇论文的心理测量量表以及BERT和GPT架构。

- rhetorical_function_cn：概述技术实现与规模。

- depends_on_cn：基于理论指导。

- sets_up_cn：引出下文细致的技术构造说明。

- evidence_pointer：Abstract

### 6. Abstract P4 S1

- order：6

- section：Abstract

- locator：Abstract P4 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：六项互补研究确认RATER的准确性、可靠性和有用性。

- rhetorical_function_cn：预告评价体系，建立可信度预期。

- depends_on_cn：模型介绍。

- sets_up_cn：直接对应正文的六个Study。

- evidence_pointer：Abstract

### 7. Abstract P5 S1

- order：7

- section：Abstract

- locator：Abstract P5 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者认为RATER能增强量表开发与验证流程，提升行为研究发现的有效性。

- rhetorical_function_cn：形成摘要层面的最终贡献声明。

- depends_on_cn：依赖前叙系统与证据。

- sets_up_cn：向读者传达研究的价值与影响。

- evidence_pointer：Abstract

### 8. Introduction P1 S1–S2

- order：8

- section：Introduction

- locator：Introduction P1 S1–S2

- move_code：CONTEXT

- paraphrase_cn：内容验证在信息系统、行为医学、教育等多个学科都受到关注，并为新量表、量表改编和现有量表再评估提供正式程序。

- rhetorical_function_cn：建立内容验证的跨学科地位和三种应用场景。

- depends_on_cn：无独立经验证据，用文献引用支撑。

- sets_up_cn：后续指出尽管重要却很少被执行。

- evidence_pointer：Introduction P1

### 9. Introduction P2 S1–S3

- order：9

- section：Introduction

- locator：Introduction P2 S1–S3

- move_code：THEORY_INTRO

- paraphrase_cn：内容效度通过三方面评估：项目对应目标构念、项目与无关构念区分、项目集代表构念域。

- rhetorical_function_cn：定义全文的核心标准框架。

- depends_on_cn：基于相关文献的定义。

- sets_up_cn：成为后面理论到设计的翻译基础。

- evidence_pointer：Introduction P2

### 10. Introduction P3 S1–S3

- order：10

- section：Introduction

- locator：Introduction P3 S1–S3

- move_code：LIMITATION

- paraphrase_cn：虽然有多种手工内容效度方法，但已发表研究很少包含内容效度评估，IS中比例约19-26%。

- rhetorical_function_cn：用统计数据凸显实践缺口。

- depends_on_cn：已有文献估计。

- sets_up_cn：引出对原因的分析。

- evidence_pointer：Introduction P3

### 11. Introduction P3 S4

- order：11

- section：Introduction

- locator：Introduction P3 S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：对内容效度关注不足被视为科学进展的重大障碍，会引发对测量与构念概念域之间关系的质疑。

- rhetorical_function_cn：放大问题后果，提升研究必要性。

- depends_on_cn：依赖执行率低的证据。

- sets_up_cn：为解决方案提供紧迫性。

- evidence_pointer：Introduction P3

### 12. Introduction P4 S1–S3

- order：12

- section：Introduction

- locator：Introduction P4 S1–S3

- move_code：LIMITATION

- paraphrase_cn：推测原因包括招募人类评分者的成本、困难和时间，研究者不知如何操作，程序解释有歧义，人类认知局限，以及程序不可复制。

- rhetorical_function_cn：系统列出阻碍内容验证的多重原因，为AI方案提供精确靶点。

- depends_on_cn：引用Cortina、Colquitt、Hoehle等人观点。

- sets_up_cn：后文逐一将这些原因转化为设计需求。

- evidence_pointer：Introduction P4

### 13. Introduction P5 S1–S2

- order：13

- section：Introduction

- locator：Introduction P5 S1–S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文提出利用AI进行内容验证的新方法，适用于新开发、改编与已有量表，并特别关注三个内容效度评估。

- rhetorical_function_cn：正式宣布研究问题与目标。

- depends_on_cn：基于前述缺口。

- sets_up_cn：为系统开发和验证奠定目标。

- evidence_pointer：Introduction P5

### 14. Introduction P6 S1

- order：14

- section：Introduction

- locator：Introduction P6 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者宣称提出迄今性能最高的内容效度评估模型，计算路径与传统手工程序有本质区别。

- rhetorical_function_cn：提前输出最强贡献声明，吸引读者。

- depends_on_cn：基于研究目标。

- sets_up_cn：需要用整个评价体系支持该声明。

- evidence_pointer：Introduction P6

### 15. Introduction P7 S1–S3

- order：15

- section：Introduction

- locator：Introduction P7 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统降低人工、成本、时间，可复制，开放扩展，包含RATER_C与RATER_D两个模型。

- rhetorical_function_cn：快速描述系统核心特征。

- depends_on_cn：贡献声明。

- sets_up_cn：为后续模型细节做预告。

- evidence_pointer：Introduction P7

### 16. Introduction P8 S1–S2

- order：16

- section：Introduction

- locator：Introduction P8 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：RATER_D利用生成AI通过合成评分者模拟H&T评级程序，用更少训练数据获得竞争力，并生成传统内容效度指标。

- rhetorical_function_cn：区分两类模型的不同定位。

- depends_on_cn：对RATER系统的整体介绍。

- sets_up_cn：解释为何需要两个模型。

- evidence_pointer：Introduction P8

### 17. Introduction P9 S1–S3

- order：17

- section：Introduction

- locator：Introduction P9 S1–S3

- move_code：CONTRIBUTION

- paraphrase_cn：开放透明可复现的评估将模型确立为未来研究的基准工件，并邀请其他研究者加入超越自有模型。

- rhetorical_function_cn：通过开放性保护贡献不被模型迭代淘汰。

- depends_on_cn：平台与模型介绍。

- sets_up_cn：Discussion中的第五项贡献与平台愿景。

- evidence_pointer：Introduction P9

### 18. Overview P1 S1

- order：18

- section：Conceptual Background

- locator：Overview P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：当前主导的内容效度程序有项目分类和项目评级两种。

- rhetorical_function_cn：介绍领域现有操作化方法。

- depends_on_cn：无法。

- sets_up_cn：后文比较两者的形式并引出语义任务相似性。

- evidence_pointer：Conceptual Background, Overview

### 19. Overview P2 S1

- order：19

- section：Conceptual Background

- locator：Overview P2 S1

- move_code：THEORY_INTRO

- paraphrase_cn：这些程序生成的数据可用来评估定义对应性和定义区分性。

- rhetorical_function_cn：将程序输出连接至两个核心构念。

- depends_on_cn：程序介绍。

- sets_up_cn：为RATER_C输出概率提供理论语言。

- evidence_pointer：Conceptual Background, Overview

### 20. Overview P3 S1–S2

- order：20

- section：Conceptual Background

- locator：Overview P3 S1–S2

- move_code：MECHANISM

- paraphrase_cn：高对应但低区分产生污染测量，高区分但低对应产生缺陷测量，只有两者都高的项目才保留。

- rhetorical_function_cn：解释内容效度判断的机制性后果。

- depends_on_cn：对应性与区分性定义。

- sets_up_cn：后文阈值判断与项目筛选标准。

- evidence_pointer：Conceptual Background, Overview

### 21. Overview P4 S1

- order：21

- section：Conceptual Background

- locator：Overview P4 S1

- move_code：LIMITATION

- paraphrase_cn：代表性关注项目集是否覆盖构念全部相关方面，但目前文献中没有正式评估程序，该部分只是初步。

- rhetorical_function_cn：指出现有方法论的盲区。

- depends_on_cn：前面对应性/区分性的讨论。

- sets_up_cn：为Study 5和未来工作提供缺口。

- evidence_pointer：Conceptual Background, Overview

### 22. Overview P5 S1–S3

- order：22

- section：Conceptual Background

- locator：Overview P5 S1–S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：现代内容效度程序出现三个变化：强调构念与项目语义联系、偏好非专家评分者、短量表使代表性更受关注。

- rhetorical_function_cn：总结领域趋势，引导设计选择。

- depends_on_cn：前面程序描述。

- sets_up_cn：解释为何AI语义模型能契合现代程序。

- evidence_pointer：Conceptual Background, Overview

### 23. Overview P6 S1–S2

- order：23

- section：Conceptual Background

- locator：Overview P6 S1–S2

- move_code：MECHANISM

- paraphrase_cn：当前内容验证活动类似于语义解析任务，即把文本转换为逻辑形式以提取意义，作者据此构建AI系统。

- rhetorical_function_cn：建立内容验证与NLP任务之间的类比，为选择语言模型提供合理性。

- depends_on_cn：概述中的语义转向。

- sets_up_cn：为Development部分使用Transformer模型提供理论连接。

- evidence_pointer：Conceptual Background, Overview

### 24. Key Challenges P1 S1

- order：24

- section：Conceptual Background

- locator：Key Challenges P1 S1

- move_code：LIMITATION

- paraphrase_cn：现有程序无法容纳多个量表，评分者会被认知压垮，尤其H&T要求对每对项目-定义做精细数值评级。

- rhetorical_function_cn：点出可扩展性缺陷。

- depends_on_cn：前面程序介绍。

- sets_up_cn：论证AI不受人类认知限制。

- evidence_pointer：Key Challenges section

### 25. Key Challenges P2 S1

- order：25

- section：Conceptual Background

- locator：Key Challenges P2 S1

- move_code：LIMITATION

- paraphrase_cn：招募数百名参与者可能花费高达一万美元，加剧全球研究资源不平等。

- rhetorical_function_cn：强调资源门槛与公平问题。

- depends_on_cn：引用Colquitt等实例。

- sets_up_cn：为免费平台提供正当性。

- evidence_pointer：Key Challenges section

### 26. Key Challenges P3 S1

- order：26

- section：Conceptual Background

- locator：Key Challenges P3 S1

- move_code：LIMITATION

- paraphrase_cn：量表趋于缩短且结构方程与alpha标准刺激冗余项，威胁代表性，而当前框架无法评估代表性。

- rhetorical_function_cn：指出短量表趋势带来的潜在危害。

- depends_on_cn：前面代表性定义。

- sets_up_cn：为Study 5代表性扩展铺路。

- evidence_pointer：Key Challenges section

### 27. Key Challenges P4 S1

- order：27

- section：Conceptual Background

- locator：Key Challenges P4 S1

- move_code：LIMITATION

- paraphrase_cn：现有方法不能很好适应量表开发的迭代性质，而LLM自动生成项目使迭代更易发生，需要廉价快速技术。

- rhetorical_function_cn：指出迭代需求缺口。

- depends_on_cn：量表开发迭代观。

- sets_up_cn：支持RATER提供即时反馈的重要价值。

- evidence_pointer：Key Challenges section

### 28. Key Challenges P5 S1–S2

- order：28

- section：Conceptual Background

- locator：Key Challenges P5 S1–S2

- move_code：LIMITATION

- paraphrase_cn：当前程序要求评分者在给定项目与构念集合内判断，因此对应性和区分性得分会随集合中是否包含其他构念与项目而变化，且尚未有人检验这种敏感性。

- rhetorical_function_cn：揭示人类程序的上下文依赖缺陷。

- depends_on_cn：前面对程序机制的描述。

- sets_up_cn：为AI基于全部定义评分的优势提供论证。

- evidence_pointer：Key Challenges section

### 29. Key Challenges P6 S1–S2

- order：29

- section：Conceptual Background

- locator：Key Challenges P6 S1–S2

- move_code：GAP

- paraphrase_cn：作者主张需要新方法来克服这些挑战，AI不受人类认知限制、不随项目数增加额外资源、可廉价执行多轮迭代。

- rhetorical_function_cn：综合缺口与方案方向。

- depends_on_cn：前五个挑战。

- sets_up_cn：为表1的挑战到需求映射提供总纲。

- evidence_pointer：Key Challenges section

### 30. Table 1 intro

- order：30

- section：Conceptual Background

- locator：Table 1 intro

- move_code：REQUIREMENT

- paraphrase_cn：表1列出构念开发过程核心组件、关键挑战与自动工具需求，本文聚焦第三步的对应性、区分性和代表性。

- rhetorical_function_cn：将问题清单转换为设计需求清单。

- depends_on_cn：之前五挑战分析。

- sets_up_cn：指导RATER系统功能设计。

- evidence_pointer：Table 1附近

### 31. Current AI Use P1 S1

- order：31

- section：Conceptual Background

- locator：Current AI Use P1 S1

- move_code：LIMITATION

- paraphrase_cn：以往计算努力没有直接解决量表开发早期步骤中已识别的挑战，如概念定义不清、冗余项目与代表性。

- rhetorical_function_cn：批评现有计算工具的病点。

- depends_on_cn：构念开发流程。

- sets_up_cn：为RATER专攻第三步做铺垫。

- evidence_pointer：Current Use of AI-Based Approaches section

### 32. Current AI Use P2 S1–S2

- order：32

- section：Conceptual Background

- locator：Current AI Use P2 S1–S2

- move_code：LIMITATION

- paraphrase_cn：自动项目生成与内容效度测量互补，但不会解决效度问题，甚至可能因低质量项增加冗余。

- rhetorical_function_cn：区分自己工作与自动项目生成。

- depends_on_cn：前面对项目生成文献的梳理。

- sets_up_cn：明确RATER定位为效度评估而非生成。

- evidence_pointer：Current Use of AI-Based Approaches section

### 33. Current AI Use P3 S1–S6

- order：33

- section：Conceptual Background

- locator：Current AI Use P3 S1–S6

- move_code：LIMITATION

- paraphrase_cn：黑盒通用对话模型有六个缺陷：不透明、不可靠、不可复制、有财务成本、缺乏量表级支持、非专门优化。

- rhetorical_function_cn：系统否定通用LLM作为科学工具的直接可用性。

- depends_on_cn：对ChatGPT等工具的观察。

- sets_up_cn：引出RATER对透明可复制开放平台的定位。

- evidence_pointer：Current Use of AI-Based Approaches section

### 34. Current AI Use P4 S1–S2

- order：34

- section：Conceptual Background

- locator：Current AI Use P4 S1–S2

- move_code：LIMITATION

- paraphrase_cn：BRASS解决部分限制但部署在需付费平台，且被作者自评在项目-定义对应任务上表现不足，也不支持量表级指标。

- rhetorical_function_cn：给出现有最接近系统的不足，作为Study 3对手。

- depends_on_cn：六缺陷分析。

- sets_up_cn：Study 3直接比较RATER与BRASS。

- evidence_pointer：Current Use of AI-Based Approaches section

### 35. Current AI Use P5 S1–S2

- order：35

- section：Conceptual Background

- locator：Current AI Use P5 S1–S2

- move_code：LIMITATION

- paraphrase_cn：Fyffe等人是唯一专门聚焦内容效度的计算方法，但限定于Big Five人格域，需要用户自行训练/微调模型，难以推广。

- rhetorical_function_cn：说明现有专门方法领域受限。

- depends_on_cn：对Fyffe等人工作的概述。

- sets_up_cn：为RATER的领域无关性主张提供对照。

- evidence_pointer：Current Use of AI-Based Approaches section

### 36. Current AI Use P6 S1–S2

- order：36

- section：Conceptual Background

- locator：Current AI Use P6 S1–S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者提出一个领域无关、开源、无成本的平台，集成可靠透明的模型，并兼容开放权重与商业API。

- rhetorical_function_cn：在文献梳理后给出RATER平台的具体定位。

- depends_on_cn：前面对黑盒、BRASS、Fyffe不足的分析。

- sets_up_cn：Development部分据此展开实现。

- evidence_pointer：Current Use of AI-Based Approaches section

### 37. Dev P1 S1–S2

- order：37

- section：Development of AI Models

- locator：Dev P1 S1–S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：监督学习模型因使用定制训练数据而优于无监督模型；高质量微调的小BERT模型也能超越更大GPT模型。

- rhetorical_function_cn：为核心建模策略提供理由。

- depends_on_cn：NLP性能研究。

- sets_up_cn：后续微调多种模型的合理性。

- evidence_pointer：Development of AI Models section

### 38. Dev P2 S1

- order：38

- section：Development of AI Models

- locator：Dev P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者评估多种LLM并开发两类模型：概率分类器与分布模型，后者模拟H&T评分者生成1-7评分。

- rhetorical_function_cn：明确两个技术路线对应两种理论操作化。

- depends_on_cn：前面内容效度程序与语义解析类比。

- sets_up_cn：建模细节与benchmark。

- evidence_pointer：Development of AI Models section

### 39. Fine-Tuning Data P1 S1

- order：39

- section：Development of AI Models

- locator：Fine-Tuning Data P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：数据集来源于八个学科2443篇论文，对论文内项目与定义做交叉积，产生意图与非意图配对共287,426对。

- rhetorical_function_cn：介绍训练语料规模与构造成分。

- depends_on_cn：需要数据支撑监督学习。

- sets_up_cn：后续划分和模型训练。

- evidence_pointer：Fine-Tuning and Evaluation Data section

### 40. Fine-Tuning Data P2 S1

- order：40

- section：Development of AI Models

- locator：Fine-Tuning Data P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：按文章级随机抽样将数据分为约80/10/10，避免同一文章的项目同时出现在训练和测试中。

- rhetorical_function_cn：说明内部有效性保障措施。

- depends_on_cn：数据集构建。

- sets_up_cn：为公正测试模型泛化打基础。

- evidence_pointer：Fine-Tuning and Evaluation Data section

### 41. Fine-Tuning Data P3 S1–S2

- order：41

- section：Development of AI Models

- locator：Fine-Tuning Data P3 S1–S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：另从八篇文章中收集858对项目-定义对，其中467对经Prolific参与者执行H&T评分，用于微调分布模型。

- rhetorical_function_cn：说明人类数据集的来源与用途。

- depends_on_cn：分布模型需要人类评分标签。

- sets_up_cn：Study 2中的人机一致性检验数据。

- evidence_pointer：Fine-Tuning and Evaluation Data section

### 42. Modeling Procedure P1 S1

- order：42

- section：Development of AI Models

- locator：Modeling Procedure P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对15个分类器进行超参数网格搜索，用验证集AUC选择最优微调参数。

- rhetorical_function_cn：展示分类器选择的系统性。

- depends_on_cn：训练/验证集。

- sets_up_cn：Table 2结果。

- evidence_pointer：Modeling Procedure section

### 43. Modeling Procedure P2 S1

- order：43

- section：Development of AI Models

- locator：Modeling Procedure P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对13个分布模型进行微调，使用量化、固定随机种子与高效推理库，以保证可复现性并降低硬件需求。

- rhetorical_function_cn：强调可复现工程细节。

- depends_on_cn：人类评分数据。

- sets_up_cn：模型比较与选择。

- evidence_pointer：Modeling Procedure section

### 44. Model Evaluation P1 S1–S2

- order：44

- section：Development of AI Models

- locator：Model Evaluation P1 S1–S2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：采用ROC AUC、macro F1和预期校准误差（ECE）三个指标评价模型，分别衡量判别能力、分类质量与概率校准。

- rhetorical_function_cn：定义评价标准。

- depends_on_cn：测试集。

- sets_up_cn：为Table 2和后续模型选择提供指标。

- evidence_pointer：Model Evaluation section

### 45. Model Evaluation P2 S1–S2

- order：45

- section：Development of AI Models

- locator：Model Evaluation P2 S1–S2

- move_code：RESULT

- paraphrase_cn：Table 2显示最佳分类器DeBERTa-v3-large与最佳开放/闭源分布模型性能相近，仅相差几个百分点。

- rhetorical_function_cn：给出benchmark结果的关键对比。

- depends_on_cn：前述评价指标与模型训练。

- sets_up_cn：决定后续RATER_C/RATER_D选择。

- evidence_pointer：Table 2

### 46. Model Evaluation P3 S1–S2

- order：46

- section：Development of AI Models

- locator：Model Evaluation P3 S1–S2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：微调普遍提升AUC但ECE变差，后者可归因于真实人类评分者的校准分布。

- rhetorical_function_cn：解释微调效果不完美之处，提示校准边界。

- depends_on_cn：Table 3微调delta。

- sets_up_cn：为RATER_C更低的ECE/更高效率提供转折。

- evidence_pointer：Table 3

### 47. Model Evaluation P4 S1–S2

- order：47

- section：Development of AI Models

- locator：Model Evaluation P4 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：分类器整体更优且计算效率高（deberta-v3-large参数少于0.5B），因此后续实验采用RATER_C；但两类模型互补，系统同时提供RATER_D并模块化可替换。

- rhetorical_function_cn：解释为什么选择RATER_C作为核心，并保留双模型设计。

- depends_on_cn：benchmark结果。

- sets_up_cn：Web界面功能与后续六项研究。

- evidence_pointer：Model Evaluation section

### 48. Web Interface P1 S1

- order：48

- section：Development of AI Models

- locator：Web Interface P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：开发RATER网页系统提供RATER_C/RATER_D访问，并模块化支持其他模型，开放源码与Kaggle竞赛。

- rhetorical_function_cn：描述系统的可访问性与扩展性。

- depends_on_cn：模型训练完成。

- sets_up_cn：后续用户可通过平台使用工具。

- evidence_pointer：Web Interface section

### 49. Eval intro S1

- order：49

- section：Evaluation of the RATER System

- locator：Eval intro S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在初步定量验证后，作者进行六项汇总性准则效度研究，检验RATER_C在内容效度任务上的表现。

- rhetorical_function_cn：交代后续评价结构与目的。

- depends_on_cn：模型选择。

- sets_up_cn：逐一展开Study 1-6。

- evidence_pointer：Evaluation of the RATER System section

### 50. Study 1 intro S1–S2

- order：50

- section：Study 1

- locator：Study 1 intro S1–S2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：任何新内容效度程序至少应能区分意图项目-构念对与非意图项目-构念对；作者据此宣称RATER_C满足该要求。

- rhetorical_function_cn：说明Study 1检验的最基本主张。

- depends_on_cn：内容效度理论。

- sets_up_cn：为t检验和混淆矩阵提供假设。

- evidence_pointer：Study 1 section

### 51. Study 1 results S1–S3

- order：51

- section：Study 1

- locator：Study 1 results S1–S3

- move_code：RESULT

- paraphrase_cn：意图对平均0.63显著高于非意图对0.097（p<0.001），决策规则下准确率92%，F1=0.78，kappa=0.73。

- rhetorical_function_cn：用统计结果支持区分能力。

- depends_on_cn：858对数据与RATER_C得分。

- sets_up_cn：建立第一层准则效度。

- evidence_pointer：Study 1 section, Table 4

### 52. Study 2 intro S1–S3

- order：52

- section：Study 2

- locator：Study 2 intro S1–S3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：新工具应与当前最佳人工准则H&T一致或更好，因此RATER_C分数应显著预测人类H&T评分。

- rhetorical_function_cn：提出Study 2的可检验主张。

- depends_on_cn：H&T作为黄金标准。

- sets_up_cn：线性混合模型检验。

- evidence_pointer：Study 2 section

### 53. Study 2 results S1–S3

- order：53

- section：Study 2

- locator：Study 2 results S1–S3

- move_code：RESULT

- paraphrase_cn：线性混合模型显示RATER_C显著预测H&T评分（F=364.91, p<0.001, marginal R²=0.43），人机判定一致88%，F1=0.82，kappa=0.73。

- rhetorical_function_cn：报告与人类判断一致性的主要证据。

- depends_on_cn：467对数据、408名评分者。

- sets_up_cn：与作者标注结果互相印证。

- evidence_pointer：Study 2 section, Table 5

### 54. After Study 2 S1

- order：54

- section：Study 1-2 transition

- locator：After Study 2 S1

- move_code：TRANSITION

- paraphrase_cn：研究1和2分别基于真实世界结果检验了模型，因此提供准则效度与生态效度。

- rhetorical_function_cn：总结前两研究意义，引出下一阶段。

- depends_on_cn：Study 1和2。

- sets_up_cn：进入与研究现有工具的比较。

- evidence_pointer：Evaluation section after Study 2

### 55. Study 3 results S1

- order：55

- section：Study 3

- locator：Study 3 results S1

- move_code：RESULT

- paraphrase_cn：在3,303对子集上RATER_C的AUC、macro F1和ECE均优于BRASS Bot。

- rhetorical_function_cn：提供与现有计算系统的相对优势证据。

- depends_on_cn：相同输入设置与代表性抽样。

- sets_up_cn：进一步支撑RATER不仅与人一致而且优于通用系统。

- evidence_pointer：Study 3 section, Table 6

### 56. Study 4 threshold S1–S2

- order：56

- section：Study 4

- locator：Study 4 threshold S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者基于测试集均值提出对应性阈值≥0.620和非意图区分阈值≤0.062，即“62启发式”，并强调其为模型特定说明性指导。

- rhetorical_function_cn：把模型分数转化为可用的决策规则。

- depends_on_cn：holdout均值分布。

- sets_up_cn：Web界面默认阈值与用户自定义支持。

- evidence_pointer：Study 4 section

### 57. Study 5 representativeness S1–S3

- order：57

- section：Study 5

- locator：Study 5 representativeness S1–S3

- move_code：RESULT

- paraphrase_cn：通过softmax归一化RATER_C分数，示例三项目量表显示benevolence仅占5%，未达代表性，而MacKenzie等人数字显示三维度约各占三分之一。

- rhetorical_function_cn：演示代表性计算方法的可行性与差异。

- depends_on_cn：Kerlinger/ MacKenzie代表性理论。

- sets_up_cn：补足内容效度三标准的计算化缺口。

- evidence_pointer：Study 5 section, Table 7

### 58. Study 6 results S1–S2

- order：58

- section：Study 6

- locator：Study 6 results S1–S2

- move_code：RESULT

- paraphrase_cn：7名外部专家给出易用性6.6、有用性5.7、使用意向5.3；定性反馈显示多数人此前未做内容验证，且部分担心不理解底层分析。

- rhetorical_function_cn：报告适用性检查的定量与定性结果。

- depends_on_cn：培训与至少一周使用。

- sets_up_cn：引出界面改进与公开平台承诺。

- evidence_pointer：Study 6 section

### 59. Trust Scale Example P1 S1–S3

- order：59

- section：Illustration

- locator：Trust Scale Example P1 S1–S3

- move_code：RESULT

- paraphrase_cn：独立团队使用RATER_C与H&T同时评估6个信任量表的56个项目，两方法总体一致，但存在个别分歧。

- rhetorical_function_cn：展示外部真实项目中的比较。

- depends_on_cn：Vitari等团队的独立使用承诺。

- sets_up_cn：进入具体差异分析。

- evidence_pointer：Illustration section, Table 8

### 60. Trust Scale T4 example

- order：60

- section：Illustration

- locator：Trust Scale T4 example

- move_code：RESULT

- paraphrase_cn：对于项目T4，H&T认为其匹配目标构念，而RATER_C认为不符合62阈值，两者结论不同。

- rhetorical_function_cn：显示RATER_C能发现H&T可能高估的对应性。

- depends_on_cn：Table 8数据。

- sets_up_cn：论证RATER提供互补洞察。

- evidence_pointer：Table 8

### 61. Further Examination P1–P2

- order：61

- section：Illustration

- locator：Further Examination P1–P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者删除“and communicate”后RATER分数上升，但提醒宽泛声明可能造成语义渗漏；建议按Leventhal子维度写新项目。

- rhetorical_function_cn：演示RATER在迭代改写中的支持作用。

- depends_on_cn：对IT程序公平构念的理论梳理。

- sets_up_cn：引导用户进行理论驱动的项目修订。

- evidence_pointer：Further Examination paragraphs

### 62. Expert Scores P1 S1–S2

- order：62

- section：Illustration

- locator：Expert Scores P1 S1–S2

- move_code：RESULT

- paraphrase_cn：5名专家对5个信任项目排序；RATER_C与专家排序相关0.97，而H&T与专家排序仅0.03。

- rhetorical_function_cn：为RATER_C较H&T在某些情况下更贴近专家判断提供直接证据。

- depends_on_cn：专家排序数据。

- sets_up_cn：讨论H&T可能受上下文影响的局限。

- evidence_pointer：Table 9

### 63. Discussion P1 S1–S2

- order：63

- section：Discussion

- locator：Discussion P1 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：本文提出新的计算技术评估内容效度，填补了量表开发计算工具文献中对这一核心过程的关注空白，提供开源、可复制、可靠、领域无关、专门且免费的工具。

- rhetorical_function_cn：重新串联引言缺口并宣布总体贡献。

- depends_on_cn：全文证据。

- sets_up_cn：逐项展开五点贡献。

- evidence_pointer：Discussion section

### 64. Contributions P1 S1–S5

- order：64

- section：Discussion

- locator：Contributions P1 S1–S5

- move_code：CONTRIBUTION

- paraphrase_cn：五项贡献：领域无关模型优于专用调优和通用系统；大规模benchmark数据集与方法；首个多维代表性计算途径；适用性检查证明现实准备度；开源透明可复制平台。

- rhetorical_function_cn：系统打包贡献点。

- depends_on_cn：讨论开头的总体概括。

- sets_up_cn：为Implications提供支撑。

- evidence_pointer：Contributions to the Literature section

### 65. Limitations P1 S1–S2

- order：65

- section：Limitations

- locator：Limitations P1 S1–S2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：模型对复杂语法和句法敏感；Flesch可读性显著预测正确性，RATER增加低可读性警告，操作化MacKenzie建议。

- rhetorical_function_cn：识别并缓解边界条件的限制。

- depends_on_cn：33,304实例的可读性分析。

- sets_up_cn：引出未来工作（单维代表性、模型更新）。

- evidence_pointer：Limitations and Future Work section

### 66. Conclusion P1 S1–S3

- order：66

- section：Conclusion

- locator：Conclusion P1 S1–S3

- move_code：CONTRIBUTION

- paraphrase_cn：RATER_C/RATER_D被开发用于评估对应性、区分性和代表性，并免费公开，预期提高内容验证的执行频率与量表质量。

- rhetorical_function_cn：以简洁的行动呼吁收束全文。

- depends_on_cn：所有研究证据。

- sets_up_cn：给读者留下工具可立即使用和未来AI辅助方法发展的印象。

- evidence_pointer：Conclusion section

## 写作技术

- gap_construction_cn：先强调内容验证的关键性，再以低执行率统计数据说明缺口，随后逐一列出成本、认知、资源、可复制性等障碍，把缺口建构为实践与方法的双重缺陷，然后引入AI作为可能的解决方式。

- signposting_cn：引言在首段即声明开发系统；发展与评价部分使用“我们评估了…”“我们测试了…”“六项研究”等路标；每节以问题式小标题出现；Discussion逐条列出五点贡献并冠以“First/Second…”

- transition_logic_cn：从概念背景到设计需求使用表1的挑战—需求映射；从模型建设到评价用“Having conducted…”，从Study 1到2用“Although…”, 从2到3用“As they successfully…”，从评价到使用案例用“In this section, we illustrate…”

- claim_evidence_rhythm_cn：每个关键主张后面紧跟统计检验/表格/案例；例如先声明RATER_C满足区分要求，再用t检验与Table 4支持；先声明与人类一致，再用LMM和Table 5支持。

- benchmark_narrative_cn：将benchmark本身作为研究贡献之一，不只作为方法；开放测试集与Kaggle竞赛邀请未来模型超越，使性能主张具有时间性与可证伪性。

- theory_return_cn：结果不仅报告性能，而且用理论概念解释：用对应性/区分性/代表性术语重述模型输出；用Kerlinger/MacKenzie代表性理论解释softmax；用语义解析类比解释为什么LLM能完成该任务。

- contribution_positioning_cn：五点贡献分别对应：模型性能/领域无关、大规模评价数据、代表性缺口、真实场景适用性、开源透明属性；每一点都围绕引言缺口中的某一障碍展开。

- novelty_protection_cn：发布开源权重、公开测试集和Kaggle竞赛，将“当前性能”开放给未来超越，因此贡献不绑定于某个特定模型；同时强调模块化设计可接入新模型。这样即使模型被超越，基准和平台依然是稳定的设计贡献。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：指出一个方法论环节尽管关键却被实践者回避（如内容验证），并用证据说明回避的代价。

- research_job_cn：找到行为研究/IS中一个由成本/技能阻碍的重要评估步骤。

- required_evidence_cn：至少一个领域的执行率数据或成本/资源障碍描述。

- transition_to_next_cn：由此引出“如果该步骤可自动化会怎样”的问题。

#### 2. 2

- step：2

- writing_job_cn：将该评估步骤拆解为可操作的标准（如correspondence/distinctiveness/representativeness）。

- research_job_cn：从目标学科方法论文献中提取规范标准及其操作化定义。

- required_evidence_cn：标准的确切定义及保留/拒绝规则。

- transition_to_next_cn：指出这些标准产生可计算任务。

#### 3. 3

- step：3

- writing_job_cn：将标准转换为计算需求，用表列出挑战→需求。

- research_job_cn：识别哪些标准可转化为监督学习或生成任务；确定输出格式。

- required_evidence_cn：每条需求至少有一个对应的传统人工流程可参照。

- transition_to_next_cn：进入数据/模型构建。

#### 4. 4

- step：4

- writing_job_cn：描述大规模训练/评价数据来源和切分策略。

- research_job_cn：从公开语料/论文中构建配对数据；用文章级划分避免泄漏；若需要人类标签，招募评分者。

- required_evidence_cn：数据量、标签来源和类不平衡的说明。

- transition_to_next_cn：说明为什么这种数据能支撑领域无关性。

#### 5. 5

- step：5

- writing_job_cn：报告多架构微调与benchmark，含多个指标（AUC/F1/校准误差）。

- research_job_cn：对多个基础模型做超参数搜索，比较微调前/后。

- required_evidence_cn：至少一个模型的性能表现与计算成本权衡。

- transition_to_next_cn：选择主模型进入需要多准则效度研究。

#### 6. 6

- step：6

- writing_job_cn：在训练后语料/作者标签上做第一层准则效度。

- research_job_cn：找到一个未参与训练的外部标签源（如后续文章作者意图）。

- required_evidence_cn：与基准机会有显著差异并报告混淆矩阵/kappa。

- transition_to_next_cn：作者标签可能主观，需要人类独立判断。

#### 7. 7

- step：7

- writing_job_cn：与人类评分者一致性检验。

- research_job_cn：采集人类数据（如H&T）；用混合模型检验预测力；报告人机一致率。

- required_evidence_cn：显著回归效应和一致性统计。

- transition_to_next_cn：与人类一致不等于优于其他计算系统。

#### 8. 8

- step：8

- writing_job_cn：与现有计算工具/基线对比。

- research_job_cn：选取一个可复现的现有系统并在相同子集做基准。

- required_evidence_cn：性能对比表，至少一个度量占优。

- transition_to_next_cn：性能优势还需用户可解释。

#### 9. 9

- step：9

- writing_job_cn：提供分数解释启发式（阈值/标准化）。

- research_job_cn：对输出分布做统计描述，设计平衡Type I/II错误的指导规则。

- required_evidence_cn：阈值来源与模型特定性说明。

- transition_to_next_cn：对应性/区分性之外还有代表性。

#### 10. 10

- step：10

- writing_job_cn：展示对缺失标准（如代表性）的计算化扩展。

- research_job_cn：找到该标准的原理性定义，设计聚合函数（如softmax），并在经典示例上演示。

- required_evidence_cn：与已有说明性数据对照; 明确适用范围。

- transition_to_next_cn：系统仅发布还不足以证明可用。

#### 11. 11

- step：11

- writing_job_cn：进行适用性检查/用户研究。

- research_job_cn：培训外部专家并使用TAM-style问卷收集定量+定性反馈。

- required_evidence_cn：至少8-10名目标用户（文中7名）和可用性/有用性均值。

- transition_to_next_cn：最终通过外部真实案例展示。

#### 12. 12

- step：12

- writing_job_cn：发布开源系统和benchmark，邀请超越。

- research_job_cn：提供公开URL、GitHub、模型权重、竞赛/测试集。

- required_evidence_cn：系统可访问性和再造性说明。

- transition_to_next_cn：进入讨论和限制。

### most_transferable_moves_cn

1. 以文章级划分构造大规模配对语料并公开测试集，防止数据泄漏并建立benchmark

2. 将理论标准（对应性、区分性、代表性）直接映射为模型输出类型与评价指标

3. 用多个互补研究逐层升级外部准则：作者标签→人类评分→现有工具→专家用户→独立现场案例

4. 用启发式阈值（如62）和softmax聚合将黑盒输出转化为研究者可操作的设计知识

5. 开放源码、开放权重、邀请超越，把性能主张从一次性结果变为可延续的平台贡献

### resource_intensive_or_nonstandard_parts_cn

1. 需要访问2,443篇论文全文以构建大规模配对数据

2. 需要招募408名Prolific评分者执行H&T评级并支付相应成本

3. 需要大量GPU资源进行15+13个模型的微调与推理评估

4. 需要外部专家团队参与培训与适用性检查

5. 需要独立的、愿意公开分享数据的第三方研究团队（如Vitari等）提供真实使用案例

### what_not_to_copy_superficially_cn

1. 不能在没有跨学科大规模训练数据的情况下宣称“领域无关”

2. 不能把“62启发式”作为通用阈值搬运到其他模型/领域，必须基于模型输出分布重新估计

3. 不能把softmax代表性方法推广到单维构念，文章只演示了多维构念

4. 不能把5个项目的专家排序相关0.97当作稳健结论，需要更大的专家样本

5. 不能只搭建网页而不提供模型权重/测试集/随机种子等复现材料，否则透明与可复制承诺会落空

- single_best_description_of_the_routine_cn：把心理学量表开发中被忽略的内容效度三重标准翻译为两个监督学习模型，并用从作者标签到人类评分者再到外部专家案例的阶梯式效度检验，最终以一个开源平台和benchmark固定住贡献。

## 分析边界

全文OCR基本完整，但Figure 1为图片无法解析具体界面细节；表2/3/4/5/6/7/9等表格以文本形式可用；未提供OSF/GitHub等线上补充材料详情；文章为MIS Quarterly接受版本，无页码和线上附录；部分段落位置只能以小节和段落编号定位，无法提供精确页码。
