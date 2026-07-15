---
theme: scholarly
title: Coding-Agent Situation Awareness
description: Construct development plan for coding-agent situation awareness
authors:
  - name: Fangzhan Lin
    institution: Tongji University
footerLeft: Coding-Agent Situation Awareness
footerMiddle: Construct Development Proposal
class: text-left
transition: slide-left
mdc: true
aspectRatio: 16/9
lang: en
themeConfig:
  colorTheme: oxford-burgundy
  sectionMode: light
  outlineToc: true
  outlineTocOpen: false
  beamerNav: true
---

# Coding-Agent Situation Awareness

## Conceptualization and Measurement for Agentic Software Development Tasks

<div class="cover-keywords">
<Keywords :keywords="['Coding Agents', 'Situation Awareness', 'Construct Development', 'Measurement']" />
</div>

<!-- Source order: cover. -->

---
layout: default
class: opening-slide
---

# Software Development Is Becoming an AI-Mediated Production Activity

<div class="opening-stats">
<div><strong>20–45%</strong><span>Potential direct productivity impact relative to annual software-engineering spending</span></div>
<div><strong>84%</strong><span>Developers who use or plan to use AI development tools in the 2025 survey</span></div>
<div><strong>Agentic IS</strong><span>Systems can accept goals, initiate actions, and adapt to feedback</span></div>
</div>

<div class="argument-band">
Software engineering combines substantial economic value, rapid AI adoption, and a broader shift from responsive tools to agentic information systems.
</div>

<p class="citation-line">McKinsey Global Institute (2023); Stack Overflow (2025); Schuetz and Venkatesh (2020); Baird and Maruping (2021)</p>

<!-- Source order: 54, Section 1.1.1, D2-D3. -->

---
layout: default
class: definition-slide
---

# Coding Agents Execute Tasks, Not Isolated Suggestions

<div class="definition-box">
A coding agent is an AI agent that accepts a software-development goal and, within a permission boundary, acquires project context, plans steps, invokes tools, modifies software artifacts, evaluates execution results, and continues adapting its actions.
</div>

<div class="plain-columns compact-top">
<div>
<h3>Unit of delegation</h3>
<p>A complete or relatively complete development task rather than one completion or one generated passage.</p>
</div>
<div>
<h3>Defining capability</h3>
<p>The system selects an action sequence and changes the software workspace without requiring the user to specify every operation.</p>
</div>
</div>

<p class="citation-line">Baird and Maruping (2021); Kumar et al. (2025)</p>

<!-- Source order: 54, Section 1.1.1, D3 and D6. -->

---
layout: default
class: compare-slide
---

# Delegation Changes How Users Participate in Software Tasks

<div class="flat-compare">
<div>
<span>Traditional development tools</span>
<h3>Users directly perform the operations</h3>
<p>Edits and state changes can usually be connected to the user's own commands, clicks, and action memory.</p>
</div>
<div>
<span>Coding agents</span>
<h3>Users delegate goals and judge the evolving task</h3>
<p>Task definition, context provision, action confirmation, change interpretation, and later decisions coexist with direct operation.</p>
</div>
</div>

<div class="argument-band">
The relationship between the user and software change becomes partly indirect because the agent moves the task forward on the user's behalf.
</div>

<!-- Source order: 54, Section 1.1.1, D4-D7. -->

---
layout: default
class: evidence-slide
---

# Delegation Does Not Eliminate the Need for User Judgment

<div class="evidence-lines">
<div><strong>Kumar et al. (2025)</strong><p>Developers who progressed incrementally and continued interacting with the agent were more likely to solve real software issues successfully.</p></div>
<div><strong>Dhanorkar et al. (2026)</strong><p>Developer oversight extended across ex ante constraint, joint planning, real-time viewing, and ex post review.</p></div>
</div>

<div class="argument-band">
Users still need to understand how the task is progressing in order to decide whether to continue delegation, intervene, or accept the work.
</div>

<!-- Source order: 54, Section 1.1.1, D5. -->

---
layout: default
class: outcome-slide
---

# A Subjective CASA Pathway to User Evaluations

<div class="causal-chain">
<div><small>Design and task conditions</small><strong>Action traces, diffs, execution evidence, notifications, task complexity</strong></div>
<div class="chain-arrow">→</div>
<div class="accent"><small>User's situation awareness</small><strong>Coding-Agent Situation Awareness</strong></div>
<div class="chain-arrow">→</div>
<div><small>Subjective experience outcomes</small><strong>Confidence, perceived control, satisfaction, continued use</strong></div>
</div>

<div class="argument-band">
Subjective CASA captures whether users feel sufficiently informed about the agent-generated task state, providing an experiential basis for confidence, perceived control, satisfaction, and continued use.
</div>

<p class="citation-line">Taylor (1990); Endsley et al. (1998); Baronas and Louis (1988); Bhattacherjee (2001)</p>

<!-- Source order: 54, Section 1.1.1, D8. This concludes the background before problem formulation. -->

---
layout: section
---

# 1. Research Question

Why coding-agent situation awareness requires construct development

<!-- Source order: 68, Section 1, begins here. -->

---
layout: default
class: argument-slide
---

# Agentic Delegation Creates a Specific Awareness Problem

