# 论文三逐段双 ISR 回读记录：最终唯一句表

## 使用规则

本记录只对应当前的 03_部分验证矩阵上的成本敏感主动补丁验证.md。每个 P 段在本轮改写完成后，均重新回读本地 ACAA 与 DSDL 原文；下列“当前句表”是该 P 段唯一有效版本，旧版句表、旧公式和旧资源数均已删除。原文行号以 database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md（ACAA）和 database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md（DSDL）的当前物理行为准；空行不被描述为内容行。

## P01　摘要

**双源定位。** 改写完成后重读 ACAA 第 29 行完整摘要及第 53–55 行“指标—研究问题—双构件—结果”链；重读 DSDL 第 27 行完整摘要及第 51–53 行“直接标签困难—集中问题—联合方法—双重证据”链。

**ACAA 逐句或句群功能。** 第 29 行先承认已有研究，再指出测量粒度造成的预测缺口；随后提出中间对象、分解指标、映射机制，最后以最终预测和中间表征两类证据闭环。第 53–55 行把多个指标收束到一个 RQ 和两个分责构件，而非拆成多项松散研究。

**DSDL 逐句或句群功能。** 第 27 行按业务机会、具体任务、理论对象、学习困难、方法与两类结果推进。第 51–53 行特别强调：中间 gold 缺失时不能靠命名构念成立，而要让联合学习对象和最终/中间评价共同承担责任。

**新段逐句功能（唯一当前句表）。** S1 建立多候选供给与隐藏评测不可见的验证困难。S2 承认测试生成、批量执行重排、完整矩阵选择和静态 verifier 已有，并定位部分结果下的剩余问题。S3 给出唯一决策问题及四类行动。S4 固定三次运行、20 类计数、base 准入与不得 future-filter。S5 指定统一 joint、主 \(K=8,Q\le4\) 的至多 1,024 状态 exact filter/exact hypothetical reweighting，以及仅供20–50项 \(K=16\) 敏感性的门控 SMC，并删除独立 posterior。S6 用 terminal loss 和三次整列双成本定义 planner。S7 给 outcome 解封前纯计算门、第三候选/测试 holdout、四项科学门及撤题出口。

**引用责任。** 摘要不堆文献；近邻责任在 P03，joint/filter、20 类观察、损失和 Pilot 门均是本文待验证设计，不能写成已有绩效。

**回读后的修改处理。** 按 ACAA 的“一个问题—分责构件—双重证据”收束摘要；按 DSDL 的中间量责任，把原来彼此不相容的 posterior/outcome 网络改成同一 joint 的 Bayes 条件化，并把旧的 stable-cell 筛选替换为 base-admissible 计数列及 generator holdout。主规模再次订正为可直接审计的 \(K=8,Q\le4\) exact state；Monte Carlo 只承担 predictive outcome 积分，\(K=16\) 不再混入主结论。

## P02　引言：从多候选供给转向验证配置

**双源定位。** 改写后重读 ACAA 第 39–43 行和 DSDL 第 35–41 行。

**ACAA 逐句或句群功能。** 第 39 行从信息渠道逐级落到预测和运营价值；第 41 行先承认“全量输入”的直觉价值，再解释数据与模型为何失配；第 43 行才提出值得学习的中间对象。

**DSDL 逐句或句群功能。** 第 35–39 行从数字化交互缩到主动邀请及有限坐席资源矛盾；第 41 行把输入可得性和运行能力成本并列为任务约束。

**新段逐句功能（唯一当前句表）。** S1 固定真实仓库和可执行 benchmark 情境。S2 把多候选供给的收益转为有限验证预算瓶颈。S3 区分部署不可见 official evaluator 与不完备的任务可见测试。S4 把静态排序改写为验证成本、错发和漏选的联合信息取得。S5 用“下一单位计算能否改变决定”给出操作性价值判据。

**引用责任。** SWE-bench/SWE-Gym 只负责真实仓库可执行评价情境；Otter 只负责 issue-only 测试生成能力。生成测试的诊断性与重复模式须由 Pilot 测量。

**回读后的修改处理。** 保留自然做法的价值后才指出失败条件，没有提前宣讲模型；与两篇 ISR 一样，先形成可观察的运营矛盾，再把算法推迟到研究问题之后。

## P03　引言：直接近邻与剩余边界

**双源定位。** 本轮近邻补充后立即重读 ACAA 第 41、43、45、47、85、87 行和 DSDL 第 43、75、77、79 行。

**ACAA 逐句或句群功能。** 第 41 行逐项承认已有数据与模型能做什么，再从粒度和无差异处理限定不足；第 45 行承认既有质量指标的诊断价值后，才用偏好异质性和冲突结果压缩其适用边界；第 85、87 行把宽泛缺口压成可操作差异，并说明现成机制为何与新要求不相容。

**DSDL 逐句或句群功能。** 第 43 行列出真实强近邻并说明输入条件为何不能直接迁移；第 75 行只保留两项缺口；第 77、79 行按“不同于何者—怎样不同—产生何种中间量”定位新方法。

