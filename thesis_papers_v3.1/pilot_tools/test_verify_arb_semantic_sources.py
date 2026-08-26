from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from verify_arb_semantic_sources import NO_RUN_STATUS, READY_STATUS, verify_sources


def git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


class SemanticSourceVerifierTests(unittest.TestCase):
    def _repository(
        self,
        root: Path,
        *,
        broken_query: bool = False,
        broken_other: bool = False,
    ) -> tuple[Path, str]:
        work = root / "work"
        work.mkdir()
        git(work.parent, "init", "--quiet", str(work))
        (work / "src").mkdir()
        query_text = "def broken(:\n" if broken_query else "def target():\n    return 1\n"
        (work / "src" / "target.py").write_text(query_text, encoding="utf-8")
        if broken_other:
            (work / "src" / "other.py").write_text("def broken(:\n", encoding="utf-8")
        (work / "README.md").write_text("fixture\n", encoding="utf-8")
        git(work, "add", ".")
        git(
            work,
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.com",
            "commit",
            "--quiet",
            "-m",
            "fixture",
        )
        commit = git(work, "rev-parse", "HEAD")
        asset_root = root / "assets"
        bare = asset_root / "org__repo"
        asset_root.mkdir()
        git(root, "clone", "--quiet", "--bare", str(work), str(bare))
        return asset_root, commit

    def _manifest(self, commit: str) -> dict:
        return {
            "status": "RESERVE_ONLY_NO_SEMANTIC_RUN",
            "sample_count": 1,
            "samples": [
                {
                    "sample_id": "s1",
                    "task_type": "code2test",
                    "repo": "org/repo",
                    "base_commit": commit,
                    "query_paths": ["src/target.py"],
                }
            ],
        }

    def test_complete_query_source_is_ready(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            assets, commit = self._repository(root)
            summary, rows = verify_sources(self._manifest(commit), asset_root=assets)
            self.assertEqual(summary["status"], READY_STATUS)
            self.assertTrue(summary["all_query_paths_present"])
            self.assertTrue(summary["all_query_python_ast_ready"])
            query_rows = [row for row in rows if row["is_query_path"]]
            self.assertEqual(len(query_rows), 1)
            self.assertEqual(len(query_rows[0]["sha256"]), 64)

    def test_broken_query_source_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            assets, commit = self._repository(root, broken_query=True)
            summary, _ = verify_sources(self._manifest(commit), asset_root=assets)
            self.assertEqual(summary["status"], NO_RUN_STATUS)
            self.assertFalse(summary["all_query_python_ast_ready"])

    def test_missing_query_path_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            assets, commit = self._repository(root)
            manifest = self._manifest(commit)
            manifest["samples"][0]["query_paths"] = ["src/missing.py"]
            summary, _ = verify_sources(manifest, asset_root=assets)
            self.assertEqual(summary["status"], NO_RUN_STATUS)
            self.assertFalse(summary["all_query_paths_present"])

    def test_repository_parse_rate_gate_fails_even_when_query_parses(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            assets, commit = self._repository(root, broken_other=True)
            summary, _ = verify_sources(
                self._manifest(commit),
                asset_root=assets,
                minimum_python_parse_rate=1.0,
            )
            self.assertEqual(summary["status"], NO_RUN_STATUS)
            self.assertTrue(summary["all_query_python_ast_ready"])
            self.assertLess(summary["python_ast_parse_rate"], 1.0)


if __name__ == "__main__":
    unittest.main()
