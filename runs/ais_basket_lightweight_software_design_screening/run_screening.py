#!/usr/bin/env python3
"""Screen recent AIS Basket full texts for feasible individual software-design examples."""

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
            value = json.loads(raw_value)
        except json.JSONDecodeError:
            value = raw_value
        metadata[key.strip()] = value
    return metadata, normalized[end + 5 :].lstrip()


def metadata_for(path: Path, fulltext: str, frontmatter: dict[str, Any]) -> dict[str, str]:
    parts = path.name.split("_", 2)
    filename_id = parts[0].lstrip("0") or "0"
    filename_year = parts[1] if len(parts) >= 3 else ""
    return {
        "record_id": str(frontmatter.get("otero_id") or filename_id),
        "source_file": path.name,
        "title": str(frontmatter.get("title") or path.stem),
        "authors": str(frontmatter.get("authors") or ""),
        "year": str(frontmatter.get("year") or filename_year),
        "journal": str(frontmatter.get("journal") or ""),
        "doi": str(frontmatter.get("doi") or ""),
        "fulltext_chars": str(len(fulltext)),
    }


def select_files(input_dir: Path, year_from: int, year_to: int) -> list[Path]:
    pattern = re.compile(r"^\d+_(\d{4})_")
    selected: list[Path] = []
    for path in sorted(input_dir.glob("*.md")):
        match = pattern.match(path.name)
        if match and year_from <= int(match.group(1)) <= year_to:
            selected.append(path)
    return selected


def parse_json_object(content: str) -> dict[str, Any]:
    if not content or not content.strip():
        raise ValueError("empty model response")
    text = content.strip()
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


def require_enum(value: Any, allowed: set[str], field: str) -> str:
    normalized = str(value or "").strip()
    if normalized not in allowed:
        raise ValueError(f"invalid {field}: {normalized!r}")
    return normalized


def require_bool(value: Any, field: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{field} must be boolean")
    return value


def require_list(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{field} must be a list")
    return value


def validate_decision(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    returned_id = str(payload.get("record_id") or "").strip()
    if returned_id != record_id:
        raise ValueError(f"record_id mismatch: expected {record_id!r}, got {returned_id!r}")

    target_match = require_bool(payload.get("target_match"), "target_match")
    eligibility = payload.get("eligibility")
    if not isinstance(eligibility, dict):
        raise ValueError("eligibility must be an object")
    eligibility_fields = (
        "individual_level",
        "runnable_individual_software_artifact",
        "feasible_for_small_research_team",
    )
    flags = []
    for field in eligibility_fields:
        value = require_bool(eligibility.get(field), f"eligibility.{field}")
        eligibility[field] = value
        flags.append(value)
    if target_match != all(flags):
        raise ValueError("target_match must equal the logical AND of eligibility fields")

    for object_name in ("source_artifact", "design_approach", "feasibility"):
        if not isinstance(payload.get(object_name), dict):
            raise ValueError(f"{object_name} must be an object")
    artifact = payload["source_artifact"]
    design = payload["design_approach"]
    feasibility = payload["feasibility"]
    require_list(artifact.get("artifact_evidence"), "source_artifact.artifact_evidence")
    require_list(design.get("design_knowledge"), "design_approach.design_knowledge")
    require_list(design.get("design_evidence"), "design_approach.design_evidence")
    require_list(feasibility.get("essential_external_dependencies_cn"), "feasibility.essential_external_dependencies_cn")
    require_list(feasibility.get("feasibility_evidence"), "feasibility.feasibility_evidence")
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
    result: dict[str, int] = {}
    for key in (
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "prompt_cache_hit_tokens",
        "prompt_cache_miss_tokens",
    ):
        value = getattr(usage, key, None)
        if isinstance(value, int):
            result[key] = value
    return result


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
    text = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, fulltext = parse_frontmatter(text)
    metadata = metadata_for(path, fulltext, frontmatter)
    user_prompt = user_template.format(**metadata, fulltext=fulltext)
    model = config["model"]
    batch = config["batch"]
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
                    "empty model response "
                    f"finish_reason={choice.finish_reason!r} reasoning_chars={len(reasoning)}"
                )
            decision = validate_decision(parse_json_object(content), metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                "analysis_version": str(config["analysis_version"]),
                "prompt_fingerprint": fingerprint,
                "model": str(model["name"]),
                "analysis_mode": "one_fulltext_one_request",
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


def load_current_decisions(path: Path, fingerprint: str) -> dict[str, dict[str, Any]]:
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


def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    config: dict[str, Any],
    fingerprint: str,
) -> None:
    rows = [decisions[name] for name in sorted(decisions)]
    eligibility_counts = {
        field: sum(bool((row.get("eligibility") or {}).get(field)) for row in rows)
        for field in (
            "individual_level",
            "runnable_individual_software_artifact",
            "feasible_for_small_research_team",
        )
    }
    summary = {
        "updated_at": utc_now(),
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "prompt_fingerprint": fingerprint,
        "input_fulltexts": len(all_files),
        "completed": len(rows),
        "pending": len(all_files) - len(rows),
        "target_match_count": sum(bool(row.get("target_match")) for row in rows),
        "target_nonmatch_count": sum(not bool(row.get("target_match")) for row in rows),
        "eligibility_true_counts": eligibility_counts,
        "usage": {
            key: sum(int((row.get("usage") or {}).get(key, 0)) for row in rows)
            for key in (
                "prompt_tokens",
                "completion_tokens",
                "total_tokens",
                "prompt_cache_hit_tokens",
                "prompt_cache_miss_tokens",
            )
        },
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    temp_summary = output_dir / "summary.json.tmp"
    temp_summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp_summary, output_dir / "summary.json")

    fields = [
        "record_id",
        "source_file",
        "title",
        "authors",
        "year",
        "journal",
        "doi",
        "target_match",
        "individual_level",
        "runnable_individual_software_artifact",
        "feasible_for_small_research_team",
        "artifact_name",
        "starting_point_cn",
        "material_design_delta_cn",
        "design_process_cn",
        "potential_coding_agent_design_method_value_cn",
        "decision_reason_cn",
        "confidence",
        "fulltext_chars",
        "attempts",
    ]
    temp_csv = output_dir / "decisions.csv.tmp"
    with temp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "record_id": row.get("record_id"),
                    "source_file": row.get("source_file"),
                    "title": row.get("title"),
                    "authors": row.get("authors"),
                    "year": row.get("year"),
                    "journal": row.get("journal"),
                    "doi": row.get("doi"),
                    "target_match": row.get("target_match"),
                    "individual_level": (row.get("eligibility") or {}).get("individual_level"),
                    "runnable_individual_software_artifact": (row.get("eligibility") or {}).get("runnable_individual_software_artifact"),
                    "feasible_for_small_research_team": (row.get("eligibility") or {}).get("feasible_for_small_research_team"),
                    "artifact_name": (row.get("source_artifact") or {}).get("artifact_name"),
                    "starting_point_cn": (row.get("source_artifact") or {}).get("starting_point_cn"),
                    "material_design_delta_cn": (row.get("source_artifact") or {}).get("material_design_delta_cn"),
                    "design_process_cn": (row.get("design_approach") or {}).get("design_process_cn"),
                    "potential_coding_agent_design_method_value_cn": row.get("potential_coding_agent_design_method_value_cn"),
                    "decision_reason_cn": row.get("decision_reason_cn"),
                    "confidence": row.get("confidence"),
                    "fulltext_chars": row.get("fulltext_chars"),
                    "attempts": row.get("attempts"),
                }
            )
    os.replace(temp_csv, output_dir / "decisions.csv")

    retained = [row for row in rows if row.get("target_match") is True]
    markdown = [
        "# Individual software design examples",
        "",
        f"Completed: {len(rows)} / {len(all_files)}",
        f"Retained: {len(retained)}",
        "",
    ]
    for row in sorted(retained, key=lambda item: (-float(item.get("confidence") or 0), str(item.get("title") or ""))):
        artifact = row.get("source_artifact") or {}
        design = row.get("design_approach") or {}
        markdown.extend(
            [
                f"## {row['title']}",
                "",
                f"- Year/journal: {row.get('year')} / {row.get('journal')}",
                f"- DOI: {row.get('doi')}",
                f"- Artifact: {artifact.get('artifact_name', '')}",
                f"- Individual user/task: {artifact.get('individual_user_and_task_cn', '')}",
                f"- Design delta: {artifact.get('material_design_delta_cn', '')}",
                f"- Design process: {design.get('design_process_cn', '')}",
                f"- Potential coding-agent design value: {row.get('potential_coding_agent_design_method_value_cn', '')}",
                f"- Decision: {row.get('decision_reason_cn', '')}",
                f"- Confidence: {row.get('confidence')}",
                "",
            ]
        )
    temp_md = output_dir / "strong_and_promising_candidates.md.tmp"
    temp_md.write_text("\n".join(markdown), encoding="utf-8")
    os.replace(temp_md, output_dir / "strong_and_promising_candidates.md")


