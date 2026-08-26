---
otero_id: "2-s2.0-0036041892"
title: "Specifying multithreaded Java semantics for program verification"
authors: "Roychoudhury A.; Mitra T."
year: "2002"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/581396.581399"
---
# Scopus title-abstract-keyword metadata
Title: Specifying multithreaded Java semantics for program verification
Abstract: The Java programming language supports multithreading where the threads interact among themselves via read/write of shared data. Most current work on multithreaded Java program verification assumes a model of execution that is based on interleaving of the operations of the individual threads. However, the Java language specification (which any implementations of Java multithreading must follow) supports a weaker model of execution, called the Java Memory Model (JMM). The JMM allows certain reordering of operations within a thread and thus permits more behaviors than the interleaving based execution model. Therefore, programs verified by assuming interleaved thread execution may not behave correctly for certain Java multithreading implementations. The main difficulty with the JMM is that it is informally described in an abstract rule-based declarative style, which is unsuitable for formal verification. In this paper, we develop an equivalent formal executable specifications of the JMM. Our specification is operational and uses guarded commands. We then use this executable model to verify popular software construction idioms (commonly used program fragments/patterns) for multithreaded Java. Our prototype verifier tool detects a bug in the widely used "Double-Checked Locking" idiom, which verifiers based on interleaving execution model cannot possibly detect.
Author keywords: 
Index keywords: Computer software selection and evaluation; Java programming language; Program compilers; Program debugging; Semantics; Synchronization; Java memory model; Multithreaded Java semantics; Program verification; Program diagnostics
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2002
EID: 2-s2.0-0036041892
DOI: 10.1145/581396.581399
Retrieval channels: authoritative_outlet_search
Local full-text files: 
