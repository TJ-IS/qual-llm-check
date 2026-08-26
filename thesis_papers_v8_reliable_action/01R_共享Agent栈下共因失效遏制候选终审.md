# 共享 Agent 栈下共因失效遏制候选终审

> **终局判定：NO-GO，不冻结为三篇论文中的独立一篇。置信度：高。**
> **证据截止：2026 年 8 月 16 日。实验状态：本候选没有运行训练、离线策略学习或在线干预实验，本文中的模型、损失、算力与结果指标均为终审用设计规格，不是已发生的结果。**

## 0. 终审结论先行

组织让同一基础模型、agent scaffold、工具链和更新版本同时驱动多个 coding-agent 任务时，一项共同误解或单点升级确实可能使多个仓库在短时间内出现相关的危险命令、安全回归、功能破坏或虚假完成。这个风险对象真实、具有组织后果，也有必要从单次任务的边际失败率上升到 fleet-level joint harm。候选的问题重要性因此通过。

候选没有通过独立理论—算法贡献门。将它钢人化之后，最强工件是一个沿共享组件谱系推断动态共因状态的层级生存或因子模型，再接一个以相关尾部损害、成功率、吞吐和成本为约束的序贯策略。该策略可选择分批运行、配置多样化、影子验证、暂停传播和回收变更。可是，在完全相同的谱系、轨迹、任务、风险、成本和动作信息下，等参数的动态因子图、异质图 Transformer 加 distributional CMDP 能够实施同一前向计算和同一动作。候选理论没有产生一种通用替代无法复制的中间状态、结构约束或方向选择。

