# The Decoy Effect and Recommendation Systems：ISR 句段级微观图谱

- 作者：Nasim Mousavi; Panagiotis Adamopoulos; Jesse Bockstedt
- 年份：2023
- DOI：10.1287/isre.2022.1197
- 源文件：28568_2023_the-decoy-effect-and-recommendation-systems.md
- 置信度：0.91

## 核实后的宏观骨架

全文围绕一个可检验的行为学命题展开：经典诱饵效应在传统选择情境中稳健为正，但在推荐系统情境中，尤其是个性化推荐情境，可能因用户对系统可靠性和匹配度的更高期望而发生方向反转。作者用说服理论（来源可信度、内容质量、匹配度）建立假设：非个性化推荐中诱饵仍应提升目标项需求，个性化推荐中诱饵应降低目标项需求并提高无选择选项需求。随后通过一个自制电影推荐平台、632名学生的受试者内随机实验建立主效应，用固定效应logit和multinomial logit确认统计显著性，用感知问卷检验机制，用AMT复制检验外部效度，再用受试者间分析、质量控制实验、前端/后端质量与匹配度分离实验以及诱饵显著性实验排除替代解释并界定边界条件。讨论部分把结果上升为‘推荐集合应整体设计’的可复用知识，并给出非个性化可用、个性化慎用的实践指导。

## 摘要逐句图谱

### 1. Abstract S1

- order：1

- locator：Abstract S1

- paraphrase_cn：本文探索推荐系统中的诱饵效应。

- move_code：CONTEXT

- statement_status：author_inference

- why_here_cn：开门见山，确定全文对象。

- inherits_from_previous_cn：无

- changes_argument_state_cn：把读者注意力集中到推荐系统的诱饵效应。

- sets_up_next_cn：为随后介绍诱饵机制和传统文献建立主题。

- failure_if_removed_cn：摘要缺失主题句，读者不知道文章研究什么。

- evidence_pointer：Abstract opening sentence

### 2. Abstract S2

- order：2

- locator：Abstract S2

- paraphrase_cn：在备选集合中加入诱饵项可通过促进决策来影响其他项目的吸引力。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：用一句话交代诱饵效应的核心机制。

- inherits_from_previous_cn：‘诱饵效应’需要定义。

- changes_argument_state_cn：引入这个现象为什么能影响选择。

- sets_up_next_cn：为‘传统文献普遍验证’提供机制基础。

- failure_if_removed_cn：读者无法理解诱饵为何重要。

- evidence_pointer：Abstract S2

### 3. Abstract S3

- order：3

- locator：Abstract S3

- paraphrase_cn：既有文献证明诱饵效应在传统选择情境中稳健且总体为正。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：建立传统知识基线，为后文的反转张力做准备。

- inherits_from_previous_cn：承接诱饵影响吸引力的一般命题。

- changes_argument_state_cn：让读者认为诱饵是可靠的正向策略。

- sets_up_next_cn：制造‘常规情境没问题，那推荐情境呢’的悬念。

- failure_if_removed_cn：缺少正向基线，后面“个性化中反转”的冲击不复存在。

- evidence_pointer：Abstract S3

### 4. Abstract S4

- order：4

- locator：Abstract S4

- paraphrase_cn：实践者常利用诱饵来推动特定商品的需求。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：说明诱饵不仅是学术现象，也是商业实践。

- inherits_from_previous_cn：承接诱饵效应正向且稳健。

- changes_argument_state_cn：把学术知识转化为商业重要性。

- sets_up_next_cn：让诱饵进入推荐系统的商业场景更自然。

- failure_if_removed_cn：商业实践意义缺失，后文“给管理者提供指引”没有前提。

- evidence_pointer：Abstract S4

### 5. Abstract S5

- order：5

- locator：Abstract S5

- paraphrase_cn：推荐系统也越来越多地被用来向用户呈现商品选择集合。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：把诱饵效应所在的传统选择环境迁移到推荐系统。

- inherits_from_previous_cn：实践者在传统场景用诱饵，现在推荐系统也很普及。

- changes_argument_state_cn：引出二者可能交汇的边界。

- sets_up_next_cn：为“两者都促进决策”的比较做铺垫。

- failure_if_removed_cn：推荐系统这个研究场景没有被引入。

- evidence_pointer：Abstract S5

### 6. Abstract S6

- order：6

- locator：Abstract S6

- paraphrase_cn：推荐系统和诱饵效应都可以作为促进决策的策略。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：点出两者有共同功能，合并在一起可能产生协同或冲突。

- inherits_from_previous_cn：两者分别是决策工具。

- changes_argument_state_cn：为研究二者交叉的必要性铺路。

- sets_up_next_cn：随后立刻指出这个交叉没有被研究。

- failure_if_removed_cn：无法说明为什么要把诱饵放进推荐系统。

- evidence_pointer：Abstract S6

### 7. Abstract S7

- order：7

- locator：Abstract S7

- paraphrase_cn：然而，此前没有研究在推荐系统情境中检验诱饵效应。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：明确指出研究空白。

- inherits_from_previous_cn：前两句表明两者都重要且可能交叉。

- changes_argument_state_cn：从‘值得研究’跳到‘还没有人研究’。

- sets_up_next_cn：为本文的填补动作提供理由。

- failure_if_removed_cn：没有缺口，整个研究失去立足点。

- evidence_pointer：Abstract S7

### 8. Abstract S8

- order：8

- locator：Abstract S8

- paraphrase_cn：诱饵效应与推荐系统结合时可能促进消费者决策并产生正面影响。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：先给一个乐观预期，让读者了解为什么有人看好。

- inherits_from_previous_cn：传统效应正向，所以有人预期推荐中也正向。

- changes_argument_state_cn：建立竞争的乐观分支。

- sets_up_next_cn：马上用“但是”转入风险和负面预期。

- failure_if_removed_cn：乐观分支缺失，不能显现竞争性假说的张力。

- evidence_pointer：Abstract S8

### 9. Abstract S9

- order：9

- locator：Abstract S9

- paraphrase_cn：但推荐情境中消费者对信息可靠性和质量有不同期待。

- move_code：WHY_GAP_MATTERS

- statement_status：theory_claim

- why_here_cn：引入推荐情境的特殊性，作为反转预期的理论依据。

- inherits_from_previous_cn：针对乐观预期提出反例。

- changes_argument_state_cn：把局势从‘应该有用’推向‘可能有害’。

- sets_up_next_cn：为诱饵负面信号解释做铺垫。

- failure_if_removed_cn：没有特殊性解释，推荐情境为何不同无从谈起。

- evidence_pointer：Abstract S9

### 10. Abstract S10

- order：10

- locator：Abstract S10

- paraphrase_cn：因此，作为推荐的诱饵可能发出系统可靠性问题的信号，造成负面效果。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：给出诱饵在推荐中可能有害的具体机制。

- inherits_from_previous_cn：来源可靠性和信息质量期望不同。

- changes_argument_state_cn：形成与乐观分支对照的悲观分支。

- sets_up_next_cn：使实证检验变得必要。

- failure_if_removed_cn：负面机制缺失，结果反转无法被预期。

- evidence_pointer：Abstract S10

### 11. Abstract S11

- order：11

- locator：Abstract S11

- paraphrase_cn：本文用随机受控实验室实验并以说服理论为透镜，证明诱饵效应在推荐系统情境中表现不同。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：预告研究方法和理论立场。

- inherits_from_previous_cn：存在竞争性预期，需要用实验裁定。

- changes_argument_state_cn：从理论推理过渡到实证承诺。

- sets_up_next_cn：为具体结论预告铺路。

- failure_if_removed_cn：读者不知道文章用什么方法获得发现。

- evidence_pointer：Abstract S11

### 12. Abstract S12

- order：12

- locator：Abstract S12

- paraphrase_cn：具体来说，是否推动目标项需求取决于推荐情境。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：用一句话概括情境依赖的核心结论。

- inherits_from_previous_cn：实证方法承诺后给出结果方向。

- changes_argument_state_cn：把两种竞争预期收束为情境依赖结论。

- sets_up_next_cn：进一步展开个性化与非个性化差异。

- failure_if_removed_cn：摘要缺失主要结论。

- evidence_pointer：Abstract S12

### 13. Abstract S13

- order：13

- locator：Abstract S13

- paraphrase_cn：在个性化推荐中，诱饵会减少对目标项的需求，偏离传统诱饵效应。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：报告最反直觉的发现。

- inherits_from_previous_cn：情境依赖结论的具体化。

- changes_argument_state_cn：确立反转效应。

- sets_up_next_cn：与下一句的非个性化形成对照。

- failure_if_removed_cn：核心发现缺失。

- evidence_pointer：Abstract S13

### 14. Abstract S14

- order：14

- locator：Abstract S14

- paraphrase_cn：非个性化推荐中，诱饵增加目标项需求，符合传统诱饵效应。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：提供镜像对照，证明不是诱饵全部无效。

- inherits_from_previous_cn：承接上句对比。

- changes_argument_state_cn：完成两个方向的证据图景。

- sets_up_next_cn：引出机制和稳健性。

- failure_if_removed_cn：没有对照，个性化反转的说服力下降。

- evidence_pointer：Abstract S14

### 15. Abstract S15

- order：15

- locator：Abstract S15

- paraphrase_cn：本文还探索机制并通过多分析和额外实验展示结果稳健。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：强调研究不仅报告系数，还解释原因并加固结论。

- inherits_from_previous_cn：主要结果已公布。

- changes_argument_state_cn：承诺从结果走向机制和边界。

- sets_up_next_cn：为贡献声明提供支持。

- failure_if_removed_cn：研究看起来只有一次性结果。

- evidence_pointer：Abstract S15

### 16. Abstract S16

- order：16

- locator：Abstract S16

- paraphrase_cn：研究发现对推荐系统设计和消费者决策理解有重要启示。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：收束摘要，指向贡献。

- inherits_from_previous_cn：结果和机制已概括。

- changes_argument_state_cn：把结论升华为设计含义。

- sets_up_next_cn：让读者期待引言展开贡献。

- failure_if_removed_cn：摘要没有价值指向。

- evidence_pointer：Abstract final sentence

## 引言逐句图谱

### 1. Introduction P1 S1

- order：1

- locator：Introduction P1 S1

- paraphrase_cn：电商平台目录庞大，消费者面临过多选择。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：从现实痛点切入。

- inherits_from_previous_cn：无

- changes_argument_state_cn：建立选择过载问题。

- sets_up_next_cn：为选择过载的后果提供铺垫。

- failure_if_removed_cn：研究背景缺失。

- evidence_pointer：Introduction paragraph 1 first sentence

### 2. Introduction P1 S2–S3

- order：2

- locator：Introduction P1 S2–S3

- paraphrase_cn：研究和报告显示选择过载带来商业后果，例如54%的顾客放弃购买、70%以上转向竞争者。

- move_code：PRACTICAL_STAKES

- statement_status：fact

- why_here_cn：用数据把问题变成高优先级商业问题。

- inherits_from_previous_cn：选择过载已经提出。

- changes_argument_state_cn：说明问题有真实经济损失。

- sets_up_next_cn：引出推荐系统作为解决方案。

- failure_if_removed_cn：问题重要性的量化证据缺失。

- evidence_pointer：Introduction P1

### 3. Introduction P1 S4–S6

- order：3

- locator：Introduction P1 S4–S6

- paraphrase_cn：推荐系统被用来解决这个问题，能提高决策质量和在线体验；Netflix观看量80%和Amazon购买量35%来自推荐。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：介绍推荐系统的主流解决方案及其普遍性。

- inherits_from_previous_cn：承接需要解决选择过载。

- changes_argument_state_cn：推荐系统被确立为重要且普及。

- sets_up_next_cn：为讨论其局限做铺垫。

- failure_if_removed_cn：推荐系统的重要性没有建立。

- evidence_pointer：Introduction P1

### 4. Introduction P1 S7–S9

- order：4

- locator：Introduction P1 S7–S9

- paraphrase_cn：但推荐系统当前设计也有局限：推荐太多相似的高吸引力选项会导致决策瘫痪，公司正寻找缓解策略。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：从解决方案转为指出方案的缺陷。

- inherits_from_previous_cn：推荐系统虽然有效。

- changes_argument_state_cn：引出一个新的设计问题：推荐集合本身可能造成过载。

- sets_up_next_cn：为诱饵效应作为缓解手段做铺垫。

- failure_if_removed_cn：推荐系统的行为缺陷未被点出，后文无从展开。

- evidence_pointer：Introduction P1 final sentences

### 5. Introduction P2 S1

- order：5

- locator：Introduction P2 S1

