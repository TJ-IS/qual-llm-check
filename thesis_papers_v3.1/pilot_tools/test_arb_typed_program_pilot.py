from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from arb_typed_program_pilot import (
    Anchor,
    CachedEvidenceStore,
    SyntheticEvidenceStore,
    _anchor_identifiers,
    _normal_path,
    canonical_pack_files,
    _safe_detail_projection,
    compile_program_spec,
    deployment_task_from_record,
    execute_program,
    run_cached_sample,
    score_execution,
    search_programs,
    selective_utility,
    unsat_eligibility,
    validate_program,
)


class GuardedMapping(dict):
    def __init__(self, *args, forbidden: set[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.forbidden = forbidden or set()

    def get(self, key, default=None):
        if key in self.forbidden:
            raise AssertionError(f"forbidden key accessed: {key}")
        return super().get(key, default)


def code2test_record() -> GuardedMapping:
    query = {
        "pr_title": "Add Widget cache invalidation regression coverage",
        "pr_body": "WidgetStore now invalidates cached widgets after an update.",
        "implementation_files": ["src/widget_store.py", "src/widget_cache.py"],
        "implementation_file_count": 2,
        "changed_file_summary": "two implementation files changed",
    }
    return GuardedMapping(
        {
            "id": "sample-code2test",
            "task_type": "code2test",
            "repo": "example/repo",
            "base_commit": "abc123",
            "query": query,
            "gold": {"related_tests": ["tests/test_widget_store.py"]},
            "metadata": {"reference_patch": "must-not-read"},
        },
        forbidden={"gold", "metadata", "gold_spans", "gold_blocks", "patch"},
    )


def compiled_code2test():
    task = deployment_task_from_record(code2test_record())
    compiled = compile_program_spec(task)
    assert compiled.spec is not None
    return compiled.spec


def operator_for(spec, action: str, entity: str | None = None) -> str:
    rows = [
        identifier
        for identifier, binding in spec.bindings.items()
        if binding.action == action and (entity is None or binding.anchor_entity == entity)
    ]
    if len(rows) != 1:
        raise AssertionError((action, entity, rows))
    return rows[0]


def typed_chain(spec, entity: str) -> list[str]:
    return [
        operator_for(spec, "bind_anchor", entity),
        operator_for(spec, "follow_relation", entity),
        operator_for(spec, "certify_lineage", entity),
    ]


class QueryOnlyConstructionTests(unittest.TestCase):
    def test_constructor_never_requests_gold_or_metadata(self) -> None:
        task = deployment_task_from_record(code2test_record())
        compiled = compile_program_spec(task)
        self.assertEqual(compiled.decision, "PROGRAM")
        self.assertEqual(
            set(compiled.audit["source_fields"]),
            {
                "query.pr_title",
                "query.pr_body",
                "query.implementation_files",
                "query.implementation_file_count",
                "query.changed_file_summary",
            },
        )
        self.assertIn("gold", compiled.audit["forbidden_sources_not_available"])

    def test_edit2ripple_does_not_read_anchor_diff_or_patch(self) -> None:
        query = GuardedMapping(
            {
                "intent": "Keep configuration aliases synchronized",
                "anchor_file": "src/config.py",
                "anchor_diff": "gold-like diff that must not be read",
            },
            forbidden={"anchor_diff", "patch", "reference_patch"},
        )
        record = GuardedMapping(
            {
                "id": "edit-sample",
                "task_type": "edit2ripple",
                "repo": "example/repo",
                "base_commit": "abc123",
                "query": query,
                "gold": {"files": ["tests/test_config.py"]},
            },
            forbidden={"gold", "patch"},
        )
        compiled = compile_program_spec(deployment_task_from_record(record))
        self.assertEqual(compiled.decision, "PROGRAM")
        self.assertFalse(compiled.audit["edit2ripple_anchor_diff_used"])
        self.assertNotIn("query.anchor_diff", compiled.audit["source_fields"])

    def test_empty_visible_query_abstains_without_inventing_obligations(self) -> None:
        task = deployment_task_from_record(
            {
                "id": "empty",
                "task_type": "trace2code",
                "repo": "example/repo",
                "base_commit": "abc123",
                "query": {"command": "go test ./..."},
            }
        )
        compiled = compile_program_spec(task)
        self.assertEqual(compiled.decision, "ABSTAIN")
        self.assertEqual(compiled.reason, "NO_QUERY_ANCHOR")
        self.assertIsNone(compiled.spec)

    def test_code2test_changed_file_schema_is_a_query_only_anchor(self) -> None:
        task = deployment_task_from_record(
            {
                "id": "changed-file-only",
                "task_type": "code2test",
                "repo": "example/repo",
                "base_commit": "abc123",
                "query": {
                    "pr_title": "Fix formatting",
                    "changed_file": "src/output/help_template.rs",
                },
            }
        )
        compiled = compile_program_spec(task)
        self.assertIsNotNone(compiled.spec)
        assert compiled.spec is not None
        self.assertEqual(compiled.spec.anchors[0].path, "src/output/help_template.rs")
        self.assertIn("query.changed_file", compiled.audit["source_fields"])

    def test_all_eight_visible_files_remain_candidate_branches_under_512_expansions(self) -> None:
        files = [f"src/module_{index}.py" for index in range(8)]
        task = deployment_task_from_record(
            {
                "id": "eight-files",
                "task_type": "code2test",
                "repo": "example/repo",
                "base_commit": "abc123",
                "query": {"implementation_files": files},
            }
        )
        compiled = compile_program_spec(task)
        self.assertIsNotNone(compiled.spec)
        assert compiled.spec is not None
        self.assertEqual(len(compiled.spec.anchors), 8)
        self.assertFalse(compiled.audit["anchor_catalog_truncated"])
        search = search_programs(compiled.spec, mode="refinement")
        self.assertTrue(search["frontier_exhausted"])
        self.assertLessEqual(search["expansions"], 512)
        self.assertEqual(search["semantically_valid_program_count"], 8)

    def test_execution_detail_projection_drops_gold_fields(self) -> None:
        detail = GuardedMapping(
            {
                "sample_id": "s",
                "task_type": "code2test",
                "repo": "r",
                "base_commit": "c",
                "top_files": ["a.py"],
                "gold_files": ["secret.py"],
                "metrics": {"gold_coverage@8k": 1.0},
            },
            forbidden={"gold_files", "metrics", "gold_spans", "gold_blocks"},
        )
        projected = _safe_detail_projection(detail)
        self.assertEqual(projected["top_files"], ["a.py"])
        self.assertNotIn("gold_files", projected)
        self.assertNotIn("metrics", projected)


class RefinementAndPrerequisiteTests(unittest.TestCase):
    def test_same_type_wrong_entity_chain_is_preexecution_rejected(self) -> None:
        spec = compiled_code2test()
        primary, secondary = spec.anchors[:2]
        wrong_chain = [
            operator_for(spec, "bind_anchor", secondary.entity),
            operator_for(spec, "follow_relation", primary.entity),
            operator_for(spec, "certify_lineage", primary.entity),
        ]
        refined_validation = validate_program(spec, wrong_chain, "refinement")
        self.assertFalse(refined_validation["valid"])
        self.assertEqual(refined_validation["reason"], "WRONG_ENTITY_BINDING")

        store = SyntheticEvidenceStore(
            bound_files={secondary.entity: [secondary.path or "secondary.py"]},
            relation_files={secondary.entity: ["tests/test_wrong_entity.py"]},
        )
        rejected = execute_program(spec, wrong_chain, mode="refinement", store=store)
        self.assertEqual(rejected["status"], "REJECTED")
        self.assertTrue(rejected["wrong_entity_rejected"])
        self.assertEqual(rejected["operator_calls"], 0)

        coarse = execute_program(spec, wrong_chain, mode="coarse", store=store)
        self.assertEqual(coarse["status"], "EXECUTED")
        self.assertFalse(coarse["certificate"]["runtime_entity_preserved"])
        self.assertFalse(coarse["certificate"]["exact_identifier_occurrence_provenance_valid"])

    def test_broken_prerequisite_is_rejected_in_both_modes(self) -> None:
        spec = compiled_code2test()
        primary = spec.anchors[0]
        missing_prefix = [operator_for(spec, "certify_lineage", primary.entity)]
        for mode in ("coarse", "refinement"):
            report = validate_program(spec, missing_prefix, mode)
            self.assertFalse(report["valid"])
            self.assertEqual(report["reason"], "BROKEN_PREREQUISITE")

    def test_runtime_bind_without_evidence_cannot_return_uncertified_typed_files(self) -> None:
        spec = compiled_code2test()
        anchor = spec.anchors[0]
        store = SyntheticEvidenceStore(
            bound_files={anchor.entity: []},
            relation_files={anchor.entity: ["tests/spurious.py"]},
        )
        result = execute_program(
            spec,
            typed_chain(spec, anchor.entity),
            mode="refinement",
            store=store,
        )
        self.assertEqual(result["status"], "UNCERTIFIED_EVIDENCE")
        self.assertEqual(result["decision"], "ABSTAIN")
        self.assertFalse(result["certificate"]["runtime_certified_for_refined_return"])

    def test_search_counts_wrong_entity_rejection_as_expansion(self) -> None:
        spec = compiled_code2test()
        refinement = search_programs(spec, mode="refinement", max_expansions=5000)
        coarse = search_programs(spec, mode="coarse", max_expansions=5000)
        self.assertGreater(refinement["wrong_entity_rejections"], 0)
        self.assertGreater(refinement["expansions"], refinement["wrong_entity_rejections"])
        self.assertEqual(refinement["semantically_valid_program_count"], len(spec.anchors))
        self.assertGreaterEqual(coarse["semantically_valid_program_count"], len(spec.anchors))
        invalid_coarse = [
            row for row in coarse["programs"] if not row["refinement_obligations_satisfied"]
        ]
        self.assertTrue(invalid_coarse)
        self.assertFalse(coarse["coarse_exhaustive_oracle_can_be_below_refinement"])

    def test_every_query_anchor_has_an_existential_exact_branch(self) -> None:
        spec = compiled_code2test()
        self.assertEqual(spec.obligation_semantics, "existential_identity_preserving_branch")
        self.assertEqual(len(spec.obligations), len(spec.anchors))
        expected_goals = {goal.render() for goal in spec.obligations}
        observed_goals: set[str] = set()
        for anchor in spec.anchors:
            validation = validate_program(spec, typed_chain(spec, anchor.entity), "refinement")
            self.assertTrue(validation["valid"], (anchor, validation))
            self.assertEqual(
                validation["satisfied_exact_goals"],
                [f"{spec.evidence_kind}<{anchor.entity}>"],
            )
            observed_goals.update(validation["satisfied_exact_goals"])
        self.assertEqual(observed_goals, expected_goals)

        first, second = spec.anchors[:2]
        cross_bound = [
            operator_for(spec, "bind_anchor", first.entity),
            operator_for(spec, "follow_relation", second.entity),
            operator_for(spec, "certify_lineage", second.entity),
        ]
        rejected = validate_program(spec, cross_bound, "refinement")
        self.assertFalse(rejected["valid"])
        self.assertEqual(rejected["reason"], "WRONG_ENTITY_BINDING")

    def test_complete_raw_identifier_catalog_is_not_silently_capped_at_32(self) -> None:
        anchor = Anchor("e", "implementation_file", "src/many.py", "src/many.py", ())
        rows = [
            {"symbol": f"Symbol{index:02d}"}
            for index in range(40)
        ] + [{"symbol": "Needle"}]
        identifiers = _anchor_identifiers(anchor, rows)
        self.assertEqual(len(identifiers), 42)
        self.assertIn("Needle", identifiers)


class DepthBudgetAndDeterminismTests(unittest.TestCase):
    def test_depth_three_typed_chain_strictly_beats_equal_cost_hybrid_fixture(self) -> None:
        spec = compiled_code2test()
        primary = spec.anchors[0]
        store = SyntheticEvidenceStore(
            hybrid_files=["docs/widget.md"],
            bound_files={primary.entity: [primary.path or "src/widget_store.py"]},
            relation_files={primary.entity: ["tests/test_widget_store.py"]},
        )
        shallow = search_programs(spec, mode="refinement", max_depth=1, max_expansions=5000)
        deep = search_programs(spec, mode="refinement", max_depth=3, max_expansions=5000)
        self.assertEqual(shallow["semantically_valid_program_count"], 0)
        self.assertEqual(deep["semantically_valid_program_count"], len(spec.anchors))

        hybrid = execute_program(
            spec,
            [operator_for(spec, "parallel_hybrid")],
            mode="coarse",
            store=store,
        )
        typed = execute_program(spec, typed_chain(spec, primary.entity), mode="refinement", store=store)
        file_texts = {
            "docs/widget.md": "Widget documentation only.",
            "src/widget_store.py": "class WidgetStore: pass",
            "tests/test_widget_store.py": "def test_widget_store(): assert WidgetStore()",
        }
        hybrid_score = score_execution(
            hybrid,
            ["tests/test_widget_store.py"],
            file_texts=file_texts,
        )
        typed_score = score_execution(
            typed,
            ["tests/test_widget_store.py"],
            file_texts=file_texts,
        )
        self.assertEqual(hybrid["depth"], 1)
        self.assertEqual(typed["depth"], 3)
        self.assertEqual(hybrid["cost_units"], typed["cost_units"])
        self.assertEqual(hybrid_score["canonical_bcy@8000_tokens"], 0.0)
        self.assertEqual(typed_score["canonical_bcy@8000_tokens"], 1.0)

    def test_budget_and_search_are_deterministic(self) -> None:
        spec = compiled_code2test()
        kwargs = dict(mode="refinement", budget=3.0, max_depth=3, max_expansions=5000)
        first = search_programs(spec, **kwargs)
        second = search_programs(spec, **kwargs)
        self.assertEqual(first, second)
        under_budget = search_programs(
            spec,
            mode="refinement",
            budget=2.99,
            max_depth=3,
            max_expansions=5000,
        )
        self.assertEqual(under_budget["semantically_valid_program_count"], 0)

    def test_canonical_tie_break_is_independent_of_catalog_insertion_order(self) -> None:
        spec = compiled_code2test()
        reversed_catalog = replace(spec, operators=tuple(reversed(spec.operators)))
        kwargs = dict(mode="coarse", budget=3.0, max_depth=3, max_expansions=37)
        first = search_programs(spec, **kwargs)
        second = search_programs(reversed_catalog, **kwargs)
        self.assertEqual(first, second)
        self.assertIn("canonical operator-id tuple", first["tie_break_policy"])

    def test_trace_program_is_depth_two_and_equal_cost(self) -> None:
        task = deployment_task_from_record(
            {
                "id": "trace-sample",
                "task_type": "trace2code",
                "repo": "example/repo",
                "base_commit": "abc123",
                "query": {
                    "failure_excerpt": "context_test.go:252: c.GetInt8 undefined",
                    "command": "go test ./...",
                },
            }
        )
        compiled = compile_program_spec(task)
        self.assertIsNotNone(compiled.spec)
        spec = compiled.spec
        assert spec is not None
        primary = spec.anchors[0]
        chain = [
            operator_for(spec, "bind_anchor", primary.entity),
            operator_for(spec, "follow_relation", primary.entity),
        ]
        store = SyntheticEvidenceStore(
            bound_files={primary.entity: ["context.go"]},
            relation_files={primary.entity: ["context.go"]},
        )
        result = execute_program(spec, chain, mode="refinement", store=store)
        self.assertEqual(result["depth"], 2)
        self.assertEqual(result["cost_units"], 3.0)


class SelectiveExtensionTests(unittest.TestCase):
    def test_no_gold_label_enters_only_postdecision_utility(self) -> None:
        self.assertEqual(selective_utility("PROGRAM", "positive"), 1.0)
        self.assertEqual(selective_utility("PROGRAM", "natural_no_gold"), -1.0)
        self.assertEqual(selective_utility("PROGRAM", "wrong_repository_no_gold"), -1.0)
        self.assertEqual(selective_utility("ABSTAIN", "natural_no_gold"), 0.0)
        self.assertEqual(selective_utility("UNSAT", "wrong_repository_no_gold"), 0.0)

    def test_unsat_requires_every_search_and_index_completeness_check(self) -> None:
        search = {
            "frontier_exhausted": True,
            "program_storage_truncated": False,
            "stored_semantically_valid_program_count": 1,
        }
        capability = {
            "corpus_full_scan_complete": True,
            "corpus_complete_for_selected_paths": True,
        }
        io = {
            "query_anchor_catalog_truncated": False,
            "bind_postings_truncated_by_entity": {"e": False},
            "relation_postings_truncated_by_entity": {"e": False},
            "canonical_missing_paths": [],
        }
        self.assertTrue(
            unsat_eligibility(search, capability, io, executed_program_count=1)["eligible"]
        )
        mutations = [
            ({**search, "program_storage_truncated": True}, capability, io),
            (search, capability, {**io, "bind_postings_truncated_by_entity": {"e": True}}),
            (search, capability, {**io, "relation_postings_truncated_by_entity": {"e": True}}),
            (search, capability, {**io, "canonical_missing_paths": ["missing.py"]}),
            (search, capability, {**io, "query_anchor_catalog_truncated": True}),
        ]
        for changed_search, changed_capability, changed_io in mutations:
            report = unsat_eligibility(
                changed_search,
                changed_capability,
                changed_io,
                executed_program_count=1,
            )
            self.assertFalse(report["eligible"], report)


class CorpusWideAndCanonicalScoringTests(unittest.TestCase):
    def test_typed_follow_can_escape_all_three_cached_top_lists(self) -> None:
        task = deployment_task_from_record(code2test_record())
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            eval_dir = root / "pilot_eval" / "v2_code2test"
            corpus_dir = root / "pilot_corpus" / "v2_code2test"
            eval_dir.mkdir(parents=True)
            corpus_dir.mkdir(parents=True)
            top_files = ["src/widget_store.py", "docs/readme.md"]
            for method in ("lexical", "bm25", "repomap"):
                row = {
                    "sample_id": task.sample_id,
                    "task_type": task.task_type,
                    "repo": task.repo,
                    "base_commit": task.base_commit,
                    "ranker": method,
                    "top_files": top_files,
                    "gold_files": ["tests/test_widget_store.py"],
                    "metrics": {"must_not_reach_executor": 1},
                }
                (eval_dir / f"{method}_details.jsonl").write_text(
                    json.dumps(row) + "\n",
                    encoding="utf-8",
                )
            chunks_path = root / "snapshot.chunks.jsonl"
            chunks = [
                {
                    "path": "src/widget_store.py",
                    "kind": "file",
                    "symbol": "",
                    "text": "class WidgetStore:\n    pass\n",
                    "chunk_id": "source-file",
                    "start_line": 1,
                    "end_line": 2,
                },
                {
                    "path": "src/widget_store.py",
                    "kind": "symbol",
                    "symbol": "WidgetStore",
                    "text": "class WidgetStore:\n    pass\n",
                    "chunk_id": "source-symbol",
                    "start_line": 1,
                    "end_line": 2,
                },
                {
                    "path": "docs/readme.md",
                    "kind": "file",
                    "symbol": "",
                    "text": "unrelated documentation",
                    "chunk_id": "docs-file",
                    "start_line": 1,
                    "end_line": 1,
                },
                {
                    "path": "tests/test_widget_store.py",
                    "kind": "file",
                    "symbol": "",
                    "text": "def test_update():\n    assert WidgetStore()\n",
                    "chunk_id": "new-file",
                    "start_line": 1,
                    "end_line": 2,
                },
                {
                    "path": "tests/test_widget_store.py",
                    "kind": "symbol",
                    "symbol": "test_update",
                    "text": "assert WidgetStore()",
                    "chunk_id": "new-symbol",
                    "start_line": 1,
                    "end_line": 2,
                },
            ]
            for index in range(21):
                path = f"tests/z{index:02d}_test.py"
                chunks.extend(
                    [
                        {
                            "path": path,
                            "kind": "file",
                            "symbol": "",
                            "text": "def test_related():\n    assert WidgetStore()\n",
                            "chunk_id": f"z{index:02d}-file",
                            "start_line": 1,
                            "end_line": 2,
                        },
                        {
                            "path": path,
                            "kind": "symbol",
                            "symbol": "test_related",
                            "text": "assert WidgetStore()",
                            "chunk_id": f"z{index:02d}-symbol",
                            "start_line": 1,
                            "end_line": 2,
                        },
                    ]
                )
            chunks_path.write_text(
                "".join(json.dumps(row) + "\n" for row in chunks),
                encoding="utf-8",
            )
            manifest = {
                "repo": task.repo,
                "base_commit": task.base_commit,
                "status": "ok",
                "chunks_path": str(chunks_path),
            }
            (corpus_dir / "corpus_manifest.jsonl").write_text(
                json.dumps(manifest) + "\n",
                encoding="utf-8",
            )

            store = CachedEvidenceStore.from_cached_arb(task, root)
            compiled = compile_program_spec(task)
            assert compiled.spec is not None
            spec = compiled.spec
            primary = spec.anchors[0]
            typed = execute_program(
                spec,
                typed_chain(spec, primary.entity),
                mode="refinement",
                store=store,
            )
            hybrid = execute_program(
                spec,
                [operator_for(spec, "parallel_hybrid")],
                mode="coarse",
                store=store,
            )
            self.assertIn(
                "tests/test_widget_store.py",
                typed["files"],
                msg={"typed": typed, "io": store.io_audit},
            )
            self.assertNotIn("tests/test_widget_store.py", hybrid["files"])
            self.assertNotIn("tests/test_widget_store.py", top_files)
            self.assertEqual(len(typed["files"]), 20)
            self.assertEqual(len(set(typed["files"])), 20)
            self.assertIn("tests/z18_test.py", typed["files"])
            self.assertGreater(
                store.io_audit["relation_paths_outside_hybrid_union_by_entity"][primary.entity],
                0,
            )
            identifiers = store.io_audit["identifiers_by_entity"][primary.entity]
            self.assertIn("WidgetStore", identifiers)
            self.assertNotIn("Widget", identifiers)
            self.assertNotIn("Store", identifiers)
            self.assertFalse(store.capability_report["call_graph_semantics"])
            self.assertFalse(store.capability_report["tree_sitter_required"])

            report = run_cached_sample(task, root)
            deployment = report["deployment_query_only_output"]
            self.assertTrue(deployment["frozen_before_gold_access"])
            selected = deployment["deployment_selection"]
            self.assertIsNotNone(selected)
            assert selected is not None
            eligible = [
                row
                for row in report["executions"]["refinement"]
                if row["status"] == "EXECUTED"
            ]
            expected = min(
                eligible,
                key=lambda row: (row["cost_units"], row["depth"], tuple(row["program"])),
            )
            self.assertEqual(selected["program"], expected["program"])
            self.assertNotIn("posthoc_score", selected)
            accounting = report["execution_accounting"]["refinement"]
            self.assertEqual(accounting["attempted_candidate_count"], len(report["executions"]["refinement"]))
            self.assertEqual(
                accounting["aggregate_nominal_cost_units"],
                sum(row.get("cost_units", 0.0) for row in report["executions"]["refinement"]),
            )
            self.assertIn("index_io_audit", report)

    def test_canonical_token_bcy_is_not_legacy_8k_char_coverage(self) -> None:
        execution = {
            "files": ["noise.py", "gold.py"],
            # Deliberately arrange the legacy chunk diagnostic differently from
            # canonical file-rank packing to make conflation detectable.
            "chunks": [{"path": "gold.py", "char_count": 100}],
        }
        score = score_execution(
            execution,
            ["gold.py"],
            file_texts={
                "noise.py": "x " * 9_000,
                "gold.py": "target = True\n",
            },
        )
        self.assertEqual(score["primary_metric"], "canonical_bcy@8000_tokens")
        self.assertEqual(score["canonical_bcy@8000_tokens"], 0.0)
        self.assertEqual(score["legacy_diagnostic"]["value"], 1.0)
        self.assertTrue(score["legacy_diagnostic"]["not_canonical_bcy"])
        self.assertEqual(
            set(score["canonical_bcy_by_min_content_tokens"]),
            {"1", "16", "32", "64", "128"},
        )

    def test_canonical_packer_preserves_leading_dot_header_token_cost(self) -> None:
        self.assertEqual(_normal_path(".gold.py"), ".gold.py")
        packed = canonical_pack_files(
            ["noise.py", ".gold.py"],
            [".gold.py"],
            {
                "noise.py": " ".join(["x"] * 7_986),
                ".gold.py": "z",
            },
        )
        # Official regex packer: noise consumes 7,993 tokens, leaving exactly
        # the seven-token `.gold.py` header and no gold content token.
        self.assertEqual(packed["used_tokens"], 8_000)
        self.assertEqual(packed["bcy"], 0.0)


if __name__ == "__main__":
    unittest.main()
