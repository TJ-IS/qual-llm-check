# The crowd against the few: Measuring the impact of expert recommendations

- 作者：Nils Herm-Stapelberg; Franz Rothlauf
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113345
- 源文件：13538_2020_the-crowd-against-the-few-measuring-the-impact-of-expert-recommendations.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.78

## 文章级论证概况

- 核心问题：在真实视频点播平台上，向现有推荐系统加入由雇佣专家提供的推荐，是否以及在多大程度上改变用户的观看行为、感知和推荐属性？

- 制品与设计：一个被改造的商业视频推荐系统：在原有朴素贝叶斯内容推荐、用户协同过滤、加权余弦内容相似、项目协同过滤和关键词推荐的基础上，加入在职专家按类别手工维护的推荐列表；专家为每个类别挑选至少20个剪辑并每日多次更新；系统将专家推荐与系统推荐随机混合，约一半位置为专家推荐，并在在线随机对照实验中构成治疗组。

- 客观结果：治疗组相对对照组：观看剪辑+9.84%、推荐点击+17.1%、总访问+8.95%、活跃访问+13.80%、多剪辑访问+15.65%、回访率+7%、留存率+14.99%；专家推荐在剪辑页被点击显著少于期望（AS=-0.077，p<0.01），着陆页略低但不显著；治疗组推荐列表ILS更低（更多样），味觉覆盖TC和URC略高，感知满意度无差异。

- 核心贡献：首次用大规模在线随机对照实验证明，向真实推荐系统加入在职专家推荐可以显著提高平台使用，尽管专家推荐本身被点击较少且成功度较低；这为“仅准确率不够”提供了在线证据，并将专家推荐的好处与多样性和味觉覆盖联系起来。

- 整篇论证链：在线内容过载使推荐系统必要，但主流算法只优化准确率并可能造成过滤气泡；离线文献显示专家推荐能提高兴趣覆盖和多样性，却缺少对真实用户行为的在线研究。作者在大型电视网视频点播平台改造商用推荐系统，让治疗组同时看到系统推荐和专家列表推荐，对照组只看到系统推荐，开展10周在线RCT。行为数据显示治疗组在观看、访问、推荐使用和留存等指标上更高；算法成功分解却显示专家推荐本身被点击少于期望，构成反直觉的悖论。作者随后分析推荐属性，发现专家推荐使推荐列表更多样、味觉覆盖略高，而满意度不变，因此将平台使用上升的可能解释指向多样化，但明确承认不能做因果推断。讨论回到“准确率不够”和过滤气泡议题，提出下一步直接控制多样性的实验。

## 类型与写作弧线判定

- 论文主类型判定：论文在真实商业视频点播平台上对现有推荐系统进行操纵，随机分配治疗组（加入专家推荐）和控制组（仅系统推荐），通过点击流和问卷观察用户行为、感知和推荐属性，属于现场平台实验而非离线benchmark或纯设计科学研究。

- 主导写作弧线判定：论文从“过滤气泡/专家推荐的离线好处”这一现象和已有机制出发，构造数字干预（加入专家推荐），用现场RCT产生因果证据，发现反直觉结果后转向属性分析以寻找潜在机制，并在结论中提出未来直接控制多样性的机制检验。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：阶段1建立实验干预：改造真实平台并接入专家推荐；阶段2招募真实用户并随机分配，采集行为与问卷数据；阶段3对比治疗/控制的用户行为，建立总体效应；阶段4分解各推荐算法的点击成功度，揭示专家推荐个体表现不佳；阶段5用条件概率分析点击后续行为，进一步确认悖论；阶段6分析推荐属性（多样性、满意度、覆盖率），为总体效应提供解释证据。各阶段依次回答“干预如何构造—数据是否有效—是否有效果—谁被点击—点击后行为如何—属性能否解释”。

### studies_or_phases

#### 1. 实验系统设计与干预实现

- order：1

- name_cn：实验系统设计与干预实现

- question_cn：如何将雇佣专家的知识转化为可嵌入现有商业推荐系统的干预？

- inputs_and_setting_cn：大型电视网运营的视频点播平台，月访问超一百万，内容超十万；平台现有朴素贝叶斯、用户协同、内容相似、项目协同和关键词推荐；在职内容专家数名。

- designed_or_compared_object_cn：专家按类别手工维护推荐列表，每类至少20个剪辑，每日多次更新；将专家推荐随机混入着陆页和剪辑页，约半数为专家推荐；治疗组显示专家+系统推荐，控制组只显示系统推荐。

- baseline_control_or_counterfactual_cn：控制组为不加入任何专家推荐的原有系统推荐组合。

##### objective_metrics

（空）

- analysis_method_cn：系统改造和专家清单设计，非实证统计。

- main_result_cn：形成了治疗组与控制组之间唯一差异为是否含专家推荐的在线实验环境。

- argumentative_role_cn：为在线RCT提供可操纵的干预和因果对比基础。

- remaining_uncertainty_cn：尚未知道该干预对真实用户行为是否有影响。

- link_to_next_phase_cn：该实验环境需要招募真实用户并采集数据，才能进入行为评价。

##### evidence_pointers

1. Section 3.1 landing page recommendations

2. Section 3.2 clip page recommendations

3. Section 3.3 randomization description

#### 2. 参与者招募、随机分配与数据采集

- order：2

- name_cn：参与者招募、随机分配与数据采集

- question_cn：如何在减少选择、需求和冷启动偏差的前提下获得有效行为数据？

- inputs_and_setting_cn：平台正常访问者通过弹窗自愿注册；6374人注册，清理后2715人；10周点击流共617194次交互；问卷3560份，有效2209份。

- designed_or_compared_object_cn：用户被随机分配到治疗组或控制组；两组推荐界面除专家推荐外完全相同；用户不知道具体测试内容和组别。

- baseline_control_or_counterfactual_cn：控制组仅系统推荐；使用注册后两周数据排除新奇/发现和冷启动效应。

##### objective_metrics

1. 最终有效用户数2715

2. 点击流交互数617194

3. 剪辑点击87357

4. 推荐点击7270

5. 有效问卷2209

- analysis_method_cn：注册弹窗、随机分配、无激励、盲实验、两周预热、数据清洗与描述统计。

- main_result_cn：获得了异质性用户样本和干净的10周行为数据，样本年龄、性别和地域分布较广。

- argumentative_role_cn：为后续所有统计比较提供有效的随机化数据和样本量。

- remaining_uncertainty_cn：尚未分析治疗组与控制组在行为上的差异。

- link_to_next_phase_cn：数据就绪后进入主行为分析。

##### evidence_pointers

1. Section 3.3 Data collection

2. Table 2 age distribution

3. Table 3 gender distribution

#### 3. 用户行为组间比较

- order：3

- name_cn：用户行为组间比较

- question_cn：收到专家推荐是否会改变用户的实际平台使用行为？

