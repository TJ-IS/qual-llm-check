#!/usr/bin/env python3
"""Screen IS benchmark articles for coding-agent-specific metric transfer."""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import importlib.util
import json
import os
import random
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
CONFIG_PATH = RUN_DIR / "config.json"
STAGE2_RUNNER = RUN_DIR.parent / "ais_is_distinctive_benchmark_logic_flash" / "run_screening.py"
spec = importlib.util.spec_from_file_location("stage2_runner", STAGE2_RUNNER)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load shared helpers: {STAGE2_RUNNER}")
stage2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage2)
base = stage2.base

GATE_NAMES = (
    "source_design_outcome_logic_is_transferable",
    "proposed_metric_is_objective_and_reproducible",
    "coding_agent_essentiality",
    "metric_is_manipulable_by_artifact_design",
    "feasible_objective_benchmark",
    "supports_a_multi_study_thesis_series",
)
LEVELS = {"strong", "moderate", "weak", "none"}
METRIC_FAMILIES = {
    "verified_autonomous_change_success",
    "repository_state_and_situational_awareness",
    "specification_and_change_scope_fidelity",
    "cross_artifact_repository_coherence",
    "tool_trajectory_efficiency",
    "calibrated_escalation_and_oversight_burden",
    "failure_recovery_and_workspace_resilience",
    "human_agent_handoff_and_reviewability",
    "long_horizon_adaptation_and_memory",
    "security_safety_and_policy_conformance",
    "other_coding_agent_specific",
}
UNITS = {"task", "trajectory", "handoff", "repository_episode", "multi_task_sequence"}


