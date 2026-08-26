# 20 篇种子论文的近期施引文献与检索式召回验证

## 结论

- 807 条 Scopus 施引记录中有 176 篇发表于 2021–2026，且全部具有摘要。
- DeepSeek V4 Pro 根据题名、摘要和关键词筛出 30 篇 `likely_direct` 和 3 篇 `possible_direct`；这些是全文复核候选，不等同于最终全文纳入。
- 30 篇明确候选中没有一篇来自 Basket 11。近期研究主要迁移到软件工程、人本编程、HCI、计算机教育和少量 AI/NLP 来源。
- 旧扩展检索式召回 25/30（83.3%）；改进后的跨领域高召回检索式召回 30/30（100%），并召回 3 篇不确定项中的 2 篇。
- 唯一没有被高召回式命中的不确定项是一本只写 `software review`、未明确说明是否审查代码的书。为找回它而加入宽泛的 `software review` 会产生大量噪声，适合由引文追踪补充。
- 该验证集来自种子论文施引链，不能证明检索式对整个 Scopus 的绝对召回率；它能证明检索式没有漏掉这批已知的近期知识后继。

## 近期候选构成

- 年份：2026=3; 2025=7; 2024=7; 2023=5; 2022=4; 2021=4。
- 行动者：human_only=25；human_ai=4；agent_only=1。
- 模型抽取的活动计数：理解 17、编写 14、调试/修复 7、检查/审查 5、生成 3、测试 2、修改/重构 2；一篇可包含多种活动。

代表性的新近分支包括：

- OpenAI 生成测试骨架，再由学生补全、验证与修复；
- Ivie 为编程助手刚生成的代码提供定位解释，支持程序员理解与检查；
- 比较开发者与神经代码模型在代码探索中的注意力；
- LLM 识别和解释程序逻辑结构；
- T5 模型生成 SQL、SPARQL 与 Cypher 查询；
- 代码注释、算法标签、眼动模式和执行日志对程序理解或调试的影响；
- 低代码开发、SQL 学习、TDD、结对编程和电子表格调试。

## 检索式回测

| 检索式 | 807 条中命中 | 近期 176 条中命中 | 明确候选召回 | 不确定候选召回 | 近期非直接命中 |
|---|---:|---:|---:|---:|---:|
| Q1 标题高精度 | 56 | 15 | 9/30 (30.0%) | 0/3 | 6 |
| Q1 题名摘要关键词 | 100 | 30 | 19/30 (63.3%) | 0/3 | 11 |
| Q2 旧扩展式 | 221 | 46 | 25/30 (83.3%) | 0/3 | 21 |
| Q8 AIS 专业词式 | 198 | 41 | 24/30 (80.0%) | 0/3 | 17 |
| Q3 现代智能体补充式 | 5 | 5 | 5/30 (16.7%) | 0/3 | 0 |
| Q9 跨领域高召回式 | 218 | 55 | 30/30 (100.0%) | 2/3 | 23 |

高召回式在 176 篇近期记录中命中 55 篇，其中 30 篇明确相关、2 篇不确定、23 篇非直接相关。它的作用是生成可控的全文筛选池，而不是直接给出最终文献集。

## 推荐的 Scopus 分块检索式

建议四个词块分别运行、分别保存命中数，最后按 EID、DOI 和题名去重。这样比一条巨型表达式更容易审计。

### A. 编写、理解与编程任务

```text
TITLE-ABS-KEY(
  "program comprehension" OR "code comprehension" OR
  "software comprehension" OR "program understanding" OR
  "code understanding" OR "code reading" OR "reading source code" OR
  "code exploration" OR
  "programming task*" OR "coding task*" OR
  "programming performance" OR "programmer performance" OR
  "programming productivity" OR "programming practice*" OR
  "programming pattern*" OR "programming environment*" OR
  "introductory programming" OR "programming education" OR
  "novice programmer*" OR "pair programming" OR
  "test-driven development" OR "execution log*"
)
```

