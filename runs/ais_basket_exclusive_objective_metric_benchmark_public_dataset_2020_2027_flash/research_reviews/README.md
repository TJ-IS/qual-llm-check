# Coding Agent 研究方向文献综述索引（六方向）

- 撰写日期：2026-08-18
- 检索时间：2026-08（联网检索，arXiv 编号/会议出处均经二次核验）
- 背景：基于 51 篇筛选结果（`output_v1/final_report_51_included_cn.md`，2020–2027 AIS 篮子期刊、公开数据集、客观指标提升）衍生的六个研究方向综述。
- 共同逻辑：每个方向均以 51 篇中被点名的论文为锚点，回答"IS 文献已验证的算法范式能否迁移到现代 coding agent（接入 LLM 的辅助编程智能体），以提升某个重要指标"。

## 文档列表

| 文件 | 方向 | 51 篇锚点 | 核心结论 | 目标指标 |
|---|---|---|---|---|
| [A_coding_agent_adversarial_robustness.md](A_coding_agent_adversarial_robustness.md) | A：对抗鲁棒性 | #49 RADAR、#26 ARText、#21 GCNN/KVP | 攻击侧成熟、防御侧偏浅；RADAR 范式（DRL 攻击器 + minimax 鲁棒训练）在 coding agent 上是空位 | ASR、Robust Resolve Rate、FPR |
| [B_context_selection_repo_awareness.md](B_context_selection_repo_awareness.md) | B：上下文选择/仓库态势感知 | #46 GASP、#8 NPECF、#33 DPA-LR | 仓库图 link/sign prediction 驱动上下文选择无系统工作；oracle headroom 与 ACRR（过度阅读 ~91%）量化了空间 | resolve rate、token、ACRR、检索 P/R@k |
| [C_trajectory_efficiency_action_prediction.md](C_trajectory_efficiency_action_prediction.md) | C：轨迹效率/动作预测 | #21 GCNN/KVP、#49 RADAR | coding agent 轨迹=事件日志，但 next-event 预测范式（GCNN/KVP）未迁移；"预测驱动"削减是空位 | next-action accuracy、剩余步数 MAE、cost/task |
| [D_federated_knowledge_transfer.md](D_federated_knowledge_transfer.md) | D：联邦知识迁移 | #41 FedKT | 联邦微调 coding LLM / 服务器蒸馏 / 联邦安全偏好均未在 SWE-bench 级评估 | resolve rate、Non-IID 方差、隐私预算 |
| [E_detection_fraud_anomaly.md](E_detection_fraud_anomaly.md) | E：检测/欺诈/异常 | #25、#26、#28、#30、#32、#11 | IS 特征工程/图结构/众包弱标签方法论未迁移到恶意 prompt/skill/轨迹检测 | P/R/F1/AUC、检测延迟、误报率 |
| [F_shapley_attribution_data_valuation.md](F_shapley_attribution_data_valuation.md) | F：Shapley 归因/数据估值 | #50 Shapley Data Masking | 补丁级上下文归因、代码数据掩蔽、prompt 组件归因三个新场景空白 | 归因稳定性、效用保持率、披露风险下降 |

## 总体结论（跨方向）

1. **51 篇全部是算法开发型论文**（新方法/模型/框架 + 公开数据 + 与基线/SOTA 对比客观指标提升），与 coding agent 结合最直接的是 A、C、B 三档。
2. **A 方向（对抗鲁棒）最推荐**：#49 RADAR 提供完整范式（DRL 攻击器 + RL-RO 鲁棒化 + 逃避率/效用双指标），攻击基准（JAWS-Bench、AgentDojo、MalSkillBench、FCV）全部公开可获取，RL 攻防训练在通用 agent 上已被 ICML 2026 系列验证，但**尚无把 RADAR 范式落地 coding agent 的工作**。
3. **风险警示**：防御训练存在 Autonomy Tax（arXiv:2603.19423，防御训练后 99% 任务超时 vs 基线 13%），任何鲁棒化研究必须同时报告良性效用，否则评估误判。
4. **指标统一**：AgentDojo 的 "Benign Utility + ASR" 与 RADAR 的 "ER + FPR + 鲁棒化效用" 同构，可直接作为 coding agent 鲁棒性的标准双指标。
5. 所有建议方向的数据集（SWE-bench Verified/Pro、AgentDojo、JAWS-Bench、MalSkillBench、公开仓库模拟）均满足"公开可查到、可获取"的新筛选要求。