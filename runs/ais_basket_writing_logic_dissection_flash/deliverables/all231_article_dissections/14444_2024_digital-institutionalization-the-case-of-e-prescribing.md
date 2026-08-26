# Digital Institutionalization: The Case of E-Prescribing

- 作者：Owen Eriksson; Sten-Erik Öhlund
- 年份 / 期刊：2024 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00845
- 源文件：14444_2024_digital-institutionalization-the-case-of-e-prescribing.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.88

## 文章级论证概况

- 核心问题：如何设计一种数字基础设施，使其能够发展出一个数字制度系统（digital institutional system）？

- 制品与设计：核心制品是一个称为NEF（National E-prescription Format）的交换合同（exchange contract）。它将法规和国际标准转译为一系列可编码、可自动验证的构成性规则（分类规则、创建规则、验证规则），并作为治理机制与数字实践接口（DPI），将质量控制从配药环节前推到处方创建环节。

- 客观结果：实施后，有错误的电子处方集比例从98.6%降至0.9%；错误总数从约597万降至约1.38万；R类（拒绝）错误不再到达药房；随后法规逐步承认电子处方为原件，最终瑞典电子处方采纳率达99%。

- 核心贡献：提出“数字制度化”（digital institutionalization）这一中程规定性理论，以及三条设计原则：分析制度环境、设计交换合同、确保数字制度实体的质量与合法性；主张数字基础设施设计必须在制度情境中主动进行，数字制度实体的创建与交换是制度化的核心。

- 整篇论证链：文章从数字化普遍化和数字基础设施设计的bootstrap/adaptability挑战切入，指出现有文献重点解释自底向上的涌现式演化，却忽略了制度情境对设计的使能与合法化作用。作者引入制度理论和数字制度实体概念，将瑞典电子处方案例中的电子处方重新定义为可复制、耐用、可交流的数字制度实体。NEF交换合同的设计和自动验证规则将法规转化为可执行的技术与治理机制；实施后用前后各一个月的全国注册库数据证明错误率大幅下降。作者进一步展示设计者还参与修改注册法、推动电子处方获得原件地位，最终形成宏观规则与微观实践双向递归的数字制度化模型。通过理论反思，他们将局部成功上升为三条可复用的设计原则，并主张该贡献可迁移到其他数字制度实体领域。

## 类型与写作弧线判定

- 论文主类型判定：文章明确按照设计科学文章模式组织，核心产出是基于现实需求（电子处方质量问题）构建制品（交换合同），在真实环境中实施与评价，最终提炼为设计原则。研究采用行动设计研究（ADR），但其主题仍是“需求—构建—评价—设计知识”，而非从理论命题推导假设再用实验检验，也非以benchmark数据集为主要证据的计算制品研究。

- 主导写作弧线判定：文章从现实问题（数字基础设施演化中的制度缺口）出发，引入制度理论和言语行为理论，设计并实施交换合同，通过前后对照数据检验效果，最后在结论部分返回到数字制度化理论贡献与设计原则。这条弧线是“问题—理论—设计—检验—回到理论”。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：阶段1基于实践问题感知形成研究问题；阶段2创造新交换合同制品；阶段3实施部署决策；阶段4用前后对照数据检验效果；阶段5用药房调查补充合法性证据；阶段6分析法规制度环境的改变；阶段7通过长期案例研究与理论反思将经验升华为数字制度化模型和设计原则。每一阶段都在回答前一段留下的不确定性，并逐步把证据从局部性能提升推向制度化与设计知识。

### studies_or_phases

#### 1. 问题形成：电子处方质量缺陷的实践感知（ADR阶段1）

- order：1

- name_cn：问题形成：电子处方质量缺陷的实践感知（ADR阶段1）

- question_cn：电子处方规模化扩展的关键瓶颈是什么？质量问题是否只是技术问题？

- inputs_and_setting_cn：2003年作者2作为NPC电子处方支持团队服务负责人的日常工作；事故报告、与县议会、药房和总部的联系；实践现场。

- designed_or_compared_object_cn：无制品；对电子处方质量问题及其与处方实践关系的认知。

- baseline_control_or_counterfactual_cn：当时的旧交换合同与网关机制造成的质量问题作为基线。

##### objective_metrics

1. 电子处方质量缺陷

2. 扩展瓶颈

- analysis_method_cn：内嵌从业者观察与问题论证（ADR问题形成）。

- main_result_cn：确认质量问题并非纯技术问题，必须改变电子处方实践；推动NEF项目立项。

- argumentative_role_cn：确定实践问题，为后续设计提供方向和理由。

- remaining_uncertainty_cn：如何通过设计改善质量，规则能否被形式化并自动验证。

- link_to_next_phase_cn：问题定义引出新交换合同（NEF）的设计。

##### evidence_pointers

1. Section 3.3.2，Author 2 作为 NPC 服务负责人的经历

2. Section 3.2，2000年NPC项目启动与2003-2004年份额增长和质量需求

#### 2. 设计新交换合同：将制度知识与标准转译为可验证规则

- order：2

- name_cn：设计新交换合同：将制度知识与标准转译为可验证规则

- question_cn：如何把旧交换合同、国际标准、国家法规和处方实践转化为一组可编码、可验证的显式规则？

- inputs_and_setting_cn：旧交换合同（EDIFACT和XML两种消息）、MEDPRE 2000、ENV 13607、SIS 2002、瑞典法规（LVFS 1997:10等）、Häggström et al. (2007)和Öhlund (2007)的基本文档。

- designed_or_compared_object_cn：新交换合同（NEF）取代旧交换合同；决策放弃EDIFACT、放弃网关转换、在发送模块中实现自动验证。

- baseline_control_or_counterfactual_cn：旧交换合同+网关的灵活性/宽松规则作为对比。

##### objective_metrics

1. 规则可自动验证性

2. 规则明确性

3. 字段和引用完整性

- analysis_method_cn：言语行为理论启发的规则工程，将法规解释为分类、创建、验证规则；XML schema编码。

- main_result_cn：生成包含分类规则（表1）和创建规则（表2：结构、数据、动态一致性、标识）的交换合同，支持自动验证。

- argumentative_role_cn：展示理论/制度知识如何转化为具体制品设计选择。

- remaining_uncertainty_cn：严格验证是否会导致大规模流程中断；实际错误减少幅度未知。

- link_to_next_phase_cn：设计完成后需要决定实施策略（错误状态、拒绝机制）。

##### evidence_pointers

1. Section 4.2-Decisive Design Decisions

2. Section 4.3 Design of the New Exchange Contract

3. Table 1, Table 2

#### 3. 实施与部署决策：强制拒绝与反馈机制

- order：3

- name_cn：实施与部署决策：强制拒绝与反馈机制

- question_cn：如何实施严格验证以改变实践，同时控制风险？

- inputs_and_setting_cn：县议会、NPC、处方模块供应商、药剂师和处方者；认证流程；反馈消息（应用错误和确认消息）。

- designed_or_compared_object_cn：错误状态的分类：警告(W)与拒绝(R)；选择强制拒绝而非仅记录错误。

- baseline_control_or_counterfactual_cn：渐进式仅记录错误而不强制执行的反事实方案。

##### objective_metrics

1. 拒绝错误是否干扰流程

2. 错误反馈能否被接收方理解

- analysis_method_cn：利益相关者协商、教育和认证实施。

- main_result_cn：县议会同意强制拒绝，发送端和接收端明确了处理W/R错误的操作流程。

- argumentative_role_cn：说明设计原则中的稳定性/灵活性平衡和治理机制如何落地。

- remaining_uncertainty_cn：实施后错误减少的实际规模和是否涌现新的问题。

- link_to_next_phase_cn：为前后定量评价提供干预定义。

##### evidence_pointers

1. Section 4.4 Governance Function of the Exchange Contract

2. Section 4.5 Implementation and Evaluation 开头部分

#### 4. 前后对照定量评价：错误率大幅下降

- order：4

- name_cn：前后对照定量评价：错误率大幅下降

- question_cn：新交换合同的实施是否降低了电子处方错误并提高了质量？

- inputs_and_setting_cn：国家电子处方注册库中的XML电子处方；实施前2008年4月3日-5月3日，实施后2009年4月3日-5月3日；样本量如正文。

- designed_or_compared_object_cn：同一注册库中实施前后各一个月的电子处方，按交换合同规则自动验证。

- baseline_control_or_counterfactual_cn：实施前一个月作为基线；旧系统缺乏统一验证造成高错误作为对照。

##### objective_metrics

1. 有至少一个错误的处方集比例

2. 错误总数

3. R和W状态错误数量

- analysis_method_cn：规则自动验证、连续抽样、描述性对比（表3）。

