# Multi-Party Certification on Blockchain and Its Impact in the Market for Lemons

- 作者：Ingrid Bauer; José Parra-Moyano; Karl Schmedders; Gerhard Schwabe
- 年份 / 期刊：2022 / Journal of Management Information Systems
- DOI：10.1080/07421222.2022.2063555
- 源文件：25476_2022_multi-party-certification-on-blockchain-and-its-impact-in-the-market-for-lemons.md
- 论文主类型：multi_method_or_multi_study_program
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.78

## 文章级论证概况

- 核心问题：多主体认证（multi-party certification）如何影响柠檬市场？即区块链支持的多方认证是否让经销商能够发送与不可观测质量更相关的信号，并由此改善信息不对称下的市场结果。

- 制品与设计：核心制品是区块链支持的多主体产品历史证书（multi-party certification），实验中被操作化为CarCerti，一个模拟Cardossier区块链系统的信息界面，向买卖双方提供经多方维护、可溯源且难以伪造的车辆维修保养历史和驾驶动态信息；与之对照的是仅由经销商/单一第三方提供的传统信号。

- 客观结果：实验室市场实验显示，与无多主体认证的Instance A相比，有CarCerti的Instance B中经销商初始要价平均降低1832美元，成交价平均降低1556美元；经销商平均相对收益从0.1866降至0.0429，买家平均相对收益从-0.1866改善至-0.0429；peach成交占比从0.08升至0.34，lemon成交占比从0.56降至0.30，所有检验均显著支持H1、H2、H2.1、H2.2和H3。

- 核心贡献：作者声称通过社会技术工件视角和形式模型，首次将区块链多主体认证与信号fit概念连接，并提供了实验室证据表明多主体认证能使经销商发送更高拟合信号，减少信息不对称、降低系统熵、改善商品配置并提高市场公平性。

- 整篇论证链：文章从柠檬市场的经典信息不对称问题出发，指出现有经销商信号虽能防止市场崩溃，但市场仍显著偏离最优：买家过度支付、经销商抽取大部分收益、好车卖家退出。随后引入区块链作为可信、去中心化资产文档化的技术基础，并采用社会技术工件框架，将多主体认证定义为多个独立方以可信方式记录资产历史；作者论证区块链的去中心化、通证化、数据溯源和激励机制使经销商获得发送更高fit信号的行动潜力。为了把这种行动潜力转化为市场预测，作者在Levin模型基础上建立连续质量空间的解析模型，用更窄的价值支持区间表示高fit信号，证明高fit信号降低熵、扩大交易区间并缩小价格范围；由此推导出H1-H3关于初始要价、成交价、相对收益和peach/lemon配置的假设。随后通过CarMarket实验室市场游戏，在105名被试（各扮演买卖双方共210个用户）中进行A/B被试间实验，Instance A只含经销商信号，Instance B增加CarCerti多主体认证；统计检验支持全部假设。讨论部分将结果重新连接到社会技术框架、信号理论和熵概念，提出高fit信号的三重来源（分散信息、可溯源、激励兼容）以及区块链作为当前唯一能够同时实现去中心化协作和数字所有权独占的技术，并在此基础上提出对经销商中介模式、系统融资和监管政策的启示。

## 类型与写作弧线判定

- 论文主类型判定：文章不是单一设计科学构建或纯解析模型，而是依次完成概念/构念化（社会技术工件分析）、解析经济模型（推出命题与假设）、实验室市场实验（操作化两种信息结构）和理论讨论。方法跨度包括理论综述、数学建模与受控实验，属于多方法、多阶段累积论证。

- 主导写作弧线判定：全文以柠檬市场问题开篇，引入信号理论和社会技术框架，通过解析模型和假设形成理论预测，再设计CarMarket/CarCerti实验进行检验，最后在讨论中将经验结果带回熵、信号fit和社会技术系统理论，完成问题—理论—设计—检验—返回理论的闭环。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第一阶段通过文献和社会技术框架定义多主体认证并论证其可产生高fit信号；第二阶段用解析模型把高fit信号参数化为更窄价值支持区间，推导出交易可行性和价格区间命题；第三阶段将模型预测结合锚定效应文献转化为H1-H3假设；第四阶段设计并运行CarMarket/CarCerti实验室市场实验，生成A/B数据；第五阶段对数据进行统计检验，支持全部假设；第六阶段在讨论中把实证结果提升为机制解释、边界条件、设计知识和理论贡献。六个阶段不是并列的Study，而是从构念、预测、操作化、证据到理论回报的累积链条。

### studies_or_phases

#### 1. 社会技术构念化：界定多主体认证与高fit信号

- order：1

- name_cn：社会技术构念化：界定多主体认证与高fit信号

- question_cn：什么是多主体认证？为什么区块链能使经销商发送比现有信号更贴近不可观测质量的信号？

- inputs_and_setting_cn：既有柠檬市场与信号文献、区块链技术文献、Cardossier汽车生态联盟案例、Figure 1中的三个社会技术子系统。

- designed_or_compared_object_cn：多主体认证的构念定义；区块链技术子系统对用户子系统的affordance映射；与单一第三方认证（Carfax/Eurotax）对比。

- baseline_control_or_counterfactual_cn：仅经销商信号和单一第三方认证报告。

##### objective_metrics

1. 构念定义

2. 子系统affordance数量

3. 信息熵降低的逻辑论证

- analysis_method_cn：文献综合、affordance分析、案例证据引用。

- main_result_cn：将多主体认证定义为多个独立方以可信方式记录资产历史；归纳出分散数据、数据溯源/通证化、激励兼容三种机制，使经销商有潜力发送更高fit的信号。

- argumentative_role_cn：建立全文的核心构念和因果前提，让后续模型和实验有明确的处理变量。

- remaining_uncertainty_cn：尚未说明高fit信号如何具体改变行为和市场均衡，也缺少经验证据。

- link_to_next_phase_cn：引入形式模型，对买家/卖家子系统的动态进行解析刻画。

##### evidence_pointers

1. Related Work, Market for Lemons and Current Mitigants

2. Blockchain-Based Product History Certification section

3. Figure 1

#### 2. 解析模型：高fit信号下的市场均衡

- order：2

- name_cn：解析模型：高fit信号下的市场均衡

- question_cn：在理论上，经销商使用多主体认证带来的高fit信号会如何影响交易可行性和价格区间？

- inputs_and_setting_cn：Levin(2001)柠檬市场模型、连续质量空间、买家/经销商各自收到信号的设定；另用CARA效用函数做稳健性扩展。

- designed_or_compared_object_cn：两种参数化情境：仅经销商信号（支持区间[L,U]）与多主体认证信号（更窄支持区间[L_M,U_M]）。

- baseline_control_or_counterfactual_cn：无多主体认证的经销商信号模型，以Proposition 1为基准。

##### objective_metrics

1. 交易是否发生

2. 可成交价格区间

3. 信息熵大小

- analysis_method_cn：闭式解析推导，分Case SL/SH/ML/MH/MM讨论；CARA效用模型稳健性检验。

- main_result_cn：Proposition 1：无高fit信号时，经销商收到均值信号m > (U+1)/2则无交易；Proposition 2：有高fit信号时存在阈值T，3m≤T则交易，否则无交易；Corollary 1：对称缩窄价值区间会缩小可成交价格范围；高fit信号对应更低的熵。

- argumentative_role_cn：把高fit信号从概念转化为可预测的价格、交易和熵效应，为假设提供数学基础。

- remaining_uncertainty_cn：模型是静态的、假设独立估值，且未包含谈判策略、锚定心理等真实行为机制。

- link_to_next_phase_cn：模型价格区间结论与行为文献中的锚定效应结合，形成H1-H3假设。

##### evidence_pointers

1. Model section

2. Proposition 1

3. Proposition 2

4. Corollary 1

5. Figure 2

#### 3. 假设发展：把模型预测转化为可观察行为

- order：3

- name_cn：假设发展：把模型预测转化为可观察行为

- question_cn：模型预测在真实谈判情境中应表现为哪些可观察的市场变量差异？

