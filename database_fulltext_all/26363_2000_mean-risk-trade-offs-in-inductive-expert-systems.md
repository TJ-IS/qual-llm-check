---
otero_id: 26363
otero_key: "JEEZCSBM"
title: "Mean-Risk Trade-Offs in Inductive Expert Systems"
authors: "Vijay S. Mookerjee; Michael V. Mannino"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.2.137.11777"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/JEEZCSBM/fulltext/images/b5e18871e87349ff47c0317c83776fd19f11c300b8c63df832de9bd1c3407d4a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Mean-Risk Trade-Offs in Inductive Expert Systems

Vijay S. Mookerjee, Michael V. Mannino,

## To cite this article:

Vijay S. Mookerjee, Michael V. Mannino, (2000) Mean-Risk Trade-Offs in Inductive Expert Systems. Information Systems Research 11(2):137-158. http://dx.doi.org/10.1287/isre.11.2.137.11777

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2000 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/JEEZCSBM/fulltext/images/3ec353b7ad2a8fd880e9e5c4356f8fa0b6d39bb692ce62e5385716f53d07553a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Mean-Risk Trade-Offs in Inductive Expert Systems

Vijay S. Mookerjee • Michael V. Mannino

Department of Management Science, Box 353200, University of Washington, Seattle, Washington 98195

Graduate School of Business Administration, Campus Box 165, P. O. Box 173364, University of Colorado at Denver,

Denver, Colorado 80217

mookerje@u.washington.edu • mmannino@carbon.cudenver.edu

otably absent in previous research on inductive expert systems is the study of meanrisk trade-offs. Such trade-offs may be significant when there are asymmetries such as unequal classification costs, and uncertainties in classification and information acquisition costs. The objective of this research is to develop models to evaluate mean-risk trade-offs in value-based inductive approaches. We develop a combined mean-risk measure and incorporate it into the Risk-Based induction algorithm. The mean-risk measure has desirable theoretical properties (consistency and separability) and is supported by empirical results on decision making under risk. Simulation results using the Risk-Based algorithm demonstrate: (i) an order of magnitude performance difference between mean-based and risk-based algorithms and (ii) an increase in the performance difference between these algorithms as either risk aversion, uncertainty, or asymmetry increases given modest thresholds of the other two factors.

(Risk Aversion in Expert Systems; Value-Based System Design; Inductive Expert Systems)

## 1. Introduction

Inductive expert systems have become an important decision-support tool as evidenced by considerable attention in the academic literature and business press. Commercial applications of inductive expert systems include fault diagnosis (Irani et al. 1993), bank failure prediction (Tam and Kiang 1990), and industry and occupation code prediction (Creecy et al. 1992). The primary goal of an inductive expert system is to perform at the same level of human experts. Inductive expert systems are commonly used to support classification tasks, that is, tasks in which an object has to be assigned to one of n categories using its significant features (Weiss and Kulikowski 1991). Such systems can provide many benefits to an organization, such as reducing decision-making time, improving the consistency of decisions, and reducing dependence on scarce human experts.

## 1.1. Problem and Motivation

Most inductive expert systems are designed under the assumption of a risk-neutral decision maker. A riskneutral decision maker cares only about expected payoffs (Landsburg 1988). However, a considerable amount of literature in decision theory, cognitive psychology, and financial economics has considered riskaverse decision makers (Sarin and Weber 1993). With risk aversion, a limit may be placed on performance variation (constrained risk approach), or expected performance may be sacrificed for reducing performance variation (mean-risk trade-off). Decision models with risk aversion have been developed in a variety of managerial situations. For example, in the manufacturing arena, business risk has been incorporated into the management of inventories (Singhal et al. 1994). Risk is a cornerstone feature of the celebrated capital asset pricing model (Sharpe 1964). Accounting studies, labeled as cost-volume-profit analysis, consider standard deviation of profit as part of the objective function (Magee 1975, Adar et al. 1977).

Expert systems with unequal and uncertain classification costs can involve risk considerations if the systems support individual decision makers. Expert systems in lending, medicine, troubleshooting, and debt collection may have these characteristics. As an example of unequal and uncertain classification costs, consider the problem of predicting uncollectible calls (Ezawa and Norton 1996) in the telecommunications industry. The cost of classifying a valuable paying customer as nonpaying can be much higher than classifying a nonpaying customer as paying. Both costs have high uncertainty because it is difficult to predict future customer behavior. Depending on the decision maker’s utility function, it may be important to balance mean and risk. A risk-neutral decision maker has equal preference for benefits and costs. A risk-averse decision maker may want to weigh misclassification costs higher than correct classification benefits. In this paper, we describe a method to make mean-risk trade-offs.

Despite the apparent link between value-sensitive induction and risk, there is little published work on risk-aware inductive systems. Nadiminti et al. (1996) incorporate risk into the ex post, normative value of information gathered for classification tasks. In reported classification systems, risk is either ignored or, in a few cases, treated as a constraint. There are several value-sensitive induction algorithms (Breiman et al. 1984, Tan 1993, Mookerjee and Dos Santos 1993, Turney 1995) that ignore risk. Assuming risk neutrality may undermine the value of inductive systems when the decision maker is risk-averse. When risk is treated as a constraint, the system is designed to limit performance variation without making explicit mean-risk trade-offs. If decision makers can quantify risk aversion, it is often better to make explicit trade-offs between mean and risk. To address these limitations in inductive expert systems, we develop and evaluate an approach that makes explicit mean-risk trade-offs.

## 1.2. Objectives and Contributions

Figure 1 outlines the main goals of this paper. The first goal is to develop a suitable measure of risk so that risk can be factored into inductive system design. To develop the measure, we identify two important elements of risk: sources of risk and aversion for risk. Sources of risk are factors that cause risk, and risk aversion deals with how decision makers trade off mean performance with risk. There are two main sources of risk: uncertainties and asymmetries. Uncertainties are measured in terms of the variance of the cost of acquiring an input and/or the variance of the classification cost corresponding to a {true class, assigned class} pair. Asymmetries in classification costs are captured by the spread in the mean values for these costs.

Figure 1 Outline of Research  
![](/api/attachments/JEEZCSBM/fulltext/images/fe902f8597a690e8868fdf0f0bd8c3a7798706eb0dd30b16638bf0c6f41f6ded.jpg)

Risk aversion is modeled in the following sense. We assume that the user (or decision maker) will pay c dollars to reduce one dollar squared of risk. The decision maker attempts to minimize a combined measure of mean and risk, termed mean-risk. Structurally, mean-risk is similar to a “mean plus constant times variance” measure, but the variance term is modified to ensure certain regularity properties, namely, consistency and separability. In addition, the mean-risk measure is consistent with empirical studies on how subjects relate risk to the magnitudes and uncertainties associated with rewards and penalties (Sarin and Weber 1993). A questionnaire can be used to assess the appropriate risk level for an individual decision maker. Maginn and Tuttle (1990) discuss the use of risk questionaries in portfolio decisions.

The second goal of this paper is to develop a meanrisk-based algorithm that incorporates the proposed risk measure in the construction of decision trees. We propose the risk-based (RB) algorithm that achieves this goal. The RB algorithm uses the sequential information model, a paradigm that has been used to design many induction algorithms.

We derive several analytical results that help reveal differences between mean-optimizing and mean-riskoptimizing algorithms. For nonsymmetric classification costs, the classification behavior of meanoptimizing algorithms is typically different from that of mean-risk algorithms. These differences can be summarized through the concept of a risky class. In a risky class, the absolute costs of misclassification and correct classification are relatively high. The RB algorithm tends to avoid risky classes to achieve greater economic stability. The RB algorithm also avoids classes and inputs with large cost uncertainties since these increase the risk involved in classification decisions.

To enhance the practical contribution of this study, we conduct extensive simulation experiments to examine relationships among the sources of variation and the impact on mean-risk performance. Our results demonstrate a significant difference in mean-risk performance (roughly an order of magnitude) between mean-based and risk-based algorithms. In addition, our results demonstrate that mean-risk performance differences between the algorithms increase as either risk aversion, classification cost asymmetry, or classification cost uncertainty increases, given some thresholds of the other two factors.

The remainder of this paper is organized as follows. Section 2 reviews related work on the design and performance evaluation of inductive systems. In § 3, we present the mathematics governing the mean-risk measure and prove several properties of this measure. Section 4 analytically examines differences between meanbased and risk-based algorithms to provide insights into the question: When do risk considerations lead to different designs? Section 5 experimentally examines the complex interactions of the factors affecting performance variation and deficiencies in existing “meanseeking” inductive approaches. Section 6 provides a summary and conclusion.

## 2. Related Work

Previous research on inductive expert systems has focused on pruning (growing the right size tree) to improve mean performance on unseen cases (Breiman et al. 1984, Quinlan 1987, Mingers 1989). Pruning achieves this by checking the tendency of the algorithm to overfit. Overfitting reduces mean performance because sampling variation causes differences between the training and test sets. By building a model that is too specialized for the training sample, mean performance degrades on the test set. A side effect of pruning is to reduce performance variation. Several pruning methods have been proposed. In these methods, the basic idea is to shorten overspecialized rules that may have been generated using small or variable partitions. Liang (1992) offers a variation wherein the rules of the inductive system are formed using hypothesis testing, rather than entropy reduction or some related information theoretic measure.

There is some evidence of risk aversion in inductive system design. Constrained risk methods attempt to limit performance variation without making a mean-risk trade-off. An example of a constrained risk approach is to ensure that no rule in the decision tree is less than 80% accurate (Gur-Ali and Wallace 1993). Another example is to leave a case as unclassified if there is not enough similar data in the training sample (Creecy et al. 1992). Constrained risk does not follow from risk neutrality, since risk-neutral users would not care about performance variation.

Although mean-risk trade-offs are uncommon in inductive systems design, they have been widely studied in other research on management decision making, including finance, manufacturing, and lending. A rich stream of research in finance has studied the mean and variation of stock returns using the framework proposed in the Capital Asset Pricing Model (CAPM) (Sharpe 1964). Singhal et al. (1993) borrow from ideas in the CAPM model and apply a mean-variance-based approach to ordering decisions in the classic Newsboy problem in inventory management. Starbird (1994) numerically examines how risk-averse suppliers react to customer acceptance sampling plans. In consumer loan granting, Altman and Haldeman (1995) propose a variety of risk-based credit-scoring models that are designed to make the profit from loans more stable. For currency loan diversification, Seppala (1994) studies a variety of mean-variance criteria.

## 3. Design of the Risk-Based Algorithm

Before describing the details of the Risk-Based algorithm, we develop a combined mean-risk measure for use in this algorithm. This measure is shown to possess two important properties: consistency and separability. We next provide a general introduction to valuesensitive induction and the design features of a typical induction algorithm. This is followed by a description of the Risk-Based algorithm.

## 3.1. Factors Affecting Risk

There are two main sources of risk studied: (1) asymmetries and (2) uncertainties. Asymmetries occur when the mean cost of classification varies across different true class, assigned class pairs. For example, consider a high-risk, high-return class and another where both risk and return are relatively low.<sup>1</sup> Such classification costs exhibit asymmetry. When asymmetries exist, choosing a high-risk, high-return class can lead to high cost variation.

One way to handle asymmetry is to penalize incorrect classification decisions more than what they are naturally penalized in a mean-seeking algorithm. From a purely mean-seeking point of view, a high-risk, high-return class may be equivalent to a low-risk, lowreturn one. However, from a combined mean-risk objective, a high-risk, high-return class may not be desirable. By placing an extra penalty on incorrect classification decisions, aversion to risky classes can be generated. Often, with such a penalty structure, a less risky class will be chosen even though the mean of the low-risk class is worse.

