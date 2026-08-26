---
otero_id: 20072
otero_key: "3JXCTFGK"
title: "An explainable lesion detection transformer model for medical imaging diagnosis decision support: Design science research"
authors: "Xinwei Wang; Yi Feng; Sutong Wang; Dujuan Wang; T.C.E. Cheng"
year: "2025"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2025.114492"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An explainable lesion detection transformer model for medical imaging diagnosis decision support: Design science research

![](/api/attachments/3JXCTFGK/fulltext/images/40eeb6fd10c1629152a7ef969fdab9a804ee989506eb27927069adda2f214635.jpg)

Xinwei Wang $^{a,b}$ , Yi Feng $^{c}$ , Sutong Wang $^{a,*}$ , Dujuan Wang $^{a}$ , T.C.E. Cheng $^{b}$

$^{a}$ Business School, Sichuan University, Chengdu 610064, China

$^{b}$ Department of Logistics and Maritime Studies, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong

$^{c}$ School of Economics and Management, Fuzhou University, Xueyuan Road, Qishan Campus, Fuzhou 350116, China

## ARTICLEINFO

Keywords:
Medical decision support
Lesion detection
Design science research
Artificial intelligence artifact
Explainable machine learning

## ABSTRACT

Utilizing machine learning methods for auxiliary decision support in medical imaging significantly reduces missed detections and unnecessary expenses. However, the strict accuracy and transparency requirements in the medical field pose challenges for deep learning applications based on neural networks. To address these issues, we propose a novel artificial intelligence artifact guided by the design science research methodology for lesion detection decision support in medical images, called Explainable Lesion DEtection TRansformer (EL-DETR). This approach features an explainable separate attention mechanism in the decoder that highlights the attention weights of content and location queries, providing insights into the inference process through attention mapping visualizations. In addition, we introduce a hybrid matching query strategy to enhance the learning of positive samples and develop an adaptive efficient compound loss function to optimize training. We demonstrate EL-DETR's superior accuracy, robustness, and interpretability using four real-world datasets, establishing it as a reliable tool for clinical diagnosis and treatment decision support based on medical imaging. The code and original data are available at https://github.com/weimingai/EL-DETR.

## 1. Introduction

Decision support systems are evolving in healthcare, using clinical data and information technology to help physicians participate in the complex decision-making process of patient diagnosis and management. Medical imaging technologies, such as Computed Tomography (CT), Magnetic Resonance Imaging (MRI), ultrasound, and endoscopy, are vital tools in modern healthcare for non-invasive diagnosis, enabling early detection and treatment of conditions like tumors and neurological disorders $[1,2]$ . However, the accuracy of diagnoses heavily depends on the expertise of radiologists, and the intensive image review process can lead to fatigue, increasing the risk of misdiagnoses $[3]$ .

Advances in medical data availability and computational power have driven the integration of information systems technologies into disease treatment and management $[4,5]$ , significantly alleviating clinicians' workloads and reducing medical costs $[6,7]$ . Neural network-based deep learning has shown promise in automating medical image analysis, including texture and feature extraction $[8]$ , medical image translation $[9]$ , and lesion classification, localization, and segmentation $[10]$ .

Among these, object detection methods are particularly noteworthy for their ability to simultaneously locate and classify lesions, with end-to-end real-time detection models enhancing medical decision support and improving diagnostic efficiency $[11]$ .

However, medical imaging decision-making faces several significant challenges that limit its accuracy and clinical applicability. First, the inherent complexities of patients' internal structures present major obstacles for lesion detection, as limited internal light sources, overlapping tissues, anatomical irregularities, food residues, and surgical implants often interfere with lesion recognition $[12]$ . Patient-specific factors, such as body movements, respiration, and variations in heart rate or blood pressure, further compromise image clarity $[13]$ . In addition, variations in imaging equipment and light sources, along with the heterogeneity in lesion location, shape, size, and color, pose substantial challenges to model decision-making $[14]$ .

Second, the opaque nature of deep neural network models, often referred to as the “black box” problem, complicates the interpretability of their inference processes, making it challenging for clinicians to trust and adopt the diagnostic recommendations provided by these models [15]. Furthermore, existing object detection models typically embed extracted features or results directly into prediction blocks without fully leveraging spatial and contextual information about lesions, which limits their ability to provide nuanced diagnostic insights $[16–18]$ .

Finally, data imbalance in medical imaging poses a critical issue for lesion detection. Most medical images or video frames are normal and lack lesions, while even lesion-containing images often include only a small fraction of lesion-related pixels $[19]$ . This imbalance hampers the training of machine learning models, often leading to missed detections or false positives. Conventional approaches, such as over-sampling or under-sampling, attempt to mitigate this issue $[20]$ , but they suffer from drawbacks like increased computational overhead, amplified noise, or reduced model robustness $[21]$ . In DEtection TRansformer (DETR)-like methods, simply increasing the number of positive queries can effectively enhance training efficiency $[22]$ .

To address the challenges outlined, we develop an information technology (IT) artifact based on AI, the Explainable Lesion DEtection TRansformer (EL-DETR), guided by design science research (DSR). EL-DETR tackles these challenges through three key innovations: First, it integrates the translation invariance of Deep Convolutional Neural Networks (DCNN) with transformers to enhance the extraction of spatial features and global contextual understanding from medical images. Second, an explainable separate attention mechanism is introduced in the transformer decoder, improving the model's comprehension of lesion spatial features while visualizing attention weights to enhance transparency and provide clinicians with interpretable decision support. Finally, a hybrid matching query method and an efficient compound loss function are employed to address data imbalance, enhancing the model's learning of positive lesion samples and ensuring robust performance with minimal computational overhead. Our work represents the first AI artifact designed using DSR for disease risk decision support in medical imaging. The primary contributions of our work are outlined below.

\- We develop a novel AI artifact for lesion diagnosis in medical imaging, providing clinicians with accurate and reliable decision support for lesion localization and classification during imaging evaluations, which expands the design theory of medical imaging decision support systems.

\- We contribute to the field of explainable machine learning in clinical applications by proposing an explainable separate attention mechanism that enables EL-DETR's decoders to independently focus on content and position queries. This innovation provides clinicians with insights into the model's reasoning processes through visual attention weight mapping.

\- To address the challenge of learning from unbalanced medical data in machine learning, we introduce a training-enhanced hybrid query matching method that combines one-to-one and one-to-many query matching, enhancing the learning ability of positive samples. In addition, we propose an efficient compound loss function that integrates one-to-one query matching loss, one-to-many query matching loss, and auxiliary loss through an adaptive weighting scheme, improving the training efficiency of the model.

We organize the rest of the paper as follows: Section 2 reviews closely related research to position our work within the literature. The design and development of EL-DETR are detailed in Section 3. Section 4 describes the process of experiments using four real data sources and demonstrates the application of EL-DETR. Section 5 verifies the EL-DETR's effectiveness, robustness, and interpretability based on experimental results. Finally, Section 6 discusses the communication step, highlighting the contributions and implications of EL-DETR, and gives a demonstration of the implementation scheme for clinical medical imaging decision support system. Section 7 concludes the paper and outlines future research directions.

## 2. Literature review

## 2.1. AI in medical decision support

Recent advancements in medical information systems have significantly enhanced the application of AI in healthcare, particularly in triage, disease diagnosis, and readmission risk prediction. Research in this area can be categorized into three major streams, reflecting the evolving methodologies and applications of AI in healthcare decision support systems.

The first research stream focuses on AI-assisted patient triage. Sánchez-Salmerón et al. [23] demonstrated that machine learning can effectively assess patient symptoms, provide accurate triage classification in emergency settings especially during pandemics, and optimize medical resource allocation. Wang et al. [24] applied heterogeneous data-driven machine learning to streamline primary and secondary care triage, reducing clinicians' assessment time.

The second research stream explores AI's role in disease diagnosis. Kalgotra et al. [25] developed a network-based machine learning model to predict colorectal cancer risk, enabling patient stratification and early intervention. Wu et al. [26] introduced a meta-path attention-based deep learning model to identify high-risk cirrhosis patients, supporting clinical decision-making.

The third research stream focuses on AI-driven predictions of hospital stay length and readmission risk. Peng et al. [27] proposed a deep learning model that integrates demographics, clinical history, injury severity, and physiological variables to predict hospital stay duration for trauma patients. Todd et al. [28] combined machine learning and survival analysis to predict readmissions, providing decision support for hospital management. Ben-Assuli et al. [29] applied machine learning to assess 30-day readmission risk in congestive heart failure patients, comparing the effectiveness of manual selection to enhance clinical decision-making.

While these studies highlight significant advancements in AI-driven medical decision-making, clinical diagnostic support remains the most directly relevant to patient treatment and health. In addition, most existing research relies on structured clinical data or electronic health records, whereas medical images often play a critical role in diagnosis. Consequently, this study emphasizes AI applications in medical image-based decision support.

## 2.2. Medical imaging decision support system

Medical imaging is the gold standard for diagnosing various diseases. With advancements in AI-driven image processing, research has increasingly focused on applying AI to assist medical image-based decision-making. And they primarily fall into two categories: AI model structure innovation and medical data feature innovation. Regarding the first category, Zhang et al. $[30]$ developed a multi-task medical image analysis model based on DCNN, integrating UNET and YOLO to simultaneously support lesion detection and segmentation. Zeng et al. $[31]$ combined graph convolutional and deep convolutional neural networks, leveraging graph structures to represent expert knowledge and refine medical image decision-making. Given the transformer's powerful contextual learning capabilities, we integrate it with DCNN to extract deeper feature information, and enhance decision support.

