# Containing COVID-19 through physical distancing: the impact of real-time crowding information

- 作者：Martin Adam; Dominick Werner; Charlotte Wendt; Alexander Benlian
- 年份 / 期刊：2020 / European Journal of Information Systems
- DOI：10.1080/0960085x.2020.1814681
- 源文件：10546_2020_containing-covid-19-through-physical-distancing-the-impact-of-real-time-crowding-information.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.86

## 文章级论证概况

- 核心问题：在COVID-19背景下，决策支持系统中显示拥挤信息（CI）是否会以及如何影响用户对不同拥挤程度地点的选择；信息即时性和用户健康焦虑如何改变这一效应。

- 制品与设计：一个虚构的医疗诊所查找网站“find-your-doctor.org”，用三个实验条件操纵CI：无CI、历史平均CI、实时CI；CI用1至4个人形图标表示候诊人数，即时性分别用“usual amount of patients (past 2 months)”和“live amount of patients (updated just now)”表示。

- 客观结果：与无CI相比，显示CI使选择拥挤程度较低诊所的几率提高4.6倍；实时CI比历史平均CI更强地促进选择低拥挤诊所；健康焦虑的调节方向与原假设相反：低健康焦虑用户在实时CI下选择低拥挤诊所的几率是6.4倍，而高健康焦虑用户只有2.5倍。

- 核心贡献：作者声称首次提供CI对选择行为的因果证据，将CI引入数字选择环境文献，扩展建构水平理论中即时性作为时间距离新面向，并联合考察时间距离与假设距离；同时为DSS提供商和政策制定者提供通过信息赋予而非家长式强制来促进身体距离的可行方案。

- 整篇论证链：论文从COVID-19中身体距离的重要性和强制隔离对自由的侵害切入，指出现实中的DSS已越来越多地显示拥挤信息，但缺乏因果证据。作者将CI置于数字选择环境中的需求信息文献中，说明高需求可能被当作高质量信号，进而可能导致用户反而选择拥挤地点；同时引入建构水平理论，认为信息即时性会改变时间距离，健康焦虑会改变假设距离。据此提出三个假设，并用德国和意大利343名参与者的三条件在线实验检验。结果显示CI能显著促进选择低拥挤地点，实时信息更强；但健康焦虑的调节方向与假设相反。讨论部分将结果回接到政策含义和理论贡献，指出CI可作为非强制性的自我调节机制，并扩展了对多心理距离联合作用的理解。

## 类型与写作弧线判定

- 论文主类型判定：文章的主要逻辑是从数字选择环境和建构水平理论推导出关于CI、即时性和健康焦虑的假设，然后构造最小化但可操纵的实验性DSS（网页）进行受控在线实验，因此属于理论导出制品并通过实验检验。

- 主导写作弧线判定：文章遵循“问题—理论—设计—实验检验—回到理论与政策”的主线：先建立疫情和身体距离问题，引入CI和建构水平理论，形成假设和实验操纵，报告有序logistic回归结果，最后讨论实践与理论贡献并回到最初缺口。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：六个阶段依次推进：理论建构与假设推导→实验制品与操纵设计→在线数据采集→测量与内部有效性验证→假设检验（三个嵌套模型）→理论返回与实践意义建构。前一个阶段的不确定性由后一个阶段处理，最终汇成因果主张和贡献声明。

### studies_or_phases

#### 1. 理论建构与假设推导

- order：1

- name_cn：理论建构与假设推导

- question_cn：CI的存在、即时性和用户健康焦虑如何影响用户对拥挤程度不同地点的选择？

- inputs_and_setting_cn：数字选择环境中的需求信息文献、COVID-19相关健康行为研究、建构水平理论文献。

- designed_or_compared_object_cn：概念上比较CI存在/不存在、高/低即时性、高/低健康焦虑。

- baseline_control_or_counterfactual_cn：无CI情境作为理论基线；已有需求信息文献中的高需求吸引效应作为对照。

##### objective_metrics

1. 假设的可检验性

2. 与文献的连贯性

- analysis_method_cn：理论整合与演绎推理，提出H1-H3。

- main_result_cn：提出三个假设：CI存在增加选择低拥挤地点；高即时性加强该效应；健康焦虑越高，高即时性下越倾向选择低拥挤地点。

- argumentative_role_cn：定义核心自变量、因变量和调节变量，为实验设计提供理论方向。

- remaining_uncertainty_cn：假设尚未经过经验检验，需要可控实验提供因果证据。

- link_to_next_phase_cn：理论命题要求可操作化：把CI、即时性、健康焦虑转成实验刺激和测量工具。

##### evidence_pointers

1. Section 2.1-2.2

2. Section 3.1-3.3

#### 2. 实验制品与操纵设计

- order：2

- name_cn：实验制品与操纵设计

- question_cn：如何用简单的DSS界面操纵CI和即时性，并使三种条件可比较？

- inputs_and_setting_cn：虚构网站find-your-doctor.org；医疗诊所作为地点情境；三种条件（无CI、历史平均CI、实时CI）。

- designed_or_compared_object_cn：实验网站中地图上的诊所列表和CI图标，以及即时性文字提示。

- baseline_control_or_counterfactual_cn：无CI条件为基线；历史平均CI作为实时CI的较低即时性对照。

##### objective_metrics

1. 操纵是否被参与者正确感知

2. 情境真实感评分

- analysis_method_cn：实验材料设计；后续操控检验验证设计有效性。

- main_result_cn：设计了三种条件，四个诊所对应0%、33%、67%、100%拥挤水平，用1-4个人形图标表示拥挤程度。

- argumentative_role_cn：把理论概念转化为可观察的刺激差异，为因果推断提供基础。

- remaining_uncertainty_cn：需要实际参与者和数据确认操控有效且情境逼真。

- link_to_next_phase_cn：材料准备好后进入实际数据采集。

##### evidence_pointers

1. Section 4.1, Figure 2

2. Section 4.2, Figure 3

#### 3. 在线实验数据采集

- order：3

- name_cn：在线实验数据采集

- question_cn：在受控环境中，CI和即时性是否因果性影响用户的诊所选择？

- inputs_and_setting_cn：360名来自Prolific.co的德国和意大利参与者；2020年6月第一周，身体距离政策施行期间；情境为因背痛需要找替代诊所。

- designed_or_compared_object_cn：参与者被随机分配到三个实验条件之一，并选择四个诊所之一。

- baseline_control_or_counterfactual_cn：随机分配形成条件间可比性；无CI条件作为CI存在条件的反事实参照。

##### objective_metrics

1. 选择诊所的拥挤水平（0%, 33%, 67%, 100%）

2. 四个注意力检查通过数

- analysis_method_cn：在线问卷收集；随机分配；记录选择行为和感知测量。

- main_result_cn：343名参与者通过全部注意力检查，形成有效样本；数据采集成功。

- argumentative_role_cn：提供检验假设的核心结果数据。

- remaining_uncertainty_cn：需要检验随机化是否成功、操纵是否被感知，以及测量是否可靠有效。

- link_to_next_phase_cn：数据质量验证后才能进行正式假设检验。

##### evidence_pointers

1. Section 4.2

2. Section 5.1, Table A2

#### 4. 测量验证、随机化与操控检查

- order：4

- name_cn：测量验证、随机化与操控检查

- question_cn：实验操纵是否有效，测量模型是否可靠，样本是否平衡？

- inputs_and_setting_cn：参与者的问卷回答、操控检查题项、健康焦虑、产品卷入、感知拥挤、感知即时性、加工流畅性；德国和意大利两个国家子样本。

