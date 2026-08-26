# Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach：ISR 句段级微观图谱

- 作者：Tongxin Zhou; Yingfei Wang; Lu (Lucy) Yan; Yong Tan
- 年份：2023
- DOI：10.1287/isre.2022.1191
- 源文件：28562_2023_spoiled-for-choice-personalized-recommendation-for-healthcare-decisions-a-multiarmed-bandit-appr.md
- 置信度：0.82

## 核实后的宏观骨架

全文遵循设计科学（build-and-evaluate）结构：第1节引言从个人健康管理背景、选择过载现实问题出发，提出个性化医疗推荐目标，并列出医疗推荐三大挑战（动态性、多样性、复杂上下文），然后预告DLDE-MAB解决方案；第2节先综述推荐系统与医疗推荐文献，再从行为健康理论提炼动态在线适应原则，以表1将原则、缺口与设计组件对应；第3节构建制品：将推荐问题形式化为带多样性约束的contextual bandit，提出TS算法，并设计用户嵌入（wide-and-deep + eLSTM + attention + 健康结果辅助损失）与干预嵌入（LSTM/FastText + SMART元属性监督）；第4节用真实减肥社区数据做描述性分析，证明偏好确实具有多样性和时间动态性，并完成模型操作化与t-SNE嵌入可视化验证；第5节安排六个实验：整体benchmark比较、消融分析、动态用户专项、推荐多样性分布（JSD）、用户改进率、以健康结果为目标的反事实扩展；第6节讨论贡献、一般化边界与局限，回扣引言缺口，并将结果升华为设计科学与prescriptive analytics贡献。

## 摘要逐句图谱

### 1. Abstract P1 S1

- locator：Abstract P1 S1

- paraphrase_cn：在线医疗平台向用户提供各种干预项目以促进个人健康。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：开篇给出应用场景，把读者带入在线健康管理领域。

- inherits_from_previous_cn：无，是全文第一句。

- changes_argument_state_cn：建立‘平台—干预—用户’的基本世界。

- sets_up_next_cn：为下一句‘选择过多’提供背景。

- failure_if_removed_cn：读者不知道研究对象是谁，后文的问题缺乏语境。

- evidence_pointer：Abstract P1 S1

### 2. Abstract P1 S2

- locator：Abstract P1 S2

- paraphrase_cn：选项很多且个体缺乏评估经验时，很难决定参加哪个干预。

- move_code：PROBLEM_AND_MECHANISM

- statement_status：author_inference

- why_here_cn：引入核心问题‘选择过载’，并给出原因（缺乏经验）。

- inherits_from_previous_cn：承接‘平台提供很多干预选项’。

- changes_argument_state_cn：把中性场景变成有问题、需要解决的场景。

- sets_up_next_cn：引出后果：影响持续参与。

- failure_if_removed_cn：摘要缺少问题，后面目标和方案没有动机。

- evidence_pointer：Abstract P1 S2

### 3. Abstract P1 S3

- locator：Abstract P1 S3

- paraphrase_cn：这可能阻碍个体对在线健康管理的持续参与。

- move_code：PRACTICAL_STAKES

- statement_status：author_inference

- why_here_cn：强调问题的实践后果，说明为什么值得研究。

- inherits_from_previous_cn：把‘难以决定’升级为‘不参与的后果’。

- changes_argument_state_cn：问题从个体不便升级为健康管理失败。

- sets_up_next_cn：为‘研究目标’提供紧迫性。

- failure_if_removed_cn：问题看似只是便利性问题，缺乏IS/健康管理的严肃性。

- evidence_pointer：Abstract P1 S3

### 4. Abstract P1 S4

- locator：Abstract P1 S4

- paraphrase_cn：本研究目标是开发个性化医疗推荐框架，帮助个体发现适合自己的干预。

- move_code：OBJECTIVE

- statement_status：author_inference

- why_here_cn：在问题之后立即宣布研究目标。

- inherits_from_previous_cn：直接回应用户决策困难与持续参与问题。

- changes_argument_state_cn：从‘问题定义’切换到‘目标声明’，为方案做铺垫。

- sets_up_next_cn：预告框架的特征。

- failure_if_removed_cn：摘要没有研究目的，后文方案无法定位。

- evidence_pointer：Abstract P1 S4

### 5. Abstract P1 S5

- locator：Abstract P1 S5

- paraphrase_cn：考虑动态医疗环境中的适应与多样化挑战，提出融合深度表示学习和理论引导多样性促进方案的在线学习框架。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：用一句话概括制品核心特征，展示技术路线。

- inherits_from_previous_cn：把‘目标’落实为‘框架’；‘挑战’二字承接动态环境。

- changes_argument_state_cn：给出解决方案的名称与构成要素。

- sets_up_next_cn：引出评价方式。

- failure_if_removed_cn：读者不知道作者用什么方法解决目标，摘要贡献不清。

- evidence_pointer：Abstract P1 S5

### 6. Abstract P1 S6

- locator：Abstract P1 S6

- paraphrase_cn：我们在真实在线减肥社区的用户干预参与数据上评估该方法。

- move_code：EVALUATION_SETTING

- statement_status：method_decision

- why_here_cn：说明评价数据与场景，显示证据来自真实世界。

- inherits_from_previous_cn：‘评估’承接‘提出框架’。

- changes_argument_state_cn：从‘方案’进入‘实证检验’，预告结果的合法性。

- sets_up_next_cn：引出结果声明。

- failure_if_removed_cn：没有数据来源，读者无法评估结果的外部有效性。

- evidence_pointer：Abstract P1 S6

### 7. Abstract P1 S7

- locator：Abstract P1 S7

- paraphrase_cn：结果强有力支持推荐框架及其各设计组件的有效性。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：报告总体结论，强调‘组件’也有效为后文消融做埋伏。

- inherits_from_previous_cn：承接真实数据评估。

- changes_argument_state_cn：把方案从‘可能有效’推进为‘有证据’。

- sets_up_next_cn：为贡献声明提供依据。

- failure_if_removed_cn：摘要只有方法与数据、没有结果，贡献缺乏支撑。

- evidence_pointer：Abstract P1 S7

### 8. Abstract P1 S8

- locator：Abstract P1 S8

- paraphrase_cn：本研究贡献于prescriptive analytics与商业智能应用的新兴IS研究，并为平台、政策制定者和用户提供启示。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：把研究定位到IS学科议题，并给出利益相关者。

- inherits_from_previous_cn：把‘有效结果’升级为‘学科贡献’。

- changes_argument_state_cn：从技术/实证结论提升为领域贡献。

- sets_up_next_cn：让读者期待正文中的详细贡献。

- failure_if_removed_cn：摘要缺少IS学科归属，文章容易被误读为纯算法论文。

- evidence_pointer：Abstract P1 S8

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：个人健康管理因慢病管理与疾病预防的重要性而受到医疗界越来越多关注。

- move_code：BROAD_CONTEXT

- statement_status：fact

- why_here_cn：以学科大背景开场，确立话题重要性。

- inherits_from_previous_cn：无。

- changes_argument_state_cn：把文章放在健康管理而非电商推荐的语境里。

- sets_up_next_cn：为区分专业照护与日常自我管理做铺垫。

- failure_if_removed_cn：文章开头没有重要性，后面问题缺乏分量。

- evidence_pointer：Introduction P1 S1

### 2. Introduction P1 S2

- order：2

- locator：Introduction P1 S2

- paraphrase_cn：与强调医生专业知识的专业诊疗不同，个人健康管理发生在日常生活中，主要依赖个体自我调节生活方式。

- move_code：CONTEXT_CONTRAST

- statement_status：fact

- why_here_cn：交代个人健康管理的特殊性：自我调节。

- inherits_from_previous_cn：承接‘健康管理重要’，解释它为何重要、有何特点。

- changes_argument_state_cn：为后文‘选择过载导致自我调节失败’埋下机制基础。

- sets_up_next_cn：引出在线平台与干预项目。

- failure_if_removed_cn：读者无法理解为什么用户’自己评估‘如此关键。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P1 S3-S4

- order：3

- locator：Introduction P1 S3-S4

- paraphrase_cn：为支持个人健康管理，许多在线平台（如fatsecret、myfitnesspal等）提供结构化行为治疗项目，如营养计划、运动项目和压力管理。

- move_code：PHENOMENON_SETTING

- statement_status：fact

- why_here_cn：给出具体平台与干预例子，让场景具体可感。

- inherits_from_previous_cn：‘为支持个人健康管理’直接承接上一句。

- changes_argument_state_cn：确立研究对象：在线医疗干预。

- sets_up_next_cn：为下一句‘这些干预已被广泛使用’提供例子。

- failure_if_removed_cn：研究对象不明确，选择过载缺乏载体。

- evidence_pointer：Introduction P1 S3-S4

### 4. Introduction P1 S5

- order：4

- locator：Introduction P1 S5

- paraphrase_cn：已有文献记录在线医疗干预在糖尿病、肥胖、精神疾病、酗酒、戒烟等领域的应用。

- move_code：PRIOR_LITERATURE

- statement_status：prior_literature

- why_here_cn：用文献证明干预在多个健康领域被使用，问题普遍。

- inherits_from_previous_cn：承接‘在线干预’概念，给出实证使用证据。

- changes_argument_state_cn：把例子上升为被广泛研究的现象。

- sets_up_next_cn：为下一句‘相对线下咨询的优势’做准备。

- failure_if_removed_cn：在线干预看似只是个别平台现象，缺乏普遍意义。

- evidence_pointer：Introduction P1 S5

### 5. Introduction P1 S6

- order：5

- locator：Introduction P1 S6

- paraphrase_cn：与线下咨询相比，在线干预更可及、更具成本效益，可能促进长期参与。

- move_code：OPPORTUNITY

- statement_status：prior_literature

- why_here_cn：强调在线干预的正面潜力，为后面‘但选择过载会破坏它’做张力铺垫。

- inherits_from_previous_cn：承接干预领域证据，转述其优点。

- changes_argument_state_cn：从‘现象存在’推进为‘有重要潜力但仍有问题’。

- sets_up_next_cn：引出第二段的转折‘尽管有潜力，选择过载会干扰’。

- failure_if_removed_cn：后文说‘尽管有潜力’缺少对照，转折失效。

- evidence_pointer：Introduction P1 S6

### 6. Introduction P2 S1

- order：6

- locator：Introduction P2 S1

- paraphrase_cn：尽管有潜力，选择过载问题可能干扰在线医疗干预的交付。

- move_code：TURN_TO_PROBLEM

- statement_status：author_inference

- why_here_cn：从正面的潜力转向负面问题，是引言的第一次转折。

- inherits_from_previous_cn：‘尽管有潜力’直接回指第一段结尾。

- changes_argument_state_cn：把故事从机会转向障碍。

- sets_up_next_cn：展开选择过载的具体表现。

- failure_if_removed_cn：引言失去从机会到问题的转折，问题出现得很突兀。

- evidence_pointer：Introduction P2 S1

### 7. Introduction P2 S2

- order：7

- locator：Introduction P2 S2

- paraphrase_cn：平台为满足异质需求提供大量干预选项。

- move_code：PROBLEM_CAUSE

- statement_status：fact

- why_here_cn：说明选择过载的来源：大量选项。

- inherits_from_previous_cn：解释为什么会出现选择过载。

- changes_argument_state_cn：把抽象的‘选择过载’落到平台供给端。

- sets_up_next_cn：为下一句‘选项太多导致决策下降’做铺垫。

- failure_if_removed_cn：读者不知道选项为什么多，无法理解过载来源。

- evidence_pointer：Introduction P2 S2

### 8. Introduction P2 S3

- order：8

- locator：Introduction P2 S3

- paraphrase_cn：当选项太多时，个体决策表现会因找不到真正相关信息而显著下降。

- move_code：PROBLEM_MECHANISM

- statement_status：prior_literature

- why_here_cn：用文献说明选择过载的机制与后果。

- inherits_from_previous_cn：从‘大量选项’推出‘决策失败’。

- changes_argument_state_cn：把平台端特征转化为用户端后果。

- sets_up_next_cn：为下一句‘用户缺乏经验更难评估’做铺垫。

- failure_if_removed_cn：问题只停留在数量多，没有说明为什么数量多有害。

- evidence_pointer：Introduction P2 S3

### 9. Introduction P2 S4

- order：9

- locator：Introduction P2 S4

- paraphrase_cn：大多数用户缺乏健康管理经验，难以评估每个干预选项。

- move_code：HEALTH_SPECIFIC_MECHANISM

- statement_status：author_inference

- why_here_cn：说明选择过载在医疗场景的特殊性：缺乏专业知识。

- inherits_from_previous_cn：承接‘难以决策’，给出医疗领域的特殊原因。

- changes_argument_state_cn：从通用选择过载转向医疗特有障碍。

- sets_up_next_cn：引出‘阻碍参与’的后果。

- failure_if_removed_cn：医疗场景的推荐问题与电商无关，特殊性消失。

- evidence_pointer：Introduction P2 S4

### 10. Introduction P2 S5

- order：10

