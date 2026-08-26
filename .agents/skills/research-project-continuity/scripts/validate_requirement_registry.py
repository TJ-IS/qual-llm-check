#!/usr/bin/env python3
"""Validate the public requirement registry against its private baseline audit."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path


CONTROL_RE = re.compile(r"^[MSC]-[A-Z]+-\d{2}$")
ATOM_RE = re.compile(r"^[HLA]\d{2}$")
POST_ATOM_RE = re.compile(r"^P\d{2}$")
BACKTICK_RE = re.compile(r"`([^`]+)`")
UUID_RE = re.compile(
    r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
)

BASELINE_IDS = {
    *(f"H{i:02d}" for i in range(1, 21)),
    *(f"L{i:02d}" for i in range(1, 34)),
    *(f"A{i:02d}" for i in range(1, 6)),
}
BASELINE_VERDICT_GROUPS = {
    "core_direct": {
        "H04", "H07", "H09", "H14", "H15", "H16", "H17", "H18", "H20",
        "L02", "L05", "L07", "L08", "L10", "L11", "L14", "L15", "L16",
        "L17", "L18", "L19", "L20", "L21", "L23", "L25", "L28",
        "A01", "A02", "A04", "A05",
    },
    "routed_ledger": {"H03", "L13", "L22", "L24", "L27", "L30"},
    "partial": {
        "H01", "H02", "H05", "H06", "H08", "H13", "H19",
        "L01", "L03", "L04", "L06", "L09", "L12", "L29", "L31", "L33",
        "A03",
    },
    "missing": {"H10", "L32"},
    "superseded": {"H11", "H12"},
    "qualified_conflict": {"L26"},
}
BASELINE_VERDICT_BY_ID = {
    atom: verdict
    for verdict, atoms in BASELINE_VERDICT_GROUPS.items()
    for atom in atoms
}
BASELINE_COUNTS = {
    verdict: len(atoms) for verdict, atoms in BASELINE_VERDICT_GROUPS.items()
}
# SHA256 of sorted ``ID=verdict`` lines with no trailing newline.
BASELINE_PAYLOAD_SHA256 = "475c173eb6bc82d463c8e6c9971eec1fca2b69f5d8db5e6c54f43d99a6a55f99"
CONTROL_STATUSES = {"active", "qualified", "run_specific", "superseded", "open", "conflict"}
DISPOSITIONS = CONTROL_STATUSES
SCOPES = {"universal", "run_specific", "paper_specific"}
KNOWN_CONSUMERS = {
    "coding-agent-manuscript",
    "ais-fulltext-screening",
    "research-project-continuity",
}
LOAD_POLICIES = {
    "every checkpoint",
    "every writing checkpoint",
    "when benchmark/evaluation is in scope",
    "when delegating",
    "final integration checkpoint",
    "resume/version/acceptance work",
    "every run",
    "systematic retrieval",
    "every expensive run",
    "public-data gate",
    "every full-text run",
    "run closure and manuscript adoption",
    "every continuity task",
    "durable correction or skill revision",
    "whenever contrary rules are found",
    "curation/publication work",
    "skill/script revision or cross-platform handoff",
}
EXPECTED_CONTROL_BY_ATOM = {
    "L24": "M-PUNCT-01",
    "L26": "M-ANCHOR-01",
}
EXPECTED_POST_ATOMS = {
    "P01": (["C-CONFLICT-01"], "active", "universal"),
    "P02": (["M-LEDGER-01", "M-TEMPLATE-01"], "active", "universal"),
    "P03": (["C-PORTABLE-01"], "active", "universal"),
}


def table_rows(lines: list[str], header_start: str) -> list[list[str]]:
    try:
        start = next(i for i, line in enumerate(lines) if line.startswith(header_start))
    except StopIteration:
        return []

    rows: list[list[str]] = []
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def clean_code(value: str) -> str:
    return value.strip().strip("`")


def is_iso_date(value: str) -> bool:
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def operative_markdown(text: str) -> str:
    """Remove comments and fenced examples before checking executable instructions."""
    without_comments = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return re.sub(r"```.*?```", "", without_comments, flags=re.DOTALL)


def baseline_payload(verdict_by_id: dict[str, str]) -> str:
    return "\n".join(f"{atom}={verdict_by_id[atom]}" for atom in sorted(verdict_by_id))


def private_verdicts(text: str) -> dict[str, str]:
    labels = {
        "核心直接覆盖": "core_direct",
        "路由台账覆盖": "routed_ledger",
        "部分覆盖": "partial",
        "未写入 skill": "missing",
        "被后续要求替代": "superseded",
        "后续限定且存在内部冲突": "qualified_conflict",
        "后续限定且内部冲突": "qualified_conflict",
    }
    found: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^\|\s*`?(H\d{2}|L\d{2}|A\d{2})`?\s*\|", line)
        if not match:
            continue
        matches = [verdict for label, verdict in labels.items() if label in line]
        if len(matches) == 1:
            found[match.group(1)] = matches[0]
    return found


def private_quote_cells(text: str) -> list[tuple[str, str]]:
    quotes: list[tuple[str, str]] = []
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not re.fullmatch(r"[HLA]\d{2}", clean_code(cells[0])):
            continue
        atom = clean_code(cells[0])
        for quote in re.findall(r"“([^”]+)”", cells[1]):
            normalized = re.sub(r"[^\w\u4e00-\u9fff]", "", quote)
            if len(normalized) >= 20:
                quotes.append((atom, normalized))
    return quotes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-no-conflicts", action="store_true")
    parser.add_argument(
        "--require-private-audit",
        action="store_true",
        help="maintainer check for ignored local provenance artifacts",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[4]
    registry = repo / "docs/research_program/requirement_registry.md"
    private_audit = repo / (
        "runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/"
        "research_reviews/v11_iterative_literature_rewrite/audit_artifacts/"
        "2026-08-26_history_original_to_skill_traceability_audit.md"
    )
    private_post_revision = repo / (
        "runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/"
        "research_reviews/v11_iterative_literature_rewrite/audit_artifacts/"
        "2026-08-26_history_original_to_skill_traceability_post_revision_checkpoint.md"
    )
    private_final_revision = repo / (
        "runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/"
        "research_reviews/v11_iterative_literature_rewrite/audit_artifacts/"
        "2026-08-26_history_original_to_skill_traceability_final.md"
    )

    errors: list[str] = []
    warnings: list[str] = []
    if set(BASELINE_VERDICT_BY_ID) != BASELINE_IDS:
        errors.append("validator baseline map does not cover the frozen 58 atoms exactly")
    payload_hash = hashlib.sha256(baseline_payload(BASELINE_VERDICT_BY_ID).encode("utf-8")).hexdigest()
    if payload_hash != BASELINE_PAYLOAD_SHA256:
        errors.append(
            "validator baseline map hash differs from the frozen public checksum: "
            f"{payload_hash}"
        )
    if not registry.is_file():
        print(f"ERROR missing registry: {registry}")
        return 1

    text = registry.read_text(encoding="utf-8")
    lines = text.splitlines()

    private_patterns = {
        "message identifier": re.compile(r"\bmsg_", re.IGNORECASE),
        "session path": re.compile(r"\.codex[/\\]sessions", re.IGNORECASE),
        "JSONL locator": re.compile(r"JSONL\s+L\d+", re.IGNORECASE),
        "task or conversation identifier": re.compile(
            r"\b(?:message|task|thread|turn|session|client|rollout)[_ -]?id\s*[:=]",
            re.IGNORECASE,
        ),
        "private quotation marker": re.compile(r"原话|verbatim\s+quote|exact\s+quote", re.IGNORECASE),
        "curly quotation": re.compile(r"[“”]"),
        "UUID": UUID_RE,
    }
    for label, pattern in private_patterns.items():
        if pattern.search(text):
            errors.append(f"public registry contains {label}")

    controls = table_rows(lines, "| Control ID |")
    if not controls:
        errors.append("current-controls table is missing")
        controls = []

    control_ids: list[str] = []
    control_status_by_id: dict[str, str] = {}
    for row in controls:
        if len(row) != 7:
            errors.append(f"control row has {len(row)} columns")
            continue
        control_id, _domain, _requirement, clause, consumer, load_policy, status = row
        control_id = clean_code(control_id)
        control_ids.append(control_id)
        control_status_by_id[control_id] = status
        if not CONTROL_RE.fullmatch(control_id):
            errors.append(f"invalid control id: {control_id}")
        if status not in CONTROL_STATUSES:
            errors.append(f"invalid control status for {control_id}: {status}")
        consumers = BACKTICK_RE.findall(consumer)
        consumer_remainder = BACKTICK_RE.sub("", consumer).replace(",", "").strip()
        if not consumers or consumer_remainder:
            errors.append(f"invalid consumer syntax for {control_id}: {consumer}")
        unknown_consumers = sorted(set(consumers) - KNOWN_CONSUMERS)
        if unknown_consumers:
            errors.append(f"unknown consumers for {control_id}: {','.join(unknown_consumers)}")
        if load_policy not in LOAD_POLICIES:
            errors.append(f"unknown load policy for {control_id}: {load_policy}")

        tokens = BACKTICK_RE.findall(clause)
        paths = [token for token in tokens if token.endswith(".md")]
        anchors = [token for token in tokens if not token.endswith(".md")]
        if not paths:
            errors.append(f"no repository-relative Markdown pointer for {control_id}")
            continue
        source_texts: list[str] = []
        for path_text in paths:
            target = (repo / path_text).resolve()
            try:
                target.relative_to(repo.resolve())
            except ValueError:
                errors.append(f"pointer escapes repository for {control_id}: {path_text}")
                continue
            if not target.is_file():
                errors.append(f"unresolved path for {control_id}: {path_text}")
            else:
                source_texts.append(target.read_text(encoding="utf-8"))
        for anchor in anchors:
            heading = re.compile(rf"^#+\s+{re.escape(anchor)}\s*$", re.MULTILINE)
            if source_texts and not any(heading.search(source) for source in source_texts):
                errors.append(f"unresolved heading for {control_id}: {anchor}")

    duplicates = [item for item, count in Counter(control_ids).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate control ids: {','.join(sorted(duplicates))}")
    control_set = set(control_ids)

    history = table_rows(lines, "| Atom | 2026-08-26 baseline verdict |")
    history_ids: list[str] = []
    verdicts: Counter[str] = Counter()
    conflicts: list[str] = []
    mapped_by_atom: dict[str, list[str]] = {}
    disposition_by_atom: dict[str, str] = {}
    for row in history:
        if len(row) != 8:
            errors.append(f"historical row has {len(row)} columns")
            continue
        atom, verdict, current_controls, disposition, scope, edge, last_verified, _meaning = row
        atom = clean_code(atom)
        history_ids.append(atom)
        verdicts[verdict] += 1
        disposition_by_atom[atom] = disposition
        if not ATOM_RE.fullmatch(atom):
            errors.append(f"invalid baseline atom: {atom}")
        expected_verdict = BASELINE_VERDICT_BY_ID.get(atom)
        if expected_verdict is not None and verdict != expected_verdict:
            errors.append(
                f"baseline verdict mismatch for {atom}: expected {expected_verdict}, found {verdict}"
            )
        if disposition not in DISPOSITIONS:
            errors.append(f"invalid disposition for {atom}: {disposition}")
        if scope not in SCOPES:
            errors.append(f"invalid scope for {atom}: {scope}")
        if not is_iso_date(last_verified):
            errors.append(f"invalid last-verified date for {atom}: {last_verified}")
        mapped = [token for token in BACKTICK_RE.findall(current_controls) if CONTROL_RE.fullmatch(token)]
        mapped_by_atom[atom] = mapped
        if not mapped:
            errors.append(f"no current control for {atom}")
        for control_id in mapped:
            if control_id not in control_set:
                errors.append(f"unknown control {control_id} referenced by {atom}")
        if disposition in {"qualified", "run_specific", "superseded", "conflict"} and edge == "—":
            errors.append(f"missing qualification/replacement edge for {atom}")
        if disposition == "conflict":
            conflicts.append(atom)
            if not any(control_status_by_id.get(control_id) == "conflict" for control_id in mapped):
                errors.append(f"conflict atom {atom} does not map to a conflict control")
        elif mapped and not any(
            control_status_by_id.get(control_id) in CONTROL_STATUSES - {"conflict", "open"}
            for control_id in mapped
        ):
            errors.append(f"non-conflict atom {atom} has no executable current control")

    if set(history_ids) != BASELINE_IDS:
        missing = sorted(BASELINE_IDS - set(history_ids))
        extra = sorted(set(history_ids) - BASELINE_IDS)
        errors.append(f"baseline atom mismatch missing={missing} extra={extra}")
    if len(history_ids) != len(set(history_ids)):
        errors.append("duplicate baseline atom ids")
    if dict(verdicts) != BASELINE_COUNTS:
        errors.append(f"baseline verdict counts mismatch: {dict(verdicts)}")

    conflict_control_ids = {
        control_id for control_id, status in control_status_by_id.items() if status == "conflict"
    }
    conflict_atom_controls = {
        control_id
        for atom in conflicts
        for control_id in mapped_by_atom.get(atom, [])
        if control_status_by_id.get(control_id) == "conflict"
    }
    orphan_conflict_controls = sorted(conflict_control_ids - conflict_atom_controls)
    if orphan_conflict_controls:
        errors.append(f"conflict controls lack conflict atoms: {','.join(orphan_conflict_controls)}")
    for atom, expected_control in EXPECTED_CONTROL_BY_ATOM.items():
        if expected_control not in mapped_by_atom.get(atom, []):
            errors.append(f"{atom} must map to {expected_control}")
        if (
            disposition_by_atom.get(atom) == "conflict"
            and control_status_by_id.get(expected_control) != "conflict"
        ):
            errors.append(f"{expected_control} must remain conflict while {atom} is unresolved")

    post = table_rows(lines, "| Atom | Added |")
    post_ids: list[str] = []
    post_mapped: dict[str, list[str]] = {}
    post_dispositions: dict[str, str] = {}
    post_scopes: dict[str, str] = {}
    for row in post:
        if len(row) != 6:
            errors.append(f"post-baseline row has {len(row)} columns")
            continue
        atom, added, current_controls, disposition, scope, _meaning = row
        atom = clean_code(atom)
        post_ids.append(atom)
        post_dispositions[atom] = disposition
        post_scopes[atom] = scope
        if not POST_ATOM_RE.fullmatch(atom):
            errors.append(f"invalid post-baseline atom: {atom}")
        if atom in BASELINE_IDS:
            errors.append(f"post-baseline atom overlaps frozen baseline: {atom}")
        if not is_iso_date(added):
            errors.append(f"invalid added date for {atom}: {added}")
        if disposition not in DISPOSITIONS:
            errors.append(f"invalid post-baseline disposition for {atom}: {disposition}")
        if scope not in SCOPES:
            errors.append(f"invalid post-baseline scope for {atom}: {scope}")
        mapped = [token for token in BACKTICK_RE.findall(current_controls) if CONTROL_RE.fullmatch(token)]
        post_mapped[atom] = mapped
        if not mapped:
            errors.append(f"no current control for post-baseline atom {atom}")
        for control_id in mapped:
            if control_id not in control_set:
                errors.append(f"unknown control {control_id} referenced by {atom}")

    duplicate_post = [item for item, count in Counter(post_ids).items() if count > 1]
    if duplicate_post:
        errors.append(f"duplicate post-baseline atom ids: {','.join(sorted(duplicate_post))}")
    for atom, (expected_controls, expected_disposition, expected_scope) in EXPECTED_POST_ATOMS.items():
        if post_ids.count(atom) != 1:
            errors.append(f"post-baseline atom {atom} must appear exactly once")
        if post_mapped.get(atom) != expected_controls:
            errors.append(f"{atom} must map exactly to {','.join(expected_controls)}")
        if (
            post_dispositions.get(atom) != expected_disposition
            or post_scopes.get(atom) != expected_scope
        ):
            errors.append(
                f"{atom} must remain {expected_disposition} and {expected_scope}"
            )
    if control_status_by_id.get("C-CONFLICT-01") != "active":
        errors.append("C-CONFLICT-01 must be an active current control")
    if control_status_by_id.get("C-PORTABLE-01") != "active":
        errors.append("C-PORTABLE-01 must be an active current control")

    for skill_path in (
        ".agents/skills/coding-agent-manuscript/SKILL.md",
        ".agents/skills/ais-fulltext-screening/SKILL.md",
        ".agents/skills/research-project-continuity/SKILL.md",
    ):
        skill_text = operative_markdown((repo / skill_path).read_text(encoding="utf-8"))
        load_instruction = re.search(
            r"(?im)^\s*(?:\d+\.\s*)?Read\b[^\n]*requirement_registry\.md",
            skill_text,
        )
        if not load_instruction:
            errors.append(f"skill does not operatively load registry: {skill_path}")
        if not (
            re.search(r"\bconflict\b", skill_text, flags=re.IGNORECASE)
            and re.search(r"\buser\b", skill_text, flags=re.IGNORECASE)
            and re.search(r"confirm", skill_text, flags=re.IGNORECASE)
        ):
            errors.append(f"skill lacks operative user-confirmation conflict gate: {skill_path}")

    if args.require_private_audit:
        for private_path in (private_audit, private_post_revision, private_final_revision):
            if not private_path.is_file():
                errors.append(f"private traceability artifact is missing: {private_path.name}")
                continue
            private_rel = str(private_path.relative_to(repo))
            ignored = subprocess.run(
                ["git", "check-ignore", "-q", private_rel],
                cwd=repo,
                check=False,
            ).returncode == 0
            if not ignored:
                errors.append(f"private traceability artifact is not ignored: {private_path.name}")
            tracked = subprocess.run(
                ["git", "ls-files", "--error-unmatch", private_rel],
                cwd=repo,
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode == 0
            if tracked:
                errors.append(f"private traceability artifact is tracked: {private_path.name}")
            staged = subprocess.run(
                ["git", "diff", "--cached", "--quiet", "--", private_rel],
                cwd=repo,
                check=False,
            ).returncode != 0
            if staged:
                errors.append(f"private traceability artifact is staged: {private_path.name}")

        if private_audit.is_file():
            private_text = private_audit.read_text(encoding="utf-8")
            private_map = private_verdicts(private_text)
            if set(private_map) != BASELINE_IDS:
                missing = sorted(BASELINE_IDS - set(private_map))
                extra = sorted(set(private_map) - BASELINE_IDS)
                errors.append(f"private baseline verdict map differs missing={missing} extra={extra}")
            for atom in sorted(BASELINE_IDS & set(private_map)):
                if private_map[atom] != BASELINE_VERDICT_BY_ID[atom]:
                    errors.append(
                        f"private/public baseline verdict differs for {atom}: "
                        f"{private_map[atom]} != {BASELINE_VERDICT_BY_ID[atom]}"
                    )
            normalized_public = re.sub(r"[^\w\u4e00-\u9fff]", "", text)
            quote_records = private_quote_cells(private_text)
            if private_post_revision.is_file():
                post_private_text = private_post_revision.read_text(encoding="utf-8")
                for quote in re.findall(r"“([^”]+)”", post_private_text):
                    normalized = re.sub(r"[^\w\u4e00-\u9fff]", "", quote)
                    if len(normalized) >= 20:
                        quote_records.append(("P01", normalized))
            if private_final_revision.is_file():
                final_private_text = private_final_revision.read_text(encoding="utf-8")
                for atom, quote in re.findall(
                    r"\b(L24|L26|P02|P03)\b[^\n]*“([^”]+)”", final_private_text
                ):
                    normalized = re.sub(r"[^\w\u4e00-\u9fff]", "", quote)
                    if len(normalized) >= 20:
                        quote_records.append((atom, normalized))
            leaked_atoms = {
                atom
                for atom, quote in quote_records
                if any(quote[index : index + 20] in normalized_public for index in range(len(quote) - 19))
            }
            if leaked_atoms:
                errors.append(
                    "public registry overlaps private quotations for atoms: "
                    + ",".join(sorted(leaked_atoms))
                )

        if private_post_revision.is_file():
            private_post_text = private_post_revision.read_text(encoding="utf-8")
            if not re.search(r"post-baseline atom\s+`P01`", private_post_text):
                errors.append("post-baseline atom P01 is absent from the private post-revision audit")
            if not re.search(r"P01.*C-CONFLICT-01", private_post_text, flags=re.DOTALL):
                errors.append("private post-revision audit does not map P01 to C-CONFLICT-01")
            if not re.search(r"P01.*(?:provenance|来源|出处)", private_post_text, flags=re.DOTALL):
                errors.append("private post-revision audit lacks P01 provenance")

        if private_final_revision.is_file():
            private_final_text = private_final_revision.read_text(encoding="utf-8")
            if not re.search(r"L24.*M-PUNCT-01.*superseded", private_final_text, flags=re.DOTALL):
                errors.append("private final audit does not resolve L24/M-PUNCT-01 as superseded")
            if not re.search(r"L26.*M-ANCHOR-01.*qualified", private_final_text, flags=re.DOTALL):
                errors.append("private final audit does not resolve L26/M-ANCHOR-01 as qualified")
            if not re.search(r"L24.*(?:provenance|来源|出处)", private_final_text, flags=re.DOTALL):
                errors.append("private final audit lacks L24 provenance")
            if not re.search(r"L26.*(?:provenance|来源|出处)", private_final_text, flags=re.DOTALL):
                errors.append("private final audit lacks L26 provenance")
            if not re.search(
                r"P02.*M-LEDGER-01.*M-TEMPLATE-01.*active",
                private_final_text,
                flags=re.DOTALL,
            ):
                errors.append("private final audit does not map active P02 to the two-pool controls")
            if not re.search(
                r"P03.*C-PORTABLE-01.*active", private_final_text, flags=re.DOTALL
            ):
                errors.append("private final audit does not map active P03 to C-PORTABLE-01")
            for atom in ("P02", "P03"):
                if not re.search(
                    rf"{atom}.*(?:provenance|来源|出处)", private_final_text, flags=re.DOTALL
                ):
                    errors.append(f"private final audit lacks {atom} provenance")

    if conflicts:
        warnings.append(f"unresolved conflicts requiring user confirmation: {','.join(conflicts)}")
        if args.require_no_conflicts:
            errors.append("registry still contains unresolved conflicts")

    print(f"controls={len(control_set)} baseline_atoms={len(set(history_ids))} post_baseline_atoms={len(post_ids)}")
    print("baseline_verdicts=" + ",".join(f"{key}:{verdicts[key]}" for key in sorted(verdicts)))
    print("private_audit=" + ("checked" if args.require_private_audit else "not_requested"))
    for warning in warnings:
        print(f"WARNING {warning}")
    for error in errors:
        print(f"ERROR {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
