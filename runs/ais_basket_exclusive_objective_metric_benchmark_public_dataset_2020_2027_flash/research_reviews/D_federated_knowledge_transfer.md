# 方向 D：联邦知识迁移（Federated Knowledge Transfer）——全面文献综述

- 综述编号：D
- 撰写日期：2026-08-18（基于 2026-08 联网检索，arXiv/会议出处均经二次核验）
- 关联 51 篇锚点：#41 FedKT（DSS，DOI:10.1016/j.dss.2023.114084，联邦知识迁移信用评分；Loan Data/HMEQ/Taiwan/GMSC/Home Credit 五个公开数据集；IID 与 Non-IID 划分下 Accuracy/Recall/F1/KS 优于 FedAvg/FedProx/FedCodl 及非联邦 LR/RF/XGBoost，含 Friedman 检验）
- 一句话结论：**联邦学习（FL）在信用评分等 IS 场景已验证（#41 FedKT），LLM 联邦化在通用领域已有大量方法（蒸馏、LoRA、RLHF），但"多组织私有代码库不出域、联邦微调 coding LLM/共享安全偏好"的工作极少——这是与 IS 51 篇衔接最直接、又几乎没有对手的方向。**

---

## 1. 问题背景

企业代码是高度敏感的私有资产（合规、商业秘密），不能出域训练；但单组织数据量不足以微调出好用的 coding agent。联邦学习提供"数据不动、模型动"的路径：

- 多组织各自私有代码库 → 联邦微调 coding LLM（LoRA 等参数高效方式）；
- 服务器端蒸馏：各客户端本地微调的小模型/低秩适配器 → 蒸馏到大服务器模型（FedKT 2024 模式）；
- 联邦 RLHF/DPO：共享"安全偏好"（哪些行为可接受）而非代码本身——与方向 A 的防御训练直接耦合；
- 联邦数据估值：跨组织贡献付费（衔接方向 F 的 Shapley）。

51 篇 #41 FedKT 证明了 IS 范式：Non-IID 分布下知识迁移比简单 FedAvg 更优，且在 5 个公开数据集上可复现。本综述梳理：FL 方法谱系、LLM 联邦化、安全与隐私、代码领域 FL、研究缺口。

---

## 2. 检索范围与方法

- 检索时间：2026-08；来源：arXiv、IEEE/ACM 会议与期刊、Pattern Recognition、ICML、Semantic Scholar。
- 时间窗：2020–2026-08。
- 关键词：`federated learning` / `knowledge distillation federated` / `federated LLM` / `federated fine-tuning` / `FedKT` / `federated code` / `privacy-preserving code model` / `federated RLHF` 等。
- 纳入标准：① FL 知识迁移/蒸馏方法；② LLM 联邦化；③ 代码/软件工程领域 FL；④ FL 安全隐私。

---

## 3. 现状：FL 知识迁移方法谱系

### 3.1 "FedKT"两个同名工作（必须区分）
- **FedKT（Li et al., 2020，arXiv:2010.01017）**：one-shot、model-agnostic 的联邦知识迁移框架；支持差分隐私变体、连续手套（continual glove）与多分类扩展；核心是"不交换数据、只交换模型蒸馏"。
- **FedKT（2024，Pattern Recognition）**：server-side distillation + client-side constrained optimization，专门抗 Non-IID drift。
- **注意**：51 篇 #41 的 FedKT 是 IS 领域 DSS 信用评分论文（DOI:10.1016/j.dss.2023.114084），**方法同名但领域与实现不同**——这本身就是"IS 贡献与 CS 方法同名共存"的典型案例，引用时务必标明 DOI。

### 3.2 蒸馏/异构客户端
- **FedEKT**（IEEE 2024）：异构客户端（不同规模模型）→ 大服务器模型的知识转移。
- **FedHKT**：层次化知识转移（hierarchical knowledge transfer）。
- **FedET / Ensemble**：联邦集成蒸馏。
- **Fed-PLoRA**（arXiv:2602.16936）：联邦 PLoRA（个性化低秩适配）。
- **FedEx-LoRA**（arXiv:2410.09432）：LoRA 联邦交换/共享（exLoRA）。
- **FedICU**（ICML 2025）：联邦"一致性更新"（ICU）方法。
- **FedCoLLM**（FATE 开源生态）：社区开源的联邦 LLM 微调框架。
- **CFLHKD**（arXiv:2512.10443）：聚类 + 多教师蒸馏，提升 +7.57 个百分点——适合客户端分布差异大的场景。

### 3.3 LLM 联邦化
- **FL 安全综述**（arXiv:2508.13730）：200+ 篇 FL 安全论文的系统综述（攻防全景）。
- **Federated LLMs: Feasibility, Robustness, Security**（arXiv:2505.08830）：专门讨论 LLM 联邦化的可行性、鲁棒性与安全。
- **SPEAR 梯度反演**（arXiv:2403.03945）：从梯度恢复训练数据的攻击——联邦微调 LLM 时"梯度即数据"风险。
- **拜占庭鲁棒聚合**：恶意客户端投毒防御（聚合规则研究）。
- **隐私跨 silo**（arXiv:2503.04451）：跨机构（cross-silo）FL 的隐私方案。
- **数据高估攻击 + Truth-Shapley**（arXiv:2502.00494）：客户端谎报数据价值 → Truth-Shapley 抗谎报估值（衔接方向 F）。
- **IPSS**（arXiv:2504.16668）：数据估值的采样近似，降低 Shapley 计算成本。

