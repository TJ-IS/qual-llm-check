# Overcoming Breakdowns in Customer-Chatbot Interaction: Design and Impact of Collaborative Repair Strategies

- 作者：Ulrich Gnewuch; Fabian Reinkemeier
- 年份 / 期刊：2026 / MIS Quarterly
- DOI：10.25300/misq/2025/18742
- 源文件：27650_2026_overcoming-breakdowns-in-customer-chatbot-interaction-design-and-impact-of-collaborative-repair.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.93

## 文章级论证概况

- 核心问题：在真实顾客-聊天机器人交互中，应如何设计协作式修复策略（collaborative repair strategies），让顾客和聊天机器人共同解决对话故障（conversational breakdowns），并比现有单方承担修复负担的策略更有效？

- 制品与设计：作者提出并实现了一套基于TLCE-bot理论的协作式修复策略设计，包含四个相互关联的组件：故障类型学（breakdown typology）、自适应修复类型（adaptive repair types）、自适应修复消息（adaptive repair messages，包含道歉、解释、指导三要素）和实时故障处理（real-time breakdown handling）。该系统被实例化部署在一家大型保险公司InsurCo的现有聊天机器人中。

- 客观结果：在随机现场实验中，协作式修复策略相比非协作基线使故障解决率从32.41%提高到38.23%（logit b=0.243, p=0.044），首次故障后立即放弃率从50.95%降到41.68%（b=-0.373, p=0.001），对修复消息的负面反馈从91.39%降到82.80%（b=-1.333, p=0.003），满意度平均分数从1.82提高到2.07（b=0.540, p=0.066）。

- 核心贡献：作者声称的贡献是：将顾客-AI服务互动叙事从对抗转向协作；扩展TLCE为TLCE-bot框架，提出三个针对顾客-聊天机器人交互的新原则；提供真实世界中故障性质与协作修复策略效果的经验证据；为 practitioners 提供可复用的设计处方。

- 整篇论证链：文章先指出现有顾客-聊天机器人交互中故障不可避免，而当前修复策略要么让顾客自行重试、要么让机器人猜测意图，形成令人沮丧的猜谜游戏；现有文献虽有合作修复偏好的迹象，但缺乏设计指导和真实场景证据。作者以TLCE为内核理论，通过概念混合整合人机沟通与客服聊天机器人文献，形成TLCE-bot三原则（辅助性自我修复、诊断透明度、努力程度与故障严重度相称），并转化为六条元需求、四组件元设计和两项可检验命题。随后在企业真实环境中用聊天记录聚类识别四类故障，用受控在线实验检验具体修复消息优于通用消息，用监督学习构建实时故障分类器并集成到InsurCo聊天机器人，最后用随机现场实验检验完整策略。结果显示协作式策略提高了故障解决率、减少立即放弃并减轻负面反馈与满意度损失；讨论部分将该结果回写为对TLCE的理论扩展、对协作叙事的贡献和对故障类型边界条件的识别。

## 类型与写作弧线判定

- 论文主类型判定：文章明确遵循设计科学研究范式，按Walls et al.的设计理论结构呈现内核理论、元需求、元设计、可检验命题，并通过三个设计片段（design episodes）实例化组件，以自然主义总结性评估收尾，最终产出的核心是设计知识与设计原则而非单纯的行为实验。

- 主导写作弧线判定：全文主线是：从TLCE-bot推导元需求→形成元设计→在实际企业中逐组件构建实例→用组件级实验和现场实验评价→提炼可复用设计知识与边界条件。这符合“要求—构建—评价—设计原则”的写作弧线。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：初始问题空间探索（论文仅提及）→设计片段1：故障类型识别→设计片段2：自适应修复类型与消息并通过在线实验验证→设计片段3：实时故障处理（分类器+Web应用+集成）→自然主义总结性随机现场实验。每个阶段生成下一阶段可用的输入：前一阶段产出故障类型学，第二段产出修复类型/消息，第三段将其自动化，现场实验对完整实例做终极检验。

### studies_or_phases

#### 1. 初始问题空间探索（DSR前置阶段）

- order：1

- name_cn：初始问题空间探索（DSR前置阶段）

- question_cn：InsurCo聊天机器人的问题空间是什么？故障为何发生？

- inputs_and_setting_cn：论文正文未详述，仅说明存在一个初始问题空间探索阶段，详见Reinkemeier & Gnewuch (2022)的前序ECIS论文。

- designed_or_compared_object_cn：未在本文中展开；隐含地界定了聊天机器人故障与修复策略这一设计问题类别。

- baseline_control_or_counterfactual_cn：未在本文中展开。

##### objective_metrics

（空）

- analysis_method_cn：论文正文仅以文献方式说明先进行了问题空间探索。

- main_result_cn：形成对顾客-聊天机器人交互中故障不可避免、现有修复策略单方负责的问题认知，并铺垫与InsurCo的合作。

- argumentative_role_cn：为后续设计片段提供现实问题和企业情境。

- remaining_uncertainty_cn：缺少在本文可检视的细节；需要具体数据才能进入组件设计。

- link_to_next_phase_cn：将问题聚焦为需要识别故障类型，从而启动设计片段1。

##### evidence_pointers

1. Design Instantiation section, first paragraph; mentions initial problem space exploration and cites Reinkemeier & Gnewuch (2022)

#### 2. 设计片段1：故障类型识别（Breakdown Type Identification）

- order：2

- name_cn：设计片段1：故障类型识别（Breakdown Type Identification）

- question_cn：InsurCo顾客与聊天机器人交互中的故障可归纳为哪些类型？

- inputs_and_setting_cn：21,736条真实顾客消息；其中5,668条造成故障的breakdown messages；另用180条消息由两位人工编码员验证类型学。

- designed_or_compared_object_cn：对故障消息进行聚类，形成故障类型学；并用人工编码分配作为参考比较自动化分类。

- baseline_control_or_counterfactual_cn：人工编码员的分类作为判断类型学有效性的参照。

##### objective_metrics

1. 与人工编码的一致率79.44%

2. Cohen's kappa = 0.70

- analysis_method_cn：基于语义权重、未知词比例、词数、句均词数四个内容无关特征对故障消息做聚类分析。

- main_result_cn：识别出四类故障：详细型（elaborate）、独特型（unique）、简短型（brief）、隐晦型（cryptic），并被验证为有效起点。

- argumentative_role_cn：为后续修复类型、修复消息和实时分类器提供基础分类。

- remaining_uncertainty_cn：尚不知道各类故障应采用哪些修复类型和消息。

- link_to_next_phase_cn：四类故障直接作为设计片段2中定义修复类型与消息的输入。

##### evidence_pointers

1. Design Episode 1 section

2. Table 2

#### 3. 设计片段2：自适应修复类型与自适应修复消息（含受控在线实验）

- order：3

- name_cn：设计片段2：自适应修复类型与自适应修复消息（含受控在线实验）

- question_cn：面对不同故障类型，应选择何种修复类型和修复消息？故障类型特定的修复消息是否比通用消息更有效？

- inputs_and_setting_cn：与InsurCo的研讨工作坊；579名参与者；自建聊天机器人界面；八条预定义对话（2种修复消息×4种故障类型）。