For data feature, the multi-source nature of medical imaging data often results in inconsistent data distributions and labeling. To address these challenges, Li et al. $[10]$ employed a dual self-supervised network to extract regions of interest from multi-source data and integrate unlabeled images for pre-training models for classification, detection, and segmentation decision-making. To mitigate label inconsistency, Li et al. $[32]$ introduced offline category mapping to recover lost labels and proposed predictive masking alongside online category mapping to counteract missing label effects. To improve training efficiency for positive samples learning, we propose an enhanced query matching mechanism, optimizing decision support in medical image diagnosis.

Existing studies highlight the progress in developing accurate AI-based medical imaging decision support systems. The black-box nature of neural networks remains a major obstacle to AI adoption in medical decision-making. Therefore, building interpretable AI models is a critical research focus.

## 2.3. Medical decision-making based on explainable AI

Despite the remarkable capabilities of machine learning across various tasks, ensuring credible and interpretable results remains a persistent challenge, particularly in medical decision-making. Interpretable machine learning (XML) typically employs feature importance analysis and decision tree-based methods, which have demonstrated strong performance when applied to tabular data and traditional machine learning models $[33,34]$ . To address deep learning's limitations with tabular data, Dentamaro et al. $[35]$ introduced an adaptive multiscale attention deep neural network, improving interpretability through attention mechanisms. Zhao et al. $[36]$ developed an interpretable deep metric learning framework that facilitates clearer image distinction. In addition, Fan et al. $[37]$ highlighted that high-level task near the decision-making layer play a crucial role in interpretability by integrating information from lower-level tasks.

Given the transparency required in healthcare applications, XAI is widely used in disease diagnosis and treatment decision-making. Janizek et al. [38] employed a feature attribution approach to optimize anticancer drug selection. Makowski et al. [39] leveraged interpretable machine learning classifiers to identify optimal antibody combinations. Beyond therapeutics, interpretable models have significantly advanced disease prediction and diagnosis. Liu et al. [40] applied a hidden Markov model to describe sepsis progression and utilized a machine learning model to analyze temporal data, producing interpretable decision-making. Bouazizi and Ltifi [41] developed a multilayered machine learning framework to enhance both accuracy and interpretability, improving EEG-based medical decision support for stroke prediction.

These studies indicate that XAI has been widely studied for healthcare decision support. However, the interpretability of complex deep learning models remains a challenge, particularly in medical imaging. Based on the above ideas, this paper focuses on the interpretable innovation of deep medical imaging model in decision-making.

## 3. Artifact description

Design science aims to create or innovate IT artifacts to solve practical problems and extend human behavior $[42]$ . We adhere to the six design steps of DSR and the nominal process model outlined by Peffers et al. $[43]$ in designing EL-DETR. This section systematically provides a comprehensive description of the artifact design, EL-DETR.

## 3.1. The overall framework

The EL-DETR model architecture adheres to the design principles of the Detection Transformer (DTER) model, which is a transformer-based, end-to-end object detection model. Unlike traditional models that rely exclusively on DCNN (such as Faster RCNN, YOLO v3), this architecture does not require the anchor generation parameter to generate detection boxes, as well as Non-Maximum Suppression (NMS) to eliminate duplicate prediction boxes. The DETR-like models use query embedding to generate the corresponding detection box and bipartite graph matching to select the optimal prediction result, which reduces the model parameters and calculation cost. By leveraging the powerful capabilities of transformers and attention mechanisms, EL-DETR extends the applicability and interpretability of DETR-like models in practical clinical settings, and addresses the “black box” nature typically associated with deep object detection models. The pipeline architecture of the EL-DETR model is depicted in Fig. 1.

In Fig. 1, the framework of EL-DETR consists of three parts: a DCNN-based backbone network, a transformer-based encoder and decoder network, and a prediction network. Initially, image data such as frame I extracted from an endoscopic video, is converted into a 3D tensor $X_{i}$ , enabling processing by the deep learning network. The tensor $X_{i}$ is then fed into the backbone network to extract multi-scale image features, resulting in the feature representation $S_{i}$ , and position embedding $E_{i}^{position}$ . To avoid the degradation of deep learning model performance with the increase of network depth, inspired by the He et al. [44], we introduce a 50-layer ResNet network structure to realize fast links and avoid gradient explosion.

Subsequently, we build a 6-layer encoder network based on the transformer to encode image features. First, we input the features $S_{i}$ the position embedding $E_{i}^{position}$ to encoder, and calculate the vector of query, key and value. Then we use the multi-head attention mechanism to update the embedding, and output the embedding $E_{i}^{encoder} = \{e_1, e_2, \cdots, e_{D_E}\}$ enhanced by feedforward neural network and normalization operations. The encoder $E_{i}^{encoder}$ , along with query embedding $Q_{i} = \{q_1, q_2, \cdots, q_L\}$ is then fed into the decoder. Utilizing an attention mechanism, the decoder updates the embeddings, outputting $E_{i}^{decoder}$ , where both $Q_{i}$ and $E_{i}^{decoder}$ have dimensions corresponding to the length of queries $L$ .

The decoder output $E_{i}^{decoder}$ is then processed by the multi-task multi-head prediction neural network block, which comprises a box regression prediction head and classification prediction head to predict the positions $P_{i} = \{p_{1}, p_{2}, \cdots, p_{n}\}$ and categories $C_{i} = \{c_{1}, c_{2}, \cdots, c_{n}\}$ of lesions in the medical image, with n denoting the number of lesions. The number of outputs is consistent with the number of queries provided to the decoder, and the most relevant outcomes are then selected based on the probability scores. The calculation processes of the box regression prediction head and the classification prediction head are detailed in Eqs.

![](/api/attachments/3JXCTFGK/fulltext/images/5e047409ab454df89da6fa5402876057234799c2f35b5c8b63eee39593d0ea1d.jpg)  
Fig. 1. Overall architecture of EL-DETR.

X. Wang et al.

(1) and (2).

$$
y _ {b o x} = \text { sigmoid } \left(f (E ^ {\text { decoder }}) + [ r ^ {T} 0 0 ] ^ {T}\right)\tag{1}
$$

$$
y _ {c l a s s} = f \big (E ^ {d e c o d e r} \big)\tag{2}
$$

where the predicted object box $y_{box} = \left[y_{box}^{x}, y_{box}^{y}, y_{box}^{width}, y_{box}^{height}\right]$ is a vector containing the predicted transverse coordinates $y_{box}^{x}$ and longitudinal coordinates $y_{box}^{y}$ of the lesion center along with its width $y_{box}^{width}$ and height $y_{box}^{height} \cdot y_{class}$ is the predicted category of lesion, f is the feedforward neural network operation, while r is the reference point generated from the corresponding to object query, serving as a parameter for predicting the candidate box.

More importantly, to enhance the efficiency and interpretability of the EL-DETR, several key improvements are introduced. First, an explainable separate attention mechanism is implemented in the decoder to learn content and spatial queries simultaneously. Second, a one-to-many query matching strategy is proposed to improve the model's learning efficiency on positive samples. Third, an efficient compound loss function is employed for model training. Finally, interpretability is achieved by analyzing the variations in the model's attention weights in the cross-attention mechanism during inference. The subsequent sections provide a detailed explanation of the EL-DETR model's key improvements.

## 3.2. Explainable transformer-based decoder

An explainable separate attention mechanism is added to decoder to process the output of encoder $E^{encoder}$ and object query Q. Inspired by Meng et al. [45], we calculate the weights using the dot product based on their respective query and key vectors, and then combine them to obtain the final attention weight, as shown in Eq. (3). The structure and calculation process of the explainable separate attention mechanism are illustrated in Fig. 2.

$$
\boldsymbol {c r o s s} _ {a t t} = \boldsymbol {q} _ {c} ^ {T} \cdot \boldsymbol {k} _ {c} + \boldsymbol {q} _ {p} ^ {T} \cdot \boldsymbol {k} _ {p}\tag{3}
$$

where $q_{c}$ and $q_{p}$ are content query and position query respectively, $k_{c}$ is the embedding of encoder's output, and $k_{p}$ is the embedding of normalized 2D coordinate of object query.

Unlike DETR, the position query in the decoder of EL-DETR is determined by a combination of decoder embeddings output from the previous layer $E_{layer-1}^{decoder}$ and reference points r. The reference points are formed according to the normalized two-dimensional coordinates of the object queries, enabling $q_{p}$ to be computed with $k_{p}$ . We normalize the reference points and then map them to embedding with sinusoidal positions, as shown in Eq. (4).

![](/api/attachments/3JXCTFGK/fulltext/images/4a207ead491006b741075c8e01f8ccb14146498344c323853291b351a9bdc9d6.jpg)  
Fig. 2. The decoder structure of EL-DETR.  
Note: The add & norm is the residuals add and normalizing layer.

$$
r _ {p} = \sin u (\text { sigmoid } (r))\tag{4}
$$

where sinu is an operation that maps to sinusoidal embeddings and sigmoid is an activation function in neural networks.

We design a feedforward neural network block f to map the embeddings of the previous layer's output of decoder to the same space and calculate the $q_{p}$ by transformation as follows:

$$
q _ {p} = f _ {r p}\tag{5}
$$

Finally, we extract the weights from the cross-attention mechanism and map them to image I for visualization, facilitating an interpretable analysis of the model.

## 3.3. Training-enhanced hybrid query matching

In medical examination images, most parts are normal and lack lesions, and most of the images have fewer than ten lesion labels. In model training, the DER-like model uses a bipartite graph matching algorithm to align each ground truth with the most matched prediction box and calculate the corresponding loss. However, other prediction boxes are treated as empty sets, resulting in more than 90 % of prediction boxes failing to contribute effective localization supervision [22].

