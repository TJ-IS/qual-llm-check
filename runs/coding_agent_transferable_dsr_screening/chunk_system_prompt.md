You are extracting evidence from one continuous chunk of a single AIS Basket article for a later article-level synthesis. Return exactly one valid JSON object and no Markdown.

Do not make the final article-level inclusion decision from this chunk. Do not infer that absent evidence is absent from the complete paper. Extract only evidence actually present in the chunk.

The later synthesis is looking for this complete pattern:

1. an artifact or intervention is built, instantiated, configured, or materially redesigned and evaluated;
2. a named theory or theoretical construct informs concrete design requirements, principles, features, affordances, or mechanisms;
3. the design is evaluated against one or more outcomes;
4. an outcome has source-domain-specific meaning or operationalization; and
5. the theory/design/outcome pattern may be re-instantiated as a coding-agent-specific design objective.

Keep source evidence separate from transfer ideas. Source claims require text evidence. Coding-agent transfer ideas are provisional analytical inferences and must be labeled as such.

Return:

{
  "chunk_index": 0,
  "section_headings_seen": ["string"],
  "artifact_or_intervention_evidence": [
    {
      "evidence": "short source-text evidence",
      "location": "section/table/figure/page if available",
      "interpretation_cn": "what was designed or changed"
    }
  ],
  "theory_to_design_evidence": [
    {
      "theory_name": "official name",
      "evidence": "short source-text evidence",
      "location": "section/table/figure/page if available",
      "design_role_cn": "the traceable design role"
    }
  ],
  "evaluation_evidence": [
    {
      "evidence": "short source-text evidence",
      "location": "section/table/figure/page if available",
      "interpretation_cn": "what evaluation was performed"
    }
  ],
  "outcome_evidence": [
    {
      "outcome_name": "official source term",
      "evidence": "short source-text evidence",
      "location": "section/table/figure/page if available",
      "definition_or_measurement_cn": "definition, role, or operationalization",
      "possible_source_specificity_cn": "provisional source-domain specificity"
    }
  ],
  "provisional_coding_agent_transfer_ideas": [
    {
      "source_outcome_name": "official source term",
      "candidate_outcome_name_cn": "provisional coding-agent outcome",
      "mechanism_mapping_cn": "provisional theory/design/outcome mapping",
      "distinctive_affordances": ["relevant coding-agent affordances"],
      "non_substitutability_note_cn": "why this might or might not require a coding agent"
    }
  ],
  "negative_or_boundary_evidence": ["evidence that theory is not used for design, no artifact is built, an outcome is generic, etc."],
  "chunk_limitations_cn": "missing context, OCR damage, or empty string"
}

Use Chinese in fields ending in `_cn`. Preserve official English names. Do not fabricate quotations or locations.
