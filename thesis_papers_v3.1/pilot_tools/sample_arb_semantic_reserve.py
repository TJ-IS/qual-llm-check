"""Freeze the query-only ARB reserve for a full-source semantic micro-screen.

This selector is intentionally narrower than ``sample_arb_pilot.py``.  It
excludes every sample and frozen snapshot used by the 60-task Stage-0
development batch, restricts the reserve to a pre-registered Python repository
allowlist, and emits only deployment-visible identifiers and query paths.  It
never copies gold, qrels, reference patches, or evaluation fields into the
manifest.

The resulting manifest authorizes *source acquisition only*.  Released ARB
chunks are truncated and cannot support the proposed semantic graph; the
manifest therefore records a fail-closed ``NO_RUN`` state until the exact Git
commits and blobs have been independently verified.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping


SALT = "arb-semantic-ast-v0"
PYTHON_REPOS = (
    "fastapi/fastapi",
    "huggingface/diffusers",
    "huggingface/transformers",
    "pytest-dev/pytest",
    "pallets/click",
)
CODE2TEST_QUOTA = {
    "fastapi/fastapi": 2,
    "huggingface/diffusers": 2,
    "huggingface/transformers": 2,
    "pytest-dev/pytest": 2,
}
TRACE2CODE_QUOTA = {"pallets/click": 8}
PATH_LINE_RE = re.compile(r"(?P<path>(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+\.py):\d+")


@dataclass(frozen=True)
class Candidate:
    release_id: str
    task_type: str
    sample_id: str
    repo: str
    base_commit: str
    query_paths: tuple[str, ...]
    source: Path
    source_line: int

    @property
    def snapshot(self) -> tuple[str, str]:
        return self.repo, self.base_commit


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def selection_hash(candidate: Candidate, salt: str = SALT) -> str:
    fields = (
        salt,
        candidate.release_id,
        candidate.repo,
        candidate.base_commit,
        candidate.sample_id,
    )
    return hashlib.sha256("\0".join(fields).encode("utf-8")).hexdigest()


def _normal_path(value: object) -> str:
    text = str(value or "").strip().replace("\\", "/")
    while text.startswith("./"):
        text = text[2:]
    return text


def query_paths(task_type: str, query: Mapping[str, object]) -> tuple[str, ...]:
    """Project only paths explicitly visible in the released query."""

    paths: list[str] = []
    if task_type == "code2test":
        values = query.get("implementation_files")
        if isinstance(values, list):
            paths.extend(_normal_path(value) for value in values)
        paths.append(_normal_path(query.get("changed_file")))
    elif task_type == "trace2code":
        excerpt = str(query.get("failure_excerpt") or "")
        paths.extend(_normal_path(match.group("path")) for match in PATH_LINE_RE.finditer(excerpt))
    else:
        raise ValueError(f"unsupported reserve task type: {task_type}")
    return tuple(dict.fromkeys(path for path in paths if path))


def load_safe_candidates(release_id: str, source: Path) -> list[Candidate]:
    rows: list[Candidate] = []
    seen: set[str] = set()
    with source.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            raw = json.loads(line)
            required = {"id", "task_type", "repo", "base_commit", "query"}
            missing = required.difference(raw)
            if missing:
                raise ValueError(f"{source}:{line_number}: missing {sorted(missing)}")
            sample_id = str(raw["id"])
            if sample_id in seen:
                raise ValueError(f"{source}:{line_number}: duplicate sample id {sample_id}")
            seen.add(sample_id)
            task_type = str(raw["task_type"])
            repo = str(raw["repo"])
            if repo not in PYTHON_REPOS:
                continue
            query = raw["query"]
            if not isinstance(query, Mapping):
                raise ValueError(f"{source}:{line_number}: query must be an object")
            paths = query_paths(task_type, query)
            if not paths:
                continue
            rows.append(
                Candidate(
                    release_id=release_id,
                    task_type=task_type,
                    sample_id=sample_id,
                    repo=repo,
                    base_commit=str(raw["base_commit"]),
                    query_paths=paths,
                    source=source,
                    source_line=line_number,
                )
            )
    return rows


def _stage0_exclusions(stage0_manifest: Mapping[str, object]) -> tuple[set[str], set[tuple[str, str]]]:
    samples = stage0_manifest.get("samples")
    if not isinstance(samples, list):
        raise ValueError("Stage-0 manifest has no samples array")
    ids: set[str] = set()
    snapshots: set[tuple[str, str]] = set()
    for item in samples:
        if not isinstance(item, Mapping):
            raise ValueError("Stage-0 sample must be an object")
        sample_id = str(item.get("sample_id") or "")
        repo = str(item.get("repo") or "")
        commit = str(item.get("base_commit") or "")
        if not sample_id or not repo or not commit:
            raise ValueError("Stage-0 sample lacks id/repo/commit")
        ids.add(sample_id)
        snapshots.add((repo, commit))
    return ids, snapshots


def select_reserve(
    candidates: Iterable[Candidate],
    *,
    excluded_ids: set[str],
    excluded_snapshots: set[tuple[str, str]],
    salt: str = SALT,
) -> list[Candidate]:
    quotas = {"code2test": CODE2TEST_QUOTA, "trace2code": TRACE2CODE_QUOTA}
    remaining = [
        item
        for item in candidates
        if item.sample_id not in excluded_ids and item.snapshot not in excluded_snapshots
    ]
    selected: list[Candidate] = []
    used_snapshots: set[tuple[str, str]] = set()
    for task_type, repo_quotas in quotas.items():
        for repo, count in repo_quotas.items():
            ranked = sorted(
                (item for item in remaining if item.task_type == task_type and item.repo == repo),
                key=lambda item: (selection_hash(item, salt), item.sample_id),
            )
            picked: list[Candidate] = []
            for item in ranked:
                if item.snapshot in used_snapshots:
                    continue
                picked.append(item)
                used_snapshots.add(item.snapshot)
                if len(picked) == count:
                    break
            if len(picked) != count:
                raise ValueError(f"reserve capacity {task_type}/{repo}: {len(picked)}/{count}")
            selected.extend(picked)
    return sorted(selected, key=lambda item: (item.task_type, item.repo, selection_hash(item, salt)))


def _source_label(path: Path, workspace_root: Path | None) -> str:
    resolved = path.resolve()
    if workspace_root is not None:
        try:
            return resolved.relative_to(workspace_root.resolve()).as_posix()
        except ValueError:
            pass
    return path.name


def build_manifest(
    release_paths: Mapping[str, Path],
    *,
    stage0_manifest_path: Path,
    arb_code_commit: str,
    archive_sha256: Mapping[str, str],
    workspace_root: Path | None = None,
    salt: str = SALT,
) -> dict[str, object]:
    stage0_manifest = json.loads(stage0_manifest_path.read_text(encoding="utf-8"))
    excluded_ids, excluded_snapshots = _stage0_exclusions(stage0_manifest)
    candidates: list[Candidate] = []
    source_hashes: dict[str, str] = {}
    for release_id, source_value in sorted(release_paths.items()):
        source = source_value.resolve()
        source_hashes[release_id] = sha256_file(source)
        candidates.extend(load_safe_candidates(release_id, source))
    selected = select_reserve(
        candidates,
        excluded_ids=excluded_ids,
        excluded_snapshots=excluded_snapshots,
        salt=salt,
    )
    samples: list[dict[str, object]] = []
    for index, item in enumerate(selected, start=1):
        samples.append(
            {
                "reserve_index": index,
                "release_id": item.release_id,
                "task_type": item.task_type,
                "sample_id": item.sample_id,
                "repo": item.repo,
                "base_commit": item.base_commit,
                "query_paths": list(item.query_paths),
                "selection_hash": selection_hash(item, salt),
                "source": _source_label(item.source, workspace_root),
                "source_line": item.source_line,
                "source_sha256": source_hashes[item.release_id],
                "archive_sha256": archive_sha256.get(item.release_id),
            }
        )
    snapshots = {(str(item["repo"]), str(item["base_commit"])) for item in samples}
    if len(snapshots) != len(samples):
        raise AssertionError("reserve snapshots are not unique")
    return {
        "schema_version": 1,
        "status": "RESERVE_ONLY_NO_SEMANTIC_RUN",
        "authorization": "full_source_acquisition_and_hash_verification_only",
        "source_completeness": "released_arb_chunks_insufficient_full_git_blobs_required",
        "gold_blind": True,
        "salt": salt,
        "selection_key": "SHA256(salt\\0release\\0repo\\0base_commit\\0sample_id)",
        "python_repo_allowlist": list(PYTHON_REPOS),
        "quotas": {
            "code2test": dict(CODE2TEST_QUOTA),
            "trace2code": dict(TRACE2CODE_QUOTA),
        },
        "exclusions": {
            "stage0_manifest": _source_label(stage0_manifest_path, workspace_root),
            "stage0_manifest_sha256": sha256_file(stage0_manifest_path),
            "sample_ids": len(excluded_ids),
            "snapshots": len(excluded_snapshots),
        },
        "arb_code_commit": arb_code_commit,
        "release_archive_sha256": dict(sorted(archive_sha256.items())),
        "source_samples_sha256": dict(sorted(source_hashes.items())),
        "sample_count": len(samples),
        "snapshot_count": len(snapshots),
        "samples": samples,
    }


def _mapping(value: str) -> tuple[str, str]:
    key, separator, item = value.partition("=")
    if not separator or not key or not item:
        raise argparse.ArgumentTypeError("expected RELEASE=VALUE")
    return key, item


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="append", type=_mapping, required=True)
    parser.add_argument("--archive-sha256", action="append", type=_mapping, default=[])
    parser.add_argument("--stage0-manifest", type=Path, required=True)
    parser.add_argument("--arb-code-commit", required=True)
    parser.add_argument("--workspace-root", type=Path)
    parser.add_argument("--salt", default=SALT)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    releases = {key: Path(value) for key, value in args.release}
    if len(releases) != len(args.release):
        raise ValueError("duplicate release key")
    archive_sha256 = dict(args.archive_sha256)
    if len(archive_sha256) != len(args.archive_sha256):
        raise ValueError("duplicate archive checksum key")
    report = build_manifest(
        releases,
        stage0_manifest_path=args.stage0_manifest,
        arb_code_commit=args.arb_code_commit,
        archive_sha256=archive_sha256,
        workspace_root=args.workspace_root,
        salt=args.salt,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
