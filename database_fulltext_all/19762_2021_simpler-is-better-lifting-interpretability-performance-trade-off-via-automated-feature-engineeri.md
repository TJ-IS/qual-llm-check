---
otero_id: 19762
otero_key: "D37BPFG4"
title: "Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering"
authors: "Alicja Gosiewska; Anna Kozak; Przemysław Biecek"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113556"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering

Alicja Gosiewska <sup>a</sup>, Anna Kozak <sup>a</sup>, Przemysław Biecek <sup>a,b,\*</sup>

<sup>a</sup> Faculty of Mathematics and Information Science, Warsaw University of Technology, Koszykowa 75, 00-662 Warsaw, Poland <sup>b</sup> Faculty of Mathematics, Informatics, and Mechanics, University of Warsaw, Poland

## A R T I C L E I N F O

Keywords: Interpretability Machine learning Feature engineering Decision-making

## A B S T R A C T

Machine learning has proved to generate useful predictive models that can and should support decision makers in many areas. The availability of tools for AutoML makes it possible to quickly create an effective but complex predictive model. However, the complexity of such models is often a major obstacle in applications, especially in terms of high-stake decisions. We are experiencing a growing number of examples where the use of black boxes leads to decisions that are harmful, unfair or simply wrong. In this paper, we show that very often we can simplify complex models without compromising their performance; however, with the benefit of much needed transparency.

We propose a framework that uses elastic black boxes as supervisor models to create simpler, less opaque, yet still accurate and interpretable glass box models. The new models were created using newly engineered features extracted with the help of a supervisor model. We supply the analysis using a large-scale benchmark on several tabular data sets from the OpenML database. There are tree main results of this paper: 1) we show that extracting information from complex models may improve the performance of simpler models, 2) we question a common myth that complex predictive models outperform simpler predictive models, 3) we present a real-life application of the proposed method.

## 1. Introduction

Questions of trust in machine learning models have become crucial issues in recent years. Complex predictive models have various appli cations in different areas [1,2], in particular, they are used by financial, medical, and security institutions. Models have an impact on whether we get a loan [3], what type of treatment we receive [4], or even whether we are searched by the police [5]. The vast and rapid devel opment of machine learning methods leads to the constant improvement of the algorithms’ performance and, at the same time, increases the complexity of such methods. Algorithms are able to achieve results as good as humans or even surpass them. However, recent cases have shown that uncritical use of machine learning may cause problems. The the list of such cases spans from accidents while using surgical robots that cause minor injuries to patients [6] to problems with automated criminal justice technologies [7] or incorrect predictions of air quality [8]. Such problems lead to resistance to using complex machine learning methods even at cost of performance, especially in strictly regulated areas, such as the finance industry.

We believe that one of the major challenges is the development of Interpretable Artificial Intelligence decision support systems that over come such issues. Hence, it is important to ensure that predictions of machine learning-based decision support systems are reliable. Cynthia Rudin [9] shows that a trade-off between accuracy and interpretability is a myth and improved interpretability is not necessarily followed by reduced model performance. Moreover, interpretable models are mostly simple (for example logistic regression) and are easy to validate because of the many methods available, including statistical. However, inter pretable models may require significant effort to construct in terms of both computation and domain expertise [9]. Therefore, the potential to automate model development should also be taken into account. Considering this, we listed four requirements whose fulfillment is essential to ensure that a system is trustworthy and accessible: (1) high performance, (2) auditability, (3) interpretability, and (4) automaticity.

1. High performance means that a system rarely makes incorrect pre dictions or that the prediction error is small on average. Usually, this can be achieved by using complex, so-called black box models, such as boosting trees [10] or deep neural networks [11]. The opposite of black boxes are glass boxes. They are simple, interpretable models, such as linear regression, logistic regression, decision trees, regres sion trees and decision rules.

2. Performance ensures only a part of information about a system’s quality. Auditability guarantees that the underlying model can be verified with respect to different criteria. They are, for example, stability, fairness, and sensitivity to a concept drift. Some tools allow black box models [12] to be audited, yet simple glass boxes offer more extended range of diagnostic methods [13].

3. Interpretability has become an important topic in recent years. On the one hand, algorithms support and facilitate the decisions. On the other hand, models trained without proper supervision may cause harm [14]. Therefore, a model’s reasoning should be transparent and accessible [15]. There is an ongoing debate about the right to an explanation, what it means and how it can be achieved [16,17]. Usually, decisions of simple models are easier to understand by humans than decisions made by complex models.

4. The automaticity of machine learning methods is spreading rapidly. Due to the increasing computational power, it is becoming easier and easier to obtain more precise models, usually in an automatic manner. There are automated frameworks for AutoML like auto keras, auto-sklearn, TPOT [18–20] that make it possible to train a model even without any statistical knowledge or programming skills. Yet, machine learning specialists can also take advantage of auto mated methods of modeling. Such methods reduce the time needed to train the model so that, human effort can be directed towards more creative and sophisticated tasks than testing a wide range of parameters and models.

In this article, we introduce a framework based on the Supervised Assisted Feature Extraction for Machine Learning framework (SAFE ML). The SAFE ML framework facilitates the construction of an accurate supervisor model of any complexity, on the basis of which interpretable feature engineering can be learned. The supervisor model should be accurate in order to produce the best variable transformations, yet it does not have to be interpretable. New features can be then supervised by a domain expert. Based on the new features, the transparent glass box model is trained. In many cases, the high accuracy of black box models comes from good data representation, which can be next extracted from the model. Later, the decisions made by an interpretable model built on refined features are transparent for the end-user. We show that SAFE ML is not only a framework that provides interpretable decisions but is also able to maintain the performance of complex, opaque models.

The paper is organized as follows. Section 2 is an overview of the literature on interpretability and feature engineering. Section 3 presents the proposed SAFE ML framework, the notation, formal problem formulation, and a description of the SAFE method algorithm for feature engineering. Section 4 contains a use case of our framework on real-data and describes the results of benchmarks for the SAFE ML framework. Conclusions can be found in Section 5.

## 2. Related work

The relevant literature review is organized as follows. We first briefly survey explainable artificial methods for tabular data and interpretable Decision Support Systems. In the second part, we survey various data engineering methods.

## 2.1. Post-hoc explanations vs. interpretable models

Nowadays, legislation, for example, European General Data Protec tion Regulation (EU GDPR) gives people the right to an explanation of the algorithm’s decision that affects one’s life [21]. In 2019, an Expert Group on AI introduced Ethics Guidelines for Trustworthy Artificial Intelligence [22]. According to these guidelines, AI should, among others, respect ethical principles and values. Essentially, the above ex amples show that interpretability becomes an integral part of designing systems and algorithms.

The field of machine learning is not defenseless when it comes to interpreting predictions of models. One way to explain model behavior is post-hoc explanations. These are methods for explaining a model without any prior knowledge about its structure. A model is treated as a black box; a spectator can provide data (observations) and obtain a result (prediction) without being able to look inside. There are several approaches to explaining the global behavior of models. A black box can be reduced to simple if-then rules [23] or decision trees [24]. A partial dependence plot [25] shows how the expected value of model prediction behaves as a function of a selected variable. Another option, less computationally expensive and more robust for dependent variables, is accumulated local effects plots [26]. There are also methods for explaining the local behavior of a model, for example, around one observation. Such methods usually show the importance of variables for a particular prediction, for example, LIME [27], or contributions of variables in a particular prediction, for example, SHAP [28] and BreakDown [29].

However, these explanations are simplifications of models and may be inaccurate. What is more, to the best of our knowledge, there is a lack of a unified way to measure fidelity of explanations. As a consequence, they may be misleading or even harmful. Hence, in many applications, it is better to train a transparent, interpretable model than apply expla nations to a complex one [9,30].

In contrast to post-hoc explanations, interpretable models have a known a priori structure. The understanding of prediction comes from the construction of such algorithms that are well known and estimated parameters that are easy to interpret [31]. Examples of such models are decision trees and linear models. However, even a linear model with hundreds of coefficients and interactions may become opaque. The major challenge in building interpretable decision systems is to maintain both the interpretability and the predictive capabilities of a complex model, which are extremely important.

## 2.2. Data engineering

Data preparation and transformations are at the core of most data analyses. The quality of the algorithm is dependent not only on its complexity but also on the features engineering step. Understanding the data and comparing it to the domain knowledge is crucial in the fields of finance [32,33], insurance [34], medicine [35] and many others.

