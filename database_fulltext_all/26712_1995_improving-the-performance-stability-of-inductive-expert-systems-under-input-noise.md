---
otero_id: 26712
otero_key: "DC5X39GC"
title: "Improving the Performance Stability of Inductive Expert Systems Under Input Noise"
authors: "Vijay S. Mookerjee; Michael V. Mannino; Robert Gilson"
year: "1995"
journal: "Information Systems Research"
doi: "10.1287/isre.6.4.328"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

![](/api/attachments/DC5X39GC/fulltext/images/a14fd0f68ca66378a1f99e738719671a09391b02d071f4142f46a26db83ef1ac.jpg)

# Improving the Performance Stability of Inductive Expert Systems Under Input Noise

Vijay S. Mookerjee, Michael V. Mannino, Robert Gilson,

## To cite this article:

Vijay S. Mookerjee, Michael V. Mannino, Robert Gilson, (1995) Improving the Performance Stability of Inductive Expert Systems Under Input Noise. Information Systems Research 6(4):328-356. https://doi.org/10.1287/isre.6.4.328

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1995 INFORMS

Please scroll down for article—it is on subsequent pages

## informs.

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Improving the Performance Stability of Inductive Expert Systems Under Input Noise

Vijay S. Mookerjee

Michael V. Mannino

Robert Gilson

Department of Management Science School of Business Administration University of Washington Seattle, Washington 98195-3200

Department of Management Science School of Business Administration University of Washington Seattle, Washington 98195-3200

Department of Management Science School of Business Administration University of Washington Seattle, Washington 98195-3200

Inductive expert systems typically operate with imperfect or noisy input attributes. We study design differences in inductive expert systems arising from implicit versus explicit handling of input noise. Most previous approaches use an implicit approach wherein inductive expert systems are constructed using input data of quality comparable to problems the system will be called upon to solve. We develop an explicit algorithm $( \mathrm { I D } 3 _ { \mathrm { e c p } } )$ that uses a clean (without input errors) training set and an explicit measure of the input noise level and compare it to a traditional implicit algorithm, $\mathbf { I D 3 _ { p } }$ (the ID3 algorithm with the pessimistic pruning procedure). The novel feature of the explicit algorithm is that it injects noise in a controlled rather than random manner in order to reduce the performance variance due to noise. We show analytically that the implicit algorithm has the same expected partitioning behavior as the explicit algorithm. In contrast, however, the partitioning behavior of the explicit algorithm is shown to be more stable $( \tt i . e .$ , lower variance) than the implicit algorithm. To extend the analysis to the predictive performance of the algorithms, a set of simulation experiments is described in which the average performance and coefficient of variation of performance of both algorithms are studied on real and artificial data sets. The experimental results confirm the analytical results and demonstrate substantial differences in stability of performance between the algorithms especially as the noise level increases.

Inductive expert systems—Input data noise—Performance stability—Variance reduction—Controlled scrambling

## 1. Introduction

Tnductive expert systems have become an important decision support tool as evi-Ldenced by considerable attention in the academic literature and business press, and

1047-7047/95/0604/0328/\$01.25 Copyright © 1995, Institute for Operations Research and the Management Sciences

Information Systems Research 6 : 4

a number of commercial products to develop such systems. Inductive expert systems are typically developed to support classification tasks, i.e., systems that attempt to classify an object as one of n categories (Quinlan 1986a). Examples of classification in business decision making include fault diagnosis in semiconductor manufacturing (Irani et al. 1993), bank failure prediction (Tam and Kiang 1990), and industry and occupation code prediction (Creecy et al. 1992). The primary goal of an inductive expert system is to perform at the same level of human experts. Such systems can provide many benefits to an organization (Holsapple and Whinston 1987) such as reducing decision making time, improving the consistency of decisions, and reducing dependence on scarce human experts.

An inductive expert system is constructed using a learning algorithm and data set. A learning algorithm develops classification rules that can be used to determine the class of an object from its description, i.e., from the object's attributes. The classification rules developed by these algorithms can be depicted as a decision tree in which the nonleaf nodes of the tree prescribe inputs that must be observed and the arcs represent states that the input variables can take. Leaf nodes in the tree indicate how an object is to be classified. Induction algorithms build such a tree from a set of preclassified cases referred to as the training set. Another part of the data set known as the test set is used to study the performance of a decision tree on novel cases. Inductive expert systems are typically developed to maximize solution accuracy, i.e., maximize the number of cases in which the output (decision, recommendation) provided by the system is similar to that provided by human experts. Economic considerations, for example, costs of observing inputs, benefits from system outputs, and other factors that may contribute to system value are rarely factored into system design (Mookerjee and Dos Santos 1993).

The subject of this paper is the design and performance evaluation of inductive expert systems using noisy input attributes. The presence of input noise can have a significant impact on the performance of an inductive expert system. We only consider noise that affects the input values used by the system to make classification decisions, not other forms of noise.¹ This definition includes errors from such causes as incorrectly measuring an input, wrongly reporting the state of an input, relying on stale values, and using imprecise measurement devices. Input errors in a training set can cause a learning algorithm to form a rule with an incorrect state for an input, while input errors in cases to be classified can cause the wrong rule to be used.

The specific issue studied here is how to account for the level of input noise: (i) implicitly through a training set with a representative level of noise, or (ii) explicitly through a noise parameter and a clean training set. Figure 1 graphically depicts the explicit and implicit approaches. In common practice, the implicit approach is used because it is cost effective and has been carefully studied. However, high variance of performance is a key disadvantage of the implicit approach that has not been widely discussed or studied. Our most important finding here is that an induction algorithm using an explicit noise parameter can have more stable performance than a comparable implicit algorithm

![](/api/attachments/DC5X39GC/fulltext/images/2fd0a07e938502485945e79a2e754f43e8b259e50791c171d1f2f797a6d89bd2.jpg)  
FIGURE 1. Explicit and Implicit Noise Handling.

Variation in performance is an outcome variable of interest in a wide variety of systems. For example, the performance of a manufacturing process is judged in terms of its mean behavior as well as by the variation in its behavior. Reducing variance is routinely used as a performance objective in survey research where errors may be introduced by interviewers, respondents, questionnaires, processing of forms, and so on. In the context of inductive expert systems however, past research has largely ignored this important design objective. Variation in performance could often be an extremely important aspect of an inductive expert system. For example, if a loan granting inductive expert system was to make very good decisions in one set of cases, but extremely poor ones in another set, it may cause the bank to fail in the period of poor performance. Thus, managers are likely to prefer a more stable system to a highly variable one even though the mean performance of the two systems is the same.

In addition to stable performance, explicit noise handling is interesting to study because there are a number of situations in which an explicit approach is more practical than an implicit approach. One such situation is when the training set is obtained from experts rather than from historical data. Here, an implicit approach would require that the input states in the training set be deliberately corrupted. In addition, if there are multiple ways to measure an input or if the level of noise in historical data is not representative of current practices, an explicit approach may be preferable.

Because explicit algorithms have not been carefully studied, the major topics presented are the design and performance evaluation of explicit algorithms. We design an explicit algorithm that injects noise according to a specified noise parameter as it partitions a data set. The novel aspect of the algorithm is that it injects noise in a controlled rather than random manner in order to reduce the variance due to noise. We show analytically that the expected partitioning behavior of the implicit and explicit algorithms is the same. However, we demonstrate analytically that the explicit algorithm has more stable partitions than the implicit algorithm. To extend the analytical results to the classification accuracy of the algorithms, we conduct a set of simulation experiments on several real and artificial data sets with a range of values for the number of classes and skewness in the class distributions. Our experimental results reveal that the expected accuracy and variance of accuracy of the algorithms are consistent with our analytical results.

This rest of this paper is organized as follows. In $\ S 2 ,$ we review related work on noise handling approaches used in inductive expert systems. In $\ S 3 ,$ ,we provide background on decision tree induction and analytically evaluate the behavior of the implicit and explicit algorithms: $\mathbf { I D 3 } _ { \mathbf { p } }$ and $\mathbf { I D 3 _ { e c p } } .$ In $\ S 4 ,$ ,we describe the hypotheses investigated, experimental designs used, and results obtained from a set of simulation experiments. A summary and conclusions are provided in $\ S$

## 2. Related Work

In this section, we summarize a theoretical study of input noise, various pruning procedures, and models to cope with measurement errors in surveys. Laird (Laird 1988) studied the Bernoulli Noise Process (BNP) as an extension of the theory of Probably, Approximately Correct (PAC) learning. The goal of PAC theory is to derive an upper bound on the number of examples needed to approximately learn a concept within a given error bound with a specified confidence level. A BNP is characterized by independent parameters for the classification error rate and the input error rate. Laird's basic result is that input error rate alone is not sufficient to determine the maximum number of examples needed. There must be an additional parameter that indicates the sensitivity of the true concept definition to input errors. This theoretical result about the relationship between the importance of an attribute and the impact of noise has been empirically demonstrated in other studies.

In more applied studies, researchers have developed pruning procedures (post construction techniques) to refine the rule set generated by a learning algorithm. Learning algorithms generally find a perfect set of rules for a training set, but the rules are usually too specialized leading to poor performance on unseen cases. Pruning techniques reduce specialization by eliminating rules in whole or part. Similarly, pruning techniques have also been found useful to handle noise because noise in a training set can lead to extra rules and highly specialized rules. For example, Quinlan (Quinlan 1987) demonstrated that four pruning methods significantly reduced the complexity of induced decision trees without adversely affecting accuracy. He later found on a study of the chi-square pruning technique (Quinlan 1986b) that the performance of a learning algorithm is better using a noisy training set than a perfect test set. He also found that increases in predictive performance from noise reduction depends on the importance of an input.

Two important themes in the development of pruning procedures are the use of an extra test set and parameters to control the amount of pruning. A number of techniques use an extra test set to choose among multiple collections of rules (critical value pruning (Mingers 1989) and error complexity pruning (Breiman et al. 1984)) or to reduce the complexity of the rules (minimum error pruning (Quinlan 1987)). These techniques require more data than techniques that prune using the training set alone (pessimistic pruning (Quinlan 1987), minimum error pruning (Niblett and Bratko 1986), and Laplace pruning (Christie 1993)). Mingers (Mingers 1989) found that pruning techniques using an extra test set achieved higher accuracy than techniques not using an extra test set. However, Quinlan (Quinlan 1987), in an earlier study, did not find higher accuracy as a result of extra test cases. Several techniques have been developed that use a single parameter to control the amount of pruning (error complexity pruning (Breiman et al. 1984) and m-probability-estimate pruning (Cestnik and Bratko 1991)). The parameters are rather coarse applying to the entire data set, not individual inputs. In addition, there are no guidelines for setting parameter values except that high values should be used when there is a large amount of noise. Moulet (Moulet 1991) developed input noise parameters for the ABACUS discovery system and demonstrated their effectiveness in learning simple laws of physics. However, he did not apply his technique to classification problems.

