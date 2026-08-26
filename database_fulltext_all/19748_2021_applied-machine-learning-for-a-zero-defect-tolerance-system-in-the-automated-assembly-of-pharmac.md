---
otero_id: 19748
otero_key: "P9FN2ZQN"
title: "Applied machine learning for a zero defect tolerance system in the automated assembly of pharmaceutical devices"
authors: "Sebastian Dengler; Said Lahriri; Emanuel Trunzer; Birgit Vogel-Heuser"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113540"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applied machine learning for a zero defect tolerance system in the automated assembly of pharmaceutical devices

![](/api/attachments/P9FN2ZQN/fulltext/images/cd158d7bd1748bbf4815750f88056cee929206608d98fc59b5e64fad024bce4b.jpg)

Sebastian Dengler <sup>a,b,\*</sup>, Said Lahriri <sup>a</sup>, Emanuel Trunzer <sup>b</sup>, Birgit Vogel-Heuser <sup>b</sup>

<sup>a</sup> Novo Nordisk A/S, Bagsværd, Denmark

<sup>b</sup> Institute of Automation and Information Systems, Technical University of Munich, Garching, Germany

## A R T I C L E I N F O

Keywords: Pharmaceutical manufacturing Quality control Automated manufacturing Ensemble methods Convolutional neural network Support vector machines

## A B S T R A C T

Creating reliable and robust quality control systems that identify process errors while having a low number of false rejects is a considerable challenge in the automated manufacturing industry. Especially in the pharma ceutical industry, where a product’s quality has to be ensured at all costs, a large amount of false rejects is acceptable to guarantee the integrity of all released products. As standard quality control systems mainly perform a binary classification, most of them do not provide insights about the reason behind rejections. As a result, the underlying reason for the rejects, such as degradation in equipment or wrong settings in process parameters, often goes unnoticed. Yet, these systems are based on conservative approaches that incorporate the uncertainties related to the measurement system and process variation such as batch-to-batch variations and assembly tol erances. In this contribution, a new data-driven quality control system is suggested. The system is based on wellestablished machine learning methods that differentiate multiple types of errors in the assembly processes of medical products. Trained on process data. the system's functionality is demonstrated in a pre-study and two rea industrial use cases. Moreover, application-specific differences are discussed. It is shown that for the two use cases and a limited number of batches the system not only detects 100% of all defective products but also limits the number of false rejects to an acceptable amount. In all of the application examples, the system has the potential to be executed as a soft real-time system that allows integration into industrial processes. Moreover, it is shown that the algorithm can present the extracted knowledge in various forms understandable for humans. allowing for more informed decision making.

## 1. Introduction

According to the Good Manufacturing Practice (GMP) regulations. manufacturers of pharmaceutical products need to demonstrate that they are in control of their manufacturing processes at any given time [1]. Much effort is put into establishing quality controls to guarantee the conformance of products and to ensure that no defective products are released. This holds for the manufacturing processes of the actual drug, as well as for additional products, such as injection devices used for self administration of the drug. The generic assembly process of such devices follows the procedure illustrated in Fig. 1. The pen subassembly is moved from station to station, continuously adding new components until the product is completed. For each assembly step, a dedicated and validated quality control (QC) station exists, which tests every assem bled product for defects or process errors that might have occurred during the previous assembly. This procedure is necessary to comply with the GMP standards and make sure no defective products are released. Fully automated manufacturing assembly lines are often interdependent hard- and software systems that influence and control complex physical processes. Consequently, process errors can occur. If an error occurs during an assembly step, the corresponding pen must be scrapped as its quality could be compromised.

Conventional systems for quality monitoring in automated manufacturing lines often do not incorporate data-driven algorithms. Most methods make use of expert systems that, for example, measure whether or not a threshold is exceeded, such as examining if too much or too little force is applied, and items are scrapped whenever a rule is violated according to the assembly process specifications. Sometimes the values are measured by the same station that executes the actual assembly step. However, in some cases, vision systems or whole stations with the only purpose of checking if the previous assembly step was successfully executed, are implemented. This results in higher complexity of the line and higher cost of acquisition. Conservative quality controls perform a binary classification, as a product can either be “good” or “bad”. This can lead to a high amount of false rejects, a higher scrap rate, and a loss in the overall equipment effectiveness (OEE). Modern manufacturing equipment often contains innovative devices, additional sensors and possibilities for data acquisition, and signal processing, while older lines are often retrofitted to meet new technology standards. Hence, vast amounts of data are generated during the manufacturing process, providing data about the condition and performance of a line. In some cases, components give highly detailed feedback during specific assembly steps in the form of time signals. Existing quality controls often do not employ the full potential of this data, as they are limited to simple, hard-coded rules.

![](/api/attachments/P9FN2ZQN/fulltext/images/ed722996e9f59ff66a0e217a72c14acf086190f2f7c556b594354b638764854c.jpg)  
Fig. 1. Conventional structure of an assembly line. After each assembly step, a quality control system checks whether the assembly step was success fully executed.

Alternatives to these rule-based systems have been explored in research and other industries. Escobar and Morales-Menendez [2], Ribeiro [3] and Lopes and Camarinha-Matos [4] have demonstrated the feasibility of using Machine Learning (ML) algorithms for QC and error recovery in different industrial processes. With respect to the pharma ceutical domain, Chi et al. [5] presented an ML-based decision support system (DSS) to optimize chemical reactions in the production of drugs. This and other DSSs for manufacturing such as [6] are meant for process planning or optimization and thus are not required to perform timecritical tasks. No examples of ML-based QC systems in the pharmaceu tical industry are known to the best knowledge of the authors. Ap proaches for the related problem of time series classification have been suggested by Grabocka et al. [7] and Lines et al. [8]. However, they face exceedingly high computational complexities and thus are not suitable for running in real-time. Furthermore, the approaches do not distinguish between False Negatives (FN) and False Positives (FP) in the wrongly classified items as they are trained to classify datasets with the highest possible accuracy. The high complexity of some of the suggested algo rithms often results in a poor explainability of the models.

To overcome the current drawbacks of conventional QCs in phar maceutical manufacturing plants, state-of-the-art ML algorithms could be employed, capable of extracting rules for differentiating between normal operation and different types of errors. Such a system could give feedback about current events at the line and allow for a more informed troubleshooting process.

