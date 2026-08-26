# 三研究 Introduction：逐句对照 RADAR 写作协议审计（v7）

- 版本：v7，2026-08-18
- 修订说明：RADAR Introduction 为**五段**结构——P1 背景与价值、P2 问题、P3 理论动机一（RO）、P4 理论动机二（RL）、P5 工件与评估。v6 曾将 P3/P4 合并为四段，v7 已按五段重写全部内容、审计表与附录。
- 目的：按写作协议重写三篇论文的 Introduction——**不是提取结构再填充，而是写完一段后逐句与 RADAR 原文对比**，严格核查是否达到原文的写作逻辑：引用文献的支持作用、句与句的联系、各段落的意义、标点符号与句式使用。不照抄原文，重在掌握顶级期刊表述的严谨性精髓（简明扼要地体现研究意义）。
- 审计基准：RADAR（Ebrahimi et al. 2025, MISQ）Introduction 全文五段共 36 句的逐句功能标注，见文末附录。
- 每篇结构：重写稿（P1–P5）→ 每段后的逐句审计表 → 研究问题。
- 证据纪律：有公开出处的数字直接给出（SWE-bench 65–80%、SWExploit ASR 0.91、QueryIPI 87%、IssueTrojanBench 66.5%、Autonomy Tax 99% vs 13%、MOCHA +32.4pp、MalSkillBench 3,944）；无出处的用【占位】标注，不编造数据。
- 引用编号说明：#25/#28/#30/#32/#11/#26 为 51 篇清单中的文献编号，正文暂以编号占位，最终排版替换为具体作者-年份。

## 写作协议（执行标准）

1. 写一段 → 2. 逐句对标 RADAR 对应段落 → 3. 核查五个维度：(a) 引用文献在句中的支撑作用；(b) 句与句的联系（推进、转折、例证、归纳）；(c) 段落整体的意义与功能；(d) 标点符号使用（破折号定义、括号证据、分号并列等）；(e) 句式结构（长句从句、连接词位置）→ 4. 判定"达标/调整"，不达标立即修订 → 5. 全段完成后整体复读，确认段落功能与 RADAR 一致。

---

## 研究一（AttackRL-Agent：编码智能体对抗攻击仿真）

### P1 重写稿（对标 RADAR P1：背景与价值）

随着大语言模型（LLM）在软件工程中的快速普及，编码智能体（coding agent）被开发出来，将缺陷定位、补丁生成与测试执行等环节自动化（Jimenez et al. 2024；Fan et al. 2023）。编码智能体已展现出在仓库级任务上的自主能力，能够理解 issue、修改代码并运行测试（Jimenez et al. 2024）。新一代智能体通过检索、工具调用与执行反馈的循环，已能完成跨文件的多步骤修改（Yang et al. 2024；Wang et al. 2024）。例如，在公开基准 SWE-bench Verified 上，领先智能体的问题修复率已从早期不足 10% 提升至 65%–80%（Jimenez et al. 2024）。如今，GitHub、OpenAI、Anthropic 等厂商正把编码智能体织入开发者的日常工作流，用于缺陷修复、功能实现与代码评审。例如，GitHub 已将 Copilot 的自动修复建议整合进拉取请求流程；OpenAI 与 Anthropic 发布了可独立运行数小时、自主修改多个仓库文件的编码智能体（Codex、Claude Code）。一项面向企业开发者的调查显示，大多数受访者认为缺少编码智能体将显著拖慢软件交付速度（【占位：调查出处】）。

### P1 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 随着…，编码智能体被开发出来，将…自动化 | P1-S1："With the recent increase in the scale and severity of cyber attacks, AI agents have been developed to automate cyber defense…"（趋势状语从句+现象主句） | Jimenez 2024（SWE-bench）、Fan 2023（LLM4Code 综述）：领域权威文献，定位研究场域 | 开篇定位：现象出现 | "随着…，…被开发出来"镜像 "With…, …have been developed to…" | 达标 |
| 2 | 编码智能体已展现出…自主能力 | P1-S2："…have demonstrated the ability to effectively detect and remediate threats…"（能力主张） | Jimenez 2024：能力证据 | S1→S2：出现→能力 | "已展现出…的能力"对应 "demonstrated the ability to" | 达标 |
| 3 | 新一代智能体通过…循环，已能完成…多步骤修改 | P1-S3："New AI agents, including deep neural networks, have shown promise in…"（技术 promise） | Yang 2024（SWE-agent）、Wang 2024（OpenHands）：新一代方法代表 | S2→S3：能力→技术手段 | "通过…的循环"定语说明技术机制 | 达标 |
| 4 | 例如，…65%–80% | P1-S4："For instance, …96% precision…"（数字实例） | Jimenez 2024：公开榜单数字可查 | S3→S4：例证 | "例如，"；数字括注出处 | 达标（数字为公开榜单区间，标注为区间而非伪造精度） |
| 5 | 如今，…正把编码智能体织入…工作流 | P1-S5："Today, leading cybersecurity and IT firms are weaving AI-enabled cyber defense into their operational fabric…"（产业采用） | 无引用（产业事实句；RADAR 此处亦无引用） | S4→S5：能力→采用 | "如今，…织入…"镜像 "Today, …weaving…fabric" | 达标 |
| 6 | 例如，GitHub 已将…；OpenAI 与 Anthropic 发布了… | P1-S6/7："For example, Avast and Symantec…"; "Endgame uses gradient boosting trees…"（两实例） | 厂商公开产品与文档（可查证） | S5→S6：采用→实例 | "例如，…；…"分号并列两实例；RADAR 用两句，我合并为一句内两分句（信息量对称、节奏相当） | 基本达标；合并理由：两实例同属"厂商集成"一档，分号并列不破坏逻辑 |
| 7 | 一项面向企业开发者的调查显示… | P1-S8："A large-scale international survey of IT firms revealed that 69% of them believe they cannot accomplish…without AI agents"（依赖加深） | 【占位：真实调查出处】 | S6→S7：实例→依赖（段落收束，为 P2 转折蓄力） | "一项…调查显示…"镜像原文；不编造 69% 式数字 | 达标（占位待补真实调查） |

段落意义核查：P1 完成"现象→能力→技术→实例→采用→实例→依赖"七步递进，与 RADAR P1 同构；末句落在"依赖加深"，为 P2 的 However 转折蓄力。✓

### P2 重写稿（对标 RADAR P2：问题）

然而，编码智能体已被发现易受对抗性操纵——对手精心构造的信息输入，诱导智能体执行本不该执行的动作（Greshake et al. 2023；OWASP 2024）。编码智能体并非例外：其输入面横跨 issue 文本、仓库文件、工具描述与技能包，任一通道都可被操纵（【恶意技能包文献】）。例如，一个看似普通的恶意 issue 可诱导自动修复智能体生成"功能正确但带漏洞"的补丁——对手先改写问题描述使其看似无害，再附加看似合理的测试用例，使补丁通过验证却可被利用（SWExploit：ASR 0.91）。再如，向工具描述注入指令可操纵智能体的工具选择——对手通过篡改工具 schema，诱导智能体调用具有危险权限的操作（QueryIPI：ASR 从约 50% 提升至 87%）。两种情况下，对手都是通过对智能体输入进行一步步精细、难以察觉的修改来构造攻击（Greshake et al. 2023）。编码智能体对信息操纵的脆弱性已被视作自主软件开发的新兴威胁，产业证据包括编码智能体的远程代码执行漏洞（Claude Code 系列 CVE，含 CVSS 9.8）与超过 3,900 个公开恶意技能包（MalSkillBench）。虽然编码智能体日益被依赖以维护生产代码，但关于如何系统地生成多样化、可迁移的对抗攻击序列，目前知之甚少。

