---
otero_id: 8884
otero_key: "Q4XC97ER"
title: "Mining actionable behavioral rules"
authors: "Peng Su; Wenji Mao; Daniel Zeng; Huimin Zhao"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mining actionable behavioral rules

Peng Su <sup>a</sup>, Wenji Mao <sup>b,</sup>⁎, Daniel Zeng <sup>b,c</sup>, Huimin Zhao d

<sup>a</sup> School of Management Engineering, Shandong Jianzhu University, Shandong 250101, China

<sup>b</sup> State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China

<sup>c</sup> Department of Management Information Systems, University of Arizona, Tucson, AZ 85721, USA

<sup>d</sup> Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee, P. O. Box 742, Milwaukee, WI 53201, USA

## a r t i c l e i n f o

Article history: Received 23 October 2011 Received in revised form 2 March 2012 Accepted 29 April 2012 Available online 10 May 2012

Keywords: Data mining Actionable knowledge discovery Actionable behavioral rule

## a b s t r a c t

Many applications can bene<sup>fi</sup>t from constructing models to predict the behavior of an entity. However, such models do not provide the user with explicit knowledge that can be directly used to in<sup>fl</sup>uence (restrain or encourage) behavior for the user's interest. Undoubtedly, the user often exactly needs such knowledge This type of knowledge is called actionable knowledge. Actionability is a very important criterion measuring the interestingness of mined patterns. In this paper, to mine such knowledge, we take a <sup>fi</sup>rst step toward formally de<sup>fi</sup>ning a new class of data mining problem, named actionable behavioral rule mining. Our de<sup>fi</sup>nition explicitly states the problem as a search problem in a framework of support and expected utility. We also propose two algorithms for mining such rules. Our experiment shows the validity of our approach, as well as the practical value of our de<sup>fi</sup>ned problem.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The behavior of an entity, be it an individual, group, organization, or country, is often greatly in<sup>fl</sup>uenced by various environmental (e.g., social, political, cultural, and economical) factors [24]. Knowledge of such in<sup>fl</sup>uence discovered through data mining has been shown to be extremely valuable for the user (e.g., a corporation or government) in many application domains, from homeland security to public policy, to business intelligence, to name a few.

Past related studies (e.g., [25,22,5,10,11]) have mainly focused on model building and interpretation. In particular, most of these studies aim at constructing predictive models, which provide predictions like “group g will have behavior b if condition c holds.” While such predictions may be very valuable for the user in getting ready for the predicted behavior of the entity in concern, they do not directly and explicitly suggest speci<sup>fi</sup>c actions to take to in<sup>fl</sup>uence (restrain or encourage) the behavior for the user's interest. The user, however, often exactly needs such knowledge.

Consider an example in security informatics. In a hypothetical scenario, assume that recently, Hezbollah has launched frequent violent terrorist attacks, and consequently, the Lebanese government is facing mounting domestic and international pressures. The Lebanese government certainly wants to change this situation by taking some effective actions to restrain terroristic behaviors of Hezbollah. As such, reliable propositions or predictions in the form of rules, such as the following, will be of signi<sup>fi</sup>cant value and interest.

“If the Lebanese government changes the degree of using lethal violence against Hezbollah from level 1 (not using lethal violence) to 2 (using periodic lethal violence) and the degree of being in agreement with Hezbollah from level 1 (negotiation) to 3 (major concession), the degree of terrorist attacks aiming at domestic targets launched by Hezbollah will change from level 3 to 2 with 70% con<sup>fi</sup>dence or 1 with 20% con<sup>fi</sup>dence, or remain unchanged with 10% con<sup>fi</sup>dence, and the degree of terrorist attacks aiming at international targets will change from level 3 to 2 with 30% con<sup>fi</sup>dence or 1 with 20% con<sup>fi</sup>dence, or remain unchanged with 50% con<sup>fi</sup>dence.”

In another hypothetical scenario, assume that in recent months, a corporation has been suffering severe employee loss, which is adversely affecting the operations of the corporation. The management of the corporation wants to change this situation by taking some effective actions to restrain job-hopping behaviors of the staff and is interested in action proposals, such as the following.

“If the corporation raises the overall salary level from 2 to 3 and the paid vacation level from 1 to 2, the level of the job-hopping behavior of the staff will change from 3 to 1 with 60% con<sup>fi</sup>dence or 2 with 30% con<sup>fi</sup>dence or remain unchanged with 10% con<sup>fi</sup>dence.”

As these scenarios illustrate, mining actionable rules to in<sup>fl</sup>uence entity behaviors has wide applicability in various domains. Rules like the examples provide the user explicit suggestions of actions to in<sup>fl</sup>uence the behaviors of the entity in concern for the user's bene<sup>fi</sup>t. This type of knowledge is called actionable knowledge, which is knowledge that one can act upon, something that leads to an act, and something that makes things happen [9]. Actionability is an important aspect of interestingness that has to be quanti<sup>fi</sup>ed based on the subjective evaluation by the user to facilitate decision making [23]. Making mined patterns actionable is one of the central themes in data mining [9]. However, the problem of mining actionable rules for in<sup>fl</sup>uencing entity behaviors has not been identi<sup>fi</sup>ed and studied in the literature yet, although there have been several investigations (e.g., [21,29,13]) into other types of actionable knowledge discovery.

In this paper, we take a <sup>fi</sup>rst step toward establishing a new class of data mining problem, named actionable behavioral rule mining. We propose a formal de<sup>fi</sup>nition for this problem. Our de<sup>fi</sup>nition explicitly states the problem as a search problem in a framework of support and expected utility, and guarantees the completeness and correctness of the discovered actionable rules. We then develop algorithms for solving this new problem. We also conduct an experiment to validate our proposed approach, and evaluate the practical value of our de<sup>fi</sup>ned problem and the comparative performance of the algorithms. The experimental results strongly suggest the validity of our approach.

The rest of the paper is organized as follows. Section 2 proposes the formal de<sup>fi</sup>nition of the actionable behavioral rule mining problem. Section 3 gives our proposed mining algorithms. Section 4 presents our experimental study demonstrating the validity and the utility of our proposed problem de<sup>fi</sup>nition and mining algorithms. Section 5 reviews and discusses the related work. Finally, Section 6 summarizes our contributions and discusses potential future research directions.

## 2. Problem de<sup>fi</sup>nition

We specify the problem of actionable behavioral rule mining through a series of formal de<sup>fi</sup>nitions, starting with the de<sup>fi</sup>nition of a behavioral information system along the line of Pawlak's de<sup>fi</sup>nition of an information system [16].

De<sup>fi</sup>nition 1. A behavioral information system pertinent to a certain entity is de<sup>fi</sup>ned as a 5-tuple $I = ( 0 , 0 ^ { * } , A , D , \rho )$ , where O is a <sup>fi</sup>nite nonempty set of observations, $o ^ { * } \in O$ is the projected next observation, A is a <sup>fi</sup>nite nonempty set of attributes, $D = \cup _ { \mathsf { a } \in A } D _ { a } ,$ , where $D _ { a }$ is the value domain of attribute a and $\rho { : } O \times A {  } D$ is a function associating each observation with a set of attribute values. A is further divided into two subsets, that is, $A = A _ { e n } \cup A _ { b e }$ , where $A _ { b e }$ is a set of behavior attributes describing the behaviors of the entity and $A _ { e n }$ is a set of environment attributes characterizing the environment in which the entity situates and having some causal in<sup>fl</sup>uence upon behavior attributes.

Except for ${ \boldsymbol { o } } ^ { * } ,$ , each observation regarding the environment and behavior attributes comes from a time period of a certain interval. $0 ^ { * }$ is a projection, based on recent observations, of the forthcoming observation should the user takes no action to in<sup>fl</sup>uence the entity's behaviors. For example, assuming that a terrorist group in some country is frequently launching terrorist attacks recently, it is very likely that in a period of time (e.g., a year), the serious situation would remain unchanged or change very slightly if the government does not take any targeted action. The objective of actionable behavioral rule mining is to identify proposals of bene<sup>fi</sup>cial actions that may be taken to improve upon the projected next observation ${ \boldsymbol { o } } ^ { * } .$ . In the just-mentioned example, the government may want to know what actions can be taken to reduce the frequency of such attacks with an overall satisfactory utility.

Without loss of generality, we assume that all attributes (both environment and behavior) are categorical while numerical attributes, if any, have been discretized in advance. Note that a behavior attribute is not restricted to be binary indicating whether a certain behavior occurs. It may also describe how frequent the behavior occurs, the extent of the behavior, and so on. $A _ { b e }$ should be a collectively comprehensive set classifying the behaviors of the entity from a certain angle.

Example. Consider a hypothetical behavioral information system for Hezbollah organization $I = ( O , o ^ { * } , A , D , \rho )$ , where $O = \{ o ^ { * } , o _ { 1 } , o _ { 2 } , . . . , o _ { 1 0 } \}$ $A _ { e n } = \{ e _ { 1 } , e _ { 2 } \} , A _ { b e } = \{ b _ { 1 } , b _ { 2 } \} , D _ { e _ { 1 } } = D _ { e _ { 2 } } = \{ 0 , 1 \} , D _ { b _ { 1 } } = D _ { b _ { 2 } } = \{ 0 , 1 , 2 \}$ , and ρ is presented in Table 1 $( \mathrm { e . g . } , \rho ( o _ { 1 } , e _ { 1 } ) = 1 , \rho ( o _ { 3 } , b _ { 2 } ) = 2 )$ . The values and the corresponding meanings of the attributes can be found in Appendix A. We will continue to use this example in the rest of the paper to illustrate various points.