Unlike the work on pruning techniques, the area of measurement errors in surveys (Groves 1991) includes a rich stream of research on techniques to measure and reduce the level of input noise and models to compensate for the effect of input noise on prediction tasks. This area of research has developed a detailed classification of input noise beginning with systematic errors that introduce bias and random errors that cause variance. Beyond this division, the source of errors (interviewer, respondent, process, questionnaire) and the cause of errors (e.g., memory loss and nonresponse) are often identified. When the level of input noise is not known, it can be estimated using a reinterview technique (Hill 1991, Rao and Thomas 1991) where error-prone measurements are made on a sample and then more expensive and relatively errorfree measurements are made on a subsample. The reinterview technique is similar to the idea of using a clean training set with an explicit estimate of the noise level. Many models have been developed to compensate for the effect of input noise on regression (Fuller 1991), analysis of variance (Biemer and Stokes 1991), and estimation of survey statistics of categorical data (Biemer and Stokes 1991). However, there is no reported research on classification tasks.

## 3. Algorithm Design and Analysis

In this section, we present the explicit noise algorithm used in our simulation experiments and analyze the mean and variance of its partitioning behavior. Before presenting the explicit noise algorithm, we review the induction process underlying the baseline algorithm, ID3p (the ID3 algorithm (Quinlan 1986a) with the pessimistic pruning procedure).

## 3.1. Decision Tree Induction

Induction algorithms develop à decision tree by recursively creating nonleaf nodes and leaf nodes in the tree. Nonleaf nodes are labeled by input names. The input chosen to label a nonleaf node is determined using an input selection criterion and a set of cases. Traditionally, inputs are selected by their information content, measured by the reduction in information entropy achieved as a result of observing the input After an input has been chosen to label a nonleaf node, each of the q outgoing arcs are labeled by a possible state of the selected input where q is the number of possible states. The set of cases used to compute the label of a node (for the root node this is the entire training set) is then partitioned into q subsets such that the state of the input used to label the node is the same within each subset. The tree can grow along each outgoing arc using the subset of cases corresponding to the state of the input used to label the arc. Creation of nonleaf nodes continues along each path of the tree until a stopping condition is reached, at which stage a leaf node is created. Leaf nodes are labeled using a classification function.

An important factor that must be considered in the design of an induction algorithm is the input selection criterion. The input selection criterion determines how, from a set of candidate inputs, an input is chosen to label a nonleaf node. We describe the input selection criterion for the ID3 algorithm in the remainder of this subsection

Let

$$
\begin{array}{c} \tilde {D} _ {N} \\ \tilde {X} _ {1}, \tilde {X} _ {2}, \ldots , \tilde {X} _ {p} \end{array}
$$

be a randomly drawn training set of size $\pmb { N } ,$ be $\pmb { p }$ observable input variables that may be used to classify an object,

$$
x _ {k 1}, x _ {k 2}, \dots , x _ {k q}
$$

be q possible states for input $\tilde { X } _ { k } ,$

be the random variable for the class of an object,

$$
\begin{array}{c} c _ {1}, c _ {2}, \dots , c _ {m} \\ Z \end{array}
$$

be m possible states for the class variable $\tilde { \psi } ,$

be a partition of the training set $( \tilde { Z } \subseteq \tilde { D } _ { N } ) ,$

be an input state conjunction, ${ \tt e . g . } , \tilde { X } _ { 1 } = x _ { 1 4 } \wedge \tilde { X } _ { 2 } = x _ { 2 3 } ,$

$$
L (\tilde {Z}, \pi)
$$

be a partition of $\tilde { z }$ such that π is true,

$k ( \check { Z } )$ be a classification function that determines how a leaf node is labeled, and

$g ( \tilde { X } _ { k } | \tilde { Z } )$ be the expected gain for input $\tilde { X } _ { k }$ given $\tilde { z }$

The input selection criterion in the ID3 algorithm chooses the input with the maximum information content (gain) measured by the reduction in information entropy (Shannon and Weaver 1949) as a result of observing the input. Formally, the gain of input $\tilde { X } _ { k }$ is defined as:

$$
g (\tilde {X} _ {k} | \tilde {Z}) = \Delta \mathrm{EN} (\tilde {X} _ {k} | \tilde {Z}) = \mathrm{EN} (\tilde {Z}) - \mathrm{EN} (\tilde {X} _ {k} | \tilde {Z}) \quad \text {where}\tag{1}
$$

$$
\mathrm{EN} (\tilde {Z}) = - \sum_ {r = 1} ^ {m} P [ \tilde {\psi} = c _ {r} | \tilde {Z} ] \log_ {2} P [ \tilde {\psi} = c _ {r} | \tilde {Z} ]\tag{2}
$$

is the initial expected entropy,

$$
\operatorname{EN} \left(\tilde {X} _ {k} \mid \tilde {Z}\right) = \sum_ {j = 1} ^ {q} P \left[ \tilde {X} _ {k} = x _ {k j} \mid \tilde {Z} \right] \operatorname{EN} \left(L \left(\tilde {Z}, \tilde {X} _ {k} = x _ {k j}\right)\right)\tag{3}
$$

is the expected entropy after observing $\tilde { X } _ { k }$ , and

$$
\operatorname{EN} \left(L \left(\tilde {Z}, \tilde {X} _ {k} = x _ {k j}\right)\right) = - \sum_ {r = 1} ^ {m} P [ \tilde {\psi} = c _ {r} | L (\tilde {Z}, \tilde {X} _ {k} = x _ {k j}) ] \log_ {2} P [ \tilde {\psi} = c _ {r} | L (\tilde {Z}, \tilde {X} _ {k} = x _ {k j}) ]\tag{4}
$$

is the expected entropy in the partition $L ( \tilde { Z } , \tilde { X } _ { k } = x _ { k j } )$

ID3 estimates the probabilities in Equations (2) through (4) by sample proportions obtained from the training data.

To demonstrate the above equations, consider a sample of 100 cases $\tilde { ( Z ) }$ with 2 classes $( c _ { 1 } = 6 6 , c _ { 2 } = 3 4 )$ ). Let input $\tilde { X } _ { k }$ with states $x _ { k 1 } , x _ { k 2 } , x _ { k 3 }$ be used to partition the 100 cases. From Equation (2) the initial entropy is:

$$
\operatorname{EN} (\tilde {Z}) = - (0. 6 6 * \log_ {2} 0. 6 6 + 0. 3 4 * \log_ {2} 0. 3 4) = 0. 9 2 4 8.
$$

For $\tilde { X } _ { k } = x _ { k 1 } ,$ , let $c _ { 1 } = 4 8$ and $c _ { 2 } = 1 2$ be the subpartition of cases obtained. The entropy within this subpartition is:

$$
\operatorname{EN} \left(L \left(\tilde {Z}, \tilde {X} _ {k} = x _ {k 1}\right)\right) = - \left(0. 8 * \log_ {2} 0. 8 + 0. 2 * \log_ {2} 0. 2\right) = 0. 7 2 1 9.
$$

For $\tilde { X } _ { k } = x _ { k 2 }$ , let $c _ { 1 } = 1 0$ and $c _ { 2 } = 2 0$ be the subpartition with $\mathbb { E } \mathbb { N } ( L ( \tilde { Z } , \tilde { X } _ { k } = x _ { k 2 } ) )$ $\mathbf { \eta = 0 . 9 1 4 9 }$ computed the same as above. For $\tilde { X } _ { k } = x _ { k 3 } ,$ , let $c _ { 1 } = 8$ and $c _ { 2 } = 2$ be the

Mookerjee • Mannino • Gilson

subpartition with $\operatorname { E N } ( L ( \tilde { Z } , \tilde { X } _ { k } = x _ { k 3 } ) ) = 0 . 7 2 1 9$ . From Equation (3), the entropy after observing $\tilde { X } _ { k }$ is:

$$
\mathrm{EN} \left(\tilde {X} _ {k} \mid \tilde {Z}\right) = (0. 6 * 0. 7 2 1 9 + 0. 3 * 0. 9 1 4 9 + 0. 1 * 0. 7 2 1 9) = 0. 7 7 9 8.
$$

Thus from Equation (1) the gain from observing input $\tilde { X } _ { k }$ is:

$$
g (\tilde {X} _ {k} | \tilde {Z}) = \Delta \operatorname{EN} (\tilde {X} _ {k} | \tilde {Z}) = 0. 9 2 4 8 - 0. 7 7 9 8 = 0. 1 4 4 9.
$$

To cope with noise and overfitting, we augment ID3 with the pessimistic pruning procedure (Quinlan 1987). We call the augmented ID3 algorithm, $\mathbf { I D 3 _ { p } } .$ The pessimistic pruning procedure uses a statistical measure to determine whether replacing a subtree by its best leaf $( \tt i . e . ,$ , the classification that maximizes accuracy for a given set of cases) is likely to increase accuracy. If so, the branch is replaced by its best leaf, otherwise the branch is retained. Once all branches have been examined, the process terminates. A more detailed description can be found in Appendix B. We use the pessimistic pruning procedure because it is easy to implement, effective on noisy data (Mingers 1989), and does not require an extra test set.

## 3.2. Model of Noise

Inductive expert systems typically operate under conditions where inputs are subject to noise. Noise occurs when the true input state is perturbed by a measurement process. We assume that measurement errors are independent of the time of measurement and the true state of an input. If we ignore differences among wrong states (e.g., measuring a high value as medium or low), noise can be characterized as a binomial process with mean $^ { c , }$ the probability of correct measurement. The value of C can be estimated from empirical data as follows. First, for each noisy input, collect a representative sample of input values. Second, correct the noisy values through various techniques such as repeated measurement (Hill 1991, Rao and Thomas 1991) and/or improved measurement, that is, using more expensive and relatively error free devices. Third, estimate the population error rate from the sample as the number of values that are incorrect divided by the sample size. One minus the sample error rate is an unbiased estimate of C.

We define the parameter W as the probability of wrong or incorrect measurement, a measure of the likelihood of disruptions in the measurement process that lead to a particular incorrect state being recorded.² We assume that wrong states are equally likely and that all inputs have the same level of noise. Thus, the relationship $C + ( q -$ $| ) W = 1$ holds for any input since there are $q - 1$ incorrect states. For example, if there is a 5 state input and the probability of correct measurement is $C = 0 . 8 ,$ , then any wrong state has a probability of $W = ( 1 - 0 . 8 ) / ( 5 - 1 ) = 0 . 0 5$ . Although the assumptions about constant $c$ across inputs and constant W within an input's states can be easily relaxed, we use them to simplify our analysis. Without these assumptions, many more noise parameters will have to be estimated. More precisely, C and W are defined as:

$$
C = P [ \tilde {X} _ {k o} = x _ {k j} | \tilde {X} _ {k t} = x _ {k j} ] \quad \forall k, j,\tag{5.1}
$$

$$
W = P [ \tilde {X} _ {k o} = x _ {k j} | \tilde {X} _ {k t} = x _ {k i} ] \quad \forall k, \forall j \neq i,\tag{5.2}
$$

where $\tilde { X } _ { k o } , \tilde { X } _ { k t }$ are the random variables for the observed (noisy) and true states of input $\tilde { X } _ { k } .$

To analytically describe the impact of noise on the input gain, we state Proposition 1:

PROPOSITION 1.

