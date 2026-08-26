#!/usr/bin/env python3
"""Screen all 2020-2027 local AIS Basket full texts: exclusive objective-metric
improvement as the sole core goal, an explicit benchmark statement, and public
datasets (findable and obtainable)."""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
import random
import re
import sys
import threading
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


RUN_DIR = Path(__file__).resolve().parent
CONFIG_PATH = RUN_DIR / "config.json"
YEAR_PATTERN = re.compile(r"^\d+_(\d{4})_")
METRIC_GATE_KEYS = (
    "construct_independent_of_human_perception_or_semantics",
    "value_deterministically_observable",
    "all_core_success_outcomes_objective",
    "objective_improvement_is_sole_core_goal_and_contribution",
)
BENCHMARK_GATE_KEYS = (
    "explicit_benchmark_statement_present",
    "benchmark_statement_in_evaluation_context",
    "benchmark_evaluation_supports_core_improvement_claim",
    "benchmark_has_explicit_comparator",
)
DATASET_GATE_KEYS = (
    "dataset_identifiable_in_fulltext",
    "dataset_publicly_findable",
    "dataset_publicly_obtainable",
    "public_dataset_supports_core_claim",
)
ALLOWED_METRICS = {"fully_objective_direct", "objective_fixed_factual_labels"}
ALL_METRICS = ALLOWED_METRICS | {
    "subjective_construct_with_fixed_labels", "human_semantic_judgment",
    "mixed_objective_subjective", "subjective_or_self_report",
    "no_qualifying_metric", "unclear",
}
ALLOWED_CORE = {"exclusive_objective_improvement"}
ALL_CORE = ALLOWED_CORE | {
    "objective_improvement_primary_but_not_exclusive",
    "objective_metric_secondary",
    "theory_or_explanation_primary",
    "unclear",
}
ALLOWED_BENCHMARK = {"named_public_benchmark_central", "benchmark_comparison_central"}
ALL_BENCHMARK = ALLOWED_BENCHMARK | {
    "named_benchmark_peripheral", "generic_benchmark_word_only",
    "no_benchmark_statement", "unclear",
}
ALLOWED_DATASET = {"named_public_dataset_central", "publicly_described_source_central"}
ALL_DATASET = ALLOWED_DATASET | {
    "private_or_confidential_core", "self_collected_not_obtainable",
    "synthetic_only", "public_peripheral_private_core",
    "dataset_not_identifiable", "no_real_data_evaluation", "unclear",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def resolve_from_run(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (RUN_DIR / path).resolve()


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return {}, normalized
    end = normalized.find("\n---\n", 4)
    if end < 0:
        return {}, normalized
    metadata: dict[str, Any] = {}
    for line in normalized[4:end].splitlines():
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        raw_value = raw_value.strip()
        try:
            metadata[key.strip()] = json.loads(raw_value)
        except json.JSONDecodeError:
            metadata[key.strip()] = raw_value
    return metadata, normalized[end + 5 :].lstrip()


def year_from_filename(path: Path) -> int | None:
    match = YEAR_PATTERN.match(path.name)
    return int(match.group(1)) if match else None


def metadata_for(path: Path, fulltext: str, frontmatter: dict[str, Any]) -> dict[str, str]:
    parts = path.name.split("_", 2)
    return {
        "record_id": str(frontmatter.get("otero_id") or (parts[0].lstrip("0") or "0")),
        "source_file": path.name,
        "title": str(frontmatter.get("title") or path.stem),
        "authors": str(frontmatter.get("authors") or ""),
        "year": str(frontmatter.get("year") or (parts[1] if len(parts) >= 3 else "")),
        "journal": str(frontmatter.get("journal") or ""),
        "doi": str(frontmatter.get("doi") or ""),
        "fulltext_chars": str(len(fulltext)),
    }


def parse_json_object(content: str) -> dict[str, Any]:
    text = (content or "").strip()
    if not text:
        raise ValueError("empty model response")
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise
        payload = json.loads(text[start : end + 1])
    if not isinstance(payload, dict):
        raise ValueError("model response is not a JSON object")
    return payload


def require_bool(value: Any, field: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{field} must be boolean")
    return value


def require_dict(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")
    return value


def require_list(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{field} must be a list")
    return value


def validate_decision(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")

    objective = require_dict(payload.get("objective_metric"), "objective_metric")
    benchmark = require_dict(payload.get("benchmark"), "benchmark")
    dataset = require_dict(payload.get("dataset"), "dataset")
    objective_gates = require_dict(objective.get("gates"), "objective_metric.gates")
    benchmark_gates = require_dict(benchmark.get("gates"), "benchmark.gates")
    dataset_gates = require_dict(dataset.get("gates"), "dataset.gates")

    metric_values = [require_bool(objective_gates.get(key), f"objective_metric.gates.{key}") for key in METRIC_GATE_KEYS]
    benchmark_values = [require_bool(benchmark_gates.get(key), f"benchmark.gates.{key}") for key in BENCHMARK_GATE_KEYS]
    dataset_values = [require_bool(dataset_gates.get(key), f"dataset.gates.{key}") for key in DATASET_GATE_KEYS]

    metric_status = str(objective.get("metric_status") or "")
    core_status = str(objective.get("core_goal_status") or "")
    benchmark_status = str(benchmark.get("benchmark_status") or "")
    dataset_status = str(dataset.get("dataset_status") or "")
    if metric_status not in ALL_METRICS or core_status not in ALL_CORE:
        raise ValueError(f"invalid objective metric/core status: {metric_status!r} / {core_status!r}")
    if benchmark_status not in ALL_BENCHMARK:
        raise ValueError(f"invalid benchmark status: {benchmark_status!r}")
    if dataset_status not in ALL_DATASET:
        raise ValueError(f"invalid dataset status: {dataset_status!r}")

    objective_expected = all(metric_values) and metric_status in ALLOWED_METRICS and core_status in ALLOWED_CORE
    benchmark_expected = all(benchmark_values) and benchmark_status in ALLOWED_BENCHMARK
    dataset_expected = all(dataset_values) and dataset_status in ALLOWED_DATASET
    objective_pass = require_bool(objective.get("pass"), "objective_metric.pass")
    benchmark_pass = require_bool(benchmark.get("pass"), "benchmark.pass")
    dataset_pass = require_bool(dataset.get("pass"), "dataset.pass")
    if objective_pass != objective_expected or benchmark_pass != benchmark_expected or dataset_pass != dataset_expected:
        raise ValueError("module pass is logically inconsistent with gates/status")
    strict_include = require_bool(payload.get("strict_include"), "strict_include")
    if strict_include != (objective_pass and benchmark_pass and dataset_pass):
        raise ValueError("strict_include must equal all module passes")

    require_list(objective.get("core_metrics"), "objective_metric.core_metrics")
    require_list(benchmark.get("named_benchmarks"), "benchmark.named_benchmarks")
    require_list(benchmark.get("comparators"), "benchmark.comparators")
    require_list(benchmark.get("benchmark_evidence_pointers"), "benchmark.benchmark_evidence_pointers")
    require_list(dataset.get("named_datasets"), "dataset.named_datasets")
    require_list(dataset.get("dataset_evidence_pointers"), "dataset.dataset_evidence_pointers")
    require_list(payload.get("evidence_pointers"), "evidence_pointers")
    require_list(payload.get("exclusion_trigger_codes"), "exclusion_trigger_codes")

    try:
        confidence = float(payload.get("confidence"))
    except (TypeError, ValueError) as exc:
        raise ValueError("confidence must be numeric") from exc
    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    payload["confidence"] = confidence
    return payload


def usage_dict(response: Any) -> dict[str, int]:
    usage = response.usage
    if usage is None:
        return {}
    keys = (
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "prompt_cache_hit_tokens",
        "prompt_cache_miss_tokens",
    )
    return {
        key: int(getattr(usage, key))
        for key in keys
        if isinstance(getattr(usage, key, None), int)
    }


class ThreadClients:
    def __init__(self, api_key: str, base_url: str, timeout: float):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.local = threading.local()

    def get(self) -> OpenAI:
        client = getattr(self.local, "client", None)
        if client is None:
            client = OpenAI(api_key=self.api_key, base_url=self.base_url, timeout=self.timeout)
            self.local.client = client
        return client


def analyze_one(
    path: Path,
    clients: ThreadClients,
    config: dict[str, Any],
    system_prompt: str,
    user_template: str,
    fingerprint: str,
) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, fulltext = parse_frontmatter(raw)
    metadata = metadata_for(path, fulltext, frontmatter)
    user_prompt = user_template.format(**metadata, fulltext=fulltext)
    model, batch = config["model"], config["batch"]
    last_error: BaseException | None = None
    for attempt in range(1, int(batch["retries"]) + 2):
        try:
            response = clients.get().chat.completions.create(
                model=str(model["name"]),
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=float(model["temperature"]),
                max_tokens=int(model["max_tokens"]),
                response_format={"type": "json_object"},
            )
            choice = response.choices[0]
            content = choice.message.content or getattr(choice.message, "reasoning_content", None) or ""
            if not content.strip():
                reasoning = getattr(choice.message, "reasoning_content", None) or ""
                raise ValueError(
                    f"empty response finish_reason={choice.finish_reason!r} reasoning_chars={len(reasoning)}"
                )
            decision = validate_decision(parse_json_object(content), metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                "analysis_version": config["analysis_version"],
                "prompt_fingerprint": fingerprint,
                "model": model["name"],
                "analysis_mode": "one_complete_local_fulltext_per_request",
                "attempts": attempt,
                "completed_at": utc_now(),
                **decision,
                "usage": usage_dict(response),
            }
        except Exception as exc:
            last_error = exc
            if attempt > int(batch["retries"]):
                break
            delay = float(batch["retry_base_delay_seconds"]) * (2 ** (attempt - 1))
            time.sleep(delay + random.uniform(0, 0.5))
    assert last_error is not None
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}") from last_error


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


LEGACY_ANALYSIS_VERSION = "ais-basket-exclusive-objective-metric-benchmark-public-dataset-2020-2027-flash-v1"
LEGACY_YEAR_RANGE = {"from": 2020, "to": 2027}


def fingerprint_for(
    analysis_version: str,
    model: str,
    year_range: dict[str, int] | None,
    system_prompt: str,
    user_template: str,
) -> str:
    value = {
        "analysis_version": analysis_version,
        "model": model,
        "year_range": year_range,
        "system_prompt": system_prompt,
        "user_template": user_template,
    }
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()


def load_current(
    path: Path,
    fingerprint: str,
    legacy_fingerprints: set[str] | None = None,
) -> dict[str, dict[str, Any]]:
    decisions: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return decisions
    accepted = {fingerprint} | (legacy_fingerprints or set())
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("prompt_fingerprint") in accepted:
                source_file = str(row.get("source_file") or "")
                if not source_file:
                    raise ValueError(f"missing source_file at {path}:{line_number}")
                decisions[source_file] = row
    return decisions


def prompt_fingerprint(config: dict[str, Any], system_prompt: str, user_template: str) -> str:
    value = {
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "year_range": config["year_range"],
        "system_prompt": system_prompt,
        "user_template": user_template,
    }
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()


def counter_by_year(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter(str(row.get("year") or "") for row in rows)
    return dict(sorted(counts.items()))


def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    config: dict[str, Any],
    fingerprint: str,
) -> None:
    rows = [decisions[name] for name in sorted(decisions)]
    strict_matches = [row for row in rows if row.get("strict_include") is True]
    input_years = Counter(str(year_from_filename(path)) for path in all_files)
    usage_keys = (
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "prompt_cache_hit_tokens",
        "prompt_cache_miss_tokens",
    )
    summary = {
        "updated_at": utc_now(),
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "max_concurrency": config["batch"]["max_concurrency"],
        "prompt_fingerprint": fingerprint,
        "year_range": config["year_range"],
        "input_source": str(resolve_from_run(str(config["input_dir"]))),
        "input_fulltexts": len(all_files),
        "input_year_counts": dict(sorted(input_years.items())),
        "completed": len(rows),
        "pending": len(all_files) - len(rows),
        "completed_year_counts": counter_by_year(rows),
        "objective_metric_pass_count": sum(
            bool((row.get("objective_metric") or {}).get("pass")) for row in rows
        ),
        "benchmark_pass_count": sum(
            bool((row.get("benchmark") or {}).get("pass")) for row in rows
        ),
        "dataset_pass_count": sum(
            bool((row.get("dataset") or {}).get("pass")) for row in rows
        ),
        "strict_include_count": len(strict_matches),
        "strict_exclude_count": len(rows) - len(strict_matches),
        "strict_include_year_counts": counter_by_year(strict_matches),
        "strict_include_journal_counts": dict(sorted(Counter(str(row.get("journal") or "") for row in strict_matches).items())),
        "metric_status_counts": dict(sorted(Counter(str((row.get("objective_metric") or {}).get("metric_status") or "") for row in rows).items())),
        "core_goal_status_counts": dict(sorted(Counter(str((row.get("objective_metric") or {}).get("core_goal_status") or "") for row in rows).items())),
        "benchmark_status_counts": dict(sorted(Counter(str((row.get("benchmark") or {}).get("benchmark_status") or "") for row in rows).items())),
        "dataset_status_counts": dict(sorted(Counter(str((row.get("dataset") or {}).get("dataset_status") or "") for row in rows).items())),
        "usage": {
            key: sum(int((row.get("usage") or {}).get(key, 0)) for row in rows)
            for key in usage_keys
        },
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    tmp_summary = output_dir / "summary.json.tmp"
    tmp_summary.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    os.replace(tmp_summary, output_dir / "summary.json")

    fields = [
        "record_id",
        "source_file",
        "title",
        "authors",
        "year",
        "journal",
        "doi",
        "strict_include",
        "objective_metric_pass",
        "metric_status",
        "core_goal_status",
        "core_metrics_json",
        "core_goal_evidence_cn",
        "other_core_goals_audit_cn",
        "benchmark_pass",
        "benchmark_status",
        "named_benchmarks",
        "benchmark_statement_quote_cn",
        "benchmark_evaluation_cn",
        "comparators",
        "dataset_pass",
        "dataset_status",
        "named_datasets",
        "dataset_source_quote_cn",
        "dataset_obtainability_cn",
        "exclusion_trigger_codes",
        "decision_reason_cn",
        "confidence",
        "fulltext_chars",
        "attempts",
    ]
    tmp_csv = output_dir / "decisions.csv.tmp"
    with tmp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            objective = row.get("objective_metric") or {}
            benchmark = row.get("benchmark") or {}
            dataset = row.get("dataset") or {}
            writer.writerow(
                {
                    "record_id": row.get("record_id"),
                    "source_file": row.get("source_file"),
                    "title": row.get("title"),
                    "authors": row.get("authors"),
                    "year": row.get("year"),
                    "journal": row.get("journal"),
                    "doi": row.get("doi"),
                    "strict_include": row.get("strict_include"),
                    "objective_metric_pass": objective.get("pass"),
                    "metric_status": objective.get("metric_status"),
                    "core_goal_status": objective.get("core_goal_status"),
                    "core_metrics_json": json.dumps(objective.get("core_metrics") or [], ensure_ascii=False),
                    "core_goal_evidence_cn": objective.get("core_goal_evidence_cn"),
                    "other_core_goals_audit_cn": objective.get("other_core_goals_audit_cn"),
                    "benchmark_pass": benchmark.get("pass"),
                    "benchmark_status": benchmark.get("benchmark_status"),
                    "named_benchmarks": " | ".join(str(x) for x in benchmark.get("named_benchmarks") or []),
                    "benchmark_statement_quote_cn": benchmark.get("benchmark_statement_quote_cn"),
                    "benchmark_evaluation_cn": benchmark.get("benchmark_evaluation_cn"),
                    "comparators": " | ".join(str(x) for x in benchmark.get("comparators") or []),
                    "dataset_pass": dataset.get("pass"),
                    "dataset_status": dataset.get("dataset_status"),
                    "named_datasets": " | ".join(str(x) for x in dataset.get("named_datasets") or []),
                    "dataset_source_quote_cn": dataset.get("dataset_source_quote_cn"),
                    "dataset_obtainability_cn": dataset.get("dataset_obtainability_cn"),
                    "exclusion_trigger_codes": " | ".join(str(x) for x in row.get("exclusion_trigger_codes") or []),
                    "decision_reason_cn": row.get("decision_reason_cn"),
                    "confidence": row.get("confidence"),
                    "fulltext_chars": row.get("fulltext_chars"),
                    "attempts": row.get("attempts"),
                }
            )
    os.replace(tmp_csv, output_dir / "decisions.csv")

    def write_markdown(filename: str, title: str, selected: list[dict[str, Any]]) -> None:
        markdown = [f"# {title}", "", f"Completed: {len(rows)} / {len(all_files)}", f"Retained: {len(selected)}", ""]
        for row in sorted(
            selected,
            key=lambda item: (
                -float(item.get("confidence") or 0),
                str(item.get("title") or ""),
            ),
        ):
            objective = row.get("objective_metric") or {}
            benchmark = row.get("benchmark") or {}
            dataset = row.get("dataset") or {}
            markdown.extend(
                [
                    f"## {row.get('title')}",
                    "",
                    f"- Year/journal: {row.get('year')} / {row.get('journal')}",
                    f"- DOI: {row.get('doi')}",
                    f"- Metric/core status: {objective.get('metric_status', '')} / {objective.get('core_goal_status', '')}",
                    f"- Metrics: {json.dumps(objective.get('core_metrics') or [], ensure_ascii=False)}",
                    f"- Benchmark status: {benchmark.get('benchmark_status', '')}",
                    f"- Named benchmarks: {' | '.join(str(x) for x in benchmark.get('named_benchmarks') or [])}",
                    f"- Benchmark evaluation: {benchmark.get('benchmark_evaluation_cn', '')}",
                    f"- Dataset status: {dataset.get('dataset_status', '')}",
                    f"- Named datasets: {' | '.join(str(x) for x in dataset.get('named_datasets') or [])}",
                    f"- Dataset obtainability: {dataset.get('dataset_obtainability_cn', '')}",
                    f"- Decision: {row.get('decision_reason_cn', '')}",
                    f"- Confidence: {row.get('confidence')}",
                    "",
                ]
            )
        tmp_path = output_dir / f"{filename}.tmp"
        tmp_path.write_text("\n".join(markdown), encoding="utf-8")
        os.replace(tmp_path, output_dir / filename)

    write_markdown("strict_matches.md", "Exclusive objective-metric improvement with explicit benchmark statements and public datasets", strict_matches)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--max-concurrency", type=int)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    if args.offset < 0:
        parser.error("--offset must be non-negative")
    if args.max_concurrency is not None and not 1 <= args.max_concurrency <= 500:
        parser.error("--max-concurrency must be between 1 and 500")
    return args


def main() -> int:
    args = parse_args()
    config = load_config()
    input_dir = resolve_from_run(str(config["input_dir"]))
    output_dir = resolve_from_run(str(config["output_dir"]))
    env_file = resolve_from_run(str(config["env_file"]))
    year_from = int(config["year_range"]["from"])
    year_to = int(config["year_range"]["to"])
    local_files = sorted(input_dir.glob("*.md"))
    all_files = [
        path
        for path in local_files
        if (year := year_from_filename(path)) is not None and year_from <= year <= year_to
    ]
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(
        encoding="utf-8"
    ).strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(
        encoding="utf-8"
    ).strip()
    fingerprint = prompt_fingerprint(config, system_prompt, user_template)
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    legacy_fingerprints = None
    if config["analysis_version"] != LEGACY_ANALYSIS_VERSION:
        legacy_fingerprints = {
            fingerprint_for(
                LEGACY_ANALYSIS_VERSION,
                str(config["model"]["name"]),
                LEGACY_YEAR_RANGE,
                system_prompt,
                user_template,
            )
        }
    decisions = load_current(decisions_path, fingerprint, legacy_fingerprints)
    selected = all_files[args.offset :]
    pending = [path for path in selected if path.name not in decisions]
    if args.limit is not None:
        pending = pending[: args.limit]
    concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    year_counts = Counter(year_from_filename(path) for path in all_files)
    print(
        f"local_fulltexts={len(local_files)} scope={len(all_files)} years={dict(sorted(year_counts.items()))} "
        f"completed={len(decisions)} pending_this_run={len(pending)} "
        f"model={config['model']['name']} concurrency={concurrency}",
        flush=True,
    )
    print(f"prompt_fingerprint={fingerprint}", flush=True)
    print(f"input_dir={input_dir}", flush=True)
    print(f"output_dir={output_dir}", flush=True)
    if args.dry_run:
        for path in pending[:10]:
            print(f"DRY_RUN file={path.name} bytes={path.stat().st_size}", flush=True)
        return 0
    if not pending:
        write_reports(output_dir, all_files, decisions, config, fingerprint)
        return 0

    load_dotenv(env_file)
    api_key = os.getenv(str(config["model"]["api_key_env"]))
    if not api_key:
        raise RuntimeError(f"missing API key env: {config['model']['api_key_env']}")
    base_url = os.getenv(str(config["model"]["base_url_env"])) or str(
        config["model"]["base_url"]
    )
    clients = ThreadClients(api_key, base_url, float(config["model"]["timeout_seconds"]))
    completed_now = 0
    failed_now = 0
    strict_matches_now = 0
    started = time.monotonic()
    progress_interval = int(config["batch"]["progress_interval"])
    report_interval = int(config["batch"]["report_interval"])

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {
            pool.submit(
                analyze_one,
                path,
                clients,
                config,
                system_prompt,
                user_template,
                fingerprint,
            ): path
            for path in pending
        }
        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                row = future.result()
                append_jsonl(decisions_path, row)
                decisions[path.name] = row
                completed_now += 1
                strict_matches_now += int(bool(row["strict_include"]))
            except Exception as exc:
                failed_now += 1
                append_jsonl(
                    errors_path,
                    {
                        "source_file": path.name,
                        "failed_at": utc_now(),
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "prompt_fingerprint": fingerprint,
                    },
                )
                print(f"ERROR file={path.name} error={exc}", flush=True)
            handled = completed_now + failed_now
            if handled % progress_interval == 0:
                elapsed = time.monotonic() - started
                rate = handled / elapsed if elapsed else 0.0
                print(
                    f"progress={handled}/{len(pending)} ok={completed_now} failed={failed_now} "
                    f"strict_matches={strict_matches_now} "
                    f"rate={rate:.2f}/s",
                    flush=True,
                )
            if handled % report_interval == 0:
                write_reports(output_dir, all_files, decisions, config, fingerprint)

    write_reports(output_dir, all_files, decisions, config, fingerprint)
    elapsed = time.monotonic() - started
    print(
        f"finished completed_now={completed_now} failed_now={failed_now} "
        f"strict_matches_now={strict_matches_now} "
        f"elapsed_seconds={elapsed:.1f}",
        flush=True,
    )
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
