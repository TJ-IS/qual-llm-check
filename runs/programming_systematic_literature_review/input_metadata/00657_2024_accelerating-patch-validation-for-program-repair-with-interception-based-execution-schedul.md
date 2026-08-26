---
otero_id: "2-s2.0-85184309775"
title: "Accelerating Patch Validation for Program Repair with Interception-Based Execution Scheduling"
authors: "Xiao Y.-A.; Yang C.; Wang B.; Xiong Y."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3359969"
---
# Scopus title-abstract-keyword metadata
Title: Accelerating Patch Validation for Program Repair with Interception-Based Execution Scheduling
Abstract: Long patch validation time is a limiting factor for automated program repair (APR). Though the duality between patch validation and mutation testing is recognized, so far there exists no study of systematically adapting mutation testing techniques to general-purpose patch validation. To address this gap, we investigate existing mutation testing techniques and identify five classes of acceleration techniques that are suitable for general-purpose patch validation. Among them, mutant schemata and mutant deduplication have not been adapted to general-purpose patch validation due to the arbitrary changes that third-party APR approaches may introduce. This presents two problems for adaption: 1) the difficulty of implementing the static equivalence analysis required by the state-of-the-art mutant deduplication approach; 2) the difficulty of capturing the changes of patches to the system state at runtime. To overcome these problems, we propose two novel approaches: 1) execution scheduling, which detects the equivalence between patches online, avoiding the static equivalence analysis and its imprecision; 2) interception-based instrumentation, which intercepts the changes of patches to the system state, avoiding a full interpreter and its overhead. Based on the contributions above, we implement ExpressAPR, a general-purpose patch validator for Java that integrates all recognized classes of techniques suitable for patch validation. Our large-scale evaluation with four APR approaches shows that ExpressAPR accelerates patch validation by 137.1x over plain validation or 8.8x over the state-of-the-art approach, making patch validation no longer the time bottleneck of APR. Patch validation time for a single bug can be reduced to within a few minutes on mainstream CPUs. © 1976-2012 IEEE.
Author keywords: Automated program repair; patch validation
Index keywords: Equivalence classes; Instrument testing; Program debugging; Software testing; Automated program repair; Code; Computer bugs; Deduplication; Life estimation; Mutation testing; Patch validation; Runtimes; Static equivalence; Testing technique; Repair
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85184309775
DOI: 10.1109/tse.2024.3359969
Retrieval channels: authoritative_outlet_search
Local full-text files: 
