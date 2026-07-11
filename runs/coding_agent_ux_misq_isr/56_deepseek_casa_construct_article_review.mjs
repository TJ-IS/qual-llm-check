import { readFile, writeFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const runDir = dirname(fileURLToPath(import.meta.url));
const workspaceDir = resolve(runDir, "..", "..");
const draftPath = resolve(runDir, "55_casa_construct_development_article_plan_v1.md");
const outputPath = resolve(runDir, "56_deepseek_casa_construct_article_review.json");

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

async function requestReview(baseUrl, apiKey, rolePrompt, draft) {
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
            "你是严格的顶级信息系统期刊审稿人。只根据提供的稿件和你确知的正式文献判断，不献媚，不虚构引用。输出有效 JSON。",
        },
        {
          role: "user",
          content: `${rolePrompt}\n\n待审稿件如下：\n\n${draft}`,
        },
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

const reviewerPrompts = [
  {
    reviewer: "misq_logic_reviewer",
    prompt: `请从 MISQ 构念开发论文的角度审查。重点比较稿件是否真正复现 Chen et al. (2024) 从新对象、母构念、具体错配、理论基础、研究问题到混合方法的论证逻辑，而不是只模仿章节标题。检查 CASA 的现实重要性、唯一基础构念、与信任/透明度/控制的边界、两个研究问题和三项贡献是否彼此一致。严格输出：
{
  "verdict": "可推进|需小幅修改|需重大修改|不成立",
  "fatal_logic_issues": [],
  "unsupported_or_overstated_claims": [],
  "chen_logic_mismatches": [],
  "missing_formal_literature": [],
  "specific_revision_instructions": [],
  "strongest_defensible_contribution": ""
}`,
  },
  {
    reviewer: "measurement_method_reviewer",
    prompt: `请从心理测量、主观态势感知和二手在线文本方法的角度审查。重点检查：SART 与 SAGAT 是否被准确区分；主观状态、客观知识、前因和后果是否混淆；Reddit 能否支持内容领域开发；开放编码、一致性、饱和、Q-sort、反映式/形成式选择、三轮样本、法则与增量效度是否足以支持顶级期刊投稿。严格输出：
{
  "verdict": "可推进|需小幅修改|需重大修改|不成立",
  "construct_boundary_risks": [],
  "measurement_model_risks": [],
  "secondary_data_risks": [],
  "validation_design_gaps": [],
  "specific_revision_instructions": [],
  "minimum_conditions_for_new_construct_claim": []
}`,
  },
];

const env = parseEnv(await readFile(resolve(workspaceDir, ".env"), "utf8"));
const baseUrl = env.NEW_API_BASE_URL || "https://api.deepseek.com";
if (!env.NEW_API_KEY) throw new Error("NEW_API_KEY is not available in .env");

const draft = await readFile(draftPath, "utf8");
const reviews = [];
for (const item of reviewerPrompts) {
  reviews.push({
    reviewer: item.reviewer,
    response: await requestReview(baseUrl, env.NEW_API_KEY, item.prompt, draft),
  });
}

await writeFile(outputPath, `${JSON.stringify(reviews, null, 2)}\n`, "utf8");
console.log(`Wrote ${outputPath}`);
