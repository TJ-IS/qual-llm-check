# Content audit notes

This note does not alter the raw model decisions or counts. It records a small boundary audit after the complete run.

## Clear theory-to-design examples in the inspected sample

- **Contextual Targeting in mHealth Apps: Harnessing Weather Information and Message Framing to Increase Physical Activity**: mood-as-resource, mood-congruity, and prospect/message-framing logic derive the weather-contingent gain/loss message design; the outcome is objectively observed 10,000-step completion.
- **Delays in Information Presentation Lead to Brain State Switching, Which Degrades User Performance, and There May Not Be Much We Can Do about It**: brain-state/task-switching logic derives delay-filling interface interventions; reaction time and accuracy provide objective outcomes.
- **A Field Experiment in Local Personalization for Charitable Crowdfunding**: dual-process, home-bias, and social-influence logic derives localized emails and landing pages; opens, clicks, and donations are behavioral outcomes.
- **The Relative Effect of the Convergence of Product Recommendations from Various Online Sources**: product-uncertainty and signaling logic derive combinations of recommendation sources; recommendation acceptance is behaviorally measured.

## Obvious theory-label conflict

- **RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning** was marked theory-guided using Robust Optimization and modern Reinforcement Learning/VAC/Gumbel-Softmax. These are precisely the kind of purely computational or mathematical foundations excluded by the prompt, and no separate psychological mechanism is identified. Treat its `theory_guided_subset_match=true` as an evident false positive pending manual correction. Its separate `base_match` judgment is not invalidated by this observation.

## Boundary cases worth manual adjudication

- **Combining review-based collaborative filtering and matrix factorization: A solution to rating's sparsity problem** uses Multi-Attribute Utility Theory. Whether this counts as psychology-related rather than formal decision theory depends on the intended disciplinary boundary.
- **Long-term multi-criteria improvement planning** translates resistance-to-change literature into an operational-change penalty. The psychological relevance is plausible, but the named basis may be a concept/literature rather than a sufficiently identifiable theory.
- **An intelligent decision support system prototype for hinterland port logistics** uses probability matching and the Bush-Mosteller behavioral learning model. Despite the phrase “reinforcement learning,” this is a behavioral learning model rather than only modern machine-learning theory; it should not be automatically excluded with the RADAR case.

## Interpretation

The 110 theory-guided matches are a machine-screened review pool, not a final human-adjudicated set. The audit found both strong positive chains and at least one direct false positive. Raw decisions remain unchanged for reproducibility.
