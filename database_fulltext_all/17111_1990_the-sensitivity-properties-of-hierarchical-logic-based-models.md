---
otero_id: 17111
otero_key: "T8HNVVZZ"
title: "The sensitivity properties of hierarchical logic-based models"
authors: "Robert W Blanning"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90002-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Sensitivity Properties of Hierarchical Logic-Based Models $^{1}$

Robert W. BLANNING

Vanderbilt University, Nashville, TN 37203, USA

Much of the work on logic modeling focuses on constructing logic-based models that represent real-world situations, investigating the properties of different types of models and logics, and developing solution procedures for the models so as to address real-world problems. An important subset of the latter task is to perform sensitivity analyses that determine how the output of such a model will change in response to a change in its inputs. In two previous papers we developed methods for calculating sensitivity measures for Boolean models using the concept of a Boolean derivative, initially developed for circuit design. In this paper we review these methods and present a method for calculating sensitivity measures, in the form of first derivatives, for models based on fuzzy logic. Since these models are piecewise linear, it is necessary to consider derivatives from both the right and the left.

Keywords: Fuzzy Logic; Sensitivity Analysis; Tree structure; Piecewise Linearity; Left Derivative; Right Derivative; Nonstandard Logics.

## 1. Introduction

Several surveys (e.g., [7]) and case studies (e.g., those found in [4]) describing the use of decision models by managers and staff analysts have disclosed that an important purpose of these models is to help their users to answer 'what if' questions by performing sensitivity analyses. These analyses may be used to determine whether a deliberate change in a decision under consideration or a possible environmental change will be beneficial or harmful. In addition, they may also assist in the economic evaluation of proposed information acquisition efforts, for if the value of a particular parameter will have little or no impact on the outcomes of interest, then it may not be worth the effort to improve the estimate of the value of that parameter.

This is true not only of decision models but also of the knowledge-based models increasingly

![](/api/attachments/T8HNVVZZ/fulltext/images/cec05a781214ab4a0c0a8c22ea39d17b02a67f8e2ffcfbc30ce1ead3fff1249f.jpg)

Fig. 1. A logic tree.

being used for management decision making [5,8,9]. However, little attention has been paid to the development of formal techniques for performing sensitivity analyses with models of this type (as opposed to incrementing an input, running the model, and observing the resulting change in output). Rather, the literature has emphasized the use of explanation facilities that reveal the inference paths used by the model.

One exception is found in two papers [2,3] that assumed a simple structure found in rule-based expert systems - a tree whose nodes represent Boolean variables combined by means of AND, OR, IF-THEN, etc. operation. By applying the concept of a Boolean derivative, which was initially developed from electronic circuit design and fault analysis [10], the papers presented simple methods of determining the sensitivity of the Boolean variable at the root of the tree (i.e., the output of the model) with respect to the input variables at the leaves of the three.

A shortcoming of this approach lies in the simplicity of the underlying model – the Boolean tree. Many rule-based systems make use of non-standard logics that substitute for a true/false dichotomy a range of degrees of truth, belief, or perceived certainty in rules and variables [5,11]. An example is fuzzy logic, in which the truth of an assertion is represented by a real number between 0 and 1 (inclusive), and logical operations (e.g., AND, OR, NOT, etc.) are performed in ways specified below. In this paper we develop procedures for performing sensitivity analyses in fuzzy logic trees.

## 2. A Logic Tree

We begin by presenting an example of a logic tree – that is, a tree in which each non-leaf node is a logical combination of the nodes beneath it. In other words, each node (including the leaves) will correspond to a variable in a logic model, and each non-leaf node will be defined by an AND, OR, IF–THEN, and NOT operation performed on the nodes beneath it. The leaf variables will be the input to the logic model, and the root variable will be the output. In this section we will not be concerned with whether the variables are “crisp” Boolean variables that can only take on the values 0 and 1 (denoting FALSE and TRUE), or whether

![](/api/attachments/T8HNVVZZ/fulltext/images/b6ae4aab45bf13459afaa16fda1a6f2d5c0f41b18b2caa946baefe8252dcf772.jpg)

A - project will be funded

B - cost is high

C - performance is good

D - tangible costs are high

E - intangible costs are high

F - system is durable

G - system is efficient

they are fuzzy variables that can take on any value in the closed unit interval (i.e., the interval [0, 1]), denoting the degree of truth associated with the variable. We will use this tree and its associated model in the following sections to review previous work on sensitivity analysis with Boolean models and to present a method for extending this work to fuzzy logic models.

The model is illustrated in fig. 1. The output is the statement, 'The project will be funded'. We note again that this will be a crisp variable in some of the sections to follow and a fuzzy variable in others. The project will be funded if whenever the cost is high, the performance is good. (The arrow denotes the IF-THEN relationship.) The cost will be high if both tangible and intangible costs are high. (The arc denotes the AND operation.) Performance will be good if the system is durable or efficient or both. (The absence of an arrow or an arc denotes an OR operation.) The NOT operation, which is absent in this model, will be denoted by a single node beneath another node.

