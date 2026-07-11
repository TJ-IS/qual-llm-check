import { readFile, writeFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const runDir = dirname(fileURLToPath(import.meta.url));
const workspaceDir = resolve(runDir, "..", "..");
const outputPath = resolve(runDir, "42_deepseek_concept_review.json");

function parseEnv(text) {
  const values = {};
  for (const raw of text.split(/\r?\n/)) {
    const line = raw.trim();
    if (!line || line.startsWith("#") || !line.includes("=")) continue;
    const index = line.indexOf("=");
    const key = line.slice(0, index).trim();
    const value = line.slice(index + 1).trim().replace(/^['"]|['"]$/g, "");
    values[key] = value;
  }
  return values;
}

const prompt = `你是一位严格的 MIS 博士论文外审专家。请独立审查下面的论文构想，中文回答。我们不会把你的回答直接当结论，而是用它找潜在概念错误。

拟议研究对象：coding agent 是能检查代码库、编辑多个文件、调用工具或终端、运行测试，并在较少实时人类指令下完成多步编程工作的 agentic IS artifact。用户仍需设定任务边界、监督、审批、纠偏和接管。

唯一基础概念：Endsley 的 situation awareness（SA）：人在动态任务环境中对相关元素的感知、理解其意义并预测近期状态的认知状态。已有证据：Endsley (1995) 区分 SA 与 situation assessment；Endsley 与 Kiris (1995) 表明自动化可造成 out-of-the-loop；Parasuraman 等 (2000) 说明自动化会改变并增加人类协调要求；Jaeger 与 Eckhardt (2021, ISJ) 已将 SA 严格迁移为 situational information security awareness；Nadj 等 (2020, DSS) 用 SA 研究交互分析仪表板与绩效。

拟议新构念（暂定、待质性修订）：编码代理工作情境觉察（coding-agent work-situation awareness, CAWSA），指用户在一次具体 coding-agent 任务中，对 agent 行动、代码库状态、工具执行结果、任务约束与后续行动风险所构成的动态工作情境，进行感知、理解和预测的程度。它是 episode-level 的认知状态，不是人格或一般技术态度。初步将 perception、comprehension、projection 仅作为 sensitizing concepts 与效标框架，不预先等同于最终量表维度。

研究设计：仿照 Chen 等 (2024, MISQ) 对公开用户评论的程序，先以 Reddit 上 coding-agent 使用者的帖子和评论进行双人开放编码、轴向编码，再把结果与 SA 理论进行反复比对；之后才决定内涵、维度与测量模型。量表会接受 Q-sort、多轮独立样本 EFA/CFA，并同时以 CA-SAGAT 式客观任务探针检验，而不是只用自评。后续研究拟检验界面中的工作状态证据支持、任务自主性或不确定性、用户经验与任务复杂度如何影响 CAWSA，以及 CAWSA 如何影响审批准确性、及时接管、校准信任、感知控制与绩效。后续前因和后果还没有被写成已验证假设。

请输出严格 JSON：
{
  "verdict": "可推进|需重大修改|不成立",
  "fatal_conflations": ["..."],
  "definition_boundary_fixes": ["..."],
  "theory_migration_test": ["必须由 Reddit 或后续研究证明的点..."],
  "chapter_1_requirements": ["开篇不能缺的论证..."],
  "chapter_3_method_guards": ["防止预设、循环论证或错误测量..."],
  "measurement_position": "...",
  "most_defensible_contribution": "..."
}`;

async function requestReview(baseUrl, apiKey) {
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
          content: "你重视概念边界、分析层次和原始文献证据。不要献媚，不要虚构不存在的引用。",
        },
        { role: "user", content: prompt },
      ],
      temperature: 0,
      max_tokens: 3000,
      response_format: { type: "json_object" },
    }),
  });
  if (!response.ok) throw new Error(`DeepSeek HTTP ${response.status}: ${await response.text()}`);
  const body = await response.json();
  return JSON.parse(body.choices[0].message.content);
}

const env = parseEnv(await readFile(resolve(workspaceDir, ".env"), "utf8"));
const baseUrl = env.NEW_API_BASE_URL || "https://api.deepseek.com";
const apiKey = env.NEW_API_KEY;
if (!apiKey) throw new Error("NEW_API_KEY is not available in .env");

const reviews = [];
for (const reviewer of ["reviewer_1", "reviewer_2"]) {
  reviews.push({ reviewer, response: await requestReview(baseUrl, apiKey) });
}
await writeFile(outputPath, `${JSON.stringify(reviews, null, 2)}\n`, "utf8");
console.log(`Wrote ${outputPath}`);
