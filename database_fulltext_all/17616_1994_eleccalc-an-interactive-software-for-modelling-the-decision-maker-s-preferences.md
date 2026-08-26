---
otero_id: 17616
otero_key: "GGYB2579"
title: "ELECCALC — an interactive software for modelling the decision maker's preferences"
authors: "Laszlo Nandor Kiss; Jean-Marc Martel; Raymond Nadeau"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90049-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# ELECCALC – an interactive software for modelling the decision maker's preferences

Laszlo Nandor Kiss \*, Jean-Marc Martel and Raymond Nadeau

Faculté des Sciences de l'Administration, Université Laval, Sainte-Foy, Québec, G1K 7P4, Canada

In general, it is difficult to articulate the decision-maker's (DM) preference structure, specially in taking into account several criteria. Most synthetical approaches (single synthetical criterion approach, synthetical outranking approach,...) are based on some a priori information. In this paper, we attempt to analyze such a structure through a descriptive approach. The idea is to explain the global preferences revealed by the DM from pairwise comparisons of reference alternatives. A disaggregation – aggregation interactive procedure like in PREFCALC is used in ELECCALC, which enables a DM to assess the parameters of ELECTRE II.

Keywords: Multiple criteria decision problem; Concordance thresholds; Discordance thresholds; Indifference thresholds; Weights of criteria; Preference relations; Direct decomposition; Inverse decomposition; Quasi-median decomposition

![](/api/attachments/GGYB2579/fulltext/images/e1f9572ec3e379113844ef2c1a7ebcd84ae5e020b802cfb04f7697198f07b437.jpg)

Laszlo Nandor Kiss is professor at the Faculté des Sciences de l'Administration de l'Université Laval. He obtained the Diploma degree in Transport Engineering in 1968, the Master Tech (OR) degree in 1973 and the degree of Doctor Tech (IE & OR) in 1977, all from the Polytechnical University of Budapest. His areas of activity are digital modeling, software development, simulation, mathematical programming, heuristical and prototype algorithms. His current research interests include hierarchical structures, multiple criteria decision analysis and decision support systems design.

## 1. Introduction

During the last two decades there have been remarkable developments in two classes of models designed to help decision makers (DM) to deal with weakly structured problems, namely Decision Support Systems (DSS) and Multiple Criteria Decision Making (MCDM) models. Despite the similarity of their goals, these two fields of research have for the most part been developed separately and there are still relatively few examples of operational systems capable of integrating both the DSS and MCDM models. However, since the middle of the 1980's several researchers have realized the potential of this integration and have attempted to put forth interactive and intelligent DSS's which take advantage of the vast support inherent in MCDM.

It is in light of this that Martel and Nadeau [7] have proposed an interactive algorithm designed to model the preferences of a DM who is placed

![](/api/attachments/GGYB2579/fulltext/images/a8f8f626b8fb27b73e51d93d8a3dff857a561df0569989f0a06e20c648d80a6d.jpg)

Jean-Marc Martel is professor and Head of the Department of Operations and Decision Systems at the Faculté des Sciences de l'Administration de l'Université Laval. He received his M.Sc. in mathematics from Université Laval and Ph.D. in Applied Economics from Université de Louvain. His research interests include Bayesian statistics, information economics and multiple criteria decision analysis. He is member of AIDS, TIMS, CORS, ASAC, ISI and AC-

FAS. Dr Martel is author of numerous books and articles.  
![](/api/attachments/GGYB2579/fulltext/images/00933b9db63ec6839d3cd6600794be6ef6afc05c14bfa587c99dd23feaea77f6.jpg)

Raymond Nadeau is professor of quantitative methods at the Faculté des Sciences de l'Administration de l'Université Laval. He received in B.Sc. in mathematics from the Université de Montréal and a M.Sc. and a Ph.D. in probability and statistics from the Université Laval. His research interests include stoachastic programming and multiple criteria decision analysis. He is the co-author of two textbooks in probability and statistics and his research papers appeared mainly in EJOR, JORS, INFOR and Operations Research.

before a semi-structured decision problem. The algorithm is based on the ELECTRE II outranking method of Roy and Bertier [8]. Faced with a multiple criteria decision problem made up of a finite and relatively small number of alternatives to be classified, the ELECTRE II multiple criteria method is appealing because it does not assume well structured preferences in the mind of the decision maker and it does not demand the aggregation of criteria into a single synthetic criterion, as do the models based on the multiple attribute utility theory (MAUT). While these models are based on rationality principles where, faced with two alternatives, only indifference and strict preference are possible, in ELECTRE II it is assumed that the two alternatives can also be incomparable and then the ranking obtained by this method is only partial. This ranking results from the outranking relations arrived at from comparing the alternatives in pairs.

In this comparison process, the DM's preferences are expressed by way of some parameters: weights of the criteria, indifference, concordance and discordance thresholds. However, determining these parameters by asking the DM relatively direct questions can be difficult in practice and this constitutes one of the major difficulties in using this method.

To get around this difficulty, we have proposed the use of an indirect approach to determine the value of the parameters in question. This approach is based on the use of a disaggregation logic of the global preferences like the one used by Jacquet-Lagrèze and Siskos [3] in the UTA method and by Jacquet-Lagrèze [4] in the PREFCALC software. In this approach, the DM globally expresses his preferences about a few reference alternatives of his choice. From these global preferences, our method enables us to specify initial values for the parameters used in ELECTRE II. On the basis of these initial values, our method allows to obtain a ranking of the reference alternatives. On the one hand, if he is satisfied with this ranking, the DM can then obtain a ranking for all the considered alternatives from the initial values of the parameters. On the other hand, if he is not satisfied with the initial ranking of the reference alternatives, he can change one or several of the parameters' values and obtain a new ranking. In other words, once a satisfactory ranking of the reference alternatives is obtained, all other alternatives can be ranked on the basis of the revised parameters. In short, the proposed algorithm uses an interactive disaggregation and aggregation process of DM's preferences.

The Martel and Nadeau's [7] interactive algorithm seems to get around an important problem one finds when using ELECTRE II. However, in order for it to become a really useful aid in decision making, it must be made operational on a computer; that interactive software called ELECCALC, is presented in what follows. It is a tool designed to aid a DM in the context of an individual decision problem with a finite number of alternatives, evaluated on several criteria, that he has to rank. This presents, therefore, a multiple criteria decision problem which can be structured from a finite set of alternatives, from a family of coherent criteria and from a matrix of performances which are considered deterministic. In developing this software, we have endeavoured to give it the desired characteristics to make it a really up to date tool; these characteristics, which are mentioned, among others, in Turban [10], are simplicity, flexibility, effectiveness, adaptability, speed, intelligence, etc...

In the following section, we present the main components of the ELECCALC algorithm grouped into four phases: determining basic elements, first dialogue with the DM, first stage calculation, new dialogue and new calculation. In Section 3, we look at how the algorithm has been made operational on a computer. After having presented the general structure of various computer modules we then give a formal mathematical-algorithmic description of some of them. Section 4 presents a small didactical example. Finally we conclude our paper with a few comments about ELECCALC.

## 2. Presentation of ELECCALC components

Generally, the ELECCALC system can be divided into four phases: determining the basic elements, first dialogue with the DM, first calculation stage, new dialogue and new calculation stage. Each of these phases will be briefly described in what follows.

## 2.1. Phase 1: determining the basic elements

The system assumes that DM's problem can be structured around three fundamental elements as in ELECTRE II:

$$
\mathbf {A} = \left\{\mathrm{a} _ {\mathrm{i}}; \mathrm{i} = 1, 2, \dots , \mathrm{M} \right\},
$$

a finite set of alternatives to be ranked,

$$
\mathbf {F} = \left\{\mathrm{g} _ {\mathrm{j}}; \mathrm{j} = 1, 2, \dots , \mathrm{N} \right\},
$$

a family of criteria with regard to which each alternative is evaluated,

$$
\mathbf {E} = \left\{\mathrm{p} _ {\mathrm{ij}} = \mathrm{g} _ {\mathrm{j}} \left(\mathrm{a} _ {\mathrm{i}}\right); \mathrm{i} = 1, 2, \dots , \mathrm{M}; \mathrm{j} = 1, 2, \dots , \mathrm{N} \right\},
$$

