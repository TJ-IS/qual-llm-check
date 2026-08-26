# 方向 C：轨迹效率与下一步动作预测（Trajectory Efficiency & Next-Action Prediction）——全面文献综述

- 综述编号：C
- 撰写日期：2026-08-18（基于 2026-08 联网检索，arXiv/会议出处均经二次核验）
- 关联 51 篇锚点：#21 GCNN/KVP（DSS 2021，事件日志下一事件预测；10 折交叉验证，44 个指标-数据集组合中 34 个超过先前方法）、#49 RADAR（MISQ 2025，动作序列生成）
- 一句话结论：**coding agent 的 thought-action-result 轨迹天然就是"事件日志"，但几乎没有工作把 IS 的过程挖掘/下一事件预测范式（GCNN/KVP）直接用于 agent 轨迹的下一步动作预判、提前 token 分配与失败预警；而轨迹冗长已被量化（单个任务典型浪费 48.4K tokens / 40 步），削减类方法正在爆发——"预测驱动"是下一个空位。**

---

## 1. 问题背景

Coding agent 每次任务都会产生一条轨迹：thought → tool call → observation → thought → ... → final patch。这条轨迹的三个属性决定了经济性与正确性：

1. **冗长**：SWE-bench Verified 上的定性分析显示，一个典型失败任务可能消耗 48.4K tokens、40+ 步才放弃；
2. **可预测**：很多动作是确定性的（读文件、跑测试），下一步往往可由历史预测；
3. **成本敏感**：2026 年主流 agent 每任务成本 $0.4–2.0，token 削减直接转化为成本削减。

IS 51 篇的 #21 GCNN/KVP 提供了成熟范式：把过程事件日志建模为序列，用门控卷积/键值注意力预测下一事件，10 折交叉验证、44 个指标-数据集组合中 34 个超过先前方法。本综述梳理：轨迹削减与效率方法、agentic RL 预算方法、成本-性能实证、过程挖掘侧的可迁移工作、研究缺口。

---

## 2. 检索范围与方法

- 检索时间：2026-08；来源：arXiv、NeurIPS/ICLR/ICML、Information Systems 期刊、MDPI、Semantic Scholar。
- 时间窗：2023–2026-08，重点 2025–2026。
- 关键词：`agent trajectory reduction` / `token efficiency agent` / `trajectory compression` / `next action prediction agent` / `process mining LLM` / `event log prediction` / `SWE-bench cost` 等。
- 纳入标准：① 直接优化 agent 轨迹效率/预算；② 或提供可迁移的轨迹建模/事件预测方法。

---

## 3. 现状：轨迹削减与效率优化

### 3.1 推理期轨迹削减
- **AgentDiet**（arXiv:2509.23586，《Improving the Efficiency of LLM Agent Systems through Trajectory Reduction》，ICLR 2026 相关）：在推理期削减冗余轨迹内容；在 SWE-bench Verified 上做了定性分析（典型浪费 48.4K tokens / 40 步案例）；结论是**频繁削减可以省钱且不损性能**。
- **Re-TRAC**（arXiv:2602.02486）：递归轨迹压缩 + 自反思——压缩后让 agent 反思是否丢失关键信息。
- **Slipstream**（arXiv，2026-05-08 发布）：轨迹"接地压缩"（grounded compression）+ 校验，压缩内容与代码库事实对齐。
- **Acon**（arXiv:2510.00615）：长程 agent 上下文压缩优化，面向超长任务。

### 3.2 训练/优化级效率
- **DEPO：Dual-Efficiency Preference Optimization**（arXiv:2511.15392）：把"推理 token 数"与"任务成功率"双目标放入偏好优化——**同时优化效率与正确性**，这是当前最接近"联合优化"的工作。
- **Latent Action Reparameterization**（arXiv:2605.18597）：用潜在动作重参数化提升 agent 推理效率。
- **Curriculum Design for Trajectory-Constrained Agent**（NeurIPS 2025，Tzannetos）：在 token budget 约束下做课程学习，length-cost 进入目标函数。
- **NAT**（arXiv:2603.06619）：把 token budget 作为一阶优化原语（budget-aware 训练）。
- **TRACE**（arXiv:2606.11119）：agentic RL 中 tree rollout 的预算分配——同样预算下更聪明地分配探索。
- **MemPO**：self-memory policy optimization——长程 agent 用自身记忆策略提升效率。

