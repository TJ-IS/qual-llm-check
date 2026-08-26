---
otero_id: "2-s2.0-105040153824"
title: "Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic approach with static analysis and test execution feedback"
authors: "Maddila C.; Tait A.; Chang C.; Cheng D.; Ahmad N.; Murali V.; Roch M.; Avondet A.; Meltzer A.; Montalvao V.; Hopko M.; Waterson C.; Thakkar P.; Fernandez R.; Kristensen K.; Barzily S.; Chen S.; Abreu R.; Nagappan N.; Shodjai P.; Murphy K.; Everingham J.; Ramani A.; Rigby P.C."
year: "2026"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2026.3696849"
---
# Scopus title-abstract-keyword metadata
Title: Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic approach with static analysis and test execution feedback
Abstract: Aim. With the advent of LLMs, agentic program repair has become viable in large organizations with large codebases. While APR research frequently motivates its techniques around helping developers, Winter et al. [1] report that studies with substantial industrial participants are rare (2%). In this work, we develop an Engineering Agent that fixes source code from test failures at scale across diverse software offerings internally. Method. Using Llama as the base model, we employ a ReAct harness to build an agent that starts from a test failure triaged by a rule-based test failure bot. The agent operates in an agentic harness with 15 actions (e.g., reading files, searching code, running tests, and generating patches), and it iteratively refines solutions using feedback from static analysis and test execution. After validations pass, we apply an LLM-as-a-Judge to filter low-quality patches before notifying a human reviewer, who can accept and land the change in our monorepo. Because we can progressively roll out the system with layered validation and human review, we use offline benchmarks primarily as readiness gates and complement them with production evaluation based on review and landing outcomes. Benchmark Findings. We curated offline benchmarks for patch generation, the agent loop, and the LLM-as-a-Judge. We found that a specialized 70B model, internally fine-tuned for patch generation in a search-and-replace format, is highly competitive with a much larger vanilla Llama-405B. We also found that patch format strongly impacts performance, with search-and-replace outperforming unified diff. In ablation studies, symbolic feedback from static analysis and test execution improves the ReAct agent. The balanced configuration achieves a benchmark solve rate of 42.3% using an average 11.8 feedback iterations. Production Findings. Over a three month period, 80% of the generated fixes were reviewed, of which 31.5% were landed (25.5% of the total number of generated fixes). Engineer Feedback and Adoption. We used open coding to extract qualitative themes from engineer feedback, including quick approvals, gratitude, and surprise, and we used negative feedback (e.g., test flakiness) to refine the production system. We also analyzed reviewed-but-not merged diffs to understand why validated patches are rejected in practice, including workflow timing, intent mismatches (revert vs. fix-forward), and broader patch acceptability concerns. © 1976-2012 IEEE.
Author keywords: Agents; AI; AI in Production; Benchmarking; Engineer Feedback; LLMs; Patch Generation; Program Repair; Test Failures
Index keywords: Agents; Codes (symbols); Computer programming; Engineering research; Engineers; Feedback; Industrial research; Iterative methods; Model checking; Repair; Reviews; Software agents; Software testing; AI in production; Engineer feedback; Large organizations; LLM; Offline; Patch generation; Program repair; Source codes; Test execution; Test failure; Benchmarking
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2026
EID: 2-s2.0-105040153824
DOI: 10.1109/tse.2026.3696849
Retrieval channels: authoritative_outlet_search
Local full-text files: 