De<sup>fi</sup>nition 2. Let $I = ( O , o ^ { * } , A , D , \rho )$ be a behavioral information system. An action is de<sup>fi</sup>ned as a triple $\boldsymbol { t } = \left( \boldsymbol { a } , \boldsymbol { v } _ { f } , \boldsymbol { v } _ { t } \right)$ , where $a { \in } A _ { e n } , \nu _ { f } { = } \rho ( o ^ { * } , a )$ and $\boldsymbol { v } _ { t } { \in } D _ { a } .$ . We call t a standard action, if v ≠v . We call t a non-standard action, if $v _ { f } = v _ { t }$ . We say that action $\boldsymbol { t } = \left( \boldsymbol { a } , \boldsymbol { v } _ { f } , \boldsymbol { v } _ { t } \right)$ holds, if the value of a is changed from v to $\nu _ { t } .$ An action set S, also called a |S|-action set, is de<sup>fi</sup>ned as a <sup>fi</sup>nite nonempty set of actions such that $t _ { 1 } . a \neq t _ { 2 } . a$ for any $t _ { 1 } , t _ { 2 } \in S$ . We say that action set S holds, if every t∈S holds. We say that observation o supports S, i $\dot { \cdot } \rho ( o , t . a ) = t . \nu _ { t }$ for every t∈S. The support of S is de<sup>fi</sup>ned as

$s u p ( S ) = | \{ o \in O |$ o  supports S :

We call S a frequent action set, or frequent |S|-action set, with regard to a user-speci<sup>fi</sup>ed threshold referred to as minsup, if sup(S)≥minsup.

Example. $( e _ { 1 } , 1 , 0 )$ is a standard action. $( e _ { 1 } , 1 , 1 )$ is a non-standard action. $( e _ { 1 } , 0 , 1 )$ is not an action. $\{ ( e _ { 1 } , 1 , 0 ) \}$ is a 1-action set and $\{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 0 ) \}$ is a 2-action set. Neither $\{ ( e _ { 1 } , 0 , 1 ) \}$ nor $\{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 1 } , 0 , 1 ) \}$ is an action set. We say that $( e _ { 1 } , 1 , 0 )$ holds, if the value of ORSTPOLSUP is changed from 1 to 0. We say that action set $\{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 1 ) \}$ holds, if both $( e _ { 1 } , 1 , 0 )$ and $( e _ { 2 } , 1 , 1 )$ hold. sup $( \{ ( e _ { 1 } , 1 , 0 ) \} ) = | \{ o _ { 5 } , o _ { 6 } , o _ { 7 } , o _ { 8 } , o _ { 9 } , o _ { 1 0 } \} | = 6 . \quad s u p ( \{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 1 ) \} )$ $= \vert \{ o _ { 5 } , o _ { 6 } , o _ { 7 } \} \vert = 3$ . Given minsup=2, {(e ,1,0)} is a frequent 1-action set and $\{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 1 ) \}$ is a frequent 2-action set. Given minsup=4, $\{ ( e _ { 1 } , 1 , 0 ) \}$ is a frequent 1-action set but $\{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 1 ) \}$ is not a frequent 2-action set.

De<sup>fi</sup>nition 3. $\operatorname { L e t } I = ( O , o ^ { * } , A , D , \rho )$ be a behavioral information system. An effect is de<sup>fi</sup>ned as a triple $e = ( a , \nu _ { f } , \nu _ { t } )$ , where $a { \in } A _ { b e } , \nu _ { f } { = } \rho ( o ^ { * } , a )$ and $\boldsymbol { v } _ { t } { \in } D _ { a }$ . Note that v can be equal to v . We say that effect $e = ( a , v _ { f } ,$ $\nu _ { t } )$ takes place, if the value of a changes from v to v . We say that observation o supports (S,e) where S is an action set and e is an effect, if o supports S and $\rho ( o , e . a ) = e . \nu _ { t }$ . An effect–probability is de<sup>fi</sup>ned as a pair $e p = ( e , p )$ , where e is an effect and $p { \in } [ 0 , 1 ]$ . We say that an effect– probability $e p = ( e , p )$ takes place, if e takes place with probability p.

Example. $( b _ { 1 } , 2 , 0 )$ is an effect. $( b _ { 1 } , 0 , 2 )$ is not an effect. We say that effect $( b _ { 1 } , 2 , 0 )$ takes place, if the value of DEMORGVIOLENCE changes from 2 to 0. We say that effect–probability $( ( b _ { 1 } , 2 , 0 ) , 0 . 5 )$ takes place, if $( b _ { 1 } , 2 , 0 )$ takes place with probability 0.5.

De<sup>fi</sup>nition 4. Let $I = ( O , o ^ { * } , A , D , \rho )$ be a behavioral information system. An actionable behavioral rule is de<sup>fi</sup>ned as a pair $r = ( S , C )$ where C is a <sup>fi</sup>nite nonempty set of effect–probabilities, $\begin{array} { r } { | C | = \sum { { a } \in { A } _ { b e } } | D _ { a } | , } \end{array}$ , and S is an action set. An actionable behavioral rule $r = ( S , C )$ suggests that if S holds, each effect–probability in C will take place.

Function ρ in behavioral information system I.

<table><tr><td rowspan="2"></td><td>ORSTPOLSUP</td><td>ORGCULTGR</td><td>DEMORGVIOLENCE</td><td>TRANSVIOLENCE</td></tr><tr><td> $e_1$ </td><td> $e_2$ </td><td> $b_1$ </td><td> $b_2$ </td></tr><tr><td> $o^*$ </td><td>1</td><td>1</td><td>2</td><td>2</td></tr><tr><td> $o_1$ </td><td>1</td><td>1</td><td>2</td><td>2</td></tr><tr><td> $o_2$ </td><td>1</td><td>0</td><td>2</td><td>1</td></tr><tr><td> $o_3$ </td><td>1</td><td>0</td><td>1</td><td>2</td></tr><tr><td> $o_4$ </td><td>1</td><td>0</td><td>1</td><td>2</td></tr><tr><td> $o_5$ </td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $o_6$ </td><td>0</td><td>1</td><td>2</td><td>1</td></tr><tr><td> $o_7$ </td><td>0</td><td>1</td><td>2</td><td>1</td></tr><tr><td> $o_8$ </td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $o_9$ </td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $o_{10}$ </td><td>0</td><td>0</td><td>1</td><td>0</td></tr></table>

$$
\left(\left\{\left(e _ {1}, 1, 0\right) \right\}, \left\{\left(\left(b _ {1}, 2, 0\right), 1 / 3\right), \left(\left(b _ {1}, 2, 1\right), 1 / 3\right), \left(\left(b _ {1}, 2, 2\right), 1 / 3\right), \right. \right.
$$

$( ( b _ { 2 } , 2 , 0 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 1 ) , 2 / 3 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} )$ is an actionable behavioral rule. It means that if action set $\{ ( e _ { 1 } , 1 , 0 ) \}$ holds, effect–probabilities $( ( b _ { 1 } , 2 , 0 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 0 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 1 ) , 2 / 3 )$ and $( ( b _ { 2 } , 2 , 2 ) , 0 )$ will take place.

Both changing the value of an environment attribute and the corresponding change of the value of a behavior attribute may bring bene<sup>fi</sup>t (positive utility) or incur cost (negative utility) for the user. In other words, an action or effect may have a positive or negative utility, which can be estimated by domain experts. Obviously, if the value of an environment (or behavior) attribute does not change, the utility of the corresponding action (or effect) is zero.

De<sup>fi</sup>nition 5. Let $I = ( O , o ^ { * } , A , D , \rho )$ be a behavioral information system. The expected utility of an actionable behavioral rule $r = ( S , C )$ is de<sup>fi</sup>ned as

$$
u t i l (r) = \sum_ {t \in S} u t i l (t) + \sum_ {e p \in C} u t i l (e p. e) \cdot e p. p,\tag{1}
$$

where util(t) and util(ep.e) denote the utilities of action t and effect ep.e, respectively. We call an actionable behavioral rule r an interesting actionable behavioral rule with regard to a user-speci<sup>fi</sup>ed threshold minutil, if util(r) ≥minutil.

Example. Assume that the utilities of $( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 0 ) , ( b _ { 1 } , 2 , 0 )$ $( b _ { 1 } , 2 , 1 ) , ( b _ { 2 } , 2 , 0 ) ,$ , and $( b _ { 2 } , 2 , 1 ) \mathrm { a r e } - 1 , - 2 , 5 , 2 , 3 , \mathrm { a n d }$ 1, respectively. The expected utility of $( \{ ( e _ { 1 } , 1 , 0 ) \} , \{ ( [ b _ { 1 } , 2 , 0 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 )$ $( ( b _ { 1 } , 2 , 2 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 0 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 1 ) , 2 / 3 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} ) \mathrm { i s } u ( ( e _ { 1 } , 1 , 1 ) , 1 , 2 / 3 ) .$ $0 ) ) + u ( ( b _ { 1 } , 2 , 0 ) ) \times 1 / 3 + u ( ( b _ { 1 } , 2 , 1 ) ) \times 1 / 3 + u ( ( b _ { 2 } , 2 , 0 ) ) \times 1 / 3 + u ( ( b _ { 2 } , 2 , 0 ) ) \times 1 / 3 + u ( ( b _ { 3 } , 2 , 1 ) )$ $1 ) ) \times 2 / 3 = 3 .$

