---
otero_id: 2178
otero_key: "9VRDHYAD"
title: "Performance of classification models from a user perspective"
authors: "David Martens; Jan Vanthienen; Wouter Verbeke; Bart Baesens"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Performance of classi<sup>fi</sup>cation models from a user perspective

David Martens <sup>a,</sup>⁎, Jan Vanthienen <sup>b</sup>, Wouter Verbeke <sup>b</sup>, Bart Baesens <sup>b,c,d</sup>

<sup>a</sup> Department of Environment, Technology and Technology Management, University of Antwerp, Prinsstraat 13, B-2000 Antwerp, Belgium

<sup>b</sup> Department of Decision Sciences and Information Management, Katholieke Universiteit Leuven, Naamsestraat 69, B-3000 Leuven, Belgium

<sup>c</sup> School of Management, University of Southampton, Highfield Southampton, SO17 1BJ, United Kingdom

<sup>d</sup> Vlerick, Leuven-Gent Management School, Reep 1, B-9000 Ghent, Belgium

## a r t i c l e i n f o

Available online 1 February 2011

Keywords: Data mining Classi<sup>fi</sup>cation Metrics Justi<sup>fi</sup>ability Comprehensibility

## a b s t r a c t

This paper proposes a complete framework to assess the overall performance of classi<sup>fi</sup>cation models from a user perspective in terms of accuracy, comprehensibility, and justi<sup>fi</sup>ability. A review is provided of accuracy and comprehensibility measures, and a novel metric is introduced that allows one to measure the justi<sup>fi</sup>ability of classi<sup>fi</sup>cation models. Furthermore, taxonomy of domain constraints is introduced, and an overview of the existing approaches to impose constraints and include domain knowledge in data mining techniques is presented. Finally, justi<sup>fi</sup>ability metric is applied to a credit scoring and customer churn prediction case.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Different data mining tasks, such as regression, classi<sup>fi</sup>cation, association rule mining and clustering, are widely discussed in the literature [5,58,72]. The task of interest in this study is classi<sup>fi</sup>cation, which comes down to assigning a data point to a prede<sup>fi</sup>ned class or group according to its predictive characteristics. The goal of a classi<sup>fi</sup>cation technique is to build a model which makes it possible to classify future data points based on a set of speci<sup>fi</sup>c characteristics in an automated way. In the literature, a myriad of different techniques has been proposed for this classi<sup>fi</sup>cation task [5,27], some of the most commonly used being C4.5 [49], CART [10], logistic regression [30], linear and quadratic discriminant analysis [9,30], knearest neighbor [1,18,30], Arti<sup>fi</sup>cial Neural Networks (ANN) [9] and Support Vector Machines (SVM) [14,56,68].

Classi<sup>fi</sup>cation techniques are often applied for credit scoring [5,59] (separating good from bad loan applicants), for customer churn prediction [70], and for medical diagnosis (e.g., for the prediction of dementia [47], classifying a breast mass as benign or malignant, or for selecting the best in-vitro fertilized embryo [43]). Many other data mining applications have been put forward recently, such as the use of data mining for bio-informatics [32], marketing and election campaigns [28], and counter-terrorism [50].

Several performance requirements exist for a classi<sup>fi</sup>cation model. From a user perspective, the model should be comprehensible and justi<sup>fi</sup>able (i.e., intuitively correct and in accordance with domain knowledge), and provide correct predictions. The last requirement is that the model generalizes well, in the sense that it provides correct predictions on new, unseen data instances. This generalization behavior is typically measured by the percentage of correctly classi<sup>fi</sup>ed test instances (PCC). Other commonly used measures include sensitivity and speci<sup>fi</sup>city, the receiver operating curve (ROC), and the area under this curve (AUC) [21]. Section 3 provides a discussion on these measures.

Comprehensibility is often a key requirement, demanding that the user is able to understand the logic behind a prediction of the model. In some domains, such as credit scoring and medical diagnosis, a lack of comprehensibility is a major issue, and causes a reluctance to use the classi<sup>fi</sup>er or even a complete rejection of the model. In a credit scoring context, the Equal Credit Opportunity Act of the U.S. requires that if credit is denied, the <sup>fi</sup>nancial institution should provide speci<sup>fi</sup>c reasons why the customer's application is rejected, whereby vague reasons for denial are illegal [24]. In the medical diagnosis domain as well, clarity and explainability are key requirements.

Whenever comprehensibility is needed, it will be needed so as to check whether the model is in line with existing domain knowledge. For instance, a model which estimates loan applicants with a high income to have a high default probability, and similar applicants with a low income to have a small default probability, is not in line with domain knowledge. Such a model is counter-intuitive and thus unacceptable for implementation. Hence when justi<sup>fi</sup>ability is required, comprehensibility will be needed as well. A data mining approach that takes into account the knowledge representing the experience of domain experts is therefore much preferred and of great focus in current data mining research. However, in depth search did not identify any measure to assess the justi<sup>fi</sup>ability. Therefore Section 5 introduces a novel metric which allows one to measure the justi<sup>fi</sup>ability of a classi<sup>fi</sup>cation model.

The stability of a model is also an important aspect, for two key reasons: (1) the independent variables in the model should be signi<sup>fi</sup>cantly related to the target variable; and (2) the nature of this relation should be independent of the number and type of the other variables included in the model. An easy implementation on the other hand is required to allow the model to be effectively deployed, and, if necessary, updated and re-estimated when new training data becomes available. This is closely related to the computational requirements needed to (re-)estimate the model, as well as to the scalability of the model, which refers to the possibility to induce and operate the model when a large amount of data is available. Although these aspects are also of importance from a general data mining perspective, the <sup>fi</sup>nal user will have little concerns once a model has been provided. Therefore these are outside of the scope of this paper.

The remainder of this paper is structured as follows: Section 2 provides a structural overview of the most common classi<sup>fi</sup>cation output types, and Section 3 discusses the most widely used measures to assess the generalization behavior of a classi<sup>fi</sup>cation model, which is a <sup>fi</sup>rst important issue when assessing a classi<sup>fi</sup>cation model. Then, Section 4 describes the comprehensibility requirement in a data mining context, and discusses how to de<sup>fi</sup>ne, measure, and obtain comprehensibility. A further discussion into the academically challenging justi<sup>fi</sup>ability requirement is provided in Section 5. Here as well, approaches to obtain justi<sup>fi</sup>able models are reviewed. Finally, a metric to measure justi<sup>fi</sup>ability is proposed.

## 2. Classi<sup>fi</sup>cation output types

Many different types of classi<sup>fi</sup>cation output exist. The most commonly used types are:

(1) Linear models, built by e.g. linear and logistic regression. A typical logistic regression formulation for a data set $D =$ $\{ \mathbf { x } ^ { i } , \bar { y } ^ { i } \} _ { i = 1 } ^ { n }$ with input data $\mathbf { x } ^ { i } \in \mathbb { R } ^ { m }$ , and corresponding binary class labels $y ^ { i } \in \{ 0 , 1 \}$ is:

$$
y _ {\mathrm{logit}} (\mathbf {x}) = \frac {1}{1 + \exp (- (\beta_ {0} + \beta^ {T} \mathbf {x}))},\tag{1}
$$

with $y _ { \mathrm { l o g i t } } ( \mathbf { x } ) { \in } [ 0 , 1 ]$ typically mapped to a class label by setting a cutoff value. The cutoff value in<sup>fl</sup>uences the generalization behavior of the classi<sup>fi</sup>er, as will be discussed in the next section.

(2) Non-linear models, built by e.g. ANNs and SVMs. The model formulation for a SVM with Radial Basis Function kernel is:

$$
y _ {\mathrm{SVM}} (\mathbf {x}) = \sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {i} \exp \left\{- \| \mathbf {x} - \mathbf {x} ^ {i} \| _ {2} ^ {2} / \sigma^ {2} \right\} + b,\tag{2}
$$

with $y _ { \mathrm { S V M } } ( \mathbf { x } ) \in [ - 1 , 1 ]$ typically mapped to a class label by a sign operator.

(3) Rule-based models, i.e. models in a rule-set format, induced by, for instance, RIPPER [13], CN2 [12], and AntMiner+ [38].

(4) Tree-based models, built by e.g. C4.5 [49], and CART [10].

Other common model types are nearest neighbor classi<sup>fi</sup>ers and Bayesian networks. Benchmarking studies have shown that in general non-linear models provide the most accurate predictions [5,61], as they are able to capture non-linearities in the data. However, this strength is also their main weakness, as the model is considered to be a black box: as shown by Eq. (2) it is very dif<sup>fi</sup>cult to understand the logics behind the decisions made by the model, if not impossible. Therefore, an incremental approach can be followed as introduced by Van Gestel et al. [62–64], which builds a non-linear SVM on top of a linear model so as to <sup>fi</sup>nd a trade-off between simple, linear techniques with good readability but restricted model <sup>fl</sup>exibility and complexity, and advanced techniques with reduced readability but extended <sup>fl</sup>exibility and generalization behavior. Fig. 1 illustrates the principle behind an incremental approach.

![](/api/attachments/9VRDHYAD/fulltext/images/b2057c1843d5be0d7c8815a5860f94ae8cad940be4f2dcf717fa3098f32c82ba.jpg)  
Fig. 1. From linear to non-linear models.

## 3. Generalization behavior

This section provides a dense, non-exhaustive summary of the most generally used measures to assess the generalization power of classi<sup>fi</sup>cation models.

## 3.1. Percentage correctly classified

The percentage of correctly classified (PCC) observations measures the proportion of correctly classi<sup>fi</sup>ed cases on a sample of data. Although straightforward, the PCC may not be the most appropriate performance criterion in a number of cases. It tacitly assumes equal misclassi<sup>fi</sup>cation costs for false positive and false negative predictions. This assumption can be problematic, since for most real-life problems, one type of classi<sup>fi</sup>cation error may be much more expensive than the other. A second implicit assumption when using the PCC as evaluation criterion is that the class distribution (class priors) among examples is presumed constant over time, and relatively balanced [48]. Thus, using the PCC alone proves to be inadequate, since class distributions and misclassi<sup>fi</sup>cation costs are rarely uniform. However, taking into account class distributions and misclassi<sup>fi</sup>cation costs proves to be quite hard, since in practice they can rarely be speci<sup>fi</sup>ed precisely, and are often subject to change [23].

