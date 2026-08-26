---
otero_id: 9938
otero_key: "WJZSJAR6"
title: "Setting priorities for data accuracy improvements in satisficing decision-making scenarios: A guiding theory"
authors: "Irit Askira Gelman"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.11.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Setting priorities for data accuracy improvements in satis<sup>fi</sup>cing decision-making scenarios: A guiding theory

Irit Askira Gelman

University of Arizona, Tucson 85716, United States

## a r t i c l e i n f o

Article history: Received 2 November 2007 Received in revised form 2 September 2009 Accepted 2 November 2009 Available online 17 November 2009

Keywords: Satis<sup>fi</sup>cing decisions Multi-criteria decisions Information accuracy Data quality management Resource allocation Mathematical-statistical model

## a b s t r a c t

This study introduces a mathematical–statistical theory that illustrates the effect of input errors on the accuracy of dichotomous decisions which are implemented through logical conjunction and disjunction of selected criteria. Decision-making instances in this category are often labeled “satis<sup>fi</sup>cing.” Mainly, our theory provides criteria for ranking the effect of errors in different inputs on decision accuracy. This ranking can be used to improve the ef<sup>fi</sup>ciency and effectiveness of resource allocation decisions in data quality management settings. All other things being equal, inputs in which errors exhibit a higher negative effect on the output would naturally earn higher priority.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

The relationship between data accuracy and the resulting information accuracy is of great interest in numerous problem domains. This relationship has been investigated in many research <sup>fi</sup>elds, assuming various information-processing models and data and error characteristics, as well as an assortment of accuracy measures. Some of these research <sup>fi</sup>elds are statistics, computer science, the physical sciences, political science, decision sciences, econometric forecasting, accounting, and information systems (e.g., [2–5,7–9,11–18,23–25,29–32,36– 38,43,44,49,52,55]). An understanding of the relationship between input accuracy and output accuracy can improve the ef<sup>fi</sup>ciency of data management and increase the accuracy and utility of information in problem-solving settings. Nonetheless, our understanding of that relationship is still partial.

This work adds to the literature about the association between input accuracy and output accuracy. An underlying observation that motivates this study originates in models that track error propagation. Such models have been introduced in the statistics literature and elsewhere (e.g., [14,24]) and have proven to be useful in many areas. In Management Information Systems (MIS), in particular, there are various frameworks that have been developed for tracking data errors and other data quality determinants through an information system (e.g., [7,11,49]). These models imply that, for any given application, the effect of input errors on output accuracy varies in magnitude, depending on the choice of the speci<sup>fi</sup>c input. While errors in one input may have a dramatic effect on output accuracy, a comparable, or even higher, error rate in another input can have a negligible effect. It has been shown that the severity of the effect of errors is in<sup>fl</sup>uenced by the nature of the manipulations that the data undergo [8]. Notably, characterization of this variation can be useful since it can guide resource allocation decisions in data quality management settings. All other things being equal, inputs in which errors exhibit a higher negative effect on the output would naturally earn higher priority.

Accordingly, this analytical inquiry sheds light on the variation in the effect of input errors on output accuracy in a popular class of applications. These applications consist of dichotomous decisions which are implemented through logical conjunction and disjunction of selected criteria. Decision-making instances in this category are often labeled “satis<sup>fi</sup>cing.” The term “satis<sup>fi</sup>cing” was coined by Herbert Simon to denote problem-solving and decision-making that aims at satisfying a chosen aspiration level instead of an optimal solution [50]. Research indicates that conjunctive and disjunctive rules agree with human choices and inferences in diverse situations involving complex problems, severe time constraints, or lack of information. Evidence in this direction has been found in consumer choice settings, medical diagnosis, job preference decisions, university admission decisions, residential rental searches, political leaders' decision-making, and in many other domains (e.g., [19–21,34,35,41,45,46]).

Consider, for example, a company decision regarding the rental of a new of<sup>fi</sup>ce. Suppose that a satis<sup>fi</sup>cing decision strategy is employed throughout the entire selection process, or else, due to the high number of alternatives, for the initial screening of alternatives (e.g., [34,45]). Suppose that <sup>fi</sup>ve of the major decision variables are rental rate, square footage, age of the of<sup>fi</sup>ce building, availability of parking spaces, and distance from a public transportation hub ([40],[51]). In particular, the decision rule that combines these variables is the following: the age of the of<sup>fi</sup>ce building must not exceed ten years and the desired of<sup>fi</sup>ce space should be in the range of $3 5 0 0 { - } 5 0 0 0 \mathrm { f t } ^ { 2 }$ and the monthly rental rate should be \$10,000 at most, and, in addition, the of<sup>fi</sup>ce building should have its own covered parking or the building must be located within a half of a mile from a public transportation hub (see Fig. 1). This decision rule can be implemented as follows: The values of each variable are tested against the matching criterion, namely, a subset of the value domain of the variable (i.e., the rental rate of each of the properties in the local commercial rentals database is tested against \$10,000, the age of each property is tested against 10, and so on). These tests determine the values of corresponding dichotomous variables $( \mathrm { e . g . } ,$ , a test of a rental rate of \$7500 would produce the value “true” and a test of a rate of \$12,500 would produce the value “false”). Next, the values of the different dichotomous variables which are determined in this way are combined using a suitable sequence of conjunction and disjunction operations to produce the outcome of the decision. The outcome can be either positive or negative (e.g., a rental property that satis<sup>fi</sup>es the entire decision rule would result in a positive decision).

Our inquiry centers on multi-criteria, satis<sup>fi</sup>cing decisions like this of<sup>fi</sup>ce rental decision. Mainly, we examine the effect of errors in the classi<sup>fi</sup>cation of data values as ful<sup>fi</sup>lling or not ful<sup>fi</sup>lling a relevant decision criterion on the accuracy of the decision. In other words, we study the effects of errors in the individual dichotomous variables portrayed above on the accuracy of the decision. A decision error is registered whenever a decision based on the available inputs deviates from the outcome of the same decision based on error-free inputs. A decision error can be a Type 1 error (false positive), e.g., when an of<sup>fi</sup>ce that does not satisfy the criteria is included in the short list of suitable properties, or it can be a Type 2 error (false negative), e.g., when an of<sup>fi</sup>ce that has the desired attributes is excluded from that list. Assuming this interpretation of the notion of a decision error, decision accuracy will be measured by decision error probability. Speci<sup>fi</sup>cally, this work offers tools for ranking the damage that the above described input classi<sup>fi</sup>cation errors in<sup>fl</sup>ict on decision accuracy. Our study de<sup>fi</sup>nes the notion of damage and produces guidelines for ranking the damage. These guidelines can be used for improving the ef<sup>fi</sup>ciency and effectiveness of resource allocation decisions in data quality management settings. The guidelines would be most useful when the major application that processes the data is equivalent to a set of satis<sup>fi</sup>cing decision rules. For instance, the company that plans to rent a new of<sup>fi</sup>ce can bene<sup>fi</sup>t from our theory to the extent that management has in<sup>fl</sup>uence over the accuracy of the data that they are using. Alternatively, the providers of those data can bene<sup>fi</sup>t from information about the average damage that errors in each input induce on the entire collection of decisions that use those data. All other things being equal, inputs (e.g., database attributes) in which errors exhibit a higher damage would naturally earn higher priority.

![](/api/attachments/WJZSJAR6/fulltext/images/488332477a87abe03d53c68d067a2447fbde7448c127c4c6829e95874f4027ae.jpg)  
Fig. 1. A satis<sup>fi</sup>cing of<sup>fi</sup>ce rental selection strategy.

This paper is organized as follows. A review of related literature is given in Section 2. It is followed in Section 3 by a description of the basic research models, which designate a single binary conjunction operation and a single binary disjunction operation and formulate the damage for these operations. We then de<sup>fi</sup>ne the notion of error dominance and apply this notion for characterizing conditions in which the damage of errors in one input is greater than the damage caused by errors in a second input (Section 4). An illustration of the former conditions, which exploits the example of the of<sup>fi</sup>ce rental decision, is provided in Section 5. An extension of the theory to a sequence of binary operations is presented in Section 6. The paper is concluded with a discussion of the implications of the theory to data quality management, limitations of this research, and future research directions.

## 2. Literature review

Research on the relationship between input accuracy and output accuracy has a long history. In particular, the classic Jury Theorem [16], which is viewed as theoretical support for group decisionmaking and democracy, dates back to the late eighteenth century. Condorcet's Jury Theorem asserts that if group members are independent, and if each member judges correctly between a pair of alternatives with probability $p { > } 0 . 5$ , and if members' judgments are combined using a majority vote rule, then the probability that the output is correct, $P _ { n } ,$ is higher than $p \ ( P _ { n } { > } p )$ . Furthermore, group accuracy approaches perfection as the number of members, n, grows to in<sup>fi</sup>nity $( P _ { n } \to 1 \ \mathsf { a s } \ n \to \infty )$ .

The literature on the relationship between input accuracy and output accuracy is vast. This relationship has been investigated in countless problem domains. Some of these problem domains are group accuracy (e.g., [16,25,32]), error propagation (e.g., [14]), feature selection (e.g., [13,17,23]), expert resolution (e.g., [15]), internal accounting control (e.g., [18,55]), multisensor fusion, and ensemble learning (e.g., [31]). In MIS, the problem of the relationship between an information system's input quality and its output quality has received considerable attention in the Data Quality (DQ) literature. For the most part, research has maintained a methodological nature. Ballou and Pazer [7] proposed a framework for tracking numeric data errors through an information system, to assist with estimates of the impact of errors on the output. Ballou et al.[11] have applied and extended the model of Ballou and Pazer to other data quality dimensions. The extended model, which may be viewed as an extension of a Data Flow Diagram (DFD) [11], has been called the Information Manufacturing Model (IMM). It can be used to analyze an information system and assess various design alternatives from a data quality standpoint. Ballou et al.'s IMM has been augmented through the Information Product Map (IPMAP) model [49] and subsequent enhancements of the IPMAP model. Research in this stream has initially drawn on inquiries in the accounting literature that offer decision aids for internal control evaluation based on mathematical modeling or simulations (e.g., [18,52,55]).

Various frameworks for assessing the relationship between the quality of the raw data and the quality of query outputs have been proposed in the context of relational database research. These frameworks have sometimes been labeled data quality algebra. The relationship between the accuracy of the data and the accuracy of the output of a database query has been studied by Reddy and Wang [54]. Naumann et al. [38] explore the problem of merging multiple source responses. They show how to determine the completeness of both single and combined responses. Additional instances of frameworks as above include [48], which studies completeness; [43] and [44] investigate completeness and accuracy, and [12] targets a broader set of data quality dimensions. Other relevant studies are [36] and [5].

A scenario that is partly compatible with this work has been addressed by Ballou and Pazer [9], who proposed a framework for assessing the effect of input errors on the accuracy of dichotomous, conjunctive decisions. They found, using a set of numeric examples, that “As the decision maker becomes more selective, the probability that his/her acceptance decisions will be correct decreases substantially.” Although Ballou and Pazer have reacted to this <sup>fi</sup>nding by saying that it “borders on the perverse,” the results of our research are consistent with, and generalize, their <sup>fi</sup>nding.

Of special signi<sup>fi</sup>cance to this work are commonly accepted error propagation models that estimate the uncertainty in the output of a function based on the standard deviations of the individual inputs (e.g. [14,24]). Also relevant are various models that have been developed by DQ research in MIS, such as Ballou et al.'s IMM and related models mentioned above. These models imply that, for any given application, the effect of input errors on output accuracy generally varies in magnitude depending on the choice of the speci<sup>fi</sup>c input.

An implicit assumption of this research is that data quality resource allocation decisions take into account the intended use of the data. Contrary to an approach that does not differentiate between errors $( \mathrm { e . g . , } [ 2 7 , 4 2 ] )$ , an approach that differentiates between errors based on the intended use of the data is consistent with the currently accepted de<sup>fi</sup>nition of data quality as “<sup>fi</sup>tness for use.” The concept of <sup>fi</sup>tness for use emphasizes the context of the data, mainly the uses, users, and suppliers of the data [28,39]. Prioritization of data quality issues according to users' perceptions and needs is assisted today by various methods and tools (e.g., [33,47,53]). There are also various tools and methods that guide design and resource allocation from a data utilization perspective, such as the models described earlier. Some tools are available today that assist directly with prioritization and resource allocation in data quality management settings (e.g., [10]).

