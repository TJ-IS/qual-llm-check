# 模仿 Dong Thesis 进行 Coding Agent UX 构念开发的方法备忘录

## 参考对象

参考文件：

- `dong_thesis.md`
- `dong_thesis_concept_development_substudy.md`

主要参考子研究：

第 3 章“社会化商务技术可供性的概念发展与量表开发”。

该子研究的目标不是直接检验因果模型，而是先完成一个前置工作：

1. 说明为什么现有概念无法充分解释新情境；
2. 基于母理论发展一个情境化构念；
3. 识别构念维度；
4. 生成、修订、评估和确定测量题项；
5. 为后续实证模型提供可用量表。

## Thesis 的概念开发逻辑

Dong thesis 的基本论证结构是：

社会化商务是一个新兴实践情境。它同时包含传统电商和社交媒体的属性，用户目标也同时包含购物和社交。现有研究虽然讨论了电子商务、社交媒体、技术接受和一般技术特征，但没有一个概念能准确刻画“社会化商务中，技术功能如何支持用户实现社会化购物目标”。因此，作者以技术可供性理论为母理论，发展出“社会化商务技术可供性”这一情境化构念。

这一构念的开发不是简单换场景，而是建立在三个缺口上：

1. 情境缺口：社会化商务不同于传统电子商务，也不同于普通社交媒体；
2. 理论缺口：既有技术可供性维度不能完全适配社会化商务；
3. 测量缺口：缺少可靠量表，使后续实证研究无法展开。

这三个缺口对应我们的研究也很重要。我们不能只说“coding agent 是新东西”，还要说：

1. coding agent 与代码补全、聊天式 AI、传统 IDE 工具不同；
2. 既有概念如 trust、control、technostress、interruption overload、verification burden 不能完整刻画我们关心的现象；
3. 缺少可以测量该现象的个体层面量表。

## Thesis 的具体步骤

### 1. 先用文献界定研究对象和边界

Dong thesis 先在前面章节界定社会化商务是什么，和传统电子商务有什么区别，再进入第 3 章开发构念。

我们需要对应完成：

- 定义 coding agent；
- 区分 coding agent、AI code completion、chatbot、传统 IDE 工具、CI/lint/formatter；
- 说明用户与 coding agent 的关系是“委托后协调”，而不是单纯使用、采纳、信任或接受建议；
- 明确分析层级是 individual/task episode，而不是团队、组织或工具整体评价。

### 2. 选择母理论，并说明为什么要迁移

Dong thesis 的母理论是 IT affordance。它的迁移理由是：技术可供性适合描述 IT 功能与用户目标行为之间的关系，但原有维度无法覆盖社会化商务。

我们的母理论更适合是：

**IS delegation / agentic IS use**。

迁移理由应写成：

coding agent 不是普通工具，而是可以被用户委托执行多步编程任务的 agentic IS artifact。既有 IS delegation 文献提出 appraisal、distribution、coordination 机制，但仍较抽象，尚未把 coding agent 情境下用户在任务执行过程中感知到的协调成本转化为可测量的 UX 构念。因此，我们把 IS delegation 中的 coordination mechanism 情境化为 coding-agent delegation 中的 perceived coordination burden。

### 3. 先给概念定义，但承认定义不足以揭示内涵

Dong thesis 在第 3.1 节先给出定义，然后马上说：单靠定义还不足以理解构念，需要继续识别维度。

我们也应这样写：

**编码代理委托协调负担**是指开发者在将具体编程任务部分委托给 coding agent 自主推进后，为了使 agent 的行动持续符合任务目标、代码库状态和自己的最终接管责任，而感知到的额外认知与交互成本。

然后补一句：

单从定义上还不能充分揭示这一构念的组成结构，因为 coding agent 的委托协调可能同时涉及任务边界、行动轨迹、权限交还、代码变更验证和接管修复等不同活动。因此，需要进一步识别其维度。

### 4. 用“宏观设计周期”组织维度识别

Dong thesis 借鉴 Takeda 等的模型设计过程：问题形成、问题建议、发展、评估、结论。

