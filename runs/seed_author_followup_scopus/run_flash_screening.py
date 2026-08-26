#!/usr/bin/env python3
"""Screen one author-follow-up bibliographic record per DeepSeek V4 Flash request."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import threading
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


ROOT = Path(__file__).resolve().parents[2]
RUN_DIR = Path(__file__).resolve().parent
INPUT = RUN_DIR / "analysis_v1" / "llm_inputs.jsonl"
SYSTEM_PROMPT = RUN_DIR / "system_prompt_author_trajectory.md"
OUTPUT = RUN_DIR / "analysis_v1" / "flash_screening_v1"
MODEL = "deepseek-v4-flash"

LABELS = {
    "direct_human_ai_programming",
    "direct_human_programming",
    "programming_artifact_or_method",
    "software_development_process_or_team",
    "information_systems_or_technology_adjacent",
    "unrelated_or_unclear",
}
CONTINUITY = {"direct", "adjacent", "topic_shift", "unclear"}
THEMES = {
    "programming_cognition_comprehension",
    "programming_performance_productivity",
    "query_database_programming",
    "spreadsheet_end_user_programming",
    "testing_debugging_quality",
    "pair_collaborative_programming",
    "software_representation_maintenance",
    "knowledge_based_system_development",
    "cognitive_fit_or_representation_outside_programming",
    "broader_software_development_process",
    "none",
    "unclear",
}
AI_CONTEXTS = {
    "ai_assisted_programming",
    "ai_for_software_artifacts",
    "ai_nonprogramming",
    "no_ai",
    "unclear",
}
METHODS = {
    "experiment",
    "survey",
    "qualitative",
    "archival_or_repository",
    "design_science_or_system_building",
    "analytical_or_modeling",
    "conceptual",
    "review",
    "mixed_methods",
    "other",
    "unclear",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return rows


def user_prompt(row: dict[str, Any]) -> str:
    return f"""Classify this single bibliographic record.

record_id: {row['record_key']}

title:
{row.get('title') or '[missing]'}

abstract:
{row.get('abstract') or '[missing]'}

author_keywords:
{row.get('author_keywords') or '[missing]'}

index_keywords:
{row.get('index_keywords') or '[missing]'}

