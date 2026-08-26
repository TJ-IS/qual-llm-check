---
otero_id: 7972
otero_key: "D4FTUFCM"
title: "Induction over Strategic Agents"
authors: "Fidan Boylu; Haldun Aytug; Gary J. Koehler"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0272"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.122.253.212] On: 25 May 2015, At: 05:57 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR

## Information Systems Research

![](/api/attachments/D4FTUFCM/fulltext/images/e1c06813c18447eda4d163ea9aa7de66dff6ef644928b3baa02bbbabe5b8bbd3.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Induction over Strategic Agents

Fidan Boylu, Haldun Aytug, Gary J. Koehler,

## To cite this article:

Fidan Boylu, Haldun Aytug, Gary J. Koehler, (2010) Induction over Strategic Agents. Information Systems Research 21(1):170-189. http://dx.doi.org/10.1287/isre.1090.0272

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/D4FTUFCM/fulltext/images/ee76dcdcb3ff5ff570d3f593b8f2186688d9c35d8880787a85b172f02141f425.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Induction over Strategic Agents

Fidan Boylu

Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, Connecticut 06269, fidan.boylu@business.uconn.edu

Haldun Aytug, Gary J. Koehler

Information Systems and Operations Management Department, The Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611 {aytugh@ufl.edu, koehler@ufl.edu}

W<sup>e</sup> <sup>study</sup> <sup>the</sup> <sup>problem</sup> <sup>where</sup> <sup>a</sup> <sup>decision</sup> <sup>maker</sup> <sup>needs</sup> <sup>to</sup> <sup>discover</sup> <sup>a</sup> <sup>classification</sup> <sup>rule</sup> <sup>to</sup> <sup>classify</sup> <sup>intelligent,</sup> self-interested agents. Agents may engage in strategic behavior to alter their characteristics for a favorable classification. We show how the decision maker can induce a classification rule that anticipates such behavior while still satisfying an important risk minimization principle.

Key words: discriminant analysis; principal-agent; strategic gaming; generalization; adversarial learning History: Seungin Whang, Senior Editor; Vijay Mookerjee, Associate Editor. This paper was received on May 23, 2007, and was with the authors 3 months for 2 revisions. Published online in Articles in Advance February 19, 2010.

## 1. Introduction and Preliminaries

We study the problem where a decision maker needs to discover a classification rule to classify intelligent agents (e.g., as good credit risks). We assume a timeframe short enough so that true nature of an agent as well as the classification rule of interest (i.e., the concept) does not change. In this timeframe, agents may engage in strategic behavior to alter superficially or disguise intentionally their true characteristics to attain a favorable classification. We show how the decision maker (we call a principal) can induce a classification rule that anticipates such behavior while still satisfying an important risk-minimization principle that we require to control for generalization of the induced rule. By risk we mean the expected cost of misclassification over all instances, seen and unseen. We call this task induction over strategic agents (ISA).

Consider the following three vignettes illustrating several aspects of this problem. In all cases, a positive classification is the desired one. We speak of positive agents as those whose true nature is in the positive class. Similarly, negative agents are agents whose true nature is the negative class.

Vignette 1 (Fraud): Individuals who engage in fraud often attempt to disguise their activities to appear nonfraudulent. A decision maker, such as a certified fraud examiner (see http://www.acfe.com/), trying to assess whether fraud is involved (for example, in occupational fraud) regularly tries to anticipate strategic activities. Innocent individuals not wanting to be classified as engaging in fraud may need to alter their practices, too, so as not to be incorrectly labeled.

Vignette 1 considers the case in which all agents know their true type. Negative agents will attempt to fool the principal (e.g., an examiner or auditor) by altering their observable attributes. The principal should anticipate such activities. True positive agents, too, will anticipate these strategic activities and alter their observable attributes to maintain a clear positive classification. The principal needs to consider this aspect, too.

Vignette 2 (College/MBA Admission<sup>1</sup>): A more typical example is the admission task. Admission boards (i.e., the principals) are increasingly recognizing that true negative or marginally positive applicants might attempt to alter their true attribute values in the short run to achieve a positive classification. For example, getting into a top-tier MBA program has many challenges. Trunk (2007) notes that

A lot of people already know this, which has made the competition to get into a top-tier b-school fierce. So much so that you probably need a consultant (Porter 2007) to help you get in. Wondering how effective those consultants are at gaming the system? So effective that schools are publicly saying they’re trying to change the application process in order to undermine the effectiveness of application coaches.

For the college admission process, better grades in high school courses are likely to positively influence admission to most universities. However, increasing a low high school GPA in one’s senior year is likely very hard for negative or marginally positive students. Other characteristics might be easier to adjust. For example, one attribute often used to discriminate is the level of participation in extracurricular activities. A potential applicant could discern this and make an effort to join clubs, etc. merely to increase his chance of a positive classification by the admission board.

Vignette 2 illustrates several additional issues. First, agents might not know their true type (whether they are college material or not—i.e., whether they are positive or negative agents). Second, some attributes might be harder to alter than others (e.g., grades are harder to improve than increasing the amount of extracurricular activity). Third, agents can often discern what attributes a principal considers in her classification process and the desired direction of change (e.g., better grades, more extracurricular activity). In addition, because inaction by some marginally positive agents might result in their being classified negative, they also will engage in strategic behavior.

Vignette 3 (Credit Approval): Obtaining credit often requires an appropriately good credit score. The principal (i.e., the grantor of credit) computes a credit score based on a number of observable attributes. There are many websites that purport to help increase one’s scores in ways that do not fundamentally alter the true nature of the agent. For example, sites like http://www.repairyourbadcredit.com/ advertise that they have ways to raise one’s credit scores.<sup>2</sup> Ultimately, of course, a principal either grants credit (i.e., labels the agent as a positive case) or not.

Vignette 3 illustrates a second dimension of discrimination—the degree of positive or negative labeling. The principal still uses a classification function that ultimately gives a positive or negative labeling for each case but also can assess the degree to which a case confirms. In credit approval situations, a credit score is often used. This score is compared to a threshold for approval. We note that actions taken to correct errors in a credit report are not what we consider “strategic” changes. Such errors represent noise in attribute measurements. Furthermore, we assume the timeframe necessary to truly change one’s true nature is longer than the usage period of the principal’s classifier.

In summary, with ISA we look at the situation where a principal desires to induce a decision rule that can be used to discriminate between true positive and true negative agents (and, secondarily, that can be used to give scores that show the degree of this labeling). Agents might or might not know their true nature, but all want to be classified positive, so every agent considers possible strategic activity. The fact that an agent might not know their true state is irrelevant to our analysis, because all agents desire a positive labeling and will strive to attain such. We assert that agents can often anticipate attributes that a principal considers important and can assess the effort required to alter these to an acceptable level.<sup>3</sup> We assume the timeframe for induction and usage is short enough that these alterations are strategic rather than fundamental, so the agent’s true nature remains stationary. That is, we do not consider longer-term changes of attributes that might change the true nature of an agent. This stationarity assumption is common in machine learning and data mining applications. As is commonly done, we adopt a rational expectation framework where all parties anticipate the actions of others simultaneously.

When the principal uses her classification rule to make a decision, she needs the attributes of the agent. In many of the scenarios above, this information is provided by the agent (e.g., in credit or admission application forms) but still needs to be verified by the principal (by accessing credit reports, criminal records, etc.). For fraud cases, the principal might have to exert significant effort in determining these attribute values. Furthermore, the costs to the agents to change attributes could include psychological costs that the principal’s actions would implicitly or explicitly force (the latter through assessment and verification processes, perhaps).

The goal of the principal is twofold. First, as part of the induction process she must anticipate strategic agent reaction to her classification rule. Second, she would like to minimize her misclassification costs over all seen and unseen cases. Hence, the principal’s ideal problem is risk minimization subject to anticipating strategic agent behavior.

Because risk is the expected loss over the entire set of instances with respect to an unknown sampling distribution, some additional assumptions are needed to make risk minimization operational. In machine learning, such assumptions are captured by the induction principle being employed. Statistical learning theory (SLT) developed by Vapnik (1998, 1999) uses the structural risk-minimization principle (SRM—discussed below), which has been shown to be quite powerful in a large number of settings (e.g., see Cristianini and Shawe-Taylor 2000). This replaces the risk-minimization goal with minimization of a bound on the overall risk that is independent of the sampling distribution.

We adapt support vector machine (SVM) methodology to solve the principal’s problem using SRM. SVMs explicitly implement the SRM principle using a convex optimization model. SVM algorithms also scale up to very large data sets and have been applied to problems involving text data, pictures, etc. We modify this optimization model to anticipate strategic agent behavior.

We make several contributions to the literature. We show that ISA is reduced to solving a mathematical program. For a base case, we fully characterize solutions as well as provide game theoretic insights to the solution provided. Because the general case (i.e., the case of nonseparable data sets) does not have properties like the base case that can be exploited for theoretical insights, we provide a workable mathematical programming formulation and use general-purpose solvers to obtain solutions in a detailed example. We also discuss game-theoretic issues for the general case.

We proceed as follows. In §2, we review Vapnik’s statistical learning theory that leads to the SRM principle. We then review SVMs whose induction process is driven by the SRM principle. In §3, we adapt the SVM model to take into consideration strategic activities of agents. For a base case, we derive necessary and sufficient conditions for an optimal SVM classifier. We also look at several issues, including game theoretic properties, a disqualification of iterative approaches for finding an ISA solution, a positioning of this research in the literature, and so forth. In §4, we extend the base model to the general case and develop a mathematical programming model that can find optimal solutions to the ISA problem. This model is applied to a credit-risk evaluation example in §5. We conclude with a discussion and possible future research in §6.

## 2. Statistical Learning Theory and Support Vector Machines

Suppose<sup>4</sup> $X \subseteq { \mathfrak { N } } ^ { n }$ contains vectors whose n observable components represent values of attributes. (We assume nominal attributes are handled with binary variables in the usual manner—for example, see Maudes et al. 2007.) X consists of cases consistent with some underlying but unknown concept (called the positive examples of the underlying concept) and the remaining cases (negative examples). A typical task in data mining, machine learning, and pattern recognition is to sample X, determine the true label and attribute values of each example, and learn a classifier from these examples.

In such situations, the concept of interest is assumed fixed but unknown. The observable relevant attributes of interest are assumed given. During the induction process, a decision maker observes instances drawn randomly with replacement from X each having a true label 1 or 1 denoting whether it is a negative or positive example of the concept. These labels are not normally observable, but during the induction process we assume that such labels are available, perhaps through extensive study or from past outcomes. This is a key assumption of this paper, that the principal can determine the true nature of the agents in the sample over which she will perform her induction.

As to the attribute values observed by the principal, these might have been subject to previous strategic actions by agents. On reflection, there are two

Table 1 Summary of Notation

<table><tr><td colspan="2">General</td></tr><tr><td>*</td><td>Used to denote an optimal value as in  $w^{*}$ .</td></tr><tr><td>,</td><td>Vector transpose as in  $x'$ .</td></tr><tr><td colspan="2">Agents (subscript i may be suppressed)</td></tr><tr><td>n</td><td>Number of attributes</td></tr><tr><td>X</td><td>Space of agent attribute vectors.  $X \subseteq \Re^n$ .</td></tr><tr><td> $x_i$ </td><td>Agent i&#x27;s vector of attributes.  $x_i \in X$ .</td></tr><tr><td> $y_i$ </td><td>Agent i&#x27;s true class.  $y_i \in \{-1, +1\}$ .  $y_i(x_i)$  Is used to show the class of agent i.</td></tr><tr><td>K</td><td>Number of agent types.</td></tr><tr><td> $d_i(w, b)$ </td><td>Agent i&#x27;s vector of attribute changes for the linear discriminate function given by w and b.</td></tr><tr><td> $d_i$ </td><td>Agent i&#x27;s vector of attribute changes with w and b suppressed.</td></tr><tr><td> $u_i$ </td><td>Agent i&#x27;s disutility function over attribute changes.</td></tr><tr><td> $F_i$ </td><td>Feasible set of altered attributes for agent i.</td></tr><tr><td> $c_i$ </td><td>Positive vector of agent i&#x27;s cost to change attributes.</td></tr><tr><td> $r_i$ </td><td>Agent i&#x27;s reservation cost for attaining a positive classification.</td></tr><tr><td> $t_i$ </td><td>Is the maximum change agent i is willing to make to be classified positive.</td></tr><tr><td>D(w)</td><td>Is a diagonal matrix defined by D(w) $_{j,j}$ = sgn(wj)</td></tr><tr><td> $q_i(w, b)$ </td><td>Change to the principal&#x27;s classification by agent i.  $q_i(w, b) = w'D(w)d_i^*(w, b)$ .</td></tr><tr><td> $z_i^*(w, b)$ </td><td>Minimum cost change to achieve a positive classification by agent i given by w and b.</td></tr><tr><td>k or j*</td><td>Used to signify an attribute selected by an agent for change.</td></tr><tr><td colspan="2">Support vector machine</td></tr><tr><td>w</td><td>Vector of weights for the linear discriminate function.</td></tr><tr><td>b</td><td>Intercept for the linear discriminate function.</td></tr><tr><td> $\xi_i$ </td><td> $\xi_i = \max(0, 1 - y_i(w'x_i + b))$ </td></tr><tr><td>C</td><td>Positive trade-off parameter between margin and training error.</td></tr><tr><td> $C_y$ </td><td>Positive trade-off parameter for an agent of type y ∈ {−1, +1}.</td></tr><tr><td>η</td><td>Confidence parameter.</td></tr><tr><td>h</td><td>Capacity measure.</td></tr><tr><td>Δ</td><td>Geometric margin.</td></tr><tr><td>R</td><td>A bound on the norm of  $x_i \in X$ .</td></tr><tr><td colspan="2">Principal</td></tr><tr><td>S</td><td>Training sample, S = (( $x_1, y_1), \ldots, (x_i, y_i)$ ).</td></tr><tr><td>f</td><td>True classification function,f: X → {−1, +1}. For linear discriminant functions f(x) = w&#x27;x + b ≥ 0 → +1 and f(x) = w&#x27;x + b &lt; 0 → −1.For a “Δ-margin” f(x) = w&#x27;x + b ≥ 1 → +1 and f(x) = w&#x27;x + b ≤ −1 → −1.</td></tr><tr><td> $\hat{f}$ </td><td>Induced classification function.</td></tr><tr><td colspan="2">MIP:</td></tr><tr><td> $I_j$ </td><td>Binary decision variable.  $I_j = 1$  if  $w_j > 0$  and zero otherwise.</td></tr><tr><td> $H_j$ </td><td>Binary decision variable.  $H_j = 0$  if  $t_i = r_i|w_j|/(c_i)_j$  and one otherwise.</td></tr><tr><td> $V_i$ </td><td>Binary decision variable.  $V_i = 0$  if agent i exerts effort to change his attributes.</td></tr><tr><td> $q_i$ </td><td>Change to the principal&#x27;s classification by agent i.</td></tr><tr><td>λ</td><td>Nonnegative trade-off parameter between positive agent changes and training error.</td></tr><tr><td>M, ε</td><td>Large and small positive value, respectively.</td></tr></table>

types of attribute changes. An agent can make an actual change (albeit not one sufficient to truly change his true label within the usage period of the classifier) to an attribute (join clubs, change accounting practices, etc.) or an agent can take action to deceive or give the appearance of an attribute change (e.g., getting a negative credit report item removed though manipulation). In the first case, the observed attribute values are correct as observed, because why an agent arrived at their current state is usually both unknowable and irrelevant. In the second case, we assume the principal will expend effort in preparing the training set and not only determine each sample’s true nature but also the true attribute values. This should also remove noise in attribute measurements. The collection of these examples forms the training set<sup>5</sup> $S = ( ( x _ { 1 } , y _ { 1 } ) , \dots , ( x _ { l } , y _ { l } ) )$ of l observations where $y _ { i } \in \{ - 1 , + 1 \}$ identifies the label.

The decision maker uses the training set to determine an instance of a representation of the target concept (the hypothesis space) that is embodied as a function $f \colon X \to \{ - 1 , + 1 \}$ , where $f ( x ) = + 1$ if $x \in X$ belongs to the positive class and $f ( x ) = - 1$ if it belongs to the negative class. In the language of learning theory (Vapnik 1998), we are performing “supervised learning” when we infer $\hat { f }$ from a training set $S$ as an estimate of the true function $f .$ The decision maker chooses a general form for ${ \hat { f } } \ ( \mathrm { e . g . }$ , decision trees, linear functions, neural networks, etc.) that constitutes the hypothesis space. Depending on the representation chosen for the target concept, one uses induction methods designed for this class. For example, for representations such as neural networks (Tam and Kiang 1992), decision trees (Quinlan 1986), discriminant functions (Hand 1981), support vector machines (Cristianini and Shawe-Taylor 2000), etc., many methods have been developed to determine an actual $\hat { f }$ given a sample S. The representation choice sets the induction bias and the methodology choice determines the quality of the final $\hat { f }$ found. It might be the case that no selection exists within the chosen hypothesis space that correctly labels the training set. Then, either the methodology reports there is no consistent hypothesis or it chooses one that meets some secondary criterion such as closest fit.

Among the many possible representation choices, linear discriminant functions (LDFs) are arguably the most widely used because they are simple to apply, easy to interpret, and provide good results for a wide range of problems (Hand 1981). In this study we restrict the class of functions, ${ \hat { f } } ,$ over which the principal searches, to $\mathrm { L D F s } . ^ { 6 }$ For binary classification with LDFs, one determines a nonzero vector $w \in \Re ^ { n }$ and a scalar b such that the hyperplane x $w ^ { \prime } x + b = 0 \}$ partitions the n-dimensional space into two half-spaces.

Then, an observed vector $x _ { i }$ is assigned to the positive class if it satisfies $w ^ { \prime } x _ { i } + b \geq 0$ and to the negative class otherwise. That is, $( w , b ) : \mathfrak { R } ^ { n }  \{ - 1 , + 1 \}$ Many approaches have been developed for determining LDFs, but most use the empirical risk minimization principle, which determines a function using the training set by minimizing the empirical risk (i.e., the number or costs of misclassifications in the training data set). This usually leads to over-fitting (Eisenbeis 1987 critiques studies based on over-fitting). Support vector machines offer a powerful alternative method for discovering LDFs by implementing principles from Vapnik’s (1998, 1999) statistical learning theory. SLT attempts to trade off over-fitting in training with generalization ability. In particular, Vapnik uses the SRM principle which trades off hypothesis space complexity with training error to minimize a bound on the overall risk functional. Often a simple hypothesis space underfits giving poor generalization (the overall risk). As the complexity increases, training error decreases and generalization usually improves until, at some point, overfitting begins giving lower empirical error but poor generalization (i.e., higher overall risk). Methods that use the SRM principle choose model complexity to minimize a bound on the overal risk functional. The need for a bound arises because the expected loss over the entire set of instances uses an unknown sampling distribution. Assuming instances are generated by sampling randomly and independently from an unknown but fixed probability distribution $( \mathrm { i . e . , i . \ i . \ d . } )$ , Vapnik (1998, 1999) developed bounds that are tight for some distributions yet valid for all distributions. In particular, it has been shown that, given $S ,$ for any target function, with a probability at least $1 - \eta ,$ , the risk functional can be bounded by the sum of the empirical risk and a term largely capturing what is called the structural risk (see Vapnik 1999 for details). The structural risk is a function of the number of training points, $l ,$ the target confidence level, $\eta ,$ and the capacity, $h ,$ of the target function. The capacity, $h ,$ measures the expressiveness of the target class of functions $( \mathrm { i . e . , }$ the complexity of the hypothesis space). An important class of LDFs of the form $y ( x ) ( w ^ { \prime } x + b - \Delta ) \ge 0$ with functional margin equal to 1 are termed $\Delta$ margin LDFs. For this class, the capacity, $h ,$ is bounded above by $1 + \operatorname* { m i n } ( n , { \lceil R ^ { 2 } / \Delta ^ { 2 } \rceil } )$ . Here $x \in X \subset \mathfrak { N } ^ { n }$ implies $\| x \| \leq R$

When applied to separable data sets, the SRM principle of minimizing the Vapnik bound on the risk functional is equivalent to minimizing the capacity, $h ,$ which, in turn, is equivalent to maximizing the geometric margin . SVMs output an LDF that maximizes the margin which is the geometric distance of support vectors to the separating hyperplane x $w ^ { \prime } x _ { i } + b = 0 \}$ Support vectors are sample points that lie closest to this hyperplane.

The (functional) margin of a point is defined as $y _ { i } \{ w ^ { \prime } x _ { i } + b \}$ . The absolute value of $w ^ { \prime } x _ { i } + b$ measures how close a point is to the separating hyperplane. One can easily use this information to create three separate categories: definitely negative, definitely positive, and needs further investigation. The closer a point to the separating hyperplane, the lower the confidence in the classification of that point.

There are several versions of SVM models tracing to which norm is used to measure distances and to properties of the training set (such as separability). The hard-margin model is used for separable data sets. It uses the 2-norm for measuring distance. This model discovers LDFs by solving

$$
P 1: \quad \min _ {w, b} w ^ {\prime} w \quad \text { s.t. } \quad y _ {i} \{w ^ {\prime} x _ {i} + b \} \geq 1 \quad i = 1, \ldots , l.
$$

This formulation produces a maximal margin hyperplane with a geometric margin equal to $\Delta = 1 / \| w \| _ { 2 }$ when the functional margin of the hyperplane is fixed at 1 (Cristianini and Shawe-Taylor 2000.) That is, maximizing  is equivalent to minimizing $\| \boldsymbol { w } \| _ { 2 }$ or simply minimizing $w ^ { \prime } w$ . The constraints in P1 set the functional margin to 1. Tight constraints are associated with support vectors. Using 1-norm to measure distances results in a linear program (see Cristianini and Shawe-Taylor 2000, Fung and Mangasarian 2002). In either case, the resulting problem is a convex minimization over linear inequality constraints (and hence have a global optimal solution) so SVMs escape the problem of local optima faced by many other learning methods.

In general, the sample space might not be linearly separable. In such cases, the 2-norm SVM problem can be formulated with the introduction of marginslack variables as follows:

$$
\begin{array}{l l} \min_ {\substack {\xi \geq 0 \\ w, b}} & w ^ {\prime} w + C \sum_ {i = 1} ^ {l} \xi_ {i} \\ \text{s.t.} & y _ {i} (w ^ {\prime} x _ {i} + b) \geq 1 - \xi_ {i} \quad i = 1, \ldots , l, \end{array}
$$

where $\xi _ { i } = \operatorname* { m a x } ( 0 , 1 - y _ { i } ( w ^ { \prime } x _ { i } + b ) )$ and C is a positive parameter. Here the SRM principle reduces to minimizing a linear trade-off of the capacity (as captured by the margin) and the classification error. $C$ trades off between margin maximization and training error minimization. This is the soft-margin SVM (Cristianini and Shawe-Taylor 2000). As in the hard margin model, there is a 1-norm counterpart.

## 3. Learning While Anticipating Strategic Behavior

In this section we start by adapting SVM to incorporate strategic gaming. We then characterize a base case providing necessary and sufficient conditions for an ISA solution. Following this, we illustrate the result and then look at several issues including game theoretic properties, a disqualification of iterative approaches for finding an ISA solution, a positioning of this research in the literature, and a reflection on the SRM principle in this setting.

## 3.1. The Agent Strategic Move Problem

We assume the principal can assess the costs to an agent to change an attribute value. Assume a disutility function $u _ { i }$ is given for agent i to change his true attribute vector $x _ { i } \in \Re ^ { n }$ to $x _ { i } + d _ { i } \in F _ { i } ,$ where $F _ { i }$ is the set of possible altered vectors of attributes. We assume that the reservation cost of being labeled a positive example is $r _ { i }$ for agent i. That $\mathrm { i s } , r _ { i }$ is the highest disutility (i.e., effort) an agent will endure to change his attributes to obtain a positive labeling.

We further assume a rational agent will engage in strategic behavior if

$$
r _ {i} \geq \min _ {x _ {i} + d _ {i} \in F _ {i}} u _ {i} (d _ {i}) \quad \mathrm{s.t.} \quad \hat {f} (x _ {i} + d _ {i}) = + 1.\tag{1}
$$

Here an agent determines a feasible, minimum cost change vector to attain a positive labeling.

Thus, we envision a situation where the original instance space, $X ,$ is possibly perturbed after $\hat { f }$ is discovered by the principal, even if $\hat { f }$ is kept secret. Most induction methods will operate using a sample from $X .$ However, we contend that strategic behavior will result in a change $X _ { \widehat { f } } ^ {  } \bar { X }$ from which future instances will be observed. This needs to be anticipated. In our setting, $\hat { f }$ is a -margin LDF (i.e., $\hat { f } ( x _ { i } + d _ { i } ) = + 1$ translates to $w ^ { \prime } ( x _ { i } + d _ { i } ) + b - 1 \geq 0 . \rangle$ 0

If the principal’s classification function was known to rational agents, they would solve what we call the strategic move problem, Equation (1), to determine how to achieve (or maintain) positive classification under the principal’s LDF at minimal cost to themselves. We make two simplifying assumptions to Equation (1). First, we assume that all agent disutility functions are linear. Using linear functions permits initial insights into this type of learning without the complications that arise with non-linear utilities. Second, we adopt assumptions made by Mannino and Koushik (2000) about agents. Mannino and Koushik (2000) study a problem they refer to as cost minimizing inverse classification problem, which is similar to our agent problem—Equation (1). They seek to find a minimum required change to an instance to reclassify it as a member of a preferred class. They make the following assumptions that enable the problem to be formulated as an optimization problem:

• Attribute domains are real-valued.

• Each attribute can be independently changed, allowing an attribute to be modified without inducing any changes in other attributes.

• Attribute change costs can differ among attributes and are linear functions.

These assumptions represent the most natural way of formulating the problem because deviation from these assumptions creates complications that often lead to intractable problems. For example, for binary attributes, changes could only be made to change a $" 0 ^ { \prime \prime }$ to a $^ { \prime \prime } { 1 ^ { \prime \prime } }$ or vice versa. This would make the agent problem a mixed integer programming (MIP) problem.

Using the Mannino and Koushik assumptions we implement Equation (1) as

$$
\min _ {d _ {i} \geq 0} c _ {i} ^ {\prime} d _ {i} \quad \text { s.t. } \quad w ^ {\prime} [ x _ {i} + D (w) d _ {i} ] + b \geq 1,
$$

where $D ( w )$ is a diagonal matrix defined by $D ( w ) _ { j , j } =$ $\operatorname { s g n } ( w _ { j } )$ and $u _ { i } ( d _ { i } ) = c _ { i } ^ { ' } d _ { i }$ for $c _ { i } > 0$ . If feasible, this problem determines a minimal cost change of attributes, $D ( w ) d _ { i } ,$ needed for a positive classification. This would be undertaken if it does not exceed the reservation cost, $r _ { i } .$ Because this optimization problem has only one constraint (other than nonnegativity constraints), the following can be determined. For nonzero w, let

$$
j ^ {*} \in \underset {j, w _ {j} \neq 0} {\arg \min} \frac {(c _ {i}) _ {j} \max (0 , 1 - (b + w ^ {\prime} x _ {i}))}{| w _ {j} |},
$$

$$
\begin{array}{l} z _ {i} ^ {*} (w, b) = \frac {\max (0 , 1 - (b + w ^ {\prime} x _ {i}))}{| w _ {j ^ {*}} |}, \\ d _ {i} ^ {*} (w, b) = \left\{ \begin{array}{l l} z _ {i} ^ {*} (w, b) 1 _ {j ^ {*}} & \text { if } (c _ {i}) _ {j ^ {*}} z _ {i} ^ {*} (w, b) \leq r _ {i} \\ 0 & \text { otherwise } \end{array} \right.. \end{array}
$$

$z _ { i } ^ { * } ( w , b )$ can be interpreted as the projection of the amount of modification that the agent needs to make on the $j ^ { * }$ th attribute to achieve positive classification with respect to the $( w , b )$ that the principal chooses. For w equal to zero or infeasible strategic move problems, we set $d _ { i } ^ { * } ( w , b ) = 0 .$ . An infeasible move occurs when the needed change gives $c _ { j ^ { * } } z _ { i } ^ { * } ( w , b ) > r _ { i }$ or no move satisfies the constraint w $' [ x _ { i } + D ( w ) d _ { i } ] + b \geq 1$ Notice that if $\left( c _ { i } \right) _ { j ^ { * } } / | w _ { j ^ { * } } |$ is the same for different values of $j ^ { * } ,$ the agent problem has alternate optimal solutions. That is, an agent will be indifferent between multiple $j ^ { * }$ values corresponding to moving in different optimal directions (or convex combinations thereof).

Note that the agent need only adjust one attribute. This is a direct result of our simplifying assumptions. Deviations from these assumptions could easily lead to optimal solutions involving more than one attribute being changed. Several of these are explored in related papers (Aytug et al. 2006, Boylu 2006).

## 3.2. The Base Case

We start with the simplest version of the ISA problem. We assume:

• All agents have the same reservation and change costs (i.e., $r _ { i } = r$ and $c _ { i } = c )$

${ \cal S } = ( ( x _ { 1 } , y _ { 1 } ) , . . . , ( x _ { l } , y _ { l } ) )$ is linearly separable.

These assumptions are removed in the next section. Although highly stylized and unreasonable, these assumptions lead to some basic insights of the more general problem.

3.2.1. Characterization. Using SVM while ignoring strategic behavior is accomplished by solving problem P1. Under ISA the principal anticipates any possible agent actions and solves

$$
\begin{array}{l l} \text {P2:} & \min _ {w, b} w ^ {\prime} w, \\ & \text {s.t.} y _ {i} \{w ^ {\prime} [ x _ {i} + D (w) d _ {i} ^ {*} (w, b) ] + b \} \geq 1 i = 1, \ldots , l. \end{array}
$$

Here each $x _ { i }$ is replaced by $x _ { i } + D ( w ) d _ { i } ^ { * } ( w , b )$ that anticipates the agent’s reaction to a chosen w b.

This problem is no longer a nice convex optimization problem with linear constraints. The constraints are not even piecewise linear convex and/or concave. Nonetheless, the following results characterize an optimal solution to the principal’s problem under strategic behavior by agents. For ease of presentation the proof is in the appendix. The first result views the learning task as a game between the agents and the principal.<sup>7</sup> The main result follows.

<sup>Lemma (Base Case).</sup> An optimal solution to P2 is a Nash equilibrium solution.

Theorem (Base Case). $( w ^ { * } , b ^ { * } )$ solves P1 if and only $i f \left( 2 w ^ { * } , 2 b ^ { * } - t ^ { * } \right) / ( 2 + t ^ { * } )$ solves P2 where t∗ is given by $t ^ { * } = r \operatorname* { m a x } _ { j } | w _ { j } ^ { * } | / c _ { j }$

This theorem states that a principal anticipating strategic behavior will use a classifier that is parallel to the LDF $( w ^ { * } , b ^ { * } )$ determined by P1 without taking into consideration strategic behavior. This hyperplane is a scaled, by $2 / ( 2 + t ^ { * } )$ , and shifted form of the original giving an objective value of P2 strictly smaller than P1’s, so its margin is greater thus producing a tighter bound on the principal’s risk functional. The scaling and shifting depends on the agent’s cost structure.

3.2.2. Illustration. For example, suppose that $c ^ { \prime } = [ 1 2 ] . r = 3$ and we have the following training set:

Positive cases $( y _ { i } = 1 )$

$$
x _ {1} = \left[ \begin{array}{c} 2 \\ 5 \end{array} \right], \quad x _ {2} = \left[ \begin{array}{c} 5 \\ 9 \end{array} \right], \quad x _ {3} = \left[ \begin{array}{c} - 1 \\ 6 \end{array} \right],
$$

Negative cases $( y _ { i } = - 1 )$

$$
x _ {4} = \left[ \begin{array}{c} 4 \\ 4 \end{array} \right], \quad x _ {5} = \left[ \begin{array}{c} 5 \\ 5 \end{array} \right], \quad \text { and } \quad x _ {6} = \left[ \begin{array}{c} 6 \\ 0 \end{array} \right].
$$

Solving P1 gives $w ^ { * \prime } ~ = ~ [ - 0 . 7 2 7 2 ~ 0 . 5 4 5 4 ]$ and $b ^ { * } = - 0 . 2 7 2 7 2 7$ The base case theorem shows that an optimal LDF under strategic behavior is $w ^ { \prime } = \left[ - 0 . 3 4 7 8 3 \ 0 . 2 6 0 8 7 \right]$ and $\textit { b } = \ - 0 . 6 5 2 1 7$ with $t ^ { * } = 2 . 1 8 1 8$ . The result of the base case theorem can be motivated using Figure 1, which shows this training set and initial LDF. Although rational expectation arguments have the principal and agents simultaneously deciding their actions, consider the following sequential reasoning. All agents would try to achieve a positive labeling by changing their true attributes if the cost of doing so does not exceed their reservation cost. However, an astute principal, anticipating such strategic behavior, shifts the P1 hyperplane so no true negative agent will benefit from engaging in such behavior. Because the negative agents have no incentive to change their true attributes, they will not exert effort. However, the marginally positive agents are now in danger of being classified as negative. Positive agents also anticipate the principal’s actions and exert effort to remain positively classified. Thus, roughly speaking, in the end the ones “penalized” for engaging in strategic behavior are not the negative agents but rather the marginal positive agents. The final discriminant function leads to a bigger gap between the two classes than P1s, as shown in Figure 1.

3.2.3. Reflections on Structural Risk Minimization. This bigger gap is consistent with the SRM principle. The base case theorem shows that an optimal solution to the principal’s problem is forcing marginal positive agents to alter their attributes in part to gain better bounds on her risk functional. Now, one may ask whether the assumptions of SLT are still valid under our ISA setting. The two assumptions needed are (1) that sampling is i.i.d. and (2) that the unknown distribution remains fixed under the induced LDF’s usage. Regarding the first point, we see no introduction of behavior affecting i.i.d. provided one could make such an assumption without considering gaming by agents.<sup>8</sup> Regarding the latter, we argue that if gaming is not anticipated (and agents game the system), the resulting distribution will be different than that during the induction process. We anticipate these new distributions directly. Not anticipating such actions would negate the second assumption.

3.2.4. Nash Equilibrium and Pareto Solutions. The base case theorem’s margin is larger than P1’s, but one need not use this merely to keep negative agents from altering their attributes to gain a positive

Figure 1 Base Case Theorem  
(a)  
![](/api/attachments/D4FTUFCM/fulltext/images/d1c5e372fabf95f8834e149af7c6aaace108fdcf1a93532989007628575fc02c.jpg)

![](/api/attachments/D4FTUFCM/fulltext/images/b7f2be20b4276da542f4793772bc9591c3d601e17821c2e23199b780eead02e7.jpg)

(c)  
![](/api/attachments/D4FTUFCM/fulltext/images/d6edbed8acffa5f74a203e04421fce50536ab1284a38a0155d90e25332031a02.jpg)

![](/api/attachments/D4FTUFCM/fulltext/images/579ed2c7a1c976bdb40615358befc0fa79fe1a9b22e8020125acf49c0d95f563.jpg)  
Notes. (a) With a P1 LDF, two negative points would change an attribute enough to be classified as positive. (b) P2 shifts this LDF, causing two positive points to have to move to stay classified as positive. (c) The two negative points gain nothing by moving, so they would not do so (thus figuratively returning to thei original positions). (d) The final LDF with wider margins reflects these anticipated steps.

classification. Any feasible solution to P2 will accomplish this. While the optimal margin is $( t ^ { * } / 2 + 1 ) / \| w ^ { * } \|$ , any margin greater than $( t ^ { * } / 2 ) / \| w ^ { * } \|$ will correctly label all negative agents as negative. Thus, it is easy to see that $( w ^ { * } , \bar { b } )$ is pareto optimal for all $\overline { { b } } \in$ $( 0 . 5 t ^ { * } , 0 . 5 t ^ { * } + 1 ] / \| w ^ { * } \|$ . So a principal can choose any of the parallel hyperplanes giving geometric margins between $( 0 . 5 t ^ { * } , 0 . 5 t ^ { * } + 1 ] / \| w ^ { * } \|$ . Hence the principal is left with a trade-off between forcing marginal positive agents to make large changes versus possibly increasing the bound on her risk functional. In an actual application, a principal might elect to choose a different pareto optimal solution with smaller margin to spare marginal positive cases the extra effort needed to be labeled positive (for example, a principal concerned about social welfare). However, as shown, the solution to P2 is a Nash equilibrium, so the principal has no incentive to do so. Initially, an agent wouldn’t know how a principal acts. Of course, over time, had the principal chosen a smaller margin, marginal positive agents would likely surmise this by comparing notes on blogs or other means.

3.2.5. Possible Invalidity of Iterative Induction. What if the base case theorem (or P2) isn’t used, but rather an iterated form of P1? As illustrated with the Dalvi et al. (2004) paper (discussed in §3.3), this is a typical approach—learn a new classifier using data resulting from strategic behavior. Interestingly, if a nonstrategic principal were to use the normal SVM methods on the new instance space, $\begin{array} { r } { \overline { { X } } \mathrm { ~ ( i . e . , } } \end{array}$ , resulting from $X _ { \widehat { f } } ^ {  } \bar { X } )$ , using the same agents to form a training set, they may not produce the same result with the altered versions of the original sample as P2. The following example illustrates this. For example, suppose that instead of using the shifted classifier that incorporates the effects of strategic behavior, the principal chooses to use one found by P1 and updates the classifier after obtaining observed attributes (now reflecting strategic behavior). We assume these iterated rounds are short enough to cumulatively fall within the original usage timeframe so we can track the same set of training examples as they play out their strategic actions. For example, solving P1 for the sample formed used above yields $w ^ { * \prime } = ( - 0 . 7 2 7 2 ~ 0 . 5 4 5 4 )$ and $b ^ { * } = - 0 . 2 7 2 7 2 7$ . Realizing that the principal will use the hyperplane $( w ^ { * } , b ^ { * } )$ in the first round, agents will adjust their attribute vectors, giving

$$
d _ {1} (w ^ {*}, b ^ {*}) = d _ {2} (w ^ {*}, b ^ {*}) = d _ {3} (w ^ {*}, b ^ {*}) = d _ {6} (w ^ {*}, b ^ {*}) = 0,
$$

$$
d _ {4} (w ^ {*}, b ^ {*}) = \left[ \begin{array}{c} 2. 7 5 0 2 \\ 0 \end{array} \right], \quad \text { and } \quad d _ {5} (w ^ {*}, b ^ {*}) = \left[ \begin{array}{c} 3 \\ 0 \end{array} \right].
$$

As a result of strategic behavior, the principal would observe the following perturbed sample:

$$
x _ {1} = \left[ \begin{array}{c} 2 \\ 5 \end{array} \right], \quad x _ {2} = \left[ \begin{array}{c} 5 \\ 9 \end{array} \right], \quad x _ {3} = \left[ \begin{array}{c} - 1 \\ 6 \end{array} \right],
$$

$$
x _ {4} = \left[ \begin{array}{c} 1. 2 4 9 8 \\ 4 \end{array} \right], \quad x _ {5} = \left[ \begin{array}{c} 2 \\ 5 \end{array} \right], \quad \text {and} \quad x _ {6} = \left[ \begin{array}{c} 6 \\ 0 \end{array} \right].
$$

In the second round, the principal will adjust the hyperplane using the normal SVM solution with the perturbed sample observed after the first period. However, the sample observed after the first round is no longer linearly separable $( x _ { 1 }$ and $x _ { 5 }$ are the same point), so the principal will use the soft-margin SVM in Equation (2) (say with $C _ { 1 } = 1$ and $C _ { - 1 } = 5$ reflecting a greater penalty for mislabeling a negative case). Solving for $( w ^ { * } , b ^ { * } )$ for the second round yields $w ^ { * } { } ^ { \prime } =$  0	4 0	8 and $b ^ { * } = - 4 . 2$

Notice that $c _ { j } / | w _ { j } |$ is the same for $j = 1 , 2 ,$ , so the agent problem has alternate optima. That is, the agent can choose to alter any of the two attributes because they yield the same objective value min $c ^ { \prime } d _ { i } = 5 .$ . For simplicity, we assume that all agents will choose to move in the smallest indexed attribute in case of alternate optima so $j ^ { * } = 1$ for our case. Calculating $z _ { i } ^ { * } ( w , b )$ for these points gives

$$
\begin{array}{r} z _ {1} ^ {*} (w, b) = 5, \quad z _ {2} ^ {*} (w, b) = 0, \quad z _ {3} ^ {*} (w, b) = 0, \\ z _ {4} ^ {*} (w, b) = 6. 2 4 9 8, \quad z _ {5} ^ {*} (w, b) = 5, \quad \text {and} z _ {6} ^ {*} (w, b) = 1 9. \end{array}
$$

For $r = 3$ , none of the points on the negative side of the hyperplane satisfy the constraint $c _ { j ^ { * } } z _ { i } ^ { * } ( w , b ) \leq r$ so $d _ { i } ^ { * } ( w , b ) = 0$ for all cases. Accordingly, after the second round nothing changes so solving for $( w ^ { * } , b ^ { * } )$ yields the same hyperplane and thus strategic behavior ends in the second round.

Figure 2 displays the hyperplane that solves P1 and the final hyperplane of the iterative approach. The iterative procedure did not find the optimal solution of P2, which is superior because it has a larger margin yielding a tighter bound on the principal’s risk functional and also prevents the movements of all negative instances, unlike the ending hyperplane of the iterative approach.

Figure 2 Multiround Nonstrategic SVM  
![](/api/attachments/D4FTUFCM/fulltext/images/3bb4469c0932059d618f974ce9d181346260e98ada8cc5436622bdbdf6ea4233.jpg)

![](/api/attachments/D4FTUFCM/fulltext/images/c78563770194012369d2c55721c1d81a93309ef647f2f037312bb0493a8337f2.jpg)  
Notes. (a) Shows the movement of negative points after the SVM LDF is announced. (b) Shows a new SVM based on these moved points.

Before presenting the general case, we discuss some related literature.

## 3.3. Related Literature

Independent of our results, Dalvi et al. (2004) presented a model somewhat similar to ours called adversarial learning. They formulate the problem as a game with two players, one named adversary and the other classifier. The adversary has known costs and utility, is able to control the attributes of observations, and aims to alter true negative observations to mislead the classifier into classifying them as positive. In our terminology, the classifier is the principal. They show that some realizations of the adversarial classification game always have a Nash equilibrium. However, finding a Nash equilibrium is prohibitive in the general case so they focus on a single-shot version of the game in which they assume one move by each of the players. The classifier publishes a classification rule $( \mathbf { C } _ { 0 } )$ before the game, and the adversary modifies the sample points to fool $\mathrm { C } _ { 0 } ,$ but knowing that the adversary will engage in such behavior the classifier actually uses a new classification rule $( \mathsf { C } _ { 1 } )$ The authors focus on a naïve Bayes classifier (NBC) and show that updating NBC based on the expectation that the adversary will try to alter the observations yields better results. For induction, they provide an MIP model and a heuristic algorithm, which are then applied to an application of spam filtering where spammers (agents) quickly adapt their e-mail tactics to circumvent spam filters. They also make the assumption (as we do), standard in game theory, that all parameters are known to each player.

While our task is similar to that studied in Dalvi et al. (2004), we outline some major differences between our approaches. First, our model takes generalization as the principal’s main goal, subject to anticipating agent strategic behavior. Dalvi et al. consider only gaming per se and try to limit the adversary for one period. They mainly look at a single-shot version of the game and touch briefly on a repeated version.

The repeated version is when the players continue to make moves indefinitely since, in their scenario, after the classifier reveals the classification function, both parties can continue playing the game for another round. They specify that the repeated version is computationally intractable and that the classifier and adversary never reach equilibrium. This is similar to the iterative scenario that we have described earlier and showed that such iteration may not produce a Nash equilibrium. We prevent this arms race by providing a Nash solution.

Second, our formulation models a multi-agent game in which one principal and many negative and positive agents are players of the game. Third, assuming that our observations are actual agents engaging in strategic behavior, we focus on the case where the agents belonging to either class may alter their own attributes. Dalvi et al. (2004) consider the case where only one negative agent engages in strategic behavior. This is a major difference. As we show in our base case theorem, only marginal positive agents must act strategically and change their attributes. Finally, we use SVMs as our learning algorithm because it implements the SRM principle. The linear classifier induced by support vector machines is also very easy to interpret as a scoring function.

With the exception of the Dalvi et al. (2004) paper and our earlier drafts, ISA approaches have not been used before. However, learning problems involving intelligent agents in a gaming situation have been investigated in other settings that are concerned with the decision making of utility-maximizing individuals in their interactions with one another and their environment. In some settings, a group of agents repeatedly play a game against their neighbors and adapt their actions to the past behavior of their opponents (Littman and Stone 2001). In other settings, for example in leader-follower systems, a leader (i.e., our principal) decides on and announces an incentive to induce followers $( \mathrm { i . e . , }$ our agents) to act in a way that maximizes the leader’s utility, while the followers maximize their own utilities under the announced incentive scheme. This is somewhat analogous to our setting because the leader tries to identify and announce the ultimate decision rule that would maximize her objective while the followers seek to maximize their own utilities. In both cases, this can be viewed as the leader trying to maximize some kind of a social welfare function given the self interested actions of the followers. These kinds of decisions are termed incentive Stackelberg games (Von Stackelberg 1952), where the leader first determines an incentive function and announces it; and the followers, after observing the announced incentive, make their own decisions. Bhattacharyya and Tharakunnel (2005) apply this kind of a sequential approach to propose a reinforcement-based learning algorithm for repeated game, leader-follower, multi-agent systems. A key point here is the sequential nature of the decisions. Learning takes place progressively as principal and agents interact with each other based on the principles of reinforcement learning (Kaelbling et al. 1996, Sutton and Barto 1998) that uses the idea of trial-anderror learning. As we have shown, iterated approaches might not solve the over-arching problem.

This rising interest in applying machine learning techniques to games in recent years has brought a computational perspective to game-theoretic analysis. Although our research has similarities with this rapidly growing area of research, there are strict distinctions. First, our emphasis is mainly on the properties of the induction mechanism but the gametheoretic properties only followed as a result of the analysis. Second, researchers in computational game theory are concerned mainly with learning in repeated games in multi-agent settings and their criteria seek to answer such questions as “How can an agent learn to maximize its rewards in an environment containing other agents who may also be learning?” Our task also involves agents, but we do not seek to model agent learning in repeated games.

One other line of research that is somewhat related to our problem is utility-based data mining (Melville et al. 2004, Provost 2005). Due to recent growing demand for solving economical problems that arise during the data mining process, there has been interest among researchers to explore the notion of economic utility and its maximization for data mining. So far, the focus has been on objectives like predictive accuracy or minimization of misclassification costs assuming that training data sets were freely available. However, over time it could become costly to acquire and maintain data, causing economic problems in data mining. Utility-based data mining trades off these acquisition costs with predictive accuracy to maximize the overall utility of the principal. While utility-based data mining is concerned with the principal’s utility, ISA additionally considers the possibility that the objects of classification are self-interested, utility maximizing and intelligent decision-making units.

Finally, two studies look at the problem of classification when the input data provided by the users might be distorted. As discussed earlier, Mannino and Koushik (2000) study a problem they refer to as the cost-minimizing inverse classification problem, which is similar to our agent problem. As part of a sensitivity analysis with similarity based learning, they seek to find the minimum required change to a case to reclassify it as a member of the preferred class. Jiang et al. (2005) look at the deductive use of a classification rule (a decision tree) where the input data provided by the users might be distorted (due to a number of realistic circumstances, including possible strategic behavior). They provide two methods, input modification (IM) and knowledge modification (KM), to deal with this. IM modifies the observed noisy input to its most likely true value before it is fed to the knowledge base. KM considers modifying the knowledge base to account for distortion. The main idea is to estimate probabilities for true input values based on noisy observations. They assume independence between the attribute values for simplicity and approach the problem as a noise-handling problem by taking corrective action while accounting for modifications after they are observed. Alternatively, we look at the problem from a preventive point of view by anticipating agent modifications in our induction process. Somewhat related is Mookerjee (2001), who presents a model that specifies how economic bias could affect training data where the term bias corresponds to noise in the class variable that occurs in a systematic, nonrandom manner. A debiasing procedure is offered to reduce the effects of expert bias when the expert and the user use different classification costs.

## 4. The General Case

In this section we assume that agents can have their own reservation (r  and change costs (c  and that the training set might not be separable. To satisfy the principal’s objective of risk minimization, we use the soft-margin form of SVM to implement SRM. This provides a natural extension of the base case. Let $C _ { y _ { i } }$ be the penalty associated with the margin shortfall (  of an agent of true type $y _ { i } .$ Let $q _ { i } ( w , b ) = w ^ { \prime } D ( w ) d _ { i } ^ { * } ( w , b )$ be the amount of bias that agent i can introduce to the principal’s classification function $w ^ { \prime } x _ { i } + b - 1$ by engaging in strategic behavior. To the pure model we add one subjective, optional feature. As discussed earlier, a principal may want to trade off tightness of the bound on her risk functional for lowered effort needed by positive agents to stay positive. Later, we argue that a reasonable way to implement this is to penalize positive agent effort by adding $\lambda \sum _ { y _ { i } = 1 } q _ { i }$ to the objective where $0 < \lambda < C _ { + 1 } .$ Setting & to zero removes this optional feature from the model. With this, our general model for ISA is

Table 2 An MIP for the General Case (Formulation P4)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(2-norm)  $\min_{\xi_{i}\geq0}w'w+\sum_{i=1}^{l}C_{y_{i}}\xi_{i}+\lambda\sum_{y_{i}=1}q_{i}$  or (1-norm)  $\min_{\xi_{i}\geq0}\sum_{j=1}^{n}(w_{j}^{+}+w_{j}^{-})+\sum_{i=1}^{l}C_{y_{i}}\xi_{i}+\lambda\sum_{y_{i}=1}q_{i},$ 
s.t. effort  $(y_{i}=+1): w'x_{i}+b+q_{i}\geq1-\xi_{i}$ $M-MV_{i}\geq\xi_{i}$ $MV_{i}\geq q_{i}\geq0$ $t_{i}\geq q_{i}$ 

effort  $(y_{i}=-1): -w'x_{i}-b\geq1-\xi_{i}$ $\xi_{i}\geq2V_{i}$ $1-w'x_{i}-b+MV_{i}\geq t_{i}+\varepsilon$ 

max adjustment:

 $r_{i}(w^{+}+w^{-})_{j}/(c_{i})_{j}\leq t_{i}\leq r_{i}(w^{+}+w^{-})_{j}/(c_{i})_{j}+MH_{i,j}$ $j=1,\ldots,n, i=1,\ldots,l$ $\sum_{j}H_{i,j}=n-1$ $i=1,\ldots,l$ 

absolute value:

 $w=w^{+}-w^{-}$ $M_{I}I_{j}\geq w_{j}^{+}\geq0$ $M_{I}-M_{I}I_{j}\geq w_{j}^{-}\geq0$ $j=1,\ldots,n$ 

integrality:

 $I_{j}, H_{i,j}, V_{i}\in\{0,1\}$
</div>

$$
\begin{array}{l l} \text {P3:} & \min _ {w, b} w ^ {\prime} w + \sum_ {i = 1} ^ {l} C _ {y _ {i}} \xi_ {i} + \lambda \sum_ {y _ {i} = + 1} q _ {i} (w, b), \\ & \text {s.t.} y _ {i} \{w ^ {\prime} x _ {i} + q _ {i} (w, b) + b \} \geq 1 - \xi_ {i} i = 1, \ldots , l, \end{array}
$$

where for $c _ { i } \geq 0$ with at least one j satisfying $0 < ( c _ { i } ) _ { j } < \infty ,$

$$
q _ {i} (w, b) = \left\{ \begin{array}{l l} 0 & \text { if } 1 - b - w ^ {\prime} x _ {i} <   0 \\ & \text { or } 1 - b - w ^ {\prime} x _ {i} > t _ {i} \\ 1 - b - w ^ {\prime} x _ {i} & \text { otherwise }, \end{array} \right.
$$

and $t _ { i } \equiv r _ { i } \operatorname* { m a x } _ { j \ni ( c _ { i } ) _ { i } \neq 0 } | w _ { j } | / ( c _ { i } ) _ { j }$ . In the appendix we show how to solve P3 as an MIP. The final MIP model is shown in Table 2 and is referred to as P4. This also shows the 1-norm counterpart.

The following lemma (discussed in the appendix) shows that the general case has the same equilibrium property as the base $\mathrm { c a s e } , ^ { 9 }$ but no results paralleling the base case theorem are possible.

<sup>Lemma (General Case).</sup> An optimal solution to P3 is a Nash equilibrium solution.

In the next section, we illustrate using P3 via MIP P4 on a credit-risk evaluation problem.

## 5. Sample Application

In this section, we illustrate our general solution procedure for ISA using a credit-risk evaluation data set that is publicly available at the UCI repository (http://www.ics.uci.edu/<sup>\~</sup>mlearn/MLRepository.html) and referred to as credit-screening data. The strategic case results are compared to the results of a nonstrategic solution to highlight the advantages of the strategic solution such as improvements in the number of misclassifications and objective function value. The original data set consists of 690 instances (653 without missing values) with 15 attributes (6 numerical, 9 categorical). We used the 653 cases without missing values. For the purposes of our analysis, all categorical attributes were replaced by binary dummy variables. Thus, the resulting data set has 40 attributes, summarized in Table 3.

Table 3 Converted Credit Data

<table><tr><td>Attribute index (i)</td><td>Type</td><td> $c_k$ </td><td>Attribute index (i)</td><td>Type</td><td> $c_k$ </td></tr><tr><td>0</td><td>Binary</td><td>∞</td><td>8</td><td>Binary</td><td>∞</td></tr><tr><td>1</td><td>Continuous</td><td>3</td><td>9</td><td>Binary</td><td>∞</td></tr><tr><td>2</td><td>Continuous</td><td>7</td><td>10</td><td>Continuous</td><td>1</td></tr><tr><td>3</td><td>Converted to binary</td><td>∞</td><td>11</td><td>Binary</td><td>∞</td></tr><tr><td>4</td><td>Converted to binary</td><td>∞</td><td>12</td><td>Converted to binary</td><td>∞</td></tr><tr><td>5</td><td>Converted to binary</td><td>∞</td><td>13</td><td>Continuous</td><td>4</td></tr><tr><td>6</td><td>Converted to binary</td><td>∞</td><td>14</td><td>Continuous</td><td>9</td></tr><tr><td>7</td><td>Continuous</td><td>2</td><td></td><td></td><td></td></tr></table>

The nonbinary, categorical attributes contained in the original data set (converted to binary variables) and the binary attributes were assigned $\textbf { a } c _ { i }$ value of infinity. This was operationalized in P4 by leaving out the inequalities of Equation (2) corresponding to such $\mathrm { j } \mathsf { s }$ and by reducing the right side of Equation (3) by one for each such j—see the appendix for Equations (2) and (3). Each remaining attribute was assigned an integer cost ranging between 1 and 10. These costs are summarized in Table 3. We randomly selected 300 examples (without replacement) for training, with the remaining 353 used as a holdout set for testing (Table 4).

We solve this problem with K = 2 (i.e., all agents have the same linear cost structure, but the first half of each data set has $r = 1 5$ and the last half has $r = 3 0 )$ . That is, the second type of agent is willing to exert more effort to attain a positive classification. Table 4 shows the breakdown of agent types in the training and test data sets. Furthermore, we set $\varepsilon = 1 0 ^ { - 7 } .$ M 10 000, M 100, $C _ { + 1 } = 5$ and $C _ { - 1 } = 5 . 1$ . We used CPLEX 9.1 (ILOG 2005) to solve all the problems. Tables 5 and 6 summarize our solutions. Table 5 addresses the optimization process performed over the training set, while Table 6 looks at generalization results using the test set (we also show the results for training and test sets combined).

The first two columns of Tables 5 and 6 show the usual nonstrategic SVM solution and the ISA solution (both with $\lambda = 0 )$ . Subsequent columns for ISA have increasing & values. The number of positive and negative agents who strategically moved is the number of agents that could alter their attributes to achieve a positive labeling. The solutions to P4 provide several significant improvements over their nonstrategic counterpart. First, strategic solutions perform better in terms of the total number of misclassifications. Second, we see a reduction in the number of negative misclassifications for strategic solutions when compared with the nonstrategic counterparts. This holds true for both the training and holdout test sets. A striking result is the change in the number of negative agents who can strategically alter their attributes to attain a positive labeling with the nonstrategic LDF. The nonstrategic solution has 287 (out of 383 total negative agents) able to change their labeling. Strategic solutions have from 21 to 61, depending on the lambda value. As expected, the strategic formulation forces positive agents to take preventive action if possible to keep from being misclassified. We see many more such moves than in the nonstrategic solution. We also see a much smaller norm for the strategic solution with $\lambda = 0 ,$ , indicating a larger margin. As a result, a better risk functional bound is likely. As discussed after the base case theorem, a principal might want to exchange some margin for lower required effort by positive agents (note the different results for different lambda values). The down side of this optional use of P4 could be a smaller margin and thus a looser bound on the principal’s risk functional. We see this in Table 5 for $\lambda \in \{ 2 , 3 \}$ as the principal gives up margin-easing positive effort and misclassification costs. Comparing the nonstrategic and strategic results, we see a dramatic drop in objective value with strategic moves in Table 5 (from 1489.472 to 244.879), emphasizing the high payoff gained by ISA.

Table 4 Types of Agents in the Training and Test Data Sets

<table><tr><td></td><td>Training set</td><td>Test set</td></tr><tr><td>Positive agents with  $r = 15$ </td><td>71</td><td>70</td></tr><tr><td>Negative agents with  $r = 15$ </td><td>79</td><td>107</td></tr><tr><td>Positive agents with  $r = 30$ </td><td>68</td><td>87</td></tr><tr><td>Negative agents with  $r = 30$ </td><td>82</td><td>89</td></tr></table>

Furthermore, when strategic results are compared for increasing values of &, we see an increase in the objective values as & increases from left to right in the table. This is a result of penalizing the objective function more for each movement of positive agents as & is increased. This forces fewer positive agents to move and hence causes an increase in the positive misclassification cost.

Table 5 1-Norm Strategic SVM Solutions (P4) vs. Nonstrategic

<table><tr><td colspan="3">Nonstrategic</td><td colspan="4">Strategic</td></tr><tr><td>Training set</td><td> $\lambda = 0$ </td><td> $\lambda = 0$ </td><td> $\lambda = 1$ </td><td> $\lambda = 2$ </td><td> $\lambda = 3$ </td><td> $\lambda = 4$ </td></tr><tr><td># Positives moved</td><td>26</td><td>116</td><td>53</td><td>36</td><td>31</td><td>23</td></tr><tr><td># Negatives moved</td><td>138</td><td>15</td><td>6</td><td>7</td><td>6</td><td>3</td></tr><tr><td># Pos. misclassifications</td><td>0</td><td>5</td><td>7</td><td>7</td><td>7</td><td>12</td></tr><tr><td># Neg. misclassifications</td><td>144</td><td>23</td><td>21</td><td>26</td><td>27</td><td>30</td></tr><tr><td> $\|w\|$ </td><td>10.71078</td><td>6.13573</td><td>10.52400</td><td>12.19895</td><td>11.58192</td><td>10.28913</td></tr><tr><td> $\lambda \sum q_i$  $y_j=1$ </td><td>35.17804</td><td>85.3489</td><td>35.66414</td><td>25.35387</td><td>21.43529</td><td>10.98469</td></tr><tr><td>Objective value(with strategic moves)</td><td>1,489.472</td><td>244.679</td><td>287.698</td><td>316.431</td><td>339.386</td><td>352.583</td></tr><tr><td>Coefficients</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Attribute 1</td><td>0.03275</td><td>0.00248</td><td>0.03621</td><td>0.04660</td><td>0.04273</td><td>0.03535</td></tr><tr><td>Attribute 2</td><td>-0.01096</td><td>-0.00584</td><td>-0.01107</td><td>-0.00822</td><td>-0.00985</td><td>-0.01507</td></tr><tr><td>Attribute 7</td><td>0.03860</td><td>-0.00504</td><td>0.01957</td><td>0.05586</td><td>0.05919</td><td>0.02445</td></tr><tr><td>Attribute 10</td><td>0.23085</td><td>0.06893</td><td>0.06667</td><td>0.06614</td><td>0.06118</td><td>0.04210</td></tr><tr><td>Attribute 13</td><td>-0.00281</td><td>-0.00024</td><td>-0.00323</td><td>-0.00355</td><td>-0.00371</td><td>-0.00314</td></tr><tr><td>Attribute 14</td><td>0.00050</td><td>0.00003</td><td>0.00026</td><td>0.00028</td><td>0.00031</td><td>0.00050</td></tr><tr><td>Seconds to solve(3.4 GHz Xeon processor)</td><td>0.094</td><td>187,743</td><td>7,309.769</td><td>1,514.748</td><td>236.567</td><td>21.61</td></tr></table>

It is interesting to note that as & changes from 0 to 4, the total number and relative division of positive and negative misclassifications remains fairly constant, all showing reasonable generalization. However, as & increases, the induced agent movement decreases dramatically (going for 129 and 46 to 36 and 18). This is likely due to the trade-off between & and $C _ { + 1 }$ terms of the objective. As & approaches $C _ { + 1 } ,$ the penalty for forcing positive agents to move becomes similar to the misclassification penalty, so there is less incentive to do so. However, because the number of misclassifications does not increase, it must be that margin maximization dominates misclassification trade-off.

Table 6 Generalization—1-Norm Strategic SVM Solutions (P4) vs. Nonstrategic

<table><tr><td></td><td colspan="2">Non-strategic</td><td colspan="4">Strategic</td></tr><tr><td>Test set</td><td> $\lambda = 0$ </td><td> $\lambda = 0$ </td><td> $\lambda = 1$ </td><td> $\lambda = 2$ </td><td> $\lambda = 3$ </td><td> $\lambda = 4$ </td></tr><tr><td># Positives moved</td><td>43</td><td>129</td><td>62</td><td>39</td><td>37</td><td>36</td></tr><tr><td># Negatives moved</td><td>149</td><td>46</td><td>28</td><td>27</td><td>25</td><td>18</td></tr><tr><td># Pos. misclassifications</td><td>2</td><td>17</td><td>16</td><td>15</td><td>15</td><td>16</td></tr><tr><td># Neg. misclassifications</td><td>172</td><td>57</td><td>59</td><td>63</td><td>62</td><td>60</td></tr><tr><td>Total set</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td># Positives moved</td><td>69</td><td>245</td><td>115</td><td>75</td><td>68</td><td>59</td></tr><tr><td># Negatives moved</td><td>287</td><td>61</td><td>34</td><td>34</td><td>31</td><td>21</td></tr><tr><td># Pos. misclassifications</td><td>2</td><td>22</td><td>23</td><td>22</td><td>22</td><td>28</td></tr><tr><td># Neg. misclassifications</td><td>316</td><td>80</td><td>80</td><td>89</td><td>89</td><td>90</td></tr></table>

As for the coefficients for the continuous attributes (the only attributes we allow to change in this example), two switch signs between the nonstrategic and strategic solutions for &  0. With one exception, the signs remain constant across the strategic solutions. Finally, note that the MIP solution times are very sensitive to lambda values, increasing dramatically as lambda decreases. We have explored heuristics to solve the ISA problem in another paper (Boylu et al. 2007).

## 6. Summary, Discussion, and Future Research

In this paper we adapted SVM methodology to induce LDF classifiers that anticipate possible strategic gaming by agents. We considered two cases. In the base case, all agents have the same attribute change and reservation cost structure (and are separable). We showed that an optimal solution to ISA is a shifted, scaled version of the nonstrategic solution. This solution is a Nash equilibrium. With this solution, true negative agents will have no incentive to change their true attributes, but agents who are marginally positive will be forced to alter their attributes. Thus, roughly speaking, the ones who must exert effort are not the negative agents but rather the marginal positive agents. We also note that under strategic behavior the final discriminant function used by the principal will produce a bigger gap between the two classes of points, resulting in a tighter bound on the principal’s risk functional. In addition, we show that the optimal solution to the base case might not be found by an iterative approach produced by a sequence of strategic, adaptive behaviors by agents, and a nonstrategic principal. This rules out approaches built on multiturn game settings and reinforcement learning type approaches.

For the general case where all agents have different reservation and cost structures, no general statements can be made similar to the base case theorem. For this case ISA can be solved as an MIP model that also provides a Nash equilibrium. We illustrate the general case in a credit card evaluation setting. Solutions shown in Table 5 illustrate the main characteristics of strategic solutions compared to their nonstrategic counterparts. These are largely consistent with the base case theorem.

The assumption that the principal knows the reservation values and costs $( r _ { i }$ and $c _ { i } )$ of each agent is strong. One way to relax this assumption is to assume that the principal, through experience or study, knows that there are different types of agents and discovers associated distributions over these types. Consequently, in solving the strategic problem, the principal has to take into account the fact that one cannot count on known $r _ { i }$ and $c _ { i }$ values. We have explored this elsewhere (Boylu 2006).

An interesting related direction of research is to relax other assumptions on what the principal and the agents know. Economists most commonly focus their analysis of the "principal—agent" problem (Laffont and Martimort 2002) on the cases in which the principal and agents are less omniscient. For example, instead of modeling agent behavior for a given LDF, we might assume that agents know only the signs of the coefficients. Also, it can be assumed that the agents can react to a classifier that is only known with some approximation. It might be the case that agents don’t even know the form of the principal’s function (it might not be an LDF as exemplified by three other studies discussed in our literature review using different classifier forms). In general, relaxing the assumptions on what agents and principal know about each other is an open area of research.

There are many other avenues to investigate. Usually, it might not be realistic to let each attribute be modified unboundedly. This is explored in Boylu (2006) for a particular application. Also, it might be possible for some attributes to be correlated with each other such that it might be a combination of movements in different directions since changing one attribute may cause others to change. More generally, one should examine $x _ { i } + d _ { i } \in F _ { i }$ for particular cases of $F _ { i } .$ . Also, we assume a negative agent remains a negative agent after attribute changes. Allowing for a change of agent type under such alteration is another area of potential research.

An unexplored issue of importance is the application of kernel mappings to SVM under strategic behavior (see Genton 2001). It might be possible to anticipate and cancel the effects of strategic behavior by applying an appropriate kernel mapping alone. Of course, for an agent to anticipate a useful way to alter attributes in some unknown feature space seems unlikely. Ramifications such as these make this approach daunting.

We assumed linear agent disutilities. Relaxing this assumption is a natural extension. An additional area for future consideration is the case where negative agents are willing to expend extreme effort to be positively classified (e.g., suicide bombers trying to get through a security check).

Additional areas of future research include the following. Agent collusion is not considered here. Many possibilities come to mind. Suppose agents collude and offer side payments to other agents (decoys) to make suboptimal changes in their attributes to confuse and thwart the principal. Can this be anticipated in the induction process? Also, we studied a static setting. If the instance space is nonstationary (due to some exogenous factors—for example in the credit granting case where incomes, ages, family size, etc. change over time), can we dynamically model user behavior and determine classifiers that will adapt efficiently? Another twist of this model occurs when the principal seeks real change (not just to thwart superficial change). This might prove useful in public policy settings.

Lastly, the MIP formulation of the general case is unlikely to scale to larger problems. Alternative solution approaches need to be studied. We have investigated a genetic algorithm that shows promise (Boylu et al. 2007). Other ideas come to mind. Because only the support vectors are critical for SVM problems, methods to reduce a large problem set could help avoid the scaling concern.

## Acknowledgments

The authors acknowledge the insightful and detailed reviews provided by three anonymous referees and the area editor.

## Appendix. Proofs

Sketch of Proof for the Lemma (Base case and Gen-<sup>eral Case).</sup> A solution of the base case theorem and an optimal solution for P3 are both Nash equilibriums because in both cases the principal can do no better $( \mathrm { i . e . } ,$ , this is an optimal solution to P2 and P3) and no agent can improve his classification (and hence utility) further. Essentially, at the equilibrium, an agent plays its best response (optimal strat-$\mathrm { e g y } ) , d _ { i } ^ { * } ( w , b )$ , and the principal plays the corresponding best response (for the base case it is $( \bar { 2 } w ^ { * } , 2 b ^ { * } - t ^ { * } ) / \bar { ( 2 + t ^ { * } ) } )$ This argument would hold for the general agent problem of Equation (1).

The base case theorem states that when the training set is separable and all agents have the same cost structure, a solution to the nonstrategic SVM problem (P1) can be shifted to a parallel plane that is a solution to the strategic SVM problem (P2). We start our proof by first showing a simple result.

Supporting Lemma. ${ \mathit { I f } } \left( { \overline { { w } } } , { \overline { { b } } } \right)$ solves P2, then

(a) $d _ { i } ^ { * } ( \bar { w } , \bar { b } ) = 0 f o r \ a l l \ y _ { i } = - 1 .$

(b) $d _ { i } ^ { * } ( \bar { w } , \bar { b } ) = r / c _ { k } 1 _ { k } f o$ r at least one i where $y _ { i } = 1$ and

$$
k = \underset {j, \bar {w} _ {j} \neq 0} {\arg \min} \frac {(c _ {i}) _ {j} \max (0 , 1 - (b + \bar {w} ^ {\prime} x _ {i}))}{| \bar {w} _ {j} |}.
$$

Proof.

(a) Because $( \boldsymbol { \bar { w } } , \boldsymbol { \bar { b } } )$ solves P2 no true negative agent can achieve a positive classification so there is no incentive for such agents to exert effort to alter attributes.

(b) At least one positive support vector will have been moved its maximal amount or else the support vector machine margin can be increased, which would be a contradiction. The maximum move is $r \operatorname* { m a x } _ { k } | \bar { w } _ { k } | / c _ { k }$

Theorem (Base Case). $( w ^ { * } , b ^ { * } )$ solves P1 if and only $i f$ $( 2 / ( 2 + t ^ { * } ) w ^ { * } , ( 2 b ^ { * } - t ^ { * } ) / ( 2 + t ^ { * } ) )$  solves P2 where t∗ is given by $t ^ { * } = r \operatorname* { m a x } _ { j } | w _ { j } ^ { * } | / c _ { j }$

<sup>Proof.</sup> Because S has at least two elements having opposite labels, P1 must have $w ^ { \ast } \neq 0 .$ . Because c and r are positive, $t ^ { * } > 0$ . We first show the feasibility of $( 2 w ^ { * } , 2 b ^ { * } - t ^ { * } ) / ( 2 + t ^ { * } )$ to P2. We break this part of the proof into two parts, one handling positively labeled agents and the other negatively labeled ones. Let $k = \arg \operatorname* { m a x } _ { j } | w _ { j } ^ { * } | / c _ { j }$

Case $y _ { i } = 1 \colon$ : We start by noting that $w ^ { * \prime } x _ { i } + b ^ { * } \geq 1$ for all $y _ { i } = 1$ and is exactly satisfied for positive support vectors. Let i index a positive support vector. Now

$$
\begin{array}{l} z _ {i} \left(\frac {2}{2 + t ^ {*}} w ^ {*}, \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}}\right) \\ = \max \left(0, 1 - \left(\frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} + \frac {2}{2 + t ^ {*}} w ^ {* ^ {\prime}} x _ {i}\right)\right) / \left| \frac {2}{2 + t ^ {*}} w _ {k} ^ {*} \right|, \quad \text { and } \\ 1 - \left(\frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} + \frac {2}{2 + t ^ {*}} w ^ {* ^ {\prime}} x _ {i}\right) = 1 + \frac {t ^ {*}}{2 + t ^ {*}} - \frac {2}{2 + t ^ {*}} (w ^ {* ^ {\prime}} x _ {i} + b ^ {*}) \\ = \frac {2 t ^ {*}}{2 + t ^ {*}}. \end{array}
$$

Furthermore, we need $c _ { k } z _ { i } ( 2 w ^ { * } , 2 b ^ { * } - t ^ { * } ) / ( 2 + t ^ { * } ) \leq r .$ . Now

$$
c _ {k} z _ {i} \left(\frac {2}{2 + t ^ {*}} w ^ {*}, \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}}\right) = \frac {c _ {k}}{\left| \frac {2 ^ {*}}{2 + t ^ {*}} w _ {k} ^ {*} \right|} \frac {2 t ^ {*}}{2 + t ^ {*}} = r \leq r.
$$

Thus,

$$
d _ {i} ^ {*} \left(\frac {2}{2 + t ^ {*}} w ^ {*}, \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}}\right) = z _ {i} \left(\frac {2}{2 + t ^ {*}} w ^ {*}, \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}}\right) 1 _ {k}
$$

