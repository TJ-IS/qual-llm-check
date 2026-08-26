#!/usr/bin/env python3
"""Screen all local IS full texts for strict objective-metric-improvement research."""

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

CENTRALITY = {"exclusive", "dominant", "mixed", "incidental", "none"}
SOLUTION_LAYERS = {
    "prediction_model",
    "prescriptive_model_or_optimization",
    "algorithm_or_computational_method",
    "software_system_or_artifact",
    "interface_or_interaction_design",
    "digital_platform_mechanism_or_policy",
    "hybrid",
    "none",
}
PARADIGMS = {
    "predictive_analytics",
    "prescriptive_analytics_or_optimization",
    "design_science_research",
    "explanatory_design_theorizing",
    "theory_driven_artifact_experiment",
    "computational_or_algorithm_design",
    "digital_platform_or_mechanism_design",
    "human_computer_interaction_experiment",
    "field_experiment_of_digital_artifact",
    "other",
}
METRIC_ROLES = {"primary_target", "primary_success_criterion", "constraint_or_tradeoff"}
BASIS_TYPES = {"theory_driven", "formal_analytical", "data_driven", "engineering_or_domain_knowledge", "hybrid"}
THEORY_ROLES = {"design_derivation", "mechanism_explanation", "boundary_conditions", "framing_only", "none"}
GATE_NAMES = (
    "purposeful_solution_design",
    "objective_metric_is_primary_target",
    "comparative_improvement_demonstrated",
    "objective_improvement_is_the_success_basis",
)


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


def require_enum(value: Any, allowed: set[str], field: str) -> str:
    normalized = str(value or "").strip()
    if normalized not in allowed:
        raise ValueError(f"invalid {field}: {normalized!r}")
    return normalized


