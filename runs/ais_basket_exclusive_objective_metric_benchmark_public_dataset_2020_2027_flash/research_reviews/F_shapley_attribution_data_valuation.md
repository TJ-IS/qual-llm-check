# 方向 F：Shapley 归因与数据估值（Shapley Attribution & Data Valuation）——全面文献综述

- 综述编号：F
- 撰写日期：2026-08-18（基于 2026-08 联网检索，arXiv/会议出处均经二次核验）
- 关联 51 篇锚点：#50 Shapley Value-Based Feature Attribution for Data Masking（MISQ 2026，DOI:10.25300/misq/2025/18502）
- 一句话结论：**Shapley 值在数据估值、上下文归因、提示归因三个子领域都已成熟且活跃；#50 把 Shapley 用于"数据共享前的披露风险-效用权衡"（risk-only vs risk-utility 两个目标函数 + 掩蔽特征与噪声水平选择），这条"归因→掩蔽→效用保持"链路可以直接迁移到 coding agent 的三个新场景：上下文文件归因（哪些文件贡献最大可裁剪）、私有代码共享前脱敏、prompt 组件归因（few-shot/system prompt 组件贡献）。**

---

## 1. 问题背景

Shapley 值（合作博弈论）的核心承诺：把"总产出"公平地分配到"参与方"，满足效率、对称性、哑元、可加性四个公理。在数据科学中它有三种典型用法：

1. **数据估值**：每条数据/每个客户端对模型性能的边际贡献（→ 定价、付费、去重）；
2. **特征归因**：每个特征对预测的贡献（→ 解释性、掩蔽决策）；
3. **上下文归因**：每个上下文片段（文件、段落、工具输出）对生成结果的贡献（→ 裁剪、调试、引用）。

51 篇 #50（MISQ 2026）把特征归因用于**数据掩蔽**：数据共享前，用 Shapley 值量化每个特征对披露风险的贡献，据此选择掩蔽哪些特征、加多少噪声，在降披露风险的同时保持数据效用。其预印本（arXiv:2607.28946，Darku 等，2026-08-03）进一步给出 disclosure risk 与 data utility 双维度 + risk-utility frontier（风险-效用前沿）。

Coding agent 侧的对应问题：

- **上下文归因**：一个补丁是读了哪些文件/工具输出后产生的？哪些上下文贡献大（可裁剪）、哪些是噪声（可丢弃）？→ 衔接方向 B/C；
- **私有代码共享前掩蔽**：企业把代码片段给第三方（外包、训练数据、联邦共享）前，哪些特征（标识符、路径、依赖）泄露了商业信息？→ 衔接方向 D；
- **prompt 组件归因**：few-shot 示例、system prompt 组件、工具描述对最终成功贡献多大？→ 衔接方向 A（工具描述是最弱环节）与 B。

---

## 2. 检索范围与方法

- 检索时间：2026-08；来源：arXiv、MISQ/ISR 等 IS 期刊、EMNLP/ICML/NeurIPS、Mathematics/IEEE 期刊、Semantic Scholar。
- 时间窗：2019（KNN-Shapley 等经典）至 2026-08。
- 关键词：`Shapley value data valuation` / `data masking Shapley` / `context attribution LLM` / `citation generation` / `prompt attribution` / `federated Shapley` / `feature attribution code` 等。
- 纳入标准：① Shapley 数据估值/特征归因/上下文归因；② 与数据共享、隐私、代码、联邦相关的 Shapley 应用。

---

## 3. 现状：数据估值与特征归因

### 3.1 数据估值
- **The Shapley Value in Data Science**（Mathematics 2025）：系统综述——Shapley 在数据科学中的全部用法与计算加速。
- **Data Asset Value Change 综述**（IEEE 2025）：数据资产价值变化测度综述——从"数据价值"到"数据资产会计"。
- **Asymmetric Data Shapley**（arXiv:2511.12863）：结构感知的数据市场——不对称结构（分层、联邦）下的估值。
- **CHG Shapley**（arXiv:2406.11730）：组合层次图（combinatorial hierarchical）Shapley，处理结构化数据。
- **KNN-Shapley 经典系**（Ghorbani & Zou 2019 起）：kNN 上可高效计算的 Shapley 估值——工业界可用性的起点。

### 3.2 上下文归因（LLM 生成结果 ← 上下文）
- **TracLLM**：长上下文 traceback——追踪生成结果来自哪个上下文片段。
- **SelfCite**（arXiv:2502.09604）：自引用生成——模型自己判断哪些上下文片段支撑了回答。
- **SynQA**（arXiv:2504.05317）：合成问答归因评测。
- **Jensen-Shannon attribution**（arXiv:2505.16415）：基于 JS 散度的归因方法。
- **Attribution/Citation/Quotation survey**（arXiv:2508.15396）：归因/引用/引用表述三者的全面综述。
- 观察：上下文归因主要面向 RAG/长文档问答，**没有专门面向"代码补丁 ← 仓库文件/tool 输出"的归因工作**。

### 3.3 提示/推理归因
- **SalaMAnder**（Findings of EMNLP 2025）：对 CoT 中的数学表达式做 Shapley 归因——推理链组件的贡献。
- **Code authorship attribution**（arXiv:2501.08165）：LLM 生成代码的作者归属，top-1 准确率 65%——代码侧归因的先例。

