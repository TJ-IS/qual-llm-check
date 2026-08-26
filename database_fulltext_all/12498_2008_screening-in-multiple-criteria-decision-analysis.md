---
otero_id: 12498
otero_key: "KTV9V3V2"
title: "Screening in multiple criteria decision analysis"
authors: "Ye Chen; D. Marc Kilgour; Keith W. Hipel"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.12.017"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Screening in multiple criteria decision analysis

Ye Chen <sup>a</sup>, D. Marc Kilgour <sup>b</sup>, Keith W. Hipel <sup>a,⁎</sup>

<sup>a</sup> Department of Systems Design Engineering, University of Waterloo, Waterloo, Ontario, Canada N2L 3G1 <sup>b</sup> Department of Mathematics, Wilfrid Laurier University, Waterloo, Ontario, Canada

Received 19 January 2007; received in revised form 13 December 2007; accepted 19 December 2007 Available online 4 January 2008

## Abstract

Screening is a process for multiple criteria decision analysis (MCDA) that reduces a large set of alternatives to a smaller set that most likely contains the best choice. To study screening in detail, MCDA is first interpreted as consequence-based preference aggregation. Consequence data and preference expressions (values and weights) are defined and the aggregation steps are elaborated. Based on these concepts, screening and sequential screening are defined and their properties are discussed. Then, it is shown how several popular MCDA methods can be integrated into a decision support system for sequential screening based upon available decision information. Finally, an illustrative application to water supply planning is presented. © 2007 Elsevier B.V. All rights reserved.

Keywords: Multiple criteria decision analysis; Preference information; Screening; Sequential screening; Water supply planning

## 1. Introduction

The task of multiple criteria decision analysis (MCDA) is to help a decision maker (DM) choose, rank or sort alternatives within a finite set according to two or more criteria [23]. During the past few decades, various MCDA methods have been proposed based upon different philosophies such as multi-attribute utility theory [14], outranking methods [26] and the analytic hierarchy process (AHP) [24]. Meanwhile, many decision support systems (DSSs) have been designed in MCDA to assist DMs in analyzing problems and making decisions more easily. For example, within the journal Decision Support Systems, a multiple criteria decision analysis software tool, the Intelligent Decision System, was suggested to help business self-assessment [27], a multicriteria DSS for housing evaluation was proposed [17], and a DSS combining techniques from MCDA and soft systems thinking to tackle complex decision problems was presented in Ref. [19].

For the basic MCDA problem of choosing a best alternative, it is useful for a DM to begin by eliminating those alternatives that do not appear to warrant further attention [12]. This procedure is often called screening. Screening helps by allowing the DM to concentrate on a smaller set that (very likely) contains the best alternative. Many approaches have been adapted for screening alternatives. For example, a case-based distance model for screening is proposed in which criterion weights and a screening threshold are obtained by assessment of a representative case set [6]. However, there has been no comprehensive examination and comparison of these screening techniques in the literature.

A systematic procedure for executing screening is developed in this paper and its usefulness is demonstrated by employing a realworld case study. This approach provides a theoretical framework upon which decision support systems for screening can be constructed. Section 2 interprets MCDA as a consequence-based preferences aggregation procedure, and definitions of consequence data, preference expressions and aggregation are given. Section 3 provides detailed descriptions of screening, sequential screening, and screening properties, and introduces several screening methods in sequence. A sequential screening procedure in water resources planning is demonstrated in Section 4, while Section 5 provides a summary and conclusions as well as suggests future research topics.

## 2. Multiple criteria decision analysis

## 2.1. Basic structure

The analysis procedure of an MCDA problem begins with problem construction which is a serial process of defining objectives, arranging them into criteria, identifying all possible alternatives, and then measuring consequences. A consequence is a direct physical measurement of the success of an alternative according to a criterion such as cost in dollars. Note that in this paper, it is assumed that consequences can be measured without uncertainty.

The basic structure of an MCDA problem established by the above processes is shown in Fig. 1. In this figure, $\overset { \cdot } { \mathbf { A } } = \{ A ^ { 1 } , A ^ { 2 } , . . . , A ^ { i } , . . . , A ^ { n } \}$ is the set of alternatives, and $\mathbf { Q } { = } \{ 1 , ~ 2 , . . . , ~ j , . . . , ~ q \}$ is the set of criteria. The consequence on criterion j of alternative $A ^ { i }$ is expressed as $c _ { j } ( A ^ { i } )$ , which can be shortened to $c _ { j } ^ { i }$ when there is no possibility of confusion. Note that there are n alternatives and q criteria altogether.

## 2.2. Problématiques

Based upon this basic structure, the DM may conceive the decision problem in several ways. Different MCDA problématiques (basic tasks) is suggested in Ref. [23] for a decision problem with alternative set A:

• Choice problématique. Choose the best alternative from A.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="6">Alternatives</td></tr><tr><td> ${A}^{1}$ </td><td> ${A}^{2}$ </td><td>...</td><td> ${A}^{i}$ </td><td>...</td><td> ${A}^{n}$ </td></tr><tr><td rowspan="6">Criteria</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>j</td><td></td><td></td><td></td><td> ${\rightarrow }_{C_{j}}^{i}$ </td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>q</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 1. The structure of MCDA.

• Sorting problématique. Sort all alternatives in A into different groups which are arranged in a preference order.

• Ranking problématique. Rank the alternatives of A from best to worst.

## 2.3. Preference expressions

The DM's preferences are crucial to the solution of any MCDA problem. Different methods have been designed to assist DMs to acquire and aggregate preferences. Here, two kinds of preference expressions are summarized: values (preferences on consequences) and weights (preferences on criteria).

## 2.3.1. Preferences on consequences

There are several ways for a DM to express preferences based directly on consequence data. Among them, the best known are utility theory-based methods [14] and outranking-based approaches [26]. Here, preferences on consequences are captured as values, which are refined data obtained by processing consequence data according to the needs and objectives of the DM. The relation between consequence data and preference data can be expressed as

$$
v _ {j} \left(A ^ {i}\right) = f _ {j} \left(c _ {j} ^ {i}\right)\tag{1}
$$

where $\nu _ { j } ( A ^ { i } ) ( \mathrm { o r } \nu _ { j } ^ { i }$ when no confusion can result) and $c _ { j } ^ { i }$ are a value datum and a consequence datum, respectively; f (∙) is a mapping from consequence data to the relevant values. The value vector for $\boldsymbol { A } ^ { i }$ is $\mathbf { v } ( \boldsymbol { A } ^ { i } ) { = } ( \nu _ { 1 } ( \boldsymbol { A } ^ { i } ) , \nu _ { 2 } ( \boldsymbol { A } ^ { i } ) , { \ldots } , \nu _ { q } ( \boldsymbol { A } ^ { i } ) )$ .

The following basic properties of values are assumed.

## Definition 1.

• Preference availability: The DM can express which of two different consequence data on a criterion is preferred.

• Preference monotonicity: All criteria are either positive or negative, where criterion ${ j } \in \mathbf { Q }$ is positive iff $c _ { j } ( A ^ { l } ) >$ $c _ { j } ( A ^ { m } )$ implies $\nu _ { j } ( A ^ { l } ) \ge \nu _ { j } ( A ^ { m } )$ for all $A ^ { l } , A ^ { m } \in \bar { \mathbf { A } }$ , and negative iff $c _ { j } ( \mathring { A } ^ { l } ) { < } c _ { j } ( \mathring { A } ^ { m } )$ implies $\nu _ { j } ( A ^ { l } ) \ge \nu _ { j } ( A ^ { m } )$ for all $A ^ { l } , A ^ { m } \in \bar { \mathbf { A } }$

## 2.3.2. Preferences on criteria

