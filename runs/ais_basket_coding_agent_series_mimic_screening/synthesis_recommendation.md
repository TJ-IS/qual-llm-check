# 从 AIS Basket 软件设计研究到 coding-agent 系列研究

## 结论

最值得采用的主线不是泛化的“可用性”“信任”或“生产力”，而是一个可以直接客观计分、又能按 coding-agent 生命周期拆成四个阶段的结果指标：

**全生命周期监督决策准确率（working label: lifecycle supervisory decision accuracy）**。

它指人在 coding agent 的关键控制点是否采取了客观上正确的监督行动。每个控制点都有由隐藏测试、仓库状态、预置错误和安全规则确定的正确答案，因此它不是需要量表开发的潜变量。

对于二元控制决策，建议用平衡准确率：

`0.5 × [正确放行安全/正确产出的比例 + 正确阻止危险/错误产出的比例]`

对于“人、agent、协作”三类委派决策，可采用宏平均准确率。四项研究分别测量阶段准确率；系列完成后再报告四阶段均值或联合的 trial-level 分层模型。共同的次级结果是隐藏测试通过率、最终仓库完整性和决策时间。

该指标在 coding-agent 情境中的独特性来自：agent 会接收委派、持续调用工具、产生部分可观察的中间状态、永久修改仓库，并在错误发生前后要求人类决定继续、阻止、接管、回滚或验收。它不只是把普通 chatbot 的“信任”改名。

## 最适合模仿的核心论文

### 1. Productive delegation：系列的任务委派模板

**Cognitive Challenges in Human–Artificial Intelligence Collaboration: Investigating the Path Toward Productive Delegation**（ISR, 2022）最接近我们想要的“系列”结构。论文自身有四项研究：delegation/inversion、解释与强制委派策略、feedback、task difficulty。核心理论机制是狭义的 `metaknowledge` 和 human–AI complementarity；核心结果是有 ground truth 的分类准确率。

值得复制：同一任务银行、同一客观正确答案，逐项改变委派规则、解释、反馈和难度；比较人自行委派给 AI 与 AI 在低置信度时将任务交还给人。

### 2. Dynamic process representation：系列的过程监控模板

**Animation as a Dynamic Visualization Technique for Improving Process Model Comprehension**（I&M, 2021）把静态复杂流程改成可播放、暂停、逐步推进的动态表示，以 cognitive theory of multimedia learning、cognitive load theory 和 cognitive dimensions framework 指导设计。其理解题覆盖执行顺序、排他关系、并发和重复，并记录完成时间。

值得复制：把 coding agent 的计划、工具调用、文件编辑、测试、重试和分支从静态聊天记录改成动态执行轨迹；用预置答案测试监督者是否正确理解执行顺序、并发冲突、循环失败和当前仓库状态。

### 3. Effective use：系列的 IS 总体结构与日志测量模板

**Designing Conversational Dashboards for Effective Use in Crisis Response**（JAIS, 2023）直接采用 Theory of Effective Use。TEU 将 effective use 分为 transparent interaction、representational fidelity 和 informed action，并把 adaptation 和 learning 视为驱动因素。该文只重点实现第一维，但提供了非常适合模仿的客观日志指标：最短必要交互步骤/实际步骤，同时测量正确任务数和用时。

值得复制：用交互日志比较用户实际监督路径与完成正确监督所需的最短路径，而不是只问“是否易用”；用同一理论把四项研究组织成从交互、表示到行动的递进故事。

### 4. Calibrated acceptance：系列的最终验证模板

**Will Humans-in-the-Loop Become Borgs?**（MISQ, 2021）同时测量最终准确率和 `unique human knowledge`，并比较 AI certainty 与 personalized AI advice。其关键贡献是揭示“个体准确率上升”可能伴随“人类识别 AI 独特错误的能力下降”。

**Trust Calibration of Automated Security IT Artifacts**（I&M, 2021）用 automation trust and reliance framework 区分 performance、process、purpose calibrators，并把校准与实际依赖、使用和防护绩效连接起来。

值得复制：同时报告接受正确 agent 结果、拒绝错误 agent 结果、人类独立发现 agent 错误的比例，避免把单纯依赖率或主观信任当成成功。

### 5. Risk intervention：系列的关键风险干预模板

**The Fog of Warnings**（MISQ, 2025）有三个实验，以 habituation generalization 和 schema theory 推导两个非常具体的软件改动：让安全警告在视觉上不同于普通通知，或者使用不同的交互方式。最终结果是实际 warning disregard，而不只是风险感知。

**A Warning Approach to Mitigating Bandwagon Bias**（JAIS, 2023）补充了一个很重要的对称评价逻辑：不仅测警告在真实偏差/风险情境中是否纠偏，也测没有偏差/风险时是否造成过度修正。

值得复制：coding agent 大量普通工具通知之后出现罕见危险操作时，比较普通点击确认与视觉/交互模式明显不同的风险门；同时测漏拦截危险操作和误拦截安全操作。

### 6. 机制与边界条件的系列写法

**Why Do Data Analysts Take IT-Mediated Shortcuts?**（JMIS, 2022）本身就是极好的系列写作模板：先验证 shortcuts 损害客观绩效，再做三项实验依次建立主效应、ego-depletion 中介、moral integrity 和 goal type 边界条件。shortcuts 与最终任务表现均由日志和正确答案客观测量。

值得复制的是研究推进方式以及“过程违规 + 最终正确性”的双重日志结果，不是其组织伦理变量。coding-agent 场景可客观记录是否跳过测试、依赖检查、diff 审查或失败后的重新验证。

## 推荐的四项 coding-agent 研究

### Study 1：正确委派——谁应该处理这个子任务？

