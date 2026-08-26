---
otero_id: "2-s2.0-85171551820"
title: "Neural Machine Translation for Recovering ASTs from Binaries"
authors: "Kc D.; Ferra T.; Morrison C.T."
year: "2023"
journal: "2023 3rd IEEE International Conference on Software Engineering and Artificial Intelligence, SEAI 2023"
doi: "10.1109/seai59139.2023.10217602"
---
# Scopus title-abstract-keyword metadata
Title: Neural Machine Translation for Recovering ASTs from Binaries
Abstract: Recovering higher-level abstractions of source code from binaries is an important task underlying malware identification, program verification, debugging, program comparison, vulnerability detection, and helping subject matter experts understand compiled code. Existing approaches to extracting higher-level structures from lower-level binary code rely on hand-crafted rules and generally require great time and effort of domain experts to design and implement. We present Binary2AST, a framework for generating a structured representation of binary code in the form of an abstract syntax tree (AST) using neural machine translation (NMT). We use the Ghidra binary analysis tool to extract assembly instructions from binaries. A tokenized version of these instructions are then translated by our NMT system into a sequence of symbols that represent an AST. The NMT framework uses deep neural network models that can require a lot of training examples. To address this, we have developed a C source code generator for a restricted subset of the C language, from which we can sample an arbitrary number of syntactically correct C source code files that in turn can be used to create a parallel data set suitable for NMT training. We evaluate several variant NMT models on their ability to recover AST representations of the original source code from compiled binaries, where the best-performing attention-based model achieves a BLEU score of 0.99 on our corpus. © 2023 IEEE.
Author keywords: abstract syntax tree; neural machine translation; transformer
Index keywords: Binary codes; C (programming language); Computational linguistics; Computer aided language translation; Neural machine translation; Program debugging; Recovery; Syntactics; Abstract Syntax Trees; C# source code; High-level abstraction; Higher-level abstraction; Malwares; Program Verification; Source codes; Subject matter experts; Transformer; Vulnerability detection; Deep neural networks
Document type: Conference paper
Conference: 
Source title: 2023 3rd IEEE International Conference on Software Engineering and Artificial Intelligence, SEAI 2023
Year: 2023
EID: 2-s2.0-85171551820
DOI: 10.1109/seai59139.2023.10217602
Retrieval channels: authoritative_outlet_search
Local full-text files: 
