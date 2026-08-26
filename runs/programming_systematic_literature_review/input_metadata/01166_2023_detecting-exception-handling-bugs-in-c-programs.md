---
otero_id: "2-s2.0-85171771066"
title: "Detecting Exception Handling Bugs in C++ Programs"
authors: "Zhang H.; Luo J.; Hu M.; Yan J.; Zhang J.; Qiu Z."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00098"
---
# Scopus title-abstract-keyword metadata
Title: Detecting Exception Handling Bugs in C++ Programs
Abstract: Exception handling is a mechanism in modern programming languages. Studies have shown that the exception handling code is error-prone. However, there is still limited research on detecting exception handling bugs, especially for C++ programs. To tackle the issue, we try to precisely represent the exception control flow in C++ programs and propose an analysis method that makes use of the control flow to detect such bugs. More specifically, we first extend control flow graph by introducing the concepts of five different kinds of basic blocks, and then modify the classic symbolic execution framework by extending the program state to a quadruple and properly processing try, throw and catch statements. Based on the above techniques, we develop a static analysis tool on the top of Clang Static Analyzer to detect exception handling bugs. We run our tool on projects with high stars from GitHub and find 36 exception handling bugs in 8 projects, with a precision of 84%. We compare our tool with four state-of-the-art static analysis tools (Cppcheck, Clang Static Analyzer, Facebook Infer and IKOS) on projects from GitHub and handmade benchmarks. On the GitHub projects, other tools are not able to detect any exception handling bugs found by our tool. On the handmade benchmarks, our tool has a significant higher recall. © 2023 IEEE.
Author keywords: bug finding; exception handling; static analysis
Index keywords: C++ (programming language); Computer software; Data flow analysis; Flow graphs; Program debugging; Analysis method; Analysis tools; Basic blocks; Bug finding; C programs; Control-flow; Control-flow graphs; Error prones; Exception handling; Static analyzers; Static analysis
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171771066
DOI: 10.1109/icse48619.2023.00098
Retrieval channels: authoritative_outlet_search
Local full-text files: 
