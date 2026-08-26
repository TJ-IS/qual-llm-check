# Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging

- 作者：Konstantina Valogianni; Wolfgang Ketter; John Collins; Gediminas Adomavicius
- 年份 / 期刊：2026 / Information Systems Research
- DOI：10.1287/isre.2023.0078
- 源文件：28578_2026_toward-sustainable-electricity-markets-capacity-based-pricing-for-electric-vehicle-smart-chargin.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.85

## 文章级论证概况

- 核心问题：在电网运营商无法获知个体EV车主偏好和可用性约束、且需满足收入目标的情况下，如何设计一个低计算复杂度的定价制品，诱导EV智能充电形成期望的聚合需求曲线，从而缓解峰值和雪崩效应并支持可再生能源整合？

- 制品与设计：基于容量的定价（capacity-based pricing, CBP）：单位电价由不依赖充电速率的基准价P0,t和依赖充电速率的容量项α_t·r组成；配套两族价格设定方法——基于无约束情形解析推导的analytical heuristic (AH)，以及从AH初始化并利用聚合充电行为数据进行修正的计算启发式(CH)。

- 客观结果：仿真结果表明，CBP配置在flat、补足家庭负荷、跟随PV三个场景中均显著优于flat pricing、rate-independent variable pricing和increasing-block pricing基准；其中CBP-CH达到近最优RMSE（如flat场景0.02 MWh、PAPR 1.07），并能在收入目标附近实现极小偏差（如0.08%）。

- 核心贡献：作者声称提出了一个IS赋能的容量定价制品，结合agent理性优化与中央协调，可在不依赖多次迭代/学习、不假设额外消费者行为特性、不限制期望需求曲线形状的情况下诱导任意期望EV充电曲线，同时维持收入等价，并推进Green IS与智能城市可持续交通。

- 整篇论证链：文章从大规模EV引入会导致晚高峰电网压力并可能威胁稳定性出发，指出现有协调方案要么需要昂贵基础设施、要么依赖外生控制、要么在统一价格下引发雪崩效应。随后通过2.2-2.3节文献梳理，将缺口界定为现有定价机制普遍存在三大约束：需要大量迭代学习、依赖除成本最小化外的消费者响应假设、以及期望需求剖面被限定为平坦或特定形状。为克服这些约束，作者引入容量定价形式P_t(r)=P0,t+α_t·r，利用“充电速率越高占用电网容量越大”的经验知识，把容量成本内化到单位电价中；在无充电可用性约束的理想情形下，作者用四组定理推导出可诱导期望曲线并实现目标收入的解析条件，形成解析启发式AH；随后将AH作为初值，利用可观测的聚合需求与收入的偏差设计计算启发式CH，使价格能够适应有私有约束的异质EV群体。评价部分构建基于Power TAC的多agent仿真，用荷兰真实出行与电价数据校准，把CBP的四种配置与三类基准在平坦曲线、家庭负荷互补、跟随PV出力三种期望曲线下比较，并用RMSE、PAPR、绝对峰值及收入偏差作为指标。结果表明CBP-CH在三类场景中都最接近期望曲线且收入偏差极小，稳健性分析还显示对近视型agent仍保持优势。讨论部分将结果回接到Green IS框架，把贡献定位为可快速适应真实环境、可诱导任意需求曲线、内置收入平衡能力的IS制品，同时用边界条件与未来方向保护其免于被视为一次性仿真结果。

## 类型与写作弧线判定

- 论文主类型判定：文章自我定位为Gregor & Hevner“Improvement”类设计科学，明确以需求/问题—制品构建（定价公式与AH/CH启发式）—仿真环境评价—设计知识贡献的顺序展开；虽然有形式模型推导和benchmark，但其核心论证逻辑是设计制品的构建与多场景评价。

- 主导写作弧线判定：论文从问题出发，用非线性定价与理性agent优化知识推导出容量定价的理论条件（Section 4），据此设计制品，再通过仿真检验，最后在讨论中回到Green IS理论贡献；这与“问题—理论—设计—检验—回到理论”的弧线最吻合。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：研究依次由七个阶段累积：解析理论推导→计算启发式设计→仿真平台构建→三个难度递进的评价场景→稳健性检验。前面的解析结果为计算启发式提供初值；平台为场景评价提供统一条件；平坦场景展示基本能力，家庭负荷互补场景证明非平坦EV曲线诱导，PV跟随场景连接可持续性目标；稳健性检验排除agent能力和预测误差作为结果驱动因素。

### studies_or_phases

#### 1. 解析启发式推导（无可用性约束的理想情形）

- order：1

- name_cn：解析启发式推导（无可用性约束的理想情形）

- question_cn：当EV agent理性且没有充电可用性约束时，容量定价的α参数应如何设定才能诱导期望需求曲线并实现给定收入目标？

- inputs_and_setting_cn：数学环境：T个离散时段，I个理性无约束agent，总充电需求Φ，期望剖面D，目标收入Ψ*；假设P0,t恒定或一般情形（附录C/D）。

- designed_or_compared_object_cn：容量定价价格参数α向量及其与期望剖面、收入目标的关系；不是实验对比，而是推导闭合条件。

- baseline_control_or_counterfactual_cn：无，理论证明与特殊/一般情形推导。

##### objective_metrics

1. closed-form诱导条件

2. 收入与期望剖面同时满足性

3. 是否需要个体偏好信息

- analysis_method_cn：解析推导：参数最优化、Kuhn-Tucker/一阶条件风格、最优解族参数化；定理与推论（Theorem 1-4及附录C/D）。

- main_result_cn：Theorem 1给出理性agent在容量定价下的最优充电率为与α_t成反比；Theorem 2给出诱导剖面D的条件为α_t·D_t/δ恒定，并且该条件不需要个体充电需求信息；Theorem 3-4给出在已知/未知个体需求信息下实现目标收入的α参数选择与调整公式。

- argumentative_role_cn：把“充电速率定价”这种设计直觉转化为可操作的解析启发式，并证明其能在理想情形下同时实现曲线诱导与收入目标，为后续计算启发式提供初值。

- remaining_uncertainty_cn：假设无可用性约束且能精确知道个体需求；真实环境中有私有可达性约束、异质需求、随机驾驶行为，这些理想条件不一定成立。

- link_to_next_phase_cn：因为真实网格管理者是不完全信息问题，作者在下一阶段以AH为初始值，引入基于聚合观测数据的计算调整。

##### evidence_pointers

1. Section 4标题与开头

2. Theorem 1, 2, 3, 4

3. 在线附录C/D一般化证明

4. Figure 5-6价格-充电率示例

#### 2. 计算启发式（CH）设计：基于聚合行为数据调整价格

- order：2

- name_cn：计算启发式（CH）设计：基于聚合行为数据调整价格

- question_cn：当EV agent有私有充电可用性约束和偏好，且网格只观察聚合需求与收入时，如何以低迭代次数将需求曲线和收入调整到目标？

- inputs_and_setting_cn：来自智能电表/网格可观察的聚合信息：初始预期需求D与目标收入Ψ*，广播CBP价格后观测到的聚合需求D^o与收入Ψ^0/Ψ^1/Ψ^2；个体需求分布信息可选（minimal或distributional）。

- designed_or_compared_object_cn：CH三步算法：初始化（Step1用定理3推论选α^0）；Step2a用w=D^o/D做α^1=α^0·w；Step2b用定理4推论调α^2；Step2c用两观测点拟合F=f(Ψ)线性函数并外推F*。

- baseline_control_or_counterfactual_cn：与AH比较：是否使用数据驱动调整；信息版本minimal vs -Distrib。

##### objective_metrics

1. 迭代次数

2. 接近目标收入Ψ*的误差

3. 接近期望剖面D的误差

- analysis_method_cn：算法设计+基于定理2/3/4的性质论证；说明α^1属于D=w诱导族，从而继承解析性质。

- main_result_cn：CH在无约束时理论上同AH最优，在有私有约束时通过少数观测与线性外推即可近最优匹配期望剖面和收入。

- argumentative_role_cn：从理想解析解过渡到现实中可用信息设置，使制品既能适应不完全信息又不依赖长时间学习。

- remaining_uncertainty_cn：算法表现依赖启发式假设，即α与充电量的反比关系在带约束时仍近似成立；只在仿真中被检验，尚未现场验证。

- link_to_next_phase_cn：为检验CH的实际表现，下一阶段搭建仿真testbed并用真实数据校准。

##### evidence_pointers

1. Section 5完整算法步骤

2. Step 1/2a/2b/2c描述

3. D=w-inducing family论证

