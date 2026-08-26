---
otero_id: "2-s2.0-85214580321"
title: "DiPri: Distance-Based Seed Prioritization for Greybox Fuzzing"
authors: "Qian R.; Zhang Q.; Fang C.; Yang D.; Li S.; Li B.; Chen Z."
year: "2024"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3654440"
---
# Scopus title-abstract-keyword metadata
Title: DiPri: Distance-Based Seed Prioritization for Greybox Fuzzing
Abstract: Greybox fuzzing is a powerful testing technique. Given a set of initial seeds, greybox fuzzing continuously generates new test inputs to execute the program under test and drives executions with code coverage as feedback. Seed prioritization is an important step of greybox fuzzing that helps greybox fuzzing choose promising seeds for input generation in priority. However, mainstream greybox fuzzers like AFL++ and Zest tend to neglect the importance of seed prioritization. They may pick seeds plainly according to the sequential order of the seeds being queued or an order produced with a random-based approach, which may consequently degrade their performance in exploring code and exposing bugs. In the meantime, existing state-of-the-art techniques like Alphuzz and K-Scheduler adopt complex strategies to schedule seeds. Although powerful, such strategies also inevitably incur great overhead and will reduce the scalability of the proposed technique.In this article, we propose a novel distance-based seed prioritization approach named DiPri to facilitate greybox fuzzing. Specifically, DiPri evaluates the queued seeds according to seed distances and chooses the outlier ones, which are the farthest from the others, in priority to improve the probabilities of discovering previously unexplored code regions. To make a profound evaluation of DiPri, we prototype DiPri on AFL++ and conduct large-scale experiments with four baselines and 24 C/C++ fuzz targets, where eight are from widely adopted real-world projects, eight are from the coverage-based benchmark FuzzBench, and eight are from the bug-based benchmark Magma. The results obtained through a fuzzing exceeding 50,000 CPU hours suggest that DiPri can (1) insignificantly influence the host fuzzer's capability of code coverage by slightly improving the branch coverage on the eight targets from real-world projects and slightly reducing the branch coverage on the eight targets from FuzzBench, and (2) improve the host fuzzer's capability of finding bugs by triggering five more Magma bugs. Besides the evaluation with the three C/C++ benchmarks, we integrate DiPri into the Java fuzzer Zest and conduct experiments on a Java benchmark composed of five real-world programs for more than 8,000 CPU hours to empirically study the scalability of DiPri. The results with the Java benchmark demonstrate that DiPri is pretty scalable and can help the host fuzzer find bugs more consistently. © 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Greybox fuzzing; seed distance; seed prioritization
Index keywords: Benchmarking; C++ (programming language); Java programming language; Model checking; Problem oriented languages; Program debugging; Program processors; Branch-coverage; Code coverage; Distance-based; Grey-box; Greybox fuzzing; Prioritization; Real world projects; Seed distance; Seed prioritization; Testing technique; Software testing
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2024
EID: 2-s2.0-85214580321
DOI: 10.1145/3654440
Retrieval channels: authoritative_outlet_search
Local full-text files: 
