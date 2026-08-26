# Developing a Measurement Framework for Context Processing Efficiency of AI Coding Agents: Evidence from Large-Scale Trajectory Data

# 开发编码智能体上下文处理效率的测量框架：来自大规模轨迹数据的证据

- 稿件性质：对标 ISR（Information Systems Research）写作逻辑的**研究一初稿**；段落结构逐段对照 #27 EAC（Shangguan et al. 2022, ISR）。
- 证据声明：本文是研究设计初稿，不是已完成的实证论文。凡标【占位】处均为拟实施分析，不填造任何显著性、比例或置信区间；所有 arXiv 预印本引用在投稿前须重新核验版本。写作逻辑与引用作用审计见附录 A。

---

## Abstract

There is increasing interest in information systems research to measure how AI coding agents process repository context, and to study how such information processing shapes task outcomes. Existing evaluations, however, rely on outcome-level metrics (e.g., resolve rate, cost) or single-dimension process metrics (e.g., token count, steps), which do not represent the quality of information processing itself. This paper employs a design science approach and proposes a measurement framework, the Context Processing Efficiency (CPE) framework, as a theory-grounded proxy for the information-processing behavior of coding agents. The framework comprises three instruments—sufficiency (SI), redundancy (RI), and economy (EI)—each anchored in information quality and information overload theory, and a diagnostic protocol that classifies task-level failure modes. We apply the framework in the context of repository-level bug fixing, where trajectories of coding agents are represented as event logs and task-relevant information is derived from publicly available gold patches. To evaluate the value of the framework, we conduct an in-depth evaluation by (1) assessing measurement quality, including stability across scaffolds and models and agreement with human annotation; (2) testing incremental predictive power over existing metrics using multiple prediction methods; (3) testing theory-derived relationships, including an inverted-U effect of redundancy on task success; and (4) evaluating the offline decision value of the measurements through a counterfactual budget-allocation analysis. [占位：结果段落待实验完成后填写。]

## 摘要

信息系统研究日益关注如何测量编码智能体（coding agent）对仓库上下文的处理行为，以及这种信息处理如何影响任务结果。然而，现有评价依赖结果层面的指标（如修复成功率、成本）或单一维度的过程指标（如 token 数、步数），并不表征信息处理本身的质量。本文采用设计科学方法，提出一个测量框架——上下文处理效率（Context Processing Efficiency, CPE）框架，作为编码智能体信息处理行为的理论锚定代理。该框架由三个独立工具构成——充分性（SI）、冗余性（RI）与经济性（EI）——分别锚定信息质量理论与信息过载理论，并配套一个将任务级失败模式分类的诊断协议。我们将该框架应用于仓库级缺陷修复情境：把智能体轨迹表示为事件日志，并以公开 gold patch 推导任务相关信息。为评估框架的价值，我们开展深入评估：（1）测量质量，包括跨 scaffold 与跨模型的稳定性及与人工标注的一致性；（2）在多种预测方法下检验相对既有指标的增量预测力；（3）检验理论推导的关系，包括冗余性对任务成功的倒 U 型效应；（4）通过反事实预算分配分析评估测量的离线决策价值。【占位：结果待实验完成后填写。】

**关键词**：编码智能体；测量框架；信息过载；信息质量；设计科学；轨迹数据

---

## 1. Introduction

### P1

编码智能体在软件平台上搜索、阅读、编辑与验证，构成围绕软件任务的持续信息处理过程。在最简单的形态下，agent 先读取 issue、检索文件、浏览符号定义，再执行修改与测试；这些活动被记录为可审计、可回放的轨迹。近年来，研究者已利用这些轨迹数据来构建上下文表示，并以此评估任务级结果，例如仓库级缺陷修复的成功率（Jimenez et al. 2024）、仓库上下文的检索质量（Qin and Xie 2026; Zhang and Wang 2026）以及轨迹层面的成本与步数（Bouzenia and Pradel 2025）。然而，在工程实践中，不同系统对"效率"的声明使用互不相同的口径：有的报告 token 消耗，有的报告步数，有的报告美元成本；在相同基准上，不同 scaffold 的成本差异可达一个数量级（SWE-Effi; icat-agent）。进一步，信息处理本身还存在多个可分离的方面——哪些相关信息被读取、哪些无关信息被读取、每单位成功消耗多少处理成本——它们共同塑造任务结果。现有度量如修复成功率与 token 数只基于结果或体量，并不表征信息处理的质量。本研究采用设计科学视角，开发一个测量框架作为编码智能体上下文处理效率的代理，并在大规模轨迹数据中评估其价值。

### P2

