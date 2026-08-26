"""Verify complete Git snapshots for the ARB semantic reserve.

The verifier reads only the query-only reserve manifest and local bare Git
object stores.  It never opens ARB gold/qrel files.  Every tree blob receives a
Git object id and an independent SHA-256 digest; Python blobs are parsed from
their complete bytes with the standard-library AST.  The output is a source
lock, not a retrieval score and not permission to train a model.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import subprocess
import time
import tokenize
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Mapping


READY_STATUS = "READY_FOR_SEMANTIC_INDEX_BUILD"
NO_RUN_STATUS = "NO_RUN_SOURCE_READINESS_FAILED"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _git(repo_dir: Path, *arguments: str) -> bytes:
    completed = subprocess.run(
        ["git", "-c", f"safe.directory={repo_dir.resolve()}", "-C", str(repo_dir), *arguments],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(arguments)} failed in {repo_dir.name}: {message}")
    return completed.stdout


def _repo_store(asset_root: Path, repo: str) -> Path:
    return asset_root / repo.replace("/", "__")


def _tree_entries(repo_dir: Path, commit: str) -> list[dict[str, object]]:
    raw = _git(repo_dir, "ls-tree", "-r", "-l", "-z", "--full-tree", commit)
    entries: list[dict[str, object]] = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, separator, raw_path = record.partition(b"\t")
        if not separator:
            raise ValueError(f"malformed ls-tree record for {commit}")
        fields = metadata.split()
        if len(fields) != 4:
            raise ValueError(f"malformed ls-tree metadata for {commit}: {metadata!r}")
        mode, object_type, oid, size = (field.decode("ascii") for field in fields)
        if object_type != "blob":
            continue
        path = raw_path.decode("utf-8", errors="surrogateescape").replace("\\", "/")
        entries.append(
            {
                "mode": mode,
                "oid": oid,
                "git_size": int(size),
                "path": path,
            }
        )
    return entries


def _read_blobs(repo_dir: Path, oids: Iterable[str]) -> Iterable[tuple[str, bytes]]:
    process = subprocess.Popen(
        [
            "git",
            "-c",
            f"safe.directory={repo_dir.resolve()}",
            "-C",
            str(repo_dir),
            "cat-file",
            "--batch",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.stdin is not None and process.stdout is not None
    try:
        for oid in oids:
            process.stdin.write(oid.encode("ascii") + b"\n")
            process.stdin.flush()
            header = process.stdout.readline().rstrip(b"\n")
            fields = header.split()
            if len(fields) == 2 and fields[1] == b"missing":
                raise RuntimeError(f"missing blob {oid} in {repo_dir.name}")
            if len(fields) != 3 or fields[1] != b"blob":
                raise RuntimeError(f"unexpected cat-file header for {oid}: {header!r}")
            size = int(fields[2])
            data = process.stdout.read(size)
            terminator = process.stdout.read(1)
            if len(data) != size or terminator != b"\n":
                raise RuntimeError(f"truncated cat-file response for {oid}")
            yield oid, data
    finally:
        process.stdin.close()
        return_code = process.wait(timeout=30)
        assert process.stderr is not None
        message = process.stderr.read().decode("utf-8", errors="replace").strip()
        process.stdout.close()
        process.stderr.close()
        if return_code != 0:
            raise RuntimeError(f"git cat-file failed in {repo_dir.name}: {message}")


def _parse_python(data: bytes) -> tuple[bool, str | None, str | None]:
    try:
        encoding, _ = tokenize.detect_encoding(io.BytesIO(data).readline)
        text = data.decode(encoding)
        ast.parse(text)
        return True, encoding, None
    except (SyntaxError, UnicodeDecodeError, LookupError) as error:
        return False, None, f"{type(error).__name__}:{error}"


def verify_sources(
    manifest: Mapping[str, object],
    *,
    asset_root: Path,
    minimum_python_parse_rate: float = 0.99,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    if manifest.get("status") != "RESERVE_ONLY_NO_SEMANTIC_RUN":
        raise ValueError("manifest is not a frozen semantic reserve")
    samples = manifest.get("samples")
    if not isinstance(samples, list) or not samples:
        raise ValueError("manifest has no samples")
    started = time.perf_counter()
    grouped: dict[str, list[Mapping[str, object]]] = defaultdict(list)
    for raw in samples:
        if not isinstance(raw, Mapping):
            raise ValueError("sample must be an object")
        grouped[str(raw["repo"])].append(raw)

    records: list[dict[str, object]] = []
    snapshot_reports: list[dict[str, object]] = []
    unique_bytes = 0
    unique_blobs = 0
    for repo, repo_samples in sorted(grouped.items()):
        repo_dir = _repo_store(asset_root, repo)
        if not repo_dir.is_dir():
            raise FileNotFoundError(f"missing bare object store: {repo_dir}")
        commit_entries: dict[str, list[dict[str, object]]] = {}
        oid_to_paths: dict[str, list[tuple[str, str]]] = defaultdict(list)
        for sample in repo_samples:
            commit = str(sample["base_commit"])
            _git(repo_dir, "cat-file", "-e", f"{commit}^{{commit}}")
            entries = _tree_entries(repo_dir, commit)
            commit_entries[commit] = entries
            for entry in entries:
                oid_to_paths[str(entry["oid"])].append((commit, str(entry["path"])))
        blob_data: dict[str, tuple[str, int, bool | None, str | None, str | None]] = {}
        for oid, data in _read_blobs(repo_dir, sorted(oid_to_paths)):
            is_python = any(path.endswith(".py") for _, path in oid_to_paths[oid])
            parsed: bool | None = None
            encoding: str | None = None
            parse_error: str | None = None
            if is_python:
                parsed, encoding, parse_error = _parse_python(data)
            blob_data[oid] = (
                hashlib.sha256(data).hexdigest(),
                len(data),
                parsed,
                encoding,
                parse_error,
            )
            unique_bytes += len(data)
            unique_blobs += 1

        for sample in repo_samples:
            commit = str(sample["base_commit"])
            sample_id = str(sample["sample_id"])
            query_paths = {str(path) for path in sample.get("query_paths", [])}
            paths_seen: set[str] = set()
            python_count = 0
            python_parsed = 0
            query_results: list[dict[str, object]] = []
            for entry in commit_entries[commit]:
                path = str(entry["path"])
                oid = str(entry["oid"])
                digest, actual_size, parsed, encoding, parse_error = blob_data[oid]
                if actual_size != int(entry["git_size"]):
                    raise RuntimeError(f"Git size mismatch for {repo}@{commit}:{path}")
                is_python = path.endswith(".py")
                if is_python:
                    python_count += 1
                    python_parsed += int(parsed is True)
                is_query = path in query_paths
                if is_query:
                    paths_seen.add(path)
                    query_results.append(
                        {
                            "path": path,
                            "oid": oid,
                            "sha256": digest,
                            "bytes": actual_size,
                            "python_ast_parse": parsed,
                            "encoding": encoding,
                            "parse_error": parse_error,
                        }
                    )
                records.append(
                    {
                        "sample_id": sample_id,
                        "repo": repo,
                        "base_commit": commit,
                        "path": path,
                        "mode": entry["mode"],
                        "git_oid": oid,
                        "sha256": digest,
                        "bytes": actual_size,
                        "is_python": is_python,
                        "python_ast_parse": parsed,
                        "encoding": encoding,
                        "parse_error": parse_error,
                        "is_query_path": is_query,
                    }
                )
            missing_query = sorted(query_paths.difference(paths_seen))
            query_python = [item for item in query_results if str(item["path"]).endswith(".py")]
            query_parse_ok = bool(query_python) and all(item["python_ast_parse"] is True for item in query_python)
            snapshot_reports.append(
                {
                    "sample_id": sample_id,
                    "task_type": sample["task_type"],
                    "repo": repo,
                    "base_commit": commit,
                    "tree_oid": _git(repo_dir, "rev-parse", f"{commit}^{{tree}}").decode("ascii").strip(),
                    "file_count": len(commit_entries[commit]),
                    "python_file_count": python_count,
                    "python_ast_parsed": python_parsed,
                    "python_ast_parse_rate": python_parsed / python_count if python_count else 0.0,
                    "query_paths_expected": sorted(query_paths),
                    "query_paths_missing": missing_query,
                    "query_paths": sorted(query_results, key=lambda item: str(item["path"])),
                    "query_python_ast_ready": query_parse_ok,
                }
            )

    python_rows = [row for row in records if row["is_python"]]
    python_parsed = sum(row["python_ast_parse"] is True for row in python_rows)
    parse_rate = python_parsed / len(python_rows) if python_rows else 0.0
    all_query_present = all(not item["query_paths_missing"] for item in snapshot_reports)
    all_query_parse = all(bool(item["query_python_ast_ready"]) for item in snapshot_reports)
    ready = (
        len(snapshot_reports) == int(manifest.get("sample_count", -1))
        and all_query_present
        and all_query_parse
        and parse_rate >= minimum_python_parse_rate
    )
    summary: dict[str, object] = {
        "schema_version": 1,
        "status": READY_STATUS if ready else NO_RUN_STATUS,
        "authorization": "semantic_index_build_only_no_gold_scoring_no_training",
        "manifest_sample_count": manifest.get("sample_count"),
        "verified_snapshot_count": len(snapshot_reports),
        "repository_count": len(grouped),
        "tree_file_rows": len(records),
        "unique_blob_objects_read": unique_blobs,
        "unique_blob_bytes_read": unique_bytes,
        "python_file_rows": len(python_rows),
        "python_ast_parsed": python_parsed,
        "python_ast_parse_rate": parse_rate,
        "minimum_python_parse_rate": minimum_python_parse_rate,
        "all_query_paths_present": all_query_present,
        "all_query_python_ast_ready": all_query_parse,
        "wall_seconds": time.perf_counter() - started,
        "snapshots": snapshot_reports,
    }
    return summary, records


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--asset-root", type=Path, required=True)
    parser.add_argument("--minimum-python-parse-rate", type=float, default=0.99)
    parser.add_argument("--blob-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    summary, records = verify_sources(
        manifest,
        asset_root=args.asset_root,
        minimum_python_parse_rate=args.minimum_python_parse_rate,
    )
    args.blob_manifest.parent.mkdir(parents=True, exist_ok=True)
    with args.blob_manifest.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    summary["reserve_manifest_sha256"] = sha256_file(args.manifest)
    summary["blob_manifest_sha256"] = sha256_file(args.blob_manifest)
    summary["blob_manifest_rows"] = len(records)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
