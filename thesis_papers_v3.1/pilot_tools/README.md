# v3.1 立项试验工具

本目录只保存 **oracle/headroom 否决工具、资产检查器与开发性诊断**，不实现论文声称的最终训练模型。论文二的 Stage-0 与 refinement-proof formulation 已分别 NO-GO；相关代码只能复核历史结果或 synthetic diagnostic，不构成继续 build、评价或训练的许可。

治理文件把继续研究分成三级。`MECHANISM-PROCEED` 只允许生成训练标签，`MODEL-PROCEED` 只允许进入独立外部评价，`CHAPTER-GO` 才允许把候选写成论文章节。工具完成、资产就绪、开发集增益或后验 oracle 均不等于任何一级通过；被 formulation-level NO-GO 覆盖的工具连第一级也不得尝试。

## 1. `recipe_family_oracle.py`

输入为 JSONL，每行是冻结上下文集合在一个 patcher/seed 单元上的唯一运行：

```json
{"task_id":"t1","pack_id":"p1","chunks":["a.py:1-20","b.py:8-16"],"patcher":"agent_a","seed":1,"success":1,"token_cost":812}
```

命令行必须显式列出全局冻结的 patcher 与 seed 网格。脚本拒绝重复的 `task × chunks × patcher × seed`，也拒绝网格外运行。每个集合、每个 patcher 的证据分成四态：

- `sufficient`：冻结 seed 网格完整且达到成功门槛；
- `confirmed_insufficient`：网格完整但未达到门槛；
- `underpowered`：只执行了部分冻结网格；
- `missing`：必要 patcher 完全缺失或该集合从未执行。

只有集合本身 portable sufficient，且其 **所有 proper subsets** 都完整执行并 confirmed insufficient，才进入 `inclusion_minimal_family`。只检查一步删除所得的是单独报告的 `one_deletion_local_family`；它不能冒充 inclusion-minimal。`observed_family_intersection` 只是已确认 inclusion family 的交集，不能在搜索未覆盖所有候选时解释成总体“必需核”。低重叠 multi-recipe trigger 只使用 inclusion-minimal family。

```powershell
& '<bundled-python>' .\recipe_family_oracle.py runs.jsonl `
  --patcher agent_a --patcher agent_b `
  --seed 1 --seed 2 --seed 3 `
  --min-runs 3 --success-threshold 0.67 --max-jaccard 0.60 `
  --output report.json
```

## 2. `typed_program_oracle.py`

输入为一个 JSON task specification。事实与义务使用 refinement type 字符串，例如 `Def<foo>`、`CallerSet<foo>`、`TestCovering<foo>`。operator 是冻结执行缓存中已经 grounded 的调用实例：

```json
{
  "task_id":"t1",
  "initial_facts":["FailureFrame<trace_1>"],
  "obligations":["Def<foo>","CallerSet<foo>","TestCovering<foo>"],
  "operators":[
    {"id":"trace_to_foo","inputs":["FailureFrame<trace_1>"],"outputs":["Def<foo>"],"cost":1.0},
    {"id":"foo_callers","inputs":["Def<foo>"],"outputs":["CallerSet<foo>"],"cost":1.0}
  ]
}
```

`--mode refinement` 要求 kind 与实体参数均一致；`--mode coarse` 只用 kind 判断 nominal applicability。无论哪种模式，脚本都逐转移保存 exact inputs、outputs 和 `exact_inputs_satisfied`，所以 coarse 链即使偶然产出 exact goal，只要曾以错误实体满足输入，就不能进入 `semantically_valid_programs`。

搜索是 **确定性的 cost-prioritized、depth/cost/expansion-budgeted search**，不是 BFS。等价的 `(exact facts, used grounded operators, transition exact-validity)` 状态在 enqueue 时去重。coarse checker 达到 nominal closure 后仍继续扩展，直至 exact-valid obligations 闭合或到达预算边界，使同一 grounded operator universe 中的 refinement-valid 后续程序不会因 coarse 提前满足 kind 义务而消失。`max_programs` 只限制结果存储数；搜索是否完整由 `frontier_exhausted`、`termination_reason` 和 `max_expansions` 判断。

```powershell
& '<bundled-python>' .\typed_program_oracle.py task.json --mode refinement --max-depth 3 --budget 6 --max-expansions 500 --output refinement.json
& '<bundled-python>' .\typed_program_oracle.py task.json --mode coarse --max-depth 3 --budget 6 --max-expansions 500 --output coarse.json
```

底层 coarse applicability 关系是 refinement applicability 的超集；报告只在逐转移 exact-valid 且 exact obligations 闭合时计入语义有效程序。有限预算比较必须同时报告搜索是否截断、有效程序数、实际执行质量与 wrong-entity 对抗拒绝，不能把 nominal program count 当成效果。

## 3. `handoff_tier_oracle.py`

输入为同一冻结状态上的 `current/scout × cheap/strong` 因子运行：

```json
{"task_id":"t1","checkpoint_id":"c1","information":"current","tier":"cheap","seed":1,"success":0,"repair_cost":1.2,"acquisition_cost":0.0}
```

