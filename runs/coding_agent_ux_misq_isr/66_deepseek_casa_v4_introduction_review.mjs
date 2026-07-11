import { readFile, writeFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const runDir = dirname(fileURLToPath(import.meta.url));
const workspaceDir = resolve(runDir, "..", "..");
const draftPath = resolve(runDir, "65_casa_construct_development_article_plan_v4.md");
const chenPath = resolve(
  workspaceDir,
  "docs_ref_MISQ",
  "Chen_2024_-_Conceptualization_and_Measurement_of_Voice-Interaction_Usability_The_Development_of_Cooperative_Pri.md",
);
const dongPath = resolve(
  workspaceDir,
  "docs_ref_thesis",
  "dong_thesis_concept_development_substudy.md",
);
const auditPath = resolve(runDir, "64_casa_introduction_necessity_logic_audit.md");
const outputPath = resolve(runDir, "66_deepseek_casa_v4_introduction_review.json");

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

async function review(baseUrl, apiKey, prompt) {
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
            "You are a demanding reviewer for a top information systems journal. Assess only the supplied manuscript and evidence. Do not invent studies, findings, quotations, or DOIs. Return valid JSON and write all JSON values in English.",
        },
        { role: "user", content: prompt },
      ],
      temperature: 0,
      max_tokens: 6500,
      response_format: { type: "json_object" },
    }),
  });
  if (!response.ok) {
    throw new Error(`DeepSeek HTTP ${response.status}: ${await response.text()}`);
  }
  const data = await response.json();
  return JSON.parse(data.choices[0].message.content);
}

const env = parseEnv(await readFile(resolve(workspaceDir, ".env"), "utf8"));
const baseUrl = env.NEW_API_BASE_URL || "https://api.deepseek.com";
if (!env.NEW_API_KEY) throw new Error("NEW_API_KEY is not available in .env");

const draft = await readFile(draftPath, "utf8");
const chen = await readFile(chenPath, "utf8");
const dong = await readFile(dongPath, "utf8");
const audit = await readFile(auditPath, "utf8");

const intro = draft.slice(draft.indexOf("## 1 引言"), draft.indexOf("## 2 理论背景"));
const chenIntro = chen.slice(chen.indexOf("## Introduction"), chen.indexOf("## Theoretical Background"));
const dongOpening = dong.slice(dong.indexOf("## 第 3 章"), dong.indexOf("## 3.2 社会化商务技术可供性概念的维度识别"));

const prompts = [
  {
    reviewer: "introduction_argument_reviewer",
    prompt: `Evaluate whether the CASA introduction reproduces the argumentative functions of Chen et al. (2024) rather than merely its paragraph count. Review C19 through C39 sentence by sentence. Pay particular attention to whether C19.10-C19.11 are actually supported by Kumar and Dhanorkar; whether C21 establishes a genuine reason to develop situation awareness; whether C23 formally defines CASA and establishes practical importance without claiming untested effects; whether C25-C27 concretely show measurement mismatch; and whether C29 clearly states why construct development is necessary for research and practice. Also assess whether the use of Dong's Chapter 3 logic strengthens necessity without importing a literature-review chapter into the introduction.

Return this structure.
{
  "verdict": "proceed|minor revisions|major revisions|not defensible",
  "strong_paragraphs": [],
  "unsupported_inferences": [],
  "necessity_chain_gaps": [],
  "redundant_or_misplaced_material": [],
  "sentence_level_revisions": [],
  "overall_assessment": ""
}

Chen introduction
${chenIntro}

Dong Chapter 3 opening
${dongOpening}

CASA logic audit
${audit}

CASA introduction
${intro}`,
  },
  {
    reviewer: "skeptical_evidence_and_style_reviewer",
    prompt: `Act as a skeptical reviewer. Test every transition in the CASA introduction against the type of evidence cited. Industry reports may establish practical importance but not CASA. Coding-agent studies may establish ongoing interaction and review work but not a new construct. Situation-awareness and IS studies may support a theoretical relevance chain but cannot establish CASA's untested effects. Identify any remaining overstatement, circular reasoning, or unsupported necessity claim. Check whether the definition is formal rather than provisional, whether adjacent programming studies have been appropriately moved out of the introduction, and whether the formal manuscript through Section 3 avoids colon-led fragments and list-like prose.

Return this structure.
{
  "verdict": "proceed|minor revisions|major revisions|not defensible",
  "evidence_type_errors": [],
  "causal_overstatements": [],
  "definition_problems": [],
  "style_problems": [],
  "required_revisions": [],
  "overall_assessment": ""
}

CASA introduction
${intro}`,
  },
];

const results = [];
for (const item of prompts) {
  results.push({ reviewer: item.reviewer, response: await review(baseUrl, env.NEW_API_KEY, item.prompt) });
}

await writeFile(outputPath, `${JSON.stringify(results, null, 2)}\n`, "utf8");
console.log(`Wrote ${outputPath}`);
