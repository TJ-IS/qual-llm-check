"""Validate and descriptively summarize the frozen ARB baseline grid.

The official design contains three releases and three fixed rankers.  This
script never modifies the evaluation root or selection manifest and makes no
causal or new-algorithm comparison.  It writes deterministic JSON and Markdown
only after the entire requested grid passes validation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from statistics import mean
from typing import Iterable


RELEASES = ("v2_code2test", "v2_edit2ripple", "v2_trace2code")
TASK_TYPES = {
    "v2_code2test": "code2test",
    "v2_edit2ripple": "edit2ripple",
    "v2_trace2code": "trace2code",
}
METHODS = ("lexical", "bm25", "repomap")
KEY_METRICS = (
    "MRR",
    "Precision@5",
    "Precision@10",
    "Precision@20",
    "Recall@5",
    "Recall@10",
    "Recall@20",
    "F0.5@5",
    "F0.5@10",
    "F0.5@20",
    "coverage_auc@20",
    "gold_coverage@8k",
    "context_efficiency@8k",
    "context_pollution_tokens@8k",
    "redundancy@8k",
    "hard_negative_hits@5",
    "hard_negative_hits@10",
    "hard_negative_hits@20",
    "irrelevant_files@5",
    "irrelevant_files@10",
    "irrelevant_files@20",
)
MARKDOWN_METRICS = (
    "MRR",
    "Recall@20",
    "F0.5@10",
    "coverage_auc@20",
    "legacy_gold_file_fraction@8k_chars",
    "legacy_context_efficiency@8k_chars",
    "context_pollution_tokens@8k",
)
OUTPUT_METRIC_NAMES = {
    metric: metric for metric in KEY_METRICS
}
OUTPUT_METRIC_NAMES.update(
    {
        "gold_coverage@8k": "legacy_gold_file_fraction@8k_chars",
        "context_efficiency@8k": "legacy_context_efficiency@8k_chars",
    }
)
OUTPUT_KEY_METRICS = tuple(OUTPUT_METRIC_NAMES[metric] for metric in KEY_METRICS)
LEGACY_PACKING_WARNING = (
    "Source fields gold_coverage@8k and context_efficiency@8k use the official "
    "legacy 8,000-character packing implementation. They are not canonical "
    "token-packed BCY; canonical BCY requires the official token-based reporting path."
)
TOP20_UNION_WARNING = (
    "The top-20 union is an intentionally generous descriptive diagnostic: it "
    "can contain up to 60 files, is not equal-cost, is not a sequential program, "
    "and does not establish complementarity or causal value."
)
FLOAT_ABS_TOL = 1e-12
FLOAT_REL_TOL = 1e-10


class DataValidationError(ValueError):
    """Raised when the tracked grid is missing, duplicated, or inconsistent."""


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_json(path: Path) -> dict:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise DataValidationError(f"missing expected file: {path.name}") from error
    except json.JSONDecodeError as error:
        raise DataValidationError(
            f"invalid or partially written JSON in {path.name}: line {error.lineno}, column {error.colno}"
        ) from error
    if not isinstance(raw, dict):
        raise DataValidationError(f"{path.name}: expected a JSON object")
    return raw


def _read_jsonl(path: Path) -> list[dict]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError as error:
        raise DataValidationError(f"missing expected file: {path.name}") from error
    rows: list[dict] = []
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            raise DataValidationError(
                f"{path.name}:{line_number}: invalid or partially written JSON"
            ) from error
        if not isinstance(row, dict):
            raise DataValidationError(f"{path.name}:{line_number}: expected a JSON object")
        rows.append(row)
    return rows


def _finite_number(value: object, *, location: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise DataValidationError(f"{location}: expected a numeric value")
    numeric = float(value)
    if not math.isfinite(numeric):
        raise DataValidationError(f"{location}: expected a finite value")
    return numeric


def _close(left: float, right: float) -> bool:
    return math.isclose(left, right, rel_tol=FLOAT_REL_TOL, abs_tol=FLOAT_ABS_TOL)


def _method_from_fixed_filename(path: Path) -> str:
    for method in METHODS:
        if path.name in {f"{method}_summary.json", f"{method}_details.jsonl"}:
            return method
    raise DataValidationError(f"unrecognized baseline filename: {path.name}")


def _validate_ranker_field(payload: dict, *, path: Path, location: str) -> None:
    expected = _method_from_fixed_filename(path)
    raw = payload.get("ranker")
    if raw is None or str(raw).strip() == "":
        if expected != "repomap" or path.name not in {
            "repomap_summary.json",
            "repomap_details.jsonl",
        }:
            raise DataValidationError(
                f"{location}: blank ranker is allowed only in fixed RepoMap filenames"
            )
        return
    if str(raw).strip().lower() != expected:
        raise DataValidationError(
            f"{location}: ranker {raw!r} conflicts with fixed filename method {expected!r}"
        )


def _canonical_sample_list_sha256(samples: list[dict]) -> str:
    rendered = "".join(
        f"{sample['release_id']}\t{sample['sample_id']}\n"
        for sample in sorted(samples, key=lambda item: int(item["pilot_index"]))
    )
    return _sha256_bytes(rendered.encode("utf-8"))


def _load_selection_manifest(path: Path) -> tuple[dict, bytes, dict[str, list[dict]]]:
    try:
        raw_bytes = path.read_bytes()
    except FileNotFoundError as error:
        raise DataValidationError(f"missing tracked selection manifest: {path.name}") from error
    try:
        manifest = json.loads(raw_bytes.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise DataValidationError("tracked selection manifest is not valid UTF-8 JSON") from error
    if not isinstance(manifest, dict) or not isinstance(manifest.get("samples"), list):
        raise DataValidationError("selection manifest must contain a samples list")
    samples = manifest["samples"]
    if manifest.get("sample_count") != len(samples):
        raise DataValidationError("selection manifest sample_count does not match samples length")

    required = {
        "pilot_index",
        "within_release_index",
        "release_id",
        "task_type",
        "sample_id",
        "repo",
        "base_commit",
    }
    global_ids: set[str] = set()
    pilot_indexes: set[int] = set()
    by_release: dict[str, list[dict]] = {release: [] for release in RELEASES}
    for position, sample in enumerate(samples, start=1):
        if not isinstance(sample, dict):
            raise DataValidationError(f"selection sample {position}: expected an object")
        missing = required.difference(sample)
        if missing:
            raise DataValidationError(
                f"selection sample {position}: missing fields {sorted(missing)}"
            )
        release = str(sample["release_id"])
        if release not in RELEASES:
            raise DataValidationError(f"selection sample {position}: unexpected release {release!r}")
        expected_task = TASK_TYPES[release]
        if str(sample["task_type"]) != expected_task:
            raise DataValidationError(
                f"selection sample {position}: task_type does not match {release}"
            )
        sample_id = str(sample["sample_id"])
        if not sample_id:
            raise DataValidationError(f"selection sample {position}: blank sample_id")
        if sample_id in global_ids:
            raise DataValidationError(f"duplicate sample_id in selection manifest: {sample_id}")
        global_ids.add(sample_id)
        pilot_index = int(sample["pilot_index"])
        if pilot_index in pilot_indexes:
            raise DataValidationError(f"duplicate pilot_index in selection manifest: {pilot_index}")
        pilot_indexes.add(pilot_index)
        by_release[release].append(sample)

    if pilot_indexes != set(range(1, len(samples) + 1)):
        raise DataValidationError("selection manifest pilot_index values are not contiguous")
    for release, release_samples in by_release.items():
        within = {int(sample["within_release_index"]) for sample in release_samples}
        if within != set(range(1, len(release_samples) + 1)):
            raise DataValidationError(
                f"selection manifest within_release_index values are not contiguous for {release}"
            )
        release_samples.sort(key=lambda item: int(item["within_release_index"]))

    declared_counts = manifest.get("counts_by_task_type")
    if not isinstance(declared_counts, dict):
        raise DataValidationError("selection manifest lacks counts_by_task_type")
    for release in RELEASES:
        task_type = TASK_TYPES[release]
        if declared_counts.get(task_type) != len(by_release[release]):
            raise DataValidationError(
                f"selection manifest count mismatch for task_type {task_type}"
            )
    return manifest, raw_bytes, by_release


def _expected_result_files() -> set[str]:
    return {
        name
        for method in METHODS
        for name in (f"{method}_summary.json", f"{method}_details.jsonl")
    }


def _validate_release_files(release_dir: Path) -> None:
    if not release_dir.is_dir():
        raise DataValidationError(f"missing expected release directory: {release_dir.name}")
    expected = _expected_result_files()
    observed = {
        path.name
        for path in release_dir.iterdir()
        if path.is_file()
        and (path.name.endswith("_summary.json") or path.name.endswith("_details.jsonl"))
    }
    missing = sorted(expected.difference(observed))
    unexpected = sorted(observed.difference(expected))
    if missing:
        raise DataValidationError(
            f"{release_dir.name}: missing expected result files {missing}"
        )
    if unexpected:
        raise DataValidationError(
            f"{release_dir.name}: unexpected result files {unexpected}"
        )


def _extract_key_metrics(payload: dict, *, location: str) -> dict[str, float]:
    metrics: dict[str, float] = {}
    for metric in KEY_METRICS:
        if metric not in payload:
            raise DataValidationError(f"{location}: missing key metric {metric}")
        metrics[metric] = _finite_number(payload[metric], location=f"{location}.{metric}")
    coverage = metrics["gold_coverage@8k"]
    if coverage < -FLOAT_ABS_TOL or coverage > 1.0 + FLOAT_ABS_TOL:
        raise DataValidationError(f"{location}.gold_coverage@8k: expected a value in [0,1]")
    return metrics


def _output_key_metrics(raw_metrics: dict[str, float]) -> dict[str, float]:
    return {
        OUTPUT_METRIC_NAMES[metric]: raw_metrics[metric] for metric in KEY_METRICS
    }


def _load_method_result(
    release_dir: Path,
    *,
    release: str,
    method: str,
    selection_samples: list[dict],
) -> tuple[dict, dict[str, dict]]:
    summary_path = release_dir / f"{method}_summary.json"
    details_path = release_dir / f"{method}_details.jsonl"
    summary = _read_json(summary_path)
    _validate_ranker_field(summary, path=summary_path, location=summary_path.name)
    rows = _read_jsonl(details_path)

    expected_by_id = {str(sample["sample_id"]): sample for sample in selection_samples}
    rows_by_id: dict[str, dict] = {}
    for line_number, row in enumerate(rows, start=1):
        location = f"{details_path.name}:{line_number}"
        _validate_ranker_field(row, path=details_path, location=location)
        sample_id = str(row.get("sample_id", ""))
        if not sample_id:
            raise DataValidationError(f"{location}: missing sample_id")
        if sample_id in rows_by_id:
            raise DataValidationError(
                f"{details_path.name}: duplicate sample_id {sample_id}"
            )
        rows_by_id[sample_id] = row
        expected = expected_by_id.get(sample_id)
        if expected is None:
            raise DataValidationError(
                f"{details_path.name}: sample_id {sample_id} is not in tracked selection"
            )
        if str(row.get("task_type")) != TASK_TYPES[release]:
            raise DataValidationError(f"{location}: task_type does not match {release}")
        if str(row.get("repo")) != str(expected["repo"]):
            raise DataValidationError(f"{location}: repo conflicts with tracked selection")
        if str(row.get("base_commit")) != str(expected["base_commit"]):
            raise DataValidationError(
                f"{location}: base_commit conflicts with tracked selection"
            )
        if not isinstance(row.get("metrics"), dict):
            raise DataValidationError(f"{location}: missing metrics object")
        _extract_key_metrics(row["metrics"], location=f"{location}.metrics")

    observed_ids = set(rows_by_id)
    expected_ids = set(expected_by_id)
    missing_ids = sorted(expected_ids.difference(observed_ids))
    extra_ids = sorted(observed_ids.difference(expected_ids))
    if missing_ids or extra_ids:
        raise DataValidationError(
            f"{details_path.name}: sample IDs do not match tracked selection; "
            f"missing={missing_ids}, extra={extra_ids}"
        )

    if summary.get("evaluated") != len(selection_samples):
        raise DataValidationError(
            f"{summary_path.name}: evaluated does not match tracked sample count"
        )
    if summary.get("skipped") not in ({}, None):
        raise DataValidationError(f"{summary_path.name}: skipped must be empty")
    summary_metrics = summary.get("metrics")
    if not isinstance(summary_metrics, dict):
        raise DataValidationError(f"{summary_path.name}: missing metrics object")
    overall = summary_metrics.get("overall")
    task_metrics = summary_metrics.get(TASK_TYPES[release])
    if not isinstance(overall, dict) or not isinstance(task_metrics, dict):
        raise DataValidationError(
            f"{summary_path.name}: missing overall or release-task metrics"
        )
    if overall.get("samples") != len(selection_samples):
        raise DataValidationError(
            f"{summary_path.name}: metrics.overall.samples does not match selection"
        )
    if task_metrics.get("samples") != len(selection_samples):
        raise DataValidationError(
            f"{summary_path.name}: task metrics samples does not match selection"
        )
    overall_key_metrics = _extract_key_metrics(
        overall, location=f"{summary_path.name}.metrics.overall"
    )
    task_key_metrics = _extract_key_metrics(
        task_metrics, location=f"{summary_path.name}.metrics.{TASK_TYPES[release]}"
    )
    for metric in KEY_METRICS:
        detail_mean = mean(
            _finite_number(
                rows_by_id[sample_id]["metrics"][metric],
                location=f"{details_path.name}.{sample_id}.{metric}",
            )
            for sample_id in sorted(rows_by_id)
        )
        if not _close(overall_key_metrics[metric], detail_mean):
            raise DataValidationError(
                f"{summary_path.name}: {metric} differs from detail mean "
                f"({overall_key_metrics[metric]} != {detail_mean})"
            )
        if not _close(overall_key_metrics[metric], task_key_metrics[metric]):
            raise DataValidationError(
                f"{summary_path.name}: overall and task metric differ for {metric}"
            )

    return (
        {
            "summary_file": summary_path.name,
            "details_file": details_path.name,
            "evaluated": len(selection_samples),
            "key_metrics": _output_key_metrics(overall_key_metrics),
        },
        rows_by_id,
    )


def _legacy_all_gold_files_packed(value: float) -> bool:
    return value >= 1.0 - FLOAT_ABS_TOL


def _is_zero_coverage(value: float) -> bool:
    return abs(value) <= FLOAT_ABS_TOL


def _task_coverage_record(
    sample: dict,
    method_rows: dict[str, dict[str, dict]],
) -> dict:
    sample_id = str(sample["sample_id"])
    gold_by_method: dict[str, list[str]] = {}
    top20_by_method: dict[str, set[str]] = {}
    recall20_by_method: dict[str, float] = {}
    for method in METHODS:
        row = method_rows[method][sample_id]
        gold_raw = row.get("gold_files")
        top_raw = row.get("top_files")
        if not isinstance(gold_raw, list) or not gold_raw:
            raise DataValidationError(f"{sample_id}.{method}: gold_files must be nonempty")
        if not isinstance(top_raw, list):
            raise DataValidationError(f"{sample_id}.{method}: top_files must be a list")
        gold = [str(path) for path in gold_raw]
        top20 = [str(path) for path in top_raw[:20]]
        if any(not path for path in gold + top20):
            raise DataValidationError(f"{sample_id}.{method}: blank file path")
        if len(set(gold)) != len(gold):
            raise DataValidationError(f"{sample_id}.{method}: duplicate gold file")
        gold_by_method[method] = gold
        top20_by_method[method] = set(top20)

    canonical_gold = set(gold_by_method[METHODS[0]])
    for method in METHODS[1:]:
        if set(gold_by_method[method]) != canonical_gold:
            raise DataValidationError(
                f"{sample_id}: gold_files differ across baseline methods"
            )
    for method in METHODS:
        observed = len(canonical_gold.intersection(top20_by_method[method])) / len(
            canonical_gold
        )
        reported = _finite_number(
            method_rows[method][sample_id]["metrics"]["Recall@20"],
            location=f"{sample_id}.{method}.Recall@20",
        )
        if not _close(observed, reported):
            raise DataValidationError(
                f"{sample_id}.{method}: top_files-derived Recall@20 differs from metrics"
            )
        recall20_by_method[method] = observed
    union_top20 = set().union(*(top20_by_method[method] for method in METHODS))
    union_fraction = len(canonical_gold.intersection(union_top20)) / len(canonical_gold)
    best_single_fraction = max(recall20_by_method.values())

    legacy_fraction = {
        method: _finite_number(
            method_rows[method][sample_id]["metrics"]["gold_coverage@8k"],
            location=f"{sample['sample_id']}.{method}.gold_coverage@8k",
        )
        for method in METHODS
    }
    all_gold_methods = [
        method
        for method in METHODS
        if _legacy_all_gold_files_packed(legacy_fraction[method])
    ]
    all_gold_flags = {method: method in all_gold_methods for method in METHODS}
    unique = all_gold_methods[0] if len(all_gold_methods) == 1 else None
    return {
        "pilot_index": int(sample["pilot_index"]),
        "within_release_index": int(sample["within_release_index"]),
        "sample_id": str(sample["sample_id"]),
        "repo": str(sample["repo"]),
        "base_commit": str(sample["base_commit"]),
        "legacy_gold_file_fraction@8k_chars": legacy_fraction,
        "legacy_all_gold_files_packed@8k_chars": all_gold_flags,
        "legacy_all_gold_files_methods": all_gold_methods,
        "legacy_all_gold_files_pattern": "+".join(all_gold_methods) if all_gold_methods else "none",
        "exclusive_legacy_all_gold_files_method": unique,
        "any_method_legacy_all_gold_files_packed": bool(all_gold_methods),
        "all_methods_legacy_all_gold_files_packed": len(all_gold_methods) == len(METHODS),
        "no_method_legacy_all_gold_files_packed": not all_gold_methods,
        "all_methods_zero_legacy_gold_file_fraction": all(
            _is_zero_coverage(value) for value in legacy_fraction.values()
        ),
        "legacy_all_gold_files_outcomes_differ": 0
        < len(all_gold_methods)
        < len(METHODS),
        "unbounded_top20_union_diagnostic": {
            "gold_file_count": len(canonical_gold),
            "method_gold_fraction@20": recall20_by_method,
            "best_single_gold_fraction@20": best_single_fraction,
            "unbounded_union_gold_fraction@20": union_fraction,
            "unbounded_union_gain_over_best_single": union_fraction
            - best_single_fraction,
            "all_methods_miss_all_gold@20": best_single_fraction <= FLOAT_ABS_TOL,
            "any_single_covers_all_gold@20": best_single_fraction
            >= 1.0 - FLOAT_ABS_TOL,
            "unbounded_union_covers_all_gold@20": union_fraction
            >= 1.0 - FLOAT_ABS_TOL,
            "unbounded_union_strictly_improves": union_fraction
            > best_single_fraction + FLOAT_ABS_TOL,
        },
    }


def _coverage_aggregate(tasks: list[dict]) -> dict:
    count = len(tasks)

    def total(field: str) -> int:
        return sum(bool(task[field]) for task in tasks)

    pattern_counts: dict[str, int] = {}
    for task in tasks:
        pattern = task["legacy_all_gold_files_pattern"]
        pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
    exclusive_counts = {
        method: sum(
            task["exclusive_legacy_all_gold_files_method"] == method for task in tasks
        )
        for method in METHODS
    }
    method_full = {
        method: sum(
            task["legacy_all_gold_files_packed@8k_chars"][method] for task in tasks
        )
        for method in METHODS
    }
    pairwise: dict[str, dict] = {}
    for left_index, left in enumerate(METHODS):
        for right in METHODS[left_index + 1 :]:
            left_only = sum(
                task["legacy_all_gold_files_packed@8k_chars"][left]
                and not task["legacy_all_gold_files_packed@8k_chars"][right]
                for task in tasks
            )
            right_only = sum(
                task["legacy_all_gold_files_packed@8k_chars"][right]
                and not task["legacy_all_gold_files_packed@8k_chars"][left]
                for task in tasks
            )
            both = sum(
                task["legacy_all_gold_files_packed@8k_chars"][left]
                and task["legacy_all_gold_files_packed@8k_chars"][right]
                for task in tasks
            )
            pairwise[f"{left}__{right}"] = {
                f"{left}_only": left_only,
                f"{right}_only": right_only,
                "both_legacy_all_gold_files": both,
                "neither_legacy_all_gold_files": count
                - left_only
                - right_only
                - both,
            }

    def with_rate(value: int) -> dict:
        return {"count": value, "rate": value / count if count else None}

    return {
        "task_count": count,
        "method_legacy_all_gold_files_packed": {
            method: with_rate(value) for method, value in method_full.items()
        },
        "any_method_legacy_all_gold_files_packed": with_rate(
            total("any_method_legacy_all_gold_files_packed")
        ),
        "all_methods_legacy_all_gold_files_packed": with_rate(
            total("all_methods_legacy_all_gold_files_packed")
        ),
        "no_method_legacy_all_gold_files_packed": with_rate(
            total("no_method_legacy_all_gold_files_packed")
        ),
        "all_methods_zero_legacy_gold_file_fraction": with_rate(
            total("all_methods_zero_legacy_gold_file_fraction")
        ),
        "legacy_all_gold_files_outcomes_differ": with_rate(
            total("legacy_all_gold_files_outcomes_differ")
        ),
        "exclusive_legacy_all_gold_files_packed": {
            method: with_rate(value) for method, value in exclusive_counts.items()
        },
        "legacy_all_gold_files_pattern_counts": dict(sorted(pattern_counts.items())),
        "pairwise_legacy_all_gold_files": pairwise,
    }


def _top20_union_aggregate(tasks: list[dict]) -> dict:
    count = len(tasks)
    diagnostics = [task["unbounded_top20_union_diagnostic"] for task in tasks]

    def with_rate(value: int) -> dict:
        return {"count": value, "rate": value / count if count else None}

    def total(field: str) -> int:
        return sum(bool(item[field]) for item in diagnostics)

    mean_best = mean(item["best_single_gold_fraction@20"] for item in diagnostics)
    mean_union = mean(item["unbounded_union_gold_fraction@20"] for item in diagnostics)
    return {
        "task_count": count,
        "all_methods_miss_all_gold@20": with_rate(
            total("all_methods_miss_all_gold@20")
        ),
        "any_single_covers_all_gold@20": with_rate(
            total("any_single_covers_all_gold@20")
        ),
        "unbounded_union_covers_all_gold@20": with_rate(
            total("unbounded_union_covers_all_gold@20")
        ),
        "unbounded_union_strictly_improves": with_rate(
            total("unbounded_union_strictly_improves")
        ),
        "mean_best_single_gold_fraction@20": mean_best,
        "mean_unbounded_union_gold_fraction@20": mean_union,
        "mean_unbounded_union_gain": mean_union - mean_best,
        "interpretation_guardrail": TOP20_UNION_WARNING,
    }


def summarize(
    eval_root: Path,
    selection_manifest: Path,
    *,
    releases: Iterable[str] = RELEASES,
) -> dict:
    requested = tuple(releases)
    if not requested or len(set(requested)) != len(requested):
        raise DataValidationError("requested releases must be nonempty and unique")
    unknown = set(requested).difference(RELEASES)
    if unknown:
        raise DataValidationError(f"unknown requested releases: {sorted(unknown)}")
    ordered_releases = tuple(release for release in RELEASES if release in requested)

    manifest, manifest_bytes, selection_by_release = _load_selection_manifest(
        selection_manifest
    )
    report_releases: dict[str, dict] = {}
    all_task_records: list[dict] = []
    for release in ordered_releases:
        release_dir = eval_root / release
        _validate_release_files(release_dir)
        method_reports: dict[str, dict] = {}
        method_rows: dict[str, dict[str, dict]] = {}
        for method in METHODS:
            method_report, rows_by_id = _load_method_result(
                release_dir,
                release=release,
                method=method,
                selection_samples=selection_by_release[release],
            )
            method_reports[method] = method_report
            method_rows[method] = rows_by_id
        task_records = [
            _task_coverage_record(sample, method_rows)
            for sample in selection_by_release[release]
        ]
        all_task_records.extend(task_records)
        report_releases[release] = {
            "task_type": TASK_TYPES[release],
            "sample_count": len(task_records),
            "methods": method_reports,
            "legacy_8k_character_packing": _coverage_aggregate(task_records),
            "unbounded_top20_union_diagnostic": _top20_union_aggregate(task_records),
            "tasks": task_records,
        }

    release_macro = {
        method: {
            metric: mean(
                report_releases[release]["methods"][method]["key_metrics"][metric]
                for release in ordered_releases
            )
            for metric in OUTPUT_KEY_METRICS
        }
        for method in METHODS
    }
    samples = manifest["samples"]
    return {
        "schema_version": 1,
        "report_kind": "descriptive_arb_baseline_grid_summary",
        "interpretation_guardrail": (
            "Descriptive validation and aggregation only; no causal effect, "
            "statistical superiority, or new-algorithm victory is inferred. "
            + LEGACY_PACKING_WARNING
            + " "
            + TOP20_UNION_WARNING
        ),
        "metric_provenance": {
            "legacy_gold_file_fraction@8k_chars": {
                "source_field": "gold_coverage@8k",
                "packing_budget": 8000,
                "packing_unit": "characters",
                "canonical_token_bcy": False,
            },
            "legacy_context_efficiency@8k_chars": {
                "source_field": "context_efficiency@8k",
                "packing_budget": 8000,
                "packing_unit": "characters",
                "canonical_token_bcy": False,
            },
            "canonical_bcy_included": False,
            "warning": LEGACY_PACKING_WARNING,
        },
        "validated_releases": list(ordered_releases),
        "expected_methods": list(METHODS),
        "complete_three_by_three_design": set(ordered_releases) == set(RELEASES),
        "sample_manifest": {
            "file_name": selection_manifest.name,
            "file_sha256": _sha256_bytes(manifest_bytes),
            "canonical_release_sample_id_list_sha256": _canonical_sample_list_sha256(
                samples
            ),
            "tracked_sample_count": len(samples),
            "validated_sample_count": sum(
                len(selection_by_release[release]) for release in ordered_releases
            ),
        },
        "releases": report_releases,
        "macro": {
            "definition": "unweighted arithmetic mean of each release-level official summary metric",
            "release_count": len(ordered_releases),
            "sample_count": len(all_task_records),
            "method_key_metrics": release_macro,
            "legacy_8k_character_packing": _coverage_aggregate(all_task_records),
            "unbounded_top20_union_diagnostic": _top20_union_aggregate(
                all_task_records
            ),
        },
    }


def _format_metric(value: float, metric: str) -> str:
    if metric == "context_pollution_tokens@8k":
        return f"{value:.1f}"
    return f"{value:.4f}"


def render_markdown(report: dict) -> str:
    lines = [
        "# ARB frozen-baseline descriptive summary",
        "",
        "> This report is descriptive validation and aggregation only. It does not establish causality, statistical superiority, or a new-algorithm win.",
        "> The legacy `gold_coverage@8k` and `context_efficiency@8k` source fields use 8,000-character packing. They are not canonical token-packed BCY; canonical BCY requires the official token-based reporting path.",
        "",
        f"- Validated releases: {', '.join(report['validated_releases'])}",
        f"- Methods: {', '.join(report['expected_methods'])}",
        f"- Tracked manifest SHA256: `{report['sample_manifest']['file_sha256']}`",
        f"- Canonical release/sample-ID list SHA256: `{report['sample_manifest']['canonical_release_sample_id_list_sha256']}`",
        "",
        "## Release-level official metrics",
        "",
        "| Release | Method | N | MRR | Recall@20 | F0.5@10 | Coverage AUC@20 | Legacy gold-file fraction@8K chars | Legacy context efficiency@8K chars | Pollution tokens@8K |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for release in report["validated_releases"]:
        release_report = report["releases"][release]
        for method in METHODS:
            metrics = release_report["methods"][method]["key_metrics"]
            lines.append(
                "| "
                + " | ".join(
                    [
                        release,
                        method,
                        str(release_report["methods"][method]["evaluated"]),
                        _format_metric(metrics["MRR"], "MRR"),
                        _format_metric(metrics["Recall@20"], "Recall@20"),
                        _format_metric(metrics["F0.5@10"], "F0.5@10"),
                        _format_metric(metrics["coverage_auc@20"], "coverage_auc@20"),
                        _format_metric(
                            metrics["legacy_gold_file_fraction@8k_chars"],
                            "legacy_gold_file_fraction@8k_chars",
                        ),
                        _format_metric(
                            metrics["legacy_context_efficiency@8k_chars"],
                            "legacy_context_efficiency@8k_chars",
                        ),
                        _format_metric(
                            metrics["context_pollution_tokens@8k"],
                            "context_pollution_tokens@8k",
                        ),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## Unweighted release macro",
            "",
            "| Method | MRR | Recall@20 | F0.5@10 | Coverage AUC@20 | Legacy gold-file fraction@8K chars | Legacy context efficiency@8K chars | Pollution tokens@8K |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for method in METHODS:
        metrics = report["macro"]["method_key_metrics"][method]
        lines.append(
            "| "
            + " | ".join(
                [
                    method,
                    _format_metric(metrics["MRR"], "MRR"),
                    _format_metric(metrics["Recall@20"], "Recall@20"),
                    _format_metric(metrics["F0.5@10"], "F0.5@10"),
                    _format_metric(metrics["coverage_auc@20"], "coverage_auc@20"),
                    _format_metric(
                        metrics["legacy_gold_file_fraction@8k_chars"],
                        "legacy_gold_file_fraction@8k_chars",
                    ),
                    _format_metric(
                        metrics["legacy_context_efficiency@8k_chars"],
                        "legacy_context_efficiency@8k_chars",
                    ),
                    _format_metric(
                        metrics["context_pollution_tokens@8k"],
                        "context_pollution_tokens@8k",
                    ),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Descriptive legacy 8K-character packing patterns",
            "",
            "`No all-gold` means no method packed every gold file under the legacy 8,000-character rule; `all zero` means every method had a zero legacy gold-file fraction. `Mixed` records differing all-gold-file events and is neither canonical BCY nor a causal complementarity estimate.",
            "",
            "| Scope | Tasks | Any all-gold | All methods all-gold | No all-gold | All zero | Mixed |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    coverage_scopes = [
        (release, report["releases"][release]["legacy_8k_character_packing"])
        for release in report["validated_releases"]
    ] + [("macro", report["macro"]["legacy_8k_character_packing"])]
    for label, coverage in coverage_scopes:
        lines.append(
            "| "
            + " | ".join(
                [
                    label,
                    str(coverage["task_count"]),
                    str(coverage["any_method_legacy_all_gold_files_packed"]["count"]),
                    str(coverage["all_methods_legacy_all_gold_files_packed"]["count"]),
                    str(coverage["no_method_legacy_all_gold_files_packed"]["count"]),
                    str(coverage["all_methods_zero_legacy_gold_file_fraction"]["count"]),
                    str(coverage["legacy_all_gold_files_outcomes_differ"]["count"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Descriptive unbounded top-20 union diagnostic",
            "",
            TOP20_UNION_WARNING,
            "",
            "| Scope | Tasks | All three miss | Union strictly adds gold | Any single covers all gold | Union covers all gold | Mean best-single fraction | Mean union fraction |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    union_scopes = [
        (release, report["releases"][release]["unbounded_top20_union_diagnostic"])
        for release in report["validated_releases"]
    ] + [("macro", report["macro"]["unbounded_top20_union_diagnostic"])]
    for label, diagnostic in union_scopes:
        lines.append(
            "| "
            + " | ".join(
                [
                    label,
                    str(diagnostic["task_count"]),
                    str(diagnostic["all_methods_miss_all_gold@20"]["count"]),
                    str(diagnostic["unbounded_union_strictly_improves"]["count"]),
                    str(diagnostic["any_single_covers_all_gold@20"]["count"]),
                    str(diagnostic["unbounded_union_covers_all_gold@20"]["count"]),
                    f"{diagnostic['mean_best_single_gold_fraction@20']:.4f}",
                    f"{diagnostic['mean_unbounded_union_gold_fraction@20']:.4f}",
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _validate_output_targets(
    *,
    eval_root: Path,
    selection_manifest: Path,
    json_output: Path,
    markdown_output: Path,
) -> None:
    eval_resolved = eval_root.resolve()
    manifest_resolved = selection_manifest.resolve()
    json_resolved = json_output.resolve()
    markdown_resolved = markdown_output.resolve()
    if json_resolved == markdown_resolved:
        raise DataValidationError("JSON and Markdown outputs must be different files")
    for output in (json_resolved, markdown_resolved):
        if output == manifest_resolved or output.is_relative_to(eval_resolved):
            raise DataValidationError(
                "report outputs may not overwrite the tracked manifest or official eval root"
            )
        if not output.parent.is_dir():
            raise DataValidationError(f"output parent does not exist: {output.parent}")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("eval_root", type=Path)
    parser.add_argument("selection_manifest", type=Path)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    try:
        report = summarize(args.eval_root, args.selection_manifest)
        _validate_output_targets(
            eval_root=args.eval_root,
            selection_manifest=args.selection_manifest,
            json_output=args.json_output,
            markdown_output=args.markdown_output,
        )
    except DataValidationError as error:
        raise SystemExit(f"ARB baseline summary validation failed: {error}") from error
    with args.json_output.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        )
    with args.markdown_output.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(render_markdown(report))


if __name__ == "__main__":
    main()
