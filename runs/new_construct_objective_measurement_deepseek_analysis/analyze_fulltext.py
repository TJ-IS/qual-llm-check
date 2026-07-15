#!/usr/bin/env python3
"""Find papers that develop a new construct and measure it objectively."""

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
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


RUN_DIR = Path(__file__).resolve().parent
CONFIG_PATH = RUN_DIR / "config.json"
RELEVANCE_VALUES = {
    "explicit_named_is_construct",
    "construct_mentioned_but_not_linked",
    "only_other_meaning",
}
OBJECTIVITY_VALUES = {
    "strict_objective",
    "rater_based_nonquestionnaire",
    "self_report_questionnaire",
    "not_measured",
    "unclear",
}
OUTCOME_VALUES = {
    "target_match",
    "no_new_construct_claim",
    "new_measure_only",
    "no_objective_measurement",
    "measurement_not_same_construct",
    "other_construct_meaning",
    "unclear",
}


class ContextLengthExceeded(RuntimeError):
    """Raised when the API explicitly rejects an overlong context."""


@dataclass(frozen=True)
class Article:
    path: Path
    source_file: str
    article_id: str
    title: str
    authors: str
    year: str
    journal: str
    doi: str
    fulltext: str


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def resolve_from_run(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (RUN_DIR / path).resolve()


def cli_path(value: Path | None, fallback: str) -> Path:
    return value.resolve() if value is not None else resolve_from_run(fallback)


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_prompt(config: dict[str, Any], key: str) -> str:
    value = config["prompt_files"][key]
    return (RUN_DIR / value).read_text(encoding="utf-8").strip()


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


def load_article(path: Path) -> Article:
    metadata, fulltext = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    filename_id = path.name.split("_", 1)[0].lstrip("0") or "0"
    return Article(
        path=path,
        source_file=path.name,
        article_id=str(metadata.get("otero_id") or filename_id),
        title=str(metadata.get("title") or path.stem),
        authors=str(metadata.get("authors") or ""),
        year=str(metadata.get("year") or ""),
        journal=str(metadata.get("journal") or ""),
        doi=str(metadata.get("doi") or ""),
        fulltext=fulltext,
    )


def select_files(input_dir: Path, requested: list[str] | None) -> list[Path]:
    if not requested:
        return sorted(input_dir.glob("*.md"))
    selected: dict[str, Path] = {}
    for value in requested:
        exact = input_dir / value
        matches = [exact] if exact.is_file() else sorted(input_dir.glob(value))
        if not matches:
            raise FileNotFoundError(f"No input article matches --file {value!r}")
        for path in matches:
            selected[path.name] = path
    return [selected[name] for name in sorted(selected)]


def split_fulltext(text: str, chunk_chars: int, overlap_chars: int) -> list[str]:
    if len(text) <= chunk_chars:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(text):
        target = min(len(text), start + chunk_chars)
        end = target
        if target < len(text):
            boundary = text.rfind("\n\n", start + int(chunk_chars * 0.7), target)
            if boundary > start:
                end = boundary
        chunks.append(text[start:end])
        if end >= len(text):
            break
        next_start = max(start + 1, end - overlap_chars)
        start = next_start
    return chunks


def parse_json_object(content: str) -> dict[str, Any]:
    if not content or not content.strip():
        raise ValueError("empty model response")
    text = content.strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            raise
        payload = json.loads(text[start : end + 1])
    if not isinstance(payload, dict):
        raise ValueError("model response is not a JSON object")
    return payload


def normalized_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def prompt_fingerprint(config: dict[str, Any], prompts: dict[str, str]) -> str:
    fingerprint_input = {
        "analysis_version": config.get("analysis_version"),
        "model": config.get("model", {}).get("name"),
        "prompts": prompts,
    }
    encoded = json.dumps(fingerprint_input, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def normalize_final(payload: dict[str, Any]) -> dict[str, Any]:
    relevance = str(payload.get("construct_term_relevance") or "").strip()
    if relevance not in RELEVANCE_VALUES:
        raise ValueError(f"invalid construct_term_relevance: {relevance!r}")
    claims_new = payload.get("claims_new_construct_development")
    objective_measurement = payload.get("objective_measurement_of_new_construct")
    target_match = payload.get("new_construct_with_objective_measurement")
    if not isinstance(claims_new, bool):
        raise ValueError("claims_new_construct_development must be boolean")
    if not isinstance(objective_measurement, bool):
        raise ValueError("objective_measurement_of_new_construct must be boolean")
    if not isinstance(target_match, bool):
        raise ValueError("new_construct_with_objective_measurement must be boolean")
    objectivity = str(payload.get("new_construct_measurement_objectivity") or "").strip()
    if objectivity not in OBJECTIVITY_VALUES:
        raise ValueError(f"invalid new_construct_measurement_objectivity: {objectivity!r}")
    outcome = str(payload.get("screening_outcome") or "").strip()
    if outcome not in OUTCOME_VALUES:
        raise ValueError(f"invalid screening_outcome: {outcome!r}")
    new_constructs = normalized_list(payload.get("new_constructs"))
    objectively_measured = normalized_list(payload.get("objectively_measured_new_constructs"))
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    return {
        "construct_term_relevance": relevance,
        "claims_new_construct_development": claims_new,
        "new_construct_development_summary_cn": str(
            payload.get("new_construct_development_summary_cn") or ""
        ).strip(),
        "new_constructs": new_constructs,
        "objective_measurement_of_new_construct": objective_measurement,
        "new_construct_measurement_objectivity": objectivity,
        "objective_measurement_summary_cn": str(
            payload.get("objective_measurement_summary_cn") or ""
        ).strip(),
        "objectively_measured_new_constructs": objectively_measured,
        "new_construct_with_objective_measurement": target_match,
        "screening_outcome": outcome,
        "match_summary_cn": str(payload.get("match_summary_cn") or "").strip(),
        "confidence": max(0.0, min(1.0, confidence)),
        "limitations_cn": str(payload.get("limitations_cn") or "").strip(),
    }


def usage_dict(response: Any) -> dict[str, int]:
    usage = response.usage
    if usage is None:
        return {}
    return {
        "prompt_tokens": int(usage.prompt_tokens or 0),
        "completion_tokens": int(usage.completion_tokens or 0),
        "total_tokens": int(usage.total_tokens or 0),
    }


def add_usage(total: dict[str, int], addition: dict[str, int]) -> None:
    for key, value in addition.items():
        total[key] = total.get(key, 0) + int(value)


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


def request_json(
    clients: ThreadClients,
    model: str,
    system_prompt: str,
    user_prompt: str,
    max_tokens: int,
    retries: int,
    retry_base_delay: float,
) -> tuple[dict[str, Any], dict[str, int]]:
    last_error: BaseException | None = None
    for attempt in range(retries + 1):
        try:
            response = clients.get().chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0,
                max_tokens=max_tokens,
                response_format={"type": "json_object"},
            )
            content = response.choices[0].message.content or ""
            return parse_json_object(content), usage_dict(response)
        except Exception as exc:
            message = str(exc).lower()
            context_markers = (
                "maximum context length",
                "context length",
                "context_length",
                "too many tokens",
                "max context",
                "token limit",
            )
            if any(marker in message for marker in context_markers):
                raise ContextLengthExceeded(str(exc)) from exc
            last_error = exc
            if attempt >= retries:
                break
            delay = retry_base_delay * (2**attempt) + random.uniform(0, 0.5)
            time.sleep(delay)
    assert last_error is not None
    raise last_error


def article_metadata(article: Article) -> dict[str, str]:
    return {
        "source_file": article.source_file,
        "article_id": article.article_id,
        "title": article.title,
        "authors": article.authors,
        "year": article.year,
        "journal": article.journal,
        "doi": article.doi,
    }


def analyze_article(
    article: Article,
    config: dict[str, Any],
    prompts: dict[str, str],
    clients: ThreadClients,
    fingerprint: str,
) -> dict[str, Any]:
    model_config = config["model"]
    batch_config = config["batch"]
    usage: dict[str, int] = {}
    direct_max_chars = int(batch_config["direct_max_chars"])
    direct_succeeded = False
    context_fallback = False

    if len(article.fulltext) <= direct_max_chars:
        user_prompt = prompts["user_template"].format(
            **article_metadata(article),
            fulltext_chars=len(article.fulltext),
            fulltext=article.fulltext,
        )
        try:
            payload, call_usage = request_json(
                clients,
                str(model_config["name"]),
                prompts["system"],
                user_prompt,
                int(model_config["max_tokens"]),
                int(batch_config["retries"]),
                float(batch_config["retry_base_delay"]),
            )
            add_usage(usage, call_usage)
            decision = normalize_final(payload)
            mode = "fulltext_single_request"
            chunk_count = 1
            direct_succeeded = True
        except ContextLengthExceeded:
            context_fallback = True

    if not direct_succeeded:
        chunks = split_fulltext(
            article.fulltext,
            int(batch_config["chunk_chars"]),
            int(batch_config["chunk_overlap_chars"]),
        )
        findings: list[dict[str, Any]] = []
        for index, chunk in enumerate(chunks, start=1):
            chunk_user = (
                f"文章元数据：{json.dumps(article_metadata(article), ensure_ascii=False)}\n"
                f"这是全文第 {index}/{len(chunks)} 块，字符范围由脚本连续切分并有少量重叠。\n\n"
                f"<ARTICLE_CHUNK>\n{chunk}\n</ARTICLE_CHUNK>"
            )
            finding, call_usage = request_json(
                clients,
                str(model_config["name"]),
                prompts["chunk_system"],
                chunk_user,
                int(model_config["chunk_max_tokens"]),
                int(batch_config["retries"]),
                float(batch_config["retry_base_delay"]),
            )
            add_usage(usage, call_usage)
            findings.append({"chunk_index": index, **finding})

        synthesis_user = (
            "这篇文章因过长而被连续分块；所有块均已读取。请根据下面覆盖整篇全文的逐块证据做最终判断，"
            "不要因为某一块没有证据就忽略其他块。\n\n"
            f"文章元数据：{json.dumps(article_metadata(article), ensure_ascii=False)}\n"
            f"全文字符数：{len(article.fulltext)}；分块数：{len(chunks)}\n\n"
            f"<CHUNK_FINDINGS>\n{json.dumps(findings, ensure_ascii=False)}\n</CHUNK_FINDINGS>"
        )
        payload, call_usage = request_json(
            clients,
            str(model_config["name"]),
            prompts["system"],
            synthesis_user,
            int(model_config["max_tokens"]),
            int(batch_config["retries"]),
            float(batch_config["retry_base_delay"]),
        )
        add_usage(usage, call_usage)
        decision = normalize_final(payload)
        mode = "fulltext_chunked_then_synthesized"
        chunk_count = len(chunks)

    return {
        **article_metadata(article),
        "analysis_version": str(config.get("analysis_version") or ""),
        "prompt_fingerprint": fingerprint,
        "model": str(model_config["name"]),
        "analysis_mode": mode,
        "fulltext_chars": len(article.fulltext),
        "chunk_count": chunk_count,
        "context_length_fallback": context_fallback,
        "completed_at": utc_now(),
        **decision,
        "usage": usage,
    }


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def load_jsonl_by_file(path: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return records
    with path.open("r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            payload = json.loads(line)
            source_file = str(payload.get("source_file") or "")
            if not source_file:
                raise ValueError(f"Missing source_file in {path}:{number}")
            records[source_file] = payload
    return records


def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    analysis_version: str,
    fingerprint: str,
) -> None:
    csv_path = output_dir / "decisions.csv"
    temp_csv = csv_path.with_suffix(".csv.tmp")
    fields = [
        "source_file",
        "article_id",
        "title",
        "year",
        "journal",
        "doi",
        "analysis_version",
        "construct_term_relevance",
        "claims_new_construct_development",
        "new_construct_development_summary_cn",
        "new_constructs",
        "objective_measurement_of_new_construct",
        "new_construct_measurement_objectivity",
        "objective_measurement_summary_cn",
        "objectively_measured_new_constructs",
        "new_construct_with_objective_measurement",
        "screening_outcome",
        "match_summary_cn",
        "confidence",
        "analysis_mode",
        "fulltext_chars",
    ]
    with temp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for source_file in sorted(decisions):
            row = dict(decisions[source_file])
            row["new_constructs"] = json.dumps(
                row.get("new_constructs", []), ensure_ascii=False
            )
            row["objectively_measured_new_constructs"] = json.dumps(
                row.get("objectively_measured_new_constructs", []), ensure_ascii=False
            )
            writer.writerow({field: row.get(field, "") for field in fields})
    os.replace(temp_csv, csv_path)

    values = list(decisions.values())
    summary = {
        "updated_at": utc_now(),
        "analysis_version": analysis_version,
        "prompt_fingerprint": fingerprint,
        "input_fulltext_files": len(all_files),
        "completed": len(decisions),
        "pending": len(all_files) - len({path.name for path in all_files} & set(decisions)),
        "construct_relevance_counts": {
            value: sum(row.get("construct_term_relevance") == value for row in values)
            for value in sorted(RELEVANCE_VALUES)
        },
        "claims_new_construct_development_true": sum(
            row.get("claims_new_construct_development") is True for row in values
        ),
        "objective_measurement_of_new_construct_true": sum(
            row.get("objective_measurement_of_new_construct") is True for row in values
        ),
        "new_construct_with_objective_measurement_true": sum(
            row.get("new_construct_with_objective_measurement") is True for row in values
        ),
        "new_construct_measurement_objectivity_counts": {
            value: sum(row.get("new_construct_measurement_objectivity") == value for row in values)
            for value in sorted(OBJECTIVITY_VALUES)
        },
        "screening_outcome_counts": {
            value: sum(row.get("screening_outcome") == value for row in values)
            for value in sorted(OUTCOME_VALUES)
        },
        "usage": {
            key: sum(int((row.get("usage") or {}).get(key, 0)) for row in values)
            for key in ("prompt_tokens", "completion_tokens", "total_tokens")
        },
    }
    summary_path = output_dir / "summary.json"
    temp_summary = summary_path.with_suffix(".json.tmp")
    temp_summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp_summary, summary_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, help="Override config input directory")
    parser.add_argument("--output-dir", type=Path, help="Override config output directory")
    parser.add_argument("--env-file", type=Path, help="Override config .env path")
    parser.add_argument("--file", action="append", help="Exact filename or glob; repeatable")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, help="Analyze only the first N pending articles")
    parser.add_argument("--max-concurrency", type=int, help="Override configured concurrency")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.offset < 0:
        parser.error("--offset must be non-negative")
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    if args.max_concurrency is not None and not 1 <= args.max_concurrency <= 16:
        parser.error("--max-concurrency must be between 1 and 16")
    return args


