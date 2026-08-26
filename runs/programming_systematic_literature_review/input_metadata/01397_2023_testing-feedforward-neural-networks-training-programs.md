---
otero_id: "2-s2.0-85145565103"
title: "Testing Feedforward Neural Networks Training Programs"
authors: "Ben Braiek H.; Khomh F."
year: "2023"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3529318"
---
# Scopus title-abstract-keyword metadata
Title: Testing Feedforward Neural Networks Training Programs
Abstract: At present, we are witnessing an increasing effort to improve the performance and trustworthiness of Deep Neural Networks (DNNs), with the aim to enable their adoption in safety critical systems such as self-driving cars or aircraft collision-avoidance systems. Multiple testing techniques are proposed to generate test cases that can expose inconsistencies in the behavior of DNN models. These techniques assume implicitly that the training program is bug-free and appropriately configured. However, satisfying this assumption for a novel problem requires significant engineering work to prepare the data, design the DNN, implement the training program, and tune the hyperparameters to produce the model for which current automated test data generators search for corner-case behaviors. All these model training steps can be error prone. Therefore, it is crucial to detect and correct errors throughout all the engineering steps of DNN-based software systems and not only on the resulting DNN model. In this article, we gather a catalog of training issues and based on their symptoms and their effects on the behavior of the training program, we propose practical verification routines to detect the aforementioned issues, automatically, by continuously validating that some important properties of the learning dynamics hold during the training. Then, we design TheDeepChecker, an end-to-end property-based debugging approach for DNN training programs and implement it as a TensorFlow-based library. As an empirical evaluation, we conduct a case study to assess the effectiveness of TheDeepChecker on synthetic and real-world buggy DL programs and compare its performance to that of the Amazon SageMaker Debugger (SMD). Results show that TheDeepChecker's on-execution validation of DNN-based program's properties through three sequential phases (pre-, on-, and post-fitting) succeeds in revealing several coding bugs and system misconfigurations errors early on and at a low cost. Moreover, our property-based approach outperforms the SMD's offline rules verification on training logs in terms of detection accuracy for unstable learning issues and coverage of additional DL bugs. © 2023 Association for Computing Machinery.
Author keywords: Neural networks; property-based debugging; training programs
Index keywords: Aircraft accidents; Errors; Feedforward neural networks; Neural network models; Program debugging; Software testing; Training aircraft; Aircraft collision avoidance systems; Car collisions; Neural network model; Neural networks trainings; Neural-networks; Performance; Property-based; Property-based debugging; Safety critical systems; Training program; Deep neural networks
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2023
EID: 2-s2.0-85145565103
DOI: 10.1145/3529318
Retrieval channels: authoritative_outlet_search
Local full-text files: 