### P2 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 然而，…易受对抗性操纵——对手精心构造的信息输入，诱导… | P2-S1："However, AI agents have been found to be vulnerable to adversarial attacks—adversarial data inputs meticulously modified by an adversary to mislead the AI agent"（转折+定义） | Greshake 2023（间接提示注入）、OWASP 2024（LLM Top 10）：定义来源 | P1→P2：价值→脆弱（However） | "然而，"转折；破折号内嵌定义（主词—同位语展开），句式与原文一致 | 达标 |
| 2 | 编码智能体并非例外：其输入面横跨… | P2-S2："Cyber defense AI agents are no exception (Apruzzese et al., 2019)."（对象收窄） | 【恶意技能包文献】：输入面证据 | S1→S2：普遍脆弱→本文对象不例外 | 保留 "并非例外" 短句内核，冒号后补充输入面（情境必要信息：输入面即研究一动作空间基础） | 达标（有意识扩展：原文此句无展开，我加冒号展开一句，因编码智能体的多通道输入面必须向读者交代） |
| 3 | 例如，恶意 issue…带漏洞的补丁——先改写…再附加… | P2-S3："For instance, a previously known malicious executable could be modified to evade…by first changing the signature section and subsequently resetting the file checksum."（实例1，步骤化） | SWExploit：ASR 0.91（公开基准） | S2→S3：例证1 | "例如，"；破折号后"先…再…"镜像 "by first…and subsequently…" | 达标 |
| 4 | 再如，工具描述注入…——通过篡改工具 schema… | P2-S4："As another example, malicious network packets could be modified…by performing encoding followed by fragmentation."（实例2） | QueryIPI：ASR 87%（公开基准） | S3→S4：例证2 | "再如，"镜像 "As another example" | 达标 |
| 5 | 两种情况下，对手都是通过…一步步精细、难以察觉的修改… | P2-S5："In both cases, an adversary crafts adversarial inputs by taking steps of meticulous and hard-to-notice changes…"（共性归纳） | Greshake 2023：归纳依据 | S3–S4→S5：两实例→共性 | "两种情况下，…"；"精细、难以察觉"对应 "meticulous and hard-to-notice" | 达标 |
| 6 | …已被视作…新兴威胁，产业证据包括… | P2-S6："The vulnerability…is construed as an emerging threat to autonomous cyber defense (Goosen et al., 2018)."（威胁定性） | Claude Code CVE、MalSkillBench：公开事件（比原文单篇引用更强） | S5→S6：共性→威胁升维 | "已被视作…新兴威胁"镜像 "is construed as an emerging threat"；逗号后以短句列举证据（原文用括注，我改用短句，因需容纳多个事件） | 达标 |
| 7 | 虽然…日益被依赖…，但关于如何…目前知之甚少 | P2-S7："While…are increasingly relied on…, little is known about strengthening the robustness…"（gap 句） | 无（gap 自指） | S6→S7：威胁→缺口（段落收束） | "虽然…，但…知之甚少"镜像 "While…, little is known about…"；保持单句简洁、无内嵌破折号（同原文） | 达标 |

段落意义核查：P2 完成"转折→定义→对象→两实例→归纳→定性→gap"七步，与 RADAR P2 同构；实例给出攻击机制（步骤化）与公开数字；gap 句落在"攻击生成"这一具体缺口（对应本文贡献）。✓

### P3 重写稿（对标 RADAR P3：理论动机一——为什么需要系统化攻击仿真）

在本研究中，我们旨在利用强化学习（RL）系统生成编码智能体的对抗攻击，以支撑其鲁棒性的度量与训练。对抗鲁棒性文献提供了一个严格框架，将对手的效应纳入智能体评估与训练过程的优化之中（Madry et al. 2018）。该框架促进对手与智能体之间的两玩家博弈：鲁棒性度量要求对手最大化危害，防御训练要求智能体最小化危害（Madry et al. 2018）。在编码智能体情境中，该框架引入一个生成上下文操纵攻击的对手，并利用这些攻击评估与训练智能体。由此，对抗鲁棒性文献确立了系统化的攻击仿真（AAE）是度量与提升编码智能体鲁棒性的前提（Kolter & Madry 2018）。

### P3 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 在本研究中，我们旨在利用 RL 系统生成… | P3-S1："In this study, we aim to strengthen…by leveraging the theories of RO and RL."（目的句） | 无（目的自指） | P2→P3：gap→回应 | "在本研究中，我们旨在…"镜像原文目的句 | 达标 |
| 2 | 对抗鲁棒性文献提供了一个严格框架，将对手的效应纳入…优化之中 | P3-S2："RO provides a rigorous framework to incorporate the effect of an adversary in the optimization process…"（理论定义） | Madry et al. 2018：minimax 框架奠基 | 目的→理论：为什么需要攻击 | "提供了一个严格框架"镜像 "provides a rigorous framework" | 达标（有意识替换：RO→对抗鲁棒性 minimax 框架。研究一不做防御优化，理论根基改为"鲁棒性度量与训练"这一一般框架，句法功能不变） |
| 3 | 该框架促进对手与智能体之间的两玩家博弈：… | P3-S3："This framework promotes a two-player game between the adversary and the AI agent (Madry et al., 2018)."（博弈性质） | Madry et al. 2018：博弈 | 定义→性质 | "该框架促进…两玩家博弈"镜像 "This framework promotes…"；冒号后展开博弈两侧（度量侧/训练侧），对应原文未展开的博弈含义 | 达标 |
| 4 | 在编码智能体情境中，该框架引入一个生成上下文操纵攻击的对手… | P3-S4："In the cyber defense context, RO introduces an adversary who generates evasive adversarial attacks and trains an AI agent that learns from these attacks…"（情境实例化） | 无 | 性质→情境 | "在…情境中，该框架引入…"镜像 "In the cyber defense context, RO introduces…" | 达标 |
| 5 | 由此，…确立了系统化的 AAE 是…前提 | P3-S5："As such, RO establishes that robust defense requires effective adversarial attack emulation (AAE) (Kolter & Madry, 2018)."（推论句） | Kolter & Madry 2018：AAE 依据 | 情境→推论（段落收束，为 P4 的 RL 铺垫） | "由此，…确立了…"镜像 "As such, …establishes…"；把"鲁棒防御要求 AAE"改写为"度量与提升鲁棒性要求 AAE"（研究一的服务对象） | 达标 |

段落意义核查：P3 完成"目的→理论定义→博弈性质→情境实例化→AAE 推论"五步，与 RADAR P3 完全同构；差异仅在理论名称（对抗鲁棒性框架而非 RO），因研究一的服务对象是"度量与训练"而非"防御优化"。✓

### P4 重写稿（对标 RADAR P4：理论动机二——为什么 RL 恰好适配）

由于对编码智能体的攻击通常涉及一串动作——修改 issue 文本、注入仓库文件、篡改工具描述——攻击仿真可以从建模对手的逐步动作中获益（SWExploit；QueryIPI）。RL 专门研究行动者（如对手）与环境（如配备编码智能体的软件仓库）在离散时间步上的序贯交互（Sutton & Barto 2018）。RL 因而非常适合仿真对手构造攻击时采取的动作序列。此外，RL 捕获的动作序列有助于洞察对手的策略模式，为检测特征设计（研究二）与防御训练（研究三）提供素材（Anderson et al. 2018）。

### P4 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 由于…攻击通常涉及一串动作——…——攻击仿真可以从建模…中获益 | P4-S1："As adversarial attacks often involve taking a sequence of actions…, AAE can benefit from modeling the steps taken by the adversary…"（攻击序贯性） | SWExploit/QueryIPI：动作通道实例 | P3→P4：AAE 需要→攻击的序贯性 | "由于…，…可以从…中获益"镜像 "As…, AAE can benefit from…"；双破折号列举三通道 | 达标 |
| 2 | RL 专门研究行动者（如对手）与环境（如…）在离散时间步上的序贯交互 | P4-S2："RL specializes in examining the sequential interaction of an actor (e.g., adversary) with the environment (e.g., IT infrastructure…) over discrete time steps (Sutton & Barto, 2018)."（方法定义） | Sutton & Barto 2018：定义权威 | S1→S2：序贯性→RL 定义 | 括号举例 "（如对手）…（如…）"镜像 "e.g., …" | 达标 |
| 3 | RL 因而非常适合仿真…动作序列 | P4-S3："RL is thus well-suited for emulating the steps (i.e., the sequence of actions) an adversary takes…"（适配结论） | 无（推论） | S2→S3：定义→适配 | "因而非常适合"镜像 "is thus well-suited for" | 达标 |
| 4 | 此外，…洞察对手的策略模式…（研究二）（研究三） | P4-S4："Additionally, the sequence of actions captured by RL is useful for gaining insights into the adversary's strategies and further enhancing the cyber defense AI agent (Anderson et al., 2018)."（附加价值） | Anderson et al. 2018：序列动作的洞察价值 | S3→S4：适配→附加价值 | "此外，"镜像 "Additionally"；"为…提供素材"对应 "useful for…enhancing"；加"研究二/三"为系列关联服务 | 达标（系列钩子是情境必要信息） |

