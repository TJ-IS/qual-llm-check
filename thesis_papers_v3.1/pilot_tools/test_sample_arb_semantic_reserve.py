from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from sample_arb_semantic_reserve import (
    CODE2TEST_QUOTA,
    TRACE2CODE_QUOTA,
    build_manifest,
)


class SemanticReserveTests(unittest.TestCase):
    def _write_release(self, root: Path, task_type: str) -> Path:
        path = root / f"{task_type}.jsonl"
        quotas = CODE2TEST_QUOTA if task_type == "code2test" else TRACE2CODE_QUOTA
        records = []
        for repo, count in quotas.items():
            for index in range(count + 2):
                query = (
                    {"changed_file": f"src/mod_{index}.py"}
                    if task_type == "code2test"
                    else {"failure_excerpt": f"tests/test_{index}.py:{index + 1}: AssertionError"}
                )
                records.append(
                    {
                        "id": f"{task_type}-{repo}-{index}",
                        "task_type": task_type,
                        "repo": repo,
                        "base_commit": f"commit-{task_type}-{repo}-{index}",
                        "query": query,
                        "gold": {"must_never_be_emitted": index},
                        "patch": "secret",
                    }
                )
        path.write_text("".join(json.dumps(row) + "\n" for row in records), encoding="utf-8")
        return path

    def _stage0(self, root: Path) -> Path:
        path = root / "stage0.json"
        path.write_text(
            json.dumps(
                {
                    "samples": [
                        {
                            "sample_id": "old",
                            "repo": "pallets/click",
                            "base_commit": "old-commit",
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        return path

    def test_manifest_is_deterministic_unique_and_gold_blind(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            releases = {
                "v2_code2test": self._write_release(root, "code2test"),
                "v2_trace2code": self._write_release(root, "trace2code"),
            }
            arguments = dict(
                stage0_manifest_path=self._stage0(root),
                arb_code_commit="arb-commit",
                archive_sha256={"v2_code2test": "a", "v2_trace2code": "b"},
                workspace_root=root,
            )
            first = build_manifest(releases, **arguments)
            second = build_manifest(releases, **arguments)
            self.assertEqual(first, second)
            self.assertEqual(first["sample_count"], 16)
            snapshots = {(row["repo"], row["base_commit"]) for row in first["samples"]}
            self.assertEqual(len(snapshots), 16)
            rendered = json.dumps(first)
            self.assertNotIn("must_never_be_emitted", rendered)
            self.assertNotIn('"gold"', rendered)
            self.assertNotIn('"patch"', rendered)
            self.assertEqual(first["status"], "RESERVE_ONLY_NO_SEMANTIC_RUN")

    def test_stage0_snapshot_is_excluded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            releases = {
                "v2_code2test": self._write_release(root, "code2test"),
                "v2_trace2code": self._write_release(root, "trace2code"),
            }
            first_row = json.loads(releases["v2_code2test"].read_text(encoding="utf-8").splitlines()[0])
            stage0 = root / "stage0.json"
            stage0.write_text(
                json.dumps(
                    {
                        "samples": [
                            {
                                "sample_id": "different-id",
                                "repo": first_row["repo"],
                                "base_commit": first_row["base_commit"],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            report = build_manifest(
                releases,
                stage0_manifest_path=stage0,
                arb_code_commit="arb",
                archive_sha256={},
            )
            self.assertNotIn(
                (first_row["repo"], first_row["base_commit"]),
                {(row["repo"], row["base_commit"]) for row in report["samples"]},
            )

    def test_capacity_failure_is_loud(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code = self._write_release(root, "code2test")
            rows = [json.loads(line) for line in code.read_text(encoding="utf-8").splitlines()]
            code.write_text(
                "".join(json.dumps(row) + "\n" for row in rows if row["repo"] != "fastapi/fastapi"),
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                build_manifest(
                    {
                        "v2_code2test": code,
                        "v2_trace2code": self._write_release(root, "trace2code"),
                    },
                    stage0_manifest_path=self._stage0(root),
                    arb_code_commit="arb",
                    archive_sha256={},
                )


if __name__ == "__main__":
    unittest.main()