A unique contribution of our research over related work by other researchers is its focus on the magnitude of the damage that the errors in one input produce relative to other inputs. We aim to identify, for instance, which of the inputs should be treated <sup>fi</sup>rst when one is seeking the highest decrease in decision error rate for each input error that he or she removes. We believe that this research angle is rare. In particular, MIS and other studies center, instead, on the aggregate effect of input errors on output accuracy.

## 3. Model

Our investigation of the effect of errors on the outcomes of disjunctive and conjunctive decisions exploits statistical properties of random variables, primarily their expected value. We <sup>fi</sup>rst examine single binary logical OR and AND operations — each of these operations employs two inputs. This section formulates the damage that is attributed to errors in a given input. The variables in use by our model are listed and de<sup>fi</sup>ned below:

• U, V: The correct input classi<sup>fi</sup>cations as ful<sup>fi</sup>lling or not ful<sup>fi</sup>lling the decision criterion. These are dichotomous random variables that accept the values 1 and 0. These values correspond to true, i.e., the value of the decision variable ful<sup>fi</sup>lls the relevant decision criterion, and false, i.e., the value of the decision variable does not ful<sup>fi</sup>ll the criterion, respectively. The terms “input” and “input classi<sup>fi</sup>cation” will be used interchangeably.

• W: The correct decision outcome; W is a dichotomous random variable that accepts the values 1 (true), i.e., the correct decision is positive, and 0 (false), i.e., the correct decision is negative.

$U _ { a } , V _ { a } \colon$ : The recorded, possibly incorrect input classi<sup>fi</sup>cations; $U _ { a }$ and $V _ { a }$ are dichotomous random variables that accept the values 1 (true) and 0 (false). Again, the terms “input” and “input classi<sup>fi</sup>cation” will be used interchangeably.

$D _ { U } , \ D _ { V } .$ Inform about the occurrence of an error in $U _ { a }$ and $V _ { a } ,$ respectively. These are dichotomous random variables that accept the values 1 and 0, which correspond to error and no error, respectively.

$W _ { a } \mathrm { : }$ The output decision that is generated based on the recorded inputs; $W _ { a }$ is a dichotomous random variable that accepts the values 1 (true) and 0 (false).

$D _ { W } \colon$ A dichotomous random variable that accepts the values 1 (error) and 0 (no error). This variable tells us if the recorded decision, $W _ { a } ,$ is correct or not. A decision error is registered whenever a decision based on the available inputs disagrees with the same decision based on error-free inputs.

Statistical parameters:

$\begin{array} { r } { p _ { U } , p _ { V } , p _ { D _ { U } } , p _ { D _ { V } } , p _ { D _ { W } } . } \end{array}$ Expected values; subscripts identify the relevant random variables. For example, the expected value of U is denoted by $p _ { U } ,$ i.e., $p _ { U } = E ( U ) = P r ( U = 1 )$ . Note that $p _ { U }$ (as well as $p _ { V } )$ is equal to the probability that a value of the decision variable satis<sup>fi</sup>es the criterion on the variable; it may also be viewed as the fraction of the true values that satisfy the criterion. Furthermore, $p _ { D _ { U } }$ and, similarly, the expected value of any random variable that represents the occurrence of an error, is the same as the probability of occurrence of that error. The terms “error probability” and “error rate” will be used interchangeably.

The relationship among $U _ { a } , D _ { U }$ , and U is given by:

$$
U _ {a} = (1 - D _ {U}) U + D _ {U} (1 - U) = U + D _ {U} - 2 U D _ {U}.\tag{1}
$$

If the value of $D _ { U }$ is zero, that is, if this variable indicates that no error has occurred, then Eq. (1) is reduced to $U _ { a } = U , { \mathrm { i . e . } }$ , the recorded input is the same as the correct input. However, if the value of $D _ { U }$ indicates the occurrence of an error, then Eq. (1) assigns a value of one to $U _ { a }$ if U is zero and a value of zero if U is one. An equivalent relationship exists among $V _ { a } , D _ { V } ,$ and V, and among $W _ { a } , D _ { W } ,$ and W:

$$
V _ {a} = (1 - D _ {V}) V + D _ {V} (1 - V) = V + D _ {V} - 2 V D _ {V}\tag{2}
$$

$$
W _ {a} = (1 - D _ {W}) W + D _ {W} (1 - W) = W + D _ {W} - 2 W D _ {W}.\tag{3}
$$

In order to simplify the analysis we will assume that our random variables are not involved in any statistical dependencies. We will discuss this assumption in the <sup>fi</sup>nal section. It should be clari<sup>fi</sup>ed, however, that our Statistical Independence Assumption (SIA) does not contradict the understanding that an error in a binary variable is inherently negatively correlated with the true variable [1]. While such an understanding refers to the magnitude of the error, this paper accounts for the incidence of an error, not its magnitude.

Statistical Independence Assumption (SIA): None of the variables in $\{ U , V , D _ { U } , D _ { V } \}$ or products of such variables is statistically dependent on any other variable in $\{ U , V , D _ { U } , D _ { V } \}$ or any product of such variables.

## 3.1. Formulation of the damage under logical conjunction

In the case of logical conjunction, the ideal logical conjunction operation—where inputs are error-free — is captured by:

$$
W = U V.\tag{4}
$$

The consistency of Eq. (4) with the de<sup>fi</sup>nition of logical conjunction can be veri<sup>fi</sup>ed through a systematic evaluation of W for each possible combination of the values of U and V.

In real-world settings, data processing applications typically do not take the accuracy of the data into account. They are not adjusted to account for variations in data accuracy. Similar to real-world settings, we model the relationship among the actual decision, $W _ { a } ,$ and the actual inputs, $U _ { a }$ and $V _ { a } ,$ equivalent to the relationship among the correct decision and inputs:

$$
W _ {a} = U _ {a} V _ {a}.\tag{5}
$$

The relationship between the observed input $U _ { a }$ and the correct input U is described by Eq. (1). Similarly, the relationship between the observed input $V _ { a }$ and the correct input V is described by Eq. (2). Finally, the relationship between the actual decision $W _ { a }$ and the correct decision W is speci<sup>fi</sup>ed by Eq. (3).

Using Eqs. (1)–(5), the link among the probability of a decision error, the correct probabilities of satisfying the decision criteria, and classi<sup>fi</sup>cation error probabilities is described by Lemma 1. Lemma 1 asserts that the probability of a decision error is equal to an aggregate of products of one or more of the probabilities of satisfying the decision criteria and/or one or more of the classi<sup>fi</sup>cation error probabilities. In particular, these products include $p _ { V } p _ { D _ { U } } , p _ { U } p _ { D _ { V } } , p _ { D _ { U } } p _ { D _ { V } } , p _ { U } p _ { D _ { U } } p _ { D _ { V } }$ $p _ { V } p _ { D _ { v } } p _ { D _ { v } }$ , and $p _ { U } p _ { V } p _ { D _ { U } } p _ { D _ { \backslash } }$ . The sign of the terms $p _ { V } p _ { D _ { U } } , p _ { U } p _ { D _ { V } } , p _ { D _ { U } } p _ { D _ { V } }$ and $p _ { U } p _ { V } p _ { D _ { U } } p _ { D _ { V } }$ is positive, and the two remaining terms are negative.

Lemma 1. Assuming Eqs. (1)–(5) and the Statistical Independence Assumption:

$$
p _ {D _ {W}} = p _ {V} p _ {D _ {U}} + p _ {U} p _ {D _ {V}} + p _ {D _ {U}} p _ {D _ {V}} - 2 p _ {U} p _ {D _ {U}} p _ {D _ {V}} - 2 p _ {V} p _ {D _ {U}} p _ {D _ {V}} + 2 p _ {U} p _ {V} p _ {D _ {U}} p _ {D _ {V}}.\tag{6}
$$

The damage that errors in an input in<sup>fl</sup>ict on output accuracy is de<sup>fi</sup>ned by this work as the change in output error probability due to a change in the error probability of that input. The idea that motivates our focus on this concept is that, all other things being equal, it would be bene<sup>fi</sup>cial to assign priority to the elimination of errors that have a higher negative effect on output accuracy over errors that have a less negative effect. For instance, suppose that, by decreasing the error rate in one of the inputs by 1%, we decrease the decision error rate by 0.5%, while a decrease in the error rate of a second input by 1% decreases the decision error rate by 0.05%. Obviously, all other things being equal, it would be more effective to decrease the error rate of the <sup>fi</sup>rst input than the second. Technically, we use a partial derivative to implement the concept of damage. A derivative is a measure of the change in the output of a function when its input changes, therefore, it is consistent with the notion of damage as it is perceived by this work. In a conjunctive decision, the damage is expressed by the derivative of $p _ { D _ { w } }$ with respect to $p _ { D _ { v } }$

$$
\partial p _ {D _ {W}} / \partial p _ {D _ {V}} = p _ {U} + p _ {D _ {U}} - 2 p _ {D _ {U}} (p _ {U} + p _ {V} - p _ {U} p _ {V})\tag{7}
$$

and, likewise, by the derivative of $p _ { D _ { w } }$ with respect to $p _ { D _ { U } } \colon$

$$
\partial p _ {D _ {W}} / \partial p _ {D _ {U}} = p _ {V} + p _ {D _ {V}} - 2 p _ {D _ {V}} (p _ {U} + p _ {V} - p _ {U} p _ {V}).\tag{8}
$$

Clearly, the damage of the errors in one input is equal to the damage of errors in the other input if and only if Eqs. (7) and (8) are equal. Table 1 lists the values of Eqs. (7) and (8) for selected parameter value sets. As demonstrated by Table 1, the gap between these two derivatives can be dramatic<sup>1</sup> (Tables 1 and 2 use a <sup>fi</sup>xed classi<sup>fi</sup>cation error probability of 0.05).

## 3.2. Formulation of the damage under logical disjunction

An error-free disjunction operation is portrayed by:

$$
W = U + V - U V.\tag{9}
$$

The consistency of Eq. (9) with the de<sup>fi</sup>nition of logical disjunction can be easily veri<sup>fi</sup>ed through a systematic evaluation of W for each possible combination of the values of U and V. The relationship among the actual decision $W _ { a }$ and the observed inputs is the same as the relationship among the correct decision and inputs:

The effect of a higher input error rate on output error rate (AND)

<table><tr><td> $p_U$ </td><td> $p_V$ </td><td> $p_{D_U}$ </td><td> $p_{D_V}$ </td><td> $\frac{\partial p_{D_W}}{\partial p_{D_U}}$ </td><td> $\frac{\partial p_{D_W}}{\partial p_{D_V}}$ </td><td> $p_U$ </td><td> $p_V$ </td><td> $p_{D_U}$ </td><td> $p_{D_V}$ </td><td> $\frac{\partial p_{D_W}}{\partial p_{D_U}}$ </td><td> $\frac{\partial p_{D_W}}{\partial p_{D_V}}$ </td></tr><tr><td>0.01</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.06</td><td>0.06</td><td>0.3</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.03</td><td>0.32</td></tr><tr><td>0.01</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.23</td><td>0.04</td><td>0.3</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.21</td><td>0.31</td></tr><tr><td>0.01</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.41</td><td>0.02</td><td>0.3</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.39</td><td>0.29</td></tr><tr><td>0.01</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.59</td><td>0</td><td>0.3</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.58</td><td>0.28</td></tr><tr><td>0.01</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.77</td><td>-0.02</td><td>0.3</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.76</td><td>0.26</td></tr><tr><td>0.01</td><td>0.99</td><td>0.05</td><td>0.05</td><td>0.94</td><td>-0.04</td><td>0.3</td><td>0.99</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.25</td></tr><tr><td>0.1</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.14</td><td>0.4</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.02</td><td>0.41</td></tr><tr><td>0.1</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.22</td><td>0.12</td><td>0.4</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.2</td><td>0.4</td></tr><tr><td>0.1</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.4</td><td>0.1</td><td>0.4</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.39</td><td>0.39</td></tr><tr><td>0.1</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.59</td><td>0.09</td><td>0.4</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.57</td><td>0.37</td></tr><tr><td>0.1</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.77</td><td>0.07</td><td>0.4</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.76</td><td>0.36</td></tr><tr><td>0.1</td><td>0.99</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.05</td><td>0.4</td><td>0.99</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.35</td></tr><tr><td>0.2</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.04</td><td>0.23</td><td>0.5</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.01</td><td>0.5</td></tr><tr><td>0.2</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.21</td><td>0.21</td><td>0.5</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.19</td><td>0.49</td></tr><tr><td>0.2</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.4</td><td>0.2</td><td>0.5</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.38</td><td>0.48</td></tr><tr><td>0.2</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.58</td><td>0.18</td><td>0.5</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.57</td><td>0.47</td></tr><tr><td>0.2</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.77</td><td>0.17</td><td>0.5</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.76</td><td>0.46</td></tr><tr><td>0.2</td><td>0.99</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.15</td><td>0.5</td><td>0.99</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.45</td></tr></table>

