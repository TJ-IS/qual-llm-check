---
otero_id: 11622
otero_key: "77222FJ9"
title: "Incorporating domain knowledge into data mining classifiers: An application in indirect lending"
authors: "Atish P. Sinha; Huimin Zhao"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.06.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Incorporating domain knowledge into data mining classi<sup>fi</sup>ers: An application in indirect lending

Atish P. Sinha, Huimin Zhao ⁎

Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee, P. O. Box 742, Milwaukee, WI 53201-0742, United State

a r t i c l e i n f o

Article history: Received 18 August 2007 Received in revised form 27 March 2008 Accepted 29 June 2008 Available online 16 July 2008

Keywords: Data mining Classi<sup>fi</sup>cation Supervised learning Domain knowledge Expert system

## a b s t r a c t

Data mining techniques have been applied to solve classi<sup>fi</sup>cation problems for a variety of applications such as credit scoring, bankruptcy prediction, insurance underwriting, and management fraud detection. In many of those application domains, there exist human experts whose knowledge could have a bearing on the effectiveness of the classi<sup>fi</sup>cation decision. The lack of research in combining data mining techniques with domain knowledge has prompted researchers to identify the fusion of data mining and knowledge-based expert systems as an important future direction. In this paper, we compare the performance of seven data mining classi<sup>fi</sup>cation methods—naive Bayes, logistic regression, decision tree, decision table, neural network, k-nearest neighbor, and support vector machine—with and without incorporating domain knowledge. The application we focus on is in the domain of indirect bank lending. An expert system capturing a lending expert's knowledge of rating a borrower's credit is used in combination with data mining to study if the incorporation of domain knowledge improves classi<sup>fi</sup>cation performance. We use two performance measures: misclassi<sup>fi</sup>cation cost and AUC (area under the curve). A 2×7 factorial, repeated-measures ANOVA, with the two factors being domain knowledge (present or absent) and data mining method (seven methods), as well as a special statistical test for comparing AUCs, is used for analyzing the results. Analysis of the results reveals that incorporation of domain knowledge signi<sup>fi</sup>cantly improves classi<sup>fi</sup>cation performance with respect to both misclassi<sup>fi</sup>cation cost and AUC. There is interaction between classi<sup>fi</sup>cation method and domain knowledge. Incorporation of domain knowledge has a higher in<sup>fl</sup>uence on performance for some methods than for others. Both measures—misclassi<sup>fi</sup>cation cost and AUC—yield similar results, indicating that the <sup>fi</sup>ndings of the study are robust.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Data mining techniques have been applied to solve classi<sup>fi</sup>cation problems for a variety of applications, including credit scoring, bankruptcy prediction, insurance underwriting, and management fraud detection. These techniques automatically induce prediction models, called classifiers, based on historical data about previously solved problem cases. The classi<sup>fi</sup>ers can then be applied to recommend solutions to new problem cases.

In many of the application domains that have been studied by data mining researchers, there exist human experts who have developed their expertise through years of experience in solving problems in those domains. An expert's knowledge tends to be heuristic in nature. Because experts often <sup>fi</sup>nd it dif<sup>fi</sup>cult to articulate the heuristics or rules of thumb that they use to ef<sup>fi</sup>ciently solve a problem, acquiring their expertise is usually a dif<sup>fi</sup>cult and challenging task. This phenomenon is commonly referred to as the knowledge acquisition bottleneck [20].

A major bene<sup>fi</sup>t of using a data mining technique is that it bypasses the knowledge acquisition bottleneck. By unearthing the patterns or knowledge from the data itself, data mining methods obviate the need for eliciting knowledge from a human expert. Clearly, data mining lends itself naturally to domains in which there is a dearth of human expertise or in which domain knowledge cannot be easily formalized. However, there are domains that have large bodies of domain knowledge encapsulated in the form of human expertise. Also, in some of those domains, there exist large volumes of data. But very little research has been conducted to examine if domain knowledge can be incorporated into data mining for better performance. As Dybowski et al. [10] (p. 293) stated:

“At present, knowledge engineering and machine learning remain largely separate disciplines, yet, in many <sup>fi</sup>elds of endeavor, substantial human expertise exists alongside data archives. When both data and domain knowledge are available, how can these two resources effectively be combined to construct decision support systems?”

In this paper, we address the question by examining if such a fusion of domain knowledge and data could improve classi<sup>fi</sup>er performance in the domain of indirect bank lending. We compare the performance of seven data mining classi<sup>fi</sup>cation methods—naive Bayes, logistic regression, decision tree, decision table, neural network, k-nearest neighbor, and support vector machine—with and without incorporating domain knowledge. An expert system capturing a lending expert's knowledge of rating a borrower's credit is used in combination with data mining to study whether the incorporation of domain knowledge improves classi<sup>fi</sup>cation performance. We use two measures—misclassi<sup>fi</sup>cation cost and AUC (area under the curve)—for evaluating classi<sup>fi</sup>er performance.

Our study makes an important contribution to existing research in data mining by empirically investigating whether domain expertise improves performance of classi<sup>fi</sup>ers built using different methods. Also, instead of using classi<sup>fi</sup>cation accuracy or error rate as the sole performance measure—as has been the norm in fusion research—we evaluate the classi<sup>fi</sup>ers with respect to misclassi<sup>fi</sup>cation cost under a range of cost ratios, and with respect to AUC, an aggregate measure.

The paper is organized as follows. Section 2 reviews the related work in the area. Section 3 describes the domain knowledge and Section 4 describes the seven classi<sup>fi</sup>cation methods used in this study. Section 5 presents the theoretical framework and research questions. Section 6 describes the research design and methodology. Section 7 presents the results and Section 8 provides a discussion of the results and their implications. Section 9 summarizes the contributions of this study and outlines directions for future research.

## 2. Background

The process of building an expert system [5] is known as knowledge engineering. It involves a knowledge engineer eliciting procedures, strategies, and rules of thumb from a domain expert and transferring this heuristic knowledge into a computer program [48]. The resulting expert system solves problems in much the same way as the expert does, by using shortcuts and tricks and ignoring irrelevant information. It uses the stored knowledge to achieve high performance [18]. Expert systems have been applied to solve different types of problems, including prediction, diagnosis, design, planning, debugging, and control.

Human experts develop their knowledge through years of experience in solving problems in a narrow area. Because experts usually <sup>fi</sup>nd it dif<sup>fi</sup>cult to articulate the heuristics or rules of thumb that they apply, knowledge engineers need to overcome what is known as the knowledge acquisition bottleneck. According to Johnson [25], “the more competent domain experts become, the less able they are to describe the knowledge they use to solve problems!” Several knowledge acquisition techniques—such as interviews, protocol analysis, observation, and focus groups—are available for facilitating knowledge transfer from experts.

The <sup>fi</sup>eld of data mining has its origins in statistics and machine learning. Several data mining methods are available for classi<sup>fi</sup>cation problems, including statistical techniques such as naive Bayes, discriminant analysis, and logistic regression, and machine learning techniques such as decision tree/ rule induction and neural network. Data mining classi<sup>fi</sup>ers have been developed in several application domains, such as bankruptcy prediction [27,44,47], <sup>fi</sup>nancial performance prediction [31], bond rating analysis [22], credit evaluation [46], credit risk assessment [9], and network intrusion detection [56].

In knowledge engineering, the focus is on the knowledge of a human expert in a speci<sup>fi</sup>c problem area. On the other hand, the focus of data mining is on the data available in an organization. As noted before, these two <sup>fi</sup>elds have largely remained independent of one another, despite the fact that expert systems and data mining methods could play complementary roles in situations where both knowledge and data are available. Fayyad et al. [14] contended that the use of domain knowledge is important in all stages of the knowledge discovery process.

In one of the earliest studies on the subject, Pazzani and Kibler [34] developed a general purpose relational learning algorithm called FOCL, which combines explanation-based and inductive learning. In a later study, Pazzani et al. [35] conducted an experiment comparing FOCL with a domain theory to FOCL without a domain theory. A partial knowledge base of an expert system was used as the domain theory. They found that incorporating domain theory signi<sup>fi</sup>cantly reduced misclassi<sup>fi</sup>cation costs when larger training sets were used.

Hirsh and Noordewier [19] used background knowledge of molecular biology to re-express data in terms of higher-level features. Using C4.5 decision trees and backprop neural networks on DNA sequence learning tasks, they conducted experiments with and without the higher-level features. For both learning methods, the use of higher-level features resulted in signi<sup>fi</sup>cantly lower error rates.

In another study, Ambrosino and Buchanan [2] examined whether the addition of domain knowledge improved the learning of a rule induction program for predicting the risk of mortality in patients with community-acquired pneumonia. The augmented models performed signi<sup>fi</sup>cantly better (lower percent mean error) than the models without domain knowledge. The method preferred by the subjects for incorporating domain knowledge was addition of new attributes, which were derived from existing attributes.

