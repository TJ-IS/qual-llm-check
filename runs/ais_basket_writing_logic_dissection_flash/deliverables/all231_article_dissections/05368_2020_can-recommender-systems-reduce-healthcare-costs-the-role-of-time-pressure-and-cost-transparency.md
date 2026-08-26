# Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice

- 作者：Lina Bouayad; Balaji Padmanabhan; Kaushal Chari
- 年份 / 期刊：2020 / MIS Quarterly
- DOI：10.25300/misq/2020/14435
- 源文件：05368_2020_can-recommender-systems-reduce-healthcare-costs-the-role-of-time-pressure-and-cost-transparency.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.93

## 文章级论证概况

- 核心问题：在医疗处方场景下，成本感知的推荐系统能否促使执业医生、执业护士和医师助理选择更便宜但疗效相同的药物？成本框架（仅低成本 vs 混合成本）和时间压力如何影响推荐系统的查看与采纳，且这种影响是否因从业者类型而异？

- 制品与设计：作者构建了一个临床推荐系统原型，在处方时针对医生先选定的治疗方案动态提供疗效或安全性相近的、同药物类别内的替代药物，并显示患者自付成本信息。系统有两种设计设置：low-cost design（所有推荐都比初始选择便宜）和 mixed-cost design（推荐中既有更便宜也有更贵的选项）。时间压力通过队列消息+倒计时器（医师实验）或竞争性绩效排名提示（NP/PA实验）操作化。

- 客观结果：医师实验中，32名真实医生在192个病例水平观察中，147次查看推荐，其中95次调整处方；GEE和Heckman模型显示成本框架显著影响处方调整，混合成本框架降低调整率，而时间压力对医师查看和调整无显著影响。NP/PA实验中，120名真实从业者在120个病例水平观察中，114次查看推荐，其中79次调整；时间压力显著降低查看率，成本框架不显著，但NP/PA整体调整率高于医师，表现出更强的成本敏感性。

- 核心贡献：作者声称这是首项通过三个研究（两个受控实验和一个访谈）系统评估医疗推荐系统中成本透明对处方选择影响的研究，共使用160名真实执业医疗人员。理论贡献在于将适应水平理论/参考价格效应扩展到医疗向他人决策情境，并识别了从业者类型（医师 vs NP/PA）作为成本框架和时间压力效果的边界条件。设计知识贡献在于指出成本感知推荐系统的有效性取决于信息展示方式和用户群体，设计需要适应从业者类型。

- 整篇论证链：论文从美国医疗费用和处方药成本的高昂现实出发，指出现有EMR系统不显示准确成本，而医生普遍缺乏药价知识且早期成本显示干预效果有限，因此提出利用推荐系统在处方时刻呈现等效低成本替代药物以降低医疗成本的可能性。基于适应水平理论和参考价格效应，作者论证两种成本框架设计（仅低成本 vs 混合成本）会导致不同的参考价格锚定，进而影响推荐采纳；基于时间压力文献，论证高时间压力会让从业者过滤信息并可能忽略推荐。为了验证这些机制，作者首先设计了经过两位医学专家验证的六份临床病历和动态成本操纵的推荐系统原型，然后对32名真实医生进行受控实验，发现成本框架显著影响医生调整处方（混合成本框架减弱调整），但时间压力无显著影响；随后访谈10名不同专科医生，确认实际缺乏成本信息且医生认为时间压力下仍愿意使用有用且易用的推荐系统；最后对120名NP/PA开展受控实验，发现时间压力显著降低他们对推荐的查看，而成本框架不显著，且整体推荐采纳率高于医师。综合这些结果，作者在讨论中回到适应水平理论，将医生对成本框架的敏感性解释为参考价格效应在代理决策情境中的表现，将NP/PA的时间压力敏感性归因于训练和收入差异，并给出适应从业者类型的推荐系统设计建议及潜在的经济节约估算。

## 类型与写作弧线判定

- 论文主类型判定：论文虽然包含设计科学元素（构建推荐系统原型），但其核心逻辑是从适应水平理论、参考价格效应和时间压力理论推导出两种设计差异（low vs mixed cost、高 vs 低时间压力），并通过两个受控实验和一项访谈来检验这些理论衍生命题。研究者并非先根据实践经验提出设计原则再评估，而是预先从理论机制推导出设计变量，并将其作为实验处理直接检验，因此属于理论衍生制品并通过实验检验。

- 主导写作弧线判定：论文结构遵循着：提出医疗成本问题（problem）→ 引入适应水平理论和时间压力文献（theory）→ 推导推荐系统设计变量和实验设计（design）→ 通过三个研究检验（test）→ 在讨论中返回理论解释结果并提炼设计知识（return）。这一弧线贯穿全文，尤其是讨论部分重新连接引言中的缺口，用参考价格效应和用户类型差异解释实验结果，并宣称理论和实践贡献。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：阶段1构建实验材料与推荐系统原型，为后续两个受控实验提供共同基础；阶段2是医师受控实验，建立成本框架对处方调整的因果影响；阶段3是医师访谈，补充外部效度并验证实践假设与设计需求；阶段4是NP/PA受控实验，扩展用户群体并显示时间压力影响的异质性。阶段2与阶段4共享相同的推荐系统设计但操作化细节不同，阶段3介于两者之间提供定性解释和过渡。

### studies_or_phases

#### 1. 实验材料与推荐系统原型构建

- order：1

- name_cn：实验材料与推荐系统原型构建

- question_cn：如何创建真实、临床可信且能操纵成本框架和时间压力的实验环境？

- inputs_and_setting_cn：与两位医疗从业者合作开发六份虚构但符合医学协议的病历；每份病历包含患者一般信息、保险、生命体征、既往史、SOAP病历等，治疗方案留待参与者填写；替代药物列表按药物类别和活性成分组织，由专家确认疗效和副作用相似性。

- designed_or_compared_object_cn：推荐系统界面和动态成本操纵方案：low-cost组推荐均低于初始选择；mixed-cost组推荐中有一个高于、一个低于初始选择。时间压力操作化工具（队列消息+计时器）也在这一阶段设计。

- baseline_control_or_counterfactual_cn：low-cost设计与mixed-cost设计互为对照；医师实验中另设控制组验证时间压力操纵。

##### objective_metrics

（空）

- analysis_method_cn：专家审查和迭代设计；后续通过操纵检验问卷和完成时间统计验证材料有效性。

- main_result_cn：六份病历被专家评定为相似复杂度和风险水平，适合所有专科和执业类型；替代药物被确定具有相似疗效和副作用，主要差异在于成本。

- argumentative_role_cn：为实验提供具有生态效度的刺激材料，确保推荐差异仅体现在成本维度，从而干净地检验成本框架效应。

- remaining_uncertainty_cn：病历数量有限且集中于初级保健，可能限制推广性；专家主观判断可能不完全代表所有从业者的认知。

- link_to_next_phase_cn：该原型和病历直接用于阶段2的医师受控实验，并在阶段4中复用（缩减为三份病历）。

##### evidence_pointers

1. Study One, Experimental Design section

2. Appendix B six cases

3. Appendix E expert reports

#### 2. Study One：医师受控实验

- order：2

- name_cn：Study One：医师受控实验

- question_cn：对执业医师来说，推荐系统的成本框架（low vs mixed）和时间压力是否影响他们对推荐的查看和处方调整？

- inputs_and_setting_cn：32名来自佛罗里达州的实际执业医师，其中大多数具有多年经验；每个医生完成6份病历，产生192个case-level观察；实验通过Qualtrics在线进行。

- designed_or_compared_object_cn：成本框架（低成本和混合成本）作为组间变量；时间压力作为组内变量（每个医生有3个高压力案例和3个低压力案例），采用平衡设计。

- baseline_control_or_counterfactual_cn：低成本组 vs 混合成本组；时间压力高低对照；额外招募8名医生作为无时间压力的控制组用于操纵检验。

##### objective_metrics

1. view：查看系统推荐的次数/比例

2. adjust：改变初始治疗计划为推荐方案的比例

- analysis_method_cn：广义估计方程（GEE）处理重复测量；Heckman两阶段模型处理查看与调整之间的选择内生性；操纵检验采用问卷和完成时间阈值；稳健性检验通过删除第一个或最后一个病例重新建模。

- main_result_cn：参与者查看了192例中的147例，并在查看过的147例中调整了95例；GEE和Heckman模型均显示：成本框架对调整有显著负效应（混合成本比低成本调整率更低），时间压力对查看无显著效应。

- argumentative_role_cn：确立了成本框架在医师中的因果影响，证明即使专家也会受参考价格效应影响；同时意外发现时间压力对医师无效用，为后续NP/PA研究提供了对比点。

- remaining_uncertainty_cn：8名医师/组的小样本；时间压力的操作化可能不够强；未直接测量参考价格；可能存在学习效应或疲劳效应（虽经稳健性检验）；结果可能受医生已有成本敏感性影响。

- link_to_next_phase_cn：由于实验结果需要解释调查对象们在真实实践中的感知，以及医生为何不受时间压力影响，作者转入访谈研究（阶段3）以增强外部效度和理解机制。

##### evidence_pointers

1. Study One, Experimental Design section

2. Study One, Subjects and Data Description

3. Study One, Experiment Results, Table 2 and Table 3

4. Study One, Robustness Checks, Table 4

#### 3. Study Two：医师事后访谈

- order：3

- name_cn：Study Two：医师事后访谈

- question_cn：真实临床实践中，医生是否有成本信息获取权？他们如何看待成本和时间压力？对成本敏感推荐系统的意向使用特征是什么？

- inputs_and_setting_cn：10名不同专科的执业医生（肾病科、内科学、急诊、老年病、妇产科、新生儿科、儿科、心脏病学），另有4名用于预测试；半结构化电话访谈，每次30-50分钟，录音转写。

- designed_or_compared_object_cn：访谈指南（protocol guide approach）覆盖成本重要性、成本信息可及性、时间压力、推荐系统使用意向等主题；对引出指标进行迭代提炼和主题编码。

- baseline_control_or_counterfactual_cn：访谈结果与实验发现相互印证：医生普遍无法获取准确成本；高时间压力下报告更依赖系统而非减少使用；这为实验中的时间压力无效结果提供解释。