4. Table 1的CH配置

#### 3. 多agent仿真testbed构建与校准

- order：3

- name_cn：多agent仿真testbed构建与校准

- question_cn：如何用真实数据构造一个含异质理性EV agent和网格控制agent的多agent仿真，使容量定价制品能在不同期望曲线和基准下被公平评价？

- inputs_and_setting_cn：荷兰CBS出行统计、EPEX批发电价加税费、荷兰家庭负荷数据、PV出力数据（威斯康星Hudson）、Power TAC规范、1,500充电桩/231,976笔真实交易数据用于flat基准。

- designed_or_compared_object_cn：仿真环境（T=168h, δ=1h, I=1000 EV agent）；评价指标集合；4种CBP配置；3类benchmark。

- baseline_control_or_counterfactual_cn：Benchmark 1真实世界flat pricing；Benchmark 2 rate-independent variable pricing（按残余容量反向定价）；Benchmark 3 increasing-block pricing（按Borenstein表并按期望剖面调整区段）。

##### objective_metrics

1. RMSE

2. 绝对峰值D_peak

3. PAPR

4. 收入偏差%

- analysis_method_cn：agent-based simulation；从分布抽样生成agent偏好并求解每agent最优化充电计划；多回合观察/调整（用于CH）。

- main_result_cn：无主要结果，属方法/平台搭建；建立了可配置粒度、可复现的仿真评价环境。

- argumentative_role_cn：为后续三个场景提供统一受控实验平台，并把真实世界数据嵌入使结果具有外部有效性。

- remaining_uncertainty_cn：仿真基于历史数据和分布抽样，无法完全代表真实市场中的行为反馈和学习；需要更多场景和稳健性检验。

- link_to_next_phase_cn：平台准备好后，依次在平坦、非平坦、高波动三种期望剖面下评估。

##### evidence_pointers

1. Section 6.1 steps 1-6

2. Section 6.2 metrics

3. Section 6.3 data description

4. Section 6.4 benchmarks

5. Section 6.5 Table 1

#### 4. 场景1：诱导平坦充电曲线并生成目标收入

- order：4

- name_cn：场景1：诱导平坦充电曲线并生成目标收入

- question_cn：在期望EV充电曲线为完全水平（flat）且需达到指定收入目标时，CBP各配置是否优于基准并接近最优？

- inputs_and_setting_cn：I=1000个异质EV agent，总需求Φ=168 MWh，P0,t=P0=0.05货币单位/kWh，目标收入Ψ*=17,878.6货币单位（等于flat pricing下的收入），T=168h。

- designed_or_compared_object_cn：广播的CBP价格α向量由AH/CH四配置生成；与flat pricing和increasing-block比较。

- baseline_control_or_counterfactual_cn：期望剖面图上1 MWh/小时的地板曲线；flat pricing和increasing-block为基准；理想zero误差为下限。

##### objective_metrics

1. RMSE (MWh)

2. PAPR

3. Peak (MWh)

4. Revenue % diff from target

- analysis_method_cn：在仿真中运行每个定价方法，观察聚合充电曲线和收入；比较指标。

- main_result_cn：CBP-CH产生RMSE 0.02 MWh、PAPR 1.07、峰值1.03 MWh，接近理想；CBP-AH RMSE 0.24、PAPR 1.46、峰值1.24；increasing-block RMSE 0.25、PAPR 1.63、峰值1.32；flat pricing 0.88/2.89/2.03。收入偏差CBP-AH 2.70%，CBP-AH-Distrib 0.14%，CBP-CH 0.12%，CBP-CH-Distrib 0.08%。

- argumentative_role_cn：提供第一个证据：在经典平坦剖面任务中，CBP能显著改善grid balancing，并能同时满足收入覆盖目标，而benchmark没有收入目标能力。

- remaining_uncertainty_cn：Flat是最简单剖面，可能高估CBP；现实网格更关心非平坦曲线、可再生能源跟随。

- link_to_next_phase_cn：下一场景转向更难的“EV充电+家庭负荷总曲线平坦”，即诱导非平坦EV曲线。

##### evidence_pointers

1. Section 7.1

2. Figure 12

3. Table 2

4. Table 3

5. Figure 13

#### 5. 场景2：补充家庭负荷以平抑总需求

- order：5

- name_cn：场景2：补充家庭负荷以平抑总需求

- question_cn：当EV充电需补充现有家庭负荷以使组合需求平坦时，CBP能否在更高波动期望剖面上维持优势？

- inputs_and_setting_cn：I=1000，EV每日总量26 MWh，P0=0.05，T=168h；家庭负荷用荷兰稳态实际需求曲线（约4个月数据）。

- designed_or_compared_object_cn：CBP AH/CH配置产生的价格；比较flat pricing、rate-independent variable pricing、increasing-block pricing。

- baseline_control_or_counterfactual_cn：期望总曲线（本来家庭负荷加上EV充电后接近平坦）；基准中rate-independent variable pricing代表无容量分量时造成雪崩效应。

##### objective_metrics

1. RMSE

2. PAPR

3. Peak (MWh)

- analysis_method_cn：仿真运行并画出EV曲线、组合曲线及指标表。

- main_result_cn：CBP-CH RMSE 0.03 MWh、PAPR 1.06、峰值2.69 MWh，接近期望峰值2.61；CBP-AH RMSE 0.29/1.37/3.07；increasing-block 0.48/1.74/3.39；flat pricing 1.12/2.22/4.23；variable pricing 2.17/6.22/8.42，其低谷时段充电形成明显雪崩峰。

- argumentative_role_cn：证明CBP在诱导非平坦EV曲线方面仍最优，同时说明无容量定价的传统可变价格会诱发雪崩效应，呼应引言核心矛盾。

- remaining_uncertainty_cn：家庭负荷是稳态/历史数据，未考虑与EV充电的实时耦合或其他柔性负荷；收入细节被推到附录H。

- link_to_next_phase_cn：下一场景升级至更强的可持续性目标——使EV充电跟随可再生能源出力。

##### evidence_pointers

1. Section 7.2

2. Figures 14-15

3. Table 4

4. Online Appendix H关于收入表

#### 6. 场景3：追踪PV出力曲线

- order：6

- name_cn：场景3：追踪PV出力曲线

- question_cn：当期望EV曲线是高波动的PV阵列出力曲线时，CBP能否诱导充电跟随可再生能源，并保持收入目标？

- inputs_and_setting_cn：I=1000；PV总产量Φ=522.56 MWh；数据来自美国威斯康星Hudson, 2015-04-25至2015-06-23；T=168h。

- designed_or_compared_object_cn：CBP-AH与CBP-CH（以及- Distrib）；因传统benchmark不适合波动剖面，仅报告increasing-block作对照。

- baseline_control_or_counterfactual_cn：期望剖面PV出力曲线；increasing-block pricing作为次级基准（RMSE=4.65）。

##### objective_metrics

1. RMSE

- analysis_method_cn：仿真运行，比较期望与实际充电曲线。

- main_result_cn：CBP-AH RMSE 0.83 MWh，CBP-CH RMSE 0.21 MWh，均远低于increasing-block的4.65 MWh。

- argumentative_role_cn：直接把制品连接到可再生能源整合与Green IS目标，说明即使期望曲线高度波动也能近最优跟随。

- remaining_uncertainty_cn：PV出力作为理想已知目标；实际中可再生能源存在预测误差，需要在在线附录I检验。

- link_to_next_phase_cn：引入预测误差和更近视agent的稳健性检验，以检查结论是否依赖完美信息和前瞻性agent假设。

##### evidence_pointers

1. Section 7.3

2. Figure 16

3. Table 5

4. Online Appendix I、H

#### 7. 稳健性检验：agent能力敏感性与预测误差

- order：7

- name_cn：稳健性检验：agent能力敏感性与预测误差

- question_cn：当EV agent更近视/更少规划，或期望剖面包含预测误差时，CBP相对于基准的优势是否保持？

- inputs_and_setting_cn：同一三个场景，但agent能力降低（myopic，如不掌握长期规划/中间deadline信息）或期望剖面加入预测误差；详见Online Appendices J和I。

- designed_or_compared_object_cn：不同agent能力版本下的CBP与基准；不同误差水平的期望剖面。

- baseline_control_or_counterfactual_cn：与主结果中前瞻性完美信息设定对比；如预测误差情况与无误差期望剖面比。

##### objective_metrics

1. RMSE

2. PAPR

3. Peak

4. 性能保持度

- analysis_method_cn：敏感性分析/稳健性检验；结果列于在线附录。

