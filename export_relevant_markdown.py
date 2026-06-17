import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_INPUT = "game_ais_abs_relevant_zh.csv"
DEFAULT_ZH_OUTPUT = "game_ais_abs_relevant_zh.md"
DEFAULT_EN_OUTPUT = "game_ais_abs_relevant_en.md"


@dataclass(frozen=True)
class Paper:
    original_index: int
    authors: str
    source_title: str
    year: str
    title_en: str
    abstract_en: str
    title_zh: str
    abstract_zh: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Export screened and translated literature records to Chinese and English "
            "Markdown files, sorted by year descending."
        )
    )
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Translated CSV path.")
    parser.add_argument("--zh-output", default=DEFAULT_ZH_OUTPUT, help="Chinese Markdown output path.")
    parser.add_argument("--en-output", default=DEFAULT_EN_OUTPUT, help="English Markdown output path.")
    parser.add_argument("--encoding", default="utf-8-sig", help="CSV and Markdown encoding.")
    parser.add_argument("--authors-column", default="Authors", help="Authors column name.")
    parser.add_argument("--journal-column", default="Source title", help="Journal/source title column name.")
    parser.add_argument("--year-column", default="Year", help="Year column name.")
    parser.add_argument("--title-column", default="Title", help="English title column name.")
    parser.add_argument("--abstract-column", default="Abstract", help="English abstract column name.")
    parser.add_argument("--zh-column", default="zh", help="Chinese translation column name.")
    return parser.parse_args()


def normalize_cell(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("\ufeff", "").strip()


def normalize_paragraph(value: str) -> str:
    lines = [line.strip() for line in normalize_cell(value).splitlines()]
    return "\n".join(line for line in lines if line)


def parse_year(value: str) -> int:
    match = re.search(r"\d{4}", value)
    if not match:
        return -1
    return int(match.group(0))


def split_zh_translation(text: str) -> tuple[str, str]:
    cleaned = normalize_paragraph(text)
    if not cleaned:
        return "", ""

    title_match = re.search(
        r"^\s*(?:标题|题目)\s*[:：]\s*(.*?)(?=\n\s*摘要\s*[:：]|\Z)",
        cleaned,
        flags=re.DOTALL,
    )
    abstract_match = re.search(r"\n?\s*摘要\s*[:：]\s*(.*)\Z", cleaned, flags=re.DOTALL)

    title = title_match.group(1).strip() if title_match else ""
    abstract = abstract_match.group(1).strip() if abstract_match else ""
    if title or abstract:
        return normalize_paragraph(title), normalize_paragraph(abstract)

    lines = cleaned.splitlines()
    title = lines[0] if lines else ""
    abstract = "\n".join(lines[1:]) if len(lines) > 1 else ""
    return normalize_paragraph(title), normalize_paragraph(abstract)


def require_columns(fieldnames: list[str], required: list[str]) -> None:
    missing = [column for column in required if column not in fieldnames]
    if missing:
        raise ValueError(f"Missing required CSV columns: {', '.join(missing)}")


def load_papers(args: argparse.Namespace) -> list[Paper]:
    input_path = Path(args.input)
    with input_path.open("r", encoding=args.encoding, newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError(f"{input_path} has no header row")

        require_columns(
            list(reader.fieldnames),
            [
                args.authors_column,
                args.journal_column,
                args.year_column,
                args.title_column,
                args.abstract_column,
                args.zh_column,
            ],
        )

        papers: list[Paper] = []
        for index, row in enumerate(reader):
            title_en = normalize_cell(row.get(args.title_column))
            abstract_en = normalize_paragraph(row.get(args.abstract_column, ""))
            title_zh, abstract_zh = split_zh_translation(normalize_cell(row.get(args.zh_column)))
            papers.append(
                Paper(
                    original_index=index,
                    authors=normalize_cell(row.get(args.authors_column)),
                    source_title=normalize_cell(row.get(args.journal_column)),
                    year=normalize_cell(row.get(args.year_column)),
                    title_en=title_en,
                    abstract_en=abstract_en,
                    title_zh=title_zh or title_en,
                    abstract_zh=abstract_zh or abstract_en,
                )
            )
    return sorted(papers, key=lambda paper: (-parse_year(paper.year), paper.original_index))


def render_zh(papers: list[Paper]) -> str:
    lines = ["# 筛选后游戏相关文献（中文）", ""]
    for index, paper in enumerate(papers, start=1):
        lines.extend(
            [
                f"## {index}. {paper.title_zh}",
                "",
                f"**作者**：{paper.authors or '未知'}",
                "",
                f"**期刊**：{paper.source_title or '未知'}",
                "",
                f"**年份**：{paper.year or '未知'}",
                "",
                f"**摘要**：{paper.abstract_zh or '无摘要'}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_en(papers: list[Paper]) -> str:
    lines = ["# Screened Game-Related Literature (English)", ""]
    for index, paper in enumerate(papers, start=1):
        lines.extend(
            [
                f"## {index}. {paper.title_en or 'Untitled'}",
                "",
                f"**Authors**: {paper.authors or 'Unknown'}",
                "",
                f"**Journal**: {paper.source_title or 'Unknown'}",
                "",
                f"**Year**: {paper.year or 'Unknown'}",
                "",
                f"**Abstract**: {paper.abstract_en or 'No abstract'}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_text(path: Path, text: str, encoding: str) -> None:
    path.write_text(text, encoding=encoding, newline="\n")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    papers = load_papers(args)
    write_text(Path(args.zh_output), render_zh(papers), args.encoding)
    write_text(Path(args.en_output), render_en(papers), args.encoding)
    print(f"Wrote {len(papers)} papers to {args.zh_output} and {args.en_output}.")


if __name__ == "__main__":
    main()
