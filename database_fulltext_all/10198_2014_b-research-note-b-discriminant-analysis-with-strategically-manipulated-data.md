---
otero_id: 10198
otero_key: "PRPEHZJ3"
title: "<b>Research Note</b>—Discriminant Analysis with Strategically Manipulated Data"
authors: "Juheng Zhang; Haldun Aytug; Gary J. Koehler"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0526"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/PRPEHZJ3/fulltext/images/911331591cb3945d751d0e54c5f8c467e480b2918ad6461900d9bee8f1a2416b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Note—Discriminant Analysis with Strategically Manipulated Data

Juheng Zhang, Haldun Aytug, Gary J. Koehler

## To cite this article:

Juheng Zhang, Haldun Aytug, Gary J. Koehler (2014) Research Note—Discriminant Analysis with Strategically Manipulated Data. Information Systems Research 25(3):654-662. http://dx.doi.org/10.1287/isre.2014.0526

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/PRPEHZJ3/fulltext/images/30f0cd7a773272f03d03919a27a8b8ab7a0e5f2c4a5b7c2079a6c61bf8600cf8.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Discriminant Analysis with Strategically Manipulated Data

Juheng Zhang

Department of Operations and Information Systems, Manning School of Business, University of Massachusetts Lowell, Lowell, Massachusetts 01854, juheng\_zhang@uml.edu

Haldun Aytug, Gary J. Koehler

Department of Information Systems and Operations Management, Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611 {aytugh@ufl.edu, koehler@ufl.edu}

W<sup>e</sup> <sup>study</sup> <sup>the</sup> <sup>problem</sup> <sup>where</sup> <sup>a</sup> <sup>decision</sup> <sup>maker</sup> <sup>uses</sup> <sup>a</sup> <sup>linear</sup> <sup>classifier</sup> <sup>over</sup> <sup>attribute</sup> <sup>values</sup> <sup>(e.g.,</sup> <sup>age,</sup> <sup>income,</sup> etc.) to classify agents into classes (e.g., creditworthy or not). Sometimes the attribute values are altered and/or hidden by agents to obtain a favorable but undeserved classification. Our main goal is to develop methods to thwart agents from hiding or distorting attribute values to obtain a favorable but incorrect classification. Intentionally altered attributes to obtain strategic goals have been studied. In this paper we develop methods that handle strategic hiding (i.e., nondisclosure) and then merge them with methods to thwart strategic distortion in the context of classification.

Keywords: classification; support vector machines; data imputation; missing values; adversarial learning; strategically hidden information

History: Vijay Mookerjee, Senior Editor; Kai-Lung Hui, Associate Editor. This paper was received on December 11, 2012, and was with the authors 8 months for 3 revisions. Published online in Articles in Advance July 14, 2014.

## 1. Introduction

In many situations, decisions are made based on data collected from intelligent individuals (who we call agents). When certain decision outcomes are preferred, individuals may act strategically when providing information. This behavior, which we call strategic manipulation, has been studied in the context of classification (e.g., Dalvi et al. 2004, Boylu et al. 2010, Dekel et al. 2010). In this context, the decision maker (the principal) uses rules to assign agents to classes. Our work extends earlier work of Boylu et al. (2010). Whereas they focus on information distortion (i.e., altering true values) we study how information hiding impacts the classification problems with or without distortion. Like them, we consider a two-class problem, positive versus negative, where agents prefer to be classified positive.

Examples of strategic manipulation exists in many domains. Online sellers often choose to publish only information favorable to themselves while concealing information that might diminish their attractiveness to a buyer (Ba 2001, Baron 2002). Credit applicants may choose not to disclose past financial problems or change their spending habits prior to applying for a loan only to revert back to their normal practices after they obtain the loan. Limited disclosure is also common in financial markets (Healy and Palepu 2001, Hirshleifer and Teoh 2003). Other examples may be found in job recruiting (Goldberg 2010), insurance approval (Insure.com 2010), school applications (Braun et al. 2010), and second-hand markets (Akerlof 1970). Ignoring such strategic activities, the decision maker would incur misclassifications. The principal should anticipate such activities and create a classifier that can thwart actions that might lead to misclassifications.

Most often we see that negative agents hide/alter information intentionally, but positive agents have incentives to reveal information strategically too. For instance, regardless of being trustworthy or not, sellers may choose not to reveal the place of production of a product because consumers may have concerns on the origin of production. A college applicant who is academically qualified may selectively include information in his application package. A credit applicant with good credit and sufficient salary may choose not to divulge all sources of income to show he is eligible because it requires effort to gather and document each item. A job candidate with good qualifications may choose not to provide the exact number of references requested because it takes effort to collect them and he may not have time to vet the potential individuals. Job applicants may also choose to exaggerate past accomplishments and not reveal their past negative performance evaluations. In all of these examples, the underlying fact is that these agents are very strong along many dimensions (perhaps with some distortion)

yielding more than enough information to guarantee a positive labeling.

There are two types of attribute hiding a principal might consider. In the first type, there is a specific attribute value that is unreported by an agent. For example, a job applicant may not answer a question such as “Do you have an arrest record?” A second type of hiding occurs when a principal cannot judge a value to be missing. For example, a medical insurance applicant may not list certain illnesses to a question asking for all past illnesses. In such cases, the principal can enumerate all illnesses of interest and ask a specific question for each. Throughout, we assume all cases of hiding are of the first type.

For a more concrete example, consider the following situation. A company advertises for a mid-level management position. Interested people (agents) are asked to fill out a form and submit their resumes. The hiring manager (principal), through past experience, has a good idea of what a qualified agent looks like and has a basic scoring function she uses. The principal’s job is to select a set of qualified applicants that can be scrutinized further. We assume each job posting has enough detail so that each agent can reasonably guess his chances of being hired and what they can do to improve their chances. Clearly, being hired has some fixed utility to the agent. The agent will apply if the expected utility he extracts from being hired is greater than the effort required to apply.

We anticipate three scenarios that define the behavior of agents for this job posting:

Type 1 (overqualified). Suppose an agent is overqualified. Once he inspects the requirements of the application process he realizes that applying is not in his best interest. This is an example of someone with years of executive experience looking at a mid-level job.

Type 2 (good fit). In this case the agent is qualified. He believes he will extract a positive net utility if he applies and is hired.

Type 3 (un[der] qualified). In this case the agent believes he is not qualified (perhaps because of a firing at a previous employment) or under-qualified (e.g., due to limited experience or education for the position). However, he thinks he will extract positive net utility if he gets hired. So if he applies he might distort or hide details about himself.

