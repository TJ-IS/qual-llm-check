# Conversational Recommender Systems and natural language:

- 作者：Andrea Iovine; Fedelucio Narducci; Giovanni Semeraro
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113250
- 源文件：08250_2020_conversational-recommender-systems-and-natural-language.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.82

## 文章级论证概况

- 核心问题：自然语言能否以及如何在会话式推荐系统（CoRS）中提升交互成本与推荐质量？CoRS各组件对推荐准确率的影响是什么？

- 制品与设计：提出并实现领域无关、可配置的会话式推荐框架ConveRSE，采用模块化架构，包含Dialog Manager、Intent Recognizer、Sentiment Analyzer、Entity Recognizer和Recommendation Services五个组件，并提供按钮、自然语言、混合三种交互方式；混合模式仅在消歧阶段用按钮替代手写实体名。

- 客观结果：在bAbI Movie Dialog Dataset和ConvRecSysDataset上，以Upper bound为基准测量Intent/Entity/Sentiment三种组件测试的HitRate损失；在电影、图书、音乐三个域开展被试内用户研究，比较三种交互模式在NQ、IT、TPQ、QD、Accuracy、MAP上的差异；统计结果显示混合模式在多数指标上显著优于纯NL和按钮模式。

- 核心贡献：贡献包括ConveRSE框架、组件级消融实验证据、真实用户交互模式比较、设计洞察（纯NL需要传统交互元素辅助，尤其在消歧和选项选择任务中），以及公开的真实对话数据集。

- 整篇论证链：论文先指出数字助手广泛使用但不具备推荐能力，而CoRS适合通过对话完成推荐，随后以模块化对话系统知识和现有CoRS研究中关于NL是否有益的矛盾观点作为缺口，提出ConveRSE框架；通过合成数据上的四配置消融实验揭示Entity和Sentiment识别在冷启动下对推荐准确率的关键作用，再通过三个领域的被试内用户研究比较NL、按钮和混合交互，证明纯NL并不稳定最优，混合模式通过降低消歧负担稳定改善交互成本和推荐质量，最后回答四个研究问题并发布对话数据集。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心是构建一个可配置的CoRS框架ConveRSE，并对其组件与交互模式进行系统评价；虽然包含用户实验和数据集发布，但整体论证仍围绕制品构建、离线消融、用户评价和设计知识展开，属于设计科学式的研究，而非单一理论检验、纯计算benchmark或平台现场实验。

- 主导写作弧线判定：文章从CoRS和数字助手的需求出发，构建框架，分别在合成数据和真实用户环境中评价，最后得出纯NL交互需要按钮支持、实体识别在冷启动中关键等可复用设计知识；虽然要求没有以显式设计原则列表提出，但叙述结构符合“要求—构建—评价—设计知识”的设计科学写作弧线。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：第一阶段构建框架并定义三种交互模式；第二阶段在合成数据上进行组件级消融实验，回答RQ3并识别关键组件；第三阶段开展三个领域、三种交互模式的真实用户研究，回答RQ1/RQ2/RQ4；第四阶段深入分析对话日志并发布真实对话数据集，支持解释与未来研究。

### studies_or_phases

#### 1. 框架构建与交互模式设计

- order：1

- name_cn：框架构建与交互模式设计

- question_cn：如何构建一个领域无关、可配置的CoRS，并设计不同的交互模式以研究自然语言的影响？

- inputs_and_setting_cn：基于模块化Goal-Oriented对话系统文献、Wikidata知识库、之前Narducci等人的系统，以及bAbI/ConvRecSys等后续评价所需的数据条件。

- designed_or_compared_object_cn：ConveRSE的五个组件及按钮、NL、混合三种交互模式。

- baseline_control_or_counterfactual_cn：模块化架构作为架构设计参照；按钮模式随后被用作用户研究的控制条件。

##### objective_metrics

（空）

- analysis_method_cn：架构设计、组件映射、运行示例说明。

- main_result_cn：得到可配置的框架，包含Dialog Manager、Intent Recognizer、Sentiment Analyzer、Entity Recognizer、Recommendation Services，并实现三种交互模式。

- argumentative_role_cn：为后续消融实验提供可独立测试的组件，为真实用户研究提供三种被比较的交互模式。

- remaining_uncertainty_cn：各组件的识别误差如何影响推荐准确率、不同交互模式在实际用户中的表现尚不清楚。

- link_to_next_phase_cn：组件划分直接决定合成数据上四配置消融实验；三种交互模式直接构成用户研究的处理条件。

##### evidence_pointers

1. Section 3, Fig. 1

2. Section 3.1, Fig. 2

3. Section 3.2, Figs. 3 and 4

#### 2. 合成数据上的组件消融实验

- order：2

- name_cn：合成数据上的组件消融实验

- question_cn：Intent Recognizer、Entity Recognizer、Sentiment Analyzer各自对推荐准确率的独立影响是什么？

- inputs_and_setting_cn：bAbI Movie Dialog Dataset和ConvRecSysDataset的MovieTweetings部分；仅使用测试/开发/验证集，并对不能映射到KB的实例进行过滤。

- designed_or_compared_object_cn：四种配置：Upper bound、Intent Test、Entity Test、Sentiment Test；每种配置只保留一个组件在真实运行，其余组件由程序提供的正确答案替代。

- baseline_control_or_counterfactual_cn：Upper bound为理想组件输入的基准；各组件测试相对Upper bound计算损失。

##### objective_metrics

1. HitRate@5/10/20/50/100

2. 相对Upper bound的HitRate损失

- analysis_method_cn：按数据集分别报告HitRate和损失，结合组件识别准确率解释损失来源。

- main_result_cn：bAbI上HR@5时Entity Recognizer损失最大（58.21%），HR@100时Intent Recognizer损失最大（21.11%）；ConvRecSysDataset上组件损失整体较小，Sentiment Recognizer约3–4%损失成为最大来源。

- argumentative_role_cn：回答RQ3，证明实体识别在冷启动和小偏好集下是推荐准确率的关键环节，情绪识别的重要性次之。

- remaining_uncertainty_cn：合成数据没有真实用户交互，无法回答NL对交互成本和用户体验的影响；也没有观察用户在对话中的实际表达方式。

- link_to_next_phase_cn：组件层面的结果说明了“听懂用户”的重要性，但需要真实用户研究来评估不同交互模式如何影响成本和准确率。

##### evidence_pointers

1. Section 4.1.2, four configurations

2. Section 4.1.3, HitRate metric

3. Table 1

4. Table 2

5. Section 4.1.4 and 4.1.5

#### 3. 真实用户交互模式比较

- order：3

- name_cn：真实用户交互模式比较

- question_cn：自然语言、按钮和混合三种交互模式在交互成本和推荐质量上是否有显著差异？关键问题出现在哪里？

- inputs_and_setting_cn：电影域50人、图书域55人、音乐域54人；每个被试在各自域内依次测试三种交互模式；系统实例的KB分别包含15954部电影、7592本书、12926首歌曲及其属性。

- designed_or_compared_object_nl：NL、Buttons、Mixed三种交互模式；三种模式共享相同推荐算法，区别只在于交互驱动方式和消歧方式。

- designed_or_compared_object_cn：NL、Buttons、Mixed三种交互模式；三种模式共享相同推荐算法，区别只在于交互驱动方式和消歧方式。

- baseline_control_or_counterfactual_cn：Buttons模式作为控制条件；Mixed模式是NL模式仅修改消歧环节后的变体。

##### objective_metrics

1. Accuracy

2. MAP

3. NQ

4. IT

5. TPQ

6. QD

- analysis_method_cn：描述性统计、MANOVA检验整体差异、Mann-Whitney配对检验并做Bonferroni校正；另用ResQue问卷采集用户主观评价。

