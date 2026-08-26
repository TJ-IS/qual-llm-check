---
otero_id: "2-s2.0-85026675138"
title: "Precise condition synthesis for program repair"
authors: "Xiong Y.; Wang J.; Yan R.; Zhang J.; Han S.; Huang G.; Zhang L."
year: "2017"
journal: "Proceedings - 2017 IEEE/ACM 39th International Conference on Software Engineering, ICSE 2017"
doi: "10.1109/icse.2017.45"
---
# Scopus title-abstract-keyword metadata
Title: Precise condition synthesis for program repair
Abstract: Due to the difficulty of repairing defect, many research efforts have been devoted into automatic defect repair. Given a buggy program that fails some test cases, a typical automatic repair technique tries to modify the program to make all tests pass. However, since the test suites in real world projects are usually insufficient, aiming at passing the test suites often leads to incorrect patches. This problem is known as weak test suites or overfitting. In this paper we aim to produce precise patches, that is, any patch we produce has a relatively high probability to be correct. More concretely, we focus on condition synthesis, which was shown to be able to repair more than half of the defects in existing approaches. Our key insight is threefold. First, it is important to know what variables in a local context should be used in an 'if' condition, and we propose a sorting method based on the dependency relations between variables. Second, we observe that the API document can be used to guide the repair process, and propose document analysis technique to further filter the variables. Third, it is important to know what predicates should be performed on the set of variables, and we propose to mine a set of frequently used predicates in similar contexts from existing projects. Based on the insight, we develop a novel program repair system, ACS, that could generate precise conditions at faulty locations. Furthermore, given the generated conditions are very precise, we can perform a repair operation that is previously deemed to be too overfitting: directly returning the test oracle to repair the defect. Using our approach, we successfully repaired 18 defects on four projects of Defects4J, which is the largest number of fully automatically repaired defects reported on the dataset so far. More importantly, the precision of our approach in the evaluation is 78.3%, which is significantly higher than previous approaches, which are usually less than 40%. © 2017 IEEE.
Author keywords: 
Index keywords: Defects; Repair; Software engineering; Dependency relation; Document analysis; Faulty locations; High probability; Real world projects; Repair operations; Repair techniques; Research efforts; Software testing
Document type: Conference paper
Conference: 
Source title: Proceedings - 2017 IEEE/ACM 39th International Conference on Software Engineering, ICSE 2017
Year: 2017
EID: 2-s2.0-85026675138
DOI: 10.1109/icse.2017.45
Retrieval channels: authoritative_outlet_search
Local full-text files: 
