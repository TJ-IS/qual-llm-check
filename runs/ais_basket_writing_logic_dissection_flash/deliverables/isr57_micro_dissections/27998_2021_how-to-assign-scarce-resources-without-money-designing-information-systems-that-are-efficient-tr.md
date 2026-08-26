# How to Assign Scarce Resources Without Money: Designing Information Systems that are Efficient, Truthful, and (Pretty) Fair：ISR 句段级微观图谱

- 作者：Martin Bichler; Alexander Hammerl; Thayer Morrill; Stefan Waldherr
- 年份：2021
- DOI：10.1287/isre.2020.0959
- 源文件：27998_2021_how-to-assign-scarce-resources-without-money-designing-information-systems-that-are-efficient-tr.md
- 置信度：0.82

## 核实后的宏观骨架

本文是一篇典型的设计科学研究（Design Science Research）。总结构为：摘要提出无货币匹配中效率、真实性与公平不可兼得，并以课程分配为具体场景，引入RESPCT机制，用形式证明和现场数据评价。引言从经典匹配理论出发，将问题收窄到课程分配，指出现有机制（TTC效率但产生嫉妒，DA无嫉妒但低效）的不足和最低配额带来的新挑战，定位为IS激励设计与设计科学贡献。第2节文献综述细致梳理TTC、DA、ESTTC、ETTC等机制，特别指出现有方法在最低配额和低嫉妒上的空白，并介绍TUM真实应用背景。第3节建立形式模型、算法和设计目标，提出mutual best的不可行性和σ-mutual best的放宽。第4节是核心设计章节，依次引入clinching、prioritized pointing、配额扩展和最大化保证席位，最终形成RESPCT完整算法并给出形式定理。第5节用TUM 10个真实数据集（50个实例）评价公平性，用ESDA对照评价效率，用合成数据（至2000学生、100门课程）评价可扩展性。第6节讨论贡献、边界和限制。第7节结论将机制推广到学校选择、医疗劳动力等更广领域，并指出单位需求假设是最重要限制。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：当货币转移不可用时，基于偏好的匹配可以协调组织内稀缺资源的有效分配，因此可作为信息系统的一个有力设计原则。

- move_code：CONTEXT_AND_VALUE

- statement_status：author_inference

- why_here_cn：开篇即建立IS领域的价值问题：把无货币匹配定位为信息系统设计原则，而非纯经济学理论。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：确立本文属于IS设计科学，而非纯粹机制设计。

- sets_up_next_cn：为引出效率、真实性与公平不可兼得的问题张本。

- failure_if_removed_cn：缺少IS定位，文章可能被视为纯经济理论或算法论文。

- evidence_pointer：Abstract, first sentence

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：众所周知，在匹配中不可能同时具备真实性、效率和公平（无嫉妒）这三个属性。

- move_code：CENTRAL_TENSION

- statement_status：prior_literature

- why_here_cn：摘要需要最快给出为什么需要新机制的答案：目标不可兼得。

- inherits_from_previous_cn：承接匹配作为设计原则的价值。

- changes_argument_state_cn：将问题从'为什么要匹配'推进到'现有匹配机制有何根本问题'。

- sets_up_next_cn：为既有机制二分法（要么高效要么无嫉妒）提供依据。

- failure_if_removed_cn：缺少核心张力，RESPCT的必要性无法确立。

- evidence_pointer：Abstract, second sentence

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：既有机制要么高效要么无嫉妒，而无嫉妒机制效率损失显著。

- move_code：GAP_ELABORATION

- statement_status：prior_literature

- why_here_cn：明确可选择的机制空间只有两个极端，为本文的中间地带铺路。

- inherits_from_previous_cn：由不可兼得定理推出机制选择的二分。

- changes_argument_state_cn：说明'标准答案'要么牺牲效率要么牺牲公平。

- sets_up_next_cn：引出需要设计同时保留效率与策略防护并压低嫉妒的新机制。

- failure_if_removed_cn：缺少效率损失的量化描述，读者不会感到非解决不可。

- evidence_pointer：Abstract, third sentence

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：我们关注匹配问题的一个广泛代表：课程分配，其中学生对课程有偏好，课程组织者对学生有优先级。

- move_code：PHENOMENON_FOCUS

- statement_status：fact

- why_here_cn：在摘要中把抽象问题具体化为可评价的实际场景。

- inherits_from_previous_cn：承接'匹配以偏好协调稀缺资源'的语境。

- changes_argument_state_cn：把问题从一般匹配收窄到一对多对象分配。

- sets_up_next_cn：介绍课程分配特有的约束。

- failure_if_removed_cn：缺少具体场景，后续的真实数据与政策改变便难以理解。

- evidence_pointer：Abstract, fourth sentence

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：课程分配的一个重要特征是每门课既有最大容量又有最低配额。

- move_code：KEY_CONSTRAINT

- statement_status：fact

- why_here_cn：本论文技术创新的核心前提：最低配额使简单保证不可行。

- inherits_from_previous_cn：承接课程分配场景。

- changes_argument_state_cn：引入现有文献普遍未处理的实际约束。

- sets_up_next_cn：将最低配额推广到其他应用领域。

- failure_if_removed_cn：没有最低配额，RESPCT的许多设计构件（扩展席位、保证向量最大化）失去意义。

- evidence_pointer：Abstract, fifth sentence

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：这一要求也出现在许多其他匹配应用，如学校选择、医院-住院医匹配、工人-岗位分配。

- move_code：GENERALIZATION

- statement_status：fact

- why_here_cn：证明最低配额不是单一应用的偶然性。

- inherits_from_previous_cn：承接课程分配中的最低配额。

- changes_argument_state_cn：提升问题的一般性，为后文科际推广提供支点。

- sets_up_next_cn：引出RESPCT作为广泛适用的机制。

- failure_if_removed_cn：若只有课程分配，IS贡献会被认为过于狭窄。

- evidence_pointer：Abstract, sixth sentence

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：我们引入扩展席位优先化锁定与交易、保证范围加宽的机制（RESPCT），它尊重最低配额且真实、高效、低嫉妒。

- move_code：ARTIFACT_INTRODUCTION

- statement_status：theory_claim

- why_here_cn：摘要必须给出解决方案的关键信息：机制名称和核心属性。

- inherits_from_previous_cn：由前三个句子的张力与缺口推出。

- changes_argument_state_cn：把'不可能'转成'可实现的工程方案'。

- sets_up_next_cn：解释嫉妒降低的原因。

- failure_if_removed_cn：没有制品名称与性质，摘要缺乏可操作贡献。

- evidence_pointer：Abstract, seventh sentence

### 8. Abstract S8

- order：8

- locator：Abstract S8

- paraphrase_cn：嫉妒的显著降低来自两个非常有效的启发式。

- move_code：MECHANISM_PREVIEW

- statement_status：empirical_result

- why_here_cn：把实证结果的核心原因浓缩为可记忆的两个创新，即为后文技术构件做摘要级预告。

- inherits_from_previous_cn：承接RESPCT的低嫉妒属性。

- changes_argument_state_cn：将贡献从'一个机制'细化到'两个可复用构件'。

- sets_up_next_cn：为正文第4节的clinching和prioritized pointing做铺垫。

- failure_if_removed_cn：没有机制层面的原因说明，读者会认为只是偶然的算法工程。

- evidence_pointer：Abstract, eighth sentence

### 9. Abstract S9

- order：9

- locator：Abstract S9

- paraphrase_cn：我们遵循设计科学方法，基于来自大规模课程分配应用的现场数据提供解析和实验结果。

- move_code：METHOD_DECLARATION

- statement_status：method_decision

- why_here_cn：IS读者需要知道评价方式：不是纯理论也不是纯实验。

- inherits_from_previous_cn：承接RESPCT及其构件。

- changes_argument_state_cn：把论文从'提出机制'推进到'如何证明有效'。

- sets_up_next_cn：预告真实数据和政策改变这一更强的证据。

- failure_if_removed_cn：缺少方法声明，贡献可能被视为纯算法论文。

- evidence_pointer：Abstract, ninth sentence

### 10. Abstract S10

- order：10

- locator：Abstract S10

- paraphrase_cn：这些结果带来政策改变，所提系统现在每学期被用于匹配数百名学生。

- move_code：IMPACT_CLAIM

- statement_status：empirical_result

- why_here_cn：用实际采纳证明机制的现实可行性，是设计科学论文最强的收尾证据。

- inherits_from_previous_cn：由现场数据成功直接推出。

- changes_argument_state_cn：把贡献从学术性质升级为组织层面的真实影响。

- sets_up_next_cn：摘要结束，引导读者进入引言中的完整论证。

- failure_if_removed_cn：缺少采纳证据，只能算模拟结果，削弱IS贡献。

- evidence_pointer：Abstract, final sentence

## 引言逐句图谱

### 1. Introduction P1 S1-S3

- order：1

- locator：Introduction P1 S1-S3

- paraphrase_cn：匹配理论始于Gale-Shapley婚姻问题：两个不同集合的参与者，在不能用货币辅助分配的条件下如何匹配成稳定婚姻集合。

- move_code：ORIGIN_ESTABLISHMENT

- statement_status：prior_literature

- why_here_cn：引言需要从学科源头建立权威性，并把'无货币'作为不可修改的前提。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：建立匹配理论并标明'无货币'是本领域核心约束。

- sets_up_next_cn：为说明稳定匹配与效率无张力的经典结果。

- failure_if_removed_cn：没有经典起点，整个IS定位会缺少理论根基。

- evidence_pointer：Introduction P1 S1-S3

### 2. Introduction P1 S4-S5

- order：2

- locator：Introduction P1 S4-S5

- paraphrase_cn：婚姻问题的核心是稳定匹配的存在性；由于稳定匹配在核中，所以是帕累托有效的，稳定与效率在此没有张力。

- move_code：PRIOR_RESULT

- statement_status：prior_literature

- why_here_cn：先给出一个没有张力的经典结果，以便后文对比学校/课程分配中的张力。

- inherits_from_previous_cn：稳定婚姻模型。

- changes_argument_state_cn：确立'稳定即有效'的语境。

- sets_up_next_cn：引出对象分配模型与公平问题。

- failure_if_removed_cn：没有这一无张力基准，后续效率-公平冲突的吃惊感会减弱。

- evidence_pointer：Introduction P1 S4-S5

### 3. Introduction P2 S1-S2

- order：3

- locator：Introduction P2 S1-S2

- paraphrase_cn：密切相关的问题是如何将代理匹配到对象；学校分配是重要例子，学校被视为'待消费对象'，学生优先级被视为'权利'。

- move_code：MODEL_SHIFT

- statement_status：prior_literature

- why_here_cn：从双边匹配转向对象分配，这是本文形式模型的基础。

- inherits_from_previous_cn：由婚姻问题引出'对象-代理'关系。

- changes_argument_state_cn：把研究问题从'均衡'改为'公平分配'。

- sets_up_next_cn：引出正当嫉妒的定义。

- failure_if_removed_cn：没有对象分配视角，课程分配的形式模型无从建立。

- evidence_pointer：Introduction P2 S1-S2

### 4. Introduction P2 S3-S5

- order：4

- locator：Introduction P2 S3-S5

- paraphrase_cn：学校分配的核心不是均衡而是公平：学生i若更想上j的学校且在该学校优先级更高，则i对j有正当嫉妒；无正当嫉妒即为公平。

- move_code：DEFINITION

- statement_status：fact

- why_here_cn：在引言中给出全文使用的公平性定义，使后文所有'更公平'可度量。

- inherits_from_previous_cn：学校为对象、优先级为权利。

- changes_argument_state_cn：确立公平性的形式判据。

- sets_up_next_cn：使课程分配与TTC/D A的对比可量化。

- failure_if_removed_cn：没有正当嫉妒定义，第5节的所有指标将无根基。

- evidence_pointer：Introduction P2 S3-S5

### 5. Introduction P3 S1-S2

- order：5

- locator：Introduction P3 S1-S2

- paraphrase_cn：我们关注教育机构内的课程分配，这是一对多对象分配（无转移）的广泛应用，与学校分配问题类似。

- move_code：PHENOMENON_FOCUS

- statement_status：fact

- why_here_cn：把一般理论收窄到主题域。

- inherits_from_previous_cn：学校分配的对象分配框架。

- changes_argument_state_cn：确立具体研究对象，为后文TUM应用铺路。

- sets_up_next_cn：介绍一对多与多对多的区别。

- failure_if_removed_cn：没有主题域，现场数据和政策采纳无从存在。

- evidence_pointer：Introduction P3 S1-S2

### 6. Introduction P3 S3-S5

- order：6

- locator：Introduction P3 S3-S5

- paraphrase_cn：课程分配可以是一对多或多对多；欧洲大学中一对多很常见，学生从许多研讨课或实验课中选一个；在TUM课程组织者提交学生排名，学生每学期只能选一门。

- move_code：PHENOMENON_DETAIL

- statement_status：fact

- why_here_cn：从一般课程分配落实到具体TUM场景，为现场数据正当化。

- inherits_from_previous_cn：一对多课程分配。

- changes_argument_state_cn：区分单位需求假设，为后文限制埋下伏笔。

- sets_up_next_cn：说明优先级来源的多样性，论证后文'异构偏好'的合理性。

- failure_if_removed_cn：缺少TUM场景，第2.4节和现场数据便没有落点。

- evidence_pointer：Introduction P3 S3-S5

### 7. Introduction P4 S1-S2

- order：7

- locator：Introduction P4 S1-S2