<div class="argument-sequence">
<div><span>1</span><p>Coding agents let users delegate multistep software tasks without specifying every operation.</p></div>
<div><span>2</span><p>Users nevertheless continue judging progress and results throughout the task.</p></div>
<div><span>3</span><p>Those judgments require awareness of agent actions, artifact changes, execution evidence, and task meaning.</p></div>
</div>

<div class="argument-band">
The research question concerns the user's subjective situation awareness of a task state generated through delegated software action.
</div>

<p class="citation-line">Kumar et al. (2025); Dhanorkar et al. (2026); Nadj et al. (2020); Endsley (2023)</p>

<!-- Source order: 68, C19.1-C19.17. -->

---
layout: default
class: difference-slide
---

# Traditional Situation Awareness Does Not Directly Represent This Task State

<div class="three-differences">
<div><span>State generation</span><p>The agent's actions continuously create new software-task states around an open goal.</p></div>
<div><span>State distribution</span><p>Relevant state is distributed across plans, action traces, interdependent artifacts, tests, and runtime evidence.</p></div>
<div><span>State access</span><p>Because users do not perform every action, they may reconstruct the task state from traces after the task has advanced.</p></div>
</div>

<div class="argument-band">
Coding agents change how task states are generated, where those states reside, and how users encounter them.
</div>

<p class="citation-line">Endsley (1995a, 1995b); Parasuraman et al. (2000); Baird and Maruping (2021); Kretsou et al. (2021)</p>

<!-- Source order: 68, C21.1-C21.7. -->

---
layout: default
class: definition-slide
---

# CASA Represents Subjective Situation Awareness of an Agent-Generated Task State

<div class="definition-box large-definition">
Coding-Agent Situation Awareness is an individual user's perceived degree of situation awareness, during a specific coding-agent task, concerning the task-relevant states created through the agent's delegated actions and their near-term development.
</div>

<div class="definition-scope">
<div><strong>Relevant states</strong><span>Agent actions, software-artifact changes, execution evidence, and their relationship to the user's task goal</span></div>
<div><strong>High CASA</strong><span>A coherent and updateable perception of what has happened, what it means, and how the task may develop</span></div>
<div><strong>Low CASA</strong><span>Difficulty determining prior actions, current meaning, or near-term task development</span></div>
</div>

<p class="citation-line">Taylor (1990); Endsley (1995b)</p>

<!-- Source order: 68, C23.1-C23.6. -->

---
layout: default
class: boundary-slide
---

# CASA Is Situation Awareness, Not an Evaluation of the Agent or Interface

<div class="boundary-matrix">
<div><strong>CASA</strong><p>The user's perceived situation awareness of the current agent-generated task state.</p></div>
<div><strong>Not task performance</strong><p>Whether the agent actually completed the software task correctly.</p></div>
<div><strong>Not trust</strong><p>Whether the user is willing to rely on the agent.</p></div>
<div><strong>Not transparency</strong><p>How much process information the system exposes.</p></div>
<div><strong>Not perceived control</strong><p>Whether the user feels able to influence the system or task.</p></div>
<div><strong>Not workload</strong><p>The cognitive effort required to perform or monitor the task.</p></div>
</div>

<div class="argument-band compact">
These concepts may be antecedents, consequences, or correlates of CASA, but they do not measure the same individual state.
</div>

<!-- Source order: 68, C23.7-C23.11 and construct boundaries. -->

---
layout: default
class: literature-slide
---

# Situation Awareness Has Been Contextualized Across Dynamic Tasks

<div class="literature-table four-col">
<div class="head">Setting</div><div class="head">Awareness content</div><div class="head">Measurement</div><div class="head">Source</div>
<div>Aviation design</div><div>Subjective knowledge, cognition, and anticipation relevant to task success</div><div>SART, post-task self-report</div><div>Taylor (1990)</div>
<div>Dynamic decision systems</div><div>Perception, comprehension, and projection of task-relevant elements</div><div>SAGAT, task freeze and state queries</div><div>Endsley (1995a, 1995b)</div>
<div>Low-event train driving</div><div>Location, speed, signals, operating constraints, and near-term events</div><div>LETSSA, task-specific self-report</div><div>Rose et al. (2018)</div>
<div>Information security</div><div>Attention to and interpretation of a current security threat</div><div>Survey, eye tracking, and behavior</div><div>Jaeger and Eckhardt (2021)</div>
<div>Analytical dashboards</div><div>Current state, causal relationships, and future outcomes</div><div>SAGAT, eye tracking, performance</div><div>Nadj et al. (2020)</div>
</div>

<div class="argument-band compact">Situation awareness transfers across settings only when its content and measurement match the user's task-relevant states.</div>

<!-- Source order: 68, C25 and Table 1; first half. -->

---
layout: default
class: literature-slide
---

# Existing Situation-Awareness Conceptualizations Define a Different Situation

<div class="transfer-table">
<div><strong>SART tradition</strong><span>Subjective SA in aviation</span><p>Defines the situation through instability, complexity, information, attention, and understanding, partly combining task conditions and individual resources.</p></div>
<div><strong>Endsley tradition</strong><span>SA in dynamic systems</span><p>Defines awareness around task-relevant elements identified from system goals, assuming that required states can be analyzed in advance.</p></div>
<div><strong>Agent-transparency tradition</strong><span>SA of an autonomous agent</span><p>Adds agent action, rationale, and future state, but retains a predefined environment and omits executable artifact relations and runtime evidence.</p></div>
</div>

