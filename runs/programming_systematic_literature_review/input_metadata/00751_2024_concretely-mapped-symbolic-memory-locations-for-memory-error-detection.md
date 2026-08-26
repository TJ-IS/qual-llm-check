---
otero_id: "2-s2.0-85192141715"
title: "Concretely Mapped Symbolic Memory Locations for Memory Error Detection"
authors: "Tu H.; Jiang L.; Hong J.; Ding X.; Jiang H."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3395412"
---
# Scopus title-abstract-keyword metadata
Title: Concretely Mapped Symbolic Memory Locations for Memory Error Detection
Abstract: Memory allocation is a fundamental operation for managing memory objects in many programming languages. Misusing allocated memory objects (e.g., buffer overflow and use-after-free) can have catastrophic consequences. Symbolic execution-based approaches have been used to detect such memory errors, benefiting from their capabilities in automatic path exploration and test case generation. However, existing symbolic execution engines still suffer from fundamental limitations in modeling dynamic memory layouts; they either represent the locations of memory objects as concrete addresses and thus limit their analyses only to specific address layouts and miss errors that may only occur when the objects are located at special addresses, or represent the locations as simple symbolic variables without sufficient constraints and thus suffer from memory state explosion when they execute read/write operations involving symbolic addresses. Such limitations hinder the existing symbolic execution engines from effectively detecting certain memory errors. In this study, we propose SymLoc, a symbolic execution-based approach that uses concretely mapped symbolic memory locations to alleviate the limitations mentioned above. Specifically, a new integration of three techniques is designed in SymLoc: (1) the symbolization of addresses and encoding of symbolic addresses into path constraints, (2) the symbolic memory read/write operations using a symbolic-concrete memory map, and (3) the automatic tracking of the uses of symbolic memory locations. We build SymLoc on top of the well-known symbolic execution engine KLEE and demonstrate its benefits in terms of memory error detection and code coverage capabilities. Our evaluation results show that: for address-specific spatial memory errors, SymLoc can detect 23 more errors in GNU Coreutils, Make, and m4 programs that are difficult for other approaches to detect, and cover 15% and 48% more unique lines of code in the programs than two baseline approaches; for temporal memory errors, SymLoc can detect 8%-64% more errors in the Juliet Test Suite than various existing state-of-the-art memory error detectors. We also present two case studies to show sample memory errors detected by SymLoc along with their root causes and implications. © 2024 IEEE.
Author keywords: memory errors; program analysis; Software reliability; software security; symbolic execution
Index keywords: Codes (symbols); Concretes; Engines; Error detection; Location; Memory architecture; Model checking; Open source software; Program debugging; Random access storage; Random errors; Reliability analysis; Storage allocation (computer); Code; Memory error; Memory-management; Program analysis; Random access memory; Resource management; Software security; Software-Reliability; Symbolic execution; Software reliability
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85192141715
DOI: 10.1109/tse.2024.3395412
Retrieval channels: authoritative_outlet_search
Local full-text files: 
