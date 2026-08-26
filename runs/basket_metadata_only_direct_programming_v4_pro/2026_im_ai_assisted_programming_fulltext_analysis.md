# Chang & Huang (2026) Full-Text Analysis

## Bottom line

This is a genuinely relevant **individual-level AI-assisted programming** paper. It should enter the review's modern core pool. It is not, however, an observational or experimental study of a concrete coding task, and it does not isolate autonomous/agentic coding. It is a cross-sectional developer survey that models perceived AI reliance and perceived systems-development performance.

The full reference list contains 113 entries. Exact comparison against the 20 seed records produced:

- DOI matches: 0/20
- Exact-title matches: 0/20

The paper therefore cites none of the 20 seeds. This confirms the earlier Scopus `REFEID` result.

## What the paper studies

The paper asks:

1. What makes programmers rely more heavily on generative AI during software development?
2. Does greater AI reliance improve systems-development performance?

It defines AI reliance as deliberate task-oriented dependence on AI-generated outputs, beyond merely using or trusting the tool. The empirical context includes ChatGPT, GitHub Copilot, and Amazon Q Developer.

The theoretical model combines three streams:

- Theory of technology dominance (TTD): experience and repeated successful interaction lead people to incorporate intelligent-system outputs into their judgment.
- Task–technology fit (TTF): AI is more useful when its capabilities fit the development task.
- Knowledge integration: developers must combine AI-generated suggestions with their own expertise before those suggestions become useful performance inputs.

The tested paths are:

```text
Task experience ──> AI reliance ──> Knowledge integration ──> Systems-development performance
                         │                                      ▲
                         └──────────────────────────────────────┘

Task–technology fit ──> AI reliance
Task–technology fit ──────────────────────────────────────────> Performance
```

## Data and method

- Online survey conducted in Taiwan during November–December 2023.
- Respondents had to report using generative AI for program development within the preceding three months.
- 972 invitations; 315 responses; 4 duplicate cases removed; final N = 311.
- Respondents came from top-500 Taiwanese firms and the Taipei Computer Association; 35.4% were titled programmers, with the remainder including systems analysts, data engineers, multimedia programmers, information-management staff, and others.
- All focal variables were seven-point self-report scales measured in the same questionnaire.
- Analysis used PLS-SEM with 5,000 bootstrap resamples.

## Main statistical results

All proposed paths were statistically significant:

| Path | Standardized coefficient |
|---|---:|
| Experience → AI reliance | 0.263 |
| Task–technology fit → AI reliance | 0.591 |
| Task–technology fit → performance | 0.387 |
| AI reliance → knowledge integration | 0.715 |
| AI reliance → performance | 0.139 |
| Knowledge integration → performance | 0.365 |

The reported R² values were 0.579 for AI reliance, 0.512 for knowledge integration, and 0.660 for systems-development performance. Knowledge integration partially mediated the relation between AI reliance and performance. The direct AI-reliance coefficient was comparatively small (0.139); much of the relationship operated through the self-reported knowledge-integration construct.

## What the paper actually establishes

The defensible conclusion is:

> Among surveyed developers who already used generative AI, those reporting stronger task–AI fit, AI reliance, and knowledge integration also reported better systems-development outcomes.

The stronger wording used in the paper—generative-AI reliance “improves” performance or “empirically validates” benefits—is not supported causally by the design. The study has no pre/post comparison, control group, randomized treatment, behavioral usage log, concrete programming task, code-quality measure, or independently assessed project outcome.

## Measurement concerns

1. **AI reliance mixes several constructs.** Its items include identifying with AI output, judging output trustworthy, using AI-assisted decisions, and relying on output. Trust and reliance are claimed to be distinct theoretically but are partially recombined in the measurement.
2. **Task experience is an unusual reflective scale.** Items cover full-time work, supervision, internships, and self-reported achievements. Its sources are résumé/hiring studies rather than programming-expertise research.
3. **TTF is generic.** Items say that AI is suitable, sufficient, or fits “my work”; they do not measure fit to a specified coding task or distinguish code generation, debugging, comprehension, testing, and design.
4. **Performance is perceived project/system performance.** Items cover customer satisfaction, reliability, debugging burden, budget, schedule, and comparative productivity. They are not objective individual programming performance.
5. **Same-source cross-sectional measurement creates endogeneity and common-method risks.** Positive project outcomes could raise perceived fit and reliance, rather than only the reverse. Harman's single-factor test and VIF checks cannot establish that this risk is absent.
6. **Heterogeneity is not modeled.** Tool type, task type, project complexity, degree of AI autonomy, role, organization, and experience level are not used as boundary conditions. Task complexity is explicitly omitted from the model.
7. **The study concerns AI assistance, not coding agents specifically.** It treats ChatGPT, Copilot, and Amazon Q as one broad category and does not measure planning autonomy, multi-step action, repository access, tool use, or delegated task completion.

