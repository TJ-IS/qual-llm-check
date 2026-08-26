---
otero_id: "2-s2.0-85211583169"
title: "MoCo: Fuzzing Deep Learning Libraries via Assembling Code"
authors: "Ji P.; Feng Y.; Wu D.; Yan L.; Chen P.; Liu J.; Zhao Z."
year: "2025"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3509975"
---
# Scopus title-abstract-keyword metadata
Title: MoCo: Fuzzing Deep Learning Libraries via Assembling Code
Abstract: The rapidly developing Deep Learning (DL) techniques have been applied in software systems of various types. However, they can also pose new safety threats with potentially serious consequences, especially in safety-critical domains. DL libraries serve as the underlying foundation for DL systems, and bugs in them can have unpredictable impacts that directly affect the behaviors of DL systems. Previous research on fuzzing DL libraries still has limitations in generating tests corresponding to crucial testing scenarios and constructing test oracles. In this paper, we propose MoCo, a novel fuzzing testing method for DL libraries via assembling code. The seed tests used by MoCo are code files that implement DL models, covering both model construction and training in the most common real-world application scenarios for DL libraries. MoCo first disassembles the seed code files to extract templates and code blocks, then applies code block mutation operators (e.g., API replacement, random generation, and boundary checking) to generate new code blocks that fit the template. To ensure the correctness of the code block mutation, we employ the Large Language Model to parse the official documents of DL libraries for information about the parameters and the constraints between them. By inserting context-appropriate code blocks into the template, MoCo can generate a tree of code files with intergenerational relations. According to the derivation relations in this tree, we construct the test oracle based on the execution state consistency and the calculation result consistency. Since the granularity of code assembly is controlled rather than randomly divergent, we can quickly pinpoint the lines of code where the bugs are located and the corresponding triggering conditions. We conduct a comprehensive experiment to evaluate the efficiency and effectiveness of MoCo using three widely-used DL libraries (i.e., TensorFlow, PyTorch, and Jittor). During the experiments, MoCo detects 77 new bugs of four types in three DL libraries, where 55 bugs have been confirmed, and 39 bugs have been fixed by developers. The experimental results demonstrate that MoCo can generate high-quality tests that cover crucial testing scenarios and detect different types of bugs, which helps developers improve the reliability of DL libraries.  © 1976-2012 IEEE.
Author keywords: bug detection; Deep learning libraries; deep learning testing; fuzzing
Index keywords: Computer debugging; Failure analysis; Model checking; Problem oriented languages; Program debugging; Subjective testing; Bug detection; Code blocks; Deep learning library; Deep learning testing; Fuzzing; Learning techniques; Safety threat; Safety-critical domain; Software-systems; Test oracles; Software testing
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2025
EID: 2-s2.0-85211583169
DOI: 10.1109/tse.2024.3509975
Retrieval channels: authoritative_outlet_search
Local full-text files: 