另需一个预注册 state manifest，可用 JSON 数组或 JSONL：

```json
{"task_id":"t1","checkpoint_id":"c1"}
{"task_id":"t2","checkpoint_id":"c1"}
```

本工具采用以下冻结口径：每个 task/checkpoint 的 `H_t` 与一次 scout 后的 `H_{t+1}` 都已固定，seed 只是 fixer 的重复随机性。因此估计量是

\[
\max_m E_{repair\ seed}[U_m(H_{t+1})]
-\max_m E_{repair\ seed}[U_m(H_t)]
-\lambda C_{acq},
\]

而不是 scout observation 随机时的 `E[max]`。如果未来允许随机 scout，必须另设 `scout_seed` 并做嵌套估计，不能复用本工具的 repair seed。

`abstain` 是效用为 0 的外部选项，不需要额外运行格。repair utility 先在 cheap、strong、abstain 中取最大；冻结 acquisition cost 与 tier、repair seed 无关，并只在 scout max 外扣一次。current acquisition cost 必须为 0。脚本拒绝重复 cell/seed、网格外 state/tier/seed 及跨 tier/seed 不一致的 scout cost。

严格 expected-seed 配对默认开启；每个 cell 必须恰好覆盖冻结 seed 网格。完全没有运行的预注册 state 仍保留在 `incomplete_states`，主要正 VOI、tier-change 与正 VOI tier-switch 比例均使用全部 expected states 的 ITT 分母；complete-case rate 只作诊断。

```powershell
& '<bundled-python>' .\handoff_tier_oracle.py runs.jsonl `
  --expected-states expected_states.jsonl `
  --expected-seed 1 --expected-seed 2 `
  --lambda-cost 0.02 --min-runs 2 --strict-pairs `
  --output report.json
```

`--allow-unpaired` 只供探索性诊断，不得用于 GO 判定。如果正式 pilot 每格只运行一次，必须预注册单 seed 并显式使用 `--min-runs 1`；若坚持 `--min-runs 2`，运行预算必须包含每格两个 fixer repeats。

## 4. 资产检查、抽样与官方基线

`check_readiness.py` 只做离线、只读环境检查。它不会回显环境变量值、模型端点、WSL 名称或本地资产绝对路径。ARB 根目录必须显式传入；路径本身只用于存在性检查。

```powershell
& '<bundled-python>' .\check_readiness.py --arb-path '<arb-root>' --compact
```

`sample_arb_pilot.py` 与 `sample_arb_abstention.py` 生成 query/gold-blind 冻结清单；`normalize_arb_corpus_manifest.py` 只重定位本地 corpus 路径。`summarize_arb_baselines.py` 复核三类正任务的官方 lexical、BM25 与 RepoMap 输出。其 `gold_coverage@8k` 是 8,000 **字符**的 legacy 字段，不是 canonical token-budget BCY。

当前已冻结的正例清单是 `pilot_manifests/arb60_selection_v0.json`，三类任务各 20 题。选择性清单虽已冻结 10 个 natural no-gold 与 10 个 wrong-repository 样本，但自由文本 query 不能无损映射到三类正任务 grammar，逐题 lexical 与 RepoMap 输出也不齐，因此选择性批次保持 `NO-RUN`。

### 4.1 ARB16 full-source reserve：readiness 保留，build 已取消

`sample_arb_semantic_reserve.py` 在排除 ARB60 已见任务与 `(repo,base_commit)` 后，query/gold-blind 冻结 16 题、16 个未见 snapshot。冻结 manifest 是 `pilot_manifests/arb16_semantic_fullsource_reserve_v0.json`，SHA256 为 `99E86EB181249CF1F91C944ED0F178F3F4332CA314F03468765B2535ADEDF212`；manifest 本身的授权仍是取得并哈希核验完整源码，不是语义运行。

`verify_arb_semantic_sources.py` 只读取该 reserve 与本地 bare Git object store：核验 commit、枚举完整 tree、实读 blob、记录 Git OID 与独立 SHA256，并用标准库 AST 解析完整 `.py` blob。机器报告 `pilot_reports/arb16_semantic_fullsource_readiness_v0.json` 的 SHA256 为 `DE53103C2DB6D89D35C41BE00BB6D888BA73EFD3E317B7581761809EF2EAE337`；简明审计报告 `pilot_reports/arb16_semantic_fullsource_readiness_v0.md` 的 SHA256 为 `E1C087A4611A4AD272484049046952E4105AF9F363E4394CF5E030C927C6938C`。

readiness 结果是 16/16 snapshot、5 个仓库、24,668 条 snapshot×path file rows、15,230/15,230 条 Python AST parsed、所有 query path 存在且可解析；去重后实读 13,421 个 blob、209,590,988 bytes。报告中的资产状态仍是 **`READY_FOR_SEMANTIC_INDEX_BUILD`**，但后续 formulation-level NO-GO 已覆盖其 build authorization。本运行始终保持 **0 gold/qrel、0 retrieval scoring、0 program evaluation、0 training**；readiness 不是 semantic mechanism evidence。

