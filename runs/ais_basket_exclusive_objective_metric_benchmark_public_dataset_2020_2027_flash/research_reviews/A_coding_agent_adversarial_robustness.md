# 方向 A：Coding Agent 对抗鲁棒性（Adversarial Robustness of AI Coding Agents）——全面文献综述

- 综述编号：A
- 撰写日期：2026-08-18（基于 2026-08 联网检索，arXiv/会议出处均经二次核验）
- 关联 51 篇锚点：#49 RADAR（MISQ 2025）、#26 ARText（JMIS 2022）、#21 GCNN/KVP（DSS 2021）、#46 GASP（JAIS 2025）、#8 NPECF（DSS 2020）
- 一句话结论：**攻击侧研究已成熟（基准、攻击面、真实漏洞案例齐全），防御侧以规则/推理期检测为主，尚无把"RL 攻击器生成对抗动作序列 + minimax 鲁棒化训练"（即 RADAR 范式）直接用于 coding agent 的工作——这是最清晰的研究空位。**

---

## 1. 问题背景：为什么 coding agent 的对抗鲁棒性重要

现代 coding agent（如 OpenAI Codex、Claude Code、Cursor、Devin、SWE-agent 等）是接入 LLM 的智能体，在仓库/终端环境中自主执行"读代码 → 推理 → 改代码 → 运行测试 → 提交"的闭环。与传统代码补全相比，它的**输入面急剧扩大**：

1. 用户 prompt（可直接注入恶意指令）；
2. 仓库上下文（README、AGENTS.md、issue、PR 评论、CI 输出——可能被第三方污染）；
3. 工具输出（shell 结果、linter、测试日志——可能被对手控制的内容诱导）；
4. MCP 服务器与外部工具（工具描述本身可被投毒）；
5. Agent skill 市场（可下载的"技能包"可能含恶意代码）；
6. 持久状态（会话记忆、checkpoint——可被跨会话利用）。

这意味着 coding agent 的鲁棒性问题从"模型层越狱"扩展为"**系统层对抗攻击**"：攻击者不直接攻击模型权重，而是通过操纵 agent 能读到的任何上下文，诱导它执行有害动作（写恶意代码、泄露密钥、提权、供应链投毒）。

51 篇筛选中命中的 #49 **RADAR**（MISQ 2025，DOI 10.25300/misq/2024/17339）恰好提供了一个可移植的范式模板：

- 问题：恶意软件检测器在对抗攻击下容易被绕过；
- 方法：r-VAC（基于 DRL 的攻击器，在真实恶意软件状态空间生成动作序列）+ RL-RO（鲁棒化训练）；
- 数据：VirusTotal 恶意软件语料 + Microsoft Windows 干净可执行文件（公开可获取）；
- 指标：逃避率（ER，≈ 攻击成功率 ASR）、假阳性率（FPR）、鲁棒化后逃避率平均降低约 84%（鲁棒性提升约 7 倍）；
- 对比：Random actions、BFA、EvadeHC、Surrogate RNN、Policy Gradient、DDQN、Rainbow、MAB-malware、ACER、A3C、GAMMA 共 10 种攻击基准。

RADAR 证明了在 IS 领域可以用"**DRL 攻击器 + 鲁棒化训练 + 双指标评估**"把对抗鲁棒性做成可测、可训练的算法贡献。本综述的核心问题就是：**这个范式在 coding agent 领域做到什么程度了？缺口在哪里？**

---

## 2. 检索范围与方法

- 检索时间：2026-08（联网检索，多轮关键词组合，命中条目逐一打开核验）。
- 数据库/来源：arXiv（含 2025–2026 滚动预印本）、ACL Anthology、NeurIPS/ICML/ICLR 会议官网、Semantic Scholar、Google Scholar、GitHub 安全公告、NVD/CVE 数据库、厂商安全披露。
- 时间窗：2023-01 至 2026-08，重点 2024–2026。
- 关键词组合（英文）：`code agent` / `coding agent` / `AI coding assistant` / `SWE-agent` + `adversarial robustness` / `prompt injection` / `jailbreak` / `red-teaming` / `backdoor` / `supply chain` / `tool poisoning` / `RL fine-tuning defense` / `agent security benchmark` 等。
- 纳入标准：① 直接以编码智能体/代码助手为研究或攻击对象；② 或提供可迁移的通用 agent 攻防方法/基准/综述。
- 结果：核心文献约 40+ 篇，其中 30+ 篇有可核验的 arXiv ID 或会议/期刊出处；另含 2 份同行评议期刊级综述与 3 份会议官方基准。

