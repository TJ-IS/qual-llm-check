---
otero_id: 13242
otero_key: "3E6YQXVG"
title: "Two-stage consumer credit risk modelling using heterogeneous ensemble learning"
authors: "Monika Papouskova; Petr Hajek"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.01.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Two-stage consumer credit risk modelling using heterogeneous ensemble learning

Monika Papouskova, Petr Hajek

![](/api/attachments/3E6YQXVG/fulltext/images/d25679d765e41f69ef04746d0bf3d86a8c43f7bd1a0789d137ae70818437c174.jpg)

Institute of System Engineering and Informatics, Faculty of Economics and Administration, University of Pardubice, Studentska 84, Pardubice, Czech Republic

## A R T I C L E I N F O

Keywords: Credit risk Ensemble learning Credit scoring Expected loss Exposure at default

## A B S T R A C T

Modelling consumer credit risk is a crucial task for banks and non-bank financial institutions to support decisionmaking on granting loans. To model the overall credit risk of a consumer loan in terms of expected loss (EL), three key credit risk parameters must be estimated: probability of default (PD), loss given default (LGD) and exposure at default (EAD). Research to date has tended to model these parameters separately. Moreover, a neglected area in the field of LGD/EAD modelling is the application of ensemble learning, which by benefitting from diverse base learners reduces the over-fitting problem and enables modelling diverse risk profiles of defaulted loans. To overcome these problems, this paper proposes a two-stage credit risk model that integrates (1) class-imbalanced ensemble learning for predicting PD (credit scoring), and (2) an EAD prediction using a regression ensemble. Furthermore, multi-objective evolutionary feature selection is used to minimize both the misclassification cost (root mean squared error) of the PD and EAD models and the number of attributes necessary for modelling. For this task, we propose a misclassification cost metric suitable for consumer loans with fixed exposure because it combines opportunity cost and LGD. We show that the proposed credit risk model is not only more efective than single-stage credit risk models but also outperforms state-of-the-art methods used to model credit risk in terms of prediction and economic performance.

## 1. Introduction

Credit risk modelling uses empirical models to support decisionmaking in both commercial (corporate) and consumer (retail) credit businesses. The latter sector has gained much attention in the literature due to its economic importance. Notably, total outstanding U.S. consumer credit in 2017 was reportedly 3.84 trillion, more than double the balance in 2000. To manage their consumer loan portfolios, banks and non-bank financial institution employ various credit risk measures. Expected loss (EL) is the most important of these, calculated as PD × EAD × LGD, where PD is the probability of default, EAD is ex posure at default, and LGD is loss given default. PD, also known as a credit score, refers to the probability that a client will default on their loan over a particular time horizon. EAD represents the expected size of the exposure at the time of default. The LGD is the proportion of a given exposure that is expected to be lost if the client defaults.

A vast amount of literature concerns the automatic estimation of PD using machine learning methods [1,2]. Modelling PD is usually approached as a strongly imbalanced classification task aiming to predict defaulted and non-defaulted loans, so that the PD can be assigned to loans based on the respective classifier's confidence. However, this credit risk parameter is insuficient to assess the loans' overall credit risk, as defaulted loans lead to diferent economic losses for the lending institution.

Previous evidence suggests that investing on potential defaulted loans may result in huge economic losses, thus misclassifying a defaulted loan outweighs misclassifying a non-defaulted loan [3]. This finding has recently led researchers to study cost-sensitive [4] and profit-based credit scoring models [5]. However, these studies have not considered the fact that diferent defaulted loans can be associated with diferent cost. Indeed, defaulted loans can eventually be profitable [6]. This issue has been addressed in profit scoring decision support systems [6], which aimed to predict profitability (efective interest rate) of each consumer loan. Efective interest rate is higher for risky loans but it is based on the credit risk calculated using PD models, which is only one of the components of consumer credit risk. Therefore, such measures are not fully adequate to model the loans' overall credit risk and recent literature on credit risk modelling has suggested that the focus of attention move from PD prediction to other key problems, such as scorecard recalibration and LGD/EAD modelling [7]. Modelling LGD and EAD hold particular interest for credit market participants, as these parameters are used respectively to calculate capital requirements and risk-weighted assets. In addition, both parameters serve as important inputs into several models, including stress testing and economic capital models [8]. Therefore, interest has recently increased in LGD [9] and EAD [10] modelling. Predicting these parameters is challenging because LGD and EAD do not follow the normal distribution; specifically, a large proportion of defaulted loans is either fully recovered or not recovered at all [11]. This problem of distribution becomes even more serious when combined with the imbalance usually present in PD modelling. Moreover, previous models have not adequately addressed this problem and LGD/EAD models have been employed separately from PD models, preventing the modelling of the overall EL. Finally, most previous studies have been limited to the use of single LGD/EAD prediction methods, thus paying far too little attention to ensemble learning [12]. This is surprising, because recent studies have shown that ensemble methods generally outperform single predictors in modelling PD [7,13]. We hypothesize that ensemble methods do equally well in LGD/EAD modelling because defaulted loans exhibit diverse risk profiles and thus make it challenging to model consumer credit risk [14]. Heterogeneous ensemble methods enable modelling this diversity by using diferent base learners.

To overcome the above-mentioned problems, in this study we pro pose a novel integrated, two-stage credit risk model. The first stage involves traditional PD modelling using classifier ensembles to distinguish between two classes of loans, namely defaulted (with EL > 0) and non-defaulted (EL = 0) loans. Related studies have shown that imbalance in the class distribution of loans significantly decreases performance on the minority class of defaulted loans [15,16]. To address the problem of imbalanced classes, we undersample the majority class of non-defaulted loans in this stage. In addition, we propose a misclassification cost performance metric for consumer PD modelling. In agreement with credit market theory [17,18], this metric considers both the cost of accepting a defaulted loan and the cost associated with rejecting a loan (opportunity cost). Here we show that the ratio between these cost measures is surprisingly low for a non-bank financial institution mainly due to higher loan interest rates compared with credit products provided by P2P electronic platforms. Those loans identified as potentially defaulting enter the second stage, which esti mates the EAD of these loans using a regression ensemble. More precisely, heterogeneous ensemble methods are used in both stages, com bining a number of diferent base learners to achieve higher diversity necessary for modelling diferent risk profiles. Finally, the two prediction models (PD and EAD) are combined to predict the overall EL. We show that this approach not only outperforms state-of-the-art methods used in LGD/EAD modelling but it is also more accurate than PD and EAD models used separately. We also demonstrate its implications on the economic performance of consumer loan portfolio.

The rest of this paper is divided into five sections. Section 2 briefly overviews related literature on credit risk modelling using machine learning methods. In Section 3, we outline a new credit risk model. Section 4 describes the consumer credit risk datasets used and their pre processing. In Section 5, we present the results of the modelling and compare them with state-of-the-art methods used in credit risk modelling. Section 6 discusses the results obtained. The final section draws conclusions, outlines the limitations of the proposed model and ofers suggestions for future research.

## 2. Modelling consumer credit risk using machine learning methods: literature review

A considerable number of studies has been published on consumer credit risk modelling using machine learning methods. These studies can be divided into two groups: (1) PD prediction (credit scoring), and (2) predicting the LGD/EAD.

## 2.1. PD prediction

Credit scoring aims to assign a score to a loan based on the prediction of a classification algorithm. This credit score is represented by the predicted PD. A comprehensive comparison of state-of-the-art classification algorithms can be found in [7]. This benchmark study employed both individual classifiers, such as Neural Networks (NNs), Support Vector Machines (SVMs), and Extreme Learning Machines (ELMs), and ensemble classifiers, such as Random Forest (RF), stochastic gradient boosting, and ensemble selection. The authors concluded that ensemble classifiers generally outperform individual classifiers in modelling PD. More precisely, RF and ensemble selection classifiers performed best among all the tested homogenous and heterogeneous ensemble methods, respectively, agreeing well with earlier related work [19–21].

Homogenous ensemble methods, such as bagging or boosting, develop an ensemble of base learners that represent a single classification algorithm but which difer in the ways they manipulate the training data or the input and output attributes. To obtain the final classification, the base learners are usually combined by majority or weighted voting [22]. Recent empirical evidence suggests that Credal Decision Trees (CDT) can be used as efective base learners in modelling PD [13].

In contrast to the homogenous methods, heterogeneous ensemble methods combine diferent classification algorithms to achieve a higher diversity of base learners that can better complement each other [23,24]. Besides simple or weighted voting, there are more complicated methods to combine base learners [25]. For example, Deep Neural Networks (DNNs) have shown good performance in combining individual predictions of ELMs [26].

It is also possible to optimize base learners' selection. The objective of ensemble selection methods is to select the best subset of base learners from a given set. Specifically, ensemble selection methods either maximize the ensemble's classification accuracy or optimize its diversity [27]. For example, the correlations among selected base learners have been minimized in ensembles of NNs [28] and SVMs [29].

Although ensemble methods have generally outperformed single classifiers in the above-mentioned studies, recent literature suggests that credit scoring models based on DNNs can ofer highly competitive classification accuracy [30,31]; these models allow an approximation of any distribution over the input–output space representing loan applicants.

Another problem with modelling PD using machine learning is that most real-world credit scoring datasets are imbalanced in favour of nondefaulted loans. In fact, the accuracy of machine learning models can be significantly improved by using resampling techniques to balance the training data [15,32]. Oversampling the minority class of defaulted loans was preferred in [15], while undersampling the majority class of non-defaulted loans was found efective in [16]. The results obtained in [16] specifically indicate that ensemble methods, such as RF and gradient boosting, perform well in the credit scoring context. An informed undersampling approach was proposed in [33] to control the imbalance ratio of the classes. Instead of resampling, cost-sensitive classifiers can be applied that assign higher weights to the samples in the minority class [34].

## 2.2. Prediction of LGD and EAD

Until recently, modelling credit risk using machine learning methods was limited to modelling PD, which is, however, only one component of current credit risk models. To estimate a loan's overall credit risk, it is also necessary to predict LGD and EAD.

LGD measures loss in terms of a percentage of the EAD [11]. Importantly, the above-mentioned credit scoring models usually use binary classifiers, whereas LGD models are considered regression problems. In other words, the former approach classifies loans into defaulted and non-defaulted, while the latter approach predicts losses from defaulted loans. Traditional methods used to solve this problem include Linear Regression (LR) [35] and single regression trees [36]. However, non-linear regression models, such as Support Vector Regression (SVR), significantly outperformed LR in predicting the LGD of corporate bonds [37]. Similarly, for modelling PD, the performance of single predictors can be improved by combining diverse methods. For this reason, Fuzzy Decision Fusion (FDF) was used to combine multiple predictions, including those of LR, SVR and regression trees [12]. Moreover, even better performance can be achieved by using a twostage methodology, which utilizes the fact that LGD datasets are typically strongly imbalanced in favour of zero or full loan recovery. For example, in a first stage, SVMs were used to classify zero recovery compared to non-zero recovery, and then SVR was applied to the latter category to predict LGD [9].

