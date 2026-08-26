---
otero_id: 17700
otero_key: "NCQ5ER8P"
title: "On sensitivity analysis for a class of decision systems"
authors: "Cs. Mészáros; T. Rapcsák"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00012-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On sensitivity analysis for a class of decision systems $^{1}$

Cs. Mészáros, T. Rapcsák \*

Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences, P.O. Box 63, XI. Kende u. 11–13, H-1518 Budapest Hungary

## Abstract

The sensitivity analysis of general decision systems originated from the Bridgman model is dealt with. It is shown that these problems are equivalent to the optimization of linear fractional functions over rectangles. By using the specialities of decision problems, an $O(n \log n)$ algorithm is elaborated for solving such problems. Computational experience is also given.

Keywords: Decision systems; Sensitivity analysis; Interval analysis; Fractional programming; Computational complexity

## 1. Introduction

The solution of a decision problem consists in selecting the best one from the available alternatives or creating an alternative better than the already existing ones. The concepts of “best” and “better” are based upon preferences or values, terms which are used as synonyms in decision theory.

As some values of decision models are often subjective (e.g., weights), uncertain and different with respect to the units of measure, the sensitivity analysis of the components of decision systems seems to be important to verify the final ranking of the alternatives. The theoretical bases of decision theory is not considered a well-defined special area in mathematics, therefore, a proper mathematical tool to solve special decision problems might be interesting.

We discuss some basic decision models and a sophisticated group DSS based on the generalization of these models, which is capable to support the solution of a wide class of decision problems. The real-life applications of this software system request the sensitivity analysis of many decision parameters, e.g., subjective ones as weights and objective ones, e.g., in utility functions. Three different sensitivity problem classes are suggested, due to the application of interval analysis. We will show that these general sensitivity problems lead to the optimization of linear fractional functions over rectangles and a polynomial algorithm with a bound $O(n \log n)$ is proposed for solving such a problem. Computational experience is also reported on.

In the second section, the classical Bridgman model (1963) and one of its modifications are studied on the basis of the generalized Kullback and Leibler I-divergence function introduced in 1951 for measuring the difference of two discrete probability distributions. Numerous applications prove the usefulness of this function, e.g., in science and engineering Kapur (1989) and in decision theory to measure the similarity of two decision vectors. Csiszár's axiomatic approach to these measures provides a parallel characterization of least squares approximation and the Kullback and Leibler I-divergence [7]. This section ends with the description of a group decision support system based on the generalization of these models by using multiattribute utility decomposition (MAUD) for the individual ranking of alternatives, and different decision principles depending on entropy optimization problems.

In the third section, it is shown that all the sensitivity problems defined previously by the preceding decision models determine the same special type of fractional programming problems. In the fourth section, we show a real-life application of the sensitivity analysis. In the Appendix, algorithms are worked out for the numerically effective solution of these problems, and computational experience is given.

## 2. Decision problems

The type of decision situations considered here contains one or more decision makers who are to evaluate and rank a finite number of alternatives with respect to a finite number of criteria. The basic model was introduced by Bridgman (1963). Here, a more general version will be described.

There are n alternatives with m criteria. Let $A_{1}, A_{2}, \ldots, A_{n}$ denote the alternatives and $C_{1}, C_{2}, \ldots, C_{m}$ the criteria. Assume that the data related to the alternatives are known and we are able to rank the criteria by weighting them. Let $a_{ij} > 0$ , $i = 1, \ldots, m$ , $j = 1, \ldots, n$ denote the value of the jth alternative with respect to the ith criterion, $w_{i} > 0$ , $i = 1, \ldots, m$ the weight of the ith criterion and $x_{j}$ , $j = 1, \ldots, n$ the unknown final ranking values of the alternatives. The data of the decision problem may be written in tabular form:

$$
\begin{array}{c c c} & & x _ {1} \quad \ldots \quad x _ {n} \\ & & A _ {1} \quad \ldots \quad A _ {n} \\ w _ {1} & C _ {1} & \left[ \begin{array}{c c c} a _ {1 1} & \ldots & a _ {1 n} \\ \vdots & \ddots & \vdots \\ a _ {m 1} & \ldots & a _ {m n} \end{array} \right]. \\ w _ {m} & C _ {m} \end{array}\tag{2.1}
$$

The decision problem is the evaluation of the alternatives, i.e., the determination of the vector x by taking every criterion with the given weight into account so that the result should “fit well” into the rows of matrix (2.1). The decision principle is to minimize the weighted sum of the generalized Kullback’s I-divergence [15,16] based on the evaluation vectors of the criteria and the vector $\mathbf{x} = (x_{1}, \ldots, x_{n})^{T}$ . This principle can be formulated as the following entropy optimization problem:

$$
\begin{array}{l} \min \frac {\sum_ {i = 1} ^ {m} w _ {i} D (\mathbf {x} | | \mathbf {a} _ {i})}{\sum_ {i = 1} ^ {m} w _ {i}} \\ \sum_ {j = 1} ^ {n} x _ {i} = c, \\ x _ {j} \geq 0, j = 1, \dots , n, \end{array}\tag{2.2}
$$

where the generalized Kullback's I-divergence is defined in $R_{+}^{n}$ (the positive orthant of $R^{n}$ ) as

$$
D (\mathbf {x} \| \mathbf {a} _ {i}) = \sum_ {j = 1} ^ {n} x _ {j} \log \left(\frac {x _ {j}}{a _ {i j}}\right) - \sum_ {j = 1} ^ {n} x _ {j} + \sum_ {j = 1} ^ {n} a _ {i j},
$$

