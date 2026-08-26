---
otero_id: 13714
otero_key: "EVC3UJAQ"
title: "Linking analytic hierarchy process and social choice methods to support group decision-making in water management"
authors: "Bojan Srdjevic"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.08.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Linking analytic hierarchy process and social choice methods to support group decision-making in water management

Bojan Srdjevic <sup>⁎</sup>

Department of Water Management, Faculty of Agriculture, University of Novi Sad, 21000 Novi Sad, Trg D. Obradovica 8, Serbia

Received 19 November 2005; received in revised form 25 April 2006; accepted 6 August 2006 Available online 3 October 2006

## Abstract

The social choice (SC) theory is in close relation with multicriteria decision-making (MCDM), especially in group decision contexts. SC theory includes various voting systems while MCDM is represented by utility and outranking methods; among utility models, the analytic hierarchy process (AHP) is probably the most popular in group decision support. In this paper, we investigate two possible contexts in modeling decentralized decision problems in water management. The first is based on AHP only and two group aggregation techniques. The second one assumes the AHP application in subgroups, while at a group level, aggregation is performed by the SC voting procedures. Comparative analyses show good agreement of the results when two methodologies are applied as the decision support to the water committee of the San Francisco river basin in Brazil. The second methodology (called AHP + SC) is considered more promising for implementation in real-decision situations in water management. © 2006 Elsevier B.V. All rights reserved.

Keywords: Group decisions; AHP; Social choice methods; Water management

## 1. Introduction

Two basically distinct methodologies are commonly used in group decision-making. The first, multicriteria decision-making (MCDM), is particularly useful in handling structured decision-making problems. The other is the social choice (SC) theory with its voting systems for group decision-making when available information is minimal, unconfident, or predominantly qualitative.

The inherent characteristics of the group decision problem determine which methodology should be used and what outcome can be expected. For example in the MCDM applications, the size of a group may become critical because most of the multicriteria methods rely on an assumption that the homogeneity principle is valid. Several authors argue that in larger groups this assumption may be violated and advocate a group clustering based on similarities in decision-making preferences [1] wherever the group is of an intermediate or large size [28]. However, even in subgroups some of the problems related to a group may reappear, such as the tedious and time-consuming process of eliciting judgments, and additional sub-grouping could be necessary. On the other hand when considering the SC theory applications, the more important issues are fairness and the manipulation of the voting system used. Because none of the voting methods is immune to violation from at least one of the commonly used fairness criteria, to preserve the homogeneity of the decision process, group clustering is an opportunity to conduct the election process in a democratic manner [5,14].

If the MCDM methodology is to be used in group decision-making, the analytic hierarchy process (AHP) [25] is probably one of the best choices. The AHP itself is a complete methodology for solving hierarchically structured decision problems. It elicits the decision maker's (DM) judgment of elements in a hierarchy and mathematically manipulates them to obtain the final preference weights of the decision alternatives with respect to the overall goal. In the most general case, the criteria are first judged with respect to the overall goal and then used as ‘local goals’ for eliciting the DM's judgment of the alternatives. The AHP is widely used for supporting individual and group decision-making in two major versions: (1) standard (denoted hereafter as SAHP) [25], and multiplicative (MAHP) [17]. Although the method is principally used in individual decisionmaking, extensions for group applications are achieved by establishing two typical aggregation contexts. The first is an aggregation of the individual judgments (AIJ) during the decision process, and the second is an aggregation of the individual priorities (AIP) of the evaluated alternative decisions once the decision process is completed. Which aggregation method is applicable or should be used in various decision-making situations is under continuous discussion in literature (e.g. [1,6,8,23,24]). Worthy to mention are some more recent investigations concerned with integrating the independent stages of group synthesis and prioritization in AHP into the unique process by methods such as goal programming [3], or fuzzy preference programming [20].

If the SC methodology is selected as being more favorable in group decision-making, several approaches have been proposed for aggregating voters' responses into a compromise ranking. Well-known election methods are plurality voting, the Hare system, the Borda count, pairwise comparisons voting and approval voting. All except the last are considered preferential methods based on ordinal preferences of candidates that are voted for. Voting methods serve as support in searches for collective choice, and many authors in the SC literature have suggested when and how to use them to find the best decision under conflicting preferences of the decision makers or interest groups. A comprehensive summary of the SC methods with case studies may be found in Refs. [27,19]. A relevant survey of different voting systems is also given in Ref. [13] and more recently by Laukkanen et al. [15]. An interesting discussion of the application of SC methods in water and natural resource management can be found in Refs. [7,15], respectively. A general framework for reaching consensus in ordinal ranking models based on distance measures is presented in Ref. [4]. Regarding MCDM and SC applications in the field of natural resource management, worth mentioning are also Refs. [10–12,16,18,26]. Because AHP has already a vast number of applications, an interested reader for studies where SC has been applied to natural resource management should consult [12,16,18].

In a group decision-making context, MCDM and SC perform differently with respect to issues such as justice, fairness, or transparency to manipulation at various stages of implementation. Various authors report that the use of the two different MCDM (or SC) methods may easily declare different winners. As correctly noticed in Ref. [7, p. 204] ‘… this is the main reason why comparison of different methods applied to the same problem is useful to both scientists and practitioners, since the detailed analysis of the results helps to find the most appropriate solution methodology in similar cases'.

In this paper, a methodology is proposed for combining the MCDM and SC theory in a group decision-making process. The problem analyzed is the selection of the most desired long-term water management plan by an authorized institution such as the river basin water committee (WC). The WC is considered as a decision body (global group) that may split into a certain number of interest subgroups (IGs). Assuming that certain decisions will be made in the IGs, the final decision should certainly be made at the WC level in a democratic manner with respect to the preferences derived by participating IGs. The proof-of-concept application is performed for the Water Committee of the San Francisco River Basin in Brazil; however, an approach is applicable to any similar decision-making context where different outcomes of the decision-making process in sub-groups have to be manipulated and aggregated to derive an acceptable solution for involved participants.

The proposed methodology is organized as a twostage procedure. At the first stage, an MCDM context is assumed and an AHP methodology is applied within each IG to determine the cardinal preferences for a given set of management plans. At the second stage, two options are proposed for aggregating the results of AHP obtained in IG. The first one is to keep going within an MCDM context and mathematically aggregate the priority weights as received from IG. The aggregation of priorities can be accomplished by either weighted average mean method (WAMM), or geometric mean method (GMM). If the standard AHP is used, either a WAMM or GMM aggregation is applicable; however, if a multiplicative AHP is used, only the GMM aggregation makes sense. The second option is to change the context and perform an aggregation by the SC methods. Using as an input the preferences obtained by AHP in each IG, different voting methods are employed to simulate the election of the candidate plans and declare the winner. A proposed change from MCDM to SC context implies that in the second stage only, the ordinal preference information related to plans is exploited. A compensation for such an intentional reduction of available information is found in an intriguing willing of the WC as a global decision-making body to behave democratically and enable representatives of important IGs to vote and elect the most desired management plan. Therefore, the second methodology, called AHP + SC, where AHP applies at sub-group levels and selected SC methods apply at a global-group level, is proposed as more realistic for implementation in complex decision situations such as participatory water management.

