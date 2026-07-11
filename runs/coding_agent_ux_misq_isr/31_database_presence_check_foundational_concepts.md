# 基础概念 database 存在性检验

## 1. 检索目的

这次只回答一个问题：

> `collaborative overload` 是否是我们的 Top11 database 中真实出现过的权威基础概念？

结论很明确：

> **不是。**

`collaborative overload` 和 `collaboration overload` 在 `database/ALL_AIS_Basket_11.csv` 中精确命中为 0。因此，如果我们坚持“基础概念必须来自权威文献中真实使用过的概念”，就不能继续以 collaborative overload 作为基础概念。

## 2. 检索范围

数据源：

`database/ALL_AIS_Basket_11.csv`

检索字段：

- Title
- Abstract
- Author Keywords
- Index Keywords

同时也用 `rg --fixed-strings` 对整个 CSV 做了补充检查。

## 3. 精确命中结果

| 检索词 | 记录数 | 判断 |
| --- | ---: | --- |
| collaborative overload | 0 | 不可作为 database-supported 基础概念 |
| collaboration overload | 0 | 不可作为 database-supported 基础概念 |
| collaborative over-load | 0 | 不可作为 database-supported 基础概念 |
| collaboration over-load | 0 | 不可作为 database-supported 基础概念 |
| collaborative burden | 0 | 不可作为基础概念 |
| collaboration burden | 0 | 不可作为基础概念 |
| collaborative effort | 7 | 有表达，但不是成熟基础构念 |
| collaboration effort | 1 | 有表达，但不是成熟基础构念 |

因此，`30_single_foundational_concept_collaborative_overload.md` 不能继续作为当前有效主文档。

## 4. database 中真实存在的相邻 overload/effort 概念

| 概念 | 记录数 | 代表文献 | 初步判断 |
| --- | ---: | --- | --- |
| information overload | 80 | 多篇 DSS / I&M / MISQ / ISR 文章 | 最权威、最稳定，但可能过于偏“信息量” |
| technostress | 47 | 2011 MISQ `Technostress: Technological antecedents and implications`；2024/2025 多篇综述和扩展 | 很权威，但过宽，容易变成一般技术压力 |
| cognitive load | 39 | 多篇 DSS / MISQ / I&M 文章 | 个体层稳定概念，但过于一般心理认知负荷 |
| effort expectancy | 17 | UTAUT / adoption 相关文献 | 权威，但更像技术接受前因，不适合描述负向使用体验 |
| work overload | 9 | 2011 MISQ technostress 等 | 个体层，但偏工作情境压力，coding-agent 特异性弱 |
| interruption overload | 3 | 2018 MISQ `Life interrupted`；2020 JSIS；2023 I&M | 适合解释 approval/notification，但太窄 |
| ICT-mediated overload | 1 | 2023 I&M `The duality of ICT-mediated overload` | 命中少，但概念范围最接近“由技术中介造成的信息/中断过载” |
| digital overload | 1 | 2021 I&M `Absorbed in technology but digitally overloaded` | 有命中，但更偏平台工作与 burnout |
| user effort | 4 | 2022 I&M recommendation agent；2023 DSS dialogue agent | 有人-agent effort 线索，但不是 overload 基础概念 |
| perceived effort | 6 | 多篇 I&M / ISR / DSS | 表达存在，但不是清晰基础构念 |

## 5. 关键代表文献

### 5.1 ICT-mediated overload

**The duality of ICT-mediated overload: Its nature and consequences**  
2023, *Information and Management*  
DOI: `10.1016/j.im.2023.103864`

摘要要点：

- 研究 multiple ICTs 使用带来的 overload；
- 明确关注 overload 如何影响 **individual productivity**；
- 将 ICT-mediated overload 区分为 congruent 和 incongruent 类型；
- 基于 transactional theory of stress；
- 通过 cognitive appraisals 和 coping responses 解释生产率影响。

初步判断：

> 这是目前 database 中最接近我们问题的单一基础概念候选，因为它是 individual-level、technology-mediated、overload-oriented，并且包含 information overload 和 interruption overload 的整合思路。