**新段逐句功能（唯一当前句表）。** S1 过渡到已有环节。S2 分配 Otter/e-Otter++、CodeT、B4 的责任。S3 加入 Agentless、SWE-RL、R2E-Gym 三个直接批量执行选择近邻。S4 明确三者已覆盖“多候选—生成测试—执行选择”，差异仅在静态批次与部分列行动。S5 定位 TC-Bench、SWE-Gym、EGSS、EET。S6 把 FRTP、Opad、Iter-T、MPTPS 与两百万补丁 regression-testing 研究纳入传统 APR 边界。S7 说明传统近邻的动作粒度、状态与目标为何不等价。S8 引入 ISSTA 2026 实证研究及两个 2026 预印本。S9 将前两项限定为立题测量边界，并把 Calibrate-Then-Act 定为最接近的规范边界而非确认性基线。S10 把唯一增量限定为概率闭合 joint filter 下的成本化下一列。S11 对自然组合给撤题规则，并明确仅覆盖动机或不同动作粒度时不夸大差异。

**引用责任。** Agentless 为 FSE 2025 正式论文；SWE-RL 为 NeurIPS 2025；R2E-Gym 为 COLM 2025，不能误写为 CCF A。FRTP、Opad、Iter-T、MPTPS 与 Lou et al. 分别承担历史失败优先、生成测试过滤、反例迭代、修改点优先/抽样和回归测试选择/优先的边界。Lin et al. 是 ISSTA 2026 accepted research paper；Calibrate-Then-Act 与 Rethinking 均只按 2026 arXiv 预印本引用，不能伪装成正式录用论文。

**回读后的修改处理。** 依照两篇 ISR“先完整保留强近邻责任，再说明输入或决策时点不等价”的写法，本轮把 MPTPS、TOSEM 2024、ISSTA 2026 和两个 2026 预印本放回正文逐项分责；没有把它们扩成主实验包袱，而是区分覆盖、差异和撤题条件，并把新颖性继续压缩到可见状态、Bayes 更新和行动规则的联合差异。

## P04　理论基础：序贯信息取得映射

**双源定位。** 改写后重读 ACAA 第 47–51 行、DSDL 第 45–51 行，并核对 Moore and Whinston（1986）第 70–106 行和 Dos Santos and Mookerjee（1993）第 45–63、101–139 行。

**ACAA 逐句或句群功能。** 第 47 行先定过程，再解释有限注意为何改变对象；第 49 行分粒度；第 51 行才把各粒度连接到理论要求和可实现指标。

**DSDL 逐句或句群功能。** 第 45 行给 expectation–experience–satisfaction 关系；第 47–49 行把不可见对象翻成学习责任；第 51 行承认无中间 gold 的识别边界。

**新段逐句功能（唯一当前句表）。** S1 给状态、实验、信号、成本、最终决定及价值判据。S2 把五项映射到候选正确性、三次整列行动、四类计数和 select/abstain。S3 明确保留规范结构但放弃无噪假设。S4 用第二篇决策理论区分冻结决策对象和可优化取得控制。S5 阻断“测试改变真实正确性”的因果误读。

**引用责任。** 两篇决策理论只承担规范结构，不替噪声模型或候选相关性背书；重复不稳定与相关性由本文矩阵测量。

**回读后的修改处理。** 将信号单位从单次四类结果改成每候选四类三次计数的联合列，保持理论映射与实际 action 完全一致。

## P05　理论基础：三个可训练约束

**双源定位。** 改写后重读 ACAA 第 100–118 行和 DSDL 第 130–156 行。

**ACAA 逐句或句群功能。** 第 100 行先区分理论阶段；第 102/104、106/108、110/112、114/116 行反复采用“理论要求—普通机制为何不足—专门机制”；第 118 行汇总一一映射。

**DSDL 逐句或句群功能。** 第 130–144 行把偏好变成矩阵；第 148–152 行从角色交错关系推出 cross-view 连接；第 156 行把中间对象落为可单独分析的张量。

**新段逐句功能（唯一当前句表）。** S1 宣布三个共同必要条件。S2 要求条件信息必须从同一 joint 解析。S3 要求用共享正确性状态和列残余表达整列相关。S4 用真实状态定义 select/abstain 损失。S5 收束为主 \(K=8\) exact Bayes 条件化与 static batch 的唯一 RQ。S6 给 prequential likelihood、联合校准和最终风险三层证据。S7 把成本限定为行动约束而非新构念。

**引用责任。** 三项要求是理论结构与部署动作共同导出的设计命题；是否成立分别由 prequential prediction、校准/coherence 和 realized loss 负责。

**回读后的修改处理。** 本轮改写后立即重读 ACAA 49、53 与 DSDL 47–51；同一静态 joint 的主问题现明确为主规模 exact Bayes 条件化，SMC 不再混入研究问题主张。

## P06　方法：实例、可见性和合法动作

**双源定位。** 改写后重读 ACAA 第 134、139、141–161 行和 DSDL 第 105、109、113、118–120 行。

**ACAA 逐句或句群功能。** 第 134 行先固定 hotel-month、时间窗、输入情形与过滤；第 139 行说明模态对齐；第 141–161 行先定义 padding/mask，再分别说明它排除什么。