我们可以模仿为：

1. 问题形成：文献显示 coding agent 使用中出现审批疲劳、验证负担、失控感、委托困难等现象，但现有概念分散，无法整体解释委托后的协调负担；
2. 问题建议：提出 CADCB 作为描述 coding agent 委托后协调成本的候选构念；
3. 发展：从文献、实践材料和访谈中形成候选维度；
4. 评估：将候选维度与真实 coding agent 工作流、访谈材料、专家反馈和卡片分类结果比较；
5. 结论：确定构念边界、维度结构和初始题项。

### 5. 用实践访谈和专家小组识别维度

Dong thesis 使用：

- 10 个具有一年以上经验的实践者访谈；
- 4 组小组讨论；
- 共 20 个专家，包括教师、博士研究生和实践者；
- 访谈约 40 分钟；
- 录音转写；
- 邮件/电话回访；
- 三名博士研究生进行逐行编码；
- 开放编码、轴向编码、聚类、分类；
- 多轮调和不一致。

我们可以模仿但要适配 coding agent：

- 访谈 12-20 位真实 coding agent 用户；
- 至少覆盖 Cursor/Claude Code/Codex/Devin/Copilot Agent/Windsurf 等不同工具；
- 包含职业软件工程师、独立开发者、数据科学/研究编程用户、开源维护者、技术管理者；
- 要求被访者最近 1-3 个月使用过能够修改代码或运行命令的 coding agent；
- 每个访谈围绕一个具体 task episode，而不是泛泛谈使用体验；
- 如果可行，收集匿名化的对话记录、diff、审批提示、运行命令、测试结果或 git 提交作为辅助材料。

### 6. 访谈提纲需要围绕“协调活动”而不是泛体验

Dong thesis 的访谈问题关注：哪些技术特征促成活动、特征之间有什么差异、缺少某特征是否影响理解。

我们的访谈问题可以对应为：

1. 请回忆最近一次你把真实编程任务交给 coding agent 自主推进的经历，它具体做了什么？
2. 在这个过程中，你需要额外做哪些事情来让 agent 的工作保持符合你的目标？
3. 哪些时刻你觉得需要停下来理解、审批、检查、限制、接管或修复 agent 的行动？
4. 这些协调活动彼此有什么不同？比如说明任务、追踪行动、处理审批、验证代码、接管修复是否是不同负担？
5. 如果少了其中一种协调活动，你是否仍能完整描述这次 coding agent 使用体验？
6. 与普通代码补全、普通 ChatGPT 问答或人工同事协作相比，这种负担有什么不同？

### 7. 维度识别必须同时接文献和访谈

Dong thesis 不是只靠访谈命名维度，而是把访谈结果与已有文献中的技术可供性维度进行对照，区分“沿用旧名”和“情境重命名”。

我们也应采用同样逻辑：

- 与 IS delegation 文献对照：appraisal、distribution、coordination；
- 与 technostress 对照：work overload、complexity、role ambiguity、intrusion；
- 与 interruption/warning fatigue 对照：提醒、审批、通知；
- 与 verification burden 对照：代码检查、测试、审查；
- 与 perceived control/trust 对照：控制与依赖；
- 与 HCI transparency/observability 对照：过程可见、行动追踪。

维度命名不能只是访谈关键词，要解释它是从哪个旧概念部分迁移而来，以及为什么在 coding agent 情境下需要重新界定。

### 8. 构念结构应采用形成式二阶模型

Dong thesis 把社会化商务技术可供性作为形成式二阶构念，六个一阶维度作为形成性指标；每个一阶维度再用反映式题项测量。

我们的 CADCB 也适合这样做：

- 二阶构念：编码代理委托协调负担；
- 一阶维度：任务边界对齐负担、行动轨迹追踪负担、审批与注意力交还负担、代码变更验证整合负担、接管与修复决策负担；
- 二阶关系：形成式，因为五种负担共同形成整体协调负担，且不必高度相关；
- 一阶题项：反映式，因为同一维度下的题项应共同反映该维度。

这点非常关键。若把 CADCB 当作单一反映式构念，很容易和 general workload 或 technostress 混在一起。

