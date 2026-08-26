# 三项否决 Pilot 执行协议与本地资产台账

> **权威提示（2026-08-15）。** 本文件自该日起不再承担现行题位或写作授权，二者仅以 `00F_现行题位与设计稿授权.md` 及当前 `01/02/03` 正文为准。现行三题依次为 EUMN（实际返回 → 来源约束 OT/F → 残余一次补取或 ACT-NOW → post-reacquisition F → U/Y）、OIWG（**DEMOTE / DESIGN-ONLY / NO-RUN**）与 AVEP（world likelihood → Bayes → $g_e^{FB}$ → distributional CQL）。下文主体仅为旧候选的历史执行协议与资产台账；真实资源事实、已完成检查、NO-GO 和未执行状态继续有效，旧题位及“不得扩写设计稿”类禁令由 `00F` 覆盖。

## 一、状态快照与责任边界

本台账记录 2026 年 8 月 14 日工作区的真实资产与三项分级 pilot。它不把公开网址等同于本地可执行环境，也不把协议文字等同于已经生成的数据。`00D_三篇高杠杆替代题与立项门.md` 定义 MECHANISM-PROCEED、MODEL-PROCEED 与 CHAPTER-GO，本文件冻结这些门如何被实际执行。论文一、三的第一轮无训练 oracle pilot 最多只能产生 MECHANISM-PROCEED。论文二 warrant 是更前置的 DEMOTE/KILL screen：它因主张涉及生成而允许训练临时 checkpoint 并读取封存后的 hidden outcome，但全过也只恢复立项资格，不获得任何三级门。

当前结论如下。

| Pilot | 公开上游是否足够 | 本地 oracle 工具 | 本地数据与执行环境 | 当前状态 |
| --- | --- | --- | --- | --- |
| 论文一：行动充分配方族 | SWE-bench Verified、SWE-smith、Agentless 固定候选均可公开取得 | `pilot_tools/recipe_family_oracle.py` 已实现基本家族分析；运行前还需增加完整 `required-patcher × seed` 矩阵预检 | 没有候选池、patcher、Docker、harness 或容器 | **协议就绪，执行 NO-RUN** |
| 论文二：旧 refinement program；新 warrant 假说 | 旧 ARB/full-source reserve 已锁定但 formulation 停止；RACE-Bench Lite 与 SWE-Gym 可公开取得 | 旧 Stage-0/source verifier/synthetic diagnostic 只作否决记录；新假说没有 constructor、atomizer、intervention runner、generator 或 checkpoint | 没有 RACE-Bench、SWE-Gym、Docker、candidate pool、自然 agent patch 或训练环境 | **旧 formulation NO-GO；新假说 DEMOTE/仅保留80题机制KILL pilot/NO-RUN** |
| 论文三：handoff–repair 配置 | SWE-Gym、SWE-smith、SWE-bench harness 与开放 7B/32B Agent 可取得 | `pilot_tools/handoff_tier_oracle.py` 已实现 cheap/strong 四格基本配对分析；运行前还需冻结双 seed、abstain=0、ITT 分母和置信区间的分析层 | 没有 Docker/Linux、scout/fixer runner 或 32B 推理端 | **协议就绪，执行 NO-RUN** |

三项 oracle、既有 readiness/抽样/基线、Stage-0 executor 与开发汇总工具此前运行 66 项单元测试，full-source reserve sampler/verifier 又通过 7 项。refinement-proof diagnostic 另通过 compile、warnings-as-errors 与 19/19 synthetic tests。测试通过只证明脚本契约或保守子集内部一致，不证明 Python runtime identity、研究机制或外部价值；这些工具只是测量、资产核验与否决工件，不是可发表模型。

本台账后文出现的 MECHANISM-PROCEED 只授权构造训练集。MODEL-PROCEED 必须在新的仓库隔离数据上另行执行，CHAPTER-GO 又必须在未参与发现、标签生成与调参的公开任务上执行。未加限定的 `GO` 不在本台账中指代内部 oracle 通过。

## 二、本地资产审计

### 2.1 当前确实存在的资源

- 工作区位于 `E:\github\qual-llm-check-IS-utd`，可使用 `git`、`rg` 和桌面绑定的 Python 3.12 运行纯 CPU 脚本。
- GPU 为 NVIDIA GeForce RTX 3060，显存约 12GB。这只表示它具有小型图/集合模型或有限 7B 量化推理的潜在硬件容量；当前没有已验证的 CUDA、torch、训练或推理环境，也不能可靠承担 32B repair tier。
- 当前可见磁盘余量约为 C 盘 83.1GiB、D 盘 3.64TiB、E 盘 274.4GiB、F 盘 476.1GiB。SWE-bench 官方建议至少 120GB，因而 Docker/WSL 数据根不能留在默认 C 盘；micro-pilot 应放 D 盘并使用 env cache，而不是约 2TB 的 instance cache。
- v3.1 已有三项纯 Python oracle 工具及测试，不依赖 torch、transformers 或云端 LLM。
- ARB 代码仓已固定在 commit `07014c986f3deadb1548c62b32c0ffbe6a81465d`；三类正任务 release 与 selective/no-gold release 已下载、checksum 校验并通过官方 validate。`pilot_manifests/arb60_selection_v0.json` 保存 60 题 SHA256 盲抽，`pilot_manifests/arb20_abstention_selection_v0.json` 保存 10 个 natural no-gold 与 10 个 wrong-repository 盲抽；三种官方 ranker×三类正 release 的基线在 60 题上无 skip 完成。这些是数据与 baseline readiness，不是 typed-depth、obligation 或 refinement pilot 结果。
- `pilot_tools/arb_typed_program_pilot.py` 已在 60 个正任务上完成 Stage-0 开发运行，原始批次 SHA256 为 `ca45c9fb9fb0eeb7028a2e737615cd126b6ff22d731d92476ef429943d0994e2`；`pilot_reports/arb60_exact_identifier_lineage_development_v0.md` 保存全分母审计结果。它只验证 reduced anchor-symbol whole-token occurrence，不是语义关系或分级门结果。
- 排除 ARB60 已见任务与 snapshot 后，`pilot_manifests/arb16_semantic_fullsource_reserve_v0.json` 冻结 16 题、16 个未见 snapshot，SHA256 为 `99E86EB181249CF1F91C944ED0F178F3F4332CA314F03468765B2535ADEDF212`。逐 commit 取得的完整 Git blobs 已通过 source verifier：16/16 snapshot、5 个仓库、24,668 条 snapshot×path file rows、15,230/15,230 条 Python AST parsed，全部 query path 存在且可解析；去重后实读 13,421 个 blobs、209,590,988 bytes。机器 readiness report SHA256 为 `DE53103C2DB6D89D35C41BE00BB6D888BA73EFD3E317B7581761809EF2EAE337`，Markdown 审计报告 `pilot_reports/arb16_semantic_fullsource_readiness_v0.md` 的 SHA256 为 `E1C087A4611A4AD272484049046952E4105AF9F363E4394CF5E030C927C6938C`。这些数字只证明源码锁曾达到构建输入要求；当前治理状态为 `SOURCE_LOCK_VERIFIED_HISTORICAL_NO_AUTHORIZATION`，不授权 semantic index build。本运行是 0 gold/qrel、0 scoring、0 program evaluation、0 training。
- `pilot_tools/semantic_ast_index.py` 是已冻结的 **diagnostic-only** 工件，SHA256 `C281BB6A0EDC613DE64E50EE37F48CF81ABC9BF34E949FA90E5885C6D2FA19CF`；测试 `pilot_tools/test_semantic_ast_index.py` SHA256 `D907338C4A0074029C3B46C5D06344CE2699767EC8E6ED86AEBF8E6765FA4D49`，19/19 通过。它没有在 ARB16 或 Click 上执行，也没有产生可发布 index。

