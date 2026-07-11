import { readFile, writeFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const runDir = dirname(fileURLToPath(import.meta.url));
const workspaceDir = resolve(runDir, "..", "..");
const draftPath = resolve(runDir, "59_casa_construct_development_article_plan_v2.md");
const citationAuditPath = resolve(runDir, "58_chen_misq_citation_logic_audit.md");
const outputPath = resolve(runDir, "60_deepseek_casa_v2_citation_review.json");

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
            "你是严格的顶级信息系统期刊审稿人。只根据给定稿件和你确知的正式文献判断。不得虚构引文内容、DOI或研究结论。输出有效JSON。",
        },
        { role: "user", content: prompt },
      ],
      temperature: 0,
      max_tokens: 5000,
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
const audit = await readFile(citationAuditPath, "utf8");
const coreDraft = draft.split("\n---\n", 1)[0];
const implementationDraft = draft.includes("\n---\n")
  ? draft.slice(draft.indexOf("\n---\n") + 5)
  : draft;
const conciseAudit = audit.slice(audit.indexOf("## 六、重写时的硬性检查"));

const prompts = [
  {
    reviewer: "misq_citation_logic_reviewer",
    prompt: `请审查下面的CASA构念开发计划是否真正学习了Chen et al. (2024) MISQ文章的引用逻辑，而不只是增加引文数量。逐段检查：技术情境、结构差异、基础构念定义、现实重要性、既有量表比较、广度与深度缺口、相邻研究、SART桥接及混合方法。特别检查每项事实主张是否由类型匹配的文献支持，综合推论是否由前文证据推出，是否存在装饰性引用或引用越界。请输出：
{
  "verdict": "可推进|需小幅修改|需重大修改|不成立",
  "best_matched_paragraphs": [],
  "citation_type_mismatches": [],
  "unsupported_claims": [],
  "missing_primary_or_classic_sources": [],
  "redundant_or_decorative_sources": [],
  "sentence_level_revisions": [],
  "overall_assessment": ""
}

引用逻辑审计规范：
${conciseAudit}

待审稿件：
${coreDraft}`,
  },
  {
    reviewer: "construct_boundary_and_measurement_reviewer",
    prompt: `请从个体层构念开发和主观态势感知测量角度审查下面稿件。检查CASA是否始终只有主观态势感知这一个基础构念；代理行动所带来的新状态对象是否足以支持情境化开发；与信任、透明度、控制、负荷、表现及客观状态知识的边界是否一致；SART、SAGAT、LETSSA及主客观分离的文献是否被准确使用；研究设计能否检验新构念主张。请输出：
{
  "verdict": "可推进|需小幅修改|需重大修改|不成立",
  "construct_definition_risks": [],
  "migration_logic_risks": [],
  "boundary_inconsistencies": [],
  "measurement_and_validation_gaps": [],
  "claims_that_should_be_weakened": [],
  "specific_revisions": [],
  "minimum_evidence_for_publication": []
}

待审稿件：
${coreDraft}

预期实施方案：
${implementationDraft}`,
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
