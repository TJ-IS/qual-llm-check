from __future__ import annotations

import unittest

from handoff_tier_oracle import analyze as analyze_handoff
from recipe_family_oracle import Run, analyze as analyze_recipes
from typed_program_oracle import Operator, TypeFact, enumerate_programs


RECIPE_SEEDS = {"0", "1", "2"}


def recipe_grid(
    packs: dict[str, tuple[set[str], float]],
    *,
    patchers: tuple[str, ...] = ("p1",),
    seeds: tuple[str, ...] = ("0", "1", "2"),
) -> list[Run]:
    rows: list[Run] = []
    for pack_id, (chunks, success) in packs.items():
        for patcher in patchers:
            for seed in seeds:
                rows.append(
                    Run(
                        "t1",
                        pack_id,
                        frozenset(chunks),
                        patcher,
                        seed,
                        success,
                        float(len(chunks)),
                    )
                )
    return rows


def analyze_recipe_rows(
    rows: list[Run],
    *,
    patchers: set[str] | None = None,
    seeds: set[str] | None = None,
    min_runs: int = 3,
) -> dict:
    return analyze_recipes(
        rows,
        min_runs=min_runs,
        success_threshold=2 / 3,
        max_jaccard=0.60,
        required_patchers=patchers or {"p1"},
        required_seeds=seeds or RECIPE_SEEDS,
    )


class RecipeFamilyTests(unittest.TestCase):
    def test_discovers_alternative_inclusion_minimal_recipes_and_intersection(self) -> None:
        rows = recipe_grid(
            {
                "empty": (set(), 0.0),
                "a": ({"A"}, 0.0),
                "b": ({"B"}, 0.0),
                "c": ({"C"}, 0.0),
                "ab": ({"A", "B"}, 0.0),
                "ac": ({"A", "C"}, 1.0),
                "bc": ({"B", "C"}, 1.0),
                "abc": ({"A", "B", "C"}, 1.0),
            }
        )
        task = analyze_recipe_rows(rows)["tasks"][0]
        self.assertEqual(task["inclusion_minimal_family_count"], 2)
        self.assertEqual(task["inclusion_minimal_family"], [["A", "C"], ["B", "C"]])
        self.assertEqual(task["observed_family_intersection"], ["C"])
        self.assertNotIn("common_core", task)
        self.assertTrue(task["multi_recipe_trigger"])

    def test_missing_proper_subsets_do_not_create_fake_minimum(self) -> None:
        rows = recipe_grid({"ac": ({"A", "C"}, 1.0)})
        task = analyze_recipe_rows(rows)["tasks"][0]
        self.assertEqual(task["inclusion_minimal_family_count"], 0)
        self.assertEqual(task["one_deletion_local_family_count"], 0)
        evidence = task["minimality_evidence"][0]
        self.assertEqual(len(evidence["proper_subsets_by_status"]["missing"]), 3)

    def test_underpowered_deletion_is_not_confirmed_insufficient(self) -> None:
        rows = recipe_grid(
            {
                "empty": (set(), 0.0),
                "b": ({"B"}, 0.0),
                "ab": ({"A", "B"}, 1.0),
            }
        )
        rows.append(Run("t1", "a", frozenset({"A"}), "p1", "0", 0.0, 1.0))
        task = analyze_recipe_rows(rows)["tasks"][0]
        evidence = next(item for item in task["pack_evidence"] if item["chunks"] == ["A"])
        self.assertEqual(evidence["evidence_status"], "underpowered")
        self.assertEqual(task["inclusion_minimal_family_count"], 0)
        self.assertEqual(task["one_deletion_local_family_count"], 0)

    def test_duplicate_task_set_patcher_seed_is_rejected(self) -> None:
        row = Run("t1", "a", frozenset({"A"}), "p1", "0", 1.0, 1.0)
        with self.assertRaisesRegex(ValueError, "duplicate run key"):
            analyze_recipe_rows([row, row], seeds={"0"}, min_runs=1)

    def test_missing_required_patcher_is_reported_missing(self) -> None:
        rows = recipe_grid({"empty": (set(), 0.0), "a": ({"A"}, 1.0)})
        task = analyze_recipe_rows(rows, patchers={"p1", "p2"})["tasks"][0]
        a_evidence = next(item for item in task["pack_evidence"] if item["chunks"] == ["A"])
        self.assertEqual(a_evidence["evidence_status"], "missing")
        self.assertEqual(task["inclusion_minimal_family_count"], 0)

    def test_nonmonotone_one_deletion_minimum_is_not_inclusion_minimum(self) -> None:
        rows = recipe_grid(
            {
                "empty": (set(), 0.0),
                "a": ({"A"}, 1.0),
                "b": ({"B"}, 0.0),
                "c": ({"C"}, 0.0),
                "ab": ({"A", "B"}, 0.0),
                "ac": ({"A", "C"}, 0.0),
                "bc": ({"B", "C"}, 0.0),
                "abc": ({"A", "B", "C"}, 1.0),
            }
        )
        task = analyze_recipe_rows(rows)["tasks"][0]
        self.assertIn(["A", "B", "C"], task["one_deletion_local_family"])
        self.assertNotIn(["A", "B", "C"], task["inclusion_minimal_family"])
        self.assertEqual(task["inclusion_minimal_family"], [["A"]])
        self.assertFalse(task["multi_recipe_trigger"])


