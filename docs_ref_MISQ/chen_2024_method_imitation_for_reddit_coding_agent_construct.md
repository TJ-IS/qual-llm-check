# 模仿 Chen et al. 2024 MISQ：用 Reddit 评论开发 Coding Agent UX 构念的准备清单

## 参考文章

参考文件：

`Chen_2024_-_Conceptualization_and_Measurement_of_Voice-Interaction_Usability_The_Development_of_Cooperative_Pri.md`

文章主题：

**Conceptualization and Measurement of Voice-Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use**

这篇文章的关键方法是：

1. 先证明现有 usability 概念和量表不能充分解释 voice-interaction 情境；
2. 用用户评论作为第一阶段的自然语言材料；
3. 用 grounded theory coding 从评论中抽取 open codes 和 axial codes；
4. 回到一个成熟理论，即 cooperative principle theory，把一阶概念组织成二阶理论维度；
5. 发现原理论无法覆盖的新维度，并把它作为理论扩展；
6. 用多轮问卷开发和验证量表；
7. 用 nomological validity 和 competing models 证明新构念比旧模型更能解释行为结果。

## 对我们的直接启发

如果我们计划从 Reddit 收集 coding agent 相关版块评论来开发构念，不能只是“收集评论、归纳主题”。MISQ 这篇文章的做法要求我们完成两件事：

1. Reddit 评论负责生成经验材料和一阶概念；
2. 理论负责解释为什么这些经验材料可以形成一个新构念，以及这个新构念如何扩展已有理论。

也就是说，Reddit 数据不能单独支撑概念开发。它必须嵌入一个理论迁移与理论扩展的逻辑中。

## 我们可以模仿的研究设计

### Phase 1：用 Reddit 评论开发构念维度

目标：

从真实用户关于 coding agent 的自然讨论中识别他们关心的 UX 问题，并将这些问题概念化为 coding-agent-specific UX 构念的维度。

对应 Chen et al. 的做法：

- 他们收集 30,834 条智能音箱用户评论；
- 先随机抽取 10% 做开放编码预试；
- 再对全部样本做开放编码；
- 然后做轴向编码；
- 最后回到 cooperative principle theory，把 13 个一阶概念归入 5 个二阶维度。

我们可以对应为：

- 收集 Reddit 中真实使用 coding agent 的帖子和评论；
- 抽取 10% 评论做预编码；
- 两名编码者独立开放编码；
- 对全部样本做逐句或逐意义单元编码；
- 得到 open codes；
- 聚合为 axial codes；
- 再回到 IS delegation / agentic IS use 理论，将一阶概念组织为二阶构念结构；
- 如果出现无法被原理论解释、但在 coding agent 情境中重要的类别，将其作为理论扩展。

### Phase 2：开发和验证量表

目标：

把第一阶段形成的概念结构转化为可以测量的量表。

对应 Chen et al. 的做法：

- 基于理论定义、用户评论中的 open codes、专家建议生成 62 个初始题项；
- 做 face validity 和 content validity；
- 用 Q-sort 检验题项与构念定义是否匹配；
- 进行三轮问卷；
- 第一轮 EFA/CFA；
- 第二轮进一步纯化量表并检验一阶/二阶构念关系；
- 第三轮复验量表、做 nomological validity，并和 TAM、UTAUT、MUG 等 competing models 比较；
- 最终从 58 个指标削减为 45 个指标。

我们可以对应为：

- 基于 CADCB 定义、Reddit open codes、相关文献和专家建议生成 50-70 个初始题项；
- 做 face validity、content validity；
- 用 Q-sort 检验题项是否能被正确归类到各一阶维度；
- 第一轮问卷做 EFA 和初步 CFA；
- 第二轮问卷进一步检验信度、聚合效度、区分效度和形成式二阶关系；
- 第三轮问卷检验 nomological validity；
- 与 trust、perceived control、technostress、verification burden、interruption overload、approval fatigue、general cognitive load 等模型比较解释力。

## 理论上最需要准备什么

### 1. 选定一个主理论，而不是只靠 Reddit 归纳

