"""Offline ARB executor for refinement-typed retrieval-program pilots.

This module deliberately separates three phases:

1. ``deployment_task_from_record`` projects a benchmark row onto a frozen
   task-specific query whitelist.  Obligation construction and search receive
   only that projection; they cannot access ``gold``, reference patches, or
   evaluation metrics.
2. ``CachedEvidenceStore`` executes programs from cached official
   lexical/BM25/RepoMap rankings and pre-split ARB corpus chunks.  It does not
   call a model, a network service, tree-sitter, or an AST parser.
3. ``score_execution`` may consume gold files only after deployment output is
   frozen.  Gold is never fed into construction, search, execution, or the
   deployment decision; a labelled post-hoc oracle may rank already-completed
   candidates only to diagnose headroom.

The implementation is intentionally a mechanism pilot, not a learned compiler.
It supports an equal-cost depth-1 parallel hybrid and task-specific depth-2/3
identity-preserving chains.  Coarse and refinement search use the same operator
catalog and cost ledger.  Refinement rejects same-kind/wrong-entity transitions;
each such rejected extension still consumes one search expansion.
"""

from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import math
import re
import time
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from typed_program_oracle import Operator, TypeFact


TASK_RELEASE = {
    "code2test": "v2_code2test",
    "trace2code": "v2_trace2code",
    "edit2ripple": "v2_edit2ripple",
}

# Only these query fields can reach obligation construction or search.  In
# particular, edit2ripple's deployment-visible anchor_diff is intentionally not
# used: the pilot binds the visible anchor file and intent, not patch text.
QUERY_FIELD_WHITELIST = {
    "code2test": (
        "pr_title",
        "pr_body",
        "changed_file",
        "implementation_files",
        "implementation_file_count",
        "changed_file_summary",
    ),
    "trace2code": (
        "failure_excerpt",
        "raw_signal",
        "trace_paths",
        "test_names",
        "command",
        "check_name",
        "run_strategy",
        "source_type",
        "path",
        "line",
        "pr_title",
    ),
    "edit2ripple": ("intent", "anchor_file"),
}

DETAIL_EXECUTION_FIELD_WHITELIST = (
    "sample_id",
    "task_type",
    "repo",
    "base_commit",
    "ranker",
    "top_files",
    "top_file_scores",
)

IDENTIFIER_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]{2,}\b")
PATH_LINE_RE = re.compile(
    r"(?P<path>[A-Za-z0-9_.\-/]+\.(?:c|cc|cpp|cs|go|h|hpp|java|js|jsx|kt|py|pyi|rb|rs|ts|tsx))(?::(?P<line>\d+))?"
)
UNDEFINED_RE = re.compile(
    r"(?:\.|\b)(?P<symbol>[A-Za-z_][A-Za-z0-9_]*)\s+(?:undefined|is not defined|not found)",
    re.IGNORECASE,
)
ATTRIBUTE_RE = re.compile(
    r"(?:attribute|method|field)[^\n]{0,80}['\"](?P<symbol>[A-Za-z_][A-Za-z0-9_]*)['\"]",
    re.IGNORECASE,
)
CAMEL_BOUNDARY_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")
CANONICAL_TOKENIZER = "regex_code_tokenizer_v1"
CANONICAL_TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|[0-9]+|[^A-Za-z0-9_\s]", re.UNICODE)
CANONICAL_COVERAGE_THRESHOLDS = (1, 16, 32, 64, 128)
STOP_TERMS = {
    "about",
    "after",
    "before",
    "changed",
    "class",
    "error",
    "failed",
    "failure",
    "files",
    "implementation",
    "method",
    "return",
    "should",
    "source",
    "test",
    "tests",
    "this",
    "using",
    "with",
    "self",
    "true",
    "false",
    "none",
    "null",
    "public",
    "private",
    "protected",
    "static",
    "final",
    "function",
    "value",
    "values",
    "string",
}


@dataclass(frozen=True)
class DeploymentTask:
    sample_id: str
    task_type: str
    repo: str
    base_commit: str
    visible_query: Mapping[str, Any]
    source_fields: tuple[str, ...]
    query_digest: str

    @property
    def query_text(self) -> str:
        return json.dumps(self.visible_query, ensure_ascii=False, sort_keys=True)


@dataclass(frozen=True)
class Anchor:
    entity: str
    source_kind: str
    label: str
    path: str | None
    terms: tuple[str, ...]


@dataclass(frozen=True)
class OperatorBinding:
    operator: Operator
    action: str
    anchor_entity: str | None


@dataclass(frozen=True)
class ProgramSpec:
    task: DeploymentTask
    anchors: tuple[Anchor, ...]
    candidate_entities: tuple[str, ...]
    initial_facts: tuple[TypeFact, ...]
    obligations: tuple[TypeFact, ...]
    obligation_semantics: str
    operators: tuple[Operator, ...]
    bindings: Mapping[str, OperatorBinding]
    chain_depth: int
    retrieval_transition_depth: int
    evidence_kind: str
    hybrid_cost: float = 3.0


@dataclass(frozen=True)
class CompileResult:
    decision: str
    reason: str | None
    spec: ProgramSpec | None
    audit: Mapping[str, Any]


@dataclass(frozen=True)
class ChunkRef:
    path: str
    chunk_id: str
    start_line: int
    end_line: int
    symbol: str
    char_count: int
    match_terms: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvidenceBundle:
    origin_entity: str
    files: tuple[str, ...]
    chunks: tuple[ChunkRef, ...]
    relation_terms: tuple[str, ...]
    certificate_valid: bool


