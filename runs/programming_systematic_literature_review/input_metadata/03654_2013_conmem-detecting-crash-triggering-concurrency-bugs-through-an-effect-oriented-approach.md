---
otero_id: "2-s2.0-84876113775"
title: "ConMem: Detecting crash-triggering concurrency bugs through an effect-oriented approach"
authors: "Zhang W.; Sun C.; Lim J.; Lu S.; Reps T."
year: "2013"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/2430545.2430546"
---
# Scopus title-abstract-keyword metadata
Title: ConMem: Detecting crash-triggering concurrency bugs through an effect-oriented approach
Abstract: Multicore technology is making concurrent programs increasingly pervasive. Unfortunately, it is difficult to deliver reliable concurrent programs, because of the huge and nondeterministic interleaving space. In reality, without the resources to thoroughly check the interleaving space, critical concurrency bugs can slip into production versions and cause failures in the field. Approaches to making the best use of the limited resources and exposing severe concurrency bugs before software release would be desirable. Unlike previous work that focuses on bugs caused by specific interleavings (e.g., races and atomicity violations), this article targets concurrency bugs that result in one type of severe effect: program crashes. Our study of the error-propagation process of real-world concurrency bugs reveals a common pattern (50% in our nondeadlock concurrency bug set) that is highly correlated with program crashes. We call this pattern concurrency-memory bugs: buggy interleavings directly cause memory bugs (NULL-pointer-dereferences, dangling-pointers, buffer-overflows, uninitialized-reads) on shared memory objects. Guided by this study, we built ConMem to monitor program execution, analyze memory accesses and synchronizations, and predictively detect these common and severe concurrency-memory bugs. We also built a validator,ConMem-v, to automatically prune false positives by enforcing potential bug-triggering interleavings. We evaluated ConMem using 7 open-source programs with 10 real-world concurrency bugs. ConMem detects more tested bugs (9 out of 10 bugs) than a lock-set-based race detector and an unserializableinterleaving detector, which detect 4 and 6 bugs, respectively, with a false-positive rate about one tenth of the compared tools. ConMem-v further prunes out all the false positives. ConMem has reasonable overhead suitable for development usage. © 2013 ACM.
Author keywords: Concurrency bugs; Software testing
Index keywords: Multicore programming; Software testing; Atomicity violations; Concurrency bugs; Concurrent program; Error propagation; Highly-correlated; Multicore technology; Open-source program; Program execution; Program debugging
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2013
EID: 2-s2.0-84876113775
DOI: 10.1145/2430545.2430546
Retrieval channels: authoritative_outlet_search
Local full-text files: 
