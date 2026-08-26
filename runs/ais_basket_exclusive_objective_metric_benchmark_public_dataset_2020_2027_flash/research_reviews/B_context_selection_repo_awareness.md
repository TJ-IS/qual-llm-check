# 方向 B：上下文选择与仓库态势感知（Context Selection & Repository Awareness）——全面文献综述

- 综述编号：B
- 撰写日期：2026-08-18（基于 2026-08 联网检索，arXiv/会议出处均经二次核验）
- 关联 51 篇锚点：#46 GASP（JAIS 2025，图增强符号预测）、#8 NPECF（DSS 2020，网络投影边分类）、#33 DPA-LR（ISR 2023，多样性偏好感知链接推荐）
- 一句话结论：**coding agent 的"该读哪些文件/符号、按什么顺序读"已被证明是正确性与成本的关键轴，且存在可量化的 headroom（oracle gold 检索仍未达上限、agent 平均过度阅读 ~91% 文件）；但"仓库图上的符号/链接预测驱动上下文选择"（把 IS 图网络方法直接迁移过来）尚无系统工作。**

---

## 1. 问题背景

Coding agent 面对大型仓库时，上下文窗口和 token 成本都是硬约束：读多了贵且引入噪声（Lost-in-the-Middle 效应），读少了漏关键信息导致修复失败。现代 coding agent 的每一步都依赖"上下文选择器"（检索器/探索器/裁剪器）决定看什么。

IS 51 篇中的图网络方法（GASP 用图增强做符号预测、NPECF 用网络投影做边分类、DPA-LR 用多样性偏好感知做链接推荐）在概念上完美对应这个决策问题：

- "读哪些文件" ≈ 仓库依赖图上的**链接预测**（link prediction：哪些节点与当前任务相关）；
- "该不该读这个符号/文件" ≈ 仓库图上的**符号预测**（sign prediction：正相关 vs 误导/噪声）；
- "探索顺序/切换策略" ≈ **多样性偏好感知的推荐**（避免上下文同质化，保持探索-利用平衡）。

本综述梳理：仓库级检索与探索的现状、上下文质量证据、可迁移的图方法、研究缺口。

---

## 2. 检索范围与方法

- 检索时间：2026-08；来源：arXiv、ACL/NeurIPS/ICLR/ICML 会议、Semantic Scholar、GitHub 仓库。
- 时间窗：2023–2026-08，重点 2025–2026。
- 关键词：`repository-level retrieval` / `code retrieval` / `context selection` / `repo exploration` / `agent context pruning` / `dependency graph code` / `RAG for code` / `SWE-bench context` 等。
- 纳入标准：直接以 coding agent 的上下文/检索/探索为对象，或提供可迁移的仓库图/检索方法。

---

## 3. 现状：仓库级检索与探索

### 3.1 基准与评测
- **Agent Retrieval Bench**（arXiv:2607.24882，Qin & Xie）：第一个 file-level 的"仓库上下文检索"基准，专门评测 coding agent 在仓库中检索相关文件的组件；关键结论是 **oracle gold 上下文仍有大幅 headroom**——即当前所有检索器都远未达到理论上限，检索环节本身值得投入。
- **SWE-Explore**（arXiv:2606.，Zhang/Wang，2026-06-04 发布，Semantic Scholar 有记录）：系统衡量 coding agent 如何探索仓库（探索轨迹、覆盖率）；结论：**agentic explorer（会思考下一步看哪里的探索器）明显优于经典检索**；line-level coverage 与"高效排序"（用最少步数覆盖关键行）是关键评价轴。
- **FastContext**（arXiv:2606.14066）：训练高效仓库探索器，把探索本身变成可学习任务。