- designed_or_compared_object_cn：三个条件之间的控制变量平衡；感知拥挤、感知即时性在不同条件间的差异。

- baseline_control_or_counterfactual_cn：无CI条件与CI存在条件比较；历史平均CI与实时CI条件比较。

##### objective_metrics

1. 方差分析p值

2. AVE

3. 复合信度

4. Cronbach's α

5. HTMT值

- analysis_method_cn：单因素ANOVA检查随机化与操控；CFA检查收敛和区分效度；HTMT检验区分效度。

- main_result_cn：操控有效：感知拥挤显著更高，感知即时性在实时条件显著更高；随机化在各条件间成功；测量模型信效度达标；德意两国除健康焦虑和产品卷入外无显著差异。

- argumentative_role_cn：建立内部有效性，证明随后回归结果来自操纵而非测量或抽样偏差。

- remaining_uncertainty_cn：尚未检验假设，也尚未评估作用的大小和方向。

- link_to_next_phase_cn：确认测量质量后，利用有序logistic回归进行假设检验。

##### evidence_pointers

1. Section 5.1

2. Section 5.2

3. Table A1

#### 5. 假设检验：有序logistic回归三个模型

- order：5

- name_cn：假设检验：有序logistic回归三个模型

- question_cn：CI、即时性和健康焦虑是否以假设方向影响选择拥挤程度？

- inputs_and_setting_cn：343名参与者的选择结果、条件编码、健康焦虑、年龄、国家、产品卷入、阅读时间、选择时间。

- designed_or_compared_object_cn：Model 1比较CI存在与缺失；Model 2在CI存在条件下比较实时与历史平均；Model 3加入健康焦虑交互。

- baseline_control_or_counterfactual_cn：Model 1中CI缺失为基线；Model 2和3中历史平均CI为实时CI的对照。

##### objective_metrics

1. 有序logistic回归系数

2. odds ratios（指数化系数）

3. Pseudo R²

4. 模型拟合检验

- analysis_method_cn：有序logistic回归；检验比例优势假设；嵌套模型比较。

- main_result_cn：H1支持：CI存在使选择低拥挤诊所的几率提高4.6倍；H2支持：实时CI比历史平均CI更能促进低拥挤选择；H3被拒绝：健康焦虑未放大高即时性效应，反而产生相反方向，低健康焦虑用户在实时CI下作用更强。

- argumentative_role_cn：为整个研究提供核心因果证据，并揭示反直觉调节效应。

- remaining_uncertainty_cn：机制（加工流畅性中介、健康焦虑的替代解释）未正式检验，外部效度需更多情境。

- link_to_next_phase_cn：结果需要在讨论中解释，并与理论预期和实际政策含义连接。

##### evidence_pointers

1. Section 5.3, Table 1

2. Figure 4

3. Note 4

#### 6. 讨论：实践与理论贡献建构

- order：6

- name_cn：讨论：实践与理论贡献建构

- question_cn：结果对COVID-19管理和IS理论意味着什么？

- inputs_and_setting_cn：前述实证结果、相关文献（如Laato et al., 2020; Trang et al., 2020）、政策背景。

- designed_or_compared_object_cn：CI显示与传统家长式封锁措施比较；论文贡献与既有理论/实践思维比较。

- baseline_control_or_counterfactual_cn：无CI或历史平均CI的信息设计作为对照；理论贡献以既有研究为基线。

##### objective_metrics

1. 实践建议的针对性

2. 理论贡献的清晰度

3. 边界条件的明确度

- analysis_method_cn：解释性论证；反直觉发现的推测；将结果定位为可复用设计知识和理论扩展。

- main_result_cn：提出CI作为自我调节、非家长式的疫情缓解机制；实时CI在低健康焦虑时最有效；理论贡献包括CI作为需求信息的新形式、即时性作为时间距离新面向、联合考察时间与假设距离。

- argumentative_role_cn：将局部实验证据提升为一般性设计知识和理论贡献，并回应引言中的缺口。

- remaining_uncertainty_cn：现场有效性、中介机制、基础设施和跨文化边界仍需未来研究。

- link_to_next_phase_cn：通过限制条件直接导向未来研究。

##### evidence_pointers

1. Section 6.1, Table 2

2. Section 6.2

3. Section 6.3

## 各部分修辞架构

### abstract_moves

1. CONTEXT: COVID-19背景下DSS越来越常见地显示CI。

2. PHENOMENON: DSS通过CI鼓励用户保持身体距离。

3. GAP: 关于CI对选择行为因果效应及即时性与健康焦虑的调节作用知之甚少。

4. THEORY_INTRO: 基于数字选择环境和建构水平理论。

5. STUDY_OVERVIEW: 进行多国在线实验。

6. RESULT: CI增加选择低拥挤地点，实时最强，低健康焦虑时更强。

7. CONTRIBUTION: 为疫情时代的IS研究增加证据，并提供可操作建议。

### introduction_moves

1. CONTEXT: 身体距离是尚无可治愈方法和疫苗时最有效的措施。

2. PRACTICAL_STAKES: 强制封锁侵害自由选择。

3. PHENOMENON: DSS显示CI的例子（DocClocker, Crowdless, Google Maps）。

4. MECHANISM: CI可均衡分布拥挤、减少接触，从而抑制疫情。

5. GAP: 不知道CI是否确实影响选择行为。

6. PRIOR_KNOWLEDGE: 需求信息文献通常显示高需求吸引用户。

7. WHY_GAP_MATTERS: 如果CI吸引用户到拥挤地，可能加剧疫情。

8. LIMITATION: 时间线索研究未考虑动态变化信息的即时性。

9. LIMITATION: 健康焦虑与即时性如何交互仍未知。

10. RQ_OR_OBJECTIVE: 提出RQ1和RQ2。

11. STUDY_OVERVIEW: 预告实验设计与主要结果。

12. CONTRIBUTION: 贡献于IS与疫情研究和建构水平理论拓展。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: CI由需求信息可视化发展而来。

2. MECHANISM: 高需求可能被视为高质量信号，导致羊群行为。

3. MECHANISM: CI反映地点容量和拥挤成本，尤其在疫情中暴露风险上升。

4. THEORY_INTRO: 介绍建构水平理论。

5. THEORY_PROPOSITION: 即时性改变时间距离，健康焦虑改变假设距离。

6. LIMITATION: 既有研究多分析静态信息，且心理距离常被孤立研究。

### artifact_design_moves

1. DESIGN_FEATURE: 虚构网站和三种条件。

2. DESIGN_FEATURE: 用1-4个小人图标表示拥挤水平。

3. DESIGN_FEATURE: 立即性提示分别为“usual amount of patients (past 2 months)”和“live amount of patients (updated just now)”。

4. METHOD_JUSTIFICATION: 选择医疗诊所的理由：感染风险、紧迫需求、依赖他人行为信息。

5. BENCHMARK_OR_CONTRAST: 将无CI作为控制条件，历史平均CI作为实时CI的较低即时性对照。

### evaluation_moves

1. STUDY_OVERVIEW: 在线实验三条件。

2. METHOD_JUSTIFICATION: Prolific样本和高通过率保证质量；德国和意大利用于稳健性。

3. DESIGN_FEATURE: 记录选择结果和多个控制变量。

4. ROBUSTNESS_OR_BOUNDARY_TEST: 随机化平衡和操控检查。

5. ROBUSTNESS_OR_BOUNDARY_TEST: CFA信效度。

6. RESULT: Model 1-3的回归结果。

7. RESULT: 反直觉的交互效应。

### discussion_and_contribution_moves

1. RESULT: 复述三个发现。

2. MECHANISM: 对健康焦虑反直觉效应的推测性解释。

