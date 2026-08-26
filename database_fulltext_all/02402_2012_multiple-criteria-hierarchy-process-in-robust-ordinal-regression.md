---
otero_id: 2402
otero_key: "N5N69CTB"
title: "Multiple Criteria Hierarchy Process in Robust Ordinal Regression"
authors: "Salvatore Corrente; Salvatore Greco; Roman Słowiński"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.03.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multiple Criteria Hierarchy Process in Robust Ordinal Regression

Salvatore Corrente <sup>a</sup>, Salvatore Greco <sup>a</sup>, Roman Słowiński <sup>b,</sup>⁎

<sup>a</sup> Department of Economics and Business, University of Catania, Corso Italia, 55, 95129 Catania, Italy

<sup>b</sup> Institute of Computing Science, Poznań University of Technology, 60–965 Poznań, and Systems Research Institute, Polish Academy of Sciences, 01-447 Warsaw, Poland

## a r t i c l e i n f o

Article history: Received 3 August 2011 Received in revised form 5 January 2012 Accepted 13 March 2012 Available online 28 March 2012

Keywords: Multiple Criteria Decision Aiding Hierarchy of criteria Multiple Criteria Hierarchy Process Robust Ordinal Regression Preference modeling

## a b s t r a c t

A great majority of methods designed for Multiple Criteria Decision Aiding (MCDA) assume that all evaluation criteria are considered at the same level, however, it is often the case that a practical application is imposing a hierarchical structure of criteria. The hierarchy helps decomposing complex decision making problems into smaller and manageable subtasks, and thus, it is very attractive for users. To handle the hierarchy of criteria in MCDA. we propose a methodology called Multiple Criteria Hierarchy Process (MCHP) which permits consideration of preference relations with respect to a subset of criteria at any level of the hierarchy. MCHP can be applied to any MCDA method. In this paper, we apply MCHP to Robust Ordinal Regression (ROR) being a family of MCDA methods that takes into account all sets of parameters of an assumed preference model, which are compatible with preference information elicited by a Decision Maker (DM). As a result of ROR, one gets necessary and possible preference relations in the set of alternatives, which hold for all compatible sets of parameters or for at least one compatible set of parameters, respectively. Applying MCHP to ROR one gets to know not only necessary and possible preference relations with respect to the whole set of criteria, but also necessary and possible preference relations related to subsets of criteria at different levels of the hierarchy. We also show how MCHP can be extended to handle group decision and interactions among criteria

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

It is well known that the dominance relation established in the set of alternatives evaluated on multiple criteria is the only objective information that comes out from a formulation of a multiple criteria decision problem (including sorting, ranking and choice). While dominance relation permits to eliminate many irrelevant (i.e. dominated) alternatives, it does not compare completely all of them, resulting in a situation where many alternatives remain incomparable. This situation may be addressed by taking into account preferences of a Decision Maker (DM). Therefore, all Multiple Criteria Decision Aiding (MCDA) methods (for state-of-the-art surveys on MCDA see [7]) require some preference information elicited by a DM. Information provided by a DM is used within a MCDA process to build a preference model which is then applied on a non-dominated (Pareto-optimal) set of alternatives to arrive at a recommendation.

A great majority of methods designed for MCDA, assume that all evaluation criteria are considered at the same level, however, it is often the case that a practical application is imposing a hierarchical structure of criteria. For example, in economic ranking, alternatives may be evaluated on indicators which aggregate evaluations on several subindicators, and these sub-indicators may aggregate another set of subindicators, etc. In this case, the marginal value functions may refer to all levels of the hierarchy, representing values of particular scores of the alternatives on indicators, sub-indicators, sub-sub-indicators, etc. Considering hierarchical, instead of <sup>fl</sup>at, structure of criteria, permits decomposition of a complex decision problem into smaller problems involving less criteria. To handle the hierarchy of criteria, we introduce in this paper a Multiple Criteria Hierarchy Process (MCHP). The basic idea of MCHP relies on consideration of preference relations at each node of the hierarchy tree of criteria. These preference relations concern both the phase of eliciting preference information, and the phase of analyzing a <sup>fi</sup>nal recommendation by the DM. Let us consider a very simple and well known preference model, the linear value function, which assigns to each alternative a ∈ A the value $U ( a ) = w _ { 1 } g _ { 1 } ( a ) + . . . +$ $w _ { n } g _ { n } ( a ) , w _ { i } { \geq } 0 , i { = } 1 , \ldots n$ , where g (a) is an evaluation of alternative a on criterion g ,i=1,…,n. If in the phase of eliciting preference information, the DM declares that alternative a is preferred to alternative b with respect to a criterion which, in a node of the hierarchy tree, groups a set of sub-criteria $\mathcal { G } _ { \mathbf { r } } ,$ , this can be modeled as

$$
\sum_ {i \in \mathcal {G} _ {\mathbf {r}}} w _ {i} g _ {i} (a) > \sum_ {i \in \mathcal {G} _ {\mathbf {r}}} w _ {i} g _ {i} (b),
$$

which puts some constraints on the values of admissible weights w . In the phase of analyzing a <sup>fi</sup>nal recommendation, even more important, MCHP shows preference relations $\succsim$ on A with respect to the set of subcriteria $\mathcal { G } _ { \bf r } ,$ such that, for all $a , b \in A ,$

$$
a \succsim_ {\mathbf {r}} b \Longleftrightarrow \sum_ {i \in \mathcal {G} _ {\mathbf {r}}} w _ {i} g _ {i} (a) \geq \sum_ {i \in \mathcal {G} _ {\mathbf {r}}} w _ {i} g _ {i} (b),
$$

wherea ${ \succsim } _ { \mathbf { r } }$ b reads alternative a is at least as good as alternative b on the set of subcriteria $\mathcal { G } _ { \mathbf { r } }$ . Analyzing the preference relation $\succsim$ is very useful <sup>G</sup>in any decision aiding process because it permits to look into structural elements of the overall preference relation c taking into account the whole set of criteria, and justify better the <sup>fi</sup>nal recommendation. For example, in a decision problem related to evaluation of students, one can say not only that student a is comprehensively preferred to student $b , \mathrm { i } . \mathsf { e } . a \succ b$ (where ≻ is the asymmetric part of c; analogously, in the following, $\succ _ { \mathbf { r } }$ is the asymmetric part of $\succsim _ { \mathbf { r } } ) ,$ , but also that a is comprehensively preferred to b because a is preferred to b on subsets of subjects (subcriteria) related to Mathematics and Physics, $\mathrm { i . e . } a \succ _ { M a t h e m a t i c s } b$ and $a \succ _ { P h y s i c s } b ,$ , even if b is preferred to a on subjects related to Humanities, i.e. $b { > } _ { H u m a n i t i e s } a$ . Moreover, one can also say that, for example, a is preferred to b on the subset of subjects related to Mathematics because, considering Analysis and Algebra as subjects (sub-criteria) related to Mathematics, a is preferred to b on Analysis, $\mathrm { i } . \mathrm { e } . a \succ _ { A n a l y s i s } b ,$ , and this is enough to compensate the fact that b is preferred to a on Algebra, i.e. $b \mathrm { > } _ { A l g e b r a }$ a. Since partial preference relations c <sub>Mathematics</sub>, c <sub>Physics</sub>, c <sub>Humanities</sub>, c <sub>Analysis</sub>, c <sub>Algebra</sub>, and so on, can be constructed using any MCDA methodology, this shows the universal character of MCHP.

In this paper, in order to show the useful features of MCHP, we apply this methodology to a recently proposed family of MCDA methods, called Robust Ordinal Regression (ROR) [8,9,11,12]. Basic ideas of ROR can be summarized as follows. To deal with a multiple criteria decision problem, Multiple Attribute Utility Theory (MAUT) [20] constructs a value function which assigns to each alternative a real number representing its degree of preferability. The <sup>fi</sup>rst MCDA methods using the ordinal regression approach [4,25,28], aimed at <sup>fi</sup>nding one value function compatible with preference information provided by the DM (see, e.g., [6,18,22,24]). Most frequently additive value functions have been considered, i.e. functions obtained by summing up marginal value functions corresponding to particular criteria. For example, in [18], each marginal value function is a piecewise-linear one. Remark that in case of ordinal regression the preference information is always indirect.

In ordinal regression, and also in ROR, the preference information elicited by the DM is indirect, i.e. the DM provides decision examples, like preferential pairwise comparisons of some selected alternatives. This type of preference information is opposed to the direct one, which is composed of values of parameters of the assumed preference model, like weights or trade-off rates of the weighted sum model. Research indicates that indirect preference elicitation requires less cognitive effort from the DM than the direct one, and thus, it becomes more and more popular.

When building, via ordinal regression, a value function compatible with indirect preference information given as pairwise comparisons of some selected alternatives, one encounters a problem of plurality of compatible value functions. Until recently, the usual practice was to select only one of the compatible value functions, either by the DM or using some mathematical tools for <sup>fi</sup>nding a “central” value function. In general, however, each compatible value function gives a different ranking of the considered set of alternatives, and thus, it is reasonable to investigate what is the consequence of applying all compatible value functions on the whole set of considered alternatives. For this reason, ROR takes into account all compatible value functions simultaneously. In this context, two preference relations are considered:

– possible preference relation, for which alternative a is possibly preferred to alternative b if a is at least as good as b for at least one compatible value function, and

– necessary preference relation, for which alternative a is necessarily preferred to alternative b if a is at least as good as b for all compatible value functions.

The <sup>fi</sup>rst method that applied the concept of ROR was ${ \mathrm { U T A } } ^ { G M S } [ { \mathfrak { g } } ] { \mathrm { : } }$ it takes into account pairwise comparisons of alternatives provided by a DM; GRIP [8] was its generalization taking into account not only pairwise comparisons, but also intensities of preference; ROR has been also applied to sorting problems [11], and it has been adapted to other preference models, like outranking relation [14,15] and non additive integrals [1].

Applying MCHP to ROR, permits to consider preference information at each level of the hierarchy in the phase of eliciting preference information. Moreover, putting together MCHP and ROR, permits to de<sup>fi</sup>ne necessary and possible preference relations at each node of the hierarchy tree. This gives an insight into evolution of the necessary and possible preference relations along the hierarchy tree. In fact, if we know that a is not necessarily comprehensively preferred to $b ,$ with MCHP we can <sup>fi</sup>nd at which level a particular subcriterion opposes to the conclusion that a is necessarily preferred to b. All the properties that hold for the “<sup>fl</sup>at” version of ROR methods are also valid in the hierarchical context, and other properties that are characteristic to the hierarchical context are given in this paper.

The paper is structured in this way: Section 2 describes some basic concepts of the MCHP; Section 3 describes the GRIP method adapted to the hierarchical context; in Section 4 we present the properties of necessary and possible preference relations; Section 5 describes the concept of intensity of preference and most representative value function; in Section 6 we present a didactic example; in Section 7 we present some extensions of the hierarchical ROR; Section 8 ends the paper with conclusions.

## 2. Multiple Criteria Hierarchy Process (MCHP)

In MCHP, we consider a set of hierarchically ordered criteria, i.e. all criteria are not considered at the same level, but they are distributed over l different levels (see Fig. 1). At level 1, there are <sup>fi</sup>rst level criteria called root criteria. Each root criterion has its own hierarchy tree. The leaves of each hierarchy tree are at the last level l and they are called elementary subcriteria. Thus, in graph theory terms, the whole hierarchy is a forest. We will use the following notation:

$A = \{ a , b , c , \ldots \}$ is the <sup>fi</sup>nite set of alternatives,

• l is the number of levels in the hierarchy of criteria,

• is the set of all criteria at all considered levels,

<sup>G</sup><sub>•</sub> $\boldsymbol { \mathcal { T } } _ { \mathcal { G } }$ is the set of indices of particular criteria representing position of <sup>IG</sup>criteria in the hierarchy,

• m is the number of the <sup>fi</sup>rst level criteria, $G _ { 1 } , . . . , G _ { m }$

$G _ { \mathbf { r } } { \in } \mathcal { G } ,$ with $\mathbf { r } = ( i _ { 1 } , . . . , i _ { h } ) { \in } \mathcal { T } _ { \mathcal { G } } ,$ denotes a subcriterion of the <sup>fi</sup>rst level <sup>G</sup>criterion $G _ { i _ { 1 } }$ <sup>¼ ð Þ IG</sup>at level h; the <sup>fi</sup>rst level criteria are denoted by $G _ { i _ { 1 } } ,$ $i _ { 1 } { = } 1 , { \ldots } , m ,$

• n r is the number of subcriteria of $G _ { \mathbf { r } }$ in the subsequent level, i.e. <sup>ð Þ</sup>the direct subcriteria of $G _ { \mathbf { r } }$ are $G _ { ( \mathbf { r } , 1 ) } , . . . , G _ { ( \mathbf { r } , n ( \mathbf { r } ) ) }$

$g _ { \mathbf { t } } ; A { \longrightarrow } \mathbb { R } , { \mathrm { w i t h } } \mathbf { t } = ( i _ { 1 } , . . . , i _ { l } ) { \in } { \mathcal { T } } _ { \mathcal { G } } ,$ <sup>ð Þ ð Þð Þ</sup>denotes an elementary subcriterion <sup>¼ ð</sup>of the <sup>fi</sup>rst level criterion $G _ { i _ { 1 } , }$ <sup>IG</sup>, i.e. a criterion at level l of the hierarchy tree of $G _ { i _ { 1 } }$

• EL is the set of indices of all elementary subcriteria:

