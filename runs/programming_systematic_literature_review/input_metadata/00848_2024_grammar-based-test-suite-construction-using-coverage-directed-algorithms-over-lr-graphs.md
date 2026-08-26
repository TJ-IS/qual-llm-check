---
otero_id: "2-s2.0-85192185778"
title: "Grammar-based test suite construction using coverage-directed algorithms over LR-graphs"
authors: "Rossouw C.; Fischer B."
year: "2024"
journal: "Journal of Systems and Software"
doi: "10.1016/j.jss.2024.112068"
---
# Scopus title-abstract-keyword metadata
Title: Grammar-based test suite construction using coverage-directed algorithms over LR-graphs
Abstract: In grammar-based testing, the test suites that drive the system under test are typically constructed from a given context-free grammar through a set of derivations that jointly satisfy some coverage criterion. In this paper, we describe and evaluate a new algorithm that instead constructs test suites from a set of valid paths that cover all edges in a labeled directed graph corresponding to an LR-automaton that accepts the language of the grammar. Vertices in this graph correspond to states in the LR-automaton; two vertices are connected by an edge iff the top of the LR-automaton's stack can change from one state to the other, either by shifting a terminal or non-terminal symbol (push edges), or by reducing with a grammar rule (pop edges). The algorithm constructs a unique reduction path for each pop edge in the graph. These reduction paths are recursively embedded into each other, and any unresolved non-terminal push edges are substituted by shortest derivations for the non-terminal symbol. The algorithm can work with different types of LR-automata, including LR(0)- and LR(1)-automata, and can successfully generate a test suite from an LR-graph even if the underlying LR-automaton construction leads to shift/reduce or reduce/reduce conflicts. The algorithm only constructs valid paths over the LR-graphs that correspond to sentences in the language and thus generates only positive tests. We therefore also describe mutations to the positive paths that are guaranteed to generate negative tests without needing any further verification by an oracle. Our algorithm is substantially more efficient than an earlier algorithm that explores LR-graphs with two consecutive breadth-first graph traversals and our experimental evaluation shows that it scales to large production-quality grammars. It is robust against random choices made to resolve ambiguity in the construction of the tests, while the code coverage of the different test suite variants is relatively uniform. Finally, our evaluation shows that the negative test suites constructed by path mutation identify more faults in a set of student grammars than those constructed by rule mutation. © 2024 The Author(s)
Author keywords: Grammars and context-free languages; Push-down automata; Software testing and debugging; Test case generation
Index keywords: Automata theory; Context free grammars; Context free languages; Directed graphs; Program debugging; Software testing; % reductions; Context-free languages; Grammar and context-free language; Grammar-based testing; Non-terminal symbols; Push-down automata; Software Testing and Debugging; Systems under tests; Test case generation; Valid paths; Quality control
Document type: Article
Conference: 
Source title: Journal of Systems and Software
Year: 2024
EID: 2-s2.0-85192185778
DOI: 10.1016/j.jss.2024.112068
Retrieval channels: authoritative_outlet_search
Local full-text files: 
