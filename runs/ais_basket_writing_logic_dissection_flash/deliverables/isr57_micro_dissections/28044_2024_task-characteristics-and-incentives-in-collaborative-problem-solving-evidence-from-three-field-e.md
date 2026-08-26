# Task Characteristics and Incentives in Collaborative Problem Solving: Evidence from Three Field Experiments：ISR 句段级微观图谱

- 作者：Jayarajan Samuel; Zhiqiang (Eric) Zheng; Vijay Mookerjee
- 年份：2024
- DOI：10.1287/isre.2021.0118
- 源文件：28044_2024_task-characteristics-and-incentives-in-collaborative-problem-solving-evidence-from-three-field-e.md
- 置信度：0.88

## 核实后的宏观骨架

全文围绕两个核心缺口展开：（1）任务特征如何影响跨职能协作的成功与失败；（2）部门级激励错位如何阻碍协作以及如何校正激励。文章采用三个顺序现场实验的论证链：实验一（第4节）用DID证明引入协作选项降低平均问题解决成本，并定位成本降低来源是功能案例向协作池转移而非正式交接案例转移；实验二（第5节）先用HLM和K-means聚类识别任务特征-协作效果的匹配规律，再用验证性干预研究确认因果；实验三（第6节）部署HRTech Analytics推荐系统，先观察工程师对推荐的遵循率并识别断点，再通过激励校正消除自我纠正。第7节讨论将结果升级为任务特征贡献、激励贡献和人机协作贡献，第8节结论闭合两个引言缺口，并给出边界和限制。

## 摘要逐句图谱

### 1. Abstract P1 S1

- order：1

- locator：Abstract P1 S1

- paraphrase_cn：作者用三个顺序现场实验研究IT支持的知识工作中协作问题解决，情境是某领先高科技公司的客户支持部门。

- move_code：声明研究主题、方法和情境

- statement_status：author_inference

- why_here_cn：摘要首句同时给研究对象、方法类型和场景，让读者立即知道这是一篇现场实验论文。

- inherits_from_previous_cn：无，摘要起点。

- changes_argument_state_cn：确立全文的研究物和方法论基调。

- sets_up_next_cn：为介绍三个实验的序列做铺垫。

- failure_if_removed_cn：摘要缺少锚点，读者不知道研究对象和方法。

- evidence_pointer：Abstract P1 S1

### 2. Abstract P1 S2

- order：2

- locator：Abstract P1 S2

- paraphrase_cn：实验一检验引入新协作问题解决过程后的绩效变化，即跨部门专家团队解决问题能否降低问题解决成本。

- move_code：预告实验一及其研究问题

- statement_status：author_inference

- why_here_cn：需要先交代实验一的总体问题，才能引出随后关于来源和条件的结果。

- inherits_from_previous_cn：承接情境句中的“IT支持协作问题解决”。

- changes_argument_state_cn：把抽象主题具体化为第一个可检验问题。

- sets_up_next_cn：需要说明协作选项是相对什么基线引入的。

- failure_if_removed_cn：实验一的价值问题缺失，后续成本降低结果没有落点。

- evidence_pointer：Abstract P1 S2

### 3. Abstract P1 S3–S4

- order：3

- locator：Abstract P1 S3–S4

- paraphrase_cn：除原有部门内解决外，实验允许两种外部求助方式：正式交接和新的协作流程（两部门专家共同工作）。

- move_code：定义实验条件中的两个帮助寻求方式

- statement_status：design_decision

- why_here_cn：必须先定义正式交接与协作的区别，后面才能解释为什么成本降低不是简单来自协作始终优于交接。

- inherits_from_previous_cn：承接实验一新流程的描述。

- changes_argument_state_cn：建立全文反复出现的两个对比对象：正式交接vs协作。

- sets_up_next_cn：为摘要下一句的“有趣发现”提供概念基础。

- failure_if_removed_cn：协作和交接的区分未建立，成本降低来源的叙述无法理解。

- evidence_pointer：Abstract P1 S3–S4

### 4. Abstract P1 S5

- order：4

- locator：Abstract P1 S5

- paraphrase_cn：有趣的是，成本降低不是因为协作总是优于正式交接，而是因为部门内客户支持工作向新协作流程转移。

- move_code：报告实验一核心发现并标注反直觉性

- statement_status：empirical_result

- why_here_cn：摘要需要立即给出核心反直觉发现，以区别于“协作有益”的平庸结论。

- inherits_from_previous_cn：依靠上一句对协作和交接的定义。

- changes_argument_state_cn：把结果从总体效应推进到来源分解，暗示机制性理解。

- sets_up_next_cn：需要解释哪些条件使得协作有效，引出实验二。

- failure_if_removed_cn：缺少来源分解，实验二的任务特征问题失去动机。

- evidence_pointer：Abstract P1 S5

### 5. Abstract P1 S6

- order：5

- locator：Abstract P1 S6

- paraphrase_cn：在实验一基础上，实验二旨在识别新协作流程何时有效或失败。

- move_code：预告实验二目的

- statement_status：author_inference

- why_here_cn：承接来源分解的不确定性，把问题转向条件性。

- inherits_from_previous_cn：依赖实验一“协作不是始终有效”的发现。

- changes_argument_state_cn：引入第三个变量维度：任务条件。

- sets_up_next_cn：需要给出具体的任务特征发现。

- failure_if_removed_cn：实验二的存在逻辑断裂，任务特征作用无由提出。

- evidence_pointer：Abstract P1 S6

### 6. Abstract P1 S7

- order：6

- locator：Abstract P1 S7

- paraphrase_cn：作者发现任务特征如新颖性和时间限制对选择合适的外部求助方式起重要作用。

- move_code：报告实验二核心发现

- statement_status：empirical_result

- why_here_cn：摘要需要把实验二的结果压缩成一个可记忆的理论标签：新颖性和时间限制。

- inherits_from_previous_cn：承接实验二目标句。

- changes_argument_state_cn：把任务特征从抽象概念变成具体发现。

- sets_up_next_cn：恰好为推荐系统开发提供规则基础。

- failure_if_removed_cn：任务特征贡献不成立，推荐系统的依据缺失。

- evidence_pointer：Abstract P1 S7

### 7. Abstract P1 S8

- order：7

- locator：Abstract P1 S8

- paraphrase_cn：这些发现被用来开发一个信息系统，推荐通过正式交接或协作寻求帮助。

- move_code：描述制品开发

- statement_status：design_decision

- why_here_cn：需要明确任务特征发现转化为信息系统的具体动作，体现IS的制品属性。

- inherits_from_previous_cn：依赖实验二的任务特征发现。

- changes_argument_state_cn：从描述性知识进入设计知识。

- sets_up_next_cn：为实验三检验用户对推荐的响应做铺垫。

- failure_if_removed_cn：文章从实验结果直接跳到行为研究，缺少人与系统交互的载体。

- evidence_pointer：Abstract P1 S8

### 8. Abstract P1 S9

- order：8

- locator：Abstract P1 S9

- paraphrase_cn：实验三检验用户如何对推荐作出反应。

- move_code：预告实验三

- statement_status：author_inference

- why_here_cn：在系统和推荐建立后，自然引入用户采纳问题。

- inherits_from_previous_cn：承接推荐系统的部署。

- changes_argument_state_cn：把研究焦点从任务设计转向激励与行为。

- sets_up_next_cn：为报告激励错位和校正结果做铺垫。

- failure_if_removed_cn：实验三没有引入，激励缺口无法闭环。

- evidence_pointer：Abstract P1 S9

### 9. Abstract P1 S10–S11

- order：9

- locator：Abstract P1 S10–S11

- paraphrase_cn：作者发现部门级激励可导致问题解决者偏离机器推荐，分析偏离原因并展示如何将公司级激励与局部激励对齐以提高遵循率。

- move_code：报告实验三核心发现和校正解决方案

