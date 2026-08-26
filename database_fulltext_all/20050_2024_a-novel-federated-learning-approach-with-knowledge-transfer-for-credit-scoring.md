---
otero_id: 20050
otero_key: "GEJ2U4CB"
title: "A novel federated learning approach with knowledge transfer for credit scoring"
authors: "Zhongyi Wang; Jin Xiao; Lu Wang; Jianrong Yao"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.114084"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel federated learning approach with knowledge transfer for credit scoring

![](/api/attachments/GEJ2U4CB/fulltext/images/819ebf7dd7bf44b60e8accca9e8cece702ebc00fdbf01ad6ba7b4d0b253ccf86.jpg)

Zhongyi Wang <sup>a</sup>, Jin Xiao <sup>a</sup>, Lu Wang <sup>b</sup>, Jianrong Yao

<sup>a</sup> Business School, Sichuan University, Chengdu, Sichuan 610064, China

<sup>b</sup> School of Information Management and Artificial Intelligence, Zhejiang University of Finance and Economics, Hangzhou 310018, China

## A R T I C L E I N F O

Keywords: Credit scoring Data privacy Federated learning Knowledge transfer

## A B S T R A C T

The expanding availability of data in the financial sector promises to take the performance of machine learning models to a new level. However, given the high business value and confidentiality of credit data. the integration of datasets from multiple institutions for credit scoring modeling may result in privacy leakage. Consequently, in this paper, a horizontal federated learning paradigm is used to protect the local private data of each participant and collaborate to train a powerful shared global model. However, in the collaborative training process, het erogeneous data distributions can result in insufficient learning of the model. To overcome this issue, we propose the federated knowledge transfer (FedKT) method, which exploits the advantages of fine-tuning and knowledge distillation to effectively extract generic and specific knowledge from the early lavers and outputs of the global model, respectively, thus improving the learning performance of the local models. We adopt five credit datasets and four performance measures to demonstrate the effectiveness of our proposed method. The experimental results show that the proposed method can securely utilize credit data from different parties to improve the performance of the credit scoring model. This also supports the potential of our proposed method for furthe applications in credit scoring

## 1. Introduction

Credit risk has always accompanied the development of the financial industry and dramatically impacted the health and safety of the financial system. Financial institutions commonly apply credit scoring to mini mize the economic losses resulting from default risk [1]. Credit scoring is an effective tool that can accurately estimate the default risk of cus tomers, which affects critical decision-making such as loan approval and credit risk control in financial institutions. The credit scoring problem can be considered as a classification problem, and its core is to construct a stable and powerful credit scoring model [2,3]. With the flourishing development and widespread application of artificial intelligence tech nology, advanced machine learning algorithms are increasingly employed in credit scoring. Credit scoring models based on machine learning algorithms can convert customer data into a measure of loan repayment ability and extract useful information from historical trans action data to support risk managerial decision-making [4].

Therefore, such credit scoring models are relying on a large amount of training data to achieve good discrimination performance. However, in practice, most financial institutions only possess partial samples because credit transaction information has extremely high commercial value and privacy [5]. And it is difficult to share private data across institutions. This severely limits the performance improvement of credit scoring models. A variety of approaches have been developed to address this limited sample issue, including data augmentation, data fusion, and integrated learning. These approaches can effectively enhance the model performance; however, given the requirements of privacy and confidentiality of credit information, direct data integration may cause privacy leakage [6]. As a result, the application of traditional machine learning methods in credit scoring is somewhat limited. and there is an urgent need for a credit scoring method that allows parties to securely share private data while protecting privacy. In this study, we work to develop such an approach to improve the accuracy of risk decision making, thereby increasing the profitability of financial institutions.

The emergence of federated learning opens up new perspectives for our work. Federated learning [7] is an innovative privacy-preserving machine learning paradigm that is coordinated by a central server, with multiple devices training models collaboratively on respective local data, without the necessity of forming a centralized dataset. It mainly includes two mainstream paradigms, horizontal (expanding samples)

## Z. Wang et al.

Table 1  
Previous works for credit scoring.

<table><tr><td>Author (year)</td><td>Number of datasets</td><td>The best models</td><td>Performance measures</td></tr><tr><td>Dastile et al. [15] (2020)</td><td>2</td><td>RF</td><td>AUC, PCC</td></tr><tr><td>Tian et al. [16] (2021)</td><td>7</td><td>FHQSLM</td><td>G-mean, AUC</td></tr><tr><td>Moscato et al. [17] (2021)</td><td>1</td><td>RF</td><td>AUC, TPR, Accuracy, TNR, G-mean</td></tr><tr><td>Shen et al. [23] (2020)</td><td>2</td><td>LSTM</td><td>AUC, KS</td></tr><tr><td>Gunnarsson et al. [19] (2021)</td><td>10</td><td>XGBoost</td><td>AUC, PG, BS, EMP</td></tr><tr><td>Ala&#x27;raj et al. [25] (2022)</td><td>2</td><td>MP-LSTM</td><td>Accuracy, AUC, H-measure, KS, Brier-score</td></tr><tr><td>Wu et al. [26] (2022)</td><td>1</td><td>MLP-ANN</td><td>Accuracy</td></tr><tr><td>Wang et al. [27] (2022)</td><td>5</td><td>DQN-CMDRF</td><td>TPR, Accuracy, F1-score, AUC</td></tr><tr><td>Abdoli et al. [18] (2023)</td><td>3</td><td>BSAC</td><td>Recall, Specificity, F1-Score, G-mean, AUC</td></tr></table>

and vertical (expanding features) federated learning, based on different perspectives of additional information utilization [8]. Federated Aver aging (FedAvg; [7]), the most popular horizontal federated learning algorithm, has been successfully employed in production practices. It has been proved that federated learning is an efficient decentralized protocol with the capability to train models utilizing multiple, diverse data [9]. Therefore, from the perspective of data security, we consider applying horizontal federated learning in the field of credit scoring to explore a co-training manner that meets the requirements of data pri vacy and security while realizing effective learning and decision making on credit data from multiple parties.

Furthermore, class imbalance is also a major issue limiting the per formance of credit scoring methods [10]. It generally refers to the skewed label distribution of the dataset [11]. In a federated learning setting, this data distribution may lead to significant differences in the parameters of local models trained by different clients, and the param eters averaging could cause a large drift among the global and local models [12]. Despite its efficient and robust performance, FedAvg re mains incompletely meeting the challenges posed by the Non-IID (nonindependent identical distribution) formed by class imbalance. There fore, it is a challenging problem to improve the performance of the federated model in heterogeneous data distribution.

To overcome the problems mentioned above, we use horizontal federated learning to construct a shareable and reliable credit scoring method without compromising data privacy. Moreover, inspired by finetuning [13] and knowledge distillation [14], we develop a federated knowledge transfer (FedKT) algorithm to better address the challenge of Non-IID credit data formed by class imbalance. Specifically, we use knowledge transfer strategies of fine-tuning and knowledge distillation to optimize the local models so that they can completely learn the knowledge of the global model. The main contributions of our work are listed as follows.

• We propose a distributed privacy-preserving credit scoring method that enables different financial institutions to collaboratively construct a credit scoring model with high performance and robustness while protecting the sensitive information of borrowers.

• We propose the federated knowledge transfer (FedKT) approach to efficiently exploit the generic knowledge and specific knowledge from the global model. The proposed FedKT can avoid insufficient learning of the local models due to class imbalance.

• We empirically evaluate the performance of our method on five credit datasets with four performance measures. The experimental results show the superior performance of the proposed FedKT over benchmark methods, especially in addressing the challenge of class imbalance data distribution.

The rest of the paper is organized as follows. In Section 2, we present a review of the literature and methods related to this work. In Section 3, we depict the details of the proposed FedKT. The experimental settings are described in Section 4. The experimental results and discussion are analyzed in Section 5. Finally, the conclusion is presented in Section 6.

## 2. Related work

In recent years, most researchers focused on credit scoring modeling based on machine learning and deep learning algorithms. Table 1 summarizes previous credit scoring research efforts. As shown in the table, different algorithms were considered for credit scoring. For example, Dastile et al. [15] analyzed the performance of classifiers such as ANN, LR, DT, and RF on credit scoring, and demonstrated that RF performed best. Tian et al. [16] proposed an improved support vector machine model based on a non-quadratic surface approach for credit scoring. Moscato et al. [17] investigated the credit scoring performance of several classifiers under different resampling methods, among which RF outperformed the others. Abdoli et al. [18] proposed a bagging su pervised autoencoder classifier and verified its superior performance on credit scoring tasks on various real-world datasets. Gunnarsson et al. [19] argued that credit scoring models constructed by tree-based algo rithms are superior to deep neural networks. Similarly, the work of [20,21] recommended the use of tree-based models on tabular data.

