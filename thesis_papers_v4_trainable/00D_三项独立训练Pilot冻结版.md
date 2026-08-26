# 三项独立训练 Pilot 冻结版

## 一、冻结状态

本文件冻结的是三项先导研究，不是三篇已经成立的论文。三项分别学习人类所需上下文、修复位置动态后验和候选补丁正确性后验。它们拥有不同的观察单位、监督标签、训练 checkpoint、部署动作与撤题条件，因而有资格通过实验争取成为三篇。任何一项未通过预注册闸门，就替换该项，不用增加网络模块掩盖失败。

暂不采用“多文件编辑拓扑候选集生成”作为第二篇。它确实需要大模型微调和大量本地算力，但 Hoppity、Recoder、DEAR、KNOD、NTR、CodePlan、CodeStruct、CascadeFix 和 Mulpor 已经覆盖图编辑、结构解码、多位置修复、模板路由和仓库计划。若没有先导结果证明集合级拓扑多样性独立提高固定预算下的 resolved@K，训练七十亿参数模型只能证明工程昂贵，不能证明研究问题成立。

## 二、系列共同问题

共同问题是：在有限计算与上下文预算下，Coding Agent 如何把仓库中的潜在信息逐步转化为足以支持并验证软件行动的任务证据。

研究一讨论信息被送入 Agent 前的任务充分表征，研究二讨论修复行动形成前的顺序信息取得，研究三讨论候选行动形成后的顺序验证。三项可以在未来组合，但各自实证必须冻结其他阶段，不能把上一项 checkpoint 设为下一项获得增益的必要条件。

与目标博士论文的对应关系不是一条工程流水线。研究一建立共同的表征机制。研究二在修复前的代码观察情境中研究动态取得。研究三在修复后的验证情境中研究动态取得。后两项共享“信息取得有成本”这一张力，但潜在状态、可见信息、动作和终端损失完全不同。

## 三、Pilot 1：人工所需上下文的层次表征与预算合成

### 3.1 唯一问题

在固定 token 预算下，能否从 issue 与冻结仓库中学习一个跨文件、代码块和行区间一致的任务充分上下文分布，使模型选择人类判断解决任务前需要读取的信息，而不只是最终被 developer patch 修改的位置。

### 3.2 标签与数据责任

主监督只使用 ContextBench 的人工 gold spans。文件标签由 gold path 得到，语法块标签由固定 Tree-sitter 版本将 gold span 投影到最小包含块，行区间保留原始 span。语法块是本文适配层，不能写成官方额外标注。

未标注候选不能直接当作错误上下文，主训练采用 positive-unlabeled 或带置信权重的 listwise 学习。developer patch locus、固定 Agent 成功轨迹中的读取区间和 RepoExec dependency invocation 分别进入来源专属辅助头。三个来源不合并成一个 gold，也不用于改变人工主标签。训练、调参与测试按规范仓库族划分，最终外测排除仓库、issue、commit 与 patch 近重复。

### 3.3 张量与架构

固定 BM25、dense 与静态关系扩展产生高召回候选子图，并公开 candidate oracle recall。冻结本地代码编码器生成初始节点向量，训练二十至五十百万参数的关系图编码器和层次概率头。

文件层为多标签 Bernoulli：

\[
p_f=\sigma(a_f).
\]

块与行使用条件因子化：

\[
p_b=p_{f(b)}\sigma(a_{b\mid f}),\qquad
p_l=p_{b(l)}\sigma(a_{l\mid b}).
\]

父子一致性由参数化保证，不用三个互相冲突的独立 softmax 再加软惩罚。预算解码器选择嵌套集合，并为已选子节点加入最小父级路径与标题。

主损失为：

\[
\mathcal L_1=
\mathcal L_{PU}
+\lambda_h\mathcal L_{hier}
+\lambda_s\mathcal L_{source}
+\lambda_b\mathcal L_{budget}
+\lambda_c\mathcal L_{calibration}.
\]

其中 \(\mathcal L_{source}\) 只训练来源专属辅助头，不能把轨迹或 patch 标签写回人工主头。

### 3.4 独立工件与指标

