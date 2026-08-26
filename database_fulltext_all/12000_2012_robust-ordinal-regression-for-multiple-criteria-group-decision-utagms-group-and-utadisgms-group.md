---
otero_id: 12000
otero_key: "45YHJSBG"
title: "Robust ordinal regression for multiple criteria group decision: UTAGMS-GROUP and UTADISGMS-GROUP"
authors: "Salvatore Greco; Miłosz Kadziński; Vincent Mousseau; Roman Słowiński"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.10.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Robust ordinal regression for multiple criteria group decision: UTA<sup>GMS</sup>-GROUP and UTADIS<sup>GMS</sup>-GROUP

Salvatore Greco <sup>a</sup>, Miłosz Kadziński <sup>b,</sup>⁎, Vincent Mousseau <sup>c</sup>, Roman Słowiński <sup>b,d</sup>

<sup>a</sup> Faculty of Economics, University of Catania, Corso Italia, 55, 95129 Catania, Italy

<sup>b</sup> Institute of Computing Science, Poznań University of Technology, 60-965 Poznań, Poland

<sup>c</sup> Laboratoire Génie Industriel, Ecole Centrale Paris, Grande Voie des Vignes, 92 295 Châtenay-Malabry Cedex, France

<sup>d</sup> Systems Research Institute, Polish Academy of Sciences, 01-447 Warsaw, Poland

## a r t i c l e i n f o

Article history: Received 11 February 2011 Received in revised form 23 July 2011 Accepted 4 October 2011 Available online 12 October 2011

Keywords: Robust ordinal regression Group decision Additive value function Compromise Inconsistency resolution Decision Desktop Decision making

## a b s t r a c t

We introduce the principle of robust ordinal regression to multiple criteria group decision, and we present two new methods using a set of additive value functions as a preference model, called UTA<sup>GMS</sup>-GROUP and UTADIS<sup>GMS</sup>-GROUP. With respect to the set of decision makers (DMs), we consider two levels of certainty for the results. The <sup>fi</sup>rst level is related to the necessary or possible consequences of indirect preference information provided by each DM, whereas the other refers to the subset of DMs agreeing for a speci<sup>fi</sup>c outcome. In this way, we investigate spaces of consensus and disagreement between the DMs. The proposed methods are illustrated by examples showing how they can support real-world group decision.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Multiple criteria aggregation model aims at aggregating vector evaluations of alternatives in a way consistent with the value system of the decision maker (DM). It induces a preference structure in a set of alternatives A, and, therefore, it is also called preference model. Its subsequent proper exploitation permits to arrive at a <sup>fi</sup>nal recommendation, which is proposed to the DM. In this paper, preferences of the DMs on a set of alternatives will be modeled with the use of the Multi-Attribute Utility Theory (MAUT) [18]. The purpose of MAUT is to represent these preferences by an overall value (utility) function $U ( a ) = U ( g _ { 1 } ( a ) , . . . , g _ { m } ( a ) ) \colon \mathcal { R } ^ { m }  \mathcal { R } .$ . The comprehensive value of an alternative serves as an index used to decide the position in the ranking, or presence in the subset of the best alternatives, or the assignment into one of prede<sup>fi</sup>ned and ordered classes. The simplest form of the value function is the additive form. It is important to stress that its use involves compensation between criteria, which are all reduced and expressed in the same unit, and requires rather strong assumption about mutual independence in the sense of preference, which is often dif<sup>fi</sup>cult to met (see [5,18]). However, as noted in [25], these requirements do not pose signi<sup>fi</sup>cant problems in a posteriori analysis. Moreover, additive value functions are appreciated by the MCDA community for an easy interpretation of numerical scores of alternatives, as well as for possibility of aggregating quantitative and qualitative evaluations.

Using additive value functions requires speci<sup>fi</sup>cation of the parameters related to the formulation of marginal value functions $u _ { j } ( g _ { j } ( a ) )$ , $j = 1 , . . . , m$ . These parameters follow either directly or indirectly from preference information provided by the DM. Recently, MCDA methods based on indirect preference information and on the disaggregation–aggregation (or regression) paradigm [14] are considered more interesting. It is the case, because they require less cognitive effort from the DM in answering questions concerning her/his preferences. The philosophy underlying the disaggregation–aggregation paradigm is to <sup>fi</sup>nd a mathematical model able to reproduce exemplary decisions of the DM. Precisely, the DM provides some holistic judgments on a set of reference alternatives $A ^ { R } \subseteq A ,$ , and from this information the parameters of a decision model are induced using a methodology called ordinal regression (see [26]). The ordinal regression consists in the resolution of mathematical programs in order to infer compatible instances of a considered preference model, which restore the exemplary decisions for reference alternatives. It has been used for at least <sup>fi</sup>fty years in the <sup>fi</sup>eld of multidimensional analysis. Historically, it has been <sup>fi</sup>rst applied within MAUT to assess weights of an additive linear value function [27], and then to assess parameters of an additive piece-wise linear value function [13]. The latter method, called UTA, initiated a stream of further developments, in both theory and applications [25].

We say that an instance of a preference model is compatible with preference information given by the DM, if it is able to restore her/ his holistic judgments. Usually, among many consistent instances of a preference model, only one speci<sup>fi</sup>c instance is considered to give a recommendation. Since its choice is rather dif<sup>fi</sup>cult and arbitrary to a large extent, robust ordinal regression has been proposed recently with the aim of taking into account all compatible instances of a preference models [9]. The <sup>fi</sup>rst robust ordinal regression method has been the generalization of the UTA method, called $\mathrm { U T A } ^ { \mathrm { G M S } }$ [6]. In $\mathrm { U T A } ^ { \mathrm { G M S } }$ , instead of only one compatible additive value function composed of piecewise-linear marginal functions, all compatible additive value functions composed of general monotonic marginal value functions are taken into account. Further, this approach has been extended in the UTADIS<sup>GMS</sup> method to deal with sorting problems [8], and in ELECTRE<sup>GKMS</sup>, which is a general scheme implementing robust ordinal regression to outranking methods [10]. Robust ordinal regression has also been applied to preference model based on Choquet integral in order to handle interaction among criteria [1].

The family of methods based on robust ordinal regression has been originally designed to deal with preferences expressed by a single DM. However, it is group decision-making that is among the most important and frequently encountered processes within companies and organizations [3,29,31]. Typical examples of such problems can be found in management and business, e.g., evaluation of consumer preferences, personnel selection, or allocation of priorities to projects (see, e.g., [12]).

In this paper, we present in detail the principle of robust ordinal regression for group decision. Its <sup>fi</sup>rst general idea has been introduced in [7]. Precisely, we consider the multiple criteria decision methods to which robust ordinal regression has been originally applied, and we propose corresponding methods which deal with preferences expressed by a set of DMs. We focus on methods employing a set of additive value functions as the preference model, and present ${ \mathrm { U T A } } ^ { \mathrm { G M S } } .$ -GROUP and UTADIS<sup>GMS</sup>-GROUP. These methods permit several DMs to cooperate in view of making a collective decision: $\mathrm { U T A } ^ { \mathrm { G M S } } \mathrm { - G R O U P } \mathrm { ~ - ~ } a$ choice and ranking decision, and $\mathrm { U T A D I S } ^ { \mathrm { G M S } } .$ GROUP — a sorting decision. For each DM who expresses her/his individual preference information we use the respective GMS method, and check whether the necessary and the possible relations or assignments hold for either at least one, or for all DMs. The collective results account for the preferences expressed by each DM. However, we avoid discussions of DMs on technical parameters, and rather consider two levels of certainty for the results. The <sup>fi</sup>rst one is related to the consequences of preference information provided by each DM on the outcome. The other involves the subset of DMs agreeing for a speci<sup>fi</sup>c outcome. Thus, we reason in terms of necessary and possible outcomes and coalitions of DMs, and we arrive at four types of results:

• necessary–necessary, i.e. result con<sup>fi</sup>rmed by all compatible instances of the preference model for all DMs;

• necessary–possible, i.e. result con<sup>fi</sup>rmed by all compatible instances of the preference model for at least one DM;

• possible–necessary, i.e. result con<sup>fi</sup>rmed by at least one compatible instance of the preference model for all DMs;

• possible–possible, i.e. result con<sup>fi</sup>rmed by at least one compatible instance of the preference model for at least one DM.

In this way, robust ordinal regression is used to investigate spaces of consensus and disagreement between DMs.

The paper is organized in the following way. In the next section, we recall the basic principles of robust ordinal regression methods in the framework of MAUT for a single DM, i.e. $\bar { \mathrm { U T A } } ^ { \mathsf { G M S } }$ and UTA-${ \mathsf { D } } { \mathsf { I S } } ^ { \mathsf { G M S } }$ . Section 3 is devoted to the new extension of robust ordinal regression for multiple criteria group decision. Precisely, we adapt this principle to group choice, ranking, and sorting problems within MAUT. In the following section, we consider the case of incompatibility.

Section 5 provides examples showing how the presented methodology can be applied in practical decision support. The last section contains conclusions and prospects future developments.

## 2. Reminder on robust ordinal regression in the framework of multi-attribute utility theory

We are considering decision problems in which a <sup>fi</sup>nite set of alternatives $A { = } \{ a _ { 1 } , a _ { 2 } , { \ldots } , a _ { i } , { \ldots } , a _ { n } \}$ is evaluated on a consistent family of criteria $G = \{ g _ { 1 } , . . . , g _ { j } , . . . , g _ { m } \} $ . Let $G _ { j }$ denote the value set (scale) of criterion $g _ { j } , j \in J { = } \{ 1 , . . . , m \}$ . Consequently, $\begin{array} { r } { G ( A ) = \prod _ { j \in J } G _ { j } } \end{array}$ represents the evaluation space. From a pragmatic point of view, it is reasonable to assume that $G _ { j } \subseteq \mathbb { R } , \operatorname { f o r } j { = } 1 , . . . ,$ m. Moreover, without loss of generality, we assume that the greater $g _ { j } ( \mathsf { a } )$ , the better solution a on criterion $g _ { j } ,$ for all j ∈ $J , a \in A .$ Finally, increasingly ordered different values of $G _ { j }$ are denoted as: $x _ { j } ^ { 1 } , x _ { j } ^ { 2 } , . . . , x _ { j } ^ { n }$ j with $x _ { j } ^ { k } { < } x _ { j } ^ { \bar { k } + 1 } , k { = } 1 , 2 { , } { \ldots } , n _ { j } { - } 1 , n _ { j } { \leq } n$

Multi-Attribute Utility Theory (MAUT) provides a theoretical foundation for preference modeling using a value function, which aggregates evaluations of alternatives on multiple criteria. In this paper, in order to represent preferences of the DM, we use a model in the form of an additive value function $\begin{array} { r } { U ( a ) = \sum _ { j = 1 } ^ { m } u _ { j } ( g _ { j } ( a ) ) { \in } [ 0 , 1 ] , } \end{array}$ where $u _ { j }$ is the marginal monotone value function for criterion $g _ { j } ,$ $u _ { j } ( x _ { j } ^ { 1 } ) = \bar { 0 }$ , for all $j \in J ,$ and $\begin{array} { r } { \sum _ { j = 1 } ^ { m } u _ { j } ( x _ { j } ^ { n _ { j } } ) = 1 } \end{array}$

In this section, we recall two robust ordinal regression methods within MAUT. One of them is intended to deal with ranking and choice problems, whereas the other is intended to support decision processes related to sorting problems.

## 2.1. $U T A ^ { G M S }$ : robust ordinal regression for ranking and choice problems

In multiple criteria ranking and choice problems, alternatives from A are compared one to any other and the results express relative judgments with the use of comparative notions. In the choice problem, the aim is to select a subset of the best alternatives, while in the ranking problem, alternatives are to be ranked from the best to the worst, according to the preferences of the DM. The idea of considering the whole set of compatible value functions to deal with rank ing and choice problems was originally introduced in the $\mathrm { U T A } ^ { \mathrm { G M S } }$ method [6], and further generalized in GRIP [4].

The UTA<sup>GMS</sup> procedure consists of three steps. It starts with the preference elicitation process, leads through the statement of appropriate ordinal regression problems and results in calculation of binary relations on the set of all alternatives. In this subsection, we recall a general scheme of the method without going into details, which are presented in [6]:

I. Ask the DM (let us denote her/him by $d _ { r } )$ for preference information in form of pairwise comparisons of some reference alternatives $a , b \in A _ { d _ { r } } ^ { \bar { R } } \subseteq A .$ . The DM can state that a is at least as good as (weakly preferred to) $b \ ( a \succsim _ { d _ { r } } b )$ , or a is indifferent to $b \ ( \mathsf { a } \sim _ { d _ { r } } b )$ , or a is strictly preferred to b $\left( \mathsf { a } \succ \mathsf { _ { { d } , } } b \right)$ In GRIP, the DM may additionally provide preferences of two other types: either a partial preorder ${ \gtrsim } _ { d _ { r } } ^ { * } 0 \mathrm { n } A _ { d _ { r } } ^ { R } { \times } A _ { d _ { r } } ^ { R }$ , such that for a,b,c,d $\in A _ { d _ { r } } ^ { R } , ( a , b ) \succsim _ { d _ { r } } ^ { * } ( c , d )$ means a is preferred to b at least as much as c is preferred to d by $d _ { r } ,$ or a partial preorder $\succsim _ { j , d _ { r } } ^ { * }$ on $A _ { d _ { r } } ^ { A } \times A _ { d _ { r } } ^ { A }$ , such that for a,b,c,d $\in A _ { d _ { r } } ^ { R } , ( a , b ) { \succ } _ { j , d _ { r } } ^ { * } ( c , d )$ means a is preferred to b at least as much as c is preferred to d by d on criterion $g _ { j } , j \in J .$

II. Formulate the ordinal regression problem to verify that the set of compatible value functions $\mathcal { U } _ { A ^ { R } , d _ { r } }$ is not empty.

III. Compute the necessary $a { \succeq } _ { d _ { r } } ^ { N } 1$ <sup>U</sup> b and the possible $a \succeq _ { d _ { r } } ^ { P } b$ weak preference relations for all $a , b \in A .$ . On the basis of the set of all compatible value functions $\mathcal { U } _ { A ^ { R } , d _ { r } }$ , two binary relations on <sup>U</sup> fi

– necessary weak preference relation $\succcurlyeq _ { d _ { r } } ^ { N }$ , in case $U ( a ) { \geq } U ( b )$ for all value functions $U \in \mathcal { U } _ { A ^ { R } , d _ { r } }$ compatible with preference information provided by $d _ { r }$ <sup>U</sup><sub>,</sub>

– possible weak preference relation $\succsim _ { d _ { r } } ^ { P }$ , in case $U ( a ) { \geq } U ( b )$ for at least one value function ${ \cal U } \in \mathcal { U } _ { A ^ { R } , d _ { r } }$ compatible with preference information provided by $d _ { r }$

Notice that from the two weak preference relations $\succcurlyeq _ { d _ { r } } ^ { N }$ and $\succsim _ { d _ { r } } ^ { P }$ one can get preference, indifference, and incomparability in a usual way.

## 2.2. $U T A D I S ^ { G M S }$ : robust ordinal regression for sorting problems

The sorting problem involves the assignment of a set of alternatives into prede<sup>fi</sup>ned homogeneous classes. This type of problem can also be referred to as the discrimination problem or the classi<sup>fi</sup>cation problem. However, in these two problems, classes are not necessarily preference ordered whereas sorting refers to classes which are ordered from the best to the worst. We denote by $C _ { 1 } , C _ { 2 } , . . . , C _ { p } ,$ prede-<sup>fi</sup>ned preference ordered classes having a semantic de<sup>fi</sup>nition, where $C _ { h + 1 }$ is preferred to $C _ { h } , h = 1 , . . . , p - 1$ . Robust ordinal regression approach for sorting problems has been introduced in $\mathsf { U T A D I S ^ { G M S } } [ 8 ]$

In UTADIS<sup>GMS</sup>, the DM $d _ { r }$ is asked to provide a set of assignment examples. Each assignment example consists of an alternative $\bar { a } ^ { * } \in A _ { d _ { r } } ^ { R } \subseteq A$ and its desired assignment $a ^ { * } \to [ C _ { L _ { d r } ( a ^ { * } ) } , C _ { R _ { d r } ( a ^ { * } ) } ] ,$ , where $[ C _ { L _ { d r } ( a ^ { * } ) } , C _ { R _ { d r } ( a ^ { * } ) } ]$ ] is an interval of contiguous classes $C _ { L _ { d r } ( a ^ { * } ) } , C _ { L _ { d r } + 1 ( a ^ { * } ) } , . . . , C _ { R _ { d r } ( a ^ { * } ) } , \ L _ { d _ { r } } ( a ^ { * } ) \leq$ $R _ { d _ { r } } ( a ^ { * } )$ . Given a value function $U ,$ a set of assignment examples is said to be consistent with U iff:

$$
\forall a ^ {*}, b ^ {*} \in A _ {d _ {r}} ^ {R}, L _ {d _ {r}} (a ^ {*}) > R _ {d _ {r}} (b ^ {*}) \Rightarrow U (a ^ {*}) > U (b ^ {*}).
$$

Considering all compatible value functions, one obtains two kinds of assignment for any alternative $a \in A { : }$

• the necessary assignment $C _ { d _ { r } } ^ { N } ( a )$ speci<sup>fi</sup>es the set of indices of classes $C _ { h }$ for which all compatible value functions $U \in \mathcal { U } _ { A ^ { R } , d _ { t } }$ assign a to $C _ { h } \mathrm { : }$

$$
\begin{array}{l} C _ {d _ {r}} ^ {N} (a) = \left[ L _ {d _ {r}} ^ {\mathcal {U}, N} (a), R _ {d _ {r}} ^ {\mathcal {U}, N} (a) \right] \\ \qquad = \Big \{h \in H: \forall U \in \mathcal {U} _ {A ^ {R}, d _ {r}} \textit {i t h o l d s} h \in \left[ L _ {d _ {r}} ^ {U} (a), R _ {d _ {r}} ^ {U} (a) \right] \Big \}, \end{array}
$$

