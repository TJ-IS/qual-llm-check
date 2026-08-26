from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "data:", "#")


def normalize_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0]
    return unquote(target).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("--output")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    markdown_files = sorted(root.rglob("*.md"))
    checked_links = 0
    broken: list[dict[str, object]] = []

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                raw = match.group(1).strip()
                if raw.lower().startswith(SKIP_PREFIXES):
                    continue
                target = normalize_target(raw)
                if not target:
                    continue
                checked_links += 1
                candidate = Path(target)
                resolved = (
                    candidate if candidate.is_absolute() else (path.parent / candidate)
                ).resolve(strict=False)
                if not resolved.exists():
                    broken.append(
                        {
                            "source": str(path.relative_to(root)),
                            "line": line_number,
                            "target": raw,
                            "resolved": str(resolved),
                        }
                    )

    result = {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "audit_script": str(Path(__file__).resolve()),
        "audit_script_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "root": str(root),
        "markdown_files": len(markdown_files),
        "checked_local_links": checked_links,
        "broken_count": len(broken),
        "broken": broken,
        "scope_note": (
            "This audit checks only Markdown link target existence. It does not infer "
            "artifact role, schema, content hashes or supersedes relationships."
        ),
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