3. CONTRIBUTION: 实践意义：CI是实现身体距离的非家长式工具。

4. CONTRIBUTION: 理论贡献：CI作为需求信息的新形式、即时性作为新时间面向、多心理距离联合。

5. BOUNDARY_CONDITION: 实时CI在低健康焦虑时最有效，但整体仍有正效应。

6. LIMITATION_AND_FUTURE: 需要现场数据、中介机制、基础设施研究。

7. CONTRIBUTION: 结论重申即刻行动价值。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 数字选择环境中的需求信息与羊群行为文献

2. 信息可视化与时间线索文献（时间戳、倒计时）

3. 建构水平理论（时间距离与假设距离）

4. 健康焦虑与疫情下回避行为研究

- 理论—设计耦合：direct

- 耦合判定理由：理论并非事后解释，而是在实验设计前决定了关键操纵。H1由需求信息质量信号与拥挤成本在疫情中的权衡推出；H2由建构水平理论推出即时性会通过建构匹配影响选择；H3由健康焦虑作为假设距离推出。实验中的三条件、即时性提示和健康焦虑测量都是这些理论命题的直接操作化。

- 理论到设计翻译链：需求信息文献认为高需求意味着高质量，但CI同时反映拥挤成本；COVID-19使感染成本突出，因此CI存在应促使选择低拥挤地。建构水平理论认为高即时性缩短时间距离，产生低水平建构，与紧急选择目标的建构匹配，从而提高加工流畅性，使拥挤成本更可信和可理解；因此高即时性应强化选择低拥挤地。健康焦虑被认为缩短假设距离，应当进一步放大风险感知；实验将这一理论预期转化为测量变量，并在有序logistic回归中加入交互项。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：需求信息在不确定环境中常被视为质量信号，使人们倾向于高需求、拥挤的地点；但在疫情中拥挤同时意味着感染风险。

- mechanism_cn：质量信号与拥挤成本的权衡；疫情使感染风险成为主导成本。

- design_requirement_cn：让用户能看到不同地点的拥挤程度，以权衡质量信号与拥挤成本。

- artifact_choice_cn：在实验网站地图上显示每个诊所的CI（1-4个人形图标），而控制条件不显示。

- evaluated_contrast_cn：CI存在 vs. CI缺失。

- objective_result_cn：CI存在使选择低拥挤诊所的几率是缺失时的4.6倍。

##### evidence_pointers

1. Section 3.1

2. Section 5.3 Model 1, Table 1

#### 2. 2

- theory_or_knowledge_claim_cn：建构水平理论：更近的时间距离导致更具体的心理表征；目标与信息建构匹配产生加工流畅性。

- mechanism_cn：高即时性缩短时间距离，提高建构匹配和加工流畅性；流畅性增强信息可信度和对拥挤成本的理解。

- design_requirement_cn：CI需要附带即时性线索，且能区分实时与历史平均值。

- artifact_choice_cn：即时性提示分别为“live amount of patients (updated just now)”和“usual amount of patients (past 2 months)”。

- evaluated_contrast_cn：实时CI vs. 历史平均CI。

- objective_result_cn：实时CI比历史平均CI更显著促进选择低拥挤诊所；且实时CI条件下加工流畅性显著更高。

##### evidence_pointers

1. Section 3.2

2. Section 5.3 Model 2, Table 1

3. Note 4

#### 3. 3

- theory_or_knowledge_claim_cn：健康焦虑反映对疾病可能性与严重性的夸大估计，等同于更近的假设距离。

- mechanism_cn：更近的假设距离使风险更具体，原假设认为会放大高即时性CI的威慑效果。

- design_requirement_cn：测量被试的健康焦虑，并在分析中检验其与即时性的交互。

- artifact_choice_cn：使用7点量表的健康焦虑测量（Abramowitz et al., 2007）；在Model 3加入immediacy × health anxiety交互。

- evaluated_contrast_cn：高健康焦虑 vs. 低健康焦虑，在实时与历史平均CI条件下的比较。

- objective_result_cn：原假设被拒绝；低健康焦虑者在实时CI下选择低拥挤地的几率（6.4倍）远高于高健康焦虑者（2.5倍）。

##### evidence_pointers

1. Section 3.3

2. Section 5.3 Model 3, Table 1

3. Figure 4

## 评价逻辑

### evaluation_modes

1. 受控在线实验（三条件组间设计）

2. 随机分配与条件间平衡检验

3. 操纵检验（感知拥挤、感知即时性）

4. 测量模型验证（CFA、AVE、CR、α、HTMT）

5. 有序logistic回归与嵌套模型比较

6. 加工流畅性的补充分析

7. 跨国家稳健性比较（德国 vs. 意大利）

- why_these_evaluations_cn：由于研究目标是因果效应和理论调节，作者选择在线实验以获得内部效度；操纵检验确保概念被正确激活；CFA和信效度检验保证潜变量测量可信；跨国家比较提供外部效度的初步证据；三个嵌套模型分别对应H1、H2、H3；补充加工流畅性分析为新提出的建构匹配机制提供过程证据。

- benchmark_and_contrast_chain_cn：从无CI条件作为最底层基线开始，证明CI本身有效；然后在CI存在条件下，以历史平均CI作为实时CI的对照，证明即时性增加效果；最后在健康焦虑的不同水平上重复估计实时CI相对历史平均CI的效应，显示调节方向。三个对比逐层递进，形成从存在到即时性再到个体差异的证据链。

### claim_evidence_ledger

#### 1. 显示CI能因果性地提高选择低拥挤地点的可能性。

- claim_cn：显示CI能因果性地提高选择低拥挤地点的可能性。

- evidence_cn：Model 1中CI系数-1.52显著，odds ratio=4.6。

- supported：是

#### 2. 更高即时性进一步强化CI的效果。

- claim_cn：更高即时性进一步强化CI的效果。

- evidence_cn：Model 2中Immediacy系数-1.35显著；实时CI条件加工流畅性显著更高。

- supported：是

#### 3. 健康焦虑越高，高即时性下越倾向选择低拥挤地点。

- claim_cn：健康焦虑越高，高即时性下越倾向选择低拥挤地点。

- evidence_cn：Model 3中交互项为正（0.40），方向相反，原假设被拒绝。

- supported：否

#### 4. 结果在德国和意大利两个疫情严重程度不同的国家间一致。

- claim_cn：结果在德国和意大利两个疫情严重程度不同的国家间一致。

- evidence_cn：除健康焦虑和产品卷入外，两国选择行为无显著差异。

- supported：是

#### 5. 高健康焦虑用户在实时CI下可能更关注质量信号而非风险。

- claim_cn：高健康焦虑用户在实时CI下可能更关注质量信号而非风险。

- evidence_cn：这是讨论中的推测，未直接测量质量关注或中介分析。

- supported：否

- internal_validity_strategy_cn：通过随机分配保证条件间可比性；用注意力检查剔除不专注被试；用操纵检查验证刺激有效性；控制年龄、国家、产品卷入、阅读和选择时间；测量模型信效度达到阈值；有序logistic回归满足比例优势假设。

- external_validity_strategy_cn：选择疫情严重程度不同的两个欧洲国家（德国和意大利）以显示跨情境稳健性；情境使用现实且受疫情影响严重的医疗诊所选址；实验程序在真实身体距离政策执行期内进行；还通过真实性评分确认情境逼真。

- what_is_not_actually_tested_cn：讨论中关于健康焦虑反直觉效应的机制（用户更关注质量而非风险）没有直接测量；加工流畅性虽然被测量，但未做正式中介分析；没有现场或观测数据证明CI能实际减少感染或替代封锁；长期健康焦虑变化和不同疫情阶段的影响未检验。

