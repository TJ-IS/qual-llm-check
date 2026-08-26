---
otero_id: "2-s2.0-85050199696"
title: "Improving regression test efficiency with an awareness of refactoring changes"
authors: "Chen Z.; Guo H.-F.; Song M."
year: "2018"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2018.07.003"
---
# Scopus title-abstract-keyword metadata
Title: Improving regression test efficiency with an awareness of refactoring changes
Abstract: Context. Developers often improve software quality through refactorings—the practice of behavior-preserving changes to existing code. Recent studies showed that, despite their awareness of tool support for automated refactorings, developers prefer manual refactorings. This practice can be often error-prone and increase testing cost. Objective. To address the problem, we present the Refactorings Investigation and Testing technique, called RIT. RIT improves the testing efficiency for validating refactoring changes and providing confidence that changed parts behave as intended. As testing is expensive for developers of high-assurance software, RIT reduces a considerable amount of its costs by only identifying dependent statements on a failure in each test and by detecting specific refactoring edits responsible for testing failures. Method. Our approach identifies refactorings by analyzing original and edited versions of a program. It then uses the semantic impact of a set of identified refactoring changes to detect tests whose behavior may have been affected and modified by refactoring edits. Given each failed asserts after running regression test suites, RIT helps developers focus their attention on logically related program statements by applying program slicing for minimizing each test. For debugging purposes, RIT determines specific failure-inducing refactoring edits, separating from other changes that only affect other asserts or tests. Results. We evaluated RIT on three open source projects, and found that RIT detected tests affected by refactorings with 80.9% accuracy on average. Furthermore, it identified and formed partitions relating program statements only dependent on failed asserts with 97.2% accuracy on average. Conclusion. RIT, which combines a refactoring reconstruction technique with change impact analysis to localize failure-inducing program edits, helps developers localize fault causes by focusing on refactoring changes as opposed to all the code fragments in the new version. © 2018 Elsevier B.V.
Author keywords: Change impact analysis; Fault localization; Refactorings; Software evolution; Test selection
Index keywords: Computer software selection and evaluation; Efficiency; Open source software; Program debugging; Semantics; Change impact analysis; Fault localization; Refactorings; Software Evolution; Test selection; Software testing
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2018
EID: 2-s2.0-85050199696
DOI: 10.1016/j.infsof.2018.07.003
Retrieval channels: authoritative_outlet_search
Local full-text files: 
