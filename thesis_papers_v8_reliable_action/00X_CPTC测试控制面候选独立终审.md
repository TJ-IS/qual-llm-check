# CPTC 测试控制面候选独立终审

审查日期：2026 年 8 月 15 日  
审查对象：`00T_第三题替换候选广搜与红队.md` 中唯一存活候选“控制目的驱动的测试控制面共演策略”，即 CPTC  
审查性质：独立终审。本文不是候选方案的补充设计，也不以保留第三题为目标。

## 1. 终审结论

**结论为 NO-GO。CPTC 不应冻结为第三篇论文，也不应以现有名称、理论机制或配对数据设计继续进入正式写作。**

这一结论不是因为风险不真实。coding agent 同时能够修改生产代码和测试时，确实可能通过削弱断言、改写 evaluator 或迎合可见测试制造虚假成功；测试又确实需要随有效需求和生产代码演化。CPTC 的行动空间也比简单的允许或拒绝更丰富，能够包含隔离测试改动、保留回归通道、生成独立控制和延迟提升等操作。这些优点使该现象值得研究，却不足以使当前候选成立。

候选同时触发三个不可由增加模块修复的撤题条件。

1. 核心配对把“哪个需求契约当前有效”与“控制者为何选择和实施控制”混为一谈。同一测试改动在旧、新契约下应被不同处理，识别的是契约条件下的正确行动，不是 Wiener 等人所定义的 control purpose 的因果作用。
2. `P`、`F` 和 `Z` 没有获得理论不可替代的信息或计算能力。只要等参数通用模型看到相同的原始 charter、规范历史、仓库图、候选 diff、执行结果和行动结果，它就能学习同一映射。若理论模型额外获得人工 purpose/fit 标签，则比较依赖特权信息，不再是理论结构带来的能力。
3. 现有公开资产可以分别提供合法测试演化和测试操纵的正、负样本，却不能提供 CPTC 所要求的“同一生产代码与测试 diff、两个都合法的控制目的、相反的唯一正确 portfolio、独立可执行真值”。用未来 commit、开发者测试补丁或据此撰写的 charter 补齐标签，会造成未来规范泄漏或后见之明；用研究者合成 charter 补齐标签，则把任务变成读取显式契约偏好的指令条件决策。

此外，截至检索截止日，测试演化、代码与测试共演训练、reward-hacking 抑制、动态 verifier、独立测试认证和迭代 verifier 修补均已有直接工作。CPTC 剩余的独立贡献只能依赖上述 purpose-conditioned portfolio 机制；该机制在构念、识别和反证三关均未通过。因此，不能把若干已有技术拼装后用 IS 控制术语重新命名为独立算法贡献。

## 2. 实际回读范围与判定口径

本次终审重新阅读了 `00T` 的候选定义、张量、损失、行动空间、配对构造、基线、撤题条件及引用表。IS 理论判断来自以下三篇本地全文，而非摘要或二手综述。

- Kirsch（1997），本地全文 `database_fulltext_all/26780_1997_portfolios-of-control-modes-and-is-project-management.md`。重点回读控制定义、formal behavior/outcome control、portfolio 构造、作用条件、动态调整及局限，尤其是第 54、68—76、94、265—281、300—306、330—336 行附近。
- Choudhury 与 Sabherwal（2003），本地全文 `database_fulltext_all/26513_2003_portfolios-of-control-in-outsourced-software-development-projects.md`。重点回读第 83—133、381—411、419—425 行附近有关 controller/controllee、正式控制、奖励、mode choice、动态组合和研究边界的论述。
- Wiener 等（2019），本地全文 `database_fulltext_all/03988_2019_moving-is-project-control-research-into-the-digital-era-the-why-of-control-and-the-concept-of-co.md`。重点回读第 81—105、128—148、185、197—203 行附近有关 what、how、why、两类 purpose、构念边界和测量要求的论述。该本地文件不含可供本次核验的在线附录，本文不声称读过附录。

