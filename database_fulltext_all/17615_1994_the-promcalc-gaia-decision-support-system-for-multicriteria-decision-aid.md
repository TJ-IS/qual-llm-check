---
otero_id: 17615
otero_key: "JVSDXATB"
title: "The PROMCALC & GAIA decision support system for multicriteria decision aid"
authors: "Jean-Pierre Brans; Bertrand Mareschal"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90048-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The PROMCALC & GAIA decision support system for multicriteria decision aid

Jean-Pierre Brans $^{a}$ and Bertrand Mareschal $^{b}$

$^{a}$ Vrije Universiteit Brussel, C.S.O.O., Pleinlaan, 2,

B-1050 Brussel, Belgium

$^{b}$ Université Libre de Bruxelles, Institut de Statistique, Boulevard du Triomphe-CP 210, B-1050 Bruxelles, Belgium

PROMCALC & GAIA is the last development of the interactive decision support system based on the PROMETHEE and GAIA methodology. In the first section, the fundamental characteristics of multicriteria problems are recalled and requisites are formulated for an appropriate multicriteria decision aid methodology. Based on these requisites, the PROMETHEE methods are then introduced, including newer developments such as PROMETHEE V (multicriteria optimization under constraints) and the GAIA visual modelling method. The actual implementation of the proposed methodology in the PROMCALC & GAIA software is then detailed and a numerical example is developed to illustrate the possibilities of the system.

Keywords: Multicriteria decision aid; Outranking; PROMETHEE; GAIA; PROMCALC

![](/api/attachments/JVSDXATB/fulltext/images/abcaf0d12588842b0d5ef7459be618bda327c7642f7e3bb109955b99de8c2a5e.jpg)

Jean-Pierre Brans received his Ph.D. in Mathematics in 1966. Since 1966 he has been Professor of Statistics, Operations Research and Computer Science at the V.U.B. and U.L.B. universities of Brussels. He was the organiser and Chairman of EURO I, the first European conference on O.R., in Brussels, 1975, and Chairman of the Programme Committee of the EURO IV Conference in Cambridge, England, 1981. Prof. Brans was President of EURO, the Euro-

pean Association of O.R. Societies, in 1983–84 and Vice-President of IFORS, the International Federation of O.R. Societies, in 1977–80 and 1989–92. He was the organisor and Chairman of IFORS-SPC1, the first specialised conference organised by IFORS, theme Decision Support Systems, in Bruges, 1991. He was awarded the “EURO Gold Medal” in 1994.

Correspondence to: J.-P. Brans, Vrije Universiteit Brussel, CSOO, Pleinlaan 2, B-1050 Brussel, Belgium.

## 1. Introduction

This paper gives the most recent developments of the PROMCALC & GAIA decision support system for multicriteria decision aid. It is also a survey paper giving a complete overview of this methodology. A special effort has been done to present all the possibilities of this DSS as concisely as possible. To decide in a multicriteria environment is difficult and important for practice. Indeed most decision problems that arise in our daily life involve different and often conflicting objectives that we try to satisfy simultaneously. In practice this attempt is illusory and we have to consider the best compromise solutions. Hence, given the complexity of the decision problems and their important impact in today's business activities, it is essential to provide decision makers with an efficient support. The current availability of powerful personal computers and the development of adapted multicriteria decision aid methods make this possible. The PROMCALC & GAIA software is such a decision support system. It is based on the PROMETHEE & GAIA methods $[3,6–8,16,2]$ . The PROMETHEE approach is normative while the GAIA procedure consists of a visual interactive modelling technique.

![](/api/attachments/JVSDXATB/fulltext/images/969a701d9ecf9db5726c5bd5332ff9b913dffb74c8f7cb7d66774c3b33fd9006.jpg)

Bertrand Mareschal is Assistant at the Solvay Business School of the Université Libre de Bruxelles (Brussels, Belgium) where he teaches statistics and operational research. He graduated in Mathematics in 1983, in Actuarial Science in 1986 and received a Ph.D. in 1989, all from the Université Libre de Bruxelles. His current research interests include multiple criteria and group decision aid, decision support systems and the use of quantitative methods in fi nance. He has published papers in the European Journal of Operational Research, Journal of the Royal Statistical Society, Mathematical and Computer Modelling, INFOR, Actualité Economique, Cahiers du C.E.R.O., and the Revue de la Banque.

After a short introduction to some fundamentals of multicriteria decision aid, the PROMETHEE and GAIA methods are fully described in the next sections. A numerical application is given to illustrate the characteristics of the methodology and its implementation in the PROMCALC & GAIA microcomputer software. The conclusion summarizes the capabilities and possible extensions of the system. A list of actual and potential fields of applications is given.

## 2. Multicriteria decision problems

## 2.1. Basic data

We consider multicriteria decision problems of the following type:

$$
\operatorname{Max} \left\{f _ {1} (a), f _ {2} (a), \dots , f _ {j} (a), \dots , f _ {k} (a) \mid a \in A \right\}.\tag{1}
$$

A is a set of n possible decisions or alternatives which are evaluated through k criteria $f_{1}, \ldots, f_{k}$ . The basic data for such a problem can be presented as shown in Table 1.

Given this table, the dominance relation, based on a unanimity principle, can be defined as follows $(a, b \in A)$ :

$$
\begin{array}{l} a \text { dominates } b (a D b) \text { iff } f _ {h} (a) \geq f _ {h} (b), \\ \forall h = 1, \dots , k \quad (\text { with   at   least   one } >). \end{array}\tag{2}
$$

The non-dominated alternatives are called efficient (or Pareto-optimal) solutions. In practice, the dominance relation is often very poor and the number of efficient solutions can be rather large.

Indeed, it is clear that such data do not generally induce a complete ranking on the set A of alternatives. The problem is not mathematically well-stated and the notion of optimal solution does not exist. However, the problem is most often economically well-stated as it expresses the different and possibly conflicting objectives of the decision maker. In order to provide the decision maker with a good assistance a particular multi-criteria methodology must be considered.

Table 1 Evaluation table

