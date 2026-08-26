#!/usr/bin/env python3
"""Download all Otero article full text matching a database query."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import math
import os
import random
import re
import shutil
import sys
import threading
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://ais.kexu.win/api/open/v1"
USER_AGENT = "otero-open-api-skill/1.0 (+https://ais.kexu.win/docs)"
PRINT_LOCK = threading.Lock()


class RequestFailure(RuntimeError):
    def __init__(self, url: str, status: int | None, message: str):
        super().__init__(message)
        self.url = url
        self.status = status


def log(message: str) -> None:
    with PRINT_LOCK:
        print(message, flush=True)


def get_json(url: str, *, timeout: float, retries: int) -> dict[str, Any]:
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        request = urllib.request.Request(
            url,
            headers={"Accept": "application/json", "User-Agent": USER_AGENT},
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return json.loads(response.read().decode(charset))
        except urllib.error.HTTPError as exc:
            body = exc.read(500).decode("utf-8", errors="replace")
            last_error = RequestFailure(url, exc.code, body or str(exc))
            if exc.code not in {408, 425, 429, 500, 502, 503, 504}:
                raise last_error
            retry_after = exc.headers.get("Retry-After")
            delay = float(retry_after) if retry_after and retry_after.isdigit() else 1.5 * (2**attempt)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = RequestFailure(url, None, str(exc))
            delay = 1.5 * (2**attempt)

        if attempt < retries:
            time.sleep(delay + random.random() * 0.5)

    assert last_error is not None
    raise last_error


def make_url(path: str, params: dict[str, Any]) -> str:
    clean = {key: value for key, value in params.items() if value is not None}
    return f"{BASE_URL}{path}?{urllib.parse.urlencode(clean)}"


def fetch_search_page(
    query: str,
    page: int,
    page_size: int,
    timeout: float,
    retries: int,
    journal: str | None = None,
) -> dict[str, Any]:
    return get_json(
        make_url(
            "/articles",
            {"q": query, "journal": journal, "page": page, "pageSize": page_size},
        ),
        timeout=timeout,
        retries=retries,
    )


def harvest_metadata(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int]:
    first = fetch_search_page(args.query, 1, args.page_size, args.timeout, args.retries)
    total = int(first.get("total", 0))
    total_pages = int(first.get("totalPages", 0))
    target_count = total if args.limit is None else min(total, args.limit)
    pages_needed = math.ceil(target_count / args.page_size) if target_count else 0
    log(f"Search reports {total} matches across {total_pages} pages.")

    if args.limit is not None:
        log(f"Test limit active: harvesting {target_count} records from {pages_needed} page(s).")
        pages: dict[int, list[dict[str, Any]]] = {1: first.get("items", [])}
        if pages_needed > 1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.metadata_workers) as pool:
                future_to_page = {
                    pool.submit(
                        fetch_search_page,
                        args.query,
                        page,
                        args.page_size,
                        args.timeout,
                        args.retries,
                    ): page
                    for page in range(2, pages_needed + 1)
                }
                completed = 1
                for future in concurrent.futures.as_completed(future_to_page):
                    page = future_to_page[future]
                    pages[page] = future.result().get("items", [])
                    completed += 1
                    if completed % 10 == 0 or completed == pages_needed:
                        log(f"Metadata pages: {completed}/{pages_needed}")
        items = [item for page in sorted(pages) for item in pages[page]][:target_count]
    else:
        journals_payload = get_json(
            f"{BASE_URL}/journals", timeout=args.timeout, retries=args.retries
        )
        journals = [str(row["name"]) for row in journals_payload.get("journals", [])]
        if not journals:
            raise RuntimeError("The journal list is empty; cannot partition the full search")

        partitions: dict[tuple[str, int], list[dict[str, Any]]] = {}
        journal_pages: dict[str, int] = {}
        journal_totals: dict[str, int] = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.metadata_workers) as pool:
            first_futures = {
                pool.submit(
                    fetch_search_page,
                    args.query,
                    1,
                    args.page_size,
                    args.timeout,
                    args.retries,
                    journal,
                ): journal
                for journal in journals
            }
            for future in concurrent.futures.as_completed(first_futures):
                journal = first_futures[future]
                payload = future.result()
                partitions[(journal, 1)] = payload.get("items", [])
                journal_pages[journal] = int(payload.get("totalPages", 0))
                journal_totals[journal] = int(payload.get("total", 0))

        partition_total = sum(journal_totals.values())
        if partition_total != total:
            raise RuntimeError(
                f"Journal partition total differs from global search: partitions={partition_total}, global={total}"
            )
        partition_pages = sum(journal_pages.values())
        log(f"Journal partitions match the global total; harvesting {partition_pages} filtered pages.")

        remaining = [
            (journal, page)
            for journal in journals
            for page in range(2, journal_pages[journal] + 1)
        ]
        completed = len(journals)
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.metadata_workers) as pool:
            page_futures = {
                pool.submit(
                    fetch_search_page,
                    args.query,
                    page,
                    args.page_size,
                    args.timeout,
                    args.retries,
                    journal,
                ): (journal, page)
                for journal, page in remaining
            }
            for future in concurrent.futures.as_completed(page_futures):
                key = page_futures[future]
                partitions[key] = future.result().get("items", [])
                completed += 1
                if completed % 10 == 0 or completed == partition_pages:
                    log(f"Filtered metadata pages: {completed}/{partition_pages}")

        items = [
            item
            for journal in journals
            for page in range(1, journal_pages[journal] + 1)
            for item in partitions[(journal, page)]
        ]

    unique = {int(item["id"]): item for item in items}
    if len(items) != target_count or len(unique) != target_count:
        raise RuntimeError(
            f"Incomplete or duplicate search harvest: expected={target_count}, records={len(items)}, unique={len(unique)}"
        )
    return list(unique.values()), total


def write_jsonl_atomic(path: Path, records: list[dict[str, Any]]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    os.replace(temp, path)


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temp, path)


def load_results(path: Path) -> dict[int, dict[str, Any]]:
    results: dict[int, dict[str, Any]] = {}
    if not path.exists():
        return results
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                record = json.loads(line)
                results[int(record["id"])] = record
    return results


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def slugify(value: str, max_length: int = 96) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", ascii_text).strip("-").lower()
    return (slug or "untitled")[:max_length].rstrip("-")


def output_filename(item: dict[str, Any]) -> str:
    fields = item.get("fields") or {}
    year_match = re.search(r"\d{4}", str(fields.get("date") or ""))
    year = year_match.group(0) if year_match else "unknown"
    title = str(fields.get("title") or "Untitled")
    return f"{int(item['id']):05d}_{year}_{slugify(title)}.md"


def markdown_otero_id(path: Path) -> int | None:
    """Read an Otero ID from the small YAML frontmatter at the top of a Markdown file."""
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line_number, line in enumerate(handle, start=1):
                match = re.fullmatch(r"otero_id:\s*(\d+)\s*", line)
                if match:
                    return int(match.group(1))
                if line_number >= 32:
                    break
    except OSError:
        return None
    return None


def index_markdown(directory: Path) -> dict[int, Path]:
    """Index previously downloaded Otero Markdown files by article ID."""
    index: dict[int, Path] = {}
    if not directory.is_dir():
        return index
    for path in sorted(directory.glob("*.md")):
        item_id = markdown_otero_id(path)
        if item_id is not None:
            index.setdefault(item_id, path)
    return index


def reusable_download_record(
    item: dict[str, Any], destination: Path, source: Path, reuse_mode: str
) -> dict[str, Any]:
    fields = item.get("fields") or {}
    doi = str(fields.get("DOI") or "").strip()
    return {
        "id": int(item["id"]),
        "key": item.get("key"),
        "title": fields.get("title"),
        "doi": doi or None,
        "status": "downloaded",
        "file": destination.name,
        "bytes": destination.stat().st_size,
        "fulltext_state": "reused",
        "reuse_mode": reuse_mode,
        "reused_from": str(source),
    }


def seed_reused_fulltexts(
    items: list[dict[str, Any]],
    output: Path,
    reuse_directories: list[Path],
    results: dict[int, dict[str, Any]],
) -> dict[str, int]:
    """Recognize files already in output and hard-link/copy files from older libraries."""
    output_index = index_markdown(output)
    source_indexes = [(directory, index_markdown(directory)) for directory in reuse_directories]
    stats = {
        "existing_output": 0,
        "hardlinked": 0,
        "copied": 0,
        "conflicts": 0,
        "seeded_records": 0,
    }

    for item in items:
        item_id = int(item["id"])
        previous = results.get(item_id)
        if previous and previous.get("status") == "downloaded":
            file_value = previous.get("file")
            if file_value and (output / str(file_value)).is_file():
                continue

        source = output_index.get(item_id)
        source_directory: Path | None = output if source is not None else None
        if source is None:
            for directory, source_index in source_indexes:
                source = source_index.get(item_id)
                if source is not None:
                    source_directory = directory
                    break
        if source is None or source_directory is None:
            continue

        if source_directory == output:
            destination = source
            reuse_mode = "existing_output"
        else:
            destination = output / output_filename(item)
            if destination.exists():
                if markdown_otero_id(destination) != item_id:
                    stats["conflicts"] += 1
                    log(
                        f"Reuse conflict for Otero ID {item_id}: destination already belongs to "
                        f"another record: {destination}"
                    )
                    continue
                reuse_mode = "existing_output"
            else:
                try:
                    os.link(source, destination)
                    reuse_mode = "hardlink"
                except OSError:
                    shutil.copy2(source, destination)
                    reuse_mode = "copy"

        results[item_id] = reusable_download_record(item, destination, source, reuse_mode)
        output_index[item_id] = destination
        stats_key = {"existing_output": "existing_output", "hardlink": "hardlinked", "copy": "copied"}[
            reuse_mode
        ]
        stats[stats_key] += 1
        stats["seeded_records"] += 1

    return stats


def yaml_scalar(value: Any) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def render_markdown(item: dict[str, Any], payload: dict[str, Any], query: str) -> str:
    fields = item.get("fields") or {}
    creators = item.get("creators") or []
    authors = "; ".join(
        " ".join(filter(None, [str(c.get("firstName") or ""), str(c.get("lastName") or "")])).strip()
        for c in creators
        if c.get("creatorType") == "author"
    )
    frontmatter = [
        "---",
        f"otero_id: {int(item['id'])}",
        f"otero_key: {yaml_scalar(item.get('key'))}",
        f"title: {yaml_scalar(fields.get('title'))}",
        f"authors: {yaml_scalar(authors)}",
        f"year: {yaml_scalar(fields.get('date'))}",
        f"journal: {yaml_scalar(fields.get('publicationTitle'))}",
        f"doi: {yaml_scalar(fields.get('DOI'))}",
        f"query: {yaml_scalar(query)}",
        "source: \"https://ais.kexu.win\"",
        "images_downloaded: false",
        "---",
        "",
    ]
    markdown = str(payload.get("markdown") or "").replace("\r\n", "\n").strip()
    return "\n".join(frontmatter) + markdown + "\n"


def fetch_one(item: dict[str, Any], args: argparse.Namespace, output: Path) -> dict[str, Any]:
    item_id = int(item["id"])
    fields = item.get("fields") or {}
    doi = str(fields.get("DOI") or "").strip()
    base_record = {
        "id": item_id,
        "key": item.get("key"),
        "title": fields.get("title"),
        "doi": doi or None,
    }
    if not doi:
        return {**base_record, "status": "missing_doi"}

    url = make_url("/items/by-doi/markdown", {"doi": doi})
    try:
        payload = get_json(url, timeout=args.timeout, retries=args.retries)
    except RequestFailure as exc:
        status = "unavailable" if exc.status == 404 else "failed"
        return {**base_record, "status": status, "http_status": exc.status, "error": str(exc)}

    markdown = payload.get("markdown")
    if payload.get("state") != "done" or not isinstance(markdown, str) or not markdown.strip():
        return {
            **base_record,
            "status": "unavailable",
            "fulltext_state": payload.get("state"),
            "error": "Markdown is not in done state or is empty",
        }

    filename = output_filename(item)
    destination = output / filename
    temp = destination.with_suffix(destination.suffix + ".tmp")
    temp.write_text(render_markdown(item, payload, args.query), encoding="utf-8", newline="\n")
    os.replace(temp, destination)
    return {
        **base_record,
        "status": "downloaded",
        "file": filename,
        "bytes": destination.stat().st_size,
        "fulltext_state": payload.get("state"),
    }


def summarize(query: str, total: int, metadata_count: int, results: dict[int, dict[str, Any]]) -> dict[str, Any]:
    counts = {"downloaded": 0, "missing_doi": 0, "unavailable": 0, "failed": 0}
    total_bytes = 0
    for record in results.values():
        status = record.get("status")
        if status in counts:
            counts[status] += 1
        total_bytes += int(record.get("bytes") or 0)
    return {
        "query": query,
        "search_total": total,
        "metadata_records": metadata_count,
        "result_records": len(results),
        **counts,
        "downloaded_bytes": total_bytes,
        "complete": total == metadata_count == len(results) == sum(counts.values()),
        "images_downloaded": False,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--query", help="Otero article search query")
    scope.add_argument(
        "--all",
        action="store_true",
        help="Download the complete Otero article corpus without a query filter",
    )
    parser.add_argument("--output", required=True, type=Path, help="Output directory")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent requests (default: 8)")
    parser.add_argument(
        "--metadata-workers",
        type=int,
        default=4,
        help="Concurrent filtered search requests (default: 4)",
    )
    parser.add_argument("--page-size", type=int, default=100, choices=range(1, 101), metavar="1..100")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--limit", type=int, help="Download only the first N records; for testing")
    parser.add_argument(
        "--reuse-metadata",
        action="store_true",
        help="Reuse output/metadata.jsonl after verifying the saved query",
    )
    parser.add_argument(
        "--reuse-from",
        action="append",
        default=[],
        type=Path,
        metavar="DIRECTORY",
        help=(
            "Reuse Markdown from an existing Otero library by article ID; may be repeated. "
            "Hard links are used when possible, with copying as a fallback."
        ),
    )
    parser.add_argument("--checkpoint-every", type=int, default=25)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 32:
        parser.error("--workers must be between 1 and 32")
    if args.metadata_workers < 1 or args.metadata_workers > 8:
        parser.error("--metadata-workers must be between 1 and 8")
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    if args.all:
        args.query = ""
    return args


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    metadata_path = output / "metadata.jsonl"
    results_path = output / "results.jsonl"
    summary_path = output / "summary.json"

    if args.reuse_metadata:
        if not metadata_path.is_file() or not summary_path.is_file():
            raise RuntimeError("--reuse-metadata requires existing metadata.jsonl and summary.json")
        saved_summary = json.loads(summary_path.read_text(encoding="utf-8"))
        if saved_summary.get("query") != args.query:
            raise RuntimeError(
                f"Saved query {saved_summary.get('query')!r} differs from requested query {args.query!r}"
            )
        items = load_jsonl(metadata_path)
        total = int(saved_summary.get("search_total", len(items)))
        if len(items) != int(saved_summary.get("metadata_records", -1)):
            raise RuntimeError("metadata.jsonl count differs from the saved summary")
        log(f"Reusing {len(items)} saved metadata records for query {args.query!r}.")
    else:
        items, total = harvest_metadata(args)
        write_jsonl_atomic(metadata_path, items)
    selected = items[: args.limit] if args.limit is not None else items
    selected_ids = {int(item["id"]) for item in selected}
    results = {item_id: record for item_id, record in load_results(results_path).items() if item_id in selected_ids}

    reuse_directories = [path.resolve() for path in args.reuse_from]
    missing_reuse_directories = [path for path in reuse_directories if not path.is_dir()]
    if missing_reuse_directories:
        missing = ", ".join(str(path) for path in missing_reuse_directories)
        raise RuntimeError(f"--reuse-from directory does not exist: {missing}")
    reuse_stats = seed_reused_fulltexts(selected, output, reuse_directories, results)
    if reuse_stats["seeded_records"]:
        ordered = [results[item_id] for item_id in sorted(results)]
        write_jsonl_atomic(results_path, ordered)
        write_json_atomic(summary_path, summarize(args.query, total, len(items), results))
    log(
        "Reuse scan: "
        f"recognized_in_output={reuse_stats['existing_output']} "
        f"hardlinked={reuse_stats['hardlinked']} copied={reuse_stats['copied']} "
        f"conflicts={reuse_stats['conflicts']}"
    )

    pending: list[dict[str, Any]] = []
    for item in selected:
        item_id = int(item["id"])
        previous = results.get(item_id)
        if previous and previous.get("status") == "downloaded":
            file_value = previous.get("file")
            if file_value and (output / str(file_value)).is_file():
                continue
        pending.append(item)

    log(f"Full text pending: {len(pending)}; already downloaded: {len(selected) - len(pending)}")
    completed_now = 0
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(fetch_one, item, args, output): int(item["id"]) for item in pending}
            for future in concurrent.futures.as_completed(futures):
                record = future.result()
                results[int(record["id"])] = record
                completed_now += 1
                if completed_now % args.checkpoint_every == 0 or completed_now == len(pending):
                    ordered = [results[item_id] for item_id in sorted(results)]
                    write_jsonl_atomic(results_path, ordered)
                    current = summarize(args.query, total, len(items), results)
                    write_json_atomic(summary_path, current)
                    log(
                        f"Full text: {completed_now}/{len(pending)} this run; "
                        f"downloaded={current['downloaded']} unavailable={current['unavailable']} "
                        f"missing_doi={current['missing_doi']} failed={current['failed']}"
                    )
    except KeyboardInterrupt:
        log("Interrupted; writing checkpoint before exit.")
        ordered = [results[item_id] for item_id in sorted(results)]
        write_jsonl_atomic(results_path, ordered)
        write_json_atomic(summary_path, summarize(args.query, total, len(items), results))
        return 130

    ordered = [results[item_id] for item_id in sorted(results)]
    write_jsonl_atomic(results_path, ordered)
    summary = summarize(args.query, total, len(items), results)
    write_json_atomic(summary_path, summary)
    log(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if (args.limit is not None or summary["complete"]) else 2


if __name__ == "__main__":
    sys.exit(main())