不足：

> 它在 database 中只有 1 条精确命中，不如 information overload 和 technostress 稳定。

### 5.2 Information overload

`information overload` 在 database 中有 80 条记录。代表文献包括：

- **ONLINE REVIEWS AND INFORMATION OVERLOAD: THE ROLE OF SELECTIVE, PARSIMONIOUS, AND CONCORDANT TOP REVIEWS** (2022, MISQ)
- **The marketing effects of live streaming in online marketplaces** (2026, I&M)
- 多篇 recommender systems、online reviews、decision support 相关研究

初步判断：

> 如果我们最看重“概念成熟度”和“权威文献中反复使用”，information overload 是最稳的单一基础概念。

不足：

> 它主要描述信息过多导致处理困难。Coding agent 的痛点不仅是信息多，还包括 agent 自主行动、权限交还、代码状态变化、验证和接管。因此，如果以 information overload 为基础，新构念必须非常清楚地说明为什么 coding agent 中的信息过载不只是“信息量太多”，而是 agentic process/code-state information overload。

### 5.3 Interruption overload

`interruption overload` 在 database 中有 3 条记录。代表文献包括：

- **Life interrupted: The effects of technology-mediated work interruptions on work and nonwork outcomes** (2018, MISQ)
- **Worker stress in the age of mobile technology: The combined effects of perceived interruption overload and worker control** (2020, JSIS)
- **The duality of ICT-mediated overload: Its nature and consequences** (2023, I&M)

初步判断：

> 它可以解释 approval fatigue、permission handoff 和频繁通知。

不足：

> 太窄，只能覆盖 coding agent 体验中的审批/打断部分，不能覆盖看不懂 diff、验证负担、行动追踪和接管修复。

### 5.4 Technostress

`technostress` 在 database 中有 47 条记录。代表文献包括：

- **Technostress: Technological antecedents and implications** (2011, MISQ)
- **DECONSTRUCTING TECHNOSTRESS** (2024, MISQ)
- **Stress from Digital Work: Toward a Unified View of Digital Hindrance Stressors** (2025, ISR)

初步判断：

> 它非常权威，而且 individual-level 很明确。

不足：

> 它太宽。若以 technostress 为基础，我们很容易变成开发一个“coding-agent technostress”量表，这会削弱 coding agent 独特性，也容易被 reviewer 认为只是旧压力构念的场景化。

## 6. 当前判断

`collaborative overload` 不应继续使用。

如果严格要求“基础概念必须在 database 中被权威文献真实使用过”，当前最可能的单一基础概念有两个：

### 选择 A：information overload

优点：

- database 命中最多；
- 概念成熟；
- 个体层处理困难明确；
- 适合模仿 Chen et al. 的“成熟基础概念 + 新交互情境”写法。

缺点：

- 太偏信息处理；
- 需要把 coding agent 的独特性写成 agent-generated process/code-state information，而不是一般信息量。

可能新构念：

> **coding-agent process information overload**

### 选择 B：ICT-mediated overload

优点：

- database 中真实存在；
- individual-level；
- technology-mediated；
- overload-oriented；
- 比 information overload 更能覆盖信息过载 + 中断过载；
- 更接近 coding agent 的 approval、process feedback、multi-step action、code-state update。

缺点：

- database 只有 1 条精确命中；
- 不如 information overload 成熟。

可能新构念：

> **coding-agent-mediated overload**

## 7. 我的建议

如果最看重“权威文献反复使用、基础概念稳定”，应选：

> **information overload**

如果最看重“和 coding agent 现象贴合，同时仍然 database-supported”，应选：

> **ICT-mediated overload**

我目前更倾向于第二个：

> **ICT-mediated overload → coding-agent-mediated overload**

原因是它比 information overload 更容易容纳 coding agent 的权限交还、过程反馈和中断特征；同时它仍然是 database 中真实出现的 individual-level overload 概念。

但这个选择需要谨慎：下一步必须精读 2023 I&M 的 `The duality of ICT-mediated overload`，确认它的定义、维度和测量是否能支撑我们模仿 Chen et al. 的概念开发逻辑。