To improve the model's learning efficiency in lesion regions and accelerate convergence during training, we introduce one-to-many queries in the query embedding and proportionally repeat the number of ground truth labels. Notably, the one-to-many matching query does not create a category imbalance because it enhances the bounding box learning without producing classification bias. Furthermore, as both one-to-one and one-to-many matching results are derived from the best prediction box aligned by the bipartite graph matching algorithm, the method does not increase the risk of misclassifying normal regions as pathological. So, it will not introduce the additional false positives.

Unlike object detection models based solely on DCNNs, the DETR-like models employ one-to-one matching queries to predict objects. Specifically, the model first sets the required number of objects to predict, then calculates the loss between the predicted results and the ground truth using a bipartite matching algorithm. Finally, it optimizes the model parameters through backpropagation and gradient descent. The loss calculation for the one-to-one matching query is as follows:

$$
\tau_ {o n e 2 o n e} = \tau_ {H u n g a r i a n} (y _ {o n e 2 o n e}, \widehat {y})\tag{6}
$$

where the Hungarian is a bipartite graph matching algorithm adopted by us, $y_{one2one}$ is the output of the prediction, and $\hat{y}$ is the ground truth.

In addition, we propose a training-enhanced hybrid matching query. We build an additional one-to-many query $\overline{Q}$ on the basis of query Q, and process them simultaneously with decoder to get the predicted result $y = \left\{y_{one2one}, y_{one2many}\right\}$ , where $y_{one2many}$ is the model prediction output corresponding to $\overline{Q}$ . We input each layer' output of the decoder into prediction block, and calculate one-to-many matching loss after matching with the enhancement target $\overline{y}$ . The losses of one-to-many matching and hybrid matching can be calculated according to Eqs. (7) and (8).

$$
\tau_ {o n e 2 m a n y} = \sum_ {n = 1} ^ {L} \tau_ {\text { Hungarian }} \left(y _ {o n e 2 m a n y}, \bar {y}\right)\tag{7}
$$

$$
\tau_ {h y b r i d} = \tau_ {o n e 2 o n e} + \lambda \tau_ {o n e 2 m a n y}\tag{8}
$$

where the $L$ is the number of layers of the decoder, $\bar{y}$ is the enhancement target of ground truth repeated $\mu$ times with $\bar{y} = \left\{\bar{y}_1,\bar{y}_2,\dots,\bar{y}_\mu \right\}$ and $\bar{y}_{1} = \bar{y}_{2} = \ldots = \bar{y}_{\mu} = \widehat{y}$ , and $\lambda$ is the coefficient of one-to-many matching loss. Moreover, to handle both one-to-one queries and one-to-many queries simultaneously, we construct a mask for the self-attention mechanism to eliminate their interactions.

According to the proposed hybrid matching query, EL-DETR first matches the model prediction with the ground truth, and then calculates the loss $\tau$ . The matched loss consists of three parts, namely Cross-Entropy (CE) loss $Loss_{ce}$ for lesion category prediction, L1 loss $Loss_{L1}$ for lesion bounding box prediction and Generalized Intersection over Union (GIOU) loss $Loss_{giou}$ for lesion area and location. Among them, compared with IOU, GIOU extends the no-overlapping gradients and better reflects the overlap situations [46]. And the specific loss calculation method is as follows:

$$
\tau = \varepsilon_ {c e} \cdot L o s s _ {c e} + \varepsilon_ {L 1} \cdot L o s s _ {L 1} + \varepsilon_ {g i o u} \cdot L o s s _ {g i o u}\tag{9}
$$

where $\varepsilon_{ce}$ , $\varepsilon_{L1}$ , and $\varepsilon_{giou}$ are the coefficients.

To accelerate model convergence speed and improve training efficiency, we construct an efficient compound loss function for hybrid matching query, and utilize embeddings from intermediate decoder layers to enhance the training process. Thus, inspired by Carion et al. [47], we introduce an auxiliary loss, denoted as $\tau_{aux}$ . By inputting outputs from the first five decoder layers into the multi-head prediction block during the one-to-one matching process, we obtain $\tau_{aux}$ based on these predictions. The specific calculation process is as follows:

$$
\tau_ {a u x} = \sum_ {n = 1} ^ {L - 1} \tau_ {\text { Hungarian }} (y _ {\text { one2one }}, \widehat {y})\tag{10}
$$

Then, we calculate compound losses $\tau_{EC}$ based on one-to-one matching losses, one-to-many matching losses, and auxiliary losses, as follows:

$$
\tau_ {E C} = \alpha_ {o n e 2 o n e} \cdot \tau_ {o n e 2 o n e} + \alpha_ {o n e 2 m a n y} \cdot \tau_ {o n e 2 m a n y} + \alpha_ {a u x} \cdot \tau_ {a u x}
$$

(11)

where $\alpha_{one2one},\alpha_{one2many}$ , and $\alpha_{aux}$ are the coefficients respectively.

## 4. Experiment

## 4.1. Data preparation

To evaluate the performance of the proposed EL-DETR in real-world scenarios, we collect four medical imaging datasets from various hospital sources including endoscopy, MRI and CT. And they all have been reviewed by relevant ethics committees for handling sensitive information and bioinformation. The detailed descriptions of the datasets are as follows:

Colonoscopy Dataset: This dataset consists of 152 colonoscopy videos with white light and narrow band imaging (NBI) light sources. These videos are labeled by four experts and three beginners.

MICCAI Dataset: Published by the Medical Image Computing and Computer Assisted Intervention (MICCAI) Society challenge, this dataset includes 38 polyp detection videos adopted in the sub-challenge for gastrointestinal image analysis. To adapt it for our task, according to Li et al. [48], we convert the mask annotation into bounding boxes and divide them into adenomas and hyperplastic polyps.

KUMC Dataset: This dataset is derived from patient colonoscopies at the University of Kansas Medical Center, consisting of 80 videos. We processed its annotation according to Li et al. [48].

Brain Tumor Dataset $^{1}$ : This dataset consists of medical images from MRI or CT scans, a total of 1116 images containing information about the existence, location and category of brain tumors, and the detection targets are classified as negative or positive.

## 4.2. Data preprocessing

Before training and testing, a series of data preprocessing steps are conducted. First, we extract frames from the videos and mark the position and category of polyps in the Colonoscopy dataset according to Mesejo et al. [14]. However, multiple video frames may contain repeated content, which could lead to model overfitting and inefficient use of computing resources. To address this, we use random intervals to extract frame images and their corresponding labels from the video files. As a result, we obtain a total of 14,120 images, comprising 2177 images from the Colonoscopy dataset, 6079 from the MICCAI dataset, 4748 from the KUMC dataset, and 1116 from Brain Tumor dataset.

In terms of data splits, we divide the dataset into training, validation, and test sets in the ratio of 6:2:2. We treat the test dataset as a held-out validation set, and only perform parameter optimization and selection on the validation dataset, so as to ensure that the test data are not leaked. We then convert the annotations of all the datasets into the Microsoft Common Objects in Context (COCO) dataset annotation format. In addition, to further improve the training efficiency of the model, we perform data augmentation on the training and validation sets. Specifically, we apply random horizontal inversion, random scaling, random clipping, and normalization on the training data, while only random scaling is applied to the validation set. No processing is performed on the test set.

## 4.3. Experimental setup and parameter selection

To train EL-DETR for optimal performance, we conduct an extensive hyperparameter tuning process. The parameter search aims to identify the best-performing configuration on the validation dataset based on the loss function values, which is the direct objective of model optimization, ensuring a balance between model accuracy and computational efficiency. The selected hyperparameter values and search scope are summarized in Table 1.

Additionally, $\alpha_{one2one}$ and $\alpha_{one2many}$ are selected adaptively according to different datasets. On all datasets, $\alpha_{one2one}$ is set to 1, and the optimal values of $\alpha_{one2many}$ for Colonoscopy, MICCAI, KUMC and Brain Tumor datasets are 0.5, 0.5, 0.5, 1 respectively. To verify the effectiveness and robustness of our proposed model, we implement it using the PyTorch library in Python and conduct experiments on an NVIDIA 3090 graphics

## Table 1

Hyperparameter search and optimization.

<table><tr><td>Parameter</td><td>Description</td><td>Parameter search space</td><td>Optimal value</td></tr><tr><td>bs</td><td>The amount of data processed per batch</td><td>[2,8]</td><td>8</td></tr><tr><td>epoch</td><td>Training iteration</td><td>[10,150]</td><td>50</td></tr><tr><td>lr</td><td>The initial learning rate of EL-DETR</td><td>[0.00001,0.1]</td><td>0.0001</td></tr><tr><td> $lr_{backbone}$ </td><td>The initial learning rate of backbone in EL-DETR</td><td>[0.00001,0.1]</td><td>0.00001</td></tr><tr><td>optimizer</td><td>The optimizer of training</td><td>[Adam, AdamW, SGD]</td><td>AdamW</td></tr><tr><td>wd</td><td>optimizer weight decay</td><td>[0.0,0.001]</td><td>0.0001</td></tr><tr><td> $\varepsilon_{ce}$ </td><td>The weight of class loss</td><td>[1,10]</td><td>2</td></tr><tr><td> $\varepsilon_{L1}$ </td><td>The weight of L1 loss for bounding box</td><td>[1,10]</td><td>5</td></tr><tr><td> $\varepsilon_{giou}$ </td><td>The weight of the loss of generalized intersection over union</td><td>[1,10]</td><td>2</td></tr><tr><td> $\alpha_{aux}$ </td><td>The weight of loss for auxiliary prediction</td><td>[0.1,1]</td><td>0.5</td></tr><tr><td> $N_q$ </td><td>Number of queries</td><td>[100,300]</td><td>100</td></tr><tr><td> $N_{one2many}$ </td><td>Number of one-to-many matching queries</td><td>[100,1500]</td><td>500</td></tr><tr><td> $\lambda$ </td><td>The number of times the ground truth is repeated in a one-to-many match</td><td>[1,10]</td><td>6</td></tr></table>