发布候选生成 manifest、图 grammar、冻结编码器版本、层次 checkpoint、来源 heads、预算 calibrator 与确定性解码器。研究一独立报告文件、块、行区间检索，父子违反率与概率校准，人工上下文与 patch 或轨迹标签差异，固定 patcher 下的 resolved/token，以及去图、去条件因子化、去来源头、去预算训练和参数量匹配消融。

### 3.5 Pilot 规模与 Go/No-Go

先在仓库隔离的开发子集训练层级文本基线与最小图模型，约三十至八十 GPU 小时，另做数百次冻结 patcher 容器运行。

只有同时满足以下条件才进入全文：候选召回上限足够，三个粒度均超过 BM25、dense 与参数量匹配的层级文本模型，条件层次建模改善校准，且固定 patcher 的 resolved/token 至少在方向和仓库层面稳定改善。若人工 gold 与 patch locus 几乎等价，或图模型只提高 patch-location recall，本题停止。

## 四、Pilot 2：修复位置后验驱动的主动仓库信息取得

### 4.1 唯一问题

在固定代码观察预算内，能否显式维护文件、代码块和行区间的修复位置后验，并选择使预期 Bayes 定位风险下降最多的下一段代码或关系邻域，从而用更少上下文获得更准确的修改位置和更好的冻结 patcher 结果。

本题不是训练一个通用搜索 Agent，也不学习何时停止。每项任务使用固定步数或固定行数预算。动作只决定下一段读取什么，达到共同上限后结束。

### 4.2 标签与可见性

主标签由 developer diff 在 base snapshot 上确定的文件、最小语法块与修改行区间产生。SWE-smith 或 SWE-Synth 可提供规模训练，SWE-Gym 提供真实 issue 与可执行内测，时间冻结后的 SWE-rebench 新仓库承担主外测。合成 issue 可能由 patch 与测试材料生成，因此合成数据只能预训练，真实结论必须在自然 issue 上成立。

策略在时刻 \(t\) 只看 issue、任务无关索引摘要、已读取代码以及已执行动作。未读取代码的原文、gold patch、未来工具返回和隐藏测试不能进入状态。BM25 或 dense 索引分数可以作为预先可用的检索元数据，但完整代码 embedding 若由原文计算后直接输入策略，会泄露所谓尚未取得的信息。主实现因此只给未读节点路径、类型、图邻接、廉价词项统计和固定检索器名次；动作执行后才暴露代码内容表示。

### 4.3 Belief 架构

仓库的廉价元数据图由关系编码器得到候选先验。已读内容通过递归状态更新器形成 \(h_t\)。层次后验写为：

\[
b_t(f),\qquad b_t(b\mid f),\qquad b_t(l\mid b),
\]

并由乘积得到叶节点概率。网络同时输出未读动作的结果分布与成本分位数。执行动作 \(a_t\) 后，读取结果 \(o_t\) 经 gated update 得到 \(b_{t+1}\)。

定位风险可定义为 gold edit set 的层次 log loss、预算内漏定位损失或其加权组合：

\[
R(b_t)=
\omega_f R_f(b_t)+\omega_b R_b(b_t)+\omega_l R_l(b_t).
\]

下一动作的价值是：

\[
VOI(a\mid b_t)=
R(b_t)-\mathbb E_{o\sim p_\theta(o\mid b_t,a)}R(b_{t+1})
-\lambda c(a).
\]

### 4.4 训练

先用随机、BM25、dense 与图 frontier 行为政策收集固定预算观察轨迹。每个前缀都能从 gold edit set 计算当前风险，但单条行为轨迹的下一动作不能当作唯一最优标签。

联合损失为：

\[
\mathcal L_2=
\mathcal L_{hier\text{-}NLL}
+\lambda_B\mathcal L_{Brier}
+\lambda_o\mathcal L_{obs}
+\lambda_c\mathcal L_{cost}
+\lambda_V\mathcal L_{VOI}
+\lambda_\pi\mathcal L_{policy}.
\]

其中 \(\mathcal L_{VOI}\) 用可枚举的小候选池 hindsight risk reduction 或短视 oracle 监督价值头，\(\mathcal L_{policy}\) 先做 oracle imitation，再在固定离线轨迹上使用保守 actor-critic。不能用在线 PPO 把基础模型、提示词和工具链同时改成不可识别的整体。