Preferences on criteria refer to expressions of the relative importance of criteria. Here we assume that these preferences are expressed using weights; the weight for criterion $\scriptstyle j \in \mathbf { Q }$ is $w _ { j } \in \mathbb { R }$ . Usually $w _ { j } { > } 0$ for all criteria, $j ,$ and $\textstyle \sum _ { j \in { \bf Q } } w _ { j } = 1$ . A weight vector is denoted as $\mathbf { w } { = } ( w _ { 1 } , \ \dot { w } _ { 2 } { \ , \cdot } { . } { . } , \ w _ { j } { , \cdot } { . } { . } , \ w _ { q } )$ . Two kinds of weights, tradeoff-based weights and non-tradeoff-based weights, are summarized in Ref. [2]. Tradeoff-based weights emphasize the “compensation” of preferences across criteria, which means that preference data are compared as they are aggregated into a single representative expression. Non-tradeoff-based weights do not contain the feature of direct tradeoffs across criteria; they are usually associated with outranking methods.

## 2.4. Aggregation models in MCDA

After the construction of an MCDA problem and the acquisition of preferences from the DM, a global model to aggregate preferences and solve the specified problématique may be constructed.

For all $A ^ { i } \in \mathbf { A }$

$$
V \left(A ^ {i}\right) = F \left(v \left(A ^ {i}\right), w\right)\tag{2}
$$

where $V ( A ^ { i } )$ is the overall evaluation of alternative $A ^ { i } ,$ $F ( \cdot )$ is a real-numbered mapping from values, $\mathbf { v } ( A ^ { i } )$ , and the weight vector, w, to the overall evaluation result. A popular evaluation method is the simple additive weighting (SAW) method.

$$
V \left(A ^ {i}\right) = \sum_ {j \in \mathbf {Q}} w _ {j} \cdot v _ {j} \left(A ^ {i}\right)\tag{3}
$$

Most aggregation methods in MCDA require three steps:

(1) Obtain preference data and weights.

(2) Aggregate preference data using weights.

(3) Apply final evaluations to meet requirements of a specified task (choice, ranking or sorting).

## 3. Screening techniques in MCDA

## 3.1. Definition

Screening in MCDA can be defined formally as follows.

Definition 2. A screening procedure is any procedure Scr that always selects a non-empty subset of an alternative set A,

$$
\emptyset \neq \operatorname{Scr} (\mathbf {A}) \subseteq \mathbf {A},\tag{4}
$$

where Scr denotes a screening procedure (sometimes subscripts are used to distinguish among different screening procedures), and Scr(A) denotes the screened set (the remaining alternatives) after the procedure Scr was applied to the alternative set A.

Speaking more practically, screening is any process that reduces a larger set of alternatives to a smaller set that (most likely) contains the best choice. An illustration is shown in Fig. 2.

Screening should accomplish the objective of reducing the number of alternatives to be considered. Screening “should eliminate alternatives that are unlikely to be chosen, so that later effort can be focused on the more attractive options [12].” With respect to problématiques in MCDA, we are focusing on a choice problématique, but it should be noted that screening can be interpreted as an application of the sorting problématique, since screening always arranges alternatives into two groups, one of which is “screened out” from further consideration.

## 3.2. Basic properties

## 3.2.1. Safety

A screening procedure for a choice problem, Scr, is safe iff whenever an alternative $A ^ { * }$ is a best choice in Scr(A), $A ^ { * }$ is also a best alternative in A. Fig. 3 shows three screening procedures, $\operatorname { S c r } _ { i } ( \mathbf { A } ) , \operatorname { S c r } _ { j } ( \mathbf { A } )$ and $\operatorname { S c r } _ { k } ( \mathbf { A } )$ (indicated by dashed rectangles), for the alternative set A. Scr (A) and $\operatorname { S c r } _ { j } ( \mathbf { A } )$ are safe screening since both procedures retain $A ^ { * }$ , while $\operatorname { S c r } _ { k } ( \mathbf { A } )$ is not a safe screening and fails to retain $A ^ { * }$

## 3.2.2. Efficiency

If Scr and Scr are distinct safe screening procedures, then Scr is more efficient than $\operatorname { S c r } _ { j } ,$ or a refinement of $\operatorname { S c r } _ { j } ,$ iff $\operatorname { S c r } _ { i } ( \mathbf { A } ) \subseteq \operatorname { S c r } _ { j } ( \mathbf { A } )$ is always true. Fig. 4 demonstrates the efficiency relationship between Scr (A) and $\operatorname { S c r } _ { j } ( \mathbf { A } )$ . Scr (A) is more efficient than $\operatorname { S c r } _ { j } ( \mathbf { A } )$ since $A ^ { * } \in \mathrm { S c r } _ { i } ( A ) , A ^ { * } \in \mathrm { S c r } _ { j } ( A )$ , and $\operatorname { S c r } _ { i } ( \mathbf { A } ) \subseteq \operatorname { S c r } _ { j } ( \mathbf { A } )$

## 3.2.3. Information

In a screening procedure, information refers to preference information provided by the DM. For example, some aspects of the DM's preference may be confirmed without providing complete information. Generally speaking, the more preference information included in a screening procedure, the more alternatives it can screen out. In the extreme case, information may be so strong that only one alternative is left after screening.

![](/api/attachments/KTV9V3V2/fulltext/images/fa4748473292174ad1e5e07bc9d6c1bf98a1ad5465bb685df0b0e96d41332785.jpg)  
Fig. 2. The relation among screening, sorting and choice.

![](/api/attachments/KTV9V3V2/fulltext/images/bd14b14e36e47e9aa56943d382ddd921ad70ebaf0e21b115c9946d79322fc308.jpg)  
Fig. 3. Safety in screening.

Following the discussion of the relationships among consequences, values, weights and aggregation models in Section 2, there are four types of screening information as follows:

• I1: the validation of basic preference properties as defined in Section 2.3.1;

• I2: the application of preference information on consequences;

• I3: the application of preference information on criteria;

• I4: the integration of aggregation models.

It is assumed that if $\mathrm { S c r } _ { 2 }$ is a refinement of $\operatorname { S c r } _ { 1 }$ , then Scr is based on more information than Scr .

## 3.3. Sequential screening

The DM may not be satisfied with the result of an initial screening. If so, other screening procedures may be applied to the screened set. Typically these follow-up procedures are based on more detailed preference information. This process is called sequential screening.

![](/api/attachments/KTV9V3V2/fulltext/images/f46d1782be1127b7d5bef37e6dd8d6f6dd7245ab0020f5e7340aa93db7dc0403.jpg)  
Fig. 4. Efficiency in screening.

Definition 3. Sequential screening is the application of a series of screening procedures in sequence to an alternative set A,

$$
\begin{array}{l} \operatorname{Scr} _ {h, h - 1, \ldots , 1} (\mathbf {A}) \\ = \operatorname{Scr} _ {h} (\operatorname{Scr} _ {h - 1} (\dots (\operatorname{Scr} _ {1} (\mathbf {A})) \dots)), \end{array}\tag{5}
$$

where $\mathrm { S c r } _ { k } , k { = } 1 , 2 . . . , h$ are screening procedures. $\operatorname { S c r } _ { h }$ is the final screening procedure in this sequential screening.

Theorem 1. Sequential screening $\mathrm { S c r } _ { h , \mathrm { h - 1 } , . . . 1 }$ is safe if Scr<sub>k</sub> is safe for $k { = } 1 , 2 , \cdots , h .$

Proof. By hypothesis, $\mathrm { S c r } _ { 1 }$ is safe. Now assume $\mathrm { S c r } _ { k - 1 }$ $k - 2 , . . . , 1$ is safe and consider $\mathrm { S c r } _ { k , k - 1 , . . . , 1 } .$ . Because $\operatorname { S c r } _ { k }$ is safe, a best alternative in $\operatorname { S c r } _ { k , \ k - 1 , \hdots , 1 } ( \mathbf { A } )$ is a best alternative in $\operatorname { S c r } _ { k - 1 , \ k - 2 , \ldots , 1 } ( \mathbf { A } )$ , which by assumption is a best alternative in A. Therefore, Theorem 1 is true by induction. □

