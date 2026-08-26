---
otero_id: 5598
otero_key: "GPT53WVX"
title: "Preprocessing unbalanced data using support vector machine"
authors: "M.A.H. Farquad; Indranil Bose"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Preprocessing unbalanced data using support vector machine

M.A.H. Farquad <sup>a</sup>, Indranil Bose <sup>b,</sup>⁎

<sup>a</sup> School of Business, The University of Hong Kong, Pok Fu Lam Road, Hong Kong

<sup>b</sup> Indian Institute of Management Calcutta, Diamond Harbour Road, Kolkata 700104, India

## a r t i c l e i n f o

Article history: Received 20 October 2011 Received in revised form 14 December 2011 Accepted 30 January 2012 Available online 15 February 2012

Keywords: Hybrid method Preprocessor SVM Unbalanced data COIL data

## a b s t r a c t

This paper deals with the application of support vector machine (SVM) to deal with the class imbalance problem. The objective of this paper is to examine the feasibility and ef<sup>fi</sup>ciency of SVM as a preprocessor. Our study analyzes different classi<sup>fi</sup>cation algorithms that are employed to predict the customers with caravan car policy based on his/her sociodemographic data and history of product ownership. A series of experiments was conducted to test various computational intelligence techniques viz., Multilayer Perceptron (MLP), Logistic Regression (LR), and Random Forest (RF). Various standard balancing techniques such as undersampling, over-sampling and Synthetic Minority Over-sampling TEchnique (SMOTE) are also employed. Subsequently, a strategy of data balancing for handling imbalanced distribution in data is proposed. The proposed approach <sup>fi</sup>rst employs SVM as a preprocessor and the actual target values of training data are then replaced by the predictions of trained SVM. Later, this modi<sup>fi</sup>ed training data is used to train techniques such as MLP, LR, and RF. Based on the measure of sensitivity, it is observed that the proposed approach not only balances the data effectively but also provides more number of instances for minority class, which in turn enhances the performance of the intelligence techniques.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The class imbalance problem has been recognized in many real world applications [26] and is an evolving topic of machine learning research. It is observed from the literature that machine learning techniques tend to produce suboptimal classi<sup>fi</sup>cation models. The class imbalance problem where little or very less instances are available for the most important class of the study exists in many real world application domains, such as telecommunications [23], detection of oil spoils in satellite radar images [32], text classi<sup>fi</sup>cation [42], medical diagnosis [29], intrusion detection [34] and fraud detection [41].

Researchers have been attempting to deal with classi<sup>fi</sup>cation using unbalanced datasets. Methods to deal with imbalanced problems include, resizing training set that includes, oversampling minority class samples [35] and downsizing majority class samples [31], adjusting misclassi<sup>fi</sup>cation costs [11] and recognition based learning [32]. Detailed review reports [19,30,39,51] have discussed the key issues related to problem solving with unbalanced training data using machine learning techniques. Research studies show that many standard machine learning approaches result in poor performance, speci<sup>fi</sup>cally when dealing with medium and large scale unbalanced datasets [17,26,32,49,50].

One of the key problems when learning with imbalanced data sets is the lack of data where the number of samples is small or no sample is available for a particular class [50]. If there is a lack of data, the estimated decision boundary can be very far from the true boundary. Japkowicz and Stephen [26] reported that for simple data sets that were linearly separable, classi<sup>fi</sup>er performances were not susceptible to any amount of imbalance. Indeed, as the degree of data complexity increased, the class imbalance factor started affecting the generalization ability of the classi<sup>fi</sup>ers. Most accuracy-driven algorithms are biased toward the prevalent class. The machine learning approaches improved overall accuracy by assigning the overlapped area to the majority class, and ignored or treated the minority class as noise [49].

Since late 1960s, researchers have put their efforts toward developing strategies to deal with the class imbalance problem. In the earliest stage of this research, researchers used the condensed nearest neighbor method of under-sampling [22]. Wilson [52] proposed an Edited Nearest Neighbor (ENN) method of under-sampling. In this method, noisy samples from the majority class are removed in order to under-sample the data. Later, Kubat and Matwin [31] developed a concept of selective under-sampling by keeping the minority samples untouched. They introduced a data cleaning procedure using the Tomek–Links concept for under-sampling and removed the borderline majority samples. Based on Wilson's ENN method, the Neighbourhood Cleaning Rule is proposed to eliminate or to discard the majority class samples [33]. Later, Chawla et al. [9] proposed SMOTE (Synthetic Minority Over-sampling TEchnique), where synthetic (arti<sup>fi</sup>cial) samples are generated rather than over-sampling

Table 1

by replacement. Maloof [37] reported that sampling has the same result as moving the decision threshold or adjusting the cost matrix. Barendela et al. [2] proposed a weighted distance function to be used in the classi<sup>fi</sup>cation phase of k-NN to compensate for the imbalance in the training samples without actually altering the distribution of classes. Ef<sup>fi</sup>ciency of SVM is then analyzed to deal with the class imbalance problem [53]. They proposed SVM with a changed kernel function, which pushed the hyperplane closer to the positive class. Estabrooks et al. [13] concluded that combining different expressions of resampling approach was an effective solution. On the contrary, some researchers also reported that there was no further improvement to the predictive performance of SVM for text classi<sup>fi</sup>cation when it was preceded by strategies such as resampling in the presence of imbalanced training data [44].

Researchers have emphasized the use of clustering based preprocessing methods as an alternative for sampling of the data. Batista et al. [3,4] proposed two hybrid sampling techniques, SMOTE+Tomek– Links and SMOTE + ENN for overlapping datasets, for better de<sup>fi</sup>ned class clusters among majority and minority classes. Jo and Japkowicz [27] presented a cluster based over-sampling approach. Majority and minority class samples are clustered <sup>fi</sup>rst and the clusters in the majority class are over-sampled to the largest cluster obtained for the majority class data. Han et al. [21] proposed borderline SMOTE, which identi<sup>fi</sup>ed minority samples at borderline and applied SMOTE. This is the only technique proposed to over-sample the borderline minority samples. Later, k-means based under-sampling method and the Agglomerative Hierarchical Clustering based oversampling method to deal with unbalanced datasets are proposed [10]. Guo and Viktor [18] proposed boosting method with various over-sampling techniques to deal with hard to classify examples and concluded that boosting approach improved the prediction accuracy of the classi<sup>fi</sup>er. Huang et al. [25] presented Biased Minimax Probability Machine to resolve the imbalance problem.