- paraphrase_cn：尽管大量研究追求预测精度，但较少关注影响系统说服力和消费者决策的行为因素。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：点出行为视角的空白。

- inherits_from_previous_cn：推荐系统设计局限并不仅靠算法解决。

- changes_argument_state_cn：把问题从算法转向行为。

- sets_up_next_cn：引出本文关注推荐集合构成。

- failure_if_removed_cn：行为研究缺口未建立。

- evidence_pointer：Introduction P2 first sentence

### 6. Introduction P2 S2

- order：6

- locator：Introduction P2 S2

- paraphrase_cn：本文聚焦推荐集合构成这一未充分探索领域，并检验诱饵效应能否缓解推荐中的选择过载。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：点明研究切入点。

- inherits_from_previous_cn：行为因素空白。

- changes_argument_state_cn：把研究问题具体到诱饵效应。

- sets_up_next_cn：为诱饵机制的解释提供空间。

- failure_if_removed_cn：研究对象不清晰。

- evidence_pointer：Introduction P2 second sentence

### 7. Introduction P2 S3–S4

- order：7

- locator：Introduction P2 S3–S4

- paraphrase_cn：诱饵效应通过加入无吸引力项形成对比，在传统选择中可以简化选择并改善顾客结果。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：介绍诱饵效应的机制和已有价值。

- inherits_from_previous_cn：诱饵作为本文核心策略。

- changes_argument_state_cn：确认诱饵在传统环境中有用。

- sets_up_next_cn：为‘推荐情境可能不同’制造对照。

- failure_if_removed_cn：诱饵效应的理论基础缺失。

- evidence_pointer：Introduction P2 middle sentences

### 8. Introduction P2 S5–S6

- order：8

- locator：Introduction P2 S5–S6

- paraphrase_cn：推荐设置具有独特特征可能改变诱饵效应，因此本文在个性化和非个性化推荐中探索诱饵策略。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：说明不能简单照搬传统结论，并预告研究范围。

- inherits_from_previous_cn：传统诱饵效果已建立。

- changes_argument_state_cn：引入情境差异，缩小到两种推荐类型。

- sets_up_next_cn：为后面两个研究问题铺路。

- failure_if_removed_cn：诱饵效应独特性的论述缺失。

- evidence_pointer：Introduction P2 final sentences

### 9. Introduction P3 S1–S2

- order：9

- locator：Introduction P3 S1–S2

- paraphrase_cn：推荐系统旨在让购物更愉快并降低搜索成本，但这要求理解影响消费者行为的因素。

- move_code：CONTEXT

- statement_status：fact

- why_here_cn：构建研究动机的基础。

- inherits_from_previous_cn：推荐系统的目标是改善选择体验。

- changes_argument_state_cn：把目标与行为理解绑定。

- sets_up_next_cn：为消费者非理性行为讨论做铺垫。

- failure_if_removed_cn：研究动机缺乏目标锚点。

- evidence_pointer：Section 1.1 P1

### 10. Introduction P3 S3–S4

- order：10

- locator：Introduction P3 S3–S4

- paraphrase_cn：理论上和实践上都已知消费者并非理性效用最大化，选择集合构成、呈现格式和选项关系等情境因素会影响决策。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：为行为因素进入推荐系统设计提供依据。

- inherits_from_previous_cn：需要理解行为因素。

- changes_argument_state_cn：把非理性行为和情境因素确立为真实存在。

- sets_up_next_cn：指出推荐系统算法忽视了这些因素。

- failure_if_removed_cn：行为视角的合法性未确立。

- evidence_pointer：Section 1.1 P1

### 11. Introduction P4 S1–S3

- order：11

- locator：Introduction P4 S1–S3

- paraphrase_cn：但推荐系统设计对消费者心理关注不足；算法基于理性行为最大化期望效用，不考虑理性边界，因此某些情境下无法满足用户。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：把上一段的情境因素问题落到推荐系统算法上。

- inherits_from_previous_cn：情境因素重要。

- changes_argument_state_cn：界定推荐系统设计的行为缺陷。

- sets_up_next_cn：引出实践者开始关注认知心理。

- failure_if_removed_cn：算法缺陷陈述缺失，研究动机减弱。

- evidence_pointer：Section 1.1 P2

### 12. Introduction P4 S4–S6

- order：12

- locator：Introduction P4 S4–S6

- paraphrase_cn：实践者讨论需要研究认知心理学；诱饵效应因传统选择中的促销作用引起注意，并被认为对推荐设置有益。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：把诱饵效应带入推荐系统设计议程。

- inherits_from_previous_cn：需要研究认知因素。

- changes_argument_state_cn：诱饵从营销手段变成推荐系统候选策略。

- sets_up_next_cn：为下一段描述推荐系统实际由高吸引力项目组成的困境。

- failure_if_removed_cn：诱饵为何进入推荐设计缺乏动机。

- evidence_pointer：Section 1.1 P2

### 13. Introduction P5 S1–S3

- order：13

- locator：Introduction P5 S1–S3

- paraphrase_cn：主流推荐系统如Netflix和Amazon通常提供高质量或高匹配项目，但这可能造成过多好选项、决策瘫痪和过度专门化，反而让决策更复杂。

- move_code：LIMITATION

- statement_status：author_inference

- why_here_cn：描述推荐系统当前策略的反效果。

- inherits_from_previous_cn：诱饵可能被用来缓解这一问题。

- changes_argument_state_cn：进一步强化推荐集合构成问题的严重性。

- sets_up_next_cn：引出加入诱饵作为对比手段。

- failure_if_removed_cn：推荐集合为何需要重新设计缺少依据。

- evidence_pointer：Section 1.1 P3

### 14. Introduction P5 S4–S5

- order：14

- locator：Introduction P5 S4–S5

- paraphrase_cn：在推荐集合中加入诱饵可以通过制造清晰对比将注意力引向目标项；但尚无行业报告或研究确凿证明其有效。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：提出诱饵的可能用途，同时承认证据缺失。

- inherits_from_previous_cn：推荐系统需要对比手段。

- changes_argument_state_cn：诱饵策略处于‘有讨论但无证据’状态。

- sets_up_next_cn：为下一段反转预期和本研究动机做铺垫。

- failure_if_removed_cn：诱饵在推荐中的研究空白不明确。

- evidence_pointer：Section 1.1 P3 final sentences

### 15. Introduction P6 S1–S3

- order：15

- locator：Introduction P6 S1–S3

- paraphrase_cn：诱饵在传统选择中有效，但推荐情境中服务质量期望不同，用户对信息质量更敏感，诱饵可能降低感知质量和满意度。

- move_code：WHY_GAP_MATTERS

- statement_status：theory_claim

- why_here_cn：给出诱饵可能有害的理论理由。

- inherits_from_previous_cn：诱饵有效但有证据空白。

- changes_argument_state_cn：首次引入推荐情境的负面机制。

- sets_up_next_cn：为研究提供管理指导的动机。

- failure_if_removed_cn：诱饵可能有害的预判缺失。

- evidence_pointer：Section 1.1 P4

### 16. Introduction P6 S4–S5

- order：16

- locator：Introduction P6 S4–S5

- paraphrase_cn：尽管有正效应证据，推荐系统的独特特征可能使诱饵有害；本文要回答这个问题并给管理者提供指导。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：把动机收拢到本文任务。

- inherits_from_previous_cn：诱饵可能有害。

- changes_argument_state_cn：研究目标明确为给管理者提供诱饵使用指导。

- sets_up_next_cn：为1.2节研究问题做铺垫。

- failure_if_removed_cn：研究导向缺失。

- evidence_pointer：Section 1.1 P4 final

### 17. Introduction P7 S1–S4

- order：17

- locator：Introduction P7 S1–S4

- paraphrase_cn：相似且高吸引力的推荐项会让决策复杂化、降低购买和满意度；传统列表中诱饵能创造清晰对比；学者因而推测推荐中也有效，但尚未检验消费者如何反应。

- move_code：GAP

- statement_status：prior_literature

- why_here_cn：重建研究空白并给出预测性期望。

- inherits_from_previous_cn：推荐集合造成决策困难。

- changes_argument_state_cn：把诱饵的潜在价值与实证空白并置。

- sets_up_next_cn：引出第一个研究问题。

- failure_if_removed_cn：研究问题没有知识背景。

- evidence_pointer：Section 1.2 P1

### 18. Introduction P7 S5

- order：18

- locator：Introduction P7 S5

- paraphrase_cn：因为推荐情境中的行为可能不同，本文研究问题是：诱饵效应如何改变推荐系统中项目的需求？

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：正式提出第一个研究问题。

- inherits_from_previous_cn：消费者对诱饵反应未知。

- changes_argument_state_cn：把一般问题固化为核心研究问题。

- sets_up_next_cn：为后续可能结果和第二个问题铺路。

- failure_if_removed_cn：核心研究问题缺失。

- evidence_pointer：Introduction 1.2 RQ1

### 19. Introduction P8 S1–S3

- order：19

- locator：Introduction P8 S1–S3

- paraphrase_cn：回答此问题将帮助实践者和设计者判断诱饵是否创造足够价值；诱饵可能通过简化决策提升满意度，也可能延续传统效应推动特定项目需求。

- move_code：WHY_GAP_MATTERS

- statement_status：author_inference

- why_here_cn：说明研究问题的应用价值并展示积极分支。

- inherits_from_previous_cn：第一个研究问题已提出。

- changes_argument_state_cn：明确受益者并勾勒正向预期。

- sets_up_next_cn：紧接着给出消极分支。

- failure_if_removed_cn：研究意义不够明确。

- evidence_pointer：Introduction 1.2 P2

### 20. Introduction P8 S4–S7

- order：20

- locator：Introduction P8 S4–S7

- paraphrase_cn：但诱饵也可能因为推荐情境独特特征适得其反，用户期望高质高匹配信息；这导致与预测不同甚至竞争性的行为，两分支都理论上成立，构成实证机会。

- move_code：WHY_GAP_MATTERS

- statement_status：theory_claim

- why_here_cn：建立竞争性预期框架。

- inherits_from_previous_cn：积极分支已给出。

- changes_argument_state_cn：从单一预期转为竞争假说。

- sets_up_next_cn：为第二个研究问题做铺垫。

- failure_if_removed_cn：反转效应缺乏理论前提。

- evidence_pointer：Introduction 1.2 P2

### 21. Introduction P9 S1–S2

- order：21

- locator：Introduction P9 S1–S2

- paraphrase_cn：实践中两种最常见推荐分别是个性化推荐（基于个人偏好高匹配）和非个性化推荐（基于平均评分的高质量项目）；研究显示用户对两种推荐的期望和依赖可能不同。

- move_code：RQ_OR_OBJECTIVE

- statement_status：prior_literature

- why_here_cn：引入第二个研究问题所需的情境定义。

- inherits_from_previous_cn：推荐情境存在差异。

- changes_argument_state_cn：把情境差异具体化为两种推荐类型。

- sets_up_next_cn：为第二个研究问题提供分类基础。

- failure_if_removed_cn：个性化与非个性化的区分缺乏定义。

- evidence_pointer：Introduction 1.2 P3

### 22. Introduction P9 S3–S4

- order：22

- locator：Introduction P9 S3–S4

- paraphrase_cn：因此用户可能对这两种情境中的诱饵反应不同；本文第二个问题是诱饵效应在个性化与非个性化推荐中是否表现不同，答案将指导管理者是否需要在两种情境采用不同策略。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：正式提出第二个研究问题。

- inherits_from_previous_cn：用户对两种推荐期望不同。

- changes_argument_state_cn：研究范围包含情境比较。

- sets_up_next_cn：为四条件实验设计做铺垫。

- failure_if_removed_cn：情境比较这一核心问题缺失。

- evidence_pointer：Introduction 1.2 RQ2

### 23. Introduction P10 S1–S3

- order：23

- locator：Introduction P10 S1–S3

- paraphrase_cn：本文用最先进的电影推荐系统进行随机受控选择实验，平台同时提供个性化和非个性化推荐，比较四种条件（个性化与是否有诱饵交叉、非个性化与是否有诱饵交叉）。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：预告实验方法。

- inherits_from_previous_cn：两个研究问题已提出。

- changes_argument_state_cn：从问题转向研究方法。

- sets_up_next_cn：为结果预告铺路。

- failure_if_removed_cn：实证策略的承诺缺失。

- evidence_pointer：Introduction 1.2 P4

### 24. Introduction P10 S4–S7

- order：24

- locator：Introduction P10 S4–S7

- paraphrase_cn：结果显示诱饵效应的性质在个性化和非个性化情境中显著不同：非个性化中仍为传统正向，个性化中偏离传统，诱饵增加无选择选项并降低目标项需求。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：在引言末尾预览主要发现。

