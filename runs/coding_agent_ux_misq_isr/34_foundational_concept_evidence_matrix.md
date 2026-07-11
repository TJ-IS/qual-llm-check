# 基础概念证据矩阵：definition、measurement 与 database 命中

## 1. 本文档的判断标准

这个文档只回答一个问题：

> 如果我们要为 coding agent UX 开发一个新概念，哪些已有基础概念有资格作为唯一的迁移起点？

判断标准比早期 brainstorm 更严格：

1. **database 中必须真实出现**：检索范围限定为 `Title + Abstract + Author Keywords + Index Keywords`，而不是整行文本或参考文献。
2. **必须有清楚的原文定义或操作化方式**：不能只凭词面意思推断。
3. **必须有可追踪的测量方式**：包括 survey item、dyadic congruence、process coding、concept mapping、field experiment 等。
4. **研究层级必须能迁移到 individual/task-episode UX**：组织层面的成本、治理或绩效概念不能作为基础概念。
5. **必须存在 coding-agent 情境下的理论断裂**：不能只是把旧概念换一个对象名称；必须说明为什么旧测量在 coding agent 中不适用或不充分。

结论先写在前面：

> 当前最有资格作为唯一基础概念的仍是 **mutual understanding**。  
> **shared understanding** 是最强命名备选，但不应被当成第二个并列基础概念。  
> 其他概念更适合作为前因、后果、边界条件、相邻构念或被排除项。

## 2. database 命中概览

检索文件：`database/ALL_AIS_Basket_11.csv`  
检索字段：`Title`, `Abstract`, `Author Keywords`, `Index Keywords`

| 候选概念 | 命中文献数 | 短语命中数 | 初步处理 |
| --- | ---: | ---: | --- |
| mutual understanding | 16 | 38 | 主基础概念 |
| shared understanding | 37 | 84 | 最强命名备选，但不单独作为第二基础概念 |
| common ground | 7 | 12 | 适合解释 grounding，但太偏沟通过程 |
| transactive memory / transactive memory system | 23 | 146 | 适合作为前因或相邻构念 |
| shared mental model / shared mental models | 9 | 36 | 太偏团队层级和 mental model 相似性 |
| team cognition | 3 | 9 | 与 shared mental model 合并看，层级偏团队 |
| teamwork quality | 1 | 4 | 更像协作结果评价 |
| collaboration quality | 3 | 4 | 更像协作结果评价 |
| collaborative repair | 1 | 3 | 很相关但过窄，只覆盖 breakdown repair |
| coordination quality | 0 | 0 | 排除 |
| coordination burden | 0 | 0 | 排除 |
| collaboration burden | 0 | 0 | 排除 |
| coordination cost / coordination costs | 22 | 71 | 命中不少，但主要是组织、市场或平台层面成本，排除 |

## 3. 主候选：mutual understanding

### 3.1 database 中的代表文献

| 标题 | 年份 | 期刊 | DOI | database 摘要显示的角色 |
| --- | ---: | --- | --- | --- |
| Mutual understanding in information systems development: Changes within and across projects | 2019 | MIS Quarterly | 10.25300/MISQ/2019/13980 | 直接研究 ISD 项目中 mutual understanding 如何变化、形成并影响项目成功 |
| Does mutuality matter? Examining the bilateral nature and effects of CEO-CIO mutual understanding | 2016 | Journal of Strategic Information Systems | 10.1016/j.jsis.2016.01.001 | 将 mutual understanding 细分为双边 perspective-taking / perceptual congruence，并解释 collaboration quality |
| CEO/CIO mutual understanding, strategic alignment, and the contribution of IS to the organization | 2010 | Information and Management | 10.1016/j.im.2010.01.002 | 用 CEO/CIO 双方视角测量对 IS 角色的 mutual understanding，并连接 strategic alignment 与 IS contribution |
| Cocreating understanding and value in distributed work: How members of onsite and offshore vendor teams give, make, demand, and break sense | 2008 | MIS Quarterly | 10.2307/25148839 | 将 shared/common/mutual understandings 放在分布式软件工作中研究，强调 sensegiving/sensemaking/sensedemanding/sensebreaking |
| Us and them: A social capital perspective on the relationship between the business and IT departments | 2011 | European Journal of Information Systems | 10.1057/ejis.2011.4 | 从 business 与 IT occupational communities 的知识分享和 social capital 解释 mutual understanding |

### 3.2 原文证据：它到底怎么定义或操作化