- inputs_and_setting_cn：模型中的价格区间、Corollary 1、锚定效应文献（Adomavicius等；Beggs & Graddy）。

- designed_or_compared_object_cn：H1（初始要价）、H2（成交价）、H2.1/H2.2（经销商/买家相对收益）、H3（peach和lemon成交比例）。

- baseline_control_or_counterfactual_cn：无多主体认证的经销商信号情境。

##### objective_metrics

1. 经销商初始要价

2. 平均成交价

3. 经销商相对收益

4. 买家相对收益

5. peach/lemon成交比例

- analysis_method_cn：理论推导与假设陈述。

- main_result_cn：提出五个假设：多主体认证降低初始要价、降低成交价、降低经销商收益、提高买家收益、增加peach减少lemon。

- argumentative_role_cn：桥接解析模型与实验设计，使理论预测可被统计检验。

- remaining_uncertainty_cn：假设只是预测，尚需受控实验数据验证。

- link_to_next_phase_cn：设计CarMarket市场游戏来操作化两种信息结构并收集数据。

##### evidence_pointers

1. Hypotheses Development section

#### 4. 实验设计与数据生成：CarMarket/CarCerti

- order：4

- name_cn：实验设计与数据生成：CarMarket/CarCerti

- question_cn：如何在受控环境中操作化多主体认证，并与仅经销商信号情境进行比较？

- inputs_and_setting_cn：105名MBA硕士生（每人先后扮演买家与经销商，共210个用户）、AutoScout24平台结构、真实二手车数据、两家瑞士专家估值、Cardossier/Corda合作、预测试。

- designed_or_compared_object_cn：CarMarket在线二手车市场；Instance A为仅经销商信号，Instance B增加CarCerti多主体认证信息（维修/保养/事故/召回历史、驾驶动态），信息在UI中高亮呈现。

- baseline_control_or_counterfactual_cn：Instance A即无多主体认证的单方信号情境，与Instance B在同批车辆、同样预算和时长下对比。

##### objective_metrics

1. 初始要价

2. 成交价

3. 相对收益

4. peach/lemon分类

5. 未成交车辆数

- analysis_method_cn：被试间设计，随机分组、随机分配车辆、控制同款车辆、相同时间与预算。

- main_result_cn：数据收集完成：Instance A保留52笔、Instance B 53笔交易；实验操作成功区分了两种信息结构。

- argumentative_role_cn：将抽象的多主体认证构念变成可复现的实验处理，从而为因果推断提供数据基础。

- remaining_uncertainty_cn：尚未进行统计检验，不知道组间差异是否显著。

- link_to_next_phase_cn：对两组数据进行假设检验。

##### evidence_pointers

1. Experimental Methods

2. Market Game Design

3. Experimental Design

4. Figure 3

#### 5. 统计检验与结果

- order：5

- name_cn：统计检验与结果

- question_cn：实验数据是否支持H1、H2、H2.1、H2.2和H3？

- inputs_and_setting_cn：Instance A 52笔交易、Instance B 53笔交易，含价格、相对收益和peach/lemon分类数据。

- designed_or_compared_object_cn：Instance A与Instance B之间的差异比较。

- baseline_control_or_counterfactual_cn：Instance A作为无多主体认证的基准。

##### objective_metrics

1. 初始要价的均值差

2. 成交价的均值差

3. 经销商相对收益均值

4. 买家相对收益均值

5. peach/lemon比例

6. p值

- analysis_method_cn：双总体t检验（均值差异）和比例检验（peach/lemon占比）。

- main_result_cn：H1：初始要价降低1832美元，p=0.00174；H2：成交价降低1556美元，p=0.00256；H2.1：经销商相对收益从0.1866降到0.0429，p≈0；H2.2：买家负收益从-0.1866改善到-0.0429，p=0.00213；H3：peach占比从0.08升到0.34，lemon占比从0.56降到0.30，p分别为0.0011和0.0071。全部假设获得支持。

- argumentative_role_cn：为多主体认证影响市场结果提供直接经验证据，并把模型中的价格区间和熵预测落实到行为层面。

- remaining_uncertainty_cn：统计检验显示组间差异显著，但未直接测量信号fit、熵或中介机制；也可能存在未观察到的被试或情境因素。

- link_to_next_phase_cn：讨论部分对这些结果进行机制解释、边界界定和理论提升。

##### evidence_pointers

1. Results section

2. Tables 1-5

#### 6. 讨论、理论回报与设计知识

- order：6

- name_cn：讨论、理论回报与设计知识

- question_cn：经验结果如何支持多主体认证的高fit信号机制？对区块链系统设计、经销商商业模式和监管有何含义？

- inputs_and_setting_cn：前序模型、实验结果、区块链文献、Cardossier项目经验、信号理论与社会技术框架。

- designed_or_compared_object_cn：将结果重新映射到Figure 1的三个子系统和高fit信号的三个来源（分散信息、溯源/通证化、激励兼容）。

- baseline_control_or_counterfactual_cn：无多主体认证时的18%过度支付（作者数据）与有认证时约4%的偏差对比。

##### objective_metrics

1. 信息熵降低的论证

2. 价格偏差百分比

3. 市场公平性

4. 经销商商业模式可持续性

- analysis_method_cn：理论讨论、案例引用、边界条件推断、设计原则提取。

- main_result_cn：论证区块链是目前唯一能让不互信多方去中心化协作并创造数字所有权独占的技术；提出高fit信号的实现来源；指出若私人卖家也能访问多主体认证，经销商中介价值将被削弱；提出通过信号访问费为系统融资。

- argumentative_role_cn：闭合全文的论证循环：把局部实验结果提升为可复用设计知识和可推广的边界主张，并回应引言中的RQ。

- remaining_uncertainty_cn：缺乏对真实区块链投票/激励机制、长期均衡、私人卖家访问和融资模式的实证。

- link_to_next_phase_cn：为未来研究指出建模复杂性、样本规模、用户感知和定价/融资等方向。

##### evidence_pointers

1. Discussion section

2. Conclusion section

3. CARA robustness note

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PHENOMENON

3. LIMITATION

4. GAP

5. THEORY_INTRO

6. STUDY_OVERVIEW

7. RESULT

8. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PHENOMENON

3. PRIOR_KNOWLEDGE

4. PRACTICAL_STAKES

5. LIMITATION

6. CONTEXT

7. PRIOR_KNOWLEDGE

8. THEORY_PROPOSITION

9. GAP

10. RQ_OR_OBJECTIVE

11. WHY_GAP_MATTERS

12. STUDY_OVERVIEW

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. THEORY_PROPOSITION

3. MECHANISM

4. THEORY_INTRO

5. LIMITATION

6. GAP

7. WHY_GAP_MATTERS

8. REQUIREMENT

9. DESIGN_FEATURE

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. THEORY_PROPOSITION

4. MECHANISM

5. BENCHMARK_OR_CONTRAST

6. METHOD_JUSTIFICATION

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. HYPOTHESIS_OR_PROPOSITION

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. MECHANISM

3. RESULT

4. BOUNDARY_CONDITION

5. CONTRIBUTION

6. LIMITATION_AND_FUTURE

7. CONTRIBUTION

## 理论/知识到设计的翻译

### 知识/理论基础

1. 信号理论（Spence；Connelly等；信号fit、频率、可观察性）

2. 柠檬市场/逆向选择理论（Akerlof；Levin）

3. 社会技术IS工件框架（Chatterjee等；Sarker等）

4. 区块链技术特性与affordance文献（去中心化、共识、通证化、溯源）

5. 行为经济学中的锚定效应文献

- 理论—设计耦合：partial

- 耦合判定理由：信号理论和社会技术框架确实前瞻性地定义了多主体认证构念和“更高fit信号”这一核心处理变量，并决定了实验要比较的信息结构；但CarCerti的具体实现形态、UI呈现和数据来源主要来自Cardossier真实区块链项目、AutoScout24平台和行业专家协作，不是纯理论推演出来的制品。因此理论指导了问题、变量和预测，但关键制品的技术实现来自领域工程和产业合作。