- 阶段：任务分解与执行权分配。
- 软件改动：在现有 coding-agent scaffold 中加入实例级委派/交还控制。agent 根据经独立验证的能力边界决定继续执行或请求人类；不要直接相信模型口头声称的 confidence。
- 狭义理论：metaknowledge、recognition of complementarity、productive delegation。
- 条件示例：人类自行委派；agent 基于经验阈值主动 inversion；阈值规则加简短解释。
- 主要结果：是否把子任务交给客观上更合适的执行者；宏平均正确率。
- 次级结果：最终隐藏测试通过率、无效交接次数和完成时间。
- 主要模仿来源：Cognitive Challenges；Borgs 的个性化建议作为补充。

### Study 2：正确监控——人是否真正知道 agent 正在做什么？

- 阶段：长时间、多步骤执行过程。
- 软件改动：把静态聊天/日志升级为可播放、分层、逐步推进的执行轨迹，明确计划节点、工具调用、文件变更、测试结果、分支与重试。
- 狭义理论：cognitive theory of multimedia learning、cognitive load theory、cognitive dimensions。
- 条件示例：静态线性日志；自动播放动态轨迹；用户控制的逐步轨迹。
- 主要结果：在安全与偏离轨迹上做出“继续/检查/停止”正确决策的平衡准确率。
- 诊断性子结果：执行顺序、排他分支、并发冲突和重复循环四类理解正确率；决策时间。
- 主要模仿来源：Animation；Conversational Dashboards 的日志路径效率作为补充。

### Study 3：正确干预——关键风险出现时，人是否会采取正确动作？

- 阶段：agent 即将执行高风险、不可逆或越权操作。
- 软件改动：区分普通进度通知与关键风险门；关键风险使用不同视觉外观或不同交互模式，例如 hold-to-approve/drag-to-authorize，而普通事件仍为常规点击。
- 狭义理论：generalization of habituation、schema theory。
- 条件示例：风险门与普通通知同形；仅视觉不同；仅交互模式不同。
- 主要结果：对危险操作正确阻止、对安全操作正确放行的平衡准确率。
- 次级结果：反应时间、漏拦截率、误拦截率、最终仓库破坏事件数。
- 主要模仿来源：Fog of Warnings；Warning Approach 用于加入“无风险时的副作用”评价。

### Study 4：正确验收——人是否接受正确结果并拒绝错误结果？

- 阶段：补丁完成后的验证与交付。
- 软件改动：提供经过校准的 error-boundary 信息或选择性建议机制；不要展示未经验证的长篇推理文本。可比较无校准器、全局历史准确率、实例级证据、个体化选择性建议。
- 狭义理论：automation trust and reliance、unique human knowledge、human–AI complementarity。
- 主要结果：接受正确补丁并拒绝错误补丁的平衡准确率。
- 关键附加结果：agent 错而人正确纠正的比例（coding-agent analogue of unique human knowledge）、最终隐藏测试通过率。
- 主要模仿来源：Borgs；Trust Calibration。
- 负面设计约束：Expl(AI)ned 表明解释可能通过 confirmation bias 改变并固化心智模型，因此应增加“撤去辅助后的复测”或 transfer trial，确认设计没有让人永久学习 agent 的错误规则。

## 保持四项研究成为“一个系列”的必要做法

1. 使用同一 coding-agent scaffold、同一日志格式和相同的监督动作集合。
2. 建立共享任务银行，但各研究使用独立任务切分，避免训练/熟悉效应。
3. 每个任务都有隐藏测试、仓库状态规则和预置错误，能确定每个关键控制点的正确监督动作。
4. 每项研究只改变一个主要产品特征；agent 基础能力和模型版本保持不变。
5. 四项研究共同使用阶段平衡准确率作为主要因变量，最终隐藏测试成功率和时间作为共同次级结果。
6. 主观 trust、perceived usefulness、cognitive load 等只作为机制、操纵检验或解释变量，不作为系列的核心成功指标。
7. 样本与分析尽量使用 task × participant 的交叉随机效应模型，因为不同仓库任务与不同参与者都构成随机变异来源。

## 两个备选主线

### 备选 A：Coding-agent effective use

以 TEU 为统一理论，将四项研究设为 transparent interaction、representational fidelity、informed action、learning/adaptation。优点是 IS 理论背书最直接，且 Conversational Dashboards 已演示日志化客观测量；缺点是 effective use 太通用，coding-agent 的“非它不可”程度弱于监督决策准确率。

### 备选 B：Coding-agent process integrity

以是否遵循计划、测试、安全与验证步骤为总结果，分为计划完整性、执行合规、验证完整性、失败恢复四阶段。Data Analysts Shortcuts 对过程合规与最终正确性的客观测量提供了强背书。优点是非常适合日志测量；缺点是现有66篇中对“恢复”阶段的软件设计模板不够强，需要再做一轮专门文献检索。

## 不建议作为主线的论文类型

- Behaviorally Measuring Usability：非常适合学习如何构造客观交互指标，但鼠标轨迹可用性太通用，只适合作为测量方法支线。
- Designing Attentive Information Dashboards：理论到设计链很强，但照搬实时眼动硬件不符合当前资源约束；可以借鉴“个体化反馈”和多阶段前后测，不应把眼动硬件作为核心。
- Expl(AI)ned：适合学习多阶段、撤除辅助和迁移测试，但其主要贡献包含解释的负面副作用，不应把它当作“解释一定提高绩效”的正向设计模板。
- 反钓鱼训练类论文：客观准确率和反馈设计很好，但更接近训练系统；适合作为 Study 4 的反馈/校准补充，不适合作为整个 coding-agent 产品系列的中心。
- 电商点击、广告、推荐布局类论文：虽有客观点击或选择行为，但核心方法对 coding agent 的代理自主性、仓库状态和监督控制利用不足。