**DSDL 逐句或句群功能。** 第 105 行固定案例和结果；第 109 行给数据到输出流程；第 113 行给入组、标签与双轨；第 118–120 行给自然片段、过滤、截断和 mask。

**新段逐句功能（唯一当前句表）。** S1 定义 \(x,C,T,s\)。S2 锁定候选与测试 pipeline 的允许/禁止输入。S3 要求 manifest 和哈希审计。S4 定义三次 \(3K\) 动作、组内完整执行和四类固定优先序。S5 将基础设施故障移出候选四类并另账。S6 定义 20 类 cell 计数、整列和资源。S7 定义合法整列历史并隔离 official \(z\)。S8 冻结主 \(K=8,M=10\) 的非 gold 稳定哈希裁剪及不足处理；\(M=5\) 只作冻结下采样，\(K=16\) 仅在20–50项预抽敏感性任务中由同一 A/B pipeline 的第二 seed block 扩成且全部 outcome 前冻结。

**引用责任。** 这是本文 schema；两篇 ISR 只提供“单位—对齐—mask”写作逻辑。可见性、group status 和 20 类计数由 manifest、容器和审计代码承担。

**回读后的修改处理。** 补齐 resolving patch、official lists 和网络访问禁令；删除 padding 候选和模糊 group outcome；将每格定义为三次计数，并固定 timeout/error/fail/pass 汇总顺序，使训练标签和部署观察一致；依照冻结单位与 mask 的逻辑，删除超出已生成主池的 \(K=32,M=20\) 伪敏感性。

## P07　方法：静态二部 factor encoder

**双源定位。** 改写后重读 ACAA 第 126、130 行和 DSDL 第 148–156 行。

**ACAA 逐句或句群功能。** 第 126 行由四项理论要求推出两个机制；第 130 行按冻结表征、流式编码、专门机制、最终/中间输出排列。

**DSDL 逐句或句群功能。** 第 148–152 行先由双模态与角色交错决定连接，再说明 cross-view 与普通 self-attention 的区别；第 156 行把输出送入下一理论量。

**新段逐句功能（唯一当前句表）。** S1 定义冻结语义表示和无 gold 静态特征。S2 删除 generator shortcut 并实施双置换。S3 把二部图限定为静态 prior/likelihood factors，观察只把式（3）Bayes 因子累加到状态 log weight。S4 唯一冻结主架构及 \(Q\in\{1,2,4\},R\in\{1,2,4\}\) 网格。S5 要求 outcome 前由构建脚本证明 encoder 冻结、分模块输出 relation/\(\rho/\pi/\omega/\xi\)/cost trainable count，并把总可训练参数锁在5–20M。S6 列五类参数量/机制对照。S7 明确主规模由 exact filter 条件化且主要工件不含 amortized history posterior。

**引用责任。** encoder revision、层数和参数均由本文签名配置负责；“二部图”不构成新颖性，必要性由同参数对照检验。

**回读后的修改处理。** 本轮改写后立即重读 ACAA 126、130 与 DSDL 148–156；把“粒子权重”改成与主 exact 实现一致的“全状态 log weight”，同时仍把网络责任严格限定为静态 factors。

## P08　方法：统一正确性 prior 与解析风险概率

**双源定位。** 改写后重读 ACAA 第 169–210 行和 DSDL 第 156–189 行。

**ACAA 逐句或句群功能。** 第 171–208 行逐式定义表征、权重及每个项的责任，第 210 行才形成综合表示；不是先给总分再补故事。

**DSDL 逐句或句群功能。** 第 156–185 行从 expectation/experience 到 dynamic disconfirmation 和 cumulative satisfaction 逐步派生；第 187–189 行明确无直接标签时的监督依据和个体异质性约束。

**新段逐句功能（唯一当前句表）。** S1 说明单候选、any-correct 和列预测必须共享对象。F1 式（1）定义静态 mixture-Bernoulli prior。S2 解释 \(q\) 与逐候选非 one-hot 标签。S3 给 \(\rho=\mathrm{softmax}\)、\(\pi=\mathrm{sigmoid}\) 的正规化等变参数化。S4 冻结 \(Q\le4\) 的证据。S5 说明历史只由式（3）Bayes 更新。F2 式（2）从 \(w_t(q,z)\) 解析 \(p_k,p_A\)。S6 删除自由 any/history heads。S7 用 \(Q2^K\le1{,}024\) 证明主 \(K=8\) 可直接作全状态 log-space exact filter与假设结果 exact reweighting，并把 SMC 降为20–50项 \(K=16\) 门控敏感性。S8 保留多种子 collapse 诊断并规定 mixture 必要性的 Brier、协同校准和持出似然证据。

**引用责任。** mixture 是可检验近似，不声称 \(q\) 是真实软件状态类型；official \(z\) 只监督 prior，history posterior 必须由 likelihood 条件化。

**回读后的修改处理。** 本轮改写后立即重读所列原文。参照两篇逐式派生且不跳步的逻辑，原 \(K=16\) 主设定已经撤销；现行主规模为 \(K=8,Q\le4\) 的 exact 枚举、log-weight 与 log-sum-exp，\(K=16\) 只保留为通过主规模对照门后的 SMC 敏感性。