$\mathbf{a}_i = (a_{i1}, \dots, a_{in})^T$ , $i = 1, \dots, m$ and $c$ is an arbitrary finite real number.

Introduce the notation $\Sigma_{i=1}^{m} w_{i}=w$ . Then, the optimal solution of (2.2) has an explicit form:

$$
x _ {j} = c \frac {\prod_ {i = 1} ^ {m} a _ {i j} ^ {w _ {i} / w}}{\sum_ {k = 1} ^ {n} \prod_ {i = 1} ^ {m} a _ {i k} ^ {w _ {i} / w}}, j = 1, \dots , n.\tag{2.3}
$$

Remark that this model is more general than the original Bridgman model [1] because the generalized $I$ -divergence is defined in $R_{+}^{n}$ instead of the set $R_{+}^{n} \cap \{x | \Sigma_{i=1}^{n} x_{i} = 1\}$ defining the discrete probability distributions.

It is well-known that the generalized I-divergence is not symmetric in the variables x and $a_{i}$ [16], thus a new decision principle can be formulated by changing the vectors $a_{i}, i=1,\ldots,m$ and the vector x in the objective function. In this way, another model of Bridgman type is obtained:

$$
\begin{array}{l} \min \frac {\sum_ {i = 1} ^ {m} w _ {i} D (\mathbf {a} _ {i} | | \mathbf {x})}{\sum_ {i = 1} ^ {m} w _ {i}} \\ \sum_ {j = 1} ^ {n} x _ {i} = c, \\ x _ {j} \geq 0, j = 1, \dots , n. \end{array}\tag{2.4}
$$

The optimal solution of model (2.4) has also an explicit form of

$$
x _ {j} = c \frac {\sum_ {i = 1} ^ {m} \frac {w _ {i}}{w} a _ {i j}}{\sum_ {k = 1} ^ {n} \sum_ {i = 1} ^ {m} \frac {w _ {i}}{w} a _ {i k}}, j = 1, \dots , n.\tag{2.5}
$$

It follows that the most popular decision principles (the geometric and arithmetic means) can be originated as explicit solutions of the same type of entropy optimization problems. Since any kind of distances widely used in statistics and engineering (e.g., Pearson and Hellinger) can be substituted for the objective function of $(2.4)$ , so we obtain a general rule to choose decision principles. The sensitivity analysis of these decision problems may consist of the solution of problem $(2.4)$ by using interval arithmetics. When the explicit solution can be obtained as a general mean value given in the form of

$$
x _ {j} = \phi^ {- 1} \left(\sum_ {i = 1} ^ {m} \frac {w _ {i}}{w} \phi (a _ {i j})\right), j = 1, \dots , n,\tag{2.6}
$$

where $\phi$ is a strictly monotone real function, then the elaborated sensitivity analysis can be applied. This class contains infinitely many elements, because the mean values

$$
\left(\sum_ {i = 1} ^ {m} \frac {w _ {i}}{w} a _ {i j} ^ {\alpha}\right) ^ {1 / \alpha}
$$

(generalized arithmetic and geometric means) can be explicitly obtained as the solution of the corresponding entropy optimization problem by Hölder–Young distances [13] given in the form of

$$
\begin{array}{r l} H _ {\alpha} (x | | a _ {i}) & = \frac {1}{\alpha (1 - \alpha)} \sum_ {j = 1} ^ {m} \alpha x _ {j} \\ & + (1 - \alpha) a _ {i j} - x _ {j} ^ {\alpha} a _ {i j} ^ {1 - \alpha}, \alpha \in R, \end{array}\tag{2.7}
$$

where $H_{\alpha}(x||a_{i})$ is defined by limit value for $\lambda=0$ and $\lambda=1$ . We point out that the Bridgman type model (2.4) can be obtained from (2.6) with voting $\phi(x)=x$ and the Bridgman model with $\phi(x)=\log(x)$ .

It seems to be important to consider a class of decision principles because the arithmetic mean to average normalized numbers (e.g., in the case of characteristics with different dimensions) may be meaningless in certain decision problems [9].

Our Department has developed a highly flexible group decision support system named WINGDSS 4.0 [4–6] based on a multiattribute utility decomposition which can be considered a generalization of the basic decision models in several directions. Instead of a decision maker, several ones are considered and among the criteria, the relations determine a decision tree. So, the application of the rule detailed above for choosing a decision principle should be extended to this general situation, because this type of sensitivity problems was required when solving real-life problems with WINGDSS.

The main purpose of a group decision process is the coordination of the decision related activities of the involved individuals or subgroups who may have different perspectives or priorities.

WINGDSS 4.0 supports the following group decision process:

The decision task is the ranking of a finite number of alternatives according to the result of their evaluation with respect to certain criteria. The set of alternatives, their attributes, the set of criteria and the evaluation functions are the same for all decision makers during a decision session. (WINGDSS 4.0 is a very flexible system with respect to task construction or modification.)

Criteria are arranged into a tree. One starts with the most general criterion and decomposes it gradually into more specific ones. The decision makers' individual preferences on the criteria set will be expressed as weights. Their individual evaluation will be carried out on the leaf (the non-decomposable) criteria by using utility functions. WINGDSS 4.0 provides its users with tools for the definition of the functions, appropriate for the actual decision task. For each alternative, the final score at the root of the criteria will be calculated as the above defined general mean value of the values achieved on the basic level criteria and of the weights expressing the individual preferences. This method (called Multi Attribute Utility Decomposition) provides the individual ranking of the alternatives according to their final scores.