Proposed AHP+SC methodology is not immune of difficulties that may arise in certain real-life situations. One must be aware of truth that AHP + SC in some cases probably can give results which are not fully consistent with the experts' judgments, especially if there are more than three alternatives. The Arrow's classic impossibility theorem shows that in these cases there is no fair way of forming a group ranking from a consistent set of individual (or subgroup) rankings. Also, the final ranking, obtained by voting (SC part of a decisionmaking process) does not necessarily depend on the number of experts, and on the size of the subgroups. Actually, in the SC process of voting a large subgroup of experts has the same power as a small subgroup which could yield to ranking that do not satisfy the conditions of social welfare functions, and especially the principle of majority decision. With this in mind, we underline importance of proper manipulation of an overall decision-making process with large number of individuals (not necessarily real experts) and preserving the balance of groups' sizes. Experience says that in large river-basin water committees, such as this one of San Francisco river in Brazil with 60 members, a decisionmaking process related to planning and overall water management will expectedly be performed with participation of ‘oriented committee members,’ bringing particular backgrounds and mostly narrowed interests from social, political or economic environments they are coming from. Therefore, in AHP part of proposed methodology we recognize importance of using different weights for individuals and assume standard aggregation of their judgments, i.e. priorities, but we do not elaborate it in more details. Our approach rather implies that representatives in water committee should not receive different weights due to their assumed or demonstrated powers, because we believe it would be hard to provide reasonable explanation for doing it without provoking an early confrontation of individuals and sub groups and possible reluctance and/or obstruction of the decision-making process in general.

The paper is organized in the following way. Section 2 presents a brief discussion on issues related to the linking of the SC methods with the AHP. The standard and multiplicative AHP are described in Section 3 as well as methods for group aggregations. The SC methods are briefly presented in Section $4 ;$ a modification of the no-preferential approval voting method is also presented as a part of the proposed AHP + SC methodology for group–subgroup decision-making. A case study application of the two methodologies: (1) AHP only, and (2) combined AHP+SC, is described in Section 5. The last Section 6 presents a summary of the results and conclusions.

## 2. Linking AHP and social choice methods

The AHP is a multi-attribute utility theory method based on the cardinal preferences of elements contained in a given hierarchy of the decision problem. At its final instance, AHP gives a measure of the relative priorities of the alternatives. The direct use of this information may be useful in decision problems such as resource allocation or cost and benefit analysis. However, in various situations only ordinal preferences are important, and the AHP results may be used similarly as the results of outranking methods [17]. The cases where the notion of mutual relative importance of alternatives is irrelevant offer an important link toward SC theory. This theory, in general, searches for the best option only (‘elected winner’), or, in extended applications, for the complete ranking of candidates (alternatives). Relative power, or influence, or candidates in the SC context is important only in evaluating part of the election process, but during the final election the only important decision is whether certain candidates receive votes or not.

In group applications, AHP may be used in various ways. Which version of AHP will be employed (e.g. standard or multiplicative), and which method will be selected for aggregating individual judgments (AIJ) or final priorities (AIP) of the alternatives is a decision by itself that can be made by an individual or by a group; in the later case, it can be accomplished through consensus, by voting or by authorizing the expert(s) to prepare a decision in favor of a group. This decision is, furthermore, closely related to creating the hierarchy and describing its elements (particularly in evaluating criteria), possible sub-grouping, elicitation of judgments from individuals, and adoption of the procedure for final synthesis. Whatever preference aggregation procedure is used, at the final instance both cardinal and ordinal preference information is available. If the decision problem is to select the most desired plan of action, the ordinal preferences are sufficient to enable the use of the SC methods; i.e., to perform or simulate a voting procedure and declare the winner.

Most voting systems are based on a single criterion or just on holistic preference information on decision alternatives. Although all were developed to be neutral and difficult to manipulate, each method is more or less deficient with respect to a notion of fairness and manipulation, including the most recent systems such as multicriteria approval [9], or declared-strategy voting [5]. For example in a declared-strategy voting system, it has been proved that the best interest of the voter is to strategically manipulate the election by voting for a candidate other than the one preferred the most. This system has a lot to do with the basic principles of fairness and neutrality that cannot be neglected without proper justification; and it is done by initially declaring the assumption that voting will be strategically manipulated.

While conducting any voting an ordinal information input is used, which means that the information base is a priori reduced in comparison to the cardinal preference information used in aggregating the results of AHP models. Furthermore, the AHP models deal with multiple criteria which, in general, means a more profound analysis of the decision problem and keeping the decision process under control in a way to preserve consistency and homogeneity of eliciting the judgments from the individual DMs. An attempt to compensate deficiencies in the information base in voting is made by developing the multicriteria approval voting scheme applicable for group decision making with multiple criteria. The ideas behind the scheme and some of the reported applications (e.g. [9,15]) indicate the potential of this system in multicriteria decision-making. The leading idea is that in composing the decision matrix, the voters of the SC theory are treated as criteria in MCDM, thus permitting their ranking by importance unlike voters in the standard SC methods. It is not, however, completely clear what implications in real use may be expected; for example, how to explain that some voters in a homogeneous group will have more power in the voting process. We believe that this system has potential, but that it suffers from being artificial and not transparent to the DMs, which rather prefer ‘understandable’ methods.

Here we propose a straightforward procedure for linking the AHP and SC methods in supporting the group decision-making process. The AHP methodology at the subgroup level is combined with the voting methods at the group level in a way to keep available the cardinal preference information on the decision alternatives (obtained by either the SAHP or MAHP model) until the latest possible moment, and in this way to enable group aggregation in a manner that is subject to a particular decision of the group. The group may decide to continue with the mathematical aggregation of the cardinal information received from the subgroups, or to elect the best solution by authorizing subgroups' representatives to vote in strict favor of their subgroups. In other words, there are two possibilities. The first is to use the AHP methodology only, which implies that group members participate only during subgroups' sessions (where detailed AHP evaluations are made). The second is to combine the AHP methodology with SC methodology, and avoid the mathematical aggregation of the AHP results by rather permitting representatives of the subgroups to vote. In our approach, it is not important if voting is really undertaken or simulated. From a social-theory point of view, these two options are fundamentally different in various aspects such as: the quantity and quality of available and used information, participation of group members, reliability of the results, possibility for manipulating the process, etc. If a combined AHP+SC methodology is chosen, it is still not possible to claim that any particular combination of any version of AHP with any voting method will give a better result then other possible combinations. This claim is however, general, because it is valid for any existing method that deals with compromises. A good agreement of results in the case study application for various combinations of AHP and voting models indicates that the proposed approach has a potential in real-life group decision-making, as well as a strong theoretical background taken from both the MCDM (AHP) and SC theories.

## 3. Aggregating priorities within standard and multiplicative AHP methodology

