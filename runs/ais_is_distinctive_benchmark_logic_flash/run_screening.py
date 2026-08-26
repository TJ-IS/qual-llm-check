#!/usr/bin/env python3
"""Screen benchmark-improvement articles for genuinely IS-distinctive design logic."""

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
BASE_RUNNER = RUN_DIR.parent / "ais_basket_strict_objective_metric_improvement_all" / "run_screening.py"

spec = importlib.util.spec_from_file_location("stage1_runner", BASE_RUNNER)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load shared runner helpers: {BASE_RUNNER}")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

GATE_NAMES = (
    "objective_benchmark_remains_central",
    "is_specific_problem_or_phenomenon_is_central",
    "is_knowledge_materially_shapes_design",
    "is_logic_not_replaceable_by_generic_cs",
    "benchmark_tests_is_shaped_solution",
)
STRENGTHS = {"strong", "moderate", "borderline", "none"}
COUNTERFACTUALS = {
    "fails_without_is_logic",
    "partly_survives_but_materially_changes",
    "fully_survives_as_generic_cs",
}
WRITING_LOGICS = {
    "theory_to_design_to_benchmark",
    "context_requirements_to_artifact_to_benchmark",
    "behavioral_mechanism_to_digital_intervention_to_outcome",
    "sociotechnical_configuration_to_joint_performance",
    "platform_governance_to_market_or_welfare_outcome",
    "organizational_process_to_decision_support_to_operational_outcome",
    "institutional_constraint_to_digital_design_to_accountable_outcome",
    "other_is_distinctive",
}
THEORY_ROLES = {"design_derivation", "mechanism_explanation", "boundary_conditions", "framing_only", "none"}


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
    match = require_bool(payload.get("is_distinctive_benchmark_match"), "is_distinctive_benchmark_match")
    gates = require_dict(payload.get("gates"), "gates")
    flags = [require_bool(gates.get(name), f"gates.{name}") for name in GATE_NAMES]
    strength = require_enum(payload.get("is_distinctiveness_strength"), STRENGTHS, "is_distinctiveness_strength")
    counterfactual = require_enum(payload.get("cs_counterfactual_result"), COUNTERFACTUALS, "cs_counterfactual_result")
    expected = all(flags) and strength in {"strong", "moderate"} and counterfactual != "fully_survives_as_generic_cs"
    if match != expected:
        raise ValueError("match must equal gate AND plus strength/counterfactual constraints")
    writing_logics = require_list(payload.get("writing_logic_types"), "writing_logic_types")
    for value in writing_logics:
        require_enum(value, WRITING_LOGICS, "writing_logic_types[]")
    if match and not writing_logics:
        raise ValueError("retained article must identify a writing logic")
    design_basis = require_dict(payload.get("is_design_basis"), "is_design_basis")
    require_list(design_basis.get("named_theories_or_constructs"), "is_design_basis.named_theories_or_constructs")
    require_list(design_basis.get("non_theoretical_basis"), "is_design_basis.non_theoretical_basis")
    require_enum(design_basis.get("theory_role"), THEORY_ROLES, "is_design_basis.theory_role")
    benchmark = require_dict(payload.get("benchmark_evidence"), "benchmark_evidence")
    require_list(benchmark.get("objective_metrics"), "benchmark_evidence.objective_metrics")
    require_list(benchmark.get("comparators"), "benchmark_evidence.comparators")
    require_list(benchmark.get("evidence"), "benchmark_evidence.evidence")
    if match and (not benchmark["objective_metrics"] or not benchmark["comparators"]):
        raise ValueError("retained article must name objective metrics and comparators")
    require_dict(payload.get("writing_logic"), "writing_logic")
    try:
        confidence = float(payload.get("confidence"))
    except (TypeError, ValueError) as exc:
        raise ValueError("confidence must be numeric") from exc
    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    payload["confidence"] = confidence
    return payload


def load_candidates(config: dict[str, Any]) -> tuple[list[Path], dict[str, str]]:
    input_dir = resolve(config["input_dir"])
    origins: dict[str, str] = {}
    with resolve(config["stage1_decisions"]).open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("strict_objective_improvement_match") is True:
                origins[str(row["source_file"])] = "stage1_model_match"
    audit_path = resolve(config["manual_audit"])
    if audit_path.exists():
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        for row in audit.get("records", []):
            if row.get("manual_outcome") == "false_negative" and row.get("manual_strict_match") is True:
                origins[str(row["source_file"])] = "manual_audit_addition"
    missing = sorted(name for name in origins if not (input_dir / name).is_file())
    if missing:
        raise FileNotFoundError(f"candidate full texts missing: {missing[:10]}")
    paths = [input_dir / name for name in sorted(origins)]
    return paths, origins


