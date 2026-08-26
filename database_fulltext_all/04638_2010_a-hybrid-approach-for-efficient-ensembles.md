---
otero_id: 4638
otero_key: "5348YWVJ"
title: "A hybrid approach for efficient ensembles"
authors: "Dan Zhu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.06.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid approach for ef<sup>fi</sup>cient ensembles

Dan Zhu

Department of Logistics, Operations and MIS, Iowa State University, Ames, IA 50011, USA

## a r t i c l e i n f o

Available online 17 June 2009

Keywords: Ensembles Classi<sup>fi</sup>cation Data envelopment analysis Stacking

## a b s t r a c t

An ensemble of classi<sup>fi</sup>ers, or a systematic combination of individual classi<sup>fi</sup>ers, often results in better classi<sup>fi</sup>cations in comparison to a single classi<sup>fi</sup>er. However, the question regarding what classi<sup>fi</sup>ers should be chosen for a given situation to construct an optimal ensemble has often been debated. In addition, ensembles are often computationally expensive since they require the execution of multiple classi<sup>fi</sup>ers for a single classi<sup>fi</sup>cation task. To address these problems, we propose a hybrid approach for selecting and combining data mining models to construct ensembles by integrating Data Envelopment Analysis and stacking. Experimental results show the ef<sup>fi</sup>ciency and effectiveness of the proposed approach.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

To reveal interesting data patterns, usually hidden within large data sets, diverse mining concepts and techniques have often been used [8,17,18]. Classi<sup>fi</sup>cation, a common mining technique, is one of the most explored topics within data mining. Signi<sup>fi</sup>cant effort and research has been devoted to the construction of a reliable classi<sup>fi</sup>er or classi<sup>fi</sup>ers which can accurately predict values for the categorical variable class. For example, to test the robustness of classi<sup>fi</sup>ers, training data – which contains known class values – is often utilized. Classi<sup>fi</sup>ers can then learn to more accurately predict class values for similar, unknown datasets. Other methods for predicting class values often use a variety of algorithms, many of which have been proposed in the accompanying literature [13,20,26,28]. While many effective algorithms have been developed for constructing classi<sup>fi</sup>ers, no single algorithm has been shown to be either empirically or theoretically better than other algorithms in all scenarios [4,30]. From this perspective, determining which data mining algorithm to utilize can be perplexing. Although some basic rules exist in choosing an appropriate algorithm, in many cases, the <sup>fi</sup>nal decision is based more on random, personal preference.

To address the problem, one proposed solution involves the use of ‘ensemble methods’ — systematically combining different classi-<sup>fi</sup>ers. Research has shown that combining a set of simple classi<sup>fi</sup>ers may result in better classi<sup>fi</sup>cation in comparison to any single sophisticated classi<sup>fi</sup>er [7,17]. Furthermore, the subsequent combination of sophisticated and unsophisticated classi<sup>fi</sup>ers improves classi<sup>fi</sup>cation dramatically when compared to simple classi<sup>fi</sup>er combinations [1,7,14,16,17,27]. Among the diverse ensemble classi-<sup>fi</sup>cation techniques that are available, voting based Bagging (short for Bootstrap Aggregating) and Boosting are most often utilized. To understand how the combination of Bagging or Boosting with other classi<sup>fi</sup>cation techniques is bene<sup>fi</sup>cial, basic understanding of individual classi<sup>fi</sup>cation techniques is required. Individually, Bagging and Boosting both <sup>fi</sup>nalize classi<sup>fi</sup>cations through voting; however, each derives models in dissimilar ways [4,23]. Although Bagging and Boosting have shown signi<sup>fi</sup>cant classi<sup>fi</sup>cation improvements, including all classi<sup>fi</sup>ers into one ensemble would be impractical. As a result, researchers have begun investigating a dynamic approach to constructing ensembles by taking into account characteristics of any dataset and incorporating the best classi<sup>fi</sup>ers for that particular dataset. However, the selection of a classi<sup>fi</sup>er as the meta-learner is not clearly de<sup>fi</sup>ned. In addition, the combination of these classi<sup>fi</sup>ers has remained simple-minded.

In this study, we propose a new hybrid approach for constructing an ensemble classi<sup>fi</sup>er by integrating Data Envelopment Analysis (DEA) and stacked generalization. DEA is a nonparametric method developed by Professor William Cooper in Operations Research and Economics for estimation of production frontiers [6]. An experimental study is designed to show the ef<sup>fi</sup>ciency and effectiveness of the proposed method. Rest of the papers is organized as follows. Section 2 reviews the literature in ensemble data mining; Section 3 introduces our hybrid DEA-based ensemble construction approach; Section 4 presents the framework of the proposed system and its components, Section 5 presents experiments and results, and Section 6 concludes the work and provides directions for future research.

## 2. Related work

The main objective of an ensemble approach is to improve classi<sup>fi</sup>cation accuracy by aggregating the classi<sup>fi</sup>cations of a diverse of classi<sup>fi</sup>ers. Previous research has shown that an ensemble of classi<sup>fi</sup>ers is often more accurate than any of the single classi<sup>fi</sup>ers in the ensemble [17]. Two popular ensemble methods are Bagging [4] and Boosting [9,10,23] and they both employ re-sampling techniques to obtain different training sets for each of the classi<sup>fi</sup>ers.

AdaBoost, short for Adaptive Boosting, is the most common implementation of the Boosting algorithm. It performs several learning iterations based on the same training set. The decisions of the classi<sup>fi</sup>ers in the ensemble are combined by using weighted voting, where each weight depends on the error of the classi<sup>fi</sup>er on the training set. It has been found that the classi<sup>fi</sup>er produced by AdaBoost has signi<sup>fi</sup>cantly lower error rates than a single decision tree [11]. Additionally, AdaBoost can avoid over <sup>fi</sup>tting problems. Despite these advantages and common usage, there are some disadvantages associated with AdaBoost. It is less likely to be effective if weak learners are actually strong and the test error might be larger than training error if the hypotheses are too complex [10,22]. One study has shown that AdaBoost can perform poorly when the training data is noisy, and it has very long training time [7].

Bagging (Bootstrap aggregating) generates different training sets by randomly drawing replacements from the original data set. The classi<sup>fi</sup>ers' decisions are then combined by using the majority vote with equal weight. Research has shown that bagging often produces good results since decision trees tend to have a high variance [11]. However, Bagging performs very poorly with stumps, which are single-split trees with only two terminal nodes that have a low variance. Despite this limitation, Bagging has been found to be the simplest algorithm that helps in reducing variance and improving unstable classi<sup>fi</sup>ers in accuracy [4]. It also enhances accuracy when random features are used and can help avoid over <sup>fi</sup>tting.

Random Forest [5] is another ensemble method that is tailored for the decision tree classi<sup>fi</sup>ers. Similar to Bagging, Random Forest creates k decision trees, where each tree is independently generated by random decisions. Bagging that uses decision trees can be viewed as a special case of Random Forests where the random decisions are the random creations of the bootstrap samples. Random Forest can derive an upper bound for the generalization error through two parameters which measure the accuracy of individual classi<sup>fi</sup>ers and the dependence between them. It is also relatively robust to outliers and noise, it is faster than Bagging, and this ensemble method gives useful internal estimates of error, strength, correlation and variable importance. Conversely, Random Forest is prone to over <sup>fi</sup>tting in noisy classi<sup>fi</sup>cation tasks and it is ineffective when handling a large number of irrelevant features [12].

Most of the ensemble methods rely on only one automatic base classi<sup>fi</sup>er (mostly decision tree) and then construct multiple classi<sup>fi</sup>ers by perturbing the training data [21]. Little research, however, has been devoted to constructing ensembles with different base classi<sup>fi</sup>ers. In this research, we explore a hybrid approach that employs a Data Envelopment Analysis (DEA) model for model selection, and we propose adopting a stacking method and DEA for an effective model combination. Table 1 presents a comparative summary of the selected aspects of this proposed approach along with the previously discussed methods.