def _canonical_digest(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def deployment_task_from_record(record: Mapping[str, Any]) -> DeploymentTask:
    """Create the only object visible to constructors and search.

    The function never requests ``gold``, ``metadata``, ``audit``, patch, or
    metric keys from ``record``.  Tests use guarded mappings to enforce this.
    """

    task_type = str(record.get("task_type") or "")
    if task_type not in TASK_RELEASE:
        raise ValueError(f"unsupported task_type: {task_type!r}")
    raw_query = record.get("query")
    if not isinstance(raw_query, Mapping):
        raw_query = {}
    allowed = QUERY_FIELD_WHITELIST[task_type]
    visible_query = {key: raw_query.get(key) for key in allowed if raw_query.get(key) is not None}
    identity = {
        "sample_id": str(record.get("id") or record.get("sample_id") or ""),
        "task_type": task_type,
        "repo": str(record.get("repo") or ""),
        "base_commit": str(record.get("base_commit") or ""),
        "query": visible_query,
    }
    if not all(identity[key] for key in ("sample_id", "repo", "base_commit")):
        raise ValueError("sample id, repo, and base_commit are required")
    return DeploymentTask(
        sample_id=identity["sample_id"],
        task_type=task_type,
        repo=identity["repo"],
        base_commit=identity["base_commit"],
        visible_query=visible_query,
        source_fields=tuple(f"query.{key}" for key in visible_query),
        query_digest=_canonical_digest((task_type, visible_query)),
    )


def _normal_path(value: str) -> str:
    normalized = value.replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _terms_from_text(text: str, limit: int = 12) -> tuple[str, ...]:
    expanded = CAMEL_BOUNDARY_RE.sub(" ", text)
    values: list[str] = []
    seen: set[str] = set()
    for token in TOKEN_RE.findall(expanded):
        lowered = token.lower()
        if len(lowered) < 3 or lowered in STOP_TERMS or lowered.isdigit() or lowered in seen:
            continue
        values.append(token)
        seen.add(lowered)
        if len(values) >= limit:
            break
    return tuple(values)


def _make_anchor(task_type: str, source_kind: str, label: str, path: str | None, terms: Iterable[str]) -> Anchor:
    normalized_path = _normal_path(path) if path else None
    if source_kind == "failure_symbol":
        cleaned_terms = tuple(
            dict.fromkeys(
                str(term).strip()
                for term in terms
                if term and IDENTIFIER_RE.fullmatch(str(term).strip())
            )
        )[:16]
    else:
        cleaned_terms = _terms_from_text(" ".join(str(term) for term in terms if term), limit=16)
    entity = "e_" + hashlib.sha256(
        f"{task_type}\0{source_kind}\0{label}".encode("utf-8")
    ).hexdigest()[:16]
    return Anchor(entity, source_kind, label, normalized_path, cleaned_terms)


def _dedupe_anchors(anchors: Iterable[Anchor]) -> tuple[Anchor, ...]:
    output: list[Anchor] = []
    seen: set[tuple[str, str]] = set()
    for anchor in anchors:
        key = (anchor.source_kind, anchor.label.lower())
        if key in seen or (not anchor.path and not anchor.terms):
            continue
        output.append(anchor)
        seen.add(key)
    return tuple(output)


def construct_query_anchors(task: DeploymentTask) -> tuple[Anchor, ...]:
    """Construct anchors solely from the frozen visible-query projection."""

    query = task.visible_query
    anchors: list[Anchor] = []
    if task.task_type == "code2test":
        files = query.get("implementation_files") or []
        if isinstance(files, Sequence) and not isinstance(files, (str, bytes)):
            for value in files:
                if not isinstance(value, str) or not value.strip():
                    continue
                path = _normal_path(value)
                stem = PurePosixPath(path).stem
                anchors.append(_make_anchor(task.task_type, "implementation_file", path, path, (stem,)))
        changed_file = query.get("changed_file")
        if isinstance(changed_file, str) and changed_file.strip():
            path = _normal_path(changed_file)
            anchors.append(
                _make_anchor(
                    task.task_type,
                    "implementation_file",
                    path,
                    path,
                    (PurePosixPath(path).stem,),
                )
            )
    elif task.task_type == "trace2code":
        text = "\n".join(
            str(query.get(key) or "") for key in ("failure_excerpt", "raw_signal", "pr_title")
        )
        for pattern in (UNDEFINED_RE, ATTRIBUTE_RE):
            for match in pattern.finditer(text):
                symbol = match.group("symbol")
                anchors.append(_make_anchor(task.task_type, "failure_symbol", symbol, None, (symbol,)))
        trace_paths = query.get("trace_paths") or []
        if isinstance(trace_paths, Sequence) and not isinstance(trace_paths, (str, bytes)):
            for value in trace_paths:
                if isinstance(value, str) and value.strip():
                    path = _normal_path(value)
                    anchors.append(
                        _make_anchor(task.task_type, "trace_path", path, path, (PurePosixPath(path).stem,))
                    )
        for match in PATH_LINE_RE.finditer(text):
            path = _normal_path(match.group("path"))
            anchors.append(_make_anchor(task.task_type, "trace_path", path, path, (PurePosixPath(path).stem,)))
    else:  # edit2ripple
        value = query.get("anchor_file")
        if isinstance(value, str) and value.strip():
            path = _normal_path(value)
            intent_terms = _terms_from_text(str(query.get("intent") or ""), limit=8)
            anchors.append(
                _make_anchor(
                    task.task_type,
                    "anchor_file",
                    path,
                    path,
                    (PurePosixPath(path).stem, *intent_terms),
                )
            )
    return _dedupe_anchors(anchors)


def compile_program_spec(task: DeploymentTask) -> CompileResult:
    anchors = construct_query_anchors(task)
    audit = {
        "constructor": "frozen_task_specific_query_only_v0",
        "source_fields": list(task.source_fields),
        "query_digest": task.query_digest,
        "forbidden_sources_not_available": [
            "gold",
            "gold_spans",
            "gold_blocks",
            "reference_patch",
            "fix_commit",
            "evaluation_metrics",
        ],
        "edit2ripple_anchor_diff_used": False,
        "anchor_catalog_truncated": False,
        "anchor_count": len(anchors),
    }
    if not anchors:
        return CompileResult("ABSTAIN", "NO_QUERY_ANCHOR", None, audit)

    query_entity = "q_" + task.query_digest[:16]
    if task.task_type == "trace2code":
        anchor_kind, bound_kind, candidate_kind, evidence_kind, chain_depth = (
            "FailureAnchor",
            "BoundCodeEntity",
            None,
            "RootCauseEvidence",
            2,
        )
    elif task.task_type == "code2test":
        anchor_kind, bound_kind, candidate_kind, evidence_kind, chain_depth = (
            "SourceAnchor",
            "BoundSourceEntity",
            "TestCandidate",
            "TestEvidence",
            3,
        )
    else:
        anchor_kind, bound_kind, candidate_kind, evidence_kind, chain_depth = (
            "EditAnchor",
            "BoundEditEntity",
            "DependentCandidate",
            "RippleEvidence",
            3,
        )

    fact = TypeFact.parse
    initial = [fact(f"Query<{query_entity}>")]
    initial.extend(fact(f"{anchor_kind}<{anchor.entity}>") for anchor in anchors)
    # Every deployment-visible query anchor defines its own identity-preserving
    # candidate branch.  Closure is existential across branches: a program
    # must produce Evidence<e> for the same e it bound, but input ordering does
    # not privilege anchors[0].  Multi-obligation conjunctive programs would
    # require a separate grammar and a larger frozen budget.
    obligations = tuple(fact(f"{evidence_kind}<{anchor.entity}>") for anchor in anchors)
    bindings: dict[str, OperatorBinding] = {}

    hybrid = Operator(
        "00_parallel_hybrid",
        (fact(f"Query<{query_entity}>"),),
        (fact(f"{evidence_kind}<{query_entity}>"),),
        3.0,
    )
    bindings[hybrid.identifier] = OperatorBinding(hybrid, "parallel_hybrid", None)

    for index, anchor in enumerate(anchors):
        bind = Operator(
            f"10_bind_{index:02d}_{anchor.entity}",
            (fact(f"{anchor_kind}<{anchor.entity}>"),),
            (fact(f"{bound_kind}<{anchor.entity}>"),),
            1.0,
        )
        bindings[bind.identifier] = OperatorBinding(bind, "bind_anchor", anchor.entity)
        if chain_depth == 2:
            follow = Operator(
                f"20_follow_{index:02d}_{anchor.entity}",
                (fact(f"{bound_kind}<{anchor.entity}>"),),
                (fact(f"{evidence_kind}<{anchor.entity}>"),),
                2.0,
            )
            bindings[follow.identifier] = OperatorBinding(follow, "follow_relation", anchor.entity)
        else:
            follow = Operator(
                f"20_follow_{index:02d}_{anchor.entity}",
                (fact(f"{bound_kind}<{anchor.entity}>"),),
                (fact(f"{candidate_kind}<{anchor.entity}>"),),
                1.0,
            )
            certify = Operator(
                f"30_certify_{index:02d}_{anchor.entity}",
                (fact(f"{candidate_kind}<{anchor.entity}>"),),
                (fact(f"{evidence_kind}<{anchor.entity}>"),),
                1.0,
            )
            bindings[follow.identifier] = OperatorBinding(follow, "follow_relation", anchor.entity)
            bindings[certify.identifier] = OperatorBinding(certify, "certify_lineage", anchor.entity)

    operators = tuple(sorted((binding.operator for binding in bindings.values()), key=lambda op: op.identifier))
    spec = ProgramSpec(
        task=task,
        anchors=anchors,
        candidate_entities=tuple(anchor.entity for anchor in anchors),
        initial_facts=tuple(initial),
        obligations=obligations,
        obligation_semantics="existential_identity_preserving_branch",
        operators=operators,
        bindings=bindings,
        chain_depth=chain_depth,
        retrieval_transition_depth=2,
        evidence_kind=evidence_kind,
    )
    return CompileResult("PROGRAM", None, spec, audit)


def _fact_kinds(facts: Iterable[str]) -> set[str]:
    return {TypeFact.parse(value).kind for value in facts}


def _grammar_allows(spec: ProgramSpec, used: Sequence[str], identifier: str) -> bool:
    """Frozen single-branch grammar; anchors are alternatives, not mixtures."""

    next_action = spec.bindings[identifier].action
    actions = tuple(spec.bindings[value].action for value in used)
    if not actions:
        return next_action in {"parallel_hybrid", "bind_anchor"}
    if actions == ("bind_anchor",):
        return next_action == "follow_relation"
    if actions == ("bind_anchor", "follow_relation") and spec.chain_depth == 3:
        return next_action == "certify_lineage"
    return False


def search_programs(
    spec: ProgramSpec,
    *,
    mode: str,
    budget: float = 3.0,
    max_depth: int = 3,
    max_expansions: int = 512,
    max_programs: int = 500,
) -> dict[str, Any]:
    """Deterministic cost-prioritized finite search with a unified ledger.

    An expansion is an attempted operator extension whose *coarse* input kinds
    are present.  A refinement rejection, budget rejection, or successful
    enqueue each consumes exactly one expansion.
    """

    if mode not in {"coarse", "refinement"}:
        raise ValueError("mode must be coarse or refinement")
    if not math.isfinite(budget) or budget < 0 or max_depth < 0:
        raise ValueError("invalid budget or max_depth")
    if max_expansions < 1 or max_programs < 1:
        raise ValueError("search limits must be positive")

    initial = frozenset(item.render() for item in spec.initial_facts)
    operators = tuple(sorted(spec.operators, key=lambda item: item.identifier))
    exact_goals = frozenset(item.render() for item in spec.obligations)
    nominal_goals = frozenset(item.kind for item in spec.obligations)
    serial = 0
    # Insertion order must never decide which state survives a finite budget.
    # The stable prefix is cost, depth, canonical operator-id sequence, sorted
    # facts, and exact-validity.  ``serial`` can only distinguish states whose
    # semantic ordering keys are already identical (normally deduplicated).
    queue: list[
        tuple[
            float,
            int,
            tuple[str, ...],
            tuple[str, ...],
            int,
            int,
            frozenset[str],
            bool,
            tuple[dict[str, Any], ...],
        ]
    ] = []
    heapq.heappush(queue, (0.0, 0, (), tuple(sorted(initial)), 0, serial, initial, True, ()))
    best_cost: dict[tuple[frozenset[str], frozenset[str], bool], float] = {
        (initial, frozenset(), True): 0.0
    }
    programs: list[dict[str, Any]] = []
    nominal_count = 0
    valid_count = 0
    expansions = 0
    popped_states = 0
    rejected_wrong_entity = 0
    rejected_budget = 0
    limit_hit = False

    while queue and not limit_hit:
        cost, depth, used, _facts_key, _exact_key, _order, facts, path_exact, lineage = heapq.heappop(queue)
        state_key = (facts, frozenset(used), path_exact)
        if cost != best_cost.get(state_key):
            continue
        popped_states += 1
        kinds = _fact_kinds(facts)
        # Candidate anchors are alternative latent programs, not a hidden
        # conjunction.  A branch closes only on its own exact entity; the
        # coarse space closes on an evidence kind regardless of entity.
        nominal_closed = bool(nominal_goals & kinds)
        satisfied_exact_goals = exact_goals & facts
        exact_closed = bool(satisfied_exact_goals)
        semantically_valid = path_exact and exact_closed
        search_closed = exact_closed if mode == "refinement" else nominal_closed
        if search_closed:
            nominal_count += 1
            valid_count += int(semantically_valid)
            if len(programs) < max_programs:
                programs.append(
                    {
                        "operators": list(used),
                        "cost": cost,
                        "depth": depth,
                        "transition_exact_valid": path_exact,
                        "exact_goals_present": exact_closed,
                        "satisfied_exact_goals": sorted(satisfied_exact_goals),
                        "refinement_obligations_satisfied": semantically_valid,
                        "lineage": list(lineage),
                    }
                )
            # Exact closure needs no extension.  Coarse nominal closure that is
            # entity-invalid continues so it can still reach an exact program.
            if semantically_valid or mode == "refinement":
                continue
        if depth >= max_depth:
            continue

        used_set = set(used)
        for operator in operators:
            if operator.identifier in used_set:
                continue
            if not _grammar_allows(spec, used, operator.identifier):
                continue
            required_kinds = {value.kind for value in operator.inputs}
            if not required_kinds.issubset(kinds):
                continue
            if expansions >= max_expansions:
                limit_hit = True
                break
            expansions += 1
            required_exact = {value.render() for value in operator.inputs}
            exact_inputs = required_exact.issubset(facts)
            if mode == "refinement" and not exact_inputs:
                rejected_wrong_entity += 1
                continue
            next_cost = cost + operator.cost
            if next_cost > budget:
                rejected_budget += 1
                continue
            outputs = frozenset(value.render() for value in operator.outputs)
            next_facts = facts | outputs
            if next_facts == facts:
                continue
            next_used = used + (operator.identifier,)
            next_exact = path_exact and exact_inputs
            transition = {
                "operator": operator.identifier,
                "required_exact_inputs": sorted(required_exact),
                "exact_inputs_satisfied": exact_inputs,
                "outputs": sorted(outputs),
            }
            next_lineage = lineage + (transition,)
            next_key = (next_facts, frozenset(next_used), next_exact)
            if next_cost >= best_cost.get(next_key, float("inf")):
                continue
            best_cost[next_key] = next_cost
            serial += 1
            heapq.heappush(
                queue,
                (
                    next_cost,
                    depth + 1,
                    next_used,
                    tuple(sorted(next_facts)),
                    0 if next_exact else 1,
                    serial,
                    next_facts,
                    next_exact,
                    next_lineage,
                ),
            )

    stored_valid = sum(1 for row in programs if row["refinement_obligations_satisfied"])
    return {
        "task_id": spec.task.sample_id,
        "mode": mode,
        "search_policy": "deterministic cost-prioritized; every nominally-applicable attempted extension costs one expansion",
        "program_grammar": "hybrid OR bind->follow[->certify], exactly one latent anchor branch per program",
        "tie_break_policy": "cost, depth, canonical operator-id tuple, sorted exact facts, exact-validity; insertion serial only after identical semantic keys",
        "space_relation": "refinement applicability is a subset of the same coarse operator space",
        "coarse_exhaustive_oracle_can_be_below_refinement": False,
        "budget": budget,
        "max_depth": max_depth,
        "max_expansions": max_expansions,
        "expansions": expansions,
        "popped_states": popped_states,
        "wrong_entity_rejections": rejected_wrong_entity,
        "budget_rejections": rejected_budget,
        "frontier_exhausted": not queue and not limit_hit,
        "termination_reason": "max_expansions" if limit_hit else "frontier_exhausted",
        "program_count": nominal_count,
        "semantically_valid_program_count": valid_count,
        "stored_program_count": len(programs),
        "stored_semantically_valid_program_count": stored_valid,
        "program_storage_truncated": nominal_count > len(programs),
        "programs": programs,
    }


def validate_program(spec: ProgramSpec, operator_ids: Sequence[str], mode: str) -> dict[str, Any]:
    if mode not in {"coarse", "refinement"}:
        raise ValueError("mode must be coarse or refinement")
    facts = {item.render() for item in spec.initial_facts}
    seen: set[str] = set()
    seen_order: list[str] = []
    lineage: list[dict[str, Any]] = []
    for identifier in operator_ids:
        binding = spec.bindings.get(identifier)
        if binding is None:
            return {"valid": False, "reason": "UNKNOWN_OPERATOR", "operator": identifier, "lineage": lineage}
        if identifier in seen:
            return {"valid": False, "reason": "REUSED_OPERATOR", "operator": identifier, "lineage": lineage}
        operator = binding.operator
        kinds = _fact_kinds(facts)
        required_kinds = {value.kind for value in operator.inputs}
        if not required_kinds.issubset(kinds):
            return {
                "valid": False,
                "reason": "BROKEN_PREREQUISITE",
                "operator": identifier,
                "lineage": lineage,
            }
        if not _grammar_allows(spec, tuple(seen_order), identifier):
            return {
                "valid": False,
                "reason": "BROKEN_PROGRAM_GRAMMAR",
                "operator": identifier,
                "lineage": lineage,
            }
        required_exact = {value.render() for value in operator.inputs}
        exact = required_exact.issubset(facts)
        if mode == "refinement" and not exact:
            return {
                "valid": False,
                "reason": "WRONG_ENTITY_BINDING",
                "operator": identifier,
                "lineage": lineage,
            }
        facts.update(value.render() for value in operator.outputs)
        seen.add(identifier)
        seen_order.append(identifier)
        lineage.append(
            {
                "operator": identifier,
                "exact_inputs_satisfied": exact,
                "required_exact_inputs": sorted(required_exact),
            }
        )
    exact_goals = {item.render() for item in spec.obligations}
    goal_kinds = {item.kind for item in spec.obligations}
    nominal_closed = bool(goal_kinds & _fact_kinds(facts))
    satisfied_exact_goals = exact_goals & facts
    exact_closed = bool(satisfied_exact_goals)
    closed = exact_closed if mode == "refinement" else nominal_closed
    return {
        "valid": closed,
        "reason": None if closed else "OBLIGATIONS_OPEN",
        "exact_goals_present": exact_closed,
        "satisfied_exact_goals": sorted(satisfied_exact_goals),
        "transition_exact_valid": all(row["exact_inputs_satisfied"] for row in lineage),
        "lineage": lineage,
    }


class SyntheticEvidenceStore:
    """Small deterministic store used by unit tests and mechanism examples."""

    def __init__(
        self,
        *,
        hybrid_files: Sequence[str] = (),
        bound_files: Mapping[str, Sequence[str]] | None = None,
        relation_files: Mapping[str, Sequence[str]] | None = None,
        chars_per_file: int = 100,
    ) -> None:
        self.hybrid_files = tuple(hybrid_files)
        self.bound_files = {key: tuple(value) for key, value in (bound_files or {}).items()}
        self.relation_files = {key: tuple(value) for key, value in (relation_files or {}).items()}
        self.chars_per_file = chars_per_file
        self.capability_report = {
            "backend": "synthetic",
            "tree_sitter_required": False,
            "cloud_model_calls": 0,
            "corpus_complete_for_selected_paths": True,
        }

    def _bundle(self, entity: str, files: Sequence[str], terms: Sequence[str], certificate: bool) -> EvidenceBundle:
        files = tuple(dict.fromkeys(files))[:20]
        refs = tuple(
            ChunkRef(path, f"synthetic:{index}", 1, 1, "", self.chars_per_file, tuple(terms))
            for index, path in enumerate(files)
        )
        return EvidenceBundle(entity, tuple(files), refs, tuple(terms), certificate)

    def apply(
        self,
        action: str,
        task: DeploymentTask,
        anchor: Anchor | None,
        incoming: EvidenceBundle,
    ) -> tuple[EvidenceBundle, dict[str, Any]]:
        if action == "parallel_hybrid":
            return self._bundle(incoming.origin_entity, self.hybrid_files, (), False), {
                "cost_units": 3.0,
                "ranker_probes": 3,
            }
        if anchor is None:
            raise ValueError(f"action {action} requires an anchor")
        if action == "bind_anchor":
            files = self.bound_files.get(anchor.entity, ())
            return self._bundle(anchor.entity, files, anchor.terms, bool(files)), {
                "cost_units": 1.0,
                "corpus_path_queries": 1,
            }
        if action == "follow_relation":
            files = self.relation_files.get(incoming.origin_entity, ())
            bundle = self._bundle(
                incoming.origin_entity,
                files,
                incoming.relation_terms,
                incoming.certificate_valid and incoming.origin_entity == anchor.entity,
            )
            return bundle, {
                "cost_units": 2.0 if task.task_type == "trace2code" else 1.0,
                "corpus_entity_queries": 1,
                "lineage_checks": 1 if task.task_type == "trace2code" else 0,
            }
        if action == "certify_lineage":
            return EvidenceBundle(
                incoming.origin_entity,
                incoming.files,
                incoming.chunks,
                incoming.relation_terms,
                incoming.certificate_valid and incoming.origin_entity == anchor.entity,
            ), {"cost_units": 1.0, "lineage_checks": 1}
        raise ValueError(f"unknown action: {action}")


def _safe_detail_projection(row: Mapping[str, Any]) -> dict[str, Any]:
    return {key: row.get(key) for key in DETAIL_EXECUTION_FIELD_WHITELIST if row.get(key) is not None}


def _read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"expected object at {path}:{line_number}")
            yield value