$$
\frac {\partial g (\tilde {X} _ {k o} | \tilde {Z} ^ {C})}{\partial C} > 0, \quad C \in (1 / q, 1 ],\tag{6.1}
$$

$$
= 0, \quad C = 1 / q,\tag{6.2}
$$

$$
<   0, \quad C \in [ 0, 1 / q),\tag{6.3}
$$

where $\tilde { z } ^ { c }$ is a noisy partition with noise level C.

With no noise, the gain is at its highest $( C = 1 )$ . As noise is increased (value of C is decreased from 1 to $1 / q )$ , the gain decreases to the point where the value of C is $1 / q$ (6.1). When C is equal to $1 / q ,$ there is no benefit from observing the input because it could occur in any of its states with equal probability (6.2). As the value of C decreases below $1 / q ,$ the noise becomes so high that the observed states become predictably incorrect. Hence, observed states of the input again begin to provide some information (6.3).

Thus the nature of the relationship between the noise level and the gain is convex, validating that we are dealing with a reasonable model of noise. In Appendix A, we prove Proposition 1 for a special case. In addition, our simulations strongly suggest that the gain monotonically decreases $( \ i . \ e . ,$ less uncertainty reduction) as the correct measurement probability increases from 0 to 1/q and then monotonically increases until the correct measurement probability is 1.

## 3.3. Impact of Noise on Expected Behavior

In this subsection, we demonstrate how the information content of a noisy input is computed in an implicit version of ID3 $( \mathbb { I D } 3 _ { \mathfrak { p } } )$ where a noisy training set is used and in an explicit version of ID3 $( \mathbf { I D 3 _ { e p } } )$ where a clean training set and noise parameters are used.

3.3.1. Implicit Handling of Noise. In an implicit algorithm such as $\mathbf { I D 3 _ { p } } ,$ the level of noise acts implicitly on the gain of an input. Specifically, Equation (3) uses two probability estimates: (i) the probability of a class given a new input and the set of previously observed inputs, and (ii) the probability of a new input given the set of previously observed inputs. With noise, we need to estimate the same two probabilities except that it is the noisy observed states rather than true states of the input that are estimated. Equation (7) shows the expected entropy of $\tilde { X } _ { k o }$ after observing a set of noisy inputs $( \tilde { \Pi } _ { o } ) . \mathbf { I D } 3 _ { \mathbf { p } }$ estimates the probabilities in Equation (7) by sample proportions obtained from the noisy training data.

$$
\mathrm{EN} (\tilde {X} _ {k o} | \tilde {\Pi} _ {o}) = - \sum_ {j = 1} ^ {q} P [ \tilde {X} _ {k o} = x _ {k j} | \tilde {\Pi} _ {o} ] \sum_ {r = 1} ^ {m} \zeta_ {r} \log_ {2} \zeta_ {r}\tag{7}
$$

where $\xi _ { r } = P [ \tilde { \psi } = c _ { r } | \tilde { X } _ { k o } = x _ { k j } \wedge \tilde { \Pi } _ { o } ]$ and $\tilde { \Pi } _ { o } = \tilde { \Pi } _ { 1 o } \wedge \ldots \wedge \tilde { \Pi } _ { d o }$ is the set of previous observations on the path

3.3.2. Explicit Handling of Noise. Explicit algorithms estimate the probabilities in Equation (7) using a clean training set and noise parameters rather than with a noisy training set. Both implicit and explicit algorithms are subject to noise processes having the same mean noise parameters (C and Win our case). The difference is that the noise process has already occurred for implicit algorithms as opposed to the noise process occurring as part of explicit algorithms. Thus, implicit and explicit algorithms will compute the same expected decision tree because the expected gain calculations are the same. Even though explicit algorithms have better information (both the noise level and clean data), their expected predictive ability is the same as that of implicit algorithms. However, in subsection 3.4, we demonstrate that the additional information can be used to reduce the variance in the predictive performance of explicit algorithms.

For explicit algorithms, one way to estimate the information content of a noisy input is to use a recursive Bayesian updating scheme (Pearl 1988). In the Bayesian approach, we rewrite the expression for $\smash { \xi _ { r } }$ from Equation (7) as Equation (8) using the chain propagation $\mathrm { \tt m i e } ^ { 3 }$ (Pearl 1988, p. 154). Because we start with a clean training set, the information content of an input in its true state can be estimated. Note that we use the property of conditional independence wherein the true state separates the class and the observed state (Pearl 1988, p. 154):

$$
\zeta_ {r} = \sum_ {i = 1} ^ {q} P [ \tilde {X} _ {k t} = x _ {k i} | \tilde {X} _ {k o} = x _ {k j} \wedge \tilde {\Pi} _ {o} ] P [ \tilde {\psi} = c _ {r} | \tilde {X} _ {k t} = x _ {k i} \wedge \tilde {\Pi} _ {o} ].\tag{8}
$$

In Equation (8), the probability of a class given the current true state and the history of observed states can be written as:

$$
P [ \tilde {\psi} = c _ {r} | \tilde {X} _ {k t} = x _ {k i} \wedge \tilde {\Pi} _ {o} ] = \sum_ {\tilde {\Pi} _ {t} \in \pi_ {t}} P [ \tilde {\psi} = c _ {r} | \tilde {X} _ {k t} = x _ {k i} \wedge \tilde {\Pi} _ {t} ] P [ \tilde {\Pi} _ {t} | \tilde {X} _ {k t} = x _ {k i} \wedge \tilde {\Pi} _ {o} ]\tag{9}
$$

where $\tilde { \Pi } _ { t }$ is the random vector for the combination of previously observed variables (without noise) and $\pmb { \pi _ { t } }$ is the set of true state vectors.

Equation (9) demonstrates the difficulty of a Bayesian approach. The first term of the right-hand side of (9) must be computed $O ( ( p - d ) ( q ^ { d } ) )$ times where d is the node or input level (root node is level 0) in a decision tree $\mathbf { \nabla } _ { \mathbf { \mathcal { P } } }$ is the number of inputs, and q is the average number of input states. The cardinality of $\pi _ { d }$ is $q ^ { d }$ as $\pmb { \pi _ { d } }$ contains all possible true states of all inputs on the path. The joint probability calculations must be repeated for all remaining inputs $( p - d )$ . Since the depth of a tree is partially dependent on the number of inputs, a recursive Bayesian updating approach is impractical for computational reasons.

As an alternative to a Bayesian updating approach, noise effects can be propagated during tree construction by introducing noise into partitions by randomly scrambling cases using the parameters C and W. This amounts to computing the class probabilities using a partition instead of calculating the probabilities in (9). A formal description of the random scrambling procedure follows:

## Procedure Random Scrambling

## Input

Z: a partition

X: branching input with q states

C: noise level

Output

S: a ‘scrambled’ set of partitions of input X, $S = \{ S _ { k } | S _ { k } \}$ is partition of S} k $\mathbf { \Omega } = 1 , 2 , \ldots , q .$

Procedure

1. Initialize each $\pmb { S _ { k } } \in \pmb { S }$ to φ.

2. Let T' be the set of true partitions resulting from splitting Z into q partitions on input X.

3. For each partition $\pmb { T _ { k } } \in \pmb { T }$ do

3.1. For each case ${ \pmb { \tau } } \in { \pmb { T } } _ { \pmb { k } }$ do

3.1.1. Let r be a random number in [0,1].

3.1.2. If $r \le C$ then set $\textstyle S _ { k } : = S _ { k } \cup$ r else randomly choose $S _ { j } , j \neq k$ and'set $S _ { j } : = S _ { j } \cup \tau .$

In contrast to the Bayesian updating approach, the complexity of injecting noise through random scrambling is $O ( ( p - d ) q )$ because q scrambling operations for each input are necessary and only the current input needs to be scrambled. The effect of noise from all but the current input on the path is already included in the starting noisy partition.

Figure 2 illustrates the random scrambling procedure. The root box depicts a partition of size 100 with 66 cases expected of class $c _ { 1 }$ and 34 cases expected of $c _ { 2 } .$ Input

![](/api/attachments/DC5X39GC/fulltext/images/6851378fcac4071454b3322a98c1927ceceb3edc25b518b09d80fb647bcc3b1c.jpg)  
FiGURE 2. Example of the Random Scrambling Process.

$X _ { k }$ is selected and partitioned by its three states where the expected size and class frequencies of the partitions are shown in the boxes without parentheses.4 Noise is then introduced by scrambling all the partitions of $X _ { k }$ according to the correct noise probability $C = 0 . 8$ . For each case in a partition, a random number is drawn to determine if the case should be moved to a partition associated with another state of the input. If the number is less than or equal to $^ { c , }$ the case remains in its original partition. Otherwise the case is randomly moved to a partition associated with another state of the input. After scrambling, the size and class frequencies of each partition are typically more uniform because of the impact of noise. In Figure $^ { 2 , }$ the scrambled partitions are beneath the clean partitions. The lines indicate that cases can be moved from a clean partition to any noisy partition.

The explicit algorithm $\mathbf { I D 3 _ { e p } }$ uses the random scrambling procedure to introduce noise into partitions. First, the usual partitioning process of the ID3 algorithm is performed. Second, the partitions created in the first step are scrambled using the random scrambling procedure. After all partitions of an input are scrambled, the normal formulas for the input selection, stopping rule, and classification function are used. Note that we retain the pessimistic pruning procedure in $\mathbf { I D 3 _ { e p } } .$ Thus, the only difference between $\mathbf { I D 3 _ { p } }$ and $\mathbf { I D 3 } _ { \mathtt { e p } }$ is the way that noise is treated. In $\mathbf { I D 3 _ { p } } ,$ the treatment of noise is indirect through a sample of the data collection process. In $\mathbf { I D 3 _ { e p } } ,$ the treatment of noise is indirect through random injection of noise in a clean training set using the parameters $c$ and $W .$ Despite the differences in handling noise, the expected behavior of both algorithms is governed by Equation (7). This observation is similar to the results of previous research comparing input selection criteria (Mantaras 1991).

## 3.4. Impact of Noise on Variance

As discussed in subsection 3.3, explicit algorithms have no advantage over implicit algorithms in terms of expected predictive ability. The advantage of explicit noise handling lies in the potential to make performance more stable. In this section, we study the impact of noise on the variance in class frequencies between a binomial noise process and a constant noise process. The binomial noise process represents $\mathbf { I D 3 } _ { \mathfrak { p } }$ and $\mathbf { I D 3 _ { e p } }$ in which noise is randomly introduced either in the training set or through the random scrambling process. The constant noise process represents a controlled variation of $\mathbf { I D } 3 _ { \mathrm { e p } } \left( \mathbf { I D } 3 _ { \mathrm { e c p } } \right)$ in which class frequencies in noisy partitions are set to their estimated expected values. As the analysis elucidates, the variance in size due to noise is much less in the constant noise process than in the binomial noise process.

We begin with the sampling variance common to both noise processes limiting our focus to a single input, state, and class. Let

$$
P [ \tilde {X} _ {k t} = x _ {k j} ] = \gamma_ {j} \quad \text { and } \quad P [ \tilde {\Psi} = c _ {r} | \tilde {X} _ {k t} = x _ {k j} ] = \rho_ {r j}
$$

