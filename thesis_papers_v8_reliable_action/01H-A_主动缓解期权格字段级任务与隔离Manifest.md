# 主动缓解期权格字段级任务与隔离 Manifest

> 文档版本：`MOL-FIELD/0.6-REPAIRED-v5`
> 研究状态：**REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN**
> 适用候选：`MOL-RC/1.5-REPAIRED-v5`
> Builder与app接口：`MigrateOptionLab-v1.3`、`MigrateOpt-Apps-v1.2`
> 修补依据：`01Y`、`02D`、`02L`保留前三轮链路，`02R_主动缓解期权格第四轮修补后独立冻结审计.md`提供本次absolute-time hazard、duration-cell条件积分与固定数值算法的直接缺口。
> 结果边界：本文没有建立 repository、生成 snapshot、运行 migration episode、训练模型或取得实验结果。下列 source、image、snapshot、trace、checker、oracle、template、split 与 runtime hash 均为 `PENDING-IMPLEMENTATION`。

## 1. 本文件的责任和七道设计门

本文件把 app family、字段变换、checker/oracle 隔离、风险注入、operator observation、CodeTwin、数据划分和runtime状态机写到实现前可检查的粒度。它与01H共同构成已修补但尚待独立再红队的契约；源码、容器、数据与自动检查仍为待实现对象。本文件不因写出字段而声称工件存在或设计已经冻结。

`01Y`基础门与`02D`二次审计要求重开的设计门在本文件中的责任如下。

| 门 | 本文件承担的责任 | 本文件结束时状态 |
|---|---|---|
| 1. 非同构 option-impact parameter tying | 为18 slots、observable global typed codec、executor/belief分离、双账、passage/direct causal closure与十项tensor/causal tests提供字段接口；计算图由01H冻结 | **REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN** |
| 2. 公平 `G-PhysicalFactoredSMDP` | 固定相同候选、动作、mask、labels、state、kernel、search、参数与FLOPs接口 | **REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN** |
| 3. 有效风险控制 | 冻结`VAL-CAL-POLICY`生成器字段、共同world和15项资格记录 | **REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN** |
| 4. CodeTwin-v1.2 泄漏隔离 | 冻结opaque candidate、policy-parameterized probe、t=0 hashes、No-Source denylist、primary/diagnostic边界与oracle mutation matrix | **REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN** |
| 5. `ENUM-IDENTIFY/TRAIN/TEST` 隔离 | 冻结三层、四代表slot selector、ID/seed/hash与partial-label边界 | **REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN** |
| 6. 字段级 task 与 manifests | 预指定18 app×4 migration、十三类实例文件、joint-kernel/dual-ledger与runtime状态机 | **REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN** |
| 7. benchmark推断单位 | 八个synthetic test app作为有限benchmark units，禁止总体外推 | **REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN** |

本文件不能单独改变候选状态；新的独立再红队仍须检查两文件是否真正闭合。

## 2. Benchmark 总体、独立性与计数

主总体计划包含18个synthetic repository families，每个family含四项migration motif，共72项field-level migration。划分为6个train app、4个validation app和8个test app，task数分别为24、16和32。CodeTwin-v1.2是附加反事实tier，不改变72项主任务计数；`A11–A18`是确认性primary，`A01–A10`只作diagnostic。这里的“family”是预注册构造单位；八个test families只支持该benchmark内的有限平均effect，不构成现实repository抽样框或OOD保证。

所有app可以共享一个只含typed workload、logging和reset protocol的versioned harness，但不得共享domain model、table declaration、business-policy function、transaction handler、checker implementation或hidden reference model。每个app必须具有独立source root、dependency lock、database role、schema namespace、endpoint namespace和transaction-family namespace。实现后排除generated scaffold、许可证、dependency vendor与harness import，计算三项冻结相似度：business-source token 5-gram set Jaccard `≤0.20`；tree-sitter typed AST subtree-multiset weighted Jaccard `≤0.30`；由`HTTP verb, endpoint-shape, tables-read, tables-written, transaction-boundary, retry/idempotency class`构成的transaction-template set Jaccard `≤0.25`。任一pair超阈值必须在任何outcome生成前重写或合并为一个推断unit；阈值只防止明显换名副本，不证明synthetic families来自独立现实总体。实际值仍为`PENDING-IMPLEMENTATION`。

| Split | App ID | 业务对象 | 计划中的核心外部不变量 |
|---|---|---|---|
| train | `A01-ledger` | account、entry、reversal | 每笔 entry 只 posting 一次；借贷符号和 reversal 链一致 |
| train | `A02-orders` | order、line、payment | line total、order total 与 payment 状态一致 |
| train | `A03-inventory` | stock、reservation、movement | reserved 不超过 on-hand；movement 守恒 |
| train | `A04-subscription` | plan、period、renewal | service period 为正且不重叠；status 与时间一致 |
| train | `A05-ticketing` | ticket、transition、assignee | transition 合法；关闭后普通 handler 不得再写 |
| train | `A06-catalog` | item、price、weight | 币种、质量单位和有效商品范围一致 |
| validation | `A07-fulfillment` | parcel、shipment、fulfillable line | shipped quantity 不超过 fulfillable quantity |
| validation | `A08-billing` | invoice、tax、credit、payment | 发票、税额、credit、payment 的金额恒等式成立 |
| validation | `A09-reservations` | resource、slot、booking | 容量不超售；同一 resource 的约束时段不非法重叠 |
| validation | `A10-entitlements` | principal、grant、scope、revocation | scope 唯一；撤销或到期后不得继续授权 |
| test | `A11-payroll` | worker、payrun、payitem | net=gross-tax-deduction；已支付 payrun 不得重算 |
| test | `A12-laboratory` | specimen、assay、result | specimen 状态单调；verified result 与 source assay 一致 |
| test | `A13-fleet` | vehicle、trip、operator、emission | trip 时段和里程非负；排放物化值与行程一致 |
| test | `A14-claims` | claim、coverage、reserve、settlement | settlement 不超过有效责任；reserve 与 paid 状态一致 |
| test | `A15-enrollment` | learner、course、enrollment、credit | seat capacity 不超限；earned credit 只来自 completed enrollment |
| test | `A16-metering` | device、reading、interval | interval end 不小于 start；consumption 与 meter delta 一致 |
| test | `A17-records` | document、retention、legal hold | legal hold 时不得处置；到期日由公开 retention policy 决定 |
| test | `A18-grants` | grant、milestone、disbursement | posted disbursement 不超过 award；关闭后不得新增付款 |

每个 app 的计划实现状态均为 `PENDING-IMPLEMENTATION`。表中的不变量是任务契约，不是已经通过的实验事实。

## 3. 四类 migration 的共同语义

### 3.1 `M1` replacement/rename

`M1` 的 forward expression 一律为 `new = old`，reverse expression 一律为 `old = new`。source 与 target 的 SQL type、长度、collation、nullability 和 default 必须相同。`NULL`、空字符串和前后空格按原字节保留，不作 trim、case-fold 或 Unicode normalization。compatible state 若出现 old/new 都非空而值不同，visible consistency checker 返回 `red`，migration operator 不自行选择一侧覆盖。该规则阻止把 rename 任务暗中改成 normalization 或 entity resolution。

### 3.2 `M2` unit/type conversion

每项 `M2` 把一个可见 `NUMERIC` 业务量转换为一个整数最小单位。记缩放后的实数为 `q`。CodeTwin 的两个可见政策为：

- `HALF_EVEN`：选择距离 `q` 最近的整数；精确 `.5` 时选择绝对值为偶数的整数。
- `HALF_UP`：选择距离 `q` 最近的整数；精确 `.5` 时向远离零的方向取整。

两种政策对非 tie 输入相同。输入为 `NULL` 时只有 source column 可空才保留 `NULL`；非有限值、缩放后超出 target integer 范围或违反表内非负约束时，new endpoint 返回 typed validation error，整个 transaction rollback。不得 silent clamp、silent zero-fill 或按数据库 session 的默认 rounding。主任务的公开政策为 `HALF_EVEN`；CodeTwin-v1.2 另生成 `HALF_UP` repository variant。CodeTwin共用的migration contract只写字面值`FROM_REPOSITORY_POLICY`，不写具体policy；精确值只存在于允许变化的visible source和policy不可见的sealed oracle manifest。

### 3.3 `M3` enum/default recoding

每项 `M3` 把 exact UTF-8 NFC string 映射到 `SMALLINT`。比较不 trim、不 case-fold；表中列出的字面值是唯一 known set。CodeTwin 的两个可见政策为：

- `REJECT_UNKNOWN`：unknown、空字符串或不合规 case 返回 typed `422`，transaction rollback。
- `MAP_OTHER`：相同输入写为代码 `99`，old-version reverse mapping 固定为字面值 `__other__`。

`NULL` 只按 column nullability 处理；本版本的 18 个 `M3` source column 均为 `NOT NULL`。主任务公开政策为 `REJECT_UNKNOWN`。default 只在字段缺省时使用，不能把显式 unknown 当成 default。known mapping与default code位于共用contract；CodeTwin的`unknown_policy`字段固定写`FROM_REPOSITORY_POLICY`，具体值只存在于visible policy source和sealed oracle manifest。hidden oracle独立重实现同一公开语义。

### 3.4 `M4` derived-field materialisation

`M4` 新增 ordinary stored column，并以 repeatable-read snapshot 执行 backfill；随后 old/new write path 必须双写 source fields 与 materialized field。它不是数据库 generated column。表内 expression、null policy、overflow policy和更新触发字段均属于公开 contract。visible checker 只抽样重算；hidden oracle 在 terminal snapshot 上对全量受影响行或全量 reference transaction 独立重算。任何算术 overflow、时间反转、缺失外键、循环 reversal 或违反表内 boundary 的记录均使 clean-path inclusion 失败，不能由 builder 自动修值。

## 4. 18 个 app × 4 个字段级 migration 契约

下表中的表达式是待实现源码必须遵守的候选语义。`R(x)` 表示第 3.2 节中 repository 可见的 rounding policy；主任务取 `HALF_EVEN`，CodeTwin 另取 `HALF_UP`。所有 target integer 运算先用 arbitrary-precision 中间值，再作范围检查，不允许 SQL integer overflow 后截断。

