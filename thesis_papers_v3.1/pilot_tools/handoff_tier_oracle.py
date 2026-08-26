"""Estimate frozen-information VOI and repair-tier switching.

The scout output is frozen within a task/checkpoint.  Seeds are repeated repair
runs, so this instrument estimates ``max_m E_seed[U_m]`` before and after the
fixed information acquisition.  Acquisition cost is state-level and is
subtracted once outside the repair-tier maximum.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import isfinite
from pathlib import Path
from statistics import mean


StateKey = tuple[str, str]


def _normalize_rows(rows: list[dict]) -> list[dict]:
    if not rows:
        raise ValueError("input contains no runs")
    required = {
        "task_id",
        "checkpoint_id",
        "information",
        "tier",
        "seed",
        "success",
        "repair_cost",
        "acquisition_cost",
    }
    normalized: list[dict] = []
    run_keys: set[tuple[str, str, str, str, str]] = set()
    for index, raw in enumerate(rows, start=1):
        missing = required.difference(raw)
        if missing:
            raise ValueError(f"run {index}: missing {sorted(missing)}")
        row = {
            "task_id": str(raw["task_id"]),
            "checkpoint_id": str(raw["checkpoint_id"]),
            "information": str(raw["information"]),
            "tier": str(raw["tier"]),
            "seed": str(raw["seed"]),
            "success": float(raw["success"]),
            "repair_cost": float(raw["repair_cost"]),
            "acquisition_cost": float(raw["acquisition_cost"]),
        }
        if not row["task_id"] or not row["checkpoint_id"] or not row["tier"] or not row["seed"]:
            raise ValueError(f"run {index}: identifiers must be nonempty")
        if row["information"] not in {"current", "scout"}:
            raise ValueError(f"run {index}: invalid information condition")
        if not isfinite(row["success"]) or not 0.0 <= row["success"] <= 1.0:
            raise ValueError(f"run {index}: success must be finite and in [0,1]")
        if (
            not isfinite(row["repair_cost"])
            or not isfinite(row["acquisition_cost"])
            or row["repair_cost"] < 0
            or row["acquisition_cost"] < 0
        ):
            raise ValueError(f"run {index}: costs must be finite and nonnegative")
        if row["information"] == "current" and row["acquisition_cost"] != 0.0:
            raise ValueError(f"run {index}: current acquisition_cost must be zero")
        key = (
            row["task_id"],
            row["checkpoint_id"],
            row["information"],
            row["tier"],
            row["seed"],
        )
        if key in run_keys:
            raise ValueError(f"duplicate run key: {key!r}")
        run_keys.add(key)
        normalized.append(row)
    return normalized


def _load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise ValueError(f"line {line_number}: invalid JSON") from error
    return _normalize_rows(rows)


def _load_expected_states(path: Path) -> set[StateKey]:
    text = path.read_text(encoding="utf-8")
    stripped = text.strip()
    if not stripped:
        raise ValueError("expected-states file is empty")
    if stripped.startswith("["):
        raw_items = json.loads(stripped)
    else:
        raw_items = [json.loads(line) for line in text.splitlines() if line.strip()]
    states: set[StateKey] = set()
    for index, item in enumerate(raw_items, start=1):
        if "task_id" not in item or "checkpoint_id" not in item:
            raise ValueError(f"expected state {index}: missing task_id or checkpoint_id")
        key = (str(item["task_id"]), str(item["checkpoint_id"]))
        if not key[0] or not key[1]:
            raise ValueError(f"expected state {index}: identifiers must be nonempty")
        if key in states:
            raise ValueError(f"duplicate expected state: {key!r}")
        states.add(key)
    return states


def analyze(
    rows: list[dict],
    *,
    tiers: list[str],
    lambda_cost: float,
    success_value: float,
    min_runs: int,
    strict_pairs: bool = True,
    expected_states: set[StateKey],
    expected_seeds: set[str],
) -> dict:
    if not tiers or len(set(tiers)) != len(tiers) or "abstain" in tiers:
        raise ValueError("repair tiers must be nonempty, unique, and exclude reserved tier 'abstain'")
    if (
        not isfinite(lambda_cost)
        or not isfinite(success_value)
        or lambda_cost < 0
        or success_value <= 0
        or min_runs < 1
    ):
        raise ValueError("invalid analysis parameter")
    if not expected_states:
        raise ValueError("expected_states must be a nonempty frozen set")
    frozen_seeds = {str(seed) for seed in expected_seeds}
    if not frozen_seeds:
        raise ValueError("expected_seeds must be a nonempty frozen set")
    if len(frozen_seeds) < min_runs:
        raise ValueError("the frozen seed grid is smaller than min_runs")

    normalized = _normalize_rows(rows)
    states: dict[StateKey, list[dict]] = defaultdict(list)
    for row in normalized:
        key = (row["task_id"], row["checkpoint_id"])
        if key not in expected_states:
            raise ValueError(f"observed state was not pre-registered: {key!r}")
        if row["tier"] not in tiers:
            raise ValueError(f"unexpected repair tier: {row['tier']!r}")
        if row["seed"] not in frozen_seeds:
            raise ValueError(f"unexpected repair seed: {row['seed']!r}")
        states[key].append(row)

    usable: list[dict] = []
    incomplete: list[dict] = []
    for task_id, checkpoint_id in sorted(expected_states):
        state_rows = states.get((task_id, checkpoint_id), [])
        cells: dict[tuple[str, str], list[dict]] = defaultdict(list)
        for row in state_rows:
            cells[(row["information"], row["tier"])].append(row)

        observed_scout_costs = {
            row["acquisition_cost"] for row in state_rows if row["information"] == "scout"
        }
        if len(observed_scout_costs) > 1:
            raise ValueError(
                f"state {(task_id, checkpoint_id)!r}: scout acquisition_cost must be identical across tiers and seeds"
            )

        seed_sets = {
            f"{information}:{tier}": {row["seed"] for row in cells[(information, tier)]}
            for information in ("current", "scout")
            for tier in tiers
        }
        missing_cells: list[str] = []
        unexpected_cell_seeds: dict[str, list[str]] = {}
        for cell, seeds in seed_sets.items():
            missing = frozen_seeds.difference(seeds)
            unexpected = seeds.difference(frozen_seeds)
            if strict_pairs:
                if missing:
                    missing_cells.append(f"{cell}:missing-seeds={','.join(sorted(missing))}")
                if unexpected:
                    unexpected_cell_seeds[cell] = sorted(unexpected)
            elif len(seeds) < min_runs:
                missing_cells.append(f"{cell}:fewer-than-{min_runs}-runs")

        common_seeds = set.intersection(*seed_sets.values()) if seed_sets else set()
        if not strict_pairs and len(common_seeds) < min_runs:
            missing_cells.append("paired-seeds")
        if strict_pairs:
            analysis_seeds = frozen_seeds
        else:
            analysis_seeds = common_seeds

        if missing_cells or unexpected_cell_seeds:
            incomplete.append(
                {
                    "task_id": task_id,
                    "checkpoint_id": checkpoint_id,
                    "missing": sorted(missing_cells),
                    "unexpected_cell_seeds": unexpected_cell_seeds,
                    "expected_seeds": sorted(frozen_seeds),
                    "cell_seeds": {key: sorted(value) for key, value in seed_sets.items()},
                }
            )
            continue

        filtered = {
            key: [row for row in value if row["seed"] in analysis_seeds]
            for key, value in cells.items()
        }

        # The frozen scout precedes repair-seed repetitions.  Its acquisition
        # cost therefore must not depend on repair tier or repair seed.
        scout_costs = observed_scout_costs
        if len(scout_costs) != 1:
            raise ValueError(
                f"state {(task_id, checkpoint_id)!r}: scout acquisition_cost must be identical across tiers and seeds"
            )
        acquisition_cost = next(iter(scout_costs))

        utilities: dict[str, dict[str, dict]] = {"current": {}, "scout": {}}
        for information in ("current", "scout"):
            for tier in tiers:
                repetitions = filtered[(information, tier)]
                success = mean(row["success"] for row in repetitions)
                repair_cost = mean(row["repair_cost"] for row in repetitions)
                repair_utility = success_value * success - lambda_cost * repair_cost
                utilities[information][tier] = {
                    "runs": len(repetitions),
                    "repair_seeds": sorted(row["seed"] for row in repetitions),
                    "success": success,
                    "repair_cost": repair_cost,
                    "repair_utility_before_acquisition": repair_utility,
                }

        tier_order = {"abstain": -1, **{tier: index for index, tier in enumerate(tiers)}}

        def best(condition: str) -> tuple[str, float]:
            candidates = [("abstain", 0.0)] + [
                (tier, utilities[condition][tier]["repair_utility_before_acquisition"])
                for tier in tiers
            ]
            return max(candidates, key=lambda item: (item[1], -tier_order[item[0]]))

        current_best, current_system_utility = best("current")
        scout_best, scout_pre_acquisition_utility = best("scout")
        scout_system_utility = scout_pre_acquisition_utility - lambda_cost * acquisition_cost
        voi = scout_system_utility - current_system_utility
        continue_recommended = voi > 0
        if continue_recommended:
            recommended_action = "CONTINUE_SCOUT"
        elif current_best == "abstain":
            recommended_action = "ABSTAIN"
        else:
            recommended_action = f"HANDOFF_{current_best}"
        usable.append(
            {
                "task_id": task_id,
                "checkpoint_id": checkpoint_id,
                "repair_seeds": sorted(analysis_seeds),
                "conditions": utilities,
                "acquisition_cost": acquisition_cost,
                "current_best_tier": current_best,
                "scout_best_tier_before_acquisition": scout_best,
                "current_system_utility": current_system_utility,
                "scout_system_utility": scout_system_utility,
                "counterfactual_tier_changed": current_best != scout_best,
                "voi": voi,
                "recommended_action": recommended_action,
                "positive_voi_tier_switch": continue_recommended and current_best != scout_best,
            }
        )

    complete_count = len(usable)
    expected_count = len(expected_states)
    positive = sum(item["voi"] > 0 for item in usable)
    changed = sum(item["counterfactual_tier_changed"] for item in usable)
    positive_switch = sum(item["positive_voi_tier_switch"] for item in usable)

    def complete_case_rate(numerator: int) -> float | None:
        return numerator / complete_count if complete_count else None

    return {
        "parameters": {
            "tiers": tiers,
            "external_option": "abstain with repair utility 0",
            "estimand": "max_m E_repair_seed[U_m | frozen information]; acquisition cost subtracted once after the scout-tier maximum",
            "lambda_cost": lambda_cost,
            "success_value": success_value,
            "min_runs": min_runs,
            "strict_pairs": strict_pairs,
            "expected_states": [
                {"task_id": task_id, "checkpoint_id": checkpoint_id}
                for task_id, checkpoint_id in sorted(expected_states)
            ],
            "expected_seeds": sorted(frozen_seeds),
        },
        "summary": {
            "expected_state_count": expected_count,
            "observed_state_count": len(states),
            "usable_state_count": complete_count,
            "incomplete_state_count": len(incomplete),
            "positive_voi_rate": positive / expected_count,
            "counterfactual_tier_change_rate": changed / expected_count,
            "positive_voi_tier_switch_rate": positive_switch / expected_count,
            "positive_voi_complete_case_rate": complete_case_rate(positive),
            "counterfactual_tier_change_complete_case_rate": complete_case_rate(changed),
            "positive_voi_tier_switch_complete_case_rate": complete_case_rate(positive_switch),
            "primary_rate_denominator": "all pre-registered expected states; incomplete states contribute zero to ITT numerators",
        },
        "states": usable,
        "incomplete_states": incomplete,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--expected-states", type=Path, required=True)
    parser.add_argument("--expected-seed", action="append", dest="expected_seeds", required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tier", action="append", dest="tiers")
    parser.add_argument("--lambda-cost", type=float, required=True)
    parser.add_argument("--success-value", type=float, default=1.0)
    parser.add_argument("--min-runs", type=int, default=2)
    pairing = parser.add_mutually_exclusive_group()
    pairing.add_argument("--strict-pairs", action="store_true", dest="strict_pairs")
    pairing.add_argument("--allow-unpaired", action="store_false", dest="strict_pairs")
    parser.set_defaults(strict_pairs=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    report = analyze(
        _load_jsonl(args.input),
        tiers=args.tiers or ["cheap", "strong"],
        lambda_cost=args.lambda_cost,
        success_value=args.success_value,
        min_runs=args.min_runs,
        strict_pairs=args.strict_pairs,
        expected_states=_load_expected_states(args.expected_states),
        expected_seeds=set(args.expected_seeds),
    )
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