有充分理由从多维度刻画编码智能体的信息处理。Simon（1955, 1991）的有限理性理论指出，决策者的信息处理能力是有限的，决策质量取决于信息获取与处理成本之间的权衡；信息过载文献进一步表明，当处理需求超过处理能力时，决策表现会下降（Eppler and Mengis 2004; Karr-Wisniewski and Lu 2010）。在编码智能体情境下，仓库上下文既是任务相关的决策资源，也可能因过量与无关而损害表现（Liu et al. 2024）。因此，一个多维度、理论锚定的测量框架能够更好地表征这一复杂信息环境，并可用于任务结果的预测与失败机制的诊断。为此，我们基于信息质量理论的多维结构（Wang and Strong 1996; DeLone and McLean 2003）与 IS 中计算式度量的先例（Shangguan et al. 2022），开发 CPE 框架。遵循设计科学原则（Hevner et al. 2004; Gregor and Hevner 2013），我们通过在真实缺陷修复任务中应用该框架预测任务结果、并与既有度量比较其增量价值来评估其有效性。

### P3

CPE 框架相较常用的结果与体量度量提供了若干优势。第一，结果度量（如 resolve rate）只反映"发生了什么"，不反映"为什么发生"；CPE 将信息处理分解为理论上可区分、经验上可分离的维度，使失败机制可归因。第二，单一维度的过程度量（如 token 数、步数、ACRR）假设某一维度占主导，无法刻画充分性、冗余性与经济性之间的权衡结构；CPE 同时测量三个维度，保留维度间的替代关系。第三，既有度量多为临时定义的比率，缺乏理论锚定；CPE 的每个维度都对应信息质量文献中可辨识的构念（相关性、简洁性与成本维度）。第四，CPE 提供诊断协议，将任务分类为充分性失败、冗余性失败与经济性失败等失败画像，而既有度量无法区分这些画像。与 EAC 相对传统网络中心性度量一样（Shangguan et al. 2022），CPE 的贡献不在于替换结果度量，而在于测量既有度量遗漏的信息处理构念。

### P4

同样重要的是考察 CPE 框架能否比既有度量更好地预测任务结果。研究度量的预测力使我们能够理解各维度的相对作用：例如，信息过载理论预期冗余性对成功的边际效应随上下文体量先正后负（Eppler and Mengis 2004），而充分性预期为正向但边际递减。因此，本文提出三个研究问题：（1）测量质量：三个工具是否测度了理论上可区分、经验上稳定且与构念一致的属性？（2）增量价值：CPE 各维度在预测任务成功与成本超支上，是否相对既有度量（token 数、步数、成本、ACRR）提供显著增量信息，且呈现出理论预期的关系形态？（3）决策价值：CPE 的测量能否支持资源分配等决策，并产生可量化的收益？

---
### P5

为评估 CPE 框架的有效性，我们在仓库级缺陷修复情境中开展应用。我们使用 SWE-bench Verified（Jimenez et al. 2024）这一公开基准，并以公开可得的大规模 agent 轨迹语料（Bouzenia and Pradel 2025）构建事件日志；任务相关信息由 gold patch 触及的文件与符号推导（gold 定义详见第 3 节）。在该情境中，agent 先读取 issue 与仓库文件，再执行修改；我们据此构造充分性、冗余性与经济性的计算式操作化，并比较其与既有度量的预测表现。

### P6

我们进行深入的预测与价值分析以展示 CPE 框架的效用。首先，我们用多种预测方法（逻辑回归、梯度提升树等）与多种评价准则（AUC、NRI/IDI 增量判别指标等）在留出样本上评估预测表现。其次，我们比较包含与不包含 CPE 工具的模型设定，检验加入 CPE 后预测能力的显著提升；随后将 CPE 与替代度量（token 数、步数、成本、ACRR）逐一对比，并通过对预测精度差异的置信区间检验（DeLong et al. 1988; Diebold and Mariano 1995）证明 CPE 的显著增量价值。再次，我们检验理论预期关系，包括冗余性的倒 U 型效应与任务复杂度的调节作用。最后，基于测量结果，我们进行离线反事实决策评估：若按 CPE 诊断执行简单规则（高冗余任务提前停止、低充分性任务追加预算），固定总预算下的成本-成功前沿是否得到提升。

### P7

我们同样考察不同维度在预测中的相对贡献。理论预期，冗余性维度在简单任务上更具区分力（简单任务中过度阅读是主要浪费），而充分性维度在复杂任务上更具区分力（复杂任务中读漏是主要失败原因）。【占位：此部分结果待实验完成后填写。】

### P8

本研究作出若干贡献。第一，我们为 IS 中日益增长的编码智能体研究补充了测量基础：据我们所知，这是第一个理论锚定、计算式操作化、并在大规模公开轨迹上验证的编码智能体信息处理测量框架。与既有网络度量只考虑连接而忽略信息内容不同（对应 EAC 的贡献定位，Shangguan et al. 2022），CPE 直接测量被结果指标遗漏的信息处理构念。第二，我们为信息过载与信息质量研究在自主智能体情境中的延伸提供机制证据：通过开发可检验的测量，我们使"信息过载是否以及如何损害 agent 决策"这一此前不可测的问题变得可检验。第三，对实践者，我们提供一个标准化的效率评价协议与诊断工具：研究者可用其在论文间进行可比的效率声明（缓解当前效率定义各异的状况），工程团队可用其定位失败机制并据此选择干预手段。

---