- inherits_from_previous_cn：实验方法已介绍。

- changes_argument_state_cn：确立核心结果。

- sets_up_next_cn：为机制解释和贡献声明提供结论。

- failure_if_removed_cn：读者不知研究发现了什么。

- evidence_pointer：Introduction 1.2 P4

### 25. Introduction P10 S8–S9

- order：25

- locator：Introduction P10 S8–S9

- paraphrase_cn：作者认为这些发现源于用户对个性化系统的期望：用户期待高匹配、高可靠来源的推荐，诱饵会负面改变他们对系统的行为。

- move_code：MECHANISM

- statement_status：author_inference

- why_here_cn：给出结果的机制性解释。

- inherits_from_previous_cn：结果已报告。

- changes_argument_state_cn：从行为结果转向期望机制。

- sets_up_next_cn：为后续机制测试和讨论铺路。

- failure_if_removed_cn：结果缺乏可解释机制，贡献降格为一次性发现。

- evidence_pointer：Introduction 1.2 P4

### 26. Introduction P10 S10

- order：26

- locator：Introduction P10 S10

- paraphrase_cn：作者通过多个附加实验展示结果稳健。

- move_code：STUDY_OVERVIEW

- statement_status：method_decision

- why_here_cn：预告稳健性证据。

- inherits_from_previous_cn：核心结果和机制已报告。

- changes_argument_state_cn：提升结论可靠性预期。

- sets_up_next_cn：为贡献声明铺路。

- failure_if_removed_cn：稳健性承诺缺失。

- evidence_pointer：Introduction 1.2 P4 final sentence

### 27. Introduction P11 S1–S4

- order：27

- locator：Introduction P11 S1–S4

- paraphrase_cn：本文回应学者在推荐系统中探索认知偏差的呼吁，扩展个性化和推荐系统的情境因素知识，作为首次研究证明诱饵效应在两种情境中影响不同，并拓宽对诱饵效应本身的理解。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：在引言中明确贡献。

- inherits_from_previous_cn：结果和机制已汇报。

- changes_argument_state_cn：把发现升华为文献贡献。

- sets_up_next_cn：为管理启示和总结做准备。

- failure_if_removed_cn：贡献声明缺失，论文价值不清晰。

- evidence_pointer：Introduction 1.2 P5

### 28. Introduction P11 S5–S7

- order：28

- locator：Introduction P11 S5–S7

- paraphrase_cn：结果回应实践争议：非个性化情境可用诱饵，个性化情境应谨慎；同时强调区分推荐情境的重要性。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出实践导向的贡献。

- inherits_from_previous_cn：文献贡献已声明。

- changes_argument_state_cn：把行为发现转成可操作建议。

- sets_up_next_cn：为全文结构预告做铺垫。

- failure_if_removed_cn：管理实践价值缺失。

- evidence_pointer：Introduction 1.2 P5

### 29. Introduction P12 S1–S5

- order：29

- locator：Introduction P12 S1–S5

- paraphrase_cn：论文结构：先是理论背景和假设，然后是研究方法和结果，接着是机制和稳健性，最后讨论含义。

- move_code：SIGNPOST

- statement_status：method_decision

- why_here_cn：告知读者文章结构。

- inherits_from_previous_cn：贡献和内容已介绍完。

- changes_argument_state_cn：给出阅读地图。

- sets_up_next_cn：让读者预期后面章节任务。

- failure_if_removed_cn：文章结构不清晰。

- evidence_pointer：Introduction final paragraph

## 引言逐段图谱

### 1. Introduction P1

- order：1

- locator：Introduction P1

- opening_move_cn：以电商选择过载的现实场景开篇。

- development_move_cn：用统计数据和Netflix/Amazon采用率说明问题严重性和推荐系统的普及。

- pivot_move_cn：转折到推荐系统虽然有效但存在推荐相似高吸引力项导致决策瘫痪的局限。

- closing_move_cn：以企业寻找更说服性推荐策略收束，为诱饵效应登场制造需求。

- paragraph_job_cn：建立现实与商业重要性，并埋下推荐系统设计缺陷的伏笔。

### 2. Introduction P2

- order：2

- locator：Introduction P2

- opening_move_cn：从算法精度研究转向行为因素空白。

- development_move_cn：介绍诱饵效应的传统价值。

- pivot_move_cn：转折到推荐设置具有独特特征可能改变诱饵效应。

- closing_move_cn：把研究范围缩小到个性化和非个性化两种推荐。

- paragraph_job_cn：将一般行为空白具体化为推荐集合构成中的诱饵效应研究。

### 3. Introduction 1.1 P1

- order：3

- locator：Introduction 1.1 P1

- opening_move_cn：以推荐系统的目标开始。

- development_move_cn：论证理解行为因素的必要性，并列举非理性消费和情境因素文献。

- pivot_move_cn：尚未转折，主要是铺垫。

- closing_move_cn：以情境因素影响决策收束，为算法缺陷做铺垫。

- paragraph_job_cn：建立行为视角在推荐系统研究中的合法性。

### 4. Introduction 1.1 P2

- order：4

- locator：Introduction 1.1 P2

- opening_move_cn：指出推荐系统对消费者心理关注不足。

- development_move_cn：批评算法基于理性假设并呼吁实践者关注认知心理。

- pivot_move_cn：引入诱饵效应作为吸引注意的重要行为因素。

- closing_move_cn：指出诱饵效应主要被认为在推荐中有利。

- paragraph_job_cn：把诱饵效应从营销文献带入推荐系统研究议程。

### 5. Introduction 1.1 P3

- order：5

- locator：Introduction 1.1 P3

- opening_move_cn：描述主流推荐系统由高质量高匹配项目组成。

- development_move_cn：说明高相似项目造成决策瘫痪和过度专门化。

- pivot_move_cn：转折到诱饵可以为相似项目制造对比。

- closing_move_cn：以‘仍无确凿证据’点出空白。

- paragraph_job_cn：指出现有推荐集合构成需要改进，而诱饵是候选方案但无证据。

### 6. Introduction 1.1 P4

- order：6

- locator：Introduction 1.1 P4

- opening_move_cn：反转预期：诱饵在推荐情境中可能无效。

- development_move_cn：论述用户对信息质量和可靠性的更高敏感度。

- pivot_move_cn：承认传统正效应证据存在，但强调推荐系统特性可能使诱饵有害。

- closing_move_cn：点明本文要为管理者提供诱饵使用指导。

- paragraph_job_cn：提出诱饵可能有害的竞争性预期，并确立研究的管理目标。

### 7. Introduction 1.2 P1

- order：7

- locator：Introduction 1.2 P1

- opening_move_cn：从推荐列表类似效用导致决策复杂切入。

- development_move_cn：传统列表中诱饵可创造对比并提高目标项吸引力；学者推测推荐中也有用。

- pivot_move_cn：转折到消费者在真实推荐设置中如何反应尚无研究。

- closing_move_cn：提出第一个研究问题。

- paragraph_job_cn：搭建研究问题一：诱饵效应如何影响推荐系统中的需求。

### 8. Introduction 1.2 P2

- order：8

- locator：Introduction 1.2 P2

- opening_move_cn：回答第一个问题的价值。

- development_move_cn：展开诱饵的积极和消极两种可能结果。

- pivot_move_cn：既可能推动需求也可能因期望问题适得其反。

- closing_move_cn：两种情形都成立，构成实证机会。

- paragraph_job_cn：确定第一个研究问题的重要性和竞争性预期。

### 9. Introduction 1.2 P3

- order：9

- locator：Introduction 1.2 P3

- opening_move_cn：区分实践中两种最常见的推荐形式。

- development_move_cn：文献显示用户对个性化和非个性化的期望与依赖不同。

- pivot_move_cn：因此他们可能对诱饵反应不同。

- closing_move_cn：提出第二个研究问题并说明管理价值。

- paragraph_job_cn：搭建研究问题二：诱饵效应在个性化和非个性化中是否不同。

### 10. Introduction 1.2 P4

- order：10

- locator：Introduction 1.2 P4

- opening_move_cn：预告随机受控选择实验。

- development_move_cn：描述四条件设计和主要结果。

- pivot_move_cn：结果与预期在个性化中反转。

- closing_move_cn：用用户期望解释机制并宣称稳健性。

- paragraph_job_cn：向读者预告方法、核心发现和机制解释。

### 11. Introduction 1.2 P5

- order：11

- locator：Introduction 1.2 P5

- opening_move_cn：声明回应学者呼吁并贡献文献。

- development_move_cn：列出首次研究、情境因素扩展、诱饵理论扩展和实践争议回应。

- pivot_move_cn：强调非个性化可用、个性化需谨慎。

- closing_move_cn：强调区分推荐情境的重要性。

- paragraph_job_cn：给出论文的文献贡献和实践启示。

### 12. Introduction 1.2 P6

- order：12

- locator：Introduction 1.2 P6

- opening_move_cn：用‘论文结构如下’开启。

- development_move_cn：按顺序介绍理论背景、假设、方法结果、机制稳健性、讨论。

- pivot_move_cn：无转折，纯路标。

- closing_move_cn：以讨论含义收束。

- paragraph_job_cn：提供全文结构地图。

## 理论到设计逐句图谱

### 1. Section 2.1 P1 S1–S3

- order：1

- locator：Section 2.1 P1 S1–S3

- paraphrase_cn：判断通常是相对的，同一选项在不同参照集中吸引力不同。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：为诱饵效应提供相对判断基础。

- inherits_from_previous_cn：引言已提到诱饵。

- changes_argument_state_cn：把诱饵效应放回情境判断理论。

- sets_up_next_cn：引出选择架构与认知有限性。

- failure_if_removed_cn：诱饵效应的心理学基础缺失。

- evidence_pointer：Section 2.1 first paragraphs

### 2. Section 2.1 P2 S1–S3

- order：2

- locator：Section 2.1 P2 S1–S3

- paraphrase_cn：选择架构展示不同呈现方式如何影响决策，因个体认知容量有限而依赖启发式。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：把诱饵效应放进设计选择架构的框架。

- inherits_from_previous_cn：相对判断和情境影响。

- changes_argument_state_cn：诱饵不仅是消费者现象，也是设计工具。

- sets_up_next_cn：为诱饵进入推荐系统设计做铺垫。

- failure_if_removed_cn：设计含义缺失，诱饵仅停留在行为层面。

- evidence_pointer：Section 2.1 P2

### 3. Section 2.1 P3 S1–S4

- order：3

- locator：Section 2.1 P3 S1–S4

- paraphrase_cn：诱饵效应违反IIA假设；Huber等首次用汽车、餐厅等多类产品证明加入非对称支配诱饵会增加目标项相对选择概率。

- move_code：THEORY_PROPOSITION

- statement_status：prior_literature

- why_here_cn：正式给出诱饵效应的理论定义和证据来源。

- inherits_from_previous_cn：启发式和选择架构。

- changes_argument_state_cn：诱饵效应被定义为可检验的理论现象。

- sets_up_next_cn：为机制解释和设计操作提供依据。

- failure_if_removed_cn：诱饵效应的正式定义缺失。

- evidence_pointer：Section 2.1 P3

### 4. Section 2.1 P4 S1–S3

- order：4

- locator：Section 2.1 P4 S1–S3

- paraphrase_cn：用两个属性商品的例子说明，诱饵与目标项在某一维度可比而更差，使目标项成为清晰赢家。

- move_code：MECHANISM

- statement_status：prior_literature

- why_here_cn：用直观例子展示非对称支配。

- inherits_from_previous_cn：诱饵效应定义。

- changes_argument_state_cn：阐明诱饵如何改变注意力。

- sets_up_next_cn：为认知负荷机制提供具体场景。

- failure_if_removed_cn：读者无法直观理解诱饵操作。

- evidence_pointer：Section 2.1 P4

### 5. Section 2.1 P5 S1–S3

- order：5

- locator：Section 2.1 P5 S1–S3

- paraphrase_cn：诱饵效应的机制是认知负荷：比较和排序多个选项消耗认知资源；诱饵通过制造清晰对比简化选择，提高满意度和信心。

- move_code：MECHANISM

- statement_status：prior_literature

- why_here_cn：解释诱饵为什么有效。

- inherits_from_previous_cn：诱饵制造清晰赢家。

- changes_argument_state_cn：把诱饵效应与决策难度联系起来。

- sets_up_next_cn：为推荐情境中如何构造诱饵提供依据。

- failure_if_removed_cn：诱饵效应的心理机制不清。

- evidence_pointer：Section 2.1 P5

### 6. Section 2.1 P6 S1–S4