- locator：Introduction P2 S5

- paraphrase_cn：这阻碍用户对医疗干预的积极参与。

- move_code：PROBLEM_CONSEQUENCE

- statement_status：author_inference

- why_here_cn：闭合从原因到后果的链条。

- inherits_from_previous_cn：从‘难以评估’推出‘不积极参与’。

- changes_argument_state_cn：问题从决策层面进入行为/参与层面。

- sets_up_next_cn：为下一句‘虽然选择过载不新鲜，但医疗领域有独特问题’做铺垫。

- failure_if_removed_cn：不参与的结果缺失，研究动机减弱。

- evidence_pointer：Introduction P2 S5

### 11. Introduction P2 S6

- order：11

- locator：Introduction P2 S6

- paraphrase_cn：虽然选择过载对在线环境不新鲜，但它在医疗领域造成独特问题。

- move_code：DIFFERENTIATION

- statement_status：author_inference

- why_here_cn：防止读者反驳‘这不就是电商推荐问题吗’。

- inherits_from_previous_cn：以‘虽然’承接通用选择过载文献。

- changes_argument_state_cn：把问题限定为医疗特异问题。

- sets_up_next_cn：为下一句‘不参与危害健康表现’做铺垫。

- failure_if_removed_cn：文章的IS贡献可能被误认为只是重复已有推荐研究。

- evidence_pointer：Introduction P2 S6

### 12. Introduction P2 S7

- order：12

- locator：Introduction P2 S7

- paraphrase_cn：研究者认为困难的决策会导致个体不参加任何干预，从而损害健康管理表现。

- move_code：CONSEQUENCE_AGGRAVATION

- statement_status：prior_literature

- why_here_cn：给出最严重后果：不参与任何干预并损害健康结果。

- inherits_from_previous_cn：承接‘医疗领域独特’，用文献落实后果。

- changes_argument_state_cn：把问题从‘参与低’升级为‘健康危害’。

- sets_up_next_cn：引出‘因此需要推荐服务’。

- failure_if_removed_cn：健康风险缺失，推荐系统显得只是锦上添花。

- evidence_pointer：Introduction P2 S7

### 13. Introduction P2 S8

- order：13

- locator：Introduction P2 S8

- paraphrase_cn：因此存在对服务以个体医疗需求更好地推广在线干预的迫切需求。

- move_code：DEMAND

- statement_status：author_inference

- why_here_cn：从问题推出需求，首次提出‘推荐服务’的必要性。

- inherits_from_previous_cn：从‘不参与损害健康’推出服务需求。

- changes_argument_state_cn：问题诊断完成，转向解决方案。

- sets_up_next_cn：为第三段研究目标做铺垫。

- failure_if_removed_cn：引言只有问题没有需求，研究目标失去落脚点。

- evidence_pointer：Introduction P2 S8

### 14. Introduction P3 S1

- order：14

- locator：Introduction P3 S1

- paraphrase_cn：本研究目标是开发个性化医疗推荐系统。

- move_code：OBJECTIVE

- statement_status：author_inference

- why_here_cn：正式宣布研究目标。

- inherits_from_previous_cn：直接回应上一段的‘迫切需求’。

- changes_argument_state_cn：从问题/需求进入方案目标。

- sets_up_next_cn：细化目标内容。

- failure_if_removed_cn：全文没有明确目标，研究问题不成立。

- evidence_pointer：Introduction P3 S1

### 15. Introduction P3 S2-S3

- order：15

- locator：Introduction P3 S2-S3

- paraphrase_cn：目标是为每位用户在每个时间提供一小组干预选项，帮助用户快速发现匹配干预并提高参与率。

- move_code：OBJECTIVE_SPECIFICATION

- statement_status：author_inference

- why_here_cn：把目标操作化为‘每期K个干预 + 提高参与率’。

- inherits_from_previous_cn：承接‘个性化推荐系统’，具体化输出。

- changes_argument_state_cn：为第3节问题形式化（top-K推荐）做预告。

- sets_up_next_cn：引出‘但医疗推荐有三大挑战’。

- failure_if_removed_cn：读者不知道系统具体输出什么，后续形式化无锚点。

- evidence_pointer：Introduction P3 S2-S3

### 16. Introduction P3 S4

- order：16

- locator：Introduction P3 S4

- paraphrase_cn：尽管推荐系统在电商中被广泛研究，但医疗场景应用充满挑战，原因如下。

- move_code：TRANSITION_TO_GAP

- statement_status：author_inference

- why_here_cn：把文献（电商推荐）与本文（医疗推荐）的落差摆出来，作为引言核心缺口。

- inherits_from_previous_cn：连接‘推荐系统’研究背景。

- changes_argument_state_cn：开启三大挑战的列举。

- sets_up_next_cn：为第四段三大挑战做总指示。

- failure_if_removed_cn：本文与推荐文献的联系与区别消失，研究为何难不成立。

- evidence_pointer：Introduction P3 S4

### 17. Introduction P4 S1

- order：17

- locator：Introduction P4 S1

- paraphrase_cn：第一，健康管理的演化性使偏好表现出强时间动态性，需要服务实时适应。

- move_code：CHALLENGE_1_DYNAMICS

- statement_status：author_inference

- why_here_cn：指出医疗推荐第一大挑战：动态偏好。

- inherits_from_previous_cn：从‘健康管理演化性’承接健康理论。

- changes_argument_state_cn：为选择在线学习/bandit预设理由。

- sets_up_next_cn：引出第二、第三挑战并铺垫对应解法。

- failure_if_removed_cn：在线学习动机消失，bandit框架没有必要性。

- evidence_pointer：Introduction P4 S1

### 18. Introduction P4 S2

- order：18

- locator：Introduction P4 S2

- paraphrase_cn：第二，个体医疗需求需从多个方面满足；健康管理通常涉及多个结局与行为维度。

- move_code：CHALLENGE_2_DIVERSITY

- statement_status：author_inference

- why_here_cn：提出第二大挑战：多维度需求。

- inherits_from_previous_cn：承接‘多方面健康管理’。

- changes_argument_state_cn：为多样性约束提供问题基础。

- sets_up_next_cn：为social cognitive theory指导的多样性设计铺垫。

- failure_if_removed_cn：多样性约束显得多余，消融实验也失去动机。

- evidence_pointer：Introduction P4 S2

### 19. Introduction P4 S3

- order：19

- locator：Introduction P4 S3

- paraphrase_cn：理想推荐需覆盖重要健康管理方面，以提供全面支持。

- move_code：CHALLENGE_2_IMPLICATION

- statement_status：author_inference

- why_here_cn：把多维度需求转化为设计条件：推荐需覆盖多个方面。

- inherits_from_previous_cn：直接承接多维度需求。

- changes_argument_state_cn：为结构多样性而非随机多样性埋下伏笔。

- sets_up_next_cn：为下一句‘第三挑战’做过渡。

- failure_if_removed_cn：读者不知道多样性对推荐意味着什么。

- evidence_pointer：Introduction P4 S3

### 20. Introduction P4 S4-S5

- order：20

- locator：Introduction P4 S4-S5

- paraphrase_cn：第三，描述健康管理上下文很困难，因为健康与行为轨迹中存在复杂序列相关和事件不规则性。

- move_code：CHALLENGE_3_CONTEXT

- statement_status：author_inference

- why_here_cn：提出第三大挑战：复杂上下文表示。

- inherits_from_previous_cn：承接健康管理背景，但聚焦数据形式。

- changes_argument_state_cn：为深度表示学习组件提供问题依据。

- sets_up_next_cn：为eLSTM、wide-and-deep等设计做铺垫。

- failure_if_removed_cn：深度学习建模失去必要性，本文与一般bandit无异。

- evidence_pointer：Introduction P4 S4-S5

### 21. Introduction P4 S6-S7

- order：21

- locator：Introduction P4 S6-S7

- paraphrase_cn：个体健康管理活动受健康经历、健康史和社会情境影响；在线数据包含多种格式与内容，需要联合处理以全面理解用户。

- move_code：CHALLENGE_3_ELABORATION

- statement_status：prior_literature

- why_here_cn：用文献支持上下文复杂性，并指出数据多样格式。

- inherits_from_previous_cn：承接‘复杂轨迹’，给出具体来源。

- changes_argument_state_cn：确定用户表示必须融合静态与动态、多序列与多格式。

- sets_up_next_cn：为下一句‘这些挑战仍是主要障碍’收束。

- failure_if_removed_cn：复杂上下文变成空话，设计细节失去依据。

- evidence_pointer：Introduction P4 S6-S7

### 22. Introduction P4 S8

- order：22

- locator：Introduction P4 S8

- paraphrase_cn：迄今为止，这些挑战仍是医疗推荐任务的主要障碍。

- move_code：GAP_CLOSURE

- statement_status：author_inference

- why_here_cn：总结三大挑战为研究缺口。

- inherits_from_previous_cn：概括前面三点。

- changes_argument_state_cn：明确本文要解决的是什么障碍。

- sets_up_next_cn：为第五段解决方案做‘我们解决这些挑战’。

- failure_if_removed_cn：三大挑战只是罗列，没有凝固成可攻击的缺口。

- evidence_pointer：Introduction P4 S8

### 23. Introduction P5 S1

- order：23

- locator：Introduction P5 S1

- paraphrase_cn：我们通过提出深度学习与多样性增强bandit框架来解决这些挑战。

- move_code：SOLUTION_OVERVIEW

- statement_status：author_inference

- why_here_cn：从缺口直接跳到解决方案名称。

- inherits_from_previous_cn：承接‘主要障碍’。

- changes_argument_state_cn：引言从问题诊断进入方案预告。

- sets_up_next_cn：解释bandit为什么适合动态环境。

- failure_if_removed_cn：问题提出后没有解法承诺，读者不知道本文做什么。

- evidence_pointer：Introduction P5 S1

### 24. Introduction P5 S2-S3

- order：24

- locator：Introduction P5 S2-S3

- paraphrase_cn：bandit能适应实时数据流、最大化累计收益，适合动态医疗推荐并促进长期参与。

- move_code：METHOD_RATIONALE

- statement_status：prior_literature

- why_here_cn：为bandit选择提供机制理由：实时适应。

- inherits_from_previous_cn：解释‘bandit框架’为何能应对动态挑战。

- changes_argument_state_cn：将动态挑战与bandit能力对齐。

- sets_up_next_cn：引出两个附加设计组件以补齐其余挑战。

- failure_if_removed_cn：选bandit显得随意，读者不知道为何不是其他算法。

- evidence_pointer：Introduction P5 S2-S3

### 25. Introduction P5 S4

- order：25

- locator：Introduction P5 S4

- paraphrase_cn：第一，用理论驱动多样性方案沿主要健康维度结构化分散干预。

- move_code：DESIGN_FEATURE_1

- statement_status：design_decision

- why_here_cn：对应第二大挑战（多样性），点出‘理论驱动’与‘结构化’。

- inherits_from_previous_cn：承接‘还需解决多样性和上下文表示’。

- changes_argument_state_cn：把方案从通用bandit升级为带理论多AC的bandit。

- sets_up_next_cn：引出第二设计组件。

- failure_if_removed_cn：多样性消隐实验的靶子缺失，理论贡献落空。

- evidence_pointer：Introduction P5 S4

### 26. Introduction P5 S5

- order：26

- locator：Introduction P5 S5

- paraphrase_cn：第二，用深度学习捕获静态属性和健康史、行为路径中的复杂序列模式。

- move_code：DESIGN_FEATURE_2

- statement_status：design_decision

- why_here_cn：对应第三大挑战（上下文），点出深度表示学习。

- inherits_from_previous_cn：承接‘除了多样性，还需表示学习’。

- changes_argument_state_cn：把方案补齐到‘bandit + 多样性 + 深度表示’。

- sets_up_next_cn：为第3节用户/干预嵌入章节做预告。

- failure_if_removed_cn：第三挑战没有对应解法，后文深度网络成为冗余。

- evidence_pointer：Introduction P5 S5

### 27. Introduction P5 S6

- order：27

- locator：Introduction P5 S6

- paraphrase_cn：我们提出基于Thompson sampling的算法，把推荐作为随机优化任务求解。

- move_code：ALGORITHM_INTRO

- statement_status：design_decision

- why_here_cn：点名求解算法（TS），预告第3.1.2的Algorithm 1。

- inherits_from_previous_cn：承接整体框架，把抽象方案落实为算法。

- changes_argument_state_cn：从‘框架’推进到‘可计算制品’。

- sets_up_next_cn：为后文评价做铺垫。

- failure_if_removed_cn：读者不知道框架如何求解，贡献不完整。

- evidence_pointer：Introduction P5 S6

### 28. Introduction P6 S1

- order：28

- locator：Introduction P6 S1

- paraphrase_cn：我们通过真实数据集上的一系列实验评估推荐框架。

- move_code：EVALUATION_PREVIEW

- statement_status：method_decision

- why_here_cn：预告评价方式，暗示证据基础是真实数据。

- inherits_from_previous_cn：承接已构建的框架。