| App | `M1` old → new 与边界 | `M2` old → new 与精确变换 | `M3` old → new、mapping、default | `M4` materialized field 与精确表达式 |
|---|---|---|---|---|
| `A01-ledger` | `entries.memo VARCHAR(255) NULL` → `entries.description VARCHAR(255) NULL`；identity，NULL/空白原样保留 | `amount_major NUMERIC(18,4) NOT NULL` → `amount_minor BIGINT NOT NULL`；`R(amount_major*100)`；要求 `amount_major>=0` | `entry_kind VARCHAR(16) DEFAULT 'debit'` → `entry_kind_code SMALLINT DEFAULT 10`；`debit→10, credit→20, reversal→30` | `signed_minor BIGINT NOT NULL`；debit=`-amount_minor`，credit=`amount_minor`，reversal=`-signed_minor(reversal_of_id)`；原 entry 必须存在且 reversal graph 无环 |
| `A02-orders` | `order_lines.sku VARCHAR(64) NOT NULL` → `product_code VARCHAR(64) NOT NULL`；identity | `unit_price_major NUMERIC(14,4) NOT NULL` → `unit_price_minor BIGINT NOT NULL`；`R(unit_price_major*100)`；价格非负 | `order_state VARCHAR(20) DEFAULT 'draft'` → `order_state_code SMALLINT DEFAULT 10`；`draft→10, placed→20, paid→30, cancelled→40, refunded→50` | `line_total_minor BIGINT NOT NULL`；`unit_price_minor*quantity`；`quantity` 为 `[0,10^6]` 整数，overflow 拒绝 |
| `A03-inventory` | `reservations.warehouse_code VARCHAR(40) NOT NULL` → `location_code VARCHAR(40) NOT NULL`；identity | `movements.quantity_each NUMERIC(18,4) NOT NULL` → `quantity_milli BIGINT NOT NULL`；`R(quantity_each*1000)`；数量非负 | `movement_kind VARCHAR(16) DEFAULT 'receipt'` → `movement_kind_code SMALLINT DEFAULT 10`；`receipt→10, issue→20, reserve→30, release→40, adjustment→50` | `stock.available_milli BIGINT NOT NULL`；`on_hand_milli-reserved_milli`；两项均非负且结果不得小于零 |
| `A04-subscription` | `renewals.plan_slug VARCHAR(80) NOT NULL` → `plan_code VARCHAR(80) NOT NULL`；identity | `plans.monthly_price_major NUMERIC(14,4) NOT NULL` → `monthly_price_minor BIGINT NOT NULL`；`R(x*100)`；价格非负 | `subscription_state VARCHAR(16) DEFAULT 'trial'` → `subscription_state_code SMALLINT DEFAULT 10`；`trial→10, active→20, paused→30, cancelled→40, expired→50` | `period_seconds BIGINT NOT NULL`；`floor(extract(epoch from period_end_utc-period_start_utc))`；两端均 UTC、end 严格晚于 start、亚秒部分向零截断 |
| `A05-ticketing` | `tickets.owner_handle VARCHAR(80) NULL` → `assignee_handle VARCHAR(80) NULL`；identity | `tickets.sla_hours NUMERIC(10,5) NOT NULL` → `sla_seconds BIGINT NOT NULL`；`R(sla_hours*3600)`；范围 `[0,87600]` 小时 | `ticket_state VARCHAR(20) DEFAULT 'open'` → `ticket_state_code SMALLINT DEFAULT 10`；`open→10, in_progress→20, resolved→30, closed→40` | `resolution_seconds BIGINT NULL`；resolved/closed 时为 `floor(resolved_at_utc-created_at_utc)`，其他状态为 NULL；负差拒绝 |
| `A06-catalog` | `items.external_sku VARCHAR(96) NOT NULL` → `merchant_item_code VARCHAR(96) NOT NULL`；identity | `items.weight_kg NUMERIC(18,7) NOT NULL` → `weight_mg BIGINT NOT NULL`；`R(weight_kg*1000000)`；重量非负 | `item_condition VARCHAR(20) DEFAULT 'new'` → `item_condition_code SMALLINT DEFAULT 10`；`new→10, used→20, refurbished→30` | `price_per_kg_milliminor BIGINT NULL`；weight 为零则 NULL，否则 `R(price_minor*10^9/weight_mg)`；price 非负，overflow 拒绝 |
| `A07-fulfillment` | `shipments.tracking_no VARCHAR(96) NULL` → `carrier_tracking_code VARCHAR(96) NULL`；identity | `shipment_lines.shipped_quantity NUMERIC(18,4) NOT NULL` → `shipped_milli BIGINT NOT NULL`；`R(x*1000)`；数量非负 | `shipment_state VARCHAR(20) DEFAULT 'packed'` → `shipment_state_code SMALLINT DEFAULT 10`；`packed→10, dispatched→20, delivered→30, returned→40` | `remaining_milli BIGINT NOT NULL`；`fulfillable_milli-shipped_milli`；结果小于零则 transaction rollback |
| `A08-billing` | `invoices.customer_ref VARCHAR(72) NOT NULL` → `billing_account_code VARCHAR(72) NOT NULL`；identity | `invoice_lines.tax_rate_pct NUMERIC(9,6) NOT NULL` → `tax_rate_ppm INTEGER NOT NULL`；`R(tax_rate_pct*10000)`；百分比范围 `[0,100]` | `invoice_state VARCHAR(20) DEFAULT 'draft'` → `invoice_state_code SMALLINT DEFAULT 10`；`draft→10, issued→20, part_paid→30, paid→40, void→50` | `net_due_minor BIGINT NOT NULL`；`total_minor-paid_minor-credit_minor`；允许负值表示 overpayment，但三项必须同币种且 overflow 拒绝 |
| `A09-reservations` | `bookings.resource_ref VARCHAR(72) NOT NULL` → `resource_code VARCHAR(72) NOT NULL`；identity | `bookings.duration_hours NUMERIC(12,6) NOT NULL` → `duration_seconds BIGINT NOT NULL`；`R(duration_hours*3600)`；必须大于零 | `booking_state VARCHAR(20) DEFAULT 'tentative'` → `booking_state_code SMALLINT DEFAULT 10`；`tentative→10, confirmed→20, checked_in→30, cancelled→40, no_show→50` | `end_at_utc TIMESTAMPTZ NOT NULL`；`start_at_utc + duration_seconds*interval '1 second'`；timestamp overflow 或非正 duration 拒绝 |
| `A10-entitlements` | `grants.subject_ref VARCHAR(128) NOT NULL` → `principal_ref VARCHAR(128) NOT NULL`；identity | `grants.quota_gb NUMERIC(18,6) NOT NULL` → `quota_bytes BIGINT NOT NULL`；`R(quota_gb*1000000000)`；使用 decimal GB，quota 非负 | `scope_name VARCHAR(16) DEFAULT 'view'` → `scope_code SMALLINT DEFAULT 10`；`view→10, edit→20, admin→30, owner→40` | `effective_until_utc TIMESTAMPTZ NULL`；取 expires_at 与 revoked_at 中较早者，NULL 视为 `+∞`，二者均 NULL 时结果 NULL |
| `A11-payroll` | `workers.payroll_ref VARCHAR(64) NOT NULL` → `worker_code VARCHAR(64) NOT NULL`；identity | `payitems.hourly_rate_major NUMERIC(14,4) NOT NULL` → `hourly_rate_minor BIGINT NOT NULL`；`R(x*100)`；rate 非负 | `payrun_state VARCHAR(20) DEFAULT 'draft'` → `payrun_state_code SMALLINT DEFAULT 10`；`draft→10, calculated→20, approved→30, paid→40, void→50` | `net_minor BIGINT NOT NULL`；`gross_minor-tax_minor-deduction_minor`；结果不得小于零；paid 后 source fields 不可再写 |
| `A12-laboratory` | `specimens.accession_no VARCHAR(80) NOT NULL` → `accession_code VARCHAR(80) NOT NULL`；identity | `specimens.sample_volume_ml NUMERIC(14,6) NOT NULL` → `sample_volume_ul BIGINT NOT NULL`；`R(x*1000)`；volume 必须大于零 | `specimen_state VARCHAR(20) DEFAULT 'collected'` → `specimen_state_code SMALLINT DEFAULT 10`；`collected→10, received→20, processing→30, verified→40, rejected→50` | `turnaround_seconds BIGINT NULL`；verified 时为 `floor(verified_at_utc-received_at_utc)`，其他状态 NULL；负差拒绝 |
| `A13-fleet` | `trips.driver_ref VARCHAR(72) NULL` → `operator_code VARCHAR(72) NULL`；identity | `trips.distance_km NUMERIC(16,6) NOT NULL` → `distance_meters BIGINT NOT NULL`；`R(x*1000)`；distance 非负 | `trip_state VARCHAR(16) DEFAULT 'planned'` → `trip_state_code SMALLINT DEFAULT 10`；`planned→10, active→20, completed→30, cancelled→40` | `emission_grams BIGINT NULL`；factor 缺失则 NULL，否则 `R(distance_meters*emission_g_per_km/1000)`；factor 与 distance 均非负 |
| `A14-claims` | `claims.policy_ref VARCHAR(80) NOT NULL` → `coverage_code VARCHAR(80) NOT NULL`；identity | `claims.reserve_major NUMERIC(18,4) NOT NULL` → `reserve_minor BIGINT NOT NULL`；`R(x*100)`；reserve 非负 | `claim_state VARCHAR(20) DEFAULT 'opened'` → `claim_state_code SMALLINT DEFAULT 10`；`opened→10, in_review→20, accepted→30, denied→40, settled→50` | `outstanding_minor BIGINT NOT NULL`；`reserve_minor-paid_minor`；结果不得小于零，settled 时必须为零 |
| `A15-enrollment` | `enrollments.student_ref VARCHAR(72) NOT NULL` → `learner_code VARCHAR(72) NOT NULL`；identity | `courses.credit_units NUMERIC(8,4) NOT NULL` → `credit_milli INTEGER NOT NULL`；`R(x*1000)`；范围 `[0,100]` | `enrollment_state VARCHAR(20) DEFAULT 'waitlisted'` → `enrollment_state_code SMALLINT DEFAULT 10`；`waitlisted→10, enrolled→20, completed→30, withdrawn→40, failed→50` | `earned_credit_milli INTEGER NOT NULL`；state=completed 时等于 credit_milli，否则为零；state 或 credit 更新均须重算 |
| `A16-metering` | `intervals.meter_ref VARCHAR(80) NOT NULL` → `device_code VARCHAR(80) NOT NULL`；identity | `intervals.energy_kwh NUMERIC(20,6) NOT NULL` → `energy_wh BIGINT NOT NULL`；`R(x*1000)`；energy 非负 | `reading_quality VARCHAR(16) DEFAULT 'actual'` → `reading_quality_code SMALLINT DEFAULT 10`；`actual→10, estimated→20, corrected→30, missing→40` | `consumption_wh BIGINT NOT NULL`；`end_register_wh-start_register_wh`；register 不得为负且 end 不得小于 start |
| `A17-records` | `documents.owner_ref VARCHAR(96) NOT NULL` → `custodian_code VARCHAR(96) NOT NULL`；identity | `retention_rules.retention_months NUMERIC(10,4) NOT NULL` → `retention_days INTEGER NOT NULL`；`R(retention_months*487/16)`；days 非负 | `classification VARCHAR(20) DEFAULT 'internal'` → `classification_code SMALLINT DEFAULT 20`；`public→10, internal→20, confidential→30, restricted→40` | `disposal_due_date DATE NULL`；legal_hold=true 时 NULL，否则 `created_date+retention_days`；date overflow 拒绝，hold 变化须重算 |
| `A18-grants` | `grants.program_ref VARCHAR(80) NOT NULL` → `funding_program_code VARCHAR(80) NOT NULL`；identity | `grants.award_major NUMERIC(18,4) NOT NULL` → `award_minor BIGINT NOT NULL`；`R(x*100)`；award 非负 | `grant_state VARCHAR(20) DEFAULT 'proposed'` → `grant_state_code SMALLINT DEFAULT 10`；`proposed→10, awarded→20, active→30, suspended→40, closed→50` | `undisbursed_minor BIGINT NOT NULL`；`award_minor-SUM(posted disbursement_minor)`，空集 sum=0；结果不得小于零，closed 后不可更新 |

每一格最终须实例化为一个独立的 `migration_contracts/<app>-<M1..M4>.yaml`。在任一格实现失败、字段语义需要改变或 clean path 不能成立时，必须生成新的 draft 版本并重新审计，不能只改源码 hash。

## 5. Visible checker 与 hidden oracle 的结构性分离

### 5.1 目录、进程与信息边界

计划目录必须满足下列单向关系。

```text
apps/<app>/old/                    # policy 可见
apps/<app>/new/                    # policy 可见
visible_checkers/<app>/<set>/      # policy 可见；只读 compatible DB
hidden_oracles/<app>/              # policy 不可见；独立 build context
fixtures/public/<app>/             # checker 可读
fixtures/hidden/<app>/             # 仅 oracle/workload runner 可读
```

visible checker image 不得包含 `hidden_oracles/`、hidden fixture、risk injection truth、future raw transaction 或 terminal reference state。hidden oracle image 不得 import visible checker source，也不得根据 method ID、chosen model、训练 seed 或论文假设改变判定。operator runner 只把 checker 的三值 observation 与允许的连续统计返回 policy；hidden oracle 只在 terminal 或预定义标准化 probe 写入 evaluation log，绝不进入 agent history。

### 5.2 八个 twin-invariant visible checker candidate sets

每个 app 计划提供八个互不重叠的 checker set，固定顺序为 `CS00` 至 `CS07`。每个 set 恰含 16 个 atomic checker，ID 为 `<app>-CSxx-C00..C15`，共 128 个 visible checkers。不同 twin 使用完全相同的 set ID、原子成员、source bytes、fixture bytes、ordering 和 action mask。

| Set | 16 个 atomic checker 的共同责任 | 明确不承担的责任 |
|---|---|---|
| `CS00-contract-shape` | old/new column、type、null/default、collation、version schema、write propagation 的结构检查；16 个 slot 对应 four motifs×four contract dimensions | 不读取业务 hidden input，不判断 active rounding/unknown policy |
| `CS01-old-endpoint` | old endpoint 的 create/read/update/retry 四类 transaction，各按 nominal/zero/null-or-omitted/max-public 四个公开 fixture 分区 | 不读取 new policy file，不访问 future workload |
| `CS02-new-endpoint` | new endpoint 的同一 4×4 公开 fixture 分区 | 不使用 hidden oracle expected output |
| `CS03-M1-identity` | NULL、empty、whitespace、Unicode NFC、min/max length、duplicate、retry、old-client、new-client 等 16 个公开 identity case | 不做 trim/case-fold，不覆盖 M2–M4 hidden boundary |
| `CS04-M2-policy-probe` | 16个twin-invariant raw probes覆盖positive/negative tie、near-tie、zero、range edge、retry和old/new read；每个probe在执行时通过稳定公开接口`new.policies.m2_rounding.expected_from_public_policy(raw)`计算expected，再与compatible DB结果比较 | checker source/ID/fixture不含`HALF_EVEN/HALF_UP` expected常量；不读取hidden oracle或future input |
| `CS05-M3-policy-probe` | 16个twin-invariant raw probes覆盖unknown、empty、case variant、whitespace、known/default、retry和old/new read；执行时通过`new.policies.m3_unknown.expected_from_public_policy(raw,presence_bit)`计算expected | checker source/ID/fixture不含`REJECT_UNKNOWN/MAP_OTHER` expected常量；不读取hidden oracle或future input |
| `CS06-M4-materialisation` | nominal、NULL branch、zero、boundary、source update、backfill row、concurrent write、retry 等 16 个公开重算 checker | 不作全表扫描，不读取 hidden terminal transaction |
| `CS07-cross-invariant` | 16 个 app-specific public invariant checker，覆盖 create/update/retry、old/new client、transaction rollback 和一组公开 concurrency schedule | 不等于 hidden full-population oracle，不访问 injection ID |

`CS04/CS05`的probe code、raw fixture bytes、candidate ID和membership在twins内逐字节相同；唯一动态依赖是同一路径下行动前已公开的repository policy function。probe只把该public policy当规范输入，不访问hidden oracle。任一set的16个probes因此对当前repository只有一个可执行expected policy，不再把互斥expected constants放进同一set。其价值是检验migration state是否符合公开政策，不是给模型泄漏variant label。`No-Source+TwinInvariantCandidates`只看opaque set ID与相同mask，不能从candidate元数据推断政策；它可以在实际执行probe后取得合法observation，这是研究中的付费信息行动。

### 5.3 四类 hidden oracle

| Motif | hidden oracle 的独立判定 | 与 visible checker 的非重合边界 |
|---|---|---|
| `M1` | 对 terminal snapshot 全量比较 old/new replacement value、双向传播、legacy/new client transaction 和幂等 retry；任一不相等计 semantic violation | 不调用 `CS03`，使用独立 reference transaction generator 和独立 SQL/read model |
| `M2` | 从raw decimal input和sealed manifest policy constant独立实现integer truth；覆盖hidden ties、负/零/上界输入及repeated transaction | 不import public policy或`CS04` source；raw input sequence在twins间相同 |
| `M3` | 从raw UTF-8 input、sealed known map/default-presence与manifest policy constant独立实现commit/rollback/code | 不import public policy或`CS05` source；unknown raw strings在twins间相同 |
| `M4` | 在 terminal repeatable-read snapshot 上全量重算 expression，并重放 hidden source-field update、retry和并发 transaction；比较所有受影响行 | 不调用 `CS06`，不接受 visible sample pass 代替全量 reference result |

四类 oracle 共同输出原始的 `success`、`data_corruption`、`semantic_violation`、`availability_loss`、`recovery_failure`、RPO、RTO、SLO area 和业务 cost。terminal semantic violation只在封存的`Ω_v(world_id,oracle_version)`上评价。`Ω_v`的reference transaction IDs、weight、denominator与oracle版本在任何policy rollout前固定，同一world的EX、AB、不同checker覆盖和不同method必须逐字节相同；未执行的reference transaction仍由sealed terminal oracle在相同terminal snapshot rule下评价，不能因某policy少做检查、较早停止或选择AB而从分母移除。它们不输出模型推荐、不参与训练标签选择，也不把 method 间差异变成 oracle 阈值。

### 5.4 Checker语义、oracle mutation与clean/injected矩阵

`CS04/CS05`的“同source bytes、不同当前repository行为”必须由固定接口实现，而不能把两个政策的expected写进fixture。每个probe只提交raw input与presence/retry metadata；sandbox在执行时导入当前repository的公开`expected_from_public_policy`，得到一个typed expected，再调用同一endpoint并比较commit/rollback、status code与stored/read value。checker log保存`raw_probe_hash,public_callable_hash,actual_hash,comparison_result`，不保存policy label。构建期AST检查拒绝`HALF_EVEN/HALF_UP/REJECT_UNKNOWN/MAP_OTHER`常量、sealed oracle import和variant-specific branch；运行期双variant source/image/checker hashes必须相同。

CodeTwin的M2/M3 oracle资格矩阵在任何model episode之前运行，`ACT`使用同一封存activation raw bytes，`NONACT`使用两政策结果相同的bytes。表中“应当”是property-test判据，当前执行状态均为`PENDING-IMPLEMENTATION`。

| Matrix ID | Visible repository policy | Sealed oracle policy | Raw bytes | 预注册checker/oracle判据 | 用途 |
|---|---|---|---|---|---|
| `CT-CLEAN-A` | `HALF_EVEN`或`REJECT_UNKNOWN` | 同左 | `ACT+NONACT` | public checker与independent oracle均接受匹配结果 | variant A clean inclusion |
| `CT-CLEAN-B` | `HALF_UP`或`MAP_OTHER` | 同左 | 与A逐字节相同 | public checker与independent oracle均接受匹配结果 | variant B clean inclusion |
| `CT-SOURCE-SWAP` | 改为另一政策 | 保持原sealed政策 | 同一`ACT` | public checker随当前source接受；hidden oracle必须报reference mismatch | source-sensitivity mutation；不是真实正确性结果 |
| `CT-ORACLE-SWAP` | 保持原政策 | sealed常量改为另一政策 | 同一`ACT` | public checker保持原判断；hidden oracle必须报reference mismatch | 证明oracle不是import repository policy |
| `CT-DOUBLE-SWAP` | 改为另一政策 | 同步改为另一sealed政策 | 同一`ACT+NONACT` | 两者重新一致；除两个允许变项外hash不变 | 对称clean控制 |
| `CT-NONACT-SWAP` | 任一 | 相反sealed政策 | 仅`NONACT` | 两政策语义相同时不得伪造mismatch | mutation specificity |
| `CT-CHECKER-CONST` | 任一 | 匹配 | 任一 | 在执行前因AST denylist或checker-byte invariant失败 | 拒绝双expected泄漏 |
| `CT-ORACLE-IMPORT` | 任一 | 任一 | 任一 | hidden image build因repository/visible-checker import denylist失败 | 拒绝循环oracle |