However, tree-based credit scoring models rely on data analysis combined with manual feature engineering, which requires consider able cost and domain expertise [22]. While deep neural network models excel at processing complex nonlinear relationships and can achieve a decent predictive performance without relying on sophisticated feature engineering [23,24]. Therefore, many researchers have conducted work on credit scoring based on deep neural networks. Shen et al. [23] developed a credit scoring integration model based on the LSTM model and AdaBoost algorithm to address imbalanced datasets. Ala'raj et al. [25] developed a two-stage model based on LSTM to improve the per formance of credit risk prediction. Wu et al. [26] proposed a new financial risk prediction model that combines Z-score and MLP models and proved that it can contribute to the reduction of economic losses. Wang et al. [27] employed a deep reinforcement learning method with the confusion-matrix-based dynamic reward function for credit scoring, and its performance was evaluated on five credit datasets.

It has been shown that the dataset size is also an essential factor in determining the performance of credit scoring methods [28–30]. An increase in the amount of training samples can avoid the reliance on complex modeling methods for credit scoring. However, the modeling methods of credit scoring mentioned above require all data to be centralized on a central server, which fails to protect the security of private data. McMahan et al. [7] first proposed horizontal federated learning, a decentralized machine learning paradigm that trains shared models with the help of private samples with the same features from multiple parties without disclosing privacy. Vertical federated learning was proposed by Hardy et al. [31], which focuses on helping various participants to share their private sample features. Hence, vertical federated learning cannot expand the training samples and requires sample alignment operations on data subjects held by each institution before performing training, which may pose a potential risk to data privacy. For financial institutions in different regions, their business patterns are similar, and therefore the data features collected are usually the same or similar. Horizontal federated learning allows these different financial institutions to securely share their private data to co-construct models and to better leverage data differences and characteristics across regions without centralizing data. Recently, due to its superior perfor mance in terms of sample augmentation and privacy preservation, horizontal federated learning has gained widespread application in the financial field, such as risk evaluation [32], credit card fraud detection [33], and anti-money laundering [34]. There are significant strengths to horizontal federated learning, as well as some challenges, e.g., the training data is heterogeneous or imbalanced across participants. In the work of Zhao et al. [35], the federated averaging algorithm has a sig nificant drop in accuracy on the MNIST and CIFAR-10 datasets with the Non-IID regime.

![](/api/attachments/GEJ2U4CB/fulltext/images/64cecc6d60789c5d476900985240be4fb16905a7d51fdd9f2db7951827d33613.jpg)  
Fig. 1. Schematic view of a single neuron.

In the field of credit scoring, class imbalance has been a prominent issue that poses a significant obstacle to model training [36]. There have been many studies to address the adverse effects of class imbalance. For example, He et al. [37] improved the BalanceCascade method to preprocess credit datasets with different imbalance ratios, enabling the prediction model to sufficiently learn. In the work of Wang et al. [38], three imbalance processing methods, SMOTE, under-sampling, and mixed sampling, were improved to enhance the quality of the financial datasets. Lei et al. [39] designed an IGAN method to generate new mi nority class samples to conquer the imbalance problem in credit data. However, these methods mentioned above are just appropriate for centralized credit scoring methods. The heterogeneous data distribution formed by class imbalance may lead to poor performance when leveraging multi-source training samples.

As a popular technique in many deep learning methods, knowledge transfer is frequently applied to improve the learning performance of neural network models [40,41]. In the context of medical image anal ysis, Tajbakhsh et al. [40] demonstrated the effectiveness of fine-tuning in enhancing the robustness and performance of the convolutiona neural network (CNN). Tzelepi et al. [41] proposed a novel online self knowledge distillation method that aims to improve the performance of deep network models. Experimentally, compared to existing distillation methods, their proposed method has superior performance on five datasets. In this paper, we use knowledge transfer strategies in the decentralized and privacy-preserving context and proposed the feder ated knowledge transfer (FedKT) algorithm to solve the class imbalance problem.

Table 2  
Statistical information of credit datasets.

<table><tr><td>Datasets</td><td>Samples</td><td>Imbalance ratio</td><td>Clients</td><td>Models</td></tr><tr><td>Loan Data</td><td>1225</td><td>2.8</td><td>5</td><td>Two-layer MLP (18 hidden units)</td></tr><tr><td>HMEQ</td><td>5960</td><td>4.01</td><td>10</td><td>Two-layer MLP (36 hidden units)</td></tr><tr><td>Taiwan</td><td>30,000</td><td>3.52</td><td>30</td><td>Two-layer MLP (56 hidden units)</td></tr><tr><td>GMSC</td><td>150,000</td><td>13.96</td><td>50</td><td>Two-layer MLP (48 hidden units)</td></tr><tr><td>HC</td><td>307,511</td><td>11.39</td><td>70</td><td>Two-layer MLP (216 hidden units)</td></tr></table>

## 3. Methodology

In this section, we start by introducing the problem formulation of credit scoring. Subsequently, we present the basic idea of a traditional neural network for credit scoring as background. Finally, the proposed FedKT method is described in detail.

## 3.1. Problem formulation

As previously described, the purpose of collaborative credit scoring is to utilize training data from multiple sources to distinguish the credit worthiness of borrowers. Therefore, in the real world, collaborative credit scoring is a dynamic decision-making process. Without loss of generality, we first assume that the multi-source training data is held by K clients with a trustworthy central server. And each client wants to improve the performance of the credit scoring model through data sharing. We use $D _ { k } = \{ ( x _ { 1 } , y _ { 1 } ) , ( x _ { 2 } , y _ { 2 } ) , . . . , ( x _ { n } , y _ { n } ) \}$ to represent a local data set of n training samples held by client k $( k = 1 , 2 , . . . , K ) , x _ { t } =$ $\left( x _ { t } ^ { 1 } , x _ { t } ^ { 2 } , . . . , x _ { t } ^ { m } \right)$ represents the t-th $( t = 1 , 2 , . . . , r$ n) sample of client k with m features, $y _ { t } \in \{ 0 ,$ , 1} represents the label (non-default and default) of sample $x _ { t } .$

The goal of collaborative credit scoring is to train a shared global model over dispersed data by minimizing the objective function $\begin{array} { r } { \begin{array} { r c l } { m i n l ( w ) = } & { \sum _ { k = 1 } ^ { K } P _ { k } l _ { k } ( w ) } \end{array} } \end{array}$ , w represents the model parameter, p represents the participation probability of client k, and $l _ { k } ( \boldsymbol { w } )$ represents the local obiective function of client k. The selected client k trains a local model on its private dataset $D _ { k }$ according to the objective function l (w) and sends the updated model parameters w to the central server for aggregation to form a global model. The probability of default predicted by the iteratively trained global model for a specific loan is ${ \bar { \boldsymbol { y } } } = p ( 1 | { \boldsymbol { x } } )$ Subsequently, a comparison of the predicted default probability with a threshold t is performed to determine whether a borrower is in good or bad creditworthiness. Finally, the loan is approved $\mathrm { i f } p ( 1 | x ) \leq t ,$ other wise it is rejected [19].

![](/api/attachments/GEJ2U4CB/fulltext/images/bb083a6f4b5de7dd5109ab5ce23ee9470249b81d9abd793e9d08007ddd01cd2a.jpg)  
Fig. 2. Schematic view of the proposed FedKT method.

Performance (%) comparison between the non-federated learning methods and FedKT in the IID setting.

<table><tr><td rowspan="2">Datasets</td><td rowspan="2">Measures</td><td colspan="4">Methods</td></tr><tr><td>LR</td><td>RF</td><td>XGB</td><td>FedKT</td></tr><tr><td rowspan="4">Loan Data</td><td>Accuracy</td><td>70.04</td><td>69.94</td><td>68.24</td><td>75.51</td></tr><tr><td>Recall</td><td>86.88</td><td>87.38</td><td>82.34</td><td>95.00</td></tr><tr><td>F1-score</td><td>78.56</td><td>78.96</td><td>77.44</td><td>85.78</td></tr><tr><td>KS</td><td>26.38</td><td>25.41</td><td>24.48</td><td>38.52</td></tr><tr><td rowspan="4">HMEQ</td><td>Accuracy</td><td>80.00</td><td>80.43</td><td>80.64</td><td>86.39</td></tr><tr><td>Recall</td><td>92.70</td><td>92.23</td><td>94.78</td><td>98.21</td></tr><tr><td>F1-score</td><td>87.55</td><td>88.50</td><td>88.89</td><td>91.87</td></tr><tr><td>KS</td><td>36.08</td><td>35.39</td><td>35.83</td><td>50.02</td></tr><tr><td rowspan="4">Taiwan</td><td>Accuracy</td><td>79.42</td><td>79.49</td><td>78.71</td><td>81.96</td></tr><tr><td>Recall</td><td>93.18</td><td>93.65</td><td>91.54</td><td>95.94</td></tr><tr><td>F1-score</td><td>86.86</td><td>86.31</td><td>87.01</td><td>89.22</td></tr><tr><td>KS</td><td>32.07</td><td>34.68</td><td>36.82</td><td>44.83</td></tr><tr><td rowspan="4">GMSC</td><td>Accuracy</td><td>92.55</td><td>92.34</td><td>92.93</td><td>93.65</td></tr><tr><td>Recall</td><td>97.99</td><td>97.76</td><td>98.21</td><td>99.82</td></tr><tr><td>F1-score</td><td>95.62</td><td>95.51</td><td>95.28</td><td>96.62</td></tr><tr><td>KS</td><td>53.37</td><td>54.20</td><td>51.40</td><td>61.39</td></tr><tr><td rowspan="4">HC</td><td>Accuracy</td><td>88.79</td><td>89.00</td><td>88.64</td><td>91.85</td></tr><tr><td>Recall</td><td>94.55</td><td>95.00</td><td>94.29</td><td>100.0</td></tr><tr><td>F1-score</td><td>92.71</td><td>93.83</td><td>92.62</td><td>95.75</td></tr><tr><td>KS</td><td>33.01</td><td>34.40</td><td>33.25</td><td>40.03</td></tr></table>