class TypedProgramTests(unittest.TestCase):
    def test_refinement_rejects_wrong_entity_chain_that_coarse_accepts(self) -> None:
        fact = TypeFact.parse
        operators = [
            Operator("01_trace_to_bar", (fact("FailureFrame<t1>"),), (fact("Def<bar>"),), 1.0),
            Operator("02_bar_callers", (fact("Def<bar>"),), (fact("CallerSet<bar>"),), 1.0),
            Operator("03_bar_tests", (fact("CallerSet<bar>"),), (fact("TestCovering<bar>"),), 1.0),
            Operator("11_trace_to_foo", (fact("FailureFrame<t1>"),), (fact("Def<foo>"),), 1.0),
            Operator("12_foo_callers", (fact("Def<foo>"),), (fact("CallerSet<foo>"),), 1.0),
            Operator("13_foo_tests", (fact("CallerSet<foo>"),), (fact("TestCovering<foo>"),), 1.0),
        ]
        kwargs = dict(
            task_id="t1",
            initial_facts=[fact("FailureFrame<t1>")],
            obligations=[fact("Def<foo>"), fact("CallerSet<foo>"), fact("TestCovering<foo>")],
            operators=operators,
            max_depth=3,
            budget=3.0,
            max_programs=100,
            max_expansions=500,
        )
        refinement = enumerate_programs(mode="refinement", **kwargs)
        coarse = enumerate_programs(mode="coarse", **kwargs)
        self.assertEqual(refinement["semantically_valid_program_count"], 1)
        self.assertEqual(
            refinement["semantically_valid_programs"][0]["operators"],
            ["11_trace_to_foo", "12_foo_callers", "13_foo_tests"],
        )
        wrong = next(
            program
            for program in coarse["programs"]
            if program["operators"]
            == ["01_trace_to_bar", "02_bar_callers", "03_bar_tests"]
        )
        self.assertFalse(wrong["refinement_obligations_satisfied"])
        self.assertGreaterEqual(coarse["semantically_valid_program_count"], 1)

    def test_exact_goal_from_wrong_input_is_not_semantically_valid(self) -> None:
        fact = TypeFact.parse
        report = enumerate_programs(
            task_id="t1",
            initial_facts=[fact("Seed<bar>")],
            obligations=[fact("Goal<foo>")],
            operators=[Operator("wrong_binding", (fact("Seed<foo>"),), (fact("Goal<foo>"),), 1.0)],
            mode="coarse",
            max_depth=1,
            budget=1.0,
            max_programs=10,
            max_expansions=10,
        )
        program = report["programs"][0]
        self.assertTrue(program["exact_goals_present"])
        self.assertFalse(program["transition_exact_valid"])
        self.assertFalse(program["refinement_obligations_satisfied"])
        self.assertEqual(report["semantically_valid_program_count"], 0)

    def test_coarse_continues_after_nominal_closure_and_covers_refined_program(self) -> None:
        fact = TypeFact.parse
        operators = [
            Operator("foo", (), (fact("Def<foo>"),), 1.0),
            Operator("bar", (), (fact("Def<bar>"),), 1.0),
        ]
        kwargs = dict(
            task_id="t1",
            initial_facts=[],
            obligations=[fact("Def<foo>"), fact("Def<bar>")],
            operators=operators,
            max_depth=2,
            budget=2.0,
            max_programs=20,
            max_expansions=100,
        )
        refinement = enumerate_programs(mode="refinement", **kwargs)
        coarse = enumerate_programs(mode="coarse", **kwargs)
        refined_sets = {frozenset(program["operators"]) for program in refinement["semantically_valid_programs"]}
        coarse_valid_sets = {frozenset(program["operators"]) for program in coarse["semantically_valid_programs"]}
        self.assertTrue(refined_sets.issubset(coarse_valid_sets))
        self.assertIn(frozenset({"foo", "bar"}), coarse_valid_sets)

    def test_equal_cost_order_equivalent_state_is_enqueued_once(self) -> None:
        fact = TypeFact.parse
        report = enumerate_programs(
            task_id="t1",
            initial_facts=[fact("Start")],
            obligations=[fact("X"), fact("Y")],
            operators=[
                Operator("x", (fact("Start"),), (fact("X"),), 1.0),
                Operator("y", (fact("Start"),), (fact("Y"),), 1.0),
            ],
            mode="refinement",
            max_depth=2,
            budget=2.0,
            max_programs=20,
            max_expansions=100,
        )
        self.assertEqual(report["program_count"], 1)
        self.assertEqual(report["semantically_valid_program_count"], 1)
        self.assertEqual(set(report["programs"][0]["operators"]), {"x", "y"})
        self.assertIn("cost-prioritized", report["search_policy"])


