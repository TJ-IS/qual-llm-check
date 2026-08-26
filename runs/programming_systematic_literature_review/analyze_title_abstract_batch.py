#!/usr/bin/env python3
"""Batch title/abstract screening with strict per-record completeness checks."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv


RUN_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG_PATH = RUN_DIR / "config_batch.json"
WRAPPER_PATH = RUN_DIR / "analyze_title_abstract.py"
SPEC = importlib.util.spec_from_file_location("programming_slr_batch_schema", WRAPPER_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load schema module from {WRAPPER_PATH}")
SCHEMA = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SCHEMA
SPEC.loader.exec_module(SCHEMA)
ENGINE = SCHEMA.ENGINE


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_from_run(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (RUN_DIR / path).resolve()


def fingerprint(config: dict[str, Any], system_prompt: str) -> str:
    payload = {
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "system_prompt": system_prompt,
    }
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()


def chunks(items: list[Any], size: int) -> list[list[Any]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def batch_user_prompt(articles: list[Any]) -> str:
    records = [
        {
            "record_id": f"R{index:03d}",
            "title": article.title,
            "authors": article.authors,
            "year": article.year,
            "source": article.journal,
            "doi": article.doi,
            "title_abstract_keywords": article.fulltext,
        }
        for index, article in enumerate(articles, start=1)
    ]
    return (
        "请逐篇独立筛选下列题名、摘要和关键词记录。检索渠道不是相关性证据；"
        "每篇都必须在 results 中恰好返回一次。\n\n"
        f"<RECORDS>\n{json.dumps(records, ensure_ascii=False)}\n</RECORDS>"
    )


def analyze_batch(
    articles: list[Any],
    config: dict[str, Any],
    system_prompt: str,
    clients: Any,
    prompt_fingerprint: str,
) -> list[dict[str, Any]]:
    model = config["model"]
    batch_config = config["batch"]
    payload, usage = ENGINE.request_json(
        clients,
        str(model["name"]),
        system_prompt,
        batch_user_prompt(articles),
        int(model["max_tokens"]),
        int(batch_config["retries"]),
        float(batch_config["retry_base_delay"]),
    )
    raw_results = payload.get("results")
    if not isinstance(raw_results, list):
        raise ValueError("batch response must contain a results list")
    by_id: dict[str, dict[str, Any]] = {}
    for raw in raw_results:
        if not isinstance(raw, dict):
            raise ValueError("each result must be an object")
        record_id = str(raw.get("record_id") or "").strip()
        if not record_id or record_id in by_id:
            raise ValueError(f"missing or duplicate record_id: {record_id!r}")
        by_id[record_id] = raw
    expected_ids = [f"R{index:03d}" for index in range(1, len(articles) + 1)]
    expected = set(expected_ids)
    if set(by_id) != expected:
        missing = sorted(expected - set(by_id))
        extra = sorted(set(by_id) - expected)
        raise ValueError(f"batch record mismatch; missing={missing}, extra={extra}")

    per_record_usage = {
        key: int(value) // len(articles) for key, value in usage.items()
    }
    records: list[dict[str, Any]] = []
    for article, response_id in zip(articles, expected_ids):
        raw_decision = dict(by_id[response_id])
        if config.get("lean_output") is True:
            label = str(raw_decision.get("screening_label") or "").strip().lower()
            reason = str(raw_decision.get("decision_reason_cn") or "").strip()
            raw_decision.setdefault(
                "study_type", "not_applicable" if label == "exclude" else "unclear"
            )
            raw_decision.setdefault(
                "unit_of_analysis", "not_applicable" if label == "exclude" else "unclear"
            )
            raw_decision.setdefault("theory_or_framework_names", [])
            if label == "exclude":
                raw_decision["research_summary_cn"] = ""
            elif not str(raw_decision.get("research_summary_cn") or "").strip():
                raw_decision["research_summary_cn"] = (
                    reason
                    or str(raw_decision.get("metadata_evidence_cn") or "").strip()
                    or "题录显示为直接编程候选"
                )
        decision = SCHEMA.normalize_final(raw_decision)
        records.append(
            {
                **ENGINE.article_metadata(article),
                "analysis_version": str(config["analysis_version"]),
                "prompt_fingerprint": prompt_fingerprint,
                "model": str(model["name"]),
                "analysis_mode": "title_abstract_batch_request",
                "fulltext_chars": len(article.fulltext),
                "chunk_count": 1,
                "context_length_fallback": False,
                "completed_at": utc_now(),
                **decision,
                "usage": per_record_usage,
            }
        )
    return records


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Batch config JSON; relative paths resolve from the current directory",
    )
    parser.add_argument("--output-dir", type=Path, help="Override configured output")
    parser.add_argument(
        "--file", action="append", help="Exact filename or glob; repeatable"
    )
    parser.add_argument("--limit", type=int, help="Maximum pending records in this run")
    parser.add_argument("--batch-size", type=int, help="Records per API request")
    parser.add_argument("--max-concurrency", type=int, help="Concurrent API requests")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    if args.batch_size is not None and not 1 <= args.batch_size <= 16:
        parser.error("--batch-size must be between 1 and 16")
    if args.max_concurrency is not None and not 1 <= args.max_concurrency <= 16:
        parser.error("--max-concurrency must be between 1 and 16")
    return args


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    config = read_config(config_path)
    input_dir = resolve_from_run(str(config["input_dir"]))
    output_dir = (
        args.output_dir.resolve()
        if args.output_dir is not None
        else resolve_from_run(str(config["output_dir"]))
    )
    env_file = resolve_from_run(str(config["env_file"]))
    system_prompt = (
        (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
        + "\n\n"
        + (RUN_DIR / config["prompt_files"]["batch_append"])
        .read_text(encoding="utf-8")
        .strip()
    )
    prompt_fingerprint = fingerprint(config, system_prompt)
    all_files = sorted(input_dir.glob("*.md"))
    selected_files = ENGINE.select_files(input_dir, args.file)
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    previous = ENGINE.load_jsonl_by_file(decisions_path)
    decisions = {
        name: record
        for name, record in previous.items()
        if record.get("prompt_fingerprint") == prompt_fingerprint
    }
    pending_files = [path for path in selected_files if path.name not in decisions]
    if args.limit is not None:
        pending_files = pending_files[: args.limit]
    batch_size = args.batch_size or int(config["batch"]["records_per_request"])
    pending_batches = chunks(pending_files, batch_size)
    print(
        f"Input records: {len(all_files)}; selected: {len(selected_files)}; "
        f"completed current prompt: {len(decisions)}; "
        f"stale: {len(previous) - len(decisions)}; pending: {len(pending_files)}; "
        f"requests: {len(pending_batches)}; batch_size: {batch_size}",
        flush=True,
    )
    print(f"Output directory: {output_dir}", flush=True)
    if args.dry_run:
        for group in pending_batches[:3]:
            print("DRY RUN", [path.name for path in group], flush=True)
        return 0
    if not pending_batches:
        output_dir.mkdir(parents=True, exist_ok=True)
        SCHEMA.write_reports(
            output_dir,
            all_files,
            decisions,
            str(config["analysis_version"]),
            prompt_fingerprint,
        )
        print("Nothing to do.", flush=True)
        return 0

    load_dotenv(env_file)
    model = config["model"]
    api_key = os.getenv(str(model["api_key_env"]))
    if not api_key:
        raise RuntimeError(f"API key not found: {model['api_key_env']}")
    base_url = os.getenv(str(model["base_url_env"])) or str(model["base_url"])
    clients = ENGINE.ThreadClients(api_key, base_url, float(model["timeout"]))
    max_concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    output_dir.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    completed_now = 0
    failed_batches = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_concurrency) as pool:
        futures = {
            pool.submit(
                analyze_batch,
                [ENGINE.load_article(path) for path in group],
                config,
                system_prompt,
                clients,
                prompt_fingerprint,
            ): group
            for group in pending_batches
        }
        for future in concurrent.futures.as_completed(futures):
            group = futures[future]
            try:
                records = future.result()
                for record in records:
                    ENGINE.append_jsonl(decisions_path, record)
                    decisions[record["source_file"]] = record
                completed_now += len(records)
                candidate_count = sum(
                    record["screening_label"] != "exclude" for record in records
                )
                print(
                    f"[{completed_now}/{len(pending_files)}] OK batch={len(records)} "
                    f"candidates={candidate_count}",
                    flush=True,
                )
            except Exception as exc:
                failed_batches += 1
                ENGINE.append_jsonl(
                    errors_path,
                    {
                        "source_files": [path.name for path in group],
                        "failed_at": utc_now(),
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "prompt_fingerprint": prompt_fingerprint,
                    },
                )
                print(
                    f"ERROR batch={[path.name for path in group]}: "
                    f"{type(exc).__name__}: {exc}",
                    flush=True,
                )

    SCHEMA.write_reports(
        output_dir,
        all_files,
        decisions,
        str(config["analysis_version"]),
        prompt_fingerprint,
    )
    print(
        f"Run finished: completed={completed_now}, failed_batches={failed_batches}, "
        f"elapsed_seconds={time.monotonic() - started:.1f}. Re-run to resume.",
        flush=True,
    )
    return 0 if failed_batches == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