- main_result_cn：Buttons模式需要更多问题；NL模式在TPQ/IT上通常更慢；Mixed模式在交互成本与准确率指标上整体最佳或与最优无异；三类模式的ResQue问卷中位数普遍为Agree，MANOVA未发现问卷整体显著差异。

- argumentative_role_cn：回答RQ1、RQ2和RQ4，证明纯NL并非最好，消歧是NL交互的主要瓶颈，按钮支持能稳定提升表现。

- remaining_uncertainty_cn：问卷未显示三个模式之间的主观差异；还需要理解低兴趣用户和指标相关性的机制；没有隔离偏好获取步骤和推荐展示步骤的独立影响。

- link_to_next_phase_cn：通过深入分析用户兴趣/经验和指标相关性，解释Mixed为什么有效，并为后续研究提出假设。

##### evidence_pointers

1. Section 4.2

2. Section 4.2.1 metrics

3. Tables 3 and 4

4. Section 4.2.3 statistical tests

5. Section 4.2.4 questionnaire

#### 4. 日志深挖与数据发布

- order：4

- name_cn：日志深挖与数据发布

- question_cn：哪些用户特征和交互行为可以解释Mixed模式的优势？这些真实对话能否成为公共资源？

- inputs_and_setting_cn：用户研究过程中收集的对话日志；用户问卷中的计算机经验（Q4）和领域兴趣（Q6）作为分组变量；约6500条NL消息和2800条Mixed消息。

- designed_or_compared_object_cn：按用户经验/兴趣划分的子群，对比NL与Mixed在IT/TPQ上的差距；计算指标之间的Pearson相关系数。

- baseline_control_or_counterfactual_cn：低兴趣用户与高兴趣用户之间的表现差距；Buttons模式下的相关系数作为参照。

##### objective_metrics

1. IT

2. TPQ

3. QD

4. Pearson相关系数

- analysis_method_cn：子群描述性比较和Pearson相关分析。

- main_result_cn：Mixed模式显著降低IT和TPQ，对低兴趣用户尤其明显；图书和音乐域中NL/Mixed的QD与IT呈弱到中度负相关，Buttons下相关较弱。

- argumentative_role_cn：加强Mixed模式优势的机制解释，同时为数据集作为公开资源提供说明。

- remaining_uncertainty_cn：相关分析不能建立因果关系；QD提升是否由NL界面引起仍只是推测，需要后续实验。

- link_to_next_phase_cn：直接引出结论和未来工作，提出需要将输入模式和对话主动性作为因素进行分解实验。

##### evidence_pointers

1. Section 4.2.5

2. Section 5

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. LIMITATION

3. RQ_OR_OBJECTIVE

4. STUDY_OVERVIEW

5. RESULT

6. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PRIOR_KNOWLEDGE

4. LIMITATION

5. PHENOMENON

6. RQ_OR_OBJECTIVE

7. STUDY_OVERVIEW

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. MECHANISM

4. REQUIREMENT

5. METHOD_JUSTIFICATION

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. MECHANISM

4. METHOD_JUSTIFICATION

5. PHENOMENON

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. HYPOTHESIS_OR_PROPOSITION

5. RESULT

6. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. RESULT

2. BOUNDARY_CONDITION

3. CONTRIBUTION

4. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 模块化Goal-Oriented对话系统架构（Williams et al., Dodge et al.）

2. 已有CoRS系统与关于自然语言是否有益的矛盾观点（ACORN vs Jannach et al.）

3. 用户中心评价框架ResQue及推荐系统UX设计指南（Pu et al.）

4. PageRank with Priors和LOD解释推荐方法（Haveliwala; Musto et al.）

- 理论—设计耦合：partial

- 耦合判定理由：模块化对话架构和用户中心评价框架影响了系统架构和评价变量，但具体技术选择如自定义Entity Recognizer、Wikidata、Personalized PageRank、三种交互模式主要来自工程启发式和已有系统经验，并非由行为理论或形式模型直接推导；理论更多用于解释和事后定位。

- 理论到设计翻译链：模块化对话系统知识要求系统分为可替换的NLU/状态/策略/生成模块，因此ConveRSE被设计成五个组件；为了评价各组件，又设计Upper bound和单组件测试。已有CoRS关于NL效果矛盾，转化为需要同时实现NL、按钮、混合三种交互模式，并用按钮作控制条件。ResQue用户中心框架将评价从纯准确率扩展到交互成本和感知质量，因此用户研究采用NQ/IT/TPQ/QD以及ResQue问卷。PageRank与解释算法为推荐和交互提供基础能力，但由于三种模式使用同一算法，用户研究可直接归因于交互模式差异。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：模块化Goal-Oriented对话系统由NLU、Dialog State Tracker、Dialog Policy、NLG组成；端到端系统虽简洁但需要大量训练数据。

- mechanism_cn：模块化可使每个环节独立开发、替换和测试，便于定位错误来源。

- design_requirement_cn：ConveRSE应采用模块化架构，使组件可独立评价并适配新领域。

- artifact_choice_cn：Dialog Manager、Intent Recognizer、Sentiment Analyzer、Entity Recognizer、Recommendation Services五个组件。

- evaluated_contrast_cn：Upper bound vs Intent Test vs Entity Test vs Sentiment Test。

- objective_result_cn：bAbI上Entity在HR@5损失58.21%，Intent在HR@100损失21.11%；ConvRecSys上Sentiment损失3–4%最大。

##### evidence_pointers

1. Section 2 paragraphs on modular/end-to-end

2. Section 3 first paragraphs

3. Section 4.1.2

4. Tables 1 and 2

#### 2. 2

- theory_or_knowledge_claim_cn：CoRS中NL可能带来自然性，但也可能增加用户负担（Jannach et al.）；ACORN等系统表明NL能实现高效对话。

- mechanism_cn：NL让用户自由表达多个偏好，但需要精确输入时（如消歧）可能成为负担。

- design_requirement_cn：需要系统比较纯NL、无NL和部分NL，以测量NL的真实效应。

- artifact_choice_cn：Buttons、NL-only、Mixed三种交互模式；Mixed只在消歧时用按钮。

- evaluated_contrast_cn：同域被试内使用三种模式，比较NQ/IT/TPQ/QD/Accuracy/MAP。

- objective_result_cn：Buttons NQ最高，NL TPQ/IT较慢，Mixed在多数指标上最佳或与最优无显著差异。

##### evidence_pointers

1. Section 2 related work

2. Section 3.2

3. Tables 3 and 4

4. Section 4.2.3

#### 3. 3

- theory_or_knowledge_claim_cn：推荐系统评价应超越准确率，纳入用户努力、解释、多样性、可交互性等用户体验（Pu et al., Konstan & Riedl）。

- mechanism_cn：用户感知的易用性、透明度和满意度会影响推荐系统整体有效性。

- design_requirement_cn：评价指标除了客观准确率，还要包含交互成本与用户主观问卷。

- artifact_choice_cn：NQ/IT/TPQ/QD客观交互成本指标，以及基于ResQue问卷的主观评价。

- evaluated_contrast_cn：三种交互模式在三个领域上的问卷回答与客观指标。

- objective_result_cn：问卷中位数普遍为Agree；三个领域MANOVA均未发现模式间问卷显著差异；Q22显示用户普遍认为系统正确理解偏好。

##### evidence_pointers

1. Section 2 ResQue discussion

2. Section 4.2.1

3. Section 4.2.4

#### 4. 4

- theory_or_knowledge_claim_cn：PageRank with Priors可在实体图上进行个性化推荐；LOD解释可基于偏好与推荐项的路径生成解释。

