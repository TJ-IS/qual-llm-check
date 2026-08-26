---
otero_id: "2-s2.0-85210080717"
title: "Deep learning based identification of inconsistent method names: How far are we?"
authors: "Wang T.; Zhang Y.; Jiang L.; Tang Y.; Li G.; Liu H."
year: "2025"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-024-10592-z"
---
# Scopus title-abstract-keyword metadata
Title: Deep learning based identification of inconsistent method names: How far are we?
Abstract: For any software system, concise and meaningful method names are critical for program comprehension and maintenance. However, for various reasons, the method names might be inconsistent with their corresponding implementations. Such inconsistent method names are confusing and misleading, often resulting in incorrect method invocations. To this end, a few intelligent deep learning-based approaches based on neural networks have been proposed to identify such inconsistent method names in the industry. Existing evaluations suggest that the performance of such DL-based approaches is promising. However, the evaluations are conducted with a perfectly balanced dataset where the number of inconsistent method names is exactly equivalent to that of consistent ones. In addition, the construction method of this balanced dataset is flawed, leading to false positives in this dataset. Consequently, the reported performance may not represent their efficiency in the field where most method names are consistent with their corresponding method bodies and only a small part of method names are inconsistent with corresponding method bodies. To this end, in this paper, we conduct an empirical study to assess the state-of-the-art DL-based approaches in the automated identification of inconsistent method names. We first build a new benchmark (dataset) by using both automatic identification from commit history and manual inspection by developers, aiming to reduce the number of false positives. Based on the benchmark, we evaluate five representative DL-based approaches to identifying inconsistent method names (one is retrieval-based and two are generation-based). Our evaluation results suggest that the performance of the evaluated approaches is substantially reduced when we switch from the existing balanced dataset to our new benchmark. Furthermore, to reveal where and why the evaluated approaches work/fail, we conduct quantitative and qualitative analyses of the evaluation results. Our analysis results suggest that the evaluated approaches work well on methods with simple bodies and short names, and retrieval-based approaches are especially good at methods whose names start with popular first sub-tokens. Retrieval-based approaches fail frequently because the adopted method representation technique is not efficient enough. Another possible reason for the failures is their unverified rationale, i.e., two methods with similar bodies should have similar names. Generation-based approaches frequently fail because of inaccurate similarity calculation formulas and immature method name generation techniques. Through the data analysis, we also propose two possible ways for better identifying inconsistent method names by leveraging contrastive learning and LLMs. Overall, our empirical study suggests that the state-of-the-art DL-based approaches in inconsistent method name identification deserve significant improvement before applying them to practical software systems. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.
Author keywords: Empirical study; Inconsistency checking; Method names; Neural networks
Index keywords: Contrastive Learning; Deep learning; Balanced datasets; Empirical studies; Evaluation results; False positive; Inconsistency checking; Method name; Neural-networks; Performance; Software-systems; State of the art; Adversarial machine learning
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2025
EID: 2-s2.0-85210080717
DOI: 10.1007/s10664-024-10592-z
Retrieval channels: authoritative_outlet_search
Local full-text files: 
