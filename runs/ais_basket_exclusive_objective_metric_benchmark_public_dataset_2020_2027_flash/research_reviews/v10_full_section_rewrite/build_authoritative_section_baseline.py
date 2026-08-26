from __future__ import annotations

import hashlib
import re
import statistics
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
OUT_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class SectionSpec:
    label: str
    start: int
    end: int


@dataclass(frozen=True)
class SourceSpec:
    code: str
    path: str
    role: str
    sections: tuple[SectionSpec, ...]


SOURCES = (
    SourceSpec(
        "ACAA-2024-ISR",
        "database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md",
        "肖老师主范式；多模态构念到注意机制的理论—算法映射",
        (
            SectionSpec("引言", 37, 56),
            SectionSpec("文献综述", 57, 88),
            SectionSpec("定位、设计理据与方法挑战", 89, 123),
            SectionSpec("所提方法", 124, 225),
            SectionSpec("实证评价", 226, 315),
            SectionSpec("贡献与启示", 316, 343),
            SectionSpec("结论", 344, 349),
        ),
    ),
    SourceSpec(
        "DSDL-2023-ISR",
        "database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md",
        "肖老师主范式；情境构念、方法挑战、模型组件和解释分析的闭环",
        (
            SectionSpec("引言", 33, 54),
            SectionSpec("文献综述", 55, 80),
            SectionSpec("理论基础与方法挑战", 81, 96),
            SectionSpec("所提方法", 97, 228),
            SectionSpec("实证评价", 229, 296),
            SectionSpec("解释分析", 297, 312),
            SectionSpec("贡献与启示", 313, 336),
            SectionSpec("结论", 337, 344),
        ),
    ),
    SourceSpec(
        "RADAR-2025-MISQ",
        "database_fulltext_all/27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md",
        "安全算法辅范式；攻击模拟、鲁棒化和同条件技术评价",
        (
            SectionSpec("引言", 29, 40),
            SectionSpec("研究背景与研究问题", 41, 117),
            SectionSpec("所提设计及实例化", 118, 209),
            SectionSpec("评价", 210, 300),
            SectionSpec("讨论", 301, 310),
            SectionSpec("结论、局限与未来研究", 311, 316),
        ),
    ),
    SourceSpec(
        "ARText-2022-JMIS",
        "database_fulltext_all/25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md",
        "安全算法辅范式；评估—增强框架、技术新颖性和多实验组织",
        (
            SectionSpec("引言", 61, 70),
            SectionSpec("研究背景", 71, 112),
            SectionSpec("鲁棒性评估与增强框架", 113, 156),
            SectionSpec("系统设计", 157, 236),
            SectionSpec("实验评价", 237, 322),
            SectionSpec("讨论", 323, 337),
            SectionSpec("结论", 338, 345),
        ),
    ),
    SourceSpec(
        "MegaFake-2026-DSS",
        "database_fulltext_all/16604_2026_megafake-a-theory-driven-dataset-of-fake-news-generated-by-large-language-models.md",
        "研究一辅范式；理论驱动攻击内容分类、数据构造和跨域评价",
        (
            SectionSpec("引言", 27, 42),
            SectionSpec("相关研究", 43, 72),
            SectionSpec("LLM-Fake理论", 73, 108),
            SectionSpec("数据集构建", 109, 149),
            SectionSpec("实验", 150, 302),
            SectionSpec("讨论与结论", 303, 318),
        ),
    ),
    SourceSpec(
        "SIGHT-2020-JMIS",
        "database_fulltext_all/01598_2020_design-principles-for-signal-detection-in-modern-job-application-systems-identifying-fabricated.md",
        "研究二辅范式；信号理论、难操纵多模态信号和标准化融合",
        (
            SectionSpec("引言", 67, 80),
            SectionSpec("研究方法", 81, 86),
            SectionSpec("信号理论与设计原则", 87, 164),
            SectionSpec("原型实现", 165, 205),
            SectionSpec("方法", 206, 233),
            SectionSpec("分析与结果", 234, 274),
            SectionSpec("讨论", 275, 292),
            SectionSpec("局限与结论", 293, 304),
        ),
    ),
    SourceSpec(
        "G-FINDER-2024-ISR",
        "database_fulltext_all/27953_2024_explainable-deep-learning-for-false-information-identification-an-argumentation-theory-approach.md",
        "研究二辅范式；理论构件进入可解释识别模型并分实验评价性能与解释",
        (
            SectionSpec("引言", 33, 52),
            SectionSpec("相关研究与理论", 53, 113),
            SectionSpec("方法", 114, 150),
            SectionSpec("实验", 151, 241),
            SectionSpec("结语与未来研究", 242, 251),
        ),
    ),
    SourceSpec(
        "PFM-2021-ISR",
        "database_fulltext_all/28020_2021_the-phishing-funnel-model-a-design-artifact-to-predict-user-susceptibility-to-phishing-websites.md",
        "研究二、三辅范式；执行前易感性预测与预测引导干预的分离评价",
        (
            SectionSpec("引言", 37, 62),
            SectionSpec("相关研究", 63, 72),
            SectionSpec("模型与预测方法", 73, 176),
            SectionSpec("预测实验", 177, 305),
            SectionSpec("干预实验", 306, 362),
            SectionSpec("结果讨论与结语", 363, 402),
        ),
    ),
    SourceSpec(
        "DTL-EL-2024-MISQ",
        "database_fulltext_all/11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md",
        "安全算法辅范式；稀缺安全标签、计算设计科学和多基线实验",
        (
            SectionSpec("引言", 35, 56),
            SectionSpec("文献综述", 57, 88),
            SectionSpec("方法基础", 89, 116),
            SectionSpec("测试床与设计", 117, 184),
            SectionSpec("实验与评价", 185, 227),
            SectionSpec("结果与讨论", 228, 293),
            SectionSpec("实践启示与知识贡献", 294, 317),
            SectionSpec("结论", 318, 325),
        ),
    ),
    SourceSpec(
        "Controlled-Diffusion-2023-MISQ",
        "database_fulltext_all/15468_2023_responding-to-online-reviews-in-competitive-markets-a-controlled-diffusion-approach.md",
        "研究三辅范式；现代最优控制问题、状态—控制—动态—价值函数写法",
        (
            SectionSpec("引言", 25, 40),
            SectionSpec("文献综述", 41, 66),
            SectionSpec("模型与最优控制问题", 67, 169),
            SectionSpec("数据", 170, 194),
            SectionSpec("估计与结果", 195, 282),
            SectionSpec("启示", 283, 346),
            SectionSpec("结论", 347, 378),
        ),
    ),
    SourceSpec(
        "Dynamic-Control-2026-ISR",
        "database_fulltext_all/28642_2026_optimal-dynamic-advertising-policies-in-digital-and-traditional-channels-a-control-theoretic-app.md",
        "研究三辅范式；近年控制理论文章的模型、政策、敏感性和扩展结构",
        (
            SectionSpec("引言", 33, 52),
            SectionSpec("文献综述", 53, 74),
            SectionSpec("基础模型", 75, 134),
            SectionSpec("最优政策", 135, 216),
            SectionSpec("敏感性分析", 217, 274),
            SectionSpec("模型扩展", 275, 409),
            SectionSpec("结语", 410, 435),
        ),
    ),
)


