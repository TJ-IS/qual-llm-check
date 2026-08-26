---
otero_id: "2-s2.0-85127050040"
title: "Fuzzing Class Specifications"
authors: "Molina F.; D'Amorim M.; Aguirre N."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510120"
---
# Scopus title-abstract-keyword metadata
Title: Fuzzing Class Specifications
Abstract: Expressing class specifications via executable constraints is important for various software engineering tasks such as test generation, bug finding and automated debugging, but developers rarely write them. Techniques that infer specifications from code exist to fill this gap, but they are designed to support specific kinds of assertions and are difficult to adapt to support different assertion languages, e.g., to add support for quantification, or additional comparison operators, such as membership or containment. To address the above issue, we present SPECFUZZER, a novel technique that combines grammar-based fuzzing, dynamic invariant detection, and mutation analysis, to automatically produce class specifications. SPECFUZZER uses: (i) a fuzzer as a generator of candidate assertions derived from a grammar that is automatically obtained from the class definition; (ii) a dynamic invariant detector -Daikon- to filter out assertions invalidated by a test suite; and (iii) a mutation-based mechanism to cluster and rank assertions, so that similar constraints are grouped and then the stronger prioritized. Grammar-based fuzzing enables SPECFUZZER to be straightforwardly adapted to support different specification languages, by manipulating the fuzzing grammar, e.g., to include additional operators. We evaluate our technique on a benchmark of 43 Java methods employed in the evaluation of the state-of-the-art techniques GAssert and EvoSpex. Our results show that SPECFUZZER can easily support a more expressive assertion language, over which is more effective than GAssert and EvoSpex in inferring specifications, according to standard performance metrics. © 2022 ACM.
Author keywords: grammar-based fuzzing; Oracle problem; specification inference
Index keywords: Program debugging; Software testing; Specification languages; Assertion language; Automated debugging; Bug finding; Comparison operators; Engineering tasks; Executables; Grammar-based fuzzing; Oracle problem; Specification inferences; Test generations; Specifications
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85127050040
DOI: 10.1145/3510003.3510120
Retrieval channels: authoritative_outlet_search
Local full-text files: 