## P09　方法：20 类列 likelihood、统一 filter 与成本尾部

**双源定位。** 改写后重读 ACAA 第 210、212、215、218、220、224 行和 DSDL 第 148–152、187–195、199–227 行。这里特意避开空行：ACAA 210 为 DTV 综合表示，212/215/218 为 AMI 输入—式（8）—权重解释，220 为 ex-post 汇总，224 为训练链；DSDL 式（7）在 192、式（8）在 202、式（9）在 208、式（10）在 216、式（11）在 224 行。

**ACAA 逐句或句群功能。** 第 210 行先形成共同表示，第 212–218 行再由同一对象产生自适应融合，第 220 行说明汇总位置为何重要，第 224 行把全部对象按训练顺序重新串联。

**DSDL 逐句或句群功能。** 第 187–195 行把最终标签、无中间 gold 和结构约束联系起来；第 199–224 行逐式形成黑箱预测、约束、融合和最终统一目标；第 227 行明确最终预测与中间 assessment 两类产物。

**新段逐句功能（唯一当前句表）。** S1 定义 20 类 \(n_k\)。S2 说明列 likelihood 的条件对象与残余 \(r\)。F1 式（3）定义整列 likelihood。S3 明确 \(\omega\) 与 \(\xi^{(0/1)}\) 都经 softmax 正规化，并说明不假设三次独立。F2 定义冻结 joint。F3 给历史 filter 与 posterior predictive。F4 给真实/假设观察共用的归一更新。S4 冻结 \(R\) 和四类辨识对照。S5 给观察顺序一致性。S6 定义 \(3K\) 工作和 wall-clock 成本头。S7 给带 \(1/0.1\) 归一化的 CVaR 及端点敏感性。S8 限定 CPU CVaR 的报告责任。S9 分配 outcome/cost 损失。

**引用责任。** joint/filter/CVaR 是本文设计；ACAA/DSDL 只承担“一个中间对象持续派生、每个式项有责任、最终训练链闭合”的写作规范。20 类 likelihood 的归一、filter 顺序不变性和成本分位校准必须由代码和实验验证。

**回读后的修改处理。** 修正旧记录把 ACAA 空行 211/221/223 和 DSDL 空行 184 当内容的问题；删除任意 \(q(z\mid H\cup Y)\) 网络，新增 joint、真实/假设同一更新式、20 类 categorical 和正确归一的 CVaR。

## P10　方法：选择—放弃的终端风险

**双源定位。** 改写后重读 ACAA 第 215、218、220、224 行及 DSDL 第 179、182、185、187–189、213–224 行。

**ACAA 逐句或句群功能。** 第 215/218 行由同一表示定义输出及权重，第 220 行说明预测后汇总，第 224 行将中间机制和最终损失放在一条优化链。

**DSDL 逐句或句群功能。** 第 179–185 行从局部量导出累计量；第 187–189 行解释监督和异质性；第 213–224 行把理论量与黑箱输出融合进同一最终目标。

**新段逐句功能（唯一当前句表）。** S1 定义 select/abstain 动作集。S2 引出真实状态损失。F1 式（4）定义错过可用补丁和错发补丁两项损失。S3 校验损失语义。S4 引出 posterior risk。F2 式（5）定义各动作及最优停止风险。S5 冻结主损失比和敏感性。S6 解释全错池与测试不完备边界。S7 规定四类选择性发布指标。

**引用责任。** 损失比是规范选择，不由两篇 ISR 背书；其变化必须通过预注册敏感性展示。

**回读后的修改处理。** 修正旧记录把 ACAA 221/223、DSDL 184 当内容的问题；风险现只读取统一 filter 的式（2），与 outcome likelihood 形成同一决策概率对象。

## P11　方法：成本敏感 EVI 与推断审计

**双源定位。** 改写后重读 ACAA 第 210–224 行和 DSDL 第 179–227 行，并重读两篇序贯信息取得理论的行动—成本—最终决定公式段。

**ACAA 逐句或句群功能。** 第 210–220 行从中间表示到最终输出不跳步，第 224 行重述训练链，使反事实输出仍由同一机制产生。

**DSDL 逐句或句群功能。** 第 179–224 行让累计量、深层量、融合量与总目标保持同源；第 227 行声明中间和最终责任。

**新段逐句功能（唯一当前句表）。** S1 引出同一 posterior predictive/filter 的 EVI。F1 式（6）用同一 terminal risk 定义前后风险差并扣双成本。S2 从 \(3K\) 作业 cap 定义 \(\bar D,\bar W\)，再以十列 cap 之和定义 \(B_D,B_W\) 并给50%/75%预算敏感性。S3 定义合法行动和实测扣账。S4 对 \(\lambda_D,\lambda_W\) 只用 A+B×U development 以 Pareto和family-level one-standard-error规则唯一冻结。S5 冻结价格并把 calibration 限于温度。S6 给主 \(K=8,Q\le4\) 的至多1,024状态 exact filter。S7 明确每个假设列也 exact reweight，MC只估 predictive outcome 期望，并给128/256/512与2,048参考及小K枚举核验。S8 将 SMC 限于20–50项 \(K=16\) 敏感性，给初始化、递推、ESS、重采样与MH。S9 要求先在K8达到 \(p_k,p_A\) 误差≤0.01、action agreement≥95%、归一化EVI regret≤0.005，并报告ESS与MC SE；失败则K16只报filter/calibration。S10 要求同一likelihood及order/log-score/EVI/martingale检查。S11 给正EVI选择和tie-break。S12 限定一步近视并设置DP oracle。