## 贡献闭环

- technical_claim_cn：在一个三条件在线实验中，CI显示显著提高用户选择较不拥挤地点的可能性，并且实时CI比历史平均CI更有效。

- artifact_claim_cn：实验网站中的CI（人形图标）和即时性提示（实时 vs. 历史平均）是该效应的可识别设计元素，因为操控检查确认了感知差异。

- mechanism_claim_cn：高即时性通过建构匹配和加工流畅性增加CI的可信度和拥挤成本的可理解性，从而强化低拥挤选择；该机制在Note 4中通过流畅性差异得到部分支持。

- boundary_claim_cn：效应在德国和意大利样本中稳健；健康焦虑调节方向与假设相反，实时CI对低健康焦虑用户效果更强；但随着高健康焦虑用户仍有正效应。

- reusable_design_knowledge_cn：DSS提供方和政策制定者可以通过显示CI，特别是实时CI，来温和地引导用户避开拥挤地点；信息呈现时应考虑用户健康焦虑水平，但不能因焦虑而放弃显示CI。

- theoretical_contribution_cn：将CI定位为数字选择环境中需求信息的一种新形式，反映拥挤成本而非仅质量信号；扩展建构水平理论，将动态变化信息的即时性视为时间距离的新面向，并首次联合考察时间距离与假设距离对信息处理和选择的影响。

- how_discussion_closes_intro_gap_cn：引言提出“CI是否会让用户反而选择更拥挤地点”的担忧，讨论用因果实验结果回答：CI实际上增加低拥挤选择；同时回答两个RQ，并说明即时性和健康焦虑的调节作用，从而把缺口闭合为实证结论和可操作建议。

- overclaim_or_unsupported_leaps_cn：作者将反直觉健康焦虑效应归因于“高焦虑用户更重视质量信号”，但没有测量质量关注或直接检验这一心理过程；同时从单一在线实验跳跃到“避免封锁”和“减少感染”仍需现场证据；将流畅性差异视为机制支持也属于间接推断。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：随着COVID-19出现，DSS越来越多地显示拥挤信息，以鼓励用户选择地点时保持身体距离。

- rhetorical_function_cn：在摘要开头建立现实背景，将技术现象与重大公共健康问题绑定。

- depends_on_cn：无前置依赖。

- sets_up_cn：为后续指出知识缺口和本研究意义提供背景。

- evidence_pointer：Abstract P1 S1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：GAP

- paraphrase_cn：尽管影响重大，但对CI在选择行为上的因果效应以及即时性和健康焦虑如何调节它知之甚少。

- rhetorical_function_cn：在摘要中快速制造知识缺口。

- depends_on_cn：依赖前一句的DSS背景。

- sets_up_cn：引出本研究的目的和方法。

- evidence_pointer：Abstract P1 S2

### 3. P1 S1

- order：3

- section：Introduction

- locator：P1 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在没有有效药物和疫苗时，身体距离是抑制COVID-19传播的最有力手段之一。

- rhetorical_function_cn：立即确立问题的现实紧迫性。

- depends_on_cn：无。

- sets_up_cn：为后续讨论强制与自由选择之间的张力提供基础。

- evidence_pointer：Introduction P1 S1

### 4. P1 S3

- order：4

- section：Introduction

- locator：P1 S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：全球近五分之一人口在2020年3月被封锁，强制身体距离构成对公民自由选择的家长式侵犯。

- rhetorical_function_cn：强调限制自由的代价，制造需要替代方案的压力。

- depends_on_cn：P1 S1的身体距离重要性。

- sets_up_cn：引出DSS显示CI作为非强制替代方案。

- evidence_pointer：Introduction P1 S3

### 5. P2 S1

- order：5

- section：Introduction

- locator：P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：为在不限制自由的情况下促进身体距离，DSS越来越多地显示拥挤信息，定义为显示地点可用容量被占用程度的信息。

- rhetorical_function_cn：定义核心概念并引入现象。

- depends_on_cn：前面建立的自由选择问题。

- sets_up_cn：为后续的CI例子和机制分析立下概念基础。

- evidence_pointer：Introduction P2 S1

### 6. P2 S2

- order：6

- section：Introduction

- locator：P2 S2

- move_code：PHENOMENON

- paraphrase_cn：给出DocClocker、Crowdless和Google Maps等实际应用作为CI的例子。

- rhetorical_function_cn：用真实系统说明CI已成为现实现象。

- depends_on_cn：CI定义。

- sets_up_cn：说明该问题的相关性和可研究性。

- evidence_pointer：Introduction P2 S2, Figure 1

### 7. P2 S3

- order：7

- section：Introduction

- locator：P2 S3

- move_code：MECHANISM

- paraphrase_cn：CI使不同地点的拥挤水平数字化可见，若用户选择较不拥挤地点，可减少过度拥挤、分布更均匀、降低接触和感染风险。

- rhetorical_function_cn：说明CI为什么具有公共卫生价值。

- depends_on_cn：CI的现实例子。

- sets_up_cn：为讨论“如果效果相反会怎样”制造张力。

- evidence_pointer：Introduction P2 S3

### 8. P3 S1

- order：8

- section：Introduction

- locator：P3 S1

- move_code：GAP

- paraphrase_cn：虽然DSS日益显示CI，但缺乏关于CI是否以及如何影响用户选择行为的知识。

- rhetorical_function_cn：明确指出文献空缺。

- depends_on_cn：前两段的现象与价值。

- sets_up_cn：引入选择困境和后续研究问题。

- evidence_pointer：Introduction P3 S1

### 9. P3 S2

- order：9

- section：Introduction

- locator：P3 S2

- move_code：PHENOMENON

- paraphrase_cn：用户面对两难：拥挤地点增加感染风险，但较不拥挤地点可能被视为质量较差，因为没有需求。

- rhetorical_function_cn：刻画CI解释中的核心张力，为假设提供动机。

- depends_on_cn：CI定义和需求信号文献。

- sets_up_cn：引出“CI可能适得其反”的担忧。

- evidence_pointer：Introduction P3 S2

### 10. P3 S3

- order：10

- section：Introduction

- locator：P3 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：既有IS研究主要考察需求信息如医生推荐数，显示用户通常被高需求、因此常常拥挤的地点吸引，因为高需求被解释为高质量信号。

- rhetorical_function_cn：总结既有知识的预测方向，制造与COVID-19需求之间的冲突。

- depends_on_cn：选择困境框架。

- sets_up_cn：为H1的“疫情下成本可能压倒质量信号”提供对比。

- evidence_pointer：Introduction P3 S3

### 11. P3 S4

- order：11

- section：Introduction

- locator：P3 S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：如果用户被吸引到拥挤地点，那么善意显示CI的DSS可能无意中加剧疫情传播。

- rhetorical_function_cn：提升缺口的现实严重性，使研究正当性更强。

- depends_on_cn：既有需求信息文献的预测。

- sets_up_cn：直接引出对因果效应研究的需求。

- evidence_pointer：Introduction P3 S4

### 12. P4 S1

- order：12

- section：Introduction

- locator：P4 S1

- move_code：GAP

- paraphrase_cn：除主效应外，还需要研究CI通常伴随的即时性线索。

- rhetorical_function_cn：引入第一个调节因素。

- depends_on_cn：CI主效应缺口的提出。

- sets_up_cn：为RQ2铺设第一块。

- evidence_pointer：Introduction P4 S1

### 13. P4 S4

- order：13

- section：Introduction

- locator：P4 S4

- move_code：LIMITATION

