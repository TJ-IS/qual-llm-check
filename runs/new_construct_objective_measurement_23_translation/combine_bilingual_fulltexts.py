from __future__ import annotations

import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT_DIR = HERE / "bilingual_zh"
OUTPUT_PATH = HERE / "all_23_bilingual_fulltexts.md"
TITLE_PATTERN = re.compile(r'^title:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)


def article_title(text: str, fallback: str) -> str:
    match = TITLE_PATTERN.search(text)
    if not match:
        return fallback
    return match.group(1).strip().strip('"\'') or fallback


def main() -> None:
    files = sorted(INPUT_DIR.glob("*.md"))
    if len(files) != 23:
        raise SystemExit(f"Expected 23 bilingual Markdown files, found {len(files)}")

    articles: list[tuple[Path, str, str]] = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace").strip()
        articles.append((path, article_title(text, path.stem), text))

    parts = [
        "# 23 篇新构念客观测量文献：中英逐段全文合集",
        "",
        "> 每篇文章均保持英文段落在前、对应中文翻译在后的顺序。",
        "",
        "## 目录",
        "",
    ]
    for index, (_, title, _) in enumerate(articles, start=1):
        parts.append(f"{index}. {title}")

    for index, (path, title, text) in enumerate(articles, start=1):
        parts.extend(
            [
                "",
                "---",
                "",
                f"# 第 {index} 篇：{title}",
                "",
                f"> 原双语文件：`{path.name}`",
                "",
                text,
            ]
        )

    OUTPUT_PATH.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Combined {len(articles)} articles into {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