- paraphrase_cn：课程分配虽具体，但与学校选择、大学录取、军校分支匹配、医院-住院医匹配、难民安置和劳动力市场相似；关键区别是课程通常要求最低学生数。

- move_code：GENERALIZATION_AND_DISTINCTION

- statement_status：fact

- why_here_cn：连接具体应用到广泛场景，说明最低配额这个特征的重要性。

- inherits_from_previous_cn：课程分配的一对多模型。

- changes_argument_state_cn：把最低配额确立为本文区别于既有文献的关键约束。

- sets_up_next_cn：为RESPCT的配额扩展提供一般性需求。

- failure_if_removed_cn：若最低配额没有普遍性，RESPCT的额外复杂度就不值得。

- evidence_pointer：Introduction P4 S1-S2

### 8. Introduction P5 S1-S3

- order：8

- locator：Introduction P5 S1-S3

- paraphrase_cn：效率、公平和激励相容是匹配与课程分配的核心设计目标，分别对应帕累托效率、无嫉妒和策略防护。

- move_code：DESIGN_DESIDERATA

- statement_status：prior_literature

- why_here_cn：明确评价机制的三把尺子，后文所有定理与实验都围绕它们。

- inherits_from_previous_cn：公平定义与匹配理论。

- changes_argument_state_cn：建立设计目标体系。

- sets_up_next_cn：转入三目标不可兼得的中心张力。

- failure_if_removed_cn：没有这三个目标，RESPCT的'策略防护、帕累托效率、低嫉妒'无从评价。

- evidence_pointer：Introduction P5 S1-S3

### 9. Introduction P5 S4-S6

- order：9

- locator：Introduction P5 S4-S6

- paraphrase_cn：课程分配、学校选择或任何对象有优先级的分配中，并不总存在公平且帕累托有效的匹配（Abdulkadiroglu & Sonmez 2003）。

- move_code：IMPOSSIBILITY

- statement_status：prior_literature

- why_here_cn：用已有定理确立问题边界：不能同时满足全部目标。

- inherits_from_previous_cn：三个设计目标。

- changes_argument_state_cn：转成'必须放宽某个目标'的工程问题。

- sets_up_next_cn：为'如何最小化嫉妒'的研究问题提供合法性。

- failure_if_removed_cn：若三目标可兼得，RESPCT的整个存在理由消失。

- evidence_pointer：Introduction P5 S4-S6

### 10. Introduction P6 S1-S4

- order：10

- locator：Introduction P6 S1-S4

- paraphrase_cn：IS文献强调激励对齐，如供应链协调、电子市场，但几乎所有工作集中在基于拍卖的机制；本文不要求货币转移，从而开放组织内外的许多新应用。

- move_code：IS_POSITIONING

- statement_status：prior_literature

- why_here_cn：把本文嵌入IS研究传统，同时标出'无货币匹配'是文献空白。

- inherits_from_previous_cn：效率、公平、激励相容的目标。

- changes_argument_state_cn：由纯匹配理论转向IS设计科学定位。

- sets_up_next_cn：为Gregor-Hevner设计科学框架的出现铺垫。

- failure_if_removed_cn：没有IS定位，论文会与ISR读者脱节。

- evidence_pointer：Introduction P6 S1-S4

### 11. Introduction P7 Purpose

- order：11

- locator：Introduction P7 Purpose

- paraphrase_cn：本研究是匹配偏好的设计科学贡献，引入策略防护且完全效率且低嫉妒的机制，并考虑最低配额。

- move_code：CONTRIBUTION_CLAIM

- statement_status：contribution_claim

- why_here_cn：在引入具体设计框架前最直接地预告贡献。

- inherits_from_previous_cn：IS文献缺口与三目标不可能性。

- changes_argument_state_cn：将缺口转化为可交付的制品。

- sets_up_next_cn：为Gregor-Hevner框架的四要素（目的、范围、方法、评价）做导引。

- failure_if_removed_cn：缺此句，引言前五段的张力缺少出口。

- evidence_pointer：Introduction P7, Purpose bullet

### 12. Introduction P7 Method + Artifact

- order：12

- locator：Introduction P7 Method + Artifact

- paraphrase_cn：方法上先提出算法并形式证明，然后用大规模应用现场数据实施制品并评价，最多每年7000名学生；这些数据显示嫉妒减少并促成TUM采用。

- move_code：METHOD_AND_IMPACT

- statement_status：method_decision

- why_here_cn：说明设计科学路径的具体形态，并提前给出采纳证据。

- inherits_from_previous_cn：Purpose bullet中的贡献声明。

- changes_argument_state_cn：把贡献从'机制性质'扩展为'实际部署'。

- sets_up_next_cn：使读者预期第4、5节的算法与评价。

- failure_if_removed_cn：缺少方法与评价说明，设计科学定位不完整。

- evidence_pointer：Introduction P7 Method and Artifact bullets

### 13. Introduction P8 S1-S2

- order：13

- locator：Introduction P8 S1-S2

- paraphrase_cn：全文结构遵循Gregor和Hevner（2013）的发表模板，并列出各章节内容。

- move_code：ROADMAP

- statement_status：method_decision

- why_here_cn：用IS设计科学惯例给读者导航。

- inherits_from_previous_cn：设计科学定位。

- changes_argument_state_cn：把论证组织成可预期的流程。

- sets_up_next_cn：进入第2节文献综述。

- failure_if_removed_cn：没有路线图，读者难以判断后文各节的论证角色。

- evidence_pointer：Introduction P8 S1-S2

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：从Gale-Shapley婚姻问题开启学科传统。

- development_move_cn：给出稳定匹配的定义、性质与无货币前提。

- pivot_move_cn：由'稳定即有效'转向对象分配模型。

- closing_move_cn：为下一段学校分配做铺垫。

- paragraph_job_cn：建立无货币匹配的权威背景，确立经典理论起点。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：引入学校分配问题作为对象分配的代表。

- development_move_cn：解释优先级作为权利、公平作为正当嫉妒的消除。

- pivot_move_cn：从均衡转向公平。

- closing_move_cn：结束公平定义，为课程分配与TUM场景做衔接。

- paragraph_job_cn：把'匹配'落实为'对象-代理分配'，给出全文公平性定义。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：直接将焦点收窄到课程分配。

- development_move_cn：区分一对多与多对多，描述TUM的研讨会与实验课场景。

- pivot_move_cn：从一般欧洲大学背景转到TUM具体操作。

- closing_move_cn：以课程组织者优先级多样性结尾，为'异构偏好'埋伏笔。

- paragraph_job_cn：建立具体应用场景的真实性与数据来源合法性。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：指出课程分配与多种匹配应用的相似性。

- development_move_cn：列举学校选择、军校、医院匹配、难民安置、劳动市场。

- pivot_move_cn：收窄到'最低配额'作为关键区别。

- closing_move_cn：强调最低配额在多个领域的重要性，为RESPCT的配额扩展做需求声明。

- paragraph_job_cn：将具体应用一般化，并确立最低配额作为本文的技术难点。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：明确三个设计目标：效率、公平、激励相容。

- development_move_cn：分别定义帕累托效率、无嫉妒与策略防护。

- pivot_move_cn：用Abdulkadiroglu & Sonmez定理给出三目标不可兼得。

- closing_move_cn：把'不可能'转成'需要新机制'。

- paragraph_job_cn：为RESPCT提供目标函数与约束条件。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：将问题嵌入IS文献。

- development_move_cn：引用Ba et al.与后续拍卖与电子市场文献，强调激励对齐而不设计。

- pivot_move_cn：指出几乎所有IS市场设计文献聚焦拍卖，本文补充无货币匹配。

- closing_move_cn：以新应用领域（任务分配、手术室、课程座位）收尾。

- paragraph_job_cn：论述为什么这个问题是IS问题而非纯经济学问题。

### 7. Introduction P7

- locator：Introduction P7

- opening_move_cn：声明本文是设计科学贡献。

- development_move_cn：按Gregor-Hevner框架列出目的、范围、方法、制品与评价。

- pivot_move_cn：从设计科学原则落实到TUM的实证结果与采纳。

- closing_move_cn：强调遵循Hevner七条设计科学指南。

- paragraph_job_cn：给出贡献的官方定位和验证标准。

### 8. Introduction P8

- locator：Introduction P8

- opening_move_cn：以论文结构作为收尾。

- development_move_cn：简要概述第2至7节各自功能。

- pivot_move_cn：无。

- closing_move_cn：宣布进入文献综述。

- paragraph_job_cn：为全文提供路线图。

## 理论到设计逐句图谱

### 1. Section 2.1 P1

- order：1

- locator：Section 2.1 P1

- paraphrase_cn：市场设计者通常只能在两种策略防护机制间选择：TTC（策略防护且高效但不无嫉妒）和DA（策略防护且无嫉妒但不高效）。

- move_code：BASELINE_DICHOTOMY

- statement_status：prior_literature

- why_here_cn：理论部分开篇设置机制选择空间，后续所有设计都在试图突破这一二分。

- inherits_from_previous_cn：引言的三个设计目标。

- changes_argument_state_cn：把'可选择机制'收缩为两个既定选项，突出缺口。

- sets_up_next_cn：为TTC的细节讨论提供入口。

- failure_if_removed_cn：缺少二分法，clinching与prioritized pointing的增量价值无从建立。

- evidence_pointer：Section 2.1 P1

### 2. Section 2.1 P2-P3, Example 1

- order：2

- locator：Section 2.1 P2-P3, Example 1

- paraphrase_cn：描述Shapley-Scarf住房市场与TTC的循环机制，并用四代理例子说明算法步骤。

- move_code：MECHANISM_EXPLICATION

- statement_status：prior_literature

- why_here_cn：读者需要精确理解TTC，才能理解后文两个改进构件针对的具体环节。

- inherits_from_previous_cn：TTC作为高效机制。

- changes_argument_state_cn：使TTC的内部循环结构成为可操作对象。

- sets_up_next_cn：引出Roth策略防护与Ma唯一性定理。

- failure_if_removed_cn：不熟悉TTC循环的读者无法追踪PCT/RESPCT的算法差异。

- evidence_pointer：Section 2.1 P2-P3

### 3. Section 2.1 P4-P6

- order：3

- locator：Section 2.1 P4-P6

- paraphrase_cn：Roth证明TTC策略防护，Ma证明其唯一性；Pápai和Pycia-Unver推广到层级交换规则；Abdulkadiroglu-Sonmez将TTC自然改造到对象分配。

- move_code：THEORETICAL_BACKBONE

- statement_status：prior_literature

- why_here_cn：建立TTC的理论地位，说明为什么以TTC为底版而非其他机制。

- inherits_from_previous_cn：TTC算法定义。

- changes_argument_state_cn：赋予TTC不可替代的理论权威，使改进TTC比推翻TTC更有价值。

- sets_up_next_cn：介绍课程分配与住房市场的两点差异（多容量、无所有权）。

- failure_if_removed_cn：TTC的独特性不被确立，后文所有Clinching/PCT定理显得无锚点。

- evidence_pointer：Section 2.1 P4-P6

### 4. Section 2.1 P7-P8

- order：4

- locator：Section 2.1 P7-P8

- paraphrase_cn：课程分配与住房分配不同：课程可容纳多人且无所有权；Abdulkadiroglu-Sonmez以学生指向最爱课程、课程指向最高优先级学生的方式自然改造TTC。

- move_code：ADAPTATION

- statement_status：prior_literature

- why_here_cn：标明本文使用的是一对多TTC版本，是后续所有嫉妒分析的底层算法。

- inherits_from_previous_cn：住房市场TTC。

- changes_argument_state_cn：把TTC从个体理性转向对象分配。

- sets_up_next_cn：为效率-嫉妒张力的分析准备条件。

- failure_if_removed_cn：若用住房市场TTC，后文'课程的优先级'概念便不成立。

- evidence_pointer：Section 2.1 P7-P8

### 5. Section 2.2 P1, Example 2

- order：5

- locator：Section 2.2 P1, Example 2

- paraphrase_cn：用三学生三课程例子展示唯一公平匹配被另一帕累托更优匹配支配，得出公平与帕累托效率冲突。

- move_code：IMPOSSIBILITY_ILLUSTRATION

- statement_status：empirical_result

- why_here_cn：用最小反例把抽象定理变成直观现象，为后文'必须放松公平'做铺垫。

- inherits_from_previous_cn：公平与效率定义。

- changes_argument_state_cn：证明在同一实例中不能同时获得公平与效率。

- sets_up_next_cn：引出对多单位TTC嫉妒程度知之甚少的文献空白。

- failure_if_removed_cn：没有反例，读者可能仍希望同时满足三个目标。

- evidence_pointer：Section 2.2 P1 and Example 2

### 6. Section 2.2 P2

- order：6

- locator：Section 2.2 P2

- paraphrase_cn：DA推荐明确因公平无嫉妒，但TTC推荐则不确定；多单位TTC的嫉妒程度研究少，DA在课程匹配中低效，TTC产生显著嫉妒，因此自然问题是：如何让高效机制尽可能少嫉妒。

- move_code：RESEARCH_QUESTION

- statement_status：author_inference

- why_here_cn：这是全文的核心研究问题声明，直接为RESPCT的设计目标设定方向。

- inherits_from_previous_cn：效率-公平不可能反例。

- changes_argument_state_cn：将'不可能'转化为'最小化嫉妒'的可优化目标。

- sets_up_next_cn：进入2.3节减少嫉妒与配额考虑的方法论。

- failure_if_removed_cn：没有研究问题，第4节的设计构件没有目的。

