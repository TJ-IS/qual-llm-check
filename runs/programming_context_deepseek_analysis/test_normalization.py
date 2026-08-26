from analyze_programming_context import normalize_final


def test_true_payload_preserves_fields() -> None:
    row = normalize_final(
        {
            "is_programming_context": True,
            "content_summary_cn": "研究代码评审。",
            "programming_context_definition_cn": "评审源代码算编程情境，普通项目会议不算。",
            "independent_variables": ["review type（评审类型）"],
            "mediators": [],
            "moderators": [],
            "dependent_variables": ["defect detection（缺陷发现）"],
            "theory_names": ["Cognitive Load Theory"],
            "research_method_cn": "随机实验。",
            "situation_awareness_relation_type": "conceptually_related",
            "situation_awareness_relation_cn": "作者未明示该理论，但涉及理解当前代码状态。",
        }
    )
    assert row["is_programming_context"] is True
    assert row["required_fields_complete"] is True
    assert row["situation_awareness_relation_type"] == "conceptually_related"
    assert row["independent_variables"] == ["review type（评审类型）"]


def test_false_payload_clears_details() -> None:
    row = normalize_final(
        {
            "is_programming_context": False,
            "content_summary_cn": "不应保留",
            "independent_variables": ["不应保留"],
            "exclusion_reason_cn": "仅使用整数规划。",
        }
    )
    assert row["is_programming_context"] is False
    assert row["content_summary_cn"] == ""
    assert row["independent_variables"] == []
    assert row["exclusion_reason_cn"] == "仅使用整数规划。"


if __name__ == "__main__":
    test_true_payload_preserves_fields()
    test_false_payload_clears_details()
    print("normalization tests passed")