be population parameters and $s ( L ( \tilde { Z } _ { n } , \tilde { X } _ { k t } = x _ { k j } ) )$ be the size of the partition ${ \tilde { Z } } _ { n }$ where $\tilde { X } _ { k t } = x _ { k j }$

The expected value and variance of the size of a partition of size n where $\tilde { X } _ { k t } = x _ { k j }$ are defined i Equations (10) and (11), respectively. For each case, the sampling process selects $\tilde { X } _ { k t } = x _ { k j }$ with probability $\gamma _ { j } .$ Thus, the size of a partition is binomially distributed with mean and variance as shown in Equations (10) and (11):

$$
E (s (L (\tilde {Z} _ {n}, \tilde {X} _ {k l} = x _ {k j}))) = n \gamma_ {j},\tag{10}
$$

$$
V (s (L (\tilde {Z} _ {n}, \tilde {X} _ {k t} = x _ {k j}))) = n \gamma_ {j} (1 - \gamma_ {j}).\tag{11}
$$

To analyze the mean and variance of the subpartition size where $\tilde { \psi } = c _ { r }$ we need to apply Wald's theorem (Ross 1970, p. 37). Wald's theorem defines the expected value and variance of the sum of $\tilde { \kappa }$ random variables where $\tilde { K }$ is also a random variable. The expected value of the sum of $\tilde { K }$ independent, identically distributed random variables $( \tilde { X _ { i } } )$ is given by $E ( \tilde { K } ) E ( \tilde { X } _ { i } )$ . The variance of the sum is given by $E ( \tilde { K } ) V ( \tilde { X } _ { i } )$ $+ \ V ( \tilde { K } ) ( E ( \tilde { X } _ { i } ) ) ^ { 2 }$ . Here, the expected size of the beginning partition is $\pmb { n } \gamma _ { j }$ as defined in (10). Within this partition, the probability of $\tilde { \psi } = c _ { r }$ is $\rho _ { \vec { \pmb { \imath } } ^ { \prime } }$ Applying Wald's theorem, the mean and variance of the subpartition size are defined by (12) and (13). In (13), we assume that the class random variables of the individual cases within the partition are independent and identically distributed:

$$
E (s (L (\tilde {Z} _ {n}, \tilde {\psi} = c _ {r} \wedge \tilde {X} _ {k t} = x _ {k j}))) = n \gamma_ {j} \rho_ {r j} = \mu_ {r j},\tag{12}
$$

$$
V (s (L (\tilde {Z} _ {n}, \tilde {\psi} = c _ {r} \wedge \tilde {X} _ {k t} = x _ {k j}))) = n \gamma_ {j} \rho_ {r j} (1 - \rho_ {r j}) + n \gamma_ {j} (1 - \gamma_ {j}) \rho_ {r j} ^ {2} = \sigma_ {r j} ^ {2}.\tag{13}
$$

Now consider the effect of the binomial noise process common to $\mathbf { I D } 3 _ { \mathbf { p } }$ and $\mathbf { I D 3 _ { e p } } .$ This process introduces more variance in the class frequency because cases are assigned at random to partitions based on the parameter C. The expected value and variance of the size of the above partition after noise is given in Equations (14) and (15) where the noise is a binomial process with mean and variance $( C , ( 1 - C ) C )$ Note that these formulations involve another application of Wald's theorem because once again the size of the beginning partitions is uncertain as defined in (12) and (13). In (14) and (15), $\mu \gamma _ { j } \pmb { \rho } _ { j }$ replaces $\pmb { { \cal E } } ( \tilde { \pmb { { \cal K } } } )$ for correct input states and $\pmb { n } \gamma _ { i } \pmb { \rho } _ { \pmb { n } }$ replaces $\pmb { { \cal E } } ( \tilde { \pmb { { \cal K } } } )$ for $q - 1$ incorrect input states. For correct input states, $c$ replaces $E ( \tilde { X _ { i } } )$ and W replaces $\pmb { \cal E } ( \tilde { X } _ { i } )$ for ${ \pmb q } - { \pmb 1 }$ incorrect states. In (15), $\sigma _ { \eta } ^ { 2 }$ from (13) replaces $V ( \tilde { K } )$ for correct input states and $\pmb { \sigma } _ { r i } ^ { 2 }$ replaces $V ( \tilde { K } )$ for $q - 1$ incorrect states. For correct input states, $C ( 1 - C )$ replaces $V ( { \tilde { X _ { i } } } )$ and $W ( 1 - W )$ replaces $V ( \tilde { X _ { i } } )$ for $q - 1$ incorrect states.

$$
E (s (L (\tilde {Z} _ {n}, \tilde {\psi} = c _ {r} \wedge \tilde {X} _ {k o} = x _ {k j}))) = n \gamma_ {j} \rho_ {r j} C + \sum_ {i \neq j} ^ {q} n \gamma_ {i} \rho_ {r i} W = C \mu_ {r j} + W \sum_ {i \neq j} ^ {q} \mu_ {r i},\tag{14}
$$