- evidence_pointer：Section 2.2 P2

### 7. Section 2.3 P1-P2

- order：7

- locator：Section 2.3 P1-P2

- paraphrase_cn：在无最低配额时，自然类比个体理性是尊重最高优先级：若课程有q容量，则q个最高优先级学生应被分配到该课程或更偏好课程，称为'保底'；指向保底学生中任一人都可保持'尊重最高优先级'。

- move_code：GUARANTEE_CONCEPT

- statement_status：theory_claim

- why_here_cn：引入'guaranteed students'概念，这是后文clinching与prioritized pointing的共同基石。

- inherits_from_previous_cn：对象分配TTC。

- changes_argument_state_cn：把公平性要求转化为可计算的保底集合。

- sets_up_next_cn：解释为何保底学生不产生嫉妒。

- failure_if_removed_cn：没有保底概念，clinching和σ-mutual best失去定义基础。

- evidence_pointer：Section 2.3 P1-P2

### 8. Section 2.3 P3-P4

- order：8

- locator：Section 2.3 P3-P4

- paraphrase_cn：如果保底学生把该课程排第一，分配给他不会造成嫉妒；只有当学生加入循环且不把自己指向的课程作第一志愿时，其在该课程的低优先级才可能制造嫉妒。设计者可利用课程优先级（机制已知）来指向更可能高优先级的保底学生，而非依赖学生自报偏好。

- move_code：MECHANISM_INTUITION

- statement_status：theory_claim

- why_here_cn：将'嫉妒'归结为低优先级学生进入非平凡交易循环，为prioritized pointing提供直接理论依据。

- inherits_from_previous_cn：保底概念与循环结构。

- changes_argument_state_cn：指出设计空间：指向谁是可自由选择的工具，而不会牺牲策略防护。

- sets_up_next_cn：引出'确定谁被保底是主要技术挑战'。

- failure_if_removed_cn：prioritized pointing的合理性将失去理论支撑。

- evidence_pointer：Section 2.3 P3-P4

### 9. Section 2.3 P5

- order：9

- locator：Section 2.3 P5

- paraphrase_cn：有最低配额时，简单'最高q个优先级'不再成立，需要Fragiadakis等人的扩展席位机制；ESTTC强组策略防护且帕累托有效，但不管嫉妒。

- move_code：ESTTC_INTRO

- statement_status：prior_literature

- why_here_cn：在理论综述中点名现有配额机制ESTTC，为RESPCT提供直接改进目标。

- inherits_from_previous_cn：技术挑战：确定保底学生。

- changes_argument_state_cn：把配额纳入理论框架，同时指出ESTTC的公平缺口。

- sets_up_next_cn：讨论ETTC的局限与真实数据比较文献。

- failure_if_removed_cn：RESPCT的配额部分将没有对比基准。

- evidence_pointer：Section 2.3 P5

### 10. Section 2.3 P6-P7

- order：10

- locator：Section 2.3 P6-P7

- paraphrase_cn：目前只有Abdulkadiroglu等用真实数据比较TTC（新奥尔良），但学校分配偏好同质、学生与对象比大；ETTC能减少TTC嫉妒但不支持最低配额，整合配额到ETTC是非平凡的。

- move_code：EMPIRICAL_GAP

- statement_status：prior_literature

- why_here_cn：用文献缺口为'用TUM现场数据'与'配额机制'制造空间。

- inherits_from_previous_cn：ESTTC作为配额基准。

- changes_argument_state_cn：指出既有真实数据证据稀缺、偏好结构不同。

- sets_up_next_cn：进入2.4节TUM实际背景。

- failure_if_removed_cn：缺少文献空白，现场数据贡献会显得重复。

- evidence_pointer：Section 2.3 P6-P7

### 11. Section 2.4 P1-P2

- order：11

- locator：Section 2.4 P1-P2

- paraphrase_cn：TUM计算机系有超过6000学生，每学期匹配2000-3000名学生，并被建筑、商、数学、机械等系采用；此前FCFS问题严重，2014年改为DA并被学生和教师视为重大改进。

- move_code：FIELD_CONTEXT

- statement_status：fact

- why_here_cn：给现场数据一个具体组织身份，并说明为什么DA被引入但仍有缺陷。

- inherits_from_previous_cn：课程分配的重要性。

- changes_argument_state_cn：从学术问题进入组织现实，为政策改变铺路。

- sets_up_next_cn：引出DA的缺陷与部门反思。

- failure_if_removed_cn：没有TUM背景，10个数据集的权威性下降。

- evidence_pointer：Section 2.4 P1-P2

### 12. Section 2.4 P3-P4

- order：12

- locator：Section 2.4 P3-P4

- paraphrase_cn：DA不允许最低配额且有显著效率损失；课程分配中偏好异构，学校选择中偏好同质使DA近似高效，但课程分配并非如此；初始分析显示TTC比DA效率损失小得多。

- move_code：CURRENT_MECHANISM_SHORTFALL

- statement_status：empirical_result

- why_here_cn：把'理论缺口'变成'组织已实际遭遇的问题'，为RESPCT引入设置现实理由。

- inherits_from_previous_cn：FCFS到DA的历史。

- changes_argument_state_cn：证明现有实际方案（DA）不满足课程分配需求。

- sets_up_next_cn：自然引入2.5节新机制RESPCT。

- failure_if_removed_cn：若DA已经完美，RESPCT只是锦上添花而非必要。

- evidence_pointer：Section 2.4 P3-P4

### 13. Section 2.5 P1-P2

- order：13

- locator：Section 2.5 P1-P2

- paraphrase_cn：我们提出RESPCT机制，学生到课程的嫉妒显著低于TTC和ESTTC，显式考虑最低配额，并适用于学校、军队、乡村医院等场景。

- move_code：ARTIFACT_PREVIEW

- statement_status：author_inference

- why_here_cn：在第2节末以预测式声明给出解决方案，使读者带着明确答案进入技术章节。

- inherits_from_previous_cn：DA的缺陷与课程分配的配额需求。

- changes_argument_state_cn：正式引入RESPCT并给其应用范围。

- sets_up_next_cn：预告形式特征与实证结果。

- failure_if_removed_cn：没有机制预告，第4节算法会显得突兀。

- evidence_pointer：Section 2.5 P1-P2

### 14. Section 2.5 P3

- order：14

- locator：Section 2.5 P3

- paraphrase_cn：我们理论刻画RESPCT的策略防护、效率与公平；利用TUM 10个27-733学生的分配集和多种配额场景，每场景嫉妒显著减少，因子三以上；与配额DA相比约10%学生可被帕累托改进。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：提前给出关键数字，让读者在技术细节前已知道结论。

- inherits_from_previous_cn：RESPCT的提出。

- changes_argument_state_cn：建立'这项设计有效'的预期。

- sets_up_next_cn：说明两个算法创新：优先指向与最大化保底席位。

- failure_if_removed_cn：若结果不能提前预告，第5节会显得缺乏方向。

- evidence_pointer：Section 2.5 P3

### 15. Section 2.5 P3-S4

- order：15

- locator：Section 2.5 P3-S4

- paraphrase_cn：嫉妒的大幅降低源于两个算法创新：prioritized pointing和最大化座位保底；二者组合显著减少正当嫉妒。

- move_code：MECHANISM_PREVIEW

- statement_status：author_inference

- why_here_cn：把复杂RESPCT简化为两个可命名构件，为第4节分节展开提供目录。

- inherits_from_previous_cn：结果预告。

- changes_argument_state_cn：将贡献从'机制整体'拆解为'两个创新构件'。

- sets_up_next_cn：第4节的4.1-4.4子节将分别论证。

- failure_if_removed_cn：后文部件化论证失去摘要级地图。

- evidence_pointer：Section 2.5 P3-S4

### 16. Section 2.5 P4

- order：16

- locator：Section 2.5 P4

- paraphrase_cn：策略防护、效率和极低嫉妒说服TUM计算机系将机制从DA切换为RESPCT，结果也适用于学校选择、医疗居民、大学录取等。

- move_code：IMPACT_AND_GENERALIZATION

- statement_status：empirical_result

- why_here_cn：以政策采纳为最强证据，并重申应用范围。

- inherits_from_previous_cn：RESPCT的三个性质与实证结果。

- changes_argument_state_cn：完成从'算法'到'制度采纳'的跳跃。

- sets_up_next_cn：为第3节形式模型建立逻辑起点。

- failure_if_removed_cn：没有采纳证据，RESPCT的社会影响无从体现。

- evidence_pointer：Section 2.5 P4

### 17. Section 3.1 P1-P2

- order：17

- locator：Section 3.1 P1-P2

- paraphrase_cn：将课程分配定义为元组(S,C,p,q,>_S,>_C)，给出学生偏好、课程优先级、最低配额、最大容量和单位需求假设。

- move_code：FORMAL_MODEL

- statement_status：fact

- why_here_cn：所有定理与算法的形式基础，必须在此处一次性落定。

- inherits_from_previous_cn：前面所有课程分配讨论。

- changes_argument_state_cn：从叙述性语言转为可验证的数学对象。

- sets_up_next_cn：定义可行匹配和机制。

- failure_if_removed_cn：没有形式模型，无法证明任何定理。

- evidence_pointer：Section 3.1 P1-P2

### 18. Section 3.1 Algorithm 1

- order：18

- locator：Section 3.1 Algorithm 1

- paraphrase_cn：给出TTC算法：学生指向有剩余容量的最爱课程，课程指向最高优先级学生，按循环分配。

- move_code：BASELINE_ALGORITHM

- statement_status：theory_claim

- why_here_cn：为后续PCT与RESPCT提供精细的操作基线。

- inherits_from_previous_cn：形式模型。

- changes_argument_state_cn：定义后文所有'改进'的起点。

- sets_up_next_cn：定义ESTTC扩展席位算法。

- failure_if_removed_cn：PCT/RESPCT与TTC的逐项对照无法进行。

- evidence_pointer：Section 3.1 Algorithm 1

### 19. Section 3.1 Algorithm 2 + Example 3

- order：19

- locator：Section 3.1 Algorithm 2 + Example 3

- paraphrase_cn：ESTTC将课程分为标准课和扩展课，扩展课按主列表指向学生，并以例子演示；其缺点是所有扩展席位都归一个学生，可被改进。

- move_code：QUOTA_BASELINE_ALGORITHM

- statement_status：theory_claim

- why_here_cn：ESTTC是RESPCT的直接改进对象，必须完全透明。

- inherits_from_previous_cn：TTC算法。

- changes_argument_state_cn：引入主列表机制并暴露其公平性缺陷。

- sets_up_next_cn：第3.2节设计目标与mutual best定义。

- failure_if_removed_cn：没有ESTTC，RESPCT的配额扩展无法定位改进。

- evidence_pointer：Section 3.1 Algorithm 2 and Example 3

### 20. Section 3.2 Definitions 1-3

- order：20

- locator：Section 3.2 Definitions 1-3

- paraphrase_cn：形式定义策略防护、帕累托效率和公平（无嫉妒）三个目标。

- move_code：DESIGN_DESIDERATA_FORMAL

- statement_status：fact

- why_here_cn：把摘要与引言中的目标转化为可证明与可测量的形式定义。

- inherits_from_previous_cn：形式模型。

- changes_argument_state_cn：建立定理与实验的判据。

- sets_up_next_cn：引入mutual best作为公平的放宽。

- failure_if_removed_cn：后续所有定理无法陈述。

- evidence_pointer：Section 3.2 Definitions 1-3

### 21. Section 3.2 Definition 4 + Mutual Best discussion

- order：21

- locator：Section 3.2 Definition 4 + Mutual Best discussion

- paraphrase_cn：定义mutual best：若s最爱c且s是c的q个最高优先级之一，则s必须被分配到c；满足mutual best的学生不会造成嫉妒。

- move_code：FAIRNESS_RELAXATION

- statement_status：theory_claim

- why_here_cn：为'尽可能公平'提供一个可计算的中间标准，而非完全无嫉妒。

- inherits_from_previous_cn：帕累托效率与无嫉妒的不可兼得。

- changes_argument_state_cn：将不可达目标替换为可达到目标。

- sets_up_next_cn：引入Theorem 1证明配额下mutual best不可实现。

- failure_if_removed_cn：σ-mutual best和最大化保底席位没有定义起点。

- evidence_pointer：Section 3.2 Definition 4

### 22. Section 3.2 Theorem 1

- order：22

- locator：Section 3.2 Theorem 1

- paraphrase_cn：在存在最低配额时，满足mutual best的匹配不一定存在。

- move_code：THEORETICAL_BOUNDARY

- statement_status：theory_claim

- why_here_cn：进一步把公平目标从mutual best推到σ-mutual best，为RESPCT的保底最大化赋予必要性。

- inherits_from_previous_cn：mutual best定义与形式模型。

- changes_argument_state_cn：将设计者从'追求mutual best'转移到'最大化σ'。

- sets_up_next_cn：引出Definition 5的σ-mutual best。

- failure_if_removed_cn：没有这个定理，σ-mutual best会被认为是人为弱化。

- evidence_pointer：Section 3.2 Theorem 1

### 23. Section 3.2 Definition 5

- order：23

- locator：Section 3.2 Definition 5

- paraphrase_cn：定义σ-mutual best：若s最爱c且s在c中处于前σ_c高优先级，则μ(c)=s；目标是最大化σ。

- move_code：DESIGN_TARGET

- statement_status：theory_claim

- why_here_cn：这是全文设计的数学目标：maximize σ. 后文第4.4节直接实现这个目标。