Note: the highest value for each performance measure is in bold.

## 3.2. Neural network for credit scoring

Classification models based on machine learning have been widely used in credit scoring to discriminate the creditworthiness of loan ap plicants; in addition, more sophisticated neural networks have been developed to improve the accuracy and robustness of credit scoring. Neural network [42] is a predictive model that simulates the structure and function of the central neural system of the human brain. It uses neurons as the unit of information manipulation, and the weight values between neurons represent the strength of the connections. The connection and structure in a neural network reflect how information is represented, transmitted, and calculated in the network, while also being able to adjust its structure to different external conditions. Therefore, neural network models are successfully used to address various nonlinear problems. Fig. 1 shows the schematic view of a single neuron, which is the basic component of a neural network model.

Performance (%) comparison between the non-federated learning methods and FedKT in the Non-IID setting.

<table><tr><td rowspan="2">Datasets</td><td rowspan="2">Measures</td><td colspan="4">Methods</td></tr><tr><td>LR</td><td>RF</td><td>XGB</td><td>FedKT</td></tr><tr><td rowspan="4">Loan Data</td><td>Accuracy</td><td>69.35</td><td>69.20</td><td>69.20</td><td>75.10</td></tr><tr><td>Recall</td><td>86.35</td><td>86.32</td><td>84.50</td><td>95.00</td></tr><tr><td>F1-score</td><td>78.51</td><td>78.24</td><td>76.07</td><td>85.28</td></tr><tr><td>KS</td><td>24.07</td><td>22.75</td><td>23.86</td><td>36.07</td></tr><tr><td rowspan="4">HMEQ</td><td>Accuracy</td><td>79.02</td><td>79.97</td><td>79.40</td><td>86.30</td></tr><tr><td>Recall</td><td>92.47</td><td>91.87</td><td>93.85</td><td>98.94</td></tr><tr><td>F1-score</td><td>86.53</td><td>87.22</td><td>87.75</td><td>91.79</td></tr><tr><td>KS</td><td>35.10</td><td>34.10</td><td>34.13</td><td>50.16</td></tr><tr><td rowspan="4">Taiwan</td><td>Accuracy</td><td>79.61</td><td>79.43</td><td>78.43</td><td>82.68</td></tr><tr><td>Recall</td><td>93.21</td><td>93.52</td><td>91.14</td><td>96.04</td></tr><tr><td>F1-score</td><td>85.98</td><td>85.27</td><td>86.82</td><td>89.60</td></tr><tr><td>KS</td><td>32.74</td><td>31.52</td><td>37.06</td><td>47.05</td></tr><tr><td rowspan="4">GMSC</td><td>Accuracy</td><td>92.56</td><td>92.38</td><td>92.00</td><td>93.50</td></tr><tr><td>Recall</td><td>96.99</td><td>96.76</td><td>97.26</td><td>99.87</td></tr><tr><td>F1-score</td><td>94.63</td><td>94.53</td><td>94.32</td><td>96.59</td></tr><tr><td>KS</td><td>52.63</td><td>54.19</td><td>51.07</td><td>60.74</td></tr><tr><td rowspan="4">HC</td><td>Accuracy</td><td>87.74</td><td>87.96</td><td>87.56</td><td>92.01</td></tr><tr><td>Recall</td><td>94.54</td><td>95.00</td><td>94.26</td><td>100.0</td></tr><tr><td>F1-score</td><td>92.68</td><td>93.81</td><td>92.58</td><td>95.83</td></tr><tr><td>KS</td><td>33.03</td><td>33.95</td><td>33.80</td><td>39.04</td></tr></table>

Note: the highest value for each performance measure is in bold.

where x $( i = 1 , 2 , 3 , . . . , k )$ represents the input signal from other neurons, w<sub>i</sub> $( i = 1 , 2 , 3 , . . . , k )$ represents the connection weight coeffi cient of $x _ { i } ,$ b represents the bias arising from internal factors of the neuron, and $\begin{array} { r } { z = \sum _ { i = 1 } ^ { k } w _ { i } x _ { i } + b } \end{array}$ represents the intermediate result ob tained by the neuron. The output y can be obtained by substituting z into the activation function.

The most commonly used neural network model in credit scoring is the multi-layer perceptron (MLP), which consists of input, hidden, and output layers. Formally, the MLP for credit scoring is performed as follows:

(1) Input data is passed from input layer neurons to hidden layer neurons, and the results are passed to the output layer after a nonlinear transformation.

(2) Calculate the error values between the actual output results and the desired output values, and then pass them backward from the output layer to the hidden layer and the input layer.

(3) Adjust the weight coefficients and thresholds for each layer ac cording to the error values.

(4) Iterate until the minimum error requirement or the number of iterations is satisfied.

The MLP is capable of propagating weights through the network, allowing it to learn the complexities of large datasets by using complex network layers. In addition, the MLP can perform pre-training and transfer learning and has a powerful distributed computing capability, which makes it the most popular training model in the decentralized federated scenario that requires the transmission of model parameters.

## 3.3. Proposed FedKT method

Improving the sample size of training data is critical for credit scoring; however, the direct integration of disparate data sources to train credit scoring models may cause privacy leakage. Considering the re quirements of privacy and confidentiality of credit data, the application of traditional machine learning methods in credit scoring has been somewhat limited. The emergence of federated learning certainly pro vides an effective solution to the above problems.

As a result, we propose a credit scoring method based on the feder ated knowledge transfer (FedKT) algorithm, which aims to securely and effectively utilize multi-party data. Specifically, we utilize horizontal federated learning to construct a decentralized and collaborative credit scoring model without compromising data privacy. As the heteroge neous data distribution resulting from class imbalance may affect the performance of the credit scoring method, we further use knowledge transfer strategies of fine-tuning and knowledge distillation to optimize the local models so that they can adequately benefit from the global model.

## 3.3.1. Knowledge transfer

Fine-tuning [13] is a typical technique to implement transfer learning, which is training a model with a set of pre-trained parameters. A common practice is to replicate the weights from a pre-trained model as the initial parameters of a new model, and then modify the number of

## Z. Wang et al.

![](/api/attachments/GEJ2U4CB/fulltext/images/8541cc6714ace4a6a54079d1b83e3bc91a1ac257efecde1b71620d6cf1aaf13a.jpg)  
Fig. 3. Performance (%) comparison between the benchmark federated methods and FedKT on five datasets with the IID setting.

## Decision Support Systems 177 (2024) 114084

neurons in the last fully connected layer depending on the number of classes in the target dataset, thus finally training a model that is appropriate for the target task.

Generally, the early layers of a network learn generic features, which apply to most classification tasks, while the late layers learn specific detailed features, which apply to the task to be solved at hand. Conse quently, fine-tuning only the last fully connected layer of the network, enables the network to be adapted to the target task and thereby improve its classification performance.

Knowledge distillation [14] allows knowledge from a powerful teacher model to be transferred to a small-sized student model, enabling the student model to approximate the performance of the teacher model. Specifically, the student model is trained using the softmax outputs (soft targets) of the teacher model and the true labels (hard targets) of the data. Therefore, the student model optimizes the following loss function:

$$
L _ {\text { student }} = L _ {\text { hard }} + L _ {\text { soft }} (Q _ {t}, Q _ {s})\tag{1}
$$

$$
Q _ {t} = \frac {\exp (z / T)}{\sum_ {i} \exp (z _ {i} / T)}\tag{2}
$$

where $L _ { h a r d }$ is the cross entropy, $\boldsymbol { L _ { s o f t } }$ is a distillation term that quantifies the distribution difference of the two model's outputs, typically refers to mean-squared error or KL divergence, Q and Q are the outputs of the teacher and student model, z is the logits of the model, and T is a tem perature parameter. This approach can enhance the learning quality of the student model through helpful information from the teacher model. Consequently, the above two knowledge transfer strategies (i.e., finetuning and knowledge distillation) are employed to propose the FedKT algorithm that improves the learning performance and robustness of the federated model.

## 3.3.2. FedKT method

In standard federated learning (FedAvg; [7]), the update of the local model in each round begins with copying all parameters of the global model, and the loss function applies only the local sample's true labels

## Z. Wang et al.