## Why none of the 20 seeds is cited

The citation gap is best explained as a difference in **theoretical lineage and unit of analysis**, not as evidence that the seeds are irrelevant.

### 1. The paper is construct-driven, not programming-cognition-driven

The authors organize the review around AI reliance, TTD, TTF, knowledge integration, and systems-development performance. They cite the canonical or scale-providing sources for those constructs. Programming is the application setting in which a general organizational-behavior model is tested.

The 20 seeds instead ask how people comprehend, write, modify, test, inspect, debug, or formulate code/queries, often through controlled tasks and objective performance. Those studies belong to a human-programming cognition/task-performance lineage that the paper never reconstructs.

### 2. The outcomes do not require the seed literature operationally

The paper does not measure program comprehension, query construction, spreadsheet error correction, code inspection, modification accuracy, test-driven development, or pair-programming productivity. Consequently, the seed papers are not needed to supply its measures or hypotheses. Its dependent variable comes from a socio-technical systems-development-performance scale, not a programming-task metric.

### 3. Its discovery vocabulary favors recent GenAI and organizational IS work

The paper's visible search vocabulary is AI reliance, trust, adoption, task–technology fit, knowledge integration, software-development performance, ChatGPT, and Copilot. Many seeds are indexed under older labels such as program comprehension, application-domain knowledge, query formulation, end-user computing, spreadsheet development, cognitive fit, or pair programming. A recent-keyword search would not naturally retrieve them.

### 4. The authors follow an adjacent IS lineage

The paper does cite older and Basket-adjacent systems-development studies—for example, distributed cognition in software design, agile development, systems-development controls, knowledge integration, and software-product organization. This shows that the omission is not simply “old papers were excluded.” The selected lineage is project/process/organizational performance rather than concrete programming activity.

### 5. The review is present-focused and selectively assembled

The 113 references include many 2023–2025 AI sources, conference papers, practitioner reports, a GitHub blog, a Thoughtworks post, a Medium article, and a programming-with-Copilot book. This is consistent with a rapidly assembled emerging-topic review, not systematic backward/forward citation tracing from foundational human-programming studies.

## Which seed omissions matter most

It would not be reasonable to expect all 20 seeds to be cited. Spreadsheet, SQL, and database-representation studies are distant from this paper's survey model. Several omissions are nevertheless conceptually important:

- **The Role of Cognitive Fit in the Relationship Between Software Comprehension and Modification** (2006): directly links developer mental representations, comprehension, modification, cognitive fit, and performance. This is the clearest missing bridge to the paper's claims about cognitive alignment and task execution.
- **The Relevance of Application Domain Knowledge** papers (1995 and 1998): directly support the role of programmer experience and domain knowledge in evaluating and understanding code.
- **Why Is Programming (Sometimes) So Difficult?** (1997): supplies a programming-specific account of cognitive complexity that would strengthen the otherwise generic treatment of programming as an inherently complex task.
- **Are Two Heads Better than One for Software Development?** (2009): provides an individual/task productivity precedent for collaborative programming and would be a useful contrast for the “AI pair programmer” idea.
- **Performance Outcomes of Test-Driven Development** (2020): illustrates how programming-performance claims can be tested with an actual development intervention and task outcomes rather than only self-report.

## Implication for the systematic review

This paper should be coded as:

- Direct AI-assisted programming: **yes**
- Individual developer constructs: **yes**
- Human–AI interaction central: **yes**
- Concrete observed coding task: **no**
- Objective programming performance: **no**
- Coding-agent autonomy specifically measured: **no**
- Cites any of the 20 seeds: **no**
- Conceptually reconnects to the seed lineage: **yes, but without bibliographic acknowledgment**

It is therefore best treated as a **modern conceptual bridge/core survey paper**, alongside—but analytically separated from—task-based coding-agent studies. Its existence weakens the claim that the Basket has no modern individual-level AI-programming work, but its missing citations demonstrate that the older human-programming lineage was not carried forward explicitly.