• the possible assignment $C _ { d _ { r } } ^ { P } ( \mathsf { a } )$ determines the set of indices of classes $C _ { h }$ for which there exists at least one compatible value function $U \in$ $\mathcal { U } _ { A ^ { R } , d _ { r } }$ assigning a to $C _ { h } \mathrm { : }$

$$
\begin{array}{l} C _ {d _ {r}} ^ {P} (a) = \left[ L _ {d _ {r}} ^ {\mathcal {U}, P} (a), R _ {d _ {r}} ^ {\mathcal {U}, P} (a) \right] \\ = \Big \{h \in H: \exists U \in \mathcal {U} _ {A ^ {R}, d _ {r}} f o r w h i c h h \in \left[ L _ {d _ {r}} ^ {U} (a), R _ {d _ {r}} ^ {U} (a) \right] \Big \}, \end{array}
$$

where $L _ { d _ { r } } ^ { U } ( a )$ and $R _ { d _ { r } } ^ { U } ( a )$ are, respectively, the indices of the worst and the best class to which alternative a is assigned by value function U.

The $\mathrm { U T A D I S } ^ { \mathrm { G M S } }$ procedure consists of six steps, out of which three initial steps agree with those from $\mathrm { U T A } ^ { \mathrm { G M S } }$ with respect to their roles. The remaining three steps concern the computation of boundary indices of possible and necessary classes and of the resulting assignments. More detailed description of the method can be found in [8].

I. Ask the DM $( d _ { r } )$ for preference information in form of a set of assignment examples, each one consisting of an alternative $a ^ { * }$ $\in A _ { d , } ^ { R } \subseteq A$ and its desired assignment $a ^ { * } {  } \big [ C _ { L _ { d r } ( a ^ { * } ) } , C _ { R _ { d r } ( a ^ { * } ) } \big ] .$

$$
\mathrm{UTA} ^ {\text { G   M   S }}
$$

IV. Compute for each $a \in A$ the boundary indices $L _ { d _ { r } } ^ { \mathcal { U } , P } ( a ) , L _ { d _ { r } } ^ { \mathcal { U } , N } ( a )$ $R _ { d _ { r } } ^ { \mathcal { U } , N } ( a )$ and $R _ { d _ { r } } ^ { \mathcal { U } , P } ( a )$ . Using necessary weak preference relation $\gtrsim _ { d _ { r } } ^ { N }$ and possible weak preference relation $\succsim _ { d _ { r } } ^ { P }$ , boundary indices of the necessary and the possible assignments $L _ { d _ { r } } ^ { \mathcal { U } , P } ( a )$ $L _ { d _ { r } } ^ { \mathcal { U } , N } ( a ) , R _ { d _ { r } } ^ { \mathcal { U } , N } ( a ) , R _ { d _ { r } } ^ { \mathcal { U } , P } ( a )$ are de<sup>fi</sup>ned as follows:

– minimum possible class:

$$
L _ {d _ {r}} ^ {\mathcal {U}, P} (a) = \operatorname{Max} \left\{\{1 \} \cup \left\{L _ {d _ {r}} \left(a ^ {*}\right): a \gtrsim_ {d _ {r}} ^ {N} a ^ {*}, a ^ {*} \in A _ {d _ {r}} ^ {R} \right\} \right\},
$$

$$
\begin{array}{l} - \text { minimum   necessary   class: } \\ L _ {d _ {r}} ^ {\mathcal {U}, N} (a) = M a x \Big \{\{1 \} \cup \Big \{L _ {d _ {r}} (a ^ {*})  :   a \gtrsim_ {d _ {r}} ^ {P} a ^ {*},   a ^ {*} \in A _ {d _ {r}} ^ {R} \Big \} \Big \}, \\ - \text { maximum   necessary   class: } \\ R _ {d _ {r}} ^ {\mathcal {U}, N} (a) = M i n \Big \{\{p \} \cup \Big \{R _ {d _ {r}} (a ^ {*})  :   a ^ {*} \gtrsim_ {d _ {r}} ^ {P} a,   a ^ {*} \in A _ {d _ {r}} ^ {R} \Big \} \Big \}, \\ - \text { maximum   possible   class: } \\ R _ {d _ {r}} ^ {\mathcal {U}, P} (a) = M i n \Big \{\{p \} \cup \Big \{R _ {d _ {r}} (a ^ {*})  :   a ^ {*} \gtrsim_ {d _ {r}} ^ {N} a,   a ^ {*} \in A _ {d _ {r}} ^ {R} \Big \} \Big \}. \end{array}
$$

V. Assign to each $a \in A$ its possible assignment $C _ { d _ { r } } ^ { P } ( a ) =$ $\left\lceil L _ { d _ { r } } ^ { \mathcal { U } , \breve { P } } ( a ) , R _ { d _ { r } } ^ { \mathcal { U } , P } ( a ) \right\rceil$

VI. Assign to each $a \in A$ its necessary assignment which is $C _ { d _ { r } } ^ { N } ( \Breve { a } ) = \left\lceil L _ { d _ { r } } ^ { \mathcal { U } , N } ( a ) , R _ { d _ { r } } ^ { \mathcal { U } , N } ( a ) \right\rceil$ in case $L _ { d _ { r } } ^ { \mathcal { U } , N } ( a ) { \leq } R _ { d _ { r } } ^ { \mathcal { U } , N } ( a )$ , and $C _ { d _ { r } } ^ { N } ( a ) = \bar { \varnothing } ,$ , otherwise.

## 3. Robust ordinal regression for group decision problems

In this section, we present an extension of the robust ordinal regression to the case of group decision. In this case, several decision makers (let us denote a set of DMs by $\mathcal { D } = \{ d _ { 1 } , . . . , d _ { p } \} )$ ) cooperate to make a collective decision. They share the same “description” of the decision problem, i.e. the same set of alternatives, family of criteria, and performance matrix. We assume that each DM plays the same role in the committee, so we do not differentiate their weights. They offer individual preference information, which is composed either of pairwise comparisons or exemplary assignments of some reference alternatives. The collective preference model accounts for preference information expressed by each DM, and robust ordinal regression is used to combine them into a consensus solution.

We will present two MCDA methods called ${ \mathrm { U T A } } ^ { \mathrm { G M S } } .$ -GROUP and UTADIS<sup>GMS</sup>-GROUP. Each of them extends the corresponding GMS method, originally designed for consideration of preferences of just a single DM, so that it is capable of dealing with ranking and choice or sorting group decision problems, respectively. Although the presented methods concern different types of decision problems, the scheme of this extension is common for both methods. In the <sup>fi</sup>rst stage of this extension, we consider each DM in individually, and we identify the necessary and the possible consequences of her/his preference information. Let us remind that, in general, the necessary results (relations or assignments) specify the most certain recommendations worked out on the basis of all compatible instances of a preference model considered simultaneously, while the possible results identify possible recommendations which stem from at least one instance of a preference model compatible with preference information. In the second stage, we investigate spaces of consensus for subsets of decision makers. This is achieved by introduction of a second level of certainty, which refers to the subset of DMs con<sup>fi</sup>rming the speci<sup>fi</sup>c outcome. Precisely, we refer again to the possibility and the necessity of this con<sup>fi</sup>rmation, and we verify whether necessary and possible results follow preference information provided by at least one or all DMs in . Notice that at this level, one could alternatively use <sup>D</sup>terms “supported” and “unanimous” to distinguish statements supported by at least one DM or all DMs, respectively. In this way, we are able to indicate what would happen always (for all compatible instances), sometimes (for at least one compatible instance), or never (for none of the compatible instances) with respect to a subset or to the whole set of DMs. Consequently, we provide results of four different types:

• Necessary–necessary (N, N) results consisting of the necessary (N) consequences of preference information provided by each DM which are con<sup>fi</sup>rmed for all DMs (N) in . They specify the rankings, <sup>D</sup>relations, or assignments to classes which hold when considering simultaneously all compatible instances of a preference model for all DMs. They can be perceived as robust with respect to indirect preference information of all decision makers. Such robustness of the necessary–necessary outcomes refers to the fact that the de<sup>fi</sup>- nite result (comparison of a pair of alternatives or assignment to a speci<sup>fi</sup>c class) is the same whichever instance of a preference model compatible with preference information of any DM would be used for analysis. Therefore, the necessary–necessary results can be referred to as “absolutely sure” preference statements.

• Necessary–possible (N, P) results consisting of the necessary (N) consequences of preference information provided by each DM con-<sup>fi</sup>rmed for at least one (P) DM in . This kind of con<sup>fi</sup>rmation <sup>D</sup>indicates certainty about the speci<sup>fi</sup>c result expressed by any DM. Notice, however, that it is important to investigate the subsets of DMs who agree or differ with respect to the given outcome. In this way, we are able to state whether the de<sup>fi</sup>nite result is “absolutely sure”, “almost sure”, “sure on average”, “barely sure”, or “not sure at all” against the set . From the point of view of a single DM, such analysis may cause her/his reaction in the following iterations.

• Possible–necessary (P, N) results formed by the possible (P) outcomes of preferences provided by each DM con<sup>fi</sup>rmed for all of them (N). They re<sup>fl</sup>ect the full conviction of the set of DMs that a speci<sup>fi</sup>c outcome may be true. Again, the truth of some possible– necessary results can persuade some DMs to change the “possible truth” into “necessary one” by enrichment of the necessary–possible and necessary–necessary results in the following iterations.

• Possible–possible (P, P) results re<sup>fl</sup>ecting the possible (P) consequences of preferences provided by each DM con<sup>fi</sup>rmed for at least one of them (P). They refer to the most general outcomes, which can be obtained when considering individually any compatible model of any DM. Notice that if possible–possible relation or assignment is true, one needs to treat it as an indication with the lowest level of certainty which is accounted by the method. However, if this speci<sup>fi</sup>c outcome is false, then this negative result can be con<sup>fi</sup>rmed with the greatest con<sup>fi</sup>dence, because it is observed simultaneously for all compatible models for all DMs.

## 3.1. Existing approaches and characteristics of the new methods

