#!/usr/bin/env python3
"""Red-team re-audit Stage 1 strict inclusions only."""

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

import run_unified_screening as base


RUN_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = RUN_DIR / "output_stage2"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_stage1() -> dict[str, dict[str, Any]]:
    path = RUN_DIR / "output_stage1" / "decisions.jsonl"
    rows: dict[str, dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            rows[str(row["source_file"])] = row
    if len(rows) != 2475:
        raise RuntimeError(f"Stage 1 must have 2475 unique decisions, got {len(rows)}")
    return {source: row for source, row in rows.items() if row.get("strict_include") is True}


def load_existing(path: Path, fingerprint: str) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("prompt_fingerprint") == fingerprint:
            rows[str(row["source_file"])] = row
    return rows


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


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def call_one(
    source: str,
    stage1: dict[str, Any],
    clients: ThreadClients,
    config: dict[str, Any],
    system: str,
    template: str,
    fingerprint: str,
) -> dict[str, Any]:
    fulltext_path = base.resolve_from_run(str(config["input_dir"])) / source
    raw = fulltext_path.read_text(encoding="utf-8", errors="replace")
    front, fulltext = base.parse_frontmatter(raw)
    metadata = base.metadata_for(fulltext_path, fulltext, front)
    user = template.format(
        **metadata,
        stage1_decision=json.dumps(stage1, ensure_ascii=False, indent=2),
        fulltext=fulltext,
    )
    model = config["model"]
    retries = int(config["batch"]["retries"])
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
            decision = base.validate_decision(base.parse_json_object(content), metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                "analysis_version": config["analysis_version"] + "-red-team-v1",
                "stage": "red_team",
                "prompt_fingerprint": fingerprint,
                "model": model["name"],
                "analysis_mode": "one_complete_local_fulltext_per_request",
                "attempts": attempt,
                "completed_at": utc_now(),
                **decision,
                "usage": base.usage_dict(response),
            }
        except Exception as exc:
            last_error = exc
            if attempt > retries:
                break
            delay = float(config["batch"]["retry_base_delay_seconds"]) * (2 ** (attempt - 1))
            time.sleep(delay + random.uniform(0, 0.5))
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}") from last_error