- order：6

- locator：Section 2.1 P6 S1–S4

- paraphrase_cn：诱饵应设计得与目标项易于比较但与竞争项比较弱，目标项获得更多正权重。

- move_code：THEORY_PROPOSITION

- statement_status：prior_literature

- why_here_cn：给出诱饵的设计原则。

- inherits_from_previous_cn：认知负荷机制。

- changes_argument_state_cn：诱饵构造规则明确。

- sets_up_next_cn：为4.2.2节诱饵设计（同类型、低评分、紧邻目标）提供依据。

- failure_if_removed_cn：实验中的诱饵设计没有理论依据。

- evidence_pointer：Section 2.1 P6

### 7. Section 2.1 P7 S1–S2

- order：7

- locator：Section 2.1 P7 S1–S2

- paraphrase_cn：诱饵效应在多种情境中稳健，但所有研究都在常规选择设置，没有研究在推荐设置中考察推荐者提供诱饵。

- move_code：GAP

- statement_status：author_inference

- why_here_cn：在文献综述内锁定空白。

- inherits_from_previous_cn：诱饵效应的稳健性。

- changes_argument_state_cn：把综述收束到本文贡献点。

- sets_up_next_cn：为推荐系统情境因素综述做过渡。

- failure_if_removed_cn：文献综述与本文贡献脱节。

- evidence_pointer：Section 2.1 final paragraph

### 8. Section 2.2 P1 S1–S3

- order：8

- locator：Section 2.2 P1 S1–S3

- paraphrase_cn：Economist订阅实验是最著名诱饵案例，纯打印版作为诱饵提升了打印加在线版的相对吸引力。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：用经典案例强化诱饵的生态效度。

- inherits_from_previous_cn：诱饵效应稳健性。

- changes_argument_state_cn：证明诱饵在真实营销场景中有效。

- sets_up_next_cn：为推荐情境的引入做对比。

- failure_if_removed_cn：诱饵效应的知名例证缺失。

- evidence_pointer：Section 2.2 P1

### 9. Section 2.2 P2 S1–S3

- order：9

- locator：Section 2.2 P2 S1–S3

- paraphrase_cn：推荐系统已成为内容消费关键驱动力，除了算法设计还需要关注行为因素。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：把推荐系统研究语境翻译成行为视角。

- inherits_from_previous_cn：Economist实验后推荐系统普及。

- changes_argument_state_cn：推荐系统的有效性离不开行为因素。

- sets_up_next_cn：为情境因素综述铺路。

- failure_if_removed_cn：推荐系统行为研究的必要性缺失。

- evidence_pointer：Section 2.2 P2

### 10. Section 2.2 P3 S1–S4

- order：10

- locator：Section 2.2 P3 S1–S4

- paraphrase_cn：由于认知容量有限，呈现格式、不熟悉产品伴随熟悉产品、推荐数量、解释类型和情绪等情境因素都会影响推荐系统效果。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：建立推荐系统情境因素研究现状。

- inherits_from_previous_cn：推荐系统需要行为视角。

- changes_argument_state_cn：推荐集合构成是一个可嵌入的情境因素。

- sets_up_next_cn：为本文把诱饵作为新情境因素做铺垫。

- failure_if_removed_cn：本文与既有情境因素研究缺乏衔接。

- evidence_pointer：Section 2.2 P3

### 11. Section 2.2 P4 S1–S4

- order：11

- locator：Section 2.2 P4 S1–S4

- paraphrase_cn：本文扩展推荐系统情境因素研究，聚焦诱饵在推荐集合中的作用；据作者所知是首篇在推荐设置中检验诱饵效应的研究。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：在文献综述末尾声明新颖性。

- inherits_from_previous_cn：情境因素研究现状。

- changes_argument_state_cn：把诱饵效应定位为本文切入点。

- sets_up_next_cn：自然过渡到理论框架与假设。

- failure_if_removed_cn：综述没有锁定本文贡献。

- evidence_pointer：Section 2.2 final paragraph

### 12. Section 3 P1 S1–S4

- order：12

- locator：Section 3 P1 S1–S4

- paraphrase_cn：诱饵和推荐系统都促进决策，问题在于两种策略结合是否产生协同；推荐系统呈现选择集，因此诱饵可能适用，但推荐情境可能改变效应。

- move_code：RQ_OR_OBJECTIVE

- statement_status：author_inference

- why_here_cn：从综述过渡到理论问题。

- inherits_from_previous_cn：诱饵和推荐系统的两条文献流。

- changes_argument_state_cn：提出本文理论问题。

- sets_up_next_cn：引入说服理论作为透镜。

- failure_if_removed_cn：理论框架没有明确问题。

- evidence_pointer：Section 3 opening

### 13. Section 3 P2 S1–S2

- order：13

- locator：Section 3 P2 S1–S2

- paraphrase_cn：作者用说服理论分析诱饵与推荐系统的交互，因为推荐系统作为传播渠道需要提供有说服力的内容。

- move_code：THEORY_INTRO

- statement_status：theory_claim

- why_here_cn：选择理论透镜。

- inherits_from_previous_cn：需要解释推荐情境差异。

- changes_argument_state_cn：说服理论进入论证。

- sets_up_next_cn：引出三个说服因素。

- failure_if_removed_cn：后续假设没有理论支撑。

- evidence_pointer：Section 3 P2

### 14. Section 3 P2 S3–S4

- order：14

- locator：Section 3 P2 S3–S4

- paraphrase_cn：说服理论认为影响说服的因素是来源可信度、内容质量和用户匹配度；可靠来源增加信息接受。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：列出理论关键构念。

- inherits_from_previous_cn：说服理论引介。

- changes_argument_state_cn：建立分析框架的三个维度。

- sets_up_next_cn：为个性化系统可靠性期望做铺垫。

- failure_if_removed_cn：分析构念缺失。

- evidence_pointer：Section 3 P2

### 15. Section 3 P3 S1–S3

- order：15

- locator：Section 3 P3 S1–S3

- paraphrase_cn：高质量、高匹配内容更具说服力；诱饵可能降低来源可靠性和内容说服力，类似建议采纳文献中低质量建议会被折价。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把诱饵与低说服信号联系起来。

- inherits_from_previous_cn：三个说服因素。

- changes_argument_state_cn：诱饵被概念化为低质量/低匹配内容。

- sets_up_next_cn：为个性化情境中诱饵的负面效应做铺垫。

- failure_if_removed_cn：诱饵为何降低可靠性缺少理论来源。

- evidence_pointer：Section 3 P3

### 16. Section 3 P4 S1–S5

- order：16

- locator：Section 3 P4 S1–S5

- paraphrase_cn：非个性化推荐重复其他消费者的质量信息，质量期望来源于大众评分；个性化推荐则承载系统对个人偏好的匹配承诺。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：区分两种推荐的信息本质。

- inherits_from_previous_cn：说服因素矩阵。

- changes_argument_state_cn：个性化和非个性化在用户期望上被正式分开。

- sets_up_next_cn：为H1、H2提供机制桥梁。

- failure_if_removed_cn：情境差异缺乏结构性解释。

- evidence_pointer：Section 3 P4

### 17. Section 3 P5 S1–S3

- order：17

- locator：Section 3 P5 S1–S3

- paraphrase_cn：当内容与个人相关性强时，用户渴望更准确匹配的信息；从专家来源看到低匹配内容会导致负面期望不一致和回旋镖效应。

- move_code：THEORY_PROPOSITION

- statement_status：theory_claim

- why_here_cn：说明个人相关性强化对信息质量的敏感性。

- inherits_from_previous_cn：个性化和非个性化的期望差异。

- changes_argument_state_cn：个性化中的低匹配诱饵导致反说服。

- sets_up_next_cn：直接支撑H2。

- failure_if_removed_cn：反转预测缺乏机制。

- evidence_pointer：Section 3 P5

### 18. Section 3 P6 S1–S5

- order：18

- locator：Section 3 P6 S1–S5

- paraphrase_cn：在个性化情境中，系统可靠性对信息接受更关键；低匹配诱饵会被视为系统不了解用户或操纵用户，损害信任和态度。

- move_code：MECHANISM

- statement_status：theory_claim

- why_here_cn：把理论命题转化为个性化情境的具体机制。

- inherits_from_previous_cn：个人相关性高时用户更敏感。

- changes_argument_state_cn：明确低匹配诱饵是可靠性信号。

- sets_up_next_cn：为H1、H2的表述做最后铺垫。

- failure_if_removed_cn：机制链不完整。

- evidence_pointer：Section 3 P6

### 19. Section 3 Hypothesis 1

- order：19

- locator：Section 3 Hypothesis 1

- paraphrase_cn：H1：在非个性化推荐设置中，诱饵效应如传统选择情境一样推动目标项需求。

- move_code：HYPOTHESIS_OR_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把非个性化机制转化为可检验假设。

- inherits_from_previous_cn：非个性化重复他人质量信息，期望较低。

- changes_argument_state_cn：给出第一个明确预测。

- sets_up_next_cn：为H2对照做准备。

- failure_if_removed_cn：非个性化预期缺少正式预测。

- evidence_pointer：Section 3 H1

### 20. Section 3 Hypothesis 2

- order：20

- locator：Section 3 Hypothesis 2

- paraphrase_cn：H2：在个性化推荐设置中，诱饵效应推动需求远离目标项。

- move_code：HYPOTHESIS_OR_PROPOSITION

- statement_status：theory_claim

- why_here_cn：把个性化机制转化为可检验假设。

- inherits_from_previous_cn：个性化中用户对可靠性和匹配敏感。

- changes_argument_state_cn：给出方向反转的预测。

- sets_up_next_cn：为四条件实验设计提供检验对象。

- failure_if_removed_cn：核心研究预测缺失。

- evidence_pointer：Section 3 H2

## 制品设计理由逐句图谱

### 1. Section 4.1 S1–S4

- order：1

- locator：Section 4.1 S1–S4

- paraphrase_cn：用MovieTweetings数据库提供真实电影评分，并限定2000-2018年电影，为推荐生成和用户熟悉度提供素材。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：需要一个现实且可控制的数据基础。

- inherits_from_previous_cn：需要实验平台。

- changes_argument_state_cn：平台数据来源确定。

- sets_up_next_cn：为种子化推荐系统做准备。

- failure_if_removed_cn：实验平台缺乏真实推荐数据。

- evidence_pointer：Section 4.1

### 2. Section 4.1 S5–S8

- order：2

- locator：Section 4.1 S5–S8

- paraphrase_cn：要求用户先对100部热门电影中至少20部评分，目的是种子化个性化推荐系统并让用户熟悉平台；选择热门电影保证用户能准确评分。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：个性化推荐需要用户偏好输入，同时种子化标准化实验流程。

- inherits_from_previous_cn：数据库选定。

- changes_argument_state_cn：用户偏好被内置到平台。

- sets_up_next_cn：为SVD个性化设置提供输入。

- failure_if_removed_cn：个性化算法无法运行。

- evidence_pointer：Section 4.1 rating task

### 3. Section 4.2 S1–S4

- order：3

- locator：Section 4.2 S1–S4

- paraphrase_cn：使用受试者内设计，四条件中个性化和非个性化各自绑定出现；随机化但保证两个个性化条件和两个非个性化条件相邻。

- move_code：DESIGN_FEATURE

- statement_status：method_decision

- why_here_cn：在受试者内比较中让用户明确区分两类推荐，减少混淆。

- inherits_from_previous_cn：四条件需要比较。

- changes_argument_state_cn：确定实验设计的核心结构。

- sets_up_next_cn：为个性化/非个性化操纵清晰化打基础。

- failure_if_removed_cn：用户可能混淆推荐类型，操纵失效。

- evidence_pointer：Section 4.2

### 4. Section 4.2 S5–S6

- order：4

- locator：Section 4.2 S5–S6

- paraphrase_cn：在条件开始前向用户展示解释文本，分别说明将看到按偏好选择的电影或大众观看的电影，以强化操纵。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：让用户在认知上区分个性化和非个性化。

- inherits_from_previous_cn：四条件结构确定。

- changes_argument_state_cn：增加操纵强度。

- sets_up_next_cn：为后面操纵检验提供过程基础。

- failure_if_removed_cn：个性化感知可能不够强。

- evidence_pointer：Section 4.2 intro texts

### 5. Section 4.2.1 S1–S4

- order：5

- locator：Section 4.2.1 S1–S4

- paraphrase_cn：个性化条件用SVD协同过滤的预测评分，非个性化条件用聚合平均评分和流行度；SVD因测试样本预测误差最低而入选。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：需要两种操作性不同的推荐生成方式。

- inherits_from_previous_cn：平台需要提供两种推荐类型。