### 3.3 轨迹理解与实证
- **Understanding SE Agents: TAR Trajectories**（arXiv:2506.18824，Bouzenia & Pradel）：对 RepairAgent / AutoCodeRover / OpenHands 的大规模轨迹研究——理解"为什么失败、卡在哪一步"，是预测器设计的实证基础。
- **SWE-Effi**（arXiv:2509.09853）：在成本约束下重新评估 5 个 scaffold，发现"贵的不一定好"。
- **To Run or Not to Run**：执行工具的成本收益分析（SWE-bench 7745 条 traces + 3000 条端到端轨迹）——回答"这一步该不该跑命令"。
- **icat-agent**（arXiv:2606.25514）：SFW-bench Verified/Pro 上成本降低 $1.18/instance，Pro 上 resolve 67.4%——工程化效率标杆。
- **Stop Wasting Your Tokens**（arXiv:2510.26585）；**CodeAgents**（arXiv:2507.03254）；**More with Less: Turn-Control Strategies**（arXiv:2510.16786）：turn 数控制的通用策略。

### 3.4 成本-性能实证（2026 年中，SWE-bench Verified 系）
- 主流 resolve rate 65–80%，cost/task $0.4–2.0；
- 典型组合：Claude Opus 4.8 达 78.4% / $1.32 per task；Sonnet 4.6 达 72.6% / $0.39；
- DeepSeek V3.2 约 $0.028/task（低成本路线）；vexp-swe-bench 73.0% / $0.67；
- 含义：**同样 resolve rate 下成本差 1–2 个数量级，效率就是竞争力**。

---## 4. 现状：过程挖掘/事件预测侧（IS 可迁移资产）

- **GCNN / KVP**（DSS 2021，DOI:10.1016/j.dss.2021.113494，51 篇 #21）：门控卷积网络 + 键值预测注意力，做事件日志的下一事件预测；11 个真实事件日志（BPI'11/12/13、Helpdesk、EnvLog 等），10 折交叉验证，44 个指标-数据集组合中 34 个超过先前方法。**这是把"下一步动作预测"做成可测算法贡献的完整模板。**
- **ProcessTransformer**（Bukhsh et al., 2021）：Transformer 用于过程预测。
- **Next activity prediction with RAG**（Information Systems 2025）：检索增强的下一活动预测——与 coding agent 的"检索+预测"天然同构。
- **LLM 数据增强稀疏事件日志**（Information Systems 2026）：用 LLM 生成/增强稀疏日志——coding agent 轨迹日志稀疏时同样适用。
- **Semantic-Aware Process Mining multi-agent**（MDPI Computers 2025）：多 agent 语义感知过程挖掘。
- **Promoting Simple Agents**（arXiv:2604.21629）：奖励"简单"（轨迹更短）的 agent——与过程挖掘的"简洁性"目标呼应。
- **评价综述**：Survey on Evaluation of LLM-based Agents（arXiv:2503.16416，Yehudai 等）；LLM-based Autonomous Agents 综述（arXiv:2308.11432）。

---

## 5. 研究缺口（核心结论）

1. **"预测驱动"的轨迹管理缺失**：现有削减（AgentDiet/Re-TRAC/Slipstream）是"事后压缩"，**没有"事前预测"**——即用 GCNN/KVP 式 next-event prediction 判断"下一步该做什么/该不该做/是否快失败了"，从而提前分配 token、提前终止、提前切换策略。
2. **事件日志范式未迁移**：coding agent 轨迹（thought-action-result）与业务流程事件日志同构，但过程挖掘社区与 coding agent 社区基本没有交集——GCNN/KVP 的"下一事件预测 + 剩余时间预测"可直接对应"下一步动作准确率 + 预计剩余步数"。
3. **效率与正确性联合优化少**：DEPO 是少数双目标工作；多数方法只压 token 不保证 resolve rate。
4. **失败预警缺失**：TAR 轨迹研究揭示了失败模式（卡循环、重复测试、误读错误），但"用轨迹预测器做失败预警"没有系统工作。
5. **可解释性**：削减类方法难解释"为什么删这一步"，事件日志方法天然可解释（预测概率 + 属性归因）。

---

## 6. 与 51 篇 IS 文献的衔接