Given enough incentive, any agent may choose to exaggerate his experiences (i.e., distort) and/or hide certain facts about his background (e.g., he may not disclose a past negative evaluation and merely not answer a question asking such) to look more positive or to reduce the cost of revealing information. The scoring function of the principal has to handle the fact that agents might have exaggerated some accomplishments or have hidden certain facts.

We will refer to this example throughout the manuscript as the hiring example. Agents whose scores are at or close to the principal’s decision threshold will be called marginal agents. Those who have very high or low scores will be called highly positive and highly negative agents, respectively.

Since agents may engage in strategic activity to confuse a principal by altering or hiding attribute values, it behooves the principal to anticipate such activity in her induction process to learn a classifier. The principal’s options are (1) to uncover missing information and/or detect distortion of attributes, (2) not to include those agents with missing information in the classification, or (3) find a way to thwart such agent activities. As mentioned above, we are interested in studying option (3).

In this study, we use notation similar to that of Boylu et al. (2010). Given any observation of n realvalued agent attributes, $x \in \Re ^ { n } .$ , the principal uses a linear discriminant function (LDF) 4w1 b5, where $w \in \Re ^ { n }$ and b is a scalar, to determine the class of $x \in \Re ^ { n }$ by the rule if $w ^ { \prime } x + b \geq z$ (where the critical value z is usually zero or one) then x is labeled positive (+1) and negative otherwise (−1). The classification rule $( w , b ) \colon \bar { \mathfrak { M } } ^ { n }  \{ - 1 , + 1 \}$ is usually learned from a collection of examples with known class labels (this collection is called a training sample). The training sample is denoted as $S = \{ ( x _ { i } , { \bar { y } } _ { i } ) , i { = } 1 , \dots , l \}$ , where l is the number of observations, the ith observation is $x _ { i } \in \Re ^ { n } .$ , and $y _ { i } \in \{ - 1 , + 1 \}$ denotes observation $i ^ { \prime } \mathrm { s }$ true class label; S is drawn randomly (independent and identically distributed with replacement) from the instance space $X \subseteq { \mathfrak { N } } ^ { n }$ of possible observations.

Boylu et al. (2008, 2010) focus on finding a classifier that minimizes the classification risk while anticipating that agents alter (rather than hide) their characteristics strategically. They show that a classifier created from unaltered data can be scaled and shifted to thwart distortion. Clearly, their results cannot be used if attributes have missing data. With strategically hidden information, the principal needs to impute missing data before classifying agents.

Another study, by Dekel et al. (2010), is perhaps the closest to our work. Our model makes some similar assumptions (described below) but has important differences. The three most important distinctions are how Dekel et al. (2010) define missing values, how they treat missing values, and how existing values are distorted. They treat missing values as randomly chosen values. Our missing attribute values are simply not disclosed. We handle missing values by using an imputation method in conjunction with an LDF. Dekel et al. (2010) distort existing values randomly whereas we assume the agent strategically distorts values. In addition, our model allows agents to have different agent utilities and there is not a shared valuation of attribute values.

