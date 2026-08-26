"""Aggregate the frozen ARB60 typed-retrieval development discovery run.

The report is deliberately conservative.  Its primary typed output is the
gold-blind selection recorded in ``deployment_query_only_output`` at executor
revision 14d00c5b.  ``best_found_posthoc_oracle`` is reported only as an oracle
ceiling.  Every effectiveness denominator is all 60 positive tasks, including
ABSTAIN and scoped UNSAT rows, whose query-only score is zero.

The official ARB baseline summary is used for provenance and Recall@20
cross-checks only.  Its legacy 8,000-character fields are never treated as
canonical token-packed BCY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
import time
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


EXECUTOR_FROZEN_REVISION = "14d00c5b"
EXPECTED_SAMPLE_COUNT = 60
EXPECTED_TASK_COUNTS = {
    "code2test": 20,
    "edit2ripple": 20,
    "trace2code": 20,
}
TASK_RELEASE = {
    "code2test": "v2_code2test",
    "edit2ripple": "v2_edit2ripple",
    "trace2code": "v2_trace2code",
}
SINGLE_BASELINES = ("lexical", "bm25", "repomap")
BASELINES = (*SINGLE_BASELINES, "rrf_equal_cost_hybrid")
PRIMARY_BCY = "canonical_bcy@8000_tokens"
CANONICAL_TOKENIZER = "regex_code_tokenizer_v1"
CANONICAL_THRESHOLDS = {"1", "16", "32", "64", "128"}
TOLERANCE = 1e-12


class DiscoveryValidationError(ValueError):
    """Raised before reporting when an input is missing or inconsistent."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise DiscoveryValidationError(message)


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    _require(isinstance(value, Mapping), f"{label} must be an object")
    return value


def _list(value: Any, label: str) -> list[Any]:
    _require(isinstance(value, list), f"{label} must be a list")
    return value


def _number(value: Any, label: str) -> float:
    _require(isinstance(value, (int, float)) and not isinstance(value, bool), f"{label} must be numeric")
    result = float(value)
    _require(math.isfinite(result), f"{label} must be finite")
    return result


def _integer(value: Any, label: str) -> int:
    _require(isinstance(value, int) and not isinstance(value, bool), f"{label} must be an integer")
    return int(value)


def _read_json(path: Path) -> Mapping[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise DiscoveryValidationError(f"cannot read JSON {path}: {exc}") from exc
    return _mapping(value, str(path))


def _read_jsonl(path: Path) -> list[Mapping[str, Any]]:
    rows: list[Mapping[str, Any]] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    value = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise DiscoveryValidationError(
                        f"invalid JSONL at {path}:{line_number}: {exc}"
                    ) from exc
                rows.append(_mapping(value, f"{path}:{line_number}"))
    except OSError as exc:
        raise DiscoveryValidationError(f"cannot read JSONL {path}: {exc}") from exc
    return rows


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
    except OSError as exc:
        raise DiscoveryValidationError(f"cannot hash {path}: {exc}") from exc
    return digest.hexdigest()


def _normal_path(value: str) -> str:
    normalized = value.replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _dedupe_paths(values: Iterable[Any], label: str) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        _require(isinstance(value, str) and value, f"{label} contains a non-path value")
        path = _normal_path(value)
        _require(path not in seen, f"{label} contains duplicate path {path!r}")
        output.append(path)
        seen.add(path)
    return output


def _close(left: float, right: float) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=TOLERANCE)


def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _rate(count: int, denominator: int) -> dict[str, Any]:
    return {
        "count": count,
        "denominator": denominator,
        "rate": count / denominator if denominator else None,
    }


def _distribution(values: Sequence[float]) -> dict[str, Any]:
    if not values:
        return {
            "count": 0,
            "total": 0.0,
            "mean": None,
            "median": None,
            "p95_nearest_rank": None,
            "max": None,
        }
    ordered = sorted(float(value) for value in values)
    p95_index = max(0, math.ceil(0.95 * len(ordered)) - 1)
    return {
        "count": len(ordered),
        "total": sum(ordered),
        "mean": _mean(ordered),
        "median": statistics.median(ordered),
        "p95_nearest_rank": ordered[p95_index],
        "max": ordered[-1],
    }


def _count_distribution(values: Iterable[Any]) -> dict[str, int]:
    return {str(key): count for key, count in sorted(Counter(values).items(), key=lambda item: str(item[0]))}


def _validate_manifest(raw: Mapping[str, Any], manifest_sha: str) -> list[Mapping[str, Any]]:
    rows = _list(raw.get("samples"), "manifest.samples")
    _require(raw.get("sample_count") == EXPECTED_SAMPLE_COUNT, "manifest sample_count must be 60")
    _require(len(rows) == EXPECTED_SAMPLE_COUNT, "manifest must contain exactly 60 samples")
    declared_counts = _mapping(raw.get("counts_by_task_type"), "manifest.counts_by_task_type")
    _require(dict(declared_counts) == EXPECTED_TASK_COUNTS, "manifest task counts must be 20/20/20")

    ordered = sorted(
        (_mapping(row, "manifest sample") for row in rows),
        key=lambda row: _integer(row.get("pilot_index"), "manifest pilot_index"),
    )
    observed_ids: set[str] = set()
    observed_counts: Counter[str] = Counter()
    for expected_index, row in enumerate(ordered, start=1):
        _require(row.get("pilot_index") == expected_index, "manifest pilot_index must be contiguous 1..60")
        sample_id = row.get("sample_id")
        task_type = row.get("task_type")
        _require(isinstance(sample_id, str) and sample_id, f"manifest sample {expected_index} has no sample_id")
        _require(sample_id not in observed_ids, f"duplicate manifest sample_id {sample_id}")
        _require(task_type in EXPECTED_TASK_COUNTS, f"unsupported manifest task_type {task_type!r}")
        _require(row.get("release_id") == TASK_RELEASE[task_type], f"manifest release mismatch for {sample_id}")
        _require(isinstance(row.get("repo"), str) and row.get("repo"), f"manifest repo missing for {sample_id}")
        _require(
            isinstance(row.get("base_commit"), str) and row.get("base_commit"),
            f"manifest base_commit missing for {sample_id}",
        )
        observed_ids.add(sample_id)
        observed_counts[task_type] += 1
    _require(dict(observed_counts) == EXPECTED_TASK_COUNTS, "observed manifest strata are not 20/20/20")
    _require(len(manifest_sha) == 64, "manifest SHA256 is malformed")
    return ordered