Comparative summary of selected approaches

<table><tr><td>Method</td><td>Number of base classifiers</td><td>Combination of classifiers</td><td>Base inducer</td><td>Experiments</td><td>Primary reference</td></tr><tr><td>AdaBoost</td><td>Single</td><td>Weighted voting</td><td>Decision Tree C4.5</td><td>10-fold cross validation</td><td>Freund and Schapire [9]</td></tr><tr><td>Bagging</td><td>Single</td><td>Equal voting Majority vote</td><td>Decision Tree C4.5</td><td>10-fold cross validation</td><td>Breiman [4]</td></tr><tr><td>Random Forest (RF)</td><td>Multiple</td><td>Unit voting Majority vote</td><td>Decision Tree (Revised C4.5)</td><td>90-10 split</td><td>Breiman [5]</td></tr><tr><td>This work</td><td>Multiple</td><td>Stacking</td><td>DEA</td><td>10-fold cross validation</td><td>Zhu</td></tr></table>

## 3. Design of a two-step procedure

Ensemble methods have been proved to be more effective than single classi<sup>fi</sup>ers. However, two questions arise when creating an ensemble: (1) What models to choose? (2) How to combine them? In this research, we propose a two-step procedure to construct ef<sup>fi</sup>cient and effective ensemble as described below.

## 3.1. Model selection with data envelopment analysis

Although numerous data mining algorithms have been developed, a major concern in constructing ensembles is how to select appropriate data mining algorithms as ensemble components. A challenge is that there is not a single algorithm that can outperform any other algorithms in all data mining tasks, i.e. there is no global optimum solution in selecting data mining algorithms although much effort has been devoted to this area. An ROC (Receiver Operating Characteristics) analysis based approach was approved to evaluate the performance of different classi<sup>fi</sup>ers and an algorithm, called ROC Convex Hull (ROCCH), was developed to identify the best classi<sup>fi</sup>ers [19]. In a two-class classi<sup>fi</sup>cation problem, one class is normally referred to as positive, and the other as negative. The true positive rate (TP) is the proportion of positive cases that were correctly identi<sup>fi</sup>ed and false positive rate (FP) is the proportion of negative cases that were incorrectly classi<sup>fi</sup>ed as positive.

An optimum classi<sup>fi</sup>er would yield TP=1 and FP=0. However in practice, there is a TP and FP tradeoff for classi<sup>fi</sup>ers and increasing the TP may also result in a higher FP [6]. For every classi<sup>fi</sup>er, we can calculate its TP and FP and map it to a two dimensional space with FP on the x-axis and TP on the y-axis. The most ef<sup>fi</sup>cient classi<sup>fi</sup>ers should lie on the convex hull of this ROC plot since they represent the most ef<sup>fi</sup>cient TP and FP tradeoff. Those classi<sup>fi</sup>ers that do not lie on the convex hull are considered as inef<sup>fi</sup>cient.

The algorithm for ROC Convex Hull (ROCCH) can help in identifying the best models on the convex hull. ROCCH was proved effective in identifying ef<sup>fi</sup>cient classi<sup>fi</sup>ers. However, one major disadvantage about ROCCH is that it can only deal with two-class classi<sup>fi</sup>cation problems. Inspired by ROCCH, Zheng and Padmanabhan [31] <sup>fi</sup>rst proposed to apply DEA to construct ensembles and they showed that both ROCCH and DEA identify a convex hall and the two convex hull were identical for a classi<sup>fi</sup>cation problem with two classes.

DEA is a nonparametric approach that addresses the issue of determining the ef<sup>fi</sup>ciency of various “decision making units” (DMUs) based on how inputs are converted into outputs [24]. A DMU is rated as fully ef<sup>fi</sup>cient (100%) if and only if the performance of other DMUs does not show that some of its inputs or outputs can be improved without worsening some of its other inputs or outputs [6]. DEA uses mathematical programming to identify ef<sup>fi</sup>cient DMUs, which form an ef<sup>fi</sup>cient frontier. There are different forms of the DEA model, of which the most commonly used model is the BCC model [3], which was adopted by [31]. For consistency and comparison purpose, we employed the BCC model in our study. However, there are many types of DEA models and different DEA models generally produce different results. This may have a signi<sup>fi</sup>cant impact to the model selection and thus in<sup>fl</sup>uence the <sup>fi</sup>nal results. We will have further discussions on this in the conclusion and future research in Section 6.

## 3.2. Model combination with DEA and stacking

Once the models are selected, the next critical step involves the combination of ensembles. As pointed out by Dietterich [7], an ensemble can achieve better performance than a single classi<sup>fi</sup>er in three fundamental ways: statistical, computational, and representational. The statistical analysis indicates that any learning algorithm tries to <sup>fi</sup>nd an accurate hypothesis against the training data. Constructing an ensemble with all classi<sup>fi</sup>ers will allow the algorithm to reduce the risk of choosing the wrong hypothesis. The computational argument is that many learning algorithms perform some sort of local search in the hypotheses space that may result in a local optimum. An ensemble constructed by running the local search from multiple different starting points may result in a better approximation to the true hypothesis. Finally, the representational analysis follows from the fact that a learning algorithm may not be capable of representing the true function. By combining several different hypotheses, it may be possible to expand the space of representational functions.

A straightforward and ef<sup>fi</sup>cient method is Ef<sup>fi</sup>cient Models Only (EMO) that selects only the ef<sup>fi</sup>cient models and then applies majority voting [4] to these ef<sup>fi</sup>cient models. Another possible method is the Ef<sup>fi</sup>ciency Score Weighting (ESW), which uses all models and weighs each model according to its ef<sup>fi</sup>ciency score θ [31]. In this paper, we propose incorporating the stacked generalization scheme in conjunction with the DEA for constructing ensembles. Stacking is a method of estimating and correcting the biases of the constituent generalizer with respect to the provided learning set. It can be used with a single generalizer and has been found to reduce the generalization error rate for many generalization problems. Stacking is also found to achieve better predictive accuracy when combining different types of learning algorithms [29].

Little research, however, has been devoted to stacking. As described in [25], the training process of the stacked generalization scheme is separated into two steps. The <sup>fi</sup>rst step is J-fold cross-validation process. Given a data $\mathsf { s e t } l = \{ ( x _ { i } , y ( x _ { i } ) ) , i = 1 , . . . , N \}$ where y (x ) is the class value of the n-the instance and $x _ { i }$ represents the associated attribute value, we run a J-fold cross-validation process over $\ell$ with K different learning algorithms. Before the cross-validation starts, the data set is randomly split into J equally disjoint subsets, i.e. $l { = } l _ { 1 } \cup . . . \cup l _ { i } \cup . . . \cup l _ { j } .$ At the j-th fold, all of the K learning algorithms are invoked on the training set of $l _ { j } ^ { \prime } = l \vert l _ { j }$ respectively, and M <sup>j</sup> denotes the model built by the i-th learning algorithm. The class value of a given element $\boldsymbol { x } \in l _ { j }$ predicted by M<sup>j</sup> is denoted as y(x)<sup>j</sup>. Accordingly, we have a vector $Y ^ { j } ( \overset { \cdot } { x } ) = \{ y ( x ) , . . . , y ( x ) _ { i } ^ { \mathrm { j } } , . . . . ,$ $y ( x ) _ { \mathrm { K } } ^ { \mathrm { j } } \}$ to encode the original class value as well as the predicted class values. We use $H ^ { \mathrm { j } } = \{ Y ^ { \mathrm { j } } ( x ) { : \bf x } \in l _ { j } \}$ to denote a set of vectors. The entire Jfold cross-validation process results in the level-1data set, which is $L { = } H ^ { 1 } \cup \ldots \cup H ^ { \mathrm { i } } \cup \ldots \cup H ^ { \mathrm { J } }$ . Invoking another learning algorithm P, which can belong to the existing K algorithms or be an extra one, on the level-1 data set and obtain a model $M _ { \mathrm { P } }$ referred to as the level-1 model. The second step of the training process applies K learning algorithms on the data set l to obtain K prediction models, and each of which is denoted as M for the i-th learning algorithm. Given a new instance a, the i-th prediction model $M _ { i }$ computes a predicted class value $y ( a ) _ { i }$ The level-1 model uses the aggregated vector, $\Upsilon ( a ) { = } \{ \mathrm { y } ( a )  _ { 1 } { , } . . . . , \mathrm { y } ( a ) _ { i } { , } . . . . , \mathrm { y } ( a ) _ { \mathrm { K } } \}$ , as the input and obtains the <sup>fi</sup>nal predicted class value. Due to the page limit, we are not going to go into any additional details. For further information about the stacking method, please refer to [25,28,29].

