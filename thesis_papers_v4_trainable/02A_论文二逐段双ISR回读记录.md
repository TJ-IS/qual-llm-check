# 已终止方案　论文二逐段双 ISR 回读记录

> 状态说明　本记录只对应已在标签与近邻闸门终止的 TEGRA 草稿，不属于新版三篇论文的逐段审计。当前论文二将在研究对象重新冻结后另建正文与审计文件。

本记录与论文二同步生成。每个 P 编号只对应正文当前版本的一个实质段落。ACAA 指 Xiao et al. 2024 的 *Attending to Customer Attention*，本地原文为 `database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md`。DSDL 指 Xiao et al. 2023 的 *A Theory-Driven Deep Learning Method for Voice Chat–Based Customer Response Prediction*，本地原文为 `database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md`。行号均指这两个 MinerU Markdown 文件在本轮写作时的物理行号。

## P01　摘要

**双源定位。** ACAA 第 29 行是完整摘要，另回读第 53 至 55 行的方法总括。DSDL 第 27 行是完整摘要，另回读第 51 至 53 行的问题、训练困难与方法总括。

**ACAA 逐句或句群功能。** 第 29 行先承认已有测量，再指出量化指标不能承担动态预测。随后用一个理论判断把注意力确立为中间对象，再把它拆到四个粒度并导出四项指标。末两句依次给出专门神经机制和预测与表征两类证据。第 53 至 55 行进一步把指标、研究问题、两个构件、数据和结果串成闭环。

**DSDL 逐句或句群功能。** 第 27 行先建立业务行动及数据机会，再把满意这一理论对象与多视图深度学习能力相连。方法句不用泛称神经网络，而是列出偏好、动态体验和理论增强预测三项可学习责任。末三句分别承担性能、联合表征和解释性证据。第 51 至 53 行还明确无直接标签这一优化困难，并说明三个构件如何联合学习。

**新段逐句功能。** 第一句建立有限预算探索的行动问题并指出现有终局监督缺少中间解释。第二句确立任务知识与仓库证据匹配这一中间机制并命名 TEGRA。第三句把两个可观察需求类型、已读证据和 frontier 动作串成输入到决策的计算链。第四句列出四项互补训练目标，并把终局偏好降为辅助信号。第五句交代训练来源、三类外测和固定预算结果责任。第六句收束不虚构结果、可干预性和识别失败退回规则。

**引用责任。** SWE-Gym 与 SWE-smith 只负责可执行任务及可重新生成轨迹的事实。ContextBench 与 SWE-Explore 分别负责人工或轨迹定义的证据过程评价。SWE-rebench 负责时间隔离、持续采集和可执行外测。Shaft and Vessey 只在正文理论节负责软件知识与修改任务匹配，不在摘要中承担算法已有效的结论。摘要中的 TEGRA 架构、损失和退回规则都是本文待检验设计，不归给外部文献。

**回读后的修改处理。** 初稿曾把 TEGRA 写成优于训练型探索代理的方案，并以一次正确下一步作为主标签。回读 ACAA 的中间指标链与 DSDL 的无直接标签处理后，删除未实证的比较级，把下一步改为多正例排序、缺口闭合、桥接距离和终局效用四个互不替代的监督责任。摘要同时加入类型识别失败后的未类型退回，使理论命名依赖可干预证据而不是网络可视化。