### 2.2 当前明确缺失的资源

- 工作区仍没有 RACE-Bench、SWE-bench、SWE-smith、SWE-Gym、ContextBench 或 CORE-Bench 的代码仓、数据、镜像或缓存；ARB 是例外。Stage-0 的 60 题 corpus 没有完整语义索引，released chunks 也不足以无损重建 Python blob。ARB16 完整 Git reserve 只清除了 source blocker；正式 semantic index 则因 formulation NO-GO 被主动叫停，并非等待补齐的普通工程缺口。未建立 SQLite、未发布 index，约 3.46 GB 被中止的临时产物已删除。
- 没有 Dockerfile、Compose、SWE harness、SWE-agent、mini-SWE-agent、OpenHands、Agentless 候选池、补丁轨迹、代码候选 atomizer 或上下文 serializer。
- 本机没有 Docker、Podman、nerdctl，也没有可用 WSL 发行版。SWE-smith 官方说明其开发和测试环境为 Ubuntu 22.04，并不支持 Windows 或 macOS，因此当前机器不能直接执行其容器任务。
- 当前项目依赖只有翻译、LangChain/OpenAI 与 dotenv。桌面 Python 中没有 `datasets`、`pyarrow`、`tree_sitter`、`torch`、`transformers`、`swebench` 或 `swesmith`；现有 `.venv` 也不是 benchmark 环境。
- 工作区中的 DeepSeek 配置服务于文献筛选，不是冻结的 Coding Agent、patcher 或 repair tier。公开 SWE 轨迹也不是本项目所需的反事实分支标签。

由此，ARB 数据与 ARB16 source readiness 仍可复核，但 refinement-proof formulation 已被上层治理否决，readiness 不再构成 build 许可。P2 新假说只有 DEMOTE/KILL-pilot 身份，且因缺少 RACE/SWE-Gym、Docker、generator 与本地 checkpoint 保持 NO-RUN；P1/P3 的 WSL/Docker、SWE 镜像以及远程 repair tier 仍是独立基础设施工作。

## 三、Pilot 1：行动充分上下文配方族

### 3.1 先用 Verified micro-pilot，而不是先训练模型

首轮使用公开 SWE-bench Verified 与 Agentless-Lite 冻结 retrieval release。Agentless 的预计算 top files 只承担部署时可见的候选生成，不使用 gold patch 或成功轨迹造候选池。每题从 base commit 上把 top files 按冻结 Tree-sitter 版本切为最多 10 个 canonical AST/span atoms，记录路径、起止行、语法类型、内容 SHA、token 成本、来源和名次。micro-pilot 只确认成员数 \(|S|\leq5\) 的 recipe；更大集合可作为搜索中间状态，但不进入本轮配方族与 1,400 次成本账。内容相同、只因切分边界不同的 atoms 先按内容 SHA 与 span-overlap 规则归并，低 Jaccard 不得由重复片段伪造。

在首次子集运行以前按仓库分层一次性盲抽并冻结 24 题、至少 4 个仓库，不看 gold patch、test patch 或历史子集结果；其中按 manifest 顺序预先标出的前 8 题构成 micro 子集，后 16 题只在扩展获准时启用，不能根据 micro 结果重抽。冻结主修复策略 \(p_0\)，并在启动前写入三个互不重叠的 seed 集：discovery seeds \(D\)、confirmation seeds \(C\) 和 held-out patcher \(p_1\) 的 transfer seeds \(T\)，每组三个。每题先用 \(p_0,D\) 执行 full-pool 与 empty-context。只有 full-pool 至少成功 2/3 且 empty-context 至多成功 1/3 的任务进入子集搜索。前一条件排除 patcher floor failure，后一条件排除不依赖外部上下文的任务。资格失败的题仍保留在对应 ITT 分母中，不得补抽到固定数量的“可搜索”任务。

### 3.2 搜索与确认

对每个合格任务仅用 \(p_0,D\) 采用三个预注册随机删除次序，跨 restart 以 `set_sha` 缓存，每题最多执行 75 个唯一子集。每次成功删除后继续 randomized ddmin/HDD，直到得到 one-minimal candidate；该结果不能称作全局最小或最小基数集合。discovery 运行不得重用 \(C\) 或 \(T\) 的补丁结果。

每题最多保留三个不同且 \(|S|\leq5\) 的候选 minimum。micro-screen 先对每个 \(S\) 及全部一步删除集合 \(S\setminus\{i\}\) 用 \(p_0,C\) 重新生成补丁并运行官方测试。数据入口先构造预期矩阵 `task × S-or-deletion × required_patcher × confirmation_seed`；只有每个矩阵单元都存在且无 infra failure 时才进入局部最小判定。在 micro-screen 的 `required_patchers={p_0}` 下，\(S\) 在 \(C\) 上成功至少 2/3 且每个一步删除集合成功至多 1/3，只能记为 `one_deletion_local_candidate`，不能进入正式 \(\mathcal M_{x,p_0}\)。只有扩展阶段为该候选的所有 proper subsets 补齐同一确认矩阵、并将每个 proper subset 判为不充分以后，才可记为 inclusion-minimal recipe。只出现一行、缺少某个 seed、required patcher 或 proper subset 的集合一律记为 incomplete，不得当作不充分证据。三个 confirmation seeds 只足以做 mechanism screen；进入 MODEL-PROCEED 数据生成前，必须为幸存配方增加预注册配对重复并用置信界重新确认。

家族冻结后才使用 \(p_1,T\) 对每个确认 \(S\) 运行可携性检验。这 72 次 transfer arms 不使用 deletion sets，也不把 \(p_1\) 成功与否回写到 \(\mathcal M_{x,p_0}\)。若后续声称 \(p_1\)-specific minimality，必须以新预算对 \(p_1\) 的全部一步删除集合完成独立矩阵，不得借用本轮 transfer 结果。

8 题中至少 2 题存在两个或以上 `one_deletion_local_candidate`，且至少一对经重复片段归并后的 Jaccard 不高于 0.60，只表示可以启用 manifest 中预先冻结的后 16 题；少于 2/8 时判为 **INCONCLUSIVE**，不是 KILL。24-task MECHANISM-PROCEED 只统计已补齐全部 proper-subset 矩阵的 inclusion-minimal recipes，同时报告 ITT 可达率、约 25% 的低重叠家族发生率、任务级区间和 first-restart one-MSC 监督造成的替代证据假负例率。后验从家族中挑成功成员形成的 `family_oracle_ceiling` 只用于估计相对预先冻结 first-restart one-MSC 政策的可学习上界，不能称部署收益；该上界约 5 个百分点以上才授权生成 family-level 训练标签。MODEL-PROCEED 另行要求仅凭部署可见特征的学习策略回收至少一半这一 regret gap。若策略顺序尝试多个 recipe，次序须在结果前冻结，而且每次生成、测试、token 和墙钟全部收费。

