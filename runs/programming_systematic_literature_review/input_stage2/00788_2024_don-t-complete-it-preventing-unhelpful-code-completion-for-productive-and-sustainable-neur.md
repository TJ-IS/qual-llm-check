---
otero_id: "2-s2.0-85213129682"
title: "Don't Complete It! Preventing Unhelpful Code Completion for Productive and Sustainable Neural Code Completion Systems"
authors: "Sun Z.; Du X.; Song F.; Wang S.; Ni M.; Li L.; Lo D."
year: "2024"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3688831"
---
# Scopus title-abstract-keyword metadata
Title: Don't Complete It! Preventing Unhelpful Code Completion for Productive and Sustainable Neural Code Completion Systems
Abstract: Currently, large pre-trained language models are widely applied in neural code completion systems. Though large code models significantly outperform their smaller counterparts, around 70% of displayed code completions from Github Copilot are not accepted by developers. Being reviewed but not accepted, their help to developer productivity is considerably limited and may conversely aggravate the workload of developers, as the code completions are automatically and actively generated in state-of-the-art code completion systems as developers type out once the service is enabled. Even worse, considering the high cost of the large code models, it is a huge waste of computing resources and energy, which severely goes against the sustainable development principle of AI technologies. However, such waste has never been realized, not to mention effectively addressed, in the research community for neural code completion. Hence, preventing such unhelpful code completions from happening in a cost-friendly way is of urgent need. To fill this significant gap, we first investigate the prompts of unhelpful code completions, called "low-return prompts."We empirically identify four observable patterns in low-return prompts, each lacking necessary information, making it difficult to address through enhancements to the model's accuracy alone. This demonstrates the feasibility of identifying such low-return prompts based on the prompts themselves. Motivated by this finding, we propose an early-rejection mechanism to turn down low-return prompts by foretelling the code completion qualities. The prompts that are estimated to receive unhelpful code completions will not be sent to the model. Furthermore, we investigated five types of estimators to demonstrate the feasibility of the mechanism. The experimental results show that the estimator can reject 20% of code completion requests with a 97.4% precision. To the best of our knowledge, it is the first systemic approach to address the problem of unhelpful code completions and this work also sheds light on an important research direction of large code models.  © 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: code completion; deep learning; large language model; productivity
Index keywords: Code completions; Computational costs; Computing resource; Energy; Floating point operations; High costs; Language model; Neural code; Rejection mechanisms; Digital arithmetic
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2024
EID: 2-s2.0-85213129682
DOI: 10.1145/3688831
Retrieval channels: authoritative_outlet_search
Local full-text files: 
