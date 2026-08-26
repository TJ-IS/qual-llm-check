# AIS 安全文献全文检索式 + "攻防安全"术语边界界定

> 目的：检索 AIS 文献库中**所有**与"攻击/漏洞"相关的安全文献——不局限于算法开发（区别于 99 篇筛选），作为 coding agent 安全研究系列的文献综述底座。
> 基准：以 99 篇（`ais_basket_security_algorithm_development_flash_v2` 严格筛选通过）作为 recall 测试集；本检索式要求对 99 篇召回率 ≥ 98%。
> 测试方式：按 SLR 惯例以**标题+摘要+关键词**为主检索（`database\ALL_AIS_Basket_11.csv`，17,745 条）；全文/head 范围为兜底口径。均为大小写不敏感子串匹配（非分词、非语义）。

## 1. "攻防安全"术语边界：先界定范围，再谈检索式

用户尚未确定"攻防安全"的边界，本节约定一套可操作的定义，供确认或修改。

### 1.1 核心定义（纳入标准）

**一篇文献属于"攻防安全"，当且仅当：存在恶意或对抗行为者，其行为是直接针对信息系统、系统用户或系统所依赖数据的攻击、操纵或滥用；或文献的研究核心是该类威胁的检测、防御、缓解、评估与建模。**

三个要素（缺一不可）：

1. **malicious_or_adversarial_actor_central**：恶意/对抗行为者存在，且其对抗行为是研究问题本身的核心对象（不是动机背景或应用场景）。
2. **security_damage_scope**：损害对象是信息系统、其用户或组织的安全属性——机密性、完整性、可用性、真实性（含隐私披露、身份真实性、内容真实性）。
3. **attack_defense_detection_focus**：研究核心围绕攻击的实施，或威胁的检测、防御、缓解、评估、建模。

### 1.2 纳入的攻击类型清单（满足任一即进入候选）

| 类别 | 具体攻击/威胁 |
|---|---|
| 恶意代码与系统破坏 | 恶意软件、勒索软件、病毒/蠕虫、木马、僵尸网络、后门、键盘记录器、间谍软件、逻辑炸弹、供应链投毒、隐蔽信道/隐写、恶意浏览器扩展 |
| 网络攻击与入侵 | 入侵检测/响应、DoS/DDoS、端口扫描、中间人、会话劫持、漏洞利用、零日漏洞、SQL/命令/代码注入、XSS、权限提升、未授权访问、沙箱逃逸 |
| 社会工程与内容攻击 | 钓鱼（网页/邮件/短信）、鱼叉钓鱼、BEC、社交工程、假冒/冒充网站、**提示注入/越狱（针对 AI/LLM 系统）**、虚假信息/假新闻/深度伪造、网络欺凌、评论/评分操纵、托攻击（shilling）、刷粉/假账户 |
| 机密性与数据泄露 | 隐私披露攻击（重识别、属性推断、记录链接）、推断攻击（snooping）、内部威胁/恶意内部人员、凭据与密钥窃取、数据泄露/外传、匿名化/脱敏/净化的防御 |
| 威胁情报与攻击侧 | 威胁情报、漏洞情报与管理、暗网/黑客社区监测、exploit 关联、攻击仿真与攻防博弈、攻击者画像 |
| AI/ML 安全 | 对抗样本、对抗训练、模型鲁棒性、模型投毒、提示注入、越狱、用 LLM 生成恶意内容（攻击侧） |

### 1.3 明确排除的类型（出现即排除，除非全文证据表明研究核心回到 1.1）

- **传统犯罪预防与执法优化**：犯罪热点预测、警力巡逻、嫌疑人识别、身份匹配辅助调查等（现实世界犯罪，无信息系统对抗环节）。
- **金融市场监管与欺诈（无信息系统攻击成分）**：市场操纵监视、会计/审计欺诈、财务造假、信用风险、一般信用卡欺诈（除非明确涉及钓鱼、社交工程、账户盗用或网络攻击）。
- **一般内容质量与有用性**：评论有用性/垃圾评论分类、情感分析（除非恶意操纵是问题核心）。
- **一般信任与信誉计算**：声誉系统改进、推荐可信度、社交推荐（除非对抗性操纵的检测/防御是核心）。
- **隐私主观感知/法规遵从**：隐私担忧、隐私偏好、GDPR 遵从（无攻击或防御算法）。
- **数据质量/清洗/缺失值**（无恶意方）。
- **一般预测/推荐/优化**（无对抗情境）。
- **一般鲁棒性/稳定性**（无攻击者的鲁棒性研究不算；"adversarial robustness"才算）。
- **一般加密/访问控制方案**：仅方案+可行性验证、无攻击建模、无新计算方法与基准比较（这类按 v2 口径不算算法开发；在新检索中也不属于"攻击/漏洞相关"核心，除非研究威胁模型与攻击评估）。
- **组织安全治理/安全文化/政策合规**：不围绕攻击或漏洞的研究。
- **泛化公共安全**：自然灾害、医疗急救、食品安全等。