段落意义核查：P4 完成"序贯性→方法定义→适配→附加价值"四步，与 RADAR P4 完全同构。✓

### P5 重写稿（对标 RADAR P5：工件与评估）

基于计算设计科学范式，我们开发 AttackRL-Agent——一个基于 RL 的编码智能体对抗攻击仿真框架，用于生成多样化、可迁移的攻击序列，支撑鲁棒性度量与防御训练。AttackRL-Agent 自动发现有效的攻击序列，并暴露编码智能体的脆弱点。具体地，该框架将攻击建模为对抗 MDP：状态由仓库、issue 与轨迹摘要构成；动作空间覆盖 issue 改写、文件注入与工具描述篡改三类通道；奖励为危害信号减去隐蔽性惩罚，并以 PPO 训练生成式攻击策略。鉴于上下文操纵是编码智能体面临的主要威胁（Greshake et al. 2023），我们将框架实例化到 SWE-bench Verified 与 AgentDojo 两类公开环境，与静态模板攻击（SWExploit、FCV）及通用 RL 越狱方法（RLbreaker）等基准比较，评估攻击成功率（ASR）、隐蔽性、多样性与跨模型可迁移性。我们的实验显示，AttackRL-Agent 显著提升了攻击成功率，并生成了静态模板无法覆盖的攻击模式（【占位：待实验数据】）。总体而言，本研究作出三点贡献。第一，我们提出一个面向编码智能体的攻击仿真框架；据我们所知，这是首个以 RL 建模编码智能体对抗操纵博弈的攻击仿真框架。第二，我们开发一种新的 RL 方法生成攻击动作序列；除超越现有静态模板与通用越狱方法外，该方法提供了对编码智能体脆弱点的可操作洞察。第三，我们产出一个公开可复用的攻击库，供检测与鲁棒化研究（研究二、三）使用，并为安全从业者提供度量智能体鲁棒性的测试基线。

### P5 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 基于计算设计科学范式，我们开发 AttackRL-Agent——… | P5-S1："Drawing on the computational design science paradigm, we leverage RO and RL to develop a novel RL-based adversarial attack robustness (RADAR) framework…"（范式+命名） | 无（范式声明） | P4→P5：动机→工件 | "基于计算设计科学范式，我们开发…"镜像原文；破折号引出命名与定位 | 达标 |
| 2 | AttackRL-Agent 自动发现…并暴露… | P5-S2："RADAR discovers effective adversarial attacks and prepares cyber defense AI agents to remediate them."（功能概述） | 无 | S1→S2：命名→功能 | "自动发现…并暴露…"镜像 "discovers…and prepares…" 对仗结构 | 达标 |
| 3 | 具体地，…对抗 MDP：状态…；动作空间…；奖励… | P5-S3："Specifically, RADAR offers a novel RL approach to emulate…and presents a novel RL-based RO formalization to strengthen…"（组件展开） | 无 | S2→S3：功能→机制 | "具体地，"镜像 "Specifically"；分号并列 MDP 三要素（原文以 and 连接两组件，我以分号列表，因 MDP 定义需三要素并置） | 达标 |
| 4 | 鉴于…是…主要威胁，我们将框架实例化到…，与…基准比较，评估… | P5-S4："Given that malware attacks are the leading threat to IT infrastructure (Bissell et al., 2019), we instantiate our RADAR framework…, evaluate the effectiveness…against state-of-the-art…benchmark methods, and present the utility…"（实例化理由+评估） | Greshake 2023：实例化理由 | S3→S4：机制→实例化与评估 | "鉴于…，我们…实例化…，与…比较，评估…"镜像 "Given that…, we instantiate…, evaluate…against…" 长句 | 达标 |
| 5 | 我们的实验显示，…（【占位：待实验数据】） | P5-S5："Our experiments showed that RADAR increased the robustness…by seven times, on average…"（结果预告） | 无（自身结果） | S4→S5：评估→结果预告 | "我们的实验显示，…"镜像原文；数字占位、不编造 | 达标（占位） |
| 6 | 总体而言，本研究作出三点贡献。第一，…；据我们所知，这是首个… | P5-S6/7/8："Overall, this study makes three major contributions. First, we propose…To our knowledge, this is the first…"（贡献总起+贡献1+新颖性） | 无（贡献声明） | S5→S6：结果→贡献 | "总体而言，…三点贡献。第一，…；据我们所知，这是首个…"镜像 "Overall…First…To our knowledge…first" | 达标 |
| 7 | 第二，…；除超越…外，…提供了…洞察 | P5-S9/10："Second, we develop a novel RL method…In addition to outperforming the state-of-the-art adversarial attack emulation, our proposed method provides actionable insights…"（贡献2+对比优势） | 无 | S6→S7：贡献2 | "第二，…；除超越…外，…"镜像 "Second…In addition to outperforming…" | 达标 |
| 8 | 第三，…攻击库…为安全从业者提供…测试基线 | P5-S11/12："Third, we design a novel RL-based RO method…The study provides cyber defense practitioners with practical insights…"（贡献3+实践启示） | 无 | S7→S8：贡献3+实践 | "第三，…"；"为…提供…"对应 "provides…practitioners with practical insights" | 达标 |

段落意义核查：P5 完成"范式→命名→功能→机制→实例化与评估→结果→三贡献（含新颖性声明与对比优势、实践价值）"八步，与 RADAR P5 同构。✓

### 研究一研究问题

如何自动生成多样化、可迁移、能逃避现有防护的编码智能体对抗攻击（上下文操纵）？基于 RL 的攻击仿真相对静态模板攻击，能否显著提升攻击成功率、覆盖面与可迁移性？
---

## 研究二（AgentShield-Detect：实时检测）

### P1 重写稿（对标 RADAR P1：背景与价值）

随着编码智能体进入生产开发流程，组织正在部署防护机制——输入过滤、沙箱隔离、权限控制与行为监控——以期在攻击造成损害之前识别威胁。这些机制已展现出识别已知攻击模式的能力，包括对显式提示注入与恶意工具调用的拦截（OWASP 2024）。结合大语言模型过滤与行为日志分析的新一代防护，已能在推理期标记可疑输入（【防护产品：CodeSentinel 等】）。例如，针对 LLM 应用的注入检测器可对已知注入模式达到 90% 以上的检测率（【占位：检测基准】）。如今，防护厂商与模型提供商正把 guardrail 织入编码智能体的开发与部署流程。例如，多家主流平台已默认开启输入过滤与权限提示（GitHub、OpenAI 产品文档）。一项面向企业安全团队的调查显示，大多数受访者认为缺少防护机制就无法安全部署编码智能体（【占位：调查出处】）。