每个`app×motif×risk-template`另有clean/injected资格矩阵。`CLEAN+NO-ACT`与`CLEAN+ACT`都必须满足direct legal target path及hidden invariant；`INJECTED+NO-ACT`必须与clean在当前窗口外等值；`INJECTED+ACT`必须只在manifest声明的physical channel产生可检测差异；`INJECTED+REPAIR`必须允许预注册operator真实纠正或控制该差异，却不能删去已发生component。四格的snapshot、trace、seed、oracle与唯一patch hash均记录，任一格失败则整项task在生成训练label前排除并公开原因。该矩阵验证任务构造，不产生任何模型性能结果。

## 6. Replay candidate universe 与 CodeTwin-v1.2

### 6.1 八个 twin-invariant replay scopes

每个 app 的 replay universe 计划固定为八个 scope，顺序不能由 analyzer 或模型改变。每个 scope 的 256 条 trace 从同一个 public replay pool 以 manifest 中的 transaction ID 选择；不足时不重复采样，而使该 task 在实现检查中失败。

| Order | Scope ID | 256 条 trace 的组成 |
|---:|---|---|
| 0 | `RS00-create` | create/initial posting transaction，按 64 nominal、64 boundary-public、64 duplicate-key、64 retry |
| 1 | `RS01-update` | source-field update，按 old/new client×first/retry 各 64 |
| 2 | `RS02-read-projection` | detail/list/aggregate/read-after-write 各 64 |
| 3 | `RS03-background` | batch、scheduler、webhook/outbox、maintenance handler 各 64 |
| 4 | `RS04-idempotency` | duplicate request、timeout retry、out-of-order retry、same-key concurrency 各 64 |
| 5 | `RS05-version-mix` | old-only、new-only、old→new、new→old client sequence 各 64 |
| 6 | `RS06-public-boundary` | zero/empty-or-omitted、public tie/unknown、min/max public domain 各 64 |
| 7 | `RS07-stratified-full` | 前七组按 transaction family 等额分层后，由 manifest seed 选出的 256 条不重复 trace |

static analyzer 可以把 source/function/query nodes 与八个既存 scopes 建边，但不得删除、增加、重命名或重排 scope。若 analyzer 读取 code，它计入 full coding-agent 工件；`SchemaTelemetryOnly` 不获得 analyzer-derived edge，`No-Source+TwinInvariantCandidates` 获得八个 opaque scope slot 及相同 action mask。

行动层级固定为四个operator types映射到十八个mitigation slots：`SR→RS00..RS07`、`SV→CS00..CS07`、`CP→CP`、`WC→WC`。主policy与`π_cov`直接在十八slots上行动；任一slot开始执行后，其type的全部slots从episode mask移除。只有ENUM auxiliary tier先用outcome-blind stable-hash selector各选一个RS/CS代表，再与CP/WC组成四slot comparison set；selector不能冒充主policy或full oracle。

### 6.2 Twin 的唯一可变项

每个 app 的 `M2` 计划生成一组 `HALF_EVEN/HALF_UP` twins，`M3` 计划生成一组 `REJECT_UNKNOWN/MAP_OTHER` twins，共 36 个 twin groups 和 72 个 variant instances。每组必须满足：

1. 相同 `database_snapshot_hash`、database rows、sequence values 和 sequence IDs。
2. 相同 future raw transaction bytes、transaction order、absolute timestamps、workload/fault seed、exercise-relative draw 和 retry schedule。
3. 相同 migration schema diff、字节相同且政策字段为`FROM_REPOSITORY_POLICY`的migration contract、pgroll plan、old repository、dependency lock、container base、public fixtures和 visible checker source。
4. 相同 replay universe、八个 scope 的 ordering、八个 checker set 的 ordering、每个 atomic member 和 `A_mask`。
5. `M2` twins 只允许 `new/policies/m2_rounding.py` 的 `ROUND_MODE` 与对应实现分支不同；`M3` twins 只允许 `new/policies/m3_unknown.py` 的 `UNKNOWN_POLICY` 与对应实现分支不同。除这一公开政策文件和由它决定的 new repository hash 外，其余 new source bytes 必须相同。
6. hidden oracle 在同一 raw input 上分别应用可见的 variant policy；不能通过替换 workload distribution 制造差异。
7. policy input 不含 `twin_group_id`、`variant_id`、oracle policy label 或 variant-specific candidate/mask bit。episode audit log 可以保存这些字段，但 input serializer 必须证明已删除。

行动前的非代码视图还必须逐字节等值。每对twins在`t=0`记录并比较`schema_diff_hash/migration_contract_hash`、database snapshot、raw public fixture、candidate/order/mask、operator contract、`X_0` telemetry prefix、空`P_0`、typed persistent `R_0`、`t_0/τ_0`、protocol precondition、old/new smoke output和所有tool-result nodes；用于主CodeTwin的precutover prefix不得包含会触发M2 tie或M3 unknown政策差异的transaction。上述字段合并为`t0_noncode_view_hash`并要求相同。唯一允许不同的是明确属于Full-Code channel的`new/policies/*.py`内容及其code-derived nodes。

`No-Source+TwinInvariantCandidates`的denylist冻结为：所有repository bytes/token、source path content、AST、call graph、code-query lineage、analyzer score/rank/coverage、repository/commit/hash、public policy value、policy-file hash、checker source/fixture body、slot-to-function/file binding和任何由这些字段计算的embedding。它只获得schema object/type/constraint graph、twin-invariant opaque slot IDs、public operator type/cost/time contract、`A_mask`、t=0等值telemetry、执行后合法observation以及typed persistent state。serializer既检查字段名，也对每个no-source tensor做taint provenance；denylisted ancestor存在即run无效。

CodeTwin-v1.2的确认性primary只使用`A11–A18`：每个app的M2/M3两项、两个variants、`clean/R1/R3`三conditions、`W1`和seeds`200..204`，共`8×2×2×3×1×5=480` worlds per policy。`A01–A10`按完全相同结构产生600 worlds，但只作diagnostic，不能进入primary p-value、效应量或贡献判定。primary methods为`Full-Code+Analyzer`、`No-Source+TwinInvariantCandidates`和`SchemaTelemetryOnly`；确认性contrasts固定为Full−No-Source与Full−SchemaTelemetry。

`Shuffled-Repository`只交换同一twin group的new policy source，保持snapshot、raw trace、candidate、mask和其余input不变，并仅作source-sensitivity falsification。它检验action/kernel是否随source变化；因为交换后的source与sealed oracle故意不匹配，其harm不得用于声称哪段代码“正确”，也不进入primary superiority family。primary scalar endpoints是severe `d∨r`、success `s`和冻结cost index `C_op`，两个contrasts×三个endpoints形成六项Holm family；`d,r,v,u,w`分别报告，scope/checker/action disagreement只作机制结果。所有结果当前留空。

本文件尚无任何 twin source、snapshot 或运行结果，上述所有 hash 仍为 `PENDING-IMPLEMENTATION`。

## 7. Split-isolated risk injection templates

所有 injection 仅在无外网、可 reset 的 PostgreSQL/container research environment 中运行。policy 可读取表内指定的 source/config clue，但不读取 `risk_bit`、template ID、hidden trigger、future schedule 或 sibling outcome。train、validation 和 test 使用不同 code path、不同配置机制和不同 template source；下表不是只换随机常数的同一模板。

| Bit | Train template family | Validation template family | Test template family | 可见线索 | hidden trigger 与外部后果 |
|---|---|---|---|---|---|
| `R1-read-semantic` | `TR-R1-detail-legacy`：detail endpoint 的 legacy projection 留用 old decode 分支 | `VA-R1-cursor-list`：cursor 边界后的 list serializer 留用 old decode 分支 | `TE-R1-aggregate-sql`：aggregate/search SQL expression 留用 old decode 分支 | 对应 handler、ORM/query 和 policy source 可读 | future raw transaction 首次命中该 handler 与 M2 tie/M3 unknown；产生 differential read 或 reference mismatch |
| `R2-write-path` | `TR-R2-batch-rawsql`：scheduled batch 的 raw SQL assignment 漏掉 replacement target | `VA-R2-webhook-upsert`：webhook `ON CONFLICT DO UPDATE` 漏掉 target assignment | `TE-R2-outbox-retry`：outbox consumer 在 duplicate/retry 分支只写 old field | handler source 和 lineage 可读；调用时刻隐藏 | hidden invocation 使 old/new value divergence，随后 legacy/new read 不一致 |
| `R3-transform-boundary` | `TR-R3-backfill-expression`：pgroll backfill expression 对 M1 NULL/empty、M2 exact tie、M3 explicit unknown 或 M4 boundary 采用错误 branch | `VA-R3-orm-callback`：ORM migration callback 对同类边界使用错误 normalization/default branch | `TE-R3-chunk-postprocess`：chunked postprocessor 在 chunk 边界行采用错误 transform；错误位于独立实现，不复用 train/validation code | transform expression、callback 或 postprocessor source 可读；具体 hidden row ID 不可见 | sealed snapshot 含至少一个 motif-specific boundary row；导致 corruption 或 semantic violation |
| `R4-load-tail` | `TR-R4-hotkey`：absolute `t=180..209`，rank-1 key 的 write arrival 为 clean baseline 4 倍 | `VA-R4-oldclient-lock`：`t=240..299` 保留 25% old-client traffic，并在 `t=238` 开始一笔 75 秒 long transaction | `TE-R4-convoy-retry`：`t=120..179` 对 top-1% keys 使用 Zipf `s=1.3`，失败请求按 50/100/200 ms 重试；`t=360..389` 再执行一次 2 倍 burst | past telemetry 与 workload gateway 配置 schema 可见；future absolute schedule隐藏 | lag、lock、timeout、SLO area 或 cutover failure；raw schedule在 episode 前封存 |
| `R5-recovery-gap` | `TR-R5-wal-catalog`：checkpoint 后产生的第一个新 WAL segment 不进入 restore catalog；visible retention config 仍可读 | `VA-R5-key-rotation`：`t=300` synthetic WAL key rotation 后，restore image 缺少 prior key；rotation config 可读 | `TE-R5-restore-dependency`：restore image 的 pinned collation/timezone extension 与 base snapshot 所需版本不符；两个 lock file 可读 | config、dependency lock、retention source 可读；实际 restore结果隐藏 | drill 或 terminal recovery 出现 checksum、RPO/RTO 或 restore failure |

`R3` 的 motif-specific hidden row 规则也必须写入 manifest：M1 使用 `NULL` 与 empty string相邻的两行；M2 使用正、负 exact `.5` 各一行以及 integer-range edge一行；M3 使用一个显式 unknown、一个 case variant和一个 omitted-field transaction；M4 使用一个 expression boundary、一次 source-field retry 和一次 concurrent update。具体 row ID 由 split-specific generator 产生并封存，不能输入 policy。

每个 risk template 必须具有 `clean_patch` 与 `injected_patch`，且 clean task 只使用 `clean_patch`。injection activation 在所有方法上相同；不得按模型、action recommendation 或先前结果启停。跨 split 的 template source tree、template ID 和 hash 必须不同；实现 hash 当前均为 `PENDING-IMPLEMENTATION`。

## 8. Operator observation v3、`d_max`与observable typed result

五类nonterminal action的slot级`d_max`冻结为`RS00..RS07=120s`、`CS00..CS07=120s`、`CP=210s`、`WC=60s`、`D60=60s`。只有protocol precondition成立且`t+d_max≤600`才允许启动；planner、executor、learned/fixed baselines、siblings与ENUM共同读取这一张表。runner必须在`d_max`内签发`OK/DEGRADED/TIMEOUT/FAILED`，到时未完成先kill再签`TIMEOUT`。`d_actual`只接受substrate monotonic clock签名且必须位于`[0,d_max]`；越界为所有methods共同的`KERNEL-SCHEMA-INVALID`，不能截断。所有颜色按`red>amber>green`优先级聚合；任一red predicate成立即red，否则任一amber predicate成立即amber，否则必须满足全部green predicate。missing、timeout或measurement schema error一律red。`B_app(metric)`是每个app在clean old version、60% stable throughput下用capacity-only seed测得的基准。所有ratio统一为`ratio(x,B)=x/max(B,ε_metric)`，冻结`ε_latency_p95=1 ms`、`ε_restore_rto=1 s`、`ε_lag_p95=1 ms`、`ε_error_rate=10^-6/request`；zero baseline不得产生除零、infinity或被事后改成absolute threshold。raw baseline、floor是否生效和ratio都写入log。old/new latency ratio也以`max(old_p95,1 ms)`为分母。阈值不按模型结果调节。

| Operator | Green | Amber | Red | 返回 policy 的连续量 |
|---|---|---|---|---|
| `M_SR` | 256/256 traces completed；semantic divergence=0；fatal exception=0；function/query coverage≥0.80；new/old p95 latency ratio≤1.25 | divergence=0、exception=0，且 coverage `[0.60,0.80)` 或 latency ratio `(1.25,1.50]` | divergence≥1，fatal exception≥1，coverage<0.60，latency ratio>1.50，或 snapshot checksum 改变 | completed、divergence count/rate、exception count、coverage、old/new p50/p95 latency、checksum delta |
| `M_SV` | 16/16 checker completed；failure=0；inconclusive=0；lineage coverage≥0.80 | failure=0，且 inconclusive `1..2` 或 coverage `[0.60,0.80)` | failure≥1、inconclusive≥3、coverage<0.60，或 compatible DB checksum被只读 checker 改变 | pass/fail/inconclusive count、coverage、minimal-counterexample size、affected lineage count、checksum delta |
| `M_CP` | restore success；checksum mismatch=0；WAL gap bytes=0；RPO=0；RTO≤`1.25*B_app(restore_rto)` | 前四项满足且 RTO 在 `(1.25,2.00]*B_app(restore_rto)`，或 retained-storage age在 `[0.75,1.00]` 倍计划上限 | restore failure、checksum mismatch≥1、WAL gap bytes>0、RPO>0、RTO>`2.00*B_app(restore_rto)`，或 storage age超过计划上限 | success、checksum mismatch、gap bytes、RPO seconds、RTO seconds、storage bytes/age |
| `M_WC` | cap 生效；lag p95≤`1.25*B_app(lag_p95)`；lock-timeout=0；write error=0；queue slope≤0 | cap 生效且 lag ratio `(1.25,2.00]`、queue slope `(0,0.05]` request/s² 或 deferred-write ratio `(0.25,0.50]` | cap 未生效、lag ratio>2.00、lock-timeout≥1、write error≥1、queue slope>0.05 或 deferred-write ratio>0.50 | admitted/deferred/rejected writes、lag p50/p95、lock wait/timeout、queue level/slope、SLO area |
| `D60` | divergence alarm=0；error rate≤`1.25*B_app(error_rate)`；lag p95≤`1.25*B_app(lag_p95)`；old-client share 单调不增 | 无 divergence alarm，且 error/lag ratio在 `(1.25,2.00]` 或 old-client share 非单调但末值≤初值+0.05 | divergence alarm≥1、error/lag ratio>2.00、data checksum alarm、或 old-client share 末值>初值+0.05 | natural transaction count、alarm count、error rate、lag、old-client share start/end、occupancy slope |

每个nonterminal operator另外必须返回互斥`η∈{OK,DEGRADED,TIMEOUT,FAILED}`和固定13维signed result vector，顺序为`rpo_sec,rto_sec,wal_gap_bytes,storage_age_sec,admission_rate,activation_delay_sec,deferred_write_count,old_client_count,old_client_share,active_tx_count,lock_wait_p95_ms,lag_p95_ms,arrival_rate_ratio`。无效channel写canonical `NA`并由validity mask排除，不得写0伪装观察值。SR、SV和D60只允许8–13，CP允许1–4与8–13，WC允许5–13。D60的status固定`OK`；对SR/SV，完成且green为`OK`，完成且amber或red为`DEGRADED`，超过action timeout为`TIMEOUT`，runner或schema失败为`FAILED`。CP/WC的exact decoder如下。

