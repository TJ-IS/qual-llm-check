"""Run deterministic cost-prioritized, budgeted grounded-program search.

The search compares coarse and refinement applicability while retaining exact
facts and an exact-validity certificate for every transition.
"""

from __future__ import annotations

import argparse
import heapq
import json
import re
from dataclasses import dataclass
from math import isfinite
from pathlib import Path


TYPE_PATTERN = re.compile(r"^([A-Za-z][A-Za-z0-9_]*)<([^<>]+)>$")


@dataclass(frozen=True)
class TypeFact:
    kind: str
    terms: tuple[str, ...]

    @classmethod
    def parse(cls, value: str) -> "TypeFact":
        text = value.strip()
        match = TYPE_PATTERN.fullmatch(text)
        if match:
            terms = tuple(part.strip() for part in match.group(2).split(","))
            if not all(terms):
                raise ValueError(f"invalid empty type term: {value!r}")
            return cls(match.group(1), terms)
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", text):
            return cls(text, ())
        raise ValueError(f"invalid type fact: {value!r}")

    def render(self) -> str:
        if not self.terms:
            return self.kind
        return f"{self.kind}<{','.join(self.terms)}>"

    def key(self, mode: str) -> str:
        return self.render() if mode == "refinement" else self.kind


@dataclass(frozen=True)
class Operator:
    identifier: str
    inputs: tuple[TypeFact, ...]
    outputs: tuple[TypeFact, ...]
    cost: float


def _validate_operators(operators: list[Operator]) -> None:
    identifiers: set[str] = set()
    for operator in operators:
        if not operator.identifier:
            raise ValueError("operator identifiers must be nonempty")
        if operator.identifier in identifiers:
            raise ValueError(f"duplicate operator id: {operator.identifier}")
        identifiers.add(operator.identifier)
        if not isfinite(operator.cost) or operator.cost < 0:
            raise ValueError(f"invalid cost for operator {operator.identifier}")