### 3.3 运行账与缓存陷阱

- `p_0,D` 的 full/empty 资格运行最多 48 次。
- discovery screen 最多 `8×75=600` 次生成与测试。
- `p_0,C` 的 micro confirmation 因明确限制 \(|S|\leq5\)，一步删除局部筛查上限为 `8×3×(1+5)×3=432` 次；它不含 inclusion-minimal 所需的其余 proper subsets。24 题扩展和 proper-subset 补齐必须在 micro 结果以前另行冻结独立成本帽，不得挤入本节 1,400 次预算。
- `p_1,T` 只对每题最多三个冻结 \(S\) 执行 transfer，上限 `8×3×3=72` 次。它不承担 \(p_1\) 最小性证明。
- 预计算主体上限为 `48+600+432+72=1,152` 次。最多 20% 基础设施重试后为 1,382.4，向上冻结为 **1,400 个 generation-plus-test episodes**。任何额外 patcher-deletion 矩阵使用新预算，不得挤入这一硬帽。
- 若每次测试 4 至 15 分钟并发 4 至 6 workers，按 1,400 次硬帽计算的纯运行墙钟约 16 至 88 小时，不含首次镜像下载或构建。
- micro-pilot 预留约 200GB，放 D 盘。当前 C 盘不足，E 盘只能勉强承担 env cache。
- 启动前还必须在 manifest 冻结每次 patcher 的最大输入/输出 token、调用价格与总货币硬帽。episode 上限不能替代 token 和货币成本账；任一上限未冻结时保持 NO-RUN。

SWE-bench harness 会按 `run_id + instance_id` 缓存。每个 subset、patcher、seed 和实际 patch 必须使用唯一 `eval_run_id=SHA256(task,set,patcher_revision,seed,prompt,patch)`，否则不同上下文生成的补丁可能错误复用第一次评测结果。

事实表 `oracle_runs` 每行对应一个 task×context-set×patcher-seed，至少包含：benchmark revision、repo、base commit、image digest、issue/pool/set hash、member IDs、token 成本、`discovery|confirmation|transfer`、restart、seed-set revision、patcher 与 prompt revision、patch hash、apply 状态、FAIL_TO_PASS/PASS_TO_PASS、resolved、infra 状态、wall/token/货币成本、eval run ID 与日志路径。`expected_matrix` 独立保存每个候选应存在的 required-patcher×seed×deletion 单元并在分析前做 anti-join；candidate manifest 独立保存 atom 定义，不在每一事实行复制源码。

## 四、Pilot 2 复盘：已否决的语义细化类型检索程序

本节的 schema、primitive 与原门槛只保留为否决审计记录，不再授权执行。P2 refinement-proof formulation 已判 NO-GO；新的 warrant 假说使用下节完全独立的 benchmark、标签与门。

### 4.1 数据抽样与可见性

