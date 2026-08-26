import json
import tempfile
import unittest
from pathlib import Path

from sample_arb_abstention import build_manifest


class ArbAbstentionSampleTests(unittest.TestCase):
    def _source(self, root: Path) -> Path:
        source = root / "samples.jsonl"
        rows = []
        for organic in (True, False):
            for index in range(8):
                rows.append(
                    {
                        "id": f"{'n' if organic else 'c'}{index}",
                        "task_type": "abstention",
                        "repo": f"org/repo{index % 4}",
                        "base_commit": f"commit-{organic}-{index}",
                        "query": {"text": f"secret query {index}"},
                        "gold": {"files": []},
                        "metadata": {
                            "organic": organic,
                            "evidence_summary": "must not be emitted",
                        },
                    }
                )
        source.write_text(
            "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
        )
        return source

    def test_balanced_selection_is_deterministic_and_blind(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = self._source(root)
            kwargs = {
                "archive_sha256": "abc",
                "arb_code_commit": "commit",
                "salt": "fixed",
                "count_per_stratum": 4,
                "max_per_repo": 2,
                "workspace_root": root,
            }
            first = build_manifest(source, **kwargs)
            second = build_manifest(source, **kwargs)
            self.assertEqual(first, second)
            self.assertEqual(
                first["counts_by_stratum"],
                {"counterfactual_wrong_repo": 4, "natural": 4},
            )
            serialized = json.dumps(first)
            self.assertNotIn("secret query", serialized)
            self.assertNotIn("evidence_summary", serialized)
            self.assertNotIn('"gold"', serialized)

    def test_repo_cap_applies_within_each_stratum(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = build_manifest(
                self._source(root),
                archive_sha256="abc",
                arb_code_commit="commit",
                salt="fixed",
                count_per_stratum=4,
                max_per_repo=1,
                workspace_root=root,
            )
            counts = {}
            for row in report["samples"]:
                key = (row["stratum"], row["repo"])
                counts[key] = counts.get(key, 0) + 1
            self.assertTrue(all(value <= 1 for value in counts.values()))

    def test_non_boolean_organic_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "samples.jsonl"
            source.write_text(
                json.dumps(
                    {
                        "id": "x",
                        "task_type": "abstention",
                        "repo": "org/repo",
                        "base_commit": "c",
                        "metadata": {"organic": "yes"},
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "metadata.organic"):
                build_manifest(
                    source,
                    archive_sha256="abc",
                    arb_code_commit="commit",
                    salt="fixed",
                    count_per_stratum=1,
                    max_per_repo=1,
                )


if __name__ == "__main__":
    unittest.main()