The EAD parameter is defined as the expected exposure (including unpaid interest and fees) upon loan default. The problem of EAD prediction depends on the loan characteristics. For fixed exposures, such as personal loans and residential mortgages, EAD is simply the amount outstanding at the time of calculation. For revolving exposures, on the other hand, EAD is divided into drawn and undrawn commitments. Then, prediction models are developed to predict EAD either directly or indirectly by predicting the so-called credit conversion factor, which is defined as the percentage of the current undrawn commitments drawn down upon default [8]. Initial studies of EAD prediction favoured indirect approaches [38], but it has recently been demonstrated that both approaches perform similarly well [8]. To predict EAD at any time over the loan period, a mixture model was proposed that combines two panel models with random efects to estimate respectively the expected balance and expected loan limit. However, all these approaches were limited to prediction of EAD alone (Table 1).

## 3. Two-stage consumer credit risk model

## 3.1. Conceptual framework

As reported in [9], single-stage statistical models assume that all loans are generated from the same distribution; thus, they fail to estimate LGD because its values usually concentrate on the boundaries at 0 (full loan recovery) or 1 (no loan recovery). This issue can be addressed by first employing a classifier to separate loans at the boundaries from those remaining and only then using a regression model to estimate LGD. Motivated by this observation, we propose to separate potentially defaulting loans with EL > 0 in a first stage and only then to predict the loans' EAD. The proposed conceptual framework is presented in Fig. 1. First, the data were divided into training and testing sets using 10 times repeated five-fold cross-validation [13]. To overcome the problem of highly imbalanced classes in the first stage, we employed EUSBoost [40], a state-of-the-art, evolutionary undersampling algorithm based on ensembles. We will demonstrate that this approach is more efective than the SMOTEBagging oversampling method [41].

Table 1  
Summary of previous studies on modelling consumer credit risk.

<table><tr><td>Study</td><td>Credit risk parameter</td><td>Method</td></tr><tr><td>[20]</td><td>PD</td><td>Heterogeneous ensemble learning</td></tr><tr><td>[21]</td><td>PD</td><td>SVM ensemble learning</td></tr><tr><td>[19]</td><td>PD</td><td>Bagging</td></tr><tr><td>[22]</td><td>PD</td><td>NN ensemble learning</td></tr><tr><td>[30]</td><td>PD</td><td>DNN</td></tr><tr><td>[7]</td><td>PD</td><td>RF, ensemble selection classifiers</td></tr><tr><td>[23,24]</td><td>PD</td><td>Heterogeneous ensemble learning</td></tr><tr><td>[26]</td><td>PD</td><td>ELM ensemble learning + DNN</td></tr><tr><td>[31]</td><td>PD</td><td>DNN</td></tr><tr><td>[35]</td><td>LGD</td><td>LR</td></tr><tr><td>[36]</td><td>LGD</td><td>Regression trees</td></tr><tr><td>[11]</td><td>LGD</td><td>LR(LogR) + SVR, LR(LogR) + NN</td></tr><tr><td>[37]</td><td>LGD</td><td>SVR</td></tr><tr><td>[12]</td><td>LGD</td><td>FDF</td></tr><tr><td>[9]</td><td>LGD</td><td>SVM + SVR</td></tr><tr><td>[38]</td><td>EAD</td><td>NN, Boosting, Mixture model</td></tr><tr><td>[8]</td><td>EAD</td><td>Mixture model</td></tr><tr><td>[10]</td><td>EAD</td><td>Mixture model</td></tr><tr><td>[39]</td><td>EAD</td><td>LR</td></tr><tr><td>This study</td><td>PD + EAD</td><td>Class-imbalanced heterogeneous classification ensemble + heterogeneous regression ensemble</td></tr></table>

Legend: DNN – Deep Neural Network, FDF – Fuzzy Decision Fusion. ELM - Extreme Learning Machine, LogR – Logistic Regression, LR – Linear Regression, NN – Neural Network (Multilaver Perceptron). RF – Random Forest. SVM - Support Vector Machine, SVR – Support Vector Regression.

Since heterogeneous ensemble learning performed best in previous studies of PD modelling (e.g., see the benchmark study in [7]), we apply this approach at both stages of credit risk modelling. Specifically, we use a stacking method that combines multiple prediction models (base models) through a meta-learning algorithm. More precisely, the base models are first trained on complete training data, and then the metalearning algorithm (meta-classifier or meta-regressor) is trained on the outputs of the base models. This model is heterogeneous, because the base models are represented by diferent learning algorithms. To further improve the performance of our model in both stages, we use nonlinear meta-classifier and meta-regressor algorithms instead of the traditional LogR and LR algorithms, respectively. In addition, a feature selection strategy is employed at both stages to increase the accuracy of prediction.

## 3.2. Undersampling majority class

As noted above, class imbalance has been considered a challenging problem in the literature on credit scoring. This refers to the situation where each class in the data is represented by a very diferent number of instances. For credit scoring, non-defaulted loans usually strongly prevail over defaulted loans in the dataset, which may significantly deteriorate the performance of classification algorithms, as these expect balanced data. Therefore, resampling (undersampling or oversampling) techniques have been used in previous studies to balance defaulted and non-defaulted loans [15,16,32]. Here, we use an undersampling approach, because, when combined with ensemble learning, it outperformed oversampling in an extensive comparative study on modelling PD [16]. Specifically, we employ the EUSBoost algorithm [40], based on RUSBoost, which integrates random undersampling and boosting. The main drawback of random undersampling is that it can discard potentially useful instances of the majority class. To overcome this problem, EUSBoost benefits from evolutionary undersampling, which favours diversity of the selected instances. More precisely, each chromosome consists of all instances in the majority class, represented by either value 0 (not included) or 1 (included). The fitness function considers both the geometric mean of true positive and true negative rates of the 1NN (nearest neighbour) classifier and the balance of the minority and majority classes. Global diversity of the selected instances, which is also an important part of the fitness function, was measured using the Q-statistic, one of the most common measures of diversity used in classifier ensembles [40].

## 3.3. Feature selection

Related studies have demonstrated that the prediction performance of credit risk models can be significantly improved using feature selection [24,42,43]. This step aims to improve model accuracy and stability by choosing a subset of only relevant input attributes. Thus, irrelevant and redundant attributes are removed and the dimensionality of the feature space is reduced. This may have considerable importance for credit risk models, because managers can better understand the determinants of loan defaults and the attributes' acquisition costs can be reduced [44,45].

![](/api/attachments/3E6YQXVG/fulltext/images/477d34e034f7d0477808196e7dc27f90a8593866702c57a05db24ca520a5b63d.jpg)  
Fig. 1. Conceptual framework for credit risk modelling.

Feature selection is an NP-hard problem that can be solved by three types of methods, namely filters, wrappers and embedded methods [46]. Filters evaluate the relevance of attributes based on data characteristics, without involving any learning algorithm. Embedded methods evaluate attribute importance while training a prediction model in order to avoid model overfitting. To improve the performance of the prediction model, wrappers use an enumeration algorithm that searches the space of attribute subsets. This usually leads to higher accuracy compared to filters, achieved at the cost of computational load.

As hinted above. two main obiectives should be considered in de. signing feature selection for credit risk modelling: maximizing the accuracy of the prediction model and minimizing the number of attributes to improve the model's interpretability and reduce attribute acquisition costs. However, these two objectives often conflict with one another. To overcome this problem, here we propose to use multi-objective evolutionary feature selection (MOEFS), which has recently been efectively used in related business applications [47]. This method uses a MOEFS algorithm called ENORA (Evolutionary NOn-dominated Radial slotsbased Algorithm) to minimize both the number of selected features and the prediction error of the RF method. This is advantageous because RF is considered a state-of-the-art benchmark algorithm in credit risk modelling [7].

Although feature selection has been successfully applied to remove redundant attributes in several credit scoring models [46,48], to the best of our knowledge, no previous study has attempted to select attributes based on multiple obiectives. Here, we use MOEFS to minimize the number of selected attributes on the one hand while minimizing the misclassification cost (MC) of the PD prediction model on the other hand. The calculation of the misclassification cost is introduced in Section 3.5.

## 3.4. Heterogeneous classification and regression ensemble

Heterogeneous classification/regression ensemble methods are sets of diferent classifiers/regressors whose individual (base) predictions are combined to improve accuracy by increasing the diversity and complementarity of the base predictors. Voting (majority, weighted or probabilistic) is typically used as a baseline method for combining the base predictors. However, the accuracy of the heterogeneous ensemble can be significantly improved by applying more complicated combination methods, such as stacking (stacked generalization) [49]. This algorithm comprises two main steps. First, a set of base predictors is generated. Then, the predictions from the first step are used to train a meta-classifier/meta-regressor. In other words, the predictions of the base learners are used as features of the meta-learning algorithm.

In the related literature, stacking has been successfully used to predict PD, that is, in credit scoring (see [7,50] for comparative studies). With a small number of base predictors, LogR is typically used as the meta-learning algorithm [50]. However, non-linear classifiers more efectively handle the meta-learning of higher-dimensional base predictions [51]. The meta-learning algorithm should also be robust against the multicollinearity of the base predictions [7]. To overcome these problems, here we examine two meta-learning algorithms: LogR and RF. As base learners, we utilize state-of-the-art learning algorithms previously used in credit risk modelling.

The stacking algorithms for modelling PD and EAD are presented in Algorithms 1 and 2, respectively. PD modelling is performed by a heterogeneous classification ensemble, while a heterogeneous regression ensemble is used for modelling EAD.

Diferent base classifiers and regressors were included for modelling PD and EAD, respectively, such as decision and regression trees, homogeneous ensemble methods (e.g., boosting, bagging), NNs and SVMs. Thus, diversity for the meta-learning algorithms is guaranteed.

Algorithm 1. Stacking algorithm for PD modelling.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs: training data  $D_{1}=\{x_{i},PD_{i}\}$ ,  $PD_{i}\in\{0,1\}$ , i=1,...,N, base classifiers  $c_{1},...,c_{j},...,c_{h}$ , where h is the number of base classifiers
Output: ensemble classifier C
For j=1 to h {
    learn base classifier  $c_{j}$  on  $D_{1}$ }