MISQ 2019 的摘要明确说，研究对象是 ISD 项目中关键 stakeholder groups 之间的 mutual understanding，并考察它如何在项目内和项目间变化，以及如何影响项目成功。其理论机制不是“满意度”，而是 planning/control mechanisms、artifacts、sensegiving、sensemaking、stakeholder engagement 如何促成或破坏理解。

JSIS 2016 更适合给我们提供测量逻辑。它把 CEO-CIO understanding 放进 perceptual congruence model 和 actor-partner interdependence model 中，区分：

- **actual agreement**：双方真实意见是否相似；
- **perceived agreement**：一方是否认为双方意见相似；
- **understanding**：一方能否准确预测另一方意见，也就是 perspective-taking；
- **mutuality / bidirectionality**：A 理解 B 与 B 理解 A 可能不对称，且对 collaboration quality 的影响不同。

I&M 2010 的测量更接近传统 business-IT alignment：用 CEO 和 CIO 对同一组问题的回答差异来操作化 mutual understanding，主题是 “the role of IS in the organization”。Benlian and Haffke (2016) 对该文的综述表明，这是一种基于双方同题回答差异的 latent-variable/congruence 测量。

### 3.3 已有测量方式

mutual understanding 至少有三种可追踪测量方式：

| 测量逻辑 | 代表文献 | 具体做法 | 对我们的启发 |
| --- | --- | --- | --- |
| dyadic congruence | Johnson and Lederer (2010); Benlian and Haffke (2016) | 收集双方对同一对象的真实意见、对对方意见的预测或感知，再计算 agreement / understanding / congruence | 原方法严谨，但 coding agent 不能像人一样填写问卷，因此不能照搬 |
| longitudinal/process tracing | Jenkin, Chan, and Sabherwal (2019); Rai et al. (2008) | 追踪 sensegiving、sensemaking、artifact、stakeholder engagement 如何改变理解状态 | coding agent 使用天然是 task episode，可以追踪 prompt、tool call、diff、test、correction |
| one-side perceived understanding | 在 CEO/CIO 和 alignment 文献中常作为双方数据的简化或单侧感知出现 | 测量一方是否认为双方有 shared view / shared understanding | 最适合 coding agent，但必须限定为 developer-perceived、action-manifested understanding |

### 3.4 典型前因与后果

已有文献中的前因包括：

- project planning and control mechanisms；
- artifacts；
- sensegiving and sensemaking activities；
- stakeholder engagement 的 depth、scope、timing；
- shared language；
- shared domain knowledge；
- structural systems of knowing；
- communication frequency；
- empathy、trust 等关系因素。

已有文献中的后果包括：

- ISD project success；
- CEO-CIO collaboration quality；
- IS strategic alignment；
- IS contribution / business value；
- business-IT relationship quality。

### 3.5 为什么 coding agent 情境必须迁移

旧概念不能直接照搬，原因很具体：

1. **不能对 agent 做对称问卷**：CEO/CIO 可以各自报告真实意见和对对方意见的预测；coding agent 没有可被视为人类主观信念的问卷回答。
2. **理解不是只通过语言显现**：coding agent 的理解主要显现在代码修改、命令执行、测试选择、上下文引用、风险边界遵守和纠偏吸收中。
3. **任务状态会被 agent 直接改变**：传统 mutual understanding 多用于协作中的认知对齐；coding agent 会自主改写代码库，因此理解状态与实际 work state 更紧密耦合。
4. **用户关心的是可工作性，不是心智真实性**：用户不会真的知道 agent 是否“理解”，只能根据行动是否体现出对任务、代码上下文和约束的把握来判断。

因此，如果以 mutual understanding 为唯一基础概念，新概念不应定义为“agent 真正理解用户”，而应定义为：

> 开发者在一次具体编程任务中，感知到自己与 coding agent 对任务目标、代码上下文、约束边界、当前进展和下一步行动形成了足以共同推进任务的工作性理解的程度。

这个定义的高低程度是连续的，不是 0-1：

- 低：用户反复解释目标和约束；agent 的行动显示它没有吸收上下文；用户不知道 agent 下一步为什么这样做。
- 中：agent 能处理局部任务，但会丢失边界、进展或代码上下文。
- 高：用户与 agent 对目标、代码状态、限制和下一步行动保持稳定、可修复、可推进的共同理解。

## 4. 最强备选：shared understanding

### 4.1 database 中的代表文献