<table><tr><td></td><td> $f_1(.)$ </td><td> $f_2(.)$ </td><td>...</td><td> $f_j(.)$ </td><td>...</td><td> $f_k(.)$ </td></tr><tr><td> $a_1$ </td><td> $f_1(a_1)$ </td><td> $f_2(a_1)$ </td><td>...</td><td> $f_j(a_1)$ </td><td>...</td><td> $f_k(a_1)$ </td></tr><tr><td> $a_2$ </td><td> $f_1(a_2)$ </td><td> $f_2(a_2)$ </td><td>...</td><td> $f_j(a_2)$ </td><td>...</td><td> $f_k(a_2)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $a_i$ </td><td> $f_1(a_i)$ </td><td> $f_2(a_i)$ </td><td>...</td><td> $f_j(a_i)$ </td><td>...</td><td> $f_k(a_i)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $a_n$ </td><td> $f_1(a_n)$ </td><td> $f_2(a_n)$ </td><td>...</td><td> $f_j(a_n)$ </td><td>...</td><td> $f_k(a_n)$ </td></tr></table>

## 2.2. Some requisites for an appropriate multicriteria method

As the purpose of most multicriteria methods is to enrich the dominance relation, we formulate seven basic requisites for a proper enrichment.

Let us first consider five small examples that will lead to the formulation of these requirements. For each example, two possible alternatives a and b are evaluated through two criteria $f_{1}$ and $f_{2}$ that have to be maximized (see Table 2).

Example I. a is the only efficient alternative. It is fairly dominating b on both criteria. In this case, a should clearly be recommended to the decision maker. This is in agreement with the notion of efficiency.

Example II. a and b are both efficient. No alternative is dominating the other one: a is fairly better on $f_{1}$ and b on $f_{2}$ . Without additional information, no sound mathematical theory could decide which decision is the best: a and b are thus incomparable. It is up to the decision maker to finalize the choice between a and b. This again is consistent with the efficiency.

Example III. a and b are still both efficient. However, they are not anymore incomparable: a should be preferred to b. Indeed a is fairly better than b on $f_{1}$ and nearly equivalent to b on $f_{2}$ . In this case the notion of efficiency is misleading: a and b are efficient while only a should be recommended to the decision maker.

Example IV. a and b are both efficient but they are in fact nearly equivalent on both criteria. In this case, a and b should be considered as indifferent decisions.

Example V. a is the only efficient alternative. It is better than b on both criteria. However, the advantage of a on both criteria is negligible. In a multicriteria context and taking into account the fact that the model is only an approximation of the real world, it would be more realistic to consider that a and b are indifferent. Indeed it is possible that some hidden criterion for which b is better than a has not been introduced in the model.

These five examples show that the efficiency theory can sometimes be misleading. For an appropriate dominance theory, the seven following requisites could realistically be formulated.

Requisite 1. The amplitude of the deviations between the evaluations of the alternatives should be taken into account. This information is not used in the efficiency theory.

Requisite 2. As the criteria are generally expressed in different units, the scaling effects should be completely eliminated. Let us for instance reconsider Example III: suppose that $f_{1}$ is a number of jobs and $f_{2}$ a return expressed in billions dollars; then an 80-jobs deviation is negligible compared to one billion dollars and b should certainly be preferred. It is therefore essential to take into account the scales of the different criteria.

Requisite 3. When comparing two alternatives a and b, an appropriate multicriteria decision aid method should come to one of the following conclusions:

\- $a$ is preferred to $b$ ( $a P b$ ) or $b$ is preferred to $a$ ( $b P a$ ),

\- $a$ and $b$ are indifferent $(a I b)$ ,

\- $a$ and $b$ are incomparable ( $a R b$ ).

This is equivalent to assessing a partial ranking $(P, I, R)$ on A. Incomparability is important because it allows the method to avoid to decide when insufficient information is available. In any case a complete ranking $(P, I)$ includes more disputable information.

Requisite 4. Multicriteria problems are not mathematically well-stated. Depending on the logic of the method and on the kind of additional information that it requires, different results can be obtained. It is therefore important that the method be understandable by the decision maker. 'Black box effects' should be avoided. Otherwise the decision maker won't be confident and won't accept the method.

Requisite 5. An appropriate method should not include any technical parameters having no economical significance. Such parameters would also induce ‘black box effects’.

Requisite 6. The analysis of the conflicting aspects of the criteria must be available. It is indeed important for a good understanding of the structure of the problem by the decision maker to have the opportunity to detect and appreciate criteria expressing similar, independent or opposite preferences.

Requisite 7. Finally, it is also important to have a clear interpretation of the weights of the criteria.

The PROMETHEE methods and the associated GAIA visual modelling method have been designed in order to take into account these seven requisites. Moreover, the new PROMETHEE V method allows to take into account additional constraints.

3. The PROMETHEE methods (Preference Ranking Organization METHOD for Enrichment Evaluations)

## 3.1. Principles of the PROMETHEE methods

The PROMETHEE methods include the three following steps:

Table 2
Examples

<table><tr><td rowspan="2"></td><td colspan="2">Example I</td><td colspan="2">Example II</td><td colspan="2">Example III</td><td colspan="2">Example IV</td><td colspan="2">Example V</td></tr><tr><td> $f_1$ </td><td> $f_2$ </td><td> $f_1$ </td><td> $f_2$ </td><td> $f_1$ </td><td> $f_2$ </td><td> $f_1$ </td><td> $f_2$ </td><td> $f_1$ </td><td> $f_2$ </td></tr><tr><td>a</td><td>100</td><td>100</td><td>100</td><td>20</td><td>100</td><td>99</td><td>100</td><td>99</td><td>100</td><td>100</td></tr><tr><td>b</td><td>30</td><td>20</td><td>30</td><td>100</td><td>20</td><td>100</td><td>99</td><td>100</td><td>99</td><td>99</td></tr></table>

Step 1. Enrichment of the preference structure. The notion of generalized criteria is introduced in order to take into account the amplitudes of the deviations between the evaluations. This step is crucial. Yet it can easily be understood by the decision maker because all the additional parameters to be defined have an economical significance. Moreover, the scaling effects are entirely handled in this first step.

Step 2. Enrichment of the dominance relation. A valued outranking relation is built taking into account all the criteria. For each pair of alternatives, the overall degree of preference of one alternative over the other is obtained.

Step 3. Exploitation for decision aid. PROMETHEE I provides a partial ranking of A, including possible incomparabilities. PROMETHEE II provides a complete ranking of A. It can look more efficient but in fact the information used is more disputable.

## 3.2. Step 1. Generalized criteria

Let us first consider one particular criterion $f(.)$ and let us suppose that it has to be maximized:

$$
f (.) \colon A \to R (\text {   to   maximize   }).\tag{3}
$$

Pairwise comparisons between the alternatives of A lead to the following natural preference structure: $\forall a, b \in A$ :