- inputs_and_setting_cn：2715名用户的10周点击流数据。

- designed_or_compared_object_cn：治疗组（专家+系统推荐）vs 控制组（仅系统推荐）。

- baseline_control_or_counterfactual_cn：控制组作为反事实，表示不加入专家推荐的情况。

##### objective_metrics

1. Clips Watched

2. Rec. Clicks

3. Total Visits

4. Active Visits

5. Multiclip Visits

6. Return Rate

7. Retain Rate

- analysis_method_cn：非参数Mann-Whitney U检验；留存率为二元结果用Fisher精确检验。

- main_result_cn：治疗组观看剪辑33.70 vs 30.68（+9.84%, p=0.045），推荐点击5.41 vs 4.62（+17.10%, p<0.01），总访问、活跃访问、多剪辑访问、回访率和留存率均高于控制组，部分指标显著性水平在0.05至0.1。

- argumentative_role_cn：建立专家推荐对平台使用的总体因果效应。

- remaining_uncertainty_cn：不知道是哪类推荐驱动了效果，也不清楚为什么专家推荐本身可能不成功。

- link_to_next_phase_cn：需要分解不同推荐算法的点击表现，于是进入算法成功分析。

##### evidence_pointers

1. Section 4.1 User behavior

2. Table 4 Group comparisons

#### 4. 算法成功分解

- order：4

- name_cn：算法成功分解

- question_cn：专家推荐与各类系统推荐相比，是否被点击得更多或更少？

- inputs_and_setting_cn：治疗组中按推荐类型显示的推荐数量和点击数量，区分着陆页和剪辑页。

- designed_or_compared_object_cn：推荐类型包括专家（EX）、内容相似（CSM）、项目协同（ICB）、关键词（KEY）、用户协同（UCB）、朴素贝叶斯（NB）；以显示份额为期望点击概率。

- baseline_control_or_counterfactual_cn：算法成功AS定义为实际点击份额减期望显示份额，0表示与期望相同。

##### objective_metrics

1. Algorithm Success (AS)

2. Relative Difference

3. Significance

- analysis_method_cn：计算期望点击份额和实际点击份额的差，并进行显著性检验。

- main_result_cn：剪辑页内容相似推荐显著高于期望（AS=+0.070），专家推荐显著低于期望（AS=-0.077, p<0.01）；着陆页专家推荐略低但不显著（p=0.13），用户协同推荐显著更高。

- argumentative_role_cn：揭示专家推荐个体吸引力弱，制造“总体效果上升但专家推荐失败”的悖论。

- remaining_uncertainty_cn：仍无法解释为何治疗组总体使用更高。

- link_to_next_phase_cn：需要分析点击推荐后是否继续点击，即推荐成功度。

##### evidence_pointers

1. Section 4.2 Algorithm success

2. Fig. 1

3. Table 5 Algorithm success

#### 5. 推荐点击后续行为分析

- order：5

- name_cn：推荐点击后续行为分析

- question_cn：用户点击一个专家推荐后，是否更可能继续点击其他推荐？

- inputs_and_setting_cn：治疗组和控制组中至少点击过一次推荐的用户。

- designed_or_compared_object_cn：比较三个概率：治疗组任意推荐点击后继续点击的概率P_all_treatment、治疗组专家推荐点击后继续点击的概率P_expert_treatment、控制组系统推荐点击后继续点击的概率P_all_control。

- baseline_control_or_counterfactual_cn：P_all_control作为无专家暴露的基准；P_all_treatment作为治疗组整体基准。

##### objective_metrics

1. P_all_treatment

2. P_expert_treatment

3. P_all_control

4. Mann-Whitney U显著性

- analysis_method_cn：条件概率计算与组间显著性检验。

- main_result_cn：P_expert_treatment=17.2%，低于P_all_treatment=31.5%；P_all_control=14.6%，甚至更低；差异显著。

- argumentative_role_cn：表明点击专家推荐会降低继续点击概率，但完全不接触专家推荐的控制组继续点击概率更低，说明专家推荐暴露有整体收益。

- remaining_uncertainty_cn：行为收益仍不能由“点击专家推荐”本身解释，需要转向推荐属性。

- link_to_next_phase_cn：进入推荐属性分析，寻找多样性和覆盖等可能解释。

##### evidence_pointers

1. Section 4.3 Success of recommendations

2. Table 6 probabilities

#### 6. 推荐属性分析

- order：6

- name_cn：推荐属性分析

- question_cn：专家推荐与系统推荐在多样性、感知满意度和覆盖上是否存在差异？

- inputs_and_setting_cn：展示给用户的推荐列表、点击行为数据，以及实验后问卷。

- designed_or_compared_object_cn：治疗组vs控制组的推荐列表属性；用ILS衡量多样性，用问卷衡量感知满意度，用TC和URC衡量味觉覆盖与独特推荐使用。

- baseline_control_or_counterfactual_cn：控制组推荐列表和满意度作为基准。

##### objective_metrics

1. Intra-list Similarity (ILS)

2. Perceived Satisfaction

3. Taste Coverage (TC)

4. Unique Recommendation Clicks (URC)

- analysis_method_cn：组间比较；问卷部分先做CFA验证效度。

- main_result_cn：治疗组ILS更低（0.578 vs 0.598, p=0.03），推荐更多样；满意度无差异（3.43 vs 3.42）；TC略高（0.258 vs 0.25, p<0.1），URC显著更高（0.161 vs 0.156, p<0.01）。

- argumentative_role_cn：为总体效应提供潜在机制证据：多样性和覆盖提高可能解释平台使用上升，但作者明确承认不能因果推断。

- remaining_uncertainty_cn：多样性是否真正导致使用上升仍未被直接操纵检验。

- link_to_next_phase_cn：结论提出未来直接控制多样性的在线实验。

##### evidence_pointers

1. Section 5.1 Diversity Table 7

2. Section 5.2 Perceived satisfaction

3. Section 5.3 Coverage

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 离线准确率导向及其过滤气泡风险

2. LIMITATION: 离线专家研究未覆盖真实用户行为

3. RQ_OR_OBJECTIVE: 在线RCT检验专家推荐影响

4. RESULT: 平台使用上升但专家推荐自身点击少

5. RESULT: 专家推荐更多样、覆盖更好、满意度不变

6. CONTRIBUTION: 对真实世界推荐系统设计有启示

### introduction_moves

1. CONTEXT: 内容过载与推荐系统必要性

2. PRIOR_KNOWLEDGE: 内容过滤与协同过滤

3. LIMITATION: 研究集中于准确率指标

4. WHY_GAP_MATTERS: 准确率不是唯一指标，多样性有用户和经济价值

5. PHENOMENON: 过滤气泡及其后果

6. MECHANISM: 相似内容/相似用户导致视野窄化

7. WHY_GAP_MATTERS: 推荐系统应促进自我实现