| 标题 | 年份 | 期刊 | DOI | database 摘要显示的角色 |
| --- | ---: | --- | --- | --- |
| Antecedents of IS Strategic Alignment: A Nomological Network | 2009 | Information Systems Research | 10.1287/isre.1070.0159 | shared understanding between CIO and TMT 是 IS strategic alignment 的社会维度和近端前因 |
| E-profiles, conflict, and shared understanding in distributed teams | 2015 | Journal of the Association for Information Systems | 10.17705/1jais.00401 | e-profiles 降低 distributed team conflict，并促进 shared understanding |
| "Computing" Requirements for Open Source Software: A Distributed Cognitive Approach | 2018 | Journal of the Association for Information Systems | 10.17705/1jais.00525 | OSS requirements work 被视为形成 shared understanding 的分布式认知过程 |
| BAUSTEIN-A design tool for configuring and representing design research | 2024 | Information Systems Journal | 10.1111/isj.12516 | design research 项目中 shared understanding 对跨边界协作重要 |

### 4.2 原文定义与测量

Preston and Karahanna (2009, ISR) 是最有用的 shared understanding 基础文献。公开摘要显示，它把 CIO 与 TMT 对 IS 角色的 shared understanding 作为 IS strategic alignment 的社会维度，并提出 shared language、shared domain knowledge、systems of knowing、experiential similarity 等前因。

Benlian and Haffke (2016) 对该文的综述进一步说明其测量方式：取 CIO 与 TMT member 对若干问题的回答平均值，这些问题询问双方是否对组织中 IS 的角色有 shared view and understanding。

### 4.3 为什么它强，但不应和 mutual understanding 并列

shared understanding 的优点是：

- 比 mutual understanding 少一点“agent 具有人类心智”的暗示；
- 更适合问用户“你是否感觉自己和 agent 共享任务理解”；
- database 命中更多，说明它在 IS 文献中是稳定表达。

但它不适合作为另一个并列基础概念，因为它和 mutual understanding 的核心理论域高度重叠。我们如果同时写两个基础概念，会回到“混入一堆概念”的问题。

更稳妥的处理是：

> 基础概念仍选 **mutual understanding**，因为它有更强的 dyadic / bidirectional measurement 证据；  
> 构念命名可以考虑用 **coding-agent working shared understanding**，以避免暗示 agent 具有人的主观理解。

换句话说，shared understanding 是命名和表述上的备选，不是第二条理论主线。

## 5. common ground

### 5.1 database 中的代表文献

| 标题 | 年份 | 期刊 | DOI | database 摘要显示的角色 |
| --- | ---: | --- | --- | --- |
| Supporting the design of data integration requirements during the development of data warehouses: A communication theory-based approach | 2017 | European Journal of Information Systems | 10.1057/ejis.2015.22 | 用 communication theory 和 common ground 处理 data integration requirements 中的 semantic heterogeneity |
| Articulation of work process models for organizational alignment and informed information system design | 2016 | Information and Management | 10.1016/j.im.2016.01.004 | 工作流程建模工具需要让协作者建立 common ground |
| Fostering quality and flow of online learning conversations by artifact-centered discourse systems | 2013 | Journal of the Association for Information Systems | 10.17705/1jais.00321 | 明确从 Clark 的 common ground 理论解释在线学习对话质量和流动 |

### 5.2 原文定义与测量

Clark 的 grounding 理论中，common ground 不是简单“信息透明”，而是沟通双方通过 grounding 过程使某个表达被理解并纳入共同基础。典型测量不是普通 Likert 量表，而是过程证据，例如：

- 是否完成 reference resolution；
- 是否出现 clarification、repair、acknowledgment；
- 信息是否被双方后续使用；
- conversation quality / flow 是否改善；
- 沟通媒介如何改变 grounding 成本。

### 5.3 为什么不选它作为基础概念

common ground 很适合解释 coding agent 的 prompt/context 维持问题，尤其是“我和 agent 是否在同一个上下文里”。但它有三个不足：

1. database 命中少于 mutual/shared understanding；
2. 理论焦点更偏沟通与语义 grounding；
3. coding agent 的核心 UX 不只是说清楚，还包括代码行动、测试、diff、工具调用、边界遵守和纠偏吸收。

因此，common ground 可以作为 mutual understanding 的过程机制之一，但不建议作为唯一基础概念。

## 6. transactive memory

### 6.1 database 中的代表文献

