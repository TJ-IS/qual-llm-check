---
otero_id: "2-s2.0-85020425764"
title: "Efficient detection and validation of atomicity violations in concurrent programs"
authors: "Eslamimehr M.; Lesani M.; Edwards G."
year: "2018"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2017.06.001"
---
# Scopus title-abstract-keyword metadata
Title: Efficient detection and validation of atomicity violations in concurrent programs
Abstract: Atomicity violations are a major source of bugs in concurrent programs. Empirical studies have shown that the majority of atomicity violations are instances of the three-access pattern, where two accesses to a shared variable by a thread are interleaved by an access to the same variable by another thread. This article describes two advancements in atomicity violation detection. First, we describe a new technique that directs the execution of a dynamic analysis tool towards three-access pattern (TAP) instances. The directed search is based on constraint solving and concolic execution. We implemented this technique in a tool called AtomChase. Using 27 benchmarks comprising 5.4 million lines of Java, we compared AtomChase to five other tools. AtomChase found 20% more TAP instances than all five tools combined. Second, we show that not all TAP instances are atomicity violations and present a formally grounded approach to validating the non-atomicity of TAP instances. This approach, called HyperCV, prevents the inclusion of false positives in results presented to users. HyperCV uses a set of provably sufficient conditions for non-atomicity to efficiently validate TAP instances. Using the same benchmarks, HyperCV validated 79% of TAP instances in linear rather than exponential execution time. © 2017 Elsevier Inc.
Author keywords: Atomicity violation; Concurrency; Software testing; Three-access pattern
Index keywords: Software testing; Access patterns; Atomicity violations; Concolic execution; Concurrency; Concurrent program; Constraint Solving; Dynamic analysis tools; Efficient detection; Program debugging
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2018
EID: 2-s2.0-85020425764
DOI: 10.1016/j.jss.2017.06.001
Retrieval channels: authoritative_outlet_search
Local full-text files: 