Therefore, the contribution of this paper is to propose a data-driven and intelligent QC system based on a combination of ML algorithms. Besides this, the model acts as DSS giving specific feedback about cur rent failures in real-time (in our case below 150 ms), aiding operators in their maintenance efforts. Furthermore, the contribution includes an industrial evaluation of the proposed system for two real applications from the pharmaceutical industry using industrial sensor data.

This work intends to provide ground research and can be viewed as a feasibility study. However, in a wider perspective it provides a potential framework for enabling predictive process monitoring. The latter can be described as a branch of process mining that aims to predict the future development of ongoing cases of a process during runtime based on a history of events [9]. Predictive process monitoring has been applied in the manufacturing domain to improve equipment maintenance [10]. In the context of the presented application, a system could detect deviating behavior in assembly processes and issue early warnings in case of repeating failures.

![](/api/attachments/P9FN2ZQN/fulltext/images/35c5e5f304f3f8b5b7a209c22d812144278e792934edfd19c8cf06e9aa113f1c.jpg)  
Fig. 2. UC 1: assembly station with 20 linear motors.

The overall structure of this paper will be presented as follows. In the next section an outline of our research methodology is given, followed by an introduction to the use cases in Section 3, the description of the systems theoretical background in Section 4 and its composition (Sec tion 5). The proposed QC system is subsequently evaluated with data from the use cases (UCs) in the sixth section. Limitations of the system are discussed in the seventh section and a summary of the results is given in the final part of the paper.

## 2. Research methodology

To assess the research methodology and put our work into the perspective of Information Systems (IS) research it is evaluated against the guidelines for design-oriented research in IS as proposed by Hevner et al. [11]. Our research aims to create an artifact in form of an ML model able to make quality critical decisions and a software prototype as an evaluation step to prove the artifact’s instantiability (Guideline 1). The problem of detecting all defective products or faulty assemblies is especially relevant for the pharmaceutical industry due to the mentioned government regulations (Guideline 2). In our search for a solution we take these regulations into account and utilize ML methods in our solution approach (Guideline 6). In the evaluation section of this article we analyse the performance of our system with help of well known statistical methods and following best practices of data science (Guideline 3). Our research contribution is a data-driven QC system and its application in two real-world UCs (Guideline 4). We take past find ings in the fields of ML and time series classification into account and apply them rigorously in the construction and evaluation of our system (Guideline 5). In the communication of our system’s predictions we put great focus on the algorithms interpretability, such that the results become understandable for academic, managerial as well as quality assurance audience (Guideline 7).

## 3. Industrial use cases

In the following, two UCs are presented, generating the data which the suggested system is later tested on. Both are featuring a station from two different real-world pharmaceutical manufacturing lines, but differ in the executed manufacturing process and the types of data acquired. What distinguishes these manufacturing processes from those of other industries is not the process itself, but the quality control goal. Operating within the pharmaceutical domain, it is required that all faulty products are detected. Here, the uncertainties related to the measurement system together with the batch-to-batch variations acquired from a thorough

![](/api/attachments/P9FN2ZQN/fulltext/images/c1ecd3a183a13372d8783a8c46234bf6e43b630ff11bd9ec7dcf53953d675550.jpg)  
Fig. 3. Schematic drawing (left) and picture (middle) of the test setup (legend: a) linear motor, b) grippers, c) fixture, d) force sensor, and e) the two parts to assemble). Normalized sample data from the pre-study (right).

![](/api/attachments/P9FN2ZQN/fulltext/images/630f45d41ae7b2bcae45b655315f62327d254c874f38a50a3e499c7601df5123.jpg)

Gage Reliability and Reproducibility (Gage R&R) study and the assem bly tolerances are incorporated to calculate the acceptance thresholds.

## 3.1. Use case 1

The first industrial UC covers a process in which two parts of the drug pen are assembled by a linear motor, as depicted in Fig. 2. The station contains 20 linear motors, which all record their position, velocity, and electric current during operation. The cycle time of the overall machine equals 4 s, while the actual assembly sequence takes approximately 1 s. Therefore, quality predictions should be available before the manufac tured parts are indexed to the next station to minimize the processing of faulty parts. For UC 1, the time between the availability of all data and the products leaving the station equals 150 ms, which corresponds to the maximal acceptable time for analysis. This time includes the processing of the data as well as the communication with the line’s PLC. The latter will be neglected in the later analysis.

To study the behavior of the linear motors and to assess the data quality, a test bench has been created to simulate this assembly step under laboratory conditions (cf. Fig, 3. (left) and (middle)). The test bench reflects the same process step and boundary conditions using the same hardware. An additional force transducer was instrumented below the pen fixture to capture the reaction force and correlate it with the current measurements. Experiments were carried out at the test setup to obtain a representative amount of data for normal operation and mul tiple error cases. The aim was to recreate assemblies equivalent to the real ones and simulate common scenarios of unsuccessful assemblies. These scenarios were identified by performing a Failure Mode and Ef fects Analysis (FMEA) and questioning manufacturers, line operators, and process domain experts. Fig. 3 (right) shows all signals gathered during one assembly. It can be seen that the force and current are at least piecewise highly correlated. Especially at stages where the motor does not move and only applies force stationery, it can be observed that both curves have a nearly linear relationship. The current fluctuates strongly in intervals where the motor is moving, as it is used to balance the motor’s acceleration. The current signal is dominated by the inertia of the linear motor when it moves. At the end position, a spike in the force measurement occurs, which is not reflected in the current measure ments. This is due to an ejection process exerted by a separate pneumatic system and not governed by the linear motor. The measured reaction forces provide more details than the current feedback, but for the real assembly line, it might not be possible to equip each nest with additional force transducers. Therefore, despite having recorded the force data on the test setup, the analysis should be limited to the data recorded by the motor to ensure industrial applicability.

![](/api/attachments/P9FN2ZQN/fulltext/images/4fd1ff6851c549bfda05e303aad81d614b18d95444581812a32b4bfaaec3e531.jpg)

After the lab tests, three of the identified failure types could be replicated on the real machine by adjusting the machine settings. Af terward, a large amount of data describing erroneous assemblies was recorded during machine operation. Acquired signals are limited to only between 37 and 41 points per time series. Neither could the velocity feedback be captured as the data was corrupted due to a wrong con version in the PLC.