## 3.2. Sensitivity, specificity, and the receiver operating characteristic curve

Class-wise decomposition of the classi<sup>fi</sup>cation of cases yields a confusion matrix as speci<sup>fi</sup>ed in Table 1. If TP, FP, FN, and TN represent the number of true positives, false positives, false negatives, and true negatives, then the sensitivity or true positive rate measures the proportion of positive examples which are predicted to be positive $\mathrm { ( T P / ( T P + F N ) } )$ , whereas the specificity or the true negative rate measures the proportion of negative examples which are predicted to be negative (TN/(TN+FP)). Using the notation of Table 1, we may now formulate the overall accuracy as $\mathrm { P C C } = ( \mathrm { T P } + \mathrm { T N } ) / ( \mathrm { T P } + \mathrm { F P } +$

The confusion matrix for binary classi<sup>fi</sup>cation.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Actual</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="2">Predicted</td><td>+</td><td>True positive (TP)</td><td>False positive (FP)</td></tr><tr><td>-</td><td>False negative (FN)</td><td>True negative (TN)</td></tr></table>

TN+FN). Note that sensitivity, speci<sup>fi</sup>city, and PCC vary together as the threshold on a classi<sup>fi</sup>er's continuous output is varied between its extremes. The receiver operating characteristic curve (ROC) is a 2- dimensional graphical illustration of the sensitivity on the Y-axis versus (1-speci<sup>fi</sup>city) on the X-axis for various values of the classi<sup>fi</sup>cation threshold. It basically illustrates the behavior of a classi<sup>fi</sup>er without regard to class distribution or misclassi<sup>fi</sup>cation cost, so it effectively decouples classi<sup>fi</sup>cation performance from these factors [19,57]. An example of a ROC curve is shown in Fig. 2.

## 3.3. Area under the receiver operating characteristic curve

In order to compare ROC curves of different classi<sup>fi</sup>ers, one often calculates the area under the receiver operating characteristic curve (AUROC or AUC). The AUC then provides a simple <sup>fi</sup>gure-of-merit for the performance of the constructed classi<sup>fi</sup>er. An intuitive interpretation of the AUC is that it provides an estimate of the probability that a randomly chosen instance of class 1 (positive instance, e.g. a churner) is correctly rated (or ranked) higher than a randomly selected instance of class 0 (negative instance, e.g. a non-churner). Note that since the area under the diagonal corresponding to a pure random classi<sup>fi</sup>cation model equals 0.5, a good classi<sup>fi</sup>er should have an AUC much larger than 0.5.

As rule-sets do not provide a continuous output, their ROC curve has only as many points as there are rules, resulting in a discontinuous, piecewise monotone ROC curve. However, by using a rule-set in a more <sup>fl</sup>exible manner, in order to produce instance scores indicating the likelihood that an instance belongs to a given class, Fawcett [20,22] extended the concept of ROC and AUC for use with rule-sets.

Recently, a conceptual error in the AUC was described by Hand [29], concerning unequal misclassi<sup>fi</sup>cation cost distributions that are tacitly assumed when comparing different classi<sup>fi</sup>ers using the AUC. Using the AUC is therefore equivalent to using different metrics to evaluate different classi<sup>fi</sup>cation rules. An alternative measure is proposed, (i.e., the H-measure), which makes explicit use of the Beta distribution as the cost distribution function, with default values α=2 and β=2. The use of the Beta distribution and the values of α and β are arbitrary choices, but as Hand [29] advocates, nonetheless allow legitimate comparison of different classi<sup>fi</sup>ers and reproducable results if generally used by the scienti<sup>fi</sup>c community.

## 3.4. Gini coefficient and Kolmogorov–Smirnov statistic

A measure that is closely related to the AUC is the Gini coefficient [59], which is equal to twice the area between the ROC curve and the diagonal, i.e. Gini=2 AUC-1. The Gini coef<sup>fi</sup>cient lies between 0 (i.e. the ROC curve lies on the diagonal and the model does not perform better than a random classi<sup>fi</sup>cation model) and 1 (i.e. maximum ROC curve and perfect classi<sup>fi</sup>cation). Another performance measure related to the ROC curve is the Kolmogorov–Smirnov (KS) statistic.

![](/api/attachments/9VRDHYAD/fulltext/images/104745123fb66dbfaf1ae039a498889ba9c85bcf37b724604db24ca8626971e2.jpg)  
Fig. 2. Example of ROC curve with convex hull.

The KS statistic gives the distance between the ROC curve and the diagonal, for the cutoff value corresponding to the largest distance between the diagonal and the ROC curve. Again, a value of the KS performance measure equal to one means a perfect classi<sup>fi</sup>cation, and KS equal to zero means no better classi<sup>fi</sup>cation than a random classi<sup>fi</sup>er. The KS measure is indicated in Fig. 2.

## 4. Comprehensibility of classi<sup>fi</sup>cation models

## 4.1. Comprehensibility as a requirement

Comprehensibility can be a key requirement for a classi<sup>fi</sup>cation model, demanding that the user can understand the motivations behind the prediction of a model. It is an absolute necessity in any domain where the model needs to be validated before it can actually be implemented for practical use. Typical domains are the highly regulated credit scoring and medical diagnosis domain. However, in other domains as well, comprehensibility and justi<sup>fi</sup>ability will lead to a greater acceptance of the provided model. For instance a customer churn prediction model [70] that is used by a marketing department to design customer retention campaigns in order to prevent customers from churning, should be comprehensible to understand why customers churn, and whether the model is in line with domain knowledge. The importance of comprehensibility for any data mining application is argued by Kodratoff, who states in his comprehensibility postulate that "each time one of our favorite machine learning approaches has been applied in industry, each time the comprehensibility of the results, though ill-de<sup>fi</sup>ned, has been a decisive factor of choice over an approach by pure statistical means, or by neural networks" [34].

De<sup>fi</sup>ning comprehensibility is close to being a philosophical discussion. Still, to get some clarity on what this requirement exactly entails, we will try to de<sup>fi</sup>ne when a classi<sup>fi</sup>cation model is comprehensible. As will be argued next, comprehensibility measures the "mental <sup>fi</sup>t" [35] of the classi<sup>fi</sup>cation model. Its main drivers are: (1) the type of output, i.e. although the comprehensibility of a speci<sup>fi</sup>c output type is largely domain-dependent, generally speaking, rulebased classi<sup>fi</sup>ers can be considered as the most comprehensible, and non-linear classi<sup>fi</sup>ers as the least comprehensible; and (2) the size of the output, i.e. smaller models are preferred.

The <sup>fi</sup>rst main criterion for comprehensibility is the model output, which can be rule-based, tree-based, linear, non-linear, instancebased (e.g. k-nearest neighbor), and many others. Which of these rule types is the most comprehensible is largely domain-speci<sup>fi</sup>c, as comprehensibility is a subjective matter, or put differently: comprehensibility is in the eye of the beholder. Michalski was one of the <sup>fi</sup>rst to address the comprehensibility issue in Knowledge Discovery in Data [41]. He states in his comprehensibility postulate that "The results of computer induction should be symbolic descriptions of given entities, semantically and structurally similar to those a human expert might produce observing the same entities." Mainon and Rokach address this subjectivity issue as follows [35]: "The comprehensibility criterion (also known as interpretability) refers to how well humans grasp the classi<sup>fi</sup>er induced. While the generalization error measures how the classi<sup>fi</sup>er <sup>fi</sup>ts the data, comprehensibility measures the "mental $\mathbf { \nabla } f t ^ { \prime \prime }$ of that classi<sup>fi</sup>er. …the accuracy and complexity factors can be quantitatively estimated, while the comprehensibility is more subjective." This concept of mental <sup>fi</sup>t points out that if the user is more familiar with linear models, the mental <sup>fi</sup>t with such models will be greater than the <sup>fi</sup>t with tree-based classi<sup>fi</sup>ers. Generally speaking however, one can argue that more linguistic models will give a better mental <sup>fi</sup>t. From that point of view rule (and tree-) based classi<sup>fi</sup>ers are considered the most comprehensible, and non-linear classi<sup>fi</sup>ers the least comprehensible model output type, keeping in mind however that for some domains other output types, such as for instance a linear model or 1NN classi<sup>fi</sup>er, can be regarded as the most comprehensible.

For a given rule output, the comprehensibility decreases with the size [3]. Domingos motivates this with Occam's razor, interpreting this principle as [17]: "preferring simpler models over more complex." Speaking in a rule-based context, the more conditions (terms), the harder to understand [31]. For a given number of conditions it is better to have many rules with a low average number of conditions per rule, than few rules with many conditions [55]: "a theory consisting of few long clauses is harder to understand than one with shorter clauses, even if the theories are of the same absolute size." This size concept can of course be extended to all rule outputs [17], for instance the number of nodes in a decision tree, the number of weights in a neural network, or the number of support vectors in a support vector machine.

Finally, although model output and model size are considered to be the main components determining comprehensibility, the concept can be deepened further, as it also depends on aspects such as the number of variables and constants in a rule, the number of instances it covers [55], and even the consistency with existing domain knowledge [44] as will be addressed in Section 5.

## 4.2. Measuring comprehensibility