## 2. Research Design：构念与测量框架

### 2.1 CPE 构念界定

CPE 框架的中心构念是编码智能体的上下文处理效率，定义为"在给定任务与处理约束下，智能体的信息处理行为与决策相关信息集的一致程度"。该构念分解为三个维度：

- **充分性（Sufficiency, SI）**：决策相关信息中被智能体实际访问的比例。对应信息质量中的相关性维度（Wang and Strong 1996）：信息不充分导致决策基础缺失。
- **冗余性（Redundancy, RI）**：被访问信息中与决策无关或重复处理的比例。对应信息质量的简洁性维度与信息过载文献中的冗余概念（Eppler and Mengis 2004）：冗余消耗有限处理能力。
- **经济性（Economy, EI）**：单位决策结果所消耗的信息处理成本。对应有限理性框架下的处理成本（Simon 1955）：同样的结果，成本越低效率越高。

三个维度共同覆盖"读什么（充分性）、读了多少不该读的（冗余性）、每单位成功花多少（经济性）"，即"感知-处理-成本"的完整决策环节。

### 2.2 为什么不合成单一复合指标

我们明确不把三个维度合成为一个复合分数，理由如下。

第一，三个维度具有不同的理论起源与不同的预期函数形态：充分性预期为正向且边际递减，冗余性预期为倒 U 型（适度冗余可能提供交叉验证，过度冗余造成过载），经济性是成本侧约束而非收益侧构念。将不同符号与不同形态的维度线性加权，需要一种尚不存在的权重理论，且加权会抹除机制信息。第二，复合指标会破坏诊断价值：CPE 的核心用途是回答"这个任务为什么失败"，而复合分数无法区分失败画像。第三，IS 与相关领域的成熟测量先例均为多维不聚合结构：信息质量本身是多维构念（Wang and Strong 1996），NASA-TLX 工作负荷以六个独立子量表呈现（Hart and Staveland 1988），软件度量套件（Chidamber and Kemerer 1994）同样提供一组工具而非单一数字。因此，本文的人工制品是"框架"：三个独立验证的工具加一个诊断协议，而非一个复合指数。若未来理论给出原则性的权重，聚合可作为扩展，但这不是本文的主张。

### 2.3 计算式操作化

设任务 t 的决策相关信息集为 $G_t$（由 gold patch 触及的文件与符号推导），agent 实际访问的信息集为 $A_t$（由轨迹事件日志推导），访问的 token 量为 $c_t$，任务成功指示为 $s_t$。草案公式：

- 充分性：$SI_t = |G_t \cap A_t| / |G_t|$（gold 覆盖率的任务级均值）
- 冗余性：$RI_t = 1 - |G_t \cap A_t| / |A_t|$（访问集内的无关比例；亦可按 token 加权与按访问顺序的重复访问惩罚扩展）
- 经济性：$EI_t = \mathbb{E}[c \mid s=1]$ 的逆或成本-成功前沿距离（草案；见 2.4）

### 2.4 在编码智能体情境中的操作化

我们将轨迹表示为事件日志（事件=读文件/编辑/运行命令/测试；属性=文件路径、token 数、退出码），从事件日志中提取访问集 $A_t$；gold 相关信息集 $G_t$ 由公开 gold patch 与仓库依赖图推导。为支持部署场景下的在线使用，我们同时给出无需 gold 的近似：以 issue 关键词与已读文件的重叠度近似充分性，以检索相关性分数阈值近似冗余性。测量窗口采用轨迹前缀（如 20%/40%/60% 进度），以支持早期预警用途。【占位：公式的最终形式与窗口敏感性分析待实验确定。】

---
## 3. Data and Trajectory Corpus

我们从公开来源收集编码智能体轨迹数据。任务层面，我们使用 SWE-bench Verified（Jimenez et al. 2024）的全部任务作为任务集；轨迹层面，我们使用公开可得的多个 scaffold（OpenHands、AutoCodeRover、RepairAgent 等）在 SWE-bench 上的完整轨迹语料（Bouzenia and Pradel 2025），其轨迹包含 thought、tool call 与 observation 的完整序列。【占位：最终语料版本、任务数与轨迹数在实验开始时固定并登记。】

我们将每条轨迹转换为事件日志：每个工具调用或编辑视为一个事件，属性包括操作类型、文件路径、token 消耗、时间戳与退出码；gold patch 与仓库依赖图用于推导任务相关信息集 $G_t$。为捕捉信息处理的动态变化，我们采用前缀窗口方式：分别以轨迹的 20%、40%、60% 进度截取前缀，计算各窗口下的 SI/RI/EI，用于早期预测分析。【占位：窗口敏感性分析待实验完成。】

## 4. Methodology

### 4.1 预测模型