## 3.2. Use case 2

In the second industrial UC, a pick-and-place unit (PPU) assembles two subassemblies on top of each other (cf. Fig. 4 (left)). The machine records the position of the gripper and the exerted force during each assembly (cf. Fig. 4 (right)). The PPU can assemble two products simultaneously in each machine cycle that lasts 2.4 s. The actual process of mounting the subassembly takes approximately 1.4 s. As for UC 1, the deadline for a quality prediction, including the communication with the

![](/api/attachments/P9FN2ZQN/fulltext/images/233c7ea4deb7a1f2886c11464c2e885e6815b4ce0c3eee24ce074ba5559b7575.jpg)  
Fig. 4. UC 2: picture of PPU (left) with a) position sensors and b) force sensors. Normalized sample data during normal operation (right).

Table 1  
Amount of samples for each dataset grouped by class.

<table><tr><td>Class</td><td>Test bench</td><td>UC 1</td><td>UC 2</td></tr><tr><td>Normal</td><td>502</td><td>830</td><td>9478</td></tr><tr><td>Error 1</td><td>504</td><td>1180</td><td>48</td></tr><tr><td>Error 2</td><td>341</td><td>821</td><td>1261</td></tr><tr><td>Error 3</td><td>571</td><td>1278</td><td>1241</td></tr><tr><td>Error 4</td><td>350</td><td>-</td><td>-</td></tr><tr><td>Total</td><td>2268</td><td>4109</td><td>12,028</td></tr></table>

PL $\mathrm { C } ,$ corresponds to 200 ms. Table 1 shows the number of classes and samples acquired in each of the UCs and the pre-study.

## 3.3. Differences between use cases

The main differences between the UCs are the resolution and the type of time series data. Whereas the first UC has a low sampling frequency of 40 Hz, data in the second UC is recorded with 2 kHz. The underlying hardware can explain this difference: while in UC 1 data is acquired by the machine’s PLC and the priority of data acquisition is low compared to machine control, in UC 2, a separate data acquisition system is part of the line. This separate system reliefs the PLC from data collection and allows higher sampling frequencies.

## 4. Theoretical background

The suggested system is a combination of different common machine learning algorithms. The theoretical background of the individual components is explained in the following.

## 4.1. Process error classification

A classifier, such as quality control, can make two different kinds of errors. FP in which a negative class sample is incorrectly classified as positive merely poses an economic loss. In the context of an assembly line, this is a correctly assembled product that is deemed bad and scrapped (false reject). FN where the system does not detect defective products, have to be strictly avoided. To evaluate the performance of the suggested system, primarily, two metrics will be evaluated. The false negative rate (FNR) and the false positive rate (FPR):

FN False Negative Rate (FNR) = FN + TP

(1)

False Positive $\mathrm { R a t e } \left( \mathrm { F P R } \right) = \frac { \mathrm { F P } } { \mathrm { F P } + \mathrm { T N } }$

(2)

## 4.2. Decision trees

According to Breiman et al. [12], inductive learning models, such as classification and regression trees (CART), can induce new knowledge by learning from examples. Originating from the root node, decision trees (DTs) repeatedly split data according to criteria that maximize the reduction of impurity, a measure for how good a particular split can differentiate between classes. By adding nodes and splits, the dataset is divided into smaller sub-datasets. Consequently, a DT is not more than a list of steps to classify new sample elements. These steps are easily un derstandable and allow for more in-depth insight into the observed process. Thus, DTs can incorporate knowledge and demonstrate it to human users in an understandable way. A disadvantage of DTs is their tendency to overfit. Without defining a maximum tree depth, DTs put too much weight on outliers and thus have a bad generalization. Pruning or setting a maximum depth can counteract this behavior. (Alpaydin [13], Pham and Afify [14]).

## 4.3. Support vector machines

First proposed by Cortes and Vapnik [15], Support Vector Machines (SVMs) construct so-called Hyperplanes to separate samples of different classes. The Hyperplane is constructed by finding the closest elements (the Support Vectors) of two different classes that maximize the distance between them and the plane. It is thus also called a Maximum Margin Hyperplane. In the prediction phase, new elements are predicted to have the same class as the other samples on its side of the Hyperplane. In cases where a Hyperplane cannot properly separate the elements, some ele ments can be allowed to be on the wrong side of the Hyperplane using a soft margin classifier, such as the C-SVM classifier suggested by Cortes and Vapnik [15]. Using a soft margin, SVMs can achieve a good generalization and robustness towards outliers. Moreover, nonlinear problems can be solved using the kernel trick [16]. Using different types of kernel functions, such as polynomial $\boldsymbol { \mathbf { \mathit { o r } } }$ radial basis function (RBF) kernels, can make a problem linearly separable. SVMs have shown good performance in tasks in a variety of fields such as manufacturing or also medical imaging Wuest et al. [17]. As opposed to instance-based methods, a mathematical function is fitted during the training phase, which results in a significantly faster prediction time. On the other hand, the mathematical function leads to limited comprehensibility of the model, as mentioned by Alpaydin [13], Bishop [18], James et al. [19].

## 4.4. Convolutional neural networks

Convolutional Neural Networks (CNNs) LeCun et al. [20] are a type of neural network especially useful for the processing of data with a gridlike topology (Goodfellow et al. [21]), for instance, image or timeseries data. CNNs are named after the mathematical operation convo lution, which is used to calculate an output instead of the general matrix multiplication in multilayer perceptrons (MLP). The weights to be learned are arranged in filters or kernels that are moved over the data, and the discretized convolution is calculated. The output of a convolution layer is called activation map. Often a pooling operation is performed, which only takes a mean or the most significant element of a part of the acti vation map into the next layer. This helps reduce the size of the network and makes it invariant to small deviations or noise in the data, thus leading to a better generalization. Unlike MLPs, CNNs do not ignore the fact that nearby data points are more strongly correlated than distant ones.