With the previous discussion in mind, comprehensibility can be measured in the following ways. First of all, there seems to be a ranking in the comprehensibility of the different output types, such that one can state that rule-based models are more comprehensible than linear ones, which are again more comprehensible than nonlinear ones. However, this seemingly obvious conclusion is not always true: a linear model with just one variable will surely be more comprehensible than a rule-based model with over twenty rules. Furthermore, comparing the comprehensibility of a nearest neighbor classi<sup>fi</sup>er is also very dif<sup>fi</sup>cult. Whereas a one nearest neighbor (1NN) classi<sup>fi</sup>er might be very logical and comprehensible in one domain, it might be pretty meaningless in another. For instance in domains with high dimensional data, where even the most similar training instance still differs in many of the variables, a nearest neighbor is rather an abstract concept that does not make much sense. In general this ranking in output types will typically be true and observable. The best way however to verify this, is to ask application domain experts and users for their own ranking, in order to determine their mental fit with the different output types.

Within a given output type, the size can be measured dependent on the type of the model. For non-linear and linear models the size can be determined as the number of terms in the <sup>fi</sup>nal mathematical formulation (e.g. the number of support vectors for SVMs or the number of weights for ANNs, and for linear models the number of included variables). The size of rule and tree based models on the other hand is characterized by respectively the number of rules and the number of leaves, as well as the number of terms per rule and nodes per branch. For a certain number of terms there is a preference for more rules with less terms.

## 4.3. Obtaining comprehensible classification models

## 4.3.1. Building rule-based models

Comprehensible classi<sup>fi</sup>ers can be obtained in a variety of ways. As we consider rules and trees to be the most comprehensible format for a classi<sup>fi</sup>cation model (given their linguistic nature, and therefore the ease of understanding them by non-experts), techniques that induce such models are considered to be the most suitable. Rule induction and extraction techniques fall into this category.

Rule induction techniques induce rules from structured data. Example techniques are C4.5, CART, CN2 and AntMiner+. Comprehensibility can also be added to black box models by extracting symbolic rules from the trained model, rather than immediately from the data. Rule extraction techniques attempt to open up the black box and generate symbolic, comprehensible descriptions with approximately the same predictive power as the black box model itself. A decompositional rule extraction technique is closely intertwined with the internal workings of the model, and will therefore typically make use of concepts as neurons, weights, support vectors, or decision boundaries. A pedagogical algorithm on the other hand considers the trained model as a black box. Instead of looking at the internal structure, these algorithms do not make use of the support vectors or the decision boundary, but directly extract rules using the input– output mapping de<sup>fi</sup>ned by the model. These techniques typically use the trained model as an oracle to label or classify training examples which are then used by a symbolic learning algorithm. The difference between decompositional and pedagogical rule extraction techniques is schematically illustrated in Fig. 3. If the rules mimic the model closely enough, and thus if the black box model is explained suf<sup>fi</sup>ciently, one might opt to use the black box model. Extraction techniques have been proposed from ANNs [4], as well as from SVMs [37,40].

## 4.3.2. Combining output types

An incremental approach that combines several output types can be followed, so as to <sup>fi</sup>nd a trade-off between simple techniques with good comprehensibility, but restricted model <sup>fl</sup>exibility and complexity, and advanced techniques with reduced comprehensibility but extended <sup>fl</sup>exibility and generalization behavior.

Setiono et al. [51,52] combine rules with logistic regression. First, rules are induced for all the nominal variables. Hereafter, instead of providing a simple class label, a linear model is estimated with the remaining continuous variables. As such, a set of rules is obtained, with a linear regression model as the <sup>fi</sup>nal prediction. This approach has been successfully applied to credit scoring [51].

Van Gestel et al. [62–64] combine the comprehensibility of linear models with the good generalization behavior of SVMs. On top of a simple logistic regression model, extra SVM terms are added that try to model the residual errors, resulting in an increased accuracy. This combination of linear, intrinsically linear, and SVM terms is formulated in Eq. (3).

$$
\begin{array}{l} z _ {L} = - \beta_ {1} x _ {1} - \beta_ {2} x _ {2} - \ldots - \beta_ {m} x _ {m} \\ z _ {I L} = - \beta_ {1} x _ {1} - \ldots - \beta_ {m} x _ {m} - \beta_ {m + 1} f _ {m + 1} (x _ {m + 1}) - \ldots - \beta_ {n} x _ {n} \\ \overbrace {- \beta_ {1} x _ {1} - \ldots - \beta_ {m} x _ {m}} ^ {\text {   intrinsically   linear   part   }} \overbrace {- \beta_ {m + 1} f _ {m + 1} (x _ {m + 1}) - \ldots - \beta_ {n} x _ {n}} ^ {\text {   linear   part   }} \\ y _ {\text { logit }} (\mathbf {x}) = \frac {1}{1 + \exp (- (\beta_ {0} + z _ {I L + S V M}))}. \end{array}\tag{3}
$$

The latent variable $z _ { L }$ is a linear combination of the independent variables $x _ { i \cdot }$ The latent variable $z _ { I L }$ includes univariate nonlinear transformations $x _ { i } \to f _ { i } ( x _ { i } )$ of the independent variables. The resulting model is called intrinsically linear, in the sense that after applying a nonlinear transformation to the explanatory variables, a linear model is being <sup>fi</sup>t. More complex nonlinearities can be captured by adding nonlinear SVM terms w<sub>i</sub>ϕ<sub>i</sub>(x), resulting in the latent variable $Z _ { I L \mathrm { ~ - ~ } }$ +SVM that is incorporated in the logistic regression model in Eq. (3) [62].

## 4.3.3. Visualization

A last approach to incorporate comprehensibility is visualization, including plots, decision tables and diagrams, and self-organizing maps.

Data visualization entails displaying information in graphical or tabular format to allow for better interpretation, and thus validation, of the information by a person in order to obtain an acceptable classi<sup>fi</sup>er [58]. Plots are a very straightforward way of visualizing data and a classi<sup>fi</sup>cation model. Higher dimensional data with four variables or more, cannot be displayed with simple plots, and therefore need to be visualized with more advanced techniques such as self-organizing maps (SOMs).

SOMs are a single-layer feedforward neural network, where the outputs are arranged in a low-dimensional grid (typically two or three dimensional), and provide a low dimensional representation of the training data. This unsupervised data mining technique is typically used for clustering and data visualization [58].

Another way to add comprehensibility to a model is by using decision tables. As the proposed justi<sup>fi</sup>ability metric in Section 5 is based on this notion, we will look at this representation form in more detail. Decision tables are a tabular representation used to describe and analyze decision situations [66,67]. They consist of four quadrants, separated by double-lines, both horizontally and vertically. The vertical line divides the table into a condition part (left) and an action part (right), while the horizontal line separates subjects (above) from entries (below). The condition subjects are the problem criteria (the variables) that are relevant to the decision-making process. The action subjects describe the possible outcomes of the decision-making process, i.e. the classes of the classi<sup>fi</sup>cation problem: customer=churner or not, applicant=good or bad. Each condition entry describes a relevant subset of values (which is called a state) for a given condition subject (variable), or contains a dash symbol (‘–’) if its value is irrelevant within the context of that row. Subsequently, every action entry holds a value assigned to the corresponding action subject (class).

Every row in the entry part of the decision table thus comprises a classi<sup>fi</sup>cation rule, indicating the actions that apply to a certain combination of condition states. For instance, in Table 2 the <sup>fi</sup>nal row tells us to classify the applicant as good if owns property=no and savings amount= high.

## 5. Justi<sup>fi</sup>ability of classi<sup>fi</sup>cation models

Although many powerful classi<sup>fi</sup>cation algorithms have been developed, they generally rely solely on modeling repeated patterns or correlations which occur in the data. However, it may well occur that observations which are very evident to classify by the domain expert, do not appear frequently enough in the data to be appropriately modeled by a data mining algorithm. Hence, the intervention and interpretation of a domain expert still remains crucial. A data mining approach that takes into account the knowledge representing the experience of domain experts is therefore much preferred and of great focus in current data mining research.

In a data mining context, a model is justifiable when it is in line with existing domain knowledge [36]. Therefore, for a model to be justi<sup>fi</sup>able it needs to be validated by a domain expert, which in turn means that the model should be comprehensible. The academically challenging problem of consolidating the automatically generated data mining knowledge with the knowledge re<sup>fl</sup>ecting experts' domain expertise, constitutes the knowledge fusion problem (see Fig. 4).

Table 2  
Classi<sup>fi</sup>cation model visualized by decision table.

<table><tr><td>1. Owns property?</td><td>2. Years client</td><td>3. Savings amount</td><td>1. Applicant = good</td><td>2. Applicant = bad</td></tr><tr><td rowspan="3">Yes</td><td rowspan="2">≤3</td><td>Low</td><td>-</td><td>×</td></tr><tr><td>High</td><td>×</td><td>-</td></tr><tr><td>&gt;3</td><td>-</td><td>×</td><td>-</td></tr><tr><td rowspan="2">No</td><td rowspan="2">-</td><td>Low</td><td>-</td><td>×</td></tr><tr><td>High</td><td>×</td><td>-</td></tr></table>

![](/api/attachments/9VRDHYAD/fulltext/images/7ba93823a33b9e2307138ad66a1d4895e0d8d67e9fe649cd5b13d2a04f3c39ae.jpg)  
Fig. 3. Pedagogical (a) and decomposional (b) rule extraction technique.

## 5.1. Taxonomy of constraints

Many types of constraints exist that a domain expert might want to incorporate. Taxonomy of possible domain constraints is shown in Table 3. Each type of constraint can be either mandatory, which we name a hard constraint, or simply preferred, which we name a soft constraint.