The actionable behavioral rule $( \{ ( e _ { 1 } , 1 , 0 ) \} , \{ ( ( b _ { 1 } , 2 , 0 ) , 2 / 9 ) , ( ( b _ { 1 } , 2 , 1 )$ $1 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 4 / 9 ) , ( ( b _ { 2 } , 2 , 0 ) , 2 / 9 ) , ( ( b _ { 2 } , 2 , 1 ) , 7 / 9 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} ) \quad \mathrm { s u g } .$ gests the following. “If ORSTPOLSUP is changed from level 1 to 0, the DOMORGVIOLENCE of Hezbollah will change from level 2 to 0 with a probability of 2/9, or to 1 with a probability of 1/3, or remain unchanged with a probability of 4/9, and TRANSVIOLTARG of Hezbollah will change from level 2 to 0 with a probability of 2/9, or to 1 with a probability of 7/9, or remain unchanged with a probability of 0.”

Now we have formally de<sup>fi</sup>ned actionable behavioral rules. The problem of mining actionable behavioral rules is to mine all reliable and interesting actionable behavioral rules from a behavioral information system. The threshold minsup is used to assure that the rules are not found by chance. The threshold minutil is used to assure that the rules are suf<sup>fi</sup>ciently bene<sup>fi</sup>ciary to warrant deliberation by the user.

## 3. Mining algorithms

We have developed two algorithms, named MABR-1 and MABR-2 (for Mining Actionable Behavioral Rules). In this section, we describe the algorithms in detail.

## 3.1. The MABR-1 algorithm

Table 2 outlines the algorithm MABR-1, which consists of three phases, candidate actionable behavioral rule generation, rule pruning and interesting actionable behavioral rule generation.

## 3.1.1. Candidate rule generation

In this phase, <sup>fi</sup>rstly, all frequent action sets are generated. Then, actionable behavioral rules with frequent action sets are generated. The generation of frequent action sets is similar to the procedure of generating frequent item sets in the Apriori algorithm for association rule mining [1]. The key idea lies in the ‘downward-closed’ property of the support of an action set. That is, if an action set has a support above minsup, all of its subsets (i.e., general action sets) have supports above minsup. This property is used to effectively reduce the number of potential frequent action sets that need to be checked.

Starting from frequent 1-action sets (by calling function Select in Line 1), the algorithm iteratively <sup>fi</sup>nds frequent 2-action sets, 3-action sets, and so forth, until there is no frequent k-action sets (Lines 3–6). During each iteration, the set of frequent k-action sets is used to generate a set of potential frequent (k+1)-action sets (by calling function Generate in Line 4), which is then checked by computing the supports based on the dataset (by calling function Select in Line 5). With each frequent action set, a candidate actionable behavioral rule is generated (by calling function CR\_Construct in Line 9). The outcome of phase 1 is the set of candidate actionable behavioral rules.

## 3.1.2. Rule pruning

In the previous phase, all action combinations are considered in turn as a rule's condition. Therefore, the candidate rules may share actions in their conditions, and for this reason there could be several rules with same standard actions, and different non-standard actions, consequences and expected utilities. Thus to deal with this problem, the candidate rules generated are pruned in this phase based on the following de<sup>fi</sup>nitions.

De<sup>fi</sup>nition 6. Le $\mathrm { \ t } I = ( O , o ^ { * } , A , D , \rho )$ be a behavioral information system. We say that actionable behavioral rule r is a general rule with regard to another actionable behavioral rule r<sup>'</sup> and r<sup>'</sup> is a specific rule with regard to r, if r.S is a proper subset of $r . S$ and $r . S \vert r . S$ contains non-standard actions only. We call $r { \in } R .$ a most specific rule in the actionable behavioral rule set R if for any specific rule r<sup>'</sup> with regard to $r , r \not \in R$

Example. $( \{ ( e _ { 1 } , 1 , 0 ) \} , \{ ( ( b _ { 1 } , 2 , 0 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 1 / 3 ) ,$ $( ( b _ { 2 } , 2 , 0 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 1 ) , 2 / 3 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} )$ is a general rule with regard to $( \{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 1 ) \} , \{ ( ( b _ { 1 } , 2 , 0 ) , 0 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 1 / 3 ) ,$ $2 / 3 ) , ( ( b _ { 2 } , 2 , 0 ) , 0 ) , ( ( b _ { 2 } , 2 , 1 ) , 1 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} )$

De<sup>fi</sup>nition 7. Let $I = ( O , o ^ { * } , A , D , \rho )$ be a behavioral information system. A binary equivalence relation \~ on an actionable behavioral rule set R is de<sup>fi</sup>ned as follows. For any $c r _ { 1 } , c r _ { 2 } { \in } R , c r _ { 1 } { \sim } { \bf c } r _ { 2 } ,$ , if for any standard action $a { \in } c r _ { 1 } . S , \ a { \in } c r _ { 2 } . S ,$ and for any standard action $b \in c r _ { 2 } . S , \ b \in c r _ { 1 } . S .$ A consolidated rule with regard to a largest equivalence class L of \~ on R is de<sup>fi</sup>ned as an actionable behavioral rule r where $r . S = \{ a \in \cap _ { c r \in }$ $_ { L } c r . S | a$ is a standard action} and for any $e p { \in } r . C , \ e p . p { = } \ \sum _ { - } f q . p ^ { . }$ $s u p ( \dot { c } r . S ) / \sum _ { l \in L } s u p ( l . S )$ , where $f q { \in } c r . C { \mathrm { ~ a n d ~ } } f q . e { = } e p . e .$ cr∈L

Example. $( \{ ( e _ { 1 } , 1 , 0 ) \} , \{ ( ( b _ { 1 } , 2 , 0 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 1 / 3 )$ $( ( b _ { 2 } , \hat { 2 , } 0 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 1 ) , 2 / 3 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} )$ is equivalent to $( \{ e _ { 1 } , 1$ 0), $( e _ { 2 } , 1 , 1 ) \} , \{ ( ( b _ { 1 } , 2 , 0 ) , 0 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 2 / 3 ) , ( ( b _ { 2 } , 2 , 0 ) , 0 )$ $( ( b _ { 2 } , 2 , 1 ) , 1 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} )$ , but is not equivalent to $( \{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 0 ) \}$ $\{ ( ( b _ { 1 } , 2 , 0 ) , 2 / 3 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 0 ) , ( ( b _ { 2 } , 2 , 0 ) , 2 / 3 ) , ( ( b _ { 2 } , 2 , 0 ) , 2 / 3 ) \}$ $1 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} ) . ( \{ ( e _ { 1 } , 1 , 0 ) \} , \{ ( ( b _ { 1 } , 2 , 0 ) , 2 / 9 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 ) \} )$ $( ( b _ { 1 } , 2 , 2 ) , 4 / 9 ) , ( ( b _ { 2 } , 2 , 0 ) , 2 / 9 ) , ( ( b _ { 2 } , 2 , 1 ) , 7 / 9 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) \} )$ is a consolidated actionable behavioral rule pertinent to the only largest equivalence class of \~ on

$$
\left\{ \begin{array}{l} \Big (\{(e _ {1}, 1, 0) \}, \left\{ \begin{array}{c} ((b _ {1}, 2, 0), 1 / 3), ((b _ {1}, 2, 1), 1 / 3), ((b _ {1}, 2, 2), 1 / 3), \\ ((b _ {2}, 2, 0), 1 / 3), ((b _ {2}, 2, 1), 2 / 3), ((b _ {2}, 2, 2), 0) \end{array} \right\} \Big), \\ \Big (\left\{ \begin{array}{c} (e _ {1}, 1, 0), \\ (e _ {2}, 1, 1) \end{array} \right\}, \left\{ \begin{array}{c} ((b _ {1}, 2, 0), 0), ((b _ {1}, 2, 1), 1 / 3), ((b _ {1}, 2, 2), 2 / 3), \\ ((b _ {2}, 2, 0), 0), ((b _ {2}, 2, 1), 1), ((b _ {2}, 2, 2), 0) \end{array} \right\} \Big) \end{array} \right\}.
$$

If a candidate actionable behavioral rule is not a most speci<sup>fi</sup>c rule, delete it (Line 11). If a largest equivalence class of \~ on the set of candidate actionable behavioral rules has more than one element, consolidate all its elements into a consolidated rule (Lines 12–13).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: behavioral information system  $I = (O, o^{*}, A, D, \rho)$ , utilities of all possible actions and effects, minsup, minutil.

Output: interesting actionable behavioral rules with expected utilities

// Phase 1: candidate rule generation

1.  $F_{1} \leftarrow \text{Select}(\{1-\text{action sets}\})$ 

2.  $k \leftarrow 1$ 

3. while  $F_{k} \neq \emptyset$ 

4.  $F_{k+1} \leftarrow \text{Generate}(F_{k})$ 

5.  $F_{k+1} \leftarrow \text{Select}(F_{k+1})$ 

6.  $k \leftarrow k + 1$ 

7.  $F \leftarrow \bigcup_{i=1}^{k-1} F_{i}$ 

8. for each  $S \in F$ 

9.  $cr \leftarrow CR\_Construct(S)$ 

10.  $CR \leftarrow CR \cup \{cr\}$ 

// Phase 2: rule pruning

11.  $CR \leftarrow \text{select all most specific rules from CR}$ 

12. for each largest equivalence class LE of ~ on CR

13.  $r \leftarrow \text{Consolidated rule from LE}$ 

14.  $R \leftarrow R \cup \{r\}$ 

//Phase 3: interesting rule generation

15. for each  $r \in R$ 

16. if util(r) ≥ minutil

17. IR  $\leftarrow IR \cup \{(r, util(r))\}$ 

18. return IR

19. Function Generate(F: set of action sets)

20. for each  $\{S_{1}, S_{2}\} \subset F$  such that  $|S_{1} \backslash S_{2}| = 1$ 

21. if  $S_{1} \cup S_{2}$  is an action set

22.  $C \leftarrow C \cup \{S_{1} \cup S_{2}\}$ 

23. for each  $c \in C$ 

24. flag  $\leftarrow 1$ 

25. for each  $c' \subset c$  such that  $|c \backslash c'| = 1$ 

26. if  $c' \notin F$ 

