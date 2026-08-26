---
otero_id: "2-s2.0-85055881729"
title: "Revisiting supervised and unsupervised models for effort-aware just-in-time defect prediction"
authors: "Huang Q.; Xia X.; Lo D."
year: "2019"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-018-9661-2"
---
# Scopus title-abstract-keyword metadata
Title: Revisiting supervised and unsupervised models for effort-aware just-in-time defect prediction
Abstract: Effort-aware just-in-time (JIT) defect prediction aims at finding more defective software changes with limited code inspection cost. Traditionally, supervised models have been used; however, they require sufficient labelled training data, which is difficult to obtain, especially for new projects. Recently, Yang et al. proposed an unsupervised model (i.e., LT) and applied it to projects with rich historical bug data. Interestingly, they reported that, under the same inspection cost (i.e., 20 percent of the total lines of code modified by all changes), it could find about 12% - 27% more defective changes than a state-of-the-art supervised model (i.e., EALR) when using different evaluation settings. This is surprising as supervised models that benefit from historical data are expected to perform better than unsupervised ones. Their finding suggests that previous studies on defect prediction had made a simple problem too complex. Considering the potential high impact of Yang et al.’s work, in this paper, we perform a replication study and present the following new findings: (1) Under the same inspection budget, LT requires developers to inspect a large number of changes necessitating many more context switches. (2) Although LT finds more defective changes, many highly ranked changes are false alarms. These initial false alarms may negatively impact practitioners’ patience and confidence. (3) LT does not outperform EALR when the harmonic mean of Recall and Precision (i.e., F1-score) is considered. Aside from highlighting the above findings, we propose a simple but improved supervised model called CBS+, which leverages the idea of both EALR and LT. We investigate the performance of CBS+ using three different evaluation settings, including time-wise cross-validation, 10-times 10-fold cross-validation and cross-project validation. When compared with EALR, CBS+ detects about 15% - 26% more defective changes, while keeping the number of context switches and initial false alarms close to those of EALR. When compared with LT, the number of defective changes detected by CBS+ is comparable to LT’s result, while CBS+ significantly reduces context switches and initial false alarms before first success. Finally, we discuss how to balance the tradeoff between the number of inspected defects and context switches, and present the implications of our findings for practitioners and researchers. © 2018, Springer Science+Business Media, LLC, part of Springer Nature.
Author keywords: Defect prediction; Evaluation metrics; Research bias
Index keywords: Alarm systems; Budget control; Codes (symbols); Electric circuit breakers; Errors; Forecasting; Inspection; Just in time production; 10-fold cross-validation; Code inspections; Cross validation; Defect prediction; Evaluation metrics; Inspection costs; Recall and precision; Replication study; Defects
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2019
EID: 2-s2.0-85055881729
DOI: 10.1007/s10664-018-9661-2
Retrieval channels: authoritative_outlet_search
Local full-text files: 