HANDOFF_STATES = {("t1", "c1")}
HANDOFF_SEEDS = {"1", "2"}


def handoff_grid(
    outcomes: dict[tuple[str, str], tuple[object, float, float]],
    *,
    task_id: str = "t1",
    checkpoint_id: str = "c1",
    seeds: tuple[str, ...] = ("1", "2"),
) -> list[dict]:
    rows: list[dict] = []
    for (information, tier), (success_spec, repair_cost, acquisition_cost) in outcomes.items():
        for seed in seeds:
            success = success_spec[seed] if isinstance(success_spec, dict) else success_spec
            rows.append(
                {
                    "task_id": task_id,
                    "checkpoint_id": checkpoint_id,
                    "information": information,
                    "tier": tier,
                    "seed": seed,
                    "success": success,
                    "repair_cost": repair_cost,
                    "acquisition_cost": acquisition_cost,
                }
            )
    return rows


def analyze_handoff_rows(
    rows: list[dict],
    *,
    lambda_cost: float = 0.05,
    expected_states: set[tuple[str, str]] | None = None,
    expected_seeds: set[str] | None = None,
    min_runs: int = 2,
    strict_pairs: bool = True,
) -> dict:
    return analyze_handoff(
        rows,
        tiers=["cheap", "strong"],
        lambda_cost=lambda_cost,
        success_value=1.0,
        min_runs=min_runs,
        strict_pairs=strict_pairs,
        expected_states=expected_states or HANDOFF_STATES,
        expected_seeds=expected_seeds or HANDOFF_SEEDS,
    )