- mechanism_cn：用户偏好实体作为种子，图上传播权重以生成推荐；推荐路径用于解释和critiquing反馈。

- design_requirement_cn：推荐服务应使用可解释的图推荐并提供critiquing能力。

- artifact_choice_cn：Personalized PageRank实现Recommendation Services；解释算法；critiquing功能。

- evaluated_contrast_cn：图算法本身不是交互模式比较中的变量；Upper bound与组件测试都使用相同推荐图。

- objective_result_cn：用户研究结果中模式间差异不能归因于推荐算法，因为三者算法相同。

##### evidence_pointers

1. Section 3 Recommendation Services

2. Section 4.2.2 accuracy result interpretation

## 评价逻辑

### evaluation_modes

1. 合成数据集上的组件消融评价

2. 真实用户被试内交互模式比较

3. 基于ResQue问卷的主观体验评价

4. 统计假设检验与多重比较校正

5. 用户子群与指标相关性的深挖分析

6. 真实对话数据集发布

- why_these_evaluations_cn：组件级问题需要隔离变量，所以用Upper bound与单组件测试在合成数据上消融；交互成本和用户体验问题无法由合成数据回答，所以用真实用户被试内实验比较三种模式；为了把判断从研究者主观视角扩展到用户感知，加入ResQue问卷；为了确认差异的稳定性，使用MANOVA和Mann-Whitney并校正多重比较；最后通过对日志的子群和相关分析解释Mixed为何有效。

- benchmark_and_contrast_chain_cn：先以Upper bound建立理想组件基准，组件测试生成损失；随后在用户研究中以Buttons作为传统交互的控制条件，NL作为纯自然语言条件，Mixed作为仅在消歧点加入按钮的变体；通过比较Mixed与NL，消歧环节被锁定为唯一差异，再通过多领域复制判断结论的跨域可靠性。

### claim_evidence_ledger

1. 组件影响主张：Entity Recognizer在bAbI上HR@5损失最大，证据是Table 1和ER约85%准确率。

2. 领域差异主张：ConvRecSys上Sentiment损失最大，证据是Table 2和更复杂的正负评分解释。

3. Mixed模式优势主张：用户研究中Mixed在Accuracy/MAP、IT等指标上最好或与最好无显著差异，证据是Tables 3–4与Mann-Whitney结果。

4. 消歧负担机制主张：Mixed与NL的唯一区别是消歧用按钮，而Mixed显著更好，证据是交互模式设计和统计比较。

5. 冷启动边界主张：组件识别误差在偏好较少时影响更大，证据是bAbI极端冷启动下的损失模式。

6. 用户满意主张：问卷中位数为Agree，证据是问卷汇总；但MANOVA未发现模式间差异，因此不能声称某一模式主观更优。

7. 数据集贡献主张：收集约6500条NL和2800条Mixed真实对话并公开，证据是Section 5和引用的数据集论文。

- internal_validity_strategy_cn：组件消融中所有非目标组件由程序提供正确答案，避免相互污染；用户研究中同一算法、同一交互系统，只有交互模式变化；被试内设计并在实验前练习以减少顺序效应；统计上使用MANOVA、Mann-Whitney和Bonferroni校正；Q22将系统展示的用户画像与用户表达偏好对照，检验系统理解是否准确。

- external_validity_strategy_cn：在电影、图书、音乐三个领域重复用户研究；合成评价使用两个不同来源的数据集；不同参与者群体（每组50余人）；公开对话数据集为其他研究者提供真实交互材料；但参与者来自同一实验环境，且未测试语音交互或真实DA集成。

- what_is_not_actually_tested_cn：没有在Amazon Alexa/Siri等真实数字助手上部署；没有与端到端对话模型比较；没有单独检验偏好获取步骤与推荐展示步骤的独立效应；QD与效率关系的解释仅为相关推测；语音交互仅作为未来工作提出；ResQue问卷虽然在三个模式间无显著差异，但文章以中位数Agree说明整体满意，这并未直接验证模式间主观优劣。

## 贡献闭环

- technical_claim_cn：ConveRSE是可在多个领域配置的模块化CoRS框架，提供NL/Buttons/Mixed三种交互模式，并采用Wikidata实体链接、Personalized PageRank、解释和critiquing功能；还发布了第一个真实CoRS对话数据集。

- artifact_claim_cn：Mixed交互模式是三种模式中最稳定的选择：在交互成本和推荐准确率上从不差于其他模式，且在多数情况下显著更好；按钮模式需大量系统提问，纯NL模式在消歧任务上负担较重。

- mechanism_claim_cn：消歧是NL交互的主要瓶颈；当用户在预定义选项中做出精确选择时，按钮能降低认知负担和输入成本；实体识别准确率在用户偏好少时对推荐质量影响最大，因此冷启动下需要更精准的偏好理解。

- boundary_claim_cn：结论在电影、图书、音乐三个领域和约50–55人的被试组中成立；低领域兴趣用户在Mixed下的改善更明显；组件影响在偏好数量充足时减弱，在冷启动或少量偏好条件下最突出。

- reusable_design_knowledge_cn：纯NL界面不应完全取代传统交互要素，至少应在需要从固定集合中选择的环节提供按钮辅助；建模NL对话时应先识别用户高负担活动；冷启动下应优先保证实体/情绪识别精度，必要时用额外询问换取准确理解。

- theoretical_contribution_cn：文章没有提出新形式理论，但对“自然语言是否有利于CoRS”的争论给出经验证据，将现有模块化对话架构、用户中心评价框架和已有CoRS观点连接为一个可检验的框架，并限定了NL优势的边界条件。

- how_discussion_closes_intro_gap_cn：引言指出“自然语言提升体验”是直觉但未被系统验证，且已有研究对NL持相反看法；结论通过实验结果说明纯NL并不稳定更好，混合模式才稳定更好，并解释按钮在消歧中的作用，从而回应四个RQ并闭合“缺少NL对UX与准确率影响的广泛研究”这一缺口。

- overclaim_or_unsupported_leaps_cn：“Mixed模式让用户更有效地表达偏好”有推测成分，虽然算法相同，但并未直接测量表达效率；QD与IT的相关分析被作者自己限定为需要进一步实验；声称‘first dataset based on real data’可能有时间性风险；用户问卷无显著差异却以中位数Agree代表整体满意，不能排除问卷区分度不足；组件消融中的因果解释依赖组件准确率与损失的关联，而非直接操纵组件误差的随机实验。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：数字助手正因能通过自然语言完成多种操作而广泛普及。

- rhetorical_function_cn：为文章设定应用背景，说明现象的重要性。

- depends_on_cn：无需依赖前文。

- sets_up_cn：引出数字助手仍缺少推荐功能这一限制。

- evidence_pointer：Abstract first sentence

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：LIMITATION

- paraphrase_cn：尽管数字助手能发短信、打电话、放歌，但没有实现推荐能力。

- rhetorical_function_cn：建立现实能力与潜在需求之间的缺口。

- depends_on_cn：数字助手的普及使缺口具有现实影响。

- sets_up_cn：为将DA与CoRS结合提供动机。

- evidence_pointer：Abstract second sentence

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文通过设计和实现ConveRSE框架来研究DA与CoRS的结合。

- rhetorical_function_cn：在摘要中直接给出核心研究对象和制品。

- depends_on_cn：前一限制使结合研究成为必要。

- sets_up_cn：为后续实验简介提供目标。

- evidence_pointer：Abstract third sentence

### 4. Abstract P1 S4

- order：4

- section：Abstract

- locator：Abstract P1 S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：由于CoRS由多个组件构成，用两个合成数据集做体外实验观察各组件对推荐准确率的影响。

- rhetorical_function_cn：预告第一种评价方式并说明原因。