The <sup>fi</sup>rst type of constraint is the univariate constraint, applicable to one single variable which can be nominal or ordinal, resulting in respectively nominal and ordinal univariate constraints. For instance in a positive discrimination context, one might prefer women (e.g. for admittance, recruitment, etc.), thus the constraint being on the nominal variable Sex. Monotone ordinal univariate constraints are commonly referred to as monotonicity constraints, and are addressed in detail in the next section. An engineering example of a monotonicity constraint is that increasing the weight of a newly designed car, keeping all other variables equal, should yield an increased predicted fuel consumption. Non-monotone ordinal univariate constraints on the other hand require a non-monotone relationship in the ordinal variable in question. Piecewise monotone constraints allow a non-monotone constraint to be considered as several monotone constraints over the range of the variable. For instance, the domain expert might demand a piecewise monotone constraint on the Age variable, with decreasing probability of default for ages between 18 and 60, and an increasing probability of default for clients over 60 years old. Non-piecewise monotone constraints are those constraints that are non-monotone, and cannot be modeled as a piecewise monotone constraint. This constraint is the hardest to be ful<sup>fi</sup>lled, as it cannot be based on the commonly researched monotonicity constraint.

Table 3  
Taxonomy of possible constraints to incorporate.

<table><tr><td rowspan="4"></td><td colspan="4">Univariate</td><td rowspan="4">Multivariate</td></tr><tr><td rowspan="3">Nominal</td><td colspan="3">Ordinal</td></tr><tr><td rowspan="2">Monotone</td><td colspan="2">Non-monotone</td></tr><tr><td>Piecewise monotone</td><td>Non-piecewise monotone</td></tr><tr><td>Soft Hard</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/9VRDHYAD/fulltext/images/da4c6ae8cbad3bd4944eaaae4a3feadcb42e54ebd258e87b0866923b81bb674d.jpg)  
Fig. 4. The knowledge fusion process.

The second type of constraints are the multivariate constraints, which apply to multiple variables and can exist of all possible combinations of two or more univariate constraints that need to be ful<sup>fi</sup>lled simultaneously. For example, a preference for young, highly educated customers is such a combination of a monotone ordinal univariate and a nominal univariate constraint. Although these clients will tend to have a rather low income and savings, when considering the complete customer lifetime value they can appear to be very pro<sup>fi</sup>table to a bank. Incorporating such policies into modeling approaches is of great importance as well, but to the best of our knowledge not yet incorporated in data mining techniques. Additionally, the relative importance of a variable can also be included. For credit scoring, one might state that income is more important than age, and this relative importance should be present in the model. Finally and arguably most dif<sup>fi</sup>cult is the introduction of interactions between predictive variables (see e.g., Wellman [71]).

## 5.2. Monotonicity constraint

Monotonicity is the most encountered and researched domain constraint to be incorporated in a model [2,6,26,47,54,69]. This constraint demands that an increase in a certain input cannot lead to a decrease in the output.

Monotonicity constraints exist in almost any domain. For instance in a customer churn prediction context an increasing number of calls to the customer helpdesk yields a higher probability to churn. Therefore if a customer churn prediction model classi<sup>fi</sup>es two customers, who called recently three and <sup>fi</sup>ve times to the helpdesk,<sup>1</sup> as respectively a future churner and a non-churner, then this model violates the expected monotone relation between customer helpdesk calls and churn probability. Another example states that an increasing income of a loan applicant should yield a decreasing probability of default. Classifying two identical customers with a low and a high income as respectively a good and a bad customer is not in line with the expected monotone relation between income and probability to default on a loan. A monotonicity constraint can be de<sup>fi</sup>ned formally, similarly to Feelders and Pardoel [26]: given a data set $D = \{ { \bf x } ^ { i } , y ^ { i } \} _ { i = 1 } ^ { n }$ , with $\mathbf { x } ^ { i } = ( x _ { 1 } ^ { i } , x _ { 2 } ^ { i }$ $\begin{array} { r } { x _ { m } ^ { i } ) { \in } X { = } X _ { 1 } { \times } X _ { 2 } { \times } { \dots } X _ { m } , } \end{array}$ a partial ordering ≤ de<sup>fi</sup>ned over the input space X, and a linear ordering ≤ de<sup>fi</sup>ned over the space Y of class values y<sup>i</sup>, then the classi<sup>fi</sup>er $f \colon \mathbf { x } ^ { i } \mapsto ( \mathbf { x } ^ { i } ) \in Y$ is monotone if the next equation holds:

$$
\mathbf {x} ^ {i} \leq \mathbf {x} ^ {j} = > f (\mathbf {x} ^ {i}) \leq f (\mathbf {x} ^ {j}), \forall i, j (\text { or } f (\mathbf {x} ^ {i}) \geq f (\mathbf {x} ^ {j}), \forall i, j).\tag{4}
$$

It has been shown that adding monotonicity to learning algorithms may impair their performance [7].

## 5.3. Obtaining justifiable classification models

Although our taxonomy reveals that many types of domain constraints exist, to the best of our knowledge only the hard monotonicity constraint has been researched so far (with the exception of the AntMiner+ technique [36] which allows the imposition of soft constraints). Different approaches exist to incorporate monotone relations in classi<sup>fi</sup>cation models. These approaches can be divided in three categories, depending on the stage in the data mining process where monotonicity constraints are imposed, i.e. in the preprocessing phase, in the data mining phase, or in a post-processing phase.

In the <sup>fi</sup>rst category monotonicity is enforced in the preprocessing phase. Daniels and Velikova [16] transform non-monotone data into monotone data by a relabeling process. The main idea is to remove all non-monotone data pairs, by iteratively changing the class of the data instance for which the increase in correctly labeled instances is maximal. Improved accuracy and comprehensibility are reported when applying this relabeling procedure, which does not guarantee that monotone classi<sup>fi</sup>ers are constructed however.

In the second category monotonicity is incorporated during the actual data mining process. To incorporate monotonicity in classi<sup>fi</sup>- cation trees, Ben-David [6] uses a splitting criterion combining both standard impurity measures, such as entropy, and a non-monotonicity measure, which is de<sup>fi</sup>ned as the ratio between the actual number of non-monotonic pairs, and the maximum number of possible nonmonotonic pairs. The author reports a signi<sup>fi</sup>cant reduction in nonmonotonicity in the classi<sup>fi</sup>cation trees, without a signi<sup>fi</sup>cant decrease in accuracy. However, a completely monotone classi<sup>fi</sup>er is not guaranteed. Sill [54] on the other hand proposed a class of ANNs that can approximate any continuous monotone function to an arbitrary degree of accuracy. The proposed network has two hidden layers: the <sup>fi</sup>rst hidden layer has linear activation functions, these hidden nodes are grouped, and connected to a node in the second hidden layer, which calculates the maximum. Finally, the output unit computes the minimum over all groups. Monotonicity is guaranteed by imposing signs on the weights from the input to the <sup>fi</sup>rst hidden layer. Although this approach is straightforward and shows good results, the comprehensibility of such an ANN classi<sup>fi</sup>er is limited. Altendorf et al. [2] build monotone Bayesian networks by imposing inequality constraints on the network parameters. Monotonicity constraints on the parameter estimation problem are handled by imposing penalties in the likelihood function. The constructed models show to be as good or better in terms of generalization behavior than when imposing no constraints. In AntMiner+ monotonicity is obtained by restricting the search space of possible rules by imposing inequality signs. This approach is also able to include soft monotonicity constraints, by adapting a problem-dependent heuristic function [36]. Monotonicity will be respected more for higher values of the heuristic, which expresses the preference for a monotone relation as desired by the expert or user. Fig. 5 represents the probability that a loan applicant is classi<sup>fi</sup>ed as a good or bad client as a function of his income, for an increasing value of the heuristic. The higher the income, the lower the probability of default should be. However, for an increment of the heuristic of zero (i.e. the model without monotonicity constraints imposed) customers with a high income have a higher probability of default than customers with a low income. Gradually increasing the heuristic value shifts the probability curve towards the correct monotone relation.

Influence of heuristic adjustment on probability  
![](/api/attachments/9VRDHYAD/fulltext/images/b0f8dcf4784210863529ff273176b0522d789829b9b4f87156ac9d05b909a5d5.jpg)  
Fig. 5. The impact of a gradually increasing soft constraint on the probability of an applicant to default on a loan.

In the third category monotonicity is enforced during a postprocessing step. A simple generate-and-test approach is applied by Feelders [25]. Many different trees are generated (each time on another randomization of the data) and the most monotonicone is used. Feelders and Pardoel [26] achieve monotone classi<sup>fi</sup>cation models by pruning classi<sup>fi</sup>cation trees. This method prunes the parent of the non-monotone leaf that provides the largest reduction in number of non-monotonic leaf pairs. Again similar accuracy is reported, but with increased comprehensibility. For linear models, checking monotonicity comes down to verifying the sign of the regression parameters. By removing those variables for which the sign is not as expected and then re-estimating the parameters, a monotone model can be built (see e.g. Van Gestel et al. [63,64]). Alternatively, adding variables might reverse the sign, or estimating the coef<sup>fi</sup>cients with non-negative (positive) constraint can yield monotone linear models.

A <sup>fi</sup>nal remark related to obtaining monotone classi<sup>fi</sup>ers concerns the difference between expressing what is wanted, which should be done by the domain expert, and demanding these constraints, which is the focus of our research. Sometimes, data mining reveals interesting but unexpected patterns [53], which might not be detected when demanding justi<sup>fi</sup>ability constraints. Deciding when and for which variables to impose constraints is left entirely up to the domain expert.

It should be stressed that in many practical settings the justi<sup>fi</sup>ability and comprehensibility of a model are more important to the users of the model than the accuracy. Users will be reluctant, and probably even refuse to use a model that is unintuitive and not in line with domain knowledge, as we experienced in previous case studies in domains such as audit mining (predicting the going concern opinion as issued by the auditor) [39], business/ICT alignment prediction [15] and software fault prediction [65]. This has also been con<sup>fi</sup>rmed in the literature by, among others, Kodratoff [34] and Askira-Gelman [3]. Therefore, a successful implementation of a model heavily depends on these two factors. But whereas the comprehensibility of a model merely depends on the choice of modeling technique and can thus quite easily be chosen, the justi<sup>fi</sup>ability on the other hand is depending on the outcome of the modeling process, which is much harder to control. As discussed above, some modeling techniques allow one to include domain knowledge by imposing monotonicity constraints, enforcing the resulting model to be intuitively correct. But much more research is required to re<sup>fi</sup>ne and extend these techniques.