is a feasible change of attributes for agent i with $( 2 w ^ { * } , 2 b ^ { * } - t ^ { * } ) / 2 + t ^ { * }$ . Now consider

$$
\begin{array}{l} y _ {i} \left\{\frac {2}{2 + t ^ {*}} w ^ {*} [ x _ {i} + D (\overline {{w}}) d _ {i} ^ {*} (\overline {{w}}, \overline {{b}}) ] + \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} \right\} \\ = \frac {2}{2 + t ^ {*}} w ^ {* \prime} x _ {i} + \frac {2 t ^ {*}}{2 + t ^ {*}} + \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} \\ = \frac {2}{2 + t ^ {*}} (w ^ {* \prime} x _ {i} + t ^ {*} + b ^ {*} - t ^ {*} / 2) \\ = \frac {2}{2 + t ^ {*}} (1 + t ^ {*} / 2) = 1. \end{array}
$$

So after the alteration we see that positive support vector agents become positive support vectors of the new LDF $( 2 w ^ { * } , 2 b ^ { * } - t ^ { * } ) / ( 2 + \bar { t } ^ { * } )$ . Any other positive agent will either not have to adjust attributes (because it was far enough from the original LDF hyperplane) or will have to adjust to a value no greater than $2 { \bar { t } } ^ { * } / ( 2 + t ^ { * } )$

