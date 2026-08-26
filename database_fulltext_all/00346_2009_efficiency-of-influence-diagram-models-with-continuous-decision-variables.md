---
otero_id: 346
otero_key: "VZHX4DRX"
title: "Efficiency of influence diagram models with continuous decision variables"
authors: "Barry R. Cobb"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.08.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ef<sup>fi</sup>ciency of in<sup>fl</sup>uence diagram models with continuous decision variables

Barry R. Cobb ⁎

Department of Economics and Business, Virginia Military Institute, Lexington, Virginia, 24450, USA

## a r t i c l e i n f o

Article history: Received 18 November 2008 Received in revised form 2 August 2009 Accepted 30 August 2009 Available online 6 September 2009

Keywords: Accuracy Complexity Continuous variable Decision analysis Decision variable Ef<sup>fi</sup>ciency Graphical model In<sup>fl</sup>uence diagram Mixtures of truncated exponentials Probability

## a b s t r a c t

A measure of ef<sup>fi</sup>ciency for in<sup>fl</sup>uence diagram models with continuous decision variables is presented in order to evaluate whether the additional computational complexity required by a more accurate model is justi<sup>fi</sup>ed. The ef<sup>fi</sup>ciency measure is a multi-objective utility function that considers both the accuracy and complexity of the ID model. Accuracy is determined as the mean squared error between in<sup>fl</sup>uence diagram decision rules and an analytical solution. Complexity is assessed by tracking the run time required to obtain the solution. The resulting ef<sup>fi</sup>ciency score considers the preferences of an individual decision maker for accuracy and complexity. Three in<sup>fl</sup>uence diagram models are compared using the ef<sup>fi</sup>ciency measurement, and an iterative solution procedure is introduced to improve model performance.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

The influence diagram (ID) is a graphical and numerical representation for a decision problem under uncertainty [15]. The ID model is composed of a directed acyclic graph that shows the relationships among chance and decision variables in the problem, as well as a set of conditional probability distributions for chance variables and a joint utility function.

In addition to providing a tractable, intuitive view that facilitates communication about the decision problem, the ID solution provides a strategy for each decision variable in the model and the expected utility from following that strategy. So while the advantages offered by IDs for communicating decision problems led to their invention, these models quickly gained additional attention from researchers for their use in providing a complete mathematical representation of a decision problem that is useful for computational purposes [12]. Subsequently, IDs were integrated into intelligent decision support systems to allow decision strategies to be developed from a dynamic knowledge base [13].

The incorporation of IDs into decision support systems has led to their use in a number of practical applications, including two published recently in Decision Support Systems. IDs have been used to represent a large body of clinical knowledge for extracting suggestions regarding optimal treatment plans in medical decisions [3]. Additionally, a method was designed for using IDs to consolidate information from multiple sources in a decision support system for command and control choices in military applications [5].

This paper evaluates the ef<sup>fi</sup>ciency of ID models that accommodate continuous decision variables using a measure that can aid in determining the model that is most consistent with an individual decision maker's preferences for accuracy and complexity. An example of a decision problem under uncertainty is described below.

## 1.1. Example

A <sup>fi</sup>rm facing uncertain demand must choose production capacity and set product prices [14]. Product demand is determined as

$$
Q (p, z) = 1 2 - p + z,\tag{1}
$$

where P is the product price and Z is a random demand “shock.” Assume $Z \sim N ( 0 , 1 )$ and that the <sup>fi</sup>rm's utility (pro<sup>fi</sup>t) function is