### P1 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 随着…，组织正在部署防护机制——输入过滤、沙箱隔离…——以期… | P1-S1（趋势状语从句+现象主句） | 无 | 开篇定位：现象出现 | 双破折号列举防护机制（替代原文直陈，因"防护机制清单"是检测研究的对象域，必须一次交代） | 达标 |
| 2 | 这些机制已展现出…能力 | P1-S2（能力主张） | OWASP 2024：能力证据 | S1→S2：出现→能力 | "已展现出…的能力" | 达标 |
| 3 | 新一代防护…已能在推理期标记可疑输入 | P1-S3（技术 promise） | 【占位：防护产品】 | S2→S3：能力→技术 | 同构 | 达标（占位） |
| 4 | 例如，…90% 以上… | P1-S4（For instance 数字实例） | 【占位：检测基准】 | S3→S4：例证 | "例如，"；数字括注 | 达标（占位，不编造数字） |
| 5 | 如今，…正把 guardrail 织入…流程 | P1-S5（Today 采用） | 无 | S4→S5：能力→采用 | "如今，…织入…"镜像 "Today, …weaving…fabric" | 达标 |
| 6 | 例如，多家主流平台已默认开启… | P1-S6/7（两实例） | GitHub、OpenAI 产品文档 | S5→S6：采用→实例 | "例如，"；单句一实例（对照研究一 P1-S6 的分号合并，此处信息量小，一句即可） | 达标 |
| 7 | 一项面向企业安全团队的调查显示… | P1-S8（依赖加深） | 【占位：调查出处】 | S6→S7：实例→依赖（段落收束） | "一项…调查显示…" | 达标（占位） |

段落意义核查：P1 完成"现象→能力→技术→实例→采用→实例→依赖"七步，与 RADAR P1 同构；末句落在"依赖加深"，为 P2 转折蓄力。✓

### P2 重写稿（对标 RADAR P2：问题）

然而，编码智能体防护已被发现存在系统性盲区——对"单点文本正常但整体意图恶意"的多步间接操纵，现有过滤与规则漏报严重（Greshake et al. 2023；IssueTrojanBench）。编码智能体场景尤为突出：攻击可跨 issue、文件、工具与技能包多通道编排，单通道防护难以捕获（MalSkillBench）。例如，精心构造的恶意 issue 可穿透主流防护——对 66.5% 的恶意 issue 样本，防护未触发任何拦截，且绝大多数拒绝来自模型自身而非防护系统（IssueTrojanBench）。再如，恶意技能包可在看似合法的工具调用掩护下逐步植入载荷——技能供应链投毒（DDIPE、PhantomSkill）可绕过输入过滤，使防护在攻击完成前无法识别（【文献】）。两种情况下，攻击者都利用了防护"只见局部、不见整体"的盲区，通过跨通道、跨步骤的信号协同达成攻击。防护盲区已被视作自主软件开发安全的新兴威胁：实时检测的缺失意味着攻击在数十次工具调用后仍不被发现（【占位】）。虽然组织日益需要实时防护，但关于如何在编码智能体上实时、低误报地检测对抗攻击，目前知之甚少——信息管理领域的检测方法（欺诈网站、欺诈评论、社交机器人）尚未迁移到这一情境。

### P2 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 然而，…存在系统性盲区——对…多步间接操纵，…漏报严重 | P2-S1（转折+定义） | Greshake 2023、IssueTrojanBench：定义与证据 | P1→P2：价值→缺陷（However） | "然而，"；破折号定义（主词—范围限定），句式同 RADAR P2-S1 | 达标 |
| 2 | 编码智能体场景尤为突出：攻击可跨…多通道编排 | P2-S2（对象收窄/情境化） | MalSkillBench：多通道证据 | S1→S2：普遍盲区→本文情境 | "尤为突出："冒号展开情境特异性（同研究一 P2-S2 的手法） | 达标 |
| 3 | 例如，恶意 issue 可穿透主流防护——对 66.5%…未触发任何拦截 | P2-S3（实例1，数字） | IssueTrojanBench：66.5%（公开基准） | S2→S3：例证1 | "例如，"；破折号后展开数字证据 | 达标 |
| 4 | 再如，恶意技能包…——技能供应链投毒（DDIPE、PhantomSkill）… | P2-S4（实例2） | DDIPE、PhantomSkill（公开报告） | S3→S4：例证2 | "再如，"镜像 "As another example" | 达标 |
| 5 | 两种情况下，攻击者都利用了…盲区，通过…信号协同… | P2-S5（共性归纳） | 无（归纳） | S3–S4→S5：两实例→共性 | "两种情况下，"；"只见局部、不见整体"为情境化改写（原文 "meticulous and hard-to-notice" 的检测侧对应） | 达标 |
| 6 | 防护盲区已被视作…新兴威胁：实时检测的缺失意味着… | P2-S6（威胁定性） | 【占位：事件/报告】 | S5→S6：共性→威胁升维 | "已被视作…新兴威胁"镜像 "is construed as an emerging threat"；冒号后展开后果（原文用括注引用，我用冒号后果句，因检测缺失的后果需要陈述） | 达标 |
| 7 | 虽然组织日益需要实时防护，但关于如何…目前知之甚少——IS 检测方法…尚未迁移 | P2-S7（gap 句） | 51 篇清单（IS 检测谱系） | S6→S7：威胁→缺口（段落收束） | "虽然…，但…知之甚少"镜像 "While…, little is known about…"；破折号后点出"谱系未迁移"这一具体缺口（本文的差异化锚点） | 达标 |

段落意义核查：P2 完成七步同构；gap 句与原文一样落在"具体缺口"上，但缺口内容从"鲁棒性强化"换成"实时检测"，并以 IS 检测谱系未迁移收束，为 P3 的谱系动机铺路。✓

### P3 重写稿（对标 RADAR P3：理论动机一——IS 检测谱系作为信号框架）

在本研究中，我们旨在借鉴信息管理（IS）检测文献的理论与方法，开发编码智能体对抗攻击的实时检测器。IS 检测文献提供了一个成熟的信号框架，利用可观察特征区分恶意与良性对象：欺诈网站检测以第三方请求的结构特征识别伪装（【#25】）。这一框架进一步主张，文本意图可通过特征工程显式建模：欺诈评论检测以情感与显式方面特征捕捉表面正常文本中的操纵意图（【#28】）。在编码智能体情境中，该框架引入一个覆盖文本、行为与工具调用三通道的检测对象，攻击信号分散在轨迹事件日志之中。由此，检测文献确立了多信号融合是有效检测的前提（【#11】）。

### P3 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 在本研究中，我们旨在借鉴 IS 检测文献… | P3-S1（目的句） | 无 | P2→P3：gap→目的 | "在本研究中，我们旨在…"镜像原文 | 达标 |
| 2 | IS 检测文献提供了一个成熟的信号框架，…：欺诈网站检测…（【#25】） | P3-S2："RO provides a rigorous framework to incorporate the effect of an adversary…(Bertsimas et al., 2010)."（理论定义） | 【#25】：第一信号源（结构特征） | 目的→理论一：结构信号 | "提供了一个…框架"镜像 "provides a rigorous framework"；冒号后例证（对应原文 S2 的单句定义，我用冒号补充一个谱系实例以落实"信号框架"的内涵） | 达标（谱系替换：RO→IS 检测信号框架，句法功能不变） |
| 3 | 这一框架进一步主张，文本意图…（【#28】） | P3-S3："This framework promotes a two-player game…(Madry et al., 2018)."（框架性质） | 【#28】：第二信号源（文本特征工程） | 理论一→性质递进 | "这一框架进一步主张，"对应 "This framework promotes…"；冒号后例证 | 达标（替换：两玩家博弈→特征工程主张；功能是"框架的第二条性质"） |
| 4 | 在编码智能体情境中，该框架引入一个覆盖…三通道的检测对象… | P3-S4："In the cyber defense context, RO introduces an adversary who generates…"（情境实例化） | 无 | 性质→情境 | "在…情境中，该框架引入…"镜像 "In the…context, …introduces…" | 达标 |
| 5 | 由此，检测文献确立了多信号融合是有效检测的前提（【#11】） | P3-S5："As such, RO establishes that robust defense requires effective adversarial attack emulation (AAE)…"（推论句） | 【#11】：外部验证信号（综合推论） | 情境→推论（段落收束，为 P4 的轨迹建模铺垫） | "由此，…确立了…"镜像 "As such, …establishes…" | 达标 |