def _find_row(path: Path, key: str, value: str) -> dict[str, Any]:
    for row in _read_jsonl(path):
        if str(row.get(key) or "") == value:
            return row
    raise ValueError(f"{key}={value!r} not found in {path}")


def _is_test_path(path: str) -> bool:
    normalized = path.replace("\\", "/").lower()
    parts = set(normalized.split("/"))
    name = PurePosixPath(normalized).name
    return bool(parts & {"test", "tests", "testing", "testdata", "testsuite", "__tests__"}) or (
        name.startswith("test_")
        or name.endswith(("_test.go", "_test.py", "_test.rs", ".test.js", ".test.ts", ".spec.js", ".spec.ts"))
    )


def _term_hits(text: str, terms: Sequence[str]) -> tuple[str, ...]:
    # Building the text token set once is equivalent to the prior exact-token
    # boundary regex but remains tractable when a bound file exposes hundreds
    # of complete raw symbols.
    present = {match.group(0).lower() for match in IDENTIFIER_RE.finditer(text)}
    return tuple(term for term in terms if len(term) >= 3 and term.lower() in present)


def _compact_chunk(row: Mapping[str, Any], path: str | None = None) -> dict[str, Any]:
    return {
        "path": path if path is not None else _normal_path(str(row.get("path") or "")),
        "chunk_id": str(row.get("chunk_id") or ""),
        "start_line": int(row.get("start_line") or 0),
        "end_line": int(row.get("end_line") or 0),
        "kind": str(row.get("kind") or ""),
        "symbol": str(row.get("symbol") or ""),
        "text": str(row.get("text") or ""),
    }