- changes_argument_state_cn：从构建阶段转向评估承诺。

- sets_up_next_cn：预告四个层级的结果。

- failure_if_removed_cn：引言没有评价承诺，正文实证显得突兀。

- evidence_pointer：Introduction P6 S1

### 29. Introduction P6 S2

- order：29

- locator：Introduction P6 S2

- paraphrase_cn：结果证明方法优于广泛基准，并证明每个设计组件有效。

- move_code：RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：给出总体结论，强调组件有效。

- inherits_from_previous_cn：承接实验评估。

- changes_argument_state_cn：把‘我们将评估’变成‘我们已证明’。

- sets_up_next_cn：为‘更细粒度分析’做铺垫。

- failure_if_removed_cn：读者不知道结果是什么，贡献声明没有根基。

- evidence_pointer：Introduction P6 S2

### 30. Introduction P6 S3

- order：30

- locator：Introduction P6 S3

- paraphrase_cn：通过更细粒度分析，我们展示框架能适应偏好动态与多样性，并在更大用户群中促进参与。

- move_code：DEEPER_RESULT_PREVIEW

- statement_status：empirical_result

- why_here_cn：预告机制级证据：动态适应、多样性、用户改进率。

- inherits_from_previous_cn：‘更细粒度’承接前一句结果。

- changes_argument_state_cn：把贡献从‘分数更高’升级为‘机制上有效’。

- sets_up_next_cn：为第五段贡献声明做铺垫。

- failure_if_removed_cn：文章看起来只是又一个更好算法，IS贡献弱化。

- evidence_pointer：Introduction P6 S3

### 31. Introduction P7 S1

- order：31

- locator：Introduction P7 S1

- paraphrase_cn：本研究对文献与实践做出多项贡献。

- move_code：CONTRIBUTION_HEADER

- statement_status：contribution_claim

- why_here_cn：开启贡献声明。

- inherits_from_previous_cn：总结前文成果。

- changes_argument_state_cn：从结果转向学科贡献。

- sets_up_next_cn：引出主要贡献的具体内容。

- failure_if_removed_cn：引言没有贡献句，收尾不完整。

- evidence_pointer：Introduction P7 S1

### 32. Introduction P7 S2-S3

- order：32

- locator：Introduction P7 S2-S3

- paraphrase_cn：主要贡献是提出医疗推荐框架，展示prescriptive analytics如何通过设计科学制品整合到个体健康管理决策支持中。

- move_code：CONTRIBUTION_MAIN

- statement_status：contribution_claim

- why_here_cn：把贡献定位为设计科学与prescriptive analytics，而不只是算法。

- inherits_from_previous_cn：承接‘多项贡献’，给出第一项。

- changes_argument_state_cn：确立文章的IS学科归属。

- sets_up_next_cn：列举框架的三个新方面。

- failure_if_removed_cn：文章与IS的关联断裂，可能被归为纯ML论文。

- evidence_pointer：Introduction P7 S2-S3

### 33. Introduction P7 S4

- order：33

- locator：Introduction P7 S4

- paraphrase_cn：框架的新颖之处包括深度表示学习、领域知识驱动的多样性促进、定制在线学习方案。

- move_code：CONTRIBUTION_ENUMERATION

- statement_status：contribution_claim

- why_here_cn：把贡献分解为三个可识别的设计组件。

- inherits_from_previous_cn：承接‘框架’，细化新在哪里。

- changes_argument_state_cn：为消融实验提供贡献层面的预告。

- sets_up_next_cn：引出实践贡献。

- failure_if_removed_cn：贡献太笼统，读者不知道具体创新点。

- evidence_pointer：Introduction P7 S4

### 34. Introduction P7 S5

- order：34

- locator：Introduction P7 S5

- paraphrase_cn：从实践角度，框架解决医疗推荐现实挑战，惠及用户、平台和政策制定者。

- move_code：CONTRIBUTION_PRACTICE

- statement_status：contribution_claim

- why_here_cn：给三类利益相关者，扩展贡献面。

- inherits_from_previous_cn：承接三个设计组件。

- changes_argument_state_cn：贡献从技术/学科扩展至实践。

- sets_up_next_cn：为第6节详细贡献讨论留接口。

- failure_if_removed_cn：实践意义缺失，文章的应用导向不完整。

- evidence_pointer：Introduction P7 S5

### 35. Introduction P7 S6

- order：35

- locator：Introduction P7 S6

- paraphrase_cn：我们将在文末详细讨论贡献。

- move_code：SIGNPOST

- statement_status：author_inference

- why_here_cn：告诉读者详细讨论在末尾，引言不必展开。

- inherits_from_previous_cn：承接所有贡献预告。

- changes_argument_state_cn：给引言画上句号，并指向第6节。

- sets_up_next_cn：为第2节文献综述做过渡。

- failure_if_removed_cn：读者可能期待引言即完整贡献，缺少路径指引。

- evidence_pointer：Introduction P7 S6

## 引言逐段图谱

### 1. Introduction P1

- locator：Introduction P1

- opening_move_cn：以‘个人健康管理重要’开篇，把话题锚定在健康管理而非算法。

- development_move_cn：区分专业照护与日常自我调节，给出在线平台与干预实例，用文献证明在线干预已在多个慢病领域应用。

- pivot_move_cn：最后一句从‘在线干预有优势’转向‘但其交付可能被选择过载干扰’。

- closing_move_cn：制造‘尽管有潜力，问题存在’的张力，为第二段问题展开做铺垫。

- paragraph_job_cn：建立研究语境与在线医疗干预的重要性，同时为选择过载埋下伏笔。

### 2. Introduction P2

- locator：Introduction P2

- opening_move_cn：直接指出问题：‘选择过载可能干扰在线干预交付’。

- development_move_cn：从平台提供大量选项→决策困难→用户缺乏经验→不参与→健康表现受损，层层递进。

- pivot_move_cn：‘虽然选择过载对在线不新鲜，但医疗领域有独特问题’。

- closing_move_cn：以‘存在迫切需求’收束，把问题转化为服务需求。

- paragraph_job_cn：把背景转成可研究的问题，并论证医疗场景中推荐服务的必要性。

### 3. Introduction P3

- locator：Introduction P3

- opening_move_cn：宣布研究目标：开发个性化医疗推荐系统。

- development_move_cn：具体化目标（为每位用户每期提供子集、提升参与率）。

- pivot_move_cn：‘虽然推荐在电商中被广泛研究，但医疗场景有挑战’。

- closing_move_cn：用‘原因如下’引出下一段三大挑战。

- paragraph_job_cn：把现实需求转成明确研究目标，并预告医疗推荐的特殊性。

### 4. Introduction P4

- locator：Introduction P4

- opening_move_cn：直接列三大挑战：动态性、多维度、复杂上下文。

- development_move_cn：每一点都给出健康管理依据与推荐设计含义。

- pivot_move_cn：末句把三大挑战总结为‘主要障碍’（研究缺口）。

- closing_move_cn：制造缺口，为第五段‘我们解决这些挑战’做铺垫。

- paragraph_job_cn：确立医疗推荐任务的三大技术障碍，形成全文Gap。

### 5. Introduction P5

- locator：Introduction P5

- opening_move_cn：‘我们用bandit框架解决这些挑战’直接对接缺口。

- development_move_cn：解释bandit为何适合动态环境，再引入两个设计组件（多样性、深度表示），最后提出TS算法。

- pivot_move_cn：从‘框架’到‘TS算法’逐步具体化。

- closing_move_cn：以算法名称收束，为第3节做预告。

- paragraph_job_cn：给出解决方案的总体结构与核心设计选择。

### 6. Introduction P6

- locator：Introduction P6

- opening_move_cn：‘我们通过真实数据上的实验评估框架’。

- development_move_cn：预告三层结果：优于基准、组件有效、机制级分析（动态/多样性/用户群）。

- pivot_move_cn：从整体结果转向‘更细粒度分析’。

- closing_move_cn：以‘促进更大用户群参与’收束，为贡献声明铺垫。

- paragraph_job_cn：预览评价设计与结论层级，让读者预期实证部分的证明顺序。

### 7. Introduction P7

- locator：Introduction P7

- opening_move_cn：‘本研究做出多项贡献’。

- development_move_cn：先给设计科学/prescriptive analytics定位，再拆三个技术新点，再给实践贡献。

- pivot_move_cn：从文献贡献转向实践贡献。

- closing_move_cn：以‘文末详细讨论’收束，指向第6节。

- paragraph_job_cn：在引言尾部完成贡献总声明，锚定IS学科身份。

## 理论到设计逐句图谱

### 1. Theory section P4 final sentence

- locator：Theory section P4 final sentence

- paraphrase_cn：行为健康研究中的动态性和多样性证据促使作者在推荐设计中纳入动态和多样性考虑。

- move_code：LITERATURE_TO_DESIGN_PRINCIPLE

- statement_status：author_inference

- why_here_cn：把文献综述的结论转成设计方向，是理论到设计的第一座桥。

- inherits_from_previous_cn：承接前面Johnson、King、Cutler等关于动态与多方面的综述。

- changes_argument_state_cn：从‘文献说了什么’推进到‘我们要据此设计’。

- sets_up_next_cn：引出2.1相关工作和2.2设计原则。

- failure_if_removed_cn：文献综述变成纯背景，设计原则失去来源。

- evidence_pointer：Section 2 intro final sentence

### 2. Section 2.1.1 P2 S1-S2

- locator：Section 2.1.1 P2 S1-S2

- paraphrase_cn：batch推荐的前提是历史选择概率在推荐时不变，这无法捕捉动态偏好变化。

- move_code：LIMITATION_OF_BATCH

- statement_status：author_inference

- why_here_cn：指出主流batch推荐的第一缺陷，为引入在线学习铺路。

- inherits_from_previous_cn：承接推荐文献分类。

- changes_argument_state_cn：确立‘batch方法不足’这一技术缺口。

- sets_up_next_cn：引出第二缺陷‘缺乏探索’。

- failure_if_removed_cn：在线学习动机不成立。

- evidence_pointer：Section 2.1.1 P2

### 3. Section 2.1.1 P2 S3-S6

- locator：Section 2.1.1 P2 S3-S6

- paraphrase_cn：batch模型大多最大化短期奖励，忽略偏好不确定性；即使频繁重训，也会因数据来自同一推荐策略而固化历史模式、无法探索更好的选项。

- move_code：LIMITATION_OF_BATCH_ELABORATED

- statement_status：author_inference

- why_here_cn：解释batch为何不仅静态，还自我强化，把缺陷从‘动态不足’推向‘探索不足’。

- inherits_from_previous_cn：承接‘历史概率不变’假设。

- changes_argument_state_cn：让batch方法几乎不可能解决医疗推荐动态问题。

- sets_up_next_cn：为MAB的exploration/exploitation平衡做铺垫。

- failure_if_removed_cn：后文bandit优势缺乏对比支点。

- evidence_pointer：Section 2.1.1 P2 S3-S6

### 4. Section 2.1.1 P3 S1

- locator：Section 2.1.1 P3 S1

- paraphrase_cn：这些问题可以更好地由多臂bandit算法解决，它通过顺序决策平衡利用与探索。

- move_code：THEORY_INTRO_MAB

- statement_status：prior_literature

- why_here_cn：引入MAB作为核心技术参照。

- inherits_from_previous_cn：承接batch的两个缺陷。

- changes_argument_state_cn：把问题-解法配对：动态→MAB。

- sets_up_next_cn：解释exploitation/exploration如何服务长期参与。

- failure_if_removed_cn：核心框架没有理论入口。

- evidence_pointer：Section 2.1.1 P3 S1

### 5. Section 2.1.2 P2 S1-S4

- locator：Section 2.1.2 P2 S1-S4

- paraphrase_cn：已有医疗推荐研究较少考虑用户健康管理上下文，也没有纳入个体健康行为序列；多样性主要靠增加随机性，不保证覆盖主要健康管理需求。

- move_code：GAP_IN_HEALTHCARE_RECOMMENDATION

- statement_status：prior_literature

- why_here_cn：在医疗推荐子文献中指出两个具体缺口：上下文与多样性。

- inherits_from_previous_cn：承接2.1.2对医疗推荐研究的概述。

- changes_argument_state_cn：确立本文要填补的两个特异性缺口。

- sets_up_next_cn：为2.2设计原则中的上下文表示与多样性原则提供依据。

- failure_if_removed_cn：本文与Rabbi、Tomkins等工作的区分度消失。

- evidence_pointer：Section 2.1.2 P2

### 6. Section 2.2 P1 S1

- locator：Section 2.2 P1 S1

- paraphrase_cn：我们提出动态在线适应原则以指导设计，包括适应不确定性、通过改进上下文表示适应观测到的动态、适应多样化健康需求。

- move_code：DESIGN_PRINCIPLE_STATEMENT

- statement_status：theory_claim

- why_here_cn：从文献缺口提升为本文的设计原则，是全文理论核心句。

- inherits_from_previous_cn：把前面一切缺口汇总为三条原则。

- changes_argument_state_cn：从‘文献批评’进入‘我们的设计要求’。

