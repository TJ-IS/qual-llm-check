# 第一轮通过清单质量审查（人工抽查）

- 审查时刻：已判定 2554 篇；通过 39 篇（1.53%）
- 门槛收敛：algorithm_pass=447 → security_pass=108 → strict_include=39
- 审查方式：对全部通过文章逐条读判定；对可疑文章打开本地全文核对摘要、引言与关键章节。

## 一、明确误判（建议排除，4 篇）

1. Design Theory for Market Surveillance Systems（2015, JMIS）：金融市场的市场操纵/内幕交易监视，属于「市场操纵、内幕交易」排除项；且论文是设计理论（design theory），不是算法开发。双重不符。
2. An investigation of Zipf's Law for fraud detection（2008, DSS）：会计/审计欺诈检测（occupational fraud），损害是经济损失，属「纯金融欺诈」排除项；它只是用了 KDDCUP'99 入侵检测数据集做实验，目标仍是审计欺诈。
3. A Decision Support System for predictive police patrolling（2015, DSS）：传统犯罪预测与警力分区优化，无恶意行为者攻击/操纵信息系统的成分，「公共安全」被泛化为「安全」。
4. Capturing the essence of word-of-mouth for social commerce（2013, DSS）：核心是评论质量分类（有用/无用），review spam 只是「无用评论」的一个子类，并非研究问题中心；无对抗行为者中心性。

## 二、边界案例（建议人工复核，约 9 篇）

- The Impact of Fake Reviews on Online Visibility（2016, ISR）：有攻击注入仿真与抗操纵排序，可辩护；但威胁对象是商家可见性（商业利益）而非系统/用户安全，偏边缘。
- A social referral appraising mechanism for the e-marketplace（2017, I&M）：信任欺诈/评级操纵是动机背景，核心是社交信誉计算，对抗行为者中心性弱。
- Sharing and access right delegation for confidential documents（2006, I&M）：安全相关性明确（机密保护），但「算法开发」弱——为方案+原型性能测试，无形式化对比评估。
- An outlier-based data association method for linking criminal incidents（2006, DSS）：执法辅助（犯罪事件关联），公共安全语境，边缘。
- A hierarchical Naïve Bayes model for approximate identity matching（2011, DSS）：执法/反恐身份匹配，威胁检测语境，边缘。
- Integrating relations and criminal background to identifying key individuals in crime networks（2020, DSS）：犯罪网络关键人物识别，执法辅助，边缘。
- Enhancing border security: Mutual information analysis to identify suspect vehicles（2007, DSS）：走私车辆检测，威胁检测可辩护，但属执法场景。
- A decision methodology for managing operational efficiency and information disclosure risk in healthcare processes（2014, DSS）：信息披露风险决策，隐私语境，边缘。
- Design Principles for Signal Detection in Modern Job Application Systems（2020, JMIS）：招聘造假检测，欺骗检测语境，边缘。

## 三、判定扎实（约 18 篇）

暗网威胁识别（JMIS 2020）、PhishWHO 钓鱼检测（DSS 2016）、隐私匿名化（JAIS 2020）、因子分析入侵检测（DSS 2006）、安全对策多目标优化（DSS 2012）、ADREL 暗网分析（MISQ 2022）、邮件蠕虫影响（DSS 2007）、软件多样性分配（ISR 2017）、虚假新闻检测（MISQ 2022）、串通欺诈交易检测（DSS 2016）、评论操纵检测（JMIS 2018）、恶意软件传播（JMIS 2016）、数据净化（DSS 2007）、隐私重编码（ISR 2007）、IT 安全投资分配（DSS 2007）、入侵防御（JMIS 2007）、网络中断缓解（DSS 2008）、网络欺凌句模提取（JAIS 2019）。

## 四、误判原因与改进建议

- 原因：安全定义中的「内容操纵/威胁检测」边界被 LLM 泛化；关键词（intrusion、fraud、surveillance、crime）易误导；「算法开发」门槛本身筛选正常。
- 建议 1：全量完成后，对通过文章做第二轮严格复核（新 prompt：逐条核对排除项，输出 A 纳入/B 边缘/C 排除 三级）。
- 建议 2：提示词增加显式排除：市场操纵/内幕交易监视；会计/审计欺诈（无网络攻击成分）；传统犯罪预测与警务优化；一般评论质量/有用性分析（无恶意行为者中心性）。
- 建议 3：数据公开性字段对后续挑选公开数据研究有用，但当前通过列表约一半为 private/unclear，选题时需注意。
