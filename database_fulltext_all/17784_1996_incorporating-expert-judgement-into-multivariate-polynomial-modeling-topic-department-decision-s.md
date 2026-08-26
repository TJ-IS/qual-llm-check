---
otero_id: 17784
otero_key: "TY6ECYXE"
title: "Incorporating expert judgement into multivariate polynomial modeling Topic department: Decision support systems foundations"
authors: "Pavel M. Brusilovskiy; Leo M. Tilman"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00039-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Incorporating expert judgement into multivariate polynomial modeling

# Topic department: Decision support systems foundations

Pavel M. Brusilovskiy $^{a}$ , Leo M. Tilman $^{b,*}$

$^{a}$ Conrail Corp. & the Academy of Natural Sciences of Philadelphia, Philadelphia, USA $^{b}$ BlackRock Financial Management, Inc., New York, USA

Received 30 May 1995; revised 25 August 1995; accepted 29 December 1995

## Abstract

The study focuses on the conceptual approach to the systematic decision support in polynomial modeling of complex systems and deals with an unusual overlapping of mathematical modeling and decision theory. While incorporating non-formal expert judgement into empirical models, a whole new analytical framework emerged, which successfully resolved a number of new issues, such as formalization of expert knowledge, consistency of expert and empirical information, and generalization of the traditional concept of the “best” model. The described ideas are invariant over the empirical quality criteria and numerical methods used to estimate the coefficients of models. The purpose of the research was to combine expert knowledge and information extracted from the empirical data in order to construct models depicting the fundamental dynamics of the given system on a macro level. The paper provides a unified decision-making framework which can be used in decision support systems involving mathematical modeling.

Keywords: Adequate method; Best model; Binary relation; Complex system; Connection; Empirical information; Expert judgement; Expert indistinguishability; GMDH; Incongruity; Measure of consistency; Multivariate polynomial modeling; Power of influence; Regression; Types of knowledge

The function of an expert is not to be more right than other people, but to be wrong for more sophisticated reasons. David Butler

## 1. Introduction

Mathematical models have become the major tool in decision making and the study of complex systems in modern finance, economics, public health, environmental and social sciences, as well as other fields. However, very frequently it is necessary to build such models when empirical data are sporadic, non-representative or uncharacteristic, or when expert knowledge about the functioning mechanism of the given system is incomplete. As a result, the constructed models exhibit a lack of meaningfulness from the viewpoint of experts and are unsuitable for forecasting. In speaking about the “traditional” methods of polynomial modeling – regression analysis [6,11], group method of data handling (GMDH) [13], mean risk minimization method [14], Chebyshev approximations [9], spline approximations [12] – one may consider various underlying axiomatic assumptions, or tests which are being performed to check statistical hypotheses, or the types of knowledge which are being used. Analyzing the latter, one might notice that all of those methods directly use only information contained in the empirical data, which we will call the empirical component of knowledge. $^{1}$ For several decades, the scientific interests of many researchers were focused on the improvement and further development of the different aspects within those traditional methods: estimation and dealing with multicollinearity, increasing of the robustness of the algorithms, their insensitivity to noise, etc. However, such approaches were quite natural at this stage of modeling when it was assumed that all empirical information was given and that basically all the information about the given system had been exhausted by this empirical data.

Today, a great deal of useful and important information about complex systems which are to be modeled is contained in the non-formal knowledge, experience, and intuition of experts who work with those systems, while methods which control the reliability of such expert knowledge are constantly improving [1]. We will call this type of information the expert component of knowledge. The intension of our research was to show how the synthesis of expert and empirical information can increase the quality, reliability, and credibility of modeling and make it possible to construct models which would both approximate empirical data and absorb the knowledge of experts. It will be shown in this article that such “synthetic” models have the capability to identify relationships which ordinary models (those based on single types of knowledge) would “miss”. As we will see, new issues dealing with the consistency of different types of knowledge arise, and it becomes logical to generalize the traditional notion of the “best” model.

The paper is organized as follows: In Section 2, we describe the use of expert knowledge on the early stages of modeling, present the basic definitions and briefly summarize the properties of the “objective” quality criteria. Section 3 contains the introduction and analysis of a special class of multivariate functions which is used later to develop so-called “measures of consistency”. Section 4, 5, 6, 7 are devoted to the conceptually different methods of combining expert and empirical information: first, a type of expert knowledge which can be used in modeling is introduced and formalized, then the concept of the subjective quality of models (based on the expert information) and the quantitative measures of the consistency of expert and empirical information are defined and analyzed. Section 8 applies the results of the previous sections to the decision making stage of modeling and to the selection of the adequate methods which incorporate expert judgement into the modeling process.

The article contains the solutions and an essential development of the problems formulated by the authors in earlier publications $[2]$ and uses the language first employed by the authors in the problems of classifications in bio-assessment $[3]$ . It deals with an unusual overlapping of mathematical modeling and decision theory and is devoted to the systematic conceptual approach to the polynomial modeling of complex systems through synthesis of expert judgement and empirical data. The unified framework presented in the paper allows us to apply the underlying approach to quite different types of expert knowledge as well as to various numerical methods. In other words, the ideas described below are invariant over the particular numerical methods or algorithms used to estimate coefficients and “objective” (based only on the empirical information) quality of models and are applicable to various types of expert knowledge. All the main stages of modeling are considered within a single approach and pursue the following main goal: to construct models which best reflect the functioning mechanism of the given system on a macro level.

Table 1  
Empirical data available to modeler

<table><tr><td>Variable Observation</td><td> $x_{1}$ </td><td> $x_{2}$ </td><td></td><td> $x_{n}$ </td><td>y</td></tr><tr><td>1</td><td> $x_{11}$ </td><td> $x_{12}$ </td><td>...</td><td> $x_{1n}$ </td><td> $y_{1}$ </td></tr><tr><td>2</td><td> $x_{21}$ </td><td> $x_{22}$ </td><td>...</td><td> $x_{2n}$ </td><td> $y_{2}$ </td></tr><tr><td>...</td><td></td><td></td><td>...</td><td></td><td></td></tr><tr><td>t</td><td> $x_{t1}$ </td><td> $x_{t2}$ </td><td>...</td><td> $x_{tn}$ </td><td> $y_{t}$ </td></tr></table>

## 2. Initial stages of modeling: Independent variables, arguments, and objective criteria

The first step of the modeling - forming the list of independent variables - necessarily requires the use of expert knowledge. Thus, every invited expert forms his or her own set of “independent variablescandidates”. The final set $X = \{x_1, \ldots, x_n\}$ of independent variables is a resulting solution for a group of experts obtained via any method of constructing the resulting expert opinions. The next step involves the collection of empirical data usually presented as shown in Table 1, where $x_{ij}$ is the $i$ th observation of $j$ th variable, $i = \overline{1,t}$ ; $j = \overline{1,n}$ . It is assumed that all empirical information available to the modeler at this stage is contained in this table.

From now on, unless stated otherwise, consider the dependences of the outcome variable y from the independent variables $\{x_{1},\ldots,x_{n}\}$ in the form of the polynomial in $x_{1},\ldots,x_{n}$ of the degree k:

$$
\begin{array}{l} y = a _ {0} + \sum_ {i = 1} ^ {n} a _ {i} x _ {i} + \sum_ {i \leq j} ^ {n} b _ {i j} x _ {i} \cdot x _ {j} + \dots \\ \quad + \sum_ {i \leq \dots \leq q} ^ {n} c _ {i, \dots , q} \underbrace {x _ {i} \cdot \dots \cdot x _ {q}} _ {}, \end{array}\tag{2.1}
$$

where $a_{i}$ , $b_{ij}$ , $c_{i,\ldots,q}$ are the coefficients to be estimated using only the empirical information from Table 1, all indexes vary from 1 to n, and k is determined by experts. Let us denote by F the family of such functions.

