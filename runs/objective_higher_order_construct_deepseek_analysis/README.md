# Objective Higher-Order Construct Screening

This run screens the already harvested Otero `construct` full-text corpus for papers that do all of the following:

1. explicitly treat a named theoretical concept as a `construct`;
2. give it at least two conceptually distinct lower-order dimensions, facets, components, or subconstructs;
3. measure every component with objective, non-questionnaire evidence; and
4. actually aggregate or estimate those components as one value of the same construct.

The paper does not need to call the construct `higher-order` or claim to develop it. A plain index or prediction score is excluded unless the paper explicitly identifies the target concept as a construct. Parallel regressors, dimension-by-dimension tests, multidimensional neural-network inputs, and merely suggested future aggregation are also excluded.

The implementation reuses the tested request, chunking, retry, and checkpoint engine from `runs/new_construct_objective_measurement_deepseek_analysis`, while keeping its prompts, schema, output, and prompt fingerprint independent.

## Refresh the Otero baseline

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\.agents\skills\otero-open-api\scripts\download_fulltext.py' --query construct --output database_fulltext_construct
```

## Dry run

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\objective_higher_order_construct_deepseek_analysis\analyze_high_order_construct.py' --dry-run --limit 3
```

## Small calibration run

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\objective_higher_order_construct_deepseek_analysis\analyze_high_order_construct.py' --output-dir '.\runs\objective_higher_order_construct_deepseek_analysis\output_sample' --file '14774_*' --file '00044_*' --file '25442_*' --file '00196_*' --max-concurrency 2
```

## Full resumable run

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\objective_higher_order_construct_deepseek_analysis\analyze_high_order_construct.py'
```

Each successful response is appended and flushed immediately to `output/decisions.jsonl`. Re-running the same command skips articles completed with the current model and prompt fingerprint, and retries unfinished or failed articles. `decisions.csv` is the readable flat report; the complete candidate evidence remains in JSONL.

To monitor the background run started from Codex:

```powershell
Get-Content -Encoding UTF8 '.\runs\objective_higher_order_construct_deepseek_analysis\output\run.resume.stdout.log' -Tail 20 -Wait
```

The current completed count can be checked without following the log:

```powershell
(Get-Content -Encoding UTF8 '.\runs\objective_higher_order_construct_deepseek_analysis\output\decisions.jsonl' | Where-Object { $_.Trim() }).Count
```
