---
otero_id: "2-s2.0-105032805637"
title: "Iter-T: ITERative Test Suite Generation for Automated Program Repair"
authors: "Godio A.; Brida S.G.; Regis G.; Bagheri H.; Nguyen T.V.; Aguirre N.; Frias M.F."
year: "2026"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2026.3671416"
---
# Scopus title-abstract-keyword metadata
Title: Iter-T: ITERative Test Suite Generation for Automated Program Repair
Abstract: Test-based automated program repair (TB-APR) techniques automatically fix buggy programs by relying on a failing test suite. This test suite serves a dual purpose: pinpointing bugs and evaluating the validity of potential patches. However, the effectiveness of TB-APR techniques in generating correct patches is highly dependent on the test suite utilized. The primary shortcoming of TB-APR techniques arises from the intrinsic incompleteness of test suites, resulting in a significant drawback: overfitting, i.e., the generation of 'overfitted patches', patches that pass the given test suites but fail to repair the subject program correctly regarding its more general intended behavior. To address this challenge, we present a novel technique designed to enhance the effectiveness of TB-APR methods by automatically generating test suites tailored for program repair. Unlike prior TB-APR techniques, it is rooted in the recognition that edge cases that invalidate overfitted patches play a pivotal role in guiding the repair process away from incorrect solutions. This technique leverages formal specifications and bounded verification to evaluate candidate patches and transforms the counterexamples (CEs) obtained from verifying candidate patches into tests for program repair. The efficacy of iteratively using such CEs as tests for TB-APR is substantiated by Iter-T our implementation of this technique for Java programs and JML specifications, evaluated on a benchmark of 717 buggy Java programs drawn from the APR literature. By progressively constructing test suites exclusively from CEs of overfitted candidate patches, Iter-T increases the odds of fixing a bug by about 58% compared to the originally provided test suites. Moreover, in cases where a TB-APR tool repairs a program using its original suite, employing CEs alone as test suites reduces the median time required to generate a correct patch by 42%. Remarkably, the generated CEs-based test suites are very small, accomplishing these results with only 2.4 tests on average. © 1976-2012 IEEE.
Author keywords: automated program repair; bounded verification; specification-based program repair; Test suite generation
Index keywords: Automatic programming; Automatic test pattern generation; Automation; Formal specification; Formal verification; Iterative methods; Java programming language; Software testing; Automated program repair; Bounded verifications; Java program; Novel techniques; Overfitting; Repair methods; Repair process; Repair techniques; Specification-based program repair; Test suite generation; Repair
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2026
EID: 2-s2.0-105032805637
DOI: 10.1109/tse.2026.3671416
Retrieval channels: authoritative_outlet_search
Local full-text files: 
