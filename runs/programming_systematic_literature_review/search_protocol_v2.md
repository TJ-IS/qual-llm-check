# 人或智能体直接编程：有界权威来源系统综述与引文扩展协议 v2

## 研究边界

关注个人或智能体直接编写、生成、补全、理解、检查、调试、修改、重构或测试程序。程序包括源代码、SQL 等可执行查询、电子表格公式/脚本以及低代码、可视化或终端用户编程产生的可执行逻辑。编程必须是研究中不可替换的核心对象，而非软件项目、团队、组织或一般知识工作的背景。

## 检索渠道

1. **权威来源概念检索：** 2026-07-26 在 Scopus 的 TITLE-ABS-KEY 运行一条冻结的概念式，并用 source title 限定预先选择的 IS、SE、HCI、CS 教育权威期刊和会议。初始结果 4,981 条。
2. **施引补充：** 对 20 篇人工确认的核心种子运行 Scopus 正向施引检索，得到 807 条，不限制来源。
3. **本地种子保障：** 纳入本地全文复核得到的 28 条直接或边界编程研究记录，防止因老文献题录缺摘要、标题术语不同而漏失。
4. **最终参考文献回溯：** 对全文确认纳入的论文逐篇回溯参考文献；新增记录走同一初筛和全文标准。

## 覆盖范围声明

本协议把“边界识别”和“语料构造”分开。4,981 条主检索是预先指定的跨学科权威来源全集，不代表全球全部相关文献；807 条不受来源限制的施引记录用于扩展该边界。完整回溯尚未结束前，研究只能声称为“权威来源有界系统综述 + 种子引文扩展”，不得声称穷尽所有期刊、会议和灰色文献。这一限制依据 Larsen et al. (2019, JAIS) 对 top-journal-only corpus 的明确批评作出。

## 冻结的主概念式

```text
TITLE-ABS-KEY(
  "program comprehension" OR "software comprehension" OR "code comprehension" OR
  "program understanding" OR "code understanding" OR "code reading" OR
  "source code review" OR "code review" OR "code inspection" OR
  "program debugging" OR "code debugging" OR "program repair" OR
  "program modification" OR "software modification" OR "code modification" OR
  "code refactoring" OR "program testing" OR "code completion" OR
  "pair programming" OR "test-driven development" OR
  "programming task" OR "programmer problem solving" OR
  "query formulation" OR "query development" OR "query reuse" OR
  "end-user programming" OR "spreadsheet development" OR
  "spreadsheet error" OR "spreadsheet testing" OR
  "database learning" OR
  "AI-assisted programming" OR "AI coding assistant" OR "coding agent"
)
```

来源限定在 Scopus 的第二个 `AND` 字段中运行：

```text
"MIS Quarterly" OR "Information Systems Research" OR
"Journal of the Association for Information Systems" OR
"Journal of Management Information Systems" OR
"European Journal of Information Systems" OR
"Information Systems Journal" OR "Journal of Information Technology" OR
"Journal of Strategic Information Systems" OR "Information and Organization" OR
"Information and Management" OR "Decision Support Systems" OR
"IEEE Transactions on Software Engineering" OR
"ACM Transactions on Software Engineering and Methodology" OR
"Empirical Software Engineering" OR "Journal of Systems and Software" OR
"Information and Software Technology" OR "Software Quality Journal" OR
"ACM Transactions on Computer-Human Interaction" OR
"Computers in Human Behavior" OR
"International Journal of Human Computer Studies" OR
"Computer Science Education" OR "Computers and Education" OR
"Journal of Computer Assisted Learning" OR
"International Conference on Software Engineering" OR
"Human Factors in Computing Systems" OR
"Visual Languages and Human-Centric Computing" OR
"Technical Symposium on Computer Science Education" OR
"Innovation and Technology in Computer Science Education"
```

## 纳入与排除

题录初筛使用 `include_candidate / uncertain / exclude` 三档，以召回为优先。`include_candidate` 和 `uncertain` 均进入独立第二次判断；仍有分歧或信息不足者进入人工全文裁决。

纳入的必要条件：

1. 核心对象、任务、系统能力或理论问题直接涉及规定的编程活动；
2. 对象是人、人与生成式/学习式/自主智能体协作，或此类智能体本身；
3. 被操作的制品是可执行程序逻辑；
4. 编程不可被“一般知识工作”替换而不改变研究问题和主要结论。

排除软件项目/团队/组织一般结果、纯仓库网络或 commit 统计、纯代码结构度量、一般算法方法、其他含义的 programming/coding，以及不产生或操作可执行逻辑的一般系统设计和需求工程。

## 报告承诺

- 同时报告题录数、论文数和能够识别时的独立研究/样本数；
- 保存各渠道、去重、每阶段排除理由和引文新增数量；
- 报告模型、提示词版本、指纹、错误与重试；不把模型称为人类编码者；
- 全文编码形成 concept matrix：编程行动、主体、制品、方法、分析层级、理论、自变量、中介、调节、因变量、主要结论及与编程智能体研究的关系；
- 搜索在提交前至少更新一次，并记录更新日期。
