#!/usr/bin/env python3
"""Reclassify data publicness for strict_include papers under v3 criteria."""
from __future__ import annotations

import concurrent.futures
import json
import os
import random
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

RUN_DIR = Path(__file__).resolve().parent
CONFIG_PATH = RUN_DIR / "config.json"
OUTPUT_DIR = RUN_DIR / "output_v1"
DECISIONS = OUTPUT_DIR / "decisions.jsonl"
INPUT_DIR = (RUN_DIR / "../../database_fulltext_all").resolve()
ALLOWED = {"public", "private_or_nonpublic", "synthetic", "mixed", "unclear"}

SYSTEM_PROMPT = """你是极其保守、只依据全文证据裁决的 IS 文献审计员。每个请求包含一篇完整文章。你的唯一任务是判定该文章主要数据的数据公开性，不判断其他任何内容。

判定口径（v3）：
- public：主要数据在发表时可通过公开渠道获取，包括：公开数据集、公开 API、公开网络爬取、政府或监管公开数据、公开市场数据，以及可通过正式申请/许可程序获取的数据（如学术许可数据、研究申请数据、VirusTotal 学术许可样本等「申请即得」渠道）。
- private_or_nonpublic：主要数据无法通过任何公开渠道或申请程序获取（企业专有数据、内部系统日志、执法或保密数据、明确协议禁止共享的数据、拒绝外部研究者访问的商业专有数据）。
- synthetic：主要数据全部为研究者自建的合成/仿真数据（随机生成、数值模拟、自设参数仿真），无真实数据源，不涉及公开性。
- mixed：上述类别混合（如公开数据集+内部数据，或公开+合成）。
- unclear：全文无法判断。

判断依据应来自全文对数据来源的描述（数据收集章节、数据集描述、致谢、可用性声明等）。只输出一个合法 JSON 对象：

{
  "record_id": "原样复制record_id",
  "data_publicness": {
    "status": "public | private_or_nonpublic | synthetic | mixed | unclear",
    "data_sources_cn": "主要数据来源一句话",
    "reason_cn": "一句判定理由（引用证据）"
  }
}"""

USER_TEMPLATE = """请判定以下完整文章的数据公开性：

- record_id：{record_id}
- 标题：{title}
- 作者：{authors}
- 年份：{year}
- 期刊：{journal}
- DOI：{doi}
- 本地全文文件：{source_file}

<FULLTEXT>
{fulltext}
</FULLTEXT>

严格依照系统提示词，只输出一个合法 JSON 对象。"""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return {}, normalized
    end = normalized.find("\n---\n", 4)
    if end < 0:
        return {}, normalized
    metadata: dict[str, Any] = {}
    for line in normalized[4:end].splitlines():
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        raw_value = raw_value.strip()
        try:
            metadata[key.strip()] = json.loads(raw_value)
        except json.JSONDecodeError:
            metadata[key.strip()] = raw_value
    return metadata, normalized[end + 5 :].lstrip()


def metadata_for(path: Path, fulltext: str, frontmatter: dict[str, Any]) -> dict[str, str]:
    parts = path.name.split("_", 2)
    return {
        "record_id": str(frontmatter.get("otero_id") or (parts[0].lstrip("0") or "0")),
        "source_file": path.name,
        "title": str(frontmatter.get("title") or path.stem),
        "authors": str(frontmatter.get("authors") or ""),
        "year": str(frontmatter.get("year") or ""),
        "journal": str(frontmatter.get("journal") or ""),
        "doi": str(frontmatter.get("doi") or ""),
    }


def parse_json_object(content: str) -> dict[str, Any]:
    text = (content or "").strip()
    if not text:
        raise ValueError("empty model response")
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise
        payload = json.loads(text[start : end + 1])
    if not isinstance(payload, dict):
        raise ValueError("not a JSON object")
    return payload