$$
E L = \left\{\mathbf {t} = (i _ {1},..., i _ {l}) \in \mathcal {I} _ {\mathcal {G}} \right\} \text {   where   } \left\{ \begin{array}{l} i _ {1} = 1,..., m \\ i _ {2} = 1,..., n (i _ {1}) \\ ... \\ i _ {l} = 1,..., n (i _ {1},..., i _ {l - 1}) \end{array} \right.
$$

$E ( G _ { \mathbf { r } } )$ is the set of indices of elementary subcriteria descending from $G _ { \Gamma } , \mathrm { i } . \mathrm { e }$

$$
E (G _ {\mathbf {r}}) = \left\{\left(\mathbf {r}, i _ {h + 1},..., i _ {l}\right) \in \mathcal {I} _ {\mathcal {G}} \right\} \text {   where   } \left\{ \begin{array}{l} i _ {h + 1} = 1,..., n (\mathbf {r}) \\ \dots \\ i _ {l} = 1,..., n (\mathbf {r}, i _ {h + 1},..., i _ {l - 1}) \end{array} \right.
$$

thus, $E ( G _ { \mathbf { r } } ) \subseteq E L$

![](/api/attachments/N5N69CTB/fulltext/images/510a343a71b1ba285b7d1ae313551d4c382a124e26339c7138f448f89dc26ff0.jpg)  
Fig. 1. Hierarchy of criteria for the <sup>fi</sup>rst level (root) criterion $G _ { i _ { 1 } } .$

• when $\mathbf { r } = 0 ,$ then by $G _ { \mathbf { r } } = G _ { 0 }$ , we mean the entire set of criteria and not a particular criterion or subcriterion; in this particular case, we have $E ( G _ { 0 } ) = E L$

Without loss of generality we suppose that each elementary subcriterion $g _ { \mathbf { t } } , \mathbf { t } { \in } E L$ , maps alternatives to real numbers $g _ { \mathrm { t } } \colon A \to \mathbb { R }$ , such that for all $a , b { \in } A , g _ { \mathbf { t } } ( a ) { \geq } g _ { \mathbf { t } } ( b )$ means that a is at least as good as b with <sup>ð Þ ð Þ</sup>respect to elementary criterion $g _ { \mathbf { t } } .$ . If criterion $g _ { \mathrm { t } }$ has, originally, an ordered qualitative scale, e.g., very bad, bad, medium, good, very good, one can number code such linguistic labels in a way maintaining the preference order. Each alternative $a \in A$ is evaluated directly on the elementary subcriteria only, such that to each alternative $a \in A$ there corresponds a vector of evaluations:

$$
\left(g _ {\mathbf {t} _ {1}} (a), \dots , g _ {\mathbf {t} _ {n}} (a)\right), \quad n = | E L |.
$$

Within MCHP, in each node $G _ { \mathbf { r } } { \in } \mathcal { G }$ of the hierarchy tree there exists a preference relation $\succsim \mathbf { r } \ 0 \mathrm { n } \ A ,$ <sup>G</sup>such that for all $a , b \in A , a \succeq _ { \mathbf { r } } b$ means $^ { * } a$ is at least as good as b on subcriterion $G _ { \mathbf { r } } "$ . In the particular case where $G _ { \mathbf { r } } = g _ { \mathbf { t } } , \mathbf { t } { \in } E L , a \succeq _ { \mathbf { t } } b$ holds i $\mid g _ { \mathrm { t } } ( a ) { \geq } g _ { \mathrm { t } } ( b )$

<sup>¼ ð Þ ð Þ</sup>A minimal requirement that preference relations ${ \succsim } _ { \mathbf { r } }$ have to satisfy is a dominance principle for hierarchy of criteria, stating that if alternative a is at least as good as alternative b for all subcriteria $G _ { ( \mathbf { r } , j ) }$ of $G _ { \mathbf { r } }$ of the level immediately below, then a is at least as good as b on $G _ { \mathbf { r } } .$ For example, if student a is at least as good as student b on Algebra and Analysis, being subcriteria of Mathematics, then a is at least as good as b on Mathematics. Formally, this dominance principle can be stated as follows: given $G _ { \mathbf { r } } , \mathbf { r } \in \mathcal { T } _ { \mathcal { G } } \setminus E L , { \mathrm { i f } } a \succ _ { ( \mathbf { r } , j ) } b$ for $\mathbf { a } | | j = 1 , . . . , n ( \mathbf { r } )$ then $a \succsim b .$

<sup>IG ð Þ ¼ ð Þ</sup>In this article, we will aggregate the evaluations of alternative $a \in A$ with respect to the elementary subcriteria $g _ { \mathbf { t } } , \mathbf { t } { \in } E L$ , using an additive value function:

$$
U \left(g _ {\mathbf {t} _ {1}} (a), \dots , g _ {\mathbf {t} _ {n}} (a)\right) = \sum_ {\mathbf {t} \in E L} u _ {\mathbf {t}} \left(g _ {\mathbf {t}} (a)\right),\tag{1}
$$

where $u _ { \mathrm { t } }$ are marginal value functions, non-decreasing with respect to the evaluation expressed by its argument. Analogously, the marginal value function of alternative a∈A on criterion $G _ { \mathbf { r } } { \in } { \mathcal { G } } ,$ , is given by:

$$
U _ {\mathbf {r}} (g _ {\mathbf {t}} (a), \mathbf {t} \in E (G _ {\mathbf {r}})) = \sum_ {\mathbf {t} \in E (G _ {\mathbf {r}})} u _ {\mathbf {t}} (g _ {\mathbf {t}} (a)),\tag{2}
$$

such that for all $a , b \in A , a \succeq _ { \mathbf { r } } b$ iff $U _ { \mathbf { r } } ( a ) { \geq } U _ { \mathbf { r } } ( b )$

<sup>ð Þ ð Þ</sup>In the following, to simplify the notation, we shall write $U ( a )$ instead of $U \big ( g _ { \mathbf { t } _ { 1 } } ( a ) , . . . , g _ { \mathbf { t } _ { n } } ( a ) \big ) , U _ { \mathbf { r } } ( a )$ instead of $U _ { \mathbf { r } } ( g _ { \mathbf { t } } ( a ) , \mathbf { t } { \in } E ( G _ { \mathbf { r } } ) )$ , and $u _ { \mathbf { t } } ( a )$ instead of $u _ { \mathrm { t } } ( g _ { \mathrm { t } } ( a ) ) ,$ .

## 3. Multiple Criteria Hierarchy Process applied to a Robust Ordinal Regression method

When aggregating evaluations of alternatives on multiple elementary subcriteria, we will take into account some preference information provided by the DM. This preference information concerns a subset of alternatives $A ^ { R } \subseteq A ,$ , called reference alternatives, on which the DM is relatively more con<sup>fi</sup>dent than on the others. The DM is expected to provide the following preference information:

$\mathbf { \Sigma } - \mathbf { \Sigma } \ a$ partial preorder c on $A ^ { R }$ , whose meaning is: for $a ^ { * } , b ^ { * } \in A ^ { R }$

$a ^ { * } \succsim b ^ { * } \Leftrightarrow \ " a $ is at least as good as $b ^ { \ast \prime }$

Denoting by $\succsim - 1$ the inverse of c, i.e. if $\cdot \boldsymbol { a } ^ { * } \succ \boldsymbol { b } ^ { * }$ then $b ^ { * } \succsim \ l ^ { - 1 } a ^ { * } , \ l ^ { \sim }$ (indifference) is the symmetric part of c given by $\succsim \cap \succsim ^ { - 1 }$ , i.e. if $a ^ { * } { \sim } b ^ { * }$ then $a ^ { * } \succ b ^ { * }$ and $a ^ { \ast } \succsim ^ { - 1 } b ^ { \ast }$ , and ≻ (preference) is the asymmetric part given by $( \succ | \sim )$ , i.e. if $a ^ { * } { \succ b } ^ { * }$ then $a ^ { * } \succ b ^ { * }$ and not $a ^ { * } \sim b ^ { * }$ - a partial preorder $\succsim$ on $A ^ { R } { \times } A ^ { R }$ , whose meaning is: for $a ^ { * } , b ^ { * } , c ^ { * } , d ^ { * } \in A ^ { R } ,$

$( { \mathfrak { a } } ^ { * } , b ^ { * } ) { \succsim } ^ { * } ( c ^ { * } , d ^ { * } ) { \iff } ^ { * } a ^ { * }$ -is preferred to $b ^ { * }$ at least as much as c-is preferred $\tan d ^ { * , * }$

Analogously to $\succsim { } ^ { * }$ and $\sim ^ { \ast }$ are the asymmetric and the symmetric part of $\succsim ^ { \ast }$ ;

\- given $\mathbf { r } { \in } { \mathcal { T } } _ { \mathcal { G } } ,$ a partial preorder ${ \succsim } _ { \bf r } 0 { \bf n } A ^ { R }$ , whose meaning is: for $a ^ { * } , b ^ { * } \in A ^ { R } ,$

$a ^ { * } \succsim b \Leftrightarrow { ^ { * } a } ^ { * }$ is at least as good as $b ^ { * }$ with respect to subcriterion $G _ { \mathbf { r } } . \mathbf { \dot { \Omega } }$

Analogously to $\succsim _ { \mathbf { r } }$ and $\sim _ { \mathbf { r } }$ are the asymmetric and the symmetric part of $\succsim$

\- given r $\yen 123,456$ a partial preorder ${ \succsim } _ { \mathbf { r } } ^ { * }$ on $\mathring { A ^ { R } } \times A ^ { R }$ , whose meaning is: for $a ^ { * } , b ^ { * } , c ^ { * } , d ^ { * } \in A ^ { R }$

$( a ^ { * } , b ^ { * } ) { \succsim } _ { \mathbf { r } } ^ { * } ( c ^ { * } , d ^ { * } ) { \iff } ^ { * } a ^ { * }$ is preferred to $b ^ { * }$ at least as much as $c ^ { * }$ is preferred to dwith respect to subcriterion $G _ { \mathbf { r } } "$

Analogously to $\succeq , \succ _ { \mathbf { r } } ^ { * }$ and $\sim _ { \bf r } ^ { \ast }$ are the asymmetric and the symmetric part of $\succsim _ { \mathbf { r } } ^ { * } .$

An additive value function is called compatible if it is able to restore the preference information supplied by the DM. Therefore, an additive value function (1) is compatible if it satis<sup>fi</sup>es the following set of linear constraints:

$$
\left. \begin{array} {l} U (a ^ {*}) > U (b ^ {*}) + \text {if} a ^ {*} \succ b ^ {*} \\ U (a ^ {*}) = U (b ^ {*}) \text {if} a ^ {*} \sim b ^ {*} \\ U (a ^ {*}) - U (b ^ {*}) > U (c ^ {*}) - U (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \succ^ {*} (c ^ {*}, d ^ {*}) \\ U (a ^ {*}) - U (b ^ {*}) = U (c ^ {*}) - U (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) > U _ {\mathbf {r}} (b ^ {*}) \text {if} a ^ {*} \succ_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) = U _ {\mathbf {r}} (b ^ {*}) \text {if} a ^ {*} \sim_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) > U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \succ_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) = U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k} \Big) - u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k - 1} \Big) \geq 0,   \forall \mathbf {t} \in E L,   k = 2,..., m _ {\mathbf {t}} \Big (A ^ {R} \Big) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {1} \Big) \geq 0,   u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}} (A ^ {R})} \Big) \leq u _ {\mathbf {t}} \big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}} \big),   \forall \mathbf {t} \in E L \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {0} \Big) = 0,   \forall \mathbf {t} \in E L \\ \sum_ {\mathbf {t} \in E L} u _ {\mathbf {t}} \big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}} \big) = 1. \\ \end{array} \right\} \mathrm{a} ^ {*}, b ^ {*}, c ^ {*}, d ^ {*} \in A ^ {R}, \mathbb {r} \in \mathcal {I} _ {\mathcal {G}} \setminus E L \\ \left(E ^ {A ^ {R}}\right)
$$

where, $x _ { \mathbf { t } } ^ { 0 } = m i n _ { a \in A } \ g _ { \mathbf { t } } ( a )$ , and $x _ { \mathfrak { t } } ^ { m _ { \mathfrak { t } } } = m a x _ { a \in A } ~ g _ { \mathfrak { t } } ( a ) ; ~ x _ { \mathfrak { t } } ^ { k } { \in } X _ { \mathfrak { t } } \Big ( A ^ { R } \Big ) , k = 1 , . . . , m _ { \mathfrak { t } } \Big ( A ^ { R } \Big )$ , with $X _ { \mathbf { t } } \Big ( A ^ { R } \Big ) \subseteq X _ { \mathbf { t } }$ , is the set of all different evaluations of reference alternatives from $A ^ { R }$ on elementary subcriteria $g _ { \mathbf { t } } , \mathbf { t } { \in } E L$ , and $m _ { \mathbf { t } } \mathopen { } \mathclose \bgroup \left( A ^ { R } \aftergroup \egroup \right) = \mathopen { } \mathclose \bgroup \left| X _ { \mathbf { t } } \mathopen { } \mathclose \bgroup \left( A ^ { R } \aftergroup \egroup \right) \aftergroup \egroup \right|$ . The values $x _ { \mathrm { t } } ^ { k ^ { ^ { \prime } } } , k = 1 , . . . , m _ { \mathrm { t } } \Big ( A ^ { R } \Big )$ , are increasingly ordered, i.e.,

$$
\chi_ {\mathbf {t}} ^ {1} <   \chi_ {\mathbf {t}} ^ {2} <   \dots <   \chi_ {\mathbf {t}} ^ {m _ {\mathbf {t}} (A ^ {R}) - 1} <   \chi_ {\mathbf {t}} ^ {m _ {\mathbf {t}} (A ^ {R})}.
$$

In order to check the existence of a compatible value function, one has to transform <sup>fi</sup>rst the strict inequalities of $E ^ { A ^ { R } }$ by adding an auxiliary variable ε. Then, we have to solve the following linear programming problem where the variables are the marginal value functions $u _ { \mathbf { t } } \left( x _ { \mathbf { t } } ^ { k } \right)$ $k = 1 , . . . , m _ { \mathrm { { t } } } \left( A ^ { R } \right)$ , and $u _ { \mathbf { t } } ( x _ { \mathbf { t } } ^ { m _ { \mathbf { t } } } )$ ; t∈EL, as well as ε :

maximize ε, subject to the constraints:

$$
\left. \begin{array} {l} U (a ^ {*}) \geq U (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ b ^ {*} \\ U (a ^ {*}) = U (b ^ {*}) \text {if} a ^ {*} \sim b ^ {*} \\ U (a ^ {*}) - U (b ^ {*}) \geq U (c ^ {*}) - U (d ^ {*}) + \varepsilon \text {if} (a ^ {*}, b ^ {*}) \succ^ {*} (c ^ {*}, d ^ {*}) \\ U (a ^ {*}) - U (b ^ {*}) = U (c ^ {*}) - U (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) \geq U _ {\mathbf {r}} (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) = U _ {\mathbf {r}} (b ^ {*}) \text {if} a ^ {*} \sim_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) \geq U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) + \varepsilon \text {if} (a ^ {*}, b ^ {*}) \succ_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) = U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k} \Big) - u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k - 1} \Big) \geq 0,   \forall \mathbf {t} \in E L,   k = 2,..., m _ {\mathbf {t}} \Big (A ^ {R} \Big) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {1} \Big) \geq 0,   u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}} (A ^ {R})} \Big) \leq u _ {\mathbf {t}} \big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}} \big),   \forall \mathbf {t} \in E L \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {0} \Big) = 0,   \forall \mathbf {t} \in E L \\ \sum_ {\mathbf {t} \in E L} u _ {\mathbf {t}} (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}}) = 1. \\ \end{array} \right\}
$$

If $\varepsilon ( E ^ { A ^ { R ^ { \prime } } } ) > 0 ,$ , where $\varepsilon ( E ^ { A ^ { R ^ { \prime } } } ) = m a x \varepsilon , s . t .$ . constraints $E ^ { A ^ { R ^ { \prime } } }$ , then there exists at least one compatible value function $U ( \cdot ) ;$ if instead ε $\lbrack E ^ { A ^ { R ^ { \prime } } } ) { \leq } 0 ,$ , then there does not exist any compatible value function $U ( \cdot )$ . Supposing that there exists at least one compatible value function, each of these functions may induce a different ranking on the whole set $A ;$ for this reason the ROR methods, (see $\begin{array} { r } { [ 1 3 , 8 , 1 5 , 1 2 , 1 1 , 1 ] ) } \end{array}$ , do not take into consideration only one compatible value function but all the compatible value functions simultaneously (we shall denote the set of all compatible value functions by $\mathcal { U } )$ Application on the ROR involves the following de<sup>fi</sup>nitions:

De<sup>fi</sup>nition 3.1. Given two alternatives $a , b \in A .$ , we say that a is weakly necessarily preferred to $b ,$ and we write $a \succsim { ^ N b } ,$ , if a is at least as good as b for all compatible value functions:

$$
a \succeq^ {N} b \Longleftrightarrow U (a) \geq U (b) \forall U \in \mathcal {U}.
$$

De<sup>fi</sup>nition 3.2. Given two alternatives $a , b \in A ,$ , we say that a is weakly possibly preferred to b, and we write $a \succsim { ^ P b }$ , if a is at least as good as b for at least one compatible value function:

$$
a \succeq^ {P} b \Longleftrightarrow \exists U \in \mathcal {U}: U (a) \geq U (b).
$$

De<sup>fi</sup>nition 3.3. Given two alternatives $a , b \in A ,$ , we say that a is weakly necessarily preferred to b with respect to subcriterion $G _ { \mathbf { r } } , \mathbf { r } { \in } { \mathcal { T } } _ { \mathcal { G } } \setminus E L ,$ , and we write $a { \boldsymbol { \gtrsim } } _ { \mathbf { r } } ^ { N } b$ , if a is at least as good as b with respect to subcriterion $G _ { \mathbf { r } }$ for all compatible value functions:

$$
a \succeq_ {\mathbf {r}} ^ {N} b \Longleftrightarrow U _ {\mathbf {r}} (a) \geq U _ {\mathbf {r}} (b) \forall U \in \mathcal {U}.
$$

De<sup>fi</sup>nition 3.4. Given two alternatives $a , b \in A ,$ , we say that a is weakly possibly preferred to b with respect to criterion $G _ { \mathbf { r } } , \mathbf { r } { \in } { \mathcal { T } } _ { \mathcal { G } } \setminus E L$ , and we write $a \succeq _ { \mathrm { r } } ^ { P } b$ , if a is at least as good as b with respect to criterion $G _ { \mathbf { r } }$ for at least one compatible value function:

$$
a \succeq_ {\mathbf {r}} ^ {P} b \Longleftrightarrow \exists U \in \mathcal {U}: U _ {\mathbf {r}} (a) \geq U _ {\mathbf {r}} (b).
$$

Note that for r∈EL, we have:

$$
\succsim_ {r} ^ {N} = \succsim_ {r} ^ {P} = \{(a, b) \in A \times A: g _ {r} (a) \geq g _ {r} (b) \}
$$