- designed_or_compared_object_cn：比较故障类型特定修复消息（具体消息）与通用修复消息（“对不起，我不理解。请重试”）；并确定不同连续故障组合的修复类型。

- baseline_control_or_counterfactual_cn：通用修复消息作为基线条件。

##### objective_metrics

1. 聊天机器人意图识别分数（intent recognition score）

2. 满意度

3. 挫败感

4. 感知聊天机器人努力程度

5. 操纵检验

- analysis_method_cn：2×4组间设计；t检验、Mann-Whitney U检验、Bonferroni校正成对比较。

- main_result_cn：具体修复消息相比通用消息显著提高意图识别分数（M=0.611 vs 0.499, p<0.001）、提高满意度、降低挫败感、提高感知努力；对elaborate、unique、brief三类均显著，对cryptic仅在10%水平显著。

- argumentative_role_cn：在受控层面建立“协作式具体消息优于通用消息”的组件级因果证据，并为现场实施提供修复消息库。

- remaining_uncertainty_cn：消息在受控情境有效，但尚不知道能否在真实聊天机器人中实时分类和触发，也不确定完整策略在真实场景是否有效。

- link_to_next_phase_cn：将修复类型与消息表传给设计片段3，用于条件流程配置。

##### evidence_pointers

1. Design Episode 2 section

2. Table 3

3. Table 4

4. Appendix B

#### 4. 设计片段3：实时故障处理（分类器、Web应用与系统集成）

- order：4

- name_cn：设计片段3：实时故障处理（分类器、Web应用与系统集成）

- question_cn：如何自动将顾客消息实时分类到故障类型，并在真实机器人后端触发对应修复消息？

- inputs_and_setting_cn：从InsurCo近三个月交互中抽取超过1,000条故障消息，由两名研究助理人工标注（一致率83%，kappa=0.80）；比较10种多分类机器学习算法；在InsurCo云端部署Flask Web应用。

- designed_or_compared_object_cn：构建并比较10种算法以选择最优故障类型分类器；开发实时分类Web应用；通过webhook集成进InsurCo聊天机器人。

- baseline_control_or_counterfactual_cn：10种算法相互比较作为基线；嵌套10折交叉验证防止过拟合。

##### objective_metrics

1. Accuracy

2. Precision

3. Recall

4. F1

5. Prediction time

- analysis_method_cn：监督机器学习；网格搜索与嵌套交叉验证；系统架构集成。

- main_result_cn：梯度提升（gradient boosting）表现最佳（准确率75.2%，F1 73.6%，预测时间0.004秒）；部署Flask Web应用，聊天机器人后端通过webhook触发分类并配置超过20条条件流程。

- argumentative_role_cn：证明协作式修复策略具备“最后一公里”可实现性，使现场实验成为可能。

- remaining_uncertainty_cn：分类器并非完美；尚不知道真实交互中的端到端效果。

- link_to_next_phase_cn：完整系统激活后进入自然主义现场实验。

##### evidence_pointers

1. Design Episode 3 section

2. Appendix C

3. Figure 4

#### 5. 自然主义总结性评价：随机现场实验

- order：5

- name_cn：自然主义总结性评价：随机现场实验

- question_cn：在真实顾客与InsurCo聊天机器人交互中，协作式修复策略是否比非协作式基线修复策略更有效地解决故障并减轻负面顾客结果？

- inputs_and_setting_cn：2022年秋季8周内4,305名与InsurCo聊天机器人交互的顾客；其中1,352名经历过故障并进入分析；随机分配到协作策略或非协作策略；收集对话数据、故障数据、顾客评价数据（满意度和拇指投票）及设备/来源/请求类别等控制变量。

- designed_or_compared_object_cn：比较协作式修复策略（分类+特定修复消息+渐进升级）与非协作式基线（通用“请重试”消息，三次后提供人工客服）之间的差异；修复策略是唯一差异，响应时间相同。

- baseline_control_or_counterfactual_cn：非协作式条件为基线，即InsurCo项目开始前原有策略。

##### objective_metrics

1. Breakdown resolution（故障解决率）

2. Immediate abandonment（首故障后立即放弃率）

3. Customer feedback（拇指负反馈比例）

4. Customer satisfaction（5星满意度）

- analysis_method_cn：Logistic回归（模型1-3）、OLS回归（模型4）；控制设备、来源、请求类别、故障类型与位置、保险产品固定效应、时间固定效应；用两阶段Heckman选择模型做稳健性检验。

- main_result_cn：协作式策略显著提高故障解决率（b=0.243, p=0.044，OR=1.274）、显著降低立即放弃率（b=-0.373, p=0.001，OR=0.689）、显著降低负面反馈（b=-1.333, p=0.003，OR=0.264），满意度提高但仅10%显著（b=0.540, p=0.066）；按故障类型看，对elaborate、brief、unique类有效，对cryptic类（无意义输入或外语）反而更低。

- argumentative_role_cn：为两项可检验命题提供现场证据，将组件级效果上升为完整策略在真实情境中的有效性证据，并揭示边界条件。

- remaining_uncertainty_cn：样本仅来自一家保险公司的意图型德语聊天机器人；satisfaction样本较小；未直接测量协作感知机制；无法排除企业特定背景对结果的影响。

- link_to_next_phase_cn：结果进入讨论，用于构建理论贡献、实践含义和未来研究边界。

##### evidence_pointers

1. Naturalistic Summative Evaluation section

2. Table 5

3. Table 6

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PHENOMENON

3. GAP

4. RQ_OR_OBJECTIVE

5. THEORY_INTRO

6. STUDY_OVERVIEW

7. RESULT

8. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. PRIOR_KNOWLEDGE

5. LIMITATION

6. GAP

7. WHY_GAP_MATTERS

8. RQ_OR_OBJECTIVE

9. STUDY_OVERVIEW

10. CONTRIBUTION

### theory_and_knowledge_moves

1. THEORY_INTRO

2. THEORY_PROPOSITION

3. MECHANISM

4. THEORY_PROPOSITION

5. MECHANISM

6. THEORY_PROPOSITION

7. MECHANISM

8. THEORY_PROPOSITION

9. REQUIREMENT

10. REQUIREMENT

11. REQUIREMENT

12. DESIGN_FEATURE

13. HYPOTHESIS_OR_PROPOSITION

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. DESIGN_FEATURE

4. DESIGN_FEATURE

5. DESIGN_FEATURE

6. DESIGN_FEATURE

7. BENCHMARK_OR_CONTRAST

8. METHOD_JUSTIFICATION

9. DESIGN_FEATURE

10. DESIGN_FEATURE

11. DESIGN_FEATURE

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. RESULT

4. RESULT

5. RESULT

6. ROBUSTNESS_OR_BOUNDARY_TEST

7. RESULT

8. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. THEORY_PROPOSITION

3. CONTRIBUTION

4. BOUNDARY_CONDITION

5. CONTRIBUTION

6. BOUNDARY_CONDITION

7. LIMITATION_AND_FUTURE

8. LIMITATION_AND_FUTURE

9. LIMITATION_AND_FUTURE

10. CONTRIBUTION

## 理论/知识到设计的翻译

### 知识/理论基础

1. Theory of Least Collaborative Effort (TLCE)