def _load_spec(path: Path) -> tuple[str, list[TypeFact], list[TypeFact], list[Operator]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    for field in ("task_id", "initial_facts", "obligations", "operators"):
        if field not in raw:
            raise ValueError(f"missing field: {field}")
    operators = [
        Operator(
            identifier=str(item["id"]),
            inputs=tuple(TypeFact.parse(value) for value in item["inputs"]),
            outputs=tuple(TypeFact.parse(value) for value in item["outputs"]),
            cost=float(item["cost"]),
        )
        for item in raw["operators"]
    ]
    _validate_operators(operators)
    return (
        str(raw["task_id"]),
        [TypeFact.parse(value) for value in raw["initial_facts"]],
        [TypeFact.parse(value) for value in raw["obligations"]],
        sorted(operators, key=lambda item: item.identifier),
    )


def enumerate_programs(
    *,
    task_id: str,
    initial_facts: list[TypeFact],
    obligations: list[TypeFact],
    operators: list[Operator],
    mode: str,
    max_depth: int,
    budget: float,
    max_programs: int,
    max_expansions: int,
) -> dict:
    if mode not in {"coarse", "refinement"}:
        raise ValueError("mode must be coarse or refinement")
    if max_depth < 0 or not isfinite(budget) or budget < 0:
        raise ValueError("invalid depth or budget")
    if max_programs < 1 or max_expansions < 1:
        raise ValueError("invalid search limit")
    _validate_operators(operators)
    operators = sorted(operators, key=lambda item: item.identifier)

    initial = frozenset(item.render() for item in initial_facts)
    goals = frozenset(item.key(mode) for item in obligations)
    exact_goals = frozenset(item.render() for item in obligations)
    initial_proof = {TypeFact.parse(fact).key(mode): "INITIAL" for fact in initial}
    serial = 0
    queue: list[
        tuple[
            float,
            int,
            int,
            frozenset[str],
            tuple[str, ...],
            dict[str, str],
            bool,
            tuple[dict, ...],
        ]
    ] = []
    initial_used: tuple[str, ...] = ()
    initial_key = (initial, frozenset(initial_used), True)
    best_cost: dict[tuple[frozenset[str], frozenset[str], bool], float] = {
        initial_key: 0.0
    }
    heapq.heappush(
        queue,
        (0.0, 0, serial, initial, initial_used, initial_proof, True, ()),
    )
    results: list[dict] = []
    valid_results: list[dict] = []
    nominal_program_count = 0
    valid_program_count = 0
    expansions = 0

    while queue and expansions < max_expansions:
        cost, depth, _, facts, used, producer, path_exact_valid, lineage = heapq.heappop(queue)
        state_key = (facts, frozenset(used), path_exact_valid)
        if cost != best_cost.get(state_key):
            continue
        expansions += 1
        fact_keys = {TypeFact.parse(fact).key(mode) for fact in facts}
        nominal_closed = goals.issubset(fact_keys)
        exact_goals_present = exact_goals.issubset(facts)
        semantically_valid = path_exact_valid and exact_goals_present
        if nominal_closed:
            result = {
                "operators": list(used),
                "cost": cost,
                "depth": depth,
                "facts": sorted(facts),
                "discharge_proof": {
                    goal: producer.get(goal, "UNKNOWN") for goal in sorted(goals)
                },
                "transition_exact_valid": path_exact_valid,
                "exact_goals_present": exact_goals_present,
                "refinement_obligations_satisfied": semantically_valid,
                "lineage": list(lineage),
            }
            nominal_program_count += 1
            if len(results) < max_programs:
                results.append(result)
            if semantically_valid:
                valid_program_count += 1
                if len(valid_results) < max_programs:
                    valid_results.append(result)

            # A refinement-closed monotone state needs no extension.  A coarse
            # nominal closure must continue: later exact-valid facts may satisfy
            # the entity-bound obligations that the coarse checker collapsed.
            if mode == "refinement" or semantically_valid:
                continue

        if depth >= max_depth:
            continue

        used_set = set(used)
        for operator in operators:
            if operator.identifier in used_set:
                continue
            input_keys = {item.key(mode) for item in operator.inputs}
            if not input_keys.issubset(fact_keys):
                continue
            next_cost = cost + operator.cost
            if next_cost > budget:
                continue
            output_facts = {item.render() for item in operator.outputs}
            output_keys = {item.key(mode) for item in operator.outputs}
            next_facts = facts | output_facts
            if next_facts == facts:
                continue

            exact_inputs = {item.render() for item in operator.inputs}
            exact_inputs_satisfied = exact_inputs.issubset(facts)
            next_exact_valid = path_exact_valid and exact_inputs_satisfied
            next_used = used + (operator.identifier,)
            next_producer = dict(producer)
            for output in sorted(output_keys):
                next_producer.setdefault(output, operator.identifier)
            transition = {
                "operator": operator.identifier,
                "required_exact_inputs": sorted(exact_inputs),
                "exact_inputs_satisfied": exact_inputs_satisfied,
                "outputs": sorted(output_facts),
            }
            next_lineage = lineage + (transition,)
            next_key = (next_facts, frozenset(next_used), next_exact_valid)
            if next_cost >= best_cost.get(next_key, float("inf")):
                continue
            best_cost[next_key] = next_cost
            serial += 1
            heapq.heappush(
                queue,
                (
                    next_cost,
                    depth + 1,
                    serial,
                    next_facts,
                    next_used,
                    next_producer,
                    next_exact_valid,
                    next_lineage,
                ),
            )

    return {
        "task_id": task_id,
        "mode": mode,
        "search_policy": "deterministic cost-prioritized search with depth, cost, expansion, and result-storage budgets",
        "max_depth": max_depth,
        "budget": budget,
        "obligations": sorted(goals),
        "refinement_obligations": sorted(exact_goals),
        "max_expansions": max_expansions,
        "expansions": expansions,
        "frontier_exhausted": not queue,
        "termination_reason": "frontier_exhausted" if not queue else "max_expansions",
        "program_count": nominal_program_count,
        "stored_program_count": len(results),
        "program_storage_truncated": nominal_program_count > len(results),
        "semantically_valid_program_count": valid_program_count,
        "stored_semantically_valid_program_count": len(valid_results),
        "programs": results,
        "semantically_valid_programs": valid_results,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--mode", choices=("coarse", "refinement"), default="refinement")
    parser.add_argument("--max-depth", type=int, default=3)
    parser.add_argument("--budget", type=float, default=6.0)
    parser.add_argument("--max-programs", type=int, default=1000)
    parser.add_argument("--max-expansions", type=int, default=10000)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    task_id, initial, obligations, operators = _load_spec(args.input)
    report = enumerate_programs(
        task_id=task_id,
        initial_facts=initial,
        obligations=obligations,
        operators=operators,
        mode=args.mode,
        max_depth=args.max_depth,
        budget=args.budget,
        max_programs=args.max_programs,
        max_expansions=args.max_expansions,
    )
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
