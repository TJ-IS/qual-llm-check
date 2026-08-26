# Independently Reproducible Method Screening

Version 16 screens only papers published from 2017 through 2026. It returns one article-level boolean for low-barrier individual-level applicability, an independent boolean for large-scale compute, and independent tags for pure survey, pure interview, and experiment designs.

There are no scores, method allowlists, or commonness ranking. Surveys and interviews remain eligible when they satisfy the low-barrier and individual-level requirements. `has_pure_survey`, `has_pure_interview`, and `has_experiment` are classification tags and never affect qualification. A true result contains the name and a short Chinese overview of one representative qualifying method. A false result contains only the decisive exclusion reason. `uses_large_scale_compute` also never affects the low-barrier decision.

All current full texts are sent in one request. The largest article in the 13,910-file library is 472,497 characters, and `direct_max_chars` is disabled with `null`. Chunking is retained only as an automatic fallback after an actual context-length error or when `--force-chunk` is explicitly used.

## Dry run

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\low_barrier_scalable_methods_deepseek_analysis\analyze_methods.py' --dry-run --limit 3
```

## Full resumable run

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\low_barrier_scalable_methods_deepseek_analysis\analyze_methods.py' --max-concurrency 12
```

Successful v16 records are appended immediately to `output_v16_2017_2026_fresh/decisions.jsonl`. The 2017–2026 scope contains 3,961 full texts. This directory starts empty and is separate from the historical outputs. Re-running the same command skips records completed under the current v16 prompt fingerprint.

## Full resumable run for papers published through 2016

```powershell
$env:PYTHONIOENCODING = 'utf-8'
& '.\.venv\Scripts\python.exe' -B '.\runs\low_barrier_scalable_methods_deepseek_analysis\analyze_methods.py' --config 'config_v16_through_2016.json' --max-concurrency 12
```

This older-paper batch writes only to `output_v16_through_2016_fresh/`, so it does not mix with the completed 2017–2026 output. Re-running the command resumes from successful records already written under the same prompt fingerprint.

No v16 model run should be started until the user confirms the prompt wording.