2. Human-machine communication research / computers are social actors paradigm

3. Customer service chatbot literature (breakdown exploration, impact, and repair)

4. Adaptive user interfaces

5. Supervised machine learning for text classification

6. Service failure and recovery literature

- 理论—设计耦合：direct

- 耦合判定理由：TLCE-bot三原则被明确翻译为六条元需求、四组件元设计和可检验命题，设计实例中的分类器、修复消息和条件流程均由这些需求驱动，现场实验直接检验命题；不是事后用理论解释。

- 理论到设计翻译链：TLCE关于人类对话修复的三原则 → 通过与人类-机器沟通和客服聊天机器人文献的概念混合，得到TLCE-bot三原则（辅助性自我修复、诊断透明、成比例努力） → 每原则翻译为两条元需求（自修复优先、自修复辅助；故障诊断、故障透明；进展评估、渐进升级） → 元设计四组件（故障类型学、自适应修复类型、自适应修复消息、实时故障处理） → 在InsurCo的实例化（具体故障类型、具体修复消息、梯度提升分类器、Webhook与条件流程） → 用在线实验组件级验证，用现场实验整体验证。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：TLCE自修复偏好原则：人类偏好让说话者自己修复自己的麻烦源；但客服聊天机器人文献显示顾客常无法自行修复并需要辅助。

- mechanism_cn：顾客需要聊天机器人提供指导性辅助，而不是被抛入猜谜或独自试错。

- design_requirement_cn：自修复优先需求；自修复辅助需求。

- artifact_choice_cn：协助式顾客自修复（assisted customer self-repair）；修复消息包含解释和具体指导；第二次连续故障时增加规则式指导。

- evaluated_contrast_cn：在线实验中特定消息与通用消息对比；现场实验中协作式与“请重试”基线对比。

- objective_result_cn：在线实验意图识别分数显著提高；现场实验故障解决率提高、立即放弃率下降。

##### evidence_pointers

1. Design Episode 2在线实验

2. Field experiment Table 6 Models 1-2

#### 2. 2

- theory_or_knowledge_claim_cn：TLCE特异性原则：人类用尽可能具体的修复发起语定位麻烦源；但现有聊天机器人常用通用“请重试”消息。

- mechanism_cn：向顾客解释故障原因能帮助其更有效地自我修复，并提升对聊天机器人的理解。

- design_requirement_cn：故障诊断需求；故障透明需求。

- artifact_choice_cn：建立聊天机器人特定故障类型学；修复消息的解释元素（如“我有时难以处理长请求”）；梯度提升故障类型分类器。

- evaluated_contrast_cn：具体解释/指导消息 vs 通用消息；不同类型故障的修复效果差异。

- objective_result_cn：在线实验中具体消息提升意图识别；现场实验对elaborate、unique、brief类解决率提升，对cryptic类反而下降。

##### evidence_pointers

1. Table 3

2. Table 4

3. Field experiment breakdown type breakdown

#### 3. 3

- theory_or_knowledge_claim_cn：TLCE渐进升级原则：人类修复失败后会升级到更费力的修复类型；但现有机器人要么卡在重复重试，要么过早转人工。

- mechanism_cn：修复努力必须与故障严重程度和连续失败次数相称，避免顾客陷入循环或过早失去耐心。

- design_requirement_cn：进展评估需求；渐进升级需求。

- artifact_choice_cn：自适应修复类型组件考虑当前及先前故障类型；第一次故障采用协助式自修复，第二次某些组合升级指导，第三次后提供转人工；实时故障处理评估先前自修复尝试。

- evaluated_contrast_cn：现场实验中协作式条件（渐进升级）与非协作式基线（三次后才转人工）之间的行为结果。

- objective_result_cn：立即放弃率显著下降；负面反馈比例下降；但cryptic类无效，显示升级逻辑对某些故障失效。

##### evidence_pointers

1. Design Episode 2 Determination of Repair Types

2. Field experiment Table 6 Models 2-3

## 评价逻辑

### evaluation_modes

1. 聚类分析 + 人工编码验证（typology validation）

2. 受控在线实验（2×4组间设计，特定 vs 通用修复消息）

3. 机器学习算法基准测试（10算法比较 + 嵌套交叉验证）

4. 自然主义随机现场实验（logistic/OLS + 固定效应 + Heckman稳健性）

- why_these_evaluations_cn：DSR需要证据链支持，不能只靠单一实验。组件级在线实验先证明“具体消息优于通用消息”的因果有效性；分类器基准证明“实时诊断可部署”；完整现场实验证明“整个策略在真实情境中有效”。每个评价都对应设计中的一项或多项需求，并逐步增加生态效度。

- benchmark_and_contrast_chain_cn：在线实验以通用修复消息为基准，检验特定消息；分类器阶段以10种算法相互比较，选择性能和速度最优者；现场实验以InsurCo原有非协作策略为基准，比较完整协作策略。各基准层层递进：从消息层面的差异到系统层面的差异，再到真实场景中的端到端差异。

### claim_evidence_ledger

#### 1. 1

- claim：故障类型特定修复消息比通用消息帮助顾客更成功地自我修复。

- evidence：在线实验中特定消息组意图识别分数显著更高（M=0.611 vs 0.499, z=6.570, p<0.001）；对elaborate/unique/brief均显著。

- supported：strong

#### 2. 2

- claim：特定修复消息改善顾客对交互的主观评价。

- evidence：在线实验中满意度更高、挫败感更低、感知聊天机器人努力更高。

- supported：strong

#### 3. 3

- claim：协作式修复策略提高真实环境中的故障解决率。

- evidence：现场实验logit b=0.243, p=0.044, OR=1.274；解决率38.23% vs 32.41%。

- supported：strong

#### 4. 4

- claim：协作式修复策略减少顾客首次故障后立即放弃。

- evidence：现场实验logit b=-0.373, p=0.001, OR=0.689；放弃率41.68% vs 50.95%。

- supported：strong

#### 5. 5

- claim：协作式修复策略减少顾客对修复消息的负面反馈。

- evidence：现场实验logit b=-1.333, p=0.003, OR=0.264；Heckman稳健性结果相似。

- supported：strong

#### 6. 6

- claim：协作式修复策略提高整体满意度。

- evidence：现场实验OLS b=0.540, p=0.066；Heckman稳健性结果相似。

- supported：weak or marginal

#### 7. 7

- claim：实时故障分类器可实际支持修复策略。

- evidence：梯度提升准确率75.2%、F1 73.6%、预测时间0.004秒，并成功通过webhook集成。

- supported：strong

#### 8. 8

- claim：协作式策略对cryptic类故障也有效。

- evidence：现场实验中cryptic类解决率在协作条件下反而更低（-30.05%和-38.62%）。

- supported：contradicted; boundary condition

- internal_validity_strategy_cn：在线实验通过预定义对话、随机分配、操纵检验和只测量一次修复尝试来控制混淆；现场实验通过随机化、检验组间在设备/来源/故障概率/故障类型/时间上的平衡、加入控制变量和固定效应、保持响应时间相同，以及用Heckman模型处理反馈和满意度的自选偏差。

