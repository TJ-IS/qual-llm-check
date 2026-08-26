---
otero_id: 16964
otero_key: "EE29VN5Z"
title: "Sensitivity analysis in logic-based models"
authors: "Robert W Blanning"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90105-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sensitivity Analysis in Logic-based Models \*

Robert W. BLANNING

Vanderbilt University, Nashville, TN 37203, USA

An important feature of the causal models used in most DSS is that they allow their users to perform sensitivity analyses. Most of these analyses are performed on continuous variables, which are the principal types of variables found in causal models. However, some of the models derived from artificial intelligence that are increasingly being used in DSS contain logic (or Boolean) variables. In this paper we exploit the notion of a ‘Boolean derivative’ developed for circuit design and apply it to the calculation of sensitivity measures in logic-based models.

![](/api/attachments/EE29VN5Z/fulltext/images/5c80705172bce1dc545ff7be934a2124bb91c65050aa99f30ea56bbd267359f4.jpg)

Robert W. Blanning is Associate Professor of Management at the Owen Graduate School of Management at Vanderbilt University. He has a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in operations research and management information systems. He has been a member of the faculties of the Schools of Business at New York Uniiversity and The Wharton School at the University of Pennsylvania. His teaching and research interests are in model management systems, information economics, and the management applications of artificial intelligence. He has published in such journals as Management Science, Decision Sciences, Communications of the ACM, Naval Research Logistics Quarterly, Decision Support Systems, Information & Management, Omega, Policy Analysis and Information Systems, International Journal of Policy and Information, Human Systems Management, Journal of Information Science, Long Range Planning, and Technological Forecasting and Social Change. He is a member of the Editorial Board of Decision Support Systems and is an Associate Editor in the Decision Support Systems Department of Management Science.

\* An earlier version of this paper was presented at the Twentieth Hawaii International Conference on System Sciences, held at Kailua-Kona, Hawaii, January 6–9, 1987. The paper was selected by the conference organizers for submission to Decision Support Systems. The research was supported by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

## 1. Introduction

Many existing DSS contain causal models that are based on continuous variables. For example, financial models may contain such variables as the size of an investment and the resulting rate of return, and logistical models many relate quantity produced or transported to production or shipping costs. However, these models are not used only to calculate the consequences of a particular decision. Surveys [11] and case studies [8] concerning the management use of planning models suggest that an important purpose of decision models is to help managers to perform sensitivity analyses, and this is reflected in the design of planning languages. Planning languages are programming languages (usually based on FORTRAN) that have special user interface procedures, some of which interpret and execute sensitivity analysis commands. These commands allow a user easily to change one or more inputs of a model and to observe the resulting change in outputs. For example, in EMPIRE the command 'WHAT IMPACTS PROFIT' (where WHAT IMPACTS are reserved words and PROFIT is an output of the model) will cause each input variable (such as costs, prices, production quantities, etc.) separately to be incremented by 1%; the system reports the new value of PROFIT for each change in input, the magnitude of the change in PROFIT, and the percent change in PROFIT [5]. This and other sensitivity analysis commands are an important feature of planning languages [10].

Some of the newer DSS contain not only causal models but expert (or knowledge-based) models that capture the expertise of knowledgeable and experienced managers and staff analysts and allow a less experienced user to apply them to a particular problem $[2,3,4,7,12]$ . However, the ability to perform sensitivity analyses will probably also be an important feature of these expert systems, for two reasons. First, if an input variable is a decision variable (e.g., the decision to include a certain feature in a new or established product, to implement a new marketing strategy, etc.) then it may be useful to determine the impact of an unexpected change in the environment to decide whether to hedge against it. Second, if the environment is not known with certainty, a sensitivity analysis may be useful in deciding whether to expend additional effort to find out more about it.

![](/api/attachments/EE29VN5Z/fulltext/images/6288914921140af42f36c023ca8ec01cad12f424d164207cb9e72f5690b4dc33.jpg)

