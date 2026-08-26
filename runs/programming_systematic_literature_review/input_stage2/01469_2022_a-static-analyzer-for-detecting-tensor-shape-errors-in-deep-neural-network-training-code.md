---
otero_id: "2-s2.0-85132408997"
title: "A Static Analyzer for Detecting Tensor Shape Errors in Deep Neural Network Training Code"
authors: "Jhoo H.Y.; Kim S.; Song W.; Park K.; Lee D.; Yi K."
year: "2022"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse-companion55297.2022.9793771"
---
# Scopus title-abstract-keyword metadata
Title: A Static Analyzer for Detecting Tensor Shape Errors in Deep Neural Network Training Code
Abstract: We present an automatic static analyzer PyTea that detects tensorshape errors in PyTorch code. The tensor-shape error is critical in the deep neural net code; much of the training cost and intermediate results are to be lost once a tensor shape mismatch occurs in the midst of the training phase. Given the input PyTorch source, PyTea statically traces every possible execution path, collects tensor shape constraints required by the tensor operation sequence of the path, and decides if the constraints are unsatisfiable (hence a shape error can occur). PyTea's scalability and precision hinges on the characteristics of real-world PyTorch applications: the number of execution paths after PyTea's conservative pruning rarely explodes and loops are simple enough to be circumscribed by our symbolic abstraction. We tested PyTea against the projects in the official PyTorch repository and some tensor-error code questioned in the StackOverflow. PyTea successfully detects tensor shape errors in these codes, each within a few seconds. © 2022 IEEE.
Author keywords: Software and its engineering → Software testing and debugging
Index keywords: Deep neural networks; Errors; Network coding; Program debugging; Software testing; Deep neural nets; Engineering software; Execution paths; NET codes; Neural networks trainings; Shape errors; Software and its engineering → software testing and debugging; Software Testing and Debugging; Static analyzers; Training codes; Tensors
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2022
EID: 2-s2.0-85132408997
DOI: 10.1109/icse-companion55297.2022.9793771
Retrieval channels: authoritative_outlet_search
Local full-text files: 