Mature areas, such as credit scoring, have established methodology for discretization that is based on domain knowledge. For example, in fraud detection, a common approach is to create new features by transforming the existing one with functions, such as minimum, maximum, mean, and standard deviation [36,37]. Gero Szepannek reviewed the existing methods for discretization in credit scoring [38]. Variables may be binned with methods based on conditional inference trees [39], maximizing AIC, BIC or the Gini coefficient of a logistic regression model [40], or binning based on $\chi ^ { 2 }$ statistic, equal width, or size of numeric variables [41]. Mostly mature, regulated areas can boast such a wide and broadly described range of methods; however, they are usually domain-based and require expert-in-the-loop.

Although several automated data transformation techniques have been developed and improved in performance, they remain timeconsuming and often worse than manual human work. As a result, years of theoretical and empirical work have gone into generating automated data transformations. Two of the most common are Principal Component Analysis or Factor Analysis [42]. More sophisticated ap proaches to automated feature engineering are based on copulas [43], iteratively generated non-linear features [44], or even training neural networks to predict the impact of transformations [45]. Yet still, newly produced features are difficult to interpret. The lack of interpretability leads to a lack of trust in model predictions. Shi et al. [46] proposed a framework to scalable interpretable feature generation and selection. Their method iteratively generates new features that come from a defined base of operations and, subsequently, features that improve the efficiency of a model are selected. The SAFE ML framework introduced in this paper is based on the idea that new features can be extracted from the complex black box model and then used to train a simple inter pretable model that often maintains the performance of the complex model. The new features reflect the non-linearities identified by a complex model and propagate them into a linear model. The main dif ference between this and the domain-based methods from the beginning of this section is to take advantage of the fact that a properly selected and trained complex model can learn the relevant relationships in the data. A credit scoring model that also enriches linear models with non linearities is a two-layer additive risk model [47]. The key concept is partitioning the features into subgroups and combining linear models for subgroups into a global model. The key advantage of the SAFE ML framework over this approach is automation for feature engineering. The transformations for the two-layer additive risk model were done with the use of domain knowledge. One can afford manual feature transformations in areas where the models are of high value. However, it is not always possible to use domain knowledge or spend much time or money on a model. In such a case, automation is essential. In addition, SAFE ML can also serve as a warm start for an expert to later analyze the variables.

## 3. SAFE ML

In this section, we describe the six-step SAFE ML framework (Fig. 1). The framework is a fully automatic process starting from raw data and ending with an interpretable model.

## 3.1. SAFE ML framework

The main idea of the SAFE ML framework is to use complex models to produce new features that are later used to fit the interpretable model. The feature engineering method is flexible and the model agnostic; any class of models may be used as a supervisor model and as a glass box model. Therefore, a supervisor model may be selected to fit the data as best as possible, while the glass box model can be selected according to the particular task or abilities of the end-users for interpreting models. We describe all 6 steps; the numbers correspond to the numbers on the diagram in Fig. 1.

Step 1 The first step is to provide a raw tabular data set. The data do not need to be preprocessed because feature engineering and feature selection will be carried out in a framework.

Step 2 The raw data is used to train a supervisor complex machine learning model. Such a model does not need to be interpretable and is treated as a black box. This can be, for example, a random forest, boosting trees, and a neural network. The purpose of this model is to extract knowledge about features in the data. Therefore, it should have a high performance to increase the probability that the supervisor model catches reliable relationships between features and predicted variable.

Step 3 The next step is to find variable transformations with the SAFE method. For continuous models (A), we use the expected prediction as a function of a variable to find changepoints that allow the best binning for the variable of interest. Point 3A contains an example transformation of a U-shape relationship between a feature and predicted values captured by a supervisor model. A simple linear model would not cap ture a U-shape relationship itself, yet such a relationship can be included in a model by providing variable transformation as shown in 3A (cate gorical variable with 3 levels marked in green). For categorical variables (B), we use clustering to merge some of the levels. The transformations are produced on training data, and then applied to both training and testing data. The details of the SAFE method are in Section 3.3.

Step 4 The new set of features includes original variables from the raw data and variables transformed with the SAFE method. The number of features is doubled, and, therefore, it could be worth performing a feature selection (but not necessarily). It can be any feature selection method, such as AIC, BIC, or a selection of k most important variables due to any measure.

Step 5 The next step is to fit a fully interpretable model on selected features. Models that can be used are, for example, logistic regression for classification problems or linear models for regression problems. Training on variables transformed by SAFE increases the chance that an interpretable model does not lose on performance when compared to the supervisor black box model. Improvement of a linear model’s perfor mance is the result of binning continuous variables, which leads to taking into account non-linear relationships between independent and target variables. Furthermore, categorical variables have fewer levels. Although SAFE does not catch high-order interactions learned by the supervisor model, SAFE transformed variables simplify the modeling of interactions between features.

Step 6 A simple model from the previous step ensures that estimated coefficients provide direct interpretation of how each variable contrib utes to the final prediction. Therefore, the end-user can use a prediction of the model followed by the explanation to support a decision.

In the following sections, we will refer to the whole process pre sented in Fig. 1 as the SAFE ML framework, whereas the SAFE method means feature engineering corresponding to steps 3–4 of Fig. 1.

![](/api/attachments/D37BPFG4/fulltext/images/8951f5d4bc8b5ede61fbab11268618f6d3ce4210224b97a3f7d0694af2bd4790.jpg)  
Fig. 1. A diagram of the SAFE ML Framework. The dotted line marks automated steps of the framework. The yellow area shows steps related to Feature Engineering steps. The green area shows steps related to human-model interaction steps. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

## 3.2. Interpretable feature transformations

The overall goal of the SAFE method is to transform original vari ables into new interpretable features. Now, we will present a formal formulation of the feature transformation problem. Let us consider a true data generating process, such as m(x), which is a true, underlying phenomenon that is creating the data $( X , Y )$ . Where X is a matrix of n rows (observations) and p columns (independent variables) and Y is a potentially stochastic vector of n response values. We consider X to be a subspace $X \subseteq \mathbb { R } ^ { p } .$ . Sometimes we will refer to X as a subset of the Cartesian product $X \subseteq X _ { 1 } \times X _ { 2 } \times \ldots \times X _ { p }$ , where $X _ { i } \subseteq \mathbb { R } ,$ , for $i = 1 , 2 , . . . , p .$ . Now, let f $: X \to \mathbb { R }$ be a black box model.

Space X is divided into aspects that will be coded separately. We are coding one variable, but also potentially multiple variables, so we define it in a more general way. $\mathbf { X } '$ is one of the coded aspects. Let $X _ { K } ^ { \prime }$ be a subset of $\mathbb { R } ^ { q _ { K } }$ for some $q _ { K }$ . We can consider vectors $x \in X$ and $\boldsymbol { x } _ { K } ^ { \prime } \in \boldsymbol { X } _ { K } ^ { \prime } .$

As the function f represents a potentially complex model, our goal is to obtain a simple model train on the basis of knowledge gained from f. To accomplish this, we use relationships between variables and model response to create transformations of variables. Transformed variables may be used to train a new simple model.

Now we can define transformer functions. Let $h _ { j } ( x ) = x _ { K _ { i } } ^ { \prime }$ , where $h _ { j }$ : $X \to X _ { K _ { i } } ^ { \prime }$ be a transformer function from space X into space $X _ { K _ { i } } .$

Let X<sup>′</sup> be a Cartesian product of sets $X _ { K _ { i } ^ { ' } \colon X ^ { \prime } } { = } X _ { K _ { 1 } ^ { ' } } \times X _ { K _ { 2 } ^ { ' } } \times \dots \times X _ { K _ { J } ^ { ' } }$ Now we can define feature transformation function $h \colon X \to X ^ { \prime } = X _ { K _ { 1 } } ^ { } ^ { \prime } \times$ $X _ { K _ { 2 } ^ { ' } } \times \ldots \times X _ { K _ { J } ^ { ' } }$

$$
h (x) = \left(h _ {1} (x), h _ {2} (x), \dots , h _ {J} (x)\right).
$$

Let us note that h could be defined on a subset of X since h do not have to include all p variables. However, we set the domain of functions h on X to keep the notation as simple as possible. Function h transforms vectors from space X into vectors in space X<sup>′</sup>.