### B. 检查、调试、修复、修改与测试

```text
TITLE-ABS-KEY(
  "code review" OR "code inspection" OR "code inspecting" OR
  "program debugging" OR "code debugging" OR "source code debugging" OR
  (debug* W/5 (program* OR code OR software)) OR
  "bug fixing" OR "fault localization" OR "fault localisation" OR
  "program repair" OR "test generation" OR "test skeleton*" OR
  "unit test generation" OR "code modification" OR
  "program modification" OR "code refactoring"
)
```

### C. 查询、电子表格、终端用户与低代码编程

```text
TITLE-ABS-KEY(
  "query formulation" OR "query development" OR "query reuse" OR
  "query complexity" OR "structured query language*" OR
  "text-to-SQL" OR "text to SQL" OR "text-to-SPARQL" OR
  "text-to-Cypher" OR
  (SQL W/8 (query OR learn* OR teach* OR error* OR debug* OR
             writ* OR formulat* OR skill*)) OR
  "spreadsheet error*" OR "spreadsheet testing" OR
  "spreadsheet development" OR "spreadsheet debugging" OR
  "spreadsheet programming" OR "spreadsheet formula*" OR
  "end-user programming" OR "low-code" OR "low code" OR
  "visual programming"
)
```

### D. 代码生成、补全与编程智能体

```text
TITLE-ABS-KEY(
  "code generation" OR "generate code" OR "generating code" OR
  "generated code" OR "just-generated code" OR
  "code completion" OR "code autocomplete" OR
  "code autocompletion" OR "code suggestion*" OR
  "AI-assisted programming" OR "AI-assisted coding" OR
  "AI-assisted software development" OR "AI pair programmer*" OR
  "coding agent*" OR "programming agent*" OR
  "coding assistant*" OR "programming assistant*" OR
  "code assistant*" OR "GitHub Copilot" OR "OpenAI Codex" OR
  (("large language model*" OR LLM* OR ChatGPT OR "generative AI")
   W/15
   (programming OR coding OR "source code" OR "code generation" OR
    "code completion" OR "program comprehension" OR
    "program repair" OR "test generation" OR SQL))
)
```

用于近期综述时，可在每个词块后追加 `AND PUBYEAR > 2015`。识别阶段不建议先限制来源或文献类型；来源和文献类型应作为筛选字段保留，而不是检索前硬删除。

## 为什么仅靠施引检索仍然不够

807 条施引记录中：

- 没有出现字面短语 `code completion`、`code autocomplete` 或 `code autocompletion`；
- 没有出现 `GitHub Copilot`，只有 Ivie 的元数据出现一般的 `Copilot`；
- 只有 5 篇被现代智能体补充词块捕捉。

因此，前向追引能发现程序理解、TDD、查询、低代码和部分 LLM 桥接研究，但不能替代 D 词块对代码补全、Copilot、Codex 和 coding agents 的独立全库检索。

## 30 篇摘要明确相关的近期施引文献

