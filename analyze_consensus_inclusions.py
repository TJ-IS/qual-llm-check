import argparse
import csv
import json
import os
import re
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_RUN_DIR = Path("runs/coding_agent_ux_misq_isr")
DEFAULT_INPUT = "included_consensus.csv"
DEFAULT_DRAFT_JSONL = "consensus_inclusion_strict_analysis_draft.jsonl"
DEFAULT_OUTPUT_MD = "consensus_inclusion_strict_analysis.md"


SYSTEM_PROMPT = """You are auditing literature screening results for an information-systems research project.

Research target:
We want to develop important individual-level user-experience concepts for coding agents. A coding agent can inspect a codebase, edit files, run commands/tests, perform multi-step work, create artifacts such as diffs/commits/PRs, and require the developer to delegate, supervise, verify, or take responsibility for its output.

Your task:
For each paper that was previously included by two LLM reviewers, strictly re-assess whether it is actually useful as concept material for coding-agent-specific UX research.

Do not trust the previous reviewers. They are only hints.

Strict criteria:
- Keep only if the paper contains an individual-level concept, phenomenon, behavior, perception, cognitive process, affective experience, collaboration pattern, learning process, trust/reliance/control issue, interruption/attention issue, expertise/identity issue, or verification/accountability issue.
- The concept should require meaningful adaptation for coding agents. Generic technology acceptance, generic trust, or generic productivity is not enough unless coding agents change the concept's meaning, boundary, stakes, or dimensions.
- The adapted concept should matter in real coding-agent use, such as code quality, safe delegation, verification burden, action boundaries, autonomy/control, responsibility, developer expertise, learning, work rhythm, trust calibration, or well-being.
- Mark weak analogies, consumer-platform analogies, market-level papers, and generic IT-use constructs as borderline or reject.

Judgment labels:
- 高适配: strong concept material; clear individual UX and clear coding-agent-specific adaptation with practical importance.
- 中适配: useful concept material but needs substantial adaptation or is less directly coding-agent-specific.
- 边界保留: interesting analogy, but indirect, generic, or weakly tied to coding-agent-specific UX; keep only for optional review.
- 建议剔除: not suitable after strict review; too generic, not individual UX, not practically important, or no meaningful coding-agent-specific adaptation.

Return only valid JSON:
{
  "items": [
    {
      "idx": 1,
      "main_cn": "one concise Chinese sentence about what the paper mainly did, based only on title/abstract/keywords",
      "strict_judgment": "高适配 | 中适配 | 边界保留 | 建议剔除",
      "candidate_concept_cn": "concise Chinese name of the possible coding-agent UX concept, or '无'",
      "strict_reason_cn": "one concise Chinese sentence explaining why it is or is not suitable under the strict criteria"
    }
  ]
}
"""


def normalize(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("\ufeff", "").strip()


def compact(value: str, limit: int = 1600) -> str:
    value = re.sub(r"\s+", " ", normalize(value))
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def load_rows(input_path: Path) -> list[dict[str, str]]:
    with input_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows: list[dict[str, str]] = []
        for idx, row in enumerate(reader, start=1):
            rows.append(
                {
                    "idx": str(idx),
                    "screen_row_number": normalize(row.get("screen_row_number")),
                    "title": normalize(row.get("Title")),
                    "year": normalize(row.get("Year")),
                    "journal": normalize(row.get("Source title")),
                    "document_type": normalize(row.get("Document Type")),
                    "author_keywords": normalize(row.get("Author Keywords")),
                    "index_keywords": normalize(row.get("Index Keywords")),
                    "abstract": normalize(row.get("Abstract")),
                    "r1_source_concept": normalize(row.get("deepseekv4pro_reviewer_1_source_concept")),
                    "r1_candidate": normalize(row.get("deepseekv4pro_reviewer_1_candidate_coding_agent_ux_concept")),
                    "r1_reason": normalize(row.get("deepseekv4pro_reviewer_1_reason")),
                    "r2_source_concept": normalize(row.get("deepseekv4pro_reviewer_2_source_concept")),
                    "r2_candidate": normalize(row.get("deepseekv4pro_reviewer_2_candidate_coding_agent_ux_concept")),
                    "r2_reason": normalize(row.get("deepseekv4pro_reviewer_2_reason")),
                }
            )
    return rows


def load_existing(jsonl_path: Path) -> dict[int, dict[str, str]]:
    existing: dict[int, dict[str, str]] = {}
    if not jsonl_path.exists():
        return existing
    with jsonl_path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            payload = json.loads(line)
            existing[int(payload["idx"])] = payload
    return existing


def batch_payload(rows: list[dict[str, str]]) -> str:
    items = []
    for row in rows:
        items.append(
            {
                "idx": int(row["idx"]),
                "title": row["title"],
                "year": row["year"],
                "journal": row["journal"],
                "document_type": row["document_type"],
                "keywords": "; ".join(
                    part for part in [row["author_keywords"], row["index_keywords"]] if part
                ),
                "abstract": compact(row["abstract"], 1700),
                "previous_reviewer_hints": {
                    "reviewer_1_source_concept": row["r1_source_concept"],
                    "reviewer_1_candidate": row["r1_candidate"],
                    "reviewer_1_reason": row["r1_reason"],
                    "reviewer_2_source_concept": row["r2_source_concept"],
                    "reviewer_2_candidate": row["r2_candidate"],
                    "reviewer_2_reason": row["r2_reason"],
                },
            }
        )
    return json.dumps({"items": items}, ensure_ascii=False, indent=2)


def parse_response(text: str) -> list[dict[str, str]]:
    text = text.strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end < start:
            raise
        payload = json.loads(text[start : end + 1])
    items = payload.get("items")
    if not isinstance(items, list):
        raise ValueError("response.items must be a list")
    parsed: list[dict[str, str]] = []
    for item in items:
        idx = int(item["idx"])
        parsed.append(
            {
                "idx": str(idx),
                "main_cn": normalize(item.get("main_cn")),
                "strict_judgment": normalize(item.get("strict_judgment")),
                "candidate_concept_cn": normalize(item.get("candidate_concept_cn")),
                "strict_reason_cn": normalize(item.get("strict_reason_cn")),
            }
        )
    return parsed


def analyze_missing(
    rows: list[dict[str, str]],
    jsonl_path: Path,
    batch_size: int,
    model: str,
    timeout: float,
) -> None:
    existing = load_existing(jsonl_path)
    missing = [row for row in rows if int(row["idx"]) not in existing]
    if not missing:
        print(f"All {len(rows)} rows already analyzed.")
        return

    load_dotenv()
    api_key = os.getenv("NEW_API_KEY")
    if not api_key:
        raise RuntimeError("NEW_API_KEY is required")
    client = OpenAI(
        api_key=api_key,
        base_url=os.getenv("NEW_API_BASE_URL") or "https://api.deepseek.com",
        timeout=timeout,
    )
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    for start in range(0, len(missing), batch_size):
        batch = missing[start : start + batch_size]
        prompt = "Audit these papers and return JSON.\n\n" + batch_payload(batch)
        for attempt in range(4):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0,
                    max_tokens=7000,
                    response_format={"type": "json_object"},
                )
                content = response.choices[0].message.content or ""
                parsed = parse_response(content)
                expected = {int(row["idx"]) for row in batch}
                received = {int(item["idx"]) for item in parsed}
                if expected != received:
                    raise ValueError(f"idx mismatch expected={sorted(expected)} received={sorted(received)}")
                with jsonl_path.open("a", encoding="utf-8", newline="\n") as file:
                    for item in parsed:
                        file.write(json.dumps(item, ensure_ascii=False) + "\n")
                print(f"Analyzed {start + len(batch)}/{len(missing)} missing rows.")
                break
            except Exception as exc:
                if attempt == 3:
                    raise
                sleep_seconds = 2 ** attempt + 0.5
                print(f"Retry after error: {type(exc).__name__}: {exc}")
                time.sleep(sleep_seconds)