- main_result_cn：有错误处方集比例从98.6%降至0.9%；错误总数从5,970,737降至13,764；R错误不再到达药房。

- argumentative_role_cn：提供最有力的效果证据：设计确实改变了实践并极大降低错误。

- remaining_uncertainty_cn：错误降低是否意味着系统获得实际合法性和持续制度化？

- link_to_next_phase_cn：引出药房调查和法规变化等制度合法性证据。

##### evidence_pointers

1. Section 4.5 Implementation and Evaluation

2. Table 3

#### 5. 补充评价：药房调查作为实用合法性的证据

- order：5

- name_cn：补充评价：药房调查作为实用合法性的证据

- question_cn：药房从业者如何看待新电子处方系统的安全性、效益和沟通改进？

- inputs_and_setting_cn：Hammar等人(2010)实施后全国药房调查结果。

- designed_or_compared_object_cn：无设计操纵；调查受访者对系统的评价。

- baseline_control_or_counterfactual_cn：无直接对照；调查证据服务于合法性主张。

##### objective_metrics

1. 认为安全、患者受益、成本有效、改善沟通的受访者比例

- analysis_method_cn：引用已发表的调查统计。

- main_result_cn：大多数受访者认为电子处方安全、有效、患者受益并改善沟通。

- argumentative_role_cn：支撑“系统具有实用合法性”的主张，为制度化过程提供微观接受证据。

- remaining_uncertainty_cn：实用合法性并不能完全等于规范合法性；法规是否跟进尚未说明。

- link_to_next_phase_cn：转向法规变化的宏观合法性论证。

##### evidence_pointers

1. Section 4.5 末尾，Hammar et al. (2010) survey

#### 6. 制度环境改变分析：从注册法修订到强制电子处方

- order：6

- name_cn：制度环境改变分析：从注册法修订到强制电子处方

- question_cn：数字制度化是否需要在宏观制度层面进行有意的变更？

- inputs_and_setting_cn：瑞典处方注册法（1996:1156）、2005修正法律（SFS 2005:259）、2009规定（LVFS 2009:13）、2021/2022规定（HSLF-FS 2021:75），以及NEF项目组向NPC提出的修改建议。

- designed_or_compared_object_cn：电子处方相对于纸质处方的法律地位：从禁止永久存储到同等原件再到强制电子化。

- baseline_control_or_counterfactual_cn：旧法规中电子处方必须以打印件存放并删除注册记录作为基线。

##### objective_metrics

1. 法律是否允许电子处方生命周期存储

2. 是否授予电子处方与纸质同等地位

3. 是否强制电子处方

- analysis_method_cn：历史制度分析，案例叙事。

- main_result_cn：2005年法律允许存储；2009年法规承认电子处方原件地位；2021/2022年强制全面电子处方。

- argumentative_role_cn：证明制度化是宏观规则与微观实践双向调整的过程，设计者主动介入制度环境。

- remaining_uncertainty_cn：除设计外，政治、财务和组织因素也促成了成功；无法在此展开。

- link_to_next_phase_cn：理论模型需要将这些案例分析转化为设计原则。

##### evidence_pointers

1. Section 4.6 Changing the Institutional Context

2. Section 6.1 DP1 制度环境分析

3. Section 7.3 局限性提及政治等因素

#### 7. 长时间案例研究与理论构建：数字制度化模型与设计原则

- order：7

- name_cn：长时间案例研究与理论构建：数字制度化模型与设计原则

- question_cn：如何将NEF项目的设计经验一般化为数字基础设施设计和制度化的规定性理论知识？

- inputs_and_setting_cn：2012-2013年关于瑞典电子处方演化的档案和关键知情人访谈；2014年瑞典eHealth Agency案例分析；数字基础设施文献、制度理论、言语行为理论。

- designed_or_compared_object_cn：NEF项目作为数字基础设施演化案例与既有文献中的自底向上/涌现观点对比。

- baseline_control_or_counterfactual_cn：文献中ANT、复杂系统、批判实在论对演化的解释作为对比基线。

##### objective_metrics

1. 基础设施是否持续增长

2. NEF干预是否关键

3. 制度实体质量的重要性

- analysis_method_cn：纵向档案分析、访谈、理论反思与形式化。

- main_result_cn：提出数字制度化双向过程模型（宏观交换合同与微观实践递归）和三条设计原则。

- argumentative_role_cn：把局部结果上升为middle-range prescriptive theory和设计知识。

- remaining_uncertainty_cn：设计原则的有效性依赖单一高成功案例，无法完全排除情境偶然性。

- link_to_next_phase_cn：进入结论部分对可推广性、局限和未来研究的讨论。

##### evidence_pointers

1. Section 3.3.4 Reflection and Learning

2. Section 3.3.5 Formalization and Learning

3. Section 5 Digital Institutionalization

4. Section 6 Design Principles

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 数字制度化过程正在根本性改变社会

2. PHENOMENON: 数字制度实体如处方、货币、保险、税收被数字化并跨情境交换

3. LIMITATION: 现有数字基础设施设计研究很少考虑制度情境对设计的合法化作用

4. GAP: 需要将制度情境纳入设计的方法

5. METHOD_JUSTIFICATION: 采用设计师批判视角，在制度情境中开发交换契约

6. CONTRIBUTION: 提出数字制度化设计原则并提供言语行为理论和制度理论的理论反思

### introduction_moves

1. CONTEXT: 数字化成为新常态，需要可扩展且合法的数字基础设施

2. PRIOR_KNOWLEDGE: 数字基础设施设计聚焦互操作性和演化挑战

3. LIMITATION: 自底向上和涌现视角占主导，制度情境未获充分关注

4. WHY_GAP_MATTERS: 数字基础设施不仅适应制度情境，还须改变它，合法性不可回避

5. RQ_OR_OBJECTIVE: 提出研究问题：如何设计数字基础设施以发展数字制度系统

6. PHENOMENON: 瑞典电子处方从技术上看很简单却耗时数十年实现99%采纳

7. STUDY_OVERVIEW: 预告文章按设计科学模式组织

### theory_and_knowledge_moves

1. THEORY_INTRO: 引入制度理论、制度逻辑、制度化过程与合法性概念

2. THEORY_PROPOSITION: 制度系统由规则/规范与制度实体构成，制度化通过脚本编码与微观实践实现

3. MECHANISM: 数字制度实体是基础设施中真正被交换的对象，具有可复制、耐用、可交流的要求

4. REQUIREMENT: 数字制度实体需由标准化构成规则支撑

5. GAP: 制度情境对设计的使能作用与设计者视角缺失，缺乏规定性理论

### artifact_design_moves

1. REQUIREMENT: 需要将质量控制推到电子处方创建源头，摆脱网关隐藏错误

2. DESIGN_FEATURE: 选择XML、放弃EDIFACT，定义分类规则、创建规则和自动验证

3. DESIGN_FEATURE: 交换合同作为API契约、数字实践接口和治理机制

4. MECHANISM: 交换合同通过错误状态、反馈和认证改变社会互动

5. METHOD_JUSTIFICATION: 使用前后对照和自动验证规则测量合规性

### evaluation_moves

1. METHOD_JUSTIFICATION: 定量方法、连续抽样和规则自动验证的选择理由

2. BENCHMARK_OR_CONTRAST: 旧交换合同+网关作为基线，实施前一个月数据作为反事实

3. RESULT: 错误率从98.6%降至0.9%，总错误数从597万降到1.38万

4. ROBUSTNESS_OR_BOUNDARY_TEST: 大规模实施无反弹，药房调查支持合法性，国际扩散率比较支持外部有效性

### discussion_and_contribution_moves

1. CONTRIBUTION: 提出数字制度化中程理论，核心是数字制度实体的生成力

2. BOUNDARY_CONDITION: 主张结论可迁移到其他制度实体，但复杂性和要求不同

3. LIMITATION_AND_FUTURE: 承认政治、财务、组织因素未展开，未来需研究网络化治理和合法性获得

4. THEORY_PROPOSITION: 数字制度化是宏观交换契约与微观实践的双向递归过程

## 理论/知识到设计的翻译

### 知识/理论基础

1. 制度理论（新制度理论：Barley & Tolbert, 1997; Thornton et al., 2012; Hasselbladh & Kallinikos, 2000）

2. 言语行为理论（Searle, 1969; 1995; 2006; Habermas, 1976）

3. 数字基础设施文献（Hanseth & Lyytinen, 2010; Henfridsson & Bygstad, 2013）

4. 合法性理论（Suchman, 1995; Deephouse & Suchman, 2008）

5. 卫生信息标准（ENV 13607, MEDPRE 2000, SIS 2002）

