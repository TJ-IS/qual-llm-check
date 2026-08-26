---
otero_id: 17628
otero_key: "38GCZP6B"
title: "JUDGES: A descriptive group decision support system for the ranking of items"
authors: "Gérard Colson; Bertrand Mareschal"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90055-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# JUDGES: A descriptive group decision support system for the ranking of items

Gérard Colson $^{a}$ and Bertrand Mareschal $^{b}$

$^{a}$ Université de Liège, Faculté d'Economie, de Gestion et de Sciences Sociales, Bât. B31 - Bte 50, B - 4000 Liège, Belgium $^{b}$ Université Libre de Bruxelles, Institut de Statistique, Boulevard du Triomphe - CP 210, B - 1050 Bruxelles, Belgium

A set of tools for group decision support are presented. Decision problems involving several decision makers, hereafter called judges, that have to rank several alternatives, are considered. The toolbox is called JUDGES. It includes the four following procedures:

\- a hierarchical representation of the judges allows to display the existing conflicts between groups of judges,

\- enhanced box-plots representations of the alternatives are generated in order to detect those that are responsible for the major conflicts,

\- specific advice is issued to each judge in order to reach more easily a consensus,

\- a general framework for a pairwise group preference structure is proposed, and can be used to finalise the decision.

These procedures are embedded in an interactive software, implemented on micro-computer, which currently simulates the use on a network. Actual network implementation is foreseen in the near future. Several applications are presented and future developments are discussed.

Keywords: Group decision; Ranking; Decision support; Multicriteria decision making

## 0. Introduction

Group decision support is not a trivial subject, as pointed out recently by C. Eden and J. Radford (see [8]). Numerous references about group decision problems and support systems are available in the literature (see [6,8,11]). In his paper 'Complexity and strategic decision-making', J. Churchill observes that groups of decision mak-

![](/api/attachments/38GCZP6B/fulltext/images/2dcce41f35ee88a7730c6ab3ccedc1750d3df68253ee4b36a1d48180113ccbdb.jpg)

Gérard Colson is Professor of Microeconomics and Decision Analysis at 'Hautes etudes Commerciales' in Liège (Belgium), where he has been President of the Economic Department. He also teaches Management Science and Decision Aid at the Business School of the University of Liège. He is engineer and received a B.S. in Economics and a Ph.D. in Management Science, all from the University of Liège. His current research interests are multicriteria decision aid,

portfolio management, decision and information theory, risk management. He is co-author of two books: Models and Methods in Multiple Criteria Decision Making (Pergamon, 1989), and Uncertain Prospects Ranking and Portfolio Analysis under the Conditions of Partial Information (Verlag Anton Hain, 1980). His articles have appeared in Computers and Operations Research, European Journal of Operational Research, Mathematical Modelling, Belgian Journal of Operations Research, Foundations of Control Engineering, Gestion 2000. Several times, he has been Guest editor.

![](/api/attachments/38GCZP6B/fulltext/images/f52e6ee69d8320c90ade3261e1e5dcdd0ed8d939a101508a5d89e23d3de17467.jpg)

Bertrand Mareschal is Assistant at the Solvay Business School of the Université Libre de Bruxelles (Brussels, Belgium) where he teaches statistics and operational research. He graduated in Mathematics in 1983, in Actuarial Science in 1986 and received a Ph.D. in 1989, all from the Université Libre de Bruxelles. His current research interests include multiple criteria and group decision aid, decision support systems and the use of quantitative methods in fi nance. He has published papers in European Journal of Operational Research, Journal of the Royal Statistical Society, Mathematical and Computer Modelling, INFOR, Actualité Economique, Cahiers du C.E.R.O., Revue de la Banque.

ers, confronted to complex decisions, are often simply confused about the situation they face and that they don't necessarily want support to resolve the situation but rather to give clarity and focus to the issues they face. Hence the need for efficient Group Decision Support Systems, which can be achieved by the development of simple visual aids to the discussion and negotiation about collective preferences. This is the major objective of the present paper.

Forthcoming developments will include the multiple criteria aspect of most decision problems which has to be considered in the collective decision context as well as in the individual decision context. This latter development will be a natural extension of the ever growing MCDM literature. Indeed, methods and applications of multiple objective and multiattribute decision making have been widely studied according to several approaches (see among others $[1,4,12,14,16,17]$ ).

On the other hand, the social choice theory has produced numerous studies on voting procedures, social choice functions and social welfare (see $[9,7]$ and $[10]$ p. 6 for a short typology).

Both domains still remain far from each other in the literature, although usually practical decision problems request a multiple criteria approach and lead to discussions by a small team of decision makers. Until now, few authors $[2,10]$ have tackled the multiple criteria multiple judge decision problem.

Our intention is to contribute to this research area by presenting a set of two papers:

(1) This first one will supply the group of decision makers with a toolbox to help them in the ranking of items (candidates, projects, ...). Each decision maker, called a judge, can supply an individual ranking of these items, which may result from the application of his own criteria and multiple criteria method.

(2) The second paper, forthcoming, will describe another toolbox which deals with the multiple criteria oriented tasks of the different judges, and which also provides various social choice functions (Borda, Condorcet, ...) or algorithms (prudent orders, ...) for tackling the multijudge final treatment of the individual multiple criteria preferences (see [5]).

Each paper is associated to an interactive microcomputer software (JUDGES for the first, ARGOS for the second). These programs are available from the authors and are foreseen to be used for decision conferencing through a network.

Both studies follow a path close to the one also borrowed independently by T. Bui (see [2]). Indeed, three conditions have been stated for the development of the software, which form a set of behavioral hypotheses:

(i) The decision setting and the group behavior is cooperative. Although negotiations can take place in the discussion, there is no personal research of power, no trickery or strategy to obtain a final personal ranking. Accordingly, there is no intentional misrepresentation of data or preferences.

(ii) Decisions are made in a distributed and democratic or business-like fashion. Each decision maker should have an individual workstation (PC) at his disposal, connected to others via a network. There is no group leader. The arbitration among different opinions is facilitated by the system itself. Visual aids are provided for discussing the decision rules of the group: the pairwise comparison of the items can lead to a strong or weak preference, an indifference or a conflict among the individual opinions.

