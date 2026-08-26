# -*- coding: utf-8 -*-
"""Write final CN audit document."""
import io

doc = r"""# 审计报告：全库全文筛选（388 篇金标准）× 三层检索式 对比验证

> 日期：2026-08-23
> 目的：验证 `security_fulltext_search_query.md` 的三层检索式（M1 元数据 / F2 head-8000 / F3 全文）能否完整召回"攻防安全"文献，回答"检索结果和全文筛选结果对得上吗"。
> 金标准：`runs\ais_basket_security_relevance_fulltext_flash_v1`（deepseek-v4-flash 全库 13,909 篇全文判定，security_include=388，0 失败）。
> 修正说明：decisions.jsonl 的 DOI 取自全文库 md 头部，与 CSV（按标题映射）有 166 处不一致（i/j 笔误、尾斜杠、个别错位如 28238）。本审计以"归一化标题 → CSV → CSV DOI"为主通道，DOI 仅作辅助，消除匹配噪声。

## 1. 结论摘要

1. **M1 元数据检索（SLR 标准第一筛）召回 365/388 = 94.1%**，补词后可达 385/388 = 99.2%；剩余 3 篇（04526/05690/22211）摘要中无任何攻防安全词，只能靠全文兜底。
2. **F2（head-8000）召回 381/388 = 98.2%**，可兜住大部分 M1 漏检；**F3（全文）召回 387/388 = 99.7%**，唯一漏检 22611（flaming）全文也无攻防词。
3. **M1 精度仅 14.6%（2,494 命中中只有 365 篇属金标准）**——这是关键词检索的正常水平（高召回、低精度），符合 SLR"先宽检索、再逐篇筛选"的惯例；不能直接用候选清单当结果，必须接摘要/全文级筛选。
4. **全文库存在 36 篇内容错配**（同一篇葡萄牙语哲学文章被错误填充），其中 2 篇（19853 假新闻检测、19862 黑客论坛文本挖掘）实为攻防安全文献却被金标准误排。二者元数据均已被 M1 命中——**检索式没错，是金标准（全文源）错了**。
5. **金标准 388 中约 15 篇边界存疑**（盗版/DRM/审计/腐败/取证类），需人工复核决定是否保留（详见第 6 节）。

## 2. 三层检索召回/精度（修正后）

| 检索层 | 金标准召回 | 召回率 | 命中数 | 对金标准精度 |
|---|---|---|---|---|
| M1 元数据（Title+Abstract+Keywords） | 365/388 | 94.1% | 2,494 | 14.6% |
| F2 head-8000 全文 | 381/388 | 98.2% | 4,896 | 7.8% |
| F3 全文 | 387/388 | 99.7% | 10,093 | 3.8% |

- M1 候选 2,494 个唯一 DOI（2,495 条记录）；原报告 2,499 为记录数，DOI 规范化去重后为 2,494。
- 噪声构成：M1 命中但金标准排除共 2,130 条，其中 1,524 条在全文库内（判定有据），606 条不在全文库 13,909 内（无判定记录，属 CSV 有而全文未下载）。
- F3 唯一漏检 22611（Flaming among first-time GSS users）：摘要、全文均无攻防词，属"全文判定宽口径纳入、检索词完全无法表达"的边界文。

## 3. M1 漏检 23 篇：分类与补词建议

全部 23 篇均在 CSV 中（元数据检索"够得到"），按是否可由补词召回分两类：

### 3.1 可经补词召回：20 篇（补词后 M1 召回 385/388 = 99.2%）

| 漏检文 | 缺的词（建议补入对应词块） |
|---|---|
| 01704 Doxing on SNS | doxing（→Q6 内容操纵） |
| 06126 Internet aggression | aggression（→Q6） |
| 06092 Online reputation systems | shill/shilling（→Q6，注意原词表 Q6 无 shill） |
| 10238 Software piracy attitude | piracy/pirated（→Q6 或新 Q11 盗版/DRM） |
| 10634 Griefing in virtual worlds | griefing（→Q6） |
| 09872 IT and government corruption | corruption/bribery（→Q6，若边界保留） |
| 12724 Platform protection & piracy | piracy/copyright（→新 Q11） |
| 13670 IP norms in online communities | intellectual property（→新 Q11） |
| 14334 DRM pricing | drm/copyright/rights management（→新 Q11） |
| 15370 Cyberharassment | cyberharass/harassment（→Q6） |
| 15516 Technological entitlement | computer abuse（→Q5 攻击者/威胁） |
| 20849 EDI controls DSS | audit/auditing/edp audit（→Q7 或新 Q11，若边界保留） |
| 21281 SDMI rights management | drm/copyright/rights management（→新 Q11） |
| 23404 IS forensics | forensic/forensics（→Q8 或新 Q11，若边界保留） |
| 22611 Flaming | flaming（→Q6；注意 F3 全文也无此词，补词可召回但判定为边界） |
| 25278 Anonymity in GSS | anonymous/anonymity（→Q7，需配合排除一般匿名研究） |
| 25539 Adult solicitor behaviour | solicitation/predation/grooming（→新 Q11 或 Q6） |
| 26923 Tradable reputation | audit/identity management（→Q6/Q7，边界） |
| 27203/27242 EDP audit | audit/auditing/computer audit（→Q7，若边界保留） |

### 3.2 摘要无任何攻防词、补词无效：3 篇（必须靠 F2/F3 兜底）

- 04526 Multi-tag RFID ownership transfer（2011, DSS）：所有权转移协议，摘要只讲供应链流转；F2/F3 命中（全文有攻击/安全协议建模）。
- 05690 Model checking for e-Business processes（2005, DSS）：模型检验设计保障，摘要无攻击词；F2/F3 命中。
- 22211 IS risk analysis based on business model（2003, I&M）：IS 风险分析，摘要无攻防词；F2/F3 命中。

> 含义：**"M1 补词 + F2 兜底"组合可覆盖 388 篇全部**（M1 补词后 385 篇，其余 3 篇 F2 命中）。这正好对应检索式文档第 4 节的"主检索式 + 全文兜底"分层策略。

## 4. 全文库内容错配：36 篇（重大数据质量问题）

- 发现方式：标题词在正文前 12,000 字符零命中的扫描（45 篇），人工核查确认 36 篇的正文是同一篇葡萄牙语哲学文章《NOMES DE LUGAR: CONFIM》(Massimo Cacciari, 2005)。
- 集中出现在 198xx/204xx/206xx（2021-2022 年 DSS 等刊），典型如 19853、19862、19841、19846、20419 等。
- **影响金标准**：其中 2 篇标题明确是攻防安全文献，但因全文错配被 LLM 判为"哲学文章"而误排：
  - `19853` Improving fake news detection with domain-adversarial and graph-attention neural network（2021, DSS）
  - `19862` A text-mining based cyber-risk assessment and mitigation framework for critical analysis of online hacker forums（2022, DSS）
  - 二者 M1/F2/F3 全部命中（元数据与检索式正常），**修正全文后应纳入金标准（金标准应修正为 390 篇）**。
- 其余 34 篇标题无安全相关（云计算、推荐系统、区块链供应链等），错配不影响安全筛选，但影响全库其他主题研究，建议整体修复。
- 金标准 388 内的 3 篇（00408/11082/14704）经核查全文内容正常，属扫描算法误报（标题词与正文格式差异），不构成问题。

## 5. 噪声复核（M1 命中但金标准排除）

### 5.1 标题含强攻击词但被排除（59 条）：仅 2 条为误排

- 误排：19853、19862（即第 4 节全文错配的 2 篇）——金标准应修正为纳入。
- 其余 57 条判定合理，主要类型：
  - exploration/exploitation、exploit 的普通用法误匹配（约 20 条，如 Exploitation vs. exploration、Juggling IT Exploration）；
  - 金融欺诈/财务造假（约 10 条，如 Financial fraud detection、Metafraud）——按边界属"无信息系统攻击成分的金融欺诈"，排除合理；
  - 攻击仅作背景的行为/组织研究（约 15 条，如数据泄露后购物意愿、投资者对勒索软件反应、OPM 泄露情绪分析）——判 peripheral/排除合理；
  - 现实世界犯罪/执法/公共安全（约 10 条，如警察安全、炭疽模拟、恐怖袭击后偏见检测）——排除合理。

### 5.2 判 peripheral 且 M1 命中（396 条）：边界案例备查

- 绝大多数为"安全/威胁仅作背景动机"的研究：访问控制方案（无攻击建模）、隐私增强工具、声誉计算综述、威胁评估决策支持、泄露后消费者/投资者行为等。
- 按检索式第 1.4 决策树第 3 步（对抗行为须为研究核心）排除合理；如需放宽（例如综述写作需要"安全背景"文献），可从 `audit_v3_final.md` 的 B2 清单按需取用。

## 6. 金标准 388 的边界审查（供人工复核，不改变检索结论）

以下类型在金标准中被纳入，但与"攻防安全"核心定义的契合度存疑，建议人工复核是否保留：

- **盗版/DRM/知识产权**（4 篇）：12724、13670、14334、21281——经济分析/方案设计，攻击者（盗版者）存在但通常无信息系统对抗环节。
- **审计/内控**（4 篇）：20849、27203、27242、26923（声誉交易审计）——审计技术或 EDP 审计，属合规与控制，非攻击检测。
- **腐败/犯罪治理**（1 篇）：09872——政府腐败与 IT，组织腐败而非系统攻击。
- **取证**（1 篇）：23404——数字取证综述，属事后调查。
- **行为研究宽口径**（4 篇）：06126（网络攻击行为威慑）、10634（griefing）、22611（flaming）、25539（网络性诱拐）——对"用户"的攻击行为研究，若严格限定"针对信息系统"则存疑，但对用户攻击属本系列（coding agent 安全）关心的安全类别，倾向保留。
- 022 篇 doxing（01704）与评论操纵（28238 好评返现）判定合理，建议保留。

> 复核建议：若论文写作需要"纯攻防算法/机制"文献，按上述清单剔除后约 370-375 篇；若需要攻防全谱（含行为、经济、治理），388 篇可整体保留。

## 7. v2 算法开发金标准（99 篇）在新金标准中的覆盖

- 99 篇中 92 篇被 388 覆盖；7 篇未覆盖：5972（微数据掩蔽）、13656（身份匹配）、14514（层级密钥管理）、9492（漏洞-安全画像 GA）、12794（事务数据隐藏）、13760（安全联邦）、19544（Web 图构建）。
- 7 篇均被判 security_peripheral_context 或 no_security_relevance——即在新口径（要求"恶意/对抗行为者为核心"）下被排除，符合预期（多为无攻击建模的隐私保护/访问控制方案）。
- 若后续综述需要这些"隐私保护算法"文献，可从 99 篇清单单独取用。

## 8. 结论与建议（检索式可用性）

1. **M1 单独可用但需补词**：当前 94.1% 召回；按第 3.1 节补 20 词后 99.2%。建议新增 Q10（提示注入/LLM 安全，面向增量语料）与 Q11（盗版/DRM/取证/审计，按边界取舍）。
2. **推荐组合：M1（补词）+ F2 兜底**，覆盖 100% 金标准；F2 仅需对"M1 未命中"的约 2,400 篇全文做 head 扫描（已有清单 `fulltext_candidates_head8000_Q1-Q8_extra.txt`）。
3. **精度预期**：M1 精度 14.6% 属正常，SLR 流程中候选清单之后必须接摘要级 LLM/人工筛选；本运行（全文级判定）的 388 篇可作为该筛选的预标注结果。
4. **必须先修数据**：36 篇全文错配（含 2 篇安全文献）需重新下载正确全文并重判；修复后金标准应为 390 篇，M1/F2/F3 召回率不变（2 篇已被检索命中）。
5. **结果文件**：本审计数据文件见 `output_v1\audit_v3_final.md`（全量 B1/B2 清单）、`output_v1\audit_v2_corrected.md`（修正前后对比）、`output_v1\missed23_keywords.txt`（漏检补词明细）、`output_v1\corpus_mismatch_scan.txt`（全文错配扫描）。
"""

path = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1\audit_final_cn.md"
with io.open(path, "w", encoding="utf-8") as f:
    f.write(doc)
print("written", path)