6. 瑞典法规（LVFS 1997:10; SFS 2005:259; HSLF-FS 2021:75）

- 理论—设计耦合：partial

- 耦合判定理由：言语行为理论和制度理论提供了‘电子处方是制度实体而非单纯数据文件’‘制度实体需要构成规则’‘规则要可编码和验证’等概念基础，并直接影响了设计者制定显式规则系统的方向；但具体交换合同的内容、XML schema、认证流程、错误类型等技术选择主要由国际标准、国家法规和工程实践驱动。制度理论更多用于事后解释制度化过程和生成设计原则，而不是理论推导出全部设计参数。因此属于部分耦合，而非完全前瞻性理论推导或完全无关。

- 理论到设计翻译链：制度实体理论（Searle）→ 电子处方应被视为具有权利/义务的数字制度实体→ 必须通过构成规则创建和识别→ 交换合同中的分类规则和标识规则→ 自动验证并减少标识类错误；言语行为理论→ 处方是高质量沟通行为→ 需要显式规则保证沟通完整→ 结构、数据、动态一致性规则→ 前后数据证明沟通错误大幅减少；制度化理论（Hasselbladh & Kallinikos）→ 制度实体需可复制、耐用、可交流→ 使用XML schema和可自动验证规则避免网关隐藏错误→ 拒绝/警告反馈使制度实体在跨情境交换中保持质量；合法性理论→ 制度环境是设计合法性的前提→ 设计原则DP1/DP3要求分析法规并主动调整制度环境→ 法规变革和药房调查支撑合法化；Barley & Tolbert的脚本理论→ 交换合同是宏观脚本，微观实践必须执行→ 交换合同作为治理机制并建立反馈→ 错误率下降和法规变化显示双向制度化。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：制度实体由构成规则创建，代表权利，协调跨实践的社会互动（Searle; Hohfeld）

- mechanism_cn：电子处方作为数字制度实体，必须通过分类规则和标识被识别和创建，才能让药剂师和患者信任其效力

- design_requirement_cn：交换合同必须定义构成性分类规则和标识机制

- artifact_choice_cn：新交换合同中的类别（处方、产品包、患者、处方者等）和标识符（PrescriptionItem ID, Product ID等）

- evaluated_contrast_cn：对比旧合同下标识类错误（Incorrect code enumeration, Invalid Prescriber Code等）

- objective_result_cn：错误数从百万量级降至个位或数十，如Incorrect code enumeration从1,704,100降至26

##### evidence_pointers

1. Section 4.3.1, Table 1

2. Table 3

#### 2. 2

- theory_or_knowledge_claim_cn：言语行为理论把沟通视为行为，电子处方创建应被设计为高质量沟通行为（Searle; Goldkuhl & Lyytinen）

- mechanism_cn：若处方字段缺失、格式错误或内容不一致，药剂师和患者无法安全解读，导致调剂障碍或用药风险

- design_requirement_cn：将法规转译为显式的结构、数据、动态一致性和标识规则，并自动验证

- artifact_choice_cn：表2中的四类构成规则；XML schema编码；创建点自动有效性控制

- evaluated_contrast_cn：实施前与实施后各一个月所有XML电子处方按统一规则验证

- objective_result_cn：有错误处方集比例从98.6%降至0.9%；总错误从5,970,737降至13,764

##### evidence_pointers

1. Section 4.3.2, Table 2

2. Section 4.5, Table 3

#### 3. 3

- theory_or_knowledge_claim_cn：制度实体需可复制、耐用、可交流，标准化符号方案是前提（Hasselbladh & Kallinikos, 2000）

- mechanism_cn：网关转换会隐藏和修复错误，使实体在跨情境交换中失真；源头验证则保证实体从创建起就标准化

- design_requirement_cn：停止依赖网关，将质量控制推到电子处方创建源头

- artifact_choice_cn：废弃网关，引入自动验证和错误反馈（W/R状态）

- evaluated_contrast_cn：旧系统与NEF系统在错误状态、错误到达药房与否的差异

- objective_result_cn：R类错误不再到达药房；实践中的质量责任从调剂端转移到处方端

##### evidence_pointers

1. Section 4.2

2. Section 4.5

#### 4. 4

- theory_or_knowledge_claim_cn：合法性分规范合法性与实用合法性，制度设计需考虑制度环境（Suchman, 1995; Bitektine & Haack, 2015）

- mechanism_cn：设计若不符合法规和标准，则缺乏规范合法性；若不能满足实践效用和扩散，则缺乏实用合法性

- design_requirement_cn：设计交换合同前必须先分析制度环境，并在错误和需求变化时主动调整制度环境

- artifact_choice_cn：DP1分析制度环境；NEF项目推动2005年注册法修订、2009年法规承认电子处方原件地位

- evaluated_contrast_cn：旧注册法禁止电子处方永久存储与2009年后电子处方获得原件地位

- objective_result_cn：电子处方被正式合法化为原件实体；2021/2022年全面强制电子处方

##### evidence_pointers

1. Section 4.6

2. Section 6.1 DP1

#### 5. 5

- theory_or_knowledge_claim_cn：制度化是宏观脚本与微观实践的双向递归过程（Barley & Tolbert, 1997）

- mechanism_cn：交换合同作为脚本规定微观实践，但微观实践中的错误和新需求又要求调整交换合同和法规

- design_requirement_cn：交换合同应作为治理机制并提供反馈回路

- artifact_choice_cn：错误状态反馈、自动验证、错误监控和持续维护

- evaluated_contrast_cn：从旧系统不规范反馈到新系统以错误统计驱动持续改进

- objective_result_cn：错误降至很低并保持，基础设施持续增长，制度化大规模扩散

##### evidence_pointers

1. Section 4.4

2. Section 5.3

## 评价逻辑

### evaluation_modes

1. 前后对照定量评价：实施前后各一个月的全国XML电子处方样本，按交换合同规则自动验证

2. 历史案例研究：文档分析、关键知情人访谈，2012-2013年纵向重建

3. 补充调查证据：引用Hammar等人2010年药房调查

4. 国际比较：与欧洲和世界其他电子处方项目比较扩散率

- why_these_evaluations_cn：由于ADR难以实现随机受控实验，作者利用真实干预形成的自然前后时序，结合规则可自动验证的特点构成准实验；用案例研究补充制度变迁和长期演化证据；用药房调查补充实践接受度；用国际比较支持外部有效性。多种评价方式分别对应“性能提升”“制度化过程”“合法性”“可推广性”四类主张。

- benchmark_and_contrast_chain_cn：先在旧交换合同+网关条件下测得错误基线；实施新交换合同后在同一注册库窗口获得干预后数据，构成主要对照；随后把瑞典扩散率与欧洲世界其他项目比较，作为外部基准；最后把Sahay等人高抽象层面的制度重建设计建议与本文具体设计原则对比，显示本文原则更可操作。

### claim_evidence_ledger

#### 1. 新技术主张：新交换合同大幅降低错误率

- claim_cn：新技术主张：新交换合同大幅降低错误率

- evidence_cn：自动规则验证下的前后对比数据（98.6%→0.9%；错误总数5,970,737→13,764）

- strong_or_weak_cn：较强：同口径大样本、自动验证减少测量偏差

#### 2. 制品主张：源头验证而非网关是关键设计特征

- claim_cn：制品主张：源头验证而非网关是关键设计特征

- evidence_cn：设计决策描述 + 错误类型分布变化；但未对网关移除之外的其他变量做正式解构

- strong_or_weak_cn：中等：有直接过程支持，但缺少对模块差异或外部政策变化的统计控制

#### 3. 机制主张：交换合同作为治理机制改变数字实践界面

- claim_cn：机制主张：交换合同作为治理机制改变数字实践界面

- evidence_cn：R错误不再到达药房，流程从配药端前移到处方端；案例和访谈支持

- strong_or_weak_cn：中等：依靠过程证据和理论解释，没有直接测量“界面责任转移”

#### 4. 边界主张：这组设计原则适用于其他数字制度实体

- claim_cn：边界主张：这组设计原则适用于其他数字制度实体

- evidence_cn：制度实体概念（货币、保险、税收等）的一般性论证 + 国际比较

- strong_or_weak_cn：较弱：属于理论外推，未在其他领域做实证

#### 5. 设计知识：三条设计原则可复用

- claim_cn：设计知识：三条设计原则可复用

- evidence_cn：基于单一高成功案例的反思提炼

- strong_or_weak_cn：中等：高质量成功案例，但缺少多案例横向对照

#### 6. 理论贡献：数字制度化是双向递归过程

- claim_cn：理论贡献：数字制度化是双向递归过程

