import argparse
import asyncio
import csv
import hashlib
import json
import os
import random
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


DEFAULT_INPUT = "llm_qual_abs_all.csv"
DEFAULT_OUTPUT = "llm_qual_abs_relevant.csv"
DEFAULT_PROGRESS = "llm_qual_abs_relevant.progress.jsonl"
DEFAULT_ERRORS = "llm_qual_abs_relevant.errors.jsonl"
DEFAULT_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-pro"


SYSTEM_PROMPT = """You are a careful literature screening assistant.

Task: judge whether a paper is relevant to "using generative AI to assist qualitative analysis".

Relevant means the title and abstract together indicate that generative AI, LLMs, ChatGPT, GPT-like tools, or other generative AI systems are used, evaluated, proposed, compared, or discussed as tools to assist qualitative analysis work, such as qualitative coding, thematic analysis, content analysis, grounded theory analysis, interview/focus-group/open-ended-response analysis, memoing, data interpretation, or synthesis of qualitative data.

Not relevant if the paper is merely:
- a qualitative study about people's opinions/adoption/use of AI;
- about AI in general clinical/educational/technical practice without qualitative analysis assistance;
- about non-generative AI, machine learning, NLP, or text mining without generative AI assisting qualitative analysis;
- about LLM evaluation, theorem understanding, chatbots, summarization, or automation unrelated to qualitative analysis.

Return only valid json. Use this exact schema:
{
  "relevant": true,
  "confidence": 0.0,
  "reason": "short reason in English or Chinese"
}
"""


@dataclass(frozen=True)
class ScreenItem:
    row_number: int
    row_key: str
    row: dict[str, str]
    title: str
    abstract: str


@dataclass(frozen=True)
class ScreenResult:
    item: ScreenItem
    relevant: bool
    confidence: float
    reason: str
    raw_response: str


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be >= 1")
    return parsed


def non_negative_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be >= 0")
    return parsed


def non_negative_float(value: str) -> float:
    parsed = float(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be >= 0")
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Screen CSV rows for papers about using generative AI to assist "
            "qualitative analysis. Relevant rows are appended to a CSV."
        )
    )
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Input CSV path.")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Relevant-row output CSV path.")
    parser.add_argument(
        "--progress",
        default=DEFAULT_PROGRESS,
        help="JSONL progress file recording completed decisions for resume.",
    )
    parser.add_argument(
        "--errors",
        default=DEFAULT_ERRORS,
        help="JSONL error log for rows that failed after retries.",
    )
    parser.add_argument("--env-file", default=".env", help="Path to .env file.")
    parser.add_argument(
        "--api-key-env",
        default="NEW_API_KEY",
        help="Environment variable containing the DeepSeek API key.",
    )
    parser.add_argument(
        "--base-url-env",
        default="NEW_API_BASE_URL",
        help="Environment variable containing the OpenAI-compatible base URL.",
    )
    parser.add_argument("--base-url", default=None, help="Override API base URL.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model name.")
    parser.add_argument("--title-column", default="Title", help="Title column name.")
    parser.add_argument("--abstract-column", default="Abstract", help="Abstract column name.")
    parser.add_argument(
        "--id-column",
        default="EID",
        help="Stable ID column. Falls back to a hash if missing or empty.",
    )
    parser.add_argument("--encoding", default="utf-8-sig", help="CSV input/output encoding.")
    parser.add_argument("--max-concurrency", type=positive_int, default=4, help="Concurrent API calls.")
    parser.add_argument("--retries", type=non_negative_int, default=3, help="Retries per row.")
    parser.add_argument("--retry-base-delay", type=non_negative_float, default=2.0, help="Initial retry delay.")
    parser.add_argument("--timeout", type=non_negative_float, default=90.0, help="API timeout in seconds.")
    parser.add_argument("--max-tokens", type=positive_int, default=220, help="Max output tokens.")
    parser.add_argument("--limit", type=positive_int, default=None, help="Only process this many pending rows.")
    parser.add_argument("--offset", type=non_negative_int, default=0, help="Skip this many input rows first.")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Delete existing output/progress/error files before running.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Load data and show pending counts without calling the API.",
    )
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def normalize_cell(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("\ufeff", "").strip()


def build_row_key(row: dict[str, str], row_number: int, id_column: str, title: str, abstract: str) -> str:
    explicit_id = normalize_cell(row.get(id_column, ""))
    if explicit_id:
        return explicit_id
    digest = hashlib.sha256(f"{row_number}\n{title}\n{abstract}".encode("utf-8")).hexdigest()[:16]
    return f"row-{row_number}-{digest}"


def load_processed_keys(progress_path: Path, output_path: Path, id_column: str, encoding: str) -> set[str]:
    processed: set[str] = set()
    if progress_path.exists():
        with progress_path.open("r", encoding="utf-8", newline="") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    payload = json.loads(line)
                except json.JSONDecodeError:
                    continue
                row_key = normalize_cell(payload.get("row_key"))
                if row_key:
                    processed.add(row_key)

    if output_path.exists():
        with output_path.open("r", encoding=encoding, newline="") as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader, start=2):
                title = normalize_cell(row.get("Title", ""))
                abstract = normalize_cell(row.get("Abstract", ""))
                row_key = build_row_key(row, index, id_column, title, abstract)
                processed.add(row_key)
    return processed