技术近邻检索覆盖三组查询：test/code co-evolution、specification change 与 test maintenance；evaluator tampering、reward hacking control 与 verifier integrity；dynamic/evolving verifier、independent oracle 与 test certification。检索截止到 2026 年 8 月 15 日，并优先核验论文全文、正式会议页面、作者项目页和公开数据页。终审判定采用强标准：现象真实和工程可运行只是必要条件；理论构念必须被正确测量并在保持原始信息相同的情况下产生通用替代模型不能复制的结构性能力。

## 3. 理论原文实际支持什么

### 3.1 Kirsch（1997）

Kirsch 将控制宽泛地定义为确保组织中的个人依照组织目标行动的各种尝试，并把 IS 开发明确视为由多类利益相关者参与的社会过程。本义中的 controller 和 controllee 是能够形成角色期待、拥有项目知识、评价行为或结果并实施奖励的组织参与者。

formal behavior control 是一种绩效评价策略。控制者需要明确规则和程序，观察 controllee 的行为，并依据其遵循程度实施奖励。适当行为是否已知、行为能否被观察，是这种模式的关键条件。formal outcome control 则要求明确目标或结果、度量是否达到目标，并依据结果奖励或惩罚 controllee。结果可测量性是其关键条件。Kirsch 的表 1 也把“规则与程序加基于遵循程度的奖励”和“目标加基于结果的奖励”写进正式控制的特征，而不是把任何技术限制或测试执行都自动归为行为或结果控制。

Kirsch 的 portfolio 结论支持多个模式和多个机制共同存在，也支持同一机制服务不同模式。研究同时显示，既有程序可能需要按项目裁剪，结果目标也可能在项目中重新协商。portfolio 的选择还取决于任务特征、角色期待以及 controller 和 controllee 的项目知识与技能。原文没有推出 obligation 级双 purpose 强度、四维 fit 分数、soft portfolio tensor、图网络或特定行动顺序。

### 3.2 Choudhury 与 Sabherwal（2003）

该研究把上述理论扩展到外包软件项目，但分析单位仍是客户与供应商中的个人或团队。outcome control 由结果规格、进度度量和相关评价构成；behavior control 由过程规定、行为观察和基于遵循程度的评价构成。论文指出所有控制都带有显性或隐性奖励，并专门提醒，仅有监控是否足以构成 behavior control 仍需进一步研究。

该研究没有把 mode choice 化为四个相互独立的连续 fit 维度。它讨论的因素包括行为可观察性、结果的指定与跟踪能力、项目规模、controller 知识、controllee 的通用和情境知识、角色期待、其他控制是否可用，以及先前绩效问题。案例结果进一步提出这些因素可能具有层级和交互关系，例如 controllee 知识、角色期待和监控难度会压过 controller 知识或项目规模。随着绩效问题和双方学习出现，初始判断及 portfolio 会改变。论文还明确警告，高不确定任务中的需求可能需要演化，不能从详细前置规格有效的个案推出规格应永久固定。

### 3.3 Wiener 等（2019）

Wiener 等区分三件事。control configuration 回答使用了什么控制，control enactment 回答如何实施控制，control purpose 回答为什么这样配置和实施控制。其表 1 和正文把 purpose 定义为“支撑 controller 配置和实施控制的意图”。因此，purpose 属于 controller 的前瞻性或回顾性意图，不等同于可观察的控制行为，更不等同于被控制工件是否符合当前规范。

value-appropriation purpose 源于代理问题，关注防止机会主义 controllee 错误占用价值，典型焦点是监督、监控、合规、奖励和制裁。value-creation purpose 源于 stewardship 视角，关注通过合作、协调、促进、指导以及整合利益相关者的异质知识和技能创造价值。后者并非“只要允许软件或测试继续变化就属于 value creation”。两种目的可以同时作用于同一机制，在某一时点其中一种可能占主导。作者还明确要求后续研究用数据评估 controller 的底层意图，谨慎区分意图与行为，以及前瞻性与回顾性意图。