![](/api/attachments/GEJ2U4CB/fulltext/images/26ae34dd2ee7cb4ee3cb2b10b07434441c0ba627cfc6912c82a5c1d790ec81fc.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/20c84ca1fceb7a4367f8c59aa678a1cd25439e4cac83daad38c50132a928d10e.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/31920cdf2066506eb11842d7c4d392f8aa62418fc815220d238a2db3f88db7c1.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/17c05bad1f83493b7fef7da2a529b0a075797572fb2174b7698a5be6cc0a0413.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/8a527b41cb06d181f82c2bc99d43bd6e8080d8d38d8111668a6c6310d0e36899.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/23e7b1f911fec249e19f9e76d3d88d123e5708cb783534cde522d828ba9b36ec.jpg)

## Decision Support Systems 177 (2024) 114084

![](/api/attachments/GEJ2U4CB/fulltext/images/f1e713d5443f9f819bdd90204e0bce8c37152484faa1e5d056502a6021bfaaac.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/a506a09766fc563ea74f24892fe39eb0d3e6365e4bffe1a1446c5f85006dc938.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/092e887236d1346d92765f316985e5da71c29788062e93125bc03a792e3d2af5.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/0a30ebb9d7033b6d4f362b41e15f7112fa50ca77ffd5e88383fc272317000ebc.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/7d6bbf04afed976d1ccc3186b754f634ff1449ed4aecbeb03cf426a8366c3950.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/b49dbde51defd1e2ac237ea77007c42f752e14b7af20994484649cebc462093e.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/07fd8768a0539b3ffc04ba5bc5e3cf5e3d5beb4b2a9653598f4fff291548fc5a.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/4c6ea4710bfa19908755f060319db4bde38d8eae7be8e959ecd03bb19a6bf7f7.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/17bdd5e6588b3d39716d181ec6e65f1454821ad6bf3706b95cbd3831d907f873.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/606b08c4b0f934cfd6a2e6d80e6b809b3da2425eb7b40812608abd98a46efde1.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/c6440b2687e75c0983a024a20f4d5b10dbf7ea5a28943a0f0bf8f28f5f41b031.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/4ae71d0a8a9641fb04953f2fc2af52ac3550a3a843b48fd969597a333d2445b3.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/0cdd2bf33917fa1dec6734417487c72625042df2fe0fe92358203472943e50a4.jpg)

![](/api/attachments/GEJ2U4CB/fulltext/images/bf94bb6d4163c2095c84fb77679b9e12e571596b303d3c5ca119d6b36e6b7334.jpg)  
Fig. 4. Performance (%) comparison between the benchmark federated methods and FedKT on five datasets with the Non-IID setting.

(“hard targets”). The independent local update method will face the data heterogeneity problem as mentioned above, resulting in lower overall training quality. Inspired by fine-tuning and knowledge distillation, we argue that the early layers of the global model can help the local model learn generic knowledge, while the output of the global model provides helpful information (“soft targets”) about the distribution among cate gories. Hence, we use the knowledge transfer approaches, as the local update strategy of clients, so that could enhance the learning ability of the federated model, as shown in Fig. 2.

The detailed process of the proposed method is described in the following steps:

(1) The server broadcasts the current global model parameter $w _ { g } ^ { t }$ to a randomly selected client subset K«N of the total clients.

(2) Each client starts the local updates $( E \ge 1$ epoch) on the early layers of the latest global model (excluding the last fully con nected layers), and uses the outputs of the global model to regularize the local model updates. The local loss function is as follows:

$$
L _ {k} \left(\omega_ {k} ^ {t}\right) = \lambda L _ {\text { hard }} + (1 - \lambda) L _ {\text { soft }} \left(Q _ {g} ^ {k}, Q _ {l} ^ {k}\right)\tag{3}
$$

$$
w _ {k} ^ {t + 1} = w _ {k} ^ {t} - \eta \nabla L _ {k} \left(w _ {k} ^ {t}\right)\tag{4}
$$

where λ is a relative weight parameter, $w _ { k } ^ { t }$ is the local model parameter of the client k for round $t , Q _ { g } ^ { k }$ and $Q _ { l } ^ { k }$ are the probability outputs of the global and local model on the private data of client $k ,$ respectively, η is the learning rate, and $w _ { k } ^ { t + 1 }$ is the updated local model parameter.

(3) The server aggregates the updated local models via Eq. (5) to generate a new global model $w _ { g } ^ { t + 1 }$

$$
w _ {g} ^ {t + 1} = \frac {1}{K} \sum_ {k = 1} ^ {K} w _ {k} ^ {t + 1}\tag{5}
$$

(4) Iterate until the global model converges or the set number of it erations is satisfied.

Table 5  
Average performance (%) of different federated methods in the IID setting.

<table><tr><td rowspan="2">Datasets</td><td rowspan="2">Measures</td><td colspan="4">Methods</td></tr><tr><td>FedAvg</td><td>FedProx</td><td>FedCodl</td><td>FedKT</td></tr><tr><td rowspan="4">Loan Data</td><td>Accuracy</td><td>70.46</td><td>72.36</td><td>71.76</td><td>73.43</td></tr><tr><td>Recall</td><td>88.86</td><td>90.97</td><td>91.32</td><td>95.32</td></tr><tr><td>F1-score</td><td>80.43</td><td>82.60</td><td>82.41</td><td>84.07</td></tr><tr><td>KS</td><td>29.28</td><td>32.16</td><td>33.86</td><td>36.17</td></tr><tr><td rowspan="4">HMEQ</td><td>Accuracy</td><td>82.49</td><td>82.59</td><td>84.42</td><td>84.61</td></tr><tr><td>Recall</td><td>95.72</td><td>96.04</td><td>96.06</td><td>96.22</td></tr><tr><td>F1-score</td><td>89.61</td><td>89.71</td><td>90.68</td><td>90.79</td></tr><tr><td>KS</td><td>43.73</td><td>45.93</td><td>48.59</td><td>48.71</td></tr><tr><td rowspan="4">Taiwan</td><td>Accuracy</td><td>80.65</td><td>80.68</td><td>81.59</td><td>81.86</td></tr><tr><td>Recall</td><td>94.10</td><td>94.33</td><td>94.77</td><td>95.50</td></tr><tr><td>F1-score</td><td>88.32</td><td>88.37</td><td>88.90</td><td>89.12</td></tr><tr><td>KS</td><td>39.88</td><td>39.20</td><td>41.81</td><td>42.38</td></tr><tr><td rowspan="4">GMSC</td><td>Accuracy</td><td>93.42</td><td>93.34</td><td>93.44</td><td>93.52</td></tr><tr><td>Recall</td><td>99.05</td><td>99.06</td><td>98.70</td><td>99.51</td></tr><tr><td>F1-score</td><td>96.57</td><td>96.52</td><td>96.55</td><td>96.61</td></tr><tr><td>KS</td><td>59.03</td><td>59.73</td><td>59.95</td><td>60.04</td></tr><tr><td rowspan="4">HC</td><td>Accuracy</td><td>89.42</td><td>91.21</td><td>90.24</td><td>91.59</td></tr><tr><td>Recall</td><td>96.15</td><td>98.77</td><td>97.80</td><td>99.53</td></tr><tr><td>F1-score</td><td>94.32</td><td>95.38</td><td>94.79</td><td>95.60</td></tr><tr><td>KS</td><td>25.76</td><td>30.47</td><td>32.85</td><td>37.55</td></tr></table>

Note: the highest value for each performance measure is in bold.

Table 6  
Average performance (%) of different federated methods in the Non-IID setting.

<table><tr><td rowspan="2">Datasets</td><td rowspan="2">Measures</td><td colspan="4">Methods</td></tr><tr><td>FedAvg</td><td>FedProx</td><td>FedCodl</td><td>FedKT</td></tr><tr><td rowspan="4">Loan Data</td><td>Accuracy</td><td>70.91</td><td>70.95</td><td>70.70</td><td>72.34</td></tr><tr><td>Recall</td><td>91.82</td><td>91.73</td><td>90.13</td><td>94.31</td></tr><tr><td>F1-score</td><td>82.25</td><td>82.09</td><td>81.64</td><td>83.42</td></tr><tr><td>KS</td><td>28.37</td><td>26.47</td><td>28.70</td><td>28.78</td></tr><tr><td rowspan="4">HMEQ</td><td>Accuracy</td><td>81.32</td><td>81.47</td><td>84.01</td><td>84.39</td></tr><tr><td>Recall</td><td>95.78</td><td>95.75</td><td>96.09</td><td>96.26</td></tr><tr><td>F1-score</td><td>89.04</td><td>89.12</td><td>90.50</td><td>90.72</td></tr><tr><td>KS</td><td>48.71</td><td>44.69</td><td>49.11</td><td>50.79</td></tr><tr><td rowspan="4">Taiwan</td><td>Accuracy</td><td>81.75</td><td>81.49</td><td>82.27</td><td>82.44</td></tr><tr><td>Recall</td><td>94.06</td><td>94.43</td><td>94.74</td><td>95.35</td></tr><tr><td>F1-score</td><td>88.99</td><td>88.88</td><td>89.33</td><td>89.48</td></tr><tr><td>KS</td><td>42.26</td><td>41.95</td><td>44.15</td><td>45.15</td></tr><tr><td rowspan="4">GMSC</td><td>Accuracy</td><td>93.32</td><td>93.17</td><td>93.34</td><td>93.35</td></tr><tr><td>Recall</td><td>98.43</td><td>98.73</td><td>98.78</td><td>99.24</td></tr><tr><td>F1-score</td><td>96.51</td><td>96.41</td><td>96.50</td><td>96.51</td></tr><tr><td>KS</td><td>59.34</td><td>58.89</td><td>59.12</td><td>59.80</td></tr><tr><td rowspan="4">HC</td><td>Accuracy</td><td>89.62</td><td>91.42</td><td>89.61</td><td>91.64</td></tr><tr><td>Recall</td><td>96.27</td><td>98.94</td><td>96.84</td><td>99.41</td></tr><tr><td>F1-score</td><td>94.44</td><td>95.50</td><td>94.37</td><td>95.62</td></tr><tr><td>KS</td><td>26.18</td><td>29.91</td><td>30.67</td><td>37.46</td></tr></table>