In this model A takes on the value of $B \rightarrow C$ , B takes on the value $D \wedge E$ , and C takes on the value $F \vee G$ . Thus we can write:

$$
\begin{array}{l} A = B \to C, \\ B = D \wedge E, \\ C = F \vee G. \end{array}
$$

In the following sections we will assign values to the leaf variables $(D, E, F, \text{and } G)$ and calculate the values of the intermediate variables $(B \text{ and } C)$ and the root variable $(A)$ . In sections 3 and 4 the variables will be Boolean variables, and we will review methods for determining whether changes in the leaves will induced a change in the root. In section 3 we will be concerned with simple sensitivity analysis, in which a single leaf variable changes, all other being held constant, and we wish to know whether the root will change. Then in section 4 and the following sections we consider the case in which the variables are fuzzy and sensitivity is defined by incremental responses in the root to incremental changes in the leaves.

## 3. Boolean Sensitivity Analysis

In [3] it was shown that a simple Boolean sensitivity analysis could be performed by using the concept of a Boolean derivative, which was originally developed for circuit design [1,10]. If X and Y are Boolean variables and $Y = Y(X)$ , the Boolean derivative of Y with respect to X is itself a Boolean variable and is defined as follows:

Definition 1. Given a Boolean function $Y()$ of a Boolean variable $X$ ,

$$
\frac {\mathrm{d} Y}{\mathrm{d} X} = Y (X) \oplus Y (\overline {{{X}}}).
$$

The symbol $\oplus$ denotes an EXCLUSIVE OR operation, which produces a TRUE result whenever one of its arguments is TRUE and the other FALSE. Using 1 to denote TRUE and 0 to denote FALSE, we have $1 \oplus 0 = 0 \oplus 1 = 1$ and $1 \oplus 1 = 0 \oplus 0 = 0$ . Thus, $\mathrm{d}Y / \mathrm{d}X$ takes on the value 1 whenever a change in $X$ (from 0 to 1 or 1 to 0) causes $Y$ to change its value; $\mathrm{d}Y / \mathrm{d}X$ is 0 if a change in $X$ causes no change in $Y$ . The truth value of $\mathrm{d}Y / \mathrm{d}X$ is the same as that of the statement, 'A change in $X$ will bring about a change in $Y$ '