Researchers then exerted their efforts toward developing hybrid approaches to deal with unbalanced data, where they combined over-sampling and under-sampling with different concepts into one approach. Some used a combination of under-sampling and over-sampling [35]. They used lift analysis instead of classi<sup>fi</sup>cation accuracy to measure a classi<sup>fi</sup>ers performance. Various hybrids, SMOTE-bootstrap hybrid [36] and a hybrid combining machine learning and unsupervised McCab feature selection method using SVM and maximum entropy method [12], and a hybrid balancing model using unsupervised clustering and decision tree boosting [6] are proposed. Later, Farquad et al. [14,15] proposed a hybrid rule extraction from SVM approach for handling the class imbalance problem. They concluded that rules extracted using their proposed approach performed very well. Table 1 provides a chronological overview of the balancing approaches proposed by various researchers.

Researchers have never reported any preprocessing using intelligent methods to balance the data. In this paper we employ SVM as a preprocessor. SVM is one of the best intelligent algorithms used for classi<sup>fi</sup>cation and regression purposes. The best property of SVM is that it always yields global optimal solution, whereas other intelligent algorithms suffer from getting stuck with a local minimum. SVM tries to <sup>fi</sup>nd the decision boundary between various classes without actually worrying about the number of instances available for a class. SVM is suitable for high dimensional problems and works with a small number of observations as well. Hence, trained SVM is proposed as a preprocessor in this paper.

The rest of the paper is organized as follows. Section 2 presents a brief overview of the method of SVM and motivation for the proposed approach. Section 3 explains the architecture of the proposed balancing approach. Section 4 presents a description of the dataset and the experimental method used in this research. Results and discussions are presented in Section 5. Section 6 concludes the paper. A brief overview of MLP, LR and RF is provided in Appendix A.

Chronological overview of the balancing techniques.

<table><tr><td>Balancing approaches (author(s), year)</td><td>References</td><td>Summary</td></tr><tr><td>Condensed nearest neighborhood (CNN) (Hart, 1968)</td><td>[22]</td><td>Noisy samples are removed from majority data using CNN</td></tr><tr><td>Tomek-Links (Kubat and Matwin, 1997)</td><td>[31]</td><td>Borderline majority data is removed using Tomek-Links</td></tr><tr><td>Over-sampling (Ling and Li, 1998)</td><td>[35]</td><td>Duplicates of the minority data are provided</td></tr><tr><td>Edited Nearest Neighbor (ENN) (Wilson, 1972; Laurikkala, 2001)</td><td>[33,52]</td><td>Noisy samples are removed from majority data using ENN</td></tr><tr><td>SMOTE (Chawla et al., 2002)</td><td>[9]</td><td>Synthetic data is generated for minority sample</td></tr><tr><td>Combination of sampling approaches (Estabrooks, Jo, and Japkowicz, 2004)</td><td>[13]</td><td>Combine over-sampling and under-sampling</td></tr><tr><td>SMOTE + Tomek (Batista, Monad, and Bazzan, 2004)</td><td>[3]</td><td>Alternate sampling using SMOTE + Tomek</td></tr><tr><td>SMOTE + ENN (Batista, Prati and Monard, 2004)</td><td>[4]</td><td>Alternate sampling using SMOTE + ENN</td></tr><tr><td>Boosting (Guo and Viktor, 2004)</td><td>[18]</td><td>Boosting is employed for over-sampling the minority data</td></tr><tr><td>Borderline SMOTE (Han, Wang and Mao, 2005)</td><td>[21]</td><td>Over sampling applied to borderline minority data only</td></tr><tr><td>SMOTE + Bootstrap (Liu et al., 2006)</td><td>[36]</td><td>Hybrid sampling approach</td></tr><tr><td>K-means agglomerative clustering (Cohen et al., 2006)</td><td>[10]</td><td>Over-sampling</td></tr><tr><td>Hybrid approaches (Eitrich et al., 2007; Bose and Chen, 2009; Farquad et al., 2009; Farquad et al., 2010)</td><td>[6,12,14,15]</td><td>Combined over-sampling and under-sampling</td></tr></table>

## 2. Overview of support vector machine

The SVM is a learning procedure based on the statistical learning theory [47] and it is one of the best machine learning techniques used in data mining [54]. It has been used in a wide variety of applications such as prediction of colon cancer [1], gene analysis [20], credit rating analysis [24], <sup>fi</sup>nancial time-series forecasting [28], <sup>fi</sup>nancial fraud detection [40], estimating manufacturing yields [43], users web browsing behavior [55], among others.

For solving a two-class classi<sup>fi</sup>cation problem, the main objective of SVM is to <sup>fi</sup>nd an optimal separating hyperplane that correctly classi<sup>fi</sup>es data points as much as possible and separates the points of the two classes as far as possible, by minimizing the risk of misclassifying the training samples and unseen test samples [47,48].

The optimization problem for the SVM can be depicted as follows:

$$
\begin{array}{l} \min \frac {1}{2} \langle w, w \rangle \\ \text { Subject   to } y _ {i} (w \cdot x _ {i} + b) \geq 1 \forall x _ {i}. \end{array}\tag{1}
$$

The SVM classi<sup>fi</sup>cation function for classifying linearly separable data can be written as:

$$
f (x) = \langle w, x \rangle + b = \sum_ {i = 1} ^ {l} y _ {i} \alpha_ {i} \langle x _ {i}, x \rangle + b.\tag{2}
$$

This is also known as hard margin, where no room is given for errors. It is observed that most of the time it is linearly nonseparable. Hence slack variable ξ is introduced to allow $\xi$ error and the optimization function takes the form of Eq. (3) as shown below:

$$
\begin{array}{l} \min \frac {1}{2} \langle w, w \rangle + C \sum_ {i = 1} ^ {l} \xi_ {i} \\ \text { Subject   to } y _ {i} (w \cdot x _ {i} + b) \geq 1 \forall x _ {i}. \end{array}\tag{3}
$$

To deal with the problem of non-linearly separable dataset, SVM <sup>fi</sup>rst projects the data into a higher dimensional feature space using various kernels and tries to <sup>fi</sup>nd the linear margin in the new feature space. The optimization function can be depicted as shown below:

$$
\begin{array}{l} \min \frac {1}{2} \langle w, w \rangle + C \sum_ {i = 1} ^ {l} \xi_ {i} \\ \text { Subject   to } y _ {i} (w \cdot \varphi (x) + b) \geq 1 \forall x _ {i}. \end{array}\tag{4}
$$