- depends_on_cn：框架的模块化设计使组件级评价成为可能。

- sets_up_cn：为Section 4.1的内容做摘要级预告。

- evidence_pointer：Abstract fourth sentence

### 5. Abstract P1 S5

- order：5

- section：Abstract

- locator：Abstract P1 S5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：另做了体内实验以理解自然语言如何影响交互成本和推荐准确率。

- rhetorical_function_cn：介绍第二类评价并指出关注变量。

- depends_on_cn：合成数据无法回答用户体验问题。

- sets_up_cn：为Section 4.2用户研究做预告。

- evidence_pointer：Abstract fifth sentence

### 6. Abstract P1 S6

- order：6

- section：Abstract

- locator：Abstract P1 S6

- move_code：RESULT

- paraphrase_cn：实验发现了CoRS架构中最关键的组件，尤其冷启动时的表现，以及自然语言交互的主要问题。

- rhetorical_function_cn：用一句话概括核心经验发现。

- depends_on_cn：两种实验都完成后才能得到该结论。

- sets_up_cn：使读者预期设计启示而非单纯算法比较。

- evidence_pointer：Abstract sixth sentence

### 7. Abstract P1 S7

- order：7

- section：Abstract

- locator：Abstract P1 S7

- move_code：CONTRIBUTION

- paraphrase_cn：所有对话被收集并公开为数据集。

- rhetorical_function_cn：增加资源性贡献，强化开放性。

- depends_on_cn：用户研究确实产生了可复用日志。

- sets_up_cn：为Section 5数据集说明埋伏笔。

- evidence_pointer：Abstract final sentence

### 8. Introduction P1 S1

- order：8

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：数字助手通过自然语言帮助用户完成记事、订票、查信息等日常任务。

- rhetorical_function_cn：扩展摘要中的背景，使读者进入DA场景。

- depends_on_cn：无需前文。

- sets_up_cn：后续讨论DA从手机转向汽车和智能家居。

- evidence_pointer：Introduction opening sentence

### 9. Introduction P2 S2

- order：9

- section：Introduction

- locator：Introduction P2 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：数字助手最常见的用途之一是寻找新的媒体内容，因此适合集成CoRS。

- rhetorical_function_cn：将一般背景收缩到推荐场景，说明DA与推荐结合的现实价值。

- depends_on_cn：DA普及和媒体发现需求。

- sets_up_cn：为介绍CoRS概念做铺垫。

- evidence_pointer：Introduction P2

### 10. Introduction P2 S3

- order：10

- section：Introduction

- locator：Introduction P2 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：CoRS的特点是在推荐过程中能够与用户交互。

- rhetorical_function_cn：给出CoRS的领域定义。

- depends_on_cn：推荐场景已经建立。

- sets_up_cn：说明CoRS为何适合无传统界面的环境。

- evidence_pointer：Introduction P2

### 11. Introduction P2 S4

- order：11

- section：Introduction

- locator：Introduction P2 S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：CoRS与传统推荐系统不同，不要求用户一次提供全部信息，而是用类人对话引导用户。

- rhetorical_function_cn：突出CoRS的核心差异。

- depends_on_cn：CoRS定义。

- sets_up_cn：为自然语言交互的必要性提供理由。

- evidence_pointer：Introduction P2

### 12. Introduction P3 S1

- order：12

- section：Introduction

- locator：Introduction P3 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文提出领域无关、可配置的CoRS框架ConveRSE。

- rhetorical_function_cn：第一次正式提出制品。

- depends_on_cn：DA缺少推荐能力、CoRS适合该场景。

- sets_up_cn：随后说明框架使用的交互机制。

- evidence_pointer：Introduction P3

### 13. Introduction P3 S2

- order：13

- section：Introduction

- locator：Introduction P3 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：ConveRSE使用自然语言、按钮以及二者结合的交互机制。

- rhetorical_function_cn：给出框架的关键设计选择。

- depends_on_cn：ConveRSE作为框架的定位。

- sets_up_cn：为RQ1/RQ2中的交互模式比较提供对象。

- evidence_pointer：Introduction P3

### 14. Introduction P3 S3

- order：14

- section：Introduction

- locator：Introduction P3 S3

- move_code：PHENOMENON

- paraphrase_cn：开发ConveRSE是为了理解自然语言如何影响CoRS的准确率和用户体验质量。

- rhetorical_function_cn：把制品构建与经验研究目标绑定。

- depends_on_cn：三种交互机制已经设计。

- sets_up_cn：解释为什么需要用户研究和准确率指标。

- evidence_pointer：Introduction P3

### 15. Introduction P4 S1

- order：15

- section：Introduction

- locator：Introduction P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：文章列出四个研究问题，涉及交互成本、推荐质量、各组件影响和NL对话建模关键点。

- rhetorical_function_cn：将研究定位成可检验的问题集。

- depends_on_cn：此前背景和框架目标。

- sets_up_cn：为实验设计提供显式检查表，结尾逐题回答。

- evidence_pointer：Introduction P4

### 16. Introduction P5 S1

- order：16

- section：Introduction

- locator：Introduction P5 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在bAbI和ConvRecSys两个合成数据集上做体外实验，评估整体准确率和组件影响，并用ResQue问卷评估用户满意度。

- rhetorical_function_cn：在进入正文前概述评价计划。

- depends_on_cn：RQ列表。

- sets_up_cn：为Section 4.1和4.2的结构做总体预告。

- evidence_pointer：Introduction final paragraph

### 17. Related work P1 S1

- order：17

- section：Related work

- locator：Related work P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：CoRS通过改变用户输入偏好和接收推荐的方式，克服传统推荐系统的限制。

- rhetorical_function_cn：重述CoRS的领域价值。

- depends_on_cn：已在引言中给定CoRS概念。

- sets_up_cn：引出后续相关系统的比较。

- evidence_pointer：Section 2 opening

### 18. Related work P2 S4

- order：18

- section：Related work

- locator：Related work P2 S4

- move_code：LIMITATION

- paraphrase_cn：Rafailidis和Manolopoulos指出虚拟助手与推荐系统之间的技术鸿沟，并认为VA能学习用户多变多维偏好。

- rhetorical_function_cn：引用前人观点确认DA+CoRS结合的正当性。

- depends_on_cn：前文模块化架构讨论。

- sets_up_cn：说明ConveRSE所要弥补的正是这一技术鸿沟。

- evidence_pointer：Related work P2

### 19. Related work P3 S1

- order：19

- section：Related work

- locator：Related work P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：构建对话智能体有两种主要架构：模块化和端到端。

- rhetorical_function_cn：建立架构选择的知识基础。

- depends_on_cn：将DA视为Goal-Oriented CA。

- sets_up_cn：为选择模块化架构做铺垫。

- evidence_pointer：Related work P3

### 20. Related work P3 S5

- order：20

- section：Related work

- locator：Related work P3 S5

- move_code：LIMITATION

- paraphrase_cn：端到端系统需要很难获得的大规模训练数据，这是采用模块化架构的原因之一。

- rhetorical_function_cn：用端到端的局限为本文架构辩护。

- depends_on_cn：端到端系统介绍。

- sets_up_cn：后续Section 3中的模块化设计。

- evidence_pointer：Related work P3

### 21. Related work P4 S1

- order：21

- section：Related work

- locator：Related work P4 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：ACORN是电影域CoRS，用NL对话获取偏好、回答问题并提供带动机的个性化推荐，用户研究支持其效率与满意度。

- rhetorical_function_cn：提供正面证据说明NL对话可行。

- depends_on_cn：已有CoRS研究传统。

- sets_up_cn：与Jannach的负面观点形成对照，构建缺口。

- evidence_pointer：Related work P4

### 22. Related work P4 S3

- order：22

