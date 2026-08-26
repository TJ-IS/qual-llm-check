---
otero_id: "2-s2.0-85168628845"
title: "Automating Code-Related Tasks Through Transformers: The Impact of Pre-training"
authors: "Tufano R.; Pascarella L.; Bavota G."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00203"
---
# Scopus title-abstract-keyword metadata
Title: Automating Code-Related Tasks Through Transformers: The Impact of Pre-training
Abstract: Transformers have gained popularity in the software engineering (SE) literature. These deep learning models are usually pre-trained through a self-supervised objective, meant to provide the model with basic knowledge about a language of interest (e.g., Java). A classic pre-training objective is the masked language model (MLM), in which a percentage of tokens from the input (e.g., a Java method) is masked, with the model in charge of predicting them. Once pre-trained, the model is then fine-tuned to support the specific downstream task of interest (e.g., code summarization). While there is evidence suggesting the boost in performance provided by pre-training, little is known about the impact of the specific pre-training objective(s) used. Indeed, MLM is just one of the possible pre-training objectives and recent work from the natural language processing field suggest that pre-training objectives tailored for the specific downstream task of interest may substantially boost the model's performance. For example, in the case of code summarization, a tailored pre-training objective could be the identification of an appropriate name for a given method, considering the method name to generate as an extreme summary. In this study, we focus on the impact of pre-training objectives on the performance of trans-formers when automating code-related tasks. We start with a systematic literature review aimed at identifying the pre-training objectives used in SE. Then, we pre-train 32 transformers using both (i) generic pre-training objectives usually adopted in SE; and (ii) pre-training objectives tailored to specific code-related tasks subject of our experimentation, namely bug-fixing, code summarization, and code completion. We also compare the pre-trained models with non pre-trained ones and show the advantage brought by pre-training in different scenarios, in which more or less fine-tuning data are available. Our results show that: (i) pre-training helps in boosting performance only if the amount of fine-tuning data available is small; (ii) the MLM objective is usually sufficient to maximize the prediction performance of the model, even when comparing it with pre-training objectives specialized for the downstream task at hand. © 2023 IEEE.
Author keywords: Code Recommenders; Pre-training
Index keywords: Codes (symbols); Java programming language; Natural language processing systems; Software engineering; Code recommender; Down-stream; Fine tuning; Java methods; Language model; Language processing; Learning models; Natural languages; Performance; Pre-training; Deep learning
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85168628845
DOI: 10.1109/icse48619.2023.00203
Retrieval channels: authoritative_outlet_search
Local full-text files: 