段落意义核查：P3 完成"目的→理论定义→性质递进→情境实例化→推论"五步，与 RADAR P3 完全同构；理论内容从 RO 换成 IS 检测谱系（#25→#28→#11），是情境差异下的必要替换。✓

### P4 重写稿（对标 RADAR P4：理论动机二——为什么轨迹行为建模恰好适配）

由于编码智能体攻击是跨通道、跨步骤的信号协同，检测器需要建模轨迹事件日志中的时序模式。行为建模方法专门研究行动序列与文本内容的融合：社交机器人检测以行为-文本深度融合、并以众包弱标签扩充训练数据，提升检测的鲁棒性（【#30】【#32】）。这类方法因而非常适合检测编码智能体轨迹中逐步展开的攻击。同时，检测器自身处于对抗环境，需以对抗样本训练，并报告对抗绕过率（Madry et al. 2018）。

### P4 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 由于编码智能体攻击是跨通道、跨步骤的信号协同，检测器需要建模…时序模式 | P4-S1："As adversarial attacks often involve taking a sequence of actions…, AAE can benefit from modeling the steps…"（对象序贯性） | 无（承接 P2 实例） | P3→P4：需要检测→攻击的时序性 | "由于…，…需要建模…"镜像 "As…, …can benefit from modeling…" | 达标 |
| 2 | 行为建模方法专门研究行动序列与文本内容的融合：…（【#30】【#32】） | P4-S2："RL specializes in examining the sequential interaction of an actor…with the environment…over discrete time steps…"（方法定义） | 【#30】：行为+文本融合；【#32】：弱监督标签 | S1→S2：时序性→方法定义 | "专门研究…：…"镜像 "specializes in examining…"；冒号后例证 | 达标（谱系替换：RL→行为建模方法，功能是"方法定义"） |
| 3 | 这类方法因而非常适合检测…逐步展开的攻击 | P4-S3："RL is thus well-suited for emulating the steps…"（适配结论） | 无（推论） | S2→S3：定义→适配 | "因而非常适合"镜像 "is thus well-suited for" | 达标 |
| 4 | 同时，检测器自身处于对抗环境… | P4-S4："Additionally, the sequence of actions captured by RL is useful for gaining insights…and further enhancing…"（附加价值/约束） | Madry et al. 2018：对抗训练必要性 | S3→S4：适配→附加约束 | "同时，"镜像 "Additionally" | 达标 |

段落意义核查：P4 完成四步同构；差异在 S4——RADAR 的附加价值是"洞察策略"，我的附加约束是"检测器自身对抗鲁棒性"（检测研究的必要补充）。✓

### P5 重写稿（对标 RADAR P5：工件与评估）

基于计算设计科学范式，我们开发 AgentShield-Detect，一个面向编码智能体对抗攻击的实时检测框架。AgentShield-Detect 逐时间步标记攻击信号，为人工审查与运行时防护提供依据。具体地，该框架以三通道特征（文本意图、行为序列、工具调用结构）输入轨迹事件日志，结合无标签轨迹自编码器与 agent-工具-文件异构图 GNN，输出逐时间步攻击概率，并以研究一生成的攻击库进行对抗训练。鉴于检测必须在攻击造成危害前触发、且不能以高误报打断正常开发，我们在公开的正常轨迹与攻击库上评估精确率、召回率、F1、AUC、检测延迟、误报率与对抗绕过率。我们的实验显示，该框架在低误报约束下达到可用的检测率，且对抗训练显著降低绕过率（【占位：待实验数据】）。总体而言，本研究作出三点贡献。第一，我们提出一个面向编码智能体的实时检测框架；据我们所知，这是首个将 IS 检测谱系系统迁移到编码智能体攻防情境的检测框架。第二，我们开发一种多通道特征融合的检测方法；除超越单通道基线外，它提供了可解释的输出，支持安全人员逐例审查。第三，我们建立检测器自身对抗鲁棒性的评估规范，填补防护评估只报攻击侧、不报检测侧鲁棒性的空白，并为从业者提供低误报约束下的部署依据。

### P5 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 基于计算设计科学范式，我们开发 AgentShield-Detect，一个…框架 | P5-S1（范式+命名） | 无 | P4→P5：动机→工件 | "基于计算设计科学范式，我们开发…，一个…框架"（同位语命名，同原文破折号命名异曲同工） | 达标 |
| 2 | AgentShield-Detect 逐时间步标记攻击信号，为…提供依据 | P5-S2（功能概述） | 无 | S1→S2：命名→功能 | 对仗："逐时间步标记…，为…提供…"镜像 "discovers…and prepares…" | 达标 |
| 3 | 具体地，…三通道特征…自编码器与…GNN…对抗训练 | P5-S3（组件展开） | 无 | S2→S3：功能→机制 | "具体地，"镜像 "Specifically"；长句串联特征、模型与训练 | 达标 |
| 4 | 鉴于检测必须在…前触发、且不能以高误报…，我们在…评估… | P5-S4（实例化理由+评估） | 无 | S3→S4：机制→评估 | "鉴于…，我们…评估…"镜像 "Given that…, we instantiate…, evaluate…" | 达标 |
| 5 | 我们的实验显示，…（【占位】） | P5-S5（结果预告） | 无 | S4→S5：评估→结果 | "我们的实验显示，…" | 达标（占位） |
| 6 | 总体而言，…三点贡献。第一，…；据我们所知，这是首个… | P5-S6/7/8（贡献总起+贡献1+新颖性） | 无 | S5→S6：贡献 | "总体而言，…第一，…；据我们所知，这是首个…" | 达标 |
| 7 | 第二，…；除超越单通道基线外，它提供了可解释的输出… | P5-S9/10（贡献2+对比优势） | 无 | S6→S7：贡献2 | "第二，…；除超越…外，…"镜像 "Second…In addition to outperforming…" | 达标 |
| 8 | 第三，…评估规范，填补…空白，并为从业者提供… | P5-S11/12（贡献3+实践启示） | 无 | S7→S8：贡献3+实践 | "第三，…；…，并为…提供…"对应 "Third…provides…practitioners with practical insights" | 达标 |

段落意义核查：P5 八步同构；贡献三落到"检测侧评估规范"，与 RADAR 贡献三"RL-RO 方法被实证检验有效"对应（都填补"评估空白"）。✓

### 研究二研究问题

如何从编码智能体的输入文本、行为轨迹与工具调用结构中实时识别对抗攻击？三通道特征融合与对抗训练能否在低误报下实现高检测率，并保持检测器自身的对抗鲁棒性？
---

## 研究三（AgentDefense-Robust：效用保持的鲁棒化）

### P1 重写稿（对标 RADAR P1：背景与价值）

随着编码智能体的对抗攻击在真实环境中显现——远程代码执行漏洞（Claude Code 系列 CVE）、私有仓库泄露（GitLost）与恶意技能包（MalSkillBench）——鲁棒化已成为其安全部署的关键环节。防御训练已展现出提升智能体鲁棒性的能力：安全微调与偏好优化可显著提高模型对恶意输入的拒绝率（MOCHA：最高 +32.4 个百分点）。将鲁棒优化与强化学习结合（RL-RO）的框架，已在恶意软件检测上展现出潜力（Ebrahimi et al. 2025）。例如，RADAR 框架使评估的恶意软件检测器的对抗鲁棒性平均提升约 7 倍（Ebrahimi et al. 2025）。如今，模型提供商正把安全微调织入编码智能体的开发流程，运行时防护（规则过滤、推理期检测）也已进入产品（CodeSentinel、TokenWall）。例如，多家厂商在发布编码智能体时同步提供安全配置与更新（厂商公告）。一项面向企业安全团队的调查显示，大多数受访者认为鲁棒性不足是编码智能体部署的首要障碍（【占位：调查出处】）。