##### objective_metrics

1. 定性指标：成本意识、成本信息获取障碍、时间压力诱因、推荐系统功能需求

- analysis_method_cn：内容分析：三位作者独立提取关键指标，再映射到成本和时间压力主题；通过共识度（低/中/高支持水平）汇总。

- main_result_cn：医生认为成本重要且影响依从性，但缺乏准确、自动化的成本信息；时间压力普遍存在且有多种诱因；医生在时间压力下会更依赖EMR的提示和模板；期望推荐系统提供疗效/安全性对比、循证证据和省时体验。

- argumentative_role_cn：为实验发现的现实相关性提供定性质证；解释了医生为何在时间压力下仍可能使用推荐系统（有用性优先）；并产出关于系统特征的设计启示。

- remaining_uncertainty_cn：访谈为意向性报告而非真实行为；样本小；难以对假设性系统给出确定性使用承诺。

- link_to_next_phase_cn：访谈确认了医生与NP/PA在训练和执业环境上的差异，自然过渡到阶段4研究NP/PA的推荐系统使用行为。

##### evidence_pointers

1. Study Two, Subjects and Methods

2. Study Two, Qualitative Results

3. Appendix C interview questionnaire

4. Appendix D interview result tables

#### 4. Study Three：NP/PA受控实验

- order：4

- name_cn：Study Three：NP/PA受控实验

- question_cn：执业护士和医师助理在成本框架和时间压力下的推荐查看与处方调整行为是否不同于医师？

- inputs_and_setting_cn：120名具有处方权的执业护士（88%）和医师助理，通过Qualtrics招募；实验包含3份病历（其中两份要求摘要病例以验证认真性），成本框架和时间压力均设计为组间变量。时间压力通过“A+ Star Performer”等绩效排名提示操作化，强度高于医师实验。

- designed_or_compared_object_cn：沿用医师实验的推荐系统和成本动态操纵，但将参与者的任务从六份病历缩减为三份，并在高时间压力组加入竞争性基准信息；成本框架仍为low vs mixed。

- baseline_control_or_counterfactual_cn：低成本组 vs 混合成本组；高时间压力组 vs 低时间压力组；使用2×2完全组间设计；操纵检验通过完成时间均值和标准差筛选。

##### objective_metrics

1. view：是否查看系统推荐

2. adjust：是否调整初始治疗方案

- analysis_method_cn：Logistic回归（模型1控制变量，模型2加入预测变量）和Heckman两阶段模型；通过病例摘要质量、完成时间和重复完成检查进行数据质量筛选。

- main_result_cn：114/120查看推荐，79/114调整处方；时间压力显著降低查看率（高时间压力组查看率0.90 vs 低时间压力组1.00），成本框架对调整无显著效应；与医师相比，NP/PA整体调整倾向更高，且不受混合成本框架的抑制作用影响。

- argumentative_role_cn：扩展了研究结论的普适性，显示从业者类型作为重要的调节变量；对时间压力的敏感性差异解释了为何推荐系统设计需要针对用户群体定制；同时提供更大的样本（120）增强统计效力，弥补医师实验样本小的弱点。

- remaining_uncertainty_cn：实验只包含一个用于处方决策的病例，可能降低决策生态效度；Qualtrics第三方招募可能引入数据质量噪音；时间压力操作化与医师实验不同，可能混淆方法差异与群体差异。

- link_to_next_phase_cn：阶段4的结果直接为讨论部分的理论回返和设计建议提供证据基础，尤其是解释医师与NP/PA对参考价格和时间压力的不同反应。

##### evidence_pointers

1. Study Three, Experimental Design

2. Study Three, Subjects

3. Study Three, Experiment Results, Table 7 and Table 8

4. Study Three, Manipulation Checks

## 各部分修辞架构

### abstract_moves

1. STUDY_OVERVIEW: 声明论文综合三项研究（两个受控实验+一个访谈）

2. METHOD_JUSTIFICATION: 强调所有被试均为真实执业医疗人员

3. RESULT: 报告总体发现：提供成本信息时普遍倾向选择低成本药物

4. RESULT: 报告时间压力对NP/PA的影响大于医师

5. CONTRIBUTION: 指出对成本降低和实时医疗推荐系统设计的启示

### introduction_moves

1. CONTEXT: 美国医疗花费达3.2万亿美元，处方药占3246亿

2. PRIOR_KNOWLEDGE: 通用名药替代和三层保险计划可降低成本

3. PHENOMENON: 处方决策者通常不知道具体药物成本

4. LIMITATION: EMR未集成成本信息，早期价格显示尝试遇到障碍

5. GAP: 尚无研究评估推荐系统用于降低医疗成本

6. DESIGN_FEATURE: 提出mixed-cost system design并解释其现实性和合理性

7. THEORY_INTRO: 引入适应水平理论和参考价格效应

8. MECHANISM: 从业者形成内部参考价格并以之锚定其他价格

9. GAP: 首次研究医疗推荐系统设计对成本有效选项采纳的影响

10. PRACTICAL_STAKES: 若混合成本设计阻碍转向低价选项则推荐系统无法降成本

11. RQ_OR_OBJECTIVE: 提出三个研究目标：成本框架、时间压力、从业者类型调节

12. CONTRIBUTION: 预告实验+访谈的贡献、理论机会和首次性宣称

### theory_and_knowledge_moves

1. CONTEXT: 医生普遍认识成本重要性（引用调查）

2. LIMITATION: 早期计算机化价格比较模块未产生显著成本变化

3. GAP: 需在同药物类别内研究品牌替代，并纳入NP/PA

4. THEORY_PROPOSITION: 适应水平理论中的刺激、适应水平和反应梯度

5. MECHANISM: 从业者以推荐成本为上下文刺激形成参考价格

6. REQUIREMENT: low-cost design触发低于初始选择的参考价格，从而促进更换

7. MECHANISM: 社会规范效应作为补充机制

8. REQUIREMENT: mixed-cost design因患者便捷性和依从性考虑而必要

9. BOUNDARY_CONDITION: 临床专家不会仅用价格推断质量

10. MECHANISM: 高成本推荐作为锚点提高参考价格，降低低成本推荐采纳

11. HYPOTHESIS_OR_PROPOSITION: NP/PA收入更低、咨询时间更长，可能更价格敏感且形成更低参考价格

12. MECHANISM: 时间压力导致过滤消息和采用启发式/默认选项

13. MECHANISM: 培训差异造成医师与NP/PA对时间压力的不同反应

14. MECHANISM: 为他人决策时决策者会查看更多替代和信息，减少偏见

### artifact_design_moves

1. STUDY_OVERVIEW: 核心设计为成本敏感推荐系统，呈现同等疗效的药物选项和精确成本

2. DESIGN_FEATURE: low-cost setting vs mixed-cost setting的定义与预期效应

3. METHOD_JUSTIFICATION: 六份病历经专家合作创建，复杂度相似，条件常见于初级保健

4. DESIGN_FEATURE: 药物替代限于同药物类别，确保副作用和疗效大体相似，差异只在成本

5. METHOD_JUSTIFICATION: 2×2混合设计（成本组间、时间压力组内）及平衡顺序

6. DESIGN_FEATURE: 时间压力通过队列消息和每页计时器操作化

7. DESIGN_FEATURE: 成本信息动态操纵，组间成本差50-100美元，推荐列表随机顺序

8. METHOD_JUSTIFICATION: 在线Qualtrics实验支持动态分配

9. DESIGN_FEATURE: NP/PA实验缩减为三例，采用绩效基准排名操作化更强时间压力

10. METHOD_JUSTIFICATION: 通过病例摘要质量和完成时间筛选数据质量

### evaluation_moves

1. METHOD_JUSTIFICATION: 使用GEE处理重复测量

2. METHOD_JUSTIFICATION: 使用Heckman两阶段模型处理查看-调整的内生性

3. BENCHMARK_OR_CONTRAST: low-cost组作为mixed-cost组的对照

4. MANIPULATION_CHECK: 通过问卷确认参与者是否注意到成本信息，未注意到则替换

5. MANIPULATION_CHECK: 用额外控制组和时间阈值验证时间压力操作

6. RESULT: 总体查看和调整率统计

7. RESULT: GEE模型显示成本框架显著、时间压力不显著

8. RESULT: Heckman模型结果一致

9. ROBUSTNESS_OR_BOUNDARY_TEST: 删除第一个和最后一个病例重新建模，结果无本质变化

10. RESULT: NP/PA中时间压力显著、成本框架不显著

11. RESULT: NP/PA整体调整率高于医师

### discussion_and_contribution_moves

1. CONTRIBUTION: 推荐系统若设计得当可显著降低药品成本

2. PRACTICAL_STAKES: 基于Medicare Part D估算潜在节省2.02亿美元

3. RESULT: 访谈证实医生缺乏成本信息且缺乏成本关注

4. CONTRIBUTION: 理论贡献涉及成本框架和时间压力

5. THEORY_RETURN: 医师实验结果支持适应水平和参考价格命题

6. LIMITATION_AND_FUTURE: 提出关于差异原因的推测（知识差距、先前倾向）

7. DESIGN_KNOWLEDGE: 成本感知推荐系统需适应用户属性和经验

8. LIMITATION_AND_FUTURE: 承认样本、环境、未直接测量参考价格、缺少社会规范信息等局限

9. CONTRIBUTION: 从IS视角重申推荐系统作为变革人工物，效果依赖于信息和环境上下文

## 理论/知识到设计的翻译

### 知识/理论基础

1. 适应水平理论（Helson 1947）

2. 参考价格效应（Rajendran and Tellis 1994; Monroe 1973）

3. 时间压力与决策简化文献（Wright 1974; Hahn et al. 1992; Bobadilla-Suarez and Love 2018）

4. 为他人决策的决策行为文献（Polman 2012; Liu et al. 2018）

5. 医疗从业者成本知识调查（Reichert et al. 2000; Shrank et al. 2005）

- 理论—设计耦合：direct