| 标题 | 年份 | 期刊 | DOI | database 摘要显示的角色 |
| --- | ---: | --- | --- | --- |
| The group mind of hybrid teams with humans and intelligent agents in knowledge-intense work | 2025 | Journal of Information Technology | 10.1177/02683962241296883 | 直接涉及 humans 与 intelligent agents 的 hybrid teams |
| Attaining individual creativity and performance in multidisciplinary and geographically distributed IT project teams: The role of transactive memory systems | 2022 | MIS Quarterly | 10.25300/MISQ/2022/14596 | TMS 影响个体 creativity 与 performance，是最接近 individual-level 的 TMS 证据 |
| Transactive memory systems as a collective filter for mitigating information overload in digitally enabled organizational groups | 2013 | Information and Organization | 10.1016/j.infoandorg.2013.06.001 | TMS 被用于解释群体如何过滤信息过载 |
| Team knowledge and coordination in geographically distributed software development | 2007 | Journal of Management Information Systems | 10.2753/MIS0742-1222240104 | 团队知识帮助地理分布式软件开发协调 |

### 6.2 原文定义与测量

TMS 的核心定义是团队中围绕知识编码、储存、检索和沟通形成的认知分工。常见测量来自 Lewis (2003) 的三维结构：

- specialization：成员是否有各自专门知识；
- credibility：成员是否相信彼此知识可靠；
- coordination：成员是否能顺畅协调知识使用。

公开全文示例中，TMS item 包括“team member has specialized knowledge”“I know which team members have expertise”“I trusted other members' knowledge”“Our team had few misunderstandings about what to do”等。这说明 TMS 的测量重心是“谁知道什么、谁可靠、知识如何协调使用”。

### 6.3 为什么不选它作为基础概念

TMS 很有价值，但它回答的问题不是我们最想测的东西。

它适合问：

> 用户是否知道 agent 擅长什么、不能做什么、应该把什么任务交给它。

但我们的目标更像：

> 在一次具体 coding task 中，用户是否感到自己和 agent 对目标、代码上下文、约束、进展和下一步行动形成了可工作的共同理解。

所以 TMS 更适合做前因或相邻构念，例如：

- perceived agent expertise map；
- perceived agent capability clarity；
- task-agent fit；
- delegation calibration。

它不应作为主基础概念，否则研究会滑向“用户如何认知 agent 能力与分工”，而不是“人与 coding agent 如何形成工作性理解”。

## 7. shared mental model / team cognition

### 7.1 database 中的代表文献

| 标题 | 年份 | 期刊 | DOI | database 摘要显示的角色 |
| --- | ---: | --- | --- | --- |
| How pair programming influences team performance: The role of backup behavior, shared mental models, and task novelty | 2019 | Information Systems Research | 10.1287/isre.2019.0856 | pair programming 通过 shared mental models 和 backup behavior 影响软件团队表现 |
| Team cognition: Development and evolution in software project teams | 2007 | Journal of Management Information Systems | 10.2753/MIS0742-1222240210 | 研究 software project teams 中 team cognition 的出现与演化 |
| Team knowledge and coordination in geographically distributed software development | 2007 | Journal of Management Information Systems | 10.2753/MIS0742-1222240104 | 研究团队知识结构如何帮助协调分布式软件开发 |
| An exploratory study on meta skills in software development teams: Antecedent cooperation skills and personality for shared mental models | 2008 | European Journal of Information Systems | 10.1057/palgrave.ejis.3000730 | shared mental models 被定义为团队成员对流程、结果和角色的共同期待 |

### 7.2 原文定义与测量

shared mental model 文献通常将其看作团队成员 mental models 的相似性或 sharedness。测量方式不是简单问“你是否理解”，而是：

- similarity ratings；
- concept mapping；
- card sorting；
- cognitive map content analysis；
- Pathfinder / UCINET / MDS 等结构表示；
- 计算团队成员知识结构的相似度、收敛度或 sharedness。

这类测量严谨，但非常依赖“每个成员都有可提取的 mental model”这个前提。

### 7.3 为什么不选它作为基础概念

它与 coding agent 情境有明显断裂，但这个断裂不一定帮我们开发更好的 individual UX 构念：

1. 它默认团队成员都有人类 mental model；
2. 测量上需要多个成员的认知结构，不适合普通用户回忆一次 coding agent 使用经历；
3. 它更偏 team-level cognition，而不是 individual-level user experience；
4. 它容易使论文变成“人-AI团队认知相似性”，而不是 coding agent 使用中的具体体验。