Let us remark that we need both the possible and the necessary preference relations $\succsim { } ^ { P }$ and $\succsim$ . In fact, considering the necessary preference relation $\succsim ^ { N }$ only, we loose some important information given by the ROR methodology. For example, for $a , b \in A ,$ , let us consider the two following cases:

Case 1). $a \succsim { N } _ { b }$ and $b \succsim { } ^ { P } a ,$

Case 2). $a \succsim { ^ N b }$ and $b \mathcal { Z } ^ { P } a .$

In both, case 1) and case 2), ∀U∈ , $U ( a ) { \geq } U ( b )$ . However, in case 1) there is at least one compatible value function U∈ such that $U ( b ) { \geq } U ( a )$ while this does not happen in case 2). If we consider only the necessary preference relation $\succsim ^ { N }$ we are not able to distinguish case 1) from case 2), while, this is not the case if we use also the possible preference relatior $\succcurlyeq { P } .$

Necessary weak preference relations $( \succcurlyeq ^ { N }$ and $\succsim _ { \mathbf { r } } ^ { N } )$ , and possible weak preference relations $( \succcurlyeq ^ { P }$ and ${ \boldsymbol { \gtrsim } } _ { \mathbf { r } } ^ { P } )$ can be calculated as follows. For all alternatives $a , b \in A ,$ , let $X _ { \mathbf { t } } \Big ( A ^ { R } \cup \{ a , b \} \Big ) \subseteq X _ { \mathbf { t } }$ be the set of all different evaluations of alternatives from $A ^ { R } \cup \{ a , b \}$ on criterion $g _ { \mathbf { t } } , \mathbf { t } { \in } E L$ , and $m _ { \mathbf { t } } \Bigl ( A ^ { R } \cup \{ a , b \} \Bigr ) = | X _ { \mathbf { t } } \Bigl ( A ^ { R } \cup \{ a , b \} \Bigr )$ . The values $x _ { \mathbf { t } } ^ { k } { \in } X _ { \mathbf { t } } { \Bigl ( } A ^ { R } { \cup } \{ a , b \} { \Bigr ) } , k { \mathrm { = } } 1 , { \ldots } , m _ { \mathbf { t } } { \Bigl ( } A ^ { R } { \cup } \{ a , b \} { \Bigr ) }$ , are increasingly ordered, i.e.,

$$
\chi_ {\mathbf {t}} ^ {1} <   \chi_ {\mathbf {t}} ^ {2} <   \dots <   \chi_ {\mathbf {t}} ^ {m _ {\mathbf {t}} \left(A ^ {R} \cup \{a, b \}\right) - 1} <   \chi_ {\mathbf {t}} ^ {m _ {\mathbf {t}} \left(A ^ {R} \cup \{a, b \}\right)}.
$$

Then, the characteristic points of $u _ { \mathbf { t } } ( \cdot ) , \mathbf { t } { \in } E L$ , are in x<sup>0</sup>; $x _ { \mathbf { t } } ^ { k } , k = 1 , . . . , m _ { \mathbf { t } } \Big ( \boldsymbol { A } ^ { R } \cup \{ a , b \} \Big ) , x _ { \mathbf { t } } ^ { m _ { \mathbf { t } } }$

Let us consider the following ordinal regression constraints $E ( \boldsymbol { a } , \boldsymbol { b } )$ , with $u _ { \mathbf { t } } \left( x _ { \mathbf { t } } ^ { k } \right)$ , t∈EL; $k = 1 , . . . , m _ { \mathrm { t } } \bigl ( A ^ { R } \cup \{ a , b \} \bigr ) , ~ u _ { \mathrm { t } } \bigl ( x _ { \mathrm { t } } ^ { m _ { \mathrm { t } } } \bigr )$ ; t∈EL, and ε as variables:

$$
\left. \begin{array} {l} U (a ^ {*}) \geq U (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ b ^ {*} \\ U (a ^ {*}) = U (b ^ {*}) \text {if} a ^ {*} \sim b ^ {*} \\ U (a ^ {*}) - U (b ^ {*}) \geq U (c ^ {*}) - U (d ^ {*}) + \varepsilon \text {if} (a ^ {*}, b ^ {*}) \succ^ {*} (c ^ {*}, d ^ {*}) \\ U (a ^ {*}) - U (b ^ {*}) = U (c ^ {*}) - U (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) \geq U _ {\mathbf {r}} (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) = U _ {\mathbf {r}} (b ^ {*}) \text {if} a ^ {*} \sim_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) \geq U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) + \varepsilon \text {if} (a ^ {*}, b ^ {*}) \succ_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) = U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k} \Big) - u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k - 1} \Big) \geq 0,   \mathbf {t} \in E L,   k = 2,..., m _ {\mathbf {t}} \Big (A ^ {R} \cup \{a, b \} \Big) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {1} \Big) \geq 0,   u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}} (A ^ {R})} \Big) \leq u _ {\mathbf {t}} \big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}} \big),   \mathbf {t} \in E L \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {0} \Big) = 0,   \mathbf {t} \in E L \\ \sum_ {\mathbf {t} \in E L} u _ {\mathbf {t}} \big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}} \big) = 1. \\ \end{array} \right\}
$$

The above constraints depend also on the pair of alternatives $a , b \in A$ because their evaluations $g _ { \mathbf { t } } ( a )$ and $g _ { \mathbf { t } } ( b )$ give coordinates for two of $m _ { \mathrm { t } } \big ( A ^ { R } \cup \{ a , b \} \big )$ characteristic points of marginal value function $u _ { \mathbf { t } } ( \cdot )$ , for each t∈EL.

For all $a , b \in A ,$ , and $\mathbf { r } { \in } { \mathcal { T } } { \mathcal { G } } \setminus E L$ , let us consider the following sets of constraints:

$$
\left. \begin{array}{l} U (b) \geq U (a) + \varepsilon \\ E (a, b) \end{array} \right\} \Big (E ^ {N} (a, b) \Big), \qquad \left. \begin{array}{l} U (a) \geq U (b) \\ E (a, b) \end{array} \right\} \Big (E ^ {P} (a, b) \Big), \qquad \left. \begin{array}{l} U _ {\mathbf {r}} (b) \geq U _ {\mathbf {r}} (a) + \varepsilon \\ E (a, b) \end{array} \right\} \Big (E _ {\mathbf {r}} ^ {N} (a, b) \Big), \qquad \left. \begin{array}{l} U _ {\mathbf {r}} (a) \geq U _ {\mathbf {r}} (b) \\ E (a, b) \end{array} \right\} \Big (E _ {\mathbf {r}} ^ {P} (a, b) \Big).
$$

If ${ \cal E } ^ { N } ( a , b ) , { \cal E } ^ { P } ( a , b ) , { \cal E } _ { \bf r } ^ { N } ( a , b )$ , and $E _ { \mathbf { r } } ^ { P } ( a , b )$ are not empty, then

$\bullet \ a \succeq { } ^ { N } b \Longleftrightarrow \mathrm { i f } \ E ^ { N } \left( a , b \right)$ is infeasible or $\varepsilon ^ { N } \left( a , b \right) \leq 0 ,$ , where $\varepsilon ^ { N } \left( a , b \right) = \operatorname* { m a x } { \varepsilon } , 5 . \mathrm { t } .$ constraints $E ^ { N } \left( a , b \right)$

$a \succeq ^ { P } b \Leftarrow \mathrm { i f } \ : E ^ { P } \left( a , b \right)$ is feasible and $\varepsilon ^ { P } \left( a , b \right) > 0 ,$ , where $\varepsilon ^ { P } \left( a , b \right) = \operatorname* { m a x } \varepsilon ,$ s.t. constraints $E ^ { P } \left( a , b \right)$

$a \gtrsim _ { r } ^ { N } b \Longleftrightarrow \mathrm { i f } \ E _ { \mathrm { r } } ^ { N } ( a , b )$ is infeasible or $\varepsilon _ { \mathrm { r } } ^ { N } ( a , b ) { \leq } 0$ , where $\varepsilon _ { \mathrm { r } } ^ { N } ( a , b ) = \operatorname* { m a x } { \varepsilon } , 5 . \mathrm { t } .$ constraints $E _ { \mathrm { r } } ^ { N } ( a , b ) ;$

$a \gtrsim _ { r } ^ { P } b \Longleftrightarrow \mathrm { i f } \ E _ { \mathrm { r } } ^ { P } ( a , b )$ is feasible and $\varepsilon _ { \mathrm { r } } ^ { P } ( a , b ) { > } 0$ , where $\varepsilon _ { \mathrm { r } } ^ { P } ( a , b ) = \operatorname* { m a x } \varepsilon ,$ s. t. constraints $E _ { \mathrm { r } } ^ { P } ( a , b )$

## 4. Properties of necessary and possible preference relations

$a \succsim { ^ N b }$ or $b \succ ^ { P } a , \forall a , b \in A ; [ 9 ]$

The necessary and possible preference relations satisfy some interesting properties presented in the following propositions:

$a \succsim { ^ N b }$ and $b \succsim { ^ P C } ,$ then $a \ge ^ { P } c , \forall a , b , c \in A ; [ 8 ]$

$a \succsim { ^ P b }$ and $b \succsim ^ { N } c$ , then $a \ge ^ { P } c , \forall a , b , c \in A . \left[ 8 \right]$

## Proposition 4.1.

In case of the hierarchy of criteria, some further properties hold, as showed by the following proposition.

$\gtrsim ^ { N } \subseteq \gtrsim ^ { P } ; [ 9 ]$

Proposition 4.2. For every $\mathbf { r } { \in } { \mathcal { T } } _ { \mathcal { G } }$

$\succsim { } ^ { N } \mathrm { i } s \mathrm { ~ a ~ }$ partial preorder (i.e. re<sup>fl</sup>exive and transitive); [9] $\succsim { } ^ { P }$ is strongly complete (i.e. for all $a , b \in A , \ a \gtrsim ^ { P } b$ or $b \succsim { } ^ { P } a )$ and negatively transitive; [9]

1. $\succeq _ { \mathbf { r } } ^ { N } \subseteq \succeq _ { \mathbf { r } } ^ { P } ;$

2. $\succeq _ { \mathbf { r } } ^ { N }$ is a partial preorder (i.e. re<sup>fl</sup>exive and transitive);

3. ${ \boldsymbol { \succ } } _ { \mathbf { r } } ^ { P }$ is strongly complete (i.e. for all $a , b { \in } A , \ a { \ge } _ { \mathbf { r } } ^ { P } b$ or $b { \succeq } _ { \mathbf { r } } ^ { P } a )$ and negatively transitive;

1. Given two alternatives $a , b \in A ,$

4. $a { \scriptscriptstyle \gtrsim } _ { \mathrm { r } } ^ { N } b$ or $b { \gtrsim } _ { \mathbf { r } } ^ { P } a , \forall a , b { \in } A ;$

$$
a \gtrsim_ {(\mathbf {r}, j)} ^ {N} b \forall j = 1, \dots , n (\mathbf {r}) \Rightarrow a \gtrsim_ {\mathbf {r}} ^ {N} b;
$$

5. $a { \scriptscriptstyle \gtrsim } _ { \mathrm { r } } ^ { N } b$ and $b { \approx } _ { \mathbf { r } } ^ { P } c ,$ then $a { \gtrsim } _ { \mathbf { r } } ^ { P } c , \forall a , b , c { \in } A ;$

6. $a { \scriptscriptstyle \gtrsim } _ { \mathrm { r } } ^ { P } b$ and $b { \approx } _ { \mathbf { r } } ^ { N } c ,$ then $a \approx _ { \mathbf { r } } ^ { P } c , \forall a , b , c \in A .$

2. Given two alternatives $a , b \in A$ such that:

$$
\alpha) a \succeq_ {(\mathbf {r}, j)} ^ {N} b, \forall j \in \{1, \dots , n (\mathbf {r}) \} \backslash \{w \}
$$

Proof. See Appendix A.

Let us observe that if we consider the comprehensive preference represented by the value function U at a “zero” level of the hierarchy, where $\mathbf { r } = 0 ,$ , we can consider Proposition (1) as a speci<sup>fi</sup>c case of Proposition (2), e.g., we can write $\stackrel { \cdot } { \sim } \frac { N } { 0 } \subseteq \stackrel { \cdot } { \sim } \frac { P } { 0 }$ instead of $\succsim { \mathbb { N } } _ { \subseteq } \succsim { \mathbb { P } } .$ The next proposition presents some results which are speci<sup>fi</sup>c for the ROR in case of the hierarchy of criteria.

$$
\beta) a \succ_ {(\mathbf {r}, w)} ^ {P} b,
$$

then $a { \boldsymbol { \gtrsim } } _ { \mathbf { r } } ^ { P } b$

3. Given two alternatives $a , b \in A$

$$
a \not \gtrsim_ {(\mathbf {r}, j)} ^ {P} b \forall j \in \{1, \dots , n (\mathbf {r}) \} \Rightarrow a \not \gtrsim_ {\mathbf {r}} ^ {P} b.
$$

Proposition 4.3. For every r∈ $\tau _ { \mathcal { G } } \setminus E L ,$

Proof. See Appendix A. □

## 5. Intensity of preference and a representative value function

## 5.1. Intensity of preference

As in the GRIP method [8], also in case of the hierarchy of criteria it is possible to de<sup>fi</sup>ne quaternary relation $\succcurlyeq { \mathbf { \Phi } ^ { * ^ { N } } } , \succcurlyeq { \mathbf { \Phi } ^ { * ^ { P } } } , \succcurlyeq _ { \mathbf { t } } ^ { \aleph ^ { N } }$ and ${ \boldsymbol { \gtrsim } _ { \mathbf { t } } ^ { * ^ { P } } } ,$ , t∈EL, related to intensity of preference, as follows:

\- for each $a , b , c , d \in A$ , we say that a is necessarily preferred to b at least as strongly as c is preferred to d, and we write $( a , b ) \succsim \ast ^ { N } ( c , d )$ , if a is preferred to b at least as strongly as c is preferred to d for all compatible value functions:

$$
(a, b) \succeq^ {N} (c, d) \Longleftrightarrow U (a) - U (b) \geq U (c) - U (d), \forall U \in \mathcal {U};
$$

\- for each $a , b , c , d \in A ,$ we say that a is possibly preferred to b at least as strongly as c is preferred to d, and we write $( a , b ) \succsim \ast ^ { P } ( c , d )$ , if a is preferred to b at least as strongly as c is preferred to d for at least one compatible value function:

$$
(a, b) \succeq^ {* ^ {P}} (c, d) \Longleftrightarrow \exists U \in \mathcal {U}: U (a) - U (b) \geq U (c) - U (d);
$$

\- for each $a , b , c , d \in A ,$ , we say that a is necessarily preferred to b at least as strongly as c is preferred to d with respect to elementary subcriterion $g _ { \mathbf { t } } ,$ , and we write $( a , b ) { \succeq } _ { \bf t } ^ { * ^ { N } } ( c , \bar { d } )$ , if a is preferred to b at least as strongly as c is preferred to d with respect to $g _ { \mathrm { t } }$ for all compatible value functions:

$$
(a, b) \gtrsim_ {\mathbf {t}} ^ {* N} (c, d) \Longleftrightarrow u _ {\mathbf {t}} (a) - u _ {\mathbf {t}} (b) \geq u _ {\mathbf {t}} (c) - u _ {\mathbf {t}} (d), \forall U \in \mathcal {U};
$$

\- for each a $, b , c , d \in A ,$ , we say that a is possibly preferred to b at least as strongly as c is preferred to d with respect to elementary subcriterion $\boldsymbol { \mathrm { \varepsilon } } _ { g _ { \mathrm { t } } }$ , and we write $( a , b ) { \stackrel { } { \sim } } _ { \bf t } ^ { * ^ { r } } ( c , d )$ , if a is preferred to b at least as strongly as c is preferred to d with respect to $g _ { \mathrm { t } }$ for at least one compatible value function:

$$
(a, b) \gtrsim_ {\mathbf {t}} ^ {* P} (c, d) \Longleftrightarrow \exists U \in \mathcal {U}: u _ {\mathbf {t}} (a) - u _ {\mathbf {t}} (b) \geq u _ {\mathbf {t}} (c) - u _ {\mathbf {t}} (d).
$$