def _anchor_identifiers(anchor: Anchor, rows: Sequence[Mapping[str, Any]]) -> tuple[str, ...]:
    """Extract whole raw anchor-symbol tokens without AST, subwords, or gold.

    This frozen reduced catalog uses only a failure label, a legal path stem,
    and ARB ``symbol`` fields from bound rows.  It is not the lexical closure
    of every identifier appearing in bound file text.
    """

    candidates: list[str] = []
    if anchor.source_kind == "failure_symbol":
        candidates.append(anchor.label)
    if anchor.path:
        stem = PurePosixPath(anchor.path).stem
        if IDENTIFIER_RE.fullmatch(stem):
            candidates.append(stem)
    # For path-bound anchors, corpus ``symbol`` fields are the strongest
    # available no-parser identity signal.  Query intent terms and identifiers
    # found only in bound file text are not promoted into this reduced catalog.
    for row in rows:
        symbol = str(row.get("symbol") or "")
        if symbol:
            candidates.append(symbol)
    output: list[str] = []
    seen: set[str] = set()
    for value in candidates:
        term = value.strip()
        lowered = term.lower()
        if (
            not IDENTIFIER_RE.fullmatch(term)
            or lowered in seen
            or lowered in STOP_TERMS
            or len(lowered) < 3
        ):
            continue
        output.append(term)
        seen.add(lowered)
    return tuple(output)