def prompt_fingerprint(config: dict[str, Any], system_prompt: str, user_template: str) -> str:
    value = {
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "system_prompt": system_prompt,
        "user_template": user_template,
    }
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


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
    if args.max_concurrency is not None and not 1 <= args.max_concurrency <= 200:
        parser.error("--max-concurrency must be between 1 and 200")
    return args


def main() -> int:
    args = parse_args()
    config = load_config()
    input_dir = resolve_from_run(str(config["input_dir"]))
    output_dir = resolve_from_run(str(config["output_dir"]))
    env_file = resolve_from_run(str(config["env_file"]))
    selection = config["selection"]
    all_files = select_files(input_dir, int(selection["year_from"]), int(selection["year_to"]))
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(encoding="utf-8").strip()
    fingerprint = prompt_fingerprint(config, system_prompt, user_template)
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    decisions = load_current_decisions(decisions_path, fingerprint)
    selected = all_files[args.offset :]
    pending = [path for path in selected if path.name not in decisions]
    if args.limit is not None:
        pending = pending[: args.limit]
    print(
        f"scope={len(all_files)} completed={len(decisions)} pending_this_run={len(pending)} "
        f"years={selection['year_from']}-{selection['year_to']} model={config['model']['name']}",
        flush=True,
    )
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
    concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    completed_now = 0
    failed_now = 0
    started = time.monotonic()

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {
            pool.submit(
                analyze_one, path, clients, config, system_prompt, user_template, fingerprint
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
                print(
                    f"[{completed_now + failed_now}/{len(pending)}] OK "
                    f"target_match={row['target_match']} attempts={row['attempts']} "
                    f"file={path.name}",
                    flush=True,
                )
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
                print(
                    f"[{completed_now + failed_now}/{len(pending)}] ERROR file={path.name} error={exc}",
                    flush=True,
                )
            if (completed_now + failed_now) % 25 == 0:
                write_reports(output_dir, all_files, decisions, config, fingerprint)

    write_reports(output_dir, all_files, decisions, config, fingerprint)
    elapsed = time.monotonic() - started
    print(
        f"finished completed_now={completed_now} failed_now={failed_now} "
        f"elapsed_seconds={elapsed:.1f}",
        flush=True,
    )
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
