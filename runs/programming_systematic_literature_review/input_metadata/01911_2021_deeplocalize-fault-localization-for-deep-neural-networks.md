---
otero_id: "2-s2.0-85112675039"
title: "DeepLocalize: Fault localization for deep neural networks"
authors: "Wardat M.; Le W.; Rajan H."
year: "2021"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse43902.2021.00034"
---
# Scopus title-abstract-keyword metadata
Title: DeepLocalize: Fault localization for deep neural networks
Abstract: Deep Neural Networks (DNNs) are becoming an integral part of most software systems. Previous work has shown that DNNs have bugs. Unfortunately, existing debugging techniques don't support localizing DNN bugs because of the lack of understanding of model behaviors. The entire DNN model appears as a black box. To address these problems, we propose an approach and a tool that automatically determines whether the model is buggy or not, and identifies the root causes for DNN errors. Our key insight is that historic trends in values propagated between layers can be analyzed to identify faults, and also localize faults. To that end, we first enable dynamic analysis of deep learning applications: by converting it into an imperative representation and alternatively using a callback mechanism. Both mechanisms allows us to insert probes that enable dynamic analysis over the traces produced by the DNN while it is being trained on the training data. We then conduct dynamic analysis over the traces to identify the faulty layer or hyperparameter that causes the error. We propose an algorithm for identifying root causes by capturing any numerical error and monitoring the model during training and finding the relevance of every layer/parameter on the DNN outcome. We have collected a benchmark containing 40 buggy models and patches that contain real errors in deep learning applications from Stack Overflow and GitHub. Our benchmark can be used to evaluate automated debugging tools and repair techniques. We have evaluated our approach using this DNN bug-and-patch benchmark, and the results showed that our approach is much more effective than the existing debugging approach used in the state-of-the-practice Keras library. For 34/40 cases, our approach was able to detect faults whereas the best debugging approach provided by Keras detected 32/40 faults. Our approach was able to localize 21/40 bugs whereas Keras did not localize any faults.  © 2021 IEEE.
Author keywords: Debugging; Deep learning bugs; Deep Neural Networks; Fault Location; Program Analysis
Index keywords: Benchmarking; Errors; Program debugging; Debugging; Deep learning bug; Dynamics analysis; Fault localization; Integral part; Modeling behaviour; Neural network model; Program analysis; Root cause; Software-systems; Deep neural networks
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2021
EID: 2-s2.0-85112675039
DOI: 10.1109/icse43902.2021.00034
Retrieval channels: authoritative_outlet_search
Local full-text files: 
