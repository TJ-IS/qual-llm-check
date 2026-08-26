# 直接编程情境文献综述：备选检索方案

## 1. 已确定的研究边界

本综述关注的“编程情境”定义为：

> 人或具有生成式、交互式或自主能力的智能体，直接编写、生成、补全、理解、检查、审查、调试、修改或测试程序。

这里的“程序”包括：

- 通用编程语言的源代码；
- 可执行的数据库查询（如 SQL）；
- 电子表格中的公式、脚本与其他可执行逻辑；
- 终端用户编程、低代码或可视化编程环境中产生的可执行逻辑。

代码补全属于核心范围，因为它直接参与程序生成或修改。为了保留不同研究对象之间的差异，纳入论文后再标记为：

- `human_only`：人直接完成编程任务；
- `human_ai`：人和代码助手或编程智能体协作；
- `agent_only`：智能体直接生成、补全、检查、调试、修改或测试代码，研究主要评价智能体的行为或产出；
- `boundary_artifact`：只分析既有代码制品、仓库或项目，没有观察人或智能体实施上述行为，作为边界文献暂存而不进入核心综合。

下列内容不因出现 coding、programming 或 software development 就自动纳入：

- 质性研究中的开放编码、轴心编码等资料编码；
- 数学规划、线性规划、基因编码、医学编码和通信编码；
- 一般软件使用、采纳或数字化工作；
- 只研究开发团队、项目管理、敏捷组织或软件公司绩效；
- 只研究仓库网络、代码规模、复杂度或演化，而不研究人或智能体的直接编程行为；
- 传统编译器、静态分析器或测试工具的纯算法论文，除非研究将其明确视为执行编程工作的智能体，或评价它与程序员的交互。

对于纯代码补全、程序修复或代码生成算法论文，第一轮不直接排除，而是标为 `agent_only` 或 `boundary_artifact`，在全文阶段判断它研究的是“智能体从事编程”还是仅优化一个脱离编程情境的模型指标。

## 2. 检索词块

### Q1：高辨识度的直接编程行为

适合用于不限来源的标题检索。

```text
"program comprehension" OR "code comprehension" OR
"programming task*" OR "coding task*" OR
"pair programming" OR "test-driven development" OR
"end-user programming" OR
"AI-assisted programming" OR "AI-assisted coding" OR
"coding agent*" OR "programming agent*" OR
"programming assistant*" OR "coding assistant*" OR "code assistant*" OR
"code completion" OR "code autocompletion" OR "code autocomplete" OR
"code suggestion*" OR
"code review" OR "code inspection" OR
"writing code"
```

### Q2：扩展的直接编程行为

适合在预先限定的权威期刊或会议集合内检索题名、摘要和关键词。它比 Q1 更宽，必须经过语义筛选。

```text
"computer program*" OR "source code" OR
"program comprehension" OR "code comprehension" OR
programmer* OR "software developer*" OR
"programming task*" OR "coding task*" OR debugging OR
"pair programming" OR "test-driven development" OR
"end-user programming" OR
"spreadsheet programming" OR "spreadsheet development" OR
"spreadsheet debugging" OR "spreadsheet testing" OR
"spreadsheet error correction" OR
"query formulation" OR "query development" OR "SQL query" OR
"instantiation of data model*" OR "instantiations of data model*" OR
"AI-assisted programming" OR "AI-assisted coding" OR
"coding agent*" OR "programming agent*" OR
"programming assistant*" OR "coding assistant*" OR "code assistant*" OR
"code generation" OR "code completion" OR
"code autocompletion" OR "code autocomplete" OR "code suggestion*" OR
"code review" OR "code inspection" OR "code modification" OR
"writing code"
```

### Q3：现代编程助手与智能体补充词块

该词块单独运行，以免现代文献因为不用传统的 programmer、programming task 等词而漏检。