(iii) Multiple criteria decision making will be the kernel of the whole system and a basis for the exchange of information among the decision makers. This last point mainly concerns the second paper and the ARGOS software and is not developed here.

This first paper introduces a new descriptive Group Decision Support System for the ranking of items. This new GDSS is a descriptive tool since it doesn't pretend to impose any normative behavior to the group. It only offers, at this stage of development, four Group (Visual) Decision Aids (GDAs). GDA1 addresses the first problem of detecting similar or dissimilar opinions via a clustering of the individual rankings. GDA2 describes more deeply the distribution of the various opinions through box-plots. GDA3 analyses the structure of these box-plots in order to provide the judges with advice in view of a consensus. GDA4 is a visual aid for defining and simulating various sets of rules for collective preferences (strong or weak preference, non preference, indifference or conflict).

Section 1 of this paper describes the JUDGES group decision aid framework. The fourth GDA has required to develop an original system of collective pairwise preference relations (including a new conflict measure) which is presented in Section 2. This new relational system of preferences is a multi-judge extension of classical results (see [13,15]). Section 3 illustrates through a simple example the GDAs included in the JUDGES toolbox, and Section 4 is devoted to a real-world application of JUDGES to the research of a consensual ranking of common stocks by an investment committee.

## 1. The JUDGES group decision aid framework

## 1.1. Purposes of the design

The JUDGES system is designed in order to support group decision making in the following framework: a group of 3 to 20 persons (experts, members of a committee, ...), hereafter called judges, tries to reach consensus on the ranking of several items (projects, candidates, ...) on the basis of a discussion. The discussion is enlightened by several group decision visual aids. The objectives of the group can be various:

(i) the judges desire to achieve a consensus on a partial or complete collective ranking of the items;

(ii) they want to point out the disagreements between themselves and to form clusters of similar judgments;

(iii) they intend to simulate voting procedures according to various sets of group ranking rules.

## 1.2. Hypotheses of behavior

The judges are assumed to be cooperative in the sense that each one really wants to avoid any trickery or strategic calculation during the session of their fair research for their collective complete or partial ranking. They honestly try the consensus on the ranking, but without forcing any judge to modify his opinion.

## 1.3. Basic data

Let us consider J judges and I items to be ranked. The set of the judges is denoted by J and the set of items by A. The basic data are the following:

\- Each judge must provide a complete preorder (ranking with possible ties) of the $I$ items. Alternatively the judge may supply a richer information by valuing each item on an interval scale. However this additional information will not be used directly by the system. Let us denote with $r_{ij}$ the rank given to the item $i$ by the judge $j$ . A complete individual preference structure $(P_j, I_j)$ is constructed on $A \times A$ in the following way: for each pair of items $(a, b)$ , $aP_jb$ ( $a$ is preferred to $b$ ) iff $r_{aj} < r_{bj}$ and $aI_jb$ iff $r_{aj} = r_{bj}$ .

\- The decisional power of the judges must be precised by the attribution of numerical weights, according to one of the two most frequently encountered problematics:

(i) The weighted case: in a business context, unequal decisional powers are often allocated to the judges. Let $W_{j}$ be the number of unitary votes allocated to the judge j and W the total number of votes, hence the relative decisional power $w_{j}$ of this judge could be considered as her relative influence in the group. We have the obvious relationships:

$$
w _ {j} = \frac {W _ {j}}{W}, \quad \text { with } \quad W = \sum_ {j = 1} ^ {J} W _ {j},\tag{1}
$$

$$
\sum_ {j = 1} ^ {J} w _ {j} = 1.\tag{2}
$$

(ii) The democratic case: in this case equal decisional powers are allocated. Therefore, $W_{j} = 1$ for $j = 1, \ldots, J$ . It is of course a special case of the previous case.

It has to be noted that these basic data will generate a purely ordinal method.

The judges and items are not limited to small numbers except for technical reasons depending on the actual implementation of the system (memory size, readability of the displays, ...).

Another possible limitation is the quickly increasing number of pairwise comparisons of the items with their number.

## 2. A pairwise group preference relations system (P, I, C, NP, Q, U, R)

This section is devoted to the definition of a system of seven pairwise group preference relations. This system is one of the basic visual aids of JUDGES.

Let us consider a pair of items $(a, b)$ and a group of judges $g \subseteq J$ . We introduce the following notations:

$$
\begin{array}{l} J ^ {+} (a, b) = \sum_ {j \in J _ {a b} ^ {+}} W _ {j}, \\ \text {where} \quad J _ {a b} ^ {+} = \left\{j \in \mathsf {J} \quad \text {s.t.} \quad a P _ {j} b \right\}, \\ J ^ {-} (a, b) = \sum_ {j \in J _ {a b} ^ {-}} W _ {j}, \\ \text {where} \quad J _ {a b} ^ {-} = \left\{j \in \mathsf {J} \quad \text {s.t.} \quad b P _ {j} a \right\}, \\ J ^ {e} (a, b) = \sum_ {j \in J _ {a b} ^ {e}} W _ {j}, \\ \text {where} J _ {a b} ^ {e} = \left\{j \in \mathsf {J} \text {s.t.} a I _ {j} b \right\}, \end{array}\tag{3a}
$$

(3b)

(3c)

with the properties:

$$
J ^ {-} (a, b) = J ^ {+} (b, a)
$$

and

$$
J ^ {+} (a, b) + J ^ {-} (a, b) + J ^ {e} (a, b) = W.\tag{4}
$$

$J^{+}(a,b), J^{-}(a,b)$ and $J^{e}(a,b)$ are the respective numbers of unitary votes in favor of the collective group $g$ 's assesments $aP_{g}b, bP_{g}a$ and $aI_{g}b$ . In the democratic case, they represent the numbers of judges $j$ for which the respective statements $aP_{j}b, bP_{j}a$ and $aI_{j}b$ are expressed.

The corresponding relative values, which are the proportions of votes in the group g, are easily obtained:

$$
j ^ {+} (a, b) = \frac {J ^ {+} (a , b)}{W} = \sum_ {j \in J _ {a b} ^ {+}} w _ {j},\tag{5a}
$$