Two commonly used versions of AHP, standard and multiplicative, do not differ significantly in the methodological sense. Namely after decomposing the problem into a hierarchy, in both versions, elements at a given hierarchical level are compared in pairs to assess their relative preference with respect to each of the elements at the next higher level; the same operation is performed at each level in a downward direction. The judgment terms presented in the first column of Table 1 are used to assess the intensity of preference between any two elements. In the standard AHP, the numerical scale (the second column of Table 1) is used to capture verbal comparisons, and facilitate the weighting of quantifiable and non-quantifiable elements. In other words, once the verbal judgments are made, they are simply translated into numbers by means of the Saaty's scale. Instead, Lootsma proposed the distance scale given in the third column of Table 1. By means of the Lootsma's scale and parameterised exponential transform the judgments are translated into numbers on the geometric ratio scale. Because several modifications are also implemented in manipulating the judgments and the synthesis of the results, this version of the method is known as the multiplicative AHP.

Table 1  
Saaty's and Lootsma's scale for pairwise comparisons in AHP

<table><tr><td rowspan="2">Judgment term</td><td>Saaty&#x27;s scale</td><td>Lootsma&#x27;s scale</td></tr><tr><td> $(a_{ij})$ </td><td> $(\delta_{ij})$ </td></tr><tr><td>Absolute preference (element i over element j)</td><td>9</td><td>+8</td></tr><tr><td>Very strong preference (i over j)</td><td>7</td><td>+6</td></tr><tr><td>Strong preference (i over j)</td><td>5</td><td>+4</td></tr><tr><td>Weak preference (i over j)</td><td>3</td><td>+2</td></tr><tr><td>Indifference of i and j</td><td>1</td><td>0</td></tr><tr><td>Weak preference (j over i)</td><td>1/3</td><td>-2</td></tr><tr><td>Strong preference (j over i)</td><td>1/5</td><td>-4</td></tr><tr><td>Very strong preference (j over i)</td><td>1/7</td><td>-6</td></tr><tr><td>Absolute preference (j over i)</td><td>1/9</td><td>-8</td></tr><tr><td colspan="3">An intermediate numerical values are used in both scales to model hesitations between two adjacent judgments</td></tr></table>

Both the standard and multiplicative AHP are well documented in pertinent literature and their description is avoided here. In both versions, the final result is a vector $\pmb { z } { = } ( z _ { 1 } , z _ { 2 } , . . . , z _ { N } )$ composed of weights for N alternatives at the bottom level of the hierarchy with respect to the goal at the top of the hierarchy. The highest value in z is associated with ‘the best alternative,’ and the lowest with ‘the worst alternative'.

So far, the standard and multiplicative version of AHP for a single DM has been considered. If there is more than one DM, the overall priorities of the alternatives can be computed only after the individual opinions of all DMs have been elicited. Forman and Peniwati [8] suggest that, depending on the adopted approach, there are three possibilities to aggregate such information: (1) to aggregate the individual judgments for each set of pairwise comparisons into an ‘aggregate hierarchy’; (2) to synthetize individual hierarchies and aggregate the resulting priorities; and (3) to aggregate the derived individual priorities in each node of the hierarchy The first is commonly referred to as aggregating the individual judgments (AIJ), and the second as aggregating the individual priorities (AIP); the third possibility is less meaningful. It is also argued that AIJ and AIP are philosophically different circumstances [8], and whether AIJ or AIP should be used depends on whether the group intends to behave as a synergistic unit or as collection of individuals. As far as group aggregations are considered, an additional issue is how to obtain the individuals weights if they are not to be equally weighted, and how to use them in aggregation.

In the group-subgroup context that is of interest here, there are two important facts. The first is that AIJ is possible to apply only at the subgroup level by eliciting judgments from the real individuals, the members of the subgroup. The second is that at a group level, AIJ is not applicable since an information on individual judgments is generally not available or meaningful; it is rather synthetized during the subgroup decision-making into priority weights of the alternatives and in this integral form reported to the group. Therefore at a group level, only AIP is possible by using the preference information on the evaluated alternatives received from the subgroups. The only thing left is to determine the proper procedure for AIP, which will as much as possible account for behavior of subgroups; i.e., available knowledge on their interests, abilities and attitudes exposed in obtaining the partial (subgroup) results by AHP.

Two commonly used AIP methods are the weighted arithmetic mean method (WAMM) and the geometric mean method (GMM):

▪ Aggregation by weighted arithmetic mean method (WAMM). Given alternative $A _ { i }$ and its resulting priority weight $z _ { i k }$ for individual k. If weight $w _ { k }$ is assigned to an individual k in a group of G individuals, then the arithmetic mean is

$$
z _ {i} ^ {\mathrm{g}} = \sum_ {k = 1} ^ {G} w _ {k} z _ {i k}\tag{1}
$$

where z<sup>g</sup> stands for final (composite) priority weight of the alternative $A _ { i } .$ The individuals' weights $w _ { k }$ are by assumption additively normalized.

▪ Aggregation by geometric mean method (GMM). This aggregation is performed by applying Eq. (2)

$$
z _ {i} ^ {\mathrm{g}} = \sum_ {k = 1} ^ {G} z _ {i k} ^ {w _ {k}}\tag{2}
$$

where the individuals' weights $w _ { k }$ are also additively normalized.

An example application of WAMM in AIP may be found in Ref. [24] where it is claimed that only this method of aggregation does not violate the Pareto (agreement) principle. Forman and Peniwati [8] refer to that claim and provide an interesting discussion on the issue by arguing that either GMM or WAMM may be used in most cases of group decision-making without violating the Pareto principle. At the final instance, they provide reasons for using the GMM, rather than WAMM.

In the web-based decision support application for individuals and groups known as Web-HIPRE [21], the aggregation is enabled in a way to take the overall priorities from each individual's AHP model, weight them according to the ‘importance’ of each individual and finally perform averaging to obtain the composite group priorities; the group needs to decide on the weight for each individual or assume that they are all equal. An aggregation of each of the individual's priorities can be performed by using a geometric mean as well. For each individual, the resulting priority weights of the alternatives (obtained by AHP) are raised to the power which is a value of the individual weight within a group; it assumes a prior additive normalization of the individual weights. Then, the raised priorities are multiplied for each alternative across all individuals and the appropriate root is taken. Finally, additive normalization is performed.

Recent studies indicate that both WAMM and GMM can be used in group decision-making for aggregating individual priorities (AIP). In a case study application presented in Section 5, WAMM and GMM were used to synthesize the subgroups' priorities for a given set of management plans, and the same final orderings were obtained for both methods. Worthy to mention here is that full agreement has also been obtained for MAHP and GMM application in AIP.

## 4. Social choice methods

Typically used SC methods, known as the preferential and non-preferential voting methods, are described below. All exclusively use ordinal preference information contained in the preference table created by collecting ballots (in real elections), by applying AHP (as is the case here), or by using a certain outranking method, etc. Notice that the terminology from SC theory is slightly adjusted here to make it comparable to the terminology used in the MCDM context.

## 4.1. Preference schedule

In applying voting methods, a special preference schedule table is useful to construct with the following properties. The size of the table is $M \times N ,$ where M is the number of subgroups and N is the number of alternatives. Each row represents the ranking of the alternatives performed by one subgroup. If j is the best alternative for ith subgroup, then rank number is $r _ { i j } = 1$ $\mathrm { i f } j$ is the second best alternative, then $r _ { i j } = 2$ , and so on; if alternative j is the worst one, then $r _ { i j } { = } N .$ . This way, each row of the preference table is simply a permutation of the integers $1 , 2 , . . . , N .$