**引用责任。** Moore–Whinston 与 Dos Santos–Mookerjee 负责信息价值必须回到最终行动及成本；它们不证明本文 exact 实现、SMC 或 MH kernel 正确。状态上界、粒子支持损失、EVI MC 稳定性、pre-cost 非负性和 martingale error 全由本文代码与测试负责。

**回读后的修改处理。** 本轮规模订正后再次重读 ACAA 210–224 与 DSDL 179–227 的逐式责任链。主 filter 收缩为 \(K=8,Q\le4\) 的至多1,024状态 exact；每个假设结果也 exact reweight，MC只积分 outcome；K16 SMC 必须先通过K8三项一致性门，使每一步都有可执行对象而不是只列算法名。

## P12　方法：联合目标和冻结训练协议

**双源定位。** 改写后重读 ACAA 第 224 行完整优化链和 DSDL 第 187–227 行。准确公式位置为 DSDL 192（式 7）、202（式 8）、208（式 9）、216（式 10）、224（式 11），最终双重产物说明在 227 行；旧记录的“188–214 包含式 7–11”已删除。

**ACAA 逐句或句群功能。** 第 224 行依数据流依次说明 preprocessing、embedding、两路 GRU、DTV、AMI、输出和反向更新对象，使训练工件与方法构件一一对应。

**DSDL 逐句或句群功能。** 第 187–195 行定义中间监督和结构正则；第 199–211 行定义深层预测与约束；第 213–224 行融合并统一目标；第 227 行同时承诺预测与中间 assessment。

**新段逐句功能（唯一当前句表）。** S1 分配 prior、20类 likelihood、成本与 Bayes-history proper scores。S2 每个task/epoch按history depth分层抽至多64个固定-seed history，强制empty/full及random、cheapest、coverage、static-batch、EVI五轨迹，不枚举1,024个子集。F1 式（7）列六类责任。S3 说明所有posterior losses来自同一filter且无辅助head。S4 限定rank/cost。S5 给history→task→family等权聚合。S6 冻结AdamW、学习率、batch、clip、epochs、early stop和损失网格。S7 给三阶段拟合及两个温度。S8 明确development/calibration权限，并在封存结果解封前签名K8 exact/MC与K16 SMC配置。S9 加纯计算microbenchmark：batch1/8/32、MC128/256/512、1,024 states、M10、显存、update、全M EVI p50/p95及2,000离线+1,200在线投影，超签名上限即No-Go。S10 排除policy/RL。

**引用责任。** 真实 \(z\)、计数列和资源直接监督各自 factors；calibration 只能用独立 split，任何 posterior 都必须在校准后的同一 joint 上重算。

**回读后的修改处理。** 本轮改写后立即重读 ACAA 224 与 DSDL 187–227；沿其“训练对象与构件逐项对应”的写法，把 development、calibration 与 sealed outcome 的权限写成互斥契约，并同步主 exact、EVI MC 和超规模 SMC 的冻结对象。

## P13　数据：公开资源分责

**双源定位。** 改写后重读 ACAA 第 228–244 行和 DSDL 第 105、109、113、118–120、231–239 行。ACAA 数据规模在 228 行而非空行 227；DSDL 案例、overview、样本分别在 105、109、113 行，而非空行 104、108、112。

**ACAA 逐句或句群功能。** 第 228 行明确预测单位、时间窗、酒店/评论/图片规模和日期；第 230–244 行再分实验与重复责任。

**DSDL 逐句或句群功能。** 第 105/109 行固定任务和流程，第 113–120 行固定样本、过滤和 mask，第 231–239 行报告规模、子集、基线、重复和实现位置。

**新段逐句功能（唯一当前句表）。** S1 声明需新建目标矩阵。S2 给 SWE-Gym 的任务/仓库责任和跨仓库边界。S3 给 SWE-rebench 的时间外测责任及去污染限制。S4 限定 SWE-smith 为预训练/压力测试。S5 给 TDD-Bench/SWT-Bench 的 issue-to-test 责任并禁止 developer tests 进入状态。S6 把现成 benchmark 与新生成候选、测试、计数矩阵和资源日志分开。

**引用责任。** 规模与公开状态由对应论文/发布版承担，最终实验需重新冻结 release、license、commit 和可重建率。

**回读后的修改处理。** 纠正五处空行行号；把 TDD-Bench Verified 的书目年份单列为 2024，删除把它与 Otter 2025 混为一项引用的做法。

## P14　数据：三 pipeline、边际 holdout 与不泄漏矩阵

**双源定位。** 改写后重读 ACAA 第 134、139、141–161、224、228 行和 DSDL 第 109、113、118–120、231–233 行。