Return exactly one JSON object."""


def extract_json(text: str) -> dict[str, Any]:
    value = text.strip()
    if value.startswith("```"):
        value = value.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(value)


def validate(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    expected = {
        "record_id",
        "trajectory_label",
        "continuity_strength",
        "direct_human_programming",
        "modern_ai_assisted_programming",
        "ai_context",
        "seed_theme_connections",
        "research_method",
        "decision_certainty",
        "evidence",
        "reason",
    }
    if set(payload) != expected:
        raise ValueError(f"Field mismatch: {set(payload) ^ expected}")
    if str(payload["record_id"]).strip() != record_id:
        raise ValueError("record_id mismatch")
    if payload["trajectory_label"] not in LABELS:
        raise ValueError("invalid trajectory_label")
    if payload["continuity_strength"] not in CONTINUITY:
        raise ValueError("invalid continuity_strength")
    for field in ("direct_human_programming", "modern_ai_assisted_programming"):
        if payload[field] is not None and not isinstance(payload[field], bool):
            raise ValueError(f"{field} must be boolean or null")
    if payload["ai_context"] not in AI_CONTEXTS:
        raise ValueError("invalid ai_context")
    themes = payload["seed_theme_connections"]
    if not isinstance(themes, list) or not themes or any(theme not in THEMES for theme in themes):
        raise ValueError("invalid seed_theme_connections")
    if payload["research_method"] not in METHODS:
        raise ValueError("invalid research_method")
    if payload["decision_certainty"] not in {"high", "medium", "low"}:
        raise ValueError("invalid decision_certainty")
    if not isinstance(payload["evidence"], list) or len(payload["evidence"]) > 2:
        raise ValueError("invalid evidence")
    if not str(payload["reason"]).strip():
        raise ValueError("reason required")
    return payload


class Clients:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.local = threading.local()

    def get(self) -> OpenAI:
        client = getattr(self.local, "client", None)
        if client is None:
            client = OpenAI(api_key=self.api_key, base_url=self.base_url, timeout=120)
            self.local.client = client
        return client


def screen(row: dict[str, Any], clients: Clients, system_prompt: str) -> dict[str, Any]:
    record_id = str(row["record_key"])
    total_usage: Counter[str] = Counter()
    last_error: Exception | None = None
    for attempt in range(1, 5):
        try:
            response = clients.get().chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt(row)},
                ],
                temperature=0,
                max_tokens=1000,
                response_format={"type": "json_object"},
            )
            usage = response.usage
            if usage:
                for key in (
                    "prompt_tokens",
                    "completion_tokens",
                    "total_tokens",
                    "prompt_cache_hit_tokens",
                    "prompt_cache_miss_tokens",
                ):
                    value = getattr(usage, key, None)
                    if isinstance(value, int):
                        total_usage[key] += value
            decision = validate(extract_json(response.choices[0].message.content or ""), record_id)
            return {
                "record_key": record_id,
                "eid": row.get("eid"),
                "doi": row.get("doi"),
                "title": row.get("title"),
                "year": row.get("year"),
                "source_title": row.get("source_title"),
                "eligible_target_author_ids": row.get("eligible_target_author_ids"),
                "eligible_target_author_names": row.get("eligible_target_author_names"),
                "eligible_target_author_tiers": row.get("eligible_target_author_tiers"),
                **decision,
                "model": MODEL,
                "attempts": attempt,
                "completed_at": now(),
                "usage": dict(total_usage),
            }
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f"{record_id}: {last_error}")


def write_summary(all_inputs: list[dict[str, Any]], errors: list[dict[str, str]]) -> dict[str, Any]:
    decisions = load_jsonl(OUTPUT / "decisions.jsonl")
    usage: Counter[str] = Counter()
    for decision in decisions:
        usage.update(decision.get("usage") or {})
    summary = {
        "updated_at": now(),
        "model": MODEL,
        "input_records": len(all_inputs),
        "completed": len(decisions),
        "remaining": len(all_inputs) - len(decisions),
        "failed_this_run": len(errors),
        "trajectory_label_counts": dict(Counter(d["trajectory_label"] for d in decisions)),
        "continuity_counts": dict(Counter(d["continuity_strength"] for d in decisions)),
        "modern_ai_assisted_programming_counts": dict(
            Counter(str(d["modern_ai_assisted_programming"]) for d in decisions)
        ),
        "usage": dict(usage),
        "errors_this_run": errors,
    }
    (OUTPUT / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=50)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    api_key = os.getenv("NEW_API_KEY")
    if not api_key:
        raise RuntimeError("NEW_API_KEY is missing")
    base_url = os.getenv("NEW_API_BASE_URL") or "https://api.deepseek.com"

    all_inputs = load_jsonl(INPUT)
    if len({row["record_key"] for row in all_inputs}) != len(all_inputs):
        raise ValueError("Duplicate record_key in input")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    decisions_path = OUTPUT / "decisions.jsonl"
    completed_ids = {row["record_key"] for row in load_jsonl(decisions_path)}
    pending = [row for row in all_inputs if row["record_key"] not in completed_ids]
    if args.limit is not None:
        pending = pending[: args.limit]

    system_prompt = SYSTEM_PROMPT.read_text(encoding="utf-8").strip()
    clients = Clients(api_key, base_url)
    errors: list[dict[str, str]] = []
    append_lock = threading.Lock()
    completed_this_run = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(screen, row, clients, system_prompt): row for row in pending}
        for future in concurrent.futures.as_completed(futures):
            row = futures[future]
            try:
                result = future.result()
                with append_lock:
                    with decisions_path.open("a", encoding="utf-8", newline="\n") as handle:
                        handle.write(json.dumps(result, ensure_ascii=False) + "\n")
                    completed_this_run += 1
                print(
                    f"completed_this_run={completed_this_run}/{len(pending)} "
                    f"record={row['record_key']} title={str(row.get('title') or '')[:70]}",
                    flush=True,
                )
            except Exception as exc:
                error = {"record_key": row["record_key"], "title": row.get("title", ""), "error": str(exc)}
                errors.append(error)
                print(
                    f"failed={len(errors)} record={row['record_key']} error={exc}", flush=True
                )

    if errors:
        with (OUTPUT / "errors.jsonl").open("a", encoding="utf-8", newline="\n") as handle:
            for error in errors:
                handle.write(json.dumps(error, ensure_ascii=False) + "\n")
    summary = write_summary(all_inputs, errors)
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