### 4.5 独立工件与指标

发布元数据图构建器、observation schema、层次 belief checkpoint、outcome/cost heads、固定预算 policy 和校准统计。主结果包括每步后验 log loss 与 Brier、gold edit recall、首次命中延迟、每步边际风险下降、重复读取率、固定行预算下的定位质量、冻结 patcher resolved/token，以及 belief 干预和去 belief、去 outcome model、去图、去 VOI、静态 retriever 等消融。

### 4.6 Pilot 规模与 Go/No-Go

先取三百至五百个任务，产生约五千个 observation prefixes，在一张二十四 GB GPU 上训练最小 belief model，预计三十至八十 GPU 小时。主比较必须包括 BM25、dense、RepoGraph 或 LocAgent 式静态方法、GraphLocator 式邻域扩展、current-rank greedy、cheapest-first 与随机 frontier。

只有当 VOI 策略在真实仓库上同时改善后验校准、相同预算的修改位置召回和冻结 patcher 结果，且增益不依赖合成 issue 模板时才继续。若选择退化为当前最高 rank、最便宜动作，或静态检索器同预算持平，本题停止。若所谓 belief 的中间指标不领先最终 gold 命中，本题也停止，不能把 belief 只当政策网络的不可解释 hidden state。

## 五、Pilot 3：部分候选—测试矩阵上的成本敏感主动验证

### 5.1 唯一问题

给定冻结候选补丁集和任务可见测试池，在只观察部分 candidate×test 结果时，如何更新候选正确性信念并联合决定下一测试组、停止、选择某一补丁或放弃全部候选，使错误发布、漏选与验证成本的总风险最小。

### 5.2 标签与矩阵构造

固定至少两个本地候选生成器，每任务生成 \(K\) 个候选。固定测试生成器只看 issue 与 buggy repository，生成 \(M\) 个任务可见 reproduction 或 regression test groups。每个候选与测试组在容器中真实执行，记录 pass、fail、error、timeout、wall-clock 与资源。候选正确性由独立 official evaluator 得到。gold patch 与隐藏测试只产生离线标签，不能进入 test bank、模型输入或策略历史。

训练、调参、校准和测试按仓库族隔离，并单列 candidate-generator holdout 与 test-generator holdout。候选来源标识不能作为主输入，以免模型直接学习哪个生成器更强。

### 5.3 World model 与终端风险

使用 candidate-test 二部关系网络。候选与测试节点由冻结编码器生成初始表示，已观测边带 outcome 与 cost，未观测边使用 mask。共享潜变量处理同一测试在多个候选上的相关结果：

\[
p(y_{1:K,m}\mid s)=
\sum_r\pi_r(s,m)\prod_k p(y_{km}\mid r,s).
\]

网络包含候选正确性 head、集合 any-correct head、masked outcome head 和成本分位数 head。终端风险写为：

\[
L_{stop}(s)=
\min\left\{
c_A P(\exists k:z_k=1\mid s),
\min_k c_W[1-P(z_k=1\mid s)]
\right\},
\]

第一项对应放弃但池内存在正确补丁，第二项对应选择错误补丁。损失比 \(c_A/c_W\) 预注册并做敏感度，不从测试集择优。

### 5.4 损失与 EVI

对完整矩阵随机 mask，形成大量合法部分状态：

\[
\mathcal L_3=
\mathcal L_{candidate\text{-}Brier}
+\lambda_A\mathcal L_{any\text{-}correct}
+\lambda_O\mathcal L_{masked\text{-}NLL}
+\lambda_C\mathcal L_{pinball}
+\lambda_R\mathcal L_{rank}
+\lambda_K\mathcal L_{calibration}.
\]

下一测试组的价值是：

\[
EVI(m\mid s)=
L_{stop}(s)-
\mathbb E_{y_{1:K,m}}L_{stop}(s\cup y_{1:K,m})
-\lambda c_m.
\]

当所有 EVI 非正、预算耗尽或风险低于阈值时停止。EVI planner 是确定性解码器，不再叠加一套无必要的在线 RL。