$$
u _ {0} (k, p, z) = \left\{ \begin{array}{l l} (p - 1) \cdot (1 2 - p + z) - k & \text { if } (1 2 - p + z) \leq k \\ (p - 1) \cdot k - k & \text { if } (1 2 - p + z) > k. \end{array} \right.\tag{2}
$$

Notice that the <sup>fi</sup>rm's sales are limited to the minimum of product demand calculated according to Eq. (1) and the established production capacity (K), and that the <sup>fi</sup>rm incurs \$1 in unit variable costs and \$1 in unit capacity costs. Fig. 1 shows an ID model for the capacity planning and pricing decision problem under uncertainty.

All decision variables in this example take values in bounded, continuous (non-countable) state spaces. Only a limited number of methods for directly representing and solving decision problems with continuous decision variables (without discretization) using IDs are available. Some of these methods are discussed in the next section.

![](/api/attachments/VZHX4DRX/fulltext/images/82da6422244e4a0768dbf400d7e0d4e5db2be12a86ba907d6ed1f2802f17caea.jpg)  
Fig. 1. A capacity planning and product pricing problem under demand uncertainty.

## 1.2. Background

Initially, IDs were proposed as a front–end for decision trees [15]. Subsequently, methods for evaluating an ID directly without converting it to a decision tree were developed [23,26]. These methods assume that all uncertain variables in the model are represented by discrete probability mass functions (pmfs) and that decision variables are discrete. Numerous improvements to exact solution procedures for solving discrete IDs have been proposed (see [4] for a comprehensive review of ID research).

Mixtures of truncated exponentials (MTE) in<sup>fl</sup>uence diagrams (MTEIDs) [9], which are in<sup>fl</sup>uence diagrams where probability density functions (pdfs) and utility functions are represented by MTE potentials [22], offer an alternative to using discrete approximations to continuous chance variables in IDs. MTEIDs are solved by using the fusion algorithm for the case where the joint utility function decomposes multiplicatively [28]. Discrete IDs and MTEIDs can only accommodate continuous decision variables if their state spaces are limited to a countable number of discrete values, as demonstrated in examples later in the paper.

Although the above mentioned ID models assume that all decision variables take values in discrete (countable) state spaces. there are some exceptions where continuous decision variables can be accommodated. In Gaussian IDs [27], all continuous chance variables are normally distributed, all decision variables are continuous, and utility functions are quadratic. The mixture-of-Gaussians ID [24,25] requires continuous chance variables to be modeled as mixtures of normal distributions and allows continuous decision variables. An improved solution procedure was later published for IDs constrained under the same conditions as mixture-of-Gaussians IDs that is able to take advantage of an additive factorization of the joint utility function [21]. Another algorithm for solving similarly restricted IDs uses arc reversal operations [20].

The continuous decision MTE in<sup>fl</sup>uence diagram (CDMTEID) [7] allows continuous decision variables with one continuous parent and continuous chance variables having any pdf. Using this approach, pdfs and utility functions are approximated by MTE potentials, which allow the marginalization operation for continuous chance variables to be performed in closed form. This technique develops a piecewise linear decision rule for continuous decision variables and subsequently marginalizes them from the model as deterministic chance variables. The linear nature of the decision rule allows the potential resulting from this operation to be maintained in the class of MTE potentials.

The primary aim of this paper is to answer the question, “When using an ID model to solve a problem with continuous decision variables, is a more accurate model worth the additional computational complexity?” This goal is addressed by developing a tool to compare ID models with continuous decision variables. This “ef<sup>fi</sup>ciency” measurement captures both the accuracy and complexity of the ID solution, and then weighs these in accordance with the preferences of an individual decision maker. Using the ef<sup>fi</sup>ciency metric, the paper compares the competency in performance of ID solutions in three models—discrete IDs, MTEIDs, and CDMTEIDs—where continuous chance variables are modeled directly, i.e. without mixtures of Gaussian distributions, for decision problems with continuous decision variables. A second contribution of this paper is an iterative solution algorithm for IDs with continuous decision variables that improves the accuracy of the resulting decision rules.

The remainder of the paper is organized as follows. Section 2 describes notation and de<sup>fi</sup>nitions used throughout the paper and describes an iterative solution algorithm for IDs with continuous decision variables. Section 3 describes the numerical representation in the three ID models considered for comparison. Section 4 provides details of the measurements used to judge the accuracy, complexity, and ef<sup>fi</sup>ciency of ID models. Section 5 illustrates the solution techniques for the three ID models and shows calculations of accuracy and complexity in these models. Section 6 presents ef<sup>fi</sup>ciency results for the three ID models under varying sets of assumptions. Section 7 concludes the paper.

## 2. Notation and de<sup>fi</sup>nitions

This section introduces notation and de<sup>fi</sup>nitions used throughout the remainder of the paper and an iterative solution algorithm for IDs with continuous decision variables.

## 2.1. Graphical representation

In graphical representations, chance variables in IDs are depicted as ovals and decision variables are depicted as rectangles. Utility nodes appear as diamonds. If C and D are chance and/or decision variables and there is an arrow pointing from C to D, then C is a parent of D. The set of all parents of a variable D is denoted by Pa(D). An arrow pointing to a chance node indicates that the distribution for this chance node is conditional on the variable at the head of the arrow. An arrow pointing to a decision node means that the value of the variable at the head of the arrow will be known at the time the decision is made; thus, the decision strategy must be a function of the observed value of this variable. This set includes all previously made decisions (assuming the no forgetting principle [26]) and observed chance variables.

Example 1. In the ID shown in Fig. 1, K and P are decision variables, Z is a chance variable, and $u _ { 0 }$ is the joint utility function in the problem. The set of parents of P is $P a ( P ) = \{ K , Z \}$

## 2.2. Numerical representation

In this paper, all decision and chance variables take values in bounded, continuous (non-countable) state spaces. All variables are denoted by capital letters in plain text, e.g., A, B, C. Sets of variables are denoted by capital letters in boldface, with Z representing chance variables, D representing decision variables, and X indicating a set of variables whose components are a combination of chance and decision variables. If A and X are one- and multi-dimensional variables, respectively, then a and x represent speci<sup>fi</sup>c values of those variables.

The bounded, continuous state space of X is denoted by Ω . The state space for a single variable B is de<sup>fi</sup>ned as $\Omega _ { B } = \{ b colon b _ { \mathrm { m i n } } \leq b \leq b _ { \mathrm { m a x } } \}$ At certain points in the ID representation and solution, the continuous state space of a set of variables, $\Omega _ { \mathbf { X } } ,$ may be replaced by a discrete approximation. The discretized state space of a set of continuous variables X will be denoted by $\Omega _ { \mathbf { X } } ^ { ( d ) }$

A probability potential, ϕ, for a set of variables X is a function ϕ: $\Omega _ { \mathbf { X } }  [ 0 , 1 ]$ . A utility potential, u, for a set of variables X is a function $\Omega _ { \mathbf { X } }  \mathcal { R } .$ . Utility potentials in this paper are denoted by $u _ { i } ,$ where the subscript i is normally zero for the joint utility function in the problem, and one for the initial approximation to the joint utility function. The subscript can be increased to index additional utility potentials in the initial representation or those created in the solution procedure.

All piecewise functions are implicitly understood to equal zero in unde<sup>fi</sup>ned regions.

Example 2 . In the ID shown in Fig. 1, the state spaces of the variables are expressed as follows: $\Omega _ { K } = \{ k \colon 0 \leq k \leq 1 4 \} ; \Omega _ { P } = \{ p \colon 1 \leq p \leq 9 \}$ ; and $\Omega _ { Z } = \{ z \colon - 3 \leq z \leq 3 \}$

## 2.3. Combination

Combination of potentials is pointwise multiplication. Let $\psi _ { 1 }$ and $\psi _ { 2 }$ be probability and/or utility potentials for $\mathbf { X } _ { 1 } = \mathbf { Z } _ { 1 } \cup \mathbf { D } _ { 1 }$ and $\mathbf { X } _ { 2 } = \mathbf { Z } _ { 2 } \cup \mathbf { D } _ { 2 }$ . The combination of $\psi _ { 1 }$ and ψ is a new potential for $\mathbf { X } { = } \mathbf { X } _ { 1 } \cup \mathbf { X } _ { 2 }$ de<sup>fi</sup>ned as follows

$$
\psi (\mathbf {x}) = (\psi_ {1} \otimes \psi_ {2}) (\mathbf {x}) = \psi_ {1} (\mathbf {x} ^ {\downarrow \Omega_ {\mathbf {x} _ {1}}}) \psi_ {2} (\mathbf {x} ^ {\downarrow \Omega_ {\mathbf {x} _ {2}}})
$$

for all $\mathbf { x } \in \Omega _ { \mathbf { X } } .$ If either $\psi _ { 1 }$ or ψ is a utility potential, the result of the combination will be a utility potential; otherwise, the result is a probability potential.

## 2.4. Marginalization of chance variables

Marginalization of chance variables corresponds to integrating over the chance variable to be removed. Let ψ be a potential for $\mathbf { X } { = } \mathbf { D } \cup \mathbf { Z } \cup Z .$ The marginal of ψ for a set of variables $\mathbf { X } ^ { \prime } { = } \mathbf { D } \cup \mathbf { Z }$ is a potential computed as

$$
\psi^ {\downarrow \mathbf {X} ^ {\prime}} (\mathbf {x} ^ {\prime}) = \int_ {\Omega_ {z}} \psi (\mathbf {x}) d z\tag{3}
$$

for all $\mathbf { x } ^ { \prime } \in \Omega _ { \mathbf { X } ^ { \prime } }$ , where $\mathbf { x } = ( \mathbf { x } ^ { \prime } , \ z )$ . In discrete IDs, the integration operator in Eq. (3) is replaced by summation.

## 2.5. Marginalization of decision variables

Marginalization with respect to a decision variable is only de<sup>fi</sup>ned for utility potentials. Let u be a utility potential for X⋃D, where D is a decision variable. The marginal of u for X is a utility potential computed as

$$
u ^ {\downarrow \mathbf {x}} (\mathbf {x}) = \max _ {d \in \Omega_ {D}} u (\mathbf {x}, d)\tag{4}
$$

for all $\mathbf { x } \in \Omega _ { \mathbf { X } } .$ The mechanics of performing the maximization operation in Eq. (4) varies with each ID model examined in this paper. The nature of the operation for each model will be illustrated by example. More detailed descriptions and de<sup>fi</sup>nitions of these operations can be found for MTEIDs in [9], for CDMTEIDs in [7], and for discrete IDs in [28].

## 2.6. Fusion algorithm

IDs are solved in this paper by applying the fusion algorithm [28], which is relevant for the case where the joint utility function factors multiplicatively. This algorithm involves deleting the variables in an elimination sequence that respects the information constraints in the problem. The sequence is chosen so that decision variables are eliminated before chance or decision variables that are immediate predecessors. When a variable is to be deleted from the model, all probability and/or utility potentials containing this variable in their domains are combined (according to the de<sup>fi</sup>nition in Section 2.3), then the variable is marginalized from the result. The appropriate marginalization operation depends on whether the variable being marginalized is a chance variable (in which case marginalization is de<sup>fi</sup>ned as in Section 2.4) or a decision variable. Section 2.5 describes marginalization of decision variables in general terms. The speci<sup>fi</sup>cs of this operation for each type of ID model will be illustrated by example in Section 5.

## 2.7. Iterative solution procedure

This section presents a new iterative solution algorithm for IDs with continuous decision variables.

The ID methods presented in this paper are sensitive to the state spaces assigned to the decision variables. If the bounded, continuous interval of possible optimal values for the decision variables can be narrowed, the accuracy of the decision rules can be improved.

Denote the set of decision and chance variables in the ID as $\mathbf { D } =$ $\{ D _ { 1 } , . . . , D _ { f } \}$ and $\mathbf { Z } { = } \{ Z _ { 1 } { , } . . . , Z _ { c } \}$ , respectively. The state spaces of the decision variables are denoted by $\Omega _ { \scriptscriptstyle D i } = \{ d _ { i } \colon { d _ { i , \operatorname* { m i n } } } \leq d _ { i } \leq d _ { i } , _ { \operatorname* { m a x } } \}$ for $i = 1 , . . . , f .$ The conditional MTE potential for $Z _ { j }$ given its parents $P a ( Z _ { j } )$ is denoted by $\phi _ { Z _ { i } }$ for each $j = 1 , . . . , c$ and the MTE approximation to the joint utility function is denoted by $u _ { 1 } .$ . An algorithm for solving the ID using an iterative process terminates when both endpoints of the state spaces of each of the decision variables $D _ { i }$ change by less than a bound $\kappa _ { i } .$ The context of the problem may suggest a reasonable error bound for a decision variable. For instance, if price (P) in the example of Section 1.1 can only be changed in increments of \$0.50, a reasonable bound may be $\kappa _ { P } =$ 0.5. The pseudo-code of the algorithm is as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
INPUT:  $u_{1}, \Omega_{D_{1}}, \ldots, \Omega_{D_{f}}, \phi_{Z_{1}}, \ldots, \phi_{Z_{c}}, \kappa_{1}, \ldots, \kappa_{f}$ 

OUTPUT:  $\Theta_{1}, \ldots, \Theta_{f}/^{*}$  A set of decision rules*/

INITIALIZATION

 $\delta_{i}=d_{i,\max}-d_{i,\min}$  for  $i=1,\ldots,f$ 

DO WHILE  $\bigcup_{i=1}^{f} (\delta_{i}&gt;\kappa_{i})$ 

Solve the influence diagram by variable elimination determine  $\Theta_{1},\ldots,\Theta_{f}$ 

FOR i=1:f

 $d_{i,\min}^{*}=\min_{\Omega_{P_{i}(D_{i})}}\Theta_{i}$ $d_{i,\max}^{*}=\max_{\Omega_{P_{i}(D_{i})}}\Theta_{i}$ $\delta_{i}=\operatorname{Max}\{d_{i,\min}^{*}-d_{i,\min}, d_{i,\max}-d_{i,\max}^{*}\}$ 

IF  $|Pa(D_{i})|=\varnothing$ $d_{i,\min}=d_{i,\min}^{*}-(d_{i,\max}-d_{i,\min})/v$ $d_{i,\max}=d_{i,\max}^{*}-(d_{i,\max}-d_{i,\min})/v$ 

ELSE

 $d_{i,\min}=d_{i,\min}^{*}$ $d_{i,\max}=d_{i,\max}^{*}$ 

END IF

END FOR

END DO
</div>

The key part of the algorithm is the calculation of the values $d _ { i , \mathrm { m i n } } ^ { * }$ and $d _ { i , \operatorname* { m a x } } ^ { \ast }$ . These are the smallest and largest values of the decision variable that are optimal when considering all potential values of the parents of the decision variable. Since values of D smaller than $\dot { d _ { i , \mathrm { m i n } } ^ { * } }$ and larger than $\boldsymbol { d } _ { i , \mathrm { m a x } } ^ { * }$ are never optimal, these can be removed from consideration in subsequent iterations.

The revised state spaces created in the algorithm are determined using different rules, depending on whether the continuous decision variable has parent variables or not. The parameter v in the IF statement of the algorithm is the number of discrete bins used in a permanent or temporary (depending on the ID model used) approximation to a continuous decision variable. This is discussed in the description of the ID models in Section 3. In non-terminal iterations of the algorithm, the ID solution interprets the optimal value selected for a continuous decision variable with no parents as an interval, as opposed to a single value. Thus, in subsequent iterations, the state space is narrowed to this interval.

![](/api/attachments/VZHX4DRX/fulltext/images/592a8f309b5572d43807384c83faebfdaba11b3d813ba8b144c3fcd6edca0de5.jpg)  
Fig. 2. An eleven-bin discrete approximation to the N(0,1) distribution over the interval [− 3, 3].

The iterative algorithm improves the accuracy of the ID solution for models with continuous variables for two primary reasons. First, in the MTEID and CDMTEID models, the MTE approximations to the utility functions are more accurate when the domains of variables are narrowed. This will become apparent from the description in Section 3.2. Second, as mentioned previously, each of the models discussed in this paper uses either a permanent or temporary discrete state space for continuous decision variables. When the state space of the decision variables is narrowed, the same number of values can be used in this discrete state space to obtain a better approximation.

The algorithm could also be designed to terminate after a set number of iterations. This iterative algorithm can be applied to any ID model with continuous decision variables that determines approximate decision rules, including the three models demonstrated in the next section.

## 3. In<sup>fl</sup>uence diagram models

This section describes the characteristics of the probability and utility potentials used to represent the example problem from Section 1.1 in each of the three models compared in the paper.

## 3.1. Discrete influence diagrams

In discrete IDs, the state space of each continuous chance and decision variable is limited to a countable number of outcomes. Throughout this paper, the N(0,1) distribution for the chance variable Z in the example of Section 1.1 will be modeled with an eleven-bin discrete approximation (denoted by ψ where $\scriptstyle \psi ( z ) = P ( Z = z ) )$ over the interval [−3, 3], as shown in Fig. 2. This effectively limits the state space of Z to the values $\Omega _ { Z } = \{ - 2 . 7 3 , ~ - 2 . 1 8 , . . . , ~ 0 , . . . , ~ 2 . 1 8 , ~ 2 . 7 3 \}$ which are the midpoints of the discrete bins.

The decision variables will also be limited to discrete outcomes. A v-point discrete approximation to a continuous decision variable D with $\Omega _ { D } = \{ d \colon d _ { \operatorname* { m i n } } \leq d \leq d _ { \operatorname* { m a x } } \}$ has values $d _ { t } = d _ { \operatorname* { m i n } } + ( t - 0 . 5 ) \cdot ( d _ { \operatorname* { m a x } } -$ $d _ { \mathrm { m i n } } ) / \nu$ for $t { = } 1 , . . . , \nu .$ Thus, the discrete state space is de<sup>fi</sup>ned as $\Omega _ { D } ^ { ( d ) } = $ $\{ d _ { 1 } , d _ { 2 } , . . . , d _ { \nu } \} .$

Suppose in the example from Section 1.1 that the variables $K ,$ P, and Z are assigned v, w, and 11 discrete states, respectively. The utility function in the ID is represented as v tables of dimension $( w \times 1 1 )$ , with the t-th table containing the values $u _ { 1 } ( k _ { t } , p _ { u } , z _ { s } ) =$ $( p _ { u } - 1 ) \cdot \mathrm { M i n } \{ k _ { t } , 1 0 - p _ { u } + z _ { s } \} - k _ { t } ,$ calculated according to Eq. (2) for $u = 1 , \ldots ,$ w and $s { = } 1 , { \ldots } , 1 1$ . With $\nu = w = 6 ,$ one such set of utility values appears in Table 1, assuming $K = k _ { 3 } = 5 . 8 3$

3.2. Mixtures of truncated exponentials (MTE) influence diagrams (MTEIDs)

The MTEID model requires all distributions for continuous chance variables to be modeled by MTE potentials and all state spaces of continuous decision variables to be discretized. Each piece of an MTE potential is composed of a sum of exponential terms where the exponent contains a linear function of the independent variable(s). The approximation to the normal pdf with mean, µ, and variance, $\sigma ^ { 2 } ,$ , is modeled by the MTE potential [8] de<sup>fi</sup>ned as

$$
\phi (z) = \left\{ \begin{array}{l} \sigma^ {- 1} \left(- 0. 0 1 0 5 9 2 8 + 1 9 7. 5 8 8 0 2 2 \exp \left\{2. 2 5 6 8 4 3 4 \left(\frac {z - \mu}{\sigma}\right) \right\} \right. \\ \quad - 4 6 2. 6 8 5 7 2 6 \exp \left\{2. 3 4 3 4 1 1 7 \left(\frac {z - \mu}{\sigma}\right) \right\} \\ \quad + 2 6 5. 5 0 8 3 1 7 \exp \left\{2. 4 0 4 3 2 7 0 \left(\frac {z - \mu}{\sigma}\right) \right\} \text {if} \mu - 3 \sigma \leq z <   \mu \\ \sigma^ {- 1} \left(- 0. 0 1 0 5 9 2 8 + 1 9 7. 5 8 8 0 2 2 \exp \left\{- 2. 2 5 6 8 4 3 4 \left(\frac {z - \mu}{\sigma} \right. \right\} \right. \\ \quad - 4 6 2. 6 8 5 7 2 6 \exp \left\{- 2. 3 4 3 4 1 1 7 \left(\frac {z - \mu}{\sigma} \right\} \right. \\ \quad + 2 6 5. 5 0 8 3 1 7 \exp \left\{- 2. 4 0 4 3 2 7 0 \left(\frac {z - \mu}{\sigma} \right\}\right) \text {if} \mu \leq z \leq \mu + 3 \sigma \end{array} \right.\tag{5}
$$

The MTE potential with $\mu { = } 0$ and $\sigma ^ { 2 } = 1$ that approximates the normal distribution for the random demand shock (Z) in the example from Section 1.1 is shown in Fig. 3, overlaid on the actual $N ( 0 , 1 )$ distribution. Since $\int _ { \Omega _ { Z } } \Phi ( z ) d z = 1$ , the MTE potential is a pdf.

<sup>ð Þ</sup>The state spaces of continuous decision variables must be discretized in MTEIDs, in the same manner as discrete IDs.

The joint utility function is approximated by an MTE utility function. This is done by <sup>fi</sup>rst approximating the function $f _ { 1 } ( z ) = z$ over the interval [−3, 3] by the MTE potential u (z)=−84.0421+81.0772exp $\{ 0 . 0 1 1 8 9 7 8 ( z + 3 ) \}$ } for all $z \in \Omega _ { Z } .$ Note that $u _ { Z } ( - 3 ) = - 2 . 9 6 5 , u _ { Z } ( 0 ) =$ $- 0 . 0 1 9 ,$ , and $u _ { Z } ( 3 ) = 3 . 0 3 5 $ , so the MTE approximation <sup>fi</sup>ts $f _ { 1 } ( z ) = z$ reasonably well. More accurate approximations can be obtained by dividing the state space of Z and de<sup>fi</sup>ning separate approximations over each region, at the expense of increasing the representation's complexity measurement (as de<sup>fi</sup>ned in Section 4.3). With K and P assigned v and w discrete values, respectively, the MTE utility function is de<sup>fi</sup>ned as

Utility values for a discrete ID with six discrete values for P and eleven discrete values for Z, assuming $K = 5 . 8 3 .$

<table><tr><td rowspan="2"></td><td rowspan="2"> $P$ </td><td> $z_1$ </td><td> $z_2$ </td><td> $z_3$ </td><td> $z_4$ </td><td> $z_5$ </td><td></td><td> $z_{11}$ </td></tr><tr><td>-2.73</td><td>-2.18</td><td>-1.64</td><td>-1.09</td><td>-0.55</td><td>...</td><td>2.73</td></tr><tr><td> $p_1$ </td><td>1.67</td><td>-1.94</td><td>-1.94</td><td>-1.94</td><td>-1.94</td><td>-1.94</td><td>...</td><td>-1.94</td></tr><tr><td> $p_2$ </td><td>3.00</td><td>5.83</td><td>5.83</td><td>5.83</td><td>5.83</td><td>5.83</td><td>...</td><td>5.83</td></tr><tr><td> $p_3$ </td><td>4.33</td><td>10.63</td><td>12.45</td><td>13.61</td><td>13.61</td><td>13.61</td><td>...</td><td>13.61</td></tr><tr><td> $p_4$ </td><td>5.67</td><td>10.99</td><td>13.54</td><td>16.09</td><td>18.63</td><td>21.18</td><td>...</td><td>21.38</td></tr><tr><td> $p_5$ </td><td>7.00</td><td>7.80</td><td>11.08</td><td>14.35</td><td>17.62</td><td>20.89</td><td>...</td><td>29.17</td></tr><tr><td> $p_6$ </td><td>8.33</td><td>1.06</td><td>5.06</td><td>9.06</td><td>13.06</td><td>17.06</td><td>...</td><td>36.94</td></tr></table>

![](/api/attachments/VZHX4DRX/fulltext/images/0d75fb2d6c8f76748af35176d5f744f16790f58b83c2cac0885bd6c5a7533220.jpg)  
Fig. 3. The MTE potential ϕ which approximates the N(0,1) pdf for Z.

$$
u _ {1} (k _ {t}, p _ {u}, z) = \left\{ \begin{array}{l l} (p _ {u} - 1) \cdot (1 2 - p _ {u} + u _ {Z} (z)) - k _ {t} & \text {if (12 - p_{u} +z)\leq k_{t}} \\ (p _ {u} - 1) \cdot k _ {t} - k _ {t} & \text {if (12 - p_{u} +z) > k_{t}}, \end{array} \right.\tag{6}
$$

for $t = 1 , . . . , \ \nu$ and all $u = 1 , . . . , \ w .$ For instance, with $\nu = w = 6 ,$ $K = k _ { 3 } = 5 . 8 3$ , and $P { = } p _ { 3 } { = } 4 . 3 3$ , the MTE utility function is de<sup>fi</sup>ned as

$$
u _ {1} (5. 8 3, 4. 3 3, z) = \left\{ \begin{array}{l l} - 2 6 0. 4 1 8 1 3 8 + 2 8 0. 0 7 8 0 5 6 \exp \{0. 0 1 1 8 9 7 8 z \} & \text { if } - 3 \leq z <   - 1. 8 3 \\ 1 3. 6 1 & \text { if } - 1. 8 3 \leq z \leq 3. \end{array} \right.
$$

Since the class of MTE potentials is closed under addition and multiplication, the functions de<sup>fi</sup>ned in Eq. (6) are MTE potentials since $u _ { Z } ( z )$ is an MTE potential.

## 3.3. Continuous decision MTE influence diagrams (CDMTEIDs)

The CDMTEID model allows the <sup>fl</sup>exibility of modeling one of the decision variables without discretization. Because CDMTEIDs limit continuous decision variables to one continuous parent, this example will be modeled with P as a continuous decision variable, K as a discrete decision variable, and Z as a continuous chance variable. The distribution for $Z$ is again modeled by the MTE potential in Eq. (5) with $\mu = 0$ and $\sigma ^ { 2 } = 1$

The state space of K is discretized in the same manner as in the discrete ID and MTEID. Since P remains a continuous decision variable, the function $f _ { 2 } ( p ) = p \ { \mathrm { o n } }$ the interval [1,9] is modeled by the MTE potentia $u _ { P } ( p ) = - 1 0 7 . 0 5 6 1 4 4 + 1 0 8 . 1 0 2 9 6 0 \mathrm { e x p } \{ 0 . 0 0 8 9 2 3 4 ( p - 1 ) \}$ for all $p \in \Omega _ { P } .$ With K assigned v discrete values, the MTE utility function is de<sup>fi</sup>ned as

$$
u _ {1} (k _ {t}, p, z) = \left\{ \begin{array}{l l} (u _ {P} (p) - 1) \cdot (1 2 - u _ {P} (p) + u _ {Z} (z)) - k _ {t} & \text {if} (1 2 - p + z) \leq k _ {t} \\ (u _ {P} (p) - 1) \cdot k _ {t} - k _ {t} & \text {if} (1 2 - p + z) > k _ {t}, \end{array} \right.
$$

for $t = 1 , . . . ,$ v. For instance, with v=6 and $K = k _ { 3 } = 5 . 8 3$ , the MTE utility function is de<sup>fi</sup>ned as

$$
u _ {1} (5. 8 3, p, z) = \left\{ \begin{array}{l l} - 3 7 8 9. 3 2 + 1 5 3 2 8. 9 \mathrm{exp} \{0. 0 0 8 9 2 3 3 8 p \} - 1 1 4 7 9. 5 \mathrm{exp} \{0. 0 1 7 8 4 6 8 p \} \\ + 9 0 0 2. 5 \mathrm{exp} \{0. 0 0 8 9 2 3 3 8 p + 0. 0 1 1 8 9 7 8 z \} - 9 0 7 9. 3 \mathrm{exp} \{0. 0 1 1 8 9 7 8 z \} \\ \qquad \qquad \qquad \text { if } p - z \geq 6. 1 7 \\ - 6 3 6. 2 + 6 2 5. 0 \mathrm{exp} \{0. 0 0 8 9 2 3 3 8 p \} \\ \qquad \qquad \qquad \text { if } p - z <   6. 1 7. \end{array} \right.
$$

The next section describes the methods used to compare the three ID models.

## 4. Measuring accuracy and complexity

This section discusses methods for comparing the ef<sup>fi</sup>ciency of ID models with continuous decision variables.

## 4.1. Analytical solution

In the example problem from Section 1.1, the <sup>fi</sup>rm knows the true value, $Z = z ,$ of the demand shock Z when it chooses capacity, so it would logically set $K = 1 2 - P + z .$ An analytical solution to the problem [14] is found by maximizing the Lagrangian

$$
£ (p, k, \lambda) = (p - 1) \cdot (1 2 - p + z) - k + \lambda \cdot (1 2 - p + z - k),
$$

subject to the $K = 1 2 - P + z$ constraint. The optimal values of K and P are

$$
p ^ {*} = \Theta_ {1} ^ {*} (z) = 2 + \frac {1 0 + z}{2} \quad \text { and } \quad k ^ {*} = \Theta_ {2} ^ {*} (z) = \frac {1 0 + z}{2}.\tag{7}
$$

## 4.2. Accuracy

Since analytical decision rules are available for K and $P ,$ the mean squared error (MSE) [30] can be used as a measure of the difference between the analytical and ID decision rules. For instance, de<sup>fi</sup>ne $\Theta _ { 2 }$ as a decision rule for K as a function of Z determined using an ID method. The MSE of this function is calculated as

$$
M S E = E [ (\Theta_ {2} (z) - \Theta_ {2} ^ {*} (z)) ^ {2} ] = \int_ {\Omega_ {z}} \phi (z) \cdot (\Theta_ {2} (z) - \Theta_ {2} ^ {*} (z)) ^ {2} d z.\tag{8}
$$

For consistency, the pdf $\phi$ de<sup>fi</sup>ned in Eq. (5) will be used to calculate MSE values, regardless of the ID method used to determine the decision rule $\Theta _ { 2 } .$ . The MSE between the decision rule $\Theta _ { 1 }$ developed in the ID models for P as a function of K and $Z$ and the analytical decision rule ${ \boldsymbol { \Theta } } _ { 1 } ^ { * }$ is similarly calculated as

$$
M S E = E [ (\Theta_ {1} (\Theta_ {2} (z), z) - \Theta_ {1} ^ {*} (z)) ^ {2} ] = \int_ {\Omega_ {z}} \phi (z) \cdot (\Theta_ {1} (\Theta_ {2} (z), z) - \Theta_ {1} ^ {*} (z)) ^ {2} d z.\tag{9}
$$

The accuracy of a given ID model will be denoted by and will be <sup>A</sup>de<sup>fi</sup>ned as the sum of the MSEs calculated using Eqs. (8) and (9).

Most prior efforts to measure the accuracy of decision strategies when evaluating approximate ID solution methods have involved models with discrete decision variables. One experimental technique is to generate random IDs, employ an exact solution method to determine the benchmark solution, and then use multiple methods to solve these models. Accuracy is measured by comparing the percentage of the time the approximate solution method identi<sup>fi</sup>ed the correct optimal strategy [6,11,19].

When both chance and decision variables in the ID are discrete, accuracy can be measured by how close the maximum expected utility calculated by an approximate solution technique is to that determined using an exact ID solution method (for an example, see [17]). Since this paper compares ID models with continuous decision and chance variables where the chance variables are approximated with discrete pmfs or MTE density functions, the maximum expected utility calculated in the models will be affected by the decision rules identi<sup>fi</sup>ed and the approximation of the pdfs for the chance variable. The accuracy of the MTE approximation to the normal pdf is discussed in [10], so MSE has been used in this paper to focus on the accuracy of the decision rules. MSE has been used previously to compare ID solutions obtained by the three ID models discussed in this paper [7], although this previous research did not evaluate these models on the basis of complexity or apply an iterative solution algorithm.

## 4.3. Complexity

The ID models in this paper are solved using Mathematica software (www.wolfram.com) on a computer with an Intel Core 2 Duo processor (2.4 GHz) with 1.95 GB of memory. To provide a relevant comparison of the three ID models, each will be solved using a common variable elimination scheme (see Section 2.6). The run time required to solve each model will be denoted by and utilized to compare the ID models. This approach has been used frequently in the computer science and decision analysis literature to compare the computational complexity of ID models or other probabilistic graphical models (for recent examples, see [11,19,20]).

Eleven bins are chosen for the discrete approximation to the N(0,1) pdf (shown in Fig. 2), because this discrete distribution has roughly the same “size” as the MTE approximation to the normal pdf (shown in Fig. 3) used in the other ID models. In this case, size is measured using the built-in Mathematica function LeafCount that measures the number of numbers, words, and symbols required to de<sup>fi</sup>ne a piecewise function [31]. Using this measure, the LeafCount of the discrete approximation to the normal pdf is 58, whereas the MTE approximation to the normal pdf has a LeafCount of 61.

## 4.4. Normalized measurements

Since the MSE accuracy measurement, , and the complexity measurement, ${ \mathcal { C } } ,$ <sup>A</sup>determined by compiling run time to obtain the <sup>C</sup>solution are stated on different numerical scales, it is advantageous to normalize these two measurements onto a common scale to determine the trade-off between accuracy and complexity.

Select any two positive real numbers, $ { \mathcal { N } } _ { \mathrm { m i n } }$ and $\mathcal { N } _ { \mathrm { m a x } } .$ . Throughout the remainder of the paper, we assume $\mathcal { N } _ { \operatorname* { m i n } } = 1$ and ${ \mathcal { N } } _ { \operatorname* { m i n } } = 2$ <sup>N N</sup>When comparing the accuracy and complexity of ID solutions for multiple models, denote as $\underline { { A } } \ : \mathrm { a n d } \ : \underline { { c } }$ the measurements for the least ̅ ̅accurate and most complex models, respectively, measured for all models under consideration. Likewise, denote as ̅ and ̅ the <sup>A C</sup>measurements for the most accurate and least complex models, respectively. In the case of both accuracy and complexity, note that smaller measurements are desirable. The normalized accuracy measurement for a given model is determined as

$$
\hat {\mathcal {A}} = \mathcal {N} _ {\min} + \frac {(\mathcal {N} _ {\max} - \mathcal {N} _ {\min}) \cdot (\mathcal {A} - \underline {{\mathcal {A}}})}{\overline {{\mathcal {A}}} - \underline {{\mathcal {A}}}}.\tag{10}
$$

Similarly, the normalized complexity measurement for a given model is calculated as

$$
\hat {\mathcal {C}} = \mathcal {N} _ {\mathrm{min}} + \frac {(\mathcal {N} _ {\mathrm{max}} - \mathcal {N} _ {\mathrm{min}}) \cdot (\mathcal {C} - \underline {{\mathcal {C}}})}{\overline {{\mathcal {C}}} - \underline {{\mathcal {C}}}}.\tag{11}
$$

The concept of normalization has been used in the ID literature recently to compile comparable metrics when comparing accuracy along two dimensions (expected utility and optimal strategy) among ID solution techniques [19].

## 4.5. Efficiency

Once the normalized accuracy and complexity measurements are determined, the efficiency of the model is determined according to the following multi-objective utility function:

$$
\varepsilon = \hat {\mathcal {A}} ^ {\alpha} \cdot \hat {\mathcal {C}} ^ {1 - \alpha}\tag{12}
$$

The exponent α (with $\scriptstyle 0 < \alpha < 1 )$ is a parameter assigned by the decision maker that conveys an individual preference for solutions that are either more accurate or less complex. If α>0.5, the decision maker values accuracy over complexity, and vice versa. Two properties of the functional form in Eq. (12) that make the expression a useful model for consumer utility functions in economics also make it valuable for measuring the ef<sup>fi</sup>ciency of ID solutions [2]:

1. If two ID models have equivalent accuracy, the model with less complexity will have greater ef<sup>fi</sup>ciency. Conversely, if two ID models have the same complexity, the model that is more accurate is judged to be more ef<sup>fi</sup>cient.

2. The ef<sup>fi</sup>ciency function for a given ID model is convex from the origin, which means there will be a diminishing marginal rate of substitution between accuracy and complexity.

Keeney and Raiffa [16] give a more rigorous derivation of the conditions under which such utility functions are applicable.

Using this ef<sup>fi</sup>ciency function allows the decision maker to approach ID model selection as a multi-objective criteria decision problem. Similar functions have been used to represent multiple preferences in the decision analysis and operations research literature [1,18,29]. Stam and Duarte Silva [29] cite the usefulness of this function with α<1 for modeling situations where the impact of one criterion decreases as the level of this measurement increases. For instance, if a decision maker has already found an ID model with extremely high accuracy, further increasing accuracy should have a relatively small effect on ef<sup>fi</sup>ciency.

The ef<sup>fi</sup>ciency measurement is de<sup>fi</sup>ned in a general way so that other measures of complexity and accuracy can be accommodated and other comparisons of ID models and solution algorithms can be made. In this paper, we utilize a common algorithm (the fusion algorithm) to evaluate three ID methods.

## 5. Example solutions

This section illustrates the solutions to the example problem using each of the three methods. The elimination sequence employed in the fusion algorithm is P, K, Z. Each of the ID models applies discrete approximations to Ω , Ω , and $\Omega _ { Z }$ at different points in the solution techniques. The illustrations in this section assume v=6 discrete states are used in all these cases, so that $\Omega _ { P } ^ { ( d ) } = \{ 1 . 6 7 , 3 . 0 0 , 4 . 3 3 , 5 . 6 7$ 7.00, 8.33}, $\Omega _ { K } ^ { ( d ) } = \{ 1 . 1 7 , \ 3 . 5 0 , \ 5 . 8 3 , \ 8 . 1 7 , \ 1 0 . 5 0 ,$ 12.83}, and $\Omega _ { Z } ^ { ( d ) } = $ $\{ - 2 . 5 , - 1 . 5 , - 0 . 5 , 0 . 5 , 1 . 5 , 2 . 5 \}$ . An exception occurs in the discrete ID, where eleven states are used in the discrete approximation to the N(0,1) pdf, as shown in Fig. 2.

## 5.1. Discrete IDs

The solution to the discrete ID model begins by selecting the discrete value of P that maximizes $u _ { 1 }$ for each con<sup>fi</sup>guration of {K, Z}. The resulting utility function is de<sup>fi</sup>ned as

$$
u _ {2} (k _ {t}, z _ {s}) = \operatorname{Max} \left\{u _ {1} \left(k _ {t}, p _ {1}, z _ {s}\right), u _ {1} \left(k _ {t}, p _ {2}, z _ {s}\right), \dots , u _ {1} \left(k _ {t}, p _ {6}, z _ {s}\right) \right\}
$$

for al $\scriptstyle { \mathrm { 1 } t = 1 , \ldots , 6 \mathrm { a n d } s = 1 , \ldots , 1 1 }$ . Some values for $u _ { 2 }$ are shown in Table 2. For instance, for $K = k _ { 3 } = 5 . 8 3$ and $Z = z _ { 1 } = - 2 . 7 3$ , corresponding values of $u _ { 1 }$ are shown in the <sup>fi</sup>rst column of Table 1. When $K { = } 5 . 8 3$ and $Z =$ $- 2 . 7 3$ , the value of $u _ { 2 }$ is de<sup>fi</sup>ned as

Values of the utility function $u _ { 2 }$ for {K, Z} in the discrete ID solution.

<table><tr><td rowspan="2"></td><td rowspan="2"> $K$ </td><td> $z_1$ </td><td> $z_2$ </td><td> $z_3$ </td><td> $z_4$ </td><td> $z_5$ </td><td></td><td> $z_{11}$ </td></tr><tr><td>-2.73</td><td>-2.18</td><td>-1.64</td><td>-1.09</td><td>-0.55</td><td>...</td><td>2.73</td></tr><tr><td> $k_1$ </td><td>1.17</td><td>5.83</td><td>7.39</td><td>7.39</td><td>7.39</td><td>7.39</td><td>...</td><td>7.39</td></tr><tr><td> $k_2$ </td><td>3.50</td><td>12.83</td><td>13.41</td><td>16.68</td><td>17.50</td><td>19.39</td><td>...</td><td>22.17</td></tr><tr><td> $k_3$ </td><td>5.83</td><td>10.99</td><td>13.54</td><td>16.09</td><td>18.63</td><td>21.18</td><td>...</td><td>36.94</td></tr><tr><td> $k_4$ </td><td>8.17</td><td>8.66</td><td>11.21</td><td>13.75</td><td>16.30</td><td>18.84</td><td>...</td><td>38.72</td></tr><tr><td> $k_5$ </td><td>10.50</td><td>6.33</td><td>8.87</td><td>11.42</td><td>13.96</td><td>16.51</td><td>...</td><td>36.39</td></tr><tr><td> $k_6$ </td><td>12.83</td><td>3.99</td><td>6.54</td><td>9.09</td><td>11.63</td><td>14.18</td><td>...</td><td>34.06</td></tr></table>

Values of the utility function $u _ { 3 }$ for Z in the discrete ID solution.

<table><tr><td></td><td> $z_1$ </td><td> $z_2$ </td><td> $z_3$ </td><td> $z_4$ </td><td> $z_5$ </td><td> $z_6$ </td><td> $z_7$ </td><td> $z_8$ </td><td> $z_9$ </td><td> $z_{10}$ </td><td> $z_{11}$ </td></tr><tr><td> $z_s$ </td><td>-2.73</td><td>-2.18</td><td>-1.64</td><td>-1.09</td><td>-0.55</td><td>2.73</td><td>-2.73</td><td>-2.18</td><td>-1.64</td><td>-1.09</td><td>-0.55</td></tr><tr><td> $u_3(z_s)$ </td><td>12.83</td><td>13.54</td><td>16.68</td><td>18.63</td><td>21.18</td><td>24.17</td><td>27.44</td><td>29.17</td><td>33.06</td><td>36.94</td><td>38.72</td></tr></table>

$$
u _ {2} (5. 8 3, - 2. 7 3) = \operatorname{Max} \{- 1. 9 4, 5. 8 3, 1 0. 6 3, 1 0. 9 9, 7. 8 0, 1. 0 6 \} = 1 0. 9 9.
$$

Since $u _ { 1 } \ ( 5 . 8 3 , 5 . 6 7 , - 2 . 7 3 ) = 1 0 . 9 9$ (see Table 1), the resulting decision rule Θ for P dictates that if $4 . 6 7 \leq K \leq 7$ and $- 3 { \le } Z { \le } - 2 . 4 5$ $( K { = } 5 . 8 3$ and $Z = - 2 . 7 3$ are the midpoints of these intervals), then price should be set to $P { = } 5 . 6 7$ . The result of the marginalization of P is the utility function $u _ { 2 } ,$ , the probability function $\psi ,$ and the decision rule $\Theta _ { 1 }$

The next variable in the elimination sequence is K, which is marginalized by calculating

$$
u _ {3} (z _ {s}) = \mathrm{Max} \{u _ {2} (k _ {1}, z _ {s}), u _ {2} (k _ {2}, z _ {s}), \dots , u _ {2} (k _ {6}, z _ {s}) \}
$$

for s=1,…, 11. The values of u are displayed in Table 3. For instance, when $Z = z _ { 1 } = - 2 . 7 3$ , the value of $u _ { 3 }$ is de<sup>fi</sup>ned as

$$
u _ {3} (- 2. 7 3) = \operatorname{Max} \{5. 8 3, 1 2. 8 3, 1 0. 9 9, 8. 6 6, 6. 3 3, 3. 9 9 \} = 1 2. 8 3.
$$

Since u $_ 2 \left( 3 . 5 0 , - 2 . 7 3 \right) = 1 2 . 8 3$ (see Table 2), the resulting decision rule $\Theta _ { 2 }$ for K dictates that $\mathrm { i f } - 3 { \le } Z { \le } - 2 . 4 5 ( Z { = } - 2 . 7 3$ is the midpoint of this interval), then capacity should be set to $K = 3 . 5 0 .$ . The complete decision rule is shown in Fig. 4 overlaid on the analytical decision rule Θ\* from Eq. (7). The result of the marginalization of K is a utility function $u _ { 3 } , \mathsf { a }$ probability function ψ, and a decision rule $\Theta _ { 2 } .$

To remove Z from the ID, we <sup>fi</sup>rst combine ψ and $u _ { 3 } .$ The chance variable Z is then marginalized by summation.

The MSE between the analytical and ID decision rules is calculated according to Eq. (8) as 0.8057. Substituting the decision rule $\Theta _ { 2 }$ for K into the decision rule $\Theta _ { 1 }$ and measuring the MSE between the result and $\boldsymbol { \Theta } _ { 1 } ^ { * }$ according to Eq. (9) give 0.3990. Thus, the total accuracy measurement for the discrete ID is $\mathcal { A } ^ { ( 1 ) } = 1 . 2 0 4 7$ . The run time <sup>A</sup>required to obtain the solution is 1.079 s, so $\mathcal { C } ^ { ( 1 ) } = 1 . 0 7 9$

The next section details the solution to the example problem using an MTEID.

## 5.2. MTEIDs

To marginalize P from the model, we compare the utility functions $u _ { 1 } ( k _ { t } , \ p _ { 1 } , \ z ) , . . . , u _ { 1 } ( k _ { t } , \ p _ { 6 } , \ z )$ for each $t = 1 , . . . , 6 .$ For $K = k _ { 3 } = 5 . 8 3$ these functions are shown graphically in Fig. 5. To create a decision rule for P as a function of $Z ,$ we <sup>fi</sup>nd the intervals in $\Omega _ { Z }$ where the optimal discrete value of P is invariant. In this case, $P { = } 5 . 6 7$ is optimal over $[ - 3 , - 0 . 4 5 ) , P = 7$ is optimal over $[ - 0 . 4 5 , 1 . 1 5 )$ , and $P { = } 8 . 3 3$ is optimal over $\left[ 1 . 1 5 , 3 \right]$ . These values are used to create the decision rule

![](/api/attachments/VZHX4DRX/fulltext/images/a7c5c9416990e8f295ae88ecde123bce38a79db99fb4d02f889fd445614d7d96.jpg)  
Fig. 4. The decision rule $\Theta _ { 2 }$ from the discrete ID overlaid on the analytical decision rule Θ\*.

$$
P (z) = \Theta_ {1, 3} (z) = \left\{ \begin{array}{l l} 5. 8 3 & \text { if } - 3 \leq z <   - 0. 4 5 \\ 7 & \text { if } - 0. 4 5 \leq z <   1. 1 5 \\ 8. 3 3 & \text { if } 1. 1 5 \leq z \leq 3, \end{array} \right.
$$

for $4 . 6 7 \leq k < 7 .$ The set of all such decision rules, $\Theta _ { 1 , 1 } , . . . , \Theta _ { 1 , 6 } ,$ for intervals with midpoints $k _ { t } , \ t = 1 , . . . , \ 6$ is combined to form the decision rule $\Theta _ { 1 }$ for P as a function of {K, Z}. After this step in the removal of $P ,$ the remaining set of functions is $\{ \phi , u _ { 1 } , \theta _ { 1 } \}$

The second step required to marginalize P is substitution of the optimal values for P into the utility function u<sub>1</sub> to create the utility function $u _ { 2 } ( k _ { t } , z ) = u _ { 1 } ( k _ { t } , \theta _ { 1 } ( z ) , z )$

The decision variable K is removed in the same manner as P. The utility functions $u _ { 2 } ( k _ { 1 } , z ) , . . . , u _ { 2 } ( k _ { 6 } , z )$ are shown graphically in Fig. 6. From the graph, it is apparent that $u _ { 2 } ( 3 . 5 , z ) \approx u _ { 2 } ( 5 . 8 3 , z )$ at $Z =$ $- 1 . 3 5$ and $u _ { 2 } ( 5 . 8 3 , z ) \approx u _ { 2 } ( 8 . 1 7 , z )$ at $Z = 2 . 4 5$ . These points are used to determine the decision rule

$$
K (z) = \Theta_ {2} (z) = \left\{ \begin{array}{l l} 3. 5 & \text { if } - 3 \leq z <   - 1. 3 5 \\ 5. 8 3 & \text { if } - 1. 3 5 \leq z <   2. 4 5 \\ 8. 1 7 & \text { if } 2. 4 5 \leq z \leq 3. \end{array} \right.
$$

The complete the marginalization of $K ,$ we create the utility function $u _ { 3 } ( z ) = u _ { 2 } ( \theta _ { 2 } ( z ) , z )$ . To marginalize Z, the potentials ϕ and $u _ { 3 }$ are <sup>fi</sup>rst combined as $\phi \otimes u _ { 3 } .$ The chance variable Z is then marginalized by integration.

The MSE of the MTEID solution is calculated according to Eqs. (8) and (9) as $\mathcal { A } ^ { ( 2 ) } = 1 . 2 1 1 9$ . The run time required to obtain the solution is 0.437 s, so $\mathcal { C } ^ { ( 2 ) } = 0 . 4 3 7$

## 5.3. CDMTEIDs

In the CDMTEID model, P is a continuous decision variable; however, the <sup>fi</sup>rst step in marginalizing this variable is accomplished by temporarily using the discrete approximation $\Omega _ { P } ^ { ( d ) }$ . The values $P _ { u } ,$ $u = 1 , \ldots ,$ , 6 are inserted in the utility potential $u _ { 1 }$ to form the utility functions $u _ { 1 } ( k _ { t } , p 1 , z ) _ { \cdots } , u _ { 1 } ( k _ { t } , p _ { 6 } , z )$ for $t = 1 , . . . , 6 $

![](/api/attachments/VZHX4DRX/fulltext/images/dab643a8238b94d531128d2a8d2a13e1c0c7ec6c39c859253fdd3f6ee8c7bec1.jpg)  
Fig. 5. The utility functions $u _ { 1 } ( k _ { 3 } , p _ { u } , z )$ for $u = 1 , \ldots$ 6 in the MTEID solution

![](/api/attachments/VZHX4DRX/fulltext/images/9c17155349670bab0f01722185d7e4db449257a458a136364cb396fe416b98d7.jpg)  
Fig. 6. The utility functions $u _ { 2 } ( k _ { t } , z )$ for $t = 1 , \ldots$ 6 in the MTEID solution

The second step in removing P is to create a piecewise linear decision rule for P as a function of Z. This is done separately for each value $k _ { t } , t = 1 , . . . , 6 .$ The procedure begins in a similar way to the marginalization procedure in the MTEID solution. For $K = k _ { 3 } = 5 . 8 3$ the utility functions $u _ { 1 } ( k _ { 3 } , p _ { u } , z )$ for $u = 1 , . . . , 6$ are similar to those in Fig. 5 and we can again conclude that $P { = } 5 . 6 7$ is optimal over $[ - 3 ,$ $- 0 . 4 5 ) , P = 7$ is optimal over $[ - 0 . 4 5 , 1 . 1 5 )$ , and $P { = } 8 . 3 3$ is optimal over [1.15, 3]. These values are used to create the piecewise linear decision rule

$$
P (z) = \Theta_ {1, 3} (z) = \left\{ \begin{array}{l l} 6. 7 7 5 1 0 0 + 0. 6 4 2 5 7 0 z & \text { if } - 3 \leq z <   - 0. 3 5 \\ 6. 7 3 0 1 4 5 + 0. 7 7 1 0 1 4 z & \text { if } 0. 3 5 \leq z <   2. 9 3 7 5 \\ 9 & \text { if } 2. 9 3 7 5 \leq z \leq 3. \end{array} \right.
$$

The values for the optimal prices and the endpoints of the intervals are used to calculate the slope and intercept values of each piece of this function. For example, the slope for the second piece is calculated as $( 8 . 3 3 - 7 ) / ( ( 1 . 1 5 + 3 ) / 2 - ( - 0 . 4 5 + 1 . 1 5 ) / 2 ) = 0 . 7 7 1 0 1 4$ , with the intercept determined as $8 . 3 3 - 0 . 7 7 1 0 1 4 \cdot ( 1 . 1 5 + 3 ) / 2 = 6 . 7 3 0 1 4 5 .$ . In some cases, such as the third piece of the function above, the endpoints of the state space are optimal beyond certain values of the observed chance variable.

Similar decision rules $\Theta _ { 1 , 1 } , . . . , \Theta _ { 1 , 6 }$ are determined corresponding to values $k _ { t } , t = 1 , . . . , 6 ,$ of the discrete decision variable K (see Fig. 7). When combined. these functions form the decision rule $\Theta _ { 1 }$

The last step in removing P from the model is to substitute the values of the decision rule Θ into the utility function $u _ { 1 }$ to form the utility functions, $u _ { 2 } ( k _ { t } , z ) = u _ { 1 } ( k _ { t } , \theta _ { 1 , t } ( z ) , z )$ , for $t = 1 , . . . , 6 . \ : \mathsf { A }$ plot of the functions $u _ { 2 } ( k _ { 1 } , z ) , . . . , u _ { 2 } ( k _ { 6 } , z )$ is shown in Fig. 8 and shows that $u _ { 2 } ( 3 . 5 , z ) \approx u _ { 2 } ( 5 . 8 3 , z )$ at $Z = - 1 . 2 5 .$ . The resulting decision rule $\Theta _ { 2 }$ speci<sup>fi</sup>es that $K = 3 . 5 \ \mathrm { i f } - 3 \leq z < - 1 . 2 5$ and $K = 5 . 8 3 { \mathrm { ~ i f } } - 1 . 2 5 \leq z \leq 3 .$

To complete the marginalization of $K ,$ we create a new utility function $u _ { 3 } ( z ) = u _ { 2 } ( \theta _ { 2 } ( z ) , z )$ . To remove Z, the potentials ϕ and $u _ { 3 }$ are combined. Integrating the result over the state space of Z completes the solution. The MSE of the CDMTEID solution is calculated according to Eqs. (8) and (9) as $\mathcal { A } ^ { ( 3 ) } = 0 . 7 7 5 2$ . The solution required a run time of 1.282 s, so $\mathcal { C } ^ { ( 3 ) } = 1 . 2 8 2$

![](/api/attachments/VZHX4DRX/fulltext/images/05857c7b6ac4173c7055557260e576496faf8d28dc88dae64fc79ae65cc6c156.jpg)  
Fig. 7. The piecewise linear decision rules $\theta _ { 1 , t }$ corresponding to values $k _ { t } , t = 1 , . . . ,$ 6 of the discrete decision variable K in the CDMTEID solution

![](/api/attachments/VZHX4DRX/fulltext/images/cf9f19544bf316d6bc609f1bb191ce6de218d68ac7d465b48d924e9e1828f39f.jpg)  
Fig. 8. The utility functions $u _ { 2 } ( k _ { t } , z )$ for $t = 1 , . . . ,$ 6 in the CDMTEID solution.

The next section compares the ID solutions for the three models.

## 6. Results

This section discusses the effects on model ef<sup>fi</sup>ciency of changing the number of states in the discrete approximations to continuous decision variables, as well as the ef<sup>fi</sup>ciency of applying the iterative solution algorithm in each of the ID models.

In each of the three ID methods illustrated, the state space of continuous variables is either permanently or temporarily discretized, and the number of discrete states used affects both the accuracy and complexity of the solution. To investigate the ef<sup>fi</sup>ciency of models with a varying number of pieces in the discrete approximation, we consider the three ID models with approximations of six through twelve states with one or two iterations of the algorithm from Section 2.7. Thus, the best and worst solutions in terms of accuracy and complexity are chosen from among 42 models when calculating the values of $\underline { { A } } , \overline { { A } } , \mathcal { L } ,$ and . ̅ <sup>A A</sup> ̅<sup>C C</sup>When a second iteration is used, the complexity measurement bears the computational burden of both iterations. Table 4 shows the unnormalized accuracy and complexity measurements for these 42 models, as well as the normalized measurements calculated according to Eqs. (10) and (11). The best and worst measurements in each category are shown in bold.

Figs. 9 and 10 show ef<sup>fi</sup>ciency scores for accuracy parameters of $\alpha { = } 0 . 1$ and $\alpha { = } 0 . 9 ,$ , respectively, after one iteration of the solution algorithm for each of the three methods. These are calculated according to Eq. (12). When accuracy is a low priority $( \alpha { = } 0 . 1 )$ ), the ef<sup>fi</sup>ciency of the models (see Fig. 9) eventually decreases with additional discrete pieces in the approximations as computational complexity overburdens the solution, though only slightly in the MTEID and CDMTEID models. In this case, the MTEID model provides slightly better ef<sup>fi</sup>ciency than the CDMTEID model. When the discrete ID and MTEID solutions employ discrete approximations to the pdf for Z that are about the same “size” (see Section 4.3), the resulting solutions have similar accuracy, but the MTEID model requires less run time. The accuracy of the MTEID model is limited by the number of states used for the decision variables.

When accuracy is a high priority $( \alpha { = } 0 . 9 )$ , the ef<sup>fi</sup>ciency of the models generally increases with additional pieces in the discrete approximations and the CDMTEID provides the best ef<sup>fi</sup>ciency (see Fig. 10). In some cases, the placement of the midpoints of the discrete bins within the state space of the decision variable adversely affects accuracy, which is why the ef<sup>fi</sup>ciency of the solutions with an eightpiece approximation is lower than with a seven-piece approximation.

Fig. 11 displays the ef<sup>fi</sup>ciency scores for the ID solutions over the entire range of possible accuracy values. To make the graph simpler to comprehend, only the ef<sup>fi</sup>ciency scores for models that gave the optimal ef<sup>fi</sup>ciency over some range of the accuracy parameter α are shown. The un-normalized accuracy (MSE) and complexity values for these models are also displayed on the chart. For very low values of α, the MTEID models with six or seven discrete states evaluated with one iteration of the solution algorithm are optimal. However, as the decision maker's desire for accuracy increases, MTEID models with increasing numbers of discrete states for decision variables that employ two iterations of the solution algorithm become optimal. Above α≈0.72, CDMTEID models that utilize two iterations of the solution algorithm and a large number of discrete states for decision variables are the best choice.

Un-normalized and normalized accuracy and complexity measurements for the three ID models.

<table><tr><td colspan="7">Un-normalized measurements</td></tr><tr><td></td><td colspan="3">Iteration 1</td><td colspan="3">Iteration 2</td></tr><tr><td>Disc. states</td><td>Discrete</td><td>MTEID</td><td>CDMTEID</td><td>Discrete</td><td>MTEID</td><td>CDMTEID</td></tr><tr><td colspan="7">Accuracy (A)</td></tr><tr><td>6</td><td>1.2047</td><td>1.2119</td><td>0.7752</td><td>0.1712</td><td>0.2598</td><td>0.0688</td></tr><tr><td>7</td><td>0.5090</td><td>0.7506</td><td>0.3822</td><td>0.0775</td><td>0.1980</td><td>0.0762</td></tr><tr><td>8</td><td>0.7998</td><td>1.0094</td><td>0.4986</td><td>0.0466</td><td>0.1307</td><td>0.0450</td></tr><tr><td>9</td><td>0.4461</td><td>0.5200</td><td>0.3225</td><td>0.1041</td><td>0.0828</td><td>0.0431</td></tr><tr><td>10</td><td>0.2985</td><td>0.3430</td><td>0.2518</td><td>0.0256</td><td>0.0840</td><td>0.0324</td></tr><tr><td>11</td><td>0.3411</td><td>0.3611</td><td>0.2546</td><td>0.1574</td><td>0.1099</td><td>0.0323</td></tr><tr><td>12</td><td>0.2883</td><td>0.4288</td><td>0.2008</td><td>0.0612</td><td>0.0433</td><td>0.0245</td></tr><tr><td colspan="7">Complexity (C)</td></tr><tr><td>6</td><td>1.079</td><td>0.437</td><td>1.282</td><td>2.531</td><td>0.891</td><td>2.406</td></tr><tr><td>7</td><td>1.609</td><td>0.547</td><td>1.750</td><td>3.406</td><td>1.063</td><td>3.203</td></tr><tr><td>8</td><td>2.235</td><td>0.672</td><td>1.532</td><td>4.828</td><td>1.390</td><td>3.031</td></tr><tr><td>9</td><td>3.110</td><td>0.891</td><td>2.156</td><td>6.797</td><td>1.828</td><td>4.125</td></tr><tr><td>10</td><td>4.125</td><td>1.079</td><td>2.313</td><td>9.110</td><td>2.187</td><td>4.563</td></tr><tr><td>11</td><td>5.578</td><td>1.281</td><td>2.843</td><td>12.047</td><td>2.657</td><td>5.500</td></tr><tr><td>12</td><td>7.281</td><td>1.485</td><td>2.750</td><td>15.156</td><td>3.125</td><td>5.438</td></tr><tr><td colspan="7">Normalized measurements</td></tr><tr><td colspan="7">Accuracy (Â)</td></tr><tr><td>6</td><td>1.000</td><td>1.000</td><td>1.368</td><td>1.876</td><td>1.802</td><td>1.963</td></tr><tr><td>7</td><td>1.592</td><td>1.388</td><td>1.699</td><td>1.955</td><td>1.854</td><td>1.956</td></tr><tr><td>8</td><td>1.347</td><td>1.171</td><td>1.601</td><td>1.981</td><td>1.911</td><td>1.983</td></tr><tr><td>9</td><td>1.645</td><td>1.583</td><td>1.749</td><td>1.933</td><td>1.951</td><td>1.984</td></tr><tr><td>10</td><td>1.769</td><td>1.732</td><td>1.809</td><td>1.999</td><td>1.950</td><td>1.993</td></tr><tr><td>11</td><td>1.733</td><td>1.717</td><td>1.806</td><td>1.888</td><td>1.928</td><td>1.993</td></tr><tr><td>12</td><td>1.778</td><td>1.660</td><td>1.852</td><td>1.969</td><td>1.984</td><td>2.000</td></tr><tr><td colspan="7">Complexity (Ç)</td></tr><tr><td>6</td><td>1.956</td><td>2.000</td><td>1.943</td><td>1.858</td><td>1.969</td><td>1.866</td></tr><tr><td>7</td><td>1.920</td><td>1.993</td><td>1.911</td><td>1.798</td><td>1.957</td><td>1.812</td></tr><tr><td>8</td><td>1.878</td><td>1.984</td><td>1.926</td><td>1.702</td><td>1.935</td><td>1.824</td></tr><tr><td>9</td><td>1.818</td><td>1.969</td><td>1.883</td><td>1.568</td><td>1.905</td><td>1.749</td></tr><tr><td>10</td><td>1.749</td><td>1.956</td><td>1.873</td><td>1.411</td><td>1.881</td><td>1.720</td></tr><tr><td>11</td><td>1.651</td><td>1.943</td><td>1.837</td><td>1.211</td><td>1.849</td><td>1.656</td></tr><tr><td>12</td><td>1.535</td><td>1.929</td><td>1.843</td><td>1.000</td><td>1.817</td><td>1.610</td></tr></table>

The best and worst measurements in each category are shown in bold.

![](/api/attachments/VZHX4DRX/fulltext/images/f588c58e6fb9501b5e08456118364c53a6bcc75e9fe30c60c64a967056e4fb35.jpg)  
Fig. 9. Ef<sup>fi</sup>ciency scores for an accuracy parameter value of α=0.1.

![](/api/attachments/VZHX4DRX/fulltext/images/d5859f226344b1f9630520261a44d2dc6f19cc9daab6293164bda4d5642cf11a.jpg)  
Fig. 10. Ef<sup>fi</sup>ciency scores for an accuracy parameter value of α=0.9.

## 7. Conclusions

In an effort to determine the ID model for problems with continuous decision variables that is best for an individual decision maker, this paper has de<sup>fi</sup>ned a measure of ef<sup>fi</sup>ciency for ID models with continuous decision variables. The metric considers both the accuracy and complexity of the representation and solution. Accuracy is measured by calculating the mean squared error between the <sup>fi</sup>nal decision rule determined using the ID and a corresponding analytical decision rule. An extremely <sup>fi</sup>ne discrete approximation can also be used in placed of an analytical solution (an example is described in [7]). Complexity is determined by the run time required to obtain the solution. The ef<sup>fi</sup>ciency measurement combining accuracy and complexity is able to consider the preferences of an individual decision maker for both accuracy and complexity.

The ef<sup>fi</sup>ciency measurement is used to compare discrete in<sup>fl</sup>uence diagrams, MTE in<sup>fl</sup>uence diagrams [9], and continuous decision MTE in<sup>fl</sup>uence diagrams [7]. The assessment is made using a capacity and pricing decision with a known analytical solution [14]. The discrete in<sup>fl</sup>uence diagram contains an approximation to the probability function of the continuous chance variable that is approximately the same size as the MTE approximation used in the other models.

In each of these models, the accuracy and complexity vary with the number of pieces used in discrete approximations to decision variables at different stages in the solution techniques. Additionally, an iterative algorithm is used to improve accuracy in each model, albeit at a greater computational cost. Depending on the decision maker's preference for accuracy versus complexity, the MTEID or CDMTEID models may each be preferable, and in some cases employing the iterative algorithm is desirable.

![](/api/attachments/VZHX4DRX/fulltext/images/5ee00d6e9cca666ccc2869c1ed64ddd21a49c4eedd6c58ad41cc05b72aa2522f.jpg)  
Fig. 11. Ef<sup>fi</sup>ciency values for ID solutions at values of between zero and one

The measurements proposed in this paper can be useful when designing decision support systems used to address ongoing process selection problems. Although the methodology requires the use of a problem with an analytical solution, a manager can develop ef<sup>fi</sup>ciency measurements for the test problem to determine the type of model required to meet the organization's standard for accuracy–complexity trade-off. The appropriate model can then be implemented in the system to solve a related, more complex problem. This can be done in the design phase of the decision support system to ensure that the effort, time, and expense committed are appropriate for the organization. For example, a manager needing to build a decision support system to address a multi-period, multi-product pricing and capacity system could use the results presented in this paper for the related single-period, single-product problem and determines the type of model that provides the desired accuracy with the appropriate complexity.

Future research may be able to address the issues that create additional complexity in the models addressed in this paper. For instance, a scheme that eliminates terms in MTE potentials that add a negligible density or utility value could be developed. Additionally, an algorithm that takes advantage of an additive factorization of the joint utility function may lead to decreased complexity. It may also be possible to use the iterative algorithm with different models in the <sup>fi</sup>rst and second stages, utilizing a less complex model to narrow the state spaces of continuous decision variables and a more accurate model to determine the <sup>fi</sup>nal decision rule.

## References

[1] J. Barzilai, W.D. Cook, B. Golani, Consistent weights for judgment matrices of the relative importance of alternatives, Operations Research Letters 6 (1987) 131–141.

[2] M.R. Baye, Managerial Economics and Business Strategy, McGraw-Hill/Irwin, New York, NY, 2006.

[3] C. Bielza, J.A. Fernández del Pozo, Explaining clinical decisions by extracting regularity patterns, Decision Support Systems 44 (2) (2008) 397–408.

[4] C. Bielza, M. Gómez, P.P. Shenoy, Modeling challenges with in<sup>fl</sup>uence diagrams: representation issues, Working Paper, University of Kansas, School of Business, Lawrence, KS, 2009.

[5] J. Brynielsson, Using AI and games for decision support in command and control, Decision Support Systems 43 (4) (2007) 1454–1463.

[6] A. Cano, M. Gómez, S. Moral, A forward–backward Monte Carlo method for solvin in<sup>fl</sup>uence diagrams, International Journal of Approximate Reasoning 42 (2006) 119–135.

[7] B.R. Cobb, In<sup>fl</sup>uence diagrams with continuous decision variables and non-Gaussian uncertainties, Decision Analysis 4 (3) (2007) 136–155.

[8] B.R. Cobb, P.P. Shenoy, Inference in hybrid Bayesian networks using mixtures of truncated exponentials, International Journal of Approximate Reasoning 41 (3) (2006) 257–286

[9] B.R. Cobb, P.P. Shenoy, Decision making with hybrid in<sup>fl</sup>uence diagrams using mixtures of truncated exponentials, European Journal of Operational Research 186 (1) (2008) 261-275.

[10] B.R. Cobb, P.P. Shenoy, R. Rumí, Approximating probability density functions in hybrid Bayesian networks with mixtures of truncated exponentials, Statistics and Computing 16 (3) (2006) 293–308.

[11] C.P. de Campos, Q. Ji, in: D.A. McAllester, P. Myllymäki (Eds.), Strategy Selection in In<sup>fl</sup>uence Diagrams using Imprecise Probabilities, Uncertainty in Arti<sup>fi</sup>cial Intelligence, vol. 24, AUAI Press, Corvallis, OR, 2008, pp. 121–128.

[12] H.W. Gottinger, H.P. Weimann, Intelligent decision support systems, Decision Support Systems 8 (4) (1992) 317–322.

[13] H.W. Gottinger, H.P. Weimann, Intelligent inference systems based on in<sup>fl</sup>uence diagrams, Decision Support Systems 15 (1) (1995) 27–43.

[14] R.F. Göx, Capacity planning and pricing under uncertainty, Journal of Management Accounting Research 14 (1) (2002) 59–78.

[15] R.A. Howard, J.F. Matheson, in: R.A. Howard, J.E. Matheson (Eds.), In<sup>fl</sup>uence Diagrams, Readings on the Principles and Applications of Decision Analysis, vol. 2, Strategic Decisions Group, Menlo Park, CA, 1984, pp. 719–762, [Reprinted in Decision Analysis 2(3) (2005) 127–143].

[16] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, John Wiley and Sons, New York, NY, 1976.

[17] S.L. Lauritzen, D. Nilsson, Representing and solving decision problems with limited information, Management Science 47 (9) (2001) 1238–1251.

[18] F.A. Lootsma, Scale sensitivity in the multiplicative AHP and SMART, Journal of Multi-Criteria Decision Analysis 2 (1993) 87–110.

[19] M. Luque, T.D. Nielsen, F.V. Jensen, An anytime algorithm for solving unconstrained in<sup>fl</sup>uence diagrams, in: M. Jaeger, T.D. Nielsen (Eds.), Proceedings of the Fourth European Workshop on Probabilistic Graphical Models (PGM-08), Hirtshals, Denmark, 2008, pp. 177–184.

[20] A.L. Madsen, Solving CLQG in<sup>fl</sup>uence diagrams using arc-reversal operations in a strong junction tree, in: M. Jaeger, T.D. Nielsen (Eds.), Proceedings of the Fourth European Workshop on Probabilistic Graphical Models (PGM-08), Hirtshals Denmark, 2008, pp. 101–108.

[21] A.L. Madsen, F. Jensen, Solving linear–quadratic conditional Gaussian in<sup>fl</sup>uence diagrams, International Journal of Approximate Reasoning 38 (3) (2005) 263–282.

[22] S. Moral, R. Rumí, A. Salmerón, Mixtures of truncated exponentials in hybrid Bayesian networks, in: P. Besnard, S. Benferhart (Eds.), Symbolic and Quantitative Approaches to Reasoning under Uncertainty, Lecture Notes in Arti<sup>fi</sup>cial Intelli gence, vol. 2143, Springer-Verlag, Heidelberg, 2001, pp. 156–167.

[23] S.M. Olmsted, On representing and solving decision problems, doctoral thesis (Stanford University, Department of Engineering–Economic Systems, Stanford, CA, 1983).

[24] W.B. Poland, Decision analysis with continuous and discrete variables: a mixture distribution approach, doctoral thesis (Department of Engineering–Economic Systems, Stanford University, Stanford, CA, 1994).

[25] W.B. Poland, R.D. Shachter, Mixtures of Gaussians and minimum relative entropy techniques for modeling continuous uncertainties, in: D. Heckerman, E.H. Mamdani (Eds.), Uncertainty in Arti<sup>fi</sup>cial Intelligence, vol. 9, Morgan Kaufmann, San Francisco, CA, 1993, pp. 183–190.

[26] R.D. Shachter, Evaluating in<sup>fl</sup>uence diagrams, Operations Research 34 (6) (1986) 871–882.

[27] R.D. Shachter, C.R. Kenley, Gaussian in<sup>fl</sup>uence diagrams, Management Science 35 (5) (1989) 527-550

[28] P.P. Shenoy, A new method for representing and solving Bayesian decision problems, in: D.J. Hand (Ed.), Arti<sup>fi</sup>cial Intelligence Frontiers in Statistics: AI and Statistics III, Chapman and Hall, London, 1993, pp. 119–138.

[29] A. Stam, P. Duarte Silva, On multiplicative priority rating methods for the AHP, European Journal of Operational Research 145 (2003) 92–108.

[30] R.L. Winkler, W.L. Hays, Statistics: Probability, Inference, and Decisions, Holt, Rinehart, and Winston, New York, NY, 1970.

[31] S. Wolfram, The Mathematica Book, 5th editionWolfram Media, Champaign, IL, 2003.

Barry R. Cobb is currently an Associate Professor of Economics and Business at Virginia Military Institute. He received his Ph.D. in business administration with an emphasis in decision sciences from the University of Kansas. His areas of research interest are decision theory, probabilistic graphical models, and simulation. His areas of teaching interest are operations management, management science, and managerial economics. His research has appeared in such journals as Decision Analysis, European Journal of Operational Research, and Statistics and Computing.