<div class="argument-band compact">The mismatch concerns what theoretically constitutes the situation, not merely how existing items are worded.</div>

<p class="citation-line">Taylor (1990); Endsley (1995a, 2021); Selkowitz et al. (2017); van de Merwe et al. (2024)</p>

<!-- Source order: 68, C27 and C47. -->

---
layout: default
class: value-slide
---

# CASA Makes an Important Agentic User State Visible

<div class="value-lines">
<div><strong>Integrates a fragmented phenomenon</strong><p>Defines one situation-awareness construct spanning agent actions, artifact changes, execution evidence, and near-term development.</p></div>
<div><strong>Explains consequential judgments</strong><p>Positions situation awareness as a cognitive basis for deciding whether to continue, intervene, or accept, and for later experience evaluations.</p></div>
<div><strong>Identifies actionable breakdowns</strong><p>Distinguishes failures to perceive actions, comprehend consequences, or project the next state, giving interface design a precise target.</p></div>
</div>

<p class="citation-line">Hong et al. (2014); Hoehle and Venkatesh (2015)</p>

<!-- Source order: 68, C29.1-C29.5. -->

---
layout: statement
class: research-question-slide
---

# Research Questions

<div class="rq-list">
<p><strong>RQ1.</strong> What dimensions constitute CASA, and how should these dimensions be measured?</p>
<p><strong>RQ2.</strong> Compared with a generic subjective situation-awareness measure, does CASA provide incremental explanatory and predictive validity for perceived control, satisfaction, and continuance intention?</p>
</div>

<!-- Source order: 68, C31.1-C31.3. -->

---
layout: default
class: approach-slide
hide: true
---

# The Research Design Moves from Content Discovery to Independent Validation

<div class="two-stage-overview">
<div><span>Stage 1</span><h3>Qualitative construct development</h3><p>Use public coding-agent narratives to identify the content domain, boundaries, and candidate dimensions.</p></div>
<div><span>Stage 2</span><h3>Quantitative scale development</h3><p>Generate items, validate the measurement model, establish a nomological network, and compare predictive value.</p></div>
</div>

<div class="argument-band compact">
Taylor defines the subjective property; Endsley organizes awareness content; user data determines the coding-agent-specific empirical structure.
</div>

<p class="citation-line">Venkatesh et al. (2013); Corbin and Strauss (1990); Moore and Benbasat (1991); MacKenzie et al. (2011)</p>

<!-- Source order: 68, C33-C35. -->

---
layout: default
class: contributions-slide
hide: true
---

# The Proposed Study Makes Three Testable Contributions

<div class="numbered-lines">
<div><span>1</span><strong>Construct</strong><p>Define CASA's content domain, boundaries, dimensions, and measurement instrument.</p></div>
<div><span>2</span><strong>Theory</strong><p>Develop subjective situation awareness for delegated, artifact-changing action by agentic information systems.</p></div>
<div><span>3</span><strong>Design</strong><p>Provide a diagnostic measure for comparing how interfaces communicate actions, changes, and execution evidence.</p></div>
</div>

<div class="argument-band compact">These contributions must be supported by content differences, discriminant validity, and incremental validity.</div>

<!-- Source order: 68, C37-C39. -->

---
layout: section
---

# 2. Theoretical Background

One base construct, one organizing theory, and one agentic context

<!-- Source order: 68, Section 2. -->

---
layout: default
class: traditions-slide
---

# Taylor and Endsley Serve Different Roles in the CASA Project

<div class="tradition-compare">
<div>
<span>Base construct</span>
<h3>Taylor's subjective situation awareness</h3>
<p>Defines the individual attribute being measured: a person's judgment of their own knowledge, cognition, and anticipation relevant to task success.</p>
</div>
<div>
<span>Organizing theory</span>
<h3>Endsley's dynamic situation awareness</h3>
<p>Organizes the content of awareness into perception, comprehension, and near-term projection while separating antecedents from consequences.</p>
</div>
</div>

<div class="argument-band compact">CASA remains an individual-level subjective construct; the three dynamic-SA levels are not prespecified as its final empirical dimensions.</div>

<p class="citation-line">Taylor (1990); Endsley (1995b)</p>

<!-- Source order: 68, C45.1-C45.7. -->

---
layout: default
class: literature-slide
---

# Existing Situation-Awareness Research Establishes Transferability and Limits

<div class="literature-table compact-table four-col">
<div class="head">Research tradition</div><div class="head">Primary object</div><div class="head">Contribution to CASA</div><div class="head">Limitation</div>
<div>Automation navigation</div><div>System state, progress, takeover conditions</div><div>Shows out-of-the-loop awareness risk</div><div>Preallocated automation functions</div>
<div>Autonomous-agent transparency</div><div>Current action, rationale, future state</div><div>Links interface information to awareness</div><div>Predefined embodied environments</div>
<div>Human-AI teaming</div><div>Task, AI action, and coordination</div><div>Positions awareness as a human-AI condition</div><div>No software-artifact construct</div>
<div>IS dashboards</div><div>Operational state and causal relations</div><div>Shows SA and performance can diverge</div><div>No delegated action</div>
<div>Information security</div><div>Threat cues and risk understanding</div><div>Demonstrates IS contextualization</div><div>Different state objects and goals</div>
</div>

