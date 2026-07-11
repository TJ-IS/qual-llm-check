# Situation awareness 经典文献原文阅读：定义、测量与 coding agent 迁移

## 1. 本文档目的

这个文档回应一个更严格的问题：

> 如果我们要以 situation awareness 作为唯一基础概念，它在经典高引文献中到底是什么意思？它是怎么被测量的？这些定义和测量如何迁移到 coding agent 用户体验研究？

本次阅读优先查看高引经典文献原文或可访问 PDF，而不是只看二手摘要。

## 2. 已获取并阅读的核心原文

本地 PDF 证据保存在：

`runs/coding_agent_ux_misq_isr/source_pdfs_sa/`

| 文献 | 年份 | 来源 | 作用 | 本地文件 |
| --- | ---: | --- | --- | --- |
| Endsley, **Toward a Theory of Situation Awareness in Dynamic Systems** | 1995 | *Human Factors* | 经典理论定义，三层结构，SA state 与 assessment process 区分 | `maritime_theory_sa.pdf` |
| Endsley, **Measurement of Situation Awareness in Dynamic Systems** | 1995 | *Human Factors* | SA 测量综述，query/freeze technique 的有效性与侵入性讨论 | `endsley_1995_measurement_sa.pdf` |
| Endsley et al., **A Comparative Analysis of SAGAT and SART for Evaluations of Situation Awareness** | 1998 | HFES proceedings | 直接比较 SAGAT 与 SART，说明 objective 与 subjective SA 不等价 | `endsley_1998_sagat_sart_comparison.pdf` |
| Salmon et al., **Situation Awareness Measurement: Methods Review and Recommendations** | 2006 | measurement review | 系统总结 freeze probe、real-time probe、self-rating、observer rating 等测量方法 | `salmon_2006_sa_measurement_review.pdf` |
| Taylor/SART 量表说明 | 1989/1990 origin, later scale sheet | SART 的 10 个评分维度和 7 点量表形式 | `sart_scale_notes.pdf` |

补充查看了 IS 语境中的应用：

- Jaeger and Eckhardt (2021), *Information Systems Journal*, **Eyes wide open: The role of situational information security awareness for security-related behaviour**；
- Nadj, Maedche, and Schieder (2020), *Decision Support Systems*, **The effect of interactive analytical dashboard features on situation awareness and task performance**。

## 3. 经典定义到底是什么意思

### 3.1 不是泛泛的 awareness

Endsley 的核心定义可以概括为：

> SA 是人在动态任务环境中，对当前相关元素进行感知、理解其意义，并预测其近期状态变化的认知状态。

它不是泛泛的“知道一点情况”，也不是单纯“信息可见”。它至少包含三层：

| 层级 | 原含义 | 关键问题 |
| --- | --- | --- |
| Level 1: perception | 感知当前环境中相关元素的状态、属性和变化 | 发生了什么？有哪些关键元素？ |
| Level 2: comprehension | 将感知到的元素整合起来，理解它们对当前目标的意义 | 这意味着什么？为什么重要？ |
| Level 3: projection | 基于当前状态和理解，预测近期状态如何变化 | 接下来可能发生什么？ |

这三个层级对我们很重要，因为 coding agent 的用户痛点不能只写成“看不清 diff”。如果只停在 Level 1，那只是信息可见性。真正的 SA 还要求：

- 用户理解 diff、测试、命令输出对任务目标和风险的意义；
- 用户能预测批准下一步后 agent 可能改变什么。

### 3.2 SA 是 state/product，不是过程本身

Endsley 的理论明确区分：

- **situation assessment**：获取、搜索、整合、解释信息的过程；
- **situation awareness**：这些过程形成的认知状态或知识状态。

这对我们写概念定义很关键。我们不能把构念定义成“用户查看日志、读 diff、问 agent 的过程”。这些是形成 SA 的活动或前因。我们要测的是：

> 用户最终是否形成了对 agent-mediated coding situation 的感知、理解和预测。

因此，coding agent UI 的计划展示、diff summary、terminal log、approval prompt、test report、risk warning 都是 **SA support**，不是 SA 本身。

### 3.3 SA 是动态、目标导向、受系统设计影响的

Endsley 的理论把 SA 放在动态决策系统中讨论，强调：

- attention 和 working memory 限制用户能处理多少信息；
- goals 和 mental models 会影响用户注意什么、如何解释信息；
- interface design、automation、workload、stress、system complexity 会影响 SA；
- SA 影响后续 decision 和 performance，但不等于 performance。