- 理论到设计翻译链：信号必须难以伪造且与不可观测质量相关（fit）→ 经销商现有信号和单一第三方认证存在信息分散、不可溯源、最小信息披露激励等缺陷 → 多主体认证通过区块链去中心化、通证化、共识机制和溯源特性聚合分散数据并保证可信 → 该构念被操作化为CarCerti信息界面，向买卖双方提供维修保养历史和驾驶动态两类高fit信息 → 解析模型将高fit信号参数化为更窄价值区间[LM,UM]，推出更低熵、更小价格区间和更多交易 → 实验室实验用Instance A（低fit信号）与Instance B（高fit信号）对比，检验初始要价、成交价、相对收益和peach/lemon比例。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：有效信号需要难以伪造且与不可观测质量相关；fit是信号有效性的核心。

- mechanism_cn：聚合多方数据并保证数据来源可追溯，会使买家感知和实际获得的质量信息更接近真实质量，降低不确定性。

- design_requirement_cn：认证系统应整合分散的信息源，提供可验证且防伪的产品历史。

- artifact_choice_cn：多主体认证CarCerti：由多个利益相关方维护的区块链车辆历史证书，提供维修/保养/事故/召回和驾驶动态信息。

- evaluated_contrast_cn：Instance A（仅经销商/单一第三方信号）与Instance B（增加CarCerti多主体认证）。

- objective_result_cn：Instance B中成交价显著降低，买家与经销商收益分布改变；价格偏差从约18%降至约4%。

##### evidence_pointers

1. Introduction P1

2. Blockchain-Based Product History Certification

3. Market Game Design

4. Results Tables 2-4

#### 2. 2

- theory_or_knowledge_claim_cn：信息优势使经销商能够在谈判中利用锚定效应获取高额收益。

- mechanism_cn：高fit信号压缩经销商的信息优势，削弱其设置高初始要价作为锚点的能力。

- design_requirement_cn：买家应能独立查看到与车辆具体实例高度相关的可信信息，而不是仅依赖经销商的广告和声誉。

- artifact_choice_cn：在Instance B中，CarCerti以高亮方式展示车辆特定实例的维修保养和驾驶动态信息。

- evaluated_contrast_cn：Instance A vs Instance B的经销商初始要价与最终成交价。

- objective_result_cn：初始要价降低1832美元（p=0.00174），成交价降低1556美元（p=0.00256）。

##### evidence_pointers

1. Hypotheses H1/H2

2. Results Tables 1-2

#### 3. 3

- theory_or_knowledge_claim_cn：逆向选择导致无认证时柠檬驱逐桃子；高fit信号使买家能区分好坏车，从而改善市场配置。

- mechanism_cn：信息熵降低后，买家愿意为peach支付更接近真实价值的价格，经销商也更愿意出售好车。

- design_requirement_cn：信号应能缩窄买家对车辆价值的先验分布区间，降低关于质量的极端不确定性。

- artifact_choice_cn：CarCerti提供两类具体实例信息，使价值区间从[1,U]缩窄到[L_M,U_M]。

- evaluated_contrast_cn：Instance A vs Instance B中peach和lemon的成交比例。

- objective_result_cn：peach占比从0.08升至0.34，lemon占比从0.56降至0.30，p值分别为0.0011和0.0071。

##### evidence_pointers

1. Model Proposition 1/2

2. Hypothesis H3

3. Results Table 5

#### 4. 4

- theory_or_knowledge_claim_cn：社会技术系统框架认为信息元素决定技术子系统与社会子系统的交互，熵衡量系统不确定性。

- mechanism_cn：更高fit信号降低买方和卖方信念分布的熵，从而减少极端结果并增加系统和谐。

- design_requirement_cn：区块链应用设计应以熵降低为目标，不仅增加数据量，还要保证数据可信和相关。

- artifact_choice_cn：去中心化数据上传、通证化所有权和溯源机制；实验中的CarCerti模拟这些特性。

- evaluated_contrast_cn：模型中的熵变化与实验中的市场结果变化。

- objective_result_cn：模型证明高fit信号对应更窄支持区间和更低熵；实验显示价格偏差和收益极端性显著降低。

##### evidence_pointers

1. Model Parametrizations

2. Figure 2

3. Discussion Economic Impacts

## 评价逻辑

### evaluation_modes

1. 解析模型与命题推导

2. 实验室市场实验（CarMarket）

3. 被试间A/B比较

4. CARA效用函数稳健性检验

5. 行业专家参与的预测试与外部效度设计

- why_these_evaluations_cn：仅靠解析模型只能说明理论均衡，无法保证真实谈判中人类会遵循模型；仅靠实验则缺少理论机制。因此先用模型给出清晰的比较静态预测和价格区间，再用实验室实验在控制其他因素的情况下引入多主体认证作为信息结构变化，检验真实行为是否与理论预测一致。CARA模型用于证明结论不依赖特定的效用函数，预测试和专家估值用于提高实验材料和车辆价值的现实性。

- benchmark_and_contrast_chain_cn：整个评价建立在同一组对比上：无多主体认证的经销商/单一第三方信号作为基准（Instance A），有CarCerti多主体认证信号作为处理（Instance B）。解析模型中，该对比表现为[L,U]与[L_M,U_M]；实验设计中，该对比表现为同款车辆、相同平台和相同被试群体下的两种信息界面。这一chain是累积的：模型用熵和价格区间解释了为什么应出现差异；实验用价格、收益和成交比例检验差异是否出现；最后用讨论中的价格偏差（18% vs 4%）将实验结果量化并连接回理论。

### claim_evidence_ledger

#### 1. 多主体认证使经销商能发送更高fit的信号。

- claim_cn：多主体认证使经销商能发送更高fit的信号。

- evidence_cn：构念论证+实验中的显著行为差异；但信号fit本身未直接测量。

#### 2. H1：多主体认证降低经销商初始要价。

- claim_cn：H1：多主体认证降低经销商初始要价。

- evidence_cn：Table 1：平均初始要价13,742 vs 11,910美元，差异1832美元，p=0.00174。

#### 3. H2：多主体认证降低成交价。

- claim_cn：H2：多主体认证降低成交价。

- evidence_cn：Table 2：平均成交价11,567 vs 10,011美元，差异1556美元，p=0.00256。

#### 4. H2.1：多主体认证降低经销商相对收益。

- claim_cn：H2.1：多主体认证降低经销商相对收益。

- evidence_cn：Table 3：0.1866 vs 0.0429，p≈0。

#### 5. H2.2：多主体认证提高买家相对收益。

- claim_cn：H2.2：多主体认证提高买家相对收益。

- evidence_cn：Table 4：-0.1866 vs -0.0429，p=0.00213。

#### 6. H3：多主体认证增加peach成交、减少lemon成交。

- claim_cn：H3：多主体认证增加peach成交、减少lemon成交。

- evidence_cn：Table 5：peach 0.08→0.34，lemon 0.56→0.30，p=0.0011/0.0071。

#### 7. 多主体认证降低系统熵。

- claim_cn：多主体认证降低系统熵。

- evidence_cn：解析模型中更窄支持区间对应更低熵；实验中的价格偏差从约18%降至4%作为间接证据。

#### 8. 多主体认证提高市场公平性。

- claim_cn：多主体认证提高市场公平性。

- evidence_cn：经销商超额收益下降、买家负收益改善；但是否等于社会福利/公平需进一步界定。

- internal_validity_strategy_cn：采用被试间设计避免学习效应；随机分配参与者和车辆；两个Instance使用相同车辆、相同预算、相同时长和相同目标；只删除一笔因小数点错输导致的异常交易；在游戏前通过问卷检验被试知识水平；用相对收益作为指标以消除车辆价值差异的影响。

- external_validity_strategy_cn：市场游戏基于真实平台AutoScout24设计，并使用当时真实在售二手车；车辆真实价值由行业标准评估表和两位专家估值确定；多主体认证界面与Cardossier项目合作开发；经过一年多次小规模预测试；讨论中说明实验结果可推广到其他存在信息不对称的市场。