![](/api/attachments/38GCZP6B/fulltext/images/5787d84f33f9b6795859e607b36054a7c4a3d7132ea6246fad72743231224fef.jpg)  
Fig. 1. Triangular display.

$$
j ^ {-} (a, b) = \frac {J ^ {-} (a , b)}{W} = \sum_ {j \in J _ {a b} ^ {-}} w _ {j},\tag{5b}
$$

$$
j ^ {e} (a, b) = \frac {J ^ {e} (a , b)}{W} = \sum_ {j \in J _ {a b} ^ {e}} w _ {j},\tag{5c}
$$

with:

$$
j ^ {+} (a, b) + j ^ {-} (a, b) + j ^ {e} (a, b) = 1.\tag{6}
$$

Given the abovementioned definitions and properties, the comparison of a and b can be represented in a triangular display which will be used by the group to explore the voting procedures related to the pairwise comparison of items (see Fig. 1). Each point of this triangle corresponds to a particular distribution of proportions of votes. The vertices A, B and 0 represent the unanimity positions of the group g, respectively for $aP_{j}b$ , $bP_{j}a$ and $aI_{j}b$ . The dotted line (see Fig. 3) is the locus of the equality of preference votes, with M being the special case where all votes express preferences.

Given some voting rules, it is possible to define several areas in the triangular display. Each area delimits the set of distributions of votes that leads to a unique collective preference assessment.

## 2.1. Definition of the preference relations

Let us first define some important preference situations for a group g and a fixed set of voting rules.

(1) Collective strong preference $P_{g}$

To achieve a collective strong preference of a over b, it seems very common that the two following rules should be verified:

(i) Absolute majority rule: A proportion of votes greater than a threshold $j^{+*}$ must be expressed in favor of the statement $aP_{g}b$ :

$$
a P _ {g} b \Rightarrow j ^ {+} (a, b) > j ^ {+ *} \geq 0. 5.\tag{7a}
$$

Alternatively a relative majority rule can also be considered which is related to expressed preferences only:

$$
a P _ {g} b \Rightarrow j ^ {+} (a, b) > j ^ {+ *} \left(1 - j ^ {e} (a, b)\right).\tag{7b}
$$

These majority rules are simple for $j^{+*}=0.5$ , otherwise they are qualified majority rules.

(ii) Weak opposition rule: The opposition (votes in favor of $bP_{g}a$ ) must not exceed the proportion of votes $j^{-*}$ :

$$
a P _ {g} b \Rightarrow j ^ {-} (a, b) \leq j ^ {- *}.\tag{7c}
$$

The combination of these two rules define necessary and sufficient conditions for the collective strong preference $a P_{g} b$ .

(2) Collective strict indifference $I_g$

The combination of the three following rules is considered for collective strict indifference:

(i) Sufficiency rule: A sufficient proportion of votes $j^{e*}$ must be expressed in favor of the statement $a I_{g} b$ :

$$
a I _ {g} b \Rightarrow j ^ {e} (a, b) \geq j ^ {e ^ {*}}.\tag{8a}
$$

(ii) Weak discrepancy rule: A sufficient equilibrium between the proportions of votes expressing preferences in favor of a and in favor of b must exist. Given the maximum allowable discrepancy $d^{*}$ , it is equivalent to:

$$
a I _ {g} b \Rightarrow | j ^ {+} (a, b) - j ^ {-} (a, b) | \leq d ^ {*}.\tag{8b}
$$

(iii) Maximum preference rule: The maximum proportion of votes in favor of one item must not exceed $p^{*}$ :

$$
a I _ {g} b \Rightarrow \operatorname{Max} \left\{j ^ {+} (a, b), j ^ {-} (a, b) \right\} \leq p ^ {*}.\tag{8c}
$$

A majority rule can also be added in this case:

$$
a I _ {g} b \Rightarrow j ^ {e} (a, b) > 0. 5.\tag{8d}
$$

(3) Collective conflict $C_g$

Before defining the rules for the conflict relation, we introduce several new concepts.

\- An absolute maximal conflict between the judges about a pair ranking exists when all the votes are strict preferences and when the opponent prefers have an equal decisional power:

$$
j ^ {+} (a, b) = j ^ {-} (a, b) = 0. 5.\tag{9a}
$$

\- A relative maximal conflict exists when the previous intensity of conflict is reduced by the presence of several ties. Since therefore $j^{e}(a, b) > 0$ , the condition becomes:

$$
j ^ {+} (a, b) = j ^ {-} (a, b) <   0. 5.\tag{9b}
$$

\- The conflict is null if there are no opponent preferrers, i.e.

$$
j ^ {+} (a, b) \cdot j ^ {-} (a, b) = 0.\tag{9c}
$$

\- A usual measure of conflict intensity is the ratio of opponents to proponents for a given preference. If we consider the case of a majority expressed in favor of $aP_g b$ for instance, this ratio is:

$$
\frac {j ^ {-} (a , b)}{j ^ {+} (a , b)}.\tag{9d}
$$

\- To insure the symmetry and to avoid indetermination of the measure, the following ratio of opposition is defined:

$$
\gamma (a, b) = \left\{ \begin{array}{l} \min \{\gamma^ {+} (a, b); \gamma^ {-} (a, b) \} \\ \text {if} j ^ {e} (a, b) \neq 1, \\ 0 \quad \text {otherwise.} \end{array} \right.\tag{9d'}
$$

where:

$$
\gamma^ {+} (a, b) = \left\{ \begin{array}{l l} \frac {j ^ {-} (a , b)}{j ^ {+} (a , b)} & \text {if} \quad j ^ {+} (a, b) > 0, \\ W & \text {if} \quad j ^ {+} (a, b) = 0. \end{array} \right.\tag{9e}
$$

$(\gamma^{-}(a,b)$ is obtained in a similar way.)

\- The reduction of conflict intensity due to the ties is taken into account by multiplying $\gamma(a,b)$ by the proportion of expressed preferences:

$$
\beta (a, b) = \gamma (a, b) \cdot (1 - j ^ {e} (a, b))\tag{9f}
$$

This final formula is our measure of conflict intensity. Given an allowable conflict intensity $\beta^{*}$ , we obtain the following condition:

$$
a C _ {g} b \Leftrightarrow \beta (a, b) > \beta^ {*}.\tag{9g}
$$

Let us note that the only value to be assessed by the group is not $\beta^{*}$ but $\gamma^{*}$ , the allowable ratio for opposition in the absence of ties (since they are unknown at the moment of the assesment). Therefore $\beta^{*}$ should be interpreted either:

(i) as the highest allowable absolute conflict intensity, i.e. $\beta^{*} = \gamma^{*}$ when $j^{e}(a,b) = 0$ ; or

(ii) as the highest allowable relative number of expressed preferences $(1 - j^{\mathrm{e}})^{*}$ , for a maximal relative conflict, i.e. $\beta^{*} = (1 - j^{e}(a,b))^{*}$ when $\gamma (a,b) = 1$ .

(4) Collective non-preference $NP_g$

The definition of the sure collective non-preference $NP_{g}$ depends on the behavioral hypothesis made on the set of individual preferences. Let us consider two exclusive cases.

\- Hypothesis 1 (H1): All individual indifferences are true ones.

In this case a simple relative majority in favor of $aP_g b$ is a necessary condition for $bNP_g a$ :

$$
b N P _ {g} a \Rightarrow \gamma^ {+} (a, b) > 1.\tag{10a}
$$

The following necessary and sufficient conditions are then obtained by excluding the collective indifference and conflict between a and b:

$$
b N P _ {g} a \Leftrightarrow \left\{ \begin{array}{l} \gamma^ {+} (a, b) > 1 \\ \text { and } \\ a   \mathcal {C} _ {g}   b \quad \text { and } \quad a   I _ {g}   b \end{array} \right.\tag{10b}
$$

\- Hypothesis 2 (H2): Some of the individual indifferences are issued from a hesitation in the ranking. In this case prudence requires to assume a possible complete indetermination of these indifferences. The relative majority condition (10a) is then replaced by an absolute majority rule and the necessary and sufficient conditions become:

$$
b N P _ {g} a \Leftrightarrow \left\{ \begin{array}{l} j ^ {+} (a, b) > 0. 5 \\ \text { and } \\ a \not C _ {g} b \quad \text { and } \quad a I _ {g} b \end{array} \right.\tag{10c}
$$

Indeed the absolute majority rule is equivalent to:

$$
j ^ {+} (a, b) > j ^ {-} (a, b) + j ^ {e} (a, b),\tag{10d}
$$

where $j^{e}(a,b)$ could be considered as representing also a possible opposition.

(5) Collective weak preference $Q_g$

The collective weak preference relation is obtained as the difference between the collective non-preference and the collective preference:

$$
a Q _ {g} b \Leftrightarrow \left\{ \begin{array}{l} b N P _ {g} a \\ \text { and } \\ a P _ {g} b \end{array} \right.\tag{11a}
$$

Under the majority rules introduced for $P_{g}$ , the following consistency property holds:

$$
a P _ {g} b \Rightarrow b N P _ {g} a.\tag{11b}
$$

(6) Collective unclassified relation $U_{g}$

This unclassified relation is the residual relation between a pair $(a,b)$ when no other defined binary relation exists for that pair.

(7) Collective refusal relation $R_g$

The collective refusal relation $R_{g}$ is defined as the union of $C_{g}$ and $U_{g}$ . Indeed it is not possible for group g to attain a collective ranking when a conflictual or a unclassified situation arises.

## 2.2. Consistency and graphical representation of the preference relations system

Given the collective preference relations, seven disjoint areas (corresponding to $P_{g}$ , $I_{g}$ , $C_{g}$ , $Q_{g}$ and $U_{g}$ ) are obtained in the triangular display already presented in Fig. 1. Additional areas (corresponding to $NP_{g}$ and $R_{g}$ ) can be derived from these basic areas.

Fig. 2, 3 and 4 show these basic areas for three particular majority rules. To avoid inconsistencies, a priority order has to be defined on the preference relations. In this paper, we have assumed the following priorities:

$$
C _ {g} \rightarrow I _ {g} \rightarrow P _ {g}, N P _ {g}, Q _ {g} \rightarrow U _ {g}, R _ {g}\tag{12a}
$$

Let us remark that consistency requires that under the hypothesis H2 (some indifferences are actually hesitations) for the collective non-preference the absolute majority rule must be adopted by the group for both non-preference and preference. This case is presented in Fig. 3.

![](/api/attachments/38GCZP6B/fulltext/images/778033feb976a8f2062fe3e2d00f4f3e27195c5cdf985274357faff8711c0247.jpg)  
Fig. 2. Basic areas for relative majority rules.

• Fig. 2: Relative majority rules.

The relative majority rule (7b) is used. It can be shown that this is equivalent to the following condition:

$$
a P _ {g} b \Rightarrow \gamma^ {+} (a, b) > \gamma^ {*} = \frac {j ^ {+ ^ {*}}}{1 - j ^ {+ ^ {*}}}\tag{12b}
$$

In this case, the opposition rule is redundant and does not appear on the figure. As previously stated, the conflict $(C_{g})$ and indifference $(I_{g})$ areas are computed first. The priority of $I_{g}$ over $P_{g}$ appears readily in Fig. 2, as it will be always in this particular case. Depending on the actual values of the parameters, the $U_{g}$ area can be either empty or a segment of the $45^{\circ}$ line. This case presents some similarities with the normalized preference intensity plot of the ORESTE multicriteria method (see [12], p. 1263).

![](/api/attachments/38GCZP6B/fulltext/images/640d6aa63e0c0b9435631780490932344e60956a101f90d433cc7b07bc891a6d.jpg)  
Fig. 3. Basic areas for absolute majority rules.

![](/api/attachments/38GCZP6B/fulltext/images/c2f5a0f653ce448156421fd24c60541f65674ee16e006f47f17d70def90b8636.jpg)  
Fig. 4. Basic areas for mixed case.

• Fig. 3: Absolute majority rules.

In this case, the opposition rule is effective and the priority of $C_g$ over $NP_g$ (and thus over $Q_g$ ) is visible. The $U_g$ area is much larger than in Fig. 2: it is constituted by a portion of the square $O, A'', M, B''$ ( $j^{+*} = j^{-*} = 0.5$ ) delimited by the above mentioned priorities of $C_g$ and $I_g$ over $U_g$ .

• Fig. 4: Mixed case.

The absolute majority rule is used for $P_{g}$ while the relative (simple) majority rule is considered for $NP_{g}$ . This case is similar to the first one except for the $P_{g}$ area. It corresponds to the hypothesis H1 where all individual indifferences are true ones. This situation seems to be the most widely used in practice and has been implemented in the JUDGES software.

## 3. Description and implementation of the JUDGES toolbox

The JUDGES software has been implemented in Turbo Pascal for IBM-compatible microcomputers. It will also be available soon for the Macintosh computer, with an enhanced interface that takes benefit of the mouse and the high resolution graphics.

JUDGES is a toolbox for group decision aid. The current version is designed to be used on a single microcomputer, but it is foreseen to develop a network version such that each decision maker will be able to use his own microcomputer to communicate with the others and to analyse the results. This network version will incorporate technical developments in order to support the network data exchange facilities between the decision makers, as well as a more complete data management interface. The user-friendliness of the system will be stressed, specially for what concerns the formulation of the decision problems and the group dynamics aspects. (Note added in proof: all the foreseen development is already achieved.)

The structure of JUDGES is given in Fig. 5. A first module has been designed for the management of the basic data: general description of the decision problem (description of the items and of the judges, individual rankings or evaluations of the items). The use in a network can be simulated: in this case, each judge enters separately and confidentially his own data.

A central module analyzes these basic data and provides the decision makers with four group decision aid (GDA) tools.

Each judge has the possibility to use an individual consultation module within which he can use the GDA tools and possibly modify his own basic data in order to reach an eventual consensus of the rankings.

![](/api/attachments/38GCZP6B/fulltext/images/41d75e5e95166928db0a6f3d165213a4e8f5c9b086887f0446155dfe90c67da4.jpg)  
Fig. 5. Structure of the JUDGES software.

Table 1

<table><tr><td colspan="7">Example: Nomination of an assistant professor in a faculty</td></tr><tr><td></td><td>J1</td><td>J2</td><td>J3</td><td>J4</td><td>J5</td><td>J6</td></tr><tr><td>C1</td><td>1</td><td>5</td><td>1</td><td>2</td><td>1</td><td>2</td></tr><tr><td>C2</td><td>2</td><td>4</td><td>6</td><td>1</td><td>2</td><td>1</td></tr><tr><td>C3</td><td>6</td><td>2</td><td>2</td><td>4</td><td>3</td><td>6</td></tr><tr><td>C4</td><td>3</td><td>1</td><td>3</td><td>3</td><td>6</td><td>3</td></tr><tr><td>C5</td><td>4</td><td>3</td><td>4</td><td>6</td><td>5</td><td>5</td></tr><tr><td>C6</td><td>5</td><td>6</td><td>5</td><td>5</td><td>4</td><td>4</td></tr></table>

We will now describe the four proposed GDA tools. They will be illustrated by a numerical example. For this purpose, let us consider the group decision problem described in Table 1.

## (1) GDA 1: Hierarchy of the judges

This first GDA tool graphically displays the similarities and conflicts among the judges. A hierarchy is constructed by considering the symmetric matrix of the Kendall's $\tau$ rank correlation coefficients between each pair of rankings (see Table 2). A negative value of $\tau$ indicates a majority of disagreements between the rankings, while a positive one shows a majority of agreements.

The simple minimal linkage hierarchy of Fig. 6 is then obtained. This representation shows that the judges J1 and J6 have the most similar rankings ( $\tau = 0.73$ is the maximal observed value in the matrix). The group formed by J1, J6, J4 and J5 has a minimal linkage of 0.20, which is the minimal $\tau$ between each pair of rankings in the group. The two other judges, J2 and J3 with also $\tau = 0.20$ , appear to be in strong disagreement with the first group, according to their minimal linkage of -0.47.

The hierarchy is displayed in the JUDGES software. A sliding horizontal line can be moved by the user in order to determine clusters of judges for which the minimal linkage is greater than the level of the line.

Table 2

<table><tr><td colspan="7">Example: Kendall&#x27;s τ matrix</td></tr><tr><td></td><td>J1</td><td>J2</td><td>J3</td><td>J4</td><td>J5</td><td>J6</td></tr><tr><td>J1</td><td>1.00</td><td>-0.20</td><td>0.07</td><td>0.47</td><td>0.20</td><td>0.73</td></tr><tr><td>J2</td><td></td><td>1.00</td><td>0.20</td><td>0.07</td><td>-0.47</td><td>-0.20</td></tr><tr><td>J3</td><td></td><td></td><td>1.00</td><td>0.07</td><td>0.07</td><td>-0.20</td></tr><tr><td>J4</td><td></td><td></td><td></td><td>1.00</td><td>0.47</td><td>0.73</td></tr><tr><td>J5</td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.20</td></tr><tr><td>J6</td><td></td><td></td><td></td><td></td><td></td><td>1.00</td></tr></table>

(2) GDA 2: Box plots of the Items.

In order to display the potential causes of disagreement, the variability of the ranks given by the judges to each item is represented by box plots.

The box plot associated to an item is constructed by considering the percentiles of the distribution of the ranks of this item (Fig. 7). The position of the box indicates the average level of the ranks given to the item by all the judges. The size of the box is proportional to the variability of these ranks. The upper and lower limits of the box are respectively the first and third quartiles of the distribution of the ranks. The center line corresponds to the median. Outside the box, the extreme points of the two vertical lines define the maximum spread of the distribution (respectively the best and the worst rank of the item).

![](/api/attachments/38GCZP6B/fulltext/images/199ce1e7b361239ec40c022978e62f2e7ad285302cf35371886b6df00a9c97f4.jpg)  
Fig. 6. Example: Hierarchy.

![](/api/attachments/38GCZP6B/fulltext/images/4e9ade7ecc92ca2b9ab82dd7f61eba52dac21ace546475c9b3343009f256365c.jpg)  
Fig. 7. Structure of a box plot.

![](/api/attachments/38GCZP6B/fulltext/images/fa94bc9da8f61620258c17c0073a4e7b91b917c37fb33cfb1961bae4cbc1b01c.jpg)  
Fig. 8(a). Example: Box plots. (a) For judge J1.

In JUDGES, each judge can examine the box plots together with his own ranks, represented by stars in the graphics.

The graphics obtained for judge J1 in the example is given in Fig. 8(a), and the similar display for judge J2 in Fig. 8(b). The size and position of the boxes lead to the following conclusions: the higher position of the C1 box and median reveals the best ranking of this candidate by the group; the C4 box seems to provide a relative consensus of the majority of the judges on the third position of this candidate, with two exceptions (best rank is 1 and worst is 6). At the opposite, the greatest conflict of opinions is revealed by the largest box of C3. It has to be noted that in this particular example, the very small number of judges makes it more difficult to exploit this GDA tool.

![](/api/attachments/38GCZP6B/fulltext/images/60627742fc35db988375e361b880a3e93f4642f2c1d5ca66c2f13034545ba19f.jpg)  
Fig. 8(b). Box plots for judge J2.

Table 3

<table><tr><td>In order to reach a consensus:</td></tr><tr><td>- you should give a better rank to item C1,</td></tr><tr><td>- you should give a worse rank to item C4,</td></tr><tr><td>- you should give a worse rank to item C5,</td></tr><tr><td>- you should give a better rank to item C6</td></tr></table>

## (3) GDA 3: Individual advice

In order to assist the decision makers to reach a consensus, individual advice is issued to each judge by considering the deviations between the ranking of the judge and the box plots. If the rank given to an item lies outside of the box, the judge is advised to modify his ranking accordingly. For instance, the advice given in Table 3 should be issued to judge J2 (see Fig. 8(b)).

(4) GDA 4: Pairwise group preference relations system

For each pair of items, the triangular display can be used in order to graphically determine the group preference relation that holds. Such displays are commented in the real-world application of Section 4.

## 4. A real-world application

In this section, we present the results of the application of the JUDGES methodology to a real-world multi-judge decision problem.

## 4.1. Description of the decision problem

Eight members of an investment club have evaluated 19 common stocks according to several criteria (return, price earning ratio, ...). Eight different rankings of the stocks have been obtained, depending on the individual weightings of the criteria. It is important for an efficient management of the club to reach a consensus on the ranking of the stocks, in view of a common investment policy.

Table 4

<table><tr><td colspan="10">Individual rankings for the investment club</td></tr><tr><td colspan="10">The 8 judges (members): Gilles, Jean-Pierre, Eliane, Philippe, Bertrand, Annie, Carlos and Gérard. The 19 common stocks: C1 to C19. Each judge has ranked individually the 19 common stocks. The following table contains the corresponding ranks.</td></tr><tr><td></td><td></td><td>Gilles</td><td>Jean-Pierre</td><td>Eliane</td><td>Philippe</td><td>Bertrand</td><td>Annie</td><td>Carlos</td><td>Gérard</td></tr><tr><td>C1:</td><td>BBL</td><td>9</td><td>7</td><td>3.5</td><td>10</td><td>2</td><td>5.5</td><td>4</td><td>2.5</td></tr><tr><td>C2:</td><td>G.Bque</td><td>6</td><td>13</td><td>3.5</td><td>2</td><td>9</td><td>5.5</td><td>7</td><td>2.5</td></tr><tr><td>C3:</td><td>Pétro.</td><td>10</td><td>11</td><td>8</td><td>18</td><td>7.5</td><td>2</td><td>8</td><td>8.5</td></tr><tr><td>C4:</td><td>Cometra</td><td>15</td><td>12</td><td>10</td><td>17</td><td>11</td><td>12</td><td>15</td><td>11</td></tr><tr><td>C5:</td><td>Sofina</td><td>4</td><td>3</td><td>1</td><td>3</td><td>4</td><td>4</td><td>3</td><td>4</td></tr><tr><td>C6:</td><td>Cobepa</td><td>2</td><td>5</td><td>2</td><td>12</td><td>5</td><td>3</td><td>1</td><td>1</td></tr><tr><td>C7:</td><td>Colruyt</td><td>14</td><td>17</td><td>15</td><td>19</td><td>3</td><td>7</td><td>17</td><td>17</td></tr><tr><td>C8:</td><td>Delhaize</td><td>12.5</td><td>14.5</td><td>13</td><td>14.5</td><td>16.5</td><td>14.5</td><td>10</td><td>19</td></tr><tr><td>C9:</td><td>Royale B.</td><td>12.5</td><td>14.5</td><td>19</td><td>14.5</td><td>16.5</td><td>14.5</td><td>18</td><td>14</td></tr><tr><td>C10:</td><td>AG</td><td>11</td><td>19</td><td>11</td><td>11</td><td>14</td><td>19</td><td>16</td><td>6</td></tr><tr><td>C11:</td><td>Solvay</td><td>8</td><td>8</td><td>14</td><td>7</td><td>6</td><td>16</td><td>2</td><td>18</td></tr><tr><td>C12:</td><td>Intercom</td><td>18</td><td>16</td><td>5</td><td>6</td><td>10</td><td>11</td><td>14</td><td>7</td></tr><tr><td>C13:</td><td>Unerg</td><td>16</td><td>10</td><td>9</td><td>13</td><td>15</td><td>10</td><td>12</td><td>15</td></tr><tr><td>C14:</td><td>Barco Elec.</td><td>17</td><td>18</td><td>18</td><td>16</td><td>18</td><td>18</td><td>9</td><td>13</td></tr><tr><td>C15:</td><td>Tirlemont</td><td>19</td><td>2</td><td>17</td><td>9</td><td>19</td><td>17</td><td>13</td><td>16</td></tr><tr><td>C16:</td><td>Glaverbel</td><td>5</td><td>9</td><td>7</td><td>4</td><td>13</td><td>9</td><td>11</td><td>10</td></tr><tr><td>C17:</td><td>Tractebel</td><td>3</td><td>6</td><td>16</td><td>5</td><td>12</td><td>13</td><td>6</td><td>12</td></tr><tr><td>C18:</td><td>CFE</td><td>7</td><td>1</td><td>12</td><td>8</td><td>7.5</td><td>8</td><td>19</td><td>8.5</td></tr><tr><td>C19:</td><td>Ciment.Obourg</td><td>1</td><td>4</td><td>6</td><td>1</td><td>1</td><td>1</td><td>5</td><td>5</td></tr><tr><td colspan="10">Note: The actual data used in this study are from 1989 and the results obtained are only valid for these period and highly dependent on the subjective weighting introduced by the judges.</td></tr></table>

![](/api/attachments/38GCZP6B/fulltext/images/2ba25ad189c41b12528ba6228e31f513e10338c64cba5e1a733cbb54292a462d.jpg)  
Fig. 9. Stocks: Hierarchy.

The individual rankings are given in Table 4.

## 4.2. Results of the JUDGES analysis

## 4.2.1. GDA 1: Hierarchy of the judges

The hierarchy of the eight judges is given in Fig. 9. The low position of the hierarchy ( $\tau = 0.15$ ) indicates the absence of strong disagreements between the judges, which augurs a rather easy task of consensus-seeking. Two main groups of more similar opinions appear: Gilles, Philippe and Jean-Pierre on one hand, Eliane, Gérard, Bertrand, Annie and Carlos on the other hand. Furthermore, two pairs of judges have very close opinions ( $\tau = 0.60$ ): Eliane and Gérard, and Bertrand and Annie. Finally, Carlos seems to have the most different ranking.

## 4.2.2. GDA 2: Box plots of the items

The box-plots obtained for the 19 common stocks are represented in Fig. 10, together with the individual ranking of Carlos shown by stars. Looking at the position of the boxes, it appears that some stocks were well positioned by most judges (C5: Sofina, C6: Cobepa, C19: Ciment Obourg, and also C1: BBL, C2: G.Bque, with a weaker consensus). At the opposite side, C9: Royale B. and C14: Barco Elec. are generally at the bottom of the ranking. C5: Sofina has obtained the best consensus, as its quite small box indicates, while C11: Solvay exhibits a large dispersion of the opinions. As observed on the hierarchy, Carlos has a most original opinion and his ranking often deviates from the boxes (seven stars are found outside of the boxes and three at the extreme points).

![](/api/attachments/38GCZP6B/fulltext/images/640b0275d2726ccacde540f764fc389eb5334481596ab9898f760e49d12b5d33.jpg)  
> Use arrow keys to see candidates names.  
Fig. 10. Stocks: Box plots.

## 4.2.3. GDA 3: Individual advice

According to Fig. 10, seven pieces of advice are given to Carlos:

\- give a worse (higher) rank to $C6$ : Cobepa, $C8$ : Delhaize, $C11$ : Solvay, $C14$ : Barco Elec.;

\- give a better (lower) rank to C9: Royale B., C16: Glaverbel and C18: CFE.

After discussion, several judges (Carlos, Jean-Pierre, Philippe, Eliane and Gérard) have accepted to follow the advice and modify their rankings accordingly. The resulting hierarchy and box-plots are given in Figs. 11 and 12.

A higher level of consensus ( $\tau = 0.40$ ) is observed in the hierarchy and the size of the boxes

![](/api/attachments/38GCZP6B/fulltext/images/794ba6489c7ffb2f2f48c94d296511d1824c8f7c2d9813996aab0e464c981ddf.jpg)  
Fig. 11. Stocks: Hierarchy, modified.

![](/api/attachments/38GCZP6B/fulltext/images/91d6cbd76ced1d417dc67b79b035508493a2b4997c3550553f62e72a1a999834.jpg)  
> Use arrow keys to see candidates names.  
ESC : Menu <

Fig. 12. Stocks: Box plots, modified.

has been reduced. At this stage, the members have decided to stop the procedure and to adopt the global ranking induced by the medians of the box-plots. This final ranking is given in Table 5, together with the box-plots main coordinates and spread (worst rank–best rank).

It appears that the three best ranked stocks have a small spread which gives a strong confidence in their good positions. The same conclusion holds for the last ranked stock. These positions are confirmed by looking at the quartiles. Let us note the large spread of C7: Colruyt, still indicating some disagreements among the judges on the evaluation of this stock; however, it is globally rather bad rated.

![](/api/attachments/38GCZP6B/fulltext/images/f7814aa23819e069e0559d9584a0af26d4394832752175f36674a2708411d0f7.jpg)  
Press <SpaceBar> to scan candidates or ESC to stop.  
Fig. 13. Stocks: Triangular display for C1 and C2.

4.2.4. GDA 4: Pairwise group preference relations system

Fig. 13 shows the triangular display for stocks C1: BBL and C2: G.Bque. It is an example of a conflicting situation.

Fig. 14 shows the triangular display for stocks C3: Petro and C18: CFE. In this case, there is a weak preference of C18: CFE over C3: Petro. This information is consistent with the quartile information given in the previous table: indeed

Table 5

<table><tr><td colspan="6">Final ranking of the 19 common stocks</td></tr><tr><td>Rank</td><td>Stock</td><td>Median</td><td>First quartile</td><td>Third quartile</td><td>Spread</td></tr><tr><td>1</td><td>C19: Ciment Obourg</td><td>1.5</td><td>1</td><td>4</td><td>4</td></tr><tr><td>2</td><td>C6: Cobepa</td><td>2.5</td><td>1</td><td>3.5</td><td>4</td></tr><tr><td>3</td><td>C5: Sofina</td><td>3</td><td>2</td><td>4</td><td>4</td></tr><tr><td>4.5</td><td>C1: BBL</td><td>4.5</td><td>2.5</td><td>5.5</td><td>7</td></tr><tr><td>4.5</td><td>C2: G. Bque</td><td>4.5</td><td>3.5</td><td>5.5</td><td>6.5</td></tr><tr><td>6.5</td><td>C3: Petro</td><td>7.5</td><td>6.5</td><td>10.5</td><td>9.5</td></tr><tr><td>6.5</td><td>C18: CFE</td><td>7.5</td><td>6</td><td>8</td><td>2.5</td></tr><tr><td>8.5</td><td>C11: Solvay</td><td>8</td><td>8</td><td>12</td><td>10.5</td></tr><tr><td>8.5</td><td>C17: Tractebel</td><td>8</td><td>5</td><td>12</td><td>10</td></tr><tr><td>10</td><td>C16: Glaverbel</td><td>8.5</td><td>8</td><td>9.5</td><td>8</td></tr><tr><td>11</td><td>C12: Intercom</td><td>10.5</td><td>9.5</td><td>13</td><td>9.5</td></tr><tr><td>12</td><td>C4: Cometra</td><td>13</td><td>11</td><td>15.5</td><td>6</td></tr><tr><td>13</td><td>C13: Unerg</td><td>13</td><td>11</td><td>15</td><td>6</td></tr><tr><td>14</td><td>C10: AG</td><td>13.5</td><td>11.5</td><td>16.5</td><td>9.5</td></tr><tr><td>15</td><td>C8: Delhaize</td><td>15</td><td>12.5</td><td>15.5</td><td>6</td></tr><tr><td>16</td><td>C9: Royale B.</td><td>15.5</td><td>14</td><td>16.5</td><td>6.5</td></tr><tr><td>17</td><td>C15: Tirlemont</td><td>17</td><td>14</td><td>18.5</td><td>5.5</td></tr><tr><td>18</td><td>C7: Colruyt</td><td>17.5</td><td>10.5</td><td>18</td><td>15.5</td></tr><tr><td>19</td><td>C14: Barco Elec.</td><td>18.5</td><td>17.5</td><td>19</td><td>3.5</td></tr></table>

![](/api/attachments/38GCZP6B/fulltext/images/73b655318fc86501abde2896a2e445f709dfe8d38118a7eedbfec8a956369724.jpg)  
Press <SpaceBar> to scan candidates or ESC to stop.

Fig. 14. Stocks: Triangular display for C3 and C18.

C18: CFE has a much narrower and better located box-plot.

## 5. Conclusion

This paper presents the first step in the construction of a complete toolbox for multicriteria multijudge decision aid. The use of original graphical representation is an important feature of the methodology and provides the decision makers with a clear view of their consensus and disagreements. The notion of conflict within the individual opinions is also emphasized and guidelines are proposed in order to help the judges to reach an eventual consensus.

JUDGES has already been successfully applied in several real-world applications: among others for the ranking of projects to be assigned to a working team, for the evaluation of products of a pipe producer and in the field of hospital management. The methodology has also been applied in a pure multicriteria context, with criteria considered as judges. A network version running under Windows has recently been developed and will be used in order to analyse more completely the behavioural reactions of groups of decision makers in using the software. At the present stage of development, we observed a facilitation of the exposure of conflicts and of a more objective expression of individual opinions.

JUDGES has proved to be a quite flexible set of descriptive Group Decision Aid tools. There is no predefined user guide and the way it is used is highly dependent of the specific application considered. In most cases, the main objective of the group is to reach either a consensus on the ranking of the items or to agree on a ranking which produces the least disagreements with respect to the individual opinions. This problem is partially addressed by JUDGES and is a central feature of the ARGOS program.

The ARGOS multicriteria-oriented toolbox will be presented in a forthcoming paper. It is already operational and has been applied in the same common stocks ranking problem presented in this paper. It proved to be a good complement to JUDGES in providing a final decision.

## References

[1] J.P. Brans, Ph. Vincke and B. Mareschal, How to select and how to rank projects: The PROMETHEE method, Europ. J. Operat. Res. 24 (2) (1986) 228–238.

[2] T.X. Bui, Coop: A group decision support system for cooperative multiple criteria group decision making, Lecture Notes in Comput. Sci. 290 (Springer-Verlag, Berlin, 1987)

[3] J. Churchill, Complexity and strategic decision-making, in C. Eden and J. Radford, eds., Tackling Strategic Problems: The Role of Group Decision Support (SAGE Publications, London, 1990) 1–17.

[4] G. Colson and Chr. De Bruyn, Guest eds., Models and methods in multiple criteria decision making, Special issue of Math. Comput. Modelling, 12, (10/11) (1989) 1201–1436.

[5] G. Colson and Chr. Dressen, ARGOS: Aide au Rangement de Groupe d'Objets à Surclasser, forthcoming.

[6] G. Doukidis, F. Land and G. Miller, Knowledge-based Management Support Systems (Ellis-Horwood, Chichester, UK, 1989).

[7] De Sanctis and Gallupe, Foundation for study of group decision support systems, Management Sci. 33 (5) (1987).

[8] C. Eden and J. Radford ed., Tackling Strategic Problems. The Role of Group Decision Support (SAGE Publications, London, 1990).

[9] P. Fishburn, The Theory of Social Choice, (Princeton University Press, Princeton, NJ, 1973).

[10] C. Hwang and M. Lin, Group decision making under multiple criteria, Lecture Notes in Econ. Math. Syst. 281 (Springer-Verlag, Berlin, 1987).

[11] T. Jelassi and R. Beauclair, An integrated framework for group decision support systems, Informat. & Management, 13 (1987) 143–153.

[12] H. Pastijn and J. Leysen, Constructing an outranking relation with ORESTE, Math. Comput. Modelling 12, (10/11) (1989) 1255–1268.

[13] M. Roubens and Ph. Vincke, Preference modelling, Lecture Notes in Econ. Math. Syst. 250 (Springer-Verlag, Berlin, 1985)

[14] B. Roy, Méthodologie Multicritère d'Aide à la Décision (Economica, Paris, 1985).

[15] B. Roy and Ph. Vincke, Relational systems of preference with one or more pseudo-criteria: Some new concepts and results, Management Sci. 30 (11) (1984) 1323–1335.

[16] R. Steuer, Multiple Criteria Optimization: Theory, Computation and Application (Wiley, New York, 1986).

[17] Ph. Vincke, Analysis of multicriteria decision aid in Europe (invited review), Europ. J. Operat. Res. 25 (2) (1986) 160–168.