- statement_status：empirical_result

- why_here_cn：摘要需要报告第二个缺口的完整答案：问题存在、原因、纠正有效。

- inherits_from_previous_cn：依赖上一句关于用户反应的预告。

- changes_argument_state_cn：完成从问题到解决的论证闭环。

- sets_up_next_cn：需要把发现上升为可推广的实践启示。

- failure_if_removed_cn：激励贡献缺位，第二个引言缺口没有回答。

- evidence_pointer：Abstract P1 S10–S11

### 10. Abstract P2 S1

- order：10

- locator：Abstract P2 S1

- paraphrase_cn：研究为开发和支持知识密集型问题解决任务的信息系统提供实践启示。

- move_code：声明实践贡献

- statement_status：contribution_claim

- why_here_cn：摘要最后需要把结果导向IS实务应用，符合ISR读者预期。

- inherits_from_previous_cn：依赖全文三个实验的发现。

- changes_argument_state_cn：把研究定位为可复用设计知识。

- sets_up_next_cn：无，摘要结束。

- failure_if_removed_cn：摘要缺少对实践和设计的贡献声明，论文意义降低。

- evidence_pointer：Abstract P2 S1

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：有效组织群体共同工作是管理的重要目标，但创建和维持有效团队是持续挑战。

- move_code：从管理大背景开场

- statement_status：prior_literature

- why_here_cn：引言首句把研究上升到组织管理的基本目标，建立问题重要性。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：确立协作问题普遍且重要。

- sets_up_next_cn：需要展开部门化与协作的张力。

- failure_if_removed_cn：缺少开场背景，问题重要性不成立。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2–S3

- order：2

- locator：Introduction P1 S2–S3

- paraphrase_cn：部门化帮助构建专业知识、分配工作、实现规模经济；另一方面，跨职能协作带来新知识和新视角，知识工作中团队协作已是常态。

- move_code：构建部门化与协作的张力

- statement_status：prior_literature

- why_here_cn：需要说明两个对立组织逻辑并存的背景，为后续讨论任务特征和激励提供语境。

- inherits_from_previous_cn：承接团队有效性的重要性。

- changes_argument_state_cn：限定研究对象：知识工作中的跨职能协作。

- sets_up_next_cn：为指出现有文献忽略任务选择做铺垫。

- failure_if_removed_cn：部门化与协作的张力缺失，后续对任务选择和激励的讨论失去组织逻辑基础。

- evidence_pointer：Introduction P1 S2–S3

### 3. Introduction P2 S1

- order：3

- locator：Introduction P2 S1

- paraphrase_cn：尽管已有研究识别多种协作障碍，但适合跨职能团队的任务选择未得到足够关注。

- move_code：指出现有文献第一个盲点

- statement_status：author_inference

- why_here_cn：在协作重要性之后立即收窄到第一个缺口，遵循“重要但未被研究”的结构。

- inherits_from_previous_cn：依赖前段协作重要性论述。

- changes_argument_state_cn：把文献综述转向缺口识别。

- sets_up_next_cn：需要列举已有任务特征研究的不足。

- failure_if_removed_cn：第一个研究问题失去直接的文献缺口来源。

- evidence_pointer：Introduction P2 S1

### 4. Introduction P2 S2–S4

- order：4

- locator：Introduction P2 S2–S4

- paraphrase_cn：早期研究显示任务难度增加协作需求、不确定性任务适合团队协作、复杂任务需要团队，但文献没有系统研究任务特征如何塑造协作问题解决。

- move_code：综述现有任务特征认知并标示碎片化

- statement_status：prior_literature

- why_here_cn：不能只说未被研究，还要展示已有零散证据，说明新研究需整合和实证化。

- inherits_from_previous_cn：承接任务选择未获关注的缺口。

- changes_argument_state_cn：把一般性缺口具体化为任务特征研究的不完整。

- sets_up_next_cn：引出为什么这一缺口令人困惑。

- failure_if_removed_cn：缺少已有文献铺垫，声称的任务特征空白显得无据。

- evidence_pointer：Introduction P2 S2–S4

### 5. Introduction P2 S5

- order：5

- locator：Introduction P2 S5

- paraphrase_cn：这一空白令人困惑，因为任务分配在工业中重要、任务特征普遍存在、任务管理工具广泛使用。

- move_code：论证缺口为何重要

- statement_status：author_inference

- why_here_cn：需要制造“该研究早就该做”的紧迫感，强化研究合法性。

- inherits_from_previous_cn：承接文献碎片化的描述。

- changes_argument_state_cn：把缺口从文献不足升级为现实重要性。

- sets_up_next_cn：直接引出第一个研究问题。

- failure_if_removed_cn：缺少急迫性论证，研究问题显得可有可无。

- evidence_pointer：Introduction P2 S5

### 6. Introduction P2 S6

- order：6

- locator：Introduction P2 S6

- paraphrase_cn：因此第一个研究问题是：任务特征（复杂度、不确定性、紧迫性）在跨职能团队协作问题解决成功中的作用。

- move_code：正式提出第一个研究问题

- statement_status：author_inference

- why_here_cn：在缺口和重要性之后，需要把任务浓缩成可研究的问题陈述。

- inherits_from_previous_cn：依赖任务特征空白的全部铺垫。

- changes_argument_state_cn：确立全文第一个理论目标。

- sets_up_next_cn：为第二个缺口（激励）让位，需要转移话题。

- failure_if_removed_cn：全文缺少年轮之一，任务特征论述没有指向。

- evidence_pointer：Introduction P2 S6

### 7. Introduction P3 S1–S2

- order：7

- locator：Introduction P3 S1–S2

- paraphrase_cn：个人协作决策由组织利益和个人奖励共同驱动，若二者不对齐，知识工作者可能在该协作时不协作。

- move_code：提出激励错位的机制假设

- statement_status：theory_claim

- why_here_cn：在任务问题后引入第二个机制维度，避免研究只停留在任务匹配。

- inherits_from_previous_cn：从“让协作成功”这一总体目标出发。

- changes_argument_state_cn：打开第二个研究主题：激励。

- sets_up_next_cn：需要明确定位这一主题的文献缺口。

- failure_if_removed_cn：激励贡献没有理论起点。

- evidence_pointer：Introduction P3 S1–S2

### 8. Introduction P3 S3

- order：8

- locator：Introduction P3 S3

- paraphrase_cn：尽管重要，激励错位如何阻碍工业环境协作以及如何对齐个人与公司激励，未得到文献足够关注。

- move_code：定位第二个文献空白

- statement_status：author_inference

- why_here_cn：需要把激励机制从学术协作文献延伸到工业场景，指出未被研究处。

- inherits_from_previous_cn：依赖前两句激励重要性。

- changes_argument_state_cn：确立第二个研究缺口。

- sets_up_next_cn：引出第二个研究问题。

- failure_if_removed_cn：第二个研究问题无来源。

- evidence_pointer：Introduction P3 S3

### 9. Introduction P3 S4

- order：9

- locator：Introduction P3 S4

- paraphrase_cn：第二个研究问题旨在通过提供校正激励错位的策略来维持跨职能协作。

- move_code：正式提出第二个研究问题及其目标

- statement_status：author_inference

- why_here_cn：需要把激励缺口表述为可操作的研究目标，暗示会有干预和校正。

- inherits_from_previous_cn：承接激励错位缺口。

- changes_argument_state_cn：把研究目标延伸到解决方案，不只诊断问题。

- sets_up_next_cn：需要解释为何需要细粒度数据。

- failure_if_removed_cn：激励维度缺少行动承诺，实验三校正部分无锚点。

- evidence_pointer：Introduction P3 S4

### 10. Introduction P4 S1–S2

- order：10

- locator：Introduction P4 S1–S2

- paraphrase_cn：这些缺口的存在部分由于缺乏细粒度数据，而IT使个体和任务级数据收集成为可能；本文数据来自全球领先的ICT公司。

