---
otero_id: "2-s2.0-105041978819"
title: "Automated and configurable undo for CRDT-based distributed systems via metaprogramming"
authors: "Mondal P.; Tilevich E."
year: "2026"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2026.112986"
---
# Scopus title-abstract-keyword metadata
Title: Automated and configurable undo for CRDT-based distributed systems via metaprogramming
Abstract: Distributed nodes can access and modify replicated data using Conflict-free Replicated Data Types (CRDTs), which provide intuitive programming abstractions and enforce Strong Eventual Consistency (SEC) for conflict resolution. As a result of user errors, program bugs, or hardware malfunctions, a CRDT may be updated incorrectly, necessitating the undoing of the effects of executed operations. However, since many CRDT libraries lack built-in undo support, adding this capability requires modifying the library's source code, which is difficult to implement in a modular and reusable manner. Consequently, programmers often add this functionality ad hoc, resulting in code that is difficult to understand, maintain, and reuse. To address this problem, this paper presents CAMEL, a metaprogramming-based approach that automatically generates and actuates undo functionality for existing operation-based CRDT libraries using simple metadata configurations, without requiring manual source code modifications. The configurations specify which operations undo each other and the conditions that trigger the undo procedures. Based on this metadata, CAMEL generates a sequence of update operations that reverses the specified updates while preserving system consistency. We have implemented CAMEL in JavaScript and evaluated it against two state-of-the-art approaches. To demonstrate CAMEL's applicability, we apply it to three representative CRDTs of increasing complexity—Counter, Set, and Map—spanning scalar, collection, and associative data structures commonly deployed in practice. Our evaluation demonstrates that CAMEL reduces latency by approximately 7%–12% and memory consumption by approximately 6%–26%, on average, while software quality metrics shows that CAMEL enhances modularity, effectively streamlining the complexity of adding advanced features to distributed programming paradigms.1 Editor's note: Open Science material was validated by the Journal of Systems and Software Open Science Board. © 2026 Elsevier Inc.
Author keywords: Automated error recovery; Conflict-free Replicated Data Types (CRDTs); Distributed systems reliability; Metaprogramming; Strong eventual consistency
Index keywords: Abstract data types; Computer software reusability; Computer software selection and evaluation; Distributed computer systems; Distributed database systems; Libraries; Metadata; Open source software; Software quality; Automated error recovery; Conflict free; Conflict-free replicated data type; Datatypes; Distributed system reliability; Error-recovery; Eventual consistency; Meta Programming; Replicated data; Strong eventual consistency; Codes (symbols)
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2026
EID: 2-s2.0-105041978819
DOI: 10.1016/j.jss.2026.112986
Retrieval channels: authoritative_outlet_search
Local full-text files: 