- sets_up_next_cn：组织2.2.1-2.2.4各小节。

- failure_if_removed_cn：理论到设计的桥消失，后文组件没有设计合法性。

- evidence_pointer：Section 2.2 P1 S1

### 7. Section 2.2.2 P1 S2-S4

- locator：Section 2.2.2 P1 S2-S4

- paraphrase_cn：推荐过程中数据是顺序获得的，服务提供者面临用户偏好不确定性，需采用在线学习，既要利用历史数据也要探索未知偏好。

- move_code：DESIGN_PRINCIPLE_UNCERTAINTY

- statement_status：theory_claim

- why_here_cn：细化‘适应不确定性’原则，为bandit选择提供理论依据。

- inherits_from_previous_cn：承接‘动态在线适应原则’。

- changes_argument_state_cn：把不确定性原则翻译为exploitation/exploration需求。

- sets_up_next_cn：为第3节TS算法和约束优化做铺垫。

- failure_if_removed_cn：TS算法看起来只是技术偏好，而非理论要求。

- evidence_pointer：Section 2.2.2 P1

### 8. Section 2.2.3.1 P1 S1

- locator：Section 2.2.3.1 P1 S1

- paraphrase_cn：健康管理上下文包含静态特征（如人口统计）和时间动态特征（如健康轨迹、行为路径），整合二者对准确预测很重要但也困难。

- move_code：DESIGN_PRINCIPLE_STATIC_PLUS_DYNAMIC

- statement_status：theory_claim

- why_here_cn：把‘适应观测动态’具体化为‘静态+动态特征融合’。

- inherits_from_previous_cn：承接2.2.3开头‘上下文表示原则’。

- changes_argument_state_cn：为wide-and-deep用户嵌入设计提供依据。

- sets_up_next_cn：为2.2.3.2多序列动态做铺垫。

- failure_if_removed_cn：用户嵌入为何要有wide和deep两条分支缺乏解释。

- evidence_pointer：Section 2.2.3.1 P1

### 9. Section 2.2.3.2 P1 S2-S5

- locator：Section 2.2.3.2 P1 S2-S5

- paraphrase_cn：健康管理是多序列自影响过程：自我监测、治疗依从和社交联系各自构成序列，序列间存在相关，事件间隔也不规则，因此需要联合建模。

- move_code：DESIGN_PRINCIPLE_MULTISEQUENCE

- statement_status：theory_claim

- why_here_cn：提出多序列联合处理要求，直接对应eLSTM设计。

- inherits_from_previous_cn：承接静态+动态原则，聚焦动态序列部分。

- changes_argument_state_cn：把‘健康上下文’细化为多序列且不规则的信号集合。

- sets_up_next_cn：为eLSTM、attention、事件间隔建模做铺垫。

- failure_if_removed_cn：eLSTM与attention机制变成无理论依据的堆砌。

- evidence_pointer：Section 2.2.3.2 P1

### 10. Section 2.2.3.3 P1 S2-S3

- locator：Section 2.2.3.3 P1 S2-S3

- paraphrase_cn：行为动机理论认为个体用健康结果作为反馈强化健康行为，因此干预偏好不只由口味驱动，还由目标健康结果驱动。

- move_code：DESIGN_PRINCIPLE_HEALTH_OUTCOME

- statement_status：theory_claim

- why_here_cn：把健康结果纳入用户表示的理论依据。

- inherits_from_previous_cn：承接2.2.3开头‘改进上下文表示’。

- changes_argument_state_cn：为辅助损失头提供机制理由。

- sets_up_next_cn：为实验6中以体重下降为奖励做铺垫。

- failure_if_removed_cn：辅助损失与健康结果实验缺乏理论根基。

- evidence_pointer：Section 2.2.3.3 P1

### 11. Section 2.2.3.3 P2 S3-S4

- locator：Section 2.2.3.3 P2 S3-S4

- paraphrase_cn：目标设定理论认为SMART五维度（具体、可测、可达、相关、时限）是评估干预目标质量的金标准，因此用它指导干预表示学习。

- move_code：DESIGN_PRINCIPLE_SMART

- statement_status：theory_claim

- why_here_cn：把干预表示学习锚定到SMART领域知识。

- inherits_from_previous_cn：承接‘干预表示更复杂，需基于健康调节理论’。

- changes_argument_state_cn：为第3.2.2干预嵌入输出SMART属性提供理论依据。

- sets_up_next_cn：为第4.2表3的标注特征列表做铺垫。

- failure_if_removed_cn：干预嵌入输出的11个属性显得随意。

- evidence_pointer：Section 2.2.3.3 P2

### 12. Section 2.2.4 P1 S1-S4

- locator：Section 2.2.4 P1 S1-S4

- paraphrase_cn：社会认知理论自我调节概念认为个体既要管理健康结果，又要管理行为常规，因此推荐应沿这两类维度多样化。

- move_code：DESIGN_PRINCIPLE_DIVERSITY

- statement_status：theory_claim

- why_here_cn：给出多样性约束的理论来源，是理论到设计最关键的一步。

- inherits_from_previous_cn：承接三条原则中的‘适应多样需求’。

- changes_argument_state_cn：把‘多样性’从随机性升级为结果/行为双维结构。

- sets_up_next_cn：为第3.1.2式(3)约束和消隐实验做铺垫。

- failure_if_removed_cn：多样性约束没有理论支撑，与普通随机探索无异。

- evidence_pointer：Section 2.2.4 P1

### 13. Section 2.2.5 Table 1附近

- locator：Section 2.2.5 Table 1附近

- paraphrase_cn：表1总结了设计原则、研究缺口和设计组件的对应关系。

- move_code：MAPPING_SUMMARY

- statement_status：design_decision

- why_here_cn：用表格把原则-缺口-组件三列对齐，是理论到设计的蓝图。

- inherits_from_previous_cn：汇总2.2.1-2.2.4全部内容。

- changes_argument_state_cn：让读者一眼看到每个理论原则如何落到组件。

- sets_up_next_cn：为第3节‘基于这些原则我们构建框架’做铺垫。

- failure_if_removed_cn：理论部分与设计部分的对齐关系不清晰，贡献难验。

- evidence_pointer：Section 2.2.5, Table 1

## 制品设计理由逐句图谱

### 1. Section 3 intro P1 S3

- locator：Section 3 intro P1 S3

- paraphrase_cn：选择contextual bandit而非完整RL，因为RL需要大量数据和系统动态知识，而医疗行为序列多外生且不受推荐系统控制。

- move_code：METHOD_SCOPE_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：在制品构建前先划定方法边界，说明为什么不选RL。

- inherits_from_previous_cn：承接‘我们提出bandit框架’。

- changes_argument_state_cn：限定本文技术贡献的范围在bandit，不是RL。

- sets_up_next_cn：为第6.2节局限讨论‘RL是未来方向’埋线。

- failure_if_removed_cn：读者会追问为什么不直接用RL，贡献边界模糊。

- evidence_pointer：Section 3 intro P1 S3

### 2. Section 3.1.1 P1 S1

- locator：Section 3.1.1 P1 S1

- paraphrase_cn：把推荐问题形式化为每期为每个用户推荐K个干预，以最大化整个推荐期的累计参与。

- move_code：PROBLEM_FORMALIZATION

- statement_status：design_decision

- why_here_cn：给出优化目标，是后续算法和评价指标的锚。

- inherits_from_previous_cn：承接第3节框架总述。

- changes_argument_state_cn：把模糊的‘推荐框架’变成可计算的top-K优化。

- sets_up_next_cn：为logistic奖励模型和式(2)做铺垫。

- failure_if_removed_cn：后文Precision@K等指标无对象。

- evidence_pointer：Section 3.1.1 P1 S1

### 3. Section 3.1.1 P2 S3-S4

- locator：Section 3.1.1 P2 S3-S4

- paraphrase_cn：假设用户反馈由潜在概率生成，该概率依赖于用户上下文、干预属性及其交互，参数未知需在线学习。

- move_code：REWARD_MODEL

- statement_status：design_decision

- why_here_cn：给出奖励生成假设，为TS后验更新提供模型。

- inherits_from_previous_cn：承接推荐问题形式化。

- changes_argument_state_cn：让‘参与’变成可估计的概率响应。

- sets_up_next_cn：为Algorithm 1的随机抽样与更新做铺垫。

- failure_if_removed_cn：TS没有模型对象，算法无法定义。

- evidence_pointer：Section 3.1.1 P2 S3-S4

### 4. Section 3.1.2 P1 S1-S3

- locator：Section 3.1.2 P1 S1-S3

- paraphrase_cn：bandit本身通过探索天然促进多样性，但医疗推荐需要更精细的方案来覆盖多维度需求，因此基于社会认知理论把维度分为结果导向和行为导向。

- move_code：DIVERSITY_DESIGN_RATIONALE

- statement_status：design_decision

- why_here_cn：解释为什么光靠bandit的随机探索不够。

- inherits_from_previous_cn：承接bandit框架与2.2.4理论。

- changes_argument_state_cn：从‘探索即多样性’推进到‘结构多样性’。

- sets_up_next_cn：引出式(3)约束。

- failure_if_removed_cn：多样性约束没有设计动机。

- evidence_pointer：Section 3.1.2 P1 S1-S3

### 5. Section 3.1.2 P1 S4-S6

- locator：Section 3.1.2 P1 S4-S6

- paraphrase_cn：用式(3)定义多样性约束：每个结果维度和行为维度至少包含一个干预。

- move_code：CONSTRAINT_DEFINITION

- statement_status：design_decision

- why_here_cn：把理论维度变成数学约束，是本文最核心的制品设计。

- inherits_from_previous_cn：承接‘两个维度’概念，具体化为约束集合。

- changes_argument_state_cn：从设计原则进入可求解的约束优化。

- sets_up_next_cn：为Algorithm 1的优化步骤做铺垫。

- failure_if_removed_cn：理论贡献无法落到算法，消融实验也没有对象。

- evidence_pointer：Section 3.1.2, Equation (3)

### 6. Section 3.1.2 P2 S1-S4

- locator：Section 3.1.2 P2 S1-S4

- paraphrase_cn：TS在贝叶斯设定下计算后验分布，通过概率匹配鼓励探索，经验表现通常优于UCB和ε-greedy。

- move_code：TS_RATIONALE

- statement_status：prior_literature

- why_here_cn：为选择TS而非其他bandit提供文献依据。

- inherits_from_previous_cn：承接‘如何求解带约束随机优化’。

- changes_argument_state_cn：从问题转到算法选择。

- sets_up_next_cn：引出Algorithm 1。

- failure_if_removed_cn：选TS显得武断，Experiment 1与UCB/ε-greedy对比失去基础。

- evidence_pointer：Section 3.1.2 P2

### 7. Section 3.2.1 P1 S1-S4

- locator：Section 3.2.1 P1 S1-S4

- paraphrase_cn：用户嵌入采用wide-and-deep网络融合静态属性与动态序列；wide分支处理属性特征，deep分支用LSTM与attention学习序列动态。

- move_code：USER_EMBEDDING_ARCHITECTURE

- statement_status：design_decision

- why_here_cn：把‘静态+动态融合’原则实例化为具体架构。

- inherits_from_previous_cn：承接2.2.3.1原则。

- changes_argument_state_cn：用户表示从‘特征拼接’升级为‘wide和deep双分支学习’。

- sets_up_next_cn：为eLSTM、attention、辅助损失子模块展开做铺垫。

- failure_if_removed_cn：用户嵌入没有架构，后文消融与t-SNE都失去对象。

- evidence_pointer：Section 3.2.1 P1

### 8. Section 3.2.1 P5 S1-S2

- locator：Section 3.2.1 P5 S1-S2

- paraphrase_cn：针对多序列问题和事件不规则性，用eLSTM把多个序列变换成元序列并用自注意机制识别顺序与间隔模式。

- move_code：ELSTM_DESIGN_RATIONALE

- statement_status：design_decision

- why_here_cn：直接回应2.2.3.2的多序列/不规则性要求。

- inherits_from_previous_cn：承接deep分支设计。

- changes_argument_state_cn：从单个LSTM升级为多序列合并的eLSTM。

- sets_up_next_cn：为attention公式和后续t-SNE轨迹验证做铺垫。

- failure_if_removed_cn：多序列挑战没有对应解决，设计贡献不成立。

- evidence_pointer：Section 3.2.1 P5 S1-S2

### 9. Section 3.2.1 P7 S1-S3

- locator：Section 3.2.1 P7 S1-S3

- paraphrase_cn：增加健康结果辅助损失有两个原因：把健康结果对偏好的影响纳入表示；在数据有限时帮助主模型提取序列信号。

- move_code：AUXILIARY_LOSS_RATIONALE

- statement_status：design_decision

- why_here_cn：给辅助损失提供理论（健康反馈）和技术（梯度平衡）双重理由。

- inherits_from_previous_cn：承接2.2.3.3健康结果机制。

- changes_argument_state_cn：把‘健康结果影响偏好’落实为损失函数项。

- sets_up_next_cn：为式(13)总损失与Experiment 6做铺垫。