- paraphrase_cn：先前时间线索研究只处理静态信息或高度可预测事件，没有考虑动态变化信息（如CI）的即时性。

- rhetorical_function_cn：定位既有文献在即时性上的空白。

- depends_on_cn：对即时性的介绍。

- sets_up_cn：为建构水平理论对即时性的解释提供动机。

- evidence_pointer：Introduction P4 S4

### 14. P5 S1

- order：14

- section：Introduction

- locator：P5 S1

- move_code：GAP

- paraphrase_cn：即时性的处理并非在真空中进行，而是受用户健康焦虑影响。

- rhetorical_function_cn：引入第二个调节因素。

- depends_on_cn：即时性缺口。

- sets_up_cn：为H3做铺垫。

- evidence_pointer：Introduction P5 S1

### 15. P5 S2

- order：15

- section：Introduction

- locator：P5 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：健康焦虑在疫情中会导致不寻常行为，例如避免拥挤地点、不必要地避免就医甚至危险自我治疗。

- rhetorical_function_cn：说明健康焦虑在疫情中的重要性。

- depends_on_cn：健康焦虑定义。

- sets_up_cn：为研究健康焦虑与即时性的交互提供现实理由。

- evidence_pointer：Introduction P5 S2

### 16. P6 S1-S2

- order：16

- section：Introduction

- locator：P6 S1-S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究先问CI存在与否是否及如何影响不同拥挤地点的选择，再问CI存在时不同即时性水平如何在不同健康焦虑水平下影响选择。

- rhetorical_function_cn：在完整背景后明确提出研究问题。

- depends_on_cn：前两段识别的两个缺口。

- sets_up_cn：为研究设计、假设和结果报告提供组织框架。

- evidence_pointer：Introduction P6

### 17. P7 S1

- order：17

- section：Introduction

- locator：P7 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为回答问题，作者整合数字选择环境影响与建构水平理论，并在德国和意大利343名参与者中进行在线实验，选择不同拥挤程度的医疗诊所。

- rhetorical_function_cn：预告研究方法和样本。

- depends_on_cn：RQ1和RQ2。

- sets_up_cn：让读者准备接收主要结果。

- evidence_pointer：Introduction P7 S1

### 18. P7 S2

- order：18

- section：Introduction

- locator：P7 S2

- move_code：RESULT

- paraphrase_cn：显示CI使选择低拥挤诊所的可能性提高4.6倍；效果在实时CI和低健康焦虑时最强。

- rhetorical_function_cn：在引言中提前给出核心结果摘要。

- depends_on_cn：研究方法预告。

- sets_up_cn：为贡献声明提供实证基础。

- evidence_pointer：Introduction P7 S2

### 19. P8 S1

- order：19

- section：Introduction

- locator：P8 S1

- move_code：CONTRIBUTION

- paraphrase_cn：本研究回应疫情时代IS研究呼吁，帮助DSS提供者和政策制定者通过CI让用户自愿选择低拥挤地点，从而在不侵犯自由的前提下降低感染风险。

- rhetorical_function_cn：把结果连接到紧迫的实践需要。

- depends_on_cn：核心结果。

- sets_up_cn：为后文实践贡献部分铺路。

- evidence_pointer：Introduction P8 S1

### 20. P8 S2

- order：20

- section：Introduction

- locator：P8 S2

- move_code：CONTRIBUTION

- paraphrase_cn：理论上，研究引入CI作为数字选择环境中的新DSS特征，并扩展建构水平理论，将即时性视为时间距离新面向，并与健康焦虑代表的假设距离共同考察。

- rhetorical_function_cn：提前声明理论贡献。

- depends_on_cn：前述理论缺口。

- sets_up_cn：为理论背景和讨论部分提供方向。

- evidence_pointer：Introduction P8 S2

### 21. Section 2 intro S1

- order：21

- section：2. Theoretical background

- locator：Section 2 intro S1

- move_code：TRANSITION

- paraphrase_cn：先介绍CI作为DSS特征并定位在需求信息文献中，再引入建构水平理论来理解即时性和健康焦虑。

- rhetorical_function_cn：路标式过渡，告诉读者理论部分的组织。

- depends_on_cn：引言中的RQ。

- sets_up_cn：安排理论部分的内容顺序。

- evidence_pointer：Section 2 intro

### 22. P1 S1

- order：22

- section：2.1 Crowding information as a DSS feature

- locator：P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：CI源于数字选择环境中广泛使用的需求信息可视化，如餐厅签到数和产品购买统计。

- rhetorical_function_cn：把CI嵌入既有DSS研究谱系。

- depends_on_cn：引言对CI的定义。

- sets_up_cn：随后讨论高需求作为质量信号。

- evidence_pointer：Section 2.1 P1 S1

### 23. P1 S2

- order：23

- section：2.1 Crowding information as a DSS feature

- locator：P1 S2

- move_code：MECHANISM

- paraphrase_cn：不确定时用户会把高需求解释为高质量，并模仿他人行为，因此倾向于选择高需求地点。

- rhetorical_function_cn：说明CI可能产生与公共健康目标相反的力量。

- depends_on_cn：需求信息文献。

- sets_up_cn：为H1中的质量信号 vs. 拥堵成本权衡提供基础。

- evidence_pointer：Section 2.1 P1 S2

### 24. P2 S1

- order：24

- section：2.1 Crowding information as a DSS feature

- locator：P2 S1

- move_code：MECHANISM

- paraphrase_cn：CI针对有限容量地点的竞争性：拥挤增加拥堵成本和对他人的负外部性，如等待时间和身体接近。

- rhetorical_function_cn：说明CI的另一个面向：拥挤成本。

- depends_on_cn：需求质量信号机制。

- sets_up_cn：在疫情下这些成本更突出。

- evidence_pointer：Section 2.1 P2 S1

### 25. P2 S3

- order：25

- section：2.1 Crowding information as a DSS feature

- locator：P2 S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：在疫情中，暴露强度和时间构成重要成本，可能破坏身体距离，因此需要研究CI是否能改变选择。

- rhetorical_function_cn：把拥挤成本机制连接到COVID-19现实。

- depends_on_cn：拥堵成本解释。

- sets_up_cn：为H1做理论铺垫。

- evidence_pointer：Section 2.1 P2 S3

### 26. P1 S1

- order：26

- section：2.2 Construal level theory

- locator：P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：建构水平理论描述目标或信息与个人心理距离如何决定心理表征的抽象或具体程度。

- rhetorical_function_cn：正式引入第二个理论视角。

- depends_on_cn：前面对即时性和健康焦虑的讨论。

- sets_up_cn：为H2和H3提供机制语言。

- evidence_pointer：Section 2.2 P1 S1

### 27. P2 S2

- order：27

- section：2.2 Construal level theory

- locator：P2 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：更高即时性表示更近的时间距离，因此导致用户对地点更具体地思考；低即时性则导致更抽象的表征。

- rhetorical_function_cn：把即时性翻译成时间距离。

- depends_on_cn：建构水平理论。

- sets_up_cn：为H2的建构匹配论证创造条件。

- evidence_pointer：Section 2.2 P2 S2

### 28. P2 S4

- order：28

- section：2.2 Construal level theory

- locator：P2 S4

- move_code：LIMITATION

- paraphrase_cn：先前IS研究的时间线索多数针对静态信息，动态变化信息如CI的即时性作用仍未清楚。

- rhetorical_function_cn：指出文献局限。

- depends_on_cn：时间线索研究回顾。

- sets_up_cn：为H2提供创新空间。

- evidence_pointer：Section 2.2 P2 S4

### 29. P3 S1

- order：29

