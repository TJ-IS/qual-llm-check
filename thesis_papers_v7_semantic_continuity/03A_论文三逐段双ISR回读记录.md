# 论文三逐段双 ISR 回读记录

> 冻结源：ACAA = `28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md`；DSDL = `16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md`。

## 03A-001｜摘要｜“数据流水线即使保持可执行”

- 句子功能（7 句）：S1 界定可执行但语义失效的现象；S2 指出现有局部防线无法选择跨期动作；S3 定义 40,108,032 参数工件、隐藏真值/部署回执边界、冻结表征与候选条件标量 actor；S4 以单事件—模板轨迹为风险原子、至少 800 条 $H_{ej}$ 为 CVaR 分布并以至少 200 个事件 cluster 推断；S5 给出 50-event development、至少 200-event confirmation、四模板和 synthetic/world-model 边界；S6 列出基线、部署代理/隐藏语义指标与多个 continuation policy 下的最佳首动作；S7 收缩理论—计算贡献。
- 本段引文：摘要按目标期刊惯例不置文内引文；所有可证伪主张在正文展开并引用。
- ACAA 实读：第 29 行依次执行“既有研究—不足—新构念—专门机制—实证比较”功能；其摘要把四层注意构念直接映射到专门神经机制。
- DSDL 实读：第 27 行依次执行“应用价值—理论构念—三项方法能力—比较—解释分析”功能；第 31 行压缩关键词。
- 回读修订：保留七句闭环；统一 800 条事件—模板轨迹与 200-event cluster 推断，加入可见回执、candidate-conditioned actor 和隐藏语义外部效度边界。

## 03A-002｜引言第 1 段｜“现代分析、机器学习与公共服务”

- 句子功能（4 句）：S1 说明流水线价值条件；S2 以数据质量理论支撑适用性；S3 说明隐性依赖与漂移危害；S4 用五维例子界定核心现象。
- 引文功能与权威性：Wang and Strong、Lee et al. 为 Basket 数据质量构念/测量来源（C/M）；Sculley et al. 为机器学习系统技术债旗舰近邻（G）；Breck et al. 与 Polyzotis et al. 为生产数据校验和数据管理旗舰方法（G/M）。
- ACAA 实读：第 39 行先建立现象价值，第 41 行再展示直观方案为何偏误，第 43 行提出更贴近机制的观察视角。
- DSDL 实读：第 35、39 行从新型应用机会推进到可行动预测价值，第 41 行用信息缺失刻画挑战。
- 回读修订：末句保留五个具体转移，防止“语义演化”退化为空泛口号；以“可执行但不连续”形成全文张力。

## 03A-003｜引言第 2 段｜“已有工具分别覆盖了”

- 句子功能（4 句）：S1 以冒号合并场景导语和规则/校验/测试证据；S2 汇总合同、结构演化并限定 WIP 责任；S3 以四类动作的相反长期后果揭示共同缺口；S4 指明单次门控缺少路径状态。
- 引文功能与权威性：Schelter、Breck、Claessen、Gulzar 为可执行数据/程序检查旗舰方法（G/M）；Schuiki et al. 2026 仅按工作论文（WIP）承担数据合同邻近实践定位（G），不承担同行评议结论；Curino、Meurice and Cleve 为模式演化与传播直接近邻（G）。
- ACAA 实读：第 41 行按数据侧与模型侧拆开直观方案的不足；第 45 行用相互冲突的经验关系证明单一指标不稳健。
- DSDL 实读：第 43 行逐项说明相似任务为何不能迁移；第 47 行从理论可行性推进到动态状态的计算挑战。
- 回读修订：将批评限定为“通常回答”，避免稻草人；新增四种动作的相反跨期代价，建立序贯学习的必要性；按来源当前责任把 Schuiki et al. 2026 明标为 WIP，并收窄为邻近实践证据。

## 03A-004｜引言第 3 段｜“自适应系统研究提供了”

- 句子功能（5 句）：S1 引入反馈控制理论；S2 定位其在本问题中的未指定部分；S3 解释在线探索不可接受；S4 组合离线学习与尾部风险方法；S5 重述新问题。
- 引文功能与权威性：Kephart and Chess、Garlan、Cheng 为自适应系统旗舰来源（C/G）；Rawlings 为 MPC 权威专著、Sutton and Barto 为 RL 权威教材（M）；Levine、Kostrikov、Bellemare、Dabney 为离线/分布价值 RL 旗舰方法（M/G）；Rockafellar and Uryasev 为 CVaR 原始方法（C/M）。
- ACAA 实读：第 49、51 行将过程与粒度理论拆成计算维度，第 53 行以组件回应研究问题。
- DSDL 实读：第 49 行把动态、多视图与交互结构联结，第 51 行呈现两条计算路径及其冲突，第 53 行再合成为方法。
- 回读修订：明确“不可任意试错”是采用离线策略的因果理由；按成本方向把风险对象纠正为“完整轨迹损害分布的上尾”，以最坏 10% 损害而非均值奖励支撑风险敏感性。

## 03A-005｜引言第 4 段｜“据此，本文围绕同一个动态控制问题”

- 句子功能（7 句）：S1 把三个 RQ 限定为同一动态控制问题；S2 提出动态表示问题；S3 提出有支持限制的风险策略问题；S4 提出真实外推比较问题；S5 分开 POMDP 的隐藏 $Y$、可见 $o$ 与近似信息状态；S6 给出“世界模型先冻—$z/t/\eta$ 增广标量 IQL—固定风险权重—具体动作 ID”的对应；S7 声明操作化贡献与无结果边界。
- 引文功能与权威性：本段综合前文已引来源，不新增引文，避免 RQ 句被文献归属遮蔽。
- ACAA 实读：第 53 行先概括构念后提出 RQ 并立即给出组件；第 55 行解释每个组件如何响应动态行为。
- DSDL 实读：第 47、49、51 行每段采用“挑战—RQ—机制”的稳定对应，并将最后一个 RQ 指向联合损失。
- 回读修订：三个 RQ 分别绑定表示、学习、外推；以精确 RU 增广状态替换“分布价值 IQL”，保留固定风险权重而非对偶约束，并把动作单位落到参数化 action ID。