<p class="citation-line">Endsley and Kiris (1995); Selkowitz et al. (2017); Nadj et al. (2020); Jaeger and Eckhardt (2021); Endsley (2023)</p>

<!-- Source order: 68, Table 1 and C47. -->

---
layout: default
class: evidence-table-slide
---

# AI-Assisted Programming Research Reveals Pieces of the CASA Phenomenon

<div class="literature-table evidence-research">
<div class="head">Research focus</div><div class="head">Method</div><div class="head">CASA-relevant finding</div>
<div>Code-generation interaction</div><div>Observation and grounded analysis</div><div>Acceleration and exploration modes; inspection and intent articulation</div>
<div>User activity and cost</div><div>Behavior sequences and time modeling</div><div>Reading, validating, editing, prompting, and waiting activities</div>
<div>Validation support</div><div>Experiment and interaction logs</div><div>Runtime values alter how users inspect and understand code</div>
<div>Trust in generated code</div><div>Interviews and design analysis</div><div>Users assess system capability and individual suggestions</div>
<div>Developer-agent collaboration</div><div>Field observation</div><div>Incremental work, continuous interaction, debugging, and testing difficulties</div>
<div>Agent oversight</div><div>Expert interviews</div><div>Ex ante, joint, real-time, and ex post oversight activities</div>
</div>

<p class="citation-line">Barke et al. (2023); Mozannar et al. (2024); Ferdowsi et al. (2024); Wang et al. (2024); Kumar et al. (2025); Dhanorkar et al. (2026)</p>

<!-- Source order: 68, C51 and Table 2. -->

---
layout: default
class: gaps-slide
---

# The Literature Leaves Three Interlocking Gaps

<div class="numbered-lines gap-lines">
<div><span>1</span><strong>Conceptual coverage</strong><p>No construct integrates perceived awareness of agent actions, software-artifact changes, execution evidence, and near-term task development.</p></div>
<div><span>2</span><strong>Construct precision</strong><p>Trust, transparency, validation cost, and general understanding capture related but different properties.</p></div>
<div><span>3</span><strong>Measurement</strong><p>No CASA scale has undergone systematic content validation and independent-sample testing.</p></div>
</div>

<div class="argument-band compact">Researchers therefore cannot compare CASA across users and products or test whether interface design affects later experience through CASA.</div>

<!-- Source order: 68, C53-C55. -->

---
layout: default
class: theory-slide
---

# Dynamic Situation Awareness Organizes What the User Comes to Know

<div class="sa-levels">
<div><span>Level 1</span><strong>Perception</strong><p>Notice task-relevant elements, their attributes, current states, and changes.</p></div>
<div><span>Level 2</span><strong>Comprehension</strong><p>Integrate elements and interpret their meaning relative to the user's task goal and prior knowledge.</p></div>
<div><span>Level 3</span><strong>Projection</strong><p>Anticipate near-term development from current state, trends, and task mechanisms.</p></div>
</div>

<div class="argument-band compact">These levels describe the awareness formed; interface design, workload, experience, goals, and task complexity are conditions that influence its formation.</div>

<p class="citation-line">Endsley (1995b)</p>

<!-- Source order: 68, C59 and Table 3. -->

---
layout: default
class: theory-slide
---

# Delegation Theory Specifies Why This Awareness Occurs in an Agentic IS Context

<div class="delegation-bridge">
<div><strong>Dynamic situation awareness</strong><p>Explains the general cognitive structure of noticing, understanding, and anticipating a changing task state.</p></div>
<div class="bridge-symbol">+</div>
<div><strong>Delegation to agentic IS</strong><p>Explains why the system can accept a task and initiate action rather than merely support user-specified operations.</p></div>
<div class="bridge-symbol">=</div>
<div class="accent"><strong>CASA context</strong><p>A user forms awareness of a software-task state produced through delegated agent action.</p></div>
</div>

<p class="citation-line">Endsley (1995b); Baird and Maruping (2021)</p>

<!-- Source order: 68, C61-C63.4. -->

---
layout: default
class: difference-slide
---

# Dynamic Situation Awareness Guides Three Candidate CASA Dimensions

<div class="sa-levels candidate-dimensions">
<div><span>Candidate dimension 1</span><strong>Perception of agent-generated states</strong><p>Perceiving key agent actions, software-artifact changes, and test or runtime evidence relevant to the current goal.</p></div>
<div><span>Candidate dimension 2</span><strong>Comprehension of task meaning</strong><p>Integrating traces, artifact relations, and evidence to understand implications for goals, dependencies, and unresolved issues.</p></div>
<div><span>Candidate dimension 3</span><strong>Projection of near-term development</strong><p>Anticipating the agent's likely next actions, the consequences of current changes, and emerging task risks.</p></div>
</div>

<div class="argument-band compact">Endsley's levels guide the higher-order dimensions; Reddit coding specifies and may refine their coding-agent-specific content.</div>

<p class="citation-line">Endsley (1995b); Baird and Maruping (2021); Chen et al. (2024); Zhou et al. (2025)</p>

<!-- Source order: 68, C63.5-C63.11. -->