## 4.2. Plurality voting

In this method, an alternative with the most first place ‘votes’ wins. Notice, however, that the winner does not have to receive a majority of the first-place votes. Using the notation similar to d'Angelo et al. [7], this concept can be mathematically formulated as follows:

Define $p ( r _ { i j } ) { = } 1$ for $r _ { i j } = 1$ , and $p ( r _ { i j } ) { = } 0$ otherwise. If for each alternative j the sum

$$
P _ {j} = \sum_ {i = 1} ^ {M} p (r _ {i j})\tag{3}
$$

is computed, then the number $P _ { j }$ simply indicates how many times alternative j has been ranked as the best. The alternative $A _ { j * }$ with the largest $P _ { j }$ value is considered the social choice.

$$
P _ {j ^ {*}} = \max _ {1 \leq j \leq N} \{P _ {j} \}.\tag{4}
$$

## 4.3. The Hare system

The Hare system is also known as the plurality with elimination method, because the plurality method is carried out in rounds. After each round of voting, the alternative with the fewest first place votes is eliminated and a new round of voting is done with the remaining alternatives. For an N alternative election, the Hare system requires $N - 1$ rounds at a maximum. The process terminates when there is an alternative with the number of first place votes greater than or equal to half of the number of alternatives. When only two alternatives remain in a round, the alternative with the most votes wins the election. If, at any stage of the procedure, the quantities $P _ { j }$ are equal to each other for all remaining alternatives, the process also terminates.

Notice that there is no need to hold any new election since each voter (here sub group) completed a ‘preference ballot’ and all ballots are used to create the preference schedule (see Subsection 4.1). The eliminated alternative in a given round is simply removed, and the remaining alternatives are adjusted appropriately in the preference schedule; for each column of a preference schedule, each alternative below an eliminated one moves up one place while the positions of alternatives above an eliminated one remain unchanged.

Mathematically at each round, the deleted alternative $j ^ { * }$ is selected as:

$$
P _ {j ^ {*}} = \min _ {1 \leq j \leq N} \left\{P _ {j} \right\}\tag{5}
$$

where the quantities $P _ { j }$ are defined in the plurality voting (see Eq. (3)). After deleting the alternative selected by Eq. (5), the preference schedule is modified in the following way:

$$
\begin{array}{l l} r _ {i j} ^ {\text { new }} = r _ {i j} ^ {\text { old }}   -   1 & \quad \text { if } r _ {i j} ^ {\text { old }}   >   r _ {i j} ^ {\text { old }}   * \\ = r _ {i j} ^ {\text { old }} & \quad \text { if } r _ {i j} ^ {\text { old }}   <     r _ {i j} ^ {\text { old }}   * \end{array}\tag{6}
$$

(for all i and $j \neq j ^ { \ast } )$

## 4.4. The Borda count

In this method, each alternative gets 1 point for each last place vote received, 2 points for each next-to-last point vote, etc., all the way up to N points for each first place vote. The alternative with the largest point total wins the election and is declared to be the social choice.

For each $r _ { i j }$ in the preference schedule, a number

$$
q _ {i j} = N - r _ {i j} + 1\tag{7}
$$

is assigned by the above procedure, and the total score for alternative j is given as

$$
\begin{array}{c} Q _ {j} = \sum_ {i = 1} ^ {M} q _ {i j} = \sum_ {i = 1} ^ {M} (N - r _ {i j} + 1) \\ = M (N - 1) - \sum_ {i = 1} ^ {M} r _ {i j} \end{array}\tag{8}
$$

The alternative $j ^ { * }$ with the highest $\boldsymbol { Q }$ value is then selected as the winner, i.e. social choice.

$$
Q _ {j ^ {*}} = \max _ {1 \leq j \leq N} Q _ {j}.\tag{9}
$$

## 4.5. Pairwise comparisons voting

In this method, each alternative is matched head-tohead with each of the other alternatives. Each alternative gets 1 point for a one-on-one win and a half a point for a tie. The alternative with the most total points is the winner.

In group-subgroup decision-making context, for each ordered pair $( j _ { 1 } , j _ { 2 } )$ of alternatives, it is determined by how many subgroups alternative $j _ { 1 }$ is preferred to $j _ { 2 }$ . If this number is denoted by $N ( j _ { 1 } , j _ { 2 } )$ , alternative $j _ { 1 }$ is preferred to alternative $j _ { 2 }$ if $N ( j _ { 1 } , j _ { 2 } ) { > } N j _ { 2 } , j _ { 1 } )$ , and alternative $j _ { 1 }$ gets a point. If $N ( j _ { 1 } , j _ { 2 } ) { = } N ( j _ { 2 } , j _ { 1 } )$ , which may happen only if the number of sub groups is even, both alternatives $j _ { 1 }$ and $j _ { 2 }$ receive a half a point. The simple addition of points for each alternative match up declares the winning alternative, which is considered the social (group) choice.

## 4.6. Approval voting

So far, the presented voting methods are preferential because they all use information directly from a preference schedule. Approval voting does not do so and is therefore considered as non-preferential. In this method, voters can vote for as many candidates as they wish. Each approved candidate receives one vote and the candidate with the most votes wins.

Approval voting is considered simple for voters to understand and use [2]. In general, the method is practical because adding or removing candidates does not change the point totals of the other candidates. If candidates drop out, it is enough to simply remove them from the list; if candidates are added, the vote totals for the original candidates remain the same, and voters only have to give their approval or disapproval of the candidates that are added.

The approval voting method needs to be adapted for the group-subgroup decision-making context proposed here. Let's assume that consensus at a group level exists such that a certain number of top ranking alternatives will be approved from each subgroup list obtained by the use of AHP. Modified approval voting will then select the alternative that has the largest number of so approved votes. Mathematically, this concept can be formulated as follows:

Define

$$
\begin{array}{c} h (r _ {i j}) = 1 \text { if } r _ {i j} {\leq} p \\ 0 \text { otherwise } \end{array}\tag{10}
$$

for all i and j. The value of p is prescribed to be between 1 and $N \left( 1 < p < N \right)$ . Then, for each alternative $j ,$ let

$$
V _ {j} = \sum_ {i = 1} ^ {M} h (r _ {i j})\tag{11}
$$

The number $V _ { j }$ indicates how many times alternative $j$ has been approved by all subgroups (voters). The alternative $j ^ { * }$ with the largest $V _ { j }$ value is then selected as the social choice:

$$
V _ {j ^ {*}} = \max _ {1 \leq j \leq N} \{V _ {j} \}.\tag{12}
$$

## 5. Application

## 5.1. Composition of the Water Committee

The Water Committee (WC) of the San Francisco River Basin in Brazil is assumed to be composed of 60 members. All come from six states (Minas Gerais, Bahia, Pernambuco, Alagoas, Sergipe, and Goiais), except one member who represents the Federal District of Brasilia and Government of Brazil. Although the WC is still in a constitutional phase, it is possible to identify six major interest groups (IG) composed of a different number of delegates that varies from 5 (Producers) to 16 (Public authorities), as given in Table 2.