Neural Networks have a reputation for poor explainability. However, methods have been suggested to identify the features models base their predictions on. Selvaraju et al. [22] suggested the Gradient-weighted Class Activation Mapping (Grad-CAM) applicable to CNNs without modifying their architecture, which is necessary for other methods. To obtain the class-specific localization map $L _ { \mathrm { G r a d - C A M } } ^ { c }$ for class $c ,$ the gradients of the score $y ^ { c }$ for class c are calculated with respect to the feature map activations $A ^ { k }$ of the final convolutional layer. To obtain the neuron importance weights $\alpha _ { k } ^ { c } ,$ these back-propagated gradients are global-average-pooled over the input (indexed with $i , j ,$ and $Z$ as the number of elements in the feature map).

$$
\alpha_ {k} ^ {c} = \frac {1}{Z} \sum_ {i} \sum_ {j} \frac {\partial y ^ {c}}{\partial A _ {i j} ^ {k}}\tag{3}
$$

The weights are combined with the forward activation map of the last convolutional layer, and a ReLU function is applied to only obtain features having a positive influence on the class of interest.

$$
L _ {\text { Grad - CAM }} ^ {c} = R e L U \left(\sum_ {k} \alpha_ {k} ^ {c} A ^ {k}\right)\tag{4}
$$

## 5. Structure of the proposed algorithm

The suggested system has to be able to classify samples into multiple different categories. One class (normal operation) is treated more carefully than others as samples wrongly classified as normal can have severe consequences. Samples have to meet strict requirements to be classified as normal. Therefore, this prerequisite is integrated into the structural design of the algorithm. A new data sample is evaluated in several stages, each of them having the possibility to sort out the sample. Each layer can be adjusted individually and influences the final pre diction. A flow chart of the algorithm is shown in Fig. 5. It should be mentioned that all parts of the algorithm are optimized individually, as an enormous parameter space would have to be searched to find a global optimum.

![](/api/attachments/P9FN2ZQN/fulltext/images/ea1c8b8ff86c578ec6cc82ab10a0eb6bb8c69f9f2663593f41b3d4b2e2f6715e.jpg)  
Fig. 5. Flow chart of the suggested algorithm.

## 5.1. Anomaly detection

It is almost sure that during assembly, additional errors than the ones contained in the training datasets can occur. When confronted with an entirely unknown class, a classifier will fall back to the classes known from the training. However, to ensure a zero-defect policy, such samples need to be sorted out in advance. Thus, an anomaly detection algorithm (AD) based on a k-means clustering algorithm is suggested. Using a distance metric, this algorithm finds k clusters and their representatives in the normal or negative class of the training data. Subsequently, the distance of all elements in the test data (containing errors and normal operation) to their nearest representative is evaluated. Based on the distributions, a threshold for distinguishing faulty from nominal is determined. This approach is equivalent to a 1-Nearest Neighbour al gorithm. Three variables influence the classification and have to be optimized, namely the threshold, the distance metric, and the number of clusters k to discover in the normal data. In this work two distance metrics are compared: The Euclidean distance and the dynamic time warping (DTW) suggested by Sakoe and Chiba [23]. An example of the optimization for UC 1 is shown in the following, Data from normal operation was split into two equally large parts: the first one for training and the calculation of cluster centers as representatives and the other one for validation. When striving for a zero failure tolerance policy, the receiver operating characteristic (ROC) curve can be consulted to visu alize the trade-off between the classification of false negatives and false positives.

![](/api/attachments/P9FN2ZQN/fulltext/images/ec4631ffd013b0892ed4d53a613f2aa14d5d40dab11848defd9657add18b9a61.jpg)  
Fig. 6. ROC curve for k = 200 cluster centres and the Euclidean distance metric. The optimal cut-off according to J is d = 2.70.

Table 2  
FNR and FPR for the AD depending on k and different distance metrics.

<table><tr><td>k</td><td>Distance metric</td><td>FNR</td><td>FPR</td></tr><tr><td>10</td><td>Euclidean</td><td>0.042</td><td>0.092</td></tr><tr><td>10</td><td>DTW</td><td>0.033</td><td>0.068</td></tr><tr><td>50</td><td>Euclidean</td><td>0.025</td><td>0.084</td></tr><tr><td>50</td><td>DTW</td><td>0.029</td><td>0.048</td></tr><tr><td>100</td><td>Euclidean</td><td>0.030</td><td>0.068</td></tr><tr><td>100</td><td>DTW</td><td>0.033</td><td>0.024</td></tr><tr><td>200</td><td>Euclidean</td><td>0.025</td><td>0.076</td></tr><tr><td>200</td><td>DTW</td><td>0.036</td><td>0.024</td></tr></table>

In Fig. 6, the ROC curve for a model with 200 clusters and the Euclidean distance metric is shown. To create a model with zero FN, the TPR has to be 1. This can be achieved at a threshold of 1.29, however, at the cost of misclassifying more than 50% of all normal products as defective. This is by no means acceptable for industrial production. Therefore, the optimal cut-off will be the one that maximizes the TPR, while minimizing the FNR. This is also known as the Youden index J (Youden [24]).

$$
\begin{array}{r l} J & = \max (\text { Sensitivity } + \text { Specificity } - 1) \\ & = \max (\text { TPR } - \text { FPR }) \end{array}\tag{5}
$$

For UC 1, the distance threshold corresponding to J is 2.70. The re sults of different combinations of cluster numbers and distance metrics are given in Table 2. Although a model with a DTW metric and a cluster number of k = 100 achieves the best overall result, the models with the Euclidean distance metric and k = 50, as well as k = 200 have the lowest FNR. Therefore, only the Euclidean distance measure is considered. This also has the advantage that the runtime complexity is significantly lower (O(n) compared to $O ( n ^ { 2 } ) )$ . Runtime trials on an Intel i7-8850H CPU revealed a runtime of 264.63±5.91 (n = 100) using DTW, and

![](/api/attachments/P9FN2ZQN/fulltext/images/0241157ff30dd1cf71cbcad2f941dafa24c7ffd99cb9a8831529704fb754e84f.jpg)  
Fig. 7. CAMs for normalized samples of classes normal (left), Errors 3 (middle), and 4 (right).  
0.60±0.06 (n = 100) for the Euclidian distance.

## 5.2. Ensemble classifier