Case $y _ { i } = - 1$ : We start by noting that $\cdot - w ^ { * } { } ^ { \prime } x _ { i } - b ^ { * } \geq 1$ for all $y _ { i } = - 1$ and is exactly satisfied for negative support vectors. Let i index a negative support vector. There are two cases. In the first, the margin of the P1 solution could be larger than the maximal move a negative agent is willing to make, so the agent would gain nothing by moving. This means that $d _ { i } ^ { * } ( \bar { w ^ { * } } , b ^ { * } ) = 0$ . The second case has $d _ { i } ^ { * } ( w ^ { * } , b ^ { * } ) \neq 0 .$ As in the positive case, we focus just on the negative support vectors, noting that any other negative agent either will not have to adjust attributes (because it was too far from the original LDF hyperplane to make a difference) or will have to adjust to a value no greater than at least as much as the support vectors.

Case $d _ { i } ^ { * } ( w ^ { * } , b ^ { * } ) = 0 \colon$ Assume $d _ { i } ^ { * } ( w ^ { * } , b ^ { * } ) = 0 .$ Then we know that $1 - ( b ^ { * } + w ^ { * \prime } x _ { i } ) = 2$ and then that $2 c _ { k } / | w _ { k } ^ { * } | > r$ (since this agent cannot move). Now consider