- failure_if_removed_cn：辅助损失看似多余，健康结果实验缺乏机制说明。

- evidence_pointer：Section 3.2.1 P7 S1-S3

### 10. Section 3.2.2 P1 S1-S2

- locator：Section 3.2.2 P1 S1-S2

- paraphrase_cn：干预嵌入模型基于干预文本格式：用LSTM学习描述语义，用平均token嵌入提取标题信号。

- move_code：ITEM_EMBEDDING_ARCHITECTURE

- statement_status：design_decision

- why_here_cn：给出干预表示的基本结构。

- inherits_from_previous_cn：承接‘需改进干预表征’的设计要求。

- changes_argument_state_cn：干预从离散属性变成可学习的文本嵌入。

- sets_up_next_cn：为输出SMART元属性做铺垫。

- failure_if_removed_cn：干预嵌入没有载体，挑战嵌入消融实验失去意义。

- evidence_pointer：Section 3.2.2 P1

### 11. Section 3.2.2 P2 S3-S4

- locator：Section 3.2.2 P2 S3-S4

- paraphrase_cn：干预嵌入网络的输出映射到SMART元属性及动机、自我监测等关键干预元属性。

- move_code：ITEM_EMBEDDING_SUPERVISION

- statement_status：design_decision

- why_here_cn：用SMART领域知识作为监督信号，使干预表示承载可解释属性。

- inherits_from_previous_cn：承接2.2.3.3 SMART原则。

- changes_argument_state_cn：干预嵌入不再是纯文本向量，而输出结构化元属性。

- sets_up_next_cn：为第4.2表3的标注与挑战嵌入消融做铺垫。

- failure_if_removed_cn：SMART理论没有进入设计，只停留在文献。

- evidence_pointer：Section 3.2.2 P2 S3-S4

## Study开头、过渡与收束图谱

### 1. Section 4 opening P1

- locator：Section 4 opening P1

- paraphrase_cn：作者在真实在线减肥社区数据上评估推荐框架，并解释为何减肥管理是个人健康管理的代表性场景。

- move_code：EVALUATION_SETTING_OPENING

- statement_status：method_decision

- why_here_cn：开始实证部分前先交代数据场景的典型性。

- inherits_from_previous_cn：承接第3节构建的制品。

- changes_argument_state_cn：从设计构建切换到真实世界评价。

- sets_up_next_cn：为数据收集窗口与样本描述做铺垫。

- failure_if_removed_cn：评价缺乏场景合法性。

- evidence_pointer：Section 4 P1

### 2. Section 4.1 P1-S5

- locator：Section 4.1 P1-S5

- paraphrase_cn：描述性分析显示用户平均每周选约两个挑战，约70%时间选多个，多选时92%覆盖超过两种类型、51%覆盖全部三种类型。

- move_code：DESCRIPTIVE_DIVERSITY

- statement_status：empirical_result

- why_here_cn：在算法评估前先用数据证明偏好多样性真实存在。

- inherits_from_previous_cn：承接数据介绍。

- changes_argument_state_cn：用经验证据验证‘多样需求’假设。

- sets_up_next_cn：为下一句‘偏好随时间漂移’做铺垫。

- failure_if_removed_cn：多样性设计建立在虚构假设上。

- evidence_pointer：Section 4.1 P1

### 3. Section 4.1 P2 final sentence

- locator：Section 4.1 P2 final sentence

- paraphrase_cn：相邻周选择向量重叠率平均仅0.37，表明用户偏好有明显时间动态。

- move_code：DESCRIPTIVE_DYNAMICS

- statement_status：empirical_result

- why_here_cn：用同样的数据证明偏好动态性，为在线学习提供经验基础。

- inherits_from_previous_cn：承接选择向量操作化。

- changes_argument_state_cn：让‘动态偏好’从文献主张变成数据事实。

- sets_up_next_cn：为模型操作化和实验评价做铺垫。

- failure_if_removed_cn：bandit在线学习的必要性没有实证支持。

- evidence_pointer：Section 4.1 P2 final sentence

### 4. Section 4.2 P3 S1-S2

- locator：Section 4.2 P3 S1-S2

- paraphrase_cn：将多样性约束操作化为推荐集至少包含一个weight loss、一个diet、一个exercise挑战。

- move_code：OPERATIONALIZATION

- statement_status：method_decision

- why_here_cn：把理论维度落到数据可执行的三维约束。

- inherits_from_previous_cn：承接干预类型划分。

- changes_argument_state_cn：让式(3)在具体数据上可计算，并让消融实验有明确开关。

- sets_up_next_cn：为消融‘with vs without constraint’做铺垫。

- failure_if_removed_cn：多样性约束无法在评价中检验。

- evidence_pointer：Section 4.2 P3

### 5. Section 4.3 P1-P2

- locator：Section 4.3 P1-P2

- paraphrase_cn：t-SNE显示挑战嵌入按类型和强度聚集，用户嵌入按性别、年龄、体重变化状态聚集，同一用户轨迹连续。

- move_code：EMBEDDING_VALIDATION

- statement_status：empirical_result

- why_here_cn：在正式性能评估前先验证嵌入的构念效度。

- inherits_from_previous_cn：承接用户与干预嵌入模型。

- changes_argument_state_cn：提供机制级证据：嵌入捕捉了健康序列与干预语义。

- sets_up_next_cn：为Experiment 1的整体性能差异提供解释资源。

- failure_if_removed_cn：深度学习组件看起来是黑箱。

- evidence_pointer：Section 4.3

### 6. Section 5 opening P1

- locator：Section 5 opening P1

- paraphrase_cn：我们开展多种实验严格评估框架，并逐一预告六个实验各自的任务。

- move_code：EXPERIMENT_ROADMAP

- statement_status：method_decision

- why_here_cn：给读者一张实验路线图，说明每个试验负责什么。

- inherits_from_previous_cn：承接第4节数据与操作化。

- changes_argument_state_cn：从数据准备进入系统性能评价。

- sets_up_next_cn：为Experiment 1到6的顺序提供导航。

- failure_if_removed_cn：六个实验看起来杂乱无章。

- evidence_pointer：Section 5 opening P1

### 7. Section 5.1 P1 S1

- locator：Section 5.1 P1 S1

- paraphrase_cn：为证明整体有效性，与一系列state-of-the-art推荐系统比较。

- move_code：BENCHMARK_OPENING

- statement_status：method_decision

- why_here_cn：开启第一个实验，说明目的。

- inherits_from_previous_cn：承接实验路线图第一项。

- changes_argument_state_cn：把评价目标定义为与现有推荐系统对比。

- sets_up_next_cn：为基准模型分组选择做铺垫。

- failure_if_removed_cn：整体优势没有外部参照。

- evidence_pointer：Section 5.1 P1 S1

### 8. Section 5.1 P3 S1-S4

- locator：Section 5.1 P3 S1-S4

- paraphrase_cn：除标准指标外，使用DR离线估计处理历史数据选择偏差，并用omniscient模拟器生成反事实用户反馈。

- move_code：OFFLINE_EVAL_JUSTIFICATION

- statement_status：method_decision

- why_here_cn：回应离线数据只能观测被推荐动作的偏差问题。

- inherits_from_previous_cn：承接评价指标描述。

- changes_argument_state_cn：提升离线结果的因果可信度。

- sets_up_next_cn：为表4结果与Experiment 6模拟器做铺垫。

- failure_if_removed_cn：离线benchmark可能被质疑选择偏差。

- evidence_pointer：Section 5.1 P3

### 9. Section 5.1 P4 S1-S4

- locator：Section 5.1 P4 S1-S4

- paraphrase_cn：表4显示DLDE-MAB在所有指标上最高，batch模型整体不佳，且优于UCB和ε-greedy。

- move_code：BENCHMARK_RESULT

- statement_status：empirical_result

- why_here_cn：报告整体胜负结果。

- inherits_from_previous_cn：承接基准模型表。

- changes_argument_state_cn：确立整体有效性主张。

- sets_up_next_cn：制造‘为什么赢’的追问，引出消融。

- failure_if_removed_cn：文章的核心性能主张没有证据。

- evidence_pointer：Section 5.1, Table 4

### 10. Section 5.1 P5 S1

- locator：Section 5.1 P5 S1

- paraphrase_cn：这些结果共同证明定制bandit框架结合增强上下文表示与多样性促进能更好适应医疗偏好。

- move_code：BENCHMARK_CLOSURE

- statement_status：author_inference

- why_here_cn：把表4数字解释为设计组合有效，为消融铺垫。

- inherits_from_previous_cn：承接整体结果。

- changes_argument_state_cn：从‘我们赢’推进到‘因为组件组合’。

- sets_up_next_cn：为Experiment 2消隐提供问题。

- failure_if_removed_cn：整体结果没有解释，读者不知道赢在哪里。

- evidence_pointer：Section 5.1 P5

### 11. Section 5.2 P1 S1

- locator：Section 5.2 P1 S1

- paraphrase_cn：通过消融分析检查每个主要设计组件的有效性。

- move_code：ABLATION_OPENING

- statement_status：method_decision

- why_here_cn：开启第二个实验，把整体性能分解为组件贡献。

- inherits_from_previous_cn：承接Experiment 1留下的‘为何赢’。

- changes_argument_state_cn：从整体比较进入组件归因。

- sets_up_next_cn：为消融变体列表做铺垫。

- failure_if_removed_cn：整体优势无法归因于具体设计。

- evidence_pointer：Section 5.2 P1

### 12. Section 5.2 P2 S2-S4

- locator：Section 5.2 P2 S2-S4

- paraphrase_cn：去掉多样性约束降6.48%，去掉用户嵌入降2.94%，去掉挑战嵌入降12.16%，替代嵌入普遍更差。

- move_code：ABLATION_RESULT

- statement_status：empirical_result

- why_here_cn：定量报告每个组件被移除后的损失。

- inherits_from_previous_cn：承接消融设计。

- changes_argument_state_cn：把整体优势归因到具体组件。

- sets_up_next_cn：解释为什么挑战嵌入贡献最大，并引出替代嵌入比较。

- failure_if_removed_cn：设计组件贡献主张无证据。

- evidence_pointer：Section 5.2, Table 5

### 13. Section 5.2 P3-P4

- locator：Section 5.2 P3-P4

- paraphrase_cn：替代嵌入如Collab_Filter/Tabular/BERT/FastText表现更差，原因是它们未建模健康序列协同或未针对干预特征设计。

- move_code：ALTERNATIVE_EMBEDDING_DISCUSSION

- statement_status：author_inference

- why_here_cn：排除‘任何深度嵌入都能赢’的替代解释。

- inherits_from_previous_cn：承接消隐表中替代模型结果。

- changes_argument_state_cn：把优势归因于本文特定的嵌入设计而非通用深度学习。

- sets_up_next_cn：为Experiment 3-6机制检验做铺垫。

- failure_if_removed_cn：挑战嵌入贡献可能被解释为‘深度学习本身’。

- evidence_pointer：Section 5.2 P3-P4

### 14. Section 5.3 P1 S1-S3

- locator：Section 5.3 P1 S1-S3

- paraphrase_cn：挑选30名偏好变化最大的用户，重跑模型与基准，以检验对动态偏好的适应。

- move_code：DYNAMIC_USERS_OPENING

- statement_status：method_decision

- why_here_cn：开启第三个实验，针对动态机制做压力测试。

- inherits_from_previous_cn：承接Experiment 2后的‘如何适应动态’追问。

- changes_argument_state_cn：从静态平均切换到最动态用户子集。

- sets_up_next_cn：为图5相对变化结果做铺垫。

- failure_if_removed_cn：动态适应主张只是理论推断，无专项证据。

- evidence_pointer：Section 5.3 P1

### 15. Section 5.3 P2

- locator：Section 5.3 P2

- paraphrase_cn：图5显示DLDE-MAB在动态用户集上精度相对提升，UCB与ε-greedy各有升降，batch模型普遍下降。

- move_code：DYNAMIC_USERS_RESULT

- statement_status：empirical_result

- why_here_cn：报告动态用户专项结果，支持在线适应机制。

- inherits_from_previous_cn：承接动态用户选择。

- changes_argument_state_cn：把‘适应动态’从原理变为证据。

- sets_up_next_cn：为Experiment 4多样性分布做过渡。

- failure_if_removed_cn：在线学习优势无机制证据。

- evidence_pointer：Section 5.3, Figure 5

### 16. Section 5.4 P1 S1-S3

- locator：Section 5.4 P1 S1-S3

- paraphrase_cn：计算各模型推荐类型频率分布与真实选择频率分布的JSD，检验推荐多样性是否匹配真实偏好结构。

- move_code：DIVERSITY_DISTRIBUTION_OPENING

- statement_status：method_decision

- why_here_cn：开启第四个实验，用分布相似度检验多样性机制。

- inherits_from_previous_cn：承接Experiment 3后‘是否只是更会猜’的追问。

- changes_argument_state_cn：从精度转向推荐分布结构。

- sets_up_next_cn：为表6 JSD结果做铺垫。