- external_validity_strategy_cn：作者选择真实企业聊天机器人、真实顾客消息、自然发生的故障和8周现场数据，并在系统层面完成真实集成，因此结果具有较高的自然主义生态效度；同时通过明确限定保险公司、德语、意图型聊天机器人来界定外推范围。

- what_is_not_actually_tested_cn：TLCE-bot机制（如顾客感受到辅助、理解故障原因、感知成比例努力）没有被直接测量；顾客“协作意愿”是从放弃率和解决率推断的；满意度效应仅在10%水平显著；完整策略的长期效应、对LLM/混合架构聊天机器人的适用性、跨语言泛化均未直接测试；分类器准确性对最终结果的中介作用也未直接分析。

## 贡献闭环

- technical_claim_cn：一个可部署的协作式修复系统（故障类型分类器+自适应修复消息+渐进升级流程）能够在真实意图型客服聊天机器人中运行，并在客观行为上优于通用“请重试”基线。

- artifact_claim_cn：故障类型特定且根据连续故障升级的修复消息是改进的主要原因；在线实验和现场实验共同支持组件-策略链条。

- mechanism_claim_cn：协作式策略通过辅助性自我修复、诊断透明和成比例努力三条机制提高了修复成功率和顾客保留，并减轻了负面情绪反应。

- boundary_claim_cn：效果集中体现在elaborate、unique、brief三类占90%以上的常见故障；对cryptic（无意义输入、外语）类故障无效，说明建立共同理解存在固有边界；结果来自德语保险情境，跨语言/LLM情境需再验证。

- reusable_design_knowledge_cn：可复用知识包括：TLCE-bot三原则；六条元需求；四组件元设计；修复消息道歉-解释-指导三要素模式；基于真实日志聚类建立故障类型学、用受控实验验证消息、再用监督学习实现实时诊断、最后现场检验的DSR设计旅程。

- theoretical_contribution_cn：将TLCE扩展为TLCE-bot，为顾客-聊天机器人交互提出三个新原则，扩展了原理论的使用范围；同时将服务交互叙事从对抗转向协作，并提示人-AI协作中权力关系可能走向AI担任更高角色。

- how_discussion_closes_intro_gap_cn：讨论部分明确回到引言提出的“修复负担落在单方”的缺口，指出协作式策略将顾客和机器人重新定位为沟通伙伴；用TLCE-bot三原则解释为什么协作有效；用现场证据回应“真实世界是否有效”的疑问；用cryptic类边界回应“是否需要更细分故障观”。

- overclaim_or_unsupported_leaps_cn：从“协作式策略”扩展到“人-AI协作权力关系”是较大理论跳跃，数据并未直接测量权力动态；将“降低放弃率”解读为“顾客愿意参与修复”是推断而非直接测量；满意度效应以10%显著作为“缓解负面结果”的证据略显勉强；作者从未直接测量顾客对“协作”本身的感知。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：越来越多组织部署AI聊天机器人以提供及时高效客服。

- rhetorical_function_cn：建立背景和产业趋势。

- depends_on_cn：无

- sets_up_cn：为后面指出聊天机器人仍会惹恼顾客做铺垫。

- evidence_pointer：Introduction P1

### 2. P1 S2-S3

- order：2

- section：Introduction

- locator：P1 S2-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：虽然市场增长快，但大量美国顾客认为聊天机器人令人沮丧和浪费时间。

- rhetorical_function_cn：说明问题的现实严重性和实践后果。

- depends_on_cn：部署趋势背景

- sets_up_cn：为“故障是造成挫败感的重要来源”做铺垫。

- evidence_pointer：Introduction P1

### 3. P2 S1

- order：3

- section：Introduction

- locator：P2 S1

- move_code：PHENOMENON

- paraphrase_cn：最让顾客沮丧的是聊天机器人无法理解请求，即对话故障。

- rhetorical_function_cn：将一般挫败感聚焦到具体经验现象。

- depends_on_cn：前文对聊天机器人问题的描述

- sets_up_cn：为本研究定义核心对象。

- evidence_pointer：Introduction P2

### 4. P2 S2

- order：4

- section：Introduction

- locator：P2 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究表明对话故障扰乱交互流程，导致放弃、不满和负面口碑。

- rhetorical_function_cn：引用既有证据确立故障后果。

- depends_on_cn：现象定义

- sets_up_cn：说明为什么要关注修复策略。

- evidence_pointer：Introduction P2

### 5. P2 S3

- order：5

- section：Introduction

- locator：P2 S3

- move_code：LIMITATION

- paraphrase_cn：自然语言的复杂和歧义使预防故障几乎不可能。

- rhetorical_function_cn：指出预防性方案的局限。

- depends_on_cn：故障不可避免的认知

- sets_up_cn：引出修复策略的必要性。

- evidence_pointer：Introduction P2

### 6. P2 S4

- order：6

- section：Introduction

- locator：P2 S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：研究者和实践者开始意识到修复策略的重要性。

- rhetorical_function_cn：介绍已有知识共识。

- depends_on_cn：故障不可避免的局限

- sets_up_cn：进入文献回顾的入口。

- evidence_pointer：Introduction P2

### 7. P3 S1

- order：7

- section：Introduction

- locator：P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：服务失败与聊天机器人设计交叉的研究正在发展，试图理解故障并评价修复策略。

- rhetorical_function_cn：概述相关研究积累。

- depends_on_cn：修复策略重要性的陈述

- sets_up_cn：随后指出该研究的盲点。

- evidence_pointer：Introduction P3

### 8. P3 S2

- order：8

- section：Introduction

- locator：P3 S2

- move_code：LIMITATION

- paraphrase_cn：但文献回顾发现现有修复策略主要把修复负担放在顾客或聊天机器人单方。

- rhetorical_function_cn：指出核心局限。

- depends_on_cn：对已有研究的概括

- sets_up_cn：建立研究缺口的基础。

- evidence_pointer：Introduction P3; Appendix A

### 9. P3 S3

- order：9

- section：Introduction

- locator：P3 S3

- move_code：MECHANISM

- paraphrase_cn：顾客驱动策略通常让聊天机器人要求顾客重复或改述，结果顾客陷入试错循环。

- rhetorical_function_cn：解释单方修复策略为何失败。

- depends_on_cn：对顾客驱动策略的定义

- sets_up_cn：为论证协作策略必要性提供机制。

- evidence_pointer：Introduction P3

### 10. P3 S4

- order：10

- section：Introduction

- locator：P3 S4

- move_code：MECHANISM

- paraphrase_cn：聊天机器人驱动策略常在不承认故障的情况下猜最可能答案，猜错则反噬。

- rhetorical_function_cn：解释聊天机器人驱动策略的失败机制。

- depends_on_cn：对聊天机器人驱动策略的定义

- sets_up_cn：共同造成猜谜游戏印象。

- evidence_pointer：Introduction P3

### 11. P3 S5

- order：11

- section：Introduction

- locator：P3 S5

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：两种策略都把交互变成顾客猜机器人能懂什么、或机器人猜顾客什么意思的猜谜游戏。

- rhetorical_function_cn：说明现有方案的后果，强化缺口重要性。

- depends_on_cn：前两条机制

- sets_up_cn：为“协作”叙事提供对比。

- evidence_pointer：Introduction P3

### 12. P3 S6

- order：12

