---
otero_id: "2-s2.0-85202721596"
title: "Method-Level Test-to-Code Traceability Link Construction by Semantic Correlation Learning"
authors: "Sun W.; Guo Z.; Yan M.; Liu Z.; Lei Y.; Zhang H."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3449917"
---
# Scopus title-abstract-keyword metadata
Title: Method-Level Test-to-Code Traceability Link Construction by Semantic Correlation Learning
Abstract: Test-to-code traceability links (TCTLs) establish links between test artifacts and code artifacts. These links enable developers and testers to quickly identify the specific pieces of code tested by particular test cases, thus facilitating more efficient debugging, regression testing, and maintenance activities. Various approaches, based on distinct concepts, have been proposed to establish method-level TCTLs, specifically linking unit tests to corresponding focal methods. Static methods, such as naming-convention-based methods, use heuristic- and similarity-based strategies. However, such methods face the following challenges: Developers, driven by specific scenarios and development requirements, may deviate from naming conventions, leading to TCTL identification failures. Static methods often overlook the rich semantics embedded within tests, leading to erroneous associations between tests and semantically unrelated code fragments. Although dynamic methods achieve promising results, they require the project to be compilable and the tests to be executable, limiting their usability. This limitation is significant for downstream tasks requiring massive test-code pairs, as not all projects can meet these requirements. To tackle the abovementioned limitations, we propose a novel static method-level TCTL approach, named TestLinker. For the first challenge of existing static approaches, TestLinker introduces a two-phase TCTL framework to accommodate different project types in a triage manner. As for the second challenge, we employ the semantic correlation learning, which learns and establishes the semantic correlations between tests and focal methods based on Pre-trained Code Models (PCMs). TestLinker further establishes mapping rules to accurately link the recommended function name to the concrete production function declaration. Empirical evaluation on a meticulously labeled dataset reveals that TestLinker significantly outperforms traditional static techniques, showing average F1-score improvements ranging from 73.48% to 202.00%. Moreover, compared to state-of-the-art dynamic methods, TestLinker, which only leverages static information, demonstrates comparable or even better performance, with an average F1-score increase of 37.40%. © 1976-2012 IEEE.
Author keywords: pre-trained code model; Software engineering; software testing; traceability
Index keywords: Computer debugging; Computer software maintenance; Computer software selection and evaluation; Embedded software; Error correction; Job analysis; Model checking; Program debugging; Slip forming; Code; Correlation; Phase Change; Pre-trained code model; Software; Software testings; Static method; Task analysis; Traceability; Traceability links; Software testing
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85202721596
DOI: 10.1109/tse.2024.3449917
Retrieval channels: authoritative_outlet_search
Local full-text files: 