这对 coding agent 特别贴切。coding agent 的任务环境是动态的：

- 文件和代码状态持续变化；
- agent 运行命令、搜索、编辑、测试；
- 用户的目标、限制、风险容忍度持续影响他该关注什么；
- automation 可能带来 out-of-the-loop problem；
- approval request 如果没有足够上下文，会增加 workload 而不是提高 SA。

## 4. 经典文献怎么测量 SA

### 4.1 SAGAT：objective freeze-probe

SAGAT 是经典 objective measure。

基本逻辑：

1. 在模拟任务或动态任务中随机或预设时点暂停；
2. 隐藏/冻结当前信息显示，防止用户继续查看；
3. 提问用户当前情境中的关键事实、意义或未来状态；
4. 将用户回答与 ground truth 比较；
5. 按 Level 1、Level 2、Level 3 分别评分。

SAGAT 的关键不是“问几个问题”，而是：

- probe 必须来自 domain-specific cognitive task analysis；
- 问题要覆盖 perception、comprehension、projection；
- 答案必须能和真实任务状态比较；
- 不能只问用户自我感觉。

Endsley et al. (1998) 的比较研究说明，SAGAT 通过 simulation freeze 中的 queries 获取 objective SA。原文也指出，SAGAT 问题通常覆盖三层 SA，并需要针对领域定制。

### 4.2 SART：subjective post-trial rating

SART 是主观量表，通常任务后填写。

完整 SART 有 10 个 7 点评分维度，常被压缩成三个更高层维度：

| 高层维度 | 典型组成 |
| --- | --- |
| attentional demand | instability, complexity, variability |
| attentional supply | arousal, concentration, division of attention, spare mental capacity |
| understanding | information quantity, information quality, familiarity |

这说明 SART 不是简单问“你有没有 situation awareness”。它实际混合了：

- 任务对注意力的需求；
- 用户可用注意力资源；
- 用户对情境信息的理解感。

所以 SART 很适合做 perceived SA，但不能等同于 actual SA。

### 4.3 SAGAT 和 SART 不等价

Endsley et al. (1998) 的重要结论是：SAGAT 和 SART 都能对系统设计变化表现出敏感性，但两者并不高度一致。SART 更接近主观信心、主观表现或自我感知；SAGAT 更接近对 ground truth 的准确掌握。

对我们来说，这意味着：

> 如果只做用户自评量表，我们测到的可能是“我觉得自己掌握了情况”，而不一定是用户真的知道 agent 改了什么、为什么改、下一步会怎样。

所以 coding agent 概念开发最好采用：

- subjective scale：用户感知的 coding-agent work-situation awareness；
- objective probes：用户对 agent logs/diffs/tests/approval consequences 的准确回答；
- behavioral outcomes：审批准确率、误批率、接管率、回滚率等。

### 4.4 real-time probe

real-time probe 不冻结任务，而是在任务过程中提问。

优点：

- 比 freeze probe 更适合真实现场；
- 可以记录回答内容和响应时间；
- 对 coding agent 的自然使用更友好。

缺点：

- 提问本身会改变用户注意力；
- 用户可能因为被问而开始关注某些信息；
- 在高频 coding task 中可能干扰工作流。

在 coding agent 场景里，real-time probe 可以放在自然断点，例如：

- agent 生成 approval request 前；
- agent 完成一组 edits 后；
- test failure 后；
- 用户准备接管或 rollback 前。

### 4.5 observer rating

observer rating 由专家根据用户行为推断 SA。

优点：

- 适合 field study；
- 不一定需要打断任务；
- 可以结合 screen recording、logs、think-aloud。

缺点：

- 很难直接知道用户内部认知状态；
- 需要领域专家；
- 不如 ground-truth probe 精准。

coding agent 场景可以用 expert coding 记录：

- 用户是否在关键风险处停下来；
- 用户是否能针对性纠偏；
- 用户审批是否与真实风险匹配；
- 用户是否误以为 agent 已完成或未完成某步。

### 4.6 performance / behavioral measures

经典文献和 review 都提醒：performance 不是 SA 本身。

原因是：

- 好 performance 可能来自运气或任务简单；
- 高 SA 也可能因为执行限制而没有转化为 performance；
- 只看 performance 无法知道用户在哪一层 SA 出问题。

因此，coding agent 中的 task success、完成时间、bug 数、rollback 数只能作为后果或辅助指标，不能直接替代 SA 测量。

### 4.7 eye tracking / physiological measures

SA 文献也讨论 eye movement、physiological indicators 等过程指标。它们更适合测用户注意到了什么、认知负荷如何，而不是直接测完整 SA。