为展示 CPE 的价值，我们评估其能否预测任务成功与成本超支。任务成功（resolve）与成本超支（成本超过某分位）是编码智能体文献中常用的结果（Jimenez et al. 2024; Bouzenia and Pradel 2025）。除 CPE 工具外，我们纳入已知结果决定因素作为基线：token 数、步数、总成本、任务难度代理（如涉及文件数、issue 长度）与 ACRR。为控制任务特性，我们加入任务与仓库层面的控制变量。基线模型采用逻辑回归；由于非线性模型可能带来更好的预测效果，我们同时使用梯度提升树与随机森林，并通过正则化、树深度限制与训练-测试误差对比控制过拟合（Dietterich 2000）。

### 4.2 评估策略

我们的验证策略是在留出样本上检验增量预测力与理论关系，共五条：

1. **有无 CPE 对比**：比较含与不含 CPE 工具的模型，检验加入后 AUC 的显著提升（DeLong et al. 1988 与 NRI/IDI 双口径）。
2. **与替代度量对比**：将 CPE 各维度与 token 数、步数、成本、ACRR 逐一对比，检验增量预测力的置信区间（Diebold and Mariano 1995 口径）。
3. **替代规格对比**：比较不同的 RI 加权方式（token 加权 vs 访问次数加权）与不同的 SI 推导方式（gold 文件级 vs 符号级），检验测量规格的稳健性。
4. **测量质量与稳健性**：跨 scaffold、跨模型报告维度稳定性（ICC 或秩相关）；以人工标注检验 RI 与构念的一致性（陈诗沁式分组排序一致率协议）；在不同窗口与不同正则下报告稳健性。
5. **离线决策评估**：基于测量的反事实预算分配——按 CPE 诊断执行简单规则（高 RI 提前停止、低 SI 追加预算）与均匀分配对比，报告固定总预算下的成本-成功前沿。【占位：第 5 条的规则形式与评估协议在实验前冻结。】

### 4.3 理论关系检验

为检验信息过载理论在 agent 情境的适用性，我们设定：冗余性 RI 与成功概率呈倒 U 型关系（一次项为正、二次项为负），充分性 SI 与成功概率呈正向且边际递减关系，任务复杂度对二者具有调节作用（复杂任务下 SI 的边际作用更强，简单任务下 RI 的负作用更强）。检验采用带二次项的逻辑回归与分组分析。【占位：假设表述与检验细节待与理论文献对齐后定稿。】

## 5. Results（占位章节）

> 本节为拟实施分析的表述模板；真实结果未产生前，不填写任何数字。所有句式为"我们检验/报告/比较……"，实际完成实验后改写为事实陈述。

### 5.1 测量质量

我们报告三个工具的描述性统计、跨 scaffold 与跨模型的稳定性，以及 RI 与人工标注的一致率。若维度间相关过高，则报告判别效度问题并讨论是否需要合并或修正。

### 5.2 增量预测力

我们报告含与不含 CPE 的模型在 AUC、NRI/IDI 上的差异，以及 CPE 与各替代度量的对比结果与置信区间。

### 5.3 理论关系

我们报告 RI 的倒 U 型检验（一次项/二次项系数、拐点位置）、SI 的边际递减检验与任务复杂度的调节效应。

### 5.4 离线决策价值

我们报告反事实预算分配下成本-成功前沿的对比结果，以及诊断规则的命中率（被诊断为 RI 失败的任务，裁剪干预的预期收益）。

## 6. 维度贡献与失败画像分析

对应 EAC 第 6 节"不同信息源的相对贡献"，本节考察三个维度的相对贡献与失败画像结构。第一，各维度在预测中的增量贡献排序（简单任务 vs 复杂任务分组）。第二，失败画像分布：以 SI/RI/EI 的阈值将失败任务分类为充分性失败、冗余性失败与经济性失败，报告画像的稳定性与跨 scaffold 一致性。第三，画像与任务特征的关联（任务复杂度、仓库规模、issue 长度），为"何时优先干预哪个维度"提供实证依据。【占位：全部结果待实验完成。】

## 7. Discussion and Conclusion

本研究开发并评估了编码智能体上下文处理效率的测量框架。我们首先将信息质量与信息过载理论情境化到编码智能体这一新型信息处理决策者，其次将三个理论维度操作化为计算式工具，再通过测量质量、增量预测力、理论关系与离线决策价值四重证据评估框架价值。

理论贡献上，本文回应了"自主智能体作为决策者的信息处理如何测量"这一 IS 新问题：与 EAC 为信息流提供可预测的代理一样（Shangguan et al. 2022），CPE 为 agent 的信息处理提供理论锚定的测量基础，使信息过载机制在 agent 情境中可检验。方法贡献上，本文示范了计算式测量框架的验证协议——不以心理测量学信度为唯一标准，而以稳定性、增量预测力、理论关系与决策价值共同构成证据链。实践贡献上，本文提供标准化的效率评价协议，缓解当前文献效率声明不可比的问题，并为工程团队提供失败机制诊断工具。

局限与未来方向包括：测量依赖公开轨迹与 gold patch，对无 gold 的部署场景需在线近似（本文提供草案）；框架的三个工具是否需要在特定任务类型下合并，留待未来理论发展；本研究的任务集限于 SWE-bench Verified 类仓库级缺陷修复，推广到代码审查、重构等任务需进一步验证。