```text
"AI-assisted programming" OR "AI-assisted coding" OR
"AI pair programmer*" OR
"coding agent*" OR "programming agent*" OR
"coding assistant*" OR "programming assistant*" OR "code assistant*" OR
"code completion" OR "code autocompletion" OR "code autocomplete" OR
"code suggestion*" OR
"GitHub Copilot" OR "OpenAI Codex" OR
(
  ("large language model*" OR LLM* OR "generative AI" OR ChatGPT)
  W/8
  (programming OR coding OR "source code" OR "code generation" OR
   "code completion" OR debugging OR "program repair" OR "test generation")
)
```

### Q4：容易漏检的具体活动补充词块

该词块不单独决定纳入，只用于敏感性搜索。

```text
"program repair" OR "automated program repair" OR
"bug fixing" OR "fault localization" OR
"test generation" OR "unit test generation" OR
"API learning" OR "API usage" OR
"program synthesis" OR
"low-code development" OR "visual programming" OR
"spreadsheet formula*" OR
"SQL query formulation"
```

## 3. 方案 A：Basket 11 核心方案

### 检索范围

仅检索 AIS Senior Scholars' Basket 11 期刊，使用本地 Otero/Basket 元数据与全文库。

### 检索方式

- 题名、摘要、作者关键词、索引关键词运行 `Q2`；
- 另运行 `Q3`，捕捉编程智能体和代码补全；
- 所有候选进入 DeepSeek 全文筛选。

### 已知规模

- Basket 元数据：17,745 条；
- `Q2` 命中：253 条；
- `Q2 + "open-source software development"` 命中：293 条；
- 扩展方案覆盖此前确认的 21/21 篇人类直接编程任务论文；
- 加入代码补全词后，当前 Basket 命中总量没有增加，表明新增收益主要会来自 Basket 之外。

### 适用的综述主张

“顶级 IS 期刊如何研究直接编程情境。”

### 优点与限制

- 优点：来源边界最清楚；已有几乎完整的本地全文；工作量最小；复现容易。
- 限制：会系统性遗漏软件工程、HCI、编程教育和新近编程智能体研究，不能据此声称覆盖整个编程研究领域。

## 4. 方案 B：AIS 学术共同体方案

### 检索范围

- Basket 11；
- ICIS、ECIS、AMCIS、PACIS；
- HICSS 单独列入并单独报告；
- 可选扩展：ACIS、CAIS 和其他 AIS eLibrary 期刊或会议。

### 检索方式

在 AIS eLibrary、Scopus 或会议元数据中运行 `Q2 + Q3`，题名、摘要和关键词均检索。

### 适用的综述主张

“IS 学术共同体如何研究人或智能体的直接编程活动。”

### 优点与限制

- 优点：比 Basket 更能捕捉新主题，因为会议论文通常早于期刊；仍具有清楚的学科边界。
- 限制：AIS eLibrary 的摘要和索引完整度不一致；仍会遗漏 ICSE、CHI、VL/HCC 等领域的主干研究。

## 5. 方案 C：IS–SE–HCI 权威来源方案

### 检索范围

第一层为方案 B 的全部来源，第二层预先固定以下邻近领域来源：

- 软件工程期刊：IEEE Transactions on Software Engineering、ACM Transactions on Software Engineering and Methodology、Empirical Software Engineering、Information and Software Technology、Journal of Systems and Software；
- 软件工程会议：ICSE、FSE、ASE、ESEM、ICPC、MSR、CHASE；
- 人机交互与人本编程：CHI、CSCW/PACMHCI、VL/HCC、ACM TOCHI、International Journal of Human–Computer Studies；
- 编程教育补充层：SIGCSE、ITiCSE、ACM Transactions on Computing Education、Computer Science Education。

最终来源名单应在正式检索前冻结，并在附录中给出来源全称、ISSN 或 Scopus Source ID。

### 检索方式

- 在限定来源内运行 `TITLE-ABS-KEY(Q2 OR Q3 OR Q4)`；
- Q4 命中必须经语义筛选，不能仅凭关键词纳入；
- 来源外的现代编程智能体研究通过方案 D 或 F 补充。