class CachedEvidenceStore:
    """Gold-blind executor over official ranks and corpus-wide identifier postings.

    Cached top-file lists are used only by the depth-1 parallel hybrid.  Typed
    bind/follow operators use a two-pass scan of the full pre-split snapshot:
    pass 1 binds query anchors and extracts exact identifiers; pass 2 builds
    task-filtered exact-identifier postings.  These postings may return files
    absent from every official top-20 list.

    ARB chunks do not encode a sound call/import graph, so this backend is
    explicitly an exact-identifier lineage pilot, not call/import semantics.
    """

    def __init__(
        self,
        task: DeploymentTask,
        ranked_paths: Mapping[str, Sequence[str]],
        chunks_by_path: Mapping[str, Sequence[Mapping[str, Any]]],
        anchors: Sequence[Anchor],
        bound_rows: Mapping[str, Sequence[Mapping[str, Any]]],
        relation_rows: Mapping[str, Sequence[Mapping[str, Any]]],
        identifiers: Mapping[str, Sequence[str]],
        canonical_file_texts: Mapping[str, str],
        io_audit: Mapping[str, Any],
    ) -> None:
        self.task = task
        self.ranked_paths = {key: tuple(value) for key, value in ranked_paths.items()}
        self._chunks_by_path = {key: tuple(dict(row) for row in value) for key, value in chunks_by_path.items()}
        self._anchors = {anchor.entity: anchor for anchor in anchors}
        self._bound_rows = {key: tuple(dict(row) for row in value) for key, value in bound_rows.items()}
        self._relation_rows = {key: tuple(dict(row) for row in value) for key, value in relation_rows.items()}
        self._identifiers = {key: tuple(value) for key, value in identifiers.items()}
        self.canonical_file_texts = dict(canonical_file_texts)
        self.io_audit = dict(io_audit)
        self.capability_report = {
            "backend": "cached_hybrid_ranks_plus_two_pass_corpus_wide_exact_identifier_postings",
            "semantic_relation_backend": "whole_token_identifier_occurrence_provenance",
            "identifier_matching": "case-insensitive whole raw anchor-symbol token only",
            "anchor_symbol_catalog_sources": ["failure label", "legal path stem", "bound ARB symbol field"],
            "bound_file_text_identifier_closure": False,
            "camel_or_snake_subword_expansion": False,
            "call_graph_semantics": False,
            "import_graph_semantics": False,
            "typed_candidates_can_escape_hybrid_top20_union": True,
            "hybrid_ranking_rule": "RRF over lexical/BM25/RepoMap, preserve fused[:20] unique file order",
            "typed_ranking_rule": "aggregate exact-identifier hits by file; descending unique identifiers, descending matching chunks, lexical path; top 20 unique files",
            "canonical_bcy_tokenizer": CANONICAL_TOKENIZER,
            "canonical_renderer": "### {path}\\n{kind=file corpus text}\\n",
            "tree_sitter_required": False,
            "ast_parser_required": False,
            "cloud_model_calls": 0,
            "execution_detail_fields": list(DETAIL_EXECUTION_FIELD_WHITELIST),
            "gold_fields_copied_to_executor": [],
            "corpus_full_scan_complete": bool(io_audit.get("full_scan_complete")),
            "corpus_complete_for_selected_paths": bool(io_audit.get("all_selected_paths_observed")),
            "scaling_gap": "postings and canonical file texts are rebuilt with three full JSONL passes per sample; persist a reusable per-snapshot index before the 60-task run",
        }

    @classmethod
    def from_cached_arb(cls, task: DeploymentTask, arb_data_root: Path) -> "CachedEvidenceStore":
        release = TASK_RELEASE[task.task_type]
        eval_dir = arb_data_root / "pilot_eval" / release
        ranked: dict[str, tuple[str, ...]] = {}
        detail_paths = {
            "lexical": eval_dir / "lexical_details.jsonl",
            "bm25": eval_dir / "bm25_details.jsonl",
            "repomap": eval_dir / "repomap_details.jsonl",
        }
        for method, path in detail_paths.items():
            if not path.exists():
                raise FileNotFoundError(path)
            raw = _find_row(path, "sample_id", task.sample_id)
            safe = _safe_detail_projection(raw)
            for field, expected in (
                ("task_type", task.task_type),
                ("repo", task.repo),
                ("base_commit", task.base_commit),
            ):
                if str(safe.get(field) or "") != expected:
                    raise ValueError(f"cached detail {field} mismatch for {task.sample_id}")
            top_files = safe.get("top_files") or []
            if not isinstance(top_files, list):
                raise ValueError(f"top_files must be a list in {path}")
            ranked[method] = tuple(_normal_path(str(value)) for value in top_files if value)

        manifest_path = arb_data_root / "pilot_corpus" / release / "corpus_manifest.jsonl"
        manifest_row = None
        for row in _read_jsonl(manifest_path):
            if row.get("repo") == task.repo and row.get("base_commit") == task.base_commit:
                manifest_row = row
                break
        if manifest_row is None:
            raise ValueError(f"corpus manifest row missing for {task.repo}@{task.base_commit}")
        chunks_path = Path(str(manifest_row.get("chunks_path") or ""))
        if not chunks_path.exists():
            raise FileNotFoundError(chunks_path)

        anchors = construct_query_anchors(task)
        hybrid_paths = {path for values in ranked.values() for path in values}
        selected_paths = set(hybrid_paths)
        for anchor in anchors:
            if anchor.path:
                selected_paths.add(anchor.path)
        chunks_by_path: dict[str, list[dict[str, Any]]] = {path: [] for path in selected_paths}
        bound_rows: dict[str, list[dict[str, Any]]] = {anchor.entity: [] for anchor in anchors}
        bind_truncated = {anchor.entity: False for anchor in anchors}
        pass1_rows = 0
        pass1_bytes = 0
        pass1_started = time.perf_counter()
        with chunks_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                pass1_rows += 1
                pass1_bytes += len(line.encode("utf-8"))
                row = json.loads(line)
                path = _normal_path(str(row.get("path") or ""))
                compact = None
                if path in chunks_by_path:
                    compact = _compact_chunk(row, path)
                    chunks_by_path[path].append(compact)
                searchable = " ".join((path, str(row.get("symbol") or ""), str(row.get("text") or "")))
                for anchor in anchors:
                    exact_path = bool(anchor.path and path == anchor.path)
                    symbol_match = bool(not anchor.path and _term_hits(searchable, anchor.terms))
                    if exact_path or symbol_match:
                        if compact is None:
                            compact = _compact_chunk(row, path)
                        # Cap retained bind rows, but never stop the scan.
                        if len(bound_rows[anchor.entity]) < 512:
                            bound_rows[anchor.entity].append(compact)
                        else:
                            bind_truncated[anchor.entity] = True

        identifiers = {
            anchor.entity: _anchor_identifiers(anchor, bound_rows[anchor.entity])
            for anchor in anchors
        }
        relation_rows: dict[str, list[dict[str, Any]]] = {anchor.entity: [] for anchor in anchors}
        relation_truncated = {anchor.entity: False for anchor in anchors}
        pass2_rows = 0
        pass2_bytes = 0
        pass2_started = time.perf_counter()
        with chunks_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                pass2_rows += 1
                pass2_bytes += len(line.encode("utf-8"))
                row = json.loads(line)
                path = _normal_path(str(row.get("path") or ""))
                searchable = " ".join((path, str(row.get("symbol") or ""), str(row.get("text") or "")))
                compact = None
                for anchor in anchors:
                    terms = identifiers[anchor.entity]
                    if not terms:
                        continue
                    if task.task_type == "code2test" and not _is_test_path(path):
                        continue
                    if task.task_type == "edit2ripple" and anchor.path and path == anchor.path:
                        continue
                    if task.task_type == "trace2code" and _is_test_path(path):
                        continue
                    hits = _term_hits(searchable, terms)
                    if not hits:
                        continue
                    if len(relation_rows[anchor.entity]) >= 4096:
                        relation_truncated[anchor.entity] = True
                        continue
                    if compact is None:
                        compact = _compact_chunk(row, path)
                    relation_rows[anchor.entity].append({**compact, "match_terms": list(hits)})

        pass2_finished = time.perf_counter()
        observed = {path for path, rows in chunks_by_path.items() if rows}
        hybrid_union = set(hybrid_paths)
        outside_counts = {}
        relation_path_counts = {}
        canonical_needed_paths = set(hybrid_paths)
        for anchor in anchors:
            relation_paths = {str(row.get("path") or "") for row in relation_rows[anchor.entity]}
            relation_path_counts[anchor.entity] = len(relation_paths)
            outside_counts[anchor.entity] = len(relation_paths - hybrid_union)
            canonical_needed_paths.update(relation_paths)

        # Official canonical BCY renders kind=file corpus text, not arbitrary
        # symbol chunks.  A third fully charged pass retrieves exactly those
        # file rows needed by hybrid and typed outputs.
        canonical_file_texts: dict[str, str] = {}
        pass3_rows = 0
        pass3_bytes = 0
        pass3_started = time.perf_counter()
        with chunks_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                pass3_rows += 1
                pass3_bytes += len(line.encode("utf-8"))
                row = json.loads(line)
                if row.get("kind") != "file":
                    continue
                path = _normal_path(str(row.get("path") or ""))
                if path in canonical_needed_paths:
                    canonical_file_texts[path] = str(row.get("text") or "")
        pass3_finished = time.perf_counter()
        audit = {
            "chunks_path_sha256": hashlib.sha256(str(chunks_path).encode("utf-8")).hexdigest(),
            "pass_1": {
                "purpose": "bind anchors and retain hybrid paths",
                "rows_scanned": pass1_rows,
                "bytes_read": pass1_bytes,
                "wall_seconds": pass2_started - pass1_started,
            },
            "pass_2": {
                "purpose": "build corpus-wide exact-identifier relation postings",
                "rows_scanned": pass2_rows,
                "bytes_read": pass2_bytes,
                "wall_seconds": pass2_finished - pass2_started,
            },
            "pass_3": {
                "purpose": "load official canonical kind=file text for every possible output path",
                "rows_scanned": pass3_rows,
                "bytes_read": pass3_bytes,
                "wall_seconds": pass3_finished - pass3_started,
            },
            "rows_scanned": pass1_rows + pass2_rows + pass3_rows,
            "bytes_read": pass1_bytes + pass2_bytes + pass3_bytes,
            "wall_seconds": pass3_finished - pass1_started,
            "full_scan_complete": True,
            "selected_path_count": len(selected_paths),
            "observed_selected_path_count": len(observed),
            "all_selected_paths_observed": observed == selected_paths,
            "missing_selected_paths": sorted(selected_paths - observed),
            "query_anchor_catalog_truncated": False,
            "identifiers_by_entity": {key: list(value) for key, value in identifiers.items()},
            "bound_chunk_count_by_entity": {key: len(value) for key, value in bound_rows.items()},
            "bind_postings_truncated_by_entity": bind_truncated,
            "relation_chunk_count_by_entity": {key: len(value) for key, value in relation_rows.items()},
            "relation_path_count_by_entity": relation_path_counts,
            "relation_paths_outside_hybrid_union_by_entity": outside_counts,
            "relation_postings_truncated_by_entity": relation_truncated,
            "canonical_file_text_count": len(canonical_file_texts),
            "canonical_missing_paths": sorted(canonical_needed_paths - set(canonical_file_texts)),
            "index_backend": "two_pass_corpus_wide_exact_identifier_postings_plus_canonical_text_pass",
            "semantic_limit": "whole-token identifier occurrence only from the frozen reduced anchor-symbol catalog; no call/import/test/dependency/causal proof",
        }
        return cls(
            task,
            ranked,
            chunks_by_path,
            anchors,
            bound_rows,
            relation_rows,
            identifiers,
            canonical_file_texts,
            audit,
        )

    def _fused_paths(self) -> tuple[str, ...]:
        scores: dict[str, float] = {}
        for method in ("lexical", "bm25", "repomap"):
            for rank, path in enumerate(self.ranked_paths.get(method, ()), start=1):
                scores[path] = scores.get(path, 0.0) + 1.0 / (60.0 + rank)
        return tuple(path for path, _score in sorted(scores.items(), key=lambda item: (-item[1], item[0])))

    def _refs_for_paths(self, paths: Sequence[str], terms: Sequence[str]) -> tuple[ChunkRef, ...]:
        """One legacy-diagnostic representative per canonical ranked file."""

        refs: list[ChunkRef] = []
        for path in _dedupe_paths(paths)[:20]:
            candidates: list[tuple[int, str, Mapping[str, Any], tuple[str, ...]]] = []
            for row in self._chunks_by_path.get(path, ()):
                searchable = " ".join((path, str(row.get("symbol") or ""), str(row.get("text") or "")))
                hits = _term_hits(searchable, terms)
                candidates.append((-len(hits), str(row.get("chunk_id") or ""), row, hits))
            if not candidates:
                continue
            candidates.sort(key=lambda item: item[:2])
            _neg_score, chunk_id, row, hits = candidates[0]
            refs.append(
                ChunkRef(
                    path=path,
                    chunk_id=chunk_id,
                    start_line=int(row.get("start_line") or 0),
                    end_line=int(row.get("end_line") or 0),
                    symbol=str(row.get("symbol") or ""),
                    char_count=len(str(row.get("text") or "")),
                    match_terms=hits,
                )
            )
        return tuple(refs)

    def _rank_rows_by_file(
        self,
        rows: Sequence[Mapping[str, Any]],
        terms: Sequence[str],
        *,
        top_k: int,
    ) -> tuple[tuple[str, ...], tuple[ChunkRef, ...], tuple[dict[str, Any], ...]]:
        grouped: dict[str, list[tuple[Mapping[str, Any], tuple[str, ...]]]] = {}
        for row in rows:
            path = str(row.get("path") or "")
            searchable = " ".join(
                (path, str(row.get("symbol") or ""), str(row.get("text") or ""))
            )
            hits = tuple(row.get("match_terms") or ()) or _term_hits(searchable, terms)
            if path:
                grouped.setdefault(path, []).append((row, hits))
        file_scores: list[tuple[int, int, str, tuple[str, ...], Mapping[str, Any]]] = []
        for path, path_rows in grouped.items():
            unique_hits = tuple(sorted({hit for _row, hits in path_rows for hit in hits}, key=str.lower))
            representative, representative_hits = min(
                path_rows,
                key=lambda item: (-len(item[1]), str(item[0].get("chunk_id") or "")),
            )
            file_scores.append((-len(unique_hits), -len(path_rows), path, representative_hits, representative))
        file_scores.sort(key=lambda item: item[:3])
        selected = file_scores[:top_k]
        files = tuple(item[2] for item in selected)
        refs = tuple(
            ChunkRef(
                path=path,
                chunk_id=str(row.get("chunk_id") or ""),
                start_line=int(row.get("start_line") or 0),
                end_line=int(row.get("end_line") or 0),
                symbol=str(row.get("symbol") or ""),
                char_count=len(str(row.get("text") or "")),
                match_terms=hits,
            )
            for _neg_unique, _neg_chunks, path, hits, row in selected
        )
        ranking = tuple(
            {
                "path": path,
                "unique_identifier_hits": -neg_unique,
                "matching_chunks": -neg_chunks,
            }
            for neg_unique, neg_chunks, path, _hits, _row in selected
        )
        return files, refs, ranking

    def apply(
        self,
        action: str,
        task: DeploymentTask,
        anchor: Anchor | None,
        incoming: EvidenceBundle,
    ) -> tuple[EvidenceBundle, dict[str, Any]]:
        fused = self._fused_paths()
        if action == "parallel_hybrid":
            paths = tuple(fused[:20])
            terms = _terms_from_text(task.query_text, limit=24)
            refs = self._refs_for_paths(paths, terms)
            return EvidenceBundle(incoming.origin_entity, paths, refs, terms, False), {
                "cost_units": 3.0,
                "ranker_probes": 3,
                "returned_files": len(paths),
                "ranking_rule": "preserve RRF fused[:20] unique file order",
            }
        if anchor is None:
            raise ValueError(f"action {action} requires an anchor")
        if action == "bind_anchor":
            rows = self._bound_rows.get(anchor.entity, ())
            terms = self._identifiers.get(anchor.entity, ())
            paths, refs, _ranking = self._rank_rows_by_file(rows, terms, top_k=8)
            return EvidenceBundle(anchor.entity, tuple(paths), refs, terms, bool(refs)), {
                "cost_units": 1.0,
                "corpus_wide_anchor_posting_queries": 1,
                "returned_files": len(paths),
            }
        if action == "follow_relation":
            origin_anchor = self._anchors.get(incoming.origin_entity, anchor)
            terms = self._identifiers.get(origin_anchor.entity, incoming.relation_terms)
            rows = self._relation_rows.get(origin_anchor.entity, ())
            files, refs, ranking = self._rank_rows_by_file(rows, terms, top_k=20)
            certificate = incoming.certificate_valid and incoming.origin_entity == anchor.entity and bool(refs)
            return EvidenceBundle(incoming.origin_entity, files, refs, terms, certificate), {
                "cost_units": 2.0 if task.task_type == "trace2code" else 1.0,
                "corpus_wide_identifier_posting_queries": 1,
                "lineage_checks": 1 if task.task_type == "trace2code" else 0,
                "returned_files": len(files),
                "returned_files_outside_hybrid_union": len(set(files) - set(fused)),
                "ranking_rule": "unique identifier hits desc, matching chunks desc, path asc; top20 unique",
                "file_ranking": list(ranking),
            }
        if action == "certify_lineage":
            valid_refs = tuple(ref for ref in incoming.chunks if ref.match_terms)
            files = tuple(dict.fromkeys(ref.path for ref in valid_refs))
            certificate = (
                incoming.certificate_valid
                and incoming.origin_entity == anchor.entity
                and bool(valid_refs)
            )
            return EvidenceBundle(incoming.origin_entity, files, valid_refs, incoming.relation_terms, certificate), {
                "cost_units": 1.0,
                "lineage_checks": 1,
                "returned_files": len(files),
            }
        raise ValueError(f"unknown action: {action}")