- section：Related work

- locator：Related work P4 S3

- move_code：GAP

- paraphrase_cn：本文扩展ACORN式研究，在不同领域测量NL对对话效率和推荐准确率的影响。

- rhetorical_function_cn：从正面案例转向本文的增量空间。

- depends_on_cn：ACORN的工作。

- sets_up_cn：为多领域用户研究提供理由。

- evidence_pointer：Related work P4

### 23. Related work P5 S1

- order：23

- section：Related work

- locator：Related work P5 S1

- move_code：GAP

- paraphrase_cn：Goker和Thompson使用NL界面，而Jannach等不使用，且后者认为NL可能阻碍对话持续；本文要检验这些主张。

- rhetorical_function_cn：把已有矛盾观点作为研究缺口。

- depends_on_cn：两类基于约束满足的CoRS。

- sets_up_cn：引出RQ1/RQ2对NL效应的检验。

- evidence_pointer：Related work P5

### 24. Related work P6 S3

- order：24

- section：Related work

- locator：Related work P6 S3

- move_code：GAP

- paraphrase_cn：Mori比较了系统主动和用户主动的展示策略，而本文关注偏好获取阶段，并将NL界面与其他交互模式比较。

- rhetorical_function_cn：进一步精确化本文与已有研究的差异。

- depends_on_cn：Mori et al.的界面比较。

- sets_up_cn：说明为什么需要三种交互模式而非仅比较展示细节。

- evidence_pointer：Related work P6

### 25. Related work P7 S3

- order：25

- section：Related work

- locator：Related work P7 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：本文NL对话模型部分受Moore启发，具有可请求细节或解释的推荐序列，以及跟踪会话的对话状态。

- rhetorical_function_cn：说明对话模型并非从零设计，而有关联基础。

- depends_on_cn：前述CoRS系统。

- sets_up_cn：为架构中Dialog Manager和解释功能提供来源。

- evidence_pointer：Related work P7

### 26. Related work P8 S1

- order：26

- section：Related work

- locator：Related work P8 S1

- move_code：LIMITATION

- paraphrase_cn：传统推荐评价指标只能判断推荐是否相关，无法体现新颖性、有用性和获取难度。

- rhetorical_function_cn：提出采用用户中心评价的必要性。

- depends_on_cn：已有推荐评估指标。

- sets_up_cn：为ResQue问卷和交互成本指标做铺垫。

- evidence_pointer：Related work P8

### 27. Related work P10 S2

- order：27

- section：Related work

- locator：Related work P10 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Pu等给出了良好RS的设计指南，包括减少用户努力、提供解释、多样推荐和允许用户细化偏好。

- rhetorical_function_cn：把用户中心设计准则引入知识基础。

- depends_on_cn：UX评价文献。

- sets_up_cn：为ConveRSE的解释、critiquing和混合交互功能提供理论正当性。

- evidence_pointer：Related work P10

### 28. Related work P11 S1

- order：28

- section：Related work

- locator：Related work P11 S1

- move_code：GAP

- paraphrase_cn：已有若干工作分析了CoRS的不同方面，但没有大规模研究自然语言对CoRS用户体验和准确率的影响。

- rhetorical_function_cn：这是全局缺口的正式表述。

- depends_on_cn：前文所有相关工作。

- sets_up_cn：为本文研究目标和RQ作对照。

- evidence_pointer：Related work final summary paragraph

### 29. Related work P11 S2

- order：29

- section：Related work

- locator：Related work P11 S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文旨在通过突出CoRS架构中的关键组件和用户交互中的关键步骤来弥合这一缺口。

- rhetorical_function_cn：明确文章在文献中的定位。

- depends_on_cn：缺口表述。

- sets_up_cn：承诺同时贡献组件级和交互级发现。

- evidence_pointer：Related work final summary paragraph

### 30. Section 3 opening P2 S1

- order：30

- section：Section 3

- locator：Section 3 opening P2 S1

- move_code：REQUIREMENT

- paraphrase_cn：ConveRSE采用槽填充交互模型，需要若干特征被填充以完成用户目标，推荐需先获取最小偏好集，因此至少需要五个组件。

- rhetorical_function_cn：将推荐过程需求转换为具体组件数量。

- depends_on_cn：推荐过程步骤和CoRS交互特点。

- sets_up_cn：随后逐一定义每个组件。

- evidence_pointer：Section 3 first paragraphs

### 31. Section 3 P3 S1

- order：31

- section：Section 3

- locator：Section 3 P3 S1

- move_code：MECHANISM

- paraphrase_cn：组件和推荐步骤不是同一回事；组件是交互中的不同时刻，步骤是架构上的不同功能，Dialog Manager负责按序调用组件。

- rhetorical_function_cn：澄清后续消融实验的逻辑基础。

- depends_on_cn：五组件列表。

- sets_up_cn：解释为什么每个组件可单独被测试。

- evidence_pointer：Section 3 P3

### 32. Section 3 Intent Recognizer paragraph

- order：32

- section：Section 3

- locator：Section 3 Intent Recognizer paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：Intent Recognizer识别四种意图：preference、recommendation、show profile、help。

- rhetorical_function_cn：定义第一个NLU组件的具体输出。

- depends_on_cn：模块化架构。

- sets_up_cn：为In-vitro Intent Test提供测试目标。

- evidence_pointer：Section 3 Intent Recognizer

### 33. Section 3 Sentiment Analyzer paragraph

- order：33

- section：Section 3

- locator：Section 3 Sentiment Analyzer paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：Sentiment Analyzer基于CoreNLP情绪标注器，把句子中的情绪标签关联到句中最接近的实体，按token距离计算。

- rhetorical_function_cn：说明情绪与实体关联机制。

- depends_on_cn：NLU组件分解。

- sets_up_cn：为Sentiment Test的误差来源提供机制。

- evidence_pointer：Section 3 Sentiment Analyzer

### 34. Section 3 Entity Recognizer paragraph

- order：34

- section：Section 3

- locator：Section 3 Entity Recognizer paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择自定义Entity Recognizer，因为现有链接算法难定制域，且NLU平台需要标注数据，而基于知识库的方法无需标注。

- rhetorical_function_cn：为关键工程选择辩护。

- depends_on_cn：选择Wikidata作为KB。

- sets_up_cn：为后续Entity Test的误差分析做铺垫。

- evidence_pointer：Section 3 Entity Recognizer

### 35. Section 3 Recommendation Services paragraph

- order：35

- section：Section 3

- locator：Section 3 Recommendation Services paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：推荐服务使用PageRank with Priors，在Wikidata实体图上工作，并提供解释和critiquing功能。

- rhetorical_function_cn：说明推荐算法和附加功能。

- depends_on_cn：实体链接和KB。

- sets_up_cn：让三种交互模式共享同一推荐算法，从而在用户研究中归因于交互模式差异。

- evidence_pointer：Section 3 Recommendation Services

### 36. Section 3.1 running example

- order：36

- section：Section 3.1

- locator：Section 3.1 running example

- move_code：PHENOMENON

- paraphrase_cn：用“I like Ghostbusters, but I hate the director”示例展示偏好获取中组件调用和消歧过程。

- rhetorical_function_cn：具体化抽象架构，让读者看到系统实际工作。

- depends_on_cn：五组件定义。

- sets_up_cn：提出NL交互的主要挑战：消歧。

- evidence_pointer：Section 3.1, Fig. 2

### 37. Section 3.2 opening

- order：37

- section：Section 3.2

- locator：Section 3.2 opening

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架实现三种交互模式：按钮、自然语言和混合，每种用不同域截图展示。

- rhetorical_function_cn：正式引入自变量。

- depends_on_cn：架构运行示例。

