from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from summarize_arb_typed_discovery import (
    CANONICAL_THRESHOLDS,
    CANONICAL_TOKENIZER,
    DiscoveryValidationError,
    PRIMARY_BCY,
    _normalize_sample,
    _scope_summary,
    _validate_manifest,
    _validated_score,
)


def canonical_score(bcy: float, recall: float) -> dict:
    return {
        "oracle_only": True,
        "primary_metric": PRIMARY_BCY,
        "tokenizer": CANONICAL_TOKENIZER,
        "gold_file_count": 1,
        "file_recall": recall,
        PRIMARY_BCY: bcy,
        "canonical_bcy_by_min_content_tokens": {
            threshold: bcy for threshold in CANONICAL_THRESHOLDS
        },
        "canonical_missing_ranked_files": 0,
    }


def execution(program: list[str], files: list[str], bcy: float, recall: float) -> dict:
    actions = ["bind_anchor", "follow_relation", "certify_lineage"]
    return {
        "status": "EXECUTED",
        "decision": "PROGRAM",
        "program": program,
        "files": files,
        "depth": 3,
        "cost_units": 3.0,
        "operator_calls": 3,
        "certificate": {"runtime_certified_for_refined_return": True},
        "action_ledger": [{"action": action} for action in actions],
        "posthoc_score": canonical_score(bcy, recall),
    }


def manifest_row() -> dict:
    return {
        "pilot_index": 1,
        "sample_id": "sample-001",
        "task_type": "code2test",
        "release_id": "v2_code2test",
        "repo": "example/repo",
        "base_commit": "abc123",
    }


def official_row(recall: float = 0.0) -> dict:
    return {
        "pilot_index": 1,
        "sample_id": "sample-001",
        "repo": "example/repo",
        "base_commit": "abc123",
        "unbounded_top20_union_diagnostic": {
            "method_gold_fraction@20": {
                "lexical": recall,
                "bm25": recall,
                "repomap": recall,
            }
        },
    }


def normal_batch(*, selected_hits_gold: bool = False, second_bcy: float = 1.0) -> dict:
    selected_files = ["outside_gold.py", "outside_noise.py"] if selected_hits_gold else ["outside_noise.py"]
    selected_bcy = 1.0 if selected_hits_gold else 0.0
    selected_recall = selected_bcy
    first = execution(["10_a", "20_a", "30_a"], selected_files, selected_bcy, selected_recall)
    second = execution(["10_b", "20_b", "30_b"], ["outside_gold.py"] if second_bcy else ["other.py"], second_bcy, second_bcy)
    coarse = execution(["00_hybrid", "20_c", "30_c"], ["outside_gold.py"], 1.0, 1.0)
    refined_best = second if second_bcy > selected_bcy or second_bcy == selected_bcy else first
    methods = {
        method: {"files": ["base.py"], "score": canonical_score(0.0, 0.0)}
        for method in ("lexical", "bm25", "repomap", "rrf_equal_cost_hybrid")
    }
    return {
        "sample_id": "sample-001",
        "task_type": "code2test",
        "batch_index": 1,
        "batch_total": 60,
        "query_only_audit": {
            "forbidden_sources_not_available": [
                "gold",
                "reference_patch",
                "evaluation_metrics",
            ]
        },
        "decision": "PROGRAM",
        "reason": None,
        "deployment_query_only_output": {
            "frozen_before_gold_access": True,
            "decision": "PROGRAM",
            "reason": None,
            "eligible_candidate_count": 2,
            "deployment_selection": {
                "program": first["program"],
                "files": first["files"],
                "certificate": first["certificate"],
                "nominal_cost_units": 3.0,
                "operator_depth": 3,
            },
        },
        "deployment_selection_posthoc_oracle": {
            "oracle_only": True,
            "selection_was_frozen_without_gold": True,
            "program": first["program"],
            "score": first["posthoc_score"],
        },
        "executions": {"refinement": [first, second], "coarse": [coarse]},
        "canonical_baselines": {
            "protocol": "same regex_code_tokenizer_v1, canonical kind=file renderer, greedy 8000-token packer",
            "methods": methods,
        },
        "best_found_posthoc_oracle": {
            "refinement": {
                "oracle_only": True,
                "not_used_for_deployment_selection_or_decision": True,
                "program": refined_best["program"],
                "score": refined_best["posthoc_score"],
            },
            "coarse": {
                "oracle_only": True,
                "not_used_for_deployment_selection_or_decision": True,
                "program": coarse["program"],
                "score": coarse["posthoc_score"],
            },
        },
        "searches": {
            mode: {
                "frontier_exhausted": True,
                "program_storage_truncated": False,
                "expansions": 5,
                "wrong_entity_rejections": 2,
            }
            for mode in ("coarse", "refinement")
        },
        "store_capabilities": {
            "gold_fields_copied_to_executor": [],
            "semantic_relation_backend": "whole_token_identifier_occurrence_provenance",
            "call_graph_semantics": False,
            "import_graph_semantics": False,
        },
        "semantic_claim_guard": {"not_semantic_evidence": True},
        "index_io_audit": {
            "pass_1": {"rows_scanned": 1, "bytes_read": 10, "wall_seconds": 0.1},
            "pass_2": {"rows_scanned": 1, "bytes_read": 10, "wall_seconds": 0.1},
            "pass_3": {"rows_scanned": 1, "bytes_read": 10, "wall_seconds": 0.1},
            "rows_scanned": 3,
            "bytes_read": 30,
            "wall_seconds": 0.3,
            "identifiers_by_entity": {"e": ["WidgetStore"]},
            "bind_postings_truncated_by_entity": {"e": False},
            "relation_postings_truncated_by_entity": {"e": False},
            "relation_paths_outside_hybrid_union_by_entity": {"e": 2},
            "full_scan_complete": True,
            "all_selected_paths_observed": True,
            "query_anchor_catalog_truncated": False,
            "canonical_missing_paths": [],
        },
        "execution_accounting": {
            "refinement": {
                "attempted_candidate_count": 2,
                "certified_executed_candidate_count": 2,
                "uncertified_candidate_count": 0,
                "no_evidence_candidate_count": 0,
                "aggregate_nominal_cost_units": 6.0,
                "aggregate_operator_calls": 6,
            }
        },
        "chain_depth": 3,
        "operator_depth": 3,
        "retrieval_transition_depth": 2,
        "certificate_step_counts_as_retrieval_transition": False,
        "depth_necessity_guard": {"strict_depth_necessary": None},
    }