$$
\begin{array}{r l} 1 - \left(\frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} + \frac {2}{2 + t ^ {*}} w ^ {* ^ {\prime}} x _ {i}\right) & = 1 - \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} - \frac {2}{2 + t ^ {*}} w ^ {* ^ {\prime}} x _ {i} \\ & = 1 + \frac {t ^ {*}}{2 + t ^ {*}} - \frac {2}{2 + t ^ {*}} (w ^ {* ^ {\prime}} x _ {i} + b ^ {*}) \\ & = 2. \end{array}
$$

Then $d _ { i } ^ { * } ( 2 / ( 2 + t ^ { * } ) w ^ { * } , ( 2 b ^ { * } - t ^ { * } ) / ( 2 + t ^ { * } ) ) = 0$ because no move is possible. Thus we have

$$
\begin{array}{l} y _ {i} \left\{\bar {w} ^ {\prime} [ x _ {i} + D (\bar {w}) d _ {i} ^ {*} (\bar {w}, \bar {b}) ] + \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} \right\} \\ = - \frac {2}{2 + t ^ {*}} w ^ {* \prime} x _ {i} - \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} = \frac {t ^ {*}}{2 + t ^ {*}} - \frac {2}{2 + t ^ {*}} (w ^ {* \prime} x _ {i} + b ^ {*}) = 1. \end{array}
$$