Note: the highest value for each performance measure is in bold.

After the completion of training, the proposed FedKT method will provide a shareable global model. The model can be applied to all clients involved in the entire collaborative modeling process, enabling each participant to use the shared model to predict the default risk of local loans.

It is important to note that, there are some limitations of the pro posed FedKT method that require consideration. Our proposed method applies fine-tuning and knowledge distillation techniques, and is therefore only applicable to specific neural network models. On the other hand, horizontal federated learning is not supported for person alized feature engineering, because it requires ensuring that each par ticipant's training data has the same feature dimensions. Therefore, neural network models that can automatically extract important fea tures are more appropriate for the proposed method.

## 4. Experimental design

In this section, we present the experimental settings in detail.

## 4.1. Datasets and model

To comprehensively validate the performance of federated learning algorithms, this study used five credit datasets with different sizes (both small and large datasets) and imbalance ratios. These include the Loan Data, HMEQ, Taiwan, Give Me Some Credit (GMSC), and Home Credit (HC) datasets. Statistical information on these datasets and corre sponding learning models are presented in Table 2.

• Loan Data: The dataset is drawn from the previous work [43], which contains 902 non-default samples and 323 default samples. Each sample includes 14 features (12 continuous features and 2 discrete features), excluding the default label.

• HMEQ: The dataset is obtained from the previous work [44], which contains 4771 non-default samples and 1189 default samples. Each sample includes 12 features (7 continuous features and 5 discrete features), excluding the default label.

• Taiwan: The dataset is obtained from the UCI machine learning re pository [45], which contains 23,364 non-default samples and 6636 default samples. Each sample includes 23 features (14 continuous features and 9 discrete features), excluding the default label.

• GMSC: The dataset is provided by the Kaggle competition, which contains 139,974 non-default samples and 10,026 default samples. Each sample includes only continuous features, excluding the default label.

• HC: The dataset is provided by the Kaggle competition, which con tains 282,686 non-default samples and 24,825 default samples. Each sample includes 120 features (60 continuous features and 60 discrete features), excluding the default label.

To eliminate the effect of different measures between features, the above experiment datasets were preprocessed with normalization, onehot coding, and correlation analysis [46]. Specifically, continuous fea tures were normalized by scaling the features to the range [0, 1]. Cat egorical features were one-hot coded by converting to several dichotomous features. One-hot coding was used to convert categorical features into several dichotomous features. Correlation analysis was employed to eliminate one of the two features with a correlation > 0.97. After preprocessing, the feature dimensions of these datasets are 28, 55, 88, 60, and 316, respectively.

## 4.2. Performance measures

In this study, four performance measures, Accuracy, Recall, F1-score, and KS were adopted to evaluate the discrimination performance of the proposed method.

Accuracy is the proportion of correctly classified samples to the total number of samples in the dataset and is widely used to evaluate classi fication performance. The Recall is the proportion of correctly classified positive samples to the total positive samples in the dataset. F1-score is the harmonic average of precision and recall, and the KS is the maximum difference between the distribution of cumulative events and cumulative non-events. Generally, the larger the Accuracy, Recall, F1-score, and KS values, the better the discriminative performance of the model.

## 4.3. Comparison methods

We compare the performance of our approach with the following methods:

• Non-federated methods, the classic machine learning methods without considering collaborative training, include logistic

IID  
![](/api/attachments/GEJ2U4CB/fulltext/images/9b72e5a6f504b12a0f9723870d5d322b9f10a3452f1773da41f698740db49e99.jpg)

Non-IID  
![](/api/attachments/GEJ2U4CB/fulltext/images/62f8e38133e357650d52823f3077329b0f2bd2995eec5edcee05c75d4a557c30.jpg)  
Fig. 5. Standard deviation of Accuracy on five credit datasets.

Table 7  
Performance (%) of FedKT with varying values of λ in the IID setting.

<table><tr><td>Datasets</td><td>Measures</td><td>0.9</td><td>0.7</td><td>0.5</td><td>0.3</td><td>0.1</td></tr><tr><td rowspan="4">Loan Data</td><td>Accuracy</td><td>68.56</td><td>69.64</td><td>70.08</td><td>73.43</td><td>72.84</td></tr><tr><td>Recall</td><td>87.96</td><td>90.12</td><td>92.33</td><td>95.32</td><td>95.84</td></tr><tr><td>F1-score</td><td>78.43</td><td>80.14</td><td>81.05</td><td>84.07</td><td>84.61</td></tr><tr><td>KS</td><td>33.43</td><td>34.28</td><td>35.01</td><td>36.17</td><td>35.61</td></tr><tr><td rowspan="4">HMEQ</td><td>Accuracy</td><td>82.81</td><td>82.93</td><td>83.01</td><td>84.61</td><td>84.58</td></tr><tr><td>Recall</td><td>94.06</td><td>94.88</td><td>95.18</td><td>96.22</td><td>95.64</td></tr><tr><td>F1-score</td><td>88.52</td><td>88.88</td><td>89.33</td><td>90.79</td><td>90.30</td></tr><tr><td>KS</td><td>44.18</td><td>45.55</td><td>46.86</td><td>48.71</td><td>47.87</td></tr><tr><td rowspan="4">Taiwan</td><td>Accuracy</td><td>79.53</td><td>80.13</td><td>80.75</td><td>81.86</td><td>81.27</td></tr><tr><td>Recall</td><td>93.79</td><td>94.13</td><td>95.08</td><td>95.50</td><td>96.07</td></tr><tr><td>F1-score</td><td>88.00</td><td>88.55</td><td>88.93</td><td>89.12</td><td>89.07</td></tr><tr><td>KS</td><td>40.68</td><td>40.75</td><td>41.73</td><td>42.38</td><td>42.65</td></tr><tr><td rowspan="4">GMSC</td><td>Accuracy</td><td>91.70</td><td>91.46</td><td>92.11</td><td>93.52</td><td>92.78</td></tr><tr><td>Recall</td><td>98.19</td><td>98.72</td><td>98.78</td><td>99.51</td><td>99.12</td></tr><tr><td>F1-score</td><td>95.28</td><td>95.33</td><td>95.59</td><td>96.61</td><td>96.04</td></tr><tr><td>KS</td><td>55.87</td><td>56.92</td><td>57.29</td><td>60.04</td><td>60.12</td></tr><tr><td rowspan="4">HC</td><td>Accuracy</td><td>90.48</td><td>90.95</td><td>91.33</td><td>91.59</td><td>91.55</td></tr><tr><td>Recall</td><td>94.56</td><td>95.09</td><td>96.55</td><td>99.53</td><td>98.82</td></tr><tr><td>F1-score</td><td>94.23</td><td>94.69</td><td>95.31</td><td>95.60</td><td>95.52</td></tr><tr><td>KS</td><td>33.60</td><td>34.54</td><td>35.11</td><td>37.55</td><td>36.61</td></tr></table>

Note: the highest value for each performance measure is in bold.

Table 8  
Performance (%) of FedKT with varying values of λ in the Non-IID setting.

