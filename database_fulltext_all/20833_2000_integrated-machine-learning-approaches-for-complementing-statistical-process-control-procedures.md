---
otero_id: 20833
otero_key: "765X4K2R"
title: "Integrated machine learning approaches for complementing statistical process control procedures"
authors: "Boo-Sik Kang; Sang-Chan Park"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00063-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrated machine learning approaches for complementing statistical process control procedures

Boo-Sik Kang, Sang-Chan Park <sup>)</sup>

Department of Industrial Engineering, Korea AdÕanced Institute of Science and Technology, 371-1 Kusong-dong, Yusong-gu, Taejon, South Korea

Accepted 24 February 2000

## Abstract

Although statistical process control SPC procedures have played a central role in solving quality problems, theirŽ . effectiveness is yet to be fully realized in the process industry with large volume data, a lot of dimensions of variables, and complex relationships among processes and variables. To complement SPC procedures, we suggest three integrated methods of inductive learning and neural networks for solving the quality problems. First, a feature subset selection method is proposed for reducing variables required for quality control. Second, a clustering inductive learning method is presented for improving the correct prediction rate CPR of inductive learning. Third, a pattern detection method is suggested forŽ . detection of different patterns comparing reference patterns. Three methods are experimented in two datasets. The results show that the three methods are effective for the multivariate process control. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Feature selection; Machine learning; Pattern detection; Multivariate process control

## 1. Introduction

Quality, a critical component of the competitive strategy, is a very important issue in manufacturing industries. A traditional way of achieving and ensuring the set quality standards is via implementing statistical process control SPC procedures. When Ž . the quality of a product is defined by more than one property, all the properties should be studied collectively. Multivariate SPC charts have been developed for this purpose, which are based on the $\chi ^ { 2 }$ statistics or on the Hotelling’s $T ^ { 2 }$ statistics 1 . All of the<sup>w</sup> <sup>x</sup> methods need a multivariate setting, require the assumption of a multivariate normal distribution, and rely heavily on the covariance matrix, whether it be known or estimated from historical data 2 . Most of<sup>w</sup> <sup>x</sup> the processes of the complex industry yield multiple properties of quality and we don’t know the covariance relationships among them beforehand. However, machine learning techniques have the ability to learn from data and to handle uncertain, imprecise, and complex information with a large amount of data.

One way to improve such SPC procedures is to complement them with machine learning methodologies equipped with learning capabilities 3 . Induc-<sup>w</sup> <sup>x</sup> tive learning like C4.5 4 can extract rules easily<sup>w</sup> <sup>x</sup> from the given data, which have a complex correlation with each other. Neural networks can learn complex nonlinear and multivariate relationships among process parameters. In this paper, we suggest three integrated methods of inductive learning and neural networks. First, a feature subset selection method is proposed for reducing variables required for quality control. It can be used for discovering major causal variables in an out-of-control state. Second, a clustering inductive learning method is presented for improving correct prediction rate CPRŽ . of inductive learning. It can be used in predicting output characteristics with a better CPR of inductive learning. Third, a pattern detection method is suggested for detecting different patterns comparing reference patterns. It can be used for detection of abnormal patterns in multivariate process control.

## 2. Inductive learning and neural networks for integrated methods

Inductive learning can extract rules from given data, each of which has a complex correlation with one another. Here we focus on C4.5 4 , which is a<sup>w</sup> <sup>x</sup> typical decision tree generator using top–down approach. It has been applied to several areas including manufacturing 5–7 , database 8 , and marketing 9 .<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> But, it often suffers from being strapped at local optimum and therefore performs poorly in dealing with some hard classification tasks, in which training data are described by high dimensional attribute vectors and the concept to be learned is complex <sup>w</sup> <sup>x</sup> 10 . On the other hand, C4.5 can generate nearly optimal decision trees in handling simple classification tasks. So when we deal with a hard classification task, we want to simplify the task into several simpler subtasks for achieving higher correct classification rate. Jia and Abe 10 suggested a classifier <sup>w</sup> <sup>x</sup> approach that utilizes a clustering method as a preprocessing and a k-nearest neighbor rule as a complementary classifier to C4.5 applied to each cluster. Using the idea of Jia and Abe 10 , we suggest a <sup>w</sup> <sup>x</sup> method clustering given data into some well-separated subsets of the data via a self-organizing feature map SOM model proposed by Kohonen 11 ,Ž . <sup>w</sup> <sup>x</sup> and then applying C4.5.

Neural networks are very useful for pattern recognition, clustering, and quality control 12–17 . Neu-<sup>w</sup> <sup>x</sup> ral networks are attractive tools for quality control due to their ability to process large amounts of data in real-time and their capacity for handling noisy, uncertain or fuzzy process data. Furthermore, neural networks can learn complex nonlinear and multivariate relationships between process parameters. This enables them to be used in the solution of many quality control problems. However, previous works manipulate only a single variable for quality control. We suggest a pattern detection method for detecting different patterns against reference patterns in the case of multivariables. First, we train a reference dataset using SOM, which can cluster the dataset into several groups. Using the grouping information, it can detect datasets having different patterns comparing the reference pattern by the $\chi ^ { 2 }$ test.

In real world applications, the number of features Ž . variables could be very large. Practical machine learning algorithms such as C4.5 are known to degrade in their prediction accuracy when trained on data containing superfluous features 18 . The prob-<sup>w</sup> <sup>x</sup> lem of feature selection is that of finding a subset of major features of a dataset, so that an induction algorithm that is run on data containing only these features generates a classifier with the highest possible accuracy. Feature selection algorithm can be classified as a filter or wrapper, depending on whether it is treated as a preprocess or intertwined with the learning task 19 . While the filter approach is gener-<sup>w</sup> <sup>x</sup> ally computationally more efficient than the wrapper approach, its major drawback is that an optimal selection of features may not be independent of the inductive and representational biases of the learning algorithm that is used to construct the classifier. The wrapper approach 19 , on the other hand, involves the computational overhead of evaluating candidate feature subsets by executing a selected learning algorithm on the dataset represented using each feature subset under consideration. A wrapper approach generally outperforms a filter one because it directly optimizes the evaluation measure of the learning task while removing features, but the time needed to complete the feature selection is much longer than a filter approach 19 . Unfortunately, as shown in Ref.<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 20 , this class of wrapper algorithms turns out to be NP-complete. So we suggest a heuristic algorithm for feature selection in the case of population with large features. The algorithm trains the population via neural networks and ranks all features by the sensitive information of network outputs, and then searches a subset in order of their rank.

## 3. Integrated methods for solving the quality problems

Quality is usually affected by factors of inputs and processes as shown in Fig. 1.

The particular interest of this study suggests integrated machine learning approaches for solving quality problems such as detecting different patterns comparing reference pattern and predicting quality characteristics of outputs using C4.5 in the case of multidimensions of data. For better performance of machine learning approaches, it requires a feature selection method selecting appropriate variables from the original dataset. We introduce three hybrid methods for feature selection, pattern detection and output prediction. Fig. 2 shows the information flow of three hybrid models for solving quality problems.

## 3.1. Feature selection method

This section suggests a heuristic method of the wrapper method for selecting a feature subset of original features as shown in Fig. 3. The algorithm trains the population via back-propagation neural networks 21 with one hidden layer as shown in Fig.<sup>w</sup> <sup>x</sup> 4, ranks all features in descending order as to their effect on the outputs of networks, and selects a subset by wrapper method using the order information.