## 5.4. Measuring justifiability

As discussed in the previous section, several adaptations to existing classi<sup>fi</sup>cation techniques have been proposed to cope with justi<sup>fi</sup>ability. Yet, a measure to identify the extent to which a model conforms to the required constraints is still lacking. In this section a novel metric is introduced, which makes use of decision tables to provide a crisp performance measure for the critical justi<sup>fi</sup>ability measure.

In what follows, it is assumed that the data set consists of n variables V . A pro<sup>fi</sup>le $p r _ { i }$ for the variable $V _ { i }$ is de<sup>fi</sup>ned as the situation for which the variable settings differ only in variable $V _ { i } ,$ with different classes assigned for the different settings. In the decision table view, this corresponds to a situation of having at least two rows with the same values for all columns except the last. A formal de<sup>fi</sup>nition of the justi<sup>fi</sup>ability measure is given below, with n the number of variables, w a weight determining the relative importance of variable $V _ { i }$ such that higher penalties are given to inconsistencies in variables with higher weights, and the $I ( p r _ { i , j } )$ operator returning one if an inconsistency is present in the $j ^ { t h }$ pro<sup>fi</sup>le of variable i, and zero otherwise. Note that the weight $w _ { i }$ of variables $V _ { i }$ that are not (expected to be) monotonically related to the target variable, is set equal to zero. Hence these variables do not have an impact on the resulting measure, as would be logically expected. The total number of pro<sup>fi</sup>les for variable $V _ { i }$ is denoted by |pr |. As we will demonstrate, inconsistencies of a model with an expected relation are easily detected by using decision tables.

$$
\text { Justifiability } = 1 - \sum_ {i = 1} ^ {n} \overbrace {w _ {i} \sum_ {j = 1} ^ {| p r _ {i} |} \frac {1}{| p r _ {i} |} \cdot I (p r _ {i j})} ^ {\text { overall   penalty   penalty   for   } V _ {j}}\tag{5}
$$

The justi<sup>fi</sup>ability metric is given by Eq. (5), with $\sum { _ { i = 1 } ^ { n } w _ { i } } = 1 ,$ , such that $0 \leq$ Justi<sup>fi</sup>ability ≤1. Each variable can bring about a penalty of maximum $w _ { i } ,$ which insures that the justi<sup>fi</sup>ability measure lies between zero and one. The weight parameter $w _ { i }$ can be set in the following ways:

1. Statistically based, with information theoretic measures such as for instance Information Value (IV), Cramer's V (CV), Information Gain (IG), or Gain ratio (GR) [60]:

• The Information Value of a categorical variable V with values v, whereby the class variable Y with values $y$ is either positive $( y = P )$ or negative $( y = N )$ , is calculated as follows:

$$
I V = \sum_ {v \in V _ {i}} (p (v | y = N) - p (v | y = P)) \log \frac {p (v | y = N)}{p (v | y = P)},\tag{6}
$$

whereby $p ( \boldsymbol { v } | \boldsymbol { y } = P )$ and $p ( \boldsymbol { v } | \boldsymbol { y } = N )$ represent the proportion of instances with respectively positive and negative class labels falling into category v of variable $V _ { i \cdot }$ High information values indicate that the positive and negative instances are unevenly distributed among the different categories, and as such the variable is very well able to explain the target variable.

• Cramer's V statistic is based on the $\chi ^ { 2 }$ statistic, which measures the dissimilarity between the reported number of observations of the values of a variable $V _ { i }$ and the expected number assuming that the variable is unrelated to the class variable. This test statistic is de<sup>fi</sup>ned as follows:

$$
\chi^ {2} = \sum_ {v \in V _ {i}} \sum_ {y \in Y} \frac {n _ {y v} - \frac {n _ {\cdot v} n _ {y \cdot}}{n ^ {2}}}{\frac {n _ {\cdot v} n _ {y \cdot}}{n}},\tag{7}
$$

with n the total number of instances, $n _ { y v }$ the number of instances with class label y $( y = P \ o \ r y = N )$ falling into category v of variable $V _ { i } , n . .$ the total number of instances falling into category v of $V _ { i } ,$ and $n _ { y }$ the total number of instances with class label $y .$ Higher values of the test statistic indicate that the independence assumption is less likely and hence the variable has good predictive power. Cramer's V is then de<sup>fi</sup>ned as follows:

$$
C V = \sqrt {\frac {\chi^ {2}}{n}}\tag{8}
$$

Cramer's V always lies between zero and one, and values closer to one indicate variables that are strongly related with the class variable.

• The Information Gain or Mutual Information is the entropy reduction in the class variable Y after having observed variable $V _ { i \cdot }$ The entropy of the class variable Y is de<sup>fi</sup>ned as follows:

$$
H (Y) = - \sum_ {y \in Y} p (y) \log_ {2} p (y),\tag{9}
$$

whereby the summation ranges over all the possible values y of Y. The entropy will be maximal when both proportions p(y) are the same, and minimal when one of the proportions becomes 100%. Hence, the entropy H(Y) measures the impurity or disorder in the data set with respect to the variable Y. The entropy after having observed variable $V _ { i }$ with possible values v is then given by:

$$
H (Y | X) = - \sum_ {v \in V _ {i}} p (v) \sum_ {y \in Y} p (y | v) \log_ {2} p (y | v).\tag{10}
$$

The entropy reduction in the class variable Y after having observed variable $V _ { i }$ is the Information Gain:

$$
I G = H (Y) - H (Y | V _ {i}).\tag{11}
$$

Again, the higher the Information Gain, the better the theoretical ability of the variable to explain the target variable.

• The Gain ratio adjusts the IG measure in order to compensate for its tendency to favor attributes with many values. It is de<sup>fi</sup>ned as follows:

$$
G R = \frac {I G}{- \sum_ {v \in V _ {i}} p (v) \log_ {2} p (v)}.\tag{12}
$$

The values of these measures can be normalized to sum up to one, and then be used as weights in the justi<sup>fi</sup>ability metric. Other information theoretic measures can be used as well [60]. As a simple, straightforward alternative, equal weights can be assigned to each variable that is expected to vary monotonically with the target variable.

## 2. Domain expert based:

• By initializing the weights using the statistically based measures, and adjusting these initial weights if deemed necessary.

• By using a ranking of the variables, based on which the weights are then determined. The variables can be ranked on their ability to predict the target class, for instance by using the information theoretic measures introduced above. The weights are then set by a domain expert, respecting the induced ranking, with higher weights for higher ranked variables.

• Immediately determining the weights based on expertise and intuition.

Using a statistically based manner to determine the weights of the variables results in an entirely objective metric to measure the justi<sup>fi</sup>ability of a classi<sup>fi</sup>cation model, which can be calculated without any intervention from a domain expert. This rules out any subjectivity, but consequently does not allow incorporating (subjective) domain knowledge about the relative importance of variables and the desired monotone relations with the target variable. The metric will not be tailor made to the context in which it is applied. Determining the weights in a domain expert based manner on the other hand implies that the metric becomes partially subjective, in the sense that the resulting justi<sup>fi</sup>ability measure is dependent on the domain expert. The possibility to set or adjust the weights manually allows the domain expert to <sup>fi</sup>ne-tune the metric to his or her needs, in order to incorporate the conceived differences in importance of the preferred monotone relations. As a result the metric will re<sup>fl</sup>ect to what extent a classi<sup>fi</sup>cation model is in line with the preferences of the domain expert. Imposing monotonicity constraints inherently implies expert based, subjective domain knowledge to be incorporated in a model. Therefore one might reasonably expect the expert that imposes these constraints to have an opinion or knowledge about the relative importance of the monotonicity constraints he imposes. A domain expert based manner of determining the weights allows expressing these opinions and this knowledge. Independently of how the weights are set, whether it be statistically based or domain expert based, the set of weights has to be determined in a uniform, coherent way in order to allow a correct comparison of different classi<sup>fi</sup>cation models.

## Table 4

Discrepancies in the classi<sup>fi</sup>cation model, visualized by a decision table

<table><tr><td rowspan="13">Purposefurniture/business</td><td rowspan="5">Duration≤15m</td><td rowspan="4">Checking Account&lt;0€</td><td>Savings Account</td><td>Credit History</td><td>Bad</td><td>Good</td></tr><tr><td rowspan="2">&lt;250 €</td><td>no credits taken/allcredits paid back duly</td><td rowspan="2">×-</td><td rowspan="2">-×</td></tr><tr><td>critical account</td></tr><tr><td>≥250 €</td><td>-</td><td>-</td><td>×</td></tr><tr><td>≥0€</td><td>-</td><td>-</td><td>-</td><td>×</td></tr><tr><td rowspan="8">&gt;15m</td><td rowspan="4">&lt;0€</td><td>&lt;250 €</td><td>-</td><td>×</td><td>-</td></tr><tr><td rowspan="2">≥250 and &lt;500 €</td><td>no credits taken/allcredits paid back duly</td><td rowspan="2">×-</td><td rowspan="2">-×</td></tr><tr><td>all credits at this bankpaid back duly orcritical account</td></tr><tr><td>≥500 €</td><td>-</td><td>-</td><td>×</td></tr><tr><td rowspan="3">≥0 and &lt;100 €</td><td rowspan="2">&lt;500 €</td><td>no credits taken/allcredits paid back duly</td><td rowspan="2">×-</td><td rowspan="2">-×</td></tr><tr><td>all credits at this bankpaid back duly orcritical account</td></tr><tr><td>≥500 €</td><td>-</td><td>-</td><td>×</td></tr><tr><td>≥100 €</td><td>-</td><td>-</td><td>-</td><td>×</td></tr><tr><td rowspan="10">car/retraining orothers</td><td rowspan="3">≤15m</td><td rowspan="3">-</td><td rowspan="2">&lt;500 €</td><td>no credits taken/allcredits paid back duly</td><td rowspan="2">×-</td><td rowspan="2">-×</td></tr><tr><td>critical account</td></tr><tr><td>≥500 €</td><td>-</td><td>-</td><td>×</td></tr><tr><td rowspan="7">&gt;15m</td><td rowspan="4">&lt;0 €</td><td>&lt;250 €</td><td>-</td><td>×</td><td>-</td></tr><tr><td rowspan="2">≥250 and &lt;500 €</td><td>no credits taken/allcredits paid back duly</td><td rowspan="2">×-</td><td rowspan="2">-×</td></tr><tr><td>critical account</td></tr><tr><td>≥500 €</td><td>-</td><td>-</td><td>×</td></tr><tr><td rowspan="3">≥0€</td><td rowspan="2">&lt;500 €</td><td>no credits taken/allcredits paid back duly</td><td rowspan="2">×-</td><td rowspan="2">-×</td></tr><tr><td>critical account</td></tr><tr><td>≥500 €</td><td>-</td><td>-</td><td>×</td></tr></table>