- what_is_not_actually_tested_cn：没有直接测量信号fit或中介机制；没有真正部署区块链共识和通证激励，而是模拟其信息输出；锚定效应未被独立测量；熵的变化只在模型中被证明而非在实验中直接观测；市场公平性和社会福利只是基于相对收益转移的推断；长期均衡、私人卖家访问认证后的市场结果以及交易费/融资机制未被检验。

## 贡献闭环

- technical_claim_cn：区块链支持的多主体认证能显著降低二手车市场中的信息不对称，使成交价更接近真实价值，并改善商品配置。

- artifact_claim_cn：具体可识别设计部分是多主体认证提供的高fit信息（维修保养历史、驾驶动态），它比单一经销商/第三方信号更能压缩买家不确定性，因而导致初始要价、成交价和收益分布的系统性变化。

- mechanism_claim_cn：高fit信号通过三条路径起作用：（1）聚合分散信息；（2）通过区块链溯源/通证化保证数据可信与可验证；（3）激励多方提供比垄断性单一认证机构更多的信息。这些机制降低买家/卖家的信念熵，削弱经销商的锚定优势，从而改变谈判结果和市场配置。

- boundary_claim_cn：结论适用于与二手车市场结构相似、存在信息不对称且质量维度可被数据描述的市场；前提是多主体认证系统能提供足够可信且不可伪造的信息，且数据提供者受到正确激励；如果私人卖家也能访问多主体认证，经销商的中介价值会被削弱。

- reusable_design_knowledge_cn：区块链认证系统设计应：（1）整合多个独立利益相关方的分散数据源；（2）利用通证化和溯源机制保证数据来源清晰且难以篡改；（3）为数据提供者设置激励以克服最小信息披露倾向；（4）通过高fit信号降低系统熵并提升市场公平性；（5）考虑通过信号访问费支付系统开发成本和基础设施成本。

- theoretical_contribution_cn：将信号理论中的fit概念与社会技术IS工件框架结合，提出了多主体认证构念；用形式模型证明高fit信号降低熵并改变柠檬市场均衡；通过实验补充了区块链经济学研究中的行为证据，回应了关于区块链affordance与市场结果之间关系的呼吁；展示了熵概念在IS研究中的应用方式。

- how_discussion_closes_intro_gap_cn：引言提出多主体认证的市场影响未知；讨论部分用实验结果证明多主体认证能产生更高fit信号，进而降低信息不对称、改善配置并提高公平性，并解释这些结果如何通过社会技术系统的熵减少而实现，从而直接回答RQ；同时把区块链从“技术炒作”重新定位为必须配合激励和系统设计才能释放价值的使能技术。

- overclaim_or_unsupported_leaps_cn：作者在引言和结论中使用了“solve the market for lemons problem”“increase in market fairness”等较强表述，但实验只展示了短期内相对收益的转移和成交结构的改变，并未测量总福利、长期均衡、实际区块链信任或私人卖家的市场进入；信号fit和熵也主要是模型证明而非直接观测，因此从实验到“真正解决柠檬市场”存在跳跃。

## 句级写作动作图谱

### 1. 摘要第1句

- order：1

- section：Abstract

- locator：摘要第1句

- move_code：CONTEXT

- paraphrase_cn：质量差异相似商品的市场会因信息不对称而受损。

- rhetorical_function_cn：开门见山指出研究的经典问题域。

- depends_on_cn：无，独立建立背景。

- sets_up_cn：为后续讨论经销商信号和多主体认证的必要性提供背景。

- evidence_pointer：Abstract

### 2. 摘要第2-3句

- order：2

- section：Abstract

- locator：摘要第2-3句

- move_code：PHENOMENON

- paraphrase_cn：经销商通过质量信号中介市场，但市场仍低于最优，大量商品被高估，收益多被中间商获取。

- rhetorical_function_cn：指出经验现实中的既有缓解机制并非充分。

- depends_on_cn：背景中信息不对称概念。

- sets_up_cn：为多主体认证作为更优信号来源埋下伏笔。

- evidence_pointer：Abstract

### 3. 摘要第4-5句

- order：3

- section：Abstract

- locator：摘要第4-5句

- move_code：GAP

- paraphrase_cn：作者在已有区块链可信资产文档化研究基础上，关注多主体认证是否真正影响市场。

- rhetorical_function_cn：从技术可能性转向未验证的市场影响，形成研究缺口。

- depends_on_cn：区块链作为enabler的已有研究。

- sets_up_cn：引出RQ。

- evidence_pointer：Abstract

### 4. 摘要第6-7句

- order：4

- section：Abstract

- locator：摘要第6-7句

- move_code：THEORY_INTRO

- paraphrase_cn：引入社会技术视角，描述多主体认证让经销商能发送与不可观测质量更相关的更高fit信号。

- rhetorical_function_cn：交代理论视角和核心机制。

- depends_on_cn：社会技术IS工件框架的引入。

- sets_up_cn：为理论化与实验设计提供概念框架。

- evidence_pointer：Abstract

### 5. 摘要第8句

- order：5

- section：Abstract

- locator：摘要第8句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者计划同时进行理论化和实验探究两类信号的市场效应。

- rhetorical_function_cn：预告研究由模型与实验组成。

- depends_on_cn：已有理论视角。

- sets_up_cn：读者预期会有解析和实证两部分。

- evidence_pointer：Abstract

### 6. 摘要最后一句

- order：6

- section：Abstract

- locator：摘要最后一句

- move_code：RESULT

- paraphrase_cn：210名被试的实验室实验发现多主体认证带来更高fit信号，减少信息不对称、更有效配置商品、提高市场公平。

- rhetorical_function_cn：在摘要尾部给出核心经验结果。

- depends_on_cn：实验设计与理论框架。

- sets_up_cn：整篇文章的核心贡献。

- evidence_pointer：Abstract

### 7. 第1段第1句

- order：7

- section：Introduction

- locator：第1段第1句

- move_code：CONTEXT

- paraphrase_cn：信息不对称发生在交易一方比另一方更了解商品质量的市场。

- rhetorical_function_cn：建立全文的经济学背景。

- depends_on_cn：无。

- sets_up_cn：引入信号和fit概念。

- evidence_pointer：Introduction P1

### 8. 第1段信号定义附近

- order：8

- section：Introduction

- locator：第1段信号定义附近

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：信号由信息优势方发送给信息劣势方，有效信号需难以伪造，其与不可观测质量的相关程度称为fit。

- rhetorical_function_cn：提供后续分析的关键术语。

- depends_on_cn：信息不对称概念。

- sets_up_cn：为评估多主体认证为何优于现有信号建立标准。

- evidence_pointer：Introduction P1

### 9. 第1段经销商部分

- order：9

- section：Introduction

- locator：第1段经销商部分

- move_code：PHENOMENON

- paraphrase_cn：经销商利用识别质量的技能，以接近平均价格收购好车，再用品牌或保修等信号高价出售。

- rhetorical_function_cn：描述当前市场最重要的信号中介者。

- depends_on_cn：信号与fit概念。

- sets_up_cn：后续讨论经销商信号虽有效但利益被其攫取。

- evidence_pointer：Introduction P1

### 10. 第2段

- order：10

- section：Introduction

- locator：第2段

- move_code：PRACTICAL_STAKES

- paraphrase_cn：尽管有积极效果，二手车市场仍明显低于最优：里程表欺诈每年给欧盟公民造成89亿欧元损失；买家对柠檬的过度支付平均占车价18%；中介拿走大部分新增收益。

- rhetorical_function_cn：用具体数字说明问题的重要性和现实代价。

- depends_on_cn：现有经销商信号的局限。

- sets_up_cn：论证需要新的缓解方案。

- evidence_pointer：Introduction P2

### 11. 第3段

- order：11

- section：Introduction

- locator：第3段

- move_code：CONTEXT

- paraphrase_cn：汽车生态数字化可能改变这一局面，车企希望将车辆数据变现，但制造商或谷歌等集中掌控数据会形成更强大平台，损害其他主体和监管者利益。

- rhetorical_function_cn：加入数字化转型的时代背景，引出去中心化方案的动机。