def prose_blocks(lines: list[str]) -> list[str]:
    blocks: list[str] = []
    current: list[str] = []
    in_code = False

    def flush() -> None:
        nonlocal current
        text = " ".join(part.strip() for part in current if part.strip()).strip()
        current = []
        if not text:
            return
        if text.startswith(("#", "![]", "<table", "</table", "Table ", "Figure ")):
            return
        if text.startswith(("$$", "\\[", "\\begin{")):
            return
        if re.fullmatch(r"[|:\-\s]+", text):
            return
        blocks.append(text)

    for raw in lines:
        line = raw.rstrip()
        if line.strip().startswith("```"):
            flush()
            in_code = not in_code
            continue
        if in_code:
            continue
        if not line.strip():
            flush()
            continue
        if line.startswith("##"):
            flush()
            continue
        current.append(line)
    flush()
    return blocks


def split_sentences(text: str) -> list[str]:
    protected = text
    replacements = {
        "et al.": "et al<prd>",
        "e.g.": "e<prd>g<prd>",
        "i.e.": "i<prd>e<prd>",
        "Fig.": "Fig<prd>",
        "Eq.": "Eq<prd>",
        "Eqs.": "Eqs<prd>",
        "Dr.": "Dr<prd>",
        "Mr.": "Mr<prd>",
        "Ms.": "Ms<prd>",
        "vs.": "vs<prd>",
    }
    for old, new in replacements.items():
        protected = protected.replace(old, new)
    protected = re.sub(r"\b([A-Z])\.(?=[A-Z]\.)", r"\1<prd>", protected)
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'“‘(\[]*[A-Z0-9])", protected)
    return [part.replace("<prd>", ".").strip() for part in parts if part.strip()]


