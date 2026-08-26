# 论文三标签日志与 Oracle 隔离 Manifest

## 1. 状态、用途与权限

统一状态：**REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN**。

本文件是 C3 的字段级实现合同，不是已经生成的数据字典或实验结果。所有镜像 digest、文件 hash、样本模拟输出、标注一致性、ESS 和 leakage probe 结果均为 `PENDING-IMPLEMENTATION`。修补者无权依据本文件自行判定 `DESIGN-FROZEN`；未参与修补的独立审查者必须核对实现产物与本合同一致后，才能决定是否恢复冻结。

本 manifest 同时约束五个责任：理论状态的独立标签，candidate lattice 的 oracle-blind 生成，真人 logging 的支持度，confirmatory 结果与训练数据的隔离，以及 confirmatory participant 的固定四臂随机化与参与者簇分析。任何实现若缺少下述字段，不得通过默认为零、从 outcome 回填或用 LLM judge 补齐。

## 2. 角色、镜像与信息流

| 角色 | 允许读取 | 允许写入 | 禁止读取 | 镜像或版本 digest |
| --- | --- | --- | --- | --- |
| `trusted_mediator` | public issue/task、canonical action bytes、repo/container、base commit、pre-state、working-tree、permission 与 scope | immutable `trial_binding_manifest` 与唯一 `binding_digest` | participant response、approval、harm、task success、gold/G/hidden、evaluator output | `PENDING-IMPLEMENTATION` |
| `task_author` | public issue/task、已冻结 `binding_digest` 及其 canonical action/pre-state/permission/scope bytes、组织约束 | `J_content`、proposition text、`m_req/κ`、四个事实/transfer bank 与答案来源 | participant response、approval、harm、task success、gold patch、G state、hidden tests | `PENDING-IMPLEMENTATION` |
| `candidate_generator` | issue/task、`binding_digest`、bound pre-state、`J_content/m_req/κ`、public tests、authorized tools、预先声明的预算 | action grammar、静态候选、动态分支模板、slot schema、mask、cost、timeout、ordering、provenance、Merkle root | gold patch、G state、hidden tests、hidden labels、evaluator output、participant/confirmatory response | `PENDING-IMPLEMENTATION` |
| `branch_instantiator` | T−2 已冻结的 grammar/template/source bank、parent state/hash、可见 response 特征、`UNKNOWN`、明示 clarification request、public execution record、决定性 seed | 可重放的 `clarify/repair` branch bytes/hash 与 generator trace | 自由文本新候选、approval/deny、gold/G/hidden、evaluator output、sealed outcome | `PENDING-IMPLEMENTATION` |
| `logging_policy` | cap 后 retained candidate set、动作前 `S_t^pre`、冻结的 `q-policy-v1` checkpoint/schema | cap 后 logits、归一化 `q_cls/q_cand`、两级 mixture propensity 与 selected `A_t` | discarded candidates、approval/deny、gold/G/hidden、evaluator output、post-action response/trigger | `PENDING-IMPLEMENTATION` |
| `public_sandbox` | bound B/pre-state、canonical proposed action、public tests、authorized tool image | B-state 或 candidate-S-state 的公开可得 execution record | G state、sealed evaluator、hidden tests | `PENDING-IMPLEMENTATION` |
| `hidden_evaluator` | 已冻结 lattice/branch root、sealed hidden tests、gold/G state、专家 adjudication rules | hidden functional/security/scope/state-damage 真值与 sealed outcome | participant identity、policy logits、理论状态、候选生成内部状态 | `PENDING-IMPLEMENTATION` |
| `interaction_logger` | renderer events、policy action、known propensity、human response、clock、public tool execution | append-only interaction log | hidden evaluator output、gold/G state | `PENDING-IMPLEMENTATION` |
| `label_annotator` | 去标识化的指定日志切片与标注手册 | `C/M/paired_interpretation` 标签、`UNKNOWN` 原因 | approval、harm、task success、hidden evaluator、模型预测 | `PENDING-IMPLEMENTATION` |
| `policy_trainer` | training split、冻结 lattice、propensity、训练标签、external training reward | checkpoint、calibration map、training log | confirmatory participant、confirmatory repo/risk、sealed test labels | `PENDING-IMPLEMENTATION` |
| `arm_allocator` | 分臂前落盘的 `baseline_reviewer_support`、`salted_participant_id`、冻结域字符串/schema 与安全服务中的 `K_arm` | 唯一 participant-level `A/B/C/D` assignment、HMAC digest、mapping receipt 与 protocol-deviation flag | trial 内容、过程日志、human response、approval、harm、task success、gold/G/hidden | `PENDING-IMPLEMENTATION` |
| `confirmatory_runner` | 冻结 checkpoint、界面、预算、lattice/branch grammar、primary 与 micro-secondary 随机化方案 | 盲态试验日志与 same-reviewer identity receipt | training update API、task-author editing API、hidden evaluator internals | `PENDING-IMPLEMENTATION` |

信息流只能是 `trusted_mediator → binding_digest → task_author → proposition/criterion/bank manifests → candidate_generator → lattice/branch-root hash → hidden_evaluator`，以及 `candidate_generator/branch_instantiator → Cap8Fn-v4 → S_t^pre → q-policy-v1 → interaction_logger`。confirmatory 分臂另有唯一单向流 `baseline_reviewer_support + salted_participant_id + precommitted HMAC schema/K_arm → arm_allocator → fixed participant arm receipt → confirmatory_runner`；allocator 不接收 trial、过程或结局字段，runner 不得要求重分配。当 logger 收到合法的 visible response/UNKNOWN/clarification request 时，仅把该事件 receipt 与可白名单的 public execution fact交给 `branch_instantiator`，再把决定性 branch bytes/trace 追加回下一 opportunity 的 cap。`branch_instantiator` 只能在 T−2 冻结的重放合同内消费这些字段，不得扩展 grammar 或换用未承诺的事实源。`q-policy-v1` 只能读取 cap 后集合，不能向实例化、排序或 cap 回传信息。hidden evaluator 不得向 mediator、task author、generator、instantiator、renderer、logging policy 或 participant 返回任何字段；其标签只进入 sealed outcome store 和获授权的离线评价阶段。

## 3. 时序状态机

confirmatory cohort 使用参与者级全局时序叠加下表的每 trial 状态机。每名参与者的 `baseline_reviewer_support`、十二个计划任务与顺序属性先落盘；每个 trial 的 binding、`J_content/m_req/κ` 与 measurement item bank 先完成 T−5/T−4，随后只在参与者级分臂一次。分臂完成后，十二个计划 trial 始终使用该固定臂；任务缺席、无法完成或日志损坏只能进入预注册缺失/偏差字段，不触发重新随机。

| 时点 | 必须完成的事件 | 此后冻结的对象 | 尚不可见的信息 |
| --- | --- | --- | --- |
| `T−6 split` | 按 participant、repository、base commit、issue/bug family、risk family、generated-test lineage 和 gold-derived sibling 分组分配 split | `split_group_manifest` | 所有 participant response 与 outcome |
| `T−5 bind` | trusted mediator 先冻结 canonical action bytes/hash、repo/container、base commit、pre-state、working-tree hash、权限与作用域，并计算覆盖全部字段的 `binding_digest` | `trial_binding_manifest`、`binding_digest` | participant response、approval、harm、task success、gold/G/hidden 与 evaluator output |
| `T−4 purpose` | 两名独立 task author 只针对同一 `binding_digest` 冻结 proposition、`J_content`、`m_req/κ`、`probe_train/paired_interpretation/transfer/confirmatory_factual` 四个 bank 与来源 | `proposition_manifest`、`criterion_manifest`、`measurement_item_bank_manifest` | participant response、approval、harm、task success、gold/G/hidden outcome |
| `T−3.5 participant-arm` | 只读处理前 `baseline_reviewer_support` 与 `salted_participant_id`，由预提交 HMAC 函数把参与者一次分入 `A/B/C/D`；十二个计划 trial 同臂 | `participant_arm_assignment_manifest`、`arm_assignment_receipt`、`arm_persistence=all_12_planned_trials` | 所有 trial 过程、response、approval、harm、task success、gold/G/hidden；allocator 不可读 |
| `T−3 generate` | generator 仅用部署可见字段生成 action grammar、静态候选、`clarify/repair` branch grammar、template/slot schema、允许事实源、mask、cost、timeout、ordering 与 termination | generator working set | gold/G/hidden、harm label、participant response、approval |
| `T−2 lattice-and-branch-commit` | 在任何 logging、human response、approval 或 hidden evaluator 前，写入完整静态 lattice、动态分支承诺，以及 `CandidateSetFn-v4/Cap8Fn-v4/q-policy-v1` 的 executable/checkpoint hash、输入 schema、dtype、temperature、mask/normalizer/tie rule；预枚举模式承诺 instance bytes/hash，参数 grammar 模式承诺 image、Merkle root、deterministic seed/replay contract | `candidate_lattice_manifest`、`branch_commitment_manifest`、`branch_merkle_manifest`、`candidate_cap_policy_manifest`、`q_policy_manifest` | evaluator output 与 participant response；commit 后禁止换函数、版本、模板、事实源、排序字段、cap 或 q checkpoint |
| `T−1 sealed-eval` | 独立 evaluator 才可运行 hidden tests/G comparison，并把结果写入 sealed store | hidden outcome | generator、policy、renderer、participant 均不可见 |
| `T0 log-action` | 先由冻结 generator/instantiator 用既往可见历史枚举全部 public-only instances，再用 `Cap8Fn-v4` 写 retained/discarded IDs 与排序字段；其后写入不含当前处理的 `S_t^pre`，最后由 `q-policy-v1` 只在 retained set 上计算归一化数值并按已知两级 propensity 抽取单列 `A_t` | instance/cap trace、pre-action state、q logits/probability、class/candidate propensity、eligible denominator、selected treatment、history/eligibility signature | 当前动作后的 response、repair trigger、最终 approval 与 sealed outcome；q 不得读取 discarded set或影响 cap |
| `T1 interact` | 记录 evidence exposure、factual response、clarification、repair 与 uptake；分支出现只能由 visible response、`UNKNOWN` 或 explicit clarification request 触发，并依 T−2 合同决定性重放 | append-only human log、branch instance bytes/hash/trace | sealed outcome、approval、hidden/G/gold |
| `T2 return-gate` | `stop` 把事件交还外 gate；与 C3 交互、接收证据并作出当前 canonical action 最终决定的同一审核者作 approval/deny，外部 gate 只记录或执行该决定 | C3 trajectory、same-reviewer receipt | C3 policy 不得接管批准；主试验不得换人或加 second reviewer |
| `T3 outcome` | 将 T2 same-reviewer approval/deny 与 sealed evaluator/专家 adjudication 产生的 safe/unsafe 真值联结为 external outcome | outcome table | 专家不产生 participant decision；outcome 不得回写任何理论标签或 lattice 字段 |