This shows that a negative support vector under P1 remains one under the new LDF $( 2 \bar { w } ^ { * } , 2 b ^ { * } - t ^ { * } ) / ( 2 + t ^ { * } )$

Case $d _ { i } ^ { * } ( w ^ { * } , b ^ { * } ) \neq 0 ;$ Assume $d _ { i } ^ { * } ( w ^ { * } , b ^ { * } ) \neq 0 .$ . Then we know

$$
\begin{array}{c} 1 - \left(\frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} + \frac {2}{2 + t ^ {*}} w ^ {* ^ {\prime}} x _ {i}\right) \\ = 1 + \frac {t ^ {*}}{2 + t ^ {*}} - \frac {2}{2 + t ^ {*}} (w ^ {* ^ {\prime}} x _ {i} + b ^ {*}) = 2, \end{array}
$$

and that

$$
\begin{array}{c} d _ {i} ^ {*} \left(\frac {2}{2 + t ^ {*}} w ^ {*}, \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}}\right) = \frac {2}{\left| \frac {2}{2 + t ^ {*}} w _ {k} ^ {*} \right|} 1 _ {k} \\ = \frac {2 + t ^ {*}}{| w _ {k} ^ {*} |} 1 _ {k} = \frac {2}{| w _ {k} ^ {*} |} 1 _ {k} + \frac {r}{c _ {k}} 1 _ {k} > \frac {r}{c _ {k}} 1 _ {k}. \end{array}
$$

