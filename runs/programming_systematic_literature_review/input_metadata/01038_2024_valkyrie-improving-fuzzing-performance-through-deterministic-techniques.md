---
otero_id: "2-s2.0-85183775208"
title: "Valkyrie: Improving fuzzing performance through deterministic techniques"
authors: "Rong Y.; Zhang C.; Liu J.; Chen H."
year: "2024"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2023.111886"
---
# Scopus title-abstract-keyword metadata
Title: Valkyrie: Improving fuzzing performance through deterministic techniques
Abstract: Greybox fuzzing has received much attention from developers and researchers due to its success in discovering bugs within many programs. However, randomized algorithms have limited fuzzers’ effectiveness. First, branch coverage feedback that is based on random edge ID can lead to branch collision. Besides, state-of-the-art fuzzers heavily rely on randomized methods to reach new coverage. Finally, some state-of-the-art fuzzers only employ heuristics-based bug exploitation methods, which are not effective in triggering those that require non-trivial triggering conditions. We believe deterministic techniques deliver consistent and reproducible results. We propose Valkyrie, a greybox fuzzer whose performance is boosted primarily by deterministic techniques. Valkyrie combines collision-free branch coverage with context sensitivity to maintain accuracy while introducing an instrumentation removal algorithm to reduce overhead. It also pioneers a new mutation method, compensated step, allowing fuzzers that use solvers to adapt to real-world fuzzing scenarios without randomness. Additionally, Valkyrie proactively identifies possible exploit points in target programs and utilizes solvers to trigger actual bugs. We implement and evaluate Valkyrie's effectiveness on the standard benchmark Magma, and a wide variety of real-world programs. Valkyrie triggered 21 unique integer and memory errors, 10.5% and 50% more than AFL++ and Angora, respectively. Valkyrie reached 8.2% and 12.4% more branches in real-world programs, compared with AFL++ and Angora, respectively. We also verify that our branch counting and mutation method is better than the state-of-the-art, which shows that deterministic techniques trump random techniques in consistency, reproducibility, and performance. © 2023 The Author(s)
Author keywords: Dynamic analysis; Fuzzing; Vulnerability detection
Index keywords: Heuristic programming; Integer programming; Program debugging; Branch-coverage; Deterministic technique; Dynamics analysis; Fuzzing; Grey-box; Performance; Randomized Algorithms; Real world projects; State of the art; Vulnerability detection; Heuristic methods
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2024
EID: 2-s2.0-85183775208
DOI: 10.1016/j.jss.2023.111886
Retrieval channels: authoritative_outlet_search
Local full-text files: 