## 3.3. Similarity and difference between two approaches

Table 2 presents a comparative summary of our approach and another DEA-based approach recently proposed in the literature. The primary similarity between our approach and Zheng and Padmanabhan's [31] is that we both employed DEA in selecting data mining models in the <sup>fi</sup>rst stage. However, our approach is signi<sup>fi</sup>cantly different as we go beyond this selection process and propose a hybrid approach for model combination through DEA and the stacking method. As shown in Table 2, two alternative methods were proposed in [31]: combining base classi<sup>fi</sup>ers based on ef<sup>fi</sup>ciency scores θ, i.e. Ef<sup>fi</sup>cient Models Only (EMO) and Ef<sup>fi</sup>ciency Score Weighting (ESW). It was found that ESW is better than EMO, as well as the naive weighted and un-weighted average methods, which simply average the predictions provided by each data mining model.

It has been found that stacking method is particularly better suited for combining multiple different types of models. Stacked generalization provides a way for this situation which is more sophisticated than winner-takes-all approach. Instead of selecting one speci<sup>fi</sup>c generalizer out of multiple ones, the stacking method combines them by using their output information as inputs into a new space. Stacking then generalizes the guesses in that new space. Therefore, stacked generalization can be viewed as a more sophisticated version of non-parametric statistical techniques such as cross-validation. The winner-takes-all combination approach is a special case of stacked generalization.

Table 2  
Comparative summary of the two approaches.

<table><tr><td>Method</td><td>Selection of base classifiers</td><td>Combination of classifiers</td><td>Experiments</td><td>Reference</td></tr><tr><td rowspan="2">Zheng&amp;Padmanabhan</td><td rowspan="2">DEA</td><td>EMO</td><td rowspan="2">60-40 split</td><td rowspan="2">[31]</td></tr><tr><td>ESW</td></tr><tr><td>Zhu</td><td>DEA</td><td>DEA+Stacking</td><td>10-fold cross validation</td><td>This work</td></tr></table>

The simple voting approaches have their obvious limitations due to their abilities in capturing only linear relationships. In stacking, an ensemble of classi<sup>fi</sup>ers is <sup>fi</sup>rst trained using bootstrapped samples of the training data, producing level-0 classi<sup>fi</sup>ers. The outputs of the level-0 classi<sup>fi</sup>ers are then used to train a level-1 classi<sup>fi</sup>er (i.e. metaclassi<sup>fi</sup>er). The goal of this next level is to ensure that the training data has accurately completed the learning process. For example, if a classi<sup>fi</sup>er consistently misclassi<sup>fi</sup>ed instances from one region as a result of incorrectly learning the feature space of that region, the metaclassi<sup>fi</sup>er may be able to discover this problem. Using the learned behaviors of other classi<sup>fi</sup>ers, it can improve such training de<sup>fi</sup>ciencies.

As described in the previous section, the multi-levels learning (e.g. level-0 model and level-1 generalizer) provides a better chance to capture the more complex relationship in the problem. This makes the stacking method be a good candidate in modeling potential subtle nonlinear combinations to construct the best ensembles. Through integration of DEA and stacking method, we are able to create more ef<sup>fi</sup>cient and effective ensembles which are signi<sup>fi</sup>cantly better than the existing approaches as con<sup>fi</sup>rmed through extensive experimentation presented in Section 5. Another difference between the two approaches is that we included less number of base classi<sup>fi</sup>ers. Instead of including an almost exhaustive list of classi<sup>fi</sup>ers, we selected only twelve diverse data mining algorithms as our base classi<sup>fi</sup>ers. By doing so, we are able to reduce the complexity and computational time while achieving better performance.

Since DEA evaluates each classi<sup>fi</sup>er by analyzing the confusion matrix, DEA requires all participating classi<sup>fi</sup>ers to be trained in order to generate confusion matrices. As a result, this procedure could often be computation intensive and time-consuming. For example, in [31], up to 29 models (classi<sup>fi</sup>ers) were evaluated for one dataset. If this evaluation is to be done on a single machine, all 29 models (classi<sup>fi</sup>ers) need to be trained one by one and subsequently evaluated. Hence, if DEA is to be fully utilized by incorporating as many different classi<sup>fi</sup>ers as possible and to be applicable to problems with multiple classes, its ef<sup>fi</sup>ciency in model evaluation is critical. We therefore expect to address this problem and reduce inef<sup>fi</sup>ciency by incorporating distributed computing [15].

## 4. A hybrid approach for ensemble classi<sup>fi</sup>ers

Most ensemble methods need to evaluate multiple models for one speci<sup>fi</sup>c task. Given that it is impractical to apply as many models as possible to the entire target data space, it is still possible to evaluate as many of them as possible on the training dataset if the evaluation is done properly. Instead of evaluating models sequentially on a single machine, we propose to assign the evaluation task to different machines so they can be performed simultaneously. In our framework, different classi<sup>fi</sup>ers need not be actually assigned to different individual machines. Utilizing the multi-tasking capability of multi-core processors that are prevalent today can greatly facilitate evaluating multiple classi<sup>fi</sup>ers in parallel.

## 4.1. Framework of the proposed system

As shown in Fig. 1, the system mainly consists of <sup>fi</sup>ve components: (1) The user interface, where users can interact with the system, input data into the database server, and obtain <sup>fi</sup>nal classi<sup>fi</sup>cation results from the system; (2) The database server is designed for ef<sup>fi</sup>cient retrieval, storage, and delivery of data; (3) The base classi<sup>fi</sup>ers $C _ { 1 , } C _ { 2 , } . . . ,$ $C _ { n }$ (or stacked classi<sup>fi</sup>ers $S C _ { 1 , } S C _ { 2 , } { \ldots } , S C _ { n } )$ are individual machines, each of which carries a certain classi<sup>fi</sup>cation algorithm and is pre-con<sup>fi</sup>gured to best <sup>fi</sup>t the requirements of the algorithm; (4) The DEA server is a machine equipped with Data Envelopment Analysis capability (e.g. DEA Frontier) that computes ef<sup>fi</sup>ciency scores for each classi<sup>fi</sup>er and determines the most ef<sup>fi</sup>cient classi<sup>fi</sup>cation model, based on confusion matrices received; and (5) Ensemble meta-classi<sup>fi</sup>er is a conceptual model that combines classi<sup>fi</sup>cation results from participating classi<sup>fi</sup>ers and generates the <sup>fi</sup>nal classi<sup>fi</sup>cation results that will be sent back to users.

Users input data along with a relatively small set of training data into the system to the database server through the user interface, and manipulate system settings by working with the system. Through an intuitive design of the user interface, users should be allowed to specify (but not limited to) the following settings: (1) classi<sup>fi</sup>ers to be evaluated; (2) DEA model; (3) the method to be used for combining base classi<sup>fi</sup>ers as an ensemble.

The database server facilitates data retrieval, storage, and delivery. It should be able to connect easily to the distributed database. The database server should also support data <sup>fi</sup>les with different formats and facilitate converting these <sup>fi</sup>les from one format to another. The coordinating mechanism may exist, which connects to other components in the system. It maintains an ef<sup>fi</sup>cient communication protocol with the database server, DEA server, and classi<sup>fi</sup>ers and it also sends and receives messages along the connecting network following pre-speci<sup>fi</sup>ed procedures. It translates users' requirements into system messages and sends them to the components that need to be adjusted. For example, if users require a different method to combine classi<sup>fi</sup>ers, the system should be able to switch to the preferred module in the ensemble classi<sup>fi</sup>er and assign the dataset in query to proper classi<sup>fi</sup>ers accordingly.

