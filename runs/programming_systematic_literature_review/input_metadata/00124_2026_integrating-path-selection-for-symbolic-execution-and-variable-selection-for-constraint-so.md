---
otero_id: "2-s2.0-105031597693"
title: "Integrating Path Selection for Symbolic Execution and Variable Selection for Constraint Solving"
authors: "Zhu S.; Sun J.; Wang J.; Chen Z.; Cheng P."
year: "2026"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3735552"
---
# Scopus title-abstract-keyword metadata
Title: Integrating Path Selection for Symbolic Execution and Variable Selection for Constraint Solving
Abstract: Symbolic execution is a powerful technique that can accurately synthesize program inputs for program testing through constraint solving. Applying symbolic execution effectively means that we must solve two searching problems efficiently. One is to search through the many program paths and the other is, given a particular path condition, to search through the numerous variable assignments to identify one satisfying solution. With few exceptions, existing symbolic execution engines treat constraint solvers as black boxes. As a result, the two searches are completely separated, which results in much redundancy (i.e., the same variable assignments may be tried for solving many program paths). Existing attempts on addressing this issue include those approaches based on constrained Horn clauses (in which the whole program is encoded as one constraint) and one preliminary attempt on caching and reusing partial solving results from the constraint solver. In this work, we propose SEC, which systematically computes the reward of concretizing a program path (for symbolic execution) and a variable (for constraint solving) and uses the reward as guide for integrating the two searches. We implemented SEC based on KLEE and evaluated it on a diverse set of programs. The results show that SEC is effective, i.e., achieving 15% more code coverage than the state-of-the-art baseline symbolic execution engines. Furthermore, we show that SEC can be readily combined with a state-of-the-art concolic testing engine to improve its performance © 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Program Analysis; SMT Solving; Symbolic Execution
Index keywords: Constraint handling; Constraint satisfaction problems; Model checking; Search engines; Software testing; Constraint solvers; Constraint Solving; Execution engine; Path selection; Program analysis; SMT solving; State of the art; Symbolic execution; Variable assignment; Variables selections; Engines
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2026
EID: 2-s2.0-105031597693
DOI: 10.1145/3735552
Retrieval channels: authoritative_outlet_search
Local full-text files: 
