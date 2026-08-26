---
otero_id: "2-s2.0-85196831711"
title: "Investigating White-Box Attacks for On-Device Models"
authors: "Zhou M.; Gao X.; Wu J.; Liu K.; Sun H.; Li L."
year: "2024"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1145/3597503.3639144"
---
# Scopus title-abstract-keyword metadata
Title: Investigating White-Box Attacks for On-Device Models
Abstract: Numerous mobile apps have leveraged deep learning capabilities. However, on-device models are vulnerable to attacks as they can be easily extracted from their corresponding mobile apps. Although the structure and parameters information of these models can be accessed, existing on-device attacking approaches only generate black-box attacks (i.e., indirect white-box attacks), which are less effective and efficient than white-box strategies. This is because mobile deep learning (DL) frameworks like TensorFlow Lite (TFLite) do not support gradient computing (referred to as non-debuggable models), which is necessary for white-box attacking algorithms. Thus, we argue that existing findings may underestimate the harm-fulness of on-device attacks. To validate this, we systematically analyze the difficulties of transforming the on-device model to its debuggable version and propose a Reverse Engineering framework for On-device Models (REOM), which automatically reverses the compiled on-device TFLite model to its debuggable version, enabling attackers to launch white-box attacks. Our empirical results show that our approach is effective in achieving automated transformation (i.e., 92.6%) among 244 TFLite models. Compared with previous attacks using surrogate models, REOM enables attackers to achieve higher attack success rates (10.23%→89.03%) with a hun-dred times smaller attack perturbations (1.0→0.01). Our findings emphasize the need for developers to carefully consider their model deployment strategies, and use white-box methods to evaluate the vulnerability of on-device models. Our artifacts11https://github.com/zhoumingyi/REOM are available.  © 2024 ACM.
Author keywords: Model Conversion; Responsible AI; SE for AI
Index keywords: Learning systems; Program debugging; Reverse engineering; Black boxes; Device modelling; Engineering frameworks; Learning capabilities; Learning frameworks; Mobile app; Model conversion; Responsible AI; SE for AI; White box; Deep learning
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2024
EID: 2-s2.0-85196831711
DOI: 10.1145/3597503.3639144
Retrieval channels: authoritative_outlet_search
Local full-text files: 