Definition 2.1. The variables $\{x_{i}, x_{i} \cdot x_{j}, \ldots, x_{i} \cdot \ldots \cdot x_{q}\}$ which appear on the right hand side of Eq. (2.1)

are called the arguments and are denoted by $\{m_{1},\ldots,m_{N}\}$ . The set of arguments is denoted by A. The set of arguments in the particular model y is called the structure of y.

For the sake of simplicity and without the loss of generality we now can assume that all models $y \in F$ have the following form: $^{2}$

$$
y = \sum_ {i = 1} ^ {N} \operatorname{coef} (m _ {i}) \cdot m _ {i}.\tag{2.2}
$$

Definition 2.2. Define the “complexity” $s = s(y)$ of the model $y \in F$ to be the number of the non-zero $^{3}$ coefficients in the model. In other words, “complexity” is the cardinality of the model’s structure, and clearly for any s such that $0 \leq s \leq N$ there exists a finite number of models of such complexity.

By definition all independent variables influence the outcome variable to some extent. As for their interactions – different products of the independent variables – experts may know that some of them are not correlated with the outcome variable because of the cause-effect relations in the system. Therefore, now the experts are asked to divide the set of arguments A in the following way:

$$
A = A _ {E} \cup A _ {P} \cup A _ {N},\tag{2.3}
$$

where by definition:

$A_{E}$ is the set of all arguments which, according to experts, essentially influence y;

$A_{P}$ is the set of all arguments which, according to experts, possibly influence y;

$A_{N}$ is the set of all arguments which, according to experts, almost do not influence y.

From now on, it is assumed that the set of arguments consists of the influential elements from $A_{E} \cup A_{P}$ .

Let $\zeta$ be an empirical quality criterion defined on the family of models $\mathcal{F}$ :

$$
\zeta \colon \mathcal {F} \rightarrow \mathrm{R} _ {+},\tag{2.4}
$$

where $R_{+}$ is the set of real non-negative numbers. We will assume that the lesser the value of the objective criterion $\zeta(y)$ the better the empirical quality of the model y. The well-known examples of $\zeta(y)$ are the criterion of regularity (GMDH), criteria based on the sum of squares of deviations (regression analysis), maximum of modulo of deviation (Chebyshev approximations), the mean risk (mean risk minimization method). Further the empirical quality of the model y will be called “the $\zeta$ -quality of y”. $^{4}$

Definition 2.3. Suppose given an algorithm of constructing empirical models, an objective criterion $\zeta$ , and a subfamily of models $\mathcal{S} \subseteq \mathcal{F}$ . The model $y_0 \in \mathcal{S} \subset \mathcal{F}$ is called “ $\zeta$ -best in $\mathcal{S}$ for the given algorithm and criterion” if

$$
\zeta (y _ {0}) = \min _ {y \in \mathcal {S}} \zeta (y)\tag{2.5}
$$

and is called “globally $\zeta$ -best for the given algorithm and criterion” when S=F. From now on we will refer to such models simply as “ $\zeta$ -best in S” and “globally $\zeta$ -best” respectively.

As it was mentioned above, the purpose of this research was to combine expert and empirical information while selecting the “best” model on $\mathcal{F}$ , in other words, to solve the problem of the two-criteria choice on $\mathcal{F}$ , where one criterion is objective (based on the empirical data) and the other one is subjective (based on expert judgement). When dealing with problems of multicriteria choice, it is convenient to use the language of binary relations. Recall that we defined the objective criterion $\zeta$ as a law which associates a non-negative number $\zeta(y)$ with any model $y\in\mathcal{F}$ , but in fact we can view $\zeta$ as a reflexive, transitive and linear binary relation $>\zeta$ on

$F^{2}$ which is called “empirically better” and is defined as follows:

$$
y _ {1} > _ {\zeta} y _ {2} \Leftrightarrow \zeta (y _ {1}) \leq \zeta (y _ {2}).\tag{2.6}
$$

Suppose now that $\zeta(y_{1})<\zeta(y_{2})$ but the actual difference $|\zeta(y_{1})-\zeta(y_{2})|$ is very small. Formally, $y_{1}$ is empirically better than $y_{2}$ , but from the viewpoint of the modeler these models are in fact “indistinguishable” by their objective quality. To reflect this phenomenon, let us introduce the number $\varepsilon=\varepsilon(\zeta)$ which is determined by experts and is a subject to the following property:

Definition 2.4. The models $y_1, y_2 \in \mathcal{F}$ are called "indistinguishable by their empirical quality" or simply "ζ-indistinguishable with barrier ε" if $|\zeta(y_1) - \zeta(y_2)| < \varepsilon(\zeta)$ . Such models will be denoted as $y_1 \sim_{\zeta} y_2$ .

In other words, we have just introduced the reflexive and symmetric binary relation $\sim_{\zeta}$ which establishes the relation of “expert indistinguishability” among some pairs of models from $\mathcal{F}^2$ . If $y_1$ and $y_2$ are not “indistinguishable by their empirical quality” the following notation will be used: $(y_1, y_2) \notin \sim_{\zeta}$ .

Remark. Let us make the following important convention: from now on, unless stated otherwise, the expression $y_1 >_{\zeta} y_2$ means “ $y_1$ is empirically better than $y_2$ and they are distinguishable: $(y_1, y_2) \notin \sim_{\zeta}$ .

## 3. Measures of consistency