In the next section, we provide a formulation of the overall problem where the agents are free to distort and/or hide attribute values. We then address induction methods for classifiers that take into account only strategic hiding as a special case. We present three imputation methods. The first, which we call $D ^ { ( - 1 ) } ( w , b )$ , can classify all agents correctly and allow positive agents to still hide some information. A second one, $D ( w , b )$ , classifies all agents correctly and incents all positive agents to reveal all of their attribute values. Finally, we merge our results with those of Boylu et al. (2010) to give our third method $D _ { S } ( w , b )$ that handles both distortion and hiding of agent attributes. Notation is summarized in Table 1. An online appendix (available as supplemental material at http://dx.doi.org/10.1287/isre.2014.0526) contains all proofs and certain formulations and details of some sets used in the paper.

<table><tr><td colspan="2">General</td></tr><tr><td> $x'$ </td><td>Vector transpose as in  $x'$ .</td></tr><tr><td>M</td><td>A sufficiently large number.</td></tr><tr><td> $e_i, e, I$ </td><td>ith unit vector, vector of ones, and identity matrix, respectively.</td></tr><tr><td colspan="2">Support vector machine</td></tr><tr><td> $w \in \Re^n$ </td><td>Vector of weights for the linear discriminate function.</td></tr><tr><td> $Z(w)$ </td><td>Set of indices of w giving zero values.</td></tr><tr><td>b</td><td>Intercept for the linear discriminate function.</td></tr><tr><td>z</td><td>Critical value. Classify x as positive if  $w'x + b \geq z$ .</td></tr><tr><td colspan="2">Agents (agent subscript i may be suppressed)</td></tr><tr><td>X, n</td><td>Space of agent attribute vectors.  $X \subseteq \Re^n$  where n is the number of attributes.</td></tr><tr><td> $x_i, y_i$ </td><td>Agent i&#x27;s vector of attributes and i&#x27;s true class,  $y_i \in \{-1, +1\}$ .</td></tr><tr><td> $\mu_i(c_i)$ </td><td>Agent i&#x27;s cost vector of disclosing (distorting) attributes.</td></tr><tr><td> $\alpha_i$ </td><td> $\alpha_{ik} = 1$  if agent i reveals the kth attribute;  $\alpha_{ik} = 0$  otherwise.</td></tr><tr><td> $v_i$ </td><td>Vector representing the amount and direction of distortion by agent i</td></tr><tr><td> $r_i$ </td><td>Agent i&#x27;s reservation value.</td></tr><tr><td> $V_i, I_i$ </td><td>Opportunity cost of agent i. Agent i participates ( $I_i = 0$ ) or not ( $I_i = 1$ ).</td></tr><tr><td>d,  $R_i(d)$ </td><td>Hyper-rectangle giving all combinations of  $x_i$  with default vector d.</td></tr><tr><td> $A_i, Y(w)$ </td><td>Diagonal matrices:  $A_{i(k,k)} = \alpha_{ik}$  and  $Y(w)_{(k,k)} = \text{sign}(w_k)$ </td></tr><tr><td> $x_s$ </td><td>Any negative support vector.</td></tr><tr><td colspan="2">Principal</td></tr><tr><td>S, I</td><td>Training sample,  $S = ((x_1, y_1), \ldots, (x_l, y_l))$ . I is the number of observations.</td></tr><tr><td> $D_i(w, b)$ </td><td>Set of all default vectors guaranteeing no misclassifications using (w, b) by agent i.</td></tr><tr><td> $D^{(y)}(w, b)$ </td><td>All default vectors guaranteeing no misclassifications with (w, b) by all type y agents.</td></tr><tr><td> $\bar{D}_i(w, b)$ </td><td>Set of all default vectors using (w, b) that incent agent i to disclose all attributes.</td></tr><tr><td> $\bar{D}^{(y)}(w, b)$ </td><td>All default vectors with (w, b) that incent all type y agents to disclose all attributes.</td></tr><tr><td> $D(w, b)$ </td><td> $D^{(-1)}(w, b) \cap \bar{D}^{(+1)}(w, b)$ —all default vectors with (w, b) that incent all positive agents to disclose all attributes and forces all agents to be correctly classified.</td></tr><tr><td> $D_s(w, b)$ </td><td>Set of all default vectors that thwart agents&#x27; distortion and hiding behaviors.</td></tr></table>

## 2. Assumptions and Formulation

Support vector machines (SVM) use a convex minimization formulation to create a classifier. We use two SVM formulations, called the hard margin (PHMSVM) and soft margin (PSMSVM) formulations, (see, Cristianini and Shawe-Taylor 2000). The details of the two formulations are given in the online appendix.

When classifying agents who strategically hide attributes to gain a positive labeling, the principal has a twofold challenge. She must determine an LDF 4w1 b5 and she must decide how to impute missing values. We signify the imputed missing values with a vector d. When attribute $\hat { k }$ is missing in an observation, the principal will substitute the value $d _ { k }$ in its place. For induction, in line with Boylu et al. (2010) and Dekel et al. (2010), we assume we have a training sample as follows.

<sup>Assumption</sup> <sup>1.</sup> We assume the training sample, S, is gathered without any missing or distorted attribute values and all values, including the class, are true values and known. Further, we assume there is at least one example in S having $y _ { i } = - 1$ and one having $y _ { i } = + 1$ and S is strictly linearly separable.

These are typical assumptions in machine learning (e.g., Boylu et al. 2010). A principal would likely have to exert extra effort to determine true values (whether missing or distorted) and validate the class and other attribute values of the training sample. We analyze the behavior of agents and the principal based on the following two assumptions.

<sup>Assumption</sup> <sup>2.</sup> An astute principal assumes a worst case: that an agent knows which 4w1 b5 and default vector d she will use, and that each agent will act in his own best interest.

<sup>Assumption</sup> <sup>3.</sup> Agent i has a linear disutility $V _ { i } I _ { i } +$ $\begin{array} { r } { \sum _ { k = 1 } ^ { n } \mu _ { i k } \alpha _ { i k } + \sum _ { k = 1 } ^ { n } c _ { i k } v _ { i k } . } \end{array}$ , where $V _ { i }$ is the disutility associated with not attaining a positive labeling and $\mu _ { i } , c _ { i } \in \mathfrak { R } ^ { n }$ are vectors of positive costs to disclose and distort attributes, respectively. The cost of disclosing all attributes is assumed less than the disutility associated with not attaining a positive labeling, $i . e . , e ^ { \prime } \bar { \mu _ { i } } < V _ { i }$ (e is a vector of ones). Agent i decides on whether to participate $( I _ { i } = 0 )$ or not $( I _ { i } = 1 )$ and, if participating, which attributes to hide $( \alpha _ { i k } = 0 )$ or disclose $( \alpha _ { i k } = 1 )$ . Similarly, for reported values, each agent will choose a vector $v _ { i }$ to distort attribute values.

Assumptions 2 and 3 create a framework, based on rational expectations and linear (dis)utilities, under which the principal can determine a strategy to thwart strategic manipulation of data. The last part of Assumption $^ { 3 , }$ that $e ^ { \prime } \mu _ { i } < V _ { i } ,$ guarantees that an agent can still distort some attributes after disclosure. Note that this assumption implies that we will not see overqualified agents (of our hiring example) in our data sets.

We note that in addition to the cost of disclosing, in certain cases there might be a cost for hiding information. The net impact of this is that agents may be better off disclosing some attributes rather than hiding them. This however, will not change our results so is not pursued further. We provide a full discussion in the appendix and will further discuss this in our conclusion section.

We define agent $i ^ { \prime } { \bf s }$ problem as follows. Given that the principal uses $( w , b )$ and $d ,$

$$
P A: \min _ {\alpha_ {i} \in \{0, 1 \} ^ {n}, I _ {i} \in \{0, 1 \}, v _ {i} \in \Re^ {n}, v _ {i} \geq 0} \left\{V _ {i} I _ {i} + \sum_ {k = 1} ^ {n} \mu_ {i k} \alpha_ {i k} + \sum_ {k = 1} ^ {n} c _ {i k} v _ {i k} \right\}
$$

s.t.

$$
\begin{array}{l} \sum_ {k = 1} ^ {n} w _ {k} (\alpha_ {i k} (x _ {i k} - d _ {k}) + Y _ {k k} v _ {i k} + d _ {k}) + M I _ {i} \geq 1 - b \\ v _ {i k} \leq M \alpha_ {i k} \quad k = 1, \ldots , n. \end{array}
$$

Here $M \geq 1 - b - w ^ { \prime } d$ is a sufficiently large number. The objective function is to minimize disutility. The first constraint attempts to attain a positive classification from the principal, where the diagonal matrix Y has $Y _ { k k } = \mathrm { s i g n } ( w _ { k } )$ , and the agent chooses a vector $Y v _ { i }$ to distort some of its attribute values—here $v _ { i } \geq 0$ If this cannot be achieved, the agent will not participate $( \mathrm { i . e . , } I _ { i } = 1 )$ . The second constraint requires that only attributes that are published can be distorted.

As mentioned above, the principal needs to choose an LDF 4w1 b5 and a default vector $\bar { d } \in \mathfrak { R } ^ { n }$ for the chosen 4w1 b5. Here we use SVMs to determine 4w1 b5. So, although we start with a strictly separable training set, S, a principal must assume that agents would try to hide and distort attributes to gain/retain a positive classification when $( w , b )$ is used for decision making. So, instead of using $x _ { i }$ in these SVM formulations, the principal needs to use her imputed values and the agent’s distorted ones as in $\begin{array} { r } { t _ { i } ( \bar { w } , b , d ) = \sum _ { k = 1 } ^ { n } ( \alpha _ { i k } ( x _ { i k } - d _ { k } ) } \end{array}$ $+ d _ { k } + Y _ { k k } v _ { i k } ) e _ { k } ,$ where $e _ { k }$ is the kth unit vector. The hardmargin formulation (for the separable case), PHMSVM, may not be applicable because the set of $t _ { i }$ vectors may not be linearly separable. Hence the principal needs to solve a soft-margin form, which we call the principal’s problem (PP):

$$
PP\colon \min_{\substack{(w,b)\in H\\ d(w,b)\in R^{n}}}\Bigl \{w^{\prime}w + C\sum_{i = 1}^{l}\max (0,1 - y_{i}(w^{\prime}t_{i}(w,b,d) + b))\Bigr \} .
$$

A special case of the principal’s problem is

$$
PP_{s}\colon \min_{\substack{(w,b)\in H\\ d(w,b)\in R^{n}}}\Bigl \{w^{\prime}w + C\sum_{i = 1}^{l}\max (0,1 - y_{i}(w^{\prime}t_{si}(w,b,d) + b))\Bigr \} ,
$$

where $\begin{array} { r } { t _ { s i } ( w , b , d ) = \sum _ { k = 1 } ^ { n } ( \alpha _ { i k } ( x _ { i k } - d _ { k } ) + d _ { k } ) e _ { k } } \end{array}$ . That is, only hiding activities are anticipated.

We study the principal’s problem in a two-step process. First we study the case where agents may hide but not distort attributes, that is, we first solve problem $P P _ { s } .$ . Armed with this result, we look at $P P ,$ the problem where agents may distort and hide attributes. Note that each agent i has his own decision variables, e.g., $\alpha _ { i k } \in \{ 0 , 1 \}$ , but we often suppress the agent subscripts to ease the notation when the context makes it clear, especially for variables using two subscripts (i.e., agent and attribute).

## 2.1. Agent Nondisclosure: Two New Imputation Methods

Given a training sample S, we will characterize two sets, $D ^ { ( - 1 ) } ( w , b )$ and $\hat { D ( } w , b \mathrm { ) }$ , from which a principal can choose vector $d .$ We now look at the principal’s problem of choosing d given 4w1 b5. Let $\begin{array} { r } { R _ { i } ( d ) \overset { - } { \equiv } \{ \sum _ { k = 1 } ^ { n ^ { - } } ( \alpha _ { k } \overset { - } { ( } x _ { i k } - d _ { k } ) } \end{array}$ $+ d _ { k } ) e _ { k } , \bar { \forall \alpha } \in \bar  \{ 0 , 1 \} ^ { n } \} . R _ { i } ( d )$ represents the set of all possible responses of agent i given the principal’s default vector d. Note that $x _ { i } \in R _ { i } ( d )$ (with $\alpha = e$ corresponding to disclosing all attributes), and $d \in R _ { i } ( d )$ (with $\alpha = 0$ , corresponding to reveal nothing). Clearly $( w , b )$ correctly classifies agent i regardless of his decisions if $t \in { \dot { R } } _ { i } ( d ) \Rightarrow y _ { i } ( w ^ { \prime } t + b ) \geq 1$ . Let $D _ { i } ( w , b ) \equiv$ 8d2 $t \in R _ { i } ( d ) \Rightarrow y _ { i } ( w ^ { \prime } t + b ) \geq 1 \}$ . This set gives all of the default vectors the principal could use that would result in a correct classification of agent i (in the training sample) regardless of the agent’s strategy. The shaded areas in Figures 1–3 show $\breve { D } _ { i } ( w , b )$ for three cases and for agents in each class. In all of the figures, a positive agent point is denoted as a square, and a negative agent point is represented by a circle. Points on the hyperplanes are support vectors. Lines projected from each agent onto a hyperplane show how we derive the projection point of the agent. Figures 1 and 2 show $\bar { D } _ { i } ( \boldsymbol { w } , \boldsymbol { b } )$ when $x _ { i }$ is a support vector, and when $x _ { i }$ is not a support vector, respectively. In both cases the w vector has no zero terms. Figure 3 shows $D _ { i } ( w , b )$ for a nonsupport vector with w having a zero component, $w _ { 2 } = 0 .$