8. PRIOR_KNOWLEDGE: 离线专家推荐能提高准确率与多样性

9. GAP: 缺少大规模在线受控实验

10. RQ_OR_OBJECTIVE: 在线部署真实推荐系统并测量行为

11. RESULT: 治疗组平台使用上升但专家推荐使用少

12. TRANSITION: 转向推荐属性解释

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 专家推荐提高准确率的离线证据

2. PRIOR_KNOWLEDGE: 专家推荐提高多样性和覆盖率

3. PRIOR_KNOWLEDGE: 新颖性、偶然性与覆盖率定义

4. PRIOR_KNOWLEDGE: 多样性提高满意度

5. STUDY_OVERVIEW: Table 1将本研究与既有离线研究对比

### artifact_design_moves

1. DESIGN_FEATURE: 专家是平台在职内容专业人士

2. REQUIREMENT: 专家以分类列表方式而非逐用户方式参与

3. DESIGN_FEATURE: 专家列表与系统推荐随机混合并约半数展示

4. MECHANISM: 组合多种算法缓解冷启动和过专门化

5. METHOD_JUSTIFICATION: 随机位置避免展示位置偏差

6. DESIGN_FEATURE: 剪辑页也加入匹配当前类别的专家推荐

### evaluation_moves

1. METHOD_JUSTIFICATION: 在线环境用行为指标替代离线准确率

2. BENCHMARK_OR_CONTRAST: 控制组作为反事实

3. RESULT: 行为指标组间差异

4. BENCHMARK_OR_CONTRAST: 显示份额作为期望点击率基准

5. RESULT: 专家推荐AS为负

6. BENCHMARK_OR_CONTRAST: 条件概率比较继续点击

7. RESULT: 专家推荐降低继续点击但控制组更低

8. RESULT: ILS、TC、URC组间差异

9. ROBUSTNESS_OR_BOUNDARY_TEST: 问卷CFA验证

### discussion_and_contribution_moves

1. CONTRIBUTION: 在线实验证明专家推荐增加平台使用

2. CONTRIBUTION: 支持‘准确率不够’论点

3. RESULT: 专家推荐更多样和覆盖更好

4. TRANSITION: 下一步直接控制多样性

5. BOUNDARY_CONDITION: 低风险VOD场景限制

6. LIMITATION_AND_FUTURE: 未披露专家身份的影响

7. LIMITATION_AND_FUTURE: 成本与专家可得性

8. LIMITATION_AND_FUTURE: 无法因果推断多样性作用

## 理论/知识到设计的翻译

### 知识/理论基础

1. 推荐系统准确率与超越准确率评价（McNee et al.; Herlocker et al.）

2. 过滤气泡与自我实现推荐（Pariser; Knijnenburg et al.）

3. 专家推荐离线文献（Amatriain; Bao; Liu; Yun; Zafar等）

4. 现代推荐技术的限制：冷启动、新物品、过专门化

5. 展示/位置偏差行为研究

6. 多样性、选择困难与满意度研究（Ziegler; Kunaver等）

- 理论—设计耦合：partial

- 耦合判定理由：专家知识、过滤气泡和多样性理论塑造了研究问题和“加入专家推荐”这一干预方向，也决定了专家以分类列表而非逐用户模型参与；但底层推荐算法（朴素贝叶斯、k近邻、加权余弦、项目协同、关键词）来自既有商用系统，混合比例和使用行为指标主要是工程与实验设计选择，不是从理论推出的唯一设计。

- 理论到设计翻译链：离线文献和过滤气泡理论指出专家推荐应更准确、更多样、覆盖冷启动。作者选择在职专家作为知识来源，让他们维护分类推荐列表而不是为每个用户建模；再把专家列表随机混合进现有系统，构成治疗组；控制组保持原有系统推荐。评价分为三层：行为指标检验总体是否有效，算法成功分解检验专家推荐是否被单独使用，推荐属性分析检验多样性和覆盖是否构成解释。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：专家拥有更丰富的领域知识，能提供高质和冷门推荐

- mechanism_cn：专家了解目录细节和细分兴趣，可绕过用户历史数据不足

- design_requirement_cn：推荐无需逐用户个性化也能服务大量用户

- artifact_choice_cn：在职专家为每类别手工挑选至少20个剪辑，每天多次更新列表

- evaluated_contrast_cn：治疗组含专家推荐 vs 控制组不含专家推荐

- objective_result_cn：治疗组观看、访问、推荐点击、留存均更高

##### evidence_pointers

1. Section 3.1 expert list design

2. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：内容过滤和协同过滤会限制内容多样性，形成过滤气泡

- mechanism_cn：系统只推荐与用户过去相似或相似用户喜欢的内容

- design_requirement_cn：推荐系统需要引入能跳出用户历史的来源

- artifact_choice_cn：将专家推荐随机混入推荐列表，约半数展示；剪辑页也加入匹配类别的专家推荐

- evaluated_contrast_cn：治疗组推荐列表 vs 控制组推荐列表

- objective_result_cn：治疗组ILS显著更低，TC和URC更高

##### evidence_pointers

1. Table 7

2. Section 5.3

#### 3. 3

- theory_or_knowledge_claim_cn：用户点击受展示位置影响，只看列表前几项

- mechanism_cn：位置而非内容决定点击会造成偏差

- design_requirement_cn：专家推荐不能被放在固定优势或劣势位置

- artifact_choice_cn：随机选择专家列表中的剪辑并随机混排，展示样式无显著区别

- evaluated_contrast_cn：无直接指标；作为排除性设计检查

- objective_result_cn：行为差异被归因于内容组合而非位置

##### evidence_pointers

1. Section 3.1 paragraph on random choice

#### 4. 4

- theory_or_knowledge_claim_cn：标准推荐存在新用户和新物品冷启动问题

- mechanism_cn：缺少评分/观看历史时协同和内容过滤效果差

- design_requirement_cn：专家推荐应能服务新用户和新内容

- artifact_choice_cn：专家列表对所有用户可用；数据分析排除注册后前两周以缓解冷启动/发现效应

- evaluated_contrast_cn：没有单独对照，作为设计保障

- objective_result_cn：作者认为冷启动未影响结果

##### evidence_pointers

1. Section 3.3 warm-up period

#### 5. 5

- theory_or_knowledge_claim_cn：更多样化的推荐可提高用户满意度和选择体验

- mechanism_cn：多样化降低选择困难，增加探索和持续使用

- design_requirement_cn：专家推荐应提高整体多样性，同时不损失满意度

- artifact_choice_cn：保留系统推荐并叠加专家推荐，形成治疗组

- evaluated_contrast_cn：满意度问卷和平台使用在两组间的比较

- objective_result_cn：满意度无差异，平台使用显著上升；多样性和覆盖上升

##### evidence_pointers

1. Section 5.2

2. Table 7

## 评价逻辑

### evaluation_modes

1. 在线随机对照实验（RCT）

