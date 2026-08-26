#!/usr/bin/env python3
"""Offline, read-only readiness check for the three falsification pilots.

The checker deliberately does not install packages, start services, contact model
endpoints, or download data.  It also never emits configured path values or
environment-variable values.  All operating-system probes are injectable so the
logic can be tested without depending on the machine that runs the tests.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Mapping, Optional, Sequence


GIB = 1024**3
DEFAULT_ASSET_ENVIRONMENTS = {
    "arb": "ARB_PATH",
    "verified": "SWE_BENCH_VERIFIED_PATH",
    "agentless": "AGENTLESS_PATH",
    "swe_gym": "SWE_GYM_PATH",
    "harness": "SWE_HARNESS_PATH",
}
DEFAULT_ENDPOINT_ENVIRONMENTS = (
    "MODEL_ENDPOINT",
    "VLLM_ENDPOINT",
    "OPENAI_BASE_URL",
)
PACKAGE_NAMES = (
    "datasets",
    "docker",
    "numpy",
    "torch",
    "transformers",
    "tree_sitter",
)


@dataclass(frozen=True)
class CommandResult:
    """Small, dependency-free result type used by injectable command probes."""

    returncode: int
    stdout: str = ""
    stderr: str = ""


def _decode_output(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.replace("\x00", "")
    raw = bytes(value)
    if b"\x00" in raw[:200]:
        return raw.decode("utf-16-le", errors="replace").replace("\x00", "")
    return raw.decode("utf-8-sig", errors="replace").replace("\x00", "")


def run_command(args: Sequence[str], timeout: float = 4.0) -> CommandResult:
    """Run one non-shell, read-only probe command with bounded execution time."""

    try:
        completed = subprocess.run(
            list(args),
            check=False,
            capture_output=True,
            text=False,
            timeout=timeout,
        )
        return CommandResult(
            returncode=int(completed.returncode),
            stdout=_decode_output(completed.stdout),
            stderr=_decode_output(completed.stderr),
        )
    except subprocess.TimeoutExpired:
        return CommandResult(returncode=124)
    except OSError:
        return CommandResult(returncode=127)


@dataclass
class ProbeSet:
    """Injectable probe functions; defaults perform only local, read-only checks."""

    which: Callable[[str], Optional[str]] = shutil.which
    run: Callable[[Sequence[str], float], CommandResult] = run_command
    path_exists: Callable[[str], bool] = os.path.exists
    disk_usage: Callable[[str], Any] = shutil.disk_usage
    find_spec: Callable[[str], Any] = importlib.util.find_spec
    environ: Mapping[str, str] = field(default_factory=lambda: os.environ)
    system: Callable[[], str] = platform.system
    version_info: Sequence[int] = field(
        default_factory=lambda: tuple(sys.version_info[:3])
    )


@dataclass(frozen=True)
class ReadinessConfig:
    workspace: str
    asset_arguments: Mapping[str, Optional[str]]
    asset_environments: Mapping[str, str]
    endpoint_environments: Sequence[str]
    endpoint_configured: bool = False
    timeout_seconds: float = 4.0


def _safe_run(
    probes: ProbeSet, args: Sequence[str], timeout: float
) -> CommandResult:
    try:
        result = probes.run(args, timeout)
    except (OSError, subprocess.SubprocessError, ValueError):
        return CommandResult(returncode=127)
    return CommandResult(
        returncode=int(result.returncode),
        stdout=_decode_output(result.stdout),
        stderr=_decode_output(result.stderr),
    )


def _probe_container_runtimes(
    probes: ProbeSet, timeout: float
) -> dict[str, dict[str, Any]]:
    report: dict[str, dict[str, Any]] = {}
    for name in ("docker", "podman", "nerdctl"):
        executable = probes.which(name)
        if not executable:
            report[name] = {
                "found": False,
                "responsive": False,
                "linux_backend": False,
            }
            continue
        version = _safe_run(probes, [executable, "--version"], timeout)
        responsive = version.returncode == 0
        linux_backend = False
        if responsive:
            info = _safe_run(probes, [executable, "info"], timeout)
            linux_backend = info.returncode == 0 and bool(
                re.search(r"\blinux\b", info.stdout, flags=re.IGNORECASE)
            )
        report[name] = {
            "found": True,
            "responsive": responsive,
            "linux_backend": linux_backend,
        }
    return report


def _nonempty_lines(text: str) -> list[str]:
    return [line.strip().lstrip("*").strip() for line in text.splitlines() if line.strip()]


def _probe_wsl(probes: ProbeSet, timeout: float) -> dict[str, Any]:
    executable = probes.which("wsl.exe") or probes.which("wsl")
    if not executable:
        return {
            "found": False,
            "responsive": False,
            "distribution_count": 0,
            "running_distribution_count": 0,
            "version2_distribution_count": 0,
        }

    all_distros = _safe_run(
        probes, [executable, "--list", "--quiet"], timeout
    )
    running_distros = _safe_run(
        probes, [executable, "--list", "--running", "--quiet"], timeout
    )
    verbose = _safe_run(
        probes, [executable, "--list", "--verbose"], timeout
    )
    all_lines = _nonempty_lines(all_distros.stdout) if all_distros.returncode == 0 else []
    running_lines = (
        _nonempty_lines(running_distros.stdout)
        if running_distros.returncode == 0
        else []
    )
    version2_count = 0
    if verbose.returncode == 0:
        for line in _nonempty_lines(verbose.stdout):
            if re.search(r"(?:^|\s)2\s*$", line):
                version2_count += 1
    return {
        "found": True,
        "responsive": all_distros.returncode == 0,
        "distribution_count": len(all_lines),
        "running_distribution_count": len(running_lines),
        "version2_distribution_count": version2_count,
    }


def _probe_gpu(probes: ProbeSet, timeout: float) -> dict[str, Any]:
    executable = probes.which("nvidia-smi")
    if not executable:
        return {
            "nvidia_smi_found": False,
            "responsive": False,
            "gpu_count": 0,
            "memory_total_mib": [],
        }
    result = _safe_run(
        probes,
        [
            executable,
            "--query-gpu=memory.total",
            "--format=csv,noheader,nounits",
        ],
        timeout,
    )
    memory: list[int] = []
    if result.returncode == 0:
        for line in result.stdout.splitlines():
            match = re.search(r"\d+", line)
            if match:
                memory.append(int(match.group(0)))
    return {
        "nvidia_smi_found": True,
        "responsive": result.returncode == 0,
        "gpu_count": len(memory),
        "memory_total_mib": memory,
    }


def _resolve_assets(
    config: ReadinessConfig, probes: ProbeSet
) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    public_report: dict[str, dict[str, Any]] = {}
    private_values: dict[str, str] = {}
    for key in DEFAULT_ASSET_ENVIRONMENTS:
        argument = config.asset_arguments.get(key)
        environment_name = config.asset_environments[key]
        environment_value = probes.environ.get(environment_name, "")
        if argument:
            source = "argument"
            value = str(argument)
        elif environment_value:
            source = "environment"
            value = str(environment_value)
        else:
            source = "none"
            value = ""
        configured = bool(value)
        try:
            exists = bool(probes.path_exists(value)) if configured else False
        except (OSError, ValueError):
            exists = False
        public_report[key] = {
            "configured": configured,
            "exists": exists,
            "source": source,
        }
        if configured and exists:
            private_values[key] = value
    return public_report, private_values


def _probe_endpoints(config: ReadinessConfig, probes: ProbeSet) -> dict[str, Any]:
    configured_count = int(config.endpoint_configured)
    for name in config.endpoint_environments:
        if probes.environ.get(name, ""):
            configured_count += 1
    return {
        "configured": configured_count > 0,
        "configured_count": configured_count,
        "checked_environment_count": len(config.endpoint_environments),
    }


def _probe_packages(probes: ProbeSet) -> dict[str, bool]:
    report: dict[str, bool] = {}
    for name in PACKAGE_NAMES:
        try:
            report[name] = probes.find_spec(name) is not None
        except (ImportError, AttributeError, ValueError):
            report[name] = False
    return report


def _probe_disks(
    workspace: str,
    private_asset_values: Mapping[str, str],
    probes: ProbeSet,
) -> dict[str, dict[str, Any]]:
    candidates = {"workspace": workspace, **private_asset_values}
    report: dict[str, dict[str, Any]] = {}
    for label, private_path in candidates.items():
        try:
            usage = probes.disk_usage(private_path)
            report[label] = {
                "available": True,
                "total_gib": round(float(usage.total) / GIB, 1),
                "free_gib": round(float(usage.free) / GIB, 1),
            }
        except (OSError, ValueError, AttributeError):
            report[label] = {
                "available": False,
                "total_gib": None,
                "free_gib": None,
            }
    return report


def _max_free_gib(disks: Mapping[str, Mapping[str, Any]], labels: Sequence[str]) -> float:
    values = [
        float(disks[label]["free_gib"])
        for label in labels
        if label in disks and disks[label].get("free_gib") is not None
    ]
    return max(values, default=0.0)


def _asset_gap(assets: Mapping[str, Mapping[str, Any]], key: str) -> Optional[str]:
    state = assets[key]
    if not state["configured"]:
        return f"asset:{key}:not_configured"
    if not state["exists"]:
        return f"asset:{key}:not_found"
    return None


def _pilot_statuses(
    *,
    python_ok: bool,
    system_name: str,
    containers: Mapping[str, Mapping[str, Any]],
    wsl: Mapping[str, Any],
    assets: Mapping[str, Mapping[str, Any]],
    endpoints: Mapping[str, Any],
    packages: Mapping[str, bool],
    disks: Mapping[str, Mapping[str, Any]],
) -> dict[str, dict[str, Any]]:
    container_ready = any(item["responsive"] for item in containers.values())
    linux_container_ready = any(
        item["responsive"] and item["linux_backend"]
        for item in containers.values()
    )
    linux_execution_ready = (
        system_name.lower() != "windows"
        or linux_container_ready
        or int(wsl["version2_distribution_count"]) > 0
    )

    definitions = {
        "P1": {
            "assets": ("verified", "agentless", "harness"),
            "packages": ("datasets", "torch", "transformers"),
            "disk_labels": ("workspace", "verified", "agentless", "harness"),
            "disk_min_gib": 200.0,
            "container": True,
            "endpoint": True,
        },
        "P2": {
            "assets": ("arb",),
            # The first mechanism pilot consumes ARB's released pre-split chunks
            # and cached file rankings.  Tree-sitter is optional for later AST
            # enrichments and must not block the no-parser execution path.
            "packages": (),
            "disk_labels": ("workspace", "arb"),
            "disk_min_gib": 10.0,
            "container": False,
            "endpoint": False,
        },
        "P3": {
            "assets": ("swe_gym", "harness"),
            "packages": ("datasets", "torch", "transformers"),
            "disk_labels": ("workspace", "swe_gym", "harness"),
            "disk_min_gib": 120.0,
            "container": True,
            "endpoint": True,
        },
    }

    result: dict[str, dict[str, Any]] = {}
    for pilot, definition in definitions.items():
        gaps: list[str] = []
        if not python_ok:
            gaps.append("python:requires_3.10_or_newer")
        for asset in definition["assets"]:
            gap = _asset_gap(assets, asset)
            if gap:
                gaps.append(gap)
        for package in definition["packages"]:
            if not packages[package]:
                gaps.append(f"python_package:{package}:not_importable")
        if definition["container"]:
            if not container_ready:
                gaps.append("container_runtime:not_responsive")
            if not linux_execution_ready:
                gaps.append("linux_execution:not_detected")
        if definition["endpoint"] and not endpoints["configured"]:
            gaps.append("model_endpoint:not_configured")
        max_free = _max_free_gib(disks, definition["disk_labels"])
        if max_free < definition["disk_min_gib"]:
            gaps.append(f"disk_free:requires_{int(definition['disk_min_gib'])}GiB")
        result[pilot] = {
            "ready": not gaps,
            "gaps": gaps,
            "disk_min_gib": definition["disk_min_gib"],
            "max_visible_free_gib": max_free,
        }
    return result


def collect_readiness(
    config: ReadinessConfig, probes: Optional[ProbeSet] = None
) -> dict[str, Any]:
    """Collect a privacy-preserving readiness report without external I/O."""

    probes = probes or ProbeSet()
    version = tuple(int(part) for part in probes.version_info[:3])
    python_ok = version >= (3, 10, 0)
    system_name = str(probes.system())
    containers = _probe_container_runtimes(probes, config.timeout_seconds)
    wsl = _probe_wsl(probes, config.timeout_seconds)
    gpu = _probe_gpu(probes, config.timeout_seconds)
    assets, private_asset_values = _resolve_assets(config, probes)
    endpoints = _probe_endpoints(config, probes)
    packages = _probe_packages(probes)
    disks = _probe_disks(config.workspace, private_asset_values, probes)
    pilots = _pilot_statuses(
        python_ok=python_ok,
        system_name=system_name,
        containers=containers,
        wsl=wsl,
        assets=assets,
        endpoints=endpoints,
        packages=packages,
        disks=disks,
    )
    return {
        "schema_version": 1,
        "policy": {
            "read_only": True,
            "network_accessed": False,
            "secret_values_emitted": False,
        },
        "python": {
            "version": ".".join(str(part) for part in version),
            "meets_minimum_3_10": python_ok,
            "packages": packages,
        },
        "system": {
            "name": system_name,
            "container_runtimes": containers,
            "wsl": wsl,
            "gpu": gpu,
            "disks": disks,
        },
        "inputs": {
            "assets": assets,
            "model_endpoints": endpoints,
        },
        "pilots": pilots,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Offline/read-only readiness check for P1, P2, and P3."
    )
    parser.add_argument("--workspace", default=str(Path.cwd()))
    for key, default_environment in DEFAULT_ASSET_ENVIRONMENTS.items():
        option = key.replace("_", "-")
        parser.add_argument(f"--{option}-path")
        parser.add_argument(f"--{option}-env", default=default_environment)
    parser.add_argument(
        "--model-endpoint-env",
        action="append",
        dest="endpoint_environments",
        help=(
            "Environment-variable name to check. Repeatable; its value is never "
            "printed or contacted."
        ),
    )
    parser.add_argument(
        "--model-endpoint-configured",
        action="store_true",
        help="Record an externally managed endpoint without supplying its value.",
    )
    parser.add_argument("--timeout-seconds", type=float, default=4.0)
    parser.add_argument("--compact", action="store_true")
    return parser


def config_from_args(args: argparse.Namespace) -> ReadinessConfig:
    timeout = min(max(float(args.timeout_seconds), 0.1), 30.0)
    asset_arguments = {
        key: getattr(args, f"{key}_path") for key in DEFAULT_ASSET_ENVIRONMENTS
    }
    asset_environments = {
        key: getattr(args, f"{key}_env") for key in DEFAULT_ASSET_ENVIRONMENTS
    }
    endpoint_environments = tuple(
        args.endpoint_environments or DEFAULT_ENDPOINT_ENVIRONMENTS
    )
    return ReadinessConfig(
        workspace=str(args.workspace),
        asset_arguments=asset_arguments,
        asset_environments=asset_environments,
        endpoint_environments=endpoint_environments,
        endpoint_configured=bool(args.model_endpoint_configured),
        timeout_seconds=timeout,
    )


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parser().parse_args(argv)
    report = collect_readiness(config_from_args(args))
    if args.compact:
        print(json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