def _initial_runtime_bundles(spec: ProgramSpec) -> dict[str, EvidenceBundle]:
    query_fact = next(value for value in spec.initial_facts if value.kind == "Query")
    runtime = {
        query_fact.render(): EvidenceBundle(query_fact.terms[0], (), (), (), True),
    }
    anchor_by_entity = {anchor.entity: anchor for anchor in spec.anchors}
    for value in spec.initial_facts:
        if value.kind == "Query":
            continue
        anchor = anchor_by_entity[value.terms[0]]
        runtime[value.render()] = EvidenceBundle(anchor.entity, (), (), anchor.terms, True)
    return runtime


def execute_program(
    spec: ProgramSpec,
    operator_ids: Sequence[str],
    *,
    mode: str,
    store: Any,
) -> dict[str, Any]:
    validation = validate_program(spec, operator_ids, mode)
    if not validation.get("valid"):
        reason = str(validation.get("reason") or "INVALID_PROGRAM")
        return {
            "status": "REJECTED",
            "decision": "ABSTAIN",
            "rejection_reason": reason,
            "wrong_entity_rejected": reason == "WRONG_ENTITY_BINDING",
            "program": list(operator_ids),
            "mode": mode,
            "operator_calls": 0,
            "validation": validation,
        }

    runtime = _initial_runtime_bundles(spec)
    anchors = {anchor.entity: anchor for anchor in spec.anchors}
    action_ledger: list[dict[str, Any]] = []
    entity_preserved = True
    for identifier in operator_ids:
        binding = spec.bindings[identifier]
        operator = binding.operator
        exact_input = operator.inputs[0].render()
        incoming = runtime.get(exact_input)
        consumed_fact = exact_input
        if incoming is None:
            required_kind = operator.inputs[0].kind
            same_kind = sorted(key for key in runtime if TypeFact.parse(key).kind == required_kind)
            if not same_kind:
                raise AssertionError("validated program lost its runtime prerequisite")
            consumed_fact = same_kind[0]
            incoming = runtime[consumed_fact]
        anchor = anchors.get(binding.anchor_entity or "")
        bundle, ledger = store.apply(binding.action, spec.task, anchor, incoming)
        expected_entity = binding.anchor_entity
        preserved = expected_entity is None or bundle.origin_entity == expected_entity
        entity_preserved = entity_preserved and preserved
        output_fact = operator.outputs[0].render()
        runtime[output_fact] = bundle
        action_ledger.append(
            {
                "operator": identifier,
                "action": binding.action,
                "consumed_fact": consumed_fact,
                "declared_input": exact_input,
                "declared_output": output_fact,
                "origin_entity": bundle.origin_entity,
                "expected_entity": expected_entity,
                "entity_preserved": preserved,
                **ledger,
            }
        )

    satisfied_goal_keys = [
        key for key in validation.get("satisfied_exact_goals") or [] if key in runtime
    ]
    final_goal_key = satisfied_goal_keys[0] if satisfied_goal_keys else None
    final_bundle = runtime.get(final_goal_key) if final_goal_key else None
    # A coarse-only hybrid closes on the nominal evidence kind under the query
    # entity, so it has no anchor-specific exact goal.  Prefer the last
    # declared evidence output rather than an arbitrary lexicographic entity.
    if final_bundle is None and action_ledger:
        last_output = str(action_ledger[-1].get("declared_output") or "")
        if last_output in runtime and TypeFact.parse(last_output).kind == spec.evidence_kind:
            final_goal_key = last_output
            final_bundle = runtime[last_output]
    if final_bundle is None:
        same_kind = sorted(
            key for key in runtime if TypeFact.parse(key).kind == spec.evidence_kind
        )
        if same_kind:
            final_goal_key = same_kind[0]
            final_bundle = runtime[final_goal_key]
        else:
            final_bundle = EvidenceBundle("", (), (), (), False)
    total_cost = sum(float(row.get("cost_units") or 0.0) for row in action_ledger)
    has_files = bool(final_bundle.files)
    runtime_certified = bool(
        final_bundle.certificate_valid
        and entity_preserved
        and validation.get("transition_exact_valid")
    )
    has_evidence = has_files and (mode == "coarse" or runtime_certified)
    if has_evidence:
        status = "EXECUTED"
    elif has_files:
        status = "UNCERTIFIED_EVIDENCE"
    else:
        status = "NO_EVIDENCE"
    return {
        "status": status,
        "decision": "PROGRAM" if has_evidence else "ABSTAIN",
        "program": list(operator_ids),
        "mode": mode,
        "depth": len(operator_ids),
        "cost_units": total_cost,
        "operator_calls": len(action_ledger),
        "obligation_semantics": spec.obligation_semantics,
        "satisfied_goal": final_goal_key,
        "files": list(final_bundle.files),
        "chunks": [
            {
                "path": ref.path,
                "chunk_id": ref.chunk_id,
                "start_line": ref.start_line,
                "end_line": ref.end_line,
                "symbol": ref.symbol,
                "char_count": ref.char_count,
                "match_terms": list(ref.match_terms),
            }
            for ref in final_bundle.chunks
        ],
        "certificate": {
            "static_exact_valid": bool(validation.get("transition_exact_valid")),
            "exact_goals_present": bool(validation.get("exact_goals_present")),
            "runtime_entity_preserved": entity_preserved,
            "exact_identifier_occurrence_provenance_valid": final_bundle.certificate_valid,
            "runtime_certified_for_refined_return": runtime_certified,
            "not_semantic_evidence": True,
            "scope": "entity identity plus whole-token identifier occurrence provenance from the frozen anchor-symbol catalog; no call/import/test/causal semantics",
        },
        "action_ledger": action_ledger,
    }


def canonical_count_tokens(text: str) -> int:
    """Strict equivalent of ARB bcy_curve.count_tokens at the pinned revision."""

    return len(CANONICAL_TOKEN_RE.findall(text)) if text else 0


def _dedupe_paths(paths: Iterable[str]) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for value in paths:
        path = _normal_path(value)
        if path and path not in seen:
            output.append(path)
            seen.add(path)
    return output


def canonical_pack_files(
    ranked_files: Sequence[str],
    gold_files: Sequence[str],
    file_texts: Mapping[str, str],
    *,
    budget: int = 8_000,
    coverage_thresholds: Sequence[int] = CANONICAL_COVERAGE_THRESHOLDS,
) -> dict[str, Any]:
    """Strictly equivalent core of pinned ARB ``bcy_curve.pack_files``."""

    if budget <= 0:
        raise ValueError("canonical token budget must be positive")
    thresholds = tuple(sorted({int(value) for value in coverage_thresholds if int(value) > 0}))
    if 1 not in thresholds:
        thresholds = (1, *thresholds)
    # Match the pinned official packer exactly at this boundary: path strings
    # affect header token counts and therefore must not be lstrip/normalized.
    ranked: list[str] = []
    seen_ranked: set[str] = set()
    for value in ranked_files:
        path = str(value)
        if path and path not in seen_ranked:
            ranked.append(path)
            seen_ranked.add(path)
    gold = {str(path) for path in gold_files}
    normalized_texts = {str(path): str(text) for path, text in file_texts.items()}
    used = 0
    covered = {threshold: set() for threshold in thresholds}
    packed_files = 0
    partial_files = 0
    missing_ranked_files = 0
    for path in ranked:
        text = normalized_texts.get(path)
        if text is None:
            missing_ranked_files += 1
            continue
        header_tokens = canonical_count_tokens(f"### {path}\n")
        content_tokens = canonical_count_tokens(text)
        separator_tokens = 1 if text else 0
        total_tokens = header_tokens + content_tokens + separator_tokens
        if total_tokens <= 0:
            continue
        remaining = budget - used
        if remaining <= 0:
            break
        packed_files += 1
        if total_tokens <= remaining:
            used += total_tokens
            included_content_tokens = content_tokens
        else:
            partial_files += 1
            included_after_header = max(0, remaining - header_tokens)
            included_content_tokens = min(content_tokens, included_after_header)
            used = budget
        if path in gold and content_tokens > 0:
            for threshold in thresholds:
                if included_content_tokens >= min(threshold, content_tokens):
                    covered[threshold].add(path)
        if used >= budget:
            break
    return {
        "budget_tokens": budget,
        "used_tokens": used,
        "bcy": len(covered[1]) / len(gold) if gold else 0.0,
        "bcy_by_min_content_tokens": {
            str(threshold): len(covered[threshold]) / len(gold) if gold else 0.0
            for threshold in thresholds
        },
        "covered_gold_count_by_min_content_tokens": {
            str(threshold): len(covered[threshold]) for threshold in thresholds
        },
        "gold_count": len(gold),
        "packed_files": packed_files,
        "partial_files": partial_files,
        "missing_ranked_files": missing_ranked_files,
    }