2. 点击流行为追踪

3. 算法成功分解（AS）

4. 条件概率继续点击分析

5. 问卷测量与验证性因子分析

6. 推荐列表属性分析（ILS/TC/URC）

- why_these_evaluations_cn：标准准确率指标只能用于离线且不能反映真实使用；在线环境需要行为指标。RCT用于分离“加入专家推荐”的因果效应；算法成功分解回答“哪类推荐被使用”；条件概率分析回答“一次点击是否带来后续使用”；推荐属性分析打开黑箱，解释总体行为差异的潜在来源。

- benchmark_and_contrast_chain_cn：控制组作为总效应的反事实基准；显示份额推导出的期望点击概率作为各推荐算法的机会基准；P_all_control和P_all_treatment作为继续点击分析的参照；ILS、满意度、TC、URC在治疗组和控制组之间构成属性比较。这些对照从“是否有效”逐步推进到“为什么会有效”。

### claim_evidence_ledger

#### 1. 专家推荐提高平台使用

- claim_cn：专家推荐提高平台使用

- evidence_cn：Table 4中治疗组在观看、点击、访问、活跃访问、多剪辑访问、回访和留存上均高于控制组，使用Mann-Whitney U/Fisher检验

- status_cn：有支持

#### 2. 专家推荐被点击少于期望

- claim_cn：专家推荐被点击少于期望

- evidence_cn：Table 5中剪辑页EX的AS=-0.077且p<0.01，着陆页EX的AS=-0.019且p=0.13不显著

- status_cn：有支持，部分页面不显著

#### 3. 点击专家推荐降低继续点击概率

- claim_cn：点击专家推荐降低继续点击概率

- evidence_cn：Table 6中P_expert_treatment=17.2%显著低于P_all_treatment=31.5%

- status_cn：有支持

#### 4. 完全不接触专家推荐的用户继续点击概率更低

- claim_cn：完全不接触专家推荐的用户继续点击概率更低

- evidence_cn：Table 6中P_all_control=14.6%，显著低于P_expert_treatment

- status_cn：有支持

#### 5. 专家推荐使推荐列表更多样

- claim_cn：专家推荐使推荐列表更多样

- evidence_cn：Table 7中治疗组ILS=0.578显著低于控制组0.598，p=0.03

- status_cn：有支持

#### 6. 专家推荐改善味觉覆盖

- claim_cn：专家推荐改善味觉覆盖

- evidence_cn：Section 5.3中TC略有提升且p<0.1，URC显著提升且p<0.01

- status_cn：有支持，效应较小

#### 7. 专家推荐不改变满意度

- claim_cn：专家推荐不改变满意度

- evidence_cn：Table 7中满意度3.43 vs 3.42，无显著差异

- status_cn：有支持

#### 8. 多样性是平台使用上升的机制

- claim_cn：多样性是平台使用上升的机制

- evidence_cn：论文只提供相关和属性差异，没有直接操纵多样性

- status_cn：未直接验证，作者自己也承认

- internal_validity_strategy_cn：随机分配治疗/控制；两组唯一差异是是否含专家推荐；用户不知道实验目标和组别；界面与内容保持一致；无金钱激励；注册后前两周数据被排除以减少发现和冷启动效应；使用非参数检验；问卷用CFA验证效度。

- external_validity_strategy_cn：使用真实商业平台、真实在职专家、真实普通用户，10周观察窗口，样本在性别、年龄和地域上有异质性；平台月访问超百万、内容超十万。

- what_is_not_actually_tested_cn：没有直接操纵推荐多样性来检验其对平台使用的因果作用；没有检验用户知道推荐来自专家时的效果；没有量化专家成本和收益；没有在不同风险或不同内容领域复现效应；没有检验推荐列表其他属性的独立作用；也没有分析满意度之外的其他感知维度。

## 贡献闭环

- technical_claim_cn：在真实在线VOD系统中加入专家推荐可以显著提高多项用户行为指标，例如观看+9.84%、推荐点击+17.1%、留存+14.99%。

- artifact_claim_cn：将专家以分类列表形式混入现有推荐系统，约半数位置展示，是产生这种改进的可识别制品选择；但论文没有隔离“混入比例”或“列表更新频率”的单独贡献。

- mechanism_claim_cn：专家推荐更丰富多样、味觉覆盖更好，这可能是平台使用上升的原因；但论文明确表示无法做因果推断，只提供相关性证据。

- boundary_claim_cn：效应发生在低风险视频点播环境，用户选错推荐代价小，可能更愿意探索；在其他高风险领域或用户不信任专家建议的场景可能不成立。

- reusable_design_knowledge_cn：可用在职专家维护按类别的推荐列表，不需要逐用户个性化；将专家推荐随机混合并控制展示位置；在线评价应使用行为指标而非只依赖离线准确率；总体效果不等于单个推荐算法的点击表现。

- theoretical_contribution_cn：为“准确率不足”论点提供在线现场证据：即使专家推荐个体点击率低，整体平台使用仍上升；将专家推荐离线文献中的多样性/覆盖优势延伸到真实用户行为；提出满意度非必要但多样性和覆盖可能重要的解释。

- how_discussion_closes_intro_gap_cn：引言指出没有大规模在线受控实验检验雇佣专家推荐；结论用10周在线RCT的证据闭合该缺口，并回到过滤气泡和多样性理论，说明专家推荐虽然点击少，但通过多样性和覆盖带来平台收益。

- overclaim_or_unsupported_leaps_cn：关键词“纯存在”可能过度，因为治疗组看到的推荐列表整体不同而不仅是“存在”；将平台使用上升归因于多样性属于推断性解释而非因果结论；满意度无差异但作者仍强调“保持用户满意度不受影响”，这是一种弱化表述；留存率、回访率等部分效应显著性边缘（p=0.07/0.09）却在摘要中直接表述为显著提升。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：大量推荐系统研究在离线条件下优化建议准确率，但这种做法可能造成过滤气泡并限制用户发现内容的多样性。

- rhetorical_function_cn：在摘要中建立问题领域和核心张力。

- depends_on_cn：无。

- sets_up_cn：引出专家推荐的离线证据和本研究必要性。

- evidence_pointer：Abstract P1 S1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：LIMITATION

- paraphrase_cn：已有离线研究显示专家能生成更多样、更新颖的推荐，并降低噪声，但这些证据不是来自真实用户行为。

- rhetorical_function_cn：指出现有离线研究的局限。

- depends_on_cn：前一句的过滤气泡背景。

- sets_up_cn：为在线实验提供动机。

- evidence_pointer：Abstract P1 S2

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文在大型电视网的视频点播网站上部署真实推荐系统，检验专家推荐对用户行为的影响。

- rhetorical_function_cn：明确研究问题与场景。

- depends_on_cn：前面的离线局限。

- sets_up_cn：介绍关键结果。

- evidence_pointer：Abstract P1 S3