The optimal hyperplane separating the binary decision classes is given by Eq. (5):

$$
f (x) = \sum_ {i = 1} ^ {l} y _ {i} \alpha_ {i} K (x _ {i}, x) + b\tag{5}
$$

where $K ( x _ { i } , x ) = \varphi ( x _ { i } ) \varphi ( x )$ is taken with a semi-positive de<sup>fi</sup>nite kernel.

## 2.1. Motivation for the proposed approach

The main objective of SVM is to <sup>fi</sup>nd an optimal separating hyperplane that correctly classi<sup>fi</sup>es data points as much as possible and separates the points of two classes as far as possible, by minimizing the risk of misclassifying the training samples and unseen test samples. C and kernel are the only parameters for training SVM. It is observed that when we modify C, which represents acceptable error, to higher values the decision boundary moves more towards majority class instances in turn misclassifying majority class instances as minority class instances (as explained in Fig. 1 below). In other words, more misclassi<sup>fi</sup>cations for majority class instances mean more number of instances for minority class. When SVM model is trained with high value of C and predictions are obtained, it yields more predictions for minority class instances. As a result, the modi<sup>fi</sup>ed data has more instances for minority class. This in turn yields data which is not only balanced but also provides more number of instances for minority class without compromising the prediction accuracy of SVM. The reason behind using SVM for such preprocessing is that, it predicts similar instances from majority class instances as minority class instances, instead of randomly selecting them from training data as minority class instances. Fig. 1 shows various decision boundaries learnt by SVM when the parameter C is changed.

Fig. 1(a) shows the decision boundary learnt by SVM when C is 0.8. It is observed that when a small value of C (refer Eq. (3) in Section 2) is provided, the decision boundary learnt by SVM is performing well with the majority class instances (red circles). As more number of instances on the boundary is for the majority class and the exempted error value is low (i.e., 0.8), therefore the yielded prediction accuracy for minority class instances is very low. Fig. 1(b) shows the decision boundary learnt by SVM when C is 5. It is observed that when more error is allowed, the decision boundary learnt by SVM moved more toward the majority class instances. Therefore some more instances of minority class are predicted correctly and more majority class instances are misclassi<sup>fi</sup>ed. At this point the prediction for minority class instances is slightly improved. Fig. 1(c) shows the decision boundary learnt by SVM when C is 10. It is observed that when more error is allowed, the decision boundary learnt by SVM moved very much toward the majority class instances. As a result of this movement, even more instances of the minority class are predicted correctly and a larger number of the majority class instances are misclassi<sup>fi</sup>ed. Likewise the prediction accuracy of the minority class instances is improved further. However, it is observed that further increase in the error could lead to the problem of over-<sup>fi</sup>tting.

![](/api/attachments/GPT53WVX/fulltext/images/1ec5df77100fca8b13a442678086b158ca0a70a20825ff61b00e8d0a046fb25d.jpg)

![](/api/attachments/GPT53WVX/fulltext/images/81becad10584106583938ba17c02539367e59dedb50b0f72b75217538399d7c4.jpg)

![](/api/attachments/GPT53WVX/fulltext/images/e79846a0bceab2b459bd9ac64ad7065bf09f3d0cbb89982f72d68ea7540348e7.jpg)  
Fig. 1. Movement of the SVM decision function based on the parameter C when (a) C=0.8, (b) C=5, and $( \mathrm { c } ) \ : C = 1 0$

## 3. Proposed balancing approach

Most of the real-world data are imbalanced in terms of the proportion of examples available for each class. This problem of imbalanced class distributions can lead the algorithms to learn overly complex models that over <sup>fi</sup>t the data and have little relevance. It is observed that despite better performance of computational intelligence techniques, they are biased towards majority class instances and learn better about majority class and learn slightly or ignore minority class. In this paper we propose a two phase balancing approach to improve the performance of intelligent algorithms viz., MLP, LR, and RF using trained SVM as a preprocessor. The steps involved in the proposed two phase balancing approach are presented in Fig. 2.

![](/api/attachments/GPT53WVX/fulltext/images/02a4c5b99388a8a481c505dee5447b9f62fdd8a3592d04a1f93d3b4fd9ad24e4.jpg)  
Fig. 2. Flowchart of the proposed two phase balancing approach.

SVM is one of the most effective classi<sup>fi</sup>cation techniques proposed in literature and it is very ef<sup>fi</sup>cient in solving two class classi<sup>fi</sup>- cation problems [54]. The proposed approach <sup>fi</sup>rst builds a SVM model; and the actual target values of the training instances are then replaced by the prediction of the trained SVM. Later, this modi-<sup>fi</sup>ed data is used to train the MLP, LR, and RF algorithms. It is observed that use of SVM prediction not only balances the data but also helps the intelligent algorithms learn better about the minority class and improves the prediction accuracy of the classi<sup>fi</sup>ers for the minority class instances.

The steps involved in the proposed two phase balancing approach are as follows: steps 1 and 2 below make up phase 1 of the proposed approach, and steps 3 and 4 make up phase 2 of the proposed approach.

Step 1 SVM training — using the available unbalanced data SVM is trained, and the SVM model with the best prediction accuracy is selected and used for prediction purposes.

Step 2 Prediction of training data using trained SVM — after successfully obtaining the trained SVM, the target values in the training data are replaced by the predictions of the trained SVM. At this stage available data is modi<sup>fi</sup>ed and balanced data is obtained.

Step 3 Modi<sup>fi</sup>ed data is then used to train various intelligent algorithms — using the modi<sup>fi</sup>ed data various intelligent techniques are trained such as MLP, LR, and RF. The reasons for selecting these intelligent techniques out of all available classi<sup>fi</sup>ers are provided in Section 5.

Step 4 Trained intelligent algorithms are used for prediction — predictions are obtained using the trained intelligent algorithms using the modi<sup>fi</sup>ed data and empirical analysis of the accuracy of prediction is carried out.

## 4. Experimental setup

## 4.1. Dataset