### 适用的综述主张

“权威 IS、软件工程和 HCI 来源中，直接编程研究形成了怎样的跨学科知识。”

### 优点与限制

- 优点：与研究问题的跨学科性质匹配；可避免不加限制地检索全部计算机科学来源。
- 限制：来源名单包含研究者判断；新兴智能体论文可能发表于 AI 会议、预印本或尚未稳定进入这些核心来源。

## 6. 方案 D：Scopus 全库高精度方案

### Scopus 检索式

```text
TITLE(
  "program comprehension" OR "code comprehension" OR
  "programming task*" OR "coding task*" OR
  "pair programming" OR "test-driven development" OR
  "end-user programming" OR
  "AI-assisted programming" OR "AI-assisted coding" OR
  "coding agent*" OR "programming agent*" OR
  "programming assistant*" OR "coding assistant*" OR "code assistant*" OR
  "code completion" OR "code autocompletion" OR "code autocomplete" OR
  "code suggestion*" OR
  "code review" OR "code inspection" OR "writing code"
)
AND (DOCTYPE(ar) OR DOCTYPE(cp) OR DOCTYPE(re))
AND LANGUAGE(english)
```

### 已知规模

加入代码补全词之前的 Q1 标题检索在 Scopus 命中 2,872 条。加入代码补全及其同义词后需要在正式检索日重新记录精确结果数，预计会有所增加。

### 适用的综述主张

“在 Scopus 收录范围内，对标题明确聚焦直接编程行为的研究进行跨学科检索。”

### 优点与限制

- 优点：不依赖主观来源名单；规模仍可用模型进行摘要初筛；适合作为来源限定方案的敏感性检验。
- 限制：标题没有明确写出编程行为的研究会漏检；代码补全可能带来大量纯算法论文。

## 7. 方案 E：Scopus 全库高召回方案

### Scopus 检索式

```text
TITLE-ABS-KEY(
  Q1 OR Q3 OR Q4
)
AND (DOCTYPE(ar) OR DOCTYPE(cp) OR DOCTYPE(re))
AND LANGUAGE(english)
```

实际运行时应展开 Q1、Q3、Q4，而不是把词块名称直接放入 Scopus。

### 已知规模

加入代码补全词之前，聚焦活动词的题名—摘要—关键词检索命中 13,133 条；无约束的 program/code/debugging/code generation 宽检索则达到 336,736 条，不适合作为筛选起点。

### 适用的综述主张

“在 Scopus 中尽可能广泛地发现直接编程研究。”

### 优点与限制

- 优点：来源和标题表述造成的漏检最少。
- 限制：需要对一万级记录进行机器辅助摘要筛选；纯算法、编程教育和一般软件工程噪声会明显增加；全文获取量也可能较大。

## 8. 方案 F：分层混合方案（推荐）

该方案不是把所有宽词一次性投向全库，而是让不同检索轨道承担不同的漏检风险。

### F1：IS 主干轨

- Basket 11 + AIS 主要会议；
- 运行 `Q2 + Q3`；
- 全部候选进入摘要筛选，疑似相关项进入全文筛选。

### F2：跨学科权威轨

- 使用方案 C 的固定 SE、HCI 和编程教育来源；
- 运行 `Q2 + Q3 + Q4`；
- 与 F1 通过 DOI、EID 和规范化题名去重。

### F3：全库敏感性轨

- 在 Scopus 全库运行方案 D 的标题检索；
- 单独运行 `TITLE-ABS-KEY(Q3)`，捕捉代码补全、Copilot、Codex、LLM 编程和编程智能体；
- 不对一般的 software development 使用全库宽检索。

### F4：引文追踪轨

- 对已有 20 篇高度相关种子文献做后向参考文献回溯和 Scopus 前向追引；
- 对新纳入的现代 `human_ai` 与 `agent_only` 核心论文继续追引；
- 每一条引文发现都执行同一纳入标准，不因引用种子论文而自动纳入；
- 连续两轮追引不再发现新的核心论文时停止，并记录停止规则。