## 3.4. Decision information based screening techniques

As stated above, decision procedures using partial preference information can often be adapted for screening. Some popular MCDA methods can be modified for screening; the general relationship among them, grouped by decision information requirements, is shown in Fig. 5.

As shown in Fig. 5, Pareto optimality based screening is a basic screening technique, and we will discuss it first. Other screening techniques based on tradeoff weights, non-tradeoff weights, aspiration levels, and data envelopment analysis (DEA) can be carried out subsequent to Pareto optimality screening. Of course, these methods require more decision information and, when used in sequence, produce refined screening.

![](/api/attachments/KTV9V3V2/fulltext/images/a18a550cfc74e0ca61ca361769f89c0d79797e6b9da8be0a9a5b60d5479f5ed4.jpg)  
Fig. 5. Screening methods and decision information.

## 3.5. Pareto optimality (PO) based screening

Pareto optimality is a famous concept put forward by Ref. [18] and is widely used in economics and elsewhere. It provides a very useful definition of optimality in MCDA because it can be interpreted to take account of multiple aspects (criteria) for overall optimality. The concept of Pareto optimality in MCDA is adapted next.

## 3.5.1. Domination and pareto optimality

Domination is a relation that might or might not hold between two alternatives.

Definition $4 , A ^ { 1 } \in \mathbf { A }$ dominates $A ^ { k } \in \mathbf { A }$ , denoted $A ^ { l } { \succ } A ^ { k }$ iff $\forall j \in \mathbf { Q } , \nu _ { j } ( A ^ { l } ) \geq \nu _ { j } ( A ^ { k } )$ with at least one strict inequality.

Using domination, we define Pareto optimality.

Definition 5. $A ^ { l } \in { \bf A }$ is a Pareto Optimal $( P O )$ alternative, also called an efficient alternative, iff ∄ $A ^ { k } \in \mathbf { A }$ such that $A _ { k } \succ A _ { l } .$ The set of all Pareto optimal alternatives in A is denoted $P O ( A )$

Usually, the information provided by the DM during the screening phase is limited and the DM may prefer not to spend too much energy on comprehensive preference expressions. Then the following theorem shows that by identifying $P O ( A )$ , we carry out PO based direct screening in MCDA based on consequences, provided some properties of preference data hold.

Theorem 2. Assume the basic properties of preference in Definition 1 are satisfied. $\mathbf { A } ^ { 1 } \not \in { \overset { \vartriangle } { P O } } ( \mathbf { A } )$ iff $\exists A ^ { k } \in \mathbf { A }$ such that $\forall j \in \mathbf { Q } , c _ { j } ( A ^ { l } ) \leq c _ { j } ( A ^ { k } )$ when j is a positive criterion and $c _ { j } ( A ^ { l } ) { \geq } { \overset { \cdot } { c _ { j } } } ( A ^ { k } )$ when j is a negative criterion, with at least one strict inequality. For a choice problem, if $A \notin P O ( A )$ , then A<sup>l</sup> can be safely screened out.

Proof. Suppose that $A ^ { l } \in { \bf A }$ and $A ^ { l } \in P O ( \mathbf { A } )$ and ∃ $A ^ { k } \in \mathbf { A }$ such that $\forall j \in \mathbf { Q } ,$ , and $c _ { j } ( A ^ { l } ) \leq c _ { j } ( A ^ { k } )$ , when j is a positive criterion; and $c _ { j } ( A ^ { l } ) { \geq } c _ { j } ( A ^ { k } )$ when j is negative criterion, with at least one strict inequality. □

By the basic preference properties, $\nu _ { j } ( A ^ { l } ) \le \nu _ { j } ( A ^ { k } )$ whenever j is a positive or negative criterion. So $\forall j \in \mathbf { Q }$ $\exists A ^ { k } \in \mathbf { A }$ such that $\nu _ { j } ( A ^ { l } ) \le \nu _ { j } ( A ^ { k } )$ with at least one strict inequality. Therefore, according to Definition $4 , A ^ { k } { \succ } A ^ { l }$ and by Definition $5 , A ^ { l } \notin { \cal P } { \cal O } ( A )$ . This contradicts the assumption. So $A ^ { l } \notin { \cal P } { \cal O } ( A )$ . As stated, the choice problem is to select the best alternative from A.

Although it is still unknown whether $A ^ { k }$ is the best alternative, $A ^ { l }$ can be safely screened out from further consideration since $A ^ { k }$ is better than $A ^ { l } .$

For the converse, suppose that $A ^ { l } \notin { \cal P } { \cal O } ( { \bf A } )$ . From Definition 5, there exists ${ \bar { A } } ^ { k } \in \mathbf { A }$ such that $\mathcal { A } ^ { k } \succ A ^ { l }$ and according to Definition $4 , \nu _ { j } ( { \cal A } ^ { k } ) \ge \nu _ { j } ( { \cal A } ^ { l } )$ with at least one strict inequality. Then, based upon the property of preference monotonicity in Definition $1 , \nu _ { j } ( { \cal A } ^ { k } ) \ge \nu _ { j } ( { \cal A } ^ { l } )$ implies $\exists A ^ { k } \in \mathbf { A }$ such that $\forall j \in \mathbf { Q } , c _ { j } ( A ^ { l } ) \overset { \cdot } { \leq } c _ { j } ( A ^ { k } )$ when $j$ is a positive criterion and $c _ { j } ( A ^ { l } ) { \geq } c _ { j } ( A ^ { k } )$ when $j$ is a negative criterion, with at least one strict inequality, thereby completing the proof. □

Theorem 2 clarifies both the relation between values and consequence data for the determination of Pareto optimality and the relation between Pareto optimality and screening for choice problems. We can safely use consequence data to screen out alternatives that are not Pareto optimal, as long as we are sure the basic preference properties are satisfied.

Although many researchers had assumed the idea of Theorem 2 (checking Pareto optimality by consequence data), it is important to clarify the relation between Pareto optimality in consequence data and values; otherwise improper screening of alternatives may result.

## 3.5.2. PO based screening procedure

• Identify preference direction (positive or negative) for each criterion;

• Compare alternatives based on their consequence data;

• Determine dominated alternatives based on Theorem 2;

• Remove dominated alternatives and retain nondominated alternatives.

## 3.6. Tradeoff weights (TW) based screening techniques

PO based screening removes some alternatives. But DMs may not be satisfied if many alternatives remain. Moreover, the power of PO based screening usually decreases as the number of criteria increases. Further information is needed in order that more efficient screening can be carried out.

TW based screening techniques are related to the research areas such as sensitivity analysis [21] and dominance and potential optimality [11,1]. Although these methods focused on different questions, they all screen alternatives in choice problems since they classify alternatives as either dominated (and therefore screened out) or non-dominated. Here, we summarize these methods and put forward a systematic screening method, tradeoff weights (TW) based screening, that underlies the existence of tradeoff weights.

## 3.6.1. Basic concepts and information requirements

With TW based screening, the following further information from the DM is needed:

(1) The value vector $\mathbf { v } ( \boldsymbol { A } ^ { i } ) \in \mathbb { R } ^ { q } , \forall \boldsymbol { A } ^ { i } \in \mathbf { A }$

(2) The final aggregation model.

Since most of these methods use a linear additive value function, or the simple additive weighting (SAW) method, as the aggregation model, we also adopt it. The SAW method, as introduced in Eq. (3), is repeated below as:

$$
V \left(A ^ {i}\right) = \langle v (A ^ {i}), \mathbf {w} \rangle = \sum_ {j \in Q} w _ {j} \cdot v _ {j} \left(A ^ {i}\right)\tag{6}
$$

where $V ( A ^ { i } )$ is the evaluation of alternative $A ^ { i }$ and w is the weight vector.

## 3.6.2. Potential optimality (PotOp) and screening

Based on the linear additive value model, we define potential optimality and consider the relationship between potential optimality and screening.

