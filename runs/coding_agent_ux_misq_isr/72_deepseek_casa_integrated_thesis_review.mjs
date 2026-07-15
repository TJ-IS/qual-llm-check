import { readFile, writeFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const runDir = dirname(fileURLToPath(import.meta.url));
const workspaceDir = resolve(runDir, "..", "..");
const draftPath = resolve(runDir, "71_casa_thesis_chapters_1_to_3_integrated_draft.md");
const dongPath = resolve(workspaceDir, "docs_ref_thesis", "dong_thesis.md");
const dongChapter3Path = resolve(workspaceDir, "docs_ref_thesis", "dong_thesis_concept_development_substudy.md");
const outputPath = resolve(runDir, "72_deepseek_casa_integrated_thesis_review.json");

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
            "You are a skeptical information systems dissertation examiner. Compare structures and argument functions, not wording. Use only supplied materials. Do not invent citations or completed findings. Return valid JSON with all values in English.",
        },
        { role: "user", content: prompt },
      ],
      temperature: 0,
      max_tokens: 6500,
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
const dong = await readFile(dongPath, "utf8");
const dongChapter3 = await readFile(dongChapter3Path, "utf8");
const dongLines = dong.split(/\r?\n/);
const dongFirstThreeChapters = dongLines.slice(548, 1340).join("\n");
const draftChapter3 = draft.slice(draft.indexOf("## 第 3 章"), draft.indexOf("## 参考文献"));

const prompts = [
  {
    reviewer: "dong_chapters_1_to_3_structure_reviewer",
    prompt: `Compare the integrated CASA draft with Dong's dissertation Chapters 1-3. The required architecture is: Chapter 1 starts from the existing CASA opening and adds purpose/significance, literature review, contents/structure, and methods/route; Chapter 2 provides theoretical background only for the construct-development study currently written, not full theories for later antecedent and consequence studies; Chapter 3 performs construct development and scale development. Identify missing paragraph functions, misplaced material, repetition across chapters, or sections that are merely skeletal rather than dissertation prose.

Return
{
  "verdict": "proceed|minor revisions|major revisions|not defensible",
  "chapter_1_alignment": [],
  "chapter_2_alignment": [],
  "chapter_3_alignment": [],
  "misplaced_or_redundant_content": [],
  "required_revisions": [],
  "overall_assessment": ""
}

Dong Chapters 1-3
${dongFirstThreeChapters}

CASA integrated draft
${draft}`,
  },
  {
    reviewer: "construct_development_rigor_reviewer",
    prompt: `Audit the CASA Chapter 3 against Dong's construct-development chapter and top-IS construct-development expectations. Situation awareness must remain the sole foundational construct. Agentic IS delegation may explain the context but must not become a second foundational construct. The empirical plan uses Reddit secondary text rather than concept workshops or fabricated interviews. Check that the sequence concept development, dimension identification, item generation, item revision, item evaluation, and item determination is complete; that Taylor defines the subjective attribute while Endsley organizes content; that dimensions and results are not predeclared; and that the plan states defensible failure criteria.

Return
{
  "verdict": "proceed|minor revisions|major revisions|not defensible",
  "dong_function_matches": [],
  "missing_methodological_elements": [],
  "single_foundation_violations": [],
  "fabricated_or_premature_claims": [],
  "required_revisions": [],
  "overall_assessment": ""
}

Dong construct-development chapter
${dongChapter3}

CASA Chapter 3
${draftChapter3}`,
  },
];

const results = [];
for (const item of prompts) {
  results.push({ reviewer: item.reviewer, response: await requestReview(baseUrl, env.NEW_API_KEY, item.prompt) });
}
await writeFile(outputPath, `${JSON.stringify(results, null, 2)}\n`, "utf8");
console.log(`Wrote ${outputPath}`);
