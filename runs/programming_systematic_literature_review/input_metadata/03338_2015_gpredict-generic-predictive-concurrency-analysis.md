---
otero_id: "2-s2.0-84951728761"
title: "GPredict: Generic predictive concurrency analysis"
authors: "Huang J.; Luo Q.; Rosu G."
year: "2015"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse.2015.96"
---
# Scopus title-abstract-keyword metadata
Title: GPredict: Generic predictive concurrency analysis
Abstract: Predictive trace analysis (PTA) is an effective approach for detecting subtle bugs in concurrent programs. Existing PTA techniques, however, are typically based on adhoc algorithms tailored to low-level errors such as data races or atomicity violations, and are not applicable to high-level properties such as "a resource must be authenticated before use" and "a collection cannot be modified when being iterated over". In addition, most techniques assume as input a globally ordered trace of events, which is expensive to collect in practice as it requires synchronizing all threads. In this paper, we present GPredict: a new technique that realizes PTA for generic concurrency properties. Moreover, GPredict does not require a global trace but only the local traces of each thread, which incurs much less runtime overhead than existing techniques. Our key idea is to uniformly model violations of concurrency properties and the thread causality as constraints over events. With an existing SMT solver, GPredict is able to precisely predict property violations allowed by the causal model. Through our evaluation using both benchmarks and real world applications, we show that GPredict is effective in expressing and predicting generic property violations. Moreover, it reduces the runtime overhead of existing techniques by 54% on DaCapo benchmarks on average. © 2015 IEEE.
Author keywords: 
Index keywords: Benchmarking; Program debugging; Trace analysis; Atomicity violations; Causal model; Concurrency analysis; Concurrent program; Effective approaches; Generic properties; Predictive traces; Runtime overheads; Software engineering
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2015
EID: 2-s2.0-84951728761
DOI: 10.1109/icse.2015.96
Retrieval channels: authoritative_outlet_search
Local full-text files: 