Definition 6. An alternative $A ^ { i } \in \mathbf { A }$ is potentially optimal $\bf ( P o t O p )$ iff there exists w such that $\langle \nu ( A ^ { i } ) , { \bf w } \rangle =$ max ${ \mathbf { } } _ { A ^ { k } \in \mathbf { A } } \left. \mathbf { v } \left( A ^ { k } \right) , \mathbf { w } \right.$ . The set of all PotOp alternatives is denoted as $\operatorname { S c r } _ { P o t O P } ( \mathbf { A } ) { = } \mathbf { P o t O p } ( \mathbf { A } )$

Theorem 3. Suppose $\scriptstyle A ^ { i } \in \mathbf { P o t O p } ( \mathbf { A } )$ and $\mathbf { w } \in \mathbf { W }$ . If $\langle \mathbf { v } ( \boldsymbol { A } ^ { i } ) , \mathbf { w } \rangle \geq \langle \mathbf { v } ( \boldsymbol { A } ^ { \bar { k } } ) , \mathbf { w } \rangle \forall \boldsymbol { A } ^ { k } \in \mathrm { \bf { P o t } } \mathbf { \bf { O p } } ( \mathrm { \bf { A } } ) ,$ , then $\langle \mathbf { v } ( A ^ { i } ) , \mathbf { w } \rangle \geq$ $\langle \mathbf { v } ( A ^ { k } ) , \mathbf { w } \rangle \forall k = 1 , 2 . . . n .$

Proof. If the theorem fails, then there exists j such that $\langle \mathbf { v } ( A ^ { j } ) , \mathbf { w } \rangle { > } \langle \mathbf { v } ( A ^ { i } ) , \mathbf { w } \rangle$ . Therefore, there exists $A ^ { h } { \in } \mathbf { P o t O p } ( \mathbf { A } )$ such that $\langle \mathbf { v } ( A ^ { h } ) , \mathbf { w } \rangle \geq \langle \mathbf { v } ( A ^ { k } )$ , w〉 for all $A ^ { k } \in \mathbf { A }$ . In particular, $\langle \mathbf { v } ( \boldsymbol { A } ^ { h } ) , \mathbf { w } \rangle \ge \langle \mathbf { v } ( \boldsymbol { A } ^ { j } ) , \mathbf { w } \rangle > \langle \mathbf { v } ( \boldsymbol { A } ^ { i } ) , \mathbf { w } \rangle$ , contradicting the hypothesis that $\langle \mathbf { v } ( A ^ { i } ) , \mathbf { w } \rangle \geq \langle \mathbf { v } ( A ^ { k } ) , \mathbf { w } \rangle$ for all $A ^ { k } \in \mathbf { P o t O p } ( \mathbf { A } )$ . It follows that if $A ^ { i }$ is best with respect to w in PotOp(A), then $A ^ { i }$ is best with respect to w in A. □

From this theorem, it follows that PotOp screening is safe. The following mathematical program can be used to determine whether alternative $A ^ { i }$ is potentially optimal [10].

$$
\begin{array}{l} \mathbf {P} (A ^ {i}) \text {Minimize:} \delta \\ \text {Subject to:} \langle \mathbf {w}, \big (\mathbf {v} (A ^ {i}) - \mathbf {v} \big (A ^ {k} \big) \big) \rangle + \delta \geq 0, \forall A ^ {k} \in \mathbf {A} \\ w \in W \\ \delta \geq 0 \end{array}
$$

If $\delta ^ { * } = 0 ,$ , then $A ^ { i } \in \mathbf { P o t O p } ( \mathbf { A } )$ . If $\delta ^ { * } > 0 .$ , then $A ^ { i }$ is not potentially optimal. Unless computational considerations intervene, $\operatorname { S c r } _ { \operatorname { P o t O p } }$ can be implemented using this program as the fundamental step.

3.6.3. TW based screening procedure

• Check the validity of the SAW method assumption;

• Set a transformation function, Eq. (1), and get values from the consequence data;

• For each $A ^ { i } \in \mathbf { A }$ , apply $\mathbf { P } ( A ^ { i } )$ to identify PotOp(A);

• Retain only the potential optimal alternatives.

## 3.7. Non-tradeoff weights (NTW) based screening techniques

Since non-tradeoff weights based techniques belong to the family of outranking methods, they can also be called outranking-based screening. Ref. [22] is considered to have originated these methods.

Definition 7. An outranking relation is a binary relation S defined on A, with the interpretation that ASB if, given what is known about the DM's preferences and values, the alternatives and the nature of the problem, there are enough arguments to decide that A is at least as good as B, while there is no essential reason to refute that statement [[26], p. 58].

Many screening methods are based on an outranking relation. Outranking methods are suitable for screening in MCDA, as Ref. [[26], p.57] notes: “Considering a choice problem, for example: if it is known that some action (alternative) a is better than b and c, it becomes irrelevant to analyze preferences between b and c. Those two actions can perfectly remain incomparable without endangering the decision-aid procedure.”

The major families of outranking methods are the ELECTRE methods and the PROME-THEE methods. ELECTRE I and PROMETHEE I are the best known and most widely used methods within their respective families.

## 3.7.1. ELECTRE technique for screening

ELECTRE seeks to reduce the set of nondominated alternatives. The DM is asked to provide a set of weights reflecting relative importance (but they are not for tradeoffs purposes). Alternatives are eliminated if they are dominated by other alternatives to a specified degree defined by the DM. The system uses a concordance index to measure the relative advantage of an alternative over all other alternatives and a discordance index to measure its relative disadvantage. These indices determine a dominated set, which is then screened out.

## 3.7.2. PROMETHEE technique for screening

PROMETHEE is an offshoot of ELECTRE. PRO-METHEE methods begin with a valued outranking function, the outranking degree $\pi ( \boldsymbol { A } ^ { l } , \boldsymbol { A } ^ { k } )$ , defined for each ordered pair of alternatives $( A ^ { l } , A ^ { k } \in { \bf A } \times { \bf A } , A ^ { l } \neq A ^ { k } )$ Hence $\pi ( \boldsymbol { A } ^ { l } , \dot { \boldsymbol { A } } ^ { \dot { k } } )$ represents a measure of how much better $A ^ { l }$ is than $A ^ { k } ; 0 \le \pi ( A ^ { l } , A ^ { k } ) \le 1$ . For the details about the form of $\pi ( \boldsymbol { A } ^ { l } , \boldsymbol { A } ^ { k } )$ , see Ref. [26].

The overall outranking degree for alternative $A ^ { l }$ is defined by the values of two functions: $\Phi ^ { + } ( A ^ { l } )$ (outgoing flow, which refers to the intensity of preference for $A ^ { \bar { l } }$ over other alternatives) and $\Phi ^ { - } ( \mathring { A } ^ { l } )$ (incoming flow, the intensity of preference for other alternatives relative to $A ^ { l } )$ . The definitions of $\mathbf { \Phi } ^ { \cdot } \Phi ^ { + } ( A ^ { l } )$ and $\Phi ^ { - } ( A ^ { l } )$ are as follows:

$$
\Phi^ {+} \left(A ^ {l}\right) = \sum_ {A ^ {k} \in \mathbf {A}} \pi \left(A ^ {l}, A ^ {k}\right),\tag{7}
$$

$$
\Phi^ {-} \left(A ^ {l}\right) = \sum_ {A ^ {k} \in \mathbf {A}} \pi \left(A ^ {k}, A ^ {l}\right)\tag{8}
$$

The final step is the generation of the outranking relations over all alternatives.

Definition 8. $A \mathbf { P } ^ { + } A ^ { k }$ iff $\Phi ^ { + } ( A ^ { l } ) { > } \Phi ^ { + } ( A ^ { k } ) ; \ A ^ { l } { \bf P } { - } A ^ { k }$ iff $\Phi ^ { - } ( A ^ { l } ) { < } \Phi ^ { - } ( A ^ { k } )$

