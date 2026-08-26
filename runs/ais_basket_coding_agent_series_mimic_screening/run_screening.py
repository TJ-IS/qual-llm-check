#!/usr/bin/env python3
"""Screen objective-outcome papers for coding-agent research-series imitation value."""

from __future__ import annotations

import argparse
import concurrent.futures
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


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def load_prior_matches(path: Path) -> dict[str, dict[str, Any]]:
    matches: dict[str, dict[str, Any]] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                if row.get("objective_outcome_match") is True:
                    matches[str(row["source_file"])] = row
    return matches


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


def require_list(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{field} must be a list")
    return value


def validate_decision(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    mimic = require_bool(payload.get("mimic_candidate"), "mimic_candidate")
    conditions = payload.get("essential_conditions")
    if not isinstance(conditions, dict):
        raise ValueError("essential_conditions must be an object")
    flags = [
        require_bool(conditions.get("material_runnable_software_change"), "material_runnable_software_change"),
        require_bool(conditions.get("design_linked_objective_outcome"), "design_linked_objective_outcome"),
        require_bool(conditions.get("bounded_reproducible_method"), "bounded_reproducible_method"),
    ]
    if mimic != all(flags):
        raise ValueError("mimic_candidate must equal logical AND of essential conditions")
    source = payload.get("source_pattern")
    series = payload.get("series_value")
    if not isinstance(source, dict) or not isinstance(series, dict):
        raise ValueError("source_pattern and series_value must be objects")
    outcomes = require_list(source.get("objective_outcomes"), "source_pattern.objective_outcomes")
    for index, outcome in enumerate(outcomes):
        if not isinstance(outcome, dict) or not isinstance(outcome.get("evidence"), list):
            raise ValueError(f"invalid objective_outcomes[{index}]")
    chains = require_list(source.get("theory_to_design_chain"), "source_pattern.theory_to_design_chain")
    for index, chain in enumerate(chains):
        if not isinstance(chain, dict) or not isinstance(chain.get("evidence"), list):
            raise ValueError(f"invalid theory_to_design_chain[{index}]")
    require_list(series.get("repeatable_design_levers_cn"), "series_value.repeatable_design_levers_cn")
    priority = str(payload.get("mimic_priority") or "")
    if priority not in {"high", "medium", "low", "reject"}:
        raise ValueError("invalid mimic_priority")
    if (not mimic and priority != "reject") or (mimic and priority == "reject"):
        raise ValueError("mimic_priority inconsistent with mimic_candidate")
    confidence = float(payload.get("confidence"))
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


def analyze_one(path: Path, prior: dict[str, Any], clients: ThreadClients, config: dict[str, Any], system_prompt: str, user_template: str, fingerprint: str) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, fulltext = parse_frontmatter(raw)
    metadata = metadata_for(path, fulltext, frontmatter)
    prior_context = {
        "objective_outcome_match": prior.get("objective_outcome_match"),
        "inclusion_routes": prior.get("inclusion_routes"),
        "objective_outcomes": prior.get("objective_outcomes"),
        "artifact_outcome_link_cn": prior.get("artifact_outcome_link_cn"),
        "decision_reason_cn": prior.get("decision_reason_cn"),
    }
    user_prompt = user_template.format(**metadata, prior_objective_assessment=json.dumps(prior_context, ensure_ascii=False), fulltext=fulltext)
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
            decision = validate_decision(parse_json_object(response.choices[0].message.content or ""), metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                "analysis_version": config["analysis_version"],
                "prompt_fingerprint": fingerprint,
                "model": model["name"],
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
            time.sleep(float(batch["retry_base_delay_seconds"]) * (2 ** (attempt - 1)) + random.uniform(0, 0.5))
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
    if path.exists():
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    row = json.loads(line)
                    if row.get("prompt_fingerprint") == fingerprint:
                        decisions[str(row["source_file"])] = row
    return decisions


def write_reports(output_dir: Path, all_files: list[Path], decisions: dict[str, dict[str, Any]], config: dict[str, Any], fingerprint: str) -> None:
    rows = [decisions[name] for name in sorted(decisions)]
    priorities = Counter(str(row.get("mimic_priority")) for row in rows)
    condition_names = ("material_runnable_software_change", "design_linked_objective_outcome", "bounded_reproducible_method")
    summary = {
        "updated_at": utc_now(),
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "prompt_fingerprint": fingerprint,
        "input_candidates": len(all_files),
        "completed": len(rows),
        "pending": len(all_files) - len(rows),
        "mimic_candidate_count": sum(bool(row.get("mimic_candidate")) for row in rows),
        "priority_counts": dict(sorted(priorities.items())),
        "condition_true_counts": {name: sum(bool(row["essential_conditions"][name]) for row in rows) for name in condition_names},
        "usage": {key: sum(int((row.get("usage") or {}).get(key, 0)) for row in rows) for key in ("prompt_tokens", "completion_tokens", "total_tokens", "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")},
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    tmp = output_dir / "summary.json.tmp"
    tmp.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, output_dir / "summary.json")

    retained = [row for row in rows if row.get("mimic_candidate")]
    order = {"high": 0, "medium": 1, "low": 2}
    lines = ["# Coding-agent series mimic candidates", "", f"Completed: {len(rows)} / {len(all_files)}", f"Mimic candidates: {len(retained)}", ""]
    for row in sorted(retained, key=lambda item: (order.get(str(item.get("mimic_priority")), 9), -float(item.get("confidence") or 0), str(item.get("title") or ""))):
        source, series = row["source_pattern"], row["series_value"]
        lines.extend([
            f"## {row['title']}", "",
            f"- Priority: {row.get('mimic_priority')} / confidence {row.get('confidence')}",
            f"- Year/journal: {row.get('year')} / {row.get('journal')}",
            f"- Design delta: {source.get('design_delta_cn', '')}",
            f"- Comparison logic: {source.get('comparison_logic_cn', '')}",
            f"- Method template: {source.get('method_template_cn', '')}",
            f"- Outcome structure: {series.get('source_outcome_structure_cn', '')}",
            f"- Coding-agent analogue outcome: {series.get('coding_agent_analogue_outcome_cn', '')}",
            f"- Stage/dimension: {series.get('coding_agent_stage_or_dimension_cn', '')}",
            f"- What to copy: {series.get('what_to_copy_cn', '')}",
            f"- Decision: {row.get('decision_reason_cn', '')}", "",
        ])
    tmp_md = output_dir / "mimic_candidates.md.tmp"
    tmp_md.write_text("\n".join(lines), encoding="utf-8")
    os.replace(tmp_md, output_dir / "mimic_candidates.md")


def fingerprint(config: dict[str, Any], system_prompt: str, user_template: str) -> str:
    value = {"analysis_version": config["analysis_version"], "model": config["model"]["name"], "system_prompt": system_prompt, "user_template": user_template}
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--max-concurrency", type=int)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    prior = load_prior_matches(resolve_from_run(config["prior_objective_decisions_jsonl"]))
    input_dir = resolve_from_run(config["input_dir"])
    all_files = sorted(path for path in input_dir.glob("*.md") if path.name in prior)
    if len(all_files) != len(prior):
        missing = sorted(set(prior) - {path.name for path in all_files})
        raise RuntimeError(f"missing {len(missing)} full texts: {missing[:5]}")
    system_prompt = (RUN_DIR / config["prompt_files"]["system"]).read_text(encoding="utf-8").strip()
    user_template = (RUN_DIR / config["prompt_files"]["user_template"]).read_text(encoding="utf-8").strip()
    prompt_hash = fingerprint(config, system_prompt, user_template)
    output_dir = resolve_from_run(config["output_dir"])
    decisions_path = output_dir / "decisions.jsonl"
    decisions = load_current(decisions_path, prompt_hash)
    pending = [path for path in all_files if path.name not in decisions]
    if args.limit is not None:
        pending = pending[: args.limit]
    print(f"scope={len(all_files)} completed={len(decisions)} pending_this_run={len(pending)} model={config['model']['name']}", flush=True)
    print(f"prompt_fingerprint={prompt_hash}", flush=True)
    print(f"output_dir={output_dir}", flush=True)
    if args.dry_run:
        for path in pending[:10]:
            print(f"DRY_RUN file={path.name} bytes={path.stat().st_size}", flush=True)
        return 0
    if not pending:
        write_reports(output_dir, all_files, decisions, config, prompt_hash)
        return 0

    load_dotenv(resolve_from_run(config["env_file"]))
    api_key = os.getenv(config["model"]["api_key_env"])
    if not api_key:
        raise RuntimeError(f"missing API key env: {config['model']['api_key_env']}")
    base_url = os.getenv(config["model"]["base_url_env"]) or config["model"]["base_url"]
    clients = ThreadClients(api_key, base_url, float(config["model"]["timeout_seconds"]))
    concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    completed_now = failed_now = 0
    started = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(analyze_one, path, prior[path.name], clients, config, system_prompt, user_template, prompt_hash): path for path in pending}
        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                row = future.result()
                append_jsonl(decisions_path, row)
                decisions[path.name] = row
                completed_now += 1
                print(f"[{completed_now + failed_now}/{len(pending)}] OK priority={row['mimic_priority']} attempts={row['attempts']} file={path.name}", flush=True)
            except Exception as exc:
                failed_now += 1
                append_jsonl(output_dir / "errors.jsonl", {"source_file": path.name, "failed_at": utc_now(), "error_type": type(exc).__name__, "error": str(exc), "prompt_fingerprint": prompt_hash})
                print(f"[{completed_now + failed_now}/{len(pending)}] ERROR file={path.name} error={exc}", flush=True)
    write_reports(output_dir, all_files, decisions, config, prompt_hash)
    print(f"finished completed_now={completed_now} failed_now={failed_now} elapsed_seconds={time.monotonic() - started:.1f}", flush=True)
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