- changes_argument_state_cn：个性化和非个性化的算法差异确定。

- sets_up_next_cn：为诱饵低预测分/低平均分的定义打基础。

- failure_if_removed_cn：两种条件可能没有真正的算法差异。

- evidence_pointer：Section 4.2.1

### 6. Section 4.2.1 S5–S8

- order：6

- locator：Section 4.2.1 S5–S8

- paraphrase_cn：排除用户已经评分的电影，保证每条件展示不同电影且不同用户看到不同集合，以避免记忆和重复效应。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：保护条件间的独立性和内部效度。

- inherits_from_previous_cn：推荐生成方式确定。

- changes_argument_state_cn：降低跨条件污染。

- sets_up_next_cn：保证后面行为差异可归于处理。

- failure_if_removed_cn：条件间可能互相污染，因果推断不可靠。

- evidence_pointer：Section 4.2.1

### 7. Section 4.2.2 S1–S2

- order：7

- locator：Section 4.2.2 S1–S2

- paraphrase_cn：诱饵从与列表第一项（目标项）相同类型的电影中随机选择，在个性化中低预测分、非个性化中低平均分，从而满足非对称支配。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：让诱饵与目标可比、与竞争项不可比，符合理论要求。

- inherits_from_previous_cn：2.1节诱饵设计原则。

- changes_argument_state_cn：把理论设计规则转化为具体操作。

- sets_up_next_cn：为诱饵显著性解释打基础。

- failure_if_removed_cn：诱饵无法形成非对称支配。

- evidence_pointer：Section 4.2.2

### 8. Section 4.2.2 S3–S4

- order：8

- locator：Section 4.2.2 S3–S4

- paraphrase_cn：作者刻意让评分显著，因为诱饵必须被用户识别才有效；并在8.2节用控制平均质量检验稳健性。

- move_code：METHOD_JUSTIFICATION

- statement_status：design_decision

- why_here_cn：诱饵显著性既是理论要求也是设计选择，同时预告后续稳健性检验。

- inherits_from_previous_cn：诱饵需要可比和可见。

- changes_argument_state_cn：评分显著性成为设计特征，也是后续边界条件。

- sets_up_next_cn：为8.3显著性实验埋下伏笔。

- failure_if_removed_cn：诱饵不可见则效应无法产生。

- evidence_pointer：Section 4.2.2

### 9. Section 4.2.2 S5–S8

- order：9

- locator：Section 4.2.2 S5–S8

- paraphrase_cn：按照Ariely将诱饵放在目标项之后作为列表第二项；为跨条件可比且让用户容易看到对比，不随机化列表顺序，均按评分降序排列。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：保持各条件呈现模式一致，并让诱饵对比更明显。

- inherits_from_previous_cn：目标项被定义为列表第一项。

- changes_argument_state_cn：列表结构和目标项定义固定。

- sets_up_next_cn：保证条件间唯一差异是诱饵。

- failure_if_removed_cn：顺序差异会干扰处理效应。

- evidence_pointer：Section 4.2.2

### 10. Section 4.2.3 S1–S4

- order：10

- locator：Section 4.2.3 S1–S4

- paraphrase_cn：用户看到每部电影标题、评分、简介、海报和预告片，在最想看的电影中选择，并设置无选择选项，随后完成感知问卷。

- move_code：DESIGN_FEATURE

- statement_status：design_decision

- why_here_cn：无选择选项用于捕捉用户拒绝整个推荐集合的倾向。

- inherits_from_previous_cn：反转预期提示用户可能退出选择。

- changes_argument_state_cn：加入外部选项作为关键因变量。

- sets_up_next_cn：为感知可靠性机制测试提供流程入口。

- failure_if_removed_cn：无法捕捉个性化中用户放弃选择的行为。

- evidence_pointer：Section 4.2.3

## Study开头、过渡与收束图谱

### 1. 1

- study_or_phase：5.1 Manipulation Check

- opening_move_cn：‘先检查个性化和诱饵操纵’直接开篇。

- transition_from_previous_cn：从实验设计结束转入结果分析。

- closure_move_cn：报告个性化感知显著更高、诱饵条件下感知匹配显著更低。

- creates_next_need_cn：操纵有效后需要看行为结果。

### 2. 2

- study_or_phase：5.2 Model-Free Evidence

- opening_move_cn：‘检验感兴趣效应’给出描述性概率。

- transition_from_previous_cn：操纵检查成功后看行为方向。

- closure_move_cn：指出非个性化中传统效应、个性化中反转并转向无选择选项。

- creates_next_need_cn：描述性证据需要统计模型确认。

### 3. 3

- study_or_phase：5.3 Empirical Analysis

- opening_move_cn：‘为充分评估目标项和无选择的统计显著性，使用logit模型’。

- transition_from_previous_cn：模型无关证据提出后转入推断。

- closure_move_cn：说明使用固定效应logit、session哑变量、用户聚类标准误。

- creates_next_need_cn：需要分别报告目标项和无选择项模型。

### 4. 4

- study_or_phase：5.4 Decoy Effect on the Target Item

- opening_move_cn：‘首先检验诱饵对目标项的影响’。

- transition_from_previous_cn：从模型设定到第一个因变量。

- closure_move_cn：交互显著为负，说明个性化中诱饵降低目标项需求，并给出实践启示。

- creates_next_need_cn：需要看无选择项是否增加。

### 5. 5

- study_or_phase：5.5 Decoy Effect on the No-Choice Option

- opening_move_cn：‘然后评估无选择选项变化的统计显著性’。

- transition_from_previous_cn：目标项已分析。

- closure_move_cn：交互显著为正，说明个性化中诱饵提高无选择，降低整个推荐集合接受度。

- creates_next_need_cn：需要看所有选项的相对变化。

### 6. 6

- study_or_phase：5.6 Relative Changes of All Options

- opening_move_cn：‘为调查其他选项相对目标的变化，估计multinomial logit’。

- transition_from_previous_cn：二值模型之后需要全选择图景。

- closure_move_cn：所有其他选项相对目标项概率上升，无选择项增幅最大，且主要在个性化情境。

- creates_next_need_cn：行为效应确立后需要解释机制。

### 7. 7

- study_or_phase：6 Underlying Mechanism Test

- opening_move_cn：‘认为机制源于个性化用户对可靠性和匹配度的期望’。

- transition_from_previous_cn：行为结果已确立，转向为什么。

- closure_move_cn：结合建议采纳文献说明低准确建议会被折价。

- creates_next_need_cn：需要用感知问卷直接检测机制。

### 8. 8

- study_or_phase：6 Mechanism perception results

- opening_move_cn：‘为检验机制，我们在实验后问感知问题’。

- transition_from_previous_cn：理论机制需要过程证据。

- closure_move_cn：诱饵显著降低感知推荐吸引力和系统可靠性，且个性化中下降更大。

- creates_next_need_cn：需要检验样本和情境的稳健性。

### 9. 9

- study_or_phase：7 Replication Study

- opening_move_cn：‘为评估推广性和稳健性，在AMT上重复同一实验’。

- transition_from_previous_cn：实验室结果需要外部效度。

- closure_move_cn：AMT结果方向与实验室一致，效应幅度类似。

- creates_next_need_cn：需要排除实验设计特性和混淆变量。

### 10. 10

- study_or_phase：8.1 Between-Subject Analysis

- opening_move_cn：‘为确认受试者内结果在受试者间也成立，用首轮数据’。

- transition_from_previous_cn：复制确认后需要排除受试者内顺序效应。

- closure_move_cn：交互方向一致，显著性因样本减少而下降。

- creates_next_need_cn：需要处理电影质量与匹配的混淆。

### 11. 11

- study_or_phase：8.2.1 Control for Item Quality

- opening_move_cn：‘先估计加入电影平均评分控制的固定效应logit’。

- transition_from_previous_cn：质量可能是替代解释。

- closure_move_cn：控制质量后交互仍显著。

- creates_next_need_cn：需要进一步分离质量和匹配度。

### 12. 12

- study_or_phase：8.2.2 Quality in Backend, Fit in Frontend

- opening_move_cn：‘为进一步确保质量不起作用，做新实验，后端控制平均质量、前端显示预测分’。

- transition_from_previous_cn：只做统计控制不够，需要实验操纵。

- closure_move_cn：无论诱饵平均质量高低，低预测分都显著提升无选择并降低目标项。

- creates_next_need_cn：需要测试两者同时可见的情况。

### 13. 13

- study_or_phase：8.2.3 Quality and Fit in Frontend

- opening_move_cn：‘为进一步区分质量和匹配，前端同时展示平均评分和预测分’。

- transition_from_previous_cn：后端控制没有反映真实界面。

- closure_move_cn：只有低匹配的诱饵显著提升无选择并降低目标项；低质量高匹配不显著。

- creates_next_need_cn：需要确认显著性维度本身是否为边界条件。

### 14. 14

- study_or_phase：8.3 Saliency of the Decoy

- opening_move_cn：‘为检验诱饵显著性关键性，在个性化设置中只展示平均评分’。

- transition_from_previous_cn：前面的结果暗示匹配信号显著性重要。

- closure_move_cn：当诱饵以平均质量显著呈现时，传统诱饵效应恢复，目标项选择上升。

- creates_next_need_cn：证据链完整，进入讨论理论含义。

### 15. 15

- study_or_phase：9 Discussion

- opening_move_cn：‘本文对推荐系统和诱饵效应文献作出贡献’。

- transition_from_previous_cn：所有实证结果已汇报。

- closure_move_cn：强调诱饵策略不能在所有推荐情境中使用，并为整体设计提供建议。

- creates_next_need_cn：最后总结全文。

### 16. 16

- study_or_phase：10 Conclusion

- opening_move_cn：‘推荐系统已成为公司在线战略的重要部分’。

- transition_from_previous_cn：讨论之后需要收束。

- closure_move_cn：重申个性化中诱饵适得其反、非个性化中有效，并总结机制和稳健性。

- creates_next_need_cn：无，全文结束。

## 讨论与贡献逐句图谱

### 1. Discussion P1 S1

- order：1

- locator：Discussion P1 S1

- paraphrase_cn：本文对推荐系统和诱饵效应文献均有贡献。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：讨论开篇直接定位贡献。

- inherits_from_previous_cn：全文实验结果。

- changes_argument_state_cn：从结果转述升级为贡献陈述。

- sets_up_next_cn：为具体文献贡献展开。

- failure_if_removed_cn：讨论没有贡献锚点。

- evidence_pointer：Section 9 first sentence

### 2. Discussion P1 S2–S3

- order：2

- locator：Discussion P1 S2–S3

- paraphrase_cn：已有文献强调推荐系统情境因素的重要性，但仍有未探索因素。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：把本文放进取景框。

- inherits_from_previous_cn：贡献声明。

- changes_argument_state_cn：指出本文填补这一缺口。

- sets_up_next_cn：引出‘首次探索诱饵效应’。

- failure_if_removed_cn：贡献的语境缺失。

- evidence_pointer：Discussion P1

### 3. Discussion P1 S4–S5

- order：3

- locator：Discussion P1 S4–S5

- paraphrase_cn：作者是首个在推荐设置中探索诱饵效应的研究；既有文献似乎暗示推荐系统可从诱饵中获益。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：直接声明新颖性并列出传统预期。

- inherits_from_previous_cn：情境因素缺口。

- changes_argument_state_cn：形成传统预期与本文发现的张力。

- sets_up_next_cn：为‘其实不是所有场景都有效’反转做铺垫。

- failure_if_removed_cn：讨论缺少对照性贡献。

- evidence_pointer：Discussion P1

### 4. Discussion P1 S6–S7

- order：4

- locator：Discussion P1 S6–S7

- paraphrase_cn：但本研究显示诱饵策略并非在所有推荐情境中都可实践；非个性化中有帮助，个性化中则适得其反。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：给出核心反直觉结论。

- inherits_from_previous_cn：传统预期已建立。

- changes_argument_state_cn：把结果总结为边界知识。

- sets_up_next_cn：为‘理论在新技术情境变化’提供论据。

- failure_if_removed_cn：核心贡献缺失。

- evidence_pointer：Discussion P1

### 5. Discussion P1 S8–S9

- order：5

- locator：Discussion P1 S8–S9

- paraphrase_cn：由于推荐系统越来越普及，理解既有理论在新技术情境中的变化很重要；诱饵在传统营销中有用，但在个性化情境中可能伤害系统可靠性。

- move_code：THEORY_RETURN

- statement_status：author_inference

- why_here_cn：把边界发现放回理论变迁框架。

- inherits_from_previous_cn：情境反转结论。