def markdown_table_cell(value: str) -> str:
    value = normalize(value)
    value = value.replace("|", "\\|")
    value = re.sub(r"\s+", " ", value)
    return value


def write_report(rows: list[dict[str, str]], analyses: dict[int, dict[str, str]], output_path: Path) -> None:
    missing = [row["idx"] for row in rows if int(row["idx"]) not in analyses]
    if missing:
        raise RuntimeError(f"Missing analyses for rows: {', '.join(missing[:10])}")

    counts: dict[str, int] = {}
    for item in analyses.values():
        label = item["strict_judgment"]
        counts[label] = counts.get(label, 0) + 1

    label_order = ["高适配", "中适配", "边界保留", "建议剔除"]
    lines = [
        "# Coding Agent UX 共识纳入文献严格复判",
        "",
        "说明：本报告基于 `included_consensus.csv` 中 205 篇双模型共识纳入记录生成。标题、年份、期刊由脚本从 CSV 抽取；主要内容与适配判断基于 CSV 中的标题、摘要、关键词和候选概念进行严格复判，未做全文精读。",
        "",
        "判断标签：",
        "",
        "- `高适配`：个体 UX 概念清楚，且迁移到 coding agent 时有明确独特性和现实重要性。",
        "- `中适配`：有用，但需要较多概念改造，或 coding-agent-specific 程度稍弱。",
        "- `边界保留`：可作为类比素材，但间接、泛化或现实意义需要再论证。",
        "- `建议剔除`：严格复判后不建议作为核心素材。",
        "",
        "## 统计",
        "",
    ]
    for label in label_order:
        lines.append(f"- {label}: {counts.get(label, 0)}")
    extra_labels = sorted(set(counts) - set(label_order))
    for label in extra_labels:
        lines.append(f"- {label}: {counts[label]}")

    lines.extend(
        [
            "",
            "## 逐篇复判",
            "",
            "| # | 年份 | 期刊 | 标题 | 文章主要做了什么 | 严格判断 | 候选 coding-agent UX 概念 | 适配/剔除理由 |",
            "| ---: | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        analysis = analyses[int(row["idx"])]
        lines.append(
            "| "
            + " | ".join(
                [
                    row["idx"],
                    markdown_table_cell(row["year"]),
                    markdown_table_cell(row["journal"]),
                    markdown_table_cell(row["title"]),
                    markdown_table_cell(analysis["main_cn"]),
                    markdown_table_cell(analysis["strict_judgment"]),
                    markdown_table_cell(analysis["candidate_concept_cn"]),
                    markdown_table_cell(analysis["strict_reason_cn"]),
                ]
            )
            + " |"
        )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8-sig")
    print(f"Wrote {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN_DIR)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--draft-jsonl", default=DEFAULT_DRAFT_JSONL)
    parser.add_argument("--output-md", default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--batch-size", type=int, default=6)
    parser.add_argument("--model", default="deepseek-v4-pro")
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--skip-api", action="store_true")
    args = parser.parse_args()

    run_dir = args.run_dir
    rows = load_rows(run_dir / args.input)
    jsonl_path = run_dir / args.draft_jsonl
    if not args.skip_api:
        analyze_missing(rows, jsonl_path, args.batch_size, args.model, args.timeout)
    analyses = {int(item["idx"]): item for item in load_existing(jsonl_path).values()}
    write_report(rows, analyses, run_dir / args.output_md)


if __name__ == "__main__":
    main()