def score_execution(
    execution: Mapping[str, Any],
    gold_files: Sequence[str],
    *,
    file_texts: Mapping[str, str],
    token_budget: int = 8_000,
    legacy_char_budget: int = 8_000,
) -> dict[str, Any]:
    """Post-hoc canonical token BCY; never call from construction or search."""

    gold = {_normal_path(path) for path in gold_files}
    files = _dedupe_paths(str(path) for path in execution.get("files") or [])
    canonical = canonical_pack_files(files, tuple(gold), file_texts, budget=token_budget)

    # Retained only to expose why the old metric is not interchangeable with
    # canonical token BCY.  It is never used for best-found selection.
    legacy_used_chars = 0
    legacy_covered: set[str] = set()
    for chunk in execution.get("chunks") or []:
        char_count = int(chunk.get("char_count") or 0)
        if legacy_used_chars + char_count > legacy_char_budget and legacy_used_chars > 0:
            break
        legacy_used_chars += char_count
        path = _normal_path(str(chunk.get("path") or ""))
        if path in gold:
            legacy_covered.add(path)
    canonical_key = f"canonical_bcy@{token_budget}_tokens"
    return {
        "oracle_only": True,
        "primary_metric": canonical_key,
        "tokenizer": CANONICAL_TOKENIZER,
        "canonical_renderer": "### {path}\\n{corpus kind=file text}\\n",
        "gold_file_count": len(gold),
        "file_recall": len(gold & set(files)) / len(gold) if gold else 0.0,
        canonical_key: canonical["bcy"],
        "canonical_bcy_by_min_content_tokens": canonical["bcy_by_min_content_tokens"],
        "canonical_used_tokens": canonical["used_tokens"],
        "canonical_packed_files": canonical["packed_files"],
        "canonical_partial_files": canonical["partial_files"],
        "canonical_missing_ranked_files": canonical["missing_ranked_files"],
        "legacy_diagnostic": {
            "metric": "legacy_gold_coverage@8000_chars",
            "not_canonical_bcy": True,
            "used_chars": legacy_used_chars,
            "value": len(legacy_covered) / len(gold) if gold else 0.0,
        },
    }


def load_gold_files_for_scoring(task: DeploymentTask, arb_data_root: Path) -> tuple[str, ...]:
    """Gold boundary: call only after every candidate program has executed."""

    release = TASK_RELEASE[task.task_type]
    path = arb_data_root / "pilot_eval" / release / "lexical_details.jsonl"
    row = _find_row(path, "sample_id", task.sample_id)
    values = row.get("gold_files") or []
    if not isinstance(values, list):
        raise ValueError("gold_files must be a list")
    return tuple(_normal_path(str(value)) for value in values if value)


def selective_utility(
    decision: str,
    evaluation_label: str,
    *,
    correct_return_reward: float = 1.0,
    false_return_penalty: float = 1.0,
    abstain_cost: float = 0.0,
) -> float:
    """Extension point for frozen natural/wrong-repository no-gold labels.

    ``evaluation_label`` is intentionally absent from every construction,
    search, and execution API.  It may be one of ``positive``,
    ``natural_no_gold``, or ``wrong_repository_no_gold`` and is consumed only
    after the decision is frozen.
    """

    if decision not in {"PROGRAM", "ABSTAIN", "UNSAT"}:
        raise ValueError("unknown decision")
    if evaluation_label not in {"positive", "natural_no_gold", "wrong_repository_no_gold"}:
        raise ValueError("unknown evaluation_label")
    if decision in {"ABSTAIN", "UNSAT"}:
        return -float(abstain_cost)
    return float(correct_return_reward) if evaluation_label == "positive" else -float(false_return_penalty)


def unsat_eligibility(
    search_report: Mapping[str, Any],
    capability_report: Mapping[str, Any],
    io_audit: Mapping[str, Any],
    *,
    executed_program_count: int,
) -> dict[str, Any]:
    """Conservative proof obligations for a scoped ``UNSAT`` decision."""

    bind_truncated = io_audit.get("bind_postings_truncated_by_entity") or {}
    relation_truncated = io_audit.get("relation_postings_truncated_by_entity") or {}
    checks = {
        "search_frontier_exhausted": bool(search_report.get("frontier_exhausted")),
        "program_storage_complete": not bool(search_report.get("program_storage_truncated")),
        "all_stored_programs_executed": executed_program_count
        == int(search_report.get("stored_semantically_valid_program_count") or 0),
        "full_corpus_scan_complete": bool(capability_report.get("corpus_full_scan_complete")),
        "selected_paths_complete": bool(capability_report.get("corpus_complete_for_selected_paths")),
        "query_anchor_catalog_not_truncated": not bool(io_audit.get("query_anchor_catalog_truncated")),
        "bind_postings_not_truncated": not any(bool(value) for value in bind_truncated.values()),
        "relation_postings_not_truncated": not any(bool(value) for value in relation_truncated.values()),
        "canonical_file_texts_complete": not bool(io_audit.get("canonical_missing_paths")),
    }
    blockers = [name for name, passed in checks.items() if not passed]
    return {
        "eligible": not blockers,
        "checks": checks,
        "blockers": blockers,
        "scope": "only the frozen query-only anchors, reduced anchor-symbol catalog (failure label/legal path stem/bound ARB symbol fields), operator grammar, depth/cost budget, and cached snapshot; not full-file identifier closure or semantic impossibility",
    }


def _load_deployment_record(arb_data_root: Path, task_type: str, sample_id: str) -> DeploymentTask:
    release = TASK_RELEASE[task_type]
    sample_path = arb_data_root / "benchmark" / release / "samples.jsonl"
    row = _find_row(sample_path, "id", sample_id)
    return deployment_task_from_record(row)


def load_positive_selection(manifest_path: Path, arb_data_root: Path) -> list[DeploymentTask]:
    """Load and verify the frozen positive-task manifest in canonical order."""

    raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    rows = raw.get("samples") if isinstance(raw, dict) else None
    if not isinstance(rows, list):
        raise ValueError("selection manifest must contain a samples list")
    expected_count = int(raw.get("sample_count") or len(rows))
    if expected_count != len(rows):
        raise ValueError("selection manifest sample_count mismatch")
    ordered = sorted(rows, key=lambda row: (int(row.get("pilot_index") or 0), str(row.get("sample_id") or "")))
    tasks: list[DeploymentTask] = []
    seen: set[str] = set()
    for row in ordered:
        task_type = str(row.get("task_type") or "")
        sample_id = str(row.get("sample_id") or "")
        if task_type not in TASK_RELEASE or not sample_id:
            raise ValueError(f"invalid positive selection row: {row!r}")
        if sample_id in seen:
            raise ValueError(f"duplicate sample_id in selection manifest: {sample_id}")
        task = _load_deployment_record(arb_data_root, task_type, sample_id)
        for field in ("repo", "base_commit"):
            selected = str(row.get(field) or "")
            if selected and getattr(task, field) != selected:
                raise ValueError(f"selection {field} mismatch for {sample_id}")
        tasks.append(task)
        seen.add(sample_id)
    return tasks