- depends_on_cn：前文市场低效问题。

- sets_up_cn：区块链作为去中心化资产文档化方案出场。

- evidence_pointer：Introduction P3

### 12. 第4段开头

- order：12

- section：Introduction

- locator：第4段开头

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：区块链信息系统被认为是实现真实世界资产可信、去中心化数字化的新方法，能保证数据完整性并控制交易成本。

- rhetorical_function_cn：介绍技术可能性的既有研究。

- depends_on_cn：数字化转型背景。

- sets_up_cn：引出多主体产品历史证书。

- evidence_pointer：Introduction P4

### 13. 第4段中间

- order：13

- section：Introduction

- locator：第4段中间

- move_code：THEORY_PROPOSITION

- paraphrase_cn：区块链支持的多主体产品历史证书给予经销商发送比当前更高fit信号的行动潜力。

- rhetorical_function_cn：陈述全文的核心理论命题。

- depends_on_cn：区块链特性与多主体证书概念。

- sets_up_cn：为RQ提供具体假设方向。

- evidence_pointer：Introduction P4

### 14. 第4段后半

- order：14

- section：Introduction

- locator：第4段后半

- move_code：GAP

- paraphrase_cn：但多主体认证只是信息不对称情境中的资源，不是解决方案本身；它能否导致显著不同的市场结果仍待检验。

- rhetorical_function_cn：将技术可能性与未验证结果之间的缺口明确化。

- depends_on_cn：前一命题。

- sets_up_cn：引出具体RQ。

- evidence_pointer：Introduction P4

### 15. 第5段开头

- order：15

- section：Introduction

- locator：第5段开头

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：RQ：多主体认证如何影响柠檬市场？

- rhetorical_function_cn：正式给出研究问题。

- depends_on_cn：前面的缺口。

- sets_up_cn：整个后续研究围绕此问题展开。

- evidence_pointer：Introduction P5

### 16. 第5段后半

- order：16

- section：Introduction

- locator：第5段后半

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：该问题响应学界对区块链affordance及其市场影响进行深入分析和实证的呼吁，IS学科最适合研究区块链能力与经济影响。

- rhetorical_function_cn：论证该问题为什么值得IS研究。

- depends_on_cn：RQ。

- sets_up_cn：说明研究定位与学科正当性。

- evidence_pointer：Introduction P5

### 17. 第6段

- order：17

- section：Introduction

- locator：第6段

- move_code：STUDY_OVERVIEW

- paraphrase_cn：文章首先回顾柠檬市场经济学，再介绍社会技术工件框架，随后建立形式模型并推出假设，接着用实验检验，最后讨论结果和意义。

- rhetorical_function_cn：给读者提供全文路线图。

- depends_on_cn：研究问题。

- sets_up_cn：建立文章结构预期。

- evidence_pointer：Introduction P6

### 18. Market for Lemons 第1段

- order：18

- section：Related Work

- locator：Market for Lemons 第1段

- move_code：MECHANISM

- paraphrase_cn：由于区分好坏车的特征大多隐藏，买家无法分辨peach和lemon，因此两类车都会按市场平均质量定价。

- rhetorical_function_cn：解释柠檬市场逆向选择的基本机制。

- depends_on_cn：信息不对称定义。

- sets_up_cn：引出经典Akerlof结果。

- evidence_pointer：Related Work, Market for Lemons P1

### 19. Market for Lemons 第1段后半

- order：19

- section：Related Work

- locator：Market for Lemons 第1段后半

- move_code：THEORY_PROPOSITION

- paraphrase_cn：经典逆向选择结果是柠檬驱逐peach，理论上甚至可能导致市场崩溃。

- rhetorical_function_cn：陈述理论基准。

- depends_on_cn：平均定价机制。

- sets_up_cn：为讨论经销商作为防止崩溃的力量铺垫。

- evidence_pointer：Related Work, Market for Lemons P1

### 20. Market for Lemons 第2段

- order：20

- section：Related Work

- locator：Market for Lemons 第2段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：市场没有崩溃的部分原因是经销商存在，他们通过保修、品牌等信号中介交易并减少产品不确定性。

- rhetorical_function_cn：解释现有缓解机制。

- depends_on_cn：逆向选择理论。

- sets_up_cn：为评价经销商信号局限提供基础。

- evidence_pointer：Related Work, Market for Lemons P2

### 21. Market for Lemons 第2段后半

- order：21

- section：Related Work

- locator：Market for Lemons 第2段后半

- move_code：LIMITATION

- paraphrase_cn：信号有效性受fit、频率和可观察性限制；经销商信号只能部分改善柠檬问题，且大部分收益被经销商拿走。

- rhetorical_function_cn：指出现有信号的结构性不足。

- depends_on_cn：信号理论。

- sets_up_cn：转向产品历史认证作为替代。

- evidence_pointer：Related Work, Market for Lemons P2

### 22. Market for Lemons 第3段

- order：22

- section：Related Work

- locator：Market for Lemons 第3段

- move_code：LIMITATION

- paraphrase_cn：个体卖家提供的产品历史证明成本高且容易伪造；单一独立认证机构（如Carfax/Eurotax）缺乏分散数据、缺少可追溯性和数据来源，且垄断性机构没有动力披露超出最低限度的信息。

- rhetorical_function_cn：系统列举现有认证方案的三种缺陷。

- depends_on_cn：信号fit理论。

- sets_up_cn：为区块链多主体认证作为替代方案提供空间。

- evidence_pointer：Related Work, Market for Lemons P3

### 23. Blockchain-Based Product History Certification 第1段

- order：23

- section：Related Work

- locator：Blockchain-Based Product History Certification 第1段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：区块链的关键特征是分布式数据库、网络共识机制和密码学逻辑带来的不可变与透明。

- rhetorical_function_cn：为之后把区块链技术特性与affordance联系起来做准备。

- depends_on_cn：已有区块链研究。

- sets_up_cn：说明为什么区块链不同于传统集中式数据库。

- evidence_pointer：Related Work, Blockchain-Based Product History Certification P1

### 24. Blockchain-Based Product History Certification 第2段

- order：24

- section：Related Work

- locator：Blockchain-Based Product History Certification 第2段

- move_code：THEORY_INTRO

- paraphrase_cn：本文将区块链视为社会技术系统，并使用Chatterjee等的IS工件框架来结构化其affordance。

- rhetorical_function_cn：引入核心理论框架。

- depends_on_cn：区块链特性。

- sets_up_cn：为三个子系统分析提供理论工具。

- evidence_pointer：Related Work, Blockchain-Based Product History Certification P2

### 25. Blockchain-Based Product History Certification 第3段

- order：25

- section：Related Work

- locator：Blockchain-Based Product History Certification 第3段

- move_code：THEORY_INTRO

- paraphrase_cn：IS工件由技术子系统、社会子系统、信息元素以及两者间的affordance/约束关系构成，熵衡量系统不确定性。

- rhetorical_function_cn：介绍框架的关键概念。

- depends_on_cn：社会技术系统视角。

- sets_up_cn：后续用熵变化解释市场结果。

- evidence_pointer：Related Work, Blockchain-Based Product History Certification P3

### 26. Infrastructure Provider Subsystem

- order：26

- section：Related Work

- locator：Infrastructure Provider Subsystem

- move_code：MECHANISM

- paraphrase_cn：面对数字巨头和监管压力，区块链的去中心化架构成为满足跨组织去中心化协作需求的技术使能者，并通过信息分布降低极端结果和熵。

- rhetorical_function_cn：解释基础设施提供者子系统中技术如何 shaping 社会需求。

- depends_on_cn：社会技术框架。

- sets_up_cn：说明区块链对上层子系统的作用。

- evidence_pointer：Infrastructure Provider Subsystem

### 27. Car-Related Businesses Subsystem

- order：27

- section：Related Work

- locator：Car-Related Businesses Subsystem

- move_code：MECHANISM

- paraphrase_cn：区块链的通证化功能赋予企业对数字资源的所有权，激励它们提供和交易数据，从而促成多主体车辆历史证书等联合产品创新。

