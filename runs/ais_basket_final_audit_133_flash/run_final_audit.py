#!/usr/bin/env python3
"""Two independent full-text audits plus adjudication of disagreements."""

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
    "objective_construct_independent_of_human_perception",
    "objective_value_deterministically_observable",
    "all_core_success_outcomes_objective",
    "objective_improvement_is_article_core_goal",
    "explicit_software_artifact_class",
    "designed_or_materially_modified_artifact_or_component",
    "component_operationally_instantiated_or_run",
)
ALLOWED_METRICS = {"fully_objective_direct", "objective_fixed_factual_labels"}
ALL_METRICS = ALLOWED_METRICS | {
    "subjective_construct_with_fixed_labels", "human_semantic_judgment",
    "mixed_objective_subjective", "subjective_or_self_report",
    "no_qualifying_metric", "unclear",
}
ALLOWED_CORE = {"objective_improvement_primary"}
ALL_CORE = ALLOWED_CORE | {"objective_metric_secondary", "theory_or_explanation_primary", "unclear"}
ALLOWED_ARTIFACTS = {"implemented_software_artifact", "implemented_artifact_component"}
ALL_ARTIFACTS = ALLOWED_ARTIFACTS | {
    "algorithm_or_model_only", "analytical_or_simulation_method_only",
    "platform_only_context", "concept_or_future_design_only", "unclear",
}
ADJ_GATE_KEYS = (
    "objective_metric", "objective_improvement_core_goal",
    "implemented_or_instantiated_software_artifact",
)


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
    return metadata, text[end + 5:].lstrip()


def load_inputs() -> list[dict[str, Any]]:
    csv_path = resolve(CONFIG["input_csv"])
    fulltext_dir = resolve(CONFIG["fulltext_dir"])
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 133:
        raise RuntimeError(f"Expected 133 input records, found {len(rows)}")
    output = []
    seen = set()
    for row in rows:
        source = str(row.get("source_file") or "")
        if not source or source in seen:
            raise RuntimeError(f"Missing or duplicate source_file: {source!r}")
        seen.add(source)
        path = fulltext_dir / source
        if not path.exists():
            raise FileNotFoundError(path)
        raw = path.read_text(encoding="utf-8", errors="replace")
        front, fulltext = parse_frontmatter(raw)
        output.append({
            "record_id": str(row.get("record_id") or front.get("otero_id") or ""),
            "source_file": source,
            "title": str(row.get("title") or front.get("title") or path.stem),
            "authors": str(row.get("authors") or front.get("authors") or ""),
            "year": str(row.get("year") or front.get("year") or ""),
            "journal": str(row.get("journal") or front.get("journal") or ""),
            "doi": str(row.get("doi") or front.get("doi") or ""),
            "fulltext": fulltext,
            "fulltext_chars": len(fulltext),
        })
    return sorted(output, key=lambda row: row["source_file"])


def parse_json_object(content: str) -> dict[str, Any]:
    text = (content or "").strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end <= start:
        raise ValueError("response has no JSON object")
    candidate = text[start:end + 1]
    try:
        payload = json.loads(candidate)
    except json.JSONDecodeError:
        payload = json.loads(re.sub(r",\s*([}\]])", r"\1", candidate))
    if not isinstance(payload, dict):
        raise ValueError("response is not a JSON object")
    return payload