## 5.2. Decision problem

Suppose that the WC has to select the best among five general management plans for planning horizon 2020, and that five global criteria were adopted for evaluating the plans. Let's also assume that the WC decided by consensus to use the hierarchy created with the overall goal (‘The Best Plan’) on the first level, criteria on the second, and plans on the third level.

The criteria for evaluating plans are identified as: (1) Political influence, (2) Economic criterion, (3) Social issues, (4) Environmental protection, and (5) Technical criterion. Political influence is considered as the gradually exposed impact of various state and in-basin agencies and bodies, representatives of cities/villages, stakeholders, producers and local leaders. Economic criterion is related to real possibilities to implement the economical process, reliability of economical parameters, estimated costs of investment, operation and maintenance, and expected direct and indirect benefits. Social criterion relates to issues such as infrastructure, demographic changes (migration), health care and working conditions. Environmental protection criterion relates to specific environmental and ambient conditions such as the distribution of pleasant resorts, preservation of historical sites and cultural values, accessing the objects and facilities, protecting water quality, and particularly preserving acceptable sanitary conditions. Technical criterion encapsulates interests in preserving proper spatial distribution of projects, technical conditions for project operations, technologies involved, and eligibility for technical improvements.

Structure of the Water Committee of the San Francisco River Basin (Brazil)

<table><tr><td>IG</td><td>Interest groups</td><td>MG</td><td>BA</td><td>PE</td><td>AL</td><td>SE</td><td>GO</td><td>DF</td><td>Total</td></tr><tr><td>1</td><td>Public authorities</td><td>5</td><td>3</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>16</td></tr><tr><td>2</td><td>Civil society</td><td>5</td><td>3</td><td>2</td><td>2</td><td>2</td><td>-</td><td>-</td><td>14</td></tr><tr><td>3</td><td>Small users</td><td>4</td><td>3</td><td>1</td><td>2</td><td>1</td><td>-</td><td>-</td><td>11</td></tr><tr><td>4</td><td>Large users</td><td>4</td><td>2</td><td>1</td><td>-</td><td>1</td><td>-</td><td>-</td><td>8</td></tr><tr><td>5</td><td>Environmentalists</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>-</td><td>-</td><td>6</td></tr><tr><td>6</td><td>Producers</td><td>2</td><td>2</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>5</td></tr><tr><td></td><td>Total</td><td>22</td><td>14</td><td>8</td><td>7</td><td>7</td><td>1</td><td>1</td><td>60</td></tr></table>

(MG – Minas Gerais, BA – Bahia, PE – Pernambuco, AL – Alagoas, SE – Sergipe, GO – Goiais, DF – Federal District of Brasilia and Government of Brazil).

The management plans are considered as decision alternatives with respect to the description below, appropriately named as ‘Balance,’ ‘Urban supply,’ and so on.

Plan 1 (Balance). High industrial developments are foreseen as well as intensive irrigation. Electric power production will increase by 20% after certain reconstructions of the existing hydroelectric objects and facilities. All users, including big users such as irrigation and hydroelectric production, will have approximately equal treatment. However, ecological and urban water requirements will receive top priority in water allocation.

Plan 2 (Urban supply). Urban supply will absolutely get an increased concern from the state agencies responsible for water management. It will be dominantly realized by means of reservoir management. Demographic movements from rural areas to cities and state capitals will continue with an actual increasing trend, but will be significantly decreased by the middle of the planning period. Irrigation will rise to only 50% of that amount estimated as maximum by the end of the period.

Plan 3 (Irrigation). Irrigation will have a dominant role with respect to the other water uses throughout the basin. Priority will be given to large irrigators (development at a level higher than 80% of the estimated maximum). No water payments are expected until 2010; only irrigation and industrial uses will be charged afterwards.

Plan 4 (Payment). Water payments will start progressively by 2007, with revisions of payment policy every 5 years (2012 and 2017). Pricing will be combined with an advanced system for obtaining the water rights. Other elements of the plan are the same as in Plan 3.

Plan 5 (Other users). This plan is a modification of Plan 1 in a way to force small irrigation users, tourism, eco-tourism and other small users (such as handmade manufacturers, ceramic industry). Intent is to enable that various users (other than large ones) will receive a higher priority by obtaining proper water rights and excluding payments; compensation for their uses of water will come from large consumers in irrigation, hydroelectric production and industry by proper pricing policy.

Table 3a  
Preferences of alternatives by interest groups obtained by standard AHP (SAHP)

<table><tr><td rowspan="2">Interest groups/ Alternatives</td><td>Balance</td><td>Urban supply</td><td>Irrigation</td><td>Payment</td><td>Other users</td></tr><tr><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td>IG1 Public authorities</td><td>0.312 (2)</td><td>0.379 (1)</td><td>0.099 (4)</td><td>0.143 (3)</td><td>0.066 (5)</td></tr><tr><td>IG2 Civil society</td><td>0.389 (1)</td><td>0.248 (2)</td><td>0.166 (3)</td><td>0.098 (5)</td><td>0.100 (4)</td></tr><tr><td>IG3 Small users</td><td>0.089 (4)</td><td>0.121 (3)</td><td>0.071 (5)</td><td>0.240 (2)</td><td>0.479 (1)</td></tr><tr><td>IG4 Large users</td><td>0.080 (5)</td><td>0.233 (2)</td><td>0.439 (1)</td><td>0.090 (4)</td><td>0.157 (3)</td></tr><tr><td>IG5 Environmentalists</td><td>0.433 (1)</td><td>0.246 (2)</td><td>0.045 (5)</td><td>0.097 (4)</td><td>0.179 (3)</td></tr><tr><td>IG6 Producers</td><td>0.388 (1)</td><td>0.087 (4)</td><td>0.303 (2)</td><td>0.065 (5)</td><td>0.157 (3)</td></tr></table>

## 5.3. Solution methodology

What follows is a simulated decision-making process within the WC to indicate how the proposed methodology can be implemented.

## 5.3.1. AHP application

First, each plan is briefly presented to the delegates at the WC meeting with a focus on the major indicators and facts related to the evaluation of alternative plans, the selection process, and the implications of the solution (decision) implementation. At the same meeting, a common hierarchy is agreed upon as described above. The WC then splits into subgroups identified as interest groups (IG). Each IG evaluates the same hierarchy of the problem by using the AHP methodology and verbal judgments only. For simplicity, each IG may be considered homogeneous in a sense that judgments are elicited by consensus and with the help of a facilitator.

After verbal judgments are gathered in all IG, the preference lists of alternative plans for both the standard and multiplicative versions of AHP were derived as presented in Tables 3a and 3b. Besides the relative importance weights of the plans, the numbers given in parentheses denote the ordinal plan preferences for each particular IG. Notice that for each AHP application, 60 judgments were necessary to elicit by each IG. The consistency criterion of 0.10 (applicable only for SAHP) is violated in only three cases from the total of 36 (six judgment matrices for each of the six IG). The overall consistency index for the IGs varied between 0.06 and 0.08.