canonical action bytes/hash、pre-state、working-tree hash、permission 或 scope 在 `T−5` 后任一变化时，旧 `binding_digest` 及全部下游对象均标记 `INVALIDATED`：proposition、`J_content`、`m_req/κ`、四个 bank、generator working set、lattice、branch root/instance、evidence、factual response、`V/B_H/C/M/g_pot/g_est/r` 与 mediator item set 全部失效。新对象必须重新执行 `T−5 bind → T−4 purpose → T−3 generate → T−2 commit`；任何旧 purpose/criterion/bank hash 不得进入新 trial。不得只清理显示缓存。

## 4. 共同标识与可见性字段

| 字段 | 类型 | 产生时点 | 训练可见性 | confirmatory policy 可见性 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `trial_id` | UUID | T−6 | 是 | 是 | 不含 outcome 语义 |
| `participant_group_id` | salted group ID | 招募后 | 仅 training split | 当前参与者自身历史摘要 | 原 ID 另库存放 |
| `salted_participant_id` | canonical salted ID | 招募后、分臂前 | 只用于 split/fold/replay | runner 只见 assignment receipt | salt、Unicode 规范化、编码与长度边界由 arm schema 冻结，不含 trial/outcome 语义 |
| `baseline_reviewer_support` | enum `low/medium/high` | 分臂前 | 是 | 是 | 唯一 randomization stratum；值与产生时间在 allocator 调用前落盘 |
| `planned_trial_index/task_order_hash` | int/SHA-256 | 分臂前 | 是 | 是 | 每人固定 12 个计划 trial 及顺序；不因分臂、响应或结局调整 |
| `confirmatory_arm/arm_assignment_digest` | enum `A/B/C/D` / SHA-256 | T−3.5 participant-arm | 分析可见 | runner 只见当前固定臂 | participant-level 一次分配，一人 12 trial 同臂；人工 override 只记 deviation，不改分配 |
| `arm_domain/seed_hash/allocator_hash/schema_hash` | string/SHA-256 | 首例入组前 | 是 | 是 | domain 固定 `C3-CONF-ARM-20260816-v1`；`seed_hash=SHA256(K_arm)` 必须在入组前填真实 64 位 hex |
| `repo_group_id/base_commit/bug_family/risk_family` | categorical | T−6/T−5 | 按 split | 当前 trial 部署可见部分 | risk family 不等于 hidden unsafe label |
| `canonical_action_hash/binding_digest` | SHA-256 | T−5 | 是 | 是 | digest 同时绑定 diff/command/tool args、repo/container、pre-state、permission 与 scope |
| `pre_state_hash/working_tree_hash` | SHA-256 | T−5 | 是 | 是 | 变化使 purpose 及全部下游对象失效 |
| `lattice_hash/branch_commitment_root` | SHA-256/Merkle root | T−2 | 是 | 是 | 对静态候选及动态 grammar/template/source/seed/replay 合同承诺 |
| `candidate_set_fn_hash/cap8_fn_hash/q_policy_hash` | SHA-256 | T−2 | 是 | 是 | 冻结实例化、public-only cap 与产生条件分布的 q 函数；不是预填未来状态的数值概率 |
| `interaction_participant_id/final_approver_id` | salted identity pair | T1/T2 | 仅 outcome 联结 | runner 可验等值 | primary outcome 必须相等，不相等只进入预注册次级分析 |
| `canonical_decision_action_hash` | SHA-256 | T2 | 仅 outcome 联结 | 是 | 必须等于 T−5 `canonical_action_hash` |
| `logging_propensity` | float `(0,1]` | T0 | 是 | 不适用 | 必须记录 eligible denominator |
| `public_history_hash/eligibility_state_signature` | SHA-256 | T0、动作抽样前 | 是 | 是 | 只承诺 `S_t^pre`、合法动作集、pre-action phase/budget；禁止 selected action 与 post-action trigger |
| `split_role` | enum | T−6 | 是 | runner 只见 confirmatory 或 micro_secondary | `pilot/train/validation/confirmatory/micro_secondary`；micro_secondary 不复用前三类 participant/trial |

## 5. 理论状态的独立标签合同

### 5.1 字段级 schema

| 字段及 shape | 允许来源与产生时点 | 可见字段 | 禁止来源 | 标注与一致性 | `UNKNOWN` 处理 |
| --- | --- | --- | --- | --- | --- |
| `J_content∈{0,1}^{P×4}` | T−4；task author 只从已冻结 `binding_digest` 与 task/action manifest 标注 objective/resource/risk/commitment | public task、bound canonical action、pre-state、permission/scope、组织约束 | 理论模型输出、approval、harm、task success、gold/G/hidden | 两名作者独立多标签；第三人裁决；报告 raw agreement 与 Krippendorff α；每行保存 `binding_digest` | 无法归类则命题退回重写，不以全零进入训练 |
| `R_joint→content∈{0,1}^{3×4}` | 设计常量；identification→objective、ability→resource+risk、willingness→commitment | 理论原文 | 数据拟合、outcome | 代码单元测试固定非零位置 | 不允许 UNKNOWN；mutual belief 不占行或列 |
| `m_req∈{0,1}^P`、外生 `criterion_spec(κ)∈[0,1]^P` | T−4；独立作者只针对同一 `binding_digest` 依据 approval purpose 与组织约束冻结 | `J_content`、公开风险规范、可观察 action scope；必填 `criterion_scale_version/criterion_basis/required_response_bank_hash/threshold_unit/threshold_sensitivity_grid/binding_digest` | participant response、approval、harm、task success、gold/G/hidden、后验调阈 | 两作者独立设定，第三人裁决；连续阈值报告 ICC 与分歧区间；每条保存 `created_at/annotator_id/adjudicator_id` | 未达一致的命题不得进入主实验 |
| `criterion_measurement_t` | T1；从预注册 factual/transfer bank 获取的可观察 action-specific fact accuracy/calibration | 独立题库回答、item-source hash、measurement time | 神经 `g_est`、approval、harm、hidden outcome、用本受试者结果重定义 `κ` | 题目真值由 task author 与 public-sandbox fact 双核；保存 `item_id/time/annotator_id` | 未回答、不适用与无法核定分类编码；按预注册缺失规则处理，不以 0 代替 |
| `V_t∈[0,1]^{P×2}` | T1；renderer access log、agent-visible context 与权限日志 | 实际曝光、访问权限、acknowledged receipt | response correctness、approval、harm | 系统日志主标；随机双人审计日志—界面一致性 | access 状态未知则保留 UNKNOWN，不推定已可见 |
| `g_pot,t∈[0,1]^P` | 由 `V_t` 与预注册 access function 计算 | 仅 `V_t` | response、approval、hidden outcome | 代码单元测试与校准，不单独人工造真值 | 任一必要 access UNKNOWN 时为 UNKNOWN |
| `B_H,t∈Π_pΔ^{K_p∪{UNKNOWN}}` | T1；`probe_train_bank` 的 action-specific post-state prediction、scope/permission/rollback 事实题 | 当前证据、回答、可信 public execution fact | confidence、停留时间、approve click、harm、同题最终结果 | 题目答案由 task author 与 public-sandbox fact 双核；train/validation item 不复用；保存 `response_event_id/observed_at/annotator_id/source_fact_hash` | 不确定、拒答、题目不适用各自保留；loss mask，不并入正确/错误 |
| `C_t∈[0,1]^{P×4}` | T1 后；盲态日志标注 `presentation/clarification/repair/grounding_acceptance` | 去标识化话轮、action/proposition binding、`grounding_event_id/observed_at/annotator_id` | gate-level approval/deny、harm、task success、模型 act tag 作为真值；schema validator 拒绝 `event_type=approve` | 两名盲态标注者；第三人裁决；每批报告 Krippendorff α | 无法判定阶段则 UNKNOWN，不自动当 `grounding_acceptance` |
| `M_t[:,1]∈[0,1]^P` | T1 后；与 C 标注事件不同的 action-specific understanding evidence 或 paired interpretation | `human_understanding_evidence_event_id/paired_interpretation_item_id/observed_at/annotator_id` | C 的同一 `grounding_event_id`、礼貌确认、approval、LLM 自评、hidden outcome | 两名盲态标注者；第三人裁决；event-ID 独占性校验 | 缺少独立理解证据则 UNKNOWN，不回填 0 |
| `M_t[:,2]∈[0,1]^P` | T1 后；系统采用修正、人看到该 uptake，再以独立 paired item 确认 | 必填 `system_uptake_event_id/human_exposure_receipt_id/paired_confirmation_item_id/observed_at/annotator_id` | 仅生成 repair 但人未暴露、C 的同一 response、approval、LLM 自评、hidden outcome | 两名盲态标注者；第三人裁决；三 ID 不得缺失 | 无人类可观察 exposure 或后续 paired confirmation 时保持 UNKNOWN；任一 M 方向 UNKNOWN 不得判 criterion 满足 |
| `g_est,t∈[0,1]^P` | 模型估计；用与 `probe_train_bank` 不重合的 `paired_interpretation_bank` 和 `transfer_item_bank` 校准 | `g_pot,B_H,C,M` 与外生 criterion | approval、harm、task success、同题 response、hidden/gold | 没有“真实信念”真值；只报告 calibration、transfer validity 和干预响应 | UNKNOWN 不插为 0；mask loss，且该命题不能触发 stop-as-met |
| `r_t=m_req⊙max(0,κ−g_est,t)` | 在线确定性计算 | `m_req,κ,g_est` | outcome 回填 | 单元测试 | `g_est` UNKNOWN 时 `r_t` 保留 unresolved 标记 |