- section：2.2 Construal level theory

- locator：P3 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：健康焦虑会改变用户的假设距离，高健康焦虑使健康威胁显得更可能、更接近。

- rhetorical_function_cn：把健康焦虑纳入建构水平理论。

- depends_on_cn：心理距离维度。

- sets_up_cn：为H3预测健康焦虑与即时性的交互。

- evidence_pointer：Section 2.2 P3 S1

### 30. P3 S2

- order：30

- section：2.2 Construal level theory

- locator：P3 S2

- move_code：LIMITATION

- paraphrase_cn：先前研究主要孤立分析假设距离，未考察与时间距离等维度的交互。

- rhetorical_function_cn：制造理论扩展的缺口。

- depends_on_cn：假设距离讨论。

- sets_up_cn：为理论贡献主张铺路。

- evidence_pointer：Section 2.2 P3 S2

### 31. Section 3 intro S1

- order：31

- section：3. Hypothesis development

- locator：Section 3 intro S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：先假设CI的影响，然后假设即时性的影响，最后假设健康焦虑的调节作用。

- rhetorical_function_cn：预告假设部分结构。

- depends_on_cn：理论背景。

- sets_up_cn：为H1-H3的顺序建立预期。

- evidence_pointer：Section 3 intro

### 32. P1 S4

- order：32

- section：3.1 The effect of CI on selection behaviour

- locator：P1 S4

- move_code：MECHANISM

- paraphrase_cn：虽然有高质量信号吸引，但疫情中同时出现的感染风险可能压倒质量信号，使用户转向低拥挤地点。

- rhetorical_function_cn：整合两个相反力量，推导出H1。

- depends_on_cn：2.1中的质量信号和拥堵成本。

- sets_up_cn：直接导出H1。

- evidence_pointer：Section 3.1 P1 S4

### 33. P1 S5

- order：33

- section：3.1 The effect of CI on selection behaviour

- locator：P1 S5

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H1：疫情时期，CI存在时用户比CI缺失时更可能选择低拥挤地点。

- rhetorical_function_cn：正式陈述第一个假设。

- depends_on_cn：前句的权衡论证。

- sets_up_cn：由后续Model 1检验。

- evidence_pointer：Section 3.1 H1

### 34. P1 S1

- order：34

- section：3.2 The effect of immediacy of CI

- locator：P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：建构匹配发生在目标与信息的建构水平一致时；立即选择地点的目标通常是具体、低水平建构的。

- rhetorical_function_cn：为高即时性的作用提供理论机制。

- depends_on_cn：建构水平理论。

- sets_up_cn：解释为什么高即时性匹配目标。

- evidence_pointer：Section 3.2 P1 S1

### 35. P2 S1-S2

- order：35

- section：3.2 The effect of immediacy of CI

- locator：P2 S1-S2

- move_code：MECHANISM

- paraphrase_cn：高即时性通过建构匹配提高加工流畅性，一方面使信息更可信、减少乐观偏差，另一方面帮助用户更易理解拥挤成本，因此更拥挤地点吸引力下降。

- rhetorical_function_cn：给出H2的两个具体机制。

- depends_on_cn：建构匹配假设。

- sets_up_cn：为H2和后续流畅性补充分析。

- evidence_pointer：Section 3.2 P2 S1-S2

### 36. P2 S3

- order：36

- section：3.2 The effect of immediacy of CI

- locator：P2 S3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H2：CI即时性高时，用户比即时性低时更可能选择低拥挤地点。

- rhetorical_function_cn：正式陈述第二个假设。

- depends_on_cn：机制论证。

- sets_up_cn：由Model 2和后续检验。

- evidence_pointer：Section 3.2 H2

### 37. P1 S1

- order：37

- section：3.3 The moderating role of health anxiety

- locator：P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：健康焦虑导致更近的假设距离和对健康风险的更具体构想。

- rhetorical_function_cn：把健康焦虑与建构水平理论连接。

- depends_on_cn：2.2的理论背景。

- sets_up_cn：为H3预测交互作用。

- evidence_pointer：Section 3.3 P1 S1

### 38. P2 S2

- order：38

- section：3.3 The moderating role of health anxiety

- locator：P2 S2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H3：健康焦虑调节即时性的影响，健康焦虑更高的用户在CI即时时更可能选择低拥挤地点。

- rhetorical_function_cn：正式陈述调节假设。

- depends_on_cn：健康焦虑放大风险感知的推理。

- sets_up_cn：由Model 3检验并最终被拒绝。

- evidence_pointer：Section 3.3 H3

### 39. P1 S1

- order：39

- section：4. Method

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为检验假设，作者设计了三条件组间在线实验，并选择德国和意大利作为疫情严重程度不同但可比较的国家。

- rhetorical_function_cn：说明实验类型和跨国家设计理由。

- depends_on_cn：研究问题。

- sets_up_cn：为外部效度提供初步依据。

- evidence_pointer：Section 4 P1 S1

### 40. P2 S1

- order：40

- section：4. Method

- locator：P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择医疗诊所是因为COVID-19在密切接触中传播，候诊室感染风险高；用户急需信息；诊所质量难以提前评估。

- rhetorical_function_cn：论证实验情境选择合理性。

- depends_on_cn：COVID-19传播机制。

- sets_up_cn：使操纵和选择任务具有现实意义。

- evidence_pointer：Section 4 P2 S1-S3

### 41. P1 S1-S2

- order：41

- section：4.1 Experimental DSS and manipulations

- locator：P1 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：创建虚构网站“find-your-doctor.org”，控制条件不显示CI，两个处理条件分别用1-4个人形图标显示拥挤水平，并用“usual amount of patients (past 2 months)”和“live amount of patients (updated just now)”区分即时性。

- rhetorical_function_cn：具体说明实验制品的核心设计。

- depends_on_cn：理论定义。

- sets_up_cn：为操控检验提供对象。

- evidence_pointer：Section 4.1, Figure 2

### 42. P1 S1

- order：42

- section：4.2 Experimental procedure

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：参与者被要求设想因背痛需要找替代诊所，然后随机分配到条件，观看地图并选择诊所，最后填写问卷。

- rhetorical_function_cn：说明实验程序以提高可复制性。

- depends_on_cn：实验设计和操纵。

- sets_up_cn：为数据和质量控制程序铺路。

- evidence_pointer：Section 4.2, Figure 3

### 43. P1 S1

- order：43

- section：4.3 Measurements

- locator：P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：因变量记录所选诊所的拥挤水平；健康焦虑用七点量表测量；同时测量多个控制变量和三个操控检查。

- rhetorical_function_cn：界定结果变量和分析变量。

- depends_on_cn：研究假设和实验设计。

- sets_up_cn：为后续统计模型设定变量集。

- evidence_pointer：Section 4.3, Table A1

### 44. 5.1 P1 S1

- order：44

- section：5. Analysis and results

- locator：5.1 P1 S1

- move_code：RESULT

- paraphrase_cn：从360名Prolific参与者中获得343名通过全部注意力检查的有效样本。

- rhetorical_function_cn：报告样本过滤结果，显示数据质量。

- depends_on_cn：数据采集程序。

- sets_up_cn：为后续样本描述和检验建立基线。

- evidence_pointer：Section 5.1 P1 S1

### 45. P2 S1

- order：45

- section：5.1 Sample description

- locator：P2 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：条件间在年龄、产品卷入和健康焦虑上无显著差异，支持随机化成功；操控检查显示感知拥挤和感知即时性在不同条件下显著不同。

- rhetorical_function_cn：验证内部有效性。

- depends_on_cn：样本数据。

- sets_up_cn：为可信的假设检验奠定基础。