We define a glass box model $g : x ^ { \prime } \in X ^ { \prime } \to y \in \mathbb { R }$ and $g \in G$ where G is a class of interpretable models. H is a defined class of transformations. The best glass box model is obtained by the following formulation:

$$
g = \underset {g \in G} {\operatorname{argmin}} \underset {h \in H} {\min} \mathcal {L} (g (h (x)), y)
$$

where L is some loss function, for example, accuracy, cross-entropy or root mean square error. Transformation $h _ { i }$ can be any tool for feature engineering.

We propose a novel method SAFE in which we use partial depen dence profiles and hierarchical clustering to obtain binary features that are easily interpretable. Especially when used for fitting linear models, they provide an additive interpretation of model predictions that is easy to understand.

## 3.2.1. SAFE as a data-driven feature transformation

Let us now consider transformation functions $h _ { i } ^ { S A F E } : X \to \{ 0 , 1 \} ^ { q _ { i } } ,$ such as $h _ { i } ^ { S A F E }$ , transforms values of the i-th variable into binary vectors of length $q _ { i } .$ .

If x; is a categorical variable. function $h _ { i } ^ { S A F E }$ merges some levels of $x _ { i }$ uing hierarchical clustering and finds new concatenated levels. If x is a numerical variable, function $h _ { i } ^ { S A F E }$ bins $x _ { i }$ due to the changepoints of the partial dependence profile or accumulated local effects plot. Now let us introduce the partial dependence profile [25].

Definition 3.1. Partial Dependence Profile (PDP).

Let $x _ { 1 } , x _ { 2 } , . . . , x _ { p }$ be features in the supervisor model f. A subset of all features except $x _ { i }$ we denote as $x _ { - i \cdot }$ The partial dependence profile is defined as

$$
f _ {i} (x _ {i}) = \mathbb {E} _ {x _ {- i}} [ f (x _ {i}, x _ {- i}) ]
$$

PDP is estimated as

$$
\widehat {f} _ {i} (x _ {i}) = \frac {1}{n} \sum_ {j = 1} ^ {n} f \left(x _ {i}, x _ {- i} ^ {j}\right),
$$

where n is the number of observations and x<sup>j</sup> is a value of the i-th feature for the j-th instance. The partial dependence profile describes the ex pected output condition on a selected variable. The visualization of this function is the Partial Dependence Plot [48]; an example plot is pre sented in Step 1 in Fig. 2.

A result o $: h _ { i } ^ { S A F E }$ transformation is a new space of interpretable binary representations of variables from a space X.

More sophisticated methods than PDP can be also considered, for example, accumulated local effects plots (ALE) [26]. To calculate ALE plots, we define a neighborhood as a grid of values of features. Then, changes are averaged and accumulated over the grid.

## 3.3. Description of the SAFE method algorithm

The SAFE method algorithm uses a complex model as a supervisor. New binary features are created on the basis of a supervisor’s pre dictions. These new features are used to train a simple refined model. Illustration of the SAFE method is presented in Fig. 2. In Algorithm 1, we describe how data transformations are extracted from the supervisor model, while in Algorithm 2, we show how to train a new refined model based on transformed features. The terminology used in the algorithms was introduced in Section 3.2.

The changepoint method [49] is used to identify times when the probability distribution of a time series changes. For the changepoint problem, we selected the PELT (Pruned Exact Linear Time) method. In the SAFE method, PELT is used to categorize the continuous features by binning the Partial Dependence Profile of the variable. The PELT method is based on the finding optimal partitions algorithm [50]. The contin uous variable is discretized in points of the largest variability, and the amount of changepoints is based on value of the penalty (λ parameter). According to Killick et al. [51], we denote $y _ { 1 : n } = ( y _ { 1 } , . . . , y _ { n } )$ as a sequence of data. The number of changepoints in our model as m, their positions are $\tau _ { 1 : m } = ( \tau _ { 1 } , . . . , \tau _ { m } )$ . Also, we define $\tau _ { 0 } = 0 \mathrm { a n d } \tau _ { m + 1 } = n .$ . To summarize, we split data into $m + 1$ segments. The aim of the PELT method is to minimize

$$
\sum_ {i = 1} ^ {m + 1} \left[ \mathscr {C} \left(y _ {\left(\tau_ {i - 1} + 1\right): \tau_ {i}}\right) \right] + \lambda ,
$$

where $\mathcal { C }$ is a cost function and λ is a penalty. The penalty term describes how much each additional division costs. There are many possible penalties, but we use the recommended Modified Bayes Information Criterion [52], $M B I C = 3$ ⋅ log n. The empirical results [51] show that PELT’s accuracy is higher than Binary Segmentation. Furthermore, the computation cost is the order of magnitude smaller than alternative methods.

Hierarchical clustering [53] is an algorithm that groups observations into clusters. It involves creating a hierarchy of clusters that have a predetermined ordering. Step 2 in Fig. 2 corresponds to both change point method and hierarchical clustering.

![](/api/attachments/D37BPFG4/fulltext/images/52283d55a0d0c2aadb078ddd9e774cb104fdae893d353aceb34603a00c78b453.jpg)  
Fig. 2. The SAFE method in three steps, i) Take predictions of elastic supervisor model, ii) approximate model response, iii) extract transformations and new features.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Supervised Assisted Feature Extraction
Input: data $X_{n \times p}$, supervisor model $M$, regularization penalty $\lambda$.
Start:
for $i = 1$ to $p$ do
    Let $x_i$ be $i$-th feature.
    if $x_i$ is numerical then
    Calculate the partial dependence profile $f_i(x)$ for feature $x_i$.
    Approximate $f_i(x)$ with interpretable features $x_i^*$, use the PELT method to discretize the variable with regularization penalty $\lambda_i$ (MBIC).
    Save transformation $t_i(x)$ that transforms $x_i$ into $x_i^*$.
    end if
    if $x_i$ is categorical then
    Calculate model responses for each observation with each imputed possible value of $x_i$.
    Merge levels of $f_i(x)$ with similar model responses and use the hierarchical clustering with a number of clusters $\lambda_i$.
    Save transformation $t_i(x)$ that transforms $x_i$ into $x_i^*$.
    end if
end for
Sets of transformations $T^* = \{t_1, ..., t_p\}$ may be used to create new data $X^*$ from features $x_i^* = t_i(x_i)$.
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Model Learning with Supervised Assisted Feature Extraction
Input: data  $X_{m \times p}^{new}$ , set of transformations  $T^{*}$  derived from supervisor model M.
Start:
Transform data set X into  $X^{*, new} = T^{*}(X^{new})$ .
Create transparent model  $M^{new}$  based on  $X^{*, new}$ .
</div>

## 4. Empirical study of SAFE

This Section is focused on the empirical study of SAFE. In Section 4.1, we show the use case on the example of the credit-g [54] data set. In Section 4.2 and we performed a benchmark on the selected data sets from the OpenML100 [55] database.

Values of gbm hyperparameters. Columns lower and upper are ranges, column value is a value of a hyperparameter after tuning.

<table><tr><td>Hyperparameter</td><td>Lower</td><td>Upper</td><td>Value</td></tr><tr><td>Number of trees</td><td>50</td><td>10000</td><td>5363</td></tr><tr><td>Interaction depth</td><td>1</td><td>3</td><td>3</td></tr><tr><td>Shrinkage</td><td>0.001</td><td>0.1</td><td>0.00138</td></tr></table>

## 4.1. Use case on the credit-g data

The credit-g is the German Credit data set that classifies people as good or bad credit risks. The data set was split into the train and test subsets in a 9:1 ratio. The split is defined in OpenML task 31 (split 4). The data set classifies people described by a set of attributes as good or bad credit risks.

As described in Section 3.1, Step 1 is to select a data set (credit-g) and, in Step 2, train a supervisor gbm model. We have tuned the hyperparameters on 100 replications of a random search and ranges of a hyperparameter. The selected hyperparameters are in Table 1.