Chen et al. 的主理论是 cooperative principle theory。它们的论证逻辑是：

人机语音交互类似人际对话，因此 CPT 可以作为理论起点；但智能产品与人不同，所以 CPT 需要被扩展。

我们也需要同样的逻辑。建议主理论是：

**IS delegation / agentic IS use**

核心论证：

coding agent 与传统软件工具不同，它不是只被用户操作，而是被用户委托执行多步编程任务。用户给出目标，agent 读取上下文、计划行动、修改代码、运行命令或测试，并在过程中向用户请求权限或交还注意力。因此，coding agent 使用不是普通 IT use，而是 agentic IS delegation。

但是，已有 IS delegation 理论中的 coordination mechanism 仍然过于抽象，尚未解释 coding agent 情境下用户在个体任务层面感知到的协调负担。因此，我们可以把 IS delegation 中的 coordination 机制发展为一个 coding-agent-specific UX 构念：

**编码代理委托协调负担**

### 2. 写清为什么已有理论适用，又为什么必须扩展

这是模仿 Chen et al. 最关键的地方。

他们不是说 CPT 完全不适用，而是说：

- CPT 适用，因为 voice interaction 像对话；
- CPT 不够，因为人机语音交互出现了人际对话中不重要的 anthropomorphism；
- 因此，他们扩展 CPT，加入 anthropomorphism 作为新维度。

我们也要这样写：

- IS delegation 适用，因为 coding agent 使用包含任务委托；
- IS delegation 不够，因为 coding agent 委托发生在可执行、可修改、可回滚但也可能造成副作用的代码库中；
- 普通 delegation coordination 不足以刻画用户为了协调 agent 的自主行动、代码变更、权限交还、验证和接管而承担的任务级负担；
- 因此，我们扩展 IS delegation，把 coordination mechanism 转化为个体层面的 perceived coordination burden，并识别 coding-agent-specific 的一阶维度。

### 3. 准备“已有概念不够用”的理论缺口表

Chen et al. 用 usability 文献表说明：已有网站、移动应用、产品 usability 维度无法覆盖 voice interaction。

我们需要做一张类似表，至少包括：

- trust in AI；
- perceived control；
- technostress/work overload；
- cognitive load；
- interruption overload；
- warning/approval fatigue；
- verification burden；
- coordination cost；
- human-AI collaboration；
- software code review / program comprehension；
- transparency / explainability / observability；
- IS delegation coordination。

每个概念要写清：

1. 它能解释 coding agent 使用中的哪一部分；
2. 它不能解释什么；
3. 为什么不能直接照搬；
4. 它与 CADCB 的关系是前因、后果、相邻概念，还是被 CADCB 部分吸收的维度。

这张表是我们理论贡献的防线。

### 4. 明确 Reddit 评论在理论开发中的位置

Reddit 评论不是“代表性样本”，更不是最终测量数据。它在第一阶段的作用是：

- 捕捉用户自然语言中真实关心的问题；
- 帮助我们发现文献没有覆盖的经验类别；
- 生成一阶概念；
- 生成题项语言；
- 检验理论骨架是否漏掉重要现象。

因此，Reddit 评论适合作为 **concept discovery / dimension discovery** 数据，而不是用来估计概念强度或做因果检验。

### 5. 确定构念结构：不要预设所有维度，但要准备 sensitizing concepts

我们不能一开始就把五个维度写死，然后只从 Reddit 找证据。更好的做法是：

先把现有五个维度作为 sensitizing concepts：

- 任务边界对齐负担；
- 行动轨迹追踪负担；
- 审批与注意力交还负担；
- 代码变更验证整合负担；
- 接管与修复决策负担。

编码时允许出现新的维度。例如 Reddit 可能会揭示：

- 多 agent 并行协调负担；
- 上下文投喂和记忆维护负担；
- 预算/速率限制下的协调负担；
- CLI/IDE 介面切换负担；
- 代理行为可恢复性负担；
- 长任务中的监督节奏负担；
- 代码库污染和回滚压力。

