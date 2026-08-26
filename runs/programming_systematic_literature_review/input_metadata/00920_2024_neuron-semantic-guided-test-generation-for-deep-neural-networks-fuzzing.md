---
otero_id: "2-s2.0-85218169035"
title: "Neuron Semantic-Guided Test Generation for Deep Neural Networks Fuzzing"
authors: "Huang L.; Sun W.; Yan M.; Liu Z.; Lei Y.; Lo D."
year: "2024"
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3688835"
---
# Scopus title-abstract-keyword metadata
Title: Neuron Semantic-Guided Test Generation for Deep Neural Networks Fuzzing
Abstract: In recent years, significant progress has been made in testing methods for deep neural networks (DNNs) to ensure their correctness and robustness. Coverage-guided criteria, such as neuron-wise, layer-wise, and path-/trace-wise, have been proposed for DNN fuzzing. However, existing coverage-based criteria encounter performance bottlenecks for several reasons: Testing Adequacy: Partial neural coverage criteria have been observed to achieve full coverage using only a small number of test inputs. In this case, increasing the number of test inputs does not consistently improve the quality of models. Interpretability: The current coverage criteria lack interpretability. Consequently, testers are unable to identify and understand which incorrect attributes or patterns of the model are triggered by the test inputs. This lack of interpretability hampers the subsequent debugging and fixing process. Therefore, there is an urgent need for a novel fuzzing criterion that offers improved testing adequacy, better interpretability, and more effective failure detection capabilities for DNNs.To alleviate these limitations, we propose NSGen, an approach for DNN fuzzing that utilizes neuron semantics as guidance during test generation. NSGen identifies critical neurons, translates their high-level semantic features into natural language descriptions, and then assembles them into human-readable DNN decision paths (representing the internal decision of the DNN). With these decision paths, we can generate more fault-revealing test inputs by quantifying the similarity between original test inputs and mutated test inputs for fuzzing. We evaluate NSGen on popular DNN models (VGG16_BN, ResNet50, and MobileNet_v2) using CIFAR10, CIFAR100, Oxford 102 Flower, and ImageNet datasets. Compared to 12 existing coverage-guided fuzzing criteria, NSGen outperforms all baselines, increasing the number of triggered faults by 21.4% to 61.2% compared to the state-of-the-art coverage-guided fuzzing criterion. This demonstrates NSGen's effectiveness in generating fault-revealing test inputs through guided input mutation, highlighting its potential to enhance DNN testing and interpretability.  © 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Author keywords: Deep learning testing; fuzzing; test input generation
Index keywords: Computer debugging; Deep neural networks; High level languages; Multilayer neural networks; Neurons; Program debugging; Coverage criteria; Decision paths; Deep learning testing; Fuzzing; Interpretability; Neural-networks; Test generations; Test input generation; Test inputs; Testing adequacies; Semantics
Document type: Article
Conference: 
Source title: ACM Transactions on Software Engineering and Methodology
Year: 2024
EID: 2-s2.0-85218169035
DOI: 10.1145/3688835
Retrieval channels: authoritative_outlet_search
Local full-text files: 