MAUT has been used to model preferences of the DMs and to build a collective model in several group decision support methods. Most of them are devoted to multiple criteria ranking problems (see [20]). For example. Jarke et al. [15l proposed a negotiation system which allows arriving at a common value function through exchange of information, negotiation and use of axioms to contract the feasible space, until DMs marginal value functions are identical. Vetschera [30] took advantage of MAUT to develop a general framework for group decision making where great emphasis is put on the feedback from the group to individual opinions, which may lead to reconsideration of the supplied preference information or its incremental speci<sup>fi</sup>cation. Matsatsinis et al. [21] proposed to construct a UTA-like decision model for each individual DM along with a satisfaction measurement model to measure the group members' satisfaction on the collective decision. Damart et al. [2] addressed multiple criteria sorting problems and proposed a methodology in which the group of DMs discusses how to sort some exemplary alternatives. The agreed sorting examples are incorporated into the collective model and all the individual models. If the group feels the collective model is satisfactory, then the procedure stops. The method is based on an disaggregation approach for ELECTRE TRI, but it can also be applied to value-based methods, such as the traditional UTADIS, as well. For the review of recent developments in group decision making, see [19,24].

The proposal for group decision making introduced in this paper compares positively to existing methods which address multiple criteria group decision problems in several ways. First of all, it considers possible and necessary consequences of preference information provided by all DMs, which no previous method did. It provides “sure” and “plausible” preference statements referring to necessary and possible results. Its outcomes have several properties of general interest for MCDA. Secondly, following the assumptions of the basic methods for a single DM, and the general trend described in [20], it requires speci<sup>fi</sup>cation of exemplary decisions for reference alternatives which play the role of a training set. This is concordant with “learning from examples” methodology, which is a paradigm of arti<sup>fi</sup>cial intel ligence and knowledge discovery. Moreover, the proposed methods make use of very general and <sup>fl</sup>exible preference models, i.e. we consider general non-decreasing marginal value functions (rather than piecewise linear marginal value functions). They are also very useful, because they do not involve any arbitrary and restrictive parametri zation. Furthermore, when searching for the spaces of consensus and disagreement between decision makers, they accept existence of all instances of a preference model compatible with preferences provided by all DMs, and assesses the results in the set of alternatives A with respect to all these instances. Distinguishing the necessary– necessary, necessary–possible, possible–necessary, and possible–pos sible consequences of using all compatible instances of a preference model of all DMs, the proposed methods answer questions of robustness concern. Another appeal of such an approach stems from the fact that it gives space for interactivity with the DMs. Presentation of the four types of results for group decision, and their comparison with consequences of one's own preferences, is a good support for generating reactions from particular DMs. Namely, (s)he could wish to enrich the necessary–possible and possible–possible results or to contradict a part of it by impoverishing the necessary–necessary and possible– necessary outcomes. The suggested way of proceeding is to analyze the necessary and possible consequences, and in the following iterations add comparisons concerning pairs (a, b) for which the possible relation was satis<sup>fi</sup>ed, but not the necessary one, or restrict the range of possible classes for some alternatives. Obviously, we admit that the DMs may remove or modify previously provided pieces of preference information. This is likely to happen, for example, in case of inconsistent judgments of at least two DMs or, in general, when a DM realizes that nobody else shares her/his point of view (i.e., advantage of one alternative over the other or possible assignment to a given class). These reactions can be integrated in the indirect preference information in the following stages. As a consequence, it is easier for the DMs to associate pieces of their preference information with the result and, therefore, to control the impact of each piece of information (s)he provides on the result.

Note that apart from reasoning in terms of the necessary and the possible at the two levels of certainty, $\mathrm { U T A } ^ { \mathrm { G M S } }$ -GROUP and UTA-$\mathsf { \bar { D } I S ^ { G M S } }$ -GROUP share several other aspects justifying their joint consideration. This includes the use of a general additive value function as an underlying preference model, requirement of exercising decisions by the DMs rather than forcing them to specify directly values of some parameters, robust elicitation of a preference model, and inconsistency management (see Section 4).

## 3.2. UTA<sup>GMS</sup>-GROUP

In case of ranking and choice problems, each DM $d _ { r } \in \mathcal { D }$ gives preference information required by $\mathsf { U T A } ^ { \mathsf { G M S } }$ <sup>D</sup>and GRIP methods. Using this information, the possible and the necessary preference relations $\succcurlyeq _ { d _ { r } } ^ { P }$ and $\succeq _ { d _ { r } } ^ { N }$ are computed for all decision makers $d _ { r } \in \mathcal { D } .$ . Then, four preference relations $\succeq _ { D ^ { \prime } } ^ { N , N } , \succeq _ { D ^ { \prime } } ^ { N , P } , \succeq _ { D ^ { \prime } } ^ { P , N }$ , and ${ \succsim } _ { D ^ { \prime } } ^ { P , P }$ <sup>D</sup>, can be determined for all subset of DMs, $\mathcal { D } ^ { ' } \subseteq \mathcal { D } .$

De<sup>fi</sup>nition 3.1.

1. ac<sup>N;N</sup><sub>′</sub> b: ac<sub>d</sub><sup>N</sup> b for all ∈ <sup>′</sup>,

2. $a { \gtrsim } _ { \mathcal { D } ^ { ' } } ^ { \mathrm { N } , \mathrm { P } } b { \colon } a { \gtrsim } _ { d _ { r } } ^ { N } $ b for at least one $d _ { r } \in \mathcal { D } ^ { ' }$

3. $a \mathrm { { \lesssim } } _ { \mathcal { D } ^ { ' } } ^ { \bar { P } , N } b \mathrm { : } a \mathrm { { \gtrsim } } _ { d _ { r } } ^ { P }$ b for all $d _ { r } \in \mathcal { D } ^ { ' }$

4. $a { \gtrsim } _ { \mathcal { D } ^ { ' } } ^ { P , P } b { \colon } a { \gtrsim } _ { d _ { r } } ^ { P } b \rfloor$ for at least one $d _ { r } \in \mathcal { D } ^ { ' }$

From the four relations $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N } , \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , P } , \succeq _ { \mathcal { D } ^ { ' } } ^ { P , N } , \mathrm { a n d } \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , P } } \end{array}$ , one can obtain indifference (∼), preference $( \succ )$ <sup>D D D</sup>, and incomparability (?), in a usual way, i.e. ≻ is the asymmetric part of c, and ∼ is its symmetric part (see Table 1). The preference relations obtained from $\begin{array} { r } { \stackrel { \star } { \approx } _ { \mathcal { D } ^ { ' } } ^ { N , N } , \stackrel { \star } { \approx } _ { \mathcal { D } ^ { ' } } ^ { N , P } , \stackrel { \star } { \approx } _ { \mathcal { D } ^ { ' } } ^ { P , N } , \mathrm { a n d } \stackrel { \star } { \approx } _ { \mathcal { D } ^ { ' } } ^ { P , R } } \end{array}$ are employed to form the rankings that are <sup>D D D D</sup>presented to the DMs as end results of the $\mathrm { U T A ^ { G M S } - G R O U P }$ method at the current stage of interaction. Although in the considered framework it is also possible to handle preference information about intensity of preference, we will skip this type of preferences to save space.

Some properties which are satis<sup>fi</sup>ed by the relations $\succeq ^ { N , N } , \succeq ^ { N , P } , \succeq ^ { P , N } ,$ and $\succsim ^ { P , P }$ , help to drive the solution process and to elaborate consensus among DMs. The most important properties are discussed in Appendix A, whereas some supplementary properties are given in e-Appendix D.

In the $\mathrm { U T A } ^ { \mathrm { G M S } } .$ -GROUP method, we are not considering the preference information provided by the DMs as a whole. Instead, they are encouraged to provide the preference information incrementally by possibly small pieces. If they associated with these pieces some numerical con<sup>fi</sup>dence levels, we could de<sup>fi</sup>ne valued preference relations on the set of alternatives.

3.2.1. Specification of pairwise comparisons with decreasing confidence levels

The $\mathrm { U T A } ^ { \mathrm { G M S } }$ method is intended to support the DM in an interactive process by permitting the DM an incremental speci<sup>fi</sup>cation of pairwise comparisons. Let $\succeq _ { 1 d _ { r } } \subseteq \succeq _ { 2 d _ { r } } \subseteq \dots \subseteq \succeq _ { t , d _ { r } }$ be embedded sets of pairwise comparisons of reference alternatives provided by a speci<sup>fi</sup>c DM, d . Each of those sets $\succeq _ { t , d _ { r } } , t { = } 1 , . . . , s ,$ , is modeled with a set of constraints generating the set of compatible value functions $\mathcal { U } _ { t . d _ { r } } ^ { A ^ { R } }$ Each time we pass from $\succeq _ { t - 1 , d _ { r } } \mathrm { t o } \succeq _ { t , d _ { r } } t = 2 , . . . , s$ we add new constraints concerning pairs $( a , b ) \in \succsim _ { t , d _ { r } }$ , while $( a , b ) \notin \succsim _ { t - 1 , d _ { r } } .$ Thus, the sets of compatible value functions are embedded in the inverse order of the related set of pairwise comparisons $\succeq _ { t , d _ { r } } , t { = } 1 , . . . s , \mathrm { i . e }$ $\mathcal { U } _ { 1 , d _ { r } } ^ { A ^ { R } } \mathcal { U } _ { 2 , d _ { r } } ^ { A ^ { R } } \ldots \mathcal { U } _ { s , d _ { r } } ^ { A ^ { R } }$ . We suppose that $\mathcal { U } _ { s } ^ { A ^ { R } } \neq \hat { \boldsymbol { \varnothing } } .$ . For each con<sup>fi</sup>dence level <sup>U</sup> <sup>U</sup> <sup>U U</sup>t, we can compute the corresponding possible and necessary weak preference relations $\succsim _ { t , d _ { r } } ^ { P }$ and $\succsim _ { t , d _ { r } } ^ { N }$ as de<sup>fi</sup>ned in [6].

In the context of group decision, we assume that we pass from $\succsim _ { t - 1 , D ^ { ' } }$ to $\succsim _ { t , \mathcal { D } ^ { ' } }$ , whenever any decision maker $d _ { h } \in \mathcal { D } ^ { \prime }$ <sup>D</sup>adds some new pairwise <sup>D D</sup>comparisons of reference alternatives. Obviously, for all $a , b , \in A$ we can compute $\begin{array} { r } { \gtrsim _ { t , \mathcal { D } ^ { ' } } ^ { N , N } \gtrsim _ { t , \mathcal { D } ^ { ' } } ^ { N , P } \gtrsim _ { t , \mathcal { D } ^ { ' } } ^ { P , N } \mathrm { a n d } \gtrsim _ { t , \mathcal { D } } ^ { P , P } } \end{array}$

## 3.2.2. Valued preference relations

Let $\theta _ { t , d _ { r } }$ be the con<sup>fi</sup>dence level assigned by $d _ { r } \in \mathcal { D } ^ { \prime }$ to the pairwise <sup>D</sup>comparisons provided in iteration t, which, however, were not in the set of her/his reference statements in iteration $t - 1$ . We assume that for each $d _ { r } \in \mathcal { D } ^ { ' } , 1 = \theta _ { 1 , d _ { r } } \ge \theta _ { 2 , d _ { r } } \ge . . . \ge \theta _ { s , d _ { r } } > 0$ . Precisely, if d adds new preference statements or makes more precise some of her/his already supplied statements in the t-th iteration, then $\theta _ { t , d _ { r } } { < } \theta _ { t - 1 , d _ { r } }$ . Otherwise, if only some other DMs provide additional preference information in the t-th iteration, $\theta _ { t , d _ { r } } = \theta _ { t - 1 , d _ { r } }$ . Consequently, if we pass from $\succsim _ { \mathrm { t } - 1 , \mathcal { D } ^ { ' } }$ to $\succsim _ { \mathrm { t } , D ^ { ' } }$ , then for all $d _ { r } \in \mathcal { D } ^ { ' }$ we have $\theta _ { t , d _ { r } } \leq \theta _ { t - 1 , d _ { r } }$ and for at least one $d _ { h }$ $\in \mathcal { D } ^ { ' }$ <sup>D</sup>we have $\theta _ { t , d _ { h } } { < } \theta _ { t - 1 , d _ { h } } .$

<sup>D</sup>Let us also denote by $\succsim _ { t , d _ { r } , \mathcal { D } ^ { ' } }$ the sets of partial preorders provided by DMs in $\mathcal { D } ^ { ' }$ <sup>D</sup>, such that we consider statements of $\mid d _ { r }$ with the con<sup>fi</sup>- <sup>D</sup>dence level not less than $\theta _ { t , d _ { r } }$ , and statements of all other DMs $d _ { h } \in$ <sup>′</sup> with the con<sup>fi</sup>dence level. Let $\succeq _ { t , d _ { r } , \mathcal { D } ^ { ' } } ^ { N , N } \succeq _ { t , d _ { r } , \mathcal { D } ^ { ' } } ^ { N , P } \succeq _ { t , d _ { r } , \mathcal { D } ^ { ' } } ^ { P , N } ,$ and $\succeq _ { t , d _ { r } , D ^ { ' } } ^ { P , P }$ <sup>D</sup>be the relations corresponding to $\succsim _ { t , d _ { r } , \mathcal { D } ^ { ' } }$

The necessary–necessary, necessary–possible, possible–necessary, and possible–possible relations inferred from $\boldsymbol { \gtrsim } _ { \mathcal { D } ^ { ' } } ^ { N , N } , \boldsymbol { \gtrsim } _ { \mathcal { D } ^ { ' } } ^ { N , P } , \boldsymbol { \gtrsim } _ { \mathcal { D } ^ { ' } } ^ { P , N }$ ; and $\succeq _ { { \mathcal D } ^ { ' } } ^ { { \dot { P } } , { P } } .$

<table><tr><td></td><td> $b\succeq_{\mathcal{D}^{\prime}}^{N,N} a$ </td><td> $not(b\succeq_{\mathcal{D}^{\prime}}^{N,N} a)$ </td><td></td><td> $b\succeq_{\mathcal{D}^{\prime}}^{P,P} a$ </td><td> $not(b\succeq_{\mathcal{D}^{\prime}}^{P,P} a)$ </td></tr><tr><td> $a\succeq_{\mathcal{D}^{\prime}}^{N,N} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{N,N} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{N,N} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{P,P} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{P,P} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{P,P} b$ </td></tr><tr><td> $not(a\succeq_{\mathcal{D}^{\prime}}^{N,N} b)$ </td><td> $b\succeq_{\mathcal{D}^{\prime}}^{N,N} a$ </td><td> $a?\succeq_{\mathcal{D}^{\prime}}^{N,N} b$ </td><td> $not(a\succeq_{\mathcal{D}^{\prime}}^{P,P} b)$ </td><td> $b\succeq_{\mathcal{D}^{\prime}}^{P,P} a$ </td><td>-</td></tr><tr><td></td><td> $b\succeq_{\mathcal{D}^{\prime}}^{N,P} a$ </td><td> $not(b\succeq_{\mathcal{D}^{\prime}}^{N,P} a)$ </td><td></td><td> $b\succeq_{\mathcal{D}^{\prime}}^{P,N} a$ </td><td> $not(b\succeq_{\mathcal{D}^{\prime}}^{P,N} a)$ </td></tr><tr><td> $a\succeq_{\mathcal{D}^{\prime}}^{N,P} a$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{N,P} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{N,P} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{P,N} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{P,N} b$ </td><td> $a\succeq_{\mathcal{D}^{\prime}}^{P,N} b$ </td></tr><tr><td> $not(a\succeq_{\mathcal{D}^{\prime}}^{N,P} b)$ </td><td> $b\succeq_{\mathcal{D}^{\prime}}^{N,P} a$ </td><td> $a?\succeq_{\mathcal{D}^{\prime}}^{N,P} b$ </td><td> $not(a\succeq_{\mathcal{D}^{\prime}}^{P,N} b)$ </td><td> $b\succeq_{\mathcal{D}^{\prime}}^{P,N} a$ </td><td> $a?\succeq_{\mathcal{D}^{\prime}}^{P,N} b$ </td></tr></table>

On the basis of nested sets of pairwise comparisons and corresponding con<sup>fi</sup>dence levels $\theta _ { t , d , } t = 1 , . . . s , d _ { r } \in \mathcal { D } ^ { \prime }$ , a valued necessary– necessary preference relation $R _ { \mathcal { D } ^ { ' } } ^ { N , N } : A \times A {  } \{ \theta _ { 1 , d _ { r } } , \theta _ { 2 , d _ { r } } , . . . , \theta _ { s , d _ { r } } , \} 0$ can be built as follows for all $a , \mathbf { b } \in { \overset {  } { A } } :$

• if for all $d _ { r } \in \mathcal { D } ^ { ' }$ there exists at least one t such that $a \approx _ { t , d _ { r } } ^ { N } b ,$ then $R _ { \mathcal { D } ^ { ' } } ^ { N , N } ( a , b ) \stackrel { \cdot } { = } m i n _ { d _ { r } } \Big \{ \operatorname* { m a x } \Big \{ \theta _ { t , d _ { r } } : a \gtrsim _ { t , d _ { r } } ^ { N } b , t = 1 , \ldots , s \Big \} \Big \}$

• if for any $d _ { r } \in \mathcal { D } ^ { \prime }$ there is no single t for which $\stackrel { \cdot } { a } \approx { } _ { t , d _ { r } } ^ { N } b ,$ then $R _ { \mathcal { D } ^ { ' } } ^ { N , N }$ $( a , b ) = 0 .$

A valued necessary–possible preference relation $R _ { n ^ { \prime } } ^ { N , P } : A \times A \xrightarrow { }$ $\left\{ \theta _ { 1 , d _ { r } } , \theta _ { 2 , d _ { r } } , . . . , \theta _ { s , d _ { r } } , 0 \right) \}$ can be built as follows for all $a , b \in A { : }$

$$
d _ {r} \in \mathcal {D} ^ {\prime}
$$

$$
a \succeq_ {t, d _ {r}} ^ {N} b,
$$

$$
R _ {\mathcal {D} ^ {\prime}} ^ {N, P}: A \times A \rightarrow \max _ {d _ {r}} \left\{\max \left\{\theta_ {1, d _ {r}}: a \gtrsim_ {t, d _ {r}} ^ {N} b, t = 1, \dots , s \right\}\right\}
$$

• if for all $d _ { r } \in \mathcal { D } ^ { \prime }$ there is no single t for which $a \gtrsim _ { t , d _ { r } } ^ { N } b ,$ , then $R _ { \mathcal { D } ^ { ' } } ^ { N , P } ( a , b ) = 0 .$

A valued possible–necessary preference relation $R _ { n ^ { \prime } } ^ { P , N } : A \times A \xrightarrow { }$ $\{ 1 - \theta _ { 1 , d _ { r } } , 1 - \bar { \theta _ { 2 , d _ { r } } } , . . . , 1 - \theta _ { s , d _ { r } } , 1 ) \}$ <sup>D</sup>can be built as follows for all $a , b \in A { : }$

• if for all $d _ { r } \in \mathcal { D } ^ { \prime }$ there exists at least one t such that $a \approx _ { t , d _ { r } } ^ { P } b ,$ then $\begin{array} { r } { R _ { \mathcal { D } ^ { ' } } ^ { P , N } ( a , b ) = \operatorname* { m i n } _ { d _ { r } } \Big \{ \operatorname* { m i n } \Big \{ 1 - \theta _ { t , d _ { r } } : n o t \Big ( a \approx _ { t , d _ { r } } ^ { P } b \Big ) , t = 1 , . . . , s \Big \} \Big \} , } \end{array}$

• if for all $d _ { r } \in \mathcal { D } ^ { ' }$ and for all t we have $a \gtrsim _ { t , d _ { r } } ^ { P } b ,$ , then $R _ { \mathcal { D } ^ { ' } } ^ { P , N } ( a , b ) = 1$

A valued possible–possible preference relation $R _ { \mathcal { D } ^ { ' } } ^ { P , P } : A \times A \xrightarrow { }$ $\{ 1 - \theta _ { 1 , d _ { r } } , 1 - \theta _ { 2 , d _ { r } } , . . . , 1 - \theta _ { s , d _ { r } } , 1 ) \}$ <sup>D</sup>can be built as follows for all $a , b \in A ;$

• if for at least one $d _ { r } \in \mathcal { D } ^ { ' }$ there exists at least one t such that $a \approx _ { t , d _ { r } } ^ { P } b ,$ then $\begin{array} { r } { R _ { \mathcal { D } ^ { \prime } } ^ { P , P } ( a , b ) = \operatorname* { m a x } _ { d _ { r } } \Big \{ \operatorname* { m i n } \Big \{ 1 - \theta _ { t , d _ { r } } : n o t \Big ( a \succ _ { t , d _ { r } } ^ { P } b \Big ) , t = 1 , \dots , s \Big \} \Big \} } \end{array}$ <sup>D</sup>• if for any $d _ { r } \in \mathcal { D } ^ { ' }$ and for all t we have $\begin{array} { r } { a \gtrsim _ { t , d _ { r } } ^ { \dot { P } } b , } \end{array}$ , then $R _ { \mathcal { D } ^ { ' } } ^ { P , P } ( a , b ) = 1$

## 3.3. UTADIS<sup>GMS</sup>-GROUP

In case of multiple criteria sorting problems, for each DM $d _ { r } \in \mathcal { D } ,$ , we consider the set of all compatible value functions $\mathcal { U } _ { A ^ { R } , d _ { r } }$ . Given a set $A _ { d _ { r } } ^ { R }$ of assignment examples, for each $a \in A$ <sup>U</sup>and for each d $\dot { \mathbf { \Omega } } \in \mathcal { D } ,$ , we de<sup>fi</sup>ne the possible and necessary assignments using $\mathrm { U T A D I S } ^ { \mathrm { G M S } }$ <sup>D</sup>, i.e.:

$$
\begin{array}{l} C _ {d _ {r}} ^ {P} (a) = \left\{h \in H: \exists U \in \mathcal {U} _ {A ^ {R}, d _ {r}} a s s i g n i n g   a   \text { to }   C _ {h} \right\} a n d \\ C _ {d _ {r}} ^ {N} (a) = \left\{h \in H: \forall U \in \mathcal {U} _ {A ^ {R}, d _ {r}} a s s i g n i n g   a   \text { to }   C _ {h} \right\} \end{array}
$$

Then, the four assignments $C _ { \mathcal { D } ^ { ' } } ^ { N , N } ( a ) , C _ { \mathcal { D } ^ { ' } } ^ { N , P } ( a ) , C _ { \mathcal { D } ^ { ' } } ^ { P , N } ( a ) ,$ , and $C _ { \mathcal { D } ^ { ' } } ^ { P , P } ( a )$ , can <sup>D ð Þ D ð Þ</sup>be computed for all subsets of decision makers $\mathcal { D } ^ { ' } \subseteq \mathcal { D } .$

De<sup>fi</sup>nition 3.2.

$$
1. C _ {\mathcal {D} ^ {\prime}} ^ {N, N} (a) = \cap_ {d _ {r} \in \mathcal {D} ^ {\prime}} C _ {d _ {r}} ^ {N} (a),
$$

$$
2. C _ {\mathcal {D} ^ {\prime}} ^ {N, P} (a) = \cup_ {d _ {r} \in \mathcal {D} ^ {\prime}} C _ {d _ {r}} ^ {N} (a),
$$

$$
3. C _ {\mathcal {D} ^ {\prime}} ^ {P, N} (a) = \cap_ {d _ {r} \in \mathcal {D} ^ {\prime}} C _ {d _ {r}} ^ {P} (a),
$$

$$
4. C _ {\mathcal {D} ^ {\prime}} ^ {P, P} (a) = \cup_ {d _ {r} \in \mathcal {D} ^ {\prime}} C _ {d _ {r}} ^ {P} (a).
$$

In Appendix B, we present a few important properties which are satis<sup>fi</sup>ed by the assignments $C ^ { N , ~ N } ( a ) , \dot { C ^ { N , ~ P } } ( a ) , \dot { C ^ { P , ~ N } } ( a )$ and $C ^ { P , ~ P } ( a )$ and help to arrive at a consensus solution. Some additional properties of these outcomes are given in e-Appendix F.

3.3.1. Specification of exemplary assignments with decreasing confidence levels

The $\mathrm { U T A D I S } ^ { \mathrm { G M S } }$ method is intended to support incremental speci<sup>fi</sup>- cation of exemplary assignments of reference alternatives. Let $[ L _ { 1 , d _ { r } } ( a ^ { * } )$ $R _ { 1 , d _ { r } } ( a ^ { * } ) ] \ [ L _ { 2 , d _ { r } } ( a ^ { * } ) , R _ { 2 , d _ { r } } ( a ^ { * } ) ] \ \dots \ [ L _ { t , d _ { r } } ( a ^ { * } ) , R _ { t , d _ { r } } ( a ^ { * } ) ]$ be embedded sets of d 's exemplary assignments. The sets of compatible value functions are embedded in the same order as the sets of the exemplary assignments $[ L _ { t , d _ { r } } ( \boldsymbol { a } ^ { * } ) , R _ { t , d _ { r } } ( \boldsymbol { a } ^ { * } ) ] , t = 1 , . . . , s , a ^ { * } \in A _ { d _ { r } } ^ { R } , \mathrm { i . e . } \mathcal { U } _ { 1 , d _ { r } } ^ { A _ { 1 , d _ { r } } ^ { R } } \mathcal { U } _ { 2 , d _ { r } } ^ { A _ { 2 , d _ { r } } ^ { R } } \ldots \mathcal { U } _ { s , d _ { r } } ^ { A _ { { s } , d _ { r } } ^ { R } }$ . We suppose that $\mathcal { U } _ { s , d _ { r } } ^ { A ^ { K } } \neq \dot { \boldsymbol { \emptyset } } .$ <sup>U</sup> <sup>U</sup> <sup>U</sup>For each iteration t, we can compute corresponding possible and necessary assignments $C _ { t , d _ { r } } ^ { P } ( a )$ and $C _ { t , d _ { r } } ^ { N } ( a )$ for each $a \in A ,$ , as de<sup>fi</sup>ned in [8].

In the context of group decision, let us denote by $\left[ L _ { t , \mathcal { D } ^ { ' } } , R _ { t , \mathcal { D } ^ { ' } } \right] = \cup _ { d _ { r } \in \mathcal { D } ^ { ' } } \left[ L _ { t , d _ { r } } ( a ^ { * } ) , R _ { t , d _ { r } } ( a ^ { * } ) \right]$ . We assume that we pass from $\left[ L _ { t - 1 , \mathcal { D } ^ { ' } } , R _ { t - 1 , \mathcal { D } ^ { ' } } \right] \mathrm { t o } \left[ L _ { t , \mathcal { D } ^ { ' } } , R _ { t , \mathcal { D } ^ { ' } } \right]$ , whenever any decision maker $d _ { r } \in \mathcal { D } ^ { ' }$ adds or makes more precise some exemplary assignments of reference alternatives. Obviously, for all $a \in \ A$ we can compute $C _ { t . \mathcal { D } ^ { ' } } ^ { N , N } ( a ) , C _ { t . \mathcal { D } ^ { ' } } ^ { N , P } ( a ) , C _ { t . \mathcal { D } ^ { ' } } ^ { P , N } ( a )$ , and $C _ { t . \mathcal { D } ^ { ' } } ^ { P , P } ( a )$ . The possible–possible and <sup>D D D D</sup>possible–necessary assignments are expressed as nested sets of classes that correspond to the different con<sup>fi</sup>dence levels.

## 4. Management of incompatible preference statements

Application of the methods introduced in this paper for a set $\mathcal { D } ^ { ' }$ of <sup>D</sup>decision makers is conditioned by the non-emptiness of the set of compatible instances of a preference model for each $d _ { r } \in \mathcal { D } ^ { ' }$ . If it is <sup>D</sup>the case, we are able to compute the necessary and the possible consequences of preference information provided by all DMs, which are subsequently combined into outcomes of the respective GROUP method. Analysis of incompatibility of preference information provided by a single DM is discussed in [6,8], and is inspired by procedures introduced in [22,23]. In this section, we consider the case of incompatibility in the context of group decision. In such a case, there is no instance of a preference model which is compatible with all pieces of preference information of all DMs.

Given a set of DMs ${ \mathcal { D } } ^ { \prime } \subseteq { \mathcal { D } } ,$ a value function U is compatible if it satis<sup>fi</sup>es the following set of LP constraints:

$$
\left. \begin{array}{l} \left(E _ {\mathcal {D} ^ {\prime}, X} ^ {A ^ {R}}\right) \\ u _ {j} \left(x _ {j} ^ {k}\right) - u _ {j} \left(x _ {j} ^ {(k - 1)}\right) \geq 0, j = 1, \dots , m, k = 2, \dots , n _ {j} \\ u _ {j} \left(x _ {j} ^ {1}\right) = 0, j = 1, \dots , m, \sum_ {j = 1} ^ {m} u _ {j} \left(x _ {j} ^ {n _ {j}}\right) = 1 \end{array} \right\} \left(E _ {\mathcal {D} ^ {\prime}, \text {group}} ^ {A ^ {R}}\right),
$$

where for ranking problems $\left( E _ { \mathcal { D } ^ { ' } , \mathrm { X } } ^ { A ^ { ' } } \right) = \left( E _ { \mathcal { D } ^ { ' } , \mathrm { r a n k } } ^ { A ^ { ' } } \right)$ , such that:

$$
\left. \begin{array}{l} U (a ^ {*}) \geq U (b ^ {*}) + \varepsilon \text {   if   } a ^ {*} \succ_ {d _ {r}} b ^ {*} \\ U (a ^ {*}) = U (b ^ {*}) \text {   if   } a ^ {*} \sim_ {d _ {r}} b ^ {*} \end{array} \right\} \forall (a ^ {*}, b ^ {*}) \in B _ {d _ {r}} ^ {R}, d _ {r} \in \mathcal {D} ^ {\prime} \Bigg \} \left(E _ {\mathcal {D} ^ {\prime}, \mathrm{rank}} ^ {A ^ {R}}\right),
$$

or for sorting problems $\biggl ( E _ { \mathcal D ^ { \prime } , X } ^ { A ^ { ^ { R } } } \biggr ) = \biggl ( E _ { \mathcal D ^ { \prime } , \mathrm { s o r t } } ^ { A ^ { ^ { R } } } \biggr )$ , such that:

$$
\begin{array}{l} U (a ^ {*}) \geq U (b ^ {*}) + \varepsilon , \forall a ^ {*} \in A _ {d _ {i}} ^ {R}, b ^ {*} \in A _ {d _ {j}} ^ {R} \\ \text { such   that } L _ {d _ {i}} (a ^ {*}) > R _ {d _ {j}} (b ^ {*}), d _ {i}, d _ {j}, \in \mathcal {D} ^ {\prime} \Bigg \} \left(E _ {\mathcal {D} ^ {\prime}, \text { sort }} ^ {A ^ {R}}\right). \end{array}
$$

Notice that the set of compatible value functions $\boldsymbol { \mathcal { U } } _ { \mathcal { D } ^ { ' } }$ is not empty if the optimal value of ε (let us denote it by $\varepsilon ^ { * } )$ <sup>UD</sup>obtained by the maximization of ε, subject to the set of constraints $\left( E _ { \mathcal { D } ^ { ' } , \mathrm { g r o u p } } ^ { A ^ { R } } \right)$ , is greater than 0, i.e. $\boldsymbol { \mathcal { U } } _ { \mathcal { D } ^ { ' } }$ ≠t if and only if $\boldsymbol { \varepsilon } ^ { * } > 0$

<sup>UD</sup>Suppose that $\boldsymbol { \mathcal { U } } _ { \mathcal { D ^ { \prime } } }$ is empty. As $\boldsymbol { \mathcal { U } } _ { \mathcal { P ^ { \prime } } }$ corresponds to the intersection <sup>UD UD</sup>of sets of compatible value functions for all $d _ { r } \in \mathcal { D } ^ { \prime }$ (each one being non-empty), this means that exemplary decisions of at least two DMs are contradictory. Identifying which are these contradictory statements amounts at solving inconsistency. This can be achieved by solving the following mixed integer programming (MIP) problem:

Minimize $: f = \sum _ { a ^ { * } b ^ { * } \in \mathrm { c o n d i t i o n } ( a ^ { * } b ^ { * } ) } v _ { a ^ { * } , b ^ { * } }$

s.t. $\left( E _ { \mathcal { D } ^ { ' } , \mathrm { g r o u p } } ^ { A ^ { R } } \right)$ , where for ranking problems condition $( a ^ { * } b ^ { * } ) = a ^ { * } \succsim _ { d _ { r } } b ^ { * }$ for each $d _ { r } \in \boldsymbol { D } ^ { ' }$ , and $\biggl ( E _ { \mathcal { D } ^ { ' } , X } ^ { A ^ { ' } } \biggr ) = \biggl ( E _ { \mathcal { D } ^ { ' } , \mathrm { r a n k } } ^ { A ^ { ' } } \biggr )$ , such that:

$$
\left. \begin{array}{l} U (a ^ {*}) + M v _ {a ^ {*}, b ^ {*}} \geq U (b ^ {*}) + \varepsilon \text {if} a ^ {*} \succ_ {d _ {r}} b ^ {*}, d _ {r} \in \mathcal {D} ^ {\prime} \\ U (a ^ {*}) + M v _ {a ^ {*}, b ^ {*}} \geq U (b ^ {*}) \\ U (b ^ {*}) + M v _ {a ^ {*}, b ^ {*}} \geq U (a ^ {*}) \end{array} \right\} \text {if} a ^ {*} \sim_ {d _ {r}} b ^ {*}, d _ {r} \in \mathcal {D} ^ {\prime} \Bigg \} \binom{E _ {\mathcal {D} ^ {\prime}, \mathrm{rank}} ^ {A ^ {R}}}{\text {if}}
$$

or for sorting problems condition a $\mathbf { \Phi } ^ { * } b ^ { * } ) = L _ { d _ { i } } ( a ^ { * } ) > R _ { d _ { i } } ( b ^ { * } )$ ; for $d _ { i } , d _ { j } { \in } \mathcal { D } ^ { ' }$ and $\biggl ( E _ { \mathcal D ^ { \prime } , \mathcal X } ^ { A ^ { R } } \biggr ) { } = \biggl ( E _ { \mathcal D ^ { \prime } , \mathrm { s o r t } } ^ { A ^ { R } } \biggr )$ , such that:

$$
\left. \begin{array}{l} U (a ^ {*}) - U (b ^ {*}) + M v _ {a ^ {*}, b ^ {*}} \geq \varepsilon , \forall a ^ {*} \in A _ {d _ {i}} ^ {R}, b ^ {*} \in A _ {d _ {j}} ^ {R}, \\ \text { such   that } L _ {d _ {i}} (a ^ {*}) > R _ {d _ {j}} (b ^ {*}), d _ {i}, d _ {j} \in \mathcal {D} ^ {\prime} \end{array} \right\} \left(E _ {\mathcal {D} ^ {\prime}, \text { sort }} ^ {A ^ {R}}\right) ^ {\prime},
$$

where $M > 1$ and $v _ { a ^ { * } , b ^ { * } }$ are binary variables. If $v _ { a ^ { * } , b ^ { * } } = 1$ , then the corresponding constraint is always satis<sup>fi</sup>ed, which is equivalent to elimination of this constraint. The optimal solution of the above program indicates one of the minimal subsets of constraints being the cause of incompatibil ity. Other subsets can be identi<sup>fi</sup>ed by adding constraints that forbid <sup>fi</sup>nd ing again the same solutions which have been already identi<sup>fi</sup>ed in the previously conducted optimizations:

$$
\sum_ {(a ^ {*}, b ^ {*}) \in S _ {i}} v _ {a ^ {*}, b ^ {*}} \leq f _ {i} ^ {*} - 1,
$$

where $f _ { i } ^ { * }$ is the optimal value of the objective function in the i-th iteration, $S _ { i } { = } \{ ( a ^ { * } , b ^ { * } ) { : } v _ { a ^ { * } , b ^ { * } } ^ { * { i } } { = } 1 \}$ , and $v _ { a ^ { * } , b ^ { * } } ^ { * _ { i } }$ are the values of the binary variables at the optimum found while identifying i-th minimal subset underlying incompatibility.

Note, however, that dealing with inconsistency in this way could be perceived as unfair by some DMs, because it could lead to removal of a signi<sup>fi</sup>cant subset of preferences of a particular DM, while preserving all statements of all other DMs. We could prevent such situations by accounting for minimization of the maximal number $v _ { \mathcal { D } ^ { ' } }$ of <sup>D</sup>pieces of preference information of each DM that should be removed. For example, in case of ranking problems, this could be achieved through solving the following MIP problem:

$$
\begin{array}{c} \text {Minimize:} v _ {\mathcal {D} ^ {\prime}}, \\ s. t. \quad \left. \begin{array}{l} E _ {\mathcal {D} ^ {\prime}, \text {group}} ^ {A ^ {R}} \\ v _ {\mathcal {D} ^ {\prime}} \geq v _ {d _ {r}} \\ v _ {d _ {r}} = \sum_ {a ^ {*} \left\{\succ_ {d _ {r}}, \sim_ {d _ {r}} \right\} b ^ {*}} v _ {a ^ {*} b ^ {*}}, \text {for each} d _ {r} \in \mathcal {D} ^ {\prime} \end{array} \right\} \left(E _ {\mathcal {D} ^ {\prime}, \text {group}} ^ {A ^ {R}, \text {min max}}\right), \end{array}
$$

where $v _ { d _ { r } }$ is a variable de<sup>fi</sup>ned separately for each DM that identi<sup>fi</sup>es the number of removed pieces of preference information which were provided by her/him. Other minimal subsets can be identi<sup>fi</sup>ed analogously to the previous case.

In general, the algorithms presented in this paper provide several subsets of constraints among which the DMs must choose to retrieve a consistent collective model. Obviously, these alternative solutions for removing incompatibility are presented to the DMs in the form of pairwise comparisons or assignment examples. Revealing such different possibilities is informative for negotiations between DMs. Moreover, knowing the various ways of solving inconsistency permits them to understand the con<sup>fl</sup>icting aspects of their statements, to learn about their preferences, and to make the elicitation process more flexible

In case DMs provided con<sup>fi</sup>dence levels for pieces of their preference information, we could differentiate the weight of each piece, and in this way pay attention of the DMs to some particular subsets. In this case, once all the minimal subsets of pieces of preference information causing incompatibility are identi<sup>fi</sup>ed, for each of them we need to analyze con-<sup>fi</sup>dence levels associated with pairs $\{ ( a ^ { * } , b ^ { * } ) : v _ { a ^ { * } b ^ { * } } = 1 \}$ . This would allow indication of the subset for which one of the following objectives is minimal:

• comprehensive sum of con<sup>fi</sup>dence levels for all DMs,

• maximal sum of con<sup>fi</sup>dence levels for any DM,

• maximal con<sup>fi</sup>dence level of any piece of preference information for any DM.

Evaluation table for the problem of ranking sales managers.

<table><tr><td>ID</td><td>Name</td><td> $g_1$ </td><td> $g_2$ </td><td> $g_3$ </td></tr><tr><td>I</td><td>Alexievich</td><td>4</td><td>16</td><td>63</td></tr><tr><td>II</td><td>Bassama</td><td>28</td><td>18</td><td>28</td></tr><tr><td>III</td><td>Calvet</td><td>26</td><td>40</td><td>44</td></tr><tr><td>IV</td><td>Dubois</td><td>2</td><td>2</td><td>68</td></tr><tr><td>V</td><td>El Mrabat</td><td>18</td><td>17</td><td>14</td></tr><tr><td>VI</td><td>Feeret</td><td>35</td><td>62</td><td>25</td></tr><tr><td>VII</td><td>Fleichman</td><td>7</td><td>55</td><td>12</td></tr><tr><td>VIII</td><td>Fourny</td><td>25</td><td>30</td><td>12</td></tr><tr><td>IX</td><td>Frechet</td><td>9</td><td>62</td><td>88</td></tr><tr><td>X</td><td>Martin</td><td>0</td><td>24</td><td>73</td></tr><tr><td>XI</td><td>Petron</td><td>6</td><td>15</td><td>100</td></tr><tr><td>XII</td><td>Psorgos</td><td>16</td><td>9</td><td>0</td></tr><tr><td>XIII</td><td>Smith</td><td>26</td><td>17</td><td>17</td></tr><tr><td>XIV</td><td>Varlot</td><td>62</td><td>43</td><td>0</td></tr><tr><td>XV</td><td>Yu</td><td>1</td><td>32</td><td>64</td></tr></table>

Preference information provided by each DM in in the <sup>fi</sup>rst iteration.

<table><tr><td colspan="2">Pairwise comparisons</td></tr><tr><td> $d_{1}$ </td><td>(Calvet (III) &gt; Dubois (IV)), (Feeret (VI), Alexievich (I) &gt; Bassama (II))</td></tr><tr><td> $d_{2}$ </td><td>(Fourny (VIII) &gt; Bassama (II), Petron (XI)), (Alexievich (I) &gt; El Mrabat (V)), (Varlot (XIV) &gt; Petron (XI))</td></tr><tr><td> $d_{3}$ </td><td>(Yu (XV) ≈ Alexievich (I) &gt; Smith (XIII)), (Fleichman (VII) &gt; Bassama (II))</td></tr></table>

## 5. Illustrative examples

In this section, we illustrate how a decision aiding process can be supported by the introduced methods. We will use $\mathsf { \bar { U } \bar { I } \bar { A } ^ { G M S } }$ -GROUP for considering the problem which has been originally discussed in [6], and we show results of UTADIS<sup>GMS</sup>-GROUP on the example from [32], which has been reconsidered in [8] to illustrate application of the UTADIS<sup>GMS</sup> method. The results are computed using implementation of the methods on the Decision Desktop platform [28]. Some implementation issues, presentation of the UTA<sup>GMS</sup>-GROUP and UTADIS<sup>GMS</sup>-GROUP systems in the framework of the Decision Desktop platform, as well as a general scheme of their use in real-world decision processes, are provided in e-Appendix G.

## 5.1. Ranking problem: ordering sales managers

A medium size <sup>fi</sup>rm wants to hire new international sales managers. A recruitment agency has interviewed 15 potential candidates which have been evaluated on 3 criteria (sales management skills (g ), international experience (g ), and human qualities $\left( g _ { 3 } \right) )$ with a [0,100] scale. The evaluations of candidates are provided in Table 2.

There are three DMs in the agency who have attended the interviews. They constitute a selection committee which should indicate the small subset of the best sales managers, or from another perspective, eliminate the greatest number of relatively bad candidates. Let us denote them by $\mathcal { D } = \{ d _ { 1 } , d _ { 2 } , d _ { 3 } \}$ . They are able to express con<sup>fi</sup>dent judgments <sup>D</sup>about some candidates which form their own sets of reference alternatives. Preference information provided by each of the DMs is presented in Table 3.

In the following step of the method, we verify whether for this initial preference information the set of compatible value functions $\mathcal { U } _ { A ^ { R } , d _ { r } }$ for each $d _ { r } \in \mathcal { D } ,$ , and the set of compatible value function $\mathcal { U } _ { \mathcal { D } }$ <sup>U</sup> for all DMs <sup>D UD</sup>are not empty. If there would be no instance of a preference model which is compatible with all pieces of preference information of all DMs, the DMs whose statements underly incompatibility would be asked to reconsider their preference information. The presentation of the subsets of pairwise comparisons underlying incompatibility allows easy identi<sup>fi</sup>cation of the reasons of the con<sup>fl</sup>ict. In this case, preference information of all DMs is consistent, so we can compute the necessary and the possible weak preference relations $\smash { a \gtrsim _ { d _ { r } } ^ { N } }$ b and $\smash { a \gtrsim _ { d _ { r } } ^ { P } }$ b for all a $\mathbf { \boldsymbol { \mathbf { \mathit { 1 } } } } , \mathbf { \boldsymbol { b } } \in \mathbf { \boldsymbol { A } }$ for $d _ { r } , r = 1 , 2 , 3$ . Generally, it shall consist in solving $2 \times 3 \times$ $1 5 ^ { 2 }$ small LP problems, i.e. for 3 DMs $1 5 ^ { 2 } ~ \mathrm { L P }$ problems to verify the truth of $\succeq _ { d _ { r } } ^ { N }$ and $1 5 ^ { 2 }$ LP problems for checking the truth of $\succcurlyeq { 2 }$ for all $( a , b ) { \in } A \times A$ . However, one can limit the number of LP problems which need to be solved, knowing that $\succsim ^ { N }$ and $\succsim { } ^ { P }$ are re<sup>fl</sup>exive, that they hold for all $a , b \in A$ such that $a \Delta b ,$ and that $\succsim d _ { r } \subseteq \succsim q _ { r } ^ { P }$ for each $d _ { r } \in \mathcal { D } .$ Note, however, that all optimization problems solved <sup>D</sup>within the framework of the proposed methods are relatively small linear programs, so their solution requires a computational effort which is much lower than the capacity of popular linear programming solvers.

Subsequently, the necessary and the possible consequences of preference information given by each DM are combined into consensus results using the framework which is provided by the ${ \mathrm { U T A } } ^ { \mathrm { G M S } } .$ -GROUP. They are presented in Table 4. For the compactness of their presentation we associate with the set of three involved DMs the string of three signs. The position of each sign in the string corresponds to the identi<sup>fi</sup>er of the DM. The signs should be interpreted in the following way when considering the results computed for the given DM:

• N — a (alternative from the row) is necessarily weakly preferred to b (alternative from the column),

• P — a is possibly weakly preferred to b,

• ∗ — a is not even possibly weakly preferred to b.

With respect to the results of ${ \mathrm { U T A } } ^ { \mathrm { G M S } } .$ -GROUP:

$a { \gtrsim } _ { \mathcal { D } } ^ { N , N }$ b iff the cell (a,b) is <sup>fi</sup>lled with “NNN” (e.g., (II,V)),

$a { \mathrm { \lesssim } } _ { \mathcal { D } } ^ { \tilde { N } , P }$ b iff in the cell (a,b) there is at least one $^ { \mathfrak { a } } N ^ { \prime \prime } \left( \mathbf { e . g . } , ( I I I , I V ) \right)$

$a { \gtrsim } _ { \mathcal { D } } ^ { \mathcal { P } , N }$ b iff in the cell (a,b) there is not any “\*” (e.g., (I,II), (I,III)), $a { \gtrsim } _ { - { \mathscr { D } } } ^ { P , P }$ b iff in the cell (a,b) there is at least one $" P "$ or $" N "$ (e.g., (I,IX), $\left( I , X \right) )$

The matrix of $\succsim _ { 1 , D } ^ { N , N } , \succ _ { 1 , D } ^ { N , P } , \succ _ { 1 , D } ^ { P , N }$ ; and $\succsim _ { 1 , { \mathcal { D } } } ^ { P , P }$ relations in the <sup>fi</sup>rst iteration for all subsets of DMs for the problem of ranking sales managers (N and P at the given position indicate DMs for <sup>D D D D</sup>whom the necessary and possible relation hold, respectively).

<table><tr><td></td><td>I</td><td>II</td><td>III</td><td>IV</td><td>V</td><td>VI</td><td>VII</td><td>VIII</td><td>IX</td><td>X</td><td>XI</td><td>XII</td><td>XIII</td><td>XIV</td><td>XV</td></tr><tr><td>I</td><td>NNN</td><td>NPP</td><td>PPP</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PPP</td><td>P**</td><td>PPP</td><td>PPP</td><td>NNN</td><td>NPN</td><td>PPP</td><td>PPP</td></tr><tr><td>II</td><td>* PP</td><td>NNN</td><td>P* P</td><td>PPP</td><td>NNN</td><td>***</td><td>PP*</td><td>P* P</td><td>* P*</td><td>PPP</td><td>PPP</td><td>NNN</td><td>NNN</td><td>PPP</td><td>PPP</td></tr><tr><td>III</td><td>PPP</td><td>PNP</td><td>NNN</td><td>NNP</td><td>NNN</td><td>PPP</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PNP</td><td>NNN</td><td>NNN</td><td>PPN</td><td>PPP</td></tr><tr><td>IV</td><td>PPP</td><td>PPP</td><td>** P</td><td>NNN</td><td>PPP</td><td>P* P</td><td>PPP</td><td>P* P</td><td>P**</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>P* P</td><td>PPP</td></tr><tr><td>V</td><td>***</td><td>PPP</td><td>P* P</td><td>PPP</td><td>NNN</td><td>***</td><td>PP*</td><td>P* P</td><td>***</td><td>PPP</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PP*</td></tr><tr><td>VI</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PNP</td><td>NNN</td><td>NNN</td><td>NNN</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PNP</td><td>NNN</td><td>NNN</td><td>PPN</td><td>PPP</td></tr><tr><td>VII</td><td>PPP</td><td>PPN</td><td>PPP</td><td>PPP</td><td>PPN</td><td>PPP</td><td>NNN</td><td>PPP</td><td>***</td><td>PPP</td><td>PPP</td><td>PPN</td><td>PPN</td><td>PPP</td><td>PPP</td></tr><tr><td>VIII</td><td>PPP</td><td>PNP</td><td>PPP</td><td>PNP</td><td>PNP</td><td>PPP</td><td>PPP</td><td>NNN</td><td>* P*</td><td>PPP</td><td>PNP</td><td>NNN</td><td>PNP</td><td>PPN</td><td>PPP</td></tr><tr><td>IX</td><td>NNN</td><td>NPN</td><td>PPP</td><td>NNN</td><td>NNN</td><td>PPP</td><td>NNN</td><td>NPN</td><td>NNN</td><td>NNN</td><td>PPP</td><td>NNN</td><td>NPN</td><td>PPN</td><td>NNN</td></tr><tr><td>X</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td></tr><tr><td>XI</td><td>PPP</td><td>PPP</td><td>P* P</td><td>NNN</td><td>PPP</td><td>P* P</td><td>PPP</td><td>P* P</td><td>PPP</td><td>PPP</td><td>NNN</td><td>NNN</td><td>PPP</td><td>P* P</td><td>PPP</td></tr><tr><td>XII</td><td>***</td><td>PP*</td><td>P**</td><td>PPP</td><td>PP*</td><td>***</td><td>PP*</td><td>P**</td><td>***</td><td>PPP</td><td>***</td><td>NNN</td><td>PP*</td><td>P* P</td><td>PP*</td></tr><tr><td>XIII</td><td>* P*</td><td>PPP</td><td>P* P</td><td>PPP</td><td>NNN</td><td>***</td><td>PP*</td><td>P* P</td><td>* P*</td><td>PPP</td><td>PPP</td><td>NNN</td><td>NNN</td><td>PPP</td><td>PP*</td></tr><tr><td>XIV</td><td>PPP</td><td>PPP</td><td>PP*</td><td>PNP</td><td>PPP</td><td>PP*</td><td>PPP</td><td>PP*</td><td>PP*</td><td>PPP</td><td>PNP</td><td>NNN</td><td>PPP</td><td>NNN</td><td>PPP</td></tr><tr><td>XV</td><td>PPN</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPN</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPN</td><td>PPN</td><td>PPP</td><td>NNN</td></tr></table>

One can see that the inferred model restores preference information provided by all DMs (e.g., (Calvet $\succeq _ { d _ { 1 } } ^ { N }$ Dubois), $\mathrm { ( Y u ~ } \succeq _ { d _ { 3 } } ^ { N }$ Alexievich)). In the <sup>fi</sup>rst iteration, when preference information is yet rather poor, the possible–possible is very rich, i.e., for most pairs of managers (a,b) it is true that $\overset { \cdot } { a } \overset { P , P } { \sim } \overset { P , P } { D } b$ , as well as that $b { \gtrsim } _ { \mathcal { D } } ^ { P , P } ($ a. In particular, there are only 9 or-<sup>D</sup>dered pairs of alternatives $( a , b )$ <sup>D</sup>for which the possible-possible relation does not hold, i.e. not $\left( a \mathfrak { z } _ { \mathcal { D } } ^ { P , \dot { P } } b \right)$ , and 176 ordered pairs for which the pos-<sup>D</sup>sible–necessary relation is true, i.e., (a,b) such that $a { \mathrm { z } } _ { \mathcal { D } } ^ { P , N } l$ . On the other <sup>D</sup>hand, it is rather unusual that one alternative is at least good as another alternative for all compatible value functions for any DM. Thus, the necessary–possible $\gtrsim _ { \mathcal { D } } ^ { N , P }$ relation, and in particular the necessary–necessary $\succeq _ { \mathcal { D } } ^ { N , N }$ <sup>D</sup>relation, is rather poor. This con<sup>fi</sup>rms that taking into account all cri-<sup>D</sup>teria values as characteristic points increases the degree of freedom in assessing the compatible value functions. This feature is not, however, a disadvantage of the presented methodology, because we are looking for robust conclusions. Therefore, we want to explore the whole space of compatible value functions, which is not the case when a limited set of characteristic points and a linear interpolation between them is considered. Obviously, it holds $\succsim _ { 1 , \mathcal { D } } ^ { N , N } \subseteq \gtrsim _ { 1 , \mathcal { D } } ^ { N , P } \subseteq \stackrel { \bullet } { \sim } _ { 1 , \mathcal { D } } ^ { P , P }$ and $\succsim _ { 1 , \mathcal { D } } ^ { N , N } \subseteq _ { \sim _ { 1 , \mathcal { D } } } ^ { \succ _ { p , N } } \subseteq _ { 1 , \mathcal { D } } ^ { P , P }$

<sup>D D</sup>The preference relations obtained from $\succsim _ { 1 , \mathcal { D } } ^ { N , N } , \succsim _ { 1 , \mathcal { D } } ^ { N , P } , \succeq _ { 1 , \mathcal { D } } ^ { P , N } ,$ <sup>D</sup>; and $\succsim _ { 1 , \mathcal { D } } ^ { P , P } ,$ <sup>D D D D</sup>constitute the corresponding rankings, which should be used to work out a <sup>fi</sup>nal recommendation. The DMs could view outcomes of UTA<sup>GMS</sup> designed for a single DM and results of the $\mathrm { U T A } ^ { \mathrm { G M S } }$ -GROUP method, which enables them to get their own clear view of the problem and to compare consequences of one's own decisions with the collective decision of the whole group of DMs. In case of ranking problems, they are asked to pay special attention to the necessary–necessary results, which correspond to the most certain recommendation (see Fig. 1).

However, the $\mathrm { U T A } ^ { \mathrm { G M S } }$ -GROUP method is intended to be used interactively, so that the DMs could provide pairwise comparisons incrementally, looking at consequences of the introduced preference information. Therefore, we will discuss the <sup>fi</sup>nal results after the second iteration. Interaction with the method by providing further reference statements may be encouraged by suggestion of the pairs of alternatives for which it would be useful to get opinion of a particular DM. Such additional pairwise comparisons should intend to enrich the necessary–necessary relation. Therefore, in the <sup>fi</sup>rst order the DMs may be asked to con<sup>fi</sup>rm the truth of the preference relation for pairs of alternatives (a,b) satisfying the following:

$a { \gtrsim } _ { \mathcal { D } } ^ { P , N } b ,$ , which means that all DMs agree that a is possibly at least as <sup>D</sup>good as b,

Additional preference information provided by each DM in in the second iteration

<table><tr><td></td><td>Additional pairwise comparisons</td></tr><tr><td> $d_1$ </td><td>(Calvet (III) &gt; Petron (XI)), (Feeret (VI) &gt; Varlot (XIV))</td></tr><tr><td> $d_2$ </td><td>(Frechet (IX) &gt; Fourny (VIII)), (Fleichman (VII) &gt; Varlot (XIV))</td></tr><tr><td> $d_3$ </td><td>(Smith (XIII) &gt; Dubois (IV)), (Calvet (III) &gt; Petron (XI))</td></tr></table>

$a { \mathop { \gtrsim } } _ { \mathcal { D } } ^ { N , P } b ,$ which means that at least one DM is certain about the ad-<sup>D</sup>vantage of a with respect to $b ,$

• there is not any other alternative that is preferred to a and b in terms of the $a { \mathop { \simeq } } _ { \mathcal { D } } ^ { \mathcal { N } , N } b$

In this perspective, it is useful for the DMs to analyze the part of the necessary-possible graph concerning alternatives which at the current stage of the interaction could be considered as potential best options. Such a graph is presented in the frame at the bottom of Fig. 1. For the moment being, let us suppose that considering the initial results, our DMs are able to provide additional preference information (see Table 5), although their opinion about the relative comparisons of these candidates may not be as certain as the initial preference information.

One can observe that the relations converge with the growth of the number of pairwise comparisons (see Table 6). Precisely, the necessary– possible and necessary–necessary relations are enriched $( \stackrel { \triangledown _ { \cdot } ^ { N , N } } { \sim } \supseteq \stackrel { \triangledown _ { \cdot } ^ { N , N } } { \sim }$ and $\succ _ { 2 , D ^ { ' } } ^ { N , P } \supseteq \succ _ { 1 , D ^ { ' } } ^ { N , P }$ , e.g., $( \mathsf { C a l v e t } \gtrsim _ { 2 , \mathcal { D } } ^ { N , N }$ Dubois) while not(Calvet $\gtrsim _ { 1 , \mathcal { D } } ^ { N , N }$ <sup>D D</sup>Dubois) <sup>D D</sup>and (Fleichman $\succsim _ { 2 , \mathcal { D } } ^ { N , \bar { P } }$ <sup>D</sup>Petron) while not(Fleichman $\succsim _ { 1 , \mathcal { D } } ^ { \dot { N } , P }$ <sup>D</sup>Petron)), where-<sup>D</sup>as the “possible-” relations are impoverished $\ l ( \mathrel { \gtrsim } _ { 2 . D } ^ { P , N } \subseteq \mathrel { \mathop { \sim } } _ { 1 . D } ^ { P , N }$ and $\succeq _ { 2 , D ^ { ' } } ^ { P , P } \subseteq \succeq _ { 1 , D ^ { ' } } ^ { \bar { P } , P } , \mathrm { e . g . }$ , not(Varlot ${ \succ } _ { 2 , \mathcal { D } } ^ { P , P }$ Feeret) while (Varlot $\stackrel { \triangledown P _ { \ P } P } { \sim } _ { 1 , \mathcal D } ^ { P , P }$ <sup>D</sup>Feeret) <sup>D D</sup>and not(Dubois $\succsim _ { 2 . { \mathcal { D } } } ^ { P , N }$ <sup>D</sup>Fleichman) while (Dubois $\succsim _ { 1 , \mathcal { D } } ^ { P , N }$ Fleichman)). The <sup>D D</sup>indication of the best alternatives and of the worst ones can be based on the following observations:

• There are three alternatives (Calvet, Feeret, and Frechet) for which there is no other alternative which is at least as good as them in the necessary–necessary and necessary–possible rankings, i.e. ∄a∈A, such that $a \neq b$ and $a { \gtrsim } _ { \mathcal { D } } ^ { N , P } b ,$ , with b ∈ {Calvet, Feeret, Frechet}. <sup>D</sup>They need to be perceived as the potential best options.

• There are <sup>fi</sup>ve alternatives (Calvet, Feeret, Frechet, Martin, and Yu) for which at least one instance of a compatible preference model for every DM admits that they are possibly not worse than any other alternative, i.e. ∀a∈A, $a \neq b$ and $b { \overset { \cdot } { \sim } } _ { \mathcal { D } } ^ { { \bar { P } } , N } a ,$ with $b = \{ { \mathrm { C a l v e t } } ,$ <sup>D</sup>Feeret,Frechet,Martin,Yu}. There are also two additional alternatives (Alexievich and Bassama) for which at least one model of any DM con<sup>fi</sup>rms that they may be at least as good as any other alternative, i.e. ∀a∈A,, a≠c and $c { \gtrsim } _ { \mathcal { D } } ^ { P , N } c$ , with c= {Alexievich,Bassama}. <sup>D</sup>They can be viewed as “good” options.

![](/api/attachments/45YHJSBG/fulltext/images/e152ee66e09dea62d00600fe244d2e5c41ef0230944acfd5793e904183aed8da.jpg)  
Fig. 1. Partial preorder $\succsim _ { 1 , \mathcal { D } } ^ { N , N }$ and the graph of the necessary–possible ${ \boldsymbol { \gtrsim } } _ { 1 , { \mathcal { D } } } ^ { N , P }$ relation for the subset of the best alternatives for the problem of ranking sales managers

The matrix o $\succ _ { 2 , D } ^ { N , N } , \succ _ { 2 , D } ^ { N , P } , \succ _ { 2 , D } ^ { P , P N }$ $\mathrm { a n d } \gtrsim _ { 2 , \mathcal { D } } ^ { P , P }$ relations in the second iteration for all subsets of DMs for the problem of ranking sales managers (N and P at the given position indicate DMs <sup>D D D D</sup>for whom the necessary and possible relation hold, respectively).

<table><tr><td></td><td>I</td><td>II</td><td>III</td><td>IV</td><td>V</td><td>VI</td><td>VII</td><td>VIII</td><td>IX</td><td>X</td><td>XI</td><td>XII</td><td>XIII</td><td>XIV</td><td>XV</td></tr><tr><td>I</td><td>NNN</td><td>NPP</td><td>PPP</td><td>PPN</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PPP</td><td>P**</td><td>PPP</td><td>PPN</td><td>NNN</td><td>NPN</td><td>PPP</td><td>PPP</td></tr><tr><td>II</td><td>*PP</td><td>NNN</td><td>P*P</td><td>PPN</td><td>NNN</td><td>*P*</td><td>PP*</td><td>P*P</td><td>**P</td><td>PPP</td><td>PPN</td><td>NNN</td><td>NNN</td><td>PPP</td><td>PPP</td></tr><tr><td>III</td><td>PPP</td><td>PNP</td><td>NNN</td><td>NNN</td><td>NNN</td><td>PPP</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PPP</td><td>NNN</td><td>NNN</td><td>NNN</td><td>PPN</td><td>PPP</td></tr><tr><td>IV</td><td>PP*</td><td>PP*</td><td>***</td><td>NNN</td><td>PPP</td><td>P**</td><td>P**</td><td>P*P</td><td>P**</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PP*</td><td>P*P</td><td>PP*</td></tr><tr><td>V</td><td>***</td><td>PPP</td><td>P*P</td><td>PPP</td><td>NNN</td><td>***</td><td>PP*</td><td>P*P</td><td>***</td><td>PPP</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PP*</td></tr><tr><td>VI</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PNN</td><td>NNN</td><td>NNN</td><td>NNN</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PNN</td><td>NNN</td><td>NNN</td><td>NNN</td><td>PPP</td></tr><tr><td>VII</td><td>PPP</td><td>PPN</td><td>PPP</td><td>PNN</td><td>PPN</td><td>PPP</td><td>NNN</td><td>PPP</td><td>***</td><td>PPP</td><td>PNN</td><td>PNN</td><td>PPN</td><td>PNP</td><td>PPP</td></tr><tr><td>VIII</td><td>PPP</td><td>PNP</td><td>PPP</td><td>PNP</td><td>PNP</td><td>PPP</td><td>PPP</td><td>NNN</td><td>***</td><td>PPP</td><td>PNP</td><td>NNN</td><td>PNP</td><td>PPN</td><td>PPP</td></tr><tr><td>IX</td><td>NNN</td><td>NNN</td><td>PPP</td><td>NNN</td><td>NNN</td><td>PPP</td><td>NNN</td><td>NNN</td><td>NNN</td><td>NNN</td><td>NPP</td><td>NNN</td><td>NNN</td><td>PNP</td><td>NNN</td></tr><tr><td>X</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>NNN</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td></tr><tr><td>XI</td><td>PP*</td><td>PP*</td><td>***</td><td>NNN</td><td>PPP</td><td>PP*</td><td>P**</td><td>P*P</td><td>PP*</td><td>PPP</td><td>NNN</td><td>NNN</td><td>PP*</td><td>P*P</td><td>PP*</td></tr><tr><td>XII</td><td>***</td><td>PP*</td><td>***</td><td>PPP</td><td>PP*</td><td>***</td><td>P**</td><td>P**</td><td>***</td><td>PPP</td><td>***</td><td>NNN</td><td>PP*</td><td>P**</td><td>PP*</td></tr><tr><td>XIII</td><td>*P*</td><td>PPP</td><td>P*P</td><td>PPN</td><td>NNN</td><td>***</td><td>PP*</td><td>P*P</td><td>**P</td><td>PPP</td><td>PPN</td><td>NNN</td><td>NNN</td><td>PPP</td><td>PP*</td></tr><tr><td>XIV</td><td>PPP</td><td>PPP</td><td>PP*</td><td>PNP</td><td>PPP</td><td>***</td><td>P*P</td><td>PP*</td><td>P**</td><td>PPP</td><td>PNP</td><td>NNN</td><td>PPP</td><td>NNN</td><td>PPP</td></tr><tr><td>XV</td><td>PPN</td><td>PPP</td><td>PPP</td><td>PPN</td><td>PPN</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPP</td><td>PPN</td><td>PPN</td><td>PPN</td><td>PPP</td><td>NNN</td></tr></table>

• There are three alternatives (Dubois, Martin, and Psorgos) for which at least one model of every DM admits that they are possibly not better than any other alternative, i.e. ∀a∈A, a≠b and $a { \gtrsim } _ { \mathcal { D } } ^ { P , N } b .$ <sup>D</sup>with b={Dubois,Martin,Psorgos}. There are also seven additional alternatives for which at least one model of any DM con<sup>fi</sup>rms that they can be not better than any other alternative. Therefore, they should be viewed as rather “bad” options (only Alexievich, Calvet, Feeret, Frechet, and Petron are excluded from this set).

• There are <sup>fi</sup>ve alternatives (Dubois, Fleichman, Martin, Psorgos, and Yu) which are not weakly preferred to any other alternative in the necessary–necessary ranking. Dubois, Martin, and Psorgos are not weakly preferred to any other alternative in the necessary–possible ranking, whereas many other alternatives are weakly preferred over them in the “necessary-” rankings. Thus, they should be considered as the potential worst options.

The partial preorder $\succsim _ { 2 , \mathcal { D } } ^ { N , N }$ is illustrated in Fig. 2. The DMs may be <sup>D</sup>satis<sup>fi</sup>ed with the results and indicate three candidates (Calvet, Feeret, and Frechet) as the best ones. Alternatively, they may want to pursue the iterative process, adding some new pairwise comparisons of reference alternatives until they perceive the outcomes of the method as decisive enough to make the choice. The new pairwise comparisons should intend to restrict the number of pairs of alternatives connected by incomparability in terms of the necessary–necessary relation, which should lead to reduction of the set of the best alternatives.

## 5.2. Sorting problem: assigning buses to the classes of technical state

A transport company is about to classify 76 buses into 4 prede-<sup>fi</sup>ned and preference ordered classes $C _ { 1 } { - } C _ { 4 } ,$ such that $C _ { 1 }$ will group the buses being in the worst technical state, needing a vary major revision, $C _ { 2 }$ will group the buses being in the lower-intermediate technical state, needing a major revision, $C _ { 3 }$ will group the buses being in the upper-intermediate technical state, needing a minor revision, and $C _ { 4 }$ will group the buses being in the best technical state, needing no revision. The buses were evaluated according to a total of 8 quantitative criteria re<sup>fl</sup>ecting their performance and technical parameters. The names and types of the criteria along with the performance matrix for a subset of buses are presented in Table 7 (see [32]; a complete data set is provided in e-Appendix H).

In the <sup>fi</sup>rst step of the method, the diagnostic experts are asked to provide possibly imprecise assignments of a few buses to the prede-<sup>fi</sup>ned classes. The experts know relatively well the technical state of some buses, and are able to provide a typical example for each class, as well as some additional imprecise assignments of other buses. Although imprecise statements still leave some freedom in assigning the alternatives to different classes, from another perspective they are very useful, since they exclude from consideration all the remaining classes. The preference information is given in Table 8.

![](/api/attachments/45YHJSBG/fulltext/images/dc0e15445c71328873812fc1b7a49b02aabbe4851a7813305f3a09025864475f.jpg)  
Fig. 2. Partial preorder ${ \boldsymbol { \gtrsim } } _ { 2 , \mathcal { D } } ^ { N , P }$ for the problem of ranking sales managers.

Table 7  
Table of criteria and a part of performance matrix for the problem of assigning buses to the classes of technical state.

<table><tr><td>Code</td><td>Criterion</td><td>Type</td><td>Bus</td><td> $g_1$ </td><td> $g_2$ </td><td> $g_3$ </td><td> $g_4$ </td><td> $g_5$ </td><td> $g_6$ </td><td> $g_7$ </td><td> $g_8$ </td></tr><tr><td> $g_1$ </td><td>Maximum speed</td><td>Gain</td><td> $a_1$ </td><td>90</td><td>2.52</td><td>38</td><td>481</td><td>21.8</td><td>26.4</td><td>0.7</td><td>145</td></tr><tr><td> $g_2$ </td><td>Compression pressure</td><td>Gain</td><td> $a_2$ </td><td>76</td><td>2.11</td><td>70</td><td>420</td><td>22.0</td><td>25.5</td><td>2.7</td><td>110</td></tr><tr><td> $g_3$ </td><td>Blacking</td><td>Cost</td><td> $a_3$ </td><td>63</td><td>1.98</td><td>82</td><td>400</td><td>22.0</td><td>24.8</td><td>3.7</td><td>101</td></tr><tr><td> $g_4$ </td><td>Torque</td><td>Gain</td><td> $a_4$ </td><td>90</td><td>2.48</td><td>49</td><td>477</td><td>21.9</td><td>25.1</td><td>1.0</td><td>138</td></tr><tr><td> $g_5$ </td><td>Summer fuel consumption</td><td>Cost</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td> $g_6$ </td><td>Winter fuel consumption</td><td>Cost</td><td> $a_{74}$ </td><td>87</td><td>2.48</td><td>52</td><td>465</td><td>21.9</td><td>24.6</td><td>1.4</td><td>135</td></tr><tr><td> $g_7$ </td><td>Oil consumption</td><td>Cost</td><td> $a_{75}$ </td><td>86</td><td>2.50</td><td>55</td><td>456</td><td>22.0</td><td>25.1</td><td>1.5</td><td>130</td></tr><tr><td> $g_8$ </td><td>Horse power</td><td>Gain</td><td> $a_{76}$ </td><td>88</td><td>2.52</td><td>46</td><td>472</td><td>21.8</td><td>23.8</td><td>1.1</td><td>141</td></tr></table>

For this initial preference information the sets of compatible value functions $\mathcal { U } _ { A ^ { R } , d _ { r } } , d _ { r } { \in } \mathcal { D } ,$ are not empty. It appears, however, that there is no additive value function $\boldsymbol { \mathcal { U } } _ { \mathcal { D } }$ compatible with the reference <sup>UD</sup>assignments of all DMs, which means that the preference information introduced by at least two DMs is inconsistent. The analysis of incompatibility reveals that assignment $( a _ { 4 0 } \to C _ { 2 } )$ provided by $d _ { 1 }$ and $( a _ { 3 0 }  C _ { 1 } )$ provided by $d _ { 3 }$ cannot be represented together by any additive value function. The two DMs are presented this subset of exemplary assignments as a reason underlying incompatibility. They are asked either to reconsider their statements concerning these two alternatives or to remove it. Suppose that $d _ { 1 }$ modi<sup>fi</sup>es the assignment of $a _ { 4 0 } \mathrm { t } 0 \ C _ { 1 } ,$ . In consequence, the system becomes consistent, and we compute the necessary and the possible weak preference relations $a \gtrsim _ { d _ { r } } ^ { \hat { N } } a ^ { * } , a \gtrsim _ { d _ { r } } ^ { P } a ^ { * } , a ^ { * } \succsim _ { d _ { r } } ^ { N } a , a ^ { * } \succ _ { d _ { r } } ^ { P }$ a for $a \in A$ and $a ^ { * } \in A _ { d _ { r } } ^ { R }$ for $d _ { r } \in \mathcal { D } .$ . It requires solving $( 3 \times 2 \times 6 \times 7 6 )$ <sup>D</sup>LP problems, i.e. for 3 DMs for all ordered pairs $( a , a ^ { * } )$ and $( a ^ { * } , a )$ such that $a \in A$ and $a ^ { * } \in A _ { d _ { r } } ^ { R }$ we need to solve an LP problem which indicates the truth of the necessary and the possible weak preference relations. Further, for each alternative $a \in A$ for each DM, we compute $L _ { d _ { r } } ^ { \mathcal { U } , P } , L _ { d _ { r } } ^ { \mathcal { U } , N } , R _ { d _ { r } } ^ { \mathcal { U } , N } ,$ ;, and $R _ { d _ { r } } ^ { \mathcal { U } , P }$ . Then, on the basis of these indices we specify the possible $C _ { d _ { r } } ^ { P }$ and the necessary $C _ { d _ { r } } ^ { N }$ assignments. Finally, we combine them into consensus results using the framework which is provided by UTADIS<sup>GMS</sup>-GROUP. The results obtained for a few representative alternatives for each DM considered individually, as well as for DMs viewed simultaneously, are presented in Table 9.

The necessary–necessary assignments can be considered as robust with respect to the exemplary judgments of all DMs. One may recognize the obtained necessary–necessary ranges of classes as the “absolutely sure” preference statements. However, in the initial iteration, when preference information is yet rather poor, the possible weak preference relation used to assess the necessary assignments is very rich, i.e., for each DM for most of pairs of buses $( a _ { i } , a _ { k } )$ it is true that $\begin{array} { r } { a _ { i } \succsim _ { d _ { r } } ^ { P } a _ { k } , } \end{array}$ as well as that $a _ { k } \succsim _ { d _ { r } } ^ { P } a _ { i } .$ . Therefore, in most cases, one can observe that $C _ { d _ { r } } ^ { N } ( a ) = \emptyset ,$ which also results in empty necessary–necessary assignments $( C _ { \mathcal { D } } ^ { N , N } ~ ( a ) = \emptyset )$ . Table 10 summarizes non-empty <sup>D</sup>necessary–necessary assignments, which is the case of 9 buses assigned to the extreme classes. With respect to the necessary–possible assignments, they are non-empty if $\hat { C _ { d _ { r } } ^ { N } } ( a ) \neq \varnothing$ for any $d _ { r } \in { \mathcal { D } } .$ . One can observe such non-empty assignments for 27 buses (see Table 10), which means that at least one DM is either sure about their desired class and expresses it directly in her/his preference statements, or all instances of a preference model compatible with her/his preference information con<sup>fi</sup>rm the same resulting assignment. Obviously, for every bus $a \in A ,$ it holds $C _ { \mathcal { D } } ^ { N , N } ( a ) \subseteq C _ { \mathcal { D } } ^ { N , P } \ ( a )$

Exemplary assignments of some reference buses for $d _ { 1 } , d _ { 2 } ,$ and $d _ { 3 } ,$ for the problem of assigning buses to the classes of technical state.

<table><tr><td> $a\in A_{d_1}^R$ </td><td> $L_{d_1}$ </td><td> $R_{d_1}$ </td><td> $a\in A_{d_2}^R$ </td><td> $L_{d_2}$ </td><td> $R_{d_2}$ </td><td> $a\in A_{d_3}^R$ </td><td> $L_{d_3}$ </td><td> $R_{d_3}$ </td></tr><tr><td> $a_1$ </td><td> $C_2$ </td><td> $C_2$ </td><td> $a_1$ </td><td> $C_2$ </td><td> $C_2$ </td><td> $a_{13}$ </td><td> $C_3$ </td><td> $C_3$ </td></tr><tr><td> $a_{32}$ </td><td> $C_3$ </td><td> $C_3$ </td><td> $a_5$ </td><td> $C_3$ </td><td> $C_3$ </td><td> $a_{26}$ </td><td> $C_2$ </td><td> $C_2$ </td></tr><tr><td> $a_{34}$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $a_7$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $a_{30}$ </td><td> $C_1$ </td><td> $C_1$ </td></tr><tr><td> $a_{35}$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $a_{12}$ </td><td> $C_2$ </td><td> $C_2$ </td><td> $a_{35}$ </td><td> $C_3$ </td><td> $C_3$ </td></tr><tr><td> $a_{40}$ </td><td> $C_2$ </td><td> $C_2$ </td><td> $a_{28}$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $a_{42}$ </td><td> $C_2$ </td><td> $C_3$ </td></tr><tr><td> $a_{44}$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $a_{40}$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $a_{74}$ </td><td> $C_4$ </td><td> $C_4$ </td></tr></table>

Table 9  
Computation of the results of UTADIS<sup>GMS</sup>-GROUP for exemplary alternatives for the problem of assigning buses to the classes of technical state.

<table><tr><td>Bus</td><td> $C_{d_1}^P$ </td><td> $C_{d_1}^N$ </td><td> $C_{d_2}^P$ </td><td> $C_{d_2}^N$ </td><td> $C_{d_3}^P$ </td><td> $C_{d_3}^N$ </td><td> $C_{\mathcal{D}}^{N,N}$ </td><td> $C_{\mathcal{D}}^{N,P}$ </td><td> $C_{\mathcal{D}}^{P,N}$ </td><td> $C_{\mathcal{D}}^{P,P}$ </td></tr><tr><td> $a_6$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1$ </td></tr><tr><td> $a_{19}$ </td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1-C_2$ </td><td></td><td> $C_1$ </td><td> $C_1$ </td><td></td><td> $C_1$ </td><td> $C_1$ </td><td> $C_1-C_2$ </td></tr><tr><td> $a_{28}$ </td><td> $C_1-C_3$ </td><td></td><td> $C_2-C_3$ </td><td></td><td> $C_1-C_3$ </td><td></td><td></td><td></td><td> $C_2-C_3$ </td><td> $C_1-C_3$ </td></tr><tr><td> $a_{35}$ </td><td> $C_3-C_4$ </td><td></td><td> $C_3-C_4$ </td><td></td><td> $C_3$ </td><td> $C_3$ </td><td></td><td> $C_3$ </td><td> $C_3$ </td><td> $C_3-C_4$ </td></tr><tr><td> $a_{43}$ </td><td> $C_1-C_3$ </td><td></td><td> $C_2-C_4$ </td><td></td><td> $C_1-C_3$ </td><td></td><td></td><td></td><td> $C_2-C_3$ </td><td> $C_1-C_4$ </td></tr><tr><td> $a_{72}$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $C_4$ </td><td> $C_4$ </td></tr></table>

<sup>D D</sup>The possible–possible assignments review all possible consequences of preference information of all DMs on sorting of the whole set of buses (see Table 11). For most buses the possible–possible assignment is non-univocal. Precisely, we have 9 buses assigned to a single class $C _ { 1 } \ { 0 } \Gamma \ C _ { 4 } ,$ 6 and 22 buses assigned, respectively, to the range of two and three contiguous classes, and 37 buses which can be possibly assigned to all four classes. This means that when choosing randomly a compatible instance of a preference model for any DM, for almost a half of the analyzed buses we cannot exclude any class from the set of possible resulting assignments. Such observation underlines <sup>fl</sup>exibility of the applied preference model.

The ranges of possible–possible classes are usually too general to be decisive enough. Being too wide, they do not allow answering questions about the most characteristic range of classes for each alternative. Instead, one can analyze the possible–necessary assignments, which are formed by the intersection of the possible ranges of classes for all DMs (Table 12). If the possible–necessary assignment was not empty, then at least one compatible preference model for each DM admits assignment to a given class. It needs to be considered as a certain recommendation and consensus solution. Consequently, the DMs are asked to pay special attention to the possible–necessary results for sorting problems. In this case, one can see that the number of buses possibly assigned to all four classes by all DMs has decreased to $6 ,$ and the number of buses which are assigned to more precise ranges consisting of a single class or two contiguous classes has almost tripled. The average width of the possible–necessary assignments for all alternatives is equal to 2.18. If the possible–necessary assignment was empty for some alternative, which is not the case for this particular problem, it would indicate disagreement between DMs.

The illustration of the use of the $\mathrm { U T A D I S } ^ { \mathrm { G M S } }$ -GROUP method will be stopped after the initial stage. However, this approach is intended to be used interactively, so that the DMs could either add some new assignments of reference alternatives or revise the previous judgments. Obviously, it would result in new necessary–necessary, necessary–possible, possible–necessary, and possible–possible assignments. Since the <sup>fi</sup>nal decision is based on $C _ { \mathcal { D } } ^ { P , N }$ , the DMs should be encouraged by the analyst <sup>D</sup>to provide their preferences concerning two types of alternatives:

Necessary–necessary $C _ { \mathcal { D } } ^ { N , N }$ and necessary–possible $C _ { \mathcal { D } } ^ { N , P }$ assignments for the problem of <sup>D</sup>assigning buses to the classes of technical state.

<table><tr><td> $C_{\mathcal{D}}^{N,N}$ </td><td>Assigned buses</td><td> $C_{\mathcal{D}}^{N,P}$ </td><td>Assigned buses</td></tr><tr><td> $C_1$ </td><td> $a_6, a_{23}, a_{40}, a_{60}, a_{62}, a_{69}$ </td><td> $C_1$ </td><td> $a_6, a_{19}, a_{23}, a_{30}, a_{34}, a_{40}, a_{47}, a_{50}, a_{60}, a_{62}, a_{63}, a_{69}$ </td></tr><tr><td> $C_2$ </td><td>-</td><td> $C_2$ </td><td> $a_1, a_{12}, a_{26}$ </td></tr><tr><td> $C_3$ </td><td>-</td><td> $C_3$ </td><td> $a_5, a_{32}, a_{35}$ </td></tr><tr><td> $C_4$ </td><td> $a_{18}, a_{29}, a_{72}$ </td><td> $C_4$ </td><td> $a_7, a_{18}, a_{29}, a_{44}, a_{49}, a_{57}, a_{72}, a_{74}, a_{76}$ </td></tr></table>

Table 11 Possible–possible $C _ { \mathcal { D } } ^ { P , P }$ assignments for the problem of assigning buses to the classes o technical state.

<table><tr><td> $C_{\mathcal{D}}^{P,P}$ </td><td>Assigned buses</td></tr><tr><td> $C_1$ </td><td> $a_6, a_{23}, a_{40}, a_{60}, a_{62}, a_{69}$ </td></tr><tr><td> $C_1 - C_2$ </td><td> $a_{14}, a_{19}$ </td></tr><tr><td> $C_1 - C_3$ </td><td> $a_2, a_5, a_8, a_{12}, a_{21}, a_{24}, a_{26}, a_{27}, a_{28}, a_{30}, a_{34}, a_{36}, a_{38}, a_{39}, a_{45}, a_{46}, a_{47}, a_{48}, a_{50}, a_{63}, a_{66}, a_{67}$ </td></tr><tr><td> $C_2 - C_4$ </td><td> $a_{32}, a_{44}, a_{51}$ </td></tr><tr><td> $C_3 - C_4$ </td><td> $a_{35}, a_{49}, a_{61}$ </td></tr><tr><td> $C_4$ </td><td> $a_{18}, a_{29}, a_{72}$ </td></tr><tr><td> $C_1 - C_4$ </td><td>The remaining 37 buses</td></tr></table>

• these for which the range of possible–necessary assignment is wide at the current stage of the interaction; this would result in the more precise assignment in the following iteration;

• non-reference alternatives, which, when assigned to some class by any DM, may affect possible assignment of numerous set of other alternatives, i.e. these which are necessarily not worse and/or not better than many other alternatives.

## 6. Conclusions

In this paper, we introduced the principle of robust ordinal regression to multiple criteria group decision. After recalling the robust ordinal regression methods within MAUT for choice and ranking problems $( { \mathrm { U T } } { \mathrm { A } } ^ { \mathrm { G M S } }$ and GRIP), and for sorting problems $( \mathrm { U T A D I S } ^ { \mathrm { G M S } } )$ we extended all these methods to multiple criteria group decision problems in UTA<sup>GMS</sup>-GROUP and UTADIS<sup>GMS</sup>-GROUP. For each DM, who expresses her/his individual preferences, we consider all compatible instances of a preference model, and compute the necessary and the possible results. Then, we search for the spaces of consensus and disagreement between the DMs. We present results of this investigation in form of different combinations of the necessary and the possible outcomes, which have several properties of general interest for MCDA and stimulate interactivity of the DMs with the method.

As far as future developments are concerned, we wish to extend other MCDA methods which are based on the principle of robust ordinal regression to group decision, i.e. ELECTRE<sup>GKMS</sup> [10] and PRO-METHEE<sup>GKS</sup> [16]. Note that in this paper, we reasoned only in terms of the necessary and the possible with respect to the set of DMs, avoiding discussions on technical parameters such as weights. In this way, the proposed methods are restricted only to group decision made by a selection committee where all DMs play the same role. An interesting future development concerns differentiation of the roles of the DMs. Moreover, we plan to extend the presented methodology with the selection of the representative preference model. We wish to work out a single preference model and representative results which follow its use, without losing advantage of knowing all compatible instances of a preference model for all DMs (see, e.g., [11,17]). The representative value function or the representative set of parameters are about to highlight the most stable part of the robust results. In this way, we will support the DMs with a very intuitive representation of the output of the robust ordinal regression methods and with an image of an achieved consensus solution. Consequently, we will be able to combine the robustness analysis conducted within $\mathrm { U T A } ^ { \mathrm { G M S } }$ -GROUP, UTADIS<sup>GMS</sup>-GROUP, ELECTRE<sup>GKMS</sup>-GROUP, and PROMETHEE<sup>GKS</sup>-GROUP with the clarity of classical UTA-like and outranking-based methods.

Possible–necessary $C _ { \mathcal { D } } ^ { P , N }$ assignments for the problem of assigning buses to the classes of technical state.

<table><tr><td> $C_{\mathcal{D}}^{P,N}$ </td><td>Assigned buses</td></tr><tr><td> $C_1$ </td><td> $a_6, a_{19}, a_{23}, a_{30}, a_{34}, a_{40}, a_{47}, a_{50}, a_{60}, a_{62}, a_{63}, a_{69}$ </td></tr><tr><td> $C_1 - C_2$ </td><td> $a_8, a_{14}, a_{17}, a_{27}$ </td></tr><tr><td> $C_1 - C_3$ </td><td> $a_2, a_{10}, a_{11}, a_{15}, a_{20}, a_{21}, a_{24}, a_{36}, a_{38}, a_{39}, a_{45}, a_{46}, a_{48}, a_{53}, a_{66}, a_{67}, a_{70}$ </td></tr><tr><td> $C_1 - C_4$ </td><td> $a_3, a_9, a_{16}, a_{52}, a_{58}, a_{68}$ </td></tr><tr><td> $C_2$ </td><td> $a_1, a_{12}, a_{26}$ </td></tr><tr><td> $C_2 - C_3$ </td><td> $a_{25}, a_{28}, a_{31}, a_{41}, a_{42}, a_{43}, a_{64}$ </td></tr><tr><td> $C_2 - C_4$ </td><td> $a_4, a_{13}, a_{22}, a_{33}, a_{37}, a_{55}, a_{56}, a_{59}, a_{65}, a_{71}, a_{73}, a_{75}$ </td></tr><tr><td> $C_3$ </td><td> $a_5, a_{32}, a_{35}$ </td></tr><tr><td> $C_3 - C_4$ </td><td> $a_{51}, a_{54}, a_{61}$ </td></tr><tr><td> $C_4$ </td><td> $a_7, a_{18}, a_{29}, a_{44}, a_{49}, a_{57}, a_{72}, a_{74}, a_{76}$ </td></tr></table>

## Acknowledgments

The second and the fourth authors wish to acknowledge <sup>fi</sup>nancial support from the Polish Ministry of Science and Higher Education, grant no. N N519 441939. We wish to thank four anonymous referees whose comments permitted to improve the previous version of the paper.

## Appendix A. Properties of the relations $\gtrsim ^ { N , N } , \gtrsim ^ { N , P } , \gtrsim ^ { P , N } ,$ , and $\succsim ^ { P , P }$

The following properties of the relations obtained in the ${ \mathrm { U T A } } ^ { \mathrm { G M S } } .$ GROUP help to drive the solution process and to elaborate consensus among DMs. We will start with discussing the link between preference information provided by any decision maker $d _ { r } \in \mathcal { D } ^ { ' } \subseteq \mathcal { D }$ and the results of $\mathrm { U T A } ^ { \mathrm { { \hat { G } M S } } } .$ -GROUP.

Remark Appendix A.1. In the absence of any pairwise comparison of reference alternatives:

1. the necessary–necessary weak preference relation $\succcurlyeq { \mathbf { \Omega } _ { \mathcal { D } ^ { ' } } }$ boils down to weak dominance relation $\Delta$ in A (aΔb $i f f g _ { j } \left( a \right) { \geq } g _ { j } \left( b \right)$ $j = 1 , . . . , m ) ;$ 2. $\gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , P } = \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N }$

<sup>D D</sup>3. the possible–necessary weak preference relation $\succeq _ { \mathcal { D } ^ { ' } } ^ { P , N }$ is a complete relation such that for any pair $a , b \in A { : }$

$\mathrm { ~ - ~ } a \sim _ { \mathcal { D } ^ { ' } } ^ { P , N }$ b⇔[(not(aΔb) and not(bΔa)) or ((aΔb) and (bΔa))],

1 $a \succ _ { \mathcal { D } ^ { ' } } ^ { P , N }$ b⇔[(aΔb) and not(bΔa)];

4. $\succeq _ { \mathcal { D } ^ { ' } } ^ { P , P } = \succeq _ { \mathcal { D } ^ { ' } } ^ { P , N }$ , and thus $\succeq _ { \mathcal { D } ^ { ' } } ^ { P , N }$ is negatively transitive;

<sup>D D D</sup>5. each pairwise comparison provided by the $d _ { r } \in \mathcal { D } ^ { ' }$ , for which the <sup>D</sup>dominance relation does not hold, contributes to enriching $\succeq _ { \mathcal { D } ^ { ' } } ^ { N , P }$ i.e. it makes the relation $\succeq _ { \mathcal { D } ^ { ' } } ^ { N , P }$ <sup>D</sup>true for at least one more pair of alternatives.

The above property allows distinguishing the consequences stemming from the analysis of the sole evaluation matrix from the outcomes resulting from application of preference information provided by the DMs. Moreover, since at the beginning $\gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , P } = \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N }$ and $\succeq _ { \mathcal { D } ^ { ' } } ^ { P , P } = \succeq _ { \mathcal { D } ^ { ' } } ^ { P , N }$ <sup>D D</sup>, one can later observe how these results diverge <sup>D D</sup>with the growth of the preference information.

At any stage of the method, each pairwise comparison provided by $\boldsymbol { d } _ { \boldsymbol { r } } \in \boldsymbol { D } ^ { \prime } \subseteq \mathcal { D }$ is re<sup>fl</sup>ected in the necessary–possible results.

Remark Appendix A.2. For all $a _ { 9 }$ and any decision maker $a _ { 1 6 } \mathrm { : }$

$$
1. a \gtrsim_ {d _ {r}} b \Rightarrow a \gtrsim_ {\mathcal {D} ^ {\prime}} ^ {N, P} b,
$$

2. $a \succ _ { d _ { r } } b \Rightarrow n o t \Big ( b \succ _ { \mathcal { D } ^ { ' } } ^ { P , N } a \Big ) .$

In this way, each DM knows how her/his statements could in<sup>fl</sup>uence the collective results in a direct way. However, the preference information provided by each DM is then translated into the necessary and possible outcomes. The truth of these relations is subsequently re<sup>fl</sup>ected in the necessary–possible and possible–possible results. Their re<sup>fl</sup>ection in the necessary–necessary and possible–necessary outcomes requires con<sup>fi</sup>rmation of the speci<sup>fi</sup>c result by each $d _ { r } \in \mathcal { D } ^ { ' }$ . These observations can also be generalized to any two subsets of $\mathrm { D M s } , \mathcal { D ^ { \prime } } , \mathcal { D ^ { \prime } } \subseteq \mathcal { D }$ such that $\mathcal { D } ^ { ' } \subseteq \mathcal { D } ^ { ' }$ <sup>D D D″</sup>. The above statements can be summarized in formal terms as <sup>D D</sup>follows:

Remark Appendix A.3. For any decision maker $\boldsymbol { d } _ { h } \in \boldsymbol { D } ^ { \prime } \subseteq \boldsymbol { D } \colon$

1. $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N } \subseteq \gtrsim _ { \{ d _ { h } \} } ^ { N , N } = \gtrsim _ { d _ { h } } ^ { N } = \gtrsim _ { \{ d _ { h } \} } ^ { N , P } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , P } , } \end{array}$

$$
\gtrsim_ {\mathcal {D} ^ {\prime}} ^ {P, N} \subseteq \gtrsim_ {\{d _ {h} \}} ^ {P, N} = \gtrsim_ {d _ {h}} ^ {P} = \gtrsim_ {\{d _ {h} \}} ^ {P, P} \subseteq \gtrsim_ {\mathcal {D} ^ {\prime}} ^ {P, P}.
$$

In general, for all $\mathcal { D } ^ { \prime } , \mathcal { D } ^ { \prime \prime } \subseteq \mathcal { D }$ such that $\mathcal { D } ^ { ' } \subseteq \mathcal { D } ^ { ' }$

1. $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , P } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , P } ; } \end{array}$

2. $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , N } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , N } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , P } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , P } . } \end{array}$

The above remark could be also used for the comparison of outcomes obtained for a single DM and collective results. In particular, each DM could view that (s)he is capable of turning the falsity to the truth of the possible–possible and necessary–possible relation for a particular pair of alternatives, and that without her/his con<sup>fi</sup>rmation any possible–necessary and necessary–necessary relation cannot be true.

The interdependencies between $\succeq ^ { N , N } , \succeq ^ { N , P } , \succeq ^ { P , N }$ , and $\succsim ^ { P , P }$ are summarized by Proposition Appendix $\mathsf { A } . 1$

Proposition Appendix A.1. For any subset of decision makers $\mathcal { D } ^ { ' } \subseteq \mathcal { D } \colon$

1. $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , P } , } \end{array}$

2. $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , N } , } \end{array}$

3. $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { \bar { N } , P } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { \bar { P } , P } , } \end{array}$

4. $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , N } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , P } , } \end{array}$

5. $\begin{array} { r } { \gtrsim _ { \mathcal { D } ^ { ' } } ^ { N , N } \subseteq \gtrsim _ { \mathcal { D } ^ { ' } } ^ { P , P } . } \end{array}$

Proof. See e-Appendix C.1. □

Note that being aware about inclusion relations between different types of results helps the analyst to drive the solution process. Since the <sup>fi</sup>nal recommendation should be based on the necessary–necessary relation, which speci<sup>fi</sup>es the most certain recommendation, it should be as rich as possible. This could be achieved by encouraging the DMs to provide additional preference information, which allows turning the truth of $\succsim ^ { P , P }$ (the most general result) into the truth of $\succsim^ { P , N } 0 \bar { \Gamma } \succeq ^ { N , P }$ , and then into the truth of $\succsim ^ { N , N }$ (the most strict result).

The decision support process could also bene<sup>fi</sup>t from Proposition Appendix A.2.

Proposition Appendix ${ \bf A } . 2 . ~ \ \stackrel { \setminus N , N } { \sim }$ is a partial preorder (i.e. a re<sup>fl</sup>exive <sup>D</sup>and transitive binary relation) for all $\mathcal { D } ^ { ' } \subseteq \mathcal { D }$

Proof. See e-Appendix C.2. □

Since the necessary–necessary relation is a partial preorder, it can be presented graphically as a directed acyclic graph in which alternatives that are indifferent are grouped within a single vertex, and directed edges represent the truth of $\succ ^ { N , N }$ relation. When drawing such a graph (also called Hasse diagram), one can take advantage of the transitivity property of $\succ ^ { N , N }$ and show to the DMs an easily interpretable transitivity reduction, which is the graph with the fewest edges that represents the same reachability.

An important property of the preference relations corresponding to different con<sup>fi</sup>dence levels is stated by the following proposition.

Proposition Appendix A.3. $\succsim _ { t , \mathcal { D } ^ { ' } } ^ { N , N } , \succsim _ { t , \mathcal { D } ^ { ' } } ^ { N , P } , \ \succ _ { t , \mathcal { D } } ^ { P , N }$ ; and $\succsim _ { t , \mathcal { D } ^ { ' } } ^ { P , P }$ are nested binary relations:

1. $\begin{array} { r } { \gtrsim _ { t , \mathcal { D } ^ { ' } } ^ { N , N } \supseteq \gtrsim _ { t - 1 , \mathcal { D } ^ { ' } } ^ { N , N } } \end{array}$

2. $\begin{array} { r } { \gtrsim _ { t , \mathcal { D } ^ { ' } } ^ { N , P } \supseteq \gtrsim _ { t - 1 , \mathcal { D } ^ { ' } } ^ { N , P } } \end{array}$

3. $\begin{array} { r } { \gtrsim _ { t , \mathcal { D } ^ { ' } } ^ { P , N } \subseteq \gtrsim _ { t - 1 , \mathcal { D } ^ { ' } } ^ { P , N } } \end{array}$

4. $\succsim _ { t , \mathcal { D } ^ { ' } } ^ { \tilde { P } , \tilde { P } } \subseteq \succsim _ { t - 1 , \mathcal { D } } ^ { \tilde { P } , \tilde { P } }$

Proof. See e-Appendix C.3. □

Consequently, when additional preference information is provided, the necessary–possible and necessary–necessary relations are enriched, whereas the possible–possible and possible–necessary relations are impoverished. In this way, the DMs may control the impact of each piece of information on the evolution of the outcomes.

Appendix B. Properties of the assignments $C ^ { N , N } ( { \pmb a } ) , C ^ { N , P } ( { \pmb a } ) , C ^ { P , N } ( { \pmb a } )$ and ${ \cal C } ^ { P , P } ( { \pmb a } )$

Let us present a few remarks and properties that are satis<sup>fi</sup>ed by the assignments $C ^ { N , N } ( a ) , C ^ { N , P } ( a ) , C ^ { P , N } ( a )$ , and $C ^ { P , P } ( a )$ . To save space, we do not discuss their practical usefulness. It could be explained analogously to the properties presented for ${ \mathrm { U T A } } ^ { \mathrm { G M S } }$ <sup>S</sup>-GROUP in Appendix A.

Remark Appendix B.1. In the absence of any assignment example:

1. the possible–necessary and possible–possible assignments $( C ^ { P , N }$ (a) and $C ^ { P , P } \left( a \right) )$ are equal to the whole range of classes $C _ { 1 } { - } C _ { p } ;$

2. the necessary–necessary and necessary–possible assignments $\dot { ( { C ^ { N , N } } }$ (a) and $C ^ { N , P } \left( a \right) )$ are empty.

Proposition Appendix B.1. Assume that $C _ { \mathcal { D } ^ { ' } } ^ { N , N } \left( a \right)$ and $C _ { \mathcal { D } ^ { ' } } ^ { P , N } \left( a \right)$ are not empty, and denote by $L _ { \mathcal { D } ^ { ' } } ^ { N , N } \left( a \right)$ and $R _ { \mathcal { D } _ { \tau } ^ { \prime } } ^ { N , N } \left( a \right)$ <sup>D D</sup>the worst and the best class of the range $C _ { \mathcal { D } ^ { ' } } ^ { N , N } \left( a \right)$ <sup>D</sup>, and by $L _ { \mathcal { D } ^ { ' } } ^ { P , N } \left( a \right)$ and $R _ { D ^ { \prime } } ^ { P , N } \left( a \right)$ the worst and the <sup>D</sup>best class of the range $C _ { \mathcal { D } ^ { ' } } ^ { P , N } \left( a \right) ^ { ' }$ <sup>D</sup>. For any decision maker $d _ { r } \in \mathcal { D } ^ { ' } \subseteq \mathcal { D }$ <sup>D</sup>and for any of her/his reference alternatives $a ^ { * } \in A _ { d _ { r } } { } ^ { R } \colon$

$1 . \ L _ { \mathcal { D } ^ { ' } } ^ { N , N } ( a ^ { * } ) { \geq } L _ { d _ { r } } ( a ^ { * } )$ and $R _ { \mathcal { D } ^ { ' } } ^ { N , N } ( a ^ { * } ) { \leq } R _ { d _ { r } } ( a ^ { * } )$

2. $L _ { \mathcal { D } ^ { ' } } ^ { P , N } ( a ^ { * } ) { \geq } L _ { d _ { r } } ( a ^ { * } )$ and $R _ { \mathcal { D } ^ { ' } } ^ { P , N } ( a ^ { * } ) { \leq } R _ { d _ { r } } ( a ^ { * } )$

Proof. See e-Appendix E.1. □

Remark Appendix B.2. For any decision maker $\begin{array} { r } { d _ { h } \in \mathcal { D } ^ { ' } \subseteq \mathcal { D } \colon } \end{array}$

$$
C _ {\mathcal {D} ^ {^ {\prime}}} ^ {N, N} (a) \subseteq C _ {\{d _ {h} \}} ^ {N, N} (a) = C _ {d _ {h}} ^ {N} (a) = C _ {\{d _ {h} \}} ^ {N, P} (a) \subseteq C _ {\mathcal {D} ^ {^ {\prime}}} ^ {N, P} (a).
$$

$$
C _ {\mathcal {D} ^ {\prime}} ^ {P, N} (a) \subseteq C _ {\{d _ {h} \}} ^ {P, N} (a) = C _ {d _ {h}} ^ {P} (a) = C _ {\{d _ {h} \}} ^ {P, P} (a) \subseteq C _ {\mathcal {D} ^ {\prime}} ^ {P, P} (a).
$$

In general, for all ${ \mathcal { D } } ^ { \prime \prime } \subseteq { \mathcal { D } } ,$ such that $\mathcal { D } ^ { ' } \subseteq \mathcal { D } ^ { ' }$

$$
C _ {\mathcal {D} ^ {\prime \prime}} ^ {N, N} (a) \subseteq C _ {\mathcal {D} ^ {\prime}} ^ {N, N} (a) \subseteq C _ {\mathcal {D} ^ {\prime}} ^ {N, P} (a) \subseteq C _ {\mathcal {D} ^ {\prime \prime}} ^ {N, P} (a),
$$

$$
C _ {\mathcal {D} ^ {' '}} ^ {P, N} (a) \subseteq C _ {\mathcal {D} ^ {'}} ^ {P, N} (a) \subseteq C _ {\mathcal {D} ^ {'}} ^ {P, P} (a) \subseteq C _ {\mathcal {D} ^ {' '}} ^ {P, P} (a).
$$

Proposition Appendix B.2. For any alternative $a \in A$ and any subset of decision makers $\mathcal { D } ^ { ' } \subseteq \mathcal { D } \colon$

1. $C _ { \mathcal { D } ^ { ' } } ^ { N , N } \left( a \right) \subseteq C _ { \mathcal { D } ^ { ' } } ^ { N , P } \left( a \right) ,$

2. $C _ { \mathcal { D } ^ { ' } } ^ { N , N } \left( a \right) \subseteq C _ { \mathcal { D } ^ { ' } } ^ { P , N } \left( a \right) ,$

3. $C _ { \mathcal { D } ^ { ' } } ^ { N , P } \left( a \right) \subseteq C _ { \mathcal { D } ^ { ' } } ^ { P , P } ( a ) ,$

4. $C _ { \mathcal { D } ^ { ' } } ^ { P , N } \left( a \right) \subseteq C _ { \mathcal { D } ^ { ' } } ^ { P , P } ( a ) ,$

5. $C _ { \mathcal { D } ^ { ' } } ^ { N , N } \left( a \right) \subseteq C _ { \mathcal { D } ^ { ' } } ^ { P , P } ( a ) .$

Proof. See e-Appendix E.2. □

Notice that for both methods introduced in this paper, interdependencies between different types of results can be illustrated in the Hasse diagram (see Fig. B.3).

Proposition Appendix B.3. For all $t = 2 , \ldots , s ,$ and for all $a \in A$

$$
C _ {t, \mathcal {D} ^ {\prime}} ^ {P, P} (a) \subseteq C _ {t - 1, \mathcal {D} ^ {\prime}} ^ {P, P} (a) \quad a n d \quad C _ {t, \mathcal {D} ^ {\prime}} ^ {P, N} (a) \subseteq C _ {t - 1, \mathcal {D} ^ {\prime}} ^ {P, N} (a).
$$

Proof. See e-Appendix E.3. □

![](/api/attachments/45YHJSBG/fulltext/images/f786fa420ac08f0f1c73c42583b56af8e5ddb95cec5760e272174413957732d3.jpg)  
Fig. B.3. Hasse diagram of the four types of results obtained in GROUP methods.

## Appendix C. Supplementary data

Supplementary data to this article can be found online at doi:10. 1016/j.dss.2011.10.005.

## References

[1] S. Angilella, S. Greco, B. Matarazzo, Non-additive robust ordinal regression: a multiple criteria decision model based on the Choquet integral, European Journal of Operational Research 201 (1) (2010) 277–288.

[2] S. Damart, L. Dias, V. Mousseau, Supporting groups in sorting decisions: methodology and use of a multi-criteria aggregation/disaggregation DSS, Decision Suppor Systems 43 (4) (2007) 1464–1475.

[3] Y. Dong, G. Zhang, W-Ch. Hong, Y. Xu, Consensus models for AHP group decision making under row geometric mean prioritization method, Decision Support Systems 49 (3) (2010) 281–289.

[4] J. Figueira, S. Greco, R. Słowiński, Building a set of additive value functions representing a reference preorder and intensities of preference: GRIP method, European Journal of Operational Research 195 (2) (2009) 460–486.

[5] S. Greco, B. Matarazzo, R. Slowinski, Axiomatic characterization of a general utility function and its particular cases in terms of conjoint measurement and rough-set decision rules, European Journal of Operational Research 158 (2) (2004) 271–292.

[6] S. Greco, V. Mousseau, R. Słowiński, Ordinal regression revisited: multiple criteria ranking using a set of additive value functions, European Journal of Operational Research 191 (2) (2008) 415-435.

[7] S. Greco, V. Mousseau, R. Słowiński, The possible and the necessary for multiple criteria group decision, in: F. Rossi, A. Tsoukias (Eds.), Algorithmic Decision Theory (ADT 2009), LNAI 5783, Springer, Berlin, 2009, pp. 203–214.

[8] S. Greco, V. Mousseau, R. Słowiński, Multiple criteria sorting with a set of additive value functions, European Journal of Operational Research 207 (4) (2010) 1455–1470.

[9] S. Greco, R. Słowiński, V. Mousseau, J. Figueira, Robust ordinal regression, in: M. Ehrgott, J. Figueira, S. Greco (Eds.), New Trends in Multiple Criteria Decision Analysis, Springer, 2010, pp. 273–320.

[10] S. Greco, M. Kadziński, V. Mousseau, R. Słowiński, ELECTRE <sup>GKMS</sup>: robust ordinal regression for outranking methods, European Journal of Operational Research 214 (1) (2011) 118-135.

[11] S. Greco, M. Kadziński, R. Słowiński, Selection of a representative value function in robust multiple criteria sorting, Computers and Operations Research 38 (11) (2011) 1620–1637.

[12] C. Hwang, M. Lin, Group decision making under multiple criteria: methods and applications, Lecture Notes in Economics and Mathematical Systems, vol. 281, Springer, Berlin, 1987.

[13] E. Jacquet-Lagrèze, Y. Siskos, Assessing a set of additive utility functions for multicriteria decision making: the UTA method, European Journal of Operational Research.10 (1982)151-164

[14] E. Jacquet-Lagrèze, Y. Siskos, Preference disaggregation: 20 years of MCDA experience, European Journal of Operational Research 130 (2) (2001) 233–245.

[15] M. Jarke, M.T. Jelassi, M.F. Shakun, MEDIATOR: toward a negotiation support system, European Journal of Operational Research 31 (3) (1987) 314–334.

[16] M. Kadziński, S. Greco, R. Słowiński, Extreme ranking analysis in robust ordinal regression, Omega 40 (4) (2012) 488-501.

[17] M. Kadziński, S. Greco, R. Słowiński, Selection of a representative value function for robust multiple criteria ranking and choice, European Journal of Operational Research 217 (3) (2012) 541–553.

[18] R.L. Keeney, H. Raiffa, Decisions with multiple objectives: preferences and value tradeoffs L. Wiley, New York, 1976.

[19] D.M. Kilgour, Y. Chen, K.W. Hipel, Multiple criteria approaches to group decision and negotiation in: M. Ehrgott L. Figueira S. Greco (Eds.) Trends in Multiple Criteria Decision Analysis, vol. 142, Springer, 2010, pp. 317–338.

[20] N.F. Matsatsinis, A.P. Samaras, MCDA and preference disaggregation in group decision support, European Journal of Operational Research 130 (2) (2001) 414–429.

[21] N. Matsatsinis, E. Grigoroudis, A. Samaras, Aggregation and disaggregation of preferences for collective decision-making, Group Decision and Negotiation 14 (2005) 217–232, doi:10.1007/s10726-005-7443-x.

[22] V. Mousseau, L.C. Dias, J. Figueira, C. Gomes, J.N. Clímaco, Resolving inconsistencies among constraints on the parameters of an MCDA model, European Journal of Operational Research 147 (1) (2003) 72–93.

[23] V. Mousseau, L.C. Dias, J. Figueira, Dealing with inconsistent judgments in multiple criteria sorting models, 4OR 4 (3) (2006) 145–158.

[24] Y. Siskos, E. Grigoroudis, Trends in aggregation–disaggregation approaches, in: P.M. Pardalos, D. Hearn, C. Zopounidis, P.M. Pardalos (Eds.), Handbook of Multicriteria Analysis, vol. 103, Springer, 2010, pp. 189–214

[25] Y. Siskos, E. Grigoroudis, N.F. Matsatsinis, UTA methods, in: J. Figueira, S. Greco, M. Ehrgott (Eds.), Multiple Criteria Decision Analysis: State of the Art Surveys, Springer, Boston, 2005, pp. 297–344.

[26] V. Srinivasan, Linear programming computational procedures for ordinal regression, Journal of the ACM 23 (3) (1976) 475–487.

[27] V. Srinivasan, A.D. Shocker, Estimating the weights for multiple attributes in a composite criterion using pairwise judgments, Psychometrika 38 (1973) 473–493.

[28] The web site of the Decision Deck project: http://www.decision-deck.org/.

[29] E. Turban, Decision Support and Expert Systems: Management Support Systems, Prentice Hall PTR, Upper Saddle River, NJ, USA, 1993.

[30] R. Vetschera, Integrating databases and preference evaluations in group decision support: A feedback-oriented approach, Decision Support Systems 7 (1) (1991) 67–77.

[31] L. Yu, K.K. Lai, A distance-based group decision-making methodology for multiperson multi-criteria emergency decision support, Decision Support Systems 51 (2) (2011) 307–315.

[32] J. Żak, J. Stefanowski, Determining maintenance activities of motor vehicles using rough sets approach, Proceeding of Euromaintenance'94 Conference, Amsterdam, 1994, pp. 39–42.

Salvatore Greco is Full Professor at the Faculty of Economics of Catania University since 2001. His main research interests are in the <sup>fi</sup>eld of Multiple Criteria Decision Analysis (MCDA), in the application of rough set approach to decision analysis, in the axiomatic foundation of multi-criteria methodology and in the fuzzy integral approach to MCDA. He is author of many articles published in important international journals and specialized books. Together with Benedetto Matarazzo and Roman Słowiński, he received the Best Theoretical Paper Award by the Decision Sciences Institute (Athens, 1999). Salvatore Greco has been member of the executive committee of the Interna tional Society of Multiple Criteria Decision Making. He is a coeditor of the book Mutiple Criteria Decision Analysis: State of the Art Surveys, and area editor of Journal of Multi-Criteria Decision Analysis. He has been Invited Professor at Poznan University of Technology, at the University of Paris Dauphine, and at Ecole Centrale Paris.

Miłosz Kadziński is an Assistant Professor at the Poznan University of Technology, member of the Laboratory of Intelligent Decision Support Systems (IDSS) within the Institute of Computing Science. He received his M.Sc. in Computer Science (2008) from Poznan University of Technology and expects to defend his Ph.D. thesis in 2012. His main research interests are in Multiple Criteria Decision Analysis (particularly in robust ordinal regression and multiple objective optimization cone contraction methods), text processing, and exploratory data analysis. He is involved in the Decision Deck project as a developer of open source software implementing MCDA methods. He has published his works in journal such as EJOR, OMEGA, GDN, and Computers & OR.

Vincent Mousseau is Professor at Ecole Centrale Paris (ECP), member of the Industrial Engineering Lab- oratory (LGI). He heads the Master's Program in Industrial and Logistic Systems Optimisation at ECP and the research team Optimisation of Production/Distribution Systems at LGI. He received his M.S. (1989), Ph.D. (1993), and Habilitation (2003), all in Computer Science from University of Paris Dauphine. Vincent's Mousseau's research interests include multiple criteria decision aid, and preference modeling and elicitation. He is the president of the Decision Deck Consortium (an international project) which aims at developing open source software implementing MCDA methods). He has published his works in journals such as EJOR, Annals of OR, Computers & OR, DSS, Journal of Global Op timization, Socio-Economic Planning Sciences, Naval Research Logistics, and others.

Roman Słowiński earned his PhD in 1977 in Computer Science from the Poznan University of Technology and Dr. Habil. in Decision Sciences, also from Poznan University of Technology in 1981. He is Professor since 1989 and Founding Head of the Laboratory of Intelligent Decision Support Systems within the Institute of Computing Science, Poznan University of Technology, Poland. Since 2002 he also holds a Professors position at the Systems Research Institute of the Polish Academy of Sciences in Warsaw. Roman Słowiński has conducted extensive research on the methodology and techniques of decision aiding, including multiple criteria decision aiding, preference learning, modeling of uncertainty in decision problems, and knowledge-based decision support. His record of publications includes 14 monographs, and over 380 scienti<sup>fi</sup>c articles in international journals and edited volumes. He is the Editor-in-Chief of the European Journal of Operational Research (EJOR) since 1999, and recipient of the EURO Gold Medal (1991) and the MCDM Societys Edgeworth-Pareto Award (1997). In 2004, he was elected member of the Polish Academy of Sciences. In 2005, he received the Annual Prize of the Foundation for Polish Science, regarded as the most prestigious scientific award in Poland. In 2010 he has been elected President of the International Rough Set Society (IRSS)