Each base-classi<sup>fi</sup>er learns from training dataset separately, based on which a classi<sup>fi</sup>cation model is built. At the end of the learning process, base-classi<sup>fi</sup>ers evaluate their performance with crossvalidation, and generate confusion matrices. A confusion matrix is a matrix that contains information about actual and predicted classi-<sup>fi</sup>cations performed by a classi<sup>fi</sup>er.

As shown in Table 3 for a two class classi<sup>fi</sup>er, the accuracy is de<sup>fi</sup>ned in the following equation as the proportion of the total number of classi<sup>fi</sup>cations that were correct to the total instances:

$$
A c c u r a c y = (C _ {1 1} + C _ {2 2}) / (C _ {1 1} + C _ {1 2} + C _ {2 1} + C _ {2 2})\tag{1}
$$

The true positive rate (TP) is de<sup>fi</sup>ned as:

$$
T P = C _ {2 2} / (C _ {2 1} + C _ {2 2})\tag{2}
$$

And the false positive rate (FP) is de<sup>fi</sup>ned as:

$$
F P = C _ {1 2} / (C _ {1 1} + C _ {1 2})\tag{3}
$$

For a k-class problem, a confusion matrix CM is a k×k matrix. Each element $C _ { i j }$ is de<sup>fi</sup>ned as the number of instances that are classi<sup>fi</sup>ed as class j when it is in fact class i. When i ≠ j, $C _ { i j } ,$ misclassi<sup>fi</sup>cations are denoted. Otherwise, when $i = j , C _ { i i } ,$ correct classi<sup>fi</sup>cations are denoted. As proved in [31], DEA and ROC convex hulls are identical. Therefore, a classi<sup>fi</sup>er can be viewed as a DMU that attempts to produce $C _ { i i }$ at the expense of $C _ { i j } .$ In other words, a classi<sup>fi</sup>er is perceived as aims at maximizing diagonal variables $C _ { i i }$ and minimizing off-diagonal variables $C _ { i j } .$ Thus, in this case, $C _ { i j }$ can be taken as the inputs and $C _ { i i }$ as the outputs to the DEA model.

Confusion matrices are sent to the DEA server for evaluation, and each confusion matrix will result in an ef<sup>fi</sup>ciency score. All or part of base classi<sup>fi</sup>ers will be selected to classify the dataset in query, depending on the method used for combining base classi<sup>fi</sup>er. In the end, all classi<sup>fi</sup>cation results are sent to the ensemble classi<sup>fi</sup>er for combination. We denote a classi<sup>fi</sup>er as a machine equipped with one classi<sup>fi</sup>cation algorithm. In reality, this requirement can be relaxed so that a machine can carry more than one algorithm. In creating this architecture, the cost of setting up more machines with fewer algorithms to achieve higher ef<sup>fi</sup>ciency needs to be considered against a more economically feasible plan of assigning more algorithms to fewer machines.

![](/api/attachments/5348YWVJ/fulltext/images/3a60ef562e139ed5652b44eec938de82c77416ed950482fb91c85321f2c35d54.jpg)  
Fig. 1. Proposed hybrid framework.

Table 3 Confusion matrix.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Predicted</td></tr><tr><td>Negative (0)</td><td>Positive (1)</td></tr><tr><td rowspan="2">True</td><td>Negative (0)</td><td> $C_{11}$ </td><td> $C_{12}$ </td></tr><tr><td>Positive (1)</td><td> $C_{21}$ </td><td> $C_{22}$ </td></tr></table>

Notes: $C _ { 1 1 } \colon$ number of negative instances that are correctly classi<sup>fi</sup>ed.  
$C _ { 1 2 } \mathrm { : }$ number of negative instances that are incorrectly classi<sup>fi</sup>ed  
$C _ { 2 1 } \colon$ number of positive instances that are incorrectly classi<sup>fi</sup>ed.  
$C _ { 2 2 } { : }$ number of positive instances that are correctly classi<sup>fi</sup>ed.

The DEA server is a separate machine equipped with mathematical programming capabilities. With a pre-speci<sup>fi</sup>ed formulation model (e.g. BCC used in this study or other radial and non-radial models), the DEA server is able to evaluate the confusion matrices received from all the base classi<sup>fi</sup>ers. It then generates an ef<sup>fi</sup>ciency score, indicating the ef<sup>fi</sup>ciency performance of each of them. These ef<sup>fi</sup>ciency scores are sent back to the system. Once the ef<sup>fi</sup>cient classi<sup>fi</sup>ers have been identi<sup>fi</sup>ed, several methods can be used to combine them as an ensemble. In this case, these ef<sup>fi</sup>cient base classi<sup>fi</sup>ers selected by DEA will be combined through the stacking method and corresponding confusion matrices will be fed back to DEA. The DEA server will evaluate the confusion matrices to determine the most ef<sup>fi</sup>cient classi<sup>fi</sup>cation model through the stacking learner, which produces the ensemble classi<sup>fi</sup>er for <sup>fi</sup>nal classi<sup>fi</sup>cation decision.

## 4.2. An illustrative example

In this section, we demonstrate our approach using the breast-w dataset from The University of California at Irvine (UCI) Machine Learning Repository [2]. As an illustrative example, breast-w is used as a training dataset with which an ensemble classi<sup>fi</sup>er is constructed. This ensemble classi<sup>fi</sup>er can thus be applied to the database from which the training dataset is developed.

Within the breast-w dataset, 699 instances and 10 attributes are contained. Our goal is to classify each instance as one of two classes. Classi<sup>fi</sup>cation models available are J48, DecisionStump, PART, OneR, ZeroR, IB1, IBk5, KStar, NaiveBayes, Logistic, SMO and MultilayerPerceptron. Our approach involves <sup>fi</sup>ve sequential steps, explained in detail as follows:

Step 1. Use all classi<sup>fi</sup>cation models one by one to classify the training dataset. For each model, a confusion matrix C is generated.

Table 4  
Results from individual base classi<sup>fi</sup>ers.

<table><tr><td>Classification model</td><td> $C_{11} (y_1)$ </td><td> $C_{12} (x_1)$ </td><td> $C_{21} (x_2)$ </td><td> $C_{22} (y_2)$ </td><td>Accuracy*</td><td>MSE</td></tr><tr><td>IBk5</td><td>444</td><td>14</td><td>9</td><td>232</td><td>96.71%</td><td>0.0249</td></tr><tr><td>Logistic</td><td>446</td><td>12</td><td>12</td><td>229</td><td>96.57%</td><td>0.0278</td></tr><tr><td>SMO</td><td>446</td><td>12</td><td>9</td><td>232</td><td>97.00%</td><td>0.03</td></tr><tr><td>Kstar</td><td>448</td><td>10</td><td>22</td><td>219</td><td>95.42%</td><td>0.0361</td></tr><tr><td>MultilayerPerceptron</td><td>440</td><td>18</td><td>15</td><td>226</td><td>95.28%</td><td>0.0388</td></tr><tr><td>NaiveBayes</td><td>436</td><td>22</td><td>6</td><td>235</td><td>95.99%</td><td>0.0398</td></tr><tr><td>IB1</td><td>443</td><td>15</td><td>18</td><td>223</td><td>95.28%</td><td>0.0472</td></tr><tr><td>J48</td><td>438</td><td>20</td><td>18</td><td>223</td><td>94.56%</td><td>0.0497</td></tr><tr><td>PART</td><td>439</td><td>19</td><td>24</td><td>217</td><td>93.85%</td><td>0.0499</td></tr><tr><td>DecisionStump</td><td>417</td><td>41</td><td>12</td><td>229</td><td>92.42%</td><td>0.0669</td></tr><tr><td>OneR</td><td>444</td><td>14</td><td>37</td><td>204</td><td>92.70%</td><td>0.073</td></tr><tr><td>ZeroR</td><td>458</td><td>0</td><td>241</td><td>0</td><td>65.52%</td><td>0.2259</td></tr></table>