According to Step 3. we extract knowledge from the tuned gbm and transform the original features from the credit-g data set. According to Algorithm 1, we used the PELT algorithm with MBIC penalty for continuous variables. In ${ \mathrm { F i g . ~ } } 3 ,$ there are example SAFE transformations calculated for the gbm model. The SAFE transformed the feature credit amount into a categorical variable with 5 levels. The average prediction for each level is non-monotonic (green lines). Therefore, new features can be used to “teach” a linear model the non-monotonic relationship. New merged levels of a variable credit history simplify the model (2 categories instead of 5) and at the same time are intuitive; lack of credits or paid credits versus existing credit or problems with payments. The SAFE method reduces the time of analysis because it automatically does feature engineering. In the domains with established expert-knowledge restrictions for merging levels or binning variables, SAFE clustering might be the initial step that eliminates the need for analyzing the data variable by variable. The black box supervisor model does the pre processing and then analysts can focus only on the important features. Confronting automatic merging with domain knowledge can improve both the performance and interpretability of the final model.

In Step 4, we selected only the transformed features and used them to train a logistic regression (Step 5). Performance and complexity of the vanilla logistic regression, supervisor gbm model, refined logistic regression on transformed features, and logistic regression on the orig inal and transformed features are in Fig. 4. The trade-off between interpretability and performance may be considered a decrease in per formance with growth in interpretability [56]. What is more, they introduced the idea of measuring interpretability of linear models and trees. According to their approach, we assess the interpretability of the models using the inverse of the number of model parameters (complexity). This measure can be applied to any model and is intuitive. More parameters mean more information to process for the human. A linear model with a few coefficients is easier to understand than one with hundreds. Similarly, a tree with several nodes can be easy to un derstand in contrast to a tree with hundreds of nodes. For linear regression models, the number of parameters is the number of the model’s coefficients, including intercept. For the gbm model from the use case, the number of parameters is the number of trees (5,363) multiplied by interaction depth $( 2 ^ { 3 } )$ , selected variables in the nodes and the threshold for them (2), and weights of two child nodes (2). In total, there are 171,616 parameters.

![](/api/attachments/D37BPFG4/fulltext/images/999aa264887425986493a4a32f66a0df33d6eae4a9bd9cb9b0a4639e129805e5.jpg)

![](/api/attachments/D37BPFG4/fulltext/images/0b6d15360afbfcf51c182951c8d8ad7a5a4d49689410db34448f3d68578b6405.jpg)

![](/api/attachments/D37BPFG4/fulltext/images/6555a74de5dba4a80296de996eeb07d2cdc97b5f183e64c2cd5449781f138016.jpg)  
Fig. 4. The interpretability-performance trade-off for models from the use case. The x-axis shows AUC on the test set, while the y-axis shows complexity of a model as the inverse of the number of parameters (complexity). The arrows illustrate interpretability-performance shifts between the supervisor gbm model, interpretable glm model on all variables and refined SAFE-based linear model. The higher value on the y-axis means better interpretability (lower number of model parameters).

In Fig. 4, the offset indicated by the arrows shows that SAFE trans formations have increased both interpretability and AUC on the test data set. The vanilla logistic regression trained on the original features has the lowest performance and has lower interpretability than the refined logistic regression trained on transformed features.

Here, AUC of vanilla logistic regression equals 0.78, while AUC of refined logistic regression equals 0.82. What is more, the number of parameters for vanilla logistic regression is 49, while for refined logistic regression it is 25. Therefore, we achieve better $\mathrm { A U C } ,$ at the same time decreasing the number of parameters. The tuned gbm supervisor model achieved AUC equals 0.80, which is slightly higher than the value for refined logistic regression, yet with the logistic model, we have gained higher interpretability. The reason for the better performance of logistic regression than gbm can be accounted for by the bias-variance trade-off [57]. It is preferable to have less complexity, and therefore reduced variance, possibly at the cost of higher bias. The gbm being a more complex model, may be overfitted.

Fig. 3. Example transformations of continuous variable, credit amount, and a categorical variable credit history. The black line on the left-hand side is a PDP profile for the credit amount variable and the segments between the red dashed lines are new features identified by the SAFE method. The green horizontal lines are average predictions for bins. The tree on the right-hand side shows merged levels of the variable credit history, i.e., no credit and all paid are merged into one level and the other three are the second level. (For interpre tation of the references to colour in this figure legend, the reader is referred to the web version of this article.)  
Coefficients of logistic regression fitted to features transformed with SAFE method based on tuned gbm model on credit-g data set. We show only features included in Fig. 3.

<table><tr><td>Variable</td><td>Estimate</td></tr><tr><td>credit_history</td><td></td></tr><tr><td>no credits/all paid</td><td>0.1765</td></tr><tr><td>all paid</td><td>0.1765</td></tr><tr><td>existing paid</td><td>0.0000</td></tr><tr><td>delayed previously</td><td>0.0000</td></tr><tr><td>critical/other existing credit</td><td>0.0000</td></tr><tr><td>credit_amount</td><td></td></tr><tr><td>(-Inf, 1308.816]</td><td>0.0000</td></tr><tr><td>(1308.816, 2572.204]</td><td>-0.0461</td></tr><tr><td>(2572.204, 3908.918]</td><td>-0.1053</td></tr><tr><td>(3908.918, 7707.041]</td><td>0.0051</td></tr><tr><td>(7707.041, Inf)</td><td>0.1216</td></tr></table>

In this case, the number of parameters decreases for the SAFE logistic regression compared to the vanilla logistic regression because of merg ing levels of categorical variables, which reduces the number of co efficients, even through binning continuous variables. SAFE aims at producing as few new features as possible, while at the same time taking into account non-linearities, hence its superiority to vanilla logistic regression.

Coefficients of the refined logistic regression are in Table 2. Refined logistic regression is fitted on new binary features, and, therefore, we can break down prediction into contributions of features in the proba bility of being in the bad class. For example, a credit amount value of (3908.918,7707.041] increases the logit of the probability by 0.0051.

## 4.2. Benchmark

We performed a benchmark on the selected data sets from the OpenML100 [55] collection of data sets for classification problems. We have selected binary classification data sets that do not contain missing values, in total 30 data sets. Each data set in the OpenML100 is linked to a task defined in the OpenML database [58]. Each task provides 10 train/test splits and a defined variable to be predicted. Some of the provided splits lead to subsets of the original data set that contain var iables with only one value. We have excluded such data sets due to technical reasons.

For each train/test split in the task we have trained 4 models: vanilla logistic regression, support vector machines on default hyperparameters (svm default), gradient boosting machines on default hyperparameters (gbm default), and tuned gradient boosting machines (gbm tuned). Hyperparameter tuning for gbm was performed on 20 randomly selected hyperparameter settings. The models’ hyperparameters and ranges for gbm tuning are in Table 3. In general, values of tuned gbm hyper parameters differ between data sets.

Table 4  
Values of default gbm, values of default svm hyperparameters, and ranges of gbm hyperparameters used for tuning.

<table><tr><td>Hyperparameter of default svm</td><td>Value</td></tr><tr><td>Kernel</td><td>Gaussian</td></tr><tr><td>C - cost of constraints violation</td><td>1</td></tr><tr><td>Hyperparameters of default gbm</td><td>Values</td></tr><tr><td>Interaction depth</td><td>1</td></tr><tr><td>Number of trees</td><td>100</td></tr><tr><td>Shrinkage</td><td>0.1</td></tr><tr><td>Bag fraction</td><td>0.5</td></tr><tr><td>Hyperparameters for gbm tunning</td><td>Ranges</td></tr><tr><td>Interaction depth</td><td>1</td></tr><tr><td>Number of trees</td><td>[50, 1000]</td></tr><tr><td>Shrinkage</td><td>[0.01, 0.6]</td></tr><tr><td>Bag fraction</td><td>[0.2, 0.7]</td></tr></table>

We used default svm, default gbm, and tuned gbm as supervisor models and applied the SAFE method to extract new features. For the changepoint penalty, we used a Modified Bayes Information Criterion [52] and continuous transformations were performed on ALE plots. On the new features, we trained a logistic regression and obtained 3 new models: SAFE gbm default, SAFE gbm tuned, SAFE svm default.

Additionally, we evaluated the models with the AUC metric. A va nilla logistic regression without any feature extraction is considered to be a baseline. Complex models such as gbm and svm are supervisors required to perform the SAFE method. Refined models are logistic re gressions trained on features extracted from the SAFE method for different supervisor models. A list of used data sets related OpenML tasks and models’ performances are in Table 4. A way to visualize perfor mances of triplets (vanilla logistic regression, supervisor model, refined SAFE model) is by plotting them in barycentric coordinates, see Fig. 5. In these plots, we can distinguish two areas related to different kinds of results.