The next step of the algorithm is the prediction about the outcome of the assembly step. This step is also applied to elements that were already deemed faulty by the anomaly detection algorithm to gain additional insight into the cause of rejection. Instead of binary classification (“good”/“bad”), the system should confirm the correctness of the product or assign the corresponding error classes from the training. A single classifier for this task could pose a possible hazard, as a wrong classification could easily lead to an FN. Instead, multiple classifiers are used in an ensemble. A grid search is performed to optimize the hyperparameters of these algorithms. For each combination of values, a 5-fold stratified cross-validation is performed to select the model with the best mean accuracy as the final model.

## 5.2.1. Decision tree

As the first part of the ensemble, a simple DT was chosen. Humans can interpret the classification rules in order to help explain the reason for failures. The DT is not trained on the full time signals, but rather on features calculated from these. To maximize the interpretability of the model, the features consist of easy-to-calculate statistical measures. Minimum and maximum values can contain information about the violation of process limits. Their index in the time series marks the instant in which the low or high value appeared. The mean provides a measure of the general tendency of a variable’s values, whereas the standard deviation indicates the fluctuation within a sample. Each time series is divided into a certain number of windows. The six features are calculated for each signal (position, velocity, …) and each window. The adjustable hyperparameters in the grid search are the split criterion and the maximum depth of the tree, as well as the number of windows.

## 5.2.2. Support vector machine

An SVM is used as the second estimator in the ensemble. SVMs are less comprehensible compared to DTs but have delivered great results with little optimization. As SVMs are suited for evaluating high dimensional data, the model is trained on the full time series signal. SVMs are sensitive to the magnitude of the inputs and will emphasize features with larger values more. The aim is to consider all variables equally as it is not known which variable contains the most information. Hence, the data is standardized by subtracting the mean of the values and dividing by their standard deviation, preserving the characteristic shapes of the signals. The hyperparameters are the kernel, the penalty parameter C, the parameter γ (for an RBF kernel only), and the degree (for a polynomial kernel).

![](/api/attachments/P9FN2ZQN/fulltext/images/a57e3073ff9377cd347a6cf3008b0163ef4aef662fc72c6952d5720bb49ffa0e.jpg)

## 5.2.3. Convolutional neural network

CNNs do not only consider the individual inputs for their analysis, but also the relations between them. This makes CNNs highly suited for time series data. A custom CNN was designed as the third classifier in the ensemble. The optimized hyperparameters include the number of con volutional lavers, the number and length of filters, the number of training epochs, and the batch size. The ADAM algorithm was chosen as an optimizer and the ReLU function as the activation function. The data is standardized, as in the case of the SVM.

The Grad-CAM method by Selvaraju et al. [22] was demonstrated for image classification by localizing regions that the model uses to classify the contents. Nevertheless, the method is not limited to images and can be adapted for one-dimensional data as well. Therefore. when calcu lating the global-average-pooled weights, the sum over only one dimension (the length of the time series) has to be calculated. Fig. 7 shows an excerpt of data samples from the pre-study for selected classes (normal, Error 3, and Error 4) and their respective CAMs for a simple CNN with two convolutional layers and one fully-connected layer with 100 neurons before the output layer. The sections colored red are acti vated the most and thus indicate regions the network bases its decision on.

In the normal class, the CNNs attention is divided over multiple re gions of the time series. In contrast, the CNNs puts particular emphasis on specific parts of the signals for Errors 3 and 4. While for class 3, the section with critically high force is highlighted, class 4 is characterized by stiction of the motor in the second half of the assembly and the ex pected current drop just before this section. It can be concluded that CAMs are powerful to indicate regions that are representative of a class to human users. This allows them to interpret and understand the pre diction results in order to localize problems. Consequently, the trans parency of the QC system is increased.

(a)  
![](/api/attachments/P9FN2ZQN/fulltext/images/4495a400f7af4f0e13a35e5d26cd9e5ca44d7315586114ba522ed5c9ac0dd2cb.jpg)  
(b)  
Fig. 8. Pre-study results. Voting Scheme (left/(a)) and Overall error per algorithm. AD with a binary classification, all others with multiple classes (right/(b)).

![](/api/attachments/P9FN2ZQN/fulltext/images/47019000bc740fbbd3cd182dc7843d0eece8159fefa7b399aa1b752081cfe69f.jpg)  
Predicted label

![](/api/attachments/P9FN2ZQN/fulltext/images/169c77b918475e75103ca35608b2e798a35e3132f0ec06c86183d1aee7260509.jpg)  
Predicted label  
Fig. 9. Binary classification results of the QC system (left) and classification results of the ensemble for the pre-study dataset (right).

## 5.3. Voting scheme

Multiple voting schemes can be employed to produce a final pre diction based on the ensemble. The most straightforward way is a ma jority vote of all classifiers, where the individual predictions are equally weighed. However, FNs are possible if enough classifiers identify an error as a normal operation. As an alternative, class labels are only assigned if all classifiers come to the same results. If not, the sample will be treated as unknown and will be rejected. This allows for further analysis of the assembly that could not be classified as one of the known errors. Henceforth, this concept will be called a veto voting scheme, as a single classifier can stop the ensemble from making a final prediction. This also implies that the ensemble will only be as accurate as its worst classifier. The last considered voting option is a meta classifier. This method employs an additional classifier (level 2 classifier), which chooses the final output based on the other models’ outputs. Wolpert [25] shows that this arrangement of stacking classifiers can improve the accuracy of an ensemble.

A test has been conducted to compare the voting schemes with two different meta classifiers to evaluate the influence of the estimator. Therefore, the pre-study dataset was split into a training (80%) and a test set (20%). The algorithms were optimized by a grid search crossvalidation and trained on the training set. Subsequently, the system was tested on the test set. Fig. 8a shows the classification results with an FNR of 0% and a FPR of 14.85% common to all voting schemes. Besides, the overall error of the individual algorithms is shown in Fig. 8b. All misclassified samples were recorded during the test and analyzed. Fifteen normal samples were incorrectly identified as bad. All of them were sorted out by the first stage (AD), although the second stage would have correctly identified them as good. A closer inspection of the sam ples reveals that similar samples can be found in the normal class and error classes 1 and 3. This might be an indication that some of the ex periments at the test bench might have failed to provoke the desired behavior and instead formed another cluster of curves. It is, however, remarkable that the system manages to sort out all these “new” samples as it seems uncertain to which category they belong.