- main_result_cn：作者报告CBP在所有检验中仍然优于所有基准；在期望剖面含预测误差时仍保持优越的grid balancing。

- argumentative_role_cn：说明主要结论不是由特定agent能力或完美期望剖面假设驱动的，扩大外部有效性和边界描述。

- remaining_uncertainty_cn：仍为仿真证据；未进行真实现场/用户实验，没有检验价格变化长期对驾驶需求的影响。

- link_to_next_phase_cn：稳健性后的讨论把经验结果上升为设计知识和Green IS理论贡献。

##### evidence_pointers

1. Section 7.4

2. Online Appendix J

3. Online Appendix I

4. Online Appendix H

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. DESIGN_FEATURE

5. REQUIREMENT

6. RESULT

7. BENCHMARK_OR_CONTRAST

8. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. LIMITATION

5. MECHANISM

6. THEORY_INTRO

7. RQ_OR_OBJECTIVE

8. DESIGN_FEATURE

9. CONTRIBUTION

10. METHOD_JUSTIFICATION

11. THEORY_PROPOSITION

### theory_and_knowledge_moves

1. THEORY_INTRO

2. PRIOR_KNOWLEDGE

3. LIMITATION

4. GAP

5. WHY_GAP_MATTERS

6. MECHANISM

7. REQUIREMENT

8. THEORY_PROPOSITION

9. DESIGN_FEATURE

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. MECHANISM

4. THEORY_PROPOSITION

5. METHOD_JUSTIFICATION

6. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. BOUNDARY_CONDITION

3. LIMITATION_AND_FUTURE

4. THEORY_INTRO

5. CONTRIBUTION

## 理论/知识到设计的翻译

### 知识/理论基础

1. 非线性/spot定价理论（Schweppe et al. 1988, Gottwalt 2015）：价格结构可包含容量/实时信号，用以激励负荷行为

2. 智能agent与市场设计（Wooldridge & Jennings 1995, Bichler et al. 2010, Power TAC）：软件agent代表消费者优化，市场机制作为协调层

3. Green IS/能源信息学框架（Watson et al. 2010; Ketter et al. 2023）：信息制品应通过需求响应、可再生能源整合实现可持续性

4. EV充电协调机制文献（centralized/decentralized/auction/iterative pricing）中的已有缺陷：雪崩效应、计算复杂度、行为假设

5. 负载均衡领域中的期望曲线/残余容量/容量成本经验知识（Nicholas & Hall, Leemput等）：充电速率对应电网容量占用

- 理论—设计耦合：direct

- 耦合判定理由：文章并非事后套用理论标签，而是从“理性agent成本最小化+非线性定价”这一形式化知识直接推导出CBP的α参数条件（定理1-4），并据此构造AH/CH价格设定方法；随后这些设计差异被仿真评价直接检验。

- 理论到设计翻译链：非线性/spot定价可以按容量占用收费 → 充电速率决定电网容量成本 → 价格中增加与速率r成比例的容量项α·r → EV agent在成本最小化下会以反比于α_t的速率充电 → 因此α向量可成为诱导期望曲线的控制变量 → 在无约束条件下定理2给出诱导条件，定理3-4给出收入和实际观测调整；在带私有约束条件下以AH为初值并用聚合观测偏差w修正α，形成CH。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：非线性的spot/capacity定价思想认为对电网容量占用收费可以影响负荷行为；顾客在价格信号下自利优化。

- mechanism_cn：容量占用与充电速率r正相关；当单位电价随r线性增长时，理性agent在满足电量需求的前提下会选择更分散/避开高α时段的充电速率，从而改变聚合负荷形状，避免所有agent集中在最低价时段。

- design_requirement_cn：价格必须是统一的广播信号，但应包含一个与充电速率相关的动态分量；同时不应直接控制充电器，不要求额外行为假设，并能适应任意期望剖面与收入目标。

- artifact_choice_cn：P_t(r)=P0,t+α_t·r；通过α_t做时间维度上的交叉补贴；AH/CH作为α定价器。

- evaluated_contrast_cn：CBP-AH/CH[-Distrib] vs flat pricing、rate-independent variable pricing、increasing-block pricing；在flat/household-complement/PV-following三种期望曲线下比较RMSE/PAPR/peak/revenue。

- objective_result_cn：CBP-CH在三个场景均最低RMSE与接近1的PAPR，并实现目标收入偏差0.08%-0.14%；rate-independent variable pricing引发早高峰雪崩效应；increasing-block仅在平坦场景次优，在波动场景远差。

##### evidence_pointers

1. Theorem 1-4

2. Figure 5-6

3. Step 2a/2b/2c

4. Table 2-5

5. 图12-16

## 评价逻辑

### evaluation_modes

1. 多agent仿真（agent-based simulation）

2. 基准比较（benchmark comparison）

3. 场景敏感性分析（期望曲线类型变化）

4. 稳健性/边界检验（agent能力、预测误差）

5. 理论推导作为评价的一部分

- why_these_evaluations_cn：由于网格运营商的不完全信息和大规模问题使真实最优不可得，作者先用解析定理给出理想情形的最优条件，再用真实数据校准的仿真在异质agent、随机驾驶行为、不同期望曲线和基准下检验制品的grid-balancing与收入表现；多种场景用于证明可诱导任意剖面而非只在平坦剖面有效；稳健性检验排除agent能力与预测误差驱动结论。

- benchmark_and_contrast_chain_cn：Benchmark 1是现状（真实世界平坦电价充电数据）；Benchmark 2是无容量分量的时变价格，用于展示雪崩效应并隔离容量定价的作用；Benchmark 3是非线性递增阶梯电价，代表最强的价格型benchmark。三类基准从简单到复杂递进，CBP则从AH到CH递进；场景从平坦(最简单)、到总负荷平坦(非平坦EV曲线)、到PV跟随(高波动)，难度递增。

### claim_evidence_ledger

#### 1. 1

- technical_claim：CBP能在较少迭代下诱导期望曲线并满足收入目标

- evidence：Table 2-5、附录H，CBP-CH RMSE接近零且收入偏差<0.5%

- supported：仿真证据充分

#### 2. 2

- technical_claim：容量项α·r是性能提升的关键

- evidence：Benchmark 2（rate-independent）在同样动态定价下出现严重雪崩峰值，而CBP显著降低PAPR；定理1/2表明agent充电速率与α_t反比

- supported：对比证据充分，但未做α项逐组消融（如仅时间无关α）

#### 3. 3

- technical_claim：价格信号通过理性成本最小化和反比响应改变充电行为

- evidence：Theorem 1-2推导+仿真结果; Online Appendix E雪崩缓解说明

- supported：解析+仿真联合支持

#### 4. 4

- technical_claim：适用于myopic agent和存在预测误差时

- evidence：Online Appendix J/I

- supported：作者报告保持优势，但具体数据未在主文展示

#### 5. 5

- technical_claim：容量定价可替代迭代学习实现低计算复杂度负载重分配

- evidence：CH只需两三个观测步骤，与需20-100天迭代/深度RL算法形成对照

- supported：对照文献+仿真

#### 6. 6

- technical_claim：扩展非线性定价到负载均衡与Green IS

- evidence：定理1-4给出一般诱导条件和收入条件，讨论将需求跟随可再生与Green IS连接

- supported：解析理论明确

- internal_validity_strategy_cn：统一仿真环境控制外部变量；基准按文献标准实现；使用多种指标（RMSE/PAPR/peak）从不同角度衡量；比较中覆盖真实世界数据基准、无容量分量基准和非线性定价基准，隔离容量定价的作用；使用随机抽样生成异质agent并报告平均表现。

- external_validity_strategy_cn：用荷兰CBS出行数据、EPEX电价、荷兰家庭负荷、威斯康星PV出力等真实数据校准；以Power TAC标准为模板；设置T=168h、δ=1h匹配文献和实践动态合同；通过改变期望剖面类型和agent能力检验可推广性。

- what_is_not_actually_tested_cn：没有真实现场实验或用户行为实验；没有测量真实EV车主对容量定价的实际接受度和响应弹性；没有测试价格长期改变是否会改变驾驶需求/出行行为；没有考虑用户在不同电价套餐间选择的行为；没有检验多电网运营商竞争或控制多段电网时的均衡；收入匹配中的个体需求分布假设在现实中可否获得也未验证。

## 贡献闭环

- technical_claim_cn：提出充电速率依赖的容量定价公式P_t(r)=P0,t+α_t·r，并给出低复杂度AH/CH价格设定方法，可在多agent仿真中诱导期望曲线并接近最优。