- move_code：用数据条件解释缺口为何现在可填补

- statement_status：author_inference

- why_here_cn：需要说明为什么是现在、为什么是本团队能回答，把数据可得性作为研究可行性依据。

- inherits_from_previous_cn：承接两个缺口。

- changes_argument_state_cn：为方法选择（现场实验和细粒度分析）奠定基础。

- sets_up_next_cn：引入具体组织情境和流程描述。

- failure_if_removed_cn：没有数据能力论证，两个研究问题缺乏实证路径。

- evidence_pointer：Introduction P4 S1–S2

### 11. Introduction P5 S1–S3

- order：11

- locator：Introduction P5 S1–S3

- paraphrase_cn：工程师收到客户故障案例后可在本部门解决，也可向外部部门专家求助；求助方式有两种：正式交接或协作。

- move_code：描述研究情境中的关键决策结构

- statement_status：fact

- why_here_cn：需要用具体情境说明协作和交接的决策点，为两个实验的操作定义做铺垫。

- inherits_from_previous_cn：依赖数据来自ICT公司的叙述。

- changes_argument_state_cn：把抽象协作问题落实到可观察的求助决策。

- sets_up_next_cn：为预告三个实验的发现和部分做铺垫。

- failure_if_removed_cn：读者不知道“协作”在实地意味着什么。

- evidence_pointer：Introduction P5 S1–S3

### 12. Introduction P6 S1–S3

- order：12

- locator：Introduction P6 S1–S3

- paraphrase_cn：实验一显示协作降低问题解决成本；实验二揭示收益来源和利于协作的任务特征，并发现高难度不紧急任务协作反而有害。

- move_code：提前浓缩前两个实验的关键结果

- statement_status：empirical_result

- why_here_cn：给读者一个先行结果地图，增加对后续详述的理解。

- inherits_from_previous_cn：依赖情境中的求助方式定义。

- changes_argument_state_cn：完成“价值+条件”的预告。

- sets_up_next_cn：为介绍推荐系统的开发和实验三做过渡。

- failure_if_removed_cn：读者没有结果预览，进入系统开发较突兀。

- evidence_pointer：Introduction P6 S1–S3

### 13. Introduction P7 S1–S4

- order：13

- locator：Introduction P7 S1–S4

- paraphrase_cn：公司实施HRTech Analytics系统指导何时协作或交接；实验三提供推荐并发现部门激励影响遵循；校正激励后工程师基于公司利益决策。

- move_code：预告实验三和最终解决方案

- statement_status：empirical_result

- why_here_cn：需要完成三个实验的导航，并把激励校正作为解决方案预告。

- inherits_from_previous_cn：依赖实验二任务特征发现。

- changes_argument_state_cn：给出“激励问题+校正成功”的完整弧线。

- sets_up_next_cn：为贡献声明做最后铺垫。

- failure_if_removed_cn：实验三对引言的承诺缺失，贡献无法对应缺口。

- evidence_pointer：Introduction P7 S1–S4

### 14. Introduction P8 S1–S2

- order：14

- locator：Introduction P8 S1–S2

- paraphrase_cn：第一项贡献：发现任务特征对协作有利或有害的证据，连接任务特征与团队协作需求。

- move_code：声明第一项贡献

- statement_status：contribution_claim

- why_here_cn：引言末尾需要把结果回接到第一个缺口。

- inherits_from_previous_cn：依赖实验二任务特征发现。

- changes_argument_state_cn：完成第一个缺口的贡献声明。

- sets_up_next_cn：转述第二项贡献。

- failure_if_removed_cn：任务特征贡献无位置，第一个研究问题未获回应。

- evidence_pointer：Introduction P8 S1–S2

### 15. Introduction P9 S1–S2

- order：15

- locator：Introduction P9 S1–S2

- paraphrase_cn：第二项贡献：识别激励在推荐系统成功实施中的作用，展示激励错位会阻止协作，并提供管理意义。

- move_code：声明第二项贡献

- statement_status：contribution_claim

- why_here_cn：需要把实验三激励发现声明为第二项贡献，闭合第二个缺口。

- inherits_from_previous_cn：依赖实验三激励校正结果。

- changes_argument_state_cn：完成两个研究问题的贡献闭环。

- sets_up_next_cn：为转入文献综述建立方向。

- failure_if_removed_cn：第二个缺口无贡献声明，引言不完整。

- evidence_pointer：Introduction P9 S1–S2

## 引言逐段图谱

### 1. Introduction P1

- paragraph_job_cn：建立协作问题在管理工作中的重要性，同时给出部门化与跨职能协作的张力，为后续两个缺口提供组织背景。

- opening_move_cn：以“管理目标+持续挑战”开场，把问题升到普遍管理层面。

- development_move_cn：平行列举部门化的收益与跨职能协作的收益，显示组织逻辑的内在矛盾。

- pivot_move_cn：在“知识工作”处收窄到知识工作语境，限定研究范围。

- closing_move_cn：以“团队协作是新常态并给出文献”结束，制造下一段“但问题仍在”的需要。

- locator：Introduction P1

### 2. Introduction P2

- paragraph_job_cn：完成第一个研究缺口的完整论证：协作障碍虽多但任务选择未被关注，任务特征虽是常识但文献不系统，由此提出第一个研究问题。

- opening_move_cn：用“然而协作不易”转折，列举已有障碍研究后定位盲点。

- development_move_cn：依次引用Hackman、Daley、Autor等建立任务特征研究的碎片化图景。

- pivot_move_cn：从“文献沉默”转向“令人困惑”的急迫性判断。

- closing_move_cn：以研究问题1作为段落终点，把读者从文献带向实证计划。

- locator：Introduction P2

### 3. Introduction P3

- paragraph_job_cn：建立第二个研究缺口：激励错位如何阻碍工业协作尚未被研究，并给出第二个研究问题的预防性解决方案导向。

- opening_move_cn：以“另一个重要方面”切换维度，从任务转到个人决策。

- development_move_cn：用组织利益与个人奖励的二元驱动框架，引用Merton、Vakili、Bikard支撑错位理论。

- pivot_move_cn：从科学协作的激励发现转向工业场景未受关注。

- closing_move_cn：以“提供校正激励的策略”作承诺，制造对实证方案的期待。

- locator：Introduction P3

### 4. Introduction P4–P5

- paragraph_job_cn：解释缺口存在的原因并引入数据条件，描述研究情境中的求助决策结构，为三个实验的预览搭台。

- opening_move_cn：以“缺口部分缺乏数据”作为方法合理性说明。

- development_move_cn：先说明IT使细粒度数据可用，再介绍具体公司、工程师角色和两种求助方式。

- pivot_move_cn：从数据条件转向组织流程中的关键决策点（求助方式选择）。

- closing_move_cn：以正式交接和协作的定义及其各自的效率逻辑收束，为实验设计做概念准备。

- locator：Introduction P4–P5

### 5. Introduction P6–P7

- paragraph_job_cn：用“结果预告-系统开发-实验三-最终方案”的顺序压缩全文研究弧线，给读者一张导航图。

- opening_move_cn：以“我们首先报告实验一…”点明实证顺序。

- development_move_cn：依次预告实验一、实验二、系统开发和实验三的关键结论。

- pivot_move_cn：从发现转到人工制品（HRTech Analytics）再转到激励校正。

- closing_move_cn：以“校正激励后基于公司利益决策”结束，强调问题可解决。

- locator：Introduction P6–P7

### 6. Introduction P8–P9

- paragraph_job_cn：正式声明两项贡献，并分别对应引入的两个缺口，完成引言到正文的交接。

- opening_move_cn：以“我们的研究做出两大贡献”直接进入贡献声明。

- development_move_cn：第一贡献详细展开任务特征对协作的有利和有害情形；第二贡献详细展开激励在推荐系统实施中的作用。