## 03A-006｜文献第 1 段｜“数据质量的”

- 句子功能（4 句）：S1 回溯情境数据质量；S2 引入规则适配与差异成本；S3 连接本体表征；S4 给出本文构念定义与反定义。
- 引文功能与权威性：Wang and Strong、Strong、Lee et al. 为 Basket 构念与测量（C/M）；Lee 2003 为 Basket 情境规则（D）；Heinrich、Cichy 为成本质量综述/方法（S/M）；Wand and Weber 为本体表征原始理论（C）；Burton-Jones and Grange 为 Basket 有效使用构念（C）。
- ACAA 实读：第 61、63、65、67 行围绕一个中介构念按数值、文本、图像证据逐层综述，并明确异质情境。
- DSDL 实读：第 57、59 行先划分渠道，再综合前因与触点，最后回扣研究任务。
- 回读修订：将连续性定义为“满足冻结谓词的能力”，并明确排除数值恒定，保持可证伪性。

## 03A-007｜文献第 2 段｜“生产数据系统已形成”

- 句子功能（4 句）：S1 以冒号合并校验链导语与 Deequ/TFDV/Data Linter 证据；S2 综述测试、差分与来源解释；S3 综述演化并把 Schuiki 2026 限定为 WIP 邻近项；S4 对照既有 unit 与本文“独立真实上游事件×受控下游模板×固定窗口”的混合回放 unit 和完整轨迹结果。
- 引文功能与权威性：Schelter、Breck、Hynes、Biessmann 为数据校验直接近邻（G/M/S）；Gulzar、Abedjan 为数据测试与错误检测直接近邻（G/S）；Cheney、Herschel 为来源追踪综述/方法（S/M）；Curino、Meurice、Schuiki、Dehghani 为演化、合同、数据网格近邻（G/D）。
- ACAA 实读：第 61、65、71、75 行按构念、数据形态、预测任务、动态扩展建立相邻流派之间的边界。
- DSDL 实读：第 63、67、69 行从传统特征和方法推进到多视图方法，再以标注依赖明确缺口。
- 回读修订：最后一句同时冻结准确的混合回放观察单位与动作后完整轨迹结果，避免把受控下游称为“真实流水线”；Schuiki 2026 再次限于 WIP 邻近定位。

## 03A-008｜文献第 3 段｜“自主计算以 MAPE-K 循环”

- 句子功能（5 句）：S1 综述反馈适配；S2 补充体系结构与恢复近邻；S3 引入时间展开能力；S4 区分普通故障状态与语义状态；S5 陈述本文的三项替换。
- 引文功能与权威性：Kephart、Salehie、Cheng、de Lemos、Garlan 为自适应系统旗舰/路线图（S/G）；Elmore、Cardellini 为在线重配置与弹性流处理近邻（G）；Boh、Tim and Leidner 为 2023 Basket 数字韧性构念（C），Duchek 为韧性能力综述（S）。
- ACAA 实读：第 75 行区分“时间特征”与真正动态效应；第 79、81 行区分理论注意与计算注意；第 85、87 行把综述缺口落实到不相容的计算函数。
- DSDL 实读：第 75、77、79 行用静态—动态、传统—深度、黑箱—理论三组对照收束缺口。
- 回读修订：明示 MAPE-K 是基线而非稻草人；用“相同差异、不同运行状态、不同动作”给出动态必要性的可测试反例；将数据库近邻收窄为文献实际支持的在线重配置，并以两篇 Basket 文献固定数字韧性的时间展开含义。

## 03A-009｜文献第 4 段｜“流水线天然是节点”

- 句子功能（5 句）：S1 说明时序图适配性；S2 综述图与时序图方法；S3 综述离线 RL 三层方法；S4 综述分布价值、损害上尾 CVaR 与 OPE；S5 把缺口限定为指定检索/公开评测边界内的操作化与评价交集，并排除对基础算子的新颖性主张。
- 引文功能与权威性：Kipf、Veličković、Xu、Rossi 为图/时序图旗舰方法（M/G）；Fu、Kumar、Kostrikov 为离线 RL 旗舰基准与算法（M/G/E）；Bellemare、Dabney、Rockafellar 为分布价值与 CVaR 原始/旗舰方法（C/M）；Precup、Jiang、Le 为 OPE 原始/旗舰方法（M）。
- ACAA 实读：第 79、81 行先定义方法能力再区分理论构念与计算机制；第 85、87 行以函数不相容而不是仅以“没人做过”构成缺口。
- DSDL 实读：第 69 行综述复杂输入方法，第 71 行解释动态构念为何要求特制损失，第 75 行收束组合缺口。
- 回读修订：统一使用“分布价值”，避免误读为多机训练；将 CVaR 方向固定为损害上尾；最后一句列出必须同现的五项操作化元素并声明不发明基础算子，避免无边界的“尚未有人做”主张。

## 03A-010｜文献第 5 段｜“概念漂移检测关注”

- 句子功能（4 句）：S1 界定漂移近邻；S2 界定修复与演化近邻；S3 用三个反例划界；S4 精确陈述未解决控制任务。
- 引文功能与权威性：Gama 为概念漂移综述（S），Rabanser 与 Lipton 为数据集/标签漂移旗舰方法（M/G）；Monperrus、Le Goues 为程序修复综述（S）；Curino 为模式演化方法（G）。
- ACAA 实读：第 85、87 行不止声称空白，而是指出既有函数与目标构念不相容；第 91 行把设计理据分成诱导、充分性、机制指导。
- DSDL 实读：第 75、77、79 行通过明确对照说明新方法做什么、已有方法少什么。
- 回读修订：增加“统计静默、测试通过、结构兼容”三个反例；把主问题固定为一个动态控制任务，不把三个子 RQ 写成三项独立研究。