For $y \in \left\{ - 1 , + 1 \right\}$ , define $\begin{array} { r } { D ^ { ( y ) } ( w , b ) \equiv \bigcap _ { y _ { i } = y } D _ { i } ( w , b ) } \end{array}$ the intersection of the $D _ { i } ( w , b )$ vectors for all type y agents. If the principal chooses $\boldsymbol { d } \in \boldsymbol { D } ^ { ( y ) } ( \boldsymbol { w } , \boldsymbol { b } )$ , all agents of type $y$ in the training sample will be correctly classified with $( w , b )$ regardless of what information they hide. The shaded areas in Figure 4 show $D ^ { ( y ) } ( w , b )$ one for each class based on the points in the figure. Unfortunately, it is easy to see that $\boldsymbol { D } ^ { ( + 1 ) } ( \boldsymbol { w } , \boldsymbol { b } ) \tilde { \cap }$ $\boldsymbol { D } ^ { ( - 1 ) } ( \boldsymbol { w } , \boldsymbol { b } )$ is empty so we need to create a different set that handles both classes.

Figure 1 Support Vectors $D _ { i } ( w , b )$  
![](/api/attachments/PRPEHZJ3/fulltext/images/a88b10fbe4636decae6bd5573dea0b98014f04ce4e7d4d23415c514e58ba2952.jpg)

Figure 2 Nonsupport Vectors $D _ { i } ( w , b )$  
![](/api/attachments/PRPEHZJ3/fulltext/images/3a572d8f56744cb6956958561f0cba0dfbc0ddb72bdb053c011e89745586a3a5.jpg)

Figure 3 Nonsupport Vector, Special Case $W _ { 2 } = 0$  
![](/api/attachments/PRPEHZJ3/fulltext/images/b51fcd790c95da4432a6ff2db2b20cebb432cf60b94628d8917bf229a96f0807.jpg)

