---
otero_id: "2-s2.0-85121780691"
title: "Deep Just-In-Time Defect Localization"
authors: "Qiu F.; Gao Z.; Xia X.; Lo D.; Grundy J.; Wang X."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2021.3135875"
---
# Scopus title-abstract-keyword metadata
Title: Deep Just-In-Time Defect Localization
Abstract: During software development and maintenance, defect localization is an essential part of software quality assurance. Even though different techniques have been proposed for defect localization, i.e., information retrieval (IR)-based techniques and spectrum-based techniques, they can only work after the defect has been exposed, which can be too late and costly to adapt to the newly introduced bugs in the daily development. There are also many JIT defect prediction tools that have been proposed to predict the buggy commit. But these tools do not locate the suspicious buggy positions in the buggy commit. To assist developers to detect bugs in time and avoid introducing them, just-in-time (JIT) bug localization techniques have been proposed, which is targeting to locate suspicious buggy code after a change commit has been submitted. In this paper, we propose a novel JIT defect localization approach, named DeepDL (Deep Learning-based defect localization), to locate defect code lines within a defect introducing change. DeepDL employs a neural language model to capture the semantics of the code lines, in this way, the naturalness of each code line can be learned and converted to a suspiciousness score. The core of our DeepDL is a deep learning-based neural language model. We train the neural language model with previous snapshots (history versions) of a project so that it can calculate the naturalness of a piece of code. In its application, for a given new code change, DeepDL automatically assigns a suspiciousness score to each code line and sorts these code lines in descending order of this score. The code lines at the top of the list are considered as potential defect locations. Our tool can assist developers efficiently check buggy lines at an early stage, which is able to reduce the risk of introducing bugs in time and improve the developers' confidence in the reliability of their software. We conducted an extensive experiment on 14 open source Java projects with a total of 11,615 buggy changes. We evaluate the experimental results considering four evaluation metrics. The experimental results show that our method outperforms the state-of-the-art by a substantial margin.  © 1976-2012 IEEE.
Author keywords: deep learning; Defect localization; just-in-time; software naturalness
Index keywords: Codes (symbols); Computational linguistics; Computer software selection and evaluation; Deep learning; Defects; Open source software; Program debugging; Software design; Software reliability; Systematic errors; Code; Code line; Computer bugs; Context models; Defect localizations; Just-in-time; Language model; Location awareness; Software; Task analysis; Semantics
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85121780691
DOI: 10.1109/tse.2021.3135875
Retrieval channels: authoritative_outlet_search
Local full-text files: 
