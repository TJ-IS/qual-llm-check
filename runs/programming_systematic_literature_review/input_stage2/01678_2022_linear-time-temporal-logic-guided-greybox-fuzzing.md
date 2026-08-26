---
otero_id: "2-s2.0-85133512050"
title: "Linear-time Temporal Logic guided Greybox Fuzzing"
authors: "Meng R.; Dong Z.; Li J.; Beschastnikh I.; Roychoudhury A."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510082"
---
# Scopus title-abstract-keyword metadata
Title: Linear-time Temporal Logic guided Greybox Fuzzing
Abstract: Software model checking as well as runtime verification are verification techniques which are widely used for checking temporal properties of software systems. Even though they are property verification techniques, their common usage in practice is in 'bug finding', that is, finding violations of temporal properties. Motivated by this observation and leveraging the recent progress in fuzzing, we build a greybox fuzzing framework to find violations of Linear-time Temporal Logic (LTL) properties. Our framework takes as input a sequential program written in C/C++, and an LTL property. It finds violations, or counterexample traces, of the LTL property in stateful software systems; however, it does not achieve verification. Our work substantially extends directed greybox fuzzing to witness arbitrarily complex event or-derings. We note that existing directed greybox fuzzing approaches are limited to witnessing reaching a location or witnessing simple event orderings like use-after-free. At the same time, compared to model checkers, our approach finds the counterexamples faster, thereby finding more counterexamples within a given time budget. Our LTL-FUZZER tool, built on top of the AFL fuzzer, is shown to be effective in detecting bugs in well-known protocol implementations, such as OpenSSL and Telnet. We use LTL-FUZZER to reproduce known vulnerabilities (CVEs), to find 15 zero-day bugs by checking properties extracted from RFCs (for which 12 CVEs have been assigned), and to find violations of both safety as well as liveness properties in real-world protocol implementations. Our work represents a practical advance over software model checkers - while simultaneously representing a conceptual advance over existing greybox fuzzers. Our work thus provides a starting point for understanding the unexplored synergies among software model checking, runtime verification and greybox fuzzing. © 2022 ACM.
Author keywords: 
Index keywords: Budget control; C++ (programming language); Computer circuits; Computer software; Model checking; Program debugging; Grey-box; Linear time temporal logic; Model@Runtime; Protocol implementation; Run-time verification; Software model checking; Software-systems; Temporal logic properties; Temporal property; Verification techniques; Temporal logic
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133512050
DOI: 10.1145/3510003.3510082
Retrieval channels: authoritative_outlet_search
Local full-text files: 
