# 方法来源快照与引用谱系台账

更新时间：2026-08-24

本目录只保存已经取得、可以按字节复核的方法原文。`archived_primary_original` 表示原始方法文献已归档并完成责任相关原文窗口复核；`local_top_is_adjacent_application` 表示权威 IS 论文可用于证明该方法在相邻研究中的实际使用，但不能代替原始方法依据；`lineage_candidate_not_terminal` 表示已发现前向或后向引用边，但尚未取得并复核原文，不能用于关闭稿件债务。

## Holm 1979：序贯拒绝式多重检验

- 状态：`archived_primary_original`
- 文件：`holm_1979_sequentially_rejective_multiple_test.pdf`
- SHA-256：`4317A0D1555DAD949DC1760605D925BA20037402827741FDF99CD8EA37E80C46`
- 书目信息：Sture Holm. 1979. “A Simple Sequentially Rejective Multiple Test Procedure.” *Scandinavian Journal of Statistics* 6(2): 65–70.
- 稳定条目：`https://www.jstor.org/stable/4615733`
- 本地快照取得地址：`https://www.ime.usp.br/~abe/lista/pdf4R8xPVzCnX.pdf`
- 已直接复核窗口：全文，包括摘要、第 1 节问题与多重显著性水平定义、第 2 节算法与定理 1、第 3 节应用和扩展、结论性建议及参考文献。PDF 第 1 页为馆藏封面，论文正文为 PDF 第 2–7 页。
- 可以承担的命题：对预先给定的一族假设，将取得的显著性水平从小到大排列，依次与 `alpha/n, alpha/(n-1), ..., alpha` 比较并在首次不能拒绝处停止，可以在任意真原假设组合下控制拒绝至少一个真原假设的概率；该程序在相同单项检验基础上不比经典 Bonferroni 更弱。
- 不能承担的命题：Holm 1979 不替研究者定义 estimand、原假设、对比方向、族边界、主要与次要分析边界，也不证明论文一的路径计数模型或联合可见性设计正确。
- 论文一当前责任：第 5.3 节四项主要方法差对比族和第 5.6 节两项联合可见性对比族。方法依据可以关闭，但必须保留“族在看见封存结果以前预注册、只在族内校正、从最小 p 值开始逐步检验、首次不能拒绝即停止”的作者协议。

## Léger et al. 2014：顶级 IS 相邻应用

- 状态：`local_top_is_adjacent_application`
- 文件：`database_fulltext_all/03596_2014_precision-is-in-the-eye-of-the-beholder-application-of-eye-fixation-related-potentials-to-inform.md`
- SHA-256：`D7A9D7011BF398A61D27AFA119BE636958DA6D94AD0490A8F839AE257B616CD4`
- 已直接复核窗口：方法猜想与实验设计、第 3.2.6 节数据处理、第 4 节及其假设检验和方法验证子节、第 5 节及相邻含义和指导部分、参考文献。
- 引用边：该文在第 4 节开头直接引用 Holm 1979，并说明对多个统计检验使用 Holm–Bonferroni 以应对第一类错误；后续密集时间窗检验再次使用该校正。
- 用法边界：只能证明权威 IS 研究会在预先组织的一组多重检验中显式说明 Holm 校正及其错误控制责任，不能直接验证论文一的结果单位、对比族或模型。

## Kim and Benbasat 2006：顶级 IS 相邻应用

- 状态：`local_top_is_adjacent_application_secondary_route`
- 文件：`database_fulltext_all/05656_2006_the-effects-of-trust-assuring-arguments-on-consumer-trust-in-internet-stores-application-of-toul.md`
- SHA-256：`0E3C0E83748CE68F982A003BA6D37842D0F32241CF5DD08F5DB9786C5D651600`
- 已直接复核窗口：引言、理论与假设、研究方法、第 5.3 节及前后相邻结果子节、讨论、限制和参考文献。
- 引用边：第 5.3 节把五项非正交对比与五个预设假设对应，并使用 Holm 序贯拒绝式 Bonferroni；该文的方法说明直接引 Kirk 1995，而不是直接承担 Holm 原始定理。
- 用法边界：可作为“权威 IS 论文将一个明确对比族绑定到预设假设并报告校正”的相邻写作样本；原始方法责任仍由 Holm 1979 承担。

## Field and Welsh 2007：cluster bootstrap

- 状态：`archived_primary_original_bounded_support`
- 文件：`field_welsh_2007_bootstrapping_clustered_data.pdf`
- SHA-256：`25FE4A7BE9EB85F9A860BEE2CBB05E6509D24DDE30B806D69E1A50B1F679650B`
- 书目信息：C. A. Field and A. H. Welsh. 2007. “Bootstrapping Clustered Data.” *Journal of the Royal Statistical Society: Series B* 69(3): 369–390.
- 本地快照取得地址：`https://bemlar.ism.ac.jp/zhuang/Refs/Refs/field2007jrssb.pdf`
- 已直接复核窗口：摘要和第 1 节；第 3 节全部方法比较，重点为第 3.3 节并同时复核相邻第 3.2、3.4 节；第 4 节小样本模拟；第 5 节结论；相关参考文献。另对 PDF 第 1、2、9、15–20 页进行了版面核验。
- 可以承担的命题：简单 cluster bootstrap 以有放回方式抽取完整组向量；在其平衡单层数组与组向量可视为独立同分布的设定下，整组重抽样保留组内依赖；当组数趋于无穷且每组大小固定时，文中所研究的均值与方差分量方差估计具有相应一致性结果。
- 必须保留的限制：论文研究的是平衡单层数组和特定统计量；模拟中组数为 5 和 15 时 cluster bootstrap 系统性低估方差；作者明确指出该方法不容易推广到更复杂的随机和混合模型。
- 不能承担的命题：该文不直接证明论文一“仓库、任务、智能体、方法、共享重复块”多层结构下的完整重抽样算法，不给出最小仓库组数阈值，也不验证论文一的有限样本区间、计数模型或具体 estimand。
- 论文一当前责任：最多支持“若仓库来源组被论证为相互独立且可交换，则敏感性分析应以仓库来源组为抽样单位并保留组内观测”的高层原则。具体嵌套保留规则、最小组数、区间构造和失效判据仍是作者协议或开放方法债务。

## 前向发展候选

- Cheng, Yu, and Huang 2013 与 Field and Welsh 2007 的前向引用关系已在发现阶段记录；当前没有完成本地原文字节归档，也没有完成核心大节及相邻大节复核。
- 状态：`lineage_candidate_not_terminal`
- 使用规则：只能作为下一轮检索路线，不得写成已经验证的现代方法背书，不得用于关闭论文一的 cluster bootstrap 债务。

## 更新和向子代理投影规则

1. 每次新增来源都记录文件路径、SHA-256、取得地址、实际直接复核窗口、能承担与不能承担的命题，以及与旧文献的引用边。
2. 任何来源字节变化都会使基于旧哈希的判断失效；新判断必须追加，不得覆盖历史判断。
3. 给子代理的任务包必须同时包含本台账和通用台账 163、164、165、171、172、175；论文一任务另包含专账 168。子代理仍须直接阅读原文，不得把本台账当作原文替代品。
4. 相邻 IS 应用只能承担适用性和写作组织背书；原始方法文献承担方法性质，作者协议承担论文一的具体估计量、族定义、样本阈值和实施规则。
5. 本台账的 `semantic_alignment`、`citation_support`、`pilot_implementation` 和 `release` 门禁均保持 `false`；来源路径闭环不等于整篇论文通过。