Decision makers will be qualified on each criterion, according to their expertise. Their competency and influence on decision making, their weighing and evaluation will be revised by the system facilitator in the form of voting powers (weights). From the individual preferences, the group weights are calculated as the weighted sum of the individual weights and voting powers. Similarly, the group evaluation at each leaf criterion is the aggregation of the decision makers' voting powers and the values they gave individually.

Group score for each alternative will be the combination of the group weights and the group evaluations. This leads to the ranking of the alternatives by an objective method reflecting the perspectives, opinion, expertise and priorities of the group members. By [10], this kind of aggregation of the individual evaluations satisfies the axioms of cardinal group utility functions.

References from the successful applications of WINGDSS 4.0 software can be obtained from the Hungarian Telecommunication Company, the State Property Agency, the Ministry of Welfare and the Ministry for Environment and Regional Policy.

## 3. Sensitivity problems of decision systems

In this section, we suppose that the final ranking values are computed by a general mean value, i.e.,

$$
x _ {j} = \phi^ {- 1} \left(\sum_ {i = 1} ^ {m} \frac {w _ {i} \phi (a _ {i j})}{w}\right), j = 1, \dots , n,
$$

where $\phi: R^{+} \to R^{+}$ is a strictly monotone increasing function. We presume that the input data for the ranking are uncertain, and incidentally degenerate intervals in the positive orthant are given for the weights and for the utility values: $w_{i} \in [w_{i}^{-}, w_{i}^{+}]$ and $a_{ij} \in [a_{ij}^{-}, a_{ij}^{+}]$ , $i = 1, \ldots, m$ , $j = 1, \ldots, n$ . For handling the uncertainty more suitable for the requirements of real-life applications, we consider the case where the weights are not normalized to 1. The consideration of the case of normalized weights, e.g., “the uncertainty of the weights is 10%” requires the solution of a fractional programming problem. Our first sensitivity problem is the computation of the upper and lower bounds of the final ranking values ( $x_{j}^{-}$ and $x_{j}^{+}$ ) for the alternatives $A_{j}$ , $j = 1, \ldots, n$ . Now, let $c_{ij} = \phi(a_{ij})$ , $c_{ij}^{+} = \phi(a_{ij}^{+})$ and $c_{ij}^{-} = \phi(a_{ij}^{-})$ . It is easy to see that for $j = 1, \ldots, n$ ,

$$
x _ {j} ^ {-} = \phi^ {- 1} \left(\min \sum_ {i = 1} ^ {m} \frac {t _ {i} c _ {i} ^ {-}}{\sum_ {k = 1} ^ {m} t _ {k}}\right), t _ {i} \in \left[ w _ {i} ^ {-}, w _ {i} ^ {+} \right],
$$

$$
i = 1, \dots , m,\tag{3.1}
$$

and

$$
\begin{array}{l} x _ {j} ^ {+} = \phi^ {- 1} \left(\max \sum_ {i = 1} ^ {m} \frac {t _ {i} c _ {i} ^ {+}}{\sum_ {k = 1} ^ {m} t _ {k}}\right), t _ {i} \epsilon \big [ w _ {i} ^ {-}, w _ {i} ^ {+} \big ], \\ i = 1, \ldots , m. \end{array}
$$

So, the sensitivity problem is transformed into the following special fractional programming problems:

minimize

$$
\frac {c ^ {T} t}{e ^ {T} t}
$$

and

maximize

$$
\frac {c ^ {T} t}{e ^ {T} t}\tag{3.2}
$$

where every component of e is 1 and $w^{1}, w^{2}, t, c, e \in R^{m}$ . Another interval approach of the classical decision models was suggested in [8].

In the inverse sensitivity problems, the question is as follows. What are the intervals of the weights with the restriction that the final ranking of the alternatives does not change? The inverse sensitivity problems can be derived from the inverse Bridgman model [12] by using intervals instead of variables.

Assume that the alternatives are ranked in decreasing order. We consider the parametric set $W_{\lambda} = [w_{1} - \lambda w_{1}^{1}, w_{1} - \lambda w_{1}^{2}]x...x[w_{m} - \lambda w_{m}^{1}, w_{m} - \lambda w_{m}^{2}]$ . We determine the maximum value of $\lambda$ so that the final ranking of the alternatives does not change if the vector of the weights can vary in $W_{\lambda}$ . In other words, for $t \in W_{\lambda}$ and for $j = 1, ..., n - 1$ , it should be

$$
\phi^ {- 1} \left(\frac {\sum_ {i = 1} ^ {m} c _ {i j} t _ {i}}{\sum_ {i = 1} ^ {m} t _ {i}}\right) > \phi^ {- 1} \left(\frac {\sum_ {i = 1} ^ {m} c _ {i , j + 1} t _ {i}}{\sum_ {i = 1} ^ {m} t _ {i}}\right).
$$

We reformulate these restrictions in the following simple parametric problem:

$$
\begin{array}{l} \max _ {\lambda} \left\{\min _ {t \in W \lambda} \left(\frac {\sum_ {i = 1} ^ {m} c _ {i j} t _ {i}}{\sum_ {i = 1} ^ {m} t _ {i}} - \frac {\sum_ {i = 1} ^ {m} c _ {i , j + 1} t _ {i}}{\sum_ {i = 1} ^ {m} t _ {i}}\right) > 0 \right\}, \\ j = 1, \dots , n - 1. \end{array}\tag{3.3}
$$

