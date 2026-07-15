from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from deep_translator import GoogleTranslator


HERE = Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "source_en"
DEFAULT_OUTPUT = HERE / "bilingual_zh"
DEFAULT_PROGRESS = HERE / ".progress"
PARAGRAPH_BREAK = re.compile(r"\n[ \t]*\n+")
TRANSLATABLE_TEXT = re.compile(r"[A-Za-z]{2,}")
PRINT_LOCK = threading.Lock()


@dataclass(frozen=True)
class FileResult:
    source: str
    status: str
    paragraphs: int
    translated_paragraphs: int
    output: str
    error: str = ""


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
            "Translate Markdown full texts paragraph by paragraph and write bilingual "
            "Markdown with each English paragraph followed by its Chinese translation."
        )
    )
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--progress-dir", type=Path, default=DEFAULT_PROGRESS)
    parser.add_argument("--source-lang", default="en")
    parser.add_argument("--target-lang", default="zh-CN")
    parser.add_argument("--max-workers", type=positive_int, default=2)
    parser.add_argument("--chunk-size", type=positive_int, default=4200)
    parser.add_argument("--retries", type=positive_int, default=5)
    parser.add_argument("--retry-delay", type=non_negative_float, default=2.0)
    parser.add_argument("--limit-files", type=positive_int, default=None)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def log(message: str, *, error: bool = False) -> None:
    with PRINT_LOCK:
        print(message, file=sys.stderr if error else sys.stdout, flush=True)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_paragraphs(text: str) -> list[str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    return [block.strip() for block in PARAGRAPH_BREAK.split(normalized) if block.strip()]


def split_long_text(text: str, chunk_size: int) -> list[str]:
    if len(text) <= chunk_size:
        return [text]
    chunks: list[str] = []
    remaining = text
    while len(remaining) > chunk_size:
        window = remaining[:chunk_size]
        candidates = [
            window.rfind(". "),
            window.rfind("; "),
            window.rfind("\n"),
            window.rfind(" "),
        ]
        cut = max(candidates)
        if cut < chunk_size // 2:
            cut = chunk_size
        elif window[cut : cut + 2] in {". ", "; "}:
            cut += 1
        piece = remaining[:cut].strip()
        if piece:
            chunks.append(piece)
        remaining = remaining[cut:].strip()
    if remaining:
        chunks.append(remaining)
    return chunks


def translate_chunk(
    translator: GoogleTranslator,
    text: str,
    retries: int,
    retry_delay: float,
) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            translated = translator.translate(text)
            if not translated or not translated.strip():
                raise ValueError("empty translation response")
            return translated.strip()
        except Exception as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(retry_delay * attempt)
    assert last_error is not None
    raise last_error


def translate_paragraph(paragraph: str, args: argparse.Namespace) -> str:
    if not TRANSLATABLE_TEXT.search(paragraph):
        return "（代码、公式、图片引用或其他非语言内容，无需翻译。）"
    translator = GoogleTranslator(source=args.source_lang, target=args.target_lang)
    chunks = split_long_text(paragraph, args.chunk_size)
    return "\n".join(
        translate_chunk(translator, chunk, args.retries, args.retry_delay)
        for chunk in chunks
    )


def read_checkpoint(path: Path, source_hash: str, paragraph_count: int) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if payload.get("source_sha256") != source_hash:
        return {}
    if payload.get("paragraph_count") != paragraph_count:
        return {}
    translations = payload.get("translations", {})
    if not isinstance(translations, dict):
        return {}
    return {str(key): str(value) for key, value in translations.items()}


def write_json_atomic(path: Path, payload: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def save_checkpoint(
    path: Path,
    source_hash: str,
    paragraph_count: int,
    translations: dict[str, str],
) -> None:
    write_json_atomic(
        path,
        {
            "source_sha256": source_hash,
            "paragraph_count": paragraph_count,
            "completed_paragraphs": len(translations),
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "translations": translations,
        },
    )


def render_bilingual(source_name: str, paragraphs: list[str], translations: dict[str, str]) -> str:
    output: list[str] = []
    for index, paragraph in enumerate(paragraphs):
        output.append(paragraph + "\n\n" + translations[str(index)])
    return "\n\n".join(output).rstrip() + "\n"


def translate_file(source_path: Path, args: argparse.Namespace) -> FileResult:
    output_path = args.output_dir / source_path.name
    checkpoint_path = args.progress_dir / (source_path.name + ".json")
    text = source_path.read_text(encoding="utf-8", errors="replace")
    paragraphs = split_paragraphs(text)
    source_hash = sha256_text(text)

    if output_path.exists() and not args.force:
        return FileResult(source_path.name, "skipped", len(paragraphs), 0, str(output_path))

    translations = {} if args.force else read_checkpoint(
        checkpoint_path, source_hash, len(paragraphs)
    )
    translated_now = 0
    for index, paragraph in enumerate(paragraphs):
        key = str(index)
        if key in translations:
            continue
        translations[key] = translate_paragraph(paragraph, args)
        translated_now += 1
        save_checkpoint(checkpoint_path, source_hash, len(paragraphs), translations)
        if translated_now == 1 or translated_now % 20 == 0:
            log(
                "[paragraph] " + source_path.name + " "
                + str(len(translations)) + "/" + str(len(paragraphs))
            )

    output_path.write_text(
        render_bilingual(source_path.name, paragraphs, translations),
        encoding="utf-8",
    )
    return FileResult(
        source_path.name,
        "completed",
        len(paragraphs),
        translated_now,
        str(output_path),
    )


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.progress_dir.mkdir(parents=True, exist_ok=True)
    sources = sorted(args.input_dir.glob("*.md"))
    if args.limit_files is not None:
        sources = sources[: args.limit_files]
    if not sources:
        raise SystemExit("No Markdown files found in " + str(args.input_dir))

    log("Files selected: " + str(len(sources)))
    results: list[FileResult] = []
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = {executor.submit(translate_file, path, args): path for path in sources}
        for future in as_completed(futures):
            source = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                log("[ERROR] " + source.name + ": " + repr(exc), error=True)
                results.append(FileResult(source.name, "failed", 0, 0, "", repr(exc)))
                continue
            results.append(result)
            log("[" + result.status.upper() + "] " + result.source)

    results.sort(key=lambda item: item.source)
    available_outputs = sum(
        (args.output_dir / source.name).exists() for source in sources
    )
    summary = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "selected": len(sources),
        "available_outputs": available_outputs,
        "pending_outputs": len(sources) - available_outputs,
        "all_outputs_complete": available_outputs == len(sources),
        "completed_this_run": sum(item.status == "completed" for item in results),
        "skipped_this_run": sum(item.status == "skipped" for item in results),
        "failed_this_run": sum(item.status == "failed" for item in results),
        "results": [item.__dict__ for item in results],
    }
    write_json_atomic(HERE / "translation_summary.json", summary)
    log(
        "Finished: available_outputs=" + str(summary["available_outputs"])
        + " pending_outputs=" + str(summary["pending_outputs"])
        + " completed_this_run=" + str(summary["completed_this_run"])
        + " skipped_this_run=" + str(summary["skipped_this_run"])
        + " failed_this_run=" + str(summary["failed_this_run"])
    )
    if summary["failed_this_run"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