$$
W _ {a} = U _ {a} + V _ {a} - U _ {a} V _ {a}.\tag{10}
$$

Subsequently, using Eqs.(1)−(3), (9), and (10), the connection among the probability of a decision error, the probabilities of satisfying the decision criteria (i.e., the probabilities that are derived from error-free data), and respective input error probabilities is described by Lemma 2. Lemma 2 asserts that the probability of a decision error is equal to an aggregate of the input error probabilities and products of one or more of the probabilities of satisfying the criteria and/or one or more of the input error probabilities. In particular, these include $p _ { D _ { U } } , p _ { D _ { V } } , p _ { V } p _ { D _ { U } } , p _ { U } p _ { D _ { V } } , p _ { D _ { U } } p _ { D _ { V } } ,$ , and $p _ { U } p _ { V } p _ { D _ { U } } p _ { D _ { V } }$ The sign of the terms $p _ { D _ { U } } \mathbf { \mathrm { , } } p _ { D _ { v } }$ , and $p _ { U } p _ { V } p _ { D _ { U } } p _ { D _ { V } }$ , is positive, while the remaining terms are negative.

Lemma 2. Assuming Eqs. $( 1 ) - ( 3 ) , ( 9 )$ , and (10), and the Statistical Independence Assumption:

$$
p _ {D _ {W}} = p _ {D _ {U}} + p _ {D _ {V}} - p _ {U} p _ {D _ {V}} - p _ {V} p _ {D _ {U}} - p _ {D _ {V}} p _ {D _ {U}} + 2 p _ {U} p _ {V} p _ {D _ {V}} p _ {D _ {U}}.\tag{11}
$$

The effect of a higher input error rate on output error rate (OR).

<table><tr><td> $p_U$ </td><td> $p_V$ </td><td> $p_{D_U}$ </td><td> $p_{D_V}$ </td><td> $\frac{\partial p_{D_W}}{\partial p_{D_U}}$ </td><td> $\frac{\partial p_{D_W}}{\partial p_{D_V}}$ </td><td> $p_U$ </td><td> $p_V$ </td><td> $p_{D_U}$ </td><td> $_{D_V}$ </td><td> $\frac{\partial p_{D_W}}{\partial p_{D_U}}$ </td><td> $\frac{\partial p_{D_W}}{\partial p_{D_V}}$ </td></tr><tr><td>0.01</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.94</td><td>0.3</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.65</td></tr><tr><td>0.01</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.75</td><td>0.94</td><td>0.3</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.76</td><td>0.66</td></tr><tr><td>0.01</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.55</td><td>0.94</td><td>0.3</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.56</td><td>0.66</td></tr><tr><td>0.01</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.35</td><td>0.94</td><td>0.3</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.37</td><td>0.67</td></tr><tr><td>0.01</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.15</td><td>0.94</td><td>0.3</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.17</td><td>0.67</td></tr><tr><td>0.01</td><td>0.99</td><td>0.05</td><td>0.05</td><td>-0.04</td><td>0.94</td><td>0.3</td><td>0.99</td><td>0.05</td><td>0.05</td><td>-0.01</td><td>0.68</td></tr><tr><td>0.1</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.85</td><td>0.4</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.55</td></tr><tr><td>0.1</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.75</td><td>0.85</td><td>0.4</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.76</td><td>0.56</td></tr><tr><td>0.1</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.55</td><td>0.85</td><td>0.4</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.57</td><td>0.57</td></tr><tr><td>0.1</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.36</td><td>0.86</td><td>0.4</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.37</td><td>0.57</td></tr><tr><td>0.1</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.16</td><td>0.86</td><td>0.4</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.18</td><td>0.58</td></tr><tr><td>0.1</td><td>0.99</td><td>0.05</td><td>0.05</td><td>-0.03</td><td>0.86</td><td>0.4</td><td>0.99</td><td>0.05</td><td>0.05</td><td>0</td><td>0.59</td></tr><tr><td>0.2</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.75</td><td>0.5</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.94</td><td>0.45</td></tr><tr><td>0.2</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.75</td><td>0.75</td><td>0.5</td><td>0.2</td><td>0.05</td><td>0.05</td><td>0.76</td><td>0.46</td></tr><tr><td>0.2</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.56</td><td>0.76</td><td>0.5</td><td>0.4</td><td>0.05</td><td>0.05</td><td>0.57</td><td>0.47</td></tr><tr><td>0.2</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.36</td><td>0.76</td><td>0.5</td><td>0.6</td><td>0.05</td><td>0.05</td><td>0.38</td><td>0.48</td></tr><tr><td>0.2</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.17</td><td>0.77</td><td>0.5</td><td>0.8</td><td>0.05</td><td>0.05</td><td>0.19</td><td>0.49</td></tr><tr><td>0.2</td><td>0.99</td><td>0.05</td><td>0.05</td><td>-0.02</td><td>0.77</td><td>0.5</td><td>0.99</td><td>0.05</td><td>0.05</td><td>0.01</td><td>0.5</td></tr></table>

The damage of errors in $V _ { a } ,$ which is expressed by the partial derivative of Eq. (11) with respect to $p _ { D _ { v } }$ , is:

$$
\partial p _ {D _ {W}} / \partial p _ {D _ {V}} = 1 - p _ {U} - p _ {D _ {U}} + 2 p _ {U} p _ {V} p _ {D _ {U}} = 1 - p _ {U} (1 - 2 p _ {V} p _ {D _ {U}}) - p _ {D _ {U}}.\tag{12}
$$

Similarly, the damage of errors in $U _ { a }$ is given by:

$$
\partial p _ {D _ {W}} / \partial p _ {D _ {U}} = 1 - p _ {V} - p _ {D _ {V}} + 2 p _ {U} p _ {V} p _ {D _ {V}} = 1 - p _ {V} (1 - 2 p _ {U} p _ {D _ {V}}) - p _ {D _ {V}}.\tag{13}
$$

Again, the damage of the errors in $V _ { a }$ is equal to the damage of the errors in $U _ { a }$ if and only if Eqs. (12) and (13) are equal. Nonetheless, in most cases Eqs. (12) and (13) are not equal and can actually be far different from each other (see Table 2).

## 4. Error dominance

Consider a decision rule that is implemented by a single Boolean binary OR or AND operation, where ISA holds true. By applying Eqs. (7) and (8) or Eqs. (12) and (13) we can calculate the damage of errors in each of the observed inputs, i.e., $U _ { a }$ and $V _ { a \cdot }$ Subsequently, these equations can be used for ranking the observed inputs of the decision rule according to the damage that they in<sup>fl</sup>ict on the output of the decision. In the following sections we will employ our model to discover general properties of those rankings. These general properties can often simplify the computation of the rankings. We will also extend our results to decision rules that consist of any number of conjunction and disjunction operations. Essentially, the results of the ensuing analysis can often obviate the need to use the damage formulas that we have produced in the previous section.

According to Eqs. (7), (8), (12), and (13), the damage depends on the probabilities of satisfying the decision criteria and the input classi<sup>fi</sup>cation error probabilities. We will focus on the concept of error dominance. We say that one input dominates another if the damage of errors in that input is greater than the damage of the errors in the second input.

De<sup>fi</sup>nition 1 (Error dominance in a single operation). If $U , V , D _ { U }$ and $D _ { V }$ are such that, using Eqs. $( 7 ) , ( 8 ) , \partial p _ { D _ { w } } / \partial p _ { D _ { U } } > \partial p _ { D _ { w } } / \partial p _ { D _ { v } }$ , then $U _ { a }$ dominates $V _ { a }$ under logical conjunction. If U, $V , D _ { U } ,$ and $D _ { V }$ are such that, using Eqs. (12)–(13), $\partial p _ { D _ { w } } / \partial p _ { D _ { U } } / \partial p _ { D _ { w } } / \partial p _ { D _ { v } }$ , then $U _ { a }$ dominates $V _ { a }$ under logical disjunction.

## 4.1. Conditions of dominance under logical conjunction

Proposition 1 characterizes conditions in which one input dominates the other in a single binary AND operation. These conditions follow directly from Eqs. (7) and (8). As will be illustrated in Section $5 ,$ Proposition 1 implies that, when the probabilities of satisfying the decision criteria (i.e., as before, the true probabilities, not the probabilities based on the recorded data) are not too similar, the input that matches a lower probability dominates the input where that probability is higher. Corollary 1 offers a simple condition that ensures that the input that matches the lower probability dominates the other input. Namely, if the difference between these probabilities is at least as high as the difference between the corresponding classification error probabilities, then the input where the probability of satisfying the criterion is lower dominates. Notably, Eq. (15) is a suf<sup>fi</sup>cient condition for such dominance, it is not a necessary condition. In fact, this dominance order often holds true when the above differences are not as far apart as speci<sup>fi</sup>ed.

Proposition 1 (AND). Assume Eqs.(7), (8). Then, $V _ { a }$ dominates $U _ { a }$ if and only if

$$
p _ {U} + p _ {D _ {U}} - 2 p _ {D _ {U}} \left(p _ {U} + p _ {V} - p _ {U} p _ {V}\right) > p _ {V} + p _ {D _ {V}} - 2 p _ {D _ {V}} \left(p _ {U} + p _ {V} - p _ {U} p _ {V}\right).\tag{14}
$$

Corollary 1 (AND). Assume Eqs. (7)–(8). For any p<sub>U</sub>, p<sub>V</sub>, $p _ { D _ { U } }$ , and $p _ { D _ { v } }$ , if

$$
p _ {U} - p _ {V} > \left| p _ {D _ {V}} - p _ {D _ {U}} \right|\tag{15}
$$

then $V _ { a }$ dominates $U _ { a \cdot }$

Section 5 presents a deeper study of Proposition 1.

## 4.2. Conditions of dominance under logical disjunction

Parallel to Proposition 1, Proposition 2 outlines conditions of dominance under the logical disjunction operation. A major <sup>fi</sup>nding of Proposition 2, which will be illustrated in Section $5 ,$ is that, when the probabilities of satisfying the criteria are not too similar, the input that matches a higher probability dominates the input where that probability is lower. Corollary 2 offers a simple condition, analogous to the condition of Corollary 1, that, when met, the input in which the probability of satisfying the related criterion is higher dominates the other input. If the difference between these probabilities is at least as high as the difference between the corresponding classification error probabilities, then the input where the probability of satisfying the criterion is higher dominates. Inequality Eq. (17) is a suf<sup>fi</sup>cient condition for such dominance, not a necessary condition. As will be shown in the following section, this dominance order often holds true, regardless.

Proposition 2 (OR). Assume Eqs. (12)–(13). Then, $U _ { a }$ dominates $V _ { a }$ if and only if

$$
1 - p _ {V} - p _ {D _ {V}} + 2 p _ {U} p _ {V} p _ {D _ {V}} > 1 - p _ {U} - p _ {D _ {U}} + 2 p _ {U} p _ {V} p _ {D _ {U}}.\tag{16}
$$

Corollary 2 (OR). Assume Eqs. (12)–(13). For any $p _ { U } , p _ { V } , p _ { D _ { U } }$ , and $p _ { D _ { V } }$ , if

$$
p _ {U} - p _ {V} > | p _ {D _ {V}} - p _ {D _ {U}} |\tag{17}
$$

then $U _ { a }$ dominates $V _ { a \cdot }$

The conditions of dominance under an OR operation are further examined in the following section.

## 5. Conditions of error dominance: illustration

## 5.1. Conditions of dominance under logical conjunction

Consider a company decision regarding the rental of a new of<sup>fi</sup>ce as described in the introduction section. We will illustrate the theoretical results pertaining to a conjunctive decision rule and, later on, the results pertaining to a disjunctive decision rule, using this scenario.

