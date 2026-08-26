from __future__ import annotations

import json
import unittest
from types import SimpleNamespace

from check_readiness import (
    GIB,
    CommandResult,
    DEFAULT_ASSET_ENVIRONMENTS,
    DEFAULT_ENDPOINT_ENVIRONMENTS,
    ProbeSet,
    ReadinessConfig,
    collect_readiness,
)


class ReadinessTests(unittest.TestCase):
    def _config(self, **overrides):
        values = {
            "workspace": "C:/private/workspace",
            "asset_arguments": {
                key: None for key in DEFAULT_ASSET_ENVIRONMENTS
            },
            "asset_environments": dict(DEFAULT_ASSET_ENVIRONMENTS),
            "endpoint_environments": DEFAULT_ENDPOINT_ENVIRONMENTS,
            "endpoint_configured": False,
            "timeout_seconds": 0.5,
        }
        values.update(overrides)
        return ReadinessConfig(**values)

    def test_all_pilots_ready_with_injected_probes(self):
        secret_paths = {
            "ARB_PATH": "D:/secret/arb",
            "SWE_BENCH_VERIFIED_PATH": "D:/secret/verified",
            "AGENTLESS_PATH": "D:/secret/agentless",
            "SWE_GYM_PATH": "D:/secret/swe-gym",
            "SWE_HARNESS_PATH": "D:/secret/harness",
        }
        environment = {
            **secret_paths,
            "MODEL_ENDPOINT": "https://endpoint.example/super-secret-token",
        }

        def fake_which(name):
            return name if name in {"docker", "wsl.exe", "nvidia-smi"} else None

        def fake_run(args, timeout):
            del timeout
            command = args[0]
            if command == "docker":
                if args[1:] == ["--version"]:
                    return CommandResult(0, "Docker version test")
                if args[1:] == ["info"]:
                    return CommandResult(0, "OSType: linux")
            if command == "wsl.exe":
                if args[1:] == ["--list", "--quiet"]:
                    return CommandResult(0, "PrivateDistro\n")
                if args[1:] == ["--list", "--running", "--quiet"]:
                    return CommandResult(0, "PrivateDistro\n")
                if args[1:] == ["--list", "--verbose"]:
                    return CommandResult(
                        0, "NAME STATE VERSION\n* PrivateDistro Running 2\n"
                    )
            if command == "nvidia-smi":
                return CommandResult(0, "24564\n24564\n")
            return CommandResult(1)

        probes = ProbeSet(
            which=fake_which,
            run=fake_run,
            path_exists=lambda path: path in set(secret_paths.values()),
            disk_usage=lambda path: SimpleNamespace(
                total=1000 * GIB, used=400 * GIB, free=600 * GIB
            ),
            find_spec=lambda name: object(),
            environ=environment,
            system=lambda: "Windows",
            version_info=(3, 12, 4),
        )
        report = collect_readiness(self._config(), probes)

        self.assertTrue(report["pilots"]["P1"]["ready"])
        self.assertTrue(report["pilots"]["P2"]["ready"])
        self.assertTrue(report["pilots"]["P3"]["ready"])
        self.assertEqual(report["system"]["wsl"]["distribution_count"], 1)
        self.assertEqual(report["system"]["wsl"]["running_distribution_count"], 1)
        self.assertEqual(report["system"]["wsl"]["version2_distribution_count"], 1)
        self.assertEqual(report["system"]["gpu"]["gpu_count"], 2)

        serialized = json.dumps(report, sort_keys=True)
        for secret in secret_paths.values():
            self.assertNotIn(secret, serialized)
        self.assertNotIn(environment["MODEL_ENDPOINT"], serialized)
        self.assertNotIn("PrivateDistro", serialized)

    def test_missing_state_produces_stable_gap_codes(self):
        probes = ProbeSet(
            which=lambda name: None,
            run=lambda args, timeout: CommandResult(127),
            path_exists=lambda path: False,
            disk_usage=lambda path: SimpleNamespace(
                total=20 * GIB, used=15 * GIB, free=5 * GIB
            ),
            find_spec=lambda name: None,
            environ={},
            system=lambda: "Windows",
            version_info=(3, 9, 18),
        )
        report = collect_readiness(self._config(), probes)

        for pilot in ("P1", "P2", "P3"):
            self.assertFalse(report["pilots"][pilot]["ready"])
            self.assertIn(
                "python:requires_3.10_or_newer",
                report["pilots"][pilot]["gaps"],
            )
        self.assertIn(
            "asset:arb:not_configured", report["pilots"]["P2"]["gaps"]
        )
        self.assertIn(
            "container_runtime:not_responsive",
            report["pilots"]["P1"]["gaps"],
        )
        self.assertIn(
            "linux_execution:not_detected", report["pilots"]["P3"]["gaps"]
        )
        self.assertIn(
            "model_endpoint:not_configured", report["pilots"]["P1"]["gaps"]
        )
        self.assertIn(
            "disk_free:requires_10GiB", report["pilots"]["P2"]["gaps"]
        )

    def test_argument_path_is_checked_but_never_disclosed(self):
        private_path = "Z:/classified/arb-corpus"
        asset_arguments = {
            key: (private_path if key == "arb" else None)
            for key in DEFAULT_ASSET_ENVIRONMENTS
        }
        probes = ProbeSet(
            which=lambda name: None,
            run=lambda args, timeout: CommandResult(127),
            path_exists=lambda path: path == private_path,
            disk_usage=lambda path: SimpleNamespace(
                total=50 * GIB, used=10 * GIB, free=40 * GIB
            ),
            find_spec=lambda name: None,
            environ={},
            system=lambda: "Linux",
            version_info=(3, 11, 0),
        )
        report = collect_readiness(
            self._config(asset_arguments=asset_arguments), probes
        )

        self.assertEqual(
            report["inputs"]["assets"]["arb"],
            {"configured": True, "exists": True, "source": "argument"},
        )
        self.assertTrue(report["pilots"]["P2"]["ready"])
        self.assertFalse(report["python"]["packages"]["tree_sitter"])
        self.assertNotIn(
            "python_package:tree_sitter:not_importable",
            report["pilots"]["P2"]["gaps"],
        )
        self.assertNotIn(private_path, json.dumps(report))

    def test_wsl_utf16_style_nuls_are_normalized_without_names(self):
        def fake_run(args, timeout):
            del timeout
            if args[1:] == ["--list", "--quiet"]:
                return CommandResult(0, "U\x00b\x00u\x00n\x00t\x00u\x00\n\x00")
            if args[1:] == ["--list", "--running", "--quiet"]:
                return CommandResult(0, "")
            return CommandResult(
                0,
                "N\x00A\x00M\x00E\x00 \x00S\x00T\x00A\x00T\x00E\x00 "
                "\x00V\x00E\x00R\x00S\x00I\x00O\x00N\x00\n\x00"
                "U\x00b\x00u\x00n\x00t\x00u\x00 \x00S\x00t\x00o\x00p\x00p\x00e\x00d\x00 \x002\x00\n\x00",
            )

        probes = ProbeSet(
            which=lambda name: "wsl.exe" if name == "wsl.exe" else None,
            run=fake_run,
            path_exists=lambda path: False,
            disk_usage=lambda path: SimpleNamespace(
                total=20 * GIB, used=1 * GIB, free=19 * GIB
            ),
            find_spec=lambda name: None,
            environ={},
            system=lambda: "Windows",
            version_info=(3, 11, 0),
        )
        report = collect_readiness(self._config(), probes)
        wsl = report["system"]["wsl"]

        self.assertEqual(wsl["distribution_count"], 1)
        self.assertEqual(wsl["running_distribution_count"], 0)
        self.assertEqual(wsl["version2_distribution_count"], 1)
        self.assertNotIn("Ubuntu", json.dumps(report))


if __name__ == "__main__":
    unittest.main()
