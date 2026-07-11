import { readFile, writeFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const runDir = dirname(fileURLToPath(import.meta.url));
const workspaceDir = resolve(runDir, "..", "..");
const draftPath = resolve(runDir, "68_casa_construct_development_article_plan_v5.md");
const auditPath = resolve(runDir, "67_casa_situation_awareness_value_evidence_audit.md");
const outputPath = resolve(runDir, "70_deepseek_casa_paragraph_bridge_review.json");

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
            "You are a skeptical reviewer for a top information systems journal. Evaluate only the supplied text and evidence. Do not invent findings or citations. Return valid JSON with all values in English.",
        },
        { role: "user", content: prompt },
      ],
      temperature: 0,
      max_tokens: 4500,
      response_format: { type: "json_object" },
    }),
  });
  if (!response.ok) throw new Error(`DeepSeek HTTP ${response.status}: ${await response.text()}`);
  const data = await response.json();
  return JSON.parse(data.choices[0].message.content);
}

const env = parseEnv(await readFile(resolve(workspaceDir, ".env"), "utf8"));
const baseUrl = env.NEW_API_BASE_URL || "https://api.deepseek.com";
if (!env.NEW_API_KEY) throw new Error("NEW_API_KEY is not available in .env");

const draft = await readFile(draftPath, "utf8");
const audit = await readFile(auditPath, "utf8");
const intro = draft.slice(draft.indexOf("## 1 引言"), draft.indexOf("## 2 理论背景"));

const prompts = [
  {
    reviewer: "paragraph_bridge_reviewer",
    prompt: `Review the first and second introduction paragraphs as a connected argument. Check whether the second paragraph now follows naturally from the first paragraph's final claim about delegating multistep software tasks. Evaluate every transition in C19.7-C19.17, especially delegation to continuing judgment, continuing judgment to task understanding, and task understanding to situation-awareness literature. Do not require a predetermined evidence order.

Return
{
  "verdict": "proceed|minor revisions|major revisions|not defensible",
  "bridge_strengths": [],
  "remaining_discontinuities": [],
  "unsupported_claims": [],
  "sentence_level_revisions": [],
  "overall_assessment": ""
}

Evidence audit
${audit}

Introduction
${intro}`,
  },
  {
    reviewer: "claim_boundary_reviewer",
    prompt: `Audit C19.7-C19.17 for evidentiary boundaries. The paragraph may use studies from adjacent dynamic-task settings as weaker motivation for studying CASA, but it must not claim that coding-agent subjective situation awareness has already been shown to cause performance, control, satisfaction, or behaviour. Check whether Kumar and Dhanorkar support the coding-agent claims and whether Jaeger, Nadj, Rose, and Endsley are characterized accurately.

Return
{
  "verdict": "proceed|minor revisions|major revisions|not defensible",
  "supported_claims": [],
  "overclaims": [],
  "needed_qualifications": [],
  "sentence_level_revisions": [],
  "overall_assessment": ""
}

Evidence audit
${audit}

Introduction
${intro}`,
  },
];

const results = [];
for (const item of prompts) {
  results.push({ reviewer: item.reviewer, response: await requestReview(baseUrl, env.NEW_API_KEY, item.prompt) });
}
await writeFile(outputPath, `${JSON.stringify(results, null, 2)}\n`, "utf8");
console.log(`Wrote ${outputPath}`);