a performance matrix of the alternatives evaluated according to each of these criteria.

Faced with a particular problem, our system enables the DM to interactively and progressively construct sets A and F, and subsequently matrix E; it is also possible to directly integrate the triplet $(A,F,E)$ which already exists. Moreover, in both cases, once the triplet is obtained, the DM is still able to modify sets A and F as well as the corresponding values of E.

From this initial structuring, our system proceeds according to the general logic of ELECTRE II. By comparing the alternative in pairs, we are looking to create two outranking relations: one “strong” ( $O^{S}$ ) and the other “weak” ( $O^{W}$ ). To do this, for each pair $(a_{i}, a_{i*})$ of alternatives of A, we define a global concordance index $c(a_{i}, a_{i*})$ on the set of criteria and also a local discordance index $d_{j}(a_{i}, a_{i*})$ with regard to each criterion $g_{j}$ . The concordance indexes depend on the weight $\pi_{j}$ associated with each criterion and the discordance indexes depend on the differences $d_{j}(a_{i}, a_{i*}) = g_{j}(a_{i*}) - g_{j}(a_{i*})$ of the respective performances of $a_{i}$ and $a_{i*}$ , with regard to each criterion $g_{j}$ . Afterwards, in order to establish whether a strong or weak outranking exists or not, we use:

\- three concordance thresholds $\mathbf{C}_1, \mathbf{C}_2$ and $\mathbf{C}_3$ such as $0 < \mathbf{C}_3 < \mathbf{C}_2 < \mathbf{C}_1 < 1$ ;

\- two sets of discordance thresholds $\mathrm{D_j}(1)$ and $\mathrm{D_j}(2)$ such as $\mathrm{D_j}(1) < \mathrm{D_j}(2), j = 1,2,\dots,N$ .

So, as in ELECTRE II (Roy and Bertier [8]; Guigou [2]), we use three concordance thresholds $C_{1}$ , $C_{2}$ and $C_{3}$ . Moreover, we slightly modify that method (Martel and Nadeau [7]) by introducing an indifference threshold $I_{j}$ on each criterion $g_{j}$ :

those thresholds $I_{j}$ intervene in outranking conditions and particularly in strong outranking conditions as that is illustrated by equations (1), (2), (3) and (4) of the following sections. According to the standard ELECTRE II method, one must assign a priori (with the help of the decision maker) the values for the weights $\pi_{j}$ , for the concordance thresholds $C_{1}$ , $C_{2}$ and $C_{3}$ , for the discordance thresholds $D_{j}(1)$ and $D_{j}(2)$ and for the indifference thresholds $I_{j}$ , $j = 1, 2, \ldots, N$ . This is a rather difficult task which can limit the application possibilities of the method.

Instead of turning to such a direct approach to assign values to the involved parameters, in ELECCALC we propose an indirect approach. These values are instead extracted from the global preferences expressed by the DM regarding a small set of alternatives from A. The dialogue which allows the information to be obtained from the DM, will be briefly discussed in the following section. Moreover, in our algorithm, in order to obtain a first set of values for the parameters, we must fix some temporary initial values for those parameters; these initial values are chosen somewhat arbitrarily but they should not have any negative effect on the first set of values calculated by the system for these parameters. The initial values of the parameters $I_{j}$ , $D_{j}(2)$ , $C_{1}$ and $C_{3}$ are respectively recorded by intervals $[I_{j}^{L}, I_{j}^{U}]$ , $[D_{j}^{L}(2), D_{j}^{U}(2)]$ , $[C_{1}^{L}, C_{2}^{U}]$ and $[C_{3}^{L}, C_{3}^{U}]$ , where “L” and “U” signifies “Lower” and “Upper” respectively.

Let $R_{j} = \max |g_{j}(a_{i}) - g_{j}(a_{i*})|$ , for all $(a_{i}, a_{i*}) \in \mathbf{A} \times \mathbf{A}$ , $j = 1, 2, \ldots, N$ , then we first put

$$
\mathrm{D} _ {\mathrm{j}} (2) = 0. 2 \mathrm{R} _ {\mathrm{j}}, \mathrm{D} _ {\mathrm{j}} (2) = 0. 5 \mathrm{R} _ {\mathrm{j}};
$$

$$
\mathrm{I} _ {\mathrm{j}} ^ {\mathrm{L}} = 0, \mathrm{I} _ {\mathrm{j}} ^ {\mathrm{U}} = 0. 1 \mathrm{R} _ {\mathrm{j}};
$$

$$
\mathrm{C} _ {1} ^ {\mathrm{L}} = 0. 7 5, \mathrm{C} _ {1} ^ {\mathrm{U}} = 1. 0, \mathrm{C} _ {3} ^ {\mathrm{L}} = 0. 5, \mathrm{C} _ {3} ^ {\mathrm{U}} = 0. 6 5.
$$

We must always have

$$
\mathrm{D} _ {\mathrm{j}} (1) <   \mathrm{D} _ {\mathrm{j}} ^ {\mathrm{L}} (2) <   \mathrm{D} _ {\mathrm{j}} ^ {\mathrm{U}} (2);
$$

$$
\mathrm{I} _ {\mathrm{j}} ^ {\mathrm{L}} <   \mathrm{I} _ {\mathrm{j}} ^ {\mathrm{U}} \ll \mathrm{D} _ {\mathrm{j}} ^ {\mathrm{L}} (2);
$$

$$
\mathrm{C} _ {3} ^ {\mathrm{L}} <   \mathrm{C} _ {3} ^ {\mathrm{U}} <   \mathrm{C} _ {2} <   \mathrm{C} _ {1} ^ {\mathrm{L}} <   \mathrm{C} _ {1} ^ {\mathrm{U}}.
$$

The initial values of these parameters, as well as the components of the triplet (A,F,E), make up the basic elements upon which the proposed system rests.

## 2.2. Phase 2: first dialogue with the decision maker

Once the structuring of the problem and the initialization of the system is completed, a dialogue between the system and the DM begins. This phase enables the DM to express his global preferences regarding a small set A' of alternatives from A. From these global preferences we will deduce the parameters' values of the algorithm and subsequently a ranking of the alternatives in A' and then in A.

As a first step in this dialogue, the DM is asked to choose a subset $A'$ (called a reference set) from A. This is a set of alternatives from A, with small cardinality (5 to 7 elements), that the DM is quite familiar with and that he will compare. The DM is also asked to choose a subset of criteria $F'$ from F, from which he wishes to evaluate the alternatives of $A'$ ; $F'$ only contains the criteria that he judges pertinent in the evaluation of the alternatives. Consequently, a submatrix $E'$ which contains the alternatives' performances of $A'$ with regard to the criteria in $F'$ , is extracted from the performance matrix E.

At this time, the comparison of the reference alternatives $\mathbf{A}'$ , in pairs, begins. For some pair $(\mathrm{a_i},\mathrm{a_{i*}})\in \mathbf{A}'\times \mathbf{A}',\mathrm{i}\neq \mathrm{i}^*$ , the DM is asked to respond to the following propositions:

(P.1) alternative $\mathbf{a}_{\mathrm{i}}$ is at least as good as alternative $\mathbf{a}_{\mathrm{i}^*}$ , and

(P.2) alternative $\mathbf{a}_{\mathrm{i}^*}$ is at least as good as alternative $\mathbf{a}_{\mathrm{j}}$ .

To each of these propositions the DM can answer “Yes” (Y), “No” (N) and “I don’t know” (I). The information revealed by the DM in this manner is disaggregated so as to construct his preference structure in order to specify values for the parameters $\pi_{j}$ , $I_{j}$ , $D_{j}(1)$ , $D_{j}(2)$ , $C_{1}$ , $C_{2}$ and $C_{3}$ which express that structure through ELECTRE II.

For the propositions (P.1,P.2), the DM can answer with one of the nine following pairs of responses: ("Yes", "Yes"), ("Yes", "No"), ("Yes", "Don't know"), ("No", "Yes"), ("No", "No"), ("No", "Don't know"), ("Don't know", "Yes"), ("Don't know", "No"), ("Don't know", "Don't know"). As soon as the DM responds to the propositions (P.1,P.2) concerning a pair of alternatives in particular, the system verifies the coherence between the information contained in the pair of responses to (P.1,P.2) and the information contained in the performance matrix $E'$ with regard to this pair of alternatives. Depending on whether this information is coherent or not, the DM's responses to $(P.1,P.2)$ are either directly used by the system as elements of information concerning the parameters to be constructed or lead the system to ask the DM other questions in order to further determine the values of these parameters.