Overall, the algorithm generates two individual predictions: a binary classification that is used for the actual QC and a more detailed classi fication providing information about the possible failure patterns. The results of the system with a decision tree as meta classifier (delivering the most accurate predictions of all ensembles in the test) are visualized as confusion matrices in Fig. 9.

In order not to lose control over the false positive predictions certain design decisions have been made by focusing on the overall accuracy rather than the no-false-negatives-policy. Instead of choosing the threshold that would result in zero false negatives, the optimal distance threshold is chosen for the anomaly detection algorithm. Just as the best models are chosen in the grid search cross-validation and not the ones limiting false negatives. By comparing different voting schemes for the classifier ensemble it can be seen that in certain cases the conservative “veto” voting scheme might not even be necessary to achieve zero false negatives and that a democratic voting scheme achieves less false positives.

## 5.4. Implementation

The QC system is implemented in Python 3 and includes several accepted libraries. For DT and SVM, the scikit-learn library<sup>1</sup> is used. The CNNs are created in Keras,<sup>2</sup> a high-level Application Programming Interface (API) for TensorFlow.<sup>3</sup> The tslearn package<sup>4</sup> includes an optimized version of the DTW algorithm, as well as k-means and k-NN specifically designed for time series data. The source code of our algo rithm was published<sup>5</sup> and is freely available.

## 6. Evaluation

In this section, the proposed QC system is evaluated for UCs 1 and 2.

## 6.1. Use case 1: linear motor

In a test, the system was trained and evaluated on the data of UC 1. As the sampling rate differs slightly between assemblies, the signals are of variable length. Most algorithms, however, need a consistent input shape. The signals thus need to be resampled to a common number of data points by linear interpolation. Therefore, different scenarios are investigated: resampling to 38 points (approximate mean length of all signals), resampling to 41 points (maximum length in the dataset), as well as resampling to 38 points and deriving the corrupted velocity data from the position data by numerical differentiation. In Fig. 10a, the FPRs of the models are shown for the different voting schemes and scenarios. Resampling the signals to 38 points seems to achieve the best result. The democratic voting scheme and the meta DT deliver the best FPR of 9.04%. Adding the derived velocity feedback only improves the system in the case of a meta SVM.

When comparing the overall error rates, as shown in Fig. 10b, it can be seen that the AD algorithm is responsible for the most significant amount of misclassifications in this test. All 15 FP classifications, as seen in Fig. 10c, have their origin in this part of the system. By using the democratic voting scheme (cf. Fig. 10d), the ensemble classifier part of the algorithm achieves a perfect classification result.

![](/api/attachments/P9FN2ZQN/fulltext/images/737bffeb0d2c2909b444b48127bf0787bb64387e4087ed9373c9cab00c24d1e4.jpg)  
(a)

![](/api/attachments/P9FN2ZQN/fulltext/images/bbd1193af30b94070f5e12e68ce3290112c8e23129506a9ead061c0579724d41.jpg)  
(b)

![](/api/attachments/P9FN2ZQN/fulltext/images/72bf32cdfb2e022713f4b34011c6c5b6693c37ca16da4207f1722904729bb6b2.jpg)  
(c)

![](/api/attachments/P9FN2ZQN/fulltext/images/f1a579dbd604484c1b3892a9e51b712309438af06614dab03677b25d7119b820.jpg)  
(d)

![](/api/attachments/P9FN2ZQN/fulltext/images/0e0286ca871a59453054f5bd878662ec30446e32773decc8c8ec99d14bca2958.jpg)  
(e)  
Fig. 10. UC 1: evaluation results. FPR (left/(a)), Overall error per algorithm. AD with a binary classification, all others with multiple classes (right/(b)), Confusion matrix binary (left/(c)), Confusion matrix classes (right/(d)) and Average execution times (n = 10) (middle/(e)).

One hundred time measurements with random samples were con ducted to estimate the processing latency. In UC 1, 20 predictions have to be conducted before the deadline of 150 ms is reached. Therefore, the QC system’s execution time and all necessary preprocessing steps are evaluated while neglecting communication delays. In Fig. 10e, the re sults of the time measurements are displayed. On average it takes 3.109±0.277 ms (n = 20) to process a sample. Due to the design of the system, the time per sample decreases, the more samples are evaluated in parallel. Instead of predicting each sample individually, waiting until all 20 samples are available and processing them as a batch can signif icantly decrease the execution time. Evaluating the labels of 20 samples in a batch resulted in an execution time of 7.922±0.423 ms (n = 10), while processing 20 samples sequentially takes 62.797±5.525 ms (n =

10). In summary, both latencies are far below the maximal acceptable latency and can be used in the real manufacturing line.

## 6.2. Use case 2: pick and place unit

A similar test was carried out for UC 2. In contrast to UC 1, the data is sampled with a high frequency and contains, on average, 1000 values. Hence, different downsampling options were tested. In three scenarios, the time series were downsampled to 100, 200, and 500 points. The results of the test are visualized in Fig. 11a. Since the FNR is 0% in all tests, only the FPR is shown. As in the comparison test that was executed with the pre-study data, no difference in the algorithm's performance for the used voting scheme can be seen. Solely the classifier using the veto scheme trained on 100 points performs marginally worse than other voting options. The number of points the time series are resampled to, however, seems to influence the accuracy of the system. The algorithm trained on 200 points of the original data achieves the best FPR of 2.32% in the experiment.

![](/api/attachments/P9FN2ZQN/fulltext/images/e773da1cbcf41b302ac227487218d981a9f7b4e48222aeceac0f7dc0a52a9ff9.jpg)  
(a)

![](/api/attachments/P9FN2ZQN/fulltext/images/d4b0b424d9f05896a08cf6a9bdcbb44403b996ce839d321ba8081b96acc07e30.jpg)  
(b)

![](/api/attachments/P9FN2ZQN/fulltext/images/ab61f265a5e82aa1cdc9495915dc4983b7b5e1bc927ed21fef478af97a191e48.jpg)  
(c)

![](/api/attachments/P9FN2ZQN/fulltext/images/ddce044676f480072ec3cdc8c8236609493d16fe8e2aab85820d1e9264523e1f.jpg)  
(d)

