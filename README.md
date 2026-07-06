# qual-llm-check-construct

用两个 LLM 独立筛选 AIS 文献，判断每条记录是否与「develop a construct / constructs」相关，并把每次筛选隔离在单独的 run 目录中。每个 run 目录包含源 CSV 副本、模型配置、提示词、进度文件和结果文件，后续做引文分析时可以直接追溯同一批输入和筛选结论。

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
uv run python main.py init --run-dir runs/construct_development_ais --input construct_all_AIS_basket.csv
```

4. 可选：预览英文提示词，不调用 API：

```powershell
uv run python main.py preview --run-dir runs/construct_development_ais --examples 1
```

5. 执行筛选：

```powershell
uv run python main.py run --run-dir runs/construct_development_ais
```

只测试少量记录：

```powershell
uv run python main.py run --run-dir runs/construct_development_ais --limit 10
```

断点续跑时直接再次运行同一命令即可。程序会读取 `progress.jsonl` 跳过已完成记录。若要从头重跑：

```powershell
uv run python main.py run --run-dir runs/construct_development_ais --reset
```

## Run 目录结构

初始化后会得到类似结构：

```text
runs/construct_development_ais/
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
| `all_screened.csv` | 所有成功筛选记录，含两个模型的判断列 |
| `included_consensus.csv` | 两个模型都判断为相关的记录 |
| `model_disagreements.csv` | 两个模型结论不一致的记录 |
| `progress.jsonl` | 行级完成记录，用于断点续跑 |
| `model_decisions.jsonl` | 模型级原始判断，保留 raw response |
| `errors.jsonl` | 多次重试后失败的记录；未写入进度，下次会重试 |

新建 run 默认使用 `row_key_mode: id_with_row_number`，即把 `EID` 和 CSV 行号一起作为断点 key，避免源数据里重复 `EID` 时影响断点续跑。

## 双模型配置

`config.json` 默认启用两个模型：

- `deepseekv4pro`: `deepseek-v4-pro`，默认读取 `NEW_API_KEY` 和 `NEW_API_BASE_URL`；
- `gpt-5-5`: `gpt-5.5`，默认同样读取 `NEW_API_KEY` 和 `NEW_API_BASE_URL`。

如需换模型、base URL、超时、最大输出 token 或并发数，只改对应 run 目录里的 `config.json`，不需要修改脚本。

程序对每条记录使用同一套提示词分别调用两个模型。只有两个模型都成功返回后，才写入该行的共识结果：

- `screen_relevant_consensus=true`: 两个模型都认为相关；
- `screen_agreement=false`: 两个模型结论不一致，会进入 `model_disagreements.csv`；
- 某模型失败：写入 `errors.jsonl`，该行不写入 `progress.jsonl`，下次续跑会重新尝试。

## 常用命令

查看帮助：

```powershell
uv run python main.py --help
uv run python main.py init --help
uv run python main.py preview --help
uv run python main.py run --help
```

只检查数据和待处理数量，不调用 API：

```powershell
uv run python main.py run --run-dir runs/construct_development_ais --dry-run
```

## 筛选标准摘要

相关文献通常是把「构念」本身作为实质贡献：提出、定义、概念化、重新概念化、精炼、操作化、测量或验证一个或一组 theoretical constructs。包括构念维度、边界、量表、测量条目和工具开发。

不相关文献通常只是使用已有构念作为变量、检验构念之间的关系、提出一般框架/模型/命题但没有清楚发展构念，或只是顺带出现 construct、framework、model、measure 等词。