### P1 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 随着…的对抗攻击在真实环境中显现——…——鲁棒化已成为…关键环节 | P1-S1（趋势状语从句+现象主句） | Claude Code CVE、GitLost、MalSkillBench：威胁证据 | 开篇定位：问题重要性 | "随着…显现——…——鲁棒化已成为…"镜像 "With…, …have been developed to…"；双破折号列举威胁事件 | 达标 |
| 2 | 防御训练已展现出…能力：安全微调与偏好优化…（MOCHA +32.4pp） | P1-S2（能力主张） | MOCHA：公开测量 | S1→S2：威胁→现有能力 | "已展现出…能力："冒号后给出能力内容与数字 | 达标 |
| 3 | 将 RO 与 RL 结合（RL-RO）的框架，已在…展现出潜力 | P1-S3（技术 promise） | Ebrahimi et al. 2025（RADAR）：方法谱系 | S2→S3：能力→方法 | "将…与…结合（…）的框架"；括号定义缩写（同 RADAR 命名缩写的括号用法） | 达标 |
| 4 | 例如，RADAR 框架使…平均提升约 7 倍 | P1-S4（For instance 数字实例） | Ebrahimi et al. 2025：7 倍数字 | S3→S4：例证 | "例如，"；数字括注出处 | 达标 |
| 5 | 如今，模型提供商正把安全微调织入…，运行时防护…也已进入产品 | P1-S5（Today 采用） | CodeSentinel、TokenWall（公开产品） | S4→S5：能力→采用 | "如今，…织入…"镜像 "Today, …weaving…fabric" | 达标 |
| 6 | 例如，多家厂商…同步提供安全配置与更新 | P1-S6/7（实例） | 厂商公告 | S5→S6：采用→实例 | "例如，" | 达标（信息量小，一句即可） |
| 7 | 一项…调查显示…首要障碍 | P1-S8（依赖加深） | 【占位：调查出处】 | S6→S7：实例→依赖（段落收束） | "一项…调查显示…" | 达标（占位） |

段落意义核查：P1 七步同构；与 RADAR P1 的差异在于"现象"从攻击规模换成"对抗攻击显现"，符合研究三所处的研究序列（前两研究已确立威胁）。✓

### P2 重写稿（对标 RADAR P2：问题）

然而，防御训练已被发现会带来"自主性税"——以显著牺牲良性任务能力为代价换取鲁棒性（Autonomy Tax，arXiv:2603.19423）。编码智能体是受其影响最典型的对象：其任务是开放性、长程的，防御训练引入的过度保守会直接转化为超时与任务失败。例如，一项系统测量显示，防御训练后智能体 99% 的良性任务超时，而基线仅为 13%（Autonomy Tax）。再如，推理期规则防护虽不改变模型，但其对正常工具调用的误伤会打断开发流程，同样构成效用损失（【占位：误报测量】）。两种情况下，防御都以可度量的方式损害了良性效用，而现有研究极少报告这一代价。自主性税已被视作鲁棒化部署的新兴障碍：若鲁棒化使智能体无法完成任务，组织将拒绝部署。虽然防御训练日益被采用，但关于如何在编码智能体上同时实现鲁棒性与良性效用，目前知之甚少——现有防御评估大多只报告攻击成功率或拒绝率，不报告防御后的良性任务完成率。

### P2 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 然而，防御训练已被发现会带来"自主性税"——以显著牺牲…为代价… | P2-S1（转折+定义） | Autonomy Tax（arXiv:2603.19423）：定义来源 | P1→P2：价值→代价（However） | "然而，"；破折号定义（"自主性税"—同位语展开），同 RADAR P2-S1 句式 | 达标 |
| 2 | 编码智能体是受其影响最典型的对象：其任务是开放性、长程的… | P2-S2（对象收窄/情境化） | 无（情境推理） | S1→S2：普遍代价→本文对象 | "最典型的对象："冒号展开情境特异性 | 达标 |
| 3 | 例如，一项系统测量显示…99% 超时，基线 13% | P2-S3（实例1，数字） | Autonomy Tax：公开测量 | S2→S3：例证1 | "例如，"；"99%…而基线仅为 13%"对照句式 | 达标 |
| 4 | 再如，推理期规则防护…误伤…打断开发流程 | P2-S4（实例2） | 【占位：误报测量】 | S3→S4：例证2 | "再如，"镜像 "As another example" | 达标（占位） |
| 5 | 两种情况下，防御都以可度量的方式损害了良性效用… | P2-S5（共性归纳） | 无 | S3–S4→S5：两实例→共性 | "两种情况下，" | 达标 |
| 6 | 自主性税已被视作…新兴障碍：若…，组织将拒绝部署 | P2-S6（威胁定性） | 无（推理） | S5→S6：共性→定性 | "已被视作…新兴障碍"镜像 "is construed as an emerging threat"；冒号展开后果 | 达标 |
| 7 | 虽然防御训练日益被采用，但关于如何…目前知之甚少——现有防御评估大多…不报告良性任务完成率 | P2-S7（gap 句） | 51 篇清单（防御评估文献） | S6→S7：威胁→缺口（段落收束） | "虽然…，但…知之甚少"镜像 "While…, little is known about…"；破折号后点出"评估不报良性效用"这一具体缺口 | 达标 |

段落意义核查：P2 七步同构；与 RADAR 的差异是威胁主体从"对抗攻击"换成"自主性税"（防御的代价），这是研究三的问题域——RADAR 的 gap 是"不知如何强化鲁棒性"，我的 gap 是"不知如何在保持效用下强化鲁棒性"，后者包含前者且更具体。✓

### P3 重写稿（对标 RADAR P3：理论动机一——RO）

在本研究中，我们旨在利用鲁棒优化（RO）与强化学习（RL）理论，开发效用保持的编码智能体鲁棒化框架。RO 提供了一个严格的框架，将对手的效应纳入智能体学习过程的优化之中（Bertsimas et al. 2010）。该框架促进对手与智能体之间的两玩家博弈（Madry et al. 2018）。在编码智能体情境中，RO 引入一个生成对抗攻击的对手，并训练智能体从这些攻击中学习以提升鲁棒性。由此，RO 确立了鲁棒防御要求有效的对抗攻击仿真（AAE）（Kolter & Madry 2018）——本研究一即提供此类攻击。

### P3 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 在本研究中，我们旨在利用 RO 与 RL 理论… | P3-S1（目的句） | 无 | P2→P3：gap→目的 | "在本研究中，我们旨在利用…"与 RADAR P3-S1 几乎逐词对应（这是情境允许的最大贴近：两研究共享 RO+RL 理论） | 达标 |
| 2 | RO 提供了一个严格的框架，将对手的效应纳入…优化之中 | P3-S2（理论定义） | Bertsimas et al. 2010：RO 奠基 | 目的→理论一 | "提供了一个严格的框架"镜像 "provides a rigorous framework" | 达标 |
| 3 | 该框架促进对手与智能体之间的两玩家博弈 | P3-S3（博弈性质） | Madry et al. 2018：博弈 | 理论→性质 | "该框架促进…"镜像 "This framework promotes…" | 达标 |
| 4 | 在编码智能体情境中，RO 引入一个生成对抗攻击的对手… | P3-S4（情境实例化） | 无 | 性质→情境 | "在…情境中，RO 引入…"镜像 "In the cyber defense context, RO introduces…" | 达标 |
| 5 | 由此，RO 确立了…AAE——本研究一即提供此类攻击 | P3-S5（推论句） | Kolter & Madry 2018：AAE 依据 | 情境→推论（段落收束，为 P4 铺垫） | "由此，…确立了…"镜像 "As such, …establishes…"；破折号后接系列钩子（本研究一） | 达标 |

段落意义核查：P3 五步与 RADAR P3 同构度最高（两研究共享 RO/RL 理论），除系列钩子外几乎逐句对应。✓

### P4 重写稿（对标 RADAR P4：理论动机二——RL 与效用保持机制）