The dataset analyzed in this paper is used in the Coil 2000 data mining competition [46]. It is related to customer data for an insurance company. The target variable is whether or not a customer would buy caravan insurance policy. For each customer, 86 attributes are provided. They included 43 socio-demographic variables derived via the customer's zip code, which included age, customer type, religion, relationship status, education level, children in the family, ownership of the house, employment, salary details, etc. and 43 variables about ownership of other insurance policies such as private accidents policy, family accidents policy, motor cycle/scooter policy, car policy, delivery van policy, tractor policies, <sup>fi</sup>re policies, agricultural machine policies, life insurance policies, etc. This dataset contained 5822 records for training and 4000 records for testing. Only 348 customers, i.e., 6% of the training data represented customers who bought the caravan insurance policy. The remaining 5474 records represented customers who did not prefer to buy caravan insurance. This is an example of a highly unbalanced dataset. 4000 records that were provided for testing also followed a similar class distribution ratio i.e., 94:6. We used all the attributes available in the dataset without employing any cleaning or preprocessing on it.

## 4.2. Experimental method

The most effective and simplest approaches proposed by researchers to deal with unbalanced datasets are resizing the training samples. Hence, we employed various sampling techniques to comparatively evaluate our proposed approach. The sampling techniques employed are 100% over-sampling, 200% over-sampling, 25% undersampling, 50% under-sampling, and SMOTE. The dataset available is already divided into training and testing, and we employed sampling on only the training data. The class distribution ratio after employing the sampling techniques is presented in Table 2. Column 6 in Table 2 presents the distribution ratio of the majority and minority class instances after modi<sup>fi</sup>cations using the proposed approach. It is observed from Column 6 of Table 2 that the trained SVM not only balanced the data but also modi<sup>fi</sup>ed the data in such a way that more number of instances is predicted as minority class instances without compromising the accuracy of the model.

## 5. Results and discussion

Identifying the potential customers who can buy caravan insurance policy is the basic intention of this study. The quantities employed to measure the quality of the classi<sup>fi</sup>ers are sensitivity, speci<sup>fi</sup>city and accuracy [16]. We place high emphasis on sensitivity alone which contributes towards <sup>fi</sup>ltering and <sup>fi</sup>nding the most possible buyers of the caravan insurance policy. Consequently, in this paper, sensitivity is given top priority ahead of speci<sup>fi</sup>city and accuracy. We de<sup>fi</sup>ne the performance measures used in this research in the following paragraphs.

Sensitivity is the measure of proportion of the true positives (customers buying caravan insurance policy in this study), which are correctly identi<sup>fi</sup>ed.

Specificity is the measure of proportion of the true negatives (customers who do not prefer to buy caravan policy in this study), which are correctly identi<sup>fi</sup>ed.

Accuracy is the measure of proportion of true positives and true negatives, which are correctly identi<sup>fi</sup>ed.

A Receiver Operating Characteristics (ROC) graph [16] has long been used in signal detection theory to depict the trade-off between hit accuracies and false alarm accuracies of classi<sup>fi</sup>ers. In a ROC curve the true positive rate (Sensitivity) is plotted in function of the false positive rate (100-Speci<sup>fi</sup>city) for different cut-off points of a classi<sup>fi</sup>- er. Each point on the ROC curve represents a sensitivity/speci<sup>fi</sup>city pair corresponding to a particular decision threshold. The area under the ROC curve is a measure of how well a parameter can distinguish between two classes (With caravan policy/Without caravan policy).

Distribution ratio of classes' instances before and after sampling and preprocessing using SVM.

<table><tr><td>Data</td><td>Total</td><td>Without caravan policy</td><td>With caravan policy</td><td>Ratio</td><td>Ratios after preprocessing using SVM</td></tr><tr><td>Original</td><td>5822</td><td>5474</td><td>348</td><td>94:6</td><td>42:58</td></tr><tr><td>SMOTE</td><td>10,948</td><td>5474</td><td>5474</td><td>50:50</td><td>35:65</td></tr><tr><td>25% under-sampling</td><td>4453</td><td>4105</td><td>348</td><td>92:8</td><td>41:59</td></tr><tr><td>50% under-sampling</td><td>3085</td><td>2737</td><td>348</td><td>89:11</td><td>45:55</td></tr><tr><td>100% over-sampling</td><td>6170</td><td>5474</td><td>696</td><td>89:11</td><td>48:52</td></tr><tr><td>200% over-sampling</td><td>6418</td><td>5474</td><td>944</td><td>85:15</td><td>40:60</td></tr><tr><td>Test data</td><td>4000</td><td>3762</td><td>238</td><td>94:6</td><td></td></tr></table>

Table 3 presents the results obtained using standalone SVM where the best SVM model is selected for obtaining the predictions for training instances in the preprocessing step. The basic and the most effective property of SVM is to generate a hyperplane between the two class instances which can discriminate the class to the maximum distance irrespective of the number of instances available to learn from for any class. Because of this property, SVM is able to learn better for both the majority and the minority class. It is observed from the experiments that SVM performs well with unbalanced data with high value of parameter C and the RBF kernel. When the decision boundary of SVM shifted more towards the majority class instances with high error rate i.e., high value of parameter C, the trained SVM yielded low accuracy for training data but performed exceptionally well for the testing data. It can be concluded that the number of instances for a particular class (for a two class classi<sup>fi</sup>cation problem) did not affect the learning and predictions made by SVM.

Neural network is an ef<sup>fi</sup>cient intelligent technique used in a variety of applications for pattern recognition in medicine, engineering, and business. A two layer backpropagation network with a suf<sup>fi</sup>cient number of hidden nodes has proven to be a universal approximator. Hence, it was selected for empirical analysis in this research. Tables 4 and 5 present the results using standalone MLP and the proposed SVM-MLP algorithms respectively, and Fig. 3 presents a comparison of the sensitivities obtained in these experiments. It is observed from the empirical results that the modi<sup>fi</sup>cation of the data using the proposed approach helped MLP to obtain better prediction of minority class instances. It is also observed that the sensitivity of the standalone MLP <sup>fl</sup>uctuated when the standard balancing techniques are used. It is concluded that MLP worked better when enough number of training instances are provided to learn about a class. At the same time, results obtained using the proposed hybrid MLP-SVM approach are much better compared to the results obtained using the standalone MLP algorithm in terms of sensitivity.

