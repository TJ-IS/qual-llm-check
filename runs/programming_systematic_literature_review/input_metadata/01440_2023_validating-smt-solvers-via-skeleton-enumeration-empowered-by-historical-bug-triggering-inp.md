---
otero_id: "2-s2.0-85171799524"
title: "Validating SMT Solvers via Skeleton Enumeration Empowered by Historical Bug-Triggering Inputs"
authors: "Sun M.; Yang Y.; Wen M.; Wang Y.; Zhou Y.; Jin H."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00018"
---
# Scopus title-abstract-keyword metadata
Title: Validating SMT Solvers via Skeleton Enumeration Empowered by Historical Bug-Triggering Inputs
Abstract: SMT solvers check the satisfiability of logic formulas over first-order theories, which have been utilized in a rich number of critical applications, such as software verification, test case generation, and program synthesis. Bugs hidden in SMT solvers would severely mislead those applications and further cause severe consequences. Therefore, ensuring the reliability and robustness of SMT solvers is of critical importance. Although many approaches have been proposed to test SMT solvers, it is still a challenge to discover bugs effectively. To tackle such a challenge, we conduct an empirical study on the historical bug-triggering formulas in SMT solvers' bug tracking systems. We observe that the historical bug-triggering formulas contain valuable skeletons (i.e., core structures of formulas) as well as associated atomic formulas which can cast significant impacts on formulas' ability in triggering bugs. Therefore, we propose a novel approach that utilizes the skeletons extracted from the historical bug-triggering formulas and enumerates atomic formulas under the guidance of association rules derived from historical formulas. In this study, we realized our approach as a practical fuzzing tool HistFuzz and conducted extensive testing on the well-known SMT solvers Z3 and cvc5. To date, HistFuzz has found 111 confirmed new bugs for Z3 and cvc5, of which 108 have been fixed by the developers. More notably, out of the confirmed bugs, 23 are soundness bugs and invalid model bugs found in the solvers' default mode, which are essential for SMT solvers. In addition, our experiments also demonstrate that HistFuzz outperforms the state-of-the-art SMT solver fuzzers in terms of achieved code coverage and effectiveness. © 2023 IEEE.
Author keywords: association rules; bug detection; fuzzing; skeleton enumeration; SMT solver
Index keywords: Air navigation; Application programs; Association rules; Program debugging; Verification; Well testing; Atomic formulae; Bug detection; Critical applications; First order theories; Fuzzing; Logic formulas; Satisfiability; Skeleton enumeration; SMT solv; Software verification; Software testing
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171799524
DOI: 10.1109/icse48619.2023.00018
Retrieval channels: authoritative_outlet_search
Local full-text files: 