def _validate_official_report(
    raw: Mapping[str, Any],
    manifest_rows: Sequence[Mapping[str, Any]],
    manifest_sha: str,
) -> dict[str, Mapping[str, Any]]:
    _require(raw.get("complete_three_by_three_design") is True, "official baseline grid is incomplete")
    _require(set(_list(raw.get("expected_methods"), "official.expected_methods")) == set(SINGLE_BASELINES), "official methods mismatch")
    _require(set(_list(raw.get("validated_releases"), "official.validated_releases")) == set(TASK_RELEASE.values()), "official releases mismatch")
    sample_manifest = _mapping(raw.get("sample_manifest"), "official.sample_manifest")
    _require(sample_manifest.get("file_sha256") == manifest_sha, "official report manifest SHA256 mismatch")
    _require(sample_manifest.get("tracked_sample_count") == EXPECTED_SAMPLE_COUNT, "official tracked count mismatch")
    _require(sample_manifest.get("validated_sample_count") == EXPECTED_SAMPLE_COUNT, "official validated count mismatch")
    provenance = _mapping(raw.get("metric_provenance"), "official.metric_provenance")
    _require(provenance.get("canonical_bcy_included") is False, "official report must remain legacy-only for BCY")

    releases = _mapping(raw.get("releases"), "official.releases")
    official_by_id: dict[str, Mapping[str, Any]] = {}
    for task_type, release in TASK_RELEASE.items():
        release_block = _mapping(releases.get(release), f"official.releases.{release}")
        _require(release_block.get("task_type") == task_type, f"official task_type mismatch in {release}")
        _require(release_block.get("sample_count") == 20, f"official sample count mismatch in {release}")
        methods = _mapping(release_block.get("methods"), f"official.releases.{release}.methods")
        _require(set(methods) == set(SINGLE_BASELINES), f"official method block mismatch in {release}")
        for method in SINGLE_BASELINES:
            _require(
                _mapping(methods[method], f"official {release} {method}").get("evaluated") == 20,
                f"official evaluated count mismatch for {release}/{method}",
            )
        tasks = _list(release_block.get("tasks"), f"official.releases.{release}.tasks")
        _require(len(tasks) == 20, f"official task list mismatch in {release}")
        for value in tasks:
            row = _mapping(value, f"official task in {release}")
            sample_id = row.get("sample_id")
            _require(isinstance(sample_id, str) and sample_id, f"official sample id missing in {release}")
            _require(sample_id not in official_by_id, f"duplicate official sample_id {sample_id}")
            official_by_id[sample_id] = row

    _require(set(official_by_id) == {str(row["sample_id"]) for row in manifest_rows}, "official sample IDs do not match manifest")
    for manifest_row in manifest_rows:
        sample_id = str(manifest_row["sample_id"])
        official_row = official_by_id[sample_id]
        for field in ("pilot_index", "repo", "base_commit"):
            _require(official_row.get(field) == manifest_row.get(field), f"official {field} mismatch for {sample_id}")
    return official_by_id


def _load_gold_files(
    arb_data_root: Path,
    manifest_rows: Sequence[Mapping[str, Any]],
) -> dict[str, tuple[str, ...]]:
    desired_by_type: dict[str, dict[str, Mapping[str, Any]]] = {task_type: {} for task_type in TASK_RELEASE}
    for row in manifest_rows:
        desired_by_type[str(row["task_type"])][str(row["sample_id"])] = row

    gold_by_id: dict[str, tuple[str, ...]] = {}
    for task_type, release in TASK_RELEASE.items():
        path = arb_data_root / "pilot_eval" / release / "lexical_details.jsonl"
        desired = desired_by_type[task_type]
        seen: set[str] = set()
        for row in _read_jsonl(path):
            sample_id = row.get("sample_id")
            if sample_id not in desired:
                continue
            _require(sample_id not in seen, f"duplicate lexical detail row for {sample_id}")
            selected = desired[str(sample_id)]
            for field in ("task_type", "repo", "base_commit"):
                _require(row.get(field) == selected.get(field), f"lexical detail {field} mismatch for {sample_id}")
            gold = _dedupe_paths(_list(row.get("gold_files"), f"gold_files for {sample_id}"), f"gold_files for {sample_id}")
            _require(gold, f"positive sample {sample_id} has no gold files")
            gold_by_id[str(sample_id)] = tuple(gold)
            seen.add(str(sample_id))
        missing = set(desired) - seen
        _require(not missing, f"missing lexical gold rows for {sorted(missing)}")
    _require(len(gold_by_id) == EXPECTED_SAMPLE_COUNT, "gold join did not yield 60 samples")
    return gold_by_id


def _validated_score(value: Any, label: str) -> dict[str, Any]:
    score = _mapping(value, label)
    _require(score.get("oracle_only") is True, f"{label} must be explicitly oracle-only")
    _require(score.get("primary_metric") == PRIMARY_BCY, f"{label} primary metric mismatch")
    _require(score.get("tokenizer") == CANONICAL_TOKENIZER, f"{label} tokenizer mismatch")
    bcy = _number(score.get(PRIMARY_BCY), f"{label}.{PRIMARY_BCY}")
    recall = _number(score.get("file_recall"), f"{label}.file_recall")
    _require(-TOLERANCE <= bcy <= 1.0 + TOLERANCE, f"{label} BCY outside [0,1]")
    _require(-TOLERANCE <= recall <= 1.0 + TOLERANCE, f"{label} recall outside [0,1]")
    gold_count = _integer(score.get("gold_file_count"), f"{label}.gold_file_count")
    _require(gold_count > 0, f"{label} must score a positive task")
    thresholds = _mapping(
        score.get("canonical_bcy_by_min_content_tokens"),
        f"{label}.canonical_bcy_by_min_content_tokens",
    )
    _require(set(thresholds) == CANONICAL_THRESHOLDS, f"{label} canonical threshold set mismatch")
    _require(_close(_number(thresholds["1"], f"{label}.threshold1"), bcy), f"{label} threshold-1 BCY mismatch")
    missing_ranked = _integer(
        score.get("canonical_missing_ranked_files"),
        f"{label}.canonical_missing_ranked_files",
    )
    _require(missing_ranked >= 0, f"{label} missing-ranked count is negative")
    return {
        "bcy": bcy,
        "recall": recall,
        "gold_file_count": gold_count,
        "canonical_missing_ranked_files": missing_ranked,
    }


def _program_key(execution: Mapping[str, Any]) -> tuple[float, int, tuple[str, ...]]:
    program = _list(execution.get("program"), "execution.program")
    _require(all(isinstance(value, str) and value for value in program), "execution program IDs must be strings")
    return (
        _number(execution.get("cost_units"), "execution.cost_units"),
        _integer(execution.get("depth"), "execution.depth"),
        tuple(program),
    )


def _oracle_key(execution: Mapping[str, Any]) -> tuple[float, float, float, tuple[str, ...]]:
    score = _validated_score(execution.get("posthoc_score"), "execution.posthoc_score")
    program = tuple(_list(execution.get("program"), "execution.program"))
    return (score["bcy"], score["recall"], -_number(execution.get("cost_units"), "execution.cost_units"), program)


def _score_matches(left: Mapping[str, Any], right: Mapping[str, Any], label: str) -> None:
    for key in ("bcy", "recall"):
        _require(_close(float(left[key]), float(right[key])), f"{label} {key} mismatch")
    _require(left["gold_file_count"] == right["gold_file_count"], f"{label} gold count mismatch")


def _validate_execution_accounting(
    accounting: Mapping[str, Any],
    executions: Sequence[Mapping[str, Any]],
    label: str,
) -> dict[str, Any]:
    attempted = len(executions)
    certified = sum(row.get("status") == "EXECUTED" for row in executions)
    uncertified = sum(row.get("status") == "UNCERTIFIED_EVIDENCE" for row in executions)
    no_evidence = sum(row.get("status") == "NO_EVIDENCE" for row in executions)
    nominal = sum(_number(row.get("cost_units"), f"{label} execution cost") for row in executions)
    calls = sum(_integer(row.get("operator_calls"), f"{label} operator_calls") for row in executions)
    expected = {
        "attempted_candidate_count": attempted,
        "certified_executed_candidate_count": certified,
        "uncertified_candidate_count": uncertified,
        "no_evidence_candidate_count": no_evidence,
        "aggregate_nominal_cost_units": nominal,
        "aggregate_operator_calls": calls,
    }
    for key, expected_value in expected.items():
        actual = accounting.get(key)
        if isinstance(expected_value, float):
            _require(_close(_number(actual, f"{label}.{key}"), expected_value), f"{label}.{key} mismatch")
        else:
            _require(actual == expected_value, f"{label}.{key} mismatch")
    return expected


