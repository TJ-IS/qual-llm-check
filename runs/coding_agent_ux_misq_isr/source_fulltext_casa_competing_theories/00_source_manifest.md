# CASA 竞争理论原文资料清单

> 本文件记录第 81 号竞争性理论审计使用的原文资料、获取状态和证据角色。Otero 下载文件保留 MinerU Markdown 原文；无法下载的资料只记录出版社或作者公开页面，不以二手转述冒充全文。

## 已由 Otero 保存的全文

| 文件 | 文献 | 主要证据角色 |
| --- | --- | --- |
| `01_mental_models_expectation_violations_2021.md` | Grimes, Schuetzler, & Giboney (2021), *Decision Support Systems* | 心智模型是支持预测的既有认知框架；与任务时点的动态态势感知不同 |
| `03_user_calibration_1996.md` | Kasper (1996), *Information Systems Research* | 校准是主观决策信心与客观决策质量的对应关系，不是态势内容维度 |
| `09_information_acquisition_mental_models_1996.md` | Todd & Benbasat (1996), *Information Systems Research* | 信息获取、问题表征与心智模型形成的关系 |
| `10_feedback_mechanisms_dss_2009.md` | Kayande et al. (2009), *Information Systems Research* | 反馈如何促进用户心智模型与决策模型对齐；属于认识形成前因 |

## 已在既有资料夹保存的全文

| 路径 | 文献 | 主要证据角色 |
| --- | --- | --- |
| `../source_fulltext_subjective_casa_matrix_axis/01_baird_maruping_2021_is_delegation.md` | Baird & Maruping (2021), *MIS Quarterly* | 能动型信息系统、任务执行与结果、权责转移、监控与更新 |
| `../source_fulltext_subjective_casa_matrix_axis/02_fuegener_et_al_2022_productive_delegation.md` | Fügener et al. (2022), *Information Systems Research* | 人工智能委托、元知识和两个委托方向的认知差异 |
| `../source_fulltext_subjective_casa_matrix_axis/05_afiouni_pinsonneault_2026_human_in_control.md` | Afiouni & Pinsonneault (2026), *Journal of the Association for Information Systems* | 个人控制是人工智能委托中的主观体验和适应结果，不是 CASA 内容 |

## 出版社或作者公开页面

| 文献 | 可核对页面 | 已核对的原文内容 | 下载状态 |
| --- | --- | --- | --- |
| Sarter & Woods (1995) | https://doi.org/10.1518/001872095779049516 | mode awareness 是监督者追踪并预期自动化系统行为的能力；自主行动和间接模式变化增加系统状态监控要求 | 出版社全文未保存；作者公开页面可在线核对 |
| Wickens (2002) | https://doi.org/10.1111/1467-8721.00184 | 航空态势感知包含 spatial、system 和 task awareness；system awareness 用于了解自动化行动 | 出版社摘要可核对，全文未保存 |
| Lee & See (2004) | https://doi.org/10.1518/hfes.46.1.50_30392 | 自动化信息可按 purpose、process 和 performance 的归因抽象程度分类 | 作者公开版本链接失效，出版社元数据可核对 |
| Chen et al. (2018) | https://doi.org/10.1080/1463922X.2017.1315750 | SAT 1 为目标、状态、意图、计划和行动；SAT 2 为理由、约束与可供性；SAT 3 为未来状态、后果、成功可能性与不确定性 | 出版社全文网页可在线阅读，PDF 下载被拒绝 |
| Jussupow et al. (2021) | https://doi.org/10.1287/isre.2020.0980 | 人工智能辅助诊断中的元认知分为 self-monitoring 和 system monitoring | Top11 摘要与出版社元数据可核对，Otero Markdown 不可用 |
| Ning et al. (2024) | https://doi.org/10.1016/j.dss.2024.114273 | 分别操纵 performance、process 和 purpose transparency，检验信任与建议使用 | 出版社全文网页可在线阅读，Otero Markdown 不可用 |
| Saffarizadeh et al. (2026) | https://doi.org/10.1111/isj.70017 | process variation 是完成路径变化，outcome variation 是成功程度变化 | Wiley 全文网页可在线阅读，Otero Markdown 不可用 |
| Kumar et al. (2025) | https://doi.org/10.1109/ASE63991.2025.00043 | 开发者与智能体解决真实软件问题时的持续互动、调试与测试 | 正式会议元数据可核对，全文未保存 |
| Dhanorkar et al. (2026) | https://doi.org/10.1145/3805689.3812402 | 事前控制、共同规划、实时查看、事后复核，以及代码审查困难与测试结果替代线索 | 正式会议元数据和作者公开版本可核对，未复制公开预印本 |

## 对第二轴证据强度的解释

没有一篇原文直接提出适用于编程智能体的智能体运行态势与软件任务态势二元轴。第 81 号稿的推导由三层证据组成。

1. 模式觉察和系统觉察研究直接证明，自主自动化系统自身可以成为区别于外部任务局面的态势认识对象。
2. SAT 模型直接界定了用户对智能体对象需要认识的目标、行动、理由、预期和不确定性内容。
3. 编程智能体研究表明，用户还需认识被智能体持续改变的代码、测试和软件任务结果。

因此，态势认识对象轴是有原始理论支撑的情境化推导，不是既有理论已经命名并验证的维度。它必须由 Reddit 编码、内容效度和测量模型继续检验。
