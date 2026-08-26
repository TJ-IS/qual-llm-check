# 99 篇通过文章数据公开性（v3 口径）分析

- 口径 v3：可申请/许可获取（学术许可、研究申请、注册下载）= public；无法通过任何公开渠道或申请程序获取（企业专有、内部日志、执法保密、拒绝研究者访问）= private；纯合成/仿真 = synthetic；混合 = mixed；无法判断 = unclear。
- 重判方式：基于全文对 99 篇逐篇重新判定（deepseek-v4-flash，temperature=0，99/99 成功）。
- 结果：public 49、synthetic 24、mixed 13、private 12、unclear 1。

## 一、最终 private 12 篇（按类型）

### 企业/组织内部专有数据（6 篇）
1. INSIDER THREATS IN A FINANCIAL INSTITUTION（2015, MISQ）：某美国金融机构 7 个月 ESSO 单点登录日志+内部应用特征。
2. Cyber-risk decision models: To insure IT or not?（2013, DSS）：印度某商学院 2 年周边安全元素日志。
3. Decision support for the optimal allocation of security controls（2018, DSS）：49 名安全专业人员问卷（漏洞概率估计）。
4. Constructing a reliable Web graph（2012, DSS）：某中国搜索引擎公司内部 Web 访问日志（28 亿点击）+内部爬虫图。
5. The Phishing Funnel Model（2021, ISR）：两家企业内部 12 个月现场实验（1,278 员工、49,373 交互）日志与问卷。
6. An IS Security Risk Assessment Model Under DS Theory（2006, JMIS）：审计公司 WebTrust 工作底稿，原文明确因保密限制不提供数据。

### 商业专有数据（2 篇）
7. Personalized Privacy Preservation in Consumer Mobile Trajectories（2024, ISR）：数据聚合商专有移动位置数据（覆盖美国约 1/4 人口）。
8. Regulating Cryptocurrencies: De-Anonymizing the Bitcoin Blockchain（2019, JMIS）：Chainalysis 专有聚类+标注的比特币数据（区块链原始数据公开，但核心标注专有）。

### 执法/机构内部数据（1 篇）
9. Complex Problem Solving: Identity Matching（2007, JAIS）：Tucson 警方 Meth World 毒品犯罪数据库。

### 实验室/参与者采集（3 篇）
10. Harmonized authentication based on ThumbStroke dynamics（2016, DSS）：12 名参与者受控实验。
11. Sleight of Hand（2019, JAIS）：75 名参与者鼠标轨迹/皮电实验。
12. A social referral appraising mechanism（2017, I&M）：187 名参与者授权提供的 Facebook/Yahoo 个人数据。

## 二、v2 -> v3 关键变化

- private -> public（8 篇）：RADAR（VirusTotal 学术许可）、Reidentification Risk in Panel Data（IRI 学术许可）、AZSecure carding（论坛公开可爬）、Cybersecurity risk planning（Verizon 公开行业调查）、Digression and Value Concatenation（公开数据集）、Exploring Emerging Hacker Assets（论坛公开可爬）、Linking Exploits（公开漏洞库）、Assessing severity of phishing（公开数据库）。
- private -> synthetic（14 篇）：纯仿真/合成数据从 private 中拆出（软件多样性、隐私重编码、病毒传播、Bayesian Stackelberg、MOST 等）。
- private -> mixed（2 篇）：IT incident impact（合成+企业案例）、熵披露风险（合成+公开数据）。
- mixed -> public（3 篇）、mixed -> private（1 篇：Bitcoin/Chainalysis）、unclear -> public/synthetic 若干。

## 三、对「必须公开数据」要求的含义

- 99 篇中可直接满足公开数据要求：public 49 篇（另 mixed 中部分含公开数据成分可考虑）。
- 需排除的 private：12 篇（真实数据不可获取：企业日志、商业专有、执法、实验室采集）。
- synthetic 24 篇：无真实数据，不满足「公开数据集」要求（但可用于纯算法/仿真研究）。
- RADAR 在新口径下为 public（VirusTotal 学术许可可申请），与用户的判断一致；其良性文件为自采但可自行复现。