def _recover_canonical_baselines(
    arb_data_root: Path,
    manifest_row: Mapping[str, Any],
    gold_files: Sequence[str],
) -> tuple[dict[str, Mapping[str, Any]], dict[str, Any]]:
    """Recover canonical baselines for a query-only terminal compile row.

    The executor legitimately returns before constructing a store when no
    anchor program can be compiled.  That early row has no canonical baseline
    block.  Treating its baselines as zero would favor the typed method, so the
    aggregator rebuilds all four baselines from the three official detail
    lists and canonical kind=file corpus text.  Gold is used only by the final
    score call, after the ranked file lists are frozen.
    """

    # Import the pinned canonical packer rather than copying metric logic.
    from arb_typed_program_pilot import score_execution

    sample_id = str(manifest_row["sample_id"])
    task_type = str(manifest_row["task_type"])
    release = TASK_RELEASE[task_type]
    ranked: dict[str, list[str]] = {}
    for method in SINGLE_BASELINES:
        detail_path = arb_data_root / "pilot_eval" / release / f"{method}_details.jsonl"
        matches = [row for row in _read_jsonl(detail_path) if row.get("sample_id") == sample_id]
        _require(len(matches) == 1, f"baseline recovery requires exactly one {method} detail row for {sample_id}")
        row = matches[0]
        for field in ("task_type", "repo", "base_commit"):
            _require(row.get(field) == manifest_row.get(field), f"baseline recovery {field} mismatch for {sample_id}/{method}")
        files = _dedupe_paths(
            _list(row.get("top_files"), f"recovery {method}.top_files for {sample_id}"),
            f"recovery {method}.top_files for {sample_id}",
        )[:20]
        ranked[method] = files

    rrf_scores: dict[str, float] = {}
    for method in SINGLE_BASELINES:
        for rank, path in enumerate(ranked[method], start=1):
            rrf_scores[path] = rrf_scores.get(path, 0.0) + 1.0 / (60.0 + rank)
    rrf_files = [
        path
        for path, _score in sorted(rrf_scores.items(), key=lambda item: (-item[1], item[0]))[:20]
    ]

    manifest_path = arb_data_root / "pilot_corpus" / release / "corpus_manifest.jsonl"
    corpus_matches = [
        row
        for row in _read_jsonl(manifest_path)
        if row.get("repo") == manifest_row.get("repo")
        and row.get("base_commit") == manifest_row.get("base_commit")
    ]
    _require(len(corpus_matches) == 1, f"baseline recovery requires one corpus manifest row for {sample_id}")
    chunks_path = Path(str(corpus_matches[0].get("chunks_path") or ""))
    _require(chunks_path.exists(), f"baseline recovery chunks file missing for {sample_id}: {chunks_path}")
    needed = {path for files in ranked.values() for path in files}
    needed.update(rrf_files)
    file_texts: dict[str, str] = {}
    rows_scanned = 0
    bytes_read = 0
    started = time.perf_counter()
    try:
        with chunks_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                rows_scanned += 1
                bytes_read += len(line.encode("utf-8"))
                row = json.loads(line)
                if row.get("kind") != "file":
                    continue
                path = _normal_path(str(row.get("path") or ""))
                if path in needed:
                    _require(path not in file_texts, f"duplicate canonical kind=file text for {sample_id}/{path}")
                    file_texts[path] = str(row.get("text") or "")
    except (OSError, json.JSONDecodeError) as exc:
        raise DiscoveryValidationError(f"baseline recovery corpus read failed for {sample_id}: {exc}") from exc
    wall_seconds = time.perf_counter() - started

    method_files = {**ranked, "rrf_equal_cost_hybrid": rrf_files}
    recovered: dict[str, Mapping[str, Any]] = {}
    for method, files in method_files.items():
        recovered[method] = {
            "files": files,
            "score": score_execution(
                {"files": files, "chunks": []},
                gold_files,
                file_texts=file_texts,
            ),
        }
    audit = {
        "performed": True,
        "reason": "query-only terminal compile row omitted canonical_baselines",
        "gold_used_only_after_ranked_files_frozen": True,
        "method": "official top_files plus canonical kind=file corpus text and pinned score_execution",
        "corpus_rows_scanned": rows_scanned,
        "corpus_bytes_read": bytes_read,
        "corpus_wall_seconds": wall_seconds,
        "canonical_file_text_count": len(file_texts),
        "canonical_missing_paths": sorted(needed - set(file_texts)),
    }
    return recovered, audit


