# -*- coding: utf-8 -*-
"""Patch run_screening_security.py: security-relevance-only schema."""
import io, re

p = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\run_screening_security.py"
src = io.open(p, encoding="utf-8").read()

# 1. docstring
src = src.replace(
    '"""Screen all local AIS Basket full texts: security-relevant research with\nalgorithm development as the core contribution."""',
    '"""Screen all local AIS Basket full texts: attack/vulnerability-focused security relevance.\nNo algorithm-development requirement (any research type qualifies if security-core)."""'
)

# 2. gate keys
src = src.replace(
    '''SECURITY_GATE_KEYS = (
    "malicious_or_adversarial_actor_central",
    "security_damage_scope",
    "attack_defense_detection_focus",
    "not_financial_fraud_only",
)''',
    '''SECURITY_GATE_KEYS = (
    "malicious_or_adversarial_actor_central",
    "security_damage_scope",
    "attack_defense_detection_focus",
    "not_excluded_type",
)'''
)

# 3. remove algorithm/publicness constants
src = re.sub(
    r'ALGORITHM_GATE_KEYS = \(.*?ALLOWED_PUBLICNESS = \{"public", "private_or_nonpublic", "mixed", "unclear"\}\n',
    '', src, flags=re.S)

# 4. validate_decision -> security-only
new_validate = '''def validate_decision(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")

    security = require_dict(payload.get("security_relevance"), "security_relevance")
    security_gates = require_dict(security.get("gates"), "security_relevance.gates")

    security_values = [require_bool(security_gates.get(key), f"security_relevance.gates.{key}") for key in SECURITY_GATE_KEYS]

    security_status = str(security.get("status") or "")
    if security_status not in ALL_SECURITY:
        raise ValueError(f"invalid security status: {security_status!r}")

    security_expected = all(security_values) and security_status in ALLOWED_SECURITY
    security_pass = require_bool(security.get("pass"), "security_relevance.pass")
    if security_pass != security_expected:
        raise ValueError("module pass is logically inconsistent with gates/status")
    security_include = require_bool(payload.get("security_include"), "security_include")
    if security_include != security_pass:
        raise ValueError("security_include must equal security_relevance.pass")

    require_list(payload.get("evidence_pointers"), "evidence_pointers")
    require_list(payload.get("exclusion_trigger_codes"), "exclusion_trigger_codes")

    try:
        confidence = float(payload.get("confidence"))
    except (TypeError, ValueError) as exc:
        raise ValueError("confidence must be numeric") from exc
    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    payload["confidence"] = confidence
    return payload

'''
start = src.index("def validate_decision(")
end = src.index("def usage_dict(")
src = src[:start] + new_validate + src[end:]