---
layout: default
class: empirical-path-slide
hide: true
---

# Taylor's Original Elicitation Logic Provides the Empirical Starting Point

<div class="elicitation-flow">
<div><span>1</span><p>Begin with users' comparisons of concrete high- and low-awareness task experiences.</p></div>
<div><span>2</span><p>Identify the attributes users actually use to judge whether they understand the task.</p></div>
<div><span>3</span><p>Use Endsley's levels to inspect coverage and separate antecedents, awareness content, and outcomes.</p></div>
<div><span>4</span><p>Retain only stable content that remains distinct from transparency, trust, workload, control, and objective knowledge.</p></div>
</div>

<div class="argument-band compact">Theory disciplines the empirical categories but does not force a three-dimensional result.</div>

<p class="citation-line">Taylor (1990); Endsley (1995b)</p>

<!-- Source order: 68, C63.12-C63.15. -->

---
layout: section
---

# 3. Research Design

Reddit-based construct development followed by scale development

<!-- Source order: 68, Section 3. -->

---
layout: default
class: method-rationale-slide
---

# Stage 1 Develops the CASA Construct from Coding-Agent Use Narratives

<div class="method-rationale">
<div><strong>Public Reddit narratives</strong><p>Collect concrete coding-agent task episodes that describe agent actions, artifact changes, execution evidence, user understanding, or awareness breakdowns.</p></div>
<div><strong>Human qualitative coding</strong><p>Use open and axial coding, theory comparison, and negative cases to define the content domain, boundaries, and candidate dimensions of CASA.</p></div>
</div>

<div class="argument-band compact">Reddit supports content discovery rather than prevalence estimation; Taylor and Endsley discipline the categories without predetermining them.</div>

<p class="citation-line">Corbin and Strauss (1990); Gioia et al. (2013); Chen et al. (2024)</p>

<!-- Source order: 68, Sections 3-4, condensed. -->

---
layout: default
class: roadmap-slide
---

# Stage 2 Develops and Tests a CASA Scale

<div class="study-roadmap">
<div><span>1</span><strong>Generate items</strong><p>Translate the validated definition, qualitative categories, and user language into task-anchored items.</p><small>Content representation</small></div>
<div><span>2</span><strong>Validate content</strong><p>Use expert review, cognitive interviews, semantic audit, and card sorting.</p><small>Clarity and boundaries</small></div>
<div><span>3</span><strong>Test structure</strong><p>Use independent EFA and CFA samples to establish reliability, validity, and invariance.</p><small>Measurement quality</small></div>
<div><span>4</span><strong>Test added value</strong><p>Compare CASA with generic subjective SA in its explanation and prediction of user outcomes.</p><small>Incremental value</small></div>
</div>

<div class="argument-band compact">If CASA shows no distinct content or incremental value, the study must be reframed as contextual scale adaptation rather than new construct development.</div>

<p class="citation-line">Moore and Benbasat (1991); MacKenzie et al. (2011); Larsen et al. (2026); Pillet et al. (2026)</p>

<!-- Source order: 68, Section 5-6, condensed. -->

---
layout: section
hide: true
---

# Expected Implementation

Procedures to be executed after data collection begins

<!-- Source order: 68, Sections 4-6; all following material is prospective. -->

---
layout: default
class: sampling-slide
hide: true
---

# Stage 1 Uses Public Narratives for Content Discovery, Not Prevalence Estimation

<div class="sampling-grid">
<div><strong>Broad entry</strong><p>Search across product-specific and cross-product communities without requiring theoretical words such as awareness or control.</p></div>
<div><strong>Strict inclusion</strong><p>Require a first-hand use episode involving a concrete task and at least one action, change, execution result, judgment, or consequence.</p></div>
<div><strong>Context-preserving unit</strong><p>Analyze a complete meaning segment with enough title, parent comment, and reply context to reconstruct the task episode.</p></div>
</div>

<div class="argument-band compact">If enterprise use, routine high-CASA episodes, or key state content is missing, critical-incident interviews will supplement the public data.</div>

<!-- Source order: 68, Sections 4.1, lines 140-148. -->

---
layout: default
class: ethics-slide
hide: true
---

# Public Availability Does Not Remove Research-Ethics Obligations

<div class="ethics-list">
<div><span>Access</span><p>Follow current platform policies and do not bypass restricted communities or access controls.</p></div>
<div><span>Identification</span><p>Replace usernames with random identifiers and remove employers, repositories, projects, and traceable details.</p></div>
<div><span>Presentation</span><p>Assess reverse-search risk and paraphrase sensitive or uniquely worded material when necessary.</p></div>
<div><span>Auditability</span><p>Share a de-identified codebook, category definitions, audit trail, and risk-treated examples rather than raw data.</p></div>
</div>

<p class="citation-line">Franzke et al. (2020); Gliniecka (2023)</p>

<!-- Source order: 68, Section 4.2. -->

---
layout: default
class: coding-slide
hide: true
---

# Coding Begins with Users' Judgments of Their Own Awareness

<div class="coding-steps">
<div><span>Prepare</span><p>Define meaning units, context windows, inclusion rules, and broad observational positions without naming final dimensions.</p></div>
<div><span>Open-code pilot</span><p>Code approximately 10% across products, interfaces, and task types using language close to users' accounts.</p></div>
<div><span>Full open coding</span><p>Double-code an overlap sample, document disagreement resolution, and test saturation on a held-out heterogeneous batch.</p></div>
</div>