- evidence_cn：法规调整与微观实践变化的历史关联，Barley & Tolbert理论框架嵌入

- strong_or_weak_cn：中等：案例分析支持，但无统计因果识别

- internal_validity_strategy_cn：利用制度化规则的可自动验证消除了测量误差；前后样本取同一日历时段（4月3日-5月3日）减少季节影响；同为国家注册库数据保持口径一致；设计者内嵌保证了干预细节完整记录；错误类型和状态（W/R）给出可检验的操作化定义。

- external_validity_strategy_cn：将瑞典电子处方扩散率与其他国家（Kierkegaard, 2013; Aanestad et al., 2017; Pereira et al., 2018）比较，说明案例处于世界领先；将一般概念从“处方”扩展到金钱、保险、税收等数字制度实体；把设计原则抽象到制度和实践层面以便迁移。

- what_is_not_actually_tested_cn：没有随机对照或反事实案例；药房调查是自评而非客观行为结果；法规变化与干预的因果链主要靠叙事而非统计识别；设计原则未在其他制度领域重复检验；W类部分错误（如Invalid reimbursement status和Invalid multiple choice）在实施后反而上升，文章未深入解释这些新增错误的来源与影响。

## 贡献闭环

- technical_claim_cn：一个更严格、可自动验证的交换合同可以显著降低跨组织交换的电子处方错误率，从98.6%错误处方集降到0.9%。

- artifact_claim_cn：关键设计特征——去除网关、将验证控制推向创建点、定义分类/创建/验证规则、以XML schema和在线注册库实现——导致改进。

- mechanism_claim_cn：交换合同作为脚本/治理机制，通过反馈和拒绝/警告状态，改变了社会互动的数字实践界面，把质量责任从配药端转移到处方端。

- boundary_claim_cn：该机制适用于存在明确构成性和规制性规则、制度实体可被形式化编码并跨组织交换的领域；其效果强弱依赖于合规、合法性和质量要求。

- reusable_design_knowledge_cn：三条设计原则：分析制度环境；设计交换合同（技术与实践并重，平衡稳定性和灵活性）；确保数字制度实体质量与合法性（自动验证、持续反馈、系统管理错误）。

- theoretical_contribution_cn：提出“数字制度化”作为middle-range prescriptive theory：数字制度化是宏观交换合同与微观实践的双向递归过程，数字制度实体的扩散是核心生成机制；主张基础设施设计不能仅被视为自底向上涌现，需要有意制度设计。

- how_discussion_closes_intro_gap_cn：开头指出现有基础设施文献忽略制度情境的使能和合法化作用、缺乏规定性理论；讨论部分重新引入这一缺口，声明本文通过设计者视角提供设计原则和理论，并将制度实体置于中心，同时通过国际比较和ADR内嵌研究为可推广性辩护。

- overclaim_or_unsupported_leaps_cn：从单案例断言设计原则有效性，且作者承认不能完全确定；‘如果未遵循设计原则就不会如此有效’是反事实主张，缺少对照；从质量提升直接跳到‘制度化’可能忽略政治、组织、市场等因素；将错误率下降解释为规范合法性提升，但规范合法性通常涉及更广泛社会认知，不只是合规错误减少。

## 句级写作动作图谱

### 1. 1.1 Background P1 S1–S2

- order：1

- section：Introduction

- locator：1.1 Background P1 S1–S2

- move_code：CONTEXT

- paraphrase_cn：数字化被定义为将数字化技术应用于更广泛社会与制度情境的过程，使数字技术基础设施化；它已成为生活和工作的新常态。

- rhetorical_function_cn：在文章开头建立宏观背景，指出数字化对社会的影响。

- depends_on_cn：无，全文起点

- sets_up_cn：为随后讨论数字基础设施设计和制度化问题做铺垫。

- evidence_pointer：Introduction 1.1 第一段前两句

### 2. 1.1 Background P1 S3–S4

- order：2

- section：Introduction

- locator：1.1 Background P1 S3–S4

- move_code：CONTEXT

- paraphrase_cn：数字化要求设计可扩展的数字基础设施，且这些基础设施必须以慎重方式设计以确保合法性和有效性。

- rhetorical_function_cn：引入数字基础设施和合法性作为核心议题。

- depends_on_cn：数字化定义

- sets_up_cn：为‘设计必须考虑制度环境’埋下伏笔。

- evidence_pointer：Introduction 1.1 第一段后两句

### 3. 1.1 Background P2 S1

- order：3

- section：Introduction

- locator：1.1 Background P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：引用Hanseth和Lyytinen将信息基础设施定义为共享、开放、异质、演化的社会技术系统，包含IT能力及用户、运维与设计社群。

- rhetorical_function_cn：给出数字基础设施的学术定义，建立术语。

- depends_on_cn：数字化定义

- sets_up_cn：为后文讨论基础设施演化和设计挑战提供概念工具。

- evidence_pointer：Introduction 1.1 P2

### 4. 1.1 Background P3 S1–S2

- order：4

- section：Introduction

- locator：1.1 Background P3 S1–S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：数字基础设施设计聚焦互操作性，设计师面临形式和经验、本地和情境之间的永久张力。

- rhetorical_function_cn：强调基础设施设计的根本困难。

- depends_on_cn：基础设施定义

- sets_up_cn：为说明已有理论无法解决制度情境问题提供背景。

- evidence_pointer：Introduction 1.1 P3

### 5. 1.1 Background P4 S1–S2

- order：5

- section：Introduction

- locator：1.1 Background P4 S1–S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：基础设施演化被概括为引导（bootstrap）问题与适应（adaptability）问题的张力，失败普遍且代价高昂。

- rhetorical_function_cn：引入基础设施演化的核心理论框架。

- depends_on_cn：基础设施设计挑战

- sets_up_cn：引出‘关键时期无法事先计划’的论点。

- evidence_pointer：Introduction 1.1 P4

### 6. 1.1 Background P4 S3–S4

- order：6

- section：Introduction

- locator：1.1 Background P4 S3–S4

- move_code：LIMITATION

- paraphrase_cn：失败原因在于关键时期难以预测，学者认为基础设施不能自上而下设计，控制是分布且零星的。

- rhetorical_function_cn：指出现有主流观点对自上而下设计和制度情境的忽视。

- depends_on_cn：基础设施演化理论

- sets_up_cn：为“我们需要有意设计”的论证提供反面对照。

- evidence_pointer：Introduction 1.1 P4后半部分

### 7. 1.1 Background P5 S1–S2

- order：7

- section：Introduction

- locator：1.1 Background P5 S1–S2

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：数字化同时需要自上而下的有意设计，因为基础设施必须合法并符合制度情境；而且基础设施不仅要适应制度情境，还要改变制度情境。

- rhetorical_function_cn：说明为什么现有文献的局限具有理论和实践后果。

- depends_on_cn：前面指出的自底向上观点

- sets_up_cn：直接引出研究问题和对制度情境的关注。

- evidence_pointer：Introduction 1.1 P5

### 8. 1.1 Background P6 S1–S3

- order：8

- section：Introduction

- locator：1.1 Background P6 S1–S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：数字基础设施对制度化过程根本重要，因为制度化发生在许多行为者以相似方式改变行为之时，常伴随基础设施技术转变；因此提出研究问题：如何设计数字基础设施以发展数字制度系统？

- rhetorical_function_cn：从背景收缩为明确研究问题。

- depends_on_cn：制度化与基础设施关系论证

- sets_up_cn：为全文研究设定中心目标。

- evidence_pointer：Introduction 1.1 P6

### 9. 1.1 Background 之后 P7 S1–S2

- order：9

- section：Introduction

- locator：1.1 Background 之后 P7 S1–S2

- move_code：PHENOMENON

- paraphrase_cn：作者采用负责数字制度系统设计、演化和合法性的设计者视角，用瑞典电子处方的演进来例证数字制度化。

- rhetorical_function_cn：引入案例和方法论视角。

- depends_on_cn：研究问题

- sets_up_cn：为后续案例描述提供定位。

- evidence_pointer：Introduction 1.1 P7

### 10. 1.2 案例段落 P7 S3–S5

- order：10

- section：Introduction

- locator：1.2 案例段落 P7 S3–S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：瑞典电子处方采纳率已达99%，是世界最成功案例之一，但实现过程漫长且困难；从技术上看只是改变媒介，却耗时如此之久，值得探究。

- rhetorical_function_cn：说明案例的重要性和研究价值。

- depends_on_cn：案例选择

- sets_up_cn：为‘为什么这不仅是技术问题’铺垫。

- evidence_pointer：Introduction 案例描述段落

### 11. 1.3 组织说明 P8 S1–S2

