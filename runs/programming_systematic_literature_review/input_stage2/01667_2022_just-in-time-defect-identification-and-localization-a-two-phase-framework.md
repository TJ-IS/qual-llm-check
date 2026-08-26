---
otero_id: "2-s2.0-85081388723"
title: "Just-In-Time Defect Identification and Localization: A Two-Phase Framework"
authors: "Yan M.; Xia X.; Fan Y.; Hassan A.E.; Lo D.; Li S."
year: "2022"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2020.2978819"
---
# Scopus title-abstract-keyword metadata
Title: Just-In-Time Defect Identification and Localization: A Two-Phase Framework
Abstract: Defect localization aims to locate buggy program elements (e.g., buggy files, methods or lines of code) based on defect symptoms, e.g., bug reports or program spectrum. However, when we receive the defect symptoms, the defect has been exposed and negative impacts have been introduced. Thus, one challenging task is: whether we can locate buggy program prior to the appearance of the defect symptom (e.g., when buggy program elements are being committed to a version control system). We refer to this type of defect localization as 'Just-In-Time (JIT) Defect localization'. Although many prior studies have proposed various JIT defect identification methods to identify whether a new change is buggy, these prior methods do not locate the suspicious positions. Thus, JIT defect localization is the next step of JIT defect identification (i.e., after a buggy change is identified, suspicious source code lines are located). To address this problem, we propose a two-phase framework, i.e., JIT defect identification and JIT defect localization. Given a new change, JIT defect identification will identify it as buggy change or clean change first. If a new change is identified as buggy, JIT defect localization will rank the source code lines introduced by the new change according to their suspiciousness scores. The source code lines ranked at the top of the list are estimated as the defect location. For JIT defect identification phase, we use 14 change-level features to build a classifier by following existing approach. For JIT defect localization phase, we propose a JIT defect localization approach that leverages software naturalness with the N-gram model. To evaluate the proposed framework, we conduct an empirical study on 14 open source projects with a total of 177,250 changes. The results show that software naturalness is effective for our JIT defect localization. Our model achieves a reasonable performance, and outperforms the two baselines (i.e., random guess and a static bug finder (i.e., PMD)) by a substantial margin in terms of four ranking measures. © 1976-2012 IEEE.
Author keywords: defect identification; Defect localization; just-in-time; software naturalness
Index keywords: Codes (symbols); Computer programming languages; Computer science; Computer software; Fans; History; Job analysis; Just in time production; Open source software; Program debugging; Computer bugs; Defect identification; Defect localizations; Just in time; Task analysis; Defects
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2022
EID: 2-s2.0-85081388723
DOI: 10.1109/tse.2020.2978819
Retrieval channels: authoritative_outlet_search
Local full-text files: 