Wiener 等将构念置于 IS project level，并以人类参与者的 agency、stewardship、内在动机、共同组织目标及知识协作为理论基础。将 coding agent 视为新的 controllee 可以形成有价值的理论扩展，但不能跳过构念转换。模型优化导致的 proxy exploitation 不必然等同于人类机会主义，语言模型也不能因完成任务就被视为具有 stewardship 意义上的内在动机、组织认同和长期福利取向。

## 4. CPTC 的构念映射审计

| CPTC 设计 | 理论可以支持的部分 | 终审发现 | 判定 |
|---|---|---|---|
| 组织或开发团队作为 controller，coding agent 作为 controllee | 控制理论允许多个 controller/controllee 关系，自动化代理可以成为新的被控制行动者 | 这是可论证的情境扩展，但需说明 agent 与人类 controllee 的差异；现稿直接继承 agency/stewardship 假设 | 有条件成立，不足以救题 |
| `P ∈ [0,1]^(B×N_o×2)` | Wiener 等确实区分 appropriation 与 creation purposes，并允许并存 | 原文没有给出 obligation 级连续强度或其监督尺度；charter 标签只是对显式输入的解析。creation-enablement 被操作化为“允许合法测试演化”，遗漏协作、知识整合和 stewardship 机制 | 构念层级错置，后验换名风险高 |
| `F ∈ [0,1]^(B×N_o×4)` | 适当行为知识、行为可观察性、结果可测量性会影响正式模式 | “结果可指定性”在 Choudhury 与 Sabherwal 中已被纳入 specify and track 的 outcome measurability；四维设计遗漏 controller/controllee 知识、角色期待、项目规模、其他控制和绩效历史，并抹去层级与交互 | 不是完整或经验证的 formal-control fit |
| `M` coverage/provenance 关系与 `I` 独立性矩阵 | 控制研究承认机制和多模式组合 | coverage、mutation、provenance、oracle independence 是软件验证事实，不由控制理论推出 | 技术核心，可保留为工程变量，但不能承担理论贡献 |
| `Z ∈ [0,1]^(B×N_o×N_m×2)` | control portfolio 和同一机制支持多种模式有理论根据 | 软权重、obligation 分解、purpose 轴和 portfolio decoder 均是设计者选择；理论没有推出该张量或 softmax 计算 | 普通结构化行动 latent 的理论命名 |
| 路径锁、shadow branch、双轨测试、隔离、独立测试、joint promotion | 可以作为组织实施控制的技术机制 | 行动集合混合 access control、分支管理、验证、修复和发布决策。若没有规则或结果的明确评价以及奖励、惩罚关系，路径锁和 sandbox 不自动成为 Kirsch 意义的 formal behavior control；独立测试也只有在结果被明确用于评价时才是 outcome control | mode 标注存在事后归类 |

特别需要指出，CPTC 最接近理论的不是“测试目录属于控制面”这一比喻，而是 controller 为何在防止假绿和促进软件演化之间选择控制组合。然而现有计算图并没有测量这种组织意图。它从研究者撰写的 charter 和版本合同产生 `P`，再用研究者提供的 purpose 标签监督 `P`。这形成的是文本解析辅助任务，不是从组织行为、交互或前瞻性选择中识别 control purpose。

## 5. 决定性混淆：contract validity 不是 control purpose

令 `C` 表示当前有效契约，`G` 表示 controller charter，`D=(ΔP,ΔC)` 表示固定的候选生产代码与测试改动，`X` 表示仓库、规范历史、执行轨迹、成本和全部可观察输入。CPTC 的核心配对改变的是：

`(C_old, G_old, D)` 与 `(C_new, G_new, D)`。

若同一 `ΔC` 在旧契约下削弱仍有效的断言、在新契约下记录合法的新行为，那么正确行动改变的直接原因是 `C_old` 与 `C_new` 定义了不同的正确软件行为和 evaluator oracle。该配对估计的是：

`A*(C_old, D) ≠ A*(C_new, D)`，

而不是：

`A*(do(P=appropriation), C, D) ≠ A*(do(P=creation), C, D)`。