The optimal value of t can be easily determined for every index j, thus an interval is obtained for $\lambda$ (see the example). From a geometrical point of view, the problem is to inflate a regular convex body of the weights such that the constraints satisfy.

The following problem is a very interesting and important one:

Consider a subset of the alternatives in which the change of the final ranking alternative values is allowed in a given interval. In what intervals are the weights allowed to vary, and how will these modifications effect the final ranking values in the entire set of the alternatives? A linear fractional programming problem similar to $(3.2)$ can be used to solve the above problem, as we shall see in the Appendix. To demonstrate the previous ideas we give the following example:

Example 3.1

There are 4 cars as alternatives denoted by $A_{1}=Car1$ , $A_{2}=Car2$ , $A_{3}=Car3$ and $A_{4}=Car4$ . Our 5 criteria are $C_{1}=Price$ , $C_{2}=Speed$ , $C_{3}=Consumption$ , $C_{4}=Reliability$ , $C_{5}=Comfort$ . The given weight of the criteria are $w_{1}=60$ , $w_{2}=30$ , $w_{3}=70$ , $w_{4}=80$ , $w_{5}=50$ . The following table which corresponds to (2.1) contains the evaluations of the alternatives with respect to the criteria:

<table><tr><td></td><td></td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td></tr><tr><td></td><td></td><td>Car1</td><td>Car2</td><td>Car3</td><td>Car4</td></tr><tr><td> $w_{1}$ </td><td>Price</td><td>80</td><td>50</td><td>40</td><td>20</td></tr><tr><td> $w_{2}$ </td><td>Speed</td><td>30</td><td>75</td><td>55</td><td>90</td></tr><tr><td> $w_{3}$ </td><td>Consumption</td><td>70</td><td>20</td><td>40</td><td>10</td></tr><tr><td> $w_{4}$ </td><td>Reliability</td><td>50</td><td>60</td><td>35</td><td>80</td></tr><tr><td> $w_{5}$ </td><td>Comfort</td><td>40</td><td>60</td><td>55</td><td>80</td></tr></table>

The resulting ranking values of the alternatives by the Bridgman type model (2.4) and (2.5) are $x_{1}=57.241$ , $x_{2}=49.827$ , $x_{3}=42.759$ and $x_{4}=51.724$ .

In the first sensitivity problem, the weights can be changed by 10%. The question is how the ranking values change. By assumptions, the intervals for the weights are $[w_{1}^{1}, w_{1}^{2}] = [54, 66]$ , $[w_{2}^{1}, w_{2}^{2}] = [27, 33]$ , $[w_{3}^{1}, w_{3}^{2}] = [63, 77]$ , $[w_{4}^{1}, w_{4}^{2}] = [72, 88]$ and $[w_{5}^{1}, w_{5}^{2}] = [45, 55]$ . So, we obtain 4 fractional programming problems to compute the lower bounds of the final ranking values, and 4 fractional programming problems to compute the upper bounds. For example, the two fractional programming problems related to the alternative Car1 are as follows:

$$
\begin{array}{l} \min \frac {8 0 t _ {1} + 3 0 t _ {2} + 7 0 t _ {3} + 5 0 t _ {4} + 4 0 t _ {5}}{t _ {1} + t _ {2} + t _ {3} + t _ {4} + t _ {5}} \\ 5 4 \leq t _ {1} \leq 6 6, \\ 2 7 \leq t _ {2} \leq 3 3, \\ 6 3 \leq t _ {3} \leq 7 7, \\ 7 2 \leq t _ {4} \leq 8 8, \\ 4 5 \leq t _ {5} \leq 5 5, \end{array}
$$

for computing the lower bound, and

$$
\begin{array}{l} \max \frac {8 0 t _ {1} + 3 0 t _ {2} + 7 0 t _ {3} + 5 0 t _ {4} + 4 0 t _ {5}}{t _ {1} + t _ {2} + t _ {3} + t _ {4} + t _ {5}} \\ 5 4 \leq t _ {1} \leq 6 6, \\ 2 7 \leq t _ {2} \leq 3 3, \\ 6 3 \leq t _ {3} \leq 7 7, \\ 7 2 \leq t _ {4} \leq 8 8, \\ 4 5 \leq t _ {5} \leq 5 5, \end{array}
$$

for computing the upper bound of the final ranking value of Car1. After solving these problems, the following intervals are obtained for the final ranking values:

$$
\begin{array}{r c l} \left[ x _ {1} ^ {1}, x _ {1} ^ {2} \right] & = & [ 5 5. 6 7 0, 5 8. 8 1 5 ], \\ \left[ x _ {2} ^ {1}, x _ {2} ^ {2} \right] & = & [ 4 8. 3 0 9, 5 1. 2 4 5 ], \\ \left[ x _ {3} ^ {1}, x _ {3} ^ {2} \right] & = & [ 4 2. 1 1 2, 4 3. 4 6 5 ], \\ \left[ x _ {4} ^ {1}, x _ {4} ^ {2} \right] & = & [ 4 8. 3 6 2, 5 5. 0 1 7 ]. \end{array}
$$

These results show that the least sensible alternative is Car3, and the most sensible is Car4.

What percentage of the weights can be changed under the restriction that the final ranking of the alternatives does not change is our next question. In this case, the parametric problem (3.3) can be solved as follows:

