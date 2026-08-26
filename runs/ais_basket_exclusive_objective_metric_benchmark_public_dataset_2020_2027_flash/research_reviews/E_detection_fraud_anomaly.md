# 方向 E：检测类研究迁移——欺诈/异常/恶意行为检测（Fraud, Anomaly & Malicious Behavior Detection）——全面文献综述

- 综述编号：E
- 撰写日期：2026-08-18（基于 2026-08 联网检索，arXiv/会议出处均经二次核验）
- 关联 51 篇锚点：#25 欺诈网站检测（DSS 2022）、#26 ARText 对抗鲁棒性设计框架（JMIS 2022）、#28 欺诈评论（DSS 2022）、#30 假评论者检测（DSS 2023）、#32 社交机器人检测（ISR 2023）、#11 "Wolf of Wall Street" 金融中介不当行为检测（JAIS 2020）
- 一句话结论：**IS 51 篇中检测类论文提供了三件可迁移资产——特征工程（#28/#30）、图结构建模（#32 众包标签、#25 请求结构）、鲁棒性度量框架（#26 ARText）；而 coding agent 的威胁对象（恶意 prompt、恶意 skill、异常轨迹、数据外泄）与欺诈/机器人检测在问题结构上同构，但"把 IS 检测范式迁移到 coding agent 行为检测"的工作目前只有零星探索，且没有使用 IS 的特征工程方法论。**

---

## 1. 问题背景

IS 检测文献处理的经典问题：

- 欺诈网站（#25）：从第三方请求结构（RS 特征）判别欺诈，CS5 准确率 0.728→0.805；
- 欺诈评论（#28）：情感表达 + 显式方面特征工程 + M-SMOTE 不平衡处理；
- 假评论者（#30）：行为特征 + 文本信息联合深度学习；
- 社交机器人（#32）：众包反应作为弱标签增强检测（BERT 基线对比）；
- 金融中介不当行为（#11）：外部验证信息（监管确认）提升检测；
- 对抗鲁棒性（#26）：性能比率 + 性能-扰动曲线下面积度量鲁棒性。

Coding agent 侧的对应威胁：

- **恶意 prompt/注入**（方向 A 的攻击载体）→ 类似"欺诈评论"，需要检测"文本表面正常但意图恶意"；
- **恶意 skill 包**（DDIPE/PhantomSkill）→ 类似"欺诈网站"，需要从"结构特征"（依赖、行为模式）判别；
- **异常 agent 轨迹**（被注入后行为漂移）→ 类似"机器人检测"，需要行为序列建模；
- **数据外泄**（agent 偷偷读敏感文件/外发）→ 类似"不当行为检测"，需要外部验证信号。

本综述梳理：coding agent 行为异常检测、恶意代码/漏洞检测、文本欺骗检测、社交机器人检测、钓鱼/恶意 URL 检测的现状，以及可迁移的 IS 方法。

---

## 2. 检索范围与方法

- 检索时间：2026-08；来源：arXiv、NeurIPS/ICML/ACL、Neurocomputing、EPJ Data Science、Semantic Scholar。
- 时间窗：2023–2026-08，重点 2025–2026。
- 关键词：`agent anomaly detection` / `LLM agent monitoring` / `malicious code detection LLM` / `fake review detection` / `social bot detection` / `phishing URL detection` / `LLM spam detection` 等。
- 纳入标准：① 直接检测 agent/LLM 行为异常；② 或检测对象与 coding agent 威胁同构（恶意代码、欺骗文本、机器人、钓鱼）。

---

## 3. 现状：Coding Agent 行为异常检测（最新、最空）

- **Trajectory Guard**（arXiv:2601.00516）：Siamese Recurrent Autoencoder + 混合损失，**无标签**实时轨迹异常检测——不需要人工标注攻击轨迹，用正常轨迹训练即可发现偏离；这是与 #30"行为特征"、#28"特征工程"最接近的 agent 侧工作。
- **AgentSight**（arXiv:2508.02736）：eBPF 系统级可观测——在内核层观察 agent 的系统调用，检测到凭据访问、外发等异常行为。
- **VIGIL**（arXiv，2025-12）：reflective runtime——agent 运行时自我反思监控。
- **Real-Time Detection and Repair of LLM Agent Failures**（arXiv:2608.02464）：content-grounding telemetry（内容接地遥测），检测能力从 0.07 提升到 0.90——先检测失败再自动修复。
- **Uber ADR Sensor**：工业界参考——覆盖 credential exfiltration（凭据外泄）、prompt injection、supply chain、anomalous burst（异常突发）四类信号。
- 观察：这些工作证明"轨迹/系统级检测"可行，但**特征设计粗糙**（多为统计阈值），没有用 IS 的精细特征工程（情感、方面、行为序列、图结构）。

