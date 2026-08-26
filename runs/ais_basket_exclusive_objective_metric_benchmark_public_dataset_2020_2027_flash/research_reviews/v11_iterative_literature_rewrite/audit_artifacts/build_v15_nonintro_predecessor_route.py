from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


PAIRS = {
    "P1": {
        "predecessor_inventory": "p1_open_citation_debt_closed_current_inventory_v1.json",
        "current_inventory": "p1_v15_authoritative_style_current_inventory_v1.json",
        "predecessor_manuscript": "179_论文一_异质工作空间攻击路径发现_v13第一轮实质回修稿.md",
        "current_manuscript": "184_论文一_异质工作空间攻击路径发现_v15权威原文句级重构稿.md",
    },
    "P2": {
        "predecessor_inventory": "p2_open_citation_debt_closed_current_inventory_v1.json",
        "current_inventory": "p2_v15_authoritative_style_current_inventory_v1.json",
        "predecessor_manuscript": "182_论文二_多模态潜藏操纵执行前识别_v14开放引文债务闭环稿.md",
        "current_manuscript": "185_论文二_多模态潜藏操纵执行前识别_v15权威原文句级重构稿.md",
    },
    "P3": {
        "predecessor_inventory": "p3_open_citation_debt_closed_current_inventory_v1.json",
        "current_inventory": "p3_v15_authoritative_style_current_inventory_v1.json",
        "predecessor_manuscript": "183_论文三_运行中反馈安全控制_v14开放引文债务闭环稿.md",
        "current_manuscript": "186_论文三_运行中反馈安全控制_v15权威原文句级重构稿.md",
    },
}


