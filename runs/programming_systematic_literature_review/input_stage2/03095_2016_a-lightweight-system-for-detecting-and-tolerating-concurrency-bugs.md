---
otero_id: "2-s2.0-84994875757"
title: "A lightweight system for detecting and tolerating concurrency bugs"
authors: "Zhang M.; Wu Y.; Lu S.; Qi S.; Ren J.; Zheng W."
year: "2016"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2016.2531666"
---
# Scopus title-abstract-keyword metadata
Title: A lightweight system for detecting and tolerating concurrency bugs
Abstract: Along with the prevalence of multi-threaded programs, concurrency bugs have become one of the most important sources of software bugs. Even worse, due to the non-deterministic nature of concurrency bugs, these bugs are both difficult to detect and fix even after the detection. As a result, it is highly desired to develop an all-around approach that is able to not only detect them during the testing phase but also tolerate undetected bugs during production runs. However, existing bug-detecting and bug-tolerating tools are usually either 1) constrained in types of bugs they can handle or 2) requiring specific hardware supports for achieving an acceptable overhead. In this paper, we present a novel program invariant, name Anticipating Invariant (Ai), that can detect most types of concurrency bugs. More importantly, Ai can be used to anticipate many concurrency bugs before any irreversible changes have been made. Thus it enables us to develop a software-only system that is able to forestall failures with a simple thread stalling technique, which does not rely on execution roll-back and hence has good performance. Experiments with 35 real-world concurrency bugs demonstrate that Ai is capable of detecting and tolerating many important types of concurrency bugs, including both atomicity and order violations. It has also exposed two new bugs (confirmed by developers) that were never reported before in the literature. Performance evaluation with 6 representative parallel programs shows that Ai incurs negligible overhead ( < 1%) for many nontrivial desktop and server applications. © 1976-2012 IEEE.
Author keywords: bug tolerating; Concurrency bugs; software reliability
Index keywords: Application programs; Concurrency control; Software reliability; bug tolerating; Concurrency bugs; Irreversible changes; Lightweight systems; Multi-threaded programs; Program invariants; Server applications; Specific hardware; Program debugging
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2016
EID: 2-s2.0-84994875757
DOI: 10.1109/tse.2016.2531666
Retrieval channels: authoritative_outlet_search
Local full-text files: 