直接近邻进一步占据了候选试图依靠的各项核心能力。Temizkan、Park 与 Saydam 的 ISR 论文已经从软件单一化造成共享脆弱性出发，建立节点—漏洞矩阵、软件多样性指标、网络拓扑加权配置优化、动态分配算法和安全—成本权衡。[本地全文](../database_fulltext_all/03040_2017_software-diversity-for-improved-network-security-optimal-distribution-of-software-based-shared-v.md) Ron、Baudry 与 Monperrus 已经在 coding agents 上直接检验 N-version 的独立失效假设、模型—harness—语言多样性和多数投票可靠性。[论文与公开工件](https://arxiv.org/html/2606.20158) Koran 等人已经用误差相关性和个体质量选择多样化监控器集合。[论文](https://arxiv.org/html/2605.15377) 分批验证、影子运行、暂停、激活与回滚则同时落入可靠发布研究和 AI 组件生命周期治理。把这些能力接到一个 fleet 控制面上能够形成有价值的工程系统，却没有自动形成一篇新的 ISR 级理论驱动算法论文。

删除 coding-agent 语境后，这一判断更加清楚。将 fleet 单元替换成批处理作业、微服务实例、风控模型或机器人，把模型、harness 和工具链替换成共享库、运行时与配置版本，谱系图、共因潜变量、相关尾险目标以及 canary、diversify、shadow、pause、rollback、withdraw 动作均保持不变。coding-agent 只改变观测模态和损害 oracle，没有改变核心计算或行动语义。因此，本候选不能以“agent fleet governance”之名占用独立论文席位。

## 1. 候选的正确风险对象与可证伪边界

### 1.1 研究单位不是单个失败，也不是 incident 数量

设一个决策期内有 $N$ 个 coding-agent 工作单元。工作单元可以是同时运行的仓库任务、同一组织内的待执行变更，或者同一更新版本的分批 cohort。第 $n$ 个单元使用 $K$ 类共享组件中的若干版本，包括基础模型、harness/scaffold、系统提示与上下文规则、工具适配器、权限策略、测试与 judge、依赖解析器和部署连接器。候选要解释的结果不是某个单元是否失败，而是给定暴露集合后，多个单元在相近时间窗内遭遇同类或相互放大的实际损害：


\[
Y_{nrt}=1
\]

表示单元 $n$ 在时点 $t$ 遭遇风险类型 $r$ 的可执行损害。可接受的 $r$ 包括隔离环境中可验证的越权命令、不可逆状态破坏、安全回归、隐藏功能回归、错误部署、已执行的虚假完成，以及这些变更在依赖图上的传播。静态告警、LLM judge 的怀疑分数、最终回复中的拒绝语句和日志中出现的危险词都不能单独充当 $Y$。

相关损害与共因失效不是同义词。任务难度、共享测试错误、同一输入分布、重复样本或观测窗口都可能制造相关性。只有当一个共享组件、共同规范盲区或共同控制面事件对多个后代单元的损害有可识别影响时，才能称为 common-cause failure state。若所有组织在每个时点只部署一个 stack 版本，版本、时间、任务批次和组织状态完全共线，观察日志无法识别这个状态。审查因此要求随机化或准随机的版本交错、并行克隆任务、重复种子、明确的暴露分母和可执行损害 oracle。

基准中的 incident count 也不是生产概率。SABER 的 716 个风险任务、某个安全补丁集的 105 个条目或一百万次共享测试输入提供的是研究者定义采样框内的条件频率。只有给出任务抽样机制、每一 component-version 的暴露次数、随机种子、停止规则和 censoring，才能估计条件风险；没有组织部署基率时，不能把该频率外推成“组织发生概率”。

### 1.2 候选必须同时改变的行动与结果

候选若成立，算法必须在 coding agent 尚可改变后果的时点介入，并真正执行下列至少一类动作：改变尚未启动任务的 stack 配置；把共享更新限制到随机化 cohort；让部分任务在隔离环境使用独立 stack 重做；封存并调用独立隐藏验证；撤销正在传播的工具权限；暂停同谱系后代任务；回滚共享配置；隔离或回收已产生的补丁和状态变更；在证据恢复后有条件继续。只输出风险分数、推荐一个模型、生成 dashboard 或发送告警均不足以成立。

评价也必须在匹配任务成功或匹配吞吐条件下比较：受损工作单元数、同一时窗内同时受损单元数、最坏 cohort 损害、依赖加权传播范围、不可逆副作用、成功任务数、完成延迟、token 与 sandbox 成本、被暂停的正常任务、人工升级次数和恢复时间。降低所有执行量自然会降低 incident count，不能算作风险控制能力。

### 1.3 三项识别要求

第一，共因必须与边际能力分开。某 stack 的平均失败率高，不等于它造成更多相关失败；某个平均能力稍弱的 stack 也可能通过低条件相关性改善组合尾险。第二，共享组件原因必须与任务家族原因分开。同一规范的歧义可能让不同模型和语言共同失效，N-version 实验已经显示这一点。第三，控制策略效果必须与选择效应分开。若策略只把简单任务送入 canary、把困难任务冻结，事后相关损害下降并不能证明干预有效。

## 2. 截止日最直接工作的终止型回读

### 2.1 决定性近邻矩阵

| 一手来源 | 已经建立的对象、数据与动作 | 对本候选的直接挤压 | 尚未覆盖，但不足以自动构成新论文的部分 |
|---|---|---|---|
| Temizkan, Park, and Saydam (2017), *Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities*, ISR, DOI [10.1287/isre.2017.0722](https://doi.org/10.1287/isre.2017.0722) | 软件产品共享漏洞造成相关感染；节点—漏洞矩阵；信息论多样性指标；两个组合线性规划；拓扑加权分配；新增节点的动态分配；SIS 传播与采购成本 | 已经直接占据“共享组件脆弱性—系统级传播—多样化配置—动态重配—安全成本权衡” | coding-agent 轨迹、部分可观测的语义盲区和补丁/命令损害 |
| Ron, Baudry, and Monperrus (2026), *N-Version Programming with Coding Agents*, arXiv:2606.20158，[论文](https://arxiv.org/html/2606.20158)，[代码与生成版本](https://github.com/ASSERT-KTH/Knight-Leveson-Redux) | 69 个 harness—model—language 配置，48 个通过准入；一百万共享输入；显著共现失效；跨 agent 和语言的故障簇；17,296 个三版本多数投票组合 | 已经直接占据 coding-agent 共因失效、可用多样性轴、错误相关性和 N-version 可靠性收益 | 多仓库异质任务、随时间更新、非投票型 containment |
| Koran et al. (2026), *Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute*, arXiv:2605.15377，[论文](https://arxiv.org/html/2605.15377) | 12 个 prompted/fine-tuned monitor；APPS ControlArena 与 BigCodeBench-Sabotage；先保证单体质量，再利用低相关信号组成集合 | 已经占据“独立影子验证器＋相关性驱动组合＋安全成本” | 不处理 fleet 共享 stack 的状态传播 |
| Yao et al. (2026), *Harness-Bench*, arXiv:2605.27922，[论文](https://arxiv.org/html/2605.27922)，[官方仓库](https://github.com/Qihoo360/harness-bench) | 106 个离线沙箱任务、6 个可配置 harness、8 个模型、5,194 条轨迹；固定外部环境并保留原生 harness 行为 | 已经占据 model×harness×task 的大规模可执行比较与失败症状；可作为 warm start | 每 cell 基本是一条完整尝试；安全 gate 在公开汇总中几乎无阳性；不是共享更新 episode |
| Vats and Golev (2026), *The Scaffold Effect in Coding Agents*, arXiv:2607.22585，[论文](https://arxiv.org/html/2607.22585)，[公开补充材料](https://anonymous.4open.science/r/scaffold-effects-dl4c-supp/) | 3 harness×2 model×50 Terminal-Bench Pro 任务；原始日志；跨模型复现的 harness failure fingerprint | 已占据“共同 harness 会产生模型无关失效指纹”的关键经验命题 | 只有 6 个 SEC 和 2 个 SYS 任务；没有真实 fleet/update/containment |
| *Don’t Blame the Large Language Model: How Agent Harness Evolution Shapes Coding Agent Quality* (2026), arXiv:2607.03691，[论文](https://arxiv.org/html/2607.03691) | 固定模型，跨 35 个连续 Qwen Code 版本，在 50 个 SWE-bench Verified 任务上重复两次，共 3,500 次运行；分离 harness 演进与模型效果 | 已占据 stack 更新、版本时间线、质量/成本/工具调用回归 | 单一 harness 家族，无损害或 fleet 控制；复制包写明接收后开放，截止日不能当作公开数据 |
| *Governed Capability Evolution* (2026), arXiv:2604.08059，[论文](https://arxiv.org/html/2604.08059) | AI 组件升级的 candidate validation、sandbox、shadow、gated activation、monitoring 与 rollback；PyBullet/ROS2 案例 | 已占据 AI 组件生命周期中的分批验证、激活和回滚动作语义 | 论文承认是单系统而非 fleet-scale，但单纯放大到 fleet 不会产生新机制 |
| Microsoft Foundry (2026), *Monitoring across your agent fleet*，[官方文档](https://learn.microsoft.com/en-us/azure/foundry/control-plane/monitoring-across-fleet) | fleet inventory、health、error、cost、policy/compliance、异常与逐层 drill-down | fleet-level observability 与治理控制面已经是产品能力 | 没有可学习共因归因和序贯 containment；说明 dashboard 本身不构成贡献 |
| Kleinberg and Raghavan (2021), *Algorithmic Monoculture and Social Welfare*, PNAS, DOI [10.1073/pnas.2018340118](https://doi.org/10.1073/pnas.2018340118)；Bommasani et al. (2022), *Picking on the Same Person*, NeurIPS，[论文](https://proceedings.neurips.cc/paper_files/paper/2022/hash/17a234c91f746d9625a75cf8a8731ee2-Abstract-Conference.html) | 共同算法造成跨决策者的结果同质化与社会损失；组件共享可增加 outcome homogenization | 支持“共享技术栈具有系统后果”，也削弱把 monoculture 当作新概念的空间 | 没有 coding action、版本谱系或动态 containment |

上述近邻不是彼此独立的零散引用。它们形成一个覆盖链：IS 文献已经把共享脆弱性变成配置优化问题；coding-agent 文献已经观测共同失效并检验多样化；AI-control 文献已经学习低相关监控组合；生命周期研究已经给出 shadow、gate 与 rollback；产品控制面已经聚合 fleet 状态。候选只有证明共享 coding-agent stack 导出一种新的、不可还原的状态更新或行动选择，才可能穿过该覆盖链。

### 2.2 对 2017 年 ISR 全文的逐段机制回读

该文不能只被当作“软件多样性有益”的背景理论。引言首先把广泛使用同一软件与大规模共同受害联系起来，指出共享漏洞使攻击可沿网络扩散。文献回顾把软件多样性、网络传播与配置决策连起来。模型部分随后建立软件产品使用哪些漏洞的二元矩阵，并用产品之间的共享脆弱性定义多样程度。LP1 在软件数量与节点分配上最大化多样性，LP2 再把网络连接度纳入目标，使高连接节点获得更安全的配置。动态部分处理新增节点而非每次全局重算，传播实验使用扩展 SIS 与 epidemic threshold 评价韧性，后续又显式分析最少安装数量和采购成本约束。[本地全文第 1–3.5、5–7 节](../database_fulltext_all/03040_2017_software-diversity-for-improved-network-security-optimal-distribution-of-software-based-shared-v.md)

因此，本候选若把“软件产品”替换为“模型/harness/toolchain”，把“节点”替换为“agent/仓库”，把“共享漏洞”替换为“共同错误模式”，再把 LP 换成神经网络或 CMDP，其理论骨架、配置行动和安全—成本结果没有发生足够变化。编码代理的部分可观测轨迹和可回收补丁确实使问题更复杂，却只是新的状态特征和动作参数。复杂性增加不等于理论新增。

### 2.3 对系统性风险聚合全文的限用结论

Mezei 与 Sarlin 把系统性风险拆成相互关联的层级 segment，使用 Fuzzy Cognitive Map 表示节点间影响，再用 Choquet integral 聚合专家判断，以保留因素之间的非加性关系。[本地全文](../database_fulltext_all/00372_2016_aggregating-expert-knowledge-for-the-measurement-of-systemic-risk.md) 这篇论文可以支持两项测量纪律：fleet 风险不能由独立单元分数简单相加；直接影响与间接传播需要分开。它不能为候选提供独占算法。其边和权重源自监管专家，输出是系统风险度量，不是从 coding-agent 轨迹学习的行动策略。把 FCM、Choquet 或非加性 aggregation 换成可训练版本，等信息的 factor graph、Deep Sets 或图网络可以复制。强行把金融系统性风险翻译成 agent fleet 理论会使理论只负责命名。

## 3. 公开数据与可运行训练情境审查

### 3.1 现有资产到底能提供什么

| 公开资产 | 可运行内容 | 能否构造真实损害标签 | 能否识别 model×harness×task/risk 共因 | 决定性缺口 |
|---|---|---|---|---|
| Harness-Bench | 106 个离线任务、任务 manifest、runner、validator、多个 model/harness 组合 | 有最终 artifact、process 和 permission/security validator；论文汇总的 security 几乎没有阳性 | 可研究配置差异，不能直接估计共因概率 | 截止日检查官方仓库时未定位到论文所述全部 5,194 条原始轨迹语料；单次 cell；无 update episode |
| Scaffold Effect 补充材料 | 300 次固定任务配对运行，原始匿名日志与配置 | 主要是通过、成本、无动作和失败指纹，安全类别很少 | 能估计 harness fingerprint 的重复，不足以识别真实 correlated harm | 只有两个模型、三个 harness、每 cell 一次；预算与原生默认项仍可能影响比较 |
| N-Version Coding Agents | 生成的多语言实现、oracle、统计流程、固定种子；百万 case 可重生 | 共享 oracle 上的具体功能失效是真实可执行结果 | 对一个共同规范可精确测 co-failure | 单一 LIP 规范；没有仓库工具行动、更新时序、风险动作和 intervention trajectories |
| SABER，arXiv:2606.01317，[论文](https://arxiv.org/html/2606.01317)，[官方仓库](https://github.com/sssr-lab/saber) | 716 个 Docker 任务，包含嵌入式注入、风险自选和上下文警告 | 以命令、工具调用和状态差分区分安全完成、拒绝与失败，适合 harm oracle | 可跨模型重跑，但共享统一接口，不能分离 vendor harness | 没有 stack 更新、fleet cohort 或控制动作的反事实覆盖 |
| OS-Harm，arXiv:2506.14866，[论文](https://arxiv.org/html/2506.14866) | 150 个 computer-use 风险任务 | 有误用、注入与模型行为风险 | 不能直接识别 coding-agent stack 共因 | 研究对象不是仓库级 coding agent，只有辅助风险语料价值 |
| SecureVibeBench，ACL 2026，[正式论文](https://aclanthology.org/2026.acl-long.1107/)，[代码](https://github.com/iCSawyer/SecureVibeBench)，[数据](https://huggingface.co/datasets/iCSawyer/SecureVibeBench) | 41 个 C/C++ 项目的 105 个仓库级内存安全任务；功能测试、PoV 与 Semgrep | 可同时测任务成功、漏洞是否修复和新增风险 | 已有多个 agent/model 组合，但每组合一次且非完整可控 factorial | 没有公开的 stack 更新 episode、重复种子与 containment action；仓库中未定位到所有原始 agent 输出 |
| PatchEval-Verified，[官方仓库](https://github.com/bytedance/PatchEval) | 230 个 Docker 验证 CVE，含功能和漏洞测试，支持 Codex/OpenCode/Trae adapter | 可提供补丁安全回归和虚假完成 oracle | 可自行补跑 factorial | 官方资产不是完整 model×harness 重复矩阵；建议约 500 GB 磁盘与 16 核，批量生成成本高 |
| Don’t Blame the LLM | 35 个 sequential harness release、固定模型、重复两次 | 当前结果是质量与成本，不是损害 | 时间结构最接近 stack update | 复制包截止日尚未公开；单一 harness 家族；无干预动作 |

这些资产足以证明候选不是“无数据可做”。研究者可以在授权沙箱中重跑公开任务，形成新的交叉数据。它们又不足以直接训练所声称的 fleet policy，因为没有一个公开资产同时包含 component lineage、同步暴露 cohort、版本前后随机化、重复 stochastic rollouts、可执行 risk oracle、pause/diversify/shadow/withdraw action 和动作后的反事实结果。

### 3.2 若坚持训练，必须新建的 episode

一个可识别 episode 应在同一 task family 内抽取多个仓库任务，将它们随机分到共享 stack 版本和至少一个独立 stack，对每个 cell 运行多个固定但互不重叠的种子。研究者在预注册时点随机引入真实、可审计的组件更新，例如模型快照、harness commit、tool adapter 或权限配置，同时保留未更新 cohort。任务只在公开、许可或隔离容器中执行。危险命令通过状态差分和不可逆性 manifest 判定，安全补丁通过隐藏功能测试、PoV 和新增漏洞扫描判定，虚假完成通过声明—artifact—test 三者不一致判定。

每一 episode 必须保留 stack BOM、组件 commit/digest、provider 参数、系统提示 hash、工具权限图、任务与仓库 commit、完整事件轨迹、真实工具副作用、所有 oracle、动作时间和 censoring 原因。暂停或回滚之后仍要继续观测恢复、残留副作用和任务结果。若只保留终局 pass/fail，无法学习“何时尚来得及阻断共同失效”。若只在同一个失败首次出现之后复制更多 sibling task，样本选择已经由结果触发，也不能用于无偏概率估计。

### 3.3 数据可行性不是本次撤题原因

新建上述数据会昂贵，但可执行。可以从 SABER、SecureVibeBench 和 PatchEval 的确定性 oracle 中抽取 risk-rich tasks，再在 Harness-Bench 支持的 open harness 上形成受控 factorial。真正的难点是数据量：要识别低频共同损害、版本随机效应和策略反事实，预计需要数万条 sandbox agent rollout，而不是现有表格的行级拼接。即使这套数据成功生成，理论与动作仍落入通用动态因子模型、N-version allocation 和 release control 的交集。因此本次 NO-GO 不以“暂时没有数据”作为理由。

## 4. 理论候选逐一终审

| 理论候选 | 能真实指出的机制 | 若进入算法，最强中间状态或约束 | 预注册冲突情境 | 等信息通用替代能否复制 | 终审 |
|---|---|---|---|---|---|
| 软件多样性与 N-version theory | 共享实现来源使独立失效假设破裂；互补错误模式比单体准确率更重要 | 组件—单元 incidence、条件共同失效矩阵、多样性约束和 redundancy 组合 | 平均准确率最高但误差高度相关的 stack，与稍弱但低相关的 stack 冲突 | 能；而且 Temizkan et al. 与 Ron et al. 已直接计算配置、相关性与组合可靠性 | **不形成新增理论计算** |
| modularity 与 common-cause failure | 故障可由共同上游组件同时作用于多个后代；局部模块边界影响传播范围 | 版本化谱系超图、minimal cut set、component-specific latent shock | 一个上游更新解释多个不同任务的同步损害，而单元边际 hazard 很低 | 能；dynamic Bayesian network、noisy-OR factor graph、异质图 Transformer 均可原样表示 | **成为合理归纳偏置，但非独占机制** |
| portfolio 与 complementarity | 在风险预算下，应按联合收益和协方差配置异质执行者，而非逐项取最优 | stack 组合的联合尾险、互补矩阵和容量约束 | 单体最强 stack 的同向尾险高于混合 stack | 能；correlation-aware portfolio、N-version selection 和 ensemble selection 直接同构 | **普通组合优化** |
| normal accident 与 digital monoculture | 紧耦合、复杂交互和统一算法可把局部错误放大为系统损害 | 耦合强度、交互复杂度、共同暴露和传播图 | 低边际风险更新在高耦合依赖图上应被延迟，而高边际风险但松耦合任务可继续 | 能；依赖图上的 propagation model 与 CVaR-CMDP 即可执行；共同原因与复杂交互也不能混为一因 | **解释组织后果，不唯一决定动作** |
| organizational resilience 与 HRO | 高可靠数字组织通过对失败的持续关注、对简化的克制、运行敏感性、韧性和结构欠规范化来处理算法 frame 外事件 | 理论上最特殊的是“算法 frame 不足”信念和转入 mindful human operation | 自动系统高置信但证据来源同质时，应暂停并升级；低置信但独立证据一致时可继续 | 若自动化，普通不确定性/novelty gate 可复制；若把 mindful human layer做实，则研究对象变成人工升级、证据呈现和组织学习 | **自动化版本过薄，社会技术版本越界 C19/C3** |
| 系统性风险与非加性聚合 | 组成单元的风险不能独立相加，直接和间接关系均影响总体风险 | FCM、专家置信权重、Choquet 容量或可学习非加性 set function | 两个中等风险因素共同出现时超过单项之和 | 能；同信息 factor graph、Deep Sets 和图网络可拟合；原理论不提供 fleet action | **只宜用于测量纪律** |

### 4.1 HRO 不能被压缩成自动暂停规则

Salovaara、Lyytinen 与 Penttinen 的 MISQ 研究强调，数字操作具有精确、可编辑、可编程和可转移特性，但算法也受开发者既定 frame 限制。其经验机制不是让一个更复杂的算法独自变得 mindful，而是以分层社会技术安排把 scalable mindless digital core 与 mindful human operations 联结起来，使集体 mindfulness 从人员、知识和数字操作的关系中出现。[本地全文](../database_fulltext_all/12734_2019_high-reliability-in-digital-organizing-mindlessness-the-frame-problem-and-digital-operations1.md)

若候选只把“对失败保持敏感”转写成 hazard threshold，把“韧性”转写成 rollback，把“拒绝简化”转写成 ensemble，它会把组织理论压扁为已有控制模块。若忠实实现理论，则算法还要决定何时承认 frame insufficiency、把哪些相互冲突的日志和补丁证据交给哪类人员、人员如何更新共享理解，以及恢复后的知识如何反馈到数字核心。这已经不再是当前候选的 fleet 自动控制，而且与有限审核容量和人类监督研究交叉。HRO 因而能强化问题重要性，却不能拯救本候选的独立算法责任。

### 4.2 理论总门结论

所有候选理论都能支持“不要只优化单次任务边际成功率”这一共同命题，但没有一个理论产生无法由同信息 generic model 实施的方向运算。最接近特殊结构的是 component lineage 上的共因生成模型；它恰好是标准 factor graph 或 hierarchical survival model。最接近特殊行动的是 HRO 的转入 mindful human operation；它要求一个不同的社会技术研究设计。当前候选若保留自动化边界，就只剩 latent factor 加 portfolio/release policy。

## 5. 最强 steelman：CCF-Guard 训练与行动规格

本节故意不给弱版本。若连以下完整版本仍无法形成独占机制，则不能用一个简化分类器、模型路由器或发布规则重开候选。

### 5.1 研究问题与决策时点

最强研究问题是：在多个 coding-agent 工作单元共享可版本化组件、观测逐步到达且损害可能相关传播的条件下，能否从 component lineage 和执行前缀中及早推断 common-cause failure state，并选择针对组件和 cohort 的序贯 containment，使匹配任务成功与吞吐下的相关尾部损害低于边际风险控制、静态多样化、N-version 投票、监控器 ensemble 和通用发布策略？

决策在五类事件后触发：共享 stack 更新已进入候选阶段但尚未执行；首个 cohort 完成或出现状态差分；多个在途任务产生相似异常；隐藏 verifier 返回部分证据；暂停或回滚后的残留状态被重新观测。候选不得等所有任务完成后再做离线归因，因为那只能成为 incident analytics。

### 5.2 输入、输出与关键张量

以 batch 大小 (B)、历史窗 (T)、最多 (N) 个工作单元、(K) 个版本化组件、每条轨迹最多 (L) 个事件和 (R) 类损害为例，模型接收：

- 工作单元状态 $X\in\mathbb{R}^{B\times T\times N\times d_x}$，包括任务类型、仓库语言与依赖、权限需求、可逆性、当前 diff、测试证据、剩余预算和暴露时间。
- 组件状态 $C\in\mathbb{R}^{B\times T\times K\times d_c}$，包括 model snapshot、harness commit、系统提示 hash、tool adapter、权限配置、oracle 与部署连接器的版本特征及版本差分。
- 二部谱系矩阵 $M\in\{0,1\}^{B\times T\times N\times K}$，表示每个工作单元实际暴露于哪些精确组件版本。只记录“Claude”或“OpenHands”名称不够，必须固定 digest 与配置。
- 执行前缀 $E\in\mathbb{R}^{B\times T\times N\times L\times d_e}$，由思考外可观察事件、tool call、stdout/stderr、文件状态差分、测试、permission decision、claim 和恢复动作编码而成。
- 仓库与部署依赖图 $G\in\{0,1\}^{B\times N\times N}$，以及可见性、censoring、未启动和已终止 mask。

模型输出五项分布，而不是一个风险二分类：

1. 单元—风险—时点的 idiosyncratic hazard (u_{nrt})。
2. 组件—风险—时点的共同冲击后验 $q_{krt}=P(z_{krt}=1\mid H_t)$。
3. 未由已知谱系解释的低秩残余 dependence $\Sigma_t$，避免把未知共同规范盲区强行归到某一组件。
4. 每个参数化联合动作下，下一证据、单元损害、任务完成、残留副作用与成本的分布 $p(s_{t+1},Y_{t+1},c_{t+1}\mid s_t,a_t)$。
5. 在安全、任务、吞吐与成本约束下的联合动作策略 $\pi(a_t\mid s_t)$ 和不确定性。

### 5.3 前向结构

事件编码器先把每个工作单元的 trace prefix 压缩成时间表征。版本 diff 编码器把模型、harness、工具、权限和 oracle 的变化映射到组件节点。异质图网络随后在工作单元—组件二部图和仓库依赖图上进行 message passing。共因层使用离散时间 competing-risk factorization。最简形式为：

\[
P(Y_{nrt}=1\mid H_t)=1-(1-u_{nrt})
\prod_{k=1}^{K}(1-M_{nkt}q_{krt}),
\]

并以共享 (z_{krt}) 的联合采样产生 sibling units 的相关结果。为了不把所有相关性都归到已知组件，另设由 task-specification、repository family 和时间事件驱动的残余低秩因子。世界模型把 action-conditioned component exposure、任务状态、文件副作用和依赖传播作为下一状态预测。分布式 critic 估计每项动作下相关损害的 quantile，而 constrained actor 在成功、吞吐与成本下最小化 cohort harm 的 CVaR。

这已经是理论候选能够给出的最强前向承诺。谱系因子的价值在于，共同组件 posterior 可以被多个早期弱证据共同更新，并将证据传给尚未执行的同谱系单元。它与只预测每个单元边际风险的模型作出不同选择。然而，这一计算也正是通用 dynamic factor graph 的标准能力，后文将据此否决独占性。

### 5.4 训练样本、标签与监督来源

训练的基本样本不是单条轨迹，而是一个预先定义 exposure set 的版本化 episode：同一时间窗内若干 task/repo siblings，明确的 shared component lineage，随机化 stack assignment，多次 agent sampling，以及所有干预与后续状态。标签包括：

- (Y_{nrt})：由沙箱状态差分、权限不变量、危险命令执行、隐藏功能测试、PoV、新增漏洞扫描和声明—artifact 不一致共同产生的类型化损害标签。
- (S_{nt})：任务是否在封存测试下成功，而不是 agent 自报完成。
- (D_{nn'})：依赖边上是否出现由前一变更引发的可执行传播。
- (Z_{krt}) 的强标签：仅在研究者随机引入单一组件变化并保留并发对照时使用；其他共同原因保持潜变量，不能按“多个单元同错”反推为已知组件标签。
- action outcome：暂停、切换、影子重做、回滚、撤权和回收之后的真实恢复、残留损害、成功、延迟与成本。

现有 N-version、Harness-Bench 和 Scaffold Effect 数据可用于 trace/component encoder 的预训练或配对表示学习。SABER、SecureVibeBench 与 PatchEval 可提供 task-specific harm oracle。它们不能直接提供 policy label。策略监督必须来自随机或充分探索的沙箱干预，或来自已知行为概率且动作覆盖足够的离线数据；事后由研究者给“本应回滚”的标签会把规则偏好写进模型。

### 5.5 损失函数

钢人化总损失可以写为：

\[
\mathcal{L}=
\mathcal{L}_{\mathrm{surv}}
+\lambda_z\mathcal{L}_{\mathrm{ccf}}
+\lambda_s\mathcal{L}_{\mathrm{sibling}}
+\lambda_w\mathcal{L}_{\mathrm{world}}
+\lambda_{cal}\mathcal{L}_{\mathrm{cal}}
+\lambda_q\mathcal{L}_{\mathrm{offlineRL}}
+\lambda_{tail}\mathcal{L}_{\mathrm{CVaR}}
+\lambda_c\mathcal{L}_{\mathrm{constraint}}.
\]



$\mathcal{L}_{\mathrm{surv}}$ 是带 censoring 的 cause-specific discrete-time survival NLL；$\mathcal{L}_{\mathrm{ccf}}$ 是随机组件更新上的原因归属监督与潜变量边际似然；$\mathcal{L}_{\mathrm{sibling}}$ 让同一共享冲击下的共同误差结构与不同冲击区分；$\mathcal{L}_{\mathrm{world}}$ 预测 action-conditioned 状态差分、测试、损害和成本；$\mathcal{L}_{\mathrm{cal}}$ 使用 groupwise Brier/ECE 与 conformal coverage 约束；$\mathcal{L}_{\mathrm{offlineRL}}$ 可采用 distributional IQL/CQL 的 Bellman 与保守项；$\mathcal{L}_{\mathrm{CVaR}}$ 优化 cohort 最大损害和依赖加权传播尾部；最后一项用拉格朗日乘子保证最低任务成功、吞吐与最高人工/计算成本。只优化平均 incident reduction 会鼓励停止一切行动，必须否决。

### 5.6 推断时真正执行的动作

动作是参数化联合动作 $a_t=(\text{type},\text{component},\text{cohort},\text{alternate stack},\text{verification},\text{recovery scope})$：

1. `continue/pin`：让指定 cohort 继续，但把共享组件固定到已验证 digest。
2. `randomized canary`：只启动一个预注册随机 cohort，其他任务保持未暴露。
3. `diversify execution`：对指定任务使用组件谱系距离更大的独立 stack 重做，不以简单 top-1 模型选择替代。
4. `sealed shadow verification`：在独立权限域调用隐藏测试、PoV 或不同来源 verifier，生成信息而不直接投票提交。
5. `patch/rollback shared configuration`：应用已审计的 harness/tool/permission 配置变化或回到上一 digest。
6. `freeze lineage cut`：暂停所有暴露于高 posterior 组件的未完成后代，撤销未使用权限和排队工具调用。
7. `quarantine/withdraw/recover`：隔离已生成补丁，回收已合并但尚未部署的变更；对已执行副作用按 manifest 运行补偿或恢复，记录不可恢复状态。
8. `resume/release`：只有新证据满足约束才恢复 cohort。

这些必须由实验执行器在许可容器中落地并记录状态差分。若模型只输出动作建议而研究者手工选择，最终评价的是建议质量，不是 safe fleet action。与此同时，动作 2、5、6、7、8 与发布控制高度同构，动作 3 与 N-version/portfolio 同构，动作 4 与 verifier ensemble 同构。这一分解是候选后续 NO-GO 的关键证据。

### 5.7 训练、验证、测试与隐藏信息隔离

所有同一原始任务、同一仓库 commit、同一 CVE、同一自然语言 specification 的 siblings、语言改写、重复 seeds 和干预分支必须进入同一个 split。按轨迹行随机切分会把共同失败模式直接泄漏到测试集。正式测试至少包含五道互不替代的切分：

- repository/project/CVE holdout，阻止代码近重复和同一修复知识泄漏。
- task specification 与 risk-family holdout，检验未知共同盲区。
- 版本时间切分，只用截止时点前的 model、harness、tool 和权限版本训练，以后续版本测试。
- lineage-family holdout，至少留出一个 harness/provider/tool family，防止只记组件 ID。
- action-policy holdout，在新 cohort size、依赖拓扑和暴露率下测试，且保持损害抽样机制可解释。

隐藏测试、PoV、gold patch、vulnerability description 的答案性字段和部署恢复脚本不得进入 agent 或预测模型上下文。benchmark 的 public tests 与 hidden tests 必须有单独 hash manifest。训练数据 manifest 应记录源任务许可证、原始 commit、容器 digest、stack BOM、种子、action propensity、失败/超时/censoring、所有后处理版本。任何 provider 模型可能见过公共仓库的风险不能通过时间切分完全消除，需以 post-cutoff private transformations 或合成但行为等价的 hidden cases 做敏感性分析。

### 5.8 最强直接基线与等参数通用替代

所有模型共享完全相同的 (X,C,M,E,G)、训练 episode、动作集合、oracle、参数规模、推断 token、sandbox 数、wall-clock 和干预预算。至少比较：

- 单元独立 hazard 加固定阈值。
- component random-effect 的层级离散时间生存模型。
- dynamic Bayesian network/noisy-OR factor graph。
- 等参数 temporal heterogeneous graph Transformer，允许读取完整谱系和依赖图。
- 相同世界模型接通用 distributional CMDP，不使用理论命名的 factorization。
- Temizkan et al. 式多样性最大化与动态分配，在相同成本/容量下重实现。
- 低相关 portfolio 与 N-version 选择，含多数投票、best marginal、最远谱系和 correlation-aware 组合。
- Koran et al. 式高质量低相关 monitor ensemble。
- 固定 canary、risk-threshold canary 和 Governed Capability Evolution 式 lifecycle controller。
- oracle component label 的上界与不提供 lineage 的下界。

如果理论模型只超过独立单元 hazard，却不能超过同信息 factor graph 或 graph Transformer，结果只能证明“相关性重要”，不能证明理论驱动算法贡献。如果策略只超过固定 canary，却不能超过同世界模型 generic CMDP，结果只能证明状态依赖控制有用，不能形成本候选独立贡献。

### 5.9 机制干预与替代模型

必须预注册以下干预：在每个时点内随机打乱 component lineage，同时保持每个组件和工作单元的 degree 与 exposure count；将共享因子置零但保持单元 hazard；把模型、harness、tool 和 oracle 的角色标签折叠成无类型组件；对 component IDs 作未见置换；删除依赖图；中和 CVaR 只优化均值；将理论 factorization 换成等参数 free relation embedding；向 generic baseline 提供完全相同的谱系和冲击监督。

理论机制应在三类冲突案例表现出方向差异：高边际成功但共同错误后验高的 stack 对低相关弱 stack；只有一个早期异常但其后代暴露范围大的共享更新对多个相互独立的局部失败；低均值损害但高传播尾险的紧耦合 cohort 对较高均值但可隔离 cohort。若打乱谱系没有损害 OOD 表现，所谓共因层没有承担责任。若等参数 generic model 在这些冲突中复制选择和外部结果，理论独占主张应撤销。

### 5.10 外部结果与统计方案

主要安全结果应是匹配 task success 或以 success 为非劣约束时的 `correlated harmful units per exposure set`、至少 (m) 个单元共同受损的概率、cohort harm 的 95% CVaR、依赖加权传播规模、不可恢复副作用和虚假完成放行。任务结果是 hidden-test success、修复接受和有效完成数。成本结果是 wall-clock、token、模型/容器调用、暂停正常任务、人工升级和恢复开销。恢复结果是 detection-to-freeze、freeze-to-clean 与残留状态。

统计上以 episode 为 cluster，报告 stratified bootstrap 置信区间、matched-success risk difference、relative risk、tail quantile difference 和预注册的 multiple-testing correction。稀有伤害不使用普通 accuracy；报告分母、零事件区间和 calibration。对离线策略先做 propensity/coverage 检查、FQE 与 doubly robust sensitivity，再在沙箱中进行随机在线比较。没有这些设计时，策略价值会被行为策略和任务挑选混淆。

### 5.11 本地算力与训练工件

数据生成预计是主要成本。一个能覆盖 5–8 个 open model/backends、4–6 个 harness 版本、数百个 risk-rich task、多个 seeds、三类随机更新和数个干预分支的设计，量级约为一万至五万次容器化 agent rollout，可能需要一万至五万 container-hours、1–10 TB 压缩轨迹和显著 API 或本地推理成本。PatchEval 官方建议本身已接近 500 GB 磁盘与 16 CPU cores。此处只是规划量级，不是已经发生的资源消耗。

编码器和世界模型可控制在 100M–350M 可训练参数，预计使用 4 张 48 GB GPU 训练 2–5 天；离线策略和 bootstrap 另需约 1–2 天。应产出 trace encoder、component/version encoder、common-cause state model、world-model checkpoint、policy checkpoint、trajectory index、Docker images、Hydra/YAML configs、split manifests、oracle hashes、固定 seeds 和逐 episode action logs。再次强调，这些工件目前都不存在。

## 6. 终止性反证：钢人版本仍可被通用模型复制

### 6.1 同信息、等参数 generic 复制

CCF-Guard 的理论结构可以分成三步：从谱系和轨迹推断共享潜变量；预测联合后果；在约束下选择组合动作。dynamic factor graph 已经执行第一步，distributional world model 执行第二步，CMDP 执行第三步。noisy-OR 不是软件多样性理论独有的运算，component lineage 也不是理论模型才能读取的数据。等参数 temporal graph Transformer 可以把组件节点当作 relation-aware latent tokens，借助相同的 (Z) 监督和 sibling contrastive loss 学到相同聚合。再把同一 action mask、CVaR 和成本约束提供给 generic actor，两者的可行动作完全一致。

这个反证不依赖“神经网络原则上能逼近任何函数”的空泛说法。直接近邻已经在更具体的结构上实现关键部分：Temizkan et al. 用共享漏洞矩阵配置多样性；Ron et al. 以失败向量计算相关性与 N-version 组合；Koran et al. 同时优化 monitor quality 与低相关性；通用生命周期控制器执行 shadow、gate 和 rollback。候选增加的只是把这些状态放入同一时间图并让策略联动。联动需要工程和数据，但没有出现理论引出的不可替代计算。

### 6.2 coding-agent 删除检验

把工作单元改成 Kubernetes 批作业，把共享组件改成 base image、service mesh、library 和 policy，把损害改成数据破坏或服务回归，输入张量、共因 posterior、世界模型、CVaR 目标和八类动作均无需改变。把工作单元改成批量授信模型或内容审核模型也同样成立。只有 trace tokenizer、风险 oracle 和可执行恢复脚本随领域变化。

coding agent 的特性本可产生两类更专属的问题。一类是共同自然语言规范盲区经自主规划、代码编辑和工具调用转化成异质副作用；另一类是 agent 可在执行中生成新的验证与恢复行动。然而前者已经由 N-version 的 shared specification failure 展示，后者若只是调用 verifier、重做、暂停和回滚，仍落入现有控制动作。候选没有给出一种只有 coding agent 才有的、理论规定的 fleet 行动。因而它没有通过不可删除性门。

### 6.3 “fleet-level”不是独立能力

多单元联合结果比单单元风险更重要，但规模层级不是理论贡献。将单实例 compatibility 或 release controller 的状态扩成 set/graph，加入 cohort index 和 shared-component random effect，就能得到 fleet-level policy。除非组织层面产生新的信息分布、责任边界或协调行动，并且这些要素进入模型结构与真实干预，fleet 只是 batch dimension 加依赖边。本候选没有把这类社会技术机制做实；若做实为人类升级和跨团队责任协调，又会进入监督与审核分配研究。

## 7. 与既有候选的排他边界

| 既有候选 | 其研究对象与核心动作 | 本候选若成立时唯一可保留的边界 | 当前为什么仍越界或被挤压 |
|---|---|---|---|
| C14 执行者—验证者分离，[终审文件](01B_执行者验证者分离候选终审.md) | 对单个 patch/action 选择独立 verifier、收集证据、修订或提交；包含职责分离、验证组合和 learned verifier | 只能把 verifier 结果当作 fleet 共因状态的一种观测，不能以多 verifier、低相关 ensemble 或影子验证为主贡献 | Koran et al. 已直接实现相关性驱动的多样化 monitor；动作 4 不能支撑本候选新增 |
| C18 可靠发布行动，[终审文件](01K_可靠发布行动候选终审.md) | canary、observe、promote、pause、rollback、发布后恢复与成本权衡 | 只能研究多个同时运行 coding jobs 的共同原因，而不能把 stack release 生命周期当主对象 | 本候选动作 2、5、6、7、8 与 C18 及 Governed Capability Evolution 同构；加多个仓库不改变动作机制 |
| C19 有限审核容量下的安全审核分配，[终审文件](01M_有限审核容量下的安全审核分配候选终审.md) | 在人员容量、专长、疲劳与相关遗漏下决定谁审核、何时双审或延后 | 可以把人工升级当外生成本或末端动作，不能学习 reviewer matching、队列或组织注意分配 | 一旦用 HRO 的 mindful human layer 拯救理论，候选必须选择信息、人员与升级时机，立即进入 C19/C3 |
| C22 模型与 Scaffold 安全兼容，[同轮终审文件](01Q_模型与Scaffold安全兼容候选终审.md) | 单个部署的 model version×executable scaffold/harness version×task-risk compatibility；预测安全/任务/成本后果，生成最小 harness patch，执行 ship/dual-track/isolate/rollback | 只能保留多个单元共享供应链或控制面的**联合相关尾险**与共同原因识别；不能做单实例兼容预测、harness patch 或单实例发布 | 若动作为 patch shared harness 或 dual-track/rollback，则回到 C22；若动作为跨单元多样性配置，则回到 Temizkan/N-version/portfolio。剩余共因 posterior 又被 generic factor graph 吸收 |

C22 在同轮独立终审中也判定其最强结构可被 generic factor graph/AutoML 复制。不能把 C22 的单实例兼容性扩大到一批实例，或把 C18 的发布动作换成 fleet 术语后重新占位。四条边界同时执行后，本候选只剩“估计 joint correlation”这一状态变量，没有独立行动。

## 8. 候选条件审计矩阵

| 必要条件 | 证据 | 结论 |
|---|---|---|
| 实际损害明确 | 危险命令、安全/功能回归、虚假完成、错误部署和依赖传播均可由沙箱 oracle 测量 | 通过 |
| coding agent 是关键行动者 | agent 会自主规划、修改、调用工具，确实放大 shared stack 风险 | 问题情境通过，但删除检验失败 |
| 公开可运行基础 | SABER、SecureVibeBench、PatchEval、Harness-Bench、N-version 等可组合重跑 | 部分通过；必须新建 factorial update episodes |
| 有实质可训练工件 | 共因 world model 与序贯 policy 需要真实训练和本地计算 | 通过 |
| 不是二分类/简单路由 | 钢人版本含联合潜状态、动作后果与多目标控制 | 通过 |
| 理论改变内部计算 | component lineage/noisy-OR 能进入前向，CVaR 进入目标 | 表面通过，但 generic factor/CMDP 完全复制 |
| 相对直接近邻有独立新增能力 | 直接近邻分别占据多样性配置、coding-agent 共因、monitor ensemble 和 staged control | 不通过 |
| 可与 C14/C18/C19/C22 排他 | 排除 verifier、release、reviewer、compatibility 后只剩共因估计 | 不通过 |
| coding-agent 不可删除 | 替换为其他共享组件 fleet 后核心算法和动作不变 | 不通过 |
| 独立论文规模 | 新数据集和系统可能很大，但贡献落在已有模块联接 | 不通过 |

工作量、数据规模和工程难度都不能弥补最后四项失败。

## 9. 肖帅勇 ACAA/DSDL 写作逻辑逐主键映射

### 9.1 回读范围与使用原则

本次回读以本地两篇 ISR 主文为准：ACAA 为 *Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews*，DSDL 为 *A Theory-Driven Deep Learning Method for Voice Chat–Based Customer Response Prediction*。同时使用 [00W 主键 Manifest](00W_肖帅勇两篇ISR源行句段主键Manifest.md) 核对段落与语法句范围。这里学习的是每句的学术功能、引文责任和下一句接口，不复制原句，也不把“模仿肖论文”写成候选正式论文主张。

两篇主文共同要求先让读者看到结果后果和既有处理为什么不足，再引入能改变表示或目标的理论机制。ACAA 由平台情境推进到评论聚合缺口，再把 attention theory 分解到过程与粒度并逐一算法化。DSDL 由 voice-chat 决策的重要性和资源约束推进到 expectation、experience、disconfirmation 的不同信息责任，再给出相应表示与损失。候选不能先写一个 fleet dashboard，再用 monoculture 或 HRO 给模块命名；理论必须像两篇论文那样在“既有网络为什么处理错”之后产生明确计算。本终审正因为找不到该计算而撤题。

### 9.2 PRE—唯一新增命题—REL—分句 CIT—NEXT 映射

| 本文件论证单元 | 对照主键 | PRE，进入本段前读者已知什么 | 本段唯一新增命题 | REL，句间关系 | 分句 CIT 责任 | NEXT，交给下一段的问题 |
|---|---|---|---|---|---|---|
| `R0-P1` 风险情境 | `ACAA-I1-S01–S05`；`DSDL-I1-S01–S05` | coding agents 能同时修改多个仓库并调用真实工具 | 共享 stack 把单任务错误变成短时相关组织损害 | 情境规模递进到结果后果 | “共享 stack”由 Harness-Bench/Scaffold Effect 支持；“共同失效”由 N-version 实验支持；组织外推只表述为可能性 | 为什么单元风险分数不够 |
| `R0-P2` 直接空白审查 | `ACAA-I2-S01–S06`；`DSDL-I2-S01–S07` | 相关损害值得控制 | 多样化、monitor 和 staged control 已分别存在，空白不能写成“此前无人研究” | 现有做法列举后形成剩余问题 | 每个既有能力分别绑定 Temizkan、Ron、Koran、GCE，不用一条泛引文覆盖全部 | 剩余问题是否需要独特理论状态 |
| `R1-P1` 构念澄清 | `ACAA-L10-S01–S05`；`DSDL-L8-S01–S05` | 需要 fleet-level 结果 | correlation、common cause、task difficulty 和 incident frequency 必须分开 | 定义、反例、识别要求 | N-version 支持相关失效；统计识别判断是本终审方法论推论，不伪托原文 | 什么数据能识别原因 |
| `R2-P1` 近邻覆盖链 | `ACAA-L10-S01–S05`；`ACAA-L11-S01–S08` | 候选核心词已定义 | 近邻不是装饰性背景，而是已经占据状态、动作或结果 | 来源逐项比较后合成覆盖链 | 表中每行只让对应一手来源支持其对象、数据和动作；“形成覆盖链”标为本终审综合判断 | 是否仍有未覆盖机制 |
| `R2-P2` ISR 决定性挤压 | `DSDL-T1-S01–S08`；`DSDL-T2-S01–S07` | 软件多样性 ISR 是最接近 IS 工件 | 该文已把共享脆弱性、配置、动态重配、传播和成本联结成完整设计 | 从构念逐级走到算法行动与结果 | 五个分句分别由该文引言、3.1–3.5、5–7 节支持，不用摘要代替全文 | coding-agent 语境究竟新增什么 |
| `R2-P3` 系统性风险限用 | `ACAA-T5a-S01–S04`；`ACAA-T5b-S01–S06` | fleet 风险可能非加性 | FCM/Choquet 能约束聚合测量，不能独占序贯行动 | 理论能力与责任边界对照 | Mezei–Sarlin 支持 interconnected segments 与非加性聚合；generic 可复制是本终审算法判断 | 其他理论能否产生方向动作 |
| `R3-P1` 数据资产 | `ACAA-I4-S01–S06`；`DSDL-I5-S01–S04` | 识别需要 factorial episode | 多套公开 benchmark 能提供互补 oracle，但没有一套直接提供完整 fleet update action data | 资产逐项审查后归纳缺口 | 数量、组合和开放状态逐项绑定论文/官方仓库；未定位文件只写成截止日仓库审查，不写成永久不存在 | 能否严谨新建训练 episode |
| `R4-P1` 理论分解 | `ACAA-T5a-S01–S04`；`ACAA-T5b-S01–S06`；`ACAA-T6a-S01–S05`；`ACAA-T6b-S01–S04` | 候选有六个理论入口 | 每一理论必须分别给出被忽略机制、中间状态、冲突选择和 generic 反证 | 理论逐项并列，各自完成同一责任链 | Temizkan/Ron、Kleinberg/Bommasani、Salovaara、Mezei–Sarlin 分别支持相邻机制；终审不让理论跨行代言 | 哪一个理论能存活 |
| `R4-P2` HRO 责任 | `DSDL-T1-S01–S08`；`DSDL-T2-S01–S07`；`DSDL-T5-S01–S06` | HRO 是最有组织内涵的候选 | faithful HRO 需要 mindful human 与 mindless digital core 的分层关系，不能压成 risk gate | 原理论机制、算法化尝试、越界后果三步推进 | 前两句由 Salovaara et al. 全文支持；C19/C3 边界来自本项目审计，不冒充外部理论事实 | 自动边界下还剩什么 |
| `R5-P1` 研究问题 | `ACAA-I4-S01–S06`；`ACAA-I5-S01–S09`；`DSDL-I7-S01–S08` | 理论门尚未通过，但需钢人化 | 研究问题必须同时比较相关损害、任务成功、吞吐、成本与最强直接控制 | 机制桥接到可检验 RQ | 这里是设计主张，不用引用制造既成结果 | 模型究竟接收和输出什么 |
| `R5-P2` 工件总览 | `ACAA-M0-S01–S02`；`DSDL-M0-S01–S03` | 已知 RQ 和 episode 单位 | 工件由 trace/component 编码、谱系共因层、世界模型和受约束策略组成 | 总览先于细节 | 每个模块只陈述拟议结构，明确未训练 | 各状态怎样进前向 |
| `R5-P3` 前向与损失 | `ACAA-M1-S01–S05`；`ACAA-M2-S01–S08`；`DSDL-M2-S01–S08` | 已知输入输出 | 谱系共因通过 noisy-OR/latent shock 进入联合 hazard，相关尾险进入 actor 目标 | 张量到公式、公式到行动 | 公式为本审查 steelman，不引用为既有发现；factor 可复制将在下一节检验 | 理论结构是否不可替代 |
| `R6-P1` generic 反证 | `ACAA-L11-S01–S08`；`DSDL-T5-S01–S06` | 已有完整理论化模型 | 同信息 factor graph/graph Transformer/CMDP 能完成相同三步计算 | 逐步构造替代，而非笼统说万能逼近 | 直接近邻证明关键子计算已真实实现；“可组合复制”是本终审论证 | coding-agent 是否仍不可删除 |
| `R7-P1` 既有候选边界 | `ACAA-T6a-S01–S05`；`ACAA-T6b-S01–S04` | generic 反证已失败 | 排除 C14/C18/C19/C22 后，没有独立动作只留下联合状态估计 | 逐候选排除后回收 | 边界由四份项目终审文件支持，外部 Koran/GCE/Temizkan 只支持对应直接动作 | 是否仍够一篇独立论文 |
| `R11-P1` 终局贡献边界 | `DSDL-I8-S01–S11`；`DSDL-C1-S01–S04` | 问题、近邻、数据、工件和反证全部完成 | 大型 benchmark/fleet stress test 可作为共享基础设施，不能预支独立理论贡献 | 回收已证命题，不添加经验结果 | 明示未跑实验；只陈述设计用途和撤题理由 | 给出唯一终判 |

### 9.3 与肖老师句法责任的一致性结论

本文件没有沿用 ACAA/DSDL 的主题或句子，而是沿用三项严格责任。第一，一个段落只承担一个新增命题，已有情境、空白、理论机制、算法和贡献不在同一句堆叠。第二，每条引文只支持相邻的经验或理论分句，“可复制”“越界”和终局判断明确属于本审查推理。第三，算法细节只有在问题和近邻挤压已经建立后出现，而且每个理论构念都必须进入张量、损失或动作；无法进入时就撤销贡献，而不是留在引言装饰。

## 10. 引用与资产核验表

| ID | 核验元数据与一手入口 | 本文件使用的具体命题 | 回读位置或资产检查 | 状态 |
|---|---|---|---|---|
| V01 | Temizkan, O., Park, S., & Saydam, C. 2017. *Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities*. **Information Systems Research**. DOI [10.1287/isre.2017.0722](https://doi.org/10.1287/isre.2017.0722) | 软件单一化与共享漏洞造成系统相关风险；节点—漏洞矩阵、多样性、两类配置模型、动态分配、SIS 和成本 | 本地全文摘要、1、2.3、3.1–3.5、5–7 节逐段回读 | 已核验全文 |
| V02 | Mezei, J., & Sarlin, P. 2016. *Aggregating Expert Knowledge for the Measurement of Systemic Risk*. **Decision Support Systems**. DOI [10.1016/j.dss.2016.05.007](https://doi.org/10.1016/j.dss.2016.05.007) | 将系统性风险拆成互联 segment，用 FCM 和 Choquet 保留非加性关系 | 本地全文摘要、2.3–3.3、4–5 节 | 已核验全文；仅限测量责任 |
| V03 | Salovaara, A., Lyytinen, K., & Penttinen, E. 2019. *High Reliability in Digital Organizing: Mindlessness, the Frame Problem, and Digital Operations*. **MIS Quarterly**. DOI [10.25300/misq/2019/14577](https://doi.org/10.25300/misq/2019/14577) | 数字操作的 frame problem；mindful human 与 mindless digital operation 的分层社会技术关系 | 本地全文 Introduction、Theory、Digital Operations、Framework、Findings、Discussion | 已核验全文 |
| V04 | Ron, J., Baudry, B., & Monperrus, M. 2026. *N-Version Programming with Coding Agents*. arXiv:2606.20158，[正文](https://arxiv.org/html/2606.20158)，[代码](https://github.com/ASSERT-KTH/Knight-Leveson-Redux) | 69 个配置、48 个 admitted version、百万输入、429 对 115.36、跨轴共同失效、17,296 个 triples 与多数投票 | Abstract、II、III、IV、Threats；官方仓库目录与统计说明 | 已核验预印本与官方工件；未独立复现实验 |
| V05 | Koran, E., Yun, Y., Tetef, S., Arnav, B., & Bernabeu-Perez, P. 2026. *Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute*. arXiv:2605.15377，[正文](https://arxiv.org/html/2605.15377) | 12 个 GPT-4.1-mini monitor；低相关与单体质量共同决定 ensemble；APPS 到 BigCodeBench-Sabotage OOD | Abstract、Methods、Experiments、Results、Limitations | 已核验预印本 |
| V06 | Yao, Y., et al. 2026. *Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows*. arXiv:2605.27922，[正文](https://arxiv.org/html/2605.27922)，[仓库](https://github.com/Qihoo360/harness-bench) | 106 任务、6 configurable harness、8 model、5,194 trajectories；固定外部条件并保留原生 harness | Abstract、§3–§6、Appendix B；官方仓库任务和运行结构 | 已核验预印本与官方资产；全量 raw trajectories 的截止日可见性保守表述 |
| V07 | Vats, N., & Golev, O. 2026. *The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation*. arXiv:2607.22585，[正文](https://arxiv.org/html/2607.22585)，[补充材料](https://anonymous.4open.science/r/scaffold-effects-dl4c-supp/) | 3×2×50 配对运行、40× token/solved 差异、跨模型复现的 harness failure fingerprints | Abstract、Experimental Setup、Results、Limitations；补充材料 raw logs/configs | 已核验预印本与一手补充资产 |
| V08 | *Don’t Blame the Large Language Model: How Agent Harness Evolution Shapes Coding Agent Quality*. 2026. arXiv:2607.03691，[正文](https://arxiv.org/html/2607.03691) | 35 个 sequential Qwen Code release、50 个 SWE-bench Verified、每项两次，固定模型研究 harness 演进 | Abstract、Study Design、Results、Data Availability、Threats | 已核验预印本；复制包截止日尚未公开，未当公开训练数据 |
| V09 | *Governed Capability Evolution: Lifecycle-Time Compatibility Checking and Rollback for AI-Component-Based Systems, with Embodied Agents as Case Study*. 2026. arXiv:2604.08059，[正文](https://arxiv.org/html/2604.08059) | candidate validation、sandbox、shadow、gated activation、monitor、rollback；单系统限制 | Abstract、Architecture、Experiments、Limitations | 已核验预印本 |
| V10 | Microsoft. 2026. *Monitoring across your agent fleet*. [官方文档](https://learn.microsoft.com/en-us/azure/foundry/control-plane/monitoring-across-fleet) | fleet inventory、health、error、cost、policy/compliance、异常和 drill-down | 官方产品文档对应栏目 | 已核验官方资产；不作为学术理论证据 |
| V11 | Kleinberg, J., & Raghavan, M. 2021. *Algorithmic Monoculture and Social Welfare*. **PNAS**. DOI [10.1073/pnas.2018340118](https://doi.org/10.1073/pnas.2018340118) | 多决策者使用共同算法可以造成系统社会福利损失 | 正式全文模型与讨论 | 已核验正式论文 |
| V12 | Bommasani, R., et al. 2022. *Picking on the Same Person: Does Algorithmic Monoculture Lead to Outcome Homogenization?* **NeurIPS 2022**. [正式页面](https://proceedings.neurips.cc/paper_files/paper/2022/hash/17a234c91f746d9625a75cf8a8731ee2-Abstract-Conference.html) | 组件共享假说与 outcome homogenization | 正式 proceedings 摘要、正文实验与讨论入口 | 已核验正式论文 |
| V13 | Hu, Q., et al. 2026. *Saber: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces*. arXiv:2606.01317，[正文](https://arxiv.org/html/2606.01317)，[仓库](https://github.com/sssr-lab/saber) | 716 个 Docker 项目任务、13 个模型、三类风险来源、完整工具/状态差分、rule-first harm judge | Abstract、§4.1–4.4、§5、Appendices B–D；官方仓库 | 已核验预印本与官方工件 |
| V14 | *OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents*. 2025. arXiv:2506.14866，[正文](https://arxiv.org/html/2506.14866) | 150 个 computer-use 风险任务，可作邻域风险资产但不是 coding-agent fleet | Benchmark Construction、Taxonomy、Limitations | 已核验预印本 |
| V15 | *SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios*. 2026. **ACL 2026**. [正式论文](https://aclanthology.org/2026.acl-long.1107/)，[代码](https://github.com/iCSawyer/SecureVibeBench)，[数据](https://huggingface.co/datasets/iCSawyer/SecureVibeBench) | 41 个项目、105 个 C/C++ 内存安全任务；功能、PoV 与新增风险评价；多 agent/model | ACL 正式页、Method、Dataset、Evaluation；官方 GitHub/HF | 已核验正式论文与官方资产 |
| V16 | *PatchEval: A New Benchmark for Evaluating LLMs on Patching Real-World Vulnerabilities*. 2025/2026. arXiv:2511.11019，[正文](https://arxiv.org/html/2511.11019)，[官方仓库](https://github.com/bytedance/PatchEval) | 230 个 Docker-verified CVE、功能与漏洞测试、多个 agent adapter；本地批量运行资源要求 | 正文 Dataset/Evaluation/Reproducibility；官方 README 与 verified 更新说明 | 已核验预印本与官方资产 |
| V17 | Peng et al. 2026. *When Correct Is Not Safe: Front-Running Coding Agents with Vulnerable Yet Functional Patches*. **ACL 2026**. [正式论文](https://aclanthology.org/2026.acl-long.707/) | 功能通过不保证安全；12 个 agent-model 组合上的功能正确但脆弱 patch | ACL 正式页、Method、Experiments、Threats | 已核验正式论文；仅支持 false completion 风险，不支持 fleet policy |

所有 2026 年 arXiv 论文在本文件中均明确按预印本处理。论文报告的数值只用于界定近邻和数据规模，不当作本候选实验结果。对官方仓库“未定位到”的判断限定在 2026 年 8 月 16 日所见内容，不推断资产永远不存在。

## 11. 终局判定与唯一可复用价值

### 11.1 实质性 NO-GO 理由

第一，候选最核心的理论直觉和优化行动已经有直接 IS 前件。2017 年 ISR 不只说明多样性重要，而是已经把共享漏洞、系统传播、配置优化、动态重配和成本联结成工件。第二，coding-agent 专属的共同失效事实、多样性轴与 N-version 组合已被 2026 年直接工作覆盖。第三，影子验证、低相关 verifier、canary、pause 和 rollback 均有直接算法或生命周期近邻。第四，候选最强剩余状态是 component-lineage latent factor，最强剩余动作是 portfolio/release policy；等信息、等参数的通用模型能够复制。第五，排除 C14、C18、C19 和 C22 后没有独立行动。第六，删除 coding agent 后核心计算保持不变。

这些理由在实验尚未运行之前就可以成立，因为它们否定的是设计层的理论独占性和研究对象不可删除性，而不是预测模型能否得到较高分。即使未来 CCF-Guard 显著降低相关损害，若同世界模型 generic CMDP 也取得相同结果，该发现仍只能证明 fleet-level joint modeling 有用，不能证明本候选提出了独立的 theory-driven algorithm。

### 11.2 不占论文席位但可复用的资产

该方向可以作为已冻结论文的强外部测试层。具体可复用项包括版本化 stack BOM、exposure-set 数据结构、相关损害指标、component-lineage split、共享更新 stress test、incident-count 与 probability 的区分、N-version/Temizkan/Koran/GCE 基线，以及 canary 后的残留副作用记录。这些资产可以检验某篇主论文在多仓库和共享基础设施条件下是否仍然可靠，也可以形成公共 benchmark 或工程系统。它们不应被包装成第四个独立理论工件。

### 11.3 只有出现新事实才值得重新立项

未来只有同时出现以下三类新事实，才值得以一个新候选重新审查，而不是继续扩写本文：存在一种 coding-agent 专属的共同原因状态，它无法在其他软件 fleet 中保持同一语义；该状态从理论上强制导出一种不同于多样化、投票、monitor、canary、pause、rollback、withdraw 和人工升级的实际行动；在预注册的随机更新 episode 中，该结构相对同信息、等参数 factor graph/graph Transformer/CMDP 在未见 stack lineage 和 risk family 上产生可重复的 matched-success 风险优势。当前文献、数据与 steelman 均未提供这三项事实。

## 12. 机械核验记录

- **句键核验。** 2026 年 8 月 16 日使用脚本从 `00W_肖帅勇两篇ISR源行句段主键Manifest.md` 展开 649 个合法语法句键，再解析本文全部 35 处范围引用，共 25 个唯一范围。逐句展开后无不存在主键、反向范围或端点越界，`INVALID_COUNT=0`。
- **证据时态核验。** 全文搜索“结果表明”“我们发现”“实验表明”“已经训练”“显著提高/降低”等完成态。本文没有把候选结果写成已发生事实；第 11.1 节的“即使未来显著降低”为明确反事实条件。所有数值要么归属于已核验来源，要么在第 5.11 节明确标作规划量级。
- **链接核验。** 本文 9 个本地 Markdown 目标均可解析，包括三篇理论全文、00W 和 C14/C18/C19/C22 四份边界文件；外部技术来源均使用论文、正式 proceedings、官方文档、官方仓库或官方数据页。
- **公式、diff 与写入范围核验。** 三组 display-math 起止符数量相等，inline math 的美元符号成对；UTF-8 文件无 NUL 字节。本文共 379 行。`git diff --no-index --check -- NUL <target>` 没有 whitespace error，返回 1 仅表示新文件与空设备不同；Git 只另行提示工作区的 LF/CRLF 转换策略。`git status --short -- <target>` 只把本文件显示为新文件。共享工作区可能同时存在其他 agent 的改动，本终审的全部 `apply_patch` 写操作均只针对本文件。

**最终状态：NO-GO。**