schema validator 对理论状态执行三项交叉约束。第一，`κ` 是外生 criterion specification，`criterion_measurement_t` 是可观察测量，二者的 field ID、producer 和 lineage 必须不同。第二，同一 response/event ID 不得同时定义 `C_t` 与 `M_t`；`C` 记录互动阶段，`M[:,1]` 需要独立 understanding/interpretation event，`M[:,2]` 需要时序更后的 uptake–exposure–confirmation 三联证据，三类目标 event ID 不得重用。第三，每个 `UNKNOWN/NOT_APPLICABLE/INVALIDATED/MISSING_LOG` 必须同步保存 `status_time/annotator_id/reason_code/forbidden_source_check`，不允许无时点或无责任人的空值。

### 5.2 题目 bank 隔离

- `probe_train_bank` 用于训练/更新 `B_H`，不得用于 `g_est` 校准或 confirmatory mechanism outcome。
- `paired_interpretation_bank` 用于检验审核者解释与系统 uptake 是否对应，不包含 approval 或 hidden outcome。
- `transfer_item_bank` 在 repair 后用新的等价事实题检查理解能否迁移，不能重复系统刚才问过的文字。
- `confirmatory_factual_bank` 只在冻结模型的前瞻 cohort 使用，不回流任何模型。
- 四个 bank 按 proposition lineage、task、repo 和 participant 成组隔离，保存 item-source hash。

### 5.3 一致性与失效门

每个需人工标注的标签至少双标 20% 和所有争议样本；主训练前计算 raw agreement、Krippendorff α，连续 `κ` 另计算 ICC。规划失效门为 α `<0.67` 或关键类别样本 `<40` 时暂停该标签训练、修订手册并重新 pilot。该阈值是预注册规则，不是已经得到的一致性结果。

`UNKNOWN`、`NOT_APPLICABLE`、`INVALIDATED` 和 `MISSING_LOG` 是不同状态。任何预处理都不得把它们折叠为负类；只有 `UNKNOWN` 可以触发新的 `acquire/factual_probe/clarify/repair` 或在预算耗尽时 `stop` 返回外部 gate，不能作为低风险、已理解或批准建议。

## 6. Oracle-blind candidate lattice schema

### 6.1 允许动作

顶层动作枚举固定为：

1. `acquire`：在授权 sandbox 中执行 public test、dry run、mutation/fuzz、dependency/call/taint/scope/provenance 或 rollback probe。
2. `present`：选择并排序已取得的 action-bound evidence。
3. `factual_probe`：询问一项可由部署可见事实核定的 post-state、scope、permission 或 reversibility 问题。
4. `clarify`：针对已观察歧义请求澄清，不作批准建议。
5. `repair`：依据审核者反馈重新呈现或取得能修复同一命题误解的证据。
6. `stop`：结束 C3 循环并返回外部 gate。

动作中不得出现 `risk_score/approve/deny/allow/when_to_ask/reviewer_assignment/second_reviewer`。人员分配、升级和批准由外部系统承担。

### 6.2 每个候选的冻结字段

| 字段 | 类型 | hidden 前必须冻结 | 说明 |
| --- | --- | --- | --- |
| `action_id/action_class` | string/enum | 是 | 绑定 trial 与 proposition |
| `parameter_schema/authorized_tool` | JSON | 是 | 只能调用白名单工具和参数范围 |
| `precondition/eligible` | boolean expression | 是 | 由部署可见状态决定 |
| `action_mask/mask_reason` | bool/enum | 是 | 不得由 hidden failure 决定 |
| `expected_cost/timeout` | float/int | 是 | 来自 public profiling 或固定预算 |
| `ordering_key/ordering_seed` | string/int | 是 | hidden 后不得重排 |
| `proposition_binding/evidence_dependency` | list | 是 | 绑定 `J_content` 命题但不含 hidden label |
| `generator_source/provenance` | string/hash | 是 | 记录 public test、tool grammar 或模板来源 |
| `candidate_content_bytes/candidate_content_hash` | bytes/SHA-256 | 是 | 静态候选保存完整 bytes；动态候选按第 6.3 节承诺 |
| `static_mask/eligibility_expression_digest` | bool/SHA-256 | 是 | 静态不合法与运行时可见触发分开，表达式不得读 hidden 或 approval |
| `branch_trigger_expression_digest` | SHA-256 | 是 | 只允许 visible response、`UNKNOWN` 或 explicit clarification request 使分支出现；public execution 只可实例化事实 slot，不得触发新分支 |
| `branch_template_id/slot_schema_digest` | string/SHA-256 | 是 | `clarify/repair` 的模板与 slot 类型、边界、排序同时冻结 |
| `allowed_factual_source_ids/source_bank_root` | list/Merkle root | 是 | 只能引用 T−2 前承诺的 public/task/action fact |
| `parent_state_schema/parent_state_hash_rule` | JSON/SHA-256 rule | 是 | 绑定 parent lattice、history、action 与 proposition IDs |
| `branch_budget/cost/latency_bucket/termination_rule` | JSON | 是 | 预算、成本、时延与终止都不得依 outcome 调整 |
| `actual_public_latency/public_execution_status` | float/enum | 动作执行后追加 | 只来自 public sandbox；hidden evaluator latency 永不进入 |

### 6.3 T−2 `clarify/repair` 动态分支承诺与重放

每个 trial 在 T−2 必须选择且只能选择一种分支承诺模式。

1. **有限预枚举。** 对每个 `K_p∪{UNKNOWN}`、可见 clarification request 与 budget bucket 的可达分支，保存完整 candidate bytes、`candidate_content_hash`、`static_mask`、`eligibility_expression_digest`、`branch_trigger_expression_digest`、ordering、action-bound proposition IDs、cost、latency bucket 与 termination。public execution record 只可填入已触发分支的预承诺 factual slot，不得决定分支是否出现。未在枚举表中的字节串永远不合法。
2. **参数 grammar。** 无法枚举所有可见回答时，不允许运行时自由生成。T−2 必须冻结 `branch_grammar_id/version/hash`、template bytes/root、slot schema、`content_instantiator_version/instantiator_image_digest`、`runtime_input_whitelist`、全部 allowed factual source bytes/hash/Merkle root、parent-state schema/hash rule、action-bound proposition IDs、budget/cost/latency/termination、决定性 seed 派生规则与 replay executable hash。相同承诺的 baseline 和 C3 必须共用同一 instantiator、seed 及生成的完全相同 branch instances，不得各自调用 LLM 补内容。

参数 grammar 的 instance 必须满足

`branch_instance_hash = H(parent_lattice_hash || branch_commitment_root || parent_state_hash || visible_response_hash || public_execution_hash || deterministic_seed || instantiated_bytes)`。

`visible_response_hash` 只可覆盖用户的可见 factual response、`UNKNOWN` 或显式 clarification request，且只有这三类事件可使分支出现。`public_execution_hash` 可为已触发分支的预承诺 slot 提供事实内容，但不得成为分支触发器。分支出现不得以 approval/deny、hidden outcome、G/gold、evaluator availability、sealed latency 或专家真值为触发条件。每次实例化都保存 input hashes、generator trace、output bytes、output hash、parent/child IDs 和终止原因。在相同容器、seed 与白名单输入下无法 byte-for-byte 重放时，该 trial 失效；若确需改 grammar 或引入新事实源，必须使旧 binding 及全部下游对象失效，重新执行 `T−5 bind → T−4 purpose → T−3 generate → T−2 commit`，并在新 hash 之后才可运行 hidden evaluator。

### 6.4 B/S/G 边界

- `B_state` 只指 trusted mediator 绑定的部署可见 pre-state，可由 generator 和 public sandbox 读取。
- `S_state` 只可由 canonical proposed action 在授权 sandbox 中执行得到，且必须记录 action/state hash；它可成为真实部署可取得的 action-derived evidence。
- `G_state`、gold patch、hidden tests 和 sealed evaluator output 对 generator、branch instantiator、policy、renderer、participant 全部禁用。它们只能在 lattice/branch commitment hash 之后由 evaluator 计算训练标签或最终 outcome。
- gold/G/hidden 不得生成 proposition、候选 test、mask、ordering、cost、timeout、latency feature 或 missingness pattern。

## 7. 文件、hash 与 lineage manifest

