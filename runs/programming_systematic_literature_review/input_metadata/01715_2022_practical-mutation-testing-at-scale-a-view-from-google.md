---
otero_id: "2-s2.0-85114607525"
title: "Practical Mutation Testing at Scale: A view from Google"
authors: "Petrovic G.; Ivankovic M.; Fraser G.; Just R."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2021.3107634"
---
# Scopus title-abstract-keyword metadata
Title: Practical Mutation Testing at Scale: A view from Google
Abstract: Mutation analysis assesses a test suite's adequacy by measuring its ability to detect small artificial faults, systematically seeded into the tested program. Mutation analysis is considered one of the strongest test-adequacy criteria. Mutation testing builds on top of mutation analysis and is a testing technique that uses mutants as test goals to create or improve a test suite. Mutation testing has long been considered intractable because the sheer number of mutants that can be created represents an insurmountable problem-both in terms of human and computational effort. This has hindered the adoption of mutation testing as an industry standard. For example, Google has a codebase of two billion lines of code and more than 150,000,000 tests are executed on a daily basis. The traditional approach to mutation testing does not scale to such an environment; even existing solutions to speed up mutation analysis are insufficient to make it computationally feasible at such a scale. To address these challenges, this paper presents a scalable approach to mutation testing based on the following main ideas: (1) mutation testing is done incrementally, mutating only changed code during code review, rather than the entire code base; (2) mutants are filtered, removing mutants that are likely to be irrelevant to developers, and limiting the number of mutants per line and per code review process; (3) mutants are selected based on the historical performance of mutation operators, further eliminating irrelevant mutants and improving mutant quality. This paper empirically validates the proposed approach by analyzing its effectiveness in a code-review-based setting, used by more than 24,000 developers on more than 1,000 projects. The results show that the proposed approach produces orders of magnitude fewer mutants and that context-based mutant filtering and selection improve mutant quality and actionability. Overall, the proposed approach represents a mutation testing framework that seamlessly integrates into the software development workflow and is applicable to industrial settings of any size. © 1976-2012 IEEE.
Author keywords: code coverage; Mutation testing; test efficacy
Index keywords: Codes (symbols); Logic programming; Probabilistic logics; Software design; Software testing; Code coverage; Code review; Google+; Mutation analysis; Mutation testing; Strong test; Test adequacy criteria; Test efficacy; Tested programs; Testing technique; Python
Document type: Review
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85114607525
DOI: 10.1109/tse.2021.3107634
Retrieval channels: authoritative_outlet_search
Local full-text files: 