Data mining techniques are good at generating useful statistics and <sup>fi</sup>nding patterns in large volumes of data, but “they are not very smart in interpreting these results, which is crucial for turning them into interesting, understandable and actionable knowledge” [37]. Pohle [37] viewed the lack of sophisticated tool support for incorporating human domain knowledge into the mining process as being the main factor responsible for the limitation.

Kopanas et al. [30] argued against the claim that data mining approaches eventually will automate the process and lead to discovery of knowledge from data with little or no support of domain experts and domain knowledge. They explored the role of domain knowledge in different phases of a large-scale data mining project, using a case study of customer insolvency in the telecommunications industry. They found that though domain knowledge plays a critical role mainly in the initial and <sup>fi</sup>nal phases of the project, it in<sup>fl</sup>uences the other phases to some degree as well.

In another study, Weiss et al. [49] combined an expert system with a data mining method for generating better sales leads. They developed an expert system that interviews executives of small and medium-sized companies and, based on their responses, recommends promising sales leads. The question–answer pairs and the recommended solutions were stored as examples to be mined by the method of rule induction. The study demonstrated how a knowledge base can be used to guide a machine learning program. The techniques developed in the study would be useful for consultation systems whose questions have different costs of acquisition.

Daniels et al. [8] demonstrated that data mining systems can be successfully combined with explicit domain knowledge. The authors focused on a special type of a priori knowledge, viz., the sign of the relationship between the dependent and independent variables, for economic decision problems. Prior knowledge was implemented as monotonicity constraints in decision tree and neural network classi-<sup>fi</sup>ers. Addition of the knowledge resulted in smaller decision trees, and smaller variations of error $R ^ { 2 }$ on the training and test sets for neural networks.

Eliciting the structure of a Bayesian network from a domain expert is a dif<sup>fi</sup>cult and time-consuming process. For that reason, current research has focused on learning the structure from data, without incorporating much prior knowledge of experts. Langseth and Nielsen [32] addressed this limitation by proposing a method for doing structural learning in objectoriented domains. Prior information provided by an expert about the structural properties of a domain was encoded into an object-oriented Bayesian network. The authors empirically showed that the proposed learning algorithm was more ef<sup>fi</sup>cient than conventional learning algorithms which do not incorporate such prior information.

The studies presented above examined the in<sup>fl</sup>uence of domain knowledge on data mining classi<sup>fi</sup>er performance from different perspectives. Pazzani et al. [35] used a general purpose relational learning algorithm based on <sup>fi</sup>rst-order predicate calculus for examining the effects of partial domain knowledge. They found the positive in<sup>fl</sup>uence of domain knowledge only for large data sets. In the other studies presented above, the classi<sup>fi</sup>ers were not evaluated with respect to misclassi<sup>fi</sup>cation cost, which is a much more appropriate measure of performance than simple error rate. Also, the focus has been on examining one or two data mining methods, not on investigating the differential impacts of domain knowledge on a variety of classi<sup>fi</sup>ers.

Recently, Fan et al. used genetic programming in learning ranking functions for search engines [13] and information routing services [12]. They applied domain knowledge in designing the building blocks of the ranking functions (GP terminals) and observed performance improvements over existing baselines.

## 3. Problem domain and domain knowledge

The problem domain for this study is that of bank loans for automobiles. Two types of attributes are present in a loan application: application attributes and credit bureau characteristics. The application attributes relate to the items on the loan application itself, such as years in current residence, years in previous residence, monthly income, and monthly payments. However, other major attributes for making lending decisions are not available in the application; they come from the Credit Bureau Report. The credit bureau characteristics include attributes such as the months on <sup>fi</sup>le, number of satisfactory trades, number of major trades, and number of minor trades.

The months on file attribute represents the total number of months the credit bureau has maintained a record on the applicant. Typically, the longer the number of months on <sup>fi</sup>le, the more credit history the applicant has. In a credit report, instances of credit are represented in a trade line, which stores the vital statistics of each instance of borrowing. For example, if a person obtains an installment loan, it would create a new trade line. The trade line would be listed on the person's credit report and the payment history would be typically updated each month. A new trade line is opened every time the borrower obtains a different loan or credit card.

Trades that have a suf<sup>fi</sup>cient payment history are rated on a scale of 1 to 9. Those trades for which all payments were received in a timely manner (i.e., none of them was received more than 29 days past the due date) are called satisfactory trades and receive a rating of 1, the best possible rating. If one of the payments for a loan was late and the late time period was between 29 and 60 days (exclusive), the loan would be classi<sup>fi</sup>ed as minor with a rating of 2. If any of the payments was received 60 days or more past the due date, the loan is classi<sup>fi</sup>ed as major with a rating of 3 or more, depending on how bad the payment history is. A rating of 9 indicates that the loan was “charged off” and was considered uncollectible by the creditor. The worst rating attribute indicates the worst rating among all the trade lines associated with the borrower.

An expert with over 15 years of lending experience was interviewed for acquiring domain knowledge. Initial, unstructured interviews helped us to gain an initial understanding of the domain. A generic loan application was used to identify the main steps and factors involved in the decision.

When the expert reviews a loan application, the <sup>fi</sup>rst thing he considers is the credit report. His assessment of the credit history is based upon attributes such as the number of trades rated as satisfactory, the number of major derogatory trades, the number of minor derogatory trades, and the months the applicant has been on <sup>fi</sup>le. After rating the applicant's credit, the expert reviews attributes on the loan application itself, such as years in current and previous residence, years with current and previous employer, monthly income, monthly payments, price of the car, down payment, etc.

The initial set of interviews was followed up with more speci<sup>fi</sup>c, structured interviews which elicited detailed knowledge of how an applicant's credit history is assessed. That knowledge was formalized as if–then rules. Provided below is an example of a rule acquired from the expert:

if number of major trades=0

and number of minor tradesb3

and number of satisfactory trades >=6

then credit rating = good cf 70

This rule states that if there are no major trades, the number of minor trades is less than 3, and the number of satisfactory trades is greater than or equal to 6, then the applicant's credit rating is good. A certainty factor (cf) is associated with the rule, re<sup>fl</sup>ecting the expert's con<sup>fi</sup>dence in the conclusion. In this case, the expert is 70% certain that the applicant's credit rating is good if the conditions hold true. The rules acquired from the lending expert for assessing credit rating were implemented in a backward-chaining expert system. The expert system has 25 such rules in its partial knowledge base. An example of a rule that classi<sup>fi</sup>es a borrower's credit rating as fair is given below:

$$
\begin{array}{l} \text {if number of major trades = 0} \\ \quad \text {and number of minor trades > 0} \\ \quad \text {and number of minor trades <  3} \\ \quad \text {and number of satisfactory trades > 0} \\ \quad \text {and number of satisfactory trades <  6} \\ \text {then credit rating = fair cf 70} \end{array}
$$

In contrast to an expert system, which explicitly captures domain knowledge, most data mining methods do not explicitly use domain knowledge but try to learn new patterns from data itself. The trained classi<sup>fi</sup>ers are then used to make predictions on new cases. So the two approaches, expert systems and data mining, are radically different. While one is expertise-driven, the other is data-driven.

The loan data set that we use for this study has 13 input attributes and one output, which is whether the loan is good or bad. The input attributes include the application attributes, as well as the following attributes from the credit bureau report: number of minor trades, number of major trades, number of satisfactory trades, and number of months on <sup>fi</sup>le. Based on the values of these attributes, the expert system determines if the credit rating of the applicant is bad, fair, good, or excellent. To examine the in<sup>fl</sup>uence of this credit rating knowledge, it is then added as an input to the data mining methods.

Approved loans with a payment history are classi<sup>fi</sup>ed into two categories as follows:

1. Approved good: The bank considers a case as “approved good” if the loan was approved and it has a good payment history. A loan is considered to have a good payment history if: it has more than 24 months of payment history; no more than two payments were between 30 and 59 days past due; and no payments were 60 days or more past due.

2. Approved bad: The bank considers a case as “approved bad” if the loan was approved, but the payment history is bad. The payment history is considered to be bad if either more than two payments were between 30 and 59 days past due, or if any payment was 60 days or more past due during the life of the loan.

## 4. Data mining classi<sup>fi</sup>cation methods

There have been several studies examining the performance of data mining techniques on business problems. The focus of most of those studies has been on binary classi<sup>fi</sup>cation problems, where the goal of the model built is to classify a problem case into one of two categories (e.g., bankrupt or non-bankrupt, bad credit or good credit, etc.).