<table><tr><td>Datasets</td><td>Measures</td><td>0.9</td><td>0.7</td><td>0.5</td><td>0.3</td><td>0.1</td></tr><tr><td rowspan="4">Loan Data</td><td>Accuracy</td><td>68.26</td><td>68.65</td><td>69.70</td><td>72.34</td><td>72.76</td></tr><tr><td>Recall</td><td>91.84</td><td>91.95</td><td>92.50</td><td>94.31</td><td>95.00</td></tr><tr><td>F1-score</td><td>79.14</td><td>80.03</td><td>81.47</td><td>83.42</td><td>83.76</td></tr><tr><td>KS</td><td>25.69</td><td>26.12</td><td>27.84</td><td>28.78</td><td>29.28</td></tr><tr><td rowspan="4">HMEQ</td><td>Accuracy</td><td>82.47</td><td>83.94</td><td>83.55</td><td>84.39</td><td>83.97</td></tr><tr><td>Recall</td><td>93.26</td><td>93.75</td><td>94.60</td><td>96.26</td><td>95.46</td></tr><tr><td>F1-score</td><td>88.11</td><td>88.89</td><td>89.94</td><td>90.72</td><td>90.87</td></tr><tr><td>KS</td><td>48.11</td><td>48.89</td><td>48.94</td><td>50.79</td><td>49.87</td></tr><tr><td rowspan="4">Taiwan</td><td>Accuracy</td><td>81.10</td><td>81.54</td><td>82.12</td><td>82.44</td><td>82.20</td></tr><tr><td>Recall</td><td>94.75</td><td>95.23</td><td>95.33</td><td>95.35</td><td>96.10</td></tr><tr><td>F1-score</td><td>88.97</td><td>89.07</td><td>89.22</td><td>89.48</td><td>89.80</td></tr><tr><td>KS</td><td>38.39</td><td>40.48</td><td>41.50</td><td>45.15</td><td>43.38</td></tr><tr><td rowspan="4">GMSC</td><td>Accuracy</td><td>92.16</td><td>92.47</td><td>92.73</td><td>93.35</td><td>92.87</td></tr><tr><td>Recall</td><td>98.57</td><td>98.60</td><td>98.60</td><td>99.24</td><td>99.57</td></tr><tr><td>F1-score</td><td>94.16</td><td>94.38</td><td>95.25</td><td>96.51</td><td>95.91</td></tr><tr><td>KS</td><td>56.35</td><td>56.47</td><td>57.52</td><td>59.80</td><td>59.82</td></tr><tr><td rowspan="4">HC</td><td>Accuracy</td><td>90.57</td><td>90.63</td><td>91.16</td><td>91.64</td><td>91.00</td></tr><tr><td>Recall</td><td>96.44</td><td>97.44</td><td>97.81</td><td>99.41</td><td>99.00</td></tr><tr><td>F1-score</td><td>94.37</td><td>94.59</td><td>95.41</td><td>95.62</td><td>95.56</td></tr><tr><td>KS</td><td>30.35</td><td>32.24</td><td>33.57</td><td>37.46</td><td>36.80</td></tr></table>

Note: the highest value for each performance measure is in bold.

## Z. Wang et al.

Table 9  
Friedman test results of the performance ranking in the IID setting.

<table><tr><td>Methods</td><td>Accuracy</td><td>Recall</td><td>F1-score</td><td>KS</td><td>Average Rank</td></tr><tr><td>FedAvg</td><td>6.33</td><td>6.33</td><td>6.00</td><td>6.33</td><td>6.25</td></tr><tr><td>FedProx</td><td>4.67</td><td>4.33</td><td>4.67</td><td>5.33</td><td>4.75</td></tr><tr><td>FedCodl</td><td>4.00</td><td>4.33</td><td>4.33</td><td>3.33</td><td>4.00</td></tr><tr><td>FedKT</td><td>1.67</td><td>1.67</td><td>1.67</td><td>1.67</td><td>1.67</td></tr><tr><td>Statistics of the Friedman test</td><td>16.00</td><td>15.40</td><td>16.00</td><td>15.40</td><td></td></tr><tr><td>P-value</td><td>0.003</td><td>0.004</td><td>0.003</td><td>0.004</td><td></td></tr></table>

Note: the best ranking values are in bold; the alpha value is 0.05; the critical value is 3.49.

Table 10  
Friedman test results of the performance ranking in the Non-IID setting.

<table><tr><td>Methods</td><td>Accuracy</td><td>Recall</td><td>F1-score</td><td>KS</td><td>Average Rank</td></tr><tr><td>FedAvg</td><td>5.33</td><td>5.33</td><td>4.50</td><td>5.00</td><td>5.13</td></tr><tr><td>FedProx</td><td>5.00</td><td>5.00</td><td>5.33</td><td>6.33</td><td>5.42</td></tr><tr><td>FedCodl</td><td>4.67</td><td>4.67</td><td>5.00</td><td>3.67</td><td>4.42</td></tr><tr><td>FedKT</td><td>1.67</td><td>1.67</td><td>1.83</td><td>1.67</td><td>1.71</td></tr><tr><td>Statistics of the Friedman test</td><td>15.20</td><td>15.20</td><td>16.00</td><td>15.40</td><td></td></tr><tr><td>P-value</td><td>0.004</td><td>0.004</td><td>0.003</td><td>0.004</td><td></td></tr></table>

Note: the best ranking values are in bold; the alpha value is 0.05; the critical value is 3.49.

regression (LR; [47]), random forest (RF; [48]), and extreme gradient boosting (XGBoost; [49]).

• FedAvg [7], the first proposed classical federated learning method. It is still an efficient and standard baseline for federated learning research.

• FedProx [50], a minor parameter modification of FedAvg. It force the parameters of the updated local models to be sufficiently approximated to the parameters of the global model.

• FedCodl [51], a new federated optimization algorithm. It adds a distillation loss to the local function to improve the performance of the federated model.

## 4.4. Implementation details

We implemented all the code in PyTorch Version 1.8.1 to simulate a federated scenario with one server and K clients. For the experiment, as these experimental datasets are without the temporal evolution element, we horizontally divided the original dataset into K equal parts according to two different data distribution settings (i.e., IID and Non-IID), rep resenting the K clients involved in the federated aggregation. Specif ically, for the IID setting, we sliced the original dataset depending on the imbalance ratio of each dataset. This ensures a complete label space across clients. For the Non-IID setting, we randomly disrupted and divided the original dataset. This partitioning may result in an incom plete label space for each client's data, especially for datasets with a large ratio of class imbalances.

Furthermore, following the data partitioning approach frequently used in credit scoring, 80% of each client's data was used as the training set, and the remaining 20% as the test set [51]. The non-federated learning models included LR, RF, and XGBoost, which were set with default parameters and optimized by using traditional gradient descent. The multi-laver perceptron (MLP) was applied as the training model for the federated learning methods due to its simple structure, and the hidden layers and units were kept fixed during the training process, as set in Table 2. In all experiments, 30% of the clients were randomly selected to participate in all rounds. For a fair comparison, the randomly selected clients in each round remained fixed across all comparison methods. In each round, the number of training passes in the local updating was set as E = 10, and the cross-entropy was used as the local loss. An SGD solver with a constant learning rate of 0.5 and a momentum of 0.5 was adopted for all federated learning methods. The threshold t was set to 0.5, which is the most commonly used value in credit scoring.

For our proposed FedKT, the mean-squared error (MSE) was employed as the distillation loss, and the temperature parameter in the distillation term was set to 1 since the credit datasets contain only two labels (default and non-default). The relative weight parameter λ in FedKT was set to 0.3, which means that the distillation term has a greater effect relative to the loss term. The performance results reported for all experiments are averaged over 10 times performed with different random seeds, each of which is the average across all client test sets.

## 5. Experimental results and discussion

In this section, we experimentally evaluate the performance of the proposed FedKT in credit scoring.

## 5.1. Performance comparison between the proposed method and the non federated methods

To validate the effectiveness of our proposed method, we evaluated the performance difference between the non-federated models (LR, RF, and XGBoost) and FedKT on five credit datasets, the performance comparison results are shown in Table. 3 and Table 4. For each dataset with two data distribution settings (i.e., IID and Non-IID), we can observe that the proposed FedKT method significantly outperforms all the non-federated methods for most performance measures. In addition, we find that the non-federated learning model LR performs best on most of the datasets.

As can be seen from the Tables, the measure that is significantly improved on all datasets is KS, which improves by 13.32% (Loan Data), 16.06% (HMEQ), 15.53% (Taiwan), 9.99% (GMSC), and 7.02% (HC). The results indicate that the proposed method not only can protect privacy but also can collaboratively utilize the training samples from different data sources to improve the performance of the credit scoring model.

## 5.2. Performance comparison between the proposed method and the benchmark federated methods

To further validate the superior performance of our proposed method, we evaluated the performance difference between the bench mark federated methods (FedAvg, FedProx, and FedCodl) and FedKT on five credit datasets over 50 communication rounds. Fig. 3 and Fig. 4 give the comparison results on the performance of different methods. From the figures, we can observe that the proposed FedKT method has a su perior performance compared to the benchmark federated methods for two data distribution settings. The average performance results over 50 communication rounds are reported in Table 5 and Table 6. We can find that for each dataset, our proposed method outperforms the other federated methods on most of the performance measures.