So the support vector does not have enough reservation to move to the positive margin hyperplane and thus $d _ { i } ^ { * } ( w ^ { * } , b ^ { * } ) = 0$

$$
\begin{array}{l} y _ {i} \left\{\frac {2}{2 + t ^ {*}} w ^ {* \prime} [ x _ {i} + D (\bar {w}) d _ {i} ^ {*} (\bar {w}, \bar {b}) ] + \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} \right\} \\ = - \bigg (\frac {2}{2 + t ^ {*}} w ^ {* \prime} x _ {i} + \frac {2 b ^ {*} - t ^ {*}}{2 + t ^ {*}} \bigg) \\ = - \bigg (- \frac {t ^ {*}}{2 + t ^ {*}} + \frac {2}{2 + t ^ {*}} (w ^ {* \prime} x _ {i} + b ^ {*}) \bigg) = 1. \end{array}
$$

This shows that a negative support vector under P1 remains one under the new LDF $( 2 w ^ { \ast } , \dot { 2 } b ^ { \ast } - t ^ { \ast } ) / ( 2 + t ^ { \ast } )$

We now start with a solution, $( \boldsymbol { \bar { w } } , \boldsymbol { \bar { b } } ) .$ , to P2. As above, we break this part of the proof into two parts, one handling positively labeled agents and the other negatively labeled ones. We start with $( \boldsymbol { \overline { { w } } } , \boldsymbol { \overline { { b } } } )$ and consider $( ( 2 + t ^ { * } ) \bar { w } _ { \cdot }$ $( 2 + t ^ { * } ) \overline { { b } } + t ^ { * } ) / 2$ as a feasible solution of P1.

