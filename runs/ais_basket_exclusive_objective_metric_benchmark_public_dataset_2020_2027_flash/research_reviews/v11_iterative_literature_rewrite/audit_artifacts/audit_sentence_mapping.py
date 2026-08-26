from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path


BLOCK_RE = re.compile(
    r"^###\s+(P[123]-U\d{4})\s*$\n(.*?)(?=^###\s+P[123]-U\d{4}\s*$|\Z)",
    re.MULTILINE | re.DOTALL,
)
FIELD_RE = re.compile(r"^-\s+`([^`]+)`\s*:\s*(.*?)\s*$", re.MULTILINE)
LINE_RANGE_RE = re.compile(r"^(\d+)(?:-(\d+))?$")
REQUIRED_FIELDS = (
    "target_sha256",
    "target_lines",
    "target_sentence",
    "paragraph_task",
    "fine_grained_function",
    "sentence_function",
    "given_from_previous",
    "new_for_next",
    "authority_sentence",
    "authority_source",
    "authority_path",
    "authority_section",
    "authority_sentence_lines",
    "authority_paragraph_lines",
    "authority_paragraph_candidate_audit",
    "match_dimensions",
    "citation_responsibility",
    "citation_support",
    "transferable_skeleton",
    "nontransferable_boundary",
    "status",
    "revision",
    "source_fact",
    "author_operationalization",
    "writing_prototype",
    "table_role",
    "unit_role",
    "target_predicate_signature",
    "authority_predicate_signature",
    "method_authority_sentence",
    "method_authority_source",
    "method_authority_lines",
    "method_assumptions",
    "is_disclosure_anchor",
    "is_disclosure_window",
    "definition_node",
    "implementation_node",
    "direct_citation_edge",
    "author_adaptation",
    "method_source",
    "authority_application",
    "resampling_or_permutation_unit",
    "null_hypothesis",
    "exchangeability_or_cluster_condition",
    "pairing_structure",
    "effective_group_count",
    "estimand",
    "finite_sample_handling",
    "author_protocol_boundary",
)
MATCH_KEYS = ("主语角色", "句子功能", "逻辑关系", "段内位置")
PREDICATE_KEYS = ("主语类型", "算子", "宾语/结果", "限定", "时序")
MAX_AUTHORITY_ANCHOR_REUSE = 8


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def normalize(value: str) -> str:
    value = value.strip()
    value = value.replace("**", "")
    value = re.sub(r"\s+", " ", value)
    return value


def parse_range(value: str) -> tuple[int, int] | None:
    match = LINE_RANGE_RE.fullmatch(value.strip())
    if not match:
        return None
    start = int(match.group(1))
    end = int(match.group(2) or start)
    if start < 1 or end < start:
        return None
    return start, end


def parse_blocks(mapping_text: str) -> tuple[dict[str, dict[str, str]], list[str]]:
    blocks: dict[str, dict[str, str]] = {}
    duplicates: list[str] = []
    for match in BLOCK_RE.finditer(mapping_text):
        target_id = match.group(1)
        fields = {key: value for key, value in FIELD_RE.findall(match.group(2))}
        if target_id in blocks:
            duplicates.append(target_id)
        blocks[target_id] = fields
    return blocks, sorted(set(duplicates))


def authority_check(
    fields: dict[str, str], repo_root: Path
) -> tuple[bool, str | None]:
    authority_path = Path(fields.get("authority_path", ""))
    resolved = authority_path if authority_path.is_absolute() else repo_root / authority_path
    if not resolved.is_file():
        return False, f"authority_path_not_found:{resolved}"
    sentence_range = parse_range(fields.get("authority_sentence_lines", ""))
    paragraph_range = parse_range(fields.get("authority_paragraph_lines", ""))
    if sentence_range is None:
        return False, "invalid_authority_sentence_lines"
    if paragraph_range is None:
        return False, "invalid_authority_paragraph_lines"
    if not (
        paragraph_range[0] <= sentence_range[0]
        and sentence_range[1] <= paragraph_range[1]
    ):
        return False, "sentence_lines_outside_paragraph_lines"
    source_lines = resolved.read_text(encoding="utf-8-sig").splitlines()
    if sentence_range[1] > len(source_lines) or paragraph_range[1] > len(source_lines):
        return False, "authority_line_out_of_range"
    excerpt = " ".join(source_lines[sentence_range[0] - 1 : sentence_range[1]])
    sentence = fields.get("authority_sentence", "")
    if normalize(sentence) not in normalize(excerpt):
        return False, "authority_sentence_not_found_in_reported_lines"
    return True, None