| Action/status | typed result rule | persistent update |
|---|---|---|
| CP/OK | drill完成、checkpoint存在、restore verified，且observation为green | 写`checkpoint_exists=1,restore_verified=1`与1–4 channels |
| CP/DEGRADED | checkpoint存在但restore未verified，或drill完成且observation为amber/red但不属于timeout/runner failure | 写`checkpoint_exists=1,restore_verified=0`与可得1–4 channels |
| CP/TIMEOUT | 超过action timeout | `checkpoint_exists=0,restore_verified=0`；1–4为NA，仍执行age passage |
| CP/FAILED | runner/schema/executor失败 | `checkpoint_exists=0,restore_verified=0`；1–4为NA，仍执行age passage |
| WC/OK | cap active且observation为green | 写`cap_active=1`与5–7 channels |
| WC/DEGRADED | cap active但observation为amber/red，且非timeout/runner failure | 写`cap_active=1`与可得5–7 channels |
| WC/TIMEOUT | 超过action timeout | `cap_active=0`；5–7为NA，仍执行exposure passage |
| WC/FAILED | runner/schema/executor失败 | `cap_active=0`；5–7为NA，仍执行exposure passage |

`GLOBAL-TYPED-CODEC/1.0`在signature、source-authority、field validity与truth-table互斥性验证之后、任何persistent/protocol/ledger state decoder之前，消费`duration[1]+result[13]+severity[4]+accumulator[6]`的`numeric[24]/validity[24]`。codec使用RFC 8949 deterministic CBOR，enum=`uint8`，time=`int64 μs`，count/bytes=`int64`，NA同时写validity=0与CBOR null，NFC、`-0→0`，NaN/∞/overflow拒绝。量化步长与01H 6.4逐字相同：time/latency=`1ms`，bytes/count=`1`，share/rate=`10^-6`，SLO area=`10^-6 SLO-second`，CPU=`1ms`，I/O=`1024 bytes`，storage=`1 MiB-second`；exact boundary round-half-even，越界不clamp。供模型与chance child使用的固定数组恰为`record_v1=[codec_version,action_rank,η,e,o,validity_bitmap,quantized_numeric[24]]`，`canonical_record_hash=SHA256("GLOBAL-RECORD-v1"∥CBOR(record_v1))`。正常action另建`runtime_binding_v1=[world_id,episode_reset_id,action_rank,action_start_us,canonical_record_hash,sorted_source_event_ids,oracle_version]`及`GLOBAL-BINDING-v1` hash；source IDs使用第9.11节observable authority keys并排除method/model/posterior/latent。binding不进入global-cell likelihood或pre-event chance probability；固定componentizer用它生成真实`Δℓ` identities，这些observable IDs进入`x_exec`及其后memo。`k_global=SHA256("GLOBAL-CELL-v1"∥action_rank∥η∥e∥validity∥quantized_numeric)`。hash索引命中后必须比较完整CBOR bytes，不同bytes同hash即schema invalid。这个函数签名没有`z/h/model_seed/posterior/checkpoint`参数。`action_rank=0..20`对应21个真实actions，`255`只用于无invocation的precheck/idle `PASSIVE-TICK-v1`，`21..254`非法；rank255不改变action cardinality。rank255唯一改用`passive_binding_v1=[world_id,episode_reset_id,passive_interval_id,canonical_record_hash,sorted_source_event_ids,oracle_version]`及`GLOBAL-PASSIVE-BINDING-v1` hash；D60 rank18仍用normal action binding，同interval两种binding互斥。

`kernel_measure_v1`是训练、belief、planning、nonterminal与terminal的唯一概率接口。它固定`alpha=(0,0.075,0.125,…,0.925,1)`、`q=(0.05,0.10,…,0.90,0.95)`与`w=(0.075,0.05×17,0.075)`；第一和第十九层就是tail strata，支持外无额外质量。每个continuous valid head输出`raw_location/raw_log_scale`，唯一解码为`μ=12tanh(raw_location/12),s=exp(clamp(raw_log_scale,-7,3))`，并以`Y=L+(U-L)sigmoid(Z), Z∼Logistic(μ,s)`定义有界分布。对codec cell`C=[l,u)`和层`B_ξ=(α_{ξ-1},α_ξ]`，唯一条件质量为`p_ξ(C)=[min(F(u),α_ξ)-max(F(l),α_{ξ-1})]_+/w_ξ`，边界约定`F(y≤L)=0,F(y≥U)=1`。代表点为`r_ξ=L+(U-L)sigmoid(μ+s logit(q_ξ))`，只用来以固定channel序播种product-cell best-first enumeration；某key首次pop时，`cell_mass(key)`立即遍历全部19个`ξ`并求`Σ_ξw_ξM_ξ(key)`，audit representative取正质量`ξ`的最小值，key进入global visited后其余命中只记collision edge而不重复加质量或建child。未枚举质量唯一为`1-Σ_{unique emitted key}cell_mass(key)`并原样进入`MEASURE-REMAINDER`，不得丢弃或均分。

continuous support唯一为：nonterminal duration的SR/SV=`[0,120]`、CP=`[0,210]`、WC=`[0,60]`，D60为`δ_60`，TIMEOUT为各slot`δ_dmax`；terminal duration的EX=`[0,120]`、AB=`[0,60]`；R1..R13为`[0,120],[0,210],[0,2^30],[0,600],[0,1],[0,20],[0,10000],[0,10000],[0,1],[0,10000],[0,1000],[0,1000],[0,4]`；severity为`[0,1],[0,1],[0,2],[0,210]`，accumulator为`[0,2],[0,10000],[0,10000],[0,2400],[0,100×2^30],[0,1000×2^30×60]`，terminal semantic proportion为`[0,1]`。NA是`δ_NA`，`e_SLO=0`时`ΔA_u=δ_0`，`e_SLO=1`时support为`(0,2]`；`ΔD_w`只由`ΔN_w`和write ratio确定，absent event severity为`δ_0`。`L_globalN`是对同一joint observable cell边际质量的未重权proper NLL，每schema-valid record权重1并按valid-record count归一；`(η,e,o)`192类macro表只是stop-gradient diagnostic，不进入训练、checkpoint selection或Bayes update。terminal severe risk对joint terminal cells的conditional event mass求和，禁止以location、median或某一点与真值相等的指示函数代替cell probability。

absolute-time hazard的字段合同也属于`kernel_measure_v1`。`time_bin_edges_us`固定为`[0,60000000,120000000,180000000,240000000,300000000,360000000,420000000,480000000,540000000,600000000]`，每箱为`[edge_j,edge_{j+1})`，exact 600秒event归terminal。对raw cloglog `g^k_{rj}`，`Λ^k_{rj}=1-exp[-exp(g^k_{rj})]`唯一表示整60秒reference-bin event probability；被`physical_causal_closure_v3`禁止的direct ancestor cell必须先在link前精确置为`Λ_dir=0`。`Δ_j=max(0,min(t_us+10^6d,edge_{j+1})-max(t_us,edge_j))`的单位为微秒，唯一exponent为`ω_j=Δ_j/60000000`。在同exact duration上，概率语义为`S_r(d)=∏_j(1-Λ^pass_{rj})^{ω_j}(1-Λ^dir_{rj})^{ω_j}`；canonical binary64 forward则按升序`j`固定pairwise求和`ℓ_r=Σ_jω_j[log1p(-Λ^pass_{rj})+log1p(-Λ^dir_{rj})]`，再取`p_r=-expm1(ℓ_r),S_r=1-p_r`。每箱内先pass后dir，`ω=0`先返回exact 0；实现固定`CPython 3.12.13+NumPy 2.3.5`的`numpy.float64/log1p/expm1`及pinned container。16个masks按`p_m^pre=∏_r p_r^{e_r}S_r^{1-e_r}`一次构造，再经同一`post_link_projection`；禁止先积分四个边际再相乘，direct不得另选impulse时点。

对continuous `C_d=[l,u)`和`B_ξ`，`u_l=max(F_D(l),α_{ξ-1})`、`u_u=min(F_D(u),α_ξ)`。`u_u>u_l`时，`P_phys(m|C_d,B_ξ)=(u_u-u_l)^{-1}∫_{u_l}^{u_u}p_m(F_D^{-1}(v))dv`；`M`只另外含一次duration mass `(u_u-u_l)/w_ξ`。`u_u≤u_l`时不建child。D60、TIMEOUT与rank255 elapsed按exact atom评价，不用representative。`duration_conditional_integrator_v1`先在`t+F_D^{-1}(v)=edge_j`的内部交点分段，每段按start升序使用hash-locked binary64 64-node Gauss–Legendre，按node index升序求值并作固定相邻pairwise tree求和。64点表SHA-256=`92CD28D4CC2EA02574BCE1C0C2D7CF769BCC3A528D214EDE7493BBCD6411F3C2`；128点审计表SHA-256=`81ADFE772788FD490376F5807520A7CAC419F8767584CBEE2CB5CBA74E2F5B2F`。独立reference用MPFR 256-bit、round-to-nearest-ties-to-even，且不进入部署forward。任一mask的`|P64-P128|`、`|P64-Pref256|`或`|P128-Pref256|`大于`5e-12`，或16-mask归一误差大于`5e-12`，均为`KERNEL-SCHEMA-INVALID`；不得改用adaptive tolerance、clamp或representative fallback。64/128具体bytes不作跨平台预填常数，只在pinned image实现后连同image/build/reference hashes记录。

同一signed outcome唯一解码`T_a=(η,k_global,e,o,r_a,Δg,κ′,Δℓ,Δc,t_end)`，其中`Δℓ=(Δℓ_evid,Δℓ_out)`；component type/amount/interval来自quantized record，identity来自同一observable runtime binding，并分别写入双账。`e`只由source-authority records确定，`o`只由本节阈值确定，`t_end=t_start+d_actual`。真实executor从不选择模型的quantile或latent branch；belief只读取模型对这个observable cell的边际likelihood。若任一signature、status、event authority、validity、codec值或积分审计不唯一，标`KERNEL-SCHEMA-INVALID`，不得用近邻cell、raw float或默认0补齐。

`κ`的离散阈值同样唯一。`lock_class=0`当`lock_wait_p95_ms=0`且lock-timeout为0，`lock_class=1`当lock wait为正且lock-timeout为0，`lock_class=2`当lock-timeout至少1；`lag_class=0/1/2`分别对应lag ratio `≤1.25,(1.25,2.00],>2.00`；`workload_bin=0/1/2`分别对应arrival-rate ratio `≤0.75,(0.75,1.25],>1.25`。`rollback_legal=1`当phase属于`READY_COMPATIBLE`或`TERMINAL_ONLY`、complete尚未执行且database process可达；`complete_legal=1`当phase=`READY_COMPATIBLE`、`old_client_count=0,old_client_share=0,active_tx_count=0,lock_class<2,t≤600`且schema有效。其他组合一律为0。EX只在`complete_legal=1`时mask-legal；AB只在`rollback_legal=1`时mask-legal；两者都非法且到期才进入EXPIRED。所有action的`pgroll_phase`、checkpoint age、cap exposure与trace cursor按时间推进，不能因为SR/SV不直接写`g`就跳过passage。

`EX` 和 `AB` 不压缩为 green/amber/red；它们由 hidden terminal oracle产生 raw outcome vector。颜色仅是 policy 可见 observation，不能代替外部 harm label。

## 9. 十三类实例文件的字段 schema 与禁止字段

所有 schema 都必须有 `spec_version`、`created_by_builder_version`、`implementation_status` 和 `content_hash`。在源码或数据尚未生成时，`implementation_status` 必须是 `PENDING-IMPLEMENTATION`，所有 hash/digest 字段必须逐字写为 `PENDING-IMPLEMENTATION`，不得填入样例 hash 冒充实例事实。

### 9.1 `apps_manifest.yaml`

| Field | Type/约束 |
|---|---|
| `apps[]` | 恰含 `A01..A18`，顺序按数字 ID |
| `app_id/split/domain` | enum；与第 2 节一致 |
| `source_root_old/source_root_new` | workspace-relative path；不得指向共享 domain package |
| `schema_namespace/database_role` | app 唯一 string |
| `entities[]/endpoints[]/transaction_families[]` | typed IDs；每个 endpoint绑定一个可定位 handler |
| `public_policy_files[]` | M2/M3 policy source path；CodeTwin 允许变化的唯一 source |
| `dependency_lock_path/harness_version` | path 与 semver |
| `capacity_baseline` | metric、seed、sample window、raw log path；value 实现后写入 |
| `source_hash_old/source_hash_new/image_digest_old/image_digest_new/lock_hash` | 当前均 `PENDING-IMPLEMENTATION` |
| `business_source_similarity` | pair IDs、exclusion globs、token5-gram Jaccard≤0.20、typed-AST subtree weighted Jaccard≤0.30、transaction-template Jaccard≤0.25；当前values pending |

禁止字段：`risk_bit`、injection ID、hidden fixture/oracle path、future trace、sibling outcome、model score、selected action、test result、任何按方法变化的 endpoint 或 policy。

### 9.2 `migration_contracts/<app>-<M1..M4>.yaml`

| Field | Type/约束 |
|---|---|
| `app_id/migration_id/motif` | 18×4 唯一复合键 |
| `entity/table` | public schema object |
| `old_column/new_column` | name、SQL type、length/precision/scale、nullability、default、collation |
| `forward_expression/reverse_expression` | 第 3–4 节的可执行表达式；含 integer intermediate type |
| `known_mapping/default_code/unknown_policy` | 仅M3；主任务写公开policy，CodeTwin的`unknown_policy`必须为同一字面值`FROM_REPOSITORY_POLICY` |
| `rounding_policy/scale_factor/unit` | 仅M2；主任务写公开policy，CodeTwin的`rounding_policy`必须为同一字面值`FROM_REPOSITORY_POLICY` |
| `derived_dependencies/update_events/backfill_isolation` | 仅 M4；列出每个触发 source field |
| `boundary_cases[]/invalid_behavior` | exact input、expected commit/rollback、SQL/HTTP error type |
| `pgroll_operation/old_version_binding/new_version_binding` | substrate plan 与 endpoint schema binding |
| `visible_contract_ids[]/candidate_universe_version` | 只引用公开 checker/candidate IDs |
| `clean_inclusion_steps[]` | validate/start、old/new smoke、direct legal target path；typed command ID而非任意 shell |
| `contract_hash/pgroll_plan_hash/source_binding_hash` | 当前均 `PENDING-IMPLEMENTATION` |

禁止字段：hidden row ID、hidden oracle expression/source、risk truth、future workload/fault seed、test outcome、模型推荐、根据结果修改的 threshold、variant-specific candidate或 mask。

### 9.3 `visible_checker_manifest.json`

| Field | Type/约束 |
|---|---|
| `app_id/catalog_version` | app ID 与 `VISIBLE-CHECKER-v1` |
| `candidate_sets[8]` | `CS00..CS07` 固定顺序 |
| `atomic_checkers[128]` | checker ID、set ID、source path、public fixture IDs、covered public invariant、timeout、output schema |
| `policy_probe_contract` | CS04/05固定public-policy callable、raw probe schema、禁止expected constants、import allowlist与sandbox hash |
| `twin_invariant_membership` | boolean，必须为 true；并记录两个 variant 的相等性检查 |
| `read_only_db_role/build_context` | 独立只读 role 与只含 visible source 的 context |
| `catalog_hash/source_hashes/fixture_hashes/image_digest` | 当前均 `PENDING-IMPLEMENTATION` |

禁止字段：active twin policy label、hidden oracle import/path、hidden fixture/trigger、risk bit、future transaction、terminal reference state、method ID、model-specific checker filter、由 analyzer删减后的 candidate list。

### 9.4 `hidden_oracle_manifest.json`