def fingerprint(config: dict[str, Any], system_prompt: str, user_template: str, candidate_names: list[str]) -> str:
    value = {
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "system_prompt": system_prompt,
        "user_template": user_template,
        "candidate_names": candidate_names,
    }
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def analyze_one(path: Path, origin: str, clients: Any, config: dict[str, Any], system_prompt: str, user_template: str, prompt_hash: str) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, fulltext = base.parse_frontmatter(raw)
    metadata = base.metadata_for(path, fulltext, frontmatter)
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
                raise ValueError(f"empty response finish_reason={choice.finish_reason!r}")
            decision = validate(base.parse_json_object(content), metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                "candidate_origin": origin,
                "analysis_version": config["analysis_version"],
                "prompt_fingerprint": prompt_hash,
                "model": model["name"],
                "analysis_mode": "one_complete_fulltext_one_request",
                "attempts": attempt,
                "completed_at": base.utc_now(),
                **decision,
                "usage": base.usage_dict(response),
            }
        except Exception as exc:
            last_error = exc
            if attempt > int(batch["retries"]):
                break
            delay = float(batch["retry_base_delay_seconds"]) * (2 ** (attempt - 1))
            time.sleep(delay + random.uniform(0, 0.5))
    assert last_error is not None
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}") from last_error


def load_current(path: Path, prompt_hash: str) -> dict[str, dict[str, Any]]:
    decisions: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return decisions
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("prompt_fingerprint") == prompt_hash:
                source = str(row.get("source_file") or "")
                if not source:
                    raise ValueError(f"missing source_file at line {line_number}")
                decisions[source] = row
    return decisions