因此，它可以作为理论背景或区分效度对象，但不建议作为基础概念。

## 8. teamwork quality / collaboration quality

### 8.1 database 中的代表文献

| 概念 | 标题 | 年份 | 期刊 | DOI |
| --- | --- | ---: | --- | --- |
| teamwork quality | Relating collaborative technology use to teamwork quality and performance: An empirical analysis | 2003 | Journal of Management Information Systems | 10.1080/07421222.2003.11045747 |
| collaboration quality | Evaluating Team Collaboration Quality: The Development and Field Application of a Collaboration Maturity Model | 2015 | Journal of Management Information Systems | 10.1080/07421222.2015.1095042 |
| collaboration quality | A perfect match or an arranged marriage? How chief digital officers and chief information officers perceive their relationship: a dyadic research design | 2023 | European Journal of Information Systems | 10.1080/0960085X.2023.2178742 |

### 8.2 原文定义与测量

Hoegl and Gemuenden (2001) 的 Teamwork Quality 是最清楚的基础。它开发的是团队协作质量的综合概念，六个 facets 是：

- communication；
- coordination；
- balance of member contributions；
- mutual support；
- effort；
- cohesion。

它的后果包括 team performance、personal success、work satisfaction、learning 等。

### 8.3 为什么不选它作为基础概念

teamwork/collaboration quality 的问题不是没有测量，而是太宽。它更像用户对“这次协作好不好”的总体评价，容易吞掉我们真正想解释的机制。

如果把它作为基础概念，我们的新构念很容易变成：

> 和 coding agent 协作得是否顺畅。

这不够独特，也很难解释为什么必须开发新概念。它更适合做后果变量：

> coding-agent working mutual understanding 越高，用户感知 collaboration quality 越高。

## 9. collaborative repair

### 9.1 database 中的代表文献

| 标题 | 年份 | 期刊 | DOI | database 摘要显示的角色 |
| --- | ---: | --- | --- | --- |
| Overcoming Breakdowns in Customer-Chatbot Interaction: Design and Impact of Collaborative Repair Strategies | 2026 | MIS Quarterly | 10.25300/MISQ/2025/18742 | 研究 customer 与 chatbot 如何共同修复 conversational breakdown |

### 9.2 原文定义与测量

这篇 MISQ 文章非常重要，因为它明确把 AI interaction breakdown 从“用户自己猜”或“chatbot 自己修”转为 customer-chatbot working together to resolve breakdowns。研究做法是设计 collaborative repair strategy，在大型保险公司 chatbot 中实例化，并用 randomized field experiment 做自然场景评估。

它的结果变量包括：

- breakdowns 是否被解决；
- breakdown 对 customer outcomes 的负面影响是否被缓解。

### 9.3 为什么不选它作为基础概念

它太窄。coding agent 使用中当然有 repair：

- agent 改错文件；
- agent 没吸收约束；
- agent 测试失败后纠偏；
- 用户反复要求撤回或缩小范围。

但我们的目标不是只研究 breakdown 后的修复，而是研究更一般的 task episode 中，用户和 agent 是否形成可共同推进的工作性理解。

所以 collaborative repair 很适合作为：

- coding-agent working mutual understanding 的一个形成机制；
- 低 mutual understanding 之后的恢复过程；
- 后续单独论文主题。

但不适合作为唯一基础概念。

## 10. coordination cost / burden 类概念

### 10.1 database 结果

| 概念 | 命中文献数 | 判断 |
| --- | ---: | --- |
| coordination quality | 0 | 排除 |
| coordination burden | 0 | 排除 |
| collaboration burden | 0 | 排除 |
| coordination cost / costs | 22 | 命中，但层级不合适 |

coordination cost 在 database 里确实出现，但主要用于：

- 组织韧性；
- 平台开发者；
- M&A；
- sourcing strategy；
- interfirm/intrafirm process integration；
- market fragmentation；
- online labor platform contract governance。

这些不是 individual-level user experience，也不是人与 coding agent 共同完成编程任务中的感知状态。

### 10.2 为什么明确排除

如果把 coordination cost/burden 当基础概念，会出现两个问题：

1. **层级不匹配**：大多数文献是 firm/platform/market level，不是 individual task episode。
2. **理论对象不匹配**：它解释交易、组织、治理或市场协调成本，不解释用户如何与 agent 建立任务理解。

因此，它最多只能作为现实动机中的口语表达，例如“用户觉得和 agent 协调很累”，不能作为我们论文的基础概念。