def sha256_bytes(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inventory(name: str) -> dict[str, object]:
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def build() -> dict[str, object]:
    records: list[dict[str, object]] = []
    papers: dict[str, object] = {}
    for paper_id, spec in PAIRS.items():
        old = load_inventory(spec["predecessor_inventory"])
        new = load_inventory(spec["current_inventory"])
        old_units = [u for u in old["units"] if u["section"] != "1. 引言"]
        new_units = [u for u in new["units"] if u["section"] != "1. 引言"]
        if len(old_units) != len(new_units):
            raise RuntimeError(
                f"{paper_id}: non-introduction denominator changed "
                f"from {len(old_units)} to {len(new_units)}"
            )
        paper_records: list[dict[str, object]] = []
        for index, (before, after) in enumerate(zip(old_units, new_units, strict=True), start=1):
            signature_before = (
                before["type"],
                before["section"],
                before["target_sentence"],
                before["target_sha256"],
            )
            signature_after = (
                after["type"],
                after["section"],
                after["target_sentence"],
                after["target_sha256"],
            )
            if signature_before != signature_after:
                raise RuntimeError(
                    f"{paper_id}: first non-introduction mismatch at ordered unit {index}: "
                    f"{signature_before!r} != {signature_after!r}"
                )
            record = {
                "paper_id": paper_id,
                "ordered_nonintro_index": index,
                "predecessor_target_id": before["target_id"],
                "current_target_id": after["target_id"],
                "type": after["type"],
                "section": after["section"],
                "predecessor_paragraph_id": before["paragraph_id"],
                "current_paragraph_id": after["paragraph_id"],
                "predecessor_lines": before["target_lines"],
                "current_lines": after["target_lines"],
                "target_sentence": after["target_sentence"],
                "target_sha256": after["target_sha256"],
                "exact_type_section_text_hash_match": True,
                "paragraph_or_line_changed": (
                    before["paragraph_id"] != after["paragraph_id"]
                    or before["target_lines"] != after["target_lines"]
                ),
                "source_and_citation_responsibility_route": (
                    "eligible_to_route_from_predecessor because visible sentence and section are exact"
                ),
                "writing_status_inherited": False,
                "route_boundary": (
                    "The route preserves predecessor source/citation responsibility and sentence identity. "
                    "It does not inherit a v12 writing-prototype verdict, semantic pass, implementation pass, "
                    "pilot pass, or result. Paragraph-level readability is assessed separately."
                ),
            }
            paper_records.append(record)
            records.append(record)
        papers[paper_id] = {
            **spec,
            "predecessor_manuscript_sha256": old["manuscript_sha256"],
            "current_manuscript_sha256": new["manuscript_sha256"],
            "predecessor_inventory_sha256": sha256_bytes(HERE / spec["predecessor_inventory"]),
            "current_inventory_sha256": sha256_bytes(HERE / spec["current_inventory"]),
            "nonintro_unit_count": len(paper_records),
            "exact_route_count": sum(
                record["exact_type_section_text_hash_match"] for record in paper_records
            ),
            "paragraph_or_line_changed_count": sum(
                record["paragraph_or_line_changed"] for record in paper_records
            ),
        }
    return {
        "artifact": "v15 non-introduction predecessor exact route",
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "generator": "audit_artifacts/build_v15_nonintro_predecessor_route.py",
        "decision_rule": {
            "scope": "all units outside Section 1 Introduction",
            "ordered_alignment_required": True,
            "exact_fields": ["type", "section", "target_sentence", "target_sha256"],
            "source_citation_responsibility_may_route": True,
            "writing_status_may_route": False,
            "semantic_or_release_gate_may_route": False,
        },
        "papers": papers,
        "summary": {
            "record_count": len(records),
            "exact_route_count": sum(
                record["exact_type_section_text_hash_match"] for record in records
            ),
            "paragraph_or_line_changed_count": sum(
                record["paragraph_or_line_changed"] for record in records
            ),
            "route_gate": all(
                record["exact_type_section_text_hash_match"] for record in records
            ),
            "writing_gate": False,
            "whole_manuscript_gate": False,
        },
        "records": records,
    }


def markdown(result: dict[str, object]) -> str:
    lines = [
        "# v15 三篇引言外正文的 predecessor 精确迁移路线",
        "",
        "本路线逐项比较 179/182/183 与 184/185/186 的引言外单元。只有类型、小节、可见文本和句哈希按顺序完全相同，旧单元的来源与引文责任才允许重绑定。旧写作原型状态、语义门、实现门、pilot、结果和发布状态一律不继承。",
        "",
        f"- 总分母：{result['summary']['record_count']}",
        f"- 精确路线：{result['summary']['exact_route_count']}",
        f"- 段号或行位改变：{result['summary']['paragraph_or_line_changed_count']}",
        f"- route gate：{str(result['summary']['route_gate']).lower()}",
        "- writing gate：false",
        "- whole manuscript gate：false",
        "",
        "## 分论文绑定",
        "",
    ]
    for paper_id, paper in result["papers"].items():
        lines.extend(
            [
                f"### {paper_id}",
                "",
                f"- predecessor：`{paper['predecessor_manuscript']}`，`{paper['predecessor_manuscript_sha256']}`",
                f"- current：`{paper['current_manuscript']}`，`{paper['current_manuscript_sha256']}`",
                f"- 引言外精确路线：{paper['exact_route_count']}/{paper['nonintro_unit_count']}",
                f"- 段号或行位改变：{paper['paragraph_or_line_changed_count']}",
                "",
            ]
        )
    lines.extend(
        [
            "## 解释边界",
            "",
            "段责拆分改变了部分段号和行位，但没有改变引言外任何句子、公式块、表格单元或所属小节。因此此前直接原文阅读、来源能力、非迁移边界和作者协议的责任可以沿本路线定位到 current 单元。该事实不把早期 v12 的低质量写作映射升级为通过，也不证明尚未实施的算法、pilot 或结果。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    result = build()
    json_path = HERE / "v15_三篇引言外正文predecessor精确迁移路线_v1.json"
    md_path = HERE / "v15_三篇引言外正文predecessor精确迁移路线_v1.md"
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(markdown(result), encoding="utf-8")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