![](/api/attachments/765X4K2R/fulltext/images/fe46e0ce24a3f42b32942f1bd043d9177ea1cec4050e7f3d8d36ed91c665ae3b.jpg)  
Fig. 1. Quality problems and integrated machine learning approaches.

![](/api/attachments/765X4K2R/fulltext/images/3505cc4cd029a1003e98b9f83be276ac8926bc30621647d43c2c4373c3d94bb7.jpg)  
Fig. 2. Information flows of three hybrid methods for solving quality problems.

In Fig. 4, the k th output pattern, $Y _ { k } ,$ , is determined by Eq. 1 when the network uses a sigmoid functionŽ . as an activation function of hidden and output layers.

$$
\operatorname{Va} \left(Y _ {k}\right) = f \left(\sum_ {j = 1} ^ {p} f \left(\sum_ {i = 1} ^ {n} x _ {i} w _ {i j} + w _ {0 j}\right) w _ {j k} + w _ {0 k}\right),\tag{1}
$$

where $f$ is a sigmoid function.

Output pattern is determined by input pattern presented to the network and the weights of connections between nodes. When attributes of the input pattern are transformed into the normalized interval <sup>w</sup> <sup>x</sup> 0, 1 before training the neural network, the effect of scale between attributes of the input pattern is greatly reduced refer to Eq. 2 , and target network outputŽ Ž .. value is also transformed to interval 0, 1 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/765X4K2R/fulltext/images/a005067f7d7d25ef393b129d1383c6d5f704a1ef81f29a3c9089ec1d56bdf17a.jpg)  
Fig. 3. Feature selection using a wrapper approach via neural networks.

![](/api/attachments/765X4K2R/fulltext/images/d5b1a7805118f838c1d60ac60792ee884ecfa2f7bf9643fa66d6f123210a3b3b.jpg)  
Fig. 4. Topology of a neural network with one hidden layer.

$$
\text { New } x _ {i j} = \left(x _ {i j} - \max x _ {j}\right) / \left(\max x _ {j} - \min x _ {j}\right),\tag{2}
$$

where i is ith input pattern and j is jth attributes Ž . features of input patterns.

The weights of the connections between nodes represent information in the neural network. After training, when an input pattern is presented to the network, associated output is produced. This output pattern represents the actual information held by the network in the input pattern. Sensitive information of tth attribute of the network inputs is defined as the difference between an output value that is generated when all attributes of the network inputs have the same value 0, and an output value that is generated when tth attribute value is 1 and the others are 0. If the sensitive information of the t th attribute is large, it means that the tth attribute has a large effect in the output pattern. When the network input values are widely distributed on the interval 0, 1 and we want<sup>w</sup> <sup>x</sup> to find the sensitive information of the k th attribute in detail, it needs to decompose the interval 0, 1<sup>w</sup> <sup>x</sup> into r-intervals $[ 0 , 1 / r ] , [ 1 / \bar { r } , 2 / r ] , \ldots , [ ( r - 1 ) / r ,$ 1 and repeat it<sup>x</sup> r times to find the sensitive information of the tth attribute. Then the effect of the tth attribute of the network inputs, $X _ { t } ,$ against the output patterns can be defined as Eq. 3 : Ž .

$$
I X _ {t} = \frac {1}{m} \left(\sum_ {k = 1} ^ {m} \sum_ {q = 1} ^ {r} \left| \operatorname{Val} \left(Y _ {k}\right) _ {\mathrm{a}} - \operatorname{Val} \left(Y _ {k}\right) _ {\mathrm{b}} \right|\right),\tag{3}
$$

where $I X _ { t }$ is the effect of tth input node about the output nodes; m is the number of output nodes; Val $( Y _ { k } ) _ { \mathrm { a } }$ is the value of kth output node, $Y _ { k }$ , when input values $X _ { i } = ( 1 / r ) ( q - 1 )$ where $( i = 1 , \ \ldots , \ n$ and $i \neq t )$ , and $X _ { t } = ( 1 / r ) q ;$ and, Val $( Y _ { k } ) _ { \mathfrak { b } }$ is the value of $Y _ { k }$ when input values $X _ { i } = ( 1 / r ) ( q - 1 )$ where $( i = 1 , 2 , \ldots , n )$

$\textstyle { I X _ { t } }$ represents the average value of the sensitive information of all output nodes. The r-value is determined by considering the variance of network input values. If r-value is small, Eq. 3 may catch theŽ . sensitive information in the big interval of inputs. If the r-value is large, then the Eq. 3 can find moreŽ . detailed and sensitive information about the smaller interval of network inputs. The r-value depends on the size and the distribution of input values. Using the sensitive information, this method selects a subset of features by the wrapper approach with the following selecting conditions.

Selecting condition 1: Given an error rate , it selects a subset S of features such that the error rate of S is no more than .

Selecting condition 2: Given two hypothesis that both satisfy selecting condition 1, the simpler one will guess better on future examples by Occam’s razor 22 .<sup>w</sup> <sup>x</sup>

Usually, would be the error rate of all features by the wrapper method. In feature selection via the neural networks FSNN algorithm, feature subset isŽ . selected through two stages. In the first stage, it finds the effect of all features among the network inputs about the outputs and ranks them. In the second stage, it searches a subset that has the smallest number of features among all subsets satisfying the stopping condition. The FSNN algorithm is described as follows.

## 3.1.1. FSNN algorithm

Step 1: Train neural networks with a back propagation algorithm after normalization of network input values by Eq. 2 and calculate the effect of allŽ . features using Eq. 3 .Ž .

Step 2: Rank the features in the descending order, $B _ { 1 } , \ B _ { 2 } , \ . . . , \ B _ { n } ,$ as the effect about outputs. Set the error rate . Set initial value $m = 1$

Step 3: A subset, $\{ B _ { 1 } , \ B _ { 2 } , \ . . . , \ B _ { m } \}$ , is evaluated by an inductive algorithm, C4.5. Let the error rate of the subset be .

Step 4: If is not large than , then the current subset, $\{ B _ { 1 } , \ B _ { 2 } , \ . . . , \ B _ { m } \}$ , is selected and stopped. Otherwise, $m = m + 1$

Step 5: If m is equal to n, then a subset, $\{ B _ { 1 } , B _ { 2 } \}$ $\cdots , \ : \boldsymbol { B } _ { n } \}$ , is selected and stopped. Otherwise, go to step 3.

In the worst case, as the FSNN algorithm searches the feature sets in N times, where N is the number of original features, its complexity is reduced to O NŽ ..

## 3.2. Clustering inductiÕe learning method

This section introduces an integrated method for predicting the output quality as shown in Fig. 5. After the feature selection, the training data with selected features are clustered into several subgroups by SOM. The decision tree for each group is generated by C4.5. The average CPR of decision trees of clustered groups is compared with that of all training data with selected features. Using cross-validation, the decision tree showing better performance is adopted for the rule generation.

![](/api/attachments/765X4K2R/fulltext/images/22a7c2a65b8aec7d17c8c8b7de720bfc0aca7b7dd772ef58d8ff5106eab39f8a.jpg)  
Fig. 5. Clustering inductive learning method.

![](/api/attachments/765X4K2R/fulltext/images/44d455b208f3794e482b9a72ce1be3b3388da3a7bb5321c5e08b232fae9d90b4.jpg)  
Fig. 6. Pattern detection method.

## 3.3. Pattern detection method