| 文件名 | 内容 | SHA-256 状态 |
| --- | --- | --- |
| `trial_binding_manifest.jsonl` | canonical action bytes/hash、repo/container、pre-state、permission、scope 与覆盖全部字段的 `binding_digest` | `PENDING-IMPLEMENTATION` |
| `proposition_manifest.jsonl` | proposition、`J_content`、source、annotator、agreement 与唯一 upstream `binding_digest` | `PENDING-IMPLEMENTATION` |
| `criterion_manifest.jsonl` | `m_req/κ`、scale/basis/bank hash/unit/sensitivity grid、冻结时点、作者、裁决与 `binding_digest` | `PENDING-IMPLEMENTATION` |
| `measurement_item_bank_manifest.jsonl` | 四个 bank 的 item bytes/source/answer、direct/transfer pairing、截取顺序、显示 seed 与 `binding_digest` | `PENDING-IMPLEMENTATION` |
| `criterion_measurement_manifest.jsonl` | `M_obs` 的 item/time/normalized-Brier aggregation/missingness/`R_post`；与 `κ` 分 producer 与 lineage | `PENDING-IMPLEMENTATION` |
| `candidate_lattice_manifest.jsonl` | 完整 static action grammar、每 class cap 8、eligible/discarded IDs、candidate bytes/hash、mask、cost、timeout、ordering | `PENDING-IMPLEMENTATION` |
| `branch_commitment_manifest.jsonl` | branch grammar、template/slot、instantiator、runtime whitelist、fact-source root、parent/hash rule、budget/termination | `PENDING-IMPLEMENTATION` |
| `branch_merkle_manifest.jsonl` | 预枚举 instance hashes 或 template/source/replay Merkle root、seed 与 branch instance lineage | `PENDING-IMPLEMENTATION` |
| `candidate_cap_policy_manifest.yaml` | `CandidateSetFn-v4/Cap8Fn-v4` hash、candidate-ID 公式、coverage/cost/hash rank、cap 8、执行时点与 retained/discarded schema | `PENDING-IMPLEMENTATION` |
| `q_policy_manifest.yaml` | `q-policy-v1` checkpoint/schema/dtype/temperature/mask/softmax、input/logit/normalizer/sum-to-one 容差与 forbidden inputs | `PENDING-IMPLEMENTATION` |
| `generator_visibility_whitelist.json` | generator 可读字段白名单 | `PENDING-IMPLEMENTATION` |
| `container_image_manifest.json` | generator/public-sandbox/evaluator/logger/trainer image digest | `PENDING-IMPLEMENTATION` |
| `oracle_access_log.jsonl` | 所有 hidden/G/gold 访问主体、时间和目的 | `PENDING-IMPLEMENTATION` |
| `interaction_log.jsonl` | `S_t^pre`、单列 `A_t`、class/candidate eligible set 与 propensity、人类互动、`R_post` 和 public execution | `PENDING-IMPLEMENTATION` |
| `label_manifest.parquet` | 标签来源、时点、可见性、标注者、UNKNOWN、裁决 | `PENDING-IMPLEMENTATION` |
| `split_group_manifest.parquet` | participant/repo/commit/bug/risk/test/gold lineage split | `PENDING-IMPLEMENTATION` |
| `arm_randomization_protocol.yaml` | domain、`seed_hash`、HMAC input canonicalization、salt/ID 规则、字节序、`0→A,1→B,2→C,3→D` 映射、allocator/schema hash、key 公开与重放规则 | `PENDING-IMPLEMENTATION`；首例入组前 `seed_hash` 必须改为真实 64 位 hex |
| `participant_arm_assignment_manifest.jsonl` | `participant_id`、分层、HMAC digest/`u_i/j_i`、固定 `A/B/C/D` arm、12-trial persistence receipt、override/deviation | `PENDING-IMPLEMENTATION` |
| `confirmatory_cluster_likelihood_manifest.yaml` | IID `O_i`、participant-product likelihood、12-trial/8-slot factorization、carryover history、跨 participant no-interference、cluster target population/weights | `PENDING-IMPLEMENTATION` |
| `logging_propensity_manifest.parquet` | 每步 treatment-free state、cap 后集合、两级 propensity、opportunity、participant-cluster weight/ESS 与 support disposition | `PENDING-IMPLEMENTATION` |
| `data_lineage_manifest.parquet` | 原始记录到 tensor/checkpoint 的 lineage | `PENDING-IMPLEMENTATION` |
| `noninterference_mirror_manifest.jsonl` | 成对 public-equivalent mirror、交换 hidden bytes、候选/trace/logit 结果 | `PENDING-IMPLEMENTATION` |
| `leakage_probe_report.json` | public baseline hash、equivalence group、conditional incremental probe、diagnosis/disposition | `PENDING-IMPLEMENTATION` |
| `sample_support_simulation.json` | simulation grid、最小 cohort/trial/ESS 输出 | `PENDING-IMPLEMENTATION` |
| `same_reviewer_outcome_manifest.jsonl` | interaction participant、final approver、canonical action identity、participant decision、expert truth | `PENDING-IMPLEMENTATION` |
| `mediation_estimand_manifest.yaml` | D-vs-C participant treatment、fixed `T_dec=6/T_max=8`、12-trial 联合 `Z^J/G_a^{J,1:r}`、`IIE_JFG^cl`、participant-equal target、absorbing no-op、item bank、过程内 `R_post`、`C_Y`、`ASSOCIATION_ONLY` 与 `MECHANISM_NOT_ESTIMABLE` | `PENDING-IMPLEMENTATION` |
| `mediation_analysis_manifest.yaml` | participant-fold seed、participant-product one-step HAL-EIC likelihood、12-trial carryover、处理前 support、probability truncation、ratio clipping、2,000 次分层整 participant-cluster bootstrap、bootstrap seed/hash/percentile interval/failure-rate 规则、repo sensitivities 与 failure codes | `PENDING-IMPLEMENTATION` |
| `micro_randomized_manifest.yaml` | 独立 cohort/split、eligibility、`p=0.5`、最大次数、washout、treatment/control bytes、evidence 等质 hash、compliance receipts、micro-item lineage、proximal ITT/GEE 与 exploratory outcomes | `PENDING-IMPLEMENTATION` |
| `direct_neighbor_coverage_manifest.md` | 六篇 2025–2026 主文的版本、实际读取入口、input/state/action/outcome 占位与不得外推边界 | `PENDING-IMPLEMENTATION` |
| `seed_and_config_manifest.yaml` | 随机种子、参数、FLOPs、搜索预算、冻结层 | `PENDING-IMPLEMENTATION` |

所有 JSONL/Parquet 行必须包含 schema version、created-at、producer image digest 与 upstream hashes。任何 hash 仍为 `PENDING-IMPLEMENTATION` 时，只能表明设计已写出，不能声称实现已通过。

## 8. Split group 与 cohort 隔离

划分的不可拆分 group key 为：

`participant_group × repository × base_commit × issue_bug_family × risk_family × generated_test_lineage × gold_derived_sibling × evidence_lattice_family`。

任何一个维度存在 sibling 关系都必须同组。confirmatory split 同时要求 participant、repository 和至少一个 risk family 对 training 完全未见；风险类型的文字别名不构成未见。confirmatory response、threshold tuning、界面改动和 calibration update 均被 access-control 阻止。

三个真人阶段的规划下限和角色如下。

| 阶段 | 保守规划下限 | 可否训练 | 主要责任 |
| --- | ---: | --- | --- |
| measurement/support pilot | 48 人 × 8–12 trials | 否 | 标签可靠性、误解路径、动作合法率、simulation 参数 |
| policy-learning logging | 180 人 × 16 trials，至少 2,880 trials | 是 | 已知两级 propensity 轨迹、`F_cg/T_ev/π_cg` 训练 |
| prospective confirmatory | 180 人 × 12 个计划 trials，至少 2,160 trials | 否 | participant-level 固定四臂的冻结模型主要与次级结果；一人 12 trial 同臂 |

这些下限不是最终样本量。`sample_support_simulation.json` 必须在招募前遍历 baseline unsafe rate、8 个百分点目标差异、participant/task ICC、五类 risk outcome、三档 reviewer support、六类顶层动作及 subtype、grounding phase、budget bucket、class/candidate availability、每 class cap 8、`ε_cls=0.30`、`ε_cand=0.40`、`clarify/repair` 触发与可达率、absorbing `stop`、3–6 步轨迹、15% attrition 和 missingness，并使用第 9 节唯一 participant-cluster Kish ESS。最终 N 取同时满足功效与支持门的最小值；若模拟要求更大则扩容，不能把下限当结果。

### 8.1 Confirmatory 固定四臂与可重放分配

`randomization_unit=participant_id`，`randomization_strata=baseline_reviewer_support`，并使用已冻结的 `low/medium/high` 三层。四臂编号唯一为 `A/B/C/D`，每层中的设计概率都为 `1/4`；D/C 确认性对比的条件 propensity 唯一为 `P(D|D∨C,H)=P(C|D∨C,H)=1/2`。`arm_persistence=all_12_planned_trials`，任何 trial-level randomization、crossover、缺席后重分配或人工 override 都不属于本设计。十二个任务和顺序属性的 hash 在 allocator 调用前冻结，后续缺席只改 missingness/deviation 字段。

HMAC 域字符串固定为 `C3-CONF-ARM-20260816-v1`。首例入组前，安全服务生成 256-bit `K_arm`，只公布 `seed_hash=SHA256(K_arm)`，不公开 key；真实入组不得在 `seed_hash` 仍为 `PENDING-IMPLEMENTATION` 或不是 64 位十六进制值时开始。令 `m_i=UTF8(domain || stratum_i || salted_participant_id_i)`，`||` 按 `arm_randomization_protocol.yaml` 中的长度边界、分隔、Unicode 规范化与字符编码唯一实现。计算

`h_i=HMAC-SHA256(K_arm,m_i)`，`u_i=UInt64BE(h_i[0:8])`，`j_i=floor(4u_i/2^64)`，