![](/api/attachments/P9FN2ZQN/fulltext/images/4ed515fdcf78599ebb18e46822098b32bba1840609b10f288da9f741b775f195.jpg)  
(e)  
Fig. 11. UC 2: evaluation results. FPR (left/(a)), Overall error per algorithm. AD with a binary classification, all others with multiple classes (right/(b)), Confusion matrix binary (left/(c)). Confusion matrix classes (right/(d)) and Average execution times (n = 10) (middle/(e))

Again, the performance of the individual components was evaluated. The results are shown in Fig. 11b. The AD shows significantly more misclassifications than any of the classifiers in the ensemble. In Fig. 11c and d. the final output of the system is given as confusion matrices. The matrix distinguishing all classes stems from an ensemble using a meta decision tree to produce a result. Even though the ensemble classifier might make FN predictions, the final result does not include them as the AD algorithm filters them out.

Again, time measurements are taken to investigate the processing time. In UC 2, only two products need to be assembled and an assess ment of their quality needs to be issued within 200 ms. Fig. 11e shows the difference between the execution time for individual samples and batches of samples. The latter is significantly faster with an average of 5.953±0.341 ms (n = 10) for two samples. Again, each of the mea surements is the average of 100 individual time measurements with random samples. The latency is thus well below the limit.

## 7. Discussion

Despite showing that it can detect all defective components in the two presented use cases, there are still limitations to the system due to the early phase of the development. The error clustering is based on an FMEA where four to five categories have been identified. To strengthen the generalization of the system, batch-to-batch variation should be included which occurs over a longer period of production time and a thorough Gage R&R should be performed on the assembly equipment in focus based on real production data. However, this system can be used as a monitoring tool that provides insight into the assembly process and can be used for targeted troubleshooting when recurrent assembly errors appear. With an increase in maturity, the system can provide a foun dation for enabling Predictive Process Monitoring by not only looking at the current assembly but also taking the history of the last assemblies into account. Another potential hazard making it more difficult to control the number of false positives are incorrectly labelled data sam ples. When a normal sample is labelled as erroneous in the training data it can have a drastic effect on the number of false rejects, as the model intentionally tends to act conservatively. The associated cost of the rejected products has not been considered in this proof of concept.

## 8. Conclusions and future research

In this work, an ML-based QC system for automated assembly lines in the pharmaceutical industry was developed an evaluated using real in dustrial data. Unlike traditional systems, the proposed system can differentiate between multiple types of failures and provide additional insights. Besides, the system was designed with strict GMP regulations in mind to permit possible market approval.

The contributed system can learn from historic sensor data. A multi layer approach aims to prevent the misclassification of defective parts as normal ones. Therefore, an anomaly detection in stage 1 of the system sorts out unknown data samples. In stage 2, individual models assess the quality of the assembled product. In the last stage, the individual quality assessments are combined by a voting scheme to yield a final quality assessment. Additionally, the proposed system can provide reasoning in ways that are comprehensible for humans.

The system was evaluated in two industrial applications from the pharmaceutical industry. In both use cases, it could be demonstrated that the system recognizes defective products with 100% accuracy when trained on data from a small number of test batches. For now, the system is in its early development stage and needs to be trained on more data reflecting the variation of a production environment. Yet, it could be shown that the system’s execution time lies well below the maximal acceptable latency for the investigated production lines. Consequently, the algorithm has the potential to control the quality of products as a soft real-time system.

In the first stage of implementation at the real line, the system could be tested while executing in parallel with the existing QC system. Once the new system is trained enough and demonstrated its proper quality assessment, it could fully replace the old QC system.

## CRediT author statement

Sebastian Dengler: Conceptualization, Methodology, Software, Validation, Formal analysis, Writing - Original Draft, Writing - Review & Editing, Investigation, Data Curation.

Said Lahriri: Conceptualization, Investigation, Writing – Original Draft, Writing - Review & Editing.

Emanuel Trunzer: Writing - Original Draft, Writing - Review & Editing, Supervision.

Birgit Vogel-Heuser: Supervision.

## Declaration of Competing Interest

None.

## References

[1] 21 Code of Federal Regulations § 210, Current good manufacturing practice in manufacturing, processing, packing, or holding of drugs; general, 2019.

[2] C.A. Escobar, R. Morales-Menendez, Machine learning techniques for quality control in high conformance manufacturing environment, Adv. Mech. Eng. 10 (2018). https://doi.org/10.1177/1687814018755519. 168781401875551

[3] B. Ribeiro, Support vector machines for quality monitoring in a plastic injection molding process, in: JEEE Transactions on Systems. Man, and Cybernetics. Part C (Applications and Reviews) 35. 2005, pp. 401–410. https://doi,org/10.1109/ TSMCC,2004.843228.

[4] L.S. Lopes, L.M. Camarinha-Matos, A machine learning approach to error detection and recovery in assembly, in: 1995 IEEE. JEEE Computer Society Press, Los Alamitos, Calif, 1995, pp. 197–203. https://doi,org/10.1109/IROS.1995.525884

[5] H.-M. Chi, H. Moskowitz, O.K. Ersoy, K. Altinkemer, P.F. Gavin, B.E. Huff, B. A. Olsen, Machine learning and genetic algorithms in pharmaceutical development

and manufacturing processes, Decis. Support. Syst. 48 (2009) 69–80, https://doi. org/10.1016/j.dss.2009.06.010.

[6] S. Deb, B. Bhattacharyya, Fuzzy decision support system for manufacturing facilities layout planning, Decis. Support. Syst. 40 (2005) 305–314. URL: htt ps://doi.org/10.1016/i.dss.2003.12.007

[7] J. Grabocka, N. Schilling, M. Wistuba, L. Schmidt-Thieme, Learning time-series shapelets, in: Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2014, pp. 392–401, https://doi.org/ 10.1145/2623330.2623613

[8] J. Lines. S. Tavlor. A. Bagnall. Time series classification with hive-cote, ACM Trans Knowl. Discoy. Data 12 (2018) 1–35, https://doi.org/10.1145/3182382

[9] C. Di Francescomarino, C. Ghidini, F.M. Maggi, F. Milani, Predictive process monitoring methods: which one suits me best?, in: Business Process Management Springer International Publishing, Cham, 2018, pp. 462–479.