## 03A-011｜理论第 1 段｜“表征理论要求系统构造”

- 句子功能（6 句）：S1 提供现实映射与有效使用基础；S2 把连续性定义为时间展开能力；S3 定义 evaluator-only 隐藏真值 $Y$、真实风险 $D^Y$ 与不含未来/真值的可见观测 $o$；S4 定义模型信念 $\hat Z,\hat U,\hat D$ 并禁止命名为 truth；S5 分开真实连续性 $C^Y$ 与政策保守估计 $\hat C$ 及单调性；S6 强调可计算、可证伪和 truth/belief 边界。
- 引文功能与权威性：Wand and Weber 为本体表征原始理论（C）；Burton-Jones and Grange 为 Basket 有效使用构念（C）；Boh 为 Basket 数字韧性构念、Duchek 为能力过程综述（C/S）。
- ACAA 实读：第 91 行要求理论指标能指导机制；第 93、95 行分别给出过程和粒度；第 100 行用反例说明为何选择所建构念。
- DSDL 实读：第 83、85 行从构念组成转向形成机制；第 87、89 行说明动态累积并压缩成两个计算任务。
- 回读修订：按 ACAA 第 91、93、95、100 行和 DSDL 第 83、85、87、89 行的“理论构念—过程—可计算分解”顺序，补入两条方向明确的单调性条件，并把 $Y$、$o$、$\hat Z/\hat U$、$C^Y/\hat C$ 全部分开，避免模型量与 evaluator truth 混用。

## 03A-012｜理论第 2 段｜“本文把环境严格写成有限时域”

- 句子功能（7 句）：S1 定义 $\mathcal M=(\mathcal X,\mathcal A,P,O,c,\rho_0,H)$、$H=24$、完整潜状态、具体动作全集与初始分布；S2 令观测核释放含成本、结算时间戳和状态的 $r_t$ 并定义近似 information state；S3 规定部署可见回执可重放累计量而隐藏 $Y$ 只供离线监督/事后评价；S4 定义至多 12 个稳定日志 ID、candidate-conditioned actor、受支持 feature-cell 新 ID 与 OOV/支持失败升级回退；S5 说明预算由 hard mask 实现而非对偶 CMDP；S6 给出相同合同差异、不同运行状态导致不同动作的反例；S7 用必要多样性把动态必要性限定为满足冻结资格和样本门槛的自然/受控 twins。
- 引文功能与权威性：Ashby 为必要多样性原始理论来源（C）；de Lemos et al. 与 Rawlings 支撑状态依赖的自适应与滚动控制（C/M）。其余符号继承前段已引理论。
- ACAA 实读：第 102、104 行从理论预期直接推到时间机制；第 106、108 行以既有函数不满足构念为冲突；第 118 行汇总理论—挑战—解法。
- DSDL 实读：第 91、93、95 行把三个理论难点逐一落到输入特征、跨视图机制与动态损失。
- 回读修订：在完整 POMDP 上补齐 deployment-visible receipt/timestamp，分开日志 ID 与 feature support，并把动态标签限定为共同支持动作上的多 continuation 真实轨迹。

## 03A-013｜理论第 3 段｜“设计科学贡献要求设计理据”

- 句子功能（3 句）：S1 给出设计理据标准；S2 建立 evaluator truth、可见信念、冻结世界模型、真实完整轨迹、受限动作、$z/t/\eta$ 增广上尾风险和运行情境的映射；S3 列出五维遮蔽、可达 twins、增广状态/固定风险项及无差异回退的可证伪预期。
- 引文功能与权威性：Hevner et al. 与 Gregor and Hevner 为 MISQ 设计科学核心来源（D）；Gregor et al. 为 JAIS 设计原则解剖（D）。
- ACAA 实读：第 118、120、122、124、126 行用总结、表题、表体、方法标题和方法导语把指标、理论、挑战、解法一一对应后才引出方法。
- DSDL 实读：第 99、103 行同样把三项目标与三项机制严格对齐；第 109 行给出端到端顺序。
- 回读修订：每个设计选择均附可失败的消融表现；用 $Y$ 对应事后测量、$o/\hat Z/\hat U$ 对应有限认知、真实完整轨迹对应动态能力，并以 $q_{0.90}$/严重失败率给出 CVaR 不能确认时仍可检验的风险表现。

## 03A-014｜方法第 1 段｜“每个时间步的可见观测冻结为”

- 句子功能（4 句）：S1 逐项冻结含上一回执值/时间戳/状态的 $o_t$，允许 $\hat Z/\hat U$ 并排除隐藏 $Y$ 和未来；S2 定义真实事件与双编码；S3 分开评价器生成的动作后隐藏 $Y$ 与部署运行器生成的可见 $o,r$；S4 说明三类编码、图构造及冻结的动作 feature 词表/缩放器/OOV 行。
- 引文功能与权威性：本段是本研究的输入协议，不依赖外部经验主张；相关编码方法在前文已引。
- ACAA 实读：第 130 行给端到端流，第 134、139 行定义样本与对齐，第 141、143 行冻结序列处理和张量。
- DSDL 实读：第 105、109 行先定任务与全流程，第 113、118、120、124 行再说明纳入、切分、掩码、嵌入。
- 回读修订：完整枚举含回执的 $o_t$，将隐藏语义监督/终局评价与部署可见观测/成本日志分开，并冻结 candidate feature 与 OOV 处理。

## 03A-015｜方法第 2 段｜“SC-Guard-40M 的实际可训练 checkpoint storage”

