---
otero_id: "2-s2.0-85193626652"
title: "Spectrum-based rule- and item-level localization of faults in context-free grammars"
authors: "Raselimo M.; Fischer B."
year: "2024"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2024.112067"
---
# Scopus title-abstract-keyword metadata
Title: Spectrum-based rule- and item-level localization of faults in context-free grammars
Abstract: We describe and evaluate spectrum-based methods aimed at finding faults in context-free grammars. In their basic form, they take as input a test suite and a parser for the grammar that is modified to collect grammar spectra (i.e., the sets of grammar elements used in attempts to parse the individual test cases), and return as output a ranked list of suspicious elements. We define grammar spectra suitable for localizing faults on the level of the grammar rules (i.e., rule spectra) and the rules’ individual symbols (i.e., item spectra), respectively. We show how both types of grammar spectra can be collected by both LL and LR parsers, and how the JavaCC, ANTLR, and CUP parser generators can be modified and used to automate the collection of the grammar spectra. We also show how grammar spectra can be synthesized directly from test cases derived from a grammar, and how such synthetic spectra can be used to localize differences between a grammar and a black-box system under test. We first evaluate our approach over a large number of medium-sized single fault grammars, which we constructed by fault seeding from a common origin grammar. At the rule level, it ranks the rules containing the seeded faults within the top five rules in about 40%–70% of the cases, depending on the applied parsing technique, test suite, and ranking metric, and pinpoints them (i.e., correctly identifies them as unique most suspicious rule) in about 10%–30% of the cases, with significantly better results for the synthetic spectra. At the item level, our approach remains remarkably effective despite the larger number of possible locations, provided it is coupled with a simple tie-breaking strategy that prefers items with the right-most designated position over other items from the same rules in a tie. It typically ranks the seeded faults within the top five positions in about 30%–60% of the cases, and pinpoints them in about 15%–40% of the cases. This specialized item-level localization also significantly outperforms a simplistic extension of the rule-level localization, where all positions within a rule are given the same score. We further evaluate our approach over grammars that contain real faults. We show that an iterative method can be used to localize and manually remove one by one multiple faults in grammars submitted by students enrolled in various compiler engineering courses; in most iterations, the top-ranked rule already contains an error, and no error is ranked outside the top five ranked rules. We finally apply our approach to a large open-source SQLite grammar and show where this version deviates from the language accepted by the actual SQLite system. © 2024 The Authors
Author keywords: Grammars and context-free languages; Software testing and debugging
Index keywords: Context free languages; Iterative methods; Program debugging; Software testing; Context-free grammars; Context-free languages; Grammar and context-free language; In contexts; Item-level; Localisation; Software Testing and Debugging; Spectra's; Synthetic spectra; Test case; Context free grammars
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2024
EID: 2-s2.0-85193626652
DOI: 10.1016/j.jss.2024.112067
Retrieval channels: authoritative_outlet_search
Local full-text files: 