Some positive agents in the training sample may not need to reveal all information to be classified as positive so they may choose to hide some attribute values to minimize cost. A principal might like a default vector that can incent all positive agents to disclose all of their information. Let $( w , b )$ be a hyperplane that separates $S ,$ and $Z ( w ) = \{ k \mid w _ { k } = 0 \}$ . Define $\bar { D } _ { i } ( w , b ) \equiv$ 8d2 t ∈ R 4d51 y 4w<sup>0</sup>t + b5 ≥ 1 ⇒ t = x 1 k y Z4w59. In the online appendi $\mathbf { x , }$ we show this set of default vectors incents agent i to disclose every attribute $k ,$ where k $\notin Z ( w )$ 5. Figure 5 illustrates such a set for a positive agent $x _ { i } .$ When the principal uses any default vector in the set $\bar { D } _ { i } ( w , b ) , \hat { x } _ { i }$ (in Figure 5) needs to disclose all attributes where $k \notin Z ( w )$ to remain in the positive region. The set of default vectors that incents all agents of type $y$ in the training sample to disclose all of their attributes is defined as $\begin{array} { r } { \bar { D } ^ { ( y ) } ( w , b ) \equiv \bigcap _ { y _ { i } = y } \bar { D } _ { i } ( w , b ) } \end{array}$ Figure 6 shows such a set for the positive class, $\mathrm { i . e . , }$ $\bar { D } ^ { ( + 1 ) } ( w , b )$ , as the shaded convex cone with vertex x˜. To ease the graphics, only three positive agents are shown. All points will be mapped onto the negative margin hyperplane or into the negative region if they hide any attribute value given any default vector in the shaded region; $\bar { D } ^ { ( + 1 ) } ( w , b )$ is designed to make the highly positive agents look like marginal negative agents if they hide an attribute.

Figure 4 $\boldsymbol { D } ^ { - 1 } ( \boldsymbol { w } , \boldsymbol { b } )$ vs. D<sup>+1</sup>4w 1 b5  
![](/api/attachments/PRPEHZJ3/fulltext/images/b98fccc22c631c562bbd1369f61e3ec295dbed8b0feb78807b14d8819e3fd242.jpg)

Figure 5 Construction of $\bar { D } _ { i } ( w , b )$  
![](/api/attachments/PRPEHZJ3/fulltext/images/93649f7adafde807018ee07879fc7d59ed407d5eb95d96b4d691c4bb72099fb7.jpg)

In summary, if the principal uses $\bar { D } ^ { ( + 1 ) } ( w , b )$ all positive agents in the training sample will disclose all of their attributes to remain positively classified. If she uses $\boldsymbol { D } ^ { ( - 1 ) } ( \boldsymbol { w } , \boldsymbol { b } )$ , all negative agents in the training sample will be classified correctly regardless of agents’ strategy. $\mathrm { S o ~ a ~ }$ principal might want to find the intersection of $\bar { D } ^ { ( + 1 ) } ( w , b )$ and $\boldsymbol { D } ^ { \aa ( - 1 ) } ( \boldsymbol { w } , \boldsymbol { b } )$ . With any default vector in such an intersection set, the principal will be able to classify all agents correctly and incent all positives to reveal all information. Note that positive agents have a stronger incentive than negative ones to reveal attribute information. Let $D ( w , b ) \equiv$ $D ^ { ( - 1 ) } ( w , b ) \cap \bar { D } ^ { ( + 1 ) } ( w , b )$ . In Figure $7 , D ( w , b )$ is the darker shaded region, a convex cone with xˆ as its vertex point, which is the intersection of two convex cones with vertices x˜ and x¯.

Figure 6 Construction of $\bar { D } ^ { + 1 } ( w , b )$  
![](/api/attachments/PRPEHZJ3/fulltext/images/42f03c2257e2dccbc6e3700b2fa1af4bd965dd20e18c6ea450c8b5f90a26d853.jpg)

Figure 7 Comparison of $D ^ { - 1 } ( w , b ) , \bar { D } ^ { + 1 } ( w , b ) , D ( w , b )$  
![](/api/attachments/PRPEHZJ3/fulltext/images/d78524d6cd81ffa2851eaaa8bc3114193f8f4df3c1677dec9db4207812feb29b.jpg)

The definitions of sets ${ \cal D } ( w , b ) , \ { \cal D } ^ { ( y ) } ( w , b )$ , and $\bar { D } ^ { ( y ) } ( w , b )$ describe only how agents in the training sample will behave if a d from one of these sets is given to us. We still need explicit formulas to construct these sets. We give details of how to construct them in Proposition 1 in the online appendix.

## 2.2. Solution of the Principal’s Problem When There Is No Distortion

We now show an optimal solution to the principal’s problem for the special case when agents can only hide information (to simplify the discussion substitute the set $D ^ { ( - 1 ) } ( w ^ { * } , b ^ { * } )$ for $\bar { D } ( \tilde { w ^ { * } } , b ^ { * } )$ if that imputation method is used by the principal).

Theorem 1. <sub>Let</sub> $( w ^ { * } , b ^ { * } )$ solve the hard margin problem (PHMSVM). Then $( w ^ { * } , b ^ { * } )$ and $d ^ { * } \in D ( w ^ { * } , b ^ { * } )$ solves the principal’s problem $( P P _ { s } )$

Theorem 1 shows that an astute principal can use any $d ^ { * } \in D ( w ^ { * } , b ^ { * } )$ with a hard-margin solution (the proof follows from the optimality of $( w ^ { * } , b ^ { * } )$ and the fact that no misclassifications result when $d ^ { * } \in D ( w ^ { * } , b ^ { * } )$ is used).