并以 `0→A,1→B,2→C,3→D` 生成唯一 assignment。`arm_randomization_protocol.yaml` 在首例入组前冻结 salt 与 salted-ID 规则、normalization、编码、字节序、四臂映射、allocator executable SHA-256 和 schema SHA-256。`participant_arm_assignment_manifest.jsonl` 每人只有一条 assignment，并将该 assignment 外键复制到十二个计划 trial；同一 participant 出现多个臂值时整个 cluster 记 `ARM_PERSISTENCE_FAIL`，不得选择性保留其中 trial。`K_arm` 在 enrollment lock 后公开，两个独立实现必须由公开 key 重放出同一 HMAC、`u_i`、`j_i` 和 arm；key/hash 不符、映射不符或人工改臂记 protocol deviation，不得重抽 key 或重分配。

## 9. Logging support、ESS 与 same-reviewer outcome 门

### 9.1 Eligibility-conditioned support

处理前状态唯一写为

`S_t^pre=(risk_stratum,baseline_reviewer_support,grounding_phase_pre,budget_pre,class_availability_bitmask,eligible_action_set_hash,public_history_hash)`。

所有字段在当前动作抽样之前落盘。`eligible_action_set_hash` 覆盖按 ID 排序的 `candidate_id/class/subtype/mask_reason/cost/timeout`；`public_history_hash` 只覆盖截至 `t−1` 的公开互动与动作。当前 selected `top_action_class`、`action_subtype`、`candidate_id`、当前动作后的 repair/clarification trigger、response 与 outcome 均不得进入 `S_t^pre` 或其 signature。当前处理另存为 `A_t=(class_t,subtype_t,candidate_id_t)`。

T−2 冻结 `CandidateSetFn-v4`、`Cap8Fn-v4` 与 `q-policy-v1`，并登记 executable/checkpoint SHA-256、schema version、dtype、temperature=`1.0`、mask/normalizer/tie rule。T−2 只冻结函数对象与静态候选；它不伪称知道未来 visible response 对应的实例，也不预填未来状态的数值概率。

每个 opportunity 的唯一执行顺序是 `instantiate-all → hash → public-only cap → persist retained/discarded → build S_t^pre → evaluate q → mix propensity → sample A_t`。动态 instance 只能由 T−2 grammar、template/slot、source Merkle root、image、seed 与截至 `t−1` 的 visible response/`UNKNOWN`/clarification request/public execution 决定性生成。candidate ID 固定为

`candidate_content_hash=SHA256(instantiated_bytes)`；`candidate_id=SHA256(CBORcanonical([binding_digest,parent_state_hash,action_class,template_id,slot_bytes,instantiated_bytes,generator_version]))`。canonical CBOR array encoder、字段类型和 schema hash 在 T−2 写入 manifest；不得用无长度边界的字符串拼接。

`Cap8Fn-v4` 在每个 class 内按三元组 `(-proposition_coverage_count, expected_public_cost_millis, candidate_content_hash)` 升序保留前 8 个，`stop` 只保留一个；coverage 只按 `J_content` proposition ID 去重计数，cost 只读 T−2 public profiler version，hash 按小写十六进制字典序。所有实例 bytes/hash、三项 rank value、retained/discarded IDs、cap reason 与函数版本在 `S_t^pre` 前落盘。截断后空 class 不进入 `class_availability_bitmask`。所有基线读取完全相同的 retained set。

logging propensity 是唯一两级 mixture。对非空合法 class 集 `C_t`，

`p_cls(c|S_t^pre)=0.70 q_cls(c|S_t^pre)+0.30/|C_t|`。

在抽中 class `c` 后，对 `K_t(c)`，

`p_cand(k|c,S_t^pre)=0.60 q_cand(k|c,S_t^pre)+0.40/|K_t(c)|`。

`q-policy-v1` 是 T−2 冻结的条件分布生成函数，不是 T−2 已知的数值分布。它只读取 cap 后 `S_t^pre`、retained candidate bytes/features 与合法 mask，分别对 class logits 和选中 class 内 candidate logits做 float64、temperature=`1.0` 的 stable softmax；tie 只影响日志排序，不改变概率。它看不到 discarded candidates，不能向 generator/cap 回传信号。每个 opportunity 保存 checkpoint/hash、input hash、logits、normalizer、全部 `q_cls/q_cand` 数值和 sum-to-one 结果；绝对误差大于 `1e-8`、NaN/Inf、版本不符或在 masked item 上分配正概率即 trial 失效，不使用结果后 fallback。联合 propensity 为 `p(A_t|S_t^pre)=p_cls×p_cand`。class-level 下界是 `0.30/|C_t|`，within-class 下界是 `0.40/|K_t(c)|`；exact-candidate support 只按 cap 后的条件下界报告，不另设与集合规模无关的固定概率门。

primary contrast 位于顶层 class。`estimand_cell_id` 固定为

`φ(S_t^pre)×A_t.class = risk_stratum×baseline_reviewer_support×grounding_phase_pre×budget_bucket_pre×class_availability_pattern×A_t.class`。

exact set hash 留在 propensity 与 replay signature 中，不进入会导致一 trial 一 cell 的支持 coarsening。subtype/candidate 只有在预注册 family 跨 trial 重复并独立通过同一门时才能作次级 contrast。一个 eligible opportunity 是 `S_t^pre`、完整合法集合和 propensity denominator 已写入，但 `A_t` 尚未抽取的决策时点；结构不合法 class 永远不构成 opportunity。

ESS 只使用 participant 为唯一 cluster。对 participant `i`、cell `h` 与 class `c`，定义

`w_it(h,c)=I{φ(S_it^pre)=h,A_it.class=c}/p_cls(c|S_it^pre)`，

`W_i(h,c)=Σ_t w_it(h,c)`，

`ESS_Kish(h,c)=(Σ_i W_i(h,c))^2/Σ_i W_i(h,c)^2`。

class-wide 检查只定义 `W_i(c)=Σ_hW_i(h,c)`，再以同一个公式计算 `ESS_Kish(c)=(Σ_iW_i(c))^2/Σ_iW_i(c)^2`。若分母为 0，相应 cell 或 class 直接 unsupported。不得对 decision rows 直接计算 ESS，不得改用 task/repository cluster、multiway cluster 或三种 ESS 取最小值。task 与 repository只进入 mixed-model/random-effect 方差和预注册敏感性，不改变支持门。policy-learning logging cohort 的序列 OPE 使用逐时点 class×candidate 联合 propensity 构造 inverse-propensity prefix weight，仍先在 participant 内聚合，再用同一 Kish 公式；它不是第 11 节的 joint-process density ratio `ρ_s`，也不进入 `IIE_JFG^cl` clever covariate。

| 门 | 唯一预注册规则 | 失败处置 |
| --- | --- | --- |
| treatment-free state | `eligibility_state_signature` 可由 `S_t^pre` 重放，且不含 selected action/subtype/candidate 或 post-action trigger | trial 失效并重建日志 |
| legal denominator | `C_t/K_t(c)` 只含结构合法且 cap 后保留的候选；保存 eligible 与 discarded IDs/mask reasons | 分母不一致则 trial 失效 |
| class positivity | 每个 eligible class 满足 `p_cls≥0.30/card(C_t)` | 重做 logging policy；不得估计该 class |
| within-class positivity | 每个 cap 后 candidate 满足 `p_cand≥0.40/card(K_t(c))` | 重做候选 cap 或 logging policy |
| structural illegality | 不合法 class/candidate 不要求 positivity、support 或 ESS | 只能使用预注册 deterministic fallback，不作反事实外推 |
| primary-cell opportunity | 每个 `h×c` 的 eligible opportunities `≥80` | 扩容或标为 unsupported |
| primary-cell selection | selected decision rows `≥40` 且 selected participant clusters `≥30` | 扩容或标为 unsupported |
| primary-cell ESS | participant-cluster `ESS_Kish(h,c)≥30` | 扩容；不得离线外推 |
| class-wide support | 每个顶层 class 的 selected participant clusters `≥80` 且跨 cell `ESS_Kish≥60` | 扩容或删除该 class 的主要主张 |
| logging-OPE weight cap | inverse logging-propensity prefix weight 主 cap `10`；报告 cap 5/10/20 与不 cap 敏感性；不得套用于 `ρ_s` | 超过 5% logging opportunity 被 cap 或 OPE 方向改变则 support failure |
| independent replay | 两个独立脚本在同一 synthetic log 上得到相同 set hash、denominator、propensity、cell、cluster count 与 ESS | 不一致则不得训练主策略 |

support failure 不能通过模型外推、simulated reviewer、改 cluster 定义或合并事后有利的风险层解决。任何 coarsening 或阈值变化必须在 outcome 解封前预注册并同步全部方法。

### 9.2 Same-reviewer primary outcome

primary unsafe approval 的行级硬校验为 `interaction_participant_id == evidence_recipient_id == final_approver_id`，且 `canonical_decision_action_hash == canonical_action_hash`。该审核者必须完成 C3 交互、接收 action-bound evidence 与中介测量，然后对同一 canonical action 作最终决定。外部 gate 只记录或执行这一决定；不得根据 C3 trajectory 换人、加 second reviewer 或重新路由后仍归入 primary estimand。

专家 adjudicator 只根据 sealed hidden tests/state-delta oracle 确定当前 action 的 safe/unsafe 真值，不能代替 participant 的 approval/deny 结果。identity 不一致或组织流程引入 secondary reviewer 的 trial 只能进入与 C19 边界相符的预注册次级分析，不得回填 primary outcome。

## 10. Oracle noninterference 与条件增量诊断

### 10.1 成对 mirror 机械非干扰门

在主模型训练与 outcome 解封前，为每个受试 group 构造成对 `public_input_equivalence_group`。两个 mirror 的 issue/task、canonical action、B/pre-state、public tests、authorized tools、全部部署可见 risk signals、budget、visible response/history 与 public execution bytes 必须完全相同；只交换 sealed G/hidden-oracle bytes 及其 label store pointer。非干扰比较覆盖：