| Field | Type/约束 |
|---|---|
| `app_id/oracle_version/build_context` | app 独立 hidden context |
| `oracle_modules` | M1 identity、M2 conversion、M3 recoding、M4 full recomputation、business invariant、recovery、availability |
| `reference_transaction_schema` | raw input field、type、timestamp、client version、idempotency key；不含模型字段 |
| `policy_binding` | twin manifest在outcome生成前写入的sealed policy constant与known-map hash；oracle独立实现且禁止import repository policy |
| `outcome_schema` | success、corruption、semantic violation、availability、recovery、RPO/RTO、SLO/cost |
| `semantic_reference_population` | `Ω_v(world_id,oracle_version)`的action-invariant reference transaction IDs、positive weights、fixed denominator与hash；同world所有policy/EX/AB/checker coverage逐字节相同 |
| `full_scan_scope/terminal_snapshot_rule` | repeatable-read snapshot 与纳入 table/row rule |
| `oracle_source_hash/hidden_fixture_hash/image_digest` | 当前均 `PENDING-IMPLEMENTATION` |

禁止字段：visible checker import/source、method ID、model seed、chosen action作为判定阈值、训练 loss、预期优胜方法、向 policy 返回的中间 oracle truth。oracle 可以读取 terminal DB 和审计动作日志以计算真实成本，但不能按 action 名称改变相同物理结果的判定。

### 9.5 `risk_injection_manifest.yaml`

| Field | Type/约束 |
|---|---|
| `template_id/split/risk_bit` | 第 7 节的 split-specific ID；三 split 不复用 source |
| `eligible_app_ids/eligible_motifs` | 明确 list |
| `clean_patch_path/injected_patch_path` | 相对路径；两者都在 outcome generation 前生成 |
| `visible_clues[]` | policy 可读 source/config/telemetry字段 |
| `hidden_activation` | absolute time、raw transaction predicate 或 restore condition；不进入 input |
| `expected_physical_channel` | observation、hazard、severity/recovery之一；不写预期模型结果 |
| `generator_seed_rule/sibling_group_rule` | deterministic rule |
| `template_hash/clean_patch_hash/injected_patch_hash/generator_hash` | 当前均 `PENDING-IMPLEMENTATION` |

禁止字段：model/method ID、model score、recommended action、结果触发 activation、跨 split 共用 source hash、把 injection ID传给 tokenizer、根据 test 调整的边界、预写某模型将避免 harm 的标签。

### 9.6 `operator_observation_v3.yaml`

| Field | Type/约束 |
|---|---|
| `operator_id/measurement_schema` | `M_SR/M_SV/M_CP/M_WC/D60` 与第 8 节连续字段、unit、window、四值status、13维result vector及action-validity mask |
| `slot_d_max/hard_start` | `RS*=120,CS*=120,CP=210,WC=60,D60=60`秒；唯一合法式`protocol_mask∧(t+d_max≤600)`；所有methods读取同一bytes |
| `typed_status_decoder` | 第8节互斥`OK/DEGRADED/TIMEOUT/FAILED` truth table；D60只允许OK |
| `result_to_state_decoder` | 第8节`CP→g_CP,WC→g_WC,all→κ`的唯一field map；无效channel必须NA |
| `green_predicates/amber_predicates/red_predicates` | 第 8 节 exact inequalities |
| `aggregation_precedence` | 固定 `red>amber>green` |
| `missing_timeout_policy` | 固定 red，另存 raw error code |
| `capacity_baseline_ref` | apps manifest metric ID；只能由 pre-episode clean run产生 |
| `ratio_definition/epsilon_floors` | `x/max(B,ε)`；latency=`1ms`、restore RTO=`1s`、lag=`1ms`、error rate=`10^-6/request`，并记录floor activation |
| `threshold_version` | `OP-OBS-v3` |
| `global_codec` | `GLOBAL-TYPED-CODEC/1.0`、`numeric[24]/validity[24]`、步长/round-half-even/invalid规则与第8节相同；训练、belief、planning与terminal均以`kernel_measure_v1`在这些边界计算cell mass，首尾tail strata、collision merge与remainder不得由operator另定义；禁止latent参数 |
| `schema_hash/threshold_hash/runner_hash/codec_hash/measure_code_hash/dmax_table_hash` | 当前均 `PENDING-IMPLEMENTATION` |

禁止字段：risk bit、hidden seed/oracle result、future telemetry、model-specific threshold、validation/test outcome tuned threshold、用拒绝率或 action frequency定义颜色。

### 9.7 `code_twin_manifest.yaml`

| Field | Type/约束 |
|---|---|
| `twin_group_id/app_id/migration_id` | 每 app 的 M2/M3 各一组 |
| `variant_ids` | M2=`HALF_EVEN/HALF_UP`；M3=`REJECT_UNKNOWN/MAP_OTHER` |
| `invariant_artifacts` | DB snapshot、raw transactions、absolute trace、fault draw、schema diff、migration contract、pgroll plan、old repo、public fixtures、checker catalog、candidate universe/order、`A_mask`、t=0非代码view |
| `variant_policy_file/variant_policy_value` | 唯一允许不同的可见 source 与 exact policy |
| `input_redaction_fields` | 必含 twin/variant/oracle policy labels |
| `baseline_views` | Full-Code、No-Source、SchemaTelemetryOnly、Shuffled-Repository 的字段 allowlist |
| `evaluation_role` | app=`A11..A18`时`PRIMARY`，app=`A01..A10`时`DIAGNOSTIC`；不可由结果改写 |
| `condition/workload/seeds` | `clean,R1,R3`；`W1`；`200..204`，twins内逐字节共同world |
| `primary_family` | methods=`Full,No-Source,SchemaTelemetry`；contrasts=`Full-NoSource,Full-SchemaTelemetry`；endpoints=`d∨r,s,C_op`；Holm family size=6 |
| `shuffled_role` | 仅`SOURCE_SENSITIVITY_FALSIFICATION`；mismatched-oracle harm禁止进入primary或代码正确性结论 |
| `oracle_qualification_matrix` | 第5.4节八个matrix IDs、raw probe hashes、预期判据与status；当前全部`PENDING-IMPLEMENTATION` |
| `no_source_denylist/taint_roots` | 第6.2节完整denylist、serializer field IDs与tensor provenance roots |
| `database_snapshot_hash/raw_transaction_hash/schema_diff_hash/migration_contract_hash/candidate_hash/mask_hash/checker_hash/t0_noncode_view_hash` | twins内最终必须相同；当前均`PENDING-IMPLEMENTATION` |
| `repository_hash_variant/oracle_hash_variant` | 允许不同；当前均 `PENDING-IMPLEMENTATION` |

禁止字段：variant-specific workload或 fault、variant-specific candidate ID/order/mask、variant-specific visible checker filter、不同 DB rows、twin ID进入模型、除公开 policy file外的 source 差异、用 action disagreement代替 external outcome、把A01–A10升级为primary、把Shuffled harm解释为正确性。

### 9.8 `split_manifest.json`

| Field | Type/约束 |
|---|---|
| `app_split` | train=`A01..A06`；validation=`A07..A10`；test=`A11..A18` |
| `world_group_id` | hash input tuple的可读前身：app、migration、snapshot seed、risk template、workload seed、fault seed、twin group；hash当前 pending |
| `validation_role` | `VAL-SELECT` 或 `VAL-CAL-POLICY`；world 不重叠；policy/checkpoint 在打开后者前冻结 |
| `cal_generator` | `CAL-GEN-v1.2`、iid superpopulation、app/migration/risk/workload weights=`1/4,1/4,1/9,1/3`、Philox root key与六component stream rules |
| `cal_qualification` | 五candidate policy hashes、fixed reference hash、15个`α/15` bounds、thresholds`0.05/0.20/-0.05`与selection tie-break |
| `enum_tier` | 仅作指向`enumeration_split_manifest.json`的mirror；后者为唯一ENUM权威 |
| `code_twin_role` | `A11..A18=PRIMARY`、`A01..A10=DIAGNOSTIC`；conditions/workload/seeds与9.7一致 |
| `fullpolicy_d60_role` | 指向`fullpolicy_d60_manifest.json`；1,152 IDs、profiles与zero-cross report，不得仅写模糊heldout list |
| `evaluation_world_arithmetic` | 每个冻结policy恰为main test `6,400` + CodeTwin `1,080` + ID-eval `1,296` + FULLPOLICY-D60 `1,152` = `9,928`个互不重叠worlds；各项ID/hash集合必须零交叉，CodeTwin的480 primary与600 diagnostic仍分别装载 |
| `seed_ranges` | data、workload、fault、sibling、CodeTwin、FULLPOLICY-D60、enumeration 与 model seeds 分列；D60固定`910..912` |
| `sibling_sampling` | 每合法 first action 的 inclusion probability、max count、deterministic seed、missing rule、共同 record IDs；不得写“按资源允许” |
| `retrieval_boundaries` | index 只由 train repo构建；current test source仅作为当次任务输入 |
| `test_open_rule` | utility、operator threshold、policy、checkpoint 与 analysis code完成后单次解封 |
| `split_hash/group_hashes/seed_manifest_hash` | 当前均 `PENDING-IMPLEMENTATION` |

禁止字段：同一 sibling group 跨 split、同一 snapshot/trace/template hash 跨 split、ENUM-TEST label进入 loss/early stop/calibration、test repository进入 retrieval memory、按结果换 split、future commit或 human rollback note。

### 9.9 `enumeration_split_manifest.json`

| Field | Type/约束 |
|---|---|
| `tiers` | 恰含`ENUM-IDENTIFY/ENUM-TRAIN/ENUM-TEST`，各自task、template、seed与用途列表 |
| `task_ids` | IDENTIFY=`D00-M1..M4`；TRAIN/TEST恰为第10.2节各八项，不允许后验增删 |
| `seed_ids/integers` | `EI-000..009→600000..600009`、`ETR-000..009→700000..700009`、`ETE-000..009→800..809` |
| `selector_version` | `enum-selector-v1`；`selector_state_hash`仅含app/migration ID、schema/contract、pre-state snapshot、opaque candidate order、physical mask与tier seed；排除repository/source/policy hash及全部runtime descendants |
| `selected_slots` | 每个start-state恰含一个`RSxx`、一个`CSxx`、`CP`、`WC`；同state全部65 sequences与methods相同 |
| `sequence_ids` | `k=0..4`按长度再按type order`SR<SV<CP<WC`字典序枚举，恰65项 |
| `label_scope` | fixed-selector、fixed-`π_ref` auxiliary partial return/rank；明确排除另外14 slots和`D60/EX/AB` |
| `record_ids/hashes` | start-state、snapshot、template、seed、selector input/selection、sequence、continuation、raw outcome与record hash |
| `heldout_fullpolicy_d60_ids` | 只保存对9.13中1,152个`FPD60-*` IDs与manifest hash的引用；不得与三个ENUM tiers、calibration、主test或CodeTwin相交 |
| `tier_hash/selector_hash/record_hashes` | 当前均`PENDING-IMPLEMENTATION` |

禁止字段：selector输入中的observation outcome、telemetry descendant、duration/cost、future/hidden seed、model score、sibling outcome；`ENUM-TEST`进入loss；把partial label命名为full/exhaustive oracle；用D60 held-out worlds修改conflict定义。

### 9.10 `runtime_lock.json`

