#!/usr/bin/env python3
"""Local consistency tests for the binary v16 result schema."""

from __future__ import annotations

import unittest

from analyze_methods import normalize_final


class V16NormalizationTests(unittest.TestCase):
    def test_true_keeps_short_method_overview(self):
        result = normalize_final(
            {
                "qualifies": True,
                "uses_large_scale_compute": False,
                "has_pure_survey": True,
                "has_pure_interview": False,
                "has_experiment": False,
                "method_name": "Online experimental task",
                "short_overview_cn": "研究者在线呈现任务并自行生成个人层面的选择数据。",
                "exclusion_reason_cn": "",
            }
        )
        self.assertTrue(result["qualifies"])
        self.assertFalse(result["uses_large_scale_compute"])
        self.assertTrue(result["has_pure_survey"])
        self.assertTrue(result["short_overview_cn"])

    def test_false_has_no_method_overview(self):
        result = normalize_final(
            {
                "qualifies": False,
                "uses_large_scale_compute": True,
                "has_pure_survey": False,
                "has_pure_interview": True,
                "has_experiment": False,
                "method_name": "irrelevant",
                "short_overview_cn": "irrelevant",
                "exclusion_reason_cn": "需要企业私有数据。",
            }
        )
        self.assertFalse(result["qualifies"])
        self.assertTrue(result["uses_large_scale_compute"])
        self.assertTrue(result["has_pure_interview"])
        self.assertEqual(result["method_name"], "")
        self.assertEqual(result["short_overview_cn"], "")

    def test_true_without_method_is_downgraded_without_retry(self):
        result = normalize_final(
            {
                "qualifies": True,
                "has_pure_survey": False,
                "has_pure_interview": False,
                "has_experiment": True,
                "method_name": "",
                "short_overview_cn": "",
                "exclusion_reason_cn": "",
            }
        )
        self.assertFalse(result["qualifies"])
        self.assertTrue(result["has_experiment"])
        self.assertTrue(result["exclusion_reason_cn"])

if __name__ == "__main__":
    unittest.main()