In this paper, we are dealing with both expert and empirical estimation of the quality of models, i.e. with the problem of multicriteria choice of the “best” model. Note that the problem of choice in this particular context is rather unusual because of the following reasons. On the one hand, there exists an “objective” criterion which provides the natural basis for the comparison of any two models in $\mathcal{F}$ – an indicator of how well the models approximate or predict the empirical data. However, despite the clear definition of the “best” model (the one with the smallest value of $\zeta(y)$ , the meaningful notion of the “reference” (or “ideal”) model is missing and the properties of such model are unknown. On the contrary, all subjective (expert-related) criteria have the naturally embedded notions of the “reference” or “ideal” model (in this article such models will be called “ $\tau$ -best”), but subjective criteria are as a rule qualitative, and not all models are comparable via them. The notion of “consistency” and the corresponding “measures of consistency” which will be introduced in this section are driven to overcome this dilemma: they link objective and subjective criteria, allowing the simultaneous comparison of any two models to each other and to the reference model. Besides, they estimate the degree to which expert and empirical information agree while constructing the “best” model. The “measures of consistency” are defined as a special class of multivariate functions denoted as $\tau$ -functions.

Let $\tau(u_1, \ldots, u_k)$ be the differentiable function of $k$ variables subject to the following properties:

(1) Function $\tau(u_1, \ldots, u_k)$ is limited on $[0, 1]$ : $0 \leq u_1, \ldots, u_k \leq 1 \Rightarrow 0 \leq \tau(u_1, \ldots, u_k) \leq 1$ .

(2) On the boundaries $\tau(u_{1},\ldots,u_{k})$ behaves in the following way:

$$
\begin{array}{l} \tau (u _ {1}, \ldots , u _ {k}) = 0 \Leftrightarrow u _ {1} = \ldots = u _ {k} = 0, \\ \tau (u _ {1}, \ldots , u _ {k}) = 1 \Leftrightarrow u _ {1} = \ldots = u _ {k} = 1. \end{array}
$$

(3) Function $\tau(u_{1},\ldots,u_{k})$ is monotonously increasing in each variable:

$$
\begin{array}{r l} u _ {i} ^ {\prime} <   u _ {i} ^ {\prime \prime} \Rightarrow \tau (u _ {1}, \dots , u _ {i - 1}, u _ {i} ^ {\prime}, u _ {i + 1}, \dots , u _ {k}) \\ & <   \tau (u _ {1}, \dots , u _ {i - 1}, u _ {i} ^ {\prime \prime}, u _ {i + 1}, \dots , u _ {k}). \end{array}
$$

(4) In the case when $k \geq 2$ , the function $\tau(u_{1}, \ldots, u_{k})$ is stable under the antisymmetric variation in any pair of variables and $\forall\delta \forall i, j$ s.t. $1 \leq i < j \leq k$ :

$$
\begin{array}{r l} \tau \big (u _ {1}, \ldots , u _ {i - 1}, u _ {i} + \delta , u _ {i + 1}, \ldots , u _ {j - 1}, u _ {j} - \delta , u _ {j + 1}, \ldots , u _ {k} \big) \\ = \tau \big (u _ {1}, \ldots , u _ {i - 1}, u _ {i}, u _ {i + 1}, \ldots , u _ {j - 1}, u _ {j}, u _ {j + 1}, \ldots , u _ {k} \big). \end{array}
$$

Proposition 3.1. If a function $\tau(u_1, \ldots, u_k)$ is subject to (1)-(4) then

$$
\frac {\partial}{\partial u _ {i}} \tau > 0 \quad \forall i = \overline {{{1 , k}}}.\tag{a}
$$

$$
\tau \left(u _ {1}, \dots , u _ {k}\right) = \tau \left(u _ {1} + \dots + u _ {k}\right).
$$

$$
\tau (0) = 0; \tau (k) = 1.\tag{b}
$$

(c)

Proof.

(a) is an obvious consequence of the property (3).

(b) Induction on $k$ . Let $k = 2$ and $\tau$ be a function of two variables $u_{1} = u$ and $u_{2} = \nu$ . From property (4) we have that for any $\delta$ function $\tau(u + \delta, \nu - \delta) = \tau(u, \nu)$ . Let us subtract $\tau(u, \nu - \delta)$ from both sides of the equation, then for any $\delta$ the equality $\tau(u + \delta, \nu - \delta) - \tau(u, \nu - \delta) = \tau(u, \nu) - \tau(u, \nu - \delta)$ holds. Dividing both sides by $\delta$ and taking the limit when $\delta \to 0$ , yields

$$
\begin{array}{r l}\lim _ {\delta \rightarrow 0}&\frac {\tau (u + \delta , \nu - \delta) - \tau (u , \nu - \delta)}{\delta}\\&= \lim _ {\delta \rightarrow 0} \frac {\tau (u , \nu) - \tau (u , \nu - \delta)}{\delta}.\end{array}
$$

Since $\tau(u, \nu)$ is differentiable in both variables, it's equivalent to saying that $(\partial/\partial u)\tau = (\partial/\partial\nu)\tau$ . Solving this partial differential equation for $\tau$ , we obtain that $\tau(u, \nu) = \tau(u + \nu)$ . It is easy to see that induction is equivalent to the successive use of the above argument $k - 1$ times. Hence, $\tau(u_1, \ldots, u_k) = \tau(u_1 + \ldots + u_k)$ . Then (c) is a direct consequence of (b) and properties (1) and (2), hence, Proposition 3.1 is proved. From now on we will use the expressions "measure of consistency" and "τ-function" interchangeably.

Examples of $\tau$ -functions:

$$
\begin{array}{l} \tau (u, \nu) = \frac {u + \nu}{2}; \tau (u, \nu) = \left(\frac {u + \nu}{2}\right) ^ {k} \forall k > 0; \\ \tau (u, \nu) = \frac {u + \nu}{2 \cdot e ^ {2}} \cdot e ^ {u + \nu}. \end{array}
$$

It will be shown in the next sections how to use $\tau$ -functions to measure the degree of consistency of expert and empirical information for different types of expert knowledge and the variety of empirical methods, besides it will be proved that for the same type of expert knowledge, all $\tau$ -functions are equivalent in some sense. Now let us demonstrate the use of $\tau$ -functions in several abstract cases when we have two independent sources of information regarding the way to form subsets of a set S. In each of the following cases, we want to measure the consistency of the information which comes from two different sources.

Case 1. Suppose given two different subsets $D \subseteq S$ , $\mathcal{W} \subseteq S$ of the same cardinality. Then the function

$$
\tau = \tau \left(\frac {| D \cap \mathcal {W} |}{| D |}\right)\tag{3.1}
$$

is the measure of consistency in this case.

Case 2. Suppose given two partitions of S into the same number p of disjoint classes: (base) partition $\{A_{i}\}_{i=1}^{p}$ and partition $\{B_{i}\}_{i=1}^{p}$ , such that $S = \bigcup_{i=1}^{p} A_{i} = \bigcup_{i=1}^{p} B_{i}$ and $A_{i}$ corresponds to $B_{i}$ in some sense for all values of i. Then the function

$$
\tau = \tau \left(\frac {\left| A _ {1} \cap B _ {1} \right|}{\left| A _ {1} \right|}, \dots , \frac {\left| A _ {p} \cap B _ {p} \right|}{\left| A _ {p} \right|}\right)\tag{3.2}
$$

is the measure of consistency of the partitions $\{A_{i}\}$ and $\{B_{i}\}$ , it estimates the degree to which the partitions $\{A_{i}\}$ and $\{B_{i}\}$ agree.

Case 3. Suppose that one source of information asserts that there exists L pairs of subsets of $\mathcal{S}(\{(C_{i},D_{i})\}_{i=1}^{L})$ such that no subset $K\subseteq S$ should contain any elements from $C_{i}$ and $D_{i}$ simultaneously. If this rule is violated, the lesser the number of such elements the better. Suppose another source of information provides us with a set $K\subseteq S$ . Then the following $\tau$ -functions can be used:

$$
\begin{array}{l} \tau = \tau \left(\frac {1}{1 + \operatorname{card} (K \cap C _ {1}) \cdot \operatorname{card} (K \cap D _ {1})}, \dots , \right. \\ \left. \frac {1}{1 + \operatorname{card} (K \cap C _ {L}) \cdot \operatorname{card} (K \cap D _ {L})}\right). \end{array}\tag{3.3}
$$

General case. Suppose given a combination of several cases: a set S has a number of “independent” types of information. Let $\tau_{1},\ldots,\tau_{q}$ be the corresponding “individual” measures of consistency. Then the generalized measure can be formed – it merely is the direct product of the “individual” measures: $\tau=\tau_{1}\times\ldots\times\tau_{q}=(\tau_{1},\ldots,\tau_{q})$ . The comparison of such vectors is the standard problem of multicriteria choice [4]. In most cases, the problems of that kind can be resolved in one of the following ways:

(a) Assign the weight for each coordinate, then reduce to the problem of one-criterion choice.

(b) Introduce a partial order on the set of such vectors, permit the existence of “best” incomparable vectors.

## 3.1. Note on the necessity of a unified approach

The next sections deal with the concrete types of expert knowledge which can be incorporated into the various empirical methods. The choice of those types of knowledge is deliberate and reflects our goal to show that the framework can handle quite different types of expert knowledge from expert partitions of the arguments to the rankings of arguments. Besides, such framework allows the modeler to apply different methods of polynomial model construction and various types of expert knowledge to the same system. The fact that all the models were constructed within the same approach, provides a basis for a meaningful comparison of the results: the functions from the same class will measure the consistency of expert and empirical information and the subjective quality of models.

## 4. Expert information about the signs of coefficients

The knowledge about “positive” and “negative” influence of the arguments on the outcome variable depicts the nature of the dependency of the outcome variable on a single argument and does not take into account the interrelationships between the arguments. Therefore it is very natural and usually available for the experts who work with the system.

Example. Studying mortgage prepayments as a function of economic, sociological and financial factors, it was determined that the percentage changes in housing starts and foreclosure rates, measures of labor turnover, borrowing potential, and regional migration have a “positive” impact on prepayments, whereas national and regional unemployment levels have a “negative” effect. It remains to note that the signs of coefficients in the corresponding models were hypothesized before the actual modeling [8].

Definition 4.1. The argument $m_i$ is said to have a “positive” (“negative”) influence on the outcome variable y if with all other factors being fixed the increase (decrease) of the value of $m_{i}$ causes the function $y \equiv y(m_{i})$ (as a function of one variable) to behave in some sense likewise.

The definition above implies for any model $y \equiv y(m_i) \in \mathcal{F}$ that if $m_i$ has positive (negative) influence on y then the corresponding coefficient $\text{coef}(m_i)$ in Eq. (2.2) is positive (negative). Now, given the expert information about the signs of the coefficients and any model $y \in F$ , let us define the subjective (based on the expert information) quality of the model – an indicator of the extent to which the empirically built models agree to the resulting opinion of experts.

Definition 4.2. The empirically built model is called “entirely consistent in terms of signs of coefficients” if either the sign of every coefficient in the model coincides with that estimated by the experts or is not determined by them.

Notice that expert information about the signs of the coefficients can be represented as the partition of the set of arguments into three classes: those with “positive” influence $(A^{+})$ , those with “negative” influence $(A^{-})$ , and those with unknown influence $(A^{0})$ . On the other hand, any empirically built model also provides us with the partition of the set of arguments into three classes:

$B^{+}$ – arguments which are present in the model and have positive coefficients not equal to zero; $B^{-}$ – arguments which are present in the model and have negative coefficients not equal to zero; $B^{0}$ – arguments which are not present in the model or have coefficients equal to zero.

First, note that the classes $A^{0}$ and $B^{0}$ by definition do not give the basis for a meaningful comparison, but the remaining classes can tell us a lot about both the subjective quality of the models and the overall consistency of expert and empirical information. Secondly, the relationship between expert and empirical partitions of the arguments are exactly as those described in the previous section (Case 2), and therefore the above defined measures of consistency can be used as follows:

$$
\tau = \tau \left(\frac {\left| A ^ {+} \cap B ^ {+} \right|}{\left| A ^ {+} \right|}, \frac {\left| A ^ {-} \cap B ^ {-} \right|}{\left| A ^ {-} \right|}\right).
$$

Table 2  
Contingency of expert and empirical information

<table><tr><td></td><td>Expert (+)</td><td>Expert (−)</td><td>Not defined by experts</td></tr><tr><td>Empirical (+)</td><td>n(+,+)</td><td>n(+,-)</td><td>n(+,0)</td></tr><tr><td>Empirical (−)</td><td>n(−,+)</td><td>n(−,-)</td><td>n(−,0)</td></tr><tr><td>Not in the model</td><td>n(0,+ )</td><td>n(0,-)</td><td>n(0,0)</td></tr></table>

This function is an indicator of the model's subjective quality and the measure of consistency of expert judgement about the signs of the coefficients and empirical information.

Proposition 4.1. A model y is entirely consistent in terms of signs of coefficients if and only if $\tau((|A^{+} \cap B^{+}|/|A^{+}|), (|A^{-} \cap B^{-}|/|A^{-}|)) = 1$ . The proof follows directly from the definitions and properties of the measures of consistency.

## 4.1. Alternative approach (non-parametric statistics)

Consider a system with the expert information about the signs of coefficients, and a model y built without making use of the expert knowledge – some $\zeta$ -best model. In order to analyze the consistency of expert and empirical information in this case, Table 2 can be formed; where $\mu,\vartheta\in\{“+”,“-”\}$ and

\- $n(\mu, \vartheta)$ stands for the number of cases when the predetermined "expert" sign $\vartheta$ was estimated to be $\mu$ by the independent empirical procedure;

\- $n(0, \vartheta)$ stands for the number of cases when the argument with the predetermined expert sign of $\vartheta$ did not appear in the globally $\zeta$ -best model;

\- $n(\mu,0)$ stands for the number of cases when the argument with the unknown “expert” sign happened to have the “empirical” sign of $\mu$ in the globally $\zeta$ -best model;

\- $n(0,0)$ stands for the number of cases when the argument with no predetermined “expert” sign did not appear in the globally $\zeta$ -best model.

One can try to apply the non-parametric statistics in order to explore the probabilistic mechanism of the distribution in Table 2 and check various statistic hypotheses about the properties of the numbers with respect to each other. The theory of such methods is well developed, and a great number of publications is devoted to it [7]. This case will not be considered in detail in this article: as it was said above, the purpose here is to show the usefulness of the synthesis of expert and empirical information on the conceptual level. However, it is worth mentioning that there exists a great number of well-known measures which determine the presence of all kinds of dependences in such tables. They can serve as “alternative” measures of consistency in this case as opposed to the $\tau$ -functions, but in general, such methods cannot be used as a universal measure of consistency of expert and empirical information: as we will see in the following sections, they are unapplicable to the types of expert knowledge other than signs of coefficients.

There are several ways how to make use of the expert knowledge about the signs of coefficients. For instance, the stepwise regression with the expert restrictions on the signs of the coefficients can be performed, i.e. the algorithm can be forced to choose on each step the argument(s) (1) which mostly increases $\zeta$ -quality of the models, and (2) whose coefficient's sign coincides with that determined by the experts. The methods of the direct use of such expert knowledge will be more closely studied in Section 8. Clearly, the above-described use of expert knowledge in the algorithms based on stepwise regression won't increase the computational intensity while providing greater credibility of models.

## 5. Expert information about “connection” and “incongruity”

While the information about the signs of the coefficients deals with the expert judgement of the relationship between a single argument and the outcome variable, this section is devoted to a quite different type of expert knowledge – the information about the cause and effect relationships between the arguments with respect to the ways they influence the outcome variable.

## 5.1. Relation of connection ( $\Psi$ )

Suppose that for some pairs of arguments of a complex system the experts are able to determine that these arguments influence the outcome variable only simultaneously, i.e. if one of the arguments influences the outcome variable, then another one also influences the outcome variable, and vice versa.

Example. If the productivity of an ecosystem is to be modeled, then the argument “biomass of a predator” should be present in any model together with the argument “biomass of the corresponding prey”, and vice versa.

It appears that using just this information about the pairwise interconnections between the arguments, one can produce a partition of the set of arguments and introduce the notion of the “best” in terms of these connections model.

Define on the set $A \times A$ the binary relation “connection” $\Psi \subseteq A \times A$ which means that the two arguments can influence the outcome variable when both are present.

Definition 5.1. The arguments $m_1$ and $m_2$ are said to be “connected” from the viewpoint of experts $-(m_1, m_2) \in \Psi$ – if in any model of the form in Eq. (2.2)

$$
\operatorname{coef} (m _ {1}) \neq 0 \text {   if   and   only   if   } \operatorname{coef} (m _ {2}) \neq 0.\tag{5.1}
$$

Remark. It is not required that all the arguments in A are comparable in terms of $\Psi$ . Thus the set of arguments with partition into the two subsets: set $A_{\Psi}$ of $\Psi$ -comparable arguments and the set $A - A_{\Psi}$ of arguments which are not $\Psi$ -comparable.

Proposition 5.1. On the set $A_{\Psi}$ the binary relation $\Psi$ is the equivalency relation.

Clearly, the above introduced binary relation is reflexive, symmetric and transitive.

Corollary 5.1. The set $A_{\Psi}$ is the disjoint union of the “connection” equivalency classes: $A_{\Psi} \cup_{i=1}^{q} A_{\Psi;i}$ , where $A_{\Psi;i}$ is the ith equivalency class and $q$ is the number of such classes.

## 5.2. Relation of incongruity (T)

Suppose that for some pairs of arguments of complex systems the experts are able to determine that these arguments can not influence the outcome variable simultaneously, i.e. if one of them influences the outcome variable, the other one does not, and vice versa.

Example. Modeling the dependency of morbidity of the population upon the quality of drinking water, one has to make sure that the arguments “concentration of chlorine” and “concentration of phenol” are not present in any model simultaneously: chlorine reacts with phenol creating the new argument – chlorine-phenol.

Definition 5.2. The arguments $m_1$ and $m_2$ are said to be “incongruent” from the viewpoint of experts $- (m_1, m_2) \in T \subseteq A \times A$ – if for any model of the form in Eq. (2.2) both of the following two conditions are satisfied:

$$
\text { if } \operatorname{coef} (m _ {1}) \neq 0 \text { then } \operatorname{coef} (m _ {2}) = 0,\tag{5.2}
$$

$$
\text { if } \operatorname{coef} (m _ {2}) \neq 0 \text { then } \operatorname{coef} (m _ {1}) = 0.\tag{5.3}
$$

It remains to note that $T \subseteq A \times A$ is a non-reflexive, symmetric, and non-transitive binary relation.

The following important properties of the newly introduced binary relations “connection” and “incongruity” are stated below.

Proposition 5.2. Let $A_{\Psi;g} = \{m_{g;1}, \ldots, m_{g;k}\}$ be a $\Psi$ -equivalency class and $m \in A$ be an argument outside $A_{\Psi;g}$ . If $m$ is incongruent to some $m_{g;i_0} \in A_{\Psi;g}$ , then $m$ is “incongruent” to any element in $A_{\Psi;g}$ , i.e.

$$
\begin{array}{r l} & m \in A - A _ {\Psi : g}, \exists m _ {g; i _ {0}} \in A _ {\Psi : g} \text {   s.t.   } (m, m _ {g; i _ {0}}) \in T \\ & \Rightarrow (m, m _ {g; i}) \in T \forall i = \overline {{1 , k}}. \end{array} \tag {5.4}
$$

Proposition 5.3. If $A_{\Psi;g} = \{m_{g;l}, \ldots, m_{g;k}\}$ and $A_{\Psi;h} = \{m_{h;l}, \ldots, m_{h;l}\}$ are the equivalency classes in $A_{\Psi}$ , and some element of $A_{\Psi;g}$ is incongruent to some element of $A_{\Psi;h}$ then any element of $A_{\Psi;g}$ is incongruent to any element of $A_{\Psi;h}$ , in other words

$$
\begin{array}{r l} & {\exists m _ {g: i _ {0}} \in A _ {\psi : g}, m _ {h: j _ {0}} \in A _ {\psi : h} \text {   s.t.   } (m _ {g: i _ {0}}, m _ {h: j _ {0}}) \in T} \\ & {\quad \Rightarrow (m _ {g: i}, m _ {h: j}) \in T \forall (i, j)} \\ & {\qquad \in \{1, \dots , k \} \times \{1, \dots , l \}.} \end{array} \tag {5.5}
$$

Both proofs follow directly from Definitions 5.1–5.2 and Proposition 5.1.

Let us forget about the formal results and notations for a second and describe the essence of the results. It has just been shown that for complex systems (for which the experts can identify the relationships of “connection” and “incongruity” among the arguments) it’s possible to break up the set of arguments into the set of equivalency classes and single incomparable elements, and establish the relation of “incongruity”. Moreover, the equivalency classes inherit the “incongruity” from their elements. To incorporate this information into modeling, one can start, for instance, with the estimation of the “best” model’s structure and consider the equivalency classes instead of the arguments from $A_{\psi}$ , and use various methods of modeling on the set of these classes paying special attention to the condition that no “incongruent” arguments (or classes) are present in the models simultaneously. It is obvious that the computational efficiency at least doesn’t increase because in the algorithms we consider classes instead of single arguments.

Definition 5.3. The model y is called “entirely consistent in terms of connection-incongruity” if any argument is present in y together with its “connection” equivalency class, and there are no incongruent elements or classes in the model.

Note that on the set of arguments, there are defined two types of information: classes of “connection” and the relation of “incongruity”. However, a close look at the properties of these binary relations enables one to identify them precisely as those described in the course of the discussion of the measures of consistency in Section 3. Thus if $\{A_{\Psi;i}\}_{i=1}^{q}$ are the connection $(\Psi)$ equivalency classes, and $M(y)$ stands for the structure of the model, then (Case 2)

$$
\tau_ {\Psi} = \tau \left(\frac {| A _ {\Psi ; 1} \cap M (y) |}{| A _ {\Psi ; 1} |}, \dots , \frac {| A _ {\Psi ; q} \cap M (y) |}{| A _ {\Psi ; q} |}\right).\tag{5.6}
$$

If $\{(C_i, D_i)\}_{i=1}^L$ are the incongruent classes, the measure of consistency corresponding to the relation of incongruity $T$ can be defined as follows (Case 3):

$$
\begin{array}{l} \tau_ {T} = \tau \left(\frac {1}{1 + \operatorname{card} (M (y) \cap C _ {1}) \cdot \operatorname{card} (M (y) \cap D _ {1})}, \dots , \right. \\ \left. \frac {1}{1 + \operatorname{card} (M (y) \cap C _ {L}) \cdot \operatorname{card} (M (y) \cap D _ {L})}\right). \end{array}\tag{5.7}
$$

The generalized measure of consistency for “connection-incongruity” is:

$$
\tau_ {(\Psi , T)} = \left(\tau_ {\Psi}, \tau_ {T}\right),\tag{5.8}
$$

where $(\tau_{\Psi},\tau_{T})$ stands for the cartesian product of the individual measures.

Proposition 5.4. The model y is consistent in terms of “connection-incongruity” if and only if $\tau_{(\Psi,T)}(y)=(1,1)$ . The straightforward proof is omitted.

Finally, while selecting the “best” model’s structure, two “independent” quality criteria are defined on the set of arguments: “objective” (based on the empirical data) quality criterion $\zeta$ and “subjective” (based on the expert knowledge) quality criterion $\tau$ . The way to use these two criteria in selection of the “best” model structure depends entirely on the qualities of the system to be modeled and on our confidence in the reliability of both expert and empirical information. If we do know for sure that expert information is reliable, and experts do know well the “cause and effect” relations in the system, then we will give the priority to expert information as follows: consider all possible combinations of equivalency classes and incomparable elements under the condition that there are no “incongruent” elements or classes. By definition, all models with such structures would be $\tau$ -best. Now choose from this collection of models the one with the minimal value of the objective criteria. Such models could be called $\zeta-\tau$ -best (we used $\tau$ first, and then $\zeta$ ). Such models – those which give priority to expert information – can be used only in situations when one considers expert information reliable. In situations when the expert information can be used but still priority is given to the empirical information, one can take the $\zeta$ -best models and estimate their $\tau$ -quality. Then we can try to increase the $\tau$ -quality of the model by adding to the model the most influential elements from each “connection” equivalency class whose representatives are present in the model, and eliminating the incongruent elements and classes while trying not to decrease substantially the empirical quality of the model.

## 6. Expert ranking of arguments' influence

In certain cases, the experts are able to provide us with the pairwise comparison of the arguments by their influence on the outcome variable, i.e. to say which argument in each pair is “more influential”.

Example. Financial experts agree that the spread between the homeowner's mortgage rate and the prevailing mortgage origination rate is a more influential (or powerful) factor that affects mortgage prepayments than, say, regional unemployment rates or housing prices [10].

If some rational restrictions on the expert comparisons are made [5], it is possible to introduce the effective methods of incorporating this type of expert information into the empirical models. Suppose that the experts are able to compare all the arguments by their influence on the outcome variable, and hence define the reflexive, and transitive and linear binary relation ( $>_{\tau}$ ) called “more influential on the outcome variable”. Let the series below represent the resulting ranking of the arguments by the group of experts:

$$
m _ {1} > _ {\tau} m _ {2} > _ {\tau} \dots > _ {\tau} m _ {N},\tag{6.1}
$$

where $m_{1}$ stands for the “most influential” argument and $m_{N}$ for the “least influential”.

Given the nature of this type of expert information, it is logical to conclude that the “best”, according to experts, model will be the one that contains the most influential elements.

Definition 6.1. The model y of the complexity s ( $0 \leq s \leq N$ ) is called “entirely consistent in terms of the expert ranking of the arguments” if it contains the first s elements of the series in Eq. (6.1).

So far we have been dealing with expert partitions of the set of arguments into a finite number of disjoint classes. Expert ranking of the arguments is a good example of the simplest type of $\tau$ -functions introduced in Section 3. Thus, since each $\zeta$ -best empirical model also provides a set [of arguments] of some cardinality $1 \leq s \leq N$ , one can use the measures of consistency to check to what degree the structure of the empirically built model matches the set of the most influential arguments of the same cardinality.

Definition 6.2. For any model $y = \operatorname{coef}(m_{i_1})m_{i_1} + \ldots + \operatorname{coef}(m_{i_s})m_{i_s}$ of complexity $s$ let's define the $\tau$ -quality as follows:

$$
\tau = \tau \left(\frac {\left| \left\{m _ {1} , \dots , m _ {s} \right\} \cap \left\{m _ {i _ {1}} , \dots , m _ {i _ {s}} \right\} \right|}{s}\right).\tag{6.2}
$$

Proposition 6.1. The model is entirely consistent in terms of the expert ranking of the arguments if and only if $\tau(y) = 1$ .

Again, if the priority is given to the expert information, then for each value of complexity one can construct all $\tau$ -best models, and then choose among them the model with the minimal value of $\zeta$ , i.e. the $\zeta-\tau$ -best model. Expert information in the form of ranking of the arguments (Eq. (6.1)) can be successfully used in the algorithms of stepwise regression where the empirical quality of the model depends on the arguments which are included in the model on every step. If expert information is considered to be reliable, then the computational time of selection of the best model will substantially decrease: on every step, instead of estimation of the empirical quality of the model obtained by adding/subtracting the arguments, one can simply add the most influential arguments.

## 7. Expert indistinguishability

## 7.1. GMDH algorithms and criteria

This section will use the specific features of GMDH-type algorithms and criteria [13]; that is why it will be useful to briefly summarize them.

The difference between GMDH and other methods of polynomial modeling lies in using the “external” quality criteria: estimation of the regression coefficients and evaluation of the [objective] quality are performed using independent (disjoint) sets of empirical observations. Briefly speaking, a typical GMDH algorithm consists of the following steps:

1. The observations in Table 1 are being partitioned into two disjoint sets - training (approximately $70\%$ of observations) and checking $(30\%)$ .

2. For each value of complexity $s$ ( $1 \leq s \leq N$ ) all possible models of such complexity are being

GMDH: Dependency $\zeta = \zeta(s)$ for $\zeta$ -best models.

![](/api/attachments/TY6ECYXE/fulltext/images/409a7e82dd7befc3baf0db0172e49fa47d1cfd51df64699a5b64c2e38849bcfa.jpg)  
Fig. 1. GMDH: Dependency $\zeta = \zeta(s)$ for $\zeta$ -best models.

built using the training set to estimate the regression coefficients.

3. The objective $(\zeta)$ quality of all models of the same complexity $s$ is being evaluated using the checking set, and for each $s$ the model with least value of $\zeta(y) - \zeta$ -best model of complexity $s$ is being selected.

4. Majority of the GMDH algorithms are iterative. One of their greatest assets is as follows: the structure and functional form of the models are not defined a priory by the modeler at the beginning, but determined by the algorithm in the course of modeling.

Once the $\zeta$ -best models of all complexities s = 1, N are built, the dependency $\zeta = \zeta(s)$ for $\zeta$ -best models can be discussed. The major empirical result of GMDH asserts that the function $\zeta = \zeta(s)$ [for $\zeta$ -best models] is of the form as shown in Fig. 1.

Definition 7.1. The value $s_{0}$ of complexity where the function $\zeta = \zeta(s)$ has its minimum is called the optimal complexity while the $\zeta$ -best model of the optimal complexity is called the best GMDH model.

## 7.2. Expert indistinguishability.

Given a ranking of the arguments by their “power of influence” $>_{\tau}$ on the outcome variable. Suppose (analogous to the discussion of the empirical quality criteria) that in the ranking of arguments (Eq. (6.1)) the experts can not distinguish the influence of some arguments considering them “close” or “equal” in influence on the outcome variable. Then on the sets $A^{2}$ (pairs of arguments) and $F^{2}$ (pairs of models) the similar constructions are defined: the ranking plus the notions of expert indistinguishability. This section will be devoted to the analysis of this interesting case.

Define on the set $A^2$ the binary relation of “expert indistinguishability of the arguments” $\sim_{\tau} \subseteq A^2$ subject for the following property: $m_1 \sim_{\tau} m_2$ if and only if the powers of influence of $m_1$ and $m_2$ on $y$ are very close. If $m_1$ and $m_2$ are not “indistinguishable by their power of influence” then write $(m_1, m_2) \notin \sim_{\tau}$ .

Remark. Similarly to the case of models, the following important convention will be used: $m >_{\tau} m_2$ will stand for the following two conditions: $m_1$ is "stronger" than $m_2$ in a sense of $>_{\tau}$ and $(m_1, m_2) \notin \sim_{\tau}$ .

The information about the indistinguishability in conjunction with the ranking of the arguments by their power of influence contains very powerful information about the system. That's why in this case we can introduce more sophisticated measures of the consistency of expert and empirical information.

Consider the binary relation $\Omega \subseteq \mathcal{F} \times \mathcal{F}$ of all the pairs of models the structures of which differ by only one argument:

$$
\begin{array}{l} \Omega = \left\{\left(y, w\right) \mid y = \sum_ {i = 1} ^ {s - 1} \operatorname{coef} \left(m _ {k _ {i}}\right) m _ {k _ {i}} + \operatorname{coef} \left(m _ {y}\right) m _ {y}; \right. \\ \left. w = \sum_ {i = 1} ^ {s - 1} \operatorname{coef} \left(m _ {k _ {i}}\right) m _ {k _ {i}} + \operatorname{coef} \left(m _ {w}\right) m _ {w} \right\}, \end{array}\tag{7.1}
$$

where $m_y$ and $m_w$ are the $s$ th argument of the models $y$ and $w$ respectively.

The notion of consistency in this case which is introduced below is based on the following two conditions. Thus, given the notions of indistinguishability of both models and arguments in addition to the ranking of arguments by their influence, we will say that expert and empirical information are consistent if for a sufficiently large percentage of the models from $\Omega$ the two natural conditions hold: (a)

if the two arguments are close enough from the viewpoint of experts then the models should be close enough by their empirical quality, and (b) if the arguments are essentially different from the viewpoint of experts then the corresponding models should be essentially different by the empirical quality, while the dependency is monotonous.

Definition 7.2. The expert information represented as $(>_{\tau}, \sim_{\tau})$ and the empirical information contained in Table 1 together with the pair $(>_{\zeta}, \sim_{\zeta})$ are called consistent with certainty $p = \nu / \eta$ , $(\eta \gg 1)$ if for the $\nu$ from $\eta$ randomly checked pairs of models $(y, w) \in \Omega$ the two following conditions hold:

Condition 7.1. (Quasi-continuity of $\sim_{\zeta}$ upon $\sim_{\tau}$ .) If the arguments, which the models $y$ and $w$ differ by, are indistinguishable then the models themselves should be indistinguishable. In other words:

$$
(y, w) \in \Omega , m _ {y} \sim_ {\tau} m _ {w} \Rightarrow y \sim_ {\zeta} w.\tag{7.2}
$$

Condition 7.2. (Monotonicity of $>_{\zeta}$ upon $>_{\tau}$ .) If $m_y$ is $\tau$ -better than $m_w$ then $y$ is $\zeta$ -better than $w$ :

$$
(y, w) \in \Omega , m _ {y} > _ {\tau} m _ {w} \Rightarrow y > _ {\zeta} w.\tag{7.3}
$$

It is possible to extend Conditions 7.1 and 7.2 for the case when the complexities of the models differ by 1. In order to do that, it suffices to remark the following: if an argument is correlated with the outcome variable very weakly, then the influence of this argument will be indistinguishable with $0 (m_{w} \sim_{\tau} 0)$ . Therefore Conditions 7.1 and 7.2 can be extended as follows:

Condition 7.1a. If the argument m has indistinguishably small influence on the outcome variable then its inclusion to or exclusion from any model y won't noticeable change its $\zeta$ -quality:

$$
m \sim_ {\tau} 0 \Rightarrow y \sim_ {\zeta} (y \pm m),\tag{7.4}
$$

where $y \pm m$ stands for inclusion/exclusion of m to/from y.

Condition 7.2a. If the complexity s of the model y is less (greater) than “optimal” complexity $s_{0}$ then inclusion/exclusion to/from the model of the argument essentially more influential than zero will essentially increase (decrease) the $\zeta$ -quality of the model:

$$
s <   s _ {0}; m > _ {\tau} 0 \Rightarrow (y + m) > _ {\zeta} y,\tag{7.5}
$$

$$
s > s _ {0}; m > _ {\tau} 0 \Rightarrow y > _ {\zeta} (y + m).\tag{7.6}
$$

For expert indistinguishability, one could as well use the measure given by Eq. (6.2), but it would not be as elaborate in this case as “certainty” p. Besides, as we will see later, “certainty” p enables us to have a closer look at the relationship between subjective and objective criteria.

Proposition 7.1. If expert and empirical information are consistent with the certainty p, and all the arguments are distinguishable by their power of influence then with the certainty p for any complexity the $\tau$ -best model is $\zeta$ -best.

Proof. Consider the $\tau$ -best (in a sense of Section 6) model of the arbitrary complexity $s$ . Via Eq. (7.2) with certainty $p$ it consists of the first $s$ elements of the series in Eq. (6.1). To prove the statement it suffices to notice that for inclusion to/exclusion from the model any of the arguments as well as the substitution for less influential arguments will “essentially” impair the $\zeta$ -quality of the model, and that means that with the certainty $p$ the $\tau$ -best model of any complexity is $\zeta$ -better than any other model of the same complexity, therefore, it is $\zeta$ -best. $\square$

Recall that for the GMDH-type quality criterion there exists a correlation between the quality of the model and its complexity, and the dependency is of the form as shown in Fig. 1.

Corollary 7.1. Under the conditions of Proposition 7.1 with certainty p the graph of the curve $\tau = \tau(s)$ has the same shape as that of the function $\zeta = \zeta(s)$ , i.e. the graph $\zeta = \zeta(s)$ for $\tau$ -best models is the same as the graph $\zeta = \zeta(s)$ for $\zeta$ -best models.

Proposition 7.2. Consider a ranking (Eq. (6.1)). Then for a given value of complexity $s$

(a) if $m_s \sim_{\tau} m_{s+1}$ then with certainty $p$ the $\tau$ -best model of the complexity $s$ is $\zeta$ -indistinguishable with the $\zeta$ -best model of the same complexity;

GMDH function $\zeta = \zeta(s)$ for $\tau$ -best models.

![](/api/attachments/TY6ECYXE/fulltext/images/cb08135d6d3565f3d373d920ecbddc1ddafe48ac460cf4aa355e18c5e8063d8e.jpg)  
Fig. 2. GMDH function $\zeta = \zeta(s)$ for $\tau$ -best models.

(b) if $(m_s, m_{s+1}) \notin \sim_{\tau}$ then with certainty $p$ the $\tau$ -best model of complexity $s$ is $\zeta$ -best. (Proof is similar to that of Proposition 7.1.)

Corollary 7.2. The domain of the function $\tau = \tau(s)$ consists of the intervals of the following types:

Type I. Corresponding arguments are indistinguishable and, hence, $\tau$ -best models are indistinguishable by the objective quality with the $\zeta$ -best models.

Type II. Corresponding arguments are essentially different and, according to Proposition 7.2, the $\tau$ -best models of such complexities are $\zeta$ -best.

The graph of the function $\zeta = \zeta(s)$ for $\tau$ -best models is shown in Fig. 2, where $s_0$ is the optimal complexity and $\varepsilon$ is the barrier of indistinguishability of the empirical quality of models. In fact, while it is easy to find the minimum of such a function, it is important to know that the $\tau$ -best model $y_0$ corresponding to minimum of the function $\zeta = \zeta(s)$ is not the only $\zeta - \tau$ -best model we can get: all the models indistinguishable with $y_0$ in terms $\sim_{\zeta}$ of will also be the “best”.

Definition 7.3. Let $y_0$ be the $\zeta - \tau$ -best model and $\zeta_0 = \zeta(y_0)$ . The set of all $\tau$ -best models which are indistinguishable with $y_0$ in terms of $\sim_{\zeta}$ is called the set of the $\zeta - \tau$ -best models or simply “best” models.

One of the essential features of the GMDH algorithms is the existence of the unique “best” model. We have just shown that if GMDH is combined with the use of expert knowledge, there appears the necessity to generalize the GMDH notion of the “best” model and introduce the whole class of “best” models indistinguishable by their empirical quality.

## 8. Modeling and decision making

As it was mentioned earlier, the problem of choosing the “best” model in the family F is basically the problem of the two-criteria – subjective $\tau$ and objective $\zeta$ – choice on F, while the concrete methods and algorithms absorbing both types of knowledge and the decision-making pattern of the modeler are determined on each iteration of modeling by at least two circumstances:

\- the level of confidence in reliability of expert knowledge and the quality of empirical information; $^{5}$

\- the level of consistency of expert and empirical information.

There are two major types of discrete models of multicriteria choice: successive and parallel [4], while the use of a particular scheme is a function of confidence and consistency.

Definition 8.1. (Successive $\zeta-\tau$ -scheme of choice.) A $\zeta-\tau$ -scheme is a two-step procedure: first, the expert criteria $\tau$ is used to choose a subfamily $\mathcal{M}$ of models which are the $\tau$ -best or have sufficient $\tau$ -quality; then the objective criteria $\zeta$ is applied to select all $\zeta$ -best model(s) in $\mathcal{M}$ and all the models which are indistinguishable with $\zeta$ -best model(s) by their objective quality.

Example. Suppose given the expert information about both the signs of coefficients and the ranking of the arguments; the confidence in the expert information is high while the empirical data is believed to be sporadic or uncharacteristic. The possible solution in this case can be to select the models which are or have sufficiently high $\tau$ -quality in both “ranking of the arguments” and “connection-incongruity” sense and then to estimate their $\zeta$ -quality choosing all the $\zeta$ -best models.

Definition 8.2. (Successive $\tau-\zeta$ -scheme of choice.) A $\tau-\zeta$ -scheme is a two-step procedure: first, all the models which are indistinguishable with the $\zeta$ -best model(s) are being selected, then the expert criteria $\tau$ is used to choose among them the models which have the highest or merely sufficient $\tau$ -quality.

Definition 8.3. (Parallel $(\tau, \zeta)$ -scheme of choice.) A $(\tau, \zeta)$ -scheme is a model of choice where selection of the best model is performed by using both criteria simultaneously.

Example. Suppose we have the expert information about “connection-incongruity”, but we are not confident in its reliability. Then one of the possible solutions can be the stepwise regression with expert-based restrictions on the structures of models on each step.

It is important to note that, according to Section 3, for any type of expert knowledge there exists an infinite number of different $\tau$ -functions, but the rule of how to choose the one to use was never formulated. With this issue deals the following proposition.

Proposition 8.1. All $\tau$ -functions are equivalent in the following sense: with the algorithm of constructing the empirical models, objective criterion and type of expert knowledge being fixed, the transition from one $\tau$ -function to another preserves the original ranking of the models by their “expert” ( $\tau$ ) quality.

Proof. Consider the two models $y$ and $w$ from $\mathcal{F}$ built using the same expert and empirical information, and suppose that $y$ is $\tau$ -better than $w$ . In other words, the following inequality holds: $\tau(u_{1:y},\ldots ,u_{k:y}) > \tau(u_{1:w},\ldots ,u_{k:w})$ where $u_{i:y}$ and $u_{i:w}$ are the values of the $\tau$ -function's arguments corresponding to the estimates of the consistency of expert and empirical information for this particular type of expert knowledge. Via Proposition 3.1, we have $\tau(u_{1:y} + \ldots +u_{k:y}) > \tau(u_{1:w} + \ldots +u_{k:w})$ .

That, because of the strict monotonicity of, $\tau$ implies $u_{1:y} + \ldots + u_{k:y} > u_{1:w} + \ldots + u_{k:w}$ . Consider now another $\tau$ -function $\bar{\tau}$ and let's use it to compare the expert quality of the models $y$ and $w$ . Since $\bar{\tau}$ is also monotonous, it follows that $\bar{\tau}(u_{1:y} + \ldots + u_{k:y}) > \bar{\tau}(u_{1:w} + \ldots + u_{k:w})$ and finally, $\bar{\tau}(u_{1:y}, \ldots, u_{k:y}) > \bar{\tau}(u_{1:w}, \ldots, u_{k:w})$ , i.e. $y$ is $\bar{\tau}$ -better than $w$ . So in any scheme of choice the result does not depend on the pick of a particular $\tau$ -function.

The methods of synthesis of expert and empirical information involve the following elements: empirical data, objective criteria and the algorithm of constructing the empirical models, expert knowledge, procedures of incorporating expert judgement into the models, and the priorities of the modeler. Therefore in the case when the modeler is not satisfied with the quality of the constructed model, the algorithm should involve a multi-stage improvement of the following elements:

\- empirical data (additional observations, testing of the outliers, bootstrap, etc.);

\- algorithm (application of different methods, objective criteria, and more sensitive diagnostics of the models, use of the new classes of models, etc.);

\- expert judgement (revision of the sets of independent variables and arguments, change of the group of experts, etc.);

\- procedures (switch between, $(\tau, \zeta)$ -, $\zeta - \tau$ )- and $\tau - \zeta$ )-schemes, simultaneous use of several different types of expert and empirical information);