Because $x_{1} > x_{4}$ , our first condition is

$$
\min \left(\frac {8 0 t _ {1} + 3 0 t _ {2} + 7 0 t _ {3} + 5 0 t _ {4} + 4 0 t _ {5}}{t _ {1} + t _ {2} + t _ {3} + t _ {4} + t _ {5}} - \frac {2 0 t _ {1} + 9 0 t _ {2} + 1 0 t _ {3} + 8 0 t _ {4} + 8 0 t _ {5}}{t _ {1} + t _ {2} + t _ {3} + t _ {4} + t _ {5}}\right) > 0
$$

subject to

$$
6 0 - 0. 6 \lambda \leq t _ {1} \leq 6 0 + 0. 6 \lambda ,
$$

$$
3 0 - 0. 3 \lambda \leq t _ {1} \leq 3 0 + 0. 3 \lambda ,
$$

$$
7 0 - 0. 7 \lambda \leq t _ {1} \leq 7 0 + 0. 7 \lambda ,
$$

$$
8 0 - 0. 8 \lambda \leq t _ {1} \leq 8 0 + 0. 8 \lambda ,
$$

$$
5 0 - 0. 5 \lambda \leq t _ {1} \leq 5 0 + 0. 5 \lambda .
$$

We use an equivalent parametric problem wherein the minimum value which is independent of $\lambda$ can be easily determined by substituting the objective function

$$
\begin{array}{r l} & \min (8 0 t _ {1} + 3 0 t _ {2} + 7 0 t _ {3} + 5 0 t _ {4} + 4 0 t _ {5} - 2 0 t _ {1} \\ & \quad + 9 0 t _ {2} + 1 0 t _ {3} + 8 0 t _ {4} + 8 0 t _ {5}) > 0 \end{array}
$$

for the preceding one. The minimum value in this case is $1600 - 140\lambda$ , thus $\lambda < 11.428$ .

Likewise, from the $x_{4}>x_{2}$ case $\lambda<9.910$ and from the $x_{2}>x_{3}$ case $\lambda<42.268$ . So, the weights can be changed by 9.91%. This value is generated by the $x_{4}>x_{2}$ case which corresponds to our first result, i.e., the most sensible alternative is Car4.

## 4. Computational experience

The application for the appraisal of hotels was an experimental task with WINGDSS [3]. Fifteen hotels from different parts of Hungary were evaluated and ranked. When carrying out the sensitivity analysis, the sensitivity of the parameters (e.g., discount rate, interest rate, value per square meter) given by decision makers was remarkable, since during the process, the final ranking of hotels may change considerably, due to a minimal alteration in parameters. In the experiment, the final ranking of hotels was strongly influenced by the fair market value, the condition and the result of yield- and goodwill analysis. Some results deriving from computational experience in appraisal of hotels by applying the mentioned first sensitivity analysis model can be seen in Table 1. The first column contains the identifying codes of the hotels and the second one the final ranking values. The upper and lower bounds are in columns 3. and 4., and the last column contains the relative uncertainty of the final ranking values, when we allow to change the values of some sensitive parameters up to 10%.

Table 1  
Evaluation of hotels with sensitivity analysis

<table><tr><td>Hotel</td><td>Ranking value</td><td>Upper bound</td><td>Lower bound</td><td>Relative interval</td></tr><tr><td>SVED</td><td>3966.95557</td><td>3303.71655</td><td>4451.47412</td><td>28.93%</td></tr><tr><td>HUSA</td><td>2937.12207</td><td>2400.05713</td><td>3289.07959</td><td>30.27%</td></tr><tr><td>BPN</td><td>2901.98877</td><td>2576.43384</td><td>3116.05493</td><td>18.59%</td></tr><tr><td>UHNY</td><td>1423.03332</td><td>1035.00183</td><td>1627.60596</td><td>41.64%</td></tr><tr><td>NPT</td><td>887.35553</td><td>499.17285</td><td>1157.42078</td><td>74.18%</td></tr><tr><td>ZEUS</td><td>605.62219</td><td>443.34732</td><td>728.40381</td><td>47.07%</td></tr><tr><td>AR</td><td>515.38892</td><td>350.06619</td><td>601.68250</td><td>48.82%</td></tr><tr><td>BAL</td><td>495.14444</td><td>316.11301</td><td>600.93610</td><td>57.52%</td></tr><tr><td>MK</td><td>487.34442</td><td>326.15384</td><td>574.45728</td><td>50.95%</td></tr><tr><td>HET</td><td>467.85556</td><td>328.45743</td><td>541.96924</td><td>45.64%</td></tr><tr><td>X</td><td>444.26666</td><td>292.78430</td><td>531.64533</td><td>53.77%</td></tr><tr><td>CITY</td><td>383.24445</td><td>272.31314</td><td>443.34503</td><td>44.63%</td></tr><tr><td>HAL</td><td>363.24445</td><td>210.46785</td><td>462.17761</td><td>69.29%</td></tr><tr><td>RIA</td><td>301.27777</td><td>183.90129</td><td>374.83719</td><td>63.38%</td></tr><tr><td>NOST</td><td>164.73334</td><td>89.24743</td><td>207.00766</td><td>71.49%</td></tr></table>

## 5. Concluding remarks