---

## 参考文献（草稿，投稿前逐条核验）

- Simon, H. A. (1955). A behavioral model of rational choice. The Quarterly Journal of Economics, 69(1), 99–118.
- Simon, H. A. (1991). Bounded rationality and organizational learning. Organization Science, 2(1), 125–134.
- Eppler, M. J., and Mengis, J. (2004). The concept of information overload: A review of literature from organization science, accounting, marketing, MIS, and related disciplines. The Information Society, 20(5), 325–344.
- Karr-Wisniewski, P., and Lu, Y. (2010). When more is too much: Operationalizing technology overload and exploring its impact on knowledge worker productivity. Computers in Human Behavior, 26(5), 1061–1072.
- Wang, R. Y., and Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. Journal of Management Information Systems, 12(4), 5–33.
- DeLone, W. H., and McLean, E. R. (2003). The DeLone and McLean model of information systems success: A ten-year update. Journal of Management Information Systems, 19(4), 9–30.
- Hart, S. G., and Staveland, L. E. (1988). Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research. Advances in Psychology, 52, 139–183.
- Chidamber, S. R., and Kemerer, C. F. (1994). A metrics suite for object oriented design. IEEE Transactions on Software Engineering, 20(6), 476–493.
- Hevner, A. R., March, S. T., Park, J., and Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105.
- Gregor, S., and Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337–355.
- Shangguan, W., Leung, A. C. M., Agarwal, A., Konana, P., and Chen, X. (2022). Developing a composite measure to represent information flows in networks: Evidence from a stock market. Information Systems Research, 33(2), 594–613.
- Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and Narasimhan, K. (2024). SWE-bench: Can language models resolve real-world GitHub issues? ICLR 2024. arXiv:2310.06770.
- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., and Liang, P. (2024). Lost in the middle: How language models use long contexts. Transactions of the Association for Computational Linguistics, 12, 157–173.
- Bouzenia, I., and Pradel, M. (2025). Understanding software engineering agents: A large-scale trajectory study. arXiv:2506.18824.（预印本，投稿前核验）
- Qin, Y., and Xie, T. (2026). Agent Retrieval Bench. arXiv:2607.24882.（预印本，投稿前核验）
- Zhang, W., and Wang, X. (2026). SWE-Explore. arXiv:2606.（预印本，投稿前核验）
- Yin, Y., and Feng, J. (2026). Do AI agents know when a task is simple? (ACRR/E3). arXiv:2607.13034.（预印本，投稿前核验）
- DeLong, E. R., DeLong, D. M., and Clarke-Pearson, D. L. (1988). Comparing the areas under two or more correlated receiver operating characteristic curves: A nonparametric approach. Biometrics, 44(3), 837–845.
- Diebold, F. X., and Mariano, R. S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263.
- Dietterich, T. G. (2000). Ensemble methods in machine learning. International Workshop on Multiple Classifier Systems, 1–15.
- SWE-Effi（2025）. arXiv:2509.09853.（预印本，投稿前核验；用于"效率口径不可比"现象）
- icat-agent（2026）. arXiv:2606.25514.（预印本，投稿前核验；用于"成本差异"现象）
- AgentDiet（2025）. arXiv:2509.23586.（预印本，投稿前核验；用于"轨迹浪费"现象）

---
## 附录 A：段落级写作对照与引用作用审计

对照对象：#27 EAC（Shangguan et al. 2022, ISR）全文第 1–7 节。模仿限于段落功能、句间逻辑与引用角色，不复制原句。

### A.1 引言八段对照

| 本稿段落 | 对照 EAC 段落 | 段落唯一功能 | 句间逻辑 | 引用作用 |
|---|---|---|---|---|
| P1 | EAC P1（数字平台→既有工作→缺口→研究定位） | 从共同事实进入情境，定位缺口 | 事实→既有做法→但（缺口）→因此本研究 | 定位既有工作（Jimenez et al. 2024 结果度量；Qin and Xie 2026; Zhang and Wang 2026 检索；Bouzenia and Pradel 2025 轨迹） |
| P2 | EAC P2（理论动机→因此需要新度量→引入工件→设计科学评估） | 理论论证"为什么需要" | 理论（有限理性）→情境化（信息过载）→因此需要多维测量→我们开发 CPE→遵循设计科学 | 理论依据（Simon 1955/1991; Eppler and Mengis 2004; Karr-Wisniewski and Lu 2010; Liu et al. 2024）；方法规范（Hevner et al. 2004; Gregor and Hevner 2013）；先例（Wang and Strong 1996; DeLone and McLean 2003; Shangguan et al. 2022） |
| P3 | EAC P3（新度量相对既有度量的四点优势） | 逐条论证新工件相对既有工具的差异 | First/Second/Third/Fourth 平行结构，最后回收与 EAC 的类比 | 对比对象引用（ACRR 隐含；Shangguan et al. 2022 类比） |
| P4 | EAC P4（为何检验预测力+研究问题） | 导出三个研究问题 | 为什么检验→能理解什么→三个 RQ | 理论预期引用（Eppler and Mengis 2004 倒 U） |
| P5 | EAC P5（应用情境与数据） | 界定情境 | 情境→数据→操作化来源 | 数据引用（Jimenez et al. 2024; Bouzenia and Pradel 2025） |
| P6 | EAC P6（评估设计预览） | 预告评估证据链 | 多方法→有无对比→替代对比→置信区间→理论检验→决策评估 | 统计方法引用（DeLong et al. 1988; Diebold and Mariano 1995） |
| P7 | EAC P7（来源分析结果预览） | 预告维度分析 | 理论预期→分组预期 | 理论引用（Eppler and Mengis 2004） |
| P8 | EAC P8（三点贡献） | 贡献声明 | First/Second/Third | 贡献定位引用（Shangguan et al. 2022 对应 EAC 定位自身） |

