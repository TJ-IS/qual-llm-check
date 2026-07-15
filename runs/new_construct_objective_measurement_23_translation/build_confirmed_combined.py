from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
CONFIRMED_DIR = REPO_ROOT / "database_fulltext_new_construct_objective_confirmed"
SOURCE_DIR = HERE / "source_en"
PROGRESS_DIR = HERE / ".progress"
ENGLISH_OUTPUT = CONFIRMED_DIR / "all_7_confirmed_fulltexts_en.md"
BILINGUAL_OUTPUT = CONFIRMED_DIR / "all_7_confirmed_fulltexts_en_zh.md"

AUDIT_FILE = "00_人工复核说明.md"
PARAGRAPH_BREAK = re.compile(r"\n[ \t]*\n+")
FRONTMATTER = re.compile(r"\A---\n(?P<yaml>.*?)\n---(?:\n|\Z)", re.DOTALL)
TITLE = re.compile(r'^title:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
ZH_TAG = re.compile(r"<!--\s*ZH\s*-->", re.IGNORECASE)
NO_TRANSLATION = "（代码、公式、图片引用或其他非语言内容，无需翻译。）"


def normalized_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compact_block(text: str) -> str:
    text = ZH_TAG.sub("", text).replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    compacted: list[str] = []
    previous_blank = False
    for line in lines:
        if line.strip():
            compacted.append(line)
            previous_blank = False
        elif compacted and not previous_blank:
            compacted.append("")
            previous_blank = True
    while compacted and not compacted[-1]:
        compacted.pop()
    return "\n".join(compacted).strip()


def clean_chinese_translation(text: str) -> str:
    text = compact_block(text).replace(NO_TRANSLATION, "").strip()
    cleaned_lines: list[str] = []
    for line in text.split("\n"):
        heading = re.match(r"^(＃+)\s*(.*)$", line)
        if heading:
            line = "#" * len(heading.group(1)) + " " + heading.group(2).lstrip()
        cleaned_lines.append(line)
    return compact_block("\n".join(cleaned_lines))


def split_paragraphs(text: str) -> list[str]:
    normalized = text.strip()
    return [compact_block(block) for block in PARAGRAPH_BREAK.split(normalized) if block.strip()]


def metadata_and_body(text: str, fallback_title: str) -> tuple[str, str]:
    match = FRONTMATTER.match(text)
    yaml = match.group("yaml") if match else ""
    title_match = TITLE.search(yaml)
    title = title_match.group(1).strip().strip("\"'") if title_match else fallback_title
    body = text[match.end() :] if match else text
    body = body.lstrip("\n")
    lines = body.split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return title, "\n".join(lines).strip()


def render_blocks(blocks: list[str]) -> str:
    cleaned = [compact_block(block) for block in blocks if compact_block(block)]
    return "\n\n".join(cleaned).rstrip() + "\n"


def checkpoint_for(source_path: Path, paragraph_count: int, source_hash: str) -> dict[str, str]:
    path = PROGRESS_DIR / f"{source_path.name}.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("source_sha256") != source_hash:
        raise ValueError(f"Checkpoint hash mismatch: {source_path.name}")
    if payload.get("paragraph_count") != paragraph_count:
        raise ValueError(f"Checkpoint paragraph count mismatch: {source_path.name}")
    translations = payload.get("translations")
    if not isinstance(translations, dict) or len(translations) != paragraph_count:
        raise ValueError(f"Incomplete checkpoint: {source_path.name}")
    return {str(key): str(value) for key, value in translations.items()}


def translation_is_redundant(english: str, chinese: str) -> bool:
    chinese_without_notice = chinese.replace(NO_TRANSLATION, "").strip()
    if not chinese_without_notice:
        return True
    return compact_block(english) == compact_block(chinese_without_notice)


def main() -> None:
    selected = sorted(
        path
        for path in CONFIRMED_DIR.glob("*.md")
        if path.name != AUDIT_FILE and not path.name.startswith("all_7_confirmed_fulltexts_")
    )
    if len(selected) != 7:
        raise SystemExit(f"Expected 7 confirmed article files, found {len(selected)}")

    english_blocks = ["# Seven Confirmed New-Construct Objective-Measurement Articles: Full Texts"]
    bilingual_blocks = ["# 七篇确认文献：英文—中文逐段全文合集"]
    translated_pairs = 0
    structural_blocks = 0

    for article_number, confirmed_path in enumerate(selected, start=1):
        confirmed_text = normalized_text(confirmed_path)
        title, confirmed_body = metadata_and_body(confirmed_text, confirmed_path.stem)
        english_blocks.append(f"# Article {article_number}: {title}")
        english_blocks.extend(split_paragraphs(confirmed_body))

        source_path = SOURCE_DIR / confirmed_path.name
        source_text = normalized_text(source_path)
        source_paragraphs = split_paragraphs(source_text)
        translations = checkpoint_for(source_path, len(source_paragraphs), sha256_text(source_text))
        bilingual_blocks.append(f"# 第 {article_number} 篇 / Article {article_number}: {title}")

        for index, english in enumerate(source_paragraphs):
            if index == 0 and english.startswith("---\n"):
                # The first cached block contains retrieval frontmatter plus the original H1.
                # Both are replaced by the clean article boundary heading above.
                continue
            bilingual_blocks.append(english)
            chinese = clean_chinese_translation(translations[str(index)])
            if translation_is_redundant(english, chinese):
                structural_blocks += 1
                continue
            bilingual_blocks.append(chinese)
            translated_pairs += 1

    ENGLISH_OUTPUT.write_text(render_blocks(english_blocks), encoding="utf-8")
    BILINGUAL_OUTPUT.write_text(render_blocks(bilingual_blocks), encoding="utf-8")
    print(f"articles={len(selected)}")
    print(f"translated_pairs={translated_pairs}")
    print(f"structural_blocks_without_duplicate_translation={structural_blocks}")
    print(f"english_output={ENGLISH_OUTPUT}")
    print(f"bilingual_output={BILINGUAL_OUTPUT}")


if __name__ == "__main__":
    main()