For i=1 to N {
    construct new data  $D_{1c}$  of predictions  $D_{1c}=\{x_{i}^{\prime},PD_{i}\}$ , where  $x_{i}^{\prime}=\{c_{1}(x_{i}),...,c_{h}(x_{i})\}$ 
Learn a meta-classifier C on  $D_{1c}$ ;
return C;
</div>

## Algorithm 2. Stacking algorithm for EAD modelling.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs: training data  $D_{z}=\{x_{i},EAD_{i}\}$ ,  $EAD_{i}\in(0,1]$ ,  $i=1,\ldots,n$ , base regressors  $r_{1},\ldots,r_{k},\ldots,r_{m}$ , where m is the number of base regressors
Output: ensemble regressor R
For k=1 to m {
    learn base regressor  $r_{k}$  on  $D_{2}$ }
For i=1 to n {
    construct new data  $D_{2x}$  of predictions  $D_{2x}=\{x_{i}',EAD_{i}\}$ , where  $x_{i}'=\{r_{1}(x_{i}),\ldots,r_{n}(x_{i})\}$ 
Learn a meta-regressor R on  $D_{2x}$ ;
return R;
</div>

Regarding PD modelling (credit scoring), LogR, MLP, SVM, C4.5 and CDT performed best as base predictors in a comparative study of credit scoring using ensemble learning [13]. Hoefding Decision Trees were used as base classifiers in adaptive RFs, outperforming bagging and boosting on a credit scoring dataset [52]. Similarly, other homogeneous ensemble learning algorithms have been efectively used in related studies on credit scoring, including MultiBoostAB [53], AdaBoostM1 [54], LogistBoost [55], bagging [56], RF [7], Decorate [13], Random Subspace [56] and Rotation Forest [13]. Forest PA (Penalizing Attri butes) is a recent decision forest algorithm that has been applied to credit scoring [57]. This algorithm not only examines the strength of all features but also promotes diversity of the constructed trees by pena lizing those features used in the latest tree.

Meta-learning algorithms previously used in related studies include DNNs [26], SVM [7], Rotation Forest [58] and boosting [51]. RF was selected here because it is considered a state-of-the-art benchmark algorithm in the credit scoring literature [7]. Note that for the purpose of comparison, LogR was also tested as a meta-classifier.

To model EAD, we adopted the following approaches in selecting base regressors and meta-regressors. For base regressors, we considered those methods used previously to modelling LGD and EAD, including LR, regression trees (M5P [59], REP Tree [60], Random Tree [60] and Alternating Model Tree [60]), SVR [9] and MLP [38]. Additionally, homogeneous ensemble methods (Rotation Forest [13], Additive Re gression [60], bagging [56], Random Subspace [56] and RF [7]) were used in modelling EAD, motivated by their observed efectiveness in previous empirical studies of modelling PD. Similarly, the regression variants of the algorithms used in modelling PD were also employed as meta-learning algorithms in modelling EAD.

In a credit scoring benchmark study in [7], selective ensemble strategies outperformed those without the selection of base predictors in terms of accuracy. Therefore, to maximize prediction accuracy, a subset of base predictors was selected using the MOEFS method in troduced in Section 3.3. Recall that we employ MOEFS for variable and ensemble selection in the first and second stage of the proposed framework, respectively (see Fig. 1). The MOEFS method selects feature subsets based on two objectives: (1) the number of base learners and (2) the prediction performance of the meta-learning algorithm. This step not only reduces the dimensionality of the feature space, thus making the algorithm's learning more efective, but it can also improve prediction accuracy by considering specific requirements of the metalearning algorithm [7]. Since it is usually dificult to search the space of feature subsets exhaustively, heuristic algorithms have been efectively used for search instead. Here, we use the ENORA algorithm to minimize the MC of the meta-classifier in modelling PD and to minimize the RMSE (Root Mean Squared Error) of the meta-regressor in modelling EAD. The measures used to evaluate the performance of both models are presented in the next section.

The predictors were learnt using the settings presented in the Appendix. To avoid overfitting in the meta-learning stage, appropriate data organization is required. Therefore, no hyper-parameter optimization was performed for base predictors and the same data partitions (without overlap) were used in both stages of modelling.

## 3.5. Performance evaluation

To evaluate the suitability of the classification and regression ensemble models presented above, we used standard classification and regression performance measures that have been previously applied in the domain of credit risk modelling [9,27,61]. In addition, we propose a measure of misclassification cost to consider the financial consequences of diferent types of error.

## 3.5.1. Performance metrics for modelling PD

Standard performance measures used to evaluate PD models include accuracy (Acc) and area under the receiver operating characteristic curve (AUC). Accuracy is calculated as follows, based on the confusion matrix (Table 2) as the percentage of correctly classified loans:

$$
A c c = \frac {T P + T N}{T P + F P + F N + T N},\tag{1}
$$

where TP, TN, FP and FN are the numbers of instances classified as true positive, true negative, false positive and false negative, respectively.

On the one hand, the wrong prediction of a loan that is unrecovered (type I error) leads to the loss of investment. On the other hand, predicting an unrecovered loan when it would be fully recovered (type II error) may result in the loss of potential interest (the so-called opportunity cost). Several credit scoring studies have combined these two errors into a MC [1], which is considered a crucial criterion in the evaluation of credit scoring effectiveness [611. However. this measure has rarely been utilized as the objective criterion in learning by prediction models [34]. In other words, previous literature has inadequately studied cost-sensitive credit risk modelling. Inspired by the example-dependent, cost-sensitive approach used for modelling PD in [34], here we propose a MC metric that combines LGD and opportunity cost as follows:

$$
M C = F P R * L G D + F N R * (r + (- r * \pi_ {P o s} + L G D * \pi_ {N e g})),\tag{2}
$$

where FPR is the false positive rate (1–TNR); FNR is the false negative rate (1–TPR); $\pi _ { P o s }$ is the percentage of positive loans, ${ \pi } _ { P o s } = ( \mathrm { T P } + \mathrm { F N } ) /$ (TN + FP + FN + TN), $\mathfrak { T } _ { N e g }$ is the percentage of negative loans, π = (TN + FP)/(TN + FP + FN + TN); r is the average profit (in terest) rate; and LGD is computed as follows:

$$
L G D = 1 - \frac {\text { recoveries } - \text { collection   recovery   fee }}{\text { outstanding   loan   amount }}.\tag{3}
$$

The main notable diference between the proposed measure of MC and that defined in [34] is that the proposed measure is expressed in relative terms and is not example-dependent (that is, r is not reported for each loan separately and individual credit lines are not considered). This has two advantages; it makes relative MC more interpretable for investors, and it means the results of diferent prediction models can be easily compared over multiple datasets. Another related measure used in earlier research is Expected Maximum Profit (EMP) [5,62], which aims to select the classifier with the highest profit. This alternative approach takes the benefits of granting loans into account, thus providing a straightforwardly interpretable financial measure that can be used with all classification algorithms. However, this approach does not consider the cost associated with rejecting a loan (opportunity cost). Moreover, EMP is expressed in absolute units and therefore cannot be used to compare the performance of prediction models over multiple datasets.

Table 2  
Confusion matrix for modelling PD.

<table><tr><td>Prediction/target</td><td>Positive</td><td>Negative</td></tr><tr><td>Positive (non-defaulted loan)</td><td>TP</td><td>FP (type I error)</td></tr><tr><td>Negative (defaulted loan)</td><td>FN (type II error)</td><td>TN</td></tr></table>

AUC is defined in [63] as the probability that the prediction model ranks a randomly chosen positive instance higher than a randomly chosen negative instance. In the literature on credit risk modelling, AUC was reported to be a suitable performance measure, mainly because it is robust against imbalanced data:

$$
A U C = \int_ {0} ^ {1} T P R (T) * \frac {d}{d T} F P R (T) d T,\tag{4}
$$

where T is any cut-of point, $0 \textless T \textless 1$ . As many classifiers provide a confidence score s of the classification for each instance i, the cut-of point T can be specified to calculate all the above-mentioned performance metrics. To estimate the optimal cut-of value, here we adopt the approach developed for credit scoring [5], considering the ratio λ of cost for TPR and FPR, respectively, as follows:

$$
\lambda = \frac {(r + (- r ^ {*} \pi_ {P o s} + L G D ^ {*} \pi_ {N e g})) * \pi_ {P o s}}{L G D ^ {*} \pi_ {N e g}}.\tag{5}
$$

## 3.5.2. Performance metrics for modelling EAD and EL

To evaluate the results of modelling EAD and EL, three diferent measures were used, including mean absolute error (MAE), RMSE and the square of the correlation coeficient square (R<sup>2</sup>). This selection matches previous studies of LGD and EAD [9,12]. The metrics are defined as follows:

$$
M A E = \frac {1}{n} \sum_ {i = 1} ^ {n} | y _ {i} - \widetilde {y} _ {i} |\tag{6}
$$

$$
R M S E = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} (y _ {i} - \widetilde {y} _ {i}) ^ {2}}\tag{7}
$$

and

$$
R ^ {2} = 1 - \frac {\sum_ {i = 1} ^ {n} (y _ {i} - \widetilde {y} _ {i}) ^ {2}}{\sum_ {i = 1} ^ {n} (y _ {i} - \overline {{y}}) ^ {2}}\tag{8}
$$

where $y _ { i }$ is the predicted EAD (EL) for the i-th loan, $\widetilde { y _ { i } }$ is the target EAD (EL) for the i-th loan and v is the mean EAD (EL).

## 4. Datasets

Our study utilizes two consumer credit risk datasets. The first was obtained from Lending Club, the largest U.S. P2P lender, for the period from January 2016 to September 2018. These data are publicly available from http://www.lendingclub.com. Note that we discarded out standing loans from this dataset. Of 365,207 loans in total that were thus retained, 283,112 were fully paid (non-defaulted) and 82,095 were charged of (defaulted). In other words, the P2P dataset was imbalanced 3.4 to 1 in favour of non-defaulted loans. This dataset includes 78 input variables, categorized into the following subsets [2]: (1) applicant assessment (grade, subgrade, etc.); (2) loan characteristics (loan purpose and amount); (3) applicant characteristics (annual income, housing situation, etc.); (4) credit history (credit history length, delinquency, etc.); and (5) applicant indebtedness (loan amount to annual income, annual instalment to income, etc.).

The second dataset encompasses 22,364 consumer loans. For each loan, socio-economic attributes of the applicant were available, including the region of permanent residence, age, sex, marital status, housing type, education level, consumer type (employee, pensioner or on maternity leave) and length of employment. In addition, the appli cants' financial situations were characterized by the following attri butes: the amount and maturity of the loan, monthly instalment, monthly expenses, free financial resources, free financial resources divided by monthly instalment, net monthly income and presence of a codebtor. The remaining attributes comprised applicant profile (new applicant, returning applicant, ofset loan or concurrent loan) and data available from credit bureaus. Table 3 describes the attributes used. For further experiments, all numeric attributes were normalized to a [0,1] range, the same as for the P2P dataset. There were no missing data in the Czech dataset, while 0.36% of data were missing in the P2P dataset.

Table 3  
Description of attributes for the Czech dataset.

<table><tr><td>Attribute</td><td>Scale</td><td>Description</td></tr><tr><td>CBS</td><td>{10, 11, ..., 26}</td><td>Credit Bureau Score from the NRCI</td></tr><tr><td>Loan amount</td><td>[11,018,484,884]</td><td>Loan amount paid increased by future interest in CZK</td></tr><tr><td>Loan maturity</td><td>[12, 48]</td><td>Loan maturity, in months</td></tr><tr><td>Length of employment</td><td>[0, 47]</td><td>Length of employment, in years</td></tr><tr><td> $K_1$  coefficient</td><td>[-3.1, 75.5]</td><td> $K_1$ =free financial resources over monthly instalment</td></tr><tr><td>Region</td><td>{1, 2, ..., 15}</td><td>Region of permanent residence</td></tr><tr><td>Monthly instalment</td><td>[456, 14,562]</td><td>Monthly instalment, in CZK</td></tr><tr><td>No. of Solus statuses</td><td>[0, 4]</td><td>Number of statuses in Solus credit register</td></tr><tr><td>Sex</td><td>{1, 2}</td><td>Sex of applicant</td></tr><tr><td>Net monthly income</td><td>[0, 165,252]</td><td>Net monthly income, in CZK</td></tr><tr><td>Applicant profile</td><td>{1, 2, 3, 4}</td><td>Applicant profile</td></tr><tr><td>Marital status</td><td>{1, 2, ..., 10}</td><td>Marital status</td></tr><tr><td>Solus status</td><td>{0, 1}</td><td>Status A, B, ..., Z in Solus credit register</td></tr><tr><td>Co-debtor</td><td>{0, 1}</td><td>Presence of a co-debtor</td></tr><tr><td>Customer type</td><td>{1, 2, 3}</td><td>Customer type</td></tr><tr><td>Housing type</td><td>{1, 2, ..., 8}</td><td>Housing type</td></tr><tr><td>Age</td><td>[18, 86]</td><td>Age of applicant</td></tr><tr><td>Free fin. Resources</td><td>[-7794,155,179]</td><td>Free financial resources, in CZK</td></tr><tr><td>Monthly expenses</td><td>[6300, 41,473]</td><td>Monthly expenses, in CZK</td></tr><tr><td>Loan amount paid</td><td>[7000, 166,000]</td><td>Loan amount paid, in CZK</td></tr><tr><td>Education</td><td>{1, 2, ..., 10}</td><td>Education level</td></tr><tr><td>Default</td><td>{0,1}</td><td>Consumer is at least 60 days past the due date</td></tr><tr><td>EAD</td><td>[0,1]</td><td>Exposure at default</td></tr></table>

These data on consumer loans were provided by a Czech non-bank financial institution that wishes to remain anonymous and keep these data publicly unavailable. The data sample includes all loan applicants between 1 January 2010 and 31 August 2015. In addition to these data, data on the credit histories of the loan applicants were available from two credit bureaus, namely the NRCI (Non-banking Register of Client Information) and Solus credit register. Specifically, the Credit Bureau Score (CBS) was drawn from the NRCI and Solus statuses were obtained from the Solus register.

For both datasets, the EL is calculated using the three credit risk parameters, $\mathrm { P D } \times \mathrm { E A D } \times \mathrm { L G D }$ . PD was estimated by categorizing customers into defaulted and non-defaulted classes. For the second dataset (hereinafter referred to as “Czech dataset”), consumers were categorized in default after being past due for > 60 days. The share of defaulted loans was 38.49%, thus imbalanced 2.6 to 1 in favour of nondefaulted loans.

Since this study concerns fixed exposure, the EAD corresponds to the drawn amount (current outstanding loan amount), represented by the ratio of the total loan amount actually used by the consumer. On average, the EAD was 79.00% and 87.61% for the P2P and Czech datasets, respectively. Unfortunately, the LGD for individual consumer loans was not available from the Czech lending institution. Therefore, to estimate $\mathrm { E L , }$ we calculated the LGD from the 12 months post-default recovery rate provided by the lending institution, which gave an LGD amounting 74.88%. For the P2P dataset, the average LGD was 93.47%. These values can be used to estimate the EL of all the loans in these datasets. In other words, the LGD parameter was fixed and was thus not predicted by the proposed model. However, the estimated LGD values were at least used to calculate the MC measures.

![](/api/attachments/3E6YQXVG/fulltext/images/c5e3dcf7b2896bd022ed5c08e00f8cce5fd7f34ed0644fb3f04b792cad82d6a6.jpg)

![](/api/attachments/3E6YQXVG/fulltext/images/a8532ac77c6e87d0b83469633ef654ceb3c5c1ad9afc1fc785b78f28d7126d30.jpg)  
Fig. 2. Distribution of EL in the P2P and Czech dataset.

The empirical distribution of EL values is depicted in Fig. 2. Ob viously, the observed EL was not normally distributed, with two peaks corresponding to EL = 0 (non-defaulted loans) and $\mathrm { E L } = 1 \ ( \mathrm { E A D } = 1 )$ .

## 5. Experimental results

Hereinafter, we report average values and standard deviations from 50 experiments performed on diferent data partitions (five-fold crossvalidation completed 10 times). For the classification task of modelling PD, we show Acc, AUC and MC, while RMSE, MAE and $R ^ { 2 }$ are reported for the results of the regression task of modelling EAD and EL. The values of MC were calculated as follows:

$$
M C _ {P 2 P} = F P R ^ {*} 0. 9 3 5 + F N R ^ {*} (0. 3 2 0 + (- 0. 3 2 0 ^ {*} 0. 7 7 5 + 0. 9 3 5 ^ {*} 0. 2 2 5)),\tag{9}
$$

$$
M C _ {C z e c h} = F P R ^ {*} 0. 7 4 9 + F N R ^ {*} (0. 8 0 2 + (- 0. 8 0 2 ^ {*} 0. 6 1 5 + 0. 7 4 9 ^ {*} 0. 3 8 5)),\tag{10}
$$

where $\mathrm { L G D } _ { \mathrm { P 2 P } } = 0 . 9 3 5$ and $\mathrm { L G D } _ { \mathrm { C z e c h } } = 0 . 7 4 9$ were calculated from the 12-month post-default recovery rate, $r _ { \mathrm { P 2 P } } = 0 . 3 2 0$ and $r _ { \mathrm { C z e c h } } = 0 . 8 0 2$ are the average return (interest) rates for average maturities $M _ { \mathrm { P 2 P } } = 3 . 4 7$ and $M _ { \mathrm { C z e c h } } = 2 . 6 2$ for each respective dataset, and $\pi _ { \mathrm { P o s } } = 0 . 7 7 5 \ \left( \pi _ { \mathrm { P o s } } = 0 . 6 1 5 \right)$ and $\pi _ { \mathrm { N e g } } = 0 . 2 2 5 \ \left( \pi _ { \mathrm { N e g } } = 0 . 3 8 5 \right)$ are the percentages of positive and negative loans for the P2P (Czech) dataset, respectively. Cut-of points $T _ { \mathrm { P 2 P } } = 0 . 4 9$ and $T _ { \mathrm { C z e c h } } = 0 . 4 4$ were calculated using Eq. (5).

In the first set of experiments, we used the original dataset with all attributes (without feature selection) to demonstrate the effect of data imbalance. Specifically, here we tested the efect of undersampling (EUSBoost method) and oversampling (SMOTE method [64]) on the results of PD classification. In the EUSBoost method [40], the undersampling process performed inside the loop of the Adaboost.M2 algorithm (with 10 classifiers, two instances per leaf and minimum confidence of 0.25). No resampling was allowed in the undersampling process, and the percentage of the majority class to retain was set in order to balance the number of instances in the minority class. SMO-TEBagging oversampling was employed as a benchmark [41], which combines minority-class oversampling with bagging so that synthetic instances are generated during subset construction. The same setting as used for the AdaBoost.M2 algorithm in the EUSBoost method were also used in the bagging algorithm of the SMOTEBagging method, in which the minority class was oversampled in order to balance the majority class in training data.

For comparative purposes, we also report the results obtained using the original, imbalanced dataset. For the sake of comparability, we used RF as the benchmark classifier [7]. The best results are in bold in Table 4.

The RF trained on the data balanced by the EUSBoost method outperformed those RF classifiers based on the SMOTE method or the original data in terms of most classification metrics. Notably, the RF trained on the original data performed well only on the majority class, while the SMOTEBagging method was also efective for the minority class, as indicated by AUC and MC values. Wilcoxon signed-rank test was performed to statistically compare the results. The best classifier outperformed the other two methods for all evaluation metrics. Taken together, these results suggest that undersampling the majority class efectively addresses the issue of class imbalance in the dataset.

In the next step, we performed MOEFS on the balanced training data using the ENORA algorithm with the following settings: number of generations = 10 and size of population = 100. The average number of selected attributes ( ± st.dev.) was $1 5 . 6 ~ \pm ~ 5 . 3$ and $3 0 . 0 ~ \pm ~ 8 . 1$ of 78 and 39 original attributes for the P2P and Czech dataset, respectively. Again, the RF method was used as the classifier in the feature selection scheme for modelling PD. In a similar manner, RF was used as the

Table 4  
The efect of class imbalance on RF performance.

<table><tr><td>Dataset</td><td>Method</td><td>Acc</td><td>AUC</td><td>MC</td></tr><tr><td rowspan="3">P2P</td><td>RF</td><td>80.27 ± 0.14</td><td>76.10 ± 0.79</td><td>0.276 ± 0.002</td></tr><tr><td>EUSBoost + RF</td><td>86.37 ± 0.16</td><td>94.46 ± 0.10</td><td>0.167 ± 0.003</td></tr><tr><td>SMOTEBagging + RF</td><td>83.01 ± 0.27</td><td>87.96 ± 0.26</td><td>0.169 ± 0.012*</td></tr><tr><td rowspan="3">Czech</td><td>RF</td><td>66.13 ± 0.68</td><td>68.81 ± 0.62</td><td>0.491 ± 0.010</td></tr><tr><td>EUSBoost + RF</td><td>78.29 ± 0.97</td><td>88.16 ± 0.97</td><td>0.292 ± 0.012</td></tr><tr><td>SMOTEBagging + RF</td><td>71.04 ± 0.30</td><td>78.44 ± 0.20</td><td>0.387 ± 0.004</td></tr></table>

<sup>⁎</sup> Significantly similar at $P < 0 . 0 5$ as the performer (in bold).

Table 6  
Table 5  
The efect of MOEFS on RF performance.

<table><tr><td>Dataset</td><td>Method</td><td>Acc</td><td>AUC</td><td>MC</td></tr><tr><td rowspan="2">P2P</td><td>EUSBoost + RF</td><td>86.37 ± 0.16</td><td>94.46 ± 0.10*</td><td>0.167 ± 0.003</td></tr><tr><td>MOEFS + EUSBoost + RF</td><td>87.97 ± 0.18</td><td>95.30 ± 0.15</td><td>0.143 ± 0.003</td></tr><tr><td rowspan="2">Czech</td><td>EUSBoost + RF</td><td>78.29 ± 0.97*</td><td>88.16 ± 0.97*</td><td>0.292 ± 0.012</td></tr><tr><td>MOEFS + EUSBoost + RF</td><td>78.55 ± 0.70</td><td>88.36 ± 0.87</td><td>0.274 ± 0.009</td></tr></table>

<sup>⁎</sup> Significantly similar at $P < 0 . 0 5$ as the performer (in bold).

Classification performance of PD models.

<table><tr><td colspan="4">Czech dataset</td><td colspan="3">P2P dataset</td></tr><tr><td>Method</td><td>Acc</td><td>AUC</td><td>MC</td><td>Acc</td><td>AUC</td><td>MC</td></tr><tr><td>Forest PA</td><td>74.94 ± 0.91</td><td>82.84 ± 1.11</td><td>0.330 ± 0.012</td><td>84.82 ± 0.24</td><td>92.17 ± 0.35</td><td>0.190 ± 0.003</td></tr><tr><td>CDT</td><td>65.43 ± 0.65</td><td>69.09 ± 1.30</td><td>0.464 ± 0.008</td><td>75.38 ± 0.35</td><td>80.92 ± 0.34</td><td>0.311 ± 0.007</td></tr><tr><td>Heoffding DT</td><td>60.20 ± 2.64</td><td>63.54 ± 2.51</td><td>0.510 ± 0.024</td><td>67.49 ± 0.54</td><td>72.51 ± 0.65</td><td>0.381 ± 0.035</td></tr><tr><td>C4.5</td><td>70.90 ± 0.83</td><td>72.86 ± 0.98</td><td>0.392 ± 0.011</td><td>81.58 ± 0.41</td><td>83.53 ± 0.37</td><td>0.243 ± 0.005</td></tr><tr><td>LogR</td><td>63.73 ± 0.80</td><td>69.87 ± 1.20</td><td>0.472 ± 0.011</td><td>69.77 ± 0.28</td><td>76.80 ± 0.25</td><td>0.354 ± 0.004</td></tr><tr><td>Bayes Network</td><td>63.45 ± 0.98</td><td>68.46 ± 1.34</td><td>0.487 ± 0.013</td><td>68.58 ± 0.19</td><td>75.73 ± 0.09</td><td>0.413 ± 0.004</td></tr><tr><td>SVM</td><td>64.31 ± 1.29</td><td>63.80 ± 1.84</td><td>0.480 ± 0.017</td><td>68.89 ± 0.46</td><td>68.90 ± 0.46</td><td>0.329 ± 0.032</td></tr><tr><td>DNN</td><td>59.62 ± 0.55</td><td>71.17 ± 0.78</td><td>0.485 ± 0.020</td><td>64.19 ± 0.48</td><td>69.75 ± 0.58</td><td>0.469 ± 0.014</td></tr><tr><td>MultiBoostAB</td><td>61.73 ± 1.62</td><td>65.97 ± 0.77</td><td>0.505 ± 0.015</td><td>62.87 ± 2.82</td><td>69.12 ± 1.52</td><td>0.452 ± 0.299</td></tr><tr><td>AdaBoostM1</td><td>62.28 ± 0.47</td><td>68.15 ± 0.92</td><td>0.478 ± 0.012</td><td>66.90 ± 0.72</td><td>73.05 ± 0.60</td><td>0.410 ± 0.037</td></tr><tr><td>LogitBoost</td><td>63.34 ± 0.91</td><td>68.60 ± 1.02</td><td>0.480 ± 0.014</td><td>68.22 ± 0.23</td><td>75.48 ± 0.34</td><td>0.372 ± 0.013</td></tr><tr><td>Rotation Forest</td><td>77.55 ± 0.64</td><td>87.24 ± 0.62</td><td>0.291 ± 0.010</td><td>86.60 ± 0.08</td><td>94.25 ± 0.17</td><td>0.167 ± 0.002</td></tr><tr><td>RF</td><td>78.55 ± 0.70</td><td>88.36 ± 0.87</td><td>0.274 ± 0.009</td><td>87.97 ± 0.18*</td><td>95.30 ± 0.15*</td><td>0.143 ± 0.003</td></tr><tr><td>Decorate</td><td>76.04 ± 0.54</td><td>85.13 ± 0.73</td><td>0.314 ± 0.008</td><td>85.92 ± 0.41</td><td>92.90 ± 0.54</td><td>0.176 ± 0.006</td></tr><tr><td>Bagging</td><td>71.26 ± 0.77</td><td>78.64 ± 1.21</td><td>0.374 ± 0.010</td><td>82.39 ± 0.16</td><td>90.04 ± 0.19</td><td>0.217 ± 0.003</td></tr><tr><td>Random Subspace</td><td>72.60 ± 0.68</td><td>81.16 ± 0.94</td><td>0.350 ± 0.011</td><td>83.15 ± 0.86</td><td>91.05 ± 0.53</td><td>0.212 ± 0.013</td></tr><tr><td>Voting - avg</td><td>73.59 ± 1.32</td><td>81.59 ± 1.12</td><td>0.354 ± 0.018</td><td>82.25 ± 0.27</td><td>89.83 ± 0.28</td><td>0.212 ± 0.013</td></tr><tr><td>Voting - maj</td><td>72.18 ± 1.09</td><td>73.71 ± 1.00</td><td>0.364 ± 0.015</td><td>78.20 ± 0.65</td><td>78.20 ± 0.65</td><td>0.258 ± 0.007</td></tr><tr><td>Stacking with LogR</td><td>77.82 ± 0.57</td><td>88.57 ± 0.78</td><td>0.295 ± 0.007</td><td>88.00 ± 0.08*</td><td>95.55 ± 0.09*</td><td>0.131 ± 0.003</td></tr><tr><td>Stacking with RF</td><td>80.45 ± 0.84</td><td>90.55 ± 0.51</td><td>0.262 ± 0.012</td><td>88.58 ± 0.25</td><td>95.72 ± 0.06</td><td>0.108 ± 0.005</td></tr></table>

<sup>⁎</sup> Significantly similar at $P < 0 . 0 5$ as the performer (in bold).

regressor in MOEFS for modelling EAD. In that case, $2 2 . 6 ~ \pm ~ 8 . 3$ and $2 7 . 4 ~ \pm ~ 1 3 . 4$ attributes were selected. Table 5 shows that MOEFS improved RF performance in both datasets, particularly in terms of MC.

In the second set of experiments, we compared the performance of the classification methods used to model PD. Table 6 presents the results for three types of classifiers: (1) single classifiers (Forest PA [57], CDT [13], Hoefding DT [52], C4.5 [60], LogR [60], Bayes Network [60], SVM [7] and DNN [26]); (2) homogeneous ensemble methods (MultiBoostAB [53], AdaBoostM1 [54], LogitBoost [55], Rotation Forest [58], RF [7], Decorate [13], bagging [56] and Random Subspace [56]); and (3) heterogeneous ensemble methods (Voting [23] and Stacking [25]). Note that the heterogeneous ensemble methods combine predictions of all the single classifiers and homogeneous ensemble methods. Again, the best performers are in bold.

The results indicate that Stacking with RF as the meta-learning algorithm outperformed the other classifiers on all evaluation measures. Only Stacking with LogR, Rotation Forest and RF performed similar to Stacking with RF in terms of accuracy and AUC. Notably, the Stacking with RF outperformed all other classifiers for the MC evaluation measure. Therefore, this method was chosen as the most suitable for modelling PD in the two-stage model.

and Rotation Forest. Interestingly, of all the homogeneous ensemble methods, only Rotation Forest performed similar to Stacking with LR. Moreover, LR model performed similarly as Rotation Forest. The poor performance of several methods, such as RF, can be explained by the poor performance of Random Trees that were also used as their base learners. This can also be attributed the fact that we performed no hyper-parameter tuning to avoid overfitting in the meta-learning stage. Overall, since Stacking with LR performed the best on all evaluation measures, we preferred this method for modelling EAD in the two-stage EL model for the Czech dataset. For the P2P dataset, the benefit of using heterogeneous Stacking ensemble methods is even more evident. Stacking with RF was chosen for the second stage as the best performer.

Finally, we combined the two stages of EL modelling in an in tegrated framework, including Stacking with RF to model PD and Stacking with LR to model EAD. More precisely, the latter algorithm was applied to those loans classified as defaulted in the first stage. Note that these defaulted loans included loans classified as both defaulted correctly (TN) and incorrectly (FP). By contrast, EL = 0 was assigned to those loans classified as non-defaulted in the first stage (including TP and FN). In other words, the EL of TN and FP loans corresponded to the EAD prediction obtained by Stacking with LR in the second stage.

In the next stage, the EAD of the sub-population of defaulted loans was predicted using the regression models. As for modelling PD, the regression models included single regressors (REP Tree [60], AMT [60], M5P [59], Random Tree [60], LR [60], SVR [9] and DNN [38]), as well as homogeneous (RF [7], Rotation Forest [13], Additive Regression [60], bagging [56] and Random Subspace [56]) and heterogeneous Stacking ensemble methods [25]. For the Czech dataset, Stacking with LR outperformed Stacking with RF in terms of $R ^ { 2 }$ and RMSE (Table 7). In addition, the Stacking with LR model outperformed most other models on all the evaluation measures, except for AMT. M5P. LR. SVR

Table 8 compares the proposed two-stage model with other state-ofthe-art credit risk models. We thereby demonstrate that the proposed model presents a more efficient tool for modelling EL. The compared methods include those used previously for modelling LGD/EAD in two categories, single-stage and two-stage models.

The single-stage models predict EL directly, without categorizing the consumer loans into PD classes. As a comparison for single-stage models, we used the Stacking with LR model that performed best on EAD prediction in this study. The other stacking approach used for comparison is FDF [12], which combines the predictions of an M5P regression tree, LR, SVR, least-squared SVR and semi-parametric leastsquared SVR. An evolutionary fuzzy rule-based system is then used as the meta-learning method. Here, we used the settings of the base learners presented in Appendix A. A genetic programming approach fuzzy rule-based system [65] was used as the meta-regressor, trained with the following learning parameters as recommended by the authors of the algorithm: number of membership functions = 3, number of rules = 8, population size = 30, number of subpopulations = 2, mutation probability = 0.01, migration probability = 0.001, and number of iterations = 10,000. The remaining single-stage models included regression trees [36], NNs [38], LR [35,39] and SVR [37]. Note that the indirect estimation methods applied to EAD by prior studies [8,10] are not applicable here because of the fixed exposures of the consumer loans.

Table 7 Prediction performance of EAD models.

<table><tr><td colspan="4">Czech dataset</td><td colspan="3">P2P dataset</td></tr><tr><td>Method</td><td> $R^2$ </td><td>RMSE</td><td>MAE</td><td> $R^2$ </td><td>RMSE</td><td>MAE</td></tr><tr><td>REP Tree</td><td>0.074 ± 0.020</td><td>0.070 ± 0.002</td><td>0.056 ± 0.001</td><td>0.493 ± 0.012</td><td>0.125 ± 0.002</td><td>0.085 ± 0.002</td></tr><tr><td>AMT</td><td>0.114 ± 0.010</td><td>0.068 ± 0.001*</td><td>0.055 ± 0.001*</td><td>0.348 ± 0.011</td><td>0.140 ± 0.001</td><td>0.110 ± 0.001</td></tr><tr><td>M5P</td><td>0.122 ± 0.015*</td><td>0.068 ± 0.001*</td><td>0.054 ± 0.001</td><td>0.356 ± 0.027</td><td>0.139 ± 0.004</td><td>0.109 ± 0.004</td></tr><tr><td>Rand. Tree</td><td>0.012 ± 0.004</td><td>0.096 ± 0.001</td><td>0.073 ± 0.001</td><td>0.664 ± 0.014</td><td>0.105 ± 0.004</td><td>0.043 ± 0.002</td></tr><tr><td>LR</td><td>0.115 ± 0.019</td><td>0.068 ± 0.002*</td><td>0.055 ± 0.001*</td><td>0.306 ± 0.006</td><td>0.144 ± 0.001</td><td>0.114 ± 0.001</td></tr><tr><td>SVR</td><td>0.122 ± 0.017*</td><td>0.068 ± 0.001*</td><td>0.055 ± 0.001*</td><td>0.276 ± 0.015</td><td>0.151 ± 0.003</td><td>0.119 ± 0.002</td></tr><tr><td>DNN</td><td>0.022 ± 0.015</td><td>0.072 ± 0.001</td><td>0.058 ± 0.001</td><td>0.235 ± 0.011</td><td>0.155 ± 0.000</td><td>0.124 ± 0.001</td></tr><tr><td>RF</td><td>0.088 ± 0.015</td><td>0.069 ± 0.001</td><td>0.056 ± 0.001</td><td>0.787 ± 0.004</td><td>0.082 ± 0.001</td><td>0.048 ± 0.001</td></tr><tr><td>Rot. For.</td><td>0.115 ± 0.015</td><td>0.068 ± 0.001*</td><td>0.055 ± 0.001*</td><td>0.706 ± 0.007</td><td>0.097 ± 0.001</td><td>0.070 ± 0.001</td></tr><tr><td>Addit. Regr.</td><td>0.074 ± 0.016</td><td>0.072 ± 0.002</td><td>0.057 ± 0.001</td><td>0.552 ± 0.013</td><td>0.119 ± 0.003</td><td>0.077 ± 0.003</td></tr><tr><td>Bagging</td><td>0.084 ± 0.014</td><td>0.070 ± 0.001</td><td>0.056 ± 0.001</td><td>0.604 ± 0.010</td><td>0.109 ± 0.002</td><td>0.077 ± 0.001</td></tr><tr><td>Rand. Subsp.</td><td>0.101 ± 0.024</td><td>0.069 ± 0.001</td><td>0.056 ± 0.001</td><td>0.684 ± 0.010</td><td>0.104 ± 0.002</td><td>0.078 ± 0.002</td></tr><tr><td>Stacking LR</td><td>0.125 ± 0.012</td><td>0.067 ± 0.001</td><td>0.054 ± 0.001</td><td>0.792 ± 0.004*</td><td>0.079 ± 0.016*</td><td>0.045 ± 0.001</td></tr><tr><td>Stacking RF</td><td>0.098 ± 0.013</td><td>0.069 ± 0.001</td><td>0.056 ± 0.001*</td><td>0.806 ± 0.005</td><td>0.076 ± 0.004</td><td>0.038 ± 0.001</td></tr></table>

<sup>⁎</sup> Significantly similar at $P < 0 . 0 5$ as the performer (in bold), AMT is Alternating Model Tree.

residuals estimated in the second stage using a non-linear regression model (SVR or NN). Comparing the results of the two model categories, there is no clear evidence for the superiority of either the single-stage or the two-stage models. Their average $R ^ { 2 }$ varied from about 7% for LogR +NN to 34% for the proposed two-stage model for the Czech dataset, while up to 66% for the P2P dataset. The proposed two-stage EL model thus outperformed all the other prediction models on all evaluation measures.

For the comparative two-stage models, we adopted the same methodology as used for the model proposed in this study: predicting the PD class in the first stage and then predicting the EAD for those loans classified as defaulted. Four models were tested, namely LogR +SVR [11], LogR+NN [11], SVM + SVR [9] and RF + NN. The RF + NN model combines two benchmark algorithms used efectively for modelling PD and LGD/EAD in previous studies. This model is ap plied on the dataset that was balanced using the undersampling method, just as in the proposed two-stage model. Note that the re maining compared models operate on the original, imbalanced dataset, as their corresponding studies have suggested. Again, the settings of the learning parameters for all of these models are presented in the $\mathsf { A p - }$ pendix. As an alternative to these models, the two-stage models proposed in [11] combine LR in the first stage with the prediction of the LR

To demonstrate the efectiveness of the proposed model in realworld scenarios, we calculated the actual profit achieved by a lender choosing top 10%, $2 0 \% , . . . ,$ 100% best loans according to: a) PD scores obtained by RF and b) EL scores obtained by the proposed two-stage approach. Fig. 3 depicts the achieved profit in absolute and relative terms, indicating that the proposed approach results in better economic performance. As expected, the average relative profit decreases with higher share of approved loans (and thus higher credit risk). The highest absolute profit was obtained by choosing top 70% and 50% loans for the Czech and P2P dataset, respectively. This can be attributed to the diferences in profit (interest) rates. Interestingly, the loan portfolio from the Czech dataset would be profitable regardless of its credit risk, whereas too high percentage (above 80%) of approved loans would lead to a loss for the P2P dataset. This can also be explained by a relatively high EAD in the P2P dataset. In other words, many defaulted loans are still profitable due to the high interest rate compensating high credit risk in the Czech dataset. Therefore, the cut-of point of approved loans should be more restrictive for the P2P consumer loans.