- 句子功能（5 句）：S1 给出 40,108,032 总账，并把 9 个实际一维 `float32` canonical flat-packed checkpoint storage tensor、控制块 $Q_1/Q_2/V/action-feature/actor$ 分账、非普通层边界及全部逻辑 view 的冻结 offset schema 落到 `03B_SC-Guard-40M参数清单.tsv`（规范化 SHA256 `AB899E8251076E1B777AB2862F143C23D07EC4B4B74AF3D306E7B6794BBF230E`）；S2 冻结 512 节点、12 边型、32-event history 与确定性三跳裁剪；S3 解释关系图与连续时间记忆；S4 定义 $p(o_{t+1},r_t\mid s_t,feat(a_t))$、event-cluster bootstrap 五头、$\hat Z/\hat U$ 校准及 time-out/source-out 覆盖；S5 分开隐藏 $Y$ 监督和部署可见观测/回执监督，并禁止世界模型产生 Bellman 样本。
- 引文功能与权威性：Veličković、Xu、Rossi 为图注意、TGAT、TGN 旗舰原始方法（M/G）。
- ACAA 实读：第 143、153 行先定义标准算子与掩码，第 173、187、189 行再以构念要求修改输入、兼容函数与时间项。
- DSDL 实读：第 148、150、152 行由双序列与交互关系导出跨视图机制；第 156、158 行把动态构念投影为逐时张量。
- 回读修订：控制块 6,012,928 被拆到候选 actor 所需的五个责任模块；新增实际 03B ledger，以 9 个只计一次的 flat-packed storage row 合计 40,108,032，以 19 个零计数 view row 冻结连续半开 offsets，并用规范化 SHA256 自证，未把 flat storage 冒充普通层张量。

## 03A-016｜方法第 3 段｜“动作 $a_t$ 执行后”

- 句子功能（7 句）：S1 定义只由部署可见 contract/run-time 量构成的物理缩放回执，并把隐藏语义移到外部效度；S2 以唯一 $\ell_t/z_{t+1}$ 公式纳入残余成本，令 $t=23$ 强制 done 并零成本吸收/补零；S3 给出单事件—模板 $H_{ej}$ 的 RU 终端损失与 $J$；S4 冻结 $\eta$ 网格并训练 action-feature 条件的双 Q、V 与 scorer；S5 给出下 expectile、done mask、detach、Polyak 且折扣只进 $z$ 一次；S6 定义动态候选 softmax、支持 mask、部署 argmax 与 ID tie-break；S7 用 development 四模板整窗事件等权目标一次选型，并排除短窗/合成/world-model Bellman 样本。
- 引文功能与权威性：Kostrikov 为 IQL 原始旗舰方法（M）；Dabney 为分位分布价值旗舰方法（M）；Rockafellar and Uryasev 为 CVaR 原始方法（C/M）。
- ACAA 实读：第 187、189、198、208 行解释每个式子中量的含义与交互，第 220、224 行闭合总体损失与算法顺序。
- DSDL 实读：第 187、189、195 行从标签困难导出定向约束并解释符号；第 199、205、207、208、213、215、216、219、221、224、227 行依次连接表示、局部目标、融合、总目标与训练责任。
- 回读修订：在原 RU 修正上进一步闭合可见 cost、$t=23$ 强制 done、残余成本唯一递推、candidate-conditioned actor 与单事件—模板风险单位。

## 03A-017｜方法第 4 段｜“具体动作由结果无关”

- 句子功能（5 句）：S1 枚举具体动作槽、稳定日志 ID、`NA` 规则、12-action cap 与结果无关截取；S2 限定 bounded patch 候选、全局 hash 和类别内无隐藏选择；S3 列允许模板、检查与升级边界；S4 定义共享外生序列下同时产出可见 $o,r$ 与隐藏 $Y$ 的真实核，并让各动作实付量先形成带时间戳回执；S5 冻结 OCI 执行并在 hybrid manifest 保存 $A_{sup}$、$t=23$、零填充和 $R_{res}$ 责任。
- 引文功能与权威性：本段是动作操作化协议，不新增外部引文。
- ACAA 实读：第 212、218 行把自适应权重限制在明确两类输入之间，第 220、224 行写清输出和训练顺序。
- DSDL 实读：第 213、216、219、221、224、227 行用融合导语、显式公式、参数解释、总目标和训练结果限制两条机制如何组合。
- 回读修订：保持有限具体 ID，同时把部署回执、隐藏评价日志、强制终止和残余成本规则纳入同一可复算执行 manifest。

## 03A-018｜方法第 5 段｜“SC-Guard-40M 从随机初始化”

- 句子功能（6 句）：S1 冻结跨篇独立性；S2 定义阶段 A 的主路径/短窗/合成训练、event-cluster bootstrap、互斥校准并永久冻结 representation、动作词表和世界模型；S3 以 `bellman_main`/sidecar 和 SHA256 键物理隔离行为六元 tuple，Q/V/actor 共享冻结表示但不得回传梯度；S4 冻结风险、$\eta$、图、OOV 与 $A_{sup}$ 的占用/计数/ESS 阈值；S5 定义外部 checkpoint 与短窗分叉销毁；S6 明确“物理表隔离 Bellman tuple—冻结 representation 共享编码”。
- 引文功能与权威性：本段为本研究训练和回放协议，不新增引文。
- ACAA 实读：第 220、224 行从总目标到训练算法，第 228、232、234、244 行定义样本时窗、动态因素、基线和重复评价。
- DSDL 实读：第 221、227 行总损失与算法闭环；第 231、233、237、239 行逐一冻结 unit、子集、基线与指标。
- 回读修订：新增 Bellman 专表、branch/synthetic/history 哈希排斥和冻结 representation 无梯度共享，闭合“共享表示不等于共享 Bellman 数据”。

## 03A-019｜设计第 1 段｜“事件库将从至少六类”