- section：Introduction

- locator：P3 S6

- move_code：GAP

- paraphrase_cn：虽有迹象表明顾客愿意与机器人协作修复，但我们对如何设计协作式修复策略、以及它在真实环境中是否更有效知之甚少。

- rhetorical_function_cn：明确提出研究缺口。

- depends_on_cn：对现有策略局限和有限迹象的总结

- sets_up_cn：引出本文研究目标。

- evidence_pointer：Introduction P3

### 13. P4 S1

- order：13

- section：Introduction

- locator：P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文研究真实顾客-聊天机器人交互中协作式修复策略的设计与影响。

- rhetorical_function_cn：直接陈述研究问题/目标。

- depends_on_cn：缺口

- sets_up_cn：预告后续方法。

- evidence_pointer：Introduction P4

### 14. P4 S2-S4

- order：14

- section：Introduction

- locator：P4 S2-S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：遵循DSR范式，基于TLCE与人机沟通/客服聊天机器人文献提出设计，与InsurCo合作实例化，并通过三阶段设计过程和随机现场实验评价。

- rhetorical_function_cn：给出研究路线和方法预告。

- depends_on_cn：研究目标

- sets_up_cn：为正文结构做路标。

- evidence_pointer：Introduction P4

### 15. P4 S5

- order：15

- section：Introduction

- locator：P4 S5

- move_code：RESULT

- paraphrase_cn：现场实验显示协作式策略提高顾客参与修复意愿、增加故障解决并减轻负面顾客结果。

- rhetorical_function_cn：提前给出核心结果，吸引读者并建立预期。

- depends_on_cn：研究路线

- sets_up_cn：为贡献声明提供证据基础。

- evidence_pointer：Introduction P4

### 16. P5 S1-S4

- order：16

- section：Introduction

- locator：P5 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：贡献包括转换叙事为协作、扩展TLCE为TLCE-bot、提供真实世界证据、给出设计处方。

- rhetorical_function_cn：提前声明四类贡献。

- depends_on_cn：结果

- sets_up_cn：讨论部分将依次兑现这些贡献。

- evidence_pointer：Introduction P5

### 17. Chatbot Breakdown and Repair Strategies, last paragraph

- order：17

- section：Related Literature

- locator：Chatbot Breakdown and Repair Strategies, last paragraph

- move_code：GAP

- paraphrase_cn：指出三个知识缺口：缺乏协作策略设计知识、缺乏真实场景影响证据、故障观过于单维。

- rhetorical_function_cn：系统性地从文献分类中提炼缺口。

- depends_on_cn：四个文献类别回顾

- sets_up_cn：为DSR方法和理论驱动设计提供理由。

- evidence_pointer：Related Literature, final paragraph

### 18. Opening paragraphs

- order：18

- section：A Theory-Driven Design for Collaborative Repair Strategies

- locator：Opening paragraphs

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：本文遵循DSR范式，研究一类问题而非单个实例，并选择Walls et al.架构组织。

- rhetorical_function_cn：说明方法论选择及其与问题类别的匹配。

- depends_on_cn：之前识别的问题类别

- sets_up_cn：为内核理论-元需求-元设计-命题的结构做框架性说明。

- evidence_pointer：Theory-Driven Design section

### 19. First three paragraphs

- order：19

- section：Kernel Theory

- locator：First three paragraphs

- move_code：THEORY_INTRO

- paraphrase_cn：选择人类沟通理论作为内核理论，因为人们会把社交脚本应用到机器交互中。

- rhetorical_function_cn：给理论选择提供合理性与出处。

- depends_on_cn：DSR对内核理论的要求

- sets_up_cn：为引入TLCE做铺垫。

- evidence_pointer：Kernel Theory section

### 20. First paragraph

- order：20

- section：Theory of Least Collaborative Effort (TLCE)

- locator：First paragraph

- move_code：THEORY_PROPOSITION

- paraphrase_cn：TLCE认为人类沟通是协作活动，人们最小化的是双方共同付出的努力。

- rhetorical_function_cn：给出TLCE核心命题。

- depends_on_cn：理论选择

- sets_up_cn：为后续三原则做定义基础。

- evidence_pointer：TLCE subsection

### 21. Paragraph on principle 1

- order：21

- section：Theory of Least Collaborative Effort (TLCE)

- locator：Paragraph on principle 1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：原则一：人类偏好自我修复而非他人修复。

- rhetorical_function_cn：陈述TLCE第一个原则。

- depends_on_cn：TLCE核心命题

- sets_up_cn：之后与客服聊天机器人情境对比。

- evidence_pointer：TLCE subsection

### 22. Paragraph on principle 2

- order：22

- section：Theory of Least Collaborative Effort (TLCE)

- locator：Paragraph on principle 2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：原则二：人类倾向于选择最具体的修复发起语以最小化协作努力。

- rhetorical_function_cn：陈述TLCE第二个原则。

- depends_on_cn：TLCE核心命题

- sets_up_cn：与聊天机器人常见通用消息形成对照。

- evidence_pointer：TLCE subsection

### 23. Paragraph on principle 3

- order：23

- section：Theory of Least Collaborative Effort (TLCE)

- locator：Paragraph on principle 3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：原则三：修复失败后人类会增量升级到更费力的修复类型。

- rhetorical_function_cn：陈述TLCE第三个原则。

- depends_on_cn：TLCE核心命题

- sets_up_cn：与聊天机器人“循环重试或过早转人工”对比。

- evidence_pointer：TLCE subsection

### 24. First paragraph

- order：24

- section：TLCE-bot

- locator：First paragraph

- move_code：MECHANISM

- paraphrase_cn：作者使用概念混合方法整合TLCE与人机沟通、客服聊天机器人文献，以识别领域差异。

- rhetorical_function_cn：说明从原理论到TLCE-bot的“概念跳跃”。

- depends_on_cn：三原则和领域文献

- sets_up_cn：为三个新原则的提出提供方法依据。

- evidence_pointer：TLCE-bot subsection

### 25. Principle 1 paragraph

- order：25

- section：TLCE-bot

- locator：Principle 1 paragraph

- move_code：THEORY_PROPOSITION

- paraphrase_cn：提出辅助性自我修复原则：顾客需要且欢迎机器人在自我修复中提供帮助。

- rhetorical_function_cn：将TLCE原则改写为面向机器人的原则。

- depends_on_cn：概念混合中的发现

- sets_up_cn：引出自修复优先和自修复辅助两条元需求。

- evidence_pointer：TLCE-bot section

### 26. Principle 2 paragraph

- order：26

- section：TLCE-bot

- locator：Principle 2 paragraph

- move_code：THEORY_PROPOSITION

- paraphrase_cn：提出诊断透明原则：机器人提供故障成因信息有助于顾客修复。

- rhetorical_function_cn：改写特异性原则为透明化要求。

- depends_on_cn：特异性原则与聊天机器人领域差异

- sets_up_cn：引出故障诊断和故障透明两条元需求。

- evidence_pointer：TLCE-bot section

### 27. Principle 3 paragraph

- order：27

- section：TLCE-bot

- locator：Principle 3 paragraph

- move_code：THEORY_PROPOSITION

- paraphrase_cn：提出成比例努力原则：修复所需努力应与故障严重程度对应。