- pivot_move_cn：从“基础设施支持”转到“工作流推荐支持”，展示信息系统的两个层次。

- closing_move_cn：以管理意义句收束，把贡献推广到组织情境。

- locator：Introduction P8–P9

## 理论到设计逐句图谱

### 1. Prior Work P1 S1–S3

- order：1

- locator：Prior Work P1 S1–S3

- paraphrase_cn：协作有很多收益，但先前工作主要关注团队构成，而非任务特征。

- move_code：归纳协作收益文献并定位缺口

- statement_status：prior_literature

- why_here_cn：文献综述首段需要肯定协作价值并划出综述范围。

- inherits_from_previous_cn：承接引言的两个缺口。

- changes_argument_state_cn：把协作收益综述压缩为团队构成导向。

- sets_up_next_cn：为引出任务特征文献的稀薄做铺垫。

- failure_if_removed_cn：协作价值基线缺失，任务特征的重要性没有对照。

- evidence_pointer：Prior Work P1

### 2. Prior Work P2 S1–S2

- order：2

- locator：Prior Work P2 S1–S2

- paraphrase_cn：任务特征对协作成败的影响文献很薄，原因是任务特征定义缺乏共识且一直缺少微观数据。

- move_code：解释任务特征文献薄弱的两个原因

- statement_status：author_inference

- why_here_cn：需要解释为什么这个缺口存在，以证明自己研究有独特数据优势。

- inherits_from_previous_cn：承接“文献主要关注团队构成”的判断。

- changes_argument_state_cn：给出任务特征研究不足的结构性原因。

- sets_up_next_cn：为“首次实证建立任务特征作用”作铺垫。

- failure_if_removed_cn：任务特征贡献的独特性缺乏解释。

- evidence_pointer：Prior Work P2 S1–S2

### 3. Prior Work P2 S3

- order：3

- locator：Prior Work P2 S3

- paraphrase_cn：据作者所知，本研究首次用细粒度数据实证建立难度、不确定性、紧迫性在成功协作中的作用。

- move_code：声明本研究的新颖性

- statement_status：contribution_claim

- why_here_cn：需要一个明确的“首次”声明把缺口转化为贡献。

- inherits_from_previous_cn：依赖任务特征文献薄弱的论证。

- changes_argument_state_cn：确立本文在任务特征理论上的增量。

- sets_up_next_cn：转入协作成本和新缺口（激励）。

- failure_if_removed_cn：任务特征贡献失去“首次”支撑。

- evidence_pointer：Prior Work P2 S3

### 4. Prior Work P3 S1–S4

- order：4

- locator：Prior Work P3 S1–S4

- paraphrase_cn：协作也有社会惰化、协调成本、冲突等成本，个体可能因联合工作而获得不成比例的奖励。

- move_code：平衡协作收益并引入个体成本

- statement_status：prior_literature

- why_here_cn：需要为激励错位铺垫成本侧面，避免把协作单纯正面化。

- inherits_from_previous_cn：承接协作收益讨论，转向另一个维度。

- changes_argument_state_cn：引入个体激励作为影响协作的独立因素。

- sets_up_next_cn：为激励文献综述做铺垫。

- failure_if_removed_cn：激励理论没有成本侧面的文献基础。

- evidence_pointer：Prior Work P3

### 5. Prior Work P4 S1–S4

- order：5

- locator：Prior Work P4 S1–S4

- paraphrase_cn：个体在收益超过成本时选择协作；学术协作中有作者因个体署名增多而增加协作，但工业场景的激励错位未被报告；作者因此假设个人激励与公司目标不一致时个体可能不协作。

- move_code：从文献延伸到工业场景的理论命题

- statement_status：theory_claim

- why_here_cn：需要把学术协作文献的激励证据转化为工业场景可检验假设。

- inherits_from_previous_cn：依赖上一段个体成本和Merton等奖励不平等文献。

- changes_argument_state_cn：完成第二个研究缺口的理论命题。

- sets_up_next_cn：为实验三的合规研究和激励校正做理论前导。

- failure_if_removed_cn：激励假设没有文献跳板，实验三机制解释悬空。

- evidence_pointer：Prior Work P4

### 6. Section 3.5 P1–P2

- order：6

- locator：Section 3.5 P1–P2

- paraphrase_cn：作者将LTE案例对应高任务难度、未知ProblemType对应高任务不确定性、高严重性对应高任务紧迫性。

- move_code：把抽象任务特征操作化为可测量变量

- statement_status：method_decision

- why_here_cn：需要把理论中的难度、不确定、紧迫转成数据中可识别的字段，是理论到设计的桥梁。

- inherits_from_previous_cn：依赖任务特征理论（Hackman、Wood、Campbell）。

- changes_argument_state_cn：把理论构念转化为推荐系统的输入变量。

- sets_up_next_cn：为实验二的聚类和推荐规则提供变量来源。

- failure_if_removed_cn：理论无法进入数据分析，也无法编码成推荐系统。

- evidence_pointer：Section 3.5

## 制品设计理由逐句图谱

### 1. Section 3.3 P1 S3–S6

- order：1

- locator：Section 3.3 P1 S3–S6

- paraphrase_cn：若交叉功能案例被正式交接，CSG工程师需花大量时间写文档，某些情境下交接的文档开销会增加总工时；传统过程的低效不是求助本身，而是求助方式。

- move_code：诊断传统过程低效的具体机制

- statement_status：author_inference

- why_here_cn：在描述流程后需要解释为什么协作选项值得增加，为设计变更提供因果动机。

- inherits_from_previous_cn：承接传统流程的描述和正式交接的文档开销。

- changes_argument_state_cn：把问题从“工程师不会解决”重定向为“求助方式引发高开销”。

- sets_up_next_cn：引出协作选项作为设计解决方案。

- failure_if_removed_cn：协作选项的引入没有动机，实验一的处理设计不成立。

- evidence_pointer：Section 3.3

### 2. Section 3.4 P1–P2

- order：2

- locator：Section 3.4 P1–P2

- paraphrase_cn：新过程在传统正式交接之外增加协作选项，CSG工程师可用协作工具同步求助PSG工程师。

- move_code：定义新制品的核心设计特征

- statement_status：design_decision

- why_here_cn：需要明确新流程相对传统流程的唯一变化是增加协作，保证实验一的干净比较。

- inherits_from_previous_cn：依赖传统流程和低效诊断。

- changes_argument_state_cn：给出实验一的处理定义。

- sets_up_next_cn：为实验一的结果变量和来源分解提供设计前提。

- failure_if_removed_cn：实验一的因果比较对象不明确。

- evidence_pointer：Section 3.4

### 3. Section 6 P1–P2

- order：3

- locator：Section 6 P1–P2

- paraphrase_cn：基于实验二发现，公司开发HRTech Analytics推荐系统，通过仪表盘把正式交接或协作推荐传达给工程师，并观察实际选择。

- move_code：说明推荐系统的来源和功能

- statement_status：design_decision

- why_here_cn：需要把实验二的任务特征规则转化为可工作的信息制品，并说明数据观察方式。

- inherits_from_previous_cn：依赖实验二验证后的任务特征结论。

- changes_argument_state_cn：从因果知识转到可部署制品。

- sets_up_next_cn：为实验三的合规观察和激励分析做铺垫。

- failure_if_removed_cn：实验三无制品可部署，人机交互部分失去对象。

- evidence_pointer：Section 6 P1–P2

### 4. Section 6.3 P1–P2

- order：4

- locator：Section 6.3 P1–P2

- paraphrase_cn：为校正激励，作者将工程师评价改为平均总工时（CSG+PSG），并移除每周协作比例仪表盘。

- move_code：定义激励校正干预

- statement_status：design_decision

- why_here_cn：需要把根因分析转化为具体的干预动作，改变可观察的激励和信息环境。