def write_reports(output_dir: Path, candidates: list[Path], decisions: dict[str, dict[str, Any]], config: dict[str, Any], prompt_hash: str) -> None:
    rows = [decisions[name] for name in sorted(decisions)]
    retained = [row for row in rows if row.get("is_distinctive_benchmark_match") is True]
    strengths = Counter(str(row.get("is_distinctiveness_strength")) for row in rows)
    counterfactuals = Counter(str(row.get("cs_counterfactual_result")) for row in rows)
    logics = Counter(value for row in retained for value in row.get("writing_logic_types", []))
    origin_counts = Counter(str(row.get("candidate_origin")) for row in rows)
    journal_counts = Counter(str(row.get("journal")) for row in retained)
    year_counts = Counter(str(row.get("year")) for row in retained)
    usage_keys = ("prompt_tokens", "completion_tokens", "total_tokens", "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")
    summary = {
        "updated_at": base.utc_now(),
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "max_concurrency": config["batch"]["max_concurrency"],
        "prompt_fingerprint": prompt_hash,
        "candidate_fulltexts": len(candidates),
        "completed": len(rows),
        "pending": len(candidates) - len(rows),
        "is_distinctive_benchmark_match_count": len(retained),
        "nonmatch_count": len(rows) - len(retained),
        "gate_true_counts": {name: sum(bool(row.get("gates", {}).get(name)) for row in rows) for name in GATE_NAMES},
        "strength_counts": dict(sorted(strengths.items())),
        "counterfactual_counts": dict(sorted(counterfactuals.items())),
        "retained_writing_logic_counts": dict(sorted(logics.items())),
        "completed_origin_counts": dict(sorted(origin_counts.items())),
        "retained_journal_counts": dict(sorted(journal_counts.items())),
        "retained_year_counts": dict(sorted(year_counts.items())),
        "usage": {key: sum(int(row.get("usage", {}).get(key, 0)) for row in rows) for key in usage_keys},
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    temporary = output_dir / "summary.json.tmp"
    temporary.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, output_dir / "summary.json")

    fields = [
        "record_id", "source_file", "title", "authors", "year", "journal", "doi", "candidate_origin",
        "is_distinctive_benchmark_match", *GATE_NAMES, "is_distinctiveness_strength", "cs_counterfactual_result",
        "writing_logic_types", "named_theories_or_constructs", "non_theoretical_basis", "theory_role",
        "objective_metrics", "comparators", "complete_writing_arc_cn", "generic_cs_counterfactual_cn",
        "decision_reason_cn", "confidence", "fulltext_chars", "attempts",
    ]
    temporary_csv = output_dir / "decisions.csv.tmp"
    with temporary_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            basis = row.get("is_design_basis", {})
            benchmark = row.get("benchmark_evidence", {})
            logic = row.get("writing_logic", {})
            writer.writerow({
                "record_id": row.get("record_id"), "source_file": row.get("source_file"), "title": row.get("title"),
                "authors": row.get("authors"), "year": row.get("year"), "journal": row.get("journal"), "doi": row.get("doi"),
                "candidate_origin": row.get("candidate_origin"), "is_distinctive_benchmark_match": row.get("is_distinctive_benchmark_match"),
                **{name: row.get("gates", {}).get(name) for name in GATE_NAMES},
                "is_distinctiveness_strength": row.get("is_distinctiveness_strength"),
                "cs_counterfactual_result": row.get("cs_counterfactual_result"),
                "writing_logic_types": " | ".join(row.get("writing_logic_types", [])),
                "named_theories_or_constructs": " | ".join(basis.get("named_theories_or_constructs", [])),
                "non_theoretical_basis": " | ".join(basis.get("non_theoretical_basis", [])), "theory_role": basis.get("theory_role"),
                "objective_metrics": " | ".join(benchmark.get("objective_metrics", [])),
                "comparators": " | ".join(benchmark.get("comparators", [])),
                "complete_writing_arc_cn": logic.get("complete_writing_arc_cn"),
                "generic_cs_counterfactual_cn": row.get("generic_cs_counterfactual_cn"),
                "decision_reason_cn": row.get("decision_reason_cn"), "confidence": row.get("confidence"),
                "fulltext_chars": row.get("fulltext_chars"), "attempts": row.get("attempts"),
            })
    os.replace(temporary_csv, output_dir / "decisions.csv")

    markdown = [
        "# IS-distinctive objective benchmark-improvement articles", "",
        f"Completed: {len(rows)} / {len(candidates)}", f"Retained: {len(retained)}", "",
    ]
    for row in sorted(retained, key=lambda item: (-float(item.get("confidence", 0)), str(item.get("title", "")) )):
        basis = row.get("is_design_basis", {})
        benchmark = row.get("benchmark_evidence", {})
        logic = row.get("writing_logic", {})
        markdown.extend([
            f"## {row.get('title')}", "",
            f"- Year/journal: {row.get('year')} / {row.get('journal')}",
            f"- DOI: {row.get('doi')}", f"- Candidate origin: {row.get('candidate_origin')}",
            f"- Strength/counterfactual: {row.get('is_distinctiveness_strength')} / {row.get('cs_counterfactual_result')}",
            f"- Writing logic types: {', '.join(row.get('writing_logic_types', []))}",
            f"- IS problem/gap: {logic.get('is_problem_and_gap_cn', '')}",
            f"- Design basis: {logic.get('design_basis_cn', '')}",
            f"- Design translation: {basis.get('design_translation_cn', '')}",
            f"- Design move: {logic.get('design_move_cn', '')}",
            f"- Artifact/intervention: {logic.get('artifact_or_intervention_cn', '')}",
            f"- Metrics: {'; '.join(benchmark.get('objective_metrics', []))}",
            f"- Comparators: {'; '.join(benchmark.get('comparators', []))}",
            f"- Evaluation: {logic.get('objective_evaluation_cn', '')}",
            f"- Improvement: {benchmark.get('demonstrated_improvement_cn', '')}",
            f"- Return to IS contribution: {logic.get('return_to_is_contribution_cn', '')}",
            f"- Complete writing arc: {logic.get('complete_writing_arc_cn', '')}",
            f"- Generic-CS counterfactual: {row.get('generic_cs_counterfactual_cn', '')}",
            f"- Decision: {row.get('decision_reason_cn', '')}", f"- Confidence: {row.get('confidence')}", "",
        ])
    temporary_md = output_dir / "retained_articles.md.tmp"
    temporary_md.write_text("\n".join(markdown), encoding="utf-8")
    os.replace(temporary_md, output_dir / "retained_articles.md")


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
    candidates, origins = load_candidates(config)
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(encoding="utf-8").strip()
    prompt_hash = fingerprint(config, system_prompt, user_template, [path.name for path in candidates])
    output_dir = resolve(config["output_dir"])
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    decisions = load_current(decisions_path, prompt_hash)
    pending = [path for path in candidates if path.name not in decisions]
    if args.limit is not None:
        pending = pending[:args.limit]
    concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    print(f"scope={len(candidates)} completed={len(decisions)} pending_this_run={len(pending)} model={config['model']['name']} concurrency={concurrency}", flush=True)
    print(f"origins={dict(Counter(origins.values()))}", flush=True)
    print(f"prompt_fingerprint={prompt_hash}", flush=True)
    print(f"output_dir={output_dir}", flush=True)
    if args.dry_run:
        for path in pending[:10]:
            print(f"DRY_RUN origin={origins[path.name]} file={path.name} bytes={path.stat().st_size}", flush=True)
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
    progress_interval = int(config["batch"]["progress_interval"])
    report_interval = int(config["batch"]["report_interval"])
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {
            pool.submit(analyze_one, path, origins[path.name], clients, config, system_prompt, user_template, prompt_hash): path
            for path in pending
        }
        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                row = future.result()
                base.append_jsonl(decisions_path, row)
                decisions[path.name] = row
                completed_now += 1
                matches_now += int(bool(row["is_distinctive_benchmark_match"]))
            except Exception as exc:
                failed_now += 1
                base.append_jsonl(errors_path, {
                    "source_file": path.name, "failed_at": base.utc_now(), "error_type": type(exc).__name__,
                    "error": str(exc), "prompt_fingerprint": prompt_hash,
                })
                print(f"ERROR file={path.name} error={exc}", flush=True)
            handled = completed_now + failed_now
            if handled % progress_interval == 0:
                elapsed = time.monotonic() - started
                print(f"progress={handled}/{len(pending)} ok={completed_now} failed={failed_now} matches={matches_now} rate={handled / elapsed:.2f}/s", flush=True)
            if handled % report_interval == 0:
                write_reports(output_dir, candidates, decisions, config, prompt_hash)
    write_reports(output_dir, candidates, decisions, config, prompt_hash)
    elapsed = time.monotonic() - started
    print(f"finished completed_now={completed_now} failed_now={failed_now} matches_now={matches_now} elapsed_seconds={elapsed:.1f}", flush=True)
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