Case $y _ { i } ~ = ~ 1 \colon$ We start by noting that $\overline { { w } } ^ { \prime } ( x _ { i } \textrm { } +$ ${ \cal D } ( \bar { w } ) d _ { i } ^ { * } ( \bar { \bar { w } } , \bar { b } ) ) + \bar { b } \geq 1$ for all $y _ { i } = 1$ and is exactly satisfied for positive support vectors. By part b of the supporting lemma, we have there is an i such that

$$
\begin{array}{l} \frac {2 + t ^ {*}}{2} \overline {{w}} ^ {\prime} x _ {i} + \frac {(2 + t ^ {*}) \overline {{b}} + t ^ {*}}{2} = \frac {2 + t ^ {*}}{2} (\overline {{w}} ^ {\prime} x _ {i} + \overline {{b}}) + \frac {t ^ {*}}{2} \\ \qquad = \frac {2 + t ^ {*}}{2} \Big (1 - r \max _ {k} | \overline {{w}} _ {k} | / c _ {k} \Big) + \frac {t ^ {*}}{2} \\ \qquad = 1 + t ^ {*} - r \max _ {k} | 0. 5 (2 + t ^ {*}) \overline {{w}} _ {k} | / c _ {k}. \end{array}
$$

Thus we see that this maximally shifted support vector can be a support vector of an unshifted problem provided $t ^ { * } =$ r max $_ k | \bar { 0 . 5 } ( 2 + t ^ { * } ) \bar { w } _ { k } | / c _ { k }$ . Now consider any other positive agent, call him/her agent j. Then

$$
\begin{array}{l} \frac {2 + t ^ {*}}{2} \bar {w} ^ {\prime} x _ {j} + \frac {(2 + t ^ {*}) \bar {b} + t ^ {*}}{2} = \frac {2 + t ^ {*}}{2} (\bar {w} ^ {\prime} x _ {j} + \bar {b}) + \frac {t ^ {*}}{2} \\ \geq \frac {2 + t ^ {*}}{2} (1 - \bar {w} ^ {\prime} D (\bar {w}) d _ {j} ^ {*} (\bar {w}, \bar {b})) + \frac {t ^ {*}}{2} \\ \geq \frac {2 + t ^ {*}}{2} (1 - \bar {w} ^ {\prime} D (\bar {w}) d _ {i} ^ {*} (\bar {w}, \bar {b})) + \frac {t ^ {*}}{2} \\ = \frac {2 + t ^ {*}}{2} \Big (1 - r \max _ {k} | \bar {w} _ {k} | / c _ {k} \Big) + \frac {t ^ {*}}{2} \\ = 1 + t ^ {*} - t ^ {*} = 1, \end{array}
$$

showing feasibility to P1.

Case $y _ { i } \ = \ - 1 { : }$ We start by noting that $- \boldsymbol { { \overline { { w } } } } ^ { \prime } ( \boldsymbol { x } _ { i } \ +$ $D ( \overline { { w } } ) d _ { i } ^ { * } ( \bar { \bar { w } } , \overline { { b } } ) ) - \bar { b } \geq 1$ for all $y _ { i } = - 1$ and is exactly satisfied for negative support vectors. By part a of the supporting lemma we know $d _ { i } ^ { * } ( \overline { { w } } , \overline { { b } } ) = 0$ for all $y _ { i } = - 1$ . Thus $- \overline { { w } } ^ { \prime } x _ { i } -$ $\overline { { b } } \geq 1$ and is equality for negative support vectors. Consider the following for a negative support vector:

$$
\begin{array}{c} - \frac {2 + t ^ {*}}{2} \overline {{w}} ^ {\prime} x _ {i} - \frac {(2 + t ^ {*}) \overline {{b}} + t ^ {*}}{2} = - \frac {2 + t ^ {*}}{2} (\overline {{w}} ^ {\prime} x _ {i} + \overline {{b}}) - \frac {t ^ {*}}{2} \\ = \frac {2 + t ^ {*}}{2} - \frac {t ^ {*}}{2} = 1. \end{array}
$$