def audit(inventory_path: Path, mapping_path: Path, repo_root: Path) -> dict[str, object]:
    inventory_bytes = inventory_path.read_bytes()
    mapping_bytes = mapping_path.read_bytes()
    inventory = json.loads(inventory_bytes.decode("utf-8-sig"))
    mapping_text = mapping_bytes.decode("utf-8-sig")
    inventory_sha256 = sha256_bytes(inventory_bytes)
    mapping_sha256 = sha256_bytes(mapping_bytes)
    validator_path = Path(__file__).resolve()
    validator_sha256 = sha256_file(validator_path)
    manuscript_path = Path(str(inventory.get("manuscript", "")))
    if not manuscript_path.is_absolute():
        manuscript_path = repo_root / manuscript_path
    binding_errors: list[str] = []
    manuscript_current_sha256: str | None = None
    if manuscript_path.is_file():
        manuscript_current_sha256 = sha256_file(manuscript_path)
        if manuscript_current_sha256.lower() != str(
            inventory.get("manuscript_sha256", "")
        ).lower():
            binding_errors.append("manuscript_sha256_mismatch_inventory")
    else:
        binding_errors.append(f"manuscript_path_not_found:{manuscript_path}")
    blocks, duplicates = parse_blocks(mapping_text)
    expected = {unit["target_id"]: unit for unit in inventory["units"]}
    missing = sorted(set(expected) - set(blocks))
    extra = sorted(set(blocks) - set(expected))
    findings: list[dict[str, object]] = []

    reuse_members: dict[tuple[str, str, str], list[str]] = {}
    for target_id in sorted(set(expected) & set(blocks)):
        fields = blocks[target_id]
        if fields.get("status", "") == "回修":
            continue
        reuse_key = (
            fields.get("authority_path", "").strip(),
            fields.get("authority_sentence_lines", "").strip(),
            normalize(fields.get("authority_sentence", "")),
        )
        reuse_members.setdefault(reuse_key, []).append(target_id)

    overused_keys = {
        key: target_ids
        for key, target_ids in reuse_members.items()
        if len(target_ids) > MAX_AUTHORITY_ANCHOR_REUSE
    }

    for target_id in sorted(set(expected) & set(blocks)):
        unit = expected[target_id]
        fields = blocks[target_id]
        errors: list[str] = []
        for field in REQUIRED_FIELDS:
            if not fields.get(field, "").strip():
                errors.append(f"missing_field:{field}")
        if fields.get("target_sha256") != unit["target_sha256"]:
            errors.append("target_sha256_mismatch")
        if fields.get("target_lines") != unit["target_lines"]:
            errors.append("target_lines_mismatch")
        if normalize(fields.get("target_sentence", "")) != normalize(
            str(unit["target_sentence"])
        ):
            errors.append("target_sentence_mismatch")
        status = fields.get("status", "")
        if status not in {"通过", "回修", "边界句", "待补文献"}:
            errors.append("invalid_status")
        dimensions = fields.get("match_dimensions", "")
        for key in MATCH_KEYS:
            if key not in dimensions:
                errors.append(f"missing_match_dimension:{key}")
        if "；；" in dimensions or ";;" in dimensions:
            errors.append("duplicated_match_dimension_delimiter")
        if status in {"通过", "边界句"}:
            dimension_values: dict[str, str] = {}
            for key in MATCH_KEYS:
                value_match = re.search(
                    rf"(?:^|[；;])\s*{re.escape(key)}\s*=\s*(一致|部分一致|不一致)\s*(?=[；;]|$)",
                    dimensions,
                )
                if value_match:
                    dimension_values[key] = value_match.group(1)
            agreement_count = sum(
                value == "一致" for value in dimension_values.values()
            )
            if agreement_count < 3:
                errors.append("fewer_than_three_consistent_dimensions")
            if status == "通过" and any(
                dimension_values.get(key) != "一致" for key in MATCH_KEYS
            ):
                errors.append("pass_has_nonexact_match_dimension")
            if status == "通过" and any(
                marker in dimensions
                for marker in (
                    "不能判为通过",
                    "至少一项未同构",
                    "存在不一致",
                    "部分共享",
                )
            ):
                errors.append("pass_match_rationale_contains_rejection")
            for signature_field in (
                "target_predicate_signature",
                "authority_predicate_signature",
            ):
                signature = fields.get(signature_field, "")
                for key in PREDICATE_KEYS:
                    if f"{key}=" not in signature:
                        errors.append(
                            f"missing_predicate_component:{signature_field}:{key}"
                        )
            paragraph_audit = fields.get(
                "authority_paragraph_candidate_audit", ""
            )
            paragraph_lines = fields.get("authority_paragraph_lines", "").strip()
            audited_all_sentences = (
                "逐句" in paragraph_audit or "全部句子" in paragraph_audit
            )
            if not audited_all_sentences or paragraph_lines not in paragraph_audit:
                errors.append("incomplete_authority_paragraph_candidate_audit")
            nontransferable = normalize(
                fields.get("nontransferable_boundary", "")
            )
            if nontransferable in {"不适用", "无", "none", "n/a"}:
                errors.append("missing_nontransferable_boundary")
            target_text = normalize(fields.get("target_sentence", ""))
            authority_text = normalize(fields.get("authority_sentence", ""))
            if len(target_text) > 40 and len(authority_text) < 20:
                errors.append("authority_anchor_too_short_for_target")
            authority_ok, authority_error = authority_check(fields, repo_root)
            if not authority_ok and authority_error:
                errors.append(authority_error)
        reuse_key = (
            fields.get("authority_path", "").strip(),
            fields.get("authority_sentence_lines", "").strip(),
            normalize(fields.get("authority_sentence", "")),
        )
        if reuse_key in overused_keys:
            errors.append(
                f"authority_anchor_overused:{len(overused_keys[reuse_key])}"
            )
        if status == "待补文献" and "[[待补文献" not in fields.get(
            "citation_support", ""
        ):
            errors.append("missing_citation_placeholder")
        findings.append(
            {
                "target_id": target_id,
                "status": status or None,
                "errors": sorted(set(errors)),
            }
        )

    invalid = [item for item in findings if item["errors"]]
    statuses = {
        status: sum(item["status"] == status for item in findings)
        for status in ("通过", "回修", "边界句", "待补文献")
    }
    authority_reuse_groups = [
        {
            "count": len(target_ids),
            "authority_path": key[0],
            "authority_sentence_lines": key[1],
            "authority_sentence": key[2],
            "target_ids": target_ids,
        }
        for key, target_ids in sorted(
            overused_keys.items(), key=lambda item: (-len(item[1]), item[0])
        )
    ]
    pending_without_inline_placeholder = [
        item["target_id"]
        for item in findings
        if item["status"] == "待补文献"
        and "[[待补文献" not in blocks[item["target_id"]].get(
            "target_sentence", ""
        )
    ]
    structural_pass = (
        not binding_errors
        and not missing
        and not extra
        and not duplicates
        and not invalid
    )
    semantic_alignment_pass = (
        structural_pass
        and statuses["回修"] == 0
        and statuses["边界句"] == 0
    )
    citation_support_pass = structural_pass and statuses["待补文献"] == 0
    return {
        "inventory": str(inventory_path),
        "mapping": str(mapping_path),
        "validator_script": str(validator_path),
        "input_bindings": {
            "manuscript": str(manuscript_path),
            "manuscript_sha256_inventory": inventory["manuscript_sha256"],
            "manuscript_sha256_current": manuscript_current_sha256,
            "inventory_sha256": inventory_sha256,
            "mapping_sha256": mapping_sha256,
            "validator_script_sha256": validator_sha256,
            "binding_errors": binding_errors,
        },
        "manuscript_sha256": inventory["manuscript_sha256"],
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "expected_units": len(expected),
        "mapped_units": len(set(expected) & set(blocks)),
        "missing_ids": missing,
        "extra_ids": extra,
        "duplicate_ids": duplicates,
        "status_counts": statuses,
        "authority_anchor_reuse_threshold": MAX_AUTHORITY_ANCHOR_REUSE,
        "authority_anchor_reuse_groups": authority_reuse_groups,
        "pending_without_inline_placeholder": pending_without_inline_placeholder,
        "invalid_records": invalid,
        "structural_pass": structural_pass,
        "semantic_alignment_pass": semantic_alignment_pass,
        "citation_support_pass": citation_support_pass,
        "pass": structural_pass
        and semantic_alignment_pass
        and citation_support_pass,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("inventory", type=Path)
    parser.add_argument("mapping", type=Path)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit(args.inventory, args.mapping, args.repo_root)
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(rendered, end="")


if __name__ == "__main__":
    main()
