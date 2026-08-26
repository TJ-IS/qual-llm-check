---
otero_id: "2-s2.0-85171870184"
title: "Improving Automatic C-to-Rust Translation with Static Analysis"
authors: "Hong J."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse-companion58688.2023.00074"
---
# Scopus title-abstract-keyword metadata
Title: Improving Automatic C-to-Rust Translation with Static Analysis
Abstract: While popular in system programming, C has been infamous for its poor language-level safety mechanisms, leading to critical bugs and vulnerabilities. C programs can still have memory and thread bugs despite passing type checking. To resolve this long-standing problem, Rust has been recently developed with rich safety mechanisms, including its notable ownership type system. It prevents memory and thread bugs via type checking. By rewriting legacy C programs in Rust, their developers can discover unknown bugs and avoid adding new bugs. However, the adaptation of Rust in legacy programs is still limited due to the high cost of manual C-to-Rust translation. Rust's safe features are semantically different from C's unsafe features and require programmers to precisely understand the behavior of their programs for correct rewriting. Existing C-to-Rust translators do not relieve this burden because they syntactically translate C features into unsafe Rust features, leaving further refactoring for programmers. In this paper, we propose the problem of improving the state-of-the-art C-to-Rust translation by automatically replacing unsafe features with safe features. Specifically, we identify two important unsafe features to be replaced: lock API and output parameters. We show our results on lock API and discuss plans for output parameters. © 2023 IEEE.
Author keywords: 
Index keywords: C (programming language); Locks (fasteners); Program debugging; Program translators; C programs; In-system programming; Language levels; Output parameters; Ownership type; Safety mechanisms; Standing problems; Type systems; Typechecking; Unsafe features; Static analysis
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171870184
DOI: 10.1109/icse-companion58688.2023.00074
Retrieval channels: authoritative_outlet_search
Local full-text files: 