• The left side of the plot, separated by the vertical dashed line, in cludes data sets where refined logistic regressions, on average, per formed better than vanilla logistic regressions. This corresponds to situations where extraction of information from complex models led to improving the performance of logistic regression models. The red area indicates data sets where SAFE-based logistic regression models performed better than complex supervisor models. The appearance of the data sets in the red area shows that there are situations where appropriate feature engineering leads to a simple model that ach ieves better performance than the complex model. It may be sur prising that the refined model is better than the supervisor, however, there are some reasons for that. Elastic models are better for capturing non-linear relations but at the price of larger variance for parameter estimation. In some cases, the refined models will work on better features and will have fewer parameters to train, thus it can outperform the supervisor model. This insight questions a common myth that complex machine learning models out perform linear ones.

• The right side of the plot, separated by the vertical dashed line, in cludes data sets for which the vanilla logistic regression method achieved on average better performance than SAFE. Yet, the blue area indicates the data sets where a complex supervisor model was worse than the vanilla logistic regression. Therefore, SAFE was

Mean AUC of models followed by standard deviation, calculated from 10 train/test splits defined for each data set in the OpenML database. Numbers in the first column are IDs of the tasks in OpenML, tasks include information about data set, train/test splits, and target variable. The highest values of AUC for each data set are bolded.

<table><tr><td>Dataset (OML task)</td><td>Vanilla logistic regression</td><td>gbm default</td><td>SAFE gbm default</td><td>gbm tuned</td><td>SAFE gbm tuned</td><td>svm</td><td>SAFE svm</td></tr><tr><td>credit-g (31)</td><td>0.79 + -0.04</td><td>0.78 + -0.04</td><td>0.77 + -0.04</td><td>0.78 + -0.05</td><td>0.77 + -0.03</td><td>0.79 + -0.04</td><td>0.73 + -0.05</td></tr><tr><td>diabetes (37)</td><td>0.83 + -0.06</td><td>0.83 + -0.04</td><td>0.84 + -0.04</td><td>0.84 + -0.04</td><td>0.83 + -0.04</td><td>0.83 + -0.05</td><td>0.83 + -0.04</td></tr><tr><td>spambase (43)</td><td>0.97 + -0.01</td><td>0.98 + -0.01</td><td>0.98 + -0.01</td><td>0.98 + -0.01</td><td>0.98 + -0.01</td><td>0.98 + -0.01</td><td>0.98 + -0.01</td></tr><tr><td>tic-tac-toe (49)</td><td>1.00 + -0</td><td>0.81 + -0.03</td><td>0.82 + -0.04</td><td>1.00 + -0</td><td>0.74 + -0.05</td><td>1.00 + -0</td><td>0.75 + -0.05</td></tr><tr><td>electricity (219)</td><td>0.75 + -0.08</td><td>0.86 + -0.01</td><td>0.86 + -0.01</td><td>0.92 + -0</td><td>0.86 + -0.01</td><td>0.88 + -0</td><td>0.84 + -0.01</td></tr><tr><td>scene (3485)</td><td>0.96 + -0.02</td><td>0.98 + -0.02</td><td>0.87 + -0.03</td><td>0.98 + -0.02</td><td>0.77 + -0.02</td><td>0.94 + -0.02</td><td>0.71 + -0.03</td></tr><tr><td>monks-problems-1 (3492)</td><td>0.70 + -0.07</td><td>0.69 + -0.06</td><td>0.70 + -0.06</td><td>0.72 + -0.06</td><td>0.72 + -0.08</td><td>1 + -0</td><td>0.71 + -0.08</td></tr><tr><td>monks-problems-2 (3493)</td><td>0.54 + -0.10</td><td>0.54 + -0.10</td><td>0.55 + -0.11</td><td>0.53 + -0.09</td><td>0.52 + -0.07</td><td>0.65 + -0.06</td><td>0.56 + -0.10</td></tr><tr><td>monks-problems-3 (3494)</td><td>0.99 + -0.02</td><td>0.98 + -0.03</td><td>0.99 + -0.02</td><td>0.99 + -0.02</td><td>0.99 + -0.02</td><td>0.98 + -0.03</td><td>0.99 + -0.02</td></tr><tr><td>gina_agnostic (3891)</td><td>0.79 + -0.02</td><td>0.92 + -0.02</td><td>0.78 + -0.03</td><td>0.94 + -0.02</td><td>0.80 + -0.03</td><td>0.96 + -0.01</td><td>0.80 + -0.03</td></tr><tr><td>mozilla4 (3899)</td><td>0.89 + -0.01</td><td>0.96 + -0.01</td><td>0.90 + -0.02</td><td>0.97 + -0.01</td><td>0.89 + -0.02</td><td>0.93 + -0.01</td><td>0.91 + -0.01</td></tr><tr><td>pc4 (3902)</td><td>0.92 + -0.03</td><td>0.93 + -0.02</td><td>0.89 + -0.03</td><td>0.94 + -0.02</td><td>0.89 + -0.03</td><td>0.90 + -0.02</td><td>0.84 + -0.05</td></tr><tr><td>pc3 (3903)</td><td>0.82 + -0.06</td><td>0.82 + -0.03</td><td>0.78 + -0.06</td><td>0.82 + -0.04</td><td>0.79 + -0.07</td><td>0.72 + -0.08</td><td>0.79 + -0.06</td></tr><tr><td>kc2 (3913)</td><td>0.82 + -0.12</td><td>0.85 + -0.09</td><td>0.82 + -0.09</td><td>0.84 + -0.11</td><td>0.83 + -0.11</td><td>0.78 + -0.1</td><td>0.81 + -0.12</td></tr><tr><td>kc1 (3917)</td><td>0.80 + -0.03</td><td>0.80 + -0.04</td><td>0.79 + -0.04</td><td>0.80 + -0.04</td><td>0.79 + -0.04</td><td>0.74 + -0.06</td><td>0.79 + -0.03</td></tr><tr><td>pc1 (3918)</td><td>0.81 + -0.07</td><td>0.82 + -0.06</td><td>0.80 + -0.07</td><td>0.83 + -0.06</td><td>0.81 + -0.09</td><td>0.78 + -0.05</td><td>0.80 + -0.08</td></tr><tr><td>MagicTelescope (3954)</td><td>1.00 + -0</td><td>1.00 + -0</td><td>0.99 + -0</td><td>1.00 + -0</td><td>1.00 + -0</td><td>1.00 + -0</td><td>1.00 + -0</td></tr><tr><td>wdbc (9946)</td><td>0.95 + -0.03</td><td>0.99 + -0.01</td><td>0.97 + -0.03</td><td>0.99 + -0.01</td><td>0.99 + -0.01</td><td>0.99 + -0.01</td><td>0.96 + -0.03</td></tr><tr><td>phoneme (9952)</td><td>0.81 + -0.02</td><td>0.87 + -0.01</td><td>0.87 + -0.02</td><td>0.90 + -0.01</td><td>0.88 + -0.01</td><td>0.91 + -0.01</td><td>0.86 + -0.01</td></tr><tr><td>qsar-biodeg (9957)</td><td>0.92 + -0.03</td><td>0.91 + -0.03</td><td>0.91 + -0.03</td><td>0.92 + -0.03</td><td>0.91 + -0.03</td><td>0.93 + -0.03</td><td>0.90 + -0.04</td></tr><tr><td>hill-valley (9970)</td><td>0.59 + -0.04</td><td>0.53 + -0.04</td><td>0.55 + -0.04</td><td>0.60 + -0.06</td><td>0.58 + -0.06</td><td>0.54 + -0.07</td><td>0.53 + -0.03</td></tr><tr><td>ilpd (9971)</td><td>0.75 + -0.07</td><td>0.73 + -0.06</td><td>0.73 + -0.05</td><td>0.73 + -0.05</td><td>0.73 + -0.07</td><td>0.66 + -0.08</td><td>0.73 + -0.08</td></tr><tr><td>madelon (9976)</td><td>0.59 + -0.04</td><td>0.69 + -0.03</td><td>0.63 + -0.03</td><td>0.68 + -0.03</td><td>0.63 + -0.04</td><td>0.62 + -0.04</td><td>0.53 + -0.01</td></tr><tr><td>ozone-level-8 h (9978)</td><td>0.90 + -0.04</td><td>0.89 + -0.04</td><td>0.89 + -0.04</td><td>0.90 + -0.03</td><td>0.88 + -0.04</td><td>0.90 + -0.04</td><td>0.83 + -0.04</td></tr><tr><td>climate-model-simulation-crashes (9980)</td><td>0.85 + -0.1</td><td>0.82 + -0.15</td><td>0.77 + -0.1</td><td>0.81 + -0.14</td><td>0.81 + -0.11</td><td>0.85 + -0.07</td><td>0.77 + -0.08</td></tr><tr><td>eeg-eye-state (9983)</td><td>0.68 + -0.01</td><td>0.78 + -0.01</td><td>0.77 + -0.01</td><td>0.85 + -0.01</td><td>0.79 + -0.01</td><td>0.88 + -0.03</td><td>0.77 + -0.01</td></tr><tr><td>banknote-authentication (10093)</td><td>1.00 + -0</td><td>0.99 + -0.01</td><td>0.99 + -0.01</td><td>1.00 + -0</td><td>1.00 + -0</td><td>1.00 + -0</td><td>0.99 + -0.01</td></tr><tr><td>blood-transfusion-service-center (10101)</td><td>0.75 + -0.05</td><td>0.75 + -0.05</td><td>0.74 + -0.05</td><td>0.75 + -0.05</td><td>0.74 + -0.05</td><td>0.69 + -0.05</td><td>0.71 + -0.04</td></tr><tr><td>bank-marketing (14965)</td><td>0.91 + -0.01</td><td>0.90 + -0.01</td><td>0.89 + -0.01</td><td>0.92 + -0.01</td><td>0.88 + -0.01</td><td>0.90 + -0.01</td><td>0.89 + -0.01</td></tr><tr><td>PhishingWebsites (34537)</td><td>0.99 + -0</td><td>0.98 + -0</td><td>0.98 + -0</td><td>0.99 + -0</td><td>0.98 + -0</td><td>0.99 + -0</td><td>0.98 + -0</td></tr></table>