$$
\left\{ \begin{array}{l} f (a) > f (b) \Leftrightarrow a P b, \\ f (a) = f (b) \Leftrightarrow a I b, \end{array} \right.\tag{4}
$$

which defines the dominance relation. This structure is usually extremely poor.

In order to take into account the deviations and the scales of the criteria, a generalized criterion is associated to each criterion. For this purpose we define the preference function $P(a, b)$ giving the degree of preference of a over b for criterion f. In most cases we can assume that $P(a, b)$ is a function of the deviation $d = f(a) - f(b)$ . We consider a normalized degree, so that $0 \leq P(a, b) \leq 1$ and:

$$
\left\{ \begin{array}{l} P (a, b) = 0 \text {if} d \leq 0, \\ \quad \text {no preference or indifference} \\ P (a, b) \approx 0 \text {if} d > 0, \text {weak preference} \\ P (a, b) \approx 1 \text {if} d \gg 0, \text {strong preference} \\ P (a, b) = 1 \text {if} d \gg 0, \text {strict preference}. \end{array} \right.\tag{5}
$$

![](/api/attachments/JVSDXATB/fulltext/images/283d5c6d56d0c282eb3d46f404f2f54ddf2773babaced94e83041ab44d21a393.jpg)  
Fig. 1. Preference function.

It is clear that $P$ has to be a non-decreasing function of $d$ , with a shape similar to that of Fig. 1. The generalized criterion associated to $f(.)$ is then defined by the pair $(f(.), P(.,).))$ .

The PROMETHEE methods request that a generalized criterion be associated to each criterion $f_{j}, j = 1, \ldots, k$ . This is an important step. In order to facilitate it, a set of six typical generalized criteria is proposed to the decision maker. The effective choice is then made interactively by the decision maker and the analyst according to their feeling of the preference degrees. In each case, no more than two parameters, each having a clear economical significance, have to be fixed. These six types of generalized criteria, numbered I to VI, have been thoroughly described in the literature [3,6–8] so that we don't develop this point. It is however important to note that other types of preference functions can be considered but that this was not necessary in all practical applications of PROMETHEE but only a few very specific ones.

## 3.3. Step 2: Outranking relation

Let us now suppose that a generalized criterion $(f_{j}(.), P_{j}(.,))$ has been associated to each criterion $f_{j}(.)$ of problem (1). A multicriteria preference index $\pi(a, b)$ of a over b can then be defined taking into account all the criteria:

$$
\pi (a, b) = \sum_ {j = 1} ^ {k} w _ {j} P _ {j} (a, b), \quad \left(\sum_ {j = 1} ^ {k} w _ {j} = 1\right)\tag{6}
$$

where $w_{j} > 0$ ( $j = 1, \ldots, k$ ) are weights associated to each criterion. These weights are positive real numbers that do not depend on the scales of the criteria.

![](/api/attachments/JVSDXATB/fulltext/images/4b91d69765e1f0f95380270381e95a3bb80eb8563ddfee2e9f105f45bf590094.jpg)  
Fig. 2. Outranking graph.

A quite intuitive interpretation of the weights is provided by the GAIA visual modelling approach. Anyway it is often interesting to consider equal weights first. In this case $\pi(a, b)$ is simply the arithmetic average of all the $P_{j}(a, b)$ degrees $(j = 1, \ldots, k)$ :

$$
\pi (a, b) = \frac {1}{k} \sum_ {j = 1} ^ {k} P _ {j} (a, b).\tag{7}
$$

The following properties obviously hold for the $\pi(a, b)$ values:

$$
\pi (a, a) = 0 \quad \text { and } \quad 0 \leq \pi (a, b) \leq 1, \quad \forall a, b \in A,\tag{8}
$$

$\left\{ \begin{array}{ll}\pi (a,b)\approx 0\\ \text{implies a weak global preference of } a\text{ over } b,\\ \pi (a,b)\approx 1 \end{array} \right.$

implies a strong global preference of $a$ over $b$ .

(9)

$\pi(a, b)$ expresses how and with which degree a is preferred to b, and $\pi(b, a)$ how b is preferred to a, over all the criteria.

For each pair of alternatives $a, b \in A$ the values $\pi(a, b)$ and $\pi(b, a)$ are computed. In this way a complete valued outranking relation is constructed on A. The associated outranking graph (see Fig. 2) emphasizes the considerable enrichment of the dominance relation due to the introduction of the generalized criteria.

![](/api/attachments/JVSDXATB/fulltext/images/3d4dc4da634bd6a429d1e1a0116f1fca93aab27687369848f2e52873da3bdf55.jpg)  
Fig. 3 (a). Positive flow. (b). Negative flow.

## 3.4. Step 3: Exploitation for decision aid

Let us consider how each alternative $a \in A$ is facing the n - 1 other ones and therefore define the two following outranking flows (see Figs. 3(a) and 3(b)):

-the positive outranking flow:

$$
\phi^ {+} (a) = \frac {1}{n - 1} \sum_ {x \in A} \pi (a, x),\tag{10}
$$

-the negative outranking flow:

$$
\phi^ {-} (a) = \frac {1}{n - 1} \sum_ {x \in A} \pi (x, a).\tag{11}
$$

The positive outranking flow expresses how much each alternative is outranking all the others. The higher $\phi^{+}(a)$ , the better the alternative. $\phi^{+}(a)$ represents the power of a, its outranking character.

The negative outranking flow expresses how much each alternative is outranked by all the others. The smaller $\phi^{-}(a)$ , the better the alternative. $\phi^{-}(a)$ represents the weakness of a, its outranked character.

## 3.4.1. The PROMETHEE I partial ranking

Two rankings of the alternatives are naturally deduced from the positive and negative outranking flows. Let us denote them $(S^{+}, I^{+})$ and $(S^{-}, I^{-})$ respectively:

![](/api/attachments/JVSDXATB/fulltext/images/9387cd38ea1c6b2cb359739c90b4df7a3cd17f3406c7dc17172186d2ea9a7bea.jpg)

$$
\left\{ \begin{array}{l l} a S ^ {+} b & \text { iff } \quad \phi^ {+} (a) > \phi^ {+} (b), \\ a I ^ {+} b & \text { iff } \quad \phi^ {+} (a) = \phi^ {+} (b); \end{array} \right.\tag{12}
$$

$$
\left\{ \begin{array}{l l} a S ^ {-} b & \text { iff } \quad \phi^ {-} (a) <   \phi^ {-} (b), \\ a I ^ {-} b & \text { iff } \quad \phi^ {-} (a) = \phi^ {-} (b). \end{array} \right.\tag{13}
$$

The PROMETHEE I partial ranking is the intersection of these two rankings:

$$
\left\{ \begin{array}{l l} a P ^ {I} b & \text { iff } \\ a I ^ {I} b & \text { iff } \\ a R b & \text { otherwise. } \end{array} \right. \quad \left\{ \begin{array}{l l} a S ^ {+} b & \text { and } \quad a S ^ {-} b, \\ a S ^ {+} b & \text { and } \quad a I ^ {-} b, \\ a I ^ {+} b & \text { and } \quad a S ^ {-} b, \end{array} \right.\tag{14}
$$

(P, I and R denote respectively preference, indifference and incomparability.)

The results of the pairwise comparisons of PROMETHEE I are the following:

(1) a $P^{I}$ b: a is preferred to b. In this case a higher power of a is associated to a lower weakness of a. The information given by both outranking flows is consistent and thus can be considered as sure.

(2) a $I^{I}$ b: a and b are indifferent. Both the positive and the negative outranking flows of a and b are equal.

(3) a R b: a and b are incomparable. In this case a higher power of one alternative is associated to a lower weakness of the other. This usually happens when a is good on a set of criteria on which b is weak, and reciprocally b is good on an other set of criteria on which a is weak. As the information corresponding to the flows is not consistent, it seems natural that the method should not decide which alternative is better. In such a case, it is up to the decision maker to take his responsibility and to decide.

## 3.4.2. The PROMETHEE II complete ranking

If a complete ranking of the alternatives is requested by the decision maker, the net outranking flow can be considered:

$$
\phi (a) = \phi^ {+} (a) - \phi^ {-} (a).\tag{15}
$$

It is the balance between the positive and negative outranking flows. The higher the net flow, the better the alternative.

The PROMETHEE II complete ranking is then defined:

$$
\left\{ \begin{array}{l l} a P ^ {I I} b & \text { iff } \quad \phi (a) > \phi (b), \\ a I ^ {I I} b & \text { iff } \quad \phi (a) = \phi (b). \end{array} \right.\tag{16}
$$

All the alternatives are now comparable and ex-aequos are still possible. There remains no incomparability but the resulting information is more disputable. A considerable part of the information gets lost by considering the difference (15).

3.5. PROMETHEE V: Optimization under constraints $^{1}$

PROMETHEE V [5] extends the field of application of the PROMETHEE II method to the problem of the selection of several alternatives given a set of constraints. This approach is particularly useful when the set of alternatives is segmented and constraints between and within the clusters must be verified.

Let us consider the multicriteria problem (1) and suppose that the decision maker has to select a subset of p alternatives (0 < p < n) subject to several constraints. The following boolean variables are then associated to the alternatives:

$$
x _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   } a _ {i} \text {   is   selected }, \\ 0 & \text { otherwise }. \end{array} \right.\tag{17}
$$

The PROMETHEE V procedure includes two steps:

Step 1. The multicriteria problem, without the constraints, is first considered. The net outranking flow $\phi$ is computed and provides the PROMETHEE II ranking.

Step 2. A 0-1 linear program is built in order to take into account the additional constraints:

$$
\operatorname{Max} \sum_ {i = 1} ^ {n} \phi (a _ {i}) x _ {i},\tag{18}
$$

$$
\sum_ {i = 1} ^ {n} \alpha_ {r i} x _ {i} \sim \beta_ {r}, \quad r = 1, \dots , m,\tag{19}
$$

$$
x _ {j} \in \{0, 1 \}, \quad i = 1, \dots , n,\tag{20}
$$

where $\sim$ holds for $\leq, \geq$ or $=$ .

The coefficients of the economic function (18) are the values of the net outranking flow. The objective is thus to collect as much outranking flow as possible within the subset of selected alternatives.

The linear constraints (19) can include cardinality, budget, return, investment, marketing constraints,... that the selected alternatives must satisfy. For instance, the requested number of alternatives corresponds to the following cardinality constraint:

$$
\sum_ {i = 1} ^ {n} x _ {i} = p.\tag{21}
$$

The 0-1 program can be solved using classical methods (e.g. branch and bound methods).

## 4. The GAIA visual modelling method (Geometrical Analysis for Interactive Assistance)

According to our Requisites 6 and 7, it is particularly important to provide the decision maker with information about the conflicting character of the criteria and the impact of the weights of the criteria on the final results. The GAIA visual modelling method (see [16]) provides such information. It is based on the PROMETHEE principles and complements the rather prescriptive approach of PROMETHEE I, II and V with a descriptive and graphically oriented analysis.

## 4.1. Net flow decomposition

Let us consider again the net outranking flow (15). According to the definitions of the positive and negative outranking flows (10) and (11) and to the expression of the multicriteria preference index (6), the following relation is obtained:

$$
\phi (a) = \frac {1}{n - 1} \sum_ {j = 1} ^ {k} w _ {j} \sum_ {x \in A} \left[ P _ {j} (a, x) - P _ {j} (x, a) \right].\tag{22}
$$

The multicriteria net outranking flow is decomposed into a weighted sum of unicriterion net outranking flows:

$$
\phi (a) = \sum_ {j = 1} ^ {k} w _ {j} \phi_ {j} (a),\tag{23}
$$

where:

$$
\phi_ {j} (a) = \frac {1}{n - 1} \sum_ {x \in A} \left[ P _ {j} (a, x) - P _ {j} (x, a) \right].\tag{24}
$$

Each alternative is then characterised by k unicriterion flows. Therefore it can be represented by a point in a k-dimensional space, the axes of which correspond to the different criteria. Let $\alpha$ be the point corresponding to the alternative a:

$$
\alpha : \left(\phi_ {1} (a), \phi_ {2} (a), \dots , \phi_ {j} (a), \dots , \phi_ {k} (a)\right).\tag{25}
$$

Moreover the following property obviously holds:

$$
\sum_ {a \in A} \phi_ {j} (a) = 0,\tag{26}
$$

so that the unicriterion flows are centered at the origin of the k-dimensional space.

Let us now consider the matrix $\Phi$ of all the unicriterion flows (see Table 3). It includes all the information on the preference structure of the decision maker as provided by the PROMETHEE methodology. This information is better than that provided by the initial evaluation table (see Table 1) because the degrees of preference given by the generalised criteria are taken into account.

In that way the set of alternatives can be represented by n points in the k-dimensional space. As the number of criteria is usually greater than two, it is impossible to have a clear vision of these points. The Principal Components Analysis can then be used in order to obtain a two-dimensional representation of the alternatives.

Table 3 $\Phi$ matrix

<table><tr><td></td><td> $\phi_1(.)$ </td><td> $\phi_2(.)$ </td><td>...</td><td> $\phi_j(.)$ </td><td>...</td><td> $\phi_k(.)$ </td></tr><tr><td> $a_1$ </td><td> $\phi_1(a_1)$ </td><td> $\phi_2(a_1)$ </td><td>...</td><td> $\phi_j(a_1)$ </td><td>...</td><td> $\phi_k(a_1)$ </td></tr><tr><td> $a_2$ </td><td> $\phi_1(a_2)$ </td><td> $\phi_2(a_2)$ </td><td>...</td><td> $\phi_j(a_2)$ </td><td>...</td><td> $\phi_k(a_2)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $a_j$ </td><td> $\phi_1(a_j)$ </td><td> $\phi_2(a_j)$ </td><td>...</td><td> $\phi_j(a_j)$ </td><td>...</td><td> $\phi_k(a_j)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $a_{ij}$ </td><td> $\phi_1(a_{ij})$ </td><td> $\phi_2(a_{ij})$ </td><td>...</td><td> $\phi_j(a_{ij})$ </td><td>...</td><td> $\phi_k(a_{ij})$ </td></tr></table>

![](/api/attachments/JVSDXATB/fulltext/images/cccaad15ae828875e2ad701afd16bfcb5872d6cd30e897df2b216f5dc23392a4.jpg)  
Fig. 4. The GAIA plane.

## 4.2. Principal components analysis

By using the Principal Components Analysis, it is possible to define a plane on which as few information as possible gets lost by projection (see Fig. 4). For this purpose the expression $u^{\prime}Cu + v^{\prime}Cv$ has to be maximized with respect to u and v, where C is the covariance matrix of the unicriterion net flows $\phi_{j}(j=1,\ldots,k)$ and u and v are two k-dimensional vectors. It can be proved that the maximum value is the following:

$$
\begin{array}{l} \underset {u, v} {\text {Max}} \left\{u ^ {\prime} C u + v ^ {\prime} C v \right\} \\ = \sum_ {j = 1} ^ {k} c _ {j j} \| \gamma_ {j} \| ^ {2} + 2 \sum_ {j = 1} ^ {k} \sum_ {s \neq j} c _ {j s} (\gamma_ {j}, \gamma_ {s}) \\ = n (\lambda_ {1} + \lambda_ {2}), \end{array}\tag{27}
$$

where:

\- $c_{ij}$ is the variance of $\phi_j$ ,

\- $c_{js}$ is the covariance between $\phi_j$ and $\phi_s$ ,

\- $\| \gamma_{i} \|$ is the length of $\gamma_{j}$ ,

\- $(\gamma_{j}, \gamma_{s})$ is the scalar product between $\gamma_{j}$ and $\gamma_{s}$ ,

\- $\lambda_{1}$ and $\lambda_{2}$ are respectively the largest and the second largest eigenvalues of $C$ ,

\- $u$ and $v$ are the corresponding unit eigenvectors.

The GAIA plane is defined by the vectors u and v. It is the plane on which as few information as possible gets lost by projection. A measure of the quantity of information being preserved is given by:

$$
\delta = \left(\lambda_ {1} + \lambda_ {2}\right) / \sum_ {j = 1} ^ {k} \lambda_ {j},\tag{28}
$$

where $\lambda_{j}(j = 1,\dots ,k)$ are the $k$ eigenvalues of $C$ . As $C$ is a symmetrical matrix, all the $\lambda_{j}$ 's are real.

It is interesting to note that in all the real world applications treated so far the value of $\delta$ has always been larger than 60% and in most cases larger than 80%. This means that even when the number of criteria is rather large (i.e. over 20), the GAIA plane still provides reliable information.

## 4.3. Representation of the criteria

Let us consider the projections $\gamma_{j}$ of the k unit vectors on the GAIA plane. These axes have different lengths and positions. Thanks to relation (27) it is possible to obtain a quite clear interpretation of their specific lengths and positions.

Differentiation power of the criteria. If the criterion $f_{j}$ is strongly differentiating the alternatives, the variance of $\phi_{j}$ , i.e. $c_{jj}$ , will be large. As the term $c_{jj} \parallel \gamma_{j} \parallel^{2}$ is contributing to the maximum in relation (27), the GAIA plane will tend to be chosen so that $\gamma_{j}$ is long. The length of the axis $\gamma_{j}$ is therefore a measure of how much $f_{j}$ differentiates the alternatives. The longer $\gamma_{j}$ , the more criterion $f_{j}$ differentiates the alternatives.

Similar criteria. Two criteria expressing the same preferences will have a large positive covariance. Let us suppose that $c_{js}$ is positive and large. Given its contribution in expression (27) the GAIA plane will tend to be chosen so that the scalar product $(\gamma_{j}, \gamma_{s})$ is positive and large, i.e. so that the two axes are oriented approximately in the same direction.

Independent criteria. If two criteria $f_{j}$ and $f_{s}$ express independent preferences, their covariance $c_{js}$ will be close to zero. As in this case the potential contribution to expression (27) is not significant, the GAIA will tend to be chosen so that $(\gamma_{j}, \gamma_{s})$ is also close to zero. Independent criteria are thus represented by nearly orthogonal axes.

Conflicting criteria. Conflicting criteria have large negative covariances. If $c_{js}$ is negative and large, the scalar product $(\gamma_{j}, \gamma_{s})$ will also tend to be negative and large in order to give a maximum positive contribution to expression (27). Thus conflicting criteria are represented by axes having opposite directions.

Fig. 5 displays an example where criteria $f_{2}$ , $f_{3}$ , $f_{6}$ and $f_{7}$ are more strongly differentiating the alternatives than $f_{4}$ and $f_{5}$ . The criteria $f_{2}$ , $f_{6}$ and $f_{4}$ are grouped in a cluster of criteria expressing similar preferences. Criteria $f_{1}$ and $f_{3}$ appear to be rather independent, while a strong conflict is visible between the group formed by $f_{1}$ , $f_{5}$ and $f_{7}$ and the one including $f_{2}$ , $f_{4}$ and $f_{6}$ .

The GAIA plane provides the decision maker with a powerful tool for the analysis of the differentiation power of the criteria and their conflicting aspects. However, two restrictions have to be formulated:

\- the GAIA plane includes only a percentage $\delta$ of the total information,

\- the conflicting aspects of the criteria are not measured in abstracto on the criteria themselves but rather in concreto based on the available data.

## 4.4. PROMETHEE decision axis

The assessment of weights to the different criteria is a crucial problem in all multicriteria techniques. In the PROMETHEE methods, the weights are real numbers that do not depend on the scales of the criteria. A clear visualisation of these weights is obtained in the GAIA plane.

Let us consider the vector of weights w in the k-dimensional space:

$$
\boldsymbol {w} = \left(w _ {1}, w _ {2}, \dots , w _ {j}, \dots , w _ {k}\right).\tag{29}
$$

The following relation is obtained easily:

$$
\left(\alpha_ {i}, \boldsymbol {w}\right) = \sum_ {j = 1} ^ {k} w _ {j} \phi_ {j} \left(a _ {i}\right) = \phi \left(a _ {i}\right).\tag{30}
$$

![](/api/attachments/JVSDXATB/fulltext/images/9b06b91ef667dc37541d48f29fba5ae6c6b27a1241a44e36f0c4ee9699a03dbb.jpg)  
Fig. 5. Visualisation of the criteria.

![](/api/attachments/JVSDXATB/fulltext/images/77cf3a11ee5b0dbc3f59fef80a38de51f8364c5f24f999e6ba7a8b3fa741d371.jpg)  
Fig. 6. Decision stick.

This means that the net outranking flows of the alternatives are obtained by considering the scalar products (30), i.e. the lengths of the projections of the $\alpha_{i}$ vectors on w. The projection of the $\alpha_{i}$ 's on w therefore give the PROMETHEE II ranking. w is a decision axis. It can be represented in the GAIA plane by projecting the unit vector along w. Let $\pi$ be this projection and let us call it the PROMETHEE decision axis.

If $\pi$ is short, the PROMETHEE decision axis has no strong decision power. In this case w is nearly orthogonal to the GAIA plane. This corresponds to a situation where some criteria are conflicting and a good compromise should be selected near the origin.

When the PROMETHEE decision axis is long, the decision maker is invited to select the alternatives that are located as far as possible in its direction.

The weight vector w appears like a stick located above the GAIA plane (see Fig. 6) that the decision maker can move according to his preferences in favour of particular criteria. When the weights are changed, the stick as well as the PROMETHEE decision axis move and the consequences can be clearly observed in the GAIA plane. For modified weights, the positions of the criteria and the alternatives in the GAIA plane remain unchanged.

## 4.5. Representation of the alternatives

Each alternative $a_{i}$ has a projection $\hat{\alpha}_{i}$ in the GAIA plane so that a representation of the alternatives is obtained.

It is easy to show that alternatives having a projection $\hat{\alpha}_{i}$ located in the direction of a particular criterion axis are generally good alternatives on this criterion.

![](/api/attachments/JVSDXATB/fulltext/images/169f50b0f9c758244cc1b89764fdbee43d520f401b281aa44adf7a8134edcc33.jpg)  
Fig. 7. Visualisation of the alternatives.

When the distance between two projections $\hat{\alpha}_{r}$ and $\hat{\alpha}_{s}$ is small, the corresponding alternatives are characterized by similar rows in the matrix $\Phi$ and are thus rather similar for the decision maker.

Clusters of similar alternatives can easily be detected in the GAIA plane. In the example of Fig. 7, the cluster $\{a_{1}, a_{2}, a_{3}, a_{4}\}$ appear to contain alternatives that are good on criteria $f_{4}$ , $f_{5}$ and $f_{6}$ but bad on criteria $f_{1}$ , $f_{2}$ and $f_{3}$ . Opposite conclusions are obtained for the cluster $\{a_{5}, a_{6}, a_{7}, a_{8}\}$ .

When the criteria are strongly conflicting, the PROMETHEE decision axis is usually rather short and good compromises are located close to the origin. In Fig. 7, $a_{11}$ and $a_{12}$ should be the best compromise solutions.

The incomparability between two alternatives is also clearly represented. Incomparability appears when one alternative is good on some criteria and bad on others, while the opposite holds for the other alternative. In Fig. 7, a strong incomparability appears to exist between $a_{2}$ and $a_{6}$ .

Moreover the alternatives recommended by PROMETHEE II are located in the direction of the PROMETHEE decision axis $\pi$ . A modification of the weights can of course modify seriously the conclusions. A visual sensitivity analysis, based on modifications of the weights, is therefore strongly recommended before finalising the decision. This sensitivity analysis is particularly easy to manage because the GAIA plane is determined independently of the weights and only the PROMETHEE decision axis is moving.

## 5. The PROMCALC & GAIA decision support system

The PROMETHEE and GAIA methods have been implemented on IBM compatible microcomputers. The resulting decision support system is called PROMCALC & GAIA. It is a user-friendly program, entirely menu-driven and including a context sensitive on-line help facility. A great care has been given to enhance the quality of the user interface, mainly thanks to the high resolution graphics available on the microcomputer.

PROMCALC & GAIA can analyse multicriteria problems with an evaluation matrix including up to 3600 numbers (e.g. 60 alternatives by 60 criteria or 120 alternatives by 30 criteria). The PROMETHEE I, II, V and GAIA methods are available, as well as descriptive statistics of the data and several additional weight stability analysis tools (see [13]). The program is available from the authors.

In this section we illustrate the use of PROM-CALC & GAIA on a numerical example.

The main menu of the program is shown in Fig. 8. It includes options for loading multicriteria problems (options 1 and 2) and saving them on files (option 6), editing the data within the integrated spreadsheet (option 3) and starting the analysis (option 5).

![](/api/attachments/JVSDXATB/fulltext/images/c7ae04d402103bd12ecc72753d270c85334c09bdc165290a83e3153012b35af9.jpg)  
Fig. 8. PROMCALC & GAIA: Menus.

<table><tr><td>CriterionMin/MaxTypeWeightActions</td><td>C..1Cons.Costsmin53.00</td><td>C..2Populationmax61.00</td><td>C..3Parking Plmax61.00</td><td>S.A.B.-U.L.B.-Ob/1952C..4Access RMmax41.00</td><td>C..5Competitormin32.50</td></tr><tr><td>A..1 Metherl 1</td><td>21.00</td><td>425.00</td><td>500.00</td><td>2.00</td><td>1.00</td></tr><tr><td>A..2 Metherl 2</td><td>21.30</td><td>475.00</td><td>522.00</td><td>2.00</td><td>0.00</td></tr><tr><td>A..3 Belgium 1</td><td>8.20</td><td>120.00</td><td>860.00</td><td>5.00</td><td>2.00</td></tr><tr><td>A..4 Belgium 2</td><td>6.60</td><td>45.00</td><td>722.00</td><td>3.00</td><td>1.00</td></tr><tr><td>A..5 Belgium 3</td><td>4.90</td><td>52.00</td><td>1050.00</td><td>4.00</td><td>3.00</td></tr><tr><td>A..6 Germany 1</td><td>21.30</td><td>755.00</td><td>850.00</td><td>3.00</td><td>5.00</td></tr><tr><td>A..7 Germany 2</td><td>17.90</td><td>625.00</td><td>200.00</td><td>2.00</td><td>5.00</td></tr><tr><td>A..8 Germany 3</td><td>17.30</td><td>524.00</td><td>780.00</td><td>2.00</td><td>5.00</td></tr><tr><td>A..9 Germany 4</td><td>14.20</td><td>540.00</td><td>690.00</td><td>4.00</td><td>6.00</td></tr><tr><td>A..10 France 1</td><td>10.40</td><td>80.00</td><td>675.00</td><td>4.00</td><td>3.00</td></tr><tr><td>A..11 France 2</td><td>12.90</td><td>310.00</td><td>786.00</td><td>5.00</td><td>2.00</td></tr><tr><td>A..12 France 3</td><td>9.60</td><td>275.00</td><td>1020.00</td><td>2.00</td><td>3.00</td></tr></table>

Fig. 9. PROMCALC & GAIA: Evaluation table.

Let us consider the following decision problem. A large North-American distribution company intends to enhance its network of distribution centers in Europe. A preliminary analysis has been done by a specialized consulting office and 12 potential sites are proposed to the company: 2 in the Netherlands, 3 in Belgium, 4 in

![](/api/attachments/JVSDXATB/fulltext/images/949fb93c9a862599ddf111877fa2a67b769aecafa56621fa02ceae349939765c.jpg)  
Fig. 10. PROMCALC & GAIA: PROMETHEE I partial ranking.

Table 4  
Generalized criteria and weights

<table><tr><td></td><td>Generalized criterion</td><td>Parameters</td><td>Weight</td></tr><tr><td>C1</td><td>V (Linear with ind.)</td><td> $q = 0.5, p = 3.2$ </td><td>3</td></tr><tr><td>C2</td><td>VI (Gaussian)</td><td> $s = 75$ </td><td>1</td></tr><tr><td>C3</td><td>VI (Gaussian)</td><td> $s = 225$ </td><td>1</td></tr><tr><td>C4</td><td>IV (Level)</td><td> $q = 1.0, p = 2.0$ </td><td>1</td></tr><tr><td>C5</td><td>III (Linear)</td><td> $p = 300$ </td><td>2.5</td></tr></table>

![](/api/attachments/JVSDXATB/fulltext/images/c3f9aa70313c7c1fe6a60023d6094a4eaeb27ed34ad29ed7cb2c01b272191273.jpg)  
SpaceBar : Flows positioning - Press ENTER for next page. ESC for menu.  
Fig. 11. PROMCALC & GAIA: PROMETHEE II complete ranking.

Germany and 3 in France. These 12 locations have then been evaluated on the following five criteria:

• C1: construction costs (expressed in millions US \$),

• C2: number of potential customers in the area (expressed in thousands people),

• C3: number of available parking places,

\- C4: access to the road network (expressed on a 0–6 scale),

• C5: number of competitors.

The criteria C2 to C4 have to be maximised, while C1 and C5 have to be minimised. The corresponding evaluations are presented in Fig. 9 as they appear in the spreadsheet of PROM-CALC & GAIA. The generalised criteria and weights associated to the criteria appear in the top of the spreadsheet display and are summarized in Table 4.

The analysis of this problem by PROMCALC & GAIA leads to the analysis menu (see Fig. 8) from where all the available results can be displayed. Descriptive statistics can be obtained for the criteria (average values, standard deviations, extreme values and correlation matrix) as a preliminary analysis. The matrix of the $\pi (\cdot ,\cdot)$ preference indices can be displayed as well as the actual values of the outranking flows.

The PROMETHEE I partial ranking (see Fig. 10) and PROMETHEE II complete ranking (see Fig. 11 for the six last ranked alternatives) are represented graphically. The actual values of the net outranking flows are also represented in Fig. 11 ('Phi Scale'). By looking at this display it is possible to detect clusters of alternatives which are very close to each other. In this example, the three first ranked alternatives (A4, A5 and A3) form such a cluster and there is a large gap between them and the two next ones (A11 and A12).

At this stage it appears clearly on the graphs that the alternatives are grouped in clusters based on their geographical area. This is quite reasonable according to the specific economical characteristics of each country.

Some incomparabilities appear in the PRO-METHEE I partial ranking. For instance, A4 and A5 are incomparable and, should the decision maker select only one location, the choice should be made between these two potential locations.

The GAIA display (see Fig. 12) confirms the specificity of the different countries. Let us first remark the quality of the representation: with $\delta = 86\%$ , only 14% of the total information gets lost by the projection. The alternatives appear to be well-clustered in the plane according to their country. In addition, the conflicting aspects of the criteria appear clearly. It is also possible to detect which alternatives are good or bad on the different criteria. For instance, the cluster France (A10, A11, A12) has a rather good situation close to the origin. The cluster Netherlands (A1, A2) is good on criteria Population and Competitors (C2 and C5). The cluster Belgium (A3, A4, A5) is good on all criteria except Population. And the cluster Germany is good only on criterion Population.

![](/api/attachments/JVSDXATB/fulltext/images/1761c0fad4bde5c8f5b81aa289f3fc5cc3213debbe82250f2b5f8bd106025b90.jpg)  
A-C-X-W/R-P: switches - Z: Zoom - F6: Pron6 - ENTER: Page - ESC: Menu  
Fig. 12. PROMCALC & GAIA: GAIA display.

According to the weights associated to the criteria, the PROMETHEE decision axis $\pi$ is strongly oriented in the direction of the cluster Belgium. This is consistent with the PROMETHEE II complete ranking given in Fig. 11. At this stage, a first weight sensitivity analysis is possible: the weights can be changed and the position of the decision axis is immediately updated in the GAIA plane.

Other weight sensitivity instruments are available through option 7 in the analysis menu (see Fig. 8). They include weight stability intervals, polygons and areas as defined in [13,15] (see also [1] for similar ideas) as well as a new procedure called The Walking Weights (see Fig. 13). This last instrument displays graphically and simultaneously the values of the net outranking flow of the alternatives and those of the weights of the criteria. It is possible to interactively modify the values of the weights and immediately observe the resulting change of the PROMETHEE II ranking.

Up till now we have been able to analyse the structure of the decision problem and to express some recommendations to the decision maker. Indeed, given the PROMETHEE I and II rankings it appears that the best locations are in Belgium and in France. However, the actual problem of the distribution company is to implant several new centers in Europa, subject to various constraints such as the coverage of the different countries. Obviously in this context it would not be appropriate to select for instance the six best alternatives of the PROMETHEE II ranking (i.e. all the Belgian and French locations).

As constraints must be taken into account, the PROMETHEE V method is an adequate approach. Let us consider the following constraints (see Table 5):

\- K1 and K2: there must be at least 5 and at most 9 selected locations;

\- K3: given expected annual returns for each location, the total expected annual return must be at least 4000 ( $\times 10^{4}$ US \$);

\- K4: one and only one of the two locations in the Netherlands (A1, A2) must be selected;

![](/api/attachments/JVSDXATB/fulltext/images/0ccf0ca726baafd7277c5817f139298fa7fd1de6cde9bc7353a211faa8a3d561.jpg)  
Fig. 13. PROMCALC & GAIA: The walking weights.

Table 5
PROMETHEE V constraints

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
K1  $x_{1} + x_{2} + x_{3} + \cdots + x_{10} + x_{11} + x_{12} \geq 5$ 
K2  $x_{1} + x_{2} + x_{3} + \cdots + x_{10} + x_{11} + x_{12} \leq 9$ 
K3  $426x_{1} + 645x_{2} + 76x_{3} + 226x_{4} + 275x_{5} + 822x_{6} + 1026x_{7} + 692x_{8} + 601x_{9} + 464x_{10} + 516x_{11} + 602x_{12} \geq 4000$ 
K4  $x_{1} + x_{2} = 1$ 
K5  $x_{3} + x_{4} + x_{5} \leq 2$ 
K6  $x_{10} + x_{12} \leq 1$
</div>

\- K5: no more than two Belgian locations (A3, A4 and A5) can be selected;

\- K6: the first and the third locations in France (A10 and A12) cannot be selected simultaneously, due to their proximity.

The corresponding 0–1 linear programme, including the objective function as defined in (18), is then solved by a branch and bound technique. The unique optimal solution is obtained after 149 iterations and 2 seconds of computing time on a 16 MHz 386SX computer. The seven following sites are actually selected by PROMETHEE V:

## A2, A4, A5, A6, A7, A10 and A12.

(31)

A sensitivity analysis is also available: the user can modify the selection and immediately observe which constraints are violated and/or what is the corresponding loss on the economical function.

## References

[1] C. Bana e Costa, The outweigh approach for multicriteria decision aid under partial intercriteria preference information, working paper STOOTW/246, V.U.B., Brussels, 1989.

[2] C. Bana e Costa, ed., Readings in Multiple Criteria Decision Aid (Springer-Verlag, Berlin, 1990).

[3] J.P. Brans, L'Ingénierie de la décision. Elaboration d'instruments d'aide à la décision. Méthode PROMETHEE, Université Laval, Colloque d'Aide à la Décision Québec, Canada, 1982, pp. 183–213.

[4] J.P. Brans and B. Mareschal, BANK ADVISER: An industrial evaluation system, Working Paper STOO/239, Vrije Universiteit Brussel, 1989.

[5] J.P. Brans and B. Mareschal, PROMETHEE V: MCDM problems with segmentation constraints, INFOR, Vol. 30. Nr. 2, 1992, 35–96.

[6] J.P. Brans, B. Mareschal and Ph. Vincke, PROMETHEE: A new family of outranking methods in MCDM, in IFORS '84 (North-Holland, Amsterdam, 1984) 447–490.

[7] J.P. Brans and Ph. Vincke, A preference ranking organisation method: The PROMETHEE method for MCDM, Management Sci. 31 6 (1985) 647–656.

[8] J.P. Brans, B. Mareschal and Ph. Vincke, How to select and how to rank projects: The PROMETHEE method, Europ. J. Operat. Res. 24 (1986) 228–238.

[9] Th. Briggs, P.L. Kunsch and B. Mareschal, Nuclear waste management: An application of the multicriteria PROMETHEE method, Europ. J. Operat. Res. 44 (1990) 1–10.

[10] G.R. D'Avignon and B. Mareschal, Specialisation of hospital services in Québec: An application of the PROMETHEE and GAIA methods, Math. Comput. Modelling 12 (1989) 1393–1400.

[11] Ph. du Bois, J.P. Brans, F. Cantraine and B. Mareschal, Medicis: An expert system for computer-aided diagnosis using the PROMETHEE method, Europ. J. Operat. Res. 39 (1989) 284–292.

[12] B. Mareschal, Stochastic multicriteria decision-making under uncertainty, Europ. J. Operat. Res. 26 (1986) 58–64.

[13] B. Mareschal, Weight stability intervals in multicriteria decision aid, Europ. J. Operat. Res. 33 (1988) 54–64.

[14] B. Mareschal, Aide à la décision multicritère: Développements théoriques et applications, C.C.E.R.O. 31 (1989) 13–120.

[15] B. Mareschal, Weight stability analysis for additive multi-criteria methods, Working paper, U.L.B., 1991.

[16] B. Mareschal and J.P. Brans, Geometrical representations for MCDA, Europ. J. Operat. Res. 34 (1988) 69–77.

[17] B. Mareschal and J.P. Brans, BANK ADVISER: An industrial evaluation system, to be published in Europ. J. Operat. Res., 54, 1991, 318–324.

[18] B. Mareschal and D. Mertens, Evaluation financière par la méthode GAIA: Application au secteur bancaire Belge, Rev. Banque 6 (1990) 317–329.

[19] N. Mladineo, J. Margeta, J.P. Brans and B. Mareschal, Multicriteria ranking of alternative locations for small scale hydroplants, Europ. J. Operat. Res. 31 (1987) 215–222.

[20] N. Mladineo and J. Grabovac, The application of multicriteria analysis in the selection of the optimal renewable energy sources for tourist facilities, Proc. Zbornik Radova, Yugoslavia (1988) 10–121.

[21] Z. Ribarovic and N. Mladineo, Application of multicriteria analysis to the ranking and evaluation of the investment programmes in the ready mixed concrete industry, Eng. Costs Prod. Econ. 12 (1987) 367–374.

[22] W. Struys and H. Pastijn, The recourse to several criteria in determining a fair burden sharing within an alliance: The case of NATO, in: G.K. Rand, ed., Operat. Research '87 (North-Holland, Amsterdam, 1988) 566–581.