def load_items(
    input_path: Path,
    title_column: str,
    abstract_column: str,
    id_column: str,
    encoding: str,
    offset: int,
) -> tuple[list[str], list[ScreenItem]]:
    with input_path.open("r", encoding=encoding, newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError(f"{input_path} has no header row")
        missing_columns = [name for name in (title_column, abstract_column) if name not in reader.fieldnames]
        if missing_columns:
            raise ValueError(f"Missing required CSV columns: {', '.join(missing_columns)}")

        items: list[ScreenItem] = []
        for row_number, row in enumerate(reader, start=2):
            if row_number - 2 < offset:
                continue
            clean_row = {key: normalize_cell(value) for key, value in row.items() if key is not None}
            title = normalize_cell(clean_row.get(title_column, ""))
            abstract = normalize_cell(clean_row.get(abstract_column, ""))
            row_key = build_row_key(clean_row, row_number, id_column, title, abstract)
            items.append(ScreenItem(row_number=row_number, row_key=row_key, row=clean_row, title=title, abstract=abstract))
    return list(reader.fieldnames), items


def build_user_prompt(item: ScreenItem) -> str:
    return f"""Please screen this literature record and output json only.

Title:
{item.title or "(empty)"}

Abstract:
{item.abstract or "(empty)"}
"""


def parse_model_json(content: str) -> tuple[bool, float, str]:
    if not content or not content.strip():
        raise ValueError("empty model response")
    payload = json.loads(content)
    if not isinstance(payload, dict):
        raise ValueError("model response is not a JSON object")
    relevant = payload.get("relevant")
    if not isinstance(relevant, bool):
        raise ValueError("JSON field 'relevant' must be boolean")
    confidence_value = payload.get("confidence", 0.0)
    try:
        confidence = float(confidence_value)
    except (TypeError, ValueError):
        confidence = 0.0
    confidence = max(0.0, min(1.0, confidence))
    reason = normalize_cell(payload.get("reason", ""))
    return relevant, confidence, reason


async def classify_with_retries(
    item: ScreenItem,
    llm: Any,
    semaphore: asyncio.Semaphore,
    retries: int,
    retry_base_delay: float,
) -> ScreenResult:
    last_error: BaseException | None = None
    for attempt in range(retries + 1):
        try:
            async with semaphore:
                response = await llm.ainvoke(
                    [
                        ("system", SYSTEM_PROMPT),
                        ("user", build_user_prompt(item)),
                    ]
                )
            raw_response = response.content if isinstance(response.content, str) else json.dumps(response.content)
            relevant, confidence, reason = parse_model_json(raw_response)
            return ScreenResult(
                item=item,
                relevant=relevant,
                confidence=confidence,
                reason=reason,
                raw_response=raw_response,
            )
        except Exception as exc:
            last_error = exc
            if attempt >= retries:
                break
            sleep_seconds = retry_base_delay * (2**attempt) + random.uniform(0, 0.5)
            await asyncio.sleep(sleep_seconds)
    assert last_error is not None
    raise last_error


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8", newline="") as file:
        file.write(json.dumps(payload, ensure_ascii=False) + "\n")
        file.flush()
        os.fsync(file.fileno())


def ensure_output_writer(output_path: Path, fieldnames: list[str], encoding: str) -> tuple[Any, csv.DictWriter]:
    file_exists = output_path.exists() and output_path.stat().st_size > 0
    file = output_path.open("a", encoding=encoding, newline="")
    writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
    if not file_exists:
        writer.writeheader()
        file.flush()
        os.fsync(file.fileno())
    return file, writer


def write_relevant_row(file: Any, writer: csv.DictWriter, row: dict[str, str]) -> None:
    writer.writerow(row)
    file.flush()
    os.fsync(file.fileno())


async def run_screening(args: argparse.Namespace) -> int:
    input_path = Path(args.input)
    output_path = Path(args.output)
    progress_path = Path(args.progress)
    errors_path = Path(args.errors)

    if args.reset:
        for path in (output_path, progress_path, errors_path):
            if path.exists():
                path.unlink()

    load_dotenv(args.env_file)
    api_key = os.getenv(args.api_key_env) or os.getenv("DEEPSEEK_API_KEY")
    base_url = args.base_url or os.getenv(args.base_url_env) or os.getenv("DEEPSEEK_BASE_URL") or DEFAULT_BASE_URL
    if not api_key and not args.dry_run:
        raise RuntimeError(
            f"API key not found. Set {args.api_key_env} in {args.env_file}, "
            "or set DEEPSEEK_API_KEY."
        )

    fieldnames, all_items = load_items(
        input_path=input_path,
        title_column=args.title_column,
        abstract_column=args.abstract_column,
        id_column=args.id_column,
        encoding=args.encoding,
        offset=args.offset,
    )
    processed_keys = load_processed_keys(progress_path, output_path, args.id_column, args.encoding)
    pending_items = [item for item in all_items if item.row_key not in processed_keys]
    if args.limit is not None:
        pending_items = pending_items[: args.limit]

    print(
        f"Loaded {len(all_items)} rows after offset; "
        f"{len(processed_keys)} already processed; {len(pending_items)} pending."
    )
    print(f"Input encoding/output encoding: {args.encoding}")
    print(f"Model: {args.model}; base_url: {base_url}")
    if args.dry_run:
        for item in pending_items[:5]:
            print(f"DRY RUN row={item.row_number} key={item.row_key} title={item.title[:100]}")
        return 0
    if not pending_items:
        print("Nothing to do.")
        return 0

    llm = ChatOpenAI(
        model=args.model,
        api_key=api_key,
        base_url=base_url,
        timeout=args.timeout,
        max_tokens=args.max_tokens,
        temperature=0,
    ).bind(response_format={"type": "json_object"})

    semaphore = asyncio.Semaphore(args.max_concurrency)
    output_file, output_writer = ensure_output_writer(output_path, fieldnames, args.encoding)
    started_at = time.monotonic()
    completed = 0
    relevant_count = 0
    failed_count = 0

    async def classify_one(item: ScreenItem) -> tuple[ScreenItem, ScreenResult | None, BaseException | None]:
        try:
            result = await classify_with_retries(
                item=item,
                llm=llm,
                semaphore=semaphore,
                retries=args.retries,
                retry_base_delay=args.retry_base_delay,
            )
            return item, result, None
        except Exception as exc:
            return item, None, exc

    try:
        tasks = [asyncio.create_task(classify_one(item)) for item in pending_items]
        for finished in asyncio.as_completed(tasks):
            item, result, error = await finished
            completed += 1
            if error is not None:
                failed_count += 1
                append_jsonl(
                    errors_path,
                    {
                        "ts": utc_now(),
                        "row_number": item.row_number,
                        "row_key": item.row_key,
                        "title": item.title,
                        "error_type": type(error).__name__,
                        "error": str(error),
                    },
                )
            elif result is not None:
                if result.relevant:
                    relevant_count += 1
                    write_relevant_row(output_file, output_writer, result.item.row)
                append_jsonl(
                    progress_path,
                    {
                        "ts": utc_now(),
                        "row_number": result.item.row_number,
                        "row_key": result.item.row_key,
                        "relevant": result.relevant,
                        "confidence": result.confidence,
                        "reason": result.reason,
                        "model": args.model,
                    },
                )

            if completed == 1 or completed % 10 == 0 or completed == len(pending_items):
                elapsed = time.monotonic() - started_at
                print(
                    f"Completed {completed}/{len(pending_items)}; "
                    f"relevant={relevant_count}; failed={failed_count}; elapsed={elapsed:.1f}s"
                )
    finally:
        output_file.close()

    print(
        f"Done. Relevant rows appended to {output_path}. "
        f"Progress: {progress_path}. Errors: {errors_path}."
    )
    return 0 if failed_count == 0 else 2


def main() -> None:
    args = parse_args()
    try:
        raise SystemExit(asyncio.run(run_screening(args)))
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        raise SystemExit(130)


if __name__ == "__main__":
    main()