The objective of detecting different patterns comparing the reference pattern is to design an early warning system to detect abnormal incidents in manufacturing processes having several dozens or hundreds of control variables. This section proposes a hybrid method of $\textbf { a } ~ \chi ^ { 2 }$ test and SOM, which can cluster groups using the characteristics of data. Fig. 6 presents the framework of this method.

When inputs are learned by SOM, SOM analyzes patterns or information against inputs and yields connection weights between layers. According to the property of SOM, the connection weights involve the information of inputs. Inputs are mapped to the output layer through connection weights of SOM. When two inputs are similar, then the maps of the output layer result in similar patterns. In the case that inputs have a large volume of data, it is difficult to analyze the information of inputs and compare them with each other. As SOM contains the information in connection weights, of which the size is smaller than that of the original data, it is easy to do a comparison among the inputs.

The pattern detection method is composed of three phases; training, pattern generation, and evaluation.

## 3.3.1. Training phase

This phase first subtracts the training dataset, for example, a set of normal process data, from the processes of in-control states. In case the normal dataset is used for a reference dataset, it will include quality characteristics of processes for desirable output. Any dataset can be the reference dataset if it is an example dataset compared with other datasets. Second, the SOM network is trained, and then weights of that are saved.

![](/api/attachments/765X4K2R/fulltext/images/2e4169a8dc2beb7eed59c788b6619f7d12786fc530ba36bbc0d9b0936b33dbd9.jpg)  
Fig. 7. Diagnosing the states of processes.

## 3.3.2. Pattern generation phase

In this phase, several patterns are generated by SOM. First, SOM generates a reference pattern from a reference dataset with fixed weights. The pattern is displayed in a cluster form of N<sup>=</sup>N groups, which include cases clustered by their characteristics. Second, the current pattern is generated from the current dataset through the same operation.

## 3.3.3. EÕaluation phase