def validate_audit(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    gates = payload.get("gates")
    if not isinstance(gates, dict):
        raise ValueError("gates must be an object")
    values = []
    for key in GATE_KEYS:
        if not isinstance(gates.get(key), bool):
            raise ValueError(f"gates.{key} must be boolean")
        values.append(gates[key])
    metric = str(payload.get("metric_status") or "")
    core = str(payload.get("core_goal_status") or "")
    artifact = str(payload.get("artifact_status") or "")
    if metric not in ALL_METRICS or core not in ALL_CORE or artifact not in ALL_ARTIFACTS:
        raise ValueError("invalid status value")
    expected = all(values) and metric in ALLOWED_METRICS and core in ALLOWED_CORE and artifact in ALLOWED_ARTIFACTS
    if payload.get("strict_include") is not expected:
        raise ValueError("strict_include is logically inconsistent")
    payload["confidence"] = float(payload.get("confidence"))
    if not 0 <= payload["confidence"] <= 1:
        raise ValueError("confidence outside [0,1]")
    return payload


def validate_adjudication(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    gates = payload.get("resolved_gates")
    if not isinstance(gates, dict):
        raise ValueError("resolved_gates must be an object")
    values = []
    for key in ADJ_GATE_KEYS:
        if not isinstance(gates.get(key), bool):
            raise ValueError(f"resolved_gates.{key} must be boolean")
        values.append(gates[key])
    metric = str(payload.get("metric_status") or "")
    core = str(payload.get("core_goal_status") or "")
    artifact = str(payload.get("artifact_status") or "")
    if metric not in ALL_METRICS or core not in ALL_CORE or artifact not in ALL_ARTIFACTS:
        raise ValueError("invalid adjudication status value")
    expected = all(values) and metric in ALLOWED_METRICS and core in ALLOWED_CORE and artifact in ALLOWED_ARTIFACTS
    if payload.get("adjudicated_include") is not expected:
        raise ValueError("adjudicated_include is logically inconsistent")
    payload["confidence"] = float(payload.get("confidence"))
    if not 0 <= payload["confidence"] <= 1:
        raise ValueError("confidence outside [0,1]")
    return payload


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


def prompt_fingerprint(stage: str, system: str, user: str) -> str:
    basis = {"analysis_version": CONFIG["analysis_version"], "stage": stage,
             "model": CONFIG["model"]["name"], "system": system, "user": user}
    return hashlib.sha256(json.dumps(basis, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def fill(template: str, values: dict[str, Any]) -> str:
    result = template
    for key, value in values.items():
        result = result.replace("{" + key + "}", str(value))
    return result


def usage_dict(response: Any) -> dict[str, int]:
    usage = response.usage
    if usage is None:
        return {}
    keys = ("prompt_tokens", "completion_tokens", "total_tokens",
            "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")
    return {key: int(getattr(usage, key)) for key in keys
            if isinstance(getattr(usage, key, None), int)}


def call_model(item: dict[str, Any], stage: str, clients: ThreadClients,
               system: str, user: str, fingerprint: str) -> dict[str, Any]:
    model = CONFIG["model"]
    retries = int(CONFIG["batch"]["retries"])
    last_error: Exception | None = None
    for attempt in range(1, retries + 2):
        try:
            response = clients.get().chat.completions.create(
                model=str(model["name"]),
                messages=[{"role": "system", "content": system},
                          {"role": "user", "content": user}],
                temperature=float(model["temperature"]),
                max_tokens=int(model["max_tokens"]),
                response_format={"type": "json_object"},
            )
            message = response.choices[0].message
            content = message.content or getattr(message, "reasoning_content", None) or ""
            payload = parse_json_object(content)
            decision = validate_adjudication(payload, item["record_id"]) if stage == "adjudication" else validate_audit(payload, item["record_id"])
            return {
                **{k: v for k, v in item.items() if k != "fulltext"},
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
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}") from last_error


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def load_jsonl(path: Path, fingerprint: str | None = None) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if fingerprint and row.get("prompt_fingerprint") != fingerprint:
            continue
        rows[str(row["source_file"])] = row
    return rows


def api_clients() -> ThreadClients:
    load_dotenv(resolve(CONFIG["env_file"]))
    model = CONFIG["model"]
    api_key = os.getenv(str(model["api_key_env"]), "")
    base_url = os.getenv(str(model["base_url_env"]), "") or str(model["base_url"])
    if not api_key:
        raise RuntimeError(f"missing API key: {model['api_key_env']}")
    return ThreadClients(api_key, base_url, float(model["timeout_seconds"]))


def run_independent(stage: str, pattern: str | None, workers: int | None) -> int:
    items = load_inputs()
    system = (RUN_DIR / "audit_system_prompt_cn.md").read_text(encoding="utf-8")
    template = (RUN_DIR / "audit_user_template_cn.md").read_text(encoding="utf-8")
    round_instruction = (
        "独立资格审计 A：从正反两面逐项核验七道门槛。"
        if stage == "audit_a" else
        "独立红队审计 B：主动寻找能推翻纳入资格的反证，尤其防止主观标签伪装成客观指标、算法伪装成软件制品、次要客观评价伪装成核心贡献；但不要为了排除而忽略明确正证据。"
    )
    fingerprint = prompt_fingerprint(stage, system, template + round_instruction)
    output = RUN_DIR / f"output_{stage}"
    existing = load_jsonl(output / "decisions.jsonl", fingerprint)
    pending = [item for item in items if item["source_file"] not in existing]
    if pattern:
        regex = re.compile(pattern, re.IGNORECASE)
        pending = [item for item in pending if regex.search(item["source_file"]) or regex.search(item["title"])]
    clients = api_clients()
    max_workers = workers or int(CONFIG["batch"]["max_concurrency"])
    print(f"stage={stage} eligible={len(items)} existing={len(existing)} pending_selected={len(pending)} workers={max_workers}", flush=True)

    def work(item: dict[str, Any]) -> dict[str, Any]:
        user = fill(template, {**item, "audit_round": stage, "round_instruction": round_instruction})
        return call_model(item, stage, clients, system, user, fingerprint)

    return run_pool(stage, pending, work, len(items), fingerprint, max_workers)


def run_adjudication(pattern: str | None, workers: int | None) -> int:
    items = {item["source_file"]: item for item in load_inputs()}
    a = load_jsonl(RUN_DIR / "output_audit_a" / "decisions.jsonl")
    b = load_jsonl(RUN_DIR / "output_audit_b" / "decisions.jsonl")
    if len(a) != 133 or len(b) != 133:
        raise RuntimeError(f"adjudication requires 133 completed decisions in each audit; got A={len(a)}, B={len(b)}")
    disagreements = [items[source] for source in sorted(items)
                     if bool(a[source]["strict_include"]) != bool(b[source]["strict_include"])]
    system = (RUN_DIR / "adjudication_system_prompt_cn.md").read_text(encoding="utf-8")
    template = (RUN_DIR / "adjudication_user_template_cn.md").read_text(encoding="utf-8")
    fingerprint = prompt_fingerprint("adjudication", system, template)
    output = RUN_DIR / "output_adjudication"
    existing = load_jsonl(output / "decisions.jsonl", fingerprint)
    pending = [item for item in disagreements if item["source_file"] not in existing]
    if pattern:
        regex = re.compile(pattern, re.IGNORECASE)
        pending = [item for item in pending if regex.search(item["source_file"]) or regex.search(item["title"])]
    clients = api_clients()
    max_workers = workers or int(CONFIG["batch"]["max_concurrency"])
    print(f"stage=adjudication disagreements={len(disagreements)} existing={len(existing)} pending_selected={len(pending)} workers={max_workers}", flush=True)

    def work(item: dict[str, Any]) -> dict[str, Any]:
        source = item["source_file"]
        user = fill(template, {**item,
            "audit_a": json.dumps(a[source], ensure_ascii=False, indent=2),
            "audit_b": json.dumps(b[source], ensure_ascii=False, indent=2)})
        return call_model(item, "adjudication", clients, system, user, fingerprint)

    return run_pool("adjudication", pending, work, len(disagreements), fingerprint, max_workers)


def run_pool(stage: str, pending: list[dict[str, Any]], work: Any,
             eligible: int, fingerprint: str, workers: int) -> int:
    output = RUN_DIR / f"output_{stage}"
    completed = failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {executor.submit(work, item): item for item in pending}
        for future in concurrent.futures.as_completed(future_map):
            item = future_map[future]
            try:
                append_jsonl(output / "decisions.jsonl", future.result())
                completed += 1
            except Exception as exc:
                append_jsonl(output / "errors.jsonl", {
                    "source_file": item["source_file"], "stage": stage,
                    "error": str(exc), "failed_at": utc_now(),
                    "prompt_fingerprint": fingerprint,
                })
                failed += 1
            if (completed + failed) % int(CONFIG["batch"]["progress_interval"]) == 0:
                print(f"progress stage={stage} finished={completed + failed}/{len(pending)} succeeded={completed} failed={failed}", flush=True)
    print(f"done stage={stage} eligible={eligible} new_completed={completed} failed={failed}", flush=True)
    return 1 if failed else 0


def build_final() -> None:
    inputs = {item["source_file"]: item for item in load_inputs()}
    a = load_jsonl(RUN_DIR / "output_audit_a" / "decisions.jsonl")
    b = load_jsonl(RUN_DIR / "output_audit_b" / "decisions.jsonl")
    adj = load_jsonl(RUN_DIR / "output_adjudication" / "decisions.jsonl")
    if len(a) != 133 or len(b) != 133:
        raise RuntimeError(f"cannot build final: A={len(a)}, B={len(b)}")
    final_rows = []
    for source, item in inputs.items():
        av = bool(a[source]["strict_include"])
        bv = bool(b[source]["strict_include"])
        if av == bv:
            included = av
            resolution = "independent_agreement_include" if av else "independent_agreement_exclude"
            decisive = a[source] if float(a[source]["confidence"]) >= float(b[source]["confidence"]) else b[source]
        else:
            if source not in adj:
                raise RuntimeError(f"missing adjudication for disagreement: {source}")
            included = bool(adj[source]["adjudicated_include"])
            resolution = "adjudicated_include" if included else "adjudicated_exclude"
            decisive = adj[source]
        final_rows.append({
            **{k: v for k, v in item.items() if k != "fulltext"},
            "final_include": included,
            "resolution": resolution,
            "audit_a_include": av,
            "audit_b_include": bv,
            "metric_status": decisive.get("metric_status", ""),
            "core_goal_status": decisive.get("core_goal_status", ""),
            "artifact_status": decisive.get("artifact_status", ""),
            "exclusion_trigger_codes": decisive.get("exclusion_trigger_codes", []),
            "final_reason_cn": decisive.get("final_reason_cn", ""),
            "confidence": decisive.get("confidence", ""),
        })
    final_rows.sort(key=lambda row: row["source_file"])
    deliver = RUN_DIR / "deliverables"
    deliver.mkdir(parents=True, exist_ok=True)
    fields = ["record_id", "source_file", "title", "authors", "year", "journal", "doi",
              "final_include", "resolution", "audit_a_include", "audit_b_include",
              "metric_status", "core_goal_status", "artifact_status",
              "exclusion_trigger_codes", "final_reason_cn", "confidence", "fulltext_chars"]
    with (deliver / "final_audit_all_133.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in final_rows:
            row = dict(row)
            row["exclusion_trigger_codes"] = " | ".join(row["exclusion_trigger_codes"] or [])
            writer.writerow(row)
    included = [row for row in final_rows if row["final_include"]]
    with (deliver / "final_included_articles.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in included:
            row = dict(row)
            row["exclusion_trigger_codes"] = " | ".join(row["exclusion_trigger_codes"] or [])
            writer.writerow(row)
    excluded = [row for row in final_rows if not row["final_include"]]
    with (deliver / "final_excluded_articles.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in excluded:
            row = dict(row)
            row["exclusion_trigger_codes"] = " | ".join(row["exclusion_trigger_codes"] or [])
            writer.writerow(row)
    with (deliver / "full_audit_trail_133.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for row in final_rows:
            source = row["source_file"]
            handle.write(json.dumps({
                "source_file": source,
                "record_id": row["record_id"],
                "title": row["title"],
                "final_include": row["final_include"],
                "resolution": row["resolution"],
                "audit_a": a[source],
                "audit_b": b[source],
                "adjudication": adj.get(source),
            }, ensure_ascii=False) + "\n")
    disagreements = sum(row["audit_a_include"] != row["audit_b_include"] for row in final_rows)
    summary = {
        "generated_at": utc_now(), "input_count": 133,
        "audit_a_include_count": sum(bool(row["audit_a_include"]) for row in final_rows),
        "audit_b_include_count": sum(bool(row["audit_b_include"]) for row in final_rows),
        "independent_disagreement_count": disagreements,
        "final_include_count": len(included),
        "final_exclude_count": 133 - len(included),
        "resolution_counts": dict(Counter(row["resolution"] for row in final_rows)),
        "metric_status_counts": dict(Counter(row["metric_status"] for row in final_rows)),
        "core_goal_status_counts": dict(Counter(row["core_goal_status"] for row in final_rows)),
        "artifact_status_counts": dict(Counter(row["artifact_status"] for row in final_rows)),
        "included_year_counts": dict(Counter(row["year"] for row in included)),
        "included_journal_counts": dict(Counter(row["journal"] for row in included)),
    }
    (deliver / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 133 篇候选文献最终审计", "",
             f"- 输入：133", f"- 审计 A 纳入：{summary['audit_a_include_count']}",
             f"- 审计 B 纳入：{summary['audit_b_include_count']}",
             f"- 两轮分歧：{disagreements}", f"- 最终纳入：{len(included)}",
             f"- 最终排除：{133-len(included)}", "", "## 最终纳入", ""]
    for row in included:
        lines.extend([f"### {row['title']}", "",
                      f"- 年份 / 期刊：{row['year']} / {row['journal']}",
                      f"- 指标 / 核心目标 / 制品：{row['metric_status']} / {row['core_goal_status']} / {row['artifact_status']}",
                      f"- 结论：{row['final_reason_cn']}", ""])
    (deliver / "final_report_cn.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("audit_a", "audit_b", "adjudication", "build"), required=True)
    parser.add_argument("--only-pattern")
    parser.add_argument("--workers", type=int)
    args = parser.parse_args()
    if args.stage in {"audit_a", "audit_b"}:
        return run_independent(args.stage, args.only_pattern, args.workers)
    if args.stage == "adjudication":
        return run_adjudication(args.only_pattern, args.workers)
    build_final()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