- 耦合判定理由：理论不仅用于解释事后结果，而且在设计阶段就决定了两项核心处理：成本框架（low vs mixed）直接来自适应水平理论中参考价格形成的预测，时间压力操作化来自时间压力对信息处理的影响。理论命题和实验设计之间有清晰的前瞻性翻译链条，且实验直接检验这些命题。

- 理论到设计翻译链：适应水平理论认为个体根据所有刺激的对数加权平均形成适应水平，价格判断以内部参考价为锚。在医疗推荐情境中，医生缺乏药价知识，因此系统显示的成本信息成为上下文刺激，形成参考价格。若推荐全为低价，参考价格低于初始选择，则更可能调整到低价替代；若推荐为混合高低价，参考价格居中，初始选择若接近参考价则不太调整。时间压力文献认为高压力下决策者过滤信息和依赖启发式，因此高时间压力可能降低查看和调整。这些机制被转化为两个可操作的设计变量：推荐列表的成本构成（全部低价 vs 混合）和时间压力提示（倒计时/绩效排名）。实验则通过比较低成本组与混合成本组、高压力与低压力组来检验这些设计差异的效果。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：适应水平理论：个体对刺激的反应取决于刺激相对于适应水平的位置；接近适应水平的刺激不引发反应

- mechanism_cn：从业者以推荐列表中的成本为上下文刺激形成参考价格（适应水平），随后将初始选择成本与该参考价格比较

- design_requirement_cn：推荐系统应设计成能系统性地操纵参考价格的成本信息呈现方式

- artifact_choice_cn：low-cost design（所有推荐低于初始选择）与 mixed-cost design（推荐有高有低）

- evaluated_contrast_cn：低成本组 vs 混合成本组对处方调整率的影响

- objective_result_cn：医师实验中，混合成本组的调整率显著低于低成本组（GEE系数-2.03，p<0.05）；NP/PA实验中成本框架不显著

##### evidence_pointers

1. Study One, Table 3, Adjustment Models Model 2

2. Study Three, Table 8, Adjustment Models Model 2

#### 2. 2

- theory_or_knowledge_claim_cn：医生普遍缺乏药价知识，保险计划导致患者自付成本因患者而异

- mechanism_cn：缺乏内部价格记忆，使系统显示的成本成为参考价格的主要来源

- design_requirement_cn：推荐系统必须在处方时刻提供准确且个性化的成本信息，而不是依赖医生记忆

- artifact_choice_cn：系统根据患者保险计划和药物数据库动态计算患者自付成本并显示

- evaluated_contrast_cn：有无成本显示（隐式通过与既有EMR对比，访谈验证）

- objective_result_cn：访谈中医生普遍报告无准确成本信息，实验中的低成本推荐被大量采纳

##### evidence_pointers

1. Study Two, Cost Information Access

2. Study One, Overall view/adjust statistics

#### 3. 3

- theory_or_knowledge_claim_cn：时间压力导致决策者过滤信息、使用启发式或默认选项

- mechanism_cn：高时间压力下，从业者可能忽略推荐和成本信息，或采用默认治疗

- design_requirement_cn：系统设计必须考虑额外时间负担，并评估时间压力对推荐使用的影响

- artifact_choice_cn：实验操作：高时间压力组显示增加病例队列消息和计时器；NP/PA实验使用绩效排名提示

- evaluated_contrast_cn：高时间压力 vs 低时间压力对查看率和调整率的影响

- objective_result_cn：医师实验中时间压力对查看无显著效应；NP/PA实验中高时间压力显著降低查看率（p<0.0001）

##### evidence_pointers

1. Study One, Table 3, Viewership Models Model 2

2. Study Three, Table 8, Viewership Models Model 2

#### 4. 4

- theory_or_knowledge_claim_cn：为他人决策时决策者倾向于查看更多信息和替代选项，且偏见较少

- mechanism_cn：从业者作为患者代理，更可能认真评估替代方案，从而增加推荐系统影响决策的机会

- design_requirement_cn：推荐系统应提供足够数量和属性的替代选项，以促进信息搜索

- artifact_choice_cn：提供两个推荐选项（低成本组或混合成本组）并列显示成本

- evaluated_contrast_cn：整体查看率是否高、调整是否发生

- objective_result_cn：医师实验中查看率76.6%（147/192）、调整率64.6%（95/147）；NP/PA实验中查看率95%（114/120）、调整率69.3%（79/114）

##### evidence_pointers

1. Study One, Subjects and Data Description

2. Study Three, Descriptive Statistics

#### 5. 5

- theory_or_knowledge_claim_cn：NP/PA收入较低、培训强调与患者更多互动，因此可能更价格敏感且更容易受时间压力影响

- mechanism_cn：较低收入导致更低参考价格；较少的高压环境训练使得他们对时间压力更敏感

- design_requirement_cn：推荐系统设计可能需要根据从业者类型调整展示方式和交互负担

- artifact_choice_cn：NP/PA实验使用更强的时间压力操作和更多质量筛查；研究者比较医师与NP/PA的响应

- evaluated_contrast_cn：医师 vs NP/PA对成本框架和时间压力的反应差异

- objective_result_cn：NP/PA对成本框架不显著但整体调整率高，时间压力显著降低查看；医师相反，成本框架显著、时间压力不显著

##### evidence_pointers

1. Study One and Study Three results tables

2. Discussion section comparison

## 评价逻辑

### evaluation_modes

1. 受控在线实验（两个）

2. 半结构化访谈（定性）

3. 稳健性检验（删除首/末病例重新分析）

4. 操纵检验（问卷+时间阈值）

5. 经济估算（基于已有研究数据）

- why_these_evaluations_cn：核心问题涉及因果效应（成本框架和时间压力），因此需要受控实验以获得内部效度；样本为真实从业者，通过随机分配和操纵检验控制混杂因素；由于重复测量和查看/调整嵌套的内生性，使用GEE和Heckman处理；访谈用于验证实验发现的外部效度并解释机制；经济估算将实验室效应转化为现实政策意义。

- benchmark_and_contrast_chain_cn：所有实验的核心对比是低成本推荐组与混合成本推荐组，这直接操作化了理论中的参考价格差异；时间压力作为另一个正交处理，提供第二个对照维度；医师实验和NP/PA实验共享相同的成本对比但时间压力操作化不同，因此构成群体间对比；访谈结果作为实验结果的定性参照，既不肯定也不否定数据，而是补充真实环境背景；稳健性检验通过删除首/末病例确保结果非学习或疲劳导致。

### claim_evidence_ledger

#### 1. 低成本推荐的展示会增加处方调整率（相较混合成本）

- claim_cn：低成本推荐的展示会增加处方调整率（相较混合成本）

- evidence_cn：医师实验GEE模型Recommendations Costs(1)系数-2.03，p=0.042；Heckman stage 2系数-2.22，p=0.026。NP/PA实验中系数不显著。因此该主张仅对医师成立。

- strength_cn：支持（医师）但群体差异明显

#### 2. 时间压力会减少推荐查看

- claim_cn：时间压力会减少推荐查看

- evidence_cn：医师实验中Time Pressure Level(1)不显著；NP/PA实验中Time Pressure Level(1)系数-22.03，p<0.0001。

- strength_cn：部分支持，取决于从业者类型

#### 3. NP/PA比医师更倾向于采纳低成本建议

- claim_cn：NP/PA比医师更倾向于采纳低成本建议

- evidence_cn：NP/PA实验中整体调整率（79/114=69.3%）高于医师（95/147=64.6%），且成本框架不显著抑制其调整；讨论中给出描述性比较。

- strength_cn：描述性支持，但未做跨实验正式统计检验

#### 4. 适应水平理论/参考价格效应在医疗代理决策中成立

- claim_cn：适应水平理论/参考价格效应在医疗代理决策中成立

- evidence_cn：医师实验对成本框架的显著反应符合理论预测；讨论将其解释为参考价格效应。但未直接测量参考价格，属于推断性支持。

- strength_cn：间接支持，缺少中介测量

#### 5. 医生在实际实践中缺乏成本信息

- claim_cn：医生在实际实践中缺乏成本信息

- evidence_cn：访谈中绝大多数医生报告无准确成本信息或需费力检索。

- strength_cn：强支持（定性一致）

#### 6. 医生在时间压力下仍会使用推荐系统

- claim_cn：医生在时间压力下仍会使用推荐系统

- evidence_cn：访谈报告在高时间压力下更依赖EMR提示和模板；实验显示时间压力不降低医师查看。

- strength_cn：支持，但为自我报告和实验代理，非现场观察

- internal_validity_strategy_cn：随机分配参与者到成本组；时间压力采用组内设计并平衡顺序以控制个体差异；操纵检验包括成本注意问卷和完成时间阈值；用Heckman模型处理查看决定与调整决定的内生性；GEE处理重复测量的相关性；稳健性检验删除首/末病例控制学习/疲劳。

- external_validity_strategy_cn：使用真实执业医师、执业护士和医师助理作为被试；病例覆盖初级保健常见病，专家确认可被任意专科处理；访谈纳入不同专科的医生；报告样本特征并与总体医生分布比较；用经济估算将结果外推至Medicare Part D规模。

- what_is_not_actually_tested_cn：未直接测量参与者的参考价格（中间机制），因此适应水平解释是推断性的；未在真实临床现场进行部署或观察，行为表现是实验代理，而非实际处方后果；未引入社会规范信息（如其他医生处方行为）对推荐影响的潜在混淆；未比较不同时间压力操作化之间的等价性；未评估推荐对患者健康结果的直接长期影响。

## 贡献闭环

- technical_claim_cn：成本感知的推荐系统能在受控实验条件下显著改变处方行为：医师在低成本推荐时更可能调整到更便宜药物；NP/PA整体调整率高，但高时间压力会减少其查看推荐。

- artifact_claim_cn：设计差异（仅低成本 vs 混合成本推荐列表）导致了医师处方调整率的显著差异，说明推荐系统的成本框架设计是影响采纳的关键可操纵属性；而该设计差异对NP/PA没有显著影响，说明设计效果取决于用户群体。

- mechanism_claim_cn：医师对混合成本框架的负面影响被归因为参考价格效应：昂贵的替代选项提高了内部参考价格，使初始选择显得相对便宜，从而降低了调整动力；NP/PA对时间压力的敏感性被归因为培训差异和收入水平导致的认知负荷与价格敏感度差异。

