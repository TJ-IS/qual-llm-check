---
otero_id: "2-s2.0-105010305410"
title: "Template-Guided Program Repair in the Era of Large Language Models"
authors: "Huang K.; Zhang J.; Meng X.; Liu Y."
year: "2025"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse55347.2025.00030"
---
# Scopus title-abstract-keyword metadata
Title: Template-Guided Program Repair in the Era of Large Language Models
Abstract: Recent advancements in automated program repair (APR) have been significantly driven by the application of Large Language Models (LLMs). In particular, the integration of LLMs with traditional template-based repair methods has demonstrated effective outcomes. Despite this, the synergy between the strengths of traditional methods and LLMs remains underexploited. This oversight originates from the indiscriminate use of templates and their insufficient coverage. Also, using small-scale LLMs within the zero-shot learning context proves to be suboptimal. To alleviate the limitations, we propose NTR (Neural Template Repair), a two-stage repair framework including template selection and patch generation, both of which are under the fine-tuning paradigm. In the template selection phase, we formulate it as a multiclass classification problem and fine-tune million-level LLMs for better selecting possible templates. During the patch generation phase, we leverage the chosen templates as probable directions (e.g., 'Mutate Conditional Expression') to guide the fine-tuning process of LLMs at the billion-level scale for precise patch creation. Moreover, we incorporate a unique template to signify the absence of a suitable template and employ a probability-based prioritization of templates, thereby optimizing patch generation. This framework not only effectively addresses template mismatch issues, but also enables the billion-level LLMs to explore the patch space more efficiently, despite the GPU memory constraints. We evaluate NTR with different foundational models on Defects4J V1.2 and HumanEval-Java, the framework consistently demonstrates significant effectiveness. When utilizing StarCoder as the foundational model for patch generation, NTR fixes 128 and 129 bugs in Defects4J and HumanEval, outperforming the best baseline APR tool by 14 and 59 bugs. With the larger CodeLlama model, the fixed bugs rise to 139 and 136, respectively, exceeding the baseline by 25 and 66 bugs. Notably, the performance stems not only from the foundational models but also benefits greatly from our NTR framework. Specifically, NTR's implementation with StarCoder and CodeLlama leads to 22 and 23 additional fixes, which is beyond what the models achieve on their own. This emphasizes the success of our new perspective on utilizing templates to unlock the bug-fixing potential of LLMs.  © 2025 IEEE.
Author keywords: Automated Program Repair; Fine-Tuning; Large Language Models; Repair Template
Index keywords: Artificial intelligence; Automation; Defects; Industrial plants; Template matching; Tuning; Automated program repair; Fine tuning; Language model; Large language model; Neural templates; Repair methods; Repair template; Small scale; Template selection; Template-based; Application programs; Repair
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2025
EID: 2-s2.0-105010305410
DOI: 10.1109/icse55347.2025.00030
Retrieval channels: authoritative_outlet_search
Local full-text files: 