- sets_up_cn：为Section 4.2用户研究设计处理条件。

- evidence_pointer：Section 3.2, Figs. 3 and 4

### 38. Section 3.2 Button-based paragraph

- order：38

- section：Section 3.2

- locator：Section 3.2 Button-based paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：按钮交互完全由系统驱动，分偏好获取和推荐两阶段，后续用作用户研究的控制组。

- rhetorical_function_cn：明确按钮模式作为无NL条件的角色。

- depends_on_cn：此前系统的改进。

- sets_up_cn：为“系统驱动vs用户驱动”差异提供结构基础。

- evidence_pointer：Section 3.2 Button-based interaction

### 39. Section 3.2 NL paragraph

- order：39

- section：Section 3.2

- locator：Section 3.2 NL paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：纯NL模式让用户用文本自由表达偏好，每条消息可含多个偏好，消歧时需手写所选实体。

- rhetorical_function_cn：定义NL模式的特殊能力与负担。

- depends_on_cn：NL组件。

- sets_up_cn：与Mixed模式形成唯一差异。

- evidence_pointer：Section 3.2 Natural language-only interaction

### 40. Section 3.2 Mixed paragraph

- order：40

- section：Section 3.2

- locator：Section 3.2 Mixed paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：混合模式与纯NL基本相同，只在消歧时显示按钮选项。

- rhetorical_function_cn：构造近乎完美的对照，使消歧成为唯一区分变量。

- depends_on_cn：纯NL模式设计。

- sets_up_cn：让用户研究可以将Mixed与NL的差异归因于消歧按钮。

- evidence_pointer：Section 3.2 Mixed interaction

### 41. Section 4 opening P1 S1

- order：41

- section：Section 4

- locator：Section 4 opening P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：组织两个实验：体外实验评估组件对推荐准确率的影响，用户研究评估不同交互模式的用户体验。

- rhetorical_function_cn：把评价阶段两分并赋予各自任务。

- depends_on_cn：RQ列表。

- sets_up_cn：为4.1和4.2章节做总纲。

- evidence_pointer：Section 4 opening

### 42. Section 4.1.2 four configurations

- order：42

- section：Section 4.1.2

- locator：Section 4.1.2 four configurations

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：设计Upper bound、Intent Test、Entity Test、Sentiment Test四种配置，使每种配置只真实运行一个组件。

- rhetorical_function_cn：建立组件级消融框架。

- depends_on_cn：模块化架构。

- sets_up_cn：为每个组件的独立影响提供证据。

- evidence_pointer：Section 4.1.2

### 43. Section 4.1.2 after configurations

- order：43

- section：Section 4.1.2

- locator：Section 4.1.2 after configurations

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设是实体识别错误会负面地影响推荐准确率，因此可通过组件测试测量该影响。

- rhetorical_function_cn：把消融实验转化为可解释的因果假设。

- depends_on_cn：组件测试配置。

- sets_up_cn：解释为何Loss可以归因于组件误差。

- evidence_pointer：Section 4.1.2 final

### 44. Section 4.1.3 metrics

- order：44

- section：Section 4.1.3

- locator：Section 4.1.3 metrics

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用HitRate@k和相对Upper bound的损失作为组件影响的度量。

- rhetorical_function_cn：明确合成数据实验的因变量。

- depends_on_cn：Upper bound配置。

- sets_up_cn：让Tables 1和2具有统一比较口径。

- evidence_pointer：Section 4.1.3

### 45. Section 4.1.4 bAbI results first interpretation

- order：45

- section：Section 4.1.4

- locator：Section 4.1.4 bAbI results first interpretation

- move_code：LIMITATION

- paraphrase_cn：bAbI上的推荐任务困难，因为每个对话只有一个正确项且偏好信息很少，处于极端冷启动。

- rhetorical_function_cn：在报告结果前说明数据特殊性。

- depends_on_cn：数据过滤后的 6667/6733 实例。

- sets_up_cn：解释为什么Entity损失特别大。

- evidence_pointer：Section 4.1.4 before Table 1 discussion

### 46. Section 4.1.4 k=5 results

- order：46

- section：Section 4.1.4

- locator：Section 4.1.4 k=5 results

- move_code：RESULT

- paraphrase_cn：k=5时Entity Recognizer损失最大，达到58.21%，Intent第二19.4%，Sentiment约4.5%。

- rhetorical_function_cn：给出最主要数字结果。

- depends_on_cn：Table 1。

- sets_up_cn：随后用组件准确率解释损失来源。

- evidence_pointer：Table 1 and following paragraph

### 47. Section 4.1.4 k=100 results

- order：47

- section：Section 4.1.4

- locator：Section 4.1.4 k=100 results

- move_code：RESULT

- paraphrase_cn：k=100时Intent损失最高，因为错误意图导致不生成推荐，无法受益于更大的k。

- rhetorical_function_cn：展示指标随k变化的非单调原因。

- depends_on_cn：Intent Test生成规则。

- sets_up_cn：强调意图识别引发的系统性损失。

- evidence_pointer：Section 4.1.4 k=100 discussion

### 48. Section 4.1.4 final interpretation

- order：48

- section：Section 4.1.4

- locator：Section 4.1.4 final interpretation

- move_code：RESULT

- paraphrase_cn：实体识别是保证前几个推荐相关性的关键，小实体误差在偏好少时造成很大准确率损失；情绪识别重要但不那么关键。

- rhetorical_function_cn：形成组件级结论。

- depends_on_cn：两个数据集的结果模式。

- sets_up_cn：为RQ3的冷启动回答提供依据。

- evidence_pointer：Section 4.1.4 final and Section 4.1.5

### 49. Section 4.1.4 ConvRecSys results after Table 2

- order：49

- section：Section 4.1.4

- locator：Section 4.1.4 ConvRecSys results after Table 2

- move_code：RESULT

- paraphrase_cn：ConvRecSys上Upper bound明显更高，组件损失更小；Sentiment最大损失约3–4%，Entity约2%，Intent约0.12%。

- rhetorical_function_cn：通过第二个数据集验证并修正组件重要性排序。

- depends_on_cn：Table 2。

- sets_up_cn：提出领域/数据特性对组件影响的条件性结论。

- evidence_pointer：Table 2 and following paragraph

### 50. Section 4.1.5 Discussion

- order：50

- section：Section 4.1.5

- locator：Section 4.1.5 Discussion

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：从体外结果可以推断实体识别在冷启动、偏好数量有限时是保证早期推荐相关性的关键步骤。

- rhetorical_function_cn：将两个数据集的差异收敛为适用范围判断。

- depends_on_cn：两个数据集的综合结果。

- sets_up_cn：为Conclusion中关于额外确认反馈的建议做铺垫。

- evidence_pointer：Section 4.1.5

### 51. Section 4.2 opening P1 S1

- order：51

- section：Section 4.2

- locator：Section 4.2 opening P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：设计了三个独立的被试内实验，在电影、图书、音乐三个域比较不同交互模式对准确率和交互成本的影响。

- rhetorical_function_cn：说明用户研究的基本设计与领域选择理由。

- depends_on_cn：三种交互模式和组件结论。

- sets_up_cn：为参与者数和域实例构建提供上下文。

- evidence_pointer：Section 4.2 opening

### 52. Section 4.2 P2 S1

- order：52

- section：Section 4.2

- locator：Section 4.2 P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验前让用户熟悉系统，以减少不同配置的顺序效应。

- rhetorical_function_cn：说明内部有效性保护措施。

- depends_on_cn：被试内设计。

- sets_up_cn：提高统计比较的可信度。

- evidence_pointer：Section 4.2 second paragraph

### 53. Section 4.2.1 metrics

- order：53

- section：Section 4.2.1