- generator/instantiator input digest、candidate IDs、candidate bytes/hash、branch instance/root、ordering、mask/reason、cost、timeout/latency feature、provenance 和 generator trace。
- 冻结 checkpoint 的 action logits、eligible logits order 和 selected-action distribution。在确定性 kernel 上要求数值逐位一致；硬件无法逐位复现时，必须事前登记 dtype/kernel 与严格绝对误差上限 `1e-7`，同时要求所有 candidate bytes/order/mask 逐字节一致。
- evaluator absent、evaluator present-but-sealed 与 hidden-byte-swapped 三种条件下的 access log、file/network syscall trace 与 branch replay trace。

任一 candidate/branch bytes、ID、order、mask、cost、latency feature、trace 或 action-logit 超过预注册数值容差，都是 mechanical noninterference failure，对应 group 及其 binding 下游全部失效，并需在修复后重新执行 `T−5 bind → T−4 purpose → T−3 generate → T−2 commit`。这一门不依赖 AUC、label 可预测性或效果方向。

### 10.2 条件增量 probe

另行报告 hidden-only 标识是否能在合法 public 信息之外预测 availability/mask/ordering/cost/timeout/public latency/missingness 的统计诊断。先用完整 public covariates、public-risk strata、visible history/state 和 action scope 建立各 availability field 的冻结基线，再在同一 equivalence group 中增加 hidden-only ID/label-store pointer，比较增量预测力；二元 field 报告 raw/delta AUC 和 AUPRC，连续/多类 field 报告 conditional log-loss/deviance 与 calibration delta。报告字段为 `public_covariate_baseline_hash/equivalence_group_key/raw_auc/delta_auc/conditional_log_loss_delta/calibration_delta/paired_permutation_result`。

合法 public risk signal 可预测真实风险是部署信息的正常作用，不得被原始 AUC 高误判为 oracle leakage。只有在 public-risk strata 和可见状态条件化后，hidden-only 标识仍对 availability 产生无法由 public lineage 解释的增量，才触发访问日志与 generator 源码调查。条件 probe 是敏感性诊断，不是设计通过的唯一证据；机械非干扰通过也不允许隐藏诊断异常。

## 11. 纵向联合取证—grounding 机制 estimand 与识别合同

### 11.1 唯一固定时间轴与联合过程 schema

| 节点 | 冻结定义 |
| --- | --- |
| `X̄_i=(B_i,X_i1,…,X_i12)` | `B_i` 是参与者基线；`X_ir` 在 arm randomization 前唯一冻结 `baseline_reviewer_support,baseline_factual_accuracy_bin,repository_stratum,task_stratum,risk_stratum,task_complexity_bin,canonical_action_type,canonical_scope_bin,public_risk_bin,initial_budget_bin,trial_order_block`。十二 trial 任务/顺序、分箱、UNKNOWN 类与 hash 均不得分析后改变 |
| `A_i` | 唯一 randomization unit 为 `participant_id`；四臂每层概率 `1/4`，参与者的 12 个计划 trial 全部保持该臂。D-vs-C 中 `A_i=1` 为冻结 C3，`A_i=0` 为等信息、等动作、等资源 Human-state POMDP，条件 propensity 均为 `1/2` |
| `Z_ir,t^J,t=1,…,6` | 参与者 `i` 的第 `r` 个 trial 每槽严格按 `D_t→U_t→E_t→F_t→C_t^g→K_t`：动作前 eligibility/phase/budget；所选 class/subtype/candidate family；public execution/evidence exposure；factual response；clarification/repair/grounding-acceptance/uptake；增量 latency/compute/fatigue proxy/stop |
| `Z_ir,7^J` | `M_valid` 与 action-specific `M_obs_bin`；continuous `M_obs` 另存校准值，不作另一 estimand |
| `Z_ir,8^J` | measurement 后安全请求与实际 evidence/repair 的 `R_post` family、exposure/receipt 和完成状态；不进行第二次 `M_obs` 覆盖 |
| `C_{Y,ir}` | participant 真实退出、日志损坏或 final decision 缺失；`R_post` 不属于 censoring |
| `Y_ir` | 同一审核者在统一 measurement regime 下对同一 canonical action 作出的 unsafe approval；专家只产生 sealed truth |
| `O_i` | IID 参与者 cluster：`O_i=(B_i,A_i,{X_ir,Z_ir^J,C_{Y,ir},Y_ir}_{r=1}^{12})`；总 likelihood 以 `i` 为乘积单位 |

固定 `T_dec=6`、`T_max=8`。在第 `s≤6` 槽选择 `stop` 后，`s+1,…,6` 的 `active=0`，所有 action/exposure/response/repair event code 为 `NOOP_ABSORB`，增量 cost/latency 为 0，剩余 budget 与最后 phase carry forward；这些值既非 UNKNOWN 也非 missing。第 7 与第 8 槽仍按安全协议执行。`g_est`、approval、harm、gold/G/hidden outcome 都不能生成任何 `Z^J` 节点。首名 confirmatory participant 进入后，`X̄/Z^J` schema、节点顺序和 version hash 不得改变；若发现未登记的 treatment 后、decision 前变量同时影响后续 process 与 `Y`，固定记 `PROCESS_SCHEMA_OMISSION`，当前样本停止因果机制报告，只能由新版本和新样本重建 estimand，不得临时另建 `L` 或扩写 `Z^J`。

总体 likelihood 唯一为 `L(P)=∏_{i=1}^n p(O_i)`，禁止以 2,160 个 trial 的 IID 乘积代替。`p(O_i)` 内部按 `r=1,…,12` 顺序展开，每个 trial 再按八槽展开。第 `r` 个 trial 的 nuisance history 包含 `B_i`、固定 `A_i`、冻结的 `X_i1:12`、该参与者所有早期 trial 的 `Z^J`、measurement、`R_post`、censoring、可见决策与可见结局历史，但不得读取当时尚封存的 hidden safe/unsafe 真值。参与者内学习、疲劳、信任调整和 repair carryover 是这一 cluster history 的允许组成；唯一 no-interference 假设仅针对不同 participant cluster 之间。

### 11.2 Item bank、联合随机干预与唯一 estimand

`measurement_item_bank_manifest` 在 `binding_digest`、`J_content/m_req/κ` 之后且 arm randomization 之前冻结。每个 required proposition 配一项 direct 与一项不同措辞 transfer item；总数为 4–8，超出时按 proposition ID hash 固定截取。每项保存 `item_bytes/item_id/proposition_id/direct_or_transfer/correct_category/source_fact_hash/response_probability_schema/display_order_seed`。全部臂使用相同 bytes、顺序、时间窗与 silent/no-feedback 界面。

审核者为每题提交类别概率。令 `b_j` 为冻结的 normalized multiclass Brier loss，`M_obs=1-|I_req|^{-1}Σ_jb_j`。primary process node 使用十个固定区间 `[0,.1),…,[.8,.9),[.9,1]`；少于 4 个有效 item 编为 `MISSING_MEASUREMENT`，不填 0。continuous value、bin、valid item count 和 missing reason 同时写入 manifest。measurement 会改变思考的可能性属于统一制度，故 `Y_ir` 只解释为该制度下的第 `r` 个 trial 结果。

令第 `r` 个 trial 开始前的 cluster history 为 `H_ir^cl=(X̄_i,Z_i,1:r-1^J,C_Y,i,1:r-1,可见决策与可见结局历史)`。当前 trial 的 arm-specific sequential law 为

`G_a^J(dz_ir^J|H_ir^cl)=∏_{t=1}^6∏_{v∈(D,U,E,F,Cg,K)}g_{a,r,t,v}(dz_{ir,t,v}|H_ir^cl,z_{ir,<t,v}^J)·g_{a,r,7}(dz_{ir,7}|H_ir^cl,z_{ir,1:6}^J)·g_{a,r,8}(dz_{ir,8}|H_ir^cl,z_{ir,1:7}^J)`。

从第一个 trial 到第 `r` 个 trial 的分布记为 `G_a^{J,1:r}(dz^J_{1:r}|X̄_i)`，并按 `r=1,…,12` 继续因子化。这里的 conditioning history 只含处理前 `X̄_i` 与此前由同一 stochastic intervention 抽出的簇内 process prefix；不含实际 arm 下另存的 acquisition、presentation、clarification/repair history，也不读 hidden unsafe truth。

确认性 D/C 目标总体固定为处理前合格且被随机分入 D 或 C 的参与者，先应用第 11.4 节在解封 `Y` 前冻结的 shared-support 规则，然后每名参与者等权、每人十二个计划 trial 等权。令 `μ_r(a,z^J_{1:r},X̄_i)=E[Y_ir|A_i=a,Z_i,1:r^J=z^J_{1:r},X̄_i,C_{Y,ir}=0]`，定义

`Ψ_J^cl(a,a*)=E_{X̄_i}[12^{-1}Σ_{r=1}^{12}∫μ_r(a,z^J_{1:r},X̄_i)G_{a*}^{J,1:r}(dz^J_{1:r}|X̄_i)]`，

`IIE_JFG^cl=Ψ_J^cl(1,0)-Ψ_J^cl(1,1)`。

