---
otero_id: "2-s2.0-84864583564"
title: "Finding atomicity-violation bugs through unserializable interleaving testing"
authors: "Lu S.; Park S.; Zhou Y."
year: "2012"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2011.35"
---
# Scopus title-abstract-keyword metadata
Title: Finding atomicity-violation bugs through unserializable interleaving testing
Abstract: Multicore hardware is making concurrent programs pervasive. Unfortunately, concurrent programs are prone to bugs. Among different types of concurrency bugs, atomicity violations are common and important. How to test the interleaving space and expose atomicity-violation bugs is an open problem. This paper makes three contributions. First, it designs and evaluates a hierarchy of four interleaving coverage criteria using 105 real-world concurrency bugs. This study finds a coverage criterion (Unserializable Interleaving Coverage) that balances the complexity and the capability of exposing atomicity-violation bugs well. Second, it studies stress testing to understand why this common practice cannot effectively expose atomicity-violation bugs from the perspective of unserializable interleaving coverage. Third, it designs CTrigger following the unserializable interleaving coverage criterion. CTrigger uses trace analysis to identify feasible unserializable interleavings, and then exercises low-probability interleavings to expose atomicity-violation bugs. We evaluate CTrigger with real-world atomicity-violation bugs from seven applications. CTrigger efficiently exposes these bugs within 1-235 seconds, two to four orders of magnitude faster than stress testing. Without CTrigger, some of these bugs do not manifest even after seven days of stress testing. Furthermore, once a bug is exposed, CTrigger can reliably reproduce it, usually within 5 seconds, for diagnosis. © 2012 IEEE.
Author keywords: bug characteristics; concurrent programming; debugging aids; diagnostics; test coverage of code; Testing and debugging; testing strategies
Index keywords: Multicore programming; Plasma diagnostics; Program debugging; Trace analysis; Bug characteristics; Concurrent programming; Debugging aids; Test coverage; Testing and debugging; Testing strategies; Program diagnostics
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2012
EID: 2-s2.0-84864583564
DOI: 10.1109/tse.2011.35
Retrieval channels: authoritative_outlet_search
Local full-text files: 