### 3.4 代码/软件工程领域 FL（直接相关但少）
- **FedAvg 开源 SE 模型共同训练**（arXiv:2404.06201）：用联邦学习共同训练软件工程模型（不共享代码）。
- **IDE 自动补全差分隐私**（ACM 2026）：补全模型的差分隐私联邦训练。
- **PrivCode**（arXiv:2512.05459）：隐私保护代码模型。
- **code-smell 检测联邦学习**（arXiv:2306.00038）：跨组织代码质量检测的 FL。
- 观察：这些工作停留在"经典模型/检测任务"，**没有在 SWE-bench 级任务上评估联邦微调 coding agent**。

---

## 4. 研究缺口（核心结论）

1. **联邦微调 coding LLM 的端到端评估缺失**：没有工作回答"10 个组织的私有仓库联邦微调后，SWE-bench Verified resolve rate 相比单组织微调/FedAvg 基线提升多少"。
2. **服务器端蒸馏未用于代码**：FedKT 2024 / FedEKT 的"异构客户端 → 大服务器模型"模式没有在代码领域验证。
3. **联邦 RLHF/DPO 安全偏好未用于 coding agent**：方向 A 需要"防御训练数据"，而各组织的"安全偏好"（哪些 prompt/行为必须拒绝）可以联邦共享——这既是防御也是隐私。
4. **Non-IID 度量缺失**：#41 FedKT 用 5 数据集做 Non-IID 验证，代码领域连"客户端分布偏移"的度量标准都没有。
5. **估值与激励**：跨组织贡献付费（Truth-Shapley）在代码场景未落地。

---

## 5. 与 51 篇 IS 文献的衔接

- **#41 FedKT（DSS）**：直接模板——Non-IID 联邦知识迁移 + 公开数据集验证 + 统计检验（Friedman）。迁移到代码：客户端=组织，数据集=私有仓库（可评测时用公开仓库模拟），目标=resolve rate / 代码质量指标。
- 与 #50 Shapley Data Masking（MISQ 2026）衔接：联邦共享前对代码做特征级掩蔽，量化披露风险（见方向 F）。
- 与 #49 RADAR（MISQ 2025）衔接：联邦"安全偏好"蒸馏可作为防御训练数据来源（见方向 A）。

---

## 6. 对 coding agent 的算法研究方向建议

1. **联邦微调 coding LLM（最优先）**
   - 设置：多个模拟客户端组织（用公开仓库子集划分模拟 Non-IID，全部公开可获取）；
   - 方法：FedAvg + Fed-PLoRA/FedEx-LoRA 参数高效联邦微调；对比单组织、集中式、FedKT 蒸馏；
   - 评估：SWE-bench Verified resolve rate、各客户端性能方差（Non-IID 鲁棒性）、通信量、隐私预算。

2. **服务器端蒸馏到 SLM**
   - 各客户端在本地私有数据上微调小模型/LoRA → 服务器聚合蒸馏成大模型（FedKT 2024 模式）；
   - 目标：让大模型获得跨组织知识而不接触任何代码。

3. **联邦安全偏好学习**
   - 各组织只共享"安全/不安全轨迹的偏好对"（脱敏），联邦 DPO/RLHF 训练鲁棒性（衔接方向 A）；
   - 用 AgentDojo/JAWS-Bench 的公开攻击构造偏好对，验证 ASR 下降同时 resolve rate 不降（防 Autonomy Tax）。

4. **指标**
   - resolve rate、Non-IID 方差、ASR（若做安全偏好）、隐私预算（ε）、通信轮次/字节、Shapley 估值公平性（衔接方向 F）。

---

## 7. 参考文献

- [1] FedKT (credit scoring). "A novel federated learning approach with knowledge transfer for credit scoring." Decision Support Systems. DOI:10.1016/j.dss.2023.114084.（51 篇 #41）
- [2] Li et al. "FedKT: Federated Knowledge Transfer." arXiv:2010.01017.
- [3] "FedKT (server-side distillation)." Pattern Recognition 2024.
- [4] "FedEKT." IEEE 2024.
- [5] "FedHKT." hierarchical knowledge transfer.
- [6] "FedET / Ensemble."
- [7] "Fed-PLoRA." arXiv:2602.16936.
- [8] "FedEx-LoRA." arXiv:2410.09432.
- [9] "FedICU." ICML 2025.
- [10] "FedCoLLM." FATE open source.
- [11] "CFLHKD." arXiv:2512.10443.
- [12] "FL Security survey (200+ papers)." arXiv:2508.13730.
- [13] "Federated LLMs: Feasibility, Robustness, Security." arXiv:2505.08830.
- [14] "SPEAR: gradient inversion." arXiv:2403.03945.
- [15] "Privacy cross-silo." arXiv:2503.04451.
- [16] "Truth-Shapley + overvaluation attack." arXiv:2502.00494.
- [17] "IPSS sampling." arXiv:2504.16668.
- [18] "FedAvg for open-source SE models." arXiv:2404.06201.
- [19] "IDE autocomplete differential privacy." ACM 2026.
- [20] "PrivCode." arXiv:2512.05459.
- [21] "Federated code-smell detection." arXiv:2306.00038.