Similarly, for other negative agents we $\mathrm { g e t } \_ { - } ( 2 \ +$ $t ^ { * } \big ) \bar { w } ^ { \prime } x _ { i } / 2 - \bar { ( } ( 2 + t ^ { * } ) \bar { b } + t ^ { * } ) / 2 \bar { \geq } 1 ,$ , showing feasibility to P1.

Above, we showed that an optimal solution, $( w ^ { * } , b ^ { * } ) ,$ to P1 provides a feasible solution, $( 2 w ^ { * } , 2 b ^ { * } - t ^ { * } ) / ( 2 + t ^ { * } )$ to P2 and in the second part we showed that an optimal solution, $( \boldsymbol { \overline { { w } } } , \boldsymbol { \overline { { b } } } )$ , to P2 provides a feasible solution, $( ( 2 +$ $t ^ { * } ) \bar { w } , ( 2 + t ^ { * } ) \bar { b } + t ^ { * } ) / 2 ,$ to P1. The following inequalities must hold:

$$
\begin{array}{c} w ^ {* \prime} w ^ {*} \leq \left(\frac {2 + t ^ {*}}{2}\right) ^ {2} \bar {w}, \bar {w} \quad \text { and } \quad \bar {w} ^ {\prime}, \bar {w} \leq \left(\frac {2}{2 + t ^ {*}}\right) w ^ {* \prime} w ^ {*}, \\ \left(\frac {2}{2 + t ^ {*}}\right) ^ {2} w ^ {* \prime} w ^ {*} \leq \bar {w} ^ {\prime} \bar {w} \leq \left(\frac {2}{2 + t ^ {*}}\right) ^ {2} w ^ {* \prime} w ^ {*}, \quad \text { and   then } \\ \left(\frac {2}{2 + t ^ {*}}\right) ^ {2} w ^ {* \prime} w ^ {*} = \bar {w} ^ {\prime} \bar {w}, \end{array}\tag{SO}
$$

completing the proof.

## Solving P3 as a Mixed Integer Program

We now develop a mixed integer programming model for the ISA problem. To compute $t _ { i }$ we introduce binary variables, $H ,$ to get

$$
r _ {i} | w _ {j} | / (c _ {i}) _ {j} \leq t _ {i} \leq r _ {i} | w _ {j} | / (c _ {i}) _ {j} + M H _ {i, j} \quad j = 1, \ldots , n,\tag{2}
$$

$$
\sum_ {j} H _ {i, j} = n - 1.\tag{3}
$$

Here, for each i, one $H _ { i , j }$ must be zero so $t _ { i } \leq r _ { i } | w _ { j } | / ( c _ { i } ) _ { j }$ for only one j. With this, the lower bound forces $t _ { i }$ to be the maximal value. These constraints need only appear for the K different cost vectors $( c _ { i } = v _ { k } )$ and reservation pairs. That is, although there are l agents there may only be $K \leq l$ unique cost vector and reservation value combinations—the base case theorem assumes $K = 1$

Let $q _ { i }$ be a decision variable representing $q _ { i } ( w , b )$ . The cost of altering attribute $j ^ { \ast }$ is $( c _ { i } ) _ { j ^ { * } } q _ { i } / | w _ { j ^ { * } } |$ where $j ^ { \ast } \in$ arg max ${ \bf \nabla } _ { r _ { i } } | w _ { j } | / ( c _ { i } ) _ { j }$ . However, adding such terms to the SVM objective would yield a nonpositive definite objective. So instead, as discussed earlier, we use a proxy for the agent effort of $\lambda \sum _ { y _ { i } = 1 } q _ { i }$

To evaluate absolute values of components of $w ,$ the usual trick of finding absolute values by $\mathrm { m i n } _ { s _ { k } \geq 0 } \sum _ { j } s _ { j }$ subject ${ \mathrm { t o ~ } } - s \leq w \leq s$ (with any additional constraints) won’t work here because our objective function has other terms impacted by minimizing the sum of the s variables. Hence, we introduce a vector of binary variables, $I ,$ and

$$
w = w ^ {+} - w ^ {-} \quad M I _ {j} \geq w _ {j} ^ {+} \geq 0 \quad M - M I _ {j} \geq w _ {j} ^ {-} \geq 0 \quad j = 1, \dots , n.
$$

Finally, we need to determine the $q _ { i }$ variables. The strict inequalities defining $q _ { i }$ are relaxed using a small perturbation, ). No agent will exert effort to adjust their attributes if the effort does not yield a positive classification. Conversely, if exerting effort (not exceeding the reservation limit) will result in a positive classification, then an agent who would otherwise be classified as negative will exert effort. Consider the case of a negative agent. We implement $y _ { i } \{ w ^ { \prime } x _ { i } +$ $q _ { i } ( w , b ) + b \} \geq 1 - \xi _ { i }$ with the following:

$$
y _ {i} \{w ^ {\prime} x _ {i} + b \} \geq 1 - \xi_ {i} \quad \xi_ {i} \geq 2 V _ {i} \quad 1 - w ^ {\prime} x _ {i} - b + M V _ {i} \geq t _ {i} + \varepsilon ,
$$

where $V _ { i } \in \{ 0 , 1 \}$ , and where $M > 0$ is a sufficiently large and $\varepsilon > 0$ sufficiently small. Table A.1 includes the full implications of these constraints with the objective function that minimizes $\xi _ { i }$ when it is otherwise unconstrained from above. Notice that $q _ { i }$ is not explicitly needed for the negative cases.

Table A.1 Negative Cases

<table><tr><td> $1 - w'x - b$ </td><td> $V$ </td><td> $\xi$ </td></tr><tr><td> $< 0$ </td><td>1</td><td> $1 - y\{w'x + b\} > 2$ </td></tr><tr><td> $\in [0, z]$ </td><td>1</td><td>2</td></tr><tr><td> $> z$ </td><td>0</td><td>0 for  $z \geq 2$  $> 0$  for  $z < 2$ </td></tr></table>

Table A.2 Positive Cases

<table><tr><td> $1 - w'x - b$ </td><td> $V$ </td><td> $q$ </td><td> $\xi$ </td></tr><tr><td> $< 0$ </td><td>0 or 1</td><td>0</td><td>0</td></tr><tr><td> $\in [0, z]$ </td><td>1</td><td> $1 - \{w'x - b\}$ </td><td>0</td></tr><tr><td> $>z$ </td><td>0</td><td>0</td><td> $1 - \{w'x - b\}$ </td></tr></table>

The last case has $V _ { i } = 0 ,$ even though the constraints also allow $V _ { i } = 1$ because the minimization process will force $\xi _ { i }$ (and hence $V _ { i } )$ to zero.

Consider the case of a positive agent. Here we implement $y _ { i } \{ w ^ { \prime } x _ { i } + q _ { i } ( w , b ) + b \} \geq 1 - \xi _ { i }$ with

$$
\begin{array}{r} y _ {i} \{w ^ {\prime} x _ {i} + b + q _ {i} \} \geq 1 - \xi_ {i} \quad M - M V _ {i} \geq \xi_ {i} \geq 0 \\ M V _ {i} \geq q _ {i} \geq 0 \quad t _ {i} \geq q _ {i}, \end{array}
$$

where $V _ { i } \in \{ 0 , 1 \}$ and $M > 0$ is sufficiently large. Table A.2 includes the full implications of these constraints together with the objective function that minimizes $\xi _ { i }$ over $q _ { i }$ when possible.

Table A.2 summarizes the general model. With a 1-norm, the objective term w<sup></sup>w is replaced by $\begin{array} { r } { \sum _ { j } ( w ^ { + } + w ^ { - } ) _ { j } , } \end{array}$ making the 1-norm version of P4 a mixed integer linear program.

## References

Aytug, H., F. Boylu, G. J. Koehler. 2006. Learning in the presence of self-interested agents. Proc. 39th Annual Hawaii Internat. Conf. System Sci. HICSS’06, Kauai, Hawaii. 158b.

Bhattacharyya, S., K. K. Tharakunnel. 2005. Reinforcement learning in leader-follower multiagent systems: Framework and an algorithm. Information Decision Sciences, University of Illinois, Chicago.

Boylu, F. 2006. Strategic learning. Unpublished doctoral dissertation, Decision and Information Sciences, University of Florida, Gainesville.

Boylu, F., H. Aytug, G. J. Koehler. 2007. Using a genetic algorithm to solve the strategic learning problem. Decision and Information Sciences, University of Florida, Gainesville.

Cristianini, N., J. Shawe-Taylor. 2000. An Introduction to Support Vector Machines and Other Kernel-Based Methods. Cambridge University Press, Cambridge, UK.

Dalvi, N., P. Domingos, M. S. Sanghai, D. Verma. 2004. Adversarial classification. Proc. Tenth ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (KDD) Seattle

Eisenbeis, R. 1987. Discussion, supplement to Srinivasan, V. and Kim, Y. H. 1987. Credit granting: A comparative analysis of classification procedures. J. Finance 42(3) 665–680.

Fung, G., O. L. Mangasarian. 2002. A feature selection Newton method for support vector machine classification. Data Mining Institute Technical Report 02–03, University of Wisconsin, Madison.

Genton, M. G. 2001. Classes of kernels for machine-learning: A statistics perspective. J. Machine Learn. Res. 2 299–312.

Hand, D. J. 1981. Discrimination and Classification. John Wiley & Sons, New York.

ILOG, ILOG CPLEX. 2005. Reference Manual and User Manual. V9.1. ILOG, Gentilly, France.

Jiang, Z., V. S. Mookerjee, S. Sarkar. 2005. Lying on the Web: Implications for expert systems redesign. Inform. System Res. 16(2) 131–148.

Kaelbling, L. P., M. L. Littman, A. W. Moore. 1996. Reinforcement learning: A survey. J. Artificial Intelligence Res. 4 237–285.

Laffont, J. J., D. Martimort. 2002. The Theory of Incentives: The Principal-Agent Model. Princeton University Press, Princeton, NJ.

Littman, M., P. Stone. 2001. Implicit negotiation in repeated games. Proc. Eighth Internat. Workshop Agent Theories, Architectures, and Languages ATAL 2001, Seattle, 393–404.

Mannino, M., M. Koushik. 2000. The cost minimizing inverse classification problem: A genetic algorithm approach. Decision Support Systems 29(3) 283–300.

Maudes, J., J. Rodríguez, C. García-Osorio. 2007. M. Haindl, J. Kittler, F. Roli, eds. Multiple Classifier Systems, Vol. 4472, Lecture Notes in Computer Science. Springer-Verlag, Berlin/ Heidelberg, 72–81.

Melville, P., M. Saar-Tsechansky, F. Provost, R. J. Mooney. 2004. Active feature acquisition for classifier induction. Proc. 4th Internat. Conf. Data Mining (ICDM <sub>−</sub> 2004), Brighton, UK, 483–486.

Mookerjee, V. S. 2001. Debiasing training data for inductive expert system construction. IEEE Trans. Knowledge Data Engrg. 13(3) 497–512.

Porter, J. 2007. A booming business in MBA coaches. http://www. businessweek.com/bschools/content/may2007/bs20070524\_906621. htm.

Provost, F. J. 2005. Toward economic machine learning and utility based data mining. Proc. ACM SIGKDD Workshop Utility-Based Data Mining, Chicago, 1.

Quinlan, J. R. 1986. Induction of decision trees. Machine Learn. 1 81–106.

Sutton, R. S., A. G. Barto. 1998. Reinforcement Learning: An Introduction. MIT Press, Cambridge, MA.

Tam, K. Y., M. Y. Kiang. 1992. Managerial applications of neural networks: The case of bank failure predictions. Management Sci. 38(7) 926–947.

Trunk, P. 2007. B-school confidential: MBAs may be obsolete. http://finance.yahoo.com/expert/article/careerist/47722.

Vapnik, V. 1998. Statistical Learning Theory. John Wiley & Sons, New York.

Vapnik, V. 1999. An overview of statistical learning theory. IEEE Trans. Neural Networks 10 988–999.

Von Stackelberg, H. 1952. The Theory of Market Economy. OxfordUniversity Press, London, UK.
