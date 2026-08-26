---
otero_id: "2-s2.0-85049406802"
title: "Inferring and asserting distributed system invariants"
authors: "Grant S.; Cech H.; Beschastnikh I."
year: "2018"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3180155.3180199"
---
# Scopus title-abstract-keyword metadata
Title: Inferring and asserting distributed system invariants
Abstract: Distributed systems are difficult to debug and understand. A key reason for this is distributed state, which is not easily accessible and must be pieced together from the states of the individual nodes in the system. We propose Dinv, an automatic approach to help developers of distributed systems uncover the runtime distributed state properties of their systems. Dinv uses static and dynamic program analyses to infer relations between variables at different nodes. For example, in a leader election algorithm, Dinv can relate the variable leader at different nodes to derive the invariant ∀ nodes i, j, leaderi = leaderj. This can increase the developer's confidence in the correctness of their system. The developer can also use Dinv to convert an inferred invariant into a distributed runtime assertion on distributed state. We applied Dinv to several popular distributed systems, such as etcd Raft, Hashicorp Serf, and Taipei-Torrent, which have between 1.7K and 144K LOC and are widely used. Dinv derived useful invariants for these systems, including invariants that capture the correctness of distributed routing strategies, leadership, and key hash distribution. We also used Dinv to assert correctness of the inferred etcd Raft invariants at runtime, using these asserts to detect injected silent bugs. © 2018 ACM.
Author keywords: 
Index keywords: Software engineering; Automatic approaches; Distributed routing; Distributed runtime; Distributed state; Distributed systems; Dynamic program analysis; Leader election algorithm; Runtimes; Program debugging
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2018
EID: 2-s2.0-85049406802
DOI: 10.1145/3180155.3180199
Retrieval channels: authoritative_outlet_search
Local full-text files: 
