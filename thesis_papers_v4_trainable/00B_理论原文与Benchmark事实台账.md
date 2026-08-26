# 理论原文与 Benchmark 事实台账

## 一、台账用途

本文件只记录进入新版三篇的事实边界。论文正文仍需按段落论证，不得把本表整段搬入引言。数据集的存在只承担标签、环境和评价责任，不构成算法贡献。规模、版本与公开状态以最终实验冻结日的官方页面、正式论文和发布清单再次核对。

## 二、ISR 与 MISQ 理论原文

### 理论驱动学习方法的两篇写作参照

Xiao et al. 2024 的 ACAA 发表在 *Information Systems Research*。本地全文为 `database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md`。第 89 至 116 行从过程与粒度框架导出四项注意要求，第 124 至 224 行把要求转成 DTV 与 AMI 训练构件，第 230 至 314 行评价最终预测、中间表征、权重解释和消融。

Xiao et al. 2023 的 DSDL 发表在 *Information Systems Research*。本地全文为 `database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md`。第 81 至 109 行从期望确认过程导出偏好、经验、动态不确认与累计满意的学习要求，第 128 至 227 行形成偏好模板、跨视图注意和对比联合学习，第 231 至 315 行分别检验预测、表征、动态满意、解释与构件责任。

### 仓库证据的表征与行动责任

Burton-Jones and Grange 2013 将有效使用定义为以有助于实现系统使用目标的方式使用系统，并从表征理论说明信息系统通过表征支持行动。其本地全文 `database_fulltext_all/01272_2013_from-use-to-effective-use-a-representation-theory-perspective.md` 第 75 至 79 行给出有效使用定义，第 101 至 145 行说明表征、系统结构与面向需要的忠实度。论文一只迁移面向任务需要的表征和行动结果要求，不把人类使用行为赋予 Agent。

Shaft and Vessey 2006 研究软件理解与修改之间的认知匹配。其本地全文 `database_fulltext_all/00546_2006_the-role-of-cognitive-fit-in-the-relationship-between-software-comprehension-and-modification1.md` 第 49 至 69 行说明更多理解不必然改善修改，第 75 至 122 行说明软件表征与修改任务强调相同知识类型时可减少转换与干扰。原 TEGRA 仅迁移任务知识与软件证据知识是否相配的计算要求，不声称 Agent 形成了人的心智表征。由于公共数据不能独立标注这种匹配状态，原方案已经在立项闸门终止。

### 序贯信息取得与验证价值

Moore and Whinston 1986 以信息取得行动、信号、成本、最终决策和收益形式化序贯信息取得。其本地全文 `database_fulltext_all/16879_1986_a-model-of-decision-making-with-sequential-information-acquisition-part-1.md` 第 70 至 106 行界定信息行动、成本和信号，第 84 至 96 行把信息策略与最终决策置于同一收益函数。论文三的自适应验证模型迁移在最终决策前比较取得信息的期望收益与成本这一规范结构。

Dos Santos and Mookerjee 1993 说明信息取得成本会降低系统价值，并把知识库决定的输出与控制机制决定的取得顺序区分开来。其本地全文 `database_fulltext_all/17296_1993_minimizing-information-acquisition-costs.md` 第 45 至 63 行建立决策质量、信息取得成本和控制机制之间的责任，第 101 至 139 行定义在部分输入状态下继续取得或作出决策。论文三只把这一结构用于候选补丁验证，不沿用其无噪声或固定规则假设。

## 三、仓库证据与探索资源

### ContextBench

