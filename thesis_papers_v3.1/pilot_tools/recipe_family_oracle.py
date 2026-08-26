"""Discover executable sufficient context-set families under a frozen run grid.

The input is JSONL with exactly one run for every observed context set on every
pre-registered patcher/seed cell.  This utility is a go/no-go instrument: it
does not train the proposed multi-set predictor.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from math import isfinite
from pathlib import Path
from statistics import mean


EVIDENCE_STATES = {"sufficient", "confirmed_insufficient", "underpowered", "missing"}


@dataclass(frozen=True)
class Run:
    task_id: str
    pack_id: str
    chunks: frozenset[str]
    patcher: str
    seed: str
    success: float
    token_cost: float


def _validate_runs(
    rows: list[Run],
    *,
    required_patchers: frozenset[str],
    required_seeds: frozenset[str],
) -> None:
    if not rows:
        raise ValueError("input contains no runs")
    if not required_patchers:
        raise ValueError("required_patchers must be a nonempty frozen set")
    if not required_seeds:
        raise ValueError("required_seeds must be a nonempty frozen set")

    run_keys: set[tuple[str, frozenset[str], str, str]] = set()
    pack_definitions: dict[tuple[str, str], frozenset[str]] = {}
    for index, row in enumerate(rows, start=1):
        if not row.task_id or not row.pack_id or not row.patcher or not row.seed:
            raise ValueError(f"run {index}: identifiers must be nonempty")
        if row.patcher not in required_patchers:
            raise ValueError(f"run {index}: unexpected patcher {row.patcher!r}")
        if row.seed not in required_seeds:
            raise ValueError(f"run {index}: unexpected seed {row.seed!r}")
        if not isfinite(row.success) or not 0.0 <= row.success <= 1.0:
            raise ValueError(f"run {index}: success must be finite and in [0,1]")
        if not isfinite(row.token_cost) or row.token_cost < 0:
            raise ValueError(f"run {index}: token_cost must be finite and nonnegative")

        run_key = (row.task_id, row.chunks, row.patcher, row.seed)
        if run_key in run_keys:
            raise ValueError(
                "duplicate run key: "
                f"task={row.task_id!r}, chunks={sorted(row.chunks)!r}, "
                f"patcher={row.patcher!r}, seed={row.seed!r}"
            )
        run_keys.add(run_key)

        pack_key = (row.task_id, row.pack_id)
        previous = pack_definitions.setdefault(pack_key, row.chunks)
        if previous != row.chunks:
            raise ValueError(
                f"pack_id {row.pack_id!r} has inconsistent chunks in task {row.task_id!r}"
            )


def _load_jsonl(path: Path) -> list[Run]:
    rows: list[Run] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            raw = json.loads(line)
            required = {
                "task_id",
                "pack_id",
                "chunks",
                "patcher",
                "seed",
                "success",
                "token_cost",
            }
            missing = required.difference(raw)
            if missing:
                raise ValueError(f"line {line_number}: missing {sorted(missing)}")
            if not isinstance(raw["chunks"], list):
                raise ValueError(f"line {line_number}: chunks must be a list")
            chunk_items = [str(item) for item in raw["chunks"]]
            if len(chunk_items) != len(set(chunk_items)):
                raise ValueError(f"line {line_number}: chunks contains duplicates")
            rows.append(
                Run(
                    task_id=str(raw["task_id"]),
                    pack_id=str(raw["pack_id"]),
                    chunks=frozenset(chunk_items),
                    patcher=str(raw["patcher"]),
                    seed=str(raw["seed"]),
                    success=float(raw["success"]),
                    token_cost=float(raw["token_cost"]),
                )
            )
    if not rows:
        raise ValueError("input contains no runs")
    return rows


def _jaccard(left: frozenset[str], right: frozenset[str]) -> float:
    union = left | right
    if not union:
        return 1.0
    return len(left & right) / len(union)


def _one_deletion_sets(candidate: frozenset[str]) -> set[frozenset[str]]:
    return {candidate.difference({chunk}) for chunk in candidate}


def _proper_subsets(candidate: frozenset[str]) -> set[frozenset[str]]:
    ordered = sorted(candidate)
    return {
        frozenset(subset)
        for size in range(len(ordered))
        for subset in combinations(ordered, size)
    }


def _sorted_sets(values: set[frozenset[str]]) -> list[frozenset[str]]:
    return sorted(values, key=lambda item: (len(item), tuple(sorted(item))))


def analyze(
    rows: list[Run],
    *,
    min_runs: int,
    success_threshold: float,
    max_jaccard: float,
    required_patchers: set[str] | frozenset[str],
    required_seeds: set[str] | frozenset[str],
) -> dict:
    if min_runs < 1:
        raise ValueError("min_runs must be at least one")
    if not 0.0 <= success_threshold <= 1.0:
        raise ValueError("success_threshold must be in [0,1]")
    if not 0.0 <= max_jaccard <= 1.0:
        raise ValueError("max_jaccard must be in [0,1]")

    patcher_grid = frozenset(str(item) for item in required_patchers)
    seed_grid = frozenset(str(item) for item in required_seeds)
    if len(seed_grid) < min_runs:
        raise ValueError("the frozen seed grid is smaller than min_runs")
    _validate_runs(rows, required_patchers=patcher_grid, required_seeds=seed_grid)

    tasks: dict[str, list[Run]] = defaultdict(list)
    for row in rows:
        tasks[row.task_id].append(row)

    task_reports: list[dict] = []
    for task_id in sorted(tasks):
        task_rows = tasks[task_id]
        grouped: dict[tuple[frozenset[str], str], dict[str, Run]] = defaultdict(dict)
        pack_ids: dict[frozenset[str], set[str]] = defaultdict(set)
        costs: dict[frozenset[str], list[float]] = defaultdict(list)
        for row in task_rows:
            grouped[(row.chunks, row.patcher)][row.seed] = row
            pack_ids[row.chunks].add(row.pack_id)
            costs[row.chunks].append(row.token_cost)

        set_status: dict[frozenset[str], str] = {}
        pack_evidence: list[dict] = []
        for chunks in _sorted_sets(set(pack_ids)):
            patcher_evidence: dict[str, dict] = {}
            patcher_states: list[str] = []
            for patcher in sorted(patcher_grid):
                by_seed = grouped.get((chunks, patcher), {})
                observed_seeds = frozenset(by_seed)
                missing_seeds = seed_grid.difference(observed_seeds)
                unexpected_seeds = observed_seeds.difference(seed_grid)
                if not observed_seeds:
                    state = "missing"
                elif missing_seeds or unexpected_seeds:
                    state = "underpowered"
                else:
                    rate = mean(by_seed[seed].success for seed in sorted(seed_grid))
                    state = "sufficient" if rate >= success_threshold else "confirmed_insufficient"
                rate = mean(item.success for item in by_seed.values()) if by_seed else None
                patcher_states.append(state)
                patcher_evidence[patcher] = {
                    "status": state,
                    "runs": len(by_seed),
                    "success_rate": rate,
                    "expected_seeds": sorted(seed_grid),
                    "observed_seeds": sorted(observed_seeds),
                    "missing_seeds": sorted(missing_seeds),
                    "unexpected_seeds": sorted(unexpected_seeds),
                }

            if "missing" in patcher_states:
                aggregate_state = "missing"
            elif "underpowered" in patcher_states:
                aggregate_state = "underpowered"
            elif all(state == "sufficient" for state in patcher_states):
                aggregate_state = "sufficient"
            else:
                aggregate_state = "confirmed_insufficient"
            assert aggregate_state in EVIDENCE_STATES
            set_status[chunks] = aggregate_state
            pack_evidence.append(
                {
                    "pack_ids": sorted(pack_ids[chunks]),
                    "chunks": sorted(chunks),
                    "token_cost_mean": mean(costs[chunks]),
                    "evidence_status": aggregate_state,
                    "portable_sufficient": aggregate_state == "sufficient",
                    "patchers": patcher_evidence,
                }
            )

        sufficient_sets = {chunks for chunks, state in set_status.items() if state == "sufficient"}
        inclusion_family: list[frozenset[str]] = []
        local_family: list[frozenset[str]] = []
        minimality_evidence: list[dict] = []
        for candidate in _sorted_sets(sufficient_sets):
            proper_subsets = _proper_subsets(candidate)
            deletion_sets = _one_deletion_sets(candidate)
            proper_by_state = {
                state: {subset for subset in proper_subsets if set_status.get(subset, "missing") == state}
                for state in sorted(EVIDENCE_STATES)
            }
            deletion_by_state = {
                state: {subset for subset in deletion_sets if set_status.get(subset, "missing") == state}
                for state in sorted(EVIDENCE_STATES)
            }
            inclusion_verified = all(
                set_status.get(subset, "missing") == "confirmed_insufficient"
                for subset in proper_subsets
            )
            local_verified = all(
                set_status.get(subset, "missing") == "confirmed_insufficient"
                for subset in deletion_sets
            )
            if inclusion_verified:
                inclusion_family.append(candidate)
            if local_verified:
                local_family.append(candidate)
            minimality_evidence.append(
                {
                    "chunks": sorted(candidate),
                    "proper_subset_count": len(proper_subsets),
                    "proper_subsets_by_status": {
                        state: [sorted(item) for item in _sorted_sets(values)]
                        for state, values in proper_by_state.items()
                    },
                    "all_proper_subsets_confirmed_insufficient": inclusion_verified,
                    "one_deletion_sets_by_status": {
                        state: [sorted(item) for item in _sorted_sets(values)]
                        for state, values in deletion_by_state.items()
                    },
                    "one_deletion_local_minimum": local_verified,
                }
            )

        pairwise = []
        for index, left in enumerate(inclusion_family):
            for right in inclusion_family[index + 1 :]:
                pairwise.append(
                    {
                        "left": sorted(left),
                        "right": sorted(right),
                        "jaccard": _jaccard(left, right),
                    }
                )
        low_overlap = [item for item in pairwise if item["jaccard"] <= max_jaccard]
        observed_intersection = (
            set.intersection(*(set(item) for item in inclusion_family))
            if inclusion_family
            else set()
        )
        task_reports.append(
            {
                "task_id": task_id,
                "required_patchers": sorted(patcher_grid),
                "required_seeds": sorted(seed_grid),
                "evidence_state_definition": {
                    "sufficient": "complete frozen grid and every patcher meets the success threshold",
                    "confirmed_insufficient": "complete frozen grid and at least one patcher misses the threshold",
                    "underpowered": "some but not all frozen cells were observed",
                    "missing": "at least one required patcher has no observations, or the set was never run",
                },
                "portable_sufficient_count": len(sufficient_sets),
                "inclusion_minimal_definition": "portable sufficient and every proper subset completely evaluated and confirmed insufficient",
                "inclusion_minimal_family_count": len(inclusion_family),
                "inclusion_minimal_family": [sorted(item) for item in inclusion_family],
                "one_deletion_local_family_count": len(local_family),
                "one_deletion_local_family": [sorted(item) for item in local_family],
                "minimality_evidence": minimality_evidence,
                "observed_family_intersection": sorted(observed_intersection),
                "pairwise_jaccard": pairwise,
                "low_overlap_pair_count": len(low_overlap),
                "multi_recipe_trigger": len(low_overlap) > 0,
                "pack_evidence": pack_evidence,
            }
        )

    triggered = sum(report["multi_recipe_trigger"] for report in task_reports)
    return {
        "parameters": {
            "min_runs": min_runs,
            "success_threshold": success_threshold,
            "max_jaccard": max_jaccard,
            "required_patchers": sorted(patcher_grid),
            "required_seeds": sorted(seed_grid),
        },
        "summary": {
            "task_count": len(task_reports),
            "multi_recipe_task_count": triggered,
            "multi_recipe_task_rate": triggered / len(task_reports),
        },
        "tasks": task_reports,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--min-runs", type=int, default=3)
    parser.add_argument("--success-threshold", type=float, default=2 / 3)
    parser.add_argument("--max-jaccard", type=float, default=0.60)
    parser.add_argument("--patcher", action="append", dest="patchers", required=True)
    parser.add_argument("--seed", action="append", dest="seeds", required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    report = analyze(
        _load_jsonl(args.input),
        min_runs=args.min_runs,
        success_threshold=args.success_threshold,
        max_jaccard=args.max_jaccard,
        required_patchers=set(args.patchers),
        required_seeds=set(args.seeds),
    )
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