The sensitivity analysis seems to be a useful tool of decision support systems. In the paper, we discuss the following three sensitivity problems related to the classical Bridgman model and the generalizations of the latter, as well as a sophisticated group decision support system originated from the preceding ones: What are the intervals of the alternatives with the restriction that the intervals of the weights are given? What are the intervals of the weights with the restriction that the final ranking of the alternatives does not change? Consider a subset of the alternatives in which the change of the alternative values is allowed in a given interval. In what intervals are the weights allowed to vary, and how will these modifications effect the values in the entire set of the alternatives?

By using the rules of interval arithmetics, the above problems may be transformed into the optimization of linear fractional functions over a rectangle. To solve these special problems an efficient polynomial algorithm with a bound $O(n \log n)$ is developed. The results are demonstrated with an example.

In the case of the discussed problems, the decision space is Euclidean. Several applications require such decision models, but we know some with nonlinear decision space as well. The paper does not deal with this latter, so the question, namely, how to handle sensitivity problems in nonlinear cases seems to remain open.

## Acknowledgements

We express our thanks to Prof. T. Vámos and J. Fülöp for the valuable advice.

## Appendix A. Solving the fractional programming problem

We consider the linear fractional programming problem (called also hyperbolic problem) to be solved in the following form:

$$
\text { maximize } f (x) = \frac {c ^ {T} x}{e ^ {T} x} \quad \text { subject   to } \quad a \leq x \leq b,\tag{A.1}
$$

where a, b, c, e and x are N-vectors, furthermore, every component of e is 1. We assume that $a \leq b$ and $e^{T}a > 0$ , then the denominator of f is positive for any feasible solution of (A.1). Since the minimization of f can be performed by the maximization of -f, only the maximization problem will be discussed here.

Let the N-vector d be defined by $d_{i}=b_{i}-a_{i}, i=1,\ldots,N$ . Without loss of generality, we can also assume that $d_{i}>0$ for $i=1,\ldots,n$ and $d_{i}=0$ for $i=n+1,\ldots,N$ , where $1\leq n\leq N$ . We have then $x_{i}=a_{i}=b_{i}, i=n+1,\ldots,N$ , for any feasible solution of (A.1).

Let $P = \{x \in R^{N} | a \leq x \leq b\}$ be the rectangle of the feasible solutions of (A.1). Let $V(P)$ denote the set of the vertices of $P$ . For any $\bar{x} \in V(P)$ , let $A(\bar{x})$ be the set of the vertices of $P$ which are adjacent to $\bar{x}$ . Naturally, for an $x \in V(P)$ we have $x \in A(\bar{x})$ if and only if there exists an integer $j = j(x) \in \{1, ..., n\}$ such that $\bar{x}_{i} = x_{i}$ for $i \in \{1, ..., N\} \setminus \{j\}$ and $\bar{x}_{j} \neq x_{j}$ . In addition, $x_{j} = a_{j} + b_{j} - \bar{x}_{j}$ .

The objective function f is pseudomonotonic, i.e., both pseudoconvex and pseudoconcave in P. The following statement follows from the theory of fractional programming [17].

Proposition A.1. The optimum of (A.1) is attained at a vertex P. An $\bar{x} \in V(P)$ is an optimal solution of (A.1) if and only if

$$
f (\bar {x}) \geq f (x) \text {   for   every   } x \in A (\bar {x}).\tag{A.2}
$$

Consequently, (A.1) can be solved by the simplex method. We start at a vertex of P and step on adjacent vertices increasing the objective function value until an $\bar{x} \in V(P)$ fulfilling (A.2) is obtained. Problem (A.1) is a special case of linear fractional programming with interval programming constraints whose matrix is of full row rank:

$$
\max \frac {c ^ {T} x + c _ {0}}{d ^ {T} x + d _ {0}} \text {   subject   to   } a \leq A x \leq b.\tag{A.3}
$$

Charnes and Cooper in [2] provided an explicit general solution for (A.3) which gives the following proposition and algorithm in our case:

Proposition A.2. Consider an $\bar{x} \in V(P)$ and an $x \in A(\bar{x})$ . Let $j = j(x)$ . Then, $f(x) > f(\bar{x})$ if and only if

$$
\operatorname{sign} \left(x _ {j} - \bar {x} j\right) \left(c _ {j} - f (\bar {x})\right) > 0.\tag{A.4}
$$

## A.1. Algorithm

Step 0: Set $\bar{x} \leftarrow a, g \leftarrow c^T a$ and $h \leftarrow e^T \bar{x}$ . By sorting the components of $c$ , determine a permutation $p$ of $\{1, \dots, n\}$ such that the sequence $\{c_{p(i)}\}_{i=1}^n$ is monotone nonincreasing. Set $j \leftarrow 1$ .

Step 1: Set $\varphi \leftarrow g / h$ . If $j > n + 1$ , then stop, otherwise set $k \leftarrow p(j)$ . If $c_k \leq \varphi$ , then stop. Otherwise, set $\bar{x}_k \leftarrow b_k, g \leftarrow g + c_k d_k, h \leftarrow h + d_k$ and $j \leftarrow j + 1$ . Repeat Step 1.

Consequently, by sorting the components of c and using a suitable order of choice of the indices j, (A.1) can be solved in at most n simplex iterations and in $O(n \log n)$ arithmetic operations. The final $\bar{x}$ is an optimal solution of (A.1) and $\varphi$ is its objective function value. The detailed description of the method can be found in [2].

Now, we return to the sensitivity analysis problem formulated at the end of Section 3. Let J denote the set of indices of the alternatives whose values are allowed to vary in the interval $[x_{j}^{1}, x_{j}^{2}]$ , and for all $j \in J$ let $c_{i}$ be defined as in Section 3. Suppose that the values $c_{i}, i = 1, \ldots, m$ are sorted in decreasing order for all $j \in J$ .

