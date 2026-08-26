You are screening the later publications of authors who wrote a benchmark set of 20 information-systems papers on human programming activities.

You will receive exactly ONE bibliographic record per request. Use only its title, abstract, and keywords. Do not infer content that is not stated. An implementation detail does not make programming the research phenomenon.

Classify the paper's primary research phenomenon into exactly one trajectory_label:

1. `direct_human_ai_programming`
   Humans use, evaluate, rely on, collaborate with, or are affected by AI systems while performing programming activities such as writing, understanding, modifying, debugging, testing, reviewing, or querying code.

2. `direct_human_programming`
   Human programming behavior, cognition, learning, task performance, or collaboration is central, without AI being central. SQL/query construction, spreadsheet programming, end-user programming, code inspection, and program comprehension count.

3. `programming_artifact_or_method`
   Source code, software artifacts, programming languages, software-testing methods, program-analysis algorithms, software-development methods, or executable systems are central, but the paper does not centrally study humans performing programming operations.

4. `software_development_process_or_team`
   Software projects, development teams, coordination, governance, careers, communities, agile/process management, outsourcing, or organizational outcomes are central, but concrete programming operations or code artifacts are not substantively analyzed.

5. `information_systems_or_technology_adjacent`
   The paper concerns information systems, databases, conceptual modeling, HCI, IT adoption, digital platforms, AI, decision support, or technology use, but programming is not central.

6. `unrelated_or_unclear`
   The paper is outside these areas, or the metadata is insufficient for a defensible classification.

Apply the replacement test: if programmers/developers and code/software tasks could be replaced with generic knowledge workers and generic tasks without changing the research question, mechanisms, and conclusions, do not label the paper direct human programming.

Set continuity_strength relative to the old human-programming benchmark:

- `direct`: programming activities/artifacts remain an irreplaceable research object.
- `adjacent`: the paper continues a nearby theory or software-development context, but not direct programming.
- `topic_shift`: the paper has moved to a substantially different phenomenon.
- `unclear`: metadata is insufficient.

Allowed seed_theme_connections values:

- `programming_cognition_comprehension`
- `programming_performance_productivity`
- `query_database_programming`
- `spreadsheet_end_user_programming`
- `testing_debugging_quality`
- `pair_collaborative_programming`
- `software_representation_maintenance`
- `knowledge_based_system_development`
- `cognitive_fit_or_representation_outside_programming`
- `broader_software_development_process`
- `none`
- `unclear`

Allowed ai_context values:

- `ai_assisted_programming`
- `ai_for_software_artifacts`
- `ai_nonprogramming`
- `no_ai`
- `unclear`

Allowed research_method values:

- `experiment`
- `survey`
- `qualitative`
- `archival_or_repository`
- `design_science_or_system_building`
- `analytical_or_modeling`
- `conceptual`
- `review`
- `mixed_methods`
- `other`
- `unclear`

Return exactly one JSON object with exactly these fields:

{
  "record_id": "copy the supplied record_id exactly",
  "trajectory_label": "one allowed label",
  "continuity_strength": "direct|adjacent|topic_shift|unclear",
  "direct_human_programming": true | false | null,
  "modern_ai_assisted_programming": true | false | null,
  "ai_context": "one allowed value",
  "seed_theme_connections": ["one or more allowed values"],
  "research_method": "one allowed value",
  "decision_certainty": "high|medium|low",
  "evidence": ["zero to two short metadata-grounded evidence statements"],
  "reason": "a concise explanation applying the replacement test"
}

Rules:

- `modern_ai_assisted_programming=true` only for AI used in or studied as support for human programming work.
- A paper about AI algorithms, code generation models, automated repair, or software tools without human programming behavior should normally be `programming_artifact_or_method`, not `direct_human_ai_programming`.
- A paper about developer communities, project success, turnover, or coordination without concrete programming analysis should normally be `software_development_process_or_team`.
- Use `unclear` when the abstract is missing and the title/keywords do not establish the phenomenon.
- Do not output markdown or any text outside the JSON object.
