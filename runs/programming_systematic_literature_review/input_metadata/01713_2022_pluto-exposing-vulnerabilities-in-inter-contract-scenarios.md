---
otero_id: "2-s2.0-85117084640"
title: "Pluto: Exposing Vulnerabilities in Inter-Contract Scenarios"
authors: "Ma F.; Xu Z.; Ren M.; Yin Z.; Chen Y.; Qiao L.; Gu B.; Li H.; Jiang Y.; Sun J."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2021.3117966"
---
# Scopus title-abstract-keyword metadata
Title: Pluto: Exposing Vulnerabilities in Inter-Contract Scenarios
Abstract: Attacks on smart contracts have caused considerable losses to digital assets. Many techniques based on symbolic execution, fuzzing, and static analysis are used to detect contract vulnerabilities. Most of the current analyzers only consider vulnerability detection intra-contract scenarios. However, Ethereum contracts usually interact with others by calling their functions. A bug hidden in a path that depends on information from external contract calls is defined as an inter-contract vulnerability. Failure to deal with this kind of bug can result in potential false negatives and false positives. In this work, we propose Pluto, which supports vulnerability detection in inter-contract scenarios. It first builds an Inter-contract Control Flow Graph (ICFG) to extract semantic information among contract calls. Afterward, it symbolically explores the ICFG and deduces Inter-Contract Path Constraints (ICPC) to check the reachability of execution paths more accurately. Finally, Pluto detects whether there is a vulnerability based on some predefined rules. For evaluation, we compare Pluto with five state-of-the-art tools, including Oyente, Mythril, Securify, ILF, and Clairvoyance on a labeled benchmark and 39,443 real-world Ethereum smart contracts. The result shows that other tools can only detect 10% of the inter-contract vulnerabilities, while Pluto can detect 80% of them on the labeled dataset. Beyond that, Pluto has detected 451 confirmed vulnerabilities on real-world contracts, including 36 vulnerabilities in inter-contract scenarios. Two bugs have been assigned with unique CVE identifiers by the US National Vulnerability Database (NVD). On average, Pluto costs 16.9 seconds to analyze a contract, which is as fast as the state-of-the-art tools.  © 1976-2012 IEEE.
Author keywords: ethereum; inter-contract vulnerabilities; Smart contracts
Index keywords: Data flow analysis; Ethereum; Flow graphs; Program debugging; Semantics; Static analysis; Code; Computer bugs; Control-flow graphs; Digital assets; Inter-contract vulnerability; Pluto; Real-world; State of the art; Virtual machining; Vulnerability detection; Smart contract
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85117084640
DOI: 10.1109/tse.2021.3117966
Retrieval channels: authoritative_outlet_search
Local full-text files: 