- 句子功能（5 句）：S1 列公开来源；S2 定义四项筛选、互斥 50-event development cohort 与至少 200 个独立事件的确认集；S3 定义五维各至少 30 个、事件只计一次与非结构变化要求；S4 明确训练/development/确认风险的原子结果都是四模板中的单个 $H_{ej}$，而切分与推断单位是事件；S5 以全部至少 800 个 $H_{ej}$ 形成 CVaR 分布、要求尾部至少 20 个不同事件，并用 $G_e=\max_jH_{ej}$ 辅助聚合事件严重度。
- 引文功能与权威性：NYC TLC、Citi Bike、MobilityData、UCI、NOAA、EIA 均为数据发布者或官方规范（E/I），用于证明数据可复现而非方法有效性。
- ACAA 实读：第 228、232 行给来源、时间和实例；第 234、244 行给多基线与重复评价。
- DSDL 实读：第 231、233 行明确一实例一观察单位及子集；第 237、239 行给比较族和评价协议。
- 回读修订：删除先取 $\bar H_e$ 的统计口径；800 条 $H_{ej}$ 进入确认 CVaR，200-event cluster 承担全部推断，$G_e$ 只作独立严重度辅助门。

## 03A-020｜设计第 2 段｜“数据按来源族、独立事件和时间”

- 句子功能（5 句）：S1 定义来源族—事件—时间三重隔离、四模板同折及不少于 120 time-out/80 source-out 的确认分层；S2 写死 synthetic/短窗只训练世界模型、IQL 只读真实行为主路径且各 cohort 互斥；S3 给出完全 world-model-free 的具体-ID 行为混合、12-action cap 与 $.05$ floor；S4 隔离未知倾向的 historical-observational 层；S5 以冻结 feature cell 定义 $A_{sup}$ 的倾向、独立事件计数、邻域占用、ESS、OOV 门，并允许 raw-new-ID 直接执行但排除 IQL/OPE。
- 引文功能与权威性：本段为防泄漏与 OPE 可识别性协议，方法依据已在 2.4 引用。
- ACAA 实读：第 228、232 行明确时间覆盖与动态因子，第 244 行说明 test fold 与重复估计。
- DSDL 实读：第 231、233 行说明样本构成，第 239 行明确结果来自未训练测试折及统计程序。
- 回读修订：在 world-model-free 倾向下界上区分日志 ID 与 learned feature support；新 ID 只可在受支持 cell 中直接评分，OOV/cell 失败回退升级，OPE 不借此冒充离线重叠。

## 03A-021｜设计第 3 段｜“执行分为两层”

- 句子功能（6 句）：S1 将可达检查点短窗全动作分支限定为 world-model-only；S2 定义 SC-Guard 以动态支持集 argmax、各冻结政策从同一 $C_{e,0}$ 完整运行；S3 拒绝无条件最优动作，在共同合法首动作上接续四个 continuation 并用 $\epsilon$-tie 集合报告一致与分歧；S4 封存未来；S5 定义隐藏 $Y$ 只检验部署代理的语义外部效度；S6 以隔离程序日志生成隐藏 $Y$ 与可见 $o,r$。
- 引文功能与权威性：本段为实验操作化，不新增引文。
- ACAA 实读：第 234、236、238、240、242、244 行把总体比较拆为输入、表示、时间序列、融合和多指标实验。
- DSDL 实读：第 237、239 行总比较与统计，第 243、249、267 行分别评价预测、表示和理论构念效用。
- 回读修订：进一步明确部署 actor 为确定性 argmax、首动作只取共同合法集、近似并列用冻结 $\epsilon$ 集合而非伪精确 argmin。

## 03A-022｜设计第 4 段｜“所有对比系统获得同一”

- 句子功能（5 句）：S1 冻结各基线共享输入、动作、预算、检查点、窗口、成本、kernel 与容器；S2 定义静态、runbook、MAPE-K 和可执行 `MPC-v1`，并冻结固定 $\eta$、同 RU 目标、beam/seed/ID tie-break；S3 定义算法消融；S4 排除未来并统一 512 次模型调用、单核 2 秒和 2 GB；S5 分开真实动作与模拟调用记账，并冻结 `MPC-v1` 代码、OCI、checkpoint 与搜索 manifest。
- 引文功能与权威性：Kephart and Chess 为 MAPE-K 原始来源（G）；Rawlings 为 MPC 权威来源（M）；Kumar、Kostrikov 为 CQL/IQL 旗舰原始方法（M）。
- ACAA 实读：第 234、236、238、240、242、244 行让基线共享基础架构并逐实验比较组件。
- DSDL 实读：第 237 行按方法家族选择 12 个对比，第 239、243 行统一折和输入。
- 回读修订：把“滚动 MPC”落实为可执行且哈希冻结的 `MPC-v1`，使其世界模型 checkpoint、搜索顺序、随机数、资源预算和 tie-break 均可复现。

## 03A-023｜设计第 5 段｜“令 $H_{ej}^{\pi}=\sum_{t=0}^{23}\gamma^t\ell_{ejt}^{\pi}$”

- 句子功能（5 句）：S1 以全部 $H_{ej}$ 定义确认风险分布，但让来源—时间切分和 2,000 次 bootstrap 始终按事件成块；S2 冻结至少 200 events、尾部 20 个不同事件、$G_e$ 严重度门与失败回退；S3 定义四个主 CVaR 对比、MPC 关键对比、Holm FWER、隐藏语义外部效度及 0.25 $H$ 精度门；S4 明确部署 argmax 目标政策、确认行为 cohort、五折事件级 cross-fitting、未截断 WIS/DR 公式和事件汇总；S5 以未截断 ESS/最大权重决定可推断性，把截断/winsor/FQE 限为敏感性并排除 raw-new-ID 等样本。
- 引文功能与权威性：Precup、Jiang and Li、Le 为重要性采样、双稳健与 FQE 旗舰方法（M）。
- ACAA 实读：第 244 行冻结重复、RMSE/MAE；第 248 行报告规则；第 290、292 行从训练模型导出构念解释分析。
- DSDL 实读：第 239 行主/稳健指标与检验；第 267、285 行单独验证动态构念和损失组件；第 297 行开启解释分析。
- 回读修订：确认 CVaR 改为 800-cell $H_{ej}$ 分布、200-event cluster 推断；OPE 明确确定性 argmax、五折 cross-fit、主分析不截断，截断只作敏感性，并冻结主比较、多重性与精度门。

