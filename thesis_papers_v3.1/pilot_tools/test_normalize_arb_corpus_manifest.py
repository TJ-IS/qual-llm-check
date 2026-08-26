from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from normalize_arb_corpus_manifest import normalize_records, write_manifest


class NormalizeManifestTests(unittest.TestCase):
    def test_rewrites_data_root_without_touching_release(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            chunk = root / "corpus" / "v2" / "repo" / "commit.chunks.jsonl"
            chunk.parent.mkdir(parents=True)
            chunk.write_text("{}\n", encoding="utf-8")
            source = root / "released.jsonl"
            original = {"repo": "org/repo", "chunks_path": "data/corpus/v2/repo/commit.chunks.jsonl"}
            source.write_text(json.dumps(original) + "\n", encoding="utf-8")

            records = normalize_records(source, root)
            self.assertTrue(records[0]["pilot_path_exists"])
            self.assertEqual(Path(records[0]["chunks_path"]), chunk.resolve())
            self.assertEqual(json.loads(source.read_text(encoding="utf-8")), original)

            output = root / "normalized" / "corpus_manifest.jsonl"
            write_manifest(records, output)
            self.assertTrue(output.is_file())


if __name__ == "__main__":
    unittest.main()