Notes: The accuracy is the proportion of the total number of classi<sup>fi</sup>cations that were correct. $C _ { 1 1 } ( y _ { 1 } ) , C _ { 1 2 } ( x _ { 1 } ) , C _ { 2 1 } ( x _ { 2 } ) , C _ { 2 2 } ( y _ { 2 } )$ will be fed into DEA server for base classi<sup>fi</sup>ers evaluation. Special treatment will be used to handle zeros.

Table 5  
Results from DEA selection for base classi<sup>fi</sup>ers.

<table><tr><td>Classification model</td><td>Efficiency</td></tr><tr><td>Kstar*</td><td>1.00000*</td></tr><tr><td>NaiveBayes*</td><td>1.00000*</td></tr><tr><td>SMO*</td><td>1.00000*</td></tr><tr><td>ZeroR*</td><td>1.00000*</td></tr><tr><td>Logistic</td><td>0.9658</td></tr><tr><td>IBk5</td><td>0.95318</td></tr><tr><td>IB1</td><td>0.74701</td></tr><tr><td>OneR</td><td>0.69485</td></tr><tr><td>MultilayerPerceptron</td><td>0.65003</td></tr><tr><td>PART</td><td>0.57954</td></tr><tr><td>J48</td><td>0.57698</td></tr><tr><td>DecisionStump</td><td>0.50576</td></tr></table>

Notes: Ef<sup>fi</sup>cient models are marked ${ \sf a s } ^ { * * } .$ In this speci<sup>fi</sup>c case, ZeroR, KStar, NaiveBayes and SMO are selected as base-classifiers

Table 4 shows the results including accuracy and Mean Squared Error (MSE).

Step 2. Take $C _ { 1 2 } \left( x _ { 1 } \right)$ and $C _ { 2 1 } \left( x _ { 2 } \right)$ as inputs, and $C _ { 1 1 } \left( y _ { 1 } \right)$ and $C _ { 2 2 } \left( y _ { 2 } \right)$ as outputs in DEA. Since DEA models cannot directly handle zero in data. When we deal with zero or a negative value, we need to apply additional processing. In our experiment, DEA frontier is used to compute model ef<sup>fi</sup>ciencies. Table 5 shows the results generated by DEA frontier.

Step 3. Based on ef<sup>fi</sup>ciencies computed in Step 2, ef<sup>fi</sup>cient classi<sup>fi</sup>ers (i.e. classi<sup>fi</sup>ers that have an ef<sup>fi</sup>ciency of 1) are identi<sup>fi</sup>ed, as indicated by a ‘⁎’ in Table 5. These classi<sup>fi</sup>ers will subsequently be used as base classi<sup>fi</sup>ers in stacking. However, all classi<sup>fi</sup>cation models are considered as candidates for meta-classi<sup>fi</sup>ers in stacking. Using one model as the meta-classi<sup>fi</sup>er per event, we can test each event, using the same training dataset. Results are shown in Table 6.

Meta-classi<sup>fi</sup>er selection results.

<table><tr><td>Classification model</td><td> $SC_{11}$  ( $y_1$ )</td><td> $SC_{12}$  ( $x_1$ )</td><td> $SC_{21}$  ( $x_2$ )</td><td> $SC_{22}$  ( $y_2$ )</td><td>Accuracy*</td><td>MSE</td></tr><tr><td>MultilayerPerceptron</td><td>445</td><td>13</td><td>3</td><td>238</td><td>97.71%</td><td>0.0218</td></tr><tr><td>Kstar</td><td>445</td><td>13</td><td>7</td><td>234</td><td>97.14%</td><td>0.0257</td></tr><tr><td>J48</td><td>444</td><td>14</td><td>5</td><td>236</td><td>97.28%</td><td>0.0262</td></tr><tr><td>IBk5</td><td>446</td><td>12</td><td>7</td><td>234</td><td>97.28%</td><td>0.0262</td></tr><tr><td>PART</td><td>443</td><td>15</td><td>5</td><td>236</td><td>97.14%</td><td>0.0265</td></tr><tr><td>Logistic</td><td>446</td><td>12</td><td>9</td><td>232</td><td>97.00%</td><td>0.0279</td></tr><tr><td>DecisionStump</td><td>441</td><td>17</td><td>5</td><td>236</td><td>96.85%</td><td>0.0299</td></tr><tr><td>OneR</td><td>444</td><td>14</td><td>7</td><td>234</td><td>98.00%</td><td>0.03</td></tr><tr><td>SMO</td><td>446</td><td>12</td><td>9</td><td>232</td><td>97.00%</td><td>0.03</td></tr><tr><td>NaiveBayes</td><td>445</td><td>13</td><td>8</td><td>233</td><td>97.00%</td><td>0.0301</td></tr><tr><td>IB1</td><td>445</td><td>13</td><td>12</td><td>229</td><td>96.42%</td><td>0.0358</td></tr><tr><td>ZeroR</td><td>458</td><td>0</td><td>241</td><td>0</td><td>65.52%</td><td>0.2259</td></tr></table>

Notes: Accuracy is the proportion of the total number of classi<sup>fi</sup>cations that were correct. Stacked generalizer ${ \sf S C } _ { 1 1 } \left( y _ { 1 } \right) ,$ $S C _ { 1 2 } \left( x _ { 1 } \right) ,$ , SC (x ), SC (y ) will be fed into DEA server again for meta-classi<sup>fi</sup>er evaluation. Special treatment will be used to handle zeros.

Table 7  
DEA for Meta-classi<sup>fi</sup>er selection results

<table><tr><td>Classification model</td><td>Efficiency</td></tr><tr><td>MultilayerPerceptron*</td><td>1.00000*</td></tr><tr><td>IBk5*</td><td>1.00000*</td></tr><tr><td>ZeroR*</td><td>1.00000*</td></tr><tr><td>Logistic</td><td>0.99155</td></tr><tr><td>SMO</td><td>0.99155</td></tr><tr><td>Kstar</td><td>0.93036</td></tr><tr><td>NaiveBayes</td><td>0.9195</td></tr><tr><td>IB1</td><td>0.90528</td></tr><tr><td>J48</td><td>0.89976</td></tr><tr><td>OneR</td><td>0.86971</td></tr><tr><td>PART</td><td>0.8434</td></tr><tr><td>DecisionStump</td><td>0.74951</td></tr></table>

Notes: Ef<sup>fi</sup>cient models are marked as ‘⁎’. In this speci<sup>fi</sup>c case, MultilayerPerceptron is selected as the meta-classifier

Step 4. DEA is applied a second time to compute ef<sup>fi</sup>ciency scores for meta-classi<sup>fi</sup>er candidates. Table 7 shows the results.

Step 5. Ef<sup>fi</sup>cient classi<sup>fi</sup>ers are hence identi<sup>fi</sup>ed. The classi<sup>fi</sup>er with the highest accuracy or lowest MSE is selected as the metaclassi<sup>fi</sup>er. Together with the base classi<sup>fi</sup>ers selected in Step 3, an ensemble of classi<sup>fi</sup>ers that is tuned speci<sup>fi</sup>cally for breastw is thus constructed. In this case, MultilayerPerceptron is selected as the meta-classi<sup>fi</sup>er in stacking.

## 5. Experiments and results

Extensive experiments were conducted to empirically evaluate the performance of the proposed ensemble construction approach. In this section, we describe the design of our experiments and subsequent results.

## 5.1. Data sets

In this research, thirteen real-world and synthesized data sets from The UCI machine learning repository were evaluated. Table 8 presents a brief description of the data sets tested and details speci<sup>fi</sup>c characteristics. As shown in Table 8, data sets ranged from 2 to 5 classes and 9 to 61 attributes. The attributes had a mix of both nominal and numeric values, and the number of instances ranged from 57 to 3772 records.

