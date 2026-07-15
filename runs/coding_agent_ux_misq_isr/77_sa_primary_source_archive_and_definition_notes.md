# Situation-Awareness Primary-Source Archive and Definition Notes

## Purpose

This file records the primary sources used to verify the situation-awareness definitions discussed on Slide 18, the local archival status of each source, and the theoretical role of the JMIS metaverse-gaming experience-value article. It distinguishes a full-text verification from a publisher-page verification and from a definition verified through an exact quotation in a later peer-reviewed review.

## Local source folder

`E:\github\qual-llm-check-IS-utd\runs\coding_agent_ux_misq_isr\source_pdfs_sa`

| Local file | Content | Status |
| --- | --- | --- |
| `endsley_1995_measurement_sa.pdf` | Endsley (1995), measurement of situation awareness | Full PDF archived |
| `endsley_1998_sagat_sart_comparison.pdf` | Endsley et al. (1998), SAGAT-SART comparison | Full PDF archived |
| `nadj_2020_dashboard_sa_fulltext.html` | Nadj et al. (2020), dashboard features, SA, and task performance | Full article HTML archived from PubMed Central |
| `salmon_2006_sa_measurement_review.pdf` | Salmon et al. review of SA measurement | Full PDF archived |
| `sart_scale_notes.pdf` | SART source notes | PDF archived |
| `maritime_theory_sa.pdf` | Maritime application of SA theory | Full PDF archived |

## Definition audit

### Endsley and Kiris (1995)

- Article: *The Out-of-the-Loop Performance Problem and Level of Control in Automation*, *Human Factors*, 37(2), 381-394.
- DOI: <https://doi.org/10.1518/001872095779064555>
- Publisher page: <https://journals.sagepub.com/doi/10.1518/001872095779064555>
- Definition excerpt: “the perception of elements in the environment ... the comprehension of their meaning, and the projection of their status in the near future.”
- Interpretation: The paper adopts Endsley's classic three-level definition. Its contribution is not a new SA definition but evidence that passive monitoring under automation can reduce SA and impair recovery after automation failure.
- Archive status: The publisher PDF was not openly retrievable in the current session. The definition and relevant experimental passage were verified against the author-uploaded full-text display and the publisher record; no paywalled PDF was copied locally.

### Selkowitz, Lakhmani, and Chen (2017)

- Article: *Using Agent Transparency to Support Situation Awareness of the Autonomous Squad Member*, *Cognitive Systems Research*, 46, 13-25.
- DOI: <https://doi.org/10.1016/j.cogsys.2017.02.003>
- Publisher page: <https://www.sciencedirect.com/science/article/pii/S1389041716301772>
- Definition excerpt: “perception of the basic elements ... comprehension of the elements' meaning ... projection of their status in the near future.”
- Interpretation: The paper explicitly adopts Endsley's definition. It contextualizes the content as the robot's actions and plans, reasoning, projected state, and uncertainty. This is a contextual application rather than a newly defined SA construct.
- Archive status: The publisher page exposes the article text and an open-manuscript route, but its tokenized download endpoint was not suitable for a stable local archive. The source remains linked here.

### Nadj, Maedche, and Schieder (2020)

- Article: *The Effect of Interactive Analytical Dashboard Features on Situation Awareness and Task Performance*, *Decision Support Systems*, 135, 113322.
- DOI: <https://doi.org/10.1016/j.dss.2020.113322>
- Publisher page: <https://www.sciencedirect.com/science/article/pii/S0167923620300774>
- Open full text: <https://pmc.ncbi.nlm.nih.gov/articles/PMC7234950/>
- Definition excerpt: “a quality criterion in terms of completeness and accuracy of the current state of knowledge.”
- Interpretation: The paper adopts Endsley's model and states more explicitly that SA varies in degree as a quality of the decision maker's current knowledge state. Its experiment separates SA from task performance: what-if analysis increased performance while decreasing SA.
- Archive status: Full article HTML is stored locally as `nadj_2020_dashboard_sa_fulltext.html`.

### Jaeger and Eckhardt (2021)

- Article: *Eyes Wide Open: The Role of Situational Information Security Awareness for Security-Related Behaviour*, *Information Systems Journal*, 31(3), 429-472.
- DOI and publisher page: <https://onlinelibrary.wiley.com/doi/10.1111/isj.12317>
- Definition excerpt: “a user's knowledge of particular security threats transported by security-related information cues captured in a situational process in the immediate system environment.”
- Interpretation: This paper develops a genuinely context-specific individual-level construct. The construct is not general security awareness; it is knowledge of a particular threat formed from cues encountered in a specific system interaction.
- Verification note: The exact definition was checked through the verbatim quotation attributed to Jaeger and Eckhardt in Ofte and Katsikas (2023), *Understanding Situation Awareness in Security Operations Centres: A Systematic Literature Review*, *Computers & Security*, 126, 103069, together with the Wiley abstract and study description.
- Archive status: The Wiley full text was not openly downloadable in the current session. The local archive therefore does not claim to contain the article PDF.

### Endsley (2023)

- Article: *Supporting Human-AI Teams: Transparency, Explainability, and Situation Awareness*, *Computers in Human Behavior*, 140, 107574.
- DOI: <https://doi.org/10.1016/j.chb.2022.107574>
- Publisher page: <https://www.sciencedirect.com/science/article/pii/S0747563222003946>
- Definition excerpt: “a constantly updated state of knowledge about what is happening in a dynamically changing world.”
- Interpretation: The paper retains classic SA and extends its requirements for human-AI teams into taskwork SA, agent SA, and teamwork SA. These are types of situation content required for teaming, not a replacement definition of individual SA.
- Archive status: The full publisher page was read, but no openly licensed stable PDF was available for local storage.

## Implications for CASA

The literature supports three conclusions. First, situation awareness can be transferred across domains because it retains a common cognitive concern with what the individual currently perceives, understands, and can project. Second, each serious transfer changes the content of the situation rather than merely renaming the setting. Third, Jaeger and Eckhardt demonstrate that an IS study can develop a context-specific individual-level awareness construct when a new interaction creates a distinct knowledge object and a distinct process through which users acquire that knowledge.

CASA should therefore be developed around the agent-generated software task state. Candidate content includes agent actions and plans, changes across executable software artifacts, evidence from tools and runtime behavior, unresolved dependencies, likely next actions, and emerging consequences. The three Endsley levels provide an initial theoretical organization; they do not predetermine the final dimensionality.

## JMIS comparison

Reference article: Zhou, Chen, Li, Zhang, and Jin (2025), *Demystifying the Dimensions and Roles of Metaverse Gaming Experience Value: A Multi-Study Investigation*, *Journal of Management Information Systems*, 42(1), 39-69.

Local text: `E:\github\qual-llm-check-IS-utd\doc_ref_JMIS\docs_ref_JMIS.md`

The JMIS article uses the mature experience-value framework as the theory base for the same broad construct it contextualizes. It does not use an unrelated external theory to dictate metaverse-gaming dimensions. The authors first open-code online reviews, identify 21 subdimensions and six concrete MGEV dimensions, and then map those empirical dimensions onto the intrinsic/extrinsic and active/reactive axes of experience value. Their abductive procedure lets data specify the context-specific content while the established construct framework supplies a theoretically meaningful higher-order organization.

This is close to the intended CASA design. Situation-awareness theory is the same-domain theoretical base for CASA. Reddit coding should identify coding-agent-specific content, while Endsley's structure provides sensitizing categories and a candidate higher-order organization. As in the JMIS study, empirical categories may cross, refine, or expose limits in the inherited framework.
