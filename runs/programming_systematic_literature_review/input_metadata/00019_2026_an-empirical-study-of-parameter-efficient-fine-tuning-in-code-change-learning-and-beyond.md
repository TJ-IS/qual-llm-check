---
otero_id: "2-s2.0-105023569063"
title: "An Empirical Study of Parameter-Efficient Fine-Tuning in Code Change Learning and Beyond"
authors: "Liu S.; Keung J.; Jin Z.; Yang Z.; Liu F.; Zhang H."
year: "2026"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2025.3637335"
---
# Scopus title-abstract-keyword metadata
Title: An Empirical Study of Parameter-Efficient Fine-Tuning in Code Change Learning and Beyond
Abstract: Compared to Full-Model Fine-Tuning (FMFT), Parameter-Efficient Fine-Tuning (PEFT) has demonstrated superior efficacy and efficiency in several code understanding tasks, owing to PEFT’s ability to alleviate the catastrophic forgetting issue of Pre-trained Language Models (PLMs) by updating only a small number of parameters. However, existing studies primarily involve static code comprehension, aligning with the pre-training paradigm of recent PLMs and facilitating knowledge transfer, but they do not account for dynamic code changes. Thus, it remains unclear whether PEFT outperforms FMFT in task-specific adaptation for code-change-related tasks. To address this question, we examine four prevalent PEFT methods (i.e., AT, LoRA, PT, and PreT) and compare their performance with FMFT across seven popular PLMs. In experiments, two widely studied code-change-related tasks, i.e., Just-In-Time Defect Prediction (JIT-DP) and Commit Message Generation (CMG) are involved, demonstrating that the four PEFT methods can surpass FMFT on JIT-DP but only exhibit comparable performances at best on CMG in common scenarios. While in cross-lingual and low-resource scenarios, they exhibit relative superiority. Afterward, a series of probing tasks from both static and dynamic perspectives are conducted in this paper, offering detailed explanations for the efficacy of PEFT and FMFT. Inspired by the distinctive advantages of PEFT and FMFT in their layer-wise probing results, we propose PastaK , a self-adaPtive efficient layer-specific tuning framework for PLMs in code change learning, which combines FMFT and PEFT during the domain adaptation according to the guidance of probing results. Experiments in the CMG task demonstrate that PastaK surpasses diverse PEFT methods in effectiveness. Even, PastaK outperforms FMFT by 1.48%, 3.21%, and 1.87% at most in terms of BLEU, Meteor, and Rouge-L, while saving 26.26% and 20.65% in terms of training time and computational memory compared with FMFT. © 1976-2012 IEEE.
Author keywords: Adapter tuning; CodeBERT; CodeT5; CodeT5+; commit message generation; GraphCodeBERT; just-in-time defect prediction; low-rank adaptation; PLBART; prefix tuning; prompt tuning; Qwen2.5-Coder; UniXcoder
Index keywords: Defects; Errors; Knowledge management; Knowledge transfer; Learning systems; Learning to rank; Modeling languages; Praseodymium compounds; Tuning; AT; CodeBERT; Codet5; Codet5+; Commit message generation; Defect prediction; Graphcodebert; Just-in-time; Just-in-time defect prediction; Low-rank adaptation; PLBART; Pret; PT; Qwen2.5-coder; Unixcoder; Codes (symbols)
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2026
EID: 2-s2.0-105023569063
DOI: 10.1109/tse.2025.3637335
Retrieval channels: authoritative_outlet_search
Local full-text files: 