Another factor that leads to performance variation is uncertainty in input and classification costs. We capture the key aspects of uncertain input and classification costs without making the models of uncertainty unmanageably complex to estimate and implement. The uncertainty models below (Equations (1) and (2))

consist of a mean component and a random noise component. The mean component is a value depending on the input or the class pair (true, assigned). The noise component has zero mean and a variance that depends on the input or the class pair.

Input Cost Uncertainty:

$$
\tilde {I} _ {X _ {p}} = \mu_ {X _ {p}} + \tilde {\varepsilon} _ {X _ {p}},\tag{1}
$$

where, ${ \tilde { I } } _ { X _ { p } }$ is the random variable representing the information cost of the $p ^ { t h }$ input $X _ { p } , p = 1 , 2 , \ldots n$

$$
\begin{array}{r l} & E (\tilde {I} _ {X _ {p}}) = \mu_ {X _ {p}}; \\ & E (\tilde {\varepsilon} _ {X _ {p}}) = 0; \\ & V (\tilde {\varepsilon} _ {X _ {p}}) = \sigma_ {X _ {p}} ^ {2}. \end{array}
$$

Classification Cost Uncertainty:

$$
\tilde {C} _ {i k} = \mu_ {i k} + \tilde {\varepsilon} _ {i k}\tag{2}
$$

where, ${ \tilde { C } } _ { i k }$ is the random variable representing the cost of classifying a case of class i as class k.

$$
\begin{array}{r} E (\tilde {C} _ {i k}) = \mu_ {i k}; \\ E (\tilde {\varepsilon} _ {i k}) = 0; \\ V (\tilde {\varepsilon} _ {i k}) = \sigma_ {i k} ^ {2}. \end{array}
$$

Uncertainty or variation in the cost of an input may arise from a variety of sources. For example, the cost of a clinical test may be influenced by factors such as how the test was conducted, who conducted the test, etc. There may also be random fluctuations in the cost. The uncertainty associated with the cost of an input may also depend on the values of other relevant inputs. For example, the uncertainty in the cost of obtaining employment history may be related to the income or the age of the applicant. These interactions can make the model of uncertainty extremely complex. Considering limitations of computing and estimation effort, we focus on input cost uncertainties that are independent of the state of other inputs.

Uncertainty in classification costs may arise from a variety of causes. Here, the mean and variance of the classification cost for a true class, assigned class pair is assumed to depend only on the pair and not on the inputs specific to the problem. Sometimes this assumption may be violated. For example, the uncertainty in the cost associated with granting a loan when it should not have been granted could depend upon the amount of the loan. However, if the classes are sufficiently detailed, the true class, assigned class pair is sufficient to determine the uncertainty in the classification cost for that pair. For example, if we have two separate classes, one for “grant-high-loan” and another “grantlow-loan” (and possibly, other more detailed classes, as required), uncertainty would only depend on the class pair.

## 3.2. Mean-Risk Criterion

Given asymmetry, uncertainty, and the user’s risk aversion, we need to develop a measure that can help a decision maker evaluate choices. To this end, there exists a large body of work on evaluating decisions under risk. Broadly speaking, the research in this area can be divided into two streams. In some research, risk is viewed as a primitive, and it is assumed that decision makers can directly make judgments about risk. Examples of primitive risk measures are variance, expectation combined with variance (Pollatsek and Tversky 1970), and exponential risk models (Keller et al. 1986). In other research, risk is derived from assumptions about the decision-maker’s utility function. One derived measure of risk uses the widely cited utility preference model by Von Neumann and Morgenstern (1947). This model assumes that the decision maker maximizes expected utility. Using this model, Pratt (1964) calculates a risk premium that is the amount a decision maker will pay to insure against the risk of an uncertain payoff. Another example of a derived risk measure is the standard deviation term in the Capital Asset Pricing Model (CAPM). Standard deviation as a measure of risk emerges from assumptions of expected utility maximization, quadratic utility, and market equilibrium.

Despite the considerable literature on risk models there is no standard, universally applicable risk measure. In this study, we start out with a simple primitive risk measure (variance) and specialize the measure for classification decisions. The proposed measure has good theoretical properties and empirical support.

Simple Mean-Variance Measure. Consider a simple mean plus constant times variance measure. This measure has certain problems that could lead to inconsistent choices in the context of classification systems.

To demonstrate a problem with a simple meanvariance criterion, consider a decision maker who receives the set of payoffs (costs) with probabilities as shown below:

<table><tr><td>Cost($)</td><td>-50</td><td>25</td><td>100</td><td>-100</td></tr><tr><td>Probability</td><td>0.2</td><td>0.3</td><td>0.25</td><td>0.25</td></tr></table>

$$
\begin{array}{r l} E (\text {Cost}) = & - 5 0 ^ {*} 0. 2 + 2 5 ^ {*} 0. 3 + 1 0 0 ^ {*} 0. 2 5 \\ & - 1 0 0 ^ {*} 0. 2 5 = - 2. 5. \end{array}
$$

$$
\begin{array}{r l} V (\text {Cost}) = & 0. 2 ^ {*} (- 5 0) ^ {2} + 0. 3 ^ {*} (2 5) ^ {2} + 0. 2 5 ^ {*} (1 0 0) ^ {2} \\ & + 0. 2 5 ^ {*} (1 0 0) ^ {2} - (2. 5) ^ {2} = 5 6 8 1. 3 () ^ {2}. \end{array}
$$

Assume $\gamma = 0 . 0 5$ dollars per dollar squared. The simple mean-variance criterion can be calculated to be $- 2 . 5 \ : + \ : 0 . 0 5 ^ { * } ( 5 6 8 1 . 3 ) \ : = \ : \$ 28 1 . 5 7 .$

Let us consider that the last cost is changed from $- \$ 100t o \ t o \ -\$ 110.$ . This change should be preferable because one of the costs has been reduced. However, the new value of the simple mean-variance criterion is 5 $+ ~ 0 . 0 5 ^ { * } 6 2 1 2 . 5 = \ S 3 0 5 . 6 3$ . The mean-variance criterion has increased (become worse) when one of the costs was reduced. Conversely, the mean-variance criterion will improve when one of the costs is increased. This situation is inconsistent because most decision makers would prefer a lower cost to a higher one.

To correct this inconsistency, we replace the variance term with a risk term in the simple criterion. The risk term does not exhibit inconsistency; yet it captures, in spirit, a measure of cost variation. We note that the inconsistencies shown above would not have occurred if the decision-maker’s aversion for risk $( \gamma )$ was chosen lower than 0.004706. Inconsistent choices are more likely at higher values of $\gamma .$ We therefore attempt to develop a mean-variance-based criterion that is consistent for all values of $\gamma$ greater than zero.

Notation and Definitions. The following notation and definitions will be used:

$\tilde { T } , \tilde { T } _ { j }$ : random variables for the total cost of the tree and the $j ^ { t h }$ path of the tree. The total cost of the tree (path) is the sum of the information cost and classification cost incurred when the tree (path) is used to solve a classification problem.

$\tilde { I } , \tilde { I } _ { j }$ : random variables for the information cost of the tree and the $j ^ { t h }$ path of the tree. The information cost of the tree (path) is the cost of collecting the information inputs when the tree (path) is used to solve a classification problem.

$\tilde { C } , \tilde { C } _ { j }$ : random variables for the classification cost of the tree and the $j ^ { t h }$ path of the tree. The classification cost of the tree (path) is the classification cost incurred when the tree (path) is used to solve a classification problem.

$$
\tilde {T} = \tilde {\dot {I}} + \tilde {C}.
$$

$$
\tilde {T} _ {j} = \tilde {I} _ {j} + \tilde {C} _ {j}.
$$

J<sup>˜</sup> : random variable for the path of the tree used to solve a case. $\boldsymbol { \tilde { J } } = \mathrm { \bar { 1 } } , 2 , \dots \boldsymbol { \Pi } .$

$\pi _ { j }$ : probability that the $j ^ { t h }$ path is used to classify a case.

c : user’s aversion for risk. The user should buy (sell) a unit of risk for c dollars.

$F _ { \tilde { \beta } } ( x )$ : cumulative distribution function for any random variable ${ \tilde { \beta } } .$

$f _ { \tilde { \beta } } ( x )$ <sup>:</sup> density function for any random variable ${ \tilde { \beta } } .$

As before, we start with a simple and intuitive meanvariance criterion: $\mathrm { E } ( \tilde { T } ) + \gamma [ \mathrm { V } ( \tilde { T } ) ]$ . To evaluate this criterion, we first evaluate $\mathrm { V } ( \tilde { T } )$ , the variance of the total cost for the tree. Conditioning the random variable $\tilde { T }$ on ${ \tilde { J } } ,$ the random variable for the path of the tree, we get:

$$
\begin{array}{l} P (\tilde {T} \leq x) = \sum_ {j = 1} ^ {\pi} P (\tilde {J} = j) \cdot P (\tilde {T} \leq x | \tilde {J} = j) \\ = \sum_ {j = 1} ^ {\Pi} \pi_ {j} \cdot P (\tilde {T} \leq x | \tilde {J} = j). \end{array}\tag{3}
$$

Using the letter F for a cumulative distribution and the letter f for a density, we can write:

$$
F _ {\tilde {T}} (x) = \sum_ {j = 1} ^ {\Pi} \pi_ {j} \cdot F _ {\tilde {T} _ {j}} (x);\tag{4}
$$

$$
f _ {\tilde {T}} (x) = \sum_ {j = 1} ^ {\Pi} \pi_ {j} \cdot f _ {\tilde {T} _ {j}} (x);\tag{5}
$$

$$
\begin{array}{r l} V (\tilde {T}) & = \int_ {- \infty} ^ {\infty} (x - \mu_ {\tilde {T}}) ^ {2} f _ {\tilde {T}} (x) d x \\ & = \int_ {- \infty} ^ {\infty} (x - \mu_ {\tilde {T}}) ^ {2} \bigg (\sum_ {j = 1} ^ {\Pi} \pi_ {j} \cdot f _ {\tilde {T} _ {j}} (x) \bigg) d x; \end{array}\tag{6}
$$

where $\mu _ { \tilde { T } }$ is the mean of the total cost (input plus classification) for the tree.

Simplifying the above we get:

$$
V (\tilde {T}) = \sum_ {j = 1} ^ {\Pi} \pi_ {j} \cdot \left(\sigma_ {\tilde {T} _ {j}} ^ {2} + \mu_ {\tilde {T} _ {j}} ^ {2}\right) - \left(\sum_ {j = 1} ^ {\Pi} \pi_ {j} \cdot \mu_ {\tilde {T} _ {j}}\right) ^ {2} \text {   where   }\tag{7}
$$

$\mu _ { \tilde { T } _ { j } }$ is the mean of the total cost (input cost plus classification cost) for the $j ^ { t h }$ path in the tree and $\sigma _ { T _ { i } } ^ { 2 }$ is the variance of the total cost for the $j ^ { t h }$ path in the tree.

Differentiating Equation (7) with respect to $\mu _ { \tilde { T } _ { j } }$ we get:

$$
\frac {\delta V (\tilde {T})}{\delta \mu_ {\tilde {T} _ {j}}} = 2 \pi_ {j} (\mu_ {\tilde {T} _ {j}} - \mu_ {\tilde {T}}).\tag{8}
$$

If $( \mu _ { \tilde { T } _ { j } } - \mu _ { \tilde { T } } ) < 0$ , then for certain values of $\gamma ,$ the total cost variance of the tree improves (i.e., decreases) as the mean total cost for a particular path increases. Conversely, the user’s utility as defined in the meanvariance criterion can increase with the total mean cost in a particular path.