Setting the weights is a dif<sup>fi</sup>cult yet necessary exercise in the justi<sup>fi</sup>ability calculations. Setting the weights completely statistically based, or relying only on the domain expert's intuition, are just two extremes of a spectrum of possibilities. By only using statistics, one will mimic the relative importance of the variables in the data set exactly. Of course, due to the lack of perfect data quality (noise, limited data availability, etc.), one can not completely rely solely on these measures. For example, if a variable is not correlated at all with the target variable, this does not mean that the weight should therefore be set to zero. For the same reason, if only one variable perfectly predicts the target variable, it should not be concluded that the weight of that variable is one, and all others zero. On the other hand, only relying on the domain expert's opinion neither is to be recommended, since the expert's intuition about the impact of different settings will be limited. From that perspective, approaches between these two extremes are sensible, where statistically based weights are adjusted according to the expert's opinion, or where an expert chooses among a set of possible weight con<sup>fi</sup>gurations. To determine the impact of changing the weights, it is surely sensible to combine this with sensitivity analysis, in order to investigate the impact on the justi<sup>fi</sup>ability metric of (small) changes in the weight settings.

The justi<sup>fi</sup>ability measure can also be used for linear classi<sup>fi</sup>ers, without the use of decision tables: there exactly one pro<sup>fi</sup>le exists for each variable. An inconsistency takes place if the sign of variable V does not correspond to the expected sign. To determine the weights, a

## Table 5

Weights of variables, de<sup>fi</sup>ned as normalized Gain ratios.

<table><tr><td></td><td>Gain ratio</td><td> $w_i$ </td></tr><tr><td>Checking account</td><td>0.0526</td><td>0.1529</td></tr><tr><td>Duration</td><td>0.2366</td><td>0.6879</td></tr><tr><td>Credit history</td><td>0.0255</td><td>0.0741</td></tr><tr><td>Purpose</td><td>0.01258</td><td>0.03657</td></tr><tr><td>Savings account</td><td>0.01666</td><td>0.04843</td></tr><tr><td>Sum</td><td>0.34394</td><td>1</td></tr></table>

Table 6  
Variables in the RIPPER rule-set and the sign of the expected relation with churn.

<table><tr><td>Feature</td><td>Constraint</td><td>What?</td><td>Weight</td></tr><tr><td>eqpdays</td><td>+</td><td>Number of days of the current equipment</td><td>2/3</td></tr><tr><td>changem</td><td>-</td><td>Change in minutes of use</td><td>1/3</td></tr><tr><td>mou</td><td></td><td>Mean monthly minutes of use</td><td>0</td></tr><tr><td>recchge</td><td></td><td>Mean total recurring charge</td><td>0</td></tr></table>

Table 7  
RIPPER rule-set without monotonicity constraints.

<table><tr><td>If eqpdays≥303 and eqpdays≤362then class=churn</td></tr><tr><td>If eqpdays≥304 and changem≤-74.5 and mou≤420.25then class=churn</td></tr><tr><td>If eqpdays≥364 and recchrgle≤34.98then class=churn</td></tr></table>

similar approach as for the rule-based classi<sup>fi</sup>ers can be followed. For the statistically proposed weights, one might use the (normalized) partial correlation coef<sup>fi</sup>cients, which is the correlation when all other variables are kept at <sup>fi</sup>xed values [33]. Other possibilities to determine the importance of a variable in a model include the (normalized) regression coef<sup>fi</sup>cients and the p-values of these coef<sup>fi</sup>cients.

Before explaining the metric in detail, we should note that since we measure an inherently subjective concept, testing with human users and comparing the proposed metric with the user's values (referred to as real human interest [11]), can provide useful guidelines for the weight settings, and the metric as a whole. Such experiments are conducted in e.g. Billman and Davila [8], Ohsaki et al. [42], Pazzani [45], Pazzani and Bay [46], but are beyond the scope of this paper.

Our justi<sup>fi</sup>ability measure will be explained in more detail using two examples from respectively the credit scoring and customer churn prediction domain. In the <sup>fi</sup>rst example, the weights are set in a statistical based manner, while the second example follows a domain expert based approach.

## 5.4.1. Credit scoring example

Table 4 reports the decision table, corresponding to the rule-set inferred by AntMiner+ on the German credit scoring data set, as published in Ref. [36]. In this credit scoring example, we have a total of 6 pro<sup>fi</sup>les for the Credit History variable, which are numbered in Table 4 and are all inconsistent. For all other variables, no inconsistencies exist. Therefore, assuming the weights being taken as given by the normalized Gain ratios in Table 5, the justi<sup>fi</sup>ability of this classi<sup>fi</sup>er is given by:

$$
\begin{array}{r l} \text {Justifiability} & = 1 - 0. 0 7 4 1 \times \left[ \frac {1}{6} + \frac {1}{6} + \frac {1}{6} + \frac {1}{6} + \frac {1}{6} + \frac {1}{6} \right] \\ & = 0. 9 2 5 9 = 9 2. 5 9 \%. \end{array}
$$

Notice that this measure is very high, although all pro<sup>fi</sup>les of the Credit History variable are incorrect. This is the result of the very low weight given to this variable. An expert might decide to put some lower bound on the possible weight, or to simply adjust these weights.

In the case of a linear classi<sup>fi</sup>er, a similar approach can be taken. Suppose we obtain the following (arti<sup>fi</sup>cial) linear classi<sup>fi</sup>cation model for the credit scoring data set, with z=+1 denoting a good customer and z=−1 a bad customer:

$$
z = \operatorname{sgn} (0. 7 \times \text { income } - 0. 4 \times \text { savings } + 0. 2 \times \text { checking } + 0. 1 \times \text { age }).
$$

We expect that a higher income will yield a higher probability of being a good customer, and therefore the expected sign for the variable income is positive. Similarly we expect positive signs for savings and checking amount. For age we have no expectation, while the linear classi<sup>fi</sup>cation model shows an unwanted sign for savings. For simplicity reasons, we use the normalized regression coef<sup>fi</sup>cient as weight $( \mathrm { e . g . } \ w _ { \mathrm { i n c o m e } } = \frac { 0 . 7 } { 0 . 7 \ + 0 . 4 \ + 0 . 2 \ + 0 . 1 } = 0 . 5 )$ which results in the following justi<sup>fi</sup>ability:

Table 8  
Decision table corresponding to the churn prediction rule-set

<table><tr><td>changem</td><td>recchrg</td><td>mou</td><td>eqpdays</td><td>churner</td><td>non-churner</td></tr><tr><td rowspan="7">≤-74.5</td><td rowspan="2">≤34.98</td><td rowspan="2">—</td><td>&lt;303</td><td>—</td><td>×</td></tr><tr><td>≥303</td><td>×</td><td>—</td></tr><tr><td rowspan="5">&gt;34.98</td><td rowspan="2">≤420.25</td><td>&lt;303</td><td>—</td><td>×</td></tr><tr><td>≥303</td><td>×</td><td>—</td></tr><tr><td rowspan="3">&gt;420.25</td><td>&lt;303</td><td>—</td><td>×</td></tr><tr><td>≥303and≤362</td><td>×</td><td>—</td></tr><tr><td>&gt;362</td><td>—</td><td>×</td></tr><tr><td rowspan="5">&gt;-74.5</td><td rowspan="2">≤34.98</td><td rowspan="2">—</td><td>&lt;303</td><td>—</td><td>×</td></tr><tr><td>≥303</td><td>×</td><td>—</td></tr><tr><td rowspan="3">&gt;34.98</td><td rowspan="3">—</td><td>&lt;303</td><td>—</td><td>×</td></tr><tr><td>≥303and ≤362</td><td>×</td><td>—</td></tr><tr><td>&gt;362</td><td>—</td><td>×</td></tr></table>

$$
\begin{array}{r l} \text {Justifiability} & = 1 - \left[ 0. 5 \times I (p r _ {\text {income}}) + 0. 2 9 \times I (p r _ {\text {savings}}) \right. \\ & \quad \left. + 0. 1 4 \times I (p r _ {\text {checking}}) + 0. 0 7 \times I (p r _ {\text {age}}) \right] \\ & = 1 - [ 0 + 0. 2 9 + 0 + 0 ] \\ & = 0. 7 1 = 7 1 \%. \end{array}
$$

## 5.4.2. Customer churn prediction example

The second example deals with the classi<sup>fi</sup>cation of customers of a wireless telecom operator as having a low or high propensity to churn. Table 7 shows a classi<sup>fi</sup>cation rule-set induced by RIPPER [13] on a reallife wireless telecom operator customer churn dataset.<sup>2</sup> Table 6 explains the variables that are used in the model, the nature of the expected relation with the target variable, i.e. whether a customer will churn or not, and the weights assigned to the variables by a domain expert. The variable eqpdays is valued double as important as changem, since it is of great importance for customer relations management. Both recchrge and mou have weights of zero since no speci<sup>fi</sup>c relations are expected or desired between these variables and the target variable.