- rhetorical_function_cn：解释多主体认证的数据供给动力。

- depends_on_cn：去中心化基础设施。

- sets_up_cn：为定义多主体认证提供依据。

- evidence_pointer：Car-Related Businesses Subsystem

### 28. Buyers and Sellers Subsystem，定义附近

- order：28

- section：Related Work

- locator：Buyers and Sellers Subsystem，定义附近

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者提出并定义“多主体认证”：多个独立方以可信方式记录资产的历史。

- rhetorical_function_cn：在文章中正式引入新的核心构念。

- depends_on_cn：前两个子系统的分析。

- sets_up_cn：后续模型和实验都围绕该构念展开。

- evidence_pointer：Buyers and Sellers of Used Cars Subsystem

### 29. Buyers and Sellers Subsystem后半

- order：29

- section：Related Work

- locator：Buyers and Sellers Subsystem后半

- move_code：THEORY_PROPOSITION

- paraphrase_cn：多主体认证通过更多综合数据和数据可信度，给予经销商发送更高fit信号的行动潜力。

- rhetorical_function_cn：提出核心假设性命题。

- depends_on_cn：区块链技术特性。

- sets_up_cn：指向仍需验证的市场影响。

- evidence_pointer：Buyers and Sellers of Used Cars Subsystem

### 30. Buyers and Sellers Subsystem最后一段

- order：30

- section：Related Work

- locator：Buyers and Sellers Subsystem最后一段

- move_code：GAP

- paraphrase_cn：虽然已有信用市场的区块链模型预测市场可能崩溃并伴随福利提高，但该结果不能直接移植到二手车市场，且缺少经验分析；这推动了本研究。

- rhetorical_function_cn：明确现有知识的缺口和转移局限。

- depends_on_cn：前文多主体认证构念。

- sets_up_cn：为建立自己的模型和实验提供动机。

- evidence_pointer：Buyers and Sellers of Used Cars Subsystem末尾

### 31. Market Definition开头

- order：31

- section：Model

- locator：Market Definition开头

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为了理解多主体认证的影响，作者提出了一个基于Levin模型稍作修改的简单经济模型，用连续质量空间并在有无多主体认证时使用不同参数化来表示信号fit。

- rhetorical_function_cn：解释建模选择的来源和用途。

- depends_on_cn：社会技术子系统分析。

- sets_up_cn：推导命题和假设。

- evidence_pointer：Model, Market Definition

### 32. Market Definition相对收益说明

- order：32

- section：Model

- locator：Market Definition相对收益说明

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：模型和实验都使用相对收益而非绝对收益，以处理不同价位汽车的问题。

- rhetorical_function_cn：说明关键指标选择的原因。

- depends_on_cn：连续质量建模。

- sets_up_cn：为实验中的相对收益指标作铺垫。

- evidence_pointer：Model, Market Definition

### 33. Parametrizations, Proposition 1

- order：33

- section：Model

- locator：Parametrizations, Proposition 1

- move_code：RESULT

- paraphrase_cn：Proposition 1：无多主体认证时，若经销商收到的均值信号m>(U+1)/2，则交易不可能；若交易发生，价格落在特定区间。

- rhetorical_function_cn：给出基准模型的可检验预测。

- depends_on_cn：参数化模型。

- sets_up_cn：与有认证情境的Proposition 2形成对比。

- evidence_pointer：Model, Proposition 1

### 34. Parametrizations, Multi-party setup

- order：34

- section：Model

- locator：Parametrizations, Multi-party setup

- move_code：MECHANISM

- paraphrase_cn：有高fit信号时，买家信念分布的支撑区间更窄，因此信息熵更低。

- rhetorical_function_cn：解释高fit信号如何降低不确定性。

- depends_on_cn：熵概念与均匀分布最大熵性质。

- sets_up_cn：为图2和假设提供理论依据。

- evidence_pointer：Model, Parametrizations

### 35. Parametrizations, Proposition 2 与 Corollary 1

- order：35

- section：Model

- locator：Parametrizations, Proposition 2 与 Corollary 1

- move_code：RESULT

- paraphrase_cn：Proposition 2给出有认证时交易发生条件为3m≤T；Corollary 1表明高fit信号使可成交价格区间更小。

- rhetorical_function_cn：完成模型的主要预测矩阵。

- depends_on_cn：多认证情境分析ML/MH/MM。

- sets_up_cn：导出H2关于成交价下降的预测。

- evidence_pointer：Model, Proposition 2 and Corollary 1

### 36. Figure 2后的段落

- order：36

- section：Model

- locator：Figure 2后的段落

- move_code：TRANSITION

- paraphrase_cn：基于知识可用性的变化，预期要价、成交价、双方收益和商品配置都会改变，这些将形式化为假设。

- rhetorical_function_cn：把模型结果转向行为假设。

- depends_on_cn：Propositions和Corollary。

- sets_up_cn：假设发展部分。

- evidence_pointer：Model, Figure 2后

### 37. H1段落

- order：37

- section：Hypotheses Development

- locator：H1段落

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H1：多主体认证可用时，经销商意识到信息优势降低，因此会以更低的初始要价开始谈判。

- rhetorical_function_cn：给出第一个可检验假设。

- depends_on_cn：模型价格区间和锚定效应文献。

- sets_up_cn：为实验中的初始要价指标服务。

- evidence_pointer：Hypotheses Development, H1

### 38. H2段落

- order：38

- section：Hypotheses Development

- locator：H2段落

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H2：由于锚定效应减弱且可成交价格集合更小，多主体认证下的平均成交价低于仅经销商信号下的成交价。

- rhetorical_function_cn：将模型价格区间结果转化为成交价格假设。

- depends_on_cn：Corollary 1与锚定效应。

- sets_up_cn：为H2.1/H2.2收益分配假设铺路。

- evidence_pointer：Hypotheses Development, H2

### 39. H2.1/H2.2段落

- order：39

- section：Hypotheses Development

- locator：H2.1/H2.2段落

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H2.1/H2.2：多主体认证下经销商平均相对收益更低，买家平均相对收益更高。

- rhetorical_function_cn：把价格降低转化为买卖双方的福利变化。

- depends_on_cn：H2与相对收益模型。

- sets_up_cn：为实验中的相对收益指标服务。

- evidence_pointer：Hypotheses Development, H2.1/H2.2

### 40. H3段落

- order：40

- section：Hypotheses Development

- locator：H3段落

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H3：多主体认证下，柠檬成交比例下降，peach成交比例上升。

- rhetorical_function_cn：把模型关于交易可行性的命题转为市场配置假设。

- depends_on_cn：Proposition 1与2的对比。

- sets_up_cn：为实验中的车辆分类指标服务。

- evidence_pointer：Hypotheses Development, H3

### 41. Market Game Design第1段

- order：41

- section：Experimental Methods

- locator：Market Game Design第1段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为检验假设，作者开发了CarMarket市场游戏；实验方法适合理解动态市场条件下的市场机制。

- rhetorical_function_cn：为实验方法给出合理理由。

- depends_on_cn：假设需要行为数据。

- sets_up_cn：介绍实验平台设计。

- evidence_pointer：Experimental Methods, Market Game Design

### 42. Market Game Design第2段

- order：42

- section：Experimental Methods

- locator：Market Game Design第2段

- move_code：DESIGN_FEATURE

- paraphrase_cn：CarMarket模拟在线二手车市场，买卖双方可协商并完成有约束力的交易，经销商额外获得车辆市场平均价格，以模拟其信息优势。

- rhetorical_function_cn：说明实验市场如何操作化现实市场特征。

- depends_on_cn：模型中的信息结构。

- sets_up_cn：为A/B信息结构差异提供环境。

- evidence_pointer：Experimental Methods, Market Game Design

### 43. Market Game Design第3段

- order：43

- section：Experimental Methods

- locator：Market Game Design第3段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：Instance A只接收基本车辆信息，Instance B在同样条件下额外访问CarCerti提供的已验证详细信息（维修保养历史、驾驶动态），信息在界面上突出显示。