由于编码智能体攻击通常涉及一串动作，鲁棒化训练可以从建模对手的逐步动作中获益；同时，标准 RO 目标不约束良性效用，需要显式的效用保持机制。RL 专门研究行动者与环境在离散时间步上的序贯交互（Sutton & Barto 2018），适配攻防的重复博弈，也适配运行时门控：检测信号（本研究二）可在检测到攻击时触发降权、隔离或回滚。RL 因而非常适合把对手的动作序列转化为安全行为：对抗重训练与偏好优化（DPO）提供了把攻击样本转化为安全行为的训练机制（【#26】）。此外，训练级鲁棒化与运行时门控的组合，使效用约束在训练与推理两个层面同时成立。

### P4 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 由于…攻击通常涉及一串动作，鲁棒化训练可以从建模…中获益；同时，标准 RO 目标不约束良性效用… | P4-S1："As adversarial attacks often involve taking a sequence of actions…, AAE can benefit from modeling the steps…"（对象序贯性） | 无 | P3→P4：AAE 需要→序贯性与效用缺口 | "由于…，…可以从…中获益；同时，…"镜像 "As…, …can benefit from…"；分号并入效用缺口（本研究差异化的理论锚点——自主性税的理论根源，RADAR 无此内容） | 达标（有意识扩展：S1 在原文句法上并入一句，为 S2–S3 的机制句铺垫） |
| 2 | RL 专门研究…序贯交互…适配攻防的重复博弈，也适配运行时门控：检测信号… | P4-S2："RL specializes in examining the sequential interaction of an actor…with the environment…over discrete time steps…"（方法定义） | Sutton & Barto 2018：定义权威 | S1→S2：序贯性→RL 定义 | "RL 专门研究…"镜像 "RL specializes in…"；冒号引出门控机制（替代原文括号举例） | 达标 |
| 3 | RL 因而非常适合把对手的动作序列转化为安全行为：…（【#26】） | P4-S3："RL is thus well-suited for emulating the steps…"（适配结论） | 【#26】：效用保持训练机制 | S2→S3：定义→适配 | "因而非常适合"镜像 "is thus well-suited for"；冒号给出转化机制 | 达标 |
| 4 | 此外，训练级鲁棒化与运行时门控的组合… | P4-S4："Additionally, the sequence of actions captured by RL is useful for gaining insights…and further enhancing…"（附加价值） | 无 | S3→S4：适配→组合价值 | "此外，"镜像 "Additionally" | 达标 |

段落意义核查：P4 完成四步同构；差异在 S1 的分号句（效用缺口）与 S2/S3 的冒号展开（门控与 DPO 机制），这是"效用保持"研究目标的必要内容。✓

### P5 重写稿（对标 RADAR P5：工件与评估）

基于计算设计科学范式，我们开发 AgentDefense-Robust，一个效用保持的编码智能体鲁棒化框架。AgentDefense-Robust 以对抗重训练、偏好优化与 RL minimax 三种机制鲁棒化智能体，并以检测器实现运行时门控。具体地，该框架在训练阶段以研究一攻击库生成对抗样本，分别执行安全微调、DPO 与 minimax 训练；在推理阶段以研究二检测器逐时间步判断攻击，触发降权、隔离或回滚。鉴于良性效用是部署的第一约束，我们在 SWE-bench Verified 上评估良性任务完成率（Robust Resolve Rate），在研究一攻击库上评估攻击成功率（ASR），并报告性能-扰动曲线下面积（RAUC）与自主性税检验。我们的实验显示，该框架在显著降低 ASR 的同时保持良性任务完成率，且运行时门控进一步改善鲁棒-效用权衡（【占位：待实验数据】）。总体而言，本研究作出三点贡献。第一，我们提出一个以良性效用为第一约束的编码智能体鲁棒化框架；据我们所知，这是首个显式处理自主性税的鲁棒化框架。第二，我们将 RADAR 的 RL-RO 范式落地到编码智能体情境，并扩展出检测-防御运行时闭环；除超越无门控的防御训练外，该方法提供了对鲁棒-效用权衡的可操作洞察。第三，我们建立"ASR + Robust Resolve Rate"的双指标评估规范，填补防御评估忽视良性效用的空白，并为从业者提供在鲁棒性与任务能力之间权衡的决策依据。

### P5 逐句审计表

| # | 重写句节选 | 对标 RADAR 句（功能/句式） | 引用支撑作用 | 句间与段落逻辑 | 标点与句式 | 判断 |
|---|---|---|---|---|---|---|
| 1 | 基于计算设计科学范式，我们开发 AgentDefense-Robust，一个…框架 | P5-S1（范式+命名） | 无 | P4→P5：动机→工件 | "基于计算设计科学范式，我们开发…，一个…框架"（同位语命名） | 达标 |
| 2 | AgentDefense-Robust 以…三种机制鲁棒化智能体，并以检测器实现运行时门控 | P5-S2（功能概述） | 无 | S1→S2：命名→功能 | 对仗："以…，并以…"镜像 "discovers…and prepares…" | 达标 |
| 3 | 具体地，…训练阶段…；推理阶段… | P5-S3（组件展开） | 无 | S2→S3：功能→机制 | "具体地，"；分号并列训练/推理两阶段（同 RADAR 以 and 连接两组件的功能） | 达标 |
| 4 | 鉴于良性效用是部署的第一约束，我们在…评估… | P5-S4（实例化理由+评估） | 无 | S3→S4：机制→评估 | "鉴于…，我们…评估…"镜像 "Given that…, we instantiate…, evaluate…" | 达标 |
| 5 | 我们的实验显示，…（【占位】） | P5-S5（结果预告） | 无 | S4→S5：评估→结果 | "我们的实验显示，…" | 达标（占位） |
| 6 | 总体而言，…三点贡献。第一，…；据我们所知，这是首个… | P5-S6/7/8（贡献总起+贡献1+新颖性） | 无 | S5→S6：贡献 | "总体而言，…第一，…；据我们所知，这是首个…" | 达标 |
| 7 | 第二，…落地…并扩展出…闭环；除超越…外，… | P5-S9/10（贡献2+对比优势） | 无 | S6→S7：贡献2 | "第二，…；除超越…外，…"镜像 "Second…In addition to outperforming…" | 达标 |
| 8 | 第三，…双指标评估规范，填补…空白，并为从业者提供… | P5-S11/12（贡献3+实践启示） | 无 | S7→S8：贡献3+实践 | "第三，…；…并为…提供…" | 达标 |

段落意义核查：P5 八步同构；与 RADAR 的差异集中在"良性效用第一约束"与"检测-防御闭环"，即本研究的两个差异化贡献。✓

### 研究三研究问题

如何在编码智能体上实现鲁棒化而不支付自主性税？对抗重训练、偏好优化与 RL minimax 的何种组合能在显著降低 ASR 的同时保持良性任务完成率？运行时检测联动（研究二）能否进一步改善鲁棒-效用权衡？
---

## 附录：RADAR Introduction 原文逐句功能标注（审计基准，五段共 36 句）

以下为 RADAR（Ebrahimi et al. 2025, MISQ）Introduction 全文的逐句功能标注，供对查。标注维度：功能、引用角色、句间联系、标点句式。

### P1（背景与价值，8 句）

| # | 原文句（节选） | 功能 | 引用角色 | 句间联系 | 标点句式 |
|---|---|---|---|---|---|
| S1 | With the recent increase in the scale and severity of cyber attacks, AI agents have been developed to automate cyber defense… | 现象出现 | 领域定位（Apruzzese 2019；Rai 2017） | 开篇 | "With…"状语从句+主句 |
| S2 | Cyber defense AI agents have demonstrated the ability to effectively detect and remediate threats at an unprecedented scale | 能力主张 | 行业报告（Tolido 2019） | S1→S2：出现→能力 | "have demonstrated the ability to" |
| S3 | New AI agents, including deep neural networks, have shown promise in rapidly detecting unseen malware… | 技术 promise | 方法权威（Goodfellow 2018） | S2→S3：能力→技术 | 插入语 "including…" |
| S4 | For instance, AI-based malware detectors can detect unseen mobile Android malware with 96% precision… | 数字实例 | 具体研究（Narayanan 2018） | S3→S4：例证 | "For instance,"；数字 |
| S5 | Today, leading cybersecurity and IT firms are weaving AI-enabled cyber defense into their operational fabric… | 产业采用 | 无 | S4→S5：能力→采用 | "Today,…weaving…fabric" |
| S6 | For example, Avast and Symantec, two major cybersecurity firms, benefit from deep neural networks… | 实例1 | 无（公司名） | S5→S6：例证 | "For example,"；同位语 |
| S7 | Endgame uses gradient boosting trees in its open-source malware detector | 实例2 | 引用（Anderson 2018；Bloomberg 2018；Song 2022） | S6→S7：例证 | 单句 |
| S8 | A large-scale international survey of IT firms revealed that 69% of them believe they cannot accomplish cyber defense without AI agents | 依赖加深 | 行业调查（Tolido 2019） | S7→S8：依赖（收束） | 数字 69% |