- inherits_from_previous_cn：依赖实验三断点回归识别的激励错位。

- changes_argument_state_cn：从诊断进入解决方案实施。

- sets_up_next_cn：为校正后12周的验证数据和回归结果做铺垫。

- failure_if_removed_cn：激励校正没有具体设计，实验三后半段无法检验。

- evidence_pointer：Section 6.3

## Study开头、过渡与收束图谱

### 1. Section 4 opening P1; Section 4.5 closing P1

- study_or_phase：实验一（Section 4）

- locator：Section 4 opening P1; Section 4.5 closing P1

- paraphrase_cn：开头提出协作是否降低平均成本、所有交叉功能任务是否受益；结尾指出收益来自功能工作向协作转移，而非正式交接向协作转移。

- move_code：实验一开场设问和结尾来源分解

- statement_status：empirical_result

- why_here_cn：实验一需要用清晰的两问限定范围，结尾需要把结果导出为下一实验的动机。

- inherits_from_previous_cn：依赖引言中的研究情境。

- changes_argument_state_cn：完成总体效应证明并留下来源之谜。

- sets_up_next_cn：功能案例转移之谜需要实验二的任务特征分析。

- failure_if_removed_cn：实验二的起点缺失。

- evidence_pointer：Section 4 P1; Section 4.5

### 2. Section 5 P1–P3; Section 5.2 P5

- study_or_phase：实验二探索性分析（Section 5.1–5.2）

- locator：Section 5 P1–P3; Section 5.2 P5

- paraphrase_cn：开头说明实验二回答协作何时有效；聚类分析发现某些簇协作降本、某些簇协作增本、某些簇只是工时转移。

- move_code：实验二开篇和探索性结果报告

- statement_status：empirical_result

- why_here_cn：实验二需要在情境中明确探索性阶段的问题，再用聚类提出可验证的规则。

- inherits_from_previous_cn：承接实验一的功能案例转移发现。

- changes_argument_state_cn：从总体价值推进到任务特征异质性。

- sets_up_next_cn：聚类结果的因果性存疑，引出验证研究。

- failure_if_removed_cn：任务特征规则没有实证来源。

- evidence_pointer：Section 5 P1; Section 5.2

### 3. Section 5.3 P1–P2; Section 5.3 closing P1

- study_or_phase：实验二验证研究（Section 5.3）

- locator：Section 5.3 P1–P2; Section 5.3 closing P1

- paraphrase_cn：开头说明对184个需要PSG帮助的案例干预协作或交接选择；结尾断言困难且紧迫任务适合协作，困难不紧迫低不确定性适合交接，不紧迫不确定任务仅转移工时。

- move_code：验证研究设计说明和结论性机制标签

- statement_status：empirical_result

- why_here_cn：探索性聚类后需要一个主动操纵的因果检验；结尾把结果转成可直接编码的决策规则。

- inherits_from_previous_cn：依赖聚类发现的簇4、簇5特征。

- changes_argument_state_cn：把任务特征效应从相关提升为因果。

- sets_up_next_cn：为推荐系统编码任务特征规则提供依据。

- failure_if_removed_cn：任务特征规则的因果可信度不足，系统设计失去依据。

- evidence_pointer：Section 5.3

### 4. Section 6 P1; Section 6.2 P1–P2

- study_or_phase：实验三合规研究（Section 6.1–6.2）

- locator：Section 6 P1; Section 6.2 P1–P2

- paraphrase_cn：开头说明实验三研究激励、推荐遵循和偏离原因；随后用断点回归识别上周协作比例超过0.6后本周合规下降0.371。

- move_code：实验三开篇和根因分析

- statement_status：empirical_result

- why_here_cn：实验三需要界定新的研究对象：人对机器推荐的遵循，以及偏离的激励机制。

- inherits_from_previous_cn：依赖实验二规则被编码到HRTech Analytics。

- changes_argument_state_cn：从任务设计转向激励行为。

- sets_up_next_cn：根因分析显示需校正激励。

- failure_if_removed_cn：第二个缺口无法实证。

- evidence_pointer：Section 6 P1; Section 6.2

### 5. Section 6.3 P1–P4

- study_or_phase：实验三激励校正（Section 6.3）

- locator：Section 6.3 P1–P4

- paraphrase_cn：开头说明校正内容（总工时评价、移除看板）；结尾报告校正后合规均值0.786且上周比例系数不显著。

- move_code：校正设计和验证结果

- statement_status：empirical_result

- why_here_cn：识别问题后需要证明解决方案有效，给激励贡献提供完整闭环。

- inherits_from_previous_cn：依赖实验三根因分析结果。

- changes_argument_state_cn：完成激励问题从诊断到解决的闭环。

- sets_up_next_cn：进入讨论，将结果升华为贡献。

- failure_if_removed_cn：激励校正无证据，第二个缺口没有实证回答。

- evidence_pointer：Section 6.3

## 讨论与贡献逐句图谱

### 1. Discussion P1 S1–S2

- order：1

- locator：Discussion P1 S1–S2

- paraphrase_cn：这是首次实验研究任务特征和激励对齐对协作问题解决的作用；大规模现场实验使作者能观察最细粒度的任务和工程师行为。

- move_code：重申研究独特性和方法优势

- statement_status：contribution_claim

- why_here_cn：讨论开篇需要把前面的实证工作提升为理论贡献。

- inherits_from_previous_cn：依赖三个实验的全部结果。

- changes_argument_state_cn：从实证报告转向贡献陈述。

- sets_up_next_cn：逐条展开三点贡献。

- failure_if_removed_cn：讨论缺少贡献总纲。

- evidence_pointer：Discussion P1 S1–S2

### 2. Discussion P1 S3–S5

- order：2

- locator：Discussion P1 S3–S5

- paraphrase_cn：第一，细化任务特征如何影响协作结果；第二，指出推荐不合规和激励失谐的重要性；第三，为人机协作文献增加正面案例。

- move_code：并列三点贡献

- statement_status：contribution_claim

- why_here_cn：需要把贡献分点列出，呼应引言的两个缺口并增加人机协作维度。

- inherits_from_previous_cn：依赖研究独特性和全部证据。

- changes_argument_state_cn：把贡献从二条扩展到三条，涵盖技术、行为、人机。

- sets_up_next_cn：为管理含义的展开做铺垫。

- failure_if_removed_cn：贡献声明无清单，读者无法快速提取价值。

- evidence_pointer：Discussion P1 S3–S5

### 3. Discussion P2 S1–S3

- order：3

- locator：Discussion P2 S1–S3

- paraphrase_cn：管理者应将正确任务分配给协作；新技术的紧迫案例适合协作，低优先级已知问题协作有害，低优先级未知问题只是工时转移。

- move_code：把结果转成任务分配的管理边界

- statement_status：contribution_claim

- why_here_cn：任务特征贡献需要通过管理动作表达，说明其可操作性。

- inherits_from_previous_cn：依赖实验二聚类和验证研究结果。

- changes_argument_state_cn：把“任务特征有效”转化为“应如此分配”的规范陈述。

- sets_up_next_cn：为讨论干预的条件性做铺垫。

- failure_if_removed_cn：任务特征贡献缺少实践翻译。

- evidence_pointer：Discussion P2

### 4. Discussion P3 S1–S6

- order：4

- locator：Discussion P3 S1–S6

- paraphrase_cn：推荐干预应区分三类情境：人类知道机器不知道、人机知识重叠、机器知道人类不知道；只有后两种且结果有实际差异时才应干预。

- move_code：把结果升级为人机干预的一般原则

- statement_status：contribution_claim

- why_here_cn：需要把局部实验发现抽象为可跨领域推广的设计原则，避免贡献停留在具体案例。

- inherits_from_previous_cn：依赖实验二、三中分支结果和相关/不相关簇的对比。