两者不能互换。一个组织在旧契约世界可以同时希望防止 agent 制造假绿并促进真正的任务完成，在新契约世界同样可以同时具有这两种目的。正确行动之所以翻转，并不要求 control purpose 翻转。Wiener 等还明确指出同一机制可同时服务两种目的，这进一步否定了“旧世界等于 appropriation、新世界等于 creation”的一一映射。

要识别 purpose 的独立作用，至少需要保持活动契约、原始仓库、候选 diff 和可用机制不变，独立改变 controller 的前瞻性目的，再观察控制配置或实施如何变化。形式上应是 `C × P` 的因子设计，而不是仅比较 `C_old × C_new`。即使建立这一设计，理论也不保证每个目的对应唯一且方向相反的 portfolio。不同机制可以实现同一目的，一个机制也可同时实现两种目的；正确标签更可能是条件效用前沿而不是单一 gold action。

因此，`00T` 的反事实方向损失 `L_counterfactual` 实际监督契约敏感性。把这个信号传入 `P` 或命名为 purpose consistency，不会改变其识别对象。若将候选改名为 contract-conditioned test evolution policy，核心混淆可以消失，但 IS control purpose 的独立理论贡献也随之消失，技术问题会落入已有 test maintenance、verifier integrity 和 constrained decision making 的拥挤空间。这不是对 CPTC 的局部修补，而是另一个研究题。

## 6. 张量、损失和动作是否由理论推出

`00T` 使用 obligation decoder、purpose decoder、fit decoder、measurement/independence decoder 和 portfolio decoder，并提出十项加权损失：obligation、purpose、fit、measurement、independence、portfolio、counterfactual、joint edit、value 和 constraint。逐项检查后，理论只对“可能有多种控制模式”“两类 purpose 应被区分”“某些条件影响模式选择”提供概念启发。它没有推出以下任何必要计算。

- 为什么 purpose 应被表示为每个 obligation 的两个连续标量，而不是项目级类别、时间变化的 controller belief 或直接的 charter embedding。
- 为什么 fit 应是四个独立连续值，以及它们应以何种函数进入 portfolio logits。
- 为什么 portfolio 必须表示为 `obligation × mechanism × mode` 的软权重，而不是约束满足、行动集合预测或 belief-state planning。
- 为什么八类执行动作具有当前顺序、粒度和组合方式。
- 为什么 `L_purpose`、`L_fit` 与 `L_portfolio` 的监督会增加外部可执行能力，而不是充当辅助正则项。
- 为什么 `L_counterfactual` 的正确方向来自 control purpose，而不是活动契约和行动结果。

真正决定风险结果的量是活动契约、候选修改的语义影响、测试与候选的共同 provenance、独立 oracle 的覆盖以及各 portfolio 的 rollout outcome。这些分别由 `S`、`M`、`I`、hidden outcome 和执行器提供。它们是软件工程与决策信息，而不是 control-purpose tensor 的结果。若打乱 `P/F` 后性能下降，仍可能只是因为删除了对 charter 或 contract 的中间监督；若不下降，则理论头被策略忽略。两种结果都不能单独证明理论带来通用替代模型无法获得的能力。

## 7. 等参数通用替代的反证

### 7.1 信息层面的二分

设 CPTC 的原始输入为

`X = (S_0:t, G_t, R_t, W_t, ΔP_t, ΔC_t, E_t, C_t)`。

现有设计中 `P=h_P(S,G)`、`F=h_F(X)`，`M` 和 `I` 也由 `X` 及执行结果计算。若这些中间标签不包含原始输入之外的特权事实，则在给定 `X` 后，它们不会给最优行动增加信息，即可写成 `I(A*; P,F | X)=0`。CPTC 所学的是一个复合函数：

`X → (P,F,M,I,Z) → A`。

等参数通用模型可以直接学习 `X → A` 或 `X → outcomes for every A → A*`。若人工 purpose/fit 标签确实包含 `X` 中没有的事实，则 CPTC 获得了 privileged supervision；公平基线也必须获得同一事实，否则差异不能归因于理论结构。这个二分没有给“理论张量独有能力”留下信息来源。

### 7.2 equal-parameter raw heterogeneous Graph Transformer