V(s(L(Žn, ↓ = c, ∧ Xko = xj)

$$
= C (1 - C) \mu_ {r j} + C ^ {2} \sigma_ {r j} ^ {2} + W (1 - W) \sum_ {i \neq j} ^ {q} \mu_ {r i} + W ^ {2} \sum_ {i \neq j} ^ {q} \sigma_ {r i} ^ {2}.\tag{15}
$$

Now consider the effect of the constant noise process associated with the controlled scrambling algorithm $\mathbf { I D 3 _ { e c p } } .$ Here, the class frequency is set to its expected value. Therefore, the variance due to noise disappears. However, the variance of the sampling process remains. Equation (16) for the partition size with a constant noise process is derived using the variance of a constant times a function of a random variable. Alternatively, the variance can be derived by dropping the first and third terms in (15) because the constant noise process has zero variance. Note that the expected value remains as defined in Equation (14):

$$
V (s (L (\tilde {Z} _ {n}, \tilde {\psi} = c _ {r} | \tilde {X} _ {k o} = x _ {k j}))) = C ^ {2} \sigma_ {r j} ^ {2} + W ^ {2} \sum_ {i \neq j} ^ {q} \sigma_ {r i} ^ {2}.\tag{16}
$$

![](/api/attachments/DC5X39GC/fulltext/images/b221874b66e8d69706e0379ed6c8111a439003cef1977cf22678d1f63ac4aef4.jpg)  
FIGURE 3. Graphical Comparison of Noise Processes of a Node at Level 4.

To further depict the difference between the binomial noise process and the constant noise process, consider a numèrical example based on Figure 2 where the population statistics are given below:

$$
P [ \tilde {X} _ {k t} = x _ {k 1} ] = 0. 6, \quad P [ \tilde {X} _ {k t} = x _ {k 2} ] = 0. 3, \quad P [ \tilde {X} _ {k t} = x _ {k 3} ] = 0. 1,
$$

$$
P [ \tilde {\psi} = c _ {1} | \tilde {X} _ {k t} = x _ {k 1} ] = 0. 8, \quad P [ \tilde {\psi} = c _ {1} | \tilde {X} _ {k t} = x _ {k 2} ] = 0. 3 3, \quad P [ \tilde {\psi} = c _ {1} | \tilde {X} _ {k t} = x _ {k 3} ] = 0. 8,
$$

$$
P [ \tilde {\psi} = c _ {2} | \tilde {X} _ {k t} = x _ {k 1} ] = 0. 2, \quad P [ \tilde {\psi} = c _ {2} | \tilde {X} _ {k t} = x _ {k 2} ] = 0. 6 7, \quad P [ \tilde {\psi} = c _ {2} | \tilde {X} _ {k t} = x _ {k 3} ] = 0. 2.
$$

The labeling of the boxes in Figure 2 shows the expected values for the input state and class in the clean and noisy partitions. The variances for the binomial (Equation (15)) and constant noise (Equation (16)) processes are shown in round and curly brackets, respectively, next to the expected values (Equation (14)) in the noisy partitions. Note the reductions for the constant noise process

Figure 3 shows a graphical view of the difference between the constant and binomial noise processes for a particular class. Here there are two curves corresponding to partitions at level 4 in a decision tree. The curves for the binomial noise process are based on (15), while the curve for the constant noise process is based on (16). For the binomial noise process, Figure 3 demonstrates that the coefficient of variation increases as the noise level increases with the peak about 1/q. Although not shown here, the difference between the coefficient of variation of the two processes increases as the depth of the tree increases because observing more noisy inputs introduces additional uncertainty.

The goal of reducing the variance of the subpartition sizes is to make the input selection process more stable and ultimately to reduce the variance in performance on a set of unseen cases. Analytically, it is rather difficult to measure the variance in the gain because distribution assumptions are necessary and the mathematics is complicated. Since any distribution assumptions would rarely be met, it seems better to make a strong statement about the subpartition sizes rather than a weak statement about the gain. Even with a strong statement about the variance of the gain, simulation experiments are still necessary to link the theoretical behavior with performance on unseen cases.

## 3.5. Controlled Scrambling Procedure

The controlled scrambling procedure is designed to behave as close as possible to the constant noise process and thereby to reduce the variance in the gain and ultimately, the performance on unseen cases. The differences between the controlled scrambling procedure and the constant noise processes are due only to rounding of fractional values and conserving the number of cases in various partitions of the training set. The controlled scrambling procedure first computes the class and true input state frequencies as close as possible to their estimated values and then randomly assigns cases to match the computed frequencies. Control of class frequencies follows from the discussion in §3.4.

The reason for controlling the true state frequency is a little subtle, however. The true state distribution shows the fraction of each true state within a noisy partition. For example in Figure $^ { 2 , }$ the true state frequencies in the noisy partition $x _ { k 1 }$ are 48 $( 6 0 * 0 . 8 )$ for true state $x _ { k 1 } , 3 \ ( 3 0 * 0 . 1 )$ for true state $x _ { k 2 } ,$ and 1 $( 1 0 * 0 . 1 )$ for true state $x _ { k 3 } .$ . Controlling the true state frequency does not affect the variance of the class frequency in the current node, but rather it potentially impacts the class frequencies in descendant nodes. The true state frequency is important to control when the next input to select in the decision tree is conditionally dependent on the current input state. When there is a strong dependence, reducing the variance in true state frequencies will reduce variance in the class frequencies of the next input. For example, the constant noise curve in Figure 3 was generated with a strong dependence between the current input state and the next input state. Thus, controlling the true state frequencies is a matter of reducing variance in descendant nodes rather than in the current node.

Computation of the class and true state frequencies is accomplished by solving two optimization models. First, the controlled scrambling procedure assigns class frequencies such that the assignment minimizes the distance between the assigned class frequencies and estimated class frequencies in a set of partitions (all the partitions of an input) subject to integer, nonnegativity, and case conservation constraints. The latter constraints ensure that the total number of cases is the same before and after allocation by the controlled scrambling procedure. Second, the controlled scrambling procedure assigns true state frequencies such that the assignment minimizes the distance between the assigned true state frequencies and the estimated true state frequencies in a subset of a partition (all cases of the same class) subject to integer, nonnegativity, and case conservation constraints. The latter constraints are based on the assignment made by the class frequency optimization model. Let

$\pmb { d ( c _ { r } , j ) }$ be the assigned frequency of class $c _ { r }$ in the noisy partition where $X _ { k o } = x _ { k j } ,$ $s ( c _ { r } , L ( Z , X _ { k t } = x _ { k j } ) )$ be the frequency of class $c _ { r }$ in the partition Z where $X _ { k t } = x _ { k j } ,$ $d ( c _ { r } , j )$ be the estimated frequency of class $c _ { r }$ in the noisy partition where $X _ { k o } = x _ { k j } ,$

$$
e \left(c _ {r}, j\right) = C * s (c _ {r}, L (Z, X _ {k t} = x _ {k j})) + W \sum_ {i \neq j} ^ {q} s \left(c _ {r}, L (Z, X _ {k t} = x _ {k i})\right),
$$

$d ( x _ { k i } , r , j )$ be the assigned frequency of true state $x _ { k i }$ in the noisy partition where $X _ { k o }$ $\approx x _ { k j }$ and the class is $c _ { n }$

$e ( x _ { k i } , r , j )$ be the estimated frequency of true state $x _ { k i }$ in the noisy partition where $X _ { k o } = X _ { k j }$ and the class is $c _ { n }$

$$
e (x _ {k i}, r, j) = C * s \left(c _ {r}, L \left(Z, X _ {k t} = x _ {k i}\right)\right) \text {   if   } i = j,
$$

$$
e (x _ {k i}, r, j) = W * s \left(c _ {r}, L (Z, X _ {k t} = x _ {k i})\right) \text {   if   } i \neq j.
$$

The class frequency optimization model solves m optimization problems $\mathbf { C F _ { \mathbf { \hat { \eta } } } } _ { \mathbf { \hat { \eta } } }$ $r = 1 , \ldots , m .$ . In each problem, there are q decision variables, $d ( c _ { n } j ) , j = 1 , \ldots , q .$

Problem CF,:

$$
\operatorname{Min} \left(\sum_ {j = 1} ^ {q} (d (c _ {r}, j) - e (c _ {r}, j)) ^ {2}\right)
$$

$$
\text { s.t. } \quad d (c _ {n}, j) \geq 0 \quad \text { and   integer, } \quad \forall j = 1, \dots , q,
$$

$$
\sum_ {j = 1} ^ {q} d (c _ {r}, j) = \sum_ {j = 1} ^ {q} s (c _ {r}, L (Z, X _ {k t} = x _ {k j})) \quad \text { case   conservation   constraint. }\tag{17}
$$

The true state frequency optimization model solves mq optimization problems $\mathrm { T S F } _ { r j } , r = 1 , \ldots , m , j = 1 , \ldots , q$ (one for each combination of class and observed state). In each problem, there are q decision variables, $d ( x _ { k i } , r , j ) , i = 1 , \ldots , q .$

Problem $\operatorname { T S F } _ { p { \mathrm { i } } }$

$$
\operatorname{Min} \left(\sum_ {i = 1} ^ {q} (d (x _ {k i}, r, j) - e (x _ {k i}, r, j)) ^ {2}\right)
$$

$$
\text { s.t. } \quad d (x _ {k i}, r, j) \geq 0 \quad \text { and   integer } \quad \forall i = 1, \dots , q,
$$

$$
\sum_ {i = 1} ^ {q} d (x _ {k i}, r, j) = d ^ {*} (c _ {r}, j) \quad \text { case   conservation   constraint }
$$

where $d ^ { * } ( c _ { r } , j )$ is the optimal value of $\pmb { d ( c _ { n } , j ) }$ in $\mathbf { C F } _ { r }$

(18)

The controlled scrambling procedure initially assigns class frequencies $\displaystyle ( d ( c _ { r } , j ) )$ by rounding the estimated class frequencies to the nearest integer value. If the case conservation constraint is not satisfied for a set of assigned class frequencies, the assigned class frequencies are adjusted in the order that minimizes the distance from the estimated class frequency until the constraint is satisfied. A similar procedure is used for the assigned true state frequencies. More precisely, the algorithm to compute the assigned class frequencies is shown in procedure Assign Class Frequencies.

Input

## Procedure Assign Class Frequencies

Z: a partition

$X _ { k }$ : branching input with q states

C: noise level

Output

D: a set of assigned class frequencies for $z$ and $X _ { k } ,$

$D = \{ d ( c _ { r } j ) | d ( c _ { r } j )$ is an assigned class frequency $r = 1 , 2 , \ldots , m ; j = 1 , 2 , \ldots , q \}$ Procedure

1. For each class $c _ { r }$ and each state $x _ { k j }$ of $X _ { k } ,$ set $d ( c _ { r } , j ) = r o u n d e d ( e ( c _ { r } , j ) )$

2. For each set of assigned frequencies of a class $( \{ d ( c _ { r } , j ) | j = 1 \cdot \cdot \cdot q \} )$ , adjust them such that the case conservation constraint is satisfied. Stop when the case conservation constraints are satisfied for all sets of assigned class frequencies.

2.1.If $\begin{array} { r } { \sum _ { j = 1 } ^ { q } d ( c _ { r } , j ) > \sum _ { j = 1 } ^ { q } s ( c _ { r } , L ( Z , X _ { k } = x _ { k j } ) ) } \end{array}$ , then adjust by taking away from some $d ( c _ { r } , j )$ . Sort $\pmb { d ( c _ { r } , j ) }$ by descending order of $( d ( c _ { r } , j ) - e ( c _ { r } , j ) )$ ). Starting from the $\pmb { d ( c _ { r } , j ) }$ with the largest difference, compute new $d ( c _ { r } , j ) = { \bf o l d } \ d ( c _ { r } , j ) - 1$ until the case conservation constraint is satisfied.

2.2. If $\begin{array} { r } { \sum _ { j = 1 } ^ { q } d ( c _ { r } , j ) < \sum _ { j = 1 } ^ { q } s ( c _ { r } , L ( Z , X _ { k t } = x _ { k j } ) ) } \end{array}$ , then adjust by adding to some $\pmb { d } ( c _ { r } , j ) .$ Sort $\pmb { d ( c _ { n } , j ) }$ by ascending order of $\dot { ( d ( c _ { r } , j ) - e ( c _ { r } , j ) ) }$ ). Starting from the $\pmb { d ( c _ { n } , j ) }$ with the smallest difference, compute new $d ( c _ { n } j ) = \mathrm { o l d } \ d ( c _ { n } j ) + 1$ until the case conservation constraint is satisfied.

The procedures to assign the class and true state frequencies are optimal and polynomial in the number of states and classes. The procedures start with the best assignment (rounded estimated values) and adjust the best assignment until a feasible value is obtained. The adiustments are always the smallest deviation from the best assignment. Because there is no interaction among the decision variables, the resulting assignment minimizes the sum of squared deviations subject to case conservation constraints. The worst case complexity of the class frequency assignment algorithm is O(ma log(a)) for each input because there are m lists of decision variables where each list must be sorted (g log(g)). The operations of computing the rounded estimates and adjusting the estimates can be performed in time linear to the number of states. Similarly, the worst case complexity for the true state frequency assignment algorithm is O(mq2log(g)) because there are mq decision variables. The total worst case complexity is the sum of the above worst case complexities because the two procedures are independently performed.

The controlled scrambling procedure uses the algorithms to assign class and true state frequencies. After the class and true state frequency assignments are made, the controlled scrambling procedure randomly selects sets of cases from the true partitions and assigns them to scrambled partitions to satisfy the class and true state frequencies. In contrast, the random scrambling procedure assigns individual cases to scrambled partitions without the constraints of the class and true state frequencies. Formally, the algorithm to introduce noise in a controlled manner is presented in procedure Controlled Scrambling

TABLE 1  
Experimental Design

<table><tr><td rowspan="2">Algorithm</td><td colspan="3">Noise Level (C)</td></tr><tr><td>L (0.95)</td><td>M (0.80)</td><td>H (0.65)</td></tr><tr><td rowspan="2"> $ID3_p$ </td><td>100 (AVG)</td><td>100 (AVG)</td><td>100 (AVG)</td></tr><tr><td>30 (CV)</td><td>30 (CV)</td><td>30 (CV)</td></tr><tr><td rowspan="2"> $ID3_{ecp}$ </td><td>100 (AVG)</td><td>100 (AVG)</td><td>100 (AVG)</td></tr><tr><td>30 (CV)</td><td>30 (CV)</td><td>30 (CV)</td></tr></table>

## Procedure Controlled Scrambling

## Input

$z { \mathrm { : } }$ : a partition

$X _ { k }$ : branching input with q states

S: a ‘scrambled’ set of partitions of input X, ${ \cal S } = \{ { \cal S } _ { j } | { \cal S } _ { j }$ is partition of $s \}$ , j $\mathbf { \Omega } = 1 , 2 , \ldots , q .$

1. Perform procedure Assign Class Frequencies.

2. Perform procedure Assign True State Frequencies.

3. Let T' be the set of true partitions resulting from splitting Z into q partitions on input $X _ { k }$

${ T = \{ T _ { i } | T _ { i } } $ is a partition of T' where $X _ { k } = x _ { k i } \rangle$

4. For each $j = 1 , 2 , \ldots , q \mathrm { d } 0$

4.1. For each $i = 1 , 2 , \ldots , q$ do

4.1.1. For each $r = 1 , 2 , \ldots , m$ do

4.1.1.1. Define $\pmb { T } _ { i n }$ such that $\pmb { T _ { i r } }$ is a partition of $\pmb { T _ { i } }$ where the class is $\pmb { c _ { r } }$

4.1.1.2. Let $\pmb { S } _ { j r }$ be $d ( x _ { k i } , r , j )$ randomly selected cases without replacement from $T _ { i r } . S _ { j } = S _ { j } \cup S _ { j r }$

The explicit algorithm $\mathbf { I D 3 _ { e c p } }$ uses the controlled scrambling procedure to introduce noise into partitions. First, the usual partitioning process of the ID3 algorithm is performed. Second, the partitions created in the first step are scrambled using the controlled scrambling procedure. After all partitions of an input are scrambled, the normal formulas for the input selection, stopping rule, and classification function are used. Note that we retain the pessimistic pruning procedure in $\mathbf { I D 3 _ { e c p } } .$

## 4. Comparison of Algorithm Performance

In this section, we describe simulation experiments that investigate the performance of the implicit $( \mathbb { I D 3 } _ { \mathfrak { p } } )$ and explicit algorithms $( \mathbf { I D 3 _ { e c p } } )$ in terms of average accuracy and coefficient of variation (CV) of accuracy. We describe the hypotheses, performance measures, data sets, methodology, and results.

## 4.1. Hypotheses

The hypotheses extend the analytical results of $\ S 3$ to the performance of the implicit and explicit algorithms. Section 3 established several relationships between the implicit and explicit noise handling approaches: (i) same expected behavior on the gain, (ii) lower variance in the class frequency of a partition for a constant noise process than a binomial noise process, and (iii) difference in variance increases as noise level increases. Because it is difficult to analytically link the performance of the algorithms to the noise handling approach, simulation experiments are necessary. We feel that these three results will extend to the performance of the implicit and explicit algorithms as stated below.

TABLE 2  
AVG Lymphography ANOVA Results

<table><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td></tr><tr><td>NL</td><td>73785.8149</td><td>2</td><td>36892.9074</td><td>1265.98614</td><td>6.368E-215</td></tr><tr><td>ALG</td><td>39.7113688</td><td>1</td><td>39.7113688</td><td>1.3627021</td><td>0.24353811</td></tr><tr><td>NL*ALG</td><td>31.9080444</td><td>2</td><td>15.9540222</td><td>0.54746488</td><td>0.57870587</td></tr><tr><td>WITHIN</td><td>17310.1319</td><td>594</td><td>29.1416361</td><td></td><td></td></tr><tr><td>TOTAL</td><td>91167.5661</td><td>599</td><td></td><td></td><td></td></tr></table>

TABLE 3  
CV Lymphography ANOVA Results

<table><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td></tr><tr><td>NL</td><td>1.72273569</td><td>2</td><td>0.86136785</td><td>675.928939</td><td>9.1635E-83</td></tr><tr><td>ALG</td><td>0.52293785</td><td>1</td><td>0.52293785</td><td>410.357584</td><td>1.212E-47</td></tr><tr><td>NL*ALG</td><td>0.16348104</td><td>2</td><td>0.08174052</td><td>64.1430741</td><td>1.3533E-21</td></tr><tr><td>WITHIN</td><td>0.22173633</td><td>174</td><td>0.00127435</td><td></td><td></td></tr><tr><td>TOTAL</td><td>2.63089091</td><td>179</td><td></td><td></td><td></td></tr></table>

Hyporhesis 1. There is no difference in expected performance between the implicit algorithm $\mathbf { I D 3 _ { p } }$ and the explicit algorithm $\mathbf { I D 3 _ { e c p } } .$

HYPOTHESIS 2. The explicit algorithm $( \mathrm { I D } 3 _ { \infty ) } )$ has a smaller coefficient of variation in performance than the implicit algorithm $( \mathbf { I D 3 } _ { \mathsf { p } } )$

