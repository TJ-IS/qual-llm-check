---
otero_id: "2-s2.0-84979741017"
title: "ReSeer: Efficient search-based replay for multiprocessor virtual machines"
authors: "Wang T.; Xu J.; Zhang W.; Zhang J.; Wei J.; Zhong H."
year: "2017"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2016.07.032"
---
# Scopus title-abstract-keyword metadata
Title: ReSeer: Efficient search-based replay for multiprocessor virtual machines
Abstract: Efficient replay of virtual machines is important for software debugging, fault tolerance, and performance analysis. The current approaches of replaying virtual machines record the details of system execution at runtime. However, these approaches incur much overhead, which affects the system performance. Especially, in a multiprocessor system, recording the shared memory operations of multiple processors leads to a large amount of computing overhead and log files. To address the above issue, this paper proposes ReSeer—a search-based replay approach for multiprocessor virtual machines. ReSeer consists of three phases including record, search, and replay. In the record phase, we record only necessary non-deterministic events at runtime, and incrementally take memory checkpoints at a defined interval. In the search phase, we encode all the possible execution paths as binary strings, and use a genetic algorithm to search expected execution paths achieving the expected checkpoint. In the replay phase, we replay the system execution according to the searched execution paths and the logged non-deterministic events. Compared with current approaches, ReSeer significantly reduces performance overhead at runtime by searching expected execution paths instead of recording all the operations of accessing shared memory. We have implemented ReSeer, and then evaluated it with a series of typical benchmarks deployed on an open source virtual machine—Xen. The experimental results show that ReSeer can reduce the record overhead at runtime efficiently. © 2016 Elsevier Inc.
Author keywords: Deterministic replay; Genetic algorithm; Memory checkpoint; Virtual machine; Xen
Index keywords: Cost reduction; Fault tolerance; Genetic algorithms; Java programming language; Memory architecture; Multiprocessing systems; Open source software; Virtual addresses; Deterministic replay; Execution paths; Multi processor systems; Multiple processors; Non-deterministic events; Performance analysis; Software debugging; Virtual machines; Program debugging
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2017
EID: 2-s2.0-84979741017
DOI: 10.1016/j.jss.2016.07.032
Retrieval channels: authoritative_outlet_search
Local full-text files: 