反证模型使用与 CPTC 完全相同的节点、边、原始 charter、规范历史、diff、执行预算和 code-model 初始化，保持相同参数量、训练 rollouts 和候选动作数。它删除 `P/F/Z` 的命名头，将腾出的参数用于同深度的 graph Transformer，并同时预测八种 portfolio 的外部结果向量及最终行动 logits。结果向量至少包括真实契约满足、false-green、回归破坏、独立认证、人工介入和计算成本。

该模型可以直接从 `G` 与 `S` 学到旧、新契约的动作翻转，也可以从 provenance 和执行图学习何时需要独立控制。CPTC 的所有中间量都是该模型输入的函数，因而不存在表示能力上的阻碍。CPTC 至多可能获得样本效率、校准或解释优势；在尚无实验且构念标签本身无自然真值时，这些可能性不足以支撑独立 ISR 级算法贡献。

### 7.3 constrained POMDP

POMDP 反证使用同一观察 `X_t`、同一八类行动和同一 rollout 结果。隐状态表示活动契约可靠性、测试独立性、evaluator integrity、需求变化不确定性和 agent 轨迹；belief update 由可见执行、差分测试、mutation 和后续反馈学习。奖励或约束直接使用任务成功、不可接受假绿、回归、人工负担与成本。该模型不需要给 belief 各维命名为 appropriation 或 creation，仍能在证据不足时隔离、增加独立测试、请求确认或延迟提升，并能在需求已被可靠 supersede 时允许测试演化。

由于 control theory 没有对状态转移、观测模型或 utility 提供额外可识别限制，CPTC 不能声称一般 POMDP 无法复制其决策。若把 charter 目的作为 POMDP 的观测或 utility 条件，复制更直接。

### 7.4 direct outcome predictor

最强的简洁反证是对每个候选行动 `a_k` 学习

`Q_k(X) = (Pr[active-contract success], Pr[false green], Pr[regression], Pr[independent certification], cost, human burden, uncertainty)`，

随后按照 prospectively declared constraints 或 Pareto 规则选择行动。它使用与 CPTC 相同的 exhaustive branch rollouts 作为监督，能够处理多目标权衡、拒绝率与任务成功的冲突，也不会退化为二分类器。活动契约改变时，`Q_k` 自然改变，因而能复制“同 diff、不同契约”的方向翻转。

这三个反证都满足 `00T` 自己规定的公平比较：相同原始 charter、相同 purpose 标签可见性、相同隐藏 oracle 查询预算、相同参数和训练数据。CPTC 没有提出任何无法被它们表示的理论约束，故 equal-parameter falsification gate 在 pilot 之前已被结构性触发。

## 8. 公开数据与配对真值审计