27. flag  $\leftarrow 0$ 

28. break

29. if flag = 0

30.  $C \leftarrow C \backslash \{c\}$ 

31. return C

32. Function Select(C: set of action sets)

33. for each o ∈ O

34.  $C_{o} \leftarrow \{c \in C | o supports c\}$ 

35. for each  $c \in C_{o}$ 

36. c.sup  $\leftarrow c.\sup + 1$ 

37. for each  $c \in C$ 

38. if c.sup &lt; minsup

39.  $C \leftarrow C \backslash \{c\}$ 

40. return C

41. Function CR_Construct(S: action set)

42. for each a ∈ A_be

43. for each v ∈ D_a

44. e ← (a, ρ(o*, a), v)

45. C ← C ∪

{(e, |{o ∈ O | o supports (S, e)}|/sup(S))}

46. return (S, C)
</div>

## 3.1.3. Interesting rule generation

This phase generates interesting actionable behavioral rules based on the rules after pruning. A rule is included in the <sup>fi</sup>nal output if its expected utility is above minutil (Lines 15–17).

Example. Following previous examples, suppose that minsup and minutil are set to 3 and 2, respectively. The running of MABR-1 can be roughly described as follows. First, the set of frequent 1-action sets $\{ \{ ( e _ { 1 } , \bar { 1 } , 1 ) \} , \{ ( e _ { 1 } , 1 , 0 ) \} , \{ ( e _ { 2 } , 1 , 1 ) \} , \{ ( e _ { 2 } , 1 , 0 ) \} \}$ is generated. Second, the set of the potential frequent 2-action sets $\{ \{ ( e _ { 1 } , 1 , 1 ) , ( e _ { 2 } , 1 , 1 ) \} , \{ ( e _ { 1 }$ $1 , 1 ) , ( e _ { 2 } , 1 , 0 ) \} , \{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 1 ) \} , \{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 0 ) \} \} \mathrm { i }$ is generated. Third, the set of the frequent 2-action sets $\{ \{ ( e _ { 1 } , 1 , 1 ) , ( e _ { 2 } , 1 , 0 ) \}$ , $\{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 1 ) \} , \{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 0 ) \} \}$ is generated. Fourth, the set of the most speci<sup>fi</sup>c frequent action sets $\{ \{ ( e _ { 1 } , 1 , 1 ) , ( e _ { 2 } , 1 , 0 ) \}$ , $\{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 1 ) \} , \{ ( e _ { 1 } , 1 , 0 ) , ( e _ { 2 } , 1 , 0 ) \} \}$ is generated. Fifth, the set of the candidate actionable behavioral rules

$\begin{array} { c c } { / \int { ( e _ { 1 } , 1 , 1 ) , } } & { { \mid \int { ( ( b _ { 1 } , 2 , 0 ) , 0 ) , ( ( b _ { 1 } , 2 , 1 ) , 2 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 1 / 3 ) , \mid } } } \end{array}$ $\begin{array} { r l r } & { } & { \Big ( \left\{ \begin{array} { c } { \breve { \cup } ^ { - 1 } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime \prime } } \\ { ( e _ { 2 } , 1 , 0 ) } \end{array} \right\} , \left\{ \begin{array} { c } { \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime \prime } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime } , \breve { \cup } ^ { \prime \prime } } \\ { ( ( b _ { 2 } , 2 , 0 ) , 0 ) , ( ( b _ { 2 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 2 ) , 2 / 3 ) } \end{array} \right\} \Big ) , } \end{array}$ $\left( \int \left( e _ { 1 } , 1 , 0 \right) , \right) _ { , } \int \left( ( b _ { 1 } ^ { - } , 2 , 0 ) , 0 ) , ( ( b _ { 1 } ^ { - } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 1 } ^ { - } , 2 , 2 ) , 2 / 3 ) , \right) ^ { \zeta }$ $\left\{ \left\{ \begin{array} { l l }  { ( e _ { 2 } , 1 , 1 ) } ^ { \prime } \end{array} \right\} , \left\{ \begin{array} { l l }  { \begin{array} { r l } { { ( ( b _ { 2 } , 2 , 0 ) , 0 ) , ( ( b _ { 2 } , 2 , 1 ) , 1 ) , ( ( b _ { 2 } ^ { \prime } , 2 , 2 ) , 0 ) } ^ { \prime } \end{array} } } \end{array} \right\} \right\}$ $  \int ( e _ { 1 } ^ { - } , 1 , 0 ) ,    \int ( ( b _ { 1 } , \bar { 2 } , 0 ) , 2 / 3 ) , ( ( b _ { 1 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 1 } , 2 , 2 ) , 0 ) ,  $ $  \begin{array} { c } { { ( \dot { e _ { 2 } } , 1 , 0 ) } } \end{array}  ^ { , }  \begin{array} { c } { { ( ( b _ { 2 } , 2 , 0 ) , 2 / 3 ) , ( ( b _ { 2 } , 2 , 1 ) , 1 / 3 ) , ( ( b _ { 2 } , 2 , 2 ) , 0 ) } } \end{array}  )$

is generated. Finally, the set of the interesting actionable behavioral rules with expected utilities

$$
\left\{ \begin{array}{l} \Bigg (\Bigg (\{(e _ {1}, 1, 0) \}, \left\{ \begin{array}{c} ((b _ {1}, 2, 0), 0), ((b _ {1}, 2, 1), 1 / 3), ((b _ {1}, 2, 2), 2 / 3), \\ ((b _ {2}, 2, 0), 0), ((b _ {2}, 2, 1), 1), ((b _ {2}, 2, 2), 0) \end{array} \right\} \Bigg), 3 \Bigg), \\ \Bigg (\Bigg (\Bigg \{ \begin{array}{c} (e _ {1}, 1, 0), \\ (e _ {2}, 1, 0) \end{array} \Bigg \}, \left\{ \begin{array}{c} ((b _ {1}, 2, 0), 2 / 3), ((b _ {1}, 2, 1), 1 / 3), ((b _ {1}, 2, 2), 0), \\ ((b _ {2}, 2, 0), 2 / 3), ((b _ {2}, 2, 1), 1 / 3), ((b _ {2}, 2, 2), 0) \end{array} \right\} \Bigg), \frac {1 0}{3} \Bigg) \end{array} \right\}
$$

is generated and returned as the <sup>fi</sup>nal output.

## 3.2. The MABR-2 algorithm

The most computationally expensive part of MABR-1 is its <sup>fi</sup>rst phase, where frequent action sets with increasing cardinalities need to be iteratively identi<sup>fi</sup>ed. At each iteration, potential frequent action sets are <sup>fi</sup>rst generated by merging frequent action sets found in the previous iteration. A complete scan of the behavioral information system is then carried out to compute the supports of the potential frequent action sets at the current iteration. This process of repeatedly scanning the database is time consuming. In a circumstance involving a behavioral information system with many attributes and/or many attribute values, and a very low support threshold, the number of potential frequent action sets at each iteration can be enormous and MABR-1 may consume considerable time.

Compared to MABR-1, MABR-2, outlined in Table 3, is much more scalable and ef<sup>fi</sup>cient. It avoids potential frequent action sets generation-and-test and uses an FA-tree data structure to signi<sup>fi</sup>cantly reduce the computational cost. Based on the de<sup>fi</sup>nition of FP-tree, which has been shown to allow highly ef<sup>fi</sup>cient and scalable association rule mining [7], we de<sup>fi</sup>ne FA-tree, conditional subtree, and conditional FA-tree as follows.

De<sup>fi</sup>nition 8. Let $I = ( O , o ^ { * } , A , D , \rho )$ be a behavioral information system. An FA-tree (for frequent action set) is a tree structure such that:

1. It consists of a root, a set of 1-action-set-pre<sup>fi</sup>x subtrees as the children of the root, and a header list.

2. Each node in the 1-action-set-pre<sup>fi</sup>x subtree consists of four <sup>fi</sup>elds: 1-action-set, count, next, and parent. The 1-action-set <sup>fi</sup>eld carries a 1-action set. The count <sup>fi</sup>eld registers the number of observations in O supporting the union of the 1-action sets carried by the nodes on the path from the root to this node. The next field links to the next node in the FA-tree sharing the same 1-action-set, forming a linked list. The parent <sup>fi</sup>eld links to the parent node.

3. Each item in the header list consists of two <sup>fi</sup>elds: 1-action-set and first. The 1-action-set <sup>fi</sup>eld carries a 1-action set. The first <sup>fi</sup>eld points to the <sup>fi</sup>rst node in the FA-tree carrying the corresponding 1-action set.

De<sup>fi</sup>nition 9. Let $I = ( 0 , 0 ^ { * } , A , D , \rho )$ be a behavioral information system and T be an FA-tree pertinent to I. The conditional subtree of α in T.header is de<sup>fi</sup>ned as a subtree of T, consisting of the nodes carrying the same 1-action-set as α and the paths from these nodes to the root. The conditional FA-tree of α is de<sup>fi</sup>ned as an FA-tree under the condition of the existence of α and can be constructed based on the conditional subtree of α.

MABR-2 tends to be much more efficient and scalable than MARB-1 for two main reasons. First, MABR-2 only scans the behavioral information system a few times. Second, the size of the FA-tree tends to be much smaller than that of the behavioral information system.

MABR-2 adopts a variant of the FP-growth method [7] and takes only three scans of the behavioral information system in all. The <sup>fi</sup>rst scan collects the set of frequent 1-action sets (Line 1). The second scan constructs the FA-tree (Lines 2–10). The third scan generates the candidate actionable behavioral rules (Lines 12–14). Generating the set of frequent action sets based on the FA-tree (Line 11) and pruning rules (Lines 15–18) do not require scanning of the behavioral information system. The steps for rule pruning and interesting rules generation (Lines 15–21) are identical to those in MABR-1. The recursive procedure Insert (Lines 23–32) inserts the sorted frequent 1-action sets supported by an observation into the FA-tree. The recursive procedure Construct (Lines 33–43) constructs all frequent k-action sets (k>1).