如果某个新维度不能被 IS delegation 的 coordination 机制解释，但在 coding agent 情境下反复出现并具有现实意义，就可能成为类似 Chen et al. 中 anthropomorphism 的理论扩展点。

### 6. 准备一个“理论-数据来回比较”的流程

Chen et al. 不是先有理论再机械分类，也不是只做纯归纳。他们做的是：

评论 open coding → axial coding → 回到 CPT → 看哪些 fit → 看哪些不 fit → 扩展 CPT。

我们应该对应为：

Reddit open coding → axial coding → 回到 IS delegation / coordination → 看哪些 fit → 看哪些无法 fit → 提出 coding-agent-specific extension。

这一点要写进方法部分，否则会显得我们只是主题分析。

## Reddit 数据收集需要准备什么

### 1. 版块和帖子筛选标准

候选来源可以包括工具型 subreddit 和跨工具讨论 subreddit。当前通过简单检索能看到的相关来源包括：

- `r/ClaudeCode`
- `r/CursorAI`
- `r/GithubCopilot`
- `r/ChatGPTCoding`
- `r/AI_Agents`
- `r/ExperiencedDevs`
- 以及和具体语言/框架相关的开发者 subreddit 中关于 Cursor、Claude Code、Codex、Copilot Agent、Windsurf、Cline/Roo 等工具的讨论。

正式收集前需要重新核验各 subreddit 的活跃度、规则、可访问性和帖子相关性。

### 2. 纳入标准

建议只纳入：

- 讨论 coding agent 真实使用经历；
- 涉及 agent 自主执行、改代码、运行命令、生成 diff、请求权限、执行测试或多步任务；
- 涉及用户如何监督、验证、接管、限制、修复 agent；
- 有足够上下文描述具体体验，而不是只有一句情绪表达。

### 3. 排除标准

建议排除：

- 纯新闻转发；
- 纯价格讨论，除非价格与使用协调行为直接相关；
- 纯模型 benchmark；
- 只讨论 autocomplete；
- 只讨论普通 ChatGPT 问答；
- 广告、推广、机器人内容、招聘帖；
- 没有具体使用经验的泛泛争论。

### 4. 样本规模和饱和

Chen et al. 编码了 30,834 条评论，并在约 21,000 条后达到理论饱和。

我们不必机械追求同样数量，但需要：

- 先收集一个足够大的 corpus，比如 10,000-30,000 条候选评论；
- 用筛选规则过滤出与 coding agent UX 相关的评论；
- 记录每一步过滤数量；
- 在编码过程中记录 theoretical saturation：新增评论是否还产生新的 open code；
- 即使饱和后继续抽样，也要说明没有出现新的核心 open code。

### 5. 数据合法与伦理

正式收集前需要处理：

- Reddit API 访问审批；
- Reddit Data API Terms；
- IRB/伦理审查；
- 用户名、链接、时间戳等可识别信息的处理；
- 是否允许直接引用原文；
- 是否需要 paraphrase 以降低可搜索性和再识别风险；
- 数据存储、访问权限和删除策略。

Reddit 当前要求 API 使用者遵守 Data API Terms，并可能要求研究者申请访问；Reddit 也说明非商业研究者在符合条件时仍可访问公共数据。抓取方案应以官方 API/研究者访问机制为优先，而不是绕过限制的大规模 scraping。

## 编码过程需要准备什么

### 1. 预编码方案

先用文献做一个初始 coding scheme，但只作为 sensitizing framework。

初始类别可包括：

- delegation；
- task boundary；
- action trace；
- approval / permission；
- attention handoff；
- verification；
- code integration；
- takeover；
- repair / rollback；
- trust；
- control；
- fatigue；
- productivity；
- refusal / abandonment；
- CLI/IDE friction；
- context management。

### 2. 双人编码和一致性

模仿 Chen et al.：

- 抽 10% 评论做预编码；
- 两名编码者独立逐句编码；
- 比较结果；
- 讨论分歧；
- 修订 codebook；
- 再进入全部样本编码；
- 计算 intercoder reliability，例如 Cohen’s kappa；
- 目标至少超过 0.70。

### 3. Open coding 到 axial coding

Open codes 要尽量贴近用户原话，例如：

