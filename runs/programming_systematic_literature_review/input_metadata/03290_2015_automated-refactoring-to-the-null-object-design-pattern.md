---
otero_id: "2-s2.0-84921033188"
title: "Automated refactoring to the Null Object design pattern"
authors: "Gaitani M.A.G.; Zafeiris V.E.; Diamantidis N.A.; Giakoumakis E.A."
year: "2015"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2014.10.010"
---
# Scopus title-abstract-keyword metadata
Title: Automated refactoring to the Null Object design pattern
Abstract: Context Null-checking conditionals are a straightforward solution against null dereferences. However, their frequent repetition is considered a sign of poor program design, since they introduce source code duplication and complexity that impacts code comprehension and maintenance. The Null Object design pattern enables the replacement of null-checking conditionals with polymorphic method invocations that are bound, at runtime, to either a real object or a Null Object. Objective This work proposes a novel method for automated refactoring to Null Object that eliminates null-checking conditionals associated with optional class fields, i.e., fields that are not initialized in all class instantiations and, thus, their usage needs to be guarded in order to avoid null dereferences. Method We introduce an algorithm for automated discovery of refactoring opportunities to Null Object. Moreover, we specify the source code transformation procedure and an extensive set of refactoring preconditions for safely refactoring an optional field and its associated null-checking conditionals to the Null Object design pattern. The method is implemented as an Eclipse plug-in and is evaluated on a set of open source Java projects. Results Several refactoring candidates are discovered in the projects used in the evaluation and their refactoring lead to improvement of the cyclomatic complexity of the affected classes. The successful execution of the projects' test suites, on their refactored versions, provides empirical evidence on the soundness of the proposed source code transformation. Runtime performance results highlight the potential for applying our method to a wide range of project sizes. Conclusion Our method automates the elimination of null-checking conditionals through refactoring to the Null Object design pattern. It contributes to improvement of the cyclomatic complexity of classes with optional fields. The runtime processing overhead of applying our method is limited and allows its integration to the programmer's routine code analysis activities. © 2014 Elsevier B.V. All rights reserved.
Author keywords: Design patterns; Null checks; Null Object; Optional fields; Refactoring
Index keywords: Automation; Computer programming languages; Cosine transforms; Design Patterns; Null checks; Null Object; Optional fields; Refactorings; Open source software
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2015
EID: 2-s2.0-84921033188
DOI: 10.1016/j.infsof.2014.10.010
Retrieval channels: authoritative_outlet_search
Local full-text files: 