To discuss the problem we use the same parametric approach as in (3.3). We consider the following real functions:

$$
f _ {j} (\lambda) = \left\{\min \frac {c ^ {t} x}{e ^ {t} x}, x \in W _ {\lambda} \right\},
$$

and, respectively,

$$
F _ {j} (\lambda) = \left\{\max \frac {c ^ {t} x}{e ^ {t} x}, x \in W _ {\lambda} \right\}
$$

for all $j \in J$ . So, we have the problem

max $\lambda$ subject to $\phi (x_j^1)\leq f_j(\lambda)\leq F_j(\lambda)\leq \phi (x_j^2),$

$$
j \in J.\tag{A.5}
$$

Clearly, $f_{j}$ and $F_{j}$ are continuous functions, $f_{j}$ is monotone decreasing, and $F_{j}$ is monotone increasing, and both functions are piecewise hyperbolic. The breakpoints of $f_{j}$ (and $F_{j}$ , respectively) can be determined as follows: by setting out from the value $\lambda = 0$ and from the corresponding optimal vertex of (A.1). Then,

$$
f _ {j} (\lambda) = \frac {\sum_ {l = 1} ^ {k} c _ {l} \left(w _ {l} + \lambda w _ {l} ^ {1}\right) + \sum_ {l = k + 1} ^ {n} c _ {l} \left(w _ {l} - \lambda w _ {l} ^ {2}\right)}{\sum_ {l = 1} ^ {k} \left(w _ {l} + \lambda w _ {l} ^ {1}\right) + \sum_ {l = k + 1} ^ {n} \left(w _ {l} - \lambda w _ {l} ^ {2}\right)}.\tag{A.6}
$$

Increasing the value of $\lambda$ from zero, the optimal vertex of (A.1) changes only if (A.4) holds, therefore the next breakpoint of $f_{i}$ is the value of $\lambda$ wherein

$$
c _ {k - 1} = \frac {\sum_ {l = 1} ^ {k} c _ {l} \left(w _ {l} + \lambda w _ {l} ^ {1}\right) + \sum_ {l = k + 1} ^ {n} c _ {l} \left(w _ {l} - \lambda w _ {l} ^ {2}\right)}{\sum_ {l = 1} ^ {k} \left(w _ {l} + \lambda w _ {l} ^ {1}\right) + \sum_ {l = k + 1} ^ {n} \left(w _ {l} - \lambda w _ {l} ^ {2}\right)}.
$$

The last breakpoint of $f_{j}$ is obtained if k = 1. It is obvious that $f_{j}$ and $F_{j}$ have at most n breakpoints, so the solution of (A.5) can be easily determined. After the determination of the rectangle of the weights, the value of the other alternatives can be computed as it is described in the first part of this section.

## A.2. Computational algorithms

The sensitivity analysis (3.1) and (3.3) must be often used for large decision problems, or e.g., in the case of MAUD, for small or moderate size problems. Therefore, we require a fast algorithm to compute. Clearly, the problem (3.3) has no computational difficulty, therefore we examine problem (3.1) only.

Table 2  
Comparison of the computational efficiency

<table><tr><td>n</td><td>SIMPLEX</td><td>QUICKSORT</td><td>HEAPSORT1</td><td>HEAPSORT2</td><td>RADIX</td></tr><tr><td>50</td><td>0.00981</td><td>0.01018</td><td>0.01074</td><td>0.00907</td><td>0.00444</td></tr><tr><td>100</td><td>0.01851</td><td>0.02037</td><td>0.02370</td><td>0.01833</td><td>0.01000</td></tr><tr><td>200</td><td>0.03703</td><td>0.04351</td><td>0.05148</td><td>0.04000</td><td>0.01759</td></tr><tr><td>300</td><td>0.05518</td><td>0.06796</td><td>0.08222</td><td>0.06074</td><td>0.02648</td></tr><tr><td>400</td><td>0.07277</td><td>0.09463</td><td>0.11518</td><td>0.08370</td><td>0.03463</td></tr><tr><td>500</td><td>0.09129</td><td>0.11963</td><td>0.14666</td><td>0.10629</td><td>0.04277</td></tr><tr><td>600</td><td>0.11000</td><td>0.14518</td><td>0.17981</td><td>0.12981</td><td>0.05185</td></tr><tr><td>700</td><td>0.12740</td><td>0.17166</td><td>0.21425</td><td>0.15277</td><td>0.06018</td></tr><tr><td>800</td><td>0.14555</td><td>0.19740</td><td>0.24796</td><td>0.17685</td><td>0.06851</td></tr><tr><td>900</td><td>0.16463</td><td>0.22444</td><td>0.28296</td><td>0.19870</td><td>0.07759</td></tr><tr><td>1000</td><td>0.18277</td><td>0.24925</td><td>0.31666</td><td>0.22351</td><td>0.08518</td></tr></table>

Sorting in the proposed algorithm is a difficult step. Our first idea was the application of QUICKSORT, which algorithm has good references [14]. We obtain better results by exploiting proposition (A.4), i.e., the sorting procedure can be stopped after determining the first k utmost element, if $c_{j} < f(x)$ for $i = k + 1, \ldots, n$ . The HEAPSORT algorithm can be modified in this way, the decrease of the computational time is shown in Table 2. The original HEAPSORT is called HEAPSORT1, and the modified algorithm HEAPSORT2.

