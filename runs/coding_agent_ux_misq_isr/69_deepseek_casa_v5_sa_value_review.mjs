import { readFile, writeFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const runDir = dirname(fileURLToPath(import.meta.url));
const workspaceDir = resolve(runDir, "..", "..");
const draftPath = resolve(runDir, "68_casa_construct_development_article_plan_v5.md");
const auditPath = resolve(runDir, "67_casa_situation_awareness_value_evidence_audit.md");
const outputPath = resolve(runDir, "69_deepseek_casa_v5_sa_value_review.json");

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
            "You are a skeptical reviewer for a top information systems journal. Evaluate only the supplied evidence and text. Do not invent findings or citations. Return valid JSON with all values in English.",
        },
        { role: "user", content: prompt },
      ],
      temperature: 0,
      max_tokens: 5500,
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
    reviewer: "sa_value_evidence_reviewer",
    prompt: `Review the first two paragraphs of the CASA introduction and the transition into C21. Determine whether the revised second paragraph establishes a valid chain from situation-awareness value evidence to the motivation for studying coding-agent situation awareness. Distinguish carefully among Jaeger and Eckhardt's individual situational information security awareness, Nadj et al.'s situation-awareness and performance divergence, Rose et al.'s subjective LETSSA evidence, Endsley's human-AI argument, and Kumar and Dhanorkar's coding-agent observations. Identify any citation that is asked to support more than it actually shows.

Return
{
  "verdict": "proceed|minor revisions|major revisions|not defensible",
  "supported_transitions": [],
  "unsupported_transitions": [],
  "subjective_sa_boundary_errors": [],
  "sentence_level_revisions": [],
  "overall_assessment": ""
}

Evidence audit
${audit}

Introduction
${intro}`,
  },
  {
    reviewer: "motivation_coherence_reviewer",
    prompt: `Assess whether the opening now makes the research motivation and significance clear without circular reasoning. The paragraph must not infer CASA directly from the existence of coding-agent review work. It should first establish that situation awareness matters in dynamic technical tasks, then that subjective awareness has meaningful outcome associations, and finally that coding-agent use contains continuing judgments under delegation. Check whether C19.14-C19.15 follow from the cited evidence and whether C23 repeats the same literature unnecessarily.

Return
{
  "verdict": "proceed|minor revisions|major revisions|not defensible",
  "logic_strengths": [],
  "remaining_leaps": [],
  "redundancies": [],
  "required_revisions": [],
  "overall_assessment": ""
}

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