In case of the hierarchy of criteria, we can further consider quaternary relations ${ \succeq _ { \mathbf { r } } } ^ { * ^ { N } }$ and ${ \boldsymbol { \gtrsim } _ { \mathbf { r } } ^ { * } } ^ { P }$ , related to intensity of preference with respect to subcriterion $G _ { \mathbf { r } } { \in } \mathcal { G }$ at an intermediate level of the hierarchy, as follows:

\- for each $a , b , c , d { \in } A$ , and for each $\mathbf { r } { \in } { \mathcal { T } } _ { \mathcal { G } } ,$ , we say that a is necessarily preferred to b at least as strongly as c is preferred to d with respect to subcriterion $G _ { \mathbf { r } } ,$ and we write $( a , b ) { \succeq } _ { \bf r } ^ { * ^ { N } } ( c , d )$ , if a is preferred to b at least as strongly as c is preferred to d with respect to subcriterion $G _ { \mathbf { r } }$ for all compatible value functions

$$
(a, b) \succeq_ {\mathbf {r}} ^ {* N} (c, d) \Longleftrightarrow U _ {\mathbf {r}} (a) - U _ {\mathbf {r}} (b) \geq U _ {\mathbf {r}} (c) - U _ {\mathbf {r}} (d), \forall U \in \mathcal {U};
$$

\- for each $a , b , c , d \in A ,$ , and for each $\mathbf { r } { \in } \mathbb { Z } _ { \mathcal { G } } ,$ , we say that a is possibly preferred to b at least as strongly as c is preferred to d with respect to subcriterion $G _ { \mathbf { r } } ,$ and we write $( a , b ) { \succsim } _ { \bf r } ^ { * ^ { N } } ( c , d )$ , if a is preferred to b at least as strongly as c is preferred to d with respect to subcriterion $G _ { \mathbf { r } }$ for at <sup>ð Þ</sup>least one compatible value function:

$$
(a, b) \succeq_ {\mathbf {r}} ^ {* P} (c, d) \Longleftrightarrow \exists U \in \mathcal {U}: U _ {\mathbf {r}} (a) - U _ {\mathbf {r}} (b) \geq U _ {\mathbf {r}} (c) - U _ {\mathbf {r}} (d).
$$

Observe that quaternary relations ${ \sucgtrsim } _ { \mathbf { t } } ^ { * ^ { N } }$ and $\boldsymbol { \gtrsim } _ { \mathbf { t } } ^ { * ^ { P } } , \mathbf { t } { \in } \boldsymbol { E } L$ , are a particular case of quaternary relations ${ \succeq _ { \mathbf { r } } } ^ { * ^ { N } }$ and ${ \boldsymbol { \gtrsim } } _ { \mathbf { r } } ^ { * ^ { P } } , \mathbf { r } { \in } \boldsymbol { \mp } _ { \mathcal { G } } ,$ in case r EL Quaternary relations $\succcurlyeq \ast ^ { N }$ and $\succcurlyeq { \mathbf { \Phi } ^ { * } } ^ { P } , \succcurlyeq { \mathbf { \Phi } _ { \mathbf { r } } ^ { * } } ^ { N }$ and ${ \boldsymbol { \gtrsim } } _ { \mathbf { r } } ^ { * ^ { r } }$ , and $\succeq _ { \mathbf { t } } ^ { \ast ^ { N } }$ and ${ \succeq } _ { \mathbf { t } } ^ { * ^ { N } }$ <sup>IG</sup>can be computed as follows. For all alternatives $a , b , c , d \in A ,$ let $X _ { \mathbf { t } } \Big ( A ^ { R } \cup \{ a , b , c , d \} \Big ) \subseteq X _ { \mathbf { t } }$ be the set of all different evaluations of alternatives from $A ^ { R } \cup \{ a , b , c , d \}$ on elementary subcriterion $g _ { \mathbf { t } } , \mathbf { t } { \in } E L$ , and $m _ { \mathrm { t } } \Bigl ( A ^ { R } \cup \{ a , b , c , d \} \Bigr ) = | X _ { \mathrm { t } } \Bigl ( A ^ { R } \cup \{ a , b , c , d \} \Bigr )$ . The values $x _ { \mathfrak { t } } ^ { k } \in X _ { \mathfrak { t } } \Bigl ( A ^ { R } \cup \{ a , b , c , d \} \Bigr ) , \quad k = 1 , . . . , m _ { \mathfrak { t } } \Bigl ( A ^ { R } \cup \{ a , b , c , d \} \Bigr )$ , are increasingly ordered, i.e.,

$$
\chi_ {\mathbf {t}} ^ {1} <   \chi_ {\mathbf {t}} ^ {2} <   \dots <   \chi_ {\mathbf {t}} ^ {m _ {\mathbf {t}} \left(A ^ {R} \cup \{a, b, c, d \}\right) - 1} <   \chi_ {\mathbf {t}} ^ {m _ {\mathbf {t}} \left(A ^ {R} \cup \{a, b, c, d \}\right)}.
$$

Then, the characteristic points of $u _ { \mathbf { t } } ( \cdot ) , \mathbf { t } { \in } E L ,$ , are in $x _ { \mathbf { t } } ^ { 0 } , x _ { \mathbf { t } } ^ { k } , k = 1 , . . . , m _ { \mathrm { t } } \Big ( A ^ { R } \cup \{ a , b , c , d \} \Big ) , x _ { \mathbf { t } } ^ { m _ { \mathrm { t } } }$

Let us consider the following ordinal regression constraints $E ( a , b , c , d ) ,$ , with

$$
\left. \begin{array} {l} U (a ^ {*}) \geq U (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ b ^ {*} \\ U (a ^ {*}) = U (b ^ {*}) \text {if} a ^ {*} \sim b ^ {*} \\ U (a ^ {*}) - U (b ^ {*}) \geq U (c ^ {*}) - U (d ^ {*}) + \varepsilon \text {if} (a ^ {*}, b ^ {*}) \succ^ {*} (c ^ {*}, d ^ {*}) \\ U (a ^ {*}) - U (b ^ {*}) = U (c ^ {*}) - U (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) \geq U _ {\mathbf {r}} (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) = U _ {\mathbf {r}} (b ^ {*}) \text {if} a ^ {*} \sim_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) \geq U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) + \varepsilon \text {if} (a ^ {*}, b ^ {*}) \succ_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) = U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k} \Big) - u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k - 1} \Big) \geq 0,   \mathbf {t} \in E L,   k = 2,..., m _ {\mathbf {t}} \big (A ^ {R} \cup \{a, b, c, d \} \big) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {1} \Big) \geq 0,   u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}} (A ^ {R} \cup \{a, b, c, d \})} \Big) \leq u _ {\mathbf {t}} (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}}),   \mathbf {t} \in E L \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {0} \Big) = 0,   \mathbf {t} \in E L \\ \sum_ {\mathbf {t} \in E L} u _ {\mathbf {t}} (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}}) = 1. \\ \end{array} \right\} a ^ {*}, b ^ {*}, c ^ {*}, d ^ {*} \in A ^ {R}, \mathbf {r} \in \mathcal {I} _ {\mathcal {G}} \setminus E L \\ (E (a, b, c, d))
$$

The above constraints depend also on the alternatives $a , b , c , d { \in } A$ because their evaluations $g _ { \mathbf { t } } ( a ) , g _ { \mathbf { t } } ( b ) , g _ { \mathbf { t } } ( c )$ and $g _ { \mathbf { t } } ( d )$ give coordinates to four of m<sub>t</sub> $\left( A ^ { R } \cup \{ a , b , c , d \} \right)$ characteristic points of marginal value function $u _ { \mathbf { t } } ( \cdot )$ , for each $\mathbf { t } { \in } E L$

For all $a , b , c , d \in A ,$ and $\mathbf { r } { \in } { \mathcal { T } } { \mathfrak { g } } \backslash E L$ , let us consider the following sets of constraints:

$$
\begin{array}{l} U (c) - U (d) \geq U (a) - U (b) + \varepsilon \\ E (a, b, c, d) \end{array} \Bigg \} \left(E ^ {N} (a, b, c, d)\right), \quad \begin{array}{l} U (a) - U (b) \geq U (c) - U (d) \\ E (a, b, c, d) \end{array} \Bigg \} \left(E ^ {P} (a, b, c, d)\right), \begin{array}{l} U _ {\mathbf {r}} (c) - U _ {\mathbf {r}} (d) \geq U _ {\mathbf {r}} (a) - U _ {\mathbf {r}} (b) + \varepsilon \\ E (a, b, c, d) \end{array} \Bigg \} \left(E _ {\mathbf {r}} ^ {N} (a, b, c, d)\right),
$$

I $\ ' E ^ { N } ( a , b , c , d )$ , and $E ^ { P } ( a , b , c , d ) , E _ { \mathbf { r } } ^ { N } ( a , b , c , d )$ and $E _ { \mathbf { r } } ^ { P } ( a , b , c , d )$ , and $E _ { \mathbf { t } } ^ { N } ( a , b , c , d )$ and $E _ { \mathbf { t } } ^ { P } ( a , b , c , d )$ are not empty, then

$( a , b ) \gtrsim \ast ^ { { \scriptscriptstyle * } } ( c , d ) \Longleftrightarrow E ^ { N } ( a , b , c , d )$ <sup>ð</sup>is infeasible or $\begin{array} { r } { \varepsilon ^ { N } \left( a , \dot { b _ { * } } c , d \right) \leq 0 , } \end{array}$ <sup>Þ</sup>where $\mathbf { \bar { \varepsilon } } ^ { N } ( a , b , c , d ) = \mathrm { m a \bar { x } }$ <sup>ð Þ</sup>ε, s.t. constraints $E ^ { N } ( a , b , c , d ) ;$

$( a , b ) \gtrsim \ast ^ { P } ( c , d ) \Longleftrightarrow \mathrm { i f } \ E ^ { P } \left( a , b , c , d \right)$ is feasible and $\varepsilon ^ { P } \left( a , b , c , d \right) > 0 ,$ , where $\varepsilon ^ { P } ( a , b , c , d ) = \operatorname* { m a x } \varepsilon ,$ s. t. constraints $E ^ { P } ( a , b , c , d ) ;$

$( a , b ) \gtrsim _ { \mathrm { r } } ^ { * ^ { N } } ( c , d ) \Longleftrightarrow \mathrm { i f } E _ { \mathrm { r } } ^ { N } \left( a , b , c , d \right)$ is infeasible or $\varepsilon _ { \mathrm { r } } ^ { N } ( a , b , c , d ) \leq 0 ,$ where $\varepsilon _ { \mathrm { r } } ^ { N } ( a , b , c , d ) = \mathrm { m a x } \varepsilon , s$ .t. constraints $E _ { \mathrm { r } } ^ { N } ( a , b , c , d ) ;$

$( a , b ) \gtrsim _ { \mathrm { r } } ^ { * ^ { P } } ( c , d ) \Longleftrightarrow \mathrm { i f } E _ { \mathrm { r } } ^ { P } \ ( a , b , c , d )$ is feasible and $\varepsilon _ { \mathrm { r } } ^ { P } ( a , b , c , d ) > 0 ,$ , where $\varepsilon _ { \mathrm { r } } ^ { P } ( a , b , c , d ) = \operatorname* { m a x } \varepsilon ,$ s.t. constraints $E _ { \mathrm { r } } ^ { P } ( a , b , c , d ) ;$

$( a , b ) \gtrsim \smash { \mathfrak { z } ^ { \ast } } ^ { N } ( c , d ) \Longleftrightarrow E _ { \mathrm { t } } ^ { N } ( a , b , c , d )$ is infeasible or $\begin{array} { r } { \varepsilon _ { \mathrm { t } } ^ { N } ( a , b , c , d ) \leq 0 , } \end{array}$ , where $\varepsilon _ { \mathrm { t } } ^ { N } ( a , b , c , d ) { = } \operatorname* { m a x } { \varepsilon } , { \mathrm { s . t . } }$ . constraints $E _ { \mathrm { t } } ^ { N } ( a , b , c , d ) ;$

$( a , b ) \gtrsim    \mathchoice { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot }  \cdot { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot }  \cdot { \cdot } { \cdot } { \cdot } { \cdot } { \cdot } { \cdot }  \cdot { \cdot } { \cdot } { \cdot } { \cdot }  \cdot { \cdot } { \cdot } { \cdot } { \cdot }  \cdot { \cdot } { \cdot } { \cdot } { \cdot \cdot } { \cdot }  \cdot { \cdot } { \cdot } { \cdot } { \cdot \cdot }  \cdot { } \cdot { \cdot } { \cdot } { \cdot \cdot }  \cdot  $ is feasible and $\varepsilon _ { \mathrm { t } } ^ { P } ( a , b , c , d ) > 0 ,$ where $\varepsilon _ { \mathrm { t } } ^ { P } ( a , b , c , d ) = \operatorname* { m a x } \varepsilon ,$ s.t. constraints $E _ { \mathrm { t } } ^ { P } ( a , b , c , d ) .$

Most of the properties of quaternary relations $\succcurlyeq { \mathbf { \Phi } ^ { * ^ { N } } \mathbf { a n d } } \geq \mathbf { \Phi } ^ { * ^ { P } } , \succeq _ { \mathbf { r } } ^ { * ^ { N } }$ and ${ \boldsymbol { \gtrsim } _ { \mathbf { r } } ^ { * } } ^ { P }$ , and $\succcurlyeq _ { \mathbf { t } } ^ { * ^ { N } }$ and $\succcurlyeq _ { \mathbf { t } } ^ { * ^ { N } }$ are the same of those of the GRIP method presented in [8]. However, there are some properties speci<sup>fi</sup>c to the case of the hierarchy of criteria, which are presented in the following proposition.

Proposition 5.1. For all r $\equiv \mathcal { T } _ { \mathcal { G } } \backslash E L$

1. Given four alternatives $a , b , c , d \in A $

$$
(a, b) \gtrsim_ {(\mathbf {r}, j)} ^ {* N} (c, d), \forall j = 1,..., n (\mathbf {r}) \Rightarrow (a, b) \gtrsim_ {\mathbf {r}} ^ {* N} (c, d);
$$

2. Given four alternatives $a , b , c , d \in A$ such that:

(a) $( a , b ) \boldsymbol { \gtrsim } _ { ( \mathbf { r } , j ) } ^ { * ^ { N } } ( c , d ) \quad \forall j \in \{ 1 , . . . , n ( \mathbf { r } ) \} \backslash \{ w \} ,$

(b) $( a , b ) { \mathop { \left/ { \sum _ { ( { \bf r } , w ) } } \right.}  } ( c , d )$

then $( a , b ) { \succsim } _ { \bf r } ^ { * ^ { P } } ( c , d ) ;$

<sup>ð Þ ð Þ</sup>3. Given four alternatives $a , b , c , d \in A $

$$
(a, b) \not \prec_ {(\mathbf {r}, j)} ^ {* P} (c, d) \forall j \in \{1, \dots , n (\mathbf {r}) \} \Rightarrow (a, b) \not \prec_ {\mathbf {r}} ^ {* P} (c, d).
$$

Proof. See Appendix $\begin{array}{c} \mathsf { A } , \boxed { \begin} {array} { r l } \end{array}$

## 5.2. The representative value function

The ROR in case of the hierarchy of criteria builds a set of additive value functions compatible with preference information provided by the DM and leads to two preference relations, $\succeq _ { \mathbf { r } } ^ { N }$ and $\succcurlyeq _ { \mathbf { r } } ^ { P } ,$ for each subcriterion $G _ { \mathbf { r } } , \mathbf { r } { \in } \mathcal { T } _ { \mathcal { G } } \backslash E L$ , from the hierarchy. Such preference relations answer to <sup>IG</sup>robustness concerns, since they are in general “more robust” than a preference relation determined by an arbitrarily chosen compatible value function. However, in practice, in some decision-making situations it is required to assign a score to considered alternatives. Moreover, possible and necessary preference relations may be not easy to interpret, even by a DM with some experience in MCDA. Thus, it is useful to determine a value function which represents well all the information contained in necessary and possible preference relations in an easily understandable way, For these reasons, a method for finding among all compatible value functions resulting from ROR a “representative” value function has beer proposed in [13], [19]. It is based on the principle of “one for all, all for $\tt o n e "$ , i.e. we look for one value function representing the set of al compatible value functions, and all compatible value functions contribute to de<sup>fi</sup>ne this representative value function.