We gain the best result by the modification of RADIX sorting. If we know any $M_{1}$ and $M_{2}$ such that $M_{1} \leq c_{i} \leq M_{2}$ for $i = 1, \ldots, n$ , we get a partition of $[M_{1}, M_{2}]$ consisting of l sorted intervals. We can put every element into one interval only. These elements inside an interval are unsorted, on the other hand, the intervals are sorted. Hereupon, we must sort the elements in one interval only, wherein a $c_{j} < f(x)$ exists. The expected behavior of this method is linear.

Our last algorithm is suggested by the simplex method: if (A.4) is fulfilled for j, then change $x_{j}$ , update $f(x)$ , and step to $j+1$ . This loop for $j=1,\ldots,n$ is repeated while j in the previous loop exists and fulfils (A.4). Our experiments show that the expected behavior of the algorithm is also linear. This procedure is called SIMPLEX.

The first column of Table 2 contains the dimension of the test problems, and the further columns the running times of different algorithms. The computational results were obtained on IBM-PC 386. The running times in Table 2 are the average computational times of 50 problems of the same dimension, and are given in seconds.

## References

[1] P.W. Bridgman, Dimensional Analysis (Yale University Press, New Haven, 1963).

[2] A. Charnes and W.W. Cooper, An Explicit General Solution in Linear Fractional Programming, Naval Research Logistics Quarterly 20 (1973) 449–446.

[3] P. Csáki, L. Csiszár, F. Fölsz, K. Keller, Cs. Mészáros, T. Rapcsák and P. Turchányi, A Decision Model for Appraisal of Hotels, Proceedings of the Third Conference on Artificial Intelligence, Ed., P. Koch, John von Neumann Society for Computer Sciences (1993) 69–78.

[4] P. Csáki, T. Rapcsák, P. Turchányi and M. Vermes, Research and Development for Group Decision Aid in Hungary by WINGDSS, a Microsoft Based Group Decision Support System, Decision Support Systems 14 (1995) 205–217.

[5] P. Csáki, L. Csiszár, F. Fölsz, K. Keller, Cs. Mészáros, T. Rapcsák and P. Turchányi, A Flexible Framework for Group Decision Support: WINGDSS 3.0, Proceedings of the Third Conference on Applied Mathematical Programming, APMOD 93, Volume of Extended Abstracts, Ed: I. Maros, Akaprint, Budapest (1993) 69–78 and Annals of Operations Research 58 (1995) 441–453.

[6] P. Csáki, F. Fölsz, K. Keller, Cs. Mészáros, G. Lóránt, T. Rapcsák and Á. Tóth, Visualization in the Decision Support System WINGDSS 4.0, KOI'95, Proc. 5th. Conf.

on Operational Research (1995) 1–32.

[7] I. Csiszár, Why Least Squares and Maximum Entropy? An Axiomatic Approach to Inverse Problems, The Annals of Statistics 19 (1991) 2032–2066.

[8] P.C. Fishburn, Decision and Value Theory (John Wiley and Sons, New York, London, Sydney, 1964).

[9] P.J. Fleming and J.J. Wallace, How Not to Lie with Statistics: The Correct Way to Summarize Benchmark Results, Communications of the ACM 29 (1968) 218–221.

[10] R.L. Keeney, Group Preference Axiomatization with Cardinal Utility, Management Science 23 (1976) 140–146.

[11] J.S. Kelly, Social Choice Theory (Springer-Verlag, Berlin, Heidelberg, New York, 1988).

[12] E. Klafszky and B. Ottmár, An Application of the Informational Divergence by Evaluating Building Structures, Proceedings of the Bicentury Anniversary of Technical University of Budapest, Budapest (1983) 65–68.

[13] E. Klafszky, Hölder-Young Distance and its Application to Decision Problems, Preprint, Budapest (1992) (in Hungarian).

[14] D.E. Knuth, Sorting and Searching. The Art of Computer Programming 3 (Addison-Wesley, Reading, MA, 1973).

[15] S. Kullback and P. Leibler, On Information and Sufficiency, Annals of Mathematical Statistics 22 (1951) 79–86.

[16] S. Kullback, Information Theory and Statistics, (John Wiley and Sons, New York, 1959).

[17] B. Martos, Nonlinear Programming Theory and Methods (Akadémiai Kiadó, Budapest, 1975).

[18] W.H. Press, B.P. Flanney, S.A. Teukolsky and W.T. Vetterling, Numerical Recipes (Cambridge University Press, Cambridge, 1986).

[19] H. Ratschek and R.L. Voller, What Can Interval Analysis Do for Global Optimization, Journal of Global Optimization 1 (1991) 11–130.

Csaba Mészáros is a young researcher of the Laboratory of Operations Research and Decision Systems, Computer and Automation Research Institute, Hungarian Academy of Sciences and between 1993–1996 a Ph.D. student at the Lóránd Eötvös University of Science, Budapest, Hungary. His research interests are linear optimization, interior point method and decision support systems.

Tamás Rapcsák is the head of the Laboratory and Department of Operations Research and Decision Systems, Computer and Automation Research Institute, Hungarian Academy of Sciences. He received his Ph.D. in nonlinear optimization at Kossuth Lajos University of Sciences, Debrecen, Hungary in 1974; Degree Candidate of Sciences in nonlinear optimization from the Hungarian Academy of Sciences in 1985. His research interests include optimization theory and decision support systems.
