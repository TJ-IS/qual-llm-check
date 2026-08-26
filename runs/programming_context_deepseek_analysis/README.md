# Programming Context Full-Text Screening

This independent DeepSeek V4 Pro batch screens all Markdown full texts for substantive programming research contexts. It excludes mathematical programming, researcher implementation code, qualitative coding, generic software use, and incidental terminology.

For matching papers it extracts a Chinese content summary, the article-specific boundary of programming, independent/mediating/moderating/dependent variables, theory names, research method, and the relationship to situation awareness. The first two and last two narrative fields are mandatory for every match. Situation-awareness relations distinguish explicit use, conceptual relation, and no relation.

All full texts are first sent in one request. Chunking is only an automatic fallback after an actual context-length error or when `--force-chunk` is specified. Results are appended immediately and the same command resumes completed records with the current prompt fingerprint.

## Calibration

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\programming_context_deepseek_analysis\analyze_programming_context.py' --limit 5 --max-concurrency 5
```

## Full run

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\programming_context_deepseek_analysis\analyze_programming_context.py' --max-concurrency 12
```

The full batch writes all decisions to `output_v1_fresh/decisions.jsonl` and `decisions.csv`. Matching articles are additionally exported to `programming_context_matches.csv`.