- order：11

- section：Introduction

- locator：1.3 组织说明 P8 S1–S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：案例是有目的的、成功的、可扩展的基础设施设计，最终改变了制度系统，可视为制度设计。

- rhetorical_function_cn：强调案例的榜样属性和设计科学价值。

- depends_on_cn：案例结果

- sets_up_cn：为贡献主张做准备。

- evidence_pointer：Introduction 案例段落

### 12. 1.4 文章结构 P9 S1–S2

- order：12

- section：Introduction

- locator：1.4 文章结构 P9 S1–S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：文章按设计科学文章模式组织，并预告各节内容。

- rhetorical_function_cn：提供全文路线图。

- depends_on_cn：前文论述

- sets_up_cn：帮助读者预期理论、案例、设计、评价和结论的顺序。

- evidence_pointer：Introduction 最后一段

### 13. 2.1 总结段 S1–S2

- order：13

- section：Literature Review

- locator：2.1 总结段 S1–S2

- move_code：GAP

- paraphrase_cn：文献综述表明制度情境及其使能与合法化作用没有被解释；文献关注涌现式自底向上，几乎没有规定性理论。

- rhetorical_function_cn：系统性归纳文献缺口。

- depends_on_cn：2.1节对三类理论的综述

- sets_up_cn：为引入制度理论和设计者视角提供理由。

- evidence_pointer：Section 2.1 总结段

### 14. 2.1 Hanseth & Lyytinen 段 S1–S3

- order：14

- section：Literature Review

- locator：2.1 Hanseth & Lyytinen 段 S1–S3

- move_code：LIMITATION

- paraphrase_cn：Hanseth和Lyytinen的设计理论虽然重要，但聚焦技术标准、假设自底向上，未考虑法规和设计合法性，也未解释制度情境如何使能自上而下设计和改变制度系统。

- rhetorical_function_cn：对准最接近的规定性理论指出其盲点。

- depends_on_cn：2.1节总结

- sets_up_cn：突出本文需要超越的技术和自底向上路径。

- evidence_pointer：Section 2.1 最后段

### 15. 2.2 P1 S1–S3

- order：15

- section：Theory

- locator：2.2 P1 S1–S3

- move_code：THEORY_INTRO

- paraphrase_cn：新制度理论将制度视为抽象、象征和社会结构，以及统治社会互动和实践的制度逻辑；宏观逻辑通过微观实践被复制。

- rhetorical_function_cn：引入制度理论的基本框架。

- depends_on_cn：前面的文献缺口

- sets_up_cn：为后文解释电子处方如何被制度化提供概念。

- evidence_pointer：Section 2.2 第一段

### 16. 2.2 P2 S1–S2

- order：16

- section：Theory

- locator：2.2 P2 S1–S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：制度化过程可由规则制定、最佳实践发展和规则更替构成；这涉及制度设计，即有意地创造和改变制度结构与行为。

- rhetorical_function_cn：把制度设计和制度化联系起来。

- depends_on_cn：制度理论框架

- sets_up_cn：为文章主张“设计者进行制度设计”提供理论依据。

- evidence_pointer：Section 2.2 第二段

### 17. 2.3.1 S1–S3

- order：17

- section：Theory

- locator：2.3.1 S1–S3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：语言预设制度系统；规则和规范是语言构造；规则分为规制性规则和构成性规则，构成性规则定义制度实体的创建条件。

- rhetorical_function_cn：说明规则类型及其在本体论上的优先性。

- depends_on_cn：制度理论和语言哲学

- sets_up_cn：为交换合同中的分类/构成规则设计提供基础。

- evidence_pointer：Section 2.3.1

### 18. 2.3.2 S1–S4

- order：18

- section：Theory

- locator：2.3.2 S1–S4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：制度实体代表权利，如处方、处方者、药剂师、医药产品；它们是制度系统的构成元素，在实践层面创建并协调社会互动。

- rhetorical_function_cn：引入制度实体概念并说明其地位。

- depends_on_cn：语言/制度本体论

- sets_up_cn：为电子处方重新定义为数字制度实体做铺垫。

- evidence_pointer：Section 2.3.2

### 19. 2.3.3 S1–S3

- order：19

- section：Theory

- locator：2.3.3 S1–S3

- move_code：MECHANISM

- paraphrase_cn：数字制度实体是数字基础设施的构成部分；跨情境交换的不是软件而是制度实体，正是这种交换使制度系统扩散。

- rhetorical_function_cn：解释数字基础设施中真正被交换的对象。

- depends_on_cn：制度实体概念

- sets_up_cn：为将设计焦点从软件/服务转向制度实体提供论证。

- evidence_pointer：Section 2.3.3

### 20. 2.3.3 S4–S5

- order：20

- section：Theory

- locator：2.3.3 S4–S5

- move_code：REQUIREMENT

- paraphrase_cn：数字制度实体必须可复制、耐用、可交流，因此需要标准化的符号方案（构成规则）来消除替代解释。

- rhetorical_function_cn：从制度实体属性推导设计需求。

- depends_on_cn：制度实体定义

- sets_up_cn：引出交换合同中规则设计的重要性。

- evidence_pointer：Section 2.3.3

### 21. 2.4 S1–S2

- order：21

- section：Theory

- locator：2.4 S1–S2

- move_code：GAP

- paraphrase_cn：主缺口是基础设施文献未重视制度情境和制度实体在设计和演化中的使能作用，导致设计和制度化关系的理解不足；这与作者在设计中亲身经历相矛盾。

- rhetorical_function_cn：明确陈述研究缺口，并用自己的经验增强说服力。

- depends_on_cn：前面综述和理论建构

- sets_up_cn：为下一节研究设置和案例做逻辑衔接。

- evidence_pointer：Section 2.4

### 22. 3.1 S1–S3

- order：22

- section：Research Setting

- locator：3.1 S1–S3

- move_code：PHENOMENON

- paraphrase_cn：案例制度系统是瑞典药品处方，由微观实践（开处方和配药）和宏观规则规范构成，并给出规制性规则例子。

- rhetorical_function_cn：描述研究对象的制度系统构成。

- depends_on_cn：前文的制度系统理论

- sets_up_cn：为后文说明规则如何被转译为设计提供情境。

- evidence_pointer：Section 3.1

### 23. 3.2 S1–S4

- order：23

- section：Research Setting

- locator：3.2 S1–S4

- move_code：PHENOMENON

- paraphrase_cn：瑞典电子处方从1983年世界首张电子处方开始，经历了引导阶段，2000年NPC项目推动份额增长，质量和合规需求随之涌现。

- rhetorical_function_cn：简述案例的早期历史和扩展背景。

- depends_on_cn：案例现象

- sets_up_cn：为NEF项目的启动做时间线铺垫。

- evidence_pointer：Section 3.2

### 24. 3.2 S5–S7

- order：24

- section：Research Setting

- locator：3.2 S5–S7

- move_code：PHENOMENON

- paraphrase_cn：2004年NEF项目启动，目的是设计和实施新的全国电子处方格式，并建立项目组和新的认证流程。

- rhetorical_function_cn：描述干预项目的启动。

- depends_on_cn：引导阶段和增长数据

- sets_up_cn：为后文设计、实施和评价提供事件背景。

- evidence_pointer：Section 3.2

### 25. 3.3.1 S1–S3

- order：25

- section：Method

- locator：3.3.1 S1–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为研究长期制度化过程，作者选择纵向研究；由于数字基础设施文献缺乏设计研究实例，设计研究（DR）更为合适。

- rhetorical_function_cn：解释方法选择的学术理由。

- depends_on_cn：研究问题和案例时间跨度

- sets_up_cn：为引入ADR提供铺垫。

- evidence_pointer：Section 3.3.1

### 26. 3.3.1 S4–S6

- order：26

- section：Method

- locator：3.3.1 S4–S6

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：研究过程起初并不明显属于哪种设计研究方法，回顾后才确认遵循了行动设计研究（ADR）。

- rhetorical_function_cn：说明ADR是回溯性确认的框架。

- depends_on_cn：作者的研究经历

- sets_up_cn：为后面的四阶段描述做框架准备。

- evidence_pointer：Section 3.3.1

### 27. 3.3.2 S1–S4

- order：27

- section：Method

- locator：3.3.2 S1–S4

- move_code：PHENOMENON

- paraphrase_cn：2003年作者2在NPC担任服务负责人时，从实践问题出发，认识到电子处方质量问题需要通过改变实践来解决，而非纯技术问题。

- rhetorical_function_cn：记录ADR问题形成阶段的实践出发点。

- depends_on_cn：引导阶段背景