- locator：Section 4.2.1 metrics

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：采用Accuracy和MAP评价推荐质量，采用NQ、IT、TPQ、QD评价交互成本。

- rhetorical_function_cn：定义用户研究两组成果指标。

- depends_on_cn：RQ1/RQ2需要成本和准确率。

- sets_up_cn：为Tables 3和4提供指标列。

- evidence_pointer：Section 4.2.1

### 54. Section 4.2.2 after Table 3

- order：54

- section：Section 4.2.2

- locator：Section 4.2.2 after Table 3

- move_code：RESULT

- paraphrase_cn：按钮模式提问数明显高，NL模式TPQ和IT通常更长，Mixed模式时间更低或相当；消歧是NL最繁重的部分。

- rhetorical_function_cn：给出交互成本结果并首次解释机制。

- depends_on_cn：Table 3。

- sets_up_cn：为Mixed优于NL提供机制解释。

- evidence_pointer：Section 4.2.2 after Table 3

### 55. Section 4.2.2 after Table 4

- order：55

- section：Section 4.2.2

- locator：Section 4.2.2 after Table 4

- move_code：RESULT

- paraphrase_cn：准确率指标中Mixed最好；由于算法相同，结果归因于用户能通过混合方式更有效地表达偏好。

- rhetorical_function_cn：把准确率差异从算法效应中分离出来。

- depends_on_cn：Table 4和交互模式共享算法。

- sets_up_cn：支持Mixed模式优于纯NL的结论。

- evidence_pointer：Section 4.2.2 after Table 4

### 56. Section 4.2.3 statistical tests

- order：56

- section：Section 4.2.3

- locator：Section 4.2.3 statistical tests

- move_code：RESULT

- paraphrase_cn：MANOVA在三个域都拒绝原假设，Mann-Whitney显示Mixed在交互成本上显著优于NL和Buttons；纯NL需要按钮支持，混合模式最差也不差于其他模式。

- rhetorical_function_cn：将描述性差异提升为统计显著结论。

- depends_on_cn：表3–4和配对检验。

- sets_up_cn：为RQ1/RQ2的正式回答提供统计基础。

- evidence_pointer：Section 4.2.3

### 57. Section 4.2.4 questionnaire results

- order：57

- section：Section 4.2.4

- locator：Section 4.2.4 questionnaire results

- move_code：RESULT

- paraphrase_cn：问卷各题中位数通常为Agree，整体用户满意；但MANOVA未发现三模式间显著差异。

- rhetorical_function_cn：报告主观体验评价，避免过度宣称模式差异。

- depends_on_cn：ResQue问卷结果。

- sets_up_cn：与客观指标结果形成对照，说明客观差异未必转化为主观差异。

- evidence_pointer：Section 4.2.4

### 58. Section 4.2.4 Q22 discussion

- order：58

- section：Section 4.2.4

- locator：Section 4.2.4 Q22 discussion

- move_code：RESULT

- paraphrase_cn：Q22询问用户画像是否与表达偏好一致，回答为Agree到Strongly Agree，说明系统在三种模式下都较准确理解了偏好。

- rhetorical_function_cn：用用户确认机制检验系统语句理解的有效性。

- depends_on_cn：系统展示用户画像后的问卷题。

- sets_up_cn：支持将准确率差异归因于交互本身而非误解。

- evidence_pointer：Section 4.2.4 Q22 paragraph

### 59. Section 4.2.5 subgroup analysis

- order：59

- section：Section 4.2.5

- locator：Section 4.2.5 subgroup analysis

- move_code：RESULT

- paraphrase_cn：按计算机经验和领域兴趣分组后发现，Mixed大幅降低低兴趣用户的IT和TPQ，说明消歧任务对不熟悉实体用户尤其沉重。

- rhetorical_function_cn：补充边界条件，解释Mixed优势的机制。

- depends_on_cn：问卷Q4/Q6和日志。

- sets_up_cn：为RQ4关于关键建模方面提供答案。

- evidence_pointer：Section 4.2.5

### 60. Section 4.2.5 correlation analysis

- order：60

- section：Section 4.2.5

- locator：Section 4.2.5 correlation analysis

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：QD与IT的负相关提示NL界面可能允许用户每轮提供更多概念从而提高效率，但这只是推测，需进一步实验确认。

- rhetorical_function_cn：提出一个开放假设而非最终结论。

- depends_on_cn：Pearson相关系数。

- sets_up_cn：为未来研究指明方向。

- evidence_pointer：Section 4.2.5 final

### 61. Section 4.3 RQ1 answer

- order：61

- section：Section 4.3

- locator：Section 4.3 RQ1 answer

- move_code：RESULT

- paraphrase_cn：纯NL界面在需要精确输入时存在障碍；在这些薄弱点加入按钮支持后，NL能使交互更高效。

- rhetorical_function_cn：正式回答RQ1，避免简单肯定或否定NL。

- depends_on_cn：用户研究结果。

- sets_up_cn：为设计建议提供依据。

- evidence_pointer：Section 4.3 RQ1

### 62. Section 4.3 RQ2 answer

- order：62

- section：Section 4.3

- locator：Section 4.3 RQ2 answer

- move_code：RESULT

- paraphrase_cn：纯NL并未稳定优于按钮，而Mixed从不差于其他模式且多数时候更好。

- rhetorical_function_cn：直接回答推荐质量层面的RQ2。

- depends_on_cn：Accuracy/MAP统计结果。

- sets_up_cn：支持混合交互作为推荐系统的稳妥设计。

- evidence_pointer：Section 4.3 RQ2

### 63. Section 4.3 RQ3 answer

- order：63

- section：Section 4.3

- locator：Section 4.3 RQ3 answer

- move_code：RESULT

- paraphrase_cn：实体和情绪识别准确率对推荐质量影响大，且偏好越多影响越小，因此冷启动时识别更关键。

- rhetorical_function_cn：将两个数据集的组件消融结论浓缩为RQ3答案。

- depends_on_cn：Tables 1–2。

- sets_up_cn：为结论中的冷启动建议提供依据。

- evidence_pointer：Section 4.3 RQ3

### 64. Section 4.3 RQ4 answer

- order：64

- section：Section 4.3

- locator：Section 4.3 RQ4 answer

- move_code：RESULT

- paraphrase_cn：建模NL对话时应先识别用户最困难的活动；在CoRS中，从一组预定义选项中选择就是这种活动，因此应加以简化。

- rhetorical_function_cn：把实验结果转化为可操作的NL对话设计要点。

- depends_on_cn：用户研究和子群分析。

- sets_up_cn：为结论中“按钮辅助消歧”设计知识做铺垫。

- evidence_pointer：Section 4.3 RQ4

### 65. Section 5 dataset paragraph

- order：65

- section：Section 5

- locator：Section 5 dataset paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：收集了约6500条NL和2800条Mixed真实用户消息，包含用户ID、消息、时间戳、意图和带情绪的实体，并匿名公开。

- rhetorical_function_cn：明确提出可复用资源贡献。

- depends_on_cn：用户研究产生的日志。

- sets_up_cn：增强论文的可复现性和社区价值。

- evidence_pointer：Section 5

### 66. Conclusion P1 S3

- order：66

- section：Conclusion

- locator：Conclusion P1 S3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：用户研究显示纯NL界面需要传统交互策略支持；当用户必须在选项集中选择时，按钮加入能显著改善交互，这对语音系统也有启示。

- rhetorical_function_cn：将核心经验发现固化为设计知识。

- depends_on_cn：RQ1/RQ2答案。

- sets_up_cn：为未来基于语音的DA设计提出可操作建议。

- evidence_pointer：Conclusion P1

### 67. Conclusion P2 S1

- order：67

- section：Conclusion

