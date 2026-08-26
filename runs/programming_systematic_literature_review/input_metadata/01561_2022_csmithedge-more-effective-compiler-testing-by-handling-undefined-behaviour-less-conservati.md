---
otero_id: "2-s2.0-85133690123"
title: "CsmithEdge: more effective compiler testing by handling undefined behaviour less conservatively"
authors: "Even-Mendoza K.; Cadar C.; Donaldson A.F."
year: "2022"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-022-10146-1"
---
# Scopus title-abstract-keyword metadata
Title: CsmithEdge: more effective compiler testing by handling undefined behaviour less conservatively
Abstract: Compiler fuzzing techniques require a means of generating programs that are free from undefined behaviour (UB) to reliably reveal miscompilation bugs. Existing program generators such as Csmith achieve UB-freedom by heavily restricting the form of generated programs. The idiomatic nature of the resulting programs risks limiting the test coverage they can offer, and thus the compiler bugs they can discover. We investigate the idea of adapting existing fuzzers to be less restrictive concerning UB, in the practical setting of C compiler testing via a new tool, CsmithEdge, which extends Csmith. CsmithEdge probabilistically weakens the constraints used to enforce UB-freedom, thus generated programs are no longer guaranteed to be UB-free. It then employs several off-the-shelf UB detection tools and a novel dynamic analysis to (a) detect cases where the generated program exhibits UB and (b) determine where Csmith has been too conservative in its use of safe math wrappers that guarantee UB-freedom for arithmetic operations, removing the use of redundant ones. The resulting UB-free programs can be used to test for miscompilation bugs via differential testing. The non-UB-free programs can still be used to check that the compiler under test does not crash or hang. Our experiments on recent versions of GCC, LLVM and the Microsoft Visual Studio Compiler show that CsmithEdge was able to discover 7 previously unknown miscompilation bugs (5 already fixed in response to our reports) that could not be found via intensive testing using Csmith, and 2 compiler-hang bugs that were fixed independently shortly before we considered reporting them. © 2022, The Author(s).
Author keywords: Compilers; Csmith; Fuzzing; GCC; LLVM; MSVC
Index keywords: Program compilers; Program debugging; Compiler; Compiler testing; Csmith; Fuzzing; GCC; Idiomatics; LLVM; MSVC; Programme risks; Test-coverage; C (programming language)
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2022
EID: 2-s2.0-85133690123
DOI: 10.1007/s10664-022-10146-1
Retrieval channels: authoritative_outlet_search
Local full-text files: 