class TypedDiscoverySummaryTests(unittest.TestCase):
    def test_query_only_selection_does_not_follow_posthoc_oracle_score(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            low_oracle = _normalize_sample(
                normal_batch(second_bcy=0.0),
                manifest_row(),
                official_row(),
                ["outside_gold.py"],
                root,
            )
            high_oracle = _normalize_sample(
                normal_batch(second_bcy=1.0),
                manifest_row(),
                official_row(),
                ["outside_gold.py"],
                root,
            )
        self.assertEqual(low_oracle["query_only"], {"bcy": 0.0, "recall": 0.0})
        self.assertEqual(high_oracle["query_only"], low_oracle["query_only"])
        self.assertEqual(low_oracle["oracle_ceiling"]["bcy"], 0.0)
        self.assertEqual(high_oracle["oracle_ceiling"]["bcy"], 1.0)

    def test_terminal_abstain_recovers_all_baselines_and_stays_in_denominator(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            release = "v2_code2test"
            eval_dir = root / "pilot_eval" / release
            corpus_dir = root / "pilot_corpus" / release
            eval_dir.mkdir(parents=True)
            corpus_dir.mkdir(parents=True)
            selected = manifest_row()
            for method, files in {
                "lexical": ["gold.py"],
                "bm25": ["noise.py"],
                "repomap": ["gold.py"],
            }.items():
                detail = {
                    "sample_id": selected["sample_id"],
                    "task_type": selected["task_type"],
                    "repo": selected["repo"],
                    "base_commit": selected["base_commit"],
                    "top_files": files,
                    "gold_files": ["gold.py"],
                }
                (eval_dir / f"{method}_details.jsonl").write_text(json.dumps(detail) + "\n", encoding="utf-8")
            chunks = root / "chunks.jsonl"
            chunks.write_text(
                "".join(
                    json.dumps({"kind": "file", "path": path, "text": text}) + "\n"
                    for path, text in (("gold.py", "target = True\n"), ("noise.py", "noise = True\n"))
                ),
                encoding="utf-8",
            )
            (corpus_dir / "corpus_manifest.jsonl").write_text(
                json.dumps({"repo": selected["repo"], "base_commit": selected["base_commit"], "chunks_path": str(chunks)}) + "\n",
                encoding="utf-8",
            )
            terminal = {
                "sample_id": selected["sample_id"],
                "task_type": selected["task_type"],
                "batch_index": 1,
                "batch_total": 60,
                "decision": "ABSTAIN",
                "reason": "NO_VALID_QUERY_ANCHOR",
                "query_only_audit": {
                    "forbidden_sources_not_available": ["gold", "reference_patch", "evaluation_metrics"]
                },
            }
            recovered_official = official_row(recall=1.0)
            recovered_official["unbounded_top20_union_diagnostic"]["method_gold_fraction@20"]["bm25"] = 0.0
            normalized = _normalize_sample(
                terminal,
                selected,
                recovered_official,
                ["gold.py"],
                root,
            )
        self.assertEqual(normalized["baseline_source"], "posthoc_recovery")
        self.assertEqual(normalized["query_only"]["bcy"], 0.0)
        self.assertEqual(normalized["baselines"]["lexical"]["bcy"], 1.0)
        self.assertEqual(normalized["baselines"]["bm25"]["bcy"], 0.0)
        self.assertEqual(normalized["baselines"]["repomap"]["bcy"], 1.0)
        self.assertEqual(normalized["baselines"]["rrf_equal_cost_hybrid"]["bcy"], 1.0)

        rows = [copy.deepcopy(normalized) for _ in range(60)]
        for row in rows[1:]:
            row["decision"] = "PROGRAM"
            row["query_only"] = {"bcy": 1.0, "recall": 1.0}
        summary = _scope_summary(rows)
        self.assertEqual(summary["n"], 60)
        self.assertEqual(summary["decisions"]["ABSTAIN"]["count"], 1)
        self.assertAlmostEqual(
            summary["effectiveness"]["query_only_primary"]["mean_canonical_bcy@8000_tokens"],
            59 / 60,
        )

    def test_legacy_diagnostic_never_replaces_canonical_bcy(self) -> None:
        score = canonical_score(0.0, 0.0)
        score["legacy_diagnostic"] = {
            "metric": "legacy_gold_coverage@8000_chars",
            "not_canonical_bcy": True,
            "value": 1.0,
        }
        self.assertEqual(_validated_score(score, "legacy trap")["bcy"], 0.0)

    def test_outside_union_gold_and_depth_are_counted_without_certificate_hop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            normalized = _normalize_sample(
                normal_batch(selected_hits_gold=True, second_bcy=0.0),
                manifest_row(),
                official_row(),
                ["outside_gold.py"],
                Path(tmp),
            )
        self.assertEqual(normalized["outside_union"]["returned_file_count"], 2)
        self.assertEqual(normalized["outside_union"]["gold_file_count"], 1)
        self.assertEqual(normalized["depth"]["selected_operator_depth"], 3)
        self.assertEqual(normalized["depth"]["selected_retrieval_transition_depth"], 2)

    def test_manifest_or_baseline_inconsistency_hard_fails(self) -> None:
        samples = []
        for index in range(1, 61):
            task_type = "code2test" if index <= 20 else "edit2ripple" if index <= 40 else "trace2code"
            release = {
                "code2test": "v2_code2test",
                "edit2ripple": "v2_edit2ripple",
                "trace2code": "v2_trace2code",
            }[task_type]
            samples.append(
                {
                    "pilot_index": index,
                    "sample_id": f"sample-{index:03d}",
                    "task_type": task_type,
                    "release_id": release,
                    "repo": "example/repo",
                    "base_commit": f"commit-{index}",
                }
            )
        raw = {
            "sample_count": 60,
            "counts_by_task_type": {"code2test": 20, "edit2ripple": 20, "trace2code": 20},
            "samples": samples[:-1],
        }
        with self.assertRaises(DiscoveryValidationError):
            _validate_manifest(raw, "0" * 64)

        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(DiscoveryValidationError):
                _normalize_sample(
                    normal_batch(second_bcy=0.0),
                    manifest_row(),
                    official_row(recall=1.0),
                    ["outside_gold.py"],
                    Path(tmp),
                )

    def test_io_or_depth_guard_drift_hard_fails(self) -> None:
        broken_io = normal_batch(second_bcy=0.0)
        broken_io["index_io_audit"]["bytes_read"] = 31
        broken_depth = normal_batch(second_bcy=0.0)
        broken_depth["certificate_step_counts_as_retrieval_transition"] = True
        with tempfile.TemporaryDirectory() as tmp:
            for row in (broken_io, broken_depth):
                with self.subTest(kind="io" if row is broken_io else "depth"):
                    with self.assertRaises(DiscoveryValidationError):
                        _normalize_sample(
                            row,
                            manifest_row(),
                            official_row(),
                            ["outside_gold.py"],
                            Path(tmp),
                        )


if __name__ == "__main__":
    unittest.main()