- sets_up_cn：为后续设计动机和干预目标提供来源。

- evidence_pointer：Section 3.3.2

### 28. 3.3.3 S1–S3

- order：28

- section：Method

- locator：3.3.3 S1–S3

- move_code：REQUIREMENT

- paraphrase_cn：言语行为理论启发作者2定义一个与法规对齐的显式规则系统，规定如何执行高质量沟通行为，体现ADR将理论写入制品。

- rhetorical_function_cn：说明理论如何进入设计要求。

- depends_on_cn：言语行为理论引入

- sets_up_cn：为第4节交换合同的规则设计提供关键线索。

- evidence_pointer：Section 3.3.3

### 29. 3.3.3 S4–S6

- order：29

- section：Method

- locator：3.3.3 S4–S6

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作为内部设计者，作者系统地用现场笔记、邮件、备忘录、文档、规范、XML schema和测试文档建立案例数据库，确保设计过程可追溯。

- rhetorical_function_cn：说明数据收集的严谨性。

- depends_on_cn：作者内嵌角色

- sets_up_cn：支撑后续案例分析和评价的证据基础。

- evidence_pointer：Section 3.3.3

### 30. 3.3.3 S7–S11

- order：30

- section：Method

- locator：3.3.3 S7–S11

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者选择定量方法评价干预：规则作为自变量，合规作为因变量；由于规则可自动验证，用实施前后各一个月的连续样本构成受控式评价。

- rhetorical_function_cn：为量化评价提供方法论理由。

- depends_on_cn：交换合同的规则设计

- sets_up_cn：为第4.5节的前后对照数据做铺垫。

- evidence_pointer：Section 3.3.3

### 31. 4.1 S1–S3

- order：31

- section：Design and Evaluation

- locator：4.1 S1–S3

- move_code：PHENOMENON

- paraphrase_cn：要把纸质处方变为电子处方，这并非简单技术媒介替换；纸质与数字实践差异很大，电子处方由药剂师从注册库检索而非患者携带。

- rhetorical_function_cn：重新定义设计挑战的实质。

- depends_on_cn：制度实体概念

- sets_up_cn：为‘电子处方成为真正原件’的讨论铺路。

- evidence_pointer：Section 4.1

### 32. 4.1 S4–S6

- order：32

- section：Design and Evaluation

- locator：4.1 S4–S6

- move_code：MECHANISM

- paraphrase_cn：电子处方是存储在注册库中的数字制度实体，被药剂师检索后实现处方者的主张和药剂师的义务，因此注册库中的电子处方成了真正的机构实体。

- rhetorical_function_cn：解释数字制度实体如何成为社会互动的中介。

- depends_on_cn：S31的实践差异

- sets_up_cn：引出需要转变制度和观念的必要性。

- evidence_pointer：Section 4.1

### 33. 4.1 S7–S8

- order：33

- section：Design and Evaluation

- locator：4.1 S7–S8

- move_code：PHENOMENON

- paraphrase_cn：历史上纸质处方被视为真正实体，数字版本只是副本；从纸质转向电子处方需要新基础设施、制度环境、实践和人们原稿概念的改变，因而困难。

- rhetorical_function_cn：强调变化的制度性而非技术性。

- depends_on_cn：S32的数字实体观点

- sets_up_cn：为制度设计主张提供情境。

- evidence_pointer：Section 4.1

### 34. 4.2 S1–S4

- order：34

- section：Design and Evaluation

- locator：4.2 S1–S4

- move_code：LIMITATION

- paraphrase_cn：旧交换合同允许过多灵活性，导致电子处方质量差；网关只是隐藏和修复错误而非验证，且修复依赖旧错误知识，复杂难维护。

- rhetorical_function_cn：揭示旧系统的设计缺陷。

- depends_on_cn：引导阶段质量数据

- sets_up_cn：为新交换合同的必要性提供依据。

- evidence_pointer：Section 4.2

### 35. 4.2 S5–S7

- order：35

- section：Design and Evaluation

- locator：4.2 S5–S7

- move_code：DESIGN_FEATURE

- paraphrase_cn：决定性设计决策是放弃网关、停止隐藏错误，并在电子处方创建点引入验证规则，使模块和处方者遵守新交换合同。

- rhetorical_function_cn：概括核心设计转向。

- depends_on_cn：旧系统缺陷

- sets_up_cn：为后续规则设计提供总原则。

- evidence_pointer：Section 4.2

### 36. 4.3 S1–S2

- order：36

- section：Design and Evaluation

- locator：4.3 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：新交换合同决定淘汰EDIFACT，采用XML，因为XML支持简单自动验证；标准和法规需在瑞典实践中被解释和具体化。

- rhetorical_function_cn：解释技术标准选择。

- depends_on_cn：自动验证要求

- sets_up_cn：为规则表的详细设计做铺垫。

- evidence_pointer：Section 4.3

### 37. 4.3.1 S1–S3

- order：37

- section：Design and Evaluation

- locator：4.3.1 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：分类规则规定类名和标识符；电子处方是关系实体，创建新处方时必须引用已存在的制度实体。

- rhetorical_function_cn：定义交换合同的分类层。

- depends_on_cn：构成性规则理论

- sets_up_cn：为表1的类别和标识符提供内容。

- evidence_pointer：Section 4.3.1, Table 1

### 38. 4.3.2 S1–S2

- order：38

- section：Design and Evaluation

- locator：4.3.2 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：另一组构成性规则用于规定如何执行高质量沟通行为，包含结构、数据、动态一致性和标识规则，并基于分类规则和法律要求。

- rhetorical_function_cn：描述四类创建规则。

- depends_on_cn：分类规则和言语行为理论

- sets_up_cn：为表2和自动验证逻辑提供基础。

- evidence_pointer：Section 4.3.2, Table 2

### 39. 4.3.3 S1–S4

- order：39

- section：Design and Evaluation

- locator：4.3.3 S1–S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：旧系统没有通用验证；新系统必须在实践过程中尽早检查规则合规，并定义清楚可沟通的错误类型。

- rhetorical_function_cn：补充验证机制和错误类型设计。

- depends_on_cn：规则形式化

- sets_up_cn：为实施中的错误反馈机制做铺垫。

- evidence_pointer：Section 4.3.3

### 40. 4.3.3 S5–S6

- order：40

- section：Design and Evaluation

- locator：4.3.3 S5–S6

- move_code：PRACTICAL_STAKES

- paraphrase_cn：错误类型必须清晰以传达给维护团队和处方者，因为处方错误可能导致严重药物不良反应甚至住院。

- rhetorical_function_cn：强调错误管理对患者安全的现实重要性。

- depends_on_cn：错误类型定义

- sets_up_cn：为实施中的强制拒绝决策提供理由。

- evidence_pointer：Section 4.3.3

### 41. 4.4 S1–S2

- order：41

- section：Design and Evaluation

- locator：4.4 S1–S2

- move_code：MECHANISM

- paraphrase_cn：交换合同是改进质量的关键，它同时作为治理机制和数字基础设施与数字实践的质量规范。

- rhetorical_function_cn：概括交换合同的功能机制。

- depends_on_cn：前文规则设计

- sets_up_cn：为第4.4.1和4.4.2详述做总起。

- evidence_pointer：Section 4.4

### 42. 4.4.1 S1–S3

- order：42

- section：Design and Evaluation

- locator：4.4.1 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：交换合同被用为API契约来认证和实现标准化模块化系统间服务；结构/数据规则编码在XML schema中，动态一致性和标识规则需要在线访问注册库。

- rhetorical_function_cn：描述交换合同在技术实现中的形态。

- depends_on_cn：治理机制概念

- sets_up_cn：为4.4.2中的实践界面概念做技术铺垫。

- evidence_pointer：Section 4.4.1, Figure 5

### 43. 4.4.2 S1–S2

- order：43

- section：Design and Evaluation

- locator：4.4.2 S1–S2

- move_code：MECHANISM

- paraphrase_cn：互操作性应被重新理解为跨实践执行社会互动的能力，交换合同定义了数字实践接口并明确各方责任。

- rhetorical_function_cn：从实践视角定义互操作性和交换合同。

- depends_on_cn：技术治理机制

- sets_up_cn：为后面评估实践改变提供理论解释。

- evidence_pointer：Section 4.4.2, Figure 6

### 44. 4.4.2 S3–S5

- order：44

- section：Design and Evaluation

- locator：4.4.2 S3–S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：2006年三个药房的案例研究发现药剂师作为把关人发现并纠正电子处方错误；结论是把自动验证推到处方方会提高质量和患者安全。

- rhetorical_function_cn：引用前期研究为设计方向提供实证支持。

- depends_on_cn：数字实践界面概念