The above problem arises because the meanvariance criterion calculates the variance across paths of the tree. To resolve this problem, we first consider the variance for each path and calculate the tree variance as the expectation of the path variances. As shown later, a further modification is required to completely resolve the problem.

The revised mean-variance criterion (K(Tree)) is defined in Equation (9). In Equation (9), K(Tree)) is an expectation of the mean-variance values for each path in the tree (K(Path ); defined in Equation (10)):

$$
K (T r e e) = \sum_ {j = 1} ^ {\Pi} \pi_ {j} \cdot K (P a t h _ {j}).\tag{9}
$$

The mean-variance criterion for a path K(Path<sub>j</sub>) is defined as:

$$
K (P a t h _ {j}) = E (\tilde {T} _ {j}) + \gamma V (\tilde {T} _ {j}).\tag{10}
$$

Information Systems Research Vol. 11, No. 2, June 2000

For a given path, the input cost for a path is independent of the classification cost for the path $( \tilde { I } _ { j }$ and ${ \tilde { C } } _ { j }$ are independent). Hence, we can write:

$$
E (\tilde {T} _ {j}) = E (\tilde {I} _ {j}) + E (\tilde {C} _ {j}).\tag{11}
$$

$$
V (\tilde {T} _ {j}) = V (\tilde {I} _ {j}) + V (\tilde {C} _ {j}).\tag{12}
$$

The variance of the classification cost for a path is given by

$$
\begin{array}{l} V (\tilde {C} _ {j}) = E (\tilde {C} _ {j} ^ {2}) - (E (\tilde {C} _ {j})) ^ {2} \\ = \sum_ {i = 1} ^ {m} p _ {i k _ {j}} (\sigma_ {i k _ {j}} ^ {2} + \mu_ {i k _ {j}} ^ {2}) - \left(\sum_ {i = 1} ^ {m} p _ {i k _ {j}} \mu_ {i k _ {j}}\right) ^ {2} \end{array}\tag{13}
$$

where $p _ { i k _ { i } }$ is the probability that a case with class $=$ i is classified as class $= k$ at the end of the jth path and $\mu _ { i k } , \sigma _ { i k _ { j } } ^ { 2 }$ are the mean and variance, respectively, of the classification cost corresponding to the pair $\{ i , k _ { j } \}$

Unfortunately, the quantity $V ( \tilde { C } _ { j } )$ can be inconsistent. At certain values of $\gamma ,$ it is beneficial to increase the mean classification cost to reduce the mean-risk measure. This can be easily shown by differentiating $V ( \tilde { C } _ { j } )$ with respect to $\mu _ { i k }$