\- priorities (revision of levels of confidence in expert and empirical information).

The analysis of the possible actions of the modeler is presented in Fig. 3. It is easy to see that all the results of the article can be generalized for time series data, and the case when there exist several objective and several subjective criteria.

## 9. Conclusion

The article deals with the problems of the direct use of expert information in multivariate polynomial modeling of complex systems. The concepts of the “subjective quality of the model”, “best model”, and “consistency of expert and empirical information” as well as its quantitative measures were introduced and studied while the well-known GMDH notion of the “best complexity” was generalized. The paper contains a detailed analysis of such types of expert information as signs of coefficients, classes of “connection-incongruity”, ranking of the arguments by influence, expert indistinguishability. It was shown how a unified approach to the use of expert knowledge can increase the quality and reliability of modeling. The main results of the paper can be easily generalized for the case of different types of expert knowledge and existence of several objective and subjective criteria. The main purpose of the research was to combine two different types of knowledge – expert and empirical – in order to build models best reflecting on macro level the functioning mechanism of the given system.

Synthesis of Expert and Empirical Information: Actions of the Modeler.  
![](/api/attachments/TY6ECYXE/fulltext/images/c3c90669c296fd45e156b321bc3417adfd3684b8a8d4e82352f989685dbe486d.jpg)  
Fig. 3. Synthesis of expert and empirical information: Actions of the modeler.