Logistic regression is a simple classi<sup>fi</sup>cation approach and very ef-<sup>fi</sup>cient in learning from unbalanced datasets. Therefore, it is employed in this research to evaluate the ef<sup>fi</sup>ciency of the proposed balancing approach. Tables 6 and 7 present the results obtained using standalone LR and the proposed hybrid SVM-LR, respectively. Fig. 4 presents a comparative analysis of the sensitivities for experiments using LR and SVM-LR. It is observed that, similar to MLP, the performance of LR is also improved using the modi<sup>fi</sup>ed data. The proposed approach SVM-LR using modi<sup>fi</sup>ed original data yielded better sensitivity of 63.03% than that of the sensitivity yielded by standalone LR with SMOTE data i.e., 56.3%. SMOTE data with the proposed approach yielded a sensitivity of 68.49% whereas 25% under-sampled data using the proposed balancing approach yielded the best sensitivity of 70.17%. Similar to MLP, standalone LR learnt better if more number of training instances is provided for a class.

Random forest is an ef<sup>fi</sup>cient and transparent data mining algorithm used for classi<sup>fi</sup>cation purposes. It generates a number of trees from the data and based on the number of votes a tree gets, prediction is provided by any of the tree in the forest. Tables 8 and 9 present the results obtained using standalone RF and the proposed SVM-RF approach, respectively. Similar to MLP and LR, RF also yielded better results using the proposed balancing approach compared to the standalone case. From Table 9 it is observed that 25% under-sampled data yielded the best sensitivity of 71.01%. Fig. 5 presents a comparison of the sensitivities obtained using RF and SVM-RF. It is concluded that RF with modi-<sup>fi</sup>ed data performed better compared to standalone RF and standalone RF with various standard balancing techniques.

Table 3  
Results obtained using SVM.

<table><tr><td>Balancing technique</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>AUC</td></tr><tr><td>Original unbalanced</td><td>63.45</td><td>42.24</td><td>43.5</td><td>5284.5</td></tr><tr><td>SMOTE</td><td>67.65</td><td>46.33</td><td>47.6</td><td>5699</td></tr><tr><td>25% under-sampling</td><td>69.75</td><td>40.59</td><td>42.34</td><td>5517</td></tr><tr><td>50% under-sampling</td><td>62.61</td><td>44.34</td><td>45.42</td><td>5347.5</td></tr><tr><td>100% over-sampling</td><td>66.39</td><td>49.04</td><td>50.08</td><td>5771.5</td></tr><tr><td>200% over-sampling</td><td>67.23</td><td>40.32</td><td>41.93</td><td>5377.5</td></tr></table>

Table 4  
Results obtained using standalone MLP.

<table><tr><td>Balancing technique</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>AUC</td></tr><tr><td>Original unbalanced</td><td>5.88</td><td>98.62</td><td>93.10</td><td>5225</td></tr><tr><td>SMOTE</td><td>34.87</td><td>85.49</td><td>82.48</td><td>6018</td></tr><tr><td>25% under-sampling</td><td>13.45</td><td>97.21</td><td>92.22</td><td>5533</td></tr><tr><td>50% under-sampling</td><td>22.69</td><td>94.02</td><td>89.78</td><td>5835.5</td></tr><tr><td>100% over-sampling</td><td>11.34</td><td>97.26</td><td>92.15</td><td>5430</td></tr><tr><td>200% over-sampling</td><td>13.45</td><td>94.02</td><td>89.22</td><td>5373.5</td></tr></table>

## 6. Conclusion

It is well known that standard machine learning algorithms are biased towards majority class when dealing with unbalanced data. In this research, the ef<sup>fi</sup>ciency of SVM in dealing with unbalanced data is analyzed and presented. The Coil dataset [46], which is highly imbalanced and has a 94:6 ratio for class distribution, is used for empirical analysis. The proposed methodology followed a two phase approach. During the <sup>fi</sup>rst phase the available training data is used to train SVM. Later, the target values of the training data are replaced by the corresponding predictions of the trained SVM. During the second phase, this modi<sup>fi</sup>ed data is used to train MLP, LR, and RF separately.

Preprocessing using trained SVM modi<sup>fi</sup>ed the data in such a way that more instances are predicted as minority instances. Selection of many samples as the minority class instance is based on the decision boundary learnt by SVM during training. SVM predicted majority class instances as minority class instances if and only if the properties of that instance are similar to the minority class instance without compromising on the accuracy of the system, i.e., sensitivity of the unseen test set. It is observed that the proposed approach not only balanced the data but also provided more data for the minority class. This is because of the decision boundary learnt by SVM with high error rate which misclassi<sup>fi</sup>ed more majority class instances as minority class instances. Hence, the modi<sup>fi</sup>ed data at hand had more instances as minority class instances.

Intelligent approaches in the second phase learnt better about minority class instances from the modi<sup>fi</sup>ed training data and predicted the minority class instances in the unseen test data better. The performance of MLP, LR and RF is improved exceptionally using this modi-<sup>fi</sup>ed dataset. It is concluded that modifying the training data using SVM as a preprocessor in order to improve the number of instances for minority class without compromising on the accuracy of the system on unseen test cases is an alternate approach for dealing with unbalanced data. We reached this conclusion based on the empirical results pertaining to the Coil dataset. However, the results may vary with various dataset. For further analysis, ef<sup>fi</sup>ciency of SVM for feature selection can also be used to make the process simpler and faster, SVM can be used for reducing noise in the training data [38], and other intelligent classi<sup>fi</sup>ers can also be employed in the second phase, and other datasets can also be analyzed.

Table 5  
Results obtained using hybrid SVM-MLP approach.

<table><tr><td>Balancing technique</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>AUC</td></tr><tr><td>Original unbalanced</td><td>65.31</td><td>38.2</td><td>39.8</td><td>5175.5</td></tr><tr><td>SMOTE</td><td>67.23</td><td>45.45</td><td>46.75</td><td>5634</td></tr><tr><td>25% under-sampling</td><td>67.23</td><td>42.32</td><td>43.8</td><td>5477.5</td></tr><tr><td>50% under-sampling</td><td>64.71</td><td>37.11</td><td>38.75</td><td>5091</td></tr><tr><td>100% over-sampling</td><td>63.87</td><td>51.36</td><td>52.1</td><td>5761.5</td></tr><tr><td>200% over-sampling</td><td>65.55</td><td>40.86</td><td>42.32</td><td>5320.5</td></tr></table>

![](/api/attachments/GPT53WVX/fulltext/images/1ecd96b79bce5f0ecf41a3ef7ee0e1cdf3c6578a07c59f97526d85a84cd172dd.jpg)  
Fig. 3. Comparison of sensitivities obtained using MLP and SVM-MLP.

## Appendix A

This section provides a brief overview of the intelligent algorithms employed during phase two of the proposed approach, such as, Multi Layer Perceptron (MLP), Logistic Regression (LR), and Random Forest (RF).