Suppose that the rental decision utilizes the following simple conjunctive rule: the age of the of<sup>fi</sup>ce building must not exceed ten years and the of<sup>fi</sup>ce space has to be in the range of 3500–5000ft<sup>2</sup>. Assume a selection process that screens the available alternatives (e.g., properties that are listed in a local commercial rentals database) according to this conjunctive rule. Now, let U=1 designate an available of<sup>fi</sup>ce that satis<sup>fi</sup>es the age requirement; U=0 otherwise. Likewise, V=1 refers to an available of<sup>fi</sup>ce that has the speci<sup>fi</sup>ed square footage; $V { = } 0$ otherwise. Accordingly, $p _ { U }$ matches the fraction of the available of<sup>fi</sup>ces that satisfy the age constraint, and $p _ { V }$ matches the fraction of of<sup>fi</sup>ces that satisfy the space constraint. Clearly, p<sub>U</sub> and $p _ { U }$ may vary across different markets. For example, $p _ { U }$ may be higher in areas in which there is a signi<sup>fi</sup>cant on-going construction of new of<sup>fi</sup>ce buildings. Similarly, $p _ { V }$ may be lower when the demand for the speci<sup>fi</sup>ed space range is temporarily high.

Suppose that the recorded values of U and V, denoted by $U _ { a }$ and $V _ { a } ,$ respectively, are infected with errors, and SIA holds true $( { \mathrm { i . e . } }$ , rental of<sup>fi</sup>ces that meet the age criterion have the same probability of meeting the space criterion as those that do not meet the age criterion; errors in the age classi<sup>fi</sup>cation are independent of errors in the space classi<sup>fi</sup>cation, etc.). Assume also that the difference between the two input error probabilities is bounded by P, i.e., $| p _ { D _ { v } } – p _ { D _ { v } } | \le P .$ Fig. 2 portrays the outcome of applying Proposition 1 for resolving which of the two inputs, $U _ { a } \thinspace 0 \Gamma \thinspace V _ { a } ,$ dominates. Fig. 2 accounts for <sup>fi</sup>ve possible values of P: 0.02, 0.05, 0.1, 0.15, and 0.2. For each of these values, it shows a chart that distinguishes combinations of $p _ { U }$ and p where $U _ { a }$ dominates $V _ { a }$ (dark gray area) from combinations where $V _ { a }$ dominates $U _ { a }$ (light gray area). The black areas mark combinations of $p _ { U }$ and $p _ { V }$ such that the difference between them is not high enough to ascertain the dominant input. In those instances we need more information about the input error rates in order to determine in which of the inputs, $U _ { a } \thinspace \mathbf { o r } \ V _ { a } ,$ errors create more damage — we will discuss those instances later.

A study of Fig. 2 uncovers the following patterns:

• Whenever the gap between $p _ { U }$ and $p _ { V }$ is higher than P, the input that is associated with the lower of $p _ { U }$ and $p _ { V }$ dominates the other

(a) $\pmb { p } = 0 . 0 2$  
![](/api/attachments/WJZSJAR6/fulltext/images/2a5c4b921fff2f65898aee62d16d3f6cee81e6f6fa699b04ea2b0c8fbd9df7f1.jpg)  
(c) ${ p } \mathrm { { = } } 0 . 1$

(b)p =0.05  
![](/api/attachments/WJZSJAR6/fulltext/images/8b77a16dc2f432bbf9f902819e6783f43ab324026f5a2aad5e78533a4dfe9ea6.jpg)  
(d) p =0.15

![](/api/attachments/WJZSJAR6/fulltext/images/35bb633263cfdfacb93277379e6c3086f091221728a644594c508e89003d497f.jpg)

![](/api/attachments/WJZSJAR6/fulltext/images/5059f5215837b97b01693bd72077a4fa79dc6ffe8ad3208cbde915b1031d50d9.jpg)

(e)p =0.2  
![](/api/attachments/WJZSJAR6/fulltext/images/4d5faaab9b7dbed05d0246501320d681317613fd8a71d78d8c0c0cdee2543291.jpg)  
Fig. 2. Conditions of dominance (AND): dark gray $\mathsf { a r e a } = U _ { a }$ dominates $V _ { a } ;$ light gray $\mathsf { a r e a } = V _ { a }$ dominates $U _ { a \cdot }$

input (Corollary 1). For example, Fig. 2 (c), which refers to $P { = } 0 . 1$ demonstrates that $V _ { a }$ dominates $U _ { a }$ for any $p _ { U }$ and $p _ { V }$ where $p _ { U } -$ $p _ { V } { > } 0 . 1$ , and $U _ { a }$ dominates $V _ { a }$ for any $p _ { U }$ and $p _ { V }$ where $p _ { V } - p _ { U } { > } 0 . 1$ • Even when the gap between $p _ { U }$ and p is not higher than P, the rule that says that the input that is associated with the lower of ${ \dot { p } } _ { U }$ and $p _ { V }$ dominates the other input often applies. Mainly, as $p _ { U } + p _ { V } - p _ { U } p _ { V }$ gradually approaches 0.5 (see $p _ { U } = p _ { V } \cong 0 . 3 )$ , that rule holds true in an increasingly higher proportion of the possible combinations of $p _ { U }$ and $p _ { V }$

Suppose, now, that the dominance rule that we have illustrated through Fig. 2 is not valid for $p _ { U }$ and $p _ { V }$ (i.e., see the black areas in Fig. 2). Fig. 3 addresses these conditions, in which we need more information about the input error rates in order to determine the balance. Fig. 3 refers to selected pairs of $p _ { U }$ and $p _ { V } ,$ as speci<sup>fi</sup>ed by the titles of the individual charts, and portrays dominance as a function of input classi<sup>fi</sup>cation error probabilities. Fig. 3 accounts for input classi<sup>fi</sup>cation errors probabilities that are less than or equal to 0.5; higher probabilities are rare in practical settings. Due to the symmetric nature of the inputs, only pairs of $p _ { U }$ and $p _ { V }$ where $p _ { U } \ge p _ { V }$ were included. In addition, Fig. 3 is limited to pairs of $p _ { U }$ and $p _ { V }$ for which $p _ { U } - p _ { V } { \le } 0 . 5$ , since, as illustrated in Section $4 , \mathrm { i f } p _ { U } - p _ { V } { > } | p _ { D _ { V } } { - } p _ { D _ { U } } |$ then $V _ { a }$ is assured to dominate $U _ { a } .$

A close observation of Fig. 3 con<sup>fi</sup>rms the following implications of Proposition 1, when $p _ { D _ { U } } , p _ { D _ { V } } { \le } 0 . 5$ :

• When the probabilities of satisfying the criteria are similar enough relative to the difference between the matching error rates, and these probabilities are high (i.e., $p _ { U } + p _ { V } - p _ { U } { \cdot } p _ { V } { > } 0 . 5 )$ ), then errors in the input with the higher error rate create more damage. For example, $U _ { a }$ dominates $V _ { a }$ when $p _ { U } = 0 . 6 , p _ { V } = 0 . 5 , p _ { D _ { U } } = 0 . 2 5$ , and $p _ { D _ { v } } = 0 . 0 5$

• Surprisingly, when the probabilities of satisfying the criteria are, again, similar relative to the difference between the matching error rates, but these probabilities are not high $( \mathrm { i . e . , } p _ { U } + p _ { V } - p _ { U } { \cdot } p _ { V } { > } 0 . 5 )$ then classi<sup>fi</sup>cation errors in the input with the lower error rate are more detrimental to the decision. For example, $U _ { a }$ dominates $V _ { a }$ when $p _ { U } = 0 . 2 , p _ { V } = 0 . 1 , p _ { D _ { U } } = 0 . 0 5 ,$ , and $p _ { D _ { v } } = 0 . 3 0$

Based on Figs. 2 and 3, our of<sup>fi</sup>ce rental scenario can be concluded as follows. If the fraction of of<sup>fi</sup>ce rentals that are at or below the age limit is low in relation to the fraction of rentals that have the required space, then errors in the classi<sup>fi</sup>cation of the of<sup>fi</sup>ce building as passing or not passing the age criterion will be more damaging to decision accuracy. Conversely, if the fraction of of<sup>fi</sup>ce rentals that have the required space is low in relation to the fraction of available rentals that are at or below the age limit, then errors in the classi<sup>fi</sup>cation of the of<sup>fi</sup>ce space will be more damaging. Nonetheless, this dominance law is not necessarily valid if the gap between the error rates is at least as high as the gap between the respective fractions of properties that satisfy one or another of the criteria. If the error rate of one input is suf<sup>fi</sup>ciently higher than the other error rate and the above fractions are high, then the input that shows the higher error rate will dominate. Hence, for instance, if the fraction of properties that satisfy the age criterion and the fraction of properties that satisfy the space requirement are not low, and the of<sup>fi</sup>ce space data set exhibits a suf<sup>fi</sup>ciently high classi<sup>fi</sup>cation error rate in relation to the classi<sup>fi</sup>cation error rate of the age data set, then the of<sup>fi</sup>ce space data will dominate. On the other hand, if the error rate of one input is suf<sup>fi</sup>ciently higher than the other error rate and the fractions are low, then the input that shows the lower error rate will dominate. Therefore, if the fraction of properties that satisfy the age criterion is low and so is the fraction of properties that satisfy the space requirement, and if the of<sup>fi</sup>ce space data set exhibits substantially lower classi<sup>fi</sup>cation error rate than the classi<sup>fi</sup>cation error rate of the age data set, then the of<sup>fi</sup>ce space data will dominate.

![](/api/attachments/WJZSJAR6/fulltext/images/7a4196d108ae72e770e491df5162859bf116a1b743ac639e729d6ea6777dda2a.jpg)  
Fig. 3. Input error rate contribution to dominance (AND).

## 5.2. Conditions of dominance under logical disjunction

We continue with the example of the company decision about the rental of a new of<sup>fi</sup>ce. Consider an alternative scenario, according to which, due to a severe parking problem in the relevant geographic area, a major requirement of this company is that either the of<sup>fi</sup>ce building has its own covered parking or the building is located within half a mile from a public transportation hub. Now, let U=1 denote an available of<sup>fi</sup>ce that has the required parking; U=0 otherwise. Likewise, V=1 denotes an available of<sup>fi</sup>ce that is within the required distance from a public transportation hub; V=0 otherwise. Fig. 4 uses the same conventions as Fig. 2 to illustrate the <sup>fi</sup>ndings of Proposition 2. A study of Figs. 4 and 5 suggests that these <sup>fi</sup>gures form simple transformations of Figs. 2 and 3, respectively. There is a fundamental similarity to the previous scenario. Nonetheless:

(a)P =0.02  
![](/api/attachments/WJZSJAR6/fulltext/images/c61a1ce0d73f3b787f1744d2846ef84ec53a68878c93c778aaeb1ec1763a819b.jpg)  
(c) ${ p } = 0 . 1$

(b)P =0.05  
![](/api/attachments/WJZSJAR6/fulltext/images/33f29b46578ba49912a91814c5ef394ad9fb2037503c2c27a24790274384bc8d.jpg)

![](/api/attachments/WJZSJAR6/fulltext/images/2a100998cf2c2479d2c3bb371ae26f604700125b2b11ad13cd6b2a7b1455355d.jpg)

(d) p =0.15  
![](/api/attachments/WJZSJAR6/fulltext/images/e987f5d9a78055b6826482e7b9747d8b524d9aac4635f66d76d9cd345c565805.jpg)

(e) ${ \pmb p } = 0 . 2$  
![](/api/attachments/WJZSJAR6/fulltext/images/f63b49ab68168206a3177cb6bd4e76d6b6ee1ea356936d0732125b92df04a73d.jpg)  
Fig. 4. Conditions of dominance (OR): dark gray $\mathsf { a r e a } = U _ { a }$ dominates V ; light gray area = $V _ { a }$ dominates $U _ { a } .$

• The input that is associated with the higher of $p _ { U }$ and $p _ { V }$ dominates the other input whenever the gap between $p _ { U }$ and $p _ { V }$ is higher than P (Corollary 2). In addition, even when the gap between $p _ { U }$ and $p _ { V }$ is not higher than P, that dominance often applies. Mainly, as p ·p gradually approaches 0.5 (see $p _ { U } = p _ { V } { \cong } 0 . 7 )$ , that dominance holds true in an increasingly higher proportion of the possible combinations of $p _ { U }$ and $p _ { V }$

