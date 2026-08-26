---
otero_id: "2-s2.0-84922553443"
title: "Exception handling analysis and transformation using fault injection: Study of resilience against unanticipated exceptions"
authors: "Cornu B.; Seinturier L.; Monperrus M."
year: "2015"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2014.08.004"
---
# Scopus title-abstract-keyword metadata
Title: Exception handling analysis and transformation using fault injection: Study of resilience against unanticipated exceptions
Abstract: Context: In software, there are the error cases that are anticipated at specification and design time, those encountered at development and testing time, and those that were never anticipated before happening inproduction. Is it possible to learn from the anticipated errors during design to analyze and improve the resilience against the unanticipated ones in production? Objective: In this paper, we aim at analyzing and improving how software handles unanticipated exceptions. The first objective is to set up contracts about exception handling and a way to assess them automatically. The second one is to improve the resilience capabilities of software by transforming the source code. Method: We devise an algorithm, called short-circuit testing, which injects exceptions during test suite execution so as to simulate unanticipated errors. It is a kind of fault-injection techniques dedicated to exception-handling. This algorithm collects data that is used for verifying two formal contracts that capture two resilience properties w.r.t. exceptions: the source-independence and pure-resilience contracts. Then we propose a code modification technique, called "catch-stretching" which allows error-recovery code (of the form of catch blocks) to be more resilient. Results: Our evaluation is performed on 9 open-source software applications and consists in analyzing 241 catch blocks executed during test suite execution. Our results show that 101/214 of them (47%) expose resilience properties as defined by our exception contracts and that 84/214 of them (39%) can be transformed to be more resilient. Conclusion: Our work shows that it is possible to reason on software resilience by injecting exceptions during test suite execution. The collected information allows us to apply one source code transformation that improves the resilience against unanticipated exceptions. This works best if the test suite exercises the exceptional programming language constructs in many different scenarios. © 2014 Elsevier B.V. All rights reserved.
Author keywords: Contract; Dynamic verification; Exception handling; Fault injection
Index keywords: Algorithms; Application programs; Codes (symbols); Contracts; Cosine transforms; Errors; Open systems; Software engineering; Software testing; Development and testing; Dynamic verifications; Exception handling; Fault injection; Fault Injection techniques; Short-circuit testing; Source code transformation; Specification and designs; Open source software
Document type: Conference paper
Conference: 
Source title: Information and Software Technology
Year: 2015
EID: 2-s2.0-84922553443
DOI: 10.1016/j.infsof.2014.08.004
Retrieval channels: authoritative_outlet_search
Local full-text files: 
