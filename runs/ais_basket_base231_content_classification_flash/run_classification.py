#!/usr/bin/env python3
"""Classify the content of the 231 retained local AIS Basket full texts."""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
import random
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

FUNCTION_CATEGORIES = {
    "human_facing_information_and_interaction",
    "recommendation_search_and_matching",
    "prediction_detection_and_assessment",
    "planning_optimization_and_allocation",
    "workflow_automation_and_coordination",
    "platform_mechanism_and_governance",
    "data_knowledge_representation_and_integration",
    "security_privacy_and_access_control",
    "other_software_function",
}
OBJECTIVE_FAMILIES = {
    "analytic_quality",
    "human_task_performance",
    "behavioral_response",
    "operational_efficiency",
    "economic_and_welfare",
    "risk_security_and_safety",
    "substantive_domain_outcome",
    "technical_system_performance",
    "multi_objective_or_tradeoff",
}
APPLICATION_CONTEXTS = {
    "commerce_marketing_and_customer_service",
    "digital_platform_social_media_and_crowdfunding",
    "healthcare_and_care",
    "cybersecurity_fraud_and_compliance",
    "enterprise_work_and_knowledge",
    "education_training_and_learning",
    "logistics_transport_supply_chain_and_manufacturing",
    "finance_accounting_and_investment",
    "public_sector_crisis_and_humanitarian",
    "general_or_cross_domain",
    "other_context",
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


def load_source_candidates(path: Path) -> dict[str, dict[str, Any]]:
    candidates: dict[str, dict[str, Any]] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("base_match") is not True:
                continue
            source = str(row.get("source_file") or "")
            if not source:
                raise ValueError(f"missing source_file at {path}:{line_number}")
            if source in candidates:
                raise ValueError(f"duplicate retained source_file: {source}")
            candidates[source] = {
                "source_base_match": True,
                "source_theory_guided_subset_match": bool(
                    row.get("theory_guided_subset_match") is True
                ),
            }
    return candidates


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


def require_dict(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")
    return value


def require_list(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{field} must be a list")
    return value


def require_enum(value: Any, allowed: set[str], field: str) -> str:
    normalized = str(value or "").strip()
    if normalized not in allowed:
        raise ValueError(f"invalid {field}: {normalized!r}")
    return normalized


def validate_decision(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    content = require_dict(payload.get("research_content"), "research_content")
    require_list(content.get("objective_metrics"), "research_content.objective_metrics")
    require_enum(payload.get("primary_artifact_function"), FUNCTION_CATEGORIES, "primary_artifact_function")
    primary_objective = require_enum(
        payload.get("primary_objective_family"), OBJECTIVE_FAMILIES, "primary_objective_family"
    )
    secondary = require_list(payload.get("secondary_objective_families"), "secondary_objective_families")
    if len(secondary) > 2:
        raise ValueError("secondary_objective_families may contain at most two values")
    if len(set(str(value) for value in secondary)) != len(secondary):
        raise ValueError("secondary_objective_families contains duplicates")
    for value in secondary:
        normalized = require_enum(value, OBJECTIVE_FAMILIES, "secondary_objective_families[]")
        if normalized == primary_objective:
            raise ValueError("secondary objective duplicates primary objective")
    require_enum(payload.get("application_context"), APPLICATION_CONTEXTS, "application_context")
    tags = require_list(payload.get("content_tags_cn"), "content_tags_cn")
    if not 2 <= len(tags) <= 4 or any(not str(tag).strip() for tag in tags):
        raise ValueError("content_tags_cn must contain 2-4 non-empty tags")
    require_list(payload.get("evidence_pointers"), "evidence_pointers")
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
    source_flags: dict[str, Any],
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
            content = choice.message.content or ""
            if not content.strip():
                reasoning = getattr(choice.message, "reasoning_content", None) or ""
                raise ValueError(
                    f"empty response finish_reason={choice.finish_reason!r} reasoning_chars={len(reasoning)}"
                )
            decision = validate_decision(parse_json_object(content), metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                **source_flags,
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


def load_current(path: Path, fingerprint: str) -> dict[str, dict[str, Any]]:
    decisions: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return decisions
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("prompt_fingerprint") == fingerprint:
                source = str(row.get("source_file") or "")
                if not source:
                    raise ValueError(f"missing source_file at {path}:{line_number}")
                decisions[source] = row
    return decisions


def prompt_fingerprint(config: dict[str, Any], system_prompt: str, user_template: str) -> str:
    value = {
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "source_decisions": config["source_decisions"],
        "system_prompt": system_prompt,
        "user_template": user_template,
    }
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()


def write_crosstab(
    path: Path,
    rows: list[dict[str, Any]],
    row_field: str,
    column_field: str,
    row_values: list[str],
) -> None:
    columns = sorted({str(row.get(column_field) or "") for row in rows})
    counts = Counter((str(row.get(row_field) or ""), str(row.get(column_field) or "")) for row in rows)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[row_field, *columns, "total"])
        writer.writeheader()
        for value in row_values:
            writer.writerow(
                {
                    row_field: value,
                    **{column: counts[(value, column)] for column in columns},
                    "total": sum(counts[(value, column)] for column in columns),
                }
            )


def write_reports(
    output_dir: Path,
    candidate_names: list[str],
    decisions: dict[str, dict[str, Any]],
    config: dict[str, Any],
    fingerprint: str,
) -> None:
    rows = [decisions[name] for name in sorted(decisions)]
    theory_rows = [row for row in rows if row.get("source_theory_guided_subset_match") is True]
    non_theory_rows = [row for row in rows if row.get("source_theory_guided_subset_match") is not True]
    isr_rows = [row for row in rows if row.get("journal") == "Information Systems Research"]
    usage_keys = (
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "prompt_cache_hit_tokens",
        "prompt_cache_miss_tokens",
    )
    function_order = sorted(FUNCTION_CATEGORIES)
    objective_order = sorted(OBJECTIVE_FAMILIES)
    context_order = sorted(APPLICATION_CONTEXTS)

    def counts(data: list[dict[str, Any]], field: str) -> dict[str, int]:
        return dict(sorted(Counter(str(row.get(field) or "") for row in data).items()))

    summary = {
        "updated_at": utc_now(),
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "max_concurrency": config["batch"]["max_concurrency"],
        "prompt_fingerprint": fingerprint,
        "input_candidates": len(candidate_names),
        "input_theory_guided_subset": 110,
        "completed": len(rows),
        "pending": len(candidate_names) - len(rows),
        "function_counts": counts(rows, "primary_artifact_function"),
        "objective_counts": counts(rows, "primary_objective_family"),
        "context_counts": counts(rows, "application_context"),
        "theory_subset_function_counts": counts(theory_rows, "primary_artifact_function"),
        "non_theory_function_counts": counts(non_theory_rows, "primary_artifact_function"),
        "isr_count": len(isr_rows),
        "isr_function_counts": counts(isr_rows, "primary_artifact_function"),
        "isr_objective_counts": counts(isr_rows, "primary_objective_family"),
        "isr_context_counts": counts(isr_rows, "application_context"),
        "journal_counts": counts(rows, "journal"),
        "year_counts": counts(rows, "year"),
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
        "record_id", "source_file", "title", "authors", "year", "journal", "doi",
        "source_theory_guided_subset_match", "primary_artifact_function",
        "primary_objective_family", "secondary_objective_families", "application_context",
        "problem_cn", "software_artifact_cn", "designed_component_cn", "artifact_in_use_cn",
        "objective_metrics", "comparison_cn", "main_finding_cn", "one_sentence_logic_cn",
        "artifact_function_reason_cn", "objective_family_reason_cn",
        "application_context_detail_cn", "content_tags_cn", "evidence_pointers",
        "confidence", "limitations_cn", "fulltext_chars", "attempts",
    ]
    tmp_csv = output_dir / "classifications.csv.tmp"
    with tmp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            content = row.get("research_content") or {}
            writer.writerow(
                {
                    "record_id": row.get("record_id"), "source_file": row.get("source_file"),
                    "title": row.get("title"), "authors": row.get("authors"),
                    "year": row.get("year"), "journal": row.get("journal"), "doi": row.get("doi"),
                    "source_theory_guided_subset_match": row.get("source_theory_guided_subset_match"),
                    "primary_artifact_function": row.get("primary_artifact_function"),
                    "primary_objective_family": row.get("primary_objective_family"),
                    "secondary_objective_families": " | ".join(row.get("secondary_objective_families") or []),
                    "application_context": row.get("application_context"),
                    "problem_cn": content.get("problem_cn"),
                    "software_artifact_cn": content.get("software_artifact_cn"),
                    "designed_component_cn": content.get("designed_component_cn"),
                    "artifact_in_use_cn": content.get("artifact_in_use_cn"),
                    "objective_metrics": " | ".join(str(x) for x in content.get("objective_metrics") or []),
                    "comparison_cn": content.get("comparison_cn"),
                    "main_finding_cn": content.get("main_finding_cn"),
                    "one_sentence_logic_cn": content.get("one_sentence_logic_cn"),
                    "artifact_function_reason_cn": row.get("artifact_function_reason_cn"),
                    "objective_family_reason_cn": row.get("objective_family_reason_cn"),
                    "application_context_detail_cn": row.get("application_context_detail_cn"),
                    "content_tags_cn": " | ".join(str(x) for x in row.get("content_tags_cn") or []),
                    "evidence_pointers": " | ".join(str(x) for x in row.get("evidence_pointers") or []),
                    "confidence": row.get("confidence"), "limitations_cn": row.get("limitations_cn"),
                    "fulltext_chars": row.get("fulltext_chars"), "attempts": row.get("attempts"),
                }
            )
    os.replace(tmp_csv, output_dir / "classifications.csv")

    write_crosstab(output_dir / "function_by_journal.csv", rows, "primary_artifact_function", "journal", function_order)
    write_crosstab(output_dir / "function_by_year.csv", rows, "primary_artifact_function", "year", function_order)
    write_crosstab(output_dir / "function_by_objective.csv", rows, "primary_artifact_function", "primary_objective_family", function_order)
    write_crosstab(output_dir / "function_by_context.csv", rows, "primary_artifact_function", "application_context", function_order)
    write_crosstab(output_dir / "function_by_theory_subset.csv", rows, "primary_artifact_function", "source_theory_guided_subset_match", function_order)
    write_crosstab(output_dir / "objective_by_journal.csv", rows, "primary_objective_family", "journal", objective_order)
    write_crosstab(output_dir / "objective_by_year.csv", rows, "primary_objective_family", "year", objective_order)
    write_crosstab(output_dir / "context_by_journal.csv", rows, "application_context", "journal", context_order)
    write_crosstab(output_dir / "context_by_year.csv", rows, "application_context", "year", context_order)

    markdown = [
        "# Articles grouped by primary software function", "",
        f"Completed: {len(rows)} / {len(candidate_names)}", "",
    ]
    for category in sorted(FUNCTION_CATEGORIES, key=lambda value: (-summary["function_counts"].get(value, 0), value)):
        selected = [row for row in rows if row.get("primary_artifact_function") == category]
        markdown.extend([f"## {category} ({len(selected)})", ""])
        for row in sorted(selected, key=lambda item: (str(item.get("year")), str(item.get("title")))):
            content = row.get("research_content") or {}
            marker = " [theory subset]" if row.get("source_theory_guided_subset_match") else ""
            markdown.extend(
                [
                    f"### {row.get('title')}{marker}", "",
                    f"- Year/journal: {row.get('year')} / {row.get('journal')}",
                    f"- Logic: {content.get('one_sentence_logic_cn', '')}",
                    f"- Objective family: {row.get('primary_objective_family')}",
                    f"- Context: {row.get('application_context')}",
                    f"- Tags: {', '.join(str(x) for x in row.get('content_tags_cn') or [])}", "",
                ]
            )
    tmp_md = output_dir / "articles_by_function.md.tmp"
    tmp_md.write_text("\n".join(markdown), encoding="utf-8")
    os.replace(tmp_md, output_dir / "articles_by_function.md")


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
    source_path = resolve_from_run(str(config["source_decisions"]))
    output_dir = resolve_from_run(str(config["output_dir"]))
    env_file = resolve_from_run(str(config["env_file"]))
    candidates = load_source_candidates(source_path)
    if len(candidates) != 231:
        raise ValueError(f"expected 231 retained candidates, found {len(candidates)}")
    local_files = {path.name: path for path in input_dir.glob("*.md")}
    missing = sorted(set(candidates) - set(local_files))
    if missing:
        raise FileNotFoundError(f"missing local full texts: {missing[:10]}")
    candidate_names = sorted(candidates)
    candidate_paths = [local_files[name] for name in candidate_names]
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(encoding="utf-8").strip()
    fingerprint = prompt_fingerprint(config, system_prompt, user_template)
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    decisions = load_current(decisions_path, fingerprint)
    selected = candidate_paths[args.offset :]
    pending = [path for path in selected if path.name not in decisions]
    if args.limit is not None:
        pending = pending[: args.limit]
    concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    theory_count = sum(bool(value["source_theory_guided_subset_match"]) for value in candidates.values())
    print(
        f"scope={len(candidate_names)} source_theory_subset={theory_count} completed={len(decisions)} "
        f"pending_this_run={len(pending)} model={config['model']['name']} concurrency={concurrency}",
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
        write_reports(output_dir, candidate_names, decisions, config, fingerprint)
        return 0

    load_dotenv(env_file)
    api_key = os.getenv(str(config["model"]["api_key_env"]))
    if not api_key:
        raise RuntimeError(f"missing API key env: {config['model']['api_key_env']}")
    base_url = os.getenv(str(config["model"]["base_url_env"])) or str(config["model"]["base_url"])
    clients = ThreadClients(api_key, base_url, float(config["model"]["timeout_seconds"]))
    completed_now = 0
    failed_now = 0
    started = time.monotonic()
    progress_interval = int(config["batch"]["progress_interval"])
    report_interval = int(config["batch"]["report_interval"])

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {
            pool.submit(
                analyze_one, path, candidates[path.name], clients, config,
                system_prompt, user_template, fingerprint,
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
            except Exception as exc:
                failed_now += 1
                append_jsonl(
                    errors_path,
                    {
                        "source_file": path.name, "failed_at": utc_now(),
                        "error_type": type(exc).__name__, "error": str(exc),
                        "prompt_fingerprint": fingerprint,
                    },
                )
                print(f"ERROR file={path.name} error={exc}", flush=True)
            handled = completed_now + failed_now
            if handled % progress_interval == 0:
                elapsed = time.monotonic() - started
                rate = handled / elapsed if elapsed else 0.0
                print(
                    f"progress={handled}/{len(pending)} ok={completed_now} failed={failed_now} rate={rate:.2f}/s",
                    flush=True,
                )
            if handled % report_interval == 0:
                write_reports(output_dir, candidate_names, decisions, config, fingerprint)

    write_reports(output_dir, candidate_names, decisions, config, fingerprint)
    elapsed = time.monotonic() - started
    print(
        f"finished completed_now={completed_now} failed_now={failed_now} elapsed_seconds={elapsed:.1f}",
        flush=True,
    )
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