### A.1.1 引言逐句功能审计（P1–P8，对应 EAC 原文句功能）

| 段落 | 句序 | EAC 句功能（原文依据） | 本稿句功能 | 本句引用作用 |
|---|---|---|---|---|
| P1 | S1 | 数字平台活动促进信息流（情境） | 编码智能体在平台上的活动构成信息处理过程 | 无（共同事实） |
| P1 | S2 | 平台以"共同浏览"呈现活动（最简形态） | agent 活动被记录为可审计轨迹 | 无 |
| P1 | S3 | 研究者用足迹构建网络并评估结果（既有工作） | 研究者用轨迹构建上下文并评估任务结果 | 定位既有工作（Jimenez et al. 2024; Qin and Xie 2026; Zhang and Wang 2026; Bouzenia and Pradel 2025） |
| P1 | S4 | However：除直接信息外多种来源贡献信息流（引入复杂性） | 然而：效率声明口径互不相同、成本差异可达数量级（引入现象缺口） | 现象证据（SWE-Effi; icat-agent） |
| P1 | S5 | 信息直达（attention）与跨节点（coattention）之分（概念区分） | 信息处理可分：读了什么/多读什么/单位成本（概念区分） | 无 |
| P1 | S6 | 现有度量只基于链接、不表征信息流（缺口） | 现有度量只基于结果或体量、不表征处理质量（缺口） | 无（缺口句不带引用，符合 EAC 惯例） |
| P1 | S7 | 本研究开发新度量并评估经济影响（研究定位） | 本研究开发测量框架并评估价值（研究定位） | 无 |
| P2 | S1 | 有理由用网络方法建模信息流（论点） | 有理由多维刻画信息处理（论点） | 无 |
| P2 | S2 | 理论：传播偏差与放大过程（Hirshleifer 2015） | 理论：有限理性（Simon 1955, 1991） | 理论依据（Simon） |
| P2 | S3 | 产品市场同理（推广） | 信息过载：处理需求超过能力则表现下降（Eppler and Mengis 2004; Karr-Wisniewski and Lu 2010） | 理论依据（信息过载） |
| P2 | S4 | 因此复合度量更优并可预测（含义） | 仓库上下文既可是资源也可是负担（Liu et al. 2024）→ 因此多维测量框架可预测可诊断（含义） | 情境化理论（Liu et al. 2024） |
| P2 | S5 | 扩展特征向量中心性开发 EAC（工件引入） | 基于信息质量多维结构开发 CPE 框架（Wang and Strong 1996; DeLone and McLean 2003; Shangguan et al. 2022） | 构念来源 + 计算度量先例 |
| P2 | S6 | 工件定义+设计科学评估（Hevner et al. 2004; Gregor and Hevner 2013） | 工件定义+设计科学评估（同引） | 方法规范（设计科学） |
| P3 | S1 | EAC 提供若干好处（论点） | CPE 相对常用度量提供若干优势（论点） | 无 |
| P3 | S2 | First：链接异质性 | First：结果度量只反映发生了什么，不反映为什么 | 无 |
| P3 | S3 | Second：节点异质性 | Second：单维过程度量无法刻画维度间权衡 | 无 |
| P3 | S4 | Third：多路径扩散 | Third：既有度量缺乏理论锚定 | 无 |
| P3 | S5 | Last：复合权重 | Fourth：CPE 提供诊断协议（失败画像） | 无 |
| P3 | S6 | 因此 EAC 捕获 attention+coattention（收束） | 与 EAC 类比：贡献在于测量遗漏的构念而非替换结果度量（收束） | 类比定位（Shangguan et al. 2022） |
| P4 | S1 | 考察预测力很重要（重要性） | 考察增量预测力很重要（重要性） | 无 |
| P4 | S2 | 预测力使我们理解来源相对影响（目的） | 预测力使我们理解维度相对作用（目的） | 无 |
| P4 | S3 | 例：Luo et al. 社交优于传统（例证） | 例：信息过载预期 RI 倒 U、SI 正向递减（例证） | 理论预期（Eppler and Mengis 2004） |
| P4 | S4 | 文献收窄：单源/标准度量、无人比较（缺口收窄） | 由此导出三个研究问题（RQ 导出） | 无 |
| P4 | S5 | 三个 RQ（问题） | 三个 RQ：测量质量/增量价值/决策价值（问题） | 无 |
| P5 | S1 | 应用情境：金融门户（情境） | 应用情境：SWE-bench Verified 缺陷修复（情境） | 数据（Jimenez et al. 2024） |
| P5 | S2 | 范围与时段（范围） | 公开轨迹语料构建事件日志（数据） | 数据（Bouzenia and Pradel 2025） |
| P5 | S3 | 节点/边定义（结构） | gold patch 推导任务相关信息（结构） | 无 |
| P5 | S4 | 权重定义（度量） | 构造 SI/RI/EI 操作化并比较（度量） | 无 |
| P5 | S5 | 四种信息源（来源） | （合并入 S2–S4，本稿不设独立来源句） | — |
| P6 | S1 | 深入预测分析（方向+幅度）（论点） | 深入预测与价值分析（论点） | 无 |
| P6 | S2 | First：多方法多准则留出样本（方法） | 多方法多准则留出样本（方法） | 无 |
| P6 | S3 | Second：含/不含 EAC 对比（有无） | 含/不含 CPE 对比（有无） | 无 |
| P6 | S4 | Then：与替代度量对比（对比） | 与替代度量逐一对比（对比） | 无 |
| P6 | S5 | Moreover：置信区间检验（显著性） | 置信区间检验（DeLong et al. 1988; Diebold and Mariano 1995） | 统计检验规范 |
| P6 | S6 | Finally：交易策略（经济价值） | 最后：离线反事实预算分配（决策价值） | 无 |
| P7 | S1 | 研究不同信息源重要性（论点） | 考察维度相对贡献（论点） | 无 |
| P7 | S2 | 复合优于分离（结果预告） | 预期 RI 在简单任务更具区分力（预期） | 理论（Eppler and Mengis 2004） |
| P7 | S3 | 社交优于传统（结果预告） | 预期 SI 在复杂任务更具区分力（预期） | 理论 |
| P7 | S4 | 复合/社交优于注意力度量（结果预告） | 【占位】结果待填写 | — |
| P8 | S1 | 若干贡献（论点） | 若干贡献（论点） | 无 |
| P8 | S2 | First：IS 文献新度量（贡献1） | First：测量基础（贡献1） | 贡献定位（Shangguan et al. 2022） |
| P8 | S3 | 设计科学对齐+深入评估（支撑） | 与 EAC 同构的贡献定位句（支撑） | 无 |
| P8 | S4 | 预测力更强（主张） | 使机制可检验、效率声明可比（主张） | 无 |
| P8 | S5 | Second：信息扩散研究（贡献2） | Second：信息过载理论延伸（贡献2） | 理论定位（Eppler and Mengis 2004） |
| P8 | S6 | 实践者：建模方法（贡献3） | 实践者：标准化评价协议与诊断工具（贡献3） | 无 |
| P8 | S7 | 股票情境指导（收束） | （合并入 S6，不设独立收束句） | — |

