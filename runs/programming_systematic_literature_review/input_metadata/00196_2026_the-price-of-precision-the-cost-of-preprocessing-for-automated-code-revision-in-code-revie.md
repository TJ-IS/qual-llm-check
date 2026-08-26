---
otero_id: "2-s2.0-105024756151"
title: "The price of precision: the cost of preprocessing for automated code revision in code review"
authors: "Pirouzkhah S.; Rani P.; Sovrano F.; Hellendoorn V.; Bacchelli A."
year: "2026"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-025-10781-4"
---
# Scopus title-abstract-keyword metadata
Title: The price of precision: the cost of preprocessing for automated code revision in code review
Abstract: Code review is a widespread practice in software engineering during which developers examine each other’s source code changes to identify potential issues and improve code quality. Among the automated techniques proposed by researchers to reduce the manual workload of code review, Automated Code Revision (ACR) aims to automatically address reviewers’ feedback by producing a revised version of the code. Transformer-based language models have demonstrated state-of-the-art results in ACR. The performance of these models, however, is significantly influenced by the quality and preparation of the training and evaluation data. We present several systematic analyses of prevalent preprocessing steps, examined both cumulatively and in isolation, across three established preprocessing pipelines and two dataset splitting strategies (time-level vs. project-level). Our study spans across models of different scales: OpenNMT (small), T5 and CodeReviewer (mid-sized), LoRA-tuned CodeLLaMA-7B (large), and GPT-3.5-Turbo (large, black-box). Using datasets up to 496k training records, we evaluate and statistically compare models’ performance using exact match ratio (EXM), CodeBLEU, and Levenshtein ratio. Our findings show that preprocessing may be a significant component in the success of the different techniques: OpenNMT relies on heavy preprocessing; T5 benefits from light filtering (selective removal of records); CodeReviewer performs best when trained on larger, less aggressively filtered data; CodeLLaMA-7B and ChatGPT-3.5 Turbo are largely indifferent to preprocessing. Overall, the effectiveness of ACR tools depends on aligning preprocessing with model scale and training setup. In general, small models need abstraction, mid-sized ones benefit from light filtering, and large-scale models perform best when trained on the original, unprocessed form of the code. © The Author(s) 2025.
Author keywords: Automated code review; Code revision; Data; Large language models; Preprocessing
Index keywords: Codes (symbols); Computer programming languages; Computer software selection and evaluation; Large datasets; Automated code; Automated code review; Code review; Code revision; Data; Language model; Large language model; Light filtering; Preprocessing; Source code changes; Automation
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2026
EID: 2-s2.0-105024756151
DOI: 10.1007/s10664-025-10781-4
Retrieval channels: authoritative_outlet_search
Local full-text files: 