- rhetorical_function_cn：建立实验的处理组与对照组。

- depends_on_cn：多主体认证构念。

- sets_up_cn：让后续统计比较有明确的操作变量。

- evidence_pointer：Experimental Methods, Market Game Design

### 44. Market Game Design第4段

- order：44

- section：Experimental Methods

- locator：Market Game Design第4段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为确保外部效度，市场设计与AutoScout24等行业专家反复讨论，使用真实二手车和两家专家估值确定车辆实际价值，并进行了为期一年的小规模测试。

- rhetorical_function_cn：支撑实验材料的现实性。

- depends_on_cn：实验平台设计。

- sets_up_cn：说明为什么实验结果可以外推。

- evidence_pointer：Experimental Methods, Market Game Design

### 45. Experimental Design第1段

- order：45

- section：Experimental Methods

- locator：Experimental Design第1段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用被试间设计，105名被试各扮演买家和经销商角色，共210个用户，以最大相对收益为目标，并用课程加分激励真实行为。

- rhetorical_function_cn：说明样本、角色设计和激励方式。

- depends_on_cn：实验目的与测量指标。

- sets_up_cn：为随机分配和统计检验提供设计基础。

- evidence_pointer：Experimental Methods, Experimental Design

### 46. Experimental Design末尾

- order：46

- section：Experimental Methods

- locator：Experimental Design末尾

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：参与者被随机分到两个Instance，车辆随机分配，两个Instance使用相同车辆、相同预算和相同时长，以保证内部效度。

- rhetorical_function_cn：说明控制变量的手段。

- depends_on_cn：被试间设计。

- sets_up_cn：让结果差异归因于CarCerti信息结构。

- evidence_pointer：Experimental Methods, Experimental Design

### 47. H1结果，Table 1附近

- order：47

- section：Results

- locator：H1结果，Table 1附近

- move_code：RESULT

- paraphrase_cn：Instance A经销商平均初始要价为13,742美元，Instance B为11,910美元，差异显著（p=0.00174），支持H1。

- rhetorical_function_cn：报告第一个假设的统计结果。

- depends_on_cn：实验数据与t检验。

- sets_up_cn：为H2的锚定效应机制提供起点。

- evidence_pointer：Results, Table 1

### 48. H2结果，Table 2附近

- order：48

- section：Results

- locator：H2结果，Table 2附近

- move_code：RESULT

- paraphrase_cn：平均成交价从11,567美元降至10,011美元，差异1556美元，p=0.00256，支持H2。

- rhetorical_function_cn：验证价格下降假设。

- depends_on_cn：H1结果与模型价格区间。

- sets_up_cn：引出收益分配假设检验。

- evidence_pointer：Results, Table 2

### 49. H2.1/H2.2结果，Tables 3-4附近

- order：49

- section：Results

- locator：H2.1/H2.2结果，Tables 3-4附近

- move_code：RESULT

- paraphrase_cn：经销商平均相对收益从0.1866降到0.0429（p≈0），买家平均相对收益从-0.1866改善到-0.0429（p=0.00213），支持H2.1和H2.2。

- rhetorical_function_cn：报告收益分配变化。

- depends_on_cn：成交价变化。

- sets_up_cn：为市场公平性讨论提供数据。

- evidence_pointer：Results, Tables 3-4

### 50. H3结果，Table 5附近

- order：50

- section：Results

- locator：H3结果，Table 5附近

- move_code：RESULT

- paraphrase_cn：Instance B的peach成交比例从0.08升至0.34，lemon成交比例从0.56降至0.30，比例差异显著，支持H3。

- rhetorical_function_cn：验证市场配置假设。

- depends_on_cn：车辆分类标准。

- sets_up_cn：为讨论社会效率和公平性打基础。

- evidence_pointer：Results, Table 5

### 51. 开头段落

- order：51

- section：Discussion

- locator：开头段落

- move_code：CONTRIBUTION

- paraphrase_cn：作者将自己的研究定位在区块链研究框架中：应用领域是二手车市场但可推广到其他信息不对称市场，核心构念是区块链资产文档化对信号有效性的影响，结果是市场动态与社会福利变化，方法包括经济建模和实验。

- rhetorical_function_cn：在讨论开头明确研究定位和贡献模式。

- depends_on_cn：全文结果。

- sets_up_cn：为后续机制解释提供框架。

- evidence_pointer：Discussion, 第一段

### 52. Blockchain-Based Multi-party Certification节

- order：52

- section：Discussion

- locator：Blockchain-Based Multi-party Certification节

- move_code：MECHANISM

- paraphrase_cn：多主体认证信号之所以fit更高，是因为它能聚合分散信息、通过通证化保证数据可追溯且不泄露商业细节、并借助激励克服单一认证机构的最小信息披露倾向。

- rhetorical_function_cn：解释结果背后的设计机制。

- depends_on_cn：区块链技术特性。

- sets_up_cn：为设计原则提供依据。

- evidence_pointer：Discussion, Blockchain-Based Multi-party Certification

### 53. Blockchain-Based Multi-party Certification末尾

- order：53

- section：Discussion

- locator：Blockchain-Based Multi-party Certification末尾

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者认为区块链目前是唯一能同时实现不可信多方去中心化协作和数字资源独有所有权的技术，但任何能达成相同目标的技术都可以用于多主体认证。

- rhetorical_function_cn：为“区块链必要性”设置边界条件。

- depends_on_cn：技术机制分析。

- sets_up_cn：防止贡献被理解为对特定技术的盲目依赖。

- evidence_pointer：Discussion, Blockchain-Based Multi-party Certification

### 54. Economic Impacts节

- order：54

- section：Discussion

- locator：Economic Impacts节

- move_code：RESULT

- paraphrase_cn：总体结果支持多主体认证减少信息不对称并提高市场公平性：价格更接近价值、经销商超额收益下降、买家损失减少、peach成交更多。

- rhetorical_function_cn：把五个假设结果综合为总体结论。

- depends_on_cn：实验结果。

- sets_up_cn：为经销商商业模式变化和熵解释铺路。

- evidence_pointer：Discussion, The Economic Impacts of Multi-party Certification

### 55. Economic Impacts后半

- order：55

- section：Discussion

- locator：Economic Impacts后半

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：若私人卖家也能访问多主体认证，好车卖家通过经销商中介的动机会减弱，经销商的商业模式会受冲击。

- rhetorical_function_cn：从实验结果推出组织/市场层面的边界后果。

- depends_on_cn：结果与信号理论。

- sets_up_cn：为实践者提供战略预警。

- evidence_pointer：Discussion, Economic Impacts

### 56. Economic Impacts中的熵段落

- order：56

- section：Discussion

- locator：Economic Impacts中的熵段落

- move_code：CONTRIBUTION

- paraphrase_cn：高fit信号降低系统熵，技术子系统与社会子系统的相互作用最终提高系统和谐与市场公平。

- rhetorical_function_cn：用熵概念将经验结果提升为理论贡献。

- depends_on_cn：社会技术框架与模型。

- sets_up_cn：引出对学者和研究者的贡献陈述。

- evidence_pointer：Discussion, Economic Impacts

### 57. 前两段

- order：57

- section：Conclusion

- locator：前两段

- move_code：CONTRIBUTION

- paraphrase_cn：作者声称推进了区块链经济学研究，在多主体认证的构念和熵计算应用方面为学者、实践者和政策制定者提供了新知识。

- rhetorical_function_cn：总结对三类读者的贡献。

- depends_on_cn：全部研究。

- sets_up_cn：引出局限性。

- evidence_pointer：Conclusion, 前两段

### 58. 局限性段落

- order：58

- section：Conclusion

- locator：局限性段落

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限包括模型简单、样本规模有限、课堂谈判与现实高额交易不同、未研究用户对区块链的感知以及系统融资/定价问题。

- rhetorical_function_cn：承认研究边界并规划未来方向。

- depends_on_cn：研究设计。

- sets_up_cn：为后续研究留下开放问题。

- evidence_pointer：Conclusion, 局限性段

### 59. 最后一段

- order：59

