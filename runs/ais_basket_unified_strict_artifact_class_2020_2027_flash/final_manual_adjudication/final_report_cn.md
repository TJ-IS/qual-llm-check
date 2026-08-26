# 2020–2027 AIS Basket 全文统一严格筛选报告

## 结论

本地 2020–2027 范围共有 2,475 篇全文（2027 年本地为 0 篇）。每篇全文单独提交给 `deepseek-v4-flash`，V3 全量筛选得到 27 篇模型候选；随后对 27 篇逐篇进行保守的全文反向审计，最终保留 17 篇，排除 10 篇。

- 模型候选率：27 / 2,475 = 1.09%
- 最终纳入率：17 / 2,475 = 0.69%
- 模型候选经最终审计后的精确率：17 / 27 = 62.96%
- 人工推翻模型阳性：10 / 27 = 37.04%
- 理论筛选：尚未应用；心理学相关理论按既定流程留作下一阶段细筛

模型适合用于把全集压缩为极小候选池，但在本研究的极严定义下不能把模型阳性直接当成最终纳入结果。

## 全量运行完整性

- 全文记录：2,475
- 唯一记录：2,475
- 待处理：0
- 全量 V3 prompt fingerprint：`3fe999fdfd248f34c4711cccbdeb03e8257448aab6ef4f86d0622060efe5c10c`
- 输入 tokens：79,712,471
- 输出 tokens：8,872,541
- 总 tokens：88,585,012
- 缓存命中输入 tokens：59,220,224
- 缓存未命中输入 tokens：20,492,247

运行中有 1 条历史格式错误，恢复后成功写入最终记录；它不属于纳入候选，未改变筛选结果。

## 最终纳入的 17 篇

| 年份 | 期刊 | 文献 | 核心客观终点 | 合格的软件制品类级贡献 |
|---:|---|---|---|---|
| 2020 | EJIS | Gamifying knowledge sharing in humanitarian organisations | KMS访问、新增资源、评论、点赞等日志行为 | KMS游戏化评分与环境反馈组件 |
| 2020 | JMIS | Effectiveness of Location-Based Advertising and the Impact of Interface Design | 真实点击率 | 位置广告应用的距离显示与排序界面 |
| 2020 | JMIS | Using Design-Science Based Gamification to Improve Organizational Security Training and Compliance | 实际钓鱼点击 | 游戏化SETA系统与设计原则 |
| 2020 | EJIS | Ingredients for successful badges | RFID记录的骑行天数 | 徽章、分享奖励与完成逻辑 |
| 2020 | DSS | A new emergency decision support system | 解释/情境化/可视化延迟及固定规则正确性 | 应急DSS架构、元模型和事件规则机制 |
| 2020 | EJIS | Feedback at scale | 评分时延、误报/漏报、完成率 | 大规模数字技能反馈系统的元需求与设计原则 |
| 2020 | DSS | Automated dynamic approach for detecting ransomware using finite-state machine | 事实标签上的TPR/FPR/准确率 | 运行的勒索软件保护应用及监听—FSM—阻断机制 |
| 2021 | JAIS | Design Principles for Robust Fraud Detection | 欺诈检测性能及对抗鲁棒性 | 欺诈检测系统设计原则与运行分类组件 |
| 2022 | JAIS | Designing Attentive Information Dashboards | 眼动注视、转移和分布指标 | 实时眼动感知与个性化反馈仪表盘 |
| 2022 | JMIS | Assessing and Enhancing Adversarial Robustness of Predictive Analytics | 预测性能、性能比率、扰动曲线面积 | 预测分析应用的鲁棒性设计框架与ARText实例 |
| 2022 | ISJ | Context-aware user profiles to improve media synchronicity | 沟通任务时间与错误数 | 上下文感知AAC系统与设计原则 |
| 2023 | JAIS | Designing Conversational Dashboards for Effective Use in Crisis Response | 任务正确性、完成效率、最短路径透明交互 | 会话式危机响应仪表盘设计理论 |
| 2023 | ISR | Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model | 密码强度与实际修改行为 | 密码强度计的说服性反馈设计 |
| 2023 | ISR | Augmenting Social Bot Detection with Crowd-Generated Labels | 社交机器人事实标签上的检测性能 | 社交机器人检测系统的众包信号融合流程 |
| 2024 | MISQ | Interleaved Design for E-Learning | 自动评分的学习成绩 | 弱项检测、知识地图和调度引擎 |
| 2024 | ISR | When Variety Seeking Meets Unexpectedness | 点击、完成观看、观看时长及经济结果 | 生产运行的意外推荐系统个性化组件 |
| 2025 | ISR | HyperCARS | RMSE、MAE、Hit@K、MRR@K等 | CARS的层次上下文表示组件 |

## 最终排除的 10 篇模型阳性

| 文献 | 最终排除原因 |
|---|---|
| Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0 | 专家判断回答是否含“恰当证据”，相关性、可信性、可操作性依赖语义判断；F1不能使目标客观化。 |
| Automating in High-Expertise, Low-Label Environments | PICO句子/片段标签由专家创建和核验，属于语义角色判断。 |
| Digital Institutionalization: The Case of E-Prescribing | 错误数只是ADR评价证据；研究问题与核心贡献是数字制度化过程和制度理论。 |
| Automated discovery of business process simulation models from event logs | 核心是自动发现方法、相似度度量和超参数优化；Simod是方法实现。 |
| Augmented Reality at Work | 核心是解释AR经由注意力影响绩效及边界条件；AR/手机是实验处理。 |
| Responsible cognitive digital clones as decision-makers | F1复刻的是个人偏好、偏差和判断；标签不能脱离人的价值与偏好成立。 |
| Providing more regular road signs infrastructure updates for connected driving | 核心是聚类、负观测和置信度融合的领域方法；云平台是运行载体。 |
| A novel decision support system for optimizing aircraft maintenance | 核心是领域约束下的调度优化模型；GUI/DSS只是求解器外壳。 |
| Enhancing User Privacy Through Ephemeral Sharing Design | 客观披露与匹配结果之外，主观隐私担忧下降也是证明“隐私增强”的核心成功终点，属于混合核心结果。 |
| Smart Markets for Real-Time Allocation of Multiproduct Resources | 核心贡献是智能市场与资源分配机制，FleetPower仿真不是软件制品类级设计贡献。 |

## 最终分布

### 按年份

| 年份 | 数量 |
|---:|---:|
| 2020 | 7 |
| 2021 | 1 |
| 2022 | 3 |
| 2023 | 3 |
| 2024 | 2 |
| 2025 | 1 |
| 2026 | 0 |
| 2027 | 0 |

### 按期刊

| 期刊 | 数量 |
|---|---:|
| Information Systems Research | 4 |
| European Journal of Information Systems | 3 |
| Journal of Management Information Systems | 3 |
| Journal of the Association for Information Systems | 3 |
| Decision Support Systems | 2 |
| Information Systems Journal | 1 |
| MIS Quarterly | 1 |

## 结果文件

- `final_adjudication_27.csv`：27篇模型阳性的逐篇最终裁决与原因
- `final_included_17.csv`：最终保留的17篇
- `final_excluded_10.csv`：人工推翻的10篇及排除代码
- `final_summary.json`：范围、数量、年份、期刊与排除原因统计
- `strict_criteria_cn.md`：可复用的最终严格标准

模型 V3 原始输出完整保留在相邻的 `output_full_v3` 目录，未被人工结果覆盖。