surrogate: svm default

Decision Support Systems xxx (xxxx) xxx

![](/api/attachments/D37BPFG4/fulltext/images/a33d5a86a41813d51392920185042e948b3028004c7385abd01a2cbf9e4d5f9c.jpg)  
Fig. 5. Ternary plots of AUC measures. One dot corresponds to model performance on one data set. The position in the triangle is composed of AUC values of vanilla logistic regression, a supervisor model, and refined logistic regression. Dots in the green area are data sets for which, on average, the supervisor model was the best. Dots in the red area indicates data sets for which models refined with the SAFE method were the best, and the blue area contains dots for which vanilla logisti regression was the best. On the left side of the vertical dashed line, there are data sets for which SAFE-based logistic regression models were, on average, better than vanilla logistic regression. The area marked by more saturated colour shows a range of the dots’ possible appearance area. Dots cannot reach corner areas because their positions are calculated based on positions in AUC ranking among three models (baseline, supervisor, and refined). This means that for a split in a data set, the best model gains 2 points, the second gains 1 point, and the third gains 0 points. After averaging over 10 splits, we obtain a trinomial vector with averaged scores for three models. If the model wins on all splits, it would gain <sup>2</sup> of the total sum of points, thereby not all parts of the triangle are reachable. Models that gain <sup>2</sup> of the total sum of points lie on the one-colored edges of the hexagon. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](/api/attachments/D37BPFG4/fulltext/images/70c05dc6e27c3a9b4d95cf100bcaf2d4bac725cfbdda73e12a6e65f767e3de3e.jpg)

![](/api/attachments/D37BPFG4/fulltext/images/7dcebdee62995f3a99dd9f7c050862c69d0d2d58c7ae0d9d2538afd4e1abebc2.jpg)

![](/api/attachments/D37BPFG4/fulltext/images/2b9b6abafde096ba037873e95fe9663527fde85fdd16b63b1db6b63545a0e557.jpg)  
Fig. 6. The interpretability-performance trade-off. The beginnings of the grey arrows mark the complex supervisor models’ performances and their interpretability levels, while the arrowheads mark SAFE-based refined models’ performances and their interpretability levels. Therefore, the grey arrows illustrate interpretability performance shifts for data sets when using the SAFE ML framework. The dark blue arrows show medians, the green dashed lines are interpretability trends for supervisor models, and the red dashed lines are interpretability trends for SAFE-based refined models. The vertical offsets between these lines show that SAFE lifted the interpretability-performance trade-off. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

unable to extract the variables from the complex model that would overtake the vanilla logistic regression performance. Additionally, the appearance of data sets in the blue area show that, despite the tuning, not every gbm model was able to achieve better results than the logistic regression.

On the whole, we enriched the performance of the benchmarked models by their interpretability measures introduced in Section 4.1. For linear regression models, the number of parameters is the number of the models’ coefficients, including intercept. For svm models, the number of parameters is the number of support vectors. For gbm models, the number of parameters is the number of trees multiplied by 4. Each tree has a maximum depth that equals 1. For this reason, one parameter is the selected variable in the node, a second one is the threshold for this variable, and the last two are weights of two child nodes. The trade-off between interpretability and performance is shown in Fig. 6. Median dark blue arrows show the overall shift of the interpretability and per formance after applying the SAFE method. We used the Wilcoxon rank sum tests to check whether there are significant differences in AUC and interpretability between results of complex supervisor models and SAFEbased models. The p-values are in Table 5. Tests show that, in general, there is no significant decrease in AUC after using SAFE and there is a significant increase in interpretability.

Generally, refined SAFE-based models are simple, with a small number of parameters, which is why it may be concluded that refined models generalize data better than complex ones. However, it is worth

## Table 5

The p-values of the Wilcoxon rank sum tests for equality of AUC values and for equality of interpretability levels. All p-values for equality of AUC tests are above the significance level 0.05, so we cannot reject the hypothesis about equality of AUC. All the p-values for equality of interpretability levels are below the sig nificance level 0.05, which means that we can reject the null hypothesis in favor of the alternative hypothesis that interpretability levels are different.

<table><tr><td></td><td>gbm defaultvsSAFE</td><td>gbm tunedvsSAFE</td><td>svmvsSAFE</td></tr><tr><td> $H_0$ : AUC values are equal</td><td>0.458</td><td>0.119</td><td>0.109</td></tr><tr><td> $H_0$ : interpretability levels are equal</td><td>7.47e-13***</td><td>7.61e-20***</td><td>1.43e-13***</td></tr></table>

noting that the refined models generalize relationships that were captured by supervisor models. Thus, without a complex model as a supervisor, it would not have been possible. With the SAFE ML frame work, transferring knowledge about relationships to a simple model is automatic and does not require detailed investigation of the complex model. Even if the black box model gains better results, it is still worth considering applying the transparent glass box model. As we have seen in previous examples, the performance of the supervisor and refined models was, in general, close to each other. The advantage of a simpler model is that we gain transparency, interpretability and auditability.

## 5. Discussion

Machine learning is increasingly used to support decision-making. The availability of high computing power and large data resources fa cilitates the creation of effective but also complex and opaque models. The choice the decision makers have is to blindly trust the black box or not use them at all. To help overcome this issue, the research presented in this paper aims to use the knowledge from the complex ML model to fit an interpretable yet still accurate model, for example, based on linear regression.

In this article, we presented a novel SAFE ML framework that uses a machine learning supervisor model to automate feature trans formations. New features are then used to train the refined glass box model, for example, logistic regression.

The SAFE ML framework allows us to fulfill the four requirements of a trustworthy Decision Support System, stated in Section 1. One can choose a final refined model, according to the simplicity and trans parency, and, thus statement (3) concerning interpretability is accom plished. Simple models, such as linear regression and logistic regression, are extensively described from a mathematical point of view. As a result, there are many methods to diagnose such models. Therefore, the requirement of the (2) auditability is also fulfilled. In Section 4.2, we showed that performances of refined models are close to the perfor mance of complex supervisor models. Hence, the SAFE ML framework makes it possible to gain (1) high model performance. In Section 4.2, we also argued that the SAFE method enables automatic feature trans formation for the purpose of fitting the refined model. This approach allows you to omit the examination of a complex model. For this reason (4), automaticity is also achieved.

In Section 4.1, we showed a use case of the SAFE ML framework on a real-world data for credit scoring. The final model was a linear regres sion that is a fully interpretable model. We demonstrated that the final model achieves performance as high as a complex gbm model. The financial field is highly regulated and in many applications black box models could not be used to make decisions, in contrast to the inter pretable models, for example, models generated by our framework.