**ACAA 逐句或句群功能。** 第 134–161 行把单位、过滤、对齐、mask 和变长处理写在网络前；第 224 行给可复现训练顺序；第 228 行量化实际数据责任。

**DSDL 逐句或句群功能。** 第 109 行先总览流程，第 113–120 行给入组/过滤/张量化，第 231–233 行报告总体与子集，防止只展示有利样本。

**新段逐句功能（唯一当前句表）。** S1 冻结至少20 family、每族上限和manifest。S2 冻结A/B/C三候选pipeline及每路四项。S3 定义A+B八候选主池和A+C八候选holdout并复用A×U；K16只由敏感性子队列A′/B′第二seed block扩展。S4 规定不足/补采/失败分母和删除来源ID。S5 定义主U10与holdout V5。S6–S9重申可见性、base准入、outcome前冻结和一次解封。S10 定义三个账面执行块并保留20类计数。S11 算出必要24k+12k+12k=48k及可选C×V后54k。S12 算出1,200 primary official和240审计复跑。S13 另账4,500 base准入；K16敏感性另账4,800–12,000 candidate–test及160–400 official。

**引用责任。** Agentless 只承担一种分阶段 pipeline 的正式实例，“工具交互式”和第三独立实现只是待冻结的 pipeline 类型，不借未列文献冒充既有方法。48k 是主块加两个边际 holdout，不冒充12×15完整全因子；联合C×V才使总量到54k。

**回读后的修改处理。** 本轮改写第二段后立即重读所列 ACAA/DSDL 原文；在既有无 future-filter 规则上补成物理访问契约：A+B×U development/calibration 独占选择与校准，三个 sealed outcome 块在全部设置签名后一次解封，资源算术不因访问时序改变。

## P15　数据：四项 Pilot 闸门

**双源定位。** 改写后重读 ACAA 第 230–260 行和 DSDL 第 235–239、249、267、285 行。

**ACAA 逐句或句群功能。** 第 230–244 行预先分预测、表征、输入和重复；第 260 行另报表征结果，不让最终 RMSE 替代中间证据。

**DSDL 逐句或句群功能。** 第 235–239 行分主预测、稳健与解释；第 249、267、285 行分别检验表示、中间量效用和组合/消融。

**新段逐句功能（唯一当前句表）。** S1 宣布存在性审查并把纯计算microbenchmark设为outcome解封前零号门。S2 给K8下50 mixed tasks、15 families及全错/全对责任。S3 给原始测试base准入率与候选计数异质门。S4 给joint NLL/Brier、主exact/换序 \(10^{-8}\) 与EVI MC 95%一致门。S5 要求SMC在K8达到边际误差≤0.01、action agreement≥95%、regret≤0.005并报ESS/MC SE；否则K16只报filter/calibration。S6 给双成本5% adaptivity及两个边际holdout方向门。S7 给撤题和禁止续命规则。

**引用责任。** 50、15、70%、30%、2%、0.02、95%、0.01、5% 都是事前研究治理阈值，不由 ISR 或近邻背书；须在结果前机器可读冻结。

**回读后的修改处理。** 本轮改写后立即重读所列实验原文；因主规模已经改为 \(K=8,Q\le4\) exact，闸门同步采用 exact 双实现、换序和 EVI MC 收敛，\(K=16\) SMC 只作门控敏感性且必须披露 support loss；holdout 方向只在一次解封后判断。

## P16　实验：基线与公平预算

**双源定位。** 改写后重读 ACAA 第 230–244 行和 DSDL 第 235–243 行。

**ACAA 逐句或句群功能。** 第 234–242 行按 base、attention、multimodal 和输入组合分层基线，同输入逐层识别机制，不堆无关 SOTA。

**DSDL 逐句或句群功能。** 第 235–237 行按 LSTM、multiview、conversation、contrastive families 组织12项基线；第 239/243 行统一评价和输入条件。

**新段逐句功能（唯一当前句表）。** S1 提出机制/系统两层。S2 固定 filter 只换七类 acquisition并统一 \(3K\) 成本。S3 列静态 verifier、CodeT、B4、e-Otter++、Agentless、SWE-RL、R2E-Gym 原生 selector。S4 要求后三个 direct neighbors 同报 native/adapted且不可语义等价时分表。S5 把 Opad、Iter-T、EGSS、EET置于原生附加实验。S6 明确 MPTPS、TOSEM 2024、ISSTA 2026 与两个预印本只作边界/测量/撤题审计，不扩主实验；只有同状态同成本的公开原生工件才进附录。S7 处理无 abstain 方法。S8 把全矩阵、hindsight、TC-Bench和DP降为上界/测量并要求适配标签。

**引用责任。** 每一近邻只由正式论文承担其原生机制；本文适配器、统一可见性和预算由实验代码承担，不能用 adapted 失败贬低原方法。

**回读后的修改处理。** 本轮新增边界句后立即重读 ACAA 234–244 与 DSDL 235–239；依其“只比较承担相同责任的构件家族”原则，没有把五项新近邻机械扩成确认性基线，而是保留覆盖、原生语义和撤题责任。

## P17　实验：Full、sealed holdout 与真实在线外测