processing unit (GPU) with 24GB of memory. All the comparative experiments and ablation studies are performed under identical conditions and with the same hardware setup.

## 5. Model evaluation

## 5.1. Basic experiment result analysis

We conduct experiments on four datasets to evaluate the effectiveness of EL-DETR, with a particular focus on the variation in loss components during training. The loss dynamics of EL-DETR during training are illustrated in Figs. 3–6, providing insights into how the model converges over time. Specifically, Fig. 3 corresponds to the Colonoscopy dataset, while Fig. 4 presents the losses for the MICCAI dataset, Fig. 5 relates to the KUMC dataset, and Fig. 6 relates to the Brain Tumor dataset.

To provide a comprehensive understanding, we also display the loss of different categories. Figs. (a) in the four datasets show the evolution of the cross-entropy loss for classification, the L1 loss for object bounding boxes, and the GIOU loss for object area and location throughout the training epochs. The overall trend indicates a significant reduction in these losses over time, reflecting improved model performance in both object localization and classification tasks. In contrast, Figs. (b) highlight the breakdown of different components of the efficient compound loss used by EL-DETR, including the one-to-one loss for predictions derived from the final layer of the decoder, the one-to-many loss for one-to-many query matching, and the auxiliary loss generated from intermediate decoder layers.

From Figs. 3–6, several key observations regarding the training dynamics can be summarized. First, all the loss categories exhibit a consistent downward trend across all the four datasets, especially during the initial training stages. The losses decrease rapidly within the first five epochs, followed by a gradual plateau and a notable drop around the 40th iteration before stabilizing. This pattern indicates that the model effectively adapts to the data, showing significant improvements in predictions during both early and later training phases. In terms of loss values, the total loss is substantially larger than the individual components: cross-entropy loss, L1 loss, and GIOU loss. Notably, during the first five epochs, the cross-entropy loss is significantly greater than the GIOU loss. However, as training progresses, the cross-entropy loss gradually approaches and aligns with the GIOU loss. This suggests that the model's ability to predict object categories is initially limited, but by the fifth epoch, there is a marked improvement in the model's predictive capability for categories, while the improvement in location prediction remains smooth and gradual.

Second, regarding the components of the efficient compound losses, the auxiliary loss remains the largest, while the one-to-one loss is the smallest throughout training. The total loss value is closer to the auxiliary loss value. In addition, the decreasing trend of the one-to-one loss is relatively smooth, whereas the one-to-many loss and auxiliary loss decrease more steeply, particularly in the initial five epochs. This suggests that both the one-to-many loss and the auxiliary loss contribute to accelerating the training efficiency and enhancing the convergence rate of the model.

![](/api/attachments/3JXCTFGK/fulltext/images/5fd14d971676d3aa9fd9997d77d33968608595f9e1dba7f3044f58eb23d93acd.jpg)

We also plot the PR curves the EL-DETR on different datasets for different categories of lesions, as shown in Supplementary material Fig. S1. According to the PR curve, we see that the prediction accuracy of the proposed EL-DETR model is accurate and very close on different categories of lesions, which demonstrates that the prediction performance of EL-DETR is almost not affected by the lesion categories. Moreover, EL-DETR also has a good balance between precision and recall indexes.

## 5.2. Comparison experiment analysis

To substantiate the effectiveness of the proposed EL-DETR in lesion detection tasks, we conduct comparative experiments across four benchmark datasets. We include baseline models with varying architectures, such as Faster R-CNN $[49]$ , YOLO v3 $[16]$ , YOLOS $[50]$ , and DETR $[47]$ . For advanced DETR-like models, we include DAB-DETR $[51]$ , Deformable-DETR $[17]$ , DN-DETR $[52]$ , and DINO $[18]$ . Among them, DAB-DETR uses dynamic anchor boxes to enhance queries, Deformable-DETR introduces multi-scale features and the deformable attention mechanism, and DN-DETR proposes a new denoising training method. DINO uses contrastive learning for denoising training, and a mixed query selection method for anchor initialization. According to these studies, we utilize Mean Average Precision (MAP) at IOU thresholds of 0.5 and 0.75, as well as MAP and Mean Average Recall (MAR) at IOU values ranging from 0.50 to 0.95, to measure the accuracy of lesion predictions.

For all comparison models, we load the pre-trained model provided by the authors to initialize the network weights and adopt the default optimal hyperparameters. Also, we compare MAP@0.50:0.95, MAP@0.50, MAP@0.75, and MAR@0.50:0.95 indicators of all the models with a maximum number of object detections of 100. From Table 2, we find that EL-DETR achieves optimal performance on MAP@0.50:0.95, MAP@0.50, and MAP@0.75 for all the four datasets. In the Colonoscopy dataset, EL-DETR achieves the second-best performance at MAR@0.50:0.95 (0.794), only $3.76\%$ lower than the best performance achieved by DINO (0.825). On the MICCAI dataset, EL-DETR achieves the third-best performance at MAR@0.50:0.95 (0.829), which is $2.36\%$ lower than the optimal performance (0.849). On the KUMC dataset, EL-DETR achieves the fourth-best performance at MAR@0.50:0.95 (0.810), which is $2.29\%$ lower than the best performance at 0.829. In the Brain Tumor dataset, EL-DETR also achieves

(a)  
![](/api/attachments/3JXCTFGK/fulltext/images/dceb772cb3e61c1c7a6e51369bffdd236d6b1dd2b39a1561264373e2531eae05.jpg)  
(b)  
Fig. 3. The training loss variation of EL-DETR in Colonoscopy dataset.

![](/api/attachments/3JXCTFGK/fulltext/images/2d37f098b863b6a790aad814c9eb1a9b558ff0e1ad77d32002736497db88b4a1.jpg)  
(a)

![](/api/attachments/3JXCTFGK/fulltext/images/5ae776de625d65ff276e8a2fc3b428f17fdb2f803c2edbe9da3a7f91fcfc7a5f.jpg)  
(b)

Fig. 4. The loss variation of EL-DETR in MICCAI dataset.  
![](/api/attachments/3JXCTFGK/fulltext/images/62e6df2eb51804e9903a267728a2e994b335af4bc6f7d9692c37fdb84387bd54.jpg)  
(a)

![](/api/attachments/3JXCTFGK/fulltext/images/1904d19205dc303769fffc3133e7f4e03867a1bf26480636e76bd8d8f6c65d7f.jpg)  
(b)

Fig. 5. The loss variation of EL-DETR in KUMC dataset.  
![](/api/attachments/3JXCTFGK/fulltext/images/1b67991aeac3299a079cb5717297677be0829523819eedb4bfbb5b60329488af.jpg)  
(a)

![](/api/attachments/3JXCTFGK/fulltext/images/880c915c7b27fc1418bcf2b7b539bee13a7bd5b2d59e3588d6b11e8b17c61bb3.jpg)  
(b)  
Fig. 6. The loss variation of EL-DETR in Brain Tumor dataset.

obvious improvement in the MAR index, which is 50.82 % higher than that of YOLO v3. Overall, the proposed EL-DETR achieves more advanced predictive performance, especially in the precision metric, indicating that the EL-DETR model can accurately detect lesions in medical images.

## 5.3. Ablation experiment analysis

In this section, we conduct ablation studies alongside the EL-DETR model to explore the role of various improvements. First, we remove all the improvements to create a Pure-DETR model as the baseline. Next, we construct Hybrid-DETR, which incorporates only hybrid matching in the query, and Explain-DETR, which adds explainable separate attention mechanisms to the decoder, to analyze their individual effects. Because efficient compound loss function is designed for hybrid matching query, Hybrid-DETR and EL-DETR use efficient compound loss function, while Pure-DETR and Explain-DETR use loss function refer to Carion et al. [47]. The specific results are shown in Table 3.

Table 3  
Table 2  
The results of the comparison experiment. $^{a}$