---

## 3. 攻击面分类学（coding agent 特有）

| 层 | 攻击载体 | 典型场景 |
|---|---|---|
| L1 用户输入 | 恶意 prompt（直接越狱/任务劫持） | 让 agent 生成恶意代码、泄露凭据 |
| L2 仓库上下文 | 恶意 issue / PR / README / AGENTS.md / 文档 | 打开仓库或跑 issue 即被注入 |
| L3 工具层 | 恶意 tool description / MCP 工具 | 工具描述里藏指令，agent 调用即触发 |
| L4 供应链 | 恶意 skill 包 / 依赖投毒 / 代码完成建议投毒 | 安装"帮助性"skill 后持续被控制 |
| L5 持久状态 | 会话记忆 / checkpoint / 缓存注入 | 跨会话、跨任务持续控制 |
| L6 分布式 | 多 PR / 多实例协同（agentic botnet） | 单点监控失效 |
| L7 模型层 | 微调后门 / 权重投毒 | 模型本身被植入触发行为 |

以下按攻击侧、防御侧、RL 攻防训练、评测基准四部分详述。

---## 4. 攻击侧现状（逐篇详述）

### 4.1 JAWS-Bench：coding agent 系统化越狱基准
- 出处：arXiv:2510.01359《Breaking the Code: Security Assessment of AI Code Agents Through Systematic Jailbreaking Attacks》（Saha、Chen 等）。
- 做了什么：构建三个工作区复杂度等级（JAWS-0 / JAWS-1 / JAWS-M），系统评估 coding agent 在越狱攻击下的行为。
- 关键数字：多文件工程场景 ASR ≈ 75%，其中约 32% 的攻击代码可直接部署执行；单文件场景攻击可绕过防御，ASR ≈ 71%。
- 意义：证明"让 agent 干坏事"成功率极高且危害可落地，越狱不再是理论威胁。

### 4.2 MOCHA：多轮恶意编码 prompt 基准
- 出处：EMNLP 2025 Findings（aclanthology.org/2025.findings-emnlp.1249）。
- 做了什么：多轮（multi-turn）恶意 coding prompt 基准，覆盖逐步升级的恶意请求；并验证微调防御。
- 关键数字：微调防御可使拒绝率提升最高 +32.4 个百分点。
- 意义：防御有效，但目前主要体现为"拒绝行为"，未解决"功能正确但带漏洞"的隐蔽攻击。

### 4.3 QueryIPI：查询无关间接注入
- 出处：arXiv:2510.23675（HKUST）。
- 做了什么：提出"查询无关间接注入"（query-independent indirect injection）新范式——注入不依赖用户具体查询，通过优化 tool description 使 agent 在正常使用中触发恶意行为。
- 关键数字：优化 tool description 后 ASR 达 87%，基线约 50%。
- 意义：工具描述是最薄弱环节之一，且攻击可规模化。

### 4.4 ToolLeak：从工具调用视角红队 coding agent
- 出处：arXiv:2509.05755《Red-Teaming Coding Agents from a Tool-Invocation Perspective》（Qu 等）。
- 做了什么：ToolLeak 攻击泄露 agent 工具调用的内部状态，配合双通道注入。
- 关键数字：被测 coding agent 全部被攻破并拿到远程代码执行（RCE）。
- 意义：工具调用内部状态泄露使注入成功率接近 100%。

### 4.5 SWExploit：恶意 issue 诱导生成"带漏洞补丁"
- 出处：arXiv:2509.25894。
- 做了什么：恶意 GitHub issue 诱导自动程序修复（APR）agent 生成"功能正确但带漏洞"的补丁。
- 关键数字：ASR 0.91。
- 意义：功能正确性不再是安全信号——攻击者要的正是"能通过测试的坏补丁"。