## 03A-024｜设计第 6 段｜“机制检验将逐一遮蔽”

- 句子功能（5 句）：S1 定义构件消融并把 $\hat U$ 遮蔽与 twin 因果检验分开；S2 冻结 natural exact-match/caliper、controlled intervention 资格及各至少 40 个独立事件对；S3 要求共同支持动作至少两个、共享外生序列/CRN，以 $\epsilon=.10$ 最佳集和 $k=3$ of 4 continuation 定义动态切换；S4 定义 time-out/source-out 等稳健性及 200-event/20-tail-unit/$G_e$ 回退；S5 无论方向报告合格率和 3-of-4 通过率，并在 twins/MPC/runbook 不支持时收缩主张。
- 引文功能与权威性：本段直接检验前文已引理论和机制，不新增引文。
- ACAA 实读：第 290、294、296、310 行逐构件做解释分析，第 312、314 行逐项移除核心机制。
- DSDL 实读：第 285、295 行比较单损失与联合损失；第 301、311 行从时间和属性两维解释构念；第 315 行再归纳贡献。
- 回读修订：在自然/受控 twins 分离上补齐 eligibility、minimum N、common-action intersection、CRN、epsilon tie 与 3-of-4 判据。

## 03A-025｜贡献第 1 段｜“理论上，本文拟把数据质量”

- 句子功能（4 句）：S1 把理论贡献写成待检验延伸；S2 严格分开评价真值 $Y$ 与控制器信念 $\hat Z/\hat U$；S3 说明上下文改变支持内动作集、未来损害和 continuation-relative 最佳首动作；S4 要求自然/受控可达 twins 在多个 continuation 下共同支持动态解释，否则收缩为静态适配。
- 引文功能与权威性：Wang and Strong 为 Basket 数据质量构念（C）；Wand and Weber 为本体表征原始理论（C）；Ashby 为必要多样性原始理论（C）。
- ACAA 实读：第 318 行依次归纳构念、方法和经验知识贡献。
- DSDL 实读：第 315 行把方法贡献与构念随时间变化的经验问题连接。
- 回读修订：贡献使用条件式未来表达，明确 $Y$ 仅供评价、$\hat Z/\hat U$ 才进入控制；未把尚未运行的可达 twins 写成已经支持，也未把两篇 ISR 的监督预测发现冒充控制证据。

## 03A-026｜贡献第 2 段｜“方法贡献限定为 SC-Guard-40M”

- 句子功能（4 句）：S1 将贡献收缩为冻结 representation/world model、行为主路径标量 IQL、candidate actor 和部署可见代理风险；S2 以至少 800 条 $H_{ej}$ 为风险分布、事件 cluster 为推断单位并准确命名混合回放；S3 用逐张量/Bellman/hybrid manifest、动作 OOV 回退和冻结 `MPC-v1` 界定可复现边界；S4 只有部署代理与隐藏语义结果一致时才扩展使用价值，背离时收缩主张。
- 引文功能与权威性：本段归纳前文已引方法，不新增引文。
- ACAA 实读：第 318 行分别写构念、方法、经验贡献；第 335 行从工具、理解、迁移和平台四层谈使用意义。
- DSDL 实读：第 315 行先方法再知识贡献；第 329、331、333、335 行按预测、理论融合、动态构念、属性构念展开应用意义。
- 回读修订：方法增量进一步限定为候选 actor、可见代理、事件—模板风险和三类 manifest 的可复现实证集成，不把代理效果自动解释为隐藏语义效果。

## 03A-027｜贡献第 3 段｜“本研究有四类边界”

- 句子功能（5 句）：S1 说明公开动机遗漏与部署代理不能由隐藏 $Y$ 在线补救；S2 限定新日志 ID 仅在受支持 feature cell 中直接执行并退出 OPE，OOV/支持失败必须升级；S3 将 IQL/OPE 推断限定于倾向、占用、事件计数和 ESS 四门；S4 区分 development/confirmation、time-out/source-out、20-event 尾部门和精度不足回退；S5 冻结后续扩展必须保留的事件 cluster 推断及逐张量/Bellman/hybrid manifest。
- 引文功能与权威性：限制来自本研究设计，不新增引文。
- ACAA 实读：第 346 行压缩构念与方法，第 348 行逐项说明数据要求、遗漏变量、领域适配和粒度限制。
- DSDL 实读：第 339、341 行结论和迁移，第 343 行说明跨域、数据覆盖、参数与后续行为研究限制。
- 回读修订：边界现同时覆盖可见代理、raw-new-ID 跨 ID 泛化、feature support、未截断 OPE、20-event 双门与关键对比精度不足。

## 03A-028｜结论｜“上游语义演化的危险在于”

- 句子功能（4 句）：S1 重申形式成功但含义失效；S2 压缩隐藏 $Y$ 的监督/外部效度边界、含时间戳可见回执、冻结 representation/world model、隔离 Bellman 数据和 candidate actor 支持门；S3 总结至少 800 条 $H_{ej}$ 构成 CVaR 分布、至少 200-event cluster 推断及双 20-event 尾部门；S4 以代理/隐藏语义背离、未截断 OPE 失败、twins 3-of-4 失败或 MPC 无劣声明可证伪性。
- 引文功能与权威性：结论综合全文，不新增引文。
- ACAA 实读：第 346 行以问题—构念—机制—经验评价收束，第 348 行紧接边界。
- DSDL 实读：第 339 行以方法与真实案例收束，第 341、343 行说明迁移条件和限制。
- 回读修订：结论同步可见代理、candidate-conditioned argmax、800-cell CVaR/200-event 推断、raw-ID/OPE 边界和 twins 3-of-4 反证条件。