$$
\begin{array}{r l} \frac {\partial V (\tilde {C} _ {j})}{\partial \mu_ {i k _ {j}}} & = 2 p _ {i k _ {j}} \mu_ {i k _ {j}} - 2 E (\tilde {C} _ {j}) p _ {i k _ {j}} \\ & = 2 p _ {i k _ {j}} (\mu_ {i k _ {j}} - E (\tilde {C} _ {j}). \end{array}\tag{14}
$$

Hence, if $\mu _ { i k _ { j } } < E ( \tilde { C } _ { j } )$ , the path mean-variance measure $K ( P a t h _ { j } )$ can be inconsistent for certain values of $\gamma .$ Hence we revise the variance term $V ( \tilde { C } _ { j } )$ to a risk term $R ( \tilde { C } _ { j } )$ as follows:

$$
R (\tilde {C} _ {j}) = \sum_ {i \neq k _ {j}} p _ {i k _ {j}} (\sigma_ {i k _ {j}} ^ {2} + \mu_ {i k _ {j}} ^ {2}) + p _ {k _ {j} k _ {j}} \sigma_ {k _ {j} k _ {j}} ^ {2}.\tag{15}
$$

The thought behind the expression in Equation (15) is as follows. The variance term defined in Equation (13) is problematic for two reasons. First, the term $- ( E ( \tilde { C } _ { j } ) ) ^ { 2 }$ leads to inconsistency because lowering the expected classification cost increases the variance. We avoid this problem by dropping this term in the revised mean-risk measure. The remaining term $E ( \tilde { C } _ { j } ^ { 2 } )$ still has problems because it includes a term for the square of the mean classification cost when the true class is equal to the assigned class. Hence we modify Equation (13) by excluding any component involving $\mu _ { i k _ { j } }$ , where $\begin{array} { r } { i \ = \ k _ { j } . } \end{array}$ After excluding correct classifications, increasing the mean classification cost for any {true class, assigned class} pair should never be beneficial.

With the above modifications, the mean-risk value for the $j ^ { t h }$ path is given by:

$$
M R _ {j} = E (\tilde {I} _ {j}) + E (\tilde {C} _ {j}) + \gamma (V (\tilde {I} _ {j}) + R (\tilde {C} _ {j})).\tag{16}
$$

The mean-risk value for the tree is given by:

$$
\begin{array}{c} M R = \sum_ {j = 1} ^ {\Pi} \pi_ {j} [ E (\tilde {I} _ {j}) + E (\tilde {C} _ {j}) \\ \quad + \gamma (V (\tilde {I} _ {j}) + R (\tilde {C} _ {j})) ], \quad \text {or} \\ M R = \sum_ {j = 1} ^ {\Pi} \sum_ {i = 1} ^ {m} \pi_ {j} (E (\tilde {I} _ {j}) + p _ {i k _ {j}} \mu_ {i k _ {j}}) + \gamma \sum_ {j = 1} ^ {\Pi} \\ \pi_ {j} \Big (V (\tilde {I} _ {j}) + \sum_ {i \neq k _ {j}} p _ {i k _ {j}} (\sigma_ {i k _ {j}} ^ {2} + \mu_ {i k _ {j}} ^ {2}) + p _ {k _ {j} k _ {j}} \sigma_ {k _ {j} k _ {j}} ^ {2} \Big). \end{array}\tag{17}
$$

(18)

The first term in Equation (18) is the usual expression for the mean total cost of classification calculated across the paths in the tree. The second term is the risk of the classification cost for the tree. The risk term has a direct interpretation. It consists of a term that is the second moment of the positive classification cost about zero, plus a term for the uncertainty of the negative classification cost. We next prove that the mean-risk measure defined in Equation (18) is consistent. Consistency requires that the mean-risk measure should increase with the mean cost of classification for any {i, k} pair $( \mu _ { i k } )$

Other functional forms may be considered to develop a primitive measure of risk in inductive systems. We think that such a measure would depend on the following factors:

1. Mean positive classification costs $( \mu _ { i j } ,$ i not equal to $j )$ .

2. The variance of the classification cost corresponding to each {true class, assigned class} pair.

3. A constant representing the user’s aversion for risk.

The measure proposed in Equation (18) is a natural extension of the mean-variance measure and hence uses second moments of classification costs. Higher moments of classification costs would also capture risk, but they would become more difficult to comprehend because the user’s aversion for risk (as measured by these higher moments) would have to be captured. Using second moments for evaluating risk is also consistent with a quadratic utility function and symmetric classification costs. The mean-variance model used in finance (Markowitz 1952) makes these assumptions. Empirical evidence and analytical tractability have validated these assumptions (Huang and Litzenberger 1988) in portfolio selection.

Proposition 1. The Mean-Risk measure in Equation (18) is consistent for all values of c greater than zero.

Proof. To prove Proposition 1, we differentiate Equation (18) with respect to $\mu _ { i j } .$ Let h be the set of paths ending with class - k. We have:

$$
\frac {\partial M R}{\partial \mu_ {i k}} = \sum_ {j \in \theta} \pi_ {j} p _ {i k} + \gamma \Bigl \{\sum_ {j \in \theta} 2 \pi_ {j} p _ {i k} \mu_ {i k} \Bigr \};
$$

$$
\text {   for   } i \neq k, \frac {\partial M R}{\partial \mu_ {i k}} = \sum_ {j \in \theta} \pi_ {j} p _ {i k} (1 + 2 \gamma \mu_ {i k}) > 0,
$$

since $\mu _ { i k } > 0 ;$

$$
\mathrm{for} i = k, \frac {\partial M R}{\partial \mu_ {i k}} = \sum_ {j \in \theta} \pi_ {j} p _ {i k} > 0,\tag{19}
$$

which proves consistency. 

In addition to consistency, the Mean-Risk measure in Equation (18) is supported by empirical research on decision making under risk. While there is less than full agreement on what measure best captures risk, some properties of risk are generally agreed upon (Sarin and Weber 1993). These include: (1) risk increases with an increase in range, variance, or expected loss; (2) risk increases if the rewards and penalties increase by a constant amount; and (3) risk increases if the rewards and penalties are multiplied by a positive constant greater than one. We show below that the first two properties are always satisfied by the Mean-Risk measure in Equation (18) and that the third property is more likely to be satisfied at higher values of the risk-aversion constant (c).

The first of the above three findings is satisfied by the Mean-Risk measure in Equation (18). The measure clearly increases with an increase in the variance of the penalty and the reward (negative costs). Although range is not directly captured in our expressions for risk, we expect that range and variance will typically be positively correlated. Risk also increases with the magnitude of loss because we have placed an extra penalty on losses (positive costs) by taking the square of these costs. It is easy to see that if $f ( x ) = x ^ { 2 } ,$ , then $f ^ { \prime } ( x ) > 0 ,$ , for $x > 0$

To show that the second finding is satisfied, let y and $x$ be the random variables for rewards and penalties, respectively. Then, for $a > 0 ,$ since $E ( y ) + E ( x ) = E ( y$ $- \ a ) \ + \ E ( x \ + \ a ) .$ , the expected cost does not change with the additive transformation. On the other hand, $E [ ( x + a ) ^ { 2 } ]$ is greater than $E [ ( x ) ^ { 2 } ]$ , if a is positive. Hence, the mean-risk measure should increase with an additive transformation.

To examine the third finding we compare the meanrisk expression E(y) $~ + ~ E ( x ) ~ + ~ E ( x ) ~ + ~ E ( x ^ { 2 } )$ with a[E(y) $+ \ E ( x ) ] \ + \ a ^ { 2 } E ( x ^ { 2 } )$ , for $a > 1$ . We consider three cases below.

Case 1: If $[ \operatorname { E } ( y ) ~ + ~ \operatorname { E } ( x ) ] ~ > ~ 0 ,$ then a multiplicative transformation will always lead to an increase in mean-risk. This case, however, is trivial because both mean and risk increase due to the transformation. Hence, in this case, a multiplicative transformation will reduce utility even for a risk-neutral decision maker (that $\mathbf { i s } , \gamma = 0 )$

Case 2: If $[ \operatorname { E } ( y ) ~ + ~ \operatorname { E } ( x ) ] ~ = ~ 0 ,$ a multiplicative transformation will have no effect on the mean, but will increase the risk. Hence, mean-risk will increase for a risk-averse decision maker $( \gamma > 0 )$

Case 3: If $[ \operatorname { E } ( y ) ~ + ~ \operatorname { E } ( x ) ] ~ < ~ 0 ,$ , then a multiplicative transformation will make the mean term decrease (become better) and the risk term increase (become worse). Hence, in this case, the value of $\gamma$ determines whether mean-risk measure increases or decreases. As $\gamma$ increases (the decision maker is more risk-averse), a multiplicative transformation will likely lead to an increase in the mean-risk measure.

## 3.3. Induction Algorithms

Before we discuss the details of the RB algorithm, we discuss the general structure of induction algorithms. Many decision-tree induction algorithms are based on the sequential decision-making paradigm (Moore and Whinston 1986, 1987). In this paradigm, information relevant to the decision is sequentially acquired, that is, the next piece of information acquired depends on the values observed for previously acquired inputs. Once enough information has been acquired, the classification decision is made.

Induction algorithms that are based on the sequential decision paradigm typically perform three main tasks: (i) input selection, (ii) stopping, and (iii) classification. Input selection is the task of selecting an input among a set of candidate inputs to label a nonleaf node in the tree. Input selection is performed using a gain function; the input with the highest gain is selected. For example, in the popular ID3 algorithm, the gain function measures the reduction in information entropy due to an input (Quinlan 1986). On the other hand, the VB algorithm uses the ratio of benefit to cost as the gain function (Mookerjee and Dos Santos 1993). The benefit of an input is the difference between the cost of classification before and after selecting the input. The cost of an input is the given information acquisition cost.

Stopping is the task of determining when creation of further nonleaf nodes along a path in the tree should be terminated. If the gain for the best input is less than or equal to a cutoff value, further creation of nonleaf nodes is terminated. The cutoff values for the ID3 and VB algorithms are zero and one, respectively. In the ID3 algorithm, creation of nonleaf nodes continues until none of the remaining inputs are informative. The VB algorithm stops when the cost incurred to acquire any remaining input exceeds the benefit.

Classification is the task of selecting a class to label a leaf node in the tree. The ID3 algorithm selects the class with the maximum frequency, whereas the VB algorithm selects the one that minimizes classification costs. In Appendix A, we describe the mathematics governing input selection, stopping, and classification for the VB algorithm.

## 3.4. The RB Algorithm

In this subsection we provide details of mathematics governing the RB algorithm. We first describe the calculation of gain in the RB algorithm. The computation of gain in the RB algorithm uses a partition analogue of the mean-risk measure in Equation (18). A set of child partitions is created by using an input to split a parent partition. In the partition analogue of Equation (18), $k _ { j }$ stands for the class chosen in the jth child partition. The gain expression is used to define the input selection, stopping, and classification processes used in the algorithm.

Gain Computation. Figure 2 shows input $X _ { p }$ being used to partition a set of cases into $q$ child partitions. We describe below how the RB algorithm computes gain for the partitioning input $X _ { p }$

Let,

j<sub>b</sub> -mean-risk measure in parent partition;

$$
E _ {j} = \text { mean   cost   in   } j \text { th   partition } = \Sigma_ {i} p _ {i j} \mu_ {i k _ {j}}; \text {   and }
$$

$$
R _ {j} = \text { risk   of   cost   in   } j \text { th   partition } = \Sigma_ {i \neq k _ {j}} p _ {i j} (\sigma_ {k _ {j}} ^ {2} + \mu_ {i k _ {j}} ^ {2}) +
$$

$p _ { k _ { j } j } \sigma _ { k _ { j } k _ { j } } ^ { 2 } ,$ where $k _ { j }$ is the class chosen to minimize the mean-risk measure in the jth partition, and $p _ { i j }$ is the probability of class i in partition j.

The mean-risk measure after observing the input z includes the mean cost of observing the input and the additional risk due to uncertainties in the cost of acquiring the input.

Let,

$\mu _ { X _ { P } }$ be the mean information cost of input $X _ { p } ,$

$\sigma _ { X _ { p } } ^ { 2 }$ be the variance of the information cost of input $X _ { p } ,$ and

$q _ { j }$ be the probability that input $X _ { p }$ occurs in the jth state, $j = 1 , 2 , . . . q .$

We define the mean-risk measure after observing the input and considering the cost of acquiring it as below:

$$
\kappa_ {a} = \sum_ {j = 1} ^ {q} q _ {j} E _ {j} + \mu_ {X _ {p}} + \gamma \biggl [ \sum_ {j = 1} ^ {q} q _ {j} R _ {j} + \sigma_ {X _ {p}} ^ {2} \biggr ].\tag{20}
$$

The gain of an input is defined as the difference between the criterion measure before and after observing the input. Assume that r is the best class in the parent partition. Hence, the Mean-Risk measure before measuring an input $( \mathbf { k } _ { b } )$ is given by:

Figure 2 q Child Partitions Created by Input $X _ { p }$  
![](/api/attachments/JEEZCSBM/fulltext/images/66c62075eb11fba0d26ad8767dd7dd54ad803a9b4b37eae1837c190bdb97867f.jpg)

$$
\kappa_ {b} = \sum_ {i = 1} ^ {m} \theta_ {i} \mu_ {i r} + \gamma \Bigl \{\sum_ {i \neq r} \theta_ {i} (\mu_ {i r} ^ {2} + \sigma_ {i r} ^ {2}) + \theta_ {r} \sigma_ {r r} ^ {2} \Bigr \},\tag{21}
$$

where $\theta _ { i } =$ of the probability of the ith class in the parent partition

$$
= \sum_ {j = 1} ^ {q} q _ {j} p _ {i j}.
$$

The gain of an input $( X _ { p } )$ is defined as below:

$$
g a i n (X _ {p}) = \kappa_ {b} - \kappa_ {a}.\tag{22}
$$

The three design principles below use the gain computation defined in Equation (22) and the mean-risk measure defined in Equation (21).

(1) Input Selection: Select the input with the highest input gain as defined in Equation (22).

(2) Stopping: Stop if the gain for all remaining inputs is less than or equal to zero.

(3) Classification: Label a leaf node with the class that minimizes the mean-risk measure.

## 3.5. Separability

When a parent partition is split into child partitions, the question arises: To guarantee maximum reduction in the mean-risk measure, will the mean-risk measure have to be jointly minimized across all the child partitions? If $s 0 ,$ a vector of classes will have to be chosen at each split. Since the number of vector combinations can potentially explode, joint optimization will result in a large search space. Separability implies that the mean-risk measure can be locally minimized for each child partition, and yet guarantee that the measure will be globally minimized across all child partitions. Hence, for computational reasons, it is important to examine the mean-risk measure for separability.

Proposition 2. The mean-risk measure in Equation (20) is separable.

Proof. From Equation (20) we find that because $\gamma$ is a constant it can be taken into the inner summation. In addition, the outer summation over j associates over the inner summations over i for both the first and second term. Hence, the mean-risk measure in Equation (20) can be rewritten as:

$$
\kappa_ {a} = \sum_ {j = 1} ^ {q} q _ {j} (E _ {j} + \gamma R _ {j}) + \mu_ {X _ {p}} + \gamma \sigma_ {x _ {p}} ^ {2}.\tag{23}
$$

In Equation (23), the term inside the parentheses represents the mean-risk measure for the $\bar { j } ^ { t h }$ child partition (denoted by MR ). Hence, Equation (23) can be rewritten as:

$$
M R = \sum_ {j = 1} ^ {q} q _ {j} M R _ {j} + \mu_ {X _ {p}} + \gamma \sigma_ {X _ {p}} ^ {2}.\tag{24}
$$

Assume that the vector k jointly minimizes the mean-risk measure in Equation (24). To prove separability it is necessary to show that the mean-risk measure can be locally minimized in the $j ^ { t h }$ partition, $j =$ $1 , 2 , \ldots q .$ . Thus separability implies that each component of the vector k can be independently chosen. Since the mean-risk measure across the child partitions is the expectation of the mean-risk measures of the individual child partitions, we have:

$$
\begin{array}{c} \underset {\mathbf {k}} {\text {Min}} (M R) = \underset {\mathbf {k}} {\text {Min}} \sum_ {j = 1} ^ {q} q _ {j} M R _ {j} + \mu_ {X _ {p}} + \gamma \sigma_ {X _ {p}} ^ {2} \\ = \sum_ {j = 1} ^ {q} q _ {j} \underset {\mathbf {k} _ {j}} {\text {Min}} M R _ {j} + \mu_ {X _ {p}} + \gamma \sigma_ {X _ {p}} ^ {2}. \end{array}\tag{25}
$$

Equation (25) proves that the mean-risk measure in Equation (20) is separable. 

## 4. Impact of Risk

To provide insights about a mean-risk-based algorithm, we examine the classification behavior of a meanseeking algorithm (VB) and a mean-risk-seeking one (RB). An algorithm based upon the mean-risk measure can be expected to classify differently than a meanbased one if cost uncertainties are introduced. While VB would ignore uncertainties, RB would explicitly attempt to avoid them.

It is more interesting, however, to find out if algorithms based upon these measures will classify differently if only classification cost asymmetries exist. In the analysis in this section, we isolate the impact of cost asymmetries by assuming that classification costs are certain (that is, $\sigma _ { i j } ^ { 2 } = 0 , \forall i , j )$ . To facilitate the analysis, we focus on a particular partition in which both VB and RB are attempting to choose the best class. The class chosen by VB and RB will be different if two con-

ditions are satisfied:

$$
1. \sum_ {i = 1} ^ {m} p _ {i} \mu_ {i r} <   \sum_ {i = 1} ^ {m} p _ {i} \mu_ {i k}\tag{26}
$$

where r and k are the classes chosen by VB and RB, respectively, and $p _ { i }$ is the proportion of cases in the partition with class i. (The mean cost of the VB class is less than the mean cost for the RB class.)

$$
2. \sum_ {i = 1} ^ {m} p _ {i} \mu_ {i r} + \gamma \sum_ {i \neq r} p _ {i} \mu_ {i r} ^ {2} > \sum_ {i = 1} ^ {m} p _ {i} \mu_ {i k} + \gamma \sum_ {i \neq k} p _ {i} \mu_ {i k} ^ {2}.\tag{27}
$$

(The mean-risk for the VB class is greater than the meanrisk for the RB class.)

Proposition 3. Classification differences between VB and RB are more likely to occur at higher values of c.

Proof. From Condition (1) we get:

$$
\sum_ {i = 1} ^ {m} p _ {i} (\mu_ {i k} - \mu_ {i r}) > 0.\tag{28}
$$

From Condition (2) we get:

$$
\gamma \left(\sum_ {i \neq r} p _ {i} \mu_ {i r} ^ {2} - \sum_ {i \neq k} p _ {i} \mu_ {i k} ^ {2}\right) > \sum_ {i = 1} ^ {m} p _ {i} \left(\mu_ {i k} - \mu_ {i r}\right) > 0.\tag{29}
$$

Classification differences will not occur unless $\Sigma _ { i \neq r } p _ { i } \mu _ { i r } ^ { 2 } \ - \ \Sigma _ { i \neq k } \ p _ { i } \mu _ { i k } ^ { 2 } > 0 $ , implying that the expected spread of the VB class is greater than the RB class. A greater expected spread of costs in the VB class leads to higher risk, and hence RB prefers a class with a higher mean cost but lower risk. However, even when the VB class has greater spread, classification differences may not occur unless $\gamma$ is sufficiently large. Hence, classification behavior differences between VB and RB are more likely to occur if $\gamma$ increases, everything else held constant. As the decision maker’s aversion for risk increases, a pure mean-seeking approach is not likely to be optimal.

## 4.1. Special Cost Structures

We examine three special cost structures to see the impact of these structures on the classification behavior of the VB and RB algorithms. We first consider symmetric costs and show that VB and RB will exhibit the same classification behavior under such a cost structure. We also find that these algorithms exhibit the same classification behavior under a dominant cost structure. Unlike symmetric and dominant cost structures, cost structures that possess risky classes highlight differences between VB and RB.

Proposition 4. For a symmetric classification cost structure, VB and RB will exhibit the same classification behavior.

Proof. Proposition 4 implies that there will be no mean-risk trade-offs for symmetric costs; that is, under such a cost condition, VB and RB will always choose the same class. For symmetric costs we have:

$$
\begin{array}{r l} \mu_ {i j} = w _ {1}, & \forall i \neq j \\ = - w _ {2}, & \forall i = j \end{array}
$$

where, $w _ { 1 } , w _ { 2 } > 0 .$

Under a symmetric cost structure, classification differences between VB and RB occur if:

$$
\begin{array}{l} (1 - p _ {r}) w _ {1} - p _ {r} w _ {2} <   (1 - p _ {k}) w _ {1} - p _ {k} w _ {2}. \\ (1 - p _ {r}) w _ {1} - p _ {r} w _ {2} + \gamma (1 - p _ {r}) w _ {1} ^ {2} \\ > (1 - p _ {k}) w _ {1} - p _ {k} w _ {2} + \gamma (1 - p _ {k}) w _ {1} ^ {2}. \end{array}\tag{30}
$$

(31)

Simplifying Equation (30) we get:

$$
\begin{array}{l} (p _ {k} - p _ {r}) (w _ {1} + w _ {2}) <   0 \\ \Rightarrow (p _ {k} - p _ {r}) <   0, \\ \text { since } (w _ {1} + w _ {2}) > 0. \end{array}
$$

Simplifying Equation (31) we get:

$$
\begin{array}{l} (p _ {k} - p _ {r}) (w _ {1} + w _ {2} + \gamma w _ {1} ^ {2}) > 0 \\ \Rightarrow (p _ {k} - p _ {r}) > 0, \\ \text { since } (w _ {1} + w _ {2} + \gamma w _ {1} ^ {2}) > 0. \end{array}\tag{32}
$$

From the above analysis, we find that the above two conditions cannot be simultaneously true. Hence, under symmetric (but not uncertain) classification costs, VB and RB will display the same classification behavior.

Another interesting case involves classes that dominate other classes from a cost standpoint. For simplicity, we consider one dominant class but the discussion here extends to multiple dominant classes. In a dominant class, the absolute value of costs corresponding to correct and incorrect classification decisions are high compared to other classes. For example, the cost of misdiagnosing cancer as another disease can be very high, and the benefit of correctly diagnosing cancer has high payoffs (high negative costs). Hence the cancer diagnosis would tend to dominate other diagnoses.

Proposition 5. For a dominant classification cost structure, VB and RB will exhibit the same classification behavior.

Proof. Let $\mu _ { i j }$ represent the cost of classifying a case with class - i as ${ \mathrm { c l a s s } } = j . \mathrm { A }$ simple cost structure in which class k dominates other classes is given by:

$$
\begin{array}{r l} \mu_ {i j} & = - \alpha , i = j \neq k \\ & = \beta , i \neq j, i \neq k \\ & = - L \alpha , i = j = k \\ & = L \beta , i \neq j, i = k \end{array}\tag{33}
$$

where L is a real number greater than 1.

To isolate the impact of the above cost structure, let us assume that the classes are uniformly distributed. Let $E _ { i } , R _ { i } ,$ and $M R _ { i } ,$ denote the expectation, risk, and mean-risk, respectively, of choosing class $i , i = 1 , 2 , \dots$ m.

For $i \neq k$

$$
\begin{array}{r l} & E _ {i} = \frac {- \alpha + L (m - 1) \beta}{m}; \\ & R _ {i} = \frac {(m - 1) (L \beta) ^ {2}}{m}; \\ & M R _ {i} = \frac {- \alpha + L (m - 1) \beta}{m} + \gamma \frac {(m - 1) (L \beta) ^ {2}}{m}. \end{array}\tag{34}
$$

For i - k

$$
\begin{array}{r l} & E _ {k} = \frac {- L \alpha + (m - 1) \beta}{m}; \\ & R _ {k} = \frac {(m - 1) \beta^ {2}}{m}; \\ & M R _ {k} = \frac {- L \alpha + (m - 1) \beta}{m} + \gamma \frac {(m - 1) \beta^ {2}}{m}. \end{array}\tag{35}
$$

From the above expressions it is clear that:

$$
E _ {k} <   E _ {i} \text {   and   } M R _ {k} <   M R _ {i}, \forall i \neq k.\tag{36}
$$

Hence, a dominant class will be chosen by both a mean- based and a mean-risk based algorithm. 

Unlike a dominant class, a risky class nicely reveals differences between mean-seeking and mean-riskseeking algorithms. A risky class is one in which correct decisions provide relatively higher profit, but misclassifying any other class as the risky class results in relatively high costs. Equivalently, a risky class is a high-risk, high-return class. Consider an example from investing in new ventures. Such investments can be very risky because correctly identifying a good investment opportunity can be very profitable, whereas an incorrect decision could result in large losses. Unlike a dominant class, a risky class leads to large losses if the class is assigned when it should not have been assigned. On the other hand, a dominant class leads to large losses if it is not assigned when it should have been assigned.

Proposition 6. For a risky classification cost structure, VB and RB can exhibit different classification behavior.

Proof. The cost structure in Equation (33) can be modified to provide a simple example of a cost structure where class k is a risky class.

$$
\begin{array}{r l} \mu_ {i j} & = - \alpha , i = j \neq k \\ & = L \beta , i \neq j, j = k, \\ & = - L \alpha , i = j = k \\ & = \beta , i \neq j, j \neq k. \end{array}\tag{37}
$$

We again isolate the impact of the above cost structure by assuming that the classes are uniformly distributed. As before, $E _ { i } , R _ { i } ,$ and $M R _ { i } ,$ denote the expectation, risk, and mean-risk, respectively, of choosing class $i , i = 1 , 2 , \dots m .$

$$
\begin{array}{r l} & {\mathrm{For} i \neq k} \\ & {\quad E _ {i} = \frac {- \alpha + (m - 1) \beta}{m};} \\ & {\quad R _ {i} = \frac {(m - 1) (\beta) ^ {2}}{m};} \\ & {\quad M R _ {i} = \frac {- \alpha + (m - 1) \beta}{m} + \gamma \frac {(m - 1) (\beta) ^ {2}}{m}.} \\ & {\mathrm{For} i = k} \\ & {\quad E _ {k} = \frac {L (- \alpha + (m - 1) \beta)}{m};} \\ & {\quad R _ {k} = \frac {(m - 1) (L \beta) ^ {2}}{m};} \\ & {\quad M R _ {k} = \frac {L (- \alpha + (m - 1) \beta)}{m} + \gamma \frac {(m - 1) (L \beta) ^ {2}}{m}.} \end{array}\tag{38}
$$

(39)

Figure 3 Classification Differences Between VB and RB  
![](/api/attachments/JEEZCSBM/fulltext/images/e2f7ca72e2c03c7129e95a957c5d03968a53bf971910e7252f212f8fbd312c16.jpg)

From Equations (38) and (39), it is clear that even if $E _ { k } < E _ { i }$ (for $i \neq k )$ , for values of $\gamma$ above a critical level, a mean-risk algorithm would not choose class k. We differentiate the mean-risk expression for the risky class with respect to the skewing factor $L$ to study its impact.

$$
\frac {\partial M R _ {k}}{\partial L} = \frac {(m - 1) \beta (1 + 2 L \gamma \beta) - \alpha}{m}.\tag{40}
$$

For values of L greater than $L _ { T } \ : = \ : \ : ( \alpha \ : - \ : ( m \ : - \ : 1 ) \beta ) /$ $( 2 \gamma ( m \mathrm { ~ - ~ } 1 ) \beta ^ { 2 } )$ , the mean-risk value for the risky class should worsen $( \mathrm { i . e . , }$ increase) with L. Note that $L _ { T }$ decreases with $\gamma .$ Hence, increasing asymmetry (L) will be more likely to increase risk at higher values of $\gamma .$ Also note that $M R _ { k }$ increases with $\gamma ,$ implying that the impact of asymmetry on risk is more at higher levels of c. 

## 4.2. Two-Class Case

To provide further insights into the mean-risk tradeoff, we examine a simple two-class case and graphically depict regions of trade-off. For this case, we are able to relax assumptions concerning classification costs and class probabilities and allow classification costs to have an arbitrary structure. Assume that Class 1 is chosen by VB and Class 2 by RB. Let $p _ { 1 }$ and $( 1 ~ -$ $p _ { 1 } )$ be the class probabilities for Classes 1 and 2, respectively. Hence the conditions for differences in classification behavior between VB and RB are:

$$
\begin{array}{c} p _ {1} \mu_ {1 1} + (1 - p _ {1}) \mu_ {2 1} <   p _ {1} \mu_ {1 2} + (1 - p _ {1}) \mu_ {2 2}. \\ p _ {1} \mu_ {1 1} + (1 - p _ {1}) \mu_ {2 1} + \gamma (1 - p _ {1}) \mu_ {2 1} ^ {2} \\ > p _ {1} \mu_ {1 2} + (1 - p _ {1}) \mu_ {2 2} + \gamma p _ {1} \mu_ {1 2} ^ {2}. \end{array}\tag{41}
$$

(42)

![](/api/attachments/JEEZCSBM/fulltext/images/78803df07888619a5cb9aad27c05583dc50d0a4d908d582f2cd6ce6b8660db62.jpg)

Simplifying the above conditions and solving for $p _ { 1 } ,$ we find that the region for classification differences is given by the interval:

$$
\left(\frac {\mu_ {2 1} - \mu_ {2 2}}{\mu}\right) <   p _ {1} <   \left(\frac {\mu_ {2 1} (1 + \gamma \mu_ {2 1}) - \mu_ {2 2}}{\mu + \gamma (\mu_ {2 1} ^ {2} + \mu_ {1 2} ^ {2})}\right)\tag{43}
$$

where, $\mu = \mu _ { 1 2 } + \mu _ { 2 1 } - \mu _ { 1 1 } - \mu _ { 2 2 }$ is the total magnitude of the classification costs.

To provide a numerical example, assume that $\gamma =$ 0.5 with classification costs: $\mu _ { 1 1 } = { } - 1 0 0 ; \mu _ { 1 2 } = 2 0 ; \mu _ { 2 1 }$ $= 3 0 ; \mu _ { 2 2 } = - 5 .$ . Using Equation (43), the region in which VB and RB will classify differently is given by $0 . 2 2 \leq p _ { 1 } \leq 0 . 6 0$ . As depicted in Figure 3, VB chooses Class 1 (left graph) in this region while RB chooses Class 2 (right graph).

## 4.3. Summary of Analytical Findings

We summarize below several analytical findings that have been established so far. First and foremost, we have shown that a risk-aware algorithm can be different from a risk-neutral one even when cost uncertainties are absent. This finding is significant because classification cost asymmetries are likely to be present in many situations. The second finding is somewhat obvious: Risk considerations become more significant at higher levels of risk aversion. The third finding involves special cost structures that nullify or intensify risk. If classification costs are symmetric or dominant, then risk can be ignored. Under such cost conditions, not only is risk nullified, but value considerations are also unimportant. On the other hand, the presence of risky classes intensifies risk and makes risk considerations important.

Although the analysis in this section provides insights into risk-aware classification, it tells us nothing about how risk considerations affect the entire tree construction process (i.e., input selection, stopping, and classification). Unfortunately, a mathematical analysis of the entire tree construction process is extremely complex and beyond the scope of this paper. In addition to the added complexity of the entire tree construction process, other issues further complicate the analysis. These issues include sampling variation, residual variation, and data set characteristics, such as number of classes, number of inputs, number of input states, etc. In the next section, we experimentally study a variety of such issues that are difficult to analyze mathematically. We demonstrate that the analytical findings in this section extend to the more realistic scenarios studied in these experiments.

## 5. Experimental Comparisons

In this section, we describe the factors affecting performance, experimental design, experimental procedure, and results. The section ends with a discussion of the results.

## 5.1. Factors and Propositions

We are interested in studying the effects on the meanrisk performance of four factors: algorithm, asymmetry, classification cost uncertainty, and risk aversion. Each factor and its anticipated effects are discussed in this subsection.

5.1.1. Algorithm. The main subject of this research is the mean-risk performance differences among the RB and VB algorithms. We expect the RB algorithm to perform better than VB over a wide range of the other factors. Even though there are some situations in which RB and VB perform identically, the RB algorithm should have significantly better performance overall. When risk aversion is zero, they are the same algorithm. Proposition 4 demonstrated that the classification behavior of the RB and VB algorithms is identical with symmetric classification costs. Since these are only isolated points of identical performance, we expect to see performance differences as stated in Proposition 7.

Proposition 7. RB has a lower mean-risk performance than VB over a wide range of the other factors.

5.1.2. Asymmetry. Section 4 demonstrated how asymmetry affects performance in a two-class case. As suggested by that analysis, we expect performance differences to be magnified by increasing the asymmetry. In addition, an examination of the mean-risk measure (Equation (18)) shows that it is sensitive to the skew in the costs of incorrect classifications. Thus, Proposition 8 summarizes our expectation about asymmetry.

Proposition 8. The performance difference between the RB and VB algorithms increases as classification cost asymmetry increases.

5.1.3. Uncertainty. The mean risk measure in Equation (18) increases as classification cost uncertainty increases. To depict the differences in the algorithms more clearly, we apply uncertainty in a nonuniform manner. That is, some classes will have more uncertainty than other classes. Coefficient of variation is used to standardize the amount of uncertainty in a class. Thus uncertainty across classes with different mean costs can be compared. Proposition 9 summarizes our expectation about uncertainty.

Proposition 9. The performance difference between RB and VB increases as classification cost uncertainty increases.

We have omitted input cost uncertainty to simplify the experimental procedures. With many factors in a regression model, identifying the important ones can be quite tedious, especially if all interactions need to be considered. We also believe that input cost uncertainty may not be much of an issue if the input is being purchased from an outside party (for example, a credit check usually costs a predetermined amount that is agreed upon between the lending firm and the credit bureau). When an input is being produced internally, cost uncertainty may exist, but such uncertainty may be reduced by using standardized procedures to calculate the input. Finally, input cost uncertainty alone leads to risk; there is no impact of input cost asymmetry on risk. On the other hand, both forms of variation (asymmetries and uncertainties) in classification costs result in risk. For the reasons discussed above, our approach in the experiments was to focus on asymmetries and uncertainties in classification costs.

5.1.4. Risk Aversion. The mean-risk measure increases as the risk-aversion coefficient $( \gamma$ in Equation 18) increases. The risk-aversion coefficient should have the most direct impact on the choice of algorithms. Thus, Proposition 10 summarizes our expectation about risk aversion.

Proposition 10. The performance difference between RB and VB increases as the risk-aversion coefficient increases.

## 5.2. Experimental Design

To test these propositions, we used the polynomial regression model shown in Equation (44). Our intention was not to predict the performance difference between algorithms. Rather, we wanted to depict whether a difference existed, and, if $\mathbf { S O } ,$ the nature of the difference.

$$
E (\Delta M R _ {T}) = \beta_ {0} + \beta_ {1} A + \beta_ {2} U
$$

$$
+ \beta_ {3} \gamma + i n t e r a c t i o n s\tag{44}
$$

where $\varDelta M R _ { T }$ is the difference in mean-risk performance between algorithms;

A is the asymmetry of the classification costs;

U is the uncertainty of the classification costs;

c is the risk aversion level; and

$$
i n t e r a c t i o n s = \beta_ {4} A U + \beta_ {5} U \gamma + \beta_ {6} A \gamma + \beta_ {7} A U \gamma .
$$

A tree’s mean risk, $M R _ { T } ,$ is estimated using a sample of unseen cases and Equation (45). For each case, the path used, total input cost, and classification cost (either correct or incorrect) are recorded. For each path, the mean-risk measure is computed using the input costs, correct classification costs, and incorrect classification costs. The mean-risk of the tree is an expectation of the path mean-risk measures.

$$
\overline {{M R}} _ {T} = \sum_ {j = 1} ^ {P} \pi_ {j} M R _ {j}.\tag{45}
$$

$$
M R _ {j} = \bar {C} _ {j} + \bar {I} _ {j} + \gamma (s _ {I _ {j}} ^ {2} + s _ {C C _ {j}} ^ {2} + \overline {{I C}} _ {j} ^ {2} + s _ {I C _ {j}} ^ {2})\tag{46}
$$

where $\pi _ { j }$ is the probability of the $j _ { t h }$ path;

$\bar { C } _ { j }$ is the sample mean of the classification cost of path $j ;$

$\bar { I } _ { j }$ is the sample mean of the input cost of path $j ;$

$s _ { I _ { j } } ^ { 2 }$ is the sample variance of the input cost of path $j ;$

$s _ { C C _ { j } } ^ { 2 }$ is the sample variance of the correct classification cost of path j;

$\overline { { I C } } _ { j }$ is the mean of the incorrect classification cost of path $j ;$ and

$s _ { I C _ { j } } ^ { 2 }$ is the sample variance of the incorrect classification cost of path j.

Asymmetry (A) and uncertainty (U) increase the risk of selected classes. These measures are applied to a classification cost matrix that is used to construct and evaluate decision trees. Each cell in a matrix contains $\mu _ { i j }$ and $C V _ { i j } ,$ the mean cost and coefficient of variation of cost when classifying a case as class j (the estimated class) when the true class is i. To increase asymmetry (uncertainty) in class $j , \mu _ { i j } ( C V _ { i j } )$ is multiplied by A (U) for all values of i. In other words, to increase the asymmetry (uncertainty) of class $j ,$ the asymmetry (uncertainty) values in the $j ^ { t h }$ column are multiplied by A (U). For $A = 1 ( U = 1 )$ ) there is no asymmetry (uncertainty). A and U are uniformly drawn in the range [1, 10].

