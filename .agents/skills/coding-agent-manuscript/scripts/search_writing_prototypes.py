#!/usr/bin/env python3
"""Find candidate writing prototypes in the frozen authoritative IS corpus.

The ranker is a discovery aid. It never verifies a prototype or substantive
evidence; a reviewer must reopen the original paragraph and major section.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_MANIFEST = SKILL_DIR / "references" / "authoritative-writing-corpus.json"

FUNCTIONS: dict[str, dict[str, tuple[str, ...]]] = {
    "context": {
        "patterns": (r"\bhas become\b", r"\bin recent years\b", r"\bwith the\b", r"\btoday\b"),
        "sections": ("introduction", "background"),
    },
    "prior-work": {
        "patterns": (r"\bprior (?:research|studies|work)\b", r"\bextant (?:research|studies|work)\b", r"\brecent studies\b", r"\bresearchers have\b"),
        "sections": ("introduction", "literature", "background", "related"),
    },
    "gap": {
        "patterns": (r"\bhowever\b", r"\bnevertheless\b", r"\blittle is known\b", r"\bremain(?:s)? (?:unclear|unknown|under)\b", r"\bfail(?:s|ed)? to\b", r"\blimit(?:s|ed|ation)\b", r"\bshortcoming\b"),
        "sections": ("introduction", "literature", "background", "challenge"),
    },
    "theory-bridge": {
        "patterns": (r"\bdrawing on\b", r"\bbased on (?:the|this) theor", r"\btheory (?:suggests|posits|provides|guides|explains)\b", r"\btheoretical (?:foundation|analysis|perspective|rationale)\b", r"\bposit(?:s|ing)? that\b", r"\bguides? our design\b", r"\bmotivates? (?:our|the)\b", r"\bin light of\b"),
        "sections": ("theor", "background", "design", "challenge", "introduction"),
    },
    "research-question": {
        "patterns": (r"\bresearch question\b", r"\bwe (?:ask|investigate|examine|seek to)\b", r"\bour (?:aim|objective)\b", r"\bthis study aims?\b"),
        "sections": ("introduction", "background", "literature"),
    },
    "artifact-overview": {
        "patterns": (r"\bwe (?:propose|develop|design|present|introduce)\b", r"\bour proposed\b", r"\bthe proposed (?:method|framework|model|artifact)\b", r"\bdrawing on.*develop\b"),
        "sections": ("introduction", "method", "design", "approach", "framework"),
    },
    "method-step": {
        "patterns": (r"\bfirst\b", r"\bsecond\b", r"\bnext\b", r"\bthen\b", r"\bafter (?:that|the)\b", r"\bwe (?:calculate|construct|derive|estimate|obtain|use|adopt|train|update|map|encode)\b", r"\bspecifically\b"),
        "sections": ("method", "design", "approach", "framework", "model", "data"),
    },
    "evaluation-design": {
        "patterns": (r"\bwe (?:evaluate|compare|test|examine|assess)\b", r"\bfor (?:the )?evaluation\b", r"\bbenchmark\b", r"\bexperiment\b", r"\bempirical(?:ly)?\b"),
        "sections": ("evaluation", "experiment", "empirical", "result"),
    },
    "result-interpretation": {
        "patterns": (r"\bresults? (?:show|indicate|suggest|demonstrate)\b", r"\bwe (?:find|found|observe|observed)\b", r"\bconsistent with\b", r"\bcompared with\b", r"\boutperform(?:s|ed)?\b"),
        "sections": ("result", "evaluation", "experiment", "analysis"),
    },
    "contribution": {
        "patterns": (r"\bcontribution\b", r"\bwe contribute\b", r"\bthis study (?:makes|offers|provides)\b", r"\bimplication\b"),
        "sections": ("contribution", "discussion", "implication", "conclusion", "introduction"),
    },
    "boundary": {
        "patterns": (r"\blimit(?:ation|ations|ed)?\b", r"\balthough\b", r"\bwhile\b", r"\bwhereas\b", r"\bmay not\b", r"\bcannot\b", r"\bfuture research\b", r"\bonly when\b"),
        "sections": ("limitation", "discussion", "conclusion", "method", "evaluation"),
    },
}

STOP_WORDS = {
    "about", "after", "again", "against", "also", "among", "and", "are", "because", "been", "before",
    "being", "between", "both", "can", "could", "does", "for", "from", "have", "into", "its", "more", "most",
    "our", "over", "such", "than", "that", "the", "their", "these", "this", "those", "through", "under",
    "using", "was", "were", "which", "while", "with", "would",
}

ABBREVIATIONS = (
    "e.g.", "i.e.", "et al.", "Fig.", "Figs.", "Eq.", "Eqs.", "No.", "Nos.", "vs.", "Dr.", "Mr.", "Prof.", "U.S.", "U.K."
)
DOT_SENTINEL = "∯"
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[.!?])\s+(?=(?:[\"“‘(\[]?[A-Z0-9]))")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z-]{2,}")
CITATION_RE = re.compile(
    r"\([^)]*\b(?:19|20)\d{2}[a-z]?\b[^)]*\)|\b[A-Z][A-Za-z'’-]+(?:\s+et\s+al\.)?\s*\((?:19|20)\d{2}[a-z]?\)"
)


@dataclass(frozen=True)
class SentenceRecord:
    source: dict[str, Any]
    section: str
    line: int
    sentence: str
    previous: str
    next: str
    paragraph: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def resolve_manifest_source(path_text: str, names_cache: dict[Path, set[str]]) -> Path:
    """Resolve one repository-relative POSIX path and enforce exact component case."""
    if (
        not path_text
        or "\\" in path_text
        or path_text.startswith("/")
        or re.match(r"^[A-Za-z]:", path_text)
    ):
        raise ValueError(f"manifest source path must be repository-relative POSIX text: {path_text!r}")
    pure = PurePosixPath(path_text)
    if any(part in {"", ".", ".."} for part in pure.parts):
        raise ValueError(f"manifest source path contains an unsafe component: {path_text!r}")

    current = REPO_ROOT.resolve()
    for part in pure.parts:
        names = names_cache.get(current)
        if names is None:
            try:
                names = {entry.name for entry in current.iterdir()}
            except OSError as exc:
                raise FileNotFoundError(current) from exc
            names_cache[current] = names
        if part not in names:
            case_matches = sorted(name for name in names if name.casefold() == part.casefold())
            if case_matches:
                raise ValueError(
                    f"manifest source path case mismatch: {path_text!r}; "
                    f"component {part!r} should be {case_matches[0]!r}"
                )
            raise FileNotFoundError(current / part)
        current = current / part

    resolved = current.resolve()
    try:
        resolved.relative_to(REPO_ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"source escapes repository: {path_text}") from exc
    return resolved


def split_sentences(paragraph: str) -> list[str]:
    protected = paragraph
    for abbreviation in ABBREVIATIONS:
        protected = re.sub(
            re.escape(abbreviation),
            abbreviation.replace(".", DOT_SENTINEL),
            protected,
            flags=re.IGNORECASE,
        )
    parts = SENTENCE_BOUNDARY_RE.split(protected)
    return [part.replace(DOT_SENTINEL, ".").strip() for part in parts if part.strip()]


def searchable(text: str) -> str:
    without_html = re.sub(r"<[^>]+>", " ", text)
    without_markdown = re.sub(r"[`*_]", " ", without_html)
    return re.sub(r"\s+", " ", without_markdown).strip()


def query_tokens(text: str) -> set[str]:
    return {token.casefold() for token in WORD_RE.findall(text) if token.casefold() not in STOP_WORDS}


def iter_paragraphs(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    seen_major_heading = False
    current_section = ""
    buffer: list[str] = []
    buffer_start = 0

    def flush():
        nonlocal buffer, buffer_start
        if buffer:
            paragraph = re.sub(r"\s+", " ", " ".join(buffer)).strip()
            if paragraph:
                yield current_section, buffer_start, paragraph
        buffer = []
        buffer_start = 0

    for line_number, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if in_frontmatter:
            if line_number > 1 and stripped == "---":
                in_frontmatter = False
            continue

        heading = HEADING_RE.match(stripped)
        if heading:
            yield from flush()
            level = len(heading.group(1))
            current_section = re.sub(r"<[^>]+>", "", heading.group(2)).strip()
            if level == 2:
                seen_major_heading = True
                if re.search(r"\b(references|bibliography)\b|参考文献", current_section, flags=re.IGNORECASE):
                    break
            continue

        if not seen_major_heading:
            continue
        if not stripped:
            yield from flush()
            continue
        if (
            stripped.startswith(("|", "![", "<table", "</table", "$$"))
            or re.fullmatch(r"[-:|\s]+", stripped)
        ):
            yield from flush()
            continue
        if not buffer:
            buffer_start = line_number
        buffer.append(stripped)

    yield from flush()


def load_manifest(path: Path, skip_hash_check: bool) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    sources = payload.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("manifest must contain a non-empty sources list")
    names_cache: dict[Path, set[str]] = {}
    for source in sources:
        source_path = resolve_manifest_source(str(source["path"]), names_cache)
        if not source_path.is_file():
            raise FileNotFoundError(source_path)
        if not skip_hash_check:
            actual = sha256_file(source_path)
            if actual != source["sha256"].upper():
                raise ValueError(f"hash mismatch for {source['id']}: {actual}")
        source["resolved_path"] = source_path
    return sources


def build_records(sources: list[dict[str, Any]]) -> list[SentenceRecord]:
    records: list[SentenceRecord] = []
    for source in sources:
        for section, line, paragraph in iter_paragraphs(source["resolved_path"]):
            sentences = split_sentences(paragraph)
            for index, sentence in enumerate(sentences):
                plain = searchable(sentence)
                if "�" in sentence or "??" in sentence:
                    continue
                if len(plain) < 40 or len(WORD_RE.findall(plain)) < 7:
                    continue
                records.append(
                    SentenceRecord(
                        source=source,
                        section=section,
                        line=line,
                        sentence=sentence,
                        previous=sentences[index - 1] if index else "",
                        next=sentences[index + 1] if index + 1 < len(sentences) else "",
                        paragraph=paragraph,
                    )
                )
    return records


def punctuation_profile(sentence: str) -> dict[str, int]:
    return {
        "comma": sentence.count(","),
        "semicolon": sentence.count(";"),
        "colon": sentence.count(":"),
        "dash": sentence.count("—") + sentence.count("–"),
        "parentheses": sentence.count("(") + sentence.count(")"),
    }


def context_warnings(paragraph: str) -> list[str]:
    warnings: list[str] = []
    if "�" in paragraph:
        warnings.append("mineru_replacement_character")
    if "??" in paragraph:
        warnings.append("unresolved_reference_marker")
    return warnings


def candidate_dict(record: SentenceRecord, score: int, overlap: list[str], function_hit: bool, section_hit: bool) -> dict[str, Any]:
    words = WORD_RE.findall(searchable(record.sentence))
    return {
        "score": score,
        "source_id": record.source["id"],
        "axis": record.source["axis"],
        "title": record.source["title"],
        "source_path": record.source["path"],
        "section": record.section,
        "paragraph_start_line": record.line,
        "sentence": record.sentence,
        "previous_sentence": record.previous,
        "next_sentence": record.next,
        "paragraph": record.paragraph,
        "function_marker_match": function_hit,
        "section_match": section_hit,
        "query_overlap": overlap,
        "has_citation": bool(CITATION_RE.search(record.sentence)),
        "leading_words": " ".join(words[:6]),
        "punctuation_profile": punctuation_profile(record.sentence),
        "context_warnings": context_warnings(record.paragraph),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--function", choices=sorted(FUNCTIONS))
    parser.add_argument("--query", default="", help="free English terms for lexical narrowing")
    parser.add_argument("--section", default="", help="case-insensitive regular expression applied to headings")
    parser.add_argument("--source", action="append", default=[], help="repeat to restrict source IDs")
    parser.add_argument("--axis", choices=("series_structural_baseline", "section_local_comparator"))
    parser.add_argument("--citation", choices=("any", "with", "without"), default="any")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--context", choices=("sentence", "neighbors", "paragraph"), default="neighbors")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--skip-hash-check", action="store_true", help="faster but removes frozen-corpus verification")
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args()
    if not args.function and not args.query.strip():
        print("ERROR provide --function, --query, or both", file=sys.stderr)
        return 2
    if args.limit < 1:
        print("ERROR --limit must be positive", file=sys.stderr)
        return 2
    try:
        section_re = re.compile(args.section, flags=re.IGNORECASE) if args.section else None
        sources = load_manifest(args.manifest.resolve(), args.skip_hash_check)
    except (FileNotFoundError, KeyError, ValueError, json.JSONDecodeError, re.error) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2

    known_ids = {source["id"] for source in sources}
    requested_ids = set(args.source)
    unknown = sorted(requested_ids - known_ids)
    if unknown:
        print("ERROR unknown source IDs: " + ", ".join(unknown), file=sys.stderr)
        return 2
    if requested_ids:
        sources = [source for source in sources if source["id"] in requested_ids]
    if args.axis:
        sources = [source for source in sources if source["axis"] == args.axis]

    function_spec = FUNCTIONS.get(args.function or "")
    function_patterns = [re.compile(pattern, flags=re.IGNORECASE) for pattern in function_spec["patterns"]] if function_spec else []
    section_hints = tuple(value.casefold() for value in function_spec["sections"]) if function_spec else ()
    requested_tokens = query_tokens(args.query)

    ranked: list[tuple[int, int, int, dict[str, Any]]] = []
    for record in build_records(sources):
        if section_re and not section_re.search(record.section):
            continue
        has_citation = bool(CITATION_RE.search(record.sentence))
        if args.citation == "with" and not has_citation:
            continue
        if args.citation == "without" and has_citation:
            continue
        plain = searchable(record.sentence)
        function_hit = any(pattern.search(plain) for pattern in function_patterns)
        section_hit = any(hint in record.section.casefold() for hint in section_hints)
        overlap = sorted(requested_tokens & query_tokens(plain))
        if requested_tokens and not overlap:
            continue
        score = (6 if function_hit else 0) + (2 if section_hit else 0) + 2 * len(overlap)
        score -= 3 * len(context_warnings(record.paragraph))
        if score <= 0:
            continue
        candidate = candidate_dict(record, score, overlap, function_hit, section_hit)
        ranked.append((score, int(record.source["priority"]), record.line, candidate))

    ranked.sort(key=lambda item: (-item[0], item[1], item[2]))
    candidates = [item[3] for item in ranked[: args.limit]]
    if args.json:
        print(json.dumps(candidates, ensure_ascii=False, indent=2))
        return 0

    print(
        f"Indexed {len(sources)} frozen sources; showing {len(candidates)} candidates. "
        "Scores are discovery signals, not prototype or evidence verdicts."
    )
    for index, candidate in enumerate(candidates, start=1):
        print(
            f"\n[{index}] score={candidate['score']} {candidate['source_id']} "
            f"line={candidate['paragraph_start_line']} section={candidate['section']}"
        )
        print(candidate["sentence"])
        if args.context == "neighbors":
            if candidate["previous_sentence"]:
                print("PREV: " + candidate["previous_sentence"])
            if candidate["next_sentence"]:
                print("NEXT: " + candidate["next_sentence"])
        elif args.context == "paragraph":
            print("PARAGRAPH: " + candidate["paragraph"])
        print(
            "FEATURES: citation={has_citation} leading={leading_words!r} punctuation={punctuation_profile} "
            "context_warnings={context_warnings}".format(
                **candidate
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
