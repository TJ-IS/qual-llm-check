---
otero_id: "2-s2.0-85183357030"
title: "ECFuzz: Effective Configuration Fuzzing for Large-Scale Systems"
authors: "Li J.; Luo F.; Li S.; Yu H.; Li X.; Li K.; Li S."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3623315"
---
# Scopus title-abstract-keyword metadata
Title: ECFuzz: Effective Configuration Fuzzing for Large-Scale Systems
Abstract: A large-scale system contains a huge configuration space because of its large number of configuration parameters. This leads to a combination explosion among configuration parameters when exploring the configuration space. Existing configuration testing techniques first use fuzzing to generate different configuration parameters, and then directly inject them into the program under test to find configuration-induced bugs. However, they do not fully consider the complexity of large-scale systems, resulting in low testing effectiveness. In this paper, we propose ECFuzz, an effective configuration fuzzer for large-scale systems. Our core approach consists of (i) Multi-dimensional configuration generation strategy. ECFuzz first designs different mutation strategies according to different dependencies and selects multiple configuration parameters from the candidate configuration parameters to effectively generate configuration parameters; (ii) Unit-testing-oriented configuration validation strategy. ECFuzz introduces unit testing into configuration testing techniques to filter out configuration parameters that are unlikely to yield errors before executing system testing, and effectively validate generated configuration parameters. We have conducted extensive experiments in real-world large-scale systems including HCommon, HDFS, HBase, ZooKeeper and Alluxio. Our evaluation shows that ECFuzz is effective in finding configuration-induced crash bugs. Compared with the state-of-the-art configuration testing tools including ConfTest, ConfErr and ConfDiagDetector, ECFuzz finds 60.3–67 more unexpected failures when the same 1000 testcases are injected into the system with an increase of 1.87x–2.63x. Moreover, ECFuzz has exposed 14 previously unknown bugs, and 5 of them have been confirmed. © 2024 IEEE Computer Society. All rights reserved.
Author keywords: Configuration; Fuzzing; Large-Scale Systems; Testing
Index keywords: Program debugging; Software testing; System theory; Wave functions; Configuration; Configuration parameters; Configuration space; First designs; Fuzzing; Large-scale systems; Multi dimensional; Testing effectiveness; Testing technique; Unit testing; Large scale systems
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85183357030
DOI: 10.1145/3597503.3623315
Retrieval channels: authoritative_outlet_search
Local full-text files: 