| Field | Type/约束 |
|---|---|
| `postgres_version/postgres_digest` | version=`17.0-bookworm`；digest当前 pending |
| `pgroll_version/commit/binary_hash` | version=`v0.16.2`、commit=`cdbe9b0`；binary hash当前 pending |
| `python_version/dependency_locks` | Python `3.12.x` exact patch 与 18 个 lock hash；patch当前 pending |
| `app/operator/checker/oracle/workload/snapshot images` | image name、build context、resolved digest |
| `os/kernel/cpu/gpu/driver` | generation/training runtime facts，实现时记录 |
| `locale/timezone/collation` | 固定 `C.UTF-8/UTC` 与 PostgreSQL collation record |
| `builder_git_commit/dirty_patch_hash/config_hash` | 实现时记录 |
| `action_cardinality/order` | 固定`A_M=18,A_N=19,A_T=2,A=21`与`RS00..RS07,CS00..CS07,CP,WC,D60,EX,AB`顺序；不得按time动态压缩或重排 |
| `nonterminal_d_max` | slot-order数组=`[120×8,120×8,210,60,60]`秒；hard-start=`protocol_mask∧(t+d_max≤600)`，main与全部baseline逐字节共享 |
| `time_bin_edges_us` | 恰为`[0,60000000,120000000,180000000,240000000,300000000,360000000,420000000,480000000,540000000,600000000]`；bin `j` 为`[edge_j,edge_{j+1})`，exact 600秒event归terminal |
| `hazard_reference_exposure_us/link` | reference exposure恰为`60000000`；raw cloglog `g→Λ=1-exp[-exp(g)]`，`Λ`是整reference-bin event probability而非每秒hazard；被`physical_causal_closure_v3`禁止的direct ancestor cell必须在link前精确置为`Λ_dir=0` |
| `omega_rule/exact_duration_joint_mask` | `Δ_j=max(0,min(t_us+10^6d,edge_{j+1})-max(t_us,edge_j))`，`ω_j=Δ_j/60000000`；pass/direct共用`[t,t+d)`，先在exact duration上构造4个bit survivals和16-mask joint mass，再作post-link projection |
| `hazard_binary64_forward` | canonical event law=`q_j=ω_j[log1p(-Λ_pass,j)+log1p(-Λ_dir,j)]→fixed_pairwise_j(q_j)→p=-expm1(ℓ),S=1-p`；每箱先pass后dir，`ω=0`项exact 0；dtype=`numpy.float64`，rounding=`nearest-ties-even`，禁止用直接`1-product`、不同sum order或平台默认fast-math旁路 |
| `duration_conditional_integrator` | `GL-CDF-SEGMENTED/1.0`；`u_l=max(F(l),α_{ξ-1}),u_u=min(F(u),α_ξ)`，积分joint mask `p_m(F^{-1}(v))`；内部bin-edge交点分段，64-node是唯一forward，128-node只审计，segment/node升序且固定pairwise tree；`u_u≤u_l`不建child，`M`中duration mass只乘一次 |
| `gl64_table_sha256/gl128_table_sha256/integration_atol` | `92CD28D4CC2EA02574BCE1C0C2D7CF769BCC3A528D214EDE7493BBCD6411F3C2`；`81ADFE772788FD490376F5807520A7CAC419F8767584CBEE2CB5CBA74E2F5B2F`；`5e-12`。hash payload为`GL-BINARY64-v1\0`+ascending nodes big-endian binary64+weights big-endian binary64 |
| `integration_runtime/container` | `CPython==3.12.13,NumPy==2.3.5,binary64,RN-even,fast-math=off`；runtime image必须按digest pin，`integration_container_digest/integrator_build_hash`当前均`PENDING-IMPLEMENTATION`。同一run的training/Bayes/planner只能装载同一build与64-node forward bytes/hash；不预宣称跨平台bit-identical |
| `reference_engine/error_contract` | 独立`MPFR precision=256 bits,rounding=MPFR_RNDN`或逐bit等价实现；Gold-09用冻结解析式，其他fixture用等价256-bit segmented reference。逐mask要求`abs(P64-P128),abs(P64-Pref256),abs(P128-Pref256)≤5e-12`且16-mask归一误差`≤5e-12`；reference不进入训练/Bayes/planner |
| `canonical_state_schema` | `x=(b,x_exec)`，`x_exec=(p,q_n,g,κ,ℓ,c,t,τ,A_mask)`；`q_n`是可观察defer计数；`executor_state_hash`排除belief/model/latent，`planner_state_hash`包含`b+executor bytes`；codec匹配01H 6.1/6.5.2 |
| `ledger_state_schema` | `ℓ=(ℓ_evid,ℓ_out)`；evidence IDs与outcome component IDs使用不同domain separator，不能互转；`c`只由`ℓ_out`投影 |
| `persistent_state_schema` | `g_CP={checkpoint_exists,restore_verified,RPO,RTO,WAL_gap,storage_age}`、`g_WC={cap_active,admission_rate,activation_time,deferred_write_count}`；SR/SV不直接改`g`，D60和全部action仍执行passage-of-time aging/exposure transition |
| `protocol_state_schema` | `κ={pgroll_phase,old_client_count,old_client_share,active_tx_count,lock_class,lag_class,workload_bin,rollback_legal,complete_legal,trace_cursor}` |
| `observable_branch_schema` | 唯一canonical executor tuple恰为`T_a=(η,k_global,e,o,r_a,Δg,κ′,Δℓ,Δc,t_end)`，其中`Δℓ=(Δℓ_evid,Δℓ_out)`，与01H 6.4逐项相同；其唯一numeric provenance是`record_v1`中的`d/result[13]/severity[4]/accumulator[6]`，ledger identity由同一observable binding唯一补全。episode audit row可另存canonical record/hash与runtime binding/hash，但不形成第二套tuple；tuple、codec和binding均禁止`z/h/ξ/model_seed/posterior`，可观察defer计数`q_n`只保留在executor state |
| `global_codec_schema` | `GLOBAL-TYPED-CODEC/1.0`、RFC8949 deterministic CBOR、`numeric[24]/validity[24]`与第8节steps/tie/invalid rules；rank0..20对应actions，rank255只对应无invocation PASSIVE-TICK，21..254非法。model一律用`kernel_measure_v1`对该同codec cell计算CDF mass，canonical content/hash供training、belief、chance child与terminal共用。runtime binding不改likelihood，但经fixed componentizer生成post-state ledger IDs并进入后续memo；同signed outcome跨模型逐bit相同 |
| `event_after_action_order` | 固定`bounded precheck→PASSIVE-ADVANCE-v1→post-passage protocol+hard-start mask→started invocation→signed record→唯一observable T_a→x_exec/ledger→kernel_measure_v1 belief→p/q_n/τ/mask`；mask改变时在passive advance后停止，不得创建invocation。runtime不选latent branch或二次读raw result |
| `next_state_equation` | 先以`(b_pc,x_exec_pc)=PASSIVE-ADVANCE-v1((b,x_exec),[t,t_pc))`产生唯一post-precheck state。若action仍合法，再以`x_exec'=Canon(P(p_pc,a,η),Q(q_pc,a),G(g_pc,Δg),κ′,Append(ℓ_pc,Δℓ),c_pc+Δc,t_end,600-t_end,Mask(d_max,...))`并以同一cell mass更新`b'=Belief(b_pc,T_a)`；否则next state就是post-passage canonical state。两路均禁止`min(t+d,600)`事后censor |
| `state_machine_version` | `MOL-RUNTIME-SM/1.5-REPAIRED-v5`；下面各transition必须生成machine-readable table |
| `precheck_transition` | 每个precheck无论operator是否声明native deadline，wrapper都强制`elapsed≤min(1.000s,600-t_start)`且超时kill。实际elapsed必须先调用下行唯一passive kernel，再重算protocol和hard-start mask；mask变化则记`mask_changed`，不创建`action_invocation_id`、不消耗slot/type或action resource，但passage outcome与maintenance cost已入账 |
| `passive_advance_kernel` | `PASSIVE-ADVANCE-v1(x,[t,t'))`以`passive_interval_id=SHA256("PASSIVE-v1"||world_id||reset_id||t_us||t'_us||trace_hash)`对half-open authoritative trace去重，固定更新序为`g_CP storage age/g_WC exposure→κ old-client/tx/lock/lag/workload bins与trace_cursor→ℓ_evid passive alarms→ℓ_out与c的production outcomes/maintenance resource→kernel_measure_v1 PASSIVE-TICK belief→t,τ,mask`。它不追加`p`、不增`q_n`、不消耗type、不生成action resource；event time恰为`t'`归下一区间，`t'=600`时先消费区间再terminal-only |
| `passive_tick_schema` | precheck/idle唯一使用保留`action_rank=255`的`PASSIVE-TICK-v1` global record及`passive_binding_v1=[world,reset,passive_interval_id,record_hash,source_ids,oracle_version]`；该rank不计入21 actions或任何mask/invocation。固定`η=OK,o=GREEN`，signed elapsed `[0,60]`为条件质量1，R1..R13全NA，event/severity/accumulator只取该half-open interval authorities；likelihood为`Σ_hΣ_ξPi_Pw_ξP_pass(e|C_elapsed)M^pass(C_severity,C_acc)`且同样调用`kernel_measure_v1`。elapsed是exact duration atom，必须用同一`time_bin_edges_us/ω/joint-16-mask`前向且`Λ_dir=0`，不调用representative或continuous integrator。idle超过60秒从原始start按60秒确定性切段。D60不发rank255，而把passage bytes并入唯一D60 `T_a`及normal action binding，只做一次Bayes update后`q_n+=1`；同一interval双binding/record/update为schema invalid |
| `started_transition` | action一旦started，即使timeout/executor failure也计同branch的elapsed/resource、按第8节status写typed result并消耗其type；CP/WC的persistent更新只服从该decoder，不以另一个success flag旁路 |
| `horizon_transition` | 每个nonterminal均只在`t+d_max≤600`时可启动；runner在`d_max`内返回，故started action不跨600。无post-hoc status rewrite；`t=590`五类nonterminal全mask=0且runner invocation=0。无native deadline的precheck也受wrapper cap、`t_start≤600`、expiry和terminal约束，决策state永不得`t>600` |
| `terminal_transition` | `t≥600`移除18 mitigation与D60；mask-legal EX和AB仍可选，单一合法则强制该项，两者都非法才`EXPIRED` |
| `terminal_evaluation` | terminal输入只取terminal action开始时的current canonical state、sealed terminal trace与action-invariant`Ω_v`；`t_start∈[0,600]`，EX/AB的absolute `evaluation_end=t_start+d`且`d∈[0,120]/[0,60]`，全局最晚为720/660秒。nonterminal的10-bin hazard只覆盖`[0,600)`，exact 600秒event与后续terminal window只由terminal joint head/sealed trace一次处理；不得重新开放nonterminal action、回写bin 9或按policy更换reference population |
| `schema_invalid_rule` | raw record不能唯一匹配status/cell/schema，或任一GL64/GL128/reference/16-mask误差超`5e-12`时标`KERNEL-SCHEMA-INVALID`；所有methods同口径作run invalid并另报failure-as-harm sensitivity，禁止raw bypass、换积分器或放宽容差 |
| `episode_record_schema` | 每步保存precheck start/end/deadline/status、`passive_interval_id`、PASSIVE-TICK或D60互斥record kind及canonical record/hash、passage event/source IDs、pre/post-passage executor/planner hashes、d_max、raw signed record hash、matched`(η,k_global,e,o)`、action canonical record/hash、runtime binding/hash、`r_a/d/Δg/κ′/Δℓ_evid/Δℓ_out/Δc/t_end`、post-action executor/planner hashes与ledger hashes；积分审计另存runtime image/build hash、GL表hash、64-node forward bytes/hash、128-node audit bytes/hash、ref256 report hash与三项误差，不得保存matched`z/h/ξ` |
| `state_mutation_suite` | `MT-STATE-01..06`：01..04保留CP/WC不同typed fields、same-record/different-posterior invariance与t=590 no-start；05重放Gold-03的passage全状态，06重放Gold-04的`t=600` terminal-only。`CODEC-GOLD-01..08`、`MEASURE-GOLD-01..09`与`HORIZON-GOLD-01..04`逐项保存fixture、expected canonical bytes与status |
| `componentizer_version` | `dual_ledger_componentizer_v3`；runtime分别写signed evidence/outcome records，只有outcome ledger可投影`c/Y`，所有IDs禁止latent/model/posterior |
| `shared_clone_contract` | `quota_seed/model_seed=2026081604`，PyTorch Philox deterministic；`shared_init_v4.bin`的同名同shape bytes分别load为MAIN/GENERIC独立storage，generic专属module以`SHA256("GENERIC-RESIDUAL-v4"||seed||module_name)`子流初始化；step0 hash可复算、data pointer全异，单边optimizer step不得改变另一clone |
| `reset_transition` | terminal后校验snapshot/database/container/RNG/trace cursor全量reset，失败world对所有methods同口径处理 |
| `runtime_lock_hash` | 当前 `PENDING-IMPLEMENTATION` |

`HORIZON-GOLD-03`的machine-readable fixture必须逐字产生下列truth table；任一字段不同都是runtime failure，不得以“动作未开始”跳过passage。

| Gold-03 字段组 | pre-state | `[479.950000,480.050000)`中唯一authority | 唯一 next-state |
|---|---|---|---|
| clock/action | `t=479.950000,tau=120.050000`，选RS且旧mask=1 | precheck elapsed=`0.100000` | `t=480.050000,tau=119.950000`，RS新mask=0，`status=mask_changed:HARD_START`，`action_invocation_id=null`，`p,q_n,type-consumption`逐byte不变 |
| persistent/protocol | `g_CP={checkpoint_exists:1,storage_age:10.000000}`，`g_WC.cap_active=0`，`κ.trace_cursor=479.950000` | `t=480.000000`的trace row为`old_client_count=2,old_client_share=0.200000,active_tx_count=1,lock_class=0,lag_class=0,workload_bin=1` | `g_CP.storage_age=10.100000`，`g_WC`不变，`κ`取该row并且`trace_cursor=480.050000` |
| evidence/outcome | fixture的两账无既有记录 | `HG03-ALARM-1`；`HG03-WRITE-1`是一条deferred production write；SLO超额=`0.250000 SLO-second` | `ℓ_evid`只加一条alarm；`ℓ_out/c`令`N_w+=1,D_w+=1,A_u+=0.250000`，每个component只写一次 |
| passive cost/belief | 本区间增量初值为0 | maintenance=`CPU 0.100000 core-second,IO 4096 bytes,storage 0` | `c`增加对应量，只生成一个`action_rank=255` PASSIVE-TICK canonical record并令`b'=Belief(b,PASSIVE-TICK)`，passive/executor/planner/ledger hashes从上述bytes唯一派生 |

`HORIZON-GOLD-04`固定pre-state为`t=599.800000`且operator未声明native deadline。wrapper必须在0.200000秒kill precheck，用上述同kernel消费`[599.8,600)`的全部authority records，不创建invocation或消耗slot/type/action resource，然后唯一地产生`t=600,tau=0,terminal-only`；EX/AB均不合法才产生`EXPIRED`，不存在`t>600`的decision state。

禁止字段：floating image tag作为最终锁、未解析 dependency range、一个 digest 指代多个 build、静默覆盖旧 lock、model performance、test result、secret或真实生产 credential。

### 9.11 `dual_ledger_schema.json`

| Field | Type/约束 |
|---|---|
| `diagnostic_evidence_ledger[]` | `evidence_id,parent_action_id,evidence_type,start,end,raw_measure,visibility,signature`；public checker、shadow replay、nonterminal CP probe与passive alarm只能写此表 |
| `outcome_event_ledger[]` | `event_id,parent_incident_id,event_type,start,end,source,raw_measure,repair_record_id,signature`；仅production gateway/database、cgroup与terminal oracle可写，interval为half-open UTC |
| `source_authority` | public/shadow/probe与authoritative passive monitor alarm=evidence；gateway=SLO/write；production database=damage；sealed terminal semantic oracle=`Ω_v/C_v`；terminal recovery oracle=`C_r`；cgroup的action与maintenance interval=resource；operator echo只链接。这些authority与是否存在action invocation无关，`PASSIVE-ADVANCE-v1`不得丢弃区间记录 |
| `outcome_component_ledger[]` | `component_id,type,stable_key,numerator,denominator,amount,first_seen,source_event_ids`；type恰为`C_d,C_v,C_u,C_w,C_r,C_sax,C_res` |
| `id_rules` | action-bound event=`SHA256("OUT-EVENT-v3"∥world_id∥episode_reset_id∥action_slot∥action_start_us∥source_authority∥raw_source_event_id∥oracle_version)`；passive interval先生成`passive_interval_id=SHA256("PASSIVE-v1"∥world_id∥episode_reset_id∥t_us∥t'_us∥trace_hash)`，再以该ID代替action slot/start进入`SHA256("OUT-EVENT-PASSIVE-v1"∥passive_interval_id∥source_authority∥raw_source_event_id∥oracle_version)`。component=`SHA256("OUT-COMP-v3"∥event_id∥type∥stable_key∥interval_start/end∥oracle_version∥local_index)`，evidence分别用`EVID-v3`或`EVID-PASSIVE-v1`。raw source ID必须由world/reset、logical request或fault、half-open interval及source-local index确定生成，禁随机UUID；全部IDs均禁`z/h/model/posterior/state_hash/method`及其散列 |
| `semantic_reference_population` | `Ω_v`的reference IDs、weights、denominator hash在world生成时封存；public/shadow/probe不得写、扩张、缩小或重新加权它 |
| `semantic_key/write_key` | semantic只由`Ω_v reference_tx_id×oracle_version`；write为production `logical_request_id`；retry不得新建key |
| `interval_rule` | SLO/resource以一秒half-open bins union；同源分片与重复回显不得改变积分或hash |
| `event_component_consistency` | `e_SLO=0⇒ΔA_u=0`且`e_SLO=1⇒ΔA_u>0`；damage crossing bit与首次`C_d`一致；public semantic/recovery probe只新增evidence；每个Δcomponent可回指同branch record |
| `terminal_rules` | CP probe不能写`C_r`；terminal一次性评价整个`Ω_v`；`C_sax`只取`SUCCESS/ABANDON/EXPIRED`之一；repair/rollback不能删除既有component |
| `mutation_suite` | `MT-LEDGER-01..14`逐项fixture、expected canonical bytes与status；07=passing-check anti-dilution，08=failing-check evidence-only，09=shadow isolation，10=policy-invariant Ω_v，11=single disposition，12=record/component一致，13=same-record cross-model hash，14=z/h-order invariance；当前status均`PENDING-IMPLEMENTATION` |
| `evidence_ledger_hash/outcome_event_hash/component_ledger_hash/componentizer_hash` | 当前均`PENDING-IMPLEMENTATION` |

禁止字段：method-specific dedupe、negative component、repair时删除历史、public/shadow/probe写`C_v`分子或分母、用checker覆盖率稀释`v`、把同一WC write同时写入action cost和`C_w`、把同一时间段SLO同时写入event penalty和`C_u`、把terminal timeout/missing-success另建task-failure component。

### 9.12 `joint_kernel_manifest.json`