- boundary_claim_cn：成本框架效应主要适用于医师，且在初级保健、药物疗效等效、医生缺乏成本知识的条件下成立；时间压力效应主要适用于NP/PA，而医师因专业训练和经验反而不受影响；结论可能不适用于高风险专科或真实处方环境。

- reusable_design_knowledge_cn：在处方时刻显示等效替代药物的准确成本可以促使从业者选择更便宜选项；若目标是最大化成本降低，全部低价的推荐列表对医师更有效，混合成本列表可能产生锚定效应抑制采纳；系统设计需考虑从业者类型：需要为NP/PA减轻时间压力造成的认知负担，而为医生应避免显示高价选项造成参考价格偏移。

- theoretical_contribution_cn：将适应水平理论和参考价格效应从消费者自购情境扩展到医疗提供者代表患者决策的代理决策情境；识别从业者类型（医师 vs NP/PA）作为参考价格效应和时间压力效应的调节变量；提出用户属性、先前倾向与经验可能调节推荐系统采纳的理论拓展方向。

- how_discussion_closes_intro_gap_cn：引言声称没有研究评估推荐系统用于降低医疗成本，讨论通过实验证明设计得当的推荐系统可以降低处方成本并给出经济估算；引言提出的混合成本设计可能的两个后果，讨论用医师实验显示混合成本确实抑制调整，但对NP/PA不抑制，从而细化了初始问题；引言强调时间压力的重要性，讨论说明其对不同从业者的不同作用，回应了实践关切。

- overclaim_or_unsupported_leaps_cn：样本量小且医师组仅32人，但作者承认并用case-level观察和与文献比较进行辩护；将成本框架效应归结为参考价格效应但未直接测量参考价格，属于推断性解释而非实证中介；NP/PA成本框架不显著却在讨论中推测为先前倾向影响，缺乏证据支持；经济估算假设实验中的采纳率可直接推广到全Medicare，未考虑报销、患者偏好和临床复杂性。

## 句级写作动作图谱

### 1. Abstract S1

- order：1

- section：Abstract

- locator：Abstract S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本文综合三项研究（两个受控实验和一个访谈）的结果，研究使用推荐系统在开处方时降低医疗成本，同时考虑时间压力。

- rhetorical_function_cn：在摘要开头直接预告研究形态和主题，让读者先建立整体结构认知。

- depends_on_cn：无，独立开篇。

- sets_up_cn：为后续详细摘要中的结果和贡献提供框架。

- evidence_pointer：Abstract S1

### 2. Abstract S2

- order：2

- section：Abstract

- locator：Abstract S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：所有参与者均为真实执业医师、执业护士或医师助理。

- rhetorical_function_cn：强调样本的真实性和领域专业性，以增强研究的可信度和实践意义。

- depends_on_cn：前一研究结构。

- sets_up_cn：暗示结论可推广到真实执业人群。

- evidence_pointer：Abstract S2

### 3. Abstract S3

- order：3

- section：Abstract

- locator：Abstract S3

- move_code：RESULT

- paraphrase_cn：主要发现是从业者在推荐系统提供成本信息时普遍倾向于选择成本更低的药物。

- rhetorical_function_cn：给出核心结论，回应标题中的疑问。

- depends_on_cn：三项研究综合结果。

- sets_up_cn：为后续关于时间压力差异和设计启示的句子作铺垫。

- evidence_pointer：Abstract S3

### 4. Abstract S4

- order：4

- section：Abstract

- locator：Abstract S4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：但日常面临的时间压力对执业护士和医师助理的影响似乎大于对医师的影响。

- rhetorical_function_cn：迅速引入重要边界条件，突显不同从业者类型的差异。

- depends_on_cn：主发现结果。

- sets_up_cn：强调研究对系统设计需要针对用户群体的启示。

- evidence_pointer：Abstract S4

### 5. Abstract S5

- order：5

- section：Abstract

- locator：Abstract S5

- move_code：CONTRIBUTION

- paraphrase_cn：这些结果对医疗成本和有效实时医疗推荐系统的设计具有重要意义。

- rhetorical_function_cn：在摘要末尾声明双重贡献：成本和设计。

- depends_on_cn：前面的结果和边界条件。

- sets_up_cn：告诉读者为什么值得读全文。

- evidence_pointer：Abstract S5

### 6. Introduction P1 S1–S4

- order：6

- section：Introduction

- locator：Introduction P1 S1–S4

- move_code：CONTEXT

- paraphrase_cn：美国医疗花费在2015年接近3.2万亿美元，处方药占3246亿；通过通用名替代或同一药物类别内品牌替代可以降低成本，但处方决策者通常不了解具体药价。

- rhetorical_function_cn：开篇用权威数据建立问题的紧迫性和现实性，同时指出已知的干预缺口。

- depends_on_cn：无。

- sets_up_cn：为后续提出推荐系统成本透明方案做背景铺垫。

- evidence_pointer：Introduction P1

### 7. Introduction P2 S1–S3

- order：7

- section：Introduction

- locator：Introduction P2 S1–S3

- move_code：PHENOMENON

- paraphrase_cn：传统上EMR不含成本信息，整合价格显示存在障碍；早期研究显示实时成本显示可适度减少实验室检查订购。

- rhetorical_function_cn：描述实际现象：系统缺陷和初步积极证据并存，为成本透明进入处方环节铺路。

- depends_on_cn：成本问题的背景。

- sets_up_cn：说明把成本透明应用于处方推荐的合理性和创新性。

- evidence_pointer：Introduction P2

### 8. Introduction P3 S1–S2

- order：8

- section：Introduction

- locator：Introduction P3 S1–S2

- move_code：GAP

- paraphrase_cn：已有研究尝试将推荐系统与EMR集成用于优化医疗计划和预测疾病风险，但据作者所知，尚无研究评估推荐系统用于降低医疗成本。

- rhetorical_function_cn：明确文献空白：现有推荐系统研究未聚焦成本降低。

- depends_on_cn：前面对医疗信息系统应用的综述。

- sets_up_cn：为本文研究目标提供直接定位。

- evidence_pointer：Introduction P3

### 9. Introduction P3 S3–S5

- order：9

- section：Introduction

- locator：Introduction P3 S3–S5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文考虑的场景是医师、医师助理或执业护士先做出诊断和治疗计划，然后推荐系统提供带有成本信息的替代方案，从业者可以选择替代或维持原计划。

- rhetorical_function_cn：具体化研究问题，界定推荐系统介入时点和用户决策顺序。

- depends_on_cn：前面的研究缺口。

- sets_up_cn：为实验设计的核心流程提供原型。

- evidence_pointer：Introduction P3 S3-S5

### 10. Introduction P4 S1–S4

- order：10

- section：Introduction

- locator：Introduction P4 S1–S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：与使用仿制药作为低成本选项的既有实践不同，本文考虑混合成本系统设计：显示与初始治疗方案疗效相当的所有药物选项的成本，其中一些可能更便宜、另一些更贵。

- rhetorical_function_cn：引入本文的设计创新点，并解释为何比仅显示低成本选项更现实。

- depends_on_cn：前文对替代药物可降低成本但医生不知情的描述。

- sets_up_cn：为后续理论推导中的low vs mixed对比奠定基础。

- evidence_pointer：Introduction P4

### 11. Introduction P5 S1–S2

- order：11

- section：Introduction

- locator：Introduction P5 S1–S2

- move_code：THEORY_INTRO

- paraphrase_cn：从理论上讲，成本如何呈现为推荐可能通过参考价格效应影响系统使用，该效应基于适应水平理论。

- rhetorical_function_cn：将设计差异与理论机制连接起来，表明设计选择不是纯粹工程启发式。

- depends_on_cn：设计特征描述。

- sets_up_cn：为后续的成本框架效应假设提供依据。

- evidence_pointer：Introduction P5

### 12. Introduction P6 S1

- order：12

- section：Introduction

- locator：Introduction P6 S1

- move_code：GAP

- paraphrase_cn：据作者所知，这是首个研究健康推荐系统设计对成本有效药物选项采纳影响的研究。

- rhetorical_function_cn：重复并强化空白声明，突出原创性。

- depends_on_cn：前文文献缺口。

- sets_up_cn：强调研究对理论和实践的重要性。

- evidence_pointer：Introduction P6 S1

### 13. Introduction P6 S2–S4

- order：13

- section：Introduction

- locator：Introduction P6 S2–S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：如果混合成本设计阻止从业者转向低价选项，这类推荐系统可能无法显著降低成本，从而可能建议只采用低成本推荐；反之，若混合成本设计也能降低成本，则提供了新的选择。

- rhetorical_function_cn：阐明研究结果对政策/设计决策的直接利害关系。

- depends_on_cn：先前的研究缺口。

- sets_up_cn：为实验中对比两种设计的重要性提供理由。

- evidence_pointer：Introduction P6 S2-S4

### 14. Introduction P7 S1–S4

- order：14

- section：Introduction

- locator：Introduction P7 S1–S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：时间在临床中是宝贵资源，从业者需额外时间查看成本和推荐，因此系统必须设计得能支持开处方时决策；由于时间压力，计算机化系统在某些情况下被选择性使用或完全移除。

- rhetorical_function_cn：引入第二个关键变量时间压力，并说明其对系统设计的现实制约。

- depends_on_cn：前文成本透明度问题。

- sets_up_cn：为实验中的时间压力操作化和假设做背景。

- evidence_pointer：Introduction P7

### 15. Introduction P8 S1–S2

- order：15

- section：Introduction

- locator：Introduction P8 S1–S2

- move_code：PHENOMENON

- paraphrase_cn：本文的独特性还在于检验推荐系统在不同从业者类型之间效果的差异：除了医生，NP和PA在许多州也有处方权，但他们的培训和财务安排不同。

- rhetorical_function_cn：把从业者类型差异作为第三个研究维度介绍。

- depends_on_cn：前文提及的NP/PA处方权。

- sets_up_cn：为Study Three和讨论中的调节效应分析铺路。

- evidence_pointer：Introduction P8