Prediction performance of the proposed two-stage EL model compared with state-of-the-art credit risk models

<table><tr><td colspan="2"></td><td colspan="3">Czech</td><td colspan="3">P2P</td></tr><tr><td>Categ.</td><td>Model</td><td> $R^2$ </td><td>RMSE</td><td>MAE</td><td> $R^2$ </td><td>RMSE</td><td>MAE</td></tr><tr><td rowspan="6">Single-stage</td><td>M5P</td><td>0.125 ± 0.006</td><td>0.265 ± 0.001</td><td>0.240 ± 0.001</td><td>0.141 ± 0.162</td><td>0.523 ± 0.386</td><td>0.309 ± 0.005</td></tr><tr><td>LR</td><td>0.125 ± 0.006</td><td>0.265 ± 0.001</td><td>0.239 ± 0.001</td><td>0.191 ± 0.005</td><td>0.352 ± 0.001</td><td>0.313 ± 0.001</td></tr><tr><td>SVR</td><td>0.126 ± 0.006</td><td>0.265 ± 0.001</td><td>0.239 ± 0.001</td><td>0.067 ± 0.008</td><td>0.424 ± 0.001</td><td>0.370 ± 0.001</td></tr><tr><td>NN</td><td>0.108 ± 0.005</td><td>0.269 ± 0.001</td><td>0.246 ± 0.003</td><td>0.155 ± 0.009</td><td>0.363 ± 0.001</td><td>0.337 ± 0.001</td></tr><tr><td>FDF</td><td>0.126 ± 0.010</td><td>0.265 ± 0.002</td><td>0.242 ± 0.003</td><td>0.612 ± 0.006</td><td>0.244 ± 0.003</td><td>0.166 ± 0.002</td></tr><tr><td>Stacking</td><td>0.131 ± 0.010</td><td>0.264 ± 0.002</td><td>0.237 ± 0.001</td><td>0.632 ± 0.028</td><td>0.238 ± 0.016</td><td>0.155 ± 0.003</td></tr><tr><td rowspan="7">Two-stage</td><td>LR + SVR</td><td>0.126 ± 0.006</td><td>0.265 ± 0.001</td><td>0.241 ± 0.001</td><td>0.191 ± 0.005</td><td>0.352 ± 0.001</td><td>0.313 ± 0.001</td></tr><tr><td>LR + NN</td><td>0.089 ± 0.009</td><td>0.271 ± 0.002</td><td>0.251 ± 0.004</td><td>0.159 ± 0.007</td><td>0.362 ± 0.002</td><td>0.336 ± 0.001</td></tr><tr><td>LogR + SVR</td><td>0.126 ± 0.006</td><td>0.265 ± 0.001</td><td>0.240 ± 0.001</td><td>0.215 ± 0.006</td><td>0.347 ± 0.001</td><td>0.303 ± 0.001</td></tr><tr><td>LogR + NN</td><td>0.070 ± 0.009</td><td>0.276 ± 0.001</td><td>0.261 ± 0.003</td><td>0.206 ± 0.004</td><td>0.354 ± 0.001</td><td>0.324 ± 0.001</td></tr><tr><td>SVM + SVR</td><td>0.126 ± 0.006</td><td>0.265 ± 0.001</td><td>0.240 ± 0.001</td><td>0.215 ± 0.005</td><td>0.347 ± 0.001</td><td>0.302 ± 0.001</td></tr><tr><td>RF + NN</td><td>0.312 ± 0.012</td><td>0.263 ± 0.001</td><td>0.175 ± 0.001</td><td>0.564 ± 0.005</td><td>0.269 ± 0.002</td><td>0.220 ± 0.002</td></tr><tr><td>Proposed model</td><td>0.337 ± 0.012</td><td>0.238 ± 0.003</td><td>0.148 ± 0.003</td><td>0.666 ± 0.006</td><td>0.227 ± 0.004</td><td>0.131 ± 0.003</td></tr></table>