# 5. write_reports: security-only
new_write_reports = '''def write_reports(
    output_dir: Path,
    all_files: list[Path],
    decisions: dict[str, dict[str, Any]],
    config: dict[str, Any],
    fingerprint: str,
) -> None:
    rows = [decisions[name] for name in sorted(decisions)]
    security_matches = [row for row in rows if row.get("security_include") is True]
    input_years = Counter(str(year_from_filename(path)) for path in all_files)
    usage_keys = (
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "prompt_cache_hit_tokens",
        "prompt_cache_miss_tokens",
    )
    summary = {
        "updated_at": utc_now(),
        "analysis_version": config["analysis_version"],
        "model": config["model"]["name"],
        "max_concurrency": config["batch"]["max_concurrency"],
        "prompt_fingerprint": fingerprint,
        "year_range": config["year_range"],
        "input_source": str(resolve_from_run(str(config["input_dir"]))),
        "input_fulltexts": len(all_files),
        "input_year_counts": dict(sorted(input_years.items())),
        "completed": len(rows),
        "pending": len(all_files) - len(rows),
        "completed_year_counts": counter_by_year(rows),
        "security_pass_count": sum(
            bool((row.get("security_relevance") or {}).get("pass")) for row in rows
        ),
        "security_include_count": len(security_matches),
        "security_exclude_count": len(rows) - len(security_matches),
        "security_include_year_counts": counter_by_year(security_matches),
        "security_include_journal_counts": dict(sorted(Counter(str(row.get("journal") or "") for row in security_matches).items())),
        "security_status_counts": dict(sorted(Counter(str((row.get("security_relevance") or {}).get("status") or "") for row in rows).items())),
        "usage": {
            key: sum(int((row.get("usage") or {}).get(key, 0)) for row in rows)
            for key in usage_keys
        },
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    tmp_summary = output_dir / "summary.json.tmp"
    tmp_summary.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8"
    )
    os.replace(tmp_summary, output_dir / "summary.json")

    fields = [
        "record_id",
        "source_file",
        "title",
        "authors",
        "year",
        "journal",
        "doi",
        "security_include",
        "security_pass",
        "security_status",
        "security_gates_json",
        "security_reason_cn",
        "exclusion_trigger_codes",
        "decision_reason_cn",
        "confidence",
        "fulltext_chars",
        "attempts",
    ]
    tmp_csv = output_dir / "decisions.csv.tmp"
    with tmp_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            security = row.get("security_relevance") or {}
            writer.writerow(
                {
                    "record_id": row.get("record_id"),
                    "source_file": row.get("source_file"),
                    "title": row.get("title"),
                    "authors": row.get("authors"),
                    "year": row.get("year"),
                    "journal": row.get("journal"),
                    "doi": row.get("doi"),
                    "security_include": row.get("security_include"),
                    "security_pass": security.get("pass"),
                    "security_status": security.get("status"),
                    "security_gates_json": json.dumps(security.get("gates") or {}, ensure_ascii=False),
                    "security_reason_cn": security.get("reason_cn"),
                    "exclusion_trigger_codes": " | ".join(str(x) for x in row.get("exclusion_trigger_codes") or []),
                    "decision_reason_cn": row.get("decision_reason_cn"),
                    "confidence": row.get("confidence"),
                    "fulltext_chars": row.get("fulltext_chars"),
                    "attempts": row.get("attempts"),
                }
            )
    os.replace(tmp_csv, output_dir / "decisions.csv")

    def write_markdown(filename: str, title: str, selected: list[dict[str, Any]]) -> None:
        markdown = [f"# {title}", "", f"Completed: {len(rows)} / {len(all_files)}", f"Retained: {len(selected)}", ""]
        for row in sorted(
            selected,
            key=lambda item: (
                -float(item.get("confidence") or 0),
                str(item.get("title") or ""),
            ),
        ):
            security = row.get("security_relevance") or {}
            markdown.extend(
                [
                    f"## {row.get('title')}",
                    "",
                    f"- Year/journal: {row.get('year')} / {row.get('journal')}",
                    f"- DOI: {row.get('doi')}",
                    f"- Security status: {security.get('status', '')}",
                    f"- Security reason: {security.get('reason_cn', '')}",
                    f"- Exclusion codes: {' | '.join(str(x) for x in row.get('exclusion_trigger_codes') or [])}",
                    f"- Decision: {row.get('decision_reason_cn', '')}",
                    f"- Confidence: {row.get('confidence')}",
                    "",
                ]
            )
        tmp_path = output_dir / f"{filename}.tmp"
        tmp_path.write_text("\\n".join(markdown), encoding="utf-8")
        os.replace(tmp_path, output_dir / filename)

    write_markdown("security_matches.md", "Security-relevant full texts (attack/vulnerability focus, any research type)", security_matches)

'''
start = src.index("def write_reports(")
end = src.index("def parse_args()")
src = src[:start] + new_write_reports + src[end:]

io.open(p, "w", encoding="utf-8", newline="\n").write(src)
print("patched ok, len:", len(src))