### 16. Introduction P9 S1–S3

- order：16

- section：Introduction

- locator：Introduction P9 S1–S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：三个目标：研究不同类型的成本感知推荐系统对处方选择行为的影响；研究时间压力如何影响系统使用；探索从业者专业知识对推荐评估和采纳的调节作用。

- rhetorical_function_cn：显式列出三个研究问题，为全文提供清晰结构。

- depends_on_cn：前文提出的两个变量和从业者类型差异。

- sets_up_cn：预告后续三部分内容（成本框架、时间压力、从业者类型）。

- evidence_pointer：Introduction P9

### 17. Introduction P10 S1–S4

- order：17

- section：Introduction

- locator：Introduction P10 S1–S4

- move_code：CONTRIBUTION

- paraphrase_cn：本文贡献包括：访谈揭示成本和时间压力的相关性，实验提供关于医疗推荐系统用于解决医疗成本上升的新见解，结果显示成本框架和时间压力能显著影响推荐采纳，并为理论构建和设计提供机会。

- rhetorical_function_cn：摘要式列出贡献，增强论文的卖点。

- depends_on_cn：三个研究目标和初步文献回顾。

- sets_up_cn：让读者预期后续详细结果。

- evidence_pointer：Introduction P10

### 18. Background P1 S1

- order：18

- section：Background and Theoretical Foundations

- locator：Background P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：大多数医生确实认识到处方时成本的重要性，调查显示愿意牺牲部分疗效来换取更可负担的药物。

- rhetorical_function_cn：建立“医生有成本意识”的已有知识，证明干预需求。

- depends_on_cn：无。

- sets_up_cn：为后续说明医生缺乏成本知识形成张力。

- evidence_pointer：Background P1

### 19. Background P2 S1–S4

- order：19

- section：Background and Theoretical Foundations

- locator：Background P2 S1–S4

- move_code：LIMITATION

- paraphrase_cn：早期在计算机化系统中添加价格比较模块的研究未发现处方成本的显著变化；另有研究发现实时成本信息对总体药物成本无影响，仅在某些药物类别有差异。

- rhetorical_function_cn：指出既有干预的不足，为本文的设计改进提供依据。

- depends_on_cn：前面对成本重要性的描述。

- sets_up_cn：引出本文的同药物类别品牌替代和加入NP/PA的新方向。

- evidence_pointer：Background P2

### 20. Background P3 S1

- order：20

- section：Background and Theoretical Foundations

- locator：Background P3 S1

- move_code：GAP

- paraphrase_cn：以往研究主要聚焦于品牌药和通用名药，而本文扩展研究同药物类别内品牌替代，这在三层保险计划日益普及的情况下更合适。

- rhetorical_function_cn：说明研究对象的创新转移。

- depends_on_cn：早期研究局限。

- sets_up_cn：为后续same drug-class替代的设计奠定基础。

- evidence_pointer：Background P3 S1

### 21. Cost Framing P1 S1–S3

- order：21

- section：The Cost Framing Effect

- locator：Cost Framing P1 S1–S3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：适应水平理论解释个体如何相对于适应水平对刺激作出反应：接近适应水平的刺激不会引发反应，高于或低于适应水平会引发相反方向的反应。

- rhetorical_function_cn：给读者提供理论核心，为之后参考价格应用做铺垫。

- depends_on_cn：前文的理论引入。

- sets_up_cn：推导出成本框架如何影响推荐的机制。

- evidence_pointer：Cost Framing P1

### 22. Cost Framing P2 S1–S2

- order：22

- section：The Cost Framing Effect

- locator：Cost Framing P2 S1–S2

- move_code：MECHANISM

- paraphrase_cn：在市场营销中，适应水平理论被用于解释消费者对价格的反应：消费者先形成内部参考价格，然后以此为锚判断其他价格。

- rhetorical_function_cn：将一般理论转化为价格领域的具体机制。

- depends_on_cn：适应水平理论。

- sets_up_cn：为医疗情境中的参考价格应用提供类比。

- evidence_pointer：Cost Framing P2

### 23. Cost Framing P3 S1–S3

- order：23

- section：The Cost Framing Effect

- locator：Cost Framing P3 S1–S3

- move_code：MECHANISM

- paraphrase_cn：在医疗情境中，从业者会根据系统显示的替代价格形成内部参考价格，并据此评估其初始处方的相对成本；由于医生缺乏成本知识，系统显示的成本成为主要刺激。

- rhetorical_function_cn：将参考价格机制移植到医疗处方决策，并说明为什么系统显示具有影响力。

- depends_on_cn：市场营销中的参考价格机制和医生成本知识缺乏的事实。

- sets_up_cn：推导出低成本或混合成本设计对参考价格的预期影响。

- evidence_pointer：Cost Framing P3

### 24. Cost Framing P4 S1–S4

- order：24

- section：The Cost Framing Effect

- locator：Cost Framing P4 S1–S4

- move_code：REQUIREMENT

- paraphrase_cn：在简单设计中，系统显示更便宜的等效替代选项，本文称为低成本设计；根据适应水平理论，这会使参考价格低于初始处方成本，从而触发更换。

- rhetorical_function_cn：把理论命题翻译为具体设计设置及其预期行为。

- depends_on_cn：参考价格机制。

- sets_up_cn：定义low-cost design并预告其正向采纳效果。

- evidence_pointer：Cost Framing P4

### 25. Cost Framing P5 S1–S3

- order：25

- section：The Cost Framing Effect

- locator：Cost Framing P5 S1–S3

- move_code：MECHANISM

- paraphrase_cn：显示更便宜的替代方案可能通过社会规范效应起作用，暗示从业者偏离了低成本处方规范，从而促使他们采纳推荐。

- rhetorical_function_cn：增加一个补充机制，说明低成本设计除了参考价格外还可能通过规范性信号起作用。

- depends_on_cn：前面低成本设计的描述。

- sets_up_cn：为讨论中可能的社会规范因素留下接口。

- evidence_pointer：Cost Framing P5

### 26. Cost Framing P6 S1–S3

- order：26

- section：The Cost Framing Effect

- locator：Cost Framing P6 S1–S3

- move_code：REQUIREMENT

- paraphrase_cn：仅推荐低成本方案不适用于儿童或老年人等特殊患者，因为更贵但使用更方便的剂型可能提高依从性；因此系统必须能够显示高低成本混合的选项。

- rhetorical_function_cn：从临床现实引出混合成本设计的必要性，表明其非任意设计。

- depends_on_cn：患者依从性和剂型考虑。

- sets_up_cn：定义mixed-cost design并解释其存在理由。

- evidence_pointer：Cost Framing P6

### 27. Cost Framing P7 S1–S2

- order：27

- section：The Cost Framing Effect

- locator：Cost Framing P7 S1–S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：与普通消费者不同，临床专家有能力识别替代药物在疗效和副作用上的相似性，因此不太可能用高价作为质量信号从而采纳更贵选项。

- rhetorical_function_cn：限制理论边界：在专家决策中价格-质量推断不适用。

- depends_on_cn：临床知识和专家报告。

- sets_up_cn：确保混合成本设计中的高成本选项不会被误认为是质量信号而采纳。

- evidence_pointer：Cost Framing P7

### 28. Cost Framing P8 S1–S4

- order：28

- section：The Cost Framing Effect

- locator：Cost Framing P8 S1–S4

- move_code：MECHANISM

- paraphrase_cn：即使高成本推荐不被采纳，它们也会作为价格评估时的锚点，根据适应水平理论，混合高低成本推荐会使参考价格处在中间位置，从而降低对低成本推荐的采纳。

- rhetorical_function_cn：明确混合成本框架的负面机制，为实验假设提供直接预测。

- depends_on_cn：参考价格机制。

- sets_up_cn：提出医师实验中混合成本组调整率降低的假设。

- evidence_pointer：Cost Framing P8

### 29. Cost Framing P9 S1–S3

- order：29

- section：The Cost Framing Effect

- locator：Cost Framing P9 S1–S3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：由于NP和PA服务的患者群体和收入水平不同（收入比医生低20-35%），他们可能更价格敏感，形成更低参考价格，因此更可能认为初始处方太贵并采纳低成本替代。

- rhetorical_function_cn：提出关于从业者类型差异的假设，为Study Three铺垫。

- depends_on_cn：NP/PA的工作环境文献。

- sets_up_cn：预期NP/PA的整体调整率更高且成本框架影响方式不同。

- evidence_pointer：Cost Framing P9

### 30. Time Pressure P1 S1–S2

- order：30

- section：The Time Pressure Effect

- locator：Time Pressure P1 S1–S2

- move_code：CONTEXT

- paraphrase_cn：医患接触时间稀缺，医生有时不到两分钟回答患者的临床问题，而NP通常花更多时间。

- rhetorical_function_cn：建立时间压力在临床中的普遍性和必要性。

- depends_on_cn：无。

- sets_up_cn：为时间压力假设提供现实基础。

- evidence_pointer：Time Pressure P1

### 31. Time Pressure P2 S1–S2

- order：31

- section：The Time Pressure Effect

- locator：Time Pressure P2 S1–S2

- move_code：GAP

- paraphrase_cn：虽然文献建议用计算机处方软件和提醒系统缓解时间不足，但尚无受控研究考察时间压力对这类系统实际使用的影响。

- rhetorical_function_cn：指出时间压力与医疗推荐系统使用之间的研究空白。

- depends_on_cn：前文关于时间压力的普遍性。

- sets_up_cn：将时间压力作为本文第二个主要研究对象。

- evidence_pointer：Time Pressure P2

### 32. Time Pressure P3 S1–S2

- order：32

- section：The Time Pressure Effect

- locator：Time Pressure P3 S1–S2

- move_code：MECHANISM

- paraphrase_cn：先前文献表明时间压力增加的认知需求会促使人们使用简化规则和默认选择；对成本感知推荐系统而言，高时间压力下医生可能直接沿用习惯治疗而忽略推荐。

- rhetorical_function_cn：从时间压力理论推导出对推荐使用的负面预期。

- depends_on_cn：时间压力决策文献。

- sets_up_cn：作为实验中时间压力操作的假设基础。