- evidence_pointer：Section 5.1 P2 S1-S3

### 46. P2 S5

- order：46

- section：5.1 Sample description

- locator：P2 S5

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：德国和意大利两国的选择行为、操控检查和年龄无显著差异，但意大利参与者健康焦虑和产品卷入更高，反映疫情严重程度差异。

- rhetorical_function_cn：检验跨国家稳健性并解释差异。

- depends_on_cn：样本数据。

- sets_up_cn：为跨国推广提供证据。

- evidence_pointer：Section 5.1 P2 S5

### 47. P1 S1

- order：47

- section：5.2 Reliability and validity

- locator：P1 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：CFA显示AVE、载荷、信度和HTMT均达到阈值，测量模型具有收敛和区分效度。

- rhetorical_function_cn：验证测量质量。

- depends_on_cn：问卷数据。

- sets_up_cn：确保后续检验不是测量噪声。

- evidence_pointer：Section 5.2

### 48. P1 S1

- order：48

- section：5.3 Hypothesis testing

- locator：P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因变量是四水平有序变量，故使用有序logistic回归，并检验比例优势假设和模型拟合。

- rhetorical_function_cn：说明统计方法选择合理性。

- depends_on_cn：变量性质。

- sets_up_cn：为三个模型结果作准备。

- evidence_pointer：Section 5.3 P1 S1

### 49. P3 S1

- order：49

- section：5.3 Hypothesis testing

- locator：P3 S1

- move_code：RESULT

- paraphrase_cn：Model 1支持H1：CI存在使选择低拥挤诊所的几率提高4.6倍。

- rhetorical_function_cn：给出第一个核心结果。

- depends_on_cn：有序logistic回归。

- sets_up_cn：支撑CI有效性的中心主张。

- evidence_pointer：Section 5.3 Model 1, Table 1

### 50. P3 S2

- order：50

- section：5.3 Hypothesis testing

- locator：P3 S2

- move_code：RESULT

- paraphrase_cn：Model 2支持H2：更高即时性导致选择低拥挤地点。

- rhetorical_function_cn：给出第二个核心结果。

- depends_on_cn：有序logistic回归。

- sets_up_cn：为即时性设计提供证据。

- evidence_pointer：Section 5.3 Model 2, Table 1

### 51. P3 S3

- order：51

- section：5.3 Hypothesis testing

- locator：P3 S3

- move_code：RESULT

- paraphrase_cn：Model 3不支持H3；相反，低健康焦虑用户在实时CI下选择低拥挤地的几率是6.4倍，高健康焦虑用户只有2.5倍。

- rhetorical_function_cn：报告反直觉交互结果并拒绝H3。

- depends_on_cn：有序logistic回归。

- sets_up_cn：为讨论中的重新解释和理论贡献提供基础。

- evidence_pointer：Section 5.3 Model 3, Figure 4

### 52. P1 S1

- order：52

- section：6. Discussion

- locator：P1 S1

- move_code：RESULT

- paraphrase_cn：回归两个研究问题，指出结果在德国和意大利均稳健，CI显著促进选择低拥挤地点。

- rhetorical_function_cn：讨论开头重新连接引言RQ。

- depends_on_cn：实证结果。

- sets_up_cn：为实践和理论贡献奠定结构。

- evidence_pointer：Section 6 P1 S1

### 53. P1 S3

- order：53

- section：6. Discussion

- locator：P1 S3

- move_code：MECHANISM

- paraphrase_cn：作者推测高健康焦虑用户在实时信息下可能利用更高流畅性来更重视地点质量，并产生“无论去哪都有风险”的宿命感，因此更倾向选择高需求地点。

- rhetorical_function_cn：为反直觉结果提供事后解释。

- depends_on_cn：H3被拒绝。

- sets_up_cn：为理论贡献中的多距离交互铺路。

- evidence_pointer：Section 6 P1 S3

### 54. P2 S1

- order：54

- section：6.1 Practical implications

- locator：P2 S1

- move_code：CONTRIBUTION

- paraphrase_cn：CI是DSS提供者和政策制定者促进身体距离的有力工具，可在不侵犯自由选择的情况下提供自我调节机制。

- rhetorical_function_cn：把结果转化为政策建议。

- depends_on_cn：核心结果H1/H2。

- sets_up_cn：与引言中家长式干预问题形成对照。

- evidence_pointer：Section 6.1 P2 S1

### 55. P3 S2

- order：55

- section：6.1 Practical implications

- locator：P3 S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：即时CI在用户健康焦虑尚未过高时最有效，但显示CI总比不显示好，即使高焦虑用户仍有正效应。

- rhetorical_function_cn：界定实践建议的边界。

- depends_on_cn：反直觉调节结果。

- sets_up_cn：防止政策含义被理解为完全无效。

- evidence_pointer：Section 6.1 P3 S2

### 56. P1 S1

- order：56

- section：6.2 Research and theoretical contributions

- locator：P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：研究推进了数字选择环境如何影响选择行为的理解，把CI作为新的DSS特征，反映需求与容量的比较以及拥挤成本。

- rhetorical_function_cn：把结果概括为理论贡献。

- depends_on_cn：引言中的理论缺口。

- sets_up_cn：为建构水平理论扩展奠基。

- evidence_pointer：Section 6.2 P1 S1

### 57. P2 S1

- order：57

- section：6.2 Research and theoretical contributions

- locator：P2 S1

- move_code：CONTRIBUTION

- paraphrase_cn：研究扩展建构水平理论，将即时性视为时间距离新面向，并联合考察时间距离与假设距离，克服先前孤立分析心理距离的局限。

- rhetorical_function_cn：从反直觉结果中提取理论价值。

- depends_on_cn：2.2中的理论缺口。

- sets_up_cn：为未来研究多距离交互铺路。

- evidence_pointer：Section 6.2 P2 S1

### 58. P1 S1

- order：58

- section：6.3 Limitations and directions for future research

- locator：P1 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：结果基于两个欧洲国家的在线实验，未来需现场设置和其他国家及地点检验，并评估CI能否真正避免封锁。

- rhetorical_function_cn：承认外部效度限制。

- depends_on_cn：实验设计。

- sets_up_cn：保护贡献不被过度一般化。

- evidence_pointer：Section 6.3 P1 S1

### 59. P2 S1

- order：59

- section：6.3 Limitations and directions for future research

- locator：P2 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来研究应考察拥挤成本的中介作用、DSS对长期健康焦虑的影响以及不同疫情阶段的效应。

- rhetorical_function_cn：指明机制和纵向研究缺口。

- depends_on_cn：反直觉结果和未测机制。

- sets_up_cn：为后续研究提供路线图。

- evidence_pointer：Section 6.3 P2 S1

### 60. P3 S1

- order：60

- section：6.3 Limitations and directions for future research

- locator：P3 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：提供实时CI需要集中数据采集和自动化处理，未来需研究多方协作时的基础设施和法律要求。

- rhetorical_function_cn：指出实践实施的限制。

- depends_on_cn：实时CI的特征。

- sets_up_cn：使实践建议更现实。

- evidence_pointer：Section 6.3 P3 S1

### 61. P1 S1-S2

- order：61

- section：7. Conclusion

- locator：P1 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：在结论中重申DSS日益重要，并总结在线实验证明CI对选择低拥挤地点的因果效应以及即时性和健康焦虑的作用，强调对疫情即刻控制的意义。

- rhetorical_function_cn：收束全文，回到引言中的紧迫问题。

- depends_on_cn：所有实证结果和讨论。

- sets_up_cn：结束论证并留下行动号召。

- evidence_pointer：Section 7