On the Loan Data dataset with the IID setting (and Non-IID setting), the improved performance measures Accuracy, Recall, F1-score, and KS obtained by the proposed FedKT are 2.97% (1.43%), 6.46% (2.49%), 3.64% (1.17%), and 6.89% (0.41%), respectively, compared with the FedAvg method. On the HMEQ dataset, the improved performance measures of the proposed FedKT are 2.12% (3.07%), 0.50% (0.48%), 1.18% (1.68%), and 4.98% (2.08%), respectively. On the Taiwan data set, the improved performance measures of the proposed FedKT are 1.21% (0.69%), 1.40% (1.29%), 0.80% (0.49%), and 2.50% (2.89%), respectively. On the GMSC dataset, the improved performance measures of the proposed FedKT are 0.10% (0.03%), 0.46% (0.81%), 0.04% (0.00%), and 1.01% (0.46%), respectively. On the HC dataset, the improved performance measures of the proposed FedKT are 2.17% (2.02%), 3.38% (3.14%), 1.28% (1.18%), and 11.79% (11.28%),

## Z. Wang et al.

respectively.

It is worth noting that, for most of the credit datasets with high imbalance ratios, the average performance of the compared methods over all rounds in the Non-IID setting is inferior to that in the IID setting. Moreover, it can be seen that the improvement of the proposed method is even more significant in the IID setting than that in the Non-IID setting. The results indicate that the label distribution skew can strongly affect the performance of the federated models.

In addition, Fig. 5 presents that the standard deviation of Accuracy in our proposed FedKT is consistently the minimum on all credit datasets with IID and Non-IID settings. This shows that our proposed method is more stable in terms of Accuracy oscillation compared to the compared methods. Given this result, it is demonstrated that FedKT transfers knowledge between global and local models, ensuring that the trained model achieves better generalization capability while averaging models directly introduces considerable uncertainty into the performance of the trained model. In conclusion, the empirical results indicate the effec tiveness of our proposed FedKT in improving discrimination perfor mance, especially for coping with heterogeneous credit data formed by class imbalance.

## 5.3. Parameter sensitivity test results

The critical parameter of our proposed method that affects perfor mance is the relative weight parameter λ. As described by our proposed method, a smaller value of the relative weight parameter results in a larger impact of the knowledge distillation term on the model training. To prove the effect of the relative weight parameter on our proposed method, we tested varying values of λ selected from {0.1, 0.3, 0.5, 0.7, 0.9}. As shown in Tables 7 and 8, the performance of our proposed method improves gradually with smaller parameter values under both data distributions (i.e., IID and Non-IID), where the highest value for each performance measure is in bold. The results demonstrate that the more significant the effect performed by the knowledge transfer in FedKT, the more external knowledge can be learned by the training process, thus improving the overall performance.

## 5.4. Significance test results

In this experiment, we performed a non-parametric test to investi gate the statistical significance of the performance differences between the above methods. Specifically, we adopted the Friedman test, which is a non-parametric test to rank the models based on the comprehensive performance of all datasets, as reported in Table 9 and Table 10. The original hypothesis of the Friedman test is that the rank of the models is equivalent, meaning that they do not differ in discrimination perfor mance. According to Lessmann et al. [52], the individual and average rankings of all methods on five credit datasets were calculated.

As shown in Tables 9 and 10, the ranking and average ranking of our proposed method are higher than that of the benchmark federated methods. Furthermore, the statistical value of each performance mea sure is larger than the critical value (3.49), and the p-value of each performance measure is less than the alpha value (0.05), which indicates the original hypothesis is rejected. To sum up, the results prove that our proposed method can significantly improve the performance of the credit scoring method.

## 5.5. Discussion

## 5.5.1. Methodological contributions

This paper proposes a privacy-preserving paradigm to effectively facilitate collaborative credit scoring modeling across participants. The proposed framework is developed for the credit scoring scenario that leverages multi-source training samples, which does not require data providers $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . ,$ , financial institutions such as banks, lending, and pay ment companies) to disclose their private datasets, but only to share the trained model parameters, thereby guaranteeing data security. In addition, the framework applies knowledge transfer strategies for improving the learning performance of the decentralized credit scoring model on credit datasets with class imbalance.

## 5.5.2. Practical implications

With the continued expansion of financial businesses and the up grade of data storage technology, a large amount of data is generated in the industry. The increase in training samples has been demonstrated to improve the discriminative performance of credit scoring methods. However, considering the requirements of privacy and confidentiality of financial data, it is difficult for various financial institutions to securely and effectively share data and collaborate on modeling. The proposed FedKT method can use training samples from multiple participants to more accurately predict the default risk of borrowers while protecting data privacy. This can facilitate large-scale collaborative modeling across different financial institutions to control default risk ratios and reduce financial losses. The empirical results show that our method has better performance in different data distributions (i.e., IID and Non-IID). Particularly, the results in the Non-IID setting indicate the significant advantage of our method in addressing the class imbalance problem. To sum up, our study shows that aggregating multi-source training samples can significantly benefit all parties involved in collaborative modeling, and the application of horizontal federated learning methods can guarantee data are not compromised during the entire process. And it can improve data utilization and alleviate the data island problem in the financial sector.

## 5.5.3. Limitations and further work

There are some limitations to this study that require addressing in future works. In terms of the model, this work just presented a neural network model (MLP) as a federated model example. The main reason is that the horizontal federated learning method we used is not yet sup porting complex feature engineering of private datasets owned by each participant, whereas the performance of the neural network model is not dependent on this operation. In terms of the data, the dataset parti tioning used in the experiments is averaged; this means that each participant possesses an equal sample size of local data, which deviates from the practical scenario. In addition, we considered only one het erogeneous data distribution, i.e., class imbalance. In future work, we try to develop new federated learning methods based on various ma chine learning models to enable better adaptation to credit scoring tasks. Moreover, further work also plans to consider more realistic data par titioning and more types of heterogeneous distribution and focus on the communication overhead and theoretical analysis.

## 6. Conclusion

In this work, a privacy-preserving framework based on horizontal federated learning was considered for credit scoring, and knowledge transfer strategies (i.e., fine-tuning and knowledge distillation) were employed to improve the learning performance of local models. In particular, the fine-tuning strategy extracts the generic knowledge of the global model, while the knowledge distillation extracts the dark knowledge of the global model about the distribution among categories. The novel learning paradigm was found to successfully handle the class imbalance issue that normally occurs in classification tasks. Compared to the non-federated methods (LR, RF, and XGB) and benchmark

## Z. Wang et al.

federated methods (FedAvg, FedProx, and FedCodl), the proposed method showed superior discrimination performance and robustness. This method could assist in the development of a secure credit scoring system for facilitating data sharing among different financial in stitutions, which could improve data utilization and profits.

## CRediT authorship contribution statement

Zhongyi Wang: Writing – original draft, Writing – review & editing, Formal analysis, Investigation, Methodology, Visualization, Validation. Jin Xiao: Writing – review & editing, Formal analysis, Investigation, Methodology. Lu Wang: Conceptualization, Writing – review & editing, Funding acquisition. Jianrong Yao: Conceptualization, Methodology, Formal analysis, Supervision.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant No. 72171160) and the National Leading Talent Culti vation Project of Sichuan University (Grant No. SKSYL2021-03).

## References

[1] J.R. Yao, Z.Y. Wang, L. Wang, M. Liu, H. Jiang, Y.G. Chen, Novel hybrid ensemble credit scoring model with stacking-based noise detection and weight assignment, Expert Syst. Appl. 198 (2022).

[2] F. Shen, X.C. Zhao, G. Kou, Three-stage reject inference learning framework for credit scoring using unsupervised transfer learning and three-way decision theory, Decis. Support. Syst. 137 (2020).

[3] J.R. Yao, Z.Y. Wang, L. Wang, Z.B. Zhang, H. Jiang, S.R. Yan, A hybrid model with novel feature selection method and enhanced voting method for credit scoring, J. Intell, Fuzzy Syst, 42 (2022) 2565–2579.

[4] D. Arnott, G. Pervan, A critical analysis of decision support systems research

[5] H.R. He, Z. Wang, H. Jain, C.Q. Jiang, S.L. Yang, A privacy-preserving decentralized credit scoring method based on multi-party information. Decis. Support. Syst. 166 (2023).

[6] A.I. Canhoto, Leveraging machine learning in the global fight against money laundering and terrorism financing: an affordances perspective, J. Bus. Res. 131 (2021) 441-452.

[7] B. McMahan, E. Moore, D. Ramage, S. Hampson, B.A. Arcas, Communicationefficient learning of deep networks from decentralized data, in: Proceedings of the 20th International Conference on Artificial Intelligence and Statistics, Fort Lauderdale, FL, United States, 2017, pp. 1273–1282.

[8] Q. Yang, Y. Liu, T.J. Chen, Y.X. Tong, Federated machine learning: concept and

[9] V. Mothukuri, R.M. Parizi, S. Pouriyeh, Y. Huang, A. Dehghantanha, G. Srivastava, A survey on security and privacy of federated learning, Fut. Generat. Comp. Syst. Int. J. Esci 115 (2021) 619–640

[10] Y.Z. Kang, N. Jia, R.B. Cui, J. Deng, A graph-based semi-supervised reject inference framework considering imbalanced data distribution for consumer credit scoring, Appl. Soft Comput. 105 (2021).

[11] L. Cleofas-Sanchez, V. Garcia, A.I. Marques, J.S. Sanchez, Financial distress prediction using the hybrid associative memory with translation, Appl. Soft Comput. 44 (2016) 144–152.