$A ^ { l } \mathbf { I } ^ { + } A ^ { k }$ iff $\scriptstyle \Phi ^ { + } ( A ^ { l } ) = \Phi ^ { + } ( A ^ { k } ) ; \ A ^ { l } \Gamma A ^ { k }$ iff $\Phi ^ { - } ( A ^ { l } ) =$ Φ $\mathbf { \bar { \rho } } ( \mathbf { \mathcal { A } } ^ { k } )$

$A ^ { l }$ outranks $A ^ { k } { \mathrm { ~ i f ~ } } \langle A \mathbf { P } ^ { + } A ^ { k }$ and $A ^ { l } \mathbf { P } ^ { - } A ^ { k } )$ or $\langle A ^ { l } \mathbf { P } ^ { + } A ^ { k }$ and $A ^ { l } \mathbf { I } ^ { - } A ^ { k } )$ or $\langle A ^ { l } \mathbf { I } ^ { + } A ^ { k }$ and $A ^ { l } \mathbf { P } ^ { - } A ^ { k } )$

All alternatives that are outranked by any alternative are then screened out.

## 3.8. Aspiration levels (AL) based screening techniques

Aspiration-level based screening techniques are techniques employing desired or acceptable consequence levels of criteria to identify better alternatives. Techniques such as Goal Programming [4], Compromise Programming [30] and the Reference Point Approach [29] can be regarded as the inspirations of aspiration-based screening. To introduce these methods, we classify them into two categories, simple linguistic methods and distance-based models.

## 3.8.1. Simple linguistic screening

Simple linguistic screening techniques use linguistic expressions on criteria as constraints (standards), eliminating alternatives that do not satisfy these constraints. The advantage of this method is that expressions are simple and there are fewer model parameters to specify. We can further classify constraints into lexicographic and conjunctive/disjunctive [13,16].

• Lexicographic constraints: Criteria are ranked in order of the relative importance. For each criterion, a constraint (goal) is set as a standard. Then all alternatives are examined, one at a time, to assess whether the first criterion is satisfied. All alternatives that fail are screened out. Then proceed to the second criterion, etc.

• Disjunctive/conjunctive constraints: Disjunctive/conjunctive constraints express conditions involving more than one criterion. In conjunctive form, characterized by $\mathrm { \Delta \ a n d ^ { \prime \prime } }$ , all the constraints (goals) must be satisfied in order for an alternative not to be screened. In disjunctive form, characterized by “or”, any alternative can remain as long as it meets at least one of the constraints. Conjunctive constraints are more powerful for screening since an alternative must pass all the standards, so relatively few alternatives will succeed unless the standards are set at a low level. In the disjunctive form, only one standard must be met, so most alternatives will pass unless all standards are set very high.

## 3.8.2. Distance-based screening

Distance-based screening employs a measure of distance between an alternative and some reference point (ideal alternative or aspiration level) as an index to screen out the alternatives that are too far away. Here we adapt the aspiration-level interactive model (AIM) for screening, which was proposed by Ref. [15].

Problem Definition: Three attainment levels for consequences must be established for each criterion $j \colon$

• The “want” level $A S _ { j }$ expresses the aspiration level on each criterion;

• The “ideal” level $( I _ { j } )$ and “nadir” levels $( N _ { j } )$ express the largest and smallest consequence data for each criterion.

Solution Process:

• Order the consequence data, $\{ c _ { j } ( A ^ { i } ) \colon A ^ { i } \in \mathbf { A } \}$ , from least to most preferred for each criterion $j .$ Then inform the DM of the current aspiration level $A S _ { j }$ for each criterion, and the proportion of alternatives that achieve it;

• For every alternative, identify the “nearest nondominated alternative”, defined to be the closest alternative according to a scalarizing function proposed by Ref. [29] (see Ref. [15] for more details) with the weight on criterion j given by $w _ { j } { = } ( A S _ { j } { - } N _ { j } ) / ( I _ { j } { - } N _ { j } )$ The weights are set to reflect the increasing importance attached to criterion j as the aspiration level is moved closer to the ideal. Notice that these weights serve only for temporary rankings and not any other purpose.

Screening process: To screen alternatives, two options are available to the DM.

• First, the DM can reset one or several aspiration levels. This is useful when the DM is not sure about his aspiration level. Updated nearest nondominated alternatives (perhaps the same, perhaps not) are obtained based on these aspiration levels. Then only these nearest alternatives remain for further consideration; all others are screened out.

• Second, if the DM prefers not to express aspiration levels, he or she can request a set of “neighboring” alternatives based on single aspiration levels. All alternatives other than these “neighboring” ones are then screened out. Ref. [15] proposed the use of ELECTRE-based outranking to find the neighbors of the nearest alternative.

## 3.9. Data Envelopment Analysis (DEA) based screening

Data Envelopment Analysis (DEA) is a technique used to measure the relative efficiency of a number of similar units performing essentially the same task. DEA was first put forward by Ref. [5]. Within the past few decades, research into the relation between DEA and MCDA has carried out by authors including Refs. [3,25,7,8]. A comparison of DEA and MCDA is conducted in Ref. [25]: DEA arises from situations where the goal is to determine the productive efficiency of a system or decision making unit (DMU) by comparing how well the unit converts inputs into outputs, while MCDA models have arisen from the need to analyze a set of alternatives according to conflicting criteria. A methodological connection between MCDA and DEA is that if all criteria in an MCDA problem can be classified as either positive criteria (benefits or output) or negative criteria (costs or inputs), then DEA is relevant to MCDA using additive linear value functions.

The basic function of DEA is to ascertain which units are efficient and which are not; in MCDA, these can be regarded as non-dominated and dominated alternatives, respectively. Refs. [7,8] applied some DEA-based models to deal with MCDA problems with both cardinal and ordinal criteria. All dominated alternatives identified by the DEA-based model can be screened out.

## 3.9.1. DEA software: frontier analyst

Frontier Analyst is commercial software based on DEA theory to measure and improve the performance of organizations [9]. Below, Frontier Analyst is employing for executing DEA computations in an illustrative example.

## 3.9.2. DEA based screening procedure

• Identify preference direction (positive or negative) for each criterion;

• Apply a DEA model to identify dominated alternatives;

• Remove dominated alternatives.

## 3.10. The implementation of sequential screening

The information requirements for each screening method, and an estimate of its efficiency, are summarized in Table 1. As stated before, I1 stands for the validation of basic preference properties, I2 is the application of preference information on consequences, I3 is the application of information on criteria and I4 is the integration of aggregation models.

Some typical sequential screening processes are Scr $\mathrm { ( S c r _ { \mathbf { P O } } ( A ) ) , ~ S c r _ { N T W } ( S c r _ { \mathbf { P O } } ( A ) ) , ~ S c r _ { A L } ( S c r _ { \mathbf { P O } } ( A ) ) }$ , and $\mathrm { S c r } _ { \mathbf { D E A } } ( \mathrm { S c r } _ { \mathbf { P O } } ( \mathbf { A } ) )$ . Note that Pareto optimality (PO) based screening is used as a primary screening and combined with another method to carry out a sequential screening.