- rhetorical_function_cn：改写增量升级原则以适应机器人情境。

- depends_on_cn：增量升级原则与客服机器人困境

- sets_up_cn：引出进展评估和渐进升级两条元需求。

- evidence_pointer：TLCE-bot section

### 28. First paragraph

- order：28

- section：Meta-Requirements

- locator：First paragraph

- move_code：REQUIREMENT

- paraphrase_cn：将TLCE-bot三原则翻译成六条元需求，每原则对应两条。

- rhetorical_function_cn：完成理论到设计空间的转换。

- depends_on_cn：TLCE-bot三原则

- sets_up_cn：作为元设计必须满足的功能清单。

- evidence_pointer：Meta-Requirements section

### 29. Requirement paragraphs for assisted self-repair

- order：29

- section：Meta-Requirements

- locator：Requirement paragraphs for assisted self-repair

- move_code：REQUIREMENT

- paraphrase_cn：协作式修复策略应保留顾客自修复机会，并全程提供辅助。

- rhetorical_function_cn：把辅助性自我修复原则转成可设计要求。

- depends_on_cn：原则一

- sets_up_cn：为自适应修复类型和消息组件提供依据。

- evidence_pointer：Meta-Requirements section

### 30. Requirement paragraphs for diagnostic transparency

- order：30

- section：Meta-Requirements

- locator：Requirement paragraphs for diagnostic transparency

- move_code：REQUIREMENT

- paraphrase_cn：协作策略应实时诊断最可能故障原因，并给出尽可能具体的成因信息。

- rhetorical_function_cn：把诊断透明原则转成可设计要求。

- depends_on_cn：原则二

- sets_up_cn：为故障类型学和修复消息解释元素提供依据。

- evidence_pointer：Meta-Requirements section

### 31. Requirement paragraphs for proportionate effort

- order：31

- section：Meta-Requirements

- locator：Requirement paragraphs for proportionate effort

- move_code：REQUIREMENT

- paraphrase_cn：协作策略应监测进展并渐进升级，直到解决或转交人工。

- rhetorical_function_cn：把成比例努力原则转成可设计要求。

- depends_on_cn：原则三

- sets_up_cn：为自适应修复类型和实时故障处理组件提供依据。

- evidence_pointer：Meta-Requirements section

### 32. Opening paragraph

- order：32

- section：Meta-Design

- locator：Opening paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：元设计包含四组件：故障类型学、自适应修复类型、自适应修复消息、实时故障处理。

- rhetorical_function_cn：给出完整设计蓝图。

- depends_on_cn：六条元需求

- sets_up_cn：后文逐组件阐述并实例化。

- evidence_pointer：Meta-Design section

### 33. Breakdown Typology paragraph

- order：33

- section：Meta-Design / Breakdown Typology

- locator：Breakdown Typology paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：用聊天日志和聚类建立机器人特定故障类型学，为诊断和透明提供基础。

- rhetorical_function_cn：描述第一个组件及其方法。

- depends_on_cn：诊断透明相关需求

- sets_up_cn：为设计片段1的聚类分析提供设计蓝图。

- evidence_pointer：Meta-Design, Breakdown Typology

### 34. Adaptive Repair Types paragraph

- order：34

- section：Meta-Design / Adaptive Repair Types

- locator：Adaptive Repair Types paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：修复类型随故障类型和先前故障历史调整，从低努力自修复到高努力转人工。

- rhetorical_function_cn：描述第二个组件及自适应逻辑。

- depends_on_cn：自修复优先/辅助需求、进展评估、渐进升级

- sets_up_cn：为设计片段2的定义修复类型工作提供蓝图。

- evidence_pointer：Meta-Design, Adaptive Repair Types

### 35. Adaptive Repair Messages paragraph and Table 1

- order：35

- section：Meta-Design / Adaptive Repair Messages

- locator：Adaptive Repair Messages paragraph and Table 1

- move_code：DESIGN_FEATURE

- paraphrase_cn：修复消息由道歉、解释、指导三要素组成，替代通用消息。

- rhetorical_function_cn：描述第三个组件及其消息模式。

- depends_on_cn：透明需求、辅助需求

- sets_up_cn：为设计片段2的具体消息撰写和在线实验提供依据。

- evidence_pointer：Meta-Design, Adaptive Repair Messages; Table 1

### 36. Real-Time Breakdown Handling paragraph

- order：36

- section：Meta-Design / Real-Time Breakdown Handling

- locator：Real-Time Breakdown Handling paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：实时组件负责分类故障、评估先前修复尝试、选择适配修复类型和消息。

- rhetorical_function_cn：描述第四个组件的运行时逻辑。

- depends_on_cn：诊断、进展评估、渐进升级需求

- sets_up_cn：为设计片段3的分类器和Web应用提供蓝图。

- evidence_pointer：Meta-Design, Real-Time Breakdown Handling

### 37. Testable Propositions paragraph

- order：37

- section：Testable Propositions

- locator：Testable Propositions paragraph

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：评估应检验协作策略能否解决故障、能否减轻故障对顾客结果的负面影响，并与基线比较。

- rhetorical_function_cn：将设计目标转化为可评价命题。

- depends_on_cn：元设计

- sets_up_cn：为在线实验和现场实验的指标预先确定。

- evidence_pointer：Testable Propositions section

### 38. Episode 1, first two paragraphs

- order：38

- section：Design Episode 1

- locator：Episode 1, first two paragraphs

- move_code：RESULT

- paraphrase_cn：基于21,736条真实消息，对5,668条故障消息聚类得到四类故障，并用人工编码验证。

- rhetorical_function_cn：报告第一个设计片段的结果。

- depends_on_cn：故障类型学组件蓝图

- sets_up_cn：为第二片段提供输入分类。

- evidence_pointer：Design Episode 1 section

### 39. Determination of Repair Types paragraph

- order：39

- section：Design Episode 2

- locator：Determination of Repair Types paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：与InsurCo研讨确定：首次故障用协助式自修复，第三次故障后提供人工转接，第二次根据故障组合决定升级方式。

- rhetorical_function_cn：说明修复类型具体如何实例化。

- depends_on_cn：自适应修复类型设计

- sets_up_cn：为现场实验条件流程提供规则。

- evidence_pointer：Design Episode 2, Determination of Repair Types

### 40. Formulation and Refinement of Repair Messages; main experiment

- order：40

- section：Design Episode 2

- locator：Formulation and Refinement of Repair Messages; main experiment

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：在受控在线实验中比较故障类型特定消息与通用消息，采用2×4组间设计。

- rhetorical_function_cn：建立组件级对照评价。

- depends_on_cn：修复消息模式

- sets_up_cn：为具体消息的有效性提供证据。

- evidence_pointer：Design Episode 2, main experiment

### 41. Results paragraphs

- order：41

- section：Design Episode 2

- locator：Results paragraphs

- move_code：RESULT

- paraphrase_cn：特定消息显著提高了意图识别得分并改善满意度、挫败感和感知努力。

- rhetorical_function_cn：报告组件级实验结果。

- depends_on_cn：在线实验设计

- sets_up_cn：为后续现场部署提供信心。

- evidence_pointer：Design Episode 2, Results; Table 4

