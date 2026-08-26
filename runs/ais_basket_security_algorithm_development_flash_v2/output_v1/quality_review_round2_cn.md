# v2 最终筛选结果与质量审查（round 2）

- 完成时间：2026-08-23（全量 13,909 篇，0 失败，37 分钟）
- 模型：deepseek-v4-flash，temperature=0，不设 max_tokens，并发 100
- 提示词指纹：1875f70152311e2841ae33eb1d7374f7ba255ef0edabbb9309c03b2d6fd63b29（v2 收紧版）
- 通过：99 篇（0.71%）；security_pass=265（1.9%）；algorithm_pass=1950（14.0%）
- 期刊分布：DSS 49、ISR 17、JMIS 13、MISQ 10、I&M 4、JAIS 4、EJIS 1、JSIS 1
- 数据公开性：public 46、private 35、mixed 11、unclear 7

## 一、通过清单构成（按主题粗分）

- 钓鱼检测/防钓鱼（约 10 篇）：PhishWHO、target domain identification、Chinese phishing e-Business、anti-phishing genre、dynamic evolving NN、statistical learning theory、phishing severity、Phishing Funnel（ISR）等。
- 隐私保护/匿名化/披露风险（约 16 篇）：扰动、重建、匿名化、交换、掩码、微数据共享、关联规则隐藏、医疗文本匿名化、隐写（1 篇）等。
- 虚假信息/虚假评论/社交机器人/网络欺凌（约 15 篇）：fake review 系列、review manipulation、social bot、false news、MegaFake、cyberbullying 等。
- 网络威胁情报/暗网/黑客社区（约 8 篇）：ADREL、exploit linking、emerging threats、hacker exploit labels、dark net markets、carding、Bitcoin 去匿名化等。
- 恶意软件/蠕虫/病毒传播/勒索软件（约 7 篇）：email worms、ransomware FSM、SIS/E-SEIR、软件多样性、immunization targets、Android 权限图异常。
- 入侵检测/异常检测（约 3 篇）：因子分析、攻击图影响评估、分布式 DSS 对抗操纵。
- 安全投资/风险/对策优化（约 12 篇）：Stackelberg、安全控制分配、cyber-risk insurance、countermeasure portfolio、系统动力学、SMECRA、网络外部性、IT investment、Dempster-Shafer 风险评估等。
- 对抗鲁棒性/防御 AI（2 篇）：RADAR（MISQ 2025）、Adversarial Robustness Design Framework（JMIS 2022）。
- 认证/访问控制/密钥（约 5 篇）：ThumbStroke、最大熵知识认证、SemForce 联邦、用户关系层次安全、RFID 分离（边缘）。
- 其他（约 4 篇）：热名单监控、可信度评估、鼠标轨迹隐藏信息检测、身份匹配（执法语境，边缘）。

## 二、明确残留误判（建议排除，2 篇）

1. An investigation of Zipf's Law for fraud detection（2008, DSS）：会计/审计欺诈检测，属「会计与审计欺诈」排除项；模型被 KDDCUP'99 数据集与防火墙日志案例误导，但论文动机是审计欺诈（assist auditors），非信息系统攻防。
2. A social referral appraising mechanism for the e-marketplace（2017, I&M）：核心是社交网络信誉计算改进，评级操纵只是动机背景，属「一般信任与信誉计算」排除项。

## 三、边缘案例（建议人工复核，约 10 篇）

- A decision methodology for managing operational efficiency and information disclosure risk in healthcare processes（2014, DSS）：核心是效率优化，披露风险只是约束。
- A novel means to address RFID tag/item separation in supply chains（2018, DSS）：方案+仿真（知识系统+认证协议），算法强度接近已被排除的 ACL 方案类。
- Complex Problem Solving: Identity Matching Based on Social Contextual Information（2007, JAIS）：执法语境身份匹配，与 v1 已排除的 HNB 身份匹配（DSS 2011）不一致。
- Regulating Cryptocurrencies: De-Anonymizing the Bitcoin Blockchain（2019, JMIS）：监督学习方法应用（Gradient Boosting 等现有算法），新颖性偏弱。
- Are social bots a real threat?（2019, EJIS）：agent-based 仿真研究，算法/模型开发与行为研究的边界。
- A system dynamics model for information security management（2015, I&M）与 SMECRA（2021, DSS）：系统动力学仿真模型，属模型开发但无真实数据。
- When Being Hot Is Not Cool: Monitoring Hot Lists for Information Security（2016, ISR）：电商操纵监控语境。
- Stylometric Identification in Electronic Markets（2008, JMIS）：市场身份伪装检测，执法/市场语境。
- The Most Popular News Recommender: Count Amplification and Manipulation Resistance（2014, ISR）：新闻推荐操纵抵抗，内容操纵语境边缘。
- Filtering trust opinions through reinforcement learning（2014, DSS）：信任意见过滤，信誉计算与操纵防御边界。

## 四、v2 相比 v1 的改进（对照）

- v1 明确误判 4 篇（市场监视、预测警务、ORQM、Zipf）中 3 篇已被排除，Zipf 残留（见二.1）。
- v1 边界 15 篇中 13 篇已被排除：HNB 身份匹配、犯罪网络关键人物、H-BAS、SIGHT、刚性检测、边境车辆、ACL、NIMPRO、多指标欺骗检测、ASCSS 等，理由均准确落在 v2 排除类型。
- 算法开发门槛收紧生效：ACL（方案+原型）、NIMPRO（系统集成）、多指标欺骗检测（现成分类器组合）均因算法门槛被排除。

## 五、结论与建议

- 99 篇中约 85-90 篇为扎实的安全+算法开发研究，约 10 篇边缘、2 篇明确误判。
- 建议 1：对 99 篇做一轮人工复核（重点：二、三节清单），排除 2 篇明确误判并裁定边缘篇目。
- 建议 2：数据公开性方面，public 46 篇可直接用于后续「必须公开数据」的选题；其余 53 篇含私有/混合/不明数据，需在选题时排除或说明。
- 建议 3：若后续重跑，可在 1.3 中再显式点名「审计欺诈（即使使用网络数据集）」「信誉计算（即使以操纵为背景）」两条，进一步压缩残留。