### 4.2 `semantic_ast_index.py`：diagnostic only

冻结代码 SHA256 为 `C281BB6A0EDC613DE64E50EE37F48CF81ABC9BF34E949FA90E5885C6D2FA19CF`；`test_semantic_ast_index.py` SHA256 为 `D907338C4A0074029C3B46C5D06344CE2699767EC8E6ED86AEBF8E6765FA4D49`。compile、warnings-as-errors 与 19/19 tests 通过。三组 synthetic fixtures 的白名单 property 覆盖 19 entities、19 scopes、18 edges、19 resolution sites、21 witnesses、8 CERTIFIED edges，并检查 foreign keys、candidate retention、snapshot partition、witness ordinal 和重复构建确定性。该结果只说明 diagnostic 子集无剩余 P0。

certificate core 刻意 fail closed：CERTIFIED CALL/REF 仅限同 module、稳定顶层 function/async-function 的 simple Name 与 `lexical_unique_binding`；CERTIFIED IMPORT 仅限 module→module 的 `SOURCE_SYNTAX_MODULE_IMPORT`；AS_TEST 只认稳定 role，fixture 无 CERTIFIED edge。`globals()`/`vars()`、`exec`、runtime rebinding 与 monkeypatch 使跨模块 symbol identity 必须标为 DYNAMIC，除非实现接近完整 Python 动态语义分析。若改称 assumption-bound lineage，generic provenance/equality guard 又可直接复制。因此该 refinement-proof formulation 已 **NO-GO**，不是“等待更多工程”的 INCONCLUSIVE。

不要调用脚本的 corpus `build` 路径。正式 build 已中止，约 3.46 GB 临时产物已删除；没有 SQLite、没有发布 index、没有 Click/ARB16 运行、没有 gold/scoring/training。原 primitive、selector 与 `ORACLE-BUILD-PROCEED_16` 条款只保留在治理文档中作历史复盘，不能恢复执行。P2 题位仍未定。

## 5. `arb_typed_program_pilot.py`

这是论文二的 **Stage-0 exact-identifier-lineage 历史开发诊断**，不是语义 refinement-type compiler。它曾用当时冻结的字段规则、官方预切 ARB chunks，以及 failure label、合法 path stem 和 ARB `symbol` 形成 reduced anchor-symbol catalog，再查找 whole-token occurrence provenance；凡由 reference PR/result 派生的字段在现行 query 白名单下都必须排除，因此该输出不能冒充新版 constructor 的 query-only 结果。它也不证明 call、import、test、dependency、root-cause 或因果关系；注释和字符串中的同词仍会命中。

程序搜索和 query-only deployment selection 在读取 gold 前冻结。部署选择器只在认证的 refinement candidates 中按 `(nominal cost, operator depth, canonical program tuple)` 取最小。完成后才加载 gold 计算该冻结输出的分数；`best_found_posthoc_oracle` 只作上界，不能当算法成绩。

```powershell
& '<bundled-python>' .\arb_typed_program_pilot.py `
  --arb-data-root '<arb-data-root>' `
  --selection-manifest '..\pilot_manifests\arb60_selection_v0.json' `
  --budget 3 --max-expansions 512 `
  --output '<raw-development-jsonl>'
```

主质量量尺严格使用官方等价 `regex_code_tokenizer_v1`、`### path` renderer 与 8,000-token canonical BCY。code2test 与 edit2ripple 的 operator depth 3 包含一个 certificate 步骤，实际 retrieval-transition depth仍为 2。逻辑 `cost_units` 只用于同 grammar 的算子账，绝不能替代三遍全 corpus scan 的 rows、bytes 与 wall time。

当前 corpus 文件未做逐遍内容 digest pin。静态本地 discovery 只是一项 reduced-catalog 历史诊断，`UNSAT` 不能用于 proof-grade 或 confirmatory 声称。原计划中的 semantic relations、PyRAG 基线、depth ablation 与对抗集不再作为待补任务；在 P2 另行立项以前不得继续建设。

## 6. 开发性结果汇总

`summarize_arb_typed_discovery.py` 只汇总冻结的 60 题开发批次。它必须保留全部 60 题，分开 query-only deployment 成绩与 post-hoc oracle ceiling，从官方明细补齐早退样本的 baseline，并报告 canonical BCY、Recall、三榜并集外命中、决策、完整性、搜索工作量与真实 I/O。报告标题不得写成 semantic algorithm evaluation，也不得输出 `MECHANISM-PROCEED`。

## 验收边界

- 这些脚本只诊断问题是否存在，不生成可发表 checkpoint。
- 任何内部 family、lineage 或 tier-switch 指标都必须再连接到官方测试、Pass@1 与完整成本。
- P2 的 `semantic_ast_index.py` 只允许 synthetic unit tests 与静态复核；不得 build corpus 或生成索引资产。
- 输入数据、候选池、agent、patcher、repair seed、tokenizer、容器镜像和 commit 均须在正式 pilot manifest 中冻结。
- 只有 `00D_三篇高杠杆替代题与立项门.md` 的对应分级条件通过后，才允许生成训练标签、实现模型或恢复论文写作。