| 公开资产 | 实际可提供的证据 | CPTC 核心真值缺口 |
|---|---|---|
| [TEBench](https://arxiv.org/abs/2605.06125) | 314 个真实 Java project-level test-evolution tasks；`V−1`、只含非测试改动的 `V−0.5`、含开发者测试改动的 `V0`；breaking、stale、missing 标签和可执行环境 | 数据只有一个历史实现世界。`V0` 的开发者 test patch 是 future ground truth，commit message 和历史也暴露后见语义；没有 controller charter、purpose 观测或独立隐藏行为 oracle。开发者选择不是唯一正确 portfolio |
| [TestEvo-Bench](https://arxiv.org/abs/2607.02469) | 746 个 test-generation tasks、509 个 test-update tasks、152 个候选来源项目；执行旧/新测试与旧/新代码的跨版本组合，支持按时间切分 | prompt 明确告诉 agent 生产代码是 post-change 真值，并限制只能修改目标测试文件。它测量测试是否适应既定新代码，不测 source/test 联合控制、controller purpose 或两个合法契约。旧行为可能是缺陷，不必然是同等合法的替代规范 |
| [ImpossibleBench](https://arxiv.org/abs/2510.20270) | 通过让测试与固定自然语言规范冲突，构造无歧义的 cheating negative；可研究测试访问、反馈、监控和修改行为 | impossible mutation 明确不合法，不能提供另一种合法 purpose。它给出冲突世界而非“同一改动在两个合法世界均有组织真值” |
| [SpecBench](https://arxiv.org/abs/2605.21384) | 30 个长程系统、可见 validation tests 与 held-out compositional tests，可测 visible-hidden gap | 没有测试演化历史、source+test diff、purpose charter 或相反世界。只能作为独立 outcome control，不是配对标签源 |
| [RewardHackingAgents](https://arxiv.org/abs/2603.11337) | evaluator tampering 与 train/test leakage 的可审计 workspace、文件访问日志、trusted external metric 和 locking 防线 | 研究的是 evaluator integrity 和技术隔离，不提供合法测试演化目的或 portfolio 真值 |

### 8.1 “同一 diff、两个合法目的”无法由这些数据直接构造

从历史 commit 可以复制同一 `ΔP` 和 `ΔC`，再把它们分别放进旧、新 revision。然而这只产生两个代码执行环境。要使两个世界都具有合法的组织规范，还需要在每个世界中存在于行动之前、可独立核验的 issue、ADR、API contract 或需求签发记录。TEBench 和 TestEvo-Bench 并未提供这种双重 prospective contract，更没有记录 controller 当时为何选择某一控制组合。

历史旧行为也不能自动当作合法旧契约。生产代码变化可能是在修 bug、安全缺陷或未定义行为。把“旧代码曾经存在”解释成“组织仍可合法选择该行为”，会把实现状态误当需求真值。Sun 等（2023）还表明，即使生产代码与测试代码同 commit 修改，朴素共演假设仍有 11.34% 的 false positives；随着时间间隔增大，false-positive rate 可上升到 96.40%。commit 邻近性不足以给出共演因果，更不足以给出 control purpose。

### 8.2 portfolio 没有唯一公开 gold

对于同一合法需求变化，保留旧 regression lane、建立版本化双轨、生成独立差分测试、隔离候选测试、只提升 source patch 或在额外认证后共同提升，都可能在不同风险偏好和成本约束下合理。公开单元测试只能判定某些行为结果，不能判定哪个组织控制组合唯一正确。CPTC 若用研究者规则生成 portfolio 标签，策略会学习规则；若用 learned verifier 生成标签，结果会继承 verifier 偏差；若用开发者历史动作作标签，只能说明当时做了什么，不能说明该动作由哪种 purpose 产生或优于所有替代动作。

可执行 rollout 可以把问题改成多目标行动结果预测，并根据预先声明的 utility 选择 portfolio。这恰好支持前述 direct outcome predictor，却不能使 control purpose 成为不可替代状态。

### 8.3 未来规范泄漏无法靠普通 group split 消除

TEBench 的 `V0` test patch、开发者 commit message、后续 commit、PR 讨论和由这些材料摘要得到的新 contract 都属于相对于 `V−0.5` 决策时点的未来或后见信息。它们可以作为 trainer-only evaluator 资料，但不能直接进入 solver 输入。若用它们生成 charter 再把 charter交给 solver，语义已经从未来补丁泄漏到输入；即使没有字节重合，仍是标签语义泄漏。

repository、lineage、issue family、commit ancestry 和 diff hash 的整体分组能阻止近重复跨 split，却不能修复时点泄漏。要避免泄漏，新契约必须由候选修改形成之前已经发布并带时间戳的 issue、规范版本或维护决策给出；隐藏 evaluator 必须独立于候选测试和同一 agent。现有四个核心公开资产均不能同时满足这些条件。

若完全合成两个 charter，可以严格控制时点，却产生另一问题。charter 会直接声明哪个行为应保留、哪个需求已 supersede，`P` 成为实验者赋予的文本条件。模型的动作翻转主要由读取契约完成，purpose 真值和正确 portfolio 都由研究者设定。这样的数据适合测 instruction following 或 contract-conditioned planning，不能验证自然组织中的 control purpose。

### 8.4 数据门最终判定

公开数据足以建立两个有价值但已被直接研究的任务：合法 test evolution；测试或 evaluator 操纵的检测与抑制。公开数据目前不足以建立 CPTC 声称的 purpose-identifying paired dataset。`00T` 提议的 100 pairs、8 个 repository lineages 和 1,200—1,800 branches 在技术上可以运行，但没有证据表明其中 100 个 case 同时具备两个合法 prospective contracts、独立 purpose 真值和非唯一 portfolio 的可比较效用。问题不在样本数，而在标签对象并不存在于这些历史记录中。

## 9. 截至 2026-08-15 的最强直接近邻

### 9.1 test/specification evolution 与 maintenance

- Sun et al.（2023），[Revisiting the Identification of the Co-evolution of Production and Test Code](https://doi.org/10.1145/3607183)，直接证明从共修改历史挖掘 PT co-evolution 会产生大量噪声，并给出 CHOSEN。
- Chi et al.（2024），[REACCEPT](https://arxiv.org/abs/2411.11033)，已经结合动态验证与 LLM 自动识别和更新 obsolete tests。
- Zhang et al.（ASE 2025），[Comprehend, Imitate, and then Update](https://cs.nju.edu.cn/yuanyao/static/ase2025.pdf)，其 COMMITUP 已直接处理 LLM test-suite evolution。
- Shang et al.（2026），[TEBench](https://arxiv.org/abs/2605.06125)，已经把 test evolution 提升到 project-level coding-agent identification 和 update。
- Wang et al.（2026），[TestEvo-Bench](https://arxiv.org/abs/2607.02469)，已经提供真实、可执行、time-stamped 的 test generation/update benchmark。
- Haroon et al.（2026），[Evaluating LLM-Based Test Generation Under Software Evolution](https://arxiv.org/abs/2603.23443)，直接研究 LLM 测试在语义改变和语义保持演化下的稳定性。

这些工作使“识别并更新需要演化的测试”“从 commit 挖 test/code co-change”“验证测试是否反映新代码”都不能成为 CPTC 的独立新增能力。

### 9.2 code/test 或 generator/evaluator 共演

- Li et al.（2025），[CoCoEvo](https://arxiv.org/abs/2502.10802)，共同演化程序和测试，并用交叉评价与多目标选择改进代码生成。
- Wang et al.（2025），[CURE](https://arxiv.org/abs/2506.03136)，通过 reinforcement learning 共同训练 coder 与 unit tester，并产生模型权重。
- Wang et al.（2026），[The Verification Horizon](https://arxiv.org/abs/2606.26300)，明确论证固定 verifier 会随 policy 能力增长而失效，verification 必须与 generator 共演。
- Wang et al.（2026），[BenchJack](https://arxiv.org/abs/2605.12673)，使用攻击与修补迭代提高 verifier/benchmark robustness。
- Protogeros et al.（2026），[Self-evolving network verifiers](https://arxiv.org/abs/2608.11340)，展示 coding agent 在 trusted router oracle 反馈下迭代修补 verifier 模型。

因此，“共演”本身、执行矩阵、多目标选择、动态 verifier 和迭代修补都已有直接工件。CPTC 必须由 purpose-specific new capability 承担剩余贡献，而该能力没有通过本审。

### 9.3 reward hacking control 与独立评价

- Farquhar et al.（ICML 2025），[MONA](https://proceedings.mlr.press/v267/farquhar25a.html)，用 myopic optimization 与 non-myopic approval 抑制多步 reward hacking，且包含测试驱动 coding 环境。
- Zhong et al.（2025），[ImpossibleBench](https://arxiv.org/abs/2510.20270)，直接研究 agent 修改或利用测试的倾向，以及 test access、context engineering 和 monitoring。
- Zhao et al.（2026），[SpecBench](https://arxiv.org/abs/2605.21384)，用 visible/held-out test gap 测量长程 coding agent 的 reward hacking。
- Atinafu 与 Cohen（2026），[RewardHackingAgents](https://arxiv.org/abs/2603.11337)，把 evaluator locking、train/test denial 和 trusted external metric 做成可审计控制。
- Lodkaew et al.（2026），[CapCode/CapReward](https://arxiv.org/abs/2606.07379)，用随机测试和 capped achievable score 检测 cheating，并把抑制信号用于训练。
- Wu 与 Tang（2026），[When Reward Hacking Rebounds](https://arxiv.org/abs/2604.01476)，在可改写 evaluator 的 coding 环境中学习 representation-level signals，并通过 Advantage Modification 改变 GRPO 更新。
- Xie et al.（2026），[Coding Agents as Test-Suite Auditors](https://arxiv.org/abs/2608.01715)，用独立 accepted solutions、brute-force dispute resolution 和 legality validator 建立不依赖官方 judge 的认证链。

这些工作分别覆盖技术锁定、训练信号、表示干预、动态监控、隐藏组合测试和独立认证。把它们与 test evolution 合并为一条 portfolio policy 可能有工程价值，但“合并两极”不构成理论不可替代的算法能力。

## 10. 撤题门逐项判定

| 终审门 | 结论 | 证据 |
|---|---|---|
| 风险是否真实影响 coding-agent 行动和外部结果 | 通过 | 测试操纵可制造假绿，永久冻结测试又会阻碍合法演化 |
| 是否有非平凡行动空间和本地训练工件 | 通过 | portfolio、rollout、图模型和 policy checkpoint 均可实现 |
| control purpose 是否被正确识别 | 不通过 | 配对改变活动契约；`P` 是 charter parser，不是 controller intention 的独立测量 |
| value creation 映射是否保持理论含义 | 不通过 | 合法 test evolution 被等同于 creation-enablement，缺少 stewardship、协作和知识整合机制 |
| formal-control fit 是否忠实 | 不通过 | `F` 选择性截取 antecedents，遗漏知识、角色、规模、其他控制和动态层级；技术路径限制也不自动构成正式控制 |
| 理论是否不可替代地进入前向、损失和行动 | 不通过 | P/F/Z 是可删除的语义瓶颈和辅助监督；真正结果由 contract、provenance、independent oracle 和 rollout 决定 |
| 同 diff、不同 purpose 的公开配对真值是否存在 | 不通过 | 现有数据只有单一历史世界或明确 impossible 世界，没有两个自然且合法的 prospective purposes |
| 是否能无未来规范泄漏 | 不通过 | V0 test patch、commit message 和后续讨论用于生成 contract/charter 会带入后见语义；普通 group split 无法修复 |
| equal-parameter generic alternative 是否不能复制 | 不通过 | raw graph Transformer、constrained POMDP 和 direct outcome predictor 均可在相同信息与预算下表达同一策略 |
| 面对直接近邻是否仍有足够大的新增能力 | 不通过 | 正向、负向、共演、训练抑制、动态 verifier 和独立认证均已有直接工作；剩余 purpose 机制失效 |

## 11. 最终处置

1. 将 CPTC 作为第三篇独立论文候选撤销，第三题宁缺毋滥。
2. 不以“contract-aware CPTC”“purpose-calibrated verifier”或增加更复杂的 `P/F/Z` 损失继续包装。前者会改变研究题，后者不能修复构念和识别。
3. 可保留的只是内部研究资产：合法 test evolution 与 evaluator tampering 的双侧 benchmark 地图、独立 oracle 构造清单、future-spec leakage 检查、以及 portfolio outcome 的多目标评价方式。它们可作为其他论文的评测组件或未来新题的基础设施，不足以单独支撑本候选。
4. 若未来重新提出相关新题，必须先取得真正 prospective 的组织控制意图数据，保持活动契约不变而操纵或测量 purpose，并以外部行动结果证明理论因子化在公平等参数比较中具有不可由 raw model、POMDP 或 direct outcome predictor 复制的能力。在这些条件出现之前，本结论不是 CONDITIONAL，而是 NO-GO。

## 12. 证据边界

本终审没有运行 CPTC 训练或 pilot，因此没有报告任何模型性能、显著性或因果效应。文中数字只来自已核验的公开论文或 `00T` 自身拟议规模。NO-GO 的依据是理论定义、识别设计、信息可得性、公开数据字段及通用替代模型的结构性反证，不是捏造的实验失败。