def run_cached_sample(
    task: DeploymentTask,
    arb_data_root: Path,
    *,
    budget: float = 3.0,
    max_expansions: int = 512,
) -> dict[str, Any]:
    compiled = compile_program_spec(task)
    base = {
        "sample_id": task.sample_id,
        "task_type": task.task_type,
        "query_only_audit": dict(compiled.audit),
        "capabilities": {
            "cloud_model_calls": 0,
            "tree_sitter_required": False,
            "ast_parser_required": False,
        },
    }
    if compiled.spec is None:
        return {**base, "decision": compiled.decision, "reason": compiled.reason}
    spec = compiled.spec
    searches = {
        mode: search_programs(
            spec,
            mode=mode,
            budget=budget,
            max_depth=3,
            max_expansions=max_expansions,
        )
        for mode in ("coarse", "refinement")
    }
    # Search is complete before any cached detail row (which also carries
    # evaluation-only fields on disk) is parsed.  The store then retains only
    # DETAIL_EXECUTION_FIELD_WHITELIST.
    store = CachedEvidenceStore.from_cached_arb(task, arb_data_root)
    executions: dict[str, list[dict[str, Any]]] = {"coarse": [], "refinement": []}
    for mode, report in searches.items():
        for program in report["programs"]:
            if mode == "refinement" and not program["refinement_obligations_satisfied"]:
                continue
            executions[mode].append(execute_program(spec, program["operators"], mode=mode, store=store))

    # Freeze the deployment decision and selected candidate before any
    # gold-bearing field is requested.  Multiple anchor branches are not
    # fused: a deterministic nominal cost/depth/program key selects one.
    eligible_refined = [row for row in executions["refinement"] if row.get("status") == "EXECUTED"]
    selected_refined = min(
        eligible_refined,
        key=lambda row: (
            float(row.get("cost_units") or 0.0),
            int(row.get("depth") or 0),
            tuple(row.get("program") or []),
        ),
        default=None,
    )
    unsat_audit = unsat_eligibility(
        searches["refinement"],
        store.capability_report,
        store.io_audit,
        executed_program_count=len(executions["refinement"]),
    )
    if selected_refined is not None:
        decision, reason = "PROGRAM", None
    elif unsat_audit["eligible"]:
        decision, reason = "UNSAT", "EXHAUSTED_TYPED_FRONTIER_OVER_FROZEN_ANCHOR_SYMBOL_CATALOG"
    else:
        decision, reason = "ABSTAIN", "NO_CERTIFIED_CANDIDATE_UNDER_FINITE_BUDGET"
    deployment_selection = None
    if selected_refined is not None:
        deployment_selection = {
            "program": list(selected_refined.get("program") or []),
            "files": list(selected_refined.get("files") or []),
            "certificate": dict(selected_refined.get("certificate") or {}),
            "nominal_cost_units": float(selected_refined.get("cost_units") or 0.0),
            "operator_depth": int(selected_refined.get("depth") or 0),
            "selection_key": [
                float(selected_refined.get("cost_units") or 0.0),
                int(selected_refined.get("depth") or 0),
                list(selected_refined.get("program") or []),
            ],
        }
    deployment_output = {
        "frozen_before_gold_access": True,
        "decision": decision,
        "reason": reason,
        "selection_policy": "minimum (nominal cost_units, operator depth, canonical program tuple) among certified refined candidates; no gold",
        "eligible_candidate_count": len(eligible_refined),
        "deployment_selection": deployment_selection,
    }
    execution_accounting = {
        mode: {
            "attempted_candidate_count": len(rows),
            "certified_executed_candidate_count": sum(row.get("status") == "EXECUTED" for row in rows),
            "uncertified_candidate_count": sum(row.get("status") == "UNCERTIFIED_EVIDENCE" for row in rows),
            "no_evidence_candidate_count": sum(row.get("status") == "NO_EVIDENCE" for row in rows),
            "aggregate_nominal_cost_units": sum(float(row.get("cost_units") or 0.0) for row in rows),
            "aggregate_operator_calls": sum(int(row.get("operator_calls") or 0) for row in rows),
        }
        for mode, rows in executions.items()
    }

    # This is the first point at which a gold-bearing field is requested.
    gold_files = load_gold_files_for_scoring(task, arb_data_root)
    for rows in executions.values():
        for execution in rows:
            execution["posthoc_score"] = score_execution(
                execution,
                gold_files,
                file_texts=store.canonical_file_texts,
            )

    native_baselines: dict[str, dict[str, Any]] = {}
    for method in ("lexical", "bm25", "repomap"):
        files = list(store.ranked_paths.get(method, ())[:20])
        native_baselines[method] = {
            "files": files,
            "score": score_execution(
                {"files": files, "chunks": []},
                gold_files,
                file_texts=store.canonical_file_texts,
            ),
        }
    rrf_files = list(store._fused_paths()[:20])
    native_baselines["rrf_equal_cost_hybrid"] = {
        "files": rrf_files,
        "score": score_execution(
            {"files": rrf_files, "chunks": []},
            gold_files,
            file_texts=store.canonical_file_texts,
        ),
    }
    best_single_method = max(
        ("lexical", "bm25", "repomap"),
        key=lambda method: (
            float(native_baselines[method]["score"]["canonical_bcy@8000_tokens"]),
            method,
        ),
    )
    baseline_block = {
        "protocol": "same regex_code_tokenizer_v1, canonical kind=file renderer, greedy 8000-token packer",
        "methods": native_baselines,
        "best_single_method_posthoc_oracle": {
            "oracle_only": True,
            "not_used_for_generation_search_or_deployment": True,
            "method": best_single_method,
            "score": native_baselines[best_single_method]["score"],
        },
    }

    best_found: dict[str, Any] = {}
    for mode, rows in executions.items():
        executed = [row for row in rows if row.get("status") == "EXECUTED"]
        best = max(
            executed,
            key=lambda row: (
                float((row.get("posthoc_score") or {}).get("canonical_bcy@8000_tokens") or 0.0),
                float((row.get("posthoc_score") or {}).get("file_recall") or 0.0),
                -float(row.get("cost_units") or 0.0),
                tuple(row.get("program") or []),
            ),
            default=None,
        )
        best_found[mode] = {
            "oracle_only": True,
            "completed_candidates_only": True,
            "not_used_for_deployment_selection_or_decision": True,
            "program": best.get("program") if best else None,
            "score": best.get("posthoc_score") if best else None,
        }
    deployment_selection_posthoc_oracle = None
    if selected_refined is not None:
        deployment_selection_posthoc_oracle = {
            "oracle_only": True,
            "selection_was_frozen_without_gold": True,
            "program": list(selected_refined.get("program") or []),
            "score": selected_refined.get("posthoc_score"),
        }
    return {
        **base,
        "decision": decision,
        "reason": reason,
        "anchors": [
            {
                "entity": anchor.entity,
                "source_kind": anchor.source_kind,
                "label": anchor.label,
                "path": anchor.path,
                "terms": list(anchor.terms),
            }
            for anchor in spec.anchors
        ],
        "obligations": [value.render() for value in spec.obligations],
        "obligation_semantics": spec.obligation_semantics,
        "candidate_anchor_count": len(spec.candidate_entities),
        "chain_depth": spec.chain_depth,
        "operator_depth": spec.chain_depth,
        "retrieval_transition_depth": spec.retrieval_transition_depth,
        "certificate_step_counts_as_retrieval_transition": False,
        "equal_cost_hybrid": {"depth": 1, "cost_units": spec.hybrid_cost},
        "searches": searches,
        "executions": executions,
        "deployment_query_only_output": deployment_output,
        "deployment_selection_posthoc_oracle": deployment_selection_posthoc_oracle,
        "execution_accounting": execution_accounting,
        "cost_accounting_guard": "nominal operator cost_units are grammar-comparison charges only; actual corpus rows/bytes/wall time are separately charged in index_io_audit",
        "canonical_baselines": baseline_block,
        "best_found_posthoc_oracle": best_found,
        "unsat_eligibility": unsat_audit,
        "store_capabilities": store.capability_report,
        "index_io_audit": store.io_audit,
        "semantic_claim_guard": {
            "not_semantic_evidence": True,
            "scope": "whole-token identifier occurrence provenance from failure labels, legal path stems, and bound ARB symbol fields only",
            "forbidden_interpretations": ["call graph", "import graph", "test relation", "dependency relation", "root cause", "causal evidence"],
        },
        "claim_guard": "best-found finite-search scores and wrong-entity rejection only; no claim that a refined exhaustive oracle exceeds coarse",
        "depth_necessity_guard": {
            "grammar_candidate_depth": spec.chain_depth,
            "retrieval_transition_depth": spec.retrieval_transition_depth,
            "strict_depth_necessary": None,
            "status": "NOT_ESTABLISHED_BY_GRAMMAR_OR_TYPE_CLOSURE",
            "required_test": "post-hoc canonical output difference versus depth<=1 and equal-cost hybrid on the same task; batch denominator remains all 60 positives",
        },
    }


def run_cached_selection(
    manifest_path: Path,
    arb_data_root: Path,
    output_jsonl: Path,
    *,
    budget: float = 3.0,
    max_expansions: int = 512,
    limit: int | None = None,
) -> dict[str, Any]:
    """Run a frozen positive selection and stream one auditable JSON row/task.

    This is a positive-only batch path.  A frozen 20-task selective manifest
    exists, but the label-withholding selective adapter is not implemented in
    this function; passing that manifest therefore fails schema validation
    instead of silently mixing abstention labels into construction/search.
    """

    tasks = load_positive_selection(manifest_path, arb_data_root)
    if limit is not None:
        if limit < 1:
            raise ValueError("limit must be positive")
        tasks = tasks[:limit]
    output_jsonl.parent.mkdir(parents=True, exist_ok=True)
    decisions: dict[str, int] = {}
    started = time.perf_counter()
    with output_jsonl.open("w", encoding="utf-8") as handle:
        for index, task in enumerate(tasks, start=1):
            report = run_cached_sample(
                task,
                arb_data_root,
                budget=budget,
                max_expansions=max_expansions,
            )
            report["batch_index"] = index
            report["batch_total"] = len(tasks)
            handle.write(json.dumps(report, ensure_ascii=False, sort_keys=True))
            handle.write("\n")
            decision = str(report.get("decision") or "UNKNOWN")
            decisions[decision] = decisions.get(decision, 0) + 1
    return {
        "status": "COMPLETED_RAW_POSITIVE_DISCOVERY_RUN",
        "mechanism_gate_evaluated": False,
        "batch_scope": "positive_only; selective_adapter_not_yet_implemented",
        "selection_manifest": str(manifest_path),
        "selection_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "output_jsonl": str(output_jsonl),
        "sample_count": len(tasks),
        "decisions": dict(sorted(decisions.items())),
        "wall_seconds": time.perf_counter() - started,
        "max_expansions_per_mode": max_expansions,
        "claim_guard": "raw positive-task reports only; strict depth necessity, adversarial rates, confidence intervals, and MECHANISM-PROCEED remain unevaluated",
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arb-data-root", type=Path, required=True)
    parser.add_argument("--task-type", choices=tuple(TASK_RELEASE))
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--sample-id")
    target.add_argument("--selection-manifest", type=Path)
    parser.add_argument("--budget", type=float, default=3.0)
    parser.add_argument("--max-expansions", type=int, default=512)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.selection_manifest:
        if args.task_type:
            raise SystemExit("--task-type is only valid with --sample-id")
        if args.output is None:
            raise SystemExit("batch mode requires --output JSONL")
        summary = run_cached_selection(
            args.selection_manifest,
            args.arb_data_root,
            args.output,
            budget=args.budget,
            max_expansions=args.max_expansions,
            limit=args.limit,
        )
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
        return
    if not args.task_type:
        raise SystemExit("single-sample mode requires --task-type")
    task = _load_deployment_record(args.arb_data_root, args.task_type, args.sample_id)
    report = run_cached_sample(
        task,
        args.arb_data_root,
        budget=args.budget,
        max_expansions=args.max_expansions,
    )
    rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