We note several properties of the Boolean derivative. First, since the value of dY/dX is independent of X (i.e., the sensitivity of Y to X is independent of whether X is changing from (0 to 1 or 1 to 0), all higher derivatives are 0. This is proven in

Result 1. Given a Boolean function $Y()$ of a Boolean variable $X$ , we have:

$$
\frac {\mathrm{d} ^ {n} Y}{\mathrm{d} X ^ {n}} = 0 \quad \text { for   all } n \geq 2.
$$

Proof. We note that $\mathrm{d}Y / \mathrm{d}X$ is independent of the value of $X$ , since if $X = 1$ , then

$$
\frac {\mathrm{d} Y}{\mathrm{d} X} = Y (1) \oplus Y (0),
$$

and if $X = 0$ , then

$$
\frac {\mathrm{d} Y}{\mathrm{d} X} = Y (0) \oplus Y (1).
$$

Since the EXCLUSIVE OR operation is commutative, both of these values are the same. Therefore, dY/dX is insensitive to X - that is, either dY/dX = 0 or dY/dX = 1, independent of X. Since dY/dX is a constant, $d^{2}Y/dX^{2} = 0$ , which is also constant. Therefore, by induction we have $d^{n}Y/dX^{n} = 0$ for all $n \geq 2$ .

In addition, there is a chain rule, as follows:

Result 2. Given a Boolean function $Y()$ of a Boolean variable $X$ and a Boolean function $Z()$ of $Y$ , we have:

$$
\frac {\mathrm{d} Z}{\mathrm{d} X} = \frac {\mathrm{d} Z}{\mathrm{d} Y} \wedge \frac {\mathrm{d} Y}{\mathrm{d} X}.
$$

Proof. Consider three cases:

Case 1: $\mathrm{d}Z / \mathrm{d}Y = \mathrm{d}Y / \mathrm{d}X = 1$ . In this case a change in $X$ will induce a change in $Y$ , and the change in $Y$ will induce a change in $Z$ ; therefore, $\mathrm{d}Z / \mathrm{d}X = 1$ .

Case 2: dY/dX=0. In this case, a change in X will produce no change in Y, and therefore, dZ/dX=0, regardless of the value of dZ/dY.

Case 3: dZ/dY = 0. In this case, a change in Y will produce no change in Z, and therefore, dZ/dX = 0, regardless of the value of dY/dX.

Since in each of these cases we have

$$
\frac {\mathrm{d} Z}{\mathrm{d} X} = \frac {\mathrm{d} Z}{\mathrm{d} Y} \wedge \frac {\mathrm{d} Y}{\mathrm{d} X},
$$

and the cases are exhaustive, this expression always obtains.

In other words, for Z to be sensitive to X, we must have both Z sensitive to Y and Y sensitive to X. We can also calculate Boolean derivatives.

There are two ways of deriving these results: constructively (by applying the definition of a Boolean derivative to the relevant expression) and nonconstructively (by showing that the result obtains for an exhaustive set of cases). Both methods are used below.

Result 3. Given Boolean variables $X_{1}$ and $X_{2}$ , we have

$$
\frac {\mathrm{d} \left(X _ {1} \wedge X _ {2}\right)}{\mathrm{d} X _ {1}} = X _ {2}.
$$

Proof 1. By definition of a Boolean derivative,

$$
\frac {\mathrm{d} \left(X _ {1} \wedge X _ {2}\right)}{\mathrm{d} X _ {1}} = \left(X _ {1} \wedge X _ {2}\right) \oplus \left(\overline {{{X}}} _ {1} \wedge X _ {2}\right).
$$

By definition of the EXCLUSIVE OR operation, this expression evaluates to

$$
\begin{array}{r l} & {\left(\left(X _ {1} \wedge X _ {2}\right) \wedge \left(\overline {{\overline {{X}} _ {1} \wedge X _ {2}}}\right)\right)} \\ & {\quad \vee \left(\left(\overline {{X _ {1} \wedge X _ {2}}}\right) \wedge \left(\overline {{X}} _ {1} \wedge X _ {2}\right)\right)} \\ & {\quad = \left(\left(X _ {1} \wedge X Z _ {2}\right) \wedge \left(X _ {1} \vee \overline {{X}} _ {2}\right)\right)} \\ & {\quad \quad \vee \left(\left(\overline {{X}} _ {1} \vee \overline {{X}} _ {2}\right) \wedge \left(\overline {{X}} _ {1} \wedge X _ {2}\right)\right)} \\ & {\quad = \left(X _ {1} \wedge X _ {2} \wedge X _ {1}\right) \vee \left(X _ {1} \wedge X _ {2} \wedge \overline {{X}} _ {2}\right)} \\ & {\quad \quad \vee \left(\overline {{X}} _ {1} \wedge \overline {{X}} _ {1} \wedge X _ {2}\right) \vee \left(\overline {{X}} _ {2} \wedge \overline {{X}} _ {1} \wedge X _ {2}\right)} \\ & {\quad = \left(X _ {1} \wedge X _ {2}\right) \vee \left(\overline {{X}} _ {1} \wedge X _ {2}\right) = X _ {2}.} \end{array}
$$

Proof 2. Consider two cases: Case 1: $X_{2} = 1$ . Then

$$
\frac {\mathrm{d} \left(X _ {1} \wedge X _ {2}\right)}{\mathrm{d} X _ {1}} = \frac {\mathrm{d} X _ {1}}{\mathrm{d} X _ {1}} = 1 = X _ {2}.
$$

Case 2: $X_{2} = 0$ . Then

$$
\frac {\mathrm{d} \left(X _ {1} \wedge X _ {2}\right)}{\mathrm{d} X _ {1}} = \frac {\mathrm{d} (0)}{\mathrm{d} X _ {1}} = 0 = X _ {2}.
$$

Since in each of these cases we have

$$
\frac {\mathrm{d} (X _ {1} \wedge X _ {2})}{\mathrm{d} X _ {1}} = X _ {2}
$$

and these cases are exhaustive, this expression always obtains.

We state without proof, as the proofs (constructive and nonconstructive) are similar, the following:

$$
\frac {\mathrm{d} (X _ {1} \vee X _ {2})}{\mathrm{d} X _ {1}} = \overline {{{X}}} _ {2},
$$

$$
\frac {\mathrm{d} (X _ {1} \rightarrow X _ {2})}{\mathrm{d} X _ {1}} = \overline {{{X}}} _ {2},
$$

$$
\frac {\mathrm{d} (X _ {1} \rightarrow X _ {2})}{\mathrm{d} X _ {2}} = X _ {1},
$$

$$
\frac {\mathrm{d} X}{\mathrm{d} X} = \frac {\mathrm{d} \overline {{X}}}{\mathrm{d} X} = \frac {\mathrm{d} X}{\mathrm{d} \overline {{X}}} = \frac {\mathrm{d} \overline {{X}}}{\mathrm{d} \overline {{X}}} = 1.
$$

We now apply these results to the logic tree described in section 2. Let D = F = 1 and E = G = 0. Then B = 0 and C = 1, which leads to A = 0. We note that changing either E or F will cause A to change, so that dA/dE = dA/dF = 1. No change in A will result from changes in D or G; hence, dA/dD = dA/dG = 0.

We can use the equations given above to find general expressions for the derivatives of the root with respect to the leaves. For example:

$$
\frac {\mathrm{d} A}{\mathrm{d} E} = \frac {\mathrm{d} A}{\mathrm{d} B} \wedge \frac {\mathrm{d} B}{\mathrm{d} E} = \overline {{{C}}} \wedge D.
$$

This tells us that two conditions must obtain for A to be sensitive to E. First, C must be false; otherwise $B \rightarrow C$ will always be true and A will be independent of the value of E. Second, D must be true; otherwise $D \wedge E$ will be false and a change in E will have no impact on the nodes above it (i.e., B and A). One can perform similar analyses with respect to the other leaf variables.

Another analysis was performed in [3], which will not be considered here. This concerns the generalization of a Boolean logic tree to a directed acyclic graph (DAG). In a DAG a single leaf variable may affect the root through more than one path. For example, let us assume that E and F are the same node in the graph of fig. 1. That is, let us assume that intangible costs are high if and only if the system is durable. In this case the chain rule given above does not apply, and a more sophisticated chain rule must be developed, as was done in [3]. Since we are concerned only with models based on trees and not with those based on DAGs, we will not examine this topic further.

This work has also been extended in [2] to include the case in which two leaf variables are changed simultaneously. For example, we may ask whether a change in the values of both D and F in fig. 1 (i.e., a change in whether tangible costs are high and also a change in whether the system is durable) will have an impact on the value of A (i.e., whether the project will be funded). In [2] a compound Boolean derivative (e.g., the derivative of A with respect to both D and F) is defined, and a chain rule (e.g., for determining the impact of changes in D and F on A through B and C) was derived. Unfortunately, the resulting analysis is rather clumsy and yields little insight into the analysis of Boolean models. Therefore, it will not be examined further here.

## 4. Fuzzy Sensitivity Analysis

We now extend this analysis to the case in which the nodes in the logic tree denote fuzzy variables. In order to do so more effectively, we must define explicitly the domain of the variables under construction. For example, if X is a variable (e.g., denoting 'cost is high'), we will define a domain variable $\omega(X)$ that represents the truth value of X - that is, the degree to which X may be asserted with confidence. As stated previously, the domain of $\omega(X)$ is the closed unit interval.

In fuzzy logic the AND operation is represented by a minimum operator applied to the $\omega(\cdot)$ functions, and OR operation is represented by a maximum operator, and a NOT by subtracting the truth value from 1. (See [6] and [12] for a more detailed discussion and some applications.) Will will derive a truth value for the IF-THEN operation by noting that $X \to Y$ is also $\overline{Y} \vee Y$ . Thus, we have

$$
\begin{array}{l}\omega (X \wedge Y) = \operatorname{MIN} (\omega (X), \omega (Y)),\\\omega (X \vee Y) = \operatorname{MAX} (\omega (X), \omega (Y)),\\\omega (X \rightarrow Y) = \operatorname{MAX} (1 - \omega (X), \omega (Y)),\\\omega (\overline {{X}}) = 1 - \omega (X).\end{array}
$$

In order to simplify notation, we will use X and $\omega(X)$ interchangeably. That is, we will write X=0.7 to mean that $\omega(X)=0.7$ ; so that the degree to which the variable X is assumed to be true is 70% of the way between 0 (i.e., FALSE) and 1 (i.e., TRUE). For example, F denotes the variable “System is durable”, and $\omega(F)$ is a number $0\leq\omega(F)\leq1$ which describes the degree to which F is to be believed. We consider the case in which the logic tree of fig. 1 contains the input (leaf) values of D=0.4, E=0.7, F=0.6, and G=0.3; we conclude that B=0.4 and C=0.6, which leads to A=0.6 as the output (root) value.

If D were to increase by a small amount – for example from 0.4 to 0.41 – there would be no change in A. Therefore, we might say that $dA/dD$ is zero when D is being increased. On the other hand, if D were to decrease – for example, from 0.4 to 0.39 – then A would increase from 0.6 to 0.61, an increase of 0.1 in A for a decrease of 0.1 in D. Therefore, we might say that $dA/dD$ is 1 for a decrease in D, except that the variables A and D will move in opposite directions. Similarly, if F were to increase by a small amount, then A would increase by the same amount, but if F were to decrease, A would not change. On the other hand, A is insensitive to E and g. That is, changing the values of E or G (or more exactly, the values of $\omega(E)$ or $\omega(G)$ ) will have no impact on the value of $\omega(A)$ . This insensitivity is independent of the direction of change – that is, the insensitivity obtains whether the incremental change in the remaining leaves (E or G) is a positive or a negative one.

In the following section we will formalize this process by defining sensitivity measures (similar to left and right derivatives) and presenting a chain rule for proceeding up the tree. However, we will observe three restrictions. First, we will consider only incremental changes; thus, we will not be concerned with what would happen if G should change from 0.3 to 0.8. Second, only one leaf variable will be allowed to change at a time; the effects of simultaneously changing several leaf variables will not be considered. Finally, we will restrict ourselves to dyadic uses of AND and OR, so that no node will have more than two nodes directly beneath it. The extension to the more general case is conceptually straightforward but leads to messier notation and does not add anything to the analysis.

## 5. Sensitivity Measures Based on Fuzzy Logic

We now define two sensitivity measures, which we will call positive and negative sensitivities, which measure the rate of increase of a function as its argument increases or decreases, respectively. In each case we assume that a fuzzy variable Y is a piecewise linear function of a fuzzy variable X. (By a fuzzy variable we mean one defined over the closed united interval for which the operations of fuzzy logic obtain.) We also make the sensitivity zero (rather than undefined) if the change would cause X to move outside of the unit interval. This will simplify the notation slightly. Thus, a sensitivity measure records the results of an attempt to change the independent variable in the appropriate direction, where an illegal attempt is recorded as no change.

Definition 2. A positive sensitivity $\Delta Y / \Delta X$ is:

(1) if $X = 1$ , then 0, otherwise,

(2) for a sufficient small $\alpha > 0$ we have $Y(X + \alpha) = Y(X) + \alpha \Delta Y / \Delta X$ .

Definition 3. A negative sensitivity $\nabla Y / \nabla X$ is:

(1) if $X = 0$ , then 0, otherwise, (2) for a sufficiently small $\alpha > 0$ we have $Y(X - \alpha) = Y(X) + \alpha \nabla Y / \nabla X$ .

Thus, a positive sensitivity is the rate of increase in Y as X increases. As such, it is the derivative of $Y(X)$ from the right, except that it is defined as 0 when X=1. A negative sensitivity is the rate of increase in Y and X decreases, and it is minus the left derivative, except that it is defined as 0 when X=0.

We now calculate the sensitivities of the operations used in the previous section:

Result 4. Given the fuzzy variables $X_{1}$ and $X_{2}$ , we have:

$$
\begin{array}{l} \frac {\Delta (X _ {1} \vee X _ {2})}{\Delta X _ {1}} = \left\{ \begin{array}{l l} 1 & \text { if } 1 > X _ {1} \geq X _ {2}, \\ 0 & \text { otherwise }, \end{array} \right. \\ \frac {\nabla (X _ {1} \vee X _ {2})}{\nabla X _ {1}} = \left\{ \begin{array}{c c} - 1 & \text { if } X _ {1} > X _ {2}, \\ 0 & \text { otherwise }. \end{array} \right. \end{array}
$$

Proof. To prove the first part of the result concerning positive sensitivities we consider three cases:

Case 1: $X_{1} = 1$ . Then $\Delta(X_{1} \vee X_{2}) / \Delta X_{1} = 0$ by definition.

Case 2: $1 > X_{1} \geq X_{2}$ . In this case $\Delta(X_{1} \vee X_{2}) / \Delta X_{1}$ is the derivative from the right of $\text{MAX}(X_{1}, X_{2})$ with respect to $X_{1}$ . Since $X_{1} < 1$ , this derivative exists, and since $X_{1} \geq X_{2}$ , this derivative is 1.

Case 3: $X_{1} < X_{2}$ . In this case $\Delta(X_{1} \vee X_{2}) / \Delta X_{1}$ is the derivative from the right of MAX $(X_{1}, X_{2})$ with respect to $X_{1}$ . Since $X_{1} < 1$ , this derivative exists, and since $X_{1} < X_{2}$ , this derivative is zero.

To prove the second part of the result we consider three cases:

Case 1: $X_{1} = 0$ . Then $\nabla (X_{1} \vee X_{2}) / \nabla X_{1} = 0$ by definition.

Case 2: $X_{1} > X_{2}$ . Therefore $X_{1} > 0$ . In this case $\nabla(X_{1} \vee X_{2}) / \nabla X_{1}$ is minus the derivative from the left of MAX( $X_{1}, X_{2}$ ) with respect to $X_{1}$ . Since $X_{1} > 0$ , this derivative exists, and since $X_{1} > X_{2}$ , this derivative is -1.

Case 3: $0 < X_{1} \leq X_{2}$ . In this case $\nabla(X_{1} \vee X_{2}) / \nabla X_{1}$ is minus the derivative from the left of $\text{MAX}(X_{1}, X_{2})$ with respect to $X_{1}$ . Since $X_{1} > 0$ , this derivative exists, and since $X_{1} \leq X_{2}$ , this derivative is zero.

We state without proof (as the proofs are similar) the following additional results:

$$
\begin{array}{l}\frac {\Delta (X _ {1} \wedge X _ {2})}{\Delta X _ {1}} = \left\{\begin{array}{l l}1&\text {if} X _ {1} <   X _ {2},\\0&\text {otherwise,}\end{array}\right.\\\frac {\nabla (X _ {1} \wedge X _ {2})}{\nabla X _ {1}} = \left\{\begin{array}{c c}- 1&\text {if} 0 <   X _ {1} \leq X _ {2},\\0&\text {otherwise,}\end{array}\right.\\\frac {\Delta \overline {{X}}}{\Delta X} = \left\{\begin{array}{c c}- 1&\text {if} X <   1,\\0&\text {if} X = 1,\end{array}\right.\\\frac {\nabla \overline {{X}}}{\nabla X} = \left\{\begin{array}{c c}1&\text {if} X > 0,\\0&\text {if} X = 0,\end{array}\right.\\\frac {\Delta (X _ {1} \rightarrow X _ {2})}{\Delta X _ {1}} = \left\{\begin{array}{c c}- 1&\text {if} X _ {1} + X _ {2} \leq 1,\\0&\text {otherwise,}\end{array}\right.\\\frac {\nabla (X _ {1} \rightarrow X _ {2})}{\nabla X _ {1}} = \left\{\begin{array}{c c}+ 1&\text {if} 0 <   X _ {1} \leq 1 - X _ {2},\\0&\text {otherwise,}\end{array}\right.\\\frac {\Delta (X _ {1} \rightarrow X _ {2})}{\Delta X _ {2}} = \left\{\begin{array}{c c}+ 1&\text {if} 1 > X _ {2} \geq 1 - X _ {1},\\0&\text {otherwise,}\end{array}\right.\\\frac {\nabla (X _ {1} \rightarrow X _ {2})}{\nabla X _ {2}} = \left\{\begin{array}{c c}- 1&\text {if} X _ {1} + X _ {2} > 1,\\0&\text {otherwise.}\end{array}\right.\end{array}
$$

Now we present a chain rule for applying these calculations to a fuzzy logic tree.

Result 5. If $Z = Z(Y)$ and $Y = Y(X)$ are fuzzy functions, then:

$$
\frac {\Delta Z}{\Delta X} = \left\{ \begin{array}{l l} \frac {\Delta Z}{\Delta Y} \times \frac {\Delta Y}{\Delta X} & \text {if} \frac {\Delta Y}{\Delta X} \geq 0, \\ - \frac {\nabla Z}{\nabla Y} \times \frac {\Delta Y}{\Delta X} & \text {if} \frac {\Delta Y}{\Delta X} \leq 0, \end{array} \right.
$$

$$
\frac {\nabla Z}{\nabla X} = \left\{ \begin{array}{l l} \frac {\Delta Z}{\Delta Y} \times \frac {\nabla Y}{\nabla X} & \text {if} \frac {\nabla Y}{\nabla X} \geq 0, \\ - \frac {\nabla Z}{\nabla Y} \times \frac {\nabla Y}{\nabla X} & \text {if} \frac {\nabla Y}{\nabla X} \leq 0. \end{array} \right.
$$

Proof. With regard to the positive sensitivity, we consider four exhaustive cases:

Case 1: X=1. Then an increase in X is not possible, and both $\Delta Y/\Delta X$ and $\Delta Z/\Delta X$ will be zero.

Case 2: X < 1 and $\Delta Y / \Delta X = 0$ . Then an increase in x will not change Y, and $\Delta Z / \Delta X$ will be zero regardless of the values of $\Delta Z / \Delta Y$ or $\nabla Z / \nabla Y$ .

Case 3: $\Delta Y / \Delta X > 0$ . Then an increase in $X$ will cause an increase in $Y$ , and by the chain rule of differential calculus, $\Delta Z / \Delta X$ will be the product of two quantities: the rate of increase of $Y$ with respect to $X$ (i.e., $\Delta Y / \Delta X$ ) and the rate of increase of $Z$ with respect to $Y$ (i.e., $\Delta Z / \Delta Y$ ).

Case 4: $\Delta Y / \Delta X < 0$ . Then an increase in $X$ will cause a decrease in $Y$ . $\nabla Z / \nabla Y$ is the rate at which $Z$ will increase as $Y$ decreases, and this quantity, multiplied by $-\Delta Y / \Delta X$ , will be the rate at which $Z$ will increase as $X$ increases.

With regard to the negative sensitivity, we consider four exhaustive cases:

Case 1: X=0. Then a decrease in X is not possible, and both $\nabla Y/\nabla X$ and $\nabla Z/\nabla X$ will be zero.

Case 2: X > 0 and $\nabla Y/\nabla X = 0$ . Then an decrease in X will not change Y, and $\nabla Z/\nabla X$ will be zero regardless of the values of $\Delta Z/\Delta Y$ or $\nabla Z/\nabla Y$ .

Case 3: $\nabla Y / \nabla X > 0$ . The a decrease in $X$ will cause an increase in $Y$ and by the chain rule of differential calculus, $\nabla Z / \nabla X$ will be the product of two quantities: the rate at which $Y$ increases as $X$ decreases (i.e., $\nabla Y / \nabla X$ ) and the rate at which $Z$ increases as $Y$ increases (i.e., $\Delta Z / \Delta Y$ ).

Case 4: $\nabla Y / \nabla X < 0$ . Then a decrease in $X$ will cause a decrease in $Y$ . $\nabla Z / \nabla Y$ is the rate at which $Z$ will increase as $Y$ decreases, and this quantity, multiplied by $-\nabla Y / \nabla X$ , will be the rate at which $Z$ will increase as $X$ decreases.

We now consider two examples of the application of these observations to the example of section 4. First, we calculate $\Delta A / \Delta D$ . Since $\Delta B / \Delta D$

is 1, we have:

$$
\frac {\Delta A}{\Delta D} = \frac {\Delta A}{\Delta B} \times \frac {\Delta B}{\Delta D} = 0 \times 1 = 0.
$$

Next we calculate $\nabla A/\nabla D$ . Since $\nabla B/\nabla D$ is 1, we have:

$$
\frac {\nabla A}{\nabla D} = \frac {\Delta A}{\Delta B} \times \frac {\nabla B}{\nabla D} = 1 \times 1 = 1.
$$

One consideration not addressed here is the effects of a compound change – that is, simultaneous changes in two or more variables – of the type mentioned for Boolean models in section 3. This can become quite complex. For example, instead of having two sensitivities (positive and negative), we would have $2^{N}$ sensitivities, where N is the number of compound variables. That is, it would be necessary to consider all combinations of increases and decreases in these variables. If one wanted to consider all possible changes among the leaf variables, then there would be $3^{M}$ sensitivities, where M is the number of leaf variables (i.e., each variable could increase, decrease, or remain fixed). The chain rule would also be more complex, especially when the compound variables are not all under the same node. Therefore, we will not investigate this topic here.

## 6. Boolean and Fuzzy Variables

We now review the relative merits of the approach developed here, based on fuzzy logic, and that developed in [3], based on Boolean logic. Boolean logic is simpler than fuzzy logic, since the former allows only two truth values, whereas the latter allows any value on the closed unit interval, measured to whatever degree of accuracy the model builder specifies. In both cases, the user of the model specifies the values of the leaf variables, and the model is used to calculate all other variable values – that is, the values of variables at all nodes, including the root of the tree. We are concerned here with the sensitivity of the value of the 'output' of the model (the root variable) with respect to the 'inputs' to the models (the leaf variables). As one might expect, the results of this analysis are more complex in the fuzzy logic case than in the Boolean case.

One area that needs further examination is the interaction between the user of a fuzzy logic model and the model itself. In some cases the user of an expert system is asked to input values of leaf variables that lie in the ranges of $[-1, +1]$ , $[-5, +5]$ , $[0, 100]$ , $[-100, +100]$ , etc. In most cases the mapping from these ranges to the closed unit interval is straightforward, (i.e., it is a simple linear transformation), but systems may be developed in the future that have more complex mappings. Some of them may make use of non-standard logics of the type discussed briefly in the following section. Another interface issue concerns the impact of the output of a fuzzy logic model, both the value of root variable and its sensitivity to change in the leaf variables, on the decision process. In conventional modeling (e.g., the construction of mathematical programming models or simulations) it is assumed that sensitivity analyses are used to: (1) determine whether a change in a decision variable will change an outcome of interest, (2) decide whether to hedge against a possible unfavorable change in an environmental variable, and/or (3) decide whether to obtain more information about the value of an environmental variable. Presumably sensitivity analyses will be used for similar purposes in logic (including fuzzy logic) modeling.

## 7. Possible Extensions

We now discuss briefly the possible extension of this framework to other types of models. (See [5,11] for more detailed discussions of these structures.) We identify five such model types.

The first consists of variations on the MAX/MIN theme for performing OR/AND operations. An example is the Bonczek–Eagin method used (among others) in the GURU system. In this method the OR operation is given by $\text{MAX}(\omega(X), \omega(Y)) + \omega(X)\omega(Y)(1 - \text{MAX}(\omega(X), \omega(Y)))$ , and the AND operation by $\omega(X)\omega(Y)(2 - \text{MIN}(\omega(X), \omega(Y)))$ . These operations are piecewise linear/quadratic rather than piecewise linear, but they are still not differentiable everywhere. Sensitivity analysis methods of the type presented in the previous section could be developed for this structure, but it would be necessary to modify the definitions of sensitivity to accommodate the nonlinear character of the Bonczek–Eagin transformations.

A second approach is to use some of the multivalued logics as a base for sensitivity analysis. One such logic, due to Lukasiewicz, is similar to the fuzzy logic presented here, except that the strength of the statement $X \rightarrow Y$ is given by MIN(1, $1 - \omega(X) + \omega(Y)$ ). It would be straightforward to modify the results of the previous sections to incorporate this function. Another multivalued logic is Kleene's three-valued logic, in which the three values are TRUE, FALSE, and UNKNOWN. Thus, (TRUE ∧ UNKNOWN) is UNKNOWN, since the expression could evaluate to either TRUE or FALSE, but (TRUE ∨ UNKNOWN) is always TRUE. A sensitivity analysis of Kleene's system would allow one to evaluate the transformation of an unknown variable to a known value.

A third approach would address the case in which the rule themselves contain fuzzy constants which are to be applied to the fuzzy variables contained in the antecedents of the rules (i.e., the 'inputs' to the non-leaf nodes) to produce the 'output' variables. In some cases, this is simple. If the fuzzy constants contained in the rules are to be applied to the antecedents in an AND or OR fashion, they can simply be treated as additional fuzzy variables. But in some cases there are two such constants, one of which is a threshold for the input to the rule. If a specified combination (usually, AND or OR) of the inputs equals or exceeds the threshold, then the other constant is combined with those of other rules that have fired (i.e., attained their thresholds), usually by a simple averaging process. Since the output of such a system is a discontinuous function of its input, simply evaluating derivatives – even pairs of one-sided derivatives – of output functions is insufficient for sensitivity analysis.

The fourth approach is to apply sensitivity analysis to some of the more unusual logics. An example might be modal logic, in which one distinguishes statements that are necessarily true (e.g., '2 + 2 = 4') from those that are possibly true (e.g., 'My name is Bob'). That is, one envisions a possible world in which I was given another name, but not one in which $2 + 2 \neq 4$ . One might ask how changes among the values of necessarily true, necessarily false, and possibly true or false will propagate throughout the system. Another example is temporal logic, in which statements can be true at some times and false at others. One might ask about the sensitivity of future values of variables with respect to present or previous values of the same or other variables.

The fifth type of model consists of those knowledge-based structures other than logic structures to which sensitivity analysis might be applied. These include semantic nets and frames. Here a perturbation that occurs in one part of a knowledge base may propagate to other parts of the knowledge base (through the arcs in the semantic net or the inheritance structure in the frames). It may be possible for simple examples of knowledge bases of these types to develop interesting analytical results.

## 8. Conclusion

We have presented a simple approach for extending an existing methodology for performing sensitivity analysis with systems based on two-valued logic to the case in which all points in the closed unit interval are possible truth values and the rules of fuzzy logic apply. The advantage of this approach over incrementing inputs and observing outputs are: (1) some insight may be gained into the structure of the model, as when one node 'blocks' changes in another node from propagating upward, (2) the sensitivity measures are proven to be first derivatives, which may not be the case when simulations are performed with positive and negative increments, since the increments may be sufficiently large than an upper or lower bound (i.e., a MAX or MIN point) is exceeded, and (3) it may be conceptually useful to have an analytical representation for an analytical treatment of this subject, even if one sometimes (or often) uses the incrementing method in practice. These results are not as simple as in the two-valued case, but they apply to an important class of information structures found in knowledge-based decision support systems.

## References

[1] Akers, Sheldon B., Jr., On a Theory of Boolean Switching Functions, Journal of the Society for Industrial and Applied Mathematics 7, No. 4 (1959) 487–498.

[2] Blanning, Robert W., Compound Sensitivity Analysis in Hierarchical Boolean Models, in: Proceedings of the Annual Meeting of the Decision Sciences Institute (November, 1987) 272–274.

[3] Blanning, Robert W., Sensitivity Analysis in Logic-Based Models, Decision Support Systems 3, No. 4 (1987) 343–349; an earlier version was published in Proceedings of the Twentieth Annual Hawaii International Conference on System Sciences (January, 1987) 665–674.

[4] Boulden, James B., Computer-Assisted Planning Systems (McGraw-Hill, New York, 1975).

[5] Holsapple, Clyde W. and Andrew B. Whinston, Business Expert Systems (Irwin, Homewood, IL, 1987).

[6] Kickert, Walter J.M., Fuzzy Theories on Decision-Making (Martinus Nijhoff, Leiden, 1978).

[7] Naylor, Thomas H. and Horst Schauland, A Survey of Users of Corporate Planning Models, Management Science 22, No. 9 (1976) 927–937.

[8] Pau, L.F., ed., Artificial Intelligence in Economics and Management (North-Holland, Amsterdam, 1986).

[9] Silverman, Barry G., ed., Expert Systems for Business (Addison-Wesley, Reading, MA, 1987).

[10] Thayse, Andre and Mark Davio, Boolean Differential Calculus and its Application to Switching Theory, IEEE Transactions on Computers, C-22, No. 4 (1973) 409–420.

[11] Turner, Raymond, Logics for Artificial Intelligence (Ellis Harwood, Chichester, 1984).

[12] Zimmerman, H.J., L.A. Zadeh and B.R. Gaines, eds., Fuzzy Sets and Decision Analysis, (North-Holland, Amsterdam, 1984).