HypOTHEsis 3. The difference in the coefficient of variation in performance of the explicit algorithm $( \mathrm { I D } 3 _ { \mathrm { e c p } } )$ minus the implicit algorithm $( \mathbb { I D } 3 _ { \mathfrak { p } } )$ increases as the noise level increases over a range of reasonable noise levels.

## 4.2. Performance Measurement

We use two measures of performance: classification accuracy, a traditional measure and relative information score, a more refined measure. Classification accuracy (ratio of correctly classified cases to total cases) does not account for the effects of the number of classes and the prior probabilities of each class. The Relative Information Score (RIS) (Kononenko and Bratko 1991) measures the percentage of the uncertainty of the data set that is explained by the learning algorithm. Thus, a high RIS value is preferred to a low value. In Equation (19). RIS is computed as the amount $( \mathbf { i . e . } ,$ the number of bits) of uncertainty removed by the classification process (Ia) divided by the amount of uncertainty in the data set before classification (the entropy of the distribution E):

$$
\mathrm{RIS} = \frac {I _ {a}}{E} * 100 \%\tag{19}
$$

TABLE 4  
AVG GD1 ANOVA Results

<table><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td></tr><tr><td>NL</td><td>230805.371</td><td>2</td><td>115402.685</td><td>7855.76366</td><td>0</td></tr><tr><td>ALG</td><td>0.74741892</td><td>1</td><td>0.74741892</td><td>0.05087877</td><td>0.82161873</td></tr><tr><td>NL*ALG</td><td>4.5854718</td><td>2</td><td>2.2927359</td><td>0.15607255</td><td>0.85553219</td></tr><tr><td>WITHIN</td><td>8725.97472</td><td>594</td><td>14.6901931</td><td></td><td></td></tr><tr><td>TOTAL</td><td>239536.678</td><td>599</td><td></td><td></td><td></td></tr></table>

Mookerjee • Mannino • Gilson

<table><tr><td colspan="6">TABLE 5CV GD1 ANOVA Results</td></tr><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td></tr><tr><td>NL</td><td>0.26582049</td><td>2</td><td>0.13291025</td><td>520.574572</td><td>3.6729E-74</td></tr><tr><td>ALG</td><td>0.0891291</td><td>1</td><td>0.0891291</td><td>349.095311</td><td>1.9006E-43</td></tr><tr><td>NL*ALG</td><td>0.01144605</td><td>2</td><td>0.00572303</td><td>22.4155911</td><td>2.1791E-09</td></tr><tr><td>WITHIN</td><td>0.04442473</td><td>174</td><td>·0.00025531</td><td></td><td></td></tr><tr><td>TOTAL</td><td>0.41082037</td><td>179</td><td></td><td></td><td></td></tr></table>

where ${ \cal I } _ { a }$ is the Average Information Score computed as

$$
I _ {a} = \frac {1}{T} * \sum_ {1} ^ {n} I _ {j}
$$

where T'is the size of the test set and I is the information score of case j where $I _ { j }$

