---
otero_id: "2-s2.0-85100123309"
title: "CMFuzz: context-aware adaptive mutation for fuzzers"
authors: "Wang X.; Hu C.; Ma R.; Tian D.; He J."
year: "2021"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-020-09927-3"
---
# Scopus title-abstract-keyword metadata
Title: CMFuzz: context-aware adaptive mutation for fuzzers
Abstract: Mutation-based fuzzing is a simple yet effective technique to discover bugs and security vulnerabilities in software. Given a set of well-formed initial seeds, mutation-based fuzzers continually generate interesting seeds by applying specific mutation strategy in order to maximize code coverage or the number of unique bugs explored at any point-in-time. However, existing fuzzers remain limited in the paths it could cover since it simply follows a uniform distribution to choose mutation operators. In this paper, we proposed a novel context-aware adaptive mutation scheme, namely CMFuzz, which utilizes a contextual bandit algorithm LinUCB to effectively choose optimal mutation operators for various seed files. To this end, CMFuzz dynamically extracts and encodes file characteristics, which allows mutation-based fuzzers to perform context-aware mutation. We apply this scheme on top of several state-of-the-art fuzzers, i.e., PTfuzz, AFL, and AFLFast, and implement CMFuzz-PT, CMFuzz-AFL, and CMFuzz-AFLFast, respectively. We conduct evaluation on 12 real-world open source applications and LAVA-M dataset against their counterparts. Extensive evaluations demonstrate that CMFuzz-based fuzzers achieve higher code coverage and find more crashes at a faster rate than their counterparts on most cases. Furthermore, we also utilize other mainstream bandit algorithms, e.g., Thompson Sample and epsilon-greedy, and implement Thompson-PT and Greedy-PT based on PTfuzz to examine the performance of proposed model. CMFuzz-PT significantly outperforms Thompson-PT especially in terms of unique crashes and paths, i.e., found 1.79× unique crashes and 1.29× unique paths on average. Compared to Greedy-PT, our approach still increases the amount of unique crashes and paths by 1.11× and 1.05×, respectively. © 2021, The Author(s), under exclusive licence to Springer Science+Business Media, LLC part of Springer Nature.
Author keywords: Bandit algorithm; Context-aware; Fuzzing; Seed mutation
Index keywords: Codes (symbols); Open source software; Program debugging; Software testing; Adaptive mutation; Contextual bandits; Mutation operators; Mutation strategy; Open source application; Optimal mutation; Security vulnerabilities; Uniform distribution; Genetic algorithms
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2021
EID: 2-s2.0-85100123309
DOI: 10.1007/s10664-020-09927-3
Retrieval channels: authoritative_outlet_search
Local full-text files: 
