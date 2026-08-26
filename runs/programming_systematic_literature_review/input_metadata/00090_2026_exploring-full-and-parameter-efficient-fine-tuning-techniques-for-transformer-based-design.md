---
otero_id: "2-s2.0-105038847841"
title: "Exploring full and parameter-efficient fine-tuning techniques for transformer-based design pattern detection"
authors: "Rezgui I.; Mzid R.; Ziadi T."
year: "2026"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2026.108176"
---
# Scopus title-abstract-keyword metadata
Title: Exploring full and parameter-efficient fine-tuning techniques for transformer-based design pattern detection
Abstract: Context: Design patterns offer reusable solutions to common software development problems, improving code quality and maintainability. Despite their significance, design pattern instances in source code are often undocumented, making difficult for developers to identify and exploit them effectively. Automating pattern detection can support program comprehension, refactoring, and maintenance; however, existing approaches face several challenges. Objective: This study aims to develop an approach for detecting Gang of Four (GoF) design patterns in source code. The proposed approach seeks to address the limitations of previous works, which often struggle with feature generalization and structural similarity among patterns. The work further explores how transfer learning strategies can enhance detection performance while reducing computational cost. Methods: In this work, we introduce a Seq2Seq modeling approach for design pattern detection, leveraging the encoder-decoder architecture of CodeT5＋ to capture both structural and semantic dependencies in object-oriented code. Instead of treating design pattern detection as a standard classification task, we reformulate it as a sequence generation problem. We propose DPDAtt+[jls-end-space/], a transformer-based framework built on a Seq2Seq. The model is trained on a curated dataset and fine-tuned using two strategies: full fine-tuning and parameter-efficient fine-tuning using Low-Rank Adaptation (LoRA). Both strategies are empirically evaluated to compare detection accuracy and computational efficiency. Results: Experimental results show that LoRA fine tuning reduces computational cost while retaining competitive accuracy. Full fine-tuning, however, achieves the highest overall detection performance, reaching 94% accuracy on GoF design pattern detection in Java codebases. Both variants of DPDAtt+ outperform state-of-the-art approaches in terms of precision, recall, and F1-score. Conclusion: The findings demonstrate that transfer learning with Transformer-based architectures effectively captures the structural and semantic characteristics of design patterns in code. DPDAtt+[jls-end-space/], through both full fine-tuning and PEFT, offers a robust solution for automated design pattern detection, contributing to more intelligent software analysis and maintenance tools. © 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.
Author keywords: Fine-tuning; GoF patterns; LLMs; Seq2Seq models; Software engineering; Transformer architecture
Index keywords: Computer software reusability; Computer software selection and evaluation; Cost reduction; Data mining; Learning systems; Object oriented programming; Software architecture; Software design; Tuning; Design pattern detections; Design Patterns; Detection performance; Fine tuning; Gang of four pattern; LLM; Seq2seq model; Source codes; Transfer learning; Transformer architecture; Computational efficiency; Semantics
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2026
EID: 2-s2.0-105038847841
DOI: 10.1016/j.infsof.2026.108176
Retrieval channels: authoritative_outlet_search
Local full-text files: 
