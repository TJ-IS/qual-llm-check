---
otero_id: "2-s2.0-79959882115"
title: "Angelic debugging"
authors: "Chandra S.; Torlak E.; Barman S.; Bodik R."
year: "2011"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/1985793.1985811"
---
# Scopus title-abstract-keyword metadata
Title: Angelic debugging
Abstract: Software ships with known bugs because it is expensive to pinpoint and fix the bug exposed by a failing test. To reduce the cost of bug identification, we locate expressions that are likely causes of bugs and thus candidates for repair. Our symbolic method approximates an ideal approach to fixing bugs mechanically, which is to search the space of all edits to the program for one that repairs the failing test without breaking any passing test. We approximate the expensive ideal of exploring syntactic edits by instead computing the set of values whose substitution for the expression corrects the execution. We observe that an expression is a repair candidate if it can be replaced with a value that fixes a failing test and in each passing test, its value can be changed to another value without breaking the test. The latter condition makes the expression flexible in that it permits multiple values. The key observation is that the repair of a flexible expression is less likely to break a passing test. The method is called angelic debugging because the values are computed by angelically nondeterministic statements. We implemented the method on top of the Java PathFinder model checker. Our experiments with this technique show promise of its applicability in speeding up program debugging. © 2011 ACM.
Author keywords: angelic non-determinism; debugging; symbolic execution; tests
Index keywords: Model checking; Repair; Software engineering; Software testing; Testing; Java PathFinder; Model checker; Non-determinism; Symbolic execution; Symbolic methods; tests; Program debugging
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2011
EID: 2-s2.0-79959882115
DOI: 10.1145/1985793.1985811
Retrieval channels: authoritative_outlet_search
Local full-text files: 
