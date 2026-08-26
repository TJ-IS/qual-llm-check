# AI 加速漏洞协调修复与披露候选终审

> 审查日期：2026-08-16  
> 研究对象：在已授权、隔离环境中发现漏洞后，由 coding agent 联合生成并验证真实修复工件、协调选定下游，并决定分阶段信息释放。  
> 终局判定：**NO-GO；不得冻结为三篇论文中的独立题位。置信度：高。**  
> 实验状态：**本终审未运行训练、Docker counterfactual rollout、PoC、补丁、消融或统计检验。** 下文模型、张量、损失、算力、基线与结果字段均是 steelman 设计或撤题检验，不是本项目的经验结果。既有论文的数字只转述其作者报告。

## 0. 终审结论先行

候选现象成立，而且比普通“漏洞检测”或“补丁生成”更接近一个重要的组织行动问题。AI security/coding agents 能压缩发现、验证与 patch-diff 逆向的时间；维护者却仍受 triage、测试、回移植、发布窗口和下游吸收能力限制。补丁因此具有双重作用：它能让防守者部署保护，也能向攻击者暴露可逆向的差异。公开信息还可能通过声誉或期限压力加快上游修复，同时加快攻击知识扩散。这个冲突需要分别观察攻击扩散、补丁就绪与质量、防护措施/下游采纳和维护容量，不能压成一个 risk score。

但是，候选不满足本项目的独立论文门槛。否决依据不是“尚未做实验”，而是三个先于实验成立的失败。

1. **直接近邻将剩余空间压缩成模块交集。** Cavusoglu、Cavusoglu 与 Raghunathan（2007）已经比较 full-vendor、immediate-public、hybrid/responsible disclosure，包含多供应商和向 selected users 提供 privileged knowledge 的 early-warning system；Arora、Telang 与 Xu（2008）已经联合 protected period、vendor patch timing、patch quality、user adoption 和 workaround；Cavusoglu、Cavusoglu 与 Zhang（2008）已经联合 vendor release 与 user update cycle；Gao et al.（2026）又联合 vulnerability discovery、imperfect debugging、dynamic user adoption 与 periodic/non-periodic patch timing。Vultron/FIRST 已把多方协调与 embargo 写成可执行状态机，Project Zero/Anthropic/OpenAI/Cisco 已把分层信息、维护吸收、下游 patch gap 与披露节奏写成现实政策。另一方面，PatchAgent、KeaRepair、PatchEval-Verified、SEC-bench 和 OSS-CRS 已覆盖真实补丁生成与验证；PoCEvolve 和 Anthropic N-day 研究直接覆盖 patch-diff→PoC/exploit；Oracle’s Gambit、ADAPT、When Discovery Outpaces Remediation 与 **APT/RL 版 VulnGym（arXiv:2607.24552）** 已覆盖攻击者—防御者竞速、容量和补丁策略。截止日未定位到一篇正式工作同时输出“真实 remedy bytes＋remedy-specific CVD packet/scope/timing＋成对执行结果”，但这一空位本身只是已有能力的交集，不是独有计算机制。
2. **MEC→MAP→ALG 不闭合。** Mitra 与 Ransbotham（2015）的相反扩散和 busy-period moderation，配合 Arora et al.（2010）的 disclosure→patch hazard，能合理导出分开的 hazard/state heads；Arora et al.（2008）能补入质量、采纳与 workaround；Ahmed et al.（2021）能限定披露机制、firm response 和 firm risk。然而这些理论没有指出获得同一原始图、动作、标签与预算的通用 temporal heterogeneous graph Transformer＋distributional SMDP 会沿哪个稳定方向算错。把 attack、readiness、quality、adoption 和 load 分成五个 heads 是良好的测量纪律，却仍可由通用多任务 world model 复制。技术事实“补丁可被逆向”更不能冒充 IS 理论。故理论可提供 MEC 和一部分 MAP，不能产生不可替代的 MAP→专用 ALG。
3. **历史数据不能识别联合政策。** OSV/GHSA/NVD、fix commits、advisory 和 registry adoption history 只记录一条实际路径；未采取的修复字节、私下通知集合、披露包与时点没有结果。隔离 Docker 中以公开 CVE 或安全 morphed clone 做 common-seed attacker/defender counterfactual rollouts，原则上能识别**该模拟器内**的策略差，但尚未构造；若攻击者扩散、维护者响应和下游采纳都由研究者写入模拟器，再用相同规则证明 theory-factored policy 最优，会形成循环验证。该风险不是增加样本即可消除。

删除 coding agent 后，核心组织问题仍完整存在：协调者仍须分配有限维护容量、选择通知对象、安排补丁/披露与下游采纳。coding agent 的不可删除部分只能是**真实生成、验证和回移植的 remedy bytes 会同时改变 defender executable outcome 与 attacker patch-diff outcome**。这是有价值的工程能力，但现有 IS 理论没有把字节级作用导出为通用控制器无法复制的计算。与状态迁移题和 C3 在现象上可以划清边界，也不能修复这一失败。

因此，本题不进入实现、真实披露、危险 PoC、维护者招募或论文正文。下文仍给出最强可实现版本，目的是证明否决来自贡献和识别，而非把候选想得过弱。

## 1. 审查范围、证据纪律与问题冻结

### 1.1 实际回读范围

本次先完整回读 `powershell-usage` 与 `otero-open-api` 两份 `SKILL.md`，随后完整回读以下本地材料：

- 肖帅勇老师两篇 ISR 主文：`database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md` 与 `database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md`。
- 写作与句键材料：`00F_逐段双ISR写作与引用审计协议.md`、`00J_肖帅勇两篇ISR全篇逐句逻辑与引文责任索引.md`、`00K_DSDL全篇逐句逻辑与引文责任索引.md`、`00M_ACAA实证贡献与结论逐句逻辑索引.md`、`00W_肖帅勇两篇ISR源行句段主键Manifest.md`。
- 本题三份本地理论全文：Mitra 与 Ransbotham（2015）`05482_*`、Arora et al.（2010）`06848_*`、Ahmed et al.（2021）`19800_*`；并回读 Arora、Telang 与 Xu（2008）的 46 页作者全文。
- 与状态迁移题、C3/有限审核容量题有关的 `01D`、`01F` 与 `01M`，用于动作和理论边界检查。

技术近邻优先使用正式出版全文、会议正式全文、作者终稿、论文官方 artifact 或机构官方政策。预印本必须有可回读全文才承担方法、数据或局限主张；搜索摘要只用于定位。Gao et al.（2026）的出版方页面提供 highlights、摘要、引言、section snippets 和结论片段，但付费 PDF 未取得，因此只使用可见页面所明确的模型范围。Cavusoglu et al.（2007）作者 PDF 在检索索引中可读到正文段落，但直接打开持续返回 502；因此关于 early warning、多供应商与政策比较只采用出版摘要和已索引正文，不扩展未见公式。Zhang、Demirezen 与 Kumar（2025）的正式页和 77 页 SSRN/博士论文章节已定位，但全文端点本次超时；仅使用正式摘要/作者项目页明确给出的 BBP、leak risk、patching complexity、security posture 与 bounty 结论。这个边界比用摘要猜测模型细节更重要。

Otero 的只读 API 说明已回读；本题所需 Basket 主文均已有本地全文或作者全文，故没有为制造“使用过 API”的记录而重复下载。未定位到联合工作只表示截至 2026-08-16 的本次检索没有发现，不是绝对不存在的证明。

### 1.2 冻结研究问题

允许保留的最强 RQ 是：

> 在维护者吸收能力有限、修补本身可能泄露漏洞信息的条件下，coding agent 如何联合分配**可执行修复努力**与**分阶段信息释放**，使已验证的 remedy artifact、下游保护采纳和攻击者可获信息共同演化，并创造且维持 defender head start？

这不是以下问题：

- 不是给漏洞打 exploitability/risk 标签。
- 不是只生成一个 patch，也不是只判断 disclose/withhold。
- 不是在已存在补丁集合中做普通优先级排序。
- 不是把 7/45/90 天固定政策换成 learned deadline。
- 不是把永久保密、全部拒绝或永远等待人审当作安全成功。
- 不是让危险 PoC 接触真实系统，或把真实未披露漏洞用于实验。

一个 episode 必须从已授权、可重置的漏洞实例开始，直到 remedy 被验证并传播、技术信息按阶段释放、下游采纳或 horizon 结束。动作必须写入并执行 patch、mitigation 或 backport，披露动作只占联合动作的一部分。

## 2. IS 理论责任：能承担什么，不能承担什么

