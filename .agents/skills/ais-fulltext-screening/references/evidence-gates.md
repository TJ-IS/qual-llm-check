# Decision boundaries and evidence gates

## Security relevance

Include work whose substantive research object, mechanism, outcome, intervention, or empirical context concerns security, privacy, abuse, adversarial behavior, trust/safety controls, or closely defined cyber risk. A term appearing only in references, boilerplate, or an unrelated example is insufficient.

## Security algorithm or method development

Require a material algorithmic, computational, measurement, detection, mitigation, or technical-method contribution for security. A study may be security-relevant without developing an algorithm. Do not count adoption studies, behavioral surveys, governance discussions, or ordinary applications as algorithm development unless the frozen rule explicitly does so.

## Objective metric or benchmark

Require an operationalized objective measure, benchmark, testbed, dataset/evaluation contribution, or reproducible measurement procedure matching the frozen prompt. Subjective labels, ordinary performance comparisons, and an uncalibrated model confidence score are not automatically objective benchmarks.

## Public-data eligibility

Classify access as one of:

- `direct_open_download`;
- `public_registration`;
- `public_application_or_license`;
- `restricted_or_internal`;
- `unknown`.

A standard application, registration, or licensing route may satisfy a broad `publicly obtainable` rule when it is publicly discoverable, open to external researchers under stated eligibility conditions, and capable of delivering the relevant analysis unit. Record that it is application-gated; do not describe it as freely downloadable, open-licensed, free, or approval-free.

Internal membership, institutional affiliation, personal invitation, private relationships, ad hoc “contact the authors” access without a public standard route, or participant-only access do not satisfy a public-data gate. Public metadata do not make private underlying observations public. If a run requires freely downloadable or openly licensed data, freeze that stricter condition separately.

For each decision, verify and record the data identity, public access URL, access category, external-researcher eligibility, approval or agreement conditions, license/terms, verification date, obtainable analysis unit, and whether that unit supports the paper's core claim. “Publicly discussed,” a named platform, or a paper's unsupported statement that data are available cannot substitute for access-route verification.

## Evidence strength

For each inclusion, retain the decisive full-text passage or section and the reasoning under the frozen definition. Metadata/title/abstract evidence can support retrieval but should not silently replace full-text classification when the standard is full text.

For each exclusion audit, retain the strongest apparently qualifying passage and why it fails the gate. This makes false-negative review possible.

## Standards

- **exploratory candidate set** — optimized for discovery; may be overinclusive.
- **screened set** — every item received the frozen decision procedure and execution reconciles.
- **provisional standard** — independently audited but has named corpus or boundary defects.
- **accepted standard** — corpus identity, decision reliability, recall/precision, and unresolved-case rules have passed the declared gates.

Do not promote a set because its size is stable across scripts or because all API calls returned successfully.

When a set is adopted into manuscript work, preserve its adoption manifest. Individual-paper facts still require direct source verification; counts, completeness, absence, representativeness, recall, or gold-standard claims additionally require an accepted set status and reconciled corpus boundary.
