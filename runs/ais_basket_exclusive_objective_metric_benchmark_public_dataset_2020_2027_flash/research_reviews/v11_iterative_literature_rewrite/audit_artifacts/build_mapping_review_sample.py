from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import math
import re
from collections import defaultdict
from pathlib import Path

from audit_sentence_mapping import parse_blocks


LINE_RANGE_RE = re.compile(r"^(\d+)(?:-(\d+))?$")


def numbered_line_window(path: Path, line_range: str | None) -> dict[str, object]:
    if not line_range:
        return {"resolved_path": str(path), "error": "missing_line_range", "lines": []}
    match = LINE_RANGE_RE.fullmatch(line_range.strip())
    if not match:
        return {"resolved_path": str(path), "error": "invalid_line_range", "lines": []}
    start = int(match.group(1))
    end = int(match.group(2) or match.group(1))
    if not path.is_file():
        return {"resolved_path": str(path), "error": "missing_authority_file", "lines": []}
    source_lines = path.read_text(encoding="utf-8-sig").splitlines()
    if start < 1 or end < start or end > len(source_lines):
        return {"resolved_path": str(path), "error": "line_range_out_of_bounds", "lines": []}
    return {
        "resolved_path": str(path),
        "error": None,
        "lines": [
            {"line": line_no, "text": source_lines[line_no - 1]}
            for line_no in range(start, end + 1)
        ],
    }


def add_pick(
    selected: dict[str, set[str]],
    selection_order: list[str],
    target_id: str,
    reason: str,
) -> None:
    if target_id not in selected:
        selected[target_id] = set()
        selection_order.append(target_id)
    selected[target_id].add(reason)