### 9. 题项生成需要多来源

Dong thesis 的条目来源包括：

- 概念定义；
- 个人访谈；
- 开放式问卷；
- 文献；
- 条目写作原则。

我们的初始题项来源应包括：

- CADCB 的正式定义；
- 访谈逐字稿；
- coding agent 使用日志/案例；
- 高适配文献摘要；
- IS delegation、technostress、interruption、verification、control、trust 等相邻量表；
- 用户自己的原话，尤其是关于“审批疲劳”“看不清改动”“不知道何时接管”“需要反复限定范围”的表达。

目标是先生成 40-60 个初始题项，不要一开始就只保留 10 个。

### 10. 条目修订需要表面效度和内容效度

Dong thesis 的修订过程：

- 3 名有相关经验的博士研究生独立检查语义；
- 删除语义不清、重复、歧义题项；
- 进行 4 轮卡片分类；
- 第一轮不给组名，让评估者自由分组并命名；
- 后续轮次给出组名和定义，加入 N/A 组；
- 计算目标命中率、总体命中率、Kappa；
- 阈值大致为命中率超过 80%，Kappa 超过 0.7。

我们可以照做：

- 第 0 轮：3-5 名研究者/博士生检查表述；
- 第 1 轮：开放式卡片分类，不给维度名，观察是否自然聚出类似维度；
- 第 2-4 轮：给出五个维度定义和 N/A，计算命中率；
- 删除低命中率、跨维度、语义含混、太像旧构念的题项；
- 每轮保留评估者反馈，作为内容效度证据。

### 11. 量化阶段要用两轮独立样本

Dong thesis 使用：

- 第一轮有效样本 296，做探索性因子分析；
- 第二轮有效样本 559，做验证和效度检验；
- 第一轮删除低载荷和双载荷题项；
- 第二轮检验内部一致性、聚合效度、区分效度、VIF 和二阶模型路径。

我们对应需要：

- 预调查样本：建议 200-300 个真实 coding agent task episodes；
- 正式验证样本：建议 400-600 个真实 coding agent task episodes；
- 筛选条件：必须使用过能读取/修改代码、运行命令或测试的 coding agent；必须基于一个具体任务回忆；排除只用 autocomplete 或普通聊天建议的样本；
- EFA 阶段：删除低载荷、双载荷、跨维度混淆题项；
- CFA/PLS-SEM 阶段：验证一阶维度的信度效度和二阶形成式结构；
- 同时测量相邻构念做区分效度。

### 12. 必须准备区分效度对象

Dong thesis 的贡献依赖于证明其构念不是已有技术特征的简单拼接。我们更需要这一点，因为 CADCB 与很多旧概念相邻。

建议同时测量：

- perceived control；
- trust in AI/coding agent；
- technostress 或 work overload；
- interruption overload；
- approval fatigue 或 warning fatigue；
- verification burden；
- cognitive load；
- perceived usefulness/productivity；
- continued use intention 或 delegation willingness。

理论上应预期：

- CADCB 与 technostress 正相关，但不是同一构念；
- CADCB 与 verification burden 正相关，但验证负担只解释其中一部分；
- CADCB 负向影响 perceived control；
- CADCB 可能通过 perceived control、approval fatigue、verification fatigue 影响 continued use；
- trust 可能降低一部分 CADCB，但高 trust 不必然消除协调负担。

## 我们开发 CADCB 前必须准备的条件

### 条件 1：清楚的研究对象边界

必须提前写清：

- 什么是 coding agent；
- 什么不是 coding agent；
- 什么算“委托”；
- 什么算“协调”；
- 为什么以 task episode 为单位测量。

如果边界不清，样本会混入 ChatGPT 问答、Copilot 补全、普通自动化工具，构念会被冲淡。

### 条件 2：旧概念不适用的证据表

需要准备一张表，逐一说明：

- trust 能解释什么，不能解释什么；
- control 能解释什么，不能解释什么；
- technostress 能解释什么，不能解释什么；
- verification burden 能解释什么，不能解释什么；
- interruption/approval fatigue 能解释什么，不能解释什么；
- IS delegation 的 coordination mechanism 能解释什么，不能解释什么。

