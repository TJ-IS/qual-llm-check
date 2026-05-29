# qual-llm-check

用 DeepSeek 官方 API 和 LangChain 对文献题名与摘要进行筛选，判断每条记录是否涉及「用生成式 AI 去辅助定性分析」。相关记录会被追加保存到 `llm_qual_abs_relevant.csv`。

## 文件结构

```text
.
├── .env                              # 本地 API 配置，不提交
├── .env.example                      # 环境变量示例
├── .gitignore                        # 忽略 .env、CSV、JSONL、日志、虚拟环境等文件
├── .python-version                   # uv 使用的 Python 版本
├── README.md                         # 项目说明
├── main.py                           # 文献筛选主程序
├── translate_csv_zh.py               # 将 CSV 的 Title + Abstract 翻译成中文并新增 zh 列
├── pyproject.toml                    # 项目依赖配置
├── uv.lock                           # uv 锁定依赖版本
├── llm_qual_abs_all.csv              # 输入数据，Scopus 导出的全部题录
├── llm_qual_abs_relevant.csv         # 输出数据，仅保存判断为相关的行
├── llm_qual_abs_relevant_zh.csv      # 中文翻译输出，多一列 zh
└── llm_qual_abs_relevant.progress.jsonl
                                      # 逐行进度记录，用于断点续跑
```

运行失败且某些行重试后仍不可用时，会额外生成：

```text
llm_qual_abs_relevant.errors.jsonl    # 错误记录，包含行号、row_key、标题和错误信息
```

## 示例检索式

```text
( TITLE-ABS-KEY ( "large language model" OR "generative AI" OR "generative artificial intelligence" ) AND TITLE-ABS-KEY ( "qualitative study" OR "grounded theory" ) )
```

## 快速上手

1. 安装依赖：

```powershell
uv sync
```

2. 配置 `.env`，这里只放 API Key 和 base URL，不在 `.env` 里配置模型：

```env
NEW_API_KEY=你的 DeepSeek API Key
NEW_API_BASE_URL=https://api.deepseek.com
```

3. 先做一次 dry-run，检查 CSV、编码、列名和断点状态：

```powershell
uv run python main.py --dry-run --limit 5
```

4. 正式运行：

```powershell
uv run python main.py --model deepseek-v4-pro --max-concurrency 4
```

5. 如果需要从头重新生成结果：

```powershell
uv run python main.py --model deepseek-v4-pro --max-concurrency 4 --reset
```

默认会读取 `llm_qual_abs_all.csv`，判断 `Title` 和 `Abstract` 合并后的内容是否相关，并把相关行追加到 `llm_qual_abs_relevant.csv`。输入和输出默认都使用 `utf-8-sig`，适合 Windows 和 Excel 场景，避免中文乱码和 BOM 问题。

## 断点续跑

程序每完成一行都会写入 `llm_qual_abs_relevant.progress.jsonl`。如果运行中断，再次执行同一命令时会跳过已经处理过的行。

不要加 `--reset`，并继续显式指定模型：

```powershell
uv run python main.py --model deepseek-v4-pro --max-concurrency 4
```

加 `--reset` 会删除已有输出、进度和错误文件，然后重新开始。

## 参数讲解

| 参数 | 默认值 | 作用 |
| --- | --- | --- |
| `--input` | `llm_qual_abs_all.csv` | 输入 CSV 路径 |
| `--output` | `llm_qual_abs_relevant.csv` | 相关文献输出 CSV 路径 |
| `--progress` | `llm_qual_abs_relevant.progress.jsonl` | 逐行进度文件，用于断点续跑 |
| `--errors` | `llm_qual_abs_relevant.errors.jsonl` | 错误日志文件 |
| `--env-file` | `.env` | 环境变量文件 |
| `--api-key-env` | `NEW_API_KEY` | API Key 对应的环境变量名 |
| `--base-url-env` | `NEW_API_BASE_URL` | API base URL 对应的环境变量名 |
| `--base-url` | 空 | 直接覆盖 API base URL |
| `--model` | `deepseek-v4-pro` | 使用的模型名。模型只通过命令行参数指定，不从 `.env` 读取 |
| `--title-column` | `Title` | 标题列名 |
| `--abstract-column` | `Abstract` | 摘要列名 |
| `--id-column` | `EID` | 稳定 ID 列名，缺失时会用标题和摘要生成哈希 |
| `--encoding` | `utf-8-sig` | CSV 输入和输出编码 |
| `--max-concurrency` | `4` | 并发 API 请求数 |
| `--retries` | `3` | 每行失败后的重试次数 |
| `--retry-base-delay` | `2.0` | 指数退避的初始等待秒数 |
| `--timeout` | `90.0` | 单次 API 请求超时时间，单位秒 |
| `--max-tokens` | `220` | 模型最大输出 token 数 |
| `--limit` | 空 | 只处理指定数量的待处理行，适合测试 |
| `--offset` | `0` | 跳过输入 CSV 前 N 行数据 |
| `--reset` | 关闭 | 删除已有输出、进度、错误文件后重跑 |
| `--dry-run` | 关闭 | 只检查数据和待处理数量，不调用 API |