## A.1. Multi layer perceptron

Arti<sup>fi</sup>cial Neural Network with more than one layer of adaptive weights was known as multi-layer perceptrons. A multilayer perceptron has three layers of units taking values in the range of 0 to 1. Each layer is nourished with the previous layers, and hence it is also called a Jump Connection Network [7]. MLPs can have any number of weighted connections, but networks with only two weighted connections are quite capable of approximating just about any functional mapping [5].

The MLP is mathematically represented by:

$$
y _ {k} = f _ {\text { outer }} \left[ \sum_ {j = 1} ^ {M} w _ {k j} ^ {(2)} f _ {\text { inner }} \left[ \sum_ {i = 1} ^ {d} w _ {j i} ^ {(1)} x _ {i} + w _ {j 0} ^ {(1)} \right] + w _ {k 0} ^ {(2)} \right]\tag{A.1}
$$

where y represents the kth output, $f _ { o u t e r }$ represents the output layer transfer function, $f _ { i n n e r }$ represents the input layer transfer function, w represents the weights and biases, and i represents the ith layer.

Table 6  
Results obtained using standalone LR.

<table><tr><td>Balancing technique</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>AUC</td></tr><tr><td>Original unbalanced</td><td>1.26</td><td>99.84</td><td>93.98</td><td>5055</td></tr><tr><td>SMOTE</td><td>56.3</td><td>73.42</td><td>72.4</td><td>6486</td></tr><tr><td>25% under-sampling</td><td>1.68</td><td>99.71</td><td>93.88</td><td>5069.5</td></tr><tr><td>50% under-sampling</td><td>3.36</td><td>99.12</td><td>93.42</td><td>5124</td></tr><tr><td>100% over-sampling</td><td>3.36</td><td>99.36</td><td>93.65</td><td>5136</td></tr><tr><td>200% over-sampling</td><td>10.08</td><td>98.09</td><td>92.85</td><td>5408.5</td></tr></table>

Table 7  
Results obtained using hybrid SVM-LR approach.

<table><tr><td>Balancing technique</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>AUC</td></tr><tr><td>Original unbalanced</td><td>63.03</td><td>41.63</td><td>42.9</td><td>5233</td></tr><tr><td>SMOTE</td><td>68.49</td><td>45.96</td><td>47.30</td><td>5722.5</td></tr><tr><td>25% under-sampling</td><td>70.17</td><td>40.14</td><td>41.93</td><td>5515.5</td></tr><tr><td>50% under-sampling</td><td>61.34</td><td>44.13</td><td>45.15</td><td>5273.5</td></tr><tr><td>100% over-sampling</td><td>66.39</td><td>49.15</td><td>50.18</td><td>5777</td></tr><tr><td>200% over-sampling</td><td>67.23</td><td>40.24</td><td>1.85</td><td>5373.5</td></tr></table>

## A.2. Logistic regression

Logistic regression has found wide acceptance as a model for describing the dependence of a binary response variable on a vector of explanatory variables. Maximum likelihood estimation method is used to <sup>fi</sup>t LR as it is a non-linear least square estimation problem. The dependent variable in LR is usually dichotomous, that is, the dependent variable can take the value 1 with a probability of success, or the value 0 with probability of failure. Although not as common and not discussed in this treatment, applications of logistic regression have also been extended to cases where the dependent variable is of more than two cases, known as multinomial or polytomous [45]. The goal of logistic regression is to correctly predict the category of outcome for individual cases using the most parsimonious model. The easy availability of LR in standard software packages is a major advantage of this technique.

## A.3. Random forest

RF, invented by Breiman [8], generates many classi<sup>fi</sup>cation trees. To classify a new object from an input vector, it puts the input vector down each of the trees in the forest. Each tree gives a classi<sup>fi</sup>cation and we say that the tree ‘votes’ for that class. The forest chooses the classi<sup>fi</sup>cation that has the most number of votes (over all of the trees in the forest). After each tree is built, all of the data are run down the tree and the proximities are computed for each pair of cases. If two cases occupy the same terminal node, their proximity is increased by one. At the end of the run, the proximities are normalized with respect to the number of trees. Proximities are used in replacing missing data, locating outliers, and producing low-dimensional views of the data.

RF is good in terms of generated accuracy among the current algorithms, runs ef<sup>fi</sup>ciently on large databases, gives estimates of what variables are important in the classi<sup>fi</sup>cation, and also offers an experimental method for detecting variable interactions.

![](/api/attachments/GPT53WVX/fulltext/images/f735a8200f8bfcd63024f85fadce4489bdb8742843942703a05fe75b91d12f65.jpg)  
Fig. 4. Comparison of sensitivities obtained using LR and SVM-LR.

Table 8  
Results obtained using standalone RF.

<table><tr><td>Balancing technique</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>AUC</td></tr><tr><td>Original unbalanced</td><td>7.14</td><td>98.22</td><td>92.8</td><td>5268</td></tr><tr><td>SMOTE</td><td>17.23</td><td>95.35</td><td>90.70</td><td>5629</td></tr><tr><td>25% under-sampling</td><td>10.08</td><td>98.11</td><td>92.88</td><td>5409.5</td></tr><tr><td>50% under-sampling</td><td>12.18</td><td>96.86</td><td>91.82</td><td>5452</td></tr><tr><td>100% over-sampling</td><td>10.08</td><td>97.47</td><td>92.27</td><td>5377.5</td></tr><tr><td>200% over-sampling</td><td>10.92</td><td>97.02</td><td>91.9</td><td>5397</td></tr></table>

Table 9  
Results obtained using hybrid SVM-RF approach.

<table><tr><td>Balancing technique</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>AUC</td></tr><tr><td>Original unbalanced</td><td>63.03</td><td>40.27</td><td>41.62</td><td>5165</td></tr><tr><td>SMOTE</td><td>67.23</td><td>45.51</td><td>46.8</td><td>5637</td></tr><tr><td>25% under-sampling</td><td>71.01</td><td>38.33</td><td>40.28</td><td>5467</td></tr><tr><td>50% under-sampling</td><td>60.5</td><td>43.2</td><td>44.22</td><td>5185</td></tr><tr><td>100% over-sampling</td><td>66.39</td><td>46.54</td><td>47.72</td><td>5646.5</td></tr><tr><td>200% over-sampling</td><td>68.91</td><td>36.12</td><td>38.07</td><td>5251.5</td></tr></table>