![](/api/attachments/3E6YQXVG/fulltext/images/7f56a36bf10869047b93ebe78d45eb94cfb3f379cdb2097544115d7e71d9198d.jpg)

![](/api/attachments/3E6YQXVG/fulltext/images/49f9b285e6e23970646877e8402f2aea086725a2d3d53e7293f008e5578fcf2c.jpg)

![](/api/attachments/3E6YQXVG/fulltext/images/e76d30ada6bd1bcde191b41304c171833b4c9e409804f8d736a061d8938255b9.jpg)

![](/api/attachments/3E6YQXVG/fulltext/images/8525d544489a51eab4eb88ed682150751441be68bb2528c5f164af1374e56b61.jpg)  
Fig. 3. Profit achieved using PD modelling and proposed two-stage (2S) approach, a) and b) profit in CZK and % for Czech dataset, c) and d) profit in USD and % for P2P dataset.

## 6. Discussion

Ensemble methods have recently gained increasing popularity for modelling PD. We hypothesized that such methods can also be efectively used to model other crucial credit risk parameters. Therefore, this study aimed to model credit risk using a two-stage approach, in which PD was modelled in the first stage and EAD was modelled in the second stage. In this study, we examined the performance of both homogeneous and heterogeneous ensemble methods for a credit risk modelling problem using a large, imbalanced dataset. We found that heterogeneous ensemble methods outperformed homogeneous methods for modelling PD, a finding consistent with previous comparative studies [7]. The superior performance of heterogeneous ensemble methods can be attributed to the relatively low dimensionality achieved using MOEFS (15–30 attributes on average for both datasets), which prevents overfitting. Another explanation for their performance could be that the relatively large datasets used in this study favours methods that mini mize empirical risk. It also seems possible that these results are due to the data distribution, which has frequent outliers at the tail of EL. In addition, we demonstrated that the performance of the ensemble methods for modelling PD can be improved by using RF as a metalearning method, which is a non-linear classifier, rather than traditional linear LogR. This finding, which is consistent with the recent use of nonlinear meta-learning methods in modelling PD [26], has important implications for developing PD models.

