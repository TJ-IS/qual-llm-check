---
otero_id: "2-s2.0-85133543887"
title: "Path Transitions Tell More: Optimizing Fuzzing Schedules via Runtime Program States"
authors: "Zhang K.; Xiao X.; Zhu X.; Sun R.; Xue M.; Wen S."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510063"
---
# Scopus title-abstract-keyword metadata
Title: Path Transitions Tell More: Optimizing Fuzzing Schedules via Runtime Program States
Abstract: Coverage-guided Greybox Fuzzing (CGF) is one of the most successful and widely-used techniques for bug hunting. Two major approaches are adopted to optimize CGF: (i) to reduce search space of inputs by inferring relationships between input bytes and path constraints; (ii) to formulate fuzzing processes (e.g., path transitions) and build up probability distributions to optimize power schedules, i.e., the number of inputs generated per seed. However, the former is subjective to the inference results which may include extra bytes for a path constraint, thereby limiting the efficiency of path constraints resolution, code coverage discovery, and bugs exposure; the latter formalization, concentrating on power schedules for seeds alone, is inattentive to the schedule for bytes in a seed. In this paper, we propose a lightweight fuzzing approach, Truzz, to optimize existing Coverage-guided Greybox Fuzzers (CGFs). To address two aforementioned challenges, Truzz identifies the bytes related to the validation checks (i.e., the checks guarding error-handling code), and protects those bytes from being frequently mutated, making most generated inputs examine the functionalities of programs, in lieu of being rejected by validation checks. The byte-wise relationship determination mitigates the problem of loading extra bytes when fuzzers infer the byte-constraint relation. Furthermore, the proposed path transition within Truzz can efficiently prioritize the seed as the new path, harvesting many new edges, and the new path likely belongs to a code region with many undiscovered code lines. To evaluate our approach, we implemented 6 state-of-the-art fuzzers, AFL, AFLFast, NEUZZ, MOPT, FuzzFactory and GreyOne, in Truzz. The experimental results show that on average, Truzz can generate 16.14% more inputs flowing into functional code, in addition to 24.75% more new edges than the vanilla fuzzers. Finally, our approach exposes 13 bugs in 8 target programs, and 6 of them have not been identified by the vanilla fuzzers. © 2022 ACM.
Author keywords: Fuzzing; Mutation; Path Transition; Software Security
Index keywords: Codes (symbols); Program debugging; Fuzzing; Grey-box; Mutation; Path constraint; Path transition; Power; Program state; Runtimes; Software security; Validation checks; Probability distributions
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133543887
DOI: 10.1145/3510003.3510063
Retrieval channels: authoritative_outlet_search
Local full-text files: 
