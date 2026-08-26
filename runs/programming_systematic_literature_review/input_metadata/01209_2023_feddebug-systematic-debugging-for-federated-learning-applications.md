---
otero_id: "2-s2.0-85171759945"
title: "FedDebug: Systematic Debugging for Federated Learning Applications"
authors: "Gill W.; Anwar A.; Gulzar M.A."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00053"
---
# Scopus title-abstract-keyword metadata
Title: FedDebug: Systematic Debugging for Federated Learning Applications
Abstract: In Federated Learning (FL), clients independently train local models and share them with a central aggregator to build a global model. Impermissibility to access clients' data and collaborative training make FL appealing for applications with data-privacy concerns, such as medical imaging. However, these FL characteristics pose unprecedented challenges for debugging. When a global model's performance deteriorates, identifying the responsible rounds and clients is a major pain point. Developers resort to trial-and-error debugging with subsets of clients, hoping to increase the global model's accuracy or let future FL rounds retune the model, which are time-consuming and costly. We design a systematic fault localization framework, Fedde-bug,that advances the FL debugging on two novel fronts. First, Feddebug enables interactive debugging of realtime collaborative training in FL by leveraging record and replay techniques to construct a simulation that mirrors live FL. Feddebug'sbreakpoint can help inspect an FL state (round, client, and global model) and move between rounds and clients' models seam-lessly, enabling a fine-grained step-by-step inspection. Second, Feddebug automatically identifies the client(s) responsible for lowering the global model's performance without any testing data and labels-both are essential for existing debugging techniques. Feddebug's strengths come from adapting differential testing in conjunction with neuron activations to determine the client(s) deviating from normal behavior. Feddebug achieves 100% accuracy in finding a single faulty client and 90.3% accuracy in finding multiple faulty clients. Feddebug's interactive de-bugging incurs 1.2% overhead during training, while it localizes a faulty client in only 2.1% of a round's training time. With FedDebug,we bring effective debugging practices to federated learning, improving the quality and productivity of FL application developers. © 2023 IEEE.
Author keywords: client; CNN; fault localization; federated learning; neural networks; software debugging; testing
Index keywords: Application programs; Learning systems; Medical imaging; Program debugging; Software testing; Client; Client models; Collaborative training; Fault localization; Federated learning; Global models; Modeling performance; Neural-networks; Software debugging; Systematic debugging; Data privacy
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171759945
DOI: 10.1109/icse48619.2023.00053
Retrieval channels: authoritative_outlet_search
Local full-text files: 