## 5.1. Data sets

In this research, thirteen real-world and synthesized data sets from The UCI machine learning repository were evaluated. Table 1 presents a brief description of the data sets tested and details speci<sup>fi</sup>c characteristics. As shown in Table 6, data sets ranged from 2 to 5 classes and 9 to 61 attributes. The attributes had a mix of both nominal and numeric values, and the number of instances ranged from 57 to 3772 records.

## 5.2. Base classifier models

The base classi<sup>fi</sup>ers included in the initial ensembles consisted of many popular and diverse classi<sup>fi</sup>ers in data mining. Speci<sup>fi</sup>cally, classi<sup>fi</sup>ers included in this ensemble were decision tree (C4.5), decision stump, PART, OneR, ZeroR, IB1, IBk5, Kstar, NaiveBayes, logistic regression, support vector machine, and neural networks (multi-layer perceptron). Each model was selected based on its uniqueness and diversity. These twelve models were then fed into DEA frontier for ef<sup>fi</sup>ciency evaluation [6]. As shown in Table 8, the number of ef<sup>fi</sup>cient models and average ef<sup>fi</sup>ciency from DEA selection were also recorded.

Table 8  
Summary of data statistics and DEA selection results

<table><tr><td>Data set</td><td>Number of records</td><td>Number of attributes</td><td>Number of classes</td><td>Number of efficient models</td><td>Average efficiency</td></tr><tr><td>Breast-w</td><td>699</td><td>10</td><td>2</td><td>4</td><td>0.806</td></tr><tr><td>Colic</td><td>368</td><td>23</td><td>2</td><td>4</td><td>0.909</td></tr><tr><td>Credit-a</td><td>690</td><td>16</td><td>2</td><td>5</td><td>0.938</td></tr><tr><td>Credit-g</td><td>1,000</td><td>21</td><td>2</td><td>4</td><td>0.936</td></tr><tr><td>Diabetes</td><td>768</td><td>9</td><td>2</td><td>3</td><td>0.907</td></tr><tr><td>Heart-c</td><td>303</td><td>14</td><td>5</td><td>4</td><td>0.832</td></tr><tr><td>Heart-h</td><td>294</td><td>14</td><td>5</td><td>3</td><td>0.858</td></tr><tr><td>Iris</td><td>150</td><td>5</td><td>3</td><td>6</td><td>0.813</td></tr><tr><td>Labor</td><td>57</td><td>17</td><td>2</td><td>4</td><td>0.689</td></tr><tr><td>Lymph</td><td>148</td><td>19</td><td>4</td><td>11</td><td>0.973</td></tr><tr><td>Sick</td><td>3,772</td><td>30</td><td>2</td><td>4</td><td>0.688</td></tr><tr><td>Sonar</td><td>208</td><td>61</td><td>2</td><td>4</td><td>0.776</td></tr><tr><td>Vote</td><td>435</td><td>17</td><td>2</td><td>5</td><td>0.808</td></tr></table>

Table 9  
Summary results from model combination.

<table><tr><td>Data set</td><td>Unweighted average (UWA)</td><td>Variance based weighting (VBW)</td><td>Efficient models only (EMO)</td><td>Efficiency score weighting (ESW)</td><td>DEA + Stacking (DST)*</td><td>Gain of DST over ESW (%)</td></tr><tr><td>Breast-w</td><td>0.033</td><td>0.027</td><td>0.027</td><td>0.03</td><td>0.0218</td><td>27.33</td></tr><tr><td>Colic</td><td>0.205</td><td>0.223</td><td>0.218</td><td>0.165</td><td>0.1232</td><td>25.33</td></tr><tr><td>Credit-a</td><td>0.155</td><td>0.149</td><td>0.215</td><td>0.139</td><td>0.1054</td><td>24.17</td></tr><tr><td>Credit-g</td><td>0.263</td><td>0.279</td><td>0.261</td><td>0.255</td><td>0.1612</td><td>36.78</td></tr><tr><td>Diabetes</td><td>0.284</td><td>0.275</td><td>0.253</td><td>0.242</td><td>0.1576</td><td>34.88</td></tr><tr><td>heart-c</td><td>0.45</td><td>0.55</td><td>0.45</td><td>0.45</td><td>0.0563</td><td>87.49</td></tr><tr><td>Heart-h</td><td>0.329</td><td>0.348</td><td>0.329</td><td>0.329</td><td>0.0562</td><td>82.92</td></tr><tr><td>Iris</td><td>0.064</td><td>0.051</td><td>0.064</td><td>0.064</td><td>0.0231</td><td>63.91</td></tr><tr><td>Labor</td><td>0.281</td><td>0.094</td><td>0.063</td><td>0.063</td><td>0.0515</td><td>18.25</td></tr><tr><td>Lymph</td><td>0.162</td><td>0.189</td><td>0.162</td><td>0.162</td><td>0.0646</td><td>60.12</td></tr><tr><td>Sick</td><td>0.018</td><td>0.014</td><td>0.036</td><td>0.017</td><td>0.01</td><td>41.18</td></tr><tr><td>Sonar</td><td>0.155</td><td>0.184</td><td>0.184</td><td>0.146</td><td>0.1009</td><td>30.89</td></tr><tr><td>Vote</td><td>0.077</td><td>0.066</td><td>0.057</td><td>0.057</td><td>0.0314</td><td>44.91</td></tr><tr><td>Mean</td><td>0.19</td><td>0.188</td><td>0.178</td><td>0.163</td><td>0.074</td><td>54.50</td></tr></table>

Notes: DST is the proposed approach. EMO and ESWare theother two DEA-based ensembles from [31]. Boldface denotes the minimum MSE of each data set across all <sup>fi</sup>ve methods.

## 5.3. Model combinations

After the base classi<sup>fi</sup>ers were selected by DEA, we then applied stacking method to combine the selected models. The results were compared with four benchmarks from known literature. These include the two methods proposed in Zheng and B. Padmanabhan [31], namely Ef<sup>fi</sup>cient Models Only (EMO) and Ef<sup>fi</sup>ciency Score Weighting (ESW). Two other common model combination methods were also included as benchmarks: unweighted-average (UWA) and popular variance-based weighting (VBW).

## 5.4. Experimental results

For each data set, a strati<sup>fi</sup>ed ten-fold cross-validation was performed. Table 9 displays the summarized results from our approach in comparison with other benchmarks based on the Mean Squared Errors (MSE). The effectiveness of this approach increases as the MSE decreases. As shown in Table 9, the leftmost column presents the data we tested and the second and third columns display the results from two simple benchmarks (UWA and VBW). The results from Zheng and Padmanabhan [31] are presented in the fourth and <sup>fi</sup>fth columns (EMO and ESW) while the results from our proposed approach are displayed in the rightmost column. From Table 9, we can see that the MSE produced by our approach is consistently smaller than those from all other approaches. The average MSE from our model combination approach, DST (short for DEA+Stacking), was reduced to 0.074, which resulted in approximately a 54.4% reduction from ESW, which is the best performing model from [31]. We can see that our approach consistently outperformed ESW, followed by EMO, VBW and UWA.

We further employed the paired t-test to determine the statistical signi<sup>fi</sup>cance of the observed differences in MSE. Table 10 displays the paired t-test across thirteen data sets and among the <sup>fi</sup>ve models evaluated at the 95% signi<sup>fi</sup>cance level. As shown in Table 10, the proposed DST approach is signi<sup>fi</sup>cantly better than all four benchmark methods.

## Table 10

Signi<sup>fi</sup>cant test results.