### 3.2 探索/定位方法
- **Libra**（arXiv:2607.00016）：把仓库索引变成**状态变量**，由 Solver 失败驱动更新；用 Markdown catalog 导航图；三个冻结 agent（Prompter / Solver / Healer）形成优化循环；与 RepoMem 直接竞争，且可解释、可迁移。
- **SWE-Pruner**（arXiv:2601.16746）：任务感知的自适应上下文裁剪，**减少 23–54% token 且成功率不降反升**；后续 **SWE-Pruner Pro**（arXiv:2607.18213）进一步扩展。
- **ACRR 论文**《Do AI Agents Know When a Task Is Simple?》（arXiv:2607.13034，Yin & Feng）：提出 **Agent Cognitive Redundancy Ratio（ACRR）** 量化"过度阅读"——agent 平均多读约 **91% 的文件**（MSE-Bench 上 ACRR≈22.1，即平均多读 22 个不相关文件）；配套 E3（Estimate, Execute, Expand）框架按任务复杂度动态分配阅读量。
- **LARGER**（arXiv:2605.16352）：词法锚定的仓库图探索检索——以任务中的标识符为锚点在依赖图上扩散。
- **Explorative/Deterministic Anchoring**（arXiv:2606.26979）：轻量 call/inheritance 拓扑（只利用调用与被继承关系）提升函数级定位 **+2.2 个百分点**，并**缩短 1.6 轮交互**——证明"极简图结构"就能带来显著收益。
- **Co-Coder**（arXiv:2606.00953）：cohesion-aware 图划分 + 依赖感知调度的多 agent 任务切分——把"变更范围"拆给多个 agent 并保证依赖顺序。
- **Exploration Structure in LLM Agents for Multi-File Change Localization**（arXiv:2606.11976）：对比线性探索 vs 结构化探索；发现文档共同演化关系是潜在依赖信号。
- **Repository Intelligence Graph**（Cherny-Shahar & Yehudai，2026-01）：把仓库构建为"智能图"供 agent 查询。
- **Effective Context Retrieval via Partial Dependency Graph**（arXiv:2608.01927）：用部分依赖图做上下文检索。
- **AOCI**（Semantic Scholar 有记录）：符号-语义混合索引。
- **CodexGraph**：开源的代表性仓库图 + agent 接口（工程实践参照）。
- **Vector Graph-Based Repository Understanding**（Semantic Scholar，Bevziuk/Fatula，2025-10）：向量 + 图混合仓库理解。
- **KGCompass**（在 RAG-APR 对比表 arXiv:2603.29067 中出现）：知识图谱导向的代码检索；**Oracle 定位后 best-of-k 还能再提升 +9.7–13.3 分**——说明定位信息本身就是性能倍增器。

### 3.3 检索增强代码生成（RAG for Code）综述与经典
- **Retrieval-Augmented Code Generation Survey**（arXiv:2510.04905）：仓库级 RAG 的系统综述。
- **AceCoder**（arXiv:2303.17780）：guided generation + 示例检索的早期代表性工作。
- **RLCoder**（arXiv:2407.19487）：用 RL 优化 repo 级代码补全的上下文使用。

---## 4. 现状：上下文质量的反思性证据

- **Evaluating AGENTS.md**（arXiv:2602.11988，Gloaguen 等）：系统评测 agent 上下文文件（AGENTS.md/REPO.md）的收益；关键发现：**LLM 生成的上下文文件使推理 token 增加 22%（GPT-5.2），成功率反而下降 3%**——上下文不是越多越好，质量与生成方式都重要。
- **Sense and Sensitivity**（ACL 2026）：区分词法匹配（lexical）与语义召回（semantic）的检索敏感度，指出长上下文下 "Lost-in-the-Middle"（Liu et al., 2024b）效应会稀释关键信息。
- **Tokalator**（arXiv:2604.08290）：把"context rot"（上下文随任务推进逐渐失真）工程化处理——上下文是动态资源，需要维护而非一次性注入。
- 综合含义：**裁剪、排序、动态维护**三个动作缺一不可；这也与方向 C（轨迹效率）直接耦合。

---

## 5. 研究缺口

1. **上限未达**：Agent Retrieval Bench 显示 oracle gold 上下文仍有大幅 headroom——"读全"不是现状，是目标。
2. **过度阅读可量化但缺少闭环**：ACRR（平均多读 ~91% 文件）给出了新指标，但"测量冗余 → 学习裁剪 → 再测量"的闭环工作还很少（SWE-Pruner 是裁剪端代表，但未与冗余度指标联动）。
3. **图符号方法未迁移**：GASP（图增强符号预测）、NPECF（网络投影边分类）、DPA-LR（多样性偏好推荐）在 IS 领域已验证，但**没有人把"仓库依赖图上的 link/sign prediction"做成上下文选择器**——这是最清晰的迁移空位。
4. **探索策略未学习化**：Libra 用失败驱动更新、Co-Coder 用图划分调度，但"何时停止探索、何时切换文件、何时请求帮助"仍靠启发式，没有 RL/偏好优化训练的探索策略。
5. **与成本联动不足**：检索/裁剪大多单独优化 token，未与 resolve rate 联合优化（方向 C 的 DEPO 思路可平移）。

---

## 6. 与 51 篇 IS 文献的衔接