Expert systems differ from causal models in that they are often logic-based rather than quantitative. Although they contain some quantitative data, the most important variables are logic variables that are either true or false. Therefore, the usual procedures for performing sensitivity analyses – incrementing an input by a marginal amount or allowing the input to vary over a range of values – do not apply. The domain of a logic variable consists of two values, and marginal increments are not defined. The purpose of this paper is to develop a procedure for the sensitivity analysis of models containing of logic variables.

## 2. Boolean Trees

One of the principal methods of knowledge representation in expert systems is the AND/OR goal tree [6,7,13]. This is a tree in which the nodes denote propositions that may be true or false. Each node except the root is combined with one or more others, using AND or OR operations, to produce a truth value of a node at the next (higher) level. Each node except for the leaves has a truth value calculated from the truth values of the nodes immediately below it, and the truth values of the leaves are the input to the system. We will extend this concept to trees containing other Boolean operations, which we will call Boolean trees (and more generally, in section 4, to Boolean graphs).

We begin by defining certain operators of mathematical logic [9], which will be used in Boolean trees and graphs. Let a, b, c, ... be propositions that may be true (denoted 1) or false (denoted 0). The logical operators are

(1) Negation: $\bar{a}$ is true if and only if $a$ is false.

(2) Conjunction: $(a \wedge b)$ is true if and only if both $a$ and $b$ are true.

(3) Inclusive disjunction: $(a \vee b)$ is true if and only if either $a$ or $b$ or both are true.

(4) Exclusive disjunction: $(a \oplus b)$ is true if and only if either $a$ or else $b$ but not both are true.

(5) Implication: $(a \to b)$ is true if and only if $b$ is true whenever $a$ is true.

(b) Graph Used in the Example

Fig. 1. Boolean Graphs.

(6) Equivalence: $(a \equiv b)$ is true if and only if $a$ and $b$ are both true or both false.

Since, conjunction is associative, we can omit imbedded parentheses and write $(a \land b \land c)$ . Similarly, inclusive disjunction is associative, and we will write $(a \lor b \lor c)$ . Exclusive disjunction and equivalence are also associative, but these operations are of significance here only when used as binary operations and therefore, will be treated here as binary operations.

We now define a Boolean tree as a tree in which the Boolean operators defined above are applied to nodes at each level to produce nodes at the next level (see fig. 1a). The unary operation of negation is applied to a single node, the binary operations of implication, exclusive disjunction, and equivalence are applied to two nodes, and the associative operations of conjunction and inclusive disjunction are applied to two or more nodes.

Consider an example, illustrated in fig. 1b, concerning a decision to manufacture a product (e.g., a furnace). The product will be manufactured if and only if both performance and delivery criteria are met. The performance criterion depends on the temperature of the furnace and whether it is heavily insulated: the temperature may be high or low, but if it is high, then the furnace must be heavily insulated for performance to be acceptable. The delivery criterion depends on the cost of the product and whether the shipment arrives early, and it is satisfied if either or both of these two conditions obtains (i.e., the customer is willing to pay a high price for early delivery). The notation of fig. 1b is as follows: $a =$ the product will be manufactured, $b =$ performance is acceptable, $c =$ delivery is acceptable, $d =$ temperature is high, $e =$ insulation is heavy, $f =$ cost is low, $g =$ shipment is early. The relationships are: $a = (b \wedge c)$ , $b = (d \rightarrow e)$ , and $c = (f \vee g)$ .

For example, if d = f = 1 and e = g = 0 (i.e., the temperature is high and the cost is low, but the insulation is not heavy and the shipment is not early), then c = 1, b = 0, and a = 0 (i.e., delivery is acceptable but performance is not acceptable and hence, the product will not be manufactured). However, if the temperature were lowered (d = 0) or the product were heavily insulated (e = 1), then performance would be acceptable and the product would be manufactured. On the other hand, if the shipment were early (g = 1), there would be no change either in the acceptability of delivery nor on the manufacturing decision. Thus, for these input data the decision to manufacture is sensitive to temperature and delivery but not to the shipment date, nor to the cost. The process just illustrated of calculating the truth values of nodes other than the leaves will be called labelling the tree, and the process of determining the impact of a change in any of the leaves on the non-leaf nodes will be called a sensitivity analysis.