According to domain knowledge the number of days of the current equipment is expected to be positively related with the probability to churn, while the change in minutes of use (with a negative value for decreasing use) is expected to be inversely related with the probability to churn, i.e. the higher the value of the variable, the lower the probability to churn is expected to be.

The rule-based classi<sup>fi</sup>er has (after pruning) a total of three rules to predict whether a customer will churn or not, which are reported in Table 7. These three rules result in the decision table as reported by Table 8, with a total of <sup>fi</sup>ve pro<sup>fi</sup>les for the eqpdays variable.

Although the rule-set seems intuitively correct, the decision table reveals that two of these <sup>fi</sup>ve pro<sup>fi</sup>les are in contradiction with the expected relation between eqpdays and churn indicated in Table 6. Both pro<sup>fi</sup>les 3 and 5 state that customers with the same characteristics for changem, recchrge, and mou, but different times since the last headset was issued, the ones with the longer time since the last new equipment was issued will not churn, while the ones with the newer headset will churn. This is counterintuitive, and therefore $I ( p r _ { \mathrm { e q p d a y s } , 3 } ) { = } 1$ and $I ( p r _ { \mathrm { e q p d a y s } , 5 } ) = 1$ . For the other pro<sup>fi</sup>les the domain constraint is ful<sup>fi</sup>lled, therefore $I ( p r _ { \mathrm { r e c a l l } , i } ) = 0$ , with $i = 1 , 2 , 4 .$ As could be checked in the decision table by placing this variable in the last column, all pro<sup>fi</sup>les for the changem variable comply with the monotonicity constraint, resulting in the following justi<sup>fi</sup>ability measure:

$$
\begin{aligned} \text{Justifiability} & = 1 - \left[ \frac {2}{3} \times \left(\frac {1}{5} I \left(p r _ {\text {recall}, 3}\right) + \frac {1}{5} I \left(p r _ {\text {recall}, 5}\right)\right) \right] \\ & = 1 - \left[ \frac {2}{3} \times \left(\frac {1}{5} \times 1 + \frac {1}{5} \times 1\right) \right] = 0.7333 = 73.33\%. \end{aligned}
$$

## 6. Conclusion

In many application domains comprehensibility is an important requirement of a classi<sup>fi</sup>cation model. Several approaches have been proposed in the literature to come to such models, from simple rule induction techniques, to advanced incremental approaches. More recently, the importance of justi<sup>fi</sup>ability has been acknowledged by a number of researchers, in the form of monotonicity constraints imposed on the resulting model. As shown by the taxonomy presented in this paper however, many other constraints exist that can be included in the learning algorithm.

Furthermore, this paper introduces a novel metric for justi<sup>fi</sup>ability. The metric allows to assess and compare the intuitiveness of classi<sup>fi</sup>ers, and also to establish a justi<sup>fi</sup>ability threshold which permits to demand a minimum justi<sup>fi</sup>ability before accepting and implementing a classi<sup>fi</sup>cation model in a decision support system. Thresholds can even be set at 100%, requiring a model that is completely in line with business expectation.

Practical experience has shown that in many cases the comprehensibility and justi<sup>fi</sup>ability are of much greater importance to the users of a model than the predictive accuracy. By providing comprehensible, justi<sup>fi</sup>able classi<sup>fi</sup>cation models, they become acceptable in domains where previously such models were deemed too theoretical and incomprehensible. As such, new opportunities emerge for data mining.

## Acknowledgements

We extend our gratitude to the Flemish Research Council for <sup>fi</sup>nancial support (FWO postdoctoral research grant, Odysseus grant B.0915.09), and the National Bank of Belgium (NBB/10/006).

## References

[1] D.W. Aha, D.F. Kibler, M.K. Albert, Instance-based learning algorithms, Machine Learning 6 (1991) 37–66.

[2] E. Altendorf. E. Restificar. T. Dietterich. Learning from sparse data by exploiting monotonicity constraints, in: Proceedings of the 21st Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, Edinburgh, Scotland, 2005.

[3] I. Askira-Gelman, Knowledge discovery: comprehensibility of the results, HICSS'98: Proceedings of the Thirty-First Annual Hawaii International Conference on System Sciences, Volume 5, IEEE Computer Society, Washington, DC, USA 1998, p. 247.

[4] B. Baesens, R. Setiono, C. Mues, J. Vanthienen, Using neural network rule extraction and decision tables for credit-risk evaluation, Management Science 49 (2003) 312–329.

[5] B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, J. Vanthienen, Benchmarking state-of-the-art classi<sup>fi</sup>cation algorithms for credit scoring, The Journal of the Operational Research Society 54 (2003) 627–635.

[6] A. Ben-David, Monotonicity maintenance in information-theoretic machine learning algorithms, Machine Learning 19 (1995) 29–43.

[7] A. Ben-David, L. Sterling, T. Tran, Adding monotonicity to learning algorithms may impair their accuracy, Expert Systems with Applications 36 (2009) 6627–6634.

[8] D. Billman, D. Davila, Consistency is the hobgoblin of human minds: people care but concept learning models do not, in: Proceedings of the 17th Annual Conference of the Cognitive Science Society, 1995, pp. 188–193.

[9] C. Bishop, Neural Networks for Pattern Recognition, Oxford University Press, Oxford, UK, 1996.

[10] L. Breiman, J. Friedman, R. Olshen, C. Stone, Classi<sup>fi</sup>cation and Regression Trees, Chapman & Hall, New York, 1984.

[11] D. Carvalho, A. Freitas, N. Ebecken, Evaluating the correlation between objective rule interestingness measures and real human interest, in: A. Jorge, L. Torgo, P. Brazdil, R. Camacho, J. Gama (Eds.), PKDD, Lecture Notes in Computer Science, volume 3721, Springer, 2005, pp. 453–461.

[12] P. Clark, T. Niblett, The CN2 induction algorithm, Machine Learning 3 (1989) 261–283.

[13] W.W. Cohen, Fast effective rule induction, in: A. Prieditis, S. Russell (Eds.), Proc. of the 12th International Conference on Machine Learning, Morgan Kaufmann, Tahoe City, CA, 1995, pp. 115–123.

[14] N. Cristianini, J. Shawe-Taylor, An Introduction to Support Vector Machines and Other Kernel-Based Learning Methods, Cambridge University Press, New York, NY, USA, 2000.

[15] B. Cumps, D. Martens, M. De Backer, S. Viaene, G. Dedene, R. Haesen, M. Snoeck, B. Baesens, Inferring rules for business/ict alignment using ants, Information Management 46 (2009) 116–124.

[16] H. Daniels, M. Velikova, Derivation of monotone decision models from noisy data, IEEE Transactions on Systems, Man, and Cybernetics. Part C: Applications and Reviews 36 (2006) 705–710.

[17] P. Domingos, The role of occam's razor in knowledge discovery, Data Mining and Knowledge Discovery 3 (1999) 409–425

[18] R. Duda, P. Hart, D. Stork, Pattern Classi<sup>fi</sup>cation, second editionJohn Wiley and Sons, 2001.

[19] J. Egan, Signal Detection Theory and ROC Analysis. Series in Cognition and Perception, Academic Press, New York, 1975.

[20] T. Fawcett, Using rule sets to maximize roc performance, IEEE International Conference on Data Mining, 0, 2001, p. 131.

[21] T. Fawcett, An introduction to roc analysis, Pattern Recognition Letters 27 (2006) 861–874.

[22] T. Fawcett, Prie: a system for generating rulelists to maximize roc performance, Data Mining and Knowledge Discovery 17 (2008) 207–224.

[23] T. Fawcett, F. Provost, Adaptive fraud detection, Data Mining and Knowledge Discovery 1–3 (1997) 291–316.

[24] Federal Trade Commission for the Consumer, Facts for consumers: equal credit opportunity, Technical Report, FTC, March 1998.

[25] A. Feelders, Prior knowledge in economic applications of data mining, Proceedings of the Fourth European Conference on Principles and Practice of Knowledge Discovery in Data Bases, Lecture Notes in Computer Science, volume 1910, Springer, 2000, pp. 395–400.

[26] A. Feelders, M. Pardoel, Pruning for monotone classi<sup>fi</sup>cation trees, Advances in Intelligent Data Analysis V, volume 2810, Springer, 2003, pp. 1–12.

[27] D. Hand, Pattern Detection and Discovery, in: D. Hand, N. Adams, R. Bolton (Eds.), Pattern detection and discovery, Lecture Notes in Computer Science, volume 2447, Springer, 2002, pp. 1–12.

[28] D. Hand, Protection or privacy? Data mining and personal data, Paci<sup>fi</sup>c-Asia Conference, PAKDD, Lecture Notes in Computer Science, volume 3918, Springer, 2006, pp. 1–10.

[29] D. Hand, Measuring classi<sup>fi</sup>er performance: a coherent alternative to the area under the roc curve, Machine Learning 77 (2009) 103–123.

[30] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning, Data Mining, Inference, and Prediction, Springer, 2001.

[31] J. Huysmans, C. Mues, B. Baesens, J. Vanthienen, An Empirical Evaluation of the Comprehensibility of Decision Table, Tree and Rule Based Predictive Models, 2007.

[32] I. Huysmans. B. Baesens. D. Martens. K. Denys. I. Vanthienen, New trends in data mining, Tijdschrift voor economie en Management, volume L, 2005, pp. 697–711

[33] D. Kleinbaum, L. Kupper, K.E. Muller, A. Nizam, Applied Regression Analysis and Multivariable Methods, Duxbury Press, 1997.

[34] Y. Kodratoff, The comprehensibility manifesto, KDD Nuggets (94:9), 1994.

[35] O.O. Maimon, L. Rokach, Decomposition Methodology For Knowledge Discovery And Data Mining: Theory And Applications (Machine Perception and Arti<sup>fi</sup>cial Intelligence), World Scienti<sup>fi</sup>c Publishing Company, 2005.

