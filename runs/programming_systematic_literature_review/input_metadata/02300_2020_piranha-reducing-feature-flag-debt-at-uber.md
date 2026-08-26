---
otero_id: "2-s2.0-85092548989"
title: "Piranha: Reducing feature flag debt at Uber"
authors: "Ramanathan M.K.; Clapp L.; Barik R.; Sridharan M."
year: "2020"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3377813.3381350"
---
# Scopus title-abstract-keyword metadata
Title: Piranha: Reducing feature flag debt at Uber
Abstract: Feature flags are commonly used in mobile app development and can introduce technical debt related to deleting their usage from the codebase. This can adversely affect the overall reliability of the apps and increase their maintenance complexity. Reducing this debt without imposing additional overheads on the developers necessitates the design of novel tools and automated workflows. In this paper, we describe the design and implementation of Piranha, an automated code refactoring tool which is used to automatically generate differential revisions (a.k.a diffs) to delete code corresponding to stale feature flags. Piranha takes as input the name of the flag, expected treatment behavior, and the name of the flag's author. It analyzes the ASTs of the program to generate appropriate refactorings which are packaged into a diff. The diff is assigned to the author of the flag for further processing, who can land it after performing any additional refactorings. We have implemented Piranha to delete code in Objective-C, Java, and Swift programs, and deployed it to handle stale flags in multiple Uber apps. We present our experiences with the deployment of Piranha from Dec 2017 to May 2019, including the following highlights: (a) generated code cleanup diffs for 1381 flags (17% of total flags), (b) 65% of the diffs landed without any changes, (c) over 85% of the generated diffs compile and pass tests successfully, (d) around 80% of the diffs affect more than one file, (e) developers process more than 88% of the generated diffs, (f) 75% of the generated diffs are processed within a week, and (g) Piranha diffs have been interacted with by ∼200 developers across Uber. Piranha is available as open source at https://github.com/uber/ piranha. © 2020 IEEE Computer Society. All rights reserved.
Author keywords: 
Index keywords: Open source software; Automated code; Design and implementations; Mobile app; Open sources; Refactorings; Technical debts; Work-flows; Codes (symbols)
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2020
EID: 2-s2.0-85092548989
DOI: 10.1145/3377813.3381350
Retrieval channels: authoritative_outlet_search
Local full-text files: 