def section_stats(lines: list[str], spec: SectionSpec) -> dict[str, object]:
    selected = lines[spec.start - 1 : spec.end]
    normalized = "\n".join(selected).strip()
    blocks = prose_blocks(selected)
    sentence_lists = [split_sentences(block) for block in blocks]
    sentences = [sentence for group in sentence_lists for sentence in group]
    words = re.findall(r"\b[\w’'-]+\b", " ".join(blocks), flags=re.UNICODE)
    citation_groups = re.findall(r"\([^)]*(?:(?:19|20)\d{2}|et al\.)[^)]*\)", " ".join(blocks))
    citation_sentences = sum(
        1
        for sentence in sentences
        if re.search(r"\([^)]*(?:(?:19|20)\d{2}|et al\.)[^)]*\)", sentence)
    )
    sentence_counts = [len(group) for group in sentence_lists]
    word_counts = [len(re.findall(r"\b[\w’'-]+\b", sentence, flags=re.UNICODE)) for sentence in sentences]
    openings = []
    for index, (block, group) in enumerate(zip(blocks, sentence_lists), start=1):
        opening = " ".join(re.findall(r"\b[\w’'-]+\b", block, flags=re.UNICODE)[:14])
        openings.append(
            {
                "index": index,
                "sentences": len(group),
                "words": len(re.findall(r"\b[\w’'-]+\b", block, flags=re.UNICODE)),
                "citations": len(re.findall(r"\([^)]*(?:(?:19|20)\d{2}|et al\.)[^)]*\)", block)),
                "opening": opening,
            }
        )
    return {
        "sha256": hashlib.sha256(normalized.encode("utf-8")).hexdigest().upper(),
        "paragraphs": len(blocks),
        "sentences": len(sentences),
        "words": len(words),
        "sentences_per_paragraph_mean": round(len(sentences) / len(blocks), 2) if blocks else 0,
        "sentences_per_paragraph_median": statistics.median(sentence_counts) if sentence_counts else 0,
        "words_per_sentence_mean": round(statistics.mean(word_counts), 2) if word_counts else 0,
        "short_paragraphs": sum(1 for count in sentence_counts if count <= 2),
        "citation_groups": len(citation_groups),
        "citation_sentences": citation_sentences,
        "semicolons": normalized.count(";"),
        "colons": normalized.count(":"),
        "em_dashes": normalized.count("—") + normalized.count("–"),
        "openings": openings,
    }


def main() -> None:
    output: list[str] = []
    output.append("# v10 权威原文整节统计基线与源文冻结清单")
    output.append("")
    output.append("本文件由脚本从冻结的 Otero MinerU 全文机械生成。统计对象是完整的对应节，而不是摘录句。段落开头只保留前十四个词用于定位；正文写作仍须回到源文整节阅读。源文行号均为一基编号，节哈希用于证明后续审计所比较的原文没有被悄然替换。")
    output.append("")
    output.append("## 一、统计口径")
    output.append("")
    output.append("段落按 Markdown 空行识别，并排除标题、图片、表格与独立公式。句界采用英文标点近似规则，因此统计用于比较段落颗粒度、句法节奏、引用密度和标点分布，不替代人工句法判断。`短段`指不超过两个语法句的 prose block；它是诊断信号，不是机械禁令。")
    output.append("")
    for source in SOURCES:
        path = ROOT / source.path
        if not path.exists():
            raise FileNotFoundError(path)
        raw = path.read_bytes()
        lines = raw.decode("utf-8-sig").splitlines()
        output.append(f"## {source.code}")
        output.append("")
        output.append(f"- 源文件：`{source.path}`")
        output.append(f"- 全文 SHA-256：`{hashlib.sha256(raw).hexdigest().upper()}`")
        output.append(f"- 本轮角色：{source.role}")
        output.append("")
        output.append("| 完整对应节 | 源行 | 节哈希 | 段 | 句 | 词 | 句/段均值 | 句/段中位数 | 短段 | 引用组 | 含引用句 | 分号 | 冒号 | 破折号 |")
        output.append("|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        section_results: list[tuple[SectionSpec, dict[str, object]]] = []
        for section in source.sections:
            stats = section_stats(lines, section)
            section_results.append((section, stats))
            output.append(
                f"| {section.label} | {section.start}–{section.end} | `{str(stats['sha256'])[:16]}` | "
                f"{stats['paragraphs']} | {stats['sentences']} | {stats['words']} | "
                f"{stats['sentences_per_paragraph_mean']} | {stats['sentences_per_paragraph_median']} | "
                f"{stats['short_paragraphs']} | {stats['citation_groups']} | {stats['citation_sentences']} | "
                f"{stats['semicolons']} | {stats['colons']} | {stats['em_dashes']} |"
            )
        output.append("")
        output.append("### 段落级定位指纹")
        output.append("")
        for section, stats in section_results:
            output.append(f"#### {section.label}")
            output.append("")
            output.append("| 段 | 句 | 词 | 引用组 | 前十四词定位 |")
            output.append("|---:|---:|---:|---:|---|")
            for item in stats["openings"]:  # type: ignore[index]
                output.append(
                    f"| {item['index']} | {item['sentences']} | {item['words']} | {item['citations']} | {item['opening']} |"
                )
            output.append("")
    output.append("## 二、对新稿的硬性用途")
    output.append("")
    output.append("新稿每一整节完成后，逐节审计必须同时记录新稿的段数、句数、字符数、句段比、短段数、引用组、含引用句比例、冒号、分号和破折号，并说明与相应源节的差异为何来自中文语法或研究内容，而不是任意偏好。仅列几个代表句、仅说结构相似或仅做关键词扫描，均不能证明完成整节对照。")
    output.append("")
    output.append("肖老师两篇原文始终是主基线。辅助论文只在其研究对象、理论或评价责任与当前研究直接对应时进入对照，不以辅助论文的局部习惯覆盖主基线。")
    output.append("")
    target = OUT_DIR / "154_v10权威原文整节统计基线与源文冻结清单.md"
    target.write_text("\n".join(output) + "\n", encoding="utf-8-sig")
    print(target)


if __name__ == "__main__":
    main()