- evidence_pointer：Time Pressure P3

### 33. Time Pressure P4 S1–S2

- order：33

- section：The Time Pressure Effect

- locator：Time Pressure P4 S1–S2

- move_code：MECHANISM

- paraphrase_cn：高时间压力下个体会过滤掉视为次要的信息（如成本），尤其在门诊环境中虽然不危及患者安全但增加工作节奏压力。

- rhetorical_function_cn：解释为什么成本信息可能在时间压力下被忽略。

- depends_on_cn：信息处理理论。

- sets_up_cn：与后续医师实验的时间压力不显著形成对照。

- evidence_pointer：Time Pressure P4

### 34. Time Pressure P5 S1–S2

- order：34

- section：The Time Pressure Effect

- locator：Time Pressure P5 S1–S2

- move_code：MECHANISM

- paraphrase_cn：医生在住院医师训练中习惯了时间压力，而NP/PA培训强调与患者更多时间以及健康教育，且收入模式不同（固定薪金vs按服务收费），因此NP/PA可能对时间压力更敏感。

- rhetorical_function_cn：从培训和激励差异推导医师和NP/PA对时间压力的不同反应。

- depends_on_cn：前文的培训差异描述。

- sets_up_cn：为Study Three中NP/PA时间压力显著效应提供理论依据。

- evidence_pointer：Time Pressure P5

### 35. Decision Making P1 S1

- order：35

- section：Decision Making on Behalf of Others

- locator：Decision Making P1 S1

- move_code：MECHANISM

- paraphrase_cn：虽然药费不由处方者承担似乎会削弱价格敏感性，但关于为他人决策的研究表明，为他人决策时会查看更多替代品和属性。

- rhetorical_function_cn：反驳“医生不敏感”的反论，从为他人决策文献找到支持。

- depends_on_cn：前文参考价格机制。

- sets_up_cn：强化从业者会查看推荐和成本信息的预期。

- evidence_pointer：Decision Making P1

### 36. Decision Making P2 S1–S2

- order：36

- section：Decision Making on Behalf of Others

- locator：Decision Making P2 S1–S2

- move_code：MECHANISM

- paraphrase_cn：选择者代表他人做决定时通常偏见更少，如省略偏差和决策后扭曲更小，因此从业者更可能认真评估有价格的替代方案。

- rhetorical_function_cn：进一步说明为什么代理决策会促进对推荐的客观评估。

- depends_on_cn：为他人决策文献。

- sets_up_cn：为实验中高查看率和调整率提供理论预期。

- evidence_pointer：Decision Making P2

### 37. Study One Opening S1–S2

- order：37

- section：Study One

- locator：Study One Opening S1–S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：所有研究的核心是设计成本敏感推荐系统，呈现同等疗效的选项并附带准确成本信息，强调同时关注成本与结果。

- rhetorical_function_cn：为整个实验研究程序给定统一的设计框架。

- depends_on_cn：引言中的设计讨论。

- sets_up_cn：引向具体的low-cost和mixed-cost设置。

- evidence_pointer：Study One, first paragraph

### 38. Study One S3–S5

- order：38

- section：Study One

- locator：Study One S3–S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：推荐设置分为低成本设置（推荐均低于初始选择）和混合成本设置（推荐有高有低），预期低成本设置的采纳更高，混合成本设置的高价选项会提高参考价从而降低采纳。

- rhetorical_function_cn：将理论预测直接转化为实验中的两个比较组。

- depends_on_cn：前文成本框架理论。

- sets_up_cn：为实验设计的具体操作提供变量定义。

- evidence_pointer：Study One, Study One opening

### 39. Experimental Design P1 S1–S2

- order：39

- section：Study One Experimental Design

- locator：Experimental Design P1 S1–S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：与两位医疗从业者合作创建六份病历，每份包含患者信息、药物清单和SOAP格式详情，治疗方案留给参与者填写。

- rhetorical_function_cn：说明实验材料的来源和真实性，增强生态效度。

- depends_on_cn：无。

- sets_up_cn：为后续被试任务和结果测量奠定基础。

- evidence_pointer：Study One, Experimental Design P1

### 40. Experimental Design P2 S1–S3

- order：40

- section：Study One Experimental Design

- locator：Experimental Design P2 S1–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：病历由专家评定为相似复杂度和风险水平，聚焦内科常见病以确保所有专科均熟悉，替代药物属于同一药物类别和活性成分，从而副作用和疗效相似，差异只在成本。

- rhetorical_function_cn：证明实验材料控制了疗效和副作用变量，使成本成为唯一主要差异。

- depends_on_cn：专家协作开发。

- sets_up_cn：为结果解释为成本框架效应提供内部效度。

- evidence_pointer：Study One, Experimental Design P2

### 41. Experimental Design P3 S1–S3

- order：41

- section：Study One Experimental Design

- locator：Experimental Design P3 S1–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用2×2实验设计，成本作为组间变量，时间压力作为组内变量，并使用平衡顺序控制顺序效应。

- rhetorical_function_cn：描述实验设计的基本结构，说明处理变量和分配方式。

- depends_on_cn：前文的理论假设。

- sets_up_cn：为统计模型（GEE）和操纵检验提供依据。

- evidence_pointer：Study One, Experimental Design P3

### 42. Experimental Design P4 S1

- order：42

- section：Study One Experimental Design

- locator：Experimental Design P4 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：时间压力处理通过在三个病例中显示系统增加了许多病例的队列消息和页面计时器来实现。

- rhetorical_function_cn：给出时间压力操作化的具体技术实现。

- depends_on_cn：时间压力理论。

- sets_up_cn：为操纵检验提供操作对象。

- evidence_pointer：Study One, Experimental Design P4

### 43. Experimental Design P6 S1–S3

- order：43

- section：Study One Experimental Design

- locator：Experimental Design P6 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：成本操作通过动态操纵成本信息实现：低成本组的推荐均比初始选择便宜；混合成本组将初始选择设为成本X，推荐成本Y和Z满足Y<X<Z。

- rhetorical_function_cn：解释了成本框架在个体水平上如何动态生成，确保每位参与者看到的推荐相对成本符合分组。

- depends_on_cn：前文的成本框架定义。

- sets_up_cn：为后续统计模型中的成本框架变量提供操作依据。

- evidence_pointer：Study One, Experimental Design P6

### 44. Procedure P1 S1

- order：44

- section：Study One Experimental Procedure

- locator：Procedure P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验使用佛罗里达州32名参与者的便利样本，并要求参与者证明只完成一次以防止学习效应。

- rhetorical_function_cn：说明样本来源和预防学习效应的措施。

- depends_on_cn：前文设计。

- sets_up_cn：介绍样本规模限制并呼吁读者关注case-level观察。

- evidence_pointer：Study One, Experimental Procedure P1

### 45. Subjects S1–S5

- order：45

- section：Study One Subjects and Data

- locator：Subjects S1–S5

- move_code：RESULT

- paraphrase_cn：32名医生参与，共192个病例观测；参与者查看了147例推荐，并在查看过的147例中调整了95例处方，总体显示出降低治疗成本的倾向。

- rhetorical_function_cn：给出总体描述性结果，营造初步积极结论。

- depends_on_cn：实验执行。

- sets_up_cn：为后续统计模型分析做铺垫。

- evidence_pointer：Study One, Subjects and Data Description

### 46. Manipulation Checks S1–S3

- order：46

- section：Study One Manipulation Checks

- locator：Manipulation Checks S1–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通过问卷检查成本框架操纵，将未注意到成本信息的三名参与者的观察替换；为检查时间压力操纵，另招募8名医生为控制组，依据完成时间均值±2个标准差替换超过56分钟的观察。

- rhetorical_function_cn：说明操纵验证和数据清洗流程，增强实验结论的可信度。

- depends_on_cn：实验设计与操作化。

- sets_up_cn：为最终统计结果排除无效数据。

- evidence_pointer：Study One, Manipulation Checks

### 47. Statistical Findings P1 S1–S3

- order：47

- section：Study One Statistical Findings

- locator：Statistical Findings P1 S1–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用GEE处理每个参与者对六份病历的重复测量，并分别建立控制模型和全模型，以检验时间压力对查看和成本框架对调整的影响。

- rhetorical_function_cn：引入统计方法并告知读者为何采用GEE。

- depends_on_cn：实验设计中的组内因子。

- sets_up_cn：为呈现Table 3的回归结果做好准备。

- evidence_pointer：Study One, Statistical Findings P1

### 48. Statistical Findings P2 S1–S3

- order：48

- section：Study One Statistical Findings

- locator：Statistical Findings P2 S1–S3

- move_code：RESULT

- paraphrase_cn：GEE结果显示时间压力对推荐查看无显著效应，而成本框架对处方调整有显著效应；医生在混合成本条件下较少改为低成本选项。

- rhetorical_function_cn：报告核心统计发现，区分查看和调整两个因变量。

- depends_on_cn：上一句统计模型。

- sets_up_cn：为后续Heckman和结果解释提供主效应。

- evidence_pointer：Study One, Statistical Findings P2

### 49. Statistical Findings P3 S1–S3

- order：49

- section：Study One Statistical Findings

- locator：Statistical Findings P3 S1–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于只有查看过推荐才能调整，使用Heckman两阶段模型处理潜在内生性，并用时间压力作为排他性限制变量。

- rhetorical_function_cn：说明处理选择偏差的稳健性方法。

- depends_on_cn：查看和调整的嵌套关系。

- sets_up_cn：为Table 3第三部分的结果作铺垫。

- evidence_pointer：Study One, Statistical Findings P3

### 50. Statistical Findings P5 S1

- order：50

- section：Study One Statistical Findings

- locator：Statistical Findings P5 S1

- move_code：RESULT

- paraphrase_cn：两阶段分析确认GEE结果：时间压力不显著，推荐成本显著影响调整行为。

- rhetorical_function_cn：报告Heckman结果，增强成本框架效应的因果解释力。

- depends_on_cn：Heckman模型设定。

- sets_up_cn：引出对参考价格效应的总体解读。

- evidence_pointer：Study One, Statistical Findings P5

### 51. Statistical Findings P6 S1–S2

- order：51

- section：Study One Interpretation