### 42. Breakdown Type Classifier and model selection

- order：42

- section：Design Episode 3

- locator：Breakdown Type Classifier and model selection

- move_code：RESULT

- paraphrase_cn：梯度提升在10种算法中表现最佳，得到75.2%准确率和0.004秒预测时间。

- rhetorical_function_cn：报告分类器选择结果。

- depends_on_cn：人工标注训练数据和算法比较

- sets_up_cn：确认实时诊断组件可实现。

- evidence_pointer：Design Episode 3, Breakdown Type Classifier; Appendix C

### 43. Web Application and Integration paragraphs

- order：43

- section：Design Episode 3

- locator：Web Application and Integration paragraphs

- move_code：DESIGN_FEATURE

- paraphrase_cn：开发Flask Web应用，通过webhook与InsurCo聊天机器人后端通信并触发超过20条条件流程。

- rhetorical_function_cn：描述系统集成方式。

- depends_on_cn：分类器

- sets_up_cn：为现场实验系统可用性做铺垫。

- evidence_pointer：Design Episode 3, Web Application; Figure 4

### 44. Experimental Design paragraph

- order：44

- section：Naturalistic Summative Evaluation

- locator：Experimental Design paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择自然主义总结性随机现场实验，以真实顾客和真实故障比较协作与非协作策略。

- rhetorical_function_cn：说明为何用现场实验作为评估方法。

- depends_on_cn：系统集成完成

- sets_up_cn：为结果报告设定证据标准。

- evidence_pointer：Naturalistic Summative Evaluation, Experimental Design

### 45. Data and Randomization Checks paragraph

- order：45

- section：Naturalistic Summative Evaluation

- locator：Data and Randomization Checks paragraph

- move_code：RESULT

- paraphrase_cn：随机化检验显示两组在设备、来源、故障发生概率、故障类型分布和时间分布上无系统差异。

- rhetorical_function_cn：支持现场实验的内部有效性。

- depends_on_cn：随机化程序

- sets_up_cn：使后面的因果推断更可信。

- evidence_pointer：Naturalistic Summative Evaluation, Data and Randomization Checks

### 46. Breakdown resolution paragraph

- order：46

- section：Naturalistic Summative Evaluation

- locator：Breakdown resolution paragraph

- move_code：RESULT

- paraphrase_cn：协作式策略显著提高故障解决率，logit模型显示正向效应。

- rhetorical_function_cn：报告第一项核心行为结果。

- depends_on_cn：随机现场实验数据

- sets_up_cn：支持可检验命题一。

- evidence_pointer：Breakdown resolution paragraph; Table 6 Model 1

### 47. Immediate abandonment paragraph

- order：47

- section：Naturalistic Summative Evaluation

- locator：Immediate abandonment paragraph

- move_code：RESULT

- paraphrase_cn：协作式策略显著降低首故障后立即放弃率。

- rhetorical_function_cn：报告第二项行为结果，进一步支持命题一。

- depends_on_cn：现场数据

- sets_up_cn：为“提高参与修复意愿”提供推断。

- evidence_pointer：Immediate abandonment paragraph; Table 6 Model 2

### 48. Customer feedback paragraph

- order：48

- section：Naturalistic Summative Evaluation

- locator：Customer feedback paragraph

- move_code：RESULT

- paraphrase_cn：协作式策略显著降低顾客对修复消息的负面反馈，Heckman稳健性检验相似。

- rhetorical_function_cn：报告第一项主观结果，支持命题二。

- depends_on_cn：现场数据

- sets_up_cn：为“缓解负面后果”提供证据。

- evidence_pointer：Customer feedback paragraph; Table 6 Model 3

### 49. Customer satisfaction paragraph

- order：49

- section：Naturalistic Summative Evaluation

- locator：Customer satisfaction paragraph

- move_code：RESULT

- paraphrase_cn：协作式策略提高满意度，但只在10%水平显著，Heckman稳健性相似。

- rhetorical_function_cn：报告第二项主观结果，同时暴露样本量限制。

- depends_on_cn：现场数据

- sets_up_cn：使结论更谨慎，并支持边界讨论。

- evidence_pointer：Customer satisfaction paragraph; Table 6 Model 4

### 50. First paragraph summary

- order：50

- section：Discussion

- locator：First paragraph summary

- move_code：CONTRIBUTION

- paraphrase_cn：总结研究问题、理论、设计旅程和现场结果，并称实现了“最后一公里”价值。

- rhetorical_function_cn：把全文重新收束为一项完整DSR贡献。

- depends_on_cn：所有设计片段和现场结果

- sets_up_cn：进入研究含义。

- evidence_pointer：Discussion, first paragraph

### 51. Second paragraph about narrative shift

- order：51

- section：Discussion / Implications for Research

- locator：Second paragraph about narrative shift

- move_code：THEORY_PROPOSITION

- paraphrase_cn：现有文献将顾客与机器人视为对手，本研究将其视为合作解决问题的伙伴，并提示人-AI权力动态可能改变。

- rhetorical_function_cn：提出理论视角转变，强化理论贡献。

- depends_on_cn：现场结果与“协作”框架

- sets_up_cn：为TLCE-bot扩展做铺垫。

- evidence_pointer：Discussion, Implications for Research

### 52. Second contribution paragraph

- order：52

- section：Discussion / Implications for Research

- locator：Second contribution paragraph

- move_code：THEORY_PROPOSITION

- paraphrase_cn：简单将“人”换成“机器人”不足以解释聊天机器人互动中的独特挑战，TLCE-bot扩展了原理论范围。

- rhetorical_function_cn：明确TLCE-bot的理论贡献。

- depends_on_cn：理论整合部分

- sets_up_cn：为实践贡献和边界讨论提供概念基础。

- evidence_pointer：Discussion, Implications for Research

### 53. Third contribution paragraph

- order：53

- section：Discussion / Implications for Research

- locator：Third contribution paragraph

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：协作策略对最常见故障类型有效，但对cryptic类无意义输入或外语故障无效，显示协作修复的内在边界。

- rhetorical_function_cn：在贡献中同时报告边界条件。

- depends_on_cn：现场实验按类型分解的结果

- sets_up_cn：促使未来研究关注LLM和跨语言情境。

- evidence_pointer：Discussion, third contribution paragraph

### 54. Practice implications paragraphs

- order：54

- section：Discussion / Implications for Practice

- locator：Practice implications paragraphs

- move_code：CONTRIBUTION

- paraphrase_cn：为实践者提供元设计、制品和实施细节作为可遵循蓝图，并推广到其他人类-AI协作领域。

- rhetorical_function_cn：将设计知识转化为实践行动建议。

- depends_on_cn：DSR评价证据

- sets_up_cn：增强现实相关性，回应“最后一公里”。

- evidence_pointer：Discussion, Implications for Practice

### 55. Limitations paragraphs

- order：55

- section：Discussion / Limitations and Future Research

- locator：Limitations paragraphs

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限性包括单一保险公司意图型德语聊天机器人、故障类型学可能跨语言不适用、未来可探索LLM和预防性反馈。

- rhetorical_function_cn：划定结果边界并指引未来研究方向。

- depends_on_cn：已有结果与边界条件