def resolve(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (RUN_DIR / path).resolve()


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


def validate(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    match = require_bool(payload.get("coding_agent_metric_transfer_match"), "coding_agent_metric_transfer_match")
    gates = require_dict(payload.get("gates"), "gates")
    flags = [require_bool(gates.get(name), f"gates.{name}") for name in GATE_NAMES]
    strength = require_enum(payload.get("transfer_strength"), LEVELS, "transfer_strength")
    necessity = require_enum(payload.get("coding_agent_necessity"), LEVELS, "coding_agent_necessity")
    expected = all(flags) and strength in {"strong", "moderate"} and necessity in {"strong", "moderate"}
    if match != expected:
        raise ValueError("match must equal gate AND plus strength/necessity constraints")
    require_enum(payload.get("primary_metric_family"), METRIC_FAMILIES, "primary_metric_family")
    for value in require_list(payload.get("secondary_metric_families"), "secondary_metric_families"):
        require_enum(value, METRIC_FAMILIES, "secondary_metric_families[]")
    transfer = require_dict(payload.get("source_to_coding_agent_transfer"), "source_to_coding_agent_transfer")
    require_list(transfer.get("source_objective_metrics"), "source_to_coding_agent_transfer.source_objective_metrics")
    require_list(transfer.get("source_evidence"), "source_to_coding_agent_transfer.source_evidence")
    metric = require_dict(payload.get("proposed_coding_agent_metric"), "proposed_coding_agent_metric")
    require_enum(metric.get("unit_of_analysis"), UNITS, "proposed_coding_agent_metric.unit_of_analysis")
    require_list(metric.get("observable_inputs"), "proposed_coding_agent_metric.observable_inputs")
    require_list(metric.get("minimum_success_conditions"), "proposed_coding_agent_metric.minimum_success_conditions")
    counterfactuals = require_dict(payload.get("coding_agent_counterfactuals"), "coding_agent_counterfactuals")
    for key in ("one_shot_generation_cn", "human_developer_alone_cn", "generic_noncoding_agent_cn", "necessity_conclusion_cn"):
        if not str(counterfactuals.get(key) or "").strip():
            raise ValueError(f"coding_agent_counterfactuals.{key} required")
    thesis = require_dict(payload.get("thesis_series_structure"), "thesis_series_structure")
    dimensions = require_list(thesis.get("dimensions_or_stages"), "thesis_series_structure.dimensions_or_stages")
    if match and len(dimensions) < 3:
        raise ValueError("retained metric needs at least three dimensions/stages")
    for index, dimension in enumerate(dimensions):
        dimension = require_dict(dimension, f"dimensions_or_stages[{index}]")
        require_list(dimension.get("candidate_design_levers"), f"dimensions_or_stages[{index}].candidate_design_levers")
    feasible = require_dict(payload.get("feasible_benchmark_design"), "feasible_benchmark_design")
    require_list(feasible.get("baselines_or_controls"), "feasible_benchmark_design.baselines_or_controls")
    require_list(feasible.get("measurement_infrastructure"), "feasible_benchmark_design.measurement_infrastructure")
    if match and not feasible["baselines_or_controls"]:
        raise ValueError("retained metric needs a baseline/control")
    try:
        confidence = float(payload.get("confidence"))
    except (TypeError, ValueError) as exc:
        raise ValueError("confidence must be numeric") from exc
    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    payload["confidence"] = confidence
    return payload


def load_candidates(config: dict[str, Any]) -> tuple[list[Path], dict[str, dict[str, Any]]]:
    input_dir = resolve(config["input_dir"])
    analyses: dict[str, dict[str, Any]] = {}
    with resolve(config["stage2_decisions"]).open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("is_distinctive_benchmark_match") is True:
                analyses[str(row["source_file"])] = row
    missing = sorted(name for name in analyses if not (input_dir / name).is_file())
    if missing:
        raise FileNotFoundError(f"candidate full texts missing: {missing[:10]}")
    return [input_dir / name for name in sorted(analyses)], analyses


def prompt_fingerprint(config: dict[str, Any], system_prompt: str, user_template: str, candidates: list[str]) -> str:
    value = {
        "analysis_version": config["analysis_version"], "model": config["model"]["name"],
        "system_prompt": system_prompt, "user_template": user_template, "candidates": candidates,
    }
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def compact_stage2(row: dict[str, Any]) -> str:
    keys = (
        "is_distinctiveness_strength", "cs_counterfactual_result", "writing_logic_types",
        "is_design_basis", "benchmark_evidence", "writing_logic", "generic_cs_counterfactual_cn", "decision_reason_cn",
    )
    return json.dumps({key: row.get(key) for key in keys}, ensure_ascii=False, separators=(",", ":"))


def analyze_one(path: Path, prior: dict[str, Any], clients: Any, config: dict[str, Any], system_prompt: str, user_template: str, prompt_hash: str) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, fulltext = base.parse_frontmatter(raw)
    metadata = base.metadata_for(path, fulltext, frontmatter)
    user_prompt = user_template.format(**metadata, fulltext=fulltext, stage2_analysis=compact_stage2(prior))
    model, batch = config["model"], config["batch"]
    last_error: BaseException | None = None
    for attempt in range(1, int(batch["retries"]) + 2):
        try:
            response = clients.get().chat.completions.create(
                model=model["name"],
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
                temperature=float(model["temperature"]), max_tokens=int(model["max_tokens"]),
                response_format={"type": "json_object"},
            )
            content = response.choices[0].message.content or ""
            if not content.strip():
                raise ValueError(f"empty response finish_reason={response.choices[0].finish_reason!r}")
            decision = validate(base.parse_json_object(content), metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                "source_stage2_strength": prior.get("is_distinctiveness_strength"),
                "source_stage2_writing_logic_types": prior.get("writing_logic_types", []),
                "analysis_version": config["analysis_version"], "prompt_fingerprint": prompt_hash,
                "model": model["name"], "analysis_mode": "one_complete_fulltext_plus_own_stage2_analysis_one_request",
                "attempts": attempt, "completed_at": base.utc_now(), **decision, "usage": base.usage_dict(response),
            }
        except Exception as exc:
            last_error = exc
            if attempt > int(batch["retries"]):
                break
            time.sleep(float(batch["retry_base_delay_seconds"]) * (2 ** (attempt - 1)) + random.uniform(0, 0.5))
    assert last_error is not None
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}") from last_error


def load_current(path: Path, prompt_hash: str) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                if row.get("prompt_fingerprint") == prompt_hash:
                    rows[str(row["source_file"])] = row
    return rows


def write_reports(output_dir: Path, candidates: list[Path], decisions: dict[str, dict[str, Any]], config: dict[str, Any], prompt_hash: str) -> None:
    rows = [decisions[name] for name in sorted(decisions)]
    retained = [row for row in rows if row.get("coding_agent_metric_transfer_match") is True]
    primary = Counter(str(row.get("primary_metric_family")) for row in retained)
    secondary = Counter(value for row in retained for value in row.get("secondary_metric_families", []))
    strengths = Counter(str(row.get("transfer_strength")) for row in rows)
    necessities = Counter(str(row.get("coding_agent_necessity")) for row in rows)
    usage_keys = ("prompt_tokens", "completion_tokens", "total_tokens", "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")
    summary = {
        "updated_at": base.utc_now(), "analysis_version": config["analysis_version"], "model": config["model"]["name"],
        "max_concurrency": config["batch"]["max_concurrency"], "prompt_fingerprint": prompt_hash,
        "candidate_fulltexts": len(candidates), "completed": len(rows), "pending": len(candidates) - len(rows),
        "coding_agent_metric_transfer_match_count": len(retained), "nonmatch_count": len(rows) - len(retained),
        "gate_true_counts": {name: sum(bool(row.get("gates", {}).get(name)) for row in rows) for name in GATE_NAMES},
        "transfer_strength_counts": dict(sorted(strengths.items())), "coding_agent_necessity_counts": dict(sorted(necessities.items())),
        "retained_primary_metric_family_counts": dict(sorted(primary.items())),
        "retained_secondary_metric_family_counts": dict(sorted(secondary.items())),
        "usage": {key: sum(int(row.get("usage", {}).get(key, 0)) for row in rows) for key in usage_keys},
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    tmp = output_dir / "summary.json.tmp"
    tmp.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, output_dir / "summary.json")

    fields = [
        "record_id", "source_file", "title", "authors", "year", "journal", "doi", "coding_agent_metric_transfer_match",
        *GATE_NAMES, "transfer_strength", "coding_agent_necessity", "primary_metric_family", "secondary_metric_families",
        "metric_name_en", "metric_name_cn", "construct_definition_cn", "unit_of_analysis", "calculation_cn",
        "unifying_outcome_cn", "dimensions_or_stages", "baselines_or_controls", "structural_analogy_cn",
        "necessity_conclusion_cn", "decision_reason_cn", "confidence", "fulltext_chars", "attempts",
    ]
    tmp_csv = output_dir / "decisions.csv.tmp"
    with tmp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            metric = row.get("proposed_coding_agent_metric", {})
            thesis = row.get("thesis_series_structure", {})
            transfer = row.get("source_to_coding_agent_transfer", {})
            counter = row.get("coding_agent_counterfactuals", {})
            feasible = row.get("feasible_benchmark_design", {})
            writer.writerow({
                "record_id": row.get("record_id"), "source_file": row.get("source_file"), "title": row.get("title"),
                "authors": row.get("authors"), "year": row.get("year"), "journal": row.get("journal"), "doi": row.get("doi"),
                "coding_agent_metric_transfer_match": row.get("coding_agent_metric_transfer_match"),
                **{name: row.get("gates", {}).get(name) for name in GATE_NAMES},
                "transfer_strength": row.get("transfer_strength"), "coding_agent_necessity": row.get("coding_agent_necessity"),
                "primary_metric_family": row.get("primary_metric_family"),
                "secondary_metric_families": " | ".join(row.get("secondary_metric_families", [])),
                "metric_name_en": metric.get("metric_name_en"), "metric_name_cn": metric.get("metric_name_cn"),
                "construct_definition_cn": metric.get("construct_definition_cn"), "unit_of_analysis": metric.get("unit_of_analysis"),
                "calculation_cn": metric.get("calculation_cn"), "unifying_outcome_cn": thesis.get("unifying_outcome_cn"),
                "dimensions_or_stages": json.dumps(thesis.get("dimensions_or_stages", []), ensure_ascii=False),
                "baselines_or_controls": " | ".join(feasible.get("baselines_or_controls", [])),
                "structural_analogy_cn": transfer.get("structural_analogy_cn"),
                "necessity_conclusion_cn": counter.get("necessity_conclusion_cn"),
                "decision_reason_cn": row.get("decision_reason_cn"), "confidence": row.get("confidence"),
                "fulltext_chars": row.get("fulltext_chars"), "attempts": row.get("attempts"),
            })
    os.replace(tmp_csv, output_dir / "decisions.csv")

    markdown = ["# Coding-agent-specific metric-transfer candidates", "", f"Completed: {len(rows)} / {len(candidates)}", f"Retained: {len(retained)}", ""]
    for row in sorted(retained, key=lambda item: (-float(item.get("confidence", 0)), str(item.get("title", "")))):
        metric = row.get("proposed_coding_agent_metric", {})
        transfer = row.get("source_to_coding_agent_transfer", {})
        counter = row.get("coding_agent_counterfactuals", {})
        thesis = row.get("thesis_series_structure", {})
        feasible = row.get("feasible_benchmark_design", {})
        markdown.extend([
            f"## {row.get('title')}", "", f"- Year/journal: {row.get('year')} / {row.get('journal')}", f"- DOI: {row.get('doi')}",
            f"- Transfer/necessity: {row.get('transfer_strength')} / {row.get('coding_agent_necessity')}",
            f"- Metric family: {row.get('primary_metric_family')}", f"- Proposed metric: {metric.get('metric_name_en')} / {metric.get('metric_name_cn')}",
            f"- Construct: {metric.get('construct_definition_cn')}", f"- Unit: {metric.get('unit_of_analysis')}",
            f"- Calculation: {metric.get('calculation_cn')}", f"- Source mechanism: {transfer.get('source_design_mechanism_cn')}",
            f"- Structural analogy: {transfer.get('structural_analogy_cn')}", f"- Coding-agent necessity: {counter.get('necessity_conclusion_cn')}",
            f"- Unifying thesis outcome: {thesis.get('unifying_outcome_cn')}",
            f"- Dimensions/stages: {json.dumps(thesis.get('dimensions_or_stages', []), ensure_ascii=False)}",
            f"- Baselines: {'; '.join(feasible.get('baselines_or_controls', []))}",
            f"- Tasks/data: {feasible.get('tasks_and_data_cn')}", f"- Decision: {row.get('decision_reason_cn')}",
            f"- Confidence: {row.get('confidence')}", "",
        ])
    tmp_md = output_dir / "retained_metric_transfers.md.tmp"
    tmp_md.write_text("\n".join(markdown), encoding="utf-8")
    os.replace(tmp_md, output_dir / "retained_metric_transfers.md")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--max-concurrency", type=int)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    if args.max_concurrency is not None and not 1 <= args.max_concurrency <= 500:
        parser.error("--max-concurrency must be between 1 and 500")
    return args


def main() -> int:
    args = parse_args()
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    candidates, priors = load_candidates(config)
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(encoding="utf-8").strip()
    prompt_hash = prompt_fingerprint(config, system_prompt, user_template, [path.name for path in candidates])
    output_dir = resolve(config["output_dir"])
    decisions_path, errors_path = output_dir / "decisions.jsonl", output_dir / "errors.jsonl"
    decisions = load_current(decisions_path, prompt_hash)
    pending = [path for path in candidates if path.name not in decisions]
    if args.limit is not None:
        pending = pending[:args.limit]
    concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    print(f"scope={len(candidates)} completed={len(decisions)} pending_this_run={len(pending)} model={config['model']['name']} concurrency={concurrency}", flush=True)
    print(f"prompt_fingerprint={prompt_hash}", flush=True)
    print(f"output_dir={output_dir}", flush=True)
    if args.dry_run:
        for path in pending[:10]:
            print(f"DRY_RUN file={path.name} bytes={path.stat().st_size}", flush=True)
        return 0
    if not pending:
        write_reports(output_dir, candidates, decisions, config, prompt_hash)
        return 0
    base.load_dotenv(resolve(config["env_file"]))
    api_key = os.getenv(config["model"]["api_key_env"])
    if not api_key:
        raise RuntimeError(f"missing API key env: {config['model']['api_key_env']}")
    base_url = os.getenv(config["model"]["base_url_env"]) or config["model"]["base_url"]
    clients = base.ThreadClients(api_key, base_url, float(config["model"]["timeout_seconds"]))
    completed_now = failed_now = matches_now = 0
    started = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {
            pool.submit(analyze_one, path, priors[path.name], clients, config, system_prompt, user_template, prompt_hash): path
            for path in pending
        }
        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                row = future.result()
                base.append_jsonl(decisions_path, row)
                decisions[path.name] = row
                completed_now += 1
                matches_now += int(bool(row["coding_agent_metric_transfer_match"]))
            except Exception as exc:
                failed_now += 1
                base.append_jsonl(errors_path, {"source_file": path.name, "failed_at": base.utc_now(), "error_type": type(exc).__name__, "error": str(exc), "prompt_fingerprint": prompt_hash})
                print(f"ERROR file={path.name} error={exc}", flush=True)
            handled = completed_now + failed_now
            if handled % int(config["batch"]["progress_interval"]) == 0:
                elapsed = time.monotonic() - started
                print(f"progress={handled}/{len(pending)} ok={completed_now} failed={failed_now} matches={matches_now} rate={handled / elapsed:.2f}/s", flush=True)
            if handled % int(config["batch"]["report_interval"]) == 0:
                write_reports(output_dir, candidates, decisions, config, prompt_hash)
    write_reports(output_dir, candidates, decisions, config, prompt_hash)
    elapsed = time.monotonic() - started
    print(f"finished completed_now={completed_now} failed_now={failed_now} matches_now={matches_now} elapsed_seconds={elapsed:.1f}", flush=True)
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