### 1.4 争议区的判定规则（决策树）

对每篇候选文献依次回答：

1. 文中是否有明确的恶意/对抗行为者（attacker、adversary、malicious actor、hacker、malicious insider、threat actor）或攻击性动作（attack、intrusion、exploit、manipulation、fraud 且有网络攻击成分、poisoning、injection）？
   - 否 → **排除**（"security" 字样只是语境）。
2. 该行为/行为者是否直接针对信息系统、系统用户或系统数据？
   - 否（针对现实世界犯罪、纯市场欺诈、人的心理欺骗但无系统环节）→ **排除**。
3. 该对抗行为是否构成研究问题的核心（而非动机背景）？
   - 否 → **排除**（标记 security_peripheral_context）。
4. 研究内容是否围绕攻击实施、或威胁的检测/防御/缓解/评估/建模？
   - 是 → **纳入**，然后区分：算法开发型（核心贡献是新计算方法+实证评估）／非算法型（实证、行为、组织、综述，仅作综述背景）。
5. 特殊类别复核：
   - 金融欺诈：有钓鱼/盗号/网络攻击/系统操纵成分才纳入；
   - 执法/犯罪：有信息系统攻击或系统数据操纵环节才纳入；
   - 评论/信誉：有操纵攻击检测/防御核心才纳入；
   - 隐私：有披露攻击（重识别/推断/记录链接）或匿名化防御才纳入；
   - AI/ML：有对抗者（对抗样本/投毒/注入/越狱）才纳入，一般模型性能不算。

### 1.5 为什么这样界定（依据）

- 与 v2 筛选提示词 1.1–1.3 完全一致：本边界就是 v2 的"安全相关性"定义的展开版，99 篇全部满足本边界（可用 99 篇作校准集）。
- 边界比 v2 更强调"攻击/漏洞"而非"安全"：因为新检索目的不是找所有安全文献（那会包含安全投资、安全管理等），而是找 coding agent 安全研究最需要的"威胁知识"来源——攻击侧与漏洞侧。
- 纳入清单中特别加入"提示注入/越狱/AI 滥用/对抗样本"：这是 99 篇里仅有零星覆盖、但对 coding agent 安全最核心的新兴类别，检索式必须为它们预留词块，避免把 2020 后的相关文献漏掉。

## 2. 检索式（9 个词块）

以下词块可直接用于本地全文子串检索（也可翻译成标题-摘要-关键词检索）。术语均为小写；检索时大小写不敏感。

### Q1 恶意代码/隐蔽传输（22 词）
malware, malicious software, malicious code, malicious program, malicious application, malicious file, ransomware, trojan, botnet, keylogger, spyware, backdoor, computer virus, email worm, malicious payload, worm, virus propagation, malware propagation, malicious app, steganography, steganographic, covert channel

### Q2 入侵/网络攻击/漏洞利用（30 词）
intrusion detection, intrusion, denial of service, denial-of-service, ddos, network attack, cyberattack, cyber attack, cyber-attack, attack detection, attack graph, sql injection, code injection, command injection, cross-site scripting, zero-day, exploit, vulnerability, vulnerable, unauthorized access, privilege escalation, account takeover, credential theft, data breach, data exfiltration, network security, security attack, attack simulation, attack surface, port scan

### Q3 对抗/AI 安全（7 词）
adversarial, adversary, adversarial attack, adversarial example, adversarial robustness, attack model, threat model

### Q4 钓鱼/认证（16 词）
phishing, spear phishing, social engineering, fake website, spoofing, spoof, deceptive, identity theft, credential, password, impersonation, masquerade, authentication, access control, authorization, key management

### Q5 攻击者/威胁（15 词）
attacker, malicious actor, malicious insider, insider threat, cybercriminal, cyber criminal, hacker, hacking, threat intelligence, cyber threat, advanced persistent threat, threat actor, malicious, cybercrime, cyber crime

### Q6 内容操纵/虚假信息（27 词）
fake review, review manipulation, opinion spam, shilling attack, rating manipulation, fake news, false news, misinformation, disinformation, false information, fake follower, social bot, bot detection, cyberbullying, spam, spamming, deceptive review, fraudulent review, fake account, manipulation, fake content, manipulative, fraud, fraudulent, deception, deceit, concealed information