### 4. P2 S1

- order：4

- section：Abstract

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：向先进系统加入专家推荐后，平台使用显著上升；即使专家推荐被使用和成功程度低于预期，用户观看更多剪辑、使用更多推荐并更频繁回访。

- rhetorical_function_cn：提前给出反直觉核心发现。

- depends_on_cn：目标句。

- sets_up_cn：为属性分析埋下伏笔。

- evidence_pointer：Abstract P2 S1

### 5. P2 S2

- order：5

- section：Abstract

- locator：P2 S2

- move_code：RESULT

- paraphrase_cn：专家推荐更多样且提高味觉覆盖，但用户满意度不变。

- rhetorical_function_cn：补充解释性结果。

- depends_on_cn：总体行为上升的结果。

- sets_up_cn：结论和理论贡献。

- evidence_pointer：Abstract P2 S2

### 6. P1 S1

- order：6

- section：1 Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：在线网站内容过多，推荐系统帮助用户缓解决策过载，被用于电商、视频、社交和学术网站。

- rhetorical_function_cn：把研究嵌入常见信息系统场景。

- depends_on_cn：无。

- sets_up_cn：引向准确率主流。

- evidence_pointer：Introduction P1 S1

### 7. P1 S2

- order：7

- section：1 Introduction

- locator：P1 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：推荐通常基于内容相似或相似用户的协同过滤。

- rhetorical_function_cn：交代技术基线。

- depends_on_cn：前一句的推荐系统背景。

- sets_up_cn：随后批评只优化准确率。

- evidence_pointer：Introduction P1 S2

### 8. P2 S1

- order：8

- section：1 Introduction

- locator：P2 S1

- move_code：LIMITATION

- paraphrase_cn：大量研究集中于优化预测准确率和分类准确率，如RMSE和精确率。

- rhetorical_function_cn：指出现有研究重心。

- depends_on_cn：推荐技术基线。

- sets_up_cn：说明准确率不是唯一指标。

- evidence_pointer：Introduction P2 S1

### 9. P2 S2-S3

- order：9

- section：1 Introduction

- locator：P2 S2-S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：准确率目标虽好，但系统质量可从多角度评价；多样性能提高满意度和平台收益。

- rhetorical_function_cn：把研究从算法指标拉向用户价值。

- depends_on_cn：准确率主导的局限。

- sets_up_cn：过滤气泡问题。

- evidence_pointer：Introduction P2 S2-S3

### 10. P3 S1

- order：10

- section：1 Introduction

- locator：P3 S1

- move_code：PHENOMENON

- paraphrase_cn：基于内容和协同过滤的系统常把用户关进‘过滤气泡’，只能看到狭窄内容。

- rhetorical_function_cn：引入经验现象。

- depends_on_cn：超越准确率评价的讨论。

- sets_up_cn：解释机制和后果。

- evidence_pointer：Introduction P3 S1

### 11. P3 S2

- order：11

- section：1 Introduction

- locator：P3 S2

- move_code：MECHANISM

- paraphrase_cn：喜欢动作片的用户会只收到动作推荐，可能错过其他内容或被强化既有观点。

- rhetorical_function_cn：具象化过滤气泡机制。

- depends_on_cn：过滤气泡现象。

- sets_up_cn：自我实现目标。

- evidence_pointer：Introduction P3 S2

### 12. P3 S3

- order：12

- section：1 Introduction

- locator：P3 S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：系统应帮助用户发现多样兴趣，即自我实现，而不是强化当前行为。

- rhetorical_function_cn：引入评价推荐系统的新价值标准。

- depends_on_cn：过滤气泡机制。

- sets_up_cn：专家作为潜在解。

- evidence_pointer：Introduction P3 S3

### 13. P4 S1

- order：13

- section：1 Introduction

- locator：P4 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：离线研究表明专家能提高推荐的准确率、多样性和新颖性；专家可从普通用户识别或为行业从业者，可直接或间接参与推荐。

- rhetorical_function_cn：总结已有知识。

- depends_on_cn：自我实现目标。

- sets_up_cn：指出还缺在线研究。

- evidence_pointer：Introduction P4 S1

### 14. P4 S2

- order：14

- section：1 Introduction

- locator：P4 S2

- move_code：GAP

- paraphrase_cn：据作者所知，尚无大规模在线受控研究检验职业雇佣专家推荐对用户行为或推荐属性的影响。

- rhetorical_function_cn：构建明确缺口。

- depends_on_cn：离线专家研究综述。

- sets_up_cn：陈述本研究。

- evidence_pointer：Introduction P4 S2

### 15. P5 S1

- order：15

- section：1 Introduction

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文在真实视频点播网站部署在线推荐，招募普通用户，研究专家推荐对平台使用的影响。

- rhetorical_function_cn：把缺口转成研究问题。

- depends_on_cn：前面缺口。

- sets_up_cn：给出具体指标和结果。

- evidence_pointer：Introduction P5 S1

### 16. P5 S2-S3

- order：16

- section：1 Introduction

- locator：P5 S2-S3

- move_code：RESULT

- paraphrase_cn：治疗组观看+9.8%、访问+9.0%、推荐使用+17.1%；专家推荐本身使用较少且成功较低，但属性分析显示其多样性和味觉覆盖更高。

- rhetorical_function_cn：提前预告完整证据链。

- depends_on_cn：研究问题句。

- sets_up_cn：引导读者进入研究设计和结果。

- evidence_pointer：Introduction P5 S2-S3

### 17. P1-P4

- order：17

- section：2 Related work

- locator：P1-P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究用不同专家类型在电影、旅游、音乐、新闻等领域提高准确率，并有的提升多样性和覆盖率。

- rhetorical_function_cn：证明专家推荐主题已有离线积累。

- depends_on_cn：引言中的专家知识。

- sets_up_cn：Table 1 对比。

- evidence_pointer：Section 2 paragraphs 1-4

### 18. Table 1前段

- order：18

- section：2 Related work

- locator：Table 1前段

- move_code：STUDY_OVERVIEW

- paraphrase_cn：Table 1总结已有研究；多数是离线评价，且专家多为被动用户专家，而本研究是在线RCT且专家为主动在职专业人员。

- rhetorical_function_cn：用表格标出本研究位置。

- depends_on_cn：相关文献综述。

- sets_up_cn：说明设计选择。

- evidence_pointer：Section 2 before Table 1

### 19. P1

- order：19

- section：3 Study design

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者使用商业系统并加入专家推荐，平台月访问超百万、内容超十万，构成信息过载场景。

- rhetorical_function_cn：说明为什么用这个现场。

- depends_on_cn：引言中的信息过载问题。

- sets_up_cn：介绍专家和页面。

- evidence_pointer：Section 3 P1

### 20. P2

- order：20

- section：3 Study design

- locator：P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：专家是每日负责平台内容的在职专业人士，对目录有深入知识，能对细分兴趣推荐高质量条目。