## 双 ISR 非空物理行证据表

下表为每个回读块指定一条实际重新打开并读取的非空物理行；“正文”与标题/公式/表格行分型，本表所用行均为正文行，16 位十六进制值是该物理行 UTF-8 字节的 SHA256 前缀，短锚点是原行开头的逐字片段而非释义。行号、类型、行哈希与锚点四者共同避免仅凭范围或标题虚构回读；完整源文件哈希见冻结项。

| 回读块 | ACAA 非空物理行 | DSDL 非空物理行 |
|---|---|---|
| 03A-001 | L29｜正文｜`312920DFA7BDBB8B`｜“Abstract. Although the impacts of he…” | L27｜正文｜`0BEB4FA0201DA702`｜“Abstract. As artificial intelligence…” |
| 03A-002 | L39｜正文｜`5C0F0CE72D217889`｜“Online reviews (reviews for short he…” | L35｜正文｜`54A3ABE58624EDBE`｜“The sustained development of digital…” |
| 03A-003 | L41｜正文｜`0849E20482692DAC`｜“As many studies have shown substanti…” | L43｜正文｜`EFCB9F0D1CFFAE1B`｜“Prior research studies prediction ta…” |
| 03A-004 | L49｜正文｜`8A2A35F13B00A69C`｜“From a spatial perspective, we, conf…” | L49｜正文｜`F98D64E5F7532AE2`｜“As for customer experience, we model…” |
| 03A-005 | L53｜正文｜`32514C8D3271CB38`｜“Overall, our induced indicators of c…” | L51｜正文｜`2F67A5246449F0DE`｜“Given the constructed customer exper…” |
| 03A-006 | L61｜正文｜`5935D647CA0C664B`｜“The reason reviews can impact produc…” | L57｜正文｜`243F816C13610F78`｜“Advances in social media and artific…” |
| 03A-007 | L71｜正文｜`1698B1D17D62993A`｜“Sales has been conventionally predic…” | L63｜正文｜`D8FC11C254CC303B`｜“Predicting customer response to mark…” |
| 03A-008 | L75｜正文｜`911482EEAB9CF601`｜“There have also been some studies th…” | L75｜正文｜`4C81DB1BF6EE7581`｜“Our review of existing related studi…” |
| 03A-009 | L79｜正文｜`A679144A27D14F33`｜“Attention mechanism, an important co…” | L69｜正文｜`C5C6E10077184ED0`｜“With the rise of omnichannel interac…” |
| 03A-010 | L85｜正文｜`34F4545A6A76B1D9`｜“Our review of related studies pinpoi…” | L75｜正文｜`4C81DB1BF6EE7581`｜“Our review of existing related studi…” |
| 03A-011 | L91｜正文｜`214862D33FA3DD2E`｜“Our aim in this study is to better l…” | L83｜正文｜`612E8E72BDDC5A37`｜“Extant research shows that customers…” |
| 03A-012 | L102｜正文｜`EC0D9FCC3CB3D5BA`｜“(1) Timeliness Attention. The dual-p…” | L91｜正文｜`4E2A97021EFE30A6`｜“However, solving this problem is met…” |
| 03A-013 | L118｜正文｜`A581950AC51D8C2F`｜“In summary, leveraging customer atte…” | L99｜正文｜`A0DFAEC4A0039EDD`｜“Our theoretical analysis lays a foun…” |
| 03A-014 | L130｜正文｜`1971A1993AC7C018`｜“Figure 2 outlines the framework of D…” | L109｜正文｜`4209A93E6D68EAF3`｜“Figure 1 outlines the framework of D…” |
| 03A-015 | L143｜正文｜`859D0D3B991F47F1`｜“To better present the padding mask o…” | L148｜正文｜`19D5D0328677C3B3`｜“To model customers’ experiences, we …” |
| 03A-016 | L187｜正文｜`EB01AA3399A64749`｜“where $\overline { { r } } _ { j }$ …” | L187｜正文｜`B50537C1165E02E6`｜“Because there are no ground-truth la…” |
| 03A-017 | L212｜正文｜`B40D1593922C7DC1`｜“4.4.4. Adaptive AMI. After obtaining…” | L213｜正文｜`5E114A422FB82EB9`｜“Having obtained both the cumulative …” |
| 03A-018 | L220｜正文｜`852D8DE5C4868801`｜“Finally, DTV-AMI takes a global aver…” | L221｜正文｜`618522A3C6E3344D`｜“Overall, the optimization objective …” |
| 03A-019 | L224｜正文｜`BCE9387054E4A71B`｜“Figure C1 (in Online Appendix C) out…” | L231｜正文｜`01470AE40DD87DD1`｜“We have evaluated DSDL in the case s…” |
| 03A-020 | L228｜正文｜`A18D01F6919FEF28`｜“For empirical evaluation in the case…” | L233｜正文｜`D272C7FA20D4ABA2`｜“We conducted experiments based on fo…” |
| 03A-021 | L232｜正文｜`9F93FEABEA0BFDDB`｜“Although our main objective in this …” | L237｜正文｜`ECA6A2D09464A945`｜“Based on each of the four data sets,…” |
| 03A-022 | L234｜正文｜`4FFD53776F2AAC08`｜“First, through two experiments, we c…” | L237｜正文｜`ECA6A2D09464A945`｜“Based on each of the four data sets,…” |
| 03A-023 | L244｜正文｜`B9146047A0EF5DE4`｜“For each setting in the four experim…” | L239｜正文｜`28795530691FAF7C`｜“For each setting in the experiments,…” |
| 03A-024 | L290｜正文｜`9B4827F424A67D3A`｜“After being trained with the real sa…” | L285｜正文｜`7FBECA5DCBF751AD`｜“5.3.4. Experiment 4: Prediction Perf…” |
| 03A-025 | L318｜正文｜`9084640FFF9A48A9`｜“This study makes several contributio…” | L315｜正文｜`21F0421C2C85DE81`｜“The main contribution of this study …” |
| 03A-026 | L335｜正文｜`9DE21083B1BC1FCF`｜“The proposed method (DTV-AMI) has pr…” | L331｜正文｜`CF3D0DBA30B302BE`｜“2. Implications from leveraging theo…” |
| 03A-027 | L348｜正文｜`28D6A843A9002E82`｜“Our work has some limitations, which…” | L343｜正文｜`AC7740D8C5877245`｜“Our work has several limitations, wh…” |
| 03A-028 | L346｜正文｜`C6D24BD246D525EE`｜“Whereas many studies have concentrat…” | L339｜正文｜`5BBF56376178086A`｜“We propose a theory-driven deep lear…” |

## 机械核验与冻结

- **段落与严格句表闭合：** 正文共有 28 个实质段落（摘要 1、引言 4、文献 5、理论 3、方法 5、设计 6、贡献与边界 3、结论 1），对应 03A-001 至 03A-028 共 28 个唯一连续回读块；按 `。！？` 切句的逐段句数向量为 `[7,4,4,5,7,4,4,5,5,4,6,7,3,4,5,7,5,6,5,5,6,5,5,5,4,4,5,4]`，总和严格为 140，每块“句子功能”均逐一覆盖 S1 至 Sn，块首短语与正文匹配，标题、关键词和逐条书目不冒充段落。
- **双 ISR 物理行闭合：** 28 个块各含 ACAA 与 DSDL 的功能回读记录，并在证据表各指定一条真实非空正文物理行；每条均同时记录行号、行型、UTF-8 物理行 SHA256 前缀和逐字开头锚点，逐项复算不一致数为 0。ACAA 冻结源共有 548 个物理行、294 个非空行；DSDL 冻结源共有 525 个物理行、283 个非空行。
- **文献闭合：** 书目含 66 篇独立来源，66 篇均在正文使用，使用率 100%；其中正文按书目首作者直接匹配 64 篇，另两篇以冻结别名 `NYC TLC 2026` 与 `U.S. EIA 2026` 匹配。Basket 来源共 9 篇；Fu 2020、Levine 2020、Rossi 2020 为 3/66 篇预印本（4.5%）且不承担核心理论责任，Schuiki 2026 另明确标为 WIP，只承担邻近实践定位。
- **引文密度：** 按正文实质段落、句末 `。！？` 切句，并以句内含作者—年份括号判定，正文共 140 句，35 句含引文（25.0%），含 104 个作者—年份键，即每百句 74.3 键。分区为：摘要 7/0，引言 20/7（35.0%），文献综述 22/14（63.6%），理论 16/5（31.2%），方法 27/3（11.1%），设计 31/4（12.9%），贡献与边界 13/2（15.4%），结论 4/0。
- **冻结设计项：** 机械搜索确认正文含完整 POMDP 七元组、隐藏 $X/Y$、含 `receipt/timestamp/status` 的可见观测、近似 $s=\phi(h)$、有限动作与动态 candidate scorer；成本只取 deployment-visible contract/run-time 量，$t=23$ 强制 done，$R_{res}$ 只经唯一 $z$ 公式进入，隐藏 $Y$ 只作世界模型监督与语义外部效度。世界模型/representation 先训后冻，`bellman_main` 与分支数据物理隔离；`03B_SC-Guard-40M参数清单.tsv` 以 9 个实际 flat-packed storage row 和 19 个 offset-view row 给出 checkpoint key/storage shape/numel/owner/role/alias_group，唯一计数合计 40,108,032，规范化 SHA256 为 `AB899E8251076E1B777AB2862F143C23D07EC4B4B74AF3D306E7B6794BBF230E`，$A_{sup}$ 冻结 feature-cell 倾向/事件计数/占用/ESS/OOV 门，raw-new-ID 只可直接执行并退出 OPE。确认 CVaR 使用至少 800 条 $H_{ej}$，所有推断以至少 200-event cluster 成块并设两个 20-event 尾部门；OPE 明确部署 argmax、五折事件 cross-fit、未截断主分析与仅敏感性截断，主比较、Holm 与精度门冻结。自然/受控 twins 另冻结 eligibility、$N_{nat}/N_{ctl}\ge40$、共同动作、CRN、$\epsilon=.10$ 与 3-of-4 规则；`distributional IQL|oracle|No-Go|资源门|资源签名|内部审计` 命中数为 0。
- **冻结校验：** 正文 SHA256 `E0FA11D20C53F2D9D7CA8B07F6428BDC318A32D3215A99B0BFD26577CF52325A`；03B 规范化 SHA256 `AB899E8251076E1B777AB2862F143C23D07EC4B4B74AF3D306E7B6794BBF230E`；ACAA 冻结源 SHA256 `22874E02E5DE71421110476BFC4B8E15FC80F86A1175D81A4FA3FCE7DF746239`；DSDL 冻结源 SHA256 `1954CA69FF5750C7C8A0CD594C7772FABE9B9F69F84F253120D39DFC85259A2B`。
- **03A 规范化哈希：** `83E9A433FC2CFDCCD572A2D462F66DD73F9C5A461CA26097EF7667FCD2CFA7DC`；算法为 UTF-8 解码、统一行尾为 LF、删除本条整行、保留其余内容与最终 LF 后计算 SHA256，故本条可自证而无自引用悖论；文件最终物理 SHA256 由交付回执报告。