class HandoffTierTests(unittest.TestCase):
    def positive_rows(self) -> list[dict]:
        return handoff_grid(
            {
                ("current", "cheap"): (0.0, 1.0, 0.0),
                ("current", "strong"): (1.0, 8.0, 0.0),
                ("scout", "cheap"): (1.0, 1.0, 1.0),
                ("scout", "strong"): (1.0, 8.0, 1.0),
            }
        )

    def test_detects_positive_voi_tier_switch(self) -> None:
        report = analyze_handoff_rows(self.positive_rows())
        state = report["states"][0]
        self.assertEqual(state["current_best_tier"], "strong")
        self.assertEqual(state["scout_best_tier_before_acquisition"], "cheap")
        self.assertTrue(state["positive_voi_tier_switch"])
        self.assertEqual(state["recommended_action"], "CONTINUE_SCOUT")
        self.assertAlmostEqual(state["voi"], 0.30)

    def test_abstain_prevents_false_positive_when_all_repairs_are_negative(self) -> None:
        rows = handoff_grid(
            {
                ("current", "cheap"): (0.0, 10.0, 0.0),
                ("current", "strong"): (0.0, 20.0, 0.0),
                ("scout", "cheap"): (0.0, 8.0, 1.0),
                ("scout", "strong"): (0.0, 20.0, 1.0),
            }
        )
        state = analyze_handoff_rows(rows, lambda_cost=1.0)["states"][0]
        self.assertEqual(state["current_best_tier"], "abstain")
        self.assertEqual(state["scout_best_tier_before_acquisition"], "abstain")
        self.assertEqual(state["voi"], -1.0)
        self.assertEqual(state["recommended_action"], "ABSTAIN")

    def test_duplicate_cell_seed_is_rejected(self) -> None:
        rows = self.positive_rows()
        rows.append(dict(rows[0]))
        with self.assertRaisesRegex(ValueError, "duplicate run key"):
            analyze_handoff_rows(rows)

    def test_strict_expected_pairing_excludes_incomplete_state(self) -> None:
        rows = self.positive_rows()
        rows = [
            row
            for row in rows
            if not (
                row["information"] == "scout"
                and row["tier"] == "strong"
                and row["seed"] == "1"
            )
        ]
        report = analyze_handoff_rows(rows)
        self.assertEqual(report["summary"]["usable_state_count"], 0)
        self.assertEqual(report["summary"]["incomplete_state_count"], 1)
        self.assertEqual(report["summary"]["positive_voi_rate"], 0.0)

    def test_current_acquisition_cost_must_be_zero(self) -> None:
        rows = self.positive_rows()
        rows[0]["acquisition_cost"] = 1.0
        with self.assertRaisesRegex(ValueError, "current acquisition_cost must be zero"):
            analyze_handoff_rows(rows)

    def test_scout_acquisition_cost_must_be_frozen_across_tiers(self) -> None:
        rows = self.positive_rows()
        for row in rows:
            if row["information"] == "scout" and row["tier"] == "strong":
                row["acquisition_cost"] = 2.0
        with self.assertRaisesRegex(ValueError, "identical across tiers and seeds"):
            analyze_handoff_rows(rows)

    def test_expected_missing_state_remains_in_itt_denominator(self) -> None:
        report = analyze_handoff_rows(
            self.positive_rows(),
            expected_states={("t1", "c1"), ("t2", "c2")},
        )
        self.assertEqual(report["summary"]["expected_state_count"], 2)
        self.assertEqual(report["summary"]["observed_state_count"], 1)
        self.assertEqual(report["summary"]["usable_state_count"], 1)
        self.assertEqual(report["summary"]["incomplete_state_count"], 1)
        self.assertEqual(report["summary"]["positive_voi_rate"], 0.5)
        self.assertEqual(report["summary"]["positive_voi_complete_case_rate"], 1.0)

    def test_frozen_scout_estimand_is_max_of_repair_seed_means(self) -> None:
        rows = handoff_grid(
            {
                ("current", "cheap"): (0.4, 0.0, 0.0),
                ("current", "strong"): (0.4, 0.0, 0.0),
                ("scout", "cheap"): ({"1": 1.0, "2": 0.0}, 0.0, 0.0),
                ("scout", "strong"): ({"1": 0.0, "2": 1.0}, 0.0, 0.0),
            }
        )
        state = analyze_handoff_rows(rows, lambda_cost=0.0)["states"][0]
        self.assertAlmostEqual(state["current_system_utility"], 0.4)
        self.assertAlmostEqual(state["scout_system_utility"], 0.5)
        self.assertAlmostEqual(state["voi"], 0.1)


if __name__ == "__main__":
    unittest.main()