Regarding the results of individual classes, the most interesting finding was that Stacking with RF outperformed the remaining methods in terms of TNR. For PD prediction models, this evaluation metric plays a crucial role due to the higher MC associated with loan default. Therefore, achieving a high TNR is an important task in modelling PD. Here, we showed that models based on RF generally perform well in terms of TNR, suggesting that the correct prediction of defaulted loans requires ensemble methods with controlled variance. This finding supports the use of RF as a benchmark method in modelling PD [7].

This study's results also corroborate the findings in [16,33], which showed that undersampling data in modelling PD improves the accu racy of benchmark classifiers. This finding contrasts with the preference for oversampling in [15]. This can be explained by the relatively large dataset used in this study, which makes it possible to eliminate redundant data in the majority class without compromising the size of training data. It should be noted that oversampling was also more effective than modelling PD on the original, imbalanced dataset. In general, therefore, resampling seems to enhance the performance of PD prediction; undersampling might be recommended for large credit scoring datasets.

As far as we know, no other authors have employed heterogeneous ensemble methods for modelling EAD. We found that these methods slightly outperform baseline methods. Moreover, the Stacking ensemble approach with RF as a meta-regressor performed poorly for modelling EAD, suggesting that a linear regression method sufices for combining predictions obtained by individual base learners. In summary, heterogeneous ensemble methods seem to deliver greater improvements in PD models than in EAD models.

