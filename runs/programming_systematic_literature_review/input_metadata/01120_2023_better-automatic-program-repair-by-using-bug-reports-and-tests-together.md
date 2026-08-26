---
otero_id: "2-s2.0-85150600616"
title: "Better Automatic Program Repair by Using Bug Reports and Tests Together"
authors: "Motwani M.; Brun Y."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00109"
---
# Scopus title-abstract-keyword metadata
Title: Better Automatic Program Repair by Using Bug Reports and Tests Together
Abstract: Automated program repair is already deployed in industry, but concerns remain about repair quality. Recent research has shown that one of the main reasons repair tools produce incorrect (but seemingly correct) patches is imperfect fault localization (FL). This paper demonstrates that combining information from natural-language bug reports and test executions when localizing faults can have a significant positive impact on repair quality. For example, existing repair tools with such FL are able to correctly repair 7 defects in the Defects4J benchmark that no prior tools have repaired correctly. We develop, Blues, the first information-retrieval-based, statement-level FL technique that requires no training data. We further develop RAFL, the first unsupervised method for combining multiple FL techniques, which outperforms a supervised method. Using RAFL, we create SBIR by combining Blues with a spectrum-based (SBFL) technique. Evaluated on 815 real-world defects, SBIR consistently ranks buggy statements higher than its underlying techniques. We then modify three state-of-the-art repair tools, Arja, SequenceR, and SimFix, to use SBIR, SBFL, and Blues as their internal FL. We evaluate the quality of the produced patches on 689 real-world defects. Arja and SequenceR significantly benefit from SBIR: Arja using SBIR correctly repairs 28 defects, but only 21 using SBFL, and only 15 using Blues; SequenceR using SBIR correctly repairs 12 defects, but only 10 using SBFL, and only 4 using Blues. SimFix, (which has internal mechanisms to overcome poor FL), correctly repairs 30 defects using SBIR and SBFL, but only 13 using Blues. Our work is the first investigation of simultaneously using multiple software artifacts for automated program repair, and our promising findings suggest future research in this directions is likely to be fruitful. © 2023 IEEE.
Author keywords: Automatic Program repair; Debugging; fault localization; Information retrieval based fault localization
Index keywords: Defects; Program debugging; Quality control; Software testing; Automatic program repair; Automatic programs; Bug reports; Debugging; Fault localization; Information retrieval based fault localization; Localization technique; Real-world; Repair tools; Information retrieval
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85150600616
DOI: 10.1109/icse48619.2023.00109
Retrieval channels: authoritative_outlet_search
Local full-text files: 