In case of the hierarchy of criteria, the DM can be interested in a value function representing not only comprehensive necessary and possible preference relations, $\succsim ^ { N } \mathrm { a n d } \succ ^ { P }$ , but also necessary and possible preference relations ${ \boldsymbol { \gtrsim } } _ { \mathbf { r } } ^ { N }$ and $\scriptstyle \sum _ { \mathbf { r } } ^ { P } , \mathbf { r } \in { \mathcal { T } } _ { \mathcal { G } } \backslash E L$ , at intermediate levels. In general, the idea of the “representative value function” is to select from among compatible value functions that one which better highlights the necessary preference by maximizing the difference of values between alternatives $a , b \in A$ for which $a \succ ^ { N } b$ , i.e. $a \succsim { ^ N b }$ and $b { \mathcal { Z } } ^ { N } a$ . As secondary objective, one can consider minimizing the difference of values between alternatives $a , b \in A$ for which $a { \varkappa } ^ { N } b$ and $b \mathcal { Z } ^ { N } a .$ . In case of the hierarchy of criteria one can imagine that the DM gives a sequence of criteria $G _ { \mathbf { r } _ { 1 } } , . . . , G _ { \mathbf { r } _ { f } } { \in } \mathcal { G } ,$ , ordered with respect to his/her interest. In this case, the representative value function is the one <sup>G</sup>maximizing the difference of values between alternatives $a , b \in A$ for which $a { \succ } _ { \mathbf { r } _ { i } } ^ { N } b$ , and minimizing the difference of values between alternatives a, $b \in A$ for which $a { \scriptscriptstyle \mathscr { Z } } _ { { \bf r } _ { i } } ^ { N } b$ and $b \mathcal { Z } _ { \mathbf { r } _ { i } } ^ { N } a ,$ , starting from the most interesting subcriterion $G _ { \mathbf { r } _ { 1 } }$ and proceeding in the above sequence until subcriterion $G _ { \mathbf { r } _ { f } }$ . In this way, the discrimination power of the “representative value function” is maximal for the most interesting subcriterion $G _ { \mathbf { r } _ { 1 } }$ , and it is decreasing, step by step, until subcriterion $G _ { \mathbf { r } _ { f } }$ . Summing up, the “representative” value function can be found via the following procedure:

1. Consider the set of constraints $E ^ { A }$ including constraints representing preference information provided by the DM, and monotonicity constraints on marginal value functions $u _ { \mathbf { t } } ( \cdot )$ ; t∈EL, whose characteristic point correspond to all different evaluations of alternatives from set A (and not onl from the reference subset $A ^ { R } \subseteq A )$ on particular elementary criteria:

$$
\left. \begin{array} {l}U (a ^ {*}) \geq U (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ b ^ {*} \\ U (a ^ {*}) = U (b ^ {*}) \text {if} a ^ {*} \sim b ^ {*} \\ U (a ^ {*}) - U (b ^ {*}) \geq U (c ^ {*}) - U (d ^ {*}) + \varepsilon \text {if} (a ^ {*}, b ^ {*}) \succ^ {*} (c ^ {*}, d ^ {*}) \\ U (a ^ {*}) - U (b ^ {*}) = U (c ^ {*}) - U (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) \geq U _ {\mathbf {r}} (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) = U _ {\mathbf {r}} (b ^ {*}) \text {if} a ^ {*} \sim_ {\mathbf {r}} b ^ {*} \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) \geq U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) + \varepsilon \text {if} (a ^ {*}, b ^ {*}) \succ_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ U _ {\mathbf {r}} (a ^ {*}) - U _ {\mathbf {r}} (b ^ {*}) = U _ {\mathbf {r}} (c ^ {*}) - U _ {\mathbf {r}} (d ^ {*}) \text {if} (a ^ {*}, b ^ {*}) \sim_ {\mathbf {r}} ^ {*} (c ^ {*}, d ^ {*}) \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k} \Big) - u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {k - 1} \Big) \geq 0,   \forall \mathbf {t} \in E L, k = 1,..., m _ {\mathbf {t}} \\ u _ {\mathbf {t}} \Big (x _ {\mathbf {t}} ^ {0} \Big) = 0,   \forall \mathbf {t} \in E L \\ \sum_ {\mathbf {t} \in E L} u _ {\mathbf {t}} (x _ {\mathbf {t}} ^ {m _ {\mathbf {t}}}) = 1, \\ \end{array} \right\} \mathrm{a} ^ {*}, b ^ {*}, c ^ {*}, d ^ {*} \in A ^ {R}, \mathbf {r} \in \mathcal {I} _ {\mathcal {G}} \setminus E L, \\ \left(E ^ {A}\right)
$$

where, $x _ { \mathbf { t } } ^ { 0 } = m i n _ { a \in A } ~ g _ { \mathbf { t } } ( a )$ , and $x _ { \mathbf { t } } ^ { m _ { \mathrm { t } } } = m a x _ { a \in A } g _ { \mathbf { t } } ( a ) ; x _ { \mathbf { t } } ^ { k } { \in } X _ { \mathbf { t } } , k = 0 , . . . , m _ { \mathrm { t } } ,$ with $X _ { \mathbf { t } }$ the set of all different evaluations of alternatives from A on elementary subcriteria $g _ { \mathbf { t } }$ ; t∈EL. The values $x _ { \mathbf { t } } ^ { k } , k = 0 , . . . , m _ { \mathbf { t } } ,$ , are increasingly ordered, $\mathrm { i . e . }$

$$
\chi_ {\mathbf {t}} ^ {1} <   \chi_ {\mathbf {t}} ^ {2} <   \dots <   \chi_ {\mathbf {t}} ^ {m _ {\mathbf {t}} - 1} <   \chi_ {\mathbf {t}} ^ {m _ {\mathbf {t}}}.
$$

2. Calculate $\varepsilon ^ { * } = m a x \varepsilon ,$ s.t. $E ^ { A } . \mathrm { I f } \varepsilon ^ { \ast } > 0 ,$ , then there exists at least one value function satisfying constraints of $E ^ { A } ,$ , so go to step $3 . \mathrm { I f } \varepsilon ^ { \ast } \leq 0$ , then there is no value function satisfying $E ^ { A } ,$ , which means that the information provided by the DM cannot be faithfully represented by any additive value function. If the DM accepts to work with not fully compatible value functions, then go to step 3; if the DM decides to remove a part of preference information causing the incompatibility, then after this removal (see Section 7), go to step 3,

$$
3. i = 1; E = E ^ {A},
$$

4. Determine the necessary preference relation ${ \boldsymbol { \gtrsim } } _ { \mathbf { r } _ { i } } ^ { N }$ and the possible preference relation ${ \boldsymbol { \gtrsim } } _ { \mathbf { r } _ { i } } ^ { P }$ with respect to subcriterion $G _ { r _ { i } } { \in } { \mathcal { G } } ,$ , considering the sets of constraints:

$$
\left. \begin{array}{l} U _ {\mathbf {r} _ {i}} (b) \geq U _ {\mathbf {r} _ {i}} (a) + \varepsilon \\ E ^ {A} \end{array} \right\} \Big (E _ {\mathbf {r} _ {i}} ^ {N} (a, b) \Big), \qquad \left. \begin{array}{l} U _ {\mathbf {r} _ {i}} (a) \geq U _ {\mathbf {r} _ {i}} (b) \\ E ^ {A} \end{array} \right\} \Big (E _ {\mathbf {r} _ {i}} ^ {P} (a, b) \Big).
$$

$a { \scriptscriptstyle \approx } _ { { \bf r } _ { i } } ^ { N } b { \scriptscriptstyle \Leftrightarrow }$ the set $E _ { \mathbf { r } _ { i } } ^ { N } ( a , b )$ is infeasible or $\varepsilon _ { \mathbf { r } _ { i } } ^ { * , N } { \le } 0$ , where $\varepsilon _ { \mathbf { r } _ { i } } ^ { * , N } = m a x \varepsilon ,$ s.t. constraints $E _ { \mathbf { r } _ { i } } ^ { N } ( a , b )$

$a { \scriptscriptstyle \gtrsim } _ { \mathbf { r } _ { i } } ^ { \scriptscriptstyle \vec { P } } b { \Longleftrightarrow } E _ { \mathbf { r } _ { i } } ^ { P } ( a , b )$ is infeasible and $\begin{array} { r } { \varepsilon _ { \mathbf { r } _ { i } } ^ { * , P } > 0 , } \end{array}$ , where $\varepsilon _ { \mathbf { r } _ { i } } ^ { * , P } =$ max ε, s.t. constraints $E _ { { \bf r } _ { i } } ^ { P } ( a , b )$

<sup>ð Þ</sup> 5. For all pairs of alternatives (a, b), such that $a { \succ } _ { \mathbf { r } _ { i } } ^ { N } b ,$ <sup>¼</sup>add the following constraint to $E \colon U _ { \mathbf { r } _ { i } } ( a ) { \geq } U _ { \mathbf { r } _ { i } } ( b ) + \varepsilon _ { \mathbf { r } _ { i } } ,$ , i.e.

$$
\left.\begin{array}{l}E\\U _ {\mathbf {r} _ {i}} (a) \geq U _ {\mathbf {r} _ {i}} (b) + \varepsilon_ {\mathbf {r} _ {i}} \quad \text { if } \quad a > _ {\mathbf {r} _ {i}} ^ {N} b\end{array}\right\}\rightarrow (E)
$$

$\mathrm { i f } i = 1$ , then go to step $6 ,$ otherwise go to step $^ { 7 , }$

6. Add constraint $\varepsilon _ { \mathbf { r } _ { i } } = \varepsilon$ to E,

$$
\left.\begin{array}{l}E\\\varepsilon_ {\mathbf {r} _ {i}} = \varepsilon\end{array}\right\}\rightarrow (E)
$$

7. Maximize $\varepsilon _ { \mathbf { r } _ { i } }$ , subject to constraints E.

8. Add the constraint $\varepsilon _ { \mathbf { r } _ { i } } = \varepsilon _ { \mathbf { r } _ { i } } ^ { * }$ to E, with $\varepsilon _ { \mathbf { r } _ { i } } ^ { * } = m a x \varepsilon _ { \mathbf { r } _ { i } }$ computed in step 7,

$$
\left. \begin{array}{l} E \\ \varepsilon_ {\mathbf {r} _ {i}} = \varepsilon_ {\mathbf {r} _ {i}} ^ {*} \end{array} \right\} \to (E)
$$

$$
\left.\begin{array}{l}E\\U _ {\mathbf {r} _ {i}} (a) - U _ {\mathbf {r} _ {i}} (b) \leq \delta_ {\mathbf {r} _ {i}}\\U _ {\mathbf {r} _ {i}} (b) - U _ {\mathbf {r} _ {i}} (a) \leq \delta_ {\mathbf {r} _ {i}}\end{array}\right\} \text {if} a \not \gtrsim_ {\mathbf {r} _ {i}} ^ {N} b \text {and} b \not \gtrsim_ {\mathbf {r} _ {i}} ^ {N} a \Bigg \} \rightarrow (E)
$$

9. For all pairs of alternatives (a, b), such that $a { \scriptscriptstyle \mathcal { Z } } _ { { \bf r } _ { i } } ^ { N } b$ and $b \mathcal { Z } _ { \mathbf { r } _ { i } } ^ { N } a$ (already computed in step 4), add the following constraints to E $: U _ { \mathbf { r } _ { i } } ( a ) - U _ { \mathbf { r } _ { i } } ( b ) { \le } \delta _ { \mathbf { r } _ { i } }$ and $U _ { { \bf r } _ { i } } ( b ) - U _ { { \bf r } _ { i } } ( a ) { \le } \delta _ { { \bf r } _ { i } }$

10. Minimize $\delta _ { \mathbf { r } _ { i } } ,$ subject to constraints E.

11. Add the constraint $\delta _ { \mathbf { r } _ { i } } = \delta _ { \mathbf { r } _ { i } } ^ { * }$ to E, with $\delta _ { \mathbf { r } _ { i } } ^ { * } = m i n \delta _ { \mathbf { r } _ { i } }$ computed in step 10,

$$
\left. \begin{array}{l} E \\ \delta_ {\mathbf {r} _ {i}} = \delta_ {\mathbf {r} _ {i}} ^ {*} \end{array} \right\} \to (E)
$$

12. If ibf then go to step 4 with $i \colon = i + 1 ,$ , otherwise stop.

Observe that the above procedure takes into account the preference information given by the DM by maximizing the value of auxiliary variable ε in the <sup>fi</sup>rst iteration. This ensures that the DM's preferences are represented with a maximal discrimination possible. If the DM does not want to express a sequence of subcriteria $G _ { \mathbf { r } 1 } , . . . , G _ { \mathbf { r } _ { f } } { \in } \mathcal { G }$ , but (s)he wants to compute the representative value function considering only the comprehensively <sup>G</sup>necessary preference relation, it will be enough to perform a single iteration of the procedure described until step 10, considering i=1 and $\mathbf { r } _ { 1 } = 0 .$

Let us mention that other methods proposed for <sup>fi</sup>nding a representative value function in ordinal regression [2,3], not referring to necessary and possible preference relations, can also be adapted to the case of hierarchy of criteria.

## 6. A didactic example