### 3.4 联邦数据估值（衔接方向 D）
- **Truth-Shapley + overvaluation attack**（arXiv:2502.00494）：客户端谎报数据价值时 Truth-Shapley 的抗谎报估值。
- **IPSS**（arXiv:2504.16668）：数据估值采样近似（IPSS），大幅降低 Shapley 计算成本。
- **Federated credit weighting Shapley**（Sensors 2025）：联邦信用加权 Shapley 的工程化。

---

## 4. 研究缺口（核心结论）

1. **代码补丁级上下文归因缺失**：TracLLM/SelfCite 面向文本问答；"这个补丁行来自哪个文件/哪次工具输出"的归因（token/行级）没有系统工作——这是方向 B（裁剪）与 C（轨迹效率）都需要的"解释层"。
2. **数据掩蔽未用于代码共享**：#50 在信用/薪资数据上验证，代码数据（标识符、路径、依赖、注释语义）的特征化披露风险建模没有对应工作。
3. **prompt 组件归因未用于 coding agent**：few-shot 示例、system prompt、工具描述对 resolve rate 的 Shapley 贡献没人系统测过；工具描述又是攻击面（QueryIPI）——归因可以直接指导"该加固哪句话"。
4. **计算成本**：Shapley 指数级复杂度在长上下文/大仓库上不可行，需要 KNN-Shapley/IPSS 式近似 + 代码领域特定的截断策略。
5. **与联邦结合**：跨组织贡献付费（#41 FedKT 场景 + Truth-Shapley）没有在代码联邦微调上落地。

---

## 5. 与 51 篇 IS 文献的衔接

- **#50 Shapley Data Masking（MISQ 2026）**：直接模板——特征级披露风险 Shapley 归因 + risk-utility 双目标 + 掩蔽决策。迁移：代码特征（符号、路径、依赖、注释）作为"特征"，第三方推理风险作为"披露风险"，代码可用性（编译通过率、下游任务性能）作为"效用"。
- **#41 FedKT（DSS）**：联邦场景的数据估值需求——哪个组织贡献了最多知识（衔接方向 D 的 Truth-Shapley）。
- **#21 GCNN/KVP（DSS 2021）**：事件属性归因——预测下一步动作时，哪些历史事件贡献最大（衔接方向 C）。
- 与方向 B/C 的互证：Shapley 上下文归因可以给 ACRR（过度阅读指标）提供"到底哪些文件是冗余的"的精确答案。

---

## 6. 对 coding agent 的算法研究方向建议

1. **补丁级上下文归因（最优先）**
   - 用 SWE-bench Verified 的公开轨迹 + gold patch：把补丁行对齐到轨迹中的文件读取/工具输出；
   - 用 Shapley（或近似：KNN-Shapley、IPSS、JS 归因）量化每个上下文片段的贡献；
   - 产出："裁剪报告"——哪些文件对最终补丁零贡献（衔接 B 的 ACRR + C 的 token 削减）；
   - 指标：归因稳定性、裁剪后 resolve rate 保持率、token 减少量。

2. **代码数据掩蔽**
   - 建模代码"披露特征"（专有标识符、路径结构、依赖组合、注释语义）；
   - 用 #50 的 risk-utility 双目标选择掩蔽特征与噪声水平（标识符重命名、路径泛化、依赖剪枝）；
   - 评估：披露风险下降 vs 下游任务（补全/修复）效用保持；
   - 数据：公开代码库模拟"敏感特征"（如把特定开源项目的专有部分设为敏感）。

3. **prompt 组件归因与加固**
   - 对 few-shot 示例、system prompt 段落、工具描述做 Shapley 归因（resolve rate 为效用）；
   - 高贡献组件优先加固（衔接方向 A：工具描述是攻击面）；
   - 指标：组件贡献排名、移除低贡献组件后的 token 与成本下降。

4. **联邦贡献估值**
   - 在联邦微调 coding LLM（方向 D）中，用 Truth-Shapley 算各组织贡献并防谎报；
   - 指标：估值公平性、抗谎报率、计算开销。

---

## 7. 参考文献

- [1] "Shapley Value-Based Feature Attribution for Data Masking." MIS Quarterly vol 50 no 1, 2026. DOI:10.25300/misq/2025/18502.（51 篇 #50）
- [2] Darku, et al. "Shapley Value-Based Feature Attribution for Data Masking" (preprint). arXiv:2607.28946.
- [3] "The Shapley Value in Data Science." Mathematics 2025.
- [4] "Data Asset Value Change survey." IEEE 2025.
- [5] "Asymmetric Data Shapley." arXiv:2511.12863.
- [6] "CHG Shapley." arXiv:2406.11730.
- [7] Ghorbani & Zou. "KNN-Shapley." 2019 起系列。
- [8] "TracLLM." long-context traceback.
- [9] "SelfCite." arXiv:2502.09604.
- [10] "SynQA." arXiv:2504.05317.
- [11] "Jensen-Shannon attribution." arXiv:2505.16415.
- [12] "Attribution/Citation/Quotation survey." arXiv:2508.15396.
- [13] "SalaMAnder." Findings of EMNLP 2025.
- [14] "Code authorship attribution." arXiv:2501.08165.
- [15] "Truth-Shapley + overvaluation attack." arXiv:2502.00494.
- [16] "IPSS sampling." arXiv:2504.16668.
- [17] "Federated credit weighting Shapley." Sensors 2025.
- [18] FedKT (credit scoring). DSS. DOI:10.1016/j.dss.2023.114084.（51 篇 #41）
- [19] GCNN/KVP. DSS 2021. DOI:10.1016/j.dss.2021.113494.（51 篇 #21）
- [20] Yin & Feng. "ACRR/E3." arXiv:2607.13034.