We benchmarked the SAFE ML framework as a feature engineering method on 30 data sets from OpenML repository for classification problems. The results confirmed that the SAFE algorithm produces features that can be further used to fit an accurate and transparent model. We also justified the advantage of refined models over supervisor black boxes. In general, they are more interpretable and, thus, trust worthy. The results of a benchmark show that there are data sets where appropriate feature engineering may lead to fitting a linear model that achieves equal or higher performance than complex models. These re sults confirm the value of extracting features from complex models in order to improve simple ones.

## 5.1. Future work

The SAFE method is used for transforming individual features. A natural extension of this approach could be considered for the identifi cation and extraction of interactions. In this work, the supervisor model could have any structure, as the SAFE method is model agnostic. For specific classes of supervisor models, there are methods of capturing interactions. Most common approaches are developed for tree assembles like for a random forest [59] or xgboost [60]. This can be used for extraction of new features, which contain information about in teractions between variables.

## 5.2. Software

The benchmark was performed with the R package rSAFE (https://g ithub.com/ModelOriented/rSAFE). The SAFE method is also imple mented as a Python library SafeTransformer (https://github.com/Mode lOriented/SAFE). All codes used in the benchmark and use case are in a GitHub repository https://github.com/agosiewska/SAFE-experiments.

## Acknowledgements

We would like to acknowledge Aleksandra Gacek and Piotr Lubon ´ for developing the Python library SAFE and Anna Gierlak for developing the R package rSAFE.

Alicja Gosiewska was financially supported by the grant of the Polish Centre for Research and Development POIR.01.01.0100-0328/17. Przemyslaw Biecek was financially supported by the NCN Opus grant 2017/27/B/ST6/01307.

## References

[1] M. Paliwal, U.A. Kumar, Neural networks and statistical techniques: a review ot applications. Expert Syst. Appl. 36 (1) (2009) 2–17. https://doi,org/10.1016/j. eswa.2007.10.005.

[2] K. Kourou, T.P. Exarchos, K.P. Exarchos, M.V. Karamouzis, D.I. Fotiadis, Machine learning applications in cancer prognosis and prediction, Comput. Struct. Biotechnol. J. 13 (2015) 8–17, https://doi.org/10.1016/j.csbj.2014.11.005.

[3] C.-L. Huang, M.-C. Chen, C.-J. Wang, Credit scoring with a data mining approach based on support yector machines, Expert Syst. Appl. 33 (4) (2007) 847–856 https://doi.org/10.1016/j.eswa.2006.07.007.

[4] J.A. Cruz, D.S. Wishart, Applications of Machine Learning in Cancer Prediction and Prognosis, Cancer Informatics 2, 2006, https://doi.org/10.1177 117693510600200030.

[5] S.V. Nath, Crime pattern detection using data mining, in: 2006 IEEE/WIC/ACM International Conference on Web Intelligence and Intelligent Agent Technology Workshops. 2006, pp. 41–44. https://doi,org/10.1109/wi-iatw.2006.55.

[6] H. Alemzadeh, J. Raman, N. Leveson, Z. Kalbarczyk, R.K. Iyer, Adverse events in robotic surgery: a retrospective study of 14 years of FDA data, PLoS One 11 (4) (2016) 1–20, https://doi.org/10.1371/journal.pone.0151470.

[7] R. Wexler, When a Computer Program Keeps You in Jail, The New York Times, 2017. Accessed: 2019-10-12. URL, https://www.nytimes.com/2017/06/13/opinio n/how-computers-are-harming-criminal-iustice.html

[8] M. McGough, How Bad is Sacramento’s Air, Exactly? Google Results Appear at Odds with Reality, some say, The Sacramento Bee, 2018. Accessed: 2019-10-12. URL. https://www.sacbee.com/news/california/fires/article216227775.html.

[9] C. Rudin, Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead, Nat. Mach. Intell. 1 (5) (2019) 206–215. https://doi.org/10.1038/s42256-019-0048-x

[10] T. Chen, C. Guestrin, XGBoost: A scalable tree boosting system, in: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 2016. pp. 785–794. https://doi.org/10.1145/2939672.2939785.

[11] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (2015) 436–444, https://doiorg/10.1038/nature1453

[12] A. Gosiewska, P. Biecek, auditor: an R package for model-agnostic visual validation and diagnostics, R J. 11 (2) (2019) 85–98, https://doi.org/10.32614/RJ-2019-036.

## A. Gosiewska et al.

[13] F.E. Harrell Jr., Regression Modeling Strategies: With Applications to Linear Models, Logistic and Ordinal Regression, and Survival Analysis, Springer Series in Statistics, Springer International Publishing, 2015.

[14] C. O’Neil, Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy, Crown Publishing Group, USA, 2016

[15] B. Kim, J. Park, J. Suh, Transparency and accountability in AI decision support: explaining and visualizing convolutional neural networks for text information, Decis. Support. Syst. 134 (2020) 113302, doi:j.dss.2020.113302.

[16] S. Wachter, B. Mittelstadt, C. Russell, Counterfactual explanations without opening the black box: automated decisions and the GDPR, SSRN Electron. J. (2017), https://doi.org/10.2139/ssrn.3063289.

[17] L. Edwards, M. Veale, Enslaving the algorithm: from a “right to an explanation” to a “right to better decisions”? IEEE Secur. Priv. 16 (3) (2018) 46–54, https://doi. org/10.1109/msp.2018.2701152.

[18] H. Jin, Q. Song, X. Hu, Auto-Keras: An efficient neural architecture search system, in: Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 2019, pp. 1946–1956, https://doi.org/10.1145/ 3292500.3330648.

[19] M. Feurer, A. Klein, K. Eggensperger, J. Springenberg, M. Blum, F. Hutter, Efficient and robust automated machine learning, Adv. Neural Inf. Proces. Syst. 28 (2015) 2962–2970. URL, https://papers.nips.cc/paper/5872-efficient-and-robust-aut omated-machine-learning.

[20] R.S. Olson, N. Bartley, R.J. Urbanowicz, J.H. Moore, Evaluation of a tree-based pipeline optimization tool for automating data science, in: Proceedings of the Genetic and Evolutionary Computation Conference 2016, 2016, pp. 485–492, https://doi.org/10.1145/2908812.2908918.

[21] B. Goodman, S. Flaxman, European Union regulations on algorithmic decisionmaking and a “right to explanation”, AI Mag. 38 (3) (2017) 50–57, https://doi.org 10.1609/aimag.v38i3.2741.

[22] EU Expert Group on AI, Ethics Guidelines for Trustworthy AI, Online. URL, http s://ec.europa.eu/digital-single-market/en/news/ethics-guidelines-trustworthy-ai, 2019.

[23] N. Puri, P. Gupta, P. Agarwal, S. Verma, B. Krishnamurthy, MAGIX: Model Agnostic Globally Interpretable Explanations, Seventh International Conference on Learning Representations ICLR, Debugging Machine Learning Models Workshop, URL https://debug-ml-iclr2019.github.io/cameraready/DebugML-19\_paper\_5.pdf, 2019.

[24] P. Hall, On the art and science of machine learning explanations, in: Proceedings of the JSM, Statistical Computing Section, American Statistical Association, Alexandria, VA, 2018, pp. 1781–1799.

[25] J.H. Friedman, Greedy function approximation: a gradient boosting machine, Ann. Stat, 29 (5) (2001) 1189–1232, https://doi.org/10.1214/aos/1013203451.

[26] D.W. Apley, J. Zhu, Visualizing the effects of predictor variables in black box supervised learning models, J. Roval Stat. Soc.: Ser. B (Stat. Methodol.) 82 (4) (2020) 1059–1086. https://doi.org/10.1111/rssb.12377.

[27] M.T. Ribeiro, S. Singh, C. Guestrin, “Why should i trust you?”: Explaining the predictions of any classifier, in: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016, pp. 113–1144, https://doi.org/10.1145/2939672.2939778.

[28] S.M. Lundberg, S.-I. Lee, A unified approach to interpreting model predictions, Adv. Neural Inf. Proces. Syst. 30 (2017) 4765–4774. URL, http://papers.nips.cc /paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf.

[29] M. Staniak, P. Biecek, Explanations of model predictions with live and breakdown packages, R J. 10 (2) (2018) 395–409. https://doi,org/10.32614/RJ-2018-072.

[30] S. Tan, R. Caruana, G. Hooker, Y. Lou, Distill-and-compare: Auditing black-box models using transparent model distillation, in: Proceedings of the 2018 AAAI/ ACM Conference on AI, Ethics, and Society, 2018, pp. 303–310, https://doi.org/ 10.1145/3278721.3278725.

[31] W.J. Murdoch, C. Singh, K. Kumbier, R. Abbasi-Asl, B. Yu, Definitions, methods, and applications in interpretable machine learning, Proc. Natl. Acad. Sci. 116 (44) (2019) 22071–22080, https://doi.org/10.1073/pnas.1900654116.

[32] B. Baesens, S. Hoppner, ¨ T. Verdonck, Data engineering for fraud detection, Decis. Support. Syst. (2021) 113492, https://doi.org/10.1016/j.dss.2021.113492.

[33] Y. Wu, Y. Xu, J. Li, Feature construction for fraudulent credit card cash-out detection, Decis. Support. Syst. 127 (2019) 113155, https://doi.org/10.1016/j. dss.2019.113155.

[34] Y. Wang, W. Xu, Leveraging deep learning with LDA-based text analytics to detect automobile insurance fraud, Decis, Support, Syst. 105 (2018) 87–95, doi:i

[35] S.F. da Silva, M.X. Ribeiro, do J.E.S. Batista Neto, C. Traina-Jr, A.J. Traina, Improving the ranking quality of medical image retrieval using a genetic feature selection method, Decis. Support. Syst. 51 (4) (2011) 810–820, doi:j. dss.2011.01.015.

[36] C. Whitrow, D.J. Hand. P. Juszczak. D. Weston, N.M. Adams. Transaction aggregation as a strategy for credit card fraud detection, Data Min. Knowl. Disc. 18 (1) (2008) 30–55, https://doi.org/10.1007/s10618-008-0116-z.

[37] L. Zheng, T. Chen, Optimizing deep learning workloads on ARM GPU with TVM, in: Proceedings of the 1st on Reproducible Quality-Efficient Systems Tournament on Co-Designing Pareto-Efficient Deep Learning. 2018. https://doi,org/10.1145/ 3229762.3229764.

[38] G. Szepannek, An Overview on the Landscape of R Packages for Credit Scoring, arXiv. URL. https://arxiv org/abs/2006.11835 2020

[39] T. Hothorn, K. Hornik, A. Zeileis, Unbiased recursive partitioning: a conditional inference framework, J. Comput, Graph, Stat. 15 (3) (2006) 651–674. https://doi 0rg/10.1198/106186006X133933

[40] A. Ehrhardt, C. Biernacki, V. Vandewalle, P. Heinrich, Feature Quantization for Parsimonious and Interpretable Predictive Models, arXiv, URL, https://arxiv. org/abs/1903.08920, 2019.

[41] S. Xie, scorecard: Credit Risk Scorecard, R Package Version 0.3.1, URL, ht ps://CRAN.R-project.org/package=scorecard, 2020.

[42] I.T. Jolliffe, Principal component analysis and factor analysis, Principal Comp. Anal. (1986) 115–128, https://doi.org/10.1007/978-1-4757-1904-8\_7.

[43] J.M. Kanter, K. Veeramachaneni, Deep feature synthesis: Towards automating data science endeavors, in: 2015 IEEE International Conference on Data Science and Advanced Analytics (DSAA), 2015, pp. 1–10, https://doi.org/10.1109/ DSAA.2015.7344858

[44] F. Horn, R. Pack, M. Rieger, The autofeat python library for automated featur engineering and selection, in: Joint European Conference on Machine Learning and Knowledge Discovery in Databases, 2019, pp. 111–120, https://doi.org/10.1007 978-3-030-43823-4.10

[45] F. Nargesian, H. Samulowitz, U. Khurana, E.B. Khalil, D. Turaga, Learning feature engineering for classification, in: Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, IJCAI-17, 2017, pp. 2529–2535, https://doi.org/10.24963/jicai,2017/352

[46] Q. Shi, Y.-L. Zhang, L. Li, X. Yang, M. Li, J. Zhou, SAFE: Scalable automatic feature engineering framework for industrial tasks, in: 2020 IEEE 36th International Conference on Data Engineering (ICDE), 2020, pp. 1645–1656, https://doi.org 10.1109/ICDE48307.2020.00146.

[47] C. Chen, K. Lin, C. Rudin, Y. Shaposhnik, S. Wang, T. Wang, An Interpretable Model with Globally Consistent Explanations for Credit Risk, Workshop on Challenges and Opportunities for AI in Financial Services: The Impact of Fairness, Explainability, Accuracy, and Privacy, 2018.

[48] B.M. Greenwell, pdp: an R package for constructing partial dependence plots, R J. 9 (1) (2017) 421–436, https://doi.org/10.32614/RJ-2017-016.

[49] C. Truong, L. Oudre, N. Vayatis, Selective review of offline change point detection methods, Signal Process. 167 (2020) 107299, https://doi.org/10.1016/j sigpro.2019.107299.

[50] B. Jackson, J.D. Scargle, D. Barnes, S. Arabhi, A. Alt, P. Gioumousis, E. Gwin, P. Sangtrakulcharoen, L. Tan, Tun Tao Tsai, An algorithm for optimal partitioning of data on an interval, IEEE Sig. Process. Lett. 12 (2) (2005) 105–108, https://doi. org/10.1109/LSP.2001.838216.

[51] R. Killick, P. Fearnhead, I.A. Eckley, Optimal detection of changepoints with a linear computational cost, J. Am. Stat. Assoc. 107 (2012) 1590–1598, https://doi. org/10.1080/01621459.2012.737745.

[52] N. Zhang, D. Siegmund, A modified Bayes information criterion with applications to the analysis of comparative genomic hybridization data, Biometrics 63 (2007) 22–32. https://doi.org/10.1111/i.1541-0420.2006.00662.x

[53] O. Maimon, L. Rokach, Data Mining and Knowledge Discovery Handbook, Springer-Verlag. Berlin. Heidelberg, 2005

[54] D. Dheeru, E. Karra Taniskidou, UCI Machine Learning Repository, URL, http://archive.ics.uci.edu/ml, 2017.

[55] J.N. van Rijn, B. Bischl, L. Torgo, B. Gao, V. Umaashankar, S. Fischer, P. Winter, B. Wiswedel. M.R. Berthold. J. Vanschoren. OpenML: A Collaborative Science Platform. Machine Learning and Knowledge Discovery in Databases. 2013 pp. 645–649, https://doi.org/10.1007/978-3-642-40994-3\_46.

[56] T. Mori, N. Uchihira, Balancing the trade-off between accuracy and interpretability in software defect prediction, Empir. Softw. Eng. 24 (2) (2018) 779–825, https:/ doi.org/10.1007/s10664-018-9638-1

[57] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Second ed., Springer Series in Statistics. Springer New York, 2009.

[58] J. Vanschoren, J.N. van Rijn, B. Bischl, L. Torgo, OpenML: networked science in machine learning, SIGKDD Explor. 15 (2) (2013) 49–60, https://doi.org/10.1145 2641190.2641198.

[59] A. Paluszynska, P. Biecek, randomForestExplainer: A Set of Tools to Understand what is Happening Inside a Random Forest, R Package Version 0.9, URL, http s://CRAN.R-project.org/package=randomForestExplainer, 2017.

[60] D. Foster, xgboostExplainer: An R Package that makes xgboost Models Fully Interpretable, R Package Version 0.1, URL, https://github.com/AppliedDataScie ncePartners/xgboostExplainer, 2017.

Alicia Gosiewska is a Ph.D. student in Computer Science at Warsaw University of Technology and holds a Master's degree in Mathematics, She works on an explainable artificial intelligence methods for tabular and sequential data, Her interests also include the application of Deep Learning to model protein structure prediction

Anna Kozak holds master degreee in Mathematical Statistics and Data Analysis at Warsaw University of Technology. Her interests are explainable machine learning and data visualization.

Przemyslaw Biecek works as associate professor at Warsaw University of Technology and University of Warsaw. His research interests include model exploration, explainable artificial intelligence and automated machine learning, as well as the development of statistical software. He is an active developer of the DALEX package and many other packages that support Explanatory Model Analysis (EMA).
