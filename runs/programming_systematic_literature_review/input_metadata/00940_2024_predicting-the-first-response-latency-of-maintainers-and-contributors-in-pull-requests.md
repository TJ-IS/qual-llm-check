---
otero_id: "2-s2.0-85201309320"
title: "Predicting the First Response Latency of Maintainers and Contributors in Pull Requests"
authors: "Khatoonabadi S.; Abdellatif A.; Costa D.E.; Shihab E."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3443741"
---
# Scopus title-abstract-keyword metadata
Title: Predicting the First Response Latency of Maintainers and Contributors in Pull Requests
Abstract: The success of a Pull Request (PR) depends on the responsiveness of the maintainers and the contributor during the review process. Being aware of the expected waiting times can lead to better interactions and managed expectations for both the maintainers and the contributor. In this paper, we propose a machine-learning approach to predict the first response latency of the maintainers following the submission of a PR, and the first response latency of the contributor after receiving the first response from the maintainers. We curate a dataset of 20 large and popular open-source projects on GitHub and extract 21 features to characterize projects, contributors, PRs, and review processes. Using these features, we then evaluate seven types of classifiers to identify the best-performing models. We also conduct permutation feature importance and SHAP analyses to understand the importance and the impact of different features on the predicted response latencies. We find that our CatBoost models are the most effective for predicting the first response latencies of both maintainers and contributors. Compared to a dummy classifier that always returns the majority class, these models achieved an average improvement of 29% in AUC-ROC and 51% in AUC-PR for maintainers, as well as 39% in AUC-ROC and 89% in AUC-PR for contributors across the studied projects. The results indicate that our models can aptly predict the first response latencies using the selected features. We also observe that PRs submitted earlier in the week, containing an average number of commits, and with concise descriptions are more likely to receive faster first responses from the maintainers. Similarly, PRs with a lower first response latency from maintainers, that received the first response of maintainers earlier in the week, and containing an average number of commits tend to receive faster first responses from the contributors. Additionally, contributors with a higher acceptance rate and a history of timely responses in the project are likely to both obtain and provide faster first responses. Moreover, we show the effectiveness of our approach in a cross-project setting. Finally, we discuss key guidelines for maintainers, contributors, and researchers to help facilitate the PR review process.  © 1976-2012 IEEE.
Author keywords: modern code review; open source software; Pull request abandonment; pull-based development; social coding
Index keywords: Open source software; Prediction models; Code review; Features extraction; Machine-learning; Modern code review; Open-source softwares; Predictive models; Pull request abandonment; Pull-based development; Social coding; Software development management; Software design
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85201309320
DOI: 10.1109/tse.2024.3443741
Retrieval channels: authoritative_outlet_search
Local full-text files: 