- inherits_from_previous_cn：Theorem 1的不可能性。

- changes_argument_state_cn：把公平性的工程目标形式化。

- sets_up_next_cn：第4节Artifact Description开始介绍机制。

- failure_if_removed_cn：RESPCT的'最大保底席位'部分没有数学依据。

- evidence_pointer：Section 3.2 Definition 5

### 24. Section 4 opening paragraph

- order：24

- locator：Section 4 opening paragraph

- paraphrase_cn：RESPCT的改进来自四步：无配额下的clinching、prioritized pointing，配额下的扩展，以及最大化保底席位。

- move_code：DESIGN_ROADMAP

- statement_status：author_inference

- why_here_cn：告知读者第4节的分节结构，与第2.5节的机制预告呼应。

- inherits_from_previous_cn：σ-mutual best目标。

- changes_argument_state_cn：把抽象目标拆成可按顺序构建的构件。

- sets_up_next_cn：4.1节clinching。

- failure_if_removed_cn：第4节内部没有清晰索引。

- evidence_pointer：Section 4 opening paragraph

### 25. Section 4.1 P1, Example 4

- order：25

- locator：Section 4.1 P1, Example 4

- paraphrase_cn：Morrill(2015b)已指出TTC中的不必要交易带来不公平却不贡献效率、策略防护或mutual best；在例子中s2被s1拖入循环，若允许s2直接clinch得到更公平且有效的结果。

- move_code：CLINCHING_MOTIVATION

- statement_status：theory_claim

- why_here_cn：第一个构件必须有明确理论来源和反例，才能证明clinching不是arbitrary改进。

- inherits_from_previous_cn：TTC循环结构。

- changes_argument_state_cn：证明'先clinch再交易'能消除不必要嫉妒。

- sets_up_next_cn：为Algorithm 3 PCT中的clinching阶段铺垫。

- failure_if_removed_cn：clinching不能单独成立，ESPCT与RESPCT也会失去公平性贡献。

- evidence_pointer：Section 4.1 P1 and Example 4

### 26. Section 4.2 P1-P3

- order：26

- locator：Section 4.2 P1-P3

- paraphrase_cn：TTC指向规则短视：总是让最高优先级学生交易，可能制造大量嫉妒；但可以指向任何保底学生而保留效率、mutual best和策略防护；在非平凡循环中学生的最终课程不是指向他的课程，因此其在该课程优先级无关。

- move_code：PRIORITIZED_POINTING_MOTIVATION

- statement_status：theory_claim

- why_here_cn：为prioritized pointing提供形式直觉：指针选择不影响核心性质。

- inherits_from_previous_cn：保底学生与循环结构。

- changes_argument_state_cn：把'指向谁'从任意选择转为一个设计变量。

- sets_up_next_cn：提出'平均优先级'启发式。

- failure_if_removed_cn：prioritized pointing的合法性不存在，后文RESPCT的低嫉妒将失去机制原因。

- evidence_pointer：Section 4.2 P1-P3

### 27. Section 4.2 P4

- order：27

- locator：Section 4.2 P4

- paraphrase_cn：设计者不能使用学生自报偏好（会破坏策略防护），但知道课程优先级；启发式为：课程c在保底学生中选择'其他课程平均优先级最高'者，并用剩余容量加权。

- move_code：HEURISTIC_RATIONALE

- statement_status：design_decision

- why_here_cn：指出启发式为何必须基于已知优先级而非自报偏好，是设计实现的关键约束。

- inherits_from_previous_cn：不能使用学生提交偏好。

- changes_argument_state_cn：设计决策落地为具体公式：平均优先级与容量权重。

- sets_up_next_cn：Algorithm 3 PCT。

- failure_if_removed_cn：PCT无法实现，RESPCT也失去核心指针规则。

- evidence_pointer：Section 4.2 P4

### 28. Section 4.2 Theorem 2

- order：28

- locator：Section 4.2 Theorem 2

- paraphrase_cn：PCT是帕累托有效、策略防护且满足mutual best。

- move_code：FORMAL_RESULT

- statement_status：theory_claim

- why_here_cn：用定理证明构件组合后的性质，说明改进不会牺牲效率与激励相容。

- inherits_from_previous_cn：Algorithm 3。

- changes_argument_state_cn：PCT成为一个可部署的机制。

- sets_up_next_cn：Theorem 3关于两门课条件的公平性。

- failure_if_removed_cn：PCT被证明无性质时，RESPCT整体性质也会崩。

- evidence_pointer：Section 4.2 Theorem 2

### 29. Section 4.2 Theorem 3 and Corollary 1

- order：29

- locator：Section 4.2 Theorem 3 and Corollary 1

- paraphrase_cn：两门课且总容量不小于学生数时，PCT是无嫉妒的；PCT这时等于学生提议DA；当课程数少时平均优先级预测能力最好。

- move_code：BOUNDARY_THEOREM

- statement_status：theory_claim

- why_here_cn：给出PCT何时完全公平的边界条件，也为后文'少课程、高容量'的优势解释提供定理。

- inherits_from_previous_cn：Theorem 2。

- changes_argument_state_cn：PCT的公平性从'启发式'升级为特定条件下的确定性性质。

- sets_up_next_cn：说明多于两门课仍有嫉妒，为配额扩展预留。

- failure_if_removed_cn：若没有此定理，后文关于'少课程场景RESPCT优势最大'的讨论无根据。

- evidence_pointer：Section 4.2 Theorem 3 and Corollary 1

### 30. Section 4.3 Algorithm 4 preamble

- order：30

- locator：Section 4.3 Algorithm 4 preamble

- paraphrase_cn：ESTTC作为层级交换规则，前p_c个座位按TTC继承，其余座位按主列表的序列独裁继承；利用'ESTTC保证每门课p_c个学生'这一观察，自然地把PCT改造成ESPCT。

- move_code：DESIGN_EXTENSION

- statement_status：theory_claim

- why_here_cn：把无配额构件clinching与prioritized pointing移植到配额市场。

- inherits_from_previous_cn：PCT和ESTTC的算法。

- changes_argument_state_cn：产生第一个配额版本机制ESPCT。

- sets_up_next_cn：给出Algorithm 4完整定义。

- failure_if_removed_cn：配额与无配额机制之间的桥梁断裂。

- evidence_pointer：Section 4.3 Algorithm 4 preamble

### 31. Section 4.3 Theorem 4 + Corollary 2

- order：31

- locator：Section 4.3 Theorem 4 + Corollary 2

- paraphrase_cn：ESTTC强组策略防护、帕累托有效、满足p-mutual best；ESPCT由此也满足这些性质。

- move_code：FORMAL_RESULT

- statement_status：theory_claim

- why_here_cn：证明ESPCT在引入构件后不丧失核心性质，且p-mutual best成立。

- inherits_from_previous_cn：Theorem 2和Theorem 4的证明。

- changes_argument_state_cn：ESPCT成为配额下的有效机制。

- sets_up_next_cn：指出p-mutual best不是最大保证，引出4.4节。

- failure_if_removed_cn：ESPCT的性质不清，RESPCT的对照实验失效。

- evidence_pointer：Section 4.3 Theorem 4 and Corollary 2

### 32. Section 4.3 final paragraph

- order：32

- locator：Section 4.3 final paragraph

- paraphrase_cn：ESTTC只保证p_c个学生，但这通常不是最大保证数；提高配额反而减少保证数并恶化公平，这是设计悖论，因此我们先用最大保证向量再加宽。

- move_code：DESIGN_PARADOX

- statement_status：author_inference

- why_here_cn：说明'为什么必须最大化σ'：标准ESTTC在高配额下反而更不公平，机制需要根本性修正。

- inherits_from_previous_cn：p-mutual best。

- changes_argument_state_cn：从'扩展席位机制'进入'保证向量优化'问题。

- sets_up_next_cn：直接过渡到4.4节最大保底席位。

- failure_if_removed_cn：最大化σ的设计步骤失去动机。

- evidence_pointer：Section 4.3 final paragraph

### 33. Section 4.4 P1-(FC)

- order：33

- locator：Section 4.4 P1-(FC)

- paraphrase_cn：为保证课程能保证超过最低配额的席位，需满足可行性条件(FC)：对任何课程子集C0，未在C0获得保底的学生数不得少于其他课程最低配额之和。

- move_code：DESIGN_CONSTRAINT

- statement_status：theory_claim

- why_here_cn：把'能否扩大保底'从口头上变成可检验的数学条件。

- inherits_from_previous_cn：最大化保证席位目标。

- changes_argument_state_cn：定义保证向量σ可行的判据。

- sets_up_next_cn：Theorems 5-7与MIP验证。

- failure_if_removed_cn：没有FC，任何σ扩张都会破坏最低配额可行性。

- evidence_pointer：Section 4.4 P1-(FC)

### 34. Section 4.4 Theorem 5-6

- order：34

- locator：Section 4.4 Theorem 5-6

- paraphrase_cn：若σ之和等于n且p≤σ≤q，则FC满足；在特定容量条件下σ=q可行。

- move_code：SUFFICIENT_CONDITIONS

- statement_status：theory_claim

- why_here_cn：给出何时可以轻松达到最大保底的理论保证。

- inherits_from_previous_cn：可行性条件。

- changes_argument_state_cn：缩小需要MIP计算的实例范围。

- sets_up_next_cn：Theorem 7关于强NP完全问题的困难性。

- failure_if_removed_cn：读者不知道哪些实例简单哪些困难。

- evidence_pointer：Section 4.4 Theorem 5-6

### 35. Section 4.4 Theorem 7

- order：35

- locator：Section 4.4 Theorem 7

- paraphrase_cn：判断σ是否与配额p不兼容是强NP完全问题，用顶点覆盖归约证明。

- move_code：COMPUTATIONAL_LIMIT

- statement_status：theory_claim

- why_here_cn：解释为什么需要一个MIP+greedy工程方案，而不是简单解析公式。

- inherits_from_previous_cn：FC的复杂性。

- changes_argument_state_cn：把设计任务从'理论可解'转到'工程可算'。

- sets_up_next_cn：引入Algorithm 5 greedy搜索。

- failure_if_removed_cn：MIP方法看起来多余；RESPCT部署时会误以为能直接解析。

- evidence_pointer：Section 4.4 Theorem 7

### 36. Section 4.4 MIP + Algorithm 5

- order：36

- locator：Section 4.4 MIP + Algorithm 5

- paraphrase_cn：用MIP验证σ与p兼容性，并给出greedy算法从下界p出发逐步增大σ直至不能增大，返回maximal向量。

- move_code：ENGINEERING_SOLUTION

- statement_status：method_decision

- why_here_cn：将NP难题转化为实际可执行的算法，是设计科学中'制品可实现'的关键。

- inherits_from_previous_cn：Theorem 7。

- changes_argument_state_cn：保证RESPCT在真实数据上可运行。

- sets_up_next_cn：Algorithm 6 RESPCT完整定义。

- failure_if_removed_cn：RESPCT无法计算σ，实验无法进行。

- evidence_pointer：Section 4.4 MIP formulation and Algorithm 5

### 37. Section 4.5 Algorithm 6 preamble

- order：37

- locator：Section 4.5 Algorithm 6 preamble

- paraphrase_cn：RESPCT将clinching与prioritized pointing扩展到扩展课程，并按σ在每轮动态重算保底；扩展课程可指向最多ε个不同学生，优先使用保底学生。

- move_code：ARTIFACT_SYNTHESIS

- statement_status：design_decision

- why_here_cn：把所有设计构件组装成最终制品，统领第4节。

- inherits_from_previous_cn：PCT、ESPCT、Algorithm 5的σ。

- changes_argument_state_cn：从'构件'到'完整机制'的状态跃迁。

- sets_up_next_cn：Example 7与Theorem 8/9验证。

- failure_if_removed_cn：RESPCT的定义不完整，实验无从谈起。

- evidence_pointer：Section 4.5 Algorithm 6 preamble

### 38. Section 4.5 Example 7

- order：38

- locator：Section 4.5 Example 7

- paraphrase_cn：同一市场例3在RESPCT下实现无嫉妒匹配，而ESTTC/ESPCT分别有4和2个嫉妒实例。

- move_code：ILLUSTRATIVE_CONTRAST

- statement_status：empirical_result

- why_here_cn：用一个具体例子直观展示RESPCT优于两个基准。

- inherits_from_previous_cn：Algorithm 6与Algorithm 2/4。

- changes_argument_state_cn：证明在同一个实例上RESPCT能实现无嫉妒。

- sets_up_next_cn：定理8/9形式化。

- failure_if_removed_cn：读者难以从算法文本看出公平性提升。

- evidence_pointer：Section 4.5 Example 7

### 39. Section 4.5 Theorem 8

- order：39

- locator：Section 4.5 Theorem 8

- paraphrase_cn：RESPCT满足策略防护、帕累托效率和σ-mutual best，且∑σ≥n。

- move_code：CORE_FORMAL_THEOREM

- statement_status：theory_claim

- why_here_cn：这是RESPCT的核心形式声明，与摘要中的'真实、高效、公平'直接对应。

- inherits_from_previous_cn：Algorithm 6与Theorem 5。

- changes_argument_state_cn：RESPCT从'被设计出的算法'升级为'被证明的机制'。

- sets_up_next_cn：Theorem 9给出更强边界条件。

- failure_if_removed_cn：RESPCT的所有理论贡献在此断裂。

- evidence_pointer：Section 4.5 Theorem 8

### 40. Section 4.5 Theorem 9

- order：40

- locator：Section 4.5 Theorem 9

