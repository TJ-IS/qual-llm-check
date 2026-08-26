#!/usr/bin/env python3
"""Screen 2020-2027 local AIS Basket full texts for objective software-artifact research and its psychology-theory-guided subset."""

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
THEORY_STATUSES = {"pass", "fail", "not_applicable"}
YEAR_PATTERN = re.compile(r"^\d+_(\d{4})_")


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
    artifact = require_dict(payload.get("software_artifact"), "software_artifact")
    theory = require_dict(payload.get("theory_guidance"), "theory_guidance")
    objective_pass = require_bool(objective.get("pass"), "objective_metric.pass")
    artifact_pass = require_bool(artifact.get("pass"), "software_artifact.pass")
    base_match = require_bool(payload.get("base_match"), "base_match")
    if base_match != (objective_pass and artifact_pass):
        raise ValueError("base_match must equal objective_metric.pass AND software_artifact.pass")

    require_list(objective.get("metric_names"), "objective_metric.metric_names")
    require_list(objective.get("evidence_pointers"), "objective_metric.evidence_pointers")
    require_list(artifact.get("evidence_pointers"), "software_artifact.evidence_pointers")
    require_list(theory.get("theory_names"), "theory_guidance.theory_names")
    require_list(theory.get("evidence_pointers"), "theory_guidance.evidence_pointers")

    theory_status = str(theory.get("status") or "").strip()
    if theory_status not in THEORY_STATUSES:
        raise ValueError(f"invalid theory_guidance.status: {theory_status!r}")
    subset_match = require_bool(payload.get("theory_guided_subset_match"), "theory_guided_subset_match")
    if subset_match != (base_match and theory_status == "pass"):
        raise ValueError("theory_guided_subset_match is logically inconsistent")
    if not base_match and theory_status != "not_applicable":
        raise ValueError("base_match=false requires theory_guidance.status=not_applicable")
    if base_match and theory_status == "not_applicable":
        raise ValueError("base_match=true requires theory_guidance.status pass or fail")

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
    base_matches = [row for row in rows if row.get("base_match") is True]
    theory_matches = [row for row in rows if row.get("theory_guided_subset_match") is True]
    input_years = Counter(str(year_from_filename(path)) for path in all_files)
    theory_statuses = Counter(
        str((row.get("theory_guidance") or {}).get("status") or "") for row in rows
    )
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
        "software_artifact_pass_count": sum(
            bool((row.get("software_artifact") or {}).get("pass")) for row in rows
        ),
        "base_match_count": len(base_matches),
        "base_nonmatch_count": len(rows) - len(base_matches),
        "base_match_year_counts": counter_by_year(base_matches),
        "theory_guided_subset_match_count": len(theory_matches),
        "theory_guided_subset_year_counts": counter_by_year(theory_matches),
        "theory_status_counts": dict(sorted(theory_statuses.items())),
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
        "base_match",
        "objective_metric_pass",
        "metric_names",
        "desired_improvement_cn",
        "measurement_source_cn",
        "objective_centrality_evidence_cn",
        "software_artifact_pass",
        "artifact_type",
        "designed_or_modified_part",
        "part_of_artifact_evidence_cn",
        "link_to_objective_metric_cn",
        "theory_guided_subset_match",
        "theory_status",
        "theory_names",
        "why_psychology_related_cn",
        "theory_to_design_chain_cn",
        "theory_guided_component_evaluation_cn",
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
            artifact = row.get("software_artifact") or {}
            theory = row.get("theory_guidance") or {}
            writer.writerow(
                {
                    "record_id": row.get("record_id"),
                    "source_file": row.get("source_file"),
                    "title": row.get("title"),
                    "authors": row.get("authors"),
                    "year": row.get("year"),
                    "journal": row.get("journal"),
                    "doi": row.get("doi"),
                    "base_match": row.get("base_match"),
                    "objective_metric_pass": objective.get("pass"),
                    "metric_names": " | ".join(str(x) for x in objective.get("metric_names") or []),
                    "desired_improvement_cn": objective.get("desired_improvement_cn"),
                    "measurement_source_cn": objective.get("measurement_source_cn"),
                    "objective_centrality_evidence_cn": objective.get(
                        "centrality_and_improvement_evidence_cn"
                    ),
                    "software_artifact_pass": artifact.get("pass"),
                    "artifact_type": artifact.get("artifact_type"),
                    "designed_or_modified_part": artifact.get("designed_or_modified_part"),
                    "part_of_artifact_evidence_cn": artifact.get("part_of_artifact_evidence_cn"),
                    "link_to_objective_metric_cn": artifact.get("link_to_objective_metric_cn"),
                    "theory_guided_subset_match": row.get("theory_guided_subset_match"),
                    "theory_status": theory.get("status"),
                    "theory_names": " | ".join(str(x) for x in theory.get("theory_names") or []),
                    "why_psychology_related_cn": theory.get("why_psychology_related_cn"),
                    "theory_to_design_chain_cn": theory.get("theory_to_design_chain_cn"),
                    "theory_guided_component_evaluation_cn": theory.get(
                        "theory_guided_component_evaluation_cn"
                    ),
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
            artifact = row.get("software_artifact") or {}
            theory = row.get("theory_guidance") or {}
            markdown.extend(
                [
                    f"## {row.get('title')}",
                    "",
                    f"- Year/journal: {row.get('year')} / {row.get('journal')}",
                    f"- DOI: {row.get('doi')}",
                    f"- Metrics: {'; '.join(str(x) for x in objective.get('metric_names') or [])}",
                    f"- Objective evidence: {objective.get('centrality_and_improvement_evidence_cn', '')}",
                    f"- Artifact: {artifact.get('artifact_type', '')} — {artifact.get('designed_or_modified_part', '')}",
                    f"- Theory: {'; '.join(str(x) for x in theory.get('theory_names') or [])}",
                    f"- Theory-to-design: {theory.get('theory_to_design_chain_cn', '')}",
                    f"- Decision: {row.get('decision_reason_cn', '')}",
                    f"- Confidence: {row.get('confidence')}",
                    "",
                ]
            )
        tmp_path = output_dir / f"{filename}.tmp"
        tmp_path.write_text("\n".join(markdown), encoding="utf-8")
        os.replace(tmp_path, output_dir / filename)

    write_markdown("base_matches.md", "Base matches", base_matches)
    write_markdown("theory_guided_matches.md", "Psychology-theory-guided subset", theory_matches)


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
    decisions = load_current(decisions_path, fingerprint)
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
    base_matches_now = 0
    theory_matches_now = 0
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
                base_matches_now += int(bool(row["base_match"]))
                theory_matches_now += int(bool(row["theory_guided_subset_match"]))
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
                    f"base_matches={base_matches_now} theory_matches={theory_matches_now} "
                    f"rate={rate:.2f}/s",
                    flush=True,
                )
            if handled % report_interval == 0:
                write_reports(output_dir, all_files, decisions, config, fingerprint)

    write_reports(output_dir, all_files, decisions, config, fingerprint)
    elapsed = time.monotonic() - started
    print(
        f"finished completed_now={completed_now} failed_now={failed_now} "
        f"base_matches_now={base_matches_now} theory_matches_now={theory_matches_now} "
        f"elapsed_seconds={elapsed:.1f}",
        flush=True,
    )
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