- changes_argument_state_cn：从单一发现上升到理论普遍化。

- sets_up_next_cn：为实践影响做铺垫。

- failure_if_removed_cn：理论贡献的普遍性缺失。

- evidence_pointer：Discussion P1 final

### 6. Discussion P2 S1–S4

- order：6

- locator：Discussion P2 S1–S4

- paraphrase_cn：本文也有重要实践含义；推荐系统提供大量吸引人的选项，可能导致选择过载并损害系统有效性。

- move_code：IMPLICATION

- statement_status：author_inference

- why_here_cn：开启管理讨论。

- inherits_from_previous_cn：贡献已声明。

- changes_argument_state_cn：把结果连接回选择过载问题。

- sets_up_next_cn：为诱饵作为缓解策略的讨论做准备。

- failure_if_removed_cn：实践含义缺失。

- evidence_pointer：Discussion P2

### 7. Discussion P2 S5–S7

- order：7

- locator：Discussion P2 S5–S7

- paraphrase_cn：传统选择中诱饵是缓解选择过载的已知策略，公司也用其增加销售；作者提到Apple、Netflix、Spotify等大公司使用该技术。

- move_code：PRIOR_KNOWLEDGE

- statement_status：prior_literature

- why_here_cn：展示实践界对诱饵的期待。

- inherits_from_previous_cn：选择过载需要策略。

- changes_argument_state_cn：诱饵被定位为成熟营销工具。

- sets_up_next_cn：为实践者讨论其在推荐中使用做铺垫。

- failure_if_removed_cn：实践界对诱饵的使用背景缺失。

- evidence_pointer：Discussion P2

### 8. Discussion P2 S8–S9

- order：8

- locator：Discussion P2 S8–S9

- paraphrase_cn：实践者已经在讨论用诱饵作为推荐系统中的助推，例如约会应用可能影响用户行为。

- move_code：CONTEXT

- statement_status：prior_literature

- why_here_cn：说明实践讨论已存在但缺乏证据。

- inherits_from_previous_cn：诱饵营销技术。

- changes_argument_state_cn：引出一个未经实证检验的实践争议。

- sets_up_next_cn：用本文结果裁定争议。

- failure_if_removed_cn：实践争议的背景不足。

- evidence_pointer：Discussion P2

### 9. Discussion P2 S10–S13

- order：9

- locator：Discussion P2 S10–S13

- paraphrase_cn：但本文显示诱饵并非所有场景都有效；其效果正负取决于情境和用户期望，非个性化可用，个性化会导致消费者放弃购买。

- move_code：RESULT

- statement_status：empirical_result

- why_here_cn：用实证结果回应实践争议。

- inherits_from_previous_cn：实践者预期诱饵有效。

- changes_argument_state_cn：实践争议被边界结论裁定。

- sets_up_next_cn：为收入损失推算做铺垫。

- failure_if_removed_cn：实践含义没有证据支撑。

- evidence_pointer：Discussion P2

### 10. Discussion P2 S14–S15

- order：10

- locator：Discussion P2 S14–S15

- paraphrase_cn：Netflix推荐系统年收入超10亿；个性化中诱饵使购买概率降低11%，可能使平台损失超1.1亿。

- move_code：PRACTICAL_STAKES

- statement_status：author_inference

- why_here_cn：把选择概率差异转成商业损失，强化管理警示。

- inherits_from_previous_cn：个性化中诱饵减少目标项选择。

- changes_argument_state_cn：把行为效应量化成经济后果。

- sets_up_next_cn：对比非个性化中的增收机会。

- failure_if_removed_cn：损失严重性的直观描述缺失。

- evidence_pointer：Discussion P2

### 11. Discussion P2 S16–S17

- order：11

- locator：Discussion P2 S16–S17

- paraphrase_cn：相反，非个性化中诱饵提升目标项选择，平台可借此把顾客引向高利润项目以增加收入。

- move_code：IMPLICATION

- statement_status：author_inference

- why_here_cn：给出正反两面的管理启示。

- inherits_from_previous_cn：个性化有损失。

- changes_argument_state_cn：指示非个性化中的机会。

- sets_up_next_cn：引出情境差异对设计的重要性。

- failure_if_removed_cn：管理建议不完整。

- evidence_pointer：Discussion P2 final

### 12. Discussion P3 S1–S2

- order：12

- locator：Discussion P3 S1–S2

- paraphrase_cn：结果强调区分推荐类型的重要性，因为不同情境带来不同期望和行为；这对管理者评估各种行为策略很关键。

- move_code：IMPLICATION

- statement_status：author_inference

- why_here_cn：从诱饵效应推广到一般情境差异化。

- inherits_from_previous_cn：两种情境结果不同。

- changes_argument_state_cn：提出一般设计原则。

- sets_up_next_cn：为多样性策略和混排内容讨论做准备。

- failure_if_removed_cn：情境差异的一般意义未提升。

- evidence_pointer：Discussion P3

### 13. Discussion P3 S3–S4

- order：13

- locator：Discussion P3 S3–S4

- paraphrase_cn：很多公司在追求多样性、新颖性、偶然性等策略；管理层应在大规模实施前先在个性化和非个性化中检验用户行为。

- move_code：IMPLICATION

- statement_status：author_inference

- why_here_cn：把情境差异原则用到常见推荐策略。

- inherits_from_previous_cn：需要区分情境。

- changes_argument_state_cn：把研究结果转化为预测试要求。

- sets_up_next_cn：为Amazon混排内容讨论做铺垫。

- failure_if_removed_cn：实践指导不够具体。

- evidence_pointer：Discussion P3

### 14. Discussion P3 S5–S6

- order：14

- locator：Discussion P3 S5–S6

- paraphrase_cn：Amazon等平台把个性化内容与热门、新品、专家推荐乃至广告混合；本研究提示个性化情境中混合内容需谨慎，以避免非预期效应。

- move_code：IMPLICATION

- statement_status：author_inference

- why_here_cn：阐述情境区分的具体应用。

- inherits_from_previous_cn：情境差异原则。

- changes_argument_state_cn：混排内容被识别为潜在风险。

- sets_up_next_cn：转向推荐系统整体设计的更广含义。

- failure_if_removed_cn：实践应用场景不完整。

- evidence_pointer：Discussion P3 final

### 15. Discussion P4 S1–S2

- order：15

- locator：Discussion P4 S1–S2

- paraphrase_cn：除诱饵具体发现外，本文对推荐系统设计有更广含义；首先强调传统和推荐选择情境的差异，以及在新环境中检验既有理论的重要性。

- move_code：THEORY_RETURN

- statement_status：contribution_claim

- why_here_cn：把贡献从诱饵扩展到理论迁移。

- inherits_from_previous_cn：情境差异已成立。

- changes_argument_state_cn：把结果升华为理论检验原则。

- sets_up_next_cn：引出整体设计观。

- failure_if_removed_cn：理论贡献的普遍性不足。

- evidence_pointer：Discussion P4

### 16. Discussion P4 S3–S5

- order：16

- locator：Discussion P4 S3–S5

- paraphrase_cn：研究提醒研究者和实践者应采用整体方法设计推荐系统，并强调情境因素和在线消费者行为应被纳入设计。

- move_code：DESIGN_KNOWLEDGE

- statement_status：contribution_claim

- why_here_cn：提出可复用的设计知识。

- inherits_from_previous_cn：理论迁移原则。

- changes_argument_state_cn：转向整体推荐系统设计。

- sets_up_next_cn：为核心‘项目非独立’观点做铺垫。

- failure_if_removed_cn：设计知识不够抽象。

- evidence_pointer：Discussion P4

### 17. Discussion P4 S6–S7

- order：17

- locator：Discussion P4 S6–S7

- paraphrase_cn：结果重申集合中的项目不是独立的，不应独立挑选；推荐列表构成影响行为、系统评价和推荐接受。

- move_code：DESIGN_KNOWLEDGE

- statement_status：contribution_claim

- why_here_cn：给出全文最核心的设计原则。

- inherits_from_previous_cn：情境因素和整体设计。

- changes_argument_state_cn：确立推荐集合整体设计观。

- sets_up_next_cn：批判现有研究孤立关注单项目。

- failure_if_removed_cn：可复用设计知识缺失。

- evidence_pointer：Discussion P4

### 18. Discussion P4 S8–S10

- order：18

- locator：Discussion P4 S8–S10

- paraphrase_cn：当前研究和实践多聚焦单个推荐项目的特征，忽略选项间关系和集合效应；本研究是首批展示应把推荐项作为整体设计的研究之一。

- move_code：CONTRIBUTION

- statement_status：contribution_claim

- why_here_cn：与现状比较并声明贡献。

- inherits_from_previous_cn：项目非独立原则。

- changes_argument_state_cn：把发现定位成对主流研究焦点的修正。

- sets_up_next_cn：为未来研究建议做铺垫。

- failure_if_removed_cn：贡献的定位不清晰。

- evidence_pointer：Discussion P4

### 19. Discussion P5 S1–S3

- order：19

- locator：Discussion P5 S1–S3

- paraphrase_cn：未来可研究其他情境因素、其他产品类型（搜索品、耐用品）以及其他消费者行为（如信息搜集）。

- move_code：FUTURE_WORK

- statement_status：author_inference

- why_here_cn：给出研究边界和扩展方向。

- inherits_from_previous_cn：本文只研究电影体验品。

- changes_argument_state_cn：承认边界并指出后续机会。

- sets_up_next_cn：为结论段收束做准备。

- failure_if_removed_cn：边界和未来方向缺失。

- evidence_pointer：Discussion P5

### 20. Conclusion S1–S3

- order：20

- locator：Conclusion S1–S3

- paraphrase_cn：推荐系统已成为公司在线战略核心，影响选择、满意度和忠诚度，因此研究其改进很重要。

- move_code：CONCLUSION

- statement_status：fact

- why_here_cn：结论段重新强调研究重要性。

- inherits_from_previous_cn：讨论中设计含义。

- changes_argument_state_cn：重申实践重要性。

- sets_up_next_cn：总结本文发现。

- failure_if_removed_cn：结论缺少背景重述。

- evidence_pointer：Section 10 opening

### 21. Conclusion S4–S6

- order：21

- locator：Conclusion S4–S6

- paraphrase_cn：本研究考察推荐系统中的诱饵效应，显示其在个性化和非个性化中对消费者行为影响不同：个性化中降低目标项并提高无选择，非个性化中提升目标项。

- move_code：CONCLUSION

- statement_status：empirical_result

- why_here_cn：简洁复述核心发现。

- inherits_from_previous_cn：重要性重述。

- changes_argument_state_cn：把结果再收束一次。

- sets_up_next_cn：总结机制和稳健性。

- failure_if_removed_cn：全文结论缺失。

- evidence_pointer：Section 10

### 22. Conclusion S7–S9

- order：22

- locator：Conclusion S7–S9

- paraphrase_cn：通过分析用户对推荐质量和系统可靠性的看法，作者说明个性化中低匹配诱饵削弱感知质量与可靠性；并通过实验室和AMT多项实验确认稳健性。

- move_code：CONCLUSION

- statement_status：empirical_result

- why_here_cn：总结机制与稳健性。

- inherits_from_previous_cn：核心发现已复述。

- changes_argument_state_cn：完整收束全文。

- sets_up_next_cn：无。

- failure_if_removed_cn：机制和稳健性总结缺失。

- evidence_pointer：Section 10 final

## Study累积逻辑

### 1. 1

- study_or_phase：主实验与模型无关证据

- evidence_job_cn：证明现象存在且方向与假设一致。

- what_it_establishes_cn：个性化中诱饵降低目标项选择、提高无选择；非个性化中提高目标项。

- what_it_cannot_establish_cn：不能排除受试者内顺序效应、样本特殊性和质量混淆。

- why_next_phase_is_needed_cn：描述性概率需要用统计模型确认显著性。

- transition_wording_function_cn：“为了充分评估统计显著性”引入logit模型。

### 2. 2

- study_or_phase：固定效应logit目标项与无选择模型

- evidence_job_cn：确认交互效应的统计显著性和方向。

- what_it_establishes_cn：Decoy×Personalization对目标项显著为负、对无选择显著为正。

- what_it_cannot_establish_cn：不能解释为什么发生反转，也不能排除质量混淆。

- why_next_phase_is_needed_cn：需要看全选项转移并解释机制。

- transition_wording_function_cn：“然后评估无选择选项”和“为调查相对变化”平滑过渡。

### 3. 3

- study_or_phase：multinomial logit相对选择模型

- evidence_job_cn：展示诱饵导致的选择转移去向，尤其是无选择项增幅最大。

- what_it_establishes_cn：个性化诱饵不仅降低目标项，还降低整个推荐集合的接受度。