- locator：Statistical Findings P6 S1–S2

- move_code：THEORY_RETURN

- paraphrase_cn：总体结果表明，推荐系统中成本替代的框架确实影响医生处方成本有效药物，说明即使是专家也受到参考价格效应的影响，且该效应发生在成本不由医生直接承担的情境中。

- rhetorical_function_cn：将统计结果提升到理论意义，回指适应水平理论。

- depends_on_cn：成本框架显著结果。

- sets_up_cn：为讨论部分的理论贡献奠定基础。

- evidence_pointer：Study One, Statistical Findings P6

### 52. Robustness Checks S1–S3

- order：52

- section：Study One Robustness Checks

- locator：Robustness Checks S1–S3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：为排除学习效应和疲劳效应，分别删除每个参与者完成的第一个和最后一个病例，重新建模，结果无实质变化。

- rhetorical_function_cn：通过稳健性检验保护主要结果的可靠性。

- depends_on_cn：成本框架效应的原始结果。

- sets_up_cn：为讨论中承认局限但坚持结论提供支撑。

- evidence_pointer：Study One, Robustness Checks

### 53. Study Two S1

- order：53

- section：Study Two Opening

- locator：Study Two S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为更好理解研究结果在实践中的影响并验证假设，对另一组医生进行了详细的事后访谈。

- rhetorical_function_cn：引入第二研究阶段，说明其目的。

- depends_on_cn：医师实验完成。

- sets_up_cn：描述访谈方法。

- evidence_pointer：Study Two, opening

### 54. Subjects and Methods S2–S4

- order：54

- section：Study Two Subjects and Methods

- locator：Subjects and Methods S2–S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：访谈采用开放问卷，先对4名医生进行预测试并迭代修正，然后对10名不同专科医生进行30-50分钟电话访谈并录音转写。

- rhetorical_function_cn：说明访谈样本、工具和流程，确保定性研究严谨性。

- depends_on_cn：无。

- sets_up_cn：为定性结果呈现提供方法论依据。

- evidence_pointer：Study Two, Subjects and Methods

### 55. Medication Cost Consideration S1–S3

- order：55

- section：Study Two Qualitative Results

- locator：Medication Cost Consideration S1–S3

- move_code：RESULT

- paraphrase_cn：访谈显示大多数医生仍认为降低患者自付成本重要，并提及经济可负担性与用药依从性之间的关联。

- rhetorical_function_cn：用定性数据验证医生成本意识假设。

- depends_on_cn：访谈数据。

- sets_up_cn：为结论‘医生愿意考虑成本’提供证据。

- evidence_pointer：Study Two, Medication Cost Consideration

### 56. Cost Information Access S1–S2

- order：56

- section：Study Two Qualitative Results

- locator：Cost Information Access S1–S2

- move_code：RESULT

- paraphrase_cn：医生报告没有或很少获得准确成本信息，现有信息过于笼统且获取费力，患者间保险差异使成本更难确定。

- rhetorical_function_cn：证实引言中的成本信息缺口，凸显推荐系统价值。

- depends_on_cn：访谈回答。

- sets_up_cn：为强调自动成本显示的必要性提供现实基础。

- evidence_pointer：Study Two, Cost Information Access

### 57. System Use under High Time Pressure S1–S3

- order：57

- section：Study Two Qualitative Results

- locator：System Use under High Time Pressure S1–S3

- move_code：RESULT

- paraphrase_cn：与急诊文献不同，门诊医生报告在高时间压力下会更加使用信息系统，通过提示、模板和事后补记来节省时间；这与实验发现的时间压力不显著一致。

- rhetorical_function_cn：提供定性解释，说明为什么医师实验时间压力效应为零。

- depends_on_cn：访谈结果和医师实验。

- sets_up_cn：支持后续‘医生会接受推荐系统’的结论。

- evidence_pointer：Study Two, System Use under High Time Pressure

### 58. System Use under High Time Pressure P3

- order：58

- section：Study Two System Feature Needs

- locator：System Use under High Time Pressure P3

- move_code：REQUIREMENT

- paraphrase_cn：医生期望推荐系统提供疗效和安全性对比、循证医学证据支持，并且使用体验省时。

- rhetorical_function_cn：将访谈反馈转化为设计需求，为设计科学贡献提供内容。

- depends_on_cn：访谈中关于意向系统的问题。

- sets_up_cn：为讨论中的设计建议提供依据。

- evidence_pointer：Study Two, System Use under High Time Pressure, numbered list

### 59. End of Study Two

- order：59

- section：Study Two End

- locator：End of Study Two

- move_code：TRANSITION

- paraphrase_cn：综合访谈与实验，医生确实认识成本重要性并可能在时间压力下采用成本敏感推荐系统，但成本框架有影响；接下来研究拥有处方权的NP和PA。

- rhetorical_function_cn：小结第一阶段并引出下一研究对象。

- depends_on_cn：医师实验和访谈。

- sets_up_cn：为Study Three的开场做铺垫。

- evidence_pointer：Study Two, final paragraph

### 60. Study Three S1

- order：60

- section：Study Three

- locator：Study Three S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：最后，为研究不同专业水平的从业者在临床环境中的决策差异，作者研究了NP和PA。

- rhetorical_function_cn：开启第三个研究阶段并说明研究目的。

- depends_on_cn：前两个研究完成。

- sets_up_cn：描述NP/PA实验设计。

- evidence_pointer：Study Three, opening

### 61. Experimental Design P1–P2

- order：61

- section：Study Three Experimental Design

- locator：Experimental Design P1–P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为减少完成时间以招募NP/PA，新实验仅使用三个病例，其中前两个要求参与者写摘要以验证认真程度；时间压力通过绩效排名提示（如A+ Star Performer）操作化，强度大于医师实验。

- rhetorical_function_cn：解释为适应样本要求而对设计做出的调整，并说明更强的压力操作。

- depends_on_cn：医师实验设计的复用。

- sets_up_cn：说明为何需要专门的质量筛选和更强操纵。

- evidence_pointer：Study Three, Experimental Design P1-P2

### 62. Experimental Design P3–P4

- order：62

- section：Study Three Experimental Design

- locator：Experimental Design P3–P4

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：成本处理复制医师实验：参与者看到全部低成本或混合成本推荐；采用2×2组间设计，随机分配。

- rhetorical_function_cn：明确对照组和组间因子，确保与医师实验可比。

- depends_on_cn：前文成本框架定义。

- sets_up_cn：为描述统计和模型结果提供结构。

- evidence_pointer：Study Three, Experimental Design P3-P4

### 63. Subjects S1

- order：63

- section：Study Three Subjects

- locator：Subjects S1

- move_code：INPUTS

- paraphrase_cn：通过Qualtrics招募了120名具有处方权的NP和PA，其中88%为NP，68%有超过10年经验。

- rhetorical_function_cn：说明样本量大于医师实验，提高统计效力。

- depends_on_cn：实验招募。

- sets_up_cn：与医师实验结果进行群体比较。

- evidence_pointer：Study Three, Subjects

### 64. Results Descriptive Statistics S1–S3

- order：64

- section：Study Three Results

- locator：Results Descriptive Statistics S1–S3

- move_code：RESULT

- paraphrase_cn：NP和PA中，120例中有114例查看推荐，其中79例调整处方；这比医师的采纳率更高。

- rhetorical_function_cn：报告总体高采纳率，突显群体差异。

- depends_on_cn：实验数据。

- sets_up_cn：引出后续统计模型中的群体比较。

- evidence_pointer：Study Three, Descriptive Statistics

### 65. Manipulation Checks S1–S4

- order：65

- section：Study Three Results

- locator：Manipulation Checks S1–S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通过注意力问卷和完成时间阈值筛选，替换未注意成本、完成过快或过慢的观察；因为样本来自Qualtrics，还通过病例摘要质量检查认真性。

- rhetorical_function_cn：承认第三方样本的噪音来源并描述质量控制程序。

- depends_on_cn：实验设计。

- sets_up_cn：为分析结果的干净性辩护。

- evidence_pointer：Study Three, Manipulation Checks

### 66. Statistical Findings S1–S3

- order：66

- section：Study Three Results

- locator：Statistical Findings S1–S3

- move_code：RESULT

- paraphrase_cn：统计结果显示混合成本框架对NP/PA的调整行为无显著效应，但他们对成本似乎比医生更敏感；时间压力则对查看推荐有显著负面影响。

- rhetorical_function_cn：报告与医师实验形成对比的关键结果。

- depends_on_cn：回归模型结果。

- sets_up_cn：为讨论中的理论和设计差异提供证据。

- evidence_pointer：Study Three, Statistical Findings

### 67. Discussion P1 S1–S2

- order：67

- section：Discussion

- locator：Discussion P1 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：如果设计得当，医疗推荐系统可以显著降低药房成本；引用已有研究估计Medicare Part D 2013年可节省约2.02亿美元。

- rhetorical_function_cn：将实验结果转化为现实经济价值，强化研究意义。

- depends_on_cn：实验采纳率和外部成本估算。

- sets_up_cn：引出对实践和政策的含义。

- evidence_pointer：Discussion P1

### 68. Discussion P3 S1–S3

- order：68

- section：Discussion

- locator：Discussion P3 S1–S3

- move_code：THEORY_RETURN

- paraphrase_cn：医师实验结果证实了基于适应水平和参考价格效应提出的命题：混合成本框架提高了医生的内部参考价格，从而减少了对低成本推荐的采纳。

- rhetorical_function_cn：明确回到理论，将实证结果与初始理论命题对接。

- depends_on_cn：医师实验成本框架显著结果。

- sets_up_cn：随后讨论NP/PA差异的原因和理论延伸。

- evidence_pointer：Discussion P3

### 69. Discussion P4 S1–S3

- order：69

- section：Discussion

- locator：Discussion P4 S1–S3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者推测NP/PA不受成本框架影响的原因可能是他们的成本知识或先前倾向不同，并指出用户属性、先前倾向和经验的调节作用未充分探索，可作为未来研究方向。

- rhetorical_function_cn：为意外结果提供解释性推测并指出理论拓展方向。

- depends_on_cn：NP/PA实验结果。