### Q7 隐私披露/数据保护（34 词）
re-identification, reidentification, de-identification, deidentification, disclosure risk, attribute disclosure, identity disclosure, record linkage, k-anonymity, k-anonymization, anonymization, anonymizing, data masking, data perturbation, data sanitization, privacy-preserving, privacy protection, privacy attack, inference attack, snooping, snooper, confidential data, sensitive data, sensitive information, data leakage, information leakage, privacy disclosure, privacy breach, deanonymization, de-anonymization, statistical disclosure, privacy, confidentiality

### Q8 威胁情报/漏洞管理（27 词）
dark web, darknet, dark net, hacker forum, hacker community, underground forum, underground economy, carding, cve, vulnerability management, vulnerability assessment, security vulnerability, countermeasure, security controls, security control, security investment, security risk, cyber risk, cyber insurance, information security, it security, cybersecurity, cyber security, security monitoring, security management, security analytics, honeypot

### Q9 通用宽词（6 词，仅作安全网，不建议单独使用）
attack, security, threat, robustness, defense, detection

> **注**：术语清单已含面向 AI 时代的补充（prompt injection / jailbreak 建议加入 Q3 或单独 Q10）：prompt injection, jailbreak, llm security, model poisoning, data poisoning, adversarial prompt, tool poisoning。本地 13,910 篇语料中这些词出现率极低（2019 年前文献不会出现），但检索未来增量语料时需要。可以在本地测试后追加：在 99 篇上这些词贡献为 0，不影响召回。

## 3. Recall 测试结果（99 篇基准，13,910 篇）

> 重要修正（2026-08-23 v2）：第一版把检索范围设为"全文"，导致 Q1–Q8 全量命中 10,093 篇（占全库 72.6%），其中 9,031/12,070 的命中只出现在参考文献或正文深处——全文范围对"筛选"几乎没有区分力，已废弃为"主检索式"，仅保留为最终查漏安全网。
> 修正后的推荐口径：**检索范围 = 每篇 md 的前 8,000 字符（标题+作者+摘要+关键词+引言开头，远早于参考文献）**；术语 = Q1–Q8（183 词）+ 补充词 {collusion, ballot stuffing, badmouthing, identity fraud, impersonation attack}（5 词）。

### 3.1 修正前后对比（99 篇基准）

| 变体 | 检索范围 | 99 命中 | 召回率 | 语料命中 | 命中密度(99/命中) |
|---|---|---|---|---|---|
| V6 旧版 Q1–Q8 全文 | 全文 | 99 | 100.0% | 10,093 | 0.98% |
| V5a Q1–Q8 | head 8,000 | 98 | 99.0% | 4,887 | 2.01% |
| **V5b Q1–Q8+补充词（推荐主用）** | **head 8,000** | **99** | **100.0%** | **4,896** | **2.02%** |
| V3 短语+强攻击单数 | head 8,000 | 94 | 94.9% | 1,258 | 7.47% |
| V1 仅多词短语 | head 8,000 | 85 | 85.9% | 962 | 8.84% |

- V5b 相对旧版全文检索：候选数从 10,093 → 4,896（-51.5%），99 篇基准召回保持 100%。
- V3（1,258 篇）适合快速主题探测：会漏掉 5 篇边界案例（多为隐私披露/内容操纵类），但在 99 篇基准上仅 94.9% 召回，不作为主检索。

### 3.2 各词块独立召回（head 8,000 范围）

| 词块 | 99 命中 | 99 召回率 | 语料命中 |
|---|---|---|---|
| Q1 恶意代码 | 41 | 41.4% | 619 |
| Q2 入侵/网络攻击 | 87 | 87.9% | 3,696 |
| Q3 对抗/AI 安全 | 35 | 35.4% | 298 |
| Q4 钓鱼/认证 | 69 | 69.7% | 1,583 |
| Q5 攻击者/威胁 | 72 | 72.7% | 820 |
| Q6 内容操纵 | 68 | 68.7% | 2,169 |
| Q7 隐私披露 | 79 | 79.8% | 2,663 |
| Q8 威胁情报/漏洞 | 70 | 70.7% | 1,308 |

（head 范围下各块命中数普遍减半以上，Q2 从 6,056 → 3,696、Q7 从 4,129 → 2,663。）

### 3.3 漏检分析与补充词

