import argparse
import csv
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from deep_translator import GoogleTranslator


DEFAULT_INPUT = "game_ais_abs_relevant.csv"
DEFAULT_ZH_COLUMN = "zh"


@dataclass(frozen=True)
class TranslationItem:
    index: int
    row_number: int
    title: str
    abstract: str
    text: str


@dataclass(frozen=True)
class TranslationResult:
    item: TranslationItem
    translated_text: str


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be >= 1")
    return parsed


def non_negative_float(value: str) -> float:
    parsed = float(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be >= 0")
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Translate the Title + Abstract text in a CSV file into Chinese "
            "with Google Translate, add a zh column, and write a *_zh.csv file."
        )
    )
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Input CSV path.")
    parser.add_argument(
        "--output",
        default=None,
        help="Output CSV path. Defaults to input file name with _zh before the suffix.",
    )
    parser.add_argument("--title-column", default="Title", help="Title column name.")
    parser.add_argument("--abstract-column", default="Abstract", help="Abstract column name.")
    parser.add_argument("--zh-column", default=DEFAULT_ZH_COLUMN, help="Output translation column name.")
    parser.add_argument("--encoding", default="utf-8-sig", help="Input/output CSV encoding.")
    parser.add_argument("--source-lang", default="auto", help="Source language code.")
    parser.add_argument("--target-lang", default="zh-CN", help="Target language code.")
    parser.add_argument("--max-workers", type=positive_int, default=4, help="Concurrent row-level translation workers.")
    parser.add_argument(
        "--chunk-size",
        type=positive_int,
        default=4500,
        help="Max characters per translation chunk. Keep below GoogleTranslator's 5000-character limit.",
    )
    parser.add_argument("--retries", type=positive_int, default=3, help="Attempts per translation chunk.")
    parser.add_argument(
        "--retry-delay",
        type=non_negative_float,
        default=1.5,
        help="Base delay between retries in seconds.",
    )
    parser.add_argument("--limit", type=positive_int, default=None, help="Only translate the first N rows.")
    return parser.parse_args()


def default_output_path(input_path: Path) -> Path:
    if input_path.suffix:
        return input_path.with_name(f"{input_path.stem}_zh{input_path.suffix}")
    return input_path.with_name(f"{input_path.name}_zh.csv")


def normalize_cell(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("\ufeff", "").strip()


def split_text(text: str, chunk_size: int) -> list[str]:
    text = text.strip()
    if len(text) <= chunk_size:
        return [text] if text else []

    chunks: list[str] = []
    current = ""
    paragraphs = text.splitlines()
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if len(paragraph) > chunk_size:
            if current:
                chunks.append(current.strip())
                current = ""
            for start in range(0, len(paragraph), chunk_size):
                chunks.append(paragraph[start : start + chunk_size].strip())
            continue
        candidate = f"{current}\n{paragraph}".strip() if current else paragraph
        if len(candidate) > chunk_size:
            chunks.append(current.strip())
            current = paragraph
        else:
            current = candidate
    if current:
        chunks.append(current.strip())
    return chunks


def translate_chunk(
    translator: GoogleTranslator,
    text: str,
    retries: int,
    retry_delay: float,
) -> str:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            translated = translator.translate(text)
            if not translated:
                raise ValueError("empty Google Translate response")
            return translated
        except Exception as exc:
            last_error = exc
            if attempt + 1 >= retries:
                break
            time.sleep(retry_delay * (attempt + 1))
    assert last_error is not None
    raise last_error


def translate_text(
    text: str,
    source_lang: str,
    target_lang: str,
    chunk_size: int,
    retries: int,
    retry_delay: float,
) -> str:
    chunks = split_text(text, chunk_size)
    if not chunks:
        return ""
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translated_chunks = [
        translate_chunk(
            translator=translator,
            text=chunk,
            retries=retries,
            retry_delay=retry_delay,
        )
        for chunk in chunks
    ]
    return "\n".join(translated_chunks)


def load_items(
    input_path: Path,
    title_column: str,
    abstract_column: str,
    encoding: str,
    limit: int | None,
) -> tuple[list[str], list[dict[str, str]], list[TranslationItem]]:
    with input_path.open("r", encoding=encoding, newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError(f"{input_path} has no header row")
        missing = [column for column in (title_column, abstract_column) if column not in reader.fieldnames]
        if missing:
            raise ValueError(f"Missing required CSV columns: {', '.join(missing)}")

        rows: list[dict[str, str]] = []
        items: list[TranslationItem] = []
        for index, row in enumerate(reader):
            if limit is not None and index >= limit:
                break
            clean_row = {key: normalize_cell(value) for key, value in row.items() if key is not None}
            title = normalize_cell(clean_row.get(title_column, ""))
            abstract = normalize_cell(clean_row.get(abstract_column, ""))
            text = f"Title: {title}\nAbstract: {abstract}".strip()
            rows.append(clean_row)
            items.append(
                TranslationItem(
                    index=index,
                    row_number=index + 2,
                    title=title,
                    abstract=abstract,
                    text=text,
                )
            )
    return list(reader.fieldnames), rows, items


def translate_item(item: TranslationItem, args: argparse.Namespace) -> TranslationResult:
    translated = translate_text(
        text=item.text,
        source_lang=args.source_lang,
        target_lang=args.target_lang,
        chunk_size=args.chunk_size,
        retries=args.retries,
        retry_delay=args.retry_delay,
    )
    return TranslationResult(item=item, translated_text=translated)


def write_output(output_path: Path, fieldnames: list[str], rows: list[dict[str, str]], zh_column: str, encoding: str) -> None:
    output_fieldnames = list(fieldnames)
    if zh_column not in output_fieldnames:
        output_fieldnames.append(zh_column)
    with output_path.open("w", encoding=encoding, newline="") as file:
        writer = csv.DictWriter(file, fieldnames=output_fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else default_output_path(input_path)

    fieldnames, rows, items = load_items(
        input_path=input_path,
        title_column=args.title_column,
        abstract_column=args.abstract_column,
        encoding=args.encoding,
        limit=args.limit,
    )
    if not items:
        write_output(output_path, fieldnames, rows, args.zh_column, args.encoding)
        print(f"No rows to translate. Wrote {output_path}.")
        return

    print(f"Loaded {len(items)} rows from {input_path}.")
    print(f"Translating Title + Abstract to {args.target_lang}; output: {output_path}")

    results: dict[int, str] = {}
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        future_map = {executor.submit(translate_item, item, args): item for item in items}
        for future in as_completed(future_map):
            item = future_map[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"[ERROR] row={item.row_number} title={item.title[:80]} error={exc}", file=sys.stderr)
                raise
            results[result.item.index] = result.translated_text
            print(f"\n[row {result.item.row_number}] {result.item.title}")
            print(result.translated_text)
            sys.stdout.flush()

    for index, row in enumerate(rows):
        row[args.zh_column] = results.get(index, "")
    write_output(output_path, fieldnames, rows, args.zh_column, args.encoding)
    print(f"\nDone. Wrote {len(rows)} rows to {output_path}.")


if __name__ == "__main__":
    main()