- changes_argument_state_cn：从具体发现升级到泛化设计知识。

- sets_up_next_cn：为激励对齐的第三点含义做铺垫。

- failure_if_removed_cn：论文无法从实证结果提升为可复用设计知识。

- evidence_pointer：Discussion P3

### 5. Discussion P4 S1–S3

- order：5

- locator：Discussion P4 S1–S3

- paraphrase_cn：引入协作时必须评估所有阻碍协作的激励，必要时改变个体文化；激励对齐是实现协作价值的前提。

- move_code：给出激励对齐的一般管理边界

- statement_status：contribution_claim

- why_here_cn：第三点贡献需要把实验三的校正结果推广为一般管理原则。

- inherits_from_previous_cn：依赖实验三激励校正成功结果。

- changes_argument_state_cn：完成激励贡献的规范化表达。

- sets_up_next_cn：转向数据发现方法的一般意义。

- failure_if_removed_cn：激励贡献缺少实践层面的落脚点。

- evidence_pointer：Discussion P4

### 6. Discussion P5 S1–S2

- order：6

- locator：Discussion P5 S1–S2

- paraphrase_cn：任务特征和摩擦都是从数据中发现的，若企业拥有细粒度任务信息，就能评估并纠正系统低效并持续改进经济结果。

- move_code：把方法路径升华为数据驱动的持续改进

- statement_status：contribution_claim

- why_here_cn：需要回应“为何用数据驱动”并给管理者可执行的方法论。

- inherits_from_previous_cn：依赖三个实验的数据挖掘过程。

- changes_argument_state_cn：把结果从一次性实验扩展为持续改进流程。

- sets_up_next_cn：为结论总结做铺垫。

- failure_if_removed_cn：数据驱动方法的意义未被提炼。

- evidence_pointer：Discussion P5

### 7. Conclusion P1 S1–S3

- order：7

- locator：Conclusion P1 S1–S3

- paraphrase_cn：三个现场实验表明适合跨职能团队的工作项被有效筛选并降本；系统部署后作者分析工程师不愿协作的根本原因，并将其追溯到过时且错位的激励系统；改变激励后展示跨职能团队的利益。

- move_code：总结研究旅程

- statement_status：contribution_claim

- why_here_cn：结论需要重述从价值证明到激励校正的完整叙事。

- inherits_from_previous_cn：依赖全部实验结果。

- changes_argument_state_cn：把分散实验结果合并为一条整体贡献链。

- sets_up_next_cn：为结论中的缺口闭合句做铺垫。

- failure_if_removed_cn：结论缺少研究旅程的整体回顾。

- evidence_pointer：Conclusion P1

### 8. Conclusion P2 S1–S3

- order：8

- locator：Conclusion P2 S1–S3

- paraphrase_cn：作者填补两个文献空白：成功协作需要正确任务分配；即使任务和团队正确，激励错位也会使协作适得其反；作者展示了如何对齐激励。

- move_code：逐点闭合引言两个缺口

- statement_status：contribution_claim

- why_here_cn：需要用与引言呼应的语言把全文的证据归入两个缺口。

- inherits_from_previous_cn：依赖引言中两个缺口的语词和全文结果。

- changes_argument_state_cn：完成贡献与缺口的对应闭环。

- sets_up_next_cn：为外部效度和限制讨论做铺垫。

- failure_if_removed_cn：引言缺口没有得到正式回应，论文论证不完整。

- evidence_pointer：Conclusion P2

### 9. Conclusion P3 S1–S3

- order：9

- locator：Conclusion P3 S1–S3

- paraphrase_cn：结果虽来自ICT行业，但适用于更广泛的服务交付场景，如保修、客户关怀、项目管理和业务流程管理。

- move_code：声明外部有效性

- statement_status：author_inference

- why_here_cn：需要让读者看到研究的可推广场景，平衡单一行业现场实验的局限。

- inherits_from_previous_cn：依赖任务特征和激励机制的普适性。

- changes_argument_state_cn：扩展结果适用域。

- sets_up_next_cn：为限制和未来研究做铺垫。

- failure_if_removed_cn：外部有效性缺失，论文影响范围变小。

- evidence_pointer：Conclusion P3

### 10. Conclusion P4 S1–S6

- order：10

- locator：Conclusion P4 S1–S6

- paraphrase_cn：研究限制包括只关注生产力和成本、未考虑员工学习、在办公室现场进行；未来可在远程工作和其他情境研究。

- move_code：列出局限和未来方向

- statement_status：author_inference

- why_here_cn：结尾需要诚实承认边界，并指出后续研究问题，符合ISR规范。

- inherits_from_previous_cn：依赖研究设计和行业特征。

- changes_argument_state_cn：从贡献转向自我批判和开放问题。

- sets_up_next_cn：无，结束全文。

- failure_if_removed_cn：缺少边界讨论会被视为过度声称。

- evidence_pointer：Conclusion P4

## Study累积逻辑

### 1. 1

- study_or_phase：实验一（价值证明）

- evidence_job_cn：证明在真实组织中引入协作选项能降低总体问题解决成本，并把收益来源分解到功能案例转移。

- what_it_establishes_cn：建立协作选项的总体因果价值、成本降低的主要来源是功能案例向协作池转移。

- what_it_cannot_establish_cn：无法说明哪些具体任务特征使协作有效或有害；无法解释为什么正式交接案例没有转移。

- why_next_phase_is_needed_cn：功能案例转移之谜需要任务特征级别的分析来揭示协作适用的条件。

- transition_wording_function_cn：实验一结尾断言“收益来自功能工作向协作工作转移”，实验二开篇复述该结论并据此提出问题。

### 2. 2

- study_or_phase：实验二探索性分析（机制识别）

- evidence_job_cn：识别任务特征（难度、不确定性、紧迫性）与协作效果的匹配关系，并纳入工程师异质性。

- what_it_establishes_cn：平均效应掩盖异质性；LTE高严重（难且紧迫）协作降本37%，LTE低严重已知（难但不紧迫不确定低）协作增本55%，LTE低严重未知仅工时转移。

- what_it_cannot_establish_cn：聚类是探索性的，选择偏差可能污染协作决策与结果的关联；不能确立因果关系。

- why_next_phase_is_needed_cn：需要一个受控的验证性干预来确认聚类特征确实是协作成本差异的原因。

- transition_wording_function_cn：验证研究开头直接说“为了验证聚类的分类”，点明实验从探索到确证的升级。

### 3. 3

- study_or_phase：实验二验证研究（因果确证）

- evidence_job_cn：通过强制干预协作或交接选择，确认任务特征规则对工程师工时的因果方向。

- what_it_establishes_cn：簇4型案例强制协作显著优于自选交接（61%下降）；簇5型案例强制交接显著优于自选协作（55.3%下降）。

- what_it_cannot_establish_cn：无法预测真实部署中工程师是否遵从推荐；无法识别激励等社会因素。

- why_next_phase_is_needed_cn：已验证的任务特征规则需要被编码进系统，并在真实使用中检验人的遵循行为。

- transition_wording_function_cn：实验三开头说明基于实验二发现开发HRTech Analytics，形成从规则到制品的转换。

### 4. 4

- study_or_phase：实验三合规研究（行为与激励诊断）

- evidence_job_cn：观察工程师是否遵循机器推荐，识别激励错位导致的行为拐点。

- what_it_establishes_cn：协作推荐遵循率低且方差高；上周协作比例超过0.6后本周合规下降0.371；访谈显示协作被视为依赖。

- what_it_cannot_establish_cn：断点回归只证明存在自我纠正行为，不能证明改变激励就能消除。

- why_next_phase_is_needed_cn：需要实际改变评价指标和信息环境，检验自我纠正是否消失。

- transition_wording_function_cn：在根因分析后，作者用“接下来我们探索如何对齐地方和全球激励”引入校正。

### 5. 5

