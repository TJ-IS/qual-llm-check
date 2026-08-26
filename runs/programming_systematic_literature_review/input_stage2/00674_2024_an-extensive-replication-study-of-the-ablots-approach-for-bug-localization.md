---
otero_id: "2-s2.0-85201937648"
title: "An extensive replication study of the ABLoTS approach for bug localization"
authors: "Niu F.; Zhang E.; Mayr-Dorn C.; Assunção W.K.G.; Huang L.; Ge J.; Luo B.; Egyed A."
year: "2024"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-024-10537-6"
---
# Scopus title-abstract-keyword metadata
Title: An extensive replication study of the ABLoTS approach for bug localization
Abstract: Bug localization is the task of recommending source code locations (typically files) that contain the cause of a bug and hence need to be changed to fix the bug. Along these lines, information retrieval-based bug localization (IRBL) approaches have been adopted, which identify the most bug-prone files from the source code space. In current practice, a series of state-of-the-art IRBL techniques leverage the combination of different components (e.g., similar reports, version history, and code structure) to achieve better performance. ABLoTS is a recently proposed approach with the core component, TraceScore, that utilizes requirements and traceability information between different issue reports (i.e., feature requests and bug reports) to identify buggy source code snippets with promising results. To evaluate the accuracy of these results and obtain additional insights into the practical applicability of ABLoTS, we conducted a replication study of this approach with the original dataset and also on two extended datasets (i.e., additional Java dataset and Python dataset). The original dataset consists of 11 open source Java projects with 8,494 bug reports. The extended Java dataset includes 16 more projects comprising 25,893 bug reports and corresponding source code commits. The extended Python dataset consists of 12 projects with 1,289 bug reports. While we find that the TraceScore component, which is the core of ABLoTS, produces comparable or even better results with the extended datasets, we also find that we cannot reproduce the ABLoTS results, as reported in its original paper, due to an overlooked side effect of incorrectly choosing a cut-off date that led to test data leaking into training data with significant effects on performance. Additionally, we conduct experiments to assess the performance of various composers that aggregate scores from different components, revealing that Logistic Regression, fixed weight, and CombSUM outperform the other composers across all three datasets, while decision tree and random forest exhibited subpar performance. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.
Author keywords: Bug localization; Composer; Information retrieval; Replication study
Index keywords: Information leakage; Java programming language; Logistic regression; Metadata; Network security; Program debugging; Python; Recommender systems; Bug localizations; Bug reports; Code space; Composer; Current practices; Localization technique; Performance; Replication study; Source codes; State of the art; Decision trees
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2024
EID: 2-s2.0-85201937648
DOI: 10.1007/s10664-024-10537-6
Retrieval channels: authoritative_outlet_search
Local full-text files: 