ISJ 2021 的 situational information security awareness 研究很有启发：它用 phishing experiment、eye tracking 和 survey 结合，研究个体经验、warning signal、contextual relevance、misplaced salience 如何影响情境性安全觉察，并进一步影响 threat appraisal、coping appraisal 和实际行为。

这说明 IS 论文可以把经典 SA 改造成具体情境概念，并用多方法测量。

## 5. IS 文献里的迁移示例

### 5.1 Situational information security awareness

Jaeger and Eckhardt (2021, ISJ) 做的事情非常像我们要做的模式：

1. 从经典 situation awareness literature 出发；
2. 针对 phishing/security-related behaviour 定义一个 context-specific construct；
3. 研究 individual-level 和 system-level 前因；
4. 用 experiment、eye tracking、survey 组合测量；
5. 连接到 threat appraisal、coping appraisal 和实际安全行为。

这个文献告诉我们：开发 coding-agent-specific SA 是合理的，但必须做到：

- 明确情境边界；
- 说明经典 SA 在新情境中如何具体化；
- 有前因、机制和后果；
- 测量不能只靠泛泛的自评。

### 5.2 DSS dashboard 中的 SA

Nadj, Maedche, and Schieder (2020, DSS) 研究 interactive analytical dashboard features 对 SA 和 task performance 的影响。该文的重要启发是：某些交互分析功能可能提高 task performance，却降低 SA，并引发 out-of-the-loop problem。

这对 coding agent 很关键：

> coding agent 可能让任务完成更快，但用户对当前工作情境的感知、理解和预测反而下降。

这正是我们概念的现实价值。

## 6. 对 coding agent 概念定义的直接影响

基于经典 SA 原文，我建议新构念写成：

> **Coding-agent work-situation awareness** 是指用户在一次具体 coding-agent 编程任务中，对由 agent 行动、代码库状态、工具执行结果、任务约束和下一步风险共同构成的动态工作情境进行感知、理解和预测的程度。

中文：

> **编码代理工作情境觉察** 是指用户在一次具体 coding-agent 编程任务中，对 agent 行动、代码库状态、工具执行结果、任务约束和下一步风险所构成的动态工作情境进行感知、理解和预测的程度。

这个定义比上一版更清楚：

- 它不是 trust；
- 不是 control；
- 不是 transparency；
- 不是 readability；
- 不是 workspace awareness；
- 不是 mutual understanding。

它测的是用户对 **agent-mediated coding situation** 的认知状态。

## 7. 三层结构如何具体化

| SA 层级 | coding agent 中测什么 | 不是测什么 |
| --- | --- | --- |
| Perception | 用户是否知道 agent 正在做什么、改了哪里、运行了什么、产生了哪些结果 | 不是界面是否好看，也不是日志是否存在 |
| Comprehension | 用户是否理解这些行动/结果对任务目标、代码语义、约束和风险意味着什么 | 不是简单能复述文件名 |
| Projection | 用户是否能预测 agent 下一步会做什么、批准后会改变什么、哪里需要介入 | 不是泛泛信任 agent |

## 8. 初始测量设计

### 8.1 Subjective scale

建议 task-episode 后使用 7 点李克特。

#### Perception

- 我能清楚知道 agent 当前正在执行什么编程行动。
- 我能清楚知道 agent 修改或检查了哪些代码位置。
- 我能及时注意到 agent 运行命令或测试后的关键结果。
- 我能区分哪些代码变化是 agent 造成的，哪些是原本已有的。

#### Comprehension

- 我能理解 agent 的修改为什么与当前任务有关。
- 我能理解 agent 的行动对代码行为或项目风险的影响。
- 我能判断 agent 当前行动是否仍符合我设定的任务约束。
- 我能理解测试结果或错误输出对当前任务进展意味着什么。

#### Projection

- 我能预期批准下一步后 agent 可能会做什么。
- 我能预测 agent 的下一步行动可能影响哪些代码或测试。
- 我能判断什么时候需要介入、纠偏或接手。
- 我能预判继续让 agent 执行可能带来的主要风险。

### 8.2 Objective probe：coding-agent SAGAT

可以设计 **CA-SAGAT**：

在任务自然断点暂停，例如 approval request、diff summary、test failure、agent plan update 后，问用户：

#### Level 1 probes

- agent 刚刚修改了哪些文件？
- agent 刚刚运行了什么命令或测试？
- 当前有哪些测试通过或失败？
- 当前 approval request 会允许 agent 执行什么动作？

#### Level 2 probes