- sets_up_cn：为结论部分的理论构建机会做铺垫。

- evidence_pointer：Discussion P4

### 70. Discussion P6 S1–S2

- order：70

- section：Discussion

- locator：Discussion P6 S1–S2

- move_code：DESIGN_KNOWLEDGE

- paraphrase_cn：成本感知推荐系统的设计可能需要适应从业者属性和经验：显示成本信息总体上有利于患者和成本降低，但采纳效果取决于用户类型（医生 vs NP/PA）。

- rhetorical_function_cn：提炼可复用的设计知识，回应引言中的设计问题。

- depends_on_cn：两个实验的对比结果。

- sets_up_cn：引出时间分配等政策建议。

- evidence_pointer：Discussion P6

### 71. Discussion P7 S1–S3

- order：71

- section：Discussion

- locator：Discussion P7 S1–S3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者承认样本量小、病例限于初级保健、实验情境推广性有限，并提到未直接测量参考价格、未包含社会规范信息、实验设计可能引入学习偏差等局限。

- rhetorical_function_cn：系统列出研究局限，保护贡献不被过度解读。

- depends_on_cn：全篇方法。

- sets_up_cn：为未来研究建议做铺垫。

- evidence_pointer：Discussion P7

### 72. Conclusion P1 S1–S3

- order：72

- section：Conclusion

- locator：Conclusion P1 S1–S3

- move_code：CONTRIBUTION

- paraphrase_cn：本文通过三项研究提供了对医疗从业者通过推荐系统使用成本信息的理解，显示总体倾向于在提供成本比较时降低成本，并指出设计良好的推荐系统可带来显著节省。

- rhetorical_function_cn：总结核心发现，强化主张。

- depends_on_cn：所有研究结果。

- sets_up_cn：最后以政策含义收尾。

- evidence_pointer：Conclusion P1

### 73. Conclusion P2 S1–S3

- order：73

- section：Conclusion

- locator：Conclusion P2 S1–S3

- move_code：CONTRIBUTION

- paraphrase_cn：将推荐系统视为带来变革的人工物，其效果取决于所呈现的信息和系统运行的整体环境，因此只优化信息显示而不考虑上下文（如时间压力）可能效果较差。

- rhetorical_function_cn：从IS理论视角提升研究贡献，呼应题目中的角色讨论。

- depends_on_cn：讨论中的设计知识。

- sets_up_cn：结束论文并留下宏观启示。

- evidence_pointer：Conclusion P2

## 写作技术

- gap_construction_cn：首先用巨额医疗成本和处方药支出数字营造紧迫性；接着指出现有EMR缺乏成本信息、医生缺乏药价知识，且早期成本显示干预效果微弱；随后聚焦推荐系统，声称‘尚无研究评估推荐系统用于降低医疗成本’，形成明确缺口；再以‘首次研究’标识强化原创性。

- signposting_cn：引言末尾明确列出三个研究目标；每个Study开头说明研究问题和方法；在Study Two结尾预告下一阶段；讨论部分使用‘本研究的贡献包括’等路标语句；结论重申三项综合研究。

- transition_logic_cn：各Study之间的过渡主要基于论证需求：实验证明机制后，访谈验证外部效度和解释异常；访谈引出NP/PA差异后，Study Three扩展群体；每个阶段末尾用一两句话小结并预告下一步。

- claim_evidence_rhythm_cn：每个实验先报告描述性统计，再报告操纵检验，然后报告正式统计模型（GEE、Heckman），随后解释结果含义并回扣理论；证据与主张紧邻放置，避免悬空。

- benchmark_narrative_cn：低成本推荐组作为基准，混合成本组作为对比，将理论中的参考价格锚定操作化；时间压力的高低对照形成另一个基准；医师实验与NP/PA实验构成跨群体对比；访谈结果作为实践基准。作者将benchmark嵌入论证，使每个对比都直接服务理论命题检验。

- theory_return_cn：讨论中把医师对成本框架的反应重新连接到适应水平理论的参考价格机制，并指出该效应在代理决策情境中的新颖性；将NP/PA的时间压力敏感性与培训和激励差异结合，从而让实验发现的意外结果重新融入理论框架，并指出未来理论构建的缺口。

- contribution_positioning_cn：在引言和讨论中反复声称‘首次研究’，同时在与其他医疗推荐系统（如预测诊断、护理计划）和早期CPOE成本显示对比中定位自己的创新；贡献分为理论、设计知识和实践收益三层，最后用经济估算加强实际影响力。

- novelty_protection_cn：通过多研究三角验证（实验+访谈）和稳健性检验使结果不止于一次性性能；通过识别从业者类型调节变量，将效应描述为具有边界条件的理论现象而不是单一样本偶然；通过讨论参考价格效应和设计自适应，将具体的成本框架效果提升为可迁移的设计知识。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：开篇用权威数据和现实后果建立问题背景，并给出读者能理解的具体痛点（医生不知道药价、EMR无成本）。

- research_job_cn：收集领域内的成本数据、已有干预尝试和失败案例。

- required_evidence_cn：可信的数据来源（国家健康支出统计）、调查或元分析显示从业者成本知识不足。

- transition_to_next_cn：由背景转向‘我们对什么知道得很少’的缺口。

#### 2. 2

- step：2

- writing_job_cn：用参考文献构建理论框架，解释为什么某个设计差异可能产生不同行为；在本文是适应水平理论→参考价格→成本框架。

- research_job_cn：选择与决策行为相关的成熟理论，将其机制翻译为可操纵的设计变量。

- required_evidence_cn：理论的核心命题、在相关领域的应用证据（如市场营销中的参考价格）。

- transition_to_next_cn：从理论命题推导出设计要求和预期效应。

#### 3. 3

- step：3

- writing_job_cn：清晰描述制品的组成：系统原型、实验材料、处理操作化；用图/附录展示界面和案例。

- research_job_cn：实际构建推荐系统界面和实验材料；请领域专家验证材料的真实性、复杂度和等效性。

- required_evidence_cn：专家报告、界面截图、案例文本、成本动态操纵的逻辑。

- transition_to_next_cn：进入数据收集阶段，说明实验设计和被试招募。

#### 4. 4

- step：4

- writing_job_cn：描述实验设计、样本、变量、操纵检查和统计方法；先报告描述性结果，再报告正式模型。

- research_job_cn：实施受控实验；收集真实从业者数据；进行操纵检验和质量筛选；选择合适统计模型（重复测量、选择模型）。

- required_evidence_cn：样本特征表、描述性统计表、回归模型结果表（含p值和系数）、稳健性检验。

- transition_to_next_cn：根据实验结果决定是否需要补充研究来解释意外发现或扩展群体。

#### 5. 5

- step：5

- writing_job_cn：在受控实验后添加定性研究（访谈）验证外部效度，并解释实验中的意外结果；报告引语和主题。

- research_job_cn：设计半结构化访谈、邀请领域专家、进行系统编码。

- required_evidence_cn：访谈样本表、主题汇总表、代表性引语。

- transition_to_next_cn：将定性发现与实验结合，提出新假设或设计改进，进入第二个实验。

#### 6. 6

- step：6

- writing_job_cn：设计第二个实验检验调节变量（从业者类型）或改变操作化，报告与第一个实验的对比。

- research_job_cn：招募更大人群（如NP/PA），调整实验长度和时间压力强度，执行相同或类似程序。

- required_evidence_cn：样本截图/人口统计表、结果表、与第一实验结果的并排解释。

- transition_to_next_cn：在讨论中综合所有研究，回到理论框架解释结果。

#### 7. 7

- step：7

- writing_job_cn：讨论部分先给出总体正面结论，然后用经济估算和理论回返提高贡献层次；列出局限和未来方向。

- research_job_cn：计算现实可实现的节省（如利用外部数据），将结果与更广泛理论连接，识别边界条件。

- required_evidence_cn：外部成本估算的引用、理论命题与结果的对齐、局限清单。

- transition_to_next_cn：以贡献声明和政策/设计启示结束。

### most_transferable_moves_cn

1. 用真实领域数据和专家合作构建高生态效度的实验材料

2. 将理论机制翻译为二值设计变量（如低成本 vs 混合成本）并进行受控对比

3. 使用操纵检查和质量筛选保障实验数据有效性

4. 用GEE和Heckman处理重复测量与选择偏差，提升统计严谨性

5. 在受控实验后加入访谈解释意外发现并补充外部效度

6. 通过群体对比（专家 vs 准专家）揭示边界条件

7. 用经济估算将实验结果转为可感知的实践价值

### resource_intensive_or_nonstandard_parts_cn

1. 招募160名真实执业医疗从业者（尤其32名医生）非常困难且成本高

2. 开发六份详细病历和动态成本操纵系统需要领域专家投入

3. 获取药品成本数据和保险自付估算需药物经济学知识

4. Heckman和GEE等计量方法需要较高统计专长

5. 访谈（10名医生，30-50分钟）以及转写编码耗时

6. 通过Qualtrics的第三方样本质量筛选复杂（约120人，需质量检查）

### what_not_to_copy_superficially_cn

1. 不可仅宣称‘首次研究’而无实际文献空白支撑

2. 不可在没有操纵检查和样本筛选的情况下报告实验结论

3. 不可将参考价格效应作为因果解释而不测量中介变量

4. 不可将医师实验的显著性直接推广到其他从业者群体

5. 不可忽略时间压力操作化的强度差异而跨实验直接比较系数量级

6. 不可仅用访谈引语代替系统化编码和共识度评估

- single_best_description_of_the_routine_cn：先用数据和文献制造真实缺口，再用成熟理论推出两个设计对比，通过两个受控实验和一个访谈对同一组假设进行三角检验，最后回到理论解释差异并转化为可复用的设计知识和经济价值。

## 分析边界

全文在任务中完整提供，包括附录和图表引用，但表格中的部分统计数值可能存在OCR误差（如Heckman系数、QIC值等），句子级位置基于段落逻辑推断而非实际页面页码；部分图表（如Table 4的稳健性结果表）在文本中被引用但未在正文完整展示数值，分析依赖正文描述；论文没有明确指出未测量参考价格这一点，但在讨论局限时有提到。
