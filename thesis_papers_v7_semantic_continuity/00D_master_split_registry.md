# v7 跨篇 master split registry 规范

## 规范实体键

在生成任何 trajectory、contract label、patch、动态 episode 或确认性结果前，建立 append-only registry。静态任务键为

`(canonical_upstream, repo_family_id, base_commit, normalized_issue_hash, data_snapshot_hash)`；

动态事件键为

`(source_family_id, transition_event_id, event_time, upstream_version_hash, downstream_pipeline_hash)`。

`repo_family_id` 合并 upstream/fork/mirror、共享提交祖先、规范包名与源码 MinHash 高相似项目；`source_family_id` 合并同一数据生产机构、同一生成系统和镜像发布源。issue、patch hunk、relational-IR、contract、input-world、property/mutation-generator family 与 output hash 用于任务级近重复边。

## 角色

每条实体记录 `paper_id`、`role∈{pilot,train,development,calibration,confirmatory,sealed,temporal-test,auxiliary-only}`、dataset/release、许可、时间戳、代码/数据/容器/evaluator hash 和 exclusion reason。角色只允许按预先登记的迁移表改变，并保留旧值与操作者。

## 跨篇隔离

任一 repo/source family 一旦在某篇承担 confirmatory、sealed 或 temporal-test，即成为 `global-sealed`，不得进入另两篇的 pilot、train、development、calibration 或 auxiliary heads。共享 benchmark 基础设施可以，但重复 family/task 的结果只算相关多终点测量，不能宣称独立复制。

论文一的确认性 family、论文二的固定快照确认性 family 与论文三的动态 source/transition family必须互斥。相同真实 upstream transition 的不同 downstream pipeline、窗口、动作分支或随机种子必须处于同一外层折，并只计为一个独立 event cluster；同一静态任务的不同 feedback arm 必须处于同一折。任何 checkpoint、adapter、calibrator、trajectory、candidate patch、hidden contract、future window 或 outcome 不跨篇传递。

## 时间外测

论文三按事件时间封存未来窗口；窗口边界在任何结果或事件内容可见前签名，并将确认集明确分为“已见来源族的较晚事件”与“整来源族未见”的 time-out/source-out strata。论文一和二如使用后来发布的新任务，须与论文三 source families 互斥。动态 replay 的训练只能读取决策时点及此前的源数据、代码与反馈，后续窗口仅由 evaluator 读取。论文三的行为日志须同时保存稳定 raw action ID、冻结动作特征、feature-cell、可行性检查、已知 propensity 与支持判定；raw ID 首次出现不等于 feature OOV，含 `raw-new-ID` 的在线轨迹须与 IQL/OPE 样本分开登记。

## 共享基础设施

允许共享冻结 parser、SQL/dbt resolver、relation/lineage extractor、container runner、property-world generator 与五维契约 schema，但必须记录版本和 hash。property-world 与 mutation generator 的家族和组合须继承外层 split，不能以同一生成模板跨折派生近重复任务。共享基础设施不能含在任一篇训练得到的参数，也不能编码 hidden test、gold patch 或未来 transition outcome；论文二的确认性 evaluator team 与训练标注团队隔离，其裁决只在封存评价时解封。