- rhetorical_function_cn：明确专家知识来源。

- depends_on_cn：专家推荐概念。

- sets_up_cn：专家如何参与推荐。

- evidence_pointer：Section 3 P2

### 21. P1

- order：21

- section：3.1 Landing page recommendations

- locator：P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：着陆页推荐基于用户完整观看历史，融合朴素贝叶斯和k近邻协同过滤两种标准技术。

- rhetorical_function_cn：描述系统基线。

- depends_on_cn：商用系统背景。

- sets_up_cn：专家推荐的接入方式。

- evidence_pointer：Section 3.1 P1

### 22. P4

- order：22

- section：3.1 Landing page recommendations

- locator：P4

- move_code：REQUIREMENT

- paraphrase_cn：专家无法给每个用户个性化推荐，因此为每个类别手工挑选至少20个剪辑并每日多次更新列表。

- rhetorical_function_cn：把专家知识转化为可实现的设计约束。

- depends_on_cn：大规模用户与专家时间限制。

- sets_up_cn：随机混合策略。

- evidence_pointer：Section 3.1 P4

### 23. P5

- order：23

- section：3.1 Landing page recommendations

- locator：P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统从专家列表随机选剪辑，与系统推荐混合，约一半为专家推荐；随机位置避免位置偏差。

- rhetorical_function_cn：保证治疗组确实看到专家推荐且排除展示位置混淆。

- depends_on_cn：专家列表设计。

- sets_up_cn：说明为何控制/治疗只差专家推荐。

- evidence_pointer：Section 3.1 P5

### 24. P6

- order：24

- section：3.1 Landing page recommendations

- locator：P6

- move_code：MECHANISM

- paraphrase_cn：结合多种算法可互相弥补：协同过滤有新品问题，内容过滤有过专门化问题，两者都有新用户问题；专家可缓解这些缺陷。

- rhetorical_function_cn：给出工程设计与理论机制的统一解释。

- depends_on_cn：标准推荐算法限制。

- sets_up_cn：专家推荐合理性的理论支撑。

- evidence_pointer：Section 3.1 P6

### 25. P1-P4

- order：25

- section：3.2 Clip page recommendations

- locator：P1-P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：剪辑页推荐基于当前观看剪辑而非完整历史，使用加权余弦内容相似、项目协同过滤和关键词推荐，再混合匹配当前类别的专家推荐。

- rhetorical_function_cn：展示干预扩展到推荐系统的第二入口。

- depends_on_cn：着陆页干预设计。

- sets_up_cn：保证两种页面都能暴露专家推荐。

- evidence_pointer：Section 3.2 P1-P4

### 26. P1

- order：26

- section：3.3 Data collection

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通过弹窗招募平台正常用户，不解释推荐生成细节，不告知专家参与，无金钱激励，以减少选择偏差。

- rhetorical_function_cn：说明样本获取和屏蔽机制。

- depends_on_cn：实验干预设计。

- sets_up_cn：样本与随机分配。

- evidence_pointer：Section 3.3 P1

### 27. P2-P3

- order：27

- section：3.3 Data collection

- locator：P2-P3

- move_code：RESULT

- paraphrase_cn：共招募6374人，清理后2715人；年龄、性别和地域分布有异质性。

- rhetorical_function_cn：给出实验样本特征。

- depends_on_cn：招募程序。

- sets_up_cn：为随机分配提供有效人群。

- evidence_pointer：Section 3.3 P2-P3, Tables 2-3

### 28. P4

- order：28

- section：3.3 Data collection

- locator：P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：用户被随机分到治疗组（系统+专家推荐）或控制组（仅系统推荐）；除专家推荐外无其他差异。

- rhetorical_function_cn：建立因果识别设计。

- depends_on_cn：样本招募。

- sets_up_cn：行为比较。

- evidence_pointer：Section 3.3 P4

### 29. P5

- order：29

- section：3.3 Data collection

- locator：P5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用户不知实验组别，界面与内容保持不变，推荐列表样式沿用平台已有设计，降低使用困难导致的流失。

- rhetorical_function_cn：强化内部效度。

- depends_on_cn：随机分配设计。

- sets_up_cn：消除界面混淆。

- evidence_pointer：Section 3.3 P5

### 30. P6

- order：30

- section：3.3 Data collection

- locator：P6

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：注册后两周数据被排除，以去除新奇/发现效应并缓解冷启动；多数用户一周内不再看到提示横幅。

- rhetorical_function_cn：处理时间相关的行为污染。

- depends_on_cn：冷启动讨论。

- sets_up_cn：得到干净10周行为数据。

- evidence_pointer：Section 3.3 P6

### 31. P7

- order：31

- section：3.3 Data collection

- locator：P7

- move_code：RESULT

- paraphrase_cn：收集10周点击流共617194次交互，其中87357次剪辑点击、7270次推荐点击；问卷收回3560份，有效2209份。

- rhetorical_function_cn：为后续分析提供数据规模。

- depends_on_cn：数据采集程序。

- sets_up_cn：结果部分。

- evidence_pointer：Section 3.3 P7

### 32. P0

- order：32

- section：4 Results

- locator：P0

- move_code：STUDY_OVERVIEW

- paraphrase_cn：先比较行为；再分析不同推荐算法被使用程度；最后考察点击推荐后是否继续点击。

- rhetorical_function_cn：预告三阶段证据。

- depends_on_cn：数据采集完成。

- sets_up_cn：4.1-4.3。

- evidence_pointer：Section 4 opening

### 33. P1

- order：33

- section：4.1 User behavior

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：标准准确率指标只适合离线，在线需用真实行为作为准确性的替代，因此使用观看、访问、推荐点击等指标。

- rhetorical_function_cn：解释从离线指标转向行为指标的理由。

- depends_on_cn：研究目标。

- sets_up_cn：指标定义和检验。

- evidence_pointer：Section 4.1 P1

### 34. P3

- order：34

- section：4.1 User behavior

- locator：P3

- move_code：RESULT

- paraphrase_cn：治疗组在观看剪辑、推荐点击、总访问、活跃访问、多剪辑访问、回访率和留存率上均高于控制组，部分达到或接近显著。

- rhetorical_function_cn：给出主效应证据。

- depends_on_cn：行为指标定义。

- sets_up_cn：说明专家推荐的总体好处。

- evidence_pointer：Section 4.1 P3, Table 4

### 35. P4

- order：35

- section：4.1 User behavior

- locator：P4

- move_code：RESULT

- paraphrase_cn：专家虽不能逐人个性化，但展示专家推荐仍带来更高平台使用。

- rhetorical_function_cn：总结主效应并回应设计限制。

- depends_on_cn：Table 4结果。

- sets_up_cn：引入悖论。

- evidence_pointer：Section 4.1 P4

### 36. P1-P2

- order：36

- section：4.2 Algorithm success