| 年份 | 标题 | 来源 | 行动者 | 摘要判断概括 |
|---:|---|---|---|---|
| 2026 | Are we too focused on single query language? Investigating text-to-SQL/SPARQL/Cypher task complexity via fine-tuning unbiased T5 models | Neurocomputing | agent_only | 研究通过微调T5模型评估文本到多查询语言（SQL/SPARQL/Cypher）的生成性能，发现查询语言选择显著影响执行准确性。 |
| 2026 | Evaluating Logical Structure in Computer Programs Using LLMs | Proceedings of the International Florida Artificial Intelligence Research Society Conference, FLAIRS | human_ai | 评估大型语言模型（LLM）识别和解释计算机程序逻辑步骤的能力，并与人类专家标注进行相似度比较。 |
| 2026 | The Effect of Comments on Program Comprehension: An Eye-tracking Study | Empirical Software Engineering | human_only | 通过眼动追踪实验研究代码注释对程序理解的影响，涉及20名计算机科学专业学生阅读和理解源代码的任务。 |
| 2025 | DevTales: A Tool for Providing Narrative Code Histories into Developer Workflows | Proceedings of IEEE Symposium on Visual Languages and Human-Centric Computing, VL/HCC | human_only | 论文提出DevTales工具，在IDE中集成代码历史叙事以帮助理解陌生代码，并在调试、理解原理和代码重用三项用户研究中评估。 |
| 2025 | Eye-movement indices of reading while debugging Python source code | Journal of Cognitive Psychology | human_only | 研究通过眼动追踪记录有经验程序员在调试Python源代码时的阅读行为，分析其与文本阅读的异同，以理解代码阅读中的眼动特征。 |
| 2025 | Implementation of Test-Driven Approach to Empower Self-Learning in PHP Web Programming Practice | International Journal of Computing | human_only | 本研究提出了一个自学习框架，利用测试驱动开发来提升PHP编程教育。框架帮助学生通过自动测试反馈独立调试和改进代码。对150名印尼IT新生评估，所有学生在经过多次尝试后都通过了全部测试用例，证明了框架有效性。 |
| 2025 | Providing Information About Implemented Algorithms Improves Program Comprehension: A Controlled Experiment | Proceedings of the 29th International Conference on Evaluation and Assessment in Software Engineering , EASE, 2025 edition, EASE 2025 | human_only | 本文通过一项包含56名参与者的受控实验，评估了源代码中算法标签（算法名称及额外信息）对程序理解正确性和时间的影响。结果显示标签显著提高了程序理解的正确性，但不影响完成时间，定性分析表明参与者认为标签有助于识别代码意图。 |
| 2025 | QUANTIFYING THE EFFECT OF TEST-DRIVEN DEVELOPMENT ON SOFTWARE QUALITY | Journal of Theoretical and Applied Information Technology | human_only | 该研究通过混合实证方法（随机对照试验与仓库挖掘）评估测试驱动开发对软件质量的影响，参与者完成结构化编程任务，比较TDD与非TDD条件下的代码覆盖率和可维护性。 |
| 2025 | Unravelling the Computational Thinking and Spatial Thinking Development: An Exploration of a Virtual Robot Programming Environment | Journal of Computer Assisted Learning | human_only | 研究通过让30名中学生完成虚拟机器人编程任务，采集编程行为日志、屏幕录像和有声思维，分析其计算思维和空间思维的微观发展模式及相互关系，发现三类学习者，并揭示了编程中自上而下和自下而上调试等特征。 |
| 2025 | “C”ing the light–assessing code comprehension in novice programmers using C code patterns | Computer Science Education | human_only | 研究使用Rasch模型评估一组C代码片段作为编程能力评估工具的有效性和难度，分析特定C操作对代码片段难度的贡献。 |
| 2024 | Automation of Test Skeletons Within Test-Driven Development Projects | Software Engineering Education Conference, Proceedings | human_ai | 研究了一个利用OpenAI模型生成测试骨架的工具，并通过学生实验探讨人机交互如何影响测试骨架到功能测试的转换，发现人机交互促进了测试优先的编程实践，提高了测试数量和代码覆盖率，并强调了AI生成测试的验证与修复中的人机交互价值。 |
| 2024 | Diversity's Double-Edged Sword: Analyzing Race's Effect on Remote Pair Programming Interactions | ACM Transactions on Software Engineering and Methodology | human_only | 研究通过让24名经验丰富的开发者进行远程结对编程任务，采用有声思维法和回顾性访谈，探究种族对交互的影响，发现混合种族对在生产力分数上更高，代码质量无差异，但面临沟通挑战和不适。 |
| 2024 | Do developer perceptions have borders? Comparing C code responses across continents | Software Quality Journal | human_only | 比较美国和中国学生对C语言中混淆原子代码片段的理解差异，通过预测输出任务测量准确性和速度。 |
| 2024 | Exploring differences in self-regulated learning strategy use between high- and low-performing students in introductory programming: An analysis of eye-tracking and retrospective think-aloud data from program comprehension | Computers and Education | human_only | 该研究通过眼动追踪和回顾性出声思考方法，分析高、低绩效学生在入门编程课程中理解Python程序时自我调节学习策略的差异。 |
| 2024 | Follow-Up Attention: An Empirical Study of Developer and Neural Model Code Exploration | IEEE Transactions on Software Engineering | human_ai | 研究比较开发者和神经代码模型在理解代码时的注意力模式，提出 follow-up attention 方法预测开发者下一步注视行，展示了利用预训练模型注意力信号进行有效代码探索的潜力。 |
| 2024 | Growth in Knowledge of Programming Patterns: A Comparison Study of CS1 vs. CS2 Students | SIGCSE 2024 - Proceedings of the 55th ACM Technical Symposium on Computer Science Education | human_only | 比较CS1和CS2学生在编程模式知识上的增长，通过在线调查评估代码识别、判断可读结构、代码理解、代码编写和编辑等任务，关注两类代码结构。 |
| 2024 | Ivie: Lightweight Anchored Explanations of Just-Generated Code | Conference on Human Factors in Computing Systems - Proceedings | human_ai | 本文提出 Ivie 工具，为编程助手生成的代码即时提供轻量级定位解释，以支持程序员对生成代码的理解和检查。通过实验室研究比较了 Ivie 与基线工具，发现 Ivie 能提高对生成代码的理解，且被程序员视为有用且低干扰的辅助。 |
| 2023 | A mental model approach to teaching database querying skills with SQL and Alteryx | Journal of Accounting Education | human_only | 提出一种基于心理模型的教学方法，通过分步教学SQL并迁移到Alteryx来培养数据库查询技能。 |
| 2023 | FxD: a functional debugger for dysfunctional spreadsheets | Proceedings of IEEE Symposium on Visual Languages and Human-Centric Computing, VL/HCC | human_only | 论文提出FxD电子表格调试器，支持用户逐步执行公式依赖项并提供上下文信息，通过受控实验评估其调试体验，发现定性改善。 |
| 2023 | Investigating the Effects of Testing Frequency on Programming Performance and Students' Behavior | SIGCSE 2023 - Proceedings of the 54th ACM Technical Symposium on Computer Science Education | human_only | 该论文通过准实验研究了测试频率对计算机科学入门课程中学生编程表现的影响，用代码写作题目评估表现，并分析学习行为。 |
| 2023 | Low-code Development Productivity | Queue | human_only | 通过实验室实验比较基于代码、低代码和极端低代码技术的开发生产力，低代码技术显示出更高的生产力。 |
| 2023 | Pair Programming Practiced in Hybrid Work | International Symposium on Empirical Software Engineering and Measurement | human_only | 本研究通过个案研究探讨混合工作环境下结对编程的实践方式，采用访谈、观察、反馈和调查等方法，发现结对编程可通过现场、远程和混合模式进行，混合模式效果最差，强调需适应个体工作模式偏好。 |
| 2022 | Effect of semantic distance on learning structured query language: An empirical study | Frontiers in Psychology | human_only | 通过实验研究语义距离对学习者编写SQL查询的影响，分析从自然语言规划到SQL编码的转换困难，并提出教学建议。 |
| 2022 | Exploring How Students Solve Open-ended Assignments: A Study of SQL Injection Attempts in a Cybersecurity Course | Annual Conference on Innovation and Technology in Computer Science Education, ITiCSE | human_only | 研究学生在网络安全课程中完成开放式SQL注入攻击作业的策略，分析学生如何生成成功的注入，发现存在探索与利用的不同模式，且后续作业中利用策略更明显。 |
| 2022 | Identifying Code Reading Strategies in Debugging using STA with a Tolerance Algorithm | APSIPA Transactions on Signal and Information Processing | human_only | 本研究通过眼动追踪实验，利用带容差的扫描路径趋势分析，识别了学生在调试任务中的代码阅读策略。发现高绩效学生能根据程序复杂度采用自下而上或自上而下的灵活策略，而低绩效学生则缺乏明确策略。 |
| 2022 | Readable vs.Writable code: A Survey of Intermediate Students' Structure Choices | SIGCSE 2022 - Proceedings of the 53rd ACM Technical Symposium on Computer Science Education | human_only | 调查中级计算机科学学生编写代码时对控制结构的选择，探讨其与专家偏好的差异、可读性认知以及理解问题，强调教学应结合读写情境。 |
| 2021 | An interview study of how developers use execution logs in embedded software engineering | Proceedings - International Conference on Software Engineering | human_only | 对25名ASML嵌入式软件开发者进行访谈，研究其如何分析执行日志以支持维护任务，发现日志分析面临缺乏领域知识、代码不熟悉和并发性等挑战，并得出需要多抽象级别日志比较和差异分类等工具支持的实证结论。 |
| 2021 | Considerations and Pitfalls in Controlled Experiments on Code Comprehension | IEEE International Conference on Program Comprehension | human_only | 论文讨论在代码理解受控实验中需要考虑的因素和常见陷阱，涉及实验对象、代码、任务和度量指标的方法论问题。 |
| 2021 | Error messages in relational database management systems: A comparison of effectiveness, usefulness, and user confidence | Journal of Systems and Software | human_only | 该研究以152名参与者为对象，比较四种关系数据库管理系统的错误消息在有效性、有用性和用户信心方面的差异，评估其对查找和修复SQL查询错误的影响。结果显示客观有效性与主观有用性存在差异。 |
| 2021 | Integrating a graph builder into python tutor | OpenAccess Series in Informatics | human_only | 论文改进Python Tutor程序可视化工具，集成控制流图、数据流图等图表示，旨在帮助编程初学者理解源代码，通过可视化分析程序结构和执行路径。 |