**双源定位。** 改写后重读 ACAA 第 232–260 行和 DSDL 第 249、267、285 行。

**ACAA 逐句或句群功能。** 主预测、输入组合、下游表示和重复分开报告；第 260 行的中间表示证据不由最终指标替代。

**DSDL 逐句或句群功能。** 第 249、267、285 行依次验证表征、中间量效用和组合/消融，形成主结果后的机制证据链。

**新段逐句功能（唯一当前句表）。** S1 冻结2,000任务与至少80 family。S2 在任何 outcome 前操作化 family并盲态裁决。S3–S7给split下限、撤回、数据分责和无future-filter replay。S8 给联合factor/计数/成本/EVI消融、K8 exact/MC收敛及门控K16 SMC敏感性。S9 将C、V限于sealed边际holdout。S10 说明replay不等于在线。S11 定义至少30新family和在线 \(3K\) 顺序执行。S12 冻结四方法、区组和1,200 episodes。S13 算出12,000列与288,000 candidate–test作业，并明确只是子账。S14 将系统近邻留在附加账。S15 给资源不足时措辞。S16 将M规模稳健性限于冻结下采样；K16只在20–50项附加seed-block子队列门控运行，不重新择模、不进在线主账。

**引用责任。** family 规则由本文预注册并发布映射，不由 ISR 背书；fork、同源包和近重复项目须先合并再切分。“在线”必须真实等当前列返回，不能预跑完整矩阵模拟等待。

**回读后的修改处理。** 本轮主规模订正后再次重读 ACAA 232–260 与 DSDL 249、267、285；family 原则保持为正文可复算关系和盲态裁决，并把288k明确为在线 candidate–test 子账。主 filter 的机制证据同步改为K8 exact/MC主审计与门控K16 SMC敏感性。

## P18　实验：统计单位、cluster 推断与功效

**双源定位。** 改写后重读 ACAA 第 244 行、DSDL 第 239 行，并回看 ACAA 第 228 行 hotel-month 与 DSDL 第 231 行 customer 单位。

**ACAA 逐句或句群功能。** 第 244 行一次说明独立运行、十折、估计数、指标和实现位置，使方差来源可追踪。

**DSDL 逐句或句群功能。** 第 239 行同时交代重复、主/稳健指标、显著性程序、敏感性和解释分析。

**新段逐句功能（唯一当前句表）。** S1 以 P17 已冻结的操作化 family 为最高独立单位并排除五类伪重复。S2 给 task→family 两级等权。S3 给 paired family mean、cluster bootstrap、Pilot wild/CR2和Full层次模型。S4 用 Pilot 方差模拟5%改善的MDE/power并禁止同族任务替代family。S5 冻结三主检验与次指标。S6 将调度seed先聚合。S7 报完整分母并删除future-stable分母。

**引用责任。** cluster 方法是本文按数据层级设计，不声称 ISR 两文采用；80 family和80% power是确认性治理条件。

**回读后的修改处理。** 在旧 task/repository 聚合上新增 Pilot 少 cluster 的稳健方法、task-within-family 模型和 simulation-based power；family 不足时撤回，而非靠 cell/history 扩样本。

## P19　实验：资源账和发布工件

**双源定位。** 改写后重读 ACAA 第 224、228、348 行和 DSDL 第 231–239 行。ACAA 224 是训练链，228 才是数据规模，348 是固定 embedding 的计算边界；旧记录把空行227写成数据行已纠正。

**ACAA 逐句或句群功能。** 第 224 行列训练对象，第 228 行用确切规模和日期把实证工作量落地，第 348 行说明降低计算的选择及其边界。

**DSDL 逐句或句群功能。** 第 231–233 行给10,625实例、标签、时间和四数据集；第 237–239 行给基线、重复、实现和附加分析。

**新段逐句功能（唯一当前句表）。** S1 估三候选/三测试生成及 joint/exact/EVI/SMC GPU/CPU，并要求以纯计算门和 telemetry 替换。S2 要求构建脚本在 outcome 解封前逐模块核算冻结 encoder、relation、\(\rho/\pi/\omega/\xi\) 与 cost heads，并把主模型限定为 5M–20M 可训练参数。S3 算 Pilot 必要 48k、4,000 容器小时、62.5 小时。S4 另账 1,200 official、240 audit、4,500 base 及 54k 可选联合。S5 把 Full 480k 主块、72k sealed 边际、552k、46,000 小时与 718.75 小时限定为 candidate–test 子账。S6 另算 Full base 64,500 及 primary official 16,000+1,200=17,200。S7 算 official 审计 3,440。S8 另账 K16 敏感性 4,800–12,000 candidate–test 及 160–400 official。S9 要求所有 Full 数由 Pilot telemetry 重算。S10 给在线 288k、24,000 小时和 375 小时的 candidate–test 子账。S11 再次把在线生成、base、official、审计与重试排除在该子账之外。S12 给资源触顶处置。S13 枚举数据工件。S14 枚举 K8 exact/EVI 及门控 K16 SMC/MH 工件。S15 发布 optimizer state、checkpoint、逐模块参数统计与训练诊断。S16 发布每个在线决策及 SMC 敏感性日志。S17 给许可证处置。