def write_outputs(stage1: dict[str, dict[str, Any]], red: dict[str, dict[str, Any]], fingerprint: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for source in sorted(stage1):
        if source not in red:
            continue
        first, second = stage1[source], red[source]
        rows.append({
            "record_id": first["record_id"],
            "source_file": source,
            "title": first["title"],
            "authors": first["authors"],
            "year": first["year"],
            "journal": first["journal"],
            "doi": first["doi"],
            "stage1_include": True,
            "red_team_include": bool(second["strict_include"]),
            "final_include": bool(second["strict_include"]),
            "metric_status": (second.get("objective_metric") or {}).get("metric_status", ""),
            "core_goal_status": (second.get("objective_metric") or {}).get("core_goal_status", ""),
            "artifact_status": (second.get("software_artifact") or {}).get("artifact_status", ""),
            "contribution_target_status": (second.get("class_level_contribution") or {}).get("contribution_target_status", ""),
            "generalization_status": (second.get("class_level_contribution") or {}).get("generalization_status", ""),
            "artifact_role_status": (second.get("class_level_contribution") or {}).get("artifact_role_status", ""),
            "exclusion_trigger_codes": " | ".join(str(x) for x in second.get("exclusion_trigger_codes") or []),
            "decision_reason_cn": second.get("decision_reason_cn", ""),
            "confidence": second.get("confidence", ""),
        })
    fields = list(rows[0].keys()) if rows else []
    for name, selected in (
        ("red_team_all_candidates.csv", rows),
        ("final_verified_included.csv", [row for row in rows if row["final_include"]]),
        ("red_team_excluded.csv", [row for row in rows if not row["final_include"]]),
    ):
        with (OUTPUT_DIR / name).open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(selected)
    with (OUTPUT_DIR / "full_two_stage_audit_trail.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for source in sorted(red):
            handle.write(json.dumps({
                "source_file": source,
                "record_id": stage1[source]["record_id"],
                "title": stage1[source]["title"],
                "stage1": stage1[source],
                "red_team": red[source],
                "final_include": bool(red[source]["strict_include"]),
            }, ensure_ascii=False) + "\n")
    included = [row for row in rows if row["final_include"]]
    usage_keys = ("prompt_tokens", "completion_tokens", "total_tokens", "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")
    summary = {
        "generated_at": utc_now(),
        "prompt_fingerprint": fingerprint,
        "stage1_candidate_count": len(stage1),
        "red_team_completed": len(red),
        "red_team_pending": len(stage1) - len(red),
        "final_include_count": len(included),
        "final_exclude_count": len(rows) - len(included),
        "final_include_year_counts": dict(sorted(Counter(str(row["year"]) for row in included).items())),
        "final_include_journal_counts": dict(sorted(Counter(str(row["journal"]) for row in included).items())),
        "usage": {key: sum(int((row.get("usage") or {}).get(key, 0)) for row in red.values()) for key in usage_keys},
    }
    (OUTPUT_DIR / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = ["# 统一严格筛选：红队复核结果", "", f"- Stage 1候选：{len(stage1)}", f"- 红队完成：{len(red)}", f"- 最终纳入：{len(included)}", "", "## 最终纳入", ""]
    for row in included:
        report.extend([f"### {row['title']}", "", f"- 年份/期刊：{row['year']} / {row['journal']}", f"- 判定：{row['decision_reason_cn']}", ""])
    (OUTPUT_DIR / "final_report_cn.md").write_text("\n".join(report), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-concurrency", type=int)
    args = parser.parse_args()
    config = base.load_config()
    stage1 = load_stage1()
    system = (RUN_DIR / "system_prompt_cn.md").read_text(encoding="utf-8") + (RUN_DIR / "red_team_addendum_cn.md").read_text(encoding="utf-8")
    template = (RUN_DIR / "red_team_user_template_cn.md").read_text(encoding="utf-8")
    fingerprint = hashlib.sha256(json.dumps({"stage": "red_team", "version": config["analysis_version"], "model": config["model"]["name"], "system": system, "template": template}, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    decisions_path = OUTPUT_DIR / "decisions.jsonl"
    errors_path = OUTPUT_DIR / "errors.jsonl"
    existing = load_existing(decisions_path, fingerprint)
    pending = [source for source in sorted(stage1) if source not in existing]
    print(f"stage1_candidates={len(stage1)} existing={len(existing)} pending={len(pending)}", flush=True)
    if not pending:
        write_outputs(stage1, existing, fingerprint)
        return 0
    load_dotenv(base.resolve_from_run(str(config["env_file"])))
    api_key = os.getenv(str(config["model"]["api_key_env"]))
    if not api_key:
        raise RuntimeError("missing API key")
    base_url = os.getenv(str(config["model"]["base_url_env"])) or str(config["model"]["base_url"])
    clients = ThreadClients(api_key, base_url, float(config["model"]["timeout_seconds"]))
    workers = args.max_concurrency or min(100, len(pending))
    completed = failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(call_one, source, stage1[source], clients, config, system, template, fingerprint): source for source in pending}
        for future in concurrent.futures.as_completed(futures):
            source = futures[future]
            try:
                row = future.result()
                append_jsonl(decisions_path, row)
                existing[source] = row
                completed += 1
            except Exception as exc:
                append_jsonl(errors_path, {"source_file": source, "failed_at": utc_now(), "error": str(exc), "prompt_fingerprint": fingerprint})
                failed += 1
                print(f"ERROR {source}: {exc}", flush=True)
    write_outputs(stage1, existing, fingerprint)
    print(f"completed={completed} failed={failed}", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
