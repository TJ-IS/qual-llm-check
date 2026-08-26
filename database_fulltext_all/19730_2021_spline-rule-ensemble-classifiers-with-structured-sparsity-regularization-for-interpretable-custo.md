---
otero_id: 19730
otero_key: "W9F4V77F"
title: "Spline-rule ensemble classifiers with structured sparsity regularization for interpretable customer churn modeling"
authors: "Koen W. De Bock; Arno De Caigny"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113523"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spline-rule ensemble classifiers with structured sparsity regularization for interpretable customer churn modeling

Koen W. De Bock <sup>a,\*</sup>, Arno De Caigny <sup>b,c</sup>

<sup>a</sup> Audencia Business School, 8 Route de la Joneli\`ere, F-44312 Nantes, France

<sup>b</sup> IESEG School of Management, 3 Rue de la Digue, F-59000 Lille, France

<sup>c</sup> LEM-CNRS 9221, 3 Rue de la Digue, F-59000 Lille, France

## A R T I C L E I N F O

Keywords: Customer churn prediction Predictive analytics Spline-rule ensemble Interpretable data science Sparse group lasso Regularized regression

## A B S T R A C T

An important business domain that relies heavily on advanced statistical- and machine learning algorithms to support operational decision-making is customer retention management. Customer churn prediction is a crucial tool to support customer retention. It allows an early identification of customers who are at risk to abandon the company and provides the ability to gain insights into why customers are at risk. Hence, customer churn pre diction models should complement predictive performance with model insights. Inspired by their ability to reconcile strong predictive performance and interpretability, this study introduces rule ensembles and their extension, spline-rule ensembles, as a promising family of classification algorithms to the customer churn pre diction domain. Spline-rule ensembles combine the flexibility of a tree-based ensemble classifier with the simplicity of regression analysis. They do, however, neglect the relatedness between potentially conflicting model components which can introduce unnecessary complexity in the models and compromises model inter pretability. To tackle this issue, a novel algorithmic extension, spline-rule ensembles with sparse group lasso regularization (SRE-SGL) is proposed to enhance interpretability through structured regularization. Experiments on fourteen real-world customer churn data sets in different industries (i) demonstrate the superior predictive performance of spline-rule ensembles with sparse group lasso over a set well yet powerful benchmark methods in terms of AUC and top decile lift; (ii) show that spline-rule ensembles with sparse group lasso regularization significantly outperform conventional rule ensembles whilst performing at least as well as conventional splinerule ensembles; and (iii) illustrate the interpretable nature of a spline-rule ensemble model and the advantage of structured regularization in SRE-SGL. by means of a case study on customer churn prediction for a telecommu: nications company.

## 1. Introduction

An important application of data science is to drive and to support data-driven decision making. Many decision makers are convinced that the use of customer-data capabilities allows to gain an unbeatable competitive advantage [1]. Therefore, modern companies have devel oped the analytical and technological capabilities that enable collection, storage and analysis of data. An important business domain that relies heavily on advanced statistical - and machine learning algorithms to support operational decision making is customer retention management [2]. Customer churn prediction (CCP) is of crucial importance for managing customer retention as a tool to identify customers who are at risk to abandon the company and to better understand why customer are at risk [3]. In line with these managerial objectives of CCP models, previous research in CCP focused both on predictive performance (i.e. detecting who is at risk) [4,5] and interpretability (i.e. understanding why a customer is at risk) [6]. Accuracy in CCP is generally pursued due to its immediate impact on campaign profitability [7]. Model inter pretability is crucial to facilitate management buy-in and organizational acceptance, to deliver insights into the drivers of churn and loyalty and consequently, to provide venues for formulating strategies to remedy customer churn and promote loyalty [8,9].

Algorithms that combine good predictive performance and inter pretable output, such as decision trees (DT) or logistic regression (LR), are preferred in CCP [2,10]. Ensemble learners can achieve higher predictive performance, but often lack on the interpretability criterion [4]. A notable exception are rule ensembles (RE), a technique that is designed to combine the merits of ensemble learners with a high degree of interpretability [11]. Like many other ensemble learners, rule en sembles first generate a set of decision trees. However, unlike other ensemble learners, trees are decomposed into rules and only a dense set of the rules derived from these trees is retained though the application of lasso regression. The initial variables are also added to the lasso regression in the form of linear basis functions (i.e., variable trans formations) to better account for linear variable effects. Rule ensembles thus combine terms rather than member classifiers. The simple nature of the constituent terms that form the model and their selection through lasso regression result in an easily interpretable model. Recently, splinerule ensembles (SRE) are presented as an extension to rule ensembles that complement rules and linear terms with single-term spline functions in order to better accommodate univariate, nonlinear relationships be tween the dependent variable and individual explanatory variable [12].

Whilst the promise of competitive predictive performance and model interpretability has attracted attention in several domains such as bio informatics and computer science [e.g. [13,14]], applications of rule ensembles in management, and more specifically, decision support in business, remain scarce to date. In an application of corporate bank ruptcy prediction, SRE demonstrated superior performance over con ventional RE whilst the added value of the integration of spline functions was demonstrated [12]. Despite their promising traits, other applica tions of RE and SRE in business decision-making problems are very scarce and to the best of our knowledge RE and SRE have not been empirically assessed for predicting customer churn thus far. This study’s primary objective is to evaluate and compare both model architectures in the domain of CCP.

RE and SRE rely on lasso regression, which does not consider relat edness that exists between covariates. This is, nevertheless, very important to consider, because the building blocks of SRE (i.e. splines, linear base functions and rules) can share a dependence on the same variables, which can cause the model to become unnecessarily complex. Imagine for example the impact on a model’s ease of interpretation if a variable enters the model in three terms: a linear base function, a spline and a rule. In such a case, an analyst would face difficulties to assess the isolated effect of that variable on the churn probability. These issues are aggravated when conflicting parameter estimate signs emerge. To tackle these issues and significantly improve the interpretability of SRE, the second objective of this study is to propose a new algorithm entitled spline-rule ensembles with sparse group lasso regularization (SRE-SGL). SRE-SGL groups rule, spline and linear terms according to the variables upon which they depend by applying a straightforward indexing function. This term grouping is followed by sparse group lasso (SGL) regulariza tion [15] that accommodates this group structure by enforcing regula rization between as well as within term groups. As such, the cooccurrence of terms that depend on the same variable or variable set is discouraged and the complexity of the resulting model is reduced in comparison to a conventional SRE model.

The contributions of this paper are the following: (i) RE and SRE are evaluated and compared in the field of CCP and their ability to reconcile accuracy and model interpretability is assessed; and (ii) SRE-SGL, extending spline-rule ensembles with sparse group lasso regulariza tion, is introduced as a natural extension of generic RE and SRE that simplifies model interpretation. To assess and compare predictive per formance of RE, SRE and the new SRE-SGL, as well as a set of benchmark algorithms, experiments are conducted on a large set of 14 data sets containing real-world customer churn data sets in various sectors to compare RE and its extensions with a set of benchmark algorithms in terms of predictive performance. The added value offered by SRE-SGL in comparison to RE and SRE in terms of model interpretability is illus trated using an in-depth case study.

This paper is structured as follows. In the next section related research is discussed. This involves three subsections: Section 2.1 discusses the concept of interpretability in data science. Section 2.2 discusses prior literature in customer churn prediction that focusses on the trade-off between accuracy and interpretability. Section 2.3 in troduces rule-based ensemble classifiers and their applications. Section 3 presents the methodology. Section 4 handles the data and the exper imental design. The results of our large benchmark experiment and a case study to demonstrate the interpretability of SRE-SGL are discussed in section 5. The study’s conclusions, limitations and areas for future research are presented in section 6.

## 2. Related literature

## 2.1. Interpretability in data science

Interpretability is an important topic in data science and various approaches have been proposed for explaining model predictions $[ 1 6 , 1 7 ]$ . Interpretability cannot be described in a pure mathematical formula, and depends on human interpretation. Hence, interpretability can be defined as the degree to which humans can understand the cause of a decision [18,19]. As the ability to understand the cause of a decision depends on the observer, interpretability is a subjective topic. Never theless, it is an important dimension to consider for model evaluation to ensure that predictions are unbiased, sensitive information is protected, the reliability and robustness of the model is checked and that humans can trust the model [20].

Approaches to explain model predictions vary in scope and flexibility [17]. The scope indicates the level of explanations and can either be on the global or on the instance level. Global explanations give an insight in the model’s predictions over all observations and for all possible vari ables’ values. Instance-level explanations, on the other hand, are specific for a single prediction and help to understand why a certain instance received a specific prediction. Flexibility indicates whether the approach is specific to the model or model-agnostic. Flexibility is linked to the way interpretability is achieved. Intrinsic interpretable models achieve interpretability by restricting the complexity of the machine learning algorithm and their interpretability is thus often modelspecific. The model can also be analyzed after training using so called post-hoc methods, which are often model-agnostic approaches.

Our approach focuses on global, model-specific interpretability. The output of SRE-SGL is intrinsically interpretable, which allow to interpret the model’s output directly as demonstrated in the case study in section 5.2.

## 2.2. Interpretable customer churn prediction

CCP models serve a dual purpose to decision makers; detecting customers who are at risk of churning and helping to understand why customers are at risk of churning [3]. Therefore, CCP models require not only high predictive performance but also interpretable output. In this section, we review literature in the CCP domain that focuses on churn prediction modeling as tool for better decision making.

The predictive performance of CCP models is a well-researched topic because of its importance for decision makers to detect which customers are at risk of churning. There are many strategies to improve the pre dictive performance of CCP models such as intelligent data preprocess ing [21], data augmentation [22] or by the choice of algorithm [2]. Given the motivation of the focal study, we focus on the latter. Re searchers have experimented with a wide range of algorithms in extensive benchmarking studies [4]. Such studies focused on the algo rithms’ ability to discriminate between churning – and non-churning customers. Logistic regression is the standard benchmark algorithm in CCP because of its ability to produce decent and robust results [7,21,]. More complex algorithms, however, frequently perform significantly better in terms of predictive performance [2,4,22,23]. The results in large benchmarking studies demonstrate that especially ensembles, such as random forests, perform well [4]. Despite the beneficial traits in terms of predictive performance, interpretability of ensembles remains an issue which causes that they are not always the preferred option.

CCP models should be interpretable in order to assist decision maker in managing customer retention. Recent studies in CCP explicitly acknowledge the importance of interpretability of predictive models. Martens et al. [10] propose a complete framework to assess the overall performance of classification models from a user perspective in terms of accuracy, interpretability and justifiability. In their analysis, interpret ability is based on the output type and output size. They state that some output types, such as rules or linear ones, and smaller output sizes are intuitively easier to understand for humans.

A first strategy to obtain interpretable models in CCP is by making non interpretable output of so called “black-box models” more interpretable through additional analyses. On the one hand, several model-agnostic interpretation techniques exist that to reveal the magnitude and nature of the effect that variables exert on a model’s predictions. Notable ex amples are permutation-based feature importance scores, and partial dependence functions and plots. Both techniques have witnessed wide spread adoption in CCP literature. On the other hand, transparent surro gate classifiers can be created to complement, or replace, opaque models. An example of this approach is rule extraction. For example, Verbeke et al. [24] experimented with new rule induction techniques, which induce accurate as well as interpretable classification rule-sets. Farquad et al. [25] propose a hybrid approach to render interpretable rule-based output for a support vector machine model. A drawback of such methods is that they only approximate the original model. The development of inter pretable models is a second strategy. Migu´eis et al. [26] introduce multivariate adaptive regression splines (MARS [27]) to customer churn prediction and highlight its ability to uncover nonlinear effects. Cousse ment et al. [28] introduced Generalized Additive Models (GAM) as a highly interpretable model in CCP. Several extensions of GAM have been presented that improved the predictive performance while maintaining its interpretability [29–31]. Other interpretable models depend at least partly on a tree-based structure. Qi et al. [32] introduce ADTreesLogit, a model that integrates the advantage of ADTrees in the logistic regression model, to improve the predictive accuracy and interpretability of existing churn prediction models. De Caigny et al. [2] introduce the logit leaf model, a highly interpretable hybrid model based on decision trees and logistic regression that delivers actionable insights.

A final strategy involves imposing the interpretability criterion in the feature engineering. Backiel et al. [33] demonstrate how interpretable features can be extracted out of call records by using social network analysis. The use of these network features can improve the performance over local features while remaining highly interpretable. Verbraken et al. [34] stress the importance of compact networks derived from a Bayesian network classifier for the model interpretability. In the tele communication industry, Lima et al. [35] show how domain knowledge can be incorporated in the data mining process for churn prediction.

The proposed SRE-SGL fits perfectly in the interpretable customer churn prediction literature, because SRE-SGL combines excellent pre dictive performance, associated with ensemble learning, and interpret ability. The SRE-SGL algorithm has two main strategies to ensure interpretability. First, it returns inherently comprehensible output that can be directly analyzed by decision makers. Second, the model auto matically introduces new, potentially insightful features through the combination of splines, linear base functions and rules. Such features can shed new light in the understanding of what is driving customer churn. To the best of our knowledge, RE and its extensions have never been used in CCP.

## 2.3. Rule-based ensemble classifiers and applications

Ensemble classification prescribes the training of multiple base learners, or member classifiers into one model and the use of a fusion rule to aggregate their individual outputs into an overall prediction [36]. The most well-known methods differ in the strategy deployed to transform the training data set into member training data for each base learner. Examples include iterative weighing of instances in adaboost [37], bootstrap sampling in bagging [38], combining bagging and random feature selection at the node level in random forests [39], and feature extraction in rotation forests [40]. While the subject of the al gorithm choice for generating an ensemble’s base learners is widely investigated, decision trees are still the most popular and the default option in the aforementioned ensemble strategies.

This study builds on previous work that has investigated the merits of deploying decision rules as base learners in ensemble classifiers. Decision rules can be interpreted as simple classifiers that take the form of logical expressions: if [conditions] then [decision]. The earliest surfacing of rulebased ensemble learning is, to the best of our knowledge, the SLIPPER algorithm [41] that uses boosting to create an ensemble of decision rules. Subsequently, Rule ensembles were proposed by Friedman and Popescu [11][] to denote a class of ensemble learners for classification and regression that derive rules from decision trees and use them as base learners in a combination scheme based on regularized regression. A related approach was presented by Błaszczyn´ski et al. [42] and Dembc zyn´ski, Kotłowski and Słowin´ski [43] who generate rules directly and use a different loss criterion. Since then, several variations, extensions and applications of rule ensembles have been presented, for example in cancer classification [44], sensor fault classification [45], analysis of start-up performance [46] and streetscape satisfaction [47]. The proposed SRE-SGL in this study extends the approach described in [12], in which rule ensembles were applied in the field of bankruptcy prediction and an extension, spline-rule ensembles, demonstrated a significant improvement in predictive performance over conventional rule ensembles.

## 3. Methodology

## 3.1. Rule and spline-rule Ensembles

In contrast to many well-known ensemble learners that combine decision trees, RE [11][] initiates by deriving rules from decision trees and use them as base learners in a supervised, linear combination scheme. Consider a data set D with an input vector $X$ summarizing n instances on $p$ features $x _ { k } ; k = 1$ to p and an outcome vector Y. Specif ically, RE derive rules $r _ { j } ( \mathbf { x } ) ; j = 1$ to q from a set of decision trees trained on X and Y for all internal and terminal nodes within every tree (interior and terminal). A rule r (x) is the product of the indicator functions that define whether input vector x meets certain criteria defined on one or more variables:

$$
r _ {j} (x) = \prod_ {s _ {j k} \neq S _ {k}} I \left(x _ {k} \in s _ {j k}\right)\tag{1}
$$

where s represents a range or subset of values of variable $x _ { k }$ and $S _ { k }$ denotes the $f u l l$ range or set of values of this variable. Variables upon which a rule $r _ { j } ( \mathbf { x } )$ depends $( \mathrm { i . e . }$ , for which $s _ { j k } \neq S _ { k } )$ are called defining variables. The rules are complemented by linear basis functions $( x _ { k } ) ; k =$ $1 , . . . , p$ which denote variables $x _ { k }$ subsequently subjected to winsori zation and normalization as defined by:

$$
l (x _ {k}) = \frac {0 . 4 ^ {*} w i n (x _ {k})}{s d (w i n (x _ {k}))}\tag{2}
$$

with win $( x _ { k } ) =$ min $( \delta _ { k } ^ { + }$ ,max $( \delta _ { k } ^ { - } , x _ { k } ) )$ ) denoting the winsorized version of variable $x _ { k }$ and where $\delta _ { k } ^ { - }$ and δ<sup>+</sup> specify the $\beta ^ { \mathrm { { t h } } }$ and $( { \cal 1 } { - } \beta ) ^ { \mathrm { t h } }$ percentiles of $x _ { k } . ^ { 1 }$

The final model takes the form of a linear regularized lassoregression [48] applied to outcome vector Y and an intermediate term matrix T that contains values for $p + q$ terms t(x): p variable trans formations and q binary rule outcomes for all instances in a training data set.

$$
\underset {\beta} {a r g m i n} \frac {1}{2} \| y - X \beta \| _ {2} ^ {2} + \lambda \| \beta \| _ {1}\tag{3}
$$

Where shrinkage parameter λ controls sparsity: increasing values decrease the proportion of non-zero parameter estimates. $\| { \boldsymbol { \| } } _ { 2 }$ and ‖‖ are the $\ell ^ { 2 }$ and $\ell ^ { 1 }$ vector norms, respectively.

Several metrics allow an identification of the relative importance and nature of relationships of the terms selected in a rule ensemble model. The first are term coefficients, i.e. the regression parameter estimates that indicate the influence a term has upon the logit transformation of the probability to churn. These deliver insight into whether a term in fluences churn positively or negatively, and to which extent. Further more, rule support figures are specific to rule terms and indicate for which percentage of instances in the training data set a rule applies. Finally, term importance measures reflect the relative importance of the terms in the model and are obtained through

$$
T I (t) = \left\{ \begin{array}{c l} | \beta_ {t} | \sqrt {\operatorname{supp} \bigl (r _ {j} (x) \bigr) \bigl (1 - \operatorname{supp} \bigl (r _ {j} (x) \bigr) \bigr)} & \text { if   } t \text { isaruleterm }; t = r _ {j} (x) \\ | \beta_ {t} | s d (l (x _ {k})) & \text { if   } t \text { isalinearterm }; t = l (x _ {k}) \\ | \beta_ {t} | s d \bigl (s _ {g} \bigl (x _ {g} \bigr) \bigr) & \text { if   } t \text { isasplineterm }; t = s _ {g} \bigl (x _ {g} \bigr) \end{array} \right.\tag{4}
$$

where supp(r (x)) represents the rule support for rule r (x) [11]. Hence, TI(t) represents the absolute value of the regression coefficient of a standardized term t.

Due to their nature, rule ensembles balance model flexibility and interpretability, which are classifier qualities that often conflict. Model interpretability in rule ensembles stems from the process of creating simplified, easily understandable base learners, while the regularization enforces model sparsity as many terms receive a parameter estimate equal to 0. Besides linear variable effects, variable interactions are naturally accommodated through the inclusion of rules. Moreover, these rules allow an identification of non-linear effects of individual variables on an outcome variable. However, this is only possible in an indirect manner when multiple rules, defined on the same variable are selected simultaneously.

Spline-rule ensembles aim for a more direct support of non-linear ef fects. To this end, a third term class was introduced in [12]: smooth functions, and in particular penalized cubic regression splines [49] of in dividual continuous variable. Penalized cubic regression splines deter mine a set of v knots $\xi _ { 1 } , \xi _ { 2 } , . . . , \xi _ { \nu }$ over a variable’s range and estimate a function that is built up of cubic polynomials between every pair of adjacent knots. As such, they allow to model a non-linear relation be tween a variable and the customer churn probability. Specifically, s(x) (the cubic regression spline function) takes the form.

$$
s (x) = \beta_ {0} + \beta_ {1} x + \beta_ {2} x ^ {2} + \beta_ {3} x ^ {3} + \beta_ {4} h (x, \xi_ {1}) + \dots + \beta_ {\nu + 3} h (x, \xi_ {\nu})
$$

$$
\text { with } h (x, \xi) = \left\{ \begin{array}{c} (x - \xi) ^ {3} \text { if } x > \xi \\ 0 \text { otherwise } \end{array} \right.\tag{5}
$$

Minimizing

$$
\sum_ {i = 1} ^ {n} \left(y _ {i} - s (x _ {i})\right) ^ {2} - \rho \int \left(s ^ {\prime \prime} (x)\right) ^ {2} d x\tag{6}
$$

allows a determination of values for $\beta _ { 1 } , \beta _ { 2 } , . . . , \beta _ { \nu + 3 } , \xi _ { 1 } , \xi _ { 2 } , . . . , \xi _ { \nu }$ as well as ρ which represents a smoothing parameter, i.e. a penalty term that is required to penalize excessive curvature in the function.

The inclusion of penalized cubic regression spline functions s(x) for all continuous variables $x _ { 1 } , . . . , x _ { u } ( u \leq p )$ in term matrix T in Eq. (3) updates the lasso regularization that estimates the final model. Note that in [12] experiments compared lasso regularization to ridge regression and elastic net regularization by generalizing $\operatorname { E q . }$ (3). Results of a model variant comparison in the field of bankruptcy prediction [12] demon strated no significant differences. Hence, in the current study these variants are not investigated further.

## 3.2. Sparse-group lasso (SGL) regularized regression

Rule and spline-rule ensembles rely on lasso regression to perform ensemble selection and improve interpretability through shrinkage. A limitation of lasso regression is that it does not take into account relat edness (a group structure) that exists between covariates. Variations of lasso regression enable structured regularization. Specifically, the group lasso [50] and sparse-group lasso (SGL) [15] allow variable grouping. In the case of the former, sparsity is enforced on the group level so that all variables within a selected group receive non-zero parameter estimates when their group is selected and 0 otherwise. In the case of $s \mathrm { G L } ,$ a dual goal of sparsity is pursued: both at the between-group as the withingroup level. In other words, the regression attempts to shrink the model to as few group as possible, and to as few variables within selected groups as possible. The SGL takes the following form:

$$
\underset {\beta} {\operatorname{argmin}} \frac {1}{2 n} \left\| y - \sum_ {o = 1} ^ {m} T ^ {(o)} \beta^ {(o)} \right\| _ {2} ^ {2} + (1 - \alpha) \lambda \sum_ {o = 1} ^ {m} \sqrt {p _ {o}} \| \beta^ {(o)} \| _ {2} + \alpha \lambda \| \beta \| _ {1}\tag{7}
$$

In which m is the number of variable groups, $T ^ { ( o ) }$ is the partial term matrix reduced to variables that belong to group $o , p _ { o }$ is the number of variables in group $o ;$ and shrinkage is controlled by parameters λ (the shrinkage parameter) and α $( 0 \leq \alpha \leq 1 )$ , the mixing parameter that controls the trade-off between between- and within-group level regularization.

## 3.3. Spline-rule ensembles with SGL regularization (SRE-SGL)

A notable disadvantage of lasso regression is that it enforces shrinkage through a loss function that does not necessarily avoid a simultaneous selection of multiple terms that rely on the same under lying variable(s). Model interpretability becomes more challenging when a variable $x _ { k }$ enters a model simultaneously as a linear basis function l(x ), a spline $s _ { k } ( \boldsymbol { x } _ { k } )$ and a (univariate) rule r (x ). Likewise, the occurrence of similar multivariate rules that share identical defining variables complicates interpretation. These issues are aggravated when conflicting parameter estimate signs emerge. To tackle these issues and significantly improve the interpretability of spline-rule ensembles we define SRE-SGL as spline-rule ensembles with term grouping and structured regularization using SGL. SRE-SGL allows a decision maker to obtain a more interpretable model by leveraging relatedness between splines, linear basis functions and rules in term matrix T that share a dependence on the same variables.

Fig. 1 graphically depicts the core mechanisms of SRE-SGL. The training process comprises of three stages. The first stage is identical to regular spline-rule ensembles and involves the derivation of linear basis functions, tree rules and penalized cubic regression splines that will serve as candidate ensemble members. The second stage, proper to SRE-SGL, involves term grouping. This involves the grouping of terms in term matrix T according to the variables upon which they depend. Specif ically, we propose the following indexing function:

$$
t g (t (\mathrm{x} _ {s})) := w: x _ {s} = s _ {w} \in S\tag{8}
$$

Where t is a term in term matrix $T , \ \mathbf { x } _ { s }$ is the set of variables upon which t depends; S is the indexed set of unique defining term variable sets that identifies $| S | = m$ groups and $s _ { w }$ is the $w ^ { \mathrm { t h } }$ element of S. For example, a multivariate term such as a rule $r _ { \nu } ( x _ { 1 } , x _ { 3 } )$ that contains conditions on variables $x _ { 1 }$ and $x _ { 3 }$ would contribute the set $\{ x _ { 1 } , x _ { 3 } \}$ to S while univariate terms such as smoothing spline s (x ) and linear basis function $l ( x _ { 2 } )$ contributes singleton $\{ x _ { 2 } \}$ to S. $t g ( t ( \mathbf { x } _ { s } ) )$ assigns a unique grouping index to every unique set of defining variables that emerges in the terms of matrix T. This encourages the term selection to choose between alternative terms that are defined on identical variables or variable sets. In the case of univariate terms, shrinkage involves selec tion within term sets (such as $T ^ { ( 1 ) }$ and $T ^ { ( p ) }$ in Fig. 1) consisting of uni variate rules, linear basis functions, splines or any subset of these, each dependent on the same variable. In the case of multivariate terms $( \mathrm { i . e . , }$ rules with multiple conditions) this involves shrinkage within term sets (such as $T ^ { ( p + 1 ) }$ and $T ^ { ( m ) }$ in Fig. 1) consisting of rules that share the same sets of defining variables.

K.W. De Bock and A. De Caigny  
Decision Support Systems xxx (xxxx) xxx  
![](/api/attachments/W9F4V77F/fulltext/images/a82b760b75c3cef350c117d72bdbfbb3d4c73c97f2e48f618dd8522b980ba172.jpg)  
Fig. 1. Visual representation of SRE-SGL model training stages.

The final component is a logistic regression with SGL regularization applied to the grouped term matrix $\mathbf { T } ^ { \prime } = ( T ^ { ( 1 ) } , T ^ { ( 2 ) } , . . . , T ^ { ( m ) } )$ and outcome vector Y as identified by Eq. (7).

## 4. Experimental validation

## 4.1. Data sets

The experimental validation of SRE-SGL involves two dimensions: predictive accuracy and interpretability. For the former, the perfor mance of SRE-SGL is compared to a set of benchmark algorithms over fourteen real-world customer churn data sets. Table 1 presents the most important characteristics of these data sets such as the industry, number of observations, number of attributes and churn incidence. Most of the data sets are proprietary and were obtained through exclusive company collaborations which limits the level of detail that can be disclosed. Therefore, the dimension of interpretability is assessed by means of a case study on publicly available data set ds9 in Section 5.2.

## 4.2. Experimental set-up

First, to assess the predictive performance of SRE-SGL, a comparison is made to a set of seven benchmark algorithms: two closely related algorithms upon which it builds: conventional RE and SRE; and five algorithms that are characterized by a widespread adoption by practi tioners, due to both high interpretability and strong predictive perfor mance, on the one hand, and frequent adoption as benchmark algorithms in prior churn prediction literature on the other: regularized logistic regression, a CART decision tree [51], random forest [39] a generalized additive logistic regression model (GAM) [52], and, finally, a multivariate adaptive regression splines (MARS) model [27]. The regularized logistic regression models are implemented with elastic net regularization. The GAM takes the form of a semi-parametric logistic regression: a binary outcome variable is predicted using a combination of splines (for continuous variables) and linear terms (for dummy variables).

Data pre-processing can have an important impact on the predictive performance of classifiers in customer churn prediction [21]. In this study, however, the impact of different data pre-processing techniques on the predictive performance of the classifiers is not one of the research objectives. Therefore, all preprocessing steps related to handling missing values, categorical variables, outliers, class imbalance and variable se lection are equal for all algorithms and chosen in line with previous benchmark studies in CCP [2,4], which help to keep the study and presentation of results lean. First, missing values are imputed with the median and dummy variables are created to flag instances that are imputed for a certain variable [21]. Next, categorical variables are dummy-encoded into a number (the number of categories minus one) of binary variables that indicate the presence or absence of a particular characteristic. Since high cardinality does not pose an issue in our datasets, we did not rely on strategies to reduce the number of categories to a manageable size, such as coarse classification using hierarchical agglomerative clustering with Euclidian distance [4,53]. Then, outliers, defined as unusual values that are more than three standard deviations from the variable’s mean, are transformed using winsorization. Class imbalance, a result of the number of churners being much lower than the number of non-churners, is handled by undersampling the majority class, i.e. non-churning customers, to the same level as the churners [22]. Finally, Fisher score selection is applied as an input selection procedure to reduce the dimensionality of the initial feature space to twenty [4]. This is justified because a classifier often yields equal, or even better, predictive performance on a small set of highly predictive variables than on an exhaustive set of mainly redundant variables.

Data set characteristics: data set identifier, industry, number of observations, number of attributes, customer churn percentage and source.

<table><tr><td>Data set</td><td>Industry</td><td># observations</td><td># attributes</td><td>% churn</td><td>Source</td></tr><tr><td>Ds1</td><td>Financial Services</td><td>631,627</td><td>&gt;100</td><td>2.53%</td><td>European Financial Services provider</td></tr><tr><td>Ds2</td><td>Financial Services</td><td>602,575</td><td>&gt;100</td><td>3.16%</td><td>European Financial Services provider</td></tr><tr><td>Ds3</td><td>Financial Services</td><td>573,895</td><td>&gt;100</td><td>2.57%</td><td>European Financial Services provider</td></tr><tr><td>Ds4</td><td>Newspaper</td><td>427,833</td><td>&gt;100</td><td>11.14%</td><td>European newspaper company</td></tr><tr><td>Ds5</td><td>Financial Services</td><td>398,087</td><td>&gt;100</td><td>4.50%</td><td>European Financial Services provider</td></tr><tr><td>Ds6</td><td>Financial Services</td><td>316,578</td><td>&gt;100</td><td>6.45%</td><td>European Financial Services provider</td></tr><tr><td>Ds7</td><td>Financial services</td><td>117,808</td><td>&gt;100</td><td>3.55%</td><td>European Financial Services provider</td></tr><tr><td>Ds8</td><td>Financial Services</td><td>102,279</td><td>&gt;100</td><td>5.99%</td><td>European Financial Services provider</td></tr><tr><td>Ds9</td><td>Telecom</td><td>71,047</td><td>87</td><td>29.00%</td><td> $Duke^1$ </td></tr><tr><td>Ds10</td><td>Telecom</td><td>50,000</td><td>&gt;100</td><td>7.34%</td><td>European telecom operator</td></tr><tr><td>Ds11</td><td>Telecom</td><td>47,761</td><td>43</td><td>3.69%</td><td>European telecom operator</td></tr><tr><td>Ds12</td><td>Retail</td><td>32,371</td><td>47</td><td>25.15%</td><td>European supermarket retailer</td></tr><tr><td>Ds13</td><td>Energy</td><td>20,000</td><td>33</td><td>10.00%</td><td>European energy company</td></tr><tr><td>Ds14</td><td>Retail</td><td>3827</td><td>16</td><td>28.14%</td><td>European DIY retailer</td></tr></table>

<sup>1</sup> Center for Customer Relationship Management Duke University, February 2014. URL: http://www.fuqua.duke.edu/centers/ccrm

A fair comparison of classifier performance requires a strategy to tune hyperparameters whilst reducing the variability in results due to sampling. To these ends, $\textsf { a } 5 \times 3$ cross-validation experimental design, nowadays common in CCP literature $[ 2 , 2 2 , 5 4 ]$ , is deployed. This pro cedure involves a stratified split of the data set in three equal parts. In each fold, one of these data parts serves as test data sample used to determine a classifier’s predictive accuracy. The other two parts serve as training and validation data samples for training and evaluating a number of alternative classifier configurations by varying their hyper parameters. The configuration that corresponds to the best performance on the validation sample is chosen to train a final model on a stacked data sample obtained by combining the training and validation samples. Three estimates of predictive performance are thus obtained per fold, and this procedure is repeated five times. All classifiers are thus trained, validated and tested on exactly the same data samples.

Hyperparameter settings of the algorithms are optimized from broad ranges of values, similar as in previous CCP studies $[ 2 , 4 , 2 1 ]$ ]. Appendix B provides an overview of the optimized hyperparameters and their candidate values for all considered algorithms. Following the approach in [12], SRE and SRE-SGL deploy penalized cubic regression splines to estimate spline terms.<sup>2</sup> The GAM benchmark model is configured with penalized cubic regression splines with shrinkage. Note that cubic regression splines in SRE, SRE-SGL and GAM depend on smoothness parameter ρ which is internally optimized using the generalized crossvalidation (GCV) criterion [55,56] during spline estimation.

To assess the predictive performance of SRE-SGL relative to the benchmark algorithms, a statistical framework based on the nonparametric Friedman test is used as described by Demˇsar [57]. As 6 algorithms and 14 data sets are considered in the focal experiment, the Friedman statistic is defined as:

$$
\chi_ {\mathrm{F}} ^ {2} = \frac {1 2 * 1 4}{6 (6 + 1 ]} \left[ \sum_ {\mathrm{a}} \mathrm{AR} _ {\mathrm{a}} ^ {2} - \frac {6 (6 + 1) ^ {2}}{4} \right]\tag{9}
$$

where $\mathsf { A R } _ { \mathsf { a } }$ denotes the average rank of the performance measures of an algorithm $a = 1 , 2 , . . . , 6$ over our 14 data sets. The Friedman test is assumed to be distributed according to $\chi _ { F } ^ { 2 }$ with k-1 degrees of freedom under the null hypothesis that states that the results of all algorithms do not differ and thus the ranks AR<sup>2</sup> should be equal. Only if the nullhypothesis is rejected, SRE-SGL is pairwise compared with the bench mark algorithms using the Holm post-hoc test [58]. Predictive perfor mance is measured in terms of area under the receiver operating characteristic curve (AUC) and top decile lift (TDL), both commonly reported in churn prediction literature.

The second part of the experimental validation of SRE-SGL involves the dimension of interpretability, assessed through an in-depth case study on one specific data set (ds9 in Table 1). Note that for reasons of consistency, the data set is preprocessed and variables are selected as described above. However, deviating from the $5 \ \times \ 3 { \cdot } \mathrm { f o l d }$ crossvalidation deployed for comparing classifiers’ predictive performance, all models and derived insights reported in this section are based on a unique fold, i.e. a single data split of the Cell2cell data set.

Interpretability of RE, SRE and SRE-SGL models is in first instance assessed by understanding selected model terms, as well as the metrics that allow an identification of the relative importance and nature of relationships of the terms selected in a rule ensemble model presented in Section 3.1: coefficient estimates, term importance measures and rule support values for rule terms. Since model terms and regularization procedures vary between RE, SRE and SRE-SGL, substantial differences amongst resulting models can be reasonably expected. Therefore, our comparison of SRE-SGL to RE and SRE models involves two additional analyses that enable a comparison of aggregated variable importance and effects. Our aim is to verify to what extent the introduction of a more stringent SGL-regularization in SRE-SGL alters model effects in com parison to RE and SRE. First, since variables might emerge in multiple terms in (spline-) rule ensemble models and regularization does not prevent their simultaneous selection, the models’ term importance measures are insufficient First, variable importance measures VI(x ) allow to assess the relative importance of individual variables $x _ { k }$ in a model. This is usually of great importance to decision makers. They are ob tained through:

$$
V I (x _ {k}) = \sum_ {x _ {k} \in \mathrm{x} _ {j}} \frac {T I \left(t _ {j} \left(\mathrm{x} _ {j}\right)\right)}{\left| \mathrm{x} _ {j} \right|}\tag{10}
$$

which expresses the sum of term importances in which variable $x _ { k }$ occurs, each term divided by the cardinality of $x _ { \mathrm { j } } ,$ the set of variables on which it depends. Hence, higher values are awarded to variables appearing (i) more frequently and (ii) in more influential terms than others. Second, we deploy partial dependence functions to identify the aggregated effects that variables or variable pairs exert in RE, SRE and SRE-SGL models. Partial dependence functions identify the isolated ef fect of one or more variables in a predictive model F(x) by taking into account an averaged effect taken over the other variables [59]:

$$
\widehat {F} _ {s} (x _ {s}) = \frac {1}{n} \sum_ {i = 1} ^ {n} F (x _ {s}, x _ {i \backslash s})\tag{11}
$$

where $\mathbf { x } _ { s }$ is the set of variables of interest, n is, in this context, the number of customers in the data set while $\mathbf { x } _ { i \setminus s }$ represents the values of customer i for all variables not occurring in variable set $\mathbf { x } _ { s \bullet }$ When $\mathbf { x } _ { s }$ consists of one variable, the nature of the relationship between a single variable and the log odds of customer churn is revealed. Hence, partial dependence functions constitute a popular instrument to reveal variable effects in predictive customer scoring [e.g. [60]]. Our analysis reports the corresponding partial dependence plots. Moreover, when $\mathbf { x } _ { s }$ consists of multiple variables, Eq. (12) provides the basis for a quantity to analyze the presence and strength of interaction effects. Specifically, the strength of the interaction effect between variables x and x [59] can be expressed as

$$
H _ {j k} ^ {2} = \sum_ {i = 1} ^ {n} \left[ \widehat {F} _ {j k} (x _ {i j}, x _ {i k}) - \widehat {F} _ {j} (x _ {i j}) - \widehat {F} _ {k} (x _ {i k}) \right] ^ {2} / \sum_ {i = 1} ^ {n} \widehat {F} _ {j k} ^ {2} (x _ {i j}, x _ {i k})\tag{12}
$$

## 5. Results

## 5.1. Predictive performance benchmark

This section presents the results of our experiment in which the predictive performance of SRE-SGL is compared with 7 benchmark al gorithms over 14 CCP data sets originating from different industries. Appendix D presents the average cross-validated results, in terms of AUC and TDL respectively, for these fourteen data sets. The standard de viations over the different runs are indicated between brackets and the best performing algorithm is underlined for every data set.

These results serve as input to determine the average ranks of the classifiers, required for the Friedman test. Table 2 displays the average ranks for the different algorithms over the 14 data sets for both AUC and TDL. A lower average rank indicates better performance. The Friedman statistic is approximately chi-squared distributed with 7 degrees of freedom and equals 55.22 (p-value = 0.00) based on AUC ranks and 58.84 $( p \mathrm { - v a l u e } = 0 . 0 0 )$ based on TDL ranks, which indicates that there are significant differences in terms of ranks. In the post-hoc analysis, SRE-SGL serves as our control algorithm. The adjusted p-values, based on the Holm post-hoc test, are given between brackets in Table 2. SRE-SGL has the lowest rank (i.e. best predictive performance) evaluated with TDL and second-best performance based on AUC. The results indicate that SRE-SGL performs always at least as well as the best per forming algorithm in our benchmark. Compared with conventional RE and SRE, the results indicate that SRE-SGL performs significantly better

## Table 2

Average classifier ranks across data sets for different performance measures.

<table><tr><td></td><td></td><td colspan="2">Metric</td></tr><tr><td>Algorithm role</td><td>Algorithm</td><td>AUC</td><td>TDL</td></tr><tr><td>Control</td><td>Spline-rule ensemble with sparse group lasso (SRE-SGL)</td><td>2.143</td><td>1.857</td></tr><tr><td rowspan="7">Benchmarks</td><td>Decision tree (DT)</td><td>7.357***(0.000)</td><td>7.857***(0.000)</td></tr><tr><td>Regularized logistic regression (LR)</td><td>5.500***(0.002)</td><td>4.500**(0.013)</td></tr><tr><td>Random forest (RF)</td><td>3.714(0.179)</td><td>3.607(0.118)</td></tr><tr><td>Rule ensembles (RE)</td><td>4.321*(0.056)</td><td>4.643**(0.011)</td></tr><tr><td>Spline-rule ensemble (SRE)</td><td>2.036(0.908)</td><td>2.500(0.489)</td></tr><tr><td>Generalized additive model (GAM)</td><td>5.500***(0.002)</td><td>5.697***(0.000)</td></tr><tr><td>Multivariate additive regression splines (MARS)</td><td>5.429***(0.002)</td><td>5.357***(0.001)</td></tr></table>

Lower average ranks indicate better performance. The best performing algo rithm is indicated in bold.  
$^ { * * * } , ^ { * * } , ^ { * }$ Indicates significance on $9 9 \% ,$ 95%, 90% level respectively. Significant differences are indicated in italic.  
The adjusted p-value for Holm post-hoc test is shown between brackets.

than RE for both performance measures. There are no significant dif ferences between SRE-SGL and SRE, indicating that reduction in model complexity of the compact SRE-SGL model over the extensive SRE model does not negatively impact the predictive performance. In comparison to traditional benchmark algorithms in CCP (i.e. DT, LR, RF, MARS and GAM), the SRE-SGL model demonstrates superior predictive perfor mance in our benchmark study.

Results show that SRE-SGL achieves significantly better predictive performance than LR,DT, MARS and GAM in terms of AUC, and it significantly outperforms DT, LR, MARS and GAM in terms of TDL. Fig. 2 summarizes the post-hoc test results visually by means of critical dif ference plots [57] for AUC and TDL.

## 5.2. Model interpretability: A case study

In this section, the SRE-SGL model is assessed in terms of its ability to deliver model interpretability. To this end, a case study focusing on customer churn prediction in a telecom setting using the Cell2cell data set (ds9 in Table 1) is presented. This public data set is well documented and has been used in previous customer churn studies [4]. The three objectives of this case study are the following: (i) to illustrate how the spline-rule ensemble model with SGL regularization results in an inter pretable model, (ii) to demonstrate how SRE-SGL offers a higher degree of interpretability in comparison to rule ensemble and spline-rule ensemble models with lasso regularization and (iii), to analyze whether the introduction of structured regularization in SRE-SGL sub stantially changes the role of variables in the model in contrast to con ventional rule and spline-rule ensembles by investigating variable importance and isolated model variable effects. Table 3 provides an overview of the 20 selected variables through applying Fisher-score selection.

## 5.2.1. SRE-SGL model interpretation

The most direct way of gaining insights into a classifier’s functioning is an interpretation of the model itself. In contrast to alternative ho mogenous ensemble methods, rule ensembles and spline-rule ensembles deliver a facilitated model interpretability thanks to three elements: (i) the nature of candidate ensemble members (i.e., rules, linear terms and splines), (ii) their simple linear combination and (iii) the shrinkage resulting from the selection procedure to which they are submitted. SRE-SGL delivers shrinkage through sparse group lasso regularization and thus enables a more intelligent selection of competing terms through structured sparsity regularization.

![](/api/attachments/W9F4V77F/fulltext/images/621b77426c19047a57770e72f3a70423fd8c71af68d246dd699fc4b9d1395ab9.jpg)

![](/api/attachments/W9F4V77F/fulltext/images/3cba199fd3ba387e25119fb3bfb802f41707d01e2e25e7da8cd62ca915bebfce.jpg)  
(b) TDL  
Fig. 2. Critical difference plots for AUC (subplot (a)) and TDL (subplot (b)).

Table 3  
Overview of selected variables in Cell2cell data set (ds9). Descriptive statistic (mean and standard deviation) are provided for preprocessed training data.

<table><tr><td>Variable label</td><td>Definition</td><td>Mean</td><td>SD</td></tr><tr><td>callwait</td><td>Mean number of waiting calls</td><td>-0.0210</td><td>0.9759</td></tr><tr><td>changem</td><td>% change in minutes of use</td><td>-0.0168</td><td>0.9992</td></tr><tr><td>changem_M</td><td>Dummy that indicates whether changem (% change in minutes of use) is imputed</td><td>0.0071</td><td>0.0842</td></tr><tr><td>creditde</td><td>Low credit rating -de</td><td>0.1190</td><td>0.3238</td></tr><tr><td>custcare</td><td>Mean number of customer care calls</td><td>-0.0304</td><td>0.9684</td></tr><tr><td>directas</td><td>Mean number of director-assisted calls</td><td>-0.0089</td><td>0.9888</td></tr><tr><td>eqpdays</td><td>Number of days of the current equipment</td><td>0.0461</td><td>1.0045</td></tr><tr><td>incalls</td><td>Mean number of inbound voice calls</td><td>-0.0264</td><td>0.9842</td></tr><tr><td>models</td><td>Number of models issued</td><td>-0.0187</td><td>0.9849</td></tr><tr><td>mou</td><td>Mean monthly minutes of use</td><td>-0.0306</td><td>0.9838</td></tr><tr><td>mou_M</td><td>Dummy that indicates whether mou is imputed</td><td>0.0029</td><td>0.0539</td></tr><tr><td>opeakvce</td><td>Mean number of in and out off-peak voice call</td><td>-0.0244</td><td>0.9859</td></tr><tr><td>outcalls</td><td>Mean number of outbound voice calls</td><td>-0.0261</td><td>0.9844</td></tr><tr><td>phones</td><td>Number of handsets issued</td><td>-0.0198</td><td>0.9869</td></tr><tr><td>recchrge</td><td>Mean total recurring charge</td><td>-0.0335</td><td>0.9914</td></tr><tr><td>retcalls</td><td>Number of calls previously made to the retention team</td><td>0.0252</td><td>1.0596</td></tr><tr><td>revenue</td><td>Mean monthly revenue</td><td>-0.0151</td><td>0.9882</td></tr><tr><td>revenue_M</td><td>Dummy that indicates whether revenue is imputed</td><td>0.0029</td><td>0.0539</td></tr><tr><td>setprcm</td><td>Missing data on handset price</td><td>0.5742</td><td>0.4945</td></tr><tr><td>webcap</td><td>Handset is web-capable</td><td>0.8908</td><td>0.3119</td></tr></table>

Table 4 shows the selected terms of the SRE-SGL model while Fig. 3 visualizes the penalized cubic regression splines selected by the model. Table 4 also provides coefficient estimates, term importance measures and rule support values for rule terms. Values of term importance measures TI(t) are rescaled so that the most important term receives a value of 100.

The following observations emerge from Table 4. First, the model contains 21 terms: 6 rules. 7 linear terms and 8 splines. Hence, the model illustrates well how SRE-SGL is capable of revealing linear effects, nonlinear effects as well as interaction effects. Second, investigating the nature of the impact of terms on customer churn is straightforward. The 4 most important terms are univariate: linear basis functions for retcalls and revenue, and splines for changem and eqpdays. Positive linear effects exist for retcalls, revenue and changem\_M; negative ones for creditde, recchrge and webcap (in order of importance). Splines, visualized in

Table 4  
The Cell2cell SRE-SGL model: terms, term types, rule conditions, coefficients, rule support and term importance. Terms are sorted on the basis of their importance.

<table><tr><td>Term index</td><td>Type</td><td>Term or rule specification</td><td>Coefficient</td><td>Rule support</td><td>Term importance</td></tr><tr><td>1</td><td>Linear term</td><td>retcalls</td><td>0.2828</td><td>-</td><td>100</td></tr><tr><td>2</td><td>Linear term</td><td>revenue</td><td>0.1982</td><td>-</td><td>65.3561</td></tr><tr><td>3</td><td>Spline</td><td>s(changem)</td><td>0.5164</td><td>-</td><td>40.7220</td></tr><tr><td>4</td><td>Spline</td><td>s(eqpdays)</td><td>0.2917</td><td>-</td><td>32.0586</td></tr><tr><td>5</td><td>Rule</td><td>eqpdays ≥ -0.2954recchge &lt; 1.3767</td><td>0.1295</td><td>0.5529</td><td>21.4745</td></tr><tr><td>6</td><td>Rule</td><td>retcalls &lt; 2.3026eqpdays &lt; -0.2996</td><td>-0.1242</td><td>0.3901</td><td>20.2173</td></tr><tr><td>7</td><td>Linear term</td><td>creditde</td><td>-0.1805</td><td>-</td><td>19.5004</td></tr><tr><td>8</td><td>Linear term</td><td>recchge</td><td>-0.0581</td><td>-</td><td>19.2098</td></tr><tr><td>9</td><td>Rule</td><td>retcalls &lt; 2.3026eqpdays &lt; -0.2954</td><td>-0.1033</td><td>0.3918</td><td>16.8194</td></tr><tr><td>10</td><td>Spline</td><td>s(mou)</td><td>0.2993</td><td>-</td><td>13.7562</td></tr><tr><td>11</td><td>Rule</td><td>eqpdays ≥ -0.2954recchge &lt; 1.6328</td><td>0.0768</td><td>0.5640</td><td>12.7105</td></tr><tr><td>12</td><td>Rule</td><td>eqpdays ≥ -0.2954recchge &lt; 1.1742</td><td>0.0565</td><td>0.5483</td><td>9.3771</td></tr><tr><td>13</td><td>Linear term</td><td>setprcm</td><td>-0.0445</td><td>-</td><td>7.3422</td></tr><tr><td>14</td><td>Spline</td><td>s(incalls)</td><td>0.1465</td><td>-</td><td>4.5656</td></tr><tr><td>15</td><td>Linear term</td><td>changem_M</td><td>0.1578</td><td>-</td><td>4.4317</td></tr><tr><td>16</td><td>Spline</td><td>s(recchge)</td><td>0.0588</td><td>-</td><td>1.2510</td></tr><tr><td>17</td><td>Spline</td><td>s(directas)</td><td>0.0634</td><td>-</td><td>0.9684</td></tr><tr><td>18</td><td>Spline</td><td>s(callwait)</td><td>0.0470</td><td>-</td><td>0.3502</td></tr><tr><td>19</td><td>Linear term</td><td>webcap</td><td>-0.0029</td><td>-</td><td>0.3051</td></tr><tr><td>20</td><td>Spline</td><td>s(custcare)</td><td>0.0219</td><td>-</td><td>0.2444</td></tr><tr><td>21</td><td>Rule</td><td>retcalls &lt; 2.3026eqpdays &lt; -0.2913</td><td>-0.0005</td><td>0.3947</td><td>0.0868</td></tr></table>

![](/api/attachments/W9F4V77F/fulltext/images/2cfd8838341bc5f39b8af49325f3a0915f09eeb39ffd9b6987a81969da6b7840.jpg)

![](/api/attachments/W9F4V77F/fulltext/images/dca2ef937829d56c78723eb89c1834767be17b7a10a14fc4950413ed92306daf.jpg)  
eqpdays

![](/api/attachments/W9F4V77F/fulltext/images/b33163ffe273d71e0859c42d1f6f1fe4e1f17ed6b5c5b075fcb7e15853e1de08.jpg)

![](/api/attachments/W9F4V77F/fulltext/images/ed236f1da7ab9fd2e936bae89f0f9dbd9d8802936adecdc3b1e9c8b91e9387be.jpg)

![](/api/attachments/W9F4V77F/fulltext/images/cbd90b894f4942660930e7cf0fc8210059ed43426bd28265c6448793fb3514c4.jpg)

![](/api/attachments/W9F4V77F/fulltext/images/b952329d911ce62c180d69a01ed9528c531638e447b0c4f8297bca77e7ec7f69.jpg)

![](/api/attachments/W9F4V77F/fulltext/images/578b4e4805cec5a621ce02a1ad73e0550ba59fc74ac1dc43786314710357329b.jpg)  
callwait

![](/api/attachments/W9F4V77F/fulltext/images/4c818332a572683f44f05f4645de901da773485ceaae8b7705266ddb7b6f8740.jpg)  
Fig. 3. Visual representation of the eight penalized cubic regression spline terms in the Cell2cell SRE-SGL model

Fig. 3, reveal varying non-linear relationships to the probability to churn. Second, the rules reveal the existence of interaction effects. Closer inspection reveals that eqpdays interacts with two variables: recchrge and retcalls. Both are represented by three rules each, that are consistent in terms of coefficient sign and rule conditions.

## 5.2.2. SRE-SGL comparison to rule and spline-rule ensembles

Next, we wish to compare the SRE-SGL model to a conventional RE and SRE model fit to the same data set (Tables A.1 and A.2 in Appendix A, respectively). This comparison illustrates the beneficial impact of SGL regularization with regards to interpretability on multiple accounts. This comparison involves three dimensions: (i) model structure and inter pretation, (ii) variable importance and (iii) isolated variable effects.In terms of model structure and interpretation, substantial differences emerge that favor SRE-SGL in terms of interpretability. First, in terms of model size, the SGL led to a more compact model for SRE-SGL in com parison to rule and spline-rule ensemble models. Both benchmark models contain more terms: 31 and 38, respectively, versus 21 for the SRE-SGL model. Despite this large difference in model size, the predic tive performance of SRE-SGL is better than RE and similar to SRE (as shown in Table 2). Second, the absence of structured regularization in conventional lasso regularization in rule and spline-rule ensemble compromises interpretability due to the presence of conflicting rules. For example, consider the interaction effect between eqpdays and ret calls. Both the rule and spline-rule ensemble model also recognize their interaction by selection rules defined on both. However, the nature of the interaction effect is much harder to disentangle due to (i) the number of rules that capture the interaction effect (7 for RE and SRE, versus 3 in SRE-SGL), and (ii) the presence of seemingly conflicting rules. For example, consider rules that depend on the variables retcalls and eqp days. Terms 7 and 25 in the rule ensemble model: (retcalls < 2.3026 \* eapdays < –0.2996; coefficient – 0.0681) versus (retcalls > 2.3026 \* eqpdays < − 0.2913; coefficient 0.0414). Such problems also emerge in the SRE model, and for the interaction between recchrge and retcalls. While in the SRE-SGL model, the sparse group lasso did not prevent a selection of multiple rules defined on both pairs of variables, within group level shrinkage resulted in a more stringent selection of consis tent rules. Third, the SRE model shows how in the absence of structured regularization, univariate terms can also cause conflicts and jeopardize model interpretability. For example: changem and recchrge occur both as a linear term and as a spline in the model. Eqpdays occurs as a spline, and in 8 univarate rules with varying coefficient signs. These problems are lifted in the SRE-SGL model. The exception is the double occurrence of recchrge, which shows that the introduction of within-group shrinkage in SGL is not absolute.

A second comparison analyses the importance of individual variables in the models. Fig. 4 presents variable importance measures for all variables in the SRE-SGL, SRE and RE models, rescaled so that the most important variable receives a score of 100. These results show consis tency between SRE-SGL, SRE and RE models, despite their differing model structures. In total, 14 variables appear in the SRE-SGL and SRE models, while there are 10 in the RE model. SRE-SGL, SRE and RE agree on the five most important variables (with an importance level above 20) are retcalls, eqpdays, revenue, changem and recchrge. These are the variables that dominate both as univariate terms, and in multiple multivariate rules in the model.

A third dimension on which SRE-SGL is compared to SRE and RE is the analysis of isolated variables effects. Our intention is to analyze whether the introduction of structured regularization in SRE-SGL sub stantially alters the nature of the effects found in regular SRE and RE models. To this end, the isolated variable effects are visualized in Fig. 5 that shows the corresponding partial dependence plots for the variable in the model, ordered by importance (defined in Fig. 4) for SRE-SGL, SRE and RE models.

![](/api/attachments/W9F4V77F/fulltext/images/59e40e5cb2ba473d7faeb73383a8df933c2673d47e2795bb3d021652c824af37.jpg)  
Fig. 4. Cell2cell SRE-SGL, SRE and RE model variable importances.

A comparison of these dependence plots leads to the following ob servations. First, effects in the SRE-SGL and SRE models are highly similar. This provides evidence that the altered model structure due to the introduction of structured regularization does in fact not substan tially alter the isolated effects of individual variables. The enforcing of a grouping structure on model terms in SGL leads to a model that is easier to understand, yet is similar in its functioning. Second, these plots highlight the added value of adding spline functions to rules and linear basis functions for churn prediction. Non-linear effects that revealed in SRE and SRE-SGL models are either not incorporated (e.g. mou, directas). or substituted by a linear effect (e.g. changem, incalls) or a piecewise linear effect (eqpdays) in the RE model. Note that such a piecewise linear function requires multiple rules to be simultaneously present in the model (as demonstrated by the many rules defined on eqpdays in the RE model in Table A.1). Third, it is useful to compare these partial depen dence visualizations with the SRE-SGL model described earlier. The selected linear and spline terms can be easily recognized, the partial dependence function for the variable eqpdays is a composite of the spline term and the rules that feature the variable while the piecewise linear plots for retcalls and recchrge summarize the linear effects and rules in which they emerge.

An alternative use of partial dependence functions is the analysis of variable interactions. An analysis of the interaction effects in the SRE-SGL model is available in Appendix E.

## 6. Conclusions, limitations and directions for future research

Customer churn prediction is an important instrument in companies retention management strategies. Such models ought to be as accurate as possible albeit not at the expense of decreased interpretability. Ensemble methods have been gaining critical acclaim since many years, mostly due to their association to strong predictive accuracy. However, in contexts where decision makers attribute high value to interpretability, their black-box nature compromises their potential deployment. RE and SRE constitute a family of classifiers tailored to reconcile these seem ingly conflicting objectives. Based on rules extracted from decision trees, spline terms and simple linear terms, they offer increased flexibility over other established methods that are easy to understand, such as decision trees or logistic regression. Yet, this increased model complexity, that could be seen as the cost of this increased flexibility, is very limited thanks to regularization, i.e. the shrinkage of the full set of candidate model terms.

Since rules, splines and linear terms are essentially based on the same set of variables, interpretation of a rule- or a spline-rule ensemble model could become less straightforward when regularization shrinkage does not prevent such terms from being selected simultaneously. To remedy this, we propose SRE-SGL, spline-rule ensembles with structure regula rization through sparse group lasso regularization. We define a straightforward indexing function to group terms when they share the same set of defining variables. Through sparse group lasso regulariza tion, term selection is driven by shrinkage at two levels: the betweengroup level and the within-group level. SRE-SGL aims for accurate models that consist of as few terms of as few variable groups as possible. Extensive experiments on a large set of churn prediction data sets confirm the highly competitive nature of SRE-SGL in terms of two di mensions it aims to reconcile: predictive accuracy and interpretability. Specifically, results demonstrate how SRE-SGL outperforms a decision tree, logistic regression, GAM, MARS and a random forest model on most datasets. It also consistently outperforms conventional RE models, and the introduction of structured regularization does not result in a disad vantage over standard SRE. Model interpretability of SRE-SGL was assessed in detail and compared to RE and SRE by means of a case study, investigating churn prediction in the setting of a telecommunications company. An analysis by means of variable importance measures and partial dependence functions demonstrates that the effects captured by SRE-SGL are highly similar to those found in the RE and SRE models. However, the SRE-SGL model is simpler in nature and its interpret ability, unlike conventional RE and SRE models, is not compromised by inconsistent or conflicting model terms or term effects based on the same variables.

The contributions of this study are thus the following: (i) we intro duce spline-rule ensembles to the field of customer churn prediction and demonstrate their ability to deliver insightful yet accurate models; (ii) we propose SRE-SGL as an extension to spline-rule ensembles that re tains the qualities of spline-rule ensembles yet avoids the pitfall of reduced model interpretability due to conflicting model term selection,

![](/api/attachments/W9F4V77F/fulltext/images/e1bf744b5dd38a142cd25abc4dcdd6c1e3406bfc229a87bd0f351e14d1a0679e.jpg)  
Fig. 5. Partial dependence plots for selected variables: a comparison of the SRE-SGL, SRE and RE Cell2cell models.

(iii) an extensive benchmark study is conducted to determine how SRE-SGL performs in comparison to well-established competing algorithms balancing accuracy and interpretability, and (iv) a case study is con ducted to illustrate how SRE-SGL avoids the issues described above and achieves a higher degree of interpretability in comparison to conven tional rule and spline-rule ensembles.

Note that a number of limitations of this study could be identified. First, our experimental comparison evaluated two well-known metrics

for assessing classifier performance in the domain of CCP with a wide spread adoption and recognition in practice: top-decile lift and AUC. Recently, promising metrics that integrate cost and profit consideration in their evaluation gained popularity in the domain, such as the ex pected maximum profit criterion [61]. Future research should evaluate SRE-SGL on the basis of such metrics, and we intend to extend SRE-SGL so that these metrics guide decision tree training as well as regulariza tion. Second, this study is exclusively focused on customer churn pre diction which is one of the most established applications in the broader field of marketing analytics. Future research should explore the viability of SRE-SGL for other tasks. Third, regularized regression is one strategy for reducing a large set of terms and combining them. Other strategies that are common for the practice of ensemble selection of ensemble pruning such as optimization, could also be deployed for term selection as well as integrating variable group selectivity. Fourth, SRE-SGL, like RE and SRE, involves the initial creation of a large set of rules and terms and sometimes overly complex rules can still be retained in the final model. Follow-up research should explore strategies for the definition of preliminary term filters that enforce a priori selection. This could be a viable option to further constrain models in pursuit of enhanced model interpretability. Finally, data preprocessing practices such as feature selection, class imbalance and outlier treatment are known to impact results. While this study based its experimental set-up on prior litera ture, future research could revisit the impact of such practices on the novel algorithms presented in this study.

## Appendix A. Cell2cell rule ensemble and spline-rule ensemble models

The Cell2cell rule ensemble model: terms, term types, rule conditions, rule support and term importance. Terms are sorted by their importance.

<table><tr><td>Term</td><td>Type</td><td>Term or rule specification</td><td>Coefficient</td><td>Rule support</td><td>Term importance</td></tr><tr><td>1</td><td>Linear term</td><td>retcalls</td><td>0.1666</td><td>-</td><td>100</td></tr><tr><td>2</td><td>Linear term</td><td>changem</td><td>-0.1095</td><td>-</td><td>61.9698</td></tr><tr><td>3</td><td>Linear term</td><td>revenue</td><td>0.0920</td><td>-</td><td>51.4809</td></tr><tr><td>4</td><td>Linear term</td><td>recchrge</td><td>-0.0544</td><td>-</td><td>30.5365</td></tr><tr><td>5</td><td>Rule</td><td>recchrge &lt; 1.3767</td><td>0.0726</td><td>0.5529</td><td>20.4608</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.2954</td><td></td><td></td><td></td></tr><tr><td>6</td><td>Rule</td><td>recchrge &lt; 1.1742</td><td>0.0679</td><td>0.5483</td><td>19.1421</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.2954</td><td></td><td></td><td></td></tr><tr><td>7</td><td>Rule</td><td>retcalls &lt; 2.3026</td><td>-0.0681</td><td>0.3901</td><td>18.8075</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2996</td><td></td><td></td><td></td></tr><tr><td>8</td><td>Linear term</td><td>creditde</td><td>-0.1001</td><td>-</td><td>18.3641</td></tr><tr><td>9</td><td>Rule</td><td>retcalls &lt; 2.3026</td><td>-0.0664</td><td>0.3918</td><td>18.3578</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2954</td><td></td><td></td><td></td></tr><tr><td>10</td><td>Rule</td><td>recchrge &lt; 1.6328</td><td>0.0652</td><td>0.5640</td><td>18.3211</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.2954</td><td></td><td></td><td></td></tr><tr><td>11</td><td>Rule</td><td>retcalls &lt; 2.3026</td><td>-0.0552</td><td>0.3947</td><td>15.2900</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2913</td><td></td><td></td><td></td></tr><tr><td>12</td><td>Linear term</td><td>webcap</td><td>-0.0765</td><td>-</td><td>13.5115</td></tr><tr><td>13</td><td>Rule</td><td>retcalls &lt; 2.3026</td><td>-0.0386</td><td>0.3654</td><td>10.5356</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.3615</td><td></td><td></td><td></td></tr><tr><td>14</td><td>Rule</td><td>eqpdays ≥ -0.2996</td><td>0.0351</td><td>0.5920</td><td>9.7650</td></tr><tr><td>15</td><td>Rule</td><td>eqpdays &lt; -0.2996</td><td>-0.0349</td><td>0.4080</td><td>9.7185</td></tr><tr><td>16</td><td>Rule</td><td>eqpdays ≥ -0.2954</td><td>0.0339</td><td>0.5903</td><td>9.4440</td></tr><tr><td>17</td><td>Rule</td><td>eqpdays &lt; -0.2954</td><td>-0.0339</td><td>0.4097</td><td>9.4374</td></tr><tr><td>18</td><td>Linear term</td><td>incalls</td><td>-0.0135</td><td>-</td><td>7.5088</td></tr><tr><td>19</td><td>Rule</td><td>eqpdays &lt; -0.3161</td><td>-0.0238</td><td>0.4017</td><td>6.6227</td></tr><tr><td>20</td><td>Linear term</td><td>setprcm</td><td>-0.0234</td><td>-</td><td>6.5475</td></tr><tr><td>21</td><td>Rule</td><td>eqpdays ≥ -0.3160</td><td>0.0233</td><td>0.5983</td><td>6.4581</td></tr><tr><td>22</td><td>Rule</td><td>eqpdays ≥ -0.2913</td><td>0.0215</td><td>0.5873</td><td>5.9955</td></tr><tr><td>23</td><td>Rule</td><td>eqpdays &lt; -0.2913</td><td>-0.0214</td><td>0.4127</td><td>5.9731</td></tr><tr><td>24</td><td>Linear term</td><td>changem_M</td><td>0.0770</td><td>-</td><td>3.6709</td></tr><tr><td>25</td><td>Rule</td><td>retcalls ≥ 2.3026</td><td>0.0414</td><td>0.0180</td><td>3.1160</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2913</td><td></td><td></td><td></td></tr><tr><td>26</td><td>Rule</td><td>retcalls ≥ 2.3026</td><td>0.0415</td><td>0.0173</td><td>3.0616</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.3615</td><td></td><td></td><td></td></tr><tr><td>27</td><td>Rule</td><td>retcalls ≥ 2.3026</td><td>0.0288</td><td>0.0179</td><td>2.1605</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.296</td><td></td><td></td><td></td></tr><tr><td>28</td><td>Rule</td><td>retcalls ≥ 2.3026</td><td>0.0280</td><td>0.0179</td><td>2.1015</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2954</td><td></td><td></td><td></td></tr><tr><td>29</td><td>Rule</td><td>eqpdays &lt; -0.3615</td><td>-0.0049</td><td>0.3827</td><td>1.3619</td></tr><tr><td>30</td><td>Rule</td><td>eqpdays ≥ -0.3615</td><td>0.0049</td><td>0.6173</td><td>1.3523</td></tr><tr><td>31</td><td>Rule</td><td>recchrge ≥ 1.3767</td><td>-0.0113</td><td>0.0374</td><td>1.2163</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.2954</td><td></td><td></td><td></td></tr></table>

Table A.2  
The Cell2cell spline-rule ensemble model: terms, term types, rule conditions, coefficients, rule support and term importance. Terms are sorted by their importance.

<table><tr><td>Term</td><td>Type</td><td>Term or rule specification</td><td>Coefficient</td><td>Rule support</td><td>Term importance</td></tr><tr><td>1</td><td>Linear term</td><td>retcalls</td><td>0.2107</td><td>-</td><td>100</td></tr><tr><td>2</td><td>Linear term</td><td>revenue</td><td>0.1523</td><td>-</td><td>67.4154</td></tr><tr><td>3</td><td>Spline</td><td>s(changem)</td><td>0.3692</td><td>-</td><td>39.0854</td></tr><tr><td>4</td><td>Linear term</td><td>recchrge</td><td>-0.0505</td><td>-</td><td>22.4276</td></tr><tr><td>5</td><td>Linear term</td><td>creditde</td><td>-0.1467</td><td>-</td><td>21.2720</td></tr><tr><td>6</td><td>Linear term</td><td>changem</td><td>-0.0438</td><td>-</td><td>19.6160</td></tr><tr><td>7</td><td>Spline</td><td>s(eqpdays)</td><td>0.1242</td><td>-</td><td>18.3232</td></tr><tr><td>8</td><td>Rule</td><td>recchrge &lt; 1.3767</td><td>0.0785</td><td>0.5529</td><td>17.4713</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.29547</td><td></td><td></td><td></td></tr><tr><td>9</td><td>Linear term</td><td>setprcm</td><td>-0.0769</td><td>-</td><td>17.0326</td></tr><tr><td>10</td><td>Rule</td><td>recchrge &lt; 1.6328</td><td>0.0705</td><td>0.5640</td><td>15.6602</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.2954</td><td></td><td></td><td></td></tr><tr><td>11</td><td>Rule</td><td>recchrge &lt; 1.1742</td><td>0.0693</td><td>0.5483</td><td>15.4544</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.2954</td><td></td><td></td><td></td></tr><tr><td>12</td><td>Rule</td><td>retcalls &lt; 2.3026</td><td>-0.0697</td><td>0.3901</td><td>15.2346</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2996</td><td></td><td></td><td></td></tr><tr><td>13</td><td>Rule</td><td>retcalls &lt; 2.3026</td><td>-0.0665</td><td>0.3918</td><td>14.5401</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2954</td><td></td><td></td><td></td></tr><tr><td>14</td><td>Linear term</td><td>webcap</td><td>-0.0987</td><td>-</td><td>13.7891</td></tr><tr><td>15</td><td>Spline</td><td>s(mou)</td><td>0.1646</td><td>-</td><td>10.1537</td></tr><tr><td>16</td><td>Rule</td><td>retcalls &lt; 2.3026</td><td>-0.0462</td><td>0.3947</td><td>10.1205</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2913</td><td></td><td></td><td></td></tr><tr><td>17</td><td>Rule</td><td>eqpdays ≥ -0.2996</td><td>0.0369</td><td>0.5920</td><td>8.1317</td></tr><tr><td>18</td><td>Rule</td><td>eqpdays &lt; -0.2996</td><td>-0.0366</td><td>0.4080</td><td>8.0486</td></tr><tr><td>19</td><td>Rule</td><td>eqpdays ≥ -0.2954</td><td>0.0343</td><td>0.5903</td><td>7.5649</td></tr><tr><td>20</td><td>Rule</td><td>eqpdays &lt; -0.2954</td><td>-0.0342</td><td>0.4097</td><td>7.5306</td></tr><tr><td>21</td><td>Spline</td><td>s(incalls)</td><td>0.1299</td><td>-</td><td>5.4361</td></tr><tr><td>22</td><td>Rule</td><td>retcalls &lt; 2.3026</td><td>-0.0226</td><td>0.3654</td><td>4.8747</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.3614</td><td></td><td></td><td></td></tr><tr><td>23</td><td>Linear term</td><td>changem_M</td><td>0.1264</td><td>-</td><td>4.7648</td></tr><tr><td>24</td><td>Rule</td><td>eqpdays &lt; -0.3160</td><td>-0.0166</td><td>0.4017</td><td>3.6533</td></tr><tr><td>25</td><td>Rule</td><td>eqpdays ≥ -0.3161</td><td>0.0160</td><td>0.5983</td><td>3.5121</td></tr><tr><td>26</td><td>Rule</td><td>retcalls ≥ 2.3026</td><td>0.0562</td><td>0.0173</td><td>3.2754</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.3615</td><td></td><td></td><td></td></tr><tr><td>27</td><td>Rule</td><td>recchrge ≥ 1.3767</td><td>-0.0369</td><td>0.0374</td><td>3.1351</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.2954</td><td></td><td></td><td></td></tr><tr><td>28</td><td>Rule</td><td>eqpdays &lt; -0.2913</td><td>-0.0142</td><td>0.4127</td><td>3.1247</td></tr><tr><td>29</td><td>Rule</td><td>eqpdays ≥ -0.2913</td><td>0.0136</td><td>0.5873</td><td>2.9880</td></tr><tr><td>30</td><td>Rule</td><td>retcalls ≥ 2.3026</td><td>0.0469</td><td>0.0180</td><td>2.7890</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2913</td><td></td><td></td><td></td></tr><tr><td>31</td><td>Rule</td><td>recchrge ≥ 1.6328</td><td>-0.0348</td><td>0.0264</td><td>2.4933</td></tr><tr><td></td><td></td><td>eqpdays ≥ -0.2954</td><td></td><td></td><td></td></tr><tr><td>32</td><td>Linear term</td><td>mou</td><td>-0.0054</td><td>-</td><td>2.3950</td></tr><tr><td>33</td><td>Spline</td><td>s(recchrge)</td><td>0.0520</td><td>-</td><td>1.4844</td></tr><tr><td>34</td><td>Rule</td><td>retcalls ≥ 2.3026</td><td>0.0248</td><td>0.0179</td><td>1.4729</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2996</td><td></td><td></td><td></td></tr><tr><td>35</td><td>Rule</td><td>retcalls ≥ 2.3026</td><td>0.0231</td><td>0.0179</td><td>1.3708</td></tr><tr><td></td><td></td><td>eqpdays &lt; -0.2954</td><td></td><td></td><td></td></tr><tr><td>36</td><td>Spline</td><td>s(directas)</td><td>0.0605</td><td>-</td><td>1.2405</td></tr><tr><td>37</td><td>Spline</td><td>s(custcare)</td><td>0.0354</td><td>-</td><td>0.5295</td></tr><tr><td>38</td><td>Spline</td><td>s(callwait)</td><td>0.0373</td><td>-</td><td>0.3732</td></tr></table>

## Appendices B to E

Appendices B–E are available as online supplementary materials available for download at https://github.com/koendebock/SRE-SGL/blob/maste r/SRE-SGL\_supplementary\_materials.pdf.

## References

[1] A. Hagiu, J. Wright, When Data Creates Competitive Advantage...And When It

[2] A. De Caigny, K. Coussement, K.W. De Bock, A new hybrid classification algorithm for customer churn prediction based on logistic regression and decision trees. Eur. J. Oper, Res, 269 (2018) 760–772.

[3] E. Ascarza, S.A. Neslin, O. Netzer, Z. Anderson, P.S. Fader, S. Gupta, B.G.S. Hardie, Customer Retention Management: Review. Key Issues, and Future Directions. Cust. Needs Solut. 2018.

[4] W. Verbeke, K. Dejaeger, D. Martens, J. Hur, B. Baesens, New insights into churn prediction in the telecommunication sector: a profit driven data mining approach. Eur. J. Oper. Res. 218 (2012) 211–229.

[5] M. Oskarsd<sup>´</sup> ottir, ´ C. Bravo, W. Verbeke, C. Sarraute, B. Baesens, J. Vanthienen, Social network analytics for churn prediction in telco: model building, evaluation and network architecture, Expert Syst. Appl. 85 (2017) 204–220.

[6] A. Gustafsson, M.D. Johnson, I. Roos, The effects of customer satisfaction. relationship commitment dimensions, and triggers on customer retention, J. Mark 69 (2005) 210–218

[7] S.A. Neslin, S. Gupta, W. Kamakura, J.X. Lu, C.H. Mason, Defection detection: measuring and understanding the predictive accuracy of customer churn models,

[8] B. Masand, P. Datta, D.R. Mani, B. Li, CHAMP: a prototype for automated cellular churn prediction, Data Min. Knowl. Disc. 3 (1999) 219–225.

[9] K.W. De Bock, D. Van Den Poel, Reconciling performance and interpretability in customer churn prediction using ensemble learning based on generalized additive models, Expert Syst. Appl. 39 (2012).

[10] D. Martens, J. Vanthienen, W. Verbeke, B. Baesens, Performance of classification models from a user perspective, Decis. Support. Syst. 51 (2011) 782–793.

[11] J.H. Friedman, B.E. Popescu, Predictive learning via rule ensembles, Ann. Appl. Stat. 2 (2008) 916–954.

[12] K.W. De Bock, The best of two worlds: Balancing model strength and comprehensibility in business failure prediction using spline-rule ensembles, Expert Syst. Appl. 90 (2017).

[13] F. Klepsch, G.F. Ecker, Impact of the recent mouse P-glycoprotein structure for structure-based ligand design. Mol. Inform. 29 (2010) 276–286.

[14] T. Ouyang, S. Ray, M. Allman, M. Rabinovich, A large-scale empirical analysis of email spam detection through network characteristics in a stand-alone enterprise, Comput, Netw. 59 (2014) 101–121

[15] N. Simon, J. Friedman, T. Hastie, R. Tibshirani, A sparse-group lasso, J. Comput. Graph. Stat. 22 (2013) 231–245.

[16] M.T. Ribeiro, S. Singh, C. Guestrin, “Why should i trust you?” Explaining the predictions of any classifier, in: Proc. ACM SIGKDD Int. Conf. Knowl. Discov. Data Min, 2016.

[17] D. Martens, F. Provost, Explaining data-driven document classifications, MIS Q. Manag, Inf, Syst, 38 (1) (2014) 73–100.

[18] O. Biran, C. Cotton, Explanation and justification in machine learning: a survey, in: IJCAI-17 Work. Explain, AI, 2017.

[19] T. Miller, Explanation in artificial intelligence: insights from the social sciences, Artif. Intell. 267 (February 2019) 1–38.

[20] C. Molnar, Interpretable machine learning, in: A Guide for Making Black Box Models Explainable, 2019.

[21] K. Coussement, S. Lessmann, G. Verstraeten, A comparative analysis of data preparation algorithms for customer churn prediction: a case study in the telecommunication industry, Decis. Support. Syst. 95 (March 2017) 27–36.

[22] A. De Caigny, K. Coussement, K.W. De Bock, S. Lessmann, Incorporating textual information in customer churn prediction models based on a convolutional neural network, Int. J. Forecast, 36 (4) (2019) 1563–1578.

[23] K. Coussement, D. Van den Poel, Churn prediction in subscription services: an application of support vector machines while comparing two parameter-selection techniques, Expert Syst. Appl. 34 (2008) 313–327.

[24] W. Verbeke, D. Martens, C. Mues, B. Baesens, Building comprehensible customer churn prediction models with advanced rule induction techniques, Expert Syst. Appl. 38 (2011) 2354–2364.

[26] V.L. Migu´eis, A. Camanho, J. Falcao ˜ e Cunha, Customer attrition in retailing: an application of multivariate adaptive regression splines. Expert Syst. Appl. 40 (2013) 6225–6232.

[27] J.H. Friedman. Multivariate adaptive regression splines. Ann. Stat. 19 (1991) 1–67

[28] K. Coussement, D.F. Benoit, D. Van den Poel, Improved marketing decision making in a customer churn prediction context using generalized additive models, Expert Syst. Appl. 37 (2010) 2132–2143.

[29] K. Coussement, K.W. De Bock, Customer churn prediction in the online gambling industry: the beneficial effect of ensemble learning, J. Bus. Res. 66 (2013) 1629–1636.

[30] K.W. De Bock, D. Van Den Poel, Reconciling performance and interpretability in customer churn prediction modeling using ensemble learning based on generalized additive models, Expert Syst. Appl. 39 (2012) 6816–6826.

[311 K.W. De Bock, K. Coussement. D. Van den Poel. Ensemble classification based on generalized additive models, Comput. Stat. Data Anal. 54 (2010).

[32] J. Qi, L. Zhang, Y. Liu, L. Li, Y. Zhou, Y. Shen, L. Liang, H. Li, ADTreesLogit model for customer churn prediction, Ann. Oper. Res. 168 (1) (2009) 247–265.

[33] A. Backiel, B. Baesens, G. Claeskens, Predicting time-to-churn of prepaid mobile telephone customers using social network analysis, J. Oper. Res. Soc. 67 (9) (2016)

[34] T. Verbraken, W. Verbeke, B. Baesens, Profit optimizing customer churn prediction with Bayesian network classifiers, Intell. Data Anal. 18 (1) (2014) 3–24.

[35] E. Lima, C. Mues, B. Baesens, Domain knowledge integration in data mining using decision tables: case studies in churn prediction, J. Oper. Res. Soc. 60 (2009) 1096–1106.

[36] L.I. Kuncheva, Combining Pattern Classifiers: Methods and Algorithms, John Wiley & Sons, Hoboken, New Jersey, 2004.

[37] Y. Freund, R.E. Schapire, Experiments with a new boosting algorithm, in: L. Saitta (Ed.), Thirteen. Int. Conf. Mach. Learn. (ICML 1996), Morgan Kauffman, Bari, Italy, 1996, pp. 148–156.

[38] L. Breiman, Bagging predictors, Mach. Learn. 24 (1996) 123–140.

[39] L. Breiman, Random forests, Mach. Learn. 45 (2001) 5–32.

[40] J.J. Rodríguez, L.I. Kuncheva, C.J. Alonso, I.C. Society, L.I. Kuncheva, C.J. Alonso, Rotation forest: a new classifier ensemble method, JEEE Trans. Pattern Anal, Mach Intell, 28 (2006) 1619–1630.

[41] W.W. Cohen, Y. Singer, A simple, fast, and effective rule learner, in: Proc. Sixt. Natl. Conf. Artif. Intell. Elev. Innov. Appl. Artif. Intell. Conf. Innov. Appl. Artif. Intell, American Association for Artificial Intelligence, USA, 1999, pp. 335–342.

[42] J. Błaszczynski, ´ K. Dembczynski, ´ W. Kotłowski, R. Słowinski, ´ M. Szelkag, Ensemble of decision rules, Found. Comput. Decis. Sci. 31 (2006) 221–232.

[43] K. Dembczynski, ´ W. Kotłowski, R. Słowinski, ´ Maximum likelihood rule ensembles, in: Proc. 25th Int. Conf. Mach. Learn, Association for Computing Machinery, New York, NY. USA, 2008, pp. 224–231.

[44] W. Yang, S. Zhang, Y. Chen, Y. Chen, W. Li, H. Lu, Mining diagnostic rules of breast tumor on ultrasound image using cost-sensitive RuleFit method, in: 2008 3rd Int. Conf. Intell. Syst. Knowl. Eng, 2008, pp. 354–359.

[45] D. Mohapatra, B. Subudhi, Weighted majority rule ensemble classifier for sensor fault classification for plasma position control in Tokamaks, Fusion Eng. Des. 160 (2020) 111969.

[46] J.M.J. Debrulle, P. Steffens, K.W. De Bock, S. De Winne, Configurations of business founder resources, strategy and environment determining new venture performance, J. Small Bus. Manag. (2021).

[47] T. Shimokawa, L. Li, K. Yan, S. Kitamura, M. Goto, Modified rule ensemble method for binary data and its applications, Behaviormetrika. 41 (2014) 225–244.

[48] R. Tibshirani, Regression shrinkage and selection via the lasso, J. R. Stat. Soc. Ser B 58 (1996) 267–288.

[49] S.N. Wood, Generalized Additive Models: An Introduction with R, CRC press, 2017.

[50] M. Yuan, Y. Lin, Model selection and estimation in regression with groupe variables, J. R. Stat. Soc. Ser. B 68 (2006) 49–67. Statistical Methodol.

[51] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classification and Regression Trees, Wadsworth International Group, Belmont, CA, 1984.

[52] T. Hastie, R. Tibshirani, Generalized Additive Models, Chapman and Hall, London, 1990.

[53] P. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, Addison Wesley, Boston, MA, 2006.

[54] J. Burez, D. Van den Poel, Handling class imbalance in customer churn prediction, Expert Syst. Appl. 36 (2009) 4626–4636.

[55] P. Craven, G. Wahba, Smoothing noisy data with spline functions, Numer. Math. 31 (1978).377–403

[56] S.N. Wood, Stable and efficient multiple smoothing parameter estimation for generalized additive models, J. Am. Stat. Assoc. 99 (2004) 673–686.

[57] J. Demˇsar, Statistical comparisons of classifiers over multiple data sets, J. Mach. Learn, Res, 7 (2006) 1–30

[58] S. García, A. Fernandez, ´ J. Luengo, F. Herrera, Advanced nonparametric tests for multiple comparisons in the design of experiments in computational intelligence and data mining: experimental analysis of power, Inf. Sci. (Ny). 180 (2010) 2044–2064.

[59] J. Hastie, Tibshirani Trevor, Friedman Robert, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Second edition, 2009.

[60] M. Bogaert, M. Ballings, D. Van den Poel, The added value of Facebook friends data

[61] T. Verbraken, W. Verbeke. B. Baesens. A novel profit maximizing metric for measuring classification performance of customer churn prediction models. JEEE Trans. Knowl. Data Eng. 25 (2013) 961–973.

![](/api/attachments/W9F4V77F/fulltext/images/3d1d9c14f3d946e9400652506422c687592a855f29131f5ad17c02580096b1da.jpg)  
Koen W. De Bock (Ph.D.) is professor of marketing analytics and digital marketing at Audencia Business School (Nantes, France). He also teaches in the MBA programs at the University of Stellenbosch Business School (USB) and TIAS School for Business and Society. His courses focus on digital marketing, web analytics, search engine marketing as well as marketing analytics. Passionate about applications of machine learning and predictive modeling in marketing, he has collaborated with several companies such as Leroy Merlin, La Redoute and Cr´edit Agricole, and his research was published in several interna tional journals includingincluding Annals of Operations Reserach, International Journal of Forecasting, Decision Support Systems and European Journal of Operational Research.

![](/api/attachments/W9F4V77F/fulltext/images/c2acd286bbaaa226282a1685fbd842c3ecdedaa282b117675361c614b4643350.jpg)

Arno De Caigny (Ph.D.) is assistant professor of marketing analytics at IESEG <sup>´</sup> School of Management (LEM-CNRS). He earned a master degree in applied economics and an advanced master degree in marketing analysis at Ghent University (Belgium). He obtained his Ph.D. from the University of Lille (France) in 2019 in which he investigated innovative ways to improve customer scoring models using big data. He has pub lished in international peer-reviewed journals such as European Journal of Operational Research, Decision Support Systems and International Journal of Forecasting.