The results of SAHP and MAHP show exactly the same ordinal preferences of all alternatives. The cardinal preferences are expectedly different, due to different scales used. These results are in full conformance with some other results presented earlier (see for example [22]). In fact, Tables 3a and 3b provide a useful checkup of two relatively distinct AHP methodologies for the same input information (elicited semantic judgments). In case of significant differences in the results obtained, additional consensus should be searched for, or one methodology selected in favor of another.

## 5.3.2. Aggregation in AHP context

In the case of SAHP, either the geometric mean method (GMM) or weighted average mean method (WAMM) may be used to aggregate individual (IG) priorities and compute the final priority weights for alternative management plans. However, only the GMM is applicable and in conformance with the MAHP methodology. The result of aggregation obtained by either method for SAHP, or by the geometric mean method for MAHP, may be considered as the final WC decision made in the group decision-making by the AHP context.

By assuming that all IG are of the same importance, the final cardinal and ordinal preferences of the management plans were obtained as shown in Table 4. Notice that in all three possible cases, the ordinal preferences of alternatives are the same: $A _ { 1 } { > } A _ { 2 } { > } A _ { 5 } { > } A _ { 3 } { > } A _ { 4 }$

Table 3b  
Preferences of alternatives by interest groups obtained by multiplicative AHP (MAHP)

<table><tr><td rowspan="2">Interest groups / Alternatives</td><td>Balance</td><td>Urban supply</td><td>Irrigation</td><td>Payment</td><td>Other users</td></tr><tr><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td>IG1 Public authorities</td><td>0.352 (2)</td><td>0.464 (1)</td><td>0.054 (4)</td><td>0.108 (3)</td><td>0.022 (5)</td></tr><tr><td>IG2 Civil society</td><td>0.505 (1)</td><td>0.264 (2)</td><td>0.135 (3)</td><td>0.025 (5)</td><td>0.071 (4)</td></tr><tr><td>IG3 Small users</td><td>0.025 (4)</td><td>0.043 (3)</td><td>0.016 (5)</td><td>0.141 (2)</td><td>0.774 (1)</td></tr><tr><td>IG4 Large users</td><td>0.032 (5)</td><td>0.202 (2)</td><td>0.599 (1)</td><td>0.049 (4)</td><td>0.119 (3)</td></tr><tr><td>IG5 Environmentalists</td><td>0.558 (1)</td><td>0.215 (2)</td><td>0.013 (5)</td><td>0.057 (4)</td><td>0.157 (3)</td></tr><tr><td>IG6 Producers</td><td>0.501 (1)</td><td>0.043 (4)</td><td>0.309 (2)</td><td>0.028 (5)</td><td>0.120 (3)</td></tr></table>

Final weights of the management plans in the AHP group decisionmaking context

<table><tr><td rowspan="2">Interest groups/Plans</td><td>Balance</td><td>Urban supply</td><td>Irrigation</td><td>Payment</td><td>Other users</td></tr><tr><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td>SAHP (WAMM)</td><td>0.282 (1)</td><td>0.219 (2)</td><td>0.187 (4)</td><td>0.122 (5)</td><td>0.190 (3)</td></tr><tr><td>SAHP (GMM)</td><td>0.276 (1)</td><td>0.236 (2)</td><td>0.166 (4)</td><td>0.134 (5)</td><td>0.187 (3)</td></tr><tr><td>MAHP (GMM)</td><td>0.315 (1)</td><td>0.250 (2)</td><td>0.138 (4)</td><td>0.095 (5)</td><td>0.202 (3)</td></tr></table>

In the multicriteria group decision-making context realized by the use of AHP only, the most desired is the Plan 1 (Balance), the second most desired is Plan 2 (Urban supply), and so on, down to the least desired Plan 4 (Payment). It is interesting to note that none of IG has obtained this order of alternative plans (cf. Tables 3a or 3b). In a consensus inspired ambient that should be preserved at the WC level, this final solution appears to be really a multicriteria and multi-interest compromise that goes along with the common efforts of the committee members in search for the best possible solution in the river basin.

## 5.3.3. Aggregation in SC context

The ordinal preference information extracted from the AHP application in IGs is used to simulate various voting procedures and see what outcome there should be if SC methods are applied at the final stage of the decision-making process in the WC. Various voting methods are applied to elect the ‘winning’ plan with the underlying assumption that only one representative from each IG can ‘objectively vote’ according to the ordinal preferences of the alternatives obtained by the use of AHP in a related IG. The ordinal preferences shown in Table 3a (the same with those in Table 3b), are rewritten in Table 5 and used in simulating the ‘election process’ by 5 voting methods. A logical extension is made to obtain a full ranking of plans for each voting method and to enable a comparison of the results within the AHP + SC context itself, but with the results obtained within a previous (AHP only) context as well.

Table 5  
Preference schedule of management plans (SC context)

<table><tr><td rowspan="2">Interest groups/Management plans</td><td>Balance</td><td>Urban supply</td><td>Irrigation</td><td>Payment</td><td>Other users</td></tr><tr><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td> $IG_1$  Public authorities</td><td>2</td><td>1</td><td>4</td><td>3</td><td>5</td></tr><tr><td> $IG_2$  Civil society</td><td>1</td><td>2</td><td>3</td><td>5</td><td>4</td></tr><tr><td> $IG_3$  Small users</td><td>4</td><td>3</td><td>5</td><td>2</td><td>1</td></tr><tr><td> $IG_4$  Large users</td><td>5</td><td>2</td><td>1</td><td>4</td><td>3</td></tr><tr><td> $IG_5$  Environmentalists</td><td>1</td><td>2</td><td>5</td><td>4</td><td>3</td></tr><tr><td> $IG_6$  Producers</td><td>1</td><td>4</td><td>2</td><td>5</td><td>3</td></tr></table>

Table 5a  
Rankings of the plans by IGs (after the plan A<sub>4</sub> is deleted)

<table><tr><td rowspan="2">Interest groups/Management plans</td><td>Balance</td><td>Urban supply</td><td>Irrigation</td><td>Other users</td></tr><tr><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_5$ </td></tr><tr><td>IG1 Public authorities</td><td>2</td><td>1</td><td>3</td><td>4</td></tr><tr><td>IG2 Civil society</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>IG3 Small users</td><td>3</td><td>2</td><td>4</td><td>1</td></tr><tr><td>IG4 Large users</td><td>4</td><td>2</td><td>1</td><td>3</td></tr><tr><td>IG5 Environmentalists</td><td>1</td><td>2</td><td>4</td><td>3</td></tr><tr><td>IG6 Producers</td><td>1</td><td>4</td><td>2</td><td>3</td></tr></table>

5.3.3.1. Plurality voting. For each plan, only the first places are considered as ‘voted’ by IGs. To apply Eq. (3) simply means to identify the number of first places in each column of Table 5:

$$
P _ {1} = 3, P _ {2} = 1, P _ {3} = 1, P _ {4} = 0, P _ {5} = 1.
$$

Since $P _ { 1 }$ is the largest, according to Eq. (4) the Balance is the winner (the WC choice). The complete ordering of plans is: $A _ { 1 } \succ A _ { 2 } = A _ { 3 } = A _ { 5 } \succ A _ { 4 }$