### 为什么推荐 F

本地 83 篇正式文献综述的方法审计显示，2016 年以来的 44 篇综述中，21 篇使用混合检索、14 篇使用广泛数据库检索、9 篇只使用限定权威集合。已有 20 篇种子文献的 807 条 Scopus 引文中，Basket 或扩展 AIS 来源仅占 231 条（28.6%），其余 576 条（71.4%）来自外部来源。只做 Basket/AIS 会低估跨学科脉络，而直接运行一条极宽的全库检索式又会产生不可控噪声；分层混合方案能同时保留规范性和召回率。

## 9. 所有方案共用的筛选问题

DeepSeek 的题名摘要筛选和全文筛选均只做布尔判断与分类，不做评分。

### 核心判断

```text
这篇论文的研究对象或实证任务，是否直接包含人或具有生成式、交互式或自主能力的智能体对程序进行编写、生成、补全、理解、检查、审查、调试、修改或测试？
```

只有明确的全文证据才能返回 `true`。不能因为论文讨论软件开发、程序员、软件项目或代码仓库，就推断它研究了直接编程行为。

### 建议输出字段

```json
{
  "qualifies": true,
  "actor_type": "human_only | human_ai | agent_only",
  "program_artifact": "source_code | database_query | spreadsheet_logic | low_code_or_visual | other",
  "programming_actions": [
    "write",
    "generate",
    "complete",
    "understand",
    "inspect_or_review",
    "debug",
    "modify",
    "test"
  ],
  "research_focus_summary": "",
  "programming_context_definition": "",
  "method": "",
  "boundary_reason": "",
  "evidence": []
}
```

`qualifies=false` 时只需给出简短排除原因和证据；`boundary_artifact` 单独保存，便于以后扩大范围但不混入核心综合。

## 10. 正式执行与报告流程

1. 在检索前冻结：研究边界、来源集合、完整检索式、语言和文献类型限制。
2. 每个数据库或集合分别保存检索日期、原始命中数和原始导出文件。
3. 按 DOI、EID、规范化题名去重，同时保留每篇论文由哪条轨道发现。
4. DeepSeek 先做题名摘要筛选；不能确定的记录进入全文，不强制模型猜测。
5. DeepSeek 阅读全文后按统一问题判断，并抽取 actor、program artifact 和 programming action。
6. 人工复核全部纳入项、全部边界项，以及随机抽取的排除项。
7. 对纳入项执行前向和后向追引，再按同一标准筛选。
8. 输出 PRISMA 式计数：各轨命中、去重、摘要排除、全文排除、追引新增和最终纳入。
9. 结果综合时分别报告 `human_only`、`human_ai` 和 `agent_only`，避免把代码补全模型基准测试与程序员行为实验混为同一类证据。

## 11. 供选择的简表

| 方案 | 来源范围 | 已知起始规模 | 召回倾向 | 最合适的综述表述 |
|---|---|---:|---|---|
| A | Basket 11 | 293 | 较低 | 顶级 IS 期刊 |
| B | Basket + AIS 会议 | 待导出 | 中等 | IS 学术共同体 |
| C | AIS + 固定 SE/HCI/教育来源 | 待导出 | 中高 | 权威跨学科来源 |
| D | Scopus 全库、仅题名 | 至少 2,872 | 中等 | 全库高精度敏感性检索 |
| E | Scopus 全库、题名摘要关键词 | 至少 13,133 | 高 | 全库高召回 |
| F | A/B/C + D + 智能体专检 + 引文追踪 | 去重后待定 | 高 | 正式跨学科文献综述 |

当前建议采用 **F**。如果希望把工作量进一步压低，可采用 **B + D + Q3 + 引文追踪**；如果论文只准备对 IS 领域作出结论，则采用 **A 或 B** 即可，但必须在标题、摘要和方法中明确说明来源边界。

