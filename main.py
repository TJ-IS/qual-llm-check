import argparse
import asyncio
import csv
import hashlib
import json
import os
import random
import re
import shutil
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


DEFAULT_SOURCE_CSV = "all_MISQ_ISR.csv"
DEFAULT_RUN_ROOT = "runs"
DEFAULT_CONFIG = "config.json"
DEFAULT_INPUT_COPY = "source.csv"
DEFAULT_SYSTEM_PROMPT = "system_prompt.md"
DEFAULT_USER_PROMPT = "user_prompt_template.md"
DEFAULT_ENCODING = "utf-8-sig"

CODING_AGENT_UX_SYSTEM_PROMPT = """You are a careful information-systems literature screening assistant.

Project goal:
We are building new individual-level user-experience concepts, constructs, and measures for coding agents. Screen MISQ/ISR papers for whether they contain an individual-level UX concept or phenomenon that could be adapted into an important coding-agent-specific UX concept.

Focal research object:
A coding agent is an AI software-engineering agent that can inspect a codebase, edit files, run shell commands/tests/linters, use tools, work across multiple files, create commits or pull requests, ask for clarification, and sometimes work asynchronously or with reduced human approval.

Open discovery stance:
Do not force every relevant paper into one predetermined concept. Calibrated delegation and control is only one promising example. Include any paper that contains an important individual-level UX concept or phenomenon that seems suitable for coding-agent-specific adaptation.

What makes a UX concept coding-agent-specific:
The concept should matter because coding agents are not just chatbots, recommender systems, search tools, generic automation, or traditional programming IDE features. Coding agents can take consequential actions inside executable and evolving code environments. They transform user experience through some combination of codebase context, tool execution, multi-step autonomy, artifact production, verification traces, permissions, background work, responsibility for code quality, and developer skill/identity.

Possible coding-agent-specific UX concept areas include, but are not limited to:
- calibrated delegation, autonomy, control, approval, interruption, and course correction;
- action-boundary awareness, permission comfort, safe stopping, overscope concern, and blast-radius sensitivity;
- context alignment: whether the agent understands the right files, architecture, conventions, dependencies, and task intent;
- verification burden and evidential traceability through diffs, tests, logs, citations, explanations, commits, or pull requests;
- proactive or background agent timing: when the agent should notify, ask, draft, continue, or stay silent;
- co-agency, authorship, responsibility, accountability, and ownership of agent-produced code;
- developer agency, expertise, learning, deskilling, confidence, flow, attention, and cognitive offloading;
- collaboration quality with a nonhuman teammate that can execute work, not merely advise;
- trust, reliance, transparency, explainability, or acceptance when older constructs do not fit the code-action setting.

Screening task:
Decide whether the paper contains a concept or phenomenon that is suitable for our team to adapt into a coding-agent-specific individual UX concept. The paper does not have to mention coding agents, develop a construct, or provide measurement guidance. The key question is whether there is a recognizable individual-level UX concept in the paper that could be meaningfully reworked for coding agents.

Include when the title, abstract, or keywords show all four gates:
Gate 1 - Individual UX relevance:
- The paper concerns individual users, developers, workers, customers, learners, professionals, or human decision makers and their perceptions, experiences, judgments, behavior, cognition, affect, learning, or collaboration with technology.

Gate 2 - Adaptable concept presence:
- The paper contains a recognizable concept, phenomenon, experience, behavior, tension, or mechanism that could be adapted by us. The paper itself does not need to define, refine, operationalize, measure, or validate that concept.

Gate 3 - Coding-agent-specific adaptation gap:
- The concept would need meaningful adaptation for coding agents because the agent can inspect code, execute tools, modify artifacts, act across time/steps, produce reviewable outputs, or create responsibility for code quality and downstream effects. If the concept transfers directly without changing its meaning, boundaries, dimensions, or stakes, it is not enough.

Gate 4 - Practical importance:
- The adapted concept would matter for real coding-agent use, not merely be a narrow curiosity. It should connect to consequential UX issues such as safe and effective delegation, code quality, verification burden, user control, action boundaries, accountability, trust/reliance calibration, productivity, flow, interruption, learning, expertise, deskilling, collaboration, responsibility, or developer well-being.

Strong inclusion signals include:
1. Direct fit: AI coding assistants, software developers, programming tools, human-AI software engineering, intelligent agents, automation, or developer experience with individual user perceptions, behaviors, or work practices.
2. Adjacent construct fit: individual-level constructs about trust, reliance, delegation, control, autonomy, transparency, accountability, explainability, interruption, cognitive load, flow, expertise, learning, user agency, technology acceptance, or human-AI collaboration that need adaptation for coding agents.
3. Adaptable concept fit: the paper contains a concept, phenomenon, behavior, experience, or mechanism that could plausibly be reworked for coding-agent UX research.
4. Practical importance: the candidate concept would address a meaningful issue in how people use, supervise, depend on, or work with coding agents.

Exclude when the paper is only:
- firm-level, market-level, platform/ecosystem-level, policy-level, or purely organizational without an individual UX mechanism;
- a technical, econometric, or methodological paper with no relevant individual UX concept;
- about IT careers, labor markets, governance, security, adoption, or productivity without a clear bridge to individual experience of using or supervising coding agents;
- a generic technology-use paper where the concept transfers directly without needing coding-agent-specific adaptation;
- a paper with a coding-agent-specific angle that is too trivial, narrow, or practically unimportant for developing a major UX concept.

Decision calibration:
- Use relevant=true for strong or moderate fit: the paper passes the four gates and contains a plausible candidate concept or phenomenon for coding-agent UX research.
- Use relevant=false for weak/no fit or when the bridge is too speculative.
- If ambiguous, choose relevant=false with decision_label="uncertain_exclude" and a lower confidence score.
- Use only the title, abstract, and keywords as evidence. Do not infer from references, authors, journal reputation, or external knowledge.

Return only valid JSON. Use this exact schema:
{
  "relevant": true,
  "confidence": 0.0,
  "decision_label": "include_strong | include_possible | uncertain_exclude | exclude_no_individual_ux | exclude_no_adaptable_concept | exclude_not_coding_agent_specific | exclude_low_practical_importance | exclude_domain_mismatch",
  "fit_level": "strong | moderate | weak | none",
  "source_concept": "concept or phenomenon in the paper that could be adapted, or 'none'",
  "candidate_coding_agent_ux_concept": "possible adapted coding-agent UX concept name, or 'none'",
  "ux_topic": "delegation_control | action_boundary_safety | context_alignment | verification_traceability | proactivity_interruption | coagency_responsibility | skill_learning_identity | cognitive_load_attention | collaboration_communication | trust_reliance_calibration | workflow_asynchrony | affect_confidence_flow | other | none",
  "adaptation_potential": "high | medium | low | none",
  "practical_importance": "why this would matter in real coding-agent use, or 'none'",
  "uniqueness_rationale": "why this concept is distinctive or mismatched when moved to coding agents, or 'none'",
  "evidence": "brief phrase from the title, abstract, or keywords that supports the decision",
  "reason": "one concise sentence explaining the decision"
}
"""

