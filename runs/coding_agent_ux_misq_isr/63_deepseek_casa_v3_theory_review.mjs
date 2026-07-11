import { readFile, writeFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const runDir = dirname(fileURLToPath(import.meta.url));
const workspaceDir = resolve(runDir, "..", "..");
const draftPath = resolve(runDir, "62_casa_construct_development_article_plan_v3.md");
const chenPath = resolve(
  workspaceDir,
  "docs_ref_MISQ",
  "Chen_2024_-_Conceptualization_and_Measurement_of_Voice-Interaction_Usability_The_Development_of_Cooperative_Pri.md",
);
const citationAuditPath = resolve(runDir, "58_chen_misq_citation_logic_audit.md");
const theoryAuditPath = resolve(runDir, "61_casa_theoretical_lens_selection_audit.md");
const outputPath = resolve(runDir, "63_deepseek_casa_v3_theory_review.json");

function parseEnv(text) {
  const values = {};
  for (const raw of text.split(/\r?\n/)) {
    const line = raw.trim();
    if (!line || line.startsWith("#") || !line.includes("=")) continue;
    const index = line.indexOf("=");
    values[line.slice(0, index).trim()] = line
      .slice(index + 1)
      .trim()
      .replace(/^['"]|['"]$/g, "");
  }
  return values;
}

async function requestReview(baseUrl, apiKey, prompt) {
  const response = await fetch(`${baseUrl.replace(/\/$/, "")}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "deepseek-v4-pro",
      messages: [
        {
          role: "system",
          content:
            "你是严格的信息系统顶级期刊审稿人。只能依据给定稿件、对标原文和正式文献证据进行判断。不得虚构原文、研究结论、引文或 DOI。请输出有效 JSON，并将 JSON 的所有值都写成英文，以避免字符编码损坏。",
        },
        { role: "user", content: prompt },
      ],
      temperature: 0,
      max_tokens: 7000,
      response_format: { type: "json_object" },
    }),
  });
  if (!response.ok) {
    throw new Error(`DeepSeek HTTP ${response.status}: ${await response.text()}`);
  }
  const body = await response.json();
  return JSON.parse(body.choices[0].message.content);
}

const env = parseEnv(await readFile(resolve(workspaceDir, ".env"), "utf8"));
const baseUrl = env.NEW_API_BASE_URL || "https://api.deepseek.com";
if (!env.NEW_API_KEY) throw new Error("NEW_API_KEY is not available in .env");

const draft = await readFile(draftPath, "utf8");
const chen = await readFile(chenPath, "utf8");
const citationAudit = await readFile(citationAuditPath, "utf8");
const theoryAudit = await readFile(theoryAuditPath, "utf8");

const draftStart = draft.indexOf("## 1 引言");
const draftEnd = draft.indexOf("## 3 混合方法路径");
const coreDraft = draft.slice(draftStart, draftEnd);
const chenStart = chen.indexOf("## Theoretical Background");
const chenEnd = chen.indexOf("## Mixed Methods Approach");
const chenTheory = chen.slice(chenStart, chenEnd);

const prompts = [
  {
    reviewer: "misq_sentence_function_and_citation_reviewer",
    prompt: `请逐段、逐句审查 CASA 稿的理论背景是否真正复现 Chen et al. (2024) MISQ 理论背景的论证功能，而非只模仿标题或增加引文。重点检查：
1. C45 是否分别完成定义、情境依赖、领域关注和表格引出；
2. C47 是否直接调用表 1 中旧概念与量表的具体内容证明不匹配；
3. 表 2、C53、C55 是否依次建立邻近研究、广度与深度缺口、构念与测量缺口；
4. C59、C61、C63 是否像 CPT 部分一样依次说明理论原义、跨领域使用、适用桥梁及新情境发展空间；
5. 每项事实主张是否由类型匹配的原始研究、Top IS 文献、经典文献或近期正式发表研究支持；
6. 是否存在装饰性引用、表格内容与正文不一致、过度推断或本可删除的作者评论。

输出：
{
  "verdict": "可推进|需小幅修改|需重大修改|不成立",
  "sentence_function_alignment": [],
  "citation_role_errors": [],
  "unsupported_or_overstated_claims": [],
  "table_problems": [],
  "missing_primary_or_top_is_sources": [],
  "specific_revisions": [],
  "overall_assessment": ""
}

Chen 理论背景原文：
${chenTheory}

CASA 引文逻辑审计：
${citationAudit}

待审 CASA 稿：
${coreDraft}`,
  },
  {
    reviewer: "theoretical_lens_and_construct_boundary_reviewer",
    prompt: `请从构念开发和理论使用角度审查 CASA 稿。核心问题是：CASA 只以 Taylor (1990) 的个体主观态势感知为基础构念；Endsley (1995b) 的动态态势感知理论承担类似 Chen et al. (2024) 中 CPT 的高阶组织作用；Baird and Maruping (2021) 只解释编程智能体的委托情境；智能体透明度只作为可能前因。请检查这种理论架构是否严谨并被稿件始终贯彻。

具体检查：
1. Endsley 理论是否真能组织二手文本而不把三层级强制设为最终维度；
2. Taylor、Endsley、IS delegation 和 agent transparency 的角色是否混淆；
3. 三类编程智能体差异是否必要、相互区分并有文献依据，是否仍只是对象名称替换；
4. CASA 是否与透明度、信任、工作负荷、感知控制、客观状态知识和任务表现保持边界；
5. 表 1 是否足以代表个体态势感知的经典、IS 和近期自主智能体文献；
6. 理论发展主张是否与后续二手数据构念开发程序相匹配。

输出：
{
  "verdict": "可推进|需小幅修改|需重大修改|不成立",
  "theory_architecture_strengths": [],
  "role_confusions": [],
  "migration_logic_risks": [],
  "construct_boundary_risks": [],
  "missing_literature_or_evidence": [],
  "specific_revisions": [],
  "minimum_evidence_needed_after_phase_1": [],
  "overall_assessment": ""
}

理论选择审计：
${theoryAudit}

待审 CASA 稿：
${coreDraft}`,
  },
];

const reviews = [];
for (const item of prompts) {
  reviews.push({
    reviewer: item.reviewer,
    response: await requestReview(baseUrl, env.NEW_API_KEY, item.prompt),
  });
}

await writeFile(outputPath, `${JSON.stringify(reviews, null, 2)}\n`, "utf8");
console.log(`Wrote ${outputPath}`);
