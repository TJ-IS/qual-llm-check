#!/usr/bin/env python3
"""Run one-fulltext-per-request writing-logic dissections for the retained corpus."""

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

ARCHETYPES = {
    "theory_derived_artifact_experiment",
    "build_evaluate_design_science",
    "computational_artifact_benchmark",
    "field_intervention_or_platform_experiment",
    "analytical_mechanism_or_optimization",
    "multi_method_or_multi_study_program",
    "action_research_or_longitudinal_change",
    "other",
}
WRITING_ARCS = {
    "problem_theory_design_test_return",
    "performance_gap_artifact_benchmark_generalize",
    "phenomenon_mechanism_intervention_field_test",
    "requirements_build_evaluate_design_principles",
    "formal_model_mechanism_simulation_policy",
    "iterative_diagnose_build_evaluate",
    "other",
}
COUPLINGS = {"direct", "partial", "none"}
STAGE2_LISTS = {
    "abstract_sentence_map",
    "introduction_sentence_map",
    "introduction_paragraph_map",
    "theory_to_design_sentence_map",
    "artifact_rationale_sentence_map",
    "study_opening_transition_and_closure_map",
    "discussion_and_contribution_sentence_map",
    "study_accumulation_logic",
    "claim_evidence_ledger",
    "writing_algorithm",
    "high_value_moves_to_mimic_cn",
    "superficial_moves_not_to_copy_cn",
    "unsupported_or_fragile_moves_cn",
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
            if row.get("source_base_match") is not True and row.get("base_match") is not True:
                continue
            source = str(row.get("source_file") or "")
            if not source:
                raise ValueError(f"missing source_file at {path}:{line_number}")
            if source in candidates:
                raise ValueError(f"duplicate source_file: {source}")
            candidates[source] = {
                "source_base_match": True,
                "source_theory_guided_subset_match": (
                    row.get("source_theory_guided_subset_match") is True
                    or row.get("theory_guided_subset_match") is True
                ),
                "source_primary_artifact_function": row.get("primary_artifact_function", ""),
                "source_primary_objective_family": row.get("primary_objective_family", ""),
                "source_application_context": row.get("application_context", ""),
            }
    return candidates


def load_jsonl_by_source(path: Path, fingerprint: str | None = None) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            if fingerprint is not None and row.get("prompt_fingerprint") != fingerprint:
                continue
            source = str(row.get("source_file") or "")
            if not source:
                raise ValueError(f"missing source_file at {path}:{line_number}")
            rows[source] = row
    return rows


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
        candidate = text[start : end + 1]
        try:
            payload = json.loads(candidate)
        except json.JSONDecodeError:
            repaired = re.sub(r",\s*([}\]])", r"\1", candidate)
            payload = json.loads(repaired)
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


def require_confidence(payload: dict[str, Any]) -> None:
    try:
        confidence = float(payload.get("confidence"))
    except (TypeError, ValueError) as exc:
        raise ValueError("confidence must be numeric") from exc
    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    payload["confidence"] = confidence


def validate_stage1(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    require_dict(payload.get("article_level_summary"), "article_level_summary")
    if payload.get("paper_archetype") not in ARCHETYPES:
        raise ValueError(f"invalid paper_archetype: {payload.get('paper_archetype')!r}")
    if payload.get("dominant_writing_arc") not in WRITING_ARCS:
        raise ValueError(f"invalid dominant_writing_arc: {payload.get('dominant_writing_arc')!r}")
    program = require_dict(payload.get("research_program"), "research_program")
    phases = require_list(program.get("studies_or_phases"), "research_program.studies_or_phases")
    try:
        phase_count = int(program.get("study_or_phase_count"))
    except (TypeError, ValueError) as exc:
        raise ValueError("research_program.study_or_phase_count must be an integer") from exc
    if phase_count != len(phases):
        raise ValueError("study_or_phase_count does not match studies_or_phases length")
    program["study_or_phase_count"] = phase_count
    require_dict(payload.get("rhetorical_architecture"), "rhetorical_architecture")
    trace = require_dict(payload.get("theory_to_design_trace"), "theory_to_design_trace")
    if trace.get("theory_design_coupling") not in COUPLINGS:
        raise ValueError("invalid theory_to_design_trace.theory_design_coupling")
    for field in ("evaluation_logic", "contribution_logic", "writing_techniques", "reusable_blueprint"):
        require_dict(payload.get(field), field)
    require_list(payload.get("sentence_level_move_map"), "sentence_level_move_map")
    require_confidence(payload)
    return payload


def validate_stage2(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    if not str(payload.get("verified_macro_scaffold_cn") or "").strip():
        raise ValueError("verified_macro_scaffold_cn is empty")
    for field in STAGE2_LISTS:
        require_list(payload.get(field), field)
    require_dict(payload.get("isr_positioning_logic"), "isr_positioning_logic")
    require_dict(payload.get("paragraph_level_mimicry_template"), "paragraph_level_mimicry_template")
    require_confidence(payload)
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


def analyze_one(
    path: Path,
    source_flags: dict[str, Any],
    stage_name: str,
    stage: dict[str, Any],
    config: dict[str, Any],
    system_prompt: str,
    user_template: str,
    stage1_row: dict[str, Any] | None,
    clients: ThreadClients,
    fingerprint: str,
) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, fulltext = parse_frontmatter(raw)
    metadata = metadata_for(path, fulltext, frontmatter)
    prompt_fields: dict[str, Any] = {**metadata, "fulltext": fulltext}
    if stage_name == "isr_micro":
        if stage1_row is None:
            raise ValueError("missing Stage 1 analysis")
        stage1_clean = {key: value for key, value in stage1_row.items() if key not in {"usage"}}
        prompt_fields["stage1_analysis"] = json.dumps(stage1_clean, ensure_ascii=False, indent=2)
    user_prompt = user_template.format(**prompt_fields)
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
                max_tokens=int(stage["max_tokens"]),
                response_format={"type": "json_object"},
            )
            choice = response.choices[0]
            content = choice.message.content or ""
            if not content.strip():
                reasoning = getattr(choice.message, "reasoning_content", None) or ""
                if reasoning.strip():
                    content = reasoning
                else:
                    raise ValueError(
                        f"empty response finish_reason={choice.finish_reason!r} reasoning_chars=0"
                    )
            try:
                payload = parse_json_object(content)
            except Exception as exc:
                raise ValueError(
                    f"response JSON invalid finish_reason={choice.finish_reason!r} "
                    f"content_chars={len(content)} usage={usage_dict(response)}: {exc}"
                ) from exc
            decision = validate_stage1(payload, metadata["record_id"]) if stage_name == "all231" else validate_stage2(payload, metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                **source_flags,
                "stage": stage_name,
                "analysis_version": stage["analysis_version"],
                "prompt_fingerprint": fingerprint,
                "model": model["name"],
                "analysis_mode": "one_complete_local_fulltext_per_request",
                "attempts": attempt,
                "finish_reason": choice.finish_reason,
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


def prompt_fingerprint(
    config: dict[str, Any], stage_name: str, stage: dict[str, Any], system_prompt: str, user_template: str
) -> str:
    value = {
        "analysis_version": stage["analysis_version"],
        "stage": stage_name,
        "model": config["model"]["name"],
        "source_decisions": config["source_decisions"],
        "max_tokens": stage["max_tokens"],
        "system_prompt": system_prompt,
        "user_template": user_template,
    }
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def safe_article_name(source_file: str) -> str:
    return Path(source_file).stem + ".json"


def write_reports(
    output_dir: Path,
    stage_name: str,
    candidate_names: list[str],
    decisions: dict[str, dict[str, Any]],
    stage: dict[str, Any],
    config: dict[str, Any],
    fingerprint: str,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    article_dir = output_dir / "articles"
    article_dir.mkdir(parents=True, exist_ok=True)
    rows = [decisions[name] for name in sorted(decisions)]
    for row in rows:
        target = article_dir / safe_article_name(str(row["source_file"]))
        tmp = target.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(row, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(tmp, target)

    usage_keys = ("prompt_tokens", "completion_tokens", "total_tokens", "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")
    summary: dict[str, Any] = {
        "updated_at": utc_now(),
        "stage": stage_name,
        "analysis_version": stage["analysis_version"],
        "model": config["model"]["name"],
        "prompt_fingerprint": fingerprint,
        "input_candidates": len(candidate_names),
        "completed": len(rows),
        "pending": len(candidate_names) - len(rows),
        "journal_counts": dict(sorted(Counter(str(row.get("journal") or "") for row in rows).items())),
        "year_counts": dict(sorted(Counter(str(row.get("year") or "") for row in rows).items())),
        "theory_subset_count": sum(row.get("source_theory_guided_subset_match") is True for row in rows),
        "usage": {key: sum(int((row.get("usage") or {}).get(key, 0)) for row in rows) for key in usage_keys},
    }
    if stage_name == "all231":
        summary.update(
            {
                "paper_archetype_counts": dict(sorted(Counter(str(row.get("paper_archetype") or "") for row in rows).items())),
                "dominant_writing_arc_counts": dict(sorted(Counter(str(row.get("dominant_writing_arc") or "") for row in rows).items())),
                "theory_design_coupling_counts": dict(sorted(Counter(str((row.get("theory_to_design_trace") or {}).get("theory_design_coupling") or "") for row in rows).items())),
                "study_or_phase_count_distribution": dict(sorted(Counter(str((row.get("research_program") or {}).get("study_or_phase_count") or 0) for row in rows).items())),
            }
        )
    else:
        summary.update(
            {
                "sentence_units": sum(
                    len(row.get(field) or [])
                    for row in rows
                    for field in (
                        "abstract_sentence_map", "introduction_sentence_map", "theory_to_design_sentence_map",
                        "artifact_rationale_sentence_map", "study_opening_transition_and_closure_map",
                        "discussion_and_contribution_sentence_map",
                    )
                ),
                "paragraph_units": sum(len(row.get("introduction_paragraph_map") or []) for row in rows),
            }
        )
    tmp_summary = output_dir / "summary.json.tmp"
    tmp_summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp_summary, output_dir / "summary.json")

    csv_fields = [
        "record_id", "source_file", "title", "authors", "year", "journal", "doi",
        "source_theory_guided_subset_match", "source_primary_artifact_function",
        "source_primary_objective_family", "source_application_context", "confidence",
        "paper_archetype", "dominant_writing_arc", "theory_design_coupling",
        "study_or_phase_count", "sentence_level_units", "attempts", "fulltext_chars",
    ]
    tmp_csv = output_dir / "article_index.csv.tmp"
    with tmp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields)
        writer.writeheader()
        for row in rows:
            sentence_units = len(row.get("sentence_level_move_map") or []) if stage_name == "all231" else sum(
                len(row.get(field) or [])
                for field in (
                    "abstract_sentence_map", "introduction_sentence_map", "theory_to_design_sentence_map",
                    "artifact_rationale_sentence_map", "study_opening_transition_and_closure_map",
                    "discussion_and_contribution_sentence_map",
                )
            )
            writer.writerow(
                {
                    "record_id": row.get("record_id"), "source_file": row.get("source_file"),
                    "title": row.get("title"), "authors": row.get("authors"), "year": row.get("year"),
                    "journal": row.get("journal"), "doi": row.get("doi"),
                    "source_theory_guided_subset_match": row.get("source_theory_guided_subset_match"),
                    "source_primary_artifact_function": row.get("source_primary_artifact_function"),
                    "source_primary_objective_family": row.get("source_primary_objective_family"),
                    "source_application_context": row.get("source_application_context"),
                    "confidence": row.get("confidence"), "paper_archetype": row.get("paper_archetype", ""),
                    "dominant_writing_arc": row.get("dominant_writing_arc", ""),
                    "theory_design_coupling": (row.get("theory_to_design_trace") or {}).get("theory_design_coupling", ""),
                    "study_or_phase_count": (row.get("research_program") or {}).get("study_or_phase_count", ""),
                    "sentence_level_units": sentence_units, "attempts": row.get("attempts"),
                    "fulltext_chars": row.get("fulltext_chars"),
                }
            )
    os.replace(tmp_csv, output_dir / "article_index.csv")

    markdown = [
        f"# {stage_name} article-level dissections", "",
        f"Completed: {len(rows)} / {len(candidate_names)}", "",
    ]
    for row in sorted(rows, key=lambda item: (str(item.get("journal")), str(item.get("year")), str(item.get("title")))):
        artifact = safe_article_name(str(row["source_file"]))
        marker = " · theory subset" if row.get("source_theory_guided_subset_match") else ""
        markdown.append(f"- {row.get('year')} · {row.get('journal')}{marker} · [{row.get('title')}](articles/{artifact})")
    tmp_md = output_dir / "article_index.md.tmp"
    tmp_md.write_text("\n".join(markdown) + "\n", encoding="utf-8")
    os.replace(tmp_md, output_dir / "article_index.md")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=("all231", "isr_micro"), required=True)
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
    stage = config["stages"][args.stage]
    input_dir = resolve_from_run(str(config["input_dir"]))
    source_path = resolve_from_run(str(config["source_decisions"]))
    output_dir = resolve_from_run(str(stage["output_dir"]))
    candidates = load_source_candidates(source_path)
    if len(candidates) != 231:
        raise ValueError(f"expected 231 retained candidates, found {len(candidates)}")
    local_files = {path.name: path for path in input_dir.glob("*.md")}
    missing = sorted(set(candidates) - set(local_files))
    if missing:
        raise FileNotFoundError(f"missing local full texts: {missing[:10]}")
    system_prompt = (RUN_DIR / str(stage["system_prompt"])).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / str(stage["user_template"])).read_text(encoding="utf-8").strip()
    fingerprint = prompt_fingerprint(config, args.stage, stage, system_prompt, user_template)
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    decisions = load_jsonl_by_source(decisions_path, fingerprint)
    for source_file, row in decisions.items():
        if source_file in candidates:
            row.update(candidates[source_file])

    journal_filter = str(stage.get("journal_filter") or "")
    candidate_names: list[str] = []
    for name in sorted(candidates):
        if journal_filter:
            raw = local_files[name].read_text(encoding="utf-8", errors="replace")
            frontmatter, fulltext = parse_frontmatter(raw)
            if metadata_for(local_files[name], fulltext, frontmatter)["journal"] != journal_filter:
                continue
        candidate_names.append(name)
    expected = 231 if args.stage == "all231" else 57
    if len(candidate_names) != expected:
        raise ValueError(f"expected {expected} candidates for {args.stage}, found {len(candidate_names)}")

    stage1_rows: dict[str, dict[str, Any]] = {}
    if args.stage == "isr_micro":
        stage1_path = resolve_from_run(str(stage["stage1_decisions"]))
        stage1_rows = load_jsonl_by_source(stage1_path)
        missing_stage1 = sorted(set(candidate_names) - set(stage1_rows))
        if missing_stage1:
            raise FileNotFoundError(f"missing Stage 1 analyses: {missing_stage1[:10]}")

    selected = candidate_names[args.offset :]
    pending_names = [name for name in selected if name not in decisions]
    if args.limit is not None:
        pending_names = pending_names[: args.limit]
    concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    print(
        f"stage={args.stage} scope={len(candidate_names)} completed={len(decisions)} "
        f"pending_this_run={len(pending_names)} model={config['model']['name']} concurrency={concurrency}",
        flush=True,
    )
    print(f"prompt_fingerprint={fingerprint}", flush=True)
    print(f"output_dir={output_dir}", flush=True)
    if args.dry_run:
        for name in pending_names[:10]:
            print(f"DRY_RUN file={name} bytes={local_files[name].stat().st_size}", flush=True)
        return 0
    if not pending_names:
        write_reports(output_dir, args.stage, candidate_names, decisions, stage, config, fingerprint)
        return 0

    env_file = resolve_from_run(str(config["env_file"]))
    load_dotenv(env_file)
    api_key = os.getenv(str(config["model"]["api_key_env"]))
    if not api_key:
        raise RuntimeError(f"missing API key env: {config['model']['api_key_env']}")
    base_url = os.getenv(str(config["model"]["base_url_env"])) or str(config["model"]["base_url"])
    clients = ThreadClients(api_key, base_url, float(config["model"]["timeout_seconds"]))
    completed_now = failed_now = 0
    started = time.monotonic()
    progress_interval = int(config["batch"]["progress_interval"])
    report_interval = int(config["batch"]["report_interval"])
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {
            pool.submit(
                analyze_one, local_files[name], candidates[name], args.stage, stage, config,
                system_prompt, user_template, stage1_rows.get(name), clients, fingerprint,
            ): name
            for name in pending_names
        }
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            try:
                row = future.result()
                append_jsonl(decisions_path, row)
                decisions[name] = row
                completed_now += 1
            except Exception as exc:
                failed_now += 1
                append_jsonl(
                    errors_path,
                    {
                        "source_file": name, "stage": args.stage, "failed_at": utc_now(),
                        "error_type": type(exc).__name__, "error": str(exc),
                        "prompt_fingerprint": fingerprint,
                    },
                )
                print(f"ERROR file={name} error={exc}", flush=True)
            handled = completed_now + failed_now
            if handled % progress_interval == 0:
                elapsed = time.monotonic() - started
                print(
                    f"progress={handled}/{len(pending_names)} ok={completed_now} failed={failed_now} "
                    f"rate={handled / elapsed if elapsed else 0:.2f}/s",
                    flush=True,
                )
            if handled % report_interval == 0:
                write_reports(output_dir, args.stage, candidate_names, decisions, stage, config, fingerprint)
    write_reports(output_dir, args.stage, candidate_names, decisions, stage, config, fingerprint)
    elapsed = time.monotonic() - started
    print(f"finished completed_now={completed_now} failed_now={failed_now} elapsed_seconds={elapsed:.1f}", flush=True)
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