<div class="argument-band compact">A direct CASA indicator must express how the user evaluates what they know, understand, or can anticipate; an objective event alone is task context.</div>

<p class="citation-line">Corbin and Strauss (1990); Gioia et al. (2013)</p>

<!-- Source order: 68, Section 4.3, preparation through Step 2. -->

---
layout: default
class: coding-slide
hide: true
---

# Later Coding Tests Structure, Theory Fit, and Alternative Explanations

<div class="coding-steps">
<div><span>Axial coding</span><p>Group first-order codes by object, state, time, and meaning; document definitions, inclusion, exclusion, and examples.</p></div>
<div><span>Theory comparison</span><p>Compare frozen categories with Taylor and Endsley while retaining stable categories that cross or depart from prior levels.</p></div>
<div><span>Negative cases</span><p>Seek high-trust/low-CASA, high-visibility/low-CASA, and available-control/low-CASA episodes that challenge premature boundaries.</p></div>
</div>

<div class="argument-band compact">Only categories that survive boundary tests enter the candidate construct structure.</div>

<!-- Source order: 68, Section 4.3, Steps 3-5. -->

---
layout: default
class: validation-slide
hide: true
---

# Stage 1 Must Validate the Definition Before It Specifies a Measurement Model

<div class="validation-sequence">
<div><strong>Revise the definition</strong><p>Specify the focal entity, core attribute, conditions, unit of analysis, state object, time boundary, and nomological position.</p></div>
<div><strong>Validate category placement</strong><p>Use separate developer and scholar card-sorting rounds with an explicit cannot-classify option.</p></div>
<div><strong>Specify dimension relations</strong><p>Choose reflective, formative, or profile-like relations from construct meaning rather than model-fit convenience.</p></div>
</div>

<div class="argument-band compact">Stage 1 advances only if the audit trail demonstrates stable and theoretically meaningful content differences from generic situation awareness.</div>

<p class="citation-line">Podsakoff et al. (2016); Law et al. (1998); Jarvis et al. (2003); Petter et al. (2007)</p>

<!-- Source order: 68, Sections 4.4-4.5. -->

---
layout: default
class: scale-slide
hide: true
---

# Stage 2A Converts the Validated Content Domain into Candidate Items

<div class="scale-sequence">
<div><span>1</span><p>Generate an oversized item pool from qualitative language, construct definitions, and relevant SA expressions.</p></div>
<div><span>2</span><p>Anchor every item to a specific recently completed coding-agent task.</p></div>
<div><span>3</span><p>Audit entity, attribute, qualifier, time boundary, and response set using the ITEM Ontology.</p></div>
<div><span>4</span><p>Conduct human content review, AI-assisted diagnostics, cognitive interviews, and repeated card sorting.</p></div>
</div>

<div class="argument-band compact">Items must measure situation awareness, not interface features, trust, liking, control, or workload.</div>

<p class="citation-line">Hinkin (1998); MacKenzie et al. (2011); Larsen et al. (2026); Pillet et al. (2026)</p>

<!-- Source order: 68, Section 5.1. -->

---
layout: default
class: scale-slide
hide: true
---

# Stage 2B Establishes Structure with Independent Samples

<div class="two-sample">
<div><span>Sample 1</span><h3>Exploration and purification</h3><p>Recent actual users describe one specific task before responding. EFA evaluates candidate structure while item retention remains tied to content coverage.</p></div>
<div><span>Sample 2</span><h3>Confirmation and comparison</h3><p>CFA compares single-factor, multidimensional, and justified higher-order models; tests reliability, convergence, discrimination, and invariance.</p></div>
</div>

<div class="argument-band compact">CASA must remain distinguishable from AI trust, perceived transparency, perceived control, cognitive load, and generic subjective SA.</div>

<!-- Source order: 68, Section 5.2. -->

---
layout: default
class: incremental-slide
hide: true
---

# Stage 2C Must Demonstrate More Than Good Model Fit

<div class="incremental-model">
<div><small>Time 1</small><strong>CASA, generic subjective SA, adjacent constructs</strong></div>
<div class="chain-arrow">→</div>
<div><small>Time 2</small><strong>Perceived control, satisfaction, continuance intention</strong></div>
</div>

<div class="incremental-tests">
<div><strong>Nomological validity</strong><p>CASA behaves coherently in the outcome chain proposed in the introduction.</p></div>
<div><strong>Incremental validity</strong><p>CASA adds explanation beyond minimally adapted SART and an independently developed task-specific SA baseline.</p></div>
<div><strong>Predictive validity</strong><p>CASA improves held-out prediction, not only in-sample fit.</p></div>
</div>

<p class="citation-line">Podsakoff et al. (2003); Taylor (1990); Bolton et al. (2022)</p>

<!-- Source order: 68, Section 5.3, lines 206-212. -->

---
layout: default
class: calibration-slide
hide: true
---

# Subjective CASA and Objective Task Knowledge Require Separate Evidence