- artifact_claim_cn：CBP制品作为IS赋能的充电协调机制，能在不强制控制充电器、无需个体偏好知情、无需大量迭代的情况下，提升grid-balancing和可再生能源跟随。具体地，CBP-CH在所有场景中RMSE最小、PAPR接近1、收入偏差极小。

- mechanism_claim_cn：CBP通过把容量成本附加到充电速率上，使理性agent的最优充电速率与α_t成反比；因此使用同一α广播价格即可分散充电行为、抑制雪崩效应，并可按需形成任意曲线。

- boundary_claim_cn：所声称优势在以下条件内成立：EV agent至少具备一定理性成本最小化；个体驾驶需求和充电可达性不受价格改变；用户均订阅该方案；期望曲线总能量不变；仿真环境校准自荷兰/威斯康星数据。

- reusable_design_knowledge_cn：可复用设计知识包括：(1) 在统一价格信号中嵌入与资源占用率相关的动态价格项可自然分散同质理性响应；(2) 用解析可解无约束情形提供初始可行参数族，再用少量聚合观测做线性调整，可显著降低迭代成本；(3) 设计收入目标选择自由度F可实现价格公平/监管约束；(4) 用真实数据校准的agent仿真可作为智能电网定价制品的评价平台。

- theoretical_contribution_cn：作者将早期非线性/spot定价思想系统化为CBP的闭合形式条件，扩展了IS/Green IS中的需求响应研究，回应了Ketter et al. (2023)关于移动需求响应激励设计的开放问题；用Watson et al. (2010)框架说明eco-equity与eco-effectiveness均被实现。

- how_discussion_closes_intro_gap_cn：讨论开篇重述了引言中的两个缺口（激励不对齐与雪崩效应、文献三大约束），然后逐条声称本文解决了这些约束：不依赖迭代、不假设额外行为特性、可诱导任意剖面，并以贡献(1)-(7)和仿真/理论证据呼应；最后用边界与未来研究避免把结论扩大为普遍现场有效性。

- overclaim_or_unsupported_leaps_cn：潜在跳跃包括：从仿真到实践有效性的推断较大；CH的“线性外推”对极端非线性约束环境未必成立；声称可诱导任意形状的需求曲线，但仅测试了三种剖面；myopic和预测误差结果放在在线附录，主文没有具体数字；没有将CBP与最新深度RL或迭代方法在同一算例做运行时间/迭代次数直接对比；收入目标的精确保证依赖个体需求ε信息，现实中往往只能近似。

## 句级写作动作图谱

### 1. Abstract P1 S1-S2

- order：1

- section：Abstract

- locator：Abstract P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：论述EV能显著降低碳强度，但大规模引入会增加电力需求峰值、威胁电网稳定。

- rhetorical_function_cn：铺垫可持续性与电网稳定性之间的核心矛盾。

- depends_on_cn：无，作为全文现实锚点。

- sets_up_cn：提出需要IS解决的需求协调问题。

- evidence_pointer：Abstract第一段

### 2. Abstract P1 S3-S4

- order：2

- section：Abstract

- locator：Abstract P1 S3-S4

- move_code：LIMITATION

- paraphrase_cn：现有多数协调方法不能保证电网与EV车主目标激励一致，且统一价格信号可能造成雪崩效应形成新峰值。

- rhetorical_function_cn：迅速指出既有方案的根本缺陷。

- depends_on_cn：依赖前一句EV大量引入的现实。

- sets_up_cn：为容量定价制品的引入提供缺口。

- evidence_pointer：Abstract第一段后半

### 3. Abstract P2 S1

- order：3

- section：Abstract

- locator：Abstract P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出包含动态收费率价格成分和基于解析/计算启发式的价格设定方法的容量定价制品。

- rhetorical_function_cn：首次给出核心解决方案。

- depends_on_cn：依赖上一句指出的缺陷。

- sets_up_cn：为摘要后续的性能声明建立对象。

- evidence_pointer：Abstract第二段前句

### 4. Abstract P2 S2-S3

- order：4

- section：Abstract

- locator：Abstract P2 S2-S3

- move_code：REQUIREMENT

- paraphrase_cn：方案利用环境信息，允许理性EV agent在个体充电需求和约束下通过计划与调度优化自身成本，同时重新平衡总充电需求以缓解雪崩效应。

- rhetorical_function_cn：明确机制层面的要求：个体优化与整体平衡共存。

- depends_on_cn：依赖容量定价制品的设计。

- sets_up_cn：解释为何该设计能实现可持续EV引入。

- evidence_pointer：Abstract第二段中后句

### 5. Abstract P3 S1-S2

- order：5

- section：Abstract

- locator：Abstract P3 S1-S2

- move_code：RESULT

- paraphrase_cn：制品在降低需求波动或实现可再生能源与充电需求匹配方面高度有效。

- rhetorical_function_cn：给出高层面实证结果。

- depends_on_cn：依赖前文设计。

- sets_up_cn：后续摘要强调比较基准与利益相关者收益。

- evidence_pointer：Abstract第三段

### 6. Abstract P3 S3

- order：6

- section：Abstract

- locator：Abstract P3 S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：在多个现实场景中与传统当前定价基准进行经验比较，展示收益。

- rhetorical_function_cn：把结果定位为相对现有方法的改进。

- depends_on_cn：依赖已有result。

- sets_up_cn：为摘要贡献结论做准备。

- evidence_pointer：Abstract第三段后半

### 7. Abstract P4-P5

- order：7

- section：Abstract

- locator：Abstract P4-P5

- move_code：CONTRIBUTION

- paraphrase_cn：支持电网运营者跨时间重平衡EV充电需求；使能源供应商在尊重市场约束时维持总收入；使市场利益相关者诱导需求曲线跟随可再生能源，最大化可再生能源利用。

- rhetorical_function_cn：把技术结果转译成利益相关者价值。

- depends_on_cn：依赖前面的设计、结果与基准比较。

- sets_up_cn：突出Green IS和可持续性贡献。

- evidence_pointer：Abstract末段

### 8. Introduction P1 S1-S5

- order：8

- section：Introduction

- locator：Introduction P1 S1-S5

- move_code：CONTEXT

- paraphrase_cn：智能城市数据激增，需要降低碳强度并提升交通可用性，EV因减排潜力而流行，且有全球百万辆目标。

- rhetorical_function_cn：把研究问题嵌入智能城市与气候变化大叙事。

- depends_on_cn：无。

- sets_up_cn：引出现有电网无法承受大规模EV充电的紧张。

- evidence_pointer：Introduction第一段

### 9. Introduction P2 S1-S3

- order：9

- section：Introduction

- locator：Introduction P2 S1-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：当前电网不是为大量EV在晚间峰值充电而设计；EV充电器是家庭最高功率负荷；传统扩容方案极为昂贵且不可持续。

- rhetorical_function_cn：强调电网升级方案的经济与环境不可持续性。

- depends_on_cn：依赖EV大规模增长背景。

- sets_up_cn：说明需要更聪明的需求侧协调而非物理扩容。

- evidence_pointer：Introduction第二段

### 10. Introduction P2 S4-S5

- order：10

- section：Introduction

- locator：Introduction P2 S4-S5

- move_code：LIMITATION

- paraphrase_cn：传统应对方式只有两条：投资电网基础设施，或向车主提供低价以换取高需求期远程关断充电器的许可。

- rhetorical_function_cn：列出当前方案的结构性局限。

- depends_on_cn：依赖上一句电网压力。

- sets_up_cn：引出后来的激励不对齐与雪崩效应问题。

- evidence_pointer：Introduction第二段后句

### 11. Introduction P3 S1-S2

- order：11

- section：Introduction

- locator：Introduction P3 S1-S2

- move_code：PHENOMENON

- paraphrase_cn：现有EV充电协调方案的短板源于无法实现电网与顾客激励一致，常造成雪崩效应——相同价格信号下顾客相似反应导致低价时段拥堵和新峰值。

- rhetorical_function_cn：提出论文要解决的中心现象。

- depends_on_cn：依赖前文传统方案局限。

- sets_up_cn：为容量定价的价格差异化机制做铺垫。

- evidence_pointer：Introduction第三段

### 12. Introduction P3 S3

- order：12

- section：Introduction

- locator：Introduction P3 S3

- move_code：MECHANISM

- paraphrase_cn：雪崩效应来自所有顾客收到相同价格信号后做相似充电决策，把需求集中到低价时段。

- rhetorical_function_cn：解释现象的因果机制。

- depends_on_cn：承接phenomenon定义。

- sets_up_cn：预示解决思路是让价格不再只随时段变化，而随充电速率变化以分散选择。