[36] D. Martens, M. De Backer, R. Haesen, B. Baesens, C. Mues, J. Vanthienen, Ant-based approach to the knowledge fusion problem, Proceedings of the Fifth International Workshop on Ant Colony Optimization and Swarm Intelligence, Lecture Notes in Computer Science, Springer, 2006, pp. 85–96.

[37] D. Martens, B. Baesens, T. Van Gestel, J. Vanthienen, Comprehensible credit scoring models using rule extraction from support vector machines, European Journal of Operational Research 183 (2007) 1466–1476.

[38] D. Martens, M. De Backer, R. Haesen, M. Snoeck, J. Vanthienen, B. Baesens, Classi<sup>fi</sup>cation with ant colony optimization, IEEE Transaction on Evolutionary Computation 11 (2007) 651–665.

[39] D. Martens, L. Bruynseels, B. Baesens, M. Willekens, J. Vanthienen, Predicting going concern opinion with data mining, Decision Support Systems 45 (2008) 765–777.

[40] D. Martens, T. Van Gestel, B. Baesens, Decompositional rule extraction from support vector machines by active learning, JFFE Transactions on Knowledge and Data Engineering 21 (2009) 178–191.

[41] R. Michalski, A theory and methodology of inductive learning, Arti<sup>fi</sup>cial Intelligence 20 (1983) 111–161.

[42] M. Ohsaki, S. Kitaguchi, K. Okamoto, H. Yokoi, T. Yamaguchi, Evaluation of rule interestingness measures with a clinical dataset on hepatitis PKDD'04: Proceedings of the 8th European Conference on Principles and Practice of Knowledge Discovery in Databases, Springer-Verlag New York, Inc., New York, NY, USA, 2004, pp. 362–3738, volume.

[43] L. Passmore, J. Goodside, L. Hamel, L. Gonzales, T. Silberstein, J. Trimarchi, Assessing decision tree models for clinical in-vitro fertilization data, Technical

Report TR03-296, Dept. of Computer Science and Statistics, University of Rhode Island, 2003.

[44] M. Pazzani, In<sup>fl</sup>uence of prior knowledge on concept acquisition: experimental and computational results, Journal of Experimental Psychology. Learning, Memory, and Cognition 17 (1991) 416–432.

[45] M. Pazzani, Learning with globally predictive tests, in: Discovery Science, 1998, pp. 220–231.

[46] M. Pazzani, S. Bay, The independent sign bias: gaining insight from multiple linear regression, in: Proceedings of the Twenty First Annual Conference of the Cognitive Science Society, 1999, pp. 525–530.

[47] M. Pazzani, S. Mani, W. Shankle, Acceptance by medical experts of rules generated by machine learning, Methods of Information in Medicine 40 (2001) 380–385.

[48] F. Provost, T. Fawcett, R. Kohavi, The case against accuracy estimation for comparing classi<sup>fi</sup>ers, in: J. Shavlik (Ed.), Proceedings of the Fifteenth International Conference on Machine Learning (ICML), Morgan Kaufmann, San Francisco, CA, U.S.A, 1998, pp. 445–453.

[49] J.R. Quinlan, C4.5 Programs for Machine Learning, Morgan Kaufmann Publishers Inc, San Francisco, CA, USA, 1993.

[50] J. Seifert, Data mining and homeland security: an overview, CRS Report for Congress, 2006.

[51] R. Setiono, B. Baesens, C. Mues, Risk management and regulatory compliance: a data mining framework based on neural network rule extraction, Proceedings of the International Conference on Information Systems, ICIS, 2006.

[52] R. Setiono, B. Baesens, C. Mues, Recursive neural network rule extraction for data with mixed attributes, IEEE Transactions on Neural Networks 19 (2008) 299–307.

[53] A. Silberschatz, A. Tuzhilin, On subjective measures of interestingness in knowledge discovery, in: KDD, 1995, pp. 275–281.

[54] J. Sill, Monotonic networks, Advances in Neural Information Processing Systems, volume 10, The MIT Press, 1998.

[55] E. Sommer, An approach to quantifying the quality of induced theories, in: C. Nedellec (Ed.), Proceedings of the IJCAI Workshop on Machine Learning and Comprehensibility, 1995.

[56] J.A.K. Suykens, T.V. Gestel, J.D. Brabanter, B. De Moor, J. Vandewalle, Least Squares Support Vector Machines, World Scienti<sup>fi</sup>c, Singapore, 2002.

[57] J. Swets, R. Pickett, Evaluation of Diagnostic Systems: Methods from Signal Detection Theory, Academic Press, New York, 1982.

[58] P.N. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, Pearson Education, Boston, MA, 2006.

[59] L. Thomas, D. Edelman, J. Crook (Eds.), Credit Scoring and its Applications, SIAM, Philadelphia, PA, 2002.

[60] T. Van Gestel, B. Baesens, Credit Risk Management, Oxford University Press, Basi Concepts, 2009.

[61] T. Van Gestel, J. Suykens, B. Baesens, S. Viaene, J. Vanthienen, G. Dedene, B. De Moor, J. Vandewalle, Benchmarking least squares support vector machine classi<sup>fi</sup>ers, Machine Learning 54 (2004) 5–32.

[62] T. Van Gestel, B. Baesens, P. Van Dijcke, J. Suykens, J. Garcia, T. Alderweireld, Linear and nonlinear credit scoring by combining logistic regression and support vector machines, Journal of Credit Risk 1 (2005).

[63] T. Van Gestel, B. Baesens, P. Van Dijcke, J. Garcia, J. Suykens, J. Vanthienen, A process model to develop an internal rating system: sovereign credit ratings, Decision Support Systems 42 (2006) 1131-1151.

[64] T. Van Gestel, D. Martens, B. Baesens, D. Feremans, J. Huysmans, J. Vanthienen, Forecasting and analyzing insurance companies' ratings, International Journal of Forecasting 23 (2007) 513–529.

[65] O. Vandecruys, D. Martens, B. Baesens, C. Mues, M. De Backer, R. Haesen, Mining software repositories for comprehensible software fault prediction models, The Journal of Systems and Software 81 (2008) 823–839.

[66] J. Vanthienen, C. Mues, A. Aerts, An illustration of veri<sup>fi</sup>cation and validation in the modelling phase of KBS development, Data & Knowledge Engineering 27 (1998) 337–352.

[67] J. Vanthienen, C. Mues, G. Wets, K. Delaere, A tool-supported approach to intertabular veri<sup>fi</sup>cation, Expert Systems with Applications 15 (1998) 277–285.

[68] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer-Verlag New York Inc., New York, NY, USA, 1995.

[69] M. Velikova, H. Daniels, A. Feelders, Solving partially monotone problems with neural networks, Proceedings of the International Conference on Neural Networks, Vienna, Austria, 2006.

[70] W. Verbeke, D. Martens, C. Mues, B. Baesens, Building comprehensible customer churn prediction models with advanced rule induction techniques, Expert Systems with Applications 38 (2011) 2354–2364.

[71] M. Wellman, Fundamental concepts of qualitative probabilistic networks, Arti<sup>fi</sup>cial Intelligence 44 (1990) 257–303.

[72] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques with Java Implementations, Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 2000.

![](/api/attachments/9VRDHYAD/fulltext/images/501533f776a7af7a3c6f93a014db361668d986413ee61788da413b7fc771608f.jpg)

David Martens is assistant professor at the University of Antwerp. He received a PhD in Applied Economic Sciences from K.U.Leuven, Belgium, in 2008. He also received a Master's degree in civil engineering at the Computer Science Department from K.U.Leuven, Belgium in 2003; and a Master of Business Administration in 2005 from Reims Management School, France. His research is mainly focused on the development of comprehensible data mining techniques, the use of swarm intelligence for data mining, and mining networked data for marketing and <sup>fi</sup>nance applications.

![](/api/attachments/9VRDHYAD/fulltext/images/d5efee10f844af52c56f52b4f766dda033e3a0229490a42081a1e2d32f76ab58.jpg)

Jan Vanthienen received the Ph.D. degree in applied economics (information systems) from the Katholieke Universiteit Leuven (K.U.Leuven), Leuven, Belgium. He is a Full Professor of information systems with the Depart ment of Decision Sciences and Information Management, K.U. Leuven. He is also Chairholder of the PriceWaterhouseCoopers Chair on E-Business at K.U. Leuven. He is the author or coauthor of numerous papers published in international journals and conference proceedings. His current research interests include information and knowledge management, business intelligence and business rules, and information systems analysis and design.

![](/api/attachments/9VRDHYAD/fulltext/images/5370498a366b9eb1b547b62cb352806c059ade7f13aa280faf931b44a135c096.jpg)

Wouter Verbeke graduated cum laude as a civil engineer at the K.U.Leuven in 2007. Currently he is working as a doctoral student at the Faculty of Business and Economics at the K.U.Leuven, Department of Decision Sciences and Information Management, His doctoral research focuses on the development and application of data mining techniques in marketing and <sup>fi</sup>nance. Wouter has been developing customer churn prediction models in the telecom sector using social network information retrieved from call detail record data, and credit rating migration models dependent on the business cycle for stress testing in the <sup>fi</sup>nancial sector.

![](/api/attachments/9VRDHYAD/fulltext/images/6dd7d5db3f20f24429567b5e43ff37e3f0974ce44d23de0e94551dfc4831d416.jpg)

Bart Baesens is an associate professor at K.U.Leuven (Belgium), and a lecturer at the University of Southampton (United Kingdom). He has done extensive research on predictive analytics, data mining, customer relationship management, fraud detection, and credit risk management. His <sup>fi</sup>ndings have been published in well-known international journals and presented at international top conferences. He is also co-author of the book Credit Risk Management: Basic Concepts, published in 2008. He regularly tutors, advices and provides consulting support to international <sup>fi</sup>rms with respect to their data mining, predictive analytics, and credit risk management policy.