• Otherwise, when the probabilities of satisfying the criteria are suf<sup>fi</sup>ciently similar relative to the difference between the respective error rates, and the probabilities are not very high $\left( p _ { U } . p _ { V } { < } 0 . 5 \right)$ , then errors in the input with the higher error rate are more detrimental to the output. For example, $V _ { a }$ dominates $U _ { a }$ when $p _ { U } = 0 . 2 , p _ { V } = 0 . 1$ $p _ { D _ { t I } } = 0 . 0 5$ , and $p _ { D _ { v } } = 0 . 2 0$

• Notably, when the probabilities of satisfying the criteria are similar, as explained above, but these probabilities are high $\left( p _ { U } \cdot p _ { V } { < } 0 . 5 \right)$ then errors in the input with the lower error rate are more damaging to the output. For example, $V _ { a }$ dominates $U _ { a }$ when $p _ { U } = 0 . 9$ $p _ { V } = 0 . 8 , p _ { D _ { U } } = 0 . 3 0$ , and $p _ { D _ { v } } = 0 . 0 5$

Subsequently, the second of<sup>fi</sup>ce rental scenario, pertaining to logical disjunction, can be concluded as follows. If the proportion of of<sup>fi</sup>ce rentals that do not exceed the limit on the distance from a hub is high in relation to the proportion of rentals that have covered parking, then errors in the categorization of properties' distance from a hub will be more damaging to decision accuracy. Conversely, if the proportion of of<sup>fi</sup>ce rentals that have covered parking is high in relation to the proportion of rentals that comply with the distance limit, then errors in the classi<sup>fi</sup>cation based on the parking criterion will be more damaging. If, however, the gap between the classi<sup>fi</sup>cation error rates is at least as high as the gap between the above proportions, then a different law may apply. If the classi<sup>fi</sup>cation error rates are suf<sup>fi</sup>ciently far apart and the proportions are not very high, then the input that shows the higher error rate will dominate. For example, the parking data will dominate the data on the distance from a hub if the fractions are not very high and the error rate in judgments of the parking availability is suf<sup>fi</sup>ciently higher than the error rate of the classi<sup>fi</sup>cation of the distance from a hub. If the classi<sup>fi</sup>cation error rates are suf<sup>fi</sup>ciently far apart and the former fractions are very high, then, contrary to our intuition, errors in the data that show the lower error rate will be more damaging. Accordingly, under such conditions, errors in the judgments of the availability of covered parking will be less damaging than errors in the distance classi<sup>fi</sup>cation if those judgments have a higher error rate.

## 6. Extension of the error dominance theory: multiple operations

The conclusions of this study can be extended to decision rules involving $N { \ge } 2$ binary operations. Given N+1 inputs, suppose that two of the inputs have the characteristic that one dominates the other under a binary operation that combines them. This section proves that, for the most part, such dominance is preserved throughout successive applications of any mixture of binary operations. Proposition 3 speci<sup>fi</sup>es a variety of suf<sup>fi</sup>cient conditions in which dominance in a single operation is preserved throughout subsequent operations. The new symbols are de<sup>fi</sup>ned below.

$I _ { j } , j = 1 , 2 , 3 , . .$ : Dichotomous random variables comparable to U (or V); I<sub>j</sub> represents an error-free input classi<sup>fi</sup>cation.

$I _ { j } ^ { a } , \ j = 1 , 2 , . . .$ Dichotomous random variables representing the available, observed input classi<sup>fi</sup>cations, comparable to $U _ { a } . \ I _ { j } ^ { a } , \ I _ { j } ,$ and F<sup>I</sup> (see below) satisfy Eq. (1).

$F _ { j } ^ { I } , j = 1 , 2 , . . .$ : Dichotomous random variables; $F _ { j } ^ { l }$ speci<sup>fi</sup>es whether an error occurred in $I _ { j } ^ { a } ,$ , similar to $D _ { U } .$

$O _ { j } , ~ j = 1 , 2 , \ldots$ Dichotomous random variables comparable to W. $O _ { 1 } \equiv I _ { 1 }$ , and $\mathrm { f o r } j { = } 2 , 3 , . . , O _ { j }$ is the result of applying an operation on $O _ { j - \cdot }$ <sub>1</sub> and $I _ { j \cdot }$

${ \cal O } _ { i } ^ { a } , j = 1 , 2 , . . .$ Dichotomous random variables comparable to $W _ { a } .$ $O _ { 1 } ^ { a } \equiv I _ { 1 } ^ { a } ,$ , and $\mathrm { f o r } j { = } 2 , 3 , . . . , O _ { j } ^ { a }$ is the result of applying an operation on $O _ { \mathrm { j } - 1 } ^ { a }$ and $I _ { j } ^ { a } .$ .

$F _ { j } ^ { \bar { O } } , j { = } 1 , \bar { 2 } , . .$ : Dichotomous random variables. $F _ { j } ^ { O } , O _ { j } ^ { a }$ , and $O _ { j }$ satisfy Eq. $( 3 ) . \ F _ { j } ^ { O }$ , which is comparable to $D _ { W } ,$ informs us about the occurrence of a decision error.

Statistical parameters:

• $p _ { j } ^ { I } \colon$ The expected value of $I _ { j } , j = 1 , 2 , . .$

$p _ { j } ^ { F _ { I } } \colon$ The expected value of $F _ { j } ^ { I } , j = 1 , 2$

$p _ { j } ^ { F o . } $ The expected value of $F _ { j } ^ { O } , j { = } 1 , 2 , . .$

De<sup>fi</sup>nition 2 (Error dominance in a sequence of operations). Given $I _ { j } , F _ { j } ^ { I } , j = 1 , . . , N + 1 \ ( N \ge 2 )$ , if $I _ { i } , F _ { i } ^ { I } , I _ { k } ,$ and $F _ { k } ^ { I } \ ( 1 \leq i , k \leq N + 1 )$ are such that $\partial p _ { N + 1 } ^ { F _ { 0 } } / \partial p _ { i } ^ { F _ { I } } { \geq } \partial p _ { N + 1 } ^ { F _ { 0 } } / \partial p _ { k } ^ { F _ { I } }$ , then $I _ { i } ^ { a }$ dominates $I _ { k } ^ { a }$ in a sequence of N operations on $I _ { j } ^ { a } , j = \bar { 1 } , . . , \bar { N } + \bar { 1 }$

Proposition 3, which is presented below, implies that the conditions in which dominance in a single operation is not preserved throughout subsequent operations are limited to a small subset of the possible value combinations of $p _ { U } , P _ { V } , p _ { D _ { U } }$ , and $p _ { D _ { v } }$ . Suppose that $V _ { a }$ dominates $U _ { a }$ in a single conjunction operation. Suppose also that their output, $W _ { a } ,$ is combined through conjunction with $O _ { N - 1 } ^ { a } ,$ which is the output of a sequence of binary operations on $I _ { j } ^ { a } , j = 1 , . . , N - 1$

![](/api/attachments/WJZSJAR6/fulltext/images/7f537ca26914fe8a81643cd049bf1157d4d841f1cb52f14bf0715cb216a9c4bb.jpg)  
Fig. 5. Input error rate contribution to dominance (OR).

(Note that, while $O _ { N - 1 } ^ { a }$ is combined with $W _ { a }$ using conjunction, $I _ { j } ^ { a } ,$ $j = 1 , . . , N - 1$ may be combined using any sequence of conjunction and disjunction operations, and, moreover, statistical dependencies are not restricted within this variable subset as well as the associated error variables.) Under these conditions, dominance reversal can only happen if the difference between $P _ { U }$ and $P _ { V }$ is less than the difference between $p _ { D _ { U } }$ and $p _ { D _ { v } } \left( \mathrm { i } . \mathrm { e } . \right.$ , if the condition of Corollary 1 is not met) and, in addition, $p _ { D _ { \iota } }$ must be lower than $p _ { D _ { V } }$ . Low values of $p _ { U }$ and $P _ { V }$ can further limit the likelihood of dominance reversal. Evidently, the former conditions are satis<sup>fi</sup>ed in a small subset of the possible combinations of $P _ { U } , P _ { V } , p _ { D _ { l l ^ { \prime } } }$ , and $p _ { D _ { v } } .$

Likewise, $\operatorname { i f } V _ { a }$ and $U _ { a }$ are combined through disjunction and $W _ { a }$ is combined with $O _ { N - 1 } ^ { \mathrm { a } }$ through conjunction, then dominance reversal can only take place if the differences as above are, again, not too far apart, $\mathrm { i . e . , }$ the condition (15) of Corollary 1 is not met, and $\mathrm { i f } \ p _ { D _ { t I } }$ is higher than $p _ { D _ { \nu } }$

Proposition 3 implies largely comparable results for instances in which $W _ { a }$ is combined with the output of the remaining variables through disjunction. However, in these instances the other decision variables form a potential factor such that low values of $p _ { j } ^ { I } , p _ { j } ^ { F _ { I } } , j = 1 , . . ,$ $N - 1$ curb dominance reversal.

An extensive set of approximately 20,000 Monte Carlo simulations that have examined purely conjunctive and purely disjunctive decision rules found dominance reversal to be rare. These simulations, which considered decisions with up to ten input variables and employed random combinations of $p _ { U } , p _ { V } , p _ { D _ { U } } ,$ , and $p _ { D _ { v } }$ such that $p _ { D _ { U } } ,$ $p _ { D _ { v } } { \leq } 0 . 1$ , have shown dominance reversal in about 1% of the variable pairs in both types of decision rules. The <sup>fi</sup>ndings of these simulations are particularly meaningful since an upper boundary of 0.1 on $p _ { D _ { v } }$ and $p _ { D _ { \iota } }$ typically corresponds to a much higher boundary on the input error rates that drive such classi<sup>fi</sup>cation error rates. That boundary may be valid in most practical settings.

Proposition $\mathbf { 3 . } ^ { 2 }$ Let $U , V , D _ { U } ,$ and $D _ { V } ,$ be such that $V _ { a }$ dominates $U _ { a }$ in a single conjunction or disjunction operation. Let $I _ { j } , F _ { j } ^ { I } , j = 1 , . . , N - 1$ be such that $U , V , D _ { U } ,$ , and $D _ { V }$ are each independent of any subset of $I _ { j } , F _ { j } ^ { I } ,$ $j = 1 , . . , N - 1$ . Then, $V _ { a }$ dominates $U _ { a }$ in a sequence of N operations on $V _ { a } , U _ { a } ,$ and $I _ { j } ^ { a } , j = 1 , . . , N - 1 ,$ if:

1. U and V, as well as W and $O _ { N - 1 }$ , are combined through conjunction, and Eq. (18) or Eq. (19) or Eq. (20) holds true:

$$
\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}} \geq 2 (p _ {D _ {V}} - p _ {D _ {U}}) p _ {U} p _ {V}\tag{18}
$$

$$
p _ {D _ {U}} - p _ {D _ {V}} \geq 0\tag{19}
$$

$$
p _ {U} - p _ {V} > | p _ {D _ {V}} - p _ {D _ {U}} |\tag{20}
$$

2. U and V are combined through disjunction and W and $O _ { N - 1 }$ are combined through conjunction, and Eq. (21) or Eq. (22) or Eq. (23) holds true:

$$
\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}} \geq 2 (p _ {D _ {U}} - p _ {D _ {V}}) p _ {U} p _ {V}\tag{21}
$$

$$
p _ {D _ {V}} - p _ {D _ {U}} \geq 0\tag{22}
$$

$$
p _ {V} - p _ {U} > | p _ {D _ {U}} - p _ {D _ {V}} |\tag{23}
$$

3. U and V, as well as W and $O _ { N - 1 } ,$ are combined through disjunction, and Eq. (24) or Eq. (25) or Eq. (26) holds true:

$$
\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}} \geq 2 (p _ {D _ {V}} - p _ {D _ {U}}) p _ {U} p _ {V} \text {and} p _ {N - 1} ^ {O} + 2 p _ {N - 1} ^ {F _ {O}} \leq 1\tag{24}
$$

$$
p _ {D _ {U}} - p _ {D _ {V}} \geq 0 \text { and } p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {O}} \leq 1\tag{25}
$$

$$
p _ {V} - p _ {U} > 3 \left| \left(p _ {D _ {V}} - p _ {D _ {U}}\right) \right| \text {   and   } p _ {N - 1} ^ {O} + 2 p _ {N - 1} ^ {F _ {O}} \leq 1\tag{26}
$$

4. U and V are combined through conjunction and W and $O _ { N - 1 }$ are combined through disjunction, and Eq. (27) or Eq. (28) or Eq. (29) holds true.