- evidence_pointer：Introduction第三段后半

### 13. Introduction P4 S1

- order：13

- section：Introduction

- locator：Introduction P4 S1

- move_code：THEORY_INTRO

- paraphrase_cn：电力市场技术演进将其变为智能市场，计算智能可支持人做更明智决策。

- rhetorical_function_cn：召唤IS文献中智能市场决策支持的研究议程。

- depends_on_cn：前面现象需要技术化解决。

- sets_up_cn：将本文制品定位为IS-enabled智能市场方案。

- evidence_pointer：Introduction第四段前句

### 14. Introduction P4 S2-S3

- order：14

- section：Introduction

- locator：Introduction P4 S2-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者回应IS文献呼吁，引入IS赋能的定价方案协调EV充电，使电网压力最小化并最好地利用可再生能源；方案只需单向价格参数通信，且不限制期望需求轮廓形状。

- rhetorical_function_cn：把一般智能市场议程收缩为本文目标。

- depends_on_cn：依赖前面的智能市场理论。

- sets_up_cn：引出容量定价核心设计。

- evidence_pointer：Introduction第四段

### 15. Introduction P4 S4-S7

- order：15

- section：Introduction

- locator：Introduction P4 S4-S7

- move_code：DESIGN_FEATURE

- paraphrase_cn：具体机制是让kWh价格包含随充电速率/kW变化的成分，即容量定价CBP；因为充电速率决定电网容量占用。

- rhetorical_function_cn：首次给出核心设计及其物理/工程依据。

- depends_on_cn：依赖雪崩效应机制与智能市场定位。

- sets_up_cn：后文用α参数与定理系统化该设计。

- evidence_pointer：Introduction第四段中后句

### 16. Introduction P4 S8-S10

- order：16

- section：Introduction

- locator：Introduction P4 S8-S10

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：研究定位为Gregor & Hevner意义上的“Improvement”，目标是克服现有grid-balancing局限，并用真实数据校准的仿真按领域指标评估。

- rhetorical_function_cn：提前声明设计科学定位和评价方式，管理读者预期。

- depends_on_cn：依赖已有制品。

- sets_up_cn：为Section 6的仿真testbed伏笔。

- evidence_pointer：Introduction第四段末

### 17. Introduction P5 S1-S4

- order：17

- section：Introduction

- locator：Introduction P5 S1-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：电网运营者可通过降低需求峰和无中断运行受益；政策制定者可用方案使需求匹配可再生出力，使可再生投资更具成本效益；由此促进EV普及并减少对额外电网容量的需要。

- rhetorical_function_cn：把技术属性转译成多重利益相关者价值。

- depends_on_cn：依赖前文制品与目标。

- sets_up_cn：为Green IS贡献定位铺垫。

- evidence_pointer：Introduction第五段

### 18. Introduction P6 S1-S4

- order：18

- section：Introduction

- locator：Introduction P6 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：贡献指向智能市场/智能城市文献，并置于Green IS；按Green IS原则，IS可借助信息实现更高效能源消耗，本文所设计制品以最小干预和低计算复杂度诱导对电网更有利的EV充电行为。

- rhetorical_function_cn：把贡献正式定位在Green IS。

- depends_on_cn：依赖前面的设计、利益相关者价值。

- sets_up_cn：引入图1的Green IS框架。

- evidence_pointer：Introduction第六段

### 19. Background 2.1 P1-P2

- order：19

- section：Section 2.1

- locator：Background 2.1 P1-P2

- move_code：THEORY_INTRO

- paraphrase_cn：Green IS研究以IT改善环境可持续为核心，本文回应Ketter et al. (2023)关于设计移动需求响应激励的研究机会。

- rhetorical_function_cn：在理论坐标中安置本文，并说明其回答的具体研究问题。

- depends_on_cn：依赖引言Green IS定位。

- sets_up_cn：后文将制品评价格为Green IS affordance。

- evidence_pointer：Section 2.1开头

### 20. Background 2.1 P3-P4

- order：20

- section：Section 2.1

- locator：Background 2.1 P3-P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Green IS中已有EV与可再生协同框架、EV电池再利用决策支持等研究，但未解决充电协调中的激励与雪崩问题。

- rhetorical_function_cn：列举邻近工作，显示本文落点。

- depends_on_cn：依赖Green IS理论定位。

- sets_up_cn：为2.2节更聚焦的充电协调综述过渡。

- evidence_pointer：Section 2.1后部

### 21. Background 2.2 P1-P3

- order：21

- section：Section 2.2

- locator：Background 2.2 P1-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：集中式（top-down）协调通常有全局目标，可管理峰值和电网参数，但需要外生控制充电器，可能侵犯车主偏好并需要通讯控制基础设施。

- rhetorical_function_cn：总结集中式协调的收益与代价。

- depends_on_cn：依赖背景知识铺垫。

- sets_up_cn：反向引出分布式机制及其缺陷。

- evidence_pointer：Section 2.2前几段

### 22. Background 2.2 P4-P5

- order：22

- section：Section 2.2

- locator：Background 2.2 P4-P5

- move_code：LIMITATION

- paraphrase_cn：分布式机制让个体最小化自身成本，能尊重个体偏好，但无法保证个体目标与电网全局目标一致；当它们收到相同价格信号时，充电计划将相关，从而出现雪崩效应。

- rhetorical_function_cn：指出纯分布式协调的关键缺口。

- depends_on_cn：依赖前面对集中式缺点的铺垫。

- sets_up_cn：为本文混合中央协调+分布式决策提供理由。

- evidence_pointer：Section 2.2中后段

### 23. Background 2.2 P6

- order：23

- section：Section 2.2

- locator：Background 2.2 P6

- move_code：GAP

- paraphrase_cn：尽管已有区块链、中介控制、迭代智能充电等尝试，但这些方案计算更复杂或需要更多信息，难以快速适应真实环境。

- rhetorical_function_cn：把已有缓解尝试概括为仍不满足快速适应需求。

- depends_on_cn：依赖前文雪崩效应现象。

- sets_up_cn：引出本文兼具低复杂度和快速适应的混合机制。

- evidence_pointer：Section 2.2末段

### 24. Background 2.3 P2-P4

- order：24

- section：Section 2.3

- locator：Background 2.3 P2-P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：许多现有定价方法依赖迭代学习、强化学习、遗传算法或行为假设来调价，它们通常需要几十到上百次迭代收敛或大量计算资源。

- rhetorical_function_cn：归纳第一类文献的共同局限：迭代/学习成本。

- depends_on_cn：依赖背景综述。

- sets_up_cn：随后将文献缺口归纳为三类。

- evidence_pointer：Section 2.3前三段

### 25. Background 2.3 P5

- order：25

- section：Section 2.3

- locator：Background 2.3 P5

- move_code：LIMITATION

- paraphrase_cn：另一类文献假设EV车主价格响应函数或效用函数，在现实中未必可得，且常只能得到静态或受限的价格。

- rhetorical_function_cn：补充第二类文献的问题：行为假设依赖。

- depends_on_cn：依赖前文综述。

- sets_up_cn：使本文“仅依赖理性成本最小化”的优势更突出。

- evidence_pointer：Section 2.3中段

### 26. Background 2.3 P6-P7

- order：26

- section：Section 2.3

- locator：Background 2.3 P6-P7

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：多种定价结构和locational marginal pricing方法可平衡电网，但大多只面向平坦负荷曲线，难以诱导任意形状剖面。

- rhetorical_function_cn：归纳第三类文献限制：剖面形状受限。

- depends_on_cn：依赖前文综述。

- sets_up_cn：为任意剖面可诱导的design feature提供对照。

- evidence_pointer：Section 2.3末前段

### 27. Background 2.3 P8

- order：27

- section：Section 2.3

- locator：Background 2.3 P8

- move_code：GAP

- paraphrase_cn：现有文献以三种方式限制问题：依赖大量迭代/学习、假设额外消费者行为特征、假设期望剖面平坦或高受限；本文用不同定价制品应对这些限制。

- rhetorical_function_cn：给出精确的三维文献缺口。

- depends_on_cn：依赖前两段的分类。

- sets_up_cn：为容量定价与AH/CH的贡献清单定基准。

- evidence_pointer：Section 2.3末段

### 28. Background 2.3 P9-P10

- order：28

- section：Section 2.3

- locator：Background 2.3 P9-P10

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者的容量定价建立在早期非线性定价思想上，并系统研究其理论性质和价格设定机制，贡献包括解析启发式、计算启发式、内置收入平衡和广泛评价。