The size (number of nodes) of an FA-tree is bounded by $\sum _ { 0 \in { \cal 0 } } \left. L ( \boldsymbol { o } ) \right. +$ 1 and the height of the tree is bounded by $\mathrm { M A X } _ { o \in O } | L ( o ) | + 1$ , where $L ( o )$ denotes the list of frequent action sets supported by observation o (derived from Lines 6–8). This means that the size of an FA-tree is bounded by the size of the behavioral information system. As the lists of frequent action sets supported by different observations may share the same items, the size of the tree is usually much smaller than the size of the behavioral information system.

Example. Following previous examples, suppose that minsup and minutil are set to 3 and 2, respectively. The running of MABR-2 can be roughly described as follows. First, the frequent 1-action sets $\{ ( e _ { 1 } , 1 , 0 ) \} , \{ ( e _ { 2 } , 1 , 0 ) \} , \{ ( e _ { 1 } , 1 , 1 ) \}$ , and $\{ ( e _ { 2 } , 1 , 1 ) \}$ are generated. Second, the FA-tree T is constructed (Fig. 1(a)). For simplicity, a symbol like $" ( a , \nu _ { f } , \nu _ { t } ) "$ such as $" ( e _ { 1 } , 1 , 0 ) "$ is used to denote an action set $\{ ( a , \nu _ { f } , \nu _ { t } ) \}$ . Third, the conditional subtree and conditional FA-tree of T.header [4] (Fig. 1(b)) are constructed and then frequent action set $\{ ( e _ { 2 } , 1 , 1 ) , ( e _ { 1 } , 1 , 0 ) \}$ is generated. Fourth, the conditional subtree and conditional FA-tree of T.header [3] (Fig. 1(c)) are constructed and then frequent action set $\{ ( e _ { 1 } , 1 , 1 ) , ( e _ { 2 } , 1 , 0 ) \}$ is generated. Fifth, the conditional subtree and conditional FA-tree of T.header [2] (Fig. 1(d)) are constructed and then frequent action set $\{ ( e _ { 2 } , 1 , 0 ) , ( e _ { 1 } , 1 , 0 ) \}$ is generated. Sixth, the set of the most speci<sup>fi</sup>c frequent action sets $\{ \{ ( e _ { 2 } , 1 , 1 ) , ( e _ { 1 } , 1 , 0 ) \} , \{ ( e _ { 1 } , 1 , 1 ) , ( e _ { 2 } , 1 , 0 ) \} , \{ ( e _ { 2 } , 1 , 0 ) , ( e _ { 1 } , 1 , 0 ) \} \}$ is generated. The rest is identical to the last two steps of the previous running example for MABR-1.

## 4. Experimental study

We have fully implemented our proposed approach to actionable behavioral rule mining. In this section, we empirically validate our approach, show an interesting example of the mined rules, and compare the running times of MABR-1 and MABR-2.

## 4.1. Experimental setup

We conduct an experiment with the benchmark MAROB datasets. The MAROB datasets cover several ethnopolitical organizations in the Middle East and North Africa. The datasets keep track of several attributes on a yearly basis from 1980 to 2004. The attributes can be broadly classi<sup>fi</sup>ed into two groups, behavioral and environmental. The former represents the behaviors of an organization in previous years while the latter characterizes the environment in which the organization situates.

We experimented with the data in MAROB and extracted three sub datasets about the Hezbollah organization in Lebanon, the Kurdistan Democratic Party of Iran, and the Iraqi Communist Party, respectively. We chose three behavior attributes, DOMORGVIOLENCE, TRANSVIOLTARG and TRANSVIOLOC, and several environment attributes that are deemed to have causal in<sup>fl</sup>uence upon the behavior attributes. The meanings and values of these attributes are given in Appendix A. Utility values of the possible actions and effects from the viewpoints of the corresponding governments were elicited from human analysts and normalized into the range of [−1, 1] (the utility values we use are omitted here, but available from the authors upon request).

```txt
Input: behavioral information system
I = (O, o*, A, D, ρ), utilities of all possible actions and effects, minsup, minutil.
Output: interesting actionable behavioral rules with expected utilities

// Phase 1: candidate rule generation
1. F ← {frequent 1-action sets}
// FA-tree construction
2. T ← An FA-tree root with no child
3. T.header ← List of (frequent 1-action set, null) pairs sorted in support-descending order
4. for each o ∈ O
5. L←Empty list
6. for each a ∈ Aen
7. if S = {(a, ρ(o*, a), ρ(o, a))} ∈ F
8. L.Add(S)
9. Sort L according to the order of T.header
10. Insert(L, T)
11. Construct(T, null)
12. for each S ∈ F
13. cr ← CR_Construct(S)
14. CR ← CR ∪ {cr}
// Phase 2: rule pruning
15. CR ← select all most specific rules from CR
16. for each largest equivalence class LE of ~ on CR
17. r ← Consolidated rule from LE
18. R ← R ∪ {r}
// Phase 3: interesting rule generation
19. for each r ∈ R
20. if util(r) ≥ minutil

21. IR ← IR ∪ {(r, util(r))}
22. return IR
23. Procedure Insert (L: List of 1-action sets, P: PA-tree node)
24. if P has no child N such that N.1-action-set = L[1]
25. i ← j such that header[j].1-action-set = L[1]
26. N ← FA-tree node (L[1], 1, T.header[i].first, P)
27. T.header[i].first ← N
28. else
29. N.count ← N.count + 1
30. L.Delete(1)
31. if L is not empty
32. Insert(L, N)
33. Procedure Construct(P: FA-tree, A: action set)
34. if P contains a single path
35. for each combination c of l-action-set fields of nodes of P except the root
36. F ← F ∪ {c ∪ A}
37. else
38. for each item I in P.header, from last to first
39. A ← A ∪ l.l-action-set
40. CB ← Conditional subtree of I
41. CT ← Conditional FA-tree of CB
42. if CT ≠ null
43. Construct(CT, A)
```

## 4.2. Baseline approach

An actionable behavioral rule r=(S,C) suggests that if S holds, each effect–probability in C will take place. The key difference among approaches is the effect–probabilities. In other words, for an action set, different approaches may yield different sets of effect–probabilities.

A natural design of the baseline approach is to follow random guessing using the true distributions of the class labels. Intuitively, it estimates the effect–probabilities with the true distributions of the values of behavior attributes. That is, given that an action set holds, it estimates the probability of an effect $\boldsymbol { e } = \left( \boldsymbol { a } , \boldsymbol { v } _ { f } , \boldsymbol { v } _ { t } \right)$ taking place at the proportion of observations with v as its a value.

Formally, the baseline approach constructs the actionable behavioral rule based on a frequent action set as follows. $\operatorname { L e t } I = ( O , o ^ { * } , A , D , \rho )$ be a behavioral information system. For any frequent action set S, actionable behavioral rule r=(S,C) is constructed, where for any a∈A and v∈ $D _ { a }$ there exists an effect–probability $( ( a , \rho ( o ^ { * } , a ) , \nu ) , | \{ o \in O | \rho ( o , a ) = \nu \} | / | O | )$ ∈C. Note that the expected utility of r is computed using Eq. (1).

(a)  
![](/api/attachments/Q4XC97ER/fulltext/images/796e5f78c826cb653b7296a4931cea0a1f1315931030315c6a44d862eee1df95.jpg)  
Fig. 1. Illustration of running MABR-II. (a) FA-tree T, conditional subtrees and conditional FA-trees of: (b) T.header [4], (c) T.header [3], (d) T.header [2], (e) T.header [1]

## 4.3. Evaluation criterion

Let au be the actual utility when an action set S are taken actually. Let eu be the expected utility of the consolidate actionable behavioral rule with S as its antecedent our approach generates or the rule the baseline approach generates with S. Certainly, we want the absolute difference between eu and au to be as small as possible. Thus, we use the mean absolute error (MAE), a standard measure for assessing the closeness between predictions and eventual outcomes, as the criterion for evaluating the performance of our approach and the baseline approach. The MAE is given by

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} | e u _ {i} - a u _ {i} |,
$$

where $e u _ { i }$ is the expected utility our approach or the baseline approach estimates and au is the actual utility. Typically, domain experts in security informatics set the MAE threshold to a reasonable value around 0.07 for <sup>fi</sup>eld evaluation.

In each year, the Lebanese government may take some actions to restrain terroristic behaviors of Hezbollah. The same goes for the other government–organization pairs. These actions and their effects have been recorded in the MAROB dataset. Thus, the actual utility of the actions can be computed according to the observations for this year and the previous year. If for this year, our approach can give the consolidated actionable behavioral rule cr with the same actions as the actual ones taken by the government, then the absolute difference between the actual utility and the expected utility of cr or the rule the baseline approach generates with the actual actions should be considered. Note that the input parameter O includes all the observations for years from 1982 to 2004 except for this year.

## 4.4. Experimental results

Table 4 shows the experimental results on the three sub MAROB datasets with 31 actual action sets that are antecedent of some consolidated actionable behavioral rules. Note that there is no other actual action set that is antecedent of any consolidated rule. The table entries present the actual utilities, the absolute errors of the baseline approach and the MABR algorithms, with minsup set to 5. For the absolute errors, the means and standard deviations are presented.

Note that although the utilities of actionable behavioral rulesinduced actions and effects were assigned by the experts in a subjective fashion, what is actually compared in our experiment is the absolute difference between the actual utility and the expected utility of the action set induced by a rule. For the same action set, different methods will yield different estimated probability distributions over the effects or outcomes. Generally speaking, the closer the estimated distribution of a rule's effects is to the actual realization, the closer the estimated utility is to the actual utility.