- head 8,000 + Q1–Q8 原词表：98/99，漏 1 篇——12102（Filtering trust opinions through RL，关键词为 Trust/Reputation/Credibility/**Collusion**，"collusion"不在原词表）。
- 补充 5 词后：99/99。补充词噪声可控：如 "collusion" 在 head 范围仅命中 15 篇（含 99 篇 1 篇），多为主办拍卖/犯罪网络/财务舞弊类，按边界决策树可筛除。
- 依赖脆弱性：仅被 1 个词块覆盖的 99 篇仍为 21403（仅 Q6）、10412（仅 Q6）、14422（仅 Q7）；Q6、Q7 不可裁。


### 3.4 SLR 标准做法：标题+摘要+关键词检索（2026-08-23 v3，推荐主用）

用户指出 SLR 传统做法是对标题和摘要检索。本地恰好有完整元数据：`database\ALL_AIS_Basket_11.csv`（Scopus 导出，17,745 条，**空摘要 0 条**，含 Title/Abstract/Author Keywords/Index Keywords/DOI/Year/Source title）。

- **检索范围**：Title + Abstract + Author Keywords + Index Keywords（Scopus 标准 SLR 字段，全部小写子串匹配）
- **词表**：Q1–Q8（183 词）+ 补充 5 词（collusion 等），与 head-8,000 版一致
- **结果：元数据命中 2,499 条；99 篇基准召回 98/99（98.99%）**
- **唯一漏检**：13656（Complex Problem Solving: Identity Matching，JAIS 2007）——其摘要与关键词通篇为 drug crimes / crime investigation / identity matching，不含任何攻防词；该文本就是已标注的疑似误判（执法身份匹配，v2 排除类型）。即：**元数据检索在 99 篇上的漏检恰好只有一篇误判文章**。
- 各词块元数据命中：Q1 58、Q2 672、Q3 61、Q4 177、Q5 155、Q6 403、Q7 474、Q8 431。
- 候选清单：`output_v1/slr_metadata_candidates.txt`（含记录索引/标题/年份/期刊/DOI）。
- 报告：`output_v1/slr_metadata_search_report.md`。

**与 head-8,000 全文版的关系**：元数据检索（2,499）比 head-8,000（4,896）再压一半，且解决了 16 篇 INFORMS 全文无摘要的本地格式缺陷（元数据含全部摘要）。head-8,000 版保留为"全文库内兜底"：对元数据未命中的全文文件，若 head 命中则人工复核（可补回 13656 这类元数据漏检）。

### 3.5 三层口径总结（从精到宽）

| 口径 | 检索范围 | 命中数 | 99 召回 | 用途 |
|---|---|---|---|---|
| **M1 元数据（推荐主用）** | Title+Abstract+Keywords（CSV） | **2,499** | **98/99（漏检=误判文）** | SLR 标准第一筛 |
| F2 head-8,000 | 本地全文前 8,000 字符 | 4,896 | 99/99 | 全文库兜底/查漏 |
| F3 全文 | 本地全文全部字符 | 10,093 | 99/99 | 仅最终安全网 |
## 4. 使用建议（分层策略）

1. **主检索式（SLR 标准，推荐）**：在 `database\ALL_AIS_Basket_11.csv` 的 Title+Abstract+Author Keywords+Index Keywords 上跑 `Q1 OR Q2 OR ... OR Q8 OR 补充词` → **2,499 条候选**。后续按第 1 节边界决策树做摘要级筛选（LLM 或人工），需要全文时再从 `database_fulltext_all` 取对应文件。候选清单：`output_v1/slr_metadata_candidates.txt`。
2. **主题分层**：分别跑 Q1–Q8（元数据层）得到各威胁族候选，便于分头写文献综述（恶意代码/对抗、内容操纵、隐私披露、威胁情报、钓鱼）。
3. **快速探测**：V3（短语+强攻击单数，head 8,000）→ 1,258 篇，适合先粗看主题分布，再回到主检索式补全。
4. **全文兜底**：对元数据未命中但本地全文 head-8,000 命中的文件（约 2,400 篇差集）做轻量复核，可补回元数据层面漏检的文献（如 13656 这类摘要无攻防词的案例）。
5. **未来增量**：对 2024 年后文献追加 Q10（prompt injection、jailbreak、LLM security、model/data poisoning、adversarial prompt、tool poisoning、sandbox escape、exfiltration）。本地 13,910 篇语料中这些词出现率极低，不影响当前召回；检索未来增量语料时必须加入。
6. **必做后处理**：子串匹配仍会把"攻击"类词的普通用法（exploit the data、attack the problem、vulnerability of the design）计入——但 head 范围已消除参考文献区的绝大部分噪声；真正纳入数仍需按 1.1–1.4 逐篇判定。

## 5. 与 99 篇筛选的关系

- 99 篇筛选 = 本检索式（元数据 M1 为主、全文兜底）∩ 算法开发门槛 ∩ 安全核心门槛，且经过了逐篇 LLM 全文判定。
- 新检索 = 只过 T6 词块 + 第 1 节边界，**去掉算法开发门槛** → 会得到比 99 篇更宽的集合，包括：行为/实证研究（如钓鱼易感性实验）、组织研究（如安全事件影响）、综述与观点文（提供理论与引文支持）、以及 v2 排除的安全投资/治理类（但需按边界再筛，投资类多属于"无攻击核心"）。
- 建议最终产出三层清单：①攻防安全+算法开发（≈99 篇，已有）；②攻防安全-非算法（新检索新增，供理论/引文）；③边界争议清单（供人工复核）。
- 检索式与边界均可用 99 篇作为回归测试集：任何词块修改后重跑 `slr_metadata_search.py`（元数据）与 `fulltext_scan_head.py`+`fulltext_precision_variants.py`（全文兜底），要求 M1 召回 ≥ 98%（当前 98/99=98.99%，漏检为误判文）、全文兜底 100%。

## 6. 可复现性

- 脚本：`slr_metadata_search.py`（元数据检索+99 召回报告）、`fulltext_recall_test.py`（全文扫描）、`fulltext_scan_head.py`（head-8,000 扫描）、`fulltext_precision_variants.py`（精度变体对比）、`gen_candidates_head.py`（全文候选清单）
- 元数据源：`database\ALL_AIS_Basket_11.csv`（17,745 条，Scopus 字段，空摘要 0）
- 缓存：`output_v1/fulltext_scan_cache.pkl`（全文）、`output_v1/fulltext_scan_head_cache.pkl`（head-8,000）
- 报告：`output_v1/slr_metadata_search_report.md`、`output_v1/fulltext_precision_analysis.md`、`output_v1/fulltext_recall_report.md`、`output_v1/fulltext_tier_analysis.md`
- 候选清单：`output_v1/slr_metadata_candidates.txt`（2,499 条，主检索式）；`output_v1/fulltext_candidates_head8000_Q1-Q8_extra.txt`（4,896 篇，全文兜底）；`output_v1/fulltext_candidates_T6_Q1-Q8.txt`（10,093 篇，全文安全网）
- 测试日期：2026-08-23；99 篇 DOI 映射 99/99；主检索式（元数据）召回 98/99（唯一漏检为已标误判文 13656）；全文兜底召回 99/99。






## 7. 与 388 篇全文筛选金标准的对比验证（2026-08-23 更新）

> 全库全文筛选（deepseek-v4-flash，13,909 篇，
uns\ais_basket_security_relevance_fulltext_flash_v1）产出攻防安全金标准 388 篇后，对本检索式三层口径做了完整对比。完整报告见 
uns\ais_basket_security_relevance_fulltext_flash_v1\output_v1\audit_final_cn.md。

### 7.1 三层召回/精度（标题主通道匹配，DOI 修正后）

| 检索层 | 金标准召回 | 召回率 | 命中数 | 精度 |
|---|---|---|---|---|
| M1 元数据 | 365/388 | 94.1% | 2,494 | 14.6% |
| F2 head-8000 | 381/388 | 98.2% | 4,896 | 7.8% |
| F3 全文 | 387/388 | 99.7% | 10,093 | 3.8% |

- M1 补词后可达 385/388（99.2%），剩余 3 篇（04526/05690/22211）摘要无任何攻防词，需 F2 兜底；**M1（补词）+ F2 组合覆盖 100%**。
- 精度 14.6% 属关键词检索正常水平，候选清单必须接摘要/全文级筛选（本 388 篇可作预标注）。

### 7.2 应补词（M1 漏检 20 篇的元数据命中词）

doxing / aggression / griefing / flaming / cyberharass(ment) / shill(shing) / piracy / pirated / copyright / drm / rights management / intellectual property / computer abuse / forensic(s) / audit(ing) / edp audit / corruption / solicitation / predation / grooming / anonymous-anonymity（需配合排除一般匿名研究）/ identity management（边界）。

### 7.3 数据质量警示

- 全文库 36 篇内容错配（198xx/204xx/206xx，正文为同一哲学文章），其中 2 篇（19853 假新闻检测、19862 黑客论坛文本挖掘）实为攻防安全文献，金标准误排、检索式正常命中；修复全文后金标准应为 390 篇。
- 金标准 388 中约 15 篇边界存疑（盗版/DRM/审计/腐败/取证类），按写作需要人工复核取舍。