- rhetorical_function_cn：以缺口为跳板，预告本文制品。

- depends_on_cn：依赖三类缺口的总结。

- sets_up_cn：为Section 3-7的展开划出路线图。

- evidence_pointer：Section 2.3末段后半

### 29. Section 3 P1-S1

- order：29

- section：Section 3

- locator：Section 3 P1-S1

- move_code：REQUIREMENT

- paraphrase_cn：假设智能电网运营者希望把现有电力需求重塑为任意期望剖面（如平坦或可再生发电模式），这即负载平衡问题。

- rhetorical_function_cn：明确设计的目标函数。

- depends_on_cn：依赖文献缺口。

- sets_up_cn：定义随后的问题参与者与价格信号。

- evidence_pointer：Section 3前段

### 30. Section 3.1 P1-P3

- order：30

- section：Section 3.1

- locator：Section 3.1 P1-P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：网格运营者在T开始时广播覆盖整个计划期的价格，只能观察聚合需求和总充电需求，不能访问个体偏好；期望剖面D需保持总电量Φ不变。

- rhetorical_function_cn：刻画信息边界和决策环境。

- depends_on_cn：依赖Section 3的目标设定。

- sets_up_cn：为3.2的α参数控制作背景。

- evidence_pointer：Section 3.1

### 31. Section 3.2 P1-P2

- order：31

- section：Section 3.2

- locator：Section 3.2 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：广播价格统一但可随时间变化并依赖于消费者选择的充电速率，即P_t(r)=P0,t+α_t·r，其中α_t是斜率/决策变量。

- rhetorical_function_cn：给出核心设计公式。

- depends_on_cn：依赖前面信息边界。

- sets_up_cn：后面定理使用该公式推导agent响应。

- evidence_pointer：Section 3.2，公式(1)

### 32. Section 3.2 P3-P4

- order：32

- section：Section 3.2

- locator：Section 3.2 P3-P4

- move_code：MECHANISM

- paraphrase_cn：充电速率决定所需电网容量；容量项α·r将容量成本转嫁给使用更高速率的顾客，因此相同能量下用更高速率充电的EV将支付更高单位电价。

- rhetorical_function_cn：解释设计背后的机制。

- depends_on_cn：依赖价格公式。

- sets_up_cn：支持Theorem 1中速率与α反比的结果。

- evidence_pointer：Section 3.2中后段

### 33. Section 3.2 P5

- order：33

- section：Section 3.2

- locator：Section 3.2 P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：α_t被定义为控制agent的决策变量，目标是为每个t选择向量α以诱导期望聚合充电剖面。

- rhetorical_function_cn：把参数上升到控制变量。

- depends_on_cn：依赖价格公式。

- sets_up_cn：引出第4节最优α条件。

- evidence_pointer：Section 3.2末尾

### 34. Section 3.3 P1-P4

- order：34

- section：Section 3.3

- locator：Section 3.3 P1-P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：定义EV agent的偏好集合、驾驶截止时间、所需电量、充电可用性和驾驶耗电，并给出成本最小化问题及两个约束。

- rhetorical_function_cn：建立agent决策模型，供后续仿真使用。

- depends_on_cn：依赖价格广播设定。

- sets_up_cn：后面定理和仿真用此模型求解最优充电率。

- evidence_pointer：Section 3.3，公式(2)-(6)

### 35. Section 3.4 P1

- order：35

- section：Section 3.4

- locator：Section 3.4 P1

- move_code：LIMITATION

- paraphrase_cn：网格管理者理想的个体偏好知情和精确优化因信息不可得和大规模计算棘手而不可行，因此必须使用启发式。

- rhetorical_function_cn：明确为什么转向近似方法。

- depends_on_cn：依赖3.3的agent复杂度。

- sets_up_cn：为Section 4/5的AH和CH提供合法性。

- evidence_pointer：Section 3.4第1段

### 36. Section 3.4 P2-P3

- order：36

- section：Section 3.4

- locator：Section 3.4 P2-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者说明可观察信息（I、聚合需求、总能量）以及由文献标准设定的行为假设；评价将在随机异质环境中进行以建立有效性。

- rhetorical_function_cn：界定信息假设和评价标准。

- depends_on_cn：依赖不完全信息论证。

- sets_up_cn：让随后heuristic的设计和仿真评价有明确前提。

- evidence_pointer：Section 3.4后段

### 37. Section 4 P1-P3

- order：37

- section：Section 4

- locator：Section 4 P1-P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：在无充电可用性约束情况下，最优定价任务可直接解析处理，理论性质直接导致可诱导期望剖面的解析启发式，因而在无约束情形最优且自然用于约束不可观察的情形。

- rhetorical_function_cn：建立Section 4的理论地位。

- depends_on_cn：依赖3.4的启发式必要性。

- sets_up_cn：为定理1-4铺路。

- evidence_pointer：Section 4前3段

### 38. Section 4.1 Theorem 1

- order：38

- section：Section 4.1

- locator：Section 4.1 Theorem 1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：定理1：在容量定价下，理性无约束agent的最优充电率r_t^*与α_t成反比，取决于总需求、时段长度和α的调和形式。

- rhetorical_function_cn：提供agent对容量定价的解析最优响应。

- depends_on_cn：依赖价格公式与agent模型。

- sets_up_cn：用于解释图5-6并引出α控制需求形状。

- evidence_pointer：Theorem 1

### 39. Section 4.1 图5-6后

- order：39

- section：Section 4.1

- locator：Section 4.1 图5-6后

- move_code：MECHANISM

- paraphrase_cn：由于最优充电率取决于α_t，网格运营者可通过调整α_t改变图6中需求的形状。

- rhetorical_function_cn：把定理结果转化为控制机制描述。

- depends_on_cn：依赖Theorem 1。

- sets_up_cn：引出4.2节最优α条件。

- evidence_pointer：Figure 5-6附近的讨论

### 40. Section 4.2 Theorem 2

- order：40

- section：Section 4.2

- locator：Section 4.2 Theorem 2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：定理2：在异质理性无约束agent群体中，若要使容量定价诱导期望剖面D，则α_t·D_t/δ在所有t应相等；该条件不需要个体充电需求精确或分布信息，并给出单自由度F的D-inducing alpha族。

- rhetorical_function_cn：给出可执行的最优价格设置条件。

- depends_on_cn：依赖Theorem 1。

- sets_up_cn：为Revenue定理3/4和CH初始化建立基础。

- evidence_pointer：Theorem 2及其讨论

### 41. Section 4.3 Theorem 3

- order：41

- section：Section 4.3

- locator：Section 4.3 Theorem 3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：定理3：要从D-inducing族中选择生成目标收入的α，应按给定公式根据Ψ*, P0, Φ和个体需求份额的平方和设定α_z。

- rhetorical_function_cn：将自由度F绑定到收入目标。

- depends_on_cn：依赖Theorem 2的解族。

- sets_up_cn：支撑收入等价与应用推论A.5/A.6。

- evidence_pointer：Theorem 3

### 42. Section 4.3 Theorem 4

- order：42

- section：Section 4.3

- locator：Section 4.3 Theorem 4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：定理4：即使在个体约束下实际观测剖面D^o偏离期望，网格运营者仍可从同一诱导族调整α以满足收入目标，前提是需知晓个体需求份额信息或使用其近似。

- rhetorical_function_cn：把收入保证扩展到带私有约束现实。

- depends_on_cn：依赖Theorem 3和D-inducing族性质。

- sets_up_cn：为CH的Step2b/2c提供依据。

- evidence_pointer：Theorem 4

### 43. Section 5 P1

- order：43

- section：Section 5

- locator：Section 5 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：在更复杂、可观察部分聚合约束的场景中，作者提出计算启发式：初始化为解析启发式，再通过观察聚合充电行为调整价格参数，无需大量迭代和计算。

- rhetorical_function_cn：介绍CH的定位与总体思路。

- depends_on_cn：依赖Theorem 2-4。

- sets_up_cn：后文逐步给出算法步骤。

- evidence_pointer：Section 5开头

### 44. Step 1

- order：44

- section：Section 5

- locator：Step 1

- move_code：DESIGN_FEATURE

- paraphrase_cn：用AH和定理3/4的推论根据目标收入选择初始α^0。

- rhetorical_function_cn：保证起点在无约束情形下已经最优。

- depends_on_cn：依赖Theorem 3/4。

- sets_up_cn：作为数据驱动调整的基准。

- evidence_pointer：CH Step 1

### 45. Step 2a

- order：45

- section：Section 5

- locator：Step 2a