def middle_id(target_ids: list[str]) -> str:
    return target_ids[(len(target_ids) - 1) // 2]


def build_sample(
    inventory_path: Path,
    mapping_path: Path,
    minimum: int,
    fraction: float,
    repo_root: Path,
) -> dict[str, object]:
    inventory_bytes = inventory_path.read_bytes()
    mapping_bytes = mapping_path.read_bytes()
    inventory = json.loads(inventory_bytes.decode("utf-8-sig"))
    mapping_text = mapping_bytes.decode("utf-8-sig")
    blocks, duplicates = parse_blocks(mapping_text)
    units = sorted(inventory["units"], key=lambda item: item["target_id"])
    expected_count = len(units)
    sample_count = min(
        expected_count, max(minimum, math.ceil(expected_count * fraction))
    )

    by_section: dict[str, list[str]] = defaultdict(list)
    by_type: dict[str, list[str]] = defaultdict(list)
    by_status: dict[str, list[str]] = defaultdict(list)
    selected: dict[str, set[str]] = {}
    selection_order: list[str] = []

    for unit in units:
        target_id = unit["target_id"]
        by_section[str(unit.get("section", ""))].append(target_id)
        by_type[str(unit.get("type", ""))].append(target_id)
        by_status[blocks.get(target_id, {}).get("status", "missing")].append(
            target_id
        )

    for section, target_ids in sorted(by_section.items()):
        add_pick(
            selected,
            selection_order,
            middle_id(target_ids),
            f"section:{section}",
        )
    for unit_type, target_ids in sorted(by_type.items()):
        add_pick(
            selected,
            selection_order,
            middle_id(target_ids),
            f"type:{unit_type}",
        )
    for status, target_ids in sorted(by_status.items()):
        add_pick(
            selected,
            selection_order,
            middle_id(target_ids),
            f"status:{status}",
        )

    pending_ids = [
        unit["target_id"]
        for unit in units
        if "[[待补文献" in str(unit.get("target_sentence", ""))
    ]
    if pending_ids:
        add_pick(
            selected,
            selection_order,
            middle_id(pending_ids),
            "inline_placeholder",
        )

    if sample_count > 1:
        for index in range(sample_count):
            if len(selected) >= sample_count:
                break
            position = round(index * (expected_count - 1) / (sample_count - 1))
            add_pick(
                selected,
                selection_order,
                units[position]["target_id"],
                "even_spacing",
            )

    for unit in units:
        if len(selected) >= sample_count:
            break
        add_pick(
            selected,
            selection_order,
            unit["target_id"],
            "fill",
        )

    selected_ids = sorted(selection_order[:sample_count])
    unit_by_id = {unit["target_id"]: unit for unit in units}
    units_by_paragraph: dict[str, list[dict[str, object]]] = defaultdict(list)
    for unit in units:
        units_by_paragraph[str(unit.get("paragraph_id", ""))].append(unit)
    sample: list[dict[str, object]] = []
    for target_id in selected_ids:
        unit = unit_by_id[target_id]
        fields = blocks.get(target_id, {})
        authority_path_text = fields.get("authority_path")
        authority_path = (
            repo_root / authority_path_text
            if authority_path_text
            else repo_root / "__missing_authority_path__"
        )
        target_context = [
            {
                "target_id": context_unit.get("target_id"),
                "type": context_unit.get("type"),
                "target_lines": context_unit.get("target_lines"),
                "target_sentence": context_unit.get("target_sentence"),
            }
            for context_unit in units_by_paragraph[str(unit.get("paragraph_id", ""))]
        ]
        sample.append(
            {
                "target_id": target_id,
                "selection_reasons": sorted(selected[target_id]),
                "section": unit.get("section"),
                "type": unit.get("type"),
                "target_lines": unit.get("target_lines"),
                "target_sentence": unit.get("target_sentence"),
                "target_paragraph_id": unit.get("paragraph_id"),
                "target_context_units": target_context,
                "status": fields.get("status"),
                "sentence_function": fields.get("sentence_function"),
                "authority_sentence": fields.get("authority_sentence"),
                "authority_source": fields.get("authority_source"),
                "authority_path": fields.get("authority_path"),
                "authority_section": fields.get("authority_section"),
                "authority_sentence_lines": fields.get(
                    "authority_sentence_lines"
                ),
                "authority_paragraph_lines": fields.get(
                    "authority_paragraph_lines"
                ),
                "authority_paragraph_window": numbered_line_window(
                    authority_path, fields.get("authority_paragraph_lines")
                ),
                "match_dimensions": fields.get("match_dimensions"),
                "citation_support": fields.get("citation_support"),
                "method_authority_sentence": fields.get(
                    "method_authority_sentence"
                ),
                "method_authority_source": fields.get("method_authority_source"),
                "method_authority_lines": fields.get("method_authority_lines"),
                "method_assumptions": fields.get("method_assumptions"),
                "is_disclosure_anchor": fields.get("is_disclosure_anchor"),
                "is_disclosure_window": fields.get("is_disclosure_window"),
                "review_target_predicate": None,
                "review_authority_argument_action": None,
                "review_target_predicate_signature": None,
                "review_authority_predicate_signature": None,
                "review_unit_role": None,
                "review_logic_direction": None,
                "review_paragraph_role": None,
                "review_mismatch_reason": None,
                "review_verdict": None,
                "review_note": None,
            }
        )

    return {
        "inventory": str(inventory_path),
        "mapping": str(mapping_path),
        "inventory_sha256": hashlib.sha256(inventory_bytes).hexdigest(),
        "mapping_sha256": hashlib.sha256(mapping_bytes).hexdigest(),
        "sample_builder": str(Path(__file__).resolve()),
        "sample_builder_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "manuscript_sha256": inventory["manuscript_sha256"],
        "generated_at_utc": datetime.datetime.now(
            datetime.timezone.utc
        ).isoformat(),
        "population_units": expected_count,
        "minimum": minimum,
        "fraction": fraction,
        "required_sample_count": sample_count,
        "actual_sample_count": len(sample),
        "duplicate_mapping_ids": duplicates,
        "sample": sample,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("inventory", type=Path)
    parser.add_argument("mapping", type=Path)
    parser.add_argument("--minimum", type=int, default=40)
    parser.add_argument("--fraction", type=float, default=0.05)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.minimum < 1:
        raise SystemExit("--minimum must be at least 1")
    if not 0 < args.fraction <= 1:
        raise SystemExit("--fraction must be in (0, 1]")
    result = build_sample(
        args.inventory,
        args.mapping,
        args.minimum,
        args.fraction,
        args.repo_root.resolve(),
    )
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