CODING_AGENT_UX_USER_PROMPT = """Screen this literature record using the system criteria.

Use the title, abstract, and keywords as evidence. The other bibliographic fields are provided only for orientation.

Row key: {row_key}
Row number: {row_number}
Title: {title}
Year: {year}
Source title: {source_title}
Document type: {document_type}
Author keywords: {author_keywords}
Index keywords: {index_keywords}

Abstract:
{abstract}
"""


@dataclass(frozen=True)
class ScreenItem:
    row_number: int
    row_key: str
    row: dict[str, str]
    title: str
    abstract: str


@dataclass(frozen=True)
class ModelSpec:
    name: str
    model: str
    api_key_env: str
    base_url_env: str | None
    base_url: str | None
    enabled: bool
    timeout: float
    max_tokens: int
    temperature: float
    response_format: dict[str, Any] | None


@dataclass(frozen=True)
class ModelDecision:
    model_name: str
    model: str
    relevant: bool
    confidence: float
    decision_label: str
    fit_level: str
    source_concept: str
    candidate_coding_agent_ux_concept: str
    ux_topic: str
    adaptation_potential: str
    practical_importance: str
    uniqueness_rationale: str
    evidence: str
    reason: str
    raw_response: str


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be >= 1")
    return parsed


def non_negative_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be >= 0")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Create run directories and screen MISQ/ISR records for coding-agent "
            "user-experience concept development with two independent LLM calls."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create an isolated screening run directory.")
    init_parser.add_argument("--run-dir", default=None, help="Run directory to create.")
    init_parser.add_argument("--input", default=DEFAULT_SOURCE_CSV, help="Source CSV to copy into the run directory.")
    init_parser.add_argument("--env-file", default=".env", help="Env file used by this run, stored as a relative path.")
    init_parser.add_argument("--first-model", default="deepseek-v4-pro", help="First reviewer model id.")
    init_parser.add_argument("--second-model", default="deepseek-v4-pro", help="Second reviewer model id.")
    init_parser.add_argument("--overwrite", action="store_true", help="Overwrite existing config and prompt files.")

    preview_parser = subparsers.add_parser("preview", help="Print configured prompts without calling any API.")
    preview_parser.add_argument("--run-dir", required=True, help="Existing run directory.")
    preview_parser.add_argument("--examples", type=non_negative_int, default=1, help="Number of rendered examples to show.")

    run_parser = subparsers.add_parser("run", help="Run the dual-model screening.")
    run_parser.add_argument("--run-dir", required=True, help="Existing run directory.")
    run_parser.add_argument("--limit", type=positive_int, default=None, help="Only process this many pending rows.")
    run_parser.add_argument("--offset", type=non_negative_int, default=0, help="Skip this many input rows before resume filtering.")
    run_parser.add_argument("--reset", action="store_true", help="Delete prior outputs in the run directory before running.")
    run_parser.add_argument("--dry-run", action="store_true", help="Load data and show pending rows without calling APIs.")

    return parser


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def normalize_cell(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("\ufeff", "").strip()


def default_run_dir() -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path(DEFAULT_RUN_ROOT) / f"coding_agent_ux_{stamp}"


def relative_to(path: Path, base: Path) -> str:
    try:
        return os.path.relpath(path.resolve(), base.resolve())
    except ValueError:
        return str(path.resolve())


def resolve_run_path(run_dir: Path, value: str | None) -> Path | None:
    if value is None or value == "":
        return None
    path = Path(value)
    if path.is_absolute():
        return path
    return run_dir / path


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return slug or "model"


def write_text_if_allowed(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        return
    path.write_text(content, encoding="utf-8")


def build_default_config(run_dir: Path, env_file: Path, first_model: str, second_model: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "created_at": utc_now(),
        "input_file": DEFAULT_INPUT_COPY,
        "encoding": DEFAULT_ENCODING,
        "title_column": "Title",
        "abstract_column": "Abstract",
        "id_column": "EID",
        "row_key_mode": "id_with_row_number",
        "env_file": relative_to(env_file, run_dir),
        "prompt_files": {
            "system": DEFAULT_SYSTEM_PROMPT,
            "user_template": DEFAULT_USER_PROMPT,
        },
        "screening": {
            "max_concurrency": 4,
            "retries": 3,
            "retry_base_delay": 2.0,
        },
        "models": [
            {
                "name": "deepseekv4pro_reviewer_1",
                "model": first_model,
                "enabled": True,
                "api_key_env": "NEW_API_KEY",
                "base_url_env": "NEW_API_BASE_URL",
                "base_url": "https://api.deepseek.com",
                "timeout": 90.0,
                "max_tokens": 900,
                "temperature": 0,
                "response_format": {"type": "json_object"},
            },
            {
                "name": "deepseekv4pro_reviewer_2",
                "model": second_model,
                "enabled": True,
                "api_key_env": "NEW_API_KEY",
                "base_url_env": "NEW_API_BASE_URL",
                "base_url": "https://api.deepseek.com",
                "timeout": 90.0,
                "max_tokens": 900,
                "temperature": 0,
                "response_format": {"type": "json_object"},
            },
        ],
        "outputs": {
            "all_screened_csv": "all_screened.csv",
            "included_csv": "included_consensus.csv",
            "disagreements_csv": "model_disagreements.csv",
            "progress_jsonl": "progress.jsonl",
            "decisions_jsonl": "model_decisions.jsonl",
            "errors_jsonl": "errors.jsonl",
        },
    }


def load_config(run_dir: Path) -> dict[str, Any]:
    config_path = run_dir / DEFAULT_CONFIG
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")
    with config_path.open("r", encoding="utf-8") as file:
        config = json.load(file)
    if not isinstance(config, dict):
        raise ValueError(f"{config_path} must contain a JSON object")
    return config


def save_config(run_dir: Path, config: dict[str, Any]) -> None:
    config_path = run_dir / DEFAULT_CONFIG
    with config_path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(config, file, ensure_ascii=False, indent=2)
        file.write("\n")


def init_run(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir) if args.run_dir else default_run_dir()
    source_path = Path(args.input)
    if not source_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {source_path}")

    run_dir.mkdir(parents=True, exist_ok=True)
    target_csv = run_dir / DEFAULT_INPUT_COPY
    if target_csv.exists() and not args.overwrite:
        print(f"Keeping existing input copy: {target_csv}")
    else:
        shutil.copy2(source_path, target_csv)
        print(f"Copied source CSV to {target_csv}")

    env_path = Path(args.env_file)
    config = build_default_config(run_dir, env_path, args.first_model, args.second_model)
    config_path = run_dir / DEFAULT_CONFIG
    if config_path.exists() and not args.overwrite:
        print(f"Keeping existing config: {config_path}")
    else:
        save_config(run_dir, config)
        print(f"Wrote config: {config_path}")

    write_text_if_allowed(run_dir / DEFAULT_SYSTEM_PROMPT, CODING_AGENT_UX_SYSTEM_PROMPT, args.overwrite)
    write_text_if_allowed(run_dir / DEFAULT_USER_PROMPT, CODING_AGENT_UX_USER_PROMPT, args.overwrite)
    print(f"Wrote prompts: {run_dir / DEFAULT_SYSTEM_PROMPT}, {run_dir / DEFAULT_USER_PROMPT}")
    print("Next: preview the prompts if needed, then run the screening.")
    return 0


def output_paths(run_dir: Path, config: dict[str, Any]) -> dict[str, Path]:
    outputs = config.get("outputs", {})
    if not isinstance(outputs, dict):
        raise ValueError("config.outputs must be an object")
    required = [
        "all_screened_csv",
        "included_csv",
        "disagreements_csv",
        "progress_jsonl",
        "decisions_jsonl",
        "errors_jsonl",
    ]
    missing = [key for key in required if key not in outputs]
    if missing:
        raise ValueError(f"Missing output config keys: {', '.join(missing)}")
    return {key: resolve_run_path(run_dir, str(outputs[key])) for key in required}  # type: ignore[return-value]


def load_prompts(run_dir: Path, config: dict[str, Any]) -> tuple[str, str]:
    prompt_files = config.get("prompt_files", {})
    if not isinstance(prompt_files, dict):
        raise ValueError("config.prompt_files must be an object")
    system_path = resolve_run_path(run_dir, normalize_cell(prompt_files.get("system")))
    user_path = resolve_run_path(run_dir, normalize_cell(prompt_files.get("user_template")))
    if system_path is None or user_path is None:
        raise ValueError("Both system and user prompt files must be configured")
    return system_path.read_text(encoding="utf-8"), user_path.read_text(encoding="utf-8")


def model_specs(config: dict[str, Any]) -> list[ModelSpec]:
    raw_models = config.get("models", [])
    if not isinstance(raw_models, list):
        raise ValueError("config.models must be a list")
    specs: list[ModelSpec] = []
    for raw_model in raw_models:
        if not isinstance(raw_model, dict):
            raise ValueError("Each configured model must be an object")
        enabled = bool(raw_model.get("enabled", True))
        spec = ModelSpec(
            name=normalize_cell(raw_model.get("name")) or normalize_cell(raw_model.get("model")),
            model=normalize_cell(raw_model.get("model")),
            api_key_env=normalize_cell(raw_model.get("api_key_env")),
            base_url_env=normalize_cell(raw_model.get("base_url_env")) or None,
            base_url=normalize_cell(raw_model.get("base_url")) or None,
            enabled=enabled,
            timeout=float(raw_model.get("timeout", 90.0)),
            max_tokens=int(raw_model.get("max_tokens", 420)),
            temperature=float(raw_model.get("temperature", 0)),
            response_format=raw_model.get("response_format"),
        )
        if spec.enabled:
            missing = []
            if not spec.name:
                missing.append("name")
            if not spec.model:
                missing.append("model")
            if not spec.api_key_env:
                missing.append("api_key_env")
            if missing:
                raise ValueError(f"Enabled model is missing: {', '.join(missing)}")
            specs.append(spec)
    if len(specs) < 2:
        raise ValueError("Enable at least two models for dual-model screening")
    return specs


def build_row_key(
    row: dict[str, str],
    row_number: int,
    id_column: str,
    title: str,
    abstract: str,
    row_key_mode: str,
) -> str:
    explicit_id = normalize_cell(row.get(id_column, ""))
    if explicit_id:
        if row_key_mode == "id_with_row_number":
            return f"{explicit_id}::row-{row_number}"
        return explicit_id
    digest = hashlib.sha256(f"{row_number}\n{title}\n{abstract}".encode("utf-8")).hexdigest()[:16]
    return f"row-{row_number}-{digest}"


def load_items(
    input_path: Path,
    title_column: str,
    abstract_column: str,
    id_column: str,
    row_key_mode: str,
    encoding: str,
    offset: int,
) -> tuple[list[str], list[ScreenItem]]:
    with input_path.open("r", encoding=encoding, newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError(f"{input_path} has no header row")
        missing_columns = [name for name in (title_column, abstract_column) if name not in reader.fieldnames]
        if missing_columns:
            raise ValueError(f"Missing required CSV columns: {', '.join(missing_columns)}")

        items: list[ScreenItem] = []
        for row_number, row in enumerate(reader, start=2):
            if row_number - 2 < offset:
                continue
            clean_row = {key: normalize_cell(value) for key, value in row.items() if key is not None}
            title = normalize_cell(clean_row.get(title_column, ""))
            abstract = normalize_cell(clean_row.get(abstract_column, ""))
            row_key = build_row_key(clean_row, row_number, id_column, title, abstract, row_key_mode)
            items.append(ScreenItem(row_number=row_number, row_key=row_key, row=clean_row, title=title, abstract=abstract))
    return list(reader.fieldnames), items


def load_processed_keys(progress_path: Path, all_screened_path: Path, encoding: str) -> set[str]:
    processed: set[str] = set()
    if progress_path.exists():
        with progress_path.open("r", encoding="utf-8", newline="") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    payload = json.loads(line)
                except json.JSONDecodeError:
                    continue
                row_key = normalize_cell(payload.get("row_key"))
                if row_key:
                    processed.add(row_key)

    if not processed and all_screened_path.exists():
        with all_screened_path.open("r", encoding=encoding, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row_key = normalize_cell(row.get("screen_row_key"))
                if row_key:
                    processed.add(row_key)
    return processed


def prompt_context(item: ScreenItem) -> dict[str, str]:
    return {
        "row_key": item.row_key,
        "row_number": str(item.row_number),
        "title": item.title or "(empty)",
        "abstract": item.abstract or "(empty)",
        "year": normalize_cell(item.row.get("Year")) or "(empty)",
        "source_title": normalize_cell(item.row.get("Source title")) or "(empty)",
        "document_type": normalize_cell(item.row.get("Document Type")) or "(empty)",
        "author_keywords": normalize_cell(item.row.get("Author Keywords")) or "(empty)",
        "index_keywords": normalize_cell(item.row.get("Index Keywords")) or "(empty)",
    }


def render_user_prompt(template: str, item: ScreenItem) -> str:
    try:
        return template.format(**prompt_context(item))
    except KeyError as exc:
        raise ValueError(f"Unknown placeholder in user prompt template: {exc}") from exc


def parse_model_json(content: str) -> tuple[bool, float, str, str, str, str, str, str, str, str, str, str]:
    if not content or not content.strip():
        raise ValueError("empty model response")
    text = content.strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            raise
        payload = json.loads(text[start : end + 1])

    if not isinstance(payload, dict):
        raise ValueError("model response is not a JSON object")
    relevant = payload.get("relevant")
    if not isinstance(relevant, bool):
        raise ValueError("JSON field 'relevant' must be boolean")
    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    confidence = max(0.0, min(1.0, confidence))
    decision_label = normalize_cell(payload.get("decision_label", ""))
    fit_level = normalize_cell(payload.get("fit_level", ""))
    source_concept = normalize_cell(payload.get("source_concept", ""))
    candidate_coding_agent_ux_concept = normalize_cell(payload.get("candidate_coding_agent_ux_concept", ""))
    ux_topic = normalize_cell(payload.get("ux_topic", ""))
    adaptation_potential = normalize_cell(payload.get("adaptation_potential", ""))
    practical_importance = normalize_cell(payload.get("practical_importance", ""))
    uniqueness_rationale = normalize_cell(payload.get("uniqueness_rationale", ""))
    evidence = normalize_cell(payload.get("evidence", ""))
    reason = normalize_cell(payload.get("reason", ""))
    return (
        relevant,
        confidence,
        decision_label,
        fit_level,
        source_concept,
        candidate_coding_agent_ux_concept,
        ux_topic,
        adaptation_potential,
        practical_importance,
        uniqueness_rationale,
        evidence,
        reason,
    )


async def classify_with_retries(
    item: ScreenItem,
    spec: ModelSpec,
    llm: Any,
    semaphore: asyncio.Semaphore,
    system_prompt: str,
    user_prompt_template: str,
    retries: int,
    retry_base_delay: float,
) -> ModelDecision:
    last_error: BaseException | None = None
    user_prompt = render_user_prompt(user_prompt_template, item)
    for attempt in range(retries + 1):
        try:
            async with semaphore:
                response = await llm.ainvoke(
                    [
                        ("system", system_prompt),
                        ("user", user_prompt),
                    ]
                )
            raw_response = response.content if isinstance(response.content, str) else json.dumps(response.content)
            (
                relevant,
                confidence,
                decision_label,
                fit_level,
                source_concept,
                candidate_coding_agent_ux_concept,
                ux_topic,
                adaptation_potential,
                practical_importance,
                uniqueness_rationale,
                evidence,
                reason,
            ) = parse_model_json(raw_response)
            return ModelDecision(
                model_name=spec.name,
                model=spec.model,
                relevant=relevant,
                confidence=confidence,
                decision_label=decision_label,
                fit_level=fit_level,
                source_concept=source_concept,
                candidate_coding_agent_ux_concept=candidate_coding_agent_ux_concept,
                ux_topic=ux_topic,
                adaptation_potential=adaptation_potential,
                practical_importance=practical_importance,
                uniqueness_rationale=uniqueness_rationale,
                evidence=evidence,
                reason=reason,
                raw_response=raw_response,
            )
        except Exception as exc:
            last_error = exc
            if attempt >= retries:
                break
            sleep_seconds = retry_base_delay * (2**attempt) + random.uniform(0, 0.5)
            await asyncio.sleep(sleep_seconds)
    assert last_error is not None
    raise last_error


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="") as file:
        file.write(json.dumps(payload, ensure_ascii=False) + "\n")
        file.flush()
        os.fsync(file.fileno())


def ensure_csv_writer(output_path: Path, fieldnames: list[str], encoding: str) -> tuple[Any, csv.DictWriter]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    file_exists = output_path.exists() and output_path.stat().st_size > 0
    file = output_path.open("a", encoding=encoding, newline="")
    writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
    if not file_exists:
        writer.writeheader()
        file.flush()
        os.fsync(file.fileno())
    return file, writer


def write_csv_row(file: Any, writer: csv.DictWriter, row: dict[str, str]) -> None:
    writer.writerow(row)
    file.flush()
    os.fsync(file.fileno())


def build_output_fieldnames(input_fieldnames: list[str], specs: list[ModelSpec]) -> list[str]:
    extra = [
        "screen_row_key",
        "screen_row_number",
        "screen_completed_at",
        "screen_model_count",
        "screen_agreement",
        "screen_relevant_consensus",
        "screen_any_relevant",
        "screen_decision_summary",
    ]
    for spec in specs:
        slug = slugify(spec.name)
        extra.extend(
            [
                f"{slug}_model",
                f"{slug}_relevant",
                f"{slug}_confidence",
                f"{slug}_decision_label",
                f"{slug}_fit_level",
                f"{slug}_source_concept",
                f"{slug}_candidate_coding_agent_ux_concept",
                f"{slug}_ux_topic",
                f"{slug}_adaptation_potential",
                f"{slug}_practical_importance",
                f"{slug}_uniqueness_rationale",
                f"{slug}_evidence",
                f"{slug}_reason",
            ]
        )
    return input_fieldnames + [name for name in extra if name not in input_fieldnames]


def decisions_payload(item: ScreenItem, decisions: list[ModelDecision]) -> dict[str, Any]:
    relevant_values = [decision.relevant for decision in decisions]
    agreement = all(value == relevant_values[0] for value in relevant_values)
    return {
        "ts": utc_now(),
        "row_number": item.row_number,
        "row_key": item.row_key,
        "title": item.title,
        "agreement": agreement,
        "relevant_consensus": agreement and all(relevant_values),
        "any_relevant": any(relevant_values),
        "decisions": [
            {
                "model_name": decision.model_name,
                "model": decision.model,
                "relevant": decision.relevant,
                "confidence": decision.confidence,
                "decision_label": decision.decision_label,
                "fit_level": decision.fit_level,
                "source_concept": decision.source_concept,
                "candidate_coding_agent_ux_concept": decision.candidate_coding_agent_ux_concept,
                "ux_topic": decision.ux_topic,
                "adaptation_potential": decision.adaptation_potential,
                "practical_importance": decision.practical_importance,
                "uniqueness_rationale": decision.uniqueness_rationale,
                "evidence": decision.evidence,
                "reason": decision.reason,
                "raw_response": decision.raw_response,
            }
            for decision in decisions
        ],
    }


def csv_output_row(item: ScreenItem, decisions: list[ModelDecision]) -> dict[str, str]:
    payload = decisions_payload(item, decisions)
    output = dict(item.row)
    output.update(
        {
            "screen_row_key": item.row_key,
            "screen_row_number": str(item.row_number),
            "screen_completed_at": payload["ts"],
            "screen_model_count": str(len(decisions)),
            "screen_agreement": str(payload["agreement"]).lower(),
            "screen_relevant_consensus": str(payload["relevant_consensus"]).lower(),
            "screen_any_relevant": str(payload["any_relevant"]).lower(),
            "screen_decision_summary": "; ".join(
                f"{decision.model_name}={str(decision.relevant).lower()}({decision.confidence:.2f})"
                for decision in decisions
            ),
        }
    )
    for decision in decisions:
        slug = slugify(decision.model_name)
        output.update(
            {
                f"{slug}_model": decision.model,
                f"{slug}_relevant": str(decision.relevant).lower(),
                f"{slug}_confidence": f"{decision.confidence:.3f}",
                f"{slug}_decision_label": decision.decision_label,
                f"{slug}_fit_level": decision.fit_level,
                f"{slug}_source_concept": decision.source_concept,
                f"{slug}_candidate_coding_agent_ux_concept": decision.candidate_coding_agent_ux_concept,
                f"{slug}_ux_topic": decision.ux_topic,
                f"{slug}_adaptation_potential": decision.adaptation_potential,
                f"{slug}_practical_importance": decision.practical_importance,
                f"{slug}_uniqueness_rationale": decision.uniqueness_rationale,
                f"{slug}_evidence": decision.evidence,
                f"{slug}_reason": decision.reason,
            }
        )
    return output


def create_llm(spec: ModelSpec) -> Any:
    api_key = os.getenv(spec.api_key_env)
    if not api_key:
        raise RuntimeError(f"API key not found for {spec.name}. Set {spec.api_key_env}.")
    base_url = spec.base_url
    if spec.base_url_env:
        base_url = os.getenv(spec.base_url_env) or base_url

    kwargs: dict[str, Any] = {
        "model": spec.model,
        "api_key": api_key,
        "timeout": spec.timeout,
        "max_tokens": spec.max_tokens,
        "temperature": spec.temperature,
    }
    if base_url:
        kwargs["base_url"] = base_url
    llm = ChatOpenAI(**kwargs)
    if spec.response_format:
        llm = llm.bind(response_format=spec.response_format)
    return llm


def load_run_data(
    run_dir: Path,
    config: dict[str, Any],
    offset: int,
) -> tuple[list[str], list[ScreenItem]]:
    input_path = resolve_run_path(run_dir, normalize_cell(config.get("input_file")))
    if input_path is None:
        raise ValueError("config.input_file is required")
    return load_items(
        input_path=input_path,
        title_column=normalize_cell(config.get("title_column")) or "Title",
        abstract_column=normalize_cell(config.get("abstract_column")) or "Abstract",
        id_column=normalize_cell(config.get("id_column")) or "EID",
        row_key_mode=normalize_cell(config.get("row_key_mode")) or "id_only",
        encoding=normalize_cell(config.get("encoding")) or DEFAULT_ENCODING,
        offset=offset,
    )


def preview_prompts(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    config = load_config(run_dir)
    system_prompt, user_prompt_template = load_prompts(run_dir, config)
    print("\n=== SYSTEM PROMPT ===\n")
    print(system_prompt.rstrip())
    print("\n=== USER PROMPT TEMPLATE ===\n")
    print(user_prompt_template.rstrip())

    if args.examples:
        _, items = load_run_data(run_dir, config, offset=0)
        for item in items[: args.examples]:
            print(f"\n=== RENDERED USER PROMPT EXAMPLE: row {item.row_number} ===\n")
            print(render_user_prompt(user_prompt_template, item).rstrip())

    return 0


async def run_screening(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    config = load_config(run_dir)
    system_prompt, user_prompt_template = load_prompts(run_dir, config)
    paths = output_paths(run_dir, config)
    encoding = normalize_cell(config.get("encoding")) or DEFAULT_ENCODING
    specs = model_specs(config)

    if args.reset and args.dry_run:
        print("DRY RUN: --reset was ignored.")
    elif args.reset:
        for path in paths.values():
            if path.exists():
                path.unlink()

    input_fieldnames, all_items = load_run_data(run_dir, config, offset=args.offset)
    processed_keys = load_processed_keys(paths["progress_jsonl"], paths["all_screened_csv"], encoding)
    pending_items = [item for item in all_items if item.row_key not in processed_keys]
    if args.limit is not None:
        pending_items = pending_items[: args.limit]

    print(
        f"Loaded {len(all_items)} rows after offset; "
        f"{len(processed_keys)} already processed; {len(pending_items)} pending."
    )
    print("Models:", ", ".join(f"{spec.name} ({spec.model})" for spec in specs))
    print(f"Run directory: {run_dir}")

    if args.dry_run:
        for item in pending_items[:5]:
            print(f"DRY RUN row={item.row_number} key={item.row_key} title={item.title[:120]}")
        return 0

    if not pending_items:
        print("Nothing to do.")
        return 0

    env_file = resolve_run_path(run_dir, normalize_cell(config.get("env_file")))
    if env_file is not None:
        load_dotenv(env_file)
        print(f"Loaded env file: {env_file}")

    screening = config.get("screening", {})
    if not isinstance(screening, dict):
        raise ValueError("config.screening must be an object")
    max_concurrency = int(screening.get("max_concurrency", 4))
    retries = int(screening.get("retries", 3))
    retry_base_delay = float(screening.get("retry_base_delay", 2.0))

    llms = {spec.name: create_llm(spec) for spec in specs}
    semaphore = asyncio.Semaphore(max_concurrency)
    output_fieldnames = build_output_fieldnames(input_fieldnames, specs)

    all_file, all_writer = ensure_csv_writer(paths["all_screened_csv"], output_fieldnames, encoding)
    included_file, included_writer = ensure_csv_writer(paths["included_csv"], output_fieldnames, encoding)
    disagreements_file, disagreements_writer = ensure_csv_writer(paths["disagreements_csv"], output_fieldnames, encoding)

    started_at = time.monotonic()
    completed = 0
    included_count = 0
    disagreement_count = 0
    failed_count = 0

    async def classify_one_row(
        item: ScreenItem,
    ) -> tuple[ScreenItem, list[ModelDecision] | None, dict[str, BaseException]]:
        tasks = [
            classify_with_retries(
                item=item,
                spec=spec,
                llm=llms[spec.name],
                semaphore=semaphore,
                system_prompt=system_prompt,
                user_prompt_template=user_prompt_template,
                retries=retries,
                retry_base_delay=retry_base_delay,
            )
            for spec in specs
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        errors: dict[str, BaseException] = {}
        decisions: list[ModelDecision] = []
        for spec, result in zip(specs, results, strict=True):
            if isinstance(result, BaseException):
                errors[spec.name] = result
            else:
                decisions.append(result)
        if errors:
            return item, None, errors
        return item, decisions, {}

    try:
        tasks = [asyncio.create_task(classify_one_row(item)) for item in pending_items]
        for finished in asyncio.as_completed(tasks):
            item, decisions, errors = await finished
            completed += 1
            if errors:
                failed_count += 1
                append_jsonl(
                    paths["errors_jsonl"],
                    {
                        "ts": utc_now(),
                        "row_number": item.row_number,
                        "row_key": item.row_key,
                        "title": item.title,
                        "errors": {
                            model_name: {
                                "error_type": type(error).__name__,
                                "error": str(error),
                            }
                            for model_name, error in errors.items()
                        },
                    },
                )
            elif decisions is not None:
                payload = decisions_payload(item, decisions)
                output_row = csv_output_row(item, decisions)
                write_csv_row(all_file, all_writer, output_row)
                append_jsonl(paths["progress_jsonl"], payload)
                for decision in decisions:
                    append_jsonl(
                        paths["decisions_jsonl"],
                        {
                            "ts": payload["ts"],
                            "row_number": item.row_number,
                            "row_key": item.row_key,
                            "model_name": decision.model_name,
                            "model": decision.model,
                            "relevant": decision.relevant,
                            "confidence": decision.confidence,
                            "decision_label": decision.decision_label,
                            "fit_level": decision.fit_level,
                            "source_concept": decision.source_concept,
                            "candidate_coding_agent_ux_concept": decision.candidate_coding_agent_ux_concept,
                            "ux_topic": decision.ux_topic,
                            "adaptation_potential": decision.adaptation_potential,
                            "practical_importance": decision.practical_importance,
                            "uniqueness_rationale": decision.uniqueness_rationale,
                            "evidence": decision.evidence,
                            "reason": decision.reason,
                            "raw_response": decision.raw_response,
                        },
                    )
                if payload["relevant_consensus"]:
                    included_count += 1
                    write_csv_row(included_file, included_writer, output_row)
                if not payload["agreement"]:
                    disagreement_count += 1
                    write_csv_row(disagreements_file, disagreements_writer, output_row)

            if completed == 1 or completed % 10 == 0 or completed == len(pending_items):
                elapsed = time.monotonic() - started_at
                print(
                    f"Completed {completed}/{len(pending_items)}; "
                    f"included={included_count}; disagreements={disagreement_count}; "
                    f"failed={failed_count}; elapsed={elapsed:.1f}s"
                )
    finally:
        all_file.close()
        included_file.close()
        disagreements_file.close()

    print(
        f"Done. Consensus inclusions: {paths['included_csv']}. "
        f"Disagreements: {paths['disagreements_csv']}. "
        f"All screened rows: {paths['all_screened_csv']}."
    )
    return 0 if failed_count == 0 else 2


def main() -> None:
    configure_stdio()
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "init":
            raise SystemExit(init_run(args))
        if args.command == "preview":
            raise SystemExit(preview_prompts(args))
        if args.command == "run":
            raise SystemExit(asyncio.run(run_screening(args)))
        parser.error(f"Unknown command: {args.command}")
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        raise SystemExit(130)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