- move_code：DESIGN_FEATURE

- paraphrase_cn：利用观测到的需求偏差w_t = D_t^o/D_t，将α_t^1设为α_t^0·w_t，以逼近期望剖面；该调整从D诱导族转换到D=w诱导族，继承解析性质。

- rhetorical_function_cn：说明第一次数据驱动调整的公式和理论性质。

- depends_on_cn：依赖Theorem 2家族思想。

- sets_up_cn：随后Step2b/2c用收入观测继续微调。

- evidence_pointer：CH Step 2a

### 46. Step 2b-2c

- order：46

- section：Section 5

- locator：Step 2b-2c

- move_code：DESIGN_FEATURE

- paraphrase_cn：根据观察到收入后，用定理4推论选α^2调整收入；若仍不充分，利用两点拟合F=f(Ψ)线性函数外推目标收入对应的F*。

- rhetorical_function_cn：完成CH对目标收入的低复杂度匹配。

- depends_on_cn：依赖Step2a产生的D=w诱导族以及收入观测。

- sets_up_cn：为后续仿真的CH配置提供算法细节。

- evidence_pointer：CH Step 2b/2c

### 47. Section 6 P1

- order：47

- section：Section 6

- locator：Section 6 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为了评估制品，作者构建基于Power TAC规范的智能市场多agent仿真，模拟理性EV agent与网格控制agent，使用真实世界驾驶行为数据初始化。

- rhetorical_function_cn：把评价方法锚定到既有仿真标准。

- depends_on_cn：依赖Section 3.3的agent模型。

- sets_up_cn：引入仿真步骤、指标、数据和基准。

- evidence_pointer：Section 6引言

### 48. Section 6.2 P1-P3

- order：48

- section：Section 6.2

- locator：Section 6.2 P1-P3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：采用RMSE度量匹配度，使用绝对峰值和峰值-平均功率比PAPR作为领域中表示电压波动和峰值的指标，仅在期望曲线平坦时计算后两者。

- rhetorical_function_cn：定义成功标准。

- depends_on_cn：依赖仿真平台。

- sets_up_cn：后续表2-5都用这些指标报告。

- evidence_pointer：Section 6.2

### 49. Section 6.3 P1-P3

- order：49

- section：Section 6.3

- locator：Section 6.3 P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用荷兰CBS出行数据、EPEX批发电价加税费形成的零售价、荷兰家庭负荷和PV出力校准仿真；使agent偏好和期望剖面来自真实世界。

- rhetorical_function_cn：建立外部有效性。

- depends_on_cn：依赖仿真平台。

- sets_up_cn：为7.1-7.3中结果的可信性提供基础。

- evidence_pointer：Section 6.3各小节

### 50. Section 6.4 P1-P3

- order：50

- section：Section 6.4

- locator：Section 6.4 P1-P3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：基准包括真实世界平坦电价充电数据、无容量项的可变价格（按残余容量反向设置）、以及递增阶梯电价（按Borenstein并适配期望剖面）。

- rhetorical_function_cn：建立评价参照系，从现状到动态无容量项再到非线性定价。

- depends_on_cn：依赖指标定义。

- sets_up_cn：为后续“CBP优于基准”的结论提供对比项。

- evidence_pointer：Section 6.4

### 51. Section 6.5 Table 1

- order：51

- section：Section 6.5

- locator：Section 6.5 Table 1

- move_code：DESIGN_FEATURE

- paraphrase_cn：按充电可用性假设（无约束AH vs 带约束CH）和个体需求信息版本（Minimal vs Distributional）形成2x2配置：CBP-AH、CBP-AH-Distrib、CBP-CH、CBP-CH-Distrib。

- rhetorical_function_cn：明确评价对象的具体实例。

- depends_on_cn：依赖Section 4-5的两个启发式。

- sets_up_cn：为7.1-7.3的结果表和配置标签提供依据。

- evidence_pointer：Table 1

### 52. Section 7 P1-P3

- order：52

- section：Section 7

- locator：Section 7 P1-P3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：评价采用T=168小时、δ=1小时；依次考察平坦、家庭负荷互补、PV跟随三种不同波动性的期望剖面，并同时考察需求与收入目标。

- rhetorical_function_cn：预告评价场景的递进结构。

- depends_on_cn：依赖仿真平台和配置。

- sets_up_cn：分开三节报告结果。

- evidence_pointer：Section 7开头

### 53. Section 7.1 结果段与表2-3

- order：53

- section：Section 7.1

- locator：Section 7.1 结果段与表2-3

- move_code：RESULT

- paraphrase_cn：在平坦场景中，CBP-CH达到近最优RMSE 0.02 MWh、PAPR 1.07、峰值1.03 MWh；收入偏差最小0.08%，且分布信息版本优于minimal版本；benchmark无法同时满足收入目标。

- rhetorical_function_cn：给出第一个核心证据：CBP同时达成需求曲线与收入目标。

- depends_on_cn：依赖配置与仿真平台。

- sets_up_cn：支撑后续任意剖面和收入平衡主张。

- evidence_pointer：Figure 12, Table 2, Table 3

### 54. Section 7.1 末段

- order：54

- section：Section 7.1

- locator：Section 7.1 末段

- move_code：CONTRIBUTION

- paraphrase_cn：与benchmark相比，本文方法不仅能优化grid balancing，还能满足收入等价目标，这是benchmark设计中没有的能力。

- rhetorical_function_cn：把结果转译为相对基准的功能差异。

- depends_on_cn：依赖表3收入结果。

- sets_up_cn：在讨论中作为贡献(4)出现。

- evidence_pointer：Section 7.1最后两段

### 55. Section 7.2 结果段

- order：55

- section：Section 7.2

- locator：Section 7.2 结果段

- move_code：RESULT

- paraphrase_cn：在家庭负荷互补场景，CBP配置仍最佳，CBP-CH RMSE 0.03 MWh、PAPR 1.06、峰值2.69 MWh；无容量项的可变价格造成约8.5 MWh清晨高峰，显示雪崩效应。

- rhetorical_function_cn：证明CBP在非平坦EV曲线任务中有效，并实证雪崩效应。

- depends_on_cn：依赖平台和基准。

- sets_up_cn：支持可诱导任意剖面与抑制雪崩的贡献。

- evidence_pointer：Figure 14-15, Table 4

### 56. Section 7.3 结果段

- order：56

- section：Section 7.3

- locator：Section 7.3 结果段

- move_code：RESULT

- paraphrase_cn：在跟随PV出力场景中，CBP-AH RMSE 0.83 MWh，CBP-CH RMSE 0.21 MWh，而递增阶梯基准RMSE 4.65 MWh，说明CBP能处理高波动剖面。

- rhetorical_function_cn：把有效性扩展到可再生能源匹配。

- depends_on_cn：依赖平台和PV数据。

- sets_up_cn：为Green IS可持续贡献提供直接证据。

- evidence_pointer：Figure 16, Table 5

### 57. Section 7.4 + Online Appendices I/J

- order：57

- section：Section 7.4

- locator：Section 7.4 + Online Appendices I/J

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：即使EV agent更近视/更少规划，或期望剖面包含预测误差，CBP在所有测试场景中仍保持对基准的优越性能。

- rhetorical_function_cn：排除结果对agent能力和完美预测的依赖。

- depends_on_cn：依赖三个主场景结果。

- sets_up_cn：为讨论中的可推广性主张提供边界。

- evidence_pointer：Section 7.4与Online Appendices I/J

### 58. Section 8 P1-P3

- order：58

- section：Section 8

- locator：Section 8 P1-P3

- move_code：CONTRIBUTION

- paraphrase_cn：文章总结：新型容量定价制品结合分布式自利决策与中央协调，可诱导任意形状需求曲线，包括匹配可再生发电，是Green IS的重要应用，实现eco-equity与eco-effectiveness。

- rhetorical_function_cn：返回引言缺口，把仿真结果上升为Green IS理论贡献。

- depends_on_cn：依赖全部结果。

- sets_up_cn：后文逐条列出七个具体贡献。

- evidence_pointer：Section 8前段

### 59. Section 8 贡献列表(1)-(7)

- order：59

- section：Section 8

- locator：Section 8 贡献列表(1)-(7)

- move_code：CONTRIBUTION

- paraphrase_cn：具体贡献包括：新定价制品、解析启发式、计算启发式、收入平衡能力、接近最优的任意剖面诱导、突破文献限制、广泛真实场景评价。

- rhetorical_function_cn：使贡献高度清单化，便于审稿人与读者快速核对。

- depends_on_cn：依赖结果和理论推导。