## 5.3. Experimental Procedure

The experimental procedure relied on the test sample method used in many previous studies (Weiss and Kulikowski 1991). In this method, the input data is randomly split into a training set and a test set. The combination of a training and test set is known as a split. The training set is used to generate trees with different inductive algorithms. The test set is used to calculate performance. The average performance across many splits is used to compare the different approaches.

Using the test sample method, we implemented the model in (44) as follows. A data set was randomly split into a training set (70% of cases) and a test set (30% of cases). The training set, a random $\gamma ,$ and a classification cost matrix were used to construct trees with each algorithm. We randomly selected 30% of the classes to apply A and U. To evaluate the trees from each algorithm, we generated classification costs for each test case. Classification costs were drawn from a uniform distribution using the mean and CV from the appropriate cell of the classification cost matrix. To isolate classification cost effects, input costs were identical to those used during tree construction. Thus, input cost variance was zero.

Each algorithm was evaluated using the set of input and classification costs generated as described above. To provide a reasonable sample size along each path, we calculated the $M R _ { T }$ measure through 100 iterations of the test set. This calculation was the $M R _ { T }$ measure for one split. One observation for each algorithm was the average performance across 30 splits.

The size and parameter settings of an experiment were as follows. Each experiment generated 300 observations per algorithm. Each observation used uniformly drawn factor values from the following ranges: A[1,10], U[1,10], and c[0.01,0.5]. Each algorithm used the same factor values for each corresponding observation. To reduce unnecessary variance in the response variable, factor values were held constant over the 30 splits of an observation.

