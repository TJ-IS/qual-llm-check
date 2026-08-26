from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


REFERENCE_HEADING_RE = re.compile(
    r"^##\s+(?:参考文献|References|Bibliography)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
REFERENCE_ENTRY_RE = re.compile(
    r"^(?P<author>[^,\n]+),.*?\b(?P<year>(?:19|20)\d{2})\.",
    re.MULTILINE,
)
CITATION_GROUP_RE = re.compile(
    r"[（(](?P<group>[^()（）]*(?:(?:19|20)\d{2})[^()（）]*)[)）]"
)
YEAR_RE = re.compile(r"(?:19|20)\d{2}")


def split_body_and_references(text: str) -> tuple[str, str]:
    match = REFERENCE_HEADING_RE.search(text)
    if not match:
        return text, ""
    return text[: match.start()], text[match.end() :]


def reference_entries(reference_text: str) -> list[dict[str, str]]:
    return [
        {
            "author": match.group("author").strip(),
            "year": match.group("year"),
            "entry": match.group(0).strip(),
        }
        for match in REFERENCE_ENTRY_RE.finditer(reference_text)
    ]


def author_mentions(text: str, authors: list[str]) -> list[tuple[int, str]]:
    mentions: list[tuple[int, str]] = []
    for author in authors:
        pattern = r"(?<![A-Za-z])" + re.escape(author) + r"(?![A-Za-z])"
        for match in re.finditer(pattern, text, re.IGNORECASE):
            mentions.append((match.start(), author))
    return sorted(mentions)


def reference_identity_markers(entry: dict[str, str]) -> dict[str, set[str]]:
    """Return first-author given names and coauthor surnames for disambiguation.

    The bibliography format used by the manuscripts starts with
    ``Surname, Given, Given Surname, ... Year.``.  The markers are only used
    when two entries share the same first-author surname and year; they do not
    replace a semantic citation audit.
    """
    prefix = re.sub(
        rf"\s*{re.escape(entry['year'])}\.\s*$", "", entry["entry"]
    ).strip()
    chunks = [chunk.strip(" .") for chunk in prefix.split(",")]
    given_markers: set[str] = set()
    coauthor_markers: set[str] = set()
    if len(chunks) >= 2:
        for token in re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ'-]+", chunks[1]):
            if len(token) >= 2:
                given_markers.add(token.casefold())
    for chunk in chunks[2:]:
        tokens = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ'-]+", chunk)
        tokens = [token for token in tokens if token.casefold() not in {"and"}]
        if tokens:
            coauthor_markers.add(tokens[-1].casefold())
    given_markers.discard(entry["author"].casefold())
    coauthor_markers.discard(entry["author"].casefold())
    return {
        "given": given_markers,
        "coauthor": coauthor_markers,
        "all": given_markers | coauthor_markers,
    }


def disambiguate_same_author_year(
    body: str, grouped_entries: list[dict[str, str]]
) -> dict[str, object]:
    author = grouped_entries[0]["author"]
    year = grouped_entries[0]["year"]
    marker_roles = [reference_identity_markers(entry) for entry in grouped_entries]
    marker_counts = Counter(
        marker for roles in marker_roles for marker in roles["all"]
    )
    unique_given_markers = [
        sorted(marker for marker in roles["given"] if marker_counts[marker] == 1)
        for roles in marker_roles
    ]
    unique_post_surname_markers = [
        sorted(marker for marker in roles["all"] if marker_counts[marker] == 1)
        for roles in marker_roles
    ]

    mentions: list[dict[str, object]] = []
    mention_pattern = re.compile(
        rf"(?<![A-Za-z]){re.escape(author)}(?![A-Za-z])[^。！？\n]{{0,180}}?{year}",
        re.IGNORECASE | re.DOTALL,
    )
    for match in mention_pattern.finditer(body):
        prefix_window = body[max(0, match.start() - 48) : match.start()]
        immediate_name_match = re.search(
            r"([A-Za-zÀ-ÖØ-öø-ÿ'-]+(?:\s+[A-Za-zÀ-ÖØ-öø-ÿ'-]+){0,2})\s*$",
            prefix_window,
        )
        immediate_prefix = immediate_name_match.group(1) if immediate_name_match else ""
        post_surname_atom = match.group(0)
        normalized_prefix = immediate_prefix.casefold()
        normalized_post = post_surname_atom.casefold()
        matched_indices = []
        for index in range(len(grouped_entries)):
            given_match = any(
                re.search(
                    rf"(?<![A-Za-z]){re.escape(marker)}(?![A-Za-z])",
                    normalized_prefix,
                )
                for marker in unique_given_markers[index]
            )
            post_match = any(
                re.search(
                    rf"(?<![A-Za-z]){re.escape(marker)}(?![A-Za-z])",
                    normalized_post,
                )
                for marker in unique_post_surname_markers[index]
            )
            if given_match or post_match:
                matched_indices.append(index)

        start = max(0, match.start() - 48)
        end = min(len(body), match.end() + 20)
        context = body[start:end]
        mentions.append(
            {
                "line": body.count("\n", 0, match.start()) + 1,
                "context": " ".join(context.split()),
                "matched_entry_indices": matched_indices,
                "resolution": "resolved" if len(matched_indices) == 1 else "unresolved",
            }
        )

    resolved_entry_indices = sorted(
        {
            int(mention["matched_entry_indices"][0])
            for mention in mentions
            if mention["resolution"] == "resolved"
        }
    )
    unresolved_mentions = [
        mention for mention in mentions if mention["resolution"] != "resolved"
    ]
    entry_records = []
    for index, entry in enumerate(grouped_entries):
        entry_records.append(
            {
                "entry_index": index,
                "reference_prefix": entry["entry"],
                "unique_given_markers_before_surname": unique_given_markers[index],
                "unique_markers_after_surname": unique_post_surname_markers[index],
                "resolved_in_body": index in resolved_entry_indices,
            }
        )
    return {
        "author": author,
        "year": year,
        "entries": entry_records,
        "mentions": mentions,
        "unresolved_mentions": unresolved_mentions,
        "resolution_status": (
            "resolved"
            if len(resolved_entry_indices) == len(grouped_entries)
            and not unresolved_mentions
            else "manual_review_required"
        ),
    }


def inspect(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    body, references = split_body_and_references(text)
    entries = reference_entries(references)
    authors = sorted({entry["author"] for entry in entries}, key=len, reverse=True)
    keys = {(entry["author"].casefold(), entry["year"]) for entry in entries}

    entries_by_key: dict[tuple[str, str], list[dict[str, str]]] = {}
    for entry in entries:
        entries_by_key.setdefault(
            (entry["author"].casefold(), entry["year"]), []
        ).append(entry)
    ambiguous_reference_resolution = [
        disambiguate_same_author_year(body, grouped_entries)
        for grouped_entries in entries_by_key.values()
        if len(grouped_entries) > 1
    ]
    resolved_ambiguous_prefixes = {
        entry_record["reference_prefix"]
        for resolution in ambiguous_reference_resolution
        for entry_record in resolution["entries"]
        if entry_record["resolved_in_body"]
    }

    orphan_references: list[dict[str, str]] = []
    for entry in entries:
        key = (entry["author"].casefold(), entry["year"])
        if len(entries_by_key[key]) > 1:
            if entry["entry"] not in resolved_ambiguous_prefixes:
                orphan_references.append(entry)
            continue
        pattern = re.compile(
            re.escape(entry["author"]) + r".{0,160}?" + entry["year"],
            re.IGNORECASE | re.DOTALL,
        )
        if not pattern.search(body):
            orphan_references.append(entry)

    missing_reference_candidates: list[dict[str, object]] = []
    unresolved_citation_groups: list[dict[str, object]] = []
    for match in CITATION_GROUP_RE.finditer(body):
        group = match.group("group")
        external = body[max(0, match.start() - 140) : match.start()]
        sentence_start = max(
            external.rfind("。"),
            external.rfind("！"),
            external.rfind("？"),
            external.rfind(";"),
            external.rfind("；"),
            external.rfind("，"),
            external.rfind(")"),
            external.rfind("）"),
            external.rfind("|"),
            external.rfind("\n"),
        )
        external_clause = external[sentence_start + 1 :]
        external_mentions = author_mentions(external_clause, authors)
        current_author = external_mentions[0][1] if external_mentions else None
        previous_year_end = 0
        resolved_any = False
        for year_match in YEAR_RE.finditer(group):
            source_segment = group[previous_year_end : year_match.start()]
            segment_mentions = author_mentions(source_segment, authors)
            if segment_mentions:
                current_author = segment_mentions[0][1]
                resolved_any = True
            if current_author is None:
                previous_year_end = year_match.end()
                continue
            key = (current_author.casefold(), year_match.group(0))
            if key not in keys:
                missing_reference_candidates.append(
                    {
                        "author": current_author,
                        "year": year_match.group(0),
                        "group": group,
                        "line": body.count("\n", 0, match.start()) + 1,
                    }
                )
            previous_year_end = year_match.end()
        if not resolved_any and not external_mentions:
            unresolved_citation_groups.append(
                {
                    "group": group,
                    "line": body.count("\n", 0, match.start()) + 1,
                }
            )

    key_counts = Counter((entry["author"].casefold(), entry["year"]) for entry in entries)
    ambiguous_reference_keys = [
        {"author": author, "year": year, "count": count}
        for (author, year), count in sorted(key_counts.items())
        if count > 1
    ]
    unresolved_ambiguous_reference_mentions = [
        {
            "author": resolution["author"],
            "year": resolution["year"],
            "mentions": resolution["unresolved_mentions"],
        }
        for resolution in ambiguous_reference_resolution
        if resolution["unresolved_mentions"]
    ]
    mechanical_reference_identity_pass = not (
        orphan_references
        or missing_reference_candidates
        or unresolved_citation_groups
        or unresolved_ambiguous_reference_mentions
        or any(
            resolution["resolution_status"] != "resolved"
            for resolution in ambiguous_reference_resolution
        )
    )
    return {
        "path": str(path),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "reference_entries": len(entries),
        "orphan_references": orphan_references,
        "missing_reference_candidates": missing_reference_candidates,
        "unresolved_citation_groups": unresolved_citation_groups,
        "ambiguous_reference_keys": ambiguous_reference_keys,
        "ambiguous_reference_resolution": ambiguous_reference_resolution,
        "unresolved_ambiguous_reference_mentions": unresolved_ambiguous_reference_mentions,
        "mechanical_reference_identity_pass": mechanical_reference_identity_pass,
        "interpretation_note": (
            "Unique first-author-year keys use surname-year matching. Same-author same-year "
            "entries require a unique given-name or coauthor marker in each body mention; "
            "unresolved identity is a mechanical blocker. Semantic support still requires "
            "direct original-source review."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscripts", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "audit_script": str(Path(__file__).resolve()),
        "audit_script_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "manuscripts": [inspect(path) for path in args.manuscripts],
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