The most striking result to emerge from feature selection is that the proposed two-stage model required a high proportion of attributes to classify the positive and negative classes in the first stage and to predict loans with EL > 0 in the second stage. When combining the two stages, 27.6 and 34.6 attributes on average were necessary to achieve the minimum error in modelling EL for the P2P and Czech dataset, respectively (i.e., about an 64.6% and 11.3% reduction in the number of attributes). It is worthwhile to note that this result was obtained even though one of the obiectives in MOEFS was to minimize the number of attributes. This finding suggests that there were only several irrelevant or redundant attributes in the original Czech dataset and that di. mensionality can be reduced only at the cost of substantial degradation of prediction performance. However, even this reduction may have considerable economic benefit for financial institutions due to de creased acquisition costs. It should also be noted that all the original set of attributes was used in an existing credit scoring system of the Czech non-bank financial institution. In contrast, the high reduction rate obtained for the P2P dataset can be attributed to the fact that the set of attributes used in the Model Rank, the internally developed credit scoring system of Lending Club, is not publicly available. Therefore, we used the complete original P2P dataset, regardless of the attributes' relevance and redundancy.

The present study also makes a noteworthy contribution to MC calculation. This performance measure has been reported to be crucial for PD models due to the higher MC associated with defaulted consumer loans. The proposed MC measure was specifically designed for fixed exposures, such as consumer loans or residential mortgages. For the Czech dataset, here we show that the MC associated with FP classification is 0.749, while it is 0.597 for FN classification. Thus, the MC ratio used in this study was about 1:1.25. That is, contrary to expectations, this study did not find a diference between the costs associated with FP and FN classifications for the consumer loans of a nonbank financial institution. For the P2P dataset, the MC ratio was about 1:3, which can be attributed to significantly lower return (interest) rates of P2P loans. Moreover, P2P loans are often repaid before maturity. For the P2P dataset, this was at 12 months on average. Note that these results difer from earlier MC ratio estimates of 1:5 for consumer loans [4]. The foremost cause of the discrepancy is due to the diferent financial institutions for which this evaluation measure was developed. The earlier reported PD models were developed for banks, whereas here we investigated non-bank financial institutions. Therefore, the lower

MC ratio can be attributed to the higher interest rate charged by the non-bank segment of the financial industry. In other words, this ratio largely depends on the type of financial institution. Generally, the MC metric proposed here could be useful for developing PD models in both bank and non-bank financial institutions.

When combining the best performing PD and EAD models in a twostage framework, the proposed model was particularly efective at predicting overall EL compared with state-of-the-art models. Its efectiveness can be attributed to both the two-stage approach to modelling EL and the balancing of training data in modelling PD. In fact, the EL models that combine PD and EAD predictions are shown to perform consistently better than traditional, single-stage models. The further increase in prediction performance can be undoubtedly attributed to the use of RF-based PD models on a balanced dataset. The relatively poor performance of the other two-stage models can be explained by the poor ability of traditional classification methods (LogR and SVM) to handle imbalanced datasets. Overall, the variance in EL (given by R<sup>2</sup>) that can be explained by the comparative models was consistently below 34% for the Czech dataset, implying that they could not explain most of the variance. For the P2P dataset, the proposed two-stage model explained > 60% of the variance in EL, indicating higher eficiency of the U.S. P2P credit market.

It was also demonstrated that predicting consumer credit risk using the proposed two-stage model may result in the selection of more profitable loan portfolios than those based on traditional PD modelling. This can be attributed to a more accurate estimate of EL, considering EAD. This finding corroborates the observations obtained for profit scoring [6]. However, note that our system was not designed to max imize profit regardless of credit risk. Instead, a more accurate EL esti mate can be used by lenders to manage the credit risk of their portfolios of consumer loans, including the support of the portfolio securitization decisions and pricing at an individual consumer level.

## 7. Conclusion

This study presented a two-stage consumer credit risk model based on heterogeneous ensemble learning. The results of this study support the idea that heterogeneous ensemble methods are efective in

## Appendix A. Settings of methods used for modelling PD and EAD

modelling consumer credit risk, estimated here by the PD and EAD parameters. In addition, this study has shown that imbalanced data must be addressed in modelling PD. We have confirmed that undersampling the majority class is an efective procedure to overcome this problem. To determine the performance of PD models, we proposed an MC metric that is suitable for predicting loans with fixed exposures. In the first stage of the proposed model, we showed that MC can be decreased by using a heterogeneous ensemble method with RF as a metaclassifier in modelling PD. This seems to be critical for the second stage, where EAD was predicted using a linear combination of base regressors. In summary, the relevance of the two-stage approach is clearly sup ported by the current findings.

The most important limitation lies in the fact that we fixed the value of LGD in the proposed model. More precisely, LGD was only considered in the calculation of MC. Therefore, further studies are needed which take LGD into account as a predicted parameter. Secondly, the proposed model also still has limited explanatory power (explaining < 34% of variance in the Czech dataset). Although this result corroborates the power observed in related predictions of EAD [38], we believe there is still room for improvement. We found only a few attributes that were not relevant for modelling EL, suggesting that future investigations might use a wider set of attributes for credit risk modelling. Thirdly, the model design prioritized prediction performance, resulting in the combination of two complex ensemble methods. Therefore, the proposed model's comprehensibility is limited. Future studies considering both performance and interpretability are therefore warranted. Further research might also explore the efectiveness of the proposed model in related credit risk modelling tasks, including (1) predicting the credit risk of loans with revolving exposures and (2) predicting the credit risk of loans with fixed exposures at bank financial institutions. For the former, we recommend replacing our MC metric with that developed by [34]. A higher MC ratio should be used for the latter.

## Acknowledgements

This work was supported by the scientific research project of the Czech Sciences Foundation Grant No: 16-19590S.

```txt
Method Parameters and their values
Forest PA No. of trees = 10
CDT Min. total weight of instances in a leaf = 2.0, maximum depth of trees unlimited and min. proportion of variance at a node = 0.001
Hoeffding Decision Tree Grace period = 200, minimum fraction of weight for info. Gain splitting = 0.01 and Hoeffding tie threshold = 0.05
C4.5 J48 version with the min. no. of instances per leaf = 2 and confidence factor for pruning = 0.25
REPTree Min. total weight of instances in a leaf = 2.0, maximum depth of trees unlimited and min. proportion of variance at a node = 0.001
Alternating Model Tree No. of iterations = 10 and shrinkage parameter = 1.0 and
M5P Tree Min. no. of instances at a leaf node = 4.0
Random Tree No. of randomly chosen attributes = log₂(#predictors) + 1 and min. proportion of variance at a node = 0.001
LogR Broyden–Fletcher–Goldfarb–Shanno learning algorithm
LR OLS
Bayes Network K2 (a hill climbing algorithm restricted by an order on the variables) with no. of parents = 2 and Bayes scoring function
SVM Sequential minimal optimization algorithm with complexity parameter C = 2³, polynomial kernel function with exponent = 2, RBF kernel function with gamma = 0.01
SVR Epsilon-SVR, epsilon for loss function = 0.1, C = 2³, polynomial kernel function with exponent = 2 and RBF kernel function with gamma = 0.01
NN Mini-batch gradient descent algorithm, size of mini-batches = 100, no. of hidden layers = 2, neurons in hidden layers = 2⁴ and 2³, learning rate = 0.1, dropout rate for input layer = 0.2, dropout rate for hidden layers = 0.5 and no. of iterations = 1000
Bagging Base learner = REP tree, no. of iterations = 10 and bag size as a percentage of the training set = {50,100}
Rotation Forest Base learner = C4.5 for classification and REP tree for regression, no. of iterations = 10, percentage of instances to be removed = 50 and projection filter = principal components
MultiBoostAB Base learner = Decision Stump, no. of iterations = 10 and no. of subcommittees = 3
AdaBoostM1 Base learner = Decision Stump and no. of iterations = 10
LogitBoost Base learner = Decision Stump, no. of iterations = 10 and shrinkage parameter = 1.0
Decorate Base learner = C4.5, no. of member classifiers = 15, no. of iterations = 50 and no. of artificial examples during training = 1.0
Random Subspace Base learner = C4.5 for classification and REP tree for regression, size of each subspace = 0.5 and no. of iterations = 10
Voting Combination rule = {average of probabilities, majority voting}
```

