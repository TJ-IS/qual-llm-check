#!/usr/bin/env python3
"""Two-stage, one-fulltext-per-request strict objective-metric screening."""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
import random
import re
import threading
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


RUN_DIR = Path(__file__).resolve().parent
CONFIG = json.loads((RUN_DIR / "config.json").read_text(encoding="utf-8"))
GATE_KEYS = (
    "designed_software_artifact",
    "core_objective_improvement_target",
    "fully_objective_measurement",
    "all_core_success_outcomes_objective",
    "comparative_improvement_demonstrated",
)
ARTIFACT_GATE_KEYS = (
    "explicit_artifact_class",
    "explicit_designed_component_relation",
    "material_software_implementation_or_instantiation",
)
ALLOWED_ARTIFACT_STATUSES = {"explicit_software_artifact", "explicit_component_of_software_artifact"}
ALL_ARTIFACT_STATUSES = ALLOWED_ARTIFACT_STATUSES | {
    "algorithm_or_model_only",
    "analytical_rule_or_method_only",
    "platform_only_context",
    "concept_or_future_design_only",
    "unclear",
}
ALLOWED_STATUSES = {"fully_objective", "benchmark_objective_with_fixed_labels"}
ALL_STATUSES = ALLOWED_STATUSES | {
    "mixed_objective_subjective",
    "human_judged_output",
    "subjective_or_self_report",
    "unclear",
    "no_qualifying_metric",
}
ALL_ROLES = {"exclusive", "dominant", "mixed", "secondary", "none"}
YEAR_RE = re.compile(r"^\d+_(\d{4})_")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def resolve(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (RUN_DIR / path).resolve()


def parse_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    text = raw.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    metadata: dict[str, Any] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        try:
            metadata[key.strip()] = json.loads(value)
        except json.JSONDecodeError:
            metadata[key.strip()] = value
    return metadata, text[end + 5 :].lstrip()


def read_article(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    front, fulltext = parse_frontmatter(raw)
    parts = path.name.split("_", 2)
    year_match = YEAR_RE.match(path.name)
    meta = {
        "record_id": str(front.get("otero_id") or (parts[0].lstrip("0") or "0")),
        "source_file": path.name,
        "title": str(front.get("title") or path.stem),
        "authors": str(front.get("authors") or ""),
        "year": str(front.get("year") or (year_match.group(1) if year_match else "")),
        "journal": str(front.get("journal") or ""),
        "doi": str(front.get("doi") or ""),
        "fulltext_chars": len(fulltext),
    }
    return meta, fulltext


def article_paths() -> list[Path]:
    year_from = int(CONFIG["year_range"]["from"])
    year_to = int(CONFIG["year_range"]["to"])
    result = []
    for path in resolve(CONFIG["input_dir"]).glob("*.md"):
        match = YEAR_RE.match(path.name)
        if match and year_from <= int(match.group(1)) <= year_to:
            result.append(path)
    return sorted(result, key=lambda p: p.name)


def parse_json_object(content: str) -> dict[str, Any]:
    text = (content or "").strip()
    if not text:
        raise ValueError("empty model response")
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end <= start:
        raise ValueError("response has no JSON object")
    candidate = text[start : end + 1]
    try:
        payload = json.loads(candidate)
    except json.JSONDecodeError:
        payload = json.loads(re.sub(r",\s*([}\]])", r"\1", candidate))
    if not isinstance(payload, dict):
        raise ValueError("model response is not a JSON object")
    return payload


def validate(payload: dict[str, Any], record_id: str, stage: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    gates = payload.get("gates")
    if not isinstance(gates, dict):
        raise ValueError("gates must be an object")
    gate_values = []
    gate_keys = ARTIFACT_GATE_KEYS if stage == "stage3" else GATE_KEYS
    for key in gate_keys:
        value = gates.get(key)
        if not isinstance(value, bool):
            raise ValueError(f"gates.{key} must be boolean")
        gate_values.append(value)
    final_key = "strict_match" if stage == "stage1" else "confirmed_strict_match" if stage == "stage2" else "artifact_confirmed"
    final_value = payload.get(final_key)
    if not isinstance(final_value, bool):
        raise ValueError(f"{final_key} must be boolean")
    if stage == "stage3":
        status = str(payload.get("artifact_status") or "")
        if status not in ALL_ARTIFACT_STATUSES:
            raise ValueError(f"invalid artifact_status: {status}")
        expected = all(gate_values) and status in ALLOWED_ARTIFACT_STATUSES
        if final_value != expected:
            raise ValueError(f"{final_key} is logically inconsistent")
        role = ""
    else:
        status = str(payload.get("objective_status") or "")
        role = str(payload.get("core_role") or "")
        if status not in ALL_STATUSES:
            raise ValueError(f"invalid objective_status: {status}")
        if role not in ALL_ROLES:
            raise ValueError(f"invalid core_role: {role}")
        expected = all(gate_values) and status in ALLOWED_STATUSES and role in {"exclusive", "dominant"}
        if final_value != expected:
            raise ValueError(f"{final_key} is logically inconsistent")
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


def prompt_files(stage: str) -> tuple[str, str]:
    system = (RUN_DIR / f"{stage}_system_prompt_cn.md").read_text(encoding="utf-8")
    user = (RUN_DIR / f"{stage}_user_template_cn.md").read_text(encoding="utf-8")
    return system, user


def prompt_fingerprint(stage: str, system: str, user: str) -> str:
    basis = {
        "analysis_version": CONFIG["analysis_version"],
        "stage": stage,
        "model": CONFIG["model"]["name"],
        "year_range": CONFIG["year_range"],
        "system": system,
        "user": user,
    }
    return hashlib.sha256(json.dumps(basis, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def fill_template(template: str, meta: dict[str, Any], fulltext: str, stage1: dict[str, Any] | None) -> str:
    values = {key: str(value) for key, value in meta.items()}
    values["fulltext"] = fulltext
    values["stage1_decision"] = json.dumps(stage1 or {}, ensure_ascii=False, indent=2)
    return template.format(**values)


def analyze_one(
    path: Path,
    stage: str,
    stage1: dict[str, Any] | None,
    clients: ThreadClients,
    system: str,
    user_template: str,
    fingerprint: str,
) -> dict[str, Any]:
    meta, fulltext = read_article(path)
    user = fill_template(user_template, meta, fulltext, stage1)
    model = CONFIG["model"]
    retries = int(CONFIG["batch"]["retries"])
    last_error: Exception | None = None
    for attempt in range(1, retries + 2):
        try:
            response = clients.get().chat.completions.create(
                model=str(model["name"]),
                messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                temperature=float(model["temperature"]),
                max_tokens=int(model["max_tokens"]),
                response_format={"type": "json_object"},
            )
            message = response.choices[0].message
            content = message.content or getattr(message, "reasoning_content", None) or ""
            decision = validate(parse_json_object(content), str(meta["record_id"]), stage)
            return {
                **meta,
                "analysis_version": CONFIG["analysis_version"],
                "stage": stage,
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
            if attempt > retries:
                break
            delay = float(CONFIG["batch"]["retry_base_delay_seconds"]) * (2 ** (attempt - 1))
            time.sleep(delay + random.uniform(0, 0.5))
    assert last_error is not None
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}") from last_error


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def load_rows(path: Path, fingerprint: str | None = None) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            if fingerprint is not None and row.get("prompt_fingerprint") != fingerprint:
                continue
            source = str(row.get("source_file") or "")
            if source:
                rows[source] = row
    return rows


def stage_candidates(stage: str) -> list[tuple[Path, dict[str, Any] | None]]:
    paths = {path.name: path for path in article_paths()}
    if stage == "stage1":
        return [(path, None) for path in paths.values()]
    if stage == "stage3":
        stage2_rows = load_rows(RUN_DIR / "output_stage2" / "decisions.jsonl")
        old_path = RUN_DIR.parent / "ais_basket_objective_software_psych_theory_2020_2027_flash" / "output_v1" / "decisions.jsonl"
        old_rows = load_rows(old_path)
        conflicts = [
            row for source, row in stage2_rows.items()
            if row.get("confirmed_strict_match") is True
            and not bool(((old_rows.get(source) or {}).get("software_artifact") or {}).get("pass"))
        ]
        return sorted([(paths[str(row["source_file"])], row) for row in conflicts if str(row["source_file"]) in paths], key=lambda item: item[0].name)
    stage1_rows = load_rows(RUN_DIR / "output_stage1" / "decisions.jsonl")
    positives = [row for row in stage1_rows.values() if row.get("strict_match") is True]
    result = []
    for row in positives:
        source = str(row["source_file"])
        if source in paths:
            result.append((paths[source], row))
    return sorted(result, key=lambda item: item[0].name)


def build_reports(stage: str, candidates: list[tuple[Path, dict[str, Any] | None]], fingerprint: str) -> dict[str, Any]:
    output = RUN_DIR / f"output_{stage}"
    rows = list(load_rows(output / "decisions.jsonl", fingerprint).values())
    final_key = "strict_match" if stage == "stage1" else "confirmed_strict_match" if stage == "stage2" else "artifact_confirmed"
    matches = [row for row in rows if row.get(final_key) is True]
    usage = Counter()
    for row in rows:
        usage.update(row.get("usage") or {})
    summary = {
        "updated_at": utc_now(),
        "analysis_version": CONFIG["analysis_version"],
        "stage": stage,
        "model": CONFIG["model"]["name"],
        "max_concurrency": CONFIG["batch"]["max_concurrency"],
        "prompt_fingerprint": fingerprint,
        "eligible_inputs": len(candidates),
        "completed": len(rows),
        "pending": max(0, len(candidates) - len(rows)),
        "match_count": len(matches),
        "nonmatch_count": len(rows) - len(matches),
        "status_counts": dict(sorted(Counter(str(row.get("artifact_status") if stage == "stage3" else row.get("objective_status")) for row in rows).items())),
        "core_role_counts": {} if stage == "stage3" else dict(sorted(Counter(str(row.get("core_role")) for row in rows).items())),
        "match_year_counts": dict(sorted(Counter(str(row.get("year")) for row in matches).items())),
        "match_journal_counts": dict(sorted(Counter(str(row.get("journal")) for row in matches).items())),
        "usage": dict(usage),
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = [
        "record_id", "source_file", "title", "authors", "year", "journal", "doi",
        final_key, "objective_status", "artifact_status", "core_role", "confidence", "decision_reason_cn", "audit_reason_cn",
    ]
    with (output / "decisions.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: str(row.get("source_file"))))
    lines = [f"# {stage} matches", "", f"- Completed: {len(rows)}", f"- Matches: {len(matches)}", ""]
    for row in sorted(matches, key=lambda item: (str(item.get("year")), str(item.get("journal")), str(item.get("title")))):
        reason = row.get("audit_reason_cn") or row.get("decision_reason_cn") or ""
        status = row.get("artifact_status") if stage == "stage3" else row.get("objective_status")
        lines.extend([f"## {row.get('title')}", "", f"- Record: {row.get('record_id')}", f"- Year / journal: {row.get('year')} / {row.get('journal')}", f"- Status / role: {status} / {row.get('core_role') or ''}", f"- Reason: {reason}", ""])
    (output / "matches.md").write_text("\n".join(lines), encoding="utf-8")
    return summary


def run(stage: str, only_pattern: str | None, workers: int | None) -> int:
    system, user_template = prompt_files(stage)
    fingerprint = prompt_fingerprint(stage, system, user_template)
    candidates = stage_candidates(stage)
    output = RUN_DIR / f"output_{stage}"
    existing = load_rows(output / "decisions.jsonl", fingerprint)
    pending = [(path, prior) for path, prior in candidates if path.name not in existing]
    if only_pattern:
        regex = re.compile(only_pattern, re.IGNORECASE)
        pending = [(path, prior) for path, prior in pending if regex.search(path.name)]

    env_file = resolve(CONFIG["env_file"])
    load_dotenv(env_file)
    model = CONFIG["model"]
    api_key = os.getenv(str(model["api_key_env"]), "")
    base_url = os.getenv(str(model["base_url_env"]), "") or str(model["base_url"])
    if not api_key:
        raise RuntimeError(f"missing API key environment variable {model['api_key_env']}")
    clients = ThreadClients(api_key, base_url, float(model["timeout_seconds"]))
    max_workers = workers or int(CONFIG["batch"]["max_concurrency"])
    print(f"stage={stage} eligible={len(candidates)} existing={len(existing)} pending_selected={len(pending)} workers={max_workers}", flush=True)
    completed = 0
    failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {
            executor.submit(analyze_one, path, stage, prior, clients, system, user_template, fingerprint): path
            for path, prior in pending
        }
        for future in concurrent.futures.as_completed(future_map):
            path = future_map[future]
            try:
                row = future.result()
                append_jsonl(output / "decisions.jsonl", row)
                completed += 1
            except Exception as exc:
                append_jsonl(output / "errors.jsonl", {"source_file": path.name, "stage": stage, "error": str(exc), "failed_at": utc_now(), "prompt_fingerprint": fingerprint})
                failed += 1
            if (completed + failed) % int(CONFIG["batch"]["progress_interval"]) == 0:
                print(f"progress stage={stage} finished={completed + failed}/{len(pending)} succeeded={completed} failed={failed}", flush=True)
            if (completed + failed) % int(CONFIG["batch"]["report_interval"]) == 0:
                build_reports(stage, candidates, fingerprint)
    summary = build_reports(stage, candidates, fingerprint)
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("stage1", "stage2", "stage3"), required=True)
    parser.add_argument("--only-pattern")
    parser.add_argument("--workers", type=int)
    args = parser.parse_args()
    return run(args.stage, args.only_pattern, args.workers)


if __name__ == "__main__":
    raise SystemExit(main())