- locator：P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为了知道哪类推荐更受用户欢迎，用显示份额作为期望点击概率，定义算法成功AS为实际点击份额减期望份额。

- rhetorical_function_cn：提供分解点击来源的基准。

- depends_on_cn：总体行为效应。

- sets_up_cn：比较不同推荐类型。

- evidence_pointer：Section 4.2 P1-P2

### 37. P4

- order：37

- section：4.2 Algorithm success

- locator：P4

- move_code：RESULT

- paraphrase_cn：剪辑页内容相似推荐被点击显著多于期望，专家推荐显著少于期望；着陆页专家推荐略低但不显著，用户协同推荐显著高于期望。

- rhetorical_function_cn：显示专家推荐个体吸引力薄弱。

- depends_on_cn：AS指标。

- sets_up_cn：制造效果悖论。

- evidence_pointer：Fig. 1, Table 5

### 38. P5

- order：38

- section：4.2 Algorithm success

- locator：P5

- move_code：RESULT

- paraphrase_cn：结果反直觉：专家建议使用低于预期，但治疗组平台使用却显著更高。

- rhetorical_function_cn：明确悖论并驱动后续分析。

- depends_on_cn：主效应和AS结果。

- sets_up_cn：继续点击概率。

- evidence_pointer：Section 4.2 P5

### 39. P1

- order：39

- section：4.3 Success of recommendations

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通过计算点击某推荐后继续点击其他推荐的条件概率，评估推荐是否真正成功。

- rhetorical_function_cn：用行为链衡量推荐质量。

- depends_on_cn：AS悖论。

- sets_up_cn：P_all/P_expert比较。

- evidence_pointer：Section 4.3 P1

### 40. P3

- order：40

- section：4.3 Success of recommendations

- locator：P3

- move_code：RESULT

- paraphrase_cn：点击专家推荐后继续点击的概率(17.2%)低于治疗组整体(31.5%)，但高于控制组整体(14.6%)；差异显著。

- rhetorical_function_cn：说明专家推荐本身不增加粘性，但接触专家推荐的整体体验提高使用。

- depends_on_cn：条件概率设计。

- sets_up_cn：属性解释。

- evidence_pointer：Section 4.3 P3, Table 6

### 41. P0

- order：41

- section：5 Properties of recommendation

- locator：P0

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为解释行为差异，转而分析推荐属性：多样性、满意度、覆盖率。

- rhetorical_function_cn：把分析从行为转向解释变量。

- depends_on_cn：行为悖论。

- sets_up_cn：三个子节。

- evidence_pointer：Section 5 opening

### 42. P1

- order：42

- section：5.1 Diversity

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用标准化列表内相似度ILS度量推荐列表多样性；高ILS表示低多样性。

- rhetorical_function_cn：选择客观属性指标。

- depends_on_cn：属性分析动机。

- sets_up_cn：报告组间差异。

- evidence_pointer：Section 5.1 P1

### 43. P3

- order：43

- section：5.1 Diversity

- locator：P3

- move_code：RESULT

- paraphrase_cn：治疗组推荐列表ILS显著更低，即专家推荐使推荐更多样；该结果与离线专家研究一致。

- rhetorical_function_cn：提供第一个解释性证据。

- depends_on_cn：ILS指标。

- sets_up_cn：联系满意度。

- evidence_pointer：Section 5.1 P3, Table 7

### 44. P1

- order：44

- section：5.2 Perceived satisfaction

- locator：P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：多样化推荐可能提高用户满意度，即使牺牲准确率，并降低选择困难。

- rhetorical_function_cn：为满意度与多样性关系提供理论预期。

- depends_on_cn：多样性结果。

- sets_up_cn：问卷测量。

- evidence_pointer：Section 5.2 P1

### 45. P2-P3

- order：45

- section：5.2 Perceived satisfaction

- locator：P2-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：问卷用5点Likert并做CFA，AVE和区分效度满足标准。

- rhetorical_function_cn：保证感知测量有效。

- depends_on_cn：满意度理论。

- sets_up_cn：报告满意度结果。

- evidence_pointer：Section 5.2 P2-P3

### 46. P4

- order：46

- section：5.2 Perceived satisfaction

- locator：P4

- move_code：RESULT

- paraphrase_cn：两组满意度几乎相同（3.42 vs 3.43），说明平台使用上升并不伴随满意度变化。

- rhetorical_function_cn：排除满意度作为机制。

- depends_on_cn：CFA验证。

- sets_up_cn：转向覆盖。

- evidence_pointer：Section 5.2 P4, Table 7

### 47. P1

- order：47

- section：5.3 Coverage

- locator：P1

- move_code：LIMITATION

- paraphrase_cn：由于两组共享同一系统且专家不逐条推荐，不测量预测覆盖和目录覆盖，只测味觉覆盖TC和独特推荐使用URC。

- rhetorical_function_cn：界定覆盖测量的边界。

- depends_on_cn：覆盖定义综述。

- sets_up_cn：TC/URC结果。

- evidence_pointer：Section 5.3 P1

### 48. P3-P4

- order：48

- section：5.3 Coverage

- locator：P3-P4

- move_code：RESULT

- paraphrase_cn：治疗组TC略高(p<0.1)，URC显著更高(p<0.01)，表明专家推荐覆盖了更多用户看过内容且独特推荐被更多使用。

- rhetorical_function_cn：提供第二个解释性证据。

- depends_on_cn：TC/URC定义。

- sets_up_cn：与多样性共同支撑解释。

- evidence_pointer：Section 5.3 P3-P4

### 49. P1-P2

- order：49

- section：6 Conclusions and future research

- locator：P1-P2

- move_code：CONTRIBUTION

- paraphrase_cn：在线实验证明专家推荐增加观看、推荐使用和留存，并能转化为收入；专家推荐虽使用低于预期，但总体平台使用更高，支持‘准确率不够’观点。

- rhetorical_function_cn：把局部结果提升为一般设计知识。

- depends_on_cn：所有实证结果。

- sets_up_cn：理论返回。

- evidence_pointer：Section 6 P1-P2

### 50. P3

- order：50

- section：6 Conclusions and future research

- locator：P3

- move_code：RESULT

- paraphrase_cn：专家推荐更多样且更好覆盖用户口味；下一步应直接控制多样性做大型受控实验。

- rhetorical_function_cn：明确提出未来机制检验。

- depends_on_cn：属性分析结果。

- sets_up_cn：限制讨论。

- evidence_pointer：Section 6 P3

### 51. P4

- order：51

- section：6 Conclusions and future research

- locator：P4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究不能推断多样性导致平台使用，因为未直接操纵多样性。

- rhetorical_function_cn：保护因果边界。

- depends_on_cn：属性分析。

- sets_up_cn：其他限制。

- evidence_pointer：Section 6 P4

### 52. P5

- order：52

- section：6 Conclusions and future research