$$
\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}} \geq 2 (p _ {D _ {U}} - p _ {D _ {V}}) p _ {U} p _ {V} \text { and } p _ {N - 1} ^ {O} + 2 p _ {N - 1} ^ {F _ {O}} \leq 1\tag{27}
$$

$$
p _ {D _ {V}} - p _ {D _ {U}} \geq 0 \text { and } p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {O}} \leq 1\tag{28}
$$

$$
p _ {U} - p _ {V} > 3 \left| \left(p _ {D _ {U}} - p _ {D _ {V}}\right) \right| \text { and } p _ {N - 1} ^ {O} + 2 p _ {N - 1} ^ {F _ {O}} \leq 1\tag{29}
$$

We can now return to the of<sup>fi</sup>ce rental decision example (Fig. 1). Proposition 3 instructs us that a dominance ranking of two variables that are connected through conjunction or disjunction is typically preserved throughout subsequent operations. This theory can be directly applied for ranking the rental rate, age of the of<sup>fi</sup>ce building, and square footage variables, since each of these variables is combined with any of the other two variables through a binary conjunction operation. Similarly, this theory can be employed for ranking the variables that are associated with the parking and public transportation hub, since these variables are combined through binary disjunction. However, our theory cannot be applied for ranking the rental rate relative to the parking data because these two variables are not directly linked by any operation. This limitation remains true for other variable pairs as well, e.g., the age of the of<sup>fi</sup>ce building and the parking data cannot be ranked. In conclusion, the usefulness of this dominance theory in complex decisions that employ both conjunction and disjunction is incomplete. Primarily, the order that it produces is partial.

## 7. Implications for data quality management

Studies indicate that the use of satis<sup>fi</sup>cing choice strategies is widespread, regardless of whether this strategy is applied for screening inferior choices or for singling out the best choice [45]. An important lesson of this study is that when a decision is obtained through a satis<sup>fi</sup>cing rule, inputs that exhibit the highest error rates are often not the inputs that are most damaging to the outcome of the decision.

Our error dominance theory implies a small set of simple guidelines for directing data quality management resource allocation decisions:

(1) When the percentage of values that satisfy the decision criterion varies signi<sup>fi</sup>cantly across two decision variables, efforts to achieve high decision accuracy under a conjunctive decision rule should assign a higher priority to the variable where a lower percentage of the values meet the criterion.

(2) When the percentage of values that satisfy the decision criterion varies signi<sup>fi</sup>cantly across two decision variables, efforts to achieve high decision accuracy under a disjunctive decision rule should assign a higher priority to the variable where a higher percentage of the values comply with the criterion.

These guidelines also hold true for the inputs of a binary conjunction or disjunction operation that forms part of a complex decision rule which may involve both conjunction and disjunction. However, as clari<sup>fi</sup>ed by this study, these guidelines may not be optimal when the input error rates are signi<sup>fi</sup>cantly far apart. In these cases, error rates may determine the dominance. As explained in Section $5 ,$ the general contribution of error rates is not intuitive. Primarily, the input with the lowest classi<sup>fi</sup>cation error rate can have the most detrimental effect on the decision:

(3) If two error rates are signi<sup>fi</sup>cantly far apart and the percentage of values that satisfy the decision criterion in each of the respective decision variables is not low, then efforts to achieve high decision accuracy under a conjunctive decision rule should assign a higher priority to the input that exhibits a higher error rate. If the error rates are signi<sup>fi</sup>cantly far apart and the former percentages are low, then efforts to achieve high decision accuracy under a conjunctive decision rule should assign a higher priority to the input that exhibits a lower error rate.

(4) If two error rates are signi<sup>fi</sup>cantly far apart and the percentage of values that satisfy the criterion in each of the respective decision variables is not high, then efforts to achieve high decision accuracy under a disjunctive decision rule should assign a higher priority to the input that exhibits a higher error rate. If the error rates are signi<sup>fi</sup>cantly far apart and the former percentages are high, then efforts to achieve high decision accuracy under a disjunctive decision rule should assign a higher priority to the input that exhibits a lower error rate.

As before, these prioritization strategies also hold true for the inputs of a binary conjunction or disjunction operation that forms part of a more complex decision rule which may involve both conjunction and disjunction. Whenever there is a doubt regarding the dominance ranking, Eqs. (7) and (8) and Eqs. (12) and (13) can assist in resolving the uncertainty.

A study of Eqs. (7) and (8) and Eqs. (12) and (13) implies that the damage of errors in a given input does not depend on the error rate of that input, but rather, on the error rate of the input to which it is compared $( \mathrm { e } . \mathrm { g } . , p _ { D _ { v } }$ is not mentioned in the Eq. (7) that determines the damage of errors in $V _ { a } ,$ but p is, in fact, mentioned there). An error rate can decrease or increase, but, all other things being equal,<sup>3</sup> that variation does not affect the damage that the errors produce. In contrast, the damage of the errors in other inputs is actually affected by such a change. Subsequently, the dominance ranking of two inputs may be reversed as a result of a decrease in the error rate of an input. The magnitude of the change that will produce this reversal, if at all possible, can be derived from the corollary of Proposition 1 or Proposition 2 or, otherwise, from the proposition itself.

The potential usefulness of this theory is not limited to data accuracy improvement. Traditional Systems Development Life Cycle (SDLC) [6] does not identify data quality improvement to be part of any stage. In reality, however, data quality improvement projects are often conducted when the system is already up and running. We believe that our theory can help at an earlier stage of the system's life cycle, particularly at the design stage, when data sources and acquisition methods are determined, and decisions about the way data are handled are made. Recent research that has explored a design framework that accounts for data quality supports the idea that choosing a source, for instance, is part of the design stage of a system's life cycle [22].

Information needs. While data quality assessment methods are outside the scope of this work, a growing number of studies explore such methods [37]. For example, [12,36], and [44] refer to the use of high quality data samples, while [26] considers a less costly data quality assessment through data mining. That approach detects errors through associations between different data. Mainly, deviations from these associations are perceived to be errors. Other common methods which are usually not too costly include user and expert evaluations [37]. Hence, for instance, the error rate of the of<sup>fi</sup>ce size data may be estimated through a comparison with public records. Alternatively, data mining techniques may prove to be useful when the of<sup>fi</sup>ce size is connected with other variables (e.g., with the location of the of<sup>fi</sup>ce). A more costly and potentially more accurate method would involve a survey of a sample of the properties. In order to determine if a recorded value in the sample set (e.g., 2590 ft<sup>2</sup>) is correct or incorrect, it can be compared to a physically measured value. Consider an example from a different problem domain: in a satis<sup>fi</sup>cing decision that uses a forecast of annual sales as one of the decision variables, if the actual sales are already known for a small number of months in the given year, then the error rate of the forecast for the whole year can be derived from that historical data.

However, an implementation of our theory requires acquiring, for each decision criterion, an estimate of the relevant classi<sup>fi</sup>cation error rate, rather than the raw data error rate. A recorded value would be considered accurate if it correctly satis<sup>fi</sup>es (or does not satisfy) the matching decision criterion. The method of estimating these error rates may be similar to the assessment of the original, raw error rates. For instance, in a decision that employs predictions of annual sales, a sample of actual sales data, as described earlier, can serve for deriving the classi<sup>fi</sup>cation error rate. In this way, an annual store sales forecast of 0.7 million dollars can be compared to the actual store sales data in order to determine if that store is correctly excluded from a marketing campaign that targets stores with predicted annual sales above 1 million dollars.

We may often avoid the need to assess those classi<sup>fi</sup>cation error rates and, instead, calculate dominance based on estimates of the raw data error rates. This may be achieved by exploiting the fact that the raw error rates form upper boundaries on the respective classi<sup>fi</sup>cation error rates. So, if, for instance, the error rate of the of<sup>fi</sup>ce size data is 3%, then, obviously, the matching classi<sup>fi</sup>cation error rate must be lower than, or, at most, equal to 3%. This boundary can be used in a calculation of the dominance ranking, making a more precise evaluation of the classi<sup>fi</sup>cation error rate redundant.

Implementation of our theory also requires, for each decision criterion, an estimate of the correct fraction of the values that meet the criterion. For example, in a marketing campaign that targets stores with predicted annual sales above 1 million dollars, a calculation of dominance would require an estimate of the fraction of the stores that meet the speci<sup>fi</sup>ed minimum sales threshold. This assessment may be carried in tandem with the evaluation of the corresponding error rate. Given that we have obtained historical data for the purpose of error rate measurement, those data can also be used for computing the fraction of the stores that satisfy the minimum sales criterion.

## 8. Limitations and future research directions

The <sup>fi</sup>ndings of this research imply that errors should not all be treated equally. Of course, if resources were unlimited, then ranking the effect of errors would be immaterial. Since resources are indeed often limited, the ability to set priorities while taking into account the intended use of the data can be valuable.

A signi<sup>fi</sup>cant limitation of our model is its statistical independence assumption (SIA) and the related assumptions of Proposition 3. Regrettably, statistical dependencies may be widespread. For example, we often face real-world settings where the probability of a false positive, when a value of the decision variable is incorrectly classi<sup>fi</sup>ed as ful<sup>fi</sup>lling the decision criterion, is different from the probability of a false negative, when a value of the decision variable is incorrectly classi<sup>fi</sup>ed as not ful<sup>fi</sup>lling the decision criterion. Another widespread phenomenon is dependence between decision variables. In the of<sup>fi</sup>ce rental scenario, for instance, we may therefore <sup>fi</sup>nd that the typical size of older properties is lower than the size of the newer properties that match the company's age prerequisite. Nonetheless, SIA prohibits such dependencies. Fortunately, our theory does not impose any statistical independence assumptions on the relationship between two inputs as long as these inputs are not the two inputs that are being ranked in relation to one another. Therefore, this theory may be applied selectively: inputs in input pairs that satisfy our independence requirements will be ranked in relation to one another, while the ranking of inputs in other input pairs will not be supported by this theory. A signi<sup>fi</sup>cant step towards minimizing the reliance on statistical independence assumptions has been made by a forthcoming extension of this theory, which designates data that serve multiple decision rules [3]. We focus on a set of decision variables that are utilized by many satis<sup>fi</sup>cing decisions, where the criteria that are tested against the decision variables vary across different decisions. The independence assumptions that this study employs are substantially weaker and may <sup>fi</sup>t many real-world scenarios.

This work also takes a partly unusual choice as far as the portrayal of the inputs of the decision and input errors. We avoid direct analysis of the original decision variables. Instead, we explore the dichotomous variables that are derived from the decision variables. Input errors, accordingly, are errors in the dichotomous variables, rather than errors in the decision variables. These deviations from common conceptions may create inconvenience for practical implementation. On the other hand, they simplify the analysis, and, in addition, the resultant theory is valid regardless of the special characteristics of the decision variables. The results of this work may be integrated in the future with models that link the raw data errors with the errors as considered here. As the earlier discussion on implementation has suggested, the raw input error rates may be redundant. Therefore, this theory can be useful despite its departure from the ordinary interpretation.

Another limitation of our dominance theory, and consequently, the guidelines based on that theory, is its focus on a single consideration, namely, the effect of input errors on output accuracy. In practice, additional factors may affect the ranking of different inputs in a resource allocation decision. For example, one possible factor is the cost of producing accurate data. That cost can vary substantially among different inputs, such that accounting for this variation may be desirable. Another example in this class is the cost of assessing input accuracy, which may, again, vary among different inputs. A different example that is not addressed by the current model is the perceived importance of distinct decision variables, which may not always be uniform. These limitations of the error dominance theory may be partially alleviated by reverting to the model on which this theory is based. Especially, Eqs. (7) and (8) and Eqs. (12) and (13) can be embedded in a broader model which accounts for additional factors. Evidently, a major disadvantage of a ranking relative to a full-<sup>fl</sup>edged quantitative measure is that a ranking may not enable a broad quantitative assessment, i.e., an assessment that accounts for the damage as well as other relevant factors.

This dominance theory also ignores the common distinction between error type 1 and error type 2. A false positive decision may have substantially different implications from a false negative decision. The costs of these two error types can vary considerably. Future work will account for that variation as well.

Finally, there is a need to conduct studies that validate this theory empirically. Initial validation, aiming to ensure the correctness of the analysis, has been partly accomplished. This step has performed a series of Monte-Carlo simulations (some results are described in [4]). However, there is a need to continue this research and validate this dominance theory through additional simulations and, unquestionably, in real-life settings. Studies in real-life settings should clarify the magnitude of the challenge of obtaining the requisite parameter measurement, and how well this model <sup>fi</sup>ts users' perceptions and considerations as well as the underlying data characteristics.