## 常用命令

只测试前 10 条：

```powershell
uv run python main.py --model deepseek-v4-pro --limit 10 --max-concurrency 1 --reset
```

提高并发：

```powershell
uv run python main.py --model deepseek-v4-pro --max-concurrency 8
```

指定其他输入输出文件：

```powershell
uv run python main.py --model deepseek-v4-pro --input other.csv --output relevant.csv
```

查看帮助：

```powershell
uv run python main.py --help
```

## 翻译相关文献

`translate_csv_zh.py` 默认读取 `llm_qual_abs_relevant.csv`，把每行的 `Title` 和 `Abstract` 合并后用 Google Translate 翻译成中文，并写入新增的 `zh` 列。默认输出文件名是在输入文件名后加 `_zh`，例如 `llm_qual_abs_relevant_zh.csv`。

运行默认翻译：

```powershell
uv run python translate_csv_zh.py
```

指定输入输出文件：

```powershell
uv run python translate_csv_zh.py --input relevant.csv --output relevant_zh.csv
```

只测试前 3 行：

```powershell
uv run python translate_csv_zh.py --limit 3 --max-workers 1
```

提高并发：

```powershell
uv run python translate_csv_zh.py --max-workers 4
```

常用参数：

| 参数 | 默认值 | 作用 |
| --- | --- | --- |
| `--input` | `llm_qual_abs_relevant.csv` | 输入 CSV 路径 |
| `--output` | 自动生成 `_zh.csv` | 输出 CSV 路径 |
| `--title-column` | `Title` | 标题列名 |
| `--abstract-column` | `Abstract` | 摘要列名 |
| `--zh-column` | `zh` | 中文翻译列名 |
| `--encoding` | `utf-8-sig` | CSV 输入和输出编码 |
| `--source-lang` | `auto` | 源语言 |
| `--target-lang` | `zh-CN` | 目标语言 |
| `--max-workers` | `4` | 行级并发翻译线程数 |
| `--chunk-size` | `4500` | 单个翻译片段最大字符数，低于 GoogleTranslator 的 5000 字符限制 |
| `--retries` | `3` | 每个片段失败后的重试次数 |
| `--retry-delay` | `1.5` | 重试等待基准秒数 |
| `--limit` | 空 | 只翻译前 N 行，适合测试 |

## 筛选标准

判断依据是 `Title` 和 `Abstract` 合并后的内容。

相关文献通常包括：

- 使用、评估、提出或讨论生成式 AI、LLM、ChatGPT、GPT 类工具辅助定性编码；
- 使用生成式 AI 辅助 thematic analysis、content analysis、grounded theory analysis；
- 使用生成式 AI 处理访谈、焦点小组、开放题回答、社交媒体文本等定性资料；
- 讨论 LLM 在定性分析中的可靠性、工作流、比较、风险或方法论影响。

不相关文献通常包括：

- 只是用定性研究方法调查人们对 AI 的看法；
- 只是讨论 AI 在临床、教育、软件工程等场景中的采用或影响；
- 使用传统机器学习、NLP 或文本挖掘，但没有生成式 AI 辅助定性分析；
- LLM 评测、聊天机器人、自动摘要、定理理解等与定性分析无关的研究。

## 实现说明

`main.py` 使用 `langchain-openai` 的 `ChatOpenAI` 连接 DeepSeek 官方 OpenAI-compatible API。程序要求模型返回 JSON，并解析其中的 `relevant`、`confidence` 和 `reason` 字段。

为了降低长任务中断风险，程序采用逐步保存：

- 判断为相关的行会立即追加写入输出 CSV；
- 每个成功判断都会立即写入 progress JSONL；
- 失败行会写入 errors JSONL；
- 每次写入后都会 flush 并 fsync，尽量避免异常退出造成已完成结果丢失。
