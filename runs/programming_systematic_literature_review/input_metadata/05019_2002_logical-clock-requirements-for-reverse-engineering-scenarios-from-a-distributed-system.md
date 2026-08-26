---
otero_id: "2-s2.0-0036530164"
title: "Logical clock requirements for reverse engineering scenarios from a distributed system"
authors: "Hrischuk C.E.; Woodside C.M."
year: "2002"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2002.995416"
---
# Scopus title-abstract-keyword metadata
Title: Logical clock requirements for reverse engineering scenarios from a distributed system
Abstract: To reverse engineer scenarios from event traces, one must infer causal relationships between events. The inferences are usually based on a trace with sequence numbers or timestamps corresponding to some kind of logical clock. In practice, there is an explosion of potentially causal relationships in the trace, which limits one's ability to extract scenarios. This work defines a more parsimonious form of causality called scenario causality that concentrates on certain major causal relationships and ignores more subtle potentially causal links. The influence of an event is restricted to the particular scenario it is part of. An event which is not a message reception is defined to be caused by the previous event in the same software object, while a message reception is caused by a sending event in another object. The events are ordered to form a scenario event graph where typed nodes are events and the typed edges are certain causal relationships. Intuitively, we might say that most logical clocks, which identify events which "happened before" a given event and, thus, are potentially causal, give an upper bound on the set of causal events; scenario causality identifies a lower bound. The much smaller lower bound set makes it possible to reverse engineer and automate the analysis of scenarios.
Author keywords: Causal order; Debugging; Distributed programming; Event labeling; Graph grammar; Logical clock; Reverse engineering; Software tracing; Trace analysis; Web services
Index keywords: Context sensitive grammars; Distributed computer systems; Inference engines; Logic programming; Object oriented programming; Program debugging; Requirements engineering; Sequential machines; Time sharing systems; Web browsers; Causal order; Event labeling; Graph grammar; Logical clock; Scenario event graph; Software object; Software tracing; Web services; Reverse engineering
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2002
EID: 2-s2.0-0036530164
DOI: 10.1109/tse.2002.995416
Retrieval channels: authoritative_outlet_search
Local full-text files: 