We use a numerical example to illustrate how the principal can apply the $\hat { D ^ { ( - 1 ) } } ( w ^ { * } , b ^ { * } )$ and $D ( w ^ { * } , b ^ { * } )$ methods to real applications such as the hiring example. Suppose hiring decisions are based on years of experience and years of education after grade school. The training set in Figure 8 has seven agents, four true negatives $( x _ { 1 } , \ldots , x _ { 4 } ) ^ { \prime } = ( ( 5 . 5 , 7 ) , ( 4 . 5 , 9 )$ 43051 551 461 50555, and three true positives $( x _ { 5 } , x _ { 6 } , x _ { 7 } ) ^ { \prime } =$ 4461 1051 48051 551 47051 80555. Given this training set, the principal’s optimal solutions are $( w ^ { * } , b ^ { * } ) = ( 1 , \bar { 0 } . 5 , - 1 0 )$ $\hat { D } ^ { - 1 } ( \hat { w ^ { * } } , b ^ { * } ) \bar { = } ( 4 . 5 , 6 ) + \lambda ( - 1 , - 1 ) , \lambda \geq 0$ and $D ( w ^ { * } , b ^ { * } ) =$ $( 4 , 1 ) + \lambda ( - 1 , - 1 ) , \lambda \geq 0 .$

Figure 8 Agents’ Strategy Based on $D _ { s } ( w , b )$  
![](/api/attachments/PRPEHZJ3/fulltext/images/5417e3b114ee6227d12288a26d521f38d11a6aa15722eab19862f60613653377.jpg)

Consider two new applicants with true values, $( 3 , 4 , - 1 )$ and 481 71 15, as shown in Table 2. Each of these applicants may hide certain attributes strategically. The principal can choose a default value from $\hat { D ^ { ( - 1 ) } } ( w ^ { \ast } , b ^ { \ast } )$ or $\bar { D } ( w ^ { * } , b ^ { * } )$ when faced with such strategic behavior. In Table 2 all possible strategies are listed in the “agent’s choices” column, and the principal’s labeling decisions with the vertex of the set $\hat { D ^ { ( - 1 ) } } ( w ^ { \ast } , b ^ { \ast } )$ or $D ( w ^ { * } , b ^ { * } )$ are in the next two columns. As shown in Table $^ { 2 , }$ the first agent, a true negative, will be classified as negative regardless of his hiding strategies when the principal uses $D ^ { ( - 1 ) } ( w ^ { * } , b ^ { * } )$ or $D ( \bar { w } ^ { * } , b ^ { * } )$ . Agent two, a true positive, will not be classified as positive unless he reveals all attributes when the principal uses $D ( w ^ { * } , b ^ { * } )$ but with $D ^ { ( - 1 ) } ( w ^ { * } , b ^ { * } )$ , he may still be classified as positive when hiding the education attribute. Given that $D ^ { ( - 1 ) } ( w , b )$ is more “forgiving,” if the principal is using $D ^ { ( - 1 ) } ( w , b )$ , positive agents that are very strong in one aspect (say extensive experience) may get by without disclosing the other attribute $( \mathrm { i . e . , }$ education).

Likely in a real setting, agents have no way of knowing in advance exactly which set the principal will use unless the principal provides a signal, for example, by asking the agents to fill out the application form as completely as they can or by saying that complete applications will be given preference (both signaling the positive agents to disclose more). If the principal’s classifier were perfect, no negative agent would apply and qualified ones would likely disclose everything assuming the worst case.

All of our results based on $D ^ { ( - 1 ) } ( w ^ { * } , b ^ { * } )$ and $D ( w ^ { * } , b ^ { * } )$ apply to agents in the training sample. Because the principal’s strategy is based on training data, it is prone to sampling error over the whole instance space. So some actual applicants may be able to thwart the principal. Of course, the larger the training sample, the lower the chance such cases will succeed. Zhang (2011) studied these two sets for large samples and showed that the misclassification rate rapidly goes to zero for both methods as the training set sizes increase. In addition, any point in $\tilde { D ^ { ( - 1 ) } } ( w ^ { \ast } , \tilde { b ^ { \ast } } )$ and $D ( w ^ { * } , b ^ { * } )$ can thwart agents’ strategic behavior. Using the vertex points of these sets is the simplest. However, to be conservative (e.g., when sample size is small or the boundary of training data is close to the margin planes), a principal may move along −w for larger values of $\gamma \geq 0$

Table 2 Choices for the Agents and the Principal

<table><tr><td rowspan="2">Agent and his label (x,y)</td><td rowspan="2">Agent&#x27;s choices</td><td colspan="2">Principal labeling agents using $\sum_{k=1}^{n} w_k (\alpha_{ik}(x_{ik} - d_k) + d_k) + b$  and  $d \in D^{-1}(w, b)$  or  $d \in D(w, b)$ (assuming no distortion) (w, b) = (1, 0.5, -10)</td><td>Labeling with distortion  $\mu' = (1, 2), c' = (1, 1), V = 3$  $\sum_{k=1}^{n} w_k (\alpha_{ik}(x_{ik} - d_k) + Y_{kk} v_{ik} + d_k) + b(w, b) = (1, 0.5, -10)$ </td></tr><tr><td> $d = (4.5, 6) \in D^{-1}$ </td><td> $d = (4, 1) \in D$ </td><td> $d = (4, 2) \in D_S$ </td></tr><tr><td rowspan="2">(3, 4, -1)</td><td>(?, 4)</td><td>(4.5, 4) → -3.5 &lt; -1</td><td>(4, 4) → -4 &lt; -1</td><td>(4, 4) + (0, 1) = (4, 5) → -3.5 &lt; -1</td></tr><tr><td>(3, ?)</td><td>(3, 6) → -4 &lt; -1</td><td>(3, 1) → -6.5 &lt; -1</td><td>(3, 2) + (2, 0) = (5, 2) → -4 &lt; -1</td></tr><tr><td rowspan="2">(8, 7, 1)</td><td>(?, 7)</td><td>(4.5, 7) → -2 &lt; -1</td><td>(4, 7) → -2.5 &lt; -1</td><td>(4, 7) + (0, 1) = (4, 8) → -2 &lt; -1</td></tr><tr><td>(8, ?)</td><td>(8, 6) → 1 ≥ 1</td><td>(8, 1) → -1.5 &lt; -1</td><td>(8, 2) + (2, 0) = (10, 2) → 1 ≥ 1</td></tr></table>

## 2.3. Principal’s Strategy When Agents Can Hide and Distort Attribute Values

We now look at the principal problem where the principal anticipates both strategic distortion and nondisclosure. First, let us briefly review the Boylu et al. (2010) results that we will employ. Under the assumptions stated earlier, Boylu et al. (2010) essentially solves a version of PP where $\alpha = e \ ( { \mathrm { i . e . } }$ , all attributes are published), and agents’ disutility of not attaining a positive classification is equivalent to $r _ { i } = V _ { i } - e ^ { \prime } \mu _ { i }$ In their study, the principal anticipates the optimal distortion by agent i, $v _ { i k } ^ { * } ( w , b )$ , and chooses a 4w1 b5 to thwart that. Under the assumption that $c _ { i } = c \ { \mathrm { a n d } } \ r _ { i } = r ,$ i.e., all agents have the same cost vector for distorting attributes and net reservation value, respectively, they prove that the solution to this reduced problem can be found by shifting and scaling the optimal solution of hard-margin problem, PHMSVM $( w ^ { * } , b ^ { * } )$ (Boylu et al. 2010, p. 177; Theorem Base Case (ThmBC)).

Since agents can end up with different $r _ { i }$ after hiding we cannot use ThmBC directly. One remedy is to find the maximum $r _ { i }$ and use that as the reservation amount needed in ThmBC. Boylu et al. (2010) highlight that, given the optimal classifier, negative agents will choose not to distort since they cannot be classified as positive by distortion. As shown in §2.2, positive agents will also choose not to publish, and will be mapped to the principal’s default vector. At this point the principal’s problem becomes somewhat arbitrary as she can increase the margin (recall that her objective is to increase margin while minimizing misclassification errors) by choosing a default vector deeper in $D ( w , b )$ or $D ^ { ( - 1 ) } \dot { ( } w , b )$ . Consequently, rather than finding an r and d in $D ( w , b )$ or $\tilde { D ^ { ( - 1 ) } } ( w , b )$ that work as discussed, we can construct a set such that all values in it are guaranteed to thwart both hiding and distortion. This set, ${ \cal D } _ { S } ( w , b ) ,$ , guarantees that no negative agent can be better off than a negative support vector after hiding and distortion. Consequently, one can use $r = V - e ^ { \prime } \mu$ as the common reservation in ThmBC to compute the amount of shifting and scaling necessary to thwart distortion. We derive $D _ { S } ( w , b )$ in the online appendix. We show that it is nonempty and intersects both $D ( w , b )$ and $\boldsymbol { D } ^ { ( - 1 ) } ( \boldsymbol { w } , \boldsymbol { b } )$ (Proposition 2). Below we provide its definition:

$$
D _ {S} (w, b) \equiv \left\{ \begin{array}{c} \forall i \colon y _ {i} = - 1, \forall \alpha \in \{0, 1 \} ^ {n}, \forall j \colon \alpha_ {j} = 1, \\ d \colon w ^ {\prime} \bigg [ \mathrm{A} _ {i} x _ {i} + (I - \mathrm{A} _ {i}) d + Y (w) \frac {V - \alpha^ {\prime} \mu}{c _ {j}} e _ {j} \bigg ] \\ \leq w ^ {\prime} \bigg [ x _ {S} + Y (w) \frac {V - e ^ {\prime} \mu}{c _ {j *}} e _ {j *} \bigg ] \end{array} \right\}.
$$

Here $j *$ represents the index of a best attribute to alter after one publishes everything (see Boylu et al. 2010); $\mathbf { A } _ { i }$ is a diagonal matrix formed from agent $i ^ { \prime } s \ \alpha , I$ is the identity matrix, and $x _ { s }$ is any negative support vector.

We show how this system of inequalities behaves on our hiring example, where we have $( w ^ { * } { } ^ { \prime } , b ^ { * } ) =$ $( ( 1 , 0 . 5 ) , - 1 0 )$ and the four negative agents: $( x _ { 1 } ,$ $\dots , x _ { 4 } ) ^ { \prime } = ( ( 5 . 5 , 7 ) , ( 4 . 5 , 9 ) , ( 3 . 5 , 5 ) , ( 6 , 5 . 5 ) )$ (Figure 8). Note that support vectors are $x _ { 1 }$ and $x _ { 2 } .$ . Suppose $\mu ^ { \prime } = ( 1 , 2 ) , c ^ { \prime } = ( 1 , 1 )$ and $V = 3 .$ . This particular V violates our Assumption 3 but illustrates an extreme case. It prevents those agents who publish everything from distorting a published value $( \mathrm { i . e . , ~ } V - e ^ { \prime } \mu = 0 )$ Consequently, a support vector agent who publishes everything cannot move and a negative point that does not publish everything can at best look like a support vector after attribute distortion. Working out the inequalities in $D _ { S } ( w , b )$ , for $i = 1$ we get

$$
\alpha = \binom {1} {0} \colon (1, 0. 5) \left[ \binom {5. 5} {d _ {2}} - \binom {\frac {V - 1}{1}} {0} \right] \leq 9 \Rightarrow d _ {2} \leq 3
$$

$$
\alpha = \binom {0} {1} \colon (1, 0. 5) \left[ \binom {d _ {1}} {7} + \binom {0} {\frac {V - 2}{1}} \right] \leq 9 \Rightarrow d _ {1} \leq 5.
$$

From the other points we get $d _ { 1 } \leq 4 , d _ { 2 } \leq 5 , d _ { 1 } \leq 6 .$ $d _ { 2 } \leq 7 ,$ and $d _ { 1 } \leq \bar { 5 } . 7 5 , \ d _ { 2 } \leq 2$ . These yield $\begin{array} { r } { D _ { \cal { S } } ( w , b ) = } \end{array}$ 8d2 $d _ { 1 } \leq 4 , d _ { 2 } \leq 2 \}$ . A strict inequality may be required to prevent points exchanging one of their coordinates with that of $\dot { d }$ when they have identical values. Ignoring strategic behavior and assuming all points want to get as close to the positive margin hyperplane as possible, given the vertex above, the best actions for points are $x _ { 1 }$ publishes everything and remains a support vector, $x _ { 2 }$ is indifferent between publishing everything or publishing education only (attribute two) and padding it by one year, $x _ { 3 }$ hides his experience, publishes and distorts education by one year $, x _ { 4 }$ publishes and distorts his experience by two years. The alterations for $x _ { 2 } , x _ { 3 } ,$ and $x _ { 4 }$ are highlighted by dashed arrows. We also see in Table 2 (last column), that $D _ { S } ( w , b )$ is able to thwart distortion and hiding on unseen negative examples.