![](/api/attachments/GPT53WVX/fulltext/images/8d63cfe1b269833660f064879b54bba92c244867e50bc1f86669f489b605d20c.jpg)  
Fig. 5. Comparison of sensitivities obtained using RF and SVM-RF.

## References

[1] S.M. Alladi, S.P. Santosh, V. Ravi, U.S. Murthy, Colon cancer prediction with genetic pro<sup>fi</sup>les using intelligent techniques, Bioinformation 3 (3) (2008) 130–133.

[2] R. Barandela, J.S. Sánchez, V. García, E. Rangel, Strategies for learning in class imbalance problems, Pattern Recognition 36 (3) (2003) 849–851.

[3] G.E.A.P.A. Batista, M.C. Monad, A.L.C. Bazzan, Improving rule induction precision for automated annotation by balancing skewed data sets, Knowledge Exploration in Life Science Informatics 3303 (2004) 20–32.

[4] G.E.A.P.A. Batista, R.C. Prati, M.C. Monard, A study of the behaviour of several methods for balancing machine learning training data, ACM SIGKDD Explorations: Special Issue on Imbalanced Data Sets 6 (1) (2004) 20–29.

[5] C.M. Bishop, Neural Networks for Pattern Recognition, Oxford University Press, UK, 1995.

[6] I. Bose, X. Chen, Hybrid models using unsupervised clustering for prediction of customer churn, Journal of Organizational Computing and Electronic Commerce 19 (2) (2009) 133–151.

[7] M. Bosque, Understanding 99% of Arti<sup>fi</sup>cial Neural Networks, Writers Club Press, 2002.

[8] L. Breiman, Random forests, Machine Learning 45 (1) (2001) 5–32.

[9] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique Journal of Artificial Intelligence Research 16 (2002) 21–357.

[10] G. Cohen, M. Hilario, H. Sax, S. Hogonnet, A. Geissbuhler, Learning from imbalanced data in surveillance of nosocomial infection, Arti<sup>fi</sup>cial Intelligence in Medicine 37 (2006) 7-18.

[11] P. Domingos, MetaCost: a general method for making classi<sup>fi</sup>ers cost-sensitive, Proceedings of the 5th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Diego, CA, USA, 1999, pp. 155–164.

[12] T. Eitrich, A. Kless, C. Druska, W. Meyer, J. Grotendorst, Classi<sup>fi</sup>cation of highly unbalanced cyp450 data of drugs using cost sensitive machine learning techniques, Journal of Chemical Information and Modeling 47 (1) (2007) 92–103.

[13] A. Estabrooks, T. Jo, N. Japkowicz, A multiple resampling method for learning from imbalanced data sets, Computational Intelligence 20 (1) (2004) 18–36.

[14] M.A.H. Farquad, V. Ravi, S.B. Raju, Data mining using rules extracted from SVM: an application to churn prediction in bank credit cards, 12th International

Conference on Rough Sets, Fuzzy Sets, Data Mining, and Granular Computing, December 16–18, 2009, New Delhi, India, 2009, pp. 390–397.

[15] M.A.H. Farquad, V. Ravi, S.B. Raju, Rule extraction from Support Vector Machine using modi<sup>fi</sup>ed active learning based approach: an application to CRM, in: R. Setchi, et al., (Eds.), 14th International Conference on Knowledge-based and Intelligent Information and Engineering Systems, Part I, September 8–10, 2010, Cardiff, Wales, UK, 2010, pp. 461–470.

[16] T. Fawcett, An introduction to ROC analysis, Pattern Recognition Letters 27 (2006) 861–874.

[17] T. Fawcett, F. Provost, Adaptive fraud detection, Data Mining and Knowledge Discovery 1 (3) (1997) 291–316.

[18] H. Guo, H.L. Viktor, Learning from imbalanced data sets with boosting and data generation: the data boosting approach, SIGKDD Explorations 6 (1) (2004) 30–39.

[19] X. Guo, Y. Yin, C. Dong, G. Yang, G. Zhou, On the class imbalance problem, Fourth International Conference on Natural Computation, Jinan, China, 2008, pp. 192–201.

[20] I. Guyon, J. Weston, S. Barnhill, V.N. Vapnik, Gene selection for cancer classi<sup>fi</sup>cation using support vector machines, Machine Learning 46 (1–3) (2002) 389–422.

[21] H. Han, W.Y. Wang, B.H. Mao, Borderline-SMOTE: a new over-sampling method in imbalanced data sets learning Proceedings of the International Conference on Intelligent Computing 2005, Part I, Hefei, China, 2005, pp. 878–887.

[22] P.E. Hart, The condensed nearest neighbor rule, IEEE Transactions on Information Theory 18 (1968) 515–516.

[23] C.S. Hilas, Designing an expert system for fraud detection in private telecommunications networks, Expert Systems with Applications 36 (9) (2009) 11559–11569.

[24] Z. Huang, H. Chen, C.-J. Hsu, W.-H. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[25] K. Huang, H. Yang, I. King, M.R. Lyu, Learning classi<sup>fi</sup>ers from imbalanced data based on biased minimax probability machine, IEEE Computer Society Conference on Computer Vision and Pattern Recognition, Washington, DC, USA, 2004, pp. 558–563.

[26] N. Japkowicz, S. Stephen, The class imbalance problem: a systematic study, Intelligent Data Analysis 6 (5) (2002) 429–450.

[27] T. Jo, N. Japkowicz, Class imbalances versus small disjuncts, SIGKDD Explorations 6 (1) (2004) 40–49.

[28] K.J. Kim, Financial time series forecasting using support vector machines, Neurocomputing 55 (1/2) (2003) 307–319.

[29] I. Kononenko, Machine learning for medical diagnosis: history, state of the art and perspective, Arti<sup>fi</sup>cial Intelligence in Medicine 23 (1) (2001) 89–109

[30] S. Kotsiantis, D. Kanellopoulos, P. Pintelas, Handling imbalanced datasets: a review, GESTS International Transactions on Computer Science and Engineering 30 (1) (2006) 25–36.

[31] M. Kubat, S. Matwin, Addressing the curse of imbalanced training sets: one sided selection, 14th International Conference on Machine Learning, Nashville, TN, USA, 1997, pp. 179–186.

[32] M. Kubat, R. Holte, S. Matwin, Machine learning for the detection of oil spills in satellite radar images, Machine Learning 30 (2–3) (2004) 195–215.

