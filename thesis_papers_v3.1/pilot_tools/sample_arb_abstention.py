"""Create a deterministic, query-blind ARB abstention pilot sample.

The released abstention file contains 50 natural no-gold cases and 32
counterfactual wrong-repository controls.  This selector samples the two
strata independently without emitting query, gold, evidence, or pairing
metadata.  Selection uses only identifiers, frozen repository coordinates,
the released ``metadata.organic`` stratum flag, and a pre-registered salt.
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
    source_line: int
    sample_id: str
    repo: str
    base_commit: str
    stratum: str

    @property
    def snapshot(self) -> tuple[str, str]:
        return self.repo, self.base_commit


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def selection_hash(salt: str, stratum: str, sample_id: str) -> str:
    payload = f"{salt}|{stratum}|{sample_id}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_candidates(source: Path) -> list[Candidate]:
    rows: list[Candidate] = []
    seen: set[str] = set()
    with source.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            raw = json.loads(line)
            required = {"id", "task_type", "repo", "base_commit", "metadata"}
            missing = required.difference(raw)
            if missing:
                raise ValueError(f"{source}:{line_number}: missing {sorted(missing)}")
            if str(raw["task_type"]) != "abstention":
                raise ValueError(
                    f"{source}:{line_number}: expected abstention, got {raw['task_type']}"
                )
            metadata = raw["metadata"]
            if not isinstance(metadata, dict) or not isinstance(metadata.get("organic"), bool):
                raise ValueError(f"{source}:{line_number}: metadata.organic must be boolean")
            stratum = "natural" if metadata["organic"] else "counterfactual_wrong_repo"
            sample_id = str(raw["id"])
            if sample_id in seen:
                raise ValueError(f"{source}:{line_number}: duplicate sample id {sample_id}")
            seen.add(sample_id)
            rows.append(
                Candidate(
                    source_line=line_number,
                    sample_id=sample_id,
                    repo=str(raw["repo"]),
                    base_commit=str(raw["base_commit"]),
                    stratum=stratum,
                )
            )
    if not rows:
        raise ValueError(f"{source}: no samples")
    return rows


def select_stratum(
    rows: list[Candidate], *, salt: str, count: int, max_per_repo: int
) -> list[Candidate]:
    if count < 1 or max_per_repo < 1:
        raise ValueError("count and max_per_repo must be positive")
    if not rows:
        raise ValueError("stratum has no candidates")
    strata = {row.stratum for row in rows}
    if len(strata) != 1:
        raise ValueError(f"expected one stratum, found {sorted(strata)}")
    stratum = next(iter(strata))
    ranked = sorted(
        rows,
        key=lambda row: (
            selection_hash(salt, stratum, row.sample_id),
            row.sample_id,
        ),
    )
    selected: list[Candidate] = []
    selected_ids: set[str] = set()
    snapshots: set[tuple[str, str]] = set()
    repo_counts: Counter[str] = Counter()
    for require_new_snapshot in (True, False):
        for row in ranked:
            if len(selected) >= count:
                break
            if row.sample_id in selected_ids or repo_counts[row.repo] >= max_per_repo:
                continue
            if require_new_snapshot and row.snapshot in snapshots:
                continue
            selected.append(row)
            selected_ids.add(row.sample_id)
            snapshots.add(row.snapshot)
            repo_counts[row.repo] += 1
        if len(selected) >= count:
            break
    if len(selected) != count:
        raise ValueError(
            f"only selected {len(selected)}/{count} from {stratum}; "
            "relax max_per_repo or add candidates"
        )
    return selected


def build_manifest(
    source: Path,
    *,
    archive_sha256: str,
    arb_code_commit: str,
    salt: str,
    count_per_stratum: int,
    max_per_repo: int,
    workspace_root: Path | None = None,
) -> dict:
    source = source.resolve()
    candidates = load_candidates(source)
    selected: list[Candidate] = []
    for stratum in ("natural", "counterfactual_wrong_repo"):
        selected.extend(
            select_stratum(
                [row for row in candidates if row.stratum == stratum],
                salt=salt,
                count=count_per_stratum,
                max_per_repo=max_per_repo,
            )
        )
    source_hash = sha256_file(source)
    try:
        source_label = (
            source.relative_to(workspace_root.resolve()).as_posix()
            if workspace_root is not None
            else source.name
        )
    except ValueError:
        source_label = source.name
    samples: list[dict] = []
    for index, row in enumerate(selected, start=1):
        samples.append(
            {
                "pilot_index": index,
                "release_id": "v2_abstention",
                "task_type": "abstention",
                "stratum": row.stratum,
                "sample_id": row.sample_id,
                "repo": row.repo,
                "base_commit": row.base_commit,
                "selection_hash": selection_hash(salt, row.stratum, row.sample_id),
                "source": source_label,
                "source_line": row.source_line,
                "source_sha256": source_hash,
                "archive_sha256": archive_sha256,
            }
        )
    counts = Counter(row["stratum"] for row in samples)
    return {
        "schema_version": 1,
        "selection_policy": {
            "salt": salt,
            "count_per_stratum": count_per_stratum,
            "max_per_repo_per_stratum": max_per_repo,
            "ranking": "SHA256(salt + '|' + stratum + '|' + sample_id), then sample_id",
            "passes": ["prefer-new-repo-base_commit", "fill-under-repo-cap"],
            "query_blind": True,
            "gold_blind": True,
            "label_use": "released metadata.organic only, for pre-specified stratification",
        },
        "arb_code_commit": arb_code_commit,
        "release_archive_sha256": archive_sha256,
        "source_samples_sha256": source_hash,
        "sample_count": len(samples),
        "counts_by_stratum": dict(sorted(counts.items())),
        "samples": samples,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--archive-sha256", required=True)
    parser.add_argument("--arb-code-commit", required=True)
    parser.add_argument("--salt", default="rtp-abstention-v0")
    parser.add_argument("--count-per-stratum", type=int, default=10)
    parser.add_argument("--max-per-repo", type=int, default=3)
    parser.add_argument("--workspace-root", type=Path)
    parser.add_argument("--keep-list", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    report = build_manifest(
        args.source,
        archive_sha256=args.archive_sha256,
        arb_code_commit=args.arb_code_commit,
        salt=args.salt,
        count_per_stratum=args.count_per_stratum,
        max_per_repo=args.max_per_repo,
        workspace_root=args.workspace_root,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if args.keep_list is not None:
        args.keep_list.parent.mkdir(parents=True, exist_ok=True)
        with args.keep_list.open("w", encoding="utf-8", newline="\n") as handle:
            for sample in report["samples"]:
                handle.write(
                    json.dumps(
                        {
                            "sample_id": sample["sample_id"],
                            "task_type": sample["task_type"],
                            "verdict": "valid",
                            "selection_hash": sample["selection_hash"],
                            "stratum": sample["stratum"],
                        },
                        sort_keys=True,
                    )
                    + "\n"
                )


if __name__ == "__main__":
    main()