[12] Z.Z. Ma, M.Y. Zhao, X.J. Cai, Z.P. Jia, Fast-convergent federated learning with class-weighted aggregation. J. Syst. Archit. 117 (2021).

[13] H. Azizpour, A.S. Razavian, J. Sullivan, A. Maki, S.E. Carlsson. Factors of transferability for a generic ConyNet representation, JEEE Trans, Pattern Anal Mach. Intell. 38 (2016).1790–1802

[14] G. Hinton, O. Vinyals, J. Dean, Distilling the Knowledge in a Neural Network, 2015.

[15] X. Dastile. T. Celik, M. Potsane, Statistical and machine learning models in credit scoring: a systematic literature survey, Appl. Soft Comput. 91 (2020) 106263.

[16] Y. Tian, B. Bian, X.F. Tang, J. Zhou, A new non-kernel quadratic surface approach for imbalanced data classification in online credit scoring, Inf. Sci. 563 (2021) 150–165.

[17] V. Moscato, A. Picariello, G. Sperlí, A benchmark of machine learning approaches for credit score prediction, Expert Syst, Appl, 165 (2021) 113986

[18] M. Abdoli, M. Akbari, J. Shahrabi, Bagging supervised autoencoder classifier for credit scoring, Expert Syst. Appl. 213 (2023).

[19] B.R. Gunnarsson, S. Vanden Broucke, B. Baesens, M. Oskarsd<sup>´</sup> ottir, ´ W. Lemahieu, Deep learning for credit scoring: Do or don't? Eur. J. Oper. Res. 295 (2021) 292–305.

[20] R. Shwartz-Ziv, A. Armon, Tabular data: deep learning is not all you need, Inform. Fusion 81 (2022).

[21] L. Grinsztajn, E. Oyallon, G. Varoquaux, Why do tree-based models still outperform deep learning on tabular data?, in: Thirty-Sixth Conference on Neural Information Processing Systems. 2022

[22] R. Van Belle, B. Baesens, J. De Weerdt, CATCHM: A novel network-based credi card fraud detection method using node representation learning, Decis. Support Syst. 164 (2023).

[23] F. Shen, X. Zhao, G. Kou, F.E. Alsaadi, A new deep learning ensemble credit risk evaluation model with an improved synthetic minority oversampling technique, Appl. Soft Comput. 98 (2020)

[24] C. Luo, D. Wu, D. Wu, A deep learning approach for credit scoring using credit default swaps, Eng. Appl. Artif. Intell. 65 (2017) 465–470.

[25] M. Ala’raj, M.F. Abbod, M. Majdalawieh, L. Jum’a, A deep learning model fo behavioural credit scoring in banks, Neural Comput. Applic. 34 (2022) 5839–5866.

[26] D. Wu, X. Ma, D.L. Olson, Financial distress prediction using integrated Z-score and multilayer perceptron neural networks, Decis. Support. Syst. 159 (2022) 113814.

[27] Y. Wang, Y. Jia, Y. Tian, J. Xiao, Deep reinforcement learning with the confusionmatrix-based dynamic reward function for customer credit scoring, Expert Syst. Appl. 200 (2022).

[28] Y.B. Li, X.M. Wang, B. Djehiche, X.M. Hu, Credit scoring by incorporating dynamic networked information, Eur, J. Oper, Res, 286 (2020) 1103–1112

[29] J.L. Zhou, C. Wang, F. Ren, G.Q. Chen, Inferring multi-stage risk for online consumer credit services: An integrated scheme using data augmentation and model enhancement, Decis. Support. Syst. 149 (2021).

[30] R.Y. Ge, J. Feng, B. Gu, P.Z. Zhang, Predicting and deterring default with socia media information in peer-to-peer lending, J. Manag. Inf. Syst. 34 (2017) 401–424.

[31] S. Hardy, W. Henecka, H. Ivey-Law, R. Nock, G. Patrini, G. Smith, B. Thorne, Private federated learning on vertically partitioned data via entity resolution and additively homomorphic encryption, 2017.

[32] D. Kawa, S. Punyani, P. Nayak, A. Karkera, V. Jyotinagar, Credit risk assessment from combined bank records using federated learning, Int. Res. J. Eng. Technol. 6 (2019)1355–1358

[33] S.S. Waghade. A.M. Karandikar. A comprehensive study of healthcare fraud detection based on machine learning. Int. J. Appl. Eng. Res. 13 (2018) 4175–4178

[34] J. Han, U. Barman, J. Haves, J. Du, E. Burgin, D. Wan, Nextgen aml: Distributed deep learning based language technologies to augment anti money laundering investigation, in: Proceedings of ACL, 2018. System Demonstrations. Association for Computational Linguistics, 2018, pp. 37–42

[35] Y. Zhao, M. Li, L. Lai, N. Suda, D. Civin, V. Chandra, Federated learning with noniid data. arXiv:1806.00582, 2018.

[36] X.-Y. Liu, J. Wu, Z.-H. Zhou, Exploratory undersampling for class-imbalance learning, IEEE Trans. Syst. Man, Cybernet. Part B 39 (2008) 539–550.

[37] H.L. He, W.Y. Zhang, S. Zhang, A novel ensemble method for credit scoring: adaption of different imbalance ratios, Expert Syst. Appl. 98 (2018) 105–117.

[38] L. Wang, Y.G. Chen, H. Jiang, J.R. Yao, Imbalanced credit risk evaluation based on multiple sampling, multiple kernel fuzzy self-organizing map and local accuracy ensemble, Appl. Soft Comput. 91 (2020).

[39] K. Lei, Y.X. Xie, S.R. Zhong, J.C. Dai, M. Yang, Y. Shen, Generative adversaria fusion network for class imbalance credit scoring, Neural Comput. Applic. 32 (2020) 8451–8462

[40] N. Tajbakhsh, J.Y. Shin, S.R. Gurudu, R.T. Hurst, C.B. Kendall, M.B. Gotway, J. M. Liang, Convolutional neural networks for medical image analysis: full training or fine tuning? IEEE Trans. Med. Imaging 35 (2016) 1299–1312

[41] M. Tzelepi, N. Passalis, A. Tefas, Online subclass knowledge distillation, Expert Syst. Appl. 181 (2021).

[42] B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, J. Vanthienen Benchmarking state-of-the-art classification algorithms for credit scoring. J. Oper. Res, Soc, 54 (2003) 627–635

[43] L.C. Thomas, D.B. Edelman, J.N. Crook, Credit Scoring and its Applications, SIAM, 2002.

[44] B. Baesens, D. Rsch, H. Scheule, Credit Risk Analytics: Measurement Techniques, Applications, and Examples in SAS. 2016

[45] A. Asuncion, D. Newman, UCI Machine Learning Repository, 2007.

[46] W.Y. Zhang, H.L. He, S. Zhang, A novel multi-stage hybrid model with enhanced multi-population niche genetic algorithm: an application in credit scoring, Expert Syst. Appl. 121 (2019) 221–232.

[47] J. Berkson. Application of the logistic function to bio-assav. J. Am. Stat. Assoc. 39

[48] L. Breiman, Random forests, Mach, Learn, 45 (2001) 5–32.

[49] T. Chen, C. Guestrin, XGBoost: A scalable tree boosting system, in: Proceedings of the 22nd ACM SIGKDD International Conference, 2016

## Z. Wang et al.

[50] T. Li, A.K. Sahu, M. Zaheer, M. Sanjabi, A. Talwalkar, V. Smith, Federated optimization in heterogeneous networks, Proc. Machine Learn. Syst. 2 (2020) 429–450.

[51] X.M. Ni, X.Y. Shen, H.M. Zhao, Federated optimization via knowledge codistillation, Expert Syst. Appl. 191 (2022).

[52] S. Lessmann, B. Baesens, H.-V. Seow, L.C. Thomas, Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research, Eur. J. Oper. Res, 247 (2015) 124–136

Zhongyi Wang is a PhD student at the School of Business, Sichuan University. His research interests include credit scoring, data mining, machine learning, and federated learning.

Jin Xiao is a Researcher at the School of Business, Sichuan University. His research in terests include artificial intelligence and big data analytics, marketing management,

## Decision Support Systems 177 (2024) 114084

business intelligence, and energy and economic forecasting. He has published in such journals as IEEE Transactions on Neural Networks and Learning Systems, IEEE Trans actions on Industrial Informatics, IEEE Intelligent Systems, Energy, Knowledge-Based Systems, Annals of Operations Research, and many others.

Lu Wang received his Ph.D. degree from Harbin Institute of Technology, China. He is currently a full-time lecturer with the School of Information, Zhejiang University of Finance and Economics, China. His current research interests include credit scoring, data mining, neural network, and pattern recognition.

Jianrong Yao received the B.S. degree from Beijing Normal University, China, in 1987. He is currently a full-time professor with the School of Information, Zhejiang University of Finance and Economics, China. His research interests include credit scoring, information management, business intelligence, business analytics, and data mining.