- locator：Conclusion P2 S1

- move_code：RESULT

- paraphrase_cn：合成数据实验表明实体和情绪识别在用户表达偏好很少时起关键作用，此时应尽量精确理解用户，即使需要额外询问。

- rhetorical_function_cn：重申组件消融结论并附加设计含义。

- depends_on_cn：Tables 1–2和RQ3答案。

- sets_up_cn：为未来减少消歧请求的研究目标做铺垫。

- evidence_pointer：Conclusion P2

### 68. Conclusion P3 S1

- order：68

- section：Conclusion

- locator：Conclusion P3 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来需要隔离交互的每个方面，设计包含输入模式和对话主动性的因子实验，并研究语音扩展。

- rhetorical_function_cn：诚实指出当前实验无法分离所有因素，并为后续研究画路线。

- depends_on_cn：当前研究整体局限。

- sets_up_cn：结束全文并开放后续问题。

- evidence_pointer：Conclusion P3

## 写作技术

- gap_construction_cn：先用数字助手缺少推荐功能的现实缺口切入，再指出VA与RS间的技术鸿沟，进而引用已有CoRS研究中关于NL是否有益的矛盾观点，最后明确表述“没有广泛研究自然语言对CoRS UX与准确率影响”的文献缺口。

- signposting_cn：在引言末尾列出RQ1–RQ4；在实验章节开头明确哪个实验回答哪些RQ；在4.3节逐条回答RQ；在架构和使用模式部分用“Fig. 1”“Fig. 2”“Figs. 3–4”作为可视化路标。

- transition_logic_cn：从相关工作中的矛盾观点过渡到“因此本文要检验”；从架构组件清单过渡到“因此可做组件消融”；从合成数据结果过渡到“还需真实用户”；从用户研究结果过渡到“深入分析日志”；最后以RQ答案串联各阶段。

- claim_evidence_rhythm_cn：每个主要结论后紧跟表格或统计检验，并使用组件准确率解释损失；描述性结果之后立即用MANOVA/Mann-Whitney确认显著性；对不能直接支持的推测（如QD效率）明确标注为有待验证。

- benchmark_narrative_cn：先以Upper bound作为理想基准，组件测试产生损失；用户研究把Buttons作为传统控制组，Mixed作为只修改消歧环节的NL变体；这样消歧按钮被构建成唯一的差异来源，随后统计检验把描述性优势提升为稳定结论。

- theory_return_cn：虽然没有形式理论，但讨论不断回到已有对话系统架构和用户中心评价框架：用模块化架构解释为何能做组件消融，用ResQue框架解释为何问卷题项能代表用户体验，用已有“NL有碍对话”观点反衬出“纯NL需按钮辅助”的修正性结论。

- contribution_positioning_cn：将贡献同时定位为框架制品、组件级知识、交互模式比较和数据集资源，避免只依赖单次用户实验结果；在结论和摘要中反复强调多领域验证与公开数据，增加贡献的稳健性。

- novelty_protection_cn：通过在三个领域重复用户实验、用真实日志形成公开数据集、采用组件级消融而非端到端比较、以及将结论表述为“混合模式最差也不差、最好则更好”的保守方式，防止贡献被还原为某一次性能数字。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实场景和文献缺口，明确RQ；写摘要时先给背景再给缺口的简短版。

- research_job_cn：调研DA/CoRS现状，找出矛盾观点，提炼可检验问题。

- required_evidence_cn：能够说明数字助手缺少推荐能力，并给出至少一组关于NL效果不一致的已有研究。

- transition_to_next_cn：用“因此本文提出/研究…”过渡到框架提案。

#### 2. 2

- step：2

- writing_job_cn：描述制品架构、组件、交互模式和运行示例；写作时先给模块清单再给示例。

- research_job_cn：构建可配置、模块化的CoRS，并实现三种交互模式。

- required_evidence_cn：系统可运行的部分；最好有架构图和对话截图。

- transition_to_next_cn：从组件清单引出“每个组件如何影响推荐准确率”的问题。

#### 3. 3

- step：3

- writing_job_cn：设计合成数据上的四配置消融，定义Upper bound和单组件测试，报告HitRate损失。

- research_job_cn：在两个合成数据集上运行Upper bound、Intent/Entity/Sentiment测试，记录组件准确率和推荐损失。

- required_evidence_cn：至少一个基准和一个单组件测试的结果，展示损失模式。

- transition_to_next_cn：说明合成数据无法回答用户体验问题，因此需要真实用户研究。

#### 4. 4

- step：4

- writing_job_cn：报告被试内用户研究：领域、参与者、三种模式、交互成本和准确率指标、问卷、统计检验。

- research_job_cn：在同一域内让同一群用户测试三种模式，记录客观日志和主观问卷。

- required_evidence_cn：三个模式的客观指标和主观问卷数据；至少一组统计显著差异。

- transition_to_next_cn：通过RQ答案或日志深挖解释“为什么某模式更好”。

#### 5. 5

- step：5

- writing_job_cn：做子群和相关性分析，将结果升华为设计建议，并列出限制与未来实验。

- research_job_cn：利用问卷和日志数据分组检验机制，计算指标相关，形成边界条件。

- required_evidence_cn：子群差异或相关值；如果只能推测，则明确标注为假设。

- transition_to_next_cn：发布资源或展望未来因子实验。

#### 6. 6

- step：6

- writing_job_cn：公开数据/代码，在结论中重申贡献并给出设计知识。

- research_job_cn：整理匿名化真实对话数据并公开；总结RQ答案。

- required_evidence_cn：可访问的数据资源或代码链接。

- transition_to_next_cn：无，论文结束。

### most_transferable_moves_cn

1. 用Upper bound作为理想基准，将组件逐一替换回真实模块，从而把end-to-end性能差异拆解为组件级损失。

2. 设计仅在关键交互环节不同的Mixed模式，与纯NL模式构成几乎完美的对照，以隔离具体机制。

3. 在多领域、多数据集上重复实验，并用MANOVA/Mann-Whitney/Bonferroni把描述性差异转为统计结论。

4. 将主观问卷与客观日志指标结合，并用一条用户确认题检验系统是否真正理解偏好。

5. 最后逐条回答引言RQ，使实验证据与初始问题形成闭环。

### resource_intensive_or_nonstandard_parts_cn

1. 真实用户研究需要约159名被试，且每个被试在三个域之一完成三种模式测试。

2. 需要为电影、图书、音乐构建三个领域KB实例，规模分别为15954/7592/12926个实体。

3. 需要过滤bAbI大规模训练集并处理ConvRecSys的数据转换，这部分并非所有团队都有现成基建。

4. 采集约6500+2800条真实对话并匿名化公开，需要伦理和数据清理工作。

### what_not_to_copy_superficially_cn

1. 不能只写“NL需要按钮支持”而没有三模式被试内对照。

2. 不能只报告准确率而不报告NQ/IT/TPQ/QD等交互成本。

3. 不能只做合成数据并声称理解了UX。

4. 不能使用同一算法但宣称交互模式效应时，缺少按钮控制组。

5. 不能在QD相关仅为推测时，直接将其写成因果结论。

- single_best_description_of_the_routine_cn：用模块化制品把研究问题转化为可独立测试的组件和可严格对照的交互模式，先以理想基准消融组件，再用跨域被试内实验证明哪个交互设计最稳健，最后用RQ答案和数据集使贡献可复用。

## 分析边界

输入中未提供图像内容和页码，部分句子定位依赖章节和段落推断；完整Mann-Whitney结果和问卷全文未在正文中给出，只能依据文中描述；参考文献列表存在编号缺失（如34），可能影响部分引用追溯；论文存在少量标题/拼写噪声，消融分析已经考虑。