### A.2 正文各节对照

| 本稿 | EAC 对应节 | 功能 |
|---|---|---|
| 2.1 构念界定 | 2.1 Concept of EAC | 先定义构念，再形式化 |
| 2.2 为什么不合成复合指标 | （EAC 无对应；为本文新增论证段） | 回应"合成指标不具逻辑性"：理论起源不同、函数形态不同、诊断价值要求多维、IS 先例均为多维不聚合 |
| 2.3 计算式操作化 | 2.1.3 EAC 数学定义 | 形式化公式草案 |
| 2.4 情境化操作化 | 2.2 EAC for Stocks | 构念在具体情境中的测量实现 |
| 3 数据 | 3 Data and Coattention Networks | 数据来源、采集、结构构建 |
| 4 方法论 | 4 Methodology（4.1 模型；4.2 评估策略） | 基线+控制变量；五条评估策略（与 EAC 的评估策略一一对应） |
| 5 结果（占位） | 5 Results（5.1 表现；5.2 差异；5.3 敏感性；5.4 交易策略） | 占位模板：测量质量/增量预测力/理论关系/决策价值 |
| 6 维度贡献与失败画像 | 6 不同信息源的预测表现 | 维度间相对贡献分析 |
| 7 讨论与结论 | 7 Discussion and Conclusion | 贡献三层（理论/方法/实践）+局限 |

### A.3 引用角色的总体规律（从 EAC 中提炼，本稿沿用）

1. **定位既有工作**：引言前段引用同类任务与既有度量，承认其有效部分，再指出边界（EAC 引 Agarwal et al. 2017 等；本稿引 SWE-bench/轨迹研究）。
2. **理论依据**：为"需要新构念"提供理论来源（EAC 引 Hirshleifer 2015；本稿引 Simon/信息过载/信息质量）。
3. **方法规范**：为评估范式背书（EAC 引 Hevner et al. 2004 设计科学；本稿同）。
4. **结果变量与控制的正当性**：EAC 引异常收益文献与控制变量文献；本稿引 resolve/cost 与任务控制。
5. **统计检验的正当性**：EAC 引 Fama-MacBeth/Newey-West；本稿引 DeLong/Diebold-Mariano。
6. **贡献定位**：在贡献段引用将被超越/将被补充的代表性文献（EAC 引 Luo et al. 2013; Chen et al. 2014；本稿引 Shangguan et al. 2022 作为计算度量先例）。

