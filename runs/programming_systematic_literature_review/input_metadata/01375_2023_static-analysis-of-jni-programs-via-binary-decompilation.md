---
otero_id: "2-s2.0-85148475131"
title: "Static Analysis of JNI Programs via Binary Decompilation"
authors: "Park J.; Lee S.; Hong J.; Ryu S."
year: "2023"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2023.3241639"
---
# Scopus title-abstract-keyword metadata
Title: Static Analysis of JNI Programs via Binary Decompilation
Abstract: JNI programs are widely used thanks to the combined benefits of C and Java programs. However, because understanding the interaction behaviors between two different programming languages is challenging, JNI program development is difficult to get right and vulnerable to security attacks. Thus, researchers have proposed static analysis of JNI program source code to detect bugs and security vulnerabilities in JNI programs. Unfortunately, such source code analysis is not applicable to compiled JNI programs that are not open-sourced or open-source JNI programs containing third-party binary libraries. While JN-SAF, the state-of-the-art analyzer for compiled JNI programs, can analyze binary code, it has several limitations due to its symbolic execution and summary-based bottom-up analysis. In this paper, we propose a novel approach to statically analyze compiled JNI programs without their source code using binary decompilation. Unlike JN-SAF that analyzes binaries directly, our approach decompiles binaries and analyzes JNI programs with the decompiled binaries using an existing JNI program analyzer for source code. To decompile binaries to compilable C source code with precise JNI-interoperation-related types, we improve an existing decompilation tool by leveraging the characteristics of JNI programs. Our evaluation shows that the approach is precise as almost the same as the state-of-the-art JNI program analyzer for source code, and more precise than JN-SAF.  © 1976-2012 IEEE.
Author keywords: binary decompilation; Java native interface; static analysis
Index keywords: Behavioral research; C (programming language); Codes (symbols); Computer architecture; Java programming language; Libraries; Open source software; Program debugging; Security systems; Binary decompilation; C programs; Code; Decompilation; Java; Java Native Interfaces; Security; Source codes; Source-coding; State of the art; Static analysis
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2023
EID: 2-s2.0-85148475131
DOI: 10.1109/tse.2023.3241639
Retrieval channels: authoritative_outlet_search
Local full-text files: 