## Appendix A. Mathematical proofs

Proof of Lemma 1. Using Eqs. (1), (2), (4), and (5), we derive from Eq. (3), that:

$$
\begin{array}{r} D _ {W} = (U D _ {V} - 2 U V D _ {V} + V D _ {U} - 2 U V D _ {U} + D _ {U} D _ {V} - 2 V D _ {U} D _ {V} \\ - 2 U D _ {U} D _ {V} + 4 U V D _ {U} D _ {V}) / (1 - 2 U V) \end{array}\tag{A.1}
$$

We show that:

$$
\begin{array}{c} (U D _ {V} - 2 U V D _ {V} + V D _ {U} - 2 U V D _ {U} + D _ {U} D _ {V} - 2 V D _ {U} D _ {V} - 2 U D _ {U} D _ {V} + 4 U V D _ {U} D _ {V}) \\ \div (1 - 2 U V) = V D _ {U} + U D _ {V} + D _ {U} D _ {V} - 2 U D _ {U} D _ {V} - 2 V D _ {U} D _ {V} + 2 U V D _ {U} D _ {V} \end{array}\tag{A.2}
$$

by calculating the value of the left-hand-side expression of Eq. (A.2) and the value of the right-hand-side expression of Eq. (A.2) given each of the possible variable-value combinations, and demonstrating that the expressions always have the same value.

<table><tr><td> $D_U$ </td><td> $D_V$ </td><td>U</td><td>V</td><td>LHS of (A.2)</td><td>RHS of (A.2)</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

It follows that:

$$
\begin{array}{r l} p _ {D _ {W}} = E (D _ {W}) & = E ((U D _ {V} - 2 U V D _ {V} + V D _ {U} - 2 U V D _ {U} + D _ {U} D _ {V} \\ & \quad - 2 V D _ {U} D _ {V} - 2 U D _ {U} D _ {V} + 4 U V D _ {U} D _ {V}) / (1 - 2 U V)) \\ & = E (V D _ {U} + U D _ {V} + D _ {U} D _ {V} - 2 U D _ {U} D _ {V} - 2 V D _ {U} D _ {V} + 2 U V D _ {U} D _ {V}) \\ & = E (V D _ {U}) + E (U D _ {V}) + E (D _ {U} D _ {V}) - 2 E (U D _ {U} D _ {V}) - 2 E (V D _ {U} D _ {V}) \\ & \quad + 2 E (U V D _ {U} D _ {V}). \end{array} \tag {A.3}
$$

Due to SIA, Eq. (6) follows immediately. End of proof.

Proof of Lemma 2. Using Eqs. (1), (2), (9), and (10), we derive from Eq. (3) that:

$$
\begin{array}{r} D _ {W} = (D _ {U} + D _ {V} - 2 U D _ {U} - 2 V D _ {V} - U D _ {V} - V D _ {U} - D _ {U} D _ {V} + 2 U V D _ {V} + 2 U V D _ {U} \\ + 2 U D _ {U} D _ {V} + 2 V D _ {U} D _ {V} - 4 U V D _ {U} D _ {V}) / (1 - 2 (U + V - U V)) \quad (\mathrm{A.4}) \end{array}
$$

We show that:

$$
\begin{array}{r l} & (D _ {U} + D _ {V} - 2 U D _ {U} - 2 V D _ {V} - U D _ {V} - V D _ {U} - D _ {U} D _ {V} + 2 U V D _ {V} + 2 U V D _ {U}) \\ & \quad + 2 U D _ {U} D _ {V} + 2 V D _ {U} D _ {V} - 4 U V D _ {U} D _ {V}) / (1 - 2 (U + V - U V)) \\ & \quad = D _ {U} + D _ {V} - U D _ {V} - V D _ {U} - D _ {U} D _ {V} + 2 U V D _ {U} D _ {V} \end{array}\tag{A.5}
$$

by calculating the value of the left-hand-side expression of Eq. (A.5) and the value of the right-hand-side expression of Eq. (A.5) given each of the possible variable–value combinations, and demonstrating that the expressions have the same value.

<table><tr><td> $D_U$ </td><td> $D_V$ </td><td>U</td><td>V</td><td>LHS of (A.5)</td><td>RHS of (A.5)</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

It follows that:

$$
\begin{array}{r l} & p _ {D _ {W}} = E (D _ {W}) = E ((D _ {U} + D _ {V} - 2 U D _ {U} - 2 V D _ {V} - U D _ {V} - V D _ {U} - D _ {U} D _ {V} \\ & \qquad + 2 U V D _ {V} + 2 U V D _ {U} + 2 U D _ {U} D _ {V} + 2 V D _ {U} D _ {V} - 4 U V D _ {U} D _ {V}) \\ & \qquad \div (1 - 2 (U + V - U V))) \\ & = E (D _ {U} + D _ {V} - U D _ {V} - V D _ {U} - D _ {U} D _ {V} + 2 U V D _ {U} D _ {V}) = E (D _ {U}) \\ & \qquad + E (D _ {V}) - E (U D _ {V}) - E (V D _ {U}) - E (D _ {U} D _ {V}) + 2 E (U V D _ {U} D _ {V}) \end{array}\tag{A.6}
$$

Due to SIA, Eq. (11) follows immediately. End of proof.

Proof of Proposition 3. Assume $\operatorname { E q . }$ (18). Eq. (A.3) shows that:

$$
\begin{array}{c} p _ {D _ {W}} = E (V D _ {W}) = E (V D _ {U}) + E (U D _ {V}) + E (D _ {U} D _ {V}) - 2 E (U D _ {U} D _ {V}) \\ - 2 E (V D _ {U} D _ {V}) + 2 E (U V D _ {U} D _ {V}). \end{array}
$$

Likewise, based on Eq. (A.3) and the commutative and associative properties of conjunction, we derive the probability of error of a decision rule based on all the $N + 1$ inputs:

$$
\begin{array}{r} p _ {N + 1} ^ {F _ {0}} = E (W F _ {N - 1} ^ {O}) + E (O _ {N - 1} D _ {W}) + E (D _ {W} F _ {N - 1} ^ {O}) - 2 E (O _ {N - 1} D _ {W} F _ {N - 1} ^ {O}) \\ - 2 E (W D _ {W} F _ {N - 1} ^ {O}) + 2 E (O _ {N - 1} W D _ {W} F _ {N - 1} ^ {O}), \end{array}
$$

where $O _ { N - 1 }$ is the output of a decision rule which combines $I _ { 1 } , I _ { 2 } , \ldots$ and $I _ { N - 1 } ,$ , and $F _ { N - 1 } ^ { O }$ is the matching decision error. A quick calculation shows that, despite SIA, $\mathsf { E } ( W D _ { W } ) \neq P _ { W } p _ { D _ { W } } , \mathsf { i . e . }$ , W and $D _ { W }$ are not statistically independent. When U and V are combined through conjunction, then, assuming SIA, $E ( W D _ { W } ) = p _ { U } p _ { V } ( p _ { D _ { U } } + p _ { D _ { V } } - p _ { D _ { U } } p _ { D _ { V } } )$ while $p _ { { W } } p _ { { D _ { v } } }$ is captured by the product of Eq. (6) and p<sub>U</sub>p<sub>V</sub>.

Therefore, using SIA, we re-express $p _ { N + 1 } ^ { F o }$ as:

$$
\begin{array}{r} p _ {N + 1} ^ {F _ {o}} = p _ {W} p _ {N - 1} ^ {F _ {o}} + p _ {D _ {W}} \cdot \{p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {o}} - 2 E (O _ {N - 1} F _ {N - 1} ^ {O}) \} \\ - 2 p _ {U} p _ {V} (p _ {D _ {U}} + p _ {D _ {V}} - p _ {D _ {U}} p _ {D _ {V}}) \cdot \{p _ {N - 1} ^ {F _ {o}} - E (O _ {N - 1} F _ {N - 1} ^ {O}) \}. \end{array}
$$

It follows that $\partial p _ { N + 1 } ^ { F _ { 0 } } / \partial p _ { D _ { \nu } }$ is given by:

$$
\begin{array}{c} \partial p _ {N + 1} ^ {F _ {0}} / \partial p _ {D _ {v}} = \partial p _ {D _ {w}} / \partial p _ {D _ {v}} \cdot \{p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {0}} - 2 E (O _ {N - 1} F _ {N - 1} ^ {O}) \} \\ - 2 p _ {U} p _ {V} (1 - p _ {D _ {U}}) \cdot \{p _ {N - 1} ^ {F _ {0}} - E (O _ {N - 1} F _ {N - 1} ^ {O}) \} \end{array}
$$

Similarly:

$$
\begin{array}{r l} & {\partial p _ {N + 1} ^ {F _ {0}} / \partial p _ {D _ {U}} = \partial p _ {D _ {W}} / \partial p _ {D _ {U}} \cdot \{p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {0}} - 2 E (O _ {N - 1} F _ {N - 1} ^ {O}) \}} \\ & {- 2 p _ {U} p _ {V} (1 - p _ {D _ {V}}) \cdot \{p _ {N - 1} ^ {F _ {0}} - E (O _ {N - 1} F _ {N - 1} ^ {O}) \}.} \end{array}
$$

By subtracting $\partial p _ { N + 1 } ^ { F _ { O } } / \partial p _ { D _ { U } }$ from $\partial p _ { N + 1 } ^ { F o } / \partial p _ { D _ { \nu } }$ we obtain:

$$
\begin{array}{r l} & {\partial p _ {N + 1} ^ {F _ {0}} / \partial p _ {D _ {v}} - \partial p _ {N + 1} ^ {F _ {0}} / \partial p _ {D _ {u}} = (\partial p _ {D _ {w}} / \partial p _ {D _ {v}} - \partial p _ {D _ {w}} / \partial p _ {D _ {u}})} \\ & {\qquad \times \{p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {0}} - 2 E (O _ {N - 1} F _ {N - 1} ^ {O}) \} - 2 p _ {U} p _ {V} (p _ {D _ {v}} - p _ {D _ {u}})} \\ & {\qquad \times \{p _ {N - 1} ^ {F _ {0}} - E (O _ {N - 1} F _ {N - 1} ^ {O}) \}.} \end{array}
$$

Since we assume that $V _ { a }$ dominates $U _ { a }$ in a single operation, it follows that $\partial p _ { D _ { w } } / \partial p _ { D _ { v } } - \partial p _ { D _ { w } } / \partial p _ { D _ { t } } \ne 0$ . Therefore, there exists ε such that $p _ { U } p _ { V } ( p _ { D _ { v } } - p _ { D _ { U } } ) = \varepsilon ( \partial ( p _ { D _ { w } } / \partial p _ { D _ { v } } - \partial p _ { D _ { w } } / \partial p _ { D _ { U } } )$ . Therefore:

$$
\begin{array}{l} \partial p _ {N + 1} ^ {F _ {0}} / \partial p _ {D _ {V}} - \partial p _ {N + 1} ^ {F _ {0}} / \partial p _ {D _ {U}} = (\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}}) \\ \quad \times \{p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {0}} - 2 E (O _ {N - 1} F _ {N - 1} ^ {O}) \} - 2 \varepsilon \cdot (\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}}) \\ \quad \times \{p _ {N - 1} ^ {F _ {0}} - E (O _ {N - 1} F _ {N - 1} ^ {O}) \} = (\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}}) \\ \quad \times \{p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {0}} - 2 E (O _ {N - 1} F _ {N - 2} ^ {O}) - 2 \varepsilon \cdot [ p _ {N - 1} ^ {F _ {0}} - E (O _ {N - 1} F _ {N - 1} ^ {O}) ] \} \\ = (\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}}) \cdot \{p _ {N - 1} ^ {O} + p _ {N - 1} ^ {F _ {0}} (1 - 2 \varepsilon) \\ \quad - E (O _ {N - 1} F _ {N - 1} ^ {O}) (2 - 2 \varepsilon) \} \end{array}
$$

