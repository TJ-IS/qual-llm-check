#!/usr/bin/env python3
"""Fresh full-text red-team audit of the 27 V3 inclusions."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

import run_unified_screening as base


RUN_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = RUN_DIR / "output_final_red_team_v4"


def load_v3_candidates(config: dict) -> list[Path]:
    rows = {}
    source_path = RUN_DIR / "output_full_v3" / "decisions.jsonl"
    with source_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                rows[str(row["source_file"])] = row
    sources = sorted(source for source, row in rows.items() if row.get("strict_include") is True)
    if len(rows) != 2475 or len(sources) != 27:
        raise RuntimeError(f"Expected 2475 V3 decisions and 27 candidates, got {len(rows)} / {len(sources)}")
    fulltext_dir = base.resolve_from_run(str(config["input_dir"]))
    return [fulltext_dir / source for source in sources]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-concurrency", type=int, default=27)
    args = parser.parse_args()
    if not 1 <= args.max_concurrency <= 100:
        parser.error("--max-concurrency must be between 1 and 100")

    config = base.load_config()
    config = json.loads(json.dumps(config))
    config["analysis_version"] = "ais-basket-unified-strict-artifact-class-final-red-team-v4"
    config["batch"]["max_concurrency"] = args.max_concurrency
    system = "\n\n".join(
        (RUN_DIR / name).read_text(encoding="utf-8").strip()
        for name in (
            "system_prompt_cn.md",
            "calibration_corrections_cn.md",
            "final_screening_addendum_cn.md",
            "final_red_team_addendum_cn.md",
        )
    )
    template = (RUN_DIR / "user_prompt_template_cn.md").read_text(encoding="utf-8").strip()
    fingerprint = hashlib.sha256(
        json.dumps(
            {
                "analysis_version": config["analysis_version"],
                "model": config["model"]["name"],
                "system": system,
                "template": template,
            },
            ensure_ascii=False,
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()
    files = load_v3_candidates(config)
    decisions_path = OUTPUT_DIR / "decisions.jsonl"
    errors_path = OUTPUT_DIR / "errors.jsonl"
    decisions = base.load_current(decisions_path, fingerprint)
    pending = [path for path in files if path.name not in decisions]
    print(
        f"v3_candidates={len(files)} existing={len(decisions)} pending={len(pending)} "
        f"model={config['model']['name']} concurrency={args.max_concurrency}",
        flush=True,
    )
    if pending:
        load_dotenv(base.resolve_from_run(str(config["env_file"])))
        api_key = os.getenv(str(config["model"]["api_key_env"]))
        if not api_key:
            raise RuntimeError("missing API key")
        base_url = os.getenv(str(config["model"]["base_url_env"])) or str(config["model"]["base_url"])
        clients = base.ThreadClients(api_key, base_url, float(config["model"]["timeout_seconds"]))
        failed = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_concurrency) as pool:
            futures = {
                pool.submit(base.analyze_one, path, clients, config, system, template, fingerprint): path
                for path in pending
            }
            for future in concurrent.futures.as_completed(futures):
                path = futures[future]
                try:
                    row = future.result()
                    base.append_jsonl(decisions_path, row)
                    decisions[path.name] = row
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
        if failed:
            print(f"failed={failed}", flush=True)
    base.write_reports(OUTPUT_DIR, files, decisions, config, fingerprint)
    print(
        f"completed={len(decisions)}/{len(files)} strict_include="
        f"{sum(bool(row.get('strict_include')) for row in decisions.values())}",
        flush=True,
    )
    return 0 if len(decisions) == len(files) else 2


if __name__ == "__main__":
    sys.exit(main())