<table><tr><td>Dataset</td><td>Model</td><td>Epoch</td><td>MAP@ 0.50:0.95</td><td>MAP@ 0.5</td><td>MAP@ 0.75</td><td>MAR@ 0.50:0.95</td></tr><tr><td rowspan="9">Colonoscopy dataset</td><td>Faster RCNN</td><td>50</td><td>0.628</td><td>0.925</td><td>0.745</td><td>0693</td></tr><tr><td>YOLO v3</td><td>50</td><td>0.546</td><td>0.940</td><td>0.579</td><td>0.633</td></tr><tr><td>YOLOS</td><td>150</td><td>0.549</td><td>0.939</td><td>0.555</td><td>0.670</td></tr><tr><td>DETR</td><td>100</td><td>0.667</td><td>0.968</td><td>0.789</td><td>0.674</td></tr><tr><td>DAB-DETR</td><td>100</td><td>0.664</td><td>0.932</td><td>0.786</td><td>0.776</td></tr><tr><td>Deformable-DETR</td><td>50</td><td>0.684</td><td>0.958</td><td>0.816</td><td>0.791</td></tr><tr><td>DN-DETR</td><td>50</td><td>0.688</td><td>0.962</td><td>0.831</td><td>0.782</td></tr><tr><td>DINO</td><td>12</td><td>0.654</td><td>0.920</td><td>0.784</td><td>0.825</td></tr><tr><td>EL-DETR</td><td>50</td><td>0.710</td><td>0.981</td><td>0.853</td><td>0.794</td></tr><tr><td rowspan="9">MICCAI dataset</td><td>Faster RCNN</td><td>50</td><td>0.768</td><td>0.979</td><td>0.923</td><td>0.812</td></tr><tr><td>YOLO v3</td><td>50</td><td>0.643</td><td>0.989</td><td>0.767</td><td>0.702</td></tr><tr><td>YOLOS</td><td>150</td><td>0.590</td><td>0.989</td><td>0.648</td><td>0.679</td></tr><tr><td>DETR</td><td>100</td><td>0.736</td><td>0.983</td><td>0.875</td><td>0.796</td></tr><tr><td>DAB-DETR</td><td>100</td><td>0.733</td><td>0.983</td><td>0.869</td><td>0.794</td></tr><tr><td>Deformable-DETR</td><td>50</td><td>0.765</td><td>0.987</td><td>0.920</td><td>0.837</td></tr><tr><td>DN-DETR</td><td>50</td><td>0.763</td><td>0.987</td><td>0.914</td><td>0.827</td></tr><tr><td>DINO</td><td>12</td><td>0.774</td><td>0.986</td><td>0.919</td><td>0.849</td></tr><tr><td>EL-DETR</td><td>50</td><td>0.778</td><td>0.990</td><td>0.937</td><td>0.829</td></tr><tr><td rowspan="9">KUMC dataset</td><td>Faster RCNN</td><td>50</td><td>0.713</td><td>0.944</td><td>0.840</td><td>0.762</td></tr><tr><td>YOLO v3</td><td>50</td><td>0.637</td><td>0.971</td><td>0.762</td><td>0.695</td></tr><tr><td>YOLOS</td><td>150</td><td>0.633</td><td>0.975</td><td>0.795</td><td>0.727</td></tr><tr><td>DETR</td><td>100</td><td>0.726</td><td>0.978</td><td>0.847</td><td>0.829</td></tr><tr><td>DAB-DETR</td><td>100</td><td>0.713</td><td>0.969</td><td>0.837</td><td>0.791</td></tr><tr><td>Deformable-DETR</td><td>50</td><td>0.738</td><td>0.985</td><td>0.863</td><td>0.808</td></tr><tr><td>DN-DETR</td><td>50</td><td>0.740</td><td>0.986</td><td>0.863</td><td>0.812</td></tr><tr><td>DINO</td><td>12</td><td>0.741</td><td>0.975</td><td>0.863</td><td>0.813</td></tr><tr><td>EL-DETR</td><td>50</td><td>0.753</td><td>0.990</td><td>0.884</td><td>0.810</td></tr><tr><td rowspan="9">Brain Tumor dataset</td><td>Faster RCNN</td><td>50</td><td>0.447</td><td>0.661</td><td>0.533</td><td>0.641</td></tr><tr><td>YOLO v3</td><td>50</td><td>0.316</td><td>0.634</td><td>0.276</td><td>0.486</td></tr><tr><td>YOLOS</td><td>150</td><td>0.438</td><td>0.738</td><td>0.484</td><td>0.667</td></tr><tr><td>DETR</td><td>100</td><td>0.380</td><td>0.652</td><td>0.386</td><td>0.647</td></tr><tr><td>DAB-DETR</td><td>100</td><td>0.497</td><td>0.728</td><td>0.561</td><td>0.748</td></tr><tr><td>Deformable-DETR</td><td>50</td><td>0.527</td><td>0.748</td><td>0.596</td><td>0.780</td></tr><tr><td>DN-DETR</td><td>50</td><td>0.487</td><td>0.727</td><td>0.567</td><td>0.760</td></tr><tr><td>DINO</td><td>12</td><td>0.337</td><td>0.521</td><td>0.384</td><td>0.788</td></tr><tr><td>EL-DETR</td><td>50</td><td>0.532</td><td>0.793</td><td>0.599</td><td>0.733</td></tr></table>

$^{a}$ The bolded values in the table represent the best values on the specified metrics in the specified dataset.

In Table 3, we observe a significant improvement in both Hybrid-DETR and Explain-DETR over Pure-DETR across all the four datasets. Specifically, for MAP@0.50:0.95, Hybrid-DETR achieves improvements of 1.35 %, 2.45 %, 1.79 % and 5.00 % on the Colonoscopy, MICCAI, KUMC and Brain Tumor datasets, respectively, compared with Pure-DETR. Similarly, Explain-DETR achieves greater gains, improving by 5.55 %, 5.03 %, 2.89 % and 38.15 % on the same datasets compared with Pure-DETR. Notably, explainable separate attention mechanisms contribute more to prediction accuracy than hybrid matching. Furthermore, the prediction accuracy can be further enhanced by adding hybrid matching queries to Explain-DETR, and the extent of improvement varies across different datasets.

In addition, we find that Hybrid-DETR achieves optimal values at MAR@0.50:0.95 across three endoscopic datasets, while the addition of the explainable separate attention mechanism reduces the improvement of hybrid matching at MAR@0.50:0.95. Furthermore, compared with the optimal value of MAR@0.50:0.95 in Table 2, Hybrid-DETR also demonstrates better performance on Colonoscopy, MICCAI, and KUMC datasets, which confirms that incorporating one-to-many queries and losses can enhance the model's learning ability for positive samples.

The results of the ablation experiment. $^{a}$

<table><tr><td>Dataset</td><td>Model</td><td>Matching</td><td>Loss</td><td>Epoch</td><td>MAP@ 0.50:0.95</td><td>MAP@ 0.5</td><td>MAP@ 0.75</td><td>MAR@ 0.50:0.95</td></tr><tr><td rowspan="4">Colonoscopy dataset</td><td>Pure-DETR</td><td>One2one</td><td> $\tau_{one2one},\tau_{aux}$ </td><td>100</td><td>0.667</td><td>0.968</td><td>0.789</td><td>0.674</td></tr><tr><td>Hybrid-DETR</td><td>Hybrid</td><td> $\tau_{EC}$ </td><td>50</td><td>0.676</td><td>0.949</td><td>0.818</td><td>0.834</td></tr><tr><td>Explain-DETR</td><td>One2one</td><td> $\tau_{one2one},\tau_{aux}$ </td><td>50</td><td>0.704</td><td>0.986</td><td>0.846</td><td>0.774</td></tr><tr><td>EL-DETR</td><td>Hybrid</td><td> $\tau_{EC}$ </td><td>50</td><td>0.710</td><td>0.981</td><td>0.853</td><td>0.794</td></tr><tr><td rowspan="4">MICCAI dataset</td><td>Pure-DETR</td><td>One2one</td><td> $\tau_{one2one},\tau_{aux}$ </td><td>100</td><td>0.736</td><td>0.983</td><td>0.875</td><td>0.796</td></tr><tr><td>Hybrid-DETR</td><td>Hybrid</td><td> $\tau_{EC}$ </td><td>50</td><td>0.754</td><td>0.988</td><td>0.895</td><td>0.873</td></tr><tr><td>Explain-DETR</td><td>One2one</td><td> $\tau_{one2one},\tau_{aux}$ </td><td>50</td><td>0.773</td><td>0.984</td><td>0.905</td><td>0.830</td></tr><tr><td>EL-DETR</td><td>Hybrid</td><td> $\tau_{EC}$ </td><td>50</td><td>0.778</td><td>0.990</td><td>0.937</td><td>0.829</td></tr><tr><td rowspan="4">KUMC dataset</td><td>Pure-DETR</td><td>One2one</td><td> $\tau_{one2one},\tau_{aux}$ </td><td>100</td><td>0.726</td><td>0.978</td><td>0.847</td><td>0.829</td></tr><tr><td>Hybrid-DETR</td><td>Hybrid</td><td> $\tau_{EC}$ </td><td>50</td><td>0.739</td><td>0.976</td><td>0.870</td><td>0.856</td></tr><tr><td>Explain-DETR</td><td>One2one</td><td> $\tau_{one2one},\tau_{aux}$ </td><td>50</td><td>0.747</td><td>0.985</td><td>0.874</td><td>0.811</td></tr><tr><td>EL-DETR</td><td>Hybrid</td><td> $\tau_{EC}$ </td><td>50</td><td>0.753</td><td>0.990</td><td>0.884</td><td>0.810</td></tr><tr><td rowspan="4">Brain Tumor dataset</td><td>Pure-DETR</td><td>One2one</td><td> $\tau_{one2one},\tau_{aux}$ </td><td>100</td><td>0.380</td><td>0.652</td><td>0.386</td><td>0.647</td></tr><tr><td>Hybrid-DETR</td><td>Hybrid</td><td> $\tau_{EC}$ </td><td>50</td><td>0.399</td><td>0.642</td><td>0.426</td><td>0.695</td></tr><tr><td>Explain-DETR</td><td>One2one</td><td> $\tau_{one2one},\tau_{aux}$ </td><td>50</td><td>0.525</td><td>0.789</td><td>0.599</td><td>0.738</td></tr><tr><td>EL-DETR</td><td>Hybrid</td><td> $\tau_{EC}$ </td><td>50</td><td>0.532</td><td>0.793</td><td>0.599</td><td>0.733</td></tr></table>

$^{a}$ The bolded values in the table represent the best values on the specified metrics in the specified dataset.

## 5.4. Explainable experiment analysis

In this section, we conduct an interpretable analysis of the EL-DETR. We visualize the attention weights of the cross-attention mechanism in the decoder part of the model and map these weights to the dimensions of the input medical image. Pixels corresponding to larger attention values are represented in brighter colors, while those with smaller values are depicted in darker colors. By examining the visual attention map, we can analyze the degree of attention and weight assigned to different pixels of medical images in the process of EL-DETR inference.