Depending on the situation, the DM may be asked three types of supplementary questions. When the system detects an incoherence between the preferences expressed by the DM concerning $(a_{i}, a_{i^{*}})$ and those suggested by the performance matrix $E'$ , he is asked the following question:

(Q.1) - “Do you wish to change your responses concerning (P.1) or (P.2)?”

If the DM changes his preferences, the outcome is analyzed as a new pair of responses. If he does not change them, the incoherence persists and pertinent information concerning the unknown parameters can not be deduced from his preferences.

Moreover, when no incoherence is noted in the DM's preferences with regard to the pair $(a_{i}, a_{i*})$ , and when it exists $g_{j} \in F'$ such that we have

$$
\left| \mathrm{d} _ {\mathrm{j}} \left(\mathrm{a} _ {\mathrm{i}}, \mathrm{a} _ {\mathrm{i} ^ {*}}\right) \right| \in ] \mathrm{I} _ {\mathrm{j}} ^ {\mathrm{L}}, \mathrm{I} _ {\mathrm{j}} ^ {\mathrm{U}} [,
$$

we then ask the DM the following type of question:

(Q.2) - “Do you consider the difference $|d_{j}(a_{i},a_{i^{*}})|$ to be significant (s.) or not (n.s.) such that you deem one of the two alternatives to be at least as good as the other, those alternatives being otherwise considered equivalent with regard to all the other criteria?”

Depending whether the answer to $(Q.2)$ is affirmative or negative, the system assigns a new value to the upper or the lower bound of the indifference threshold $I_{i}$ .

Finally, when no incoherence is found in the DM's preferences with regard to the pair $(\mathbf{a}_i,\mathbf{a}_{i^*})$ and when it exists $\mathbf{g_j}\in \mathbf{F}'$ such that we have $|\mathrm{d_j}(\mathrm{a_i},\mathrm{a_{i^*}})|\in ]\mathrm{D_j}^{\mathrm{L}}(2),\mathrm{D_j}^{\mathrm{U}}(2)[$ , we then ask the DM the following type of question:

(Q.3) - “Do you consider the difference $|d_{j}(a_{i},a_{i^{*}})|$ to be big enough (b.e.) or not (n.b.e.) to prevent you from declaring that one is at least as good as the other no matter what the performances of these two alternatives are with regard to all the other criteria?"

Depending on whether the answer to $(Q.3)$ is affirmative or negative, the system assigns a new value to the upper or the lower bound of the discordance threshold $D_{i}(2)$ .

In summary, we ask the DM to respond to the propositions $(P.1)$ and $(P.2)$ regarding a pair of alternatives $(a_{i},a_{i*})$ from A'. Depending on his responses, we eventually ask him one or several questions of the type $(Q.1)$ , $(Q.2)$ or $(Q.3)$ . However, in order to limit the number of questions asked in this first dialogue phase, we do not try to eliminate at any cost all the possible incoherencies between the DM's revealed preferences and those suggested by E'. If an incoherence still persists after a limited number of questions, the system will simply not consider the DM's preferences regarding this particular pair $(a_{i},a_{i*})$ in the determination of the unknown parameters. Martel and Nadeau [7] describes the dialogue between the system and the DM, resulting from each of the nine pairs of possible responses to the pair of propositions $(P.1,P.2)$ . It should also be mentioned that the DM is not obliged to give a response concerning all the possible pairs of alternatives from A', but obviously the more information he reveals with regard to his preferences the more the ranking of A' and of A (which the system will subsequently supply) will satisfy the DM.

To illustrate this dialogue between the system and the DM as well as the obtained information concerning the values of the unknown parameters, suppose that the DM answers (“Yes”, “No”) to propositions (P.1, P.2) for an alternatives’ pair $(a_{i*}, a_{i})$ . First the system verifies if one alternative is dominating another. If, for example, $a_{i}$ dominates $a_{i*}$ and if some criteria $g_{j} \in F'$ exist such as $d_{j}(a_{i*}, a_{i}) \in ]I_{j}^{L}, I_{j}^{U}[$ , we ask the DM a (Q.2) type question for each of these criteria. For the criteria that the DM deems $d_{j}(a_{i*}, a_{i})$ not to be significant (n.s.), this $d_{j}(a_{i*}, a_{i})$ becomes the new lower bound for $I_{j}$ , and for those for which he deems $d_{j}(a_{i*}, a_{i})$ to be significant (s.), this $d_{j}(a_{i*}, a_{i})$ becomes the new upper bound for $I_{j}$ . If the system verifies that we have $d_{j}(a_{i*}, a_{i}) \leqslant I_{j}^{L}$ for all the criteria $g_{j} \in F'$ , then the DM is warned about an incoherency in his answers and we ask him a (Q.1) type question. His response to Q.1 becomes his new revealed preference for the pair $(a_{i}, a_{i*})$ ; if there is still an incoherency, another pair of alternatives is chosen. In the context of this same pair of responses, if at least one criterion $g_{j} \in F''$ exists such as $d_{j}(a_{i}, a_{i*}) \geqslant I_{j}^{U}$ , the system will not detect an incoherence but will not obtain any additional information concerning the values of the unknown parameters.

Again, in the framework of a (“Yes”, “No”) answer, after the system has verified that there is no dominance, suppose that it exists some $g_{j} \in F'$ such as $|d_{j}(a_{i}, a_{i*})| \geqslant I_{j}^{U}$ and that these $d_{j}(a_{i*}, a_{i})$ do not all have the same sign. If, for all these $g_{j}$ , we have $|d_{j}(a_{i}, a_{i*})| < D_{j}^{U}(2)$ , then the “Yes” in P.1 is interpreted as a strong outranking such that we have:

$$
\sum_ {j \in J ^ {(-)}} \pi_ {j} \geqslant \sum_ {j \in J ^ {(-)}} \pi_ {j};\tag{1}
$$

$$
\mathrm{c} \left(\mathrm{a} _ {\mathrm{i}}, \mathrm{a} _ {\mathrm{i} ^ {*}}\right) \geqslant \mathrm{C} _ {1},
$$

where

(2)

$$
\mathrm{c} \left(\mathrm{a} _ {\mathrm{i}}, \mathrm{a} _ {\mathrm{i} ^ {*}}\right) = \sum_ {\mathrm{j} \in \mathrm{J} ^ {(+)} \cup \mathrm{J} ^ {(-)}} \pi_ {\mathrm{j}}\tag{3}
$$

and

$$
\mathbf {J} ^ {(+)} \left(a _ {i}, a _ {i ^ {*}}\right) = \left\{g _ {j} \in \mathbf {F} ^ {\prime} \mid g _ {j} \left(a _ {i}\right) > g _ {j} \left(a _ {i ^ {*}}\right) + I _ {j} ^ {L} \right\};
$$

$$
\mathbf {J} ^ {(-)} \left(a _ {i}, a _ {i ^ {*}}\right) = \left\{g _ {j} \in \mathbf {F} ^ {\prime} \mid g _ {j} \left(a _ {i}\right) <   g _ {j} \left(a _ {i ^ {*}}\right) - I _ {j} ^ {L} \right\};\tag{4}
$$

$$
\mathbf {J} ^ {(=)} \left(a _ {i}, a _ {i ^ {*}}\right) = \left\{g _ {j} \in \mathbf {F} ^ {\prime} \mid | g _ {j} \left(a _ {i}\right) - g _ {j} \left(a _ {i ^ {*}}\right) \leqslant I _ {j} ^ {I} \right\};
$$

and thus $\mathrm{MIN}\{\mathrm{c}(\mathrm{a}_{i},\mathrm{a}_{j*}),\mathrm{C}_{1}^{\mathrm{U}}\}$ becomes a new upper bound for $C_{1}$ . Also we should have

$$
\mathrm{d} _ {\mathrm{j}} \left(\mathrm{a} _ {\mathrm{i}}, \mathrm{a} _ {\mathrm{i} ^ {*}}\right) \leqslant \mathrm{D} _ {\mathrm{j}} (2), \text { for   all } \mathrm{g} _ {\mathrm{j}} \in \mathbf {F} ^ {\prime},\tag{5}
$$

and thus MAX $\{d_{j}(a_{i},a_{i*}),D_{j}^{L}(2)\}$ becomes the new lower bound for $D_{j}(2)$ , where

$$
\mathrm{d} _ {\mathrm{j}} \left(\mathrm{a} _ {\mathrm{i}}, \mathrm{a} _ {\mathrm{i} ^ {*}}\right) = \mathrm{g} _ {\mathrm{j}} \left(\mathrm{a} _ {\mathrm{i} ^ {*}}\right) - \mathrm{g} _ {\mathrm{j}} \left(\mathrm{a} _ {\mathrm{i}}\right).\tag{6}
$$

If, among these $g_{j}$ , the system finds at least one for which $d_{j}(a_{i}, a_{i*}) \geqslant D_{j}^{U}(2)$ , the DM is asked a $(Q.3)$ type question for each one of these $g_{j}$ . On the one hand, the differences $d_{j}(a_{i}, a_{i*})$ that the DM deems to be not big enough (n.b.e.) become the new lower bounds for $D_{j}(2)$ . On the other hand, if one (or more) of these differences is considered by the DM to be big enough (b.e.), an incoherence is brought to his attention and the system then ask him a $(Q.1)$ type question. It should be noted that other inconsistencies may be observed and other information may be obtained from the responses (“Yes”, “No”).

From the pair of responses (“Yes”, “Yes”), we obtain, among other things, information concerning the concordance threshold $C_{3}$ . If the system verifies that there is no dominance and that for all $g_{j} \in F''$ , we have $|d_{j}(a_{i}, a_{i*})| < D_{j}^{U}(2)$ and that these $d_{j}(a_{i}, a_{i*})$ do not have the same sign, then the pair of responses (“Yes”, “Yes”) is interpreted as two weak outranking. Consequently, we have $|d_{j}(a_{i}, a_{i*})| \leqslant D_{j}(2)$ for all $g_{j} \in F'$ and MAX $\{|d_{j}(a_{j},a_{i*})|,D_{j}^{U}(2)\}$ becomes a new lower bounds for $D_{j}(2)$ . Also

$$
\sum_ {j \in J ^ {(+)}} \pi_ {j} \approx \sum_ {j \in J ^ {(-)}} \pi_ {j};\tag{7}
$$

$$
\mathrm{c} \left(\mathrm{a} _ {\mathrm{i}}, \mathrm{a} _ {\mathrm{i} ^ {*}}\right) \geqslant \mathrm{C} _ {3} \text {   and   } \mathrm{c} \left(\mathrm{a} _ {\mathrm{i} ^ {*}}, \mathrm{a} _ {\mathrm{i}}\right) \geqslant \mathrm{C} _ {3};\tag{8}
$$

thus MIN{min[c(a\_i,a\_i\*),c(a\_i,a\_i\*)],C\_3^U} becomes a new upper bound for C\_3. The system performs the same type of analysis for the eight pairs of possible responses (for more details, see Martel and Nadeau [7]). All this information is used to calculate the parameters of ELECTRE II.

![](/api/attachments/GGYB2579/fulltext/images/611315cc564d0c452be544cf5b572256f9f70d6147054eabcfc5982f6b2311cd.jpg)  
Fig. 1. Schema of the algorithm.

## 2.3. Phase 3: first calculation stage

The system proceeds with the first calculation stage after having gathered information from the first dialogue between it and the DM. This first stage is made up of two parts: obtaining the first set of parameters and obtaining an initial ranking of alternatives in A'.

Following the dialogue phase, for each of the parameters $I_{j}, D_{j}(2)$ , $C_{1}$ and $C_{3}$ , we have intervals with values $[I_{j}^{L}, I_{j}^{U}]$ , $[D_{j}^{L}(2), D_{j}^{U}(2)]$ , $[C_{1}^{L}, C_{1}^{U}]$ and $[C_{3}^{L}, C_{3}^{U}]$ respectively. As a precaution, we have decided to keep as the first set of parameters $I_{j} = I_{j}^{L}$ , $D_{j}(2) = D_{j}^{L}(2)$ , $C_{1} = C_{1}^{U}$ and $C_{3} = C_{3}^{U}$ . From these values for $I_{j}$ , $D_{j}(2)$ , $C_{1}$ and $C_{3}$ , the values of $D_{j}(1)$ and $C_{2}$ are extracted as follows:

$$
\mathrm{D} _ {\mathrm{j}} (1) = \frac {\mathrm{D} _ {\mathrm{j}} (2) + \mathrm{I} _ {\mathrm{j}}}{2} \text { and } \mathrm{C} _ {2} = \frac {4 \mathrm{C} _ {1} + 5 \mathrm{C} _ {3}}{9}.\tag{9}
$$

In reality, the values for $C_{1}$ and $C_{3}$ cannot be established until the values of the weights $\pi_{j}$ are determined (see conditions (2) and (8)). In the dialogue phase we obtain a set of inequalities where the weights $\pi$ are implicated. These inequalities form a convex polyhedron of the sets of weights which satisfy the preferences revealed by the DM. Even if any set of weights which is inside that polyhedron necessarily satisfies the DM's preferences, we think that is appropriate to choose in the polyhedron a set of central weights (a concept used by Solymosi and Dombi [9]): this set of central weights represents, in a way, the polyhedron's center of gravity (centroid). The algorithm that we have developed to determine those central weights is briefly presented in section 3.2. Even if this set of weights is only one of the possible sets, it should be representative and robust. Moreover, if it happens that the polyhedron is empty, we assess equal weight to each criterion. The DM will have the opportunity of changing those weights if they are not consistent with his preferences.

Once the system has calculated initial values for all parameters $I_{j}$ , $D_{j}(1)$ , $D_{j}(2)$ , $C_{1}$ , $C_{2}$ , $C_{3}$ and $\pi j$ , it constructs the outranking relations (strong and weak) according to ELECTRE II with indifference thresholds; then it ranks the alternatives of the reference set A'. In fact, the system gives three rankings (direct, inverse and quasi-median).

2.4. Phase 4: new dialogue and new calculation stage

Once an initial ranking of A' and an initial set of values for the key parameters is obtained in the previous phase, the system then proceeds to the final phase after having presented this ranking and this set of values to the DM. This phase has two stages: a new dialogue and a new calculation. It should be noted that each of these stages can be repeated several times and each repetition of either one of these two stages constitutes an iteration of the system. In order to get a better picture of the final phase of our DSS, one can refer to Fig.1.

Presented with the initial ranking of the set A' and the set of parameters obtained from the previous phase, the DM can declare himself:

· with regard to the ranking of A'

\- in agreement,

\- not in agreement;

\- with regard to the values of parameters,

\- in agreement,

\- not in agreement.

When we say that he is in agreement, we mean that he declares that there is agreement between the obtained results and his preferences.

\- If the DM does not agree with the ranking of $\mathbf{A}'$ or with the values obtained for the parameters, he can then modify one or several of these values as he wishes. This modification can affect: the weights $\pi_j$ , the indifference thresholds $I_j$ , the discordance thresholds $D_j(1)$ and $D_j(2)$ , the concordance thresholds $C_1$ , $C_2$ and $C_3$ . Following that modification, there is a new calculation stage and the system proceeds with a new ranking of $\mathbf{A}'$ based on the modified parameters. The system then asks the DM again if he agrees or not with the new ranking obtained for $\mathbf{A}'$ . If he does not agree, he can once again modify one or several of the parameters and the system will give a new ranking of $\mathbf{A}'$ . If, after several iterations, the disagreement persists, the DM can (as shown in Fig.1) return to the initial phase of the algorithm. If he agrees with the ranking of $\mathbf{A}'$ , he can proceed to the final stage which consists of ranking $\mathbf{A}$ .

\- If the DM agrees with the ranking of $\mathbf{A}'$ and with the values of the parameters, he then advances to the final stage which consists of ranking the set $\mathbf{A}$ of all the possible alternatives. If, on the one hand, the DM agrees with the ranking of $\mathbf{A}$ , the process ends and we can conclude that we have succeeded in adequately modelling the DM's preference structure. If, on the other hand, he does not agree with the ranking obtained for $\mathbf{A}$ , he has the choice of (see Fig. 1) modifying one or several parameters and obtaining a new ranking of $\mathbf{A}$ , selecting two new subsets $\mathbf{A}'$ and $\mathbf{F}'$ , or quitting the system.

## 3. Presentation of the ELECCALC system

## 3.1. General structure

The ELECCALC system is a conglomerate of several aggregate programs whose intelligent junction assures the efficient use of the computer's total power. Thanks to the possible access paths to the extended memory, the ELECCALC system offers a multiple criteria decision support tool which is fast as well as clear and user-friendly; in this support tool, the commands for chaining the programs are either generated automatically according to some algorithmic procedures or executed by the user himself. In this section, we will first look at how the system works. The interconnections of the aggregate programs involved in ELECCALC are carried out as shows in the operator schema (Kiss [5]) of Fig.2. In this schema, the upper-left hand indexes represent the origin(s) of the command, the upper-right hand indexes indicate the destination(s) of the command and the lower-right hand indexes represent the logical numbers of the aggregate programs.

The following is a brief description of the functional role of each of the aggregate programs:

$A_{1}$ - A service program called directly by the user, enabling him to change the default access path to the files. The user is advised to use this program if a virtual disk has already been defined.

$\mathbf{A}_2$ - Initially called by $\mathbf{A}_1$ , and then by $\mathbf{A}_3, \mathbf{A}_5$ , $\mathbf{A}_6, \mathbf{A}_8, \mathbf{A}_{10}$ and $\mathbf{A}_{13}$ , this aggregate program supervises the global functioning of the system and enables managing of the data base (creation, deleting, maintenance) as well as preparing the selection(s) (alternatives, criteria) and the dialogue between the user and the computer. It alternately transmits a command to $\mathbf{A}_3, \mathbf{A}_4, \mathbf{A}_5$ or to the operational system according to user's choice.

$A_{3}$ – Called by $A_{2}$ , this aggregate program enables the user to rapidly choose a subset of alternatives and of criteria (by presenting an overall view of the data base) which will then constitute the principal basis of the dialogue between the user and the computer. Once this subset is selected, the command is transmitted to $A_{4}$ or to $A_{2}$ .

![](/api/attachments/GGYB2579/fulltext/images/5b8f735239ffeb7b877a9d7d65554502b9dca1001236e0741ccdf0649a5981e7.jpg)  
Fig. 2. Synopsis of the interconnections of the aggregate programs.

$A_{4}$ - After having received the command from $A_{3}$ or directly from $A_{2}$ , this program, taking the size of the selected subset into account, rapidly traces a parametrized screen mask for the dialogue and save it in binary form and then transmits the command to $A_{6}$ .

$\mathbf{A}_5$ - Called by $\mathbf{A}_2$ , this aggregate program offers the user the possibility to create a new data file or to modify an existing file. Thanks to scrolling toroidal windows, the user can easily move around within the large selection of data. At the end of this option, the command is transmitted to $\mathbf{A}_2$ . $\mathbf{A}_6$ - This aggregate program manages the dialogue between the user and the computer and makes up the heart of the system. It has several windows displayed simultaneously to allow the maximum amount of pertinent information to be displayed at all times and in order to aid the DM as much as possible in expressing his preferences. It is, in fact, a sort of subjugated system where the process evolves by continually comparing the user's responses with the set of values recorded as the performances in the reference set and with the indifference, concordance and discordance thresholds. Naturally, the user can abandon or end the dialogue at any time. In the first case, the command is transmitted to $\mathbf{A}_2$ and in the second case, the command is transmitted to $\mathbf{A}_7$ .

$A_{7}$ - An interface program between $A_{6}$ and $A_{8}$ with its main objective being to define the mathematical constraints which are verified by the weights of the criteria and to generate the initial simplex table which will be used to determine those weights.

$A_{8}$ - An aggregate program whose role is to determine a set of weights of the criteria by using a procedure which locates the centroid of a convex polyhedral set. Once the evaluation is completed, the command transmitted to $A_{9}$ .

$A_{9}-$ By virtue of the files created by $A_{6}$ and $A_{8}$ , this aggregate program determines the weak and strong outranking relations between the alternatives involved in the subset A'. We then continue on to $A_{10}$ .

$A_{10}$ - Called alternately by $A_{9}$ or by $A_{12}$ , this aggregate program uses a direct and inverse transitive closing procedure to detect the eventual presence of circuits in the graph associated with the outranking matrix and then transmits the command to $A_{11}$ or to $A_{13}$ .

$A_{11}$ – Called by $A_{10}$ , this aggregate program, after having ranked the alternatives of the subset $A'$ (in view of direct, quasi-median and inverse outranking relations), enables a new dialogue once again between the user and the computer where the user can modify the weights of the criteria, the indifference, discordance and concordance thresholds. The command is transmitted to $A_{9}$ or $A_{12}$ depending on what is analyzed by the user is the subset $A'$ or the entire set A.

$A_{12}$ - Its function is identical to that of $A_{9}$ but the outranking relationships are determined this time with regard to the entire set A. After, we proceed to $A_{10}$ to detect the eventual presence of circuits in the graph associated with the outranking matrix.

$A_{13}$ – Selected by $A_{10}$ , this aggregate program ranks all the alternatives recorded in the data base and displays a ranking table depending on the key chosen by the user (that is to say direct, quasi-median or inverse). Moreover, it presents an overall view of the hierarchy of the alternatives by drawing a decomposed graph, thanks to the use of a large scrolling virtual screen. Following this (these) ranking(s), the command is transmitted to $A_{2}$ either to quit the ELECCALC system or to begin a new processing once again.

## 3.2. Specific elements of the system

We will now present some mathematical-algorithmic devices which constitute the most important specific elements of our system: the global comparison of the alternatives, the search of a central set of weights for the criteria, the ranking procedure for the alternatives.

Global comparison of the alternatives (dialogue phase)

In program $A_{6}$ which governs the dialogue phase, we proceed with the global comparison of the alternatives in pairs in the following manner:

$$
\left(a _ {i} \rightleftharpoons a _ {i ^ {*}}) = \left(\omega_ {1}; \omega_ {2}\right) _ {r}; a _ {i}, a _ {i ^ {*}} \in A ^ {\prime};
$$

$$
\begin{array}{l} \mathrm {i, i^ {*} = 1,2,\ldots,m; i\neq i^ {*}}; \\ (\omega_ {1}; \omega_ {2}) _ {\mathrm{r}} \in \Omega = \left\{\left(\omega_ {1}; \omega_ {2}\right) _ {\mathrm{r}} | \omega_ {1}, \omega_ {2} \in \{Y; N; I \}; \right. \\ \mathrm {r = 1,2,\ldots,3^ {2}} \} \end{array}
$$

Depending on the result of his comparison, the system proceeds with a certain number of verifications or operations:

\- Dominance control (D) regarding the pair of actions which are to be compared:

$$
\mathbf {a} _ {\mathrm{i}} \mathbf {D} \mathbf {a} _ {\mathrm{i} ^ {*}}
$$

$$
\exists \mathbf {g} _ {i} \in \mathbf {F} ^ {\prime}
$$

$$
\mathrm{d} _ {\mathrm{i}} \left(\mathrm{a} _ {\mathrm{i}}, \mathrm{a} _ {\mathrm{j} ^ {*}}\right) \leqslant 0, \forall \mathrm{j}, \mathrm{j} = 1, 2, \dots , \mathrm{n};
$$

$$
_ {i} \left(a _ {i}, a _ {i ^ {*}}\right) <   0;
$$

$$
\mathrm{a} _ {\mathrm{i}} * \mathbf {D} \mathrm{a} _ {\mathrm{i}}, \text {   if   } \mathrm{d} _ {\mathrm{j}} (\mathrm{a} _ {\mathrm{i}} *, \mathrm{a} _ {\mathrm{i}}) \geqslant 0, \forall \mathrm{j}, \mathrm{j} = 2, \dots , \mathrm{n};
$$

$$
\in \mathbf {F} ^ {\prime}
$$

$$
\exists \mathrm{g} _ {\mathrm{j}}
$$

$$
\mathrm{d} _ {\mathrm{i}} \left(\mathrm{a} _ {\mathrm{i}}, \mathrm{a} _ {\mathrm{i} ^ {*}}\right) > 0;
$$

\- else, no dominance, that is $a_i \overline{\mathbf{D}} a_{i*}$ and $a_{i*} \overline{\mathbf{D}} a_{i*}$ .  
- Compensation control, if $a_i \overline{\mathbf{D}} a_{i*}$ and $a_{i*} \overline{\mathbf{D}} a_{i*}$ :

\- no compensation, if $\Delta p_j > 0$ ; $\forall j, j = 1,2,\ldots,n$ , or if $\Delta p_j < 0$ ; $\forall j, j = 1,2,\ldots,n$ ; where $\Delta p_j = f((\omega_1;\omega_2)_r) = \{d_j(a_i,a_{i*}), \text{ or } |d_j(a_i,a_{i*})|$ , or $d_j(a_{i*},a_i)$ ;

\- else, there is compensation.

\- Immediate analysis of the characteristic values with regard to the results of both preceding controls.

\- Systematic generation of a series of questions in accordance with the responses $(\omega_{1};\omega_{2})_{\mathrm{r}}$ of the user and with regard to the preceding analysis in order to stimulate the reformulation of $(\omega_{1};\omega_{2})_{\mathrm{r}}$ or the readjustment of the vectors I, D, $\mathbf{C}_1$ and $\mathbf{C}_3$ with 2n components.

Following this initial control stage, the system records the user's responses to the questions which may have been asked in the last step of this phase by using an alphanumerical vector $\Lambda$ , which is defined as follows:

$$
\Lambda = \left\{\lambda_ {j} (a _ {i}, a _ {i ^ {*}}) \mid \lambda_ {j} \in \{Y; N \}; j = 1, 2, \dots , n \right\}.
$$

The system then makes an on-line readjustment of the current values of the indifference thresholds I or the discordance thresholds $D_{j}(2)$ in the vectors I and D respectively, where

$$
\begin{array}{l} \mathbf {I}, \mathbf {D} = \Gamma_ {\S} \left(\Delta p _ {j}, \left(\omega_ {1}; \omega_ {2}\right) _ {r}, \Lambda , | (a _ {i}, a _ {i ^ {*}}); \right. \\ \quad j = 1, 2, \dots , n) \end{array}
$$

and

## $\Gamma_{\S} =$ a collection of rules and procedures

for the readjustment of I and D.

Searching the weights of the criteria

While it adjusts the current values of the parameters $I_{j}$ , $D_{j}(2)$ , $C_{1}$ and $C_{3}$ , the system also updates a set of indexes' pointers whose the final states determine a set of inequalities which serve to evaluate the weights of the criteria. At the end of the dialogue stage, the system calculates the weights $\pi_{j}$ , $j = 1, \ldots, n$ , of the criteria by activating programs $A_{7}$ and $A_{8}$ . In fact, the obtained inequalities define a convex polyhedron: all the sets of weights in this polyhedron necessarily satisfy the preferences revealed by the DM. As noted previously, we have developed an algorithm enabling us to determine a set of central weights which represents the center of gravity of this polyhedron.

Suppose that the dialogue has generated T inequalities. For each inequality, we associate the hyperplane

$$
\mathrm{k} _ {\mathrm{t} 1} \pi_ {1} + \dots + \mathrm{k} _ {\mathrm{tj}} \pi_ {\mathrm{j} +} \dots + \mathrm{k} _ {\mathrm{tn}} \pi_ {\mathrm{n}} = 0\tag{10}
$$

in the space $\mathbb{R}^{\mathrm{n}}$ , with $k_{\mathrm{tj}} = -1, 0$ or $1; t = 1,2,\ldots,T$ and $j = 1,2,\ldots,n \leqslant N$ . From the condition $\pi_{n} = 1 - \sum_{j=1}^{n-1} \pi_j$ , those hyperplanes are transformed in the space $\mathbb{R}^{n-1}$ and we obtain:

$$
\kappa_ {t 1} \pi_ {1} + \dots + \kappa_ {t j} \pi_ {j} + \dots + \kappa_ {t n - 1} \pi_ {n - 1} - b _ {t} = 0\tag{11}
$$

Written in the normalized form, (11) becomes: $\gamma_{t1}\pi_{1} + \gamma_{t2}\pi_{2} + \ldots + \gamma_{tj}\pi_{j} + \ldots$

$$
+ \gamma_ {\mathrm{tn-1}} \pi_ {\mathrm{n-1}} - \beta_ {\mathrm{t}} = 0\tag{12}
$$

where $\gamma_{\mathrm{tj}}$ is the directional cosine in $\mathbb{R}^{n - 1}$ , that is

$$
\gamma_ {\mathrm{tj}} \equiv \cos \alpha_ {\mathrm{tj}} = \frac {\kappa_ {\mathrm{tj}}}{\left(\sum_ {j = 1} ^ {\mathrm{n} - 1} \kappa_ {\mathrm{t} j} ^ {2}\right) ^ {1 / 2}}; \beta_ {\mathrm{t}} = \frac {\mathrm{b} _ {\mathrm{t}}}{\left(\sum_ {j = 1} ^ {\mathrm{n} - 1} \kappa_ {\mathrm{t} j} ^ {2}\right) ^ {1 / 2}},
$$

and $(\sum_{j=1}^{n}\kappa_{t,j}^{2})^{1/2}$ is the euclidean norm of the coefficients.

Consequently, the euclidean distance $\delta_{t}$ between the sought-after center of gravity $\mathbf{M}(\pi_{1}^{(*)};\pi_{2}^{(*)};\ldots ;\pi_{j}^{(*)};\ldots ;\pi_{n - 1}^{(*)})$ and the $t^{\text{th}}$ hyperplane is defined as

$$
\delta_ {t} \left[ \mid \gamma_ {t 1} \pi_ {1} ^ {(*)} + \gamma_ {t 2} \pi_ {2} ^ {(*)} + \dots + \gamma_ {t j} \pi_ {j} ^ {(*)} + \dots \right.
$$

$$
+ \gamma_ {t n - 1} \pi_ {n - 1} ^ {(*)} - \beta_ {t} |.\tag{13}
$$

The problem then is to find $\mathbf{M}(\pi_{1}^{(*)};\pi_{2}^{(*)};\ldots;\pi_{j}^{(*)};\ldots;\pi_{n-1}^{(*)})$ such that $\delta_{1}\approx\delta_{2}\approx\ldots\approx\delta_{t}\approx\ldots\approx\delta_{T}=\delta$ , which is obtained by solving the following linear program:

$$
\left. \begin{array}{l} \text {Max} \delta \\ \text {subject to} \\ \delta + \sum_ {j = 1} ^ {n - 1} \gamma_ {t j} \pi_ {j} \leqslant \beta_ {t}; t = 1, 2, \dots T \\ \delta - \pi_ {j} \leqslant 0; j = 1, 2, \dots n - 1 \\ \delta + \pi_ {j} \leqslant 1; j = 1, 2, \dots , n - 1 \\ \delta \geqslant 0 \end{array} \right\}\tag{14}
$$

The solution of (14) gives $(\pi_{1}^{(*)};\pi_{2}^{(*)};\ldots;\pi_{j}^{(*)};\ldots;\pi_{n-1}^{(*)})$ and using $\pi_{n}^{(*)}=1-\sum_{j=1}^{n-1}\pi_{j}^{(*)}$ , we obtain a set of weights verifying the DM's revealed preferences.

## Ranking of the alternatives

Once the dialogue phase ends and the parameters have been determined, the system constructs the outranking matrix for $\mathbf{A}'$ or for $\mathbf{A}$ ( $\mathbf{A}_9, \mathbf{A}_{12}$ ). When an outranking matrix $\mathbf{H}$ is used to obtain a ranking of $\mathbf{A}'$ or of $\mathbf{A}$ ( $\mathbf{A}_{11}$ ), it is important to use a procedure to detect possible circuits in the graph associated with this matrix ( $\mathbf{A}_{10}$ ). To do this, we use an aggregative isolation procedure to section the graph associated with the matrix $\mathbf{H}$ . This sectioning is done in classes of vertexes which form strong maximally related subgraphs by using the following method which is both simple and easily programmable: based on the fact that the equivalence class of a vertex $a_i$ is defined by the intersection between the set of the vertexes which can be arrived at, starting from $a_i$ (i.e. direct transitive closing) and the set of the vertexes from which $a_i$ can be arrived at (i.e. indirect transitive closing), a circuit is detected if this intersection is not empty. Let denoted by $\psi_h\{a_i\}$ this intersection, i.e. the $h_{th}$ strong maximally related subgraph; the final value of $h$ gives the number of equivalence classes, $h \leqslant m$ . After having carried out the procedure to detect circuits, the outranking between the equivalence classes are naturally recalculated and thus creating the matrix $\mathbf{H}_{[h \times h]}'$ of the revised outranking, $\mathbf{H}_{[h \times h]}'\subseteq H_{[m \times m]}$ . To obtain a ranking of $\mathbf{A}'$ or of $\mathbf{A}$ ( $\mathbf{A}_{11}, \mathbf{A}_{13}$ ), an aggregative decomposition procedure (Kiss and Martel [6]) is used. This consists of locating and sequentially separating the vertexes of the graph $\Psi_{[h]}(\psi_{h_{1}}\{a_{i_{1}}\},O)$ , $i_{1}=1,\ldots,\xi_{h_{1}}$ , $h_{1}=1,\ldots,h$ , $h\leqslant m$ , associated with the matrix $\mathbf{H}_{[h\times h]}^{\prime}$ whose the outside half degrees $d_{\Psi}^{+}$ are zero and the inside half degrees $d_{\Psi}^{-}$ are not necessarily non-zero, where $\xi_{h_{1}}$ is the number of vertexes (i.e. alternatives) classed in an $h_{1}^{th}$ equivalence class created by the detection procedure of the circuits ( $h_{1}=1,2,\ldots,h$ ). Within ELECCALC, this procedure gives a direct decomposition $\mathbf{D}^{\rightarrow}$ from the graph $\Psi_{[h]}(\psi_{h_{1}}\{a_{i_{1}}\},O)$ , an inverse decomposition $\mathbf{D}^{-}$ from the graph $\Psi_{[h]}^{\prime}(\psi_{h_{1}}\{a_{i_{1}}\},O^{-1})$ and a quasi-median decomposition $\stackrel{\rightarrow}{\to}\mathbf{D}^{\leftarrow}$ . It should be noted that is difficult to define a general rule which enables the median criterion to be determined as far as the quasi-median decomposition is concerned. In ELECTRE II, for example, simply half the distance of the changes in the direct and inverse hierarchical positions of each of the alternatives is taken. To further maintain the isomorphism between the outranking obtained and the one proposed, we have endeavoured to define a median rule which allows to construct a hierarchical structure “somewhere” halfway between the direct and inverse decomposition, while respecting the outranking relations between the alternatives. Kiss and Martel [6] have developed several corollaries showing the multiplicity of hierarchical decompositions stemming from the same preference relations system.

With regard to that quasi-median decomposition, suppose that the m alternatives, grouped into h equivalence classes, were decomposed into n hierarchical levels which contain $\eta_{1}, \eta_{2}, \ldots, \eta_{\nu}$ equivalence classes respectively, that is we have

$$
\bigcup_ {i = 1} ^ {m} a _ {i} = \bigcup_ {h _ {1} = 1} ^ {h} \left(\bigcup_ {i _ {1} = 1} ^ {\xi_ {h _ {1}}} \psi_ {h 1} [ i _ {1} ]\right) = \bigcup_ {r = 1} ^ {r} \left(\bigcup_ {r _ {1} = 1} ^ {\eta_ {r}} \mathscr {D} _ {r [ r _ {1} ]}\right)
$$

$$
\text { and } \sum_ {r = 1} ^ {v} \eta_ {r} = \sum_ {h _ {1} = 1} ^ {h} \xi_ {h _ {1}} = m.
$$

To construct a quasi-median decomposition, first we determine the median hierarchical level(s) and then we try to contract the obtained decomposition by converging the elements of other levels on this (these) median hierarchical level(s) while respecting the outranking relations. We, therefore, have

$$
\mathcal {D} _ {M e} = \left\{ \begin{array}{l l} \mathcal {D} _ {\nu + 1 / 2}, & \text { if } \nu \text { is   odd }; \\ \mathcal {D} _ {\nu / 2} \cup \mathcal {D} _ {\nu / 2 + 1}, & \text { if } \nu \text { is   even }; \mathcal {D} _ {M e} \in \mathbf {D} \end{array} \right..
$$

![](/api/attachments/GGYB2579/fulltext/images/c65cb22e4c428cbeadad8d099f9539b6990ce356ce490342cefa582608e8380e.jpg)  
Fig. 3. Contraction of an uneven $\nu$ level decomposition.

and the contraction procedure works as showed in Figs. 3 and 4, with $\vec{\mathbf{D}}^{\leftarrow} = f_{\S}(\mathbf{D}^{\rightarrow})$ , when $f_{\S}$ is a logic-algorithmic family of routines and rules for contracting the direct decomposition $\mathbf{D}^{\rightarrow}$ . The same procedure, based on the inverse decomposition $\mathbf{D}^{\leftarrow}$ is used, but it does not necessarily lead to the same quasi-median decomposition. Note that the quasi-median decomposition cannot be carried out if $\nu \leqslant 2$ .

## 4. Didactical example

In order to illustrate how our software practically works, we briefly present a small didactical example: the decision problem consists of choosing a car among a set of ten cars which are evaluated relatively to eight criteria: aesthetics, equipment, interior space, comfort, performance, road-holding, security and price. The scores of the ten cars (which are sold on the canadian market) relatively to these criteria are given in Fig. A.3 of the appendix (from Duquette and Lachapelle, 1991). At the first the DM is asked to choose a reference set of cars and a subfamily of the criteria which he judges pertinent. Let us suppose that the DM chooses four cars in his reference set: Chevrolet Lumina ( $a_{1}$ ), Plymouth

Acclaim $(a_{2})$ , Volkswagen Passat $(a_{3})$ and Hyundai Sonata $(a_{4})$ . Among the eight criteria, he takes aesthetics, equipment, performance, holding and price. The reduced matrix including those four cars evaluated relatively to those five criteria is presented in Fig. A.4 of the appendix.

Now, from that reduced matrix, a dialogue between the DM and the system begins in order to enable the DM to reveal his preferences relatively to the reference set and after to enable the system to calculate values for the weights and the indifference, concordance and discordance thresholds. In that dialogue, relatively to each pair $(a_{i}, a_{i^{*}})$ of cars of the reference set, where $i, i^{*} = 1, \ldots, 4$ ; $i \neq i^{*}$ , the DM has to give an answer to the pair of propositions (P.1, P.2). For example, for the pair $(a_{1}, a_{2}) = (\text{Chevrolet, Plymouth})$ , he can answer “I don’t know” (I, i.e. ignorance) to P.1 and “Yes” (Y) to P.2 (see Fig. A.5 of the appendix). If there is incoherence between the answers of the DM and the scores of those two cars, the system asks the DM whether he wants to revise his answers; if there is coherence, the system can ask some supplementary questions to the DM about the observed differences between the scores of those cars relatively to some criteria: that additional information is used by the system to readjust the values of the thresholds. Because, in our case, the reference set contains four cars, the system can ask the DM to evaluate six possible pairs of cars: obviously, the DM is never forced to make all the six comparisons.

![](/api/attachments/GGYB2579/fulltext/images/594b985a98c30620b74d03e5553ff3c1aebadf67793a41e5e291e8ee12b5be8c.jpg)  
Fig. 4. Contraction of an even $\nu$ level decomposition.

In our example, we suppose that the DM accepts to make the six possible comparisons: at each one of the propositions P.1 and P.2, he can answer “Yes” (Y), “No” (N) or “I don’t know” (I). Relatively to the pairs of cars $(a_{1},a_{2})$ , $(a_{1},a_{3})$ , $(a_{1},a_{4})$ , $(a_{2},a_{3})$ , $(a_{2},a_{4})$ and $(a_{3},a_{4})$ , let us suppose that his answers to (P.1, P.2) have been successively: (I,Y), (N,Y), (N,Y), (N,I), (I,Y) and $_{j}(Y,N)$ . Obviously, following some of those answers the system has asked some supplementary questions about the differences between the scores relatively to some criteria. So, for example, as one can see in Fig. A.5 of the appendix, after that the DM answers (I,Y) to (P.1, P.2) relatively to the pair of cars $(a_{1},a_{2})$ , the system asks the DM whether he judges that a difference 1.5 on the criterion “equipment” is significant or not: his answer will use to readjust the indifference threshold of this criterion. Taking into account the revealed information, the system can calculate a first set of weights for the criteria which is presented in Fig. A.6 of the appendix; it also obtains a first set of values for the concordance, indifference and discordance thresholds which are presented in Fig. A.7 and Fig. A.8 of the appendix. At this time, if he wishes, the DM can modify any one of those weights and/or thresholds. Suppose that he accepts the obtained values, then the system obtains a partial order of the reference set: here this order is from the most preferred to the last preferred car: $(a_{3})$ , $(a_{4}/a_{2})$ and $(a_{1})$ (see Fig. A.9 of the appendix). If the DM is in agreement with this order, the system can put in order all the cars which are included in the data set by using a direct, a quasi-median (see Fig. A.10 of the appendix) and an indirect ordering. In our example, those three orders coincide and are presented in Fig. A.11 of the appendix: as we can see, the most preferred cars are the Volkswagen Passat and the Honda Accord and the less preferred car is the Chevrolet Lumina, whereas the other cars are shared between the second and the third equivalence classes. Obviously, in that small example, we have illustrated only same possibilities of our software. Many other interactions between the DM and the system are possible: for example, the DM can again define a new reference set, a new subfamily of criteria and so on.

## 5. Concluding remarks

As one can see in particular in the figures of the appendix, ELECCALC is a very user-friendly tool. Each phases of the algorithm is illustrated by many graphical presentations, which are well adapted to visualise the involved information. For example, the weights of the criteria are illustrated by a pie-diagram where each sector is proportional to the $\pi_{j}$ value that this sector represents (see Fig. A.6 of the appendix). Each one of the parameters $I_{j}$ , $D_{j}(2)$ , $C_{1}$ and $C_{3}$ is graphically illustrated by arrows on a line segment: the length of this segment is directly proportional to the range of the illustrated parameter, as one can visualise in Fig. A.7 and Fig. A.8 of appendix. For example, a modification of the $I_{j}$ threshold value produces an immediate move of the corresponding arrow on the line segment which graphically represents this threshold. Furthermore, the system provides the DM with a logical support such a way that the needed relations between the magnitudes of the involved parameters are always respected.

As shown in the schema of Fig.1, the system is very flexible. The user is free not only to modify his answers in the first dialogue phase and the parameters' values in the new dialogue stage of the last phase, but also to change again the parameters' values after that the alternatives of A have been ranked, if he disagrees with this last ranking. When the DM is asked a question, he is never compelled in his response; not only it is possible for him to answer "I don't know" to a question about his global preferences, but also the system does not persist in obtaining another response for him, if an incoherence occurs again. Furthermore, the scrolling toroidal windows add a flexible support because they provide a lot of pertinent information during the dialogue steps.

Thanks to a good integration of many mathematical algorithmic devices and to a well organised sequencing of diverse aggregate programs, our software provides the DM with a very fast and efficient support. In order to obtain a quick performance, we have used the mixed programming technique (Microsoft C, Microsoft Assembler, Microsoft QuickBASIC 4.5). The ELECCALC software package runs on a IBM PS/2 micro-computer or compatible. It uses the MS DOS 3.3 (or higher) and needs at least the following configuration: 1 Mbyte RAM, hard disk and EGA/VGA screen. The system ELECCALC has a better performance if it is possible to define a 1.44 Mbyte virtual RAM-DRIVE.

![](/api/attachments/GGYB2579/fulltext/images/5327ded24c091bd198d7ecc44e0e296c8d0a65f2470c8c31a622d5df45c7a97d.jpg)  
Fig. A.1. Starting screen.

![](/api/attachments/GGYB2579/fulltext/images/265294674d4ecaaa26c882168b40dc624e5d5072726fe5758810044b7d535749.jpg)  
Fig. A.3. Data set.

## Appendix

![](/api/attachments/GGYB2579/fulltext/images/87ad95a6ca5e53605f0f59ee909e24ea1299e07927cdaad264ced2cec889a393.jpg)  
Fig. A.4. Reference set.

Some illustrative menus and screen dumps

![](/api/attachments/GGYB2579/fulltext/images/daaf8962914b519287aaebe47010a5821bbd85baa1d942ea89b05f22387b5ff5.jpg)  
Fig. A.2. Principal menu.

![](/api/attachments/GGYB2579/fulltext/images/9b55448785931974b728a192494ca3b240e273f40304c9f3962b7cce5be748cb.jpg)  
Fig. A.5. Interactive dialogue.

![](/api/attachments/GGYB2579/fulltext/images/b0307d5d39630f17c770dc2d048ed12fa366e392eb35516493635a14e97f8818.jpg)  
Fig. A.6. First set of weights for the criteria.

![](/api/attachments/GGYB2579/fulltext/images/674b1706a3aa967e491bdf03e63f23b5b83ef2cd719348afbd181f17cbc1d506.jpg)  
Fig. A.9. Quasi-median order of the reference set.

![](/api/attachments/GGYB2579/fulltext/images/d35d51ddcfe95101e5bd9d6efbf372bc8cb1868f6d24068ca40f0a89566f1f78.jpg)  
Fig. A.7. First set of values for the concordance thresholds.

![](/api/attachments/GGYB2579/fulltext/images/781e08e4edbd0dce575c6ff1b1d3a3375407ba1fdc93a920361d74cb1951bc44.jpg)  
Fig. A.10. Quasi-median order of the data set.

![](/api/attachments/GGYB2579/fulltext/images/55e93b0381fef9c0d5896a7d7faea05e2a8b77dc8843ad93f77518169c768005.jpg)  
Fig. A.8. First set of values for the indifference and discordance thresholds.

![](/api/attachments/GGYB2579/fulltext/images/84163bf26ef0df48844bc7782f7a276f254bc1692b103dabb6d50073a1c234f3.jpg)  
Fig. A.11. Final order of the data set.

## References

[1] Duquette, D. et M. Lachapelle, Le guide de l'auto 91, Editions de l'homme, Montréal, 1991.

[2] Guigou, J.L., Méthodes multidimensionnelles, Dunod, Paris, 1977.

[3] Jacquet-Lagrèze, E. and J. Siskos, « Assessing a set of Additive Utility Functions for Multicriteria Decision-Making: The UTA Method », European Journal of Operational Research, Vol. 10, 2, 1982, pp. 151–164.

[4] Jacquet-Lagrèze, E., PREFCALC, Évaluation et décision multicritère, (user guide), Euro-Décision, Paris, 1983.

[S] Kiss, L.N., « Waiting Lines in the Stochastic Network of a Car Service », Progress in Operational Research, North Holland Publishing Company, 1976, pp. 547–559.

[6] Kiss, L.N., J.M. Martel, « Hiérarchisation d'entités à partir de comparaisons binaires assisté par un système

interactif », RAIRO Recherche Opérationnelle/Operations Research, Vol. 25., n 2, 1991, pp. 129–160.

[7] Martel, J.M. and R. Nadeau, « An interactive Approach For Modeling Revealed Preferences with ELECTRE II », Working Paper, Faculté des Sciences de l'Administration, Université Laval, Québec, 1991.

[8] Roy, B. et P. Bertier, « La méthode ELECTRE II - Une application au média-planning » in O.R. '72, M. Ross (Ed.), North Holland P.C., 1973, pp. 291-302.

[9] Solymosi, T. and J. Dombi, « A Method for Determining the Weights of Criteria: The Centralized Weights », European Journal of Operational Research, Vol. 26., pp. 35–41, 1986.

[10] Turban, E., Decision Support and Expert Systems, second edition, Macmillan Publishing Company, New York, 1990.