## 5.3.3.2. The Hare system (Plurality with elimination).

The alternatives are deleted one by one. Because the alternative $A _ { 4 }$ (Payment) is with a minimum number of the first place votes (Eq. (5)), it is deleted first. Due to Eq. (6), the initial Table 5 becomes Table 5a.

In the second step, any plan except Balance can be deleted arbitrarily because:

$$
P _ {1} ^ {\text { new }} = 3, P _ {2} ^ {\text { new }} = 1, P _ {3} ^ {\text { new }} = 1, P _ {5} ^ {\text { new }} = 1.
$$

Since there is a tie among the three plans, and Balance is the winner, the final ranking is: $A _ { 1 } \succ A _ { 2 } = A _ { 3 } = A _ { 5 } \succ A _ { 4 } ;$ recall that plan $A _ { 4 }$ (as the first deleted) is considered the worst.

5.3.3.3. The Borda count. In this case, $M { = } 6$ and N=5. By applying Eq. (8) to the ranks given in Table 5 one obtains

$$
Q _ {1} = 2 4 - (2 + 1 + 4 + 5 + 1 + 1) = 2 4 - 1 4 = 1 2
$$

$$
Q _ {2} = 2 4 - (1 + 2 + 3 + 2 + 2 + 4) = 2 4 - 1 4 = 1 2
$$

$$
Q _ {3} = 2 4 - (4 + 3 + 5 + 1 + 5 + 2) = 2 4 - 2 0 = 4
$$

$$
Q _ {4} = 2 4 - (3 + 5 + 2 + 4 + 4 + 5) = 2 4 - 2 3 = 1
$$

$$
Q _ {5} = 2 4 - (5 + 4 + 1 + 3 + 3 + 3) = 2 4 - 1 9 = 5
$$

Because Balance and Urban supply are tied, they are the WC choices. The complete ranking is: $A _ { 1 } { = } A _ { 2 } { > } A _ { 5 } { > }$ $A _ { 3 } \succ A _ { 4 }$

5.3.3.4. Pairwise comparisons voting. To identify the winner, plans are compared head-to-head. By scoring these match-ups (1 pt. for a win, 0.5 pts. for a tie), Table 6 is obtained.

A direct match-up gives the following total of points: Balance – 3.5, Urban supply – 3.5, Irrigation – 1.5, Payment – 0.5, and Other users – 1. Notice that among the 5 plans, only Balance and Urban Supply are preferred overall by the three other plans; consequently, they are both considered as the WC choice. The final ranking is: $A _ { 1 } { = } A _ { 2 } { > } A _ { 3 } { > } A _ { 5 } { > } A _ { 4 }$

5.3.3.5. Approval voting. To apply this method, first the value of $\cdot _ { p }$ had to be specified. For $p { = } 2 ,$ only plans ranked as the first and as the second received one vote due to Eq. (10); the others receive zero votes. Table 5 transforms into Table 7:

The addition of votes by columns (Eq. (11)) gives:

$$
V _ {1} = 4, V _ {2} = 4, V _ {3} = 2, V _ {4} = 1, V _ {5} = 1.
$$

Since $V _ { 1 }$ and $V _ { 2 }$ are the largest, there is a tie and both Balance and Urban supply are the WC choice (Eq. (12)). The complete ordering by this method is therefore: $A _ { 1 } { = } A _ { 2 } { > } A _ { 3 } { > } A _ { 4 } { = } A _ { 5 }$

The final ordering of water management plans for various combinations of AHP and voting methods within two general frameworks (AHP only, and AHP+ SC) is summarized in Table 8. The most preferred by all methods is the management plan $A _ { 1 }$ denoted as Balance. It may be declared as the optimal group decision in the multicriteria decision-making sense, since the first methodology is used based exclusively on a standard and multiplicative version of the AHP and a mathematical aggregation of the final priorities. The same plan is the declared winner in a group decision context based on the combined use of the AHP and SC methods. When the AHP results are used as inputs to various voting methods, for plurality and Hare

Table 6  
Points received in head-to-head comparison

<table><tr><td> $j_{1}/j_{2}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>-</td><td>0.5</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>0.5</td><td>-</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>0</td><td>0</td><td>-</td><td>0.5</td><td>1</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0.5</td><td>-</td><td>0</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>-</td></tr></table>

Table 7  
Approval voting for $p { = } 2$

<table><tr><td rowspan="2">Interest groups/Management plans</td><td>Balance</td><td>Urban supply</td><td>Irrigation</td><td>Payment</td><td>Other users</td></tr><tr><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td></tr><tr><td>IG1 Public authorities</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IG2 Civil society</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IG3 Small users</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>IG4 Large users</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>IG5 Environmentalists</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>IG6 Producers</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr></table>

Balance is the absolute winner; it is tied with the second most preferred plan Urban supply for Borda, Pairwise and Approval. Furthermore, Urban supply is tied with the second position with Irrigation and Other users for the Plurality and Hare. The least desired plan is Payment that is ranked last by all methods except Approval where there is a tie with Other users in the 4-th and 5-th positions.

When the first (AHP only) methodology is applied, the rankings of management plans in Table 8 indicate an absolute agreement of the results for SAHP and MAHP, whatever group aggregation is used. Notice that the cardinal preferences (presented in Table 3a and 3b) were directly integrated (without any voting!), so the best alternative is identified exactly as well as the ordering of the other alternatives. A possibility of ties of alternatives, like in voting procedures, is obviously very small.

When the second (AHP + SC) methodology is applied, different voting procedures give a different ordering of the alternatives. However, the same winner is always declared, or at maximum, is tied with the second best alternative. Ties generally appear if the problem environment is inadequate for applying SC methods, such as a case when the number of voters is small, or the number of alternatives is big; the worst case obviously being a combination of these two. The other reason for possible ties is inherent to the voting methods themselves. Namely, some of the methods use only partial information (e.g. plurality voting), or do not use all the available information at one time (e.g. the Hare system). The results obtained in this case example are logical and in a particular way offer additional possibilities for the Water Committee — to use tied alternative plans and continue their evaluation in next phases of the decision process.

Table 8  
Final rankings obtained by the two methodologie

<table><tr><td rowspan="2">Methodologies</td><td>Balance</td><td>Urban supply</td><td>Irrigation</td><td>Payment</td><td>Other users</td></tr><tr><td> $A_{1}$ </td><td> $A_{2}$ </td><td> $A_{3}$ </td><td> $A_{4}$ </td><td> $A_{5}$ </td></tr><tr><td colspan="6">1. AHP</td></tr><tr><td>Standard AHP with WAMM</td><td>1</td><td>2</td><td>4</td><td>5</td><td>3</td></tr><tr><td>Standard AHP with GMM</td><td>1</td><td>2</td><td>4</td><td>5</td><td>3</td></tr><tr><td>Multiplicative AHP with GMM</td><td>1</td><td>2</td><td>4</td><td>5</td><td>3</td></tr><tr><td colspan="6">2. AHP+SC</td></tr><tr><td>Plurality</td><td>1</td><td>2–4</td><td>2–4</td><td>5</td><td>2–4</td></tr><tr><td>Hare</td><td>1</td><td>2–4</td><td>2–4</td><td>5</td><td>2–4</td></tr><tr><td>Borda</td><td>1–2</td><td>1–2</td><td>4</td><td>5</td><td>3</td></tr><tr><td>Pairwise</td><td>1–2</td><td>1–2</td><td>3</td><td>5</td><td>4</td></tr><tr><td>Approval</td><td>1–2</td><td>1–2</td><td>3</td><td>4–5</td><td>4–5</td></tr></table>