- study_or_phase：实验三激励校正（解决方案验证）

- evidence_job_cn：证明激励校正能消除自我纠正，使工程师按公司利益遵循推荐。

- what_it_establishes_cn：校正后合规均值0.786方差降低，上周比例系数不显著，自我纠正消失。

- what_it_cannot_establish_cn：无法证明长期持续有效、其他组织适用性、学习效应等特点。

- why_next_phase_is_needed_cn：结果需要升级为理论贡献和管理原则，进入讨论。

- transition_wording_function_cn：实验三结果后讨论开头宣称“首次实验研究”，把行为干预结果提升为贡献。

## 主张—证据台账

### 1. 引入协作选项降低平均问题解决成本

- claim_cn：引入协作选项降低平均问题解决成本

- claim_level：artifact

- supporting_evidence_cn：DID回归显示CaseTAT下降25.7%、EngineerHours下降13.6%、CaseIdleTime下降31.8%，固定效应和控制变量存在。

- support_strength：direct

- where_claim_is_made：Section 4.4

- where_evidence_is_provided：Table 4, Equation 1

### 2. 成本降低来自功能案例转向协作而非正式交接转向协作

- claim_cn：成本降低来自功能案例转向协作而非正式交接转向协作

- claim_level：mechanism

- supporting_evidence_cn：Logit显示PSG求助几率增加13倍；功能案例子样本EngineerHours下降13.3%显著，交叉功能子样本总工时变化不显著。

- support_strength：direct

- where_claim_is_made：Section 4.5

- where_evidence_is_provided：Tables 5–7, Equation 2

### 3. 任务特征（新颖性、时间限制、不确定性）决定协作有利或有害

- claim_cn：任务特征（新颖性、时间限制、不确定性）决定协作有利或有害

- claim_level：mechanism

- supporting_evidence_cn：HLM聚类显示簇4协作降本37%、簇5协作增本55%、簇2仅工时转移；树结构子样本结果一致。

- support_strength：direct

- where_claim_is_made：Section 5.2

- where_evidence_is_provided：Tables 10–11, Figure 3

### 4. 任务特征规则具有因果效力

- claim_cn：任务特征规则具有因果效力

- claim_level：mechanism

- supporting_evidence_cn：验证研究强制协作/交接：簇4型强制协作均值13.86小时远低于自选交接35.63小时；簇5型强制交接15.13小时远低于自选协作33.83小时。

- support_strength：direct

- where_claim_is_made：Section 5.3

- where_evidence_is_provided：Figures 4–5

### 5. 部门激励错位导致工程师自我纠正偏离协作推荐

- claim_cn：部门激励错位导致工程师自我纠正偏离协作推荐

- claim_level：boundary

- supporting_evidence_cn：断点回归显示上周协作比例超过0.6时本周合规下降0.371；访谈显示协作被视为依赖。

- support_strength：direct

- where_claim_is_made：Section 6.2

- where_evidence_is_provided：Figure 8, Table 13, Equation 5

### 6. 激励校正消除自我纠正行为

- claim_cn：激励校正消除自我纠正行为

- claim_level：design_knowledge

- supporting_evidence_cn：校正后12周合规均值0.786，上周比例系数β1=-0.0142不显著。

- support_strength：direct

- where_claim_is_made：Section 6.3

- where_evidence_is_provided：Figure 9, Table 14, Equation 6

### 7. 成功协作需要正确任务分配

- claim_cn：成功协作需要正确任务分配

- claim_level：theory

- supporting_evidence_cn：实验二全部结果和验证研究；讨论和结论把任务特征匹配升级为理论贡献。

- support_strength：direct

- where_claim_is_made：Conclusion P2; Discussion P1

- where_evidence_is_provided：Sections 5.2–5.3

### 8. 即使任务和团队正确，激励错位也会使协作适得其反

- claim_cn：即使任务和团队正确，激励错位也会使协作适得其反

- claim_level：theory

- supporting_evidence_cn：实验三的合规下降和访谈证据；校正后行为恢复。

- support_strength：direct

- where_claim_is_made：Conclusion P2; Introduction P3

- where_evidence_is_provided：Section 6.2–6.3

### 9. 结果适用于更广泛服务交付场景

- claim_cn：结果适用于更广泛服务交付场景

- claim_level：boundary

- supporting_evidence_cn：作者以机制普遍性推断，未提供跨行业实证。

- support_strength：asserted

- where_claim_is_made：Conclusion P3

- where_evidence_is_provided：Conclusion P3

### 10. 这是首次实证建立细粒度任务特征在协作中的作用

- claim_cn：这是首次实证建立细粒度任务特征在协作中的作用

- claim_level：theory

- supporting_evidence_cn：文献综述声称据作者所知尚未有类似研究，辅以三个实验的数据支持。

- support_strength：partial

- where_claim_is_made：Prior Work P2 S3

- where_evidence_is_provided：Prior Work P2; Sections 5.2–5.3

## ISR定位逻辑

- constitutive_is_problem_cn：问题被构成为：信息系统的部署不仅改变流程，还改变了工程师对外部求助的成本和感知；IT使细粒度任务数据可得，使作者能在真实组织中检验任务特征和激励如何塑造协作。协作不是一个中立的团队构成问题，而是由信息系统支持的流程设计、推荐和激励共同构成的组织行为问题。

- technology_behavior_or_market_entanglement_cn：技术制品（协作工具、HRTech Analytics推荐、仪表盘）与工程师的求助行为、部门荣誉感、自我纠正紧密纠缠：增加协作选项改变求助倾向（PSG求助几率增13倍）；推荐系统的看板把协作比例公开化，强化部门激励；移除看板并改用总工时评价又改变行为。技术不是换一个工具的简单替代，而是重塑行为决策环境。

- role_of_benchmark_or_objective_evidence_cn：每个客观效果都被用来支持超出工程性能的IS主张：DID下降幅度支持“协作流程的价值及其来源分解”；聚类降本/增本百分比支持“任务特征应作为流程选择的依据”；断点回归的0.371下降支持“激励错位会破坏机器推荐的有效性”；校正后系数不显著支持“激励对齐是推荐系统成功落地的前提”。即客观证据被用来支持任务-流程匹配和激励设计的组织理论主张。

- theory_in_design_cn：理论部分进入设计的方式是混合的：任务难度、不确定性、紧迫性被操作化为LTE、ProblemType、Severity，编码进推荐系统；但具体哪些组合推荐协作是数据驱动的聚类发现，不是从理论演绎。激励理论（个人奖励与组织目标不一致）指导了实验三的预测和校正方案的设计，但识别机制依赖断点回归和访谈。可以概括为理论提供构念和语言，设计规则由数据补充。

- technical_vs_is_contribution_balance_cn：文章把篇幅分配给行为和组织机制多于纯技术实现：实验一和实验二从总体效应到任务异质性，实验三从合规到激励校正；对推荐系统的实现只给简短描述（在线附录给细节）。贡献声明也集中在协作问题解决文献和激励文献，而不是推荐算法性能。技术制品是研究载体，IS贡献是任务-流程匹配、激励对齐和人机协作。

- beyond_transient_performance_cn：作者避免了“协作总是更好”的一次性结论：通过来源分解、聚类、验证研究、断点回归和校正前后比较，把结果升级为条件性设计知识——“何时协作、何时交接、何时干预、何时只调激励”。这种条件性知识可在未来任务分类和激励审计中复用，因此超越一时的性能优势。

## 段落级仿写模板

### abstract_steps

1. 第一句给出对象、方法、情境。

2. 第二至三句依次预告每个实验的研究问题。

3. 第四至六句用“有趣的是”引出每个实验的关键发现，并给出条件化结论。

4. 最后一句声明实践启示，指向IS开发与实施。

### introduction_paragraph_steps

1. 段1用管理目标开篇，建立部门化与协作的张力。

