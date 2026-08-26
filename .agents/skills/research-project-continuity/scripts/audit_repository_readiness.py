#!/usr/bin/env python3
"""Inventory Git/GitHub readiness without reading file contents or changing state."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import unicodedata
from collections import Counter
from pathlib import Path


SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules"}
SECRET_NAMES = {".env", ".env.local", ".env.production", "credentials.json", "secrets.json"}


def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=root, text=True, encoding="utf-8", errors="replace",
        capture_output=True, check=False
    )


def count_porcelain(root: Path) -> dict[str, int]:
    result = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    if result.returncode:
        return {"error": result.returncode}
    counts: Counter[str] = Counter()
    for record in result.stdout.split("\0"):
        if record:
            counts[record[:2]] += 1
    return dict(sorted(counts.items()))


def ignored(root: Path, relative: str) -> bool:
    return git(root, "check-ignore", "-q", "--", relative).returncode == 0


def collision_groups(paths: list[str], *, fold_case: bool) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for path in paths:
        key = unicodedata.normalize("NFC", path)
        if fold_case:
            key = key.casefold()
        groups.setdefault(key, []).append(path)
    return [sorted(set(group)) for group in groups.values() if len(set(group)) > 1]


def candidate_inventory(root: Path) -> dict[str, object]:
    """Inventory tracked plus visible untracked files selected by ignore rules."""
    result = git(root, "ls-files", "-co", "--exclude-standard", "-z")
    if result.returncode:
        return {"error": result.returncode}
    relative_paths = sorted(set(path for path in result.stdout.split("\0") if path))
    total_bytes = 0
    stat_errors: list[str] = []
    large_files: list[dict[str, object]] = []
    long_paths: list[dict[str, object]] = []
    directory_counts: Counter[str] = Counter()
    secret_like: list[str] = []
    overlong_components: list[dict[str, object]] = []
    for relative_text in relative_paths:
        path = root / Path(relative_text)
        directory_counts[str(Path(relative_text).parent)] += 1
        if len(str(path)) > 240:
            long_paths.append({"path": relative_text, "absolute_chars": len(str(path))})
        name = path.name.lower()
        if name in SECRET_NAMES or name.startswith(".env."):
            secret_like.append(relative_text)
        for component in Path(relative_text).parts:
            encoded_bytes = len(component.encode("utf-8"))
            if encoded_bytes > 255:
                overlong_components.append(
                    {"path": relative_text, "component": component, "utf8_bytes": encoded_bytes}
                )
        try:
            size = path.stat().st_size
        except OSError:
            stat_errors.append(relative_text)
            continue
        total_bytes += size
        if size >= 50 * 1024 * 1024:
            large_files.append({"path": relative_text, "bytes": size, "over_100_mib": size > 100 * 1024 * 1024})
    case_or_normalization_collisions = collision_groups(relative_paths, fold_case=True)
    normalization_collisions = collision_groups(relative_paths, fold_case=False)
    return {
        "files": len(relative_paths),
        "bytes": total_bytes,
        "stat_error_count": len(stat_errors),
        "stat_error_examples": stat_errors[:25],
        "large_files": sorted(large_files, key=lambda item: item["bytes"], reverse=True),
        "long_path_count": len(long_paths),
        "long_path_examples": sorted(long_paths, key=lambda item: item["absolute_chars"], reverse=True)[:25],
        "wide_directories": [
            {"path": path, "entries": count}
            for path, count in directory_counts.most_common()
            if count > 3000
        ],
        "secret_like_paths": sorted(secret_like),
        "case_or_normalization_collision_count": len(case_or_normalization_collisions),
        "case_or_normalization_collision_examples": case_or_normalization_collisions[:25],
        "unicode_normalization_collision_count": len(normalization_collisions),
        "unicode_normalization_collision_examples": normalization_collisions[:25],
        "overlong_component_count": len(overlong_components),
        "overlong_component_examples": overlong_components[:25],
    }


def scan(root: Path) -> dict[str, object]:
    total_bytes = 0
    file_count = 0
    large_files: list[dict[str, object]] = []
    long_paths: list[dict[str, object]] = []
    wide_dirs: list[dict[str, object]] = []
    secret_like: list[str] = []
    top_level_bytes: Counter[str] = Counter()

    for current, dirs, files in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        current_path = Path(current)
        if len(files) > 3000:
            wide_dirs.append({"path": str(current_path.relative_to(root)), "entries": len(files)})
        for name in files:
            path = current_path / name
            try:
                size = path.stat().st_size
            except OSError:
                continue
            relative = path.relative_to(root)
            file_count += 1
            total_bytes += size
            top_level_bytes[relative.parts[0]] += size
            if size >= 50 * 1024 * 1024:
                large_files.append({"path": str(relative), "bytes": size, "over_100_mib": size > 100 * 1024 * 1024})
            if len(str(path)) > 260:
                long_paths.append({"path": str(relative), "absolute_chars": len(str(path))})
            if name.lower() in SECRET_NAMES or name.lower().startswith(".env."):
                secret_like.append(str(relative))

    return {
        "files": file_count,
        "bytes": total_bytes,
        "top_level_bytes": dict(top_level_bytes.most_common()),
        "large_files": sorted(large_files, key=lambda item: item["bytes"], reverse=True),
        "long_path_count": len(long_paths),
        "long_path_examples": sorted(long_paths, key=lambda item: item["absolute_chars"], reverse=True)[:25],
        "wide_directories": sorted(wide_dirs, key=lambda item: item["entries"], reverse=True),
        "secret_like_paths": sorted(secret_like),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--fail-on-blockers", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    critical = [
        "database_fulltext_all",
        ".agents/skills",
        "docs/research_program",
        ".env",
    ]
    payload = {
        "root": str(root),
        "git_status_counts": count_porcelain(root),
        "critical_ignore_status": {path: ignored(root, path) for path in critical},
        "publication_candidates": candidate_inventory(root),
        "inventory": scan(root),
        "interpretation": "read-only preflight; inspect licenses, staged diff, and corpus rights before push",
    }
    if args.as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(payload["root"])
        print(payload["interpretation"])
        print(f"files={payload['inventory']['files']} bytes={payload['inventory']['bytes']}")
        print(f"git_status_counts={payload['git_status_counts']}")
        print(f"critical_ignore_status={payload['critical_ignore_status']}")
        print(
            "publication_candidates="
            f"{payload['publication_candidates'].get('files')} files, "
            f"{payload['publication_candidates'].get('bytes')} bytes"
        )
        print(f"candidate_large_files={payload['publication_candidates'].get('large_files')}")
        print(f"candidate_long_paths={payload['publication_candidates'].get('long_path_count')}")
        print(f"candidate_wide_directories={payload['publication_candidates'].get('wide_directories')}")
        print(
            "candidate_case_or_normalization_collisions="
            f"{payload['publication_candidates'].get('case_or_normalization_collision_count')}"
        )
        print(
            "candidate_unicode_normalization_collisions="
            f"{payload['publication_candidates'].get('unicode_normalization_collision_count')}"
        )
        print(
            "candidate_overlong_components="
            f"{payload['publication_candidates'].get('overlong_component_count')}"
        )
        print(f"large_files={len(payload['inventory']['large_files'])}")
        print(f"long_paths={payload['inventory']['long_path_count']}")
        print(f"wide_directories={payload['inventory']['wide_directories']}")
        print(f"secret_like_paths={payload['inventory']['secret_like_paths']}")

    blockers = any(item["over_100_mib"] for item in payload["publication_candidates"].get("large_files", []))
    blockers = blockers or not payload["critical_ignore_status"][".env"]
    blockers = blockers or bool(
        payload["publication_candidates"].get("case_or_normalization_collision_count")
    )
    blockers = blockers or bool(payload["publication_candidates"].get("overlong_component_count"))
    return 2 if blockers and args.fail_on_blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
