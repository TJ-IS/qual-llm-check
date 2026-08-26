from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from summarize_arb_baselines import (
    DataValidationError,
    KEY_METRICS,
    METHODS,
    RELEASES,
    TASK_TYPES,
    render_markdown,
    summarize,
)


def _write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _metrics(*, gold_fraction: float, offset: float) -> dict[str, float]:
    payload: dict[str, float] = {}
    for index, metric in enumerate(KEY_METRICS, start=1):
        if metric == "gold_coverage@8k":
            value = gold_fraction
        elif metric == "context_pollution_tokens@8k":
            value = 1000.0 + offset * 100.0 + index
        elif metric.startswith("hard_negative_hits") or metric.startswith(
            "irrelevant_files"
        ):
            value = offset + index / 10.0
        else:
            value = min(0.95, 0.05 + offset / 10.0 + index / 1000.0)
        payload[metric] = value
    return payload


class ArbBaselineFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.eval_root = root / "eval"
        self.eval_root.mkdir()
        self.manifest_path = root / "arb60_selection_v0.json"
        self.samples: list[dict] = []
        pilot_index = 0
        for release in RELEASES:
            for within_index in (1, 2):
                pilot_index += 1
                self.samples.append(
                    {
                        "pilot_index": pilot_index,
                        "within_release_index": within_index,
                        "release_id": release,
                        "task_type": TASK_TYPES[release],
                        "sample_id": f"{release}-sample-{within_index}",
                        "repo": f"org/{release}-repo-{within_index}",
                        "base_commit": f"{pilot_index:040x}",
                    }
                )
        manifest = {
            "schema_version": 1,
            "sample_count": len(self.samples),
            "counts_by_task_type": {
                TASK_TYPES[release]: 2 for release in RELEASES
            },
            "samples": self.samples,
        }
        _write_json(self.manifest_path, manifest)
        self._write_eval_grid()

    def _write_eval_grid(self) -> None:
        for release_index, release in enumerate(RELEASES):
            release_dir = self.eval_root / release
            release_dir.mkdir()
            release_samples = [
                sample for sample in self.samples if sample["release_id"] == release
            ]
            for method_index, method in enumerate(METHODS):
                rows = []
                for sample_index, sample in enumerate(release_samples):
                    if sample_index == 0:
                        gold_fraction = {
                            "lexical": 1.0,
                            "bm25": 0.0,
                            "repomap": 0.5,
                        }[method]
                    else:
                        gold_fraction = 0.0
                    metric_payload = _metrics(
                        gold_fraction=gold_fraction,
                        offset=float(release_index + method_index + sample_index),
                    )
                    gold_files = [
                        f"{sample['sample_id']}/gold-a.py",
                        f"{sample['sample_id']}/gold-b.py",
                    ]
                    if sample_index == 0:
                        top_files = {
                            "lexical": [gold_files[0], "irrelevant/lexical.py"],
                            "bm25": [gold_files[1], "irrelevant/bm25.py"],
                            "repomap": [gold_files[0], "irrelevant/repomap.py"],
                        }[method]
                    else:
                        top_files = [f"irrelevant/{method}.py"]
                    metric_payload["Recall@20"] = len(
                        set(gold_files).intersection(top_files[:20])
                    ) / len(gold_files)
                    row = {
                        "sample_id": sample["sample_id"],
                        "task_type": sample["task_type"],
                        "repo": sample["repo"],
                        "base_commit": sample["base_commit"],
                        "metrics": metric_payload,
                        "gold_files": gold_files,
                        "top_files": top_files,
                    }
                    if method != "repomap":
                        row["ranker"] = method
                    rows.append(row)
                details_path = release_dir / f"{method}_details.jsonl"
                details_path.write_text(
                    "".join(
                        json.dumps(row, sort_keys=True) + "\n"
                        for row in reversed(rows)
                    ),
                    encoding="utf-8",
                )
                means = {
                    metric: sum(row["metrics"][metric] for row in rows) / len(rows)
                    for metric in KEY_METRICS
                }
                means["samples"] = len(rows)
                summary = {
                    "evaluated": len(rows),
                    "skipped": {},
                    "metrics": {
                        "overall": dict(means),
                        TASK_TYPES[release]: dict(means),
                    },
                }
                if method != "repomap":
                    summary["ranker"] = method
                _write_json(release_dir / f"{method}_summary.json", summary)

    def details_path(self, release: str, method: str) -> Path:
        return self.eval_root / release / f"{method}_details.jsonl"

    def summary_path(self, release: str, method: str) -> Path:
        return self.eval_root / release / f"{method}_summary.json"


class ArbBaselineSummaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.fixture = ArbBaselineFixture(Path(self.temp.name))

    def test_valid_grid_is_deterministic_descriptive_and_legacy_labeled(self) -> None:
        first = summarize(self.fixture.eval_root, self.fixture.manifest_path)
        second = summarize(self.fixture.eval_root, self.fixture.manifest_path)
        self.assertEqual(first, second)
        self.assertTrue(first["complete_three_by_three_design"])
        self.assertEqual(first["macro"]["sample_count"], 6)
        expected_hash = hashlib.sha256(self.fixture.manifest_path.read_bytes()).hexdigest()
        self.assertEqual(first["sample_manifest"]["file_sha256"], expected_hash)
        self.assertFalse(first["metric_provenance"]["canonical_bcy_included"])
        lexical_metrics = first["releases"][RELEASES[0]]["methods"]["lexical"][
            "key_metrics"
        ]
        self.assertIn("legacy_gold_file_fraction@8k_chars", lexical_metrics)
        self.assertIn("legacy_context_efficiency@8k_chars", lexical_metrics)
        self.assertNotIn("gold_coverage@8k", lexical_metrics)
        first_task = first["releases"][RELEASES[0]]["tasks"][0]
        self.assertEqual(first_task["legacy_all_gold_files_methods"], ["lexical"])
        self.assertTrue(first_task["legacy_all_gold_files_outcomes_differ"])
        self.assertTrue(
            first_task["unbounded_top20_union_diagnostic"][
                "unbounded_union_strictly_improves"
            ]
        )
        self.assertEqual(
            first["macro"]["unbounded_top20_union_diagnostic"][
                "unbounded_union_strictly_improves"
            ]["count"],
            len(RELEASES),
        )
        second_task = first["releases"][RELEASES[0]]["tasks"][1]
        self.assertTrue(second_task["all_methods_zero_legacy_gold_file_fraction"])
        markdown = render_markdown(first)
        self.assertIn("Legacy gold-file fraction@8K chars", markdown)
        self.assertIn("not canonical token-packed BCY", markdown)
        self.assertNotIn("Gold coverage@8K", markdown)
        self.assertIn("not equal-cost", markdown)

    def test_duplicate_detail_sample_is_rejected(self) -> None:
        path = self.fixture.details_path(RELEASES[0], "lexical")
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines + [lines[0]]) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(DataValidationError, "duplicate sample_id"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)

    def test_missing_detail_sample_is_rejected(self) -> None:
        path = self.fixture.details_path(RELEASES[1], "bm25")
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text(lines[0] + "\n", encoding="utf-8")
        with self.assertRaisesRegex(DataValidationError, "sample IDs do not match"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)

    def test_untracked_extra_detail_sample_is_rejected(self) -> None:
        path = self.fixture.details_path(RELEASES[2], "lexical")
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        extra = dict(rows[0])
        extra["sample_id"] = "not-in-selection"
        path.write_text(
            "".join(json.dumps(row) + "\n" for row in rows + [extra]),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(DataValidationError, "not in tracked selection"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)

    def test_missing_expected_result_file_is_rejected(self) -> None:
        self.fixture.summary_path(RELEASES[0], "bm25").unlink()
        with self.assertRaisesRegex(DataValidationError, "missing expected result files"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)

    def test_blank_ranker_is_allowed_only_for_fixed_repomap_files(self) -> None:
        valid = summarize(self.fixture.eval_root, self.fixture.manifest_path)
        self.assertEqual(valid["expected_methods"], list(METHODS))
        path = self.fixture.summary_path(RELEASES[0], "lexical")
        summary = _read_json(path)
        summary["ranker"] = ""
        _write_json(path, summary)
        with self.assertRaisesRegex(DataValidationError, "blank ranker is allowed only"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)

    def test_repomap_nonblank_conflicting_ranker_is_rejected(self) -> None:
        path = self.fixture.details_path(RELEASES[0], "repomap")
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        rows[0]["ranker"] = "lexical"
        path.write_text(
            "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
        )
        with self.assertRaisesRegex(DataValidationError, "conflicts with fixed filename"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)

    def test_summary_detail_metric_mismatch_is_rejected(self) -> None:
        path = self.fixture.summary_path(RELEASES[1], "repomap")
        summary = _read_json(path)
        summary["metrics"]["overall"]["MRR"] += 0.1
        _write_json(path, summary)
        with self.assertRaisesRegex(DataValidationError, "differs from detail mean"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)

    def test_duplicate_selection_sample_is_rejected(self) -> None:
        manifest = _read_json(self.fixture.manifest_path)
        manifest["samples"][1]["sample_id"] = manifest["samples"][0]["sample_id"]
        _write_json(self.fixture.manifest_path, manifest)
        with self.assertRaisesRegex(DataValidationError, "duplicate sample_id"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)

    def test_unexpected_result_filename_is_rejected(self) -> None:
        release_dir = self.fixture.eval_root / RELEASES[0]
        _write_json(release_dir / "mystery_summary.json", {})
        with self.assertRaisesRegex(DataValidationError, "unexpected result files"):
            summarize(self.fixture.eval_root, self.fixture.manifest_path)


if __name__ == "__main__":
    unittest.main()