### 5.5 独立工件与指标

发布完整矩阵数据、candidate/test schema、world-model checkpoint、校准器、损失比与 deterministic EVI planner。主结果包括 masked outcome NLL、候选与 any-correct 校准、风险—覆盖曲线、wrong-release、相同风险下总容器成本与尾延迟、相同成本下 Bayes regret、相对最优固定 batch 的 adaptivity gap，以及 generator-holdout 与时间外测。

### 5.6 Pilot 规模与 Go/No-Go

先做一百个 repo-disjoint 任务、两个候选生成器、每任务至少十六个候选与十个测试组，并对测试稳定性重复三次。主矩阵至少包含一万六千个候选—测试格子，另做候选 official evaluation。

至少五十个任务必须同时含正确与错误候选，至少七成测试稳定，且同一测试不能对几乎所有候选输出常量。模型必须在 generator-holdout 上胜过 static verifier，并在等总成本和等 wall-clock 两种口径下胜过 random、cheapest、coverage、entropy、B4 fixed-budget 与最优静态 batch。若没有跨仓库 adaptivity gap，本题停止或退化为一篇静态验证论文。

## 六、三项不可混淆的边界

| 项目 | Pilot 1 | Pilot 2 | Pilot 3 |
|---|---|---|---|
| 潜在目标 | 人类认为任务所需的上下文 | 最终 developer edit location | 候选补丁语义正确性 |
| 主标签 | 人工 needed-context spans | gold diff file/block/line | official evaluator resolved |
| 状态 | 静态 issue 与仓库候选 | 已读代码与层次位置后验 | 部分 candidate×test outcomes |
| 动作 | 一次性预算上下文包 | 下一段代码或关系邻域 | 下一测试组或 select/abstain |
| checkpoint | 层次证据表征器 | belief world model 与取得 policy | 验证 world model |
| 主要成本 | context tokens | 观察行数与检索延迟 | 容器运行与尾延迟 |
| 不得声称 | gold 等于必要性 | patch locus 等于所需上下文 | visible tests 等于语义正确性 |

Pilot 1 与 Pilot 2 不是同一个检索器的静态和动态版。前者以人类 needed-context 为测量对象并输出最终上下文包，后者以 developer edit location 为状态目标并研究顺序观察对后验风险的影响。二者必须独立训练和独立评价，Pilot 2 不得把 Pilot 1 checkpoint 设为必要输入。

Pilot 2 与 Pilot 3 都使用信息价值，但一个减少修改位置不确定性，另一个减少候选正确性不确定性。二者的 observation、cost、terminal risk 和 benchmark labels 不同，不能共享一个 policy head 或把同一损失换变量名。

## 七、与肖文写法和方法硬度的对应

后续每篇都必须完成五层证据链。第一，理论构念导出普通 ranker 或 verifier 无法自然表达的结构。第二，该结构成为可命名和可观察的中间张量。第三，联合损失同时约束中间张量和最终行动目标。第四，中间张量用校准、探针、交换或干预单独检验。第五，最终行动结果、成本、解释和消融形成非替代证据。

Pilot 1 的专门张量是条件层次概率，Pilot 2 是随观察更新的层次修复位置 belief 与风险下降，Pilot 3 是部分验证矩阵上的候选正确信念与相关 outcome 分布。三者都必须通过本地训练得到，删除 checkpoint 后无法由提示词等价替代。真正的硬度来自这些中间对象和训练约束，而不是参数量本身。

## 八、启动顺序

实际研发按 Pilot 3、Pilot 1、Pilot 2 排序。Pilot 3 的标签最硬，矩阵是否有可利用信息最快可证伪。Pilot 1 的人工标签责任最清楚，规模较小。Pilot 2 的近邻最多，且“未观察代码”的可见性边界最容易被破坏，必须最后启动。

在三个 Pilot 通过前，不再撰写三篇完整正文，只撰写事实台账、可复算数据协议、基线实现与撤题判据。通过后再为每篇逐段写作，并在每个实质段完成后立即回读 ACAA 与 DSDL 的对应原文位置、逐句功能和引用责任。