def _normalize_sample(
    batch_row: Mapping[str, Any],
    manifest_row: Mapping[str, Any],
    official_row: Mapping[str, Any],
    gold_files: Sequence[str],
    arb_data_root: Path,
) -> dict[str, Any]:
    sample_id = str(manifest_row["sample_id"])
    label = f"sample {sample_id}"
    _require(batch_row.get("sample_id") == sample_id, f"batch sample order mismatch at {sample_id}")
    _require(batch_row.get("task_type") == manifest_row.get("task_type"), f"batch task_type mismatch for {sample_id}")
    _require(batch_row.get("batch_index") == manifest_row.get("pilot_index"), f"batch_index mismatch for {sample_id}")
    _require(batch_row.get("batch_total") == EXPECTED_SAMPLE_COUNT, f"batch_total mismatch for {sample_id}")

    query_audit = _mapping(batch_row.get("query_only_audit"), f"{label}.query_only_audit")
    forbidden = set(_list(query_audit.get("forbidden_sources_not_available"), f"{label}.forbidden_sources"))
    _require({"gold", "reference_patch", "evaluation_metrics"}.issubset(forbidden), f"query-only audit incomplete for {sample_id}")

    terminal_compile = "deployment_query_only_output" not in batch_row
    if terminal_compile:
        _require(batch_row.get("decision") == "ABSTAIN", f"only query-only ABSTAIN may omit deployment output for {sample_id}")
        _require(
            all(key not in batch_row for key in ("executions", "searches", "canonical_baselines", "best_found_posthoc_oracle")),
            f"partial terminal schema is inconsistent for {sample_id}",
        )
        deployment: Mapping[str, Any] = {
            "frozen_before_gold_access": True,
            "decision": "ABSTAIN",
            "reason": batch_row.get("reason"),
            "eligible_candidate_count": 0,
            "deployment_selection": None,
        }
        decision = "ABSTAIN"
        refinement: list[Mapping[str, Any]] = []
        coarse: list[Mapping[str, Any]] = []
    else:
        deployment = _mapping(batch_row.get("deployment_query_only_output"), f"{label}.deployment_query_only_output")
        _require(deployment.get("frozen_before_gold_access") is True, f"deployment output was not frozen before gold for {sample_id}")
        decision = deployment.get("decision")
        _require(decision in {"PROGRAM", "ABSTAIN", "UNSAT"}, f"invalid deployment decision for {sample_id}")
        _require(batch_row.get("decision") == decision, f"top-level decision mismatch for {sample_id}")
        _require(batch_row.get("reason") == deployment.get("reason"), f"decision reason mismatch for {sample_id}")
        executions_block = _mapping(batch_row.get("executions"), f"{label}.executions")
        refinement = [
            _mapping(value, f"{label}.executions.refinement")
            for value in _list(executions_block.get("refinement"), f"{label}.executions.refinement")
        ]
        coarse = [
            _mapping(value, f"{label}.executions.coarse")
            for value in _list(executions_block.get("coarse"), f"{label}.executions.coarse")
        ]
    eligible = [row for row in refinement if row.get("status") == "EXECUTED"]
    expected_selected = min(eligible, key=_program_key, default=None)
    _require(deployment.get("eligible_candidate_count") == len(eligible), f"eligible candidate count mismatch for {sample_id}")

    selected = deployment.get("deployment_selection")
    selection_posthoc = batch_row.get("deployment_selection_posthoc_oracle")
    typed_files: list[str] = []
    selected_execution: Mapping[str, Any] | None = None
    if expected_selected is None:
        _require(selected is None, f"deployment selected a program without an eligible candidate for {sample_id}")
        _require(selection_posthoc is None, f"posthoc selected score exists without deployment selection for {sample_id}")
        _require(decision != "PROGRAM", f"PROGRAM has no selected execution for {sample_id}")
        typed_score = {
            "bcy": 0.0,
            "recall": 0.0,
            "gold_file_count": len(gold_files),
            "canonical_missing_ranked_files": 0,
        }
    else:
        selected_map = _mapping(selected, f"{label}.deployment_selection")
        expected_program = list(_program_key(expected_selected)[2])
        _require(selected_map.get("program") == expected_program, f"query-only selector mismatch for {sample_id}")
        _require(decision == "PROGRAM", f"selected program is not reflected by PROGRAM decision for {sample_id}")
        certificate = _mapping(selected_map.get("certificate"), f"{label}.selection.certificate")
        _require(certificate.get("runtime_certified_for_refined_return") is True, f"selected program is uncertified for {sample_id}")
        typed_files = _dedupe_paths(
            _list(selected_map.get("files"), f"{label}.selection.files"),
            f"{label}.selection.files",
        )
        expected_files = _dedupe_paths(
            _list(expected_selected.get("files"), f"{label}.selected execution files"),
            f"{label}.selected execution files",
        )
        _require(typed_files == expected_files, f"selected files mismatch for {sample_id}")
        posthoc = _mapping(selection_posthoc, f"{label}.deployment_selection_posthoc_oracle")
        _require(posthoc.get("oracle_only") is True, f"selected posthoc score is not oracle-labelled for {sample_id}")
        _require(posthoc.get("selection_was_frozen_without_gold") is True, f"selected posthoc score lacks freeze guard for {sample_id}")
        _require(posthoc.get("program") == expected_program, f"selected posthoc program mismatch for {sample_id}")
        typed_score = _validated_score(posthoc.get("score"), f"{label}.query_only_selected_score")
        execution_score = _validated_score(expected_selected.get("posthoc_score"), f"{label}.selected_execution_score")
        _score_matches(typed_score, execution_score, f"selected score for {sample_id}")
        selected_execution = expected_selected

    gold = set(gold_files)
    _require(typed_score["gold_file_count"] == len(gold), f"typed gold count mismatch for {sample_id}")
    observed_typed_recall = len(set(typed_files) & gold) / len(gold)
    _require(_close(typed_score["recall"], observed_typed_recall), f"typed file recall/path mismatch for {sample_id}")

    baseline_recovery = {
        "performed": False,
        "reason": None,
        "gold_used_only_after_ranked_files_frozen": True,
        "corpus_rows_scanned": 0,
        "corpus_bytes_read": 0,
        "corpus_wall_seconds": 0.0,
        "canonical_missing_paths": [],
    }
    if "canonical_baselines" in batch_row:
        canonical = _mapping(batch_row.get("canonical_baselines"), f"{label}.canonical_baselines")
        _require("8000-token" in str(canonical.get("protocol")), f"canonical baseline protocol mismatch for {sample_id}")
        methods = _mapping(canonical.get("methods"), f"{label}.canonical_baselines.methods")
    else:
        _require(terminal_compile, f"nonterminal row is missing canonical baselines for {sample_id}")
        recovered_methods, baseline_recovery = _recover_canonical_baselines(
            arb_data_root,
            manifest_row,
            gold_files,
        )
        methods = recovered_methods
    _require(set(methods) == set(BASELINES), f"canonical baseline methods mismatch for {sample_id}")
    baseline_values: dict[str, dict[str, Any]] = {}
    union_paths: set[str] = set()
    official_diag = _mapping(
        official_row.get("unbounded_top20_union_diagnostic"),
        f"official union diagnostic for {sample_id}",
    )
    official_recalls = _mapping(
        official_diag.get("method_gold_fraction@20"),
        f"official method recalls for {sample_id}",
    )
    for method in BASELINES:
        block = _mapping(methods.get(method), f"{label}.baseline.{method}")
        files = _dedupe_paths(_list(block.get("files"), f"{label}.{method}.files"), f"{label}.{method}.files")
        _require(len(files) <= 20, f"{method} returns more than 20 files for {sample_id}")
        score = _validated_score(block.get("score"), f"{label}.{method}.score")
        _require(score["gold_file_count"] == len(gold), f"{method} gold count mismatch for {sample_id}")
        observed_recall = len(set(files) & gold) / len(gold)
        _require(_close(score["recall"], observed_recall), f"{method} file recall/path mismatch for {sample_id}")
        if method in SINGLE_BASELINES:
            official_recall = _number(official_recalls.get(method), f"official {method} recall for {sample_id}")
            _require(_close(score["recall"], official_recall), f"official Recall@20 cross-check failed for {sample_id}/{method}")
            union_paths.update(files)
        baseline_values[method] = {**score, "files": files}

    outside_paths = set(typed_files) - union_paths
    outside_gold = outside_paths & gold

    oracle_values: dict[str, dict[str, Any]] = {}
    if terminal_compile:
        for mode in ("refinement", "coarse"):
            oracle_values[mode] = {
                "bcy": 0.0,
                "recall": 0.0,
                "gold_file_count": len(gold),
                "canonical_missing_ranked_files": 0,
            }
    else:
        best_found = _mapping(batch_row.get("best_found_posthoc_oracle"), f"{label}.best_found_posthoc_oracle")
        for mode, executions in (("refinement", refinement), ("coarse", coarse)):
            block = _mapping(best_found.get(mode), f"{label}.best_found.{mode}")
            _require(block.get("oracle_only") is True, f"{mode} best-found lacks oracle label for {sample_id}")
            _require(
                block.get("not_used_for_deployment_selection_or_decision") is True,
                f"{mode} best-found lacks nondeployment guard for {sample_id}",
            )
            executed = [row for row in executions if row.get("status") == "EXECUTED"]
            expected_best = max(executed, key=_oracle_key, default=None)
            if expected_best is None:
                _require(block.get("program") is None and block.get("score") is None, f"empty {mode} oracle mismatch for {sample_id}")
                oracle_values[mode] = {
                    "bcy": 0.0,
                    "recall": 0.0,
                    "gold_file_count": len(gold),
                    "canonical_missing_ranked_files": 0,
                }
            else:
                _require(block.get("program") == expected_best.get("program"), f"{mode} oracle program mismatch for {sample_id}")
                recorded = _validated_score(block.get("score"), f"{label}.{mode}_oracle_score")
                expected_score = _validated_score(expected_best.get("posthoc_score"), f"{label}.{mode}_expected_oracle_score")
                _score_matches(recorded, expected_score, f"{mode} oracle score for {sample_id}")
                oracle_values[mode] = recorded
    _require(
        oracle_values["refinement"]["bcy"] + TOLERANCE >= typed_score["bcy"],
        f"query-only BCY exceeds its oracle ceiling for {sample_id}",
    )

    search_values: dict[str, dict[str, Any]] = {}
    if terminal_compile:
        for mode in ("coarse", "refinement"):
            search_values[mode] = {
                "frontier_exhausted": False,
                "program_storage_complete": False,
                "expansions": 0,
                "wrong_entity_rejections": 0,
            }
    else:
        searches = _mapping(batch_row.get("searches"), f"{label}.searches")
        for mode in ("coarse", "refinement"):
            search = _mapping(searches.get(mode), f"{label}.searches.{mode}")
            search_values[mode] = {
                "frontier_exhausted": search.get("frontier_exhausted") is True,
                "program_storage_complete": search.get("program_storage_truncated") is False,
                "expansions": _integer(search.get("expansions"), f"{label}.{mode}.expansions"),
                "wrong_entity_rejections": _integer(
                    search.get("wrong_entity_rejections"),
                    f"{label}.{mode}.wrong_entity_rejections",
                ),
            }
    exhaustive_superset_check = (
        search_values["coarse"]["frontier_exhausted"]
        and search_values["coarse"]["program_storage_complete"]
        and search_values["refinement"]["frontier_exhausted"]
        and search_values["refinement"]["program_storage_complete"]
    )
    if exhaustive_superset_check:
        coarse_pair = (oracle_values["coarse"]["bcy"], oracle_values["coarse"]["recall"])
        refined_pair = (oracle_values["refinement"]["bcy"], oracle_values["refinement"]["recall"])
        _require(coarse_pair >= refined_pair, f"coarse/refinement superset sanity failed for {sample_id}")

    if decision == "UNSAT":
        unsat = _mapping(batch_row.get("unsat_eligibility"), f"{label}.unsat_eligibility")
        _require(unsat.get("eligible") is True, f"ineligible UNSAT decision for {sample_id}")
        _require(isinstance(unsat.get("scope"), str) and unsat.get("scope"), f"UNSAT scope missing for {sample_id}")

    pass_values: dict[str, dict[str, Any]] = {}
    if terminal_compile:
        capabilities: Mapping[str, Any] = {}
        io: Mapping[str, Any] = {}
        for key in ("pass_1", "pass_2", "pass_3"):
            pass_values[key] = {"rows_scanned": 0, "bytes_read": 0, "wall_seconds": 0.0}
        rows_scanned = 0
        bytes_read = 0
        wall_seconds = 0.0
        identifier_lengths: list[int] = []
        bind_truncation: Mapping[str, Any] = {}
        relation_truncation: Mapping[str, Any] = {}
        outside_candidate_entity_sum = 0
    else:
        capabilities = _mapping(batch_row.get("store_capabilities"), f"{label}.store_capabilities")
        _require(capabilities.get("gold_fields_copied_to_executor") == [], f"gold fields reached executor for {sample_id}")
        _require(
            capabilities.get("semantic_relation_backend") == "whole_token_identifier_occurrence_provenance",
            f"semantic backend drift for {sample_id}",
        )
        _require(capabilities.get("call_graph_semantics") is False, f"call-graph overclaim flag for {sample_id}")
        _require(capabilities.get("import_graph_semantics") is False, f"import-graph overclaim flag for {sample_id}")
        semantic_guard = _mapping(batch_row.get("semantic_claim_guard"), f"{label}.semantic_claim_guard")
        _require(semantic_guard.get("not_semantic_evidence") is True, f"semantic claim guard missing for {sample_id}")
        io = _mapping(batch_row.get("index_io_audit"), f"{label}.index_io_audit")
        for key in ("pass_1", "pass_2", "pass_3"):
            block = _mapping(io.get(key), f"{label}.io.{key}")
            pass_values[key] = {
                "rows_scanned": _integer(block.get("rows_scanned"), f"{label}.{key}.rows_scanned"),
                "bytes_read": _integer(block.get("bytes_read"), f"{label}.{key}.bytes_read"),
                "wall_seconds": _number(block.get("wall_seconds"), f"{label}.{key}.wall_seconds"),
            }
        rows_scanned = _integer(io.get("rows_scanned"), f"{label}.io.rows_scanned")
        bytes_read = _integer(io.get("bytes_read"), f"{label}.io.bytes_read")
        wall_seconds = _number(io.get("wall_seconds"), f"{label}.io.wall_seconds")
        _require(sum(value["rows_scanned"] for value in pass_values.values()) == rows_scanned, f"I/O row total mismatch for {sample_id}")
        _require(sum(value["bytes_read"] for value in pass_values.values()) == bytes_read, f"I/O byte total mismatch for {sample_id}")
        _require(rows_scanned >= 0 and bytes_read >= 0 and wall_seconds >= 0, f"negative I/O accounting for {sample_id}")
        identifiers = _mapping(io.get("identifiers_by_entity"), f"{label}.identifiers_by_entity")
        identifier_lengths = []
        for entity, values in identifiers.items():
            identifier_lengths.append(len(_list(values, f"{label}.identifiers.{entity}")))
        bind_truncation = _mapping(io.get("bind_postings_truncated_by_entity"), f"{label}.bind_truncation")
        relation_truncation = _mapping(io.get("relation_postings_truncated_by_entity"), f"{label}.relation_truncation")
        outside_candidates = _mapping(
            io.get("relation_paths_outside_hybrid_union_by_entity"),
            f"{label}.outside_candidate_paths",
        )
        outside_candidate_entity_sum = sum(
            _integer(value, f"{label}.outside candidate count") for value in outside_candidates.values()
        )
    completeness = {
        "any_identifier": any(value > 0 for value in identifier_lengths),
        "all_anchors_have_identifier": bool(identifier_lengths) and all(value > 0 for value in identifier_lengths),
        "refinement_frontier_exhausted": search_values["refinement"]["frontier_exhausted"],
        "refinement_program_storage_complete": search_values["refinement"]["program_storage_complete"],
        "coarse_frontier_exhausted": search_values["coarse"]["frontier_exhausted"],
        "coarse_program_storage_complete": search_values["coarse"]["program_storage_complete"],
        "full_scan_complete": (not terminal_compile) and io.get("full_scan_complete") is True,
        "selected_paths_complete": (not terminal_compile) and io.get("all_selected_paths_observed") is True,
        "query_anchor_catalog_not_truncated": (not terminal_compile) and io.get("query_anchor_catalog_truncated") is False,
        "bind_postings_not_truncated": not any(value is True for value in bind_truncation.values()),
        "relation_postings_not_truncated": not any(value is True for value in relation_truncation.values()),
        "canonical_file_texts_complete": (
            not bool(baseline_recovery.get("canonical_missing_paths"))
            if terminal_compile
            else not bool(_list(io.get("canonical_missing_paths"), f"{label}.canonical_missing_paths"))
        ),
        "baseline_ranked_texts_complete": all(
            value["canonical_missing_ranked_files"] == 0 for value in baseline_values.values()
        ),
    }

    if terminal_compile:
        refinement_accounting = {
            "attempted_candidate_count": 0,
            "certified_executed_candidate_count": 0,
            "uncertified_candidate_count": 0,
            "no_evidence_candidate_count": 0,
            "aggregate_nominal_cost_units": 0.0,
            "aggregate_operator_calls": 0,
        }
        declared_operator_depth: int | None = None
        declared_transitions: int | None = None
    else:
        execution_accounting = _mapping(batch_row.get("execution_accounting"), f"{label}.execution_accounting")
        refinement_accounting = _validate_execution_accounting(
            _mapping(execution_accounting.get("refinement"), f"{label}.execution_accounting.refinement"),
            refinement,
            f"{label}.refinement_accounting",
        )
        declared_operator_depth = _integer(batch_row.get("operator_depth"), f"{label}.operator_depth")
        _require(batch_row.get("chain_depth") == declared_operator_depth, f"chain/operator depth mismatch for {sample_id}")
        declared_transitions = _integer(
            batch_row.get("retrieval_transition_depth"),
            f"{label}.retrieval_transition_depth",
        )
        _require(batch_row.get("certificate_step_counts_as_retrieval_transition") is False, f"certificate transition guard failed for {sample_id}")
        depth_guard = _mapping(batch_row.get("depth_necessity_guard"), f"{label}.depth_necessity_guard")
        _require(depth_guard.get("strict_depth_necessary") is None, f"strict depth necessity was overclaimed for {sample_id}")

    actual_operator_depth: int | None = None
    actual_retrieval_transitions: int | None = None
    selected_nominal_cost: float | None = None
    if selected_execution is not None:
        actual_operator_depth = _integer(selected_execution.get("depth"), f"{label}.selected.depth")
        actions = [
            _mapping(value, f"{label}.selected.action_ledger").get("action")
            for value in _list(selected_execution.get("action_ledger"), f"{label}.selected.action_ledger")
        ]
        actual_retrieval_transitions = sum(action in {"bind_anchor", "follow_relation"} for action in actions)
        _require(actual_retrieval_transitions == declared_transitions, f"actual retrieval transition mismatch for {sample_id}")
        selected_nominal_cost = _number(selected_execution.get("cost_units"), f"{label}.selected.cost_units")

    return {
        "pilot_index": manifest_row["pilot_index"],
        "sample_id": sample_id,
        "task_type": manifest_row["task_type"],
        "repo": manifest_row["repo"],
        "base_commit": manifest_row["base_commit"],
        "decision": decision,
        "reason": deployment.get("reason"),
        "query_only_terminal_compile": terminal_compile,
        "baseline_source": "posthoc_recovery" if baseline_recovery["performed"] else "executor_row",
        "baseline_recovery": baseline_recovery,
        "query_only": {"bcy": typed_score["bcy"], "recall": typed_score["recall"]},
        "oracle_ceiling": {
            "bcy": oracle_values["refinement"]["bcy"],
            "recall": oracle_values["refinement"]["recall"],
        },
        "coarse_oracle_ceiling": {
            "bcy": oracle_values["coarse"]["bcy"],
            "recall": oracle_values["coarse"]["recall"],
        },
        "baselines": {
            method: {"bcy": value["bcy"], "recall": value["recall"]}
            for method, value in baseline_values.items()
        },
        "outside_union": {
            "returned_file_count": len(outside_paths),
            "gold_file_count": len(outside_gold),
            "incremental_gold_recall": len(outside_gold) / len(gold),
            "candidate_entity_sum_not_unique_output": outside_candidate_entity_sum,
            "has_candidate_escape": outside_candidate_entity_sum > 0,
        },
        "completeness": completeness,
        "io": {
            "rows_scanned": rows_scanned,
            "bytes_read": bytes_read,
            "wall_seconds": wall_seconds,
            "passes": pass_values,
        },
        "search_work": {
            **refinement_accounting,
            "expansions": search_values["refinement"]["expansions"],
            "wrong_entity_rejections": search_values["refinement"]["wrong_entity_rejections"],
        },
        "depth": {
            "declared_operator_depth": declared_operator_depth,
            "declared_retrieval_transition_depth": declared_transitions,
            "selected_operator_depth": actual_operator_depth,
            "selected_retrieval_transition_depth": actual_retrieval_transitions,
            "selected_nominal_cost_units": selected_nominal_cost,
            "strict_depth_necessary": None,
        },
        "superset_sanity": {
            "evaluated": exhaustive_superset_check,
            "passed": True if exhaustive_superset_check else None,
        },
    }


