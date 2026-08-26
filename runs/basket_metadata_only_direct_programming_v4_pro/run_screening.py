#!/usr/bin/env python3
"""Screen Basket metadata-only programming-query hits with DeepSeek V4 Pro."""

from __future__ import annotations

import concurrent.futures
import csv
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
METADATA = ROOT / "database" / "ALL_AIS_Basket_11.csv"
CANDIDATES = (
    ROOT
    / "runs"
    / "literature_review_search_sources_analysis"
    / "basket_programming_query_candidates.csv"
)
SYSTEM_PROMPT = RUN_DIR / "system_prompt.md"
OUTPUT = RUN_DIR / "output_v1"
MODEL = "deepseek-v4-pro"
MAX_WORKERS = 12

LABELS = {
    "direct_human_ai_programming",
    "direct_human_programming",
    "direct_programming_artifact_or_method",
    "software_development_context_only",
    "not_programming",
    "uncertain",
}
ACTIONS = {
    "write",
    "understand",
    "modify",
    "debug",
    "test",
    "inspect",
    "verify",
    "query",
    "develop_executable_application",
    "other",
    "none",
    "unclear",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def norm(value: str | None) -> str:
    return " ".join((value or "").casefold().split())


def load_rows() -> list[dict[str, str]]:
    with METADATA.open("r", encoding="utf-8-sig", newline="") as handle:
        metadata = list(csv.DictReader(handle))
    by_eid = {norm(row.get("EID")): row for row in metadata if row.get("EID")}
    by_doi = {norm(row.get("DOI")): row for row in metadata if row.get("DOI")}
    by_title = {norm(row.get("Title")): row for row in metadata if row.get("Title")}

    selected: list[dict[str, str]] = []
    with CANDIDATES.open("r", encoding="utf-8-sig", newline="") as handle:
        for candidate in csv.DictReader(handle):
            if candidate.get("evidence_stage") != "no_fulltext_screen_record":
                continue
            row = (
                by_eid.get(norm(candidate.get("eid")))
                or by_doi.get(norm(candidate.get("doi")))
                or by_title.get(norm(candidate.get("title")))
            )
            if row is None:
                raise ValueError(f"Metadata record not found: {candidate.get('title')}")
            selected.append(row)
    if len(selected) != 31:
        raise ValueError(f"Expected 31 records, found {len(selected)}")
    return selected


def user_prompt(row: dict[str, str]) -> str:
    record_id = row.get("EID") or row.get("DOI") or row.get("Title")
    return f"""Screen this single bibliographic record.

record_id: {record_id}

title:
{row.get('Title') or '[missing]'}

abstract:
{row.get('Abstract') or '[missing]'}

author_keywords:
{row.get('Author Keywords') or '[missing]'}

index_keywords:
{row.get('Index Keywords') or '[missing]'}

Return exactly one JSON object."""


def extract_json(text: str) -> dict[str, Any]:
    value = text.strip()
    if value.startswith("```"):
        value = value.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(value)


def validate(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    expected = {
        "record_id",
        "screening_label",
        "has_human_programming_task",
        "is_irreplaceable_direct_programming_research",
        "involves_ai_programming_system",
        "programming_actions",
        "fulltext_priority",
        "decision_certainty",
        "evidence",
        "reason",
    }
    if set(payload) != expected:
        raise ValueError(f"Field mismatch: {set(payload) ^ expected}")
    if str(payload["record_id"]).strip() != record_id:
        raise ValueError("record_id mismatch")
    if payload["screening_label"] not in LABELS:
        raise ValueError("invalid screening_label")
    for field in (
        "has_human_programming_task",
        "is_irreplaceable_direct_programming_research",
        "involves_ai_programming_system",
    ):
        if payload[field] is not None and not isinstance(payload[field], bool):
            raise ValueError(f"{field} must be boolean or null")
    actions = payload["programming_actions"]
    if not isinstance(actions, list) or not actions or any(x not in ACTIONS for x in actions):
        raise ValueError("invalid programming_actions")
    if payload["fulltext_priority"] not in {"high", "medium", "low", "exclude"}:
        raise ValueError("invalid fulltext_priority")
    if payload["decision_certainty"] not in {"high", "medium", "low"}:
        raise ValueError("invalid decision_certainty")
    if not isinstance(payload["evidence"], list) or len(payload["evidence"]) > 3:
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
            client = OpenAI(api_key=self.api_key, base_url=self.base_url, timeout=180)
            self.local.client = client
        return client


def screen(
    row: dict[str, str], clients: Clients, system_prompt: str
) -> dict[str, Any]:
    record_id = row.get("EID") or row.get("DOI") or row.get("Title")
    last_error: Exception | None = None
    total_usage: Counter[str] = Counter()
    for attempt in range(1, 5):
        try:
            response = clients.get().chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt(row)},
                ],
                temperature=0,
                max_tokens=1600,
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
            decision = validate(
                extract_json(response.choices[0].message.content or ""), record_id
            )
            return {
                "title": row.get("Title"),
                "year": row.get("Year"),
                "source_title": row.get("Source title"),
                "doi": row.get("DOI"),
                "eid": row.get("EID"),
                **decision,
                "model": MODEL,
                "attempts": attempt,
                "completed_at": now(),
                "usage": dict(total_usage),
            }
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f"{record_id}: {last_error}")


def main() -> int:
    load_dotenv(ROOT / ".env")
    api_key = os.getenv("NEW_API_KEY")
    if not api_key:
        raise RuntimeError("NEW_API_KEY is missing")
    base_url = os.getenv("NEW_API_BASE_URL") or "https://api.deepseek.com"
    rows = load_rows()
    system_prompt = SYSTEM_PROMPT.read_text(encoding="utf-8").strip()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    clients = Clients(api_key, base_url)
    results: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(screen, row, clients, system_prompt): row for row in rows}
        for future in concurrent.futures.as_completed(futures):
            row = futures[future]
            try:
                results.append(future.result())
                print(
                    f"completed={len(results) + len(errors)}/{len(rows)} "
                    f"title={row.get('Title', '')[:80]}",
                    flush=True,
                )
            except Exception as exc:
                errors.append({"title": row.get("Title", ""), "error": str(exc)})
                print(
                    f"failed={len(results) + len(errors)}/{len(rows)} "
                    f"title={row.get('Title', '')[:80]} error={exc}",
                    flush=True,
                )
    results.sort(key=lambda x: (int(x.get("year") or 0), x.get("title") or ""))
    with (OUTPUT / "decisions.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for result in results:
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")
    usage: Counter[str] = Counter()
    for result in results:
        usage.update(result.get("usage") or {})
    summary = {
        "completed_at": now(),
        "model": MODEL,
        "input_records": len(rows),
        "completed": len(results),
        "failed": len(errors),
        "screening_label_counts": dict(
            Counter(result["screening_label"] for result in results)
        ),
        "irreplaceable_direct_counts": dict(
            Counter(str(result["is_irreplaceable_direct_programming_research"]) for result in results)
        ),
        "usage": dict(usage),
        "errors": errors,
    }
    (OUTPUT / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