### 4.6 FCV-Attack：形式化"功能正确但有漏洞"攻击
- 出处：arXiv:2510.17862（ACL 2026 Main；代码：GitHub Infini-AI-Lab/FCV）。
- 做了什么：形式化 FCV（Functionally Correct but Vulnerable）补丁概念并构造攻击。
- 关键数字：GPT-5 Mini + OpenHands 上 ASR 40.7%。
- 意义：与 SWExploit 共同确立"正确性-安全性分离"研究范式：**通过测试 ≠ 安全**。

### 4.7 IssueTrojanBench：恶意 issue 穿透 guardrail
- 出处：arXiv:2607.20759。
- 做了什么：恶意 issue 注入基准，测试 guardrail 拦截率。
- 关键数字：穿透 guardrail 率 66.5%；拒绝几乎全部来自 LLM 层而非系统 guardrail。
- 意义：现有 guardrail 基本失效，防御必须前移到模型/训练层。

### 4.8 MalSkillBench：恶意 skill 三维运行时验证基准
- 出处：arXiv:2606.07131。
- 做了什么：3,944 个恶意 skill + 4,000 个良性 skill，三维（Generate-Verify-Feedback）108 格运行时验证基准。
- 意义：skill 生态已成为攻击主战场，且需要"运行时"而非"安装时"验证。

### 4.9 DDIPE：skill 生态系统供应链投毒
- 出处：arXiv:2604.03081《Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems》。
- 做了什么：在 skill 的文档、代码示例、配置模板中隐藏恶意载荷，agent 加载 skill 即被控制。
- 意义：供应链攻击从"依赖包"扩展到"技能包"。

### 4.10 PhantomSkill：agent skill 生态恶意代码注入
- 出处：arXiv:2606.19191。
- 做了什么：在 skill 市场注入恶意代码的另一条路线，强调安装后延迟触发。
- 意义：与 DDIPE 互补，说明 skill 投毒是多路线、难检测的。

### 4.11 XOXO：跨源上下文投毒
- 出处：arXiv:2503.14281。
- 做了什么：跨源上下文投毒（cross-source poisoning），污染模型读取的多个来源。
- 关键数字：GPT-4o / Claude 3.5 Sonnet 等模型在 HumanEval+ 上 ASR 87%+、MBPP+ 94%+。
- 意义：即使非 agent 的代码补全场景也高度脆弱，agent 场景输入面更大、风险更高。

### 4.12 Iterative VibeCoding：持久状态下的分布式攻击
- 出处：arXiv:2607.02514《Distributed Attacks in Persistent-State AI Control》。
- 做了什么：跨 PR 的分布式攻击，利用持久状态协同控制多个任务实例。
- 关键数字：集成监控的检测率从 93% 降至 47%。
- 意义：单一监控点（per-instance）失效，需要全局/关联视角。

### 4.13 MCP 工具投毒
- MCPTox（arXiv:2508.14925）：MCP 工具生态投毒分析。
- MCP-TDP Security Benchmark（arXiv:2605.24069）：32 个测试例、6 个风险类别，首个系统化 MCP 投毒测试基准。
- ToolGuardian（arXiv:2607.21835）：MCP 工具调用防护（防御侧）。
- 意义：MCP 正成为 coding agent 标准接口，工具描述投毒是低门槛高收益攻击。

### 4.14 其他攻击/威胁研究
- Agentic botnets 与 hallucination squatting（arXiv:2607.07433）：大规模伪造 agent/工具生态的僵尸网络化利用。
- Prompt Injection Attacks on Agentic Coding Assistants（arXiv:2601.17548，Maloyan & Namiot）：编码助手注入攻击综述。
- Injection–Execution Dissociation（arXiv:2605.08442）：持久记忆攻击——注入与执行解耦，跨会话潜伏触发。
- 综述《A focused survey of code agent security》（Information and Software Technology）：覆盖 82 篇论文（2024–2026），提出两层 S1–S5 攻击分类体系。
- The Attack and Defense Landscape of Agentic AI（arXiv:2603.11088）：agentic AI 攻防全景综述。
- The Balkanization of Execution-Security Research（arXiv:2607.05743）：39 篇、17 类执行安全研究梳理；Pwn2Own Berlin 2026 新增 "Coding Agents" 类别，标志编码智能体成为业界公认攻击目标。
- LLM Vulnerability 综述（arXiv:2606.31639）：LLM 漏洞分类总览。
- Refusal Evaluation in Coding LLMs 综述（arXiv:2605.20351）：编码 LLM 拒绝行为评估方法论。