- what_it_cannot_establish_cn：不能揭示用户内心的期望不一致过程。

- why_next_phase_is_needed_cn：需要感知问卷连接行为与机制。

- transition_wording_function_cn：“我们认为机制源于……”引出机制测试。

### 4. 4

- study_or_phase：感知机制测试

- evidence_job_cn：证明诱饵降低感知推荐吸引力和系统可靠性，尤其在个性化中更严重。

- what_it_establishes_cn：提供了与理论机制一致的过程证据。

- what_it_cannot_establish_cn：是事后自报感知，未做正式中介分析，不能排除其他心理机制。

- why_next_phase_is_needed_cn：需要外部效度检验，确认结果不限于学生样本。

- transition_wording_function_cn：“为评估推广性和稳健性”引出AMT复制。

### 5. 5

- study_or_phase：AMT复制

- evidence_job_cn：证明主效应在不同人口样本中复现。

- what_it_establishes_cn：实验室结果不是学生样本或实验室环境的人为产物。

- what_it_cannot_establish_cn：仍非真实平台，效应幅度略小，且未做统一推断。

- why_next_phase_is_needed_cn：需要排除受试者内设计特有的顺序效应。

- transition_wording_function_cn：“为确保受试者内结果在受试者间也成立”引出受试者间分析。

### 6. 6

- study_or_phase：受试者间分析

- evidence_job_cn：排除受试者内设计和顺序效应的替代解释。

- what_it_establishes_cn：只用首轮数据时交互方向仍一致。

- what_it_cannot_establish_cn：样本量减小使部分结果显著性下降，且仍未排除电影质量。

- why_next_phase_is_needed_cn：需要检验质量与匹配的混淆。

- transition_wording_function_cn：“然后我们控制了电影平均评分”进入质量控制。

### 7. 7

- study_or_phase：质量控制与前后端实验

- evidence_job_cn：排除诱饵平均质量作为驱动因素，锁定低预测匹配度。

- what_it_establishes_cn：控制质量后交互效应仍在；后端质量和前端双展示实验中，低匹配始终驱动反转。

- what_it_cannot_establish_cn：尚未回答诱饵显著性维度是否是关键边界。

- why_next_phase_is_needed_cn：需要验证若诱饵显著性维度换成平均质量是否恢复传统效应。

- transition_wording_function_cn：“为检验诱饵显著性关键性”引出最后一个实验。

### 8. 8

- study_or_phase：诱饵显著性实验

- evidence_job_cn：把反转效应归因于匹配度维度的显著性，并界定边界条件。

- what_it_establishes_cn：当诱饵以平均质量显著呈现时，传统诱饵效应恢复，目标项选择上升。

- what_it_cannot_establish_cn：未测试真实平台中两类分数同时出现且同等显著的情况。

- why_next_phase_is_needed_cn：证据链完整，进入讨论和理论贡献。

- transition_wording_function_cn：讨论段用“本文对文献作出贡献”承接并升华。

## 主张—证据台账

### 1. 非个性化推荐中诱饵提升目标项需求

- claim_cn：非个性化推荐中诱饵提升目标项需求

- claim_level：artifact

- supporting_evidence_cn：实验室模型无关证据0.25→0.31，固定效应logit Decoy主效应β=0.300 p<0.05；AMT复制0.27→0.29；受试者间分析Decoy β=0.569 p<0.05。

- support_strength：direct

- where_claim_is_made：Section 5.2, 5.4, 7, 8.1; Hypothesis 1

- where_evidence_is_provided：Figure 4, Table 3, Figure 9, Table 9

### 2. 个性化推荐中诱饵降低目标项需求并提高无选择选项

- claim_cn：个性化推荐中诱饵降低目标项需求并提高无选择选项

- claim_level：artifact

- supporting_evidence_cn：实验室目标项0.34→0.20，无选择0.05→0.16；交互项目标-1.005、无选择1.544均p<0.001；AMT方向一致；受试者间交互-1.610和2.489。

- support_strength：direct

- where_claim_is_made：Section 5.2, 5.4, 5.5, 7, 8.1; Hypothesis 2

- where_evidence_is_provided：Figure 4, Tables 3-4, Figures 9-10, Tables 9-10

### 3. 个性化中的反转由降低的感知推荐质量和系统可靠性驱动

- claim_cn：个性化中的反转由降低的感知推荐质量和系统可靠性驱动

- claim_level：mechanism

- supporting_evidence_cn：诱饵显著降低感知吸引力-0.556且个性化中更显著-0.638；系统可靠性-0.673且个性化中-0.815。

- support_strength：partial

- where_claim_is_made：Section 6 and Introduction P10 S8

- where_evidence_is_provided：Tables 6-7, Figures 7-8

### 4. 反转效应由低匹配（预测分）驱动，而非低平均质量驱动

- claim_cn：反转效应由低匹配（预测分）驱动，而非低平均质量驱动

- claim_level：mechanism

- supporting_evidence_cn：后端质量控制中高质低匹配和低质低匹配诱饵都显著提升无选择并降低目标项；前端双展示中只有低匹配处理显著。

- support_strength：direct

- where_claim_is_made：Section 8.2.2 and 8.2.3

- where_evidence_is_provided：Tables 13-14

### 5. 诱饵显著性维度决定是否出现反转：以匹配度显著则反转，以平均质量显著则传统效应恢复

- claim_cn：诱饵显著性维度决定是否出现反转：以匹配度显著则反转，以平均质量显著则传统效应恢复

- claim_level：boundary

- supporting_evidence_cn：个性化设置只展示平均评分时，诱饵使目标项选择β=0.651 p<0.05，无选择不显著。

- support_strength：direct

- where_claim_is_made：Section 8.3

- where_evidence_is_provided：Table 15

### 6. 个性化诱饵可能导致超过1.1亿美元收入损失

- claim_cn：个性化诱饵可能导致超过1.1亿美元收入损失

- claim_level：design_knowledge

- supporting_evidence_cn：以Netflix年收入超10亿和购买概率下降11%推算，没有经济模型或实际转化率。

- support_strength：asserted

- where_claim_is_made：Discussion P2 S14-S15

- where_evidence_is_provided：无直接证据，只有概率推算

### 7. 推荐集合应作为整体设计，项目不是独立的

- claim_cn：推荐集合应作为整体设计，项目不是独立的

- claim_level：design_knowledge

- supporting_evidence_cn：诱饵效应整体改变集合接受度和无选择倾向；但没有直接对比“整体设计”和“独立设计”两种系统。

- support_strength：partial

- where_claim_is_made：Discussion P4 S6-S10

- where_evidence_is_provided：全文行为证据作为间接支持

## ISR定位逻辑

- constitutive_is_problem_cn：本文把推荐系统理解为一种选择架构：算法决定呈现给用户的集合，因此算法的‘设计选择’会反过来构成用户行为与市场结果。诱饵效应不是外部噪音，而是推荐系统内容设计的一部分。

- technology_behavior_or_market_entanglement_cn：个性化技术制造了用户对‘系统了解我’的期望。这种期望使同一个诱饵在个性化推荐与非个性化推荐中产生相反的行为和系统评价，说明技术能力与心理机制不可分离。

- role_of_benchmark_or_objective_evidence_cn：非个性化条件充当传统诱饵效应的基准，无诱饵条件充当自然选择基准；固定效应logit和multinomial logit把键盘选择概率转化为可推断的因果交互，支持‘情境决定效应方向’的IS主张。

- theory_in_design_cn：说服理论确实进入设计：决定操纵什么（匹配度vs质量、个性化 vs 非个性化）以及测量什么（感知可靠性和吸引力）都来自理论。但推荐算法本身（SVD、数据库）来自工程实践，理论没有精确决定算法细节。

- technical_vs_is_contribution_balance_cn：技术内容主要用于构建实验平台而非作为研究贡献；篇幅上，行为实验、模型、机制和稳健性占绝对主导。文章的技术贡献是‘能操纵诱饵的推荐实验平台’，但核心IS贡献是行为差异和设计规则。

- beyond_transient_performance_cn：文章没有止于一次分数或选择概率差：用感知问卷解释机制，用AMT复制、受试者间、质量和显著性实验确立边界条件，最后把结果上升为‘推荐集合应整体设计’的可复用知识，因此超越暂时性性能优势。

## 段落级仿写模板

### abstract_steps

#### 1. 1

- step：1

- rhetorical_job_cn：点明研究对象。

- evidence_required_cn：需要明确具体研究对象。

- sentence_function_cn：一句话给出领域与核心概念。

- transition_to_next_cn：立即给出该对象的核心机制。

#### 2. 2

- step：2

- rhetorical_job_cn：综述传统知识的稳健性。

- evidence_required_cn：需要一个在传统情境有充分证据的机制。

- sentence_function_cn：用文献共识建立基线。

- transition_to_next_cn：同时提实践者使用，证明商业重要性。

#### 3. 3

- step：3

- rhetorical_job_cn：把传统机制迁移到新情境。

- evidence_required_cn：需要新情境正在普及且有独特特征。

- sentence_function_cn：建立传统机制与新情境的关联和张力。

- transition_to_next_cn：指出该机制尚未在新情境中被检验。

#### 4. 4

- step：4

- rhetorical_job_cn：说明为什么新情境可能改变机制。

- evidence_required_cn：需要有一个理论上的机制理由（如期望差异）。

- sentence_function_cn：给出‘因此可能正面也可能负面’的竞争预期。

- transition_to_next_cn：预告实证方法。

#### 5. 5

- step：5

- rhetorical_job_cn：预告研究方法和理论透镜。

- evidence_required_cn：需要已经选定实验方法。

- sentence_function_cn：用‘我们进行了随机受控实验并用某理论作为透镜’概括。

- transition_to_next_cn：给出主要结果。

#### 6. 6

- step：6

- rhetorical_job_cn：报告核心结果的方向性。

- evidence_required_cn：需要已经得到结果。

- sentence_function_cn：用‘取决于情境，诱饵可以或不可以推动目标项需求’等概括。

- transition_to_next_cn：分开说明两种情境。

#### 7. 7

- step：7

- rhetorical_job_cn：分别报告个性化和非个性化的具体结果。

- evidence_required_cn：需要两种情境足够的对比证据。

- sentence_function_cn：用两句镜像句给出反转。

- transition_to_next_cn：承诺机制和稳健性。

#### 8. 8

- step：8

- rhetorical_job_cn：声明机制、稳健性和贡献。

- evidence_required_cn：需要已做机制测量和附加实验。

- sentence_function_cn：用‘我们还探索机制、多实验稳健，发现对设计有启示’收束。

- transition_to_next_cn：无需继续。

### introduction_paragraph_steps

#### 1. 1

- step：1

- rhetorical_job_cn：从现实问题或商业后果开篇。

- evidence_required_cn：需要行业统计或可引用的商业数据。

- sentence_function_cn：给出问题规模。

- transition_to_next_cn：介绍当前解决方案及其局限。

#### 2. 2

- step：2

- rhetorical_job_cn：把现实问题转成学术空白。

- evidence_required_cn：需要既有文献对行为因素的忽视。

- sentence_function_cn：从‘算法精度’转向‘行为因素’。

- transition_to_next_cn：引入核心理论工具。

#### 3. 3

- step：3

- rhetorical_job_cn：介绍核心理论工具在传统情境中的价值。

- evidence_required_cn：需要经典理论文献。

- sentence_function_cn：强调理论和实践上的有效性。

- transition_to_next_cn：转折到新情境的独特特征。

#### 4. 4

- step：4

- rhetorical_job_cn：建立新情境与旧情境的结构性差异。

- evidence_required_cn：需要用户期望、技术特征等理论依据。

- sentence_function_cn：指出‘因此不能简单照搬’。

- transition_to_next_cn：陈述本文研究范围。

#### 5. 5

- step：5

- rhetorical_job_cn：提出第一个研究问题。

- evidence_required_cn：需要研究问题有理论和实践相关性的论证。

- sentence_function_cn：用引号明示研究问题。

- transition_to_next_cn：描述回答问题的两种可能结果。

#### 6. 6

- step：6

- rhetorical_job_cn：让竞争性预期显得都合理。

- evidence_required_cn：需要每个分支都有理论或文献支持。

- sentence_function_cn：分别列出积极和消极分支。

- transition_to_next_cn：提出第二个研究问题。

#### 7. 7

- step：7

- rhetorical_job_cn：定义实践中的关键情境维度。

- evidence_required_cn：需要有一组真实且常见的推荐类型。

- sentence_function_cn：个性化vs非个性化定义。

- transition_to_next_cn：提出情境比较的研究问题。

#### 8. 8

