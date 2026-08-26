---
otero_id: "2-s2.0-85178655672"
title: "APR4Vul: an empirical study of automatic program repair techniques on real-world Java vulnerabilities"
authors: "Bui Q.-C.; Paramitha R.; Vu D.-L.; Massacci F.; Scandariato R."
year: "2024"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-023-10415-7"
---
# Scopus title-abstract-keyword metadata
Title: APR4Vul: an empirical study of automatic program repair techniques on real-world Java vulnerabilities
Abstract: Security vulnerability fixes could be a promising research avenue for Automated Program Repair (APR) techniques. In recent years, APR tools have been thoroughly developed for fixing generic bugs. However, the area is still relatively unexplored when it comes to fixing security bugs or vulnerabilities. In this paper, we evaluate nine state-of-the-art APR tools and one vulnerability-specific repair tool. In particular, we investigate their ability to generate patches for 79 real-world Java vulnerabilities in the Vul4J dataset, as well as the level of trustworthiness of these patches. We evaluate the tools with respect to their ability to generate security patches that are (i) testable, (ii) having the positive effect of closing the vulnerability, and (iii) not having side effects from a functional point of view. Our results show that the evaluated APR tools were able to generate testable patches for around 20% of the considered vulnerabilities. On average, nearly 73% of the testable patches indeed eliminate the vulnerabilities, but only 44% of them could actually fix security bugs while maintaining the functionalities. To understand the root cause of this phenomenon, we conduct a detailed comparative study of the general bug fix patterns in Defect4J and the vulnerability fix patterns in ExtraVul (which we extend from Vul4J). Our investigation shows that, although security patches are short in terms of lines of code, they contain unique characteristics in their fix patterns compared to general bugs. For example, many security fixes require adding method calls. These method calls contain specific input validation-related keywords, such as encode, normalize, and trim. In this regard, our study suggests that additional repair patterns should be implemented for existing APR tools to fix more types of security vulnerabilities. © 2023, The Author(s).
Author keywords: Automated program repair; Empirical experiments; Java; Vulnerability
Index keywords: Computer software; Java programming language; Network security; Program debugging; Automated program repair; Empirical experiments; Java; Real-world; Repair techniques; Repair tools; Security bugs; Security patches; Security vulnerabilities; Vulnerability; Repair
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2024
EID: 2-s2.0-85178655672
DOI: 10.1007/s10664-023-10415-7
Retrieval channels: authoritative_outlet_search
Local full-text files: 