### 4.15 真实世界证据（不是论文，是已发生的事）
- Claude Code 累计 16 个 CVE，含 CVE-2025-59536（远程代码执行）与 CVE-2025-66032（CVSS 9.8 高危）。
- s1ngularity：恶意"代码完成建议"被武器化的实证（IDE 补全投毒）。
- GitHub Agentic Workflows 私有仓库泄漏事件（GitLost / Noma 工具链披露）。
- hazmat 仓库（github.com/dredozubov/hazmat）：社区汇编的 agent 安全证据与攻击原语集。
- 意义：研究不再是"假设威胁"，攻击已在真实生产环境发生。

---## 5. 防御侧现状（逐篇详述）

### 5.1 CodeSentinel：三层推理期防御
- 出处：arXiv:2606.19235。
- 做了什么：三层推理期防御——静态代码结构检查 + 节点级似然异常检测 + logits 行为影响分析。
- 关键数字：在对比实验中优于 CodeGarrison、DePA、KillBadCode。
- 局限：推理期检测，未做训练级鲁棒化。

### 5.2 TokenWall：语义 token 流运行时审计
- 出处：arXiv:2607.08395（原名 "Token-Flow Firewall"；注意不是 2607.08400/08402）。
- 做了什么：面向 OpenClaw 风格持久 agent 的语义 token 流运行时审计，阻止不安全状态迁移。
- 意义：把"防火墙"概念引入 token 流，适合持久运行 agent。

### 5.3 ClawGuard：工具调用边界规则防御
- 出处：arXiv:2604.11790。
- 做了什么：在工具调用边界实施规则式防御，覆盖 web/local 内容三条间接注入通道。
- 意义：防御面聚焦"内容进工具参数"的必经之路。

### 5.4 AgentLens：白盒机制性子空间干预
- 出处：arXiv:2606.22673。
- 做了什么：白盒机制分析 + 子空间干预，多轮 coding agent 运行时安全检测 + 表征级缓解。
- 意义：从"行为层"深入"表征层"，可解释性强。

### 5.5 Data Leakage Prevention：预先加固
- 出处：arXiv:2607.18847。
- 做了什么：在攻击发生前对 agent 做数据泄漏加固。
- 关键数字：utility 从 37.0% 提升到 72.2%。
- 意义：证明"先加固再上线"可同时改善效用（可能是防御训练清理了干扰）。

### 5.6 AgentAntibody：免训练类免疫系统
- 出处：arXiv:2608.04053。
- 做了什么：免训练防御，借鉴免疫系统——潜用户边界（latent user boundary）+ 表位迁移（epitope transfer）。
- 意义：无需微调即可防御新攻击，适合快速演进威胁。

### 5.7 其他防御
- ARGUS（arXiv:2605.03378）：agent 安全监控/防御框架。
- Reasoning-enabled Task Alignment（arXiv:2606.15441）：推理增强的任务对齐防御。
- SIC（arXiv:2510.21057）：语义注入遏制。
- AegisAgent（arXiv:2512.20986）：agent 防护智能体。
- ContainmentBench（arXiv:2607.23999）：专门评测"注入后遏制"能力的基准——追踪注入发生后 agent 能否被控制住。

### 5.8 关键反例：Autonomy Tax（防御训练的代价）
- 出处：arXiv:2603.19423《The Autonomy Tax: Defense Training Breaks LLM Agents》（Li & Zhao）。
- 做了什么：系统测量防御训练（安全对齐）对 agent 自主任务完成能力的影响。
- 关键数字：防御训练后 agent **99% 的任务超时**（基线 13%）。
- 意义：**纯防御训练可能摧毁自主性**——"能力-对齐悖论"。任何鲁棒化研究必须同时报告良性效用（benign utility / robust resolve rate），否则评估会系统性误判。这也是 RADAR 式双指标设计（ER + FPR + 鲁棒化后效用）必须坚持的原因。