Table 4  
Comparison of the results by different approaches.

<table><tr><td rowspan="2">Action set</td><td rowspan="2">Actual utility</td><td colspan="2">Absolute error</td></tr><tr><td>Baseline</td><td>MABRs</td></tr><tr><td>1</td><td>-0.006</td><td>0.091</td><td>0.085</td></tr><tr><td>2</td><td>-0.246</td><td>0.184</td><td>0.123</td></tr><tr><td>3</td><td>0.194</td><td>0.298</td><td>0.119</td></tr><tr><td>4</td><td>0.072</td><td>0.056</td><td>0.064</td></tr><tr><td>5</td><td>-0.008</td><td>0.107</td><td>0.080</td></tr><tr><td>6</td><td>-0.012</td><td>0.103</td><td>0.071</td></tr><tr><td>7</td><td>0.000</td><td>0.115</td><td>0.057</td></tr><tr><td>8</td><td>-0.003</td><td>0.112</td><td>0.093</td></tr><tr><td>9</td><td>-0.004</td><td>0.111</td><td>0.118</td></tr><tr><td>10</td><td>0.064</td><td>0.179</td><td>0.000</td></tr><tr><td>11</td><td>-0.004</td><td>0.111</td><td>0.041</td></tr><tr><td>12</td><td>-0.016</td><td>0.099</td><td>0.000</td></tr><tr><td>13</td><td>-0.006</td><td>0.109</td><td>0.053</td></tr><tr><td>14</td><td>-0.003</td><td>0.112</td><td>0.000</td></tr><tr><td>15</td><td>0.154</td><td>0.269</td><td>0.147</td></tr><tr><td>16</td><td>-0.017</td><td>0.098</td><td>0.041</td></tr><tr><td>17</td><td>-0.016</td><td>0.099</td><td>0.093</td></tr><tr><td>18</td><td>-0.004</td><td>0.111</td><td>0.041</td></tr><tr><td>19</td><td>-0.086</td><td>0.175</td><td>0.012</td></tr><tr><td>20</td><td>-0.011</td><td>0.015</td><td>0.012</td></tr><tr><td>21</td><td>-0.011</td><td>0.015</td><td>0.012</td></tr><tr><td>22</td><td>-0.006</td><td>0.015</td><td>0.015</td></tr><tr><td>23</td><td>0.077</td><td>0.062</td><td>0.024</td></tr><tr><td>24</td><td>-0.084</td><td>0.175</td><td>0.003</td></tr><tr><td>25</td><td>0.077</td><td>0.062</td><td>0.032</td></tr><tr><td>26</td><td>0.071</td><td>0.062</td><td>0.024</td></tr><tr><td>27</td><td>-0.004</td><td>0.098</td><td>0.089</td></tr><tr><td>28</td><td>-0.120</td><td>0.213</td><td>0.089</td></tr><tr><td>29</td><td>-0.011</td><td>0.027</td><td>0.062</td></tr><tr><td>30</td><td>-0.010</td><td>0.027</td><td>0.047</td></tr><tr><td>31</td><td>0.117</td><td>0.142</td><td>0.024</td></tr><tr><td>Mean</td><td></td><td>0.092</td><td>0.054</td></tr><tr><td>SD</td><td></td><td>0.118</td><td>0.069</td></tr></table>

The experimental results show the validity of our approach. From Table 4, we can see that the MAE of our approach is much less than the validity threshold 0.07. Meanwhile, we can see that our approach signi<sup>fi</sup>cantly outperforms the baseline approach, as the MAE value of our approach is almost 50% less than that of the baseline approach.

Here we show an example rule mined using MABRs on Hezbollah, with minsup, minutil, and o<sup>∗</sup> set to 8, 0.05, and the observation of year 2003, respectively. It is

$$
\left(\left(\left\{ \begin{array}{l} (e _ {2}, 1, 0), \\ (e _ {3}, 0, 2) \end{array} \right\}, \left\{ \begin{array}{l} ((b _ {1}, 2, 0), 0. 3), ((b _ {1}, 2, 1), 0), ((b _ {1}, 2, 2), 0. 7), \\ ((b _ {1}, 2, 3), 0), ((b _ {1}, 2, 4), 0), ((b _ {1}, 2, 5), 0), \\ ((b _ {2}, 2, 0), 0. 1), ((b _ {2}, 2, 1), 0), ((b _ {2}, 2, 2), 0. 6), \\ ((b _ {2}, 2, 3), 0. 2), ((b _ {2}, 2, 4), 0. 1), ((b _ {2}, 2, 5), 0), \\ ((b _ {3}, 5, 0), 0. 6), ((b _ {3}, 5, 1), 0), ((b _ {3}, 5, 2), 0), \\ ((b _ {3}, 5, 3), 0), ((b _ {3}, 5, 4), 0), ((b _ {3}, 5, 5), 0. 4) \end{array} \right\}\right), 0. 1 2\right).
$$

The symbols in the rule and corresponding attributes are listed in Appendix A. This rule provides the following proposal of actions to the Lebanon government:

“If DIAFINSUP is changed from level 1 to 0 and ORGCULTGR is changed from level 0 to 2, the DOMORGVIOLENCE of Hezbollah will change from level 2 to 0 with a probability of 0.3, or remain unchanged with a probability of 0.7, TRANSVIOLTARG of Hezbollah will change from level 2 to 0 with a probability of 0.1, or to 3 with a probability of 0.2, or to 4 with a probability of 0.1, or remain unchanged with a probability of 0.6, and TRANSVIOLOC of Hezbollah will change from level 5 to 0 with a probability of

0.6, or remain unchanged with a probability of 0.4. This actionable behavioral rule has an expected utility of 0.12.”

## 4.5. Comparison of MABR algorithm

Fig. 2 contrasts the running times of MABR-1 and MABR-2 on Hezbollah as minsup increases from 8 to 23 (The results on the other two sub datasets are quite similar, and the parameter minutil has little effect on the running time from our experimental <sup>fi</sup>ndings.).

MABR-2 appears to be more ef<sup>fi</sup>cient and scalable than MABR-1. When minsup is low, the advantage of MABR-2 over MABR-1 is especially notable. When minsup is 8, the running time of MABR-2 is only 0.07% of that of MABR-1. As minsup goes up, this advantage becomes less prominent. The reason is that large frequent action sets become unusual for high minsup.

## 5. Related work

While there is no previous work on mining actionable rules specifically for in<sup>fl</sup>uencing entity behaviors, there have been several investigations into other types of actionable knowledge discovery. Actionable knowledge usually takes the form of actionable rules. A rule is considered actionable if users can take an action to their advantage directly based on this rule [14].

For example, to improve the pro<sup>fi</sup>tability of customers of a bank, action rules constructed from certain pairs of classi<sup>fi</sup>cation rules were proposed in Ref. [21]. Attributes are categorized into two types, stable and <sup>fl</sup>exible. The former (latter) includes the attributes whose values cannot (can) be changed or in<sup>fl</sup>uenced by a bank. Rules are extracted from a decision table giving preference to <sup>fl</sup>exible attributes. This class of rules forms a special repository of rules from which new rules called action rules are constructed. An action is taken when a change in a <sup>fl</sup>exible attribute is encountered. An action rule is de<sup>fi</sup>ned as a term $[ ( \omega ) \Lambda ( \alpha \to \beta ) ] \Rightarrow ( \gamma \to \varphi )$ , where ω is a conjunction of values of stable attributes, $( \alpha \to \beta )$ represents proposed changes in values of <sup>fl</sup>exible attributes, and $( \gamma \to \varphi )$ is a desired effect of the action. The discovered knowledge provides an insight into how the values of some attributes need to be changed so that the undesirable objects can be shifted to a desirable group.

A change of attribute value may incur cost. In Ref. [26], the notion of cost and feasibility of an action rule was proposed and a search graph based method for constructing feasible action rules at the lowest cost was given. In Ref. [20], interesting action rules were de<sup>fi</sup>ned as the rules of the lowest cost. In Ref. [19], a heuristic strategy for constructing interesting action rules was proposed. In Ref. [27], a method, which combines the action forest algorithm for extracting action rules and a heuristic strategy, was proposed for generating interesting action rules.

Despite their differences in choosing classi<sup>fi</sup>cation algorithms, the above-mentioned methods on mining action rules all produce an actionable rule based on a certain pair of classi<sup>fi</sup>cation rules or a single classi<sup>fi</sup>cation rule. A main shortcoming of this strategy is that some interesting actionable rules can be missed. To address this problem, another strategy was proposed in a support-con<sup>fi</sup>dence-cost framework for discovering action rules directly from a database [8]. In Ref. [18], an approach was proposed to generate association-type action rules. In Ref. [17], a bottom-up strategy was proposed to discover action rules without using pre-existing classi<sup>fi</sup>cation rules.

![](/api/attachments/Q4XC97ER/fulltext/images/cf7afee02a829ea665539d3068f8150affc325ef74ea1463415c07a5572f1a06.jpg)  
Fig. 2. Running time with minsup.

In Ref. [29], to help devise a direct-marketing plan in order to increase the pro<sup>fi</sup>t of an institution, a lazy approach was proposed to use ‘role models’ for generating advice and plans. The role models are typical cases that form a case base and can be used for customer advice generation. For each new customer seeking advice, a nearestneighbor algorithm is used to <sup>fi</sup>nd a cost-effective and highly probable plan for switching a customer to the most desirable role model. Such a method does not provide rules in advance and will incur high computation costs when generating action suggestions.