ContextBench 当前为 2026 年预印本及公开项目，论文为 Li et al. 2026, *ContextBench: A Benchmark for Context Retrieval in Coding Agents*, arXiv:2602.05892。官方项目报告 1,136 个 issue-resolution 任务、66 个仓库和 8 种语言，并为任务提供人工标注 gold context spans 与过程评价代码。当前研究以 release 中的文件路径、起止位置和内容字段为原始责任。文件标签可由路径聚合，AST block 必须由预注册 Tree-sitter 版本把 span 投影到最小包含语法块，因此 block 是本文适配单位，不得写成新增人工标注。Lite 或完整集合的具体分母仍须在实验冻结时从 release tag 核对。项目页为 [ContextBench](https://cioutn.github.io/context-bench/)。

在论文一中，ContextBench 承担主要人类证据监督、仓库隔离拟合与三粒度机制评价。它不承担成功轨迹事实，也不自动提供可执行的所有仓库环境。若执行子集需要重建容器，应单列环境合格率和任务分母。

### SWE-Explore

SWE-Explore 当前为 2026 年预印本及公开代码。官方仓库报告 848 个 issue、203 个开源仓库与 10 种语言。每项记录包含 issue、仓库快照元数据、从独立成功修复轨迹提炼的 line-level core 与 optional 区域、read-step provenance 和评价元数据。论文为 Zhang et al. 2026, *SWE-Explore: Benchmarking How Coding Agents Explore Repositories*, arXiv:2606.07297，代码为 [SWE-Explore-Bench](https://github.com/Qiushao-E/SWE-Explore-Bench)。

在论文一中，它承担轨迹定义证据的外部迁移。成功轨迹实际读过的区域不能被称为所有修复路径所必需的证据。原 TEGRA 的固定预算探索责任已经撤销，新的论文二不得沿用本条作为既定数据设计。

### Agent Retrieval Bench

Agent Retrieval Bench 当前为公开 benchmark 项目。官方页面报告 427 个样本、25 个开源仓库、345 个正例和 82 个 selective 无金标准任务。正例由 `code2test`、`comment2context`、`trace2code` 和 `edit2ripple` 四类工作流构成。Selective 集含自然无金标准任务与错误仓库控制。每个子集发布冻结 corpus 与评价工具。官方页面为 [Agent Retrieval Bench](https://agent-retrieval-bench.github.io/)。

在论文一中，ARB 只承担文件级工作流外部泛化、预算覆盖和选择性边界。它的 287 个 span-evidence core 如被投影为本文的块或行单位，必须明确这是研究适配而不是官方原生主指标。它不承担论文二的训练标签。

### RepoGraph 与 LocAgent

Ouyang et al. 2025 的 *RepoGraph: Enhancing AI Software Engineering with Repository-Level Code Graph* 正式发表于 ICLR 2025。它把仓库级代码图作为可插入模块，为 SWE agent 提供导航。正式论文为 [ICLR 2025 RepoGraph](https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf)。

Chen et al. 2025 的 *LocAgent: Graph-Guided LLM Agents for Code Localization* 正式发表于 ACL 2025，使用异构代码图和图导航 Agent 完成多跳定位，并训练 Qwen-2.5-Coder-Instruct-32B 版本。论文与代码入口为 [ACL Anthology](https://aclanthology.org/2025.acl-long.426/)。

这两项工作意味着论文一不得把仓库建图、图导航或训练专用定位 Agent 本身作为新颖性。论文一必须以人类证据的跨粒度一致测量和预算表征为中心。原 TEGRA 试图以显式任务需求、已读证据和剩余表征缺口建立差异，但因中间状态没有独立监督而终止。

### CodeRAG

Zhang et al. 2025 的 *CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion* 正式发表于 EMNLP 2025。它包含基于生成概率的 query construction、多路径检索和 preference-aligned BestFit reranking，评价场景是 repository-level code completion。正式入口为 [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1187/)。

论文二候选 Pilot 使用 developer diff 的 file、block 与 line 位置作为层次后验标签，研究固定观察预算下的位置不确定性更新。该标签不等于人类 needed-context，也不等于唯一正确修复方案。GraphLocator、ToolTrain、LocAgent、SWE-Search 和一般主动信息取得是正面近邻。差异只能建立在可校准的动态位置 belief、成本化后验风险下降及其独立中间检验上，不能以多路径检索、图网络或强化学习本身声称新颖性。

## 四、可执行训练与外测资源

### SWE-Gym

Pan et al. 2025 的 *Training Software Engineering Agents and Verifiers with SWE-Gym* 正式发表于 ICML 2025，PMLR 267:47717–47737。正式论文报告 2,438 个真实 Python 任务、11 个仓库、可执行环境、单元测试和自然语言任务，并公开模型与 Agent 轨迹。正式入口为 [PMLR](https://proceedings.mlr.press/v267/pan25g.html)。

SWE-Gym 在论文三中可承担候选补丁与验证矩阵生成。它只有 11 个仓库，任务数量不能替代仓库级独立性。三篇不得在以仓库隔离为主结论时把其任务随机拆入训练与测试。

### SWE-smith

Yang et al. 2025 的 *SWE-smith: Scaling Data for Software Engineering Agents* 正式发表于 NeurIPS 2025 Datasets and Benchmarks Track。正式论文报告 50,000 个合成可执行实例，来自 128 个 GitHub 仓库，并公开构造程序、任务、轨迹和模型。正式入口为 [NeurIPS Proceedings](https://papers.nips.cc/paper_files/paper/2025/hash/8b86cf5ace600c48fd188efbb8dedec8-Abstract-Datasets_and_Benchmarks_Track.html)。

SWE-smith 可提供训练规模，但合成故障不应掩盖真实 issue 的外部效度。论文一如使用 patch locus，只作辅助预训练。论文三可用其环境生成候选与验证矩阵。新的论文二若使用 SWE-smith，必须重新定义其标签责任。三篇共享同一任务时不能把结果当作三次独立复制。

### SWE-rebench

Badertdinov et al. 2025 的 *SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents* 正式发表于 NeurIPS 2025 Datasets and Benchmarks Track。正式论文报告公开数据超过 21,000 个交互式 Python 软件工程任务，并提供持续收集新鲜任务的方法。正式入口为 [NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/21bec6ace947b1b58967b945c8ac0f10-Abstract-Datasets_and_Benchmarks_Track.html)。

论文一行动检验与论文三可从冻结时间窗中形成仓库隔离外测。公开 SWE-rebench 本身不等于任何基础模型均未见过其代码或 issue。若声称时间去污染，需要按任务创建时间、模型训练截止时间和封存协议另行证明。

## 五、测试生成与补丁验证近邻

Ahmed et al. 2025 的 *Otter: Generating Tests from Issues to Validate SWE Patches* 正式发表于 ICML 2025，PMLR 267:752–771。Otter 只看 issue 与原始仓库生成修复前失败、修复后通过的测试，并用生成测试过滤 SWE agent 补丁。正式入口为 [PMLR](https://proceedings.mlr.press/v267/ahmed25b.html)。

Pan et al. 2025 的 SWE-Gym 已训练静态 verifier 做 best-of-n 候选选择。因此论文三不能把训练补丁 verifier、从 issue 生成测试或用测试过滤补丁写成研究空白。其候选差异只可能位于冻结测试库上，依据候选集合与部分结果动态估计下一验证组的信息价值，并联合 patch-select 与 abstain。

传统 automated program repair 已研究过度拟合补丁检测、生成测试和验证加速。论文三的文献综述必须覆盖这些正式工作，并逐项核查 2025 至 2026 年 Coding Agent 的 test-generation、test-consolidation、debugging 与 patch-selection 工作。若已有正式方法同时覆盖 issue-driven 候选池、部署时可见复现测试库、候选集合条件的序贯信息价值和选择或放弃，论文三停止立项。

## 六、事实冻结与引用规则

所有 2026 年预印本在正文和参考文献中明确标为预印本。正式会议论文按正式 venue、页码与 DOI 引用，不再引用较早 arXiv 版本作为发表状态。官方 GitHub 只支持数据字段、发布对象、下载与运行说明，算法主张优先由正式论文支持。

最终冻结前，对所有数据资源保存 release tag、commit hash、下载清单、文件校验和与许可。对所有模型保存权重 revision、tokenizer revision 和许可证。任何规模变化均先更新本台账，再同步三篇正文、逐段审计和交叉验收报告。
