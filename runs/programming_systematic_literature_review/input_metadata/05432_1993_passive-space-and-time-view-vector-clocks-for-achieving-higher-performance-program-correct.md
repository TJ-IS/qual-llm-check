---
otero_id: "2-s2.0-0027659495"
title: "Passive-space and Time View: Vector Clocks for Achieving Higher Performance, Program Correction, and Distributed Computing"
authors: "Ahuja M.; Carlson T."
year: "1993"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/32.241768"
---
# Scopus title-abstract-keyword metadata
Title: Passive-space and Time View: Vector Clocks for Achieving Higher Performance, Program Correction, and Distributed Computing
Abstract: We have noticed two problems with viewing a process as a sequence of events: The first problem is the complete loss of information about potential intra-process concurrency for both sequential and distributed computations, and partial loss of information about potential inter-process concurrency for distributed computations. The second problem is that the resulting reasoning framework does not lend itself to refinement (from sequential computing or a given set of distributed processes) to a preferable set of distributed processes. We argue that it is more natural to view a computation, either distributed or sequential, as a partially ordered set of events. Doing so leads to a view, called passive-space and time view, which we propose in this paper. In the proposed view, a point in space is a passive entity which does not order events that occur at it, and the order is determined by the interaction among the events. We define a relation, “Affects”, between pairs of events, which captures the partial order on events. To aid users of the relation “Affects” in developing algorithms, we define vector clocks, that are global logical clocks, so that the relation “Affects”, and hence all potential concurrency, between events can be identified from their timestamps assigned. Since this research is motivated by the need to solve practical problems, we define passive-space and time view such that a user has control, in two ways, over the costs involved. First, a process designer may choose any granularity of events and choose any mechanism for determining partial order among events on the process. Second, a user may choose a vector clock such that the extent of potential intra-process concurrency identified depends on the costs associated with the identification. We give vector clocks which trade cost incurred and concurrency identification. We compare the proposed view with the space and time view. Finally, we give a scheme for reducing the cost of communicating timestamps. © 1993 IEEE
Author keywords: and concurrency; distributed computing; event causality; event ordering; Experimental systems; global logical clocks; high-performance computing; measuring parallelism; program correction (debugging); timestamps; vector clocks
Index keywords: Algorithms; Clocks; Performance; Program debugging; Event ordering; Vector clocks; Distributed computer systems
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 1993
EID: 2-s2.0-0027659495
DOI: 10.1109/32.241768
Retrieval channels: authoritative_outlet_search
Local full-text files: 
