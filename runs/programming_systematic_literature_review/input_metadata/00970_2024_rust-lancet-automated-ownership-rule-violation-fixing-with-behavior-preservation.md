---
otero_id: "2-s2.0-85196796859"
title: "Rust-lancet: Automated Ownership-Rule-Violation Fixing with Behavior Preservation"
authors: "Yang W.; Song L.; Xue Y."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3639103"
---
# Scopus title-abstract-keyword metadata
Title: Rust-lancet: Automated Ownership-Rule-Violation Fixing with Behavior Preservation
Abstract: As a relatively new programming language, Rust is designed to provide both memory safety and runtime performance. To achieve this goal, Rust conducts rigorous static checks against its safety rules during compilation, effectively eliminating memory safety issues that plague C/C++ programs. Although useful, the safety rules pose programming challenges to Rust programmers, since programmers can easily violate safety rules when coding in Rust, leading their code to be rejected by the Rust compiler, a fact underscored by a recent user study. There exists a desire to automate the process of fixing safety-rule violations to enhance Rust's programmability. In this paper, we concentrate on Rust's ownership rules and develop rust-lancet to automatically fix their violations. We devise three strategies for altering code, each intended to modify a Rust program and make it pass Rust's compiler checks. Additionally, we introduce mental semantics to model the behaviors of Rust programs that cannot be compiled due to ownership-rule violations. We design an approach to verify whether modified programs preserve their original behaviors before patches are applied. We apply rust-lancet to 160 safety-rule violations from two sources, successfully fixing 102 violations under the optimal configuration - more than RUSTC and six LLM-based techniques. Notably, rust-lancet avoids generating any incorrect patches, a distinction from all other baseline techniques. We also verify the effectiveness of each fixing strategy and behavior preservation validation and affirm the rationale behind these components.  © 2024 ACM.
Author keywords: Compiler Error; Error handling and recovery; Program Repair; Rust; Software and its engineering → General programming languages; Software development techniques
Index keywords: C++ (programming language); Program compilers; Safety engineering; Software design; Compiler error; Error handling and recovery; General programming; Ownership rules; Program repair; Rule violation; Rust; Safety rules; Software and its engineering → general programming language; Software development techniques; Semantics
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85196796859
DOI: 10.1145/3597503.3639103
Retrieval channels: authoritative_outlet_search
Local full-text files: 
