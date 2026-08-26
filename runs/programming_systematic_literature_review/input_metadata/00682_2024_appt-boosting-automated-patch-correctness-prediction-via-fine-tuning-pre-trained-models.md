---
otero_id: "2-s2.0-85182923361"
title: "APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models"
authors: "Zhang Q.; Fang C.; Sun W.; Liu Y.; He T.; Hao X.; Chen Z."
year: "2024"
journal: "IEEE Transactions on Software Engineering"
doi: "10.1109/tse.2024.3354969"
---
# Scopus title-abstract-keyword metadata
Title: APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models
Abstract: Automated program repair (APR) aims to fix software bugs automatically without human debugging efforts and plays a crucial role in software development and maintenance. Despite the recent significant progress in the number of fixed bugs, APR is still challenged by a long-standing overfitting problem (i.e., the generated patch is plausible but overfitting). Various techniques have thus been proposed to address the overfitting problem. Recently, researchers have employed BERT to extract code features, which are then used to train a classifier for patch correctness prediction, indicating the potential of such pre-trained models in reasoning about patch correctness. However, BERT is restricted to feature extraction for classifier training without benefiting from the training process, potentially generating sub-optimal vector representations for patched code snippets. In this paper, we propose APPT, a pre-trained model-based automated patch correctness assessment technique by both pre-training and fine-tuning. APPT adopts a pre-trained model as the encoder stack, followed by an LSTM stack and a deep learning classifier. More importantly, the pre-trained model is fine-tuned in conjunction with other components as a whole pipeline to fully adapt it specifically for reasoning about patch correctness. Although our idea is general and can be built on various existing pre-trained models, we have implemented APPT based on the BERT model. We conduct an extensive experiment on 1,183 Defects4J patches and the experimental results show that APPT achieves prediction accuracy of 79.7% and recall of 83.2%, outperforming the state-of-the-art technique CACHE by 4.3% and 6.7%. Our additional investigation on 49,694 real-world patches shows that APPT achieves the optimum performance (exceeding 99% in five common metrics for assessing patch classification techniques) compared with existing representation learning techniques. We further investigate the impact of each component and find that they all positively contribute to APPT, e.g., the fine-tuning process and the LSTM stack increase F1-score by 10.22% and 4.11%, respectively. We also prove that adopting advanced pre-trained models can further provide substantial advancement (e.g., GraphCodeBERT-based APPT improves BERT-based APPT by 2.8% and 3.3% in precision and AUC, respectively), highlighting the generalizability of APPT. Overall, our study highlights the promising future of fine-tuning pre-trained models to assess patch correctness and reduce the manual inspection effort of debugging experts when deploying APR tools in practice. © 1976-2012 IEEE.
Author keywords: Automated program repair; patch correctness; pre-trained model
Index keywords: Automation; Classification (of information); Codes (symbols); Extraction; Forecasting; Long short-term memory; Optimal systems; Repair; Software design; Adaptation models; Automated program repair; Code; Computer bugs; Features extraction; Fine tuning; Patch correctness; Pre-trained model; Predictive models; Task analysis; Feature extraction
Document type: Article
Conference: 
Source title: IEEE Transactions on Software Engineering
Year: 2024
EID: 2-s2.0-85182923361
DOI: 10.1109/tse.2024.3354969
Retrieval channels: authoritative_outlet_search
Local full-text files: 