## 6. Discussion and conclusion

Good agreement of the final results obtained by two different approaches in group preference aggregations leads to a conclusion that either can be chosen by groups such as in the example of the WC. By employing the methodology based on AHP only (the MCDM context), it is possible to control and preserve the consistency of the decision-making process, but in fact the process excludes members of the WC, or representatives of IGs, from the real decision-making in the final stage of the process. The final decision is simply derived by mathematical aggregation. If a combination of MCDM and SC is implemented (the MCDM+SC context), during the SC phase (voting) important cardinal preference information obtained by AHP is not used, and only permutations of integer numbers are manipulated. Reduced information may lead to different outcomes for different voting methods, ties of alternatives etc. However, the compensation for this drawback is that there is a good chance (as shown here) that the goal will be achieved, and at least the best alternative will be recognized and posted to the first position in a list. Also important is that voting may not necessarily be virtual (simulated); it can be really performed thus giving a chance to IGs and their representatives to expose their choices in a more explicit and democratic way.

Our belief is that the second approach (AHP + SC, with either SAHP or MAHP and with either voting technique) has more potential and flexibility. Better chances for adaptation in real life decision-making we see in cases when water committees or similar decisionmaking bodies anticipate the importance of decentralization and occasionally split into subgroups to preserve the homogeneity and overall consistency of the decision process, as well as assuring that the fundamental axioms of fairness and thrust will not be violated.

## Acknowledgments

The author wish to thank FEP – Fundação de Escola Politecnica da UFBA and FAPESB – Fundação de Amparo á Pesquisa do Estado da Bahia (Brazil) for the partial support of this research.

## References

[1] N. Bolloju, Aggregation of analytic hierarchy process models based on similarities in decision makers' preferences, European Journal of Operational Research 128 (2001).

[2] S.T. Brams, P. Fishburn, Approval Voting, Birkhauser, Boston, 1983.

[3] N. Bryson, A. Joseph, Generating consensus priority point vectors: a logarithmic goal programming approach, Computers & Operations Research 26 (1999).

[4] W.D. Cook, M. Kress, L.M. Seiford, A general framework for distance-based consensus in ordinal ranking models, European Journal of Operational Research 96 (1996).

[5] L.F. Cranor, Declared-strategy voting: an instrument for group decision-making (Washington University, dissertation, 1996).

[6] A. Cwolka, M.G. Raith, Group preference aggregation with AHP — implications for multiple-issue agendas, European Journal of Operational Research 132 (2001).

[7] A. d'Angelo, A. Eskandari, F. Szidarovszky, Social choice procedures in water resources management, Journal of Environ mental Management 52 (1998).

[8] E. Forman, K. Peniwati, Aggregating individual judgments and priorities with the analytic hierarchy process, European Journal of Operational Research 108 (1998).

[9] N.M. Fraser, J.W. Hauge, Multicriteria approval: application of approval voting concepts to MCDM problems, Journal of Multi-Criteria Decision Analysis 7 (1998).

[10] J. Kangas, A. Kangas, Multiple criteria decision support methods in forest management: an overview and comparative analyses, Multi-Objective Forest Planning, Managing Forest Ecosystems, vol. 6, Kluwer Academic Publishers, 2002.

[11] J. Kangas, A. Kangas, Multicriteria approval and SMAA-O in natural resources decision analysis with both ordinal and cardinal criteria, Journal of Multi-Criteria Decision Analysis 12 (2003).

[12] S. Kant, S. Lee, A social choice approach to sustainable forest management: an analysis of multiple forest values in Northwestern Ontario, Forest Policy and Economics 6 (2004).

[13] J.S. Kelly, Social Choice Theory. An Introduction, Springer Verlag, New York, 1988.

[14] E. Lakeman, How Democracies Vote: A Study of Electoral Systems, 4th Edition, Faber & Faber, London, 1974.

[15] S. Laukkanen, A. Kangas, J. Kangas, Applying voting theory in natural resource management: a case of multiple-criteria group decision support, Journal of Environmental Management 64 (2002).

[16] S. Laukkanen, T. Palander, J. Kangas, Applying voting theory in participatory decision support for sustainable timber harvesting, Canadian Journal of Forest Research 34 (2004).

[17] F.A. Lootsma, H. Schuijt, The multiplicative AHP, SMART, and ELECTRE in a common context, Journal of Multi-Criteria Decision Analysis 6 (1997).

[18] W.E. Martin, D.J. Schields, B. Tolwinski, B. Kent, An application of social choice theory to U.S.D.A. Forest Service decision making, Journal of Policy Modeling 18 (1996).

[19] P.A. McNut, The Economics of Public Choice, Edward Elgar, UK, 1996.

[20] L. Mikhailov, Group prioritization in the AHP by fuzzy preference programming method, Computers & Operations Research 31 (2004).

[21] J. Mustajoki, R. Hämäläinen, Web-HIPRE: global decision support by value tree and AHP analysis, INFOR 31 (2000).

[22] D.L. Olson, G. Fliedner, K. Currie, Comparison of the REMBRANDT system with analytic hierarchy process, European Journal of Operational Research 82 (1995).

[23] R. Ramanathan, A note on the use of the analytic hierarchy process for environmental impact assessment, Journal of Environmental Management 63 (2001).

[24] R. Ramanathan, L.S. Ganesh, Group preference aggregating methods employed in AHP: an evaluation and intrinsic process for deriving members' weightages, European Journal of Operational Research 79 (1994).

[25] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[26] D.J. Shields, B. Tolwinski, B.M. Kent, Models for conflict resolution in ecosystem management, Socio-Economic Planning Sciences 33 (1999).

[27] A.D. Taylor, Mathematics and Politics, Springer Verlag, New York, 1995.

[28] S. Zahir, Clusters in a group: decision making in the vector space formulation of the analytic hierarchy process, European Journa of Operational Research 112 (1999).

![](/api/attachments/EVC3UJAQ/fulltext/images/9d2ba6790114649a5c9aa4cfa64f88ead7eee6502eb244370f1759784d896d98.jpg)

Bojan Srdjevic is a Professor in the Faculty of Agriculture at University of Novi Sad, Serbia. He is also a Visiting Professor at the School of Polytechnic, Federal University of Bahia (UFBA), Salvador, Brazil, and a Guest Professor at the University of Stuttgart in Germany. He received the PhD degree in technical science from the University of Novi Sad (1987), and the MS (1984) and BS degree (1974), both in electrical engineering, from the

University of Belgrade in Serbia. His research interests include multiple criteria decision analysis, decision-making under uncertainty, and decision support systems in natural resources management. He has published in Elsevier's Computers and Operations Research and Springer's Water Resources Management, among others.