- **#21 GCNN/KVP（DSS 2021）**：直接模板——把 coding agent 轨迹转成事件日志（事件=thought/tool call/observation；属性=工具类型、文件路径、token 数、退出码），训练 next-event 预测器。
- **#49 RADAR（MISQ 2025）**：动作序列的 DRL 生成/预测范式——攻击器生成动作序列（方向 A）与预测器预测动作序列（本方向）共享同一状态表示，可统一建模。
- 另可衔接 #20 邻居感知预测（NAP，CNN 上下文基线，分类准确率 +1%–5%）的思路：用"邻居动作/上下文"预测当前动作的成败。
- 与方向 B 联动：ACRR（过度阅读指标，arXiv:2607.13034）本质是轨迹冗余度的度量，是预测器训练标签的一部分。

---

## 7. 对 coding agent 的算法研究方向建议

1. **Coding Agent 轨迹事件日志 + Next-Action 预测器（最优先）**
   - 用公开轨迹（SWE-bench Verified 上的 OpenHands/AutoCodeRover/RepairAgent 轨迹，TAR 论文已公开大规模数据）构造事件日志；
   - 迁移 GCNN/KVP：门控卷积编码历史、键值注意力选择关键历史事件，预测下一步动作类别（读文件/编辑/运行测试/停止）与剩余步数；
   - 指标：next-action accuracy、剩余步数 MAE、失败预警 AUC（提前 N 步识别失败任务）。

2. **预测驱动的 token 预算分配**
   - 预测器输出接入预算控制器：高置信路径给足预算，低置信路径提前触发"切换策略/请求帮助"；
   - 与 NAT（arXiv:2603.06619）的 budget 原语、TRACE（arXiv:2606.11119）的 rollout 分配结合。

3. **双目标效率偏好优化**
   - 在 DEPO 基础上加入"可跳过步数"标签（预测器判定冗余的步骤），训练"更短且更好"的策略；
   - 用 AgentDiet 的定性案例（48.4K tokens/40 步浪费）作为负样本。

4. **失败预警与自愈**
   - 用轨迹预测器做实时失败预警，触发 Re-TRAC 式自反思或更换工具策略；
   - 对照 icat-agent 的 $1.18/instance 成本降低目标，量化收益。

---

## 8. 参考文献

- [1] "AgentDiet: Improving the Efficiency of LLM Agent Systems through Trajectory Reduction." arXiv:2509.23586.
- [2] "DEPO: Dual-Efficiency Preference Optimization." arXiv:2511.15392.
- [3] "Latent Action Reparameterization." arXiv:2605.18597.
- [4] "Re-TRAC." arXiv:2602.02486.
- [5] "Slipstream." 2026-05-08.
- [6] "Acon." arXiv:2510.00615.
- [7] Tzannetos. "Curriculum Design for Trajectory-Constrained Agent." NeurIPS 2025.
- [8] "NAT." arXiv:2603.06619.
- [9] "TRACE." arXiv:2606.11119.
- [10] "MemPO: self-memory policy optimization."
- [11] "Stop Wasting Your Tokens." arXiv:2510.26585.
- [12] "CodeAgents." arXiv:2507.03254.
- [13] "More with Less: Turn-Control Strategies." arXiv:2510.16786.
- [14] Bouzenia & Pradel. "Understanding SE Agents: TAR Trajectories." arXiv:2506.18824.
- [15] "SWE-Effi." arXiv:2509.09853.
- [16] "To Run or Not to Run." SWE-bench 7745 traces + 3000 end-to-end.
- [17] "icat-agent." arXiv:2606.25514.
- [18] GCNN/KVP. "Process data properties matter." DSS 2021. DOI:10.1016/j.dss.2021.113494.
- [19] Bukhsh et al. "ProcessTransformer." 2021.
- [20] "Next activity prediction with RAG." Information Systems 2025.
- [21] "LLM data augmentation for sparse event logs." Information Systems 2026.
- [22] "Semantic-Aware Process Mining multi-agent." MDPI Computers 2025.
- [23] "Promoting Simple Agents." arXiv:2604.21629.
- [24] Yehudai et al. "Survey on Evaluation of LLM-based Agents." arXiv:2503.16416.
- [25] "LLM-based Autonomous Agents survey." arXiv:2308.11432.
- [26] RADAR. MIS Quarterly 2025. DOI:10.25300/misq/2024/17339.
- [27] Yin & Feng. "ACRR/E3." arXiv:2607.13034.