A more sophisticated approach is $\operatorname { S c r } _ { \mathbf { T W } } ( \operatorname { S c r } _ { \mathbf { D E A } }$ $\left( \operatorname { S c r } _ { \mathbf { P O } } ( \mathbf { A } ) \right)$ . DEA based screening and tradeoff weights (TW) based screening share the same aggregation model assumption (linear additive value function), and TW based screening can be applied after DEA screening. Combined with PO based screening, these screening methods together constitute a powerful sequential screening technique.

## 4. Case study

## 4.1. Waterloo water supply planning problem (WWSP)

The Regional Municipality of Waterloo, located in the southwestern part of Ontario, Canada, comprises the three cities of Kitchener, Waterloo, and Cambridge, plus adjacent rural municipalities. At present, the Waterloo region is one of the largest communities in Canada to rely almost exclusively on groundwater for its water supply. Due to increases in residential, industrial and commercial demand and decreases in the reliability of groundwater resources, the Regional Government developed over 1991–2000 a Long Term Water Strategy to the year 2041 [20,28].

Table 1  
Information requirements for different screening methods

<table><tr><td rowspan="2">Screening methods</td><td colspan="4">Information</td><td rowspan="2">Screening efficiency</td></tr><tr><td>I1</td><td>I2</td><td>I3</td><td>I4</td></tr><tr><td>Pareto optimality</td><td>√</td><td>×</td><td>×</td><td>×</td><td>Low</td></tr><tr><td>Tradeoff weights</td><td>√</td><td>√</td><td>×</td><td>√</td><td>Medium</td></tr><tr><td>Non-tradeoff weights</td><td>√</td><td>×</td><td>√</td><td>√</td><td>Medium</td></tr><tr><td>Aspiration levels</td><td>√</td><td>√</td><td>√</td><td>√</td><td>High</td></tr><tr><td>DEA</td><td>√</td><td>×</td><td>×</td><td>√</td><td>Low</td></tr></table>

Table 2  
The basic structure of the WWSP

<table><tr><td rowspan="2">Criteria</td><td colspan="12">Alternatives</td></tr><tr><td>GW1</td><td>GW2</td><td>AQ1</td><td>AQ2</td><td>GR</td><td>LF1</td><td>LF2</td><td>LF3</td><td>PL1</td><td>PL2</td><td>PL3</td><td>PL4</td></tr><tr><td>INVEST(-)</td><td>100</td><td>61</td><td>8.6</td><td>17</td><td>5</td><td>112</td><td>123.6</td><td>111.25</td><td>120.4</td><td>126</td><td>181</td><td>222</td></tr><tr><td>OPER(-)</td><td>4</td><td>2.4</td><td>5.9</td><td>8.8</td><td>2</td><td>6.2</td><td>6.6</td><td>6.7</td><td>4.2</td><td>3.4</td><td>2.3</td><td>2.5</td></tr><tr><td>INFRA(-)</td><td>30</td><td>30</td><td>40</td><td>50</td><td>30</td><td>60</td><td>60</td><td>60</td><td>60</td><td>65</td><td>60</td><td>60</td></tr><tr><td>ENVIR(-)</td><td>60</td><td>60</td><td>45</td><td>45</td><td>40</td><td>50</td><td>40</td><td>90</td><td>80</td><td>80</td><td>80</td><td>80</td></tr><tr><td>RISK(-)</td><td>80</td><td>80</td><td>50</td><td>50</td><td>80</td><td>60</td><td>70</td><td>70</td><td>30</td><td>30</td><td>30</td><td>30</td></tr><tr><td>SUPPLY(+)</td><td>29</td><td>20</td><td>40</td><td>40</td><td>5</td><td>50</td><td>80</td><td>80</td><td>80</td><td>80</td><td>80</td><td>80</td></tr><tr><td>QUAL(+)</td><td>50</td><td>50</td><td>70</td><td>70</td><td>30</td><td>60</td><td>60</td><td>60</td><td>70</td><td>70</td><td>80</td><td>70</td></tr></table>

The overall purpose of this project was to design and implement the best water resources plan for the Waterloo Region. In light of this purpose, seven criteria were proposed to evaluate possible alternatives: investment cost (INVEST); operation cost (OPER); water quality (QUAL); infrastructure impact (INFRA); environmental impact (ENVIR); risk (RISK); and supply capability (SUPPLY).

Twelve alternatives were identified. Table 2 shows the MCDA problem constitued to represent the WWSP. The consequence data for water quality, environmental impacts and risk were estimated according to a preliminary evaluation by a consulting company. SUPPLY and QUAL are identified as positive criteria (indicated by “+” in Table 2); others are negative preference criteria (indicated by “−” in Table 2). Below is a brief explanation of each of the twelve alternatives.

• Groundwater, option 1 (GW1) — Develop additional groundwater sources in the vicinity of Kitchener– Waterloo.

• Groundwater, option 2 (GW2) — Develop groundwater sources in new fields, mainly in the south Woolwich area, the Roseville area, and the St. Agatha area.

• Aquifer Recharge, option 1 (AQ1) — Construct dual purpose recharge and recovery wells at the Mannheim site, with capacity of 10 MIGD.

![](/api/attachments/KTV9V3V2/fulltext/images/4367a765f83e7ab9df542d23a91d0cbe670d602854396cc02628f22a6bbccf2c.jpg)  
Fig. 6. Frontier analyst based DEA screening.

Table 3  
Values of reduced WWSPP

<table><tr><td rowspan="2">Criteria</td><td colspan="8">Alternatives</td></tr><tr><td>GW2</td><td>AQ1</td><td>GR</td><td>LF1</td><td>LF2</td><td>PL1</td><td>PL2</td><td>PL3</td></tr><tr><td>INVEST(+)</td><td>0.082</td><td>0.581</td><td>1.000</td><td>0.045</td><td>0.040</td><td>0.042</td><td>0.040</td><td>0.028</td></tr><tr><td>OPER(+)</td><td>0.833</td><td>0.339</td><td>1.000</td><td>0.323</td><td>0.303</td><td>0.476</td><td>0.588</td><td>0.870</td></tr><tr><td>INFRA(+)</td><td>1.000</td><td>0.750</td><td>1.000</td><td>0.500</td><td>0.500</td><td>0.500</td><td>0.462</td><td>0.500</td></tr><tr><td>ENVIR(+)</td><td>0.667</td><td>0.889</td><td>1.000</td><td>0.800</td><td>1.000</td><td>0.500</td><td>0.500</td><td>0.500</td></tr><tr><td>RISK(+)</td><td>0.375</td><td>0.600</td><td>0.375</td><td>0.500</td><td>0.429</td><td>1.000</td><td>1.000</td><td>1.000</td></tr><tr><td>SUPPLY(+)</td><td>0.250</td><td>0.500</td><td>0.063</td><td>0.625</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td></tr><tr><td>QUAL(+)</td><td>0.625</td><td>0.875</td><td>0.375</td><td>0.750</td><td>0.750</td><td>0.875</td><td>0.875</td><td>1.000</td></tr></table>

• Aquifer Recharge, option 2 (AQ2) — Construct dual purpose recharge and recovery wells at the Mannheim site, with capacity of 20 MIGD.

• Grand River (GR) — Extract water from Grand River during times of peak demand.

• Grand River Low Flow Augmentation (LF1) — Augment Grand River water flow by implementing the West Montrose Dam project.

• Grand River Low Augment (LF2) — Augment Grand River water flow by constructing a pipeline from Georgian Bay.

• Grand River Low Flow Augmentation (LF3) — Augment Grand River water flow by constructing a pipeline from Lake Huron.

• Pipeline (PL1) — Transport water to the region via a high pressure pipeline from Lake Ontario.

• Pipeline (PL2) — Transport water to the region via a high pressure pipeline from Lake Erie, using the Nanticoke water treatment facility.

• Pipeline (PL3) — Transport water to the region via a high pressure pipeline from Lake Huron at Goderich.

• Pipeline (PL4) — Transport water to the region via high pressure pipeline from Georgian Bay via Thornbury.

## 4.2. Screening procedure

First, each criterion was checked for the satisfaction of basic preference properties. Then sequential screening, $\operatorname { S c r } _ { \mathbf { T W } } ( \operatorname { S c r } _ { \mathbf { D E A } } ( \operatorname { S c r } _ { \mathbf { P O } } ( \mathbf { A } ) ) )$ , was applied. The results are as follows.

1. Pareto optimality based screening: AQ1≻AQ2 and PL3 ≻PL4, so alternatives AQ2 and PL4 can be screened out. Ten alternatives remain.

2. Data envelopment analysis based screening: The software Frontier Analyst was used to analyze DEA efficiency. The result is shown in Fig. 6. GW1 and LF3 are identified as inefficient and can be screened out. Eight alternatives remain.

3. Tradeoff weights based screening: For negative criteria, the transformation function of consequences to values is assumed below.

$$
v _ {j} ^ {i} = \frac {\min _ {A ^ {i} \in \mathbf {A}} \left(c _ {j} ^ {i}\right)}{c _ {j} ^ {i}}\tag{9}
$$

For positive preference criteria, the transformation function is

$$
v _ {j} ^ {i} = \frac {c _ {j} ^ {i}}{\max _ {A ^ {i} \in \mathbf {A}} \left(c _ {j} ^ {i}\right)}\tag{10}
$$

Then the values for the remaining eight alternatives are listed in Table 3.

Based on $\mathbf { P } ( \boldsymbol { A } ^ { i } )$ , the following program can be applied to assess alternative GW2:

$$
\begin{array}{c} - 0. 4 9 9 w _ {1} + 0. 4 9 4 w _ {2} + 0. 2 5 w _ {3} - 0. 2 2 2 w _ {4} - 0. 2 2 5 w _ {5} \\ - 0. 2 5 w _ {6} - 0. 2 5 w _ {7} + \delta \geq 0 \end{array}
$$

$$
\begin{array}{l} - 0. 9 1 8 w _ {1} - 0. 1 6 7 w _ {2} - 0. 3 3 3 w _ {4} + 0. 1 8 8 w _ {6} + 0. 2 5 w _ {7} \\ \quad + \delta \geq 0 \end{array}
$$

$$
\begin{array}{c} 0. 0 3 7 w _ {1} + 0. 5 1 1 w _ {2} + 0. 5 w _ {3} - 0. 1 3 3 w _ {4} - 0. 1 2 5 w _ {5} \\ - 0. 3 7 5 w _ {6} - 0. 1 2 5 w _ {7} + \delta \geq 0 \end{array}
$$

$$
0. 0 4 2 w _ {1} + 0. 5 3 w _ {2} + 0. 5 w _ {3} - 0. 3 3 3 w _ {4} - 0. 0 5 4 w _ {5}
$$

$$
\begin{array}{c} 0. 0 4 w _ {1} + 0. 3 5 7 w _ {2} + 0. 5 w _ {3} + 0. 1 6 7 w _ {4} - 0. 6 2 5 w _ {5} \\ - 0. 7 5 w _ {6} - 0. 2 5 w _ {7} + \delta \geq 0 \end{array}
$$

$$
\begin{array}{c} 0. 0 4 2 w _ {1} + 0. 2 4 5 w _ {2} + 0. 5 3 8 w _ {3} + 0. 1 6 7 w _ {4} - 0. 6 2 5 w _ {5} \\ - 0. 7 5 w _ {6} - 0. 2 5 w _ {7} + \delta \geq 0 \end{array}
$$

$$
\begin{array}{c} 0. 0 5 4 w _ {1} - 0. 0 3 6 w _ {2} + 0. 5 w _ {3} + 0. 1 6 7 w _ {4} - 0. 6 2 5 w _ {5} \\ - 0. 7 5 w _ {6} - 0. 3 7 5 w _ {7} + \delta \geq 0 \end{array}
$$

$$
\sum_ {j = 1} ^ {7} w _ {j} = 1
$$

$$
w _ {j} > 0, j = 1, 2, 3, 4, 5, 6, 7.
$$

Table 4  
Tradeoff weights based screening

<table><tr><td rowspan="2">Screening steps</td><td colspan="8">Alternatives</td></tr><tr><td>GW2</td><td>AQ1</td><td>GR</td><td>LF1</td><td>LF2</td><td>PL1</td><td>PL2</td><td>PL3</td></tr><tr><td> $\delta_{A}^{*}$ </td><td>0</td><td>0</td><td>0</td><td>0.861</td><td>0.103</td><td>0</td><td>0</td><td>0</td></tr><tr><td>PotOp</td><td>√</td><td>√</td><td>√</td><td>×</td><td>×</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Screening out</td><td>×</td><td>×</td><td>×</td><td>√</td><td>√</td><td>×</td><td>×</td><td>×</td></tr></table>

where w denotes the weight of each criteria in Table 2 sequentially (in practical computations using LINGO, w<sub>j</sub> ≥ 0.01 is set).

Using the software LINGO, we get ${ \delta } _ { G W 2 } ^ { * } = 0 .$ , so GW2 ∈ PotOp and cannot be screened out. Other alternatives are checked similarly. The results, shown in Table 4, are that alternatives GW2, AQ1, GR, PL1, PL2, PL3 are retained for further consideration. The number of alternatives is decreased by half as a result of the three screening methods applied sequentially.

Fig. 7 summarizes this application, and shows how each screening method works to screen out alternatives and what preference information is required from the DM.

## 4.3. Practical implementation of WWSPP

To ensure an adequate water supply to the region in the near future, Waterloo Regional council approved three alternatives with different construction schedules, as Waterloo's long term water strategy on May 10, 2000 [28].

• AQ1: The immediate construction of a 5 MIGD Aquifer Storage and Recovery (ASR) facility, with an additional 5 MIGD ASR facility in 2007.

• GW2: 5 MIGD per day of additional groundwater facilities to be implemented between the years 2018 and 2020.

• PL2/PL3: 95 MIGD per day through a pipeline to either Lake Huron or Lake Erie by the year 2035.

## 5. Conclusions

In this paper, the screening process has been studied systematically within the context of MCDA problems. MCDA is interpreted as a consequence-based preference aggregation problem. Consequence data and preference expressions (values and weights) are defined and aggregation steps are discussed. Then, screening, a process that reduces a large set of alternatives to a smaller set that most likely contains the best choice, is investigated. General properties of screening and sequential screening are defined, and a framework to carry out sequential screening is designed. An illustrative application of screening techniques in water supply planning is presented.

The screening procedures examined in this paper focus on the reduction of alternatives based on the information provided by the DM. The remaining alternatives may be similar to each other. However, a good screening procedure ought to present a diversity of alternatives to the DM. As Ref. [[12], p.48] say: Screening “should give the DM a range of options that emphasizes different attributes. Screening should not ‘stack the deck’ in favor of a particular set of values, nor should it yield a set of options that are essentially similar”. We have not addressed this question, and hope that future research can show how to improve screening on the diversity dimension.

![](/api/attachments/KTV9V3V2/fulltext/images/5a6f064a9080e457141d4a8d13f2c1047a7277bbbe9f80cd8fcf720b2f4956e3.jpg)  
Fig. 7. Screening methods and information available.

## Acknowledgements

The authors are grateful to two anonymous reviewers and the Editor-in-Chief, Dr. Andrew B. Whinston, for their helpful comments and suggestions to improve the quality of their paper.

## References

[1] A.D. Athanassopoulos, V.V. Podinovski, Dominance and potential optimality in multiple criteria decision analysis with imprecise information, Journal of the Operational Research Society 48 (1997) 142–150.

[2] V. Belton, T.J. Stewart, Multiple Criteria Decision Analysis: An integrated Approach, Kluwer, Dordrecht, 2002.

[3] V. Belton, S.P. Vickers, Demystifying DEA — a visual interactive approach based on multiple criteria analysis, Journal of the Operational Research Society 44 (1993) 883–896.

[4] A. Charnes, W.W. Cooper, R. Ferguson, Optimal estimation of executive compensation by linear programming, Management Science 1 (1955) 138–151.

[5] A. Charnes, W.W. Cooper, E. Rhodes, Measuring efficiency of decision-making units, European Journal of Operational Research 2 (1961) 428–449.

[6] Y. Chen, D.M. Kilgour, K.W. Hipel, A case-based distance model for screening in multiple criteria decision aid, OMEGA 36 (3) (2008) 373–383.

[7] W.D. Cook, M.A. Kress, Multiple criteria decision model with ordinal preference data, European Journal of Operational Research 54 (1981) 191–198.

[8] W.D. Cook, M.A. Kress, L.M. Seiford, Data envelopment analysis in the presence of both quantitative and qualitative factors, Journal of the Operational Research Society 47 (1996) 945–953.

[9] Frontier Analyst. Banxia Software Ltd. http://www.banxia.com, cited on October 24, 2006.

[10] A. Geoffrion, Proper efficiency and theory of vector maximization, Journal of Mathematical Analysis and Applications 22 (1968) 618–630.

[11] G.B. Hazen, Partial information, Dominance, and Potential Optimality in Multi-Attribute Utility Theory, Operations Research 34 (1986) 296–310.

[12] B.F. Hobbs, P. Meier, Energy Decisions and the Environment: A Guide to the Use of Multicriteria Methods, Kluwer, Massachusetts, 2000.

[13] C.L. Hwang, K. Yoon, Multiple Attribute Decision Making: Methods and Applications, Springer-Verlag, Berlin, 1981.

[14] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Wiley, New York, 1976.

[15] V. Lotfi, T.J. Stewart, S. Zionts, An aspiration-level interactive model for multiple criteria decision making, Computers and Operations Research 19 (1992) 671–681.

[16] K.R. MacCrimmon, An overview Of multiple objective decision making, in: J.L. Cochrance, M. Zeleny (Eds.), Multiple Criteria Decision Making, University of South Carolina Press, Columbia, 1973, pp. 18–44.

[17] E. Natividade-Jesus, J. Coutinho-Rodrigues, C.H. Antunes, A multicriteria decision support system for housing evaluation, Decision Support Systems 43 (2007) 779–790.

[18] V. Pareto, Mannual of Political Economy, A.M. Kelley Publishers, New York, 1971 (English translation).

[19] D. Petkov, O. Petkova, T. Andrew, T. Nepal, Mixing multiple criteria decision making with soft systems thinking techniques for decision support in complex situations, Decision Support Systems 43 (2007) 1615–1629.

[20] S. Rajabi, K.W. Hipel, D.M. Kilgour, Water supply planning under interdependence of actions: theory and application, Water Resources Research 35 (1999) 2225–2235.

[21] D. Rios Insua, Sensitivity Analysis in Multiple Objective Decision Making, Springer-Verlag, Berlin, 1990.

[22] B. Roy, Critères multiples et modélisation des préférences: l'apport des relations de surclassement, Revue d'Economie Politique 84 (1974) 1–44.

[23] B. Roy, Multicriteria Methodology for Decision Aiding, Kluwer, Dordrecht, 1996.

[24] T.L. Saaty, Analytic Hierarchy Process, McGraw Hill, New York, 1980

[25] T. Stewart, Relationships between data envelopment analysis and multicriteria decision analysis, Journal of the Operational Research Society 47 (1996) 654–665.

[26] Ph. Vincke, Multicriteria Decision-Aid, Wiley, New York, 1992.

[27] D.L. Xu, G. McCarthy, J.B. Yang, Intelligent decision system and its application in business innovative capability assessment, Decision Support Systems 42 (2006) 664–673.

[28] Waterloo Regional Council, Waterloo's long term water strategy, Waterloo Regional Council Report, E-00-027.1, Waterloo, Ontario, Canada, 2000.

[29] A. Wierzbicki, A mathematical basis for satisfying decision making, Mathematical Modelling 3 (1982) 391–405.

[30] M. Zeleny, Compromise programming, in: J. Cochrane, M. Zeleny (Eds.), Multiple Criteria Decision Making, University of South Carolina Press, Columbia, 1973, pp. 262–301.

![](/api/attachments/KTV9V3V2/fulltext/images/946f91b47375b0c5603763c7e93dbe700b9e8b4c9a64b993ea3d9a352ba74fab.jpg)

Ye Chen received his Bachelor of Engineering degree from Yanshan University, Qin Huangdao, China in 1997, Master's of Engineering degree from Tianjin University, Tianjin, China in 2001, and PhD degree in the Department of Systems Design Engineering at the University of Waterloo, Waterloo, Canada in 2006. His research interests include development of classification techniques within the field of multiple criteria decision analysis and its applications to water

resources, inventory management, environmental engineering, and elsewhere. He has written papers which have been published in journals which include OMEGA, INFOR, Computers and Operations Research, IEEE Transactions on Systems, Man and Cybernetics, Springer Transactions on Rough Sets, and Journal of Systems Science and Systems Engineering. Currently, Dr. Chen is a PostDoctoral Fellow within the Conflict Analysis Group in the Department of Systems Design Engineering and is the manager of a large research project on brownfield redevelopment.

![](/api/attachments/KTV9V3V2/fulltext/images/2d65c66859fba93e38df6940c409a9f827ec2d8760329188da4df39d091b3499.jpg)

D. Marc Kilgour is Professor of Mathematics at Wilfrid Laurier University in Waterloo, Ontario, Canada, Associate Director of the Laurier Centre for Military Strategic and Disarmament Studies, and Adjunct Professor of Systems Design Engineering at the University of Waterloo. With degrees in Engineering Physics, Applied Mathematics, and Mathematics from University of Toronto, he has held academic and administrative positions

at Wilfrid Laurier University since 1973, with leaves at the University of Waterloo, Graduate Institute for International Studies (Geneva, Switzerland), and Kyoto University (Japan) and Université de Caen (France). International awards have supported other research and teaching visits to USA, France, Germany, and Japan. Dr. Kilgour's primary research interests lie in decision analysis, at the intersection of mathematics, engineering, and social science. His applications of game theory and related formal techniques include problems in international security and arms control, environmental management, negotiation and arbitration, voting, fair division, and coalition formation, and he has pioneered the development of systems for decision support in strategic conflict. His four books and more than 140 refereed articles cross many academic disciplines, including mathematics, operations research, management science, political science, international security, systems engineering, environmental management, economics, social choice, biology, and philosophy. Dr. Kilgour is Corresponding Editor of Theory and Decision and Area Co-Editor of Group Decision and Negotiation, and is active in twelve professional societies.

![](/api/attachments/KTV9V3V2/fulltext/images/5ef33f1370cd3c4e0b7a6dceba571154d1274dd26d8ebb1036a69a5a64cd78b7.jpg)

Keith W. Hipel is University Professor of Systems Design Engineering at the University of Waterloo, Waterloo, Ontario, Canada, and is Vice President of the Academy of Sciences, which part of the Royal Society of Canada. Dr. Hipel thoroughly enjoys teaching and is a recipient of the Distinguished Teacher Award. His major research interests are the development and application of conflict resolution, multiple objective decision making and time

series analysis techniques from a systems design engineering perspective. The main application areas of these decision technologies are water resources management, hydrology, environmental engineering and sustainable development. Dr. Hipel is the author or co-author of four books, nine edited books, close to 200 journal papers, as well as many conference and encyclopedia articles. He is Fellow of the Royal Society of Canada (FRSC), Canadian Academy of Engineering (FCAE), Institute of Electrical and Electronics Engineers (FIEEE), International Council of Systems Engineering (FINCOSE), Engineering Institute of Canada (FEIC), and the American Water Resources Association (FAWRA). Dr. Hipel is also a recipient of the Norbert Wiener Award from the IEEE Systems, Man and Cybernetics (SMC) Society, Outstanding Contribution Award from the IEEE SMC Society, W.R. Boggess Award from AWRA, as well as the Award for Excellence in Research and Excellence in Graduate Supervision from the University of Waterloo. He has held a Canada Council Killam Research Fellowship, Monbusho Kyoto University Visiting Professor Position, Stanley Vineberg Memorial Visiting Professorship, Centre National de la Recherche Scientifique (CNRS) Research Fellowship, and Japan Society for Promotion of Science (JSPS) Fellowship. Moreover, he is a Professional Engineer (PEng) and has carried out consulting activities with engineering firms, government agencies, and utilities in many countries. Finally, he is an Associate Editor of many international journals including the IEEE Transactions on Systems, Man and Cybernetics, Group Decision and Negotiation, and Systems Engineering.