First, we compare the cross-attention weights of different layers in the decoder of EL-DETR, as shown in Fig. 7. It is evident that EL-DETR accurately identifies both the location and category of lesions, with the cross-attention weights in each layer all corresponding to the lesions' locations. Notably, different layers of the decoder focus on different aspects of the diseased areas. For instance, the first layer of the decoder emphasizes the pixels within the lesion, while as the layers progress, EL-DETR increasingly attends to the shapes and borders. This observation aligns with clinical criteria, as the shape and size of a patient's lesion significantly influence diagnosis and treatment decisions [53].

In addition, we compare the cross-attention weight maps of the decoder in EL-DETR with the baseline model, DETR. Fig. 8 presents the cross-attention weight map for DETR's decoder, while Fig. 9 shows the corresponding map for EL-DETR's decoder. Both models accurately predict lesion locations and categories in medical images, with the decoder's attention focusing on lesion pixels. However, in medical images, DETR's attention is more susceptible to noise and pays less attention to lesions than EL-DETR. In contrast, EL-DETR enhances the learning of positive lesion samples through one-to-many matching training, reducing the impact of noise. Moreover, the attention of EL-DETR emphasizes the boundaries and shape of the lesion site, reflecting the benefits of enhanced position queries in EL-DETR's decoder. Notably, EL-DETR allocates greater attention weight to diseased areas compared with DETR, indicating that EL-DETR more effectively distinguishes diseased tissue from surrounding areas during inference. These distinctions illustrate that EL-DETR provides a more reliable and interpretable mechanism for lesion detection.

In Supplementary material Figs. S2–S3, we also visualize the feature mapping of other modules of EL-DETR, including the last-layer features of the backbone network and the last-layer cross-attention features of the encoder network. Moreover, we employ Gradient-weighted Class Activation Mapping (Grad-CAM). a visual interpretation technique for convolutional neural networks $[54]$ , to further enhance the interpretability of the backbone network reasoning process of EL-DETR, and the results are presented in Supplementary material Fig. S4. The results show that although Grad-CAM highlights a broader area of interest, the feature weights and attention visualization maps focus more precisely on the lesion region. This improves the transparency of the entire prediction process of EL-DETR, and the interpretability analysis results of different components reveal the process of EL-DETR's image reasoning and decision-making. Notably, the decoder features near the decision-making layer more directly reflect the model's decision reasoning basis of the model. This aligns with Fan et al.'s study, as higher-level tasks incorporate information from lower-level tasks, making them more relevant to reasoning and decision-making $[37]$ . In addition, Supplementary material Figs. S5–S13 presents case studies that evaluate EL-DETR's interpretability across various datasets. The results confirm its consistent interpretability across different lesion types and sizes, underscoring the model's generalizability in medical images.

## 6. Communication and implication

## 6.1. Theoretical implication

This study offers three key theoretical contributions. First, it extends the theoretical application of DSR and AI in medical imaging decision support systems. While DSR has been widely utilized in decision support systems across various fields, its application in AI-based medical image diagnosis has not been thoroughly explored. Furthermore, although previous studies have applied AI for diagnosis grading $[24]$ , readmission prediction $[29]$ , and specific disease risk assessment $[41]$ , few have addressed robust lesion detection to enhance medical imaging decision. EL-DETR provides accurate lesion detection in medical images from diverse sources, presenting a novel perspective for designing AI-based medical imaging decision support systems within a theoretical framework.

Second, we enhance the interpretability of deep learning in medical decision support. Previous efforts often rely on post-hoc explanations, which lack transparency in model reasoning $[38,41]$ . By visualizing the cross-attention mappings embedded before the prediction block, EL-DETR reveals the model's focus on specific regions during inference. Specifically, we develop an explainable separate attention mechanism in the decoder tailored for lesion detection. Unlike existing methods that

Ground-truth: hyperplastic  
![](/api/attachments/3JXCTFGK/fulltext/images/96cbd99cacf409e60f7080a10cd157614d3327849f4da9d7e4b1bff19c12dad0.jpg)

![](/api/attachments/3JXCTFGK/fulltext/images/a6608b2076427543662464845cea7f5793847f14f7c6a88799731f89364a680f.jpg)

![](/api/attachments/3JXCTFGK/fulltext/images/80c3570e81dd2a221f942dcd09c0ac04e04abf28d14baaa6d6de70ae1caf862a.jpg)

![](/api/attachments/3JXCTFGK/fulltext/images/07fa28ae6b213a725a22d310fa08152880ea56ba32b2e7000481e43f6663cae8.jpg)  
Fig. 7. The visualization analysis of cross attention weight in the decoder of EL-DETR.

Prediction

Attention

Prediction

![](/api/attachments/3JXCTFGK/fulltext/images/33a4df92bf9ac35d7388fb9ef3beb5b46adacacc6af15d25255823967fa5620a.jpg)  
adenomatous

![](/api/attachments/3JXCTFGK/fulltext/images/b8dce4bc293c05493bf04775d30f32999c0e6539870c1ff7d747a36da5c98edd.jpg)  
hyperplastic

![](/api/attachments/3JXCTFGK/fulltext/images/a291bff54164308ce561870f5161793cdbcfe8dd40f37aa8b68eb5ecf4bf4ee1.jpg)  
serrated

![](/api/attachments/3JXCTFGK/fulltext/images/d26d253824f25c12b611a3496dbdfc59ccf502833ec63ce441277f00e5bce8d6.jpg)  
negative

![](/api/attachments/3JXCTFGK/fulltext/images/a3976eff8f131609b0c1f7e1b50e79824217e9ed40b5a84bf80a294ef366a91e.jpg)  
positive

Attention

Fig. 8. The visualization analysis of cross attention weight in decoder of DETR.  
![](/api/attachments/3JXCTFGK/fulltext/images/f67634bd4eeb6da7fcd44bb2c05634a81067ea30e5913942f9bbc2339f276d56.jpg)  
adenomatous

![](/api/attachments/3JXCTFGK/fulltext/images/1eda72df08091a2081933590cdad41354233ded2ce2706f6d1eb391f9665fde1.jpg)  
hyperplastic

![](/api/attachments/3JXCTFGK/fulltext/images/e25c63c3dff8b5328e510216d76b30d10299f8ed4cedc9791ee9d229bc2100a1.jpg)  
serrated

![](/api/attachments/3JXCTFGK/fulltext/images/c7da1aa5773738bf57da4b78b5634886380aa6989ee53e8f918d1c6984e0af70.jpg)  
negative

![](/api/attachments/3JXCTFGK/fulltext/images/86b16d5e5b17e0698bf977a4ac37014e724dcc207d3b4bd804f40638c0c0a0c2.jpg)  
positive  
Fig. 9. The visualization analysis of cross attention weight in decoder of EL-DETR.

primarily emphasize object content $[11,18]$ , our approach separates the content and position queries, highlighting the boundary shape and spatial position of lesions—factors that are crucial for detection and classification in clinical lesion diagnosis. Overall, the proposed EL-DETR mitigates the “black-box” nature of deep learning models, providing physicians with a trustworthy decision-support.

Third, we provide insights into addressing medical data imbalances and improving positive sample training. Medical data are frequently dominated by healthy samples, which poses challenges for training machine learning models $[20]$ . To overcome this issue, we propose a hybrid matching query method and an efficient compound loss function, significantly enhancing the model's learning ability for positive samples.

## 6.2. Managemental implications

This study also presents managerial implications for advancing medical imaging decision support through explainable AI-driven solutions. Radiologists often encounter overwhelming workloads when analyzing complex medical images, where both accuracy and efficiency are critical. EL-DETR addresses these challenges by offering an interpretable and robust framework that enhances diagnostic workflows while fostering trust in AI-based systems $[1,6]$ .

First, we introduce an AI artifact for an accurate and efficient decision support system in medical imaging lesion detection. Leveraging a DETR-like architecture, EL-DETR employs advanced separate attention mechanisms, a hybrid matching query strategy, and an efficient compound loss function to accurately and rapidly recognize lesion locations and classifications in clinical settings. Our evaluations, conducted on four diverse medical image datasets, demonstrate EL-DETR's robust performance. The design of EL-DETR ensures rapid and precise lesion analysis, alleviating radiologists' workloads and enhancing decision-making efficiency.

Second, interpretability is a key feature of EL-DETR, addressing the inherent “black box” nature of deep learning models $[15]$ . By visualizing cross-attention weight mappings in decoder and aligning them with the dimensions of the input medical images, EL-DETR provides clinicians with interpretable insights into its reasoning process. Specifically, the attention reveals that EL-DETR focuses on different lesion attributes at various decoder layers: earlier layers emphasize internal pixels, while later layers capture lesion boundaries and shapes, which aligns with clinical diagnostic criteria. Compared with DETR, EL-DETR's attention mechanism is less affected by noise and better distinguishes diseased areas, highlighting its capacity to support reliable and transparent diagnostic processes.

## 6.3. Medical imaging decision support system enabled by the proposed method

As depicted in Fig. 10, we implement the proposed EL-DETR as a medical imaging decision support system aimed at enhancing clinical decision-making and patient management. The system adopts a four-layer architecture: data layer, model layer, application layer, and user layer. At the data layer, a labeled dataset is constructed using open source data and then fed into the model layer for training and evaluation. The medical image data of a new patient can be obtained through the data acquisition unit in the application layer. These data are processed in the model layer and the trained model is invoked to generate predictive results and interpretable analysis reports. These results and reports are ultimately presented to patients and physicians through a human-computer interface at the application layer. Based on the doctor's diagnostic feedback, the system integrates new clinical image data into the local dataset at the data layer. Then, the model parameters and weights are retrained and updated at the model layer.