### A.3.1 引用实例对照（EAC 原文引用角色 → 本稿对应）

| EAC 原文引用实例 | 在 EAC 中的角色 | 本稿对应引用 | 在本稿中的角色 |
|---|---|---|---|
| Agarwal et al. 2017; Leung et al. 2017; Lin et al. 2017 | 定位既有应用（用网络链接评估市场结果） | Jimenez et al. 2024; Qin and Xie 2026; Zhang and Wang 2026; Bouzenia and Pradel 2025 | 定位既有评价实践（结果/检索/轨迹度量） |
| Hirshleifer 2015 | 理论依据（为什么信息流重要） | Simon 1955, 1991; Eppler and Mengis 2004; Karr-Wisniewski and Lu 2010 | 理论依据（有限理性/信息过载） |
| Borgatti 2005 | 方法来源（被扩展的度量） | Wang and Strong 1996; DeLone and McLean 2003 | 构念来源（被情境化的信息质量维度） |
| Hevner et al. 2004; Gregor and Hevner 2013 | 方法规范（设计科学评估范式） | 同左 | 方法规范（同左） |
| Luo et al. 2013（社交媒体 vs 传统媒体） | 例证：来源差异影响预测力 | Eppler and Mengis 2004（倒 U 预期） | 例证：理论预期关系形态 |
| Dewan and Ren 2007; Luo et al. 2013; Chen et al. 2014 | 结果变量正当性（异常收益常用于金融/IS） | Jimenez et al. 2024; Bouzenia and Pradel 2025 | 结果变量正当性（resolve/cost 常用于编码智能体文献） |
| Antweiler and Frank 2004; Brown and Cliff 2004; Baker and Wurgler 2007; Sabherwal et al. 2011 | 控制变量正当性（情绪） | （拟补：任务复杂度代理的控制变量文献，投稿前补齐） | 控制变量正当性 |
| Wahal and Yavuz 2013 | 控制变量正当性（同行联动） | （同上，投稿前补齐） | 控制变量正当性 |
| Fama and MacBeth 1973; Newey and West 1987; Pontiff and Woodgate 2008 等 | 估计方法正当性 | DeLong et al. 1988; Diebold and Mariano 1995 | 统计检验正当性 |
| Dietterich 2000; Rokach 2010; Kuncheva 2014 | 过拟合控制正当性（集成方法） | Dietterich 2000 | 过拟合控制正当性（可补 Rokach/Kuncheva） |
| Oestreicher-Singer and Sundararajan 2012; Susarla et al. 2012; Liu et al. 2020 等 | 缺口收窄（文献矩阵式引用证明"无人做过"） | （拟补：编码智能体度量文献矩阵，含 ACRR/SWE-Effi/AgentDiet） | 缺口收窄（证明"无人提供理论锚定多维测量"） |
| Luo et al. 2013; Chen et al. 2014（贡献段） | 贡献定位（被补充的研究流） | Shangguan et al. 2022 | 贡献定位（计算度量先例，本研究扩展其情境） |

### A.4 针对"动机存疑"与"复合指标不逻辑"的直接回应

- 动机存疑的回应位置：P1（缺口：结果度量不能解释为什么）、P2（理论：有限理性+信息过载使"信息处理"成为可测量的决策构念）、P8（贡献：测量基础使机制可检验、效率声明可比）。核心论证：**测量先于机制**——没有工具就无法检验 agent 信息过载理论，也无法让效率声明跨论文可比。
- 复合指标的回应位置：2.2 专段论证（理论起源不同、函数形态不同、诊断价值要求多维、先例均为多维不聚合）。核心论证：**框架而非指数**——三个工具各自独立验证，诊断协议提供可行动输出；若未来出现原则性权重理论，聚合留作扩展。
- 价值证明的回应位置：4.2 五条评估策略 + 5 节占位（测量质量、增量预测力、理论关系、离线决策价值四重证据），全部可在论文内部闭环，不依赖研究二/三/四。

### A.5 已知风险清单（初稿阶段）

1. "度量即贡献"在 ISR 的接受度：以 EAC 为直接先例（ISR 2022 发表），并在引言与贡献段显式引用其范式。
2. 审稿人可能质疑"这不是 IS 而是 CS"：每个维度锚定 IS 理论（信息质量/信息过载/有限理性），并强调诊断价值（决策支持）。
3. 结果度量（resolve）与 CPE 的判别效度：必须在 4.2 策略 1–2 中给出判别效度证据（相关结构+增量预测力），防止"换皮指标"批评。
4. 无 gold 的部署场景：2.4 提供在线近似草案，并列为局限。
5. 全部 arXiv 预印本引用需在投稿前重新核验版本与出处。