## 3 篇需要全文确认的边界文献

| 年份 | 标题 | 来源 | 为什么不确定 |
|---:|---|---|---|
| 2024 | Modern Software Review: Techniques and Technologies | Modern Software Review: Techniques and Technologies | 摘要提及软件评审用于检测缺陷，但未明确评审对象是否包含代码或可执行程序；软件评审常包括代码审查，存在直接涉及代码检查的可能，需查看全文确认。 |
| 2023 | Systematically reusing low‐code IT artefacts; A technological and managerial approach | CEUR Workshop Proceedings | 题名明确涉及低代码工件，属于低代码编程产物，但摘要缺失，无法确认研究是否直接聚焦于人或智能体的具体编程活动（如编写、修改、测试等），可能更多关注重用策略与管理层面，因此暂列为可能直接相关。 |
| 2022 | Low-Code Versus Code-Based Software Development: Which Wins the Productivity Game? | IT Professional | 摘要明确提及对软件开发技术进行生产力比较的实验，涉及开发与维护，暗示参与者执行了编程活动，但未具体描述活动类型（如编写、调试），需查看全文确认是否直接研究编程活动。 |

## 解释边界

这次 30/30 是对“20 篇旧种子的近期施引后继”的回溯性召回，不是对全体近期编程文献的绝对召回证明。更可靠的正式流程应是：

1. 用 A–D 四个词块在 Scopus 全库独立检索；
2. 用 20 篇种子的前向与后向引文补充；
3. 对全库检索新增而施引链未发现的代码补全/智能体论文建立第二个验证集；
4. 用 DeepSeek 做题名摘要高召回筛选，再全文确认；
5. 报告各轨新增文献数以及每条轨道独有的最终纳入文献。