- step：8

- rhetorical_job_cn：预告研究方法和核心发现。

- evidence_required_cn：需要已设计实验并有结果。

- sentence_function_cn：用四条件实验和结果预告。

- transition_to_next_cn：解释机制的预期。

#### 9. 9

- step：9

- rhetorical_job_cn：解释发现背后的机制并宣称稳健性。

- evidence_required_cn：需要有理论机制解释，且计划了稳健性实验。

- sentence_function_cn：用‘我们相信这是因为用户期望’等。

- transition_to_next_cn：声明贡献。

#### 10. 10

- step：10

- rhetorical_job_cn：把结果写成文献贡献和实践启示。

- evidence_required_cn：需要回指学者呼吁和实际争议。

- sentence_function_cn：列出首项研究、理论扩展、实践指导。

- transition_to_next_cn：给出论文结构。

### theory_to_design_steps

#### 1. 1

- step：1

- rhetorical_job_cn：综述核心理论并给出机制。

- evidence_required_cn：需要经典理论和机制文献。

- sentence_function_cn：从相对判断到诱饵机制层层递进。

- transition_to_next_cn：指出新情境中的空白。

#### 2. 2

- step：2

- rhetorical_job_cn：综述新情境的既有研究并定位本文贡献。

- evidence_required_cn：需要推荐系统情境因素文献。

- sentence_function_cn：从呈现格式到推荐集合构成。

- transition_to_next_cn：引出理论透镜。

#### 3. 3

- step：3

- rhetorical_job_cn：选择理论透镜并提取关键构念。

- evidence_required_cn：需要理论与情境有可映射关系。

- sentence_function_cn：用说服理论的来源可信度、内容质量、匹配度解释推荐系统。

- transition_to_next_cn：区分两种推荐类型的信息本质。

#### 4. 4

- step：4

- rhetorical_job_cn：通过机制推理导出竞争性预测。

- evidence_required_cn：需要期望不一致、建议采纳等理论连接。

- sentence_function_cn：从‘个人相关性强=更敏感’推导反转。

- transition_to_next_cn：给出假设。

#### 5. 5

- step：5

- rhetorical_job_cn：把机制映射到具体设计参数。

- evidence_required_cn：需要在界面中能操纵匹配度和质量信号。

- sentence_function_cn：把低匹配诱饵操作化为低预测分、同类型、显眼评分。

- transition_to_next_cn：进入实验设计。

### method_and_study_sequence_steps

#### 1. 1

- step：1

- rhetorical_job_cn：给出整体实验策略和样本。

- evidence_required_cn：需要预设样本和实验类型。

- sentence_function_cn：先交代随机受控实验和复制。

- transition_to_next_cn：描述平台与数据。

#### 2. 2

- step：2

- rhetorical_job_cn：说明平台、数据、种子化流程。

- evidence_required_cn：需要真实数据源和用户评分。

- sentence_function_cn：用电影数据库和评分任务建立平台。

- transition_to_next_cn：说明四条件设计。

#### 3. 3

- step：3

- rhetorical_job_cn：解释实验设计的每个关键选择。

- evidence_required_cn：需要设计决策的理由。

- sentence_function_cn：对受试者内、绑定条件、算法选择、诱饵放置逐一辩护。

- transition_to_next_cn：报告操纵检验。

#### 4. 4

- step：4

- rhetorical_job_cn：先报告操纵检验再报告模型无关证据。

- evidence_required_cn：需要操纵检验数据和描述性统计。

- sentence_function_cn：用表格和图展示模式。

- transition_to_next_cn：进入推断模型。

#### 5. 5

- step：5

- rhetorical_job_cn：用多个计量模型交叉验证。

- evidence_required_cn：需要目标项、无选择项和全选项模型。

- sentence_function_cn：固定效应logit加multinomial logit。

- transition_to_next_cn：解释机制。

#### 6. 6

- step：6

- rhetorical_job_cn：用感知调查连接机制。

- evidence_required_cn：需要过程变量测量。

- sentence_function_cn：比较有无诱饵条件下感知质量与可靠性。

- transition_to_next_cn：复制和稳健性。

#### 7. 7

- step：7

- rhetorical_job_cn：用复制、替换分析、分离实验和边界实验加固结论。

- evidence_required_cn：需要AMT样本、首轮数据、附加实验样本。

- sentence_function_cn：逐一回应每个替代解释。

- transition_to_next_cn：进入讨论。

### results_reporting_steps

#### 1. 1

- step：1

- rhetorical_job_cn：报告操纵检验，建立处理有效性。

- evidence_required_cn：需要感知操纵题项和固定效应模型。

- sentence_function_cn：用显著系数证明‘用户确实感知到个性化/诱饵’。

- transition_to_next_cn：进入行为结果。

#### 2. 2

- step：2

- rhetorical_job_cn：先给模型无关证据。

- evidence_required_cn：需要各条件选择概率。

- sentence_function_cn：用图展示四条件概率并解读方向。

- transition_to_next_cn：进入统计模型。

#### 3. 3

- step：3

- rhetorical_job_cn：分层报告统计模型：目标项、无选择项、全选项。

- evidence_required_cn：需要logit、交互项和multinomial估计。

- sentence_function_cn：先主效应再交互模型，逐表解读系数。

- transition_to_next_cn：指出机制问题。

#### 4. 4

- step：4

- rhetorical_job_cn：把行为结果与理论机制连接。

- evidence_required_cn：需要感知问卷数据。

- sentence_function_cn：用感知吸引力和可靠性回归展示交互。

- transition_to_next_cn：转入复制和稳健性。

### discussion_and_contribution_steps

#### 1. 1

- step：1

- rhetorical_job_cn：重述文献定位和核心贡献。

- evidence_required_cn：需要全文证据的综合。

- sentence_function_cn：第一句声明双重文献贡献。

- transition_to_next_cn：用‘虽然传统预期…但本研究…’制造对比。

#### 2. 2

- step：2

- rhetorical_job_cn：把结果转化为管理实践含义。

- evidence_required_cn：需要有可引用的商业规模数字。

- sentence_function_cn：用收入损失和增收机会量化启示。

- transition_to_next_cn：扩展到一般情境区分。

#### 3. 3

- step：3

- rhetorical_job_cn：提出更抽象的设计原则。

- evidence_required_cn：需要从行为证据到设计知识的推理。

- sentence_function_cn：从‘项目不独立’到‘推荐集合整体设计’。

- transition_to_next_cn：批判现有研究焦点。

#### 4. 4

- step：4

- rhetorical_job_cn：承认边界并给未来方向。

- evidence_required_cn：需要意识到产品类型和情境限制。

- sentence_function_cn：列出产品类型、行为类型和情境因素扩展。

- transition_to_next_cn：结论段收束。

#### 5. 5

- step：5

- rhetorical_job_cn：结论段重述重要性、发现、机制和稳健性。

- evidence_required_cn：需要核心结果和机制摘要。

- sentence_function_cn：用‘推荐系统重要→我们发现→机制→稳健性’收束。

- transition_to_next_cn：无。

## 可执行写作算法

### 1. 1

- step：1

- rhetorical_job_cn：用现实问题或商业后果开篇并建立研究对象的重要性。

- research_evidence_required_cn：需要行业统计、公司案例或权威报告说明问题规模。

- sentence_pattern_function_cn：先给出规模句，再给出当前方案，最后指出方案局限。

- transition_condition_cn：当读者承认问题重要且现有方案有缺陷时，进入文献缺口。

### 2. 2

- step：2

- rhetorical_job_cn：同时综述核心理论和新情境文献，并指出交叉空白。

- research_evidence_required_cn：需要经典理论有大量稳健证据，新情境有普及度和独特特征。

- sentence_pattern_function_cn：每个文献流先综述后收束，最后用‘然而没有研究…’合成空白。

- transition_condition_cn：当空白清晰且填补理由成立时，选择理论透镜。

### 3. 3

- step：3

- rhetorical_job_cn：用理论透镜把空白转化为机制性假设。

- research_evidence_required_cn：需要理论构念能映射到情境变量，并能解释为何效应方向可能反转。

- sentence_pattern_function_cn：先介绍理论构念，再区分情境的信息本质，最后推导竞争性假设。

- transition_condition_cn：当机制链完整且两个假设方向明确时，进入实验设计。

### 4. 4

- step：4

- rhetorical_job_cn：构造能操纵情境变量的实验平台，并说明每个设计选择的理由。

- research_evidence_required_cn：需要可运行的推荐系统、真实数据、用户评分流程和被试。

- sentence_pattern_function_cn：先整体实验策略，再数据平台，再四条件结构，再诱饵设计，最后选择任务。

- transition_condition_cn：当实验平台能产生两类推荐且诱饵可识别时，报告操纵检验。

### 5. 5

- step：5

- rhetorical_job_cn：先操纵检验，再模型无关证据，再统计模型分层报告。

- research_evidence_required_cn：需要操纵题项显著、各条件选择概率以及固定效应/混合效应/multinomial模型。

- sentence_pattern_function_cn：按目标项→无选择项→全选项的顺序报告交互项系数。

- transition_condition_cn：当核心交互效应显著且方向与假设一致时，进入机制解释。

### 6. 6

- step：6

- rhetorical_job_cn：用过程变量把行为结果与理论机制连接。

- research_evidence_required_cn：需要在实验流程中加入感知问卷或过程指标。

- sentence_pattern_function_cn：先陈述理论机制，再用感知变量回归结果支持机制。

- transition_condition_cn：当机制变量在关键条件下显著变化时，进入复制和稳健性。

### 7. 7

- step：7

- rhetorical_job_cn：通过复制、设计替换分析和边界实验排除替代解释。

- research_evidence_required_cn：需要第二样本、受试者间数据、控制混淆变量的实验组设计。

- sentence_pattern_function_cn：针对每个替代解释安排一个实验或分析，并逐一排除。

- transition_condition_cn：当所有主要替代解释被排除且边界条件清晰时，进入讨论。

### 8. 8

- step：8

- rhetorical_job_cn：把结果上升为理论贡献、设计知识和边界条件。

- research_evidence_required_cn：需要结果能回答引言中的竞争性预期并有边界证据。

- sentence_pattern_function_cn：先文献贡献，再管理含义，再抽象设计原则，最后未来方向。

- transition_condition_cn：当读者看到结论不止于一次性效应时，论文完成。

## 应模仿的高价值动作

1. 先报告模型无关证据再上计量模型，让读者先看到直观模式再看到统计显著。

2. 在引言中把积极与消极两种分支都构建得理论可行，从而制造实证检验的必要性。

3. 用交互项而不是单纯主效应来表述核心预测，把个性化/非个性化差异变成可检验的统计交互。

4. 把无选择选项作为关键因变量，从而捕捉用户对推荐集合整体的拒绝。

5. 每个稳健性问题都配置专门实验，而不是只用统计控制带过。

6. 在讨论中把具体诱饵结果抽象为‘推荐集合应整体设计’的设计知识。

7. 用AMT复制、受试者间分析、质量和显著性实验逐层加固同一个核心主张。

## 不要只复制的表面动作

1. 不要仅用一句‘据我们所知首次’来宣称新颖性，必须有充分的文献综述支撑。

2. 不要把选择概率的下降直接等价于收入损失，除非有经济模型和真实转化率。

3. 不要使用商业博文或从业者网页作为关键机制证据。

4. 不要在受试者内设计中绑定条件后不讨论可能的顺序效应。

5. 不要把事后问卷调查中的感知差异直接当成已证明的中介机制。

## 证据薄弱或跳跃的动作

1. 从11%选择概率下降直接推算超过1.1亿美元收入损失，缺乏转化率和商品价格数据。

2. 称Apple、Netflix、Spotify实际使用诱饵效应没有正式公开证据，只引用博文。

3. ‘诱饵降低感知可靠性’被当作机制，但未做正式中介分析。

4. AMT复制的效应幅度小于实验室，且没有把两样本放进统一推断模型。

5. 多个附加实验的样本量较小，部分系数只有边际显著。

## 一句话套路

用理论透镜锁定一个经典效应可能在新情境中反转的条件，用随机实验和交互模型确认方向，用感知变量解释机制，再用复制和一串排除实验确立边界，最后把发现抽象为可复用的推荐系统整体设计知识。

## 分析边界

正文中的表格和图片OCR存在格式噪音（如上下标、引号、部分系数符号显示异常），个别系数如β=1.544、β=1.704在原文中显示为带下划线或上标，本分析以上下文语义为准。在线附录（Table A1、C1、Figures B/E）只能从正文推断，未直接核对。结论中的收入损失属于作者推算而非实证。未能获取实际实验代码和完整问卷文本。