2. 段2指出现有文献忽略任务选择，综述已有任务特征证据，提出研究问题1。

3. 段3用个人奖励与组织利益的框架提出激励错位，给出研究问题2。

4. 段4–5解释数据条件和现场情境，定义正式交接与协作。

5. 段6–7按顺序预告三个实验和最终结果，给出导航图。

6. 段8–9分列两项贡献，回接两个缺口。

### theory_to_design_steps

1. 综述协作收益并标记文献缺口。

2. 给出任务特征理论的碎片化证据，声明首次贡献。

3. 综述协作成本并引出激励理论。

4. 把学术激励证据延伸到工业场景，形成可检验命题。

5. 把理论构念操作化为数据变量，连接实验设计和推荐系统输入。

### method_and_study_sequence_steps

1. 每个实验开头用一两句说明实验目的和后续问题。

2. 描述数据来源、随机化单元和变量定义。

3. 说明计量模型并证明模型选择的必要性（如ICC）。

4. 报告模型自由证据（均差、图表）和正式回归结果。

5. 解释结果来源或机制。

6. 用过渡句把未解决的问题导向下一实验。

### results_reporting_steps

1. 先报告总效应并转换为百分比。

2. 再分解来源或按子样本报告异质性。

3. 对探索性发现主动承认因果限制。

4. 用干预或验证性研究确认因果方向。

5. 对行为机制使用图形、断点和访谈交叉印证。

6. 最后用校正或验证设计展示解决方案有效。

### discussion_and_contribution_steps

1. 首段重申研究独特性，列出三点贡献。

2. 把任务特征发现转化为管理分配指南。

3. 把干预条件抽象为人机知识三种情境。

4. 把激励校正推广为激励审计原则。

5. 把数据驱动方法升华为持续改进路径。

6. 结论重述研究旅程，逐点闭合引言缺口。

7. 声明外部有效性。

8. 列出限制和未来方向。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立两个研究缺口的完整论证

- research_evidence_required_cn：已有文献支持协作重要性和激励理论；细粒度数据可得；明确的组织情境和求助决策结构。

- sentence_pattern_function_cn：用“尽管…但…”指出缺口，用“因此研究问题是…”给出问题，随后用数据条件解释为何现在可答。

- transition_condition_cn：当读者知道两个缺口和两个研究问题后，进入情境描述。

### 2. 2

- step：2

- rhetorical_job_cn：描述组织情境和制品的两个求助方式

- research_evidence_required_cn：具体公司、部门结构、传统流程和新增协作选项的设计细节。

- sentence_pattern_function_cn：先描述现状和流程，再诊断传统流程的低效机制，最后定义新流程的唯一新增选项。

- transition_condition_cn：当读者理解协作选项相对于传统流程的差异，进入实验一。

### 3. 3

- step：3

- rhetorical_job_cn：报告实验一总体效应和来源分解

- research_evidence_required_cn：DID回归结果、Logit结果、功能案例和交叉功能案例子样本的比较。

- sentence_pattern_function_cn：以研究问题开头，说明随机化单元和模型，报告总效应，再分两步追踪来源，最后以“来源之谜”收束。

- transition_condition_cn：当读者相信总体价值存在但来源不明，进入实验二。

### 4. 4

- step：4

- rhetorical_job_cn：用探索性聚类识别任务特征异质性

- research_evidence_required_cn：ICC诊断、HLM模型、K-means聚类结果和子样本成立性检查。

- sentence_pattern_function_cn：先证明工程师异质性需要HLM，再报告平均效应不显著，转向聚类并展示每簇的系数方向和显著性，最后用树结构验证。

- transition_condition_cn：当读者相信存在任务特征相关的异质性但因果未定，进入验证研究。

### 5. 5

- step：5

- rhetorical_job_cn：用验证性干预确认因果

- research_evidence_required_cn：对关键簇类型案例的强制干预数据、t检验和干预组与自选组均值比较。

- sentence_pattern_function_cn：先说明样本和干预设计，再用图和t检验报告两种任务的干预结果，最后给出结对的任务特征标签。

- transition_condition_cn：当读者相信任务特征规则具有因果效力，进入推荐系统部署。

### 6. 6

- step：6

- rhetorical_job_cn：部署推荐系统并观察人的遵循行为

- research_evidence_required_cn：HRTech Analytics部署后的周级合规数据、访谈证据和断点回归。

- sentence_pattern_function_cn：先介绍系统来源和功能，再报告合规均值和方差，用访谈揭示部门荣誉感机制，用断点回归识别拐点。

- transition_condition_cn：当读者相信激励错位导致自我纠正，进入激励校正。

### 7. 7

- step：7

- rhetorical_job_cn：实施激励校正并验证行为改变

- research_evidence_required_cn：校正后12周数据、合规均值和回归系数不显著。

- sentence_pattern_function_cn：先描述校正动作（总工时评价、移除看板），再报告校正后合规趋势，用回归证明原影响消失。

- transition_condition_cn：当读者相信激励对齐有效，进入讨论。

### 8. 8

- step：8

- rhetorical_job_cn：把实验结果升级为理论贡献、管理原则和边界

- research_evidence_required_cn：三个实验的全部结果、任务特征和激励的机制性解释、可泛化的人机情境分类。

- sentence_pattern_function_cn：先宣布首次贡献并列出三点，再逐条把结果译为管理动作和设计原则，最后用结论闭合引言缺口并列出限制。

- transition_condition_cn：当贡献与缺口一一对应，研究完成。

## 应模仿的高价值动作

1. 先用一个反直觉结果（“成本降低不是因为协作总是更优，而是来源转移”）吸引读者，而不是简单说协作有效。

2. 在每个实验开头重复研究问题，结尾留下未解决问题，形成链条。

3. 用平均效应不显著推动探索性聚类，展示从总体到条件的推理动作。

4. 在探索性聚类后主动承认因果风险，并设置验证性干预，提升可信度。

5. 用访谈（部门将协作视为依赖）和断点回归共同锁定激励机制。

6. 把设计知识抽象为三类人机知识情境，使结果可从具体案例提炼为原则。

7. 讨论和结论逐句回扣引言两个缺口，给读者完整闭环。

## 不要只复制的表面动作

1. 不要在没有真实现场随机化的情况下照搬DID的报告节奏。

2. 不要在没有工程师异质性数据的情况下照搬ICC/HLM论证。

3. 不要在没有真实断点数据的情况下照搬“0.6阈值”式的断点回归叙事。

4. 不要在没有访谈证据时声称“自豪感或依赖”是机制。

5. 不要把三个实验的顺序叙述机械复制为“总是有益的”研究，本文的价值在条件性结论。

## 证据薄弱或跳跃的动作

1. 结论中外部有效性断言（适用保修、项目管理等）无直接跨行业证据，属于推断。

2. “首次实证建立细粒度任务特征作用”依赖“据作者所知”表述，难以完全验证。

3. 把LTE等同于高难度、Severity等同于紧迫性、ProblemType等同于不确定性，是代理操作化，语义可能不完整。

4. 激励校正后只有12周数据，长期持续性和其他混淆因素未完全排除。

5. 访谈证据只见机制解释，未提供系统编码的引语或正式分析方法。

## 一句话套路

用三个顺序现场实验把信息系统的流程支持从价值证明推进到任务-流程匹配，再把推荐系统部署中暴露出的部门激励错位识别并校正，最后把条件性实验结果升级为任务分配、干预策略和激励对齐的可复用IS设计知识。

## 分析边界

全文可读，但部分表格和图（如图6–9）依赖OCR的图像标签，细节可能与原文有微小偏差；在线附录未提供，因此随机化检查、操作检查、推荐系统详细实现、验证研究更多细节和摘要中提到的补充材料无法核实；自然段边界和句序基于文章版式推断，个别位置可能存在跨段合并或拆分；单篇解读属于分析性重构，不替代对原文的引用。