def validate(payload: dict[str, Any], record_id: str) -> dict[str, Any]:
    if str(payload.get("record_id") or "").strip() != record_id:
        raise ValueError("record_id mismatch")
    pub = payload.get("data_publicness")
    if not isinstance(pub, dict):
        raise ValueError("data_publicness must be an object")
    status = str(pub.get("status") or "")
    if status not in ALLOWED:
        raise ValueError(f"invalid status: {status!r}")
    return payload


class ThreadClients:
    def __init__(self, api_key: str, base_url: str, timeout: float):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.local = threading.local()

    def get(self) -> OpenAI:
        client = getattr(self.local, "client", None)
        if client is None:
            client = OpenAI(api_key=self.api_key, base_url=self.base_url, timeout=self.timeout)
            self.local.client = client
        return client


def analyze_one(path: Path, clients: ThreadClients, config: dict[str, Any],
                system_prompt: str, user_template: str) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, fulltext = parse_frontmatter(raw)
    meta = metadata_for(path, fulltext, frontmatter)
    user_prompt = user_template.format(**meta, fulltext=fulltext)
    model, batch = config["model"], config["batch"]
    last_error: BaseException | None = None
    for attempt in range(1, int(batch["retries"]) + 2):
        try:
            response = clients.get().chat.completions.create(
                model=str(model["name"]),
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=float(model["temperature"]),
                max_tokens=None if not model.get("max_tokens") else int(model["max_tokens"]),
                response_format={"type": "json_object"},
            )
            choice = response.choices[0]
            content = choice.message.content or getattr(choice.message, "reasoning_content", None) or ""
            if not content.strip():
                raise ValueError("empty response")
            decision = validate(parse_json_object(content), meta["record_id"])
            return {**meta, "data_publicness": decision["data_publicness"], "attempts": attempt}
        except Exception as exc:
            last_error = exc
            if attempt > int(batch["retries"]):
                break
            delay = float(batch["retry_base_delay_seconds"]) * (2 ** (attempt - 1))
            time.sleep(delay + random.uniform(0, 0.5))
    assert last_error is not None
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}") from last_error


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def main() -> int:
    config = load_config()
    model, batch = config["model"], config["batch"]
    rows = []
    with DECISIONS.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("strict_include") is True:
                rows.append(row)
    output_path = OUTPUT_DIR / "data_publicness_v3.jsonl"
    done = {}
    if output_path.exists():
        with output_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                done[item["record_id"]] = item
    pending = [r for r in rows if r["record_id"] not in done]
    print(f"passed={len(rows)} done={len(done)} pending={len(pending)} model={model['name']}", flush=True)
    if not pending:
        print("nothing to do", flush=True)
        return 0
    load_dotenv((RUN_DIR / "../../.env").resolve())
    api_key = os.getenv(str(model["api_key_env"]))
    if not api_key:
        raise RuntimeError("missing API key")
    base_url = os.getenv(str(model["base_url_env"])) or str(model["base_url"])
    clients = ThreadClients(api_key, base_url, float(model["timeout_seconds"]))
    system_prompt = SYSTEM_PROMPT.strip()
    user_template = USER_TEMPLATE.strip()
    started = time.monotonic()
    completed = failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(batch["max_concurrency"])) as pool:
        futures = {
            pool.submit(analyze_one, INPUT_DIR / r["source_file"], clients, config,
                        system_prompt, user_template): r
            for r in pending
        }
        for future in concurrent.futures.as_completed(futures):
            row = futures[future]
            try:
                result = future.result()
                append_jsonl(output_path, result)
                done[result["record_id"]] = result
                completed += 1
            except Exception as exc:
                failed += 1
                print(f"ERROR file={row.get('source_file')} error={exc}", flush=True)
            if (completed + failed) % 10 == 0:
                elapsed = time.monotonic() - started
                print(f"progress={completed + failed}/{len(pending)} ok={completed} failed={failed} "
                      f"rate={(completed + failed) / elapsed if elapsed else 0:.2f}/s", flush=True)
    elapsed = time.monotonic() - started
    print(f"finished ok={completed} failed={failed} elapsed_seconds={elapsed:.1f}", flush=True)
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    sys.exit(main())

