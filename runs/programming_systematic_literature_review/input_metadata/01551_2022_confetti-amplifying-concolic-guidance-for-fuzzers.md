---
otero_id: "2-s2.0-85133504059"
title: "CONFETTI: Amplifying Concolic Guidance for Fuzzers"
authors: "Kukucka J.; Pina L.; Ammann P.; Bell J."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3510003.3510628"
---
# Scopus title-abstract-keyword metadata
Title: CONFETTI: Amplifying Concolic Guidance for Fuzzers
Abstract: Fuzz testing (fuzzing) allows developers to detect bugs and vul-nerabilities in code by automatically generating defect-revealing inputs. Most fuzzers operate by generating inputs for applications and mutating the bytes of those inputs, guiding the fuzzing pro-cess with branch coverage feedback via instrumentation. Whitebox guidance (e.g., taint tracking or concolic execution) is sometimes in-tegrated with coverage-guided fuzzing to help cover tricky-to-reach branches that are guarded by complex conditions (so-called 'magic values'). This integration typically takes the form of a targeted in-put mutation, e.g., placing particular byte values at a specific offset of some input in order to cover a branch. However, these dynamic analysis techniques are not perfect in practice, which can result in the loss of important relationships between input bytes and branch predicates, thus reducing the effective power of the technique. We introduce a new, surprisingly simple, but effective technique, global hinting, which allows the fuzzer to insert these interesting bytes not only at a targeted position, but in any position of any input. We implemented this idea in Java, creating Confetti, which uses both targeted and global hints for fuzzing. In an empirical com-parison with two baseline approaches, a state-of-the-art greybox Java fuzzer and a version of Confetti without global hinting, we found that Confetti covers more branches and finds 15 previously unreported bugs, including 9 that neither baseline could find. By conducting a post-mortem analysis of Confetti's execution, we determined that global hinting was at least as effective at revealing new coverage as traditional, targeted hinting. © 2022 ACM.
Author keywords: concolic execution; fuzz testing; taint tracking
Index keywords: Program debugging; Branch-coverage; Complex condition; Concolic execution; Dynamic analysis techniques; Effective power; Fuzz Testing; Grey-box; Simple++; State of the art; Taint tracking; Java programming language
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85133504059
DOI: 10.1145/3510003.3510628
Retrieval channels: authoritative_outlet_search
Local full-text files: 