- failure_if_removed_cn：多样性约束效果无直接证据。

- evidence_pointer：Section 5.4 P1

### 17. Section 5.4 P1 final sentence

- locator：Section 5.4 P1 final sentence

- paraphrase_cn：DLDE-MAB的JSD最小，表明其推荐多样性分布最接近真实选择。

- move_code：DIVERSITY_DISTRIBUTION_RESULT

- statement_status：empirical_result

- why_here_cn：报告多样性实验核心结论。

- inherits_from_previous_cn：承接JSD设计。

- changes_argument_state_cn：把多样性约束的效果从‘存在’升级为‘对齐真实需求’。

- sets_up_next_cn：为Experiment 5用户改进率做铺垫。

- failure_if_removed_cn：多样性约束只证明推荐多样，未证明多样得对。

- evidence_pointer：Section 5.4, Table 6

### 18. Section 5.5 P1 S1-S3

- locator：Section 5.5 P1 S1-S3

- paraphrase_cn：定义用户改进率为相比基线算法获得更多偏好物品的用户比例，以PMF为基线。

- move_code：USER_IMPROVEMENT_OPENING

- statement_status：method_decision

- why_here_cn：开启第五个实验，把推荐优势翻译为用户层面收益。

- inherits_from_previous_cn:：承接Experiment 4后‘对个体用户是否都好’。

- changes_argument_state_cn：从分布统计转向用户个体福利。

- sets_up_next_cn：为图6改进率结果做铺垫。

- failure_if_removed_cn：性能优势可能只惠及少数用户。

- evidence_pointer：Section 5.5 P1

### 19. Section 5.5 P1 result sentence

- locator：Section 5.5 P1 result sentence

- paraphrase_cn：DLDE-MAB用户改进率约97%，高于ε-greedy与UCB，远高于batch模型20%-80%。

- move_code：USER_IMPROVEMENT_RESULT

- statement_status：empirical_result

- why_here_cn：报告宏观用户改进结果，显示平台层面受益面。

- inherits_from_previous_cn：承接PMF基线。

- changes_argument_state_cn：把性能优势推广到用户群体福利。

- sets_up_next_cn：为平台可持续性含义与Experiment 6做铺垫。

- failure_if_removed_cn：平台意义与用户福利主张悬空。

- evidence_pointer：Section 5.5, Figure 6

### 20. Section 5.6 P1 S1-S4

- locator：Section 5.6 P1 S1-S4

- paraphrase_cn：为展示框架灵活性，将奖励信号从参与改为期内体重下降率，无需改变模型架构。

- move_code：HEALTH_OUTCOME_OPENING

- statement_status：method_decision

- why_here_cn：开启第六个实验，检验目标可迁移性。

- inherits_from_previous_cn：承接前五个实验后‘框架能否用于健康结果’的追问。

- changes_argument_state_cn：从参与率目标切换到健康结果目标。

- sets_up_next_cn：为反事实模拟器说明做铺垫。

- failure_if_removed_cn：健康结果导向这一重要扩展缺失。

- evidence_pointer：Section 5.6 P1

### 21. Section 5.6 P2 S1-S2

- locator：Section 5.6 P2 S1-S2

- paraphrase_cn：为评估需生成反事实体重结果，在挑战选择模拟器之外构建体重结果模拟器，并扰动权重近似噪声。

- move_code：COUNTERFACTUAL_SIMULATOR

- statement_status：method_decision

- why_here_cn：说明如何在没有真实实验的情况下估计体重变化。

- inherits_from_previous_cn：承接新的奖励信号。

- changes_argument_state_cn：为表7结果提供模拟证据来源。

- sets_up_next_cn：为结果报告做铺垫。

- failure_if_removed_cn：健康结果数字缺少来源，会被视为伪造。

- evidence_pointer：Section 5.6 P2

### 22. Section 5.6 P3

- locator：Section 5.6 P3

- paraphrase_cn：表7显示DLDE-MAB平均期内体重下降率最高（top-5 72.75%，top-10 73.61%），依赖选择历史的深度batch模型最差。

- move_code：HEALTH_OUTCOME_RESULT

- statement_status：empirical_result

- why_here_cn：报告健康结果实验结果，展示目标互迁移。

- inherits_from_previous_cn：承接体重结果模拟器。

- changes_argument_state_cn：把框架价值从参与率扩展到健康结果。

- sets_up_next_cn：为第6节讨论中的灵活性与局限做铺垫。

- failure_if_removed_cn：健康导向贡献失去证据。

- evidence_pointer：Section 5.6, Table 7

## 讨论与贡献逐句图谱

### 1. Discussion P1 S1-S2

- locator：Discussion P1 S1-S2

- paraphrase_cn：本研究开发了帮助个体参与在线医疗干预的个性化推荐系统，并按设计科学范式用系列实验检验其性能。

- move_code：RESEARCH_SUMMARY

- statement_status：contribution_claim

- why_here_cn：开场回顾研究做了什么，以设计科学范式定位。

- inherits_from_previous_cn：承接全部实验。

- changes_argument_state_cn：从实证结果回到全文总成绩。

- sets_up_next_cn：引出结果小结与贡献。

- failure_if_removed_cn：讨论没有锚点，直接进入贡献显得突兀。

- evidence_pointer：Discussion P1 S1-S2

### 2. Discussion P1 S3

- locator：Discussion P1 S3

- paraphrase_cn：评价结果表明系统能有效适应动态且多样的医疗偏好，并优于多种state-of-the-art推荐模型。

- move_code：RESULT_SUMMARY

- statement_status：empirical_result

- why_here_cn：用一句话重述核心实证结论。

- inherits_from_previous_cn：承接研究概述。

- changes_argument_state_cn：把机制与性能结论并置。

- sets_up_next_cn：为贡献定位做铺垫。

- failure_if_removed_cn：讨论与实际结果脱节。

- evidence_pointer：Discussion P1 S3

### 3. Discussion P2 S1

- locator：Discussion P2 S1

- paraphrase_cn：本研究贡献于商业智能应用的新兴文献，展示prescriptive analytics可与IT制品整合产生可应用洞见。

- move_code：DISCIPLINARY_POSITIONING

- statement_status：contribution_claim

- why_here_cn：把文章锚定为IS/prescriptive analytics贡献，而不只是ML。

- inherits_from_previous_cn：承接研究小结。

- changes_argument_state_cn：从技术成绩升级到学科贡献。

- sets_up_next_cn：引出医疗推荐文献贡献。

- failure_if_removed_cn：文章与IS学科的联系消失。

- evidence_pointer：Discussion P2 S1

### 4. Discussion P2 S2

- locator：Discussion P2 S2

- paraphrase_cn：我们丰富医疗推荐文献，设计并评价了自动化个性化医疗推荐的新框架。

- move_code：HEALTHCARE_RECOMMENDATION_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：细化贡献到医疗推荐子领域。

- inherits_from_previous_cn：承接商业智能贡献。

- changes_argument_state_cn：把贡献范围从通用IS缩到医疗推荐。

- sets_up_next_cn：引出方法论贡献。

- failure_if_removed_cn：医疗推荐文献增量缺失。

- evidence_pointer：Discussion P2 S2

### 5. Discussion P2 S3-S5

- locator：Discussion P2 S3-S5

- paraphrase_cn：方法论贡献包括：理论引导多样化与深度上下文增强的bandit统一框架；用户嵌入中的eLSTM多序列建模与健康结果辅助损失。

- move_code：METHOD_CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：列举三个技术新点，与第3节设计一一对应。

- inherits_from_previous_cn：承接医疗推荐贡献。

- changes_argument_state_cn：把制品细节转化为可引用贡献。

- sets_up_next_cn：为设计科学文献贡献做铺垫。

- failure_if_removed_cn：贡献停留在‘新框架’而无具体方法增量。

- evidence_pointer：Discussion P2 S3-S5

### 6. Discussion P3 S1-S3

- locator：Discussion P3 S1-S3

- paraphrase_cn：实践上框架帮助用户更好参与干预、改善依从性，为平台提供用户参与体验的可行方案并促进可持续性。

- move_code：PRACTICE_CONTRIBUTION_USERS_PLATFORM

- statement_status：contribution_claim

- why_here_cn：给出用户和平台两方实践含义。

- inherits_from_previous_cn：承接方法论贡献后转向实践。

- changes_argument_state_cn：把技术贡献翻译成利益相关者收益。

- sets_up_next_cn：引出政策制定者含义。

- failure_if_removed_cn：实践价值缺失，应用导向不完整。

- evidence_pointer：Discussion P3 S1-S3

### 7. Discussion P3 S4-S5

- locator：Discussion P3 S4-S5

- paraphrase_cn：对政策制定者，本研究展示将IT制品与医疗交付整合以改进个性化的方式；政策制定者可在主要在线医疗门户集成推荐系统。

- move_code：PRACTICE_CONTRIBUTION_POLICY

- statement_status：contribution_claim

- why_here_cn：给出政策层面含义，扩大贡献面。

- inherits_from_previous_cn：承接用户/平台含义。

- changes_argument_state_cn：贡献从技术延伸到公共健康管理。

- sets_up_next_cn：引入一般化讨论。

- failure_if_removed_cn：政策含义缺失，摘要中的stakeholders不完整。

- evidence_pointer：Discussion P3 S4-S5

### 8. Section 6.1 P1 S1-S2

- locator：Section 6.1 P1 S1-S2

- paraphrase_cn：减肥管理是个人健康管理的代表性场景；其他慢病（糖尿病、心血管）也需调节类似健康与行为方面。

- move_code：GENERALIZABILITY_OPENING

- statement_status：author_inference

- why_here_cn：开始论证结论可迁移到其他健康场景。

- inherits_from_previous_cn：承接实践贡献。

- changes_argument_state_cn：从单一场景扩展到多场景。

- sets_up_next_cn：为‘设计组件可定制’做铺垫。

- failure_if_removed_cn：贡献被限定在减肥社区，外部有效性弱。

- evidence_pointer：Section 6.1 P1

### 9. Section 6.1 P2 S1-S4

- locator：Section 6.1 P2 S1-S4

- paraphrase_cn：深度表示学习可处理不同健康行为数据，多样性约束可替换维度，因此设计可推广到穿戴设备、移动健康和医疗文档。

- move_code：GENERALIZABILITY_ELABORATION

- statement_status：author_inference

- why_here_cn：说明哪个组件可迁移、如何迁移。

- inherits_from_previous_cn：承接‘设计是通用的’。

- changes_argument_state_cn：把一般化主张落到具体组件。

- sets_up_next_cn：为局限性讨论做铺垫。

- failure_if_removed_cn：一般化只是口号，没有机制说明。

- evidence_pointer：Section 6.1 P2

### 10. Section 6.2 P1 S1-S3

- locator：Section 6.2 P1 S1-S3

- paraphrase_cn：本研究只用在线数据；未来可整合穿戴设备与医院电子健康记录等离线数据以提高推荐。

- move_code：LIMITATION_DATA

- statement_status：author_inference

- why_here_cn：开始局限性讨论，承认数据来源限制。

- inherits_from_previous_cn：承接一般化之后。

- changes_argument_state_cn：从贡献转向诚实边界。

- sets_up_next_cn：引出bandit vs RL局限。

- failure_if_removed_cn：文章显得忽略数据局限。

- evidence_pointer：Section 6.2 P1

### 11. Section 6.2 P1 S4-S6

- locator：Section 6.2 P1 S4-S6

- paraphrase_cn：本文bandit假设上下文独立同分布，忽略干预对未来状态的影响；更完整的模型属于RL，是bandit的严格推广。

- move_code：LIMITATION_MODEL_SCOPE

- statement_status：author_inference

- why_here_cn：明确建模边界，防止把bandit结果过度解释为RL。

- inherits_from_previous_cn：承接在线数据局限后转向模型局限。

- changes_argument_state_cn：从数据边界进入模型边界。

- sets_up_next_cn：为RL挑战的具体讨论做铺垫。

- failure_if_removed_cn：bandit的假设问题被隐藏，贡献被过度宣称。

- evidence_pointer：Section 6.2 P1 S4-S6

### 12. Section 6.2 P2 S1-S4

- locator：Section 6.2 P2 S1-S4

- paraphrase_cn：在医疗场景应用完整RL面临两大挑战：定义包含所有决策信息的状态变量困难；状态空间大且连续，数据需求极高。

- move_code：RL_CHALLENGES

- statement_status：author_inference

- why_here_cn：解释为什么未来工作才做RL，同时为自己的bandit选择辩护。

- inherits_from_previous_cn：承接‘RL是严格推广’。

- changes_argument_state_cn：把局限转成合理边界与未来方向。

- sets_up_next_cn：为结论句做铺垫。

- failure_if_removed_cn：读者可能认为作者回避RL是因为能力不足。

- evidence_pointer：Section 6.2 P2

### 13. Section 6.2 P2 S5-S7

- locator：Section 6.2 P2 S5-S7

- paraphrase_cn：bandit学习速度快，适合在线平台高流失率，能提供合理近似，因此我们把完整RL留给未来。