### P2（问题，7 句）

| # | 原文句（节选） | 功能 | 引用角色 | 句间联系 | 标点句式 |
|---|---|---|---|---|---|
| S1 | However, AI agents have been found to be vulnerable to adversarial attacks—adversarial data inputs meticulously modified by an adversary to mislead the AI agent | 转折+定义 | 定义来源（Yuan 2019） | P1→P2：转折 | "However,"；破折号定义 |
| S2 | Cyber defense AI agents are no exception | 对象收窄 | 引用（Apruzzese 2019） | S1→S2 | 短句 |
| S3 | For instance, a previously known malicious executable could be modified to evade an AI malware detector by first changing the signature section and subsequently resetting the file checksum | 实例1（步骤化） | 无 | S2→S3：例证 | "For instance,"；"by first…and subsequently…" |
| S4 | As another example, malicious network packets could be modified to evade an intrusion detection system by performing encoding followed by fragmentation | 实例2 | 无 | S3→S4：例证 | "As another example," |
| S5 | In both cases, an adversary crafts adversarial inputs by taking steps of meticulous and hard-to-notice changes… | 共性归纳 | 引用（Goodfellow 2018；Monteiro 2019） | S3–S4→S5 | "In both cases," |
| S6 | The vulnerability…is construed as an emerging threat to autonomous cyber defense | 威胁定性 | 引用（Goosen 2018） | S5→S6：升维 | "is construed as an emerging threat" |
| S7 | While cyber defense AI agents are increasingly relied on…, little is known about strengthening the robustness… | gap 句 | 无 | S6→S7：收束 | "While…, little is known about…" |

### P3（理论动机一：RO，5 句）

| # | 原文句（节选） | 功能 | 引用角色 | 句间联系 | 标点句式 |
|---|---|---|---|---|---|
| S1 | In this study, we aim to strengthen the robustness…by leveraging the theories of RO and RL | 目的句 | 无 | P2→P3：回应 gap | "In this study, we aim to…by leveraging…" |
| S2 | RO provides a rigorous framework to incorporate the effect of an adversary in the optimization process of learning an AI agent | 理论定义 | RO 奠基（Bertsimas 2010） | 目的→理论 | "provides a rigorous framework" |
| S3 | This framework promotes a two-player game between the adversary and the AI agent | 框架性质 | 博弈（Madry 2018） | 定义→性质 | "This framework promotes…" |
| S4 | In the cyber defense context, RO introduces an adversary who generates evasive adversarial attacks and trains an AI agent that learns from these attacks… | 情境实例化 | 无 | 性质→情境 | "In the…context, RO introduces…" |
| S5 | As such, RO establishes that robust defense requires effective adversarial attack emulation (AAE) | 推论 | AAE 依据（Kolter & Madry 2018） | 情境→推论（收束） | "As such, …establishes…" |

### P4（理论动机二：RL，4 句）

| # | 原文句（节选） | 功能 | 引用角色 | 句间联系 | 标点句式 |
|---|---|---|---|---|---|
| S1 | As adversarial attacks often involve taking a sequence of actions…, AAE can benefit from modeling the steps taken by the adversary… | 对象序贯性 | 引用（Anderson 2018；Fang 2019） | P3→P4：AAE 需要→序贯性 | "As…, …can benefit from modeling…" |
| S2 | RL specializes in examining the sequential interaction of an actor (e.g., adversary) with the environment (e.g., IT infrastructure…) over discrete time steps | 方法定义 | RL 权威（Sutton & Barto 2018） | 序贯性→RL | 括号举例 "e.g., …" |
| S3 | RL is thus well-suited for emulating the steps (i.e., the sequence of actions) an adversary takes… | 适配结论 | 无 | 定义→适配 | "is thus well-suited for" |
| S4 | Additionally, the sequence of actions captured by RL is useful for gaining insights into the adversary's strategies and further enhancing the cyber defense AI agent | 附加价值 | 引用（Anderson 2018） | 适配→附加 | "Additionally," |

### P5（工件与评估，12 句）

| # | 原文句（节选） | 功能 | 引用角色 | 句间联系 | 标点句式 |
|---|---|---|---|---|---|
| S1 | Drawing on the computational design science paradigm, we leverage RO and RL to develop a novel RL-based adversarial attack robustness (RADAR) framework… | 范式+命名 | 无 | P4→P5 | "Drawing on…paradigm, we develop…"；括号缩写 |
| S2 | RADAR discovers effective adversarial attacks and prepares cyber defense AI agents to remediate them | 功能概述 | 无 | 命名→功能 | 对仗 "discovers…and prepares…" |
| S3 | Specifically, RADAR offers a novel RL approach to emulate adversarial attacks and presents a novel RL-based RO formalization to strengthen… | 组件展开 | 无 | 功能→机制 | "Specifically,"；"offers…and presents…" |
| S4 | Given that malware attacks are the leading threat to IT infrastructure, we instantiate our RADAR framework…, evaluate the effectiveness…against state-of-the-art…benchmark methods, and present the utility… | 实例化理由+评估 | 威胁统计（Bissell 2019） | 机制→评估 | "Given that…, we instantiate…, evaluate…, and present…" |
| S5 | Our experiments showed that RADAR increased the robustness…by seven times, on average… | 结果预告 | 无（自身结果） | 评估→结果 | 数字 "seven times" |
| S6 | Overall, this study makes three major contributions | 贡献总起 | 无 | 结果→贡献 | "Overall," |
| S7 | First, we propose a framework for strengthening…at a large scale | 贡献1 | 无 | S6→S7 | "First," |
| S8 | To our knowledge, this is the first robustification framework modeling the adversarial game… | 贡献1 新颖性 | 无 | S7→S8 | "To our knowledge, this is the first…" |
| S9 | Second, we develop a novel RL method for emulating sequences of adversarial attack actions… | 贡献2 | 无 | S8→S9 | "Second," |
| S10 | In addition to outperforming the state-of-the-art adversarial attack emulation, our proposed method provides actionable insights… | 贡献2 对比优势 | 无 | S9→S10 | "In addition to outperforming…, …provides…" |
| S11 | Third, we design a novel RL-based RO method that is empirically tested to be effective… | 贡献3 | 无 | S10→S11 | "Third," |
| S12 | The study provides cyber defense practitioners with practical insights, including… | 实践启示 | 无 | S11→S12 | "provides…practitioners with practical insights" |

## 使用说明

- 三篇重写稿的每一句都可在上表中找到对应功能句；审计表中标注"有意识调整/扩展"之处，均为情境差异（编码智能体 vs 恶意软件、检测谱系 vs RO/RL）导致的必要替换，句法功能与推进逻辑保持不变。
- 段落对应关系：P1 背景与价值、P2 问题、P3 理论动机一（研究一=攻击仿真必要性/研究二=IS 检测信号框架/研究三=RO）、P4 理论动机二（研究一=RL 适配攻击仿真/研究二=轨迹行为建模/研究三=RL 与效用保持机制）、P5 工件与评估。
- 下一步（若通过审核）：研究一的完整 MDP 定义（状态/动作/奖励、PPO 细节、基线 SWExploit/FCV/RLbreaker）、研究二的特征与模型细节、研究三的训练与门控细节，以及三篇的"研究背景（Research Background）"部分逐句对标。