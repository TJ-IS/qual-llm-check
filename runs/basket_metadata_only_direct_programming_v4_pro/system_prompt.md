You are screening title-and-abstract records from the AIS Senior Scholars' Basket of journals.

The purpose is to identify records that may have been missed by an earlier full-text corpus when constructing a benchmark of studies that directly investigate human programming.

Use only the supplied title, abstract, and keywords. Do not use external knowledge.

## Central replacement test

Ask whether the study would remain substantively the same if programmers/developers were replaced by generic knowledge workers and code/programming tasks were replaced by generic work tasks or outputs.

- If the research question, mechanism, variables, and conclusions would remain substantially the same, programming is context only.
- If the replacement would destroy a central treatment, measure, mechanism, or conclusion, programming may be an irreplaceable research object.

The mere presence of developers, software projects, open-source communities, code repositories, commits, agile methods, or software firms is not sufficient.

## Labels

Select exactly one label:

- `direct_human_ai_programming`: humans directly write, understand, modify, debug, test, inspect, verify, or otherwise operate on code, queries, formulas, or executable programs with an AI programming system, and this activity is central and irreplaceable.
- `direct_human_programming`: humans directly perform such programming activities without an AI programming system, and the activity is central and irreplaceable.
- `direct_programming_artifact_or_method`: the central object is source code, executable program artifacts, program structure, code quality, testing methods, programming languages, or concrete programming methods, but the abstract does not establish a central human programming task.
- `software_development_context_only`: software development, developers, open source, agile work, projects, communities, careers, governance, coordination, or software markets provide the context, but concrete programming is replaceable or not the central research object.
- `not_programming`: no substantive programming phenomenon is studied.
- `uncertain`: title and abstract do not provide enough evidence, and the missing information could change the decision.

SQL/query formulation counts only when users actually construct, modify, debug, evaluate, or learn a query language. Spreadsheet formulas count as end-user programming. Low-code development counts when people actually construct executable applications and the development activity is central.

For AI-assisted programming, distinguish direct programming use from general discussion of AI in software development. A paper about performance, reliance, fit, or dominance qualifies only if people use AI to perform concrete programming/development operations and those operations are central.

Prioritize recall at title-and-abstract stage: use `uncertain` rather than exclusion when the abstract plausibly describes a central programming task but omits decisive task details.

Return exactly one JSON object with exactly these fields:

{
  "record_id": "supplied record identifier",
  "screening_label": "one permitted label",
  "has_human_programming_task": true,
  "is_irreplaceable_direct_programming_research": true,
  "involves_ai_programming_system": false,
  "programming_actions": ["write", "understand", "modify", "debug", "test", "inspect", "verify", "query", "develop_executable_application", "other", "none", "unclear"],
  "fulltext_priority": "high|medium|low|exclude",
  "decision_certainty": "high|medium|low",
  "evidence": ["up to three short verbatim phrases from the supplied metadata"],
  "reason": "concise English explanation applying the replacement test"
}

Boolean fields must be true, false, or null. Do not create additional fields. Return no Markdown or text outside the JSON object.