To discover actionable knowledge for customer relationship management (CRM), methods were proposed to suggest actions to reclassify a customer from an undesired status to a desired one while post-processing decision trees to maximum expected net pro<sup>fi</sup>t [13,30]. However, these methods could miss some actions with higher net pro<sup>fi</sup>t. To handle this problem, multiple trees with different subsets of “hard” attributes need to be built [13]. To get optimal actions, the number of trees could be very large, especially when there are many “hard” attributes.

In addition, in Ref. [6], a formal view of actionable knowledge discovery (AKD) is presented from the system and decision-making perspectives, and correspondingly four types of generic AKD frameworks proposed, formalized, and illustrated.

Another line of related work is on associative classi<sup>fi</sup>cation (AC), which integrates two data mining tasks, association rule discovery and classi<sup>fi</sup>cation, to build a prediction model (classi<sup>fi</sup>er). AC algorithms normally derive a large set of rules, many of which are redundant or misleading [15,12]. Several pruning methods have been used to reduce the size of associative classi<sup>fi</sup>ers. Most AC algorithms use rule ranking procedures for rule pruning. One important parameter used to determine the precedence of the rules is rule antecedent length. Some AC algorithms, such as those in Refs. [12,28,2], tend to prefer general rules (those with shorter antecedent) and consequently suffer poor classi<sup>fi</sup>cation accuracy. On the contrary, other algorithms, such as those in Refs. [4,3], which tend to prefer speci<sup>fi</sup>c rules, reduce the chance of misclassi<sup>fi</sup>cation. The strategy to re<sup>fi</sup>ne the generated rule set so as to acquire quality rules is also an important issue in mining actionable behavioral rules.

An AC rule can be represented as [α]⇒(γ), where α represents values of feature attributes, and γ is a value of a decision attribute. In contrast with actionable rule mining, AC and other traditional rule-based classi<sup>fi</sup>cation do not consider changes of attribute values. Therefore, in both problem de<sup>fi</sup>nition and formalism, traditional classi<sup>fi</sup>cation methods do not provide actionable suggestions on how attributes need to be changed to cater to the user's interest.

Nonetheless, previous work on mining actionable rules is incapable of mining actionable behavioral rules we identify. The goal of previous approaches is to reclassify some member objects of an entity (e.g. customers of a company) from an undesired decision class to a desired one for the user's interest, while our approach is aimed to change an entity's multiple behavioral attribute (e.g. attacks conducted by a radical group) values from current observations for the user's interest.

In the framework we propose, an actionable behavioral rule takes the form of $[ ( \alpha \to \beta ) ] \Rightarrow [ ( \gamma \to \varphi , p ) ] .$ , where p represents the probabilities of corresponding effects of the action. There are two main differences in the forms of previous actionable rules and the behavioral rule in our approach. First, the α and γ in our rule are the attribute values associated with the current observation. Second, previous approaches can only process a single decision attribute with two possible values, while for our problem, our approach handles multiple behavior attributes, each of which may have multiple possible values. As a result, from the formalism to the method we develop, our actionable behavioral rule mining approach is different from previous approaches. Table 5 provides a comparison of different approaches.

To the best of our knowledge, there is no previous related work on actionable rule mining providing validation of the proposed approaches. Thus, the quality of mined rules can only be evaluated by domain experts. Through developing appropriate evaluation criteria, we give the empirical validation of our proposed approach, which may also shed some light on the related work. Nevertheless, developing more rigorous evaluation criteria and approaches still deserves extensive further research.

## 6. Conclusions

In this paper, we have formally formulated the problem of mining actionable behavioral rules pertinent to an entity—an individual, group, organization, or country. The proposed actionable behavior rules provide the user explicit suggestions of actions to in<sup>fl</sup>uence the behaviors of the entity in concern with satisfactory utility to the user. The problem may <sup>fi</sup>nd valuable applications in many domains, such as counter-terrorism, marketing, and human resource management. We have also proposed two algorithms for solving this new problem and conducted an experiment, which strongly recommends the validity of our proposed approach, and shows the practical value of our de<sup>fi</sup>ned problem and the comparative performance of the algorithms.

Our work has established a new important data mining problem and opened up several avenues for further research. First, while we have focused on categorical attributes and assumed that numerical attributes (if any) are discretized in advance, further research may investigate more sophisticated treatments of numerical attributes. Second, while we have conducted a preliminary experiment using domain datasets, more comprehensive experiments with many large datasets drawn from various domains can be conducted to validate the generalizability of our <sup>fi</sup>ndings. Third, another direction is to design and evaluate more ef<sup>fi</sup>cient and scalable algorithms for mining actionable behavioral rules.

Comparison of our approach and previous approaches.

<table><tr><td></td><td>Our approach</td><td>Previous actionable rule mining</td><td>Traditional classification</td></tr><tr><td>Object representation in dataset</td><td>Observations of an entity</td><td>Member objects of an entity</td><td>Observations of an entity</td></tr><tr><td>Decision attribute</td><td>Multiple</td><td>Single</td><td>Single</td></tr><tr><td>Decision attribute value</td><td>Multiple</td><td>Two</td><td>Multiple</td></tr><tr><td>Need minimum confidence</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Need minimum support</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Need action utility value specified by expert</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Rule form/output</td><td>[(α→β)]⇒[(γ→φ,p)]</td><td>[(ω)A(α→β)]⇒(γ→φ)</td><td>[α]⇒(γ)</td></tr><tr><td>Expected direct consequence of suggested action</td><td>Change the behavior of an entity</td><td>Reclassify some member objects of an entity</td><td>None</td></tr></table>

## Acknowledgments

This work is supported in part by the National Natural Science Foundation of China under Grant Nos. 60921061, 61175040, 71025001, 90924302 and 91024030, and the Research Fund of State Key Laboratory of Management and Control for Complex Systems under Grant No. 20110102.

## Appendix A

Table A1: Selected attributes in the MAROB datasets.

<table><tr><td colspan="2">Behavior attributes</td></tr><tr><td>Name</td><td>DOMORGVIOLENCE</td></tr><tr><td>Code</td><td> $b_{1}$ </td></tr><tr><td>Meaning</td><td>To what degree the organization uses violence domestically as a strategy?</td></tr><tr><td>Value</td><td>Label</td></tr><tr><td>0</td><td>Organization is not using violence as a strategy</td></tr><tr><td>1</td><td>Organization is using violence as occasional strategy but is not specifically targeting persons (coded if organization targets infrastructure and/or gives warnings before attacks)</td></tr><tr><td>2</td><td>Organization is using violence regularly as a strategy but is targeting security personnel (including state security personnel and non-state armed militias) and not government non-security personnel or civilians</td></tr><tr><td>3</td><td>Organization is using violence regularly as a strategy but is targeting security personnel(including state security personnel and non-state armed militias) and/or government non-security personnel, but not civilians</td></tr><tr><td>4</td><td>Organization is occasionally targeting civilians but most of its violent acts target security personnel or government non-security personnel</td></tr><tr><td>5</td><td>Organization is targeting civilians regularly</td></tr><tr><td>Name</td><td>TRANSVIOLTARG</td></tr><tr><td>Code</td><td> $b_{2}$ </td></tr><tr><td>Meaning</td><td>To what degree the organization uses violence to target transnational entities as a strategy?</td></tr><tr><td>Value</td><td>Label</td></tr><tr><td>0</td><td>Organization is not using transnational violence as a strategy</td></tr><tr><td>1</td><td>Organization is using transnational violence as occasional strategy but is not specifically targeting persons (coded if organization targets infrastructure and/or gives warnings before attacks)</td></tr><tr><td>2</td><td>Organization is using transnational violence regularly as a strategy but is targeting security personnel (including state security personnel and non-state armed militias) and not government non-security personnel or civilians</td></tr><tr><td>3</td><td>Organization is using transnational violence regularly as a strategy but is targeting security personnel (including state security personnel and non-state armed militias) and/or government non-security personnel, but not civilians</td></tr><tr><td>4</td><td>Organization is using transnational violence occasionally targeting civilians but most of its violent acts target security personnel or government non-security personnel</td></tr><tr><td>5</td><td>Organization is using transnational violence to target civilians regularly</td></tr><tr><td>Name</td><td>TRANSVIOLOC</td></tr><tr><td>Code</td><td> $b_{3}$ </td></tr><tr><td>Meaning</td><td>To what degree the organization uses violence transnationally outside the boundaries of the state in which the group lives?</td></tr><tr><td>Value</td><td>Label</td></tr><tr><td>0</td><td>Organization is not using transnational violence as a strategy</td></tr><tr><td>1</td><td>Organization is using transnational violence as occasional strategy but is not specifically targeting persons (coded if organization targets infrastructure and/or gives warnings before attacks)</td></tr><tr><td>2</td><td>Organization is using transnational violence regularly as a strategy but is targeting security personnel (including state security personnel and non-state armed militias) and not government non-security personnel or civilians</td></tr><tr><td>Value</td><td>Label</td></tr><tr><td>3</td><td>Organization is using transnational violence regularly as a strategy but is targeting security personnel (including state security personnel and non-state armed militias) and/or government non-security personnel, but not civilians</td></tr><tr><td>4</td><td>Organization is using transnational violence occasionally targeting civilians but most of its violent acts target security personnel or government non-security personnel</td></tr></table>

Table A1 (continued)

