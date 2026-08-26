---
otero_id: "2-s2.0-84994128640"
title: "CARE: Cache guided deterministic replay for concurrent Java programs"
authors: "Jiang Y.; Gu T.; Xu C.; Ma X.; Lu J."
year: "2014"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/2568225.2568236"
---
# Scopus title-abstract-keyword metadata
Title: CARE: Cache guided deterministic replay for concurrent Java programs
Abstract: Deterministic replay tools help programmers debug concurrent programs. However, for long-running programs, a replay tool may generate huge log of shared memory access dependences. In this paper, we present CARE, an application-level deterministic record and replay technique to reduce the log size. The key idea of CARE is logging read-write dependences only at per-thread value prediction cache misses. This strategy records only a subset of all exact read-write dependences, and reduces synchronizations protecting memory reads in the instrumented code. Realizing that such record strategy provides only value-deterministic replay, CARE also adopts variable grouping and action prioritization heuristics to synthesize sequentially consistent executions at replay in linear time. We implemented CARE in Java and experimentally evaluated it with recognized benchmarks. Results showed that CARE successfully resolved all missing read-write dependences, producing sequentially consistent replay for all benchmarks. CARE exhibited 1.7 - 40X (median 3.4X) smaller runtime overhead, and 1.1 - 309X (median 7.0X) smaller log size against state-of-the-art technique LEAP. © 2014 ACM.
Author keywords: Cache; Concurrency; Debugging; Replay
Index keywords: Computer debugging; Computer software; Memory architecture; Program debugging; Software engineering; Well logging; Cache; Concurrency; Concurrent Java programs; Concurrent program; Deterministic replay; Record-and-replay; Replay; State-of-the-art techniques; Java programming language
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2014
EID: 2-s2.0-84994128640
DOI: 10.1145/2568225.2568236
Retrieval channels: authoritative_outlet_search
Local full-text files: 
