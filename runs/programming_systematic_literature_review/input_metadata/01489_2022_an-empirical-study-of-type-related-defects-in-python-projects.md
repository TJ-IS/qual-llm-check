---
otero_id: "2-s2.0-85106692319"
title: "An Empirical Study of Type-Related Defects in Python Projects"
authors: "Khan F.; Chen B.; Varro D.; McIntosh S."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2021.3082068"
---
# Scopus title-abstract-keyword metadata
Title: An Empirical Study of Type-Related Defects in Python Projects
Abstract: In recent years, Python has experienced an explosive growth in adoption, particularly among open source projects. While Python's dynamically-typed nature provides developers with powerful programming abstractions, that same dynamic type system allows for type-related defects to accumulate in code bases. To aid in the early detection of type-related defects, type annotations were introduced into the Python ecosystem (i.e., PEP-484) and static type checkers like mypy have appeared on the market. While applying a type checker like mypy can in theory help to catch type-related defects before they impact users, little is known about the real impact of adopting a type checker to reveal defects in Python projects. In this paper, we study the extent to which Python projects benefit from such type checking features. For this purpose, we mine the issue tracking and version control repositories of 210 Python projects on GitHub. Inspired by the work of Gao et al. on type-related defects in JavaScript, we add type annotations to test whether mypy detects an error that would have helped developers to avoid real defects. We observe that 15 percent of the defects could have been prevented by mypy. Moreover, we find that there is no significant difference between the experience level of developers committing type-related defects and the experience of developers committing defects that are not type-related. In addition, a manual analysis of the anti-patterns that most commonly lead to type-checking faults reveals that the redefinition of Python references, dynamic attribute initialization and incorrectly handled Null objects are the most common causes of type-related faults. Since our study is conducted on fixed public defects that have gone through code reviews and multiple test cycles, these results represent a lower bound on the benefits of adopting a type checker. Therefore, we recommend incorporating a static type checker like mypy into the development workflow, as not only will it prevent type-related defects but also mitigate certain anti-patterns during development.  © 1976-2012 IEEE.
Author keywords: dynamic type systems; empirical study; Software defects; static type checkers
Index keywords: High level languages; Open source software; Development workflow; Dynamic attributes; Dynamic type systems; Empirical studies; Explosive growth; Open source projects; Programming abstractions; Type annotations; Defects
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85106692319
DOI: 10.1109/tse.2021.3082068
Retrieval channels: authoritative_outlet_search
Local full-text files: 