- sets_up_cn：弱化过度泛化风险，同时保留研究重要性。

- evidence_pointer：Discussion, Limitations and Future Research

### 56. Final paragraph

- order：56

- section：Discussion / Conclusion

- locator：Final paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：总结协作式修复策略对顾客和组织都有益，并重申对顾客-AI服务互动的新思考方式。

- rhetorical_function_cn：以贡献性声明收束全文。

- depends_on_cn：所有证据和理论讨论

- sets_up_cn：给读者留下最终印象。

- evidence_pointer：Discussion, final paragraph

## 写作技术

- gap_construction_cn：作者不采用“没人研究”型缺口，而是通过文献分类（故障探索、故障影响、修复策略探索、修复策略影响）反复指出“现有修复策略把负担放在单方”，再引用Ashktorab等人对协作策略的偏好证据，制造“有迹象但无设计”的缺口；同时强调真实场景缺失和故障观单维，形成三缺口叠加。

- signposting_cn：引言末尾给出全文结构；每个理论原则都先陈述原TLCE原则，再概念混合，最后形成TLCE-bot原则；每个设计片段开头明确该片段要实例化的组件；DSR章节反复使用“首先…其次…最后…”等路标。

- transition_logic_cn：阶段间采用“前一片段产出作为下一片段输入”的递进逻辑；例如故障类型学为修复消息提供基础，修复消息为条件流程提供内容，实时处理使系统可运行，最后用现场实验验证完整系统；断点处都明确指出尚不确定的问题。

- claim_evidence_rhythm_cn：每个机制主张后都配有对应的组件选择；每个组件选择后都配有组件级或系统级证据；现场实验按命题组织四个模型，先报告客观行为结果再报告主观评价结果，始终保持主张-证据交替。

- benchmark_narrative_cn：基准不是单一基准而是层层升级：在线实验中用通用消息作为消息组件基准；分类器用10个算法互比；现场实验用InsurCo既有非协作策略作为系统级真实基准，从而让读者看到每层设计都比对照组更好。

- theory_return_cn：现场结果没有停留在“效果好”，而是回到TLCE-bot三原则解释为什么效果好，并用cryptic类反例说明原则的边界，最终把经验结果转化为理论扩展和适用范围限定。

- contribution_positioning_cn：引言先预告四类贡献，结论再逐条兑现；在讨论中把贡献置于服务失败、聊天机器人设计、人类-AI协作三股文献的交汇处，并将“从对抗到协作”作为更高层的理论叙事。

- novelty_protection_cn：作者用TLCE-bot的命名和三条新原则标定理论新颖性；用真实企业现场实验和自然故障数据标定经验新颖性；用四个组件和“最后一公里”实现标定制品的可落地性；用不同故障类型的效果反差防止贡献被视为无条件的性能改进。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：写出现实中的反复性失败现象，并用市场数据/customer experience数据说明代价。

- research_job_cn：选择一个实践问题类别（如服务故障），并确认它普遍存在且后果严重。

- required_evidence_cn：能说明问题普遍性和负面后果的数据或文献。

- transition_to_next_cn：从“问题普遍且后果严重”过渡到“现有方案为何不足”。

#### 2. 2

- step：2

- writing_job_cn：通过文献分类梳理现有策略，指出其共同局限，并留下一个具体空白。

- research_job_cn：系统回顾相关文献，尤其是有无“协作”迹象但无设计证据的线索。

- required_evidence_cn：显示现有策略单一化或缺少真实场景的文献证据。

- transition_to_next_cn：从缺口过渡到“用DSR方法解决”。

#### 3. 3

- step：3

- writing_job_cn：选择合适的内核理论，并通过概念混合或类比将其适配到目标情境。

- research_job_cn：确认理论有解释力，同时寻找目标情境与该理论的差异点。

- required_evidence_cn：至少列出理论原则与情境证据的对应和偏移。

- transition_to_next_cn：把适配后的理论原则翻译为设计要求。

#### 4. 4

- step：4

- writing_job_cn：将每个理论原则转化为两条元需求，再以需求清单指导元设计。

- research_job_cn：逐条推导需求，并设计出满足需求的组件集合。

- required_evidence_cn：每个组件都能溯源到至少一条元需求。

- transition_to_next_cn：说明仅靠一个组件不够，需要一个系统方案。

#### 5. 5

- step：5

- writing_job_cn：按设计片段逐组件实例化，并给每个片段安排小规模验证。

- research_job_cn：用真实日志、工作坊、受控实验或模型基准分别验证各组件。

- required_evidence_cn：每个组件都有至少一种有效性或可实现性证据。

- transition_to_next_cn：从组件验证过渡到完整系统集成与现场评价。

#### 6. 6

- step：6

- writing_job_cn：用随机现场实验或自然主义评价检验完整系统，报告客观行为与主观结果。

- research_job_cn：设计随机对照，控制混淆，使用回归/固定效应/稳健性检验。

- required_evidence_cn：至少一个客观行为指标显著，并有稳健性检验。

- transition_to_next_cn：从实验结果过渡到理论扩展和边界。

#### 7. 7

- step：7

- writing_job_cn：将结果回写为理论贡献、边界条件和实践处方。

- research_job_cn：识别哪些结果支持/挑战原理论，哪些条件限制推广，哪些知识可复用。

- required_evidence_cn：必须用数据中的异质性或反例来界定边界。

- transition_to_next_cn：以研究含义和未来路径收束。

### most_transferable_moves_cn

1. 用文献分类制造“有迹象但无设计”的缺口

2. 用概念混合将人际沟通理论改编为AI交互情境的TLCE-bot

3. 将理论原则逐条翻译为元需求，并让每个设计组件可溯源

4. 使用“设计片段”概念组织迭代开发，而不是一次构建完整系统

5. 先用受控实验验证组件，再用现场实验验证完整系统

6. 在贡献叙事中同时报告效应和按故障类型分解的反例

### resource_intensive_or_nonstandard_parts_cn

1. 与大型企业InsurCo的深度合作与真实聊天机器人接入

2. 数万条真实交互日志和五万多条故障消息

3. 真实环境中的8周随机现场实验

4. 多轮受控在线实验和人工编码标注

5. 自定义Web应用、分类器和超过20条条件流程的系统集成

### what_not_to_copy_superficially_cn

1. 不能只写“协作式修复”而不展示具体消息和分类机制

2. 不能只套用TLCE术语而不做概念混合的差异分析

3. 不能只用实验室实验断言真实世界有效

4. 不能只报告整体效果而不检查不同故障类型的异质性

5. 不能把“愿意参与修复”直接等同于实际测量的协作意愿

- single_best_description_of_the_routine_cn：从一个双方互相猜谜的实践缺口出发，借人类会话修复理论完成“概念跳跃”，生成可操作设计和测试命题，再以真实企业为试验场，用组件级受控实验和自然主义现场实验两级验证，最后把结果回写为理论扩展和边界条件。

## 分析边界

全文已完整提供，但论文没有逐页页码，句子定位基于章节、段落和表格；初始问题空间探索阶段在正文中只被引用而未详述；附录A为超大文献表，部分信息来自该表而非正文；受控实验中cryptic类型差异仅10%显著、现场满意度模型仅10%显著，需在解读时注意。