<table><tr><td colspan="2">Behavior attributes</td></tr><tr><td>5</td><td>Organization is using transnational violence to target civilians regularly</td></tr><tr><td colspan="2">Environment attributes</td></tr><tr><td>Name</td><td>ORSTPOLSUP</td></tr><tr><td>Code</td><td> $e_{1}$ </td></tr><tr><td>Meaning</td><td>Did foreign state provide political support?</td></tr><tr><td>Value</td><td>Label</td></tr><tr><td>0</td><td>No</td></tr><tr><td>1</td><td>Yes</td></tr><tr><td>Name</td><td>DIAFINSUP</td></tr><tr><td>Code</td><td> $e_{2}$ </td></tr><tr><td>Meaning</td><td>Did diaspora provide non-military financial support?</td></tr><tr><td>Value</td><td>Label</td></tr><tr><td>0</td><td>No</td></tr><tr><td>1</td><td>Yes</td></tr><tr><td>Name</td><td>ORGCULTGR</td></tr><tr><td>Code</td><td> $e_{3}$ </td></tr><tr><td>Meaning</td><td>Code the dominant cultural grievance of the organization.</td></tr><tr><td>Value</td><td>Label</td></tr><tr><td>0</td><td>No expressed cultural grievances</td></tr><tr><td>1</td><td>Cultural grievances focused on elimination of discrimination</td></tr><tr><td>2</td><td>Cultural grievances focused on creating or strengthening economic remedial policies (i.e., establishing or increasing state funding for cultural protection and/or promotion)</td></tr></table>

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceeding of the Twentieth International Conference on VLDB, 1994, pp. 487–499.

[2] M.-L. Antonie, O.R. Zaïane, An associative classi<sup>fi</sup>er based on positive and negative rules, Proceedings of the Ninth ACM SIGMOD Workshop on Research Issues in Data Mining and Knowledge Discovery, 2004, pp. 64–69.

[3] E. Baralis, S. Chiusano, P. Garza, On support thresholds in associative classi<sup>fi</sup>cation, Proceedings of the 2004 ACM Symposium on Applied Computing, 2004, pp. 553–558.

[4] E. Baralis, P. Garza, A lazy approach to pruning classi<sup>fi</sup>cation rules, Proceedings of the Second IEEE International Conference on Data Mining (ICDM'02), 2002, pp. 35–42.

[5] J. Bond, V. Petroff, S. O'Brien, D. Bond, Forecasting turmoil in Indonesia: an application of hidden Markov models, Proceedings of the International Studies Association Annual Convention, 2004, pp. 11–27.

[6] L. Cao, Y. Zhao, H. Zhang, D. Luo, C. Zhang, E.K. Park, Flexible frameworks for actionable knowledge discovery, IEEE Transactions on Knowledge and Data Engineering 22 (9) (2010) 1299-1312.

[7] J. Han, J. Pei, Y. Yin, R. Mao, Mining frequent patterns without candidate generation: a frequent-pattern tree approach, Data Mining and Knowledge Discovery 8 (1) (2004) 53–87.

[8] Z. He, X. Xu, S. Deng, R. Ma, Mining action rules from scratch, Expert Systems with Applications 29 (3) (2005) 691–699.

[9] H. Kaur, Actionable rules: issues and new directions, Proceedings of World Academy of Science, Engineering and Technology, 2005, pp. 61–64.

[10] S. Khuller, M. Martinez, D. Nau, A. Sliva, G. Simari, V. Subrahmanian, Computing most probable worlds of action probabilistic logic programs: scalable estimation for 10<sup>30,000</sup> worlds, Annals of Mathematics and Arti<sup>fi</sup>cial Intelligence 51 (2) (2007) 295–331.

[11] E. Kim, W. Kim, Y. Lee, Combination of multiple classi<sup>fi</sup>ers for the customer's purchase behavior prediction, Decision Support Systems 34 (2003) 167–175.

[12] W. Li, J. Han, J. Pei, CMAR: accurate and ef<sup>fi</sup>cient classi<sup>fi</sup>cation based on multiple class-association rules, Proceedings of the First IEEE International Conference on Data Mining (ICDM'01), 2001, pp. 369–376

[13] C. Ling, T. Chen, Q. Yang, J. Chen, Mining optimal actions for intelligent CRM, Proceedings of the Second IEEE International Conference on Data Mining (ICDM'02), 2002, pp. 767–770.

[14] B. Liu, W. Hsu, S. Chen, Using general impressions to analyze discovered classi<sup>fi</sup>- cation rules, Proceedings of the Third International Conference on Knowledge Discovery and Data Mining (KDD'97), 1997, pp. 31–36.

[15] B. Liu, W. Hsu, Y. Ma, Integrating classi<sup>fi</sup>cation and association rule mining, Proceedings of the Fourth International Conference on Knowledge Discovery and Data Mining (KDD'98), 1998, pp. 80–86.

[16] Z. Pawlak, Information systems theoretical foundations, Information Systems 6 (3) (1981) 205–218.

[17] Z. Ras, A. Dardzinska, Action rules discovery without pre-existing classi<sup>fi</sup>cation rules, Proceedings of RSCTC 2008 Conference, 2008, pp. 181–190.

[18] Z. Ras, A. Dardzinska, L.-S. Tsay, H. Wasyluk, Association action rules, Proceedings of IEEE/ICDM Workshop on Mining Complex Data (MCD'08) 2008 pp. 283–290

[19] Z. Ras, A. Tzacheva, In search for action rules of the lowest cost, in: B. Dunin-Keplicz, A. Jankowski, A. Skowron, M. Szczuka (Eds.), Monitoring, Security, and Rescue Techniques in Multiagent Systems, Springer-Verlag, 2005, pp. 261–272.

[20] Z. Ras, A. Tzacheva, L. Tsay, O. Gurdal, Mining for interesting action rules, Proceedings of IEEE/WIC/ACM International Conference on Intelligent Agent Technology (IAT'2005), 2005, pp. 187–193.

[21] Z. Ras, A. Wieczorkowska, Action-rules: how to increase pro<sup>fi</sup>t of a company, in: D. Zighed, J. Komorowski, J. Zytkow (Eds.), Principles of Data Mining and Knowledge Discovery, Springer-Verlag, 2000, pp. 75–116.

[22] P. Schrodt, Forecasting con<sup>fl</sup>ict in the Balkans using hidden Markov models, in: T. Robert (Ed.), Programming for Peace, Springer-Verlag, 2006, pp. 161–184.

[23] A. Silberschatz, A. Tuzhilin, What makes patterns interesting in knowledge discovery systems, IEEE Transactions on Knowledge and Data Engineering 8 (6) (1996) 970–974.

[24] V. Subrahmanian, Computer science: cultural modeling in real time, Science 317 (5844) (2007) 1509–1510.

[25] V. Subrahmanian, M. Albanese, M. Martinez, D. Nau, D. Reforgiato, G. Simari, A. Sliva, O. Udrea, J. Wilkenfeld, CARA: a cultural-reasoning architecture, IEEE Intelligent Systems 22 (2) (2007) 12–16.

[26] A. Tzacheva, Z. Ras, Action rule mining, International Journal of Intelligent Systems 20 (7) (2005) 719–736.

[27] A. Tzacheva, L.-S. Tsay, Tree-based construction of low-cost action rules, Fundamenta Informaticae 86 (1,2) (2008) 213–225.

[28] K. Wang, S. Zhou, Y. He, Growing decision trees on support-less association rules, Proceedings of the Sixth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2000, pp. 265–269.

[29] Q. Yang, H. Cheng, Mining case bases for action recommendation, Proceedings of the Second IEEE International Conference on Data Mining (ICDM'02), 2002, pp. 522–529.

[30] Q. Yang, J. Yin, C. Ling, T. Chen, Post processing decision trees to extract actionable knowledge, Proceedings of the Third IEEE International Conference on Data Mining (ICDM'03), 2003, pp. 685–688.

![](/api/attachments/Q4XC97ER/fulltext/images/d561081624b79d553a776b51288ae37217588884e74a4afae9307d8e9b20d723.jpg)  
Peng Su received his Ph.D. degree in Computer Application Technology from the Chinese Academy of Sciences in 2011. He is a lecturer in the School of Management Engineering at Shandong Jianzhu University. Dr. Su is a member of IFAC Technical Committees on Economic and Business Systems (TC9.1). His research interests mainly focus on data mining and social computing.

![](/api/attachments/Q4XC97ER/fulltext/images/62b273760d340c642983b894356d64cb0e8551a7bcfe37f96463cb093a63ecc7.jpg)

![](/api/attachments/Q4XC97ER/fulltext/images/da6b33d89235993c08d6305dfc4a3ba199bc36121de893331d98ff151d1f08cd.jpg)

![](/api/attachments/Q4XC97ER/fulltext/images/edba725d5dfc45c6386c50bd780509078d1bb2b0c299261b680b66b1742815a5.jpg)

Wenji Mao received her Ph.D. degree in Computer Science from the University of Southern California in 2006. She is an associate professor at the Institute of Automation, Chinese Academy of Sciences. Prof. Mao is a member of ACM and AAAI, and a senior member of the China Computer Federation. Her research interests include arti<sup>fi</sup>cial intelli gence, multi-agent systems and social modeling.

Daniel Zeng received his Ph.D. degree in Industrial Administration from the Carnegie Mellon University in 1998. He is an associate professor and the director of the Intelligent Systems and Decisions Laboratory in the Department of Management Information Systems at the University of Arizona's Eller College of Management. He is also an af<sup>fi</sup>liated professor at the Institute of Automation, Chinese Academy of Sciences. Prof. Zeng is a member of IEEE. His research interests include software agents and multi-agent systems, intelligence and security informatics, social computing and recommender systems.

Huimin Zhao received the B.E. and M.E. degrees in automation from Tsinghua University, Beijing, China, in 1990 and 1993, respectively, and the Ph.D. degree in management information systems from the University of Arizona, Tucson, Arizona, USA in 2002. He is an Associate Professor of management information systems in the Sheldon B. Lubar School of Business at the University of Wisconsin– Milwaukee. His current research interests include data mining and recommendation systems. He is a member of the IEEE, the Association for Information Systems (AIS), and the Information Resources Management Association (IRMA).
