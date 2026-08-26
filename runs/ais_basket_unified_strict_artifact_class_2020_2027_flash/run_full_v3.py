#!/usr/bin/env python3
"""Run the V3 unified strict screen over every local 2020-2027 full text."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import random
import sys
import time
from collections import Counter
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

import run_unified_screening as base


RUN_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = RUN_DIR / "output_full_v3"


def analyze_one_with_closed_client(
    path: Path,
    api_key: str,
    base_url: str,
    timeout: float,
    config: dict,
    system: str,
    template: str,
    fingerprint: str,
) -> dict:
    """Analyze one article and explicitly close its HTTP connection before returning."""

    raw = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, fulltext = base.parse_frontmatter(raw)
    metadata = base.metadata_for(path, fulltext, frontmatter)
    user = template.format(**metadata, fulltext=fulltext)
    model = config["model"]
    retries = int(config["batch"]["retries"])
    last_error: Exception | None = None
    for attempt in range(1, retries + 2):
        try:
            with OpenAI(api_key=api_key, base_url=base_url, timeout=timeout) as client:
                response = client.chat.completions.create(
                    model=str(model["name"]),
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    temperature=float(model["temperature"]),
                    max_tokens=int(model["max_tokens"]),
                    response_format={"type": "json_object"},
                )
            message = response.choices[0].message
            content = message.content or getattr(message, "reasoning_content", None) or ""
            payload = base.parse_json_object(content)
            artifact = payload.get("software_artifact")
            if isinstance(artifact, dict) and artifact.get("artifact_status") == "no_qualifying_metric":
                artifact["artifact_status"] = "unclear"
            decision = base.validate_decision(payload, metadata["record_id"])
            return {
                **{key: value for key, value in metadata.items() if key != "fulltext_chars"},
                "fulltext_chars": int(metadata["fulltext_chars"]),
                "analysis_version": config["analysis_version"],
                "prompt_fingerprint": fingerprint,
                "model": model["name"],
                "analysis_mode": "one_complete_local_fulltext_per_request_closed_client",
                "attempts": attempt,
                "completed_at": base.utc_now(),
                **decision,
                "usage": base.usage_dict(response),
            }
        except Exception as exc:
            last_error = exc
            if attempt > retries:
                break
            delay = float(config["batch"]["retry_base_delay_seconds"]) * (2 ** (attempt - 1))
            time.sleep(delay + random.uniform(0, 0.5))
    assert last_error is not None
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}") from last_error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-concurrency", type=int, default=100)
    parser.add_argument("--batch-size", type=int)
    args = parser.parse_args()
    if not 1 <= args.max_concurrency <= 300:
        parser.error("--max-concurrency must be between 1 and 300")
    if args.batch_size is not None and args.batch_size < 1:
        parser.error("--batch-size must be positive")

    config = base.load_config()
    config = json.loads(json.dumps(config))
    config["analysis_version"] = "ais-basket-unified-strict-artifact-class-full-v3"
    config["batch"]["max_concurrency"] = args.max_concurrency
    prompt_parts = [
        "system_prompt_cn.md",
        "calibration_corrections_cn.md",
        "final_screening_addendum_cn.md",
    ]
    system = "\n\n".join((RUN_DIR / name).read_text(encoding="utf-8").strip() for name in prompt_parts)
    template = (RUN_DIR / "user_prompt_template_cn.md").read_text(encoding="utf-8").strip()
    fingerprint = hashlib.sha256(
        json.dumps(
            {
                "analysis_version": config["analysis_version"],
                "model": config["model"]["name"],
                "year_range": config["year_range"],
                "system": system,
                "template": template,
            },
            ensure_ascii=False,
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()

    input_dir = base.resolve_from_run(str(config["input_dir"]))
    year_from = int(config["year_range"]["from"])
    year_to = int(config["year_range"]["to"])
    files = [
        path
        for path in sorted(input_dir.glob("*.md"))
        if (year := base.year_from_filename(path)) is not None and year_from <= year <= year_to
    ]
    if len(files) != 2475:
        raise RuntimeError(f"Expected 2475 full texts in scope, got {len(files)}")
    decisions_path = OUTPUT_DIR / "decisions.jsonl"
    errors_path = OUTPUT_DIR / "errors.jsonl"
    decisions = base.load_current(decisions_path, fingerprint)
    pending = [path for path in files if path.name not in decisions]
    if args.batch_size is not None:
        pending = pending[: args.batch_size]
    print(
        f"fulltexts={len(files)} years={dict(sorted(Counter(base.year_from_filename(p) for p in files).items()))} "
        f"existing={len(decisions)} pending={len(pending)} model={config['model']['name']} "
        f"concurrency={args.max_concurrency}",
        flush=True,
    )
    print(f"prompt_fingerprint={fingerprint}", flush=True)

    failed = 0
    if pending:
        load_dotenv(base.resolve_from_run(str(config["env_file"])))
        api_key = os.getenv(str(config["model"]["api_key_env"]))
        if not api_key:
            raise RuntimeError("missing API key")
        base_url = os.getenv(str(config["model"]["base_url_env"])) or str(config["model"]["base_url"])
        timeout = float(config["model"]["timeout_seconds"])
        started = time.monotonic()
        handled = 0
        new_includes = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_concurrency) as pool:
            futures = {
                pool.submit(
                    analyze_one_with_closed_client,
                    path,
                    api_key,
                    base_url,
                    timeout,
                    config,
                    system,
                    template,
                    fingerprint,
                ): path
                for path in pending
            }
            for future in concurrent.futures.as_completed(futures):
                path = futures[future]
                try:
                    row = future.result()
                    base.append_jsonl(decisions_path, row)
                    decisions[path.name] = row
                    new_includes += int(bool(row.get("strict_include")))
                except Exception as exc:
                    failed += 1
                    base.append_jsonl(
                        errors_path,
                        {
                            "source_file": path.name,
                            "error_type": type(exc).__name__,
                            "error": str(exc),
                            "prompt_fingerprint": fingerprint,
                        },
                    )
                    print(f"ERROR file={path.name} error={exc}", flush=True)
                handled += 1
                if handled % 25 == 0 or handled == len(pending):
                    elapsed = time.monotonic() - started
                    print(
                        f"progress={handled}/{len(pending)} failed={failed} strict_include={new_includes} "
                        f"rate={handled / elapsed if elapsed else 0:.2f}/s",
                        flush=True,
                    )
                if handled % 250 == 0:
                    base.write_reports(OUTPUT_DIR, files, decisions, config, fingerprint)

    base.write_reports(OUTPUT_DIR, files, decisions, config, fingerprint)
    print(
        f"completed={len(decisions)}/{len(files)} failed_this_run={failed} "
        f"strict_include={sum(bool(row.get('strict_include')) for row in decisions.values())}",
        flush=True,
    )
    if failed:
        return 2
    if args.batch_size is not None:
        return 0
    return 0 if len(decisions) == len(files) else 2


if __name__ == "__main__":
    sys.exit(main())