In this section, we apply the procedure described in the previous sections to cope with a hierarchical multiple criteria decision problem which is very frequent in the scholar system, and in the academic sector in particular. Let us suppose that each year a faculty of natural sciences has the economic possibility to give a scholarship to one of its best students; to make the choice, the Dean is considering <sup>fi</sup>fteen students who attended the courses and passed the test of two macro subjects: Mathematics and Chemistry. Mathematics has two subsubjects: Algebra and Analysis, while Chemistry has two subsubjects: Analytical Chemistry and Organic Chemistry; each of these sub-subjects has other two sub-subjects for a total of eight elementary sub-subjects shown in Fig. 2. Using the terminology introduced in Section 2, the set of alternatives $A = \{ \mathbf { A } , \mathbf { B } , . . . , \mathbf { R } \}$ is <sup>¼ f g</sup>composed of 15 alternatives; the number of levels l=3; the set of all criteria $\mathcal { G } = \left\{ G _ { 1 } , G _ { 2 } , G _ { ( 1 , 1 ) } , G _ { ( 1 , 2 ) } , G _ { ( 2 , 1 ) } , G _ { ( 2 , 2 ) } , g _ { ( 1 , 1 , 1 ) } , g _ { ( 1 , 1 , 2 ) } , g _ { ( 1 , 2 , 1 ) } , \right.$ g , g ,g , g ,g } is composed of criteria and subcriteria whose names are given in Fig. 2; the set of indices of all criteria is 1; 2, (1, 1), (1, 2), (2, 1), (2, 2), (1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)}; the number of <sup>fi</sup>rst level criteria $m = 2 ;$ if we consider $G _ { \mathbf { r } } = G _ { 1 }$ then $n ( \mathbf { r } ) = 2 ,$ , while if we consider $G _ { \mathbf { r } } = G _ { ( 1 , 1 ) }$ then $n ( ( 1 , 1 ) ) = 2 ;$ g<sub>(1, 1, 1)</sub>, g<sub>(1, 1, 2)</sub>, g<sub>(1, 2, 1)</sub>, g , g ,g , g ,g are the elementary subcriteria; the set of indices of elementary subcriteria is $E L = \{ ( 1 , 1 , 1 ) , ( 1 , 1 , 2 )$ (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2,2,1),(2,2,2); if we consider $G _ { \mathbf { r } } = G _ { 1 }$ then $E ( G _ { ( 1 ) } ) = \{ ( 1 , 1 , 1 ) , ( 1 , 1 , 2 ) , ( 1 , 2 , 1 ) , ( 1 , 2 , 2 ) \}$ while if we consider $G _ { \mathbf { r } } =$ $G _ { ( 2 , 1 ) }$ then $E ( G _ { ( 2 , 1 ) } ) = \{ ( 2 , 1 , 1 ) , ( 2 , 1 , 2 ) \}$

![](/api/attachments/N5N69CTB/fulltext/images/8f96f4e278f5088445fe861d7ea2b04ffc7d14714b0db384510635060763e0e7.jpg)  
Fig. 2. Hierarchical structure of criteria

Evaluations of students on the eight elementary subcriteria.

<table><tr><td>Student\subcriteria</td><td> $g_{(1,1,1)}$ </td><td> $g_{(1,1,2)}$ </td><td> $g_{(1,2,1)}$ </td><td> $g_{(1,2,2)}$ </td><td> $g_{(2,1,1)}$ </td><td> $g_{(2,1,2)}$ </td><td> $g_{(2,2,1)}$ </td><td> $g_{(2,2,2)}$ </td></tr><tr><td>A</td><td>Very bad</td><td>Very good</td><td>Very bad</td><td>Good</td><td>Very good</td><td>Very good</td><td>Very bad</td><td>Bad</td></tr><tr><td>B</td><td>Bad</td><td>Very good</td><td>Medium</td><td>Very good</td><td>Very bad</td><td>Bad</td><td>Very bad</td><td>Very bad</td></tr><tr><td>C</td><td>Very good</td><td>Medium</td><td>Medium</td><td>Very bad</td><td>Very good</td><td>Good</td><td>Bad</td><td>Medium</td></tr><tr><td>D</td><td>Medium</td><td>Very bad</td><td>Bad</td><td>Very bad</td><td>Very bad</td><td>Bad</td><td>Medium</td><td>Very bad</td></tr><tr><td>E</td><td>Very good</td><td>Very good</td><td>Medium</td><td>Medium</td><td>Bad</td><td>Very good</td><td>Bad</td><td>Very bad</td></tr><tr><td>F</td><td>Good</td><td>Bad</td><td>Bad</td><td>Medium</td><td>Very bad</td><td>Very bad</td><td>Very good</td><td>Very good</td></tr><tr><td>H</td><td>Medium</td><td>Very bad</td><td>Bad</td><td>Bad</td><td>Very good</td><td>Very bad</td><td>Very bad</td><td>Very bad</td></tr><tr><td>I</td><td>Good</td><td>Good</td><td>Good</td><td>Medium</td><td>Medium</td><td>Bad</td><td>Good</td><td>Very bad</td></tr><tr><td>L</td><td>Good</td><td>Very bad</td><td>Bad</td><td>Good</td><td>Good</td><td>Very bad</td><td>Very good</td><td>Good</td></tr><tr><td>M</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Bad</td><td>Medium</td><td>Medium</td><td>Very good</td><td>Good</td></tr><tr><td>N</td><td>Good</td><td>Bad</td><td>Very good</td><td>Medium</td><td>Bad</td><td>Very good</td><td>Very good</td><td>Medium</td></tr><tr><td>O</td><td>Good</td><td>Medium</td><td>Bad</td><td>Bad</td><td>Medium</td><td>Bad</td><td>Very good</td><td>Very bad</td></tr><tr><td>P</td><td>Bad</td><td>Very bad</td><td>Bad</td><td>Medium</td><td>Bad</td><td>Very good</td><td>Medium</td><td>Very bad</td></tr><tr><td>Q</td><td>Very good</td><td>Very good</td><td>Medium</td><td>Very bad</td><td>Bad</td><td>Medium</td><td>Medium</td><td>Bad</td></tr><tr><td>R</td><td>Good</td><td>Good</td><td>Bad</td><td>Very bad</td><td>Bad</td><td>Bad</td><td>Medium</td><td>Medium</td></tr></table>

![](/api/attachments/N5N69CTB/fulltext/images/45b6c64dd2f2ec57ac270e32a84667a013fa403372677c80289aba83097e4bb6.jpg)  
Fig. 3. Dominance relation in the set of students.

<sup>Þ</sup>As it was declared in Section 2, the students are evaluated directly on the elementary subcriteria only, and thus, they are evaluated with respect to the eight elementary sub-subjects; these evaluations are shown in Table 1. Each elementary subcriterion has <sup>fi</sup>ve qualitative levels of evaluation that go from very bad to very good, increasingly ordered.

The only comprehensive relation that comes out from the problem formulation is the dominance relation in the set of students, shown in Fig. 3. The dominance relation does not take into account the preferences of the Dean and, moreover, it leaves too many students incomparable. For this reason, the Dean decides to use the ROR approach adapted to the hierarchical structure of criteria.

The Dean provides the following preference information which is then transformed to constraints of the ordinal regression problem:

1. On Chemistry, student I is preferred to student H. In order to take into consideration this preference information, it is represented in the constraints $( E ^ { A ^ { R } } )$ as follows:

$$
\begin{array}{c} U _ {2} (\mathbf {I}) > U _ {2} (\mathbf {H}) \Longleftrightarrow U _ {(2, 1)} (\mathbf {I}) + U _ {(2, 2)} (\mathbf {I}) > U _ {(2, 1)} (\mathbf {H}) + U _ {(2, 2)} (\mathbf {H}) \Longleftrightarrow \\ \Longleftrightarrow u _ {(2, 1, 1)} (\mathbf {I}) + u _ {(2, 1, 2)} (\mathbf {I}) + u _ {(2, 2, 1)} (\mathbf {I}) + u _ {(2, 2, 2)} (\mathbf {I}) > u _ {(2, 1, 1)} (\mathbf {H}) \\ + u _ {(2, 1, 2)} (\mathbf {H}) + u _ {(2, 2, 1)} (\mathbf {H}) + u _ {(2, 2, 2)} (\mathbf {H}). \end{array}
$$

Fig. 4 shows the necessary preference relation determined by this piece of preference information. In Fig. 4, the arrow from I to H is bold marked because it constitutes the part of necessary preference relation originating from the considered piece of preference information and, therefore, not present at the previous stage (dominance relation, see Fig. 3). Bold marked arrows in the following <sup>fi</sup>gures have an analogous interpretation with respect to preference information provided in further steps.

2. On Analytical Chemistry, student E is preferred to student H. This, can be modeled using the following constraint:

$$
U _ {(2, 1)} (\mathbf {E}) > U _ {(2, 1)} (\mathbf {H}) \Longleftrightarrow u _ {(2, 1, 1)} (\mathbf {E}) + u _ {(2, 1, 2)} (\mathbf {E}) > u _ {(2, 1, 1)} (\mathbf {H}) + u _ {(2, 1, 2)} (\mathbf {H}).
$$

Fig. 5 shows the necessary preference relation determined by the two pieces of preference information.

3. On Mathematics, student N is preferred to student Q. This, can be modeled using the following constraint:

$$
\begin{array}{c} U _ {1} (\mathbf {N}) > U _ {1} (\mathbf {Q}) \Longleftrightarrow U _ {(1, 1)} (\mathbf {N}) + U _ {(1, 2)} (\mathbf {N}) > U _ {(1, 1)} (\mathbf {Q}) + U _ {(1, 2)} (\mathbf {Q}) \Longleftrightarrow \\ \Longleftrightarrow u _ {(1, 1, 1)} (\mathbf {N}) + u _ {(1, 1, 2)} (\mathbf {N}) + u _ {(1, 2, 1)} (\mathbf {N}) + u _ {(1, 2, 2)} (\mathbf {N}) > u _ {(1, 1, 1)} (\mathbf {Q}) \\ + u _ {(1, 1, 2)} (\mathbf {Q}) + u _ {(1, 2, 1)} (\mathbf {Q}) + u _ {(1, 2, 2)} (\mathbf {Q}). \end{array}
$$

Fig. 6 shows the necessary preference relation determined by the three pieces of preference information.

![](/api/attachments/N5N69CTB/fulltext/images/acffb3be4bc6e7507eb6d534d8628f30a78546137092536f995608ed52601be5.jpg)  
Fig. 4. Necessary preference relation determined by the <sup>fi</sup>rst piece of preference information.

![](/api/attachments/N5N69CTB/fulltext/images/c206e816ba6791dca57b16a6467a750b8cfa9e2336f144421a091dc6fbe06f69.jpg)  
Fig. 5. Necessary preference relation determined by the two pieces of preference information.

![](/api/attachments/N5N69CTB/fulltext/images/aaa53deacdec0f17ef2dbc52cde9c47f97e459aced11592b373db2a48c55eb16.jpg)  
Fig. 6. Necessary preference relation determined by the three pieces of preference information

4. On Chemistry, student L is preferred to student P. This, can be modeled using the following constraint:

$$
\begin{array}{l} U _ {2} (\mathbf {L}) > U _ {2} (\mathbf {P}) \Longleftrightarrow U _ {(2, 1)} (\mathbf {L}) + U _ {(2, 2)} (\mathbf {L}) > U _ {(2, 1)} (\mathbf {P}) + U _ {(2, 2)} (\mathbf {P}) \Longleftrightarrow \\ \qquad \Longleftrightarrow u _ {(2, 1, 1)} (\mathbf {L}) + u _ {(2, 1, 2)} (\mathbf {L}) + u _ {(2, 2, 1)} (\mathbf {L}) + u _ {(2, 2, 2)} (\mathbf {L}) > u _ {(2, 1, 1)} (\mathbf {P}) \\ \qquad + u _ {(2, 1, 2)} (\mathbf {P}) + u _ {(2, 2, 1)} (\mathbf {P}) + u _ {(2, 2, 2)} (\mathbf {P}). \end{array}
$$

Fig. 7 shows the necessary preference relation determined by the four pieces of preference information.

In the context of the hierarchical multiple criteria evaluation, it is possible to check the necessary preference relation at intermediate levels of the hierarchy, that is we can see if student a is necessarily preferred to student b with respect to considered domain (Mathematics, Chemistry, Algebra, Analysis and so on); in Tables 2 and 3, we present the necessary preference relation with respect to macro subjects: Mathematics and Chemistry, respectively.

In Tables 2 and 3, the alternatives in italics are those for which the necessary preference relation is true at the second level but it is not true at the level below. For example, $\mathbf { L } { \boldsymbol { \gtrsim } } _ { 2 } ^ { N } \mathbf { B }$ but $\mathbf { L } ^ { \mathcal { \mathbf { N } } } _ { ( 2 , 1 ) } \mathbf { B }$

As shown in subsection 2, one can compute the representative value function, taking into account a sequence of subcriteria $G _ { \mathbf { r } _ { 1 } } , . . . , G _ { \mathbf { r } _ { f } } { \in } \mathcal { G }$ ordered with respect to the Dean's interest. Results <sup>G</sup>presented in Table 4 show the ranking of students obtained using the representative value function in three different cases:

• the Dean considers as the most important and the second most important the criteria Mathematics $\left( G _ { 1 } \right)$ and Chemistry $\left( G _ { 2 } \right) .$ respectively, and consequently, he considers the sequence of corresponding necessary preference relations $\succsim _ { 1 } ^ { N } , \succ _ { 2 } ^ { N }$ (1st and 2nd columns),

• the Dean considers as the most important and the second most important the criteria Chemistry $\left( G _ { 2 } \right)$ and Mathematics $( G _ { 1 } ) _ { 1 } $ , respectively, and consequently, he considers the sequence of corresponding necessary preference relations $\succsim _ { 2 } ^ { N } , \succsim _ { 1 } ^ { N }$ (3rd and 4th columns),

• the Dean does not discriminate criteria with respect to their importance and consequently he takes into account only the comprehensive necessary preference relation $\succsim _ { 0 } ^ { N }$ (5th column).

We can observe three important facts:

![](/api/attachments/N5N69CTB/fulltext/images/815b7e042c04aa13d34d02a7b63ea75c30d3c9eebda0fbc0186c648b42e18c0e.jpg)  
Fig. 7. Necessary preference relation determined by the four pieces of preference information.

Table 2  
Necessary preference relations for Mathematics and its subcriteria

<table><tr><td>Student\ subcriterion</td><td> $\gtrsim 1^N$ </td><td> $\gtrsim (1,1)^N$ </td><td> $\gtrsim (1,2)^N$ </td></tr><tr><td>A</td><td></td><td></td><td></td></tr><tr><td>B</td><td>A,P</td><td>A,P</td><td>A,C,D,E,F,H,L,M,O,P,Q,R</td></tr><tr><td>C</td><td>D</td><td>D,F,H,L,M,N,O,P</td><td>D,Q,R</td></tr><tr><td>D</td><td></td><td>H,P</td><td>R</td></tr><tr><td>E</td><td>C,D,F,H,M,O,P,Q,R</td><td>A,B,C,D,F,H,I,L,M,N,O,P,Q,R</td><td>C,D,F,H,M,O,P,Q,R</td></tr><tr><td>F</td><td>D,H,P</td><td>D,H,L,N,P</td><td>D,H,O,P,R</td></tr><tr><td>H</td><td>D</td><td>D,P</td><td>D,O,R</td></tr><tr><td>I</td><td>D,F,H,M,O,P,R</td><td>D,F,H,L,M,N,O,P,R</td><td>C,D,E,F,H,M,O,P,Q,R</td></tr><tr><td>L</td><td>D,H,P</td><td>D,H,P</td><td>A,D,F,H,O,P,R</td></tr><tr><td>M</td><td>D,H</td><td>D,H,P</td><td>C,D,H,O,Q,R</td></tr><tr><td>N</td><td>C,D,F,H,P,Q,R</td><td>D,F,H,L,P</td><td>C,D,E,F,H,I,M,O,P,Q,R</td></tr><tr><td>O</td><td>D,H</td><td>D,F,H,L,M,N,P</td><td>D,H,R</td></tr><tr><td>P</td><td></td><td></td><td>D,F,H,O,R</td></tr><tr><td>Q</td><td>C,D,R</td><td>A,B,C,D,E,F,H,I,L,M,N,O,P,R</td><td>C,D,R</td></tr><tr><td>R</td><td>D</td><td>D,F,H,I,L,M,N,O,P</td><td>D</td></tr></table>

\- student N is almost always the best one in the ranking obtained using different representative value functions,

\- the ranking obtained by the representative value function changes between the <sup>fi</sup>rst and the second iteration of the method,

\- the ranking obtained by the representative value function changes if we consider a different order of importance between the necessary preference relations.

## 7. Further extensions of ROR for the hierarchy of criteria

## 7.1. Infeasibility

We have seen in Section 3, that the <sup>fi</sup>rst step of ROR is to check if there exists at least one value function compatible with the preference information provided by the DM. In fact, it is possible that the information provided by the DM is such that it is not possible to <sup>fi</sup>nd a compatible additive value function. In this case, the DM, together with the analyst, can decide to continue the study while accepting to work with not fully compatible value functions, or look for sets of constraints responsible of this infeasibility (let us call them troublesome constraints), and remove them from the linear program.

Table 3  
Necessary preference relation for Chemistry and its subcriteria.

<table><tr><td>Student\ subcriterion</td><td> $\succsim_2^N$ </td><td> $\succsim_{(2,1)}^N$ </td><td> $\succsim_{(2,2)}^N$ </td></tr><tr><td>A</td><td>B,H</td><td>B,C,D,E,F,H,I,L,M,N,O,P,Q,R</td><td>B,H</td></tr><tr><td>B</td><td></td><td>D,F</td><td>H</td></tr><tr><td>C</td><td>B,H</td><td>B,D,F,H,I,L,M,O,Q,R</td><td>A,B,E,H</td></tr><tr><td>D</td><td>B</td><td>B,F</td><td>B,E,H,P</td></tr><tr><td>E</td><td>B,H</td><td>B,D,F,H,L,N,P,Q,R</td><td>B,H</td></tr><tr><td>F</td><td></td><td></td><td>A,B,C,D,E,H,I,L,M,N,O,P,Q,R</td></tr><tr><td>H</td><td></td><td>F,L</td><td>B</td></tr><tr><td>I</td><td>B,D,H</td><td>B,D,F,O,R</td><td>B,D,E,H,P</td></tr><tr><td>L</td><td>B,D,H,P</td><td>F</td><td>A,B,C,D,E,H,I,M,N,O,P,Q,R</td></tr><tr><td>M</td><td>B,D,H,I,O,Q,R</td><td>B,D,F,I,O,Q,R</td><td>A,B,C,D,E,H,I,L,N,O,P,Q,R</td></tr><tr><td>N</td><td>B,D,E,H,P,Q,R</td><td>B,D,E,F,H,L,P,Q,R</td><td>A,B,C,D,E,H,I,O,P,Q,R</td></tr><tr><td>O</td><td>B,D,H,I</td><td>B,D,F,I,R</td><td>B,D,E,H,I,P</td></tr><tr><td>P</td><td>B,D,E,H</td><td>B,D,E,F,H,L,N,Q,R</td><td>B,D,E,H</td></tr><tr><td>Q</td><td>B,D</td><td>B,D,F,R</td><td>A,B,D,E,H,P</td></tr><tr><td>R</td><td>B,D</td><td>B,D,F</td><td>A,B,C,D,E,H,P,Q</td></tr></table>

Table 4  
Ranking of students by a representative value function (in parentheses there are value of the corresponding alternatives).

<table><tr><td> $\succsim_{\mathbf{r}_{1}}^{N}=\succsim_{1}^{N}$ </td><td> $\succsim_{\mathbf{r}_{2}}^{N}=\succsim_{2}^{N}$ </td><td> $\succsim_{\mathbf{r}_{1}}^{N}=\succsim_{2}^{N}$ </td><td> $\succsim_{\mathbf{r}_{2}}^{N}=\succsim_{1}^{N}$ </td><td> $\succsim^{N}$ </td></tr><tr><td>N(0.8560)</td><td>N(0.8586)</td><td>N(1)</td><td>N(1)</td><td>M(0.8808)</td></tr><tr><td>I(0.6635)</td><td>I(0.6949)</td><td>M(0.8752)</td><td>M(0.8636)</td><td>N(0.8622)</td></tr><tr><td>E(0.6250)</td><td>E(0.6250)</td><td>L(0.7663)</td><td>L(0.7273)</td><td>F(0.6690)</td></tr><tr><td>M(0.6023)</td><td>M(0.5881)</td><td>O(0.6934)</td><td>O(0.6818)</td><td>L(0.6690)</td></tr><tr><td>Q(0.5611)</td><td>Q(0.5453)</td><td>F(0.6754)</td><td>F(0.6364)</td><td>A(0.6690)</td></tr><tr><td>F(0.5)</td><td>F(0.5)</td><td>P(0.5844)</td><td>P(0.5455)</td><td>I(0.5426)</td></tr><tr><td>L(0.5)</td><td>L(0.5)</td><td>I(0.5735)</td><td>I(0.5)</td><td>C(0.4915)</td></tr><tr><td>C(0.4773)</td><td>C(0.4590)</td><td>Q(0.4940)</td><td>Q(0.4944)</td><td>O(0.4893)</td></tr><tr><td>B(0.4630)</td><td>A(0.4572)</td><td>A(0.4875)</td><td>A(0.4489)</td><td>R(0.4654)</td></tr><tr><td>A(0.4588)</td><td>O(0.4474)</td><td>R(0.4091)</td><td>R(0.4091)</td><td>Q(0.4617)</td></tr><tr><td>O(0.4559)</td><td>B(0.4389)</td><td>E(0.4026)</td><td>E(0.3636)</td><td>P(0.4190)</td></tr><tr><td>R(0.4087)</td><td>R(0.3678)</td><td>C(0.3621)</td><td>C(0.3567)</td><td>E(0.4190)</td></tr><tr><td>P(0.25)</td><td>P(0.25)</td><td>D(0.2273)</td><td>D(0.2273)</td><td>B(0.3808)</td></tr><tr><td>H(0.1250)</td><td>H(0.125)</td><td>H(0.1934)</td><td>H(0.1818)</td><td>D(0.2117)</td></tr><tr><td>D(0.0880)</td><td>D(0.0639)</td><td>B(0.1754)</td><td>B(0.1364)</td><td>H(0.1690)</td></tr></table>

In case of the hierarchy of criteria, inconsistencies can be present at different levels of the hierarchy and for this reason, differently from [21] where all constraints translate preference information concerning the same level, the DM could be interested in removing troublesome constraints regarding a particular set of criteria/subcriteria $\big \{ G _ { \mathbf { r } _ { 1 } } , . . . , G _ { \mathbf { r } _ { \mathbf { h } } } \big \}$ . For example, considering preference information regarding students evaluated on criteria structured according to the hierarchy shown in Section 6, the DM could be interested in removing the troublesome constraints at the lowest level possible, i.e. starting by the last but one level, that is constraints regarding Algebra, Analysis, Analytical Chemistry and Organic Chemistry. Then, if it is still not suf<sup>fi</sup>cient to get feasibility of the whole set of constraints $E ^ { A ^ { R } } ,$ , one can look at the constraints of the level immediately above, that is constraints regarding Mathematics and Chemistry, and so on; in this way (s)he could examine the infeasibility going up the hierarchy of criteria. Another DM could be interested in removing troublesome constraints regarding sets of criteria from different levels, like, for example, {Mathematics, Organic Chemistry} or {Analysis, Analytical Chemistry}, or Mathematics alone, or Chemistry alone, and so on. Two important remarks concerning this procedure have to be done:

• looking for troublesome constraints among all constraints $E ^ { A ^ { R } }$ translating the full preference information provided by the DM can be seen as a particular case of the above procedure; in fact, in order to get the whole set of constraints $\dot { E ^ { A ^ { R } } } ,$ , it is suf<sup>fi</sup>cient to consider the set $\big \{ G _ { \mathbf { r } _ { 1 } } , . . . , G _ { \mathbf { r } _ { \mathbf { h } } } \big \}$ of criteria composed of all criteria from the <sup>fi</sup>rst level of the hierarchy,

• <sup>fi</sup>nding a set of troublesome constraints regarding a particular set of criteria/subcriteria could be not suf<sup>fi</sup>cient to remove the infeasibility of the whole set of constraints $E ^ { A ^ { R } } ;$ ; if it would be the case, one should continue the search and add some criterion/subcriterion to the set of criteria $\big \{ G _ { \mathbf { r } _ { 1 } } , . . . , G _ { \mathbf { r } _ { \mathbf { h } } } \big \}$ considered before in order to verify if removing troublesome constraints from the extended set is suf<sup>fi</sup>cient to make $E ^ { A ^ { R } }$ feasible.

Knowing a few or all sets of constraints causing infeasibility, if the DM would refuse to choose the one to be removed, then the analyst could suggest a certain heuristic for ordering these sets of constraints with respect to importance of the corresponding piece of preference information. For example, given a set of constraints $S = \{ C _ { 1 } , . . . , C _ { p } \}$ coming from levels $\{ h _ { 1 } , . . . , h _ { p } \}$ , respectively, one could associate to this set the number $\begin{array} { r } { H _ { S } = \big ( \sum _ { k = 1 } ^ { p } h _ { k } \big ) / p . \ H _ { S } } \end{array}$ represents an average level of <sup>¼ ¼</sup>constraints belonging to set S. Supposing that a constraint from level h is more important than the one from level $h + 1$ , one could decide to remove $S _ { i } ,$ such that $H _ { S _ { i } } { > } H _ { S _ { i } }$ for all $j \neq i ,$ that is the set having the greatest value of $H _ { S _ { i } } .$ If two sets, $S _ { i }$ and $S _ { j } ,$ would have the same score $H _ { S _ { i } } { = } H _ { S _ { i } }$ , then we could remove the one that has less constraints coming from the lowest level. In order to <sup>fi</sup>nd sets of troublesome constraints in a set of constraints translating preference information, one can proceed as shown in [21].

## 7.2. Credibility

ROR methods permit to specify incrementally the preferences of the DM, assigning them a different degree of credibility. The idea of considering a sequence of pieces of preference information ordered according to their credibility has been introduced in [9] and investigated further in [15]. More formally, the preference information given by the DM is represented as a chain of embedded preference relations $\succsim _ { 1 } \subseteq \dots \subseteq \succeq _ { n } ,$ where for each $r , s = 1 , . . . , n ,$ with $r { < } s ,$ , the preference $\succsim r$ is more credible than $\succsim s$ . If for any $t { = } 1 , . . . , n$ , we denote by $E _ { t }$ the set of constraints obtained from $\succsim _ { t }$ and by $\mathcal { U } _ { t }$ the sets of value functions compatible with the preference information of $\succsim t \cdot$ then we have $E _ { 1 } \subseteq \ldots \subseteq E _ { n }$ and $\mathcal { U } _ { 1 } \supseteq \hdots \supseteq \mathcal { U } _ { n } ,$ , and consequently $\gtrsim _ { 1 } ^ { \dot { N } } \subseteq \ldots \subseteq \gtrsim _ { n } ^ { N } ,$ and $\gtrsim _ { 1 } ^ { P } \supseteq \hdots \supseteq \gtrsim _ { n } ^ { P } ,$ <sup>U U</sup>that is the smaller the credibility of the considered preference relation $\succsim t \cdot$ the richer the necessary preference relation $\succsim _ { t } ^ { N }$ and the poorer the possible preference relation $\succsim _ { t } ^ { P } .$ In case of the hierarchy of criteria, for each subcriterion $G _ { \mathbf { r } } { \in } { \mathcal { G } } ,$ we have a sequence of nested possible preference relations $\succsim _ { \mathbf { r } , 1 } ^ { P } \supseteq \cdots \supseteq \succeq _ { \mathbf { r } , n } ^ { P }$ and a sequence of nested necessary preference relations $\succsim _ { \mathbf { r } , 1 } ^ { N } \subseteq \dots \subseteq \succeq _ { \mathbf { r } , n } ^ { N }$

## 7.3. Extreme ranking

Necessary and possible preference relations give information regarding couples of alternatives. However, it could be interesting to analyse some information related to the whole set of alternatives in terms of the best and the worst ranking position assigned to each alternative by the compatible value functions. This constitutes the extreme ranking analysis introduced in [15]. In case of the hierarchy of criteria, the extreme ranking analysis can be performed for each subcriterion $G _ { \mathbf { r } } { \in } { \mathcal { G } } .$

## 7.4. UTADIS<sup>GMS</sup>

In general, MCDA considers three types of problems:

• ranking, consisting in completely or partially ordering the alternatives from the best to the worst,

• choice, consisting in selecting a subset of the best alternatives,

• sorting, consisting in assigning the alternatives to some prede<sup>fi</sup>ned and preferentially ordered classes.

Ranking and choice problems are based on pairwise comparisons of alternatives and, therefore, they can be dealt with possible and necessary preference relations. Sorting relies instead on the intrinsic value of an alternative and not on its comparison to others. Therefore, sorting problems need speci<sup>fi</sup>c methods. Within ROR, UTADIS<sup>GMS</sup> [11] has been proposed to deal with sorting problems as follows. Given a set of pre-de<sup>fi</sup>ned classes $C _ { 1 } , C _ { 2 } , . . . , C _ { p } ,$ ordered from the worst to the best, the DM gives preference information in terms of exemplary assignments of reference alternatives to some sequences of classes, such that $a ^ { * } \to [ C _ { L ^ { D M } } ( a ^ { * } ) , C _ { R ^ { D M } } ( a ^ { * } ) ]$ , with $L ^ { D M } \le \dot { R } ^ { D M }$ , means that reference alternative a<sup>∗</sup> can be assigned to one of the classes between $C _ { L ^ { D M } } ( a ^ { * } )$ and $C _ { R ^ { D M } } ( a ^ { * } )$ . Denoting by $A ^ { R } \subseteq A$ the set of reference alternatives considered by the DM, we say that a value function U is compatible if

$$
\forall a ^ {*}, b ^ {*} \in A ^ {R}, L ^ {D M} (a ^ {*}) > R ^ {D M} (b ^ {*}) \Rightarrow U (a ^ {*}) > U (b ^ {*}).\tag{3}
$$

Denoting by the set of compatible value functions, we have that each $U { \in } U$ <sup>U</sup>assigns an alternative $a \in A$ to a sequence of classes $[ L ^ { U } ( a )$ $R ^ { U } ( a ) ]$ <sup>U</sup>, where

$$
\begin{array}{l} L ^ {U} (a) = \max \Big (\{1 \} \cup \Big \{L ^ {D M} (a ^ {*}) \colon U (a ^ {*}) \leq U (a), a ^ {*} \in A ^ {R} \Big \} \Big), \\ R ^ {U} (a) = \min \Big (\{p \} \cup \Big \{R ^ {D M} (a ^ {*}) \colon U (a ^ {*}) \geq U (a), a ^ {*} \in A ^ {R} \Big \} \Big). \end{array}
$$

Within ROR, considering the set of all compatible value functions, for each $a \in A$ one can de<sup>fi</sup>ne the possible assignment $C ^ { P } ( a )$ and the necessary assignment $C ^ { N } ( a )$ as follows:

$$
\begin{array}{l} \bullet C ^ {P} (a) = \big [ L _ {P} ^ {\mathcal {U}} (a), R _ {P} ^ {\mathcal {U}} (a) \big ] = \cup_ {U \in \mathcal {U}} \Big [ L ^ {U} (a), R ^ {U} (a) \Big ], \\ \bullet C ^ {N} (a) = \big [ L _ {N} ^ {\mathcal {U}} (a), R _ {N} ^ {\mathcal {U}} (a) \big ] = \cap_ {U \in \mathcal {U}} \Big [ L ^ {U} (a), R ^ {U} (a) \Big ]. \end{array}
$$

In case of the hierarchy of criteria, the DM can give exemplary assignments $a ^ { * } \to [ C _ { L ^ { D M } } ( a ^ { * } ) , C _ { R ^ { D M } } ( a ^ { * } ) ]$ at a comprehensive level, but (s) he can also give assignments $a ^ { * } \xrightarrow { } _ { \mathbf { r } } \bigg \lceil C _ { L _ { \mathbf { r } } ^ { D M } } ^ { \mathbf { r } } ( a ^ { * } ) , C _ { R _ { \mathbf { r } } ^ { D M } } ^ { \mathbf { r } } ( a ^ { * } ) \bigg \rceil$ with respect to each subcriterion $G _ { \mathbf { r } }$ from the hierarchy, excluding the elementary subcriteria, i.e. $\mathbf { r } { \in } { \mathcal { T } } { \mathfrak { g } } \backslash E L$

<sup>IG</sup>For example, suppose that a Dean has to evaluate students according to their scores in various subjects. He can say that student $s _ { 1 }$ is assigned comprehensively to a class between “Medium” and “Very good”, i.e. $s _ { 1 } \to [ \mathrm { M e d i u m }$ ,Very good], but he can also say that student $s _ { 2 }$ (not necessarily $s _ { 2 }$ different from $s _ { 1 } )$ is assigned to a class between “Weakly bad” and “Weakly good” with respect to Literature, i.e. $s _ { 2 } \to _ { L i t } [ \mathrm { W e a k l y }$ $\mathsf { b a d } _ { L i t }$ , Weakly $\operatorname { g o o d } _ { L i t } ] .$ The compatibility condition relative to the assignment with respect to subcriterion $G _ { \mathbf { r } } , \mathbf { r } { \in } \mathcal { T } _ { \mathcal { G } } \backslash E L$ , is as follows:

$$
\forall a ^ {*}, b ^ {*} \in A ^ {R}, L _ {\mathbf {r}} ^ {D M} (a ^ {*}) > R _ {\mathbf {r}} ^ {D M} (b ^ {*}) \Rightarrow U _ {\mathbf {r}} (a ^ {*}) > U _ {\mathbf {r}} (b ^ {*}).\tag{4}
$$

At the output, for each $a \in A ,$ besides the comprehensive possible assignments $C ^ { P } ( a )$ and the necessary assignments $C ^ { N } ( a )$ , the method gives the possible assignment $C _ { \mathbf { r } } ^ { P } ( a )$ and the necessary assignment ${ \bar { C } } _ { \mathbf { r } } ^ { N } ( a )$ for each $G _ { \mathbf { r } } , \mathbf { r } { \in } \mathcal { T } _ { \mathcal { G } } \backslash E L$ , as follows:

$$
\bullet C _ {\mathbf {r}} ^ {P} (a) = \left[ L _ {\mathbf {r}, P} ^ {\mathcal {U}} (a), R _ {\mathbf {r}, P} ^ {\mathcal {U}} (a) \right] = \cup_ {U \in \mathcal {U}} \left[ L _ {\mathbf {r}} ^ {U} (a), R _ {\mathbf {r}} ^ {U} (a) \right],
$$

$$
\bullet C _ {\mathbf {r}} ^ {N} (a) = \left[ L _ {\mathbf {r}, N} ^ {\mathcal {U}} (a), R _ {\mathbf {r}, N} ^ {\mathcal {U}} (a) \right] = \cap_ {U \in \mathcal {U}} \left[ L _ {\mathbf {r}} ^ {U} (a), R _ {\mathbf {r}} ^ {U} (a) \right],
$$

where

$$
\begin{array}{l} L _ {\mathbf {r}} ^ {U} (a) = \max \Big (\{1 \} \cup \Big \{L _ {\mathbf {r}} ^ {D M s} (a ^ {*}) \colon U _ {\mathbf {r}} (a ^ {*}) \leq U _ {\mathbf {r}} (a), a ^ {*} \in A ^ {*} \Big \} \Big), \\ R _ {\mathbf {r}} ^ {U} (a) = \min \Big (\{p \} \cup \Big \{R _ {\mathbf {r}} ^ {D M s} (a ^ {*}) \colon U _ {\mathbf {r}} (a ^ {*}) \geq U _ {\mathbf {r}} (a), a ^ {*} \in A ^ {*} \Big \} \Big). \end{array}
$$

## 7.5. Group decision

In many decision making situations there is a plurality of DMs. For example, in case of decision related to land development, a group of stakeholders with different perceptions of prede<sup>fi</sup>ned criteria has to be involved. ROR ( [10,16]) has been applied to group decision as follows. Considering a set of DMs, and a sets of pairwise comparisons provided by the DMs belonging to $\mathcal { D } ^ { ' } \subseteq \mathcal { D } ,$ for each DM $d _ { h } \in \mathcal { D } ^ { ' }$ <sup>D D</sup>we <sup>fi</sup>nd the necessary and possible preference relations $\succsim _ { h } ^ { N }$ and $\succsim _ { h } ^ { P } .$ . Then, we can represent consensus between decision makers from $\mathcal { D } ,$ de<sup>fi</sup>ning the following preference relations for all ${ \mathcal { D } } ^ { \prime } \subseteq { \mathcal { D } } ;$

• the necessary-necessary preference relation $( \succeq _ { \mathcal { D } ^ { ' } } ^ { N , N } )$ , for which a is necessarily preferred to b for all $d _ { h } { \in } { \mathcal { D } }$

<sup>D</sup>• the necessary-possibly preference relation $( \succeq _ { \mathcal { D } ^ { ' } } ^ { N , P } )$ , for which a is necessarily preferred to b for at least one $d _ { h } { \in } { \mathcal { D } } ^ { \prime }$

• the possibly-necessary preference relation $( \succeq _ { \mathcal { D } ^ { ' } } ^ { P , N } )$ , for which a is possibly preferred to b for all $d _ { h } \in \mathcal { D } ^ { ' }$

<sup>D</sup>• the possibly-possibly preference relation $( \succeq _ { \mathcal { D } ^ { ' } } ^ { P , P } )$ , for which a is possibly preferred to b for at least one $d _ { h } \in \mathcal { D } ^ { ' }$

In case of the hierarchy of criteria we can de<sup>fi</sup>ne the above four relations for each subcriterion $G _ { \mathbf { r } }$ from the hierarchy, excluding the elementary subcriteria, i.e. r∈ $\mathcal { T } _ { \mathcal { G } } \backslash E L$

## 7.6. Interacting criteria

UTA<sup>GMS</sup>, UTADIS<sup>GMS</sup> and GRIP take into account an additive value function. This model is among the most popular ones because it has the advantage of being easily manageable, and, moreover, it has a very sound axiomatic basis (see, e.g., [20,27]). However, the additive value function is not able to represent interactions among criteria. For example, consider evaluation of cars using such criteria as maximum speed, acceleration and price. In this case, there may exist a negative interaction (negative synergy) between maximum speed and acceleration because a car with a high maximum speed also has a good acceleration, so, even if each of these two criteria is very important for a DM who likes sport cars, their joint impact on reinforcement of preference of a more speedy and better accelerating car over a less speedy and worse accelerating car will be smaller than a simple addition of the impacts of the two criteria considered separately in validation of this preference relation. In the same decision problem, there may exist a positive interaction (positive synergy) between maximum speed and price because a car with a high maximum speed is usually expensive, and thus a car with a high maximum speed and relatively low price is very much appreciated. Thus, the comprehensive impact of these two criteria on the strength of preference of a more speedy and cheaper car over a less speedy and more expensive car is greater than the impact of the two criteria considered separately in validation of this preference relation. To handle the interactions among criteria, one can consider non-additive integrals, such as Choquet integral [5] and Sugeno integral [26], or an additive value, function augmented by additional components reinforcing the value when there is a positive interaction for some pairs of criteria, or penalizing the value when this interaction is negative, like in $\mathrm { U T A } ^ { G M S } – \mathrm { I N T }$ [17]. In case of the hierarchy of criteria we can consider interaction among criteria at each level of the hierarchy. For example, evaluating students we can have negative synergy (redundancy) for Mathematics and Physics (because, in general, good students in Mathematics are good also in Physics) and positive synergy for Algebra and Analysis at a lower level (because Algebra and Analysis require different aptitudes, and therefore a student good in Algebra is not always good in Analysis).

## 8. Conclusions

In this paper, in order to deal with one important issue of Multiple Criteria Decision Aiding (MCDA), that is the hierarchy of criteria, we proposed a new methodology called Multiple Criteria Hierarchy Process (MCHP). The basic idea of MCHP relies on consideration of preference relations regarding subcriteria at each level of the hierarchy of criteria, obtaining in this way a better insight into the problem at hand. MCHP can be applied to any MCDA method. In this paper, we considered the case where evaluations of alternatives are aggregated by a value function, and we applied MCHP to one particular MCDA methodology that is the Robust Ordinal Regression (ROR). In this case, the preference model is the entire set of general additive value functions compatible with preference information given by the Decision Maker (DM) in terms of pairwise comparisons of some alternatives, and in terms of intensity of preference with respect to some pairs of alternatives. The advantage is twofold:

• from the point of view of preference information, the hierarchy of criteria is enriching the possibility of the DM to express his/her preferences: in fact, the DM can give preference information at a comprehensive level, e.g., student $s _ { 1 }$ is comprehensively preferred to student $s _ { 2 } ,$ as well as at an intermediate level with respect to subcriteria, e.g., student $s _ { 1 }$ is preferred to student s<sub>2</sub> on a subset of criteria related to Mathematics;

• with respect to decision support, taking into account the hierarchy of criteria permits to de<sup>fi</sup>ne possible and necessary preference relations not only at a comprehensive level but also at each intermediate level of the hierarchy: in fact, as a <sup>fi</sup>nal result, we can have not only that student $s _ { 1 }$ is comprehensively necessarily preferred to student $s _ { 2 } ,$ and student $s _ { 3 }$ is comprehensively possibly preferred to student $s _ { 4 } ,$ but also that, $\mathrm { e . g . , }$ student $s _ { 1 }$ is necessarily preferred to student $s _ { 2 }$ on a subset of criteria related to Mathematics, and $s _ { 3 }$ is possibly preferred to student $s _ { 4 }$ on criteria related to Organic Chemistry.

Adapting ROR to the hierarchy of criteria, i.e. putting together MCHP and ROR, gives a very powerful methodology of Multiple Criteria Decision Aiding: in fact, in this way we conjugate, on one hand, the robustness concerns by taking into account the set of all value functions compatible with preference information supplied by DM, and, on the other hand, the bene<sup>fi</sup>ts of the hierarchical decomposition of a complex multiple criteria decision problem. We have shown, moreover, that all the methodological developments proposed within the ROR can be used in the case of the hierarchy of criteria: calculation of a representative value function, consideration of different credibilities of preference information, extreme ranking analysis, application to sorting problems, group decision, handling interaction among criteria. Let us observe that we can consider preference relations referring to a subset of criteria also if there is no explicit hierarchy in the set of criteria. In fact, for any subset of criteria $\mathcal { T } ,$ the DM can always express preferences of the type “a is preferred to b with respect to $\mathcal { T } ^ { \mathfrak { n } }$ , as well as we can de<sup>fi</sup>ne necessary and <sup>J</sup>possible preference relations with respect to $\mathcal { I } .$

<sup>J</sup>We envisage three further methodological developments of the ROR adapted to the case of the hierarchy of criteria:

• consideration of imprecise evaluations on speci<sup>fi</sup>c criteria;

• consideration of the outranking preference models;

• consideration of a structure of criteria more complex than the hierarchy de<sup>fi</sup>ned in this paper: for example, while in this paper we assume that each subcriterion descends from only one criterion located at the upper level of the hierarchy tree, we can have a real situation where one subcriterion descends from more than one criterion of the upper level; for example, in case of evaluation of students at a scienti<sup>fi</sup>c faculty, Analytic Mechanics can descend from both Mathematics and Physics; we also plan to deal with more complex criteria structures, like those considered in Analytical Network Process (ANP) [23].

## Acknowledgment

The third author wishes to acknowledge the <sup>fi</sup>nancial support from the Polish National Science Centre, grant no. NN519 441939.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at doi:10. 1016/j.dss.2012.03.004.

## References

[1] S. Angilella, S. Greco, B. Matarazzo, Non-additive robust ordinal regression: a multiple criteria decision model based on the Choquet integral, European Journal of Operational Research 201 (1) (2010) 277–288.

[2] M. Beuthe, G. Scannella, Comparative analysis of UTA multicriteria methods, European Journal of Operational Research 130 (2) (2001) 246–262

[3] G. Bous, P. Fortemps, F. Glineur, M. Pirlot, ACUTA: a novel method for eliciting additive value functions on the basis of holistic preference statements, European Journal of Operational Research 206 (2) (2010) 435–444.

[4] A. Charnes, W.W. Cooper, R. Ferguson, Optimal estimation of executive compensation by linear programming, Management Science 1 (2) (1955) 138–151.

[5] G. Choquet, Theory of capacities, Annales de l'institut Fourier 5 (1954) 131–295.

[6] S. Damart, L.C. Dias, V. Mousseau, Supporting groups in sorting decisions: methodology and use of a multi-criteria aggregation/disaggregation DSS Decision Support Systems 43 (4) (2007) 1464–1475.

[7] J. Figueira, S. Greco, M. Ehrgott, Multiple Criteria Decision Analysis: State of the Art Surveys, Springer, Berlin, 2005.

[8] J.R. Figueira, S. Greco, R. Słowiński, Building a set of additive value functions representing a reference preorder and intensities of preference: GRIP method, European Journal of Operational Research 195 (2) (2009) 460–486.

[9] S. Greco, V. Mousseau, R. Słowiński, Ordinal regression revisited: multiple criteria ranking using a set of additive value functions, European Journal of Operational Research 191 (2) (2008) 416–436.

[10] S. Greco, V. Mousseau, R. Słowiński, The possible and the necessary for multiple criteria group decision, in: F. Rossi, A. Tsoukias (Eds.), Algorithmic Decision Theory (ADT 2009), LNAI 5783, Springer, Berlin, 2009, pp. 203–214.

[11] S. Greco, V. Mousseau, R. Słowiński, Multiple criteria sorting with a set of additive value functions, European Journal of Operational Research 207 (3) (2010) 1455–1470.

[12] S. Greco, R. Słowiński, V. Mousseau, J. Figueira, Robust ordinal regression, in: M. Ehrgott, J. Figueira, S. Greco (Eds.), Trends in Multiple Criteria Decision Analysis, Springer, New York, 2010, pp. 241–283.

[13] S. Greco, M. Kadziński, R. Słowiński, Selection of a representative value function in robust multiple criteria sorting, Computers and Operations Research 38 (2011) 1620–1637.

[14] S. Greco, M. Kadziński, V. Mousseau, R. Słowiński, ELECTRE<sup>GKMS</sup>: Robust ordinal regression for outranking methods, European Journal of Operational Research 214 (1) (2011) 118-135.

[15] M. Kadziński, S. Greco, R. Słowiński, Extreme ranking analysis in robust ordinal regression, Omega 40 (4) (2012) 488–501.

[16] S. Greco, M. Kadziński, V. Mousseau, R. Słowiński, Robust Ordinal Regression for multiple criteria group decision: UTA<sup>GMS</sup>-GROUP and UTADIS<sup>GMS</sup>-GROUP, Decision Support Systems 52 (3) (2012) 549–561.

[17] S. Greco, V. Mousseau, R. Słowiński, UTA<sup>GMS</sup>–INT: Robust Ordinal Regression for Value Functions Handling Interacting Criteria, Technical report, Laboratoire Génie Industriel, Ecole Centrale Paris, February 2012.

[18] E. Jacquet-Lagreze, J. Siskos, Assessing a set of additive utility functions for multicriteria decision-making, the UTA method, European Journal of Operational Research 10 (2) (1982) 151–164.

[19] M. Kadziński, S. Greco, R. Słowiński, Selection of a representative value function in robust multiple criteria ranking and choice, European Journal of Operational Research 217 (3) (2012) 541-553.

[20] R.L. Keeney, H. Raiffa, Decisions with multiple objectives: preferences and value tradeoffs, J. Wiley, New York, 1976.

[21] V. Mousseau, J. Figueira, L. Dias, C. Gomes da Silva, J. Climaco, Resolving inconsistencies among constraints on the parameters of an MCDA model, European Journal of Operational Research 147 (1) (2003) 72–93.

[22] D. Pekelman, S.K. Sen, Mathematical programming models for the determination of attribute weights, Management Science 20 (8) (1974) 1217–1229.

[23] T.L. Saaty, The analytic hierarchy and analytic network processes for the measurement of intangible criteria and for decision-making, in: J. Figueira, S. Greco, M. Ehrgott (Eds.), Multiple Criteria Decision Analysis: State of the Art Surveys, Springer, Berlin, 2005, pp. 345–382.

[24] V. Srinivasan, A.D. Shocker, Estimating the weights for multiple attributes in a composite criterion using pairwise judgments. Psychometrika 38 (4) (1973) 473–493.

[25] V. Srinivasan, A.D. Shocker, Linear programming techniques for multidimensional analysis of preferences. Psychometrika 38 (3)(1973) 337–369.

[26] M. Sugeno, Theory of fuzzy integrals and its applications, Tokyo Institute of Technology, 1974.

[27] P.P. Wakker, Additive representations of preferences: a new foundation of decision analysis, volume 4, Springer, Berlin, 1989.

[28] F.W. Young, J. De Leeuw, Y. Takane, Regression with qualitative and quantitative variables: an alternating least squares with optimal scaling features, Psychome trika 41 (4) (1976) 505–529.

![](/api/attachments/N5N69CTB/fulltext/images/20af2d7fc7ba2f383b514e03cf8dc74d6e7bc2ed497bfef495fee1a8bc708a6f.jpg)

Salvatore Corrente has received a Bachelor degree in Applied Mathematics in 2005, and a Master degree in Mathematics in 2008, both from the University of Catania. He is a third year PhD Student in Applied Mathematics at the Department of Economics and Business at the University of Catania. His research interests concern, in particular, Decision Theory and Multiple Criteria Decision Making.

![](/api/attachments/N5N69CTB/fulltext/images/dbb0ee71ce021fb43fab3e36f54ebcc12a6cd2f0efd7b4d99f3ea75dcec8cbb7.jpg)

Salvatore Greco received Master degree in Economics from the Faculty of Economics of the University of Catania in 1988. He has been assistant researcher at the Faculty of Economics of the University of Catania since 1994, associate professor since 1998 and full professor since 2001. His main research interests are in multiple criteria decision analysis and preference modeling, particularly, with the use of rough set theory. He used rough set theory as a framework for decision rule induction from a set of decision examples provided by a decision maker. He has been invited professor at the Poznan University of Technology, at the University of Paris Dauphine and at Ecole Centrale Paris. He co-edited a collection of state-of-

the-art reference surveys in multiple criteria decision analysis, published by Springer in 2005 and 2010.  
![](/api/attachments/N5N69CTB/fulltext/images/1eed16378a5781f4cb3020951feb389a0dd242ec8f796b9a76939e974a0fb40b.jpg)

Roman Słowiński is Professor and Founding Head of the Laboratory of Intelligent Decision Support Systems within the Institute of Computing Science, Poznan University of Technology. As member of the Polish Academy of Sciences (PAS), he is currently president of the Poznan Branch of the PAS. His area of expertise covers Multiple Criteria Decision Aiding, preference modeling, rough set theory, granular computing and knowledge discovery. Author or co-author of 14 books and more than 200 papers in major scienti<sup>fi</sup>c journals. Laureate of the EURO Gold Medal (1991), and Doctor Honoris Causa of Polytech' Mons (2000), University of Paris Dauphine (2001) and Technical University of Crete (2008). He holds, moreover, the

Edgeworth-Pareto Award, by International Society on Multiple Criteria Decision Making (1997) and the 2005 Prize of the Foundation for Polish Science, regarded as the most prestigious scienti<sup>fi</sup>c award in Poland. Since 1999, he is editor-in-chief of the European Journal of Operational Research. Senior Member of the IEEE.
