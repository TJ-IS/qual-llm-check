# 编程情境文献综述：检索来源调查与推荐方案
## 一句话建议
建议采用“混合式、双轨检索”，而不是只在 AIS/Basket 内检索，也不建议直接把一个很宽的检索式投向整个 Scopus 后人工筛选：
1. **领域权威轨**：在 AIS Basket 11、AIS 主要会议，以及一组事先声明的软件工程/HCI 核心来源内，用较高召回率的题名—摘要—关键词检索式检索。
2. **全库敏感性轨**：在 Scopus 全库只对题名使用更聚焦的编程活动词，获取可控规模的跨领域候选。
3. **引文补充轨**：对既有 20 篇种子、4 篇现代 LLM 桥梁论文和新纳入论文执行前向、后向追引。
这个设计既保留了“从可复现检索式出发”的正规流程，也避免因为把检索范围锁死在 Basket 而漏掉 CHI、ICSE、TSE、VL/HCC、ICPC 等现代编程研究。
## 对本地 AIS Basket 综述的实证调查
### 样本与方法
从本地 13,910 篇 AIS Basket Markdown 全文中，根据题名和摘要中的 systematic review、literature review、meta-analysis、bibliometric 等高置信度表达筛出 93 篇候选，再让 DeepSeek V4 Pro 阅读全文并审计其实际检索方法。模型必须区分：
- 书目数据库：Scopus、Web of Science、ABI/INFORM 等；
- 出版平台：ScienceDirect、Wiley Online Library 等；
- 数字图书馆：AIS eLibrary、ACM Digital Library、IEEE Xplore；
- 搜索引擎：Google Scholar；
- 限定期刊/会议集合：AIS Senior Scholars’ Basket、FT50、ICIS/ECIS/AMCIS 等；
- 前向、后向追引或其他补充手段。
93 篇候选全部处理成功，83 篇被确认为真正实施了文献综述或元分析，10 篇是题名/摘要规则造成的误候选。
### 检索策略分布
| 策略 | 83 篇全部综述 | 2016 年以来 44 篇 |
|---|---:|---:|
| 广泛数据库检索 | 29（34.9%） | 14（31.8%） |
| 混合式检索 | 29（34.9%） | 21（47.7%） |
| 限定权威期刊/会议集合 | 14（16.9%） | 9（20.5%） |
| 未充分说明 | 11（13.3%） | 0 |
| 仅依赖引文追引 | 0 | 0 |
现代综述的主要模式是混合式或广泛数据库检索。2016 年以来，35/44（79.5%）使用这两类方法；完全只做权威集合检索仍然存在，但不是多数。
### 实际使用的检索来源
下表计数表示“83 篇综述中，有多少篇明确把该来源用于构建或补充样本”。同一篇可以使用多个来源。
| 来源 | 类型 | 篇数 | 占 83 篇 |
|---|---|---:|---:|
| Citation chaining | 前后向追引 | 35 | 42.2% |
| ScienceDirect | 出版平台 | 28 | 33.7% |
| Web of Science | 书目数据库 | 23 | 27.7% |
| ABI/INFORM | 书目数据库 | 20 | 24.1% |
| Google Scholar | 搜索引擎 | 18 | 21.7% |
| AIS eLibrary | 数字图书馆 | 18 | 21.7% |
| Scopus | 书目数据库 | 16 | 19.3% |
| EBSCO | 书目数据库 | 13 | 15.7% |
| ACM Digital Library | 数字图书馆 | 13 | 15.7% |
| Business Source Premier | 书目数据库 | 12 | 14.5% |
| IEEE Xplore | 数字图书馆 | 11 | 13.3% |
| ProQuest Dissertations & Theses | 书目数据库 | 10 | 12.0% |
| JSTOR | 数字图书馆 | 9 | 10.8% |
流程层面，36 篇明确进行后向追溯，16 篇进行前向追引，20 篇进行逐刊或逐会议手工检查。
### “权威文献集合”到底有哪些
12 篇综述明确把 AIS Senior Scholars’ Basket 作为限定集合，其中 1 篇在 Basket 外额外加入 Decision Support Systems。其他常见做法不是照搬某一个固定清单，而是根据研究的跨学科边界构造组合集合，例如：
- AIS Basket + 主要 AIS 会议；
- AIS Basket + HCI 核心期刊 + CHI；
- AIS Basket + FT50 + 管理学/创业领域期刊；
- 特定顶级 IS 期刊集合；
- 学科评级清单中的期刊和会议。
这说明“先声明一个权威集合，再在集合内运行检索式”是完全被 Basket 综述接受的做法；但跨学科主题通常还会增加数据库检索或邻近学科来源。
## 与我们最相似的既有做法
### 1. 只限定顶级 IS 期刊
**Synthesizing Information Systems Knowledge: A Typology of Literature Reviews**（2015）手工浏览 I&M、ISR、JAIS、JMIS、MISQ 五本期刊在 1999–2013 年间的文章，初始得到 146 篇，最终纳入 139 篇。这是最纯粹的“权威期刊集合”设计。
本地全文：[00752_2015_synthesizing-information-systems-knowledge-a-typology-of-literature-reviews.md](review_fulltexts/00752_2015_synthesizing-information-systems-knowledge-a-typology-of-literature-reviews.md)
### 2. Basket 作为核心，再用数据库覆盖集合外高影响文献
**Getting Value from Business Intelligence Systems: A Review and Research Agenda**（2017）先限定 Basket of Eight + DSS，再用 ProQuest、EBSCO、ScienceDirect、ABI/INFORM、Wiley 等检索；Basket/DSS 以外的论文用 Scopus 引用数 ≥25 作为补充门槛。初始 738 篇，最终纳入 106 篇。
本地全文：[00670_2017_getting-value-from-business-intelligence-systems-a-review-and-research-agenda.md](review_fulltexts/00670_2017_getting-value-from-business-intelligence-systems-a-review-and-research-agenda.md)
### 3. 数据库检索 + Basket 手工检查 + 前后向追引
**Cyberbullying on Social Networking Sites**（2021）同时检索 Academic Search Complete、PsycINFO、Web of Science、Scopus，手工检查 Basket of Eight，再做前向和后向追引；由 420 条候选得到 56 篇。
本地全文：[20291_2021_cyberbullying-on-social-networking-sites-a-literature-review-and-future-research-directions.md](review_fulltexts/20291_2021_cyberbullying-on-social-networking-sites-a-literature-review-and-future-research-directions.md)
### 4. 为跨 IS/CS 主题专门建立领域组合
**On the Design of and Interaction with Conversational Agents**（JAIS 2022）使用 Basket of Eight、四本 CS/HCI 期刊、ICIS/ECIS/HICSS/AMCIS/PACIS 和 CHI；通过 Web of Science、AIS eLibrary、ACM Digital Library 与来源网站检索，再进行前后向追引。初始 8,768 条，最终纳入 262 篇。
本地全文：[11232_2022_on-the-design-of-and-interaction-with-conversational-agents-an-organizing-and-assessing-review-o.md](review_fulltexts/11232_2022_on-the-design-of-and-interaction-with-conversational-agents-an-organizing-and-assessing-review-o.md)
这篇与我们的情境最相似：编程智能体同样横跨 IS、HCI 和计算机科学，不能只依赖 Basket。
### 5. 全库检索 + 权威集合验证 + 引文追踪
**Socio-technical Phenomena Involving Blockchain Use**（JSIS 2025）先在 Web of Science、Scopus、ScienceDirect 检索，再限定/核验 FT50、AIS Basket、AIS 会议、WWW、CHI，并进行前后向追引和专家补充；由 61,902 条初始记录得到 234 篇。
本地全文：[16429_2025_socio-technical-phenomena-involving-blockchain-use-literature-review-conceptual-framework-and-re.md](review_fulltexts/16429_2025_socio-technical-phenomena-involving-blockchain-use-literature-review-conceptual-framework-and-re.md)
它证明初始检索结果很大并不自动破坏正规性，但要求清楚报告自动去重、初筛和排除流程。
## 我们的候选检索式在 Basket 内是否可行
在本地 17,745 条 Basket 11 Scopus 元数据的题名、摘要、作者关键词和索引关键词中，使用以下概念组：
```text
"computer program*" OR "source code" OR
"program comprehension" OR "code comprehension" OR
programmer* OR "software developer*" OR
"coding task*" OR "programming task*" OR debugging OR
"pair programming" OR "test-driven development" OR
"end-user programming" OR
"spreadsheet programming" OR "spreadsheet development" OR
"spreadsheet debugging" OR "spreadsheet testing" OR
"spreadsheet error correction" OR
"query formulation" OR "query development" OR "SQL query" OR
"instantiation of data model*" OR "instantiations of data model*" OR
"AI-assisted programming" OR "AI-assisted coding" OR
"coding agent*" OR "programming assistant*" OR
"code generation" OR "code review" OR "code inspection" OR
"code modification" OR "writing code"
```
得到：
| 指标 | 结果 |
|---|---:|
| Basket 11 元数据总数 | 17,745 |
| 检索命中 | 253 |
| 已有本地全文 | 230 |
| 2016 年以来 | 31 |
| 2021 年以来 | 17 |
该检索式还能覆盖之前人工/DeepSeek 确认的 28 篇“直接研究编程”中的 23 篇（82.1%），以及其中 21 篇有人类编程任务的论文中的 20 篇（95.2%）。唯一漏掉的人类任务论文研究开放源码软件的核心—边缘结构；其余漏检主要是软件复杂度、软件演化等代码制品分析，而不是个人执行编程任务。
因此，如果研究问题最终聚焦于“个人如何编写、理解、检查、调试或委托生成代码”，这组检索词在 Basket 内已经具有很好的已知样本召回率。
## 完全广泛地检索会有多大
2026 年 7 月 26 日在已登录 Scopus 中进行了三个只读规模测试：
| 范围 | 命中数 |
|---|---:|
| 较宽的编程/code/debugging/code generation 等词，题名/摘要/关键词 | 336,736 |
| 聚焦的编程活动词，题名/摘要/关键词 | 13,133 |
| 同一组聚焦词，仅限题名 | 2,872 |
聚焦题名检索的 2,872 条中，Computer Science 2,419 条；Conference paper 1,942 条，Article 730 条。主要来源是 LNCS 121、ICSE Proceedings 110、IEEE ICPC 97、ACM Proceedings 96、Empirical Software Engineering 76。2023–2026 四个年份已有 717 条。
因此：
- 336,736 条不可作为人工筛选起点；
- 13,133 条可以做机器辅助摘要筛选，但仍然偏大；
- 2,872 条适合成为“跨领域敏感性检索”，先对题名/摘要批量筛选，再下载少量全文。
## 推荐的正式检索协议
### 轨道 A：权威集合内高召回检索
集合建议分三层，所有层都在方案中事先声明：
1. **IS 期刊核心**：本地 AIS Basket 11。
2. **AIS 会议核心**：ICIS、AMCIS、ECIS、PACIS；ACIS 可作为地区扩展，HICSS 单列但建议纳入。
3. **编程/HCI 核心扩展**：根据本次 Scopus 来源分布和 JAIS conversational-agent 综述，至少考虑 ICSE、ICPC、CHI、VL/HCC、ESEM、IEEE TSE、Empirical Software Engineering、Information and Software Technology、Journal of Systems and Software。最终清单应在检索前固定。
在这些来源内运行上面的完整题名—摘要—关键词检索式。Basket 内预计 253 条，规模很小，可以全部进入自动初筛。
### 轨道 B：Scopus 全库题名敏感性检索
使用经过实测的聚焦题名检索：
```text
TITLE(
  "program comprehension" OR "code comprehension" OR
  "programming task*" OR "coding task*" OR
  "pair programming" OR "test-driven development" OR
  "end-user programming" OR
  "AI-assisted programming" OR "AI-assisted coding" OR
  "coding agent*" OR "programming assistant*" OR
  "code review" OR "code inspection" OR "writing code"
)
```
当前命中 2,872 条。可先限制为 Article、Conference paper、Review 和 English，再让 DeepSeek 对题名与摘要判断是否真正研究编程活动。该轨用于发现没有进入 IS 权威集合的现代软件工程/HCI 文献。
### 轨道 C：引文追引
对以下文献集分别做：
- 已有 20 篇直接编程种子；
- 已识别的 Ivie、Follow-Up Attention、DevTales、Evaluating Logical Structure 四篇现代桥梁；
- 轨道 A/B 最终纳入的所有核心论文。
执行参考文献回溯与 Scopus 前向追引，并记录“由哪一篇种子、哪一种追引方式发现”。追引发现的论文仍需满足同一纳入标准，不因被核心论文引用就自动纳入。
## 建议的筛选边界
为了避免 13,133 条中混入大量项目管理和组织研究，建议把核心纳入条件定义为：
> 论文的研究对象必须直接包含人类或智能体对可执行代码、查询、电子表格逻辑或其他程序制品的编写、生成、理解、检查、调试、修改、测试或协同完成；仅研究软件项目、开发团队、开发组织、敏捷管理、软件公司绩效或代码仓库宏观结构，不自动视为个人编程情境。
可以把纯代码制品分析设为邻近类别，而不是完全丢弃。这样既符合你之前对“正经研究编程这件事本身”的要求，也能在需要时讨论自动化代码分析。
## 正式报告时应保存的审计信息
每个数据库/集合都应保存：
1. 检索日期、数据库版本和完整检索式；
2. 来源限制、年份、语言和文献类型；
3. 原始命中数、导出数、去重数；
4. 题名摘要排除数、全文排除数及排除理由；
5. 前向/后向追引新增数；
6. DeepSeek 模型名、提示词版本、温度、批处理脚本与失败重试记录；
7. 一个人工复核样本，至少覆盖所有纳入项和随机抽取的排除项；
8. 最终 PRISMA 式流程图或等价流程表。
DeepSeek 可以承担初筛和结构化抽取，但正式综述中应把它表述为机器辅助筛选，并保留人工审计与可重复的原始检索集合。
## 需要确认的范围决定
在真正开始检索前，只需要确定两点：
1. 核心范围是否采用“个人/智能体直接编程活动”，将纯代码制品分析和组织级软件开发列为邻近类别；
2. 权威集合是否采用推荐的三层结构（Basket 11 + AIS 会议 + 核心 SE/HCI 来源），还是先只做 Basket 11 与 AIS 会议。
如果采用推荐方案，下一步可以直接生成各平台的正式检索式、来源清单和 PRISMA 计数目录，然后开始导出与去重。