def _win_tie_loss(primary: Sequence[float], comparator: Sequence[float]) -> dict[str, int]:
    wins = ties = losses = 0
    for left, right in zip(primary, comparator):
        difference = left - right
        if difference > TOLERANCE:
            wins += 1
        elif difference < -TOLERANCE:
            losses += 1
        else:
            ties += 1
    return {"wins": wins, "ties": ties, "losses": losses}


def _scope_summary(samples: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    n = len(samples)
    query_bcy = [float(row["query_only"]["bcy"]) for row in samples]
    query_recall = [float(row["query_only"]["recall"]) for row in samples]
    oracle_bcy = [float(row["oracle_ceiling"]["bcy"]) for row in samples]
    oracle_recall = [float(row["oracle_ceiling"]["recall"]) for row in samples]

    comparisons: dict[str, Any] = {}
    for method in BASELINES:
        baseline_bcy = [float(row["baselines"][method]["bcy"]) for row in samples]
        baseline_recall = [float(row["baselines"][method]["recall"]) for row in samples]
        comparisons[method] = {
            "canonical_bcy": {
                "query_only_mean": _mean(query_bcy),
                "baseline_mean": _mean(baseline_bcy),
                "paired_mean_delta": _mean([left - right for left, right in zip(query_bcy, baseline_bcy)]),
                **_win_tie_loss(query_bcy, baseline_bcy),
            },
            "file_recall": {
                "query_only_mean": _mean(query_recall),
                "baseline_mean": _mean(baseline_recall),
                "paired_mean_delta": _mean([left - right for left, right in zip(query_recall, baseline_recall)]),
                **_win_tie_loss(query_recall, baseline_recall),
            },
        }

    decisions = Counter(str(row["decision"]) for row in samples)
    decision_block = {
        decision: _rate(decisions.get(decision, 0), n)
        for decision in ("PROGRAM", "ABSTAIN", "UNSAT")
    }
    reasons = Counter(str(row["reason"] or "NONE") for row in samples)

    outside_file_count = sum(int(row["outside_union"]["returned_file_count"]) for row in samples)
    outside_gold_count = sum(int(row["outside_union"]["gold_file_count"]) for row in samples)
    escaped_tasks = sum(int(row["outside_union"]["returned_file_count"]) > 0 for row in samples)
    useful_tasks = sum(int(row["outside_union"]["gold_file_count"]) > 0 for row in samples)
    candidate_escape_tasks = sum(bool(row["outside_union"]["has_candidate_escape"]) for row in samples)

    completeness_keys = tuple(samples[0]["completeness"]) if samples else ()
    completeness = {
        key: _rate(sum(bool(row["completeness"][key]) for row in samples), n)
        for key in completeness_keys
    }

    io_rows = [float(row["io"]["rows_scanned"]) for row in samples]
    io_bytes = [float(row["io"]["bytes_read"]) for row in samples]
    io_wall = [float(row["io"]["wall_seconds"]) for row in samples]
    pass_totals: dict[str, Any] = {}
    for key in ("pass_1", "pass_2", "pass_3"):
        pass_totals[key] = {
            "rows_scanned_total": sum(int(row["io"]["passes"][key]["rows_scanned"]) for row in samples),
            "bytes_read_total": sum(int(row["io"]["passes"][key]["bytes_read"]) for row in samples),
            "wall_seconds_total": sum(float(row["io"]["passes"][key]["wall_seconds"]) for row in samples),
        }

    selected_depths = [row["depth"]["selected_operator_depth"] for row in samples if row["depth"]["selected_operator_depth"] is not None]
    selected_transitions = [
        row["depth"]["selected_retrieval_transition_depth"]
        for row in samples
        if row["depth"]["selected_retrieval_transition_depth"] is not None
    ]
    selected_costs = [
        float(row["depth"]["selected_nominal_cost_units"])
        for row in samples
        if row["depth"]["selected_nominal_cost_units"] is not None
    ]

    return {
        "n": n,
        "decisions": decision_block,
        "decision_reasons": dict(sorted(reasons.items())),
        "effectiveness": {
            "query_only_primary": {
                "mean_canonical_bcy@8000_tokens": _mean(query_bcy),
                "mean_file_recall": _mean(query_recall),
                "positive_bcy_tasks": _rate(sum(value > TOLERANCE for value in query_bcy), n),
            },
            "oracle_ceiling_diagnostic_only": {
                "mean_canonical_bcy@8000_tokens": _mean(oracle_bcy),
                "mean_file_recall": _mean(oracle_recall),
                "mean_oracle_minus_query_bcy": _mean([left - right for left, right in zip(oracle_bcy, query_bcy)]),
                "mean_oracle_minus_query_recall": _mean([left - right for left, right in zip(oracle_recall, query_recall)]),
            },
            "paired_comparisons": comparisons,
        },
        "outside_union_posthoc_gold_join": {
            "definition": "selected query-only files outside the union of lexical/BM25/RepoMap top20; gold joined only after selection",
            "returned_file_count": outside_file_count,
            "gold_file_count": outside_gold_count,
            "escape_task_rate_all": _rate(escaped_tasks, n),
            "useful_escape_task_rate_all": _rate(useful_tasks, n),
            "useful_escape_task_rate_conditional": _rate(useful_tasks, escaped_tasks),
            "outside_file_precision_micro": outside_gold_count / outside_file_count if outside_file_count else None,
            "mean_incremental_gold_recall": _mean(
                [float(row["outside_union"]["incremental_gold_recall"]) for row in samples]
            ),
            "candidate_escape_task_rate_diagnostic_only": _rate(candidate_escape_tasks, n),
            "candidate_counts_are_not_unique_outputs_or_useful_hits": True,
            "budget_effect_attribution_not_available": True,
        },
        "completeness": completeness,
        "io_and_cost": {
            "three_full_scan_rows": _distribution(io_rows),
            "three_full_scan_bytes_read": _distribution(io_bytes),
            "three_full_scan_wall_seconds": _distribution(io_wall),
            "per_pass_totals": pass_totals,
            "index_storage_bytes": None,
            "index_storage_bytes_status": "NOT_MEASURED; bytes_read is scan traffic, not index size",
            "batch_end_to_end_wall_seconds": None,
            "batch_end_to_end_wall_status": "NOT_AVAILABLE_FROM_BATCH_JSONL",
            "baseline_recovery": {
                "task_count": sum(row["baseline_source"] == "posthoc_recovery" for row in samples),
                "corpus_rows_scanned": sum(
                    int(row["baseline_recovery"]["corpus_rows_scanned"]) for row in samples
                ),
                "corpus_bytes_read": sum(
                    int(row["baseline_recovery"]["corpus_bytes_read"]) for row in samples
                ),
                "corpus_wall_seconds": sum(
                    float(row["baseline_recovery"]["corpus_wall_seconds"]) for row in samples
                ),
                "separate_from_typed_executor_io": True,
            },
            "refinement_candidates_attempted_total": sum(
                int(row["search_work"]["attempted_candidate_count"]) for row in samples
            ),
            "refinement_aggregate_nominal_cost_units": sum(
                float(row["search_work"]["aggregate_nominal_cost_units"]) for row in samples
            ),
            "refinement_aggregate_operator_calls": sum(
                int(row["search_work"]["aggregate_operator_calls"]) for row in samples
            ),
            "refinement_search_expansions_total": sum(int(row["search_work"]["expansions"]) for row in samples),
            "refinement_wrong_entity_rejections_total": sum(
                int(row["search_work"]["wrong_entity_rejections"]) for row in samples
            ),
            "selected_nominal_cost_units": _distribution(selected_costs),
            "nominal_cost_guard": "operator cost_units are grammar-comparison charges, not equal physical compute",
        },
        "depth": {
            "declared_operator_depth_counts_all_tasks": _count_distribution(
                row["depth"]["declared_operator_depth"] for row in samples
            ),
            "declared_retrieval_transition_depth_counts_all_tasks": _count_distribution(
                row["depth"]["declared_retrieval_transition_depth"] for row in samples
            ),
            "selected_program_count": len(selected_depths),
            "selected_operator_depth_counts": _count_distribution(selected_depths),
            "selected_retrieval_transition_depth_counts": _count_distribution(selected_transitions),
            "no_selected_program_count": n - len(selected_depths),
            "certificate_step_counts_as_retrieval_transition": False,
            "strict_depth_necessary": None,
            "strict_depth_status": "NOT_ESTABLISHED",
        },
        "superset_sanity": {
            "evaluated_tasks": sum(bool(row["superset_sanity"]["evaluated"]) for row in samples),
            "failed_tasks": 0,
            "interpretation": "implementation consistency check only; not theory-effect evidence",
        },
    }


def summarize_discovery(
    batch_jsonl: Path,
    arb_data_root: Path,
    manifest_path: Path,
    official_baseline_report: Path,
) -> dict[str, Any]:
    manifest_sha = _sha256(manifest_path)
    manifest_raw = _read_json(manifest_path)
    manifest_rows = _validate_manifest(manifest_raw, manifest_sha)
    official_raw = _read_json(official_baseline_report)
    official_by_id = _validate_official_report(official_raw, manifest_rows, manifest_sha)
    gold_by_id = _load_gold_files(arb_data_root, manifest_rows)
    batch_rows = _read_jsonl(batch_jsonl)
    _require(len(batch_rows) == EXPECTED_SAMPLE_COUNT, "batch JSONL must contain exactly 60 nonblank rows")
    batch_ids = [row.get("sample_id") for row in batch_rows]
    _require(len(set(batch_ids)) == EXPECTED_SAMPLE_COUNT, "batch JSONL contains duplicate sample IDs")
    expected_ids = [row["sample_id"] for row in manifest_rows]
    _require(batch_ids == expected_ids, "batch JSONL order/IDs must exactly match manifest pilot order")

    normalized = [
        _normalize_sample(
            batch_row,
            manifest_row,
            official_by_id[str(manifest_row["sample_id"])],
            gold_by_id[str(manifest_row["sample_id"])],
            arb_data_root,
        )
        for batch_row, manifest_row in zip(batch_rows, manifest_rows)
    ]
    observed_counts = Counter(str(row["task_type"]) for row in normalized)
    _require(dict(observed_counts) == EXPECTED_TASK_COUNTS, "normalized batch strata are not 20/20/20")

    overall = _scope_summary(normalized)
    by_task = {
        task_type: _scope_summary([row for row in normalized if row["task_type"] == task_type])
        for task_type in EXPECTED_TASK_COUNTS
    }
    return {
        "schema_version": 1,
        "report_kind": "arb60_exact_identifier_lineage_development_discovery_audit",
        "status": "COMPLETED_DEVELOPMENT_DISCOVERY_AGGREGATION",
        "executor_schema_contract": f"deployment_query_only_output@{EXECUTOR_FROZEN_REVISION}",
        "provenance": {
            "batch_jsonl": str(batch_jsonl),
            "batch_jsonl_sha256": _sha256(batch_jsonl),
            "arb_data_root": str(arb_data_root),
            "manifest": str(manifest_path),
            "manifest_sha256": manifest_sha,
            "official_baseline_report": str(official_baseline_report),
            "official_baseline_report_sha256": _sha256(official_baseline_report),
            "arb_code_commit": manifest_raw.get("arb_code_commit"),
            "sample_count": EXPECTED_SAMPLE_COUNT,
            "task_counts": dict(EXPECTED_TASK_COUNTS),
            "repo_count": len({row["repo"] for row in manifest_rows}),
            "snapshot_count": len({(row["repo"], row["base_commit"]) for row in manifest_rows}),
        },
        "integrity": {
            "all_hard_checks_passed": True,
            "exact_manifest_order_match": True,
            "exact_60_row_denominator": True,
            "exact_20_per_task_type": True,
            "official_three_by_three_grid_complete": True,
            "official_manifest_hash_match": True,
            "official_recall20_crosscheck_passed": True,
            "gold_join_after_query_only_selection": True,
            "canonical_metric": PRIMARY_BCY,
            "canonical_tokenizer": CANONICAL_TOKENIZER,
            "official_legacy_character_metrics_used_as_canonical": False,
        },
        "claim_guard": {
            "development_discovery": True,
            "confirmatory": False,
            "mechanism_gate_evaluated": False,
            "model_gate_evaluated": False,
            "chapter_gate_evaluated": False,
            "strong_semantic_baseline_included": False,
            "selective_no_gold_gate_included": False,
            "adversarial_gate_included": False,
            "strict_depth_necessity_established": False,
            "primary_typed_output": "deployment_query_only_output; frozen before gold access",
            "oracle_ceiling": "best_found_posthoc_oracle.refinement; diagnostic only",
            "semantic_scope": "whole-token exact-identifier occurrence lineage, not call/import/dependency semantics",
            "forbidden_claims": [
                "MECHANISM-PROCEED",
                "statistical superiority",
                "causal theory effect",
                "semantic relation recovery",
                "strict depth necessity",
                "selective abstention validity",
                "confirmatory generalization",
            ],
        },
        "scopes": {
            "overall": overall,
            "by_task_type": by_task,
        },
        "samples": normalized,
    }


def _fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "NA"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def render_markdown(report: Mapping[str, Any]) -> str:
    scopes = _mapping(report.get("scopes"), "report.scopes")
    overall = _mapping(scopes.get("overall"), "report.scopes.overall")
    by_task = _mapping(scopes.get("by_task_type"), "report.scopes.by_task_type")
    named_scopes = [("overall", overall), *[(task, _mapping(by_task[task], task)) for task in EXPECTED_TASK_COUNTS]]

    lines = [
        "# ARB60 exact-identifier-lineage development discovery audit",
        "",
        "> Development/discovery evidence only. This report is not confirmatory and does not evaluate MECHANISM-PROCEED.",
        "> The primary typed score is the query-only deployment selection frozen before gold access; best-found scores are oracle ceilings only.",
        "> The mechanism is whole-token exact-identifier occurrence lineage, not call/import/dependency semantics.",
        "",
        "## Integrity and provenance",
        "",
        f"- Executor schema contract: `{report['executor_schema_contract']}`",
        f"- Manifest SHA256: `{report['provenance']['manifest_sha256']}`",
        f"- Batch SHA256: `{report['provenance']['batch_jsonl_sha256']}`",
        f"- Denominator: {report['provenance']['sample_count']} tasks; 20 per task type",
        f"- Repositories/snapshots: {report['provenance']['repo_count']}/{report['provenance']['snapshot_count']}",
        "- Official lexical/BM25/RepoMap Recall@20 cross-check: passed",
        "- Official legacy 8K-character fields used as canonical BCY: no",
        "",
        "## Query-only primary versus baselines",
        "",
        "| Scope | Comparator | N | Query BCY | Baseline BCY | Delta | W/T/L | Query recall | Baseline recall | Delta | W/T/L |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for scope_name, scope in named_scopes:
        comparisons = scope["effectiveness"]["paired_comparisons"]
        for method in BASELINES:
            bcy = comparisons[method]["canonical_bcy"]
            recall = comparisons[method]["file_recall"]
            lines.append(
                "| "
                + " | ".join(
                    [
                        scope_name,
                        method,
                        str(scope["n"]),
                        _fmt(bcy["query_only_mean"]),
                        _fmt(bcy["baseline_mean"]),
                        _fmt(bcy["paired_mean_delta"]),
                        f"{bcy['wins']}/{bcy['ties']}/{bcy['losses']}",
                        _fmt(recall["query_only_mean"]),
                        _fmt(recall["baseline_mean"]),
                        _fmt(recall["paired_mean_delta"]),
                        f"{recall['wins']}/{recall['ties']}/{recall['losses']}",
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## Query-only score versus oracle ceiling",
            "",
            "| Scope | N | Query BCY | Oracle BCY | Oracle-query gap | Query recall | Oracle recall | Gap |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for scope_name, scope in named_scopes:
        query = scope["effectiveness"]["query_only_primary"]
        oracle = scope["effectiveness"]["oracle_ceiling_diagnostic_only"]
        lines.append(
            f"| {scope_name} | {scope['n']} | {_fmt(query['mean_canonical_bcy@8000_tokens'])} | "
            f"{_fmt(oracle['mean_canonical_bcy@8000_tokens'])} | {_fmt(oracle['mean_oracle_minus_query_bcy'])} | "
            f"{_fmt(query['mean_file_recall'])} | {_fmt(oracle['mean_file_recall'])} | "
            f"{_fmt(oracle['mean_oracle_minus_query_recall'])} |"
        )

    lines.extend(
        [
            "",
            "## Decisions and outside-union retrieval",
            "",
            "| Scope | PROGRAM | ABSTAIN | Scoped UNSAT | Escape tasks | Useful escape tasks | Conditional useful | Outside files | Outside gold | Micro precision |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for scope_name, scope in named_scopes:
        decisions = scope["decisions"]
        outside = scope["outside_union_posthoc_gold_join"]
        lines.append(
            f"| {scope_name} | {decisions['PROGRAM']['count']} | {decisions['ABSTAIN']['count']} | "
            f"{decisions['UNSAT']['count']} | {outside['escape_task_rate_all']['count']} | "
            f"{outside['useful_escape_task_rate_all']['count']} | "
            f"{_fmt(outside['useful_escape_task_rate_conditional']['rate'])} | "
            f"{outside['returned_file_count']} | {outside['gold_file_count']} | "
            f"{_fmt(outside['outside_file_precision_micro'])} |"
        )

    completeness_keys = list(overall["completeness"])
    lines.extend(
        [
            "",
            "Outside usefulness is retrieval-level post-hoc gold overlap. The current schema cannot attribute canonical packed-BCY gains to individual outside files.",
            "",
            "## Completeness",
            "",
            "| Check | Overall pass | code2test | edit2ripple | trace2code |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for key in completeness_keys:
        lines.append(
            f"| {key} | {overall['completeness'][key]['count']}/{overall['n']} | "
            f"{by_task['code2test']['completeness'][key]['count']}/20 | "
            f"{by_task['edit2ripple']['completeness'][key]['count']}/20 | "
            f"{by_task['trace2code']['completeness'][key]['count']}/20 |"
        )

    io = overall["io_and_cost"]
    depth = overall["depth"]
    lines.extend(
        [
            "",
            "## I/O, search work, and depth",
            "",
            f"- Three-pass rows scanned: {_fmt(io['three_full_scan_rows']['total'], 0)}",
            f"- Three-pass bytes read: {_fmt(io['three_full_scan_bytes_read']['total'], 0)} (scan traffic, not index size)",
            f"- Sum of per-task scan wall time: {_fmt(io['three_full_scan_wall_seconds']['total'])} seconds",
            f"- Median/p95/max per-task scan wall: {_fmt(io['three_full_scan_wall_seconds']['median'])} / "
            f"{_fmt(io['three_full_scan_wall_seconds']['p95_nearest_rank'])} / {_fmt(io['three_full_scan_wall_seconds']['max'])} seconds",
            f"- Refinement candidates attempted/operator calls: {io['refinement_candidates_attempted_total']} / "
            f"{io['refinement_aggregate_operator_calls']}",
            f"- Refinement nominal cost units: {_fmt(io['refinement_aggregate_nominal_cost_units'])}; these are not physical equal-compute charges",
            f"- Declared operator depths: `{json.dumps(depth['declared_operator_depth_counts_all_tasks'], sort_keys=True)}`",
            f"- Declared retrieval-transition depths: `{json.dumps(depth['declared_retrieval_transition_depth_counts_all_tasks'], sort_keys=True)}`",
            f"- Selected operator depths: `{json.dumps(depth['selected_operator_depth_counts'], sort_keys=True)}`",
            f"- Selected retrieval-transition depths: `{json.dumps(depth['selected_retrieval_transition_depth_counts'], sort_keys=True)}`",
            "- Certificate counts as a retrieval transition: no",
            "- Strict depth necessity: not established",
            "",
            "## Claim guard",
            "",
            "This development report does not include a strong semantic baseline, selective no-gold evaluation, adversarial rewiring/entity tests, or an untouched confirmatory set. It cannot support MECHANISM-PROCEED, statistical-superiority, causal-theory, semantic-relation, or strict-depth claims.",
            "",
        ]
    )
    return "\n".join(lines)


def write_report(report: Mapping[str, Any], output_json: Path, output_markdown: Path) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_markdown.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    output_markdown.write_text(render_markdown(report), encoding="utf-8")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-jsonl", type=Path, required=True)
    parser.add_argument("--arb-data-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--official-baseline-report", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    report = summarize_discovery(
        args.batch_jsonl,
        args.arb_data_root,
        args.manifest,
        args.official_baseline_report,
    )
    write_report(report, args.output_json, args.output_md)


if __name__ == "__main__":
    main()