正值表示在 C3 outcome arm 下，将十二 trial 簇内完整 joint process 从 Human-state POMDP 分布换成 C3 分布所减少的参与者平均 unsafe approval。`z^J_{1:r}` 包含当前与早期 trial 的全部八槽历史；缺失由 `C_Y` 处理，不得 complete-case 删除后改变参与者权重。policy total effect 另报；natural、organic、history-conditional mediator shift、single-`M_obs` effect、神经 `g_est` mediation 与 analyst-chosen shift 全部非法。[Wang et al. (2025), DOI 10.1515/jci-2023-0013](https://doi.org/10.1515/jci-2023-0013) 只为随机干预、likelihood factorization、HAL-EIC 与 general longitudinal stochastic-intervention estimator 提供方法依据；participant-level 固定臂、簇目标与 bootstrap 是本研究的预注册实施选择。

### 11.3 唯一 estimator、fold、概率与 density ratio

primary estimator 只能是 simultaneously targeting `Ψ_J^cl(1,0)` 与 `Ψ_J^cl(1,1)` 的 one-step HAL-EIC longitudinal TMLE。nuisance likelihood 是第 11.1 节 `∏_i p(O_i)` 中的 participant-product likelihood；每个 `p(O_i)` 在簇内序贯建模十二 trial 和每 trial 八槽，允许 carryover。outer cross-fitting 只按 participant 分五折，seed 固定为 `C3-JFG-CF-20260816-v1`。在 `baseline_reviewer_support` 各层内以 `SHA256(UTF8(seed)||0x00||UTF8(salted_participant_id))` 升序排列，层内 rank `j` 分到 `fold=1+((j-1) mod 5)`；各 support 层 participant 数跨折之差至多 1，同一 participant 的全部十二 trial 与所有 row 只能进入同一 fold。fold seed、participant-to-fold 清单、清单 SHA-256 和 nuisance 配置 SHA-256 在读取确认性 `Y` 前冻结。participant–repository connected-component folds 明确作废。每个 outer training fold 内，binary/categorical process factors、censoring 与 outcome 使用二阶交互 HAL likelihood；连续 process factors 使用同一二阶基与 sectional-variation bound 的 HAL conditional-density estimator。bound 仅由 seed 派生的三折 participant inner-CV negative log-likelihood 决定，tie 取较小 bound。D/C 已知 arm propensity 使用条件随机化常数 `1/2`。任何另一 TMLE、g-formula、IPW 或事后 stacking 不得替换 primary。

二元 nuisance probability 先截断到 `[0.01,0.99]`。`K` 类 probability vector 只能用 `p_j^tr=0.98p_j+0.02/K` 保持和为 1。density ratio 与 probability 是不同对象。对任一 joint-process prefix `s`，保存未裁剪

`ρ_s=∏_{u≤s}g_{a*,u}(Z_u|X̄,Z^J_{<u})/g_{a,u}(Z_u|X̄,Z^J_{<u})`，

并在 clever covariate 中唯一使用 `ρ_s^clip=exp{clip(logρ_s,-log20,log20)}∈[1/20,20]`；ratio 可以且通常会大于 1，不得截到 0.99。可评价 prefix 指截至 `s` 的全部字段均为实测值或预注册结构码且尚未进入 `C_Y`。对 arm `a`、outer fold `k`，定义 `clip_rate_{a,k}=Σ_{i,r,s}I(A_i=a,fold_i=k,prefix_{irs}可评价,|logρ_{irs}|>log20)/Σ_{i,r,s}I(A_i=a,fold_i=k,prefix_{irs}可评价)`。分母为 0、任一 `clip_rate_{a,k}>0.05`、出现非有限 ratio，或未裁剪/裁剪 `IIE_JFG^cl` 的符号不同即设 `RATIO_SUPPORT_FAIL`，不尝试其他 cap。

区间固定为 2,000 次 participant-cluster bootstrap。每个 replicate 在 `arm×baseline_reviewer_support` 层内有放回抽取完整 participant cluster，保留 cluster multiplicity 和其十二 trial 全部记录。bootstrap 域字符串固定为 `C3-JFG-BOOT-20260816-v1`，实际 seed 与 SHA-256 在读取确认性 `Y` 前写入 manifest。每个 replicate 必须完整重拟 nuisance、重做 cross-fit 预测和 targeting，不得仅对终端 trial 行重抽；95% 区间唯一为 percentile interval。失败 replicate 不重抽、不补抽；非有限值、截断/ratio 门违反或 pipeline 失败均计入失败率，失败率超过 5% 固定输出 `MECHANISM_NOT_ESTIMABLE`，不切换区间方法。repository 不参与 primary fold 或替代 participant resampling。repository 依赖另报 participant×repository two-way influence-curve variance。repository OOD seed 为 `C3-JFG-REPO-OOD-20260816-v1`，组号是 `1+(UInt64BE(SHA256(UTF8(seed)||0x00||UTF8(repository_id))[0:8]) mod 5)`；每次其余组训练 nuisance，目标组 participant 若出现在训练组则整体移除。它只作外部敏感性，不能替换 primary。

### 11.4 处理前 common support、结构空 cell 与降级

对 trial `r` 与 participant `i`，处理前 common-support key 唯一为 `H_ir=(risk_stratum_ir,baseline_reviewer_support_i)`，只读取 arm assignment 前字段。定义 `N^P_{a,h}=Σ_i I{∃r:A_i=a,H_ir=h}`、`N^T_{a,h}=Σ_{i,r}I{A_i=a,H_ir=h}` 与 `S_h^count=I{min_aN^P_{a,h}≥20 ∧ min_aN^T_{a,h}≥30}`。另定义 `B_h=1` 当且仅当 T−2 state machine 在 cell `h` 中存在 reference process 可达的 public prefix/category，而 outcome arm 在同一 prefix 将该 category 结构性 mask；它只读 grammar、mask、family code 与 public state，不读 `q`、response outcome、approval 或 `Y`。唯一最终指标为 `S_h=S_h^count(1-B_h)`。在 sealed `Y` 解封前，`S_h^count=0` 记 `BASELINE_UNSUPPORTED`，`B_h=1` 记 `ASYMMETRIC_STRUCTURAL_ZERO`，两者都移出 shared-support population。没有 `S_h=1` cell 时固定记 `MECHANISM_NOT_ESTIMABLE`。否则 `P_sup^cl` 固定为 D/C 两臂 shared-support 参与者的合并经验分布，每人等权且每人内十二个计划 trial 等权。定义 `r_a^cl=n_a^{-1}Σ_{i:A_i=a}[12^{-1}Σ_rS_{H_ir}]`；任一 `r_a^cl<0.80`、任一 risk stratum 在任一臂没有 `S_h=1` trial，或存在任一 `B_h=1` 时，`IIE_JFG^cl` 固定降为 association-only。若支持规则排除了处理前 strata，解释边界必须写为该 shared-support 参与者总体。

冻结 public mask 在同一 history 下判为不合法的 action/category 是 structural zero，其 `G_a^J` probability 固定为 0，不要求 positivity，也不进入 denominator。不得以 Laplace smoothing、probability floor、合并 outcome 后有利 cell 或删除单个不利 row 伪造支持。所有 `S_h^count/B_h/S_h`、structural-zero 和 ratio disposition 必须早于 `Y` 解封。

因果表达要求 participant-level treatment randomization、policy/action/measurement version consistency、给定 `X̄_i` 与同一参与者既往 `Z^J` 的 sequential process–outcome exchangeability、baseline 与 sequential overlap、仅跨 participant cluster no-interference 以及 `C_Y` 可识别。参与者内 12-trial carryover 必须进入 likelihood history，不能被无干扰假设删去。识别假设、80%/stratum support、asymmetric structural zero、ratio clipping-rate 或任一 arm `C_Y≤5%` 门失败，但 cross-fitted HAL initial likelihood 仍有限且可重放时，固定记 `ASSOCIATION_ONLY`，跳过因果 targeting，只用同一 `P_sup^cl` 计算 `SA_J^cl=E_{P_sup^cl}[12^{-1}Σ_r∫μ̂_r(1,z^J_{1:r},X̄){Ĝ_0^{J,1:r}-Ĝ_1^{J,1:r}}(dz^J_{1:r}|X̄)]`，命名为 `standardized joint-process association`，并按第 11.3 节作 2,000 次整 participant-cluster bootstrap。HAL/conditional-density nonconvergence、任一 outer fold `Y=1<10`、nonfinite ratio/EIC、`PROCESS_SCHEMA_OMISSION`、bootstrap 失败率超过 5%，或两个独立实现不能逐字段重放 `Z^J`、fold、ratio、target 与 TMLE 时，固定记 `MECHANISM_NOT_ESTIMABLE`，不报告机制数字。两类失败均仍可报告随机 policy total effect；不得使用“中介”“间接效应”或“机制被证实”。

micro-randomized encouragement 只在不复用 D-vs-C primary participant/trial 的 `micro_secondary` cohort 运行。在 `repair` 合法、技术 evidence bytes 固定、有未展示 `micro_transfer_item`、同 trial 尚未 encouragement 且 active encouragement 后已 washout 一 trial时，以已知 `p=0.5` 最多随机一次。treatment/control bytes、receipt/exposure compliance、participant-cluster GEE proximal ITT 与探索性 distal outcome沿用冻结合同；micro item 不进入 `Z_7`，该随机化不改变 `G_a^{J,1:r}`、`IIE_JFG^cl` 或 primary TMLE。

## 12. 最新直接近邻的主文核验与字段边界

本表只登记截至 2026 年 8 月 16 日实际取得并阅读的 arXiv 主文版本。正式写作不得从标题或摘要扩张字段，也不得再使用已变更的旧题名 “HAI-Eval” 指称 arXiv:2512.04111。

| 主文与读取入口 | 输入/参与者 | 状态与动作 | 结果 | 对 C3 的硬边界 |
| --- | --- | --- | --- | --- |
| [CentaurEval v3](https://arxiv.org/html/2512.04111) | 45 templates、450 tasks、45 participants、5 LLMs | 人或 agent 单独/协作完成 coding tasks，4 种 intervention conditions | pass、partial pass、time、tokens 与协作分析 | 无 fixed escalation、same-action unsafe truth、evidence acquisition 或 factual-grounding mediator |
| [RECODE-H v2](https://arxiv.org/pdf/2510.06186) | 102 research-code tasks；主文 PDF 29 页已读 | ReCodeAgent 在最多 10 轮中消费由 GPT-o4-mini 结合 canonical code/tests 生成的五级反馈 | MRR、Recall、test pass 与 code similarity | simulated expert feedback 可接触 canonical implementation，不是真人批准或 oracle-blind grounding |
| [PULSE v3](https://arxiv.org/html/2510.09801) | OpenHands 上约 15,000 名真实用户与 in-the-wild trajectories | A/B 变更 LLM、planning 或 memory design；模型预测 user satisfaction | satisfaction effect 与 prediction-powered CI | 真人结果已被占据，但 outcome 不是 unsafe approval，state 不是 action-specific factual grounding |
| [Human-AI Synergy in Agentic Code Review v1](https://arxiv.org/html/2603.15911) | 300 projects、278,790 inline conversations | human/agent reviewer feedback、互动序列与 suggestion adoption | adoption、rounds、code metrics | 观察性对话无 sealed truth、随机 repair 或 fixed canonical approval |
| [From Human-Centric to Agentic Code Review v1](https://arxiv.org/html/2607.13196) | 207 projects、1.02 million reviewed PRs | 三个 review eras 与 human/LLM/agent interaction sequences | review efficiency 与 quality association | 主文明示 explanatory not causal；无 action binding、中介测量或 unsafe approval |
| [RepoComplianceBench v1](https://arxiv.org/html/2607.26819) | 49 repositories、106 issues、四类 written rules | agent refuse/disclose/verify/handoff 及 steering/feedback | rule compliance | run 在 agent reply 结束，maintainer interaction 未观察；handoff 不是 fixed-post-escalation 同人审核 |

因此，`direct_neighbor_coverage_manifest.md` 必须把 C3 的联合交集限定为 `fixed post-escalation → immutable action binding → oracle-blind executable evidence/grounding policy → same human final approval → sealed state-damage truth → observable acquisition–presentation–clarification/repair–factual-grounding joint process`。任何一篇新工作若占据该全交集，设计需重新送审。

## 13. 等信息基线与容量 manifest

Human-state POMDP、Raw-POMDP、generic proposition Transformer 与 contextual bandit 必须获得同一 `J_content`、所有 proposition labels、factual/phase/uptake human feedback、静态 candidate lattice、T−2 动态 branch/replay contract 及完全相同的实例 bytes、action mask、external reward 和 logging propensity。它们使用同一 pretrained `E_tech`、split、training steps、seed count 和搜索配置数。

理论模型与每个学习型基线按可训练参数正负 1%、推断 FLOPs 正负 5% 和 wall-clock budget 匹配。结构损失的标签也向等容量通用多任务头开放；C3 只能通过结构使用方式不同。通用模型在表达能力上可复制 C3，理论贡献只在有限数据、OOD、方向干预和安全—效率前沿未被复制时成立。

容量 manifest 必须逐项记录 `00H` 规定的上限：`E_tech` 人类阶段可训练部分不超过 15M，`F_cg≤10M`、`T_ev≤12M`、`π_cg≤5M`，后三者均最多两层且状态维不超过 192。匹配以全部人类阶段可训练参数为口径，不能只比较 policy head。

## 14. 实施前机械门

- [ ] 所有角色 image digest 不再是 `PENDING-IMPLEMENTATION`。
- [ ] `trial_binding_manifest/binding_digest` 先于 `J_content/m_req/κ` 与四个 bank，且所有下游 upstream digest 相同。
- [ ] `J_content/m_req/κ` 与 item bank 的 created-at 早于 arm assignment、response、approval 和 hidden access。
- [ ] `baseline_reviewer_support`、每人 12 个计划任务及顺序在分臂前落盘；`randomization_unit=participant_id`、四臂每层 `1/4`、D/C 条件概率 `1/2` 与 `arm_persistence=all_12_planned_trials` 逐行一致，无 trial-level randomization/crossover/重分配。
- [ ] `C3-CONF-ARM-20260816-v1`、真实 `seed_hash`、salt/normalization/encoding/字节序、HMAC input、`UInt64BE`、`floor(4u/2^64)`、`0→A,1→B,2→C,3→D`、allocator/schema hash 在首例入组前冻结；enrollment lock 后公开 `K_arm`，两个独立实现重放的 HMAC/arm 完全一致，无人工 override。
- [ ] action/pre-state/working-tree/permission/scope swap 会机械失效 proposition、criterion、bank、lattice、branch、evidence 和全部理论状态，并重放 bind→purpose→generate→commit。
- [ ] `κ` 的 scale/basis/bank hash/unit/sensitivity grid 齐全，且与 `criterion_measurement_t` 的 producer/lineage 分离。
- [ ] lattice hash 与动态 branch commitment/Merkle root 早于任何 logging、response、approval 及 evaluator 首次 access log。
- [ ] 有限枚举或参数 grammar 在相同可见输入下可 byte-for-byte 重放，且全部基线共用该分支合同。
- [ ] paired hidden-byte mirror 的 candidate IDs/bytes/order/mask/cost/latency/trace/action logits 通过机械非干扰门。
- [ ] B/S/G 可见性单元测试通过。
- [ ] 三个 primary cohort 无 participant/repo lineage 重叠，`micro_secondary` 也不复用其 participant/trial。
- [ ] `S_t^pre` 不含 selected action/subtype/candidate 或 post-action trigger；`A_t` 单列且两个实现得到相同 signature。
- [ ] `CandidateSetFn-v4/Cap8Fn-v4/q-policy-v1` 的 hash/schema/dtype/temperature/mask/normalizer/tie rule 已在 T−2 冻结；每个机会严格重放 `instantiate-all → candidate hash → public-only class cap 8 → retained/discarded 落盘 → S_t^pre → q → 两级抽样`，且 `q` 无法读取 discarded set 或影响实例化、排序、cap；`0.30/|C_t|` class positivity 与 `0.40/|K_t(c)|` within-class positivity 均通过。
- [ ] 每个主要 cell 的 opportunity、selected rows、selected participant clusters 与唯一 participant-cluster Kish ESS 通过；没有 decision-row/task/repo ESS 替代，结构不合法 cell 未外推。
- [ ] conditional incremental probe 已在 public-risk/visible-state 条件下报告，没有用裸 AUC 把合法 public signal 判为泄漏。
- [ ] primary outcome 通过 same-reviewer 与 same-canonical-action 硬校验，expert adjudicator 只产生 hidden 真值。
- [ ] `measurement_item_bank_manifest` 的 direct/transfer pairing、4–8 item、bytes/order、normalized Brier、silent/no-feedback 与 missing rule 在 arm assignment 前冻结。
- [ ] IID 单位唯一为 `O_i`，likelihood 唯一为 `∏_i p(O_i)`，簇内按 12 trial×8 槽并纳入学习/疲劳/repair carryover；no-interference 仅限跨 participant，无 trial-IID likelihood 或“跨 trial 无干扰”残留。
- [ ] 唯一 `IIE_JFG^cl=Ψ_J^cl(1,0)-Ψ_J^cl(1,1)`、12-trial joint-process kernels `G_0^{J,1:r}/G_1^{J,1:r}`、participant-equal 且簇内 trial-equal 目标总体、六个决策槽加 measurement/`R_post` 两个终端槽、stop 后 absorbing no-op、participant-level 五折 one-step HAL-EIC longitudinal TMLE、`ASSOCIATION_ONLY` plug-in 与 `MECHANISM_NOT_ESTIMABLE` 两级失败处置在 outcome 前冻结；participant–repository connected-component folds、替代 primary estimator 与事后阈值选择均不存在。
- [ ] 2,000 次 bootstrap 在 `arm×baseline_reviewer_support` 层内抽完整 participant cluster，保留 multiplicity、全量重拟 nuisance/cross-fit/target、使用预提交 seed/hash 与 percentile interval；失败 replicate 不补抽，失败率 `>5%` 输出 `MECHANISM_NOT_ESTIMABLE`。
- [ ] 二元/多类 nuisance probability 稳定化与可大于 1 的 prefix density ratio 已分别按 `[0.01,0.99]`、`0.98p+0.02/K` 和 `[1/20,20]` 合同实现；任一 arm/fold 的 ratio clipping 比例超过 5%、ratio 非有限或裁剪改变估计方向时停止因果机制报告。
- [ ] 处理前 common-support 只以 `risk_stratum×baseline_reviewer_support` 计算；D/C 每 cell 的 `participant_clusters≥20` 且 `trials≥30`、participant-equal 80% retained 门、risk-stratum 存续门、结构空 cell 与 `ASYMMETRIC_STRUCTURAL_ZERO` 处置均在 sealed `Y` 解封前生成，并在失败时固定降为 association-only；排除 strata 后的目标总体明示为 shared-support participants。
- [ ] micro-randomized encouragement 只在独立 `micro_secondary` cohort 作 `p=0.5`、每 trial 最多一次、active 后一 trial washout 的次级机制实验；technical evidence bytes 相同，receipt/exposure compliance、assignment-based proximal ITT 与 participant-cluster GEE 已冻结，micro item 不进入 `M_obs`。
- [ ] 六篇最新直接近邻的主文版本和字段边界写入 coverage manifest；arXiv:2512.04111 使用 CentaurEval 当前题名。
- [ ] confirmatory runner 没有训练写权限。
- [ ] `C.grounding_acceptance` 与 gate approval 分离，`M[:,2]` 三个 event/receipt/item ID 齐全，C/M 无同一 response 循环定义。
- [ ] 所有理论标签无 approval/harm/task-success lineage，UNKNOWN 含 time/annotator/reason/forbidden-source check。
- [ ] 所有 baseline 的字段、参数、FLOPs、搜索预算与种子匹配。

当前以上复选项均未执行，不得勾选。本文件因此保持 **REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN**。