| Field | Type/约束 |
|---|---|
| `kernel_version/factorization` | `Q-SEMI-MARKOV/1.5-REPAIRED-v5`；唯一started-action顺序=`z→action-invariant passage h→duration/resource→passage+masked-direct exact-duration joint physical→duration-cell conditional integration→tool status/observation→GLOBAL-TYPED-CODEC→observable T_a`；precheck/idle/D60的no-action elapsed只走`PASSIVE-ADVANCE-v1`与其`PASSIVE-TICK`。两者的continuous record都使用`kernel_measure_v1`，runtime不选latent branch |
| `axes` | `A_N=19,A_T=2,A=21,Z=32,H=8,ETA=4,Q=19,T_R=13,E=4,F=16,O=3,K=6,D_C=24,time_bins=10`；`time_bin_edges_us=[0,60000000,…,600000000]`的11个值必须完整保存；`action_rank=255`是codec-only PASSIVE-TICK而非action，`ξ=1..19`专用measure stratum，executor defer count专用`q_n`；`K_global`为countable observable codec |
| `quadrature_nodes/weights` | `alpha=(0,0.075,0.125,…,0.925,1)`，`q=(0.05,0.10,…,0.90,0.95)`，`w=(0.075,0.05×17,0.075)`；`ξ=1,19`是显式tail strata。每个head只用`raw_location/raw_log_scale→μ=12tanh(raw/12),s=exp(clamp(raw,-7,3))`的bounded transformed-logistic family；representative=`L+(U-L)sigmoid(μ+s logit(q_ξ))`只播种enumeration，不代替CDF cell mass |
| `continuous_cell_measure` | 对`C=[l,u)`和`B_ξ=(α_{ξ-1},α_ξ]`，`p_ξ(C)=[min(F(u),α_ξ)-max(F(l),α_{ξ-1})]_+/w_ξ`；先对primitive valid heads取条件乘积，再对全部`C_prim`经`Link_codec` push-forward到同一global cell求和，故derived `ΔD_w=round_half_even(ΔN_w r_w)`没有独立head。global mass为`Σ_ξ w_ξ M_ξ`。某key首次pop即遍历全部19层求exact global mass并按最小正质量`ξ`记audit representative；global visited确保其他seed/path只记collision edge而不重复加质量或建child。remainder=`1-Σ_{unique emitted key}cell_mass(key)`。training、belief、planning与terminal调用同一函数和同codec boundaries |
| `hazard_time_contract` | `time_bin_edges_us=[0,60000000,120000000,180000000,240000000,300000000,360000000,420000000,480000000,540000000,600000000]`，箱为half-open；`reference_exposure_us=60000000`，`Λ=1-exp[-exp(g)]`，`ω=Δ/reference_exposure_us`。pass/direct在同exact `[t,t+d)`上按stable binary64 `p=-expm1(fixed_pairwise_j{ω[log1p(-Λ_pass)+log1p(-Λ_dir)]})`得到bit mass并一次构造16-mask joint；禁止direct另选impulse time、直接`1-product`或fast-math，exact 600秒event只归terminal |
| `duration_conditional_integrator` | `u_l=max(F_D(l),α_{ξ-1}),u_u=min(F_D(u),α_ξ)`，每个mask的唯一forward是`(u_u-u_l)^-1∫p_m(F_D^-1(v))dv`；先按absolute-bin交点分段，每段用64-node GL和固定pairwise tree，128-node只审计。GL64 SHA=`92CD28D4CC2EA02574BCE1C0C2D7CF769BCC3A528D214EDE7493BBCD6411F3C2`，GL128 SHA=`81ADFE772788FD490376F5807520A7CAC419F8767584CBEE2CB5CBA74E2F5B2F`；canonical runtime=`CPython3.12.13+NumPy2.3.5 binary64`且container/build hash必填，独立reference=`MPFR-256/RNDN`。逐mask `64↔128,64↔ref,128↔ref`与16-mask归一的atol均=`5e-12`；`u_u≤u_l`不建child，duration mass只在`M`中乘一次 |
| `nonterminal_shapes` | `Pi_P[32,8],D_N[19,32,8,19,2],g_pass/Lambda_pass[32,8,4,10],g_dir/Lambda_dir[19,32,8,4,10],Gamma_tool[19,32,8,19,4],R_tool[19,32,8,4,13,19,2],S_pass[32,8,4,19,2],S_dir[19,32,8,4,19,2],K_pass[32,8,16,6,19,2],K_dir/res[19,32,8,16,6,19,2],Xi_G[19,32,8,19,4,16,K_global],O[19,32,8,4,19,16,3]`；hazard tensor的10轴严格对应冻结absolute-time bins，`g→Λ`只按cloglog整箱概率解码；`Xi_G`仅sparse evaluate observed/planning cells |
| `terminal_shapes` | `Pi_T[2,32,8],J[2,32,8,8],V_v[2,32,8,8,1,19,2],D_T[2,32,8,19,2],K_T[2,32,8,6,19,2]`；最后两轴仍是同一`(ξ,location/log_scale)`参数化，terminal joint cell质量也由`kernel_measure_v1`给出。terminal `u,w`由`c+K_T`唯一派生；`d/r/v/u/w`都以cell/conditional event mass判定，禁止location点值等号 |
| `global_codec` | `GLOBAL-TYPED-CODEC/1.0`；RFC8949 CBOR、`numeric[24]/validity[24]`、steps/half-even/tails/invalid、`k_global`与record hash逐字匹配第8节；codec签名禁`z/h/model/posterior` |
| `belief_likelihood` | 逐字实现01H 6.4：`L_z(T)=Σ_hΣ_ξ Pi_P[z,h]w_ξ P_phys(e;x,a,z,h,ξ,C_d)Gamma_tool[a,z,h,ξ,η]M_{a,z,h,ξ,η,e}(C_global)O[a,z,h,η,ξ,e,o]`，再以`b'(z)∝b(z)L_z(T)`归一化。`P_phys`必须是上行64-node integrator对post-projection joint 16-mask的cell-conditional mass；禁止先积分四个边际再相乘，禁止以128-node审计值替代forward。duration/result/severity/accumulator的cell质量已在`M`中，不得再乘duration mass或在representative上取hazard点值。`M`就是上行同codec cell的CDF mass，不得漏`ξ`、另造point-density likelihood或以MAP latent branch代替边际化 |
| `globalN_training_likelihood` | `L_globalN=-(1/N_valid)Σ_i log max(Σ_z b_i(z)L_z(T_i),2^-52)`，每schema-valid train record权重恰为1，不过采样也不按class重权；rank255 PASSIVE-TICK同样各计1，其结构性`η/o/duration`质量为1且只训练passage event/severity/accumulator likelihood，不能删除或与D60双计。所有continuous-action records的event项与Bayes/planner逐byte共用同一64-node joint-mask conditional mass；`L_pass/L_direct`也不得使用边际后处理或representative surrogate。这个proper joint NLL是deployment/Bayes的唯一likelihood。`(η,e,o)`192类macro NLL以非空class各`1/|C+|`归一，但只写stop-gradient diagnostic table，不入total loss、checkpoint或belief |
| `physical_decomposition` | `Pi_P(z)`先抽shared `h`且无action接口；`PassageKernel(H0,z,h,R_phys,L_evt,t,d)`在matched pre-state/absolute interval/duration下action-invariant；`DirectKernel(H0,z,h,e_m,p)`可条件化同一`h`但不能重加权它，只走声明路径；pass/direct primitives经规范化deterministic `Link_phys+post_link_projection`得到唯一final physical distribution；`ToolObs`不能成为physical parent；`Resource`只写资源/机会成本 |
| `option_factor_widths` | active families=`tool=608,obs=29184,dur=152,evidence=464,persist=1976,availwrite=7528,resource=21888`；`Pi_P/PassageKernel`无active residual；main/pair broadcast按01H 6.3 |
| `causal_artifact` | `physical_causal_closure_v3.npz`物化`base_action_invariant[outcome,ancestor]`、`direct_allow[operator,outcome,ancestor]`、`direct_ancestor_closure`、`duration_mediation_allow`、`post_link_projection`、axis labels与hash；main/generic共同读取 |
| `operator_outcome_direct_allow` | outcome顺序=`damage,semantic,availability,write,recovery,g_CP,g_WC,evidence,resource`；SR=`0,0,0,0,0,0,0,1,1`；SV同；CP=`0,0,0,0,0,1,0,1,1`；WC=`0,0,1,1,0,0,1,0,1`；D60全0。逐个非零cell的唯一ancestor set为：SR/SV evidence=`candidate_static,ordered_path,registered_operator_fields`；CP evidence同理且`g_CP=η,valid_R1..R4→fixed_decoder`；WC availability/write=`candidate_static,ordered_path,declared_write_cap`且`g_WC=η,valid_R5..R7→fixed_decoder`；SR/SV/CP/WC resource=`candidate_static,ordered_path,d_actual,cgroup_fields`。其余operator×outcome×ancestor cells在post-link后仍为0；`η/o`不得成为前五类physical outcome祖先。`g_CP/g_WC`禁止另设`Δg`随机head、cell或loss |
| `duration_mediation` | 所有合法action可因duration不同承受不同absolute-time passage；matched duration时SR/SV/CP不得改五类production/terminal outcome，WC只可改availability/write；CP仅`g_CP→future recovery`、WC仅`g_WC→availability/write`为允许中介 |
| `tool_no_reweight` | `Gamma_tool/O`位于physical link之后；不得输入`Pi_P/Lambda_pass/Lambda_dir/S_pass/S_dir/K_pass/K_dir`，置换status/observation logits须保持physical marginals逐bit不变 |
| `terminal_history_closure` | terminal heads只读`H0,z,R_phys,ℓ_out,t`、terminal action与sealed trace；禁止直接读`p,q_n,ℓ_evid`、既往tool status/observation或nonterminal action ID。CP history仅`g_CP→recovery`，WC history仅`g_WC→availability/write`，SR/SV history无terminal physical path；同一post-link projection执行 |
| `causal_tests` | TT-1..4=firewall/pair/truncation/isomorphism；TT-5 BaseJacobian；TT-6 DirectCausalJacobian；TT-7 matched-duration total effect；TT-8 duration-mediated effect；TT-9 tool no-reweight；TT-10 support mutation；main/generic同测 |
| `event_after_action_transition` | 指向runtime lock的observable branch/order；precheck elapsed先用`PASSIVE-ADVANCE-v1`同时推进`t/g/κ/ℓ/c/b`，typed CP/WC result及started passage继续影响后续action，event/accumulator/component按9.11结构link一致；episode key删latent |
| `cell_scales/tails` | codec steps逐字匹配第8节；support与transform不再使用可选normalizer。duration/R13/severity/accumulator/terminal-v的冻结support逐字匹配第8节`kernel_measure_v1`；首尾层各保存0.075 mass，half-even只定义codec boundary，runtime overflow invalid而非clip |
| `duration_horizon` | started action的`d_max=[120×8,120×8,210,60,60]`，启动条件`t+d_max≤600`；D60=`δ_60`，TIMEOUT=`δ_dmax`，其余时长用第8节对应bounded family；precheck另受`min(1s,600-t)`wrapper cap，真实elapsed走passive kernel，禁cross-horizon censor/rewrite。nonterminal hazard bins严格止于half-open 600秒；terminal EX/AB支持`[0,120]/[0,60]`，exact 600秒及后续event只由terminal joint cells处理，不重用bin 9 |
| `risk_target` | 资格与planner threshold只用severe `d∨r`；`v/u`独立报告，不得改称统一安全保证 |
| `memo/pruning` | memo codec、`UB`、AND-OR bound propagation、priority tuple、fallback、200,000 cap与tie-break逐字匹配01H 6.5.2 |
| `shared_baseline_contract` | `G-PhysicalFactoredSMDP`获得相同visible bytes、raw/global/partial labels、21 actions/mask、d_max、records/split、causal artifact、heads、codec/measure/loss、update count/batch order/optimizer/scheduler/precision/clipping/early-stop、componentizer、qualification worlds、tool/rollout/tree search、200k cap与wall-clock；唯一差异为direct residual tying |
| `generic_architecture` | serializer恰18 tokens；4层不共享的pre-LN bidirectional Transformer均用`d_model=384,heads=6,dropout=0.10`，每层FFN唯一为`384→W→384`。固定family序`tool,obs,dur,evidence,persist,availwrite,resource`的head唯一为`384→r_f→d_f`，`d_f=608,29184,152,464,1976,7528,21888`。`a_contract`含d_max，输出只接closure允许direct axes；seed=`2026081604`且独立storage/optimizer不alias |
| `generic_quota_domain` | tuple=`(W,r_tool,r_obs,r_dur,r_evidence,r_persist,r_availwrite,r_resource)`；`W∈{384..3072}`逐整数，每个`r_f∈{1..128}`逐整数。参数式唯一为`P_fixed+4(2×384W+W+384)+Σ_f[(385+d_f)r_f+d_f]`且必须等于`P_main`；候选集、字段序和整数域不得改 |
| `parameter_flop_match` | `FLOP-PROBE-v4`用seed `2026081604`和shape train=`B64,L18,A21,Z32,H8,Q19`、infer=`B1`且其余相同，逐个21 root actions使用各自冻结的action/result-validity/physical-closure masks并按PyTorch-FX实际graph计MAC。`δ_train/infer`各为21 actions上相对MAC差的最大值。先保留参数完全相同且两项`δ≤0.005`的tuple，再唯一最小化`(maxδ,δ_train,δ_infer,W,r_tool,r_obs,r_dur,r_evidence,r_persist,r_availwrite,r_resource)`；空集则配置无效，无seeded/stochastic tie-break。禁idle branch/padding或缩小inputs/labels/actions |
| `generic_quota_manifest` | 在任何label解封前，`generic_quota_v4.json`必须写唯一tuple、完整domain/key、`P_main/P_fixed/P_G`、逐21-action train/infer MAC、seed、版本与script/source hash，并由`parameter_count_v4.py --verify-manifest`空进程重算字节相等；它是唯一argmin的记录，不是实施者的选项表。当前为`PENDING-IMPLEMENTATION` |
| `golden_suites` | `CODEC-GOLD-01..08`、`MEASURE-GOLD-01..09`（含tail mass守恒、`ξ=2/7/11`首次pop即遍历19层的碰撞合并、terminal/nonterminal同codec、proper NLL/Bayes共享likelihood、PASSIVE/D60不双计以及absolute-time cross-bin joint-mask积分）、`HORIZON-GOLD-01..04`、`MT-STATE-01..06`、`MT-LEDGER-01..14`、`CLONE-GOLD-01..03`均保存fixture与expected bytes，当前`PENDING-IMPLEMENTATION` |
| `measure_fixture_constants` | 普通CDF fixture用IEEE binary64/ties-to-even与probability atol=`5e-15`。`MG03`：support[0,1]、step1e-6、logscale0，`ξ2/7/11`的`raw_location=12atanh[-logit(q)/12]`且`q=.10/.35/.55`，其余层按01H给定±`12atanh(11/12)`；expected code500000、cell[.4999995,.5000005)、mass=`2.25999999994841e-6`、audit ξ2、child1。`MG04`：raw0/logscale0，expected tail=.075/.075、interior=.85、total1。`MG05`：duration codes=`60000/120000/210000/60000`且atom mass1。`MG06`：两侧`e_SLO=1,ΔA_u=.4`、support(0,2]、ξ4，expected code400000、cell[.3999995,.4000005)、conditional=`1e-5`、unconditional=`5e-7`。`MG08`：rank255 precheck与rank18 D60各一record/一update/weight1，macro gradient0 |
| `cross_bin_fixture` | 透明更正`02R`的illustrative数值：原`[.0995,.1005)`正确mean=`0.000273715921527166726076182596457777431887020665453…`，不是`02R`所列常数，且与center只差`5.76150640555997728939777864672e-13`，无法在`5e-12`下拒绝center。Gold-09改用`t=59.95`、integrator diagnostic `C_d=[.095,.105)`、`F_D(d)=d/120`、`ξ=1`、`Λ_pass=(.1,.2,0,…)`、`Λ_dir=0`；保存解析式 `p_bar=1-0.9^(0.05/60)×60/[0.01 ln(0.8)]×[0.8^(0.055/60)-0.8^(0.045/60)]`，MPFR-256 expected=`0.000273715864488253310046247308663703168609609179332…`，center=`0.000273715922103317366632180325397555296559371695323…`，diff=`5.76150640565859330167338521279e-11`；错把重叠秒数直接作exponent的unit fork=`0.016290841134078839839074520041534572635018392409060…`。GL64 canonical/GL128 audit/ref256三项误差与16-mask normalization均须`≤5e-12`，center/unit fork拒绝，`M`只乘一次duration mass，training/Bayes/planner共用同一runtime的64 bytes/hash。64/128具体数值不作跨平台预填常数；该diagnostic区间不修改runtime 1ms codec |
| `schema_hash/kernel_code_hash/codec_hash/measure_code_hash/causal_hash/memo_codec_hash/search_code_hash/integration_container_digest/integrator_build_hash/gold09_forward_hash/gold09_audit_hash/ref256_report_hash/generic_quota_manifest_hash/parameter_report_hash/flop_report_hash` | 当前均`PENDING-IMPLEMENTATION` |