<div class="calibration-grid">
<div><strong>CASA</strong><p>Measured first as the user's subjective degree of perceived situation awareness.</p></div>
<div><strong>Task truth</strong><p>Reconstructed from agent logs, version differences, command outputs, tests, and runtime results.</p></div>
<div><strong>Trajectory-matched probe</strong><p>Administered during task replay after CASA, without redefining CASA as question accuracy.</p></div>
</div>

<div class="argument-band compact">The substudy examines calibration and criterion evidence, including high-subjective/low-objective and low-subjective/high-objective cases.</div>

<!-- Source order: 68, Section 5.3, line 214. -->

---
layout: default
class: gates-slide
hide: true
---

# A New CASA Construct Is a Claim to Be Earned, Not Assumed

<div class="gate-list">
<div><span>1</span><p>If qualitative categories fit generic SA entirely, position the work as contextual scale adaptation.</p></div>
<div><span>2</span><p>If categories mainly describe visibility, usability, or trust, return them to those constructs.</p></div>
<div><span>3</span><p>If content is product-specific, narrow the construct boundary.</p></div>
<div><span>4</span><p>If discriminant validity fails, revise or terminate the new-construct claim.</p></div>
<div><span>5</span><p>If CASA adds no content, explanatory, predictive, or diagnostic value, do not claim theoretical improvement.</p></div>
</div>

<!-- Source order: 68, Section 6. -->

---
layout: statement
class: closing-slide
---

# The Central Claim

**Coding-agent use creates a distinct awareness object: a software-task state generated through delegated action, distributed across executable artifacts and evidence, and encountered partly through traces rather than direct operation.**

CASA is worth developing only if empirical evidence shows that this object requires content and measurement beyond generic subjective situation awareness.

