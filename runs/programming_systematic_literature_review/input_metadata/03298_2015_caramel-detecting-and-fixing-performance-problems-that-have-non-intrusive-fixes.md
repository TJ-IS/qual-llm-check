---
otero_id: "2-s2.0-84951840695"
title: "CARAMEL: Detecting and fixing performance problems that have non-intrusive fixes"
authors: "Nistor A.; Chang P.-C.; Radoi C.; Lu S."
year: "2015"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse.2015.100"
---
# Scopus title-abstract-keyword metadata
Title: CARAMEL: Detecting and fixing performance problems that have non-intrusive fixes
Abstract: Performance bugs are programming errors that slow down program execution. While existing techniques can detect various types of performance bugs, a crucial and practical aspect of performance bugs has not received the attention it deserves: how likely are developers to fix a performance bug? In practice, fixing a performance bug can have both benefits and drawbacks, and developers fix a performance bug only when the benefits outweigh the drawbacks. Unfortunately, for many performance bugs, the benefits and drawbacks are difficult to assess accurately. This paper presents CARAMEL, a novel static technique that detects and fixes performance bugs that have non-intrusive fixes likely to be adopted by developers. Each performance bug detected by CARAMEL is associated with a loop and a condition. When the condition becomes true during the loop execution, all the remaining computation performed by the loop is wasted. Developers typically fix such performance bugs because these bugs waste computation in loops and have nonintrusive fixes: when some condition becomes true dynamically, just break out of the loop. Given a program, CARAMEL detects such bugs statically and gives developers a potential sourcelevel fix for each bug. We evaluate CARAMEL on real-world applications, including 11 popular Java applications (e.g., Groovy, Log4J, Lucene, Struts, Tomcat, etc) and 4 widely used C/C++ applications (Chromium, GCC, Mozilla, and MySQL). CARAMEL finds 61 new performance bugs in the Java applications and 89 new performance bugs in the C/C++ applications. Based on our bug reports, developers so far have fixed 51 and 65 performance bugs in the Java and C/C++ applications, respectively. Most of the remaining bugs are still under consideration by developers. © 2015 IEEE.
Author keywords: 
Index keywords: C++ (programming language); Costs; Java programming language; Software engineering; Bug reports; Java applications; Non-intrusive; Performance bugs; Performance problems; Program execution; Programming errors; Static techniques; Program debugging
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2015
EID: 2-s2.0-84951840695
DOI: 10.1109/icse.2015.100
Retrieval channels: authoritative_outlet_search
Local full-text files: 