Even though some positive agents can gain an advantage by not publishing everything, they will publish and distort just enough to be no worse than a positive support vector. Because $D _ { S } ( w , b )$ allows positive agents to hide some information it is analogous to $D ^ { ( - 1 ) } ( \omega , b )$

## 3. Conclusion and Future Research

In this paper we study a classification problem when agents can hide and distort attribute values to attain positive classification. First, we focus on the disclosure problem and develop two new imputation methods, $\hat { D } ^ { - 1 } ( w , b )$ and $D ( w , \hat { b } ) ; D ^ { - 1 } ( w , b )$ thwarts negative agents but allows positive agents to hide information; $\Breve { \boldsymbol { D } _ { } } ( \boldsymbol { w } , \boldsymbol { b } )$ thwarts negative agents too. It additionally forces positive agents to disclose all of their attributes. Both methods are easy to use in practice, a hallmark of imputation methods.

We also extend results of Boylu et al. (2010) to a general case where agents are free to use a combination of hiding and distortion as a strategy. We show that if the training set is separable and all agents have the same costs, it is possible to compute a set of default vectors, ${ D _ { S } ( w , b ) }$ , that prevent negative agents from gaining an advantage by altering/hiding attributes where $( w , b )$ are computed based on Boylu’s results. The principal can prevent agent distortion and nondisclosure by negative agents by using $\bar { x } - \gamma w$ for $\gamma \geq 0$ If she desires she can force positive agents to disclose all attributes by using $\hat { x } - \lambda w$ (see Proposition 2 in the online appendix). We note that $D _ { S } ( w , b )$ does not explicitly constrain the strategy of the positive agents. However, one can constrain the positive agents such that no positive agent that hides and distorts information can be better off than a positive support vector that publishes everything and distorts as necessary. A set of default values derived this way would guarantee that positive agents reveal everything even if some attributes can be distorted. The derivation of the set implied by this restriction is similar to that of $D _ { S } ( w , b )$ Because a nonsupport vector positive agent is in a better position than a support vector positive agent when he reveals everything  needs to be constrained to $\forall \alpha \in \{ 0 , 1 \} ^ { n } / e$