- **#46 GASP（JAIS 2025）**：用图增强（graph augmentation）提升边符号预测，在稀疏、非平衡网络上显著提升 Accuracy/Optimized Precision 等指标 → 迁移为"仓库依赖图 + 图增强预测该读/不该读"；稀疏标注（只有少数任务有 gold 文件）正是 GASP 的适用条件。
- **#8 NPECF（DSS 2020）**：网络投影做符号边分类，处理稀疏与非平衡 → 迁移为"文件-符号网络的投影 + 边分类"做函数级定位排序（对照 Explorative Anchoring 的 +2.2pp 收益，图方法还有结构增益空间）。
- **#33 DPA-LR（ISR 2023）**：多样性偏好感知链接推荐（DPMS/Precision/Recall/F1 全面更优，p<0.001）→ 迁移为"探索-利用平衡"：既读最相关文件，也读多样性文件（不同模块/不同抽象层），防止上下文同质化导致的漏判。
- 与 #21 GCNN/KVP（DSS 2021）的联动见方向 C：探索轨迹本身也是事件序列。

---

## 7. 对 coding agent 的算法研究方向建议

1. **仓库图 link/sign prediction 上下文选择器（最优先）**
   - 构建仓库依赖图（call/inheritance/import/文档-代码共现边），把"给定任务，读哪些文件"定义成链接预测、把"该文件是否相关"定义成符号预测；
   - 用 GASP 式图增强处理稀疏标注；用 NPECF 式网络投影处理大规模仓库；
   - 产出可解释的选择器（给出"为什么读这个文件"的图路径），对标 Libra 的可解释性；
   - 数据：SWE-bench Verified 的 gold patch 可自动生成弱标注（gold patch 触及的文件=正样本），全部公开可获取。

2. **ACRR 驱动的冗余度闭环**
   - 把 ACRR（arXiv:2607.13034）作为训练目标之一，学习"该读多少"；
   - 与 SWE-Pruner 式裁剪结合：先预测冗余，再裁剪，再验证 resolve rate 不降。

3. **探索策略的 RL 化**
   - 把探索轨迹建模为 MDP（状态=已读文件集合+失败信息；动作=读哪个文件/符号/停止），用策略优化训练探索器；
   - 失败驱动更新（Libra 思路）作为奖励信号的一部分。

4. **指标**
   - resolve rate（SWE-bench Verified/Pro）、token 消耗、cost/task、检索 precision/recall@k（file-level）、ACRR、定位步数、覆盖率（line-level，SWE-Explore 定义）。

---

## 8. 参考文献

- [1] Qin & Xie. "Agent Retrieval Bench." arXiv:2607.24882.
- [2] Zhang & Wang. "SWE-Explore." arXiv:2606.（2026-06-04，Semantic Scholar 可查）。
- [3] "FastContext." arXiv:2606.14066.
- [4] "Libra." arXiv:2607.00016.
- [5] "SWE-Pruner." arXiv:2601.16746.
- [6] "SWE-Pruner Pro." arXiv:2607.18213.
- [7] Yin & Feng. "Do AI Agents Know When a Task Is Simple? (ACRR/E3)." arXiv:2607.13034.
- [8] "LARGER." arXiv:2605.16352.
- [9] "Explorative/Deterministic Anchoring." arXiv:2606.26979.
- [10] "Co-Coder." arXiv:2606.00953.
- [11] "Exploration Structure in LLM Agents for Multi-File Change Localization." arXiv:2606.11976.
- [12] "Retrieval-Augmented Code Generation Survey." arXiv:2510.04905.
- [13] "AceCoder." arXiv:2303.17780.
- [14] "RLCoder." arXiv:2407.19487.
- [15] Cherny-Shahar & Yehudai. "Repository Intelligence Graph." 2026-01.
- [16] "Effective Context Retrieval via Partial Dependency Graph." arXiv:2608.01927.
- [17] "AOCI: symbolic-semantic indexing." Semantic Scholar.
- [18] "CodexGraph." GitHub.
- [19] Bevziuk & Fatula. "Vector Graph-Based Repository Understanding." 2025-10.
- [20] "RAG-APR (KGCompass comparison)." arXiv:2603.29067.
- [21] Gloaguen, et al. "Evaluating AGENTS.md." arXiv:2602.11988.
- [22] "Sense and Sensitivity." ACL 2026.
- [23] Liu, et al. "Lost in the Middle." 2024b.
- [24] "Tokalator." arXiv:2604.08290.
- [25] GASP. "A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks." JAIS 2025. DOI:10.17705/1jais.00941.
- [26] NPECF. "Network projection-based edge classification framework for signed networks." DSS 2020. DOI:10.1016/j.dss.2020.113321.
- [27] DPA-LR. "Diversity Preference-Aware Link Recommendation for Online Social Networks." ISR 2023. DOI:10.1287/isre.2022.1174.
- [28] GCNN/KVP. "Process data properties matter." DSS 2021. DOI:10.1016/j.dss.2021.113494.