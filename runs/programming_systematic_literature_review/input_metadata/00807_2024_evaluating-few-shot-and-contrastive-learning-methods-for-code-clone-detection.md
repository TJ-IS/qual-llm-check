---
otero_id: "2-s2.0-85206261755"
title: "Evaluating few-shot and contrastive learning methods for code clone detection"
authors: "Khajezade M.; Fard F.H.; Shehata M.S."
year: "2024"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-024-10441-z"
---
# Scopus title-abstract-keyword metadata
Title: Evaluating few-shot and contrastive learning methods for code clone detection
Abstract: Context: Code Clone Detection (CCD) is a software engineering task that is used for plagiarism detection, code search, and code comprehension. Recently, deep learning-based models have achieved an F1-Score (a metric used to assess classifiers) of ∼95% on the CodeXGLUE benchmark. These models require many training data, mainly fine-tuned on Java or C++ datasets. However, no previous study evaluates the generalizability of these models where a limited amount of annotated data is available. Objective: The main objective of this research is to assess the ability of the CCD models as well as few-shot learning algorithms for unseen programming problems and new languages (i.e., the model is not trained on these problems/languages). Method: We assess the generalizability of the state-of-the-art models for CCD in few-shot settings (i.e., only a few samples are available for fine-tuning) by setting three scenarios: i) unseen problems, ii) unseen languages, iii) combination of new languages and new problems. We choose CodeNet and conduct our experiments on Java, C++, and Ruby languages. Then, we employ Model Agnostic Meta-learning (MAML), where the model learns a meta-learner capable of extracting transferable knowledge from the train set; so that the model can be fine-tuned using a few samples. Finally, we combine contrastive learning with MAML to further study whether it can improve the results of MAML. Results: Our results show that the performance of the models drops ∼50% for Java and ∼20% for C++ and Ruby for unseen problems, which are then boosted by 13% to 24% F1 scores for Java and C++/Ruby, respectively when MAML is used. Similar observations are found for unseen languages and the third scenario. Though in case of third scenario (i.e., unseen problems and unseen languages) the scores are lower. Integrating contrastive learning with MAML did not help in boosting the performance more than what we could achieve with MAML. Our results open new avenues of research and the need to develop robust models for clone detection, in the settings we investigated here. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.
Author keywords: Code clone detection; Contrastive learning; Few-shot learning
Index keywords: Adaptive boosting; Benchmarking; C++ (programming language); Java programming language; Network security; Problem oriented languages; Code clone detection; Code search; Detection codes; Engineering tasks; F1 scores; Few-shot learning; Learning methods; Metalearning; Performance; Plagiarism detection; Ruby
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2024
EID: 2-s2.0-85206261755
DOI: 10.1007/s10664-024-10441-z
Retrieval channels: authoritative_outlet_search
Local full-text files: 