这张表是概念开发的防线。没有它，CADCB 容易被认为是旧概念换名。

### 条件 3：实践材料

至少需要收集：

- coding agent 工具的真实工作流；
- 权限请求和审批机制样例；
- diff/patch 展示方式；
- agent 自动运行命令和测试的样例；
- 用户抱怨审批疲劳、看不清改动、难以接管的真实表达；
- 不同工具之间的差异。

这些材料用于证明 CADCB 不是抽象想象，而是来自 coding agent 使用实践。

### 条件 4：访谈样本

建议初期至少：

- 12-20 个深度访谈；
- 3-4 个专家小组或研究者讨论；
- 覆盖至少 4 类用户：职业开发者、独立开发者、研究/数据编程用户、开源维护者；
- 覆盖至少 3 类工具：IDE agent、CLI agent、远程自主 agent。

### 条件 5：编码团队和编码规则

需要准备：

- 访谈提纲；
- 转写规范；
- 开放编码规则；
- 轴向编码规则；
- 维度命名原则；
- 分歧调和机制；
- 代码本/codebook。

最好至少 2-3 名编码者独立编码部分材料，并记录一致性与分歧。

### 条件 6：初始条目池

不要直接从现在的 10 个题项开始正式测。

建议先生成：

- 每个维度 8-12 个题项；
- 总计 40-60 个题项；
- 另生成 3-5 个二阶总括题项，用于模型验证和效标检查；
- 每个题项都标注来源：访谈原话、文献迁移、研究者概括或实践观察。

### 条件 7：卡片分类评估者

需要准备：

- 第一轮开放式分类评估者 6-8 人；
- 后续轮次 6-10 人；
- 评估者应混合研究者、开发者和有 coding agent 经验的用户；
- 每轮都要保存分类结果、命中率、Kappa、修改理由。

### 条件 8：两轮问卷样本

建议：

- 预调查/EFA：200-300 个有效 task episodes；
- 正式验证/CFA 或 PLS：400-600 个有效 task episodes；
- 每个样本都记录使用工具、任务类型、任务复杂度、agent 自主性、审批次数、修改文件数、用户经验等控制变量。

### 条件 9：后续理论模型

Dong thesis 的第 3 章是后续第 4-6 章的基础。我们也应该提前知道 CADCB 后续要解释什么。

建议后续模型可以围绕：

- 前因：agent 自主性、行动透明度、审批机制、diff 可视化、任务复杂度、代码库熟悉度、agent 可靠性；
- 后果：perceived control、approval fatigue、verification fatigue、continued use intention、delegation willingness、task performance、takeover frequency；
- 调节：用户专业经验、任务风险、测试覆盖、工具使用经验。

## 与 thesis 的关键相似点和差异

相似点：

- 都是新情境下发展情境化构念；
- 都要证明旧文献不足以覆盖新情境；
- 都用母理论迁移；
- 都用文献和访谈共同识别维度；
- 都适合做形成式二阶构念；
- 都需要严格量表开发程序。

差异：

- Dong thesis 研究的是技术支持“可能性”，我们的研究是委托后“协调成本”；
- Dong thesis 的维度多对应平台功能，我们的维度多对应用户在 agentic workflow 中承担的协调活动；
- Dong thesis 的对象是社会化商务平台，我们的对象是 task episode 中的 coding agent 使用；
- Dong thesis 的后续模型解释购买意向，我们的后续模型更适合解释控制感、疲劳、继续使用、委托意愿和接管行为。

## 现阶段建议

下一步不要急着定最终量表，而应先完成三个文档：

1. `CADCB_construct_boundary.md`：正式定义、对象边界、相邻概念区分；
2. `CADCB_literature_gap_table.md`：旧概念能解释什么、不能解释什么；
3. `CADCB_interview_protocol.md`：访谈对象、筛选标准、访谈问题、编码方案。

完成这三个文档后，再生成 40-60 个初始题项，进入卡片分类和预调查。
