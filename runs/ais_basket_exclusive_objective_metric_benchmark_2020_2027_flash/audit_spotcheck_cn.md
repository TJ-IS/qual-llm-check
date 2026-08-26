# 抽检审计报告：唯一客观指标 + Benchmark 表述筛选（全库 13,909 篇 → 315 篇）

审计人：Codex（基于本地全文人工核读）
审计日期：2026-08-09

## 1. 抽检方法

- 全量判定：13,909 篇，315 篇命中（strict_include=true），0 失败。
- 分层随机抽样 12 篇命中（按年代层：1991–1994、1996–2009、2010–2019、2020–2026），
  另全量核查全部低置信度命中（confidence<0.8，13 篇）与全部 1996 年前命中（3 篇），去重后约 20 篇逐一对照原文核读。
- 近差排除样本：objective_metric 通过但被排除 6 篇、benchmark 通过但被排除 6 篇，逐一核读判定理由与原文。
- 漏检侧检查：标题含 "benchmark" 的被排除文献 17 篇全部核查其判定是否合理。
- 全库量化核查：统计命中文献中 benchmark 表述引文不含 "benchmark" 字样、以及全文完全不出现 "benchmark" 字样的篇数。

## 2. 抽检结果

### 2.1 判定质量总体良好

核读的典型正确命中（真阳性）：
- MIS Quarterly 2023 HACS 多期贷款违约预测：全文明确 "benchmarked methods from two families"，与 Cox/MCM/MTLSA 等比较，C-index/IBS/AUC 客观，无并列主观目标。
- DSS 2022 欺诈网站检测：明确 "benchmark comparisons"，欺诈标签来自外部权威清单，Accuracy/F1/MCC 等客观指标。
- JMIS 2020 O2O 推荐：命名 MovieLens 100K 公开基准数据集，与 CF/MF/DL 等比较。
- DSS 2010 烧伤患者住院时长预测：明确 "using linear regression analysis as our performance benchmark"。
- DSS 2019 车险费率厘定、DSS 2008 Shopbot 节省额、JMIS 2018 POI 推荐、ISR 2025 状态依赖推荐（C1/C2 标为 "Benchmark schemes"）等，均符合两个条件。

近差排除判定同样正确（没有把"无 benchmark 表述"错放进来）：
- 高尔夫四人组 DSS（自建实例求解，无 benchmark 表述）、OLAP 立方（合成数据实验）、S&P500 混合 AI 预测、PLS-SEM 最小样本量（仅 Monte Carlo 对照）均被正确排除。
- "benchmark 通过但客观指标未通过"的排除：ISR 2025 讲师表现预测（学生评分=主观构念）、DSS 2014 情感分类（情感极性=主观构念）、ISR 2021 钓鱼漏斗（自报标签混合）、众包推荐（满意度与准确率并列）——模型对 fixed-labels 例外把握正确。
- 标题含 "benchmark" 的 17 篇被排除文献（newsvendor 行为实验、MISQ 2016 Competitive Benchmarking 方法论文、IT 基准管理综述等）均属合理排除。

### 2.2 发现的明确误判（假阳性）

1. **MISQ 2002《How Do ERP Systems Affect Firm Risk?》**（09896，conf 0.70）：
   这是解释性计量实证研究（TOIP 理论、2,127 firm-year 样本、假设检验 ERP 与风险的关系），核心目标是理论解释而非提升客观指标；
   "benchmark" 是计量上的参照组（"using firms with no ERP systems as a benchmark"），不是对方案的 benchmark 评价。
   应判 core=theory_or_explanation_primary、benchmark=generic/no，两个模块都应失败。误判根因：把"参照组"当成了 benchmark 评价。

2. **DSS 2012 COLPEL 成本敏感正例学习**（03198，conf 0.95）：
   核心标签是 Amazon 图书星级评分（≥4 为积极），是客户对图书质量的评价性判断，并非"脱离人的感受、意义理解和价值判断而成立"的外部事实标签；
   按提示词 fixed-labels 极窄例外应排除（与前序轮次排除"讲师表现预测"逻辑一致）。误判根因：把"用户评分阈值"当成了客观事实标签。

### 2.3 边界风险区（无 "benchmark" 字样的纳入）

全库核查：**315 篇命中中，44 篇（14%）全文完全不出现 "benchmark" 字样**（32 篇的 benchmark 引文也不含该词），全部以"命名公开数据集/标准算例=benchmark"的解释纳入，如 UCI 数据集、MovieLens、IEEE 30/118 节点系统、contact lens 数据等。

- 其中较可靠：MovieLens 100K、UCI 标准分类数据集、IEEE 标准测试系统——这些确实是领域公认基准测试场地，且原文有明确参照点比较（如 DSS 2012 结构变换、DSS 2009 贝叶斯网络、DSS 2013 最优潮流、ISR 2006 隐私扰动）。
- 其中较勉强（建议人工复核）：
  - DSS 1997 Knowledge Discovery by Inspection：仅称 "well-known data sets"，无 benchmark 框架；
  - DSS 2014 银行电话营销：只有 "for comparison purposes"，模型把"对比"解释为"benchmark"（09916）；
  - DSS 2018 自动特征加权：同样只有对比表述（14770）；
  - DSS 1998 GA vs 反向传播比较、DSS 2012 KBGA、2007 参考元数据抽取等同类情况；
  - DSS 2017 SPMM：以 "benchmark" 指前测基线任务（human experiment），语义较弱；
  - DSS 1991 EMS 网络评价：核心是评价/选型研究，与"提升指标"的目标略有出入。

### 2.4 量化小结

- 抽检核读样本（约 20 篇命中）：明确误判 2 篇（10%），边界/勉强 6–8 篇（30–40%），可靠命中约 60%。
- 全库 315 篇：约 86% 的命中全文出现 "benchmark" 字样（271 篇）；约 14%（44 篇）依赖"命名基准"解释，其中估计 5–10 篇属于把"对比/基线"拔高为 benchmark 的勉强纳入。
- 漏检（假阴性）方向：未发现明显漏检；无 benchmark 表述的排除与提示词要求一致。

## 3. 主要错误模式（按出现频率）

1. **把"对比/参照组"等价为 benchmark 表述**（最常见）：计量实证的对照组合（ERP 风险）、"for comparison purposes"式表述（银行电话营销、特征加权）。
2. **fixed-labels 例外放宽**：把用户评分/偏好类标签当成客观事实标签（COLPEL 图书评分）。
3. **命名数据集解释过宽**：把任何"知名数据集"都当作 benchmark 表述（INSPECT、UCI 非标准任务）。
4. 少数情况下核心目标判定偏松（EMS 1991 评价型研究）。

## 4. 建议（可选下一步）

1. **保守版复核（推荐）**：对 315 篇做一轮独立红队复核（沿用既往 `final_red_team_addendum` 思路），重点反查三类：无 "benchmark" 字样的 44 篇、低置信度（<0.8）命中、以及计量实证类文献；预期可筛掉 10–20%。
2. **收紧提示词**：若你要求的是"字面上必须有 benchmark 表述"，可在 benchmark 门槛中增加硬条件：全文必须出现 benchmark/benchmarking 字样（命名式例外仅限公认 benchmark 套件如 ImageNet/GLUE/SWE-bench/MovieLens/UCI 基准，且原文明确以基准框架表述），并增加"参照组≠benchmark""对比≠benchmark"的反例校准。
3. **直接使用**：若接受"标准测试场地+明确参照点比较"作为 benchmark 的等价形式，则当前 315 篇可直接使用，仅需人工复核 final_report_cn.md 中标注的 44 篇。