$$
I _ {j} = \left\{ \begin{array}{l l} - \log_ {2} P (C) & \text { if   a   correct   classification   is   made, } \\ \log_ {2} (1 - P (C)) & \text { if   an   incorrect   classification   is   made, } \end{array} \right.
$$

where P(C) is the prior probability of class C (determined from the data set)

## 4.3. Data Sets

To provide a range of case distributions, we executed the experiments with 5 data sets, 2 real and 3 artificially generated. The Bankruptcy data set (Liang 1992) contains 50 cases, 8 inputs, and 2 equally distributed classes (bankrupt or healthy). The Lymphography data set (Murphy and Aha 1991) was developed through data collection at the University Medical Centre, Institute of Oncology in Ljubljana, Yugoslavia. To reduce the effects of spurious noise, we removed cases with missing values, removed redundant cases, and removed all but one among conflicting cases. After this cleansing activity, the Lymphography data set contains 148 cases distributed among 4 classes where 2 classes are very sparse (2 and 4 cases, respectively). The Lymphography data set contains 18 inputs with an average of 3.3 states per input where the number of states ranges from 2 to 8.

The artificial data sets were generated by a program based on the specifications described in (Bisson 1991). The data set generator can control the number of cases, classes, inputs, states per input, the distribution of cases among classes, and the complexity of the true rule sets for each class. Data set 1 contains 4 equally distributed classes with 10 inputs. Data set 2 contains 8 moderately skewed classes and 15 inputs.

TABLE 6  
P Values for Other Data Sets

<table><tr><td rowspan="2"></td><td colspan="2">Bankruptcy</td><td colspan="2">GD2</td><td colspan="2">GD3</td></tr><tr><td>AVG</td><td>CV</td><td>AVG</td><td>CV</td><td>AVG</td><td>CV</td></tr><tr><td>NL</td><td>1.5053E-62</td><td>5.7346E-56</td><td>0.0000</td><td>2.3041E-95</td><td>0.0000</td><td>4.6106E-76</td></tr><tr><td>ALG</td><td>0.6006</td><td>2.2906E-68</td><td>0.8216</td><td>9.0516E-64</td><td>0.4669</td><td>2.5253E-39</td></tr><tr><td>NL*ALG</td><td>0.9231</td><td>1.7721E-33</td><td>0.8555</td><td>2.3986E-22</td><td>0.0225</td><td>3.0017E-18</td></tr></table>

<table><tr><td colspan="5">TABLE 7Lymphography CV Mean Differences</td></tr><tr><td></td><td>ID3p</td><td>ID3ecp</td><td>t-value</td><td>p-value</td></tr><tr><td>H</td><td>0.429047734</td><td>0.251359557</td><td>11.53771308</td><td>1.16936E-12</td></tr><tr><td>M</td><td>0.268555164</td><td>0.153436962</td><td>15.87069539</td><td>3.88396E-16</td></tr><tr><td>L</td><td>0.11611841</td><td>0.08552477</td><td>6.540714774</td><td>1.8278E-07</td></tr><tr><td>M-H</td><td>-0.160492571</td><td>-0.097922595</td><td>-3.638112396</td><td>0.000529124</td></tr><tr><td>L-M</td><td>-0.152436757</td><td>-0.067912194</td><td>-10.34340997</td><td>1.52555E-11</td></tr></table>

Data set 3 contains 12 highly skewed classes with 20 inputs. In data set 2, two classes have 50% of the cases and the remainder of the cases are uniformly distributed among the other 6 classes. In data set 3, 80% of the cases are distributed to 3 classes and the remainder are uniformly distributed to the other 9 classes. In the artificial data sets, the number of cases was 200, the average number of states per input was 3, and the average size of the true rule sets was 2 rules per class and 3 conjunctive terms per rule.

## 4.4. Experimental Design

Table 1 shows a $\mathbf { 2 } \times \mathbf { 3 }$ factorial design for the algorithm³ and noise level factors. The numbers in the cells show the observations for each treatment. As shown in Table 1, we choose 3 levels of noise: high $( C = 0 . 6 5 )$ , moderate $( C = 0 . 8 0 )$ , and low $( C = 0 . 9 5 )$ . The low level of noise is close to perfect measurement. The moderate level of noise causes a significant decrease in predictive performance. The high noise level causes a further significant decrease in predictive performance. Further decline in predictive performance from higher levels of noise is not as significant. In separate experiments, the entire range of noise levels is studied to graphically depict the functional relationship between noise and the mean and variance of performance.

There are two experiments corresponding to the dependent variable average RIS and coefficient of variation (CV) of RIS. The method used to estimate performance is the standard test-sample method (Breiman et al. 1984). Each observation is the average performance of the same 30 splits of a data set where the data set is divided roughly 70% for training and 30% for testing. Each cell of both experiments uses the same set of 100 noise perturbations. In a perturbation, the data set is randomly changed using the given C and W values. $\mathbf { I D 3 _ { p } }$ is given a perturbed training set while

TABLE 8  
GD1 CV Mean Differences

<table><tr><td></td><td>ID3p</td><td>ID3ecp</td><td>t-value</td><td>p-value</td></tr><tr><td>H</td><td>0.1812388</td><td>0.1180832</td><td>11.717007</td><td>8.071E-13</td></tr><tr><td>M</td><td>0.1197556</td><td>0.0735932</td><td>16.073779</td><td>2.786E-16</td></tr><tr><td>L</td><td>0.0678872</td><td>0.043692</td><td>13.31519161</td><td>3.47781E-14</td></tr><tr><td>M-H</td><td>-0.061483251</td><td>-0.044490058</td><td>-2.464027269</td><td>0.009954073</td></tr><tr><td>L-M</td><td>-0.051868367</td><td>-0.029901399</td><td>-6.473220833</td><td>2.19337E-07</td></tr></table>

The algorithms and simulation experiment were implemented using Microsoft C on a 486 personal computer.

Generated Data Set 1 - Average Performance (RIS)  
![](/api/attachments/DC5X39GC/fulltext/images/8434bd1c9cf04cac38719ff9acbe70a1ea914989f56dce5ab9de074f650f73fc.jpg)  
Generated Data Set 1 - Variance of Performance (RIS)

![](/api/attachments/DC5X39GC/fulltext/images/dd048e070d4adc6751854a0104e679024d7cd9ec5e40e651b2ea81c5d136a59d.jpg)  
FIGURE 4. RIS Performance Graphs for Generated Data Set 1.

$\mathbf { I D 3 _ { e c p } }$ is given a clean training set. Both algorithms use the same test set and the same perturbed training set in the pessimistic pruning procedure. In the average experiment, all observations are used. In the CV experiment, each cell contains the same 30 random samples6 of size 30 from the 100 observations. An observation is the CV computed from the given sample.

## 4.5. Results

Analysis of variance was used to determine whether there are performance differences between the algorithms across the 5 data sets. Tables 2–5 report the analysis of variance results for the Lymphography data set and data set 1 (GD1). The ANOVA tables show that the simulation results are consistent with the theoretical analysis in §3. The noise level (NL) affects both dependent variables (AVG RIS and CV RIS), but the algorithm (ALG) and the interaction term (NL  ALG) are not significant for AVG RIS (Tables 2 and 4). However, ALG and the interaction term are significant for CV RIS (Tables 3 and 5). Thus, the ANOVA results confirm Hypothesis 1 and support Hypotheses 2 and 3. Similar results were obtained for the other data sets (see Table 6).

Generated Data Set 1 - Average Performance (Accuracy)  
![](/api/attachments/DC5X39GC/fulltext/images/25c98cd342d19596af835f098dda361f832807f5a2ceec02f3481c8033b094bf.jpg)  
Generated Data Set 1 - Variance of Performance (Accuracy)

![](/api/attachments/DC5X39GC/fulltext/images/5e5fb2d6e1191add49631b0847dabe75f23924efd46bad37a61eaca33c21e903.jpg)  
FIGURE 5. Accuracy Performance Graphs for Generated Data Set 1.

Tables 7 and 8 list mean CV differences between the algorithms (first-order differences) at each noise level and mean differences between the algorithms at adjacent noise levels (second-order differences). Because both the first-order and second-order differences are significant, Hypotheses 2 and 3 are confirmed

## 4.6. Discussion

To depict the magnitudes of the differences in performance, we generated simulation data to graphically compare the performances. In a simulation run, each observation was computed from the same 20 splits and 20 perturbations. In Figures 4 and

Lymphography Data Set - Average Performance (RIS)  
![](/api/attachments/DC5X39GC/fulltext/images/aab45a2fc96075435d36b9b9f31b1090ffec5ecbd721a38dc0fa3289bd735977.jpg)  
Lymphógraphy Data Set - Variance of Performance (RIS)

![](/api/attachments/DC5X39GC/fulltext/images/14c8baef40b8c90b2da1f05497b7dc2a7bed1c67e261eabe00593248503ff4a6.jpg)  
FIGURE 6. RIS Performance Graphs for the Lymphography Data Set.

5, the average performance graphs of GD1 almost coincide as expected. In Figures 6 and 7, the average performance graphs for the Lymphography data set are more erratic as the graphs cross numerous times. This slightly erratic behavior is probably due to the increased level of residual variation in the Lymphography data set as its maximum RIS is slightly less than 50% compared to more than 80% for GD1. The shape of the average performance graphs provides evidence to support Proposition 1 in §3.2. Note that the average RIS and accuracy is minimized near 1/q and the bowllike shape of the curves. For GD1, the average number of states is just below 3. For the Lymphography data set, the average number of states is 3.3 and there is a larger variation in the number of states (2 of the inputs have 8 states). Because ID3 favors inputs with many states, the inputs with 8 states probably appear on most paths in the decision tree. This explains why the Lymphography graph is minimized below the simple average number of states from the data set.

As for the CV of performance, Figures 4 through 7 show a strong separation between the implicit and explicit algorithms. In addition, the CV of performance increases as noise increases and the difference between the explicit and implicit algorithms increases as the noise level increases. The shape of the curves and their extreme point is consistent with the theoretical graphs shown in Figure 3. There is larger separation between the explicit and implicit graphs in the Lymphography data set (Figures 6 and 7) than in the GD1 (Figure 4 and 5). The difference at low levels of noise is obscured in Figures 6 and 7 because the scale is wider. However, the difference between the plotted points is larger for the Lymphography data set than GD1 even at low levels of noise. Note also that the shape of the CV graphs in Figures 6 and 7 differ because the CV RIS graph (Figure 6) is affected by some negative RIS values.

Lymphography Data Set - Average Performance (Accuracy)  
![](/api/attachments/DC5X39GC/fulltext/images/fa749fae77304b6a0b8be5681ef8daa7efdf0606cb7308b4d25fd3fd68c49093.jpg)  
Lymphography Data Set - Variance of Performance (Accuracy)

![](/api/attachments/DC5X39GC/fulltext/images/60d8f07d0f0bef160dfb51cb95cb853c2f24d942343a5fc2af49eaed0f84b0bc.jpg)  
FiGURE 7. Performance Graphs (Accuracy) for the Lymphography Data Set.

To probe the sensitivity of $\mathbf { I D 3 _ { e c p } } ,$ we generated additional simulation data for GD1. Here, the true noise level (C) used in the test set and in the training set of $\mathbf { I D 3 _ { p } }$ differed from the false noise parameters given to $\mathbf { I D } 3 _ { \mathrm { e c p } } ( C ^ { \prime } )$ . In the constant error sensitivity runs, the false noise parameter $C ^ { \prime }$ was misstated by 0.10 (either all high or all low in a run) except near the end points $( C = 0 \ \mathbf { o r } \ 1 )$ . In varying error sensitivity runs, the mean of the false noise level $C ^ { \prime }$ was equal to the true noise level C but variance in a range o $\mathbf { f } \pm 0 . 1 0 \ \mathbf { o r } \pm 0 . 0 5$ of the true $c$ value was introduced. Somewhat surprisingly, the average performance of the algorithms in each sensitivity run shows little difference than in Figure 4. In Figure $\mathfrak { 8 } ,$ the CV of performance continues to demonstrate a large advantage for $\mathbf { I D } 3 _ { \mathsf { e c p } }$ for both constant error runs (high and low). In Figure 9, the CV advantage of $\mathbf { I D 3 _ { e c p } }$ has disappeared at high values of C in the ±0.10 case. In the ±0.05 case, however, there is still a marked advantage for $\mathbf { I D 3 _ { e c p } } .$ Figure 9 demonstrates that CV of performance of $\mathbf { I D 3 _ { e c p } }$ is relatively sensitive to accurate noise level assessments as compared to an implicit algorithm using a training set drawn from the same noise process as unseen cases. Thus, the stable behavior of explicit algorithms may deteriorate due to the variance caused by incorrect specification of the noise level. When the variance in incorrect specification is high, the noise variance acting on implicit algorithms may be balanced by the incorrect specification variance acting on explicit algorithms.

ID3ecp Sensitivity in Generated Data Set 1 - Constant Low (-0.1)  
![](/api/attachments/DC5X39GC/fulltext/images/1152f4703958bda7d6a025b8f06dfd61597a085a89913bc213fb82d2c9663771.jpg)  
ID3ecp Sensitivity in Generated Data Set 1 - Constant High (+0.1)

![](/api/attachments/DC5X39GC/fulltext/images/29e0b4dd8f877a7458634b68f7fe9b8970db20db0e658dd5959656ac51532cc6.jpg)  
FIGURE 8. Constant Sensitivity Graphs for Generated Data Set 1.

ID3ecp Sensitivity in Generated Data Set 1 - Varying [-0.1, +0.1]  
![](/api/attachments/DC5X39GC/fulltext/images/a6e2fa4f09f46777ff10b174300738f6fbe6c1ecfa3112d8d4be4acf858f2b03.jpg)  
ID3ecp Sensitivity in Generated Data Set 1 - Varying [-0.05, +0.05]

![](/api/attachments/DC5X39GC/fulltext/images/f5539221896596a3469aa44b1241df7c864a39dee9797f447a1701a344cb09eb.jpg)  
FIGURE 9. Varying Sensitivity Graphs for Generated Data Set 1.

## 5. Summary and Conclusions

We compared decision tree induction algorithms under conditions of noisy input data where the level of noise was either implicitly known through a sample of the noise process or explicitly known through an external parameter. Explicit measurement of noise is cost effective when training data is provided directly by experts or when the cost of directly estimating the level of noise is less than the cost of sampling a representative noisy process. In addition, the appeal of explicit noise measurement broadens when there is an associated performance benefit. Here, we demonstrated that explicit noise measurement can be accompanied by more stable performance on unseen cases.

Our primary contributions were to develop an explicit noise handling algorithm $( \mathrm { I D } 3 _ { \mathrm { e c p } } )$ and demonstrate its advantages as compared to a standard implicit noise algorithm (ID3 with the pessimistic pruning procedure). $\mathbf { I D 3 _ { e c p } }$ injects random noise into partitions but controls the class and true state frequencies in a partition as close as possible to their estimated values. The aim of the controlled scrambling procedure is to reduce the variance in the partitioning behavior. We demonstrated that the implicit and explicit algorithms have the same expected behavior and performance, but the explicit algorithm has more stable behavior and performance. The behavioral results were demonstrated by an analytical comparison of a constant noise process as the best case for a controlled partitioning process and a binomial noise process for implicit noise measurement. The performance of the algorithms was demonstrated by simulation experiments to compare the average performance and coefficient of variation of performance for the two algorithms.

This research is part of our long term interest concerning the economics of expert systems. Two direct extensions of this work are treating the noise level as a decision variable rather than a constraint and developing induction algorithms that combine mean and variance of performance. In the former topic, explicit measurement of noise is required to make a tradeoff among the cost of removing noise with the benefit of improved decision making. Other topics not directly related to this work are optimizing expert system performance over a multiperiod horizon and developing costbenefit objectives for other approaches such as Bayesian reasoning networks.\*

\* Michael J. Shaw, Associate Editor. This paper was received on March 21, 1994, and has been with the authors 2 months for 2 revisions.

Appendix A: Convexity of Gain with Respect to Noise Level

PROPOSITION 1.

$$
\frac {\partial g (\tilde {X} _ {k o} | \tilde {Z} ^ {C})}{\partial C} > 0, \quad C \in (1 / q, 1 ],\tag{6.1}
$$

$$
= 0, \quad C = 1 / q,\tag{6.2}
$$

$$
<   0, \quad C \in [ 0, 1 / q).\tag{6.3}
$$

We prove (6.2) and demonstrate the truth of (6.1) and (6.3) for a special case. Let us begin by showing the second condition, namely, the slope is zero at $C = 1 / q .$ , With some alġebra, first derivative of the gain function with respect to $C ( \mathsf { A l } )$ can be derived:

$$
\frac {\partial g \left(\tilde {X} _ {k o} \mid \tilde {Z} ^ {C}\right)}{\partial C} = \frac {1}{q - 1} \sum_ {r = 1} ^ {m} \sum_ {j = 1} ^ {q} \left(q p _ {j} p _ {r j} - p _ {r}\right) \log_ {2} \left(\frac {p _ {r} + \alpha \left(q p _ {j} p _ {r j} - p _ {r}\right)}{1 + \alpha \left(q p _ {j} - 1\right)}\right) \quad \text {where}
$$

$$
p _ {j} = P \left(\tilde {X} _ {k a} = x _ {k j} \mid \tilde {Z} ^ {C}\right), \quad p _ {r} = P \left(\tilde {\psi} = c _ {r} \mid \tilde {Z} ^ {C}\right), \quad p _ {r j} = P \left(\tilde {\psi} = c _ {r} \mid \tilde {Z} ^ {C} \wedge \tilde {X} _ {k a} = x _ {k j}\right), \quad \alpha = (1 - W q).\tag{A1}
$$

For $C = 1 / q , \alpha = 0$ .Substituting ${ \pmb { \alpha } } = { \pmb { 0 } }$ in the above equation for the slope we obtain:

$$
\frac {\partial g \left(\tilde {X} _ {k o} \mid \tilde {Z} ^ {C}\right)}{\partial C} = \frac {1}{1 - q} \sum_ {r = 1} ^ {m} \log_ {2} \left(p _ {r}\right) \sum_ {j = 1} ^ {q} \left(q p _ {j} p _ {r j} - p _ {r}\right) = 0 \quad \text { as } \sum_ {j = 1} ^ {q} \left(q p _ {j} p _ {r j} - p _ {r}\right) = q p _ {r} - q p _ {r} = 0.
$$

The second condition in the proposition is proved.

For (6.1) and (6.3), we show that the second derivative is greater than zero in a special case. With some algebra, the second derivative of the gain with respect to W can be derived as (A2). We must show that the second derivative is greater than 0 as stated in (A3).

$$
\begin{array}{r l} \frac {\partial^ {2} g (\tilde {X} _ {k o} | \tilde {Z} ^ {C})}{\partial^ {2} W} & = - \sum_ {j = 1} ^ {q} \sum_ {r = 1} ^ {m} \frac {\delta_ {r j} (p _ {r} + q \delta_ {r j})}{W p _ {r} + (1 - W q) \delta_ {r j}} + \sum_ {j = 1} ^ {q} \frac {\delta_ {j} (1 - q \delta_ {j})}{W + (1 - W q) \delta_ {j}} \\ & W = \frac {1 - C}{q - 1}, \quad \delta_ {r j} = q p _ {j} p _ {r j} - p _ {r}, \quad \dot {\delta} _ {j} = q p _ {j} - 1, \end{array} \quad \text { where }\tag{A2}
$$

$$
\sum_ {j = 1} ^ {q} \frac {\delta_ {j} (1 - q \delta_ {j})}{W + (1 - W q) \delta_ {j}} > \sum_ {j = 1} ^ {q} \sum_ {r = 1} ^ {m} \frac {\delta_ {r j} (p _ {r} + q \delta_ {r j})}{W p _ {r} + (1 - W q) \delta_ {r j}}.\tag{A3}
$$

Because $\begin{array} { r } { \sum _ { r } \delta _ { p j } = \delta _ { j } , } \end{array}$ we assume that one of the $\delta _ { \pmb { \eta } }$ terms equals $\delta _ { j }$ and the other $m - 1$ terms be divided into pairs such that the sum of each pair is zero and each pair member is the same absolute value. In addition, we assume that ${ p } _ { r } ( = \mu )$ is constant for all r. Using these assumptions and some algebra, the righthand side $\pmb { \mathfrak { o f } } ( \pmb { \mathbb { A } } 3 )$ can be reduced to a quantity less than (A4).

$$
\sum_ {j = 1} ^ {q} \frac {\delta_ {j} (\mu - q \delta_ {j})}{W \mu + (1 - W q) \delta_ {j}}.\tag{A4}
$$

Substituting (A4) into (A3) and using some further algebra, (A3) can be reduced to (A5):

$$
\sum_ {j = 1} ^ {q} \frac {\delta_ {j} ^ {2}}{D} > \sum_ {j = 1} ^ {q} \frac {\delta_ {j} ^ {2} \mu}{D} \quad \text { where } \quad D = (W \mu + (1 - W q) \delta_ {j}) (W + (1 - W q) \delta_ {j}).\tag{A5}
$$

(A5) is true because $\delta _ { j } ^ { 2 } > 0$ and $\mu < 1$ and $\mathbf { \nabla } \pmb { D } > \mathbf { 0 } ,$ This proves (6.1) and (6.3) for the special case stated above. □

## Appendix B: Pessimistic Pruning Procedure

Appendix B describes the pruning procedure used in the algorithms $\mathbf { I D 3 } _ { \mathfrak { p } }$ and $\scriptstyle \mathbf { I D 3 _ { e c p } }$ This description has been adapted from (Quinlan 1987)

For any given tree $^ { T , }$ generated using a training set of N cases, let some leaf in the tree account for K of these cases with J of them misclassified. The ratio J/K does not provide a reasonable estimate of the error rate when classifying unseen cases (Quinlan 1987). A more reasonable estimate is obtained using the continuity correction factor for the binomial distribution, wherein J is replaced by $\mathbf { \widetilde { J } } + \mathbf { 0 . 5 }$ (Snedecor and Cochran 1980).

Let S be a subtree of T with $\pmb { L } _ { \pmb { S } }$ leaves, and let $J _ { s }$ and $\pmb { K } _ { S }$ be the corresponding sums of errors and cases classified over S. Using the continuity correction factor, the expected number of cases $( M s )$ misclassified by $\pmb { S }$ out of $\pmb { K } _ { \pmb { S } }$ unseen cases should be $M _ { S } = J _ { S } + 0 . 5 L _ { S } .$ The standard error of $M _ { S } , S e ( M _ { S } )$ , is given by

$$
\operatorname{Se} (M _ {S}) = \sqrt {\frac {M _ {S} * (K _ {S} - M _ {S})}{K _ {S}}}.
$$

Let E be the number of cases misclassified out of $K _ { S }$ if the subtree S is replaced by its best leaf. The pessimistic pruning procedure replaces S by its best leaf if $E + 0 . 5 \leq M _ { S } + \mathrm { S e } ( M _ { S } )$

In pessimistic pruning, all nonleaf subtrees are examined only once and subtrees of pruned subtrees need not be examined at all.

## References

Biemer, P. and L. Stokes, "Approaches to the Modeling of Measurement Error," in Measurement Errors in Surveys, Chapter 24, P. Biemer, R. Groves, L. Lyberg, N. Mathiowetz, and S. Sudman, (Eds.), John Wiley & Sons, New York, 1991, 487–516.

Bisson, H., “Evaluation of Learning Systems: An Artificial Data-Based Approach," in Proceedings of the European Working Session on Machine Learning, Y. Kodratoff (Ed.), Springer-Verlag, Berlin, 1991.

Breiman, L., J. Friedman, R. Olshen, and C. Stone, Classification and Regression Trees, Wadsworth Publishing, Belmont, CA, 1984.

Cestnik, B. and I. Bratko, "On Estimating Probabilities in Tree Pruning," in Proceedings of the European Working Session on Machine Learning, Porto, Portugal, Springer-Verlag, March 1991, 138-150.

Christie, A., "Induction of Decision Trees from Noisy Examples,"AI Expert, May (1993), 16–21.

Creecy, R., B. Masand, S. Smith, and D. Waltz, "Trading MIPS and Memory of Knowledge Engineering," Communications of the ACM, 35, 8 (August 1992), 48–64.

Fuller, W., “Regression Estimation in the Presence of Measurement Error," in Measurement Errors in Surveys, Chapter 30, P. Biemer, R. Groves, L. Lyberg, N. Mathiowetz, and S. Sudman, (Eds.), John Wiley & Sons, New York, 1991, 617–636.

Groves, R., "Measurement Error Açross Disciplines," in Measurement Errors in Surveys, Chapter 1, P. Biemer, R. Groves, L. Lyberg, N. Mathiowetz, and S. Sudman, (Eds.), John Wiley & Sons, New York, 1991, 1–28.

Hill, D., “Interviewer, Respondent, and Regional Office Effects," in Measurement Errors in Surveys, Chapter 23, P. Biemer, R. Groves, L. Lyberg, N. Mathiowetz, and S. Sudman, (Eds.), John Wiley & Sons, New York, 1991, 463–486

Holsapple, C. and A. Whinston, Business Expert Systems, Irwin, Homewood, IL, 1987.

Irani, K., J. Cheng, U. Fayyad, and Z. Qian, "Applying Machine Learning to Semiconductor Manufacturing," IEEE Expert, 8, 1 (February 1993), 41–47.

Kononenko, I. and I. Bratko, "Information-Based Evaluation Criterion for Classifier's Performance," Machine Learning, 6 (1991), 67–80

Laird, P., Learning from Good and Bad Data, Kluwer Academic Publishers, Norwell, MA, 1988.

Liang, T., “A Composite Approach to Inducing Knowledge for Expert System Design," Management Science, 38, 1 (1992), 1–17.

Mantaras, R., “A Distance-Based Attribute Selection Measure for Decision Tree Induction," Machine Learning, 6 (1991), 81–92

Mingers, J., “An Empirical Comparison of Pruning Methods for Decision Tree Induction," Machine Learning, 4, 2 (1989), 227–243.

Mookerjee, V. and B. Dos Santos, "Inductive Expert System Design: Maximizing System Value," Information Systems Research, 4, 2 (1993), 111–140.

Moulet, M., "Using Accuracy in Scientific Discovery," in Proceedings of the European Working Session on Machine Learning, Porto, Portugal, Springer-Verlag, March 1991, 118–136.

Murphy, P. and D. Aha, UCI Repository of Machine Learning Databases, Department ofInformation and Computer Science, University of California, Irvine, CA, 1991.

Niblett, T. and I. Bratko, "Learning Decision Rules in Noisy Domains," in “Research and Development in Expert Systems," Proceedings of the Sixth Technical Conference of the BCS Specialist Group on Expert Systems, Brighton, UK, 1986.

Pearl, J., Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Morgan Kauffman Publishers, San Mateo, CA, 1988.

Quinlan, J., "Induction of Decision Trees," Machine Learning, 1 (1986a), 81–106

, "The Effect of Noise on Concept Learning," Machine Learning, Vol. 2, R. Michalski, J. Carbonnell, and T. Mitchel, (Eds.), Tioga Press, Palo Alto, CA, 1986b, 149–166.

, "Simplifying Decision Trees," International Journal of Man Machine Studies, 27 (1987), 221– 234.

Rao, J. and R. Thomas, “Chi-Squared Tests with Complex Survey Data Subject to Misclassification Error," in Measurement Errors in Surveys, Chapter 31, P. Biemer, R. Groves, L. Lyberg, N. Mathiowetz, and S. Sudman, (Eds.), John Wiley & Sons, New York, 1991, 637–664.

Ross, S., Applied Probability Models, Holden-Day, San Francisco, CA, 1970.

Shannon, C. and W. Weaver, The Mathematical Theory of Communication, University of Illinois Press, Urbana, IL, 1949.

Snedecor, G. and W. Cochran, Statistical Methods, 7th edition, Iowa State University Press, Ames, IA, 1980.

Tam, K. and M. Kiang, "Predicting Bank Failures: A Neural Network Approach," Applied Artificial Intelligence, 4 (1990), 265–282.