Four experiments were executed, one per data set. Two of the four data sets were artificially generated, and the remaining two were taken from real domains. The artificial data sets were generated by a program based on specifications described in (Bisson 1991). The data set generator can control the number of cases, classes, attributes, states per attribute, and the complexity of rule sets for each class. Data Set 1 contains four equally distributed classes and ten input attributes. Data Set 2 contains eight moderately skewed classes and 15 input attributes. Half the cases in Data Set 2 are uniformly distributed between two classes, while the remaining cases are uniformly distributed among the other six classes. Both artificial data sets share the following characteristics: (1) the number of cases is 200, (2) the average number of states per attribute is three (between two and five), and (3) the average size of the rule sets is two rules per class with three attributes per rule.

The first real domain data set, Lymphography (LYM), was selected from the Repository of Machine Learning Databases and Domain Theories (Murphy and Aha 1991). This data set was originally obtained from the University Medical Centre, Institute of Oncology, Ljubljana, Yugoslavia. LYM has four classes, 18 attributes (mix of Boolean and nominal with a few states), and 148 cases. In this data set, two classes are infrequent compared to the other classes. The other real data set, Bankruptcy (BNK), consists of 50 cases of firms that have been classified as likely to become bankrupt or not (Liang 1992). BNK has eight input attributes that have between two and four states and two uniformly distributed classes.

## 5.4. Results

Table 1 shows the fitted response functions for the four data sets. Step-wise polynomial regression was used to find the significant factors. The response functions contain the variables that were found to be significant at a P-value of 0.10 or below. Complete regression results can be found in Appendix B. Table 2 shows that the model in Equation (44) explains a significant amount of the variation in the simulation results.

Results of Propositions. To test Proposition 7, we conducted the following one-tailed t-test assuming unequal variances:

$$
\begin{array}{l} H _ {0} \colon M R _ {T} (R B) = M R _ {T} (V B). \\ H _ {1} \colon M R _ {T} (R B) <   M R _ {T} (V B). \end{array}
$$

$H _ { 0 }$ is strongly rejected. The largest p-value across the four data sets was less than 0.001. For all the data sets, the sample mean for VB was an order of magnitude higher than that for RB. Hence, we can conclude that RB performs much better than VB over a wide range of values for uncertainty, asymmetry, and risk aversion.

To study the other Propositions (8 through 10), we isolated the effects of each factor by taking the partial derivatives of the response functions for each data set as shown in Table 3. The partial derivatives indicate some support for Propositions 8, 9, and 10. The LYM results support all three propositions, while the BNK results support Proposition 9. For the other data sets, the performance difference depends on the factor values. For DS1, when U - 1 (no uncertainty), c must be larger than 0.1437 for Proposition 8 to hold. When U - 3 (low classification cost uncertainty), c must only be larger than 0.037. Overall, the results indicate that both asymmetry and uncertainty must be present to support Propositions 8 through 10 as summarized in Table 4.

Table 1 VB-RB Fitted Differences

<table><tr><td>Data set</td><td>Response Function Difference</td></tr><tr><td>DS1</td><td> $13547 - 71756\gamma - 2990.76U - 3036.33A + 17000A\gamma + 7247.56U\gamma + 593.79AU$ </td></tr><tr><td>DS2</td><td> $25359 - 128521\gamma - 3875.50U - 5221.33A + 11310U\gamma + 757.44AU + 24173A\gamma$ </td></tr><tr><td>Lymphography</td><td> $-17444 + 553.98AU + 17773A\gamma$ </td></tr><tr><td>Bank</td><td> $-69152\gamma - 2592.26A + 25432A\gamma + 666.13UA$ </td></tr></table>

Table 2 Analysis of Variance Summary

<table><tr><td>Data Set</td><td>R2</td><td>Adjusted R2</td></tr><tr><td>DS1</td><td>0.6267</td><td>0.6191</td></tr><tr><td>DS2</td><td>0.7162</td><td>0.7104</td></tr><tr><td>Lymphography</td><td>0.5080</td><td>0.5047</td></tr><tr><td>Bank</td><td>0.6160</td><td>0.6095</td></tr></table>

Table 3 Partial Derivatives of Response Functions