- agent 为什么修改这个文件？
- 这个失败测试说明了什么问题？
- 当前修改是否触碰了你设定的限制？
- 哪个改动最可能影响核心功能？

#### Level 3 probes

- 如果批准下一步，agent 最可能接着做什么？
- 哪个文件或模块最可能被继续修改？
- 如果不介入，最大的风险是什么？
- 你下一步最应该检查什么？

评分方式：

- 将回答与 agent logs、diff、test output、approval prompt、task constraints 比较；
- 对 factual probes 用正确/部分正确/错误；
- 对 projection probes 用 predefined acceptable answers 或 expert rating；
- 分别计算 Level 1、Level 2、Level 3 分数。

### 8.3 Behavioral outcomes

作为后果变量或效标效度：

- approval accuracy；
- risky approval rate；
- unnecessary denial rate；
- diff inspection time；
- repeated clarification requests；
- correction frequency；
- rollback / revert rate；
- takeover rate；
- task success；
- perceived control；
- approval fatigue；
- calibrated trust；
- continued use intention。

## 9. 为什么经典 SA 必须迁移，而不是直接照搬

经典 SA 通常假设：

- 操作者面对外部动态环境；
- 系统显示环境状态；
- 人根据态势做决策；
- freeze probe 可以询问环境元素。

coding agent 情境不同：

| 经典 SA | coding agent 情境 |
| --- | --- |
| situation 多为外部环境，如飞行、控制室、交通、战场 | situation 是代码库、agent 行动、工具调用、测试结果和任务约束共同构成 |
| 操作者通常直接操控系统 | 用户常处于监督、审批、纠偏、接管的位置 |
| automation 可能隐藏系统状态 | coding agent 直接生成代码状态变化，并可能让用户 out of the loop |
| ground truth 是环境/模拟状态 | ground truth 是 logs、diff、commands、tests、git status、task constraints |
| projection 是环境状态变化 | projection 包括 agent 下一步行动和代码状态风险 |

所以我们不是简单使用 SA，而是开发：

> agent-mediated coding work 中的 situation awareness。

这就是新概念的迁移合理性。

## 10. 当前判断

读完经典定义和测量文献后，`situation awareness` 作为基础概念比 `workspace awareness` 更稳，原因更明确：

- 概念定义成熟；
- 三层结构清楚；
- 测量传统严谨；
- 有 objective 和 subjective 两种测量路径；
- 可以自然解释 out-of-the-loop 和 automation；
- 可以迁移到 coding agent 的审批、监督、纠偏、接管场景；
- 能从 ISJ 2021 和 DSS 2020 看到 IS 领域已有情境化迁移做法。

因此建议继续推进：

> **基础概念：situation awareness**  
> **新构念：coding-agent work-situation awareness / 编码代理工作情境觉察**

## 11. 后续需要补的证据

下一步最好做两件事：

1. 精读更多 IS 中的 SA 应用文献，尤其是：
   - phishing / information security awareness；
   - dashboard / operational DSS；
   - automation / out-of-the-loop；
   - AI-assisted decision support。
2. 从 Reddit coding agent 评论里编码 SA 缺失的自然语言证据，例如：
   - 看不懂 agent 正在干什么；
   - 不知道 diff 意味着什么；
   - 不知道审批下一步会发生什么；
   - 反复要求 agent summarize；
   - 因为看不清状态而接管或停用。

如果这些用户评论确实大量落在 perception、comprehension、projection 三层上，这个构念就会非常扎实。

## 12. 使用链接

- Endsley (1995), Toward a Theory of Situation Awareness in Dynamic Systems: https://journals.sagepub.com/doi/10.1518/001872095779049543
- Endsley (1995), Measurement of Situation Awareness in Dynamic Systems: https://journals.sagepub.com/doi/10.1518/001872095779049499
- Endsley et al. (1998), A Comparative Analysis of SAGAT and SART: https://journals.sagepub.com/doi/10.1177/154193129804200119
- Taylor/SART overview: https://skybrary.aero/articles/situation-awareness-rating-technique-sart
- Salmon et al. (2006), Situation Awareness Measurement review PDF: https://bura.brunel.ac.uk/bitstream/2438/1422/1/Situation_awareness_measurement_Salmon_et_al.pdf
- Jaeger and Eckhardt (2021), Situational information security awareness: https://onlinelibrary.wiley.com/doi/abs/10.1111/isj.12317
- Nadj, Maedche, and Schieder (2020), Dashboard SA and task performance: https://www.sciencedirect.com/science/article/pii/S0167923620300774