---

## 6. RL 攻防训练现状（与 RADAR 范式最直接相关）

- **MAGIC**（ICML 2026）：多轮多智能体 attacker-defender 不对称博弈，攻防双方在博弈中共同进化。
- **AdvEvo-MARL**（ICML 2026）：多智能体进化攻防，ASR 降到 <20%（基线 38.33%）。
- **Self-RedTeam**（ICML 2026）：在线自博弈红队，跨 5 个模型达到 95% 攻击成功率。
- **ARLAS**（arXiv:2510.05442）：共演化攻击者，能发现未见过的注入类型。
- **RLbreaker**（arXiv:2406.08705）：DRL + PPO 黑盒越狱，无需访问模型内部。
- **Tool-Disguised Attacks via RL**（arXiv:2601.05466）：用 RL 生成"伪装成正常工具调用"的攻击。
- **Robust Critics**（arXiv:2607.20472）：鲁棒评判器辅助对齐。
- **Dual-Adversarial Safety Alignment**（arXiv:2608.09542）：双重对抗安全对齐。
- **Tree-based DRL Red-Teaming**（arXiv:2510.02286）：树搜索 + DRL 红队。

**关键观察**：这些工作证明"RL 攻防训练"在通用 agent/LLM 上有效，但**没有一篇把 RL 攻击器（生成对抗性动作序列）与 minimax 式鲁棒化训练同时用于 coding agent 的具体场景**（恶意 issue/prompt → 工具动作序列 → 补丁/漏洞产出）。这正是 RADAR 范式空位。

---## 7. 评测基准与指标体系

| 基准 | 出处 | 规模 | 核心指标 |
|---|---|---|---|
| AgentDojo | arXiv:2406.13352（NeurIPS 2024 SafeBench） | 97 任务 / 629 测试例 | **Benign Utility + Attack Success Rate（双指标）** |
| InjecAgent | arXiv:2403.02691 | 30 个 tool-integrated agent | ASR、任务成功率 |
| RAS-Eval | arXiv:2506.15253 | 多 agent 场景 | TFR（任务失败率）+ ASR + unified score |
| AgentToolBench-Code | GitHub allenwu-blip/agenttoolbench-code | 10 类静默安全失败 | 锚定 OWASP ASI + Mindgard 框架 |
| CyberSecEval v1–v4 | arXiv:2312.04724 | 多代演进 | CWE 弱点类别 + attack helpfulness；v4 引入 "Instruct or Autocomplete" |
| Action-Graded Severity Scale | arXiv:2607.07474 | — | 按动作危害分级评估攻击后果 |
| ContainmentBench | arXiv:2607.23999 | — | 注入后遏制成功率 |
| MalSkillBench | arXiv:2606.07131 | 3,944 恶意 + 4,000 良性 skill | 三维 108 格运行时验证 |

**指标统一性结论**：AgentDojo 的 "Benign Utility + ASR" 双指标与 RADAR 的 "逃避率 ER + FPR + 鲁棒化后效用" 在结构上完全同构——这是把 RADAR 迁移到 coding agent 的天然桥梁：把 ASR 看成 ER 的 agent 版，把 benign utility / robust resolve rate 看成鲁棒化后任务完成率。

---

## 8. 研究缺口（核心结论）

1. **攻击侧成熟**：越狱（JAWS-Bench）、间接注入（QueryIPI/ToolLeak）、供应链（DDIPE/PhantomSkill）、MCP 投毒、分布式攻击（VibeCoding）、真实 CVE——攻击面与攻击效果都已充分刻画。
2. **防御侧偏浅**：CodeSentinel/TokenWall/ClawGuard 等以规则、启发式、推理期检测为主，未见"训练级鲁棒化"（对攻击轨迹做对抗训练/偏好优化）的系统工作。
3. **RL 攻防训练出现但未落地 coding agent**：MAGIC/AdvEvo-MARL/Self-RedTeam 证明 RL 攻防范式有效，但场景是通用 agent 对话/工具，不是"恶意 issue → 代码补丁"的编码闭环。
4. **RADAR 范式空位**：目前没有工作同时做到 ① DRL 攻击器在编码状态空间生成对抗动作序列；② minimax/鲁棒化训练提升鲁棒性；③ 用 ASR + robust resolve rate + FPR 双指标评估。
5. **Autonomy Tax 警示**：防御训练可能使 agent 99% 任务超时（arXiv:2603.19423），所以鲁棒化必须把"良性任务完成率"作为第一约束，而不是只压 ASR。
6. **正确性-安全性分离**：SWExploit（ASR 0.91）与 FCV（ASR 40.7%）证明"通过测试"不再是安全信号，鲁棒化目标应包含"漏洞率/安全通过率"。