<table><tr><td>Method</td><td>UWA</td><td>VBW</td><td>EMO</td><td>ESW</td><td>DST</td></tr><tr><td>UWA</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td>VBW</td><td>0.45 (0.11)</td><td>-</td><td></td><td></td><td></td></tr><tr><td>EMO</td><td>0.26 (0.66)</td><td>0.18 (0.97)</td><td>-</td><td></td><td></td></tr><tr><td>ESW</td><td>0.06 (1.68)</td><td>0.005 (3.09)</td><td>0.02 (2.22)</td><td>-</td><td></td></tr><tr><td> $DST^*$ </td><td>0.002 (3.66)</td><td>0.005 (3.01)</td><td>0.003 (3.39)</td><td>0.008 (2.78)</td><td>-</td></tr></table>

Notes: DST is the proposed approach. p-values (t-values). Boldface denotes the significant p-values.

![](/api/attachments/5348YWVJ/fulltext/images/d4f25043676839a50eb0c2626731e635ad9c19ee8005ad7c09df6489e234b6bb.jpg)  
Fig. 2. Ef<sup>fi</sup>ciency count of different models from DEA selection.

In addition, the average rank for each algorithm being chosen by our approach is shown in Fig. 2. As can be seen in Fig. 2, ZeroR was selected the most frequently (13 times) with DecisionStump taking a distant second (7 times). NaiveBayes, C4.5, and support vector machine (SVM) all tied for third (6 times). Initially, this seems to be counter-intuitive as popular belief states that ZeroR is often not the best performing algorithm as an individual classi<sup>fi</sup>er. However, this result is not surprising from the DEA perspective. Based on the criteria set by the DEA selection, ZeroR always falls in the convex hall. On the other hand, from the ensemble aspect, this con<sup>fi</sup>rms that the best individual classi<sup>fi</sup>ers may not be the best choices in constructing ensembles. This is consistent with theories in current ensemble research focusing on the impact of diversity among different algorithms. That is, if classi<sup>fi</sup>cation is performed by a single classi<sup>fi</sup>er, we expect that classi<sup>fi</sup>er to have high classi<sup>fi</sup>cation accuracy. However, the classi<sup>fi</sup>cation accuracy of each individual classi<sup>fi</sup>er is not that critical in an ensemble. As long as the classi<sup>fi</sup>ers are diverse, they make uncorrelated classi<sup>fi</sup>cation errors, and each classi<sup>fi</sup>er is reasonably accurate, aggregating the predictions of the classi<sup>fi</sup>ers with the stacking method improves classi<sup>fi</sup>cation accuracy.

Additional experiments have been conducted in comparing our approach with some of the most popular ensemble data mining methods, i.e. Adaboost, Bagging and Random Forest. These methods promote diversity by presenting each base model with a different subset of training examples or different weight distributions over the examples. Decision trees make good candidates for combining as they are structurally unstable classi<sup>fi</sup>ers. In present research and software products, AdaBoost and Bagging are used almost exclusively with decision trees. In addition, research has shown that bagged ensembles improve base models with unstable learning algorithms and bagged decision trees often outperform individual decision trees [4].

## Table 11

Ensemble comparative results

<table><tr><td>Data set</td><td>AdaBoost</td><td>Bagging</td><td>Random Forest (RF)</td><td>DST</td></tr><tr><td>Breast-w</td><td>0.0554</td><td>0.0528</td><td>0.0286</td><td>0.0218</td></tr><tr><td>Colic</td><td>0.1785</td><td>0.1576</td><td>0.1176</td><td>0.1232</td></tr><tr><td>Credit-a</td><td>0.1576</td><td>0.1396</td><td>0.1118</td><td>0.1054</td></tr><tr><td>Credit-g</td><td>0.2369</td><td>0.1968</td><td>0.1788</td><td>0.1612</td></tr><tr><td>Diabetes</td><td>0.2227</td><td>0.1949</td><td>0.1831</td><td>0.1576</td></tr><tr><td>heart-c</td><td>0.0748</td><td>0.0645</td><td>0.0535</td><td>0.0563</td></tr><tr><td>Heart-h</td><td>0.0686</td><td>0.0615</td><td>0.0589</td><td>0.0562</td></tr><tr><td>Iris</td><td>0.0471</td><td>0.0535</td><td>0.0253</td><td>0.0231</td></tr><tr><td>Labor</td><td>0.1313</td><td>0.1083</td><td>0.1116</td><td>0.0515</td></tr><tr><td>Lymph</td><td>0.0929</td><td>0.0812</td><td>0.0647</td><td>0.0646</td></tr><tr><td>Sick</td><td>0.0312</td><td>0.0319</td><td>0.0135</td><td>0.01</td></tr><tr><td>Sonar</td><td>0.1894</td><td>0.1745</td><td>0.1272</td><td>0.1009</td></tr><tr><td>Vote</td><td>0.0619</td><td>0.0609</td><td>0.0372</td><td>0.0314</td></tr><tr><td>Mean</td><td>0.1191</td><td>0.106</td><td>0.086</td><td>0.074</td></tr></table>

Notes: DST is the proposed approach. Boldface denotes the minimum MSE of each data set across all four methods

Table 11 presents the MSEs from our DST approach (in the rightmost column) together with the results obtained from Adaboost, Bagging, and Random Forest. The MSEs from Adaboost and Bagging are based on the averages of each ensemble method over all individual classi<sup>fi</sup>ers. The minimum MSEs among all <sup>fi</sup>ve combination methods for each data set are highlighted. As shown in Table 11, the MSEs from our approach are smaller than the majority of those produced by Random Forest except in two cases (colic and heart-c). On average, our DST approach is slightly better than the Random Forest approach, Bagging and Boosting methods.

In summary, extensive experimental results indicated that our approach signi<sup>fi</sup>cantly outperformed the best approach proposed by Zheng and Padmanabhan [31] and other benchmark model combination methods. In addition, we also compared our approach with some of the most well known ensemble methods in literature and found our approach consistently outperformed those ensemble methods. One reason for this success is possibly due to the selection of diverse base classi<sup>fi</sup>ers from an improved DEA model. Another major reason is attributed to the powerful model combination with the stacking method.

Although the stacking algorithm has been developed for years, it is less widely used than AdaBoost and Bagging, mainly due to its dif<sup>fi</sup>culty in being analyzed theoretically [28]. In this study, the stacking method turns out to be a better approach for model combination than Zheng and Padmanabhan's ESW model, which uses linear weighting of each model based on its ef<sup>fi</sup>ciency score. Their EMO model uses majority voting among the ef<sup>fi</sup>cient models identi<sup>fi</sup>ed by DEA. It was observed that majority or plurality voting is frequently used for classi<sup>fi</sup>cation problems, a technique commonly used in Bagging. Research, however, has shown that the major disadvantage of Bagging is that it is dif<sup>fi</sup>cult to interpret, because a linear combination is always hard to explain than a single tree. It has also been shown that the effectiveness of Bagging will be reduced as the training set becomes large [7].

Instead of employing a winner-take-all approach or using a linear combination of weights, the stacking method attempts to combine the base classi<sup>fi</sup>ers non-linearly, thus producing better results. Furthermore, unlike Boosting and Bagging, stacked generalization has been found to be a better choice when combining models of different types. It has been found that stacking is effective when the distribution of the posterior probability of the classi<sup>fi</sup>er estimates with respect to all classes is used. Overall, the proposed approach allows for a more effective combination of data mining models, in addition to an ef<sup>fi</sup>cient selection through DEA. By combining the strength of DEA with the stacking method, we were able to achieve superior results.

## 6. Conclusion

In this study, we combined the strength of Data Envelopment Analysis and the stacking method to develop a new framework for constructing ef<sup>fi</sup>cient and effective ensembles. Wrapped in a distributed framework, DEA can be more ef<sup>fi</sup>ciently used in the model selection process. In addition, stacking allows for effective combination of different models. The proposed approach appears to be the best ensemble building and combination approach as indicated by outperforming all other benchmarking approaches. Furthermore, the proposed approach can be easily distributed and parallelized. As a result, we are able to more fully exploit the power of distributed processing.

