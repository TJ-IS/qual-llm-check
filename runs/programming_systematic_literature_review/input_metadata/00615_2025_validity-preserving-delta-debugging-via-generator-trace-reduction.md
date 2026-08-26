---
otero_id: "2-s2.0-86000588099"
title: "Validity-Preserving Delta Debugging via Generator Trace Reduction"
authors: "Ren L.; Zhang X.; Hua Z.; Jiang Y.; He X.; Xiong Y.; Xie T."
year: "2025"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3705305"
---
# Scopus title-abstract-keyword metadata
Title: Validity-Preserving Delta Debugging via Generator Trace Reduction
Abstract: Reducing test inputs that trigger bugs is crucial for efficient debugging. Delta debugging is the most popular approach for this purpose. When test inputs need to conform to certain specifications, existing delta debugging practice encounters a validity problem: it blindly applies reduction rules, producing a large number of invalid test inputs that do not satisfy the required specifications. This overall diminishing effectiveness and efficiency becomes even more pronounced when the specifications extend beyond syntactical structures. Our key insight is that we should leverage input generators, which are aware of these specifications, to generate valid reduced inputs, rather than straightforwardly performing reduction on test inputs. In this article, we propose a generator-based delta debugging method, namely GReduce, which derives validity-preserving reducers. Specifically, given a generator and its execution, demonstrating how the bug-inducing test input is generated, GReduce searches for other executions on the generator that yield reduced, valid test inputs. The evaluation results on five benchmarks (i.e., graphs, DL models, JavaScript programs, SymPy, and algebraic data types) show that GReduce substantially outperforms state-of-the-art syntax-based reducers including Perses and T-PDD, and also outperforms QuickCheck, SmartCheck, as well as the state-of-the-art choice-sequence-based reducer Hypothesis, demonstrating the effectiveness, efficiency, and versatility of GReduce.  © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: delta debugging; generator-based testing; software debugging
Index keywords: Benchmarking; Computer debugging; Computer software selection and evaluation; Input output programs; Program debugging; Syntactics; % reductions; Delta debugging; Effectiveness and efficiencies; Generator-based testing; Reduced inputs; Reduction rules; Software debugging; State of the art; Syntactical structures; Test inputs; Software testing
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2025
EID: 2-s2.0-86000588099
DOI: 10.1145/3705305
Retrieval channels: authoritative_outlet_search
Local full-text files: 