Since $E ( { \cal O } _ { N - 1 } F _ { N - 1 } ^ { O } ) \leq \operatorname* { m i n } \{ p _ { N - 1 } ^ { O } , \ : P _ { N } ^ { F _ { O } } - 1 \} ,$ , it is easy to see that, if $\varepsilon \le 0 . 5$ , then $\{ p _ { N - 1 } ^ { o } , \ P _ { N } \ _ { - 1 } + ^ { F _ { o } } ( 1 - 2 \varepsilon ) - \mathrm { E } ( O _ { N - 1 } F _ { N - 1 } ^ { o } ) ( 2 - 2 \varepsilon ) \} \ge 0 .$ Therefore, if $\varepsilon \le 0 . 5 ,$ , i.e., if Eq. (18) holds true, then: $\partial p _ { D _ { W } } / \partial p _ { D _ { V } } -$ $\partial p _ { D _ { w } } / \partial p _ { D _ { u } } > 0 \partial p _ { N + 1 } ^ { F _ { o } } / \partial p _ { D _ { v } } - \partial p _ { N + 1 } ^ { F _ { o } } / \partial p _ { D _ { U } } \geq 0 .$ . End of proof.

• Assume Eq. (19). Consider, again, the equation that we used in the <sup>fi</sup>rst part of this proof (Eq. (18)), i.e., $\ L _ { U } p _ { V } ( p _ { D _ { V } } - p _ { D _ { U } } ) = \varepsilon ( \partial p _ { D _ { W } } / \partial p _ { D _ { V } } -$ $\partial p _ { D _ { W } } / \partial p _ { D _ { U } } )$ . Since, by assumption, $V _ { a }$ dominates $U _ { a }$ in a single operation , $\partial p _ { D _ { w } } / \partial p _ { D _ { v } } - \partial p _ { D _ { w } } / \partial p _ { D _ { v } } > 0$ . Since, by assumption, $p _ { D _ { U } } -$ $p _ { D _ { v } = 0 }$ , it follows that ε≤0. Therefore, $\varepsilon \le 0 . 5$ . Therefore, using Eq. (18), Proposition 3 implies that $\partial p _ { N + 1 } ^ { \mathrm { F } _ { o } } / \partial p _ { D _ { v } } - \partial p _ { N + 1 } ^ { \mathrm { F } _ { o } } / \partial p _ { D _ { U } } 2 0$ . End of proof.

Assume Eq. (20). Suppose that $p _ { U } - p _ { V } { > } | p _ { D _ { v } } - p _ { D _ { U } } |$ . Using Eqs. (7) and (8), and the laws of probability:

$$
\begin{array}{r l} & {\partial p _ {D _ {W}} / \partial p _ {D _ {V}} - \partial p _ {D _ {W}} / \partial p _ {D _ {U}} = (p _ {U} - p _ {V}) + (p _ {D _ {U}} - p _ {D _ {V}}) - 2 (p _ {D _ {U}} - p _ {D _ {V}})} \\ & {\qquad \times (p _ {U} + p _ {V} - p _ {V} p _ {U}) > | (p _ {D _ {V}} - p _ {D _ {U}}) | - (p _ {D _ {V}} - p _ {D _ {U}})} \\ & {\qquad + 2 (p _ {D _ {V}} - p _ {D _ {U}}) (p _ {U} + p _ {V} - p _ {V} p _ {U}) \geq 2 (p _ {D _ {V}} - p _ {D _ {U}})} \\ & {\qquad \times (p _ {U} + p _ {V} - p _ {V} p _ {U}) \geq 2 p _ {U} p _ {V} (p _ {D _ {V}} - p _ {D _ {U}})} \end{array}
$$

It follows that we can apply the proof of Proposition 3 with respect to Eq. (18). End of proof.

## References

[1] D.J. Aigner, Regression with a binary independent variable subject to errors of observation, Journal of Econometrics 1 (4) (1973).

[2] I. Askira Gelman, GIGO or not GIGO: The Accuracy of Multi-Criteria, Satis<sup>fi</sup>cing Decisions. ACM Journal of Data and Information Quality (ACM JDIQ). in press.

[3] I. Askira Gelman, A model of error propagation in satis<sup>fi</sup>cing decisions and its application to database quality management, Proc. 14<sup>th</sup> American Conference on Information Systems (AMCIS 2008), Toronto, Canada, 2008.

[4] I. Askira Gelman, Simulations of error propagation for prioritizing data accuracy improvements in multi-criteria satis<sup>fi</sup>cing decision making scenarios, $3 0 ^ { \mathrm { { i h } } }$ International Conference on Information Systems (ICIS-09). Phoenix, Arizona 2009.

[5] A. Avenali, C. Batini, P. Bertolazzi, P. Missier, Brokering infrastructure for minimum cost data procurement based on quality–quantity models, Decision Support Systems 45 (1) (2008).

[6] D. Avison, G. Fitzgerald, Information systems development: methodologies, techniques and tools, McGraw-Hill Education, Maidenhead, 2008.

[7] D.P. Ballou, H.L. Pazer, Modeling data and process quality in multi-input, multioutput information systems, Management Science 31 (2) (1985).

[8] D.P. Ballou, H.L. Pazer, S. Belardo, B.D. Klein, Implications of data quality for spreadsheet analysis, DATA BASE 18 (3) (1987).

[9] D.P. Ballou, H.L. Pazer, A framework for the analysis of error in conjunctive, multicriteria, satis<sup>fi</sup>cing decision processes, Decision Sciences 21 (4) (1990).

[10] D.P. Ballou, G.K. Tayi, Methodology for allocating resources for data quality enhancement, Communications of the ACM 32 (3) (1989).

[11] D.P. Ballou, H.L. Pazer, G.K. Tayi, R.Y. Wang, Modeling information manufacturing systems to determine information product quality, Management Science 44 (4) (1998).

[12] D.P. Ballou, I.N. Chengalur-Smith, R.Y. Wang, Sample-based quality estimation of query results in relational database environments, IEEE Transactions on Knowledge and Data Engineering 18 (5) (2006).

[13] T.L. Barabash, On properties of symbol recognition, Engineering Cybernetic (Sept./Oct. 1965).

[14] P.R. Bevington, Data Reduction and Error Analysis for the Physical Sciences, Ch. 4, McGraw-Hill, New York, 1969.

[15] R.T. Clemen, R.L. Winkler, Limits for the precision and value of information from dependent sources, Operations Research 33 (2) (1985).

[16] Nicolas Caritat de Condorcet, Essai sur l'application de l'analyse a la probabilité des décision rendues à la pluralité des voix (Paris, 1785).

[17] T. Cover, The best two independent measurements are not the two best, IEEE Transactions on Systems, Man and Cybernetics SMC-4 (1) (1974).

[18] B.E. Cushing, A mathematical approach to the analysis and design of internal control systems, Accounting Review 49 (1) (1974).

[19] H.J. Einhorn, The use of nonlinear, noncompensatory models in decision making, Psychological Bulletin 73 (3) (1970).

[20] H.J. Einhorn, The use of nonlinear, noncompensatory models as a function of task and amount of information, Organizational Behavior and Human Performance 6 (1) (1971).

[21] H.J. Einhorn, Expert measurement and mechanical combination, Organizational Behavior and Human Performance 7 (1972).

[22] A. Even, G. Shankaranarayan, P.D. Berger, Economics driven data management: an application to the design of tabular data sets JEEE Transactions on Knowledge and Data Engineering 19 (6) (2007)

[23] A.G. Frantsuz, In<sup>fl</sup>uence of correlations between attributes on their informativeness for pattern recognition, Engineering Cybernetics 4 (July-Aug 1967).

[24] L.A. Goodman, On the exact variance of products, Journal of the American Statistical Association 55 (292) (1960).

[25] B. Grofman, G. Owen, S.L. Feld, Thirteen theorems in search of the truth, Theory and Decision 15 (1983).

[26] J. Hipp, U. Guntzer, G. Grimmer, Data quality mining: making a virtue of necessity, Proceedings of the 6<sup>th</sup> ACM SIGMOD Workshop on Research Issues in Data Mining and Knowledge Discovery (DMKD 2001), 2001.

[27] M. Janson, Data quality: the Achilles heel of end-user computing, Omega: International Journal of Management Science 16 (5) (1988).

[28] J.M. Juran, Juran on planning for quality, The Free Press, New York, 1988.

[29] B.D. Klein, D.F. Rossin, Data quality in linear regression models: effect of errors in test data and errors in training data on predictive accuracy, Informing Science 2 (2) (1999).

[30] B.D. Klein, D.F. Rossin, Data quality in neural network models: effect of error rate and magnitude of error on predictive accuracy, Omega 27 (5) (1999).

[31] L.I. Kuncheva, C.J. Whitaker, Measures of diversity in classi<sup>fi</sup>er ensembles and their relationship with the ensemble accuracy, Machine Learning 51 (2003).

[32] K.K. Ladha, The Condorcet Jury Theorem, free speech, and correlated votes, American Journal of Political Science 36 (1992).

[33] Y. Lee, D. Strong, B. Kahn, R. Wang, AIMQ: a methodology for information quality assessment, Information and Management 40 (2) (2002).

[34] D.A. Lussier, R.W. Olshavsky, Task complexity and contingent processing in brand choice, The Journal of Consumer Research 6 (2) (1979)

[35] A. Mintz, How do leaders make decisions? A poliheuristic perspective, Journal of Con<sup>fl</sup>ict Resolution 48 (1) (2004).

[36] A. Motro, I. Rakov, Not all answers are equally good: estimating the quality of database answers, in: T. Andreasen, H. Christiansen, H.L. Larsen (Eds.), Flexible Query-Answering Systems, Kluwer Academic Publishers, 1997, pp. 1–21.

[37] F. Naumann, C. Rolker, Assessment methods for information quality criteria, Proceeding of the 5<sup>th</sup> International Conference on Information Quality (ICIQ-2000), 2000.

[38] F. Naumann, J.C. Freytag, U. Leser, Completeness of integrated information sources, Information Systems 29 (7) (2004).

[39] P.M. Neely, The product approach to data quality and <sup>fi</sup>tness for use: a framework for analysis, Proc. 10th Int'l Conf. Information Quality, 2005, pp. 52–67.

[40] V. Oven, D. Pekdemir, Of<sup>fi</sup>ce rent determinants utilising factor analysis — a case study for Istanbul, The Journal for Real Estate Finance and Economics 33 (1) (2006).

[41] C.W. Park, The effect of individual and situation-related factors on consumer selection of judgmental models, Journal of Marketing Research 13 (2) (1976).

[42] K. Parsaye, M. Chignell, Data quality control with SMART databases, AI Expert 8 (5) (1993).

[43] A. Parssian, S. Sarkar, S.J. Varghese, Assessing data quality for information products: impact of selection, projection, and Cartesian product, Management Science 50 (7) (2004).

[44] A. Parssian, Managerial decision support with knowledge of accuracy and completeness of the relational aggregate functions, Decision Support Systems 42 (3) (2006).

[45] J.W. Payne, Task complexity and contingent processing in decision making: an information search and protocol analysis, Organizational Behavior and Human Performance 16 (1976).

[46] A.G. Phipps, Utility function switching during residential search, Geogra<sup>fi</sup>ska Annaler. Series B, Human Geography 65 (1) (1983).

[47] L. Pipino, Y.W. Lee, R.Y. Wang, Data quality assessment, Communications of the ACM 45 (4) (2002).

[48] M. Scannapieco, C. Batini, Completeness in the relational model: a comprehensive framework, Proceeding of the 9<sup>th</sup> International Conference on Information Quality (ICIQ-2004), 2004.

[49] G. Shankaranarayan, M. Zaid, R.Y. Wang, Managing data quality in dynamic decision environments: an information product approach, Journal of Database Management 14 (4) (2003).

[50] H.A. Simon, Models of Man: Social and Rational, John Wiley and Sons, Inc, 1957.

[51] R. Sivitanidou, Do of<sup>fi</sup>ce-commercial <sup>fi</sup>rms value access to service employment centers? A hedonic value analysis within polycentric Los Angeles, Journal of Urban Economics 40 (1996)

[52] W.O. Stratton, Accounting systems: the reliability approach to internal control evaluation, Decision Sciences 12 (1) (1981).

[53] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996).

[54] R.W. Wang, M. Ziad, Y.W. Lee, Data Quality, Springer, 2001.

[55] S. Yu, J. Neter, A stochastic model of the internal control system, Journal of Accounting Research 11 (2) (1973).

Irit Askira Gelman is a visiting scholar at the University of Arizona. She received her B.Sc in Mathematics from Tel Aviv University, Israel, M.Sc. in Information Systems from Tel Aviv University, and Ph.D. in Management Information Systems from the University of Arizona. She is a member of JEEE and AIS. Her research interests include data and informatior quality, knowledge discovery and data mining, and model management systems.
