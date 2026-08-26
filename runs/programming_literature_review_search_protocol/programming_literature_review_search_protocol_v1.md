# 编程情境文献综述检索方案 v1
> **已被取代。** 本文件保留为早期召回审计与备选词库存，不是正式执行协议。正式执行采用 `runs/programming_systematic_literature_review/search_protocol_v2.md` 的“一条稳定概念式 + 有界权威来源 + 引文扩展”方案。

版本日期：2026-07-26
## 一、建议采用的总体设计
主检索不限定 AIS、Basket 或某几个期刊，而是在 Scopus 全库的标题、摘要、关键词字段中检索；另以 Web of Science Core Collection 复检，并用 ACM Digital Library、IEEE Xplore 和 AISeL 补充数据库覆盖差异。AIS Basket 11、AIS 期刊/会议及软件工程、HCI、计算机教育来源在检索后作为来源分层报告，而不是在检索前删除。
完整文献集由四条相互独立、最后合并去重的轨道构成：
1. 数据库主题检索：运行下列 A—D 四个 Scopus 检索块。
2. 引文追溯：对最终纳入文献以及现有 20 篇已确认种子做后向参考文献追溯和前向施引追溯。
3. 综述追溯：寻找主题相关综述，从其纳入表、参考文献和施引文献补充。
4. 更新检索：正式写作或投稿前，用相同检索式重跑并记录新增文献。
这四条轨道必须分别保存命中数和独有纳入数。20 篇种子不能作为唯一检索入口，也不能用来反推一个只会重新找到种子的窄检索式；它们只用于验证检索式对已知正例的召回。
## 二、研究边界
### 核心定义
纳入研究个人、多人协作主体或软件/AI 智能体直接从事以下一种或多种活动的文献：
- 编写、生成、合成或补全程序；
- 阅读、理解、解释、导航、探索、检查或审查程序；
- 调试、定位故障、修复、修改、编辑、重构或维护程序；
- 编写、生成、执行或评价程序测试。
“程序”包括传统源代码，也包括在任务中承担可执行或形式化计算功能的数据库查询、电子表格公式/模型、低代码或可视化程序。是否把这些边界形式并入核心分析，应在编码时用 `program_representation` 字段区分，而不应在初检时删除。
### 纳入所要求的中心性
只有当上述活动本身是研究对象、干预/设计对象、被评价能力或主要任务时才纳入。仅仅把“程序员”“软件开发”“代码库”作为样本背景、职业背景、项目背景、组织情境或数据来源，不构成纳入。
### 初检阶段不使用的限制
- 不添加 `human`、`developer` 或 `programmer` 作为必须满足的 AND 条件，否则会漏掉智能体独立编程以及摘要没有写明参与者称谓的研究。
- 不使用宽泛的 `software development` 单独作为检索词。
- 不用 `AND NOT` 排除 survey、project、organization、education 等词；这些只能通过题录和全文筛选判断，提前排除会降低召回。
- 主检索不设起始年份。检索后再分别报告全时期、2016 年以来和 2021 年以来的结果。
## 三、Scopus 模块化检索式
所有检索均限定为 `TITLE-ABS-KEY`。四块分别运行、分别导出，再按 EID、DOI、规范化题名去重。模块化运行比一个超长检索式更容易复核每一类词带来的新增文献，也能降低 Scopus 复杂检索超时的风险。
### A. 人类编程、编程表现与直接任务
```text
TITLE-ABS-KEY(
  "programming task" OR "coding task" OR
  "programming performance" OR "programmer performance" OR
  "programming productivity" OR "programmer productivity" OR
  "programming practice" OR "programming behavior" OR
  "programming behaviour" OR "programming strategy" OR
  "programming pattern" OR "programming environment" OR
  "programmer problem solving" OR
  "introductory programming" OR "programming education" OR
  "learning to program" OR "learning programming" OR
  "teaching programming" OR
  "novice programmer" OR "student programmer" OR
  "pair programming" OR "mob programming" OR
  "test-driven development"
)
```
### B1. 代码生成、补全与编程智能体：通用术语
```text
TITLE-ABS-KEY(
  "code generation" OR "source code generation" OR
  "program generation" OR "program synthesis" OR
  "automatic programming" OR
  "code completion" OR "code autocomplete" OR
  "code autocompletion" OR "code suggestion" OR
  "AI-assisted programming" OR "AI assisted programming" OR
  "AI-assisted coding" OR "AI assisted coding" OR
  "AI-assisted software development" OR
  "AI pair programmer" OR "AI coding assistant" OR
  "AI programming assistant" OR "AI code assistant" OR
  "coding agent" OR "programming agent" OR
  "software engineering agent" OR
  "coding assistant" OR "programming assistant" OR
  "code assistant" OR "code language model" OR
  "code large language model"
)
```
### B2. 代码生成、补全与编程智能体：生成式 AI 语境补充
```text
TITLE-ABS-KEY(
  "large language model" OR LLM OR ChatGPT OR
  "generative AI" OR "foundation model"
)
AND
TITLE-ABS-KEY(
  programming OR coding OR "source code" OR
  "code generation" OR "code completion" OR
  "program synthesis" OR "program comprehension" OR
  "code comprehension" OR "program repair" OR
  "code review" OR debugging OR "test generation"
)
```
B2 有意比 B1 宽。它用于捕获没有使用“coding assistant”标准称谓的近期研究，噪声应在筛选阶段处理。
### B3. 代码生成、补全与编程智能体：工具名称补充
```text
TITLE-ABS-KEY(
  "GitHub Copilot" OR "OpenAI Codex" OR
  "Amazon CodeWhisperer" OR CodeWhisperer OR
  Tabnine OR "Replit Ghostwriter" OR
  AlphaCode OR "Code Llama" OR CodeLlama OR
  "Claude Code" OR "Gemini Code Assist" OR
  "Cursor IDE" OR "Devin AI"
)
```
B3 是版本化补充词表，不是稳定的概念检索式。每次更新检索都要检查新增或改名工具，并在附录保存当次词表版本。
### C. 理解、检查、调试、修改与测试
```text
TITLE-ABS-KEY(
  "program comprehension" OR "code comprehension" OR
  "software comprehension" OR "program understanding" OR
  "code understanding" OR "source code understanding" OR
  "code reading" OR "reading source code" OR
  "code exploration" OR "code navigation" OR
  "program visualization" OR "code visualization" OR
  "code review" OR "source code review" OR
  "code inspection" OR "program inspection" OR
  "program debugging" OR "code debugging" OR
  "source code debugging" OR
  "bug fixing" OR "fault localization" OR "fault localisation" OR
  "program repair" OR "automated program repair" OR
  "code modification" OR "program modification" OR
  "code editing" OR "program editing" OR
  "code refactoring" OR "program refactoring" OR
  "program maintenance" OR
  "execution log" OR "execution trace" OR
  "program testing" OR "code testing" OR "unit testing" OR
  "test generation" OR "test case generation" OR
  "unit test generation" OR "test skeleton" OR
  "program verification" OR "code verification" OR
  "code explanation" OR "code summarization"
)
```
### D. SQL、电子表格、终端用户与低代码编程
```text
TITLE-ABS-KEY(
  "query formulation" OR "query development" OR
  "query writing" OR "query reuse" OR "query debugging" OR
  "structured query language" OR "SQL programming" OR
  "SQL query writing" OR "SQL query formulation" OR
  "text-to-SQL" OR "text to SQL" OR
  "text-to-SPARQL" OR "text to SPARQL" OR
  "text-to-Cypher" OR "text to Cypher" OR
  "spreadsheet programming" OR "spreadsheet development" OR
  "spreadsheet debugging" OR "spreadsheet testing" OR
  "spreadsheet error" OR "spreadsheet formula" OR
  "end-user programming" OR "end user programming" OR
  "end-user development" OR "end user development" OR
  "low-code development" OR "low code development" OR
  "no-code development" OR "no code development" OR
  "visual programming" OR "block-based programming" OR
  "robot programming"
)
```
## 四、检索来源及其角色
| 来源 | 角色 | 是否作为主检索 |
|---|---|---|
| Scopus | 跨 IS、软件工程、HCI、计算机教育与 AI 的主元数据库；导出 EID 便于去重和引文追溯 | 是 |
| Web of Science Core Collection | 独立复检并支持前向施引追溯 | 是 |
| ACM Digital Library | 补足 CHI、CSCW、SIGCSE、ICSE/FSE 相关 ACM 会议和期刊 | 补充 |
| IEEE Xplore | 补足 TSE、ICSE、VL/HCC 等 IEEE 来源 | 补充 |
| AISeL | 补足 ICIS、AMCIS、ECIS、PACIS 和 AIS 期刊 | 补充 |
| Google Scholar | 已知文献核对、前向追引和缺失条目恢复；因覆盖和排序不透明，不作为可复现的唯一主库 | 追溯 |
| AIS Basket 11 | 作为 IS 顶级期刊子集报告覆盖、年代和主题差异 | 分层，不硬限 |
如果资源只允许先运行一个数据库，应先运行 Scopus A—D，再做 20 篇种子和新增纳入文献的双向引文追溯；不能只检索 Basket。现有验证中，20 篇种子的 807 篇施引记录里有 176 篇发表于 2021 年以后，题录筛出的 30 篇近期明确候选没有一篇来自 Basket 11。
## 五、筛选和编码流程
### 阶段 1：去重与自动检查
保留每条记录的检索轨道、数据库、完整检索式、检索日期和原始导出批次。依次按 EID、DOI、题名规范化结果去重；同一研究的会议版和期刊扩展版先关联，不在初期武断删除。
### 阶段 2：标题—摘要—关键词高召回筛选
DeepSeek 只判断：
1. 是否有证据表明编程活动本身可能是研究对象或评价对象；
2. 涉及哪些动作；
3. 行动者是人、人与 AI、智能体还是不明确；
4. 是否需要全文确认。
模型输出 `include`、`exclude` 或 `uncertain`，并给出证据片段和排除原因。`include` 与 `uncertain` 全部进入全文筛选。
### 阶段 3：全文纳入判断
全文必须明确支持“直接编程活动是研究中心”，并编码：
- `actor_configuration`：human / human-human / human-AI / agent-only；
- `programming_action`：write / generate / complete / understand / inspect / debug / repair / modify / refactor / test；
- `program_representation`：source-code / SQL-query / spreadsheet / low-code / visual-or-block / other；
- `study_focus`：programming-activity / tool-design-and-evaluation / technical-benchmark / education / project-or-organization；
- `unit_of_analysis`；
- `empirical_method`；
- 自变量、中介、调节、因变量、理论；
- 与 situation awareness 的显式关系和可推导关系，二者分开记录。
### 阶段 4：人工复核
- 所有模型判为纳入和不确定的文献由人核对全文。
- 随机复核一批模型排除项，并对每个检索模块分别抽样，避免某类术语系统性漏判。
- 最好由两名筛选者独立判断一部分重叠样本，报告一致率并通过协商解决分歧；如果只有一名研究者，则至少保存模型原始输出、人工改判和理由，明确这一限制。
## 六、召回校准与停止规则
检索式冻结前做两类回测：
1. 历史正例：20 篇已人工确认的核心编程文献应全部命中数据库检索或引文追溯联合流程。
2. 近期正例：现有 807 篇施引记录中由题录筛出的 30 篇 `likely_direct` 应全部被 A—D 联合式命中。此前跨领域高召回式已达到 30/30；旧式只达到 25/30。
这只能证明对已知正例的召回，不能证明对 Scopus 全库的绝对查全。还需检查：
- 数据库主题检索发现但引文链没有发现的近期文献，尤其代码补全、Copilot、Codex 和 coding-agent 文献；
- 引文追溯发现但主题式没有命中的文献，并记录其缺失术语；
- 每次扩词后新增纳入文献数。当连续两轮扩词与双向追溯几乎不再产生独有纳入文献时，才可说明达到经验饱和。
## 七、与 AIS 顶级期刊综述实践的对应
以下不是单一强制模板，而是 MISQ、ISR、JAIS、JMIS 代表性综述反复出现的共同做法：
| 代表性论文 | 实际做法 | 对本项目的含义 |
|---|---|---|
| Webster & Watson (2002), MISQ | 数据库关键词检索后做后向参考文献和前向施引追溯；强调以概念组织综述、合理界定边界 | 不能只靠一个关键词式或只按作者逐篇罗列 |
| Cram, D’Arcy & Proudfoot (2019), MISQ | 明确检索截止日期；检索 ABI/INFORM、ACM DL、Business Source Premier、JSTOR；不限制期刊；另搜 AIS 会议、学位论文和未发表研究；双向追溯；报告每阶段数量、纳排标准和排除示例 | 保存检索日志、流量表、排除理由，来源范围需与研究问题匹配 |
| Eisend (2019), ISR | 从既有综述及其施引文献出发，同时检索多个数据库，再检查每篇参考文献；纳入多种发表类型；双人编码 | 种子、数据库检索和引文追溯应联合，而不是相互替代 |
| Diederich et al. (2022), JAIS | 为跨 IS/CS 的新兴主题，同时选 Basket、HCI 期刊、IS/CS 会议；使用 Web of Science、AISeL、ACM DL 和来源网站；公开精确查询、两次检索日期、初检数和最终数，并做双向追溯 | 编程智能体主题同样必须跨 IS、SE、HCI 和计算机教育 |
| Larsen et al. (2019), JAIS | 区分“研究边界识别”和“最终语料构建”，证明常规关键词加有限引文追溯可能漏掉大量隐性相关研究 | 需保留引文网络验证，并对模型排除项抽样审计 |
| Qahri-Saremi & Montazemi (2019), JMIS | 采用 PRISMA 思路，检索多个数据库，预先规定纳入标准，两位作者独立筛选并逐步报告 597→167→137→79 等数量变化 | 本项目应生成可复核的筛选流程图和逐阶段数量 |
| Leidner (2018), JAIS | 对 assessing review，透明、可复核的检索和编码提升结论可信度；但顶级综述最终仍要有理论组织、解释或理论发展 | 检索做到系统只是底线，最终贡献不能停留在文献清单 |
JAIS 当前的 Literature Reviews 栏目也明确偏好“用理论组织一个或多个研究流并提出战略研究平台”或“由综述发展/拓展理论”，而不是只做描述、制图或范围综述。因此，本项目的最终综合宜围绕“编程活动 × 人—AI 配置 × 认知/情境意识机制 × 结果”形成理论化框架，而不是只统计工具、方法和变量。
## 八、建议冻结的正式方案
推荐冻结以下方案作为正式检索协议：
1. 无起始年份，检索截止日单独记录；标题、摘要、关键词字段。
2. Scopus A—D 为主检索，Web of Science 为独立复检，ACM DL、IEEE Xplore、AISeL 为领域补充。
3. 不以 Basket 或 AIS 限制主语料；另报告 Basket、AIS、SE、HCI、CS 教育、AI 等来源层。
4. 20 篇种子、所有最终纳入文献和相关综述均做前向、后向追溯。
5. DeepSeek 做高召回题录筛选和全文结构化编码，人负责全部正例/不确定项的最终纳入判断，并抽查负例。
6. 保存精确检索式、检索日期、数据库、原始导出、去重规则、逐阶段数量、排除理由、模型版本、提示词和人工改判。
7. 投稿前更新检索并追加，而不是覆盖第一次检索结果。
## 参考入口
- MISQ：Webster & Watson (2002), [Analyzing the Past to Prepare for the Future](https://misq.umn.edu/skin/frontend/default/misq/pdf/TheoryReview/GuestEd.pdf)
- JAIS：Larsen et al. (2019), [Understanding the Elephant](https://aisel.aisnet.org/jais/vol20/iss7/15/)
- JAIS：Diederich et al. (2022), [On the Design of and Interaction with Conversational Agents](https://aisel.aisnet.org/jais/vol23/iss1/9/)
- JAIS：[Manuscript Categories and Information for Authors](https://aisel.aisnet.org/jais/authorinfo.html)
- Scopus：[Search syntax and proximity operators](https://service.elsevier.com/app/answers/detail/a_id/34325/supporthub/scopus/kw/wildcards/)
## 本地核对全文
- `database_fulltext_all/12802_2019_seeing-the-forest-i-and-i-the-trees-a-meta-analysis-of-the-antecedents-to-information-security-p.md`
- `database_fulltext_all/00350_2019_explaining-digital-piracy-a-meta-analysis.md`
- `database_fulltext_all/11232_2022_on-the-design-of-and-interaction-with-conversational-agents-an-organizing-and-assessing-review-o.md`
- `database_fulltext_all/12268_2019_understanding-the-elephant-the-discourse-approach-to-boundary-identification-and-corpus-construc.md`
- `database_fulltext_all/12278_2019_factors-affecting-the-adoption-of-an-electronic-word-of-mouth-message-a-meta-analysis.md`