## References

[1] F. Bolder, G. Wright, Assessing the quality of expert judgement, Decision Support Systems, No. 11 (1994).

[2] P.M. Brusilovskiy and L.M. Tilman, The Construction of Polynomial Models for Complex Systems: Synthesis of Expert and Empirical Information (BSU and UAI Press, Ufa, 1992).

[3] P.M. Brusilovskiy, L.M. Ivanova and L.M. Tilman, An Approach to the Development of Expert Systems in Problems of Bio-Assessment, in: Bio-Assessment: Theory, Methods, Applications (Russian Academy of Sciences, Toljatti, 1994).

[4] D.W. Bunn, Applied Decision Analysis (McGraw-Hill Book Co., NY, 1984).

[5] G. Colson, B. Mareschal, JUDGES: A Descriptive Group Decision Support System For The Ranking of Items, Decision Support Systems, No. 12 (1994).

[6] N.R. Draper and H. Smith, Applied Regression Analysis (John Wiley and Sons, NY, 1983).

[7] J.L. Fleiss, Statistical Methods for Rates and Proportions (John Wiley and Sons, NY, 1981).

[8] A.J. Heuson, Prepayment Expectations and the Pricing of GNMA Pass-Through Securities, Housing Finance Review, No. 4 (Winter 1987).

