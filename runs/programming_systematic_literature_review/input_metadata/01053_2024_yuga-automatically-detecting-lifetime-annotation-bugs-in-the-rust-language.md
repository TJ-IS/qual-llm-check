---
otero_id: "2-s2.0-85201745129"
title: "Yuga: Automatically Detecting Lifetime Annotation Bugs in the Rust Language"
authors: "Nitin V.; Mulhern A.; Arora S.; Ray B."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3447671"
---
# Scopus title-abstract-keyword metadata
Title: Yuga: Automatically Detecting Lifetime Annotation Bugs in the Rust Language
Abstract: The Rust programming language is becoming increasingly popular among systems programmers due to its efficient performance and robust memory safety guarantees. Rust employs an ownership model to ensure these guarantees by allowing each value to be owned by only one identifier at a time. It uses the concept of borrowing and lifetimes to enable other variables to temporarily borrow values. Despite its benefits, security vulnerabilities have been reported in Rust projects, often attributed to the use of 'unsafe' Rust code. These vulnerabilities, in part, arise from incorrect lifetime annotations on function signatures. However, existing tools fail to detect these bugs, primarily because such bugs are rare, challenging to detect through dynamic analysis, and require explicit memory models. To overcome these limitations, we characterize incorrect lifetime annotations as a source of memory safety bugs and leverage this understanding to devise a novel static analysis tool, Yuga, to detect potential lifetime annotation bugs. Yuga uses a multi-phase analysis approach, starting with a quick pattern-matching algorithm to identify potential buggy components and then conducting a flow and field-sensitive alias analysis to confirm the bugs. We also curate new datasets of lifetime annotation bugs. Yuga successfully detects bugs with good precision on these datasets, and we make the code and datasets publicly available. © 1976-2012 IEEE.
Author keywords: lifetimes; Rust; static analysis
Index keywords: C (programming language); Information management; Memory management; Multitasking; Problem oriented languages; Program debugging; Records management; Annotation; Code; Computer bugs; Lifetime; Memory safety; Memory-management; Performance; Rust; Safety guarantees; Security; Static analysis
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85201745129
DOI: 10.1109/tse.2024.3447671
Retrieval channels: authoritative_outlet_search
Local full-text files: 