## 写作技术

- gap_construction_cn：作者先将CI定义为现实且常见的DSS特征，再指出一个危险矛盾：已有需求信息文献预测用户会被高需求吸引，因此CI可能适得其反。通过“如果在善意的系统中用户反而选择更拥挤地点”这一反事实，把知识缺口转化为紧迫的现实风险，再补充即时性和健康焦虑两个未被研究的调节因素，最终形成两个RQ。

- signposting_cn：摘要中预告研究问题和结果；引言末尾预告方法、样本和贡献；理论部分开头预告CI和CLT两块内容；假设部分开头预告H1-H3；方法、结果和讨论各部分都有清晰的路标。

- transition_logic_cn：段落间常用“除了主效应之外”“第二”和“因此”推进；从问题到理论、从理论到假设、从假设到实验、从实验到讨论均使用显式过渡句；讨论以RQ复述作为再锚点。

- claim_evidence_rhythm_cn：每个假设后紧接有序logistic回归模型和odds ratio；实证结果前先呈现操控检查、随机化、信效度，形成“先证明测量有效，再报告因果估计”的节奏；反直觉结果后紧接着讨论解释，但用“we speculate”区分证据与推测。

- benchmark_narrative_cn：以CI缺失作为最底层基线，证明任何CI都有效；以历史平均CI作为实时CI的对照，证明时间维度上的增益；加入德国和意大利的比较，将基线检查转化为跨情境稳健性；操控检查和加工流畅性作为心理证据嵌入叙述。

- theory_return_cn：实证结果不止步于“有显著效应”，而是回到建构水平理论：H2被解释为建构匹配与流畅性；H3的反直觉结果被用来论证时间距离与假设距离的联合作用，从而将失败假设转化为理论扩展点。

- contribution_positioning_cn：作者用“既有思维/实践 vs. 本文贡献”的表格和段落，把CI从一个疫情特例提升为数字选择环境中需求信息的新形式；把即时性从静态时间线索中分离出来，确立为动态信息的新时间面向；把健康焦虑从个体差异变量转化为假设距离的实证操作。

- novelty_protection_cn：通过受控实验、随机分配、操控检验、多国样本和补充流畅性分析，防止结果被解读为一次性在线现象；通过把反直觉调节嵌入理论扩展，使论文即使假设被拒也能贡献理论；通过反复强调“无CI就不显示、显示实时CI最有效”的政策信息，将局部实验证据转化为可复制设计原则。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：在引言中用危机背景和具体应用确立一个信息系统特征（如CI）的现实重要性。

- research_job_cn：识别一个在真实DSS中已经存在但缺乏因果评估的设计特征。

- required_evidence_cn：真实系统例子、WHO/实践引述、政策语境；需要说明该特征有潜在公共价值。

- transition_to_next_cn：指出“虽然已部署，但没有因果证据”，导向研究缺口。

#### 2. 2

- step：2

- writing_job_cn：用既有文献制造缺口：说明已有理论或实证可能预测相反结果。

- research_job_cn：梳理相关类型的信息（如需求信息）在数字选择环境中的效应。

- required_evidence_cn：至少一组会指向相反方向的文献；形成“若该系统真按文献工作，可能有害”的反事实。

- transition_to_next_cn：由缺口引入可解释新机制的理论。

#### 3. 3

- step：3

- writing_job_cn：引入理论将特征翻译为可测试的假设，并为调节变量提供理论基础。

- research_job_cn：选择能解释该特征处理机制的理论，并将特征属性映射到理论构念（如时间距离、假设距离）。

- required_evidence_cn：理论命题能推导出至少两个可操纵/可测量的差异和一个交互项。

- transition_to_next_cn：假设形成后转入实验设计。

#### 4. 4

- step：4

- writing_job_cn：设计并描述实验制品和处理条件：一个最小但逼真的数字界面，包含基线条件。

- research_job_cn：创建网站/界面，设计操纵（有/无特征、高/低水平），并确保情境对目标人群有意义。

- required_evidence_cn：操纵的具体刺激、条件间唯一差异、场景真实性保证。

- transition_to_next_cn：描述程序并说明测量工具。

#### 5. 5

- step：5

- writing_job_cn：报告数据采集、样本筛选、随机化检查和操纵检查，建立内部有效性。

- research_job_cn：进行在线实验，使用注意力检查、操控检查、信效度分析。

- required_evidence_cn：样本量、通过率、条件间平衡、操控感知差异、测量模型达标。

- transition_to_next_cn：在测量可信后进入核心统计检验。

#### 6. 6

- step：6

- writing_job_cn：用适合因变量性质的统计模型（如有序logistic回归）报告嵌套模型结果和效应量。

- research_job_cn：按假设设计模型层级：基础效应→特征水平→调节变量；检验模型假设和拟合。

- required_evidence_cn：回归系数、标准差、显著性、odds ratio、伪R²；假设支持/拒绝的清晰陈述。

- transition_to_next_cn：结果后进入解释和理论返回。

#### 7. 7

- step：7

- writing_job_cn：在讨论中回到RQ，把结果翻译为实践意义和理论贡献，并用限制保护主张。

- research_job_cn：对反直觉结果给出机制推测；比较既有思维与本文贡献；明确不能在未测情境中推广。

- required_evidence_cn：结果与背景文献的对照、边界条件、下一研究需要的数据。

- transition_to_next_cn：结论段落以行动性语言收束。

### most_transferable_moves_cn

1. 用真实系统例子和危机背景包装设计特征，使IS研究具有即时相关性。

2. 通过“已有文献预测相反方向”制造缺口，而非仅说“没人研究”。

3. 在实验结果前先报告操控检查和随机化平衡，增强因果可信度。

4. 用嵌套模型逐层回答“特征是否有用→更强形式是否更有用→谁受益最多”。

5. 将反直觉结果转化为理论扩展点，而不是隐藏它。

6. 以表格“既有思维/实践 vs. 本文贡献”清晰定位贡献。

### resource_intensive_or_nonstandard_parts_cn

1. 需要在疫情真实流行期间快速收集跨国样本，依赖Prolific等平台和现实事件的时间窗口。

2. 医疗诊所场景虽可用虚构网站模拟，但需要精细的视觉刺激和操控检查。

3. 跨国家比较需要能够获得有多国参与者的高质量众包样本。

4. 若没有真实疫情背景和WHO政策语境，同样的实验会失去紧迫性。

### what_not_to_copy_superficially_cn

1. 不能只引用建构水平理论而不实际推导设计差异；必须把时间距离、假设距离翻译成具体刺激和测量。

2. 不能只报告“显著”而不报告odds ratio和实际选择变化；需要给读者直观数量。

3. 不能把讨论中的推测（如健康焦虑导致质量关注）当作已验证机制；否则会在同行评审中暴露漏洞。

4. 不能忽略基线和对照条件；没有无特征/低水平对照，因果主张无法成立。

- single_best_description_of_the_routine_cn：用真实危机场景包装一个已有但未验证的信息设计特征，从既有文献中挖出它可能适得其反的矛盾，用建构理论把特征的两个水平和一个个体差异翻译成实验处理，借助跨国在线实验和有序logistic回归证明特征能改变选择，再用反直觉调节扩展理论并给出非强制政策建议。

## 分析边界

本文基于提供的全文PDF/文本进行分析，缺少原始页码和可能的在线附录；没有观察到作者是否做过更细的鲁棒性检验或预注册；健康焦虑反直觉机制属于事后推测，无法从论文数据中直接验证；跨文化外部效度仅有两个欧洲国家；统计分析细节（如比例优势假设检验的具体输出）未完整呈现。
