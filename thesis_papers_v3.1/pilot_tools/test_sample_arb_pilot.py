from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from sample_arb_pilot import build_manifest, load_candidates, select_candidates


class ArbSampleTests(unittest.TestCase):
    def _source(self, root: Path, task_type: str, rows: int = 12) -> Path:
        path = root / f"{task_type}.jsonl"
        records = []
        for index in range(rows):
            records.append(
                {
                    "id": f"{task_type}-{index:02d}",
                    "task_type": task_type,
                    "repo": f"org/repo{index % 4}",
                    "base_commit": f"commit-{index}",
                    "gold": {"must_not_affect_selection": index},
                }
            )
        path.write_text(
            "".join(json.dumps(item) + "\n" for item in records), encoding="utf-8"
        )
        return path

    def test_selection_is_deterministic_and_respects_repo_cap(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = self._source(Path(temporary), "trace2code")
            rows = load_candidates("v2_trace2code", source)
            first = select_candidates(rows, salt="fixed", count=8, max_per_repo=2)
            second = select_candidates(rows, salt="fixed", count=8, max_per_repo=2)
            self.assertEqual([item.sample_id for item in first], [item.sample_id for item in second])
            counts: dict[str, int] = {}
            for item in first:
                counts[item.repo] = counts.get(item.repo, 0) + 1
            self.assertTrue(all(value <= 2 for value in counts.values()))

    def test_manifest_omits_query_and_gold(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self._source(root, "code2test")
            manifest = build_manifest(
                {"v2_code2test": source},
                archive_sha256={"v2_code2test": "abc"},
                arb_code_commit="def",
                salt="fixed",
                count_per_release=4,
                max_per_repo=1,
                workspace_root=root,
            )
            rendered = json.dumps(manifest)
            self.assertNotIn("must_not_affect_selection", rendered)
            self.assertNotIn('"gold"', rendered)
            self.assertNotIn('"query"', rendered)
            self.assertEqual(manifest["sample_count"], 4)

    def test_insufficient_capacity_fails_loudly(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = self._source(Path(temporary), "edit2ripple", rows=4)
            rows = load_candidates("v2_edit2ripple", source)
            with self.assertRaises(ValueError):
                select_candidates(rows, salt="fixed", count=4, max_per_repo=0)


if __name__ == "__main__":
    unittest.main()