- locator：P5

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：实验处于低风险VOD场景，用户选错推荐代价小，可能更愿探索；在其他高风险领域未必成立。

- rhetorical_function_cn：限定适用范围。

- depends_on_cn：核心结论。

- sets_up_cn：建议变换领域。

- evidence_pointer：Section 6 P5

### 53. P6

- order：53

- section：6 Conclusions and future research

- locator：P6

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：雇佣专家难找且需付费，经济可行性因平台而异；小众品类可能更难找专家。

- rhetorical_function_cn：讨论资源约束。

- depends_on_cn：成本与效益框架。

- sets_up_cn：成本收益待估计。

- evidence_pointer：Section 6 P6

### 54. P7

- order：54

- section：6 Conclusions and future research

- locator：P7

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：实验未告知用户推荐来自专家；若披露专家身份，用户信任和感知可能不同；算法与人类建议偏好需进一步研究。

- rhetorical_function_cn：指出另一个边界条件。

- depends_on_cn：未披露设计。

- sets_up_cn：未来研究。

- evidence_pointer：Section 6 P7

## 写作技术

- gap_construction_cn：作者先肯定离线专家推荐的优势，再明确指出“尚无大规模在线受控研究”，形成‘离线证据充分但在线行为证据缺失’的方法论缺口；同时用过滤气泡的社会影响提高缺口的重要性。

- signposting_cn：摘要提前给结果；引言末尾预告关键数字；Section 3开头说明改造系统；Results开头预告4.1-4.3；Section 5开头声明转属性分析；结论逐条回扣贡献和限制。

- transition_logic_cn：行为正效应之后立即问“哪类推荐被使用”；AS显示专家推荐失败后立即问“点击后是否继续点击”；继续点击仍不能解释总体效应，于是转向推荐属性；属性结果引出“未来直接控制多样性”。

- claim_evidence_rhythm_cn：每个结果段先定义指标，接着报告数值、检验统计量和p值，再给出解释；对反直觉结果不回避，而是将其作为下一阶段分析的起点。

- benchmark_narrative_cn：控制组是总效应的反事实基准；显示份额形成期望点击概率基准；P_all_control/P_all_treatment是继续点击分析基准；这些benchmark都服务于把行为差异从‘总体是否有效’推进到‘哪个部分、为什么有效’。

- theory_return_cn：结论回到McNee等人的‘准确率不够’和过滤气泡，用在线证据说明专家推荐带来的多样性和覆盖可能比单个推荐点击率更重要，从而把实证结果重新接回理论争论。

- contribution_positioning_cn：作者把贡献定位于‘首个在线RCT’、‘真实平台与真实用户’、‘专业雇佣专家’以及‘揭示准确率与行为使用的分离’，并强调对推荐系统设计和平台收益的含义。

- novelty_protection_cn：作者不把贡献包装成‘专家推荐点击率高’，而是反转叙事：尽管专家推荐本身点击低，整体效果仍显著上升；再用多样性和覆盖属性解释，防止退化为一次性性能结果；同时留下明确因果边界，避免被批评为过度解释。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立推荐系统准确率主导的局限、过滤气泡问题、离线专家推荐优势，并指出现有研究缺少在线实验。

- research_job_cn：系统综述专家推荐文献并识别方法缺口。

- required_evidence_cn：证明专家推荐离线优势存在但没有在线RCT证据。

- transition_to_next_cn：用“本文部署真实在线RCT”承接。

#### 2. 2

- step：2

- writing_job_cn：描述平台、专家、推荐算法和实验干预设计。

- research_job_cn：改造真实商业系统，构造治疗/控制差异，确保除专家推荐外其他条件不变。

- required_evidence_cn：清晰说明专家列表生成、混合比例、随机位置和屏蔽设计。

- transition_to_next_cn：说明如何招募和采集数据。

#### 3. 3

- step：3

- writing_job_cn：描述参与者招募、随机分配、盲实验、数据清洗和预热期。

- research_job_cn：执行10周现场RCT，采集点击流和问卷。

- required_evidence_cn：给出有效样本量、数据规模和清洗逻辑。

- transition_to_next_cn：进入行为比较。

#### 4. 4

- step：4

- writing_job_cn：定义行为指标和统计检验，报告组间差异。

- research_job_cn：用非参数检验比较治疗组和控制组。

- required_evidence_cn：多个行为指标显著或边缘显著且方向一致。

- transition_to_next_cn：追问“是否因为某类推荐被使用”。

#### 5. 5

- step：5

- writing_job_cn：定义算法成功指标和期望基准，报告各推荐类型的AS；再用条件概率分析点击后续行为。

- research_job_cn：计算显示份额与点击份额之差；计算继续点击概率。

- required_evidence_cn：显示专家推荐点击低但整体效果仍为正，形成可解释的悖论。

- transition_to_next_cn：从行为分解转向推荐属性。

#### 6. 6

- step：6

- writing_job_cn：报告多样性、满意度、覆盖属性差异，并回到理论解释；最后明确限制和未来因果实验。

- research_job_cn：计算ILS、问卷CFA、TC/URC，比较两组。

- required_evidence_cn：属性差异与行为差异方向一致，同时承认不能因果推断。

- transition_to_next_cn：结论提出直接控制多样性。

### most_transferable_moves_cn

1. 用Table对比已有研究与本研究，快速定位贡献

2. 用显示份额作为期望点击概率的简单基准，进行算法成功分解

3. 用条件概率分析点击推荐后的继续行为

4. 在个体推荐点击表现不佳时转而分析推荐属性作为解释

5. 将正效应与个体推荐失败并置制造认知张力，驱动后续证据

### resource_intensive_or_nonstandard_parts_cn

1. 需要真实商业平台和超过一百万月访量

2. 需要雇佣并管理在职专家，要求专家每日维护多类别推荐列表

3. 10周在线实验和大量用户招募无激励，可能成本高

4. 需要获得平台方支持并嵌入系统，无法仅靠离线数据复现

### what_not_to_copy_superficially_cn

1. 不能只在讨论中声称多样性和覆盖导致使用上升，除非做了直接操纵

2. 不能忽略专家推荐本身点击率低的事实而只报告总体正效应

3. 不能把边缘显著指标说成强显著

4. 不能在没有对照组和随机分配的情况下宣称因果效应

5. 不能把VOD低风险结论推广到电商、约会等高风险场景

- single_best_description_of_the_routine_cn：用一个真实平台上的在线RCT比较含与不含专家推荐的推荐系统，先用行为指标证明总体效应，再用算法点击份额和条件概率分解悖论，最后用推荐属性分析给出可能的非准确率解释。

## 分析边界

未提供问卷具体题项文本，仅说明5点Likert和CFA；Fig.1为图片无法确认误差线细节；参考文献OCR格式有轻微错乱；论文未说明AS显著性检验的具体方法；补充材料和附录缺失；没有编码页面号，仅以章节和段落定位。
