---
otero_id: "2-s2.0-85179808010"
title: "Better Pay Attention Whilst Fuzzing"
authors: "Zhu S.; Wang J.; Sun J.; Yang J.; Lin X.; Wang T.; Zhang L.; Cheng P."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2023.3338129"
---
# Scopus title-abstract-keyword metadata
Title: Better Pay Attention Whilst Fuzzing
Abstract: Fuzzing is one of the prevailing methods for vulnerability detection. However, even state-of-the-art fuzzing methods become ineffective after some period of time, i.e., the coverage hardly improves as existing methods are ineffective to focus the attention of fuzzing on covering the hard-to-trigger program paths. In other words, they cannot generate inputs that can break the bottleneck due to the fundamental difficulty in capturing the complex relations between the test inputs and program coverage. In particular, existing fuzzers suffer from the following main limitations: 1) lacking an overall analysis of the program to identify the most 'rewarding' seeds, and 2) lacking an effective mutation strategy which could continuously select and mutates the more relevant 'bytes' of the seeds. In this work, we propose an approach called ATTuzz to address these two issues systematically. First, we propose a lightweight dynamic analysis technique that estimates the 'reward' of covering each basic block and selects the most rewarding seeds accordingly. Second, we mutate the selected seeds according to a neural network model which predicts whether a certain 'rewarding' block will be covered given certain mutations on certain bytes of a seed. The model is a deep learning model equipped with an attention mechanism which is learned and updated periodically whilst fuzzing. Our evaluation shows that ATTuzz significantly outperforms 5 state-of-the-art grey-box fuzzers on 6 popular real-world programs and MAGMA data sets at achieving higher edge coverage and finding new bugs. In particular, ATTuzz achieved 1.2X edge coverage and 1.8X bugs detected than AFL++ over 24-hour runs. In addition, ATTuzz also finds 4 new bugs in the latest version of some popular software including p7zip and openUSD.  © 1976-2012 IEEE.
Author keywords: attention model; deep learning; Fuzzing; program analysis
Index keywords: Codes (symbols); E-learning; Edge detection; Neural network models; Program debugging; Software testing; Attention model; Code; Computer bugs; Deep learning; Fuzzing; Image edge detection; Program analysis; State of the art; Recurrent neural networks
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85179808010
DOI: 10.1109/tse.2023.3338129
Retrieval channels: authoritative_outlet_search
Local full-text files: 