Without loss of generality, a binary classi<sup>fi</sup>cation problem is described by an m-dimensional vector of variables $\mathbf { x } = < \mathbf { x } _ { 1 } ,$ ${ \bf x } _ { 2 } , . . . , { \bf x } _ { m } > ,$ , called attributes, and a binary variable y, called class. A training sample is a set of problem cases with known class values. A classification method takes a training sample as input and learns a general rule $, f ,$ called a classifier, which is a mapping from the attributes to the class. This learned classi<sup>fi</sup>er can then be used to predict the class outcomes of other cases not present in the training sample.

A variety of classi<sup>fi</sup>cation methods have been developed in the <sup>fi</sup>elds of statistical pattern recognition, machine learning, and arti<sup>fi</sup>cial neural networks [51]. In this study, we have selected the following widely used classi<sup>fi</sup>cation methods available in the Weka data mining package [53]: naive Bayes, logistic regression, J4.8 decision tree (Weka's implementation of C4.5), decision table, backpropagation neural network, knearest neighbor, and support vector machine. We brie<sup>fl</sup>y review these classi<sup>fi</sup>cation methods with a focus on binary classi<sup>fi</sup>cation problems.

## 4.1. Naive Bayes

Theoretically, an optimal classi<sup>fi</sup>er (called Bayes optimal classifier) that minimizes error rate exists and is equivalent to the following mapping [51]:

$$
f ^ {*} (x) = \left\{ \begin{array}{c c} - 1, & \text { if } P (\mathbf {y} = - 1 | \mathbf {x} = x) > P (\mathbf {y} = 1 | \mathbf {x} = x) \\ 1, & \text { otherwise } \end{array} \right.
$$

where $P ( \mathbf { y } = - 1 | \mathbf { x } = x )$ is the conditional probability of a negative class outcome given a particular attribute vector.

Applying the Bayes conditional probability rule, this is equivalent to:

$$
f ^ {*} (x) = \left\{ \begin{array}{l l} - 1, & \text { if } P (\mathbf {x} = x | \mathbf {y} = - 1) P (\mathbf {y} = - 1) > P (\mathbf {x} = x | \mathbf {y} = 1) P (\mathbf {y} = 1) \\ 1, & \text { otherwise } \end{array} \right.
$$

where $P ( \mathbf { x } { = } x | \mathbf { y } { = } - 1 )$ is the conditional probability of a particular attribute vector given that the class outcome is negative and $P ( \mathbf { y } = - 1 )$ is the prior probability of the event that the class outcome is negative.

Finding this optimal classi<sup>fi</sup>er requires determination of prior probabilities $P ( \mathbf { y } )$ and conditional probabilities $P ( \mathbf { x } | \mathbf { y } )$ In practical classi<sup>fi</sup>cation applications, however, it is usually impossible to directly estimate $P ( \mathbf { x } | \mathbf { y } )$ , as enumerating the points in X requires an enormous number of training cases, especially when some of the attributes are continuous. All practical classi<sup>fi</sup>cation methods can be seen as attempts to estimate $P ( \mathbf { x } | \mathbf { y } )$ with various simplifying assumptions and heuristic search strategies. For example, the naive Bayes method assumes that the attributes are conditionally independent, such that $P ( \mathbf { x } | \mathbf { y } ) = \prod _ { i = 1 } ^ { m } P ( \mathbf { x } _ { i } | \mathbf { y } )$ [24]. The problem of estimating the conditional joint distribution $P ( \mathbf { x } | \mathbf { y } )$ is reduced to estimating the individual conditional distributions $P ( \mathbf { x } _ { i } | \mathbf { y } ) ( i \mathbf { = } 1 , 2 , . . . , m )$

## 4.2. Logistic regression

Logistic regression (LR) is a widely used statistical method for classi<sup>fi</sup>cation. It assumes that the logit, logarithm of the odds ratio, is linear with regard to the attributes [21].

$$
g (x) = \ln \frac {P (\mathbf {y} = - 1 | \mathbf {x} = x)}{P (\mathbf {y} = 1 | \mathbf {x} = x)} = \sum_ {j = 1} ^ {m} \beta_ {j} x _ {j} + \beta_ {0}
$$

The decision boundary that separates the classes in the attribute space X is linear. The coef<sup>fi</sup>cients, $\beta _ { j } ( j = 0 , 1 , 2 , . . . , m )$ , can be found using an iterative weighted least squares procedure.

## 4.3. Decision tree

Decision tree techniques follow a “divide and conquer” heuristic search strategy and generate tree-like sequential decision models. Most decision tree inducers assume that the overall prediction decision can be made via a sequence of small tests (or decisions), each of which usually involves a single attribute $\mathbf { x } _ { i \cdot }$ Different decision tree inducers mainly differ in the goodness measure used to select the splitting attribute at each intermediate tree node. For example, a popular decision tree inducer named ID3 selects the attribute that results in the maximum information gain (or entropy reduction) [40]. C4.5, a successor of ID3, replaces information gain with gain ratio to compensate ID3's bias of favoring highly-branching attributes [41]. The tree building procedure is usually followed by a pruning phase, in which some of the sub-trees are replaced by leaves or raised to substitute their parents, to reduce the chance of overfitting [33].

## 4.4. Decision table

A decision table learner selects the most discriminating attributes based on the training sample to form a lookup table, which is then used to classify new cases. Different subsets of attributes are evaluated using a performance estimation method, such as cross-validation [29], and the best-performing subset, $\mathbf { X } ^ { * } = < \mathbf { X } _ { 1 } ^ { \prime } , \mathbf { X } _ { 2 } ^ { \prime } , . . . , \mathbf { X } _ { p } ^ { \prime } > \left( p \leq m \right)$ , is kept in the <sup>fi</sup>nal decision table. Ef<sup>fi</sup>cient heuristic algorithms (e.g., [28]) exist for <sup>fi</sup>nding approximately optimal subsets of attributes. Given a testing case, for which $\mathbf { x } ^ { * } = x { = } { < } x _ { 1 } , x _ { 2 } , { \ldots } , x _ { p } { > }$ , let S(x) denote the set of the training cases, for which $\mathbf { x } ^ { * } { = } x \left( \mathrm { i } . e . \right.$ , they match exactly the testing case on the selected attributes in the decision table), the predicted class membership f(x) is determined as:

<sup>f</sup> <sup>x</sup>ð Þ ¼ the majority class of the training cases in $S ( x ) , { \mathrm { ~ i f ~ } } S ( x ) \neq \Phi ;$

## 4.5. Backpropagation neural network

Backpropagation is one of the most widely used neural network techniques for classi<sup>fi</sup>cation [6,42]. Neural networks are highly interconnected networks, which learn by adjusting the weights of the connections between nodes on different layers. A backpropagation neural network has an input layer (corresponding to the attribute vector ${ \mathbf { x } } ) ,$ , an output layer (corresponding to the class y), and, possibly, one or more hidden layers. The training of a neural network is often not trivial; it takes experience and experimenting to adjust the parameters, such as the number of nodes on a hidden layer and the learning rate.

## 4.6. k-nearest neighbor

Unlike the methods described above, k-nearest neighbor (kNN) is an instance-based method [1] and does not learn a model in the true sense. It assigns a new case to the majority class among the k closest cases in the training set [16]. The objective is to identify the cases that are similar to the new case and then classify the new case based on the outcome of the majority of its neighbors. There are three components of a nearest-neighbor solution: the set of stored cases; the distance metric used to compute the distance between cases; and the value of k [50]. Many applications use the Euclidean distance metric. We selected the Euclidean distance metric in the Weka package to develop the kNN model.

## 4.7. Support vector machine

Support vector machines (SVM) [3,22,26,36,53] combine linear modeling and case-based learning. A small number of critical boundary cases called support vectors are selected from each class. A linear discriminant function representing the so-called maximum margin hyperplane is found to separate the support vectors as much as possible. All other cases in the training data set are irrelevant.

Support vector machines can also model non-linear class boundaries by transforming the original attributes using non-linear transformations and searching for the maximum margin hyperplane in the transformed attribute space. Let the set of support vectors be denoted $\{ < x ^ { i } , y ^ { i } > | i = 1 , 2 , . . . , l \} ;$ a support vector machine has the general form of $f ( x ) =$ sign $( \sum _ { i = 1 } ^ { l } y ^ { i } \alpha _ { i } k ( x , x ^ { i } ) + \beta )$ , where k is called a kernel function and is used to implement non-linear transformations. The support vectors and the parameters $\alpha _ { i }$ and $\beta$ are found by solving a so-called constrained quadratic optimization problem.

## 5. Theoretical framework

As discussed in the Background section, prior research in data mining has not devoted much attention to the role of domain knowledge. Part of the reason could be that the domains of application are typically data-rich, giving the impression that domain knowledge is not really necessary. Also, the fact that in many domains expert knowledge is not readily available or, even when available, knowledge acquisition tends to be a dif<sup>fi</sup>cult and time-consuming process, could be a factor in not addressing the issue of domain knowledge.

Dybowski et al. [10] emphasized that in domains where both data and expertise are available, it is worthwhile exploring the fusion of domain knowledge and data mining. In this study, we explore if partial domain knowledge, captured in an expert system, can help improve the performance of data mining algorithms. The few studies (e.g., [2,8,19,32,35,49]) that examined the effects of such a fusion have produced promising results.

![](/api/attachments/77222FJ9/fulltext/images/15f787938aa175c6102924cd4d4ebe95a43b9e005f2a7609f49feb5008070372.jpg)  
Fig. 1. Research model.

The objective of this study is to empirically examine if the incorporation of domain knowledge has a positive in<sup>fl</sup>uence on classi<sup>fi</sup>er performance, especially in situations where the knowledge is partial (i.e., the knowledge leads to intermediate concepts but is not suf<sup>fi</sup>cient to make the <sup>fi</sup>nal prediction of interest) and the data is limited. To that end, we used an expert system that captures partial domain knowledge and applied learning algorithms to a relatively small data set.

Human learning usually takes place within an environment rich with background knowledge. However, the majority of research in learning has focused on how agents learn from examples without any prior knowledge. Devoid of prior knowledge, a learning method needs to search a large hypothesis space to <sup>fi</sup>nd a solution. Infusing domain knowledge into the learning process would reduce the hypothesis space, thereby facilitating the search for a solution. To build an autonomous learning agent that employs background knowledge, Russell and Norvig [43] (p. 626) contended that “the agent must have some method for obtaining the background knowledge” and can no longer make “naive speculations, and should use its background knowledge to learn more and more effectively.”

Fig. 1 shows the research model for this study. The knowledge provided by the expert system de<sup>fi</sup>nes the context for learning. The expert system evaluates an applicant's credit rating and provides its value as an input to the data mining method. The other inputs come from the data set itself.

As the <sup>fi</sup>gure shows, we examine two factors that could in<sup>fl</sup>uence classi<sup>fi</sup>er performance: domain knowledge and data mining method. Domain knowledge has two values: present and absent. Data mining method has seven possible values, each corresponding to one of the methods being used in the study.

The results from prior studies strongly attest to the positive in<sup>fl</sup>uence of domain knowledge—whether it be in the form of partial domain theory, higher-level attributes, monotonicity constraints, or structural properties—on classi<sup>fi</sup>er performance. However, those studies focused on one or two data mining methods and did not examine the AUCs for the resultant classi<sup>fi</sup>ers. In most of those studies, the performance measure used was accuracy or error rate, not misclassi<sup>fi</sup>cation cost.

In our study, we compare the performance of classi<sup>fi</sup>ers built using seven of the most widely-used data mining methods, with respect to both misclassi<sup>fi</sup>cation cost and AUC. We expect that the incorporation of credit rating knowledge, captured in an expert system, into the learning process will improve performance. Note that the cascading of an expert system with a classi<sup>fi</sup>er is similar to cascading multiple classi<sup>fi</sup>ers [54,55]. However, in the former, higher-level attributes are generated by an expert system built using human expertise, while in the latter, data mining methods are used to learn potentially useful higher-level attributes. We pose the following research questions:

Table 1 Input attributes

<table><tr><td>Source</td><td>Attribute</td><td>Description</td></tr><tr><td rowspan="7">Loan application</td><td>Res-years</td><td>The number of years the applicant has lived at the current residence.</td></tr><tr><td>Prev-res-years</td><td>The number of years the applicant lived in the previous residence.</td></tr><tr><td>Employ-years</td><td>The number of years the applicant has been employed by the current employer.</td></tr><tr><td>Prev-employ-years</td><td>The number of years the applicant was employed by the previous employer.</td></tr><tr><td>Gross-inc-month</td><td>The amount in dollars of the applicant&#x27;s gross income per month.</td></tr><tr><td>Debt-inc-ratio</td><td>The ratio of the total monthly debt payments to applicant&#x27;s gross monthly income.</td></tr><tr><td>Percent-to-finance</td><td>The loan amount as a percentage of the value of the automobile being purchased.</td></tr><tr><td rowspan="6">Credit Bureau Report</td><td>Minor</td><td>The number of trades rated as minor derogatory.</td></tr><tr><td>Major</td><td>The number of trades rated as major derogatory.</td></tr><tr><td>Satisfactory</td><td>The number of trades rated as satisfactory.</td></tr><tr><td>Worst</td><td>The worst rating among all the trades associated with the applicant.</td></tr><tr><td>Bankrupt</td><td>Whether the applicant has ever been declared bankrupt.</td></tr><tr><td>Months</td><td>The number of months the applicant has been on file.</td></tr></table>

![](/api/attachments/77222FJ9/fulltext/images/eb427a00238e2a3c0c3096275b684976b210c8299002c70990595b9dc8d3f8c2.jpg)  
Fig. 2. Integration of expert system and data mining classi<sup>fi</sup>er.

RQ1: Does a data mining classi<sup>fi</sup>er built by incorporating partial domain knowledge result in lower misclassi<sup>fi</sup>cation cost than a classi<sup>fi</sup>er built using a data mining method alone?

RQ2: Does a data mining classi<sup>fi</sup>er built by incorporating partial domain knowledge produce a larger AUC than a classi<sup>fi</sup>er built using a data mining method alone?

Different methods are not expected to yield identical results, but as RQ1 examines, each of them is expected to produce better results when domain knowledge is incorporated. However, it is not at all clear that the degree of improvement will be the same for all the methods. Prior research has shown that data mining methods could react to treatments in different ways. For example, Chung and Tam [7] found that the performance of methods is task dependent, and Kim and McLeod [27] found that ID3 and neural networks performed better than statistical methods for modeling nonlinear strategies. For bankruptcy prediction, Sung et al. [47] found that decision trees were only a little more accurate than discriminant analysis models under normal conditions, but were much more accurate under crisis conditions. We can therefore expect that the degree of performance improvement using domain knowledge would vary according to the method employed. We pose the following research question:

RQ3: Does the degree of performance improvement of a classi<sup>fi</sup>er built using partial domain knowledge depend on the data mining method employed?

## 6. Research design and methodology

In this section, we describe the research design and methodology we employed to address the research questions. We used two performance measures, viz., misclassification cost and AUC, for evaluating the classi<sup>fi</sup>ers in this study (see Fig. 1). The performance measure most frequently used in the literature for comparing data mining methods has been error rate or accuracy. The error rate of a classi<sup>fi</sup>er f is de<sup>fi</sup>ned as

$$
\begin{array}{l} \text { error } (f) = P (f (\mathbf {x}) \neq \mathbf {y}) = P (\mathbf {y} = - 1) P (f (\mathbf {x}) = 1 | \mathbf {y} = - 1) \\ \quad + P (\mathbf {y} = 1) P (f (\mathbf {x}) = - 1 | \mathbf {y} = 1). \end{array}
$$

Accuracy is de<sup>fi</sup>ned as accuracy $( f ) { = } 1 { \mathrm { - e r r o r } } ( f )$ . The method generating the minimum error rate (or the maximum accuracy) has usually been considered to be the best.

For many real-world problems, however, the costs for different types of misclassi<sup>fi</sup>cation errors are not equal. For example, misclassi<sup>fi</sup>cation costs are typically unequal in problems such as credit scoring, bankruptcy prediction, insurance underwriting, and fraud detection. For such problems, the objective should be to minimize overall misclassi<sup>fi</sup>cation cost, not misclassi<sup>fi</sup>cation error rate [11,16,39]. In a binary classi<sup>fi</sup>cation problem, a speci<sup>fi</sup>c case belongs to one of two classes: positive or negative. Tests are conducted to detect if a case is positive (e.g., breast cancer, bankrupt <sup>fi</sup>rm, bad credit, etc.) or negative. A false positive results when the test is positive but the case does not actually belong to the positive class. A false negative results when the test is negative but the case actually belongs to the positive class.

When the costs of making classi<sup>fi</sup>cation errors are known, the performance of a classi<sup>fi</sup>er f can be measured using misclassi<sup>fi</sup>cation cost, de<sup>fi</sup>ned as:

$$
\begin{array}{c} \text {cost} (f) = P (\mathbf {y} = - 1) P (f (\mathbf {x}) = 1 | \mathbf {y} = - 1) C _ {1 | - 1} \\ + P (\mathbf {y} = 1) P (f (\mathbf {x}) = - 1 | \mathbf {y} = 1) C _ {- 1 | 1} \end{array}
$$

where $C _ { 1 | - 1 }$ is the cost of a false positive mistake and $C _ { - 1 | 1 }$ is the cost of a false negative mistake. Error rate can be viewed as a special case of misclassi<sup>fi</sup>cation cost, when the two types of errors are weighted equally (i.e., $C _ { 1 | - 1 } = C _ { - 1 | 1 } )$ . Therefore, we use the more general measure, misclassi<sup>fi</sup>cation cost, in this study.

In the last few years, a number of studies have also used Receiver Operating Characteristic (ROC) curves for analyzing a classi<sup>fi</sup>er's performance with respect to misclassi<sup>fi</sup>cation costs (e.g., [38,46,52]). An ROC curve plots the true positive rate of a classi<sup>fi</sup>er against its false positive rate and those values can be used to compute the expected cost of the classi<sup>fi</sup>er for a given decision threshold. An ROC curve visually depicts classi<sup>fi</sup>er

Table 2  
Mean misclassi<sup>fi</sup>cation costs

<table><tr><td>Cost ratio</td><td>Knowledge</td><td>Bayes</td><td>LR</td><td>Tree</td><td>Table</td><td>Neural</td><td>kNN</td><td>SVM</td></tr><tr><td rowspan="2">1</td><td>Absent</td><td>0.243</td><td>0.245</td><td>0.269</td><td>0.292</td><td>0.250</td><td>0.279</td><td>0.252</td></tr><tr><td>Present</td><td>0.231</td><td>0.217</td><td>0.265</td><td>0.226</td><td>0.222</td><td>0.264</td><td>0.218</td></tr><tr><td rowspan="2">2</td><td>Absent</td><td>0.249</td><td>0.233</td><td>0.251</td><td>0.332</td><td>0.232</td><td>0.288</td><td>0.227</td></tr><tr><td>Present</td><td>0.201</td><td>0.207</td><td>0.235</td><td>0.199</td><td>0.188</td><td>0.256</td><td>0.216</td></tr><tr><td rowspan="2">3</td><td>Absent</td><td>0.240</td><td>0.218</td><td>0.220</td><td>0.250</td><td>0.206</td><td>0.231</td><td>0.201</td></tr><tr><td>Present</td><td>0.186</td><td>0.186</td><td>0.205</td><td>0.218</td><td>0.176</td><td>0.209</td><td>0.189</td></tr><tr><td rowspan="2">4</td><td>Absent</td><td>0.217</td><td>0.200</td><td>0.179</td><td>0.200</td><td>0.194</td><td>0.206</td><td>0.176</td></tr><tr><td>Present</td><td>0.184</td><td>0.165</td><td>0.182</td><td>0.153</td><td>0.151</td><td>0.187</td><td>0.155</td></tr><tr><td rowspan="2">5</td><td>Absent</td><td>0.194</td><td>0.172</td><td>0.151</td><td>0.167</td><td>0.167</td><td>0.189</td><td>0.159</td></tr><tr><td>Present</td><td>0.180</td><td>0.155</td><td>0.162</td><td>0.127</td><td>0.126</td><td>0.172</td><td>0.128</td></tr><tr><td rowspan="2">Overall</td><td>Absent</td><td>0.229</td><td>0.214</td><td>0.214</td><td>0.248</td><td>0.210</td><td>0.239</td><td>0.203</td></tr><tr><td>Present</td><td>0.197</td><td>0.186</td><td>0.210</td><td>0.185</td><td>0.172</td><td>0.217</td><td>0.181</td></tr></table>

Without Knowledge  With Knowledge  
![](/api/attachments/77222FJ9/fulltext/images/8972bc60cfe977aa91aba7bba785cd713e2cafe974ed5c01514a78f3254c2c41.jpg)  
(a) Cost Ratio = 1

![](/api/attachments/77222FJ9/fulltext/images/6be68bc1a576ebcda8517531c3635571954ee81f11bcd792cb9cdc4c88c1b593.jpg)  
(b) Cost Ratio = 2

![](/api/attachments/77222FJ9/fulltext/images/b2f8f325608187071d7f2eade58afb286d5c615c5f57cf69df3a59312e9a4058.jpg)  
(c)Cost Ratio = 3

![](/api/attachments/77222FJ9/fulltext/images/8206189c6e50f9df3670978f366f5aed9ba8d981d6f01bfcd77f6c588f194c5d.jpg)  
(d)Cost Ratio = 4

![](/api/attachments/77222FJ9/fulltext/images/47070ef3f9476596ef40fe7552f07a94ae00a8a505ca22c8541b17e9c5f35fe0.jpg)  
(e) Cost Ratio = 5  
Fig. 3. Misclassi<sup>fi</sup>cation costs with and without domain knowledge.

performance across a spectrum of decision thresholds and is a very useful technique for visualizing and evaluating classi<sup>fi</sup>er performance [15].

In situations where costs are often dif<sup>fi</sup>cult to estimate or are unknown, the area under an ROC curve—which is computed by integrating over all possible values of the ratio of one cost to the other—can be used to assess classi<sup>fi</sup>er performance [16]. The area under the curve (AUC) is an appropriate measure for comparing data mining methods at an aggregate level [3,23]. Higher AUC indicates better aggregate performance.

The loan data set that we use for this study has 13 input attributes (described in Table 1) and one output, which is whether the loan is good or bad. A sample of 220 loan applications obtained from a bank was used. All of those cases were approved loans with more than two years of payment history, and included an equal number of good and bad loans.

The primary objective of this study is to compare the performance of the data mining methods with and without domain knowledge. Based on the values of the attributes obtained from the credit bureau report, the expert system determines if the credit rating of the applicant is bad, fair, good, or excellent. The credit rating output, which represents a higher-level concept derived using domain knowledge, could in turn become an input to a data mining classi<sup>fi</sup>er for making decisions on bank loans.

To test the effects of domain knowledge on classi<sup>fi</sup>er performance, for each case we added the value of credit rating proposed by the expert system to the other inputs (e.g., debtto-income ratio, percentage-to-<sup>fi</sup>nance, number of satisfactory trades, etc.). Classi<sup>fi</sup>ers built using input data enhanced by the credit rating knowledge formed the experimental group. For the control group, we built the classi<sup>fi</sup>ers using the original 13 input attributes (without credit rating), which include those from the credit bureau report (minor, major, satisfactory, etc.) Fig. 2 depicts how the output from the expert system was integrated with the data mining classi<sup>fi</sup>ers. Note that the input port for domain knowledge is turned off when using data mining methods alone. When domain knowledge is incorporated, this port accepts the credit rating output from the expert system as an input to classi<sup>fi</sup>er learning.

Seven classi<sup>fi</sup>cation methods available in the Weka data mining package—naive Bayes, logistic regression, J4.8 decision tree, decision table, backpropagation neural network, k-nearest neighbor, and support vector machine—were used in the study. Each method was used to build classi<sup>fi</sup>ers for the two treatments, one without and the other with credit rating knowledge.

The parameters of the classi<sup>fi</sup>cation methods were set as follows. For kNN, k was set to 3. We also tested kNN with other parameter settings such as k=1 and $k = 5$ and obtained similar results. We therefore report results for $k = 3$ only. For backpropagation neural network, the number of hidden nodes was set to 2. To minimize the effects of any expert bias in empirical comparison, Bradley [4] recommended that there be no attempt to tune the classi<sup>fi</sup>cation methods to a speci<sup>fi</sup>c problem. We therefore retained the default settings of Weka for all other parameters of the methods.

Because performance of a classi<sup>fi</sup>er on training data— known as apparent performance—is usually overly optimistic and not reliable, we used 10-fold cross-validation, a highly recommended performance estimation technique [29], to estimate the performance of learned classi<sup>fi</sup>ers. This technique randomly splits the full data set into ten subsets called folds. Each fold is used for estimating the performance of a classi<sup>fi</sup>er learned using the remaining nine folds. The average over the ten runs is used as an overall performance estimate. We performed this estimation 20 times for each method on both the control and experimental data sets. In each run, we provided the same seed for the random number generator used by 10-fold cross-validation for all the methods on both data sets, giving rise to a repeated-measures design.

A 2×7 factorial ANOVA was used for comparing misclassi<sup>fi</sup>cation costs (normalized by dividing the cost by $P ( \mathbf { y } = - 1 )$ $C _ { 1 | - 1 } + P ( \mathbf { y } = 1 ) C _ { - 1 | 1 } ) ,$ with the two factors being domain knowledge (present or absent) and data mining method (one of seven methods). Because the same cases are used for comparison, both across domain knowledge and method, we used the repeated-measures ANOVA procedure in SPSS. The cost ratio, $\begin{array} { r } { r \dot { = } \frac { P ( \mathbf { y } = - 1 ) C _ { 1 | - 1 } } { P ( \mathbf { y } = 1 ) C _ { - 1 | 1 } } , } \end{array}$ was used as a covariate because misclassi<sup>fi</sup>cation <sup>j</sup> costs vary with cost ratios. In this study, we use <sup>fi</sup>ve different cost ratios (1, 2, 3, 4, and 5). Cost ratios outside the range [1, 5] were deemed unrealistic and not considered. With a given cost ratio, the classi<sup>fi</sup>cation methods in Weka can re-weight the two types (positive and negative) of cases appropriately and attempt to minimize misclassi<sup>fi</sup>cation cost [53].

![](/api/attachments/77222FJ9/fulltext/images/80168b0198eae7526f768adcbb67d750d500c5d607dba6ea34dd4a73d634c5fc.jpg)  
(a) Cost Ratio = 2

![](/api/attachments/77222FJ9/fulltext/images/3c7ef1dd9f69c73acb05489d86fa5132c4e54b54181eaccb94267174d04f4935.jpg)  
(b) Cost Ratio = 3  
Fig. 4. Effects of domain knowledge for two cost ratios.

Table 4 Comparison of AUCs  
Table 3  
Repeated-measures ANOVA for misclassi<sup>fi</sup>cation cost

<table><tr><td>Effect</td><td>Mean square</td><td>F</td><td>Sig.</td></tr><tr><td>Knowledge</td><td>0.023</td><td>352.196</td><td>0.000</td></tr><tr><td>Method</td><td>0.007</td><td>117.733</td><td>0.000</td></tr><tr><td>Knowledge*Method</td><td>0.002</td><td>44.096</td><td>0.000</td></tr></table>

When using AUC to measure the aggregate performance of a classi<sup>fi</sup>cation method over all possible cost ratios, we pooled together the 20 runs for each classi<sup>fi</sup>cation method with or without domain knowledge and compared the AUC measures using the method proposed by Hanley and McNeil [17]. This test calculates a z score based on the difference between two AUCs, their estimated standard errors, and the estimated correlation between them. The signi<sup>fi</sup>cance level associated with z can be found by using a normal distribution table.

## 7. Results

Table 2 shows the means for misclassi<sup>fi</sup>cation costs of the learned classi<sup>fi</sup>ers across the different cost ratios. Figs. 3 and 4 graphically show the misclassi<sup>fi</sup>cation costs for each data mining method with and without domain knowledge under each cost ratio. In general, the misclassi<sup>fi</sup>cation costs go down appreciably with the addition of domain knowledge for all methods, except for decision tree. The magnitude of reduction is usually highest for decision table, followed by neural network, naive Bayes, and logistic regression.

Table 3 presents the results of the repeated-measures ANOVA with domain knowledge and method as factors and cost ratio as a covariate. Both the main effects are signi<sup>fi</sup>cant. Incorporating domain knowledge reduces misclassi<sup>fi</sup>cation costs signi<sup>fi</sup>cantly (F=352.2, pb0.001); hence, research question RQ1, which asks if data mining classi<sup>fi</sup>ers that incorporate domain knowledge outperform—with respect to misclassi<sup>fi</sup>- cation cost—those that do not, is answered in the positive. To examine RQ1 for each method, we conducted separate nonparametric sign tests [45]. For each method, we tested if the classi<sup>fi</sup>er built using knowledge resulted in lower misclassi-<sup>fi</sup>cation cost than the one built without knowledge. The sign test is applicable because we are comparing the pairwise performance of two related samples. The test was signi<sup>fi</sup>cant at pb.001 for all the methods, except for decision tree, indicating that addition of knowledge does reduce misclassi<sup>fi</sup>- cation cost for the methods individually.

We also <sup>fi</sup>nd that the effect of the incorporation of domain knowledge on misclassi<sup>fi</sup>cation cost depends on the cost ratio.

![](/api/attachments/77222FJ9/fulltext/images/7526ff7179c5438348775795bb950aa808e53c96733c83b990ed86deb1e18518.jpg)  
Fig. 5. ROC curves for naive Bayes.

As the cost ratio increases, the reduction of misclassi<sup>fi</sup>cation cost due to incorporation of domain knowledge becomes less pronounced (see Figs. 3 and 4). When the cost ratio is greater than 5, no classi<sup>fi</sup>cation method can perform better than the simple decision of always rejecting a loan application, because approving a potentially bad loan tends to be too costly.

Research question RQ2 asks if a data mining classi<sup>fi</sup>er that incorporates domain knowledge produces a larger AUC than that without. Table 4 presents the AUCs for classi<sup>fi</sup>ers built using the seven methods, with knowledge absent and knowledge present. The table also summarizes the results of Hanley and McNeil's test for comparing AUCs. Incorporating domain knowledge increases AUC signi<sup>fi</sup>cantly for all classi<sup>fi</sup>cation methods, except for J4.8 decision tree. Hence, RQ2 is answered in the af<sup>fi</sup>rmative.

Fig. 5 shows two ROC curves for naive Bayes, one with knowledge and the other without. The curve for the Bayes classi<sup>fi</sup>er with knowledge dominates the one without, across almost the entire spectrum. We observed the same phenomenon for most of the other classi<sup>fi</sup>ers.

Research Question RQ3 examines if the degree of performance improvement using domain knowledge would vary according to the method employed. As shown in Table 3, the differences in cost among the methods are signi<sup>fi</sup>cant (F=117.73, pb.001). The interaction between the two factors (Knowledge and Method) is also signi<sup>fi</sup>cant (F=44.1, pb0.001) due to the differential effects of domain knowledge on cost reduction across the methods. Therefore, RQ3 is answered in the positive.

## 8. Discussion of results

The results underscore the important role played by domain knowledge in classi<sup>fi</sup>er learning. Out of the seven methods examined, all except decision tree resulted in signi<sup>fi</sup>cantly better classi<sup>fi</sup>ers when knowledge was incorporated. For decision tree, the reduction in misclassi<sup>fi</sup>cation cost was the lowest and the AUC actually became smaller when knowledge was added. That could be because the knowledge added in the form of the higher-level attribute, credit rating, has many values, resulting in many branches and potential over<sup>fi</sup>tting, especially in situations with small training samples. Although massaging this attribute (e.g., re-categorizing the values of the attribute) can lead to better performance, for the fairness of comparison, we report the original result without tampering with this attribute in any manner.

<table><tr><td>Knowledge</td><td></td><td>Bayes</td><td>LR</td><td>Tree</td><td>Table</td><td>Neural</td><td>kNN</td><td>SVM</td></tr><tr><td>Absent</td><td>Mean (SE)</td><td>0.790(0.007)</td><td>0.828(0.006)</td><td>0.743(0.008)</td><td>0.775(0.007)</td><td>0.833(0.006)</td><td>0.761(0.007)</td><td>0.751(0.008)</td></tr><tr><td>Present</td><td>Mean (SE)</td><td>0.824(0.006)</td><td>0.855(0.006)</td><td>0.734(0.008)</td><td>0.796(0.007)</td><td>0.848(0.006)</td><td>0.778(0.007)</td><td>0.782(0.007)</td></tr><tr><td>Correlation r</td><td></td><td>0.870</td><td>0.780</td><td>0.540</td><td>0.590</td><td>0.730</td><td>0.540</td><td>0.400</td></tr><tr><td>Z</td><td></td><td>10.027</td><td>6.697</td><td>-1.212</td><td>3.404</td><td>3.497</td><td>2.516</td><td>3.831</td></tr><tr><td>P</td><td></td><td>0.000</td><td>0.000</td><td>0.226</td><td>0.001</td><td>0.001</td><td>0.012</td><td>0.000</td></tr></table>

The decision table learner experienced the largest reduction in misclassi<sup>fi</sup>cation cost and a relatively high increase in AUC. The attributes selected in the <sup>fi</sup>nal decision table are satisfactory, minor, and worst when domain knowledge is absent. When domain knowledge is present, only credit rating and one of the original attributes, months, are kept in the <sup>fi</sup>nal decision table, highlighting the importance of domain knowledge.

We also found that the impact of domain knowledge was quite sensitive to the cost ratio assumption. For example, there is a 40% reduction in misclassi<sup>fi</sup>cation cost when cost ratio=2, whereas the reduction is 22.6% for cost ratio=1 and only 12.8% for cost ratio=3. As discussed in Section 4.4, a decision table learner creates a lookup table, which stores the most discriminating attributes. Because the decision table learner reweights the positive and negative cases in the training set based on the cost ratio, it is possible that the lookup table is not very robust against changes in cost ratio. For example, when domain knowledge is absent, the decision table learner selects satisfactory, minor, and worst when cost ratio=1, and satisfactory and minor when cost ratio=3, whereas it selects only satisfactory when cost ratio=2. If minor was included in addition to satisfactory, the performance of the decision table learner without domain knowledge could have been relatively better.

In the absence of credit rating knowledge, Bayes, logistic regression, neural network, and SVM generate much lower misclassi<sup>fi</sup>cation costs than decision table, kNN, and decision tree under costs ratio = 1. As the cost of misclassifying a bad load becomes greater (for example, when cost ratio=3), decision tree and kNN improve their performance considerably, but SVM, neural net, and logistic perform the best. When the cost ratio is very high (e.g., 5), decision tree and SVM are the best performers, while Bayes and kNN are the worst. The performance of kNN relative to the other methods is consistently poor, irrespective of the value of cost ratio. On the other hand, the relative performance of decision tree improves and that of Bayes deteriorates as cost ratio goes up. The results suggest that the value of cost ratio could be a determining factor for selecting a classi<sup>fi</sup>er, though, overall, SVM's performance is the most impressive, followed by neural network and logistic regression.

The addition of credit rating knowledge to the learning process results in signi<sup>fi</sup>cant performance improvement for all methods, except decision tree, across the <sup>fi</sup>ve different cost ratios. The results corroborate the central theme of our research, that partial domain knowledge, made available to the learning methods by explicitly including a higher-level concept derived from expertise, has a signi<sup>fi</sup>cant in<sup>fl</sup>uence on performance of classi<sup>fi</sup>ers trained on limited data. Such performance improvements provide important guidelines for <sup>fi</sup>nancial institutions that lend money to customers. Appropriate choice of a data mining method, along with the incorporation of domain knowledge, could translate to substantial monetary bene<sup>fi</sup>ts for a bank.

Another important <sup>fi</sup>nding of the study is that the degree of in<sup>fl</sup>uence of domain knowledge varies according to method. For instance, we found that while the performance improvement for decision table was substantial, that for decision tree was minimal. From a practical standpoint, the implication is that just because a method performs below par in a pure data mining situation, it should not be excluded from consideration when the fusion of expertise and data is being attempted.

## 9. Conclusion and future directions

The primary objective of the study was to examine the role of domain knowledge on classi<sup>fi</sup>er learning. To that end, we incorporated knowledge of credit rating into the learning process and investigated whether that resulted in better classi<sup>fi</sup>er performance. The results of this study underscore the synergy between domain knowledge and data mining, especially in situations where knowledge and data are both limited.

Apportioning responsibilities between knowledge and data mining is an important issue for effective fusion to take place. When knowledge such as credit rating is readily available from experts or other sources, it makes sense to incorporate that knowledge into the decision process. On the other hand, it is relatively more dif<sup>fi</sup>cult to capture the knowledge of the loan approval decision, which involves a certain amount of subjectivity. For example, if the debt to income ratio is much lower than the cutoff (say, 36%), a loan of<sup>fi</sup>cer could use that to compensate for other attributes whose values are not that promising. Acquiring the knowledge of all such nuances and shortcuts is an arduous and time-consuming task, lending itself well to a data mining solution. But if an expert system for loan approval is available, a future direction would be to compare its performance with that of the fusion method presented in this paper. Another possibility is to examine if cascading the data mining methods could lead to comparable performance results.

As pointed out earlier in the paper, the knowledge engineering and data mining <sup>fi</sup>elds have remained largely independent. with little effort devoted to the issue of fusion of the two. Our research builds upon some of the prior work in that area. It is more comprehensive than the earlier studies by including seven of the most popular data mining methods and two performance measures. While many of those studies have used accuracy or error rate as the sole performance criterion (e.g., [2,19]), we assess performance using misclassi-<sup>fi</sup>cation cost, which is a more appropriate measure to use in cost-sensitive problems such as the one in this study. We also used the AUC measure for assessing classi<sup>fi</sup>er performance across the spectrum of possible costs.

Note that Pazzani et al. [35] found that adding domain knowledge resulted in signi<sup>fi</sup>cant cost reduction only when larger data sets were used. They used a relational learning algorithm in which the explanation-based part uses the knowledge base of an expert system and the inductive part adds, deletes, and revises existing rules in that knowledge base. In contrast, we did not change any of the internal parameters of the expert system, but used its output as an additional input to the classi<sup>fi</sup>ers. Also, note that we evaluated the effects of domain knowledge on the performance of seven widely-used data mining methods.

The main contribution of our research is in demonstrating that domain expertise captured in the form of a partial knowledge base can signi<sup>fi</sup>cantly improve the performance of a wide variety of classi<sup>fi</sup>ers on relatively small data sets. Instead of focusing on one or two learning methods, as has been the norm, we evaluated seven of the most widely used, commercially available methods, and found that the results hold across almost the entire spectrum. Another important contribution of this study is that the incorporation of domain knowledge affects different classi<sup>fi</sup>ers to different degrees, something that has not been empirically examined in prior research.

Our study opens up several avenues for future research. More studies are needed in different domains to understand what other types of knowledge could in<sup>fl</sup>uence performance. For instance, future studies could explore the effects of theory-based feature construction and subsequent re<sup>fi</sup>nement of that knowledge through data mining. We focused on a binary classi<sup>fi</sup>cation task in this study, but future studies could examine if the results extend to regression or value prediction tasks such as sales forecasting.

Bayesian belief networks have been successfully applied in several problems. Because the knowledge of the dependency structure of such networks is not usually available beforehand, prior research has primarily focused on deriving the structure from available data. However, if knowledgeable experts exist in the domain, their knowledge could be used to de<sup>fi</sup>ne the structure. For example, the domain knowledge in our study could be employed to develop a partial structure for a Bayesian network (e.g., [32]), which could then be re<sup>fi</sup>ned based on the available data. Comparing the performance of such a network with a network that is developed fully using data is an interesting future direction.

## References

[1] D. Aha, D. Kibler, Instance-based learning algorithms, Machine Learning 6 (1) (1991) 37–66.

[2] R. Ambrosino, B.G. Buchanan, The use of physician domain knowledge to improve the learning of rule-based models for decision-support, Proceedings of the Annual Fall Symposium of the American Medical Informatics Association, Washington DC., 1999, pp. 192–196.

[3] N.H. Barakat, A.P. Bradley, Rule extraction from support vector machines: a sequential covering approach, IEEE Transactions on Knowl edge and Data Engineering 19 (6) (2007) 729–741.

[4] A.P. Bradley, The use of the area under the ROC curve in the evaluation of machine learning algorithms, Pattern Recognition 30 (7) (1997) 1145–1159

[5] B.G. Buchanan, E.H. Shortliffe, Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project, Addison– Wesley, Reading, MA, 1984.

[6] Y. Chauvin, D.E. Rumelhart, Backpropagation: Theory, Architectures, and Applications, Lawrence Erlbaum Assoc., Hillsdale, NJ, 1995.

[7] H.M. Chung, K.Y. Tam, A comparative analysis of inductive learning algorithms, Intelligent Systems in Accounting, Finance and Management 2 (1) (1993) 3–18.

[8] H. Daniels, A. Feelders, M. Velikova, Integrating economic knowledge in data mining algorithms, Proceedings of the 8th International Conference on Society for Computational Economics: Computing in Economics and Finance, Aix-en-Provence, France, 2002.

[9] M. Doumpos, K. Kosmidou, G. Baourakis, C. Zopounidis, Credit risk assessment using a multicriteria hierarchical discrimination approach: a comparative analysis, European Journal of Operational Research 138 (2) (2002) 392–412.

[10] R. Dybowski, K.B. Laskey, J.W. Myers, S. Parsons, Introduction to the special issue on the fusion of domain knowledge with data for decision support, Journal of Machine Learning Research 4 (2003) 293–294.

[11] C. Elkan, The foundations of cost-sensitive learning, Proceedings of th 17th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, Seattle, WA, 2001, pp. 973–978.

[12] W. Fan, M.D. Gordon, P. Pathak, An integrated two-stage model for intelligent information routing, Decision Support Systems 42 (1) (2006) 362–374.

[13] W. Fan, P. Pathak, L. Wallace, Nonlinear ranking function representations in genetic programming-based ranking discovery for personalized Web search, Decision Support Systems 42 (3) (2006) 1338–1349.

[14] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From data mining to knowledge discovery in databases, AI Magazine 17 (3) (1996) 37–54.

[15] T. Fawcett, ROC graphs: notes and practical considerations for data mining researchers, HPL-2003-4, Intelligent Enterprise Technologies Lab, Hewlett-Packard, Palo Alto, CA, 2003.

[16] D. Hand, H. Mannila, P. Smyth, Principles of Data Mining, MIT Press, Cambridge, MA, 2001.

[17] J.A. Hanley, B.J. McNeil, A method of comparing the areas under receiver operating characteristic curves derived from the same cases, Radiology 148 (1983) 839–843.

[18] F. Hayes-Roth, D.A. Waterman, D. Lenat (Eds.), Building Expert Systems, Addison–Wesley, 1983.

[19] H. Hirsh, M. Noordewier, Using background knowledge to improve inductive learning: a case study in molecular biology, IEEE Expert 10 (1994) 3–6.

[20] R.R. Hoffman, The problem of extracting the knowledge of experts from the perspective of experimental psychology, AI Magazine (1987) 53–67.

[21] D.W. Hosmer, S. Lemeshow, Applied Logistic Regression, second edition, John Wiley & Sons, Inc., 2000.

[22] Z. Huang, H. Chen, C. Hsu, W. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[23] J. Huang, C.X. Ling, Using AUC and accuracy in evaluating learning algorithms, IEEE Transactionson Knowledge and Data Engineering 17 (3) (2005) 299–310.

[24] G.H. John, G.H. Langley, Estimating continuous distributions in Bayesian classi<sup>fi</sup>ers, in: P. Besnard, S. Hanks (Eds.), Proceedings of the 11th Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, Morgan Kaufmann, San Mateo, 1995, pp. 338–345.

[25] P.E. Johnson, What kind of expert should a system be? Journal of Medicine and Philosophy 8 (1) (1983) 77–97.

[26] S.S. Keerthi, S.K. Shevade, C. Bhattacharyya, K.R.K. Murthy, Improvements to Platt's SMO algorithm for SVM classifier design. Technical Report CD-99-14. Control Division, Dept of Mechanical and Production Engineering, National University of Singapore, 1999.

[27] C.N. Kim, R. McLeod, Expert, linear models, and nonlinear models of expert decision making in bankruptcy prediction: a lens model analysis, Journal of Management Information Systems 16 (1) (1999) 189–206.

[28] R. Kohavi, The power of decision tables, in: N. Lavrae, S. Wrobel (Eds.), Proceedings of the European Conference on Machine Learning, Springer Verlag, Berlin, Heidelberg, 1995, New York.

[29] R. Kohavi, A study of cross-validation and bootstrap for accuracy estimation and model selection, in: C.S. Mellish (Ed.), Proceedings of the 14th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, Morgan Kaufmann, San Mateo, CA, 1995, pp. 1137–1143.

[30] I. Kopanas, N.M. Avouris, S. Daskalaki, The role of domain knowledge in a large scale data mining project, in: I.P. Vlahavas, C.D. Spyropoulos (Eds.), Applications of Arti<sup>fi</sup>cial Intelligence, Lecture Notes in AI, no. 2308, Springer–Verlag, Berlin, Germany, 2002, pp. 288–299.

[31] M. Lam, Neural network techniques for <sup>fi</sup>nancial performance prediction: integrating fundamental and technical analysis, Decision Support Systems 37 (4) (2004) 567–581.

[32] H. Langseth, H. Nielsen, Fusion of domain knowledge with data for structural learning in object oriented domains, Journal of Machine Learning Research 4 (2003) 339–368.

[33] S.K. Murthy, Automatic construction of decision trees from data: a multidisciplinary survey, Data Mining and Knowledge Discovery 2 (4) (1998) 345-389.

[34] M. Pazzani, D. Kibler, The utility of knowledge in inductive learning, Machine Learning 9 (1) (1992) 57–94.

[35] M. Pazzani, C. Merz, P. Murphy, K. Ali, T. Hume, C. Brunk, Reducing misclassi<sup>fi</sup>cation costs, Proceedings of the 11th Conference on Machine Learning. Rutgers Univ., New Brunswick, NJ, 1994, pp. 217–225.

[36] J. Platt, Fast training of support vector machines using sequential minimal optimization in: B. Schölkopf C. Burges A. Smola (Eds.) Advances in Kernel Methods — Support Vector Learning, MIT Press, 1998, pp. 185–208.

[37] C. Pohle, Integrating and updating domain knowledge with data mining, in: M.H. Scholl T Grust (Eds.) Proceedings of the VLDB 2003 PhD Workshop (electronic edn.), Berlin, Germany, 2003.

[38] F. Provost, T. Fawcett, Robust classi<sup>fi</sup>cation for imprecise environments, Machine Learning 42 (3) (2001) 203–231.

[39] F. Provost, T. Fawcett, R. Kohavi, The case against accuracy estimation for comparing induction algorithms, Proceedings of the 15th International Conference on Machine Learning, Madison, WI, 1998, pp. 445–453

[40] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1) (1986) 81–106.

[41] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, 1993.

[42] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representations by error propagation, in: D.E. Rumelhart, J.L. McClelland (Eds.), Parallel Distributed Processing, MIT Press, Cambridge, MA, 1986, pp. 318–362.

[43] S. Russell, P. Norvig, Arti<sup>fi</sup>cial Intelligence: A Modern Approach, Prentice Hall, Englewood Cliffs, NJ, 1995.

[44] Y.U. Ryu, W.T. Yue, Firm bankruptcy prediction: experimental comparison of isotonic separation and other classi<sup>fi</sup>cation approaches, IEEE Transactions on Systems, Man and Cybernetics, Part A 35 (5) (2005) 727–737.

[45] S. Siegel, Nonparametric Statistics for the Behavioral Sciences, McGraw-Hill, New York, NY, 1956.

[46] A.P. Sinha, J.H. May, Evaluating and tuning predictive data mining models using receiver operating characteristic curves, Journal of Management Information Systems 21 (3) (2005) 253–284.

[47] T.K. Sung, N. Chang, G. Lee, Dynamics of modeling in data mining: interpretive approach to bankruptcy prediction, Journal of Management Information Systems 16 (1) (1999) 63–85.

[48] D.A. Waterman, A Guide to Expert Systems, Addison–Wesley, Reading MA, 1986.

[49] S.M. Weiss, S.J. Buckley, S. Kapoor, S. Damgaard, Knowledge-based data mining, Proceedings of the 9th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. Washington D.C., 2003, pp. 456–461.

[50] S.M. Weiss, N. Indurkhya, Predictive Data Mining: A Practical Guide, Morgan Kaufmann, San Francisco, CA, 1998.

[51] S.M. Weiss, C.A. Kulikowski, Computer Systems that Learn: Classi<sup>fi</sup>cation and Prediction Methods from Statistics, Neural Nets, Machine Learning, and Expert Systems, Morgan Kaufmann, San Mateo, CA, 1991.

[52] G.M. Weiss, F. Provost, The effect of class distribution on classi<sup>fi</sup>er learning: an empirical study, Technical Report ML-TR-44, Dept. of Computer Science, Rutgers Univ., 2001.

[53] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Technigues, Morgan Kaufmann, San Francisco, CA. 2005.

[54] H. Zhao S. Ram Constrained cascade generalization of decision trees JEEE Transactions on Knowledge and Data Engineering 16 (6) (2004) 727–739.

[55] H. Zhao, A.P. Sinha, An ef<sup>fi</sup>cient algorithm for generating generalized decision forests, IEEE Transactions on Systems, Man, and Cybernetics, Part A 35 (5) (2005) 754–762.

[56] D. Zhu, G. Premkumar, X. Zhang, C. Chu, Data mining for network intrusion detection: a comparison of alternative methods, Decision Sciences 32 (4) (2001) 635–660.

![](/api/attachments/77222FJ9/fulltext/images/1f8ee7aad3281aff7bd84d334909f865a528cae630419baf06fb0a9122d76858.jpg)

Atish P. Sinha is a Professor of MIS and Roger L. Fitzsimonds Distinguished Scholar at the Sheldon B. Lubar School of Business, University of Wisconsin– Milwaukee. He earned his Ph.D. in business, with a concentration in Arti<sup>fi</sup>cial Intelligence, from the University of Pittsburgh. His current research interests are in the areas of data mining, data warehousing, and component-based software engineering. His research has been published in several journals, including Communications of the ACM, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Transactions on Software Engineering, IEEE

Transactions on Systems, Man, and Cybernetics, Information Systems Research, International Journal of Human-Computer Studies, and Journal of Management Information Systems. Professor Sinha is a member of ACM, AIS, and INFORMS. He served as the co-chair of the 16th Workshop on Information Technologies and Systems (WITS) in 2006.

![](/api/attachments/77222FJ9/fulltext/images/caae8493c38baa16a0e2ee8f372a7d512dd6942043b8cf7bfb5984e8b80fbd67.jpg)

Huimin Zhao is an Associate Professor of MIS at the Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee. He earned his Ph.D. in MIS from The University of Arizona. His current research interests are in the areas of data mining, data integration, and medical informatics. His research has been published in several journals, including Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems, Data and Knowledge Engineering, Journal of Management Information Systems, and Decision Support

Systems. He serves on the editorial review board of the Journal of Database Management. He is a member of IEEE, AIS, IRMA, and INFORMS Information Systems Society.