![](/api/attachments/3JXCTFGK/fulltext/images/bb4e8c6cb5d7a32e77ae4483492c2c569d2da3c4cfc64f80580cf8deda98d185.jpg)  
Fig. 10. A medical imaging decision support system enabled by the proposed EL-DETR.

## 7. Conclusion and future work

Under the guidance of DSR, this paper proposes a novel lesion detection model, EL-DETR, to support diagnostic decision-making in medical imaging. The model incorporates an explainable separate attention mechanism to enhance its focus on lesion locations and borders while providing visual explanations of its predictions through attention weight mappings. To improve lesion region learning, we introduce a hybrid matching query method that combines one-to-one and one-to-many matching. In addition, we develop an adaptive and efficient compound loss function that integrates weighted one-to-one matching loss, one-to-many matching loss, and auxiliary loss, improving training efficiency.

To evaluate the model's performance and robustness, we construct a medical lesion detection dataset comprising 14,120 images from four authentic sources. Comparison and ablation experiments demonstrate that EL-DETR achieves competitive predictive performance in real-world medical image-assisted decision-making scenarios, highlighting the effectiveness of its proposed improvements. Furthermore, case-based interpretability analysis confirms that EL-DETR's reasoning process is explainable, thereby enhancing trust in its predictions. This study has other limitations that warrant future research. Although the proposed EL-DETR achieves obvious improvement in the evaluation matrix, due to the limitation of medical image datasets, we hope to train EL-DETR on larger scale labeled datasets in the future to further improve the accuracy. In addition, we will explore more transparent deep learning models to improve our work.

## CRediT authorship contribution statement

Xinwei Wang: Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Conceptualization. Yi Feng: Writing – review & editing, Writing – original draft, Methodology, Conceptualization. Sutong Wang: Writing – review & editing, Writing – original draft, Resources, Methodology, Funding acquisition, Data curation, Conceptualization. Dujuan Wang: Writing – review & editing, Writing – original draft, Validation, Resources, Project administration, Funding acquisition, Conceptualization. T.C.E. Cheng: Writing – review & editing, Supervision, Resources.

## Declaration of competing interest

We declare that we have no financial and personal relationships with other people or organizations that can inappropriately influence our work, there is no professional or other personal interest of any nature or kind in any product, service and/or company that could be construed as influencing the position presented in, or the review of, the manuscript entitled, “An explainable lesion detection transformer model for medical imaging diagnosis decision support: Design science research”.

## Acknowledgments

This work is supported by grants from the National Natural Science Foundation of China (No. 7240010926, 72471158); the Postdoctoral Fellowship Program of CPSF (No. GZB20230459); the China Postdoctoral Science Foundation (No. 2024M762217); the Sichuan University to Building a World-class University (No. SKSYL2021-08) Sichuan University Interdisciplinary Innovation Fund.

## Data availability

Data will be available at https://github.com/weimingai/EL-DETR.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.dss.2025.114492.

## Data availability

Data will be made available on request.

## References

[1] Y.-P. Zhang, X.-Y. Zhang, Y.-T. Cheng, B. Li, X.-Z. Teng, J. Zhang, S. Lam, T. Zhou, Z.-R. Ma, J.-B. Sheng, V.C.W. Tam, S.W.Y. Lee, H. Ge, J. Cai, Artificial intelligence-driven radiomics study in cancer: the role of feature engineering and modeling, Mil. Med. Res. 10 (2023) 22.

[2] J. Olveres, G. Gonzalez, F. Torres, J.C. Moreno-Tagle, E. Carbajal-Degante, A. Valencia-Rodríguez, N. Méndez-Sánchez, B. Escalante-Ramírez, What is new in computer vision and artificial intelligence in medical image analysis applications, Quant. Imaging Med. Surg. 11 (2021) 3830–3853.

[3] A. Naeem, T. Anees, M. Khalil, K. Zahra, R.A. Naqvi, S.-W. Lee, SNC\_Net: skin cancer detection by integrating handcrafted and deep learning-based features using dermoscopy images, Mathematics 12 (2024) 1030.

[4] G. Meyer, G. Adomavicius, P.E. Johnson, M. Elidrisi, W.A. Rush, J.M. Sperl-Hillen, P.J. O'Connor, A machine learning approach to improving dynamic decision making, Inf. Syst. Res. 25 (2014) 239–263.

[5] R. Kohli, S.S.-L. Tan, Electronic health records: how can IS researchers contribute to transforming healthcare? MIS Q. 40 (2016) 553–574.

[6] M. Aziz, H. Haghbin, W. Sayeh, H. Alfatlawi, M.K. Gangwani, A.H. Sohail, T. Zahdeh, S. Weissman, F. Kamal, W. Lee-Smith, A. Nawras, P. Sharma, A. Shaukat, Comparison of artificial intelligence with other interventions to improve adenoma detection rate for colonoscopy: a network meta-analysis, J. Clin. Gastroenterol. 58 (2024) 143.

[7] A. Rimondi, K. Gottlieb, E.J. Despott, M. Iacucci, A. Murino, G.E. Tontini, Can artificial intelligence replace endoscopists when assessing mucosal healing in ulcerative colitis? A systematic review and diagnostic test accuracy meta-analysis, Dig. Liver Dis. 56 (2024) 1164–1172.

[8] G. Chakraborty, W. Wang, B. Chakraborty, S.-K. Tai, Y.-S. Lo, Grading of HCC biopsy images using nucleus and texture features, IEEE J. Biomed. Health Inform. 27 (2023) 65–74.

[9] Y. Li, H.-C. Shao, X. Liang, L. Chen, R. Li, S. Jiang, J. Wang, Y. Zhang, Zero-shot medical image translation via frequency-guided diffusion models, IEEE Trans. Med. Imaging 43 (2024) 980–993.

[10] J. Li, P. Zhang, T. Wang, L. Zhu, R. Liu, X. Yang, K. Wang, D. Shen, B. Sheng, DSMT-Net: dual self-supervised multi-operator transformation for multi-source endoscopic ultrasound diagnosis, IEEE Trans. Med. Imaging 43 (2024) 64–75.

[11] X. Liu, W. Li, Y. Yuan, Decoupled unbiased teacher for source-free domain adaptive medical object detection, IEEE Trans. Neural Netw. Learn. Syst. 35 (2024) 7287–7298.

[12] B. Chen, X. Huang, Y. Liu, Z. Zhang, G. Lu, Z. Zhou, J. Pan, Attention-guided and noise-resistant learning for robust medical image segmentation, IEEE Trans. Instrum. Meas. 73 (2024) 1–13.

[13] O. Ghekiere, R. Salgado, N. Buls, T. Leiner, I. Mancini, P. Vanhoenacker, P. Dendale, A. Nchimi, Image quality in coronary CT angiography: challenges and technical solutions, Br. J. Radiol. 90 (2017) 20160567.

[14] P. Mesejo, D. Pizarro, A. Abergel, O. Rouquette, S. Beorchia, L. Poincloux, A. Bartoli, Computer-aided classification of gastrointestinal lesions in regular colonoscopy, IEEE Trans. Med. Imaging 35 (2016) 2051–2063.

[15] B.R. Kim, K. Srinivasan, S.H. Kong, J.H. Kim, C.S. Shin, S. Ram, ROLEX: a novel method for interpretable machine learning using robust local explanations, MIS Q. 47 (2023).

[16] M. Dutta, A. Ganguly, Incremental-based YoloV3 model with hyper-parameter optimization for product image classification in E-commerce sector, Appl. Soft Comput. 165 (2024) 112029.

[17] Y. Chen, C. Zhang, B. Chen, Y. Huang, Y. Sun, C. Wang, X. Fu, Y. Dai, F. Qin, Y. Peng, Y. Gao, Accurate leukocyte detection based on deformable-DETR and multi-level feature fusion for aiding diagnosis of blood diseases, Comput. Biol. Med. 170 (2024) 107917.

[18] F. Li, H. Zhang, H. Xu, S. Liu, L. Zhang, L.M. Ni, H.Y. Shum, Mask DINO: towards a unified transformer-based framework for object detection and segmentation, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Vancouver, BC, Canada, 2023, pp. 3041–3050.

[19] T. Huynh, A. Nibali, Z. He, Semi-supervised learning for medical image classification using imbalanced training data, Comput. Methods Prog. Biomed. 216 (2022) 106628.

[20] Z. Afzal, M.J. Schuemie, J.C. van Blijderveen, E.F. Sen, M.C. Sturkenboom, J.A. Kors, Improving sensitivity of machine learning methods for automated case identification from free-text electronic medical records, BMC Med. Inform. Decis. Mak. 13 (2013) 30.

[21] Y. Yuan, J. Wei, H. Huang, W. Jiao, J. Wang, H. Chen, Review of resampling techniques for the treatment of imbalanced industrial data classification in equipment condition monitoring, Eng. Appl. Artif. Intell. 126 (2023) 106911.

[22] D. Jia, Y. Yuan, H. He, X. Wu, H. Yu, W. Lin, L. Sun, C. Zhang, H. Hu, DETRs with hybrid matching, in: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Vancouver, BC, Canada, 2023, pp. 19702–19712.

[23] R. Sanchez-Salmeron, J.L. Gomez-Urquiza, L. Albendín-García, M. Correa-Rodríguez, M.B. Martos-Cabrera, A. Velando-Soriano, N. Suleiman-Martos, Machine learning methods applied to triage in emergency services: a systematic review, Int. Emerg. Nurs. 60 (2022) 101109.

[24] B. Wang, W. Li, A. Bradlow, E. Bazuaye, A.T.Y. Chan, Improving triaging from primary care into secondary care using heterogeneous data-driven hybrid machine learning, Decis. Support. Syst. 166 (2023) 113899.