Additive Regression Base learner = M5P, no. of iterations = 10 and shrinkage parameter $= 1 . 0$ RF Maximum depth of trees unlimited, no. of trees to be generated = 100 and no. of attributes randomly sampled as candidates at each split = log₂(#predictors) + 1 Stacking Meta-learning algorithm = {LogR, RF} for classification and {LR, RF} for regression

## References

[1] F. Louzada, A. Ara, G.B. Fernandes, Classification methods applied to credit scoring: systematic review and overall comparison, Surv. Oper. Res. Manag. Sci. 21 (2016) 117–134.

[2] C. Serrano-Cinca, B. Gutierrez-Nieto, L. López-Palacios, Determinants of default in P2P lending, PloS one 10 (10) (2015) e0139427.

[3] Y. Xia, C. Liu, N. Liu, Cost-sensitive boosted tree for loan evaluation in peer-to-peer lending, Electron. Commer. Res. Appl. 24 (2017) 30–49.

[4] X. Feng, Z. Xiao, B. Zhong, Y. Dong, J. Qiu, Dynamic weighted ensemble classification for credit scoring using Markov Chain, Appl. Intell. (2018) 1–14.

[5] T. Verbraken, C. Bravo, R. Weber, B. Baesens, Development and application of consumer credit scoring models using profit-based classification measures, Eur. J. Oper. Res. 238 (2014) 505–513.

[6] C. Serrano-Cinca, B. Gutiérrez-Nieto, The use of profit scoring as an alternative to credit scoring systems in peer-to-peer (P2P) lending, Decis. Support. Syst. 89 (2016) 113–122.

[7] S. Lessmann, B. Baesens, H.V. Seow, L.C. Thomas, Benchmarking state-of-the-art classification algorithms for credit scoring: an update of research, Eur. J. Oper. Res. 247 (2015) 124–136.

[8] E.N.C. Tong, C. Mues, I. Brown, L.C. Thomas, Exposure at default models with and without the credit conversion factor, Eur. J. Oper. Res. 252 (2016) 910–920.

[9] X. Yao, J. Crook, G. Andreeva, Enhancing two-stage modelling methodology for loss given default with support vector machines, Eur. J. Oper. Res. 263 (2017) 679–689.

[10] M. Leow, J. Crook, A new mixture model for the estimation of credit card exposure at default, Eur. J. Oper. Res. 249 (2016) 487–497.

[11] G. Loterman, I. Brown, D. Martens, C. Mues, B. Baesens, Benchmarking regression algorithms for loss given default modeling. Int. J. Forecast. 28 (2012) 161–170.

[12] A. Nazemi, E. Fatemi Pour. K. Heidenreich. E.J. Fabozzi, Fuzzy decision fusior approach for loss-given-default modeling, Eur, J. Oper. Res, 262 (2017) 780–791

[13] J. Abellan, J.G. Castellano, A comparative study on base classifiers in ensemble methods for credit scoring, Expert Syst. Appl. 73 (2017) 1–10.

[14] K. Roszbach, Bank lending policy, credit scoring and value-at-risk, J. Bank. Financ. 86 (2003) 946–958.

[15] A.I. Marqués, V. García, J.S. Sánchez, On the suitability of resampling techniques for the class imbalance problem in credit scoring, J. Oper. Res. Soc. 64 (2013) 1060–1070.

[16] I. Brown, C. Mues, An experimental comparison of classification algorithms for imbalanced credit scoring data sets, Expert Syst. Appl. 39 (2012) 3446–3453.

[17] D. Besanko, A.V. Thakor, Collateral and rationing: sorting equilibria in monopolistic and competitive credit markets, Int. Econ. Rev, 28 (1987) 671–689.

[18] J. Maudos, L. Solís, The determinants of net interest income in the Mexican banking system: an integrated model, J. Bank, Financ. 33 (2009) 1920–1931.

[19] D. Zhang, X. Zhou, S.C.H. Leung, J. Zheng, Vertical bagging decision trees model for credit scoring, Expert Syst. Appl. 37 (2010) 7838–7843.

[20] N.C. Hsieh, L.P. Hung, A data driven ensemble classifier for credit scoring analysis, Expert Syst. Appl. 37 (2010) 534–545.

[21] L. Yu, W. Yue, S. Wang, K.K. Lai, Support vector machine based multiagent ensemble learning for credit risk evaluation, Expert Syst. Appl. 37 (2010) 1351–1360.

[22] C.-F. Tsai, C. Hung, Modeling credit scoring using neural network ensembles. Kybernetes 43 (2014) 1114–1123.

[23] M. Alarai, M.F. Abbod, Classifiers consensus system approach for credit scoring. Knowl.-Based Syst, 104 (2016) 89–105.

[24] M. Alaraj, M.F. Abbod, A new hybrid ensemble credit scoring model based on classifiers consensus system approach, Expert Syst. Appl. 64 (2016) 36–55.

[25] S. Dzeroski, B. Zenko, Is combining classifiers with stacking better than selecting the best one? Mach, Learn, 54 (2004) 255–273.

[26] L. Yu, Z. Yang, L. Tang, A novel multistage deep belief network based extreme learning machine ensemble learning paradigm for credit risk assessment. Flex. Sery Manuf. J. 28 (2016) 576–592

[27] R. Florez-Lopez, J.M. Ramon-Jeronimo, Enhancing accuracy and interpretability of ensemble strategies in credit risk assessment. A correlated-adiusted decision forest proposal, Expert Syst. Appl. 42 (2015) 5737–5753.

[28] L. Yu, S. Wang, K.K. Lai, Credit risk assessment with a multistage neural network ensemble learning approach, Expert Syst. Appl. 34 (2008) 1434–1444.

[29] L. Zhou, K.K. Lai, L. Yu, Least squares support vector machines ensemble models for credit scoring, Expert Syst, Appl, 37 (2010) 127–133.

[30] J.M. Tomczak, M. Zieba, Classification restricted Boltzmann machine for comprehensible credit scoring model, Expert Syst. Appl. 42 (2015) 1789–1796.

[31] C. Luo, D. Wu, D. Wu, A deep learning approach for credit scoring using credit default swaps, Eng. Appl. Artif. Intell. 65 (2017) 465–470.

[32] S.F. Crone, S. Finlay, Instance sampling in credit scoring: an empirical study of sample size and balancing, Int. J. Forecast. 28 (2012) 224–238.

[33] H. He, W. Zhang, S. Zhang, A novel ensemble method for credit scoring: adaption of different imbalance ratios. Expert Syst. Appl. 98 (2018) 105–117

[34] A.C. Bahnsen, D. Aouada. B. Ottersten. Example-dependent cost-sensitive decision trees, Expert Syst, Appl, 42 (2015) 6609–6619.

[35] S. Caselli, S. Gatti, F. Querci, The sensitivity of the loss given default rate to systematic risk: new empirical evidence on bank loans, J. Financ. Serv. Res. 34 (2008) 1-34.

[36] J.A. Bastos, Forecasting bank loans loss-given-default, J. Bank. Financ. 34 (2010) 2510–2517.

[37] X. Yao, J. Crook, G. Andreeva, Support vector regression for loss given default modelling, Eur. J. Oper. Res. 240 (2015) 528–538.

[38] B.H. Yang, M. Tkachenko, Modeling exposure at default and loss given default empirical approaches and technical implementation, J. Credit Risk 8 (2012) 22

[39] M. Gurtler, M.T. Hibbeln, P. Usselmann, Exposure at default modeling - a theoretical and empirical assessment of estimation approaches and parameter choice, J. Bank. Financ. (2018) 1–13

[40] M. Galar, A. Fernández, E. Barrenechea, F. Herrera, EUSBoost: enhancing ensembles for highly imbalanced data-sets by evolutionary undersampling. Pattern Recogn. 4e (2013) 3460–3471.

[41] S. Wang, X. Yao, Diversity analysis on imbalanced data sets by using ensemble models, 2009 IEEE Symp. Comput. Intell. Data Min, 2009, pp. 324–331.

[42] P. Hajek, K. Michalak, Feature selection in corporate credit rating prediction, Knowl.-Based Syst. 51 (2013) 72–84.

[43] P. Hajek, Predicting corporate investment/non-investment grade by using intervalvalued fuzzy rule-based systems - a cross-region analysis, Appl. Soft Comput. J. 62 (2018) 73–85.

[44] S. Maldonado, J. Pérez, C. Bravo, Cost-based feature selection for support vector machines: an application in credit scoring, Eur. J. Oper. Res. 261 (2017) 656–665

[45] S. Maldonado. C. Bravo. J. López, J. Pérez, Integrated framework for profit-based feature selection and SVM classification in credit scoring, Decis. Support. Syst. 104 (2017) 113–121

[46] S. Oreski, G. Oreski, Genetic algorithm-based heuristic for feature selection in credit risk assessment, Expert Syst. Appl. 41 (2014) 2052–2064, https://doi.org/10.1016 j.eswa.2013.09.004.

[47] F. Jiménez, G. Sánchez, J.M. García, G. Sciavicco, L. Miralles, Multi-objective evolutionary feature selection for online sales forecasting, Neurocomputing 234 (2017) 75–92.

[48] Y. Xia, C. Liu, Y.Y. Li, N. Liu, A boosted decision tree approach using Bayesian hyper-parameter optimization for credit scoring, Expert Syst. Appl. 78 (2017) 225-241.

[49] L. Todorovski, S. Dzeroski, Combining classifiers with meta decision trees, Mach. Learn. 50 (2003) 223–249.

[50] G. Wang, J. Hao, J. Ma, H. Jiang, A comparative assessment of ensemble learning for credit scoring. Expert Syst. Appl. 38 (2011) 223–230

[51] Y. Xia, C. Liu, B. Da, F. Xie, A novel heterogeneous ensemble credit scoring model based on bstacking approach, Expert Syst, Appl, 93 (2018) 182–199

[52] H.M. Gomes, A. Bifet, J. Read, J.P. Barddal, F. Enembreck, B. Pfharinger, G. Holmes. T. Abdessalem. Adaptive random forests for evolving data stream classification, Mach. Learn. 106 (2017) 1469–1495

[53] Y. Zhu, C. Xie, G.J. Wang, X.G. Yan, Comparison of individual, ensemble and integrated ensemble machine learning methods to predict China's SME credit risk in supply chain finance, Neural Comput. & Applic. 28 (2017) 41–50.

[54] F.N. Koutanaei, H. Sajedi, M. Khanbabaei, A hybrid data mining model of feature selection algorithms and ensemble learning classifiers for credit scoring, J. Retail. Consum, Sery. 27 (2015) 11–23

[55] S. Finlay, Multiple classifier architectures and their application to credit risk assessment, Eur, J Oper, Res, 210 (2011) 368–378

[56] G. Wang, J. Ma, L. Huang, K. Xu, Two credit scoring models based on dual strategy ensemble trees, Knowl.-Based Syst. 26 (2012) 61–68.

[57] M.N. Adnan, M.Z. Islam, Forest PA: constructing a decision forest by penalizing attributes used in previous trees, Expert Syst. Appl. 89 (2017) 389–403.

[58] M. Abedini, F. Ahmadzadeh, R. Noorossana, Customer credit scoring using a hybrid data mining approach. Kybernetes 45 (2016) 1576–1588

[59] E. Frank, Y. Wang, S. Inglis, G. Holmes, I.H. Witten, Using model trees for classification. Mach Learn. 32 (1998) 63–76

[60] I.H. Witten, E. Frank, M.A. Hall, CJ. Pal. Data Mining: Practical Machine Learning Tools and Techniques, Elsevier, Amsterdam, 2017.

[61] H.A. Abdou, J. Pointon, Credit scoring, statistical techniques and evaluation cri teria: a review of the literature, Intell. Syst. Accounting, Financ. Manag. 18 (2011) 59-88.

[62] T. Verbraken, W. Verbeke, B. Baesens, A novel profit maximizing metric for measuring classification performance of customer churn prediction models, IEEE Trans. Knowl. Data Eng. 25 (2013) 961–973.

[63] T. Fawcett, An introduction to ROC analysis, Pattern Recogn. Lett. 27 (2006) 861–874.

[64] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique, J. Artif. Intell. Res. 16 (2002) 321–357.

[65] L. Sànchez, I. Couso, J.A. Corrales, Combining GP operators with SA search to evolve fuzzy rule based classifiers, Inf. Sci. 136 (2001) 175–191.

Monika Papouskova received M.S. degree in system engineering and informatics from the University of Pardubice, Czech Republic, in 2011. She is currently a Ph.D. student in applied informatics with the Institute of System Engineering and Informatics, Faculty of Economics and Administration, University of Pardubice, Czech Republic. Her research interests include credit risk modelling using machine learning methods.

Petr Hajek received degree in economic policy and administration from the University of Pardubice, Czech Republic, in 2003, and a Ph.D. degree in system engineering and informatics from the University of Pardubice, Czech Republic, in 2006. He is currently an associate professor with the Institute of System Engineering and Informatics, Faculty of Economics and Administration, University of Pardubice, Czech Republic. He is the author or co-author of four books and more than 80 articles. His research interests include knowledge-based systems and soft computing.