def validate_decision(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")

    match = require_bool(payload.get("strict_objective_improvement_match"), "strict_objective_improvement_match")
    gates = require_dict(payload.get("gates"), "gates")
    flags = [require_bool(gates.get(name), f"gates.{name}") for name in GATE_NAMES]
    centrality = require_enum(payload.get("objective_metric_centrality"), CENTRALITY, "objective_metric_centrality")
    expected = all(flags) and centrality in {"exclusive", "dominant"}
    if match != expected:
        raise ValueError("match must equal gate AND and exclusive/dominant centrality")

    require_enum(payload.get("solution_layer"), SOLUTION_LAYERS, "solution_layer")
    paradigms = require_list(payload.get("research_paradigms"), "research_paradigms")
    for value in paradigms:
        require_enum(value, PARADIGMS, "research_paradigms[]")

    metrics = require_list(payload.get("objective_metrics"), "objective_metrics")
    for index, metric in enumerate(metrics):
        metric = require_dict(metric, f"objective_metrics[{index}]")
        require_enum(metric.get("metric_role"), METRIC_ROLES, f"objective_metrics[{index}].metric_role")
        require_list(metric.get("evidence"), f"objective_metrics[{index}].evidence")
    if match and not metrics:
        raise ValueError("retained article must include objective_metrics")

    knowledge = require_dict(payload.get("knowledge_and_design_basis"), "knowledge_and_design_basis")
    for value in require_list(knowledge.get("basis_types"), "knowledge_and_design_basis.basis_types"):
        require_enum(value, BASIS_TYPES, "knowledge_and_design_basis.basis_types[]")
    require_list(knowledge.get("named_theories_or_formalisms"), "knowledge_and_design_basis.named_theories_or_formalisms")
    require_enum(knowledge.get("theory_role"), THEORY_ROLES, "knowledge_and_design_basis.theory_role")
    require_dict(payload.get("research_logic"), "research_logic")

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
    keys = ("prompt_tokens", "completion_tokens", "total_tokens", "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")
    return {key: int(getattr(usage, key)) for key in keys if isinstance(getattr(usage, key, None), int)}


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


def analyze_one(path: Path, clients: ThreadClients, config: dict[str, Any], system_prompt: str, user_template: str, fingerprint: str) -> dict[str, Any]:
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
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
                temperature=float(model["temperature"]),
                max_tokens=int(model["max_tokens"]),
                response_format={"type": "json_object"},
            )
            choice = response.choices[0]
            content = choice.message.content or ""
            if not content.strip():
                reasoning = getattr(choice.message, "reasoning_content", None) or ""
                raise ValueError(f"empty response finish_reason={choice.finish_reason!r} reasoning_chars={len(reasoning)}")
            decision = validate_decision(parse_json_object(content), metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                "analysis_version": config["analysis_version"],
                "prompt_fingerprint": fingerprint,
                "model": model["name"],
                "analysis_mode": "one_complete_fulltext_one_request",
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
        "system_prompt": system_prompt,
        "user_template": user_template,
    }
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def write_reports(output_dir: Path, all_files: list[Path], decisions: dict[str, dict[str, Any]], config: dict[str, Any], fingerprint: str) -> None:
    rows = [decisions[name] for name in sorted(decisions)]
    retained = [row for row in rows if row.get("strict_objective_improvement_match") is True]
    centrality_counts = Counter(str(row.get("objective_metric_centrality")) for row in rows)
    layer_counts = Counter(str(row.get("solution_layer")) for row in retained)
    paradigm_counts = Counter(value for row in retained for value in (row.get("research_paradigms") or []))
    summary = {
        "updated_at": utc_now(),
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "max_concurrency": config["batch"]["max_concurrency"],
        "prompt_fingerprint": fingerprint,
        "input_fulltexts": len(all_files),
        "completed": len(rows),
        "pending": len(all_files) - len(rows),
        "strict_match_count": len(retained),
        "strict_nonmatch_count": len(rows) - len(retained),
        "gate_true_counts": {name: sum(bool((row.get("gates") or {}).get(name)) for row in rows) for name in GATE_NAMES},
        "centrality_counts": dict(sorted(centrality_counts.items())),
        "retained_solution_layer_counts": dict(sorted(layer_counts.items())),
        "retained_research_paradigm_counts": dict(sorted(paradigm_counts.items())),
        "usage": {key: sum(int((row.get("usage") or {}).get(key, 0)) for row in rows) for key in ("prompt_tokens", "completion_tokens", "total_tokens", "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")},
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    tmp_summary = output_dir / "summary.json.tmp"
    tmp_summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp_summary, output_dir / "summary.json")

    fields = [
        "record_id", "source_file", "title", "authors", "year", "journal", "doi",
        "strict_objective_improvement_match", *GATE_NAMES, "objective_metric_centrality",
        "solution_layer", "research_paradigms", "objective_metric_names", "basis_types",
        "theory_role", "focal_objective_cn", "proposed_solution_cn", "evaluation_logic_cn",
        "main_finding_cn", "decision_reason_cn", "confidence", "fulltext_chars", "attempts",
    ]
    tmp_csv = output_dir / "decisions.csv.tmp"
    with tmp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            gates = row.get("gates") or {}
            knowledge = row.get("knowledge_and_design_basis") or {}
            logic = row.get("research_logic") or {}
            writer.writerow({
                "record_id": row.get("record_id"), "source_file": row.get("source_file"),
                "title": row.get("title"), "authors": row.get("authors"), "year": row.get("year"),
                "journal": row.get("journal"), "doi": row.get("doi"),
                "strict_objective_improvement_match": row.get("strict_objective_improvement_match"),
                **{name: gates.get(name) for name in GATE_NAMES},
                "objective_metric_centrality": row.get("objective_metric_centrality"),
                "solution_layer": row.get("solution_layer"),
                "research_paradigms": " | ".join(row.get("research_paradigms") or []),
                "objective_metric_names": " | ".join(str(metric.get("metric_name") or "") for metric in (row.get("objective_metrics") or [])),
                "basis_types": " | ".join(knowledge.get("basis_types") or []),
                "theory_role": knowledge.get("theory_role"),
                "focal_objective_cn": logic.get("focal_objective_cn"),
                "proposed_solution_cn": logic.get("proposed_solution_cn"),
                "evaluation_logic_cn": logic.get("evaluation_logic_cn"),
                "main_finding_cn": logic.get("main_finding_cn"),
                "decision_reason_cn": row.get("decision_reason_cn"), "confidence": row.get("confidence"),
                "fulltext_chars": row.get("fulltext_chars"), "attempts": row.get("attempts"),
            })
    os.replace(tmp_csv, output_dir / "decisions.csv")

    markdown = [
        "# Strict objective-metric-improvement articles", "",
        f"Completed: {len(rows)} / {len(all_files)}", f"Retained: {len(retained)}", "",
    ]
    for row in sorted(retained, key=lambda item: (-float(item.get("confidence") or 0), str(item.get("title") or ""))):
        logic = row.get("research_logic") or {}
        knowledge = row.get("knowledge_and_design_basis") or {}
        metrics = row.get("objective_metrics") or []
        markdown.extend([
            f"## {row.get('title')}", "",
            f"- Year/journal: {row.get('year')} / {row.get('journal')}",
            f"- DOI: {row.get('doi')}",
            f"- Centrality: {row.get('objective_metric_centrality')}",
            f"- Solution layer: {row.get('solution_layer')}",
            f"- Paradigms: {', '.join(row.get('research_paradigms') or [])}",
            f"- Objective: {logic.get('focal_objective_cn', '')}",
            f"- Proposed solution: {logic.get('proposed_solution_cn', '')}",
            f"- Design basis: {knowledge.get('design_derivation_cn', '')}",
            f"- Evaluation: {logic.get('evaluation_logic_cn', '')}",
            f"- Main finding: {logic.get('main_finding_cn', '')}",
            f"- Progression: {logic.get('multi_study_or_stage_progression_cn', '')}",
            f"- Metrics: {'; '.join(str(metric.get('metric_name') or '') for metric in metrics)}",
            f"- Decision: {row.get('decision_reason_cn', '')}",
            f"- Confidence: {row.get('confidence')}", "",
        ])
    tmp_md = output_dir / "retained_articles.md.tmp"
    tmp_md.write_text("\n".join(markdown), encoding="utf-8")
    os.replace(tmp_md, output_dir / "retained_articles.md")


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
    all_files = sorted(input_dir.glob("*.md"))
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(encoding="utf-8").strip()
    fingerprint = prompt_fingerprint(config, system_prompt, user_template)
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    decisions = load_current(decisions_path, fingerprint)
    selected = all_files[args.offset :]
    pending = [path for path in selected if path.name not in decisions]
    if args.limit is not None:
        pending = pending[: args.limit]
    concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    print(f"scope={len(all_files)} completed={len(decisions)} pending_this_run={len(pending)} model={config['model']['name']} concurrency={concurrency}", flush=True)
    print(f"prompt_fingerprint={fingerprint}", flush=True)
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
    base_url = os.getenv(str(config["model"]["base_url_env"])) or str(config["model"]["base_url"])
    clients = ThreadClients(api_key, base_url, float(config["model"]["timeout_seconds"]))
    completed_now = 0
    failed_now = 0
    matches_now = 0
    started = time.monotonic()
    progress_interval = int(config["batch"]["progress_interval"])
    report_interval = int(config["batch"]["report_interval"])

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(analyze_one, path, clients, config, system_prompt, user_template, fingerprint): path for path in pending}
        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                row = future.result()
                append_jsonl(decisions_path, row)
                decisions[path.name] = row
                completed_now += 1
                matches_now += int(bool(row["strict_objective_improvement_match"]))
            except Exception as exc:
                failed_now += 1
                append_jsonl(errors_path, {
                    "source_file": path.name, "failed_at": utc_now(), "error_type": type(exc).__name__,
                    "error": str(exc), "prompt_fingerprint": fingerprint,
                })
                print(f"ERROR file={path.name} error={exc}", flush=True)
            handled = completed_now + failed_now
            if handled % progress_interval == 0:
                elapsed = time.monotonic() - started
                rate = handled / elapsed if elapsed else 0.0
                print(f"progress={handled}/{len(pending)} ok={completed_now} failed={failed_now} matches={matches_now} rate={rate:.2f}/s", flush=True)
            if handled % report_interval == 0:
                write_reports(output_dir, all_files, decisions, config, fingerprint)

    write_reports(output_dir, all_files, decisions, config, fingerprint)
    elapsed = time.monotonic() - started
    print(f"finished completed_now={completed_now} failed_now={failed_now} matches_now={matches_now} elapsed_seconds={elapsed:.1f}", flush=True)
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