One underlying theme of all three methods is that negative agents end up not participating because none of the strategies help them game the system. There are however two reasons why a negative agent may participate. First, as we discuss in the appendix, in the presence of a positive cost of hiding, a default strategy is to reveal those attributes for which the cost of hiding is higher than publishing, or when the cost of publishing is zero (for example, one can view the effort needed to prepare a resume as sunk cost and hence the costs of the relevant attributes as zero). This does not impact the misclassification rate of the principal. There is also the possibility that a negative agent will reveal some or all of his attributes because he might be able to exceed the threshold score (as we discussed earlier the classification performance of $( w , b )$ and d is subject to sampling error).

Assuming the worst case, the principal should use a point in $D _ { S } ( w , b )$ since it allows some latitude to positive agents (similar to $\boldsymbol { D } ^ { - 1 } ( \boldsymbol { w } , \boldsymbol { b } ) )$ . However, in a reallife situation, where principals compete for business and where even some of the negative agents (perhaps those that are marginally negative) can generate revenue for the principal, some default values in all three sets we described will reduce revenue. In such situations, a principal has to trade off classification error with loss of business. Also, incorporating multiprincipal competition into the formulation, and determining if and when a general solution can be offered, is an interesting future research direction.

One area for future research is to relax our assumptions. A key assumption, that S is strictly linearly separable, is restrictive. Relaxing this assumption means that all LDFs may misclassify some agents even if they reveal all of their attributes. Although the SVM model has a soft margin formulation allowing possible misclassifications, trading off these with generalization goals and the impact on the choice of imputation vector is a theoretical challenge. Such an analysis is also confounded by two factors: (1) is there a 4w1 b5 better than the solution to the soft-margin SVM formulation, and (2) how should ${ \cal D } ^ { - 1 } ( w , b ) , { \cal D } ( w , b )$ , and $D _ { S } ( w , b )$ be computed when $( w , b )$ is known to make mistakes?

The assumptions on agent utility can be relaxed too. Even while maintaining a linear structure, we assumed the cost to an agent of disclosing all attributes is less than the disutility associated with not attaining a positive labeling. Without this assumption, some theoretical results we give are too strong. Of course, our results are then just conservative.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2014.0526.

## Appendix. Discussion on the Agent’s Objective Function

One can argue that there may be a cost to hiding an attribute. Let $\omega _ { i k } \ge 0$ be agent i’s cost to hide attribute k. In such cases the objective function of the agent would be $\begin{array} { r } { V _ { i } I _ { i } + \sum _ { k = 1 } ^ { n } ( \mu _ { i k } \alpha _ { i k } + \omega _ { i k } ( 1 - \alpha _ { i k } ) ) + \sum _ { k = 1 } ^ { n } c _ { i k } v _ { i k } ^ { - } , } \end{array}$ and after simplification, letting $\begin{array} { r } { \Omega _ { i } = \sum _ { k = 1 } ^ { n } \omega _ { i k } } \end{array}$ , the objective is $\Omega _ { i } +$ $\begin{array} { r } { V _ { i } I _ { i } + \sum _ { k = 1 } ^ { n } \bar { \mu } _ { i k } \alpha _ { i k } + \sum _ { k = 1 } ^ { n } c _ { i k } v _ { i k } , } \end{array}$ , where $\bar { \mu } _ { i k } = \mu _ { i k } - \omega _ { i k }$ can be negative. Suppose no combination of hiding and publishing attributes can result in a positive labeling. Even though publishing will not yield a positive labeling, the agent will publish attributes where $\bar { \mu } _ { i k } < 0 ,$ hide ones where $\bar { \mu } _ { i k } > 0 ,$ and choose to hide or publish those with $\bar { \mu } _ { i k } = 0$ . We call this the default agent strategy (realizing there may be alternatives when some attributes have the same cost for hiding as publishing). Our imputation methods guarantee that no true negative agent (i.e., those with a true negative label) can attain a positive labeling and so will select a default strategy. When either the cost of hiding is zero, or less than the cost of publishing, a default strategy for the agent is not to publish any attributes.

## References

Akerlof G (1970) The market for “lemons”: Quality uncertainty and the market mechanism. Quart. J. Econom. 84(3):488–500.

Ba S (2001) Establishing online trust through a community responsibility system. Decision Support Systems 31(3):323–336.

Baron DP (2002) Private ordering on the Internet: The eBay community of traders. Bus. Politics 4(3):245–274.

Boylu F, Aytug H, Koehler GJ (2008) Systems for strategic learning. Inform. Systems E-Bus. Management 6(2):205–220.

Boylu F, Aytug H, Koehler GJ (2010) Induction over strategic agents. Inform. Systems Res. 21(1):170–189.

Braun S, Dwenger N, Kübler D (2010) Telling the truth may not pay off: An empirical study of centralised university admissions in Germany. B.E.J. Econom. Anal. Policy 10(1):1–38.

Cristianini N, Shawe-Taylor J (2000) An Introduction to Support Vector Machines and Other Kernel-Based Learning Methods (Cambridge University Press, Cambridge, UK).

Dalvi N, Domingos P, Sanghai MS, Verma D (2004) Adversarial classification. Proc. Tenth ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (KDD), Seattle, 99–108.

Dekel O, Shamir O, Xiao L (2010) Learning to classify with missing and corrupted features. Machine Learn. 81(2):149–178.

Goldberg S (2010) Young job-seekers hiding their Facebook pages. CNN. Retrieved March 29, 2010, http://www.cnn.com/2010/ TECH/03/29/facebookjob-seekers/.

Healy PM, Palepu KG (2001) Information asymmetry, corporate disclosure, and the capital markets: A review of the empirical disclosure literature. J. Accounting Econom. 31(1–3): 405–440.

Hirshleifer D, Teoh SH (2003) Limited attention, information disclosure, and financial reporting. J. Accounting Econom. 36(1–3): 337–386.

Insure.com (2010) Can you hide smoking from life insurance companies? Retrieved April 2, 2010, http://www.insure.com/articles/ lifeinsurance/smoking.html.

Zhang J (2011) Linear discrimination with strategic missing values. Disseration, University of Florida, Gainesville, FL.