[25] P. Kalgotra, R. Sharda, S. Parasa, Quantifying disease-interactions through co-occurrence matrices to predict early onset colorectal cancer, Decis. Support. Syst. 168 (2023) 113929.

[26] Z. (Eric) Wu, D. Xu, P.J.-H. Hu, L. Li, T.-S. Huang, A meta-path, attention-based deep learning method to support hepatitis carcinoma predictions for improved cirrhosis patient management, Decis. Support. Syst. 181 (2024) 114226.

[27] J. Peng, D. Xu, P.J.-H. Hu, J.Q. Sheng, T.-S. Huang, A deep learning-based method to predict the length of stay for patients with traumatic fall injuries in support of physicians' clinical decisions and patient management, Decis. Support. Syst. 191 (2025) 114411.

[28] J. Todd, A. Gepp, S. Stern, B.J. Vanstone, Improving decision making in the management of hospital readmissions using modern survival analysis techniques, Decis. Support. Syst. 156 (2022) 113747.

[29] O. Ben-Assuli, T. Heart, R. Klempfner, R. Padman, Human-machine collaboration for feature selection and integration to improve congestive Heart failure risk prediction, Decis. Support. Syst. 172 (2023) 113982.

[30] K. Zhang, L. Zhang, H. Pan, UoloNet: based on multi-tasking enhanced small target medical segmentation model, Artif. Intell. Rev. 57 (2024) 31.

[31] X. Zeng, Y. Liu, J. Zhang, Y. Guo, Medical object detector jointly driven by knowledge and data, Neural Netw. 172 (2024) 106084.

[32] Q. Li, Y. Liu, Z. Zhang, J. Liu, Y. Yuan, K. Wang, R. He, Learning with incomplete labels of multisource datasets for ECG classification, Pattern Recogn. 150 (2024) 110321.

[33] Z. Bian, J. Zhang, F.-L. Chung, S. Wang, Residual sketch learning for a feature-importance-based and linguistically interpretable ensemble classifier, IEEE Trans. Neural Netw. Learn. Syst. 35 (2024) 10461–10474.

[34] A. Hjort, I. Scheel, D.E. Sommervoll, J. Pensar, Locally interpretable tree boosting: an application to house price prediction, Decis. Support. Syst. 178 (2024) 114106.

[35] V. Dentamaro, P. Giglio, D. Impedovo, G. Pirlo, M.D. Ciano, An interpretable adaptive multiscale attention deep neural network for tabular data, IEEE Trans. Neural Netw. Learn. Syst. 36 (2024) 1–15.

[36] W. Zhao, Y. Rao, J. Zhou, J. Lu, DIML: deep interpretable metric learning via structural matching, IEEE Trans. Pattern Anal. Mach. Intell. 46 (2024) 2518–2532.

[37] F.-L. Fan, J. Xiong, M. Li, G. Wang, On interpretability of artificial neural networks: a survey, IEEE Trans. Radiat. Plasma Med. Sci. 5 (2021) 741–760.

[38] J.D. Janizek, A.B. Dincer, S. Celik, H. Chen, W. Chen, K. Naxerova, S.-I. Lee, Uncovering expression signatures of synergistic drug responses via ensembles of explainable machine-learning models, Nat. Biomed. Eng. 7 (2023) 811–829.

[39] E.K. Makowski, T. Wang, J.M. Zupancic, J. Huang, L. Wu, J.S. Schardt, A.S. De Groot, S.L. Elkins, W.D. Martin, P.M. Tessier, Optimization of therapeutic antibodies for reduced self-association and non-specific binding via interpretable machine learning, Nat. Biomed. Eng 8 (2024) 45–56.

[40] Z. Liu, A. Khojandi, X. Li, A. Mohammed, R.L. Davis, R. Kamaleswaran, A machine learning–enabled partially observable markov decision process framework for early sepsis prediction, INFORMS J. Comput. 34 (2022) 2039–2057.

[41] S. Bouazizi, H. Ltifi, Enhancing accuracy and interpretability in EEG-based medical decision making using an explainable ensemble learning framework application for stroke prediction, Decis. Support. Syst. 178 (2024) 114126.

[42] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Q. 28 (2004) 75–105.

[43] M.A.R. Ken Peffers Tuure Tuunanen, S. Chatterjee, A design science research methodology for information systems research, J. Manag. Inf. Syst. 24 (2007) 45–77.

[44] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 2016, pp. 770–778.

[45] D. Meng, X. Chen, Z. Fan, G. Zeng, H. Li, Y. Yuan, L. Sun, J. Wang, Conditional DETR for fast training convergence, in: Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2021, pp. 3651–3660.

[46] H. Rezatofighi, N. Tsoi, J. Gwak, A. Sadeghian, I. Reid, S. Savarese, Generalized intersection over union: a metric and a loss for bounding box regression, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Long Beach, CA, USA, 2019, pp. 658–666.

[47] N. Carion, F. Massa, G. Synnaeve, N. Usunier, A. Kirillov, S. Zagoruyko, End-to-end object detection with transformers, in: A. Vedaldi, H. Bischof, T. Brox, J.-M. Frahm (Eds.), Computer Vision – ECCV 2020, Springer International Publishing, Cham, 2020, pp. 213–229.

[48] K. Li, M.I. Fathan, K. Patel, T. Zhang, C. Zhong, A. Bansal, A. Rastogi, J.S. Wang, G. Wang, Colonoscopy polyp detection and classification: dataset creation and comparative evaluations, PLoS ONE 16 (2021) e0255809.

[49] S. Ren, K. He, R. Girshick, J. Sun, Faster R-CNN: towards real-time object detection with region proposal networks, IEEE Trans. Pattern Anal. Mach. Intell. 39 (2017) 1137–1149.

[50] Y. Fang, B. Liao, X. Wang, J. Fang, J. Qi, R. Wu, J. Niu, W. Liu, You only look at one sequence: rethinking transformer in vision through object detection, in:

Proceedings of the 35th International Conference on Neural Information Processing Systems, Curran Associates Inc., Red Hook, NY, USA, 2024, pp. 26183–26197.

[51] J. Yang, H. Zhang, Y. Zhou, Z. Guo, F. Lin, Improved DAB-DETR model for irregular traffic obstacles detection in vision based driving environment perception scenario, Appl. Intell. 55 (2025) 541.

[52] F. Li, H. Zhang, S. Liu, J. Guo, L.M. Ni, L. Zhang, DN-DETR: accelerate DETR training by introducing query denoising, in: Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), New Orleans, LA, USA, 2022, pp. 13619–13627.

[53] B.C. Jacobson, A. Bhatt, K.B. Greer, L.S. Lee, W.G. Park, B.G. Sauer, V.M. Shami, ACG clinical guideline: diagnosis and management of gastrointestinal subepithelial lesions, Off. J. Am. Coll. Gastroenterol. | ACG 118 (2023) 46.

[54] R.R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, D. Batra, Grad-CAM: visual explanations from deep networks via gradient-based localization, in: Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), Venice, Italy, 2017, pp. 618–626.

Xinwei Wang is currently pursuing the Ph.D. degree in Management Science and Engineering from Sichuan University, Chengdu, China. He received the B.S. degree from Wuhan University of technology, Wuhan, China. He is currently working as a research assistant at The Hong Kong Polytechnic University under a joint-PhD project. His current research interests include machine learning, medical data mining and business data analytics. Part of his work has been published in journals such as IEEE Transactions on Industrial Informatics and Annals of Operations Research.

Yi Feng received the Ph.D. degree in Management Science and Engineering from the Sichuan University, Chengdu, China. She is a lecturer in Fuzhou University, Fuzhou, China. Her current research interests include information management, smart marketing, data mining and machine learning. Part of her work has been published in leading journals such as Decision Support Systems, Journal of Business Research, Annals of Operations Research, IEEE Journal of Biomedical and Health Informatics, Computers & Industrial Engineering etc.

Sutong Wang is currently an Associate Researcher (Full-time Research) at Business School, Sichuan University, Chengdu, China. He received the M.S. and Ph.D. degrees in Management Science and Engineering from the Dalian University of Technology (DUT), Dalian, China. His research interests are in medical data mining, multimodal large language models, and explainable artificial intelligence (XAI). He has published more than 20 papers in various international journals including IEEE Transactions on Cybernetics, IEEE Transactions on Industrial Informatics, European Journal of Operational Research, Annals of Operations Research, International Journal of Production Economics, etc.

Dujuan Wang is currently a professor with Business School, Sichuan University, Chengdu, China. She received the B.S. and M.S. degrees in Computer Science and Technology, and the Ph.D. degree in Management Science and Engineering from the Dalian University of Technology (DUT), Dalian, China. Her research interests are in logistics and supply chain management, service operation management and optimization, and machine learning. She has published more than 80 papers in various international journals including Transportation Research Part B, Decision Support Systems, Naval Research Logistics, Omega, European Journal of Operational Research, IEEE Transactions on SMC, International Journal of Production Economics etc.

T.C.E. Cheng is Dean of PolyU Business School, Fung Yiu King - Wing Hang Bank Professor in Business Administration, and Chair Professor of Management at The Hong Kong Polytechnic University. He obtained a B.Sc.[Eng] (first class honours) from the University of Hong Kong; an M.Sc. from the University of Birmingham, U.K.; and a Ph.D. and an Sc.D. from the University of Cambridge, U.K. His research interests are in Information Systems Management, Operations Management and Operations Research. He has published over 1000 SCI/SSCI papers in such journals as California Management Review, Journal of Operations Management, Management Science, MIS Quarterly, Operations Research, Organization Science, and Production and Operations Management.