<table><tr><td>DS1</td><td>DS2</td></tr><tr><td> $\frac{\partial\Delta MR_{T}}{\partial A} = -3036.33 + 17000\gamma + 593.79U$ </td><td> $\frac{\partial\Delta MR_{T}}{\partial A} = -5221.33 + 24173\gamma + 757.44U$ </td></tr><tr><td> $\frac{\partial\Delta MR_{T}}{\partial U} = -2990.76 + 7247.56\gamma + 593.79A$ </td><td> $\frac{\partial\Delta MR_{T}}{\partial U} = -3875.5 + 11310\gamma + 757.44A$ </td></tr><tr><td> $\frac{\partial\Delta MR_{T}}{\partial\gamma} = -2990.76 + 17000A + 7247.56U$ </td><td> $\frac{\partial\Delta MR_{T}}{\partial\gamma} = -128521 + 24173A + 11310U$ </td></tr><tr><td>LYM</td><td>BNK</td></tr><tr><td> $\frac{\partial\Delta MR_{T}}{\partial A} = 17773\gamma + 553.98U$ </td><td> $\frac{\partial\Delta MR_{T}}{\partial A} = -2592.26 + 25432\gamma + 666.13U$ </td></tr><tr><td> $\frac{\partial\Delta MR_{T}}{\partial U} = 553.98A$ </td><td> $\frac{\partial\Delta MR_{T}}{\partial U} = 666.13$ </td></tr><tr><td> $\frac{\partial\Delta MR_{T}}{\partial\gamma} = 17773A$ </td><td> $\frac{\partial\Delta MR_{T}}{\partial\gamma} = -69152 + 25432A$ </td></tr></table>

Graphical Results. We further depict the behavior of the RB and VB algorithms in Figures 4 and 5. The graphs were produced by varying one factor (shown on the x-axis) and holding the other two factors constant. Each observation was the average over 20 splits. In both sets of graphs, performance differences are not manifest until a moderate amount of the varying factor occurs when the other factors are moderate. In Figures 4a and 5a, the cut-off value is about 4 for the varying factors (A and U, respectively). When one factor is high, the cutoff of the other factor is low.

The results demonstrate performance differences between the VB and RB algorithms using the mean-risk measure. In one sense, the mean-risk measure favors the RB algorithm because it is the measure used to construct RB trees. The performance differences among the algorithms should not be limited to the mean-risk measure, however. The algorithms should show performance differences for other utility functions with suitable properties. For correct classification decisions (negative costs), the utility function should be relatively flat, showing a decreasing utility of wealth. For incorrect classification decisions (positive cost), the utility function should be steep, showing an increasing risk aversion. More precisely, utility functions should have the following properties:

$$
\begin{array}{r l} U (x) & <   0 \text {   if   } x > 0. \\ & > 0 \text {   if   } x > 0. \end{array}
$$

$U ^ { \prime } ( x ) < 0 \forall x$ (slope is always negative).

$$
\begin{array}{l} U ^ {\prime \prime} (x) <   0 \text { if } x > 0 (\text { slope   is   rising }) \\ \quad > 0 \text { if } x <   0 (\text { slope   is   flattening }). \end{array}
$$

To study performance on alternative measures, we chose a utility function that satisfied these properties. We created trees for the algorithms using the original mean and mean-risk measures for VB and RB, respectively. However, we measured the performance of the algorithms using the new utility measure. Thus the results demonstrate whether the algorithms show performance differences when the performance measure differs from the classification function. Figures 6 and 7 show the performance of the algorithms using the utility function in Equation (47) with the  parameter set to 0.007. The results appear similar to Figures 4 and 5 except that the performance differences are much more pronounced when the constant factor (asymmetry or uncertainty) is high. The scale changes by an order of magnitude or more for both graphs (U - 10 and $A =$ 10).

$$
\begin{array}{r l} U (x) & = - e ^ {\alpha x} \text {   if   } x > 0, 0 \leq \alpha \leq 1 \\ & = \ln (- x) \text {   if   } x <   0. \end{array}\tag{47}
$$

## 5.5. Discussion

The experimental results in this section extend the analytical results obtained in the previous section. Because the algorithms can exhibit different behavior based only on the classification function, input selection and stopping appear less important for predicting the behavior of risk-based algorithms. There is, however, a possible concern about the RB algorithm’s stopping mechanism that deserves mention. Although stopping does not play a dominant role, under some conditions the RB algorithm could stop collecting inputs early. Input collection would stop if the best class in the parent partition is the same as the best class in the child partitions generated by an input. We refer to this effect as the “freezing” effect.

Table 4 Summary of Support for Propositions

<table><tr><td>Proposition</td><td>DS1</td><td>DS2</td><td>LYM</td><td>BNK</td></tr><tr><td>8 (Asymmetry)</td><td>Depends on γ and U</td><td>Depends on γ and U</td><td>Support</td><td>Depends on γ and U</td></tr><tr><td>9 (Uncertainty)</td><td>Depends on γ and A</td><td>Depends on γ and A</td><td>Support</td><td>Support</td></tr><tr><td>10 (Risk Aversion)</td><td>Depends on A and U</td><td>Depends on A and U</td><td>Support</td><td>Depends on A</td></tr></table>

Figure 4 Asymmetry Graphs for DS1  
![](/api/attachments/JEEZCSBM/fulltext/images/e4cc5f3f78689d17fa082881c789f0c1770dbe626d92990c931543cd921fd7d5.jpg)

![](/api/attachments/JEEZCSBM/fulltext/images/123283ee95bd58ba77cfa491842c80810f845e79998a6dd3d56700169250a968.jpg)

Figure 5 Uncertainty Graphs for DS1  
![](/api/attachments/JEEZCSBM/fulltext/images/99450425dd948a49b4bdc16c532a1f27b2953208de90cdec8d188b7f88dcb2b4.jpg)

![](/api/attachments/JEEZCSBM/fulltext/images/ca5b57324977ec6937c508288370fa5cd91e30817a9c084ffdbb4eb311d80c5f.jpg)

Figure 6 Asymmetry Graphs for DS1 Using the Alternative Utility Function  
![](/api/attachments/JEEZCSBM/fulltext/images/17cffc99d5196e4c714ccb717a55b10124a8693e90f49edde3de06f8a0dc8f19.jpg)

![](/api/attachments/JEEZCSBM/fulltext/images/55c647d19adc951bd7b5ae57c8b51070c2b0ae19e2fc354bd66f6d4fae76ab91.jpg)

Figure 7 Uncertainty Graphs for DS1 Using the Alternative Utility Function  
![](/api/attachments/JEEZCSBM/fulltext/images/909156fb93bab5562c592978e274dc1050922c5424260a7a6f6bf0708e781fd7.jpg)

The question arises: When there is a dominant class in the data, will the RB algorithm freeze? To study this question, we implemented another algorithm $( \mathrm { R B } _ { \mathrm { L } } ,$ for Risk-Based Light) with the input selection and stopping principles of the VB algorithm and the classification principle of the RB algorithm. Conceptually, a $\mathrm { R B _ { L } }$ tree is a VB tree except that the leaves of the $\mathrm { R B _ { L } }$ tree are replaced by classes that RB would choose under the partitions generated at the leaves. All the simulation experiments in this section actually involved three algorithms: VB, RB, and $\mathrm { R B } _ { \mathrm { L } } .$ . There were no significant differences between RB and $\mathrm { R B } _ { \mathrm { L } }$ . Hence, we suppressed $\mathrm { R B _ { L } }$ in the earlier part of this section.

The above discussion concerning $\mathrm { R B _ { L } }$ is connected with a deeper issue concerning the design of risk-based algorithms. When the stopping rule of an induction algorithm is greedy, it fails to detect that residual variation can be reduced by observing additional inputs. This could lead to freezing. Sometimes freezing may have beneficial side effects. Smaller trees are typically more robust in the presence of sampling variation. However, beyond a point, the overall effect of greedy stopping may be detrimental to performance. Also, greedy stopping may cause more freezing problems in risk-based algorithms, because they are more sensitive to variation.

![](/api/attachments/JEEZCSBM/fulltext/images/422ba006bdefde9c2152a23eb3cbeaff732aa9fda0a116fd21215eba34dd67d1.jpg)

One solution to freezing in risk-based algorithms may be addressed by considering a family of riskbased algorithms. In this study, we explored the end points of this family. RB is an algorithm that pays no attention to freezing. On the other hand, $\mathrm { R B } _ { \mathrm { L } }$ completely ignores risk until a leaf node needs to be created. A family of risk-based algorithms may be implemented by continuously varying risk considerations in stopping, from no consideration (RB ) to full consideration (RB).

Another solution to freezing may be to avoid greedy stopping. CART (Breiman et al. 1984) and ICET (Turney 1995) offer two alternatives to nongreedy search for value-based induction. CART uses crossvalidation techniques to search the space of pruned trees. ICET uses a genetic algorithm to evolve a population of input costs for a decision tree induction algorithm. Both techniques involve additional overhead, but they have reported generating better trees. Thus, it seems reasonable that better trees can be generated for risk-based algorithms with additional overhead.

## 5.6. Implications for Managers

We end this section with the managerial implications of this research. We first address the issue of constrained risk versus mean-risk trade-offs. While constrained risk approaches are applicable to both valuesensitive and non-value-sensitive induction, mean-risk trade-offs only apply to value-sensitive induction. If classification costs are difficult to estimate, then a constrained risk approach is the appropriate way to deal with risk. However, if classification costs can be quantified, then mean-risk trade-offs offer the designer a finer level of control over risk. Hence, for valuesensitive induction, mean-risk trade-offs should be the guiding paradigm.

Another aspect of risk-based system design can be summarized in the following question. How different will a risk-based design be from risk-neutral one? An important issue is the relationship between risk and the value of information (Nadiminti et al. 1996). We find from our experiments that when risk is large (either risk aversion is high or the sources that cause risk are strong), the value of information decreases. If a greedy stopping rule is used, risk-based algorithms have a greater tendency to freeze. A greedy stopping rule is a special case of satisficing behavior. Since human decision makers are subject to bounded rationality, satisficing choice behavior is often assumed (Simon 1955). Therefore, our finding that information value decreases with risk is reasonable for human decision makers. For nongreedy search, more analysis is needed to explore the relationship between information value and risk.

We finally pose a broad question: How strong is the link between information systems design and the risk framework developed in this paper? For example, do risk considerations apply equally to transactionprocessing systems, as they do to decision-support or expert-support systems? These are, of course, broad characterizations and some systems may overlap across multiple categories. To address such questions, we note that risk in this study applies to the level of the individual decision maker. Thus, as long as we are designing an information system that supports individual decisions, the risk paradigm may be valid. The importance of considering risk may also be linked to the frequency and criticality of decisions. For highfrequency decisions, risk may be less important because the long-run average performance may be sufficient to optimize. However, if the decisions involve high rewards and losses, risk considerations may be appropriate. The most compelling situation for considering risk may be for medium frequency decisions with high stakes (for example, bidding for large projects in a consulting environment). Thus, for systems at the individual level with significant stakes, the riskbased paradigm developed here may be appropriate.

## 6. Conclusion

We described an approach to support mean-risk tradeoffs for inductive expert systems. Because decision makers in many situations are risk-averse, mean-risk trade-offs are important to account for the level of risk aversion. We developed a mean-risk measure that is consistent and separable. In addition, this measure was supported by empirical studies on decision making under risk.

The measure was incorporated into the input selection criterion, stopping rule, and classification function of an induction algorithm (RB algorithm). Empirical analysis demonstrated that the mean-risk performance difference between the risk-based algorithm and a mean-seeking algorithm improved as sources of variation increased. The presence of asymmetries generates risky classes. Risky classes have a profound influence on the relative performance of mean-risk-based versus simple mean-based algorithms. Our risk paradigm is more appropriate for designing systems to support individuals that make decisions with relatively high stakes.