One method of performing a sensitivity analysis on a labelled tree is to make a change in the truth value of one of the leaves and to relabel the tree. We present here a method that is computationally more efficient and that may offer insights into the processes being modeled by Boolean trees. This is explained and illustrated in the following section.

## 3. Boolean Derivatives

The concept of sensitivity analysis as applied to Boolean functions has already been developed in the context of electronic circuit design [1,14,15]. We will refine and as appropriate, extend this work to Boolean graphs. To simplify matters, we consider in this section only those graphs that are also trees and defer discussion of more general graphs to the following section.

Consider a Boolean function y of a Boolean variable x. That is, $y = y(x)$ . The sensitivity of y with respect to x is measured by the Boolean derivative of y with respect to x, which is 1 whenever a change in the truth value of x entails a change in the truth value of y and is 0 if no such change occurs. The Boolean derivative, denoted dy/dx, is defined as

$$
\begin{array}{r l} \frac {d y}{d x} & = y (x) \oplus y (\bar {x}) \\ & = \left(\left(y (x) \wedge \overline {{y (\bar {x})}}\right) \vee \overline {{(y (x)}} \wedge y (\bar {x})\right). \end{array}
$$

In general $y$ will be a function of several Boolean variables. If $y = y(x_1, x_2, \ldots, x_N)$ , the partial derivative of $y$ with respect to $x_1$ is

$$
\frac {\partial y}{\partial x _ {1}} = y \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \oplus y \left(\bar {x} _ {1}, x _ {2}, \dots , x _ {N}\right).
$$

We say that $y$ is sensitive to $x_1$ if $\partial y / \partial x_1 = 1$ , and 1 and that $y$ is insensitive to $x_1$ if $\partial y / \partial x_1 = 0$ .

Three useful results follow from this definition and are proven in [1,14,15]. The first is that d y/d x is invariant to negation of y or x which follows from the definition of d y/d x, that is,

$$
\frac {d y}{d x} = \frac {d \bar {y}}{d x} = \frac {d y}{d \bar {x}} = \frac {d \bar {y}}{d \bar {x}}.
$$

However, we note that $(dy / dx) \neq (\overline{dy / dx})$ and that $dy / dx$ is independent of $x$ , that is, $d^2y / dx^2 = 0$ for any $y(x)$ .

The second result is a 'chain rule' for Boolean derivatives. We define $z = z(y)$ with $y = y(x)$ and attempt to find $dz / dx$ . It is clear that $z$ is sensitive to $x$ if and only if $z$ is sensitive to $y$ and $y$ is sensitive to $x$ . Thus

$$
\frac {d z}{d x} = \frac {d z}{d y} \wedge \frac {d y}{d x}.
$$

We will find this result useful in performing sensitivity analyses at successive levels of a Boolean tree.

The third result concerns the application of Boolean derivatives to the operations of conjunction and inclusive disjunction.

$$
\frac {\partial \left(x _ {1} \wedge x _ {2} \wedge \dots \wedge x _ {N}\right)}{\partial x _ {1}} = x _ {2} \wedge x _ {3} \wedge \dots \wedge x _ {N},
$$

$$
\frac {\partial \left(x _ {1} \vee x _ {2} \vee \dots \vee x _ {N}\right)}{\partial x _ {1}} = \overline {{{x}}} _ {2} \wedge \overline {{{x}}} _ {3} \wedge \dots \wedge \overline {{{x}}} _ {N}.
$$

We now extend these results to the operations of exclusive disjunction, equivalence, and implication.

Theorem 1:

$$
\frac {\partial \left(x _ {1} \equiv x _ {2}\right)}{\partial x _ {1}} = \frac {\partial \left(x _ {1} \oplus x _ {2}\right)}{\partial x _ {1}} = 1,
$$

$$
\frac {\partial \left(x _ {1} + x _ {2}\right)}{\partial x _ {2}} = \overline {{{x}}} _ {2},
$$

$$
\frac {\partial \left(x _ {1} + x _ {2}\right)}{\partial x _ {2}} = x _ {1}.
$$

This is proven in appendix 1.

We now address the issue raised at the end of the previous section: the calculation of the sensitivities of each element in a Boolean tree with respect to the elements at the various levels beneath it. The procedure is recursive. At each level, Boolean derivatives are used to calculate derivatives at the next level, and the chain rule is used to calculate derivatives of elements at a level with respect to elements more than one level below them.

Consider the example described in the previous section. Since $a = (b \vee c)$ , we have

$$
\frac {\partial a}{\partial b} = c \quad \text { and } \quad \frac {\partial a}{\partial c} = b.
$$

Similarly, since $b = (d \to e)$ and $c = (f \vee g)$ , we have

$$
\begin{array}{l l} \frac {\partial b}{\partial d} = \bar {e} & \text {and} \quad \frac {\partial b}{\partial e} = d, \quad \text {and} \\ \frac {\partial c}{\partial f} = \bar {g} & \text {and} \quad \frac {\partial c}{\partial g} = \bar {f}. \end{array}
$$

Thus, we have obtained the Boolean derivatives of the elements at each level with respect to the elements at the level immediately below.

To calculate the Boolean derivatives of elements separated by more than one level (in this case, the Boolean derivatives of a with respect to $d, e, f,$ and $g)$ , we apply the chain rule as follows:

$$
\frac {d a}{d d} = \frac {\partial a}{\partial b} \wedge \frac {\partial b}{\partial d} = c \wedge \bar {e},
$$

$$
\frac {d a}{d e} = \frac {\partial a}{\partial b} \wedge \frac {\partial b}{\partial e} = c \wedge d,
$$

$$
\frac {d a}{d f} = \frac {\partial a}{\partial c} \wedge \frac {\partial c}{\partial f} = b \wedge \bar {g},
$$

$$
\frac {d a}{d g} = \frac {\partial a}{\partial c} \wedge \frac {\partial c}{\partial g} = b \wedge \bar {f}.
$$

For example, if $d = f = 1$ and $e = g = 0$ , we have $b = 0$ , $c = 1$ , and $a = 0$ . Therefore,

$$
\begin{array}{l} \frac {d a}{d d} = c \wedge \bar {e} = 1 \wedge 1 = 1, \\ \frac {d a}{d e} = c \wedge d = 1 \wedge 1 = 1, \\ \frac {d a}{d f} = b \wedge \bar {g} = 0 \wedge 1 = 0, \\ \frac {d a}{d g} = b \wedge \bar {f} = 0 \wedge 0 = 0, \end{array}
$$

which is confirmed by the analysis of the previous section.

There are two advantages of calculating Boolean derivatives in this fashion. The first is computational efficiency. We could have defined a directly as function of $d, e, f$ , and $g$ (i.e., $a = ((d \mapsto e) \wedge (f \vee g))$ ) and calculated the Boolean derivatives of a with respect to $d, e, f$ , and $g$ using the definition of a Boolean derivative. For example $da / de$ would be calculated by evaluating the expression

$$
\big ((d \to e) \land (f \lor g) \big) \oplus \big ((d \to \bar {e}) \land (f \lor g) \big).
$$

This would be tedious. Furthermore, da/de would be expressed in terms of d, e, f, and g (i.e., $da/de = ((f \vee g) \wedge d)$ ). But one would not calculate da/de numerically unless the tree were already labelled and the value of c were known. The resulting calculation $da/de = (c \wedge d)$ is simpler. This relative simplicity would be even greater for trees of greater depth and breadth than the one illustrated here.

The second advantage of this approach is that it may yield insights into the structure of processes being modeled by Boolean trees. Consider again the result $da/de = c \wedge d$ . This tells us that a will be sensitive to e if and only if conditions c and d both obtain. In other words, the decision to manufacture the product is affected by the presence or absence of heavy insulation if and only if the temperature is high and delivery is acceptable. If delivery were not acceptable, the product would not be manufactured and it would be immaterial whether the product were heavily insulated. On the other hand, if delivery were acceptable, then the decision to manufacture would be sensitive to the presence of heavy insulation if and only if the temperature were high. If the temperature were high, then the decision to manufacture the product would depend on the presence of heavy insulation; but if the temperature were not high, performance would be acceptable, and it would not matter whether the product were heavily insulated. Once again, this explanatory advantage is even greater for large trees.

In summary, we have defined sensitivity in Boolean trees as a Boolean derivative and have presented a simple calculation procedure that has the advantages of computational efficiency and explanatory power. However, the approach presented here and the problem being analyzed were deliberately simplified in order to focus on important concepts rather than mathematical details. An extension of these concepts to the more complex problem of Boolean graphs is examined in the following section.

## 4. Boolean Graphs

We now consider the case of a Boolean graph that is not a tree, such that a single node at one level may affect more than one node at the next higher (or any higher) level. If in the example of the previous section e and f were equivalent (so that heavy insulation is equivalent to low cost), then the graph would not be a tree. The labeling procedure would still be straightforward, but sensitivity analysis would be more difficult.

The cause of the difficulty is that the chain rule of result two no longer applies, because a would be affected by the new node that replaces e and f through both b and c. We now extend the chain rule to this more complex case. The extension of the chain rule to the operations of conjunction and inclusive disjunction is given in

Theorem 2. (1) Let $z = \wedge_{i} y_1(x) = y_1(x) \wedge y_2(x) \wedge \ldots \wedge y_N(x)$ . Then

$$
\begin{array}{l} \frac {d z}{d x} = \left(\left(\bigwedge_ {i} \left(\bar {y} _ {i} \vee \frac {\overline {{d y _ {i}}}}{d x}\right)\right) \vee \left(\bigwedge_ {i} \left(y _ {i} \vee \frac {\overline {{d y _ {i}}}}{d x}\right)\right)\right) \\ \quad \wedge \left(\bigwedge_ {i} \left(y _ {i} \vee \frac {d y _ {i}}{d x}\right)\right). \\ (2) L e t z = \wedge_ {i} y _ {i} (x) = y _ {i} (x) \vee y _ {2} (x) \vee \dots \vee y _ {N} (x). \\ T h e n \\ \frac {d z}{d x} = \left(\left(\bigwedge_ {i} \left(\bar {y} _ {i} \vee \frac {\overline {{d y _ {i}}}}{d x}\right)\right) \vee \left(\bigwedge_ {i} \left(y _ {i} \vee \frac {d y _ {i}}{d x}\right)\right)\right) \\ \quad \wedge \left(\bigwedge_ {i} \left(\bar {y} _ {i} \vee \frac {d y _ {i}}{d x}\right)\right). \end{array}
$$

This is proven in appendix 2.

The extension to the operations of exclusive disjunction, equivalence, and implication is given in

$$
\begin{array}{r l} \text { Theorem   3: } & \\ \frac {d (y _ {1} (x) \oplus y _ {2} (x))}{d x} = \frac {d (y _ {1} (x) \equiv y _ {2} (x))}{d x} \\ & = \frac {d y _ {1}}{d x} \oplus \frac {d y _ {2}}{d x}, \\ \frac {d (y _ {1} (x) \to y _ {2} (x))}{d x} = \text { the   truth   table   in   table   1 }. \end{array}
$$

(The truth table given in table 1 is the subset of the truth table for which $d(y_1(x) \to y_2(x)) / dx$ takes on the value 1, that is, the tuples for which the derivative is zero are omitted.) This theorem is proven in appendix 3.

In the example of the previous section let nodes $e$ and $f$ be combined to produce a single node, which we will call $h$ . We wish to calculate $da / dh$ . (The calculations of $da / dd$ and $da / dg$ are performed as in section 3.) Let $d = y = 1$ and $g = 0$ . Then $b = c = a = 1$ , $db / dh = d = 1$ , and $dc / dh = \bar{g} = 1$ . To calculate $da / dh$ we use the first part of Theorem 2, letting $N = 2$ , $z = a$ , $y_1 = b$ , $y_2 = c$

Truth Table for Theorem 3.

<table><tr><td> $y_1$ </td><td> $y_2$ </td><td> $\frac{dy_1}{dx}$ </td><td> $\frac{dy_2}{dx}$ </td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td></tr></table>

and $x = h$ , as follows:

$$
\begin{array}{r l} \frac {d a}{d h} & = \left(\left(\left(\overline {{b}} \vee \frac {\overline {{d b}}}{d h}\right) \wedge \left(\overline {{c}} \vee \frac {\overline {{d c}}}{d h}\right)\right) \right. \\ & \quad \vee \left(\left(b \vee \frac {\overline {{d b}}}{d h}\right) \wedge \left(c \vee \frac {\overline {{d c}}}{d h}\right)\right) \\ & \quad \wedge \left(\left(b \vee \frac {d b}{d h}\right) \wedge \left(c \vee \frac {d c}{d h}\right)\right) \\ & = \left(\left((0 \vee 0) \wedge (0 \vee 0)\right) \vee ((1 \vee 0) \wedge (1 \vee 0))\right) \\ & \quad \wedge ((1 \vee 1) \wedge (1 \vee 1)) = 1, \end{array}
$$

which can be verified by setting h = 0 and relabeling the graph.

## 5. Conclusion

We have seen that the concept of sensitivity analysis, often formalized as a partial derivative of related measure (i.e., dual variable, adjoint variable, or Lagrange multiplier), may be extended to logic-based models in which the variables are Boolean. There appear to be two fruitful areas for further research. The first is to extend these notions to some of the other logics used in artificial intelligence, such as fuzzy logic and modal logic [6,16]. The second is to examine the concept of sensitivity analysis in expert systems that are based on constructs other than first-order logic, such as situation-action rules, semantic or other nets, and frames [7,13]. It is not clear how successful such efforts might be, but is appears that the concept of sensitivity analysis may usefully be extended beyond its traditional domain – causal models with continuous variables.

Appendix 1

We prove Theorem 1:

$$
\begin{array}{l}\frac {\partial (x _ {1} \equiv x _ {2})}{\partial x _ {1}} = \frac {\partial (x _ {1} \oplus x _ {2})}{\partial x _ {1}} = 1,\\\frac {\partial (x _ {1} \rightarrow x _ {2})}{\partial x _ {1}} = \bar {x} _ {2},\\\frac {\partial (x _ {1} \rightarrow x _ {2})}{\partial x _ {2}} = x _ {1}.\end{array}
$$

Proof. We begin by demonstrating that $\partial(x_1 \equiv x_2)/\partial x_1 = 1$ . Although this could be proven by

writing

$$
\begin{array}{r l}(x _ {1} \equiv x _ {2})&= (x _ {1} \rightarrow x _ {2}) \wedge (x _ {2} \rightarrow x _ {1})\\&= (\bar {x} _ {1} \vee x _ {2}) \wedge (\bar {x} _ {2} \vee x _ {1})\end{array}
$$

and applying the definition of a Boolean derivative, it can be demonstrated more simply. The expression $(x_{1} \equiv x_{2})$ is 1 whenever $x_{1}$ and $x_{2}$ have the same truth value and is 0 otherwise. Therefore, changing the truth value of $x_{1}$ with $x_{2}$ unchanged will always change the value of $(x_{1} \equiv x_{2})$ ; hence $\partial(x_{1} \equiv x_{2})/\partial x_{1} = 1$ .

The second part of this result follows from the first:

$$
\frac {\partial \left(x _ {1} \oplus x _ {2}\right)}{\partial x _ {1}} = \frac {\partial \left(\overline {{x _ {1} \equiv x _ {2}}}\right)}{\partial x _ {1}} = \frac {\partial \left(x _ {1} \equiv x _ {2}\right)}{\partial x _ {1}} = 1.
$$

The third and fourth parts of this result are obtained as follows:

$$
\begin{array}{l}\frac {\partial (x _ {1} \rightarrow x _ {2})}{\partial x _ {1}} = \frac {\partial (\bar {x} _ {1} \vee x _ {2})}{\partial x _ {1}} = \frac {\partial (\bar {x} _ {1} \vee x _ {2})}{\partial \bar {x} _ {1}} = \bar {x} _ {2},\\\frac {\partial (x _ {1} \rightarrow x _ {2})}{\partial x _ {2}} = \frac {\partial (\bar {x} _ {1} \vee x _ {2})}{\partial x _ {2}} = x _ {1}\end{array}
$$

Appendix 2

We prove Theorem 2:

(1) Let $z = \wedge_{i} y_{i}(x) = y_{1}(x) \wedge y_{2}(x) \wedge \ldots \wedge y_{N}(x)$ . Then

$$
\begin{array}{l} \frac {d z}{d x} \left(\left(\bigwedge_ {i} \left(\bar {y} _ {i} \vee \frac {\overline {{d y _ {i}}}}{d x}\right)\right) \vee \left(\bigwedge_ {i} \left(y _ {i} \vee \frac {\overline {{d y _ {i}}}}{d x}\right)\right)\right) \\ \wedge \left(\bigwedge_ {i} \left(y _ {i} \vee \frac {d y _ {i}}{d x}\right)\right). \end{array}
$$

(2) Let $z = \vee_{i} y_{i}(x) = y_{1}(x) \vee y_{2}(x) \vee \ldots y_{N}(x)$ . Then

$$
\begin{array}{l} \frac {d z}{d x} = \left(\left(\bigwedge_ {i} \left(\bar {y} _ {i} \vee \frac {\overline {{d y _ {i}}}}{d x}\right)\right) \vee \left(\bigwedge_ {i} \left(y _ {i} \vee \frac {\overline {{d y _ {i}}}}{d x}\right)\right)\right) \\ \wedge \left(\bigwedge_ {i} \left(\bar {y} _ {i} \vee \frac {d y _ {i}}{d x}\right)\right). \end{array}
$$

Proof. Let $S$ be the subset of $\{i = 1 \ldots N\}$ for which $\mathrm{d}y_i / dx = 0$ . Consider the conjunctive case. The formula given for $dz / dx$ is a conjunction of two components, which correspond to two conditions that are individually necessary and collectively sufficient for $dz / dx = 1$ . The first condition is that $y_i = 0$ for all $i \in S$ or $y_i = 1$ all $i \in S$ , for otherwise $z = 0$ independent of $x$ . Thus, we must have $dy_{i} / dx \to \bar{y}_{i}$ for $i = 1 \ldots N$ or $\mathrm{d}y_{i} / \mathrm{d}x \to y_{i}$ for $i = 1 \ldots N$ . This condition is stated in the first component of the formula for $\mathrm{d}z / \mathrm{d}x$ .

The second condition is that $y_{i} = 1$ for all $i \in \overline{S}$ , for otherwise $z = 0$ independent of $x$ . Thus, we must have $(\overline{dy_i / dx}) \to y_i$ for $i = 1 \ldots N$ . This is stated in the second component of the formula for $dz / dx$ .

The formula for the disjunctive case is derived in a similar fashion.

## Appendix 3

We prove Theorem 3:

$$
\begin{array}{r l}\frac {d (y _ {1} (x) \oplus y _ {2} (x))}{d x}&= \frac {d (y _ {1} (x) \equiv y _ {2} (x))}{d x}\\&= \frac {d y _ {1}}{d x} \oplus \frac {d y _ {2}}{d x},\\\frac {d (y _ {1} (x) \rightarrow y _ {2} (x))}{d x}&= \text { the   truth   table   in   table   1. }\end{array}
$$

Proof. For the first case

$$
\begin{array}{r l} & \frac {d (y _ {1} (x) \oplus y _ {2} (x))}{d x} \\ & = (y _ {1} (x) \oplus y _ {2} (x)) \oplus (y _ {1} (\bar {x}) \oplus y _ {2} (\bar {x})) \\ & = (y _ {1} (x) \oplus y _ {2} (\bar {x})) \oplus (y _ {1} (x) \oplus y _ {2} (\bar {x})) \\ & = \frac {d y _ {1}}{d x} \oplus \frac {d y _ {2}}{d x}. \end{array}
$$

Since equivalence is the negation of exclusive disjunction, the result for equivalence is the same. The result for implication is derived either by expanding the function

$$
\begin{array}{r l}&\frac {d (y _ {1} (x) \rightarrow y _ {2} (x))}{d x}\\&\quad = (y _ {1} (x) \rightarrow y _ {2} (x)) \oplus (y _ {1} (\bar {x}) \rightarrow y _ {2} (\bar {x}))\\&\quad = (y _ {1} \rightarrow y _ {2}) \oplus \left(\left(y _ {1} \oplus \frac {d y _ {1}}{d x} \rightarrow \left(y _ {2} \oplus \frac {d y _ {2}}{d x}\right)\right)\right),\end{array}
$$

or by directly working out the truth table.

## Acknowledgement

This research was supported by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

## References

[1] Sheldon B. Akers, Jr., On a Theory of Boolean Switching Functions, Journal of the Society for Industrial and Applied Mathematics 7, Nr. 4 (Dec., 1959) 487–498.

[2] Robert W. Blanning, ed., Foundations of Expert Systems for Management, to be published by Verlag Rheinland, Koln (1986).

[3] Robert W. Blanning, Management Applications of Expert Systems, Information & Management 7, Nr. 6 (Dec., 1984) 311–316.

[4] Robert W. Blanning, Issues in the Design of Expert Systems for Management, Proceedings of the National Computer Conference (July, 1984) 489–495.

[5] Germain Boer, A Beginner's Guide to EMPIRE, Applied Data Research, Princeton (1980).

[6] M. Bohanek, I. Bratko and V. Rajkovic, An Expert System for Decision Making, in: H.G. Sol, ed., Processes and Tools for Decision Support (North-Holland, Amsterdam, 1983).

[7] Robert H. Bonmczek, Clyde W. Holsapple and Andrew B. Whinston, Foundations of Decision Support System (Academic Press, New York, 1981).

[8] James B. Boulden, Computer-Assisted Planning Systems (McGraw-Hill, New York, 1975).

[9] Angelo Margaris, First Order Mathematical Logic (Blaisdell, Waltham, 1967).

[10] Thomas H. Naylor and Michele Mann, Computer Based Planning Systems, Planning Executives Institute, Oxford (1982).

[11] Thomas H. Naylor and Horst Schauland, A Survey of Users of Corporate Planning Models, Management Science 22, Nr. 9 (May, 1976) 927–937.

[12] L.F. Pau, Artificial Intelligence in Economics and Management (North-Holland, Amsterdam, 1986).

[13] Elaine Rich, Artificial Intelligence (McGraw-Hill, New York, 1983).

[14] Frederick F. Seller, Jr., M.Y. Hsiao and L.W. Bearnson, Analyzing Errors with the Boolean Difference, IEEE Transactions on Computers C-17, Nr. 7 (July, 1968) 676–683.

[15] Andre Thayse and Mark Davio, Boolean Differential Calculus and its Application to Switching Theory, IEEE Transactions on Computers C-22, Nr. 4 (April, 1973) 409–420.