def main() -> int:
    args = parse_args()
    config = load_config()
    input_dir = cli_path(args.input_dir, str(config["input_dir"]))
    output_dir = cli_path(args.output_dir, str(config["output_dir"]))
    env_file = cli_path(args.env_file, str(config["env_file"]))
    all_files = sorted(input_dir.glob("*.md"))
    selected_files = select_files(input_dir, args.file)[args.offset :]
    decisions_path = output_dir / "decisions.jsonl"
    errors_path = output_dir / "errors.jsonl"
    prompts = {
        "system": read_prompt(config, "system"),
        "user_template": read_prompt(config, "user_template"),
        "chunk_system": read_prompt(config, "chunk_system"),
    }
    fingerprint = prompt_fingerprint(config, prompts)
    previous_decisions = load_jsonl_by_file(decisions_path)
    decisions = {
        source_file: record
        for source_file, record in previous_decisions.items()
        if record.get("prompt_fingerprint") == fingerprint
    }
    stale_count = len(previous_decisions) - len(decisions)
    pending = [path for path in selected_files if path.name not in decisions]
    if args.limit is not None:
        pending = pending[: args.limit]

    print(
        f"Input full texts: {len(all_files)}; selected: {len(selected_files)}; "
        f"already completed for current prompt: {len(decisions)}; stale prior results: {stale_count}; "
        f"pending this run: {len(pending)}"
    )
    print(f"Output directory: {output_dir}")
    if args.dry_run:
        threshold = int(config["batch"]["direct_max_chars"])
        for path in pending[:10]:
            article = load_article(path)
            mode = "single" if len(article.fulltext) <= threshold else "chunked"
            print(f"DRY RUN {path.name}: chars={len(article.fulltext)} mode={mode}")
        return 0
    if not pending:
        output_dir.mkdir(parents=True, exist_ok=True)
        write_reports(
            output_dir,
            all_files,
            decisions,
            str(config.get("analysis_version") or ""),
            fingerprint,
        )
        print("Nothing to do.")
        return 0

    load_dotenv(env_file)
    model_config = config["model"]
    api_key_env = str(model_config["api_key_env"])
    api_key = os.getenv(api_key_env)
    if not api_key:
        raise RuntimeError(f"API key not found. Set {api_key_env} in {env_file}")
    base_url = os.getenv(str(model_config["base_url_env"])) or str(model_config["base_url"])
    clients = ThreadClients(api_key, base_url, float(model_config["timeout"]))
    max_concurrency = args.max_concurrency or int(config["batch"]["max_concurrency"])
    output_dir.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    completed_now = 0
    failed_now = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_concurrency) as pool:
        futures = {
            pool.submit(analyze_article, load_article(path), config, prompts, clients, fingerprint): path
            for path in pending
        }
        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                record = future.result()
                append_jsonl(decisions_path, record)
                decisions[path.name] = record
                completed_now += 1
                flag_a = record["claims_new_construct_development"]
                flag_b = record["objective_measurement_of_new_construct"]
                flag_c = record["new_construct_with_objective_measurement"]
                print(
                    f"[{completed_now + failed_now}/{len(pending)}] OK {path.name} "
                    f"new_construct={flag_a} objective={flag_b} target_match={flag_c}"
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
                    },
                )
                print(f"[{completed_now + failed_now}/{len(pending)}] ERROR {path.name}: {type(exc).__name__}: {exc}")

    write_reports(
        output_dir,
        all_files,
        decisions,
        str(config.get("analysis_version") or ""),
        fingerprint,
    )
    elapsed = time.monotonic() - started
    print(
        f"Run finished: completed={completed_now}, failed={failed_now}, "
        f"elapsed_seconds={elapsed:.1f}. Re-run the same command to resume."
    )
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