- sets_up_cn：为实施和评价奠定实践预期。

- evidence_pointer：Section 4.4.2, Åstrand et al. (2009)

### 45. 4.5 S1–S3

- order：45

- section：Design and Evaluation

- locator：4.5 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：错误状态被定义为警告(W)和拒绝(R)，县议会同意强制拒绝，这意味着R错误不能由药剂师处理。

- rhetorical_function_cn：说明关键实施决策。

- depends_on_cn：错误类型和自动验证

- sets_up_cn：为测量合规性和错误率变化提供操作定义。

- evidence_pointer：Section 4.5

### 46. 4.5 S4–S6

- order：46

- section：Design and Evaluation

- locator：4.5 S4–S6

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为评估干预效果，作者用连续抽样收集实施前后各一个月的全部XML电子处方，以测量合规性。

- rhetorical_function_cn：说明评价数据来源和方法。

- depends_on_cn：实施决策

- sets_up_cn：为表3的对照结果提供基础。

- evidence_pointer：Section 4.5

### 47. 4.5 S7–S9

- order：47

- section：Design and Evaluation

- locator：4.5 S7–S9

- move_code：RESULT

- paraphrase_cn：结果显示实施后错误大幅减少：有错误的处方集从98.6%降至0.9%，总错误数从5,970,737降至13,764；R错误不再到达药房，说明实践发生改变。

- rhetorical_function_cn：报告核心效果证据。

- depends_on_cn：前后对照数据

- sets_up_cn：为“社会互动被制度化”的论断提供数据支撑。

- evidence_pointer：Section 4.5, Table 3

### 48. 4.5 S10–S12

- order：48

- section：Design and Evaluation

- locator：4.5 S10–S12

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：大规模从宽松转为限制性互动并未导致混乱；药房调查显示大多数受访者认为电子处方安全、患者受益、成本有效并改善沟通，支持实用合法性。

- rhetorical_function_cn：补充实施安全性和合法性的证据。

- depends_on_cn：定量结果

- sets_up_cn：为制度合法性主张和后续法规讨论做铺垫。

- evidence_pointer：Section 4.5 末尾, Hammar et al. (2010)

### 49. 4.6 S1–S4

- order：49

- section：Design and Evaluation

- locator：4.6 S1–S4

- move_code：MECHANISM

- paraphrase_cn：NEF项目还推动修改注册法：2004年提议，2005年法律允许电子处方在整个生命周期中存储，第一次在制度层面承认电子处方作为潜在原件。

- rhetorical_function_cn：说明设计者主动改变制度环境。

- depends_on_cn：制度化过程

- sets_up_cn：为双向制度化模型提供宏观证据。

- evidence_pointer：Section 4.6

### 50. 4.6 S5–S8

- order：50

- section：Design and Evaluation

- locator：4.6 S5–S8

- move_code：RESULT

- paraphrase_cn：2009年电子处方达到80%成为惯例，法规正式授予其与纸质同等地位；2021/2022年法律强制全面电子处方，制度化过程完成。

- rhetorical_function_cn：报告制度层面最终结果。

- depends_on_cn：法规变化与扩散数据

- sets_up_cn：为数字制度化理论模型提供经验锚点。

- evidence_pointer：Section 4.6

### 51. 5 开头 S1–S2

- order：51

- section：Theory Building

- locator：5 开头 S1–S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：数字制度化是发展数字制度系统的过程，通过治理和改变数字基础设施及微观数字实践，使跨情境的合法社会互动成为可能；它是宏观交换合同和微观实践之间双向调整的过程。

- rhetorical_function_cn：提出文章的核心理论定义。

- depends_on_cn：前文的制度理论、设计原则和案例结果

- sets_up_cn：为模型（Figure 7）和设计原则提供理论框架。

- evidence_pointer：Section 5 开头

### 52. 5.1 S1–S3

- order：52

- section：Theory Building

- locator：5.1 S1–S3

- move_code：REQUIREMENT

- paraphrase_cn：宏观层面由制度逻辑构成；规则必须正式精确以编码进软件模块和注册库，交换合同作为脚本规定微观社会互动。

- rhetorical_function_cn：将制度逻辑和脚本概念转化为设计需求。

- depends_on_cn：制度理论脚本概念

- sets_up_cn：为DP2的具体要求提供理论解释。

- evidence_pointer：Section 5.1

### 53. 5.2 S1–S3

- order：53

- section：Theory Building

- locator：5.2 S1–S3

- move_code：MECHANISM

- paraphrase_cn：微观层面由数字实践构成；数字制度实体是制度系统扩散的生成机制，正式编码使其可复制、耐用、可交流。

- rhetorical_function_cn：解释制度实体如何驱动扩散。

- depends_on_cn：制度实体属性理论

- sets_up_cn：为DP3提供理论基础。

- evidence_pointer：Section 5.2

### 54. 5.3 S1–S4

- order：54

- section：Theory Building

- locator：5.3 S1–S4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：数字制度化是双向递归过程，宏观和微观彼此关联；基础设施不能仅自底向上涌现并合法化，需要反馈机制把错误和新交换需求送回制度设计。

- rhetorical_function_cn：解释双向过程模型的核心。

- depends_on_cn：宏观微观辩证关系

- sets_up_cn：为第6节设计原则中的反馈和持续改进提供依据。

- evidence_pointer：Section 5.3, Figure 7

### 55. 6 开头 S1–S2

- order：55

- section：Design Principles

- locator：6 开头 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：本节提出三条设计原则，捕获设计工作中获得的知识：分析制度环境、设计交换合同、确保数字制度实体质量与合法性。

- rhetorical_function_cn：正式声明设计知识贡献。

- depends_on_cn：数字制度化模型

- sets_up_cn：为结论部分的贡献定位做铺垫。

- evidence_pointer：Section 6 开头

### 56. 6.1 S1–S3

- order：56

- section：Design Principles

- locator：6.1 S1–S3

- move_code：REQUIREMENT

- paraphrase_cn：制度环境是制度设计的先决条件；标准通常复杂需选择适用子集，法规是强制的，设计者需解释法规并理解其理性，必要时主动改变制度环境。

- rhetorical_function_cn：展开第一条设计原则。

- depends_on_cn：合法性理论

- sets_up_cn：为后续稳定性和灵活性平衡做铺垫。

- evidence_pointer：Section 6.1

### 57. 6.2 S1–S3

- order：57

- section：Design Principles

- locator：6.2 S1–S3

- move_code：REQUIREMENT

- paraphrase_cn：交换合同应从技术和实践双重视角设计，定义技术格式、构成规则、规制规则和合法性验证控制。

- rhetorical_function_cn：展开第二条设计原则的具体内涵。

- depends_on_cn：交换合同设计经验

- sets_up_cn：为第4节设计细节提供原则级总结。

- evidence_pointer：Section 6.2

### 58. 6.2 S4–S6

- order：58

- section：Design Principles

- locator：6.2 S4–S6

- move_code：MECHANISM

- paraphrase_cn：实施交换合同需平衡稳定性与灵活性；网关使连接容易但增加复杂性，制度化总是伴随着标准化，从而增强可复制、耐用和可交流性。

- rhetorical_function_cn：解释设计原则背后的机制权衡。

- depends_on_cn：Hasselbladh & Kallinikos制度和标准化理论

- sets_up_cn：支持D1/D2的具体应用。

- evidence_pointer：Section 6.2

### 59. 6.3 S1–S4

- order：59

- section：Design Principles

- locator：6.3 S1–S4

- move_code：REQUIREMENT

- paraphrase_cn：数字制度化要求制度实体可复制、耐用、可交流；应通过自动有效性控制使发送方承担责任，并持续识别新交换需求、系统管理错误和反馈。

- rhetorical_function_cn：展开第三条设计原则。

- depends_on_cn：制度实体质量理论和错误管理文献

- sets_up_cn：为结论部分的贡献和限制做铺垫。

- evidence_pointer：Section 6.3

### 60. 7.1.1 S1–S2

- order：60

- section：Conclusion

- locator：7.1.1 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：该中程理论回应了将制度理论纳入IS研究并分析更大制度化过程的紧迫需求；数字制度实体及其生成力是数字制度化过程的核心。

- rhetorical_function_cn：重申理论贡献。

- depends_on_cn：数字制度化模型

- sets_up_cn：为边界声明和推广性论证提供基础。

- evidence_pointer：Section 7.1.1

### 61. 7.1.1 S3–S5

- order：61

- section：Conclusion

- locator：7.1.1 S3–S5

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：假设发现可转移到瑞典电子处方之外，尽管交换复杂性和合规、合法性、质量要求在不同情境会有差异。

