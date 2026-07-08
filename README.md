# qual-llm-check-coding-agent-ux

用两个独立 LLM 调用筛选 MISQ/ISR 文献，判断每条记录里是否有适合被我们改造成「coding agent 个体用户体验」概念、构念或量表的素材。当前默认任务采取开放式概念发现取向：只要文章包含一个个体 UX 概念或现象，并且它迁移到 coding agent 时有明显不匹配、同时对应重要现实问题，就可以纳入。文章本身不需要做构念开发，也不需要指导我们如何改造。

每次筛选隔离在单独的 run 目录中。run 目录包含源 CSV 副本、模型配置、提示词、进度文件和结果文件，后续可以直接追溯同一批输入和筛选结论。

## 快速流程

1. 安装依赖：

```powershell
uv sync
```

2. 配置 `.env`：

```env
NEW_API_KEY=你的 DeepSeek API Key
NEW_API_BASE_URL=https://api.deepseek.com
```

3. 新建一次筛选运行：

```powershell
uv run python main.py init --run-dir runs/coding_agent_ux_misq_isr --input all_MISQ_ISR.csv
```

4. 预览英文提示词，不调用 API：

```powershell
uv run python main.py preview --run-dir runs/coding_agent_ux_misq_isr --examples 1
```

5. 先测试少量记录：

```powershell
uv run python main.py run --run-dir runs/coding_agent_ux_misq_isr --limit 10
```

6. 确认提示词效果后执行全量筛选：

```powershell
uv run python main.py run --run-dir runs/coding_agent_ux_misq_isr
```

断点续跑时直接再次运行同一命令即可。程序会读取 `progress.jsonl` 跳过已完成记录。若要从头重跑：

```powershell
uv run python main.py run --run-dir runs/coding_agent_ux_misq_isr --reset
```

## Run 目录结构

初始化后会得到类似结构：

```text
runs/coding_agent_ux_misq_isr/
├── config.json
├── source.csv
├── system_prompt.md
├── user_prompt_template.md
├── all_screened.csv
├── included_consensus.csv
├── model_disagreements.csv
├── progress.jsonl
├── model_decisions.jsonl
└── errors.jsonl
```

关键文件：

| 文件 | 作用 |
| --- | --- |
| `config.json` | 模型、列名、并发和输出文件 |
| `source.csv` | 本次 run 使用的输入文件副本 |
| `system_prompt.md` | 英文系统提示词，可在运行前审阅和修改 |
| `user_prompt_template.md` | 英文用户提示词模板，可引用 CSV 字段 |
| `all_screened.csv` | 所有成功筛选记录，含两个 reviewer 的判断列 |
| `included_consensus.csv` | 两个 reviewer 都判断为相关的记录 |
| `model_disagreements.csv` | 两个 reviewer 结论不一致的记录 |
| `progress.jsonl` | 行级完成记录，用于断点续跑 |
| `model_decisions.jsonl` | 模型级原始判断，保留 raw response |
| `errors.jsonl` | 多次重试后失败的记录；未写入进度，下次会重试 |

新建 run 默认使用 `row_key_mode: id_with_row_number`，即把 `EID` 和 CSV 行号一起作为断点 key，避免源数据里重复 `EID` 时影响断点续跑。

## 双模型配置

`config.json` 默认启用两个 reviewer，两个都调用 DeepSeek V4 Pro：

- `deepseekv4pro_reviewer_1`: `deepseek-v4-pro`
- `deepseekv4pro_reviewer_2`: `deepseek-v4-pro`

两个 reviewer 使用不同名称，方便保留独立判断和一致性结果。默认都读取 `NEW_API_KEY` 和 `NEW_API_BASE_URL`。如需换模型、base URL、超时、最大输出 token 或并发数，只改对应 run 目录里的 `config.json`。

程序对每条记录使用同一套提示词分别调用两个 reviewer。只有两个 reviewer 都成功返回后，才写入该行的共识结果：

- `screen_relevant_consensus=true`: 两个 reviewer 都认为相关；
- `screen_agreement=false`: 两个 reviewer 结论不一致，会进入 `model_disagreements.csv`；
- 某个 reviewer 失败：写入 `errors.jsonl`，该行不写入 `progress.jsonl`，下次续跑会重新尝试。

## 输出判读

每个 reviewer 会输出：

- `relevant`: 是否纳入；
- `confidence`: 置信度；
- `decision_label`: 纳入/排除原因标签；
- `fit_level`: strong、moderate、weak 或 none；
- `source_concept`: 文章中可被改造的原始概念或现象；
- `candidate_coding_agent_ux_concept`: 可能改造成的 coding-agent UX 概念名；
- `ux_topic`: 对应的宽泛 UX 话题类别；
- `adaptation_potential`: 改造潜力高低；
- `practical_importance`: 这个概念为什么在真实 coding agent 使用中重要；
- `uniqueness_rationale`: 为什么这个概念迁移到 coding agent 时有独特性或不匹配；
- `evidence`: 来自标题、摘要或关键词的简短证据；
- `reason`: 一句话解释。

## 筛选标准摘要

当前焦点不是一个固定构念，而是开放寻找 coding-agent-specific UX concept opportunities。coding agent 的特殊性在于它不只是聊天、推荐或补全，而是会在可执行、持续变化的代码环境中理解上下文、调用工具、修改产物、跨步骤推进任务，并留下需要用户审查和承担责任的 diff、test、log、commit、PR 等痕迹。

相关文献可以是直接研究 AI coding/coding agent/developer experience 的文章，也可以是相邻的人机交互或 IS 文章。关键不是文章是否已经开发构念，而是它是否包含一个值得被我们改造的个体 UX 概念或现象，并且这个概念对应 coding agent 使用中的重要现实问题。典型候选方向包括但不限于委托与控制、行动边界、上下文对齐、验证负担、证据可追溯性、主动性与打断、共同能动性、责任归属、学习/去技能化、认知卸载、信任校准和开发者心流。

不相关文献通常只是 firm/market/platform 层面的文章、纯方法论文、一般组织治理或职业市场研究，或者只有泛泛的技术采用/生产率讨论但没有个体 UX 概念、没有 coding-agent-specific 不匹配、或缺乏重要现实意义。