- paraphrase_cn：在Σ_{c'≠c}q_c'+p_c≥n对所有课程成立时，RESPCT满足mutual best。

- move_code：STRONG_CONDITION_THEOREM

- statement_status：theory_claim

- why_here_cn：给出RESPCT在理想容量条件下能达到'更强公平'的条件，使理论贡献具有层次。

- inherits_from_previous_cn：Theorem 6与Theorem 8。

- changes_argument_state_cn：把'σ-mutual best'升级为'mutual best'的特殊情况。

- sets_up_next_cn：进入第5节评价。

- failure_if_removed_cn：RESPCT的公平性上限没有被刻画。

- evidence_pointer：Section 4.5 Theorem 9

## 制品设计理由逐句图谱

### 1. Section 4 opening P1 S1-S2

- order：1

- locator：Section 4 opening P1 S1-S2

- paraphrase_cn：说明RESPCT的公平改进来自四个部分：clinching、prioritized pointing、配额扩展、最大化保底席位。

- move_code：ARTIFACT_ARCHITECTURE

- statement_status：design_decision

- why_here_cn：把设计决策模块化，便于后续逐项验证。

- inherits_from_previous_cn：第2.5节的机制预告。

- changes_argument_state_cn：将综合制品拆解为可论证的构件。

- sets_up_next_cn：为每个构件提供独立子节。

- failure_if_removed_cn：读者无法追踪RESPCT的内部逻辑。

- evidence_pointer：Section 4 opening paragraph

### 2. Section 4.1 P1-S2

- order：2

- locator：Section 4.1 P1-S2

- paraphrase_cn：clinching设计选择：学生在交易前先锁定其保底且最爱的课程，消除不必要交易造成的不公平。

- move_code：CLINCHING_RATIONALE

- statement_status：design_decision

- why_here_cn：直接解释为什么首先加入clinching阶段。

- inherits_from_previous_cn：TTC循环结构。

- changes_argument_state_cn：说明clinching不损害效率、策略防护和mutual best（Morrill）。

- sets_up_next_cn：为PCT Algorithm 3的Clinching phase提供理由。

- failure_if_removed_cn：RESPCT vs ESTTC的公平性差异无法归因于第一个构件。

- evidence_pointer：Section 4.1 P1

### 3. Section 4.2 P1-P3

- order：3

- locator：Section 4.2 P1-P3

- paraphrase_cn：prioritized pointing设计选择：课程指向'其他课程平均优先级最高'的保底学生，而非最高优先级学生。

- move_code：POINTING_RATIONALE

- statement_status：design_decision

- why_here_cn：因为短视指针会导致低平均优先级学生进入循环制造嫉妒。

- inherits_from_previous_cn：非平凡循环中优先级无关的观察。

- changes_argument_state_cn：证明指针规则可从'最高优先级'改为'平均优先级'而不破坏性质。

- sets_up_next_cn：定义平均优先级指标的容量加权。

- failure_if_removed_cn：RESPCT与TTC在指针上没有区别，嫉妒无法降低。

- evidence_pointer：Section 4.2 P1-P3

### 4. Section 4.2 P4

- order：4

- locator：Section 4.2 P4

- paraphrase_cn：为什么使用平均优先级而不是自报偏好：使用提交偏好会破坏策略防护。

- move_code：STRATEGYPROOFNESS_CONSTRAINT

- statement_status：design_decision

- why_here_cn：这是设计约束的关键：机制不能依赖不可信信息。

- inherits_from_previous_cn：策略防护的硬性要求。

- changes_argument_state_cn：将指针设计约束到公开可观测数据上。

- sets_up_next_cn：指明平均优先级的容量加权细节。

- failure_if_removed_cn：指针规则会违反策略防护，RESPCT核心性质崩塌。

- evidence_pointer：Section 4.2 P4

### 5. Section 4.3 P2-S5

- order：5

- locator：Section 4.3 P2-S5

- paraphrase_cn：配额扩展设计的理由：ESTTC只能保证p_c个学生，但标准课与扩展课的组合可以继承PCT的clinching与pointing；ESPCT将扩展课按平均优先级主列表指向。

- move_code：QUOTA_EXTENSION_RATIONALE

- statement_status：design_decision

- why_here_cn：解释算法从无配额到配额如何透过扩展席位机制无损迁移。

- inherits_from_previous_cn：ESTTC的层级交换结构。

- changes_argument_state_cn：将PCT的性质移植到配额市场。

- sets_up_next_cn：为RESPCT的扩展课程处理提供原型。

- failure_if_removed_cn：RESPCT无法处理最低配额。

- evidence_pointer：Section 4.3 P2-S5 and Algorithm 4

### 6. Section 4.4 P1

- order：6

- locator：Section 4.4 P1

- paraphrase_cn：为什么最大化保底席位：占更大保证集合能够使clinching和prioritized pointing在更多学生上生效，从而降低嫉妒。

- move_code：MAXIMIZE_GUARANTEE_RATIONALE

- statement_status：author_inference

- why_here_cn：把两个构件与第四个构件相连：构件效果依赖保底集合大小。

- inherits_from_previous_cn：Theorem 4对p-mutual best的保证。

- changes_argument_state_cn：从'给定p'转向'优化σ'。

- sets_up_next_cn：引入可行性条件FC。

- failure_if_removed_cn：保底最大化成为无根据的选择，RESPCT的显著公平优势无解释。

- evidence_pointer：Section 4.4 P1

### 7. Section 4.4 MIP paragraph

- order：7

- locator：Section 4.4 MIP paragraph

- paraphrase_cn：为何用MIP：验证σ的FC兼容性可建模为MIP，虽然不能直接最大化σ，但贪心算法可在多项式步数内得到maximal向量。

- move_code：MIP_DESIGN_DECISION

- statement_status：method_decision

- why_here_cn：NPC结果要求务实工程方案，MIP+greedy是实现机制可用的必然选择。

- inherits_from_previous_cn：Theorem 7的强NP完全性。

- changes_argument_state_cn：把理论困难转化为工程可解。

- sets_up_next_cn：Algorithm 5作为RESPCT每轮调用的子程序。

- failure_if_removed_cn：RESPCT无法在真实数据上运行。

- evidence_pointer：Section 4.4 MIP paragraph

### 8. Section 4.5 preamble

- order：8

- locator：Section 4.5 preamble

- paraphrase_cn：RESPCT设计选择：将扩展课程也纳入clinching与prioritized pointing，并在每轮重算σ，让扩展席位不再只按主列表。

- move_code：FINAL_SYNTHESIS_RATIONALE

- statement_status：design_decision

- why_here_cn：这是完整制品最关键的设计决定：扩展课不再按主列表死板指向，而是动态优先保底学生。

- inherits_from_previous_cn：Algorithm 5的σ与PCT的指向规则。

- changes_argument_state_cn：RESPCT在扩展机制中保留了prioritized pointing的全部优点。

- sets_up_next_cn：定义Algorithm 6。

- failure_if_removed_cn：RESPCT会退化为ESPCT，公平优势消失。

- evidence_pointer：Section 4.5 preamble

### 9. Section 4.5 Algorithm 6 step 1

- order：9

- locator：Section 4.5 Algorithm 6 step 1

- paraphrase_cn：用Algorithm 5确定初始σ¹，并定义基于平均优先级的主列表。

- move_code：INITIALIZATION_DECISION

- statement_status：design_decision

- why_here_cn：确保机制在第一步就使用最大可行保底向量。

- inherits_from_previous_cn：Algorithm 5。

- changes_argument_state_cn：把σ作为一个动态变量贯穿整个机制。

- sets_up_next_cn：Clinching阶段按σ判定。

- failure_if_removed_cn：RESPCT的保底范围没有初始化，机制无法启动。

- evidence_pointer：Section 4.5 Algorithm 6 step 1

### 10. Section 4.5 Algorithm 6 Clinching phase

- order：10

- locator：Section 4.5 Algorithm 6 Clinching phase

- paraphrase_cn：Clinching设计：只要学生s不在指向课程且其优先级在σ_c内就分配给他，并在每轮后重新计算σ。

- move_code：DYNAMIC_CLINCHING_DECISION

- statement_status：design_decision

- why_here_cn：动态重算确保保底集合随市场剩余状态更新，扩大可clinch席位。

- inherits_from_previous_cn：Algorithm 5的每轮重算。

- changes_argument_state_cn：使clinching在配额市场下持续有效。

- sets_up_next_cn：Cycle Resolution阶段。

- failure_if_removed_cn：静态σ会错过可clinch的席位，公平性提升有限。

- evidence_pointer：Section 4.5 Algorithm 6 Clinching phase

### 11. Section 4.5 Algorithm 6 Cycle Resolution phase

- order：11

- locator：Section 4.5 Algorithm 6 Cycle Resolution phase

- paraphrase_cn：扩展课程指向：先让σ_c>p_c的扩展课按prioritized pointing指向，若指向学生数不足ε，再用主列表补充。

- move_code：EXTENDED_POINTING_DECISION

- statement_status：design_decision

- why_here_cn：在保持扩展席位数量上限ε的同时，让扩展课也优先考虑保底学生。

- inherits_from_previous_cn：ESPCT中扩展课只按ML指向的不足。

- changes_argument_state_cn：RESPCT与ESPCT在扩展课处理上的本质区别。

- sets_up_next_cn：Example 7验证。

- failure_if_removed_cn：扩展课仍按ML指向，RESPCT的嫉妒仍高。

- evidence_pointer：Section 4.5 Algorithm 6 Cycle Resolution phase

## Study开头、过渡与收束图谱

### 1. Section 5 opening P1

- locator：Section 5 opening P1

- study_or_phase：Evaluation overall

- opening_move_cn：说明评价方式：用TUM现场数据进行计算研究评价RESPCT的嫉妒水平。

- transition_function_cn：从理论章节转入实证章节，用'evaluate the level of envy'直接对应研究问题。

- closure_move_cn：为5.1数据描述做准备。

- evidence_pointer：Section 5 opening P1

### 2. Section 5.1 P2-P3

- locator：Section 5.1 P2-P3

- study_or_phase：Data description

- opening_move_cn：描述TUM数据：2014-2016年研讨会与实践课程注册数据，10个数据集，27-733学生，6-43门课。

- transition_function_cn：让读者判断外部效度。

- closure_move_cn：用TS1和TS2展示偏好和优先级异构性，为'为何RESPCT更公平'埋下原因。

- evidence_pointer：Section 5.1 P2-P3

### 3. Section 5.1 P4

- locator：Section 5.1 P4

- study_or_phase：Quota generation

- opening_move_cn：解释为什么设置p=3到7：课程最低配额尚未被实际使用，基于经验取现实范围。

- transition_function_cn：把单一机制测试扩展为50个实例的稳健检验。

- closure_move_cn：给出50个测试实例的总构造规则。

- evidence_pointer：Section 5.1 P4

### 4. Section 5.1 P5

- locator：Section 5.1 P5

- study_or_phase：Mechanisms and metrics

- opening_move_cn：列出比较机制ESTTC、ESPCT、RESPCT与ESDA，并定义三个公平指标。

- transition_function_cn：为后续三个结果子节设立评价方法。

- closure_move_cn：报告运行时间，指出最长139秒，实际可行。

- evidence_pointer：Section 5.1 P5

### 5. Section 5.2 opening P1

- locator：Section 5.2 opening P1

- study_or_phase：Fairness study

- opening_move_cn：报告σ=q在37/50实例可行，其余用Algorithm 5求maximal σ；ESTTC为随机主列表，取10次平均。

- transition_function_cn：建立公平性比较的实验条件，消除随机性混淆。

- closure_move_cn：为Figure 6的解释做准备。

- evidence_pointer：Section 5.2 P1

### 6. Section 5.2 P2-P5

- locator：Section 5.2 P2-P5

- study_or_phase：Fairness results

- opening_move_cn：呈现Figure 6：RESPCT在所有配额下嫉妒实例最少，即使未扩大保底，ESPCT也明显优于ESTTC。

- transition_function_cn：第2.5节的预告在此兑现：降低嫉妒来自两个构件。

- closure_move_cn：解释配额增加时RESPCT优势缩小、ESTTC/ESPCT反而变好的设计悖论。

- evidence_pointer：Section 5.2 P2-P5

### 7. Section 5.3 opening P1

- locator：Section 5.3 opening P1

- study_or_phase：Efficiency study

- opening_move_cn：声明评价目标：与公平机制ESDA对比RESPCT的效率优势。

- transition_function_cn：从公平转向效率，填补'无嫉妒机制效率损失'的引言缺口。

- closure_move_cn：报告'约10%学生可被帕累托改进'的量化损失。

- evidence_pointer：Section 5.3 P1

### 8. Section 5.3 P2

- locator：Section 5.3 P2

- study_or_phase：Efficiency results detail

- opening_move_cn：给出Figure 9与Table 8：RESPCT平均排名和等级分布远优于ESDA。

- transition_function_cn：证明RESPCT不是以效率换公平。

- closure_move_cn：用Table 9汇总p=5时所有机制的公平与效率。

- evidence_pointer：Section 5.3 P2

### 9. Section 5.4 P1

- locator：Section 5.4 P1

- study_or_phase：Scalability study

- opening_move_cn：介绍合成数据：最多2000学生、60-100门课程，偏好结构模仿现场数据。

- transition_function_cn：从现场样本跳到大规模部署问题。

- closure_move_cn：报告最大实例90分钟内可解，并确认现场结论在大规模数据下成立。

- evidence_pointer：Section 5.4 P1

### 10. Section 6 opening P1

- locator：Section 6 opening P1

- study_or_phase：Discussion opening

- opening_move_cn：把协调问题放回IS决策支持与设计科学传统，提出匹配偏好是市场设计的另一个支柱。

- transition_function_cn：从结果回到IS理论语境，开始贡献升级。

- closure_move_cn：重提TTC/ESTTC与DA/ESDA的权衡，为RESPCT定位。

- evidence_pointer：Section 6 opening P1

### 11. Section 6 P2

- locator：Section 6 P2

- study_or_phase：Mechanism contribution interpretation

- opening_move_cn：重述RESPCT的两个创新：非短视指向与最大化保底席位。

- transition_function_cn：把实证公平性归因到机制构件。

- closure_move_cn：强调ESPCT即使不扩大保底也改进，说明clinching+pointing自身有效。

- evidence_pointer：Section 6 P2

### 12. Section 6 P3

- locator：Section 6 P3

- study_or_phase：Boundary and design guidance

- opening_move_cn：声明若只关心公平则用DA，但效率几乎总重要。

- transition_function_cn：为避免过度声明，给出清晰立场并界定适用条件。

- closure_move_cn：指出无配额时RESPCT相对TTC优势更大，配额定m较小是最优场景。

- evidence_pointer：Section 6 P3

### 13. Section 6 P4

- locator：Section 6 P4

- study_or_phase：Computational feasibility and generalization

- opening_move_cn：给出实现要求：数学规划求解器与90分钟大规模上限。

- transition_function_cn：把结果推广到其他一对多匹配领域。

- closure_move_cn：声明RESPCT可作为许多一对多分配的治愈方案。

- evidence_pointer：Section 6 P4

### 14. Section 6 P5-P6

- locator：Section 6 P5-P6

- study_or_phase：Limitations

- opening_move_cn：列出不适用场景：复杂录取要求、非序数偏好、偏好依赖与多对象需求。

- transition_function_cn：为结论中的未来研究铺路。

- closure_move_cn：指出单位需求是最重要限制。

- evidence_pointer：Section 6 P5-P6

### 15. Section 7 P1

- locator：Section 7 P1

- study_or_phase：Conclusion opening

- opening_move_cn：重新表述公平-效率政策权衡。

- transition_function_cn：把RESPCT嵌入学校选择等更广讨论。

- closure_move_cn：重申最低配额在学校选择中也重要。

- evidence_pointer：Section 7 P1

### 16. Section 7 P2

- locator：Section 7 P2

- study_or_phase：Conclusion closing

- opening_move_cn：总结贡献：策略防护、高效、低嫉妒，并重提TUM政策改变。

- transition_function_cn：把论文端点放回政策采纳与理论意义。

- closure_move_cn：以单位需求作为最重要限制和未来方向结束。

- evidence_pointer：Section 7 P2

## 讨论与贡献逐句图谱

### 1. Section 6 P1 S1-S2

- order：1

- locator：Section 6 P1 S1-S2

- paraphrase_cn：协调是决策支持与设计科学经典话题，拍卖是该文献的重要部分，但货币转移常不可用；有偏好的匹配是市场设计的另一支柱，为信息系统设计提供重要机制。

- move_code：IS_RETURN

- statement_status：prior_literature

- why_here_cn：讨论开篇重新把技术结果放回IS学科脉络，防止成为纯算法论文。

- inherits_from_previous_cn：第2.5节的IS定位。

- changes_argument_state_cn：从'算法有效'升级为'学科贡献'。

- sets_up_next_cn：指出本文处理效率-公平权衡。

- failure_if_removed_cn：讨论会失去IS语境。

- evidence_pointer：Section 6 P1 S1-S2

### 2. Section 6 P1 S3

- order：2

- locator：Section 6 P1 S3

- paraphrase_cn：我们借助匹配理论最新进展，针对效率与公平的权衡做出设计科学贡献。

- move_code：CONTRIBUTION_RESTATEMENT

- statement_status：contribution_claim

- why_here_cn：直接声明贡献主题，统领整段讨论。

- inherits_from_previous_cn：引言中的设计科学定位。

- changes_argument_state_cn：把RESPCT定位为效率-公平权衡的解决方案。

- sets_up_next_cn：展开TTC/DA权衡细节。

- failure_if_removed_cn：贡献声明缺失，后文讨论无中心。

- evidence_pointer：Section 6 P1 S3

### 3. Section 6 P1 S4-S5

- order：3

- locator：Section 6 P1 S4-S5

- paraphrase_cn：TTC（或配额版ESTTC）产生正当嫉妒，DA（或ESDA）非常低效，效率损失显著，给设计者带来艰难权衡。

- move_code：PROBLEM_REFRAME

- statement_status：empirical_result

- why_here_cn：用一句话总结前文三个机制的问题，确立RESPCT的中间地带。

- inherits_from_previous_cn：第2节、5.2、5.3结果。

- changes_argument_state_cn：把问题固定为设计者必须面对的权衡。

- sets_up_next_cn：然后提出RESPCT如何破解该权衡。

- failure_if_removed_cn：讨论没有了问题抓手。

- evidence_pointer：Section 6 P1 S4-S5

### 4. Section 6 P2 S1

- order：4

- locator：Section 6 P2 S1

- paraphrase_cn：我们引入RESPCT，通过非短视指向与最大化保底席位，显著比ESTTC公平。

- move_code：MECHANISM_ATTRIBUTION

- statement_status：empirical_result

- why_here_cn：把实证结果归因于机制设计，给出因果解释。

- inherits_from_previous_cn：5.2结果。

- changes_argument_state_cn：从'结果'上升为'机制-原因'。

- sets_up_next_cn：讨论构件组合效应。

- failure_if_removed_cn：公平性提升没有可解释机制，贡献限于表象。

- evidence_pointer：Section 6 P2 S1

### 5. Section 6 P2 S2-S3

- order：5

- locator：Section 6 P2 S2-S3

- paraphrase_cn：是这些创新的组合造成嫉妒大幅减少；即使不扩大保底，仅clinching与prioritized pointing的ESPCT也显著优于ESTTC，印证两个构件各自有效。

- move_code：COMPONENT_DECOMPOSITION

- statement_status：empirical_result

- why_here_cn：通过ESPCT与ESTTC的对照，把RESPCT的总效果分解到两个构件。

- inherits_from_previous_cn：5.2中ESPCT vs ESTTC。

- changes_argument_state_cn：证明贡献不是单一算法技巧而是可复用构件。

- sets_up_next_cn：讨论设计者何时使用RESPCT。

- failure_if_removed_cn：RESPCT的优势无法归因，设计知识不可迁移。

- evidence_pointer：Section 6 P2 S2-S3

### 6. Section 6 P3 S1-S2

- order：6

- locator：Section 6 P3 S1-S2

- paraphrase_cn：如果设计者只关心公平，DA/ESDA是明确选择；但效率几乎总重要，设计者不愿浪费资源，而RESPCT完全有效且嫉妒很少。

- move_code：BOUNDARY_POSITION

- statement_status：author_inference

- why_here_cn：防止过度声明，诚实交代什么时候应选择传统机制。

- inherits_from_previous_cn：效率-公平权衡。

- changes_argument_state_cn：把RESPCT定位为'当效率首要且低嫉妒为优'时的选择。

- sets_up_next_cn：描述RESPCT最佳适用条件。

- failure_if_removed_cn：贡献会被认为不切实际或一概最优。

- evidence_pointer：Section 6 P3 S1-S2

### 7. Section 6 P3 S3-S5

- order：7

- locator：Section 6 P3 S3-S5

- paraphrase_cn：当配额相对总代理数比例低时RESPCT效果最好；无配额时RESPCT相对TTC优势比有配额时更大；其最适合最低配额相对容量较小的应用如课程分配。

- move_code：BOUNDARY_CONDITION

- statement_status：empirical_result

- why_here_cn：量化说明RESPCT的优势区间，回应用户可能问的'什么时候用'。

- inherits_from_previous_cn：5.2配额趋势结果。

- changes_argument_state_cn：把结果转成可操作设计指导。

- sets_up_next_cn：讨论计算可行性与其他领域。

- failure_if_removed_cn：缺少边界条件，设计知识不完整。

- evidence_pointer：Section 6 P3 S3-S5

### 8. Section 6 P4 S1-S3

- order：8

- locator：Section 6 P4 S1-S3

- paraphrase_cn：RESPCT可轻松实现于任何可用(ES)TTC或DA解决的匹配问题；需要数学规划求解器，2000学生100课程都可在90分钟内解。

- move_code：DEPLOYMENT_FEASIBILITY

- statement_status：empirical_result

- why_here_cn：为设计者给出工程可行性证据。

- inherits_from_previous_cn：5.4可扩展性结果。

- changes_argument_state_cn：把机制从概念推进到可部署系统。

- sets_up_next_cn：推广到新领域。

- failure_if_removed_cn：设计者会担心运行成本。

- evidence_pointer：Section 6 P4 S1-S3

### 9. Section 6 P4 S4

- order：9

- locator：Section 6 P4 S4

- paraphrase_cn：更大的匹配应用如课程分配、军校分支、住院医匹配通常每几个月才做一次，计算时间不是问题，因此RESPCT可服务许多一对多分配。

- move_code：GENERALIZATION

- statement_status：author_inference

- why_here_cn：从计算可行性推出更广适用性，符合设计科学的知识迁移。

- inherits_from_previous_cn：90分钟结论。

- changes_argument_state_cn：把RESPCT从TUM案例扩展为通用制品。

- sets_up_next_cn：讨论限制。

- failure_if_removed_cn：应用范围过窄，IS贡献受质疑。

- evidence_pointer：Section 6 P4 S4

### 10. Section 6 P5 S1-S3

- order：10

- locator：Section 6 P5 S1-S3

- paraphrase_cn：限制：RESPCT不适合复杂录取要求（如印度预留配额）；依赖完整、非自反、传递的序数偏好；偏好需独立私密。

- move_code：LIMITATION_ADMISSION

- statement_status：fact

- why_here_cn：诚实划出机制的能力边界，避免过度推销。

- inherits_from_previous_cn：偏好独立假设。

- changes_argument_state_cn：把贡献限定在特定偏好环境下。

- sets_up_next_cn：解释若偏好相互依赖，可改用优化模型但会失去策略防护。

- failure_if_removed_cn：缺乏边界声明，会被审稿人指责过度泛化。

- evidence_pointer：Section 6 P5 S1-S3

### 11. Section 6 P5 S4-S5

- order：11

- locator：Section 6 P5 S4-S5

- paraphrase_cn：若学生满意与结果依赖观察到的他人偏好，机制设计者可能改选数学优化模型，但会失去策略防护且可能找不到无嫉妒分配。

- move_code：ALTERNATIVE_TRADEOFF

- statement_status：prior_literature

- why_here_cn：说明为什么坚持序数独立偏好假设是合理的选择而非疏忽。

- inherits_from_previous_cn：局限性中的偏好依赖。

- changes_argument_state_cn：把限制转化为设计选择论证。

- sets_up_next_cn：讨论单位需求假设。

- failure_if_removed_cn：限制会显得是论文弱点而非有依据的取舍。

- evidence_pointer：Section 6 P5 S4-S5

### 12. Section 6 P6 S1-S2

- order：12

- locator：Section 6 P6 S1-S2

- paraphrase_cn：一对一分配文献的关键假设是单位需求，多对象分配（如课程表分配）更难，策略防护机制只有序列独裁；近年才有满足弱激励相容的随机机制。

- move_code：UNIT_DEMAND_LIMITATION

- statement_status：prior_literature

- why_here_cn：点出本文最重要限制，并用文献证明这是公认难题。

- inherits_from_previous_cn：课程分配单位需求假设。

- changes_argument_state_cn：把限制上升为整个领域的开放问题。

- sets_up_next_cn：结论中以单位需求作为未来方向。

- failure_if_removed_cn：结论缺少最重要的未来研究指向。

- evidence_pointer：Section 6 P6 S1-S2

### 13. Section 7 P1 S1-S3

- order：13

- locator：Section 7 P1 S1-S3

- paraphrase_cn：公平与效率权衡在匹配应用中构成重大政策问题，公平常被优先；我们证明合适算法可实现高效且极低嫉妒，这可能是TTC在学校选择等其他应用中的论据。

- move_code：POLICY_CONTRIBUTION

- statement_status：author_inference

- why_here_cn：在结论中把技术结果转化为公共政策论点。

- inherits_from_previous_cn：6.3的边界讨论。

- changes_argument_state_cn：把RESPCT放入学校选择等长期争论。

- sets_up_next_cn：重申最低配额对学校的意义。

- failure_if_removed_cn：结论变成纯算法总结，失去IS影响力。

- evidence_pointer：Section 7 P1 S1-S3

### 14. Section 7 P2 S1

- order：14

- locator：Section 7 P2 S1

- paraphrase_cn：总之，我们提供策略防护、高效且低嫉妒的机制，这是TUM从DA切换到RESPCT的主要理由。

- move_code：CONTRIBUTION_SUMMARY

- statement_status：contrib_claim

- why_here_cn：一句话总结全部贡献，并用实际采纳作为证明。

- inherits_from_previous_cn：整篇论文。

- changes_argument_state_cn：闭环到引言的贡献预告。

- sets_up_next_cn：推广到医疗、军校、学校选择。

- failure_if_removed_cn：论文缺少终点总结。

- evidence_pointer：Section 7 P2 S1

### 15. Section 7 P2 S2-S3

- order：15

- locator：Section 7 P2 S2-S3

- paraphrase_cn：类似考虑也应适用于医疗劳动力、军校分支匹配或学校选择，那里长期争论DA vs TTC；RESPCT是无货币一对多对象分配的通用工具，是分布式信息系统设计的有力手段。

- move_code：FINAL_GENERALIZATION

- statement_status：author_inference

- why_here_cn：完成从单一应用向设计知识库的迁移。

- inherits_from_previous_cn：第2.5节的应用范围。

- changes_argument_state_cn：确立RESPCT作为可复用设计制品的地位。

- sets_up_next_cn：最后提及单位需求这一最大限制。

- failure_if_removed_cn：贡献会被视为TUM一次性案例。

- evidence_pointer：Section 7 P2 S2-S3

### 16. Section 7 P2 S4

- order：16

- locator：Section 7 P2 S4

- paraphrase_cn：单位需求假设是最严重也最具挑战的限制，正吸引大量关注，扩展它将显著增加匹配偏好的应用。

- move_code：FUTURE_RESEARCH

- statement_status：author_inference

- why_here_cn：以未来方向收尾，给领域留下延伸点。

- inherits_from_previous_cn：第6.6节单位需求讨论。

- changes_argument_state_cn：论文闭环并指向下一步研究。

- sets_up_next_cn：结束全文。

- failure_if_removed_cn：结尾显得封闭，缺乏对学科前景的展望。

- evidence_pointer：Section 7 P2 S4

## Study累积逻辑

### 1. 1

- study_or_phase：Phase 1: Formal model and impossibility (Section 3)

- evidence_job_cn：建立评价语言和设计目标，证明公平与效率(尤其mutual best)在配额下不可兼得。

- what_it_establishes_cn：为什么需要放宽公平，以及σ-mutual best为何是合适的放宽。

- what_it_cannot_establish_cn：没有任何证据说明有机制能实际降低嫉妒而不牺牲效率或策略防护。

- why_next_phase_is_needed_cn：形式语言需要具体构件来落实。

- transition_wording_function_cn：第4节开头说'包含几项创新'，把理论缺口接到设计。

### 2. 2

- study_or_phase：Phase 2: No-quota components PCT (Section 4.1-4.2)

- evidence_job_cn：证明clinching和prioritized pointing各自能降低嫉妒，且保留帕累托效率、策略防护与mutual best。

- what_it_establishes_cn：构件层面的因果有效性：不必要交易与短视指针是嫉妒的来源。

- what_it_cannot_establish_cn：无法解决最低配额问题，也没有在真实数据上验证。

- why_next_phase_is_needed_cn：课程分配需要最低配额，无配额机制不能直接使用。

- transition_wording_function_cn：'biggest challenge...incorporating minimum quotas'把问题转向配额。

### 3. 3

- study_or_phase：Phase 3: Quota extension and σ maximization (Section 4.3-4.4)

- evidence_job_cn：把PCT构件移植到配额市场并证明ESPCT性质；证明最大化保底向量可行且有必要，给出MIP+greedy计算工具。

- what_it_establishes_cn：配额不是简单约束，而是需要专门设计的保证席位问题；σ可以扩大。

- what_it_cannot_establish_cn：尚未说明这些构件和σ最大化组合起来的完整机制在数据上有多好。

- why_next_phase_is_needed_cn：需要一个同时使用全部构件的完整机制。

- transition_wording_function_cn：'As a result...we define range-widened...'把构件合成RESPCT。

### 4. 4

- study_or_phase：Phase 4: Complete artifact RESPCT and formal theorems (Section 4.5)

- evidence_job_cn：给出完整算法和形式定理（策略防护、帕累托效率、σ-mutual best，特定条件下mutual best）。

- what_it_establishes_cn：RESPCT作为机制的形式保证。

- what_it_cannot_establish_cn：实际数据上的公平性、效率与可扩展性。

- why_next_phase_is_needed_cn：设计科学必须展示现场可行性。

- transition_wording_function_cn：第5节开头'In order to evaluate...we conducted computational study'从定理转向证据。

### 5. 5

- study_or_phase：Phase 5a: Field-data fairness evaluation (Section 5.1-5.2)

- evidence_job_cn：在真实异构偏好和优先级数据上，证明RESPCT显著优于ESTTC和ESPCT的公平性。

- what_it_establishes_cn：机制在真实场景中降低嫉妒，且构件分解（ESPCT vs ESTTC）支持各个设计决策。

- what_it_cannot_establish_cn：相对无嫉妒公平机制（如ESDA）的效率损失有多大；大规模计算是否可行。

- why_next_phase_is_needed_cn：只证明'更公平'不足以说服实践者，若效率损失巨大则仍是权衡。

- transition_wording_function_cn：'In order to evaluate the gains in efficiency...we also implemented ESDA'引出效率对照。

### 6. 6

- study_or_phase：Phase 5b: Efficiency vs ESDA (Section 5.3)

- evidence_job_cn：证明RESPCT相对公平机制ESDA在效率和排名分布上的显著优势。

- what_it_establishes_cn：RESPCT不仅公平而且高效，约10%学生可被帕累托改进，效率不是牺牲品。

- what_it_cannot_establish_cn：在更大规模（2000学生以上）时运行是否可行；与其他领域的通用性。

- why_next_phase_is_needed_cn：大规模部署需要一个可扩展性证据。

- transition_wording_function_cn：'In order to evaluate how well our algorithms scale, we generated synthetic data'引出规模测试。

### 7. 7

- study_or_phase：Phase 5c: Scalability (Section 5.4)

- evidence_job_cn：用合成数据证明RESPCT可扩展至2000学生、100课程，并确认公平性与效率结论在大规模下成立。

- what_it_establishes_cn：RESPCT有实际部署的计算可行性。

- what_it_cannot_establish_cn：TUM之外领域的迁移效果、真实部署后学生行为与满意度。

- why_next_phase_is_needed_cn：把局部结果转化为可复用设计知识。

- transition_wording_function_cn：第6节讨论把结果放回IS与设计科学传统。

### 8. 8

- study_or_phase：Phase 6: Discussion and general design knowledge (Section 6-7)

- evidence_job_cn：把经验结果上升为设计原则和理论贡献，界定边界并给出未来方向。

- what_it_establishes_cn：RESPCT作为无货币一对多分配的通用工具，以及每种构件在什么条件下有效。

- what_it_cannot_establish_cn：跨领域实证推广。

- why_next_phase_is_needed_cn：无；论文到此收束。

- transition_wording_function_cn：讨论从问题重述到贡献、边界、限制、未来。

## 主张—证据台账

### 1. RESPCT满足策略防护、帕累托效率和σ-mutual best且∑σ≥n。

- claim_cn：RESPCT满足策略防护、帕累托效率和σ-mutual best且∑σ≥n。

- claim_level：theory

- supporting_evidence_cn：Theorem 8的证明，附录补充。

- support_strength：direct

- where_claim_is_made：Section 4.5 Theorem 8

- where_evidence_is_provided：Section 4.5 Theorem 8 and Appendix

### 2. 在配额下，满足mutual best的匹配不一定存在。

- claim_cn：在配额下，满足mutual best的匹配不一定存在。

- claim_level：theory

- supporting_evidence_cn：Theorem 1的反例。

- support_strength：direct

- where_claim_is_made：Section 3.2 Theorem 1

- where_evidence_is_provided：Section 3.2 Theorem 1 proof

### 3. 验证σ与最低配额向量p不兼容是强NP完全问题。

- claim_cn：验证σ与最低配额向量p不兼容是强NP完全问题。

- claim_level：theory

- supporting_evidence_cn：Theorem 7从顶点覆盖的强NP完全归约。

- support_strength：direct

- where_claim_is_made：Section 4.4 Theorem 7

- where_evidence_is_provided：Section 4.4 Theorem 7 and Appendix proof

### 4. PCT在无配额时是帕累托有效、策略防护且满足mutual best。

- claim_cn：PCT在无配额时是帕累托有效、策略防护且满足mutual best。

- claim_level：theory

- supporting_evidence_cn：Theorem 2证明，Appendix。

- support_strength：direct

- where_claim_is_made：Section 4.2 Theorem 2

- where_evidence_is_provided：Section 4.2 Theorem 2 and Appendix

### 5. 两门课且容量足够时PCT等于学生提议DA，因此无嫉妒。

- claim_cn：两门课且容量足够时PCT等于学生提议DA，因此无嫉妒。

- claim_level：theory

- supporting_evidence_cn：Theorem 3和Corollary 1证明。

- support_strength：direct

- where_claim_is_made：Section 4.2 Theorem 3 and Corollary 1

- where_evidence_is_provided：Section 4.2 Theorem 3, Corollary 1 and Appendix

### 6. RESPCT在所有配额水平上显著降低正当嫉妒实例数。

- claim_cn：RESPCT在所有配额水平上显著降低正当嫉妒实例数。

- claim_level：artifact

- supporting_evidence_cn：Figure 6：RESPCT在50个实例中嫉妒最低。

- support_strength：direct

- where_claim_is_made：Section 5.2

- where_evidence_is_provided：Section 5.2 Figure 6

### 7. 仅clinching与prioritized pointing（ESPCT）已显著改善公平性。

- claim_cn：仅clinching与prioritized pointing（ESPCT）已显著改善公平性。

- claim_level：mechanism

- supporting_evidence_cn：Figure 6-8中ESPCT vs ESTTC，即使没有扩大保底。

- support_strength：direct

- where_claim_is_made：Section 5.2 and Section 6 P2

- where_evidence_is_provided：Section 5.2 Figures 6-8

### 8. RESPCT效率远高于公平机制ESDA。

- claim_cn：RESPCT效率远高于公平机制ESDA。

- claim_level：artifact

- supporting_evidence_cn：Table 8和Figure 9：RESPCT平均排名和等级分布更好，约10%学生可被ESDA帕累托改进。

- support_strength：direct

- where_claim_is_made：Section 5.3

- where_evidence_is_provided：Section 5.3 Table 8 and Figure 9

### 9. RESPCT可扩展至2000学生、100课程，90分钟内可解。

- claim_cn：RESPCT可扩展至2000学生、100课程，90分钟内可解。

- claim_level：artifact

- supporting_evidence_cn：Section 5.4合成数据实验，最大实例运行时间有限。

- support_strength：direct

- where_claim_is_made：Section 5.4

- where_evidence_is_provided：Section 5.4

### 10. RESPCT被TUM计算机系采用并每学期匹配数百名学生。

- claim_cn：RESPCT被TUM计算机系采用并每学期匹配数百名学生。

- claim_level：artifact

- supporting_evidence_cn：作者在摘要、引言与结论中的陈述。

- support_strength：partial

- where_claim_is_made：Abstract, Introduction P7, Section 2.5 P4, Section 7 P2

- where_evidence_is_provided：作者自我报告，无独立部署后数据

### 11. ESPCT/ESTTC在高配额下反而更公平是因为扩展席位减少。

- claim_cn：ESPCT/ESTTC在高配额下反而更公平是因为扩展席位减少。

- claim_level：mechanism

- supporting_evidence_cn：Section 5.2中的配额趋势与Section 4.3的设计悖论解释。

- support_strength：direct

- where_claim_is_made：Section 5.2 P3-P4

- where_evidence_is_provided：Section 5.2 Figure 6 and Section 4.3 discussion

### 12. RESPCT适用并推广到学校选择、医疗劳动力、军校匹配等无货币一对多分配。

- claim_cn：RESPCT适用并推广到学校选择、医疗劳动力、军校匹配等无货币一对多分配。

- claim_level：design_knowledge

- supporting_evidence_cn：机制形式性质+现场证据+计算可行性+领域相似性类推。

- support_strength：partial

- where_claim_is_made：Section 6 P4, Section 7 P1-P2

- where_evidence_is_provided：类推而非跨领域数据

### 13. 无配额时RESPCT相对TTC优势比配额时更大。

- claim_cn：无配额时RESPCT相对TTC优势比配额时更大。

- claim_level：boundary

- supporting_evidence_cn：讨论中基于clinching和pointing在无配额时保底计算非常简单。

- support_strength：partial

- where_claim_is_made：Section 6 P3 S4

- where_evidence_is_provided：未提供专门无配额实验，属作者推断

### 14. TTC的某些实例可产生比PCT/ETTC更少的嫉妒，故无法解析证明PCT总比TTC公平。

- claim_cn：TTC的某些实例可产生比PCT/ETTC更少的嫉妒，故无法解析证明PCT总比TTC公平。

- claim_level：mechanism

- supporting_evidence_cn：Section 4.2末段构造性声明。

- support_strength：partial

- where_claim_is_made：Section 4.2 final paragraph

- where_evidence_is_provided：作者声明实例可构造，未在正文详细展开

## ISR定位逻辑

- constitutive_is_problem_cn：本文把'如何设计一个让组织内稀缺资源无需货币即可有效分配的机制'建构为IS设计问题：机制必须在信息约束（不能依赖虚假偏好）、激励约束（策略防护）、技术约束（最低配额和计算复杂度）下运行；因此它既是信息系统规则设计，又是市场设计。

- technology_behavior_or_market_entanglement_cn：技术不是可替换工具：指针指向规则、保底席位向量与clinch时机直接决定学生最终面临多少正当嫉妒，因此算法的微观技术选择构成对公平和效率的行为性结果；反过来，学生与教师的偏好和优先级数据（真实市场现象）又决定算法是否有效。

- role_of_benchmark_or_objective_evidence_cn：benchmark（ESTTC、ESPCT、ESDA）和客观指标（正当嫉妒实例数、被嫉妒学生数、平均排名、运行时间）被用来支持三类主张：机制在某目标上的相对优势、设计构件对公平性的增量贡献、以及替代公平机制的高昂效率代价。这些数字让'低嫉妒'成为可证伪的IS设计结论，而非直觉。

- theory_in_design_cn：理论直接进入设计：效率-公平不可能性决定放宽公平方向；mutual best/σ-mutual best定义具体保底目标；非平凡循环与优先级无关观察决定指针规则；FC与NP完全性决定σ计算工具。理论不只是解释结果，而是构造制品的蓝图。

- technical_vs_is_contribution_balance_cn：论文约一半篇幅是算法设计与定理（第3、4节），另一半是现场数据、效率、可扩展性与政策影响（第2.4、5、6、7节）。它把技术贡献（新算法构件、定理）作为手段，把IS贡献（为无货币组织分配提供可部署、被采纳的机制，并提炼设计知识）作为目的。

- beyond_transient_performance_cn：文章超越了'分数优势'：给出形式定理证明性质不依赖数据；用真实异构偏好数据集检验外部效度；把结果归因到可复用的设计构件（clinching、prioritized pointing、保底最大化），并提供何时有效的边界条件；最后依靠组织采纳（TUM从DA切换到RESPCT）把性能优势转化为制度层面的持续使用。

## 段落级仿写模板

### abstract_steps

1. 首句给IS价值：在无货币条件下用偏好匹配协调稀缺资源，是信息系统设计原则。

2. 次句给出不可兼得定理，说明现有机制选择空间。

3. 第三句说明现状选择要么效率要么无嫉妒，且无嫉妒效率损失巨大。

4. 第四句引入具体匹配场景（课程分配）及其特征。

5. 第五句指出该场景的核心约束（最低配额）并推广到其他领域。

6. 第六句提出机制名称并给出三个性质。

7. 第七句把嫉妒降低归因于两个启发式构件。

8. 第八句声明设计科学方法与现场数据证据。

9. 第九句以政策采纳和持续使用收尾。

### introduction_paragraph_steps

1. 第一段：从经典文献开篇，确立学科传统与不可更改前提（无货币），给出无张力基线。

2. 第二段：从双边匹配转向对象分配，定义公平（正当嫉妒）。

3. 第三段：把问题收窄到具体应用，描述现场细节与约束。

4. 第四段：推广场景相似性，强调特定约束构成差异。

5. 第五段：列出设计目标并给出不可能性结论。

6. 第六段：嵌入IS文献，指出无货币匹配是空白。

7. 第七段：按设计科学框架声明贡献、方法与影响。

8. 第八段：给出全文路线图。

### theory_to_design_steps

1. 先给机制空间二分法（TTC vs DA）。

2. 给出TTC算法及其经典性质与文献地位。

3. 用反例或例子展示效率与公平张力。

4. 提出研究问题：如何让高效机制少嫉妒。

5. 引入关键概念（保底学生、mutual best、σ-mutual best）并证明其不可达或需放宽。

6. 把每个设计构件写成：动机例子→决策规则→形式定理。

7. 从无配额构件扩展到配额市场，并证明性质。

8. 形成完整算法与核心定理，再转向实证评价。

### method_and_study_sequence_steps

1. 先说明为什么用现场数据计算研究而非实验室实验。

2. 描述数据来源、规模、偏好异构性。

3. 解释配额实例生成规则与选择理由。

4. 列出比较机制与评价指标。

5. 按公平性→效率→可扩展性三个维度组织结果。

6. 每个结果子节：报告条件→展示图表→解释趋势与边界→连接下一个问题。

### results_reporting_steps

1. 先报告σ可行性条件，说明实验可执行性。

2. 对每个机制给出所有指标；关键图与表相互配合。

3. 报告趋势，包括反直觉结果（配额上升时ESTTC/ESPCT变好）。

4. 用对照分解贡献：ESPCT vs ESTTC 分离clinching/pointing；RESPCT vs ESPCT 分离扩大保底。

5. 报告效率损失（ESDA约10%学生可帕累托改进）。

6. 报告可扩展性与运行时间，连接部署可行性。

### discussion_and_contribution_steps

1. 把结果放回IS与设计科学文献。

2. 把实证结果归因到机制构件，指明组合效应。

3. 给出使用边界：何时RESPCT最优，何时应选DA。

4. 给出工程可实现性与更广应用。

5. 诚实列限制，并把每个限制与其他设计选择（如策略防护）连接。

6. 以政策采纳和领域未来方向收尾。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：建立无货币匹配的IS价值并给出经典理论起点。

- research_evidence_required_cn：一份经典文献和'无货币'设定；随后可直接引用Gale-Shapley的稳定匹配。

- sentence_pattern_function_cn：用'匹配理论始于...'打开，以'无货币'作为约束标记，随后给出无张力基线。

- transition_condition_cn：当读者理解稳定匹配有效率且无货币是前提后，进入对象分配模型。

### 2. 2

- step：2

- rhetorical_job_cn：把研究问题具体化为对象分配并给出公平定义。

- research_evidence_required_cn：需要'学校/课程优先级作为权利'的文献共识，以及正当嫉妒的正式定义。

- sentence_pattern_function_cn：用'一个密切相关的问题是...'连接，用'对象被消费、优先级是权利'修正模型，用'如果...则...'定义核心概念。

- transition_condition_cn：当公平性成为可计算概念后，引入具体应用。

### 3. 3

- step：3

- rhetorical_job_cn：引入具体应用场景并交代真实数据来源。

- research_evidence_required_cn：具体组织（TUM）的操作信息、课程规模、优先级来源。

- sentence_pattern_function_cn：用'我们的焦点是...'收窄范围，用'在TUM...'提供事实细节，用'课程组织者提交排名'说明数据来源。

- transition_condition_cn：当读者知道课程分配的现实规模与约束后，列出应用相似性。

### 4. 4

- step：4

- rhetorical_job_cn：确立问题普遍性并标注核心约束差异。

- research_evidence_required_cn：至少一个领域列表（学校、军校、医院等）和最低配额特征。

- sentence_pattern_function_cn：用'虽然课程分配具体，但类似'连接，用'关键区别在于...'切出本文的技术难点。

- transition_condition_cn：当最低配额被确立为普遍且未解决时，列出设计目标。

### 5. 5

- step：5

- rhetorical_job_cn：声明设计目标并给出不可兼得定理。

- research_evidence_required_cn：效率、公平、激励相容定义与至少一个不可能性定理或引用。

- sentence_pattern_function_cn：用'被视为关键设计目标'定义判据，用'中心张力在于...'引出不可能性。

- transition_condition_cn：当读者接受必须妥协时，把问题转向IS文献定位。

### 6. 6

- step：6

- rhetorical_job_cn：在IS文献中定位研究并说明无货币匹配的贡献。

- research_evidence_required_cn：若干拍卖与市场设计IS文献，明确说明'几乎都聚焦拍卖'。

- sentence_pattern_function_cn：用'我们的论文与IS文献有多种连接'展开，用'然而几乎所有文献...'制造缺口。

- transition_condition_cn：当IS缺口成立后，声明设计科学贡献。

### 7. 7

- step：7

- rhetorical_job_cn：用设计科学框架声明贡献、方法与影响。

- research_evidence_required_cn：Gregor-Hevner框架、已完成的机制初步结果或至少可行性认知。

- sentence_pattern_function_cn：用'我们是...设计科学贡献'作为中心句，用bullet列出目的、范围、方法、评价。

- transition_condition_cn：当贡献被定位后，给路线图。

### 8. 8

- step：8

- rhetorical_job_cn：理论综述：从经典机制二分到文献空白。

- research_evidence_required_cn：TTC定义与性质、DA性质、ESTTC定义、ETTC局限、真实数据缺乏。

- sentence_pattern_function_cn：用'设计者通常可在两种机制间选择'开始，用'自然问题'结束综述并引入设计目标。

- transition_condition_cn：当阅读者被引导到'如何让高效机制少嫉妒'后，进入形式模型。

### 9. 9

- step：9

- rhetorical_job_cn：建立形式模型、算法与设计目标。

- research_evidence_required_cn：匹配元组定义、TTC和ESTTC算法、三个定义、mutual best与σ-mutual best。

- sentence_pattern_function_cn：用'作为典型例子，我们考虑元组...'定义模型，用'定义...'为每个目标建立断言。

- transition_condition_cn：当σ-mutual best被确立为设计目标后，进入设计章节。

### 10. 10

- step：10

- rhetorical_job_cn：设计章节：按构件顺序给出动机、决策与定理。

- research_evidence_required_cn：每个构件需要动机反例、算法定义、性质定理与证明。

- sentence_pattern_function_cn：对每个构件用'考虑以下例子'说明问题，用'我们介绍...'给算法，用'定理...'声明性质。

- transition_condition_cn：每个构件证明后，用'然而'或'现在考虑'进入下一个约束，最后组装RESPCT。

### 11. 11

- step：11

- rhetorical_job_cn：完整机制定义为核心定理。

- research_evidence_required_cn：完整算法伪代码、例示性运行、核心定理及其证明。

- sentence_pattern_function_cn：用'作为上述考虑的结果'组合构件，用'Algorithm 6'给出机制，用'Theorem 8'给出性质。

- transition_condition_cn：形式保证完成后，进入实证评价。

### 12. 12

- step：12

- rhetorical_job_cn：现场数据计算研究：数据、实验设计、公平性、效率、可扩展性。

- research_evidence_required_cn：真实数据集、基准机制实现、配额实例、指标定义、合成数据与运行时间。

- sentence_pattern_function_cn：用'为评价嫉妒水平，我们进行...'开启，用'我们比较...'列基准，用'图/表显示...'报告结果。

- transition_condition_cn：当三个维度都报告后，进入讨论与贡献。

### 13. 13

- step：13

- rhetorical_job_cn：讨论：把结果升级为贡献、设计知识与边界。

- research_evidence_required_cn：与引言缺口呼应的结果重述、构件归因、使用条件、部署可行性、限制。

- sentence_pattern_function_cn：用'协调是决策支持...'回到学科，用'是结合...的结果'归因，用'如果只关心公平...'设边界，用'限制包括...'列假设。

- transition_condition_cn：当边界和限制清晰后，以政策意义和未来方向收尾。

## 应模仿的高价值动作

1. 用最小反例展示效率与公平不可兼得，再引出可量化的放宽定义（mutual best→σ-mutual best）。

2. 把设计拆成独立构件，每个构件配'动机例子→算法规则→形式定理'三段式。

3. 用ESPCT vs ESTTC的对比把RESPCT的总效果分解到单个构件，证明每个设计决策都有效。

4. 明确用'如果只关心公平，选DA'的边界声明来防止过度宣称，同时保留RESPCT的合理生态位。

5. 用'约10%可帕累托改进'这类量化损失把效率优势锚定到可理解数字。

6. 把NP完全性结果转化为'为什么用MIP+greedy'的工程理由，而不是绕开困难。

7. 用政策改变（TUM从DA切到RESPCT）作为设计科学的最强外部证据，同时把它放在多个位置复述。

## 不要只复制的表面动作

1. 不要把'政策采纳'当作唯一证据，复述过多会显得自我报告；应补充部署后数据或至少说明其不足。

2. 不要只报告3个公平指标而忽略指标间的潜在权衡，尤其是'学生被嫉妒数'与'嫉妒学生数'的变化方向可能不同。

3. 不要把'平均嫉妒减少三倍'当作无条件事实，在配额较高时优势缩小，需要如实说明。

4. 不要把'无配额时RESPCT更好'当作已实验事实，本文只有推断。

5. 不要照搬'随机主列表取10次平均'而不说明方差。

6. 不要把合成数据说成与现场数据等价的证据，应区分模拟与现场。

## 证据薄弱或跳跃的动作

1. 政策采纳声明来自作者自我报告，缺少独立观察或部署后行为数据；摘要和引言多次重复它，使其成为核心证据但证据强度有限。

2. '无配额时RESPCT相对TTC优势更大'是推断而非实验，讨论中却近乎结论。

3. 'PCT在无配额时比ETTC产生更少嫉妒'的初步测试在正文中没有数据表支持，只在文字中提到。

4. 把TUM结果类推到学校选择、医疗劳动力等，没有跨领域数据，仅有机制相似性。

5. '合成数据偏好结构模仿现场数据'的说明较简短，未详述生成分布，模拟证据的可复核性有限。

6. 缺乏对'平均更少嫉妒'是否真正满足学校选择/法律公平诉求的讨论；公平概念被简化为计数。

## 一句话套路

本文从匹配理论中效率与公平不可兼得的不能定理出发，将一个具体分配应用（课程分配）中的最低配额约束转化为保底席位最大化的设计问题，用clinching、prioritized pointing与动态σ三个构件构造RESPCT，再以形式定理、真实现场数据对照（ESTTC/ESPCT/ESDA）和合成可扩展性实验三层证据证明其策略防护、高效与低嫉妒，最终用TUM机制切换证明其制度价值并把局部结果提升为可复用的无货币一对多分配设计知识。

## 分析边界

全文中部分公式、表格和图表在转换时可能有符号错位（如表格内html标记），但章节结构完整；附录证明保留但未完全逐句映射；政策采纳为作者自述，无部署后独立数据；'无配额时RESPCT更好'等推断没有专门实验；合成数据生成细节简短。由于全文以Markdown形式提供，段落边界的判断在个别处（如Example 6后的片段与4.4节衔接）可能不完全精确。