**引用责任。** 所有GPUh是规划估计；容器算术为48,000×5/60=4,000、552,000×5/60=46,000、288,000×5/60=24,000，再分别除64。64,500、17,200与3,440是独立子账，不可重复混入candidate–test时数。最终论文必须以microbenchmark与telemetry替换估计并报告偏差。

**回读后的修改处理。** 本轮规模订正后再次重读 ACAA 224、228、348 与 DSDL 231–239；把552k/288k限定为离线/在线 candidate–test 子账，并补齐 Full 64,500 base 准入、17,200 primary official 与3,440审计复跑。算法日志同步K8 exact/EVI、门控K16 SMC/MH和分模块参数核算的实际分责。

## P20　预期贡献：IS 理论与设计科学责任

**双源定位。** 改写后重读 ACAA 第 316–318 行和 DSDL 第 315、329、331 行。

**ACAA 逐句或句群功能。** 第 318 行依次给概念、方法/工件和实证知识责任，没有把“用了深度学习”本身当贡献。

**DSDL 逐句或句群功能。** 第 315 行把主贡献限定为 methodological 并列学习策略和经验发现；第 329/331 行分别从预测行动价值与理论中间量—黑箱协同给实践/设计科学含义。

**新段逐句功能（唯一当前句表）。** S1 条件式提出测试作为历史依赖信息行动。S2 把规范结构落实为闭合joint、主 \(K=8\) exact filter、受门控的 \(K=16\) SMC敏感性、双成本与terminal risk。S3 将四项工件绑定持出、coherence、校准或消融。S4 明确只迁移两篇ISR的论证规范。S5 给三次计数资源矩阵的数据贡献。S6 规定joint/filter/EVI/online失败后的降格。

**引用责任。** 决策理论负责规范结构；ACAA/DSDL 只负责设计写法，不证明本文算法。所有“贡献”在实证前均为条件命题。

**回读后的修改处理。** 本轮改写后立即重读 ACAA 316–318 与 DSDL 315、329、331；贡献措辞同步主 exact、超规模 SMC 敏感性的真实分责，没有把近似推断写成主算法硬度。

## P21　主张边界与 No-Go

**双源定位。** 改写后重读 ACAA 第 346、348 行和 DSDL 第 339–343 行。

**ACAA 逐句或句群功能。** 第 346 行收束问题、指标、机制和结果；第 348 行依次限制情境、数据要求、遗漏因素、参数和固定 embedding 粒度。

**DSDL 逐句或句群功能。** 第 339–341 行并置一般性与情境 tailoring；第 343 行按跨域、输入覆盖、复杂度、过拟合和行为使用逐项限界。

**新段逐句功能（唯一当前句表）。** S1 将 official correctness 与更广质量安全切开。S2 列非贡献和一步 EVI 边界。S3 对直接近邻及自然组合给先于 Pilot 的撤题条件。S4 逐项重复 K8 mixed-family、base 准入/异质、joint+K8 exact/MC+SMC 一致性/coherence、adaptivity/holdout 四门。S5 规定撤题输出并禁止 future-filter、gold 筛选、复杂化和事后调价。S6 增加 Full family 下限与真实在线主张门。S7 规定 K16 未通过误差、行动一致率和 regret 三门时只能报告 filter/calibration，不得承担主动 policy 主张。

**引用责任。** No-Go 阈值来自 P15 研究治理；官方标签语义来自 benchmark harness，生产安全需额外验证。

**回读后的修改处理。** 本轮改写后立即重读 ACAA 346、348 与 DSDL 339–343；把近邻边界升级为明确撤题条件，并将旧 exact–SMC 主门改为 exact 双实现、EVI MC 与 coherence 主门，SMC 不再承担主结论。

## P22　结论：执行顺序与对称出口

**双源定位。** 改写后重读 ACAA 第 346–348 行、DSDL 第 339–343 行，并回看两篇摘要。

**ACAA 逐句或句群功能。** 第 346 行按问题—概念—机制—证据复核全文承诺，第 348 行立即给输入与泛化限制，不在结尾增加机制。

**DSDL 逐句或句群功能。** 第 339–343 行以任务、方法、外推和限制结束，保持情境特定性。

**新段逐句功能（唯一当前句表）。** S1 明确协议而非结果。S2 给三候选/三测试、20 Pilot family、outcome前参数核算与纯计算门、仅用A+B×U development/calibration冻结joint/K8 exact/MC/门控K16 SMC/损失价格、三个sealed outcome一次解封、四门、Full及在线family的唯一时序。S3 把全文压回“下一项三次整列是否值得其双成本”的唯一算法问题。S4 给正结果工件链和负结果静态边界知识两个对称出口。

**引用责任。** 结论不新增事实；未完成实验前不得改成性能完成式，缺在线则保留offline限定，门失败则保留原始分母和负结果。

**回读后的修改处理。** 本轮改写后立即重读 ACAA 346–348 与 DSDL 339–343；结论顺序现在与 A+B×U 独占开发/校准、三个 sealed outcome 一次解封、主 exact 与超规模 SMC 敏感性完全一致，没有新增RL、LLM微调或多步planner。