- "I have to babysit it";
- "it keeps asking for permission";
- "I cannot see what changed";
- "it made a mess across files";
- "I had to rollback";
- "CLI makes it hard to monitor";
- "I trust it for small scripts but not production";
- "I spend more time reviewing than coding"。

Axial coding 再把它们聚合成概念，例如：

- supervision demand；
- permission triage；
- change traceability；
- codebase side-effect checking；
- context feeding；
- takeover judgment；
- repair effort。

### 4. Selective coding 和理论映射

最后再回到主理论：

- 哪些 axial codes 可以被 IS delegation coordination 解释？
- 哪些属于 technostress、verification burden、approval fatigue 等旧概念？
- 哪些是 coding agent 情境中独有且旧理论没有命名好的？
- 哪些可以成为 CADCB 的一阶维度？
- 哪些更适合作为前因、后果或边界条件？

## 量表开发需要准备什么

### 1. 初始题项来源

题项应来自三类来源：

1. 构念和维度定义；
2. Reddit 评论 open codes 和原话；
3. 相关文献与专家建议。

不要直接把 Reddit 原话变成题项。要先抽象为构念语言，再保持用户语言的自然性。

### 2. 内容效度和 Q-sort

需要准备：

- 每个一阶维度的定义；
- 每个题项；
- 每个题项预期归属；
- 评估者说明；
- Q-sort 表格；
- 命中率、总体正确率、Kappa 或类似指标。

建议至少 20 名有编程或 IS 背景的评估者参与 Q-sort。

### 3. 多轮问卷验证

建议：

- 第一轮：300-500 个 coding agent 用户，做 EFA/CFA；
- 第二轮：400-600 个用户，进一步纯化并检验一阶/二阶结构；
- 第三轮：400-600 个用户，做 nomological validity 和 competing models 比较。

如果资源有限，最低也应保留两轮独立样本。

### 4. Competing models

Chen et al. 用 TAM、UTAUT、MUG 作为 competing models，证明自己的 context-specific model 更强。

我们可以比较：

- trust/control model；
- technostress model；
- verification burden model；
- cognitive load model；
- generic usability / ease-of-use model；
- IS delegation model 中较抽象的 appraisal/distribution/coordination 变量。

目标不是说旧模型没用，而是证明 CADCB 对 coding agent 重要结果有增量解释力。

## 我们最终要形成的理论贡献

模仿 Chen et al. 后，我们的理论贡献可以写成四层：

### 贡献 1：开发 coding-agent-specific UX 构念

我们把 coding agent 使用从普通 AI tool use 中区分出来，提出一个描述 agentic programming delegation 后协调负担的个体层面构念。

### 贡献 2：扩展 IS delegation / agentic IS use

我们不是只应用 IS delegation，而是把其中较抽象的 coordination mechanism 转化为任务情境中的用户感知负担，并识别 coding agent 情境下的具体组成。

### 贡献 3：用 Reddit 评论发现情境特有维度

Reddit 用户评论提供自然发生的使用经验，帮助发现文献中尚未命名或未充分测量的用户问题。

### 贡献 4：证明新构念有预测价值

通过量表开发和 competing models 比较，证明 CADCB 能解释 perceived control、approval fatigue、verification fatigue、continued use intention、delegation willingness 或 takeover behavior 等结果，并且解释力超过相邻旧概念。

## 现阶段最应该先做的文件

建议下一步先准备四个文件：

1. `reddit_data_collection_protocol.md`
   - subreddit 选择、关键词、时间范围、纳入/排除标准、伦理与 API 方案。

2. `CADCB_theoretical_gap_table.md`
   - trust、control、technostress、verification burden、approval fatigue 等旧概念为什么不够。

3. `CADCB_reddit_codebook_v0.md`
   - 初始 sensitizing codes、定义、例子、排除规则。

4. `CADCB_theory_mapping_plan.md`
   - open codes 如何进入 axial codes，axial codes 如何映射到 IS delegation / coordination，哪些情况构成理论扩展。

这四个文件准备好后，再开始抓取 Reddit 数据会更稳。