Research has shown that combining the predictions of multiple classi<sup>fi</sup>ers is more accurate than any of the individual classi<sup>fi</sup>ers making up the ensemble. An ensemble is more accurate than any individual classi<sup>fi</sup>er when the classi<sup>fi</sup>ers are both accurate and diverse. One advantage of DEA-based approaches over other methods is the ability to use this approach without specifying a mathematical form for the production function. This approach can easily handle multiple inputs and outputs, with the added capability of DEA being used with any input-output measurement. Although DEA was developed to measure the ef<sup>fi</sup>ciency of multiple decision making units, it is currently only available to offer limited alternative production assumptions. As pointed out by Sueyoshi and Sekitani [24], all the DEA models suffered from an occurrence of multiple projections and multiple solutions. There is no guarantee that unique solutions can be obtained in terms of ef<sup>fi</sup>ciency measures. Different DEA models will always generate different results. For instance, the results obtained from an input-oriented BCC ef<sup>fi</sup>ciency and those from output-oriented BCC can be quite different. This difference is often very large in terms of ef<sup>fi</sup>ciency scores and other important information. Additionally, research has found that non-radial ef<sup>fi</sup>ciency measures have a higher discriminating power in evaluating the ef<sup>fi</sup>ciencies of DMUs. Therefore, it will be interesting to evaluate the impact of these different DEA models to the performance of ensemble classi<sup>fi</sup>er and <sup>fi</sup>nal decisions.

Future research will require studying the properties of DEA and its impact on ensemble selection in more detail. In particular, investigation as to whether the required number of models in terms of classes can be relaxed and the effect of using different DEA models needs further analysis. Furthermore, dynamic model integration framework could be a useful complement to our framework in enhancing the learning process [30,32]. As an extension in this area, introducing human interaction into the model selection process can also be analyzed. This would involve studying the factors and the extent to which they affect the performance of an ensemble. In these cases, the proper methodology and procedure used or developed for constructing more effective ensembles in user-friendly environments needs to be identi<sup>fi</sup>ed.

## Acknowledgment

This research is supported in part by a fund from the Information Infrastructure Institute (iCube) and a research fund from College of Business at Iowa State University. I would like to thank Mr. X. Yang and Mr. Prashant Singh for their technical assistance. I would also like to thank the editors and three anonymous reviewers. Additionally, I would like to acknowledge the help from Mr. James Hall, Mr. Abhijit Rao and Mr. Kurt Roots for their careful proofreading of the paper.

## References

[1] E. Alfaro, N. García, M. Gámez, D. Elizondo, Bankruptcy forecasting: an empirical comparison of AdaBoost and neural networks, Decision Support Systems 45 (1) (2008) 110–122.

[2] A. Asuncion, D.J. Newman, UCI Machine Learning Repository, University of California, Department of Information and Computer Science, Irvine, CA, 2007.

[3] R.D. Banker, A. Charnes, W.W. Cooper, Some models for estimating technical and scale inef<sup>fi</sup>ciencies in data envelopment analysis, Management Science 30 (9) (1984) 1078–1093.

[4] L. Breiman, Bagging Predictors, Machine Learning 24 (1996) 123–140.

[5] L. Breiman, Random forests–random features, Machine Learning 45 (1) (2001) 27

[6] W. Cooper, L. Seiford, K. Tone, Data envelopment analysis: A comprehensive text with models, applications, references and DEA-solver software, Kluwer Academic Publishers, Dordrecht, Netherlands, 2002.

[7] T. Dietterich, An experimental comparison of three methods for constructing ensembles of decision trees: bagging, boosting, and randomization, Machine Learning 40 (2000) 139–158.

[8] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy, Advances in knowledge discovery and data mining, AAAI/MIT Press, 1997.

[9] Y. Freund, Boosting a weak learning algorithm by majority, Information and Computation 121 (2) (1996) 256–285.

[10] Y. Freund, R. Schapire, Experiments with a New Boosting Algorithm, in 13th Int'l Conf. on Machine Learning, Bari, Italy, 1996

[11] J. Friedman, T. Hastie, R. Tibshirani, Additive logistic regression: a statistical view of boosting, The Annals of Statistics 28 (2) (2000) 37.

[12] M. Gashler, C. Giraud-Carrier, T. Martinez, Decision tree ensemble: small heterogeneous is better than large homogeneous, The Seventh International Conference on Machine Learning and Applications, 2008, pp. 900–905.

[13] J. Han, M. Kamber, Data Mining: Concepts and Techniques, second ed: Morgan Kaufmann, 2005.

[14] Y. Kim, W.N. Street, An intelligent system for customer targeting: a data mining approach, Decision Support Systems 37 (2) (2004) 215–228.

[15] F. Lin, H. Kuo, S. Lin, The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems, Decision Support Systems 45 (4) (2008) 795–810.

[16] M. Mannino, Y. Yang, Y. Ryu, Classi<sup>fi</sup>cation algorithm sensitivity to training data with non representative attribute noise, Decision Support Systems 46 (3) (2009) 743–751.

[17] D. Optiz, R. Maclin, Popular ensemble methods: an empirical study, Journal of Arti<sup>fi</sup>cial Intelligence Research 11 (1999) 169–198.

[18] N.C. Oza, Ensemble Data Mining Methods, in Encyclopedia of Data Warehousing and Mining, J. Wang, Editor Idea Group Reference, 2006.

[19] F. Provost, T. Fawcett, Robust classi<sup>fi</sup>cation for imprecise environments, Machine Learning 42 (2001) 203–231.

[20] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, 1993.

[21] R. Quinlan, Boosting, Bagging and C4.5, Proceedings of Thirteenth National Conference on Arti<sup>fi</sup>cial Intelligence, 1996.

[22] R. Schapire, Y. Singer, Improved boosting algorithms using con<sup>fi</sup>dence-rated predictions, Proceedings of the Eleventh Annual Conference on Computational Learning Theory, 1998.

[23] R.E. Schapire, A Brief Introduction to Boosting, Proc. 16th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 1999.

[24] T. Sueyoshi, K. Sekitani, An occurrence of multiple projections in DEA-based measurement of technical ef<sup>fi</sup>ciency: theoretical comparison among DEA models from desirable properties, European Journal of Operational Research 196 (2) (2009) 764–794.

[25] K. Ting, I. Witten, Issues in stacked generalization, Journal of Arti<sup>fi</sup>cial Intelligence Research 10 (1999) 271–289

[26] J. Wang, Encyclopedia of Data Warehousing and Mining, second ed: Information Science Reference, 2008

[27] C.-P. Wei, H.-C. Chen, T.-H. Cheng, Effective spam <sup>fi</sup>ltering: a single-class learning and ensemble approach, Decision Support Systems 45 (3) (2008) 491–503.

[28] I.H. Witten, E. Frank, Data mining: practical machine learning tools with Java implementations, second ed: Morgan Kaufmann, San Francisco, 2005.

[29] D.H. Wolpert, Stacked generalization, Neural Networks 5 (2) (1992) 241–259.

[30] Y. Yang, D. Zhu, Randomized allocation with nonparametric estimation for a multiarmed bandit problem with covariates, Annals of Statistics 30 (2002) 100–121.

[31] Z. Zheng, B. Padmanabhan, Constructing ensembles from data envelopment analysis, INFORMS Journal on Computing 19 (4) (2007) 486–496.

[32] D. Zhu, R. Padman, Connectionist approaches for solver selection in constrained project scheduling, Annals of Operations Research 72 (1997) 265–298.

Dan Zhu obtained her Ph.D. degree in Management Science and Information Systems from Carnegie Mellon University. Her current research interests are in business intelligence and decision support systems. Dr. Zhu's research has been published in the Proceedings of National Academy of Sciences, Information System Research, Decision Sciences, Naval Research Logistics, Annals of Statistics, Annals of Operations Research, Journal of Databases, Journal of Information and Software Technology, International Journal of Knowledge Management, Omega, etc. Her work has been funded by the National Science Foundation. She teaches Business Intelligence, Databases, System Analysis and Design, and Advanced Software Development courses.