[33] J. Laurikkala, Improving identi<sup>fi</sup>cation of dif<sup>fi</sup>cult small classes by balancing class distribution, Arti<sup>fi</sup>cial Intelligence in Medicine 2101 (2001) 63–66.

[34] W. Lee, S. Stolfo, K. Mok, Mining in a data-<sup>fl</sup>ow environment: Experience in network intrusion detection. 5th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Diego, CA, USA, 1999 pp. 114–124

[35] C.X. Ling, C. Li, Data mining for direct marketing problems and solutions, Proceedings of the 4th International Conference on Knowledge Discovery and Data Mining, New York, New York, USA, 1998, pp. 73–79.

[36] Y. Liu, N.V. Chawla, M.P. Harper, E. Shrilberg, A. Stolcke, A study in machine learning from imbalanced data for sentence boundary detection in speech, Computer Speech and Language 20 (4) (2006) 468–494.

[37] M. Maloof, Learning when data sets are imbalanced and when costs are unequal and unknown, Proceedings of the ICML 2003 Workshop on Learning from Imbalanced Datasets, Washington, DC, USA, 2003, pp. 73–80.

[38] M. Mannino, Y. Yang, Y. Rhu, Classi<sup>fi</sup>cation algorithm sensitivity to training data with non representative attribute noise, Decision Support Systems 46 (3) (2009) 743–751.

[39] M.C. Monard, G.E.A.P.A. Batista, Learning with skewed class distribution, Ad vances in Logic, Arti<sup>fi</sup>cial Intelligence and Robotics (2002) 173–180.

[40] P. Ravisankar, V. Ravi, G.R. Rao, I. Bose, Detection of <sup>fi</sup>nancial statement fraud and feature selection using data mining techniques, Decision Support Systems 50 (2) (2011) 491–500

[41] D. Sanchez, M.A. Vila, L. Cerda, J.M. Serrano, Association rules applied to credit card fraud detection, Expert Systems with Applications 36 (2) (2009) 3630–3640.

[42] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Surveys 34 (1) (2002) 1–47.

[43] D. Stoneking, Improving the manufacturability of electronic designs, IEEE Spectrum 36 (6) (1999) 70–76.

[44] A. Sun, E.-P. Lim, Y. Liu, On strategies for imbalanced text classi<sup>fi</sup>cation using SVM: a comparative study, Decision Support Systems 48 (1) (2009) 191–201.

[45] B.G. Tabachnick, L.S. Fidell, Logistic regressionRetrieved on October 10, 2011, from, http://userwww.sfsu.edu/\~efc/classes/biol710/logistic/logisticreg.htm1996.

[46] CoIL Challenge 2000: the insurance company case, in: P. van der Putten, M. van Someren (Eds.), Leiden Institute of Advanced Computer Science Technical Report 2000–09, June 22, 2000.

[47] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer-Verlag, New York, USA, 1995.

[48] V.N. Vapnik, The Nature of Statistical Learning Theory, 2nd edition Springer-Verlag, New York, USA, 1998.

[49] S. Visa, A. Ralescu, Issues in mining imbalanced data sets — a review paper, Proceedings of the 16th Midwest Arti<sup>fi</sup>cial Intelligence and Cognitive Science Conference Dayton, OH, USA, 2005, pp. 67–73.

[50] G.M. Weiss, Learning with rare cases and small disjuncts, Proceedings of the 12th International Conference on Machine Learning, Tahoe City, CA, USA, 1995, pp. 558–565.

[51] G.M. Weiss, Mining with rarity: a unifying framework, SIGKDD Explorations 6 (1) (2004) 7–19.

[52] D.L. Wilson, Asymptotic properties of nearest neighbor rules using edited data, IEEE Transactions on Systems, Man, and Cybernetics 2 (1972) 408–420.

[53] G. Wu, E. Chang, Class-boundary Alignment for Imbalanced Dataset Learning, ICML 2003 Workshop on Learning from Imbalanced Data Sets, Washington, DC, USA, , 2003.

[54] X. Wu, V. Kumar, J.R. Quinlan, J. Ghosh, Q. Yang, H. Motoda, G.J. McLachlan, A. Ng B. Liu, P.S. Yu, Z.-H. Zhou, M. Steinbach, D.J. Hand, D. Steinberg, Top 10 algorithms in data mining, Knowledge and Information Systems 14 (1) (2008) 1–37.

[55] C. Yang, Web user behavioral pro<sup>fi</sup>ling for user identi<sup>fi</sup>cation, Decision Support Systems 49 (3) (2010) 261–271.

![](/api/attachments/GPT53WVX/fulltext/images/2f6ed05593072f0e9d2bea7f2bbea14cbcc0d9bad8a1a971adc55b412bcb63e4.jpg)

Mohammed Abdul Haque Farquad is a Research Assistant at the School of Business, The University of Hong Kong. He holds a Ph.D. in Computer Science from University of Hyderabad, Hyderabad, India. His research interests include data mining, soft computing, banking, <sup>fi</sup>nance, and customer relationship management. His research work has been published in Expert Systems with Applications, International Journal of Information and Decision Sciences, and in various Proceedings of International Conferences published by IEEE and Springer. He is an ad-hoc referee for Information Sciences Journal, Knowledge Based System Journal and various IEEE International Conferences. He is a Program Committee member of International Conference on Data Mining 2011, Las Vegas and also a Technical committee member of the 3rd International Conference on Computer Technology and Development, China.

![](/api/attachments/GPT53WVX/fulltext/images/396924255b9195fb4548810a88f5d243ad0d8f9675fad2e7606fd617afc41ed7.jpg)

Indranil Bose is Full Professor at the Indian Institute of Management Calcutta. He holds a B. Tech. from the Indian Institute of Technology, MS from the University of Iowa, and MS and Ph.D. from Purdue University. His research interests are in telecommunications, data mining, information security, and supply chain management. His publications have appeared in Communications of the ACM, Communications of AIS, Computers and Operations Research, Decision Support Systems, Ergonomics, European Journal of Operational Research, Information & Management, Journal of Organizational Computing and Electronic Commerce, Journal of the American Society for Information Science and Technology, Operations Research

Letters, etc. He is listed in the International Who's Who of Professionals 2005–2006, Marquis Who's Who in the World 2006, Marquis Who's Who in Asia 2007, Marquis Who's Who in Science and Engineering 2007, and Marquis Who's Who of Emerging Leaders 2007. He serves on the editorial board of Information & Management, Commu nications of AIS, and several other IS journals.