- rhetorical_function_cn：界定推广范围，同时声明可迁移性。

- depends_on_cn：单案例基础

- sets_up_cn：为设计原则放回DSR知识框架做铺垫。

- evidence_pointer：Section 7.1.1

### 62. 7.1.1 S6–S7

- order：62

- section：Conclusion

- locator：7.1.1 S6–S7

- move_code：CONTRIBUTION

- paraphrase_cn：文章从设计者视角描述制度化，强调设计者（公共或私营网络中的权威）对系统合法性的责任；数字制度设计常处于灰色地带，需要法律论证和解释技能。

- rhetorical_function_cn：提升设计者责任议题，扩展制度设计的外延。

- depends_on_cn：设计师视角

- sets_up_cn：为未来研究和局限的讨论提供方向。

- evidence_pointer：Section 7.1.1

### 63. 7.1.2 S1–S3

- order：63

- section：Conclusion

- locator：7.1.2 S1–S3

- move_code：CONTRIBUTION

- paraphrase_cn：设计原则属于Gregor和Hevner知识贡献框架中“已知问题的新解决方案”，并通过与其它国家电子处方扩散率的国际比较来支持其成功。

- rhetorical_function_cn：把贡献定位到设计科学框架中。

- depends_on_cn：国际比较证据

- sets_up_cn：为设计原则有效性的条件声明做铺垫。

- evidence_pointer：Section 7.1.2

### 64. 7.1.2 S4–S6

- order：64

- section：Conclusion

- locator：7.1.2 S4–S6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者承认不能完全确定设计原则有效，因为存在情境偶然性；但相信若没有有意制度设计并遵循这些原则，数字制度化不会如此有效。

- rhetorical_function_cn：在过度自信和谨慎之间划定边界。

- depends_on_cn：案例成功与设计原则

- sets_up_cn：引出研究过程评价和未来研究。

- evidence_pointer：Section 7.1.2

### 65. 7.2 S1–S5

- order：65

- section：Conclusion

- locator：7.2 S1–S5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：ADR与纵向研究结合、作者2内部研究者的身份，使深入理解制度环境和制度实体质量的重要性成为可能；这些洞见难以通过其他方法获得。

- rhetorical_function_cn：辩护研究方法对知识贡献的必要性。

- depends_on_cn：研究过程经验

- sets_up_cn：为局限讨论做铺垫。

- evidence_pointer：Section 7.2

### 66. 7.3 S1–S4

- order：66

- section：Conclusion

- locator：7.3 S1–S4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：交换合同成功并非唯一因素，政治、财务和组织因素未展开；未来需研究网络内治理策略、设计者如何获取合法性、信任和财务支持。

- rhetorical_function_cn：识别未控制的成功因素并指出未来方向。

- depends_on_cn：案例成功

- sets_up_cn：为重新思考数字化时代制度化做总结。

- evidence_pointer：Section 7.3

### 67. 7.3 S5–S6

- order：67

- section：Conclusion

- locator：7.3 S5–S6

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：电子处方案例表明需要重新思考数字化时代的制度化；数字基础设施是制度转型的强大力量，数字制度化值得进一步实证和理论发展。

- rhetorical_function_cn：给出研究收尾和未来议程。

- depends_on_cn：全文贡献

- sets_up_cn：文章自然结束。

- evidence_pointer：Section 7.3

## 写作技术

- gap_construction_cn：先综述三类数字基础设施演化理论（ANT、复杂系统、批判实在论），指出它们都侧重自底向上涌现；再指出制度理论使用案例多描述失败或制度阻碍演化；最后指出缺乏规定性和设计师视角，形成缺口。

- signposting_cn：摘要后引言末尾说明文章按Gregor & Hevner设计科学模式组织；各节开头有‘In Section X, we ...’；第5节开头预告第6节设计原则。

- transition_logic_cn：第2节从文献综述到理论再到缺口；第3节从案例描述到ADR方法；第4节从设计挑战到决策到规则设计到治理功能到实施评价到制度环境；第5节从过程模型到设计原则。

- claim_evidence_rhythm_cn：用规则和错误类型表展示设计细节，用表3提供前后数据，用法规和调查故事补充合法性；证据密度从设计表到定量结果再到制度事件和国际比较逐步升级。

- benchmark_narrative_cn：先建立旧系统错误蔓延基线，然后对比新系统；通过国际扩散排名（世界前三）作为外部基准；引用Sahay等抽象指导与本文具体原则形成对照。

- theory_return_cn：第5节将NEF项目重新概念化为数字制度化双向过程，用Barley & Tolbert脚本、Hasselbladh & Kallinikos的可复制性/耐用性/可交流性等理论概念解释结果；第7节回到该理论并主张其可转移到其它制度实体。

- contribution_positioning_cn：在设计科学知识贡献框架中定位为‘已知问题的新解决方案’；强调middle-range prescriptive theory；同时突出设计者责任和制度设计这种新视角。

- novelty_protection_cn：通过在国际背景比较中把成功归因于设计原则；通过对比已有文献的抽象指导强调本文原则的具体性和可操作性；通过指出大多数基础设施演化理论只是涌现式、本文是前所未有的有意设计案例，防止其被视为一次性性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立宏观背景：数字化普遍性、基础设施需要设计且容易失败

- research_job_cn：找到可观察的制度实体交换场景和痛点

- required_evidence_cn：实践中的错误或低效证据，或成功的反常现象

- transition_to_next_cn：用现有理论解释为何会有这些现象，指出解释不足

#### 2. 2

- step：2

- writing_job_cn：综述现有基础设施演化理论，指出自底向上和涌现视角的局限

- research_job_cn：系统梳理文献，识别规定性理论缺口

- required_evidence_cn：多篇文献引用和对比，说明普遍忽视制度情境

- transition_to_next_cn：引入能弥补缺口的理论（制度理论、言语行为理论等）

#### 3. 3

- step：3

- writing_job_cn：用理论重构目标对象：从数据/软件重新定义为数字制度实体

- research_job_cn：将理论概念（制度实体、规则、合法性）映射到案例对象

- required_evidence_cn：案例对象的制度属性（规则、实体、规范）

- transition_to_next_cn：推导出设计要求：需要可验证的构成规则和治理机制

#### 4. 4

- step：4

- writing_job_cn：描述制品设计：交换合同的规则分类、技术选择、验证机制

- research_job_cn：把法规/标准转译为可编码规则，开发XML schema和自动验证

- required_evidence_cn：设计决策、规则表、技术标准说明

- transition_to_next_cn：说明如何实施和强制规则（错误状态、反馈）

#### 5. 5

- step：5

- writing_job_cn：用前后对照数据报告效果量化

- research_job_cn：收集干预前后同口径数据，用规则自动验证计算错误率

- required_evidence_cn：样本量、时间窗、错误率对比表

- transition_to_next_cn：从技术效果转向制度合法性证据

#### 6. 6

- step：6

- writing_job_cn：用理论语言重构经验：双向制度化模型和设计原则

- research_job_cn：反思设计与制度变迁的关联，提炼可复用原则

- required_evidence_cn：法规变化、实践扩散、国际比较等制度证据

- transition_to_next_cn：讨论贡献、边界和未来研究

### most_transferable_moves_cn

1. 用“制度实体”而非“数据文件”作为设计焦点

2. 把法规/标准转译成可自动验证的构成规则

3. 利用错误状态（警告/拒绝）推动实践改变

4. 用前后窗口同口径数据建立准实验证据

5. 从设计原则返回制度理论，贡献middle-range理论

### resource_intensive_or_nonstandard_parts_cn

1. 长期内嵌研究者身份（作者2在NPC工作）

2. 全国性数字基础设施和注册库数据访问

3. 与立法机构互动的制度设计能力

4. 可自动验证的规则基础和XML schema工程

5. 多年纵向文档档案和访谈重建

### what_not_to_copy_superficially_cn

1. 没有内嵌设计和长期数据，仅复述“制度设计”“合法性”词汇无法支撑贡献

2. 没有规则自动验证和前后数据，仅设计原则列表会缺少效果证据

3. 反事实断言“若无设计原则不会成功”若无对照证据会显得过度

4. 单一成功案例需谨慎，不能简单宣称普遍有效

- single_best_description_of_the_routine_cn：把制度实体而非软件作为设计中心，通过可自动验证的交换合同把规则推到起点，以前后数据证明错误下降，再用制度理论把它升华为双向数字制度化过程和设计原则。

## 分析边界

基于全文OCR文本，无精确页码；部分章节标题可能重复（4.4.1与4.4.2标题相同），但不影响论证判断；研究阶段划分基于内容重构；定量评价为前后对比而非随机对照。
