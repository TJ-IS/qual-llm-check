#!/usr/bin/env python3
"""Blind independent confirmation of stage-one programming candidates."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
MODULE_PATH = RUN_DIR / "analyze_title_abstract.py"
SPEC = importlib.util.spec_from_file_location("programming_slr_stage2_runner", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load stage-one runner from {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


if __name__ == "__main__":
    sys.exit(MODULE.main("config_stage2.json"))