---

## 9. 与 51 篇 IS 文献的衔接

- **#49 RADAR（MISQ 2025）**：直接模板。r-VAC（DRL 攻击器）+ RL-RO（鲁棒化）的完整范式可原样迁移到 coding agent：状态=仓库+issue+历史轨迹；动作=文件编辑/命令执行/工具调用；攻击者目标=产出带漏洞补丁或执行恶意动作；防御者目标=在保持 resolve rate 的前提下最小化 ASR。
- **#26 ARText（JMIS 2022）**：对抗鲁棒性的"设计框架 + 度量"模板——用性能比率与"性能-扰动曲线下面积"度量鲁棒性，可迁移为 coding agent 的"鲁棒性-效用前沿"（utility vs perturbation strength）。
- **#21 GCNN/KVP（DSS 2021）**：事件日志序列建模 → 把攻击轨迹/agent 行为序列建模为事件日志，用门控卷积/键值注意力识别攻击模式（衔接方向 C）。
- **#46 GASP / #8 NPECF（图符号/边分类）**：agent-工具-文件依赖图的符号预测与边分类 → 检测"注入后行为异常"（衔接方向 B/E）。

---

## 10. 对 coding agent 的算法研究方向建议（按优先级）

1. **RL 鲁棒化（最优先，RADAR 范式落地）**
   - 把"恶意 issue/prompt → agent 动作序列 → 结果（漏洞补丁/拒绝/正常修复）"建模为对抗 MDP；
   - 训练 DRL 攻击器（r-VAC 式）生成多样化对抗动作序列，提高攻击样本覆盖；
   - 用 RL-RO 式鲁棒化或 MAGIC/AdvEvo-MARL 式不对称博弈做防御训练；
   - 全程监控 benign resolve rate，防 Autonomy Tax；
   - 数据集全部公开可获取：SWE-bench Verified、AgentDojo、JAWS-Bench、MalSkillBench、FCV 攻击库。

2. **指标设计**
   - 主指标：ASR（攻击成功率）+ Robust Resolve Rate（鲁棒化后良性任务完成率）+ FPR；
   - 附加指标：FCV 漏洞率、cost/task、token 消耗、注入后遏制率（ContainmentBench）。

3. **防御数据管道**
   - 用公开攻击基准自动构造"恶意轨迹-安全轨迹"配对数据；
   - 做对抗重训练/DPO 对齐（ARText 的对抗重训练思路 + MOCHA 的微调防御验证）；
   - 动态补充：共演化攻击器（ARLAS）持续生成新攻击。

4. **评估框架**
   - 把 CyberSecEval / AgentToolBench-Code 的静态安全失败类别、AgentDojo 的双指标、RADAR 的逃避率统一为一个鲁棒性分数；
   - 发布时可对标"Pwn2Own Berlin 2026 Coding Agents 类别"的真实攻击难度。

---

## 11. 参考文献

