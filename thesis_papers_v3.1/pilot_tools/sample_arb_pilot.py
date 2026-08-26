"""Create a deterministic, gold-blind Agent Retrieval Bench pilot sample.

The selector reads released ``samples.jsonl`` files but deliberately emits no
query or gold fields.  Selection depends only on the public sample identifier,
repository, base commit, task type, and a pre-registered salt.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Candidate:
    release_id: str
    source: Path
    source_line: int
    sample_id: str
    task_type: str
    repo: str
    base_commit: str

    @property
    def snapshot(self) -> tuple[str, str]:
        return self.repo, self.base_commit


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def selection_hash(salt: str, sample_id: str) -> str:
    return hashlib.sha256(f"{salt}|{sample_id}".encode("utf-8")).hexdigest()


def load_candidates(release_id: str, source: Path) -> list[Candidate]:
    rows: list[Candidate] = []
    seen: set[str] = set()
    with source.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            raw = json.loads(line)
            required = {"id", "task_type", "repo", "base_commit"}
            missing = required.difference(raw)
            if missing:
                raise ValueError(f"{source}:{line_number}: missing {sorted(missing)}")
            sample_id = str(raw["id"])
            if sample_id in seen:
                raise ValueError(f"{source}:{line_number}: duplicate sample id {sample_id}")
            seen.add(sample_id)
            rows.append(
                Candidate(
                    release_id=release_id,
                    source=source,
                    source_line=line_number,
                    sample_id=sample_id,
                    task_type=str(raw["task_type"]),
                    repo=str(raw["repo"]),
                    base_commit=str(raw["base_commit"]),
                )
            )
    if not rows:
        raise ValueError(f"{source}: no samples")
    task_types = {row.task_type for row in rows}
    if len(task_types) != 1:
        raise ValueError(f"{source}: expected one task type, found {sorted(task_types)}")
    return rows


def select_candidates(
    rows: list[Candidate], *, salt: str, count: int, max_per_repo: int
) -> list[Candidate]:
    if count < 1 or max_per_repo < 1:
        raise ValueError("count and max_per_repo must be positive")
    ranked = sorted(rows, key=lambda row: (selection_hash(salt, row.sample_id), row.sample_id))
    selected: list[Candidate] = []
    selected_ids: set[str] = set()
    selected_snapshots: set[tuple[str, str]] = set()
    repo_counts: Counter[str] = Counter()

    # First pass maximizes distinct frozen snapshots without looking at gold.
    # The second pass fills any remaining slots while retaining the repo cap.
    for require_new_snapshot in (True, False):
        for row in ranked:
            if len(selected) >= count:
                break
            if row.sample_id in selected_ids or repo_counts[row.repo] >= max_per_repo:
                continue
            if require_new_snapshot and row.snapshot in selected_snapshots:
                continue
            selected.append(row)
            selected_ids.add(row.sample_id)
            selected_snapshots.add(row.snapshot)
            repo_counts[row.repo] += 1
        if len(selected) >= count:
            break
    if len(selected) != count:
        raise ValueError(
            f"only selected {len(selected)}/{count}; relax max_per_repo or add candidates"
        )
    return selected


def build_manifest(
    release_paths: dict[str, Path],
    *,
    archive_sha256: dict[str, str],
    arb_code_commit: str,
    salt: str,
    count_per_release: int,
    max_per_repo: int,
    workspace_root: Path | None = None,
) -> dict:
    all_selected: list[dict] = []
    source_fingerprints: dict[str, str] = {}
    global_ids: set[str] = set()
    global_index = 0
    for release_id in sorted(release_paths):
        source = release_paths[release_id].resolve()
        rows = load_candidates(release_id, source)
        selected = select_candidates(
            rows, salt=salt, count=count_per_release, max_per_repo=max_per_repo
        )
        source_fingerprints[release_id] = sha256_file(source)
        for within_index, row in enumerate(selected, start=1):
            if row.sample_id in global_ids:
                raise ValueError(f"sample id appears in multiple releases: {row.sample_id}")
            global_ids.add(row.sample_id)
            global_index += 1
            if workspace_root is not None:
                try:
                    source_label = source.relative_to(workspace_root.resolve()).as_posix()
                except ValueError:
                    source_label = source.name
            else:
                source_label = source.name
            all_selected.append(
                {
                    "pilot_index": global_index,
                    "within_release_index": within_index,
                    "release_id": release_id,
                    "task_type": row.task_type,
                    "sample_id": row.sample_id,
                    "repo": row.repo,
                    "base_commit": row.base_commit,
                    "selection_hash": selection_hash(salt, row.sample_id),
                    "source": source_label,
                    "source_line": row.source_line,
                    "source_sha256": source_fingerprints[release_id],
                    "archive_sha256": archive_sha256.get(release_id),
                }
            )

    by_type = Counter(item["task_type"] for item in all_selected)
    repo_type = Counter((item["task_type"], item["repo"]) for item in all_selected)
    if any(value > max_per_repo for value in repo_type.values()):
        raise AssertionError("repository cap violated")
    return {
        "schema_version": 1,
        "selection_policy": {
            "salt": salt,
            "count_per_release": count_per_release,
            "max_per_repo_per_task_type": max_per_repo,
            "ranking": "SHA256(salt + '|' + sample_id), then sample_id",
            "passes": ["prefer-new-repo-base_commit", "fill-under-repo-cap"],
            "gold_blind": True,
        },
        "arb_code_commit": arb_code_commit,
        "release_archive_sha256": dict(sorted(archive_sha256.items())),
        "source_samples_sha256": dict(sorted(source_fingerprints.items())),
        "sample_count": len(all_selected),
        "counts_by_task_type": dict(sorted(by_type.items())),
        "samples": all_selected,
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
    parser.add_argument("--arb-code-commit", required=True)
    parser.add_argument("--salt", default="rtp-oracle-v0")
    parser.add_argument("--count-per-release", type=int, default=20)
    parser.add_argument("--max-per-repo", type=int, default=4)
    parser.add_argument("--workspace-root", type=Path)
    parser.add_argument(
        "--keep-dir",
        type=Path,
        help="Optional directory for one ARB-compatible keep-list JSONL per release.",
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    releases = {key: Path(value) for key, value in args.release}
    if len(releases) != len(args.release):
        raise ValueError("duplicate --release key")
    archive_sha256 = dict(args.archive_sha256)
    if len(archive_sha256) != len(args.archive_sha256):
        raise ValueError("duplicate --archive-sha256 key")
    unknown = set(archive_sha256).difference(releases)
    if unknown:
        raise ValueError(f"archive checksums without release input: {sorted(unknown)}")
    report = build_manifest(
        releases,
        archive_sha256=archive_sha256,
        arb_code_commit=args.arb_code_commit,
        salt=args.salt,
        count_per_release=args.count_per_release,
        max_per_repo=args.max_per_repo,
        workspace_root=args.workspace_root,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.keep_dir is not None:
        args.keep_dir.mkdir(parents=True, exist_ok=True)
        by_release: dict[str, list[dict]] = {}
        for sample in report["samples"]:
            by_release.setdefault(sample["release_id"], []).append(
                {
                    "sample_id": sample["sample_id"],
                    "task_type": sample["task_type"],
                    "verdict": "valid",
                    "selection_hash": sample["selection_hash"],
                }
            )
        for release_id, samples in sorted(by_release.items()):
            keep_path = args.keep_dir / f"{release_id}.jsonl"
            keep_path.write_text(
                "".join(json.dumps(item, sort_keys=True) + "\n" for item in samples),
                encoding="utf-8",
            )


if __name__ == "__main__":
    main()