The reference pattern is considered as a standard pattern that we shall compare with other patterns. If the current pattern is similar to the reference pattern, we assume that the two datasets are generated from the same states. In case we use a normal dataset as a reference dataset, if the current pattern is not similar to the reference pattern, the current dataset has an abnormal pattern of the out-of-control state. To determine how similar to the reference pattern it is, this phase uses goodness-of-fit test $( \chi ^ { \tt A }$ test; see Appendix A ..

The above procedures can be applied to the process stability control that signals a warning if it demonstrates an abnormal pattern. A pattern detection method can be used for an intelligent quality control system that diagnoses the states of the processes. It starts with a current dataset with selected features attributes from processing data, generates aŽ . pattern through the connection weights of SOM, and tests it by the goodness-of-fit test. And it plots the $\chi ^ { 2 }$ value of the dataset on a control chart. If it is in a state of in-control, it continues its diagnosing operations. But if it is in a state of out-of-control, it generates a warning signal and produces a list of causal variables using the feature ordering method already mentioned in Section 3.1 refer to Fig. 7 .Ž .

Dataset 1 artificial created datasetŽ .  
Rand is the function of random number generation in MS-Excel with uniformly distributed interval 0, 1 .Ž. <sup>w</sup> <sup>x</sup>

<table><tr><td colspan="2">A</td><td colspan="2">B</td><td colspan="2">C</td></tr><tr><td># Cases</td><td>Value</td><td># Cases</td><td>Value</td><td># Cases</td><td>Value</td></tr><tr><td>1–30</td><td>rand × 0.2</td><td>1–37</td><td>rand × 0.25</td><td>1–50</td><td>rand × 0.33</td></tr><tr><td>31–60</td><td>rand × 0.2 + 0.2</td><td>38–74</td><td>rand × 0.25 + 0.25</td><td>51–100</td><td>rand × 0.33 + 0.33</td></tr><tr><td>61–90</td><td>rand × 0.2 + 0.4</td><td>75–112</td><td>rand × 0.25 + 0.5</td><td>101–150</td><td>rand × 0.33 + 0.66</td></tr><tr><td>91–120</td><td>rand × 0.2 + 0.6</td><td>113–150</td><td>rand × 0.25 + 0.75</td><td></td><td></td></tr><tr><td>121–150</td><td>rand × 0.2 + 0.8</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="4">Attributes (features)</td><td colspan="2">Class</td></tr><tr><td colspan="2">D</td><td colspan="2">E</td><td># Cases</td><td>Value</td></tr><tr><td># Cases</td><td>Value</td><td># Cases</td><td>Value</td><td></td><td></td></tr><tr><td>1–75</td><td>rand × 0.5</td><td>1–150</td><td>rand</td><td>1–30</td><td>0.1</td></tr><tr><td>76–150</td><td>rand × 0.5 + 0.5</td><td></td><td></td><td>31–60</td><td>0.3</td></tr><tr><td></td><td></td><td></td><td></td><td>61–90</td><td>0.5</td></tr><tr><td></td><td></td><td></td><td></td><td>91–120</td><td>0.7</td></tr><tr><td></td><td></td><td></td><td></td><td>121–150</td><td>0.9</td></tr></table>

Table 2  
Dataset 2 mini-CorrAl 23 Ž <sup>w</sup> <sup>x</sup>.

<table><tr><td>#</td><td>A0</td><td>A1</td><td>B0</td><td>B1</td><td>I</td><td>C</td><td>Class</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>4</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>5</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>6</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>7</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>8</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>9</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>10</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>11</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>12</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>13</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>14</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>15</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>16</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr></table>

## 4. Experimental procedures and results

## 4.1. Feature selection method

For validation of feature ordering by the weights of trained neural networks, two datasets are chosen in which the first dataset is an artificially created dataset with five features, and the second is mini-CorrAL 23 . Table 1 summarizes dataset 1, which <sup>w</sup> <sup>x</sup> was created artificially. Each attribute is relevant to class in order of A, B, C, D, and E.

Another dataset used for brief validation of feature ordering is in Table 2, which contains 16 instances originally 32 instances of the original Cor-Ž . rAL dataset. This mini-dataset has binary classes, and six Boolean features $( \mathbf { A } _ { 0 } , \ \mathbf { A } _ { 1 } , \ \mathbf { B } _ { 0 } , \ \mathbf { B } _ { 1 } , \ \mathbf { I } , \ \mathbf { C } )$ Where feature I is irrelevant, feature C is correlated to the class label 75% of the time, and the other four features are relevant to the Boolean target concept: $( \mathsf { A } _ { 0 } \setminus \mathsf { Q A } _ { 1 } ) \sim ( \mathsf { B } _ { 0 } \setminus \mathsf { Q B } _ { 1 } )$ 23 .<sup>w</sup> <sup>x</sup>

For threefold cross-validation, dataset 1 is decomposed into three sub-datasets in which each subdataset has 50 cases and classes distributed equally. The experiment uses two sub-datasets for training and one sub-dataset for testing of back-propagation neural networks with five hidden units, five input units, one output unit, and randomized initial weights interval <sup>w</sup> <sup>x</sup> <sup>y</sup>10, 10 . And then it ranks the features as to their sensitive information about outputs using Eq. Ž . 3 with r <sup>s</sup> 30. Table 3 displays the results after the above procedure is repeated three times. The result of the mini-CorrAL dataset is shown in Table 4 when the network has six input units, six hidden units, one output unit, randomized initial weights interval <sup>w</sup> <sup>xy</sup>10, 10 , and r<sup>s</sup>1 because the values ofŽ the attributes of Table 2 are 0 or 1 ..

From the experiments with the two datasets, we think that feature ordering method using the neural networks ranks features very well. Thus, when the information of feature ordering is used for the wrapper method, it is expected to reduce the search space of all features.

For an experiment of FSNN, the PIMA dataset with 768 cases and the Image Segmentation dataset with 2310 cases are chosen 24 . The PIMA problem<sup>w</sup> <sup>x</sup> is to forecast the onset of diabetes mellitus by eight different attributes. The learning task of the PIMA problem is of binary classification, and the class value 1 is interpreted as ‘‘tested positive for diabetes’’.

Table 3  
Results after feature ordering procedure to dataset 1

<table><tr><td rowspan="2">Feature</td><td colspan="4">Sensitive info.</td><td rowspan="2">Weight</td><td rowspan="2">Rank</td></tr><tr><td>1st iteration</td><td>2nd iteration</td><td>3rd iteration</td><td>Average</td></tr><tr><td>A</td><td>0.647</td><td>0.649</td><td>0.531</td><td>0.609</td><td>60.0</td><td>1</td></tr><tr><td>B</td><td>0.146</td><td>0.126</td><td>0.274</td><td>0.182</td><td>17.9</td><td>2</td></tr><tr><td>C</td><td>0.057</td><td>0.120</td><td>0.109</td><td>0.095</td><td>9.4</td><td>3</td></tr><tr><td>D</td><td>0.035</td><td>0.119</td><td>0.114</td><td>0.089</td><td>8.8</td><td>4</td></tr><tr><td>E</td><td>0.025</td><td>0.060</td><td>0.032</td><td>0.039</td><td>3.9</td><td>5</td></tr></table>

Table 4  
Result after feature ordering procedure to mini-CorrAL

<table><tr><td>Rank</td><td>Sens. Info.</td></tr><tr><td>B1</td><td>0.6656</td></tr><tr><td>A1</td><td>0.5259</td></tr><tr><td>A0</td><td>0.2117</td></tr><tr><td>B0</td><td>0.1740</td></tr><tr><td>I</td><td>0.1223</td></tr><tr><td>C</td><td>0.1026</td></tr></table>

In order to demonstrate the effectiveness of the feature selection algorithm, the experiment uses fourfold cross validation. It divides the original dataset with 768 cases into four sub-datasets with 192 cases.

In step 1 of FSNN, the original dataset is transformed into a normalized interval 0, 1 by Eq. 2<sup>w</sup> <sup>x</sup> Ž . and decomposed into four sub-datasets. It uses three sub-datasets for training and one for testing of backpropagation neural networks with 24 hidden units, 8 input units, 1 output unit, and initial random weight interval <sup>w</sup> <sup>x</sup> <sup>y</sup>20, 20 . Then it computes the sensitive information of the attributes of the network inputs in the output pattern using Eq. 3 . This procedure isŽ . repeated four times with a different testing subdataset.

In step 2, the features are ranked in descending order along the average sensitive information. The order is represented to A, F, E, B, G, C, H, D. And let be the average error rate of the pruned decision tree of C4.5 with eight attributes of three training sub-datasets and one testing sub-dataset.

Table 5 summarizes the results of FSNN for PIMA after four iterations of steps 3, 4, and 5. The table provides the accuracy of the pruned decision tree of C4.5 on the testing dataset with and without feature selection. Table 5 shows that feature selection can improve the predictive accuracy of C4.5 and reduce the number of features to be considered. In this section, the particular interest is to select a subset that does not have large a error rate than the other features. Selected features after FSNN are reduced to 4 from 8.

Table 5  
Results of FSNN to the PIMA dataset

<table><tr><td># Test set</td><td>θ with eight features</td><td>ε with selected features</td><td>Feature subset</td></tr><tr><td>1</td><td>28.6</td><td>30.7</td><td>{A,F,E,B}</td></tr><tr><td>2</td><td>32.3</td><td>31.2</td><td></td></tr><tr><td>3</td><td>25.5</td><td>19.8</td><td></td></tr><tr><td>4</td><td>21.4</td><td>22.9</td><td></td></tr><tr><td>Average</td><td>26.95</td><td>26.15</td><td>4</td></tr></table>

Table 6  
Results of FSNN to the image segmentation dataset 38 hidden units, 19 input units, 1 output unit, and initial random weight interval   <sup>y</sup>20, 20 after normalization by Eq. 2 . Ž .

<table><tr><td># Test set</td><td>θ with 19 features</td><td>ε with selected features</td><td>Feature subset</td></tr><tr><td>1</td><td>4.9</td><td>4.8</td><td>{ A19, A16, A18, A14, A8, A15, A2, A7, A17 }</td></tr><tr><td>2</td><td>3.4</td><td>4.4</td><td></td></tr><tr><td>3</td><td>5.6</td><td>4.7</td><td></td></tr><tr><td>Average</td><td>4.63</td><td>4.63</td><td>9</td></tr></table>

The Image Segmentation problem 24 is to clas-<sup>w</sup> <sup>x</sup> sify each instance, which is a 3<sup>=</sup>3 region consisting of nine pixels, into seven classes by 19 continuous attributes.

For demonstration of the feature selection algorithm for Image Segmentation, the experiment uses threefold cross validation. It divides the original dataset with 3210 cases into three sub-datasets with 770 cases.

Table 6 summarizes the results of FSNN for Image Segmentation after nine iterations of FSNN. The table shows the error rate of the pruned decision tree of C4.5 on the testing dataset with and without feature selection. It also shows the selected features of Image Segmentation after FSNN was reduced to 9 from 19. In selecting a subset of all features, FSNN has yielded good results for the PIMA and Image Segmentation problem.

## 4.2. Clustering inductiÕe learning method

For the illustration of clustering inductive learning method, PIMA and Image Segmentation datasets are chosen. Feature selection utilizes FSNN algorithm, of which results are A, F, E, B in PIMA and A19,

A16, A18, A14, A8, A15, A2, A7, A17 in Image Segmentation as already shown in Tables 5 and 6.

With selected features except the class information, SOM clusters each of the two datasets into 2 <sup>=</sup> 2 groups. Of course, the dataset is transformed into a normalized interval 0, 1 by Eq. 2 before   Ž . training. Each case of a dataset belongs to only one group, which has the largest output value as shown in Table 7. The cases of the training dataset in each group are used for generation of decision trees by

C4.5, and testing cases are tested by the decision tree. For comparing performance, cross-validation already used in Section 4.1 is applied. The results of cross-validation of the two datasets are also displayed in Table 7.

When we adopt a strategy that selects the best decision tree from all training data and that of each group, the performance is improved as shown in Table 8, which describes the experimental results of two datasets.

Table 7  
Results of SOM to the PIMA and image segmentation datasets

<table><tr><td>c.v.</td><td>Group</td><td># Train data</td><td># Test data</td><td># Error</td><td>Error rate</td></tr><tr><td colspan="6">(a) PIMA dataset with four selected features</td></tr><tr><td rowspan="5">1st</td><td>(0, 0)</td><td>99</td><td>30</td><td>4</td><td>25.5</td></tr><tr><td>(0, 1)</td><td>178</td><td>51</td><td>15</td><td></td></tr><tr><td>(1, 0)</td><td>200</td><td>74</td><td>8</td><td></td></tr><tr><td>(1, 1)</td><td>99</td><td>37</td><td>22</td><td></td></tr><tr><td>all</td><td>576</td><td>192</td><td>59</td><td>30.7</td></tr><tr><td rowspan="5">2nd</td><td>(0, 0)</td><td>92</td><td>37</td><td>10</td><td>30.2</td></tr><tr><td>(0, 1)</td><td>166</td><td>63</td><td>28</td><td></td></tr><tr><td>(1, 0)</td><td>212</td><td>62</td><td>7</td><td></td></tr><tr><td>(1, 1)</td><td>106</td><td>30</td><td>13</td><td></td></tr><tr><td>all</td><td>576</td><td>192</td><td>60</td><td>31.2</td></tr><tr><td rowspan="5">3rd</td><td>(0, 0)</td><td>105</td><td>24</td><td>6</td><td>24.5</td></tr><tr><td>(0, 1)</td><td>174</td><td>55</td><td>18</td><td></td></tr><tr><td>(1, 0)</td><td>195</td><td>79</td><td>5</td><td></td></tr><tr><td>(1, 1)</td><td>102</td><td>34</td><td>18</td><td></td></tr><tr><td>all</td><td>576</td><td>192</td><td>38</td><td>19.8</td></tr><tr><td rowspan="5">4th</td><td>(0, 0)</td><td>91</td><td>38</td><td>9</td><td>22.4</td></tr><tr><td>(0, 1)</td><td>169</td><td>60</td><td>20</td><td></td></tr><tr><td>(1, 0)</td><td>215</td><td>59</td><td>2</td><td></td></tr><tr><td>(1, 1)</td><td>101</td><td>35</td><td>12</td><td></td></tr><tr><td>all</td><td>576</td><td>192</td><td>44</td><td>22.9</td></tr><tr><td colspan="6">(b) Image Segmentation dataset with nine selected features</td></tr><tr><td rowspan="5">1st</td><td>(0, 0)</td><td>235</td><td>114</td><td>0</td><td>5.5</td></tr><tr><td>(0, 1)</td><td>497</td><td>263</td><td>26</td><td></td></tr><tr><td>(1, 0)</td><td>582</td><td>289</td><td>16</td><td></td></tr><tr><td>(1, 1)</td><td>226</td><td>104</td><td>0</td><td></td></tr><tr><td>all</td><td>1540</td><td>770</td><td>37</td><td>4.8</td></tr><tr><td rowspan="5">2nd</td><td>(0, 0)</td><td>233</td><td>116</td><td>0</td><td>2.2</td></tr><tr><td>(0, 1)</td><td>507</td><td>253</td><td>14</td><td></td></tr><tr><td>(1, 0)</td><td>595</td><td>276</td><td>3</td><td></td></tr><tr><td>(1, 1)</td><td>205</td><td>125</td><td>0</td><td></td></tr><tr><td>all</td><td>1540</td><td>770</td><td>34</td><td>4.4</td></tr><tr><td rowspan="5">3rd</td><td>(0, 0)</td><td>230</td><td>119</td><td>3</td><td>4.3</td></tr><tr><td>(0, 1)</td><td>516</td><td>244</td><td>17</td><td></td></tr><tr><td>(1, 0)</td><td>565</td><td>306</td><td>12</td><td></td></tr><tr><td>(1, 1)</td><td>229</td><td>101</td><td>1</td><td></td></tr><tr><td>all</td><td>1540</td><td>770</td><td>36</td><td>4.7</td></tr></table>

Table 8  
Experimental results of clustering inductive learning method

<table><tr><td rowspan="3">c.v.</td><td colspan="8"># Error</td></tr><tr><td colspan="2">(0, 0)</td><td colspan="2">(0, 1)</td><td colspan="2">(1, 0)</td><td colspan="2">(1, 1)</td></tr><tr><td>All</td><td>Cluster</td><td>All</td><td>Cluster</td><td>All</td><td>Cluster</td><td>All</td><td>Cluster</td></tr><tr><td colspan="9">(a) PIMA dataset</td></tr><tr><td>1st</td><td>7</td><td>4</td><td>23</td><td>15</td><td>8</td><td>8</td><td>21</td><td>22</td></tr><tr><td>2nd</td><td>12</td><td>10</td><td>26</td><td>28</td><td>7</td><td>7</td><td>15</td><td>13</td></tr><tr><td>3rd</td><td>7</td><td>6</td><td>15</td><td>18</td><td>5</td><td>5</td><td>11</td><td>18</td></tr><tr><td>4th</td><td>10</td><td>9</td><td>20</td><td>20</td><td>2</td><td>2</td><td>12</td><td>12</td></tr><tr><td>Sum</td><td>36</td><td>29</td><td>84</td><td>81</td><td>22</td><td>22</td><td>59</td><td>65</td></tr><tr><td>Select</td><td colspan="2">cluster: 29</td><td colspan="2">cluster: 81</td><td colspan="2">cluster, all: 22</td><td colspan="2">all: 59</td></tr><tr><td># Total error</td><td colspan="2">191</td><td colspan="2"></td><td colspan="2"></td><td colspan="2"></td></tr><tr><td># Total test</td><td colspan="2">768 (192 × 4)</td><td colspan="2"></td><td colspan="2"></td><td colspan="2"></td></tr><tr><td>Ave. error rate</td><td colspan="2">24.87</td><td colspan="2"></td><td colspan="2"></td><td colspan="2"></td></tr><tr><td colspan="9">(b) Image Segmentation dataset</td></tr><tr><td>1st</td><td>0</td><td>0</td><td>21</td><td>26</td><td>16</td><td>16</td><td>0</td><td>0</td></tr><tr><td>2nd</td><td>0</td><td>0</td><td>18</td><td>14</td><td>15</td><td>3</td><td>1</td><td>0</td></tr><tr><td>3rd</td><td>1</td><td>3</td><td>20</td><td>17</td><td>14</td><td>12</td><td>1</td><td>1</td></tr><tr><td>Sum</td><td>1</td><td>3</td><td>59</td><td>57</td><td>45</td><td>31</td><td>2</td><td>1</td></tr><tr><td>Select</td><td colspan="2">all: 1</td><td colspan="2">cluster: 57</td><td colspan="2">cluster: 31</td><td colspan="2">cluster: 1</td></tr><tr><td># Total error</td><td colspan="2">90</td><td colspan="2"></td><td colspan="2"></td><td colspan="2"></td></tr><tr><td># Total test</td><td colspan="2">2310 (770 × 3)</td><td colspan="2"></td><td colspan="2"></td><td colspan="2"></td></tr><tr><td>Ave. error rate</td><td colspan="2">3.90</td><td colspan="2"></td><td colspan="2"></td><td colspan="2"></td></tr></table>

Group 1, 1 of PIMA dataset has better perfor-Ž . mance not in the decision tree generated by clustering data but in the one by all training data. So when unseen testing cases are assigned to group 1, 1 ,Ž . Ž . they are passed to the decision tree generated from all training data and others are applied to the decision tree of clusters. Then, the average error rate of clustering inductive learning method after fourfold cross validation is reduced to 24.87 from 26.15 of all training data with four features. In the same way, the average error rate of the Image Segmentation dataset is reduced to 3.9 from 4.63.

The above experiments have showed the clustering inductive learning method of SOM and C4.5 improves the prediction accuracy.

## 4.3. Pattern detection method

Pattern detection method is applied to PIMA and Image Segmentation dataset. PIMA dataset has two classes, class 1 with 268 cases and class 0 with 500 cases. We subtract 10 sub-datasets from PIMA, each of which is composed of 50 cases, and four features selected by FSNN in Section 4.1. Five sub-datasets are extracted from class 1, which are class11, class12, class13, class14 and class15. And five sub-datasets are extracted from class 0, which are class01, class02, class03, class04 and class05. Each sub-dataset is normalized by Eq 2 for the training and generating pattern of SOM. Table 9 shows an example of sub-dataset of PIMA.

Table 9  
A sub-dataset of PIMA with class 1

<table><tr><td rowspan="2">Cases</td><td colspan="4">Attributes</td></tr><tr><td>A</td><td>F</td><td>E</td><td>B</td></tr><tr><td>1</td><td>0.35294</td><td>0.50075</td><td>0.00001</td><td>0.74372</td></tr><tr><td>2</td><td>0.47059</td><td>0.34724</td><td>0.00001</td><td>0.9196</td></tr><tr><td>3</td><td>0.00001</td><td>0.64232</td><td>0.19858</td><td>0.68844</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>50</td><td>0.23529</td><td>0.44262</td><td>0.19858</td><td>0.86935</td></tr></table>

Table 10  
Results of pattern detection method to PIMA Train set: class11, reference pattern of train set: $\left( 0 , 0 \right) = 4 ; \left( 0 , 1 \right) = 3 0 ; \left( 1 , 0 \right) = 6 ; \left( 1 , 1 \right) = 2 8$ Ž ; criteria strength value output value of each . group <sup>s</sup>0.8; and $\chi ^ { 2 } ~ ( 1 , 0 . \dot { 0 } 1 ) = 6 . 6 3 5 .$

<table><tr><td rowspan="2">Test set</td><td colspan="4">Pattern</td><td colspan="4"> $\chi^2$  Statistics</td><td rowspan="2">Result</td></tr><tr><td>(0, 0)</td><td>(0, 1)</td><td>(1, 0)</td><td>(1, 1)</td><td>(0, 0)</td><td>(0, 1)</td><td>(1, 0)</td><td>(1, 1)</td></tr><tr><td>Class11</td><td>4</td><td>30</td><td>6</td><td>28</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>accept</td></tr><tr><td>Class12</td><td>0</td><td>24</td><td>6</td><td>31</td><td>4.348</td><td>3.000</td><td>0.000</td><td>0.731</td><td>accept</td></tr><tr><td>Class13</td><td>2</td><td>30</td><td>4</td><td>29</td><td>1.087</td><td>0.000</td><td>0.758</td><td>0.081</td><td>accept</td></tr><tr><td>Class14</td><td>0</td><td>27</td><td>6</td><td>30</td><td>4.348</td><td>0.750</td><td>0.000</td><td>0.325</td><td>accept</td></tr><tr><td>Class15</td><td>3</td><td>24</td><td>7</td><td>33</td><td>0.272</td><td>3.000</td><td>0.189</td><td>2.029</td><td>accept</td></tr><tr><td>Class01</td><td>3</td><td>19</td><td>1</td><td>16</td><td>0.272</td><td>10.083</td><td>4.735</td><td>11.688</td><td>reject</td></tr><tr><td>Class02</td><td>1</td><td>26</td><td>1</td><td>11</td><td>2.446</td><td>1.333</td><td>4.735</td><td>23.458</td><td>reject</td></tr><tr><td>Class03</td><td>1</td><td>25</td><td>1</td><td>13</td><td>2.446</td><td>2.083</td><td>4.735</td><td>18.263</td><td>reject</td></tr><tr><td>Class04</td><td>2</td><td>30</td><td>3</td><td>11</td><td>1.087</td><td>0.000</td><td>1.705</td><td>23.458</td><td>reject</td></tr><tr><td>Class05</td><td>3</td><td>26</td><td>0</td><td>10</td><td>0.272</td><td>1.333</td><td>6.818</td><td>26.299</td><td>reject</td></tr></table>

Table 10 displays the results of pattern detection using SOM in the PIMA dataset. The experiment selects class11 as a training set, and trains it through SOM with inputs 4, outputs groups 4 and theŽ .

stopping condition is when the sum of the change amounts of each weight is less than 0.1. Once it is trained, it generates output patterns of sub-datasets through SOM with learned weights. Each case belongs to four groups with certain strength 0, 1 the<sup>w</sup> <sup>x</sup> Ž value of the output neurons . When we filter the. cases with a larger strength value than a criteria value, each case may not belong to any group, or may belong to one or more groups according to its strength to groups. The number of cases constituting each group output node is called the pattern of theŽ . sub-dataset. Each pattern is compared with the reference pattern that is generated from the training subdataset. By the goodness-of-fit test, we accept or reject it. The value in each group of pattern in Table 10 illustrates cases belonging to that group with a larger strength value the value of output node than Ž . 0.8. Each case may belong to one or more groups according to its output value. The value in each group of $\chi ^ { 2 }$ statistics is computed by Appendix A. For example, the value of group 0, 0 to class12 isŽ . $( 0 - 4 ) ^ { 2 } / 4 + ( ( 5 0 - 0 ) - ( 5 0 - 4 ) ) ^ { 2 } / ( 5 0 - 4 ) =$ 4.348. When all values in each group of $\chi ^ { 2 }$ statistics is less than $\chi ^ { 2 } ( 1 , 0 . 0 1 ) = 6 . 6 3 5$ , we decide that the sub-dataset is similar to the training sub-dataset with significance level $\alpha = 0 . 0 3 9 4 ( 1 - ( 0 . 9 9 ) ^ { 4 } )$ ..

Table 11  
Results of detection method as varying the criteria strength value Train set: class11, and $\chi ^ { 2 } ~ ( 1 , 0 . 0 \dot { 1 } ) { = } 6 . 6 3 5 .$

<table><tr><td rowspan="2">Criteria</td><td rowspan="2">Test set</td><td rowspan="2">Result</td><td colspan="2">Error</td></tr><tr><td>Type 1</td><td>Type 2</td></tr><tr><td rowspan="3">0.9</td><td>class11, class12, class14, class15</td><td>accept</td><td>0.2</td><td>0.0</td></tr><tr><td>class13</td><td>reject</td><td></td><td></td></tr><tr><td>class01, class02, class03, class04, class05</td><td>accept</td><td>0.0</td><td>1.0</td></tr><tr><td rowspan="2">0.8</td><td>class11, class12, class13, class14, class15</td><td>accept</td><td>0.0</td><td>0.0</td></tr><tr><td>class01, class02, class03, class04, class05</td><td>reject</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="2">0.7</td><td>class11, class12, class13, class14, class15</td><td>accept</td><td>0.0</td><td>0.0</td></tr><tr><td>class01, class02, class03, class04, class05</td><td>reject</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="2">0.6</td><td>class11, class12, class13, class14, class15</td><td>accept</td><td>0.0</td><td>0.0</td></tr><tr><td>class01, class02, class03, class04, class05</td><td>reject</td><td>0.0</td><td>0.0</td></tr></table>

Table 12  
Results of detection method when sub-datasets contain some errors Train set: class11, reference pattern of train set: $\left( 0 , 0 \right) = 4 ; \left( 0 , 1 \right) = 3 0 ; \left( 1 , 0 \right) = 6 ; \left( 1 , 1 \right) = 2 8$ Ž ; criteria strength value output value of each . group <sup>s</sup>0.8; and $\chi ^ { 2 } ~ ( 1 , 0 . 0 1 ) = 6 . 6 3 5 .$

<table><tr><td rowspan="2">Error rate (%)</td><td rowspan="2">Test set</td><td rowspan="2">Judge</td><td colspan="2">Errors</td></tr><tr><td>Type 1</td><td>Type 2</td></tr><tr><td rowspan="2">10</td><td>class11, class12, class13, class14, class15</td><td>accept</td><td>0.0</td><td>0.0</td></tr><tr><td>class01, class02, class03, class04, class05</td><td>reject</td><td></td><td></td></tr><tr><td rowspan="2">20</td><td>class11, class12, class13, class14, class15</td><td>accept</td><td>0.0</td><td>0.0</td></tr><tr><td>class01, class02, class03, class04, class05</td><td>reject</td><td></td><td></td></tr><tr><td rowspan="2">30</td><td>class11, class12, class13, class14, class15</td><td>accept</td><td>0.0</td><td>0.0</td></tr><tr><td>class01, class02, class03, class04, class05</td><td>reject</td><td></td><td></td></tr><tr><td rowspan="2">40</td><td>class11, class12, class13, class14, class15</td><td>accept</td><td>0.0</td><td>0.0</td></tr><tr><td>class01, class02, class03, class04, class05</td><td>reject</td><td></td><td></td></tr></table>

The pattern of each sub-dataset is different as to how it sets the criteria strength value. Table 11 shows the results of each sub-dataset as varying in the criteria strength value. Discrimination between class 0 and 1 is good on the strength interval 0.6,<sup>w</sup> 0.8 for the PIMA dataset. Type 2 error increases in<sup>x</sup> the interval, which is larger than 0.9. Discrimination is based on the interval 0, 0.5 because each group <sup>w</sup> <sup>x</sup> contains every case.

Table 12 illustrates results of the detection method by SOM when sub-datasets contain some errors. Despite errors, the experiment shows that its capability of detecting different patterns is good.

Image Segmentation dataset has seven classes, and each class has 330 cases. Five sub-datasets are formed from a class 1 of the Image Segmentation dataset, each of which is composed of 50 cases with nine major features selected by FSNN in Section 3.1 and named cls11, cls12, cls13, cls14 and cls15, respectively. The same procedures are repeated for the other six classes. Each sub-dataset is normalized before training. Table 13 displays the results of pattern detection using SOM in the Image Segmentation dataset. Discrimination among classes is good on the strength interval 0.8, 0.95 . Most experiments<sup>w</sup> <sup>x</sup> yield good results on the strength value 0.9 according to our expectation, but the two tests are good on different strength values. Though the experiment sets a reference pattern from only one sub-dataset for validation of the detection method, if it uses an average value of some patterns generated from a few sub-datasets for it, a better performance is expected.

Experiments show that the pattern detection method using SOM is effective in discriminating between a reference pattern and other patterns. In the experiments, discrimination ability of the method is good at a certain strength interval. When it is too high, SOM acts sensitively about the small change of the dataset. So, though two datasets are similar, it may be rejected. But, when the strength is too low, the cases belonging to each group are similar to the reference pattern and hence the discrimination ability goes down. Thus, it needs to set the level of proper strength value for each and every application. Thus, some refinements of the pattern detection method are needed according to its application. From the above experiments, the detection of certain patterns using SOM is useful for a large amount of data. In actual situations, there may exist a lot of normal datasets in a process. Thus, the number of reference patterns will be increased along the normal patterns. Since we use each abnormal pattern as a reference pattern, it is ineffective because abnormal patterns have many kinds as their abnormal coefficients are varied. Thus, we recommend this method for applying the detection between normal and abnormal patterns. If a dataset has an abnormal pattern, it needs to discover causal variables of the abnormal pattern. The feature ordering method by Eq. 3 lists them in descending Ž . order of their effect on an abnormal pattern. And then each variable can be tested using existing methods Guh and Hsieh 16 , Hwarng and Hubele 15 ,Ž <sup>w x</sup> <sup>w x</sup> Pham and Oztemel 13 for each single variable.<sup>w</sup> <sup>x</sup>.

Table 13  
Results of detection method to the image segmentation dataset

<table><tr><td>Criteria</td><td>Train set</td><td>Type1 error</td><td>Type2 error</td></tr><tr><td>0.9</td><td>class11</td><td>0.0</td><td>0.0</td></tr><tr><td>0.9</td><td>class21</td><td>0.0</td><td>0.0</td></tr><tr><td>0.9</td><td>class31</td><td>0.0</td><td>0.0</td></tr><tr><td>0.9</td><td>class41</td><td>0.0</td><td>0.0</td></tr><tr><td>0.8</td><td>class51</td><td>0.0</td><td>0.033</td></tr><tr><td>0.9</td><td>class61</td><td>0.0</td><td>0.0</td></tr><tr><td>0.95</td><td>class71</td><td>0.0</td><td>0.0</td></tr></table>

## 5. Discussions

We have suggested three hybrid methods for complementing SPC procedures in the case of multivariate process control. Traditional methods have several limitations to monitor and control the processes with a lot of variables. Multivariate process control complemented with our methods enables SPC procedures to detect different patterns of processes and inputs and predict outputs with higher CPRs. It will be able to find major factors against any out-of-states using a feature ordering method of which the complexity is O N .Ž .

Our methods need to refine their parameters according to their application. And they have to extend to integrate with existing SPC procedures or knowledge-based systems. Once they are used properly, we think that they yield good results for multivariate process control.

## Acknowledgements

The authors like to thank two anonymous referees for their helpful comments on this paper.

## Appendix A

The goodness-of-fit test is to compare the distribution of data between expected cell frequency ref- Ž erence pattern and observed cell frequency current . Ž pattern . Appendix A.1 shows data distribution of . each pattern. There are r groups and n cases of a dataset. Each case belongs to only one group. Frequency $O _ { i }$ is the number of cases belonging to group $\mathbf { G } _ { i }$ of the current pattern, and $O _ { 1 } + O _ { 2 } + \ldots + O _ { r } =$ n.

## A.1. Data obserÕation of each group

$$
\begin{array}{c c c c c c} & \text {Groups of each pattern} & \text {Total} \\ & \mathrm{G} _ {1} & \mathrm{G} _ {2} & \mathrm{G} _ {3} & \dots & \mathrm{G} _ {r} \\ \text {Observed cell frequency (current pattern)} & O _ {1} & O _ {2} & O _ {3} & \dots & O _ {r} & n \\ \text {Expected cell frequency (reference pattern)} & E _ {1} & E _ {2} & E _ {3} & \dots & E _ {r} & n \\ \end{array}
$$

Assume a probability where in a current pattern belongs to group $\mathrm { G } _ { j }$ is $P _ { i 0 } , P _ { 1 0 } + P _ { 2 0 } + . . . + P _ { r 0 } =$ 1. Then the form of a hypothesis test can be formulated as follows:

$$
\begin{array}{l} H _ {0}: \big (P _ {1}, P _ {2}, \ldots , P _ {r} \big) = \big (P _ {1 0}, P _ {2 0}, \ldots , P _ {r 0} \big) \\ H _ {1}: \big (P _ {1}, P _ {2}, \ldots , P _ {r} \big) \neq \big (P _ {1 0}, P _ {2 0}, \ldots , P _ {r 0} \big). \end{array}
$$

The expected cell frequency would be $E _ { i } = n P _ { i } $ for each cell and the observed cell frequency:

$$
\chi^ {2} = \sum_ {i = 1} ^ {r} \frac {\left(O _ {i} - E _ {i}\right) ^ {2}}{E _ {i}}\tag{A - 1}
$$

would be $O _ { i } = n P _ { i 0 }$ . The test statistics for goodnessof-fit test are given as follows:

The df associated with the test statistics processing r groups equal Ž . r <sup>y</sup> 1 . The rejection region of null hypothesis is $\chi ^ { 2 } \geq \chi ^ { 2 } ( ( r - 1 )$ .  ,  ,  is the significance level.

## References

<sup>w</sup> <sup>x</sup> 1 T. Kourti, J.F. Macgregor, Multivariate SPC methods for process and product monitoring, J. Qual. Technol. 28 4Ž . Ž . 1996 409–428.

<sup>w</sup> <sup>x</sup> 2 R.L. Mason, C.W. Champ, N.D. Tracy, S.J. Wierda, J.C. Young, Assessment of multivariate process control techniques, J. Qual. Technol. 29 2 1997 140–143.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 D.T. Pham, E. Oztemal, Intelligent Quality Systems, Springer, Great Britain, London, 1996.

<sup>w</sup> <sup>x</sup> 4 J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

<sup>w</sup> <sup>x</sup> 5 S.C. Park, N. Raman, M.J. Shaw, Adaptive scheduling in dynamic flexible manufacturing systems: a dynamic rule selection approach, IEEE Trans. Rob. Autom. 13 4 1997Ž . Ž . 486–502.

<sup>w</sup> <sup>x</sup> 6 B.S. Kang, J.H Lee, C.K. Shin, S.J. Yu, S.C. Park, Hybrid machine learning system for integrated yield management in semiconductor manufacturing, Expert Syst. Appl. 15 1998Ž . 123–132.

<sup>w</sup> <sup>x</sup> 7 B.S. Kang, D.H. Choe, S.C. Park, Intelligent process control in manufacturing industry with sequential processes, Int. J. Prod. Econ. 60–61 1999 583–590.Ž .

<sup>w</sup> <sup>x</sup> 8 F. Esposito, D. Malerba, V. Ripa, G. Semeraro, Discovering causal rules in relational databases, Appl. Artif. Intell. 11 Ž .1997 71–83.

<sup>w</sup> <sup>x</sup> 9 T. Terano, Y. Ishino, Interactive knowledge discovery from marketing questionnaire using simulated breeding and inductive learning methods, 2nd Int. Conf. Knowl. Discovery Data Min. 1996 279–282.Ž .

<sup>w</sup> <sup>x</sup> 10 J. Jia, K. Abe, Improvements of decision tree generation by using instance-based learning and clustering method, in: IEEE International Conference on Systems Man, and Cybernetics Oct. 14–17, 1996, pp. , 696–701.

<sup>w</sup> <sup>x</sup> 11 T. Kohonen, Self-organizing map, Proc. IEEE 9 1990 Ž . 1464–1480.

<sup>w</sup> <sup>x</sup> 12 A. Al-Ghanim, An unsupervised learning neural algorithm for identifying process behavior on control charts and a comparison with supervised learning approaches, Comput. Ind. Eng. 32 3 1997 627–639.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 D.T. Pham, E. Oztemel, Control chart pattern recognition using learning vector quantization networks, Int. J. Prod. Res. 32 3 1994 721–729.Ž . Ž .

14 S.J. Yu, S.C. Park, Application of the TQM theory to the material quality management: augmented by the self-organizing map, 14th Int. Conf. Prod. Res. 1997 1220–1224.Ž .

<sup>w</sup> <sup>x</sup> 15 H.B. Hwarng, N. Hubele, Back-propagation pattern recognizers for x-bar control charts : methodology and performance, Comput. Ind. Eng. 24 2 1993 219–235.Ž . Ž .

<sup>w</sup> <sup>x</sup>16 R. Guh, Y. Hsieh, A neural work based model for abnormal pattern recognition of control charts, Comput. Ind. Eng. 36 Ž . 1999 97–108.

<sup>w</sup> <sup>x</sup> 17 Y. Guo, K.J. Dooley, Identification of changes structure in statistical process control, Int. J. Prod. Res. 30 1992 1655–Ž . 1669.

<sup>w</sup> <sup>x</sup> 18 H. Liu, H. Motoda Eds. , Feature Extraction, Construction,Ž . and Selection: A Data Mining Perspective, Kluwer Academic Publishing, Norwell, MA, 1998.

<sup>w</sup> <sup>x</sup> 19 R. Kohavi, G.H. John, Wrappers for feature subset selection, Artif. Intell. 97 1–2 1997 273–324.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 S. Davies, S. Russell, NP-completeness of searches for smallest possible feature sets, Proc. 1994 AAAI Fall Symp. Relevance 1994 37–39.Ž .

<sup>w</sup> <sup>x</sup> 21 D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representations by error propagation, in: D.E. Rumelhart, J.L. McCleland Eds. , Parallel Distributed Processing Vol. 1 Ž . MIT Press, Cambridge, MA, 1986, Chap. 8.

<sup>w</sup> <sup>x</sup> 22 H. Wang, D. Bell, F. Murtagh, Relevance approach to feature subset selection, in: H. Liu, H. Motoda Eds. , FeatureŽ . Extraction, Construction, and Selection: A Data Mining Perspective, Kluwer Academic Publishing, Norwell, MA, 1998.

23 M. Dash, H. Liu, Feature selection methods for classifications, Intell. Data Anal.: Int. J. 1 3 1997 http:Ž . Ž . <sup>rr</sup>wwweast.elsevier.com<sup>r</sup>ida<sup>r</sup>browse<sup>r</sup>0103<sup>r</sup>ida00013<sup>r</sup>article.htm.

<sup>w</sup> <sup>x</sup> 24 C.J. Merz, P.M. Murphy, UCI Repository of Machine Learning Databases, University of California, Department of Information and Computer Science, Irvine, CA, 1996, http:<sup>rr</sup>www.ics.uci.edu<sup>r</sup>mlearn<sup>r</sup>MLRepository.html.

![](/api/attachments/765X4K2R/fulltext/images/7180565ef362c5fd4f43a2960814898744c7cd20e67f6db76fe76aecdea034f7.jpg)

Sang-Chan Park is an Associate Professor at the Department of Industrial Engineering of the Korea Advanced Institute of Science and Technology. He was formerly a faculty member of the School of Business, University of Wisconsin in Madison. He received his MBA degree from the University of Minneapolis, and his PhD degree in MIS from the University of Illinois, Urbana-Champaign. His research interest includes the application of artificial intelligence, especially ma-

chine learning methodologies, to the design of knowledge-based systems for various management principles. He has expanded his research domain into Total Quality Management<sup>r</sup>Quality Information Systems, B2B EC, Data Mining and Educational Technology for the gifted as well. He has contributed papers to the IEEE Transactions on Systems, Man, and Cybernetics, Information Processing and Management, Annals of OR, the European Journal of OR, DSS, International Journal of Technology Management, IIE Transactions, Expert Systems with Applications, International Journal of Production Economics, IEEE Transactions on Robotics & Automation, and IEEE Transactions on Knowledge and Data Engineering.

![](/api/attachments/765X4K2R/fulltext/images/275283f0e69f570b278eee24ac47ec3bc9737d2f6f13c724a8247f0dce5c7df5.jpg)

Boo-Sik Kang is a doctoral student at the Department of Industrial Engineering of the Korea Advanced Institute of Science and Technology. He has over 10 years of work experience in the areas of management information system and data communications at Korea Telecom. He received his MSc degree at Korea Advanced Institute of Science and Technology in 1989. His research interests are in Machine Learning, Data Mining, Electronic Commerce and Total Quality

Management. His recent publications appear in Expert Systems with Applications and International Journal of Production Economics.