- [1] Saha, Chen, et al. "Breaking the Code: Security Assessment of AI Code Agents Through Systematic Jailbreaking Attacks." arXiv:2510.01359.
- [2] "MOCHA: Multi-turn malicious coding prompt benchmark." EMNLP 2025 Findings. https://aclanthology.org/2025.findings-emnlp.1249
- [3] "QueryIPI: Query-independent indirect injection." arXiv:2510.23675.
- [4] Qu, et al. "Red-Teaming Coding Agents from a Tool-Invocation Perspective." arXiv:2509.05755.
- [5] "SWExploit: Malicious GitHub issues against APR agents." arXiv:2509.25894.
- [6] "FCV-Attack: Functionally Correct but Vulnerable patches." arXiv:2510.17862 (ACL 2026 Main).
- [7] "IssueTrojanBench." arXiv:2607.20759.
- [8] "MalSkillBench." arXiv:2606.07131.
- [9] "DDIPE: Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems." arXiv:2604.03081.
- [10] "PhantomSkill." arXiv:2606.19191.
- [11] "XOXO: Cross-source context poisoning." arXiv:2503.14281.
- [12] "Iterative VibeCoding: Distributed Attacks in Persistent-State AI Control." arXiv:2607.02514.
- [13] "MCPTox." arXiv:2508.14925.
- [14] "MCP-TDP Security Benchmark." arXiv:2605.24069.
- [15] "ToolGuardian." arXiv:2607.21835.
- [16] "Agentic botnets / hallucination squatting." arXiv:2607.07433.
- [17] Maloyan & Namiot. "Prompt Injection Attacks on Agentic Coding Assistants." arXiv:2601.17548.
- [18] "Injection–Execution Dissociation: persistent memory attacks." arXiv:2605.08442.
- [19] "A focused survey of code agent security." Information and Software Technology (82 papers, 2024–2026).
- [20] "The Attack and Defense Landscape of Agentic AI." arXiv:2603.11088.
- [21] "The Balkanization of Execution-Security Research." arXiv:2607.05743.
- [22] "LLM Vulnerability survey." arXiv:2606.31639.
- [23] "Refusal Evaluation in Coding LLMs." arXiv:2605.20351.
- [24] "CodeSentinel." arXiv:2606.19235.
- [25] "TokenWall (Token-Flow Firewall)." arXiv:2607.08395.
- [26] "ClawGuard." arXiv:2604.11790.
- [27] "AgentLens." arXiv:2606.22673.
- [28] "Data Leakage Prevention." arXiv:2607.18847.
- [29] "AgentAntibody." arXiv:2608.04053.
- [30] "ARGUS." arXiv:2605.03378.
- [31] "Reasoning-enabled Task Alignment." arXiv:2606.15441.
- [32] "SIC." arXiv:2510.21057.
- [33] "AegisAgent." arXiv:2512.20986.
- [34] "ContainmentBench." arXiv:2607.23999.
- [35] Li & Zhao. "The Autonomy Tax: Defense Training Breaks LLM Agents." arXiv:2603.19423.
- [36] "MAGIC." ICML 2026.
- [37] "AdvEvo-MARL." ICML 2026.
- [38] "Self-RedTeam." ICML 2026.
- [39] "ARLAS." arXiv:2510.05442.
- [40] "RLbreaker." arXiv:2406.08705.
- [41] "Tool-Disguised Attacks via RL." arXiv:2601.05466.
- [42] "Robust Critics." arXiv:2607.20472.
- [43] "Dual-Adversarial Safety Alignment." arXiv:2608.09542.
- [44] "Tree-based DRL Red-Teaming." arXiv:2510.02286.
- [45] "AgentDojo." arXiv:2406.13352 (NeurIPS 2024 SafeBench).
- [46] "InjecAgent." arXiv:2403.02691.
- [47] "RAS-Eval." arXiv:2506.15253.
- [48] "AgentToolBench-Code." GitHub: allenwu-blip/agenttoolbench-code.
- [49] "CyberSecEval v1–v4." arXiv:2312.04724.
- [50] "Action-Graded Severity Scale." arXiv:2607.07474.
- [51] RADAR: "A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning." MIS Quarterly 2025. DOI:10.25300/misq/2024/17339.
- [52] ARText: "Assessing and Enhancing Adversarial Robustness of Predictive Analytics." Journal of Management Information Systems 2022. DOI:10.1080/07421222.2022.2063549.
- [53] GCNN/KVP: "Process data properties matter." Decision Support Systems 2021. DOI:10.1016/j.dss.2021.113494.
- [54] GASP: "A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks." JAIS 2025. DOI:10.17705/1jais.00941.
- [55] NPECF: "Network projection-based edge classification framework for signed networks." DSS 2020. DOI:10.1016/j.dss.2020.113321.