## 11. 最终建议

如果严格遵守“只能选一个基础概念”的要求：

> **基础概念：mutual understanding**  
> **新构念暂定名：coding-agent working mutual understanding**  
> **中文名：编码代理工作性相互理解**

如果担心 “mutual” 暗示 agent 有人类式主观理解，论文标题或量表名可改为：

> **coding-agent working shared understanding**  
> **编码代理工作性共享理解**

但理论基础仍只写 mutual understanding，不再把 shared understanding、common ground、TMS、team cognition 等都混进基础概念。

更精确地说，我们要开发的不是：

- trust；
- control；
- usability；
- readability；
- collaboration quality；
- coordination burden；
- transactive memory；
- common ground 本身。

我们要开发的是：

> 用户在具体 coding agent 编程任务中，感知自己与 agent 是否已经形成一种能被代码行动、测试行动、约束遵守、状态更新和纠偏吸收持续体现出来的工作性共同理解。

这件事在实践上重要，是因为它能解释很多 coding agent 使用中的真实痛点：

- 用户为什么不愿意用 CLI agent：不是只因为界面难用，而是看不见 agent 是否理解了任务和代码状态；
- 用户为什么审批疲劳：每一步都需要人工确认 agent 是否仍在同一个任务理解里；
- 用户为什么反复检查 diff：用户不确定 agent 的修改是否体现了共享的目标、边界和上下文；
- 用户为什么中途接管：工作性相互理解断裂后，信任、掌控感、效率和继续使用意愿都会下降。

因此，这个概念同时有理论价值和实践价值：

- 理论上，它把 human-human mutual understanding 迁移到 human-agent coding work，并解释为什么传统 dyadic congruence 测量不能直接使用；
- 实践上，它能指导 coding agent 产品设计：更好的 diff 展示、状态摘要、约束记忆、纠偏吸收提示、下一步行动预告和低疲劳审批机制。

## 12. 后续必须补齐的证据

为了达到可写论文的标准，下一步不能直接写量表，而要补齐：

1. 下载并精读 `mutual understanding` 主文献全文，摘出原文定义、构念边界、测量表或编码方式。
2. 对 `shared understanding` 只保留命名备选证据，不让它扩散为第二基础概念。
3. 从 Reddit coding agent 评论中抽取 domain facets，验证用户是否真的在谈：
   - 任务目标是否被理解；
   - 代码上下文是否被理解；
   - 约束边界是否被理解；
   - 当前进展是否被共同把握；
   - 下一步行动是否可预期；
   - 纠偏是否被吸收。
4. 用 expert sorting / Q-sort 区分它和 trust、control、usability、transparency、cognitive load、verification burden。
5. 再进行 EFA/CFA 或 PLS-SEM，检验它是多维形成式还是单维反映式。

## 13. 本文档使用的外部证据链接

- Jenkin, Chan, and Sabherwal (2019), MIS Quarterly: https://aisel.aisnet.org/misq/vol43/iss2/15/
- Preston and Karahanna (2009), Information Systems Research: https://pubsonline.informs.org/doi/10.1287/isre.1070.0159
- Benlian and Haffke (2016), Journal of Strategic Information Systems: https://www.researchgate.net/publication/291422047_Does_mutuality_matter_Examining_the_bilateral_nature_and_effects_of_CEO-CIO_mutual_understanding
- Johnson and Lederer (2010), Information and Management: https://www.sciencedirect.com/science/article/abs/pii/S0378720610000030
- Clark (1991), Grounding in Communication: https://worrydream.com/refs/Clark_H_1991_-_Grounding_in_Communication.pdf
- Transactive Memory System definition resource: https://psychiatry.ucsd.edu/research/programs-centers/instep/tools-resource/definitions/emergent-states/cognitive-emergent-states/tms.html
- Huang, Liu, and Zhong (2013), TMS measurement example: https://www.researchgate.net/publication/262563092_The_impact_of_transactive_memory_systems_on_team_performance
- Hoegl and Gemuenden (2001), Teamwork Quality: https://ideas.repec.org/a/inm/ororsc/v12y2001i4p435-449.html
- Gnewuch and Reinkemeier (2026), MIS Quarterly collaborative repair: https://aisel.aisnet.org/misq/vol50/iss2/8/
- Shared mental model measurement examples: https://link.springer.com/article/10.3758/s13428-012-0201-5 and https://atlas.northwestern.edu/papers/sharedTeam.pdf