| 理论来源 | 原文可承担的机制/状态 | 合法 MAP | 不得冒充的责任 | 终审作用 |
|---|---|---|---|---|
| Mitra & Ransbotham, ISR 2015，[DOI](https://doi.org/10.1287/isre.2014.0560)；本地 `05482_*` 全文 | 攻击与保护措施沿相反方向扩散；以攻击/保护半衰期、扩散率与 delay 表示竞速；成功 compromise 是攻击先于保护；full disclosure 加快首次攻击，也可使保护更快扩散；defender busy period 放大 full-disclosure 的首次攻击效应 | 分开的 `attack_hazard`、`protection_adoption_hazard`、delay、workload moderator；不能合成单一 risk head | 原文 IDS 数据没有观察 defender action、patch quality、客户损失或成功 compromise，也未证明 limited disclosure 总是更优；作者明确警告不能据其分析得出该政策结论 | **MEC 有效，MAP 部分有效** |
| Arora, Krishnan, Telang & Yang, ISR 2010，[DOI](https://doi.org/10.1287/isre.1080.0226)；本地 `06848_*` 全文 | vendor 在开发成本与其内化的客户损失间权衡；disclosure 是 time-varying covariate；在历史样本中实际 disclosure 后 patch-release hazard 约为之前的 2.45 倍，severity/source/open-source status 也相关 | `patch_readiness_hazard(t｜actual disclosure, severity, source, vendor)` 与 calibration target | 是 reduced-form hazard，不是最优政策；不观察开发成本/客户损失，不识别 threat-of-disclosure、patch quality、攻击扩散或反事实 disclosure；作者保留 endogeneity/选择问题 | **MEC/经验校准有效，不能直接给 policy** |
| Arora, Telang & Xu, Management Science 2008，[作者全文](https://www.heinz.cmu.edu/~rtelang/disclosure_MS.pdf)、[DOI](https://doi.org/10.1287/mnsc.1070.0771) | social planner 选择 protected period `T`，vendor 选择 patch time `τ` 与扩展中的 quality `q`；用户按 `p(z,q)` 采纳；patch 可暴露额外细节；smart users 可用有成本 workaround `α,w`；更长保护期不必然产生更高质量 | protected-period state、patch readiness/quality、post-patch adoption、workaround coverage 和 pre/post-patch loss 分开建模 | 单一 vendor、binary all-or-none disclosure、外生用户/攻击者、确定 patch time 等简化；不是多方 CVD、内容级 disclosure 或 learned agent | **最强政策理论邻居；显著挤压 timing/quality/adoption 新意** |
| Ahmed et al., DSS 2021，[DOI](https://doi.org/10.1016/j.dss.2021.113586)；本地 `19800_*` 全文 | 系统综述区分 market/non-market、direct/platform/indirect mechanisms；过程包含 report→verify→notify vendor→protected period→technical disclosure；后果分 firm response 与 firm risk；SSC 可先向客户提供保护过滤；综述记录 patch/advisory 可吸引攻击 | 披露机制类别、参与者、firm response/risk 与信息阶段的 schema | 作者明确排除技术 discovery，目标是 synthesis/framework 与 future theorizing；没有统一因果模型、神经状态、联合动作或 policy identification | **定义/边界有效，不是 MEC→ALG 理论** |

理论合成最多得到如下状态，而不能得到一个标量 `risk_head`：

\[
s_t=\left(h_t^{attack},h_t^{ready},q_t^{patch},h_t^{adopt},W_t^{maint},I_t^{exposed}\right).
\]

其中 `attack` 负责攻击扩散，`ready` 负责上游补丁就绪，`patch` 负责正确性/回归质量，`adopt` 负责 workaround、保护措施和下游部署，`maint` 负责维护队列/忙碌状态，`exposed` 负责不同 disclosure artifact 已经暴露的信息。任何模型若把它们相加成一个“defender head start score”，便抹掉理论中的冲突。

### 2.1 MEC→MAP→ALG 的致命断点

理论确实产生有意义的方向冲突：公开信息可提高 `h_ready`，也可提高 `h_attack`；更快 patch 可缩短无保护期，却可能降低 `q_patch`；发布 patch 提高 `h_adopt`，同时通过 diff 提高 `I_exposed`；busy workload 会延长 readiness/backport 并改变冲突大小。这构成 MEC。

但这些冲突并没有产生 ACAA 中“普通 affinity 必然偏好相似项、而理论要求互补项”那样的稳定错误方向，也没有产生 DSDL 中不可交换的 `F-E`。一个通用 action-conditioned Transformer 或 POMDP 本来就可以把 observation、transition、reward、hazard 与 constraint 分开，并从同一 paired rollout 学到上述交互。给 theory-factored 模型额外的 attack/defense/quality/load 标签而不给 generic model，比较不公平；给双方相同标签，generic multi-head model 又能复制。

因此：

- `MEC`：**PASS**，但来自多篇理论的组合。
- `MEC→MAP`：**PARTIAL**，可产生可审计状态分解。
- `MAP→不可替代 ALG`：**FAIL**，没有理论规定的专属不可交换运算或通用错误方向。
- `理论删除测试`：**FAIL**，删除理论名称后，数据、生成器、world model、policy、动作与损失均可原样保留。

按本项目门槛，这一项已经足以 NO-GO。

## 3. 直接近邻矩阵：剩余交集是否只是拼接

### 3.1 披露、补丁时机、采纳与容量

| 工作/政策 | 实际输入 | 实际动作 | 外部结果/状态 | 对本候选的挤压与边界 | 回读深度 |
|---|---|---|---|---|---|
| Cavusoglu, Cavusoglu & Raghunathan 2007，[TSE DOI](https://doi.org/10.1109/TSE.2007.26) | vulnerability risk、vendor incentives、用户/供应商成本、单/多 vendor | full vendor、immediate public、hybrid/responsible、grace period；扩展含 selected-user early warning | social loss、patch incentive、workaround/attack exposure | 已占据 scope/timing、selected privileged users、多供应商和 early discovery；候选不能声称首次提出私下通知选定下游。边界是无真实 remedy bytes、无 learned agent | 正式摘要＋作者全文索引正文；直链 502，未扩张公式 |
| Arora, Telang & Xu 2008，[MS DOI](https://doi.org/10.1287/mnsc.1070.0771) | benign discovery、vendor cost、attacker self-discovery、user loss | planner 选 protected period；vendor 选 `τ,q`；扩展 workaround | patch speed/quality、采纳、pre/post-patch loss | 直接占据 protected period、速度—质量—采纳冲突；剩余必须是 remedy-specific executable outcome | 46 页作者全文 |
| Cavusoglu, Cavusoglu & Zhang 2008，[MS DOI](https://doi.org/10.1287/mnsc.1070.0794) | vendor release cost、firm update/damage cost | time/event-driven release/update cycles、cost sharing、liability | synchronized social optimum、decentralized equilibrium | 已占据 upstream release—downstream update 协调；候选不能把 downstream adoption 本身当新机制 | 正式全文页＋作者全文索引 |
| Gao et al. 2026，[RESS DOI](https://doi.org/10.1016/j.ress.2026.112586) | vulnerability discovery、imperfect debugging、user diffusion/feedback | 联合优化 patch 数量与 periodic/non-periodic timing | residual vulnerabilities、expected lifecycle cost | 已把发现、修复缺陷、用户扩散和补丁时机放入一个优化模型；候选剩余不是 generic diffusion/timing，而是 remedy bytes 与信息包共同改变双方执行结果 | 出版方全文 preview/section snippets；付费 PDF 未取得 |
| Zhang, Demirezen & Kumar 2025，[ISR DOI](https://doi.org/10.1287/isre.2021.0349) | BBP 中 researcher 能力/数量、patching complexity、security posture、legal protection、leak-related cost | bounty 与 BBP 的博弈设计 | discovery、post-discovery cost、firm total cost | 直接占据 AI/外部发现增加后 post-discovery leak risk 与 patch complexity 的组织设计；候选不是 bounty 题 | 正式摘要/作者项目页；全文端点超时，未声称公式细节 |
| Liu et al. 2025，[TOSEM DOI](https://doi.org/10.1145/3716822)、[作者全文](https://xing-hu.github.io/assets/papers/tosem25shuhan.pdf) | 21,501 CVEs、8,073 OSS projects、issue/commit/advisory 路径与 practitioner survey | 观察 report、discussion、fix、disclose channel/path | CVD conformity、premature discussion、patch-at-disclosure | 已占据 OSS report→fix→disclose 实践、commit/patch 可泄露攻击信息与平台治理；是 observational taxonomy，不学反事实 policy | 31 页全文 |
| [Vultron / Designing Vultron](https://www.sei.cmu.edu/library/designing-vultron-a-protocol-for-multi-party-coordinated-vulnerability-disclosure-mpcvd/) | report、participants、embargo、case state | report management、embargo management、case state 三个 DFA | 协调状态、解除/延长 embargo、case completion | 多方 CVD 与 embargo 状态机已是正式协议；正文明确 content considerations 不在其主范围，故 remedy-specific 内容仍空，但“多方 router”不新 | SEI 页面＋完整 PDF |
| [FIRST multiparty CVD v1.1](https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1) | 多供应商、供应链和不同披露准备状态 | 私下协调、limited public notice、部署 patch/mitigation、升级协调 | 多方 readiness 和披露 | 已覆盖 bilateral CVD 不足、分阶段有限信息和供应链协同；不是 learned policy | 官方指南全文 |
| [CERT Guide to CVD](https://certcc.github.io/CERT-Guide-to-CVD/howto/coordination/disclosure_timing/) | active exploitation、vendor progress、complexity、known users | 提前、延后、第三方协调 | contingent timeline | 正式政策已把 timing 写成情境决策，不存在一个公认固定最优 deadline | 官方网页 |
| [Project Zero 2025 Reporting Transparency](https://projectzero.google/2025/07/reporting-transparency.html) | vendor/product/report date/deadline、upstream/downstream patch status | 约一周后只公开高层 metadata；90+30；保留技术细节/PoC | upstream patch gap、end-user adoption gap | 已实现“公开压力但不泄露技术细节”的阶段化 action，并显式追踪下游；候选必须超越 generic staged disclosure | 官方政策与 tracker |
| [Anthropic 2026 CVD](https://www.anthropic.com/coordinated-vulnerability-disclosure) | AI-found、human-confirmed vulnerabilities；maintainer capacity、active exploit、ecosystem scope | private report、suggested candidate fix、90d/7d、patch 后通常再等 45d 发 full details、按维护者可吸收速率提交 | patch/mitigation readiness、downstream deployment buffer | 几乎逐项覆盖候选现实流程；尚不是 learned counterfactual policy，也不自动生成生产级 patch | 官方政策全文 |
| [OpenAI outbound CVD](https://openai.com/policies/outbound-coordinated-disclosure-policy/) | validated AI/agent finding、human review、vendor responsiveness | private by default；必要时协调 CERT/CISA 或公开；无硬性统一期限 | coordinated remediation | 已占据“agent 发现→人工复核→私下协调”的政策流程；非 learned policy | 官方政策全文 |
| [Cisco risk-based disclosure 2026](https://sec.cloudapps.cisco.com/security/center/resources/risk-based-disclosure) | AI 增加的发现量、severity、产品/平台、release cadence | twice-monthly hardening releases、7-day advance metadata、紧急 out-of-cycle | 客户预留 change window、批量吸收与部署 | 直接证明组织会用 batch/cadence 管理 AI finding volume；候选不能把 queue/batching 当原创 | 官方页面全文 |
| Gordeychik 2026, [UPS Meets Patch Queues](https://papers.ssrn.com/sol3/Delivery.cfm/6286359.pdf?abstractid=6286359&mirid=1) | evidence timeline、KEV、capacity/cadence/compliance | queue prioritization | time-to-patch、compliance、backlog | 低权重 SSRN 近邻，已占有限容量优先级；不含真实 patch 生成、披露内容或 attack diffusion | 19 页预印本 |

### 3.2 攻防竞速、补丁策略与 patch-as-signal

| 工作 | 实际输入/状态 | 动作 | 结果 | 与本题的精确边界 | 回读深度 |
|---|---|---|---|---|---|
| Mitra & Ransbotham 2015，[ISR DOI](https://doi.org/10.1287/isre.2014.0560) | IDS attacks、disclosure mechanism、attack/protection diffusion 与 busy period | 观察 full/limited disclosure，不执行补丁 | first attack、attack volume/effective life | 占据 opposite diffusion＋busy moderation，但没观察 defender action/quality/compromise | 本地全文 |
| Arora et al. 2010，[ISR DOI](https://doi.org/10.1287/isre.1080.0226) | vendor/vulnerability、actual disclosure time | vendor patch release | patch hazard | 占据 disclosure pressure→patch speed；不是反事实策略 | 本地全文 |
| [The Oracle’s Gambit, arXiv:2607.05442](https://arxiv.org/html/2607.05442v1) | attacker/defender capability rates、detect/create/test/ship/adopt stages | 选择 model-access/timing；attacker 可逆向 shipped patch | defender coverage、attack success、head-start timing | 最直接占据 patch release 同时开启 defender adoption 与 patch-diff attack route；但 rates 合成、n≤3、synthetic、无真实代码/多方 CVD | 全文 |
| Faghani et al., [When Discovery Outpaces Remediation, arXiv:2606.11022](https://arxiv.org/html/2606.11022v1) | latent vulnerability pool、backlog、capacity、triage degradation、propagation graph | capacity/segmentation interventions | compromise propagation、queue collapse | 直接占据发现超过修复、容量瓶颈与传播；synthetic、未校准、不生成 remedy 或 disclosure | 全文 |
| [ADAPT, JNCA 2026](https://doi.org/10.1016/j.jnca.2026.104436)、[作者全文](https://www.uclab.re.kr/publications_openaccesspdf/uamr_jnca_2026_open.pdf) | `(S,D,P,x)` attack/dependency state、CVSS/EPSS/KEV、existing patches | binary patch selection `a_t` under CMDP/PPO | scalar network risk、cost/constraints | 已占据 attack-graph 上的 RL patch prioritization；不生成 source patch、不披露、风险过度标量化 | 正式全文 |
| **VulnGym-APT**, [arXiv:2607.24552](https://arxiv.org/html/2607.24552v1)、[代码](https://github.com/dessertlab/vulnGym) | 100-node shared evolving network、2020 NVD CVEs、两类 topology、APT28/APT41 profiles、limited patch effort | DQN attacker 选 scan/exploit/lateral/persistence 等；defender 按 severity/importance/centrality 周期扫描与 patch queue | goal achievement、compromised-node NVI、time-to-goal、time-to-patch、backlog | **最强新增近邻**：已覆盖真实 CVE、攻防共演、补丁预算、策略/优先级与 RL。Defender 是 fixed configurable policies，patch 是抽象状态切换；不生成/验证代码，不含 disclosure 或 patch-diff channel。候选若删除 remedy bytes 便被其直接吸收 | 论文全文、方法/实验/validity、官方代码链接 |
| [PatchWeaver, USENIX Security 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/li-rui)、[全文](https://www.usenix.org/system/files/usenixsecurity26-li-rui.pdf) | 持续刷新、版本化且带 hash 的 K8s assets/dependencies/identities/vulnerabilities/approvals/evidence graph | typed remediation plan：build/sign image、deploy/canary、RBAC、approval；rollout 预测政策违规 | progress、step/episode violations、operational policy | 版本化异构图、可执行 remediation 与 risk-bounded rollouts 已被占据；不改源代码、不控制 CVD，跨组织协商明确超范围 | USENIX 正式全文 |
| [PatchAgent, USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/yu-zheng) | PoC-triggered vulnerable program、language server、tests | localization→patch generation→verification | end-to-end repair | “同一 agent 生成并验证真实 patch”本身不新；不处理 disclosure/diffusion | 正式全文页/PDF |
| [KeaRepair, arXiv:2607.00820](https://arxiv.org/html/2607.00820v1) | repo、vulnerability description、历史 vuln-patch knowledge、verified program facts | ReAct diagnosis、RAG patch、compile/PoC replay/tests、iterative refine | 55 个 C/C++ 可复现实例与 cross-language repair | 真实 remedy 生成/验证已被直接占据；不协调 CVD | 全文 |
| [PatchEval-Verified](https://github.com/bytedance/PatchEval) | 230 个 Docker CVE cases、repo/description/image、strengthened PoC | coding agent 输出 source patch；harness fix-run | correctness/PoC/hidden tests | 真实可验证 patch benchmark 已成熟；当前 image 内含 evaluator `fix.patch`，policy 必须隔离以防泄漏。官方表截至截止日已有强 frontier 结果，不能用弱 patch baseline | 官方 repo、schema、runner、leaderboard |
| [PoCEvolve, arXiv:2607.22076](https://arxiv.org/pdf/2607.22076) | security patch commit＋repo | 从 diff 生成/evolve PoC；Docker replay | PoC success、patch-to-CVE timing | 直接占据 remedy-specific patch→PoC，候选不能声称首次发现 patch-as-signal；JS/npm 与公开 VFC 范围限制外部效度 | 全文 |
| [Anthropic N-day exploit study, 2026-06-08](https://www.anthropic.com/research/n-days) | public patch diff（移除 maintainer regression test）、pre/post vulnerable builds 或 Windows binaries、逆向工具 | LLM 生成并迭代 N-day PoC/exploit | 是否在隔离 harness 触发 vulnerable build 且 patched build 不触发、time/cost | 是 patch-diff information-exposure oracle 的最直接现实基线；不是 IS 理论或 disclosure policy learner | 官方研究全文页 |
| [RETRACE, arXiv:2608.08950](https://arxiv.org/abs/2608.08950) | issue、agent trajectory、candidate patch | forward/backward reconstruction、independent alignment、reconciliation | patch acceptance/correction | 截止日前新增的独立 patch verification 近邻；仍不控制 CVD。只作为 patch verifier baseline，不扩张其 SWE-bench 结果到安全 CVE | 全文 |

### 3.3 两个同名 VulnGym 必须分开

| 名称 | 标识 | 单位与任务 | 本题角色 |
|---|---|---|---|
| VulnGym-APT | [arXiv:2607.24552](https://arxiv.org/html/2607.24552v1) | 企业网络、APT attacker、有限 patch queue、策略 stress test；100-node simulation、真实 CVE metadata | 强近邻/环境与 policy baseline；挤压攻防仿真＋RL＋优先级 |
| VulnGym-Repo | [arXiv:2608.02001](https://arxiv.org/html/2608.02001v1)、[官方数据](https://github.com/Tencent/VulnGym) | 23 repos、184 advisories、408 entry points 的 repository-level white-box vulnerability detection/evidence task | 数据入口/检测 baseline；不修补、不披露、不做网络攻防策略 |

不能把二者数字、代码或结论互相引用。前者的 CVE 是模拟网络状态，后者的 unit 是真实 repository entry/evidence chain。

### 3.4 “是否已有完全同输入—动作—外部结果的联合 learned agent”检索结论

检索组合覆盖 `joint patch generation disclosure timing`、`coding agent coordinated vulnerability disclosure`、`remedy-specific information release RL`、`patch-as-signal policy`、`vulnerability remediation diffusion agent`，并沿上述正式论文的参考和被引线索检查。截止日内，本次回读没有找到单一正式工件同时满足：

1. 输入是一个真实 repository vulnerability、维护容量、下游依赖/部署和分阶段信息状态；
2. 动作既输出并执行真实 patch/mitigation/backport bytes，又输出 recipient/scope/timing 的 CVD artifact；
3. 同一 remedy bytes 在 common-seed 隔离 attacker 与 defender rollouts 中分别产生可执行结果；
4. policy 由这些 counterfactual outcomes 学得，而非固定规则或手工优化。

这是一项**有限范围的未定位结论**，不是“世界上首次”的证据。更关键的是，把 PatchAgent/KeaRepair/PatchEval、PoCEvolve/Anthropic N-day、Vultron/FIRST/现实政策与 Oracle/VulnGym-APT/ADAPT 串联即可得到该 I/O。没有不可替代 MEC→MAP→ALG 时，联合空位仍是模块拼接。

## 4. 七项不可替代性与独立性门

| 门 | 反事实检验 | 证据 | 判定 |
|---|---|---|---|
| 1. 是否只是 patch agent＋CVD router | 固定 KeaRepair/PatchAgent 生成器，外接 Vultron/Project Zero/Anthropic 规则；再与 learned controller 比较 | 两侧已有成熟工件；联合模型尚无专属中间运算 | **FAIL** |
| 2. 等参数 generic model 能否复制 | 给 raw temporal graph Transformer＋distributional SMDP 完全相同原始输入、action bytes、各 head labels、rollout 和预算 | 理论只规定 state typing，没有通用模型错误方向 | **FAIL；核心撤题门** |
| 3. historical one-policy 是否识别反事实 | 同一 CVE 是否有多组 remedy/scope/timing 且共享外生随机数 | 公开历史只有实际路径；advisory/registry 不是 action counterfactual | **FAIL** |
| 4. 删除 coding agent 后问题是否完整 | 用协调者＋已有 patch artifacts 替代 generator | timing、capacity、selected downstream、adoption 和 disclosure 仍完整；只少了字节生成 | **FAIL；agent 是实施器** |
| 5. action space 是否有唯一可训练能力 | 改变 remedy bytes 时，defender correctness/adoption 与 attacker diff-reversibility 是否共同变化 | 原则上存在，但 patch generation 与 diff exploitation 已分别被占；IS 理论未规定选择函数 | **PARTIAL，不足以救题** |
| 6. 与迁移题/C3 是否独立 | 排除 schema/data cutover；固定人审主体与 evidence UI，不选择如何说服 reviewer | 现象、数据和安全结果可分；若选择 maintainer/reviewer 或呈现证据则回到 C3 | **PASS at phenomenon，非贡献救济** |
| 7. 双用途边界是否可守 | 仅 public-known/synthetic clone、sealed Docker、无外网、不公布 exploit/PoC、真实 disclosure 由人负责 | 可设计合规环境，但 attacker artifact 仍高风险且需访问控制/删除 | **CONDITIONAL ethics** |

终局由第 2、3、4 门触发。第 5 门说明一个可能有工程价值的 benchmark；它没有把题目恢复为 ISR 级理论驱动算法。

## 5. 最强 steelman 工件：即使 NO-GO，也必须能被完整复现

### 5.1 episode、可见输入与隐藏真值

每个 episode 锁定一个已公开 CVE 或安全 synthetic/morphed clone、一个 vulnerable repository snapshot、至少一个受影响版本和两个 downstream deployment variants。所有实例在无外网、可重置 Docker/VM 中执行。episode 的起点是 finder 已在授权环境中验证 vulnerability exists；终点是修复被验证并进入选定下游、披露阶段完成或 horizon 到期。

推断时允许看见：

- repository 文件、build manifest、dependency lock、AST/CFG、vulnerable version、公开 issue/advisory 中在该时点已经公开的字段；
- 一个最小、去危险化的 private report，包含触发条件类别和 evaluator 提供的 sealed reproducer handle，但不直接暴露 gold fix；
- maintainer queue length、role/ownership、release calendar、历史响应速度、可用 testing/backport hours；
- package/version/downstream dependency graph、公开 registry versions、截至时点的 adoption counts；
- agent 自己此前执行的 commands、diff、visible tests、compiler/sanitizer output、recipient acknowledgements 与 disclosure state。

推断时禁止看见：gold patch、`fix.patch`、hidden tests、未来 commit/advisory、未来 exploitation/adoption、paired-world sibling 的 outcome、evaluator-only PoC 和 solution seed。PatchEval image 中若保留 `/workspace/fix.patch`，runner 必须 mount-mask 或把 evaluator 与 policy container 分离。

### 5.2 版本化 temporal heterogeneous graph

时间 `t` 的图为 `G_t=(V_t,E_t,X_t,M_t)`，所有节点/边带 `valid_from`、`valid_to`、content hash、source、visibility 与 confidence。节点类型只保留七类，避免无界堆模块：

1. `vulnerability`：CWE、severity、known-exploitation、公开/私密状态；
2. `code_region`：file/function/AST/CFG region 与 version；
3. `remedy`：patch、mitigation、backport candidate 及其 parent candidate；
4. `maintainer`：owner、review/CI/backport capacity 和 queue state；
5. `package_version`：upstream release、registry version、dependency lineage；
6. `downstream_deployment`：consumer、criticality、deployed version、mitigation/patch state；
7. `disclosure_artifact`：private report、limited metadata alert、mitigation notice、patch/release、technical advisory。

边类型固定为 `affects`、`located_in`、`fixes`、`mitigates`、`backports_to`、`depends_on`、`deployed_as`、`owned_by`、`queued_at`、`notified_to`、`reveals`、`supersedes` 和 `validated_by`。recipient、release 与 disclosure 不是自由文本标签，而是图上的实际状态变化。

设 batch `B`、时间步 `T`、图节点 `N`、代码 token `L`、候选 remedy `K`、下游 `J`、候选联合动作 `A`：

\[
X^G\in\mathbb{R}^{B\times T\times N\times d_g},\quad
E^G\in\{1,\ldots,R\}^{B\times T\times N\times N},\quad
X^C\in\mathbb{R}^{B\times L\times d_c},
\]

\[
M^{vis}\in\{0,1\}^{B\times T\times N},\quad
Z^{rem}\in\mathbb{R}^{B\times K\times d_r},\quad
Z^{down}\in\mathbb{R}^{B\times J\times d_d}.
\]

`M_vis` 必须在 manifest 中逐字段登记；把未来 advisory 或 evaluator-only test 隐藏在 embedding 中也算 leakage。

### 5.3 四个且仅四个 learned blocks

1. **Graph/code encoder。** 一个 typed temporal graph Transformer 处理 `G_≤t`；一个共享的 code/AST encoder 处理 repository region。二者通过 vulnerability↔code、remedy↔code edges 交互，输出 `H_t^G`、`H^C`。这算一个表示 block，不再另堆 dependency、maintainer 和 disclosure encoder。
2. **Executable remedy generator。** 固定开放 checkpoint `Qwen/Qwen2.5-Coder-7B-Instruct`，以 4-bit NF4 QLoRA、rank 64、alpha 128、target `q/k/v/o/up/down/gate` 训练。一次生成至多 `K=8` 个 typed artifacts：source patch、runtime/config mitigation、supported-branch backport。每项必须包含 unified diff、build/test command、affected versions 和 rollback。checkpoint 的 exact revision/hash 在 preregistration 后冻结；未冻结 hash 不得称为复现完成。
3. **Coupled survival/diffusion world model。** 共享 latent state，但输出五个互不替代的分布：攻击到达/扩散 hazard、remedy readiness hazard、patch quality distribution、下游 protective-adoption hazard、维护队列/忙碌状态 transition；另输出 remedy-specific information exposure。它不是一个 scalar risk network。
4. **Constrained distributional offline SMDP policy。** semi-Markov action duration 由真实 build/test/backport/coordination time 决定；quantile critic 预测多结果分布，expectile value/advantage-weighted actor 只在 behavior support 内更新，并以 Lagrange multipliers 满足安全、容量与任务完成约束。

compiler、test runner、sanitizer、package builder、Vultron DFA 和 sealed attacker harness 是 deterministic tools/oracles，不计为 learned modules。这样已经足够 steelman；继续增加独立“ethics network”“CVD LLM”“maintainer LLM”只会掩盖可替代性。

### 5.4 完整前向计算

表示阶段：

\[
H_t^G=f_{TG}(X^G_{\le t},E^G_{\le t},M^{vis}),\qquad
H^C=f_{AST}(X^C),\qquad
h_t=\operatorname{Pool}(H_t^G,H^C,a_{<t}).
\]

生成阶段由 7B QLoRA 以 `h_t`、可见 report 和 repository context 产生 `K` 个 remedy bytes。每个 candidate 在 policy 可见的 verifier 上运行 compile、public/visible tests、sanitizer 与 limited regression；结果编码为：

\[
z_k=[h_t,\operatorname{Enc}(\Delta_k),v^{compile}_k,v^{visible}_k,cost_k,targets_k].
\]

`hidden-test`、gold-patch similarity 和 sealed exploit success 不进入 `z_k`。训练时它们可作为 outcome labels；评估时只由 evaluator 在 action commit 后计分。

对每个联合动作 `a=(k,e,r,c,\tau)`，`k` 是 remedy candidate，`e` 是 testing/backport/coordination effort allocation，`r` 是 recipient subset，`c` 是 content tier，`τ` 是下一决策或释放时间。world model 预测：

\[
\lambda^A_{t,u}=\operatorname{softplus}(g_A(h_t,z_k,r,c,u)),\quad
\lambda^R_{t,u}=\operatorname{softplus}(g_R(h_t,z_k,e,u)),
\]

\[
Q_k\sim\operatorname{Beta}(\alpha_Q,\beta_Q),\quad
\lambda^D_{j,t,u}=\operatorname{softplus}(g_D(h_t,z_k,j,r,c,u)),
\]

\[
W_{t+1}\sim p_W(\cdot\mid h_t,e,r,k),\quad
I^{diff}_{k,c}\sim p_I(\cdot\mid \operatorname{Enc}(\Delta_k),c).
\]

`A/R/Q/D/W/I` 分别是 attack、readiness、quality、defensive adoption、workload 和 information exposure。coupling 只通过共享 state 和显式交叉项发生，例如 patch ship 会同时改变 `λ_D` 与 `I_diff→λ_A`；不得把五项先相加再预测。

policy critic 输出每个结果通道的 `M` 个 quantiles：

\[
Z_\psi(s_t,a)\in\mathbb{R}^{A\times O\times M}.
\]

actor 只在 legal/behavior-support mask 内产生联合动作概率，并以各结果分布而非压平后的 risk score 选择动作：

\[
\pi_\theta(a\mid s_t)=\operatorname{MaskedSoftmax}\!\left(f_\theta(h_t,z_a,\widehat Y_a)\right),
\qquad
a_t^*=\arg\max_{a\in\mathcal A_{legal}}\mathbb E[U(Z_\psi(s_t,a))]
\]

\[
\text{s.t. }\operatorname{CVaR}_{\alpha}\!\left(C_\ell(s_t,a)\right)\le b_\ell,
\quad \ell\in\{critical\ compromise,hidden\ regression,maintainer\ load,disclosure\ delay\},
\]

其中 duration `d(a)` 推进 semi-Markov clock，`U` 同时保留任务完成与正常服务效用；它不得给永久保密、全拒绝或无限 handoff 正奖励。

推断时先删除 compile fail、违反 embargo/authorization、超出维护预算或无法 rollback 的动作，再在预注册约束下选择 Pareto 可接受动作。结果必须是真实执行：写入 diff，构建 patched image，运行 visible verifier，更新选定 downstream clone 和 disclosure DFA；不能只输出 recommendation text。

### 5.5 动作空间必须包含可验证代码工件

| 动作族 | 参数 | 必须改变的外部对象 | 成功证据 |
|---|---|---|---|
| 私下验证 | `run_probe(test,scope)`、`minimize_reproducer` | isolated image、sealed evidence store | vulnerable build 可复现且 patched/control 不误触发；不生成可外发危险细节 |
| 生成修复 | `apply_patch(diff)`、`apply_mitigation(config)`、`backport(diff,branch)` | repository、config、supported branch | compile、PoC neutralization、visible/hidden regression、artifact hash |
| 分配努力 | `allocate(test_hours,review_slots,backport_slots)` | maintainer queue、CI slots、release plan | consumed time、queue wait、完成/失败状态 |
| 防御协调 | `notify(recipient,content_tier)`、`stage_downstream(remedy)` | selected downstream clone、private notice | acknowledgement、successful build/deploy、coverage time |
| 分阶段释放 | `publish_metadata`、`publish_mitigation`、`ship_patch`、`publish_advisory` | disclosure artifact、registry/release | exact bytes/hash、recipient/scope/time；attacker 只获得该阶段内容 |
| 恢复/停止 | `rollback_candidate`、`supersede_remedy`、`escalate_human` | repository/deployment/DFA | rollback verified；handoff 单列成本且不自动算安全成功 |

`allow/withhold/disclose` 三分类不合格。相反，若只生成 patch 而 `r,c,τ` 固定，则退化为 AVR；若只选 `r,c,τ` 而 remedy bytes 外生，则退化为 CVD router/patch policy。

### 5.6 标签、损失与训练阶段

标签必须分开：

- `y_attack`：在 sealed attacker rollout 中首次 exploit/compromise 时间、受损 critical assets 和 attack diffusion path；
- `y_ready`：remedy 达到预注册 build＋visible validation threshold 的时间；
- `y_quality`：PoC neutralization、hidden regression、incomplete fix/bypass、cross-version correctness；
- `y_adopt`：每个 downstream 成功 mitigation/patch、失败或仍暴露的时间；
- `y_load`：triage/review/CI/backport work、queue length、busy period；
- `y_info`：仅由该 disclosure tier 或 patch diff 可得时，sealed attacker 是否重建有效触发；不保存可公开复用 PoC。

world model loss 为：

\[
\mathcal L_{WM}=\mathcal L_{surv}^{A}+\mathcal L_{surv}^{R}+\mathcal L_{beta}^{Q}+\mathcal L_{surv}^{D}+\mathcal L_{NLL}^{W}+\mathcal L_{NLL}^{I}+\lambda_{cal}\mathcal L_{cal}.
\]

generator 先以历史 vulnerability-fix pairs 作 QLoRA SFT，再以 compile、visible tests 和安全 verifier 的 pairwise ranking 学 candidate selection；gold patch 只在训练样本中作为 target，evaluation lineage 完全隔离。policy 使用 quantile Huber Bellman loss、expectile value loss、advantage-weighted behavior cloning 和 conservative support penalty；constraints 分别对 hidden-regression risk、critical compromise、maintainer budget、task completion 和 disclosure deadline 建 Lagrangian，而不是优化一个永久保密可取胜的 reward。

训练严格分五阶段：

1. 只用 train lineage 预训练 graph/code representation 与 QLoRA remedy generator；
2. 用历史单一路径拟合静态字段、build prior 和 hazard calibration，**不**学习 policy effect；
3. 在 train Docker twins 上执行 common-seed paired actions，拟合 coupled world model；
4. 冻结 generator/encoder 的 preregistered checkpoint，训练 constrained distributional offline SMDP；
5. 冻结全部参数，在未见 lineage、双世界变体和 seeds 上一次性评价。

checkpoint manifest 至少包含：base model ID/revision、LoRA config/hash、tokenizer hash、graph schema version、world-model/policy state dict hash、optimizer/scheduler、random seeds、Docker image digests、repository commit、dataset row hashes、visibility mask、action budget、tool versions和每次 command log。只给 prompt 或 notebook 不算复现。

### 5.7 本地算力边界

最小可行本地规格预估为一张 24GB GPU、24–32 CPU cores、128GB RAM、至少 2TB NVMe；7B NF4 QLoRA 用 gradient checkpointing/accumulation，graph/world/policy 分阶段而非同时驻留。Docker paired rollouts 更受 CPU、磁盘与 build time 限制。该规格是**设计预算，不是已核验的本机配置或运行记录**。若真实机器低于此规格，应缩小 train episodes/K/horizon，不能更换成 API frontier model 后仍宣称“本地可复现”。frontier API 只作外部 baseline，调用日期、model snapshot、token/tool budget必须冻结。

## 6. 数据与 policy 识别

### 6.1 公开资产各自只承担其原责任

| 资产 | 可提供什么 | 不可提供什么 | 合法用途 |
|---|---|---|---|
| [PatchEval-Verified](https://github.com/bytedance/PatchEval) | 230 个 Docker CVE、强化 PoC、patch correctness harness | 多方 CVD、下游采纳、维护队列、同一状态多政策结果 | source-patch generation/verification pretraining 与 held-out evaluator |
| [VulnGym-Repo](https://arxiv.org/html/2608.02001v1) | 184 advisories、408 entry points、23 repos 的检测/evidence ground truth | remedy、CVD 或 diffusion | finder/evidence encoder pretraining；与 VulnGym-APT 分开 |
| [CVE-Bench](https://github.com/uiuc-kang-lab/cve-bench) | 40 个 critical web CVE 的可执行 exploit-oriented environments | patch policy、adoption、CVD | 仅 safe subset 的 sealed attack evaluator；不得外发 PoC |
| [SEC-bench](https://github.com/SEC-bench/SEC-bench) | OSV/CVE 自动构造、Docker、patch 与 PoC modes | 组织/下游状态、政策反事实 | patch/PoC baseline 与 instance builder |
| [Vul4J](https://github.com/tuhh-softsec/vul4j)、VJBench/VJBenchTrans | Java reproducible vulnerabilities、PoV、candidate patch compile/test | disclosure/adoption trajectories | cross-language remedy generation；同 lineage split |
| [OSS-Fuzz](https://google.github.io/oss-fuzz/)、[OSS-CRS/CRSBench](https://oss-crs.openssf.org/) | 多语言 fuzz harness、private bug workflow、统一 bug-find/fix/triage/seed/harness interface | CVD policy labels或维护者反事实 | safe clone、fuzz verifier、frontier/open CRS baselines |
| CVEfixes、JavaVFC/VFC | 历史 vulnerability-fixing commits、code/diff metadata | 未采取 patch、hidden regression、披露包结果 | generator SFT 与 code-diff representation；只作 history |
| [OSV](https://osv.dev)、[GHSA](https://github.com/advisories)、[NVD](https://nvd.nist.gov) | advisory、affected/fixed versions、severity/links/time | 完整 first-private-report time、未公开协调、反事实 | graph metadata 与 time-safe features |
| [deps.dev](https://deps.dev) 与 registry histories | dependency/version graph、release/adoption proxy | 真实部署或组织内 patch adoption | downstream proxy/calibration；不得称为 firm deployment truth |
| VulnGym-APT | shared attacker/defender network、patch effort、TTPV/backlog/compromise metrics | executable source remedy 与 patch-as-signal | simulator baseline；不可把抽象 patch 状态当真实修复 |

### 6.2 历史单一路径只做 pretraining/calibration

对一个真实 CVE，历史通常只观察：某个报告渠道、某个 vendor response、某个最终 fix commit、某个 advisory 时间和不完整的 registry adoption。不存在“同一初态下同时选择 private-selected-downstream、public-metadata、ship-mitigation、ship-patch、full-details at day 7/45/90”的 outcomes。将 historical action 当 optimal label 会复制旧政策；inverse propensity weighting 也无法补出零支持的 remedy bytes/content tiers。

因此，历史数据只能：预训练 code/graph representation、SFT generator、估计 unconditional/actual-path hazard、校准 workload/adoption ranges。不得训练或宣称识别联合 policy value。

### 6.3 真正的识别单元：common-seed Docker twins

每个已公开 CVE 或安全 clone 生成一个 pre-state 和若干可观察上等价、隐藏 implementation/fault path 不同的 morphed variants。对每个合法联合 action，用同一 seed 固定外生 build noise、maintainer service time、downstream availability 和 attacker search budget，再产生：

- defender world：只有被通知的 recipient 获得对应 tier；实际应用 patch/mitigation/backport，记录正确性、部署与等待；
- attacker world：只获得当时已经公开/泄露的 metadata、advisory、binary/source patch diff；在 sealed container 内尝试重建 trigger，成功也只记录 evaluator token 与 time，不导出 exploit；
- control world：同 seed 但不提供该 artifact，估计 remedy/content-specific incremental signal；
- busy/normal twins：保持漏洞与动作相同，只置换 queue/load realization，测试 Mitra moderation。

一个 action effect 只能写成该封闭 benchmark 中的 paired difference，例如：

\[
\Delta Y(a,a')=Y(s_0,a,\omega)-Y(s_0,a',\omega),
\]

不能外推为真实攻击者或真实维护组织的因果效应。若 attacker/maintainer/adoption transition 全由理论参数直接生成，theory-factored policy 对该 simulator 的优势是构造效应；必须用与理论无关的 executable tests、真实 build times、held-out attacker agent 和多个 adoption models 降低循环性。

### 6.4 split 与泄漏纪律

- 同一 CVE、repository fork、package lineage、修复 commit 的 cherry-pick/backport、morphed clone、双世界 variant 全部进入同一 split。
- 主划分按 repository/package lineage；再做时间 holdout、language/CWE OOD 与 maintainer-capacity OOD。
- gold patch、future advisory、future exploit、future adoption 和 sibling outcome 永不进入 policy observation；所有 feature 按 episode clock 截断。
- 预训练模型可能记忆公开 CVE。必须报告 exact CVE exposure audit，以 synthetic/morphed holdout 检查记忆；不能把 gold-patch reproduction 当泛化。
- test/validation budget 对所有 patch agents相同；frontier agent、开放 agent和本模型使用同一 visible report、repository、tools、wall-clock/token/command budget。

这套设计能识别**benchmark 内**的联合 action value，却仍不能修复理论算法不可替代性。它是未来系统/安全 benchmark 的可行路线，不是当前 GO 依据。

## 7. 外部结果、基线、干预与撤题实验

### 7.1 结果向量，不用永久保密取胜

| 结果通道 | 计算 | 必须同时报告的失败模式 |
|---|---|---|
| criticality-weighted exposure-days | 每个 downstream 从漏洞进入可利用状态到 verified protection 的天数乘 asset criticality | quarantine/disable 造成的正常服务损失不得从 exposure 中消失 |
| isolated compromise | sealed attacker 在 critical downstream 的成功率、time-to-first/goal 与传播范围 | 仅计 Docker/VM；不得对真实服务尝试 |
| patch correctness | build、PoC neutralization、hidden tests、incomplete-fix/bypass、cross-version backport | 只过 public test、overfit PoC、删除功能均算失败 |
| time-to-validated remediation | report 到首个 production-eligible remedy，以及到各 supported branch | 生成快但验证/回移植慢须分开 |
| downstream defensive adoption | time-to-mitigation/patch、criticality-weighted coverage curve、failed deployment | release 不等于 adoption；registry download 只是 proxy |
| maintainer load | triage/review/CI/backport hours、queue wait、interruptions、busy-period overload | 把工作隐性转给下游/人审不得漏计 |
| information exposure | 每个 tier 的 attacker incremental success/time reduction、diff reconstruction rate | patch 本身的 signal 单列；不得仅以公开/未公开二元替代 |
| cost/normal utility | GPU/CPU、tokens、build minutes、downtime、功能损失、人工沟通 | 全拒绝、永久保密、永远 disable、无界 handoff 不能成为最优 |

策略必须在预注册 minimum task-completion、maximum functionality loss、maximum disclosure delay 与 maintainer budget 下报告 Pareto frontier。安全通道和任务通道都不允许用一个加权总分隐藏。

### 7.2 公平基线

所有 learned baseline 获得相同 raw graph/code/report、候选 action schema、supervision、train episodes、hidden evaluator隔离和总预算：

1. frontier coding agent 与开放 7B patch agent；PatchAgent、KeaRepair、SEC-bench/OSS-CRS strongest configured patchers；
2. fixed 7/45/90-day policies；immediate/full、private-until-patch、disclose-on-patch；Project Zero 90+30/metadata-first 与 Anthropic policy simulator；
3. PatchWeaver typed policy/rollout baseline；
4. ADAPT attack-graph patch policy；VulnGym-APT severity/importance/centrality policies；
5. Faghani queue/capacity policy；Arora protected-period policy；Cavusoglu synchronized release/update 与 Gao periodic/non-periodic policies；
6. **equal-parameter raw temporal heterogeneous graph Transformer＋distributional SMDP**，得到完全相同 inputs、action bytes、labels 和预算；
7. anonymous coupled-factor model：仍有相同 head 数和参数，但随机置换 attack/readiness/quality/adoption/load 的名称与专属连接，检查增益来自 supervision/容量还是理论；
8. oracle upper bound：可见 gold future outcomes，仅作 ceiling，不参与训练或部署。

若理论模型只比 fixed deadlines 强、却不能稳定胜过第 6/7 项，则 ISR 贡献失败，即使系统比现行 CVD 更好。

### 7.3 必做机制干预

| 干预 | 保持不变 | 被删除/打乱 | 理论预期；未运行 |
|---|---|---|---|
| collapse attack/defense diffusion | artifacts、总事件数、成本 | 把两个 diffusion process 合成单一 exposure rate | theory-factored 优势应消失；否则分头只是参数增容 |
| shuffle workload | CVE/remedy/disclosure 和边际 load 分布 | maintainer busy periods 在 episode 间置换 | 若 busy moderation 真进入 policy，action ranking/披露节奏应改变 |
| remove disclosure pressure | attacker information channel 保留 | `disclosure→patch readiness hazard` 路径置零 | public-pressure 动作价值应下降 |
| remove patch reverse-engineering channel | patch correctness/adoption 保留 | attacker 看不到 diff/binary delta | ship-patch 的防守收益保留而攻击成本消失，ranking 应反转于部分情境 |
| neutralize protected period | 其他状态保留 | 所有 content tiers 在同一时刻可见 | staged disclosure 的独立价值应消失 |
| equalize remedy bytes | effort/scope/timing 保留 | 不同 policy 使用同一个 verified patch | 若优势仍全在 timing/router，则 coding agent 可删 |
| hide theory labels from both | raw observations/actions/outcomes 保留 | 不给任何 factor labels | 测量收益与理论运算收益分离 |

### 7.4 预注册撤题条件

即便未来获准只做 pilot，以下任一发生就不再 rescue：

- matched generic model 在主要外部结果与 OOD 上复制 theory-factored model；
- equalize remedy bytes 后性能不变，说明联合 agent 实际只是 CVD router；
- 替换为外生 gold/strong patch 后 policy 问题仍完整，说明 coding agent 可删；
- paired action 在 common seeds 上没有可重复的 ranking reversal；
- information-exposure head 只预测公开/未公开，而不能区分不同 remedy bytes/content tiers；
- world model 只在由自身规则生成的 simulator 上校准，换 held-out attacker/adoption model 即失效；
- 通过全拒绝、永久保密、无限等待或过度 disable 获得表面安全；
- 任一真实未披露漏洞、真实生产目标或可复用危险 PoC 进入实验/公开 artifact。

## 8. 双用途与现实治理边界

研究环境只允许已公开 CVE、已修复历史版本或安全 morphed clones；必须有仓库许可和明确测试授权。网络默认 deny-all，container 无云凭据、无宿主敏感路径、无真实 package publish token。attacker 与 defender runner 分离，PoC/evaluator artifact 加密、最小权限、访问审计并在 retention 到期后销毁。论文和 artifact 只发布 instance builder、非危险 aggregate labels、patch correctness 和 disclosure-state traces，不发布能够迁移到真实未修复系统的触发细节或 exploit chain。

实验中的 `publish`、`notify`、`ship` 都只作用于模拟 registry、mock maintainer 和 isolated downstream。任何研究过程中偶然发现的新真实漏洞立即退出数据流程，交由人工安全负责人依 [OpenAI outbound CVD](https://openai.com/policies/outbound-coordinated-disclosure-policy/)、[Anthropic CVD](https://www.anthropic.com/coordinated-vulnerability-disclosure)、FIRST/CERT 或项目 policy 处理；模型不自主联系真实维护者、不作最后 disclosure 决定。

这些控制让安全 benchmark 原则上可做，却不能消除 attacker-side research 的剩余风险，也不是 NO-GO 的主要理由。

## 9. `00W` 精确句键与强化 `00F` 功能审计

下表不是按“引言—理论—方法—结果”的位置类比。每行只使用一个 `00W` 段落主键和一个真实语法句 ID，并显式记录固定链：**PRE→SRC_NEW/CAND_NEW→REL→CIT→NEXT→RESULT**。`source_function_code` 来自肖老师原句在原论文中的主功能；`candidate_function_code` 是本文件候选句实际承担的功能。代码相同仍需比较前提、引文与后继义务；代码或推进责任不同即写“位置参照，非功能同位”或“无同功能锚点”，不强配。

`责任状态` 的 PASS/PARTIAL/FAIL/NO-GO 评价该句能否兑现功能同位与候选责任，不是本题经验表现。`RESULT` 严格按 `00F` 只取“保留、改写、拆分、合并、删除”；所有 EVAL 行都是未运行设计，没有任何 RES 行被候选伪造。

| ID | `00W` 精确句键 | `source_function_code` | `candidate_function_code` | 责任状态 | `PRE→SRC_NEW/CAND_NEW→REL→CIT→NEXT→RESULT` |
|---|---|---|---|---|---|
| V01 | `ACAA-I1 / ACAA-I1-S01` | CXT | CXT | PASS | PRE=尚未建立情境 → SRC_NEW=肖文建立日常信息渠道 / CAND_NEW=AI finder、patch generator、maintainer queue、downstream deployment 与 disclosure artifact 共同构成漏洞协调情境 → REL=均先建立具体信息工作流，功能同位 → CIT=Anthropic CVD、Project Zero 与 PatchWeaver 官方来源仅支持现实渠道；联合情境是候选定义 → NEXT=说明该情境产生何种外部损害 → RESULT=保留 |
| V02 | `ACAA-I1 / ACAA-I1-S02` | IMP | IMP | PASS | PRE=已建立漏洞协调渠道 → SRC_NEW=肖文从渠道推进购买后果 / CAND_NEW=修复延迟、错误补丁、未采纳与信息过曝会分别影响 compromise、回归和 exposure-days → REL=均由渠道推进外部后果，内容不同但功能同位 → CIT=本地理论全文和 Anthropic N-day 只承担各自事实；本候选未测损害规模 → NEXT=说明行动怎样改变后果 → RESULT=保留 |
| V03 | `DSDL-I3 / DSDL-I3-S05` | IMP+MAP | IMP+MAP | PASS | PRE=损害已重要且维护容量有限 → SRC_NEW=肖文用预测改变资源分配的反事实闭合价值 / CAND_NEW=漏洞状态预测只有改变 remedy effort、recipient、content 和 timing 并执行后才是行动能力 → REL=预测→资源动作→外部结果，功能同位 → CIT=VulnGym-APT/UPS 支持容量与队列存在；行动价值是设计要求，未运行 → NEXT=冻结完整动作集 → RESULT=保留 |
| V04 | `ACAA-I4 / ACAA-I4-S03` | ACK+LIM | ACK+LIM | PASS | PRE=行动价值已建立 → SRC_NEW=肖文承认旧指标诊断价值后限定其群体稳定性 / CAND_NEW=CVSS/EPSS/KEV、fixed deadlines 和 CVD DFA 有用，但不表示 remedy-specific 双向执行结果 → REL=先承认再限定，功能同位 → CIT=FIRST、Vultron、ADAPT、VulnGym-APT 各自只承担原任务 → NEXT=给出直接近邻矩阵而非全称否定 → RESULT=保留 |
| V05 | `ACAA-I5 / ACAA-I5-S03` | MEC | MEC | PASS | PRE=简单风险/期限指标不足 → SRC_NEW=肖文引入过程理论 / CAND_NEW=Mitra 双扩散、Arora patch hazard 与 protected period 共同产生攻击、防护、就绪和质量的相反过程 → REL=由过程机制替代静态指标，功能同位 → CIT=四篇理论只按第2节责任使用 → NEXT=把机制映射为分开状态 → RESULT=保留 |
| V06 | `ACAA-L10 / ACAA-L10-S04` | ACK+GAP | ACK+LIM | PARTIAL | PRE=已回读 patch/CVD 文献 → SRC_NEW=肖文承认既有 causal content 分解后收窄 richer data 缺口 / CAND_NEW=真实 patch、diff exploit、CVD、攻防 RL 和 adoption 均已有直接工作，剩余只是它们尚未在一篇中联合 → REL=均经 ACK 收窄空位；候选只能得 LIM，不能自动得 GAP，部分同位 → CIT=§3 一手全文/官方 artifact → NEXT=检查联合空位是否产生不可替代计算 → RESULT=改写 |
| V07 | `ACAA-L11 / ACAA-L11-S04` | MEC→ALG | MEC→ALG | FAIL | PRE=联合空位仍可能只是拼接 → SRC_NEW=肖文明确规定通用 affinity 的错误方向并要求互补计算 / CAND_NEW=本题必须指出 generic world model 在 patch-as-signal 下会稳定选错何种 remedy/content action → REL=同为“通用错误方向→专用动作”的验收，功能同位 → CIT=四篇 IS 理论没有给出该稳定错误方向；判断来自全文对照 → NEXT=若不能给出则终止 ALG 新颖性 → RESULT=删除 |
| V08 | `DSDL-L8 / DSDL-L8-S05` | MAP→ALG | MAP→ALG | PARTIAL | PRE=理论可产生多个状态但专用算法未立 → SRC_NEW=肖文让理论状态同时改变训练和最终预测 / CAND_NEW=attack/readiness/quality/adoption/load 状态应同时进入 world-model losses 与 SMDP action value → REL=理论状态进入训练与输出，功能同位 → CIT=这是 steelman 设计，未运行；理论只支持状态语义 → NEXT=做 generic equal-label 对照 → RESULT=改写 |
| V09 | `ACAA-T1 / ACAA-T1-S04` | BND | BND | PASS | PRE=不能用理论名称包装模块 → SRC_NEW=肖文规定理论节须回答导出、充分性和设计指导三项责任 / CAND_NEW=本候选理论必须产生 MEC、不可替代 MAP 与专用 ALG，任何一项失败即 NO-GO → REL=理论验收合同，功能同位 → CIT=`00F` 与两篇主文承担写作标准；不是外部经验事实 → NEXT=逐层验收 → RESULT=保留 |
| V10 | `ACAA-T2 / ACAA-T2-S03` | BND | BND | PASS | PRE=已有理论过程 → SRC_NEW=肖文把研究责任限定到特定 processing stage / CAND_NEW=本题只研究已授权发现后的 remediation/CVD episode，不研究 zero-day hunting 或真实攻击 → REL=用阶段边界防止范围扩张，功能同位 → CIT=候选定义与伦理边界，无需借肖文引文支持安全事实 → NEXT=把抽象阶段落到真实节点 → RESULT=保留 |
| V11 | `ACAA-T3 / ACAA-T3-S07` | CXT→MAP | CXT→MAP | PASS | PRE=episode 边界已定 → SRC_NEW=肖文用真实界面路径把抽象粒度变成可观察节点 / CAND_NEW=七类 versioned nodes 与十三类 typed edges 把 vulnerability→code→remedy→package→downstream→disclosure 落到执行路径 → REL=抽象机制情境化为可观察图，功能同位 → CIT=PatchWeaver/Vultron只支持部分图/状态；完整 schema 是候选设计 → NEXT=规定张量与 forward → RESULT=保留 |
| V12 | `ACAA-T5a / ACAA-T5a-S03` | MEC | MEC | PASS | PRE=图已建立时间维 → SRC_NEW=肖文以旧/新信息获得不同处理机会导出时间机制 / CAND_NEW=同一 remedy 在未发布、metadata alert、patch ship 和 full details 阶段产生不同 attack/adoption hazards → REL=时间阶段改变作用方向，功能同位 → CIT=Arora 2008、Project Zero、Oracle’s Gambit 与 Anthropic N-day 分别支持阶段冲突 → NEXT=把阶段写入 hazard heads → RESULT=保留 |
| V13 | `ACAA-T5b / ACAA-T5b-S04` | ALG | ALG | PARTIAL | PRE=时间阶段机制已建立 → SRC_NEW=肖文把时间衰减转成明确权重更新 / CAND_NEW=policy 必须以 semi-Markov duration 和 actual disclosure clock 更新 action value → REL=均把时间机制写入计算，但本题并无理论指定的衰减函数，只是位置参照，非完全功能同位 → CIT=设计定义，未运行 → NEXT=不得把该设计冒充理论专用算法 → RESULT=改写 |
| V14 | `ACAA-T6a / ACAA-T6a-S03` | MEC | MEC | PASS | PRE=单一作用仍不足 → SRC_NEW=肖文由群体异质偏好导出互补信息作用 / CAND_NEW=recipient/downstream criticality 与 remedy compatibility 使同一信息包对不同防守者价值不同 → REL=异质主体产生非同质作用，功能同位 → CIT=Cavusoglu 2007 selected-user warning、FIRST 与 Project Zero downstream gap 支持现实异质性 → NEXT=要求 recipient-specific adoption head → RESULT=保留 |
| V15 | `ACAA-T6b / ACAA-T6b-S03` | MEC→ALG | MEC→ALG | FAIL | PRE=异质作用已建立 → SRC_NEW=肖文由 affinity redundancy 导出 incompatible/complementary attention / CAND_NEW=候选需由理论导出 generic policy 必须反向更新的 remedy-specific operator → REL=同为从错误方向到专门运算的核心桥 → CIT=现有理论没有该 operator；patch-diff 是技术事实而非 IS 理论 → NEXT=触发 theory-algorithm NO-GO → RESULT=删除 |
| V16 | `ACAA-T9 / ACAA-T9-S02` | MAP | MAP | PASS | PRE=两次专用运算测试均失败 → SRC_NEW=肖文用 indicator–theory–challenge–solution 责任矩阵收束 / CAND_NEW=attack、readiness、quality、adoption、load、exposure 每行须有理论、标签、计算和干预 → REL=责任矩阵同位 → CIT=§2 与 §7 提供矩阵；尚无结果 → NEXT=检查是否只剩 feature typing → RESULT=保留 |
| V17 | `DSDL-I7 / DSDL-I7-S04` | MEC | MEC | PASS | PRE=需构造可观察代理 → SRC_NEW=肖文进一步指出个体异质状态不可直接观察 / CAND_NEW=maintainer capacity、downstream installability 和 attacker diff skill 对 CVE/remedy 成对异质 → REL=异质潜状态提出表示难题，功能同位 → CIT=Mitra busy-period、Gao adoption、VulnGym-APT profiles 只支持各自维度 → NEXT=设计 versioned graph 与 paired labels → RESULT=保留 |
| V18 | `DSDL-I8 / DSDL-I8-S05` | MAP | MAP | PASS | PRE=多主体异质性已出现 → SRC_NEW=肖文要求模型保留体验时变性 / CAND_NEW=五个 hazard/state heads 必须随 report、verification、ship、adoption 和 load 更新而非静态汇总 → REL=时变状态进入表示，功能同位 → CIT=理论与政策来源支持时间变化；具体 heads 是设计 → NEXT=规定 forward 与 labels → RESULT=保留 |
| V19 | `DSDL-I9 / DSDL-I9-S03` | LIM | LIM | PASS | PRE=需要监督中间状态 → SRC_NEW=肖文承认期望/体验无真值标签 / CAND_NEW=历史漏洞路径没有未采取 remedy/scope/timing 的 counterfactual labels → REL=中间监督缺失，功能同位 → CIT=OSV/GHSA/NVD/fix histories 字段对照；不是肖文引用迁移 → NEXT=引入安全 paired rollout 且说明识别边界 → RESULT=保留 |
| V20 | `DSDL-T2 / DSDL-T2-S05` | MEC | MEC | PASS | PRE=需要有方向关系而非状态罗列 → SRC_NEW=肖文规定体验超过期望与反向具有不同含义 / CAND_NEW=ship patch 同时提高 defender adoption 与 attacker diff signal，两个方向不可用绝对值或单一 risk 抵消 → REL=都是有方向冲突；内容不同但功能同位 → CIT=Arora 2008 与 Oracle’s Gambit 支持双向作用，PoCEvolve/Anthropic支持 diff channel → NEXT=分头预测并做 channel removal → RESULT=保留 |
| V21 | `ACAA-M0 / ACAA-M0-S02` | ALG | ALG | PASS | PRE=理论状态和动作已定义 → SRC_NEW=肖文按理论顺序列出方法兑现清单 / CAND_NEW=encoder→generator→world model→constrained SMDP→executor 是单一训练/推断链 → REL=理论合同进入方法总览，功能同位 → CIT=完整链是 steelman 设计，不归任何近邻 → NEXT=给出关键张量、checkpoint 与 loss → RESULT=保留 |
| V22 | `ACAA-M10a / ACAA-M10a-S02` | ACK+ALG | ACK+ALG | PASS | PRE=必须公平比较通用/专用 → SRC_NEW=肖文明确 common attention 与专用 key–key/query calculation 的差异 / CAND_NEW=本题须让 equal-param generic Transformer＋SMDP 获得同样 raw inputs、labels、actions 与 budget → REL=均先定义 common computation 再比较专用差异，功能同位 → CIT=公平对照是设计标准；尚无运行 → NEXT=若 generic 复制则撤题 → RESULT=保留 |
| V23 | `ACAA-M10b / ACAA-M10b-S05` | ALG | ALG | FAIL | PRE=通用差异已定义 → SRC_NEW=肖文从限制诊断落到实际计算修正 / CAND_NEW=理论若成立必须给出一个不能由 generic model 原样复现的 action update；当前没有 → REL=同为“诊断→修正”的动作句，功能同位但候选责任未兑现 → CIT=理论全文对照，不是性能结论 → NEXT=不再以多 heads 充当修正 → RESULT=删除 |
| V24 | `ACAA-M16 / ACAA-M16-S05` | ALG | ALG | PASS | PRE=模块已冻结 → SRC_NEW=肖文把专用机制放入端到端联合训练顺序 / CAND_NEW=7B QLoRA candidates、verifier features、coupled heads 与 policy checkpoint 必须按五阶段冻结 → REL=训练流程闭合，功能同位 → CIT=§5.6 设计；实验未运行 → NEXT=冻结 manifest 与 leakage mask → RESULT=保留 |
| V25 | `DSDL-M13 / DSDL-M13-S03` | ALG | ALG | PASS | PRE=typed graph 包含不同参与者 → SRC_NEW=肖文按说话者角色把序列分开 / CAND_NEW=maintainer、downstream、attacker 和 public 只能接收其 recipient/content tier 可见的信息 → REL=角色约束改变前向可见性，功能同位 → CIT=Vultron/FIRST/政策支持角色存在；visibility mask 是设计 → NEXT=验证不发生跨角色泄漏 → RESULT=保留 |
| V26 | `DSDL-M14 / DSDL-M14-S05` | ALG | ALG | PARTIAL | PRE=角色序列已分开 → SRC_NEW=肖文区分一般 attention 与跨角色匹配 / CAND_NEW=remedy-specific world model 必须比较 source patch bytes 对 defender tests 与 attacker diff harness 的两条路径 → REL=都是跨角色关系计算，但本候选仍可由 generic cross-attention 实现，位置参照非不可替代同位 → CIT=PoCEvolve、Anthropic N-day、PatchEval 支持两侧 evaluator → NEXT=做 equalize-bytes/anonymous-head 反证 → RESULT=改写 |
| V27 | `DSDL-M15 / DSDL-M15-S03` | MAP→ALG | MAP→ALG | PASS | PRE=需生成第一个中间状态 → SRC_NEW=肖文把偏好模板展开为动态期望矩阵 / CAND_NEW=world model 输出独立 attack survival distribution 而非 scalar risk → REL=理论构念生成可监督动态状态，功能同位 → CIT=Mitra 支持 attack diffusion语义；神经分布是作者设计 → NEXT=生成对应 defense/adoption state → RESULT=保留 |
| V28 | `DSDL-M16 / DSDL-M16-S02` | MAP→ALG | MAP→ALG | PASS | PRE=attack state 已分开 → SRC_NEW=肖文让第二状态与第一状态位于同一属性×时间坐标 / CAND_NEW=protection adoption 与 attack hazard 必须在同一 CVE/downstream/time grid 输出 → REL=同坐标使方向比较可验算，功能同位 → CIT=Mitra 只支持相反扩散；grid 是设计 → NEXT=定义二者耦合而非相减标量 → RESULT=保留 |
| V29 | `DSDL-M17_18 / DSDL-M17_18-S03` | MEC→ALG | MEC→ALG | FAIL | PRE=攻防两状态同坐标 → SRC_NEW=肖文按理论方向形成不可交换差值 / CAND_NEW=本题没有同等理论责任的不可交换 operator；仅有多个 action-conditioned distributions → REL=以 DSDL 最强标准做反证，候选无同功能锚点 → CIT=四篇理论未规定张量差/次序 → NEXT=判 MAP→专用 ALG 失败 → RESULT=删除 |
| V30 | `DSDL-M19 / DSDL-M19-S02` | LIM→ALG | LIM→ALG | PASS | PRE=历史无中间/反事实真值 → SRC_NEW=肖文以外部结果给弱监督方向并保留代理噪声 / CAND_NEW=common-seed Docker outcomes 可监督各 head，但只识别封闭模拟器内 action effect → REL=结果代理监督＋边界，功能同位 → CIT=§6 设计；未运行且不得外推真实组织 → NEXT=使用 held-out executable oracles/attacker models → RESULT=保留 |
| V31 | `DSDL-M21 / DSDL-M21-S03` | ALG | ALG | PASS | PRE=已有分开的时间序列 → SRC_NEW=肖文说明理论序列经时序压缩进入预测 / CAND_NEW=quantile critic 消费完整 factor trajectories，输出每个 outcome channel 的 return distribution → REL=中间序列进入最终预测，功能同位 → CIT=steelman 设计，未运行 → NEXT=与 scalar/generic critic 等预算比较 → RESULT=保留 |
| V32 | `DSDL-M22 / DSDL-M22-S02` | ALG | ALG | PARTIAL | PRE=有 factor outcomes 与通用 latent → SRC_NEW=肖文定义理论信号和黑箱预测的可学习融合 / CAND_NEW=policy 在约束下联合读取 factor heads 与 raw latent，但不得给前者额外未来信息 → REL=两条信号进入决策，功能同位 → CIT=设计定义；融合本身不是理论贡献 → NEXT=anonymous heads/equal-label baseline → RESULT=改写 |
| V33 | `DSDL-M23 / DSDL-M23-S02` | ALG+IMP | ALG+IMP | PASS | PRE=训练目标已定义 → SRC_NEW=肖文把联合优化连到预测与实践输出 / CAND_NEW=joint loss 必须产生真实 remedy execution 与 disclosure state change，而非只给 score → REL=训练输出进入外部行动，功能同位 → CIT=动作规格与 verifier contract；尚未执行 → NEXT=用外部结果评价 → RESULT=保留 |
| V34 | `DSDL-E11 / DSDL-E11-S02` | EVAL | EVAL | PASS | PRE=端到端表现不能证明理论 → SRC_NEW=肖文分别比较理论状态、深度表示与组合 / CAND_NEW=分别评价 factor-only、raw-generic、combined、anonymous-factor 和 oracle → REL=中间状态独立效用检验，功能同位 → CIT=预注册设计，未运行 → NEXT=解释任何组合增益来源 → RESULT=保留 |
| V35 | `DSDL-E12b / DSDL-E12b-S03` | RES+BND | BND | PASS | PRE=未来可能观察 factor 增益 → SRC_NEW=肖文主动防止把理论分支优势误解为深度分支可删 / CAND_NEW=即便 factor model 更好，也须排除额外 labels、参数、simulator construction 和 calibration 所致 → REL=防止过度解释同位；候选无 RES，故只保留 BND → CIT=未运行，不得写性能完成时 → NEXT=等参数/等标签/多 simulator 复核 → RESULT=保留 |
| V36 | `DSDL-E13 / DSDL-E13-S03` | EVAL | EVAL | PASS | PRE=需检验 factor/raw 协同 → SRC_NEW=肖文用两个极端损失作消融 / CAND_NEW=collapse diffusion、shuffle workload、remove pressure、remove diff channel、neutralize protected period 必须逐项运行 → REL=极端机制干预，功能同位 → CIT=§7.3 是实验设计；无结果 → NEXT=任何核心干预无预期变化则撤题 → RESULT=保留 |
| V37 | `ACAA-P5.5 / ACAA-P5.5-S02` | EVAL | EVAL | PASS | PRE=多个机制需独立责任 → SRC_NEW=肖文从母模型每次删除一个机制 / CAND_NEW=每个 factor/channel 单独删除且 action/data/budget不变 → REL=单项删除反事实同位 → CIT=ACAA 本地附录 I 缺失，故只模仿设计责任；本题也未运行 → NEXT=不声称消融证明 → RESULT=保留 |
| V38 | `DSDL-C1 / DSDL-C1-S03` | CONB | CONB | NO-GO | PRE=理论、方法、评价责任已列 → SRC_NEW=肖文把方法工具定位到特定文献流 / CAND_NEW=本候选最多贡献安全工程 benchmark/system，不能回收 ISR 独有理论算法 → REL=贡献必须回指已建立证据；功能同位 → CIT=§2–§7 综合终审，不归某一外部文献 → NEXT=决定题位 → RESULT=保留 |
| V39 | `ACAA-P7-1 / ACAA-P7-1-S03` | CONB | CONB | FAIL | PRE=贡献类型已判断 → SRC_NEW=肖文用一句压缩理论指标到算法机制 / CAND_NEW=候选若保留，必须一句说明哪个 IS mechanism 强制哪个不可替代 action computation；当前无法写出 → REL=理论→算法压缩验收，功能同位 → CIT=MEC→MAP→ALG 表显示缺口 → NEXT=不以模块列表替代该句 → RESULT=删除 |
| V40 | `ACAA-P7-2 / ACAA-P7-2-S02` | BND | BND | PASS | PRE=核心贡献回收失败 → SRC_NEW=肖文先承认单场景评价限制跨域泛化 / CAND_NEW=本题甚至尚未生成 paired worlds，所有效力、OOD 和真实 CVD 外推均未运行/未知 → REL=外部效度边界同位 → CIT=本项目没有日志；不是否决主因 → NEXT=不使用结果措辞 → RESULT=保留 |
| V41 | `DSDL-Z3_6 / DSDL-Z3_6-S11` | BND | BND | PASS | PRE=技术 benchmark 仍可能可做 → SRC_NEW=肖文把预测能力与真实使用者受益留作后续行为研究 / CAND_NEW=模拟 policy 优势不能证明真实维护者负担下降、下游更快采纳或真实 compromise 减少 → REL=离线/模拟能力与部署收益分开，功能同位 → CIT=未运行；Mitra/Arora 历史结果也不能替本 policy 背书 → NEXT=若另立系统 benchmark，明确不作真实组织因果声称 → RESULT=保留 |

### 9.1 审计结论

41 个键均来自 `00W` 的真实段落与句序。V07、V15、V23、V29、V39 是最关键的失败链：肖文原句的独特功能是从理论机制识别通用计算的错误方向并落到不可替代运算；本候选没有同功能命题。把这些行改成“我们设计五个 heads”只能形成位置相似，不能把 FAIL 改成 PASS。

## 10. 终局判定与唯一可复活条件

### 10.1 为什么是 NO-GO，而不是 CONDITIONAL

| 必要门 | 当前证据 | 状态 |
|---|---|---|
| 真实 broad-safety harm 与可执行行动 | 成立；修复 bytes、下游部署、泄露与维护负载可直接测量 | PASS |
| 不是普通 detection/patch/disclosure 分类 | steelman 动作足够丰富 | PASS |
| 直接近邻独立性 | 各组件和关键两两耦合已被正式理论、工件或政策覆盖；剩余是交集 | FAIL |
| IS MEC | opposite diffusion、patch pressure、quality/adoption/capacity 冲突成立 | PASS |
| 不可替代 MAP→ALG | generic equal-label temporal model 可复制；无稳定错误方向/不可交换运算 | FAIL |
| policy 识别 | 历史单路径失败；paired simulator 尚不存在且有循环识别风险 | FAIL |
| coding agent 不可删除 | 只有 remedy bytes 部分不可删；组织 policy 主体可保留 | FAIL |
| 与迁移/C3 独立 | 现象层可分 | PASS，但不能补救前三项 |
| 双用途可控 | 严格 sealed-public/synthetic 设计下条件可控 | CONDITIONAL |

依照用户给出的否决规则，理论链、识别和直接近邻独立性中任一失败即 NO-GO；本题三项同时失败。把它降格为“先跑 pilot 再看”会把理论/贡献失败误写成样本不确定性。

### 10.2 未来只有一个真正不同的复活路径

只有出现下列**全部**新证据才值得重新立项，而不是修改本判定：

1. 一个独立 IS mechanism 明确规定 remedy content 的某种关系，使 generic action-conditioned model 在可观测冲突状态下产生稳定、可预注册的错误 action ordering；
2. 由该机制导出的 operator 同时消费真实 remedy bytes、defender executable feedback 与 attacker diff-reconstruction feedback，删除其中任一条都会改变 action；
3. common-seed paired environments 已构造并用 held-out attacker/adoption models 验证，优势不来自 simulator 写入的同一规则；
4. equal-param/equal-label generic Transformer＋distributional SMDP、anonymous factor model 和强 patch/CVD policies 无法复制；
5. 删除 coding generator 或 equalize remedy bytes 后核心能力显著消失；
6. 所有危险 artifacts 都满足第8节隔离与非公开要求。

这不是“增加一个 patch exposure head”或“把 Vultron 接到 KeaRepair”。在这些条件出现前，正确行动是停止该候选作为 ISR 论文，而不是实施一个昂贵系统后再寻找理论解释。

## 11. 主要来源与证据状态

| 来源 | 状态 | 本终审使用责任 |
|---|---|---|
| Xiao et al., ACAA, ISR 2024，本地 `28706_*`；`00J/00M/00W` | 主文完整回读；附录/图像缺失边界沿用本地审计 | 写作功能、通用错误方向→专用 attention、方法/消融/贡献责任 |
| Chen et al., DSDL, ISR 2023，本地 `16409_*`；`00K/00W` | 主文完整回读；在线附录缺失 | 理论状态、方向运算、前向/损失、独立机制评价与部署边界 |
| [Mitra & Ransbotham 2015](https://doi.org/10.1287/isre.2014.0560) | 本地全文 | 攻击/保护相反扩散、busy period、明确局限 |
| [Arora et al. 2010](https://doi.org/10.1287/isre.1080.0226) | 本地全文 | actual disclosure→patch hazard；reduced-form 边界 |
| [Arora, Telang & Xu 2008](https://doi.org/10.1287/mnsc.1070.0771) | 作者 46 页全文 | protected period、speed/quality/adoption/workaround |
| [Ahmed et al. 2021](https://doi.org/10.1016/j.dss.2021.113586) | 本地全文 | disclosure mechanisms、firm response/risk；综述边界 |
| [Cavusoglu et al. 2007](https://doi.org/10.1109/TSE.2007.26) | 正式摘要＋作者 PDF 索引正文；直链 502 | policy families、多 vendor、early warning selected users；不猜公式 |
| [Cavusoglu et al. 2008](https://doi.org/10.1287/mnsc.1070.0794) | 正式全文页＋作者 PDF 索引 | release/update cycles、cost sharing/liability |
| [Gao et al. 2026](https://doi.org/10.1016/j.ress.2026.112586) | 出版方 preview/section snippets；PDF 付费未取得 | discovery/imperfect debugging/user diffusion＋patch timing；不扩张细节 |
| [Zhang et al. 2025](https://doi.org/10.1287/isre.2021.0349) | 正式页/作者页；全文端点超时 | BBP leak risk、patch complexity/security posture；不猜推导 |
| [PatchWeaver](https://www.usenix.org/system/files/usenixsecurity26-li-rui.pdf)、[KeaRepair](https://arxiv.org/html/2607.00820v1)、[PoCEvolve](https://arxiv.org/pdf/2607.22076)、[Oracle’s Gambit](https://arxiv.org/html/2607.05442v1)、[Faghani](https://arxiv.org/html/2606.11022v1)、[VulnGym-APT](https://arxiv.org/html/2607.24552v1)、[VulnGym-Repo](https://arxiv.org/html/2608.02001v1) | 全文逐项回读 | 直接技术邻居、输入—动作—结果与作者局限 |
| [Anthropic N-days](https://www.anthropic.com/research/n-days)、[Anthropic CVD](https://www.anthropic.com/coordinated-vulnerability-disclosure)、[Project Zero](https://projectzero.google/2025/07/reporting-transparency.html)、[OpenAI outbound CVD](https://openai.com/policies/outbound-coordinated-disclosure-policy/)、[Vultron](https://www.sei.cmu.edu/library/designing-vultron-a-protocol-for-multi-party-coordinated-vulnerability-disclosure-mpcvd/)、[FIRST](https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1) | 官方研究/政策/协议全文 | patch-as-signal oracle 与现实协调边界 |

## 12. 文件级结论

**最终建议：删除该候选的独立论文题位。** 若团队希望保留工程资产，可把 common-seed remedy-specific attacker/defender benchmark 作为独立安全系统项目，不使用 Mitra/Arora/Ahmed 给 generic RL architecture 贴理论标签，也不预先承诺 ISR 贡献。当前没有运行任何实验；NO-GO 来自理论—算法不可替代性、历史反事实不可识别和直接近邻交集，而非未运行本身。