---

## 4. 现状：恶意代码/漏洞检测（LLM 时代）

- **IRIS**（arXiv:2508/2509 系列）：neuro-symbolic——LLM + 静态分析融合，整仓推理找漏洞。
- **VulSolver**（arXiv:2509.00882）：LLM 漏洞定位与修复求解。
- **VulnLLM-R**（arXiv:2512.07533）：LLM 漏洞检测的鲁棒性研究。
- **LLM Vulnerability Discovery 综述**（Code Metrics，arXiv:2509 系列）：LLM 找漏洞能力的系统盘点。
- **PYPILINE**（arXiv:2606 系列）：恶意 PyPI 包检测流水线——供应链检测工程实践。
- 衔接点：恶意 skill 包检测（MalSkillBench/DDIPE 的攻击对象）可以复用这些"恶意包/恶意代码"特征。

---

## 5. 现状：文本欺骗/评论/机器人/钓鱼（IS 相邻领域）

### 5.1 假评论与 spam
- **LLM 生成 spam reviews 检测**（Semantic Scholar，2025-10）：LLM embedding + GNN——用图结构捕获"生成评论团伙"；与 #30（行为+文本）、#28（情感+方面）直接同构。
- **fake review deep hybrid**：文本 + 评分 + 方面（aspect）深度混合模型。
- **ReviewGuard**（arXiv:2510.16549）：评论防护框架。
- **Reviewer 对抗攻击**（arXiv:2506.11113）：对评论者检测器的对抗攻击——提醒检测器本身需要鲁棒性（衔接 #26）。

### 5.2 社交机器人
- **BotLGT**（Neurocomputing 2025）：LLM + graph transformer 的机器人检测。
- **MM-HGT-Bot**（EPJ Data Science 2025）：多模态异构图 transformer——文本 + 关系 + 时序。
- 衔接点：#32 的"众包反应弱标签"思路在 agent 场景对应"人类开发者对可疑 PR/agent 行为的投票标记"。

### 5.3 钓鱼/恶意 URL
- **Role-Aware Multi-modal FL phishing**（arXiv:2509.22369）：多模态联邦学习钓鱼检测。
- **Graph-Attentive LSTM**（2025）：图注意 LSTM 恶意 URL。
- **hybrid DL + anomaly**（arXiv:2512.03462）：深度 + 异常混合。
- **BERT URL phishing**；**character-level CNN ensemble**（arXiv:2512.16717）。
- 衔接点：agent 调用外部 URL/API 前做 URL 信誉检测——直接可用的工程组件。

---

## 6. 研究缺口（核心结论）

1. **IS 特征工程方法论未迁移**：agent 行为检测目前是"统计阈值/embedding 相似度"级别；#28 的情感+方面特征、#30 的行为序列特征、#25 的结构特征（请求结构→工具调用结构）方法论没有被用于"恶意 prompt/skill/轨迹"检测。
2. **图结构检测缺失**：LLM+图（BotLGT/MM-HGT）在机器人领域有效，但"agent-工具-文件-仓库"异构图上的异常检测没有系统工作（方向 B 的仓库图 + 本方向的异常检测可合并）。
3. **弱标签众包未用**：#32 证明众包弱标签能增强检测；coding agent 的 PR 评审/issue 讨论天然提供弱标签（哪些提交被驳回/标记恶意）。
4. **检测器本身的鲁棒性未评估**：Reviewer 对抗攻击（arXiv:2506.11113）提醒：检测器会被攻击；#26 ARText 的"性能-扰动曲线"框架可迁移为"检测器鲁棒性度量"。
5. **实时性指标缺失**：多数工作报告 P/R/F1，不报告检测延迟与误报对正常开发流程的干扰（agent 场景误报成本高——打断即损失）。

---

## 7. 与 51 篇 IS 文献的衔接

- **#28（DSS 2022）**：情感 + 显式方面特征工程 + M-SMOTE → "恶意 prompt"的意图特征（表面礼貌 vs 深层恶意）+ 恶意样本增强。
- **#30（DSS 2023）**：行为特征提取器 + 文本联合 → "恶意 skill"的行为画像（安装后行为序列）+ skill 描述文本。
- **#25（DSS 2022）**：第三方请求结构（RS）特征 → 工具的"第三方调用结构"特征（一个 skill 调用了哪些外部端点）。
- **#32（ISR 2023）**：众包弱标签 → 开发者社区对可疑 PR/agent 行为的投票。
- **#11（JAIS 2020）**：外部验证信息提升检测 → agent 行为的外部队列（git 历史、CI 日志、代码评审记录）作为验证信号。
- **#26（JMIS 2022）**：对抗鲁棒性设计框架 + 性能-扰动曲线 → 检测器的鲁棒性度量（直接衔接方向 A）。

---

## 8. 对 coding agent 的算法研究方向建议

1. **恶意 prompt/轨迹检测器（最优先）**
   - 特征：文本意图特征（#28 方法论）+ 动作序列行为特征（#30 方法论）+ 工具调用结构特征（#25 方法论）；
   - 模型：Siamese Recurrent Autoencoder（Trajectory Guard，无标签）+ 图 transformer（BotLGT 迁移）；
   - 数据：AgentDojo/JAWS-Bench/MalSkillBench 的公开攻击轨迹为恶意样本，正常 SWE-bench 轨迹为良性样本——全部公开可获取；
   - 指标：P/R/F1/AUC + 检测延迟 + 误报率。

2. **众包弱标签闭环**
   - 用公开 GitHub 仓库的 issue/PR 评审数据构造弱标签（驳回/标记可疑的提交）；
   - 训练后与人工评审对比，量化"检测器替代部分评审"的可行性（#32 验证过的范式）。

3. **检测器鲁棒性度量**
   - 用 #26 ARText 的性能-扰动曲线下面积评估检测器在对抗扰动（改写 prompt、混淆 skill）下的鲁棒性；
   - 与方向 A 的防御联动：检测器 + 鲁棒化训练双线。

4. **实时监控架构**
   - 参照 Uber ADR Sensor 的四类信号（凭据外泄/注入/供应链/异常突发）+ AgentSight 的系统级观测；
   - 输出可解释告警（命中哪些特征），降低误报对开发流程的干扰。

---

## 9. 参考文献

- [1] "Trajectory Guard." arXiv:2601.00516.
- [2] "AgentSight." arXiv:2508.02736.
- [3] "VIGIL reflective runtime." 2025-12.
- [4] "Real-Time Detection and Repair of LLM Agent Failures." arXiv:2608.02464.
- [5] "Uber ADR Sensor." 工程披露。
- [6] "IRIS: neuro-symbolic repository reasoning." arXiv:2508/2509.
- [7] "VulSolver." arXiv:2509.00882.
- [8] "VulnLLM-R." arXiv:2512.07533.
- [9] "LLM Vulnerability Discovery survey." Code Metrics, arXiv:2509.
- [10] "PYPILINE: malicious PyPI detection." arXiv:2606.
- [11] "LLM-generated spam review detection (embedding+GNN)." Semantic Scholar 2025-10.
- [12] "Fake review deep hybrid (text+rating+aspect)."
- [13] "ReviewGuard." arXiv:2510.16549.
- [14] "Adversarial attacks on reviewer detection." arXiv:2506.11113.
- [15] "BotLGT." Neurocomputing 2025.
- [16] "MM-HGT-Bot." EPJ Data Science 2025.
- [17] "Role-Aware Multi-modal FL phishing." arXiv:2509.22369.
- [18] "Graph-Attentive LSTM phishing." 2025.
- [19] "Hybrid DL + anomaly phishing." arXiv:2512.03462.
- [20] "Character-level CNN ensemble phishing." arXiv:2512.16717.
- [21] #25 "Analysis of third-party request structures to detect fraudulent websites." DSS 2022. DOI:10.1016/j.dss.2021.113698.
- [22] #26 "Assessing and Enhancing Adversarial Robustness of Predictive Analytics." JMIS 2022. DOI:10.1080/07421222.2022.2063549.
- [23] #28 "Fraudulent review detection model focusing on emotional expressions and explicit aspects." DSS 2022. DOI:10.1016/j.dss.2021.113728.
- [24] #30 "A deep learning approach for detecting fake reviewers." DSS 2023. DOI:10.1016/j.dss.2022.113911.
- [25] #32 "Augmenting Social Bot Detection with Crowd-Generated Labels." ISR 2023. DOI:10.1287/isre.2022.1136.
- [26] #11 "Who Is the Next 'Wolf of Wall Street'?" JAIS 2020. DOI:10.17705/1jais.00633.