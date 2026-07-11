# 外部文献使用量审查：workspace awareness 是否太小众

## 1. 为什么需要这次审查

`workspace awareness` 在我们的 Top11 IS database 中只有 1 篇精确命中：

- Cooper and Haines (2008), **The Influence of workspace awareness on group intellective decision effectiveness**, *European Journal of Information Systems*.

这个数量太少，不能直接断言它适合作为概念开发的基础。这里补做外部学术网络检索，检验它是不是一个被广泛使用、至少有稳定引用链的基础概念。

结论先写在前面：

> `workspace awareness` 不是无人使用，也不是随便造出来的词；它在 CSCW/HCI 中有清楚定义、经典文献和可观引用。  
> 但它确实是一个相对小众、领域集中的概念。若我们要求基础概念必须有更强主流文献地基，**不应把 workspace awareness 作为唯一基础概念**。  
> 更稳妥的基础概念应改为 **situation awareness**，然后开发 coding-agent-specific 的 **coding-agent work-situation awareness / 编码代理工作情境觉察**。

## 2. 检索方式

### 2.1 Top11 database

检索文件：`database/ALL_AIS_Basket_11.csv`  
检索字段：`Title`, `Abstract`, `Author Keywords`, `Index Keywords`

### 2.2 外部学术索引

使用 OpenAlex API 做 title-level 检索。因为 Crossref 的 `query.title` 和一般搜索容易把短语拆成宽泛关键词，本次不采用 Crossref 的总量数字作为结论依据。

OpenAlex 检索方式：

- `filter=title.search:<concept>`
- 再对可抓取结果做标题精确短语检查，例如标题中是否真的包含 `workspace awareness`。

Semantic Scholar API 本次返回 `429 Too Many Requests`，不作为数量证据。

## 3. 外部使用量对比

OpenAlex title-level 检索显示：

| 概念 | OpenAlex title.search 数量 | 已抓取结果中的精确标题短语数量 | 初步解释 |
| --- | ---: | ---: | --- |
| workspace awareness | 145 | 74 | 小众但稳定，有经典 CSCW/HCI 文献 |
| situation awareness | 11,566 | 未全量抓取 | 大规模成熟概念 |
| mutual understanding | 1,346 | 943 | 使用很多，但跨学科且含义分散 |
| shared understanding | 3,196 | 888 | 使用很多，但跨学科且较宽 |
| common ground | 7,295 | 未全量抓取 | 大规模成熟概念，偏沟通/语言/协作 |
| transactive memory system | 509 | 497 | 成熟团队认知概念，测量强 |
| shared mental model | 795 | 649 | 成熟团队认知概念，测量强 |
| teamwork quality | 454 | 115 | 成熟但更像协作结果评价 |
| algorithmic transparency | 733 | 未全量抓取 | AI/算法治理与使用中成熟增长 |
| explainable AI | 13,900 | 未全量抓取 | 大规模 AI/XAI 文献 |

这个结果说明：

- `workspace awareness` 的外部文献使用量并不是 0，也不是个位数；
- 但它和 `situation awareness`、`common ground`、`shared understanding`、`explainable AI` 这种主流概念不是同一量级；
- 它更像一个 CSCW/HCI 内部清晰、但在 IS 主流期刊中使用较少的专门概念。

## 4. workspace awareness 的外部引用链

OpenAlex 中 `workspace awareness` title-level 结果的高引用文献包括：

| 标题 | 年份 | 来源 | OpenAlex cited_by | DOI |
| --- | ---: | --- | ---: | --- |
| Awareness and coordination in shared workspaces | 1992 | CSCW | 2503 | 10.1145/143457.143468 |
| A Descriptive Framework of Workspace Awareness for Real-Time Groupware | 2002 | Computer Supported Cooperative Work | 1151 | 10.1023/A:1021271517844 |
| Workspace Awareness in Real-Time Distributed Groupware: Framework, Widgets, and Evaluation | 1996 | HCI/CSCW proceedings | 330 | 10.1007/978-1-4471-3588-3_18 |
| The effects of workspace awareness support on the usability of real-time distributed groupware | 1999 | ACM Transactions on Computer-Human Interaction | 259 | 10.1145/329693.329696 |
| Support for workspace awareness in educational groupware | 1995 | CSCL | 243 | 10.3115/222020.222126 |
| Workspace awareness for groupware | 1996 | CHI companion | 203 | 10.1145/257089.257284 |
| Empirical evidence of the benefits of workspace awareness in software configuration management | 2008 | software engineering / CSCW | 63 | 10.1145/1453101.1453118 |

这说明 `workspace awareness` 至少有三个优点：

1. **不是自造词**：有经典定义和持续引用。
2. **和协作工具强相关**：特别是 groupware、shared workspace、software configuration management。
3. **和我们的现象很贴**：它本来就关心“别人正在共享工作空间里做什么、在哪里做、为什么做”。

但它也有两个硬伤：

1. **文献规模偏小**：OpenAlex title.search 145，精确标题 74；和 situation awareness 的 11,566 不在一个量级。
2. **领域集中**：主要在 CSCW/HCI，不是 IS Top11 的高频基础概念。

## 5. 与其他候选的对比判断

### 5.1 为什么不能继续把 workspace awareness 作为首选基础概念

如果我们要写的是 HCI/CSCW 论文，`workspace awareness` 很可能是非常好的基础概念。

但我们的目标更像 IS 概念开发和量表开发，需要一个足够稳的基础概念。`workspace awareness` 在 Top11 database 中只有 1 篇，外部也主要局限于 CSCW/HCI；这会带来风险：

- 审稿人可能认为基础概念太窄；
- 它没有 `situation awareness` 那样成熟的测量传统；
- 它较难支撑一个面向 broader IS audience 的概念开发论文；
- 我们会花很多篇幅证明这个基础概念本身的重要性，而不是证明 coding agent 情境为什么需要迁移。

所以，经外部检索后，我不建议再把 `workspace awareness` 作为唯一基础概念。

### 5.2 为什么 situation awareness 更稳

`situation awareness` 的优势很明显：

- Top11 database 中有 16 篇相关记录；
- OpenAlex title.search 数量约 11,566；
- 有经典三层定义：perception、comprehension、projection；
- 有成熟测量方式：SAGAT、SART、real-time probes、behavioral/performance measures；
- IS 文献已经把它用于 phishing、DSS dashboard、cybersecurity、emergency response、smart activity monitoring 等动态任务情境；
- 它天然适合解释 out-of-the-loop problem、automation、decision support 和 human oversight。

最重要的是，coding agent 使用本质上就是动态任务情境：

- agent 改代码；
- agent 运行命令；
- agent 生成 diff；
- agent 请求审批；
- agent 使代码库状态持续变化；
- 用户需要感知、理解并预测这些变化，才能审批、监督、纠偏和接手。

这与 situation awareness 的经典定义高度一致。

## 6. 新建议：以 situation awareness 为唯一基础概念

建议把主线改为：

> **基础概念：situation awareness**  
> **新构念：coding-agent work-situation awareness**  
> **中文名：编码代理工作情境觉察**

初步定义：

> 编码代理工作情境觉察是指，用户在一次具体 coding-agent 编程任务中，对由 agent 行动、代码库状态、工具执行结果、任务约束和下一步风险共同构成的动态工作情境进行感知、理解和预测的程度。这种觉察使用户能够进行审批、监督、纠偏、接续和授权。

这个定义严格继承 situation awareness 的三层结构：

| situation awareness 原层级 | coding-agent work-situation awareness 的迁移 |
| --- | --- |
| perception | 用户是否感知 agent 当前在做什么、改了哪里、运行了什么命令、产生了什么 diff/test result |
| comprehension | 用户是否理解这些行动和状态变化对任务目标、代码语义、约束边界和风险的含义 |
| projection | 用户是否能预测批准下一步后 agent 可能做什么、代码状态可能如何变化、风险可能在哪里 |

这样做的好处是：

- 基础概念足够主流；
- 定义和测量足够成熟；
- coding agent 情境中的迁移断裂也很明确；
- 不需要依赖一个在 IS database 中只有 1 篇的概念；
- 仍然能解释 CLI agent、diff inspection、approval fatigue 等现实痛点。

## 7. workspace awareness 还怎么处理

为了满足“只能有一个基础概念”的要求，不建议把 `workspace awareness` 写成第二基础概念。

更合适的处理是：

> `workspace awareness` 不作为基础概念，只作为 situation awareness 在 shared workspace / groupware 语境中的相邻文献，用来说明为什么 coding agent 的 situation awareness 必须关注共享代码工作空间中的行动痕迹。

如果论文写作时需要更干净，也可以暂时完全不展开 `workspace awareness`，只在后文讨论 UI design implications 时引用。

## 8. 初步测量方案

如果基于 `situation awareness` 开发，我们可以做得更严谨：

### 8.1 subjective scale

任务后 7 点量表，三维：

1. **Perception of agent-mediated work state**
   - 我能清楚知道 agent 当前正在执行什么编程行动。
   - 我能清楚知道 agent 修改或检查了哪些代码位置。
   - 我能及时注意到 agent 运行命令或测试后的关键结果。

2. **Comprehension of agent-mediated work state**
   - 我能理解 agent 的修改为什么与当前任务有关。
   - 我能理解 agent 的行动对代码行为或风险的影响。
   - 我能判断 agent 当前行动是否仍符合我设定的约束。

3. **Projection of agent-mediated work state**
   - 我能预期批准下一步后 agent 可能会做什么。
   - 我能预测 agent 的下一步行动可能影响哪些代码或测试。
   - 我能判断什么时候需要介入、纠偏或接手。

### 8.2 objective awareness probes

模仿 SAGAT：

- 在 coding-agent task episode 中暂停；
- 让用户回答：
  - agent 刚刚修改了哪些文件；
  - 哪些测试通过或失败；
  - 当前审批请求会导致什么；
  - 哪个约束存在风险；
  - agent 下一步最可能做什么；
- 将回答与 logs、diff、test output、approval request ground truth 比较。

### 8.3 behavioral outcomes

可测：

- 审批准确率；
- 误批率；
- diff 检查时间；
- 纠偏次数；
- 回滚/撤销次数；
- 接管率；
- verification burden；
- approval fatigue；
- perceived control；
- calibrated trust；
- task success。

## 9. 与相邻概念的边界

| 相邻概念 | 边界 |
| --- | --- |
| trust | trust 是是否愿意依赖；work-situation awareness 是用户是否知道当前发生了什么、意味着什么、接下来会怎样 |
| perceived control | control 是能否影响过程和结果；work-situation awareness 是控制之前的认知基础 |
| transparency | transparency 是系统提供信息的程度；work-situation awareness 是用户形成的认知状态 |
| explainability | explainability 是解释机制；work-situation awareness 是解释是否帮助用户感知、理解、预测工作情境 |
| workspace awareness | workspace awareness 是 shared workspace 中他人行动觉察；work-situation awareness 用更主流的 SA 框架覆盖 agent-mediated coding task |
| mutual understanding | mutual understanding 是协作双方理解对齐；work-situation awareness 是用户对动态任务情境的认知状态 |
| cognitive load | cognitive load 是认知资源消耗；work-situation awareness 不足会增加负荷，但不是负荷本身 |

## 10. 当前推荐结论

经外部检索后，我建议修正为：

> 不再以 `workspace awareness` 作为唯一基础概念。  
> 改以 `situation awareness` 作为唯一基础概念，开发 `coding-agent work-situation awareness`。

这不是否认 `workspace awareness` 的价值。它的价值是帮助我们看清 coding agent 情境中“shared code workspace”这一层独特性。但从概念开发论文的基础概念选择看，`situation awareness` 更稳、更主流、更可测，也更容易向 IS audience 解释。

## 11. 使用的外部链接

- OpenAlex title.search API 示例：https://api.openalex.org/works?per-page=10&sort=cited_by_count:desc&filter=title.search:workspace%20awareness
- Dourish and Bellotti (1992), Awareness and Coordination in Shared Workspaces: https://doi.org/10.1145/143457.143468
- Gutwin and Greenberg (2002), A Descriptive Framework of Workspace Awareness for Real-Time Groupware: https://link.springer.com/article/10.1023/A:1021271517844
- Gutwin, Greenberg, and Roseman (1996), Workspace Awareness in Real-Time Distributed Groupware: https://doi.org/10.1007/978-1-4471-3588-3_18
- Gutwin and Greenberg (1999), The effects of workspace awareness support: https://doi.org/10.1145/329693.329696
- Cooper and Haines (2008), The Influence of workspace awareness on group intellective decision effectiveness: https://ideas.repec.org/a/taf/tjisxx/v17y2008i6p631-648.html
- Endsley (1995), Toward a Theory of Situation Awareness in Dynamic Systems: https://doi.org/10.1518/001872095779049543
- Endsley (1995), Measurement of Situation Awareness in Dynamic Systems: https://doi.org/10.1518/001872095779049499
- Endsley et al. (1998), A Comparative Analysis of SAGAT and SART: https://journals.sagepub.com/doi/10.1177/154193129804200119
- Franke et al. (2021), Situational information security awareness: https://onlinelibrary.wiley.com/doi/abs/10.1111/isj.12317
- The effect of interactive analytical dashboard features on situation awareness and task performance: https://www.sciencedirect.com/science/article/pii/S0167923620300774