禁止字段：runtime latent cell或matched`z/h/ξ`、用continuous point density/location equality代替cell mass、class-reweighted deployment/Bayes likelihood、丢弃tail/collision/remainder mass、post-hoc horizon censor、passive elapsed只改`t`、joint record之外的started-action state update、tool-status physical reweighting、action-conditioned passage base、head-bit替代ancestor closure、另一套belief codec、future-truth bound、method-specific d_max/mask/prior、live shared parameters、只给理论模型的label或larger search budget、从多个generic tuple中人工选择。

### 9.13 `fullpolicy_d60_manifest.json`

| Field | Type/约束 |
|---|---|
| `suite_version` | `FULLPOLICY-D60-v1` |
| `app/migration/risk/workload/profile/seeds` | `A11..A18`×`M1..M4`×`{R1,R4,R1R4}`×`{W1,W3}`×`{LONG_INFO,TIGHT_UNINFO}`×`{910,911,912}` |
| `world_count/id_rule` | `8×4×3×2×2×3=1,152`；ID=`FPD60-{app}-{migration}-{risk}-{workload}-{profile}-{seed}` |
| `profiles` | `LONG_INFO:t0=180,τ=420,informative passive prefix`；`TIGHT_UNINFO:t0=420,τ=180,uninformative prefix`；具体trace在outcome前冻结 |
| `policies` | frozen Full、`No-PassiveInfo`、`No-D60`；均保留21-slot space、相同joint kernel、search cap、budget，除指定机制外不变 |
| `primary_family` | 2 contrasts×2 profiles×`{d∨r,s,C_op}`=12项Holm；app为最高paired unit |
| `mechanism_outputs` | D60选择率、首个后继action、belief change；不得用于改profile、threshold、utility或policy |
| `zero_cross_sets` | 与train、VAL-SELECT、VAL-CAL-POLICY、test主world、CodeTwin、三个ENUM tiers的world/template/trace/seed hashes全部零交叉 |
| `policy_hash/world_hash/trace_hash/zero_cross_report_hash` | 当前均`PENDING-IMPLEMENTATION` |

禁止字段：用ENUM结果选择profile、把D60 worlds写入loss/early stop/calibration、根据结果移动`t0`、不保留共同21-slot action mask、把尚未运行的机制方向写成事实。

## 10. Split、风险校准与 exact-enumeration 隔离

### 10.1 App 与 world 角色

- Train app 为 `A01..A06`。训练、first-action siblings 与 `ENUM-TRAIN` 只能使用这些 repository 的 train world。
- Validation app为`A07..A10`。`VAL-SELECT`只用于primitive validation、early stopping和hyperparameter选择。`VAL-CAL-POLICY`按`CAL-GEN-v1.2`无限iid simulator superpopulation独立抽样：app、该app内migration、九个validation risk configurations与`W0..W2`的weights依次为`1/4,1/4,1/9,1/3`；Philox root key、六component streams和draw indices均写入split manifest。checkpoint、五个threshold candidates、固定reference、utility、search与三项资格阈值冻结后才解封。
- Test app为`A11..A18`，共32项migration。八个app是有限benchmark的最高paired units；migration nested within app，motif作为固定effect，world/seed不能膨胀repository样本量。报告small-cluster、leave-one-app-out与app-level randomization敏感性，不声称现实repository总体外推。
- CodeTwin确认性primary只用`A11..A18`的480 worlds，`A01..A10`的600 worlds只作diagnostic；Shuffled只作source-sensitivity falsification。三者必须分别带`evaluation_role`，analysis loader拒绝混合。
- FULLPOLICY-D60只用9.13的1,152 held-out worlds与seeds`910..912`。它与主test、CodeTwin、calibration及ENUM均零交叉，且不能反向修改训练、threshold或冲突定义。
- `VAL-CAL-POLICY`只支持该generator superpopulation上frozen policy的边际harm和任务能力资格。它不产生history-conditional UCB，也不扩展到test held-out slices。

world-level seed 的实际整数清单必须在 builder 运行前写入 `split_manifest.json`。本草案只预留互斥 namespace：train=`T-*`、VAL-SELECT=`VS-*`、VAL-CAL-POLICY=`VC-*`、test=`TE-*`、ENUM-IDENTIFY=`EI-*`、ENUM-TRAIN=`ETR-*`、ENUM-TEST=`ETE-*`。这些是 ID namespace，不是已经生成的随机样本。

### 10.2 三个 exact tiers

| Tier | 计划 task | 可做的事 | 永久禁止的事 |
|---|---|---|---|
| `ENUM-IDENTIFY` | `D00-option-conflict-fixture`的M1–M4与`EI-000..009` | 先按outcome-blind selector冻结一个RS和一个CS slot，再检查四type可省略、顺序有物理差异及65序列可执行 | 产生训练label、进入任何结果总体或使用D00选择正式test case |
| `ENUM-TRAIN` | `A01-M1,A01-M4,A02-M3,A03-M2,A04-M1,A04-M4,A05-M3,A06-M2`与`ETR-000..009` | 每个start state用`enum-selector-v1`冻结RS/CS代表，与CP/WC构成四slots；枚举65个ordered subsets并由fixed-selector `π_ref`终止，向所有可比模型提供同一auxiliary partial ranking | 给另外14 slots或`D60/EX/AB`贴global label；称full oracle |
| `ENUM-TEST` | `A11-M1,A12-M2,A13-M3,A14-M4,A15-M1,A16-M2,A17-M3,A18-M4`与`ETE-000..009` | 在从未进入loss/early stop/calibration/conflict选择的records上报告四代表slots的fixed-continuation order regret与预注册reversal | 训练、调参、校准、改selector/conflict或报告完整policy oracle |

`65=Σ_{k=0}^4 4!/(4-k)!`只覆盖每个state由稳定hash冻结的四个代表slots。selector输入allowlist为app/migration ID、schema/contract hash、pre-state snapshot hash、opaque candidate order、行动前physical mask与tier seed；明确禁止repository/source/policy hash、observation/telemetry descendant、duration/cost、future/hidden seed、model score与sibling result，因此CodeTwin两侧selection相同。相同state的所有65条、siblings和methods必须得到同一selection。`D60`—expiry冲突仅用`heldout_fullpolicy_d60_ids`中的21-slot完整policy rollout，不进入三个ENUM tiers或`L_lat`。

### 10.3 Sibling sampling 的无裁量规则

`SIBLING-TRAIN-1.2`只在每个train world的`trajectory_slot=0`初始decision state分支一次。它从同一snapshot执行当时全部合法21 slots：`RS00..RS07,CS00..CS07,CP,WC,D60,EX,AB`。任一主动slot开始执行后，其operator type全部slots在continuation中失效。`π_ref`对每个尚未使用type以`SHA256("ref-selector-v1"||selector_state_hash||slot_id)`选最小合法代表，再按`SR<SV<CP<WC`继续；red则AB，时间不足则在mask-legal EX/AB中EX优先，两者皆非法才受控failure。不得按模型不确定性追加siblings或按资源/结果删除branch。2,880 worlds的上界仍为60,480条episodes；executor failure保留并服从runtime状态机。

## 11. 实现状态、hash 和可以声称的证据

本修补规格预指定18个app families、72项migration语义、8×16 visible checker结构、四类hidden oracle、五类split-isolated injection、operator阈值、CodeTwin invariants、十三类文件schema、runtime状态机与enumeration边界。它没有证明这些工件已经存在、task全部clean、D60有信息、operator effects可识别、排序反转、CodeTwin需要source、风险控制有效或主模型优于公平generic SMDP。

实现前后必须使用以下状态词，不得混用。

| 状态词 | 含义 |
|---|---|
| `PENDING-IMPLEMENTATION` | 只有本文件的候选语义，尚无对应 artifact/hash |
| `BUILT-UNVERIFIED` | artifact存在并有真实 hash，但尚未通过 isolation、clean-path和leakage tests |
| `VERIFIED-INSTANCE` | 单个 artifact 通过预注册自动检查；不代表候选设计冻结或结果成立 |
| `REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN` | 本版规格已修补；只有独立再红队可改变全局设计状态，且没有结果 |

所有实现 hash 在本文件版本中均保持字面值 `PENDING-IMPLEMENTATION`。后续 builder 应生成一个新实例版本写入真实值，不能回填本草案后声称早已冻结。

## 12. 肖老师 ISR 逐句逻辑与引用责任

本文件属于内部设计与隔离审计，不是正式论文正文。未来任何正式段落若使用这里的研究情境、字段任务、理论映射、算法机制或实验边界，必须与正文同步写入对应的 `逐段ISR对照记录.md`，并为**每一句**填写：

1. `00W_肖帅勇两篇ISR源行句段主键Manifest.md` 中可解析的段落主键和语法句 ID。
2. 分别填写`source_function_code`与`candidate_function_code`；主键可解析不等于功能同位。
3. 上一句建立的成立前提，以及源句自身的成立前提。
4. 源句与候选句各自唯一新增且可检验的命题。
5. 源句与候选句各自的展开、证据、因果、转折、限定、综合或推导关系。
6. 每个候选分句的文献事实、本文推论、方法定义或待实验预期，以及引用覆盖范围。
7. 源句与候选句各自的下一句后继义务。
8. 保留、改写、拆分、合并或删除的审计结论。

优先参照键必须写到语法句级，例如 ACAA 的 `ACAA-I3-S01..S04`、`ACAA-I4-S01..S06`、`ACAA-T6a-S01..S05`、`ACAA-T6b-S01..S04`、`ACAA-M10a-S01..S03`、`ACAA-M10b-S01..S07`，以及 DSDL 的 `DSDL-I6-S01..S05`、`DSDL-I7-S03..S08`、`DSDL-I9-S01..S07`、`DSDL-T2-S01..S07`、`DSDL-M15-S01..S06`、`DSDL-M17_18-S01..S04`、`DSDL-M19-S01..S02`、`DSDL-M20-S01..S10`、`DSDL-M21-S01..S05`、`DSDL-M22-S01..S03`、`DSDL-M23-S01..S03`、`DSDL-E11-S01..S02`、`DSDL-E12a-S01..S03`、`DSDL-E12b-S01..S05`、`DSDL-E13-S01..S03`、`DSDL-E14a-S01..S03` 和 `DSDL-E14b-S01..S04`。这里的范围只列出候选参照集合；正式审计中的每一句仍须读取源句后逐项比较`PRE→SRC_NEW→CAND_NEW→REL→CIT→NEXT→RESULT`。若前提、命题、关系、引用或后继义务不对应，必须写“无同功能锚点”并调整候选行文，不能把章节位置或主键可解析当成严格模仿。

引用责任同样逐分句处理。公开平台版本、数据库迁移能力、统计方法和理论机制必须回到一手全文；本文件定义的字段、阈值与 split属于待实现方法定义，不以外部引用伪装成经验事实。任何 outcome 数字只可连接真实 episode log、oracle record和统计脚本；实验前只能写设计、预注册预期或结果占位。

## 13. 自洽性核验与当前结论

本文件预注册的静态计数为：18个主app families、72项主migration、train/validation/test app数6/4/8、test migration数32、CodeTwin groups 36、twin variant instances 72、每app visible checkers 128、主动slots 18、总actions 21、每个ENUM start state四个代表slots与65条序列、FULLPOLICY-D60 held-out worlds 1,152，以及每个冻结policy合计9,928个互不重叠evaluation worlds。十三类实例文件均给出required schema和forbidden fields；所有待实现hash统一为`PENDING-IMPLEMENTATION`。

实现前必须通过以下自动核验，当前没有一项可被报告为已经运行。

- app、migration、field 和 enum mapping 的唯一性及 18×4 完整性。
- M1 identity、M2 rounding、M3 unknown/default 和 M4 recomputation 的 contract property tests。
- CS04/CS05每个set只有一个由公开repository policy参数化的可执行expected，checker不得同时含互斥expected constants；hidden oracle不import public policy或visible source。
- twins的snapshot、raw transactions、schema diff、migration contract、candidate/order、mask、visible checker和`t0_noncode_view_hash`逐字节相等；除公开policy file外source diff为空，No-Source denylist/taint检查为零泄漏。
- 第5.4节oracle mutation/clean matrix八项逐一满足预注册property；primary/diagnostic与Shuffled roles不可被analysis loader混用。
- train、VAL-SELECT、VAL-CAL-POLICY、test和三个 ENUM tier 的 group/hash零交叉。
- FULLPOLICY-D60恰有1,152个`FPD60-*` worlds，与全部其他tiers零交叉，两个profiles及seeds`910..912`不随结果变化。
- `A_M/A_N/A_T/A=18/19/2/21`、slot-order d_max=`120×8,120×8,210,60,60`、hard-start`t+d_max≤600`、每state selected slots=`1 RS+1 CS+CP+WC`、sequence count=65与split IDs完全一致。
- 01H的kernel shapes、action-invariant passage mixture、observable global codec、`kernel_measure_v1`、`PASSIVE-ADVANCE-v1`、passage/direct/tool/resource分解、event-after-action transition、十项causal tests及`GENERIC-QUOTA-v4`公平baseline接口在实现后逐项核验；当前只登记测试契约，不登记已通过。
- `MT-STATE-01..06`要求CP/WC不同typed fields保持可区分、same record跨posterior/model保持executor/ledger hash一致，在`t=590`拒绝全部nonterminal且不调用runner，并对Gold-03/04生成与truth table相同的passage全状态和`t=600` terminal-only bytes；不得把13维result退化为颜色别名。
- `MT-LEDGER-01..14`覆盖duplicate、interval split、reorder、retry、CP/terminal recovery、repair、anti-dilution、evidence-only、shadow isolation、policy-invariant`Ω_v`、single disposition、record/component一致、cross-model hash与z/h-order invariance；未运行前状态均为`PENDING-IMPLEMENTATION`。
- `CODEC-GOLD-01..08`覆盖half-even、overflow、NA/0、authority conflict、跨文件相同canonical CBOR/hash与runtime binding/hash、binding不改变cell likelihood但其ledger IDs进入post-state memo，以及tool no-reweight；`MEASURE-GOLD-01..09`除既有归一、training/belief/planning同cell bytes、`ξ=2/7/11`碰撞合并、首尾0.075 tail mass、duration atoms、terminal/nonterminal同codec、terminal cell risk与proper NLL外，还以跨absolute-time bin反例核验解析expected、16-mask归一、stable binary64 event law、GL64/GL128/ref256三项误差、unit fork与center rejection；`HORIZON-GOLD-01..04`覆盖`t=590`、exact d_max结束、Gold-03 passage与Gold-04无deadline边界；`CLONE-GOLD-01..03`覆盖无live alias。
- `generic_quota_v4.json`在label解封前唯一记录有限域argmin；核验脚本必须证明参数完全相同、21个root action的train/infer MAC差均不超过0.5%、seed/tuple/hash重算bytes一致，且inputs、labels、actions、updates、optimizer、tool与search预算没有变小。
- risk template source在 split间不相同，activation不依赖模型输出。
- operator threshold schema与第 8 节一致，missing/timeout不能变 green。
- test八个synthetic repository families作为八个最高paired units，migration nested within app、motif fixed，并报告small-cluster与leave-one-app-out。
- 任一正式论文句子的 `00W` 精确键、逻辑承接和分句引用责任均有同步审计条目。

因此，本文件的当前状态只能是：**REPAIRED-v5 / INDEPENDENT RE-REDTEAM PENDING / RESULTS NOT RUN**。它登记了字段级修补，不自行关闭设计门，不宣称环境可运行，也不提前确认任何经验贡献。