- section：Conclusion

- locator：最后一段

- move_code：CONTRIBUTION

- paraphrase_cn：作者相信多主体认证最终可能通过更高fit信号减少信息不对称，从而解决柠檬市场问题。

- rhetorical_function_cn：以有希望的远景收束全文，强化研究意义。

- depends_on_cn：研究结果。

- sets_up_cn：为未来研究提供终极愿景。

- evidence_pointer：Conclusion, 最后一段

## 写作技术

- gap_construction_cn：先用量化现实损失（89亿欧元里程欺诈、18%过度支付）和中介收益掠夺建立“现有缓解机制仍不充分”的认知，再指出区块链虽能产生多主体认证，但“认证只是资源，不是解决方案”，并且已有信用市场模型无法直接迁移、缺乏经验分析，从而把缺口定义为“高fit信号的市场影响尚未被理论和实验验证”。

- signposting_cn：引言末尾有全文路线图；每个主要部分开头用“we now present”“we first explain”“In the following, we present”等预告；假设部分把五个假设紧密排列；结果部分按假设顺序逐一报告并配表格。

- transition_logic_cn：从现有信号的局限转向产品历史认证；从区块链子系统分析转向“coined term”；从“gap”转向“motivates our research study”；从模型命题转向“Hypotheses Development”；从假设转向“Experimental Methods”；从实验结果转向“Discussion”，每一段都以理论或结果中的未解决问题为下一阶段的动因。

- claim_evidence_rhythm_cn：每个假设先陈述理论/模型预测，再叙述对应表格中的均值和t检验/p值，最后用“support H1/H2/...”明确结论。证据以桌面表格形式直接嵌入正文，保持主张与证据紧邻。

- benchmark_narrative_cn：文章没有使用传统基准数据集，而是把“仅经销商信号”同时作为理论模型中的基准（Proposition 1）和实验中的对照组（Instance A），把“多主体认证高fit信号”作为处理（Proposition 2/Instance B），通过模型预言、实验设计、统计检验三层嵌套完成对比叙事。

- theory_return_cn：结果验证假设后，讨论部分重新打开社会技术框架，把经验差异解释为熵降低、affordance实现和系统和谐；再以“信号fit的三来源”返回信号理论，以“区块链唯一性条件”返回区块链经济学，使实验数据不是一次性性能结果而是理论命题的证据。

- contribution_positioning_cn：在讨论开头用Kohli和Liang的区块链研究框架给自己定位：应用域为二手车市场但可推广到其他信息不对称市场，核心构念为资产文档化的信号有效性，结果为市场动态和社会福利，方法为建模与实验，从而把论文嵌入IS学科议题。

- novelty_protection_cn：通过四种方式防止贡献退化为一次性结果：一是用解析模型把高fit信号与熵联系起来，说明结果有理论必然性；二是用CARA效用函数做稳健性检验；三是引入“区块链目前是唯一能实现这些目标的技术，但其他技术也可”的边界条件；四是在讨论和结论中反复强调对实践者/政策制定者的设计知识和商业模式含义。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用具体损失数字和现实市场经验说明一个经典经济问题仍然重要。

- research_job_cn：识别一个具有明确理论基准（如柠檬市场）且存在现实代价的问题域。

- required_evidence_cn：至少一个量化市场失灵指标（损失金额、过度支付比例等）或有权威来源的行业数据。

- transition_to_next_cn：从“现有缓解机制虽有效但仍不够”过渡到“需要新的方案”。

#### 2. 2

- step：2

- writing_job_cn：综述现有缓解方案并逐一指出其结构性局限。

- research_job_cn：系统梳理经销商信号、个体认证、单一第三方认证的不足，明确为什么需要新制品。

- required_evidence_cn：对每种现状的机制性解释和至少两个独立缺陷来源。

- transition_to_next_cn：引入新技术（区块链）作为可能的使能者，形成缺口。

#### 3. 3

- step：3

- writing_job_cn：引入一个可解释新制品如何改变问题的理论框架，并给出新构念的定义。

- research_job_cn：用理论框架（如社会技术工件/affordance）把技术特性映射为用户行动潜力，定义新构念。

- required_evidence_cn：能够独立定义的核心构念；技术特性与行动潜力之间的逻辑链条。

- transition_to_next_cn：从“为什么可能有效”过渡到“具体带来什么市场变化”。

#### 4. 4

- step：4

- writing_job_cn：构建一个形式模型，把新构念转化为可计算参数和比较静态命题。

- research_job_cn：在已有经济模型基础上加入代表新构念的参数化差异，推导价格/交易命题。

- required_evidence_cn：至少一个可检验命题；普适性检验（如替代效用函数）。

- transition_to_next_cn：把模型价格/交易结论结合行为文献转化为可检验假设。

#### 5. 5

- step：5

- writing_job_cn：用一组有序的假设把模型预测转为可观察变量。

- research_job_cn：确保每个假设对应一个可测指标和明确的方向性预测。

- required_evidence_cn：变量定义和预期方向；每个假设与模型/文献的对应关系。

- transition_to_next_cn：说明需要受控实验来检验人类行为，进入实验设计。

#### 6. 6

- step：6

- writing_job_cn：设计实验平台和操作化处理，并详细说明外部效度和内部效度控制。

- research_job_cn：建立与现实严格对应的实验环境，设置对照组/处理组，随机化和预测试。

- required_evidence_cn：实验材料来源（如真实平台、真实数据）、随机化方案、预测试结果。

- transition_to_next_cn：数据收集完成后，进入统计检验。

#### 7. 7

- step：7

- writing_job_cn：按假设顺序报告统计结果，每个结果与对应表格紧邻。

- research_job_cn：进行均值/比例检验，报告p值，说明哪些假设被支持。

- required_evidence_cn：每组统计量和p值；样本量和数据清理说明。

- transition_to_next_cn：把统计结果放到理论框架和现实含义中讨论。

#### 8. 8

- step：8

- writing_job_cn：在讨论中把经验结果升华为机制、边界条件和设计原则，并回应引言缺口。

- research_job_cn：从数据差异识别可复用的设计知识，定义适用边界，提出来来研究。

- required_evidence_cn：机制解释必须能同时覆盖模型推导和实验观察；边界条件要有明确前提。

- transition_to_next_cn：在结论中总结对学者/实践者/政策者的不同贡献和局限。

### most_transferable_moves_cn

1. 用现实损失数字使经典理论问题紧迫化

2. 通过理论框架定义新构念并形成affordance链条

3. 先建模后实验，让实验检验有清晰的理论基准

4. 把处理变量操作化为信息结构差异而非技术本身

5. 在每个假设后紧邻表格和p值，形成稳定的证据节奏

6. 在讨论中明确边界条件和可迁移条件，避免技术炒作

### resource_intensive_or_nonstandard_parts_cn

1. 与Cardossier真实区块链联盟的深入合作

2. AutoScout24平台数据与界面授权

3. 瑞士行业伙伴提供的标准评估表和专家估值

4. 持续一年的预测试和迭代设计

5. 105名MBA学生各扮演两个角色的大型实验室实验

### what_not_to_copy_superficially_cn

1. 不能只写“区块链提高市场效率”而不操作化具体的信息结构

2. 不能把实验室中的价格偏差直接等同于社会福利或公平性

3. 不能在没有模型的情况下用“熵”作为事后解释

4. 不能声称“更高fit”已被测量，如果实验只观察价格和收益

5. 不能忽略样本量和单一实验情境对因果推断的限制

- single_best_description_of_the_routine_cn：用经典经济失效给出问题，用社会技术理论定义新构念，用解析模型把构念转成市场预测，再用一个高度现实化的实验室市场游戏检验预测，最后把行为差异解释为熵降低和信号fit提高，从而输出可复用的区块链系统设计知识。

## 分析边界

PDF/OCR转换存在少量公式符号异常（如½1;2m-1�、字符错位），但核心命题、实验结果和论证结构清晰可辨；部分参考文献页码和表格细节可能因OCR不完整，不影响整体研究链重建；没有在线附录全文，但正文已足够支撑分析。