- move_code：CLOSING_JUSTIFICATION

- statement_status：author_inference

- why_here_cn：以‘bandit合理’收尾，保护当前贡献。

- inherits_from_previous_cn：承接RL挑战。

- changes_argument_state_cn：把‘我们没有做RL’重新解释为‘bandit是恰当近似’。

- sets_up_next_cn：结束全文。

- failure_if_removed_cn：文章结尾显得承认失败而非选择权衡。

- evidence_pointer：Section 6.2 P2 S5-S7

## Study累积逻辑

### 1. 1

- study_or_phase：理论设计原则提炼（Section 2）

- evidence_job_cn：从行为健康理论证明‘动态、多样、复杂上下文’三类要求是医疗推荐设计的正当约束。

- what_it_establishes_cn：建立设计原则：适应不确定性、改进上下文表示、适应多样需求。

- what_it_cannot_establish_cn：不能证明这些要求可被任何算法满足。

- why_next_phase_is_needed_cn：需要把原则实例化为可运行制品。

- transition_wording_function_cn：‘基于这些原则，我们构建框架’实现从理论到设计的切换。

### 2. 2

- study_or_phase：DLDE-MAB制品构建（Section 3）

- evidence_job_cn：证明设计原则可转化为具体算法、网络结构与约束。

- what_it_establishes_cn：给出TS加多样性约束、用户与干预嵌入的可计算方法。

- what_it_cannot_establish_cn：不能证明组件在真实数据上有用。

- why_next_phase_is_needed_cn：需要真实数据评价与操作化。

- transition_wording_function_cn：第4节开头‘我们在真实数据上评价’切换到实证。

### 3. 3

- study_or_phase：数据描述性分析（Section 4.1）

- evidence_job_cn：用真实平台数据证明多样性与动态性不只是理论假设。

- what_it_establishes_cn：约70%多选、92%跨两类型、重叠率0.37等事实。

- what_it_cannot_establish_cn：不能证明推荐框架有效。

- why_next_phase_is_needed_cn：需要模型操作化与嵌入验证，再进入性能评价。

- transition_wording_function_cn：从‘偏好确实多样动态’进入‘模型能否捕获’。

### 4. 4

- study_or_phase：嵌入可视化验证（Section 4.3）

- evidence_job_cn：证明深度嵌入捕获了干预语义与用户健康序列模式。

- what_it_establishes_cn：挑战嵌入按类型/强度聚集，用户嵌入按特征与轨迹连续。

- what_it_cannot_establish_cn：不能替代推荐性能指标。

- why_next_phase_is_needed_cn：需要正式指标证明嵌入带来性能优势。

- transition_wording_function_cn：‘我们开展系列实验’进入第5节。

### 5. 5

- study_or_phase：Experiment 1 整体benchmark

- evidence_job_cn：与18个batch、深度、bandit基准比较，建立整体有效性。

- what_it_establishes_cn：DLDE-MAB在六项指标上全面领先，且优于UCB/ε-greedy。

- what_it_cannot_establish_cn：不能证明哪个组件导致领先。

- why_next_phase_is_needed_cn：需要消融归因组件贡献。

- transition_wording_function_cn：‘我们进行消融以检验每个组件’。

### 6. 6

- study_or_phase：Experiment 2 消融分析

- evidence_job_cn：把整体优势分解到多样性约束、用户嵌入、干预嵌入三个组件。

- what_it_establishes_cn：移除任一组件都显著下降，替代嵌入更差。

- what_it_cannot_establish_cn：不能直接展示动态适应与多样性的机制。

- why_next_phase_is_needed_cn：需要专项实验验证机制。

- transition_wording_function_cn：‘我们聚焦偏好变化最大的用户’转向动态机制。

### 7. 7

- study_or_phase：Experiment 3 动态用户专项

- evidence_job_cn：在偏好最动态的用户子集上检验在线适应机制。

- what_it_establishes_cn：框架在动态用户上精度相对提升，batch下降。

- what_it_cannot_establish_cn：不能证明推荐组合的多样性匹配真实结构。

- why_next_phase_is_needed_cn：需要JSD检验多样性分布。

- transition_wording_function_cn：‘我们评估推荐多样性分布是否近似真实’。

### 8. 8

- study_or_phase：Experiment 4 多样性分布

- evidence_job_cn：用JSD证明推荐多样性分布最接近真实选择。

- what_it_establishes_cn：DLDE-MAB的JSD最小（0.0456）。

- what_it_cannot_establish_cn：不能证明个体层面的用户受益。

- why_next_phase_is_needed_cn：需要用户层面改进率检验。

- transition_wording_function_cn：‘从宏观角度看是否惠及更多用户’。

### 9. 9

- study_or_phase：Experiment 5 用户改进率

- evidence_job_cn：把推荐优势翻译为用户群体福利。

- what_it_establishes_cn：相对PMF约97%用户获得更多偏好物品。

- what_it_cannot_establish_cn：不能证明长期健康结果改善。

- why_next_phase_is_needed_cn：需要改变奖励信号检验健康结果导向。

- transition_wording_function_cn：‘作为扩展，我们考虑以健康结果为奖励’。

### 10. 10

- study_or_phase：Experiment 6 健康结果反事实扩展

- evidence_job_cn：证明框架可切换目标函数，并探索健康结果优化。

- what_it_establishes_cn：新奖励下DLDE-MAB仍最高（top-5 72.75%，top-10 73.61%）。

- what_it_cannot_establish_cn：不能证明真实临床结局，因为采用模拟器。

- why_next_phase_is_needed_cn：讨论需要把结果升华为设计知识与边界。

- transition_wording_function_cn：第6节‘本研究开发…’把全部实验收束为贡献。

## 主张—证据台账

### 1. DLDE-MAB整体优于state-of-the-art推荐系统。

- claim_cn：DLDE-MAB整体优于state-of-the-art推荐系统。

- claim_level：technical

- supporting_evidence_cn：Table 4显示DLDE-MAB在所有六项指标上最高，几乎所有基准显著更差。

- support_strength：direct

- where_claim_is_made：Section 5.1 P4-P5

- where_evidence_is_provided：Section 5.1 Table 4

### 2. 多样性约束、用户嵌入、干预嵌入各自有效。

- claim_cn：多样性约束、用户嵌入、干预嵌入各自有效。

- claim_level：artifact

- supporting_evidence_cn：Table 5消隐显示去约束降6.48%、去用户嵌入降2.94%、去挑战嵌入降12.16%。

- support_strength：direct

- where_claim_is_made：Section 5.2 P2

- where_evidence_is_provided：Section 5.2 Table 5

### 3. 本文独特的深度嵌入设计优于替代深度学习嵌入。

- claim_cn：本文独特的深度嵌入设计优于替代深度学习嵌入。

- claim_level：artifact

- supporting_evidence_cn：Table 5中DLDE-Collab、DLDE-Tabular、DLDE-BERT、DLDE-FastText均显著更差。

- support_strength：direct

- where_claim_is_made：Section 5.2 P3-P4

- where_evidence_is_provided：Section 5.2 Table 5

### 4. 框架能适应偏好最动态的用户。

- claim_cn：框架能适应偏好最动态的用户。

- claim_level：mechanism

- supporting_evidence_cn：Experiment 3在30名最动态用户上精度相对提升，batch模型下降。

- support_strength：direct

- where_claim_is_made：Section 5.3 P2

- where_evidence_is_provided：Section 5.3 Figure 5

### 5. 推荐多样性分布符合用户真实偏好结构。

- claim_cn：推荐多样性分布符合用户真实偏好结构。

- claim_level：mechanism

- supporting_evidence_cn：Table 6中DLDE-MAB的JSD最小（0.0456）。

- support_strength：direct

- where_claim_is_made：Section 5.4 P1 final sentence

- where_evidence_is_provided：Section 5.4 Table 6

### 6. 推荐能惠及更大比例的用户群体。

- claim_cn：推荐能惠及更大比例的用户群体。

- claim_level：boundary

- supporting_evidence_cn：Figure 6显示相对PMF约97%用户改进率，高于其他模型。

- support_strength：partial

- where_claim_is_made：Section 5.5 P1 result sentence

- where_evidence_is_provided：Section 5.5 Figure 6

### 7. 框架可用于改善健康结果（体重下降）。

- claim_cn：框架可用于改善健康结果（体重下降）。

- claim_level：design_knowledge

- supporting_evidence_cn：Table 7显示改为体重下降奖励后DLDE-MAB平均期内体重下降率最高。

- support_strength：partial

- where_claim_is_made：Section 5.6 P3

- where_evidence_is_provided：Section 5.6 Table 7

### 8. 在线学习优于batch学习与纯exploitation/exploration。

- claim_cn：在线学习优于batch学习与纯exploitation/exploration。

- claim_level：technical

- supporting_evidence_cn：Table 4中batch模型整体差于DLDE-MAB；附录A9.1有side experiment。

- support_strength：direct

- where_claim_is_made：Section 5.1 P4

- where_evidence_is_provided：Section 5.1 Table 4；Online Appendix A9.1

### 9. 理论驱动的多样性约束优于随机多样性。

- claim_cn：理论驱动的多样性约束优于随机多样性。

- claim_level：theory

- supporting_evidence_cn：Table 5中移除约束导致显著下降；Table 6中JSD最小支持对齐真实多样性。

- support_strength：direct

- where_claim_is_made：Section 5.2 P2；Section 5.4

- where_evidence_is_provided：Section 5.2 Table 5；Section 5.4 Table 6

### 10. 研究贡献于prescriptive analytics与设计科学。

- claim_cn：研究贡献于prescriptive analytics与设计科学。

- claim_level：theory

- supporting_evidence_cn：讨论中将框架定位为设计科学制品；但证据依赖离线benchmark与模拟，无现场部署。

- support_strength：partial

- where_claim_is_made：Discussion P2 S1

- where_evidence_is_provided：Section 5 Table 4-7

### 11. 健康结果辅助损失有助于用户表示。

- claim_cn：健康结果辅助损失有助于用户表示。

- claim_level：mechanism

- supporting_evidence_cn：用户嵌入整体消融有效，但没有单独消融辅助损失。

- support_strength：partial

- where_claim_is_made：Section 3.2.1 P7

- where_evidence_is_provided：Section 5.2 Table 5（仅整体用户嵌入）

### 12. eLSTM与attention能捕获多序列相关与事件不规则性。

- claim_cn：eLSTM与attention能捕获多序列相关与事件不规则性。

- claim_level：mechanism

- supporting_evidence_cn：t-SNE轨迹连续与用户嵌入消融下降间接支持；无单独消融。

- support_strength：partial

- where_claim_is_made：Section 3.2.1 P5；Section 4.3

- where_evidence_is_provided：Section 4.3 Figure 4；Section 5.2 Table 5

## ISR定位逻辑

- constitutive_is_problem_cn：文章把健康管理自我调节过程与在线平台的干预供给之间的匹配问题构成为IS问题：用户的持续参与不只是偏好匹配，而是受健康信息不对称、动态偏好与多维度健康需求共同制约的决策支持问题。平台需要设计能实时更新、能在探索与利用间平衡、并能利用多源健康数据推断用户上下文的信息制品。

- technology_behavior_or_market_entanglement_cn：技术设计（bandit探索、深度表示、多样性约束）直接嵌入用户的健康行为过程：健康结果反馈被建模为辅助损失与奖励信号，社交行为、自我监测等行为轨迹被建模为用户嵌入输入，推荐集的结构多样性被约束为覆盖结果与行为维度。因此技术不是外生工具，而构成用户健康行为的调节回路。

- role_of_benchmark_or_objective_evidence_cn：benchmark、DR估计、omniscient模拟与JSD不是用来证明‘分数更高’，而是用来支持以下IS主张：在线学习能适应健康偏好漂移、深度表示能捕获健康行为多序列结构、理论约束能使推荐结构对齐真实健康需求。客观证据承担了从制品性能到机制解释再到设计知识的上升功能。

- theory_in_design_cn：理论以两种方式进入设计：第一，社会认知理论与SMART目标设定直接决定多样性约束维度和干预嵌入输出属性；第二，健康结果反馈理论决定辅助损失与奖励信号设计。理论不是事后解释结果的标签，而是先于实现的设计约束；但bandit架构与深度学习组件本身来自ML/CIS文献，属于部分耦合。

- technical_vs_is_contribution_balance_cn：约三成篇幅用于技术构建（bandit、eLSTM、wide-and-deep、SMART嵌入），约六成用于评价与机制验证（六个实验、消融、JSD、用户改进率、健康结果仿真），结尾把技术细节上缴为设计知识与IS贡献。作者刻意避免把文章写成‘我们算法更好’，而是强调组件如何对应健康理论设计原则。

- beyond_transient_performance_cn：文章通过消隐、动态用户专项、JSD与用户改进率把一次性分数优势转成可归因的设计知识：每个组件对应一条理论原则和一类证据；目标切换实验（Experiment 6）进一步表明框架不绑定单目标，从而把贡献从‘某一数据上的优势’提升为‘可复用设计’。不过其‘用户福利/平台可持续’仍部分依赖用户改进率与模拟健康结果，存在一定跳跃。