- sets_up_cn：为实践意义和未来研究段作铺垫。

- evidence_pointer：Section 8贡献(1)-(7)

### 60. Section 8 实践意义段

- order：60

- section：Section 8

- locator：Section 8 实践意义段

- move_code：PRACTICAL_STAKES

- paraphrase_cn：电网运营者可重塑需求、能源供应商可管理峰值和容量成本、城市交通规划者可促进可持续EV采纳、公用事业可维持需求与收入目标、EV司机受益于低停电风险和绿色电价。

- rhetorical_function_cn：把贡献向多个利益相关者扩展。

- depends_on_cn：依赖贡献列表。

- sets_up_cn：最后转向边界与未来研究。

- evidence_pointer：Section 8实践意义段

### 61. Section 8 未来研究段

- order：61

- section：Section 8

- locator：Section 8 未来研究段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者指出分析假设价格不改变私人驾驶需求和充电可用性；未来可研究极端价格对行为的影响、多套餐选择以及更细粒度IoT信息。

- rhetorical_function_cn：划定适用范围并给出后续路径。

- depends_on_cn：依赖贡献和评价边界。

- sets_up_cn：结束全文并保护贡献不过度外推。

- evidence_pointer：Section 8末段

## 写作技术

- gap_construction_cn：先在引言用雪崩效应与基础设施成本建立现实危机，然后在2.2用集中式/分布式两分法暴露各自短板，最后在2.3用三大约束（迭代、行为假设、曲线受限）把文献缺口精确化，使CBP的设计空间不是‘没有人做过’，而是‘现有方法以牺牲快速适应、通用剖面和隐私信息为代价’。

- signposting_cn：多处使用‘first/second/third’和‘as a result/we observe/goals’；在Section 3.4用‘Context and Scope’预告Section 4-7；在Section 7开头总述评估目标；在Section 8列出(1)-(7)贡献；附录编号被多次提前引用以建立完整感。

- transition_logic_cn：每个主要部分以现状问题结尾转入下一部分：2.3最后总结缺口并预告CBP；3.4点明不完全信息和计算困难→需要heuristics→Section4解析、Section5计算；7.1平坦→7.2非平坦→7.3高波动，难度递增；7.4→边界；8回到Green IS。

- claim_evidence_rhythm_cn：先在定理中给闭合条件，再在仿真中给表/图数字；每个场景先画曲线/表格，再解释benchmark为何差、CBP为何好；讨论处再把这些数字提升为设计知识和理论贡献。

- benchmark_narrative_cn：benchmark不是随意选取：flat pricing代表现状、rate-independent variable pricing代表无容量项时的对照并展示雪崩效应、increasing-block代表最优非线性pricing对照；每个benchmark的缺陷都被用来突出CBP的对应特征（公平性、低计算、任意剖面）。

- theory_return_cn：结果被重新解释为Green IS框架中的eco-equity（grid balancing）与eco-effectiveness（renewables integration），并回接到Ketter et al. (2023)研究议程；定理的普适性被用于说明这不是一次性机制。

- contribution_positioning_cn：摘要、引言和讨论三处都有贡献清单；作者把贡献放在‘IS-enabled artifact’而非纯算法或纯经济机制层面，既回应smart markets文献又回应Green IS；用Gregor & Hevner Improvement类别预先定位expected contribution。

- novelty_protection_cn：用封闭形式定理证明CBP在理想情形成立，用多种场景展示arbitrary profile灵活性；收入目标能力使制品在不同监管环境下可复用；快速适应/低迭代与文献中需长时间学习的机制形成鲜明对比；最后用稳健性检验保护结论不依赖理想agent假设。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：先建立现实问题与利害关系

- research_job_cn：收集EV/电网/政策数据，确定具体行业痛点

- required_evidence_cn：能展示大规模EV会加剧电网峰值或增加基础设施成本的证据

- transition_to_next_cn：指出当前方案在成本/激励/市场信号上的不足

#### 2. 2

- step：2

- writing_job_cn：文献系统归类并制造精确缺口

- research_job_cn：系统检索定价/协调文献，提取每类的适用条件与失败模式

- required_evidence_cn：能归纳出现有方法的三类共同限制或尚不能实现的功能

- transition_to_next_cn：将缺口表述为可由信息制品解决的设计空间

#### 3. 3

- step：3

- writing_job_cn：将知识基础转化为制品机制

- research_job_cn：形式化问题：目标函数、约束、信息集合、控制变量

- required_evidence_cn：能给出一种新价格形式与至少一个可控参数

- transition_to_next_cn：用可控参数推导理想条件下诱导目标剖面的条件

#### 4. 4

- step：4

- writing_job_cn：理想情形推导闭合条件并形成初始启发式

- research_job_cn：证明最优响应、诱导条件、目标收入条件

- required_evidence_cn：解析公式或闭合条件，并说明不需要个体偏好信息

- transition_to_next_cn：将解析解作为初始值，再考虑真实约束的调整步骤

#### 5. 5

- step：5

- writing_job_cn：用可观测信息设计计算调整步骤

- research_job_cn：基于聚合观测数据设计低复杂度修正/学习步骤

- required_evidence_cn：调整后有收敛或近最优的论证，或至少实例验证

- transition_to_next_cn：搭建评价平台以检验制品

#### 6. 6

- step：6

- writing_job_cn：用真实数据搭建与基准对比的评价环境

- research_job_cn：获取/校准真实数据；实现基准方法

- required_evidence_cn：模拟器参数和benchmark与文献可比

- transition_to_next_cn：逐步增加场景难度展示外部有效性

#### 7. 7

- step：7

- writing_job_cn：多场景评价+稳健性边界

- research_job_cn：运行多个期望剖面；扰动agent能力、预测误差

- required_evidence_cn：至少两个场景优于基准，且主要结论在稳健性检验中保持

- transition_to_next_cn：把结果回接到初始理论/框架并声明边界

#### 8. 8

- step：8

- writing_job_cn：讨论贡献、边界与未来

- research_job_cn：识别从仿真到实践的距离、未处理行为反馈/套餐选择

- required_evidence_cn：贡献与前面证据对应，不越过仿真边界

- transition_to_next_cn：结束，同时为后续研究留口

### most_transferable_moves_cn

1. 用三类基准递进隔离关键设计分量：现状/无关键分量/最强同类方法，从而支持制品主张

2. 解析可解情形作为初始条件，再设计数据驱动调整，使理论结果与实际启发式形成连接

3. 每个评价场景都有明确难度递进：平坦→互补→高波动，支撑任意剖面设计主张

4. 用家庭负荷+EV充电的总曲线而非仅EV曲线，提升现实相关性和可持续性叙事

5. 在开始评价前给出可观察信息集合与不可观察信息边界，诚实地限定知识基础

### resource_intensive_or_nonstandard_parts_cn

1. 荷兰CBS出行分布、EPEX电价、1,500充电桩真实交易数据、Power TAC平台需要专门数据与领域知识

2. 基于文献参数化increasing-block pricing等benchmarks需要做多次校准，包含较多领域判断

3. 定理1-4及一般情形证明/附录C/D需要较强的数学推导能力，较难照搬

4. PV数据来自美国特定地区且只有三个月，需要另行获取才会具有对应代表性

5. 大规模EV agent的仿真和每agent最优化问题需要可扩展求解器支持

### what_not_to_copy_superficially_cn

1. 不能只写‘引入按速率的动态价格’而不给出α参数设定/收入调整的具体条件，否则容易退化为一般动态定价

2. 不能宣称‘任意需求曲线’而只测试平坦场景；至少需包含一个非平坦或高波动场景

3. 不能在一个仿真平台上随意得到near-optimal结论，必须有可复现的数据来源、随机种子/置信区间和基准实现方式

4. 不能把‘实验结果’直接写成‘真实市场会这样’；需讨论行为反馈、套餐选择、长期需求变化的边界

5. 不能只复制Green IS套话；需要把结果与具体affordance（peak mitigation, renewable following）一一映射

- single_best_description_of_the_routine_cn：用一个资源占用相关的动态价格组件把自由市场自利行为转化为中央协调的柔性控制，先用解析解找到理想参数族，再用聚合数据小步调整，最后在难度递进的真实数据仿真中证明其比现状、无该组件版本和最强替代方案都更接近期望曲线且不损失收入。

## 分析边界

基于全文可读文本分析；无精确页码，定位采用章节/段/表/图；部分稳健性结果位于在线附录I/J，主文只给出结论而未提供数字，因此对myopic/预测误差的分析基于作者叙述而非具体表；无法确认在线附录完整内容。