There are a number of fruitful avenues of future research. One problem is to develop nongreedy search methods. These methods could be tested to see if solution quality improves relative to increased overhead. Another area involves more detailed models of asymmetry and uncertainty. A third area is to investigate risk measures derived from utility theory. Finally, risk issues may be incorporated in other value-sensitive areas of expert systems research.

## Appendix A: The VB Algorithm Let

Z(X<sub>t</sub>) be information acquisition cost of input $X _ { t } ;$

$C ( i , j )$ be the cost of classifying an object of class i as class j;

L be a set of cases;

$f ( i , L )$ be the proportion of cases in L with class $= i ;$

$L \mid X _ { t } = s$ be the cases in L for which $X _ { t } = s ;$ and

$h ( X _ { t } = s , L )$ be the proportion of cases in L for which $X _ { t } = s .$

$E C ^ { * } ( L ) = M i n \ [ \Sigma _ { i = 1 } ^ { m } f ( i , L ) \ C ( i , j ) ]$ is the least expected classification cost in the partition L.

$\begin{array} { r } { E C ^ { * } \left( L \mid X _ { t } \right) = \Sigma _ { s = 1 } ^ { q } h ( X _ { t } = s , L ) E C ^ { * } \left( L \mid X _ { t } = s \right) } \end{array}$ is the least expected classification cost in L, after observing $X _ { t } .$

Hence, $A E C ^ { * } \left( L \mid X _ { t } \right) ~ = ~ E C ^ { * } \left( L \right) ~ - ~ E C ^ { * } \left( L \mid X _ { t } \right)$ is the benefit of observing X in the partition L.

Input selection is governed by the following two rules:

Table B1 Complete Regression Results

<table><tr><td>Variable</td><td>DF</td><td>Parameter Est.</td><td>Std. Error</td><td>t-value</td><td>P-value</td></tr><tr><td colspan="6">DS1</td></tr><tr><td>INTERCEPT</td><td>1</td><td>113547</td><td>6052.0438</td><td>2.238</td><td>0.0259</td></tr><tr><td> $\gamma$ </td><td>1</td><td>-71756</td><td>16205.8700</td><td>-4.428</td><td>0.0001</td></tr><tr><td>U</td><td>1</td><td>-2990.7599</td><td>922.8109</td><td>-3.241</td><td>0.0013</td></tr><tr><td>A</td><td>1</td><td>-3036.3332</td><td>822.7027</td><td>-3.691</td><td>0.0003</td></tr><tr><td> $A^{*}U$ </td><td>1</td><td>593.7900</td><td>108.6931</td><td>5.463</td><td>0.0001</td></tr><tr><td> $A^{*}\gamma$ </td><td>1</td><td>17000</td><td>1942.8014</td><td>8.750</td><td>0.0001</td></tr><tr><td> $U^{*}\gamma$ </td><td>1</td><td>7247.5606</td><td>1988.5864</td><td>3.645</td><td>0.0003</td></tr><tr><td colspan="6">DS2</td></tr><tr><td>INTERCEPT</td><td>1</td><td>25359</td><td>6481.7073</td><td>3.912</td><td>0.0001</td></tr><tr><td> $\gamma$ </td><td>1</td><td>-128521</td><td>19116.9084</td><td>-6.723</td><td>0.0001</td></tr><tr><td>U</td><td>1</td><td>-3875.5002</td><td>872.8676</td><td>-4.440</td><td>0.0001</td></tr><tr><td>A</td><td>1</td><td>-5221.3317</td><td>920.0516</td><td>-5.675</td><td>0.0001</td></tr><tr><td> $A^{*}U$ </td><td>1</td><td>757.4369</td><td>120.7256</td><td>6.274</td><td>0.0001</td></tr><tr><td> $A^{*}\gamma$ </td><td>1</td><td>24173</td><td>2155.6675</td><td>11.213</td><td>0.0001</td></tr><tr><td> $U^{*}\gamma$ </td><td>1</td><td>11310</td><td>2326.3511</td><td>4.861</td><td>0.0001</td></tr><tr><td colspan="6">LYM</td></tr><tr><td>INTERCEPT</td><td>1</td><td>-17444</td><td>2820.4626</td><td>-6.185</td><td>0.0001</td></tr><tr><td> $A^{*}\gamma$ </td><td>1</td><td>17773</td><td>1537.7213</td><td>11.558</td><td>0.0001</td></tr><tr><td> $A^{*}U$ </td><td>1</td><td>553.9799</td><td>79.5675</td><td>6.962</td><td>0.0001</td></tr><tr><td colspan="6">BNK</td></tr><tr><td> $\gamma$ </td><td>1</td><td>-69152</td><td>13010.9257</td><td>-5.315</td><td>0.0001</td></tr><tr><td>A</td><td>1</td><td>-2592.26</td><td>735.9328</td><td>-3.522</td><td>0.0005</td></tr><tr><td> $A^{*}U$ </td><td>1</td><td>666.13</td><td>96.9963</td><td>4.939</td><td>0.0001</td></tr><tr><td> $A^{*}\gamma$ </td><td>1</td><td>25432</td><td>2620.2011</td><td>10.871</td><td>0.0001</td></tr></table>

1. Select free inputs before costly ones.

2. For costly inputs, select the one with the highest input gain, $g ( X _ { t } , L ) = \varDelta E C ^ { * } ( L \bar { | } X _ { t } ) / Z ( X _ { t } )$

Stop if there are no free inputs left and for all costly inputs, $g ( X _ { t } , L )$ $\leq 1 .$

The classification function k(L) labels a leaf node with the class that minimizes expected classification cost. Formally, $k ( L ) = \lambda ,$ such that $E C ^ { * } \left( L \right) = \Sigma _ { i = 1 } ^ { m } f \left( i , L \right) C \{ i , \lambda )$

## Appendix B: Regression Results

Table B1 presents the complete regression results for the response functions in Equation (35) for the four data sets. In these tables, only those variables that were found to be significant at a P-value of 0.10 or below are shown. Step-wise polynomial regression was used to find the significant factors.

## References

Adar, Z., A. Barnea, B. Lev. 1977. A comprehensive cost-volumeprofit analysis under uncertainty. Accounting Rev. 52 137–149.

Altman, E., R. Haldeman. 1995. Corporate credit-scoring models: Approaches and tests for successful implementation. J. Commercial Lending 77(9) 10–13.

Bisson, H. 1991. Evaluation of learning systems: An artificial databased approach. Y. Kodratoff, ed. Proc. European Working Session on Machine Learning. Springer-Verlag, Berlin, F.R.G.

Braun, H., J. Chandler. 1987. Predicting stock market behavior through rule induction: An application of the learning-fromexamples approach. Decision Sci. 18(3) 415–429.

Breiman, L., J. Friedman, R. Olshen, C. Stone. 1984. Classification and Regression Trees. Wadsworth Publishing, Belmont, CA.

Creecy, R., B. Masand, S. Smith, D. Waltz. 1992. Trading MIPS and memory of knowledge engineering. Comm. ACM 35(8) 48–64.

Andrew B. Whinston, Associate Editor. This paper was received on November 5, 1996, and was with the authors 8 months for 2 revisions.

Ezawa, K., S. Norton, 1996. Constructing Bayesian networks to predict uncollectible telecommunications accounts. IEEE Expert 11(5) 45–51.

Gur-Ali, O., W. Wallace. 1993. Induction of rules subject to a quality constraint: Probabilistic inductive learning. IEEE Trans. Knowledge Data Engrg 5(6) 979–984.

Huang, C., R. Litzenberger. 1988. Foundations for Financial Economics. Elsevier Science, New York.

Irani, K., J. Cheng, U. Fayyad, Z. Qian. 1993. Applying machine learning to semiconductor manufacturing. IEEE Expert 8(1) 41– 47.

Keller, L., R. Sarin, M. Weber. 1986. Empirical investigation of some properties of the perceived riskiness of gambles. Organ. Behavior Human Decision Process. 38 114–130.

Landsburg, S. 1988. Price Theory and Its Applications. Southwestern College Publishing, Cincinnati OH.

Liang, T. 1992. A composite approach to inducing knowledge for expert system design. Management Sci. 38(1) 1–17.

Magee, R. 1975. Cost-volume-profit analysis, uncertainty and capital market equilibrium. J. Accounting Res. 13 257–266.

Maginn, J., D. Tuttle. eds. 1990. Managing Investment Portfolios. Warren, Gorham, and Lamont, Boston, MA.

Markowitz, H. 1952. Portfolio selection. J. Finance 7 77–91.

Mingers, J. 1989. An empirical comparison of pruning methods for decision tree induction. Machine Learning 4(2) 227–243.

Mookerjee, V., B. Dos Santos. 1993. Inductive expert system design: Maximizing system value. Inform. Systems Res. 4(2) 111–140.

——, M. Mannino. 1997. Redesigning case based retrieval to reduce information acquisition costs. Inform. Systems Res. 8(1) 51–68.

Moore, J., A. Whinston. 1986. A model of sequential decision making—part I. Decision Support Systems 2(4) 285–307.

—, ——. 1987. A model of sequential decision making—part II. Decision Support Systems 3(1) 47–72.

Murphy, P., D. Aha. 1991. UCI Repository of Machine Learning Databases. University of California, Irvine, Department of Information and Computer Science, Irvine, CA.

Nadiminti, R., T. Mukhopadhyay, C. Kriebel. 1996. Risk aversion and the value of information. Decision Support Systems 16 241– 254.

Nunez, M. 1991. The use of background knowledge in decision tree induction. Machine Learning 6 231–50.

Pollatsek, A., A. Tversky. 1970. A theory of risk. J. Math. Psych. 7 540–553.

Pratt, J. 1964. Risk aversion in the small and in the large. Econometrica 32 122–136.

——. 1986. Induction of Decision Trees, Machine Learning 1 81–106.

——. 1987. Simplifying decision trees. Internat. J. Man Machine Stud. 27 221–234.

Sarin, R., M. Weber. 1993. Risk-value models. European J. Oper. Res. 70 135–149.

Seppala, J. 1994. The diversification of currency loans: A comparison between safety-first and mean-variance criteria. European J. Oper. Res. 74(2) 325–43.

Sharpe, W. 1964. Capital asset prices: A theory of market equilibrium. J. Finance 19 425–442.

Simon, H. 1955. A behavioral model of rational choice. Quart. J. Econom. 69 99–118.

Singhal, V., A. Raturi, J. Bryant. 1993. On incorporating business risk into continuous review inventory models. European J. Oper. Res. 75(1) 135–50.

Srinivasan, V., Y. Kim. 1987. Credit granting: A comparative analysis of classification procedures. J. Finance XLII(3) 665–681.

Starbird, A. 1994. The effect of acceptance sampling and risk aversion on the quality delivered by suppliers. J. Oper. Res. Soc. 45(3) 309–320.

Tam, K., M. Kiang. 1990. Predicting bank failures: A neutral network approach. Appl. Artificial Intelligence 4 265–282.

Tan, M. 1993. Cost-sensitive learning of classification knowledge and its applications in robotics. Machine Learning 13 7–33.

Turney, P. 1995. Cost-sensitive classification: Empirical evaluation of a hybrid genetic decision tree induction algorithm. J. Artificial Intelligence Res. 2 369–409.

Von Neumann, J., O. Morgenstern. 1947. Theory of Games and Economic Behavior. Princeton University Press, Princeton, NJ.

Weiss, M., C. Kulikowski. 1991. Computer Systems That Learn: Classification and Prediction Methods from Statistics, Neural Nets, Machine Learning, and Expert Systems. Morgan Kaufmann Publishers, San Mateo, CA.
