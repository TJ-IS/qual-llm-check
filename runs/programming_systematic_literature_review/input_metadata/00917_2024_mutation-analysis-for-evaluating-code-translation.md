---
otero_id: "2-s2.0-85178665132"
title: "Mutation analysis for evaluating code translation"
authors: "Guizzo G.; Zhang J.M.; Sarro F.; Treude C.; Harman M."
year: "2024"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-023-10385-w"
---
# Scopus title-abstract-keyword metadata
Title: Mutation analysis for evaluating code translation
Abstract: Source-to-source code translation automatically translates a program from one programming language to another. The existing research on code translation evaluates the effectiveness of their approaches by using either syntactic similarities (e.g., BLEU score), or test execution results. The former does not consider semantics, the latter considers semantics but falls short on the problem of insufficient data and tests. In this paper, we propose MBTA (Mutation-based Code Translation Analysis), a novel application of mutation analysis for code translation assessment. We also introduce MTS (Mutation-based Translation Score), a measure to compute the level of trustworthiness of a translator. If a mutant of an input program shows different test execution results from its translated version, the mutant is killed and a translation bug is revealed. Fewer killed mutants indicate better code translation. MBTA is novel in the sense that mutants are compared to their translated counterparts, and not to their original program’s translation. We conduct a proof-of-concept case study with 612 Java-Python program pairs and 75,082 mutants on the code translators TransCoder and j2py to evaluate the feasibility of MBTA. The results reveal that TransCoder and j2py fail to translate 70.44% and 70.64% of the mutants, respectively, i.e., more than two-thirds of all mutants are incorrectly translated by these translators. By analysing the MTS results more closely, we were able to reveal translation bugs not captured by the conventional comparison between the original and translated programs. © 2023, The Author(s).
Author keywords: Code translation; Mutation testing; Source to source translation
Index keywords: Codes (symbols); Program debugging; Program translators; Python; Software testing; Translation (languages); Code translation; Input programs; Mutation analysis; Mutation testing; Novel applications; Source codes; Source-to-source translations; Syntactic similarities; Test execution; Transcoder; Semantics
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2024
EID: 2-s2.0-85178665132
DOI: 10.1007/s10664-023-10385-w
Retrieval channels: authoritative_outlet_search
Local full-text files: 