<!-- Source order: synthesis of 68, Sections 1-6. -->

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. <em>MIS Quarterly, 45</em>(1), 315-341.</p>
<p>Barke, S., James, M. B., & Polikarpova, N. (2023). Grounded Copilot: How programmers interact with code-generating models. <em>Proceedings of the ACM on Programming Languages, 7</em>(OOPSLA1), 85-111.</p>
<p>Baronas, A.-M. K., & Louis, M. R. (1988). Restoring a sense of control during implementation: How user involvement leads to system acceptance. <em>MIS Quarterly, 12</em>(1), 111-123.</p>
<p>Bhattacherjee, A. (2001). Understanding information systems continuance: An expectation-confirmation model. <em>MIS Quarterly, 25</em>(3), 351-370.</p>
<p>Bolton, M. L., Biltekoff, E., & Humphrey, L. R. (2022). The level of measurement of subjective situation awareness and its dimensions in SART. <em>IEEE Transactions on Human-Machine Systems, 52</em>(6), 1147-1154.</p>
<p>Chen, Q., Gong, Y., Keil, M., Liu, S., & Lu, Y. (2024). Conceptualization and measurement of voice-interaction usability. <em>MIS Quarterly, 48</em>(3), 1009-1046.</p>
<p>Corbin, J. M., & Strauss, A. (1990). Grounded theory research: Procedures, canons, and evaluative criteria. <em>Qualitative Sociology, 13</em>(1), 3-21.</p>
</div>

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>Dhanorkar, S., Passi, S., & Vorvoreanu, M. (2026). Human oversight of agentic systems in practice. <em>Proceedings of ACM FAccT</em>, 6438-6465.</p>
<p>Endsley, M. R. (1995a). Measurement of situation awareness in dynamic systems. <em>Human Factors, 37</em>(1), 65-84.</p>
<p>Endsley, M. R. (1995b). Toward a theory of situation awareness in dynamic systems. <em>Human Factors, 37</em>(1), 32-64.</p>
<p>Endsley, M. R. (2021). A systematic review and meta-analysis of direct objective measures of situation awareness. <em>Human Factors, 63</em>(1), 124-150.</p>
<p>Endsley, M. R. (2023). Supporting human-AI teams: Transparency, explainability, and situation awareness. <em>Computers in Human Behavior, 140</em>, 107574.</p>
<p>Endsley, M. R., & Kiris, E. O. (1995). The out-of-the-loop performance problem and level of control in automation. <em>Human Factors, 37</em>(2), 381-394.</p>
<p>Endsley, M. R., Selcon, S. J., Hardiman, T. D., & Croft, D. G. (1998). A comparative analysis of SAGAT and SART for evaluations of situation awareness. <em>Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 42</em>(1), 82-86.</p>
</div>

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>Ferdowsi, K., Huang, R., James, M. B., Polikarpova, N., & Lerner, S. (2024). Validating AI-generated code with live programming. <em>Proceedings of ACM CHI</em>, Article 143.</p>
<p>Franzke, A. S., Bechmann, A., Zimmer, M., Ess, C., & AoIR. (2020). <em>Internet research: Ethical guidelines 3.0</em>. Association of Internet Researchers.</p>
<p>Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research. <em>Organizational Research Methods, 16</em>(1), 15-31.</p>
<p>Gliniecka, M. (2023). The ethics of publicly available data research: A situated ethics framework for Reddit. <em>Social Media + Society, 9</em>(3).</p>
<p>Hinkin, T. R. (1998). A brief tutorial on the development of measures for use in survey questionnaires. <em>Organizational Research Methods, 1</em>(1), 104-121.</p>
<p>Hoehle, H., & Venkatesh, V. (2015). Mobile application usability: Conceptualization and instrument development. <em>MIS Quarterly, 39</em>(2), 435-472.</p>
<p>Hong, W., Chan, F. K. Y., Thong, J. Y. L., Chasalow, L. C., & Dhillon, G. (2014). A framework and guidelines for context-specific theorizing in IS research. <em>Information Systems Research, 25</em>(1), 111-136.</p>
</div>

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>Jaeger, L., & Eckhardt, A. (2021). Eyes wide open: The role of situational information security awareness for security-related behaviour. <em>Information Systems Journal, 31</em>(3), 429-472.</p>
<p>Jarvis, C. B., MacKenzie, S. B., & Podsakoff, P. M. (2003). A critical review of construct indicators and measurement model misspecification. <em>Journal of Consumer Research, 30</em>(2), 199-218.</p>
<p>Kretsou, M., Arvanitou, E.-M., Ampatzoglou, A., Deligiannis, I., & Gerogiannis, V. C. (2021). Change impact analysis: A systematic mapping study. <em>Journal of Systems and Software, 174</em>, 110892.</p>
<p>Kumar, A., Bajpai, Y., Gulwani, S., Soares, G., & Murphy-Hill, E. (2025). Why AI agents still need you. <em>Proceedings of IEEE/ACM ASE</em>, 432-444.</p>
<p>Larsen, K. R., et al. (2026). The ITEM Ontology: A tool to elucidate the anatomy of psychometric indicators. <em>Information Systems Research, 37</em>(1), 549-567.</p>
<p>Law, K. S., Wong, C.-S., & Mobley, W. H. (1998). Toward a taxonomy of multidimensional constructs. <em>Academy of Management Review, 23</em>(4), 741-755.</p>
<p>MacKenzie, S. B., Podsakoff, P. M., & Podsakoff, N. P. (2011). Construct measurement and validation procedures in MIS and behavioral research. <em>MIS Quarterly, 35</em>(2), 293-334.</p>
</div>

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>McKinsey Global Institute. (2023). <em>The economic potential of generative AI: The next productivity frontier</em>.</p>
<p>Moore, G. C., & Benbasat, I. (1991). Development of an instrument to measure perceptions of adopting an IT innovation. <em>Information Systems Research, 2</em>(3), 192-222.</p>
<p>Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E. (2024). Reading between the lines: Modeling user behavior and costs in AI-assisted programming. <em>Proceedings of ACM CHI</em>, Article 142.</p>
<p>Nadj, M., Maedche, A., & Schieder, C. (2020). The effect of interactive analytical dashboard features on situation awareness and task performance. <em>Decision Support Systems, 135</em>, 113322.</p>
<p>Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. <em>IEEE Transactions on SMC-A, 30</em>(3), 286-297.</p>
<p>Petter, S., Straub, D., & Rai, A. (2007). Specifying formative constructs in information systems research. <em>MIS Quarterly, 31</em>(4), 623-656.</p>
</div>

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>Pillet, J.-C., et al. (2026). AI-augmented content validation in behavioral research: Development and evaluation of the RATER system. <em>MIS Quarterly, 50</em>(1), 59-86.</p>
<p>Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research. <em>Journal of Applied Psychology, 88</em>(5), 879-903.</p>
<p>Podsakoff, P. M., MacKenzie, S. B., & Podsakoff, N. P. (2016). Recommendations for creating better concept definitions. <em>Organizational Research Methods, 19</em>(2), 159-203.</p>
<p>Rose, J., Bearman, C., & Dorrian, J. (2018). The Low-Event Task Subjective Situation Awareness technique. <em>Applied Ergonomics, 68</em>, 273-282.</p>
</div>

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>Schuetz, S., & Venkatesh, V. (2020). The rise of human machines. <em>Journal of the Association for Information Systems, 21</em>(2), 460-482.</p>
<p>Selkowitz, A. R., Lakhmani, S. G., & Chen, J. Y. C. (2017). Using agent transparency to support situation awareness. <em>Cognitive Systems Research, 46</em>, 13-25.</p>
<p>Stack Overflow. (2025). <em>2025 Developer Survey: AI</em>.</p>
<p>Taylor, R. M. (1990). Situational Awareness Rating Technique: The development of a tool for aircrew systems design. In <em>Situational Awareness in Aerospace Operations</em>, AGARD-CP-478.</p>
</div>

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>van de Merwe, K., Mallam, S., & Nazir, S. (2024). Agent transparency, situation awareness, mental workload, and operator performance. <em>Human Factors, 66</em>(1), 180-208.</p>
<p>Venkatesh, V., Brown, S. A., & Bala, H. (2013). Bridging the qualitative-quantitative divide. <em>MIS Quarterly, 37</em>(1), 21-54.</p>
</div>

---
layout: default
class: references-slide
---

# REFERENCES

<div class="reference-list">
<p>Wang, R., Cheng, R., Ford, D., & Zimmermann, T. (2024). Investigating and designing for trust in AI-powered code generation tools. <em>Proceedings of ACM FAccT</em>, 1475-1493.</p>
<p>Zhou, Z., Chen, Z., Li, W., Zhang, Y., & Jin, X.-L. (2025). Demystifying the dimensions and roles of metaverse gaming experience value: A multi-study investigation. <em>Journal of Management Information Systems, 42</em>(1), 39-69.</p>
</div>