## 段落级仿写模板

### abstract_steps

#### 1. S1

- step：S1

- job_cn：用一句事实性背景句建立应用场景。

- evidence_required_cn：有明确平台/领域背景。

#### 2. S2

- step：S2

- job_cn：指出问题及其人群层面后果。

- evidence_required_cn：问题机制文献或平台证据。

#### 3. S3

- step：S3

- job_cn：宣布研究目标。

- evidence_required_cn：目标可操作化为系统输出。

#### 4. S4

- step：S4

- job_cn：一句话给出制品核心特征。

- evidence_required_cn：制品已实现或有技术原型。

#### 5. S5

- step：S5

- job_cn：说明评价数据/环境。

- evidence_required_cn：真实或高质量数据集。

#### 6. S6

- step：S6

- job_cn：报告整体结果并强调组件有效。

- evidence_required_cn：benchmark与消融结果。

#### 7. S7

- step：S7

- job_cn：给出学科贡献与利益相关者。

- evidence_required_cn：能定位到IS子领域，如prescriptive analytics。

### introduction_paragraph_steps

#### 1. P1

- step：P1

- job_cn：建立领域重要性、场景与平台。

- evidence_required_cn：领域事实、平台例子、应用文献。

#### 2. P2

- step：P2

- job_cn：从现象到机制再到后果，最后推出服务需求。

- evidence_required_cn：选择过载文献+医疗特殊性论证。

#### 3. P3

- step：P3

- job_cn：宣布目标并预告领域差异。

- evidence_required_cn：目标可操作化为K项推荐。

#### 4. P4

- step：P4

- job_cn：列出本领域的2-3个技术挑战，形成缺口。

- evidence_required_cn：每项挑战都有健康理论与数据复杂性支撑。

#### 5. P5

- step：P5

- job_cn：给出解决方案总体设计并逐一对应挑战。

- evidence_required_cn：已有算法/模型结构与每个挑战的对应。

#### 6. P6

- step：P6

- job_cn：预告评价设计与证据层次。

- evidence_required_cn：已规划benchmark、消融、机制实验。

#### 7. P7

- step：P7

- job_cn：声明学术与实践贡献。

- evidence_required_cn：能列出3个设计新点与3类利益相关者。

### theory_to_design_steps

#### 1. T1

- step：T1

- job_cn：总结相关文献并指出batch/已有推荐的具体缺陷。

- evidence_required_cn：文献中的可机制化限制。

#### 2. T2

- step：T2

- job_cn：从行为/组织理论提炼设计原则。

- evidence_required_cn：理论提出的维度/机制可被算法化。

#### 3. T3

- step：T3

- job_cn：用映射表把原则、缺口、组件三列对齐。

- evidence_required_cn：每个原则至少对应一个可执行组件。

#### 4. T4

- step：T4

- job_cn：从原则进入制品章节前的过渡句。

- evidence_required_cn：声明‘基于原则构建’。

### method_and_study_sequence_steps

#### 1. M1

- step：M1

- job_cn：先描述数据与场景典型性。

- evidence_required_cn：数据源、时间窗口、样本与变量。

#### 2. M2

- step：M2

- job_cn：用描述性分析验证设计假设。

- evidence_required_cn：能证明动态/多样现象存在的统计。

#### 3. M3

- step：M3

- job_cn：模型操作化：把理论约束变成可计算形式。

- evidence_required_cn：明确的变量定义与可执行约束。

#### 4. M4

- step：M4

- job_cn：嵌入可视化验证表示质量。

- evidence_required_cn：t-SNE或其他可解释可视化。

#### 5. M5

- step：M5

- job_cn：按‘整体→组件→机制→用户→目标迁移’排列实验。

- evidence_required_cn：每个实验解决前一个实验留给的未答问题。

### results_reporting_steps

#### 1. R1

- step：R1

- job_cn：先报告整体benchmark，并解释设计组合意义。

- evidence_required_cn：多指标、多基准、显著性检验。

#### 2. R2

- step：R2

- job_cn：用消融把整体成绩归因到组件。

- evidence_required_cn：移除组件与替代设计的对照。

#### 3. R3

- step：R3

- job_cn：用专项实验展示机制（动态、多样性）。

- evidence_required_cn：子集分析、分布相似度等。

#### 4. R4

- step：R4

- job_cn：把结果翻译为用户/平台层收益。

- evidence_required_cn：用户改进率等宏观统计。

#### 5. R5

- step：R5

- job_cn：用目标切换实验检验扩展性。

- evidence_required_cn：新奖励下的反事实或仿真证据。

### discussion_and_contribution_steps

#### 1. D1

- step：D1

- job_cn：重述研究结果并将其定位到学科子领域。

- evidence_required_cn：全文主要结果。

#### 2. D2

- step：D2

- job_cn：逐条列理论/方法贡献，对应设计组件。

- evidence_required_cn：消融与专项实验结果。

#### 3. D3

- step：D3

- job_cn：给出实践方贡献（用户、平台、政策）。

- evidence_required_cn：能从结果合理推出的实践含义。

#### 4. D4

- step：D4

- job_cn：论证一般化：哪些组件可迁移、如何迁移。

- evidence_required_cn：组件的领域无关性说明。

#### 5. D5

- step：D5

- job_cn：诚实给出数据、模型、因果边界与未来方向。

- evidence_required_cn：对方法假设的了解与替代方案讨论。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：用领域重要性与一个具体平台现象开场。

- research_evidence_required_cn：领域数据/文献证明问题存在且重要。

- sentence_pattern_function_cn：首句给重要性，次句给场景，再用平台例子具体化。

- transition_condition_cn：当读者对‘在哪里发生’有了清晰画面后转入问题。

### 2. 2

- step：2

- rhetorical_job_cn：把现象转成‘机制+后果+需求’链条。

- research_evidence_required_cn：每个环节至少有文献或统计支持。

- sentence_pattern_function_cn：先给原因句，再给后果句，最后用‘因此需要…’收束。

- transition_condition_cn：当‘服务需求’被读者接受后宣布研究目标。

### 3. 3

- step：3

- rhetorical_job_cn：从目标进入本领域的2-3个特异挑战，并总结为缺口。

- research_evidence_required_cn：每项挑战与领域理论或数据特征绑定。

- sentence_pattern_function_cn：‘首先…其次…第三…’并列；末句以‘这些仍是主要障碍’收束。

- transition_condition_cn：当读者确信‘通用方法不能直接迁移’后给出解决方案。

### 4. 4

- step：4

- rhetorical_job_cn：给出方案整体结构，并让每个组件对应一个挑战。

- research_evidence_required_cn：算法/模型设计与挑战有明确映射。

- sentence_pattern_function_cn：先给框架名，再逐句解释每个组件解决哪个挑战。

- transition_condition_cn：当组件与挑战一一对应后预告评价设计。

### 5. 5

- step：5

- rhetorical_job_cn：从行为/组织理论提炼设计原则并用映射表固定。

- research_evidence_required_cn：理论能导出可算法化的维度或机制。

- sentence_pattern_function_cn：原则句→理论句→设计含义句的重复结构，最后以表格汇总。

- transition_condition_cn：当每个原则都能指向具体组件后进入制品章节。

### 6. 6

- step：6

- rhetorical_job_cn：把原则实例化为可运行制品，并解释每个关键设计选择的理由。

- research_evidence_required_cn：形式化定义、算法伪代码、网络结构与损失函数。

- sentence_pattern_function_cn：问题定义句→模型假设句→算法描述句→深度结构句→损失函数句。

- transition_condition_cn：当制品可被复现后转入数据与评价。

### 7. 7

- step：7

- rhetorical_job_cn：用描述性数据验证设计假设，再操作化模型并验证表示质量。

- research_evidence_required_cn：真实数据上能证明动态/多样性的事实统计与可视化。

- sentence_pattern_function_cn：数据描述句→统计证据句→操作化定义句→可视化解释句。

- transition_condition_cn：当读者信服假设成立后进入正式性能评价。

### 8. 8

- step：8

- rhetorical_job_cn：先用整体benchmark建立优势，再用消融归因到组件，再用专项实验验证机制。

- research_evidence_required_cn：多基准多指标结果、消融表、动态用户分析、JSD、用户改进率。

- sentence_pattern_function_cn：每个实验以目的句开场，以结果句报告，以解释句收尾，并用过渡句指向下一实验。

- transition_condition_cn：当上一实验留下未答问题且下一实验能回答时进入下一步。

### 9. 9

- step：9

- rhetorical_job_cn：用目标切换实验检验框架的可迁移性与边界。

- research_evidence_required_cn：反事实模拟或可辩护的新目标实验。

- sentence_pattern_function_cn：先给出新的目标信号，再说明模拟器，再报告结果。

- transition_condition_cn：当扩展性得到展示后进入讨论。

### 10. 10

- step：10

- rhetorical_job_cn：在讨论中完成从结果到贡献的升级，并给出一般化与局限。

- research_evidence_required_cn：能支撑每一条贡献的实验指针；对边界的诚实说明。

- sentence_pattern_function_cn：重述结果→IS定位→方法贡献→实践贡献→一般化→局限与未来。

- transition_condition_cn：当贡献有证据对应且边界被划定后结束全文。

## 应模仿的高价值动作

1. 用三大挑战结构化引言缺口，每个挑战都对应一个后续设计组件，使技术选择有义务可溯。

2. 理论到设计用表1做原则—缺口—组件三列映射，让消隐实验可以直接对应理论主张。

3. 先描述性证明偏好动态与多样真实存在，再构建算法，避免‘假设驱动设计’的空中楼阁。

4. 整体benchmark后立刻做消隐，把‘我们赢’分解成‘因为哪个组件赢’。

5. 用t-SNE嵌入可视化作为性能差异前的机制合法性证据。

6. 在离线评价中引入DR估计和omniscient模拟，主动回应历史日志选择偏差。

7. 实验顺序按‘整体→组件→机制→用户→目标迁移’递进，每个实验开头用一句目的句，结尾用一句过渡句。

8. 动态用户专项用相对变化而非绝对指标表达，使机制在子集中更直观。

9. 用JSD检验推荐分布与真实偏好结构的相似性，而不是只看多样性数量。

10. 目标切换实验（参与率→体重下降）证明框架不绑定单一奖励，提升可复用设计知识。

11. 讨论中以‘bandit学习快、适合高流失平台’把无RL的局限重写为合理边界。

## 不要只复制的表面动作

1. 不要只抄‘三个挑战’的结构而无相应组件对应，否则成为装饰性缺口。

2. 不要只创建一个多样性约束而不给出理论维度来源，否则与随机探索无异。

3. 不要只堆LSTM/注意力而不说明它们对应哪条健康行为机制。

4. 不要只报告整体指标就宣称组件有效，必须有消隐。

5. 不要用离线模拟结果直接声称真实健康改善。

6. 不要只讲‘算法更好’而不做IS学科定位，否则被归为纯ML论文。

7. 不要把所有深度嵌入都说成‘本文设计有效’而不做替代嵌入对比。

8. 不要在讨论中把bandit假设写死后又回避RL，必须给出为何不做RL的理由。

## 证据薄弱或跳跃的动作

1. 用户嵌入中辅助损失、attention、eLSTM的独立贡献未分别消融，只能依赖整体用户嵌入消融推断。

2. 健康结果实验基于omniscient模拟器而非真实随机实验，表7数字不能直接作为医疗效果。

3. 动态用户专项只选30名用户，样本小，可能放大模型相对优势。

4. 用户改进率基于历史选择偏好，而非长期真实参与或健康结局，用户福利主张存在跳跃。

5. SMART属性、motivational与self-monitoring的人工标注流程在正文未展开，标注质量依赖附录。

6. t-SNE可视化只提供直观证据，不能作为严格统计检验。

7. 从离线benchmark到‘平台可持续性’结论缺少现场A/B实验中介。

8. 正文对DR估计与omniscient模拟的细节依赖online appendix，正文自含性有限。

## 一句话套路

本文的ISR套路是：从个人健康管理的现实选择困境出发，用行为健康理论提炼可算法化的三条设计原则，把原则编码为‘TS+理论多样性约束+深度多序列表示’的推荐制品，再用真实平台数据依次以描述性统计、整体benchmark、消融、动态用户专项、JSD、用户改进率和反事实健康仿真，把性能优势逐级上升为可归因设计组件、机制解释与设计知识，最终回扣prescriptive analytics与利益相关者贡献。

## 分析边界

OCR把图1-6均转为images占位符，算法框与公式以LaTeX形式保留；表1-7主体可读但部分表头与显著性格号有OCR噪声。Online Appendix A1-A9未随全文提供，DR估计、omniscient模拟细节、SMART标注流程、超参数扩展和A9.1-A9.4专项实验只能转引正文线索，无法核实。正文无页码，位置只能以section和paragraph首句定位。已据全文逐句核实第一阶段结构；少量内容（如A9 side experiment）无法从正文本身独立验证，已在证据位置标明附录引用。