[9] A.P. Korostelev, Minimax Theory of Image Reconstruction (Springer-Verlag, NY, 1993).

[10] N.T. Milonas, Prepayment Option in the GNMA-Treasury Bond Spread, Housing Finance Review, No. 4 (1987).

[11] F. Mosteller and J.W. Tukey, Data Analysis and Regression (Addison-Wesley, Reading, 1981).

[12] G. Numberger, Approximation by Spline Functions (Springer-Verlag, NY, 1989).

[13] S.J. Farlow, Self-Organizing Methods in Modeling: GMDH-Type Algorithms (M. Dekker, NY, 1984).

[14] V.N. Vapnik, Estimation of Dependences Based on Empirical Data (Springer-Verlag, NY, 1982).

![](/api/attachments/TY6ECYXE/fulltext/images/9616733e918af958b7907810ffa150adaaf72b4f15c41356b6e28f16eb29f9b3.jpg)

Pavel M. Brusilovskiy is Risk Management Analyst at Conrail Corp. and a Research Associate at the Academy of Natural Sciences of Philadelphia. For many years, he served as a full professor of Applied Statistics and Modeling at Engineering University, Ufa, Russia. Dr. Brusilovskiy holds a Ph.D. in Applied Statistics, decision making and Modeling from the Academy of Sciences of Russia (1978) and has an M.S. in Mathematics. He is the author of two books

and more than fifty articles on applied statistics, decision making and modeling.

![](/api/attachments/TY6ECYXE/fulltext/images/9032c796ce4dbab5166f9655ce1c154e980228609624d3748dcf221faf2642e0.jpg)

Leo M. Tilman is a Risk Management Analyst at BlackRock Financial Management, Inc. in New York City, where he is dealing with analysis and modeling of complex systems in finance. He holds his cum laude B.A. in Mathematics from Columbia University and is currently pursuing his graduate degree in Statistics at Columbia. Mr. Tilman has a number of publications on mathematical modeling and expert systems. Several of his works were presented at the interna-

tional conferences on modeling and decision making.