[10] E. Ruschel, E.A.P. Santos, E. de Freitas Rocha Loures, Mining shop-floor data for preventive maintenance management: Integrating probabilistic and predictive models, Proc. Manuf. 11 (2017) 1127–1134, https://doi.org/10.1016/j. promfg.2017.07.234. 27th International Conference on Flexible Automation and Intelligent Manufacturing, FAIM2017, 27–30 June 2017, Modena, Italy.

[11] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Q. 28 (2004) 75–105.

[12] L. Breiman, J. Friedman, C.J. Stone, R.A. Olshen, Classification and Regression Trees, CRC Press, 1984.

[13] E. Alpaydin, Introduction to Machine Learning, Adaptive Computation and Machine Learning, 3rd ed., The MIT Press, Cambridge, Massachusetts, 2014.

[14] D.T. Pham, A.A. Afify, Machine-learning techniques and their applications in manufacturing, Proc. Inst. Mech. Eng. B J. Eng. Manuf. 219 (2005) 395–412, https://doi.org/10.1243/095440505X32274.

[15] C. Cortes, V. Vapnik, Support-vector networks, Mach. Learn. 20 (1995) 273–297, https://doi.org/10.1007/BF00994018.

[16] B.E. Boser, I.M. Guyon, V.N. Vapnik, A training algorithm for optimal margin classifiers, in: Proceedings of the Fifth Annual Workshop on Computationa Learning Theory, 1992, pp. 144–152.

[17] T. Wuest, D. Weimer, C. Irgens, K. Thoben, Machine learning in manufacturing: advantages, challenges, and applications, Prod. Manuf. Res. 4 (2016) 23–45.

[18] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, New York, NY, 2006.

[19] G. James, D. Witten, T. Hastie, R. Tibshirani, An Introduction to Statistical Learning: With Applications in R, Volume 103 of Springer texts in statistics, Springer, New York, 2013.

[20] Y. LeCun, B. Boser, J.S. Denker, D. Henderson, R.E. Howard, W. Hubbard, L. D. Jackel. Backpropagation applied to handwritten zip code recognition. Neura Comput. 1 (1989) 541–551. https://doi,org/10.1162/neco.1989.1.4.541.

[21] Y. Goodfellow, A. Bengio, Courville, Deep Learning, MIT Press, 2016.

[22] R.R. Selvaraiu, M. Cogswell. A. Das, R. Vedantam, D. Parikh. D. Batra, Grad-cam: visual explanations from deep networks via gradient-based localization. Int. J Comput. Vis. 35 (2019) 1798, https://doi.org/10.1007/s11263-019-01228-7.

[23] H. Sakoe, S. Chiba, Dynamic programming algorithm optimization for spoken word recognition, IEEE Trans. Acoust. Speech Signal Process. 26 (1978) 43–49, https:/ doi.org/10.1109/TASSP.1978.1163055.

[24] W.J. Youden, Index for rating diagnostic tests, Cancer 3 (1950) 32–35, https://doi. org/10.1002/1097-0142(1950)3:132::AID-CNCR28200301063.0.CO:2-3

[25] D.H. Wolpert, Stacked generalization, Neural Netw. 5 (1992) 241–259, https://doi. org/10.1016/S0893-6080(05)80023-1

![](/api/attachments/P9FN2ZQN/fulltext/images/8b0c14e84ec5b979f1dbb6d2f6f257d498e3ce4a758dbba7966af76c4d039696.jpg)  
Sebastian Dengler received a B.Sc. (‘17) in engineering science and a M.Sc. (‘20) in mechanical engineering from the Technical University of Munich, Germany. He is currently working as a Data Scientist for Novo Nordisk A/S in Denmark. His interests include Machine Learning and Deep Learning applications for automated manufacturing processes and industrial Internet of Things solutions.

![](/api/attachments/P9FN2ZQN/fulltext/images/928173d52ba15d805c49733752236d69519a3f5ed0779e2939e2c239dccf7776.jpg)

![](/api/attachments/P9FN2ZQN/fulltext/images/4d4bbdf0d0a1a4e0fdaf7240c49f0d8122436193d6a6dcddb6dcc05fa5ffac89.jpg)

Said Lahriri holds a MSc (‘08) in Mechanical Engineering and a Ph.D (13) in Nonlinear Dynamics both from the Technical University of Denmark – DTU. He has worked in the energy industry for 6 years where he was a specialist in mechanical and structural dynamics in machinery and rotordynamics in particular. Since 2014 he has worked for the pharmaceutical company Novo Nordisk A/S within the department of Manufacturing Intelligence. Here, he is the technical lead for the process domain expert team where he leads and orches trates the activities, projects and research within Industry 4.0. During the last years he is also working as appointed examiner at DTU and he is an in peer technical reviewer for the Journal of Mechanism and Machine Theory – Elsevier.

Emanuel Trunzer received a B.Sc. (‘13) and an M.Sc. (‘16) in chemical engineering, as well as a Dr.-Ing. Degree in mechan ical engineering (‘20) from the Technical University of Munich, Germany. His interests include model-driven system architec tures for data collection in Industrie 4.0 scenarios and data analytics for CPPS and the Industrial Internet of Things.

![](/api/attachments/P9FN2ZQN/fulltext/images/e0168a2da1738b2322527bd6d4becf8502d9685dbb39bbea855d402f7acfc585.jpg)

Birgit Vogel-Heuser (M’04–SM’12) holds an Dipl.-Ing. degree in electrical engineering and a Dr.-Ing. degree in mechanical engineering (RWTH Aachen, Germany, 1991). She was involved in industrial automation with the machine and plant manufacturing industry for nearly ten years. She has been Head of the Automation and Information Systems Institute at the Technical University of Munich, Germany, since 2009. Vogel-Heuser was Coordinator of the Collaborative Research Centre SFB 768. She is a member of the German Academy of Science and Engineering, editor of IEEE-TASE, and GC of IEEE CASE 2018. Her current research interests include systems and soft ware engineering, and modeling distributed and reliable embedded systems. During the last five years, her work ach

ieved wide-spread acceptance and was frequently cited (according to Google Scholar, 4779 citations since 2015).