[Agent Retrieval Bench](https://agent-retrieval-bench.github.io/) 当前公开 427 项、25 个仓库，其中 code2test 106、trace2code 101、edit2ripple 58，足够各抽 20 项。ARB repo 已 pin 在 `07014c986f3deadb1548c62b32c0ffbe6a81465d`，三类正任务与 selective/no-gold release ID、下载 checksum、corpus manifest 均已冻结并通过官方 validate。`pilot_manifests/arb60_selection_v0.json` 已按 `SHA256("rtp-oracle-v0|"+task_type+"|"+instance_id)` 完成每类 20 项的盲抽，每个 repo×task type 最多 4 项并优先不同 `(repo,base_commit)`；`pilot_manifests/arb20_abstention_selection_v0.json` 又在任何 typed-program 结果产生前冻结 10 个 natural no-gold 与 10 个 wrong-repository 样本。两份清单均不得在看到后续结果后重抽。

主体包含 60 个有 gold 的正任务；另冻结 20 个 selective 任务作为**条件性** `ABSTAIN` 扩展，其中 10 个来自公开 natural no-gold 轨、10 个是 wrong-repository 对照。该 release 的部署 query 只有 `source` 与自由文本 `text`，不能无损恢复三类正任务的结构化 grammar；当前逐题 top-20 又只有 BM25，lexical 与 RepoMap 仍缺。因此这 20 题在独立的 query-only generic-issue grammar、三方法同条件 details 与 label sidecar 冻结前保持 `NO-RUN`，不得被强行套入正任务 executor。运行时必须隐藏 `query.source=counterfactual_wrong_repo`、sample-ID 前缀、manifest stratum 与 metadata；这些字段只进入事后标签 sidecar，否则等同把 no-gold 标签送入 selector。正任务的 gold 仅在所有候选程序执行完后用于评分。code2test 与 trace2code 可做 block/span 诊断，edit2ripple 只承担文件级结果。ARB 只验证上游检索，不直接支持补丁通过结论；只有后续 `MODEL-PROCEED` 才允许进入 ContextBench 或 SWE-bench 可执行任务。

截至当前，三种官方 ranker×三类正 release 的基线已在冻结 60 题上无 skip 完成。官方 summary 的 `gold_coverage@8k` 使用 legacy 8K **character** packing，只能保留为官方复现实验字段，不能冒充本协议的 canonical token-budget BCY。后者必须直接复用或严格等价实现官方 `regex_code_tokenizer_v1`、canonical path-header renderer 与 scorer revision，在 **8,000-token** budget 下从原始 ranked output 另算，并逐题保存 exact token count；在该 scorer 完成以前，任何现有 summary 数字都不能代入 C/D 门槛。当前 top-20 并集相对逐题最佳单一官方方法仅在 2/60 题严格改善，因此旧 FIT-USE/服务集合组合路线记为 **NO-GO**；这项诊断没有运行 typed program、query-only obligation、深度消融或 refinement search，不能据此推进或否决当前论文二。

随后完成的 Stage-0 开发批次不是本节规定的完整 typed pilot。它当时冻结的 selector 输出在 60 题上的 canonical BCY 为 0.3583，后验 oracle ceiling 为 0.3750，RepoMap 为 0.3806；PROGRAM/ABSTAIN 为 54/6。其 reduced catalog 曾读取 release failure label、path stem 与 ARB `symbol`；凡由 reference PR/result 派生者在现行 query 白名单下都须剔除，故该运行不能作为新 constructor 的 query-only 证据。54 题实际返回三榜并集外文件，但只有 6 题的榜外文件命中 gold，727 个榜外文件中只有 7 个 gold，微观精度约 0.96%。该运行扫描 59 个可编译任务约 4.43 GB、518 万 JSONL 行；19/60 题 relation postings 截断，20/60 题 selected-path completeness 未闭合。它只证明实现能逃离官方列表，不证明榜外信息有系统价值；whole-token 代理作为论文算法记 NO-GO，且不得在该开发集上报告显著性或泛化。

为避免把截断 release chunks 冒充完整源码，另在未读取 gold 的条件下冻结 ARB16 full-source reserve，并逐 commit 核验本地 bare Git blobs。reserve manifest SHA256 为 `99E86EB181249CF1F91C944ED0F178F3F4332CA314F03468765B2535ADEDF212`；readiness JSON SHA256 为 `DE53103C2DB6D89D35C41BE00BB6D888BA73EFD3E317B7581761809EF2EAE337`，对应 Markdown 报告 SHA256 为 `E1C087A4611A4AD272484049046952E4105AF9F363E4394CF5E030C927C6938C`。16/16 snapshot 的完整 trees 可读，覆盖 5 个仓库、24,668 条 file rows；15,230/15,230 条 Python file rows 通过 AST，全部 query path 存在且可解析，去重实读 blob 为 209,590,988 bytes。机器当时输出的 `READY_FOR_SEMANTIC_INDEX_BUILD` 现仅作为 legacy 资产记录保留；当前状态是 **`SOURCE_LOCK_VERIFIED_HISTORICAL_NO_AUTHORIZATION`**，明确不允许构建或校验正式 semantic index。当前仍是 **0 gold/qrel、0 scoring、0 program evaluation、0 training**，不得写成机制证据。

readiness 后只在三组 synthetic fixtures 上运行 proof-feasibility diagnostic，没有读取 ARB16/Click 或 gold。冻结代码 SHA256 为 `C281BB6A0EDC613DE64E50EE37F48CF81ABC9BF34E949FA90E5885C6D2FA19CF`，测试 SHA256 为 `D907338C4A0074029C3B46C5D06344CE2699767EC8E6ED86AEBF8E6765FA4D49`；compile、warnings-as-errors 与 19/19 tests 通过。白名单 property 共覆盖 19 entities、19 scopes、18 edges、19 resolution sites、21 witnesses 和 8 条 CERTIFIED edges；foreign-key、候选保留、snapshot partition、witness ordinal 与重复构建确定性守恒。该结果表示 diagnostic 子集无剩余 P0，不提高 runtime-refinement 或 source-readiness 等级。

审计限定的 symbol certificate core 极窄：CERTIFIED CALL/REF 只允许同 module、稳定顶层 function/async-function、simple Name 与 `lexical_unique_binding`；CERTIFIED IMPORT 只允许 module→module 的 `SOURCE_SYNTAX_MODULE_IMPORT`；AS_TEST 仅在稳定 role 上认证，fixture relation 无 CERTIFIED edge。`globals()`/`vars()`、`exec`、runtime rebinding 与 monkeypatch 说明跨模块 symbol identity 若要 proof-grade，必须接近完整 Python 动态语义分析；保守 fail-closed 时这些候选全为 DYNAMIC，原定跨文件 relational-depth 机制没有可执行支点。

把目标放宽为 assumption-bound static lineage 也不能挽救理论贡献，因为相同约束可由共享 entity IDs/witness/status 的 generic provenance/equality guard 直接复制。因此本 formulation 判 **NO-GO**。正式 build 已停止，约 3.46 GB 临时产物已删除；不建 SQLite、不发布 index、不跑 Click/ARB16、不读 gold、不 scoring、不训练。readiness 事实仍保留，但其原 build authorization 已被本治理决定覆盖。

### 4.2 已停用的 query-only obligation constructor

在查看任何 gold、qrel 或 no-gold 标签以前，按 task type 冻结 constructor revision、prompt/规则、字段白名单、schema 和失败值。白名单只含部署时确实可见的 task type、repo/base commit、query 原文、原文内明示的 trace/test frame，以及原文明示的仓库相对路径、span 或名称；reference PR/patch/diff、changed-file/result 列表、gold/qrel/evidence、由 reference change 或评价结果派生的 symbol/label，以及未逐字出现在 query 中的事后测试结果一律禁用。code2test、trace2code 与 edit2ripple 只能从该白名单分别产生“测试/被测实体”“定义/调用者”和“依赖/涟漪位置”义务。query 明示的文件可作已给 anchor，却不算新取得 evidence，也不能单独满足 relational-depth necessity。constructor 可以确定性输出 `UNRESOLVED`，但不得因为事后知道没有 gold 而输出 `ABSTAIN`；`ABSTAIN` 只能由冻结义务未满足、所有候选无证据或预算耗尽的预注册规则触发，并同时报告 60 个正任务的 false-abstain 与 20 个 selective 任务的 false-evidence。

### 4.3 已停用的 retrieval primitive 与 proof predicates

所有 primitive 只读取 query-only obligation 与 base-commit corpus，严禁把 gold evidence signal 送入执行器。

1. `QUERY_NAMES(Task<t>) → Set[QueryName<t,name,witness>]`，只解析冻结白名单字段。
2. `TRACE_FRAMES(Task<t>) → Set[Frame<t,path,line?,name?,witness>]`，只解析 query 明示的 trace/test frame。
3. `GIVEN_ANCHORS(Task<t>) → Set[Anchor<t,path,line?,name?,witness>]`，只读取 query 明示的 path/span/name。
4. `DEFS_AT(FileAnchor|Frame[,QueryName]) → Set[Def<t,s,repo,commit,path,qualname,span,blob_oid>]`，枚举坐标或词法范围内的全部 AST matches；不得以 task relevance 直接返回“相关定义”。
5. `RESOLVE_UNIQUE(Mention|Frame|Ref|Call|Import) → Entity|AMBIGUOUS|DYNAMIC|UNRESOLVED`，只按冻结的 lexical/import scope 唯一解析，严禁用 downstream closure、输出质量或 gold 消歧。
6. `CALLEES_OF(Def<caller=c>) → Set[Call<caller=c,callee=s,witness,status>]`。
7. `CALLERS_OF(Def<callee=s>) → Set[Call<caller=c,callee=s,witness,status>]`。
8. `IMPORTS_OF(File<src=f>) → Set[Import<src=f,dst=g,witness,status>]`。
9. `IMPORTERS_OF(File<dst=f>) → Set[Import<src=g,dst=f,witness,status>]`。
10. `REFS_TO(Entity<target=s>) → Set[Ref<source=c,target=s,witness,status>]`。

`AS_TEST(Def<s>) → Test<s>|NOT_TEST` 只按同一实体的 path/name/decorator/unittest 证据做 unary cast；`USES_FIXTURE(Test<t>,Fixture<f>) → FixtureUse<t,f,witness>|false` 只验证一条 direct fixture edge。二者是 depth-0 proof predicates，不得搜索“某实体对应哪些测试”。禁止 `TESTS_FOR(Entity)`、双向 `IMPORTS_OR_IMPORTERS_OF`、方向含混的 `REFS_OF`、primitive 内 transitive closure，以及把 `Task` 直接送入语义 operator 后返回 relevant defs/tests；如需 inverse fixture retrieval，必须另立方向明确的 operator。

entity ID 固定为 `(repo,commit,blob_oid,path,qualname,lineno,end_lineno,kind)`；每条图边保存 `{repo,commit,src_entity_id,dst_entity_id,witness_path,witness_span,resolution_rule,status}`，其中 status 取 `CERTIFIED|AMBIGUOUS|DYNAMIC`。refined proof 只能消费 `CERTIFIED` edge，但 refined、coarse、PyRAG-style 与各强基线必须看到同一批 raw candidates、witness 和 status；不得在 index build 时替 refined 预删 ambiguous/dynamic，或对基线隐藏状态。

### 4.4 已停用的搜索、基线与门槛

原 formulation 的程序以 QUERY_NAMES、TRACE_FRAMES 或 GIVEN_ANCHORS 为根，`relational_depth` 最多为 3，且只计 primitive 6–10 实际跨 entity/file 的 direct edge；primitive 1–5、AS_TEST、USES_FIXTURE、filter 和 render 均为 depth 0。其余 scheduler、raw fan-out、cache 与 given-evidence 规则保留为复盘基准，但不再授权实现或运行。

原协议要求 gold 前封存全部 candidate/selector/output/cost bundle，并只以 `frozen_query_only_selected_*` 进入 C/D；posthoc oracle 只能作上界。这些反泄漏规则仍是未来任何新 P2 的最低纪律，但没有 bundle 被生成，本 formulation 也不得借此恢复。

原计划的强基线包括 depth-1、equal-cost hybrid、PyRAG-style 显式变量/dataflow，以及取得相同 entity IDs、witness/status 的 generic provenance/equality guard。feasibility audit 已表明：放宽后的 static lineage 直接落入最后一项，故无需用 gold 实验再把同一工件包装成 refinement 贡献。

原比较曾分为三层，现仅作为未执行的预注册记录。

1. 全枚举 sanity。只有当同一 objective、operator semantics、raw fan-out 和 output rule 下，typed 与 coarse 两侧都写出 `frontier_exhausted=true`，且没有 `max_programs`、超时、内存、posting 或 edge truncation 时，才可称 full enumeration。此时 refined space 是 coarse space 的子集，coarse posthoc oracle ceiling 必须不低于 refined oracle；否则只能标作 bounded search，不能主张 coverage ceiling。
2. 固定搜索预算。所有系统使用同一 cost-prioritized best-first scheduler、同一 priority tuple 与 512 个 attempted partial-program expansions、128 个唯一 primitive invocations、4,096 个 posting/图边读取、raw fan-out 20、top-20 和官方 **8,000-token** canonical 装入预算。successor 一经提出就消耗 expansion，即使随后被拒；type checking、lineage、index build/lookup、cache hit/miss、CPU、峰值内存、I/O 与墙钟都进入同一 cost ledger。`invalid_execution` 由系统外、gold-blind 且事先冻结的 shared checker 判定：仅包括 runtime/schema precondition 失败，或 grounded transition 声称的 direct relation/identity binding 无法由共享 witness 证实；合法但 zero-result 的调用不算 invalid，系统自己的 reject 数也不能循环自证。比较 `frozen_query_only_selected_*` 的 BCY/Recall、该外部 invalid 指标和总资源。
3. 深度必要性与 same-skeleton stress test。gold 前，每题按 query-only priority 冻结最多 3 条 identity-consistent、nonempty、relational-depth 2–3 的 valid controls。每个被消费实体 `e` 的 decoy `e′` 必须来自同 repo/commit 的 query-visible pool，保持 nominal kind/type，并以 SHA tie-break 在 producer/consumer 均可执行、degree/output-cardinality/path-role 同 bucket、实际成本 ±10%、下游 nonempty 的候选中选取；不可构造就进入 constructibility 分母并报告原因，不得看 gold 后换 decoy。`WE1` 由平行 branch 正常产生 `e′` 后只改接 downstream consumer；`WE2` 把后续 subchain 一致替换为 `e′`、保持内部 dataflow 自洽但 mandatory obligation target 仍为 `e`；`rewire` 交换两个平行 branch 的 downstream consumers，同时保持 operator multiset、DAG 节点数、depth、fan-out 和 output cap。alpha-renaming、平行分支换序及同实体 alias-normalization 作为应通过且输出不变的 benign controls。JSONL 锁定 task/program/control/decoy hashes、substitution site、skeleton、bindings、eligibility、raw outputs 与真实成本；拒绝率分母是全部 query-only eligible matched pairs，另报相对所有 valid controls 的 constructibility，gold 后才报告 BCY harm、output Jaccard 与是否挤掉非 query 明示 gold。

原 `ORACLE-BUILD-PROCEED_16`、MECHANISM、MODEL、CHAPTER、K1/K2 与 NO-SCALE 条件全部在运行前退役：没有构建正式 index，没有形成 query-only bundle，没有读取 gold，也没有 ARB16 指标。故当前结论不是“16 题未过效果门”，而是更前置的 **formulation-level NO-GO**。diagnostic 代码只可保存、静态检查和运行 synthetic unit tests；不得调用其 corpus `build` 路径，不得据 readiness 继续工程化。下节是新的 DEMOTE/KILL 协议，不复用本节任何门、标签或 build 许可。

## 五、Pilot 2 新假说：claim–hunk–test observed-interventional warrant closure

本节只定义一次 80 题机制 KILL pilot，不把新假说恢复为 conditional candidate。当前没有本地资产，故全节为 **NO-RUN**。

### 5.1 RACE-Bench Lite 20+80、SWE-Gym 与可见性

[RACE-Bench](https://arxiv.org/abs/2603.26337) Lite 是官方 difficulty-aware 的 100 题 feature-addition 子集。下载并锁定 benchmark/container revision 后、读取任何 Reference Reasoning、Gold Patch、PTP 或 official result 前，按 `SHA256("p2-warrant-v1|"+benchmark_revision+"|"+instance_id)` 升序固定前 20 题为 debug、后 80 题为冻结 ITT 主批次，保存全部 digest、顺序、repo、base commit 与 image digest。20 题只调试 gold-free constructor、schema、hunk atomizer、容器与账本；预测封存后才可用 Reference Reasoning 检查 claim recall/overprediction，不能把 20 题加入效应量、训练 edge model 或事后换入 80。`schema-slot` 只是该低成本 offline screen，不构成第二题。

RACE 正式 agent input 只开放 Feature Request、base repository/environment 和全部 visible FTP tests。部署 claim 白名单进一步固定为 issue/Feature Request、base snapshot、FTP 源码与修复前失败输出及其确定性静态派生；Gold/Reference Patch、Reference Reasoning、Test Patch 中未公开部分、changed-file/hunk 标签、hidden PTP、official evaluator 输出及其派生字段全部隔离到 seal 以后。封存顺序固定为：先封存全部主方法/基线 claim、candidate pool、decoder trace 与选择；再只用 visible-FTP intervention matrix 标记 `W`；随后按下文预注册规则生成并封存 targeted edge-neutralization 归因臂；最后封存全部 patch hash 与成本，才运行 hidden PTP/official evaluator。visible FTP pass 不能代替官方 resolved，neutralization 结果也不得反馈重训或改变主输出。

[SWE-Gym](https://proceedings.mlr.press/v267/pan25g.html) 不承担 RACE 的 claim gold 或最终外测。它只在与 RACE 外测仓库隔离且去污染的 split 上生成自然 agent trajectories、候选/干预三分类监督，并本地训练、保存一个能相对初始化或无结构目标取得预注册验证改善的非平凡 checkpoint。必须保存 training data IDs、repo split、base weights、optimizer、seed、step、checkpoint hash 与 validation curve。没有仓库隔离 split、没有真正保存的本地 checkpoint，或只下载作者权重，均不得进入 80 题。

### 5.2 自然标签、partial-patch 边界与不可识别值

每题只从预冻结普通 beam 的自然 agent patches 形成标签池；Gold Patch 删 hunk、手工 bypass、synthetic refute 或看到 official result 后挑 patch 均禁用。自然成功候选可以提供 support，但计入负边门的 refute/antagonistic 必须来自自然失败候选。claim schema 固定为 `claim_id/trigger/subject/expected_observable/polarity/scope/source_span/ftp_observability/unresolved_reason`。边标签为互斥 `SUPPORT|REFUTE|MISSING`：相同 partial-patch coalition 的加入使 claim-aligned FTP 在独立执行中稳定 fail→pass 才是 support，使其稳定 pass→fail 才是 refute/antagonistic；无稳定效应、无测试观察、执行不一致或无法识别都为 missing。`MISSING` 不得当负例或用于补足负边门。另存 `INDIVIDUAL_WITNESS|JOINT_ONLY|SUBSTITUTABLE|NON_IDENTIFIABLE|INFRA`。

hunk rollback 只说明冻结 patch/test/environment 下的条件观察效应，不是 claim 级语义因果证明。single-hunk removal 也不能排除联合必要与替代实现。[IBugFinder](https://doi.org/10.1145/3660828) 已枚举 partial-patch powerset 并研究八类 multi-hunk 关系，[TRIM](https://arxiv.org/abs/2607.18161) 已做 trajectory-guided patch minimization 并比较 DD-Hunk；因此 rollback、powerset、ddmin、one-minimality 和 joint-hunk discovery 全部只作标签生产/强基线。主张只能来自自然稳定的 signed triangle 使训练与约束解码产生普通 completed-patch pools 外的新正确 patch。

### 5.3 80 题候选、干预与物理运行账

主批次启动前一次性冻结 `K=4`、所有 decoder/atomizer/test/evaluator revision、相同最大输入输出 token、forward-pass、candidate、FTP execution 与墙钟预算。普通 beam 每题产生 4 个 completed patches；只取其按 beam rank 最前的两个自然候选进入 intervention label pool，不按 FTP、hunk 数或后验结果换位。每个候选以 `git diff --unified=0` 形成 hunk，再按预注册的重叠/编译依赖规则合并；合并后 (H\le4) 时执行包含 full patch 在内的全部非空 subsets，base/empty 结果按任务缓存。(H>4) 不截成有利的四块，直接记 `NON_IDENTIFIABLE` 并保留在 80 分母。

- 自然 intervention pool 最多 `80×2=160` 个 patches；每 patch 最多 (2^4-1=15) 个非空 variants，即最多 2,400 个 unique partial-patch variants。
- 每个 variant 在全新容器执行 visible FTP 两次，最多 4,800 次；结果冲突的预注册 10% adjudication 容量再留 240 次。base/empty 每题两次另 160 次。因此自然边标签容量上限为 **5,200 次 visible-FTP executions**。
- 十个等预算主生成臂固定为 ordinary beam、diverse beam、test-augmented beam、MultiMend-style、MultiFixer-style、generic minimum-claim coverage、同参数 generic graph、signed-warrant decoder、within-task rewire、sign-shuffle；另设一个**只用于归因、不得计部署效果**的 targeted edge-neutralization 臂。主臂每题完成 4 个 patch；neutralization 臂对 signed-warrant 的每个封存 candidate，先在其封存 decoder trace 中筛出经 visible matrix 判为 `W` 的分量，再按冻结 signed contribution 降序与 component hash 破平选择一个，将该分量相关 signed edges 置为中性，并以同 seed、同 search budget 重新解码；无合格分量则记 `NOT_APPLICABLE`，不能在看到 official outcome 后补跑。十一臂最多形成 `80×11×4=3,520` 个 completed-patch hashes。若能忠实运行原 MultiMend/MultiFixer 则替换对应 `-style` 主臂并冻结版本，不能在结果后择优。另设 generic single-hunk ablation、IBugFinder-style exhaustive-subset/indivisibility 与 DD-Hunk/TRIM-style minimization 三个独立 postprocessor 臂，各最多再产 1 个 patch/题，共 240 个 hashes；不得把三者合成一个弱化基线。所有 apply failure 也留在 pool manifest。
- 每个生成/后处理臂冻结一个 gold-free final selection；另有一个只在训练/验证 split 预选并冻结的最强 posthoc verifier，从其合法 baseline pool 冻结一个选择，不能看 RACE 80 再决定使用哪个 verifier。最多 `80×15=1,200` 个 official patch evaluations。加上 visible-FTP intervention，得到 **6,400 个确定性标签/封存后评价 jobs**。该数字不是完整主批次上限：十五个方法×任务单元在生成或选择期间自行触发的资源必须分别冻结向量上限 `\mathbf b_{m,i}=(n_{FTP},n_{compile},n_{tool},n_{forward},tokens,wall,compute,money)` 并逐次收费，再按维度聚合为 `\mathbf B_{gen,total}=\sum_{m=1}^{15}\sum_{i=1}^{80}\mathbf b_{m,i}`；统一向量上限为 `\mathbf b` 时即逐维不超过 `1,200\mathbf b`。缓存可以降低物理执行，却不能把逻辑调用从公平性账中抹去。完整物理上限必须作为 `{6,400 个确定性 jobs, \mathbf B_{gen,total}, 20题debug, SWE-Gym数据生成与训练, 镜像/infra}` 的多维账冻结，不能把异质量尺硬相加；任一维未实测冻结均保持 NO-RUN。
- 每个 job ID 为 `pilot_revision/instance/method/patch_hash/coalition/repeat`。逐事件保存 image/base/fs/config hash、claim/edge/model/decoder hash、FTP/PTP 可见性、exit/timeout/infra、输入/缓存/输出 token、forward passes、test invocations、CPU/GPU/内存/I/O/墙钟与货币成本。启动前必须以实测容器中位数和 P95 冻结总 GPU-hour、container-hour、磁盘与货币硬帽；任一未冻结继续 NO-RUN。

上述是容量账，不是完成事实。未执行单元以 `NOT_APPLICABLE|NON_IDENTIFIABLE|INFRA` 留在 expected-cell manifest，不补抽、不缩分母，也不把未跑当 refute。

### 5.4 强基线与一次性 DEMOTE/KILL 门

所有主方法与基线必须共享同一 gold-free claim constructor、raw candidates、visible FTP 与总预算。训练方法可共享训练 split 的 intervention supervision；RACE 80 的 observed intervention matrix 只在主输出封存后供标签审计与 posthoc 机制评价，任何部署候选 generator、decoder、selector 或 verifier 在推断时都不得读取它，只能使用冻结模型预测的边。唯一例外是明确标为非部署归因工具的 targeted edge-neutralization 臂：它只能按 5.1 的封存顺序选择已在主 decoder trace 中出现、且由 visible matrix 判为 `W` 的分量，输出不得回流主方法，也不得计入性能优势。强基线至少包括 test augmentation、ordinary/diverse equal-compute beam、MultiMend/MultiFixer 式 multi-hunk generator、SWE-Gym/static 与语义 patch verifier、generic minimum-claim coverage、同参数无理论图模型、generic hunk ablation、IBugFinder-style exhaustive subsets、DD-Hunk/TRIM-style minimization；无法忠实运行原方法时标为 `-style` 并列差异。posthoc verifier 不得读取 hidden PTP 或 official result 来训练或选 patch。

定义 task-level `W`：一题只有在**同一个 claim/test 分量**中同时存在两个以上共同必要 hunk 与自然 `SUPPORT+REFUTE/ANTAGONISTIC`，才进入 `W`；同题不同 claim、test 或无共享机制分量的 candidate family 不得拼接。80 题必须一次性同时满足：同一 claim/test 下两个以上共同必要 hunk 的任务 `≥25/80`，多个独立 claim 的单 hunk 覆盖不计；稳定 support 与 refute/antagonistic 同时出现于 `≥20/80` 且 `≥4 repos`；`W≥16/80` 且 `≥4 repos`；按仓库 held-out 的 `SUPPORT|REFUTE|MISSING` macro-F1 `≥0.75`；hidden official resolved 相对 generic coverage 和同参数 graph 各 `≥5/80` 且至少 4 repo 同向，其中至少 3 个净新增解决在对应 neutralization 后必须失去 official resolved；signed decoder 至少 8 个 official-correct 新解不在任何 baseline completed-patch pool，其中至少 5 个的具体 hash 或对应选择必须被同分量 neutralization 消除；rewire 与 sign-shuffle 在 `W` 内各消掉至少一半相对强 generic baseline 的增益；最强 posthoc verifier 仍不能追到只差 2 题以内。即使全过也只允许重新立项，不自动获得 MECHANISM-PROCEED、MODEL-PROCEED 或 CHAPTER-GO。

该 80 题筛查只有在至少 64/80 题完成预注册 candidate 与 intervention matrix、且覆盖至少 4 个仓库时才具有否决资格，否则记 `INCONCLUSIVE` 并维持 DEMOTE。升格时未完成单元保留在 80 的 ITT 分母且不算成功；KILL 时每个 `NON_IDENTIFIABLE/INFRA` 单元都先按潜在 `W`、潜在自然负边和最大理论方法优势补全。只有据此计算的 `W` 单侧 95% Clopper–Pearson 上界仍低于预注册 20% 最小相关率才可因低发生率 KILL；稳定自然负边为零只有全部 80 题完成负边识别时才能单独 KILL。generic coverage/graph 的等价性 KILL 也必须在上述最坏情形补全后，其按仓库聚类的配对 95% 区间仍完全落入 `[-0.025,0.025]`，并且没有已观察或可能被缺失单元隐藏的基线池外新正确解。其他任一升格门失败只维持 DEMOTE；不得用“DEMOTE 或 KILL”回避预注册映射。

## 六、Pilot 3：自适应 handoff–repair 配置

### 6.1 样本、检查点与四格实验

冻结一个 SWE-Gym Lite revision 后按仓库分层抽 80 项，不看 gold patch 或 test patch 选样。用 `SHA256("handoff-tier-v1|"+benchmark_revision+"|"+instance_id)` 在每个仓库层内排序并交替分配，预先固定 40 项早检查点与 40 项晚检查点；保存 digest、排序位置和 assignment manifest，禁止使用跨进程不稳定的 Python `hash()`。早检查点为冻结 scout 完成第二个成功只读行动以后，晚检查点为完成第五个成功只读行动以后；若 scout 在额度内达不到该点，记 applicability failure，不补抽、不换点，并保留其 scout 消耗。它在所有 ITT 比率的分母 80 中记为“未触发”，不能从分析集删除。

Scout 只开放 `list_dir`、`read_file`、`search_symbol`、`search_text` 和 `run_named_test`。禁止文件写入、任意 Python、网络与 `git log/show/branch/tag`。每个 observation 截断到 1,000 个冻结 tokenizer token，\(H_t\) 总预算 10K，one-more 另留 2K，保证 \(H_{t+1}=H_t+\)最后一项 action/observation，而不是挤掉旧证据。handoff 是 issue、文件/符号/行、复现证据与未决问题的确定性 JSON 投影，不调用第二个总结 LLM。

每个 fixer 分支从相同 image digest 和 base commit 的全新容器开始，prompt 只差 handoff。四格为 `{H_t,H_{t+1}}×{cheap,strong}`，每格运行两个完全共同的 repair seeds；同一题的两个 seed ID 必须跨四格复用，同 tools、system prompt、temperature 0、`do_sample=false`、30 步、总墙钟 30 分钟与单工具 5 分钟。修复期允许继续读、改、测，其全部成本进入 repair cost。`abstain` 是 \(H_t\) 与 \(H_{t+1}\) 下都可选的确定性外部选项，定义为零增量效用，不调用 fixer、不生成 patch，也不占 repair seed。

### 6.2 Tier、运行账与分析

优先使用同 scaffold 的开放模型对，例如 SWE-Gym/OpenHands-7B-Agent 与 OpenHands-32B-Agent，或 SWE-agent-LM-7B 与 SWE-agent-LM-32B。正式前另取不与 80 题重合的 20 项，对两个 tier 各跑两个共同 repair seeds，共 `20×2×2=80` 次 fixer calibration runs；要求 cheap 有非零解题率、strong 留下可观增益且单位成本明显更高。本机 RTX 3060 12GB 只是可能的 smoke/timing 资源，不构成 7B 或 32B 可运行性证明；最终 tier、量化、远程 endpoint、GPU 型号与软件栈必须实测后冻结，不能把“可获得硬件”写成“已具备运行资产”。

比较 manifest 必须冻结 fixed SuperScout handoff、SuperScout router/no-router、issue-only router、普通 partial-trajectory success/cost router、Agent-as-a-Router-style execution-feedback router 与 Switchcraft-style agentic cost router；CodeRescue、ECLoop 和 Guided Search 仅在输入/动作可对齐时另报。若没有忠实运行原代码，必须明确写作 `-style` 本地复现并列出差异，不能声称击败原系统。所有 router 共享同一四格 outcome table、rate card、非劣界和部署策略账，禁止让基线使用更少的已发生 scout 成本。

- 80 个 scout processes。早组至多 3 次、晚组至多 6 次模型调用，总计至多 360 次 scout calls。
- 完整四格双种子矩阵为 `80×2 info×2 tier×2 seed=640` 个 repair processes，cheap 与 strong 各 320 个；主体满矩阵为 `80+640=720` 个 agent processes。
- repair 分支至多 `640×30=19,200` 次模型调用，加 scout 后主体至多 19,560 次模型调用；完整矩阵产生 640 个独立 patch evaluations。
- 按每个 repair process 预留 30 分钟，repair-agent 容器额度为 320 container-hours；官方 patch evaluation 再按每 patch 预留 30 分钟，为 320 container-hours。主体必须至少预留 **640 container-hours**，且这还不含 scout。
- 80 次 tier calibration 另预留最多 40 repair-agent hours 和 40 evaluation hours；约 10 次 gold-image infrastructure smoke 另账，均不计入主体 720 个 processes。索引/镜像构建、scout、calibration、repair-agent、patch evaluation 和失败重试六类成本不得合并成一个模糊数字。

上述 640/720 是完整矩阵的预注册容量与 expected-cell 账。若 applicability 或预注册 infra failure 使某格没有启动，事实表仍保存 `NOT_APPLICABLE`/`INFRA` 单元，报告实际 processes 与未用容量；不得补抽或把分母缩小，也不得把缺失单元当作失败 patch 来伪造满矩阵。

每个 arm/tier 使用 `pilot_revision/instance/checkpoint/info/tier/seed` 的唯一 harness run ID。成本必须同时给出两本账：**物理实验账**记录所有实际 scout、四格分支、calibration、评测、基础设施和重试；**部署策略账**只对策略实际选择的 acquisition 与 repair 分支收费，共享 scout prefix 只计一次，`H_t` 前的 sunk cost 不因四格重复，one-more 的增量 acquisition cost 只在选择继续 scout 时计一次。启动前必须冻结各模型输入/缓存/输出 token 上限、模型调用上限、CPU/GPU/内存/I/O/墙钟上限、货币币种与 rate-card revision、成功价值 \(V\)、成本权重 \(\lambda\) 和总预算；任一未冻结时保持 NO-RUN。

冻结 scout 每题只产生一条 \(H_t\rightarrow H_{t+1}\) 轨迹，不得多跑 scout 再选择最有利 observation。对 \(m\in\{cheap,strong\}\)，以两个共同 repair seeds 的均值估计

\[
Q_m(H)=\mathbb E_{seed}[VY-\lambda C_{rep}\mid H,m],\qquad Q_{abstain}(H)=0.
\]

取得前后都用 `max_m E[U]`，而不是对单次 resolved realization 事后取最大；经验 VOI 为 `max_m Q_m(H_{t+1})-max_m Q_m(H_t)-lambda*C_acq(one-more)`。`repair_cost` 与 `acquisition_cost` 都保存冻结 rate card 换算后的同单位原始标量，oracle 工具才统一乘一次 `lambda_cost`；若输入已经效用化，必须使用不同字段与新公式，不能复用现行工具。两个 seed 只提供最小可计算重复，不足以把方差说成已稳定；必须报告 seed sensitivity，并在扩样前增加重复或做顺序精度审查。

80 项只判断 headroom，不训练神经 paired-uplift。`MECHANISM-PROCEED` 要求正经验 VOI 且最优期望效用 tier 改变的 ITT 状态至少约 `16/80`，并报告以仓库为 cluster 的 95% 置信区间、applicability、适用样本条件 tier-switch、ITT tier-switch 和每原始任务成本；点估计过门不等于已获外部贡献。`MODEL-PROCEED` 后才用更大且仓库隔离的标签集训练模型。`CHAPTER-GO` 的 Pass@1 非劣界 \(\Delta_{NI}\)、成功价值、成本权重、比较策略和单/双侧检验必须在四格结果前冻结；独立外测要求 paired/repository-clustered 95% 置信区间下界不低于 \(-\Delta_{NI}\)，并同时使 cost-per-solve、每原始任务成本或 strong-tier 调用率改善约 15%。冻结 policy 的 checkpoint/applicability 或任一适用任务四格不完整时记 `INCONCLUSIVE`；数据有效但未过 16/80 headroom 门时维持 `DEMOTE`。KILL 只在具有预注册功效的后续样本出现任一路径时触发：frontier-crossing 率的 95% 上界仍低于冻结最小相关率；固定 handoff/router 在效用与外部结果的等价界内复制全部收益；或降低 strong 使用时 Pass@1 聚类区间越过 \(-\Delta_{NI}\)。cheap/strong 可解集合嵌套和单次 realized max 都不是 KILL 条件。

### 6.3 冻结数据表

1. `task_checkpoint` 保存 benchmark/revision、instance、repo、base commit、image digest、SHA256 digest/排序位置/检查点 assignment、checkpoint rule、applicability 与失败原因、prefix/fs/config hash、scout model/seed 和完整 scout 成本。
2. `branch_result` 以 expected-cell manifest 为母表，保存 info arm、tier、共同 repair seed、`RUN|NOT_APPLICABLE|INFRA`、model/scaffold/prompt/handoff hash、patch hash、changed files、resolved、FAIL_TO_PASS/PASS_TO_PASS、exit/timeout/infra/leakage。
3. `cost_event` 逐事件保存 `infrastructure|scout|calibration|repair|evaluation|retry` phase、physical/policy ledger 标记、模型/工具调用、输入/缓存/输出 token、wall/GPU/CPU 秒、内存/I/O、rate-card revision、币种与货币成本。
4. `paired_outcome` 保存每格两 seed 的结果与成本、\(Q_m(H_t)\)、\(Q_m(H_{t+1})\)、确定性 `abstain=0`、取得前后最优期望效用 tier、tier switch、acquisition cost、oracle VOI、applicability 与 ITT contribution。
5. `analysis_manifest` 在结果前冻结 \(V\)、\(\lambda\)、\(\Delta_{NI}\)、rate card、`repair_cost` 与 `acquisition_cost` 的原始单位及其到统一标量的换算、比较策略、cluster/CI 方法、缺失与 infra 处理规则；没有该 manifest 不得开跑。

## 七、执行顺序与基础设施门

1. **论文二旧 refinement-proof formulation 永久停止。** Stage-0 whole-token 与该 formulation 分别 NO-GO；ARB16 source readiness 不恢复 build 许可。`semantic_ast_index.py` 仅保留为 synthetic diagnostic：不得走 corpus build、建 SQLite、发布 index、跑 Click/ARB16、读 gold、评分或训练。
2. **论文二新假说保持 DEMOTE/NO-RUN。** 只有建立隔离 Linux/Docker、锁定 RACE/SWE-Gym revision、完成 gold/visibility firewall、实测并冻结 6,400 个确定性标签/评价 jobs、逐臂逐题 `\mathbf b_{m,i}`、逐维聚合 `\mathbf B_{gen,total}` 与训练硬帽后，才可先运行 20 题 debug；20 题不能授权正文或改状态。80 题必须一次性冻结运行，失败不追加样本救题。
3. **另行建立 Linux/Docker 运行仓。** 当前 Windows 工作区只保存论文、protocol、manifest、ARB 正任务资产和分析工具；SWE/RACE 镜像、日志与大缓存应放 D 盘或远程 Linux。不得污染当前 Python 3.12 文献工程。
4. **再做论文一的 8-task micro-screen。** 它比论文三便宜，并直接判断是否存在多个可替代充分配方；少于 2/8 只记 `INCONCLUSIVE`，不得仅凭小样本取消该题。只有预注册 24-task 扩展才具有 MECHANISM 级否决责任。
5. **完成 tier 校准后再跑论文三 80-task pilot。** 未证明 cheap/strong 具有稳定能力—成本差异以前，四格实验没有解释意义。
6. 论文一/三通过 `MECHANISM-PROCEED` 后才生成训练标签；论文二新假说必须先通过本节全部 KILL 门才有资格重新立项。通过 `MODEL-PROCEED` 后才进入外部 Agent 评价；只有通过 `CHAPTER-GO` 才重写摘要、引言与方法。基础设施准备、官方 baseline 或内部 oracle 指标本身都不构成论文贡献。

论文三在 Linux/Docker 和双 tier 以前唯一允许的零推理前置筛查，是对版本锁定、非 solved-only、具有完整逐行动 observation 的 SWE-Gym/SWE-agent 域轨迹做 80 题兼容性普查。输出只能包含预注册 early/late checkpoint 可达率、合法 one-more、污染、可重建/可重放和 acquisition-cost 字段完整性；异策略轨迹不得科学 KILL 当前 policy，且任何轨迹都不得输出 VOI、tier switch 或 repair uplift。不同模型、prompt、scaffold、snapshot 或 seed 的公开结果禁止拼成 cheap/strong 四格。

当前没有因为“公开 benchmark 足够”而可以跳过的步骤。论文一的充分配方和论文三的 paired uplift 必须由本项目实际执行生成；论文二新假说的监督必须来自协议规定的自然 agent patches 与 gold-free claim，负/拮抗边必须来自自然失败候选，不能复用已否决路线的 program labels、现成 qrel、Stage-0 输出、RACE Gold Patch 删改或 synthetic signs。任何现成轨迹或 gold patch 都不能冒充本项目的反事实监督。
