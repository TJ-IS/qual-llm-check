---
otero_id: 4982
otero_key: "B92SMBA2"
title: "Fusion Miner: Process discovery for mixed-paradigm models"
authors: "Johannes De Smedt; Jochen De Weerdt; Jan Vanthienen"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Johannes De Smedt ⁎, Jochen De Weerdt, Jan Vanthienen

KU Leuven Faculty of Economics and Business Department of Decision Sciences and Information Management, Naamsestraat 69, B-3000 Leuven, Belgium

## a r t i c l e i n f o

Article history: Received 23 October 2014 Received in revised form 21 April 2015 Accepted 11 June 2015 Available online 19 June 2015

Keywords: Business process mining Workflow models Declare

## a b s t r a c t

The research area of business process mining has vastly matured in recent years. Its main focus centers around the extraction and analysis of process models from event logs. A strong emphasis lies on the automatic discovery of models for which numerous algorithms have been proposed already. So far, most discovery algorithms were limited to the derivation of single-paradigm models, which contain either procedural or declarative constructs, targeting the mining of strict and flexible processes respectively. This paper proposes the first fully-automated mining technique to discover procedural workflows combined with Declare templates to capture processes that are difficult to mine with only a single paradigm, e.g., workflows with different layers of flexibility. This approach provides process analysts with new discovery capabilities, including the retrieval of better fitting and more precise models with high comprehensibility. The main contribution consists of the Fusion Miner algorithm, which has been implemented in the process mining framework ProM as a plug-in.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Business practitioners often face the need to gain insights into how their business processes are actually being carried out. They query whether the current enactment of processes such as purchase-to-pay, fault-to-resolution, or invoice-to-cash, etc., are in line with how the process is envisioned, either described in documents such as process models, but also in terms of expectations. In the case of misalignments, adaptation is needed to ensure that decisions made by business owners are reflected in the information system under scrutiny. The field of process mining [1], which fits under the umbrella of information mining [2], addresses this challenge by focusing on the automatic retrieval and subsequent analysis of business process models and insights from data logs containing events. As such, process mining can be a powerful approach for decision makers for assessing and improving business practices. It does so according to three pillars, process discovery, enhancement and conformance checking. The former can be considered the primordial task in a process mining exercise, supporting the two latter pillars that typically build on top of it. The goal of process discovery is to learn a process model from data in the form of an event log in the most comprehensive, comprehensible and correct way. In order to do so, many mining algorithms have been proposed, including, among others, Alpha Miner [3] and Heuristics Miner [4]. Generally, these miners retrieve procedural models, containing strict sequence information, such as Petri nets [5].

More recently, declarative process modeling and mining has gained popularity and several discovery techniques such as, e.g., Declare Miner [6], have been implemented for discovery purposes. These miners derive rules from event logs to create models with a more flexible view on the information contained in the log, as any behavior that is not strictly forbidden is allowed.

In accordance with the “maps” view on process models proposed in Ref. [1], one retrieves different information by mining for different paradigms. Similar to reading maps with different perspectives, which cover multiple layers of an area, it is possible to retrieve different paradigms at once to gain complementary insights from the information retrieved from the log. For example, combining street maps with altitude information can provide a deeper understanding of the explored area.

In line with this metaphor, this paper presents an approach based on the principles of the authors' work in Ref. [7] for combining procedural model fragments and declarative constraints in one map. As such, a new way of mining and representing process models is proposed. This process mining approach exploits the different characteristics of both process paradigms, with each paradigm better capable of representing distinct behavioral aspects of an event log. In the literature, the combination of both paradigms into one discovery algorithm has received very little attention so far. Nonetheless, the prospect of learning richer, mixed-paradigm process models seems promising, especially in the context of semi- or unstructured processes. Our proposed approach has been implemented in ProM<sup>1</sup> as a plug-in and borrows some key principles of the two most frequently used process mining techniques for each paradigm, Heuristics Miner [4] and Declare Miner [6]. The results show models that are fitting and precise for event logs that contain different layers of flexibility, meaning they show behavior consisting of both strict event sequences and rather loosely defined event occurrences. This improves current single-paradigm approaches regarding both conformance and comprehensibility, hence supporting the initial problem of discovering, enacting, and improving current decision making processes. Furthermore, the proposed approach provides a nice visualization to allow decision makers to read and inform themselves quickly and in an elaborate way.

The remainder of this paper is structured as follows. The second section covers the related works, followed by a section that elaborates on the authors' take on mixed-paradigm models and the algorithm to mine and criteria to evaluate them. The fourth section evaluates two simulated examples and one real-life case by comparing current techniques and the outcome of Fusion Miner. The last section concludes the paper with a discussion and future work.

## 2. Related work

Within the field of process mining, a strong emphasis is put on the automatic retrieval of business process models from event logs. The algorithms offer mining solutions that deal with aspects such as the tradeoff between recall, precision, generalization, and the presence of noise in the event log [8]. Initially, procedural process mining approaches were put forward. Some well known and widely used ones are discussed in Refs. [9,3,4,10,11]. They capture sequence constraints and parallelism by incorporating information supporting adjacency and (direct) succession in a process log, extended with (X)OR- and AND-split and -join information. Most of the constraints are locally defined (an exception is Fuzzy Miner, which uses an optional distance metric for deriving sequence constraints), but calculated on log level.

More recently, the modeling and mining of flexible process models has gained popularity among researchers. The most prominent declarative control flow modeling framework is Declare [12], which offers a set of linear temporal logic (LTL)-based constraint templates for modeling and rule verification purposes, bundled in the ConDec language. An overview of the most commonly used templates can be found in Table A1. Many declarative process discovery algorithms have been developed, such as in Refs. [6,13–15]. The technique in Ref. [6] mines directly for automata of Declare constraints using Apriori-based rule learning [16]. In Ref. [13], the authors use distinct support functions for each constraint. Regular expressions are used to express the constraints, rather than Büchi automata. Significant performance gains are achieved in Ref. [14]. The last algorithm presented in Ref. [15] uses SCIFF [17], a declarative language based on computational logic. While different languages are used, the outcome is still represented or can be represented with Declare.

There exist some approaches on the verge between both paradigms, such as Fuzzy Miner [10], UnconstrainedMiner [14] and AGNEs Miner [18]. The former captures flexible processes by incorporating multiple perspectives such as social network and control flow information (note that this is different from a mixed-paradigm approach). The algorithm makes it possible to visualize process models, called Fuzzy models, that highlight the sequences within the log that have the highest impact on these perspectives, which enables the capturing of flexible models better than, e.g., Alpha Miner. UnconstrainedMiner approaches the mixed-paradigm perspective the other way around, starting from a declarative constraint mining implementation which can incorporate any constraint based on regular expressions. As such, the technique is able to incorporate very procedural constraints. A similar approach is used in Ref. [18], where the authors propose a discovery algorithm based on NS (no-sequel), a declarative predicate which can be used to derive constructs that form a Petri net.

The field of business process modeling has various solutions for combining declarative, flexible model constructs and procedural languages. Pockets of flexibility [19], worklets [20], and the combination of YAWL and Declare [12] introduce atomic subworkflows into procedural workflows, hence making certain parts of the model more flexible. However, the execution semantics of both modeling types are still separate, as every paradigm still executes in its own part of the model hierarchy. A truly mixed-paradigm approach, that is one with intertwined state-spaces, is proposed in Ref. [21] for Petri nets and Declare. Another approach is the incorporation of rules into procedural models [22] by calculating process trees and applying change operations on the tree for data constraints afterwards. The scope of this work, however, is more focused on including data aspects into a process model.

A mixed-paradigm outcome in process mining, however, has not been pursued yet as such, with the very recent exception of Ref. [23], in which the authors break down the event log into a hierarchy and mine the different subprocesses according to the appropriate paradigm. Note that this is similar to the principles of the mixed-paradigm approaches based on hierarchy cited above. While the purpose is somewhat similar to the one pursued in this paper, there are some noticeable differences. First of all, the authors assume atomic subprocesses, which are still disjoint. This restricts synergies between both paradigms in terms of state space, as they cannot interact to mine and represent process behavior. Furthermore, while the authors propose an approach based on counting predecessors and successors which is somewhat comparable to direct succession in Section 3.2, applying a threshold on the exact number of predecessors and successors seems rather coarse for deciding on the structured versus unstructured nature of activities, especially for smaller logs. Therefore, our approach includes a configurable threshold based on the concept of entropy, which allows for making a more versatile trade-off between structured and unstructured behavior. In addition, the mandatory hierarchical structure of the mined hybrid model in Ref. [23] puts a limitation on its application to event logs where structured and unstructured behavior are much more intertwined. The approach presented in this paper does not presume such a hierarchical structure. Finally, the approach is not setup as a discovery algorithm and serves rather as a log preprocessor.

## 3. Mixed-paradigm mining and Fusion Miner

In this section, a definition of mixed-paradigm models is provided, followed by the Fusion Miner algorithm and the evaluation criteria that can be used for mixed-paradigm models.

## 3.1. Mixed-paradigm models for mining

The models used in this paper are based on dependency nets, which can be converted to Petri nets, and Declare. In this paper we assume to execute these models as described in Ref. [21]. The work provides an indepth analysis of executing Declare constraint automata and Petri nets. The authors suggest three ways of enactment (the last one only applicable to data-aware nets), of which the first approach is called Simple Simulation. This boils down to constructing the automaton for each Declare constraint separately and updating them during execution. Some constraints, when intertwined, can lead to a permanent violation even when separately they do not. Hence, the full automaton of all individual constraints should be computed. This is called Smart Simulation. In this paper, we assume to execute mixed models of Declare and Petri nets as described in the latter approach.

The choice for a dependency net and Declare constraints is founded on their application in two very well-known and supported mining algorithms, namely Heuristics Miner [4] and Declare Miner [6]. The dependency net can be converted to Causal nets or Petri nets afterwards, as some examples in this paper show. Numerous techniques exist for this purpose and are incorporated in, e.g., Heuristics Miner. Declare models can be represented as a constraint set π which is applied on activities D, thus resulting in DM = π(D). A dependency net DN is defined as a tuple of activities or nodes L and the flow in the net $F =$ $L \times L ,$ constituting a directed graph $D N = \left( L , F \right)$

(a)  
![](/api/attachments/B92SMBA2/fulltext/images/0fa33055ba184f31c2e3bb54270fafe8d9689a6f667e49a0d52890ea92553be9.jpg)

(b)  
![](/api/attachments/B92SMBA2/fulltext/images/51e8fe9c1f208ef292474bf2e11699c4597978a1c597b5f512b171162a8138d6.jpg)

(c)  
![](/api/attachments/B92SMBA2/fulltext/images/3d217cd7c0ee3e56e16e8f7fc482f244fbd7a3ff11865918006440c2c98ac156.jpg)  
Fig. 1. Graphical representation of the behavior allowed by the models, both procedural and declarative, and present in the log. In (b), both models restrict each other's behavior to provide a stricter outcome. In (c), the union of both models is displayed. Any subsection can be an outcome of our mining approach.

The different behavior of the models over activities A can be represented as proposed in Ref. [12]. Fig. 1a shows the declarative behavior π(D) over activities D ⊆ A in the trapezoid-like, dotted shape and the procedural behavior $D N = \left( L , F \right)$ in light gray with L for the transitions, L ⊆ A. While the figure was proposed for modeling, it is now applied to mining. Therefore, the behavior contained in the log should be included. It is represented by the checkered, unstructured polygon.

We propose a mixed-paradigm model as follows: let MPM be a tuple $M P M = \left( L , F , D , \pi \right)$ . As such, we define both rules and strict sequences over the activities. The outcome of the model is then any part of DN and DM, MPM ⊆ DN ∪ DM, which constricts the behavior of A in different ways:

• A more narrow result: DN ∩ DM: by taking the intersection of the behavior allowed by both models, it becomes possible to more strictly describe the process flow. This is represented by Fig. 1b, where the intersection is indicated as the dark gray part. The main cause for this is that procedural models are good at capturing straightforward sequences, and Declare constraints have rich semantics to capture flexible behavior, but also long-distance relationships and duplicate tasks. Combining them offers the possibility to use the best representation in different situations.

• A mixed result: DN ∪ DM: by taking the union of all behavior, it becomes possible to capture behavior in the log that previously remained undiscovered (typically in the procedural model) or was too broadly captured (typically in the declarative model). By taking subsets of this union, one can more closely retrieve the behavior in the log. This is shown in Fig. 1c, where the possible subsets are in dicated in dark gray.

The basic idea behind the mining algorithm explained below is the division of the set of activities A in the event log into the two sets introduced above, namely the procedural activities L and the so-called entropic activities D. We define entropic activities as activities for which behavior is hard to capture in a strict procedural process flow. Arcs in mixed-paradigm models can be of the following type:

$D D \subseteq D \times D { \mathrm { : } }$ arcs between entropic activities are represented by Declare constraints.

• DL ⊆ D × L and $L D \subseteq L \times D { \mathrm { : } }$ arcs between entropic and procedural activities are either explained by Declare constraints or the dependency net, with a prioritization of the former.

• LL ⊆ L × L: arcs between procedural activities are represented by the dependency net.

As such, there exist activities that are either completely captured in the Declare model, $A _ { D D } \in D ,$ , only captured in the Petri net, $A _ { L L } \in L ,$ and activities present in both models, $A _ { D L _ { D } / L D _ { D } } \in D$ and $A _ { D L _ { L } / L D _ { L } } \in L .$ . Note that $D = A _ { D D } \mathsf { U } A _ { D L _ { D } } \mathsf { U } A _ { L D _ { D } }$ and $L = A _ { L L } \cup A _ { L D _ { L } } \cup A _ { D L _ { l } }$ . It is to be avoided that the paradigms become too convoluted, as the mining of both model types simultaneously is based on heuristics and cannot assure that there are no contradictions in the state spaces of both models. There exist model checking techniques, such as [24], which can convert both models into automata. The synchronous product could yield errors which can be taken into account during process discovery. However, the overhead introduced by these techniques is significant. Nonetheless, Fusion Miner actually exploits these “mismatches” in the state space, as both model types will restrict the workflow in a different way, yielding models with higher precision. This will become clear in the replay and evaluation subsections in Section 4.

However, in order to keep both model types somewhat separated, Declare constraints are prioritized as mining and representation form, as the semantics of LTL formulae are richer than a dependency net relationship. Declare constraints are mined for all activities, except the ones in $A _ { L L } .$ If no constraints are discovered for an activity in D, the algo rithm is resilient and puts the activity in L.

Table 1  
The four different types of connections in a mixed-paradigm process model.

<table><tr><td>Activities</td><td>D</td><td>L</td></tr><tr><td rowspan="2">D</td><td> $D \times D$ </td><td> $D \times L$ </td></tr><tr><td>Declare Constraints</td><td>Declare Constraints(Dependency graph)</td></tr><tr><td>Contains</td><td> $A_{DD}$ </td><td> $A_{DL_D} \cup A_{DL_L}$ </td></tr><tr><td rowspan="2">L</td><td> $L \times D$ </td><td> $L \times L$ </td></tr><tr><td>Declare Constraints(Dependency graph)</td><td>Dependency graph</td></tr><tr><td>Contains</td><td> $A_{LD_D} \cup A_{LD_L}$ </td><td> $A_{LL}$ </td></tr></table>

## 3.2. The Fusion Miner algorithm

The Fusion Miner implementation<sup>2</sup> is based on the combination of Heuristics Miner [4] and Declare Miner [25]. Starting from the dependency net, it identifies activities that are connected to a relatively higher number of other activities in the graph, as these can be considered a causal factor of the increase in potential process behavior. As such, we target them for inclusion in the set of activities that are subject to Declare mining in the second part of the discovery process. Finally, the Declare model can be pruned optionally and the mining result is displayed in a model containing both paradigms (Table 1).

## 3.2.1. The algorithm

The algorithm starts off by calculating dependency measures for log L containing the activity alphabet $A _ { L }$ with Heuristics Miner. This results in a tuple (DG, DS, L2L, LDD) with $D G \subseteq A _ { L } \times A _ { L }$ as the flow relations in the dependency net, DS as the direct succession values between $A _ { L } ,$ L2L as the level 2-loop values, and LDD as long distance dependency values. By analyzing the strength of the direct succession metric (which is controlled by a threshold d called Dependency threshold) between activities $A _ { L } ,$ , one can retrieve the activities most closely related in a small window containing local neighbors in the log. Activities that are connected to others many times, or are somewhat but not strongly connected, are candidates to be placed in the set of declarative activities $D \subseteq A _ { L } .$ Others that have few but strong connections to neighboring activities, are candidates to remain in the procedural part of the model $L \subseteq A _ { L } .$ Phrased differently, we target activities with unclear direct succession relations, which can be an indication of the ad-hoc all-over-the-place occurrence of this activity, which results in non-structured and cluttered up sequential process models. Note that this approach also often captures the activities that cannot be fitted into the model and thus puts activities that are connected only when the “All activities connected” option is chosen in Heuristics Miner in D.

The details of the algorithm can be found below. It first checks for entropic activities and for this purpose we propose a metric called activity entropy (AE) which captures the average of the direct succession (DS) values between an activity and the others in the log where the dependency threshold d is not met (lines 3–4). In other words, it captures weak dependencies. Procedural activities in a log will have a very low activity entropy, as most of the connections will be either strong (Nd) or non-existing (close or equal to zero). Based on a given threshold $0 \leq e \leq 1$ which is an input parameter of Fusion Miner, a proportion of the log is withheld. The different values AE<sub>i</sub> are ranked and $\lfloor \lvert A _ { L } \rvert ( 1 - e ) \rfloor$ activities are kept in the sorted set E (lines 5–6). Furthermore, if there is a gap of 1/e between the values for AE of two activities in $E ,$ the activities ranked below the gap are removed (lines 7–9). This procedure avoids introducing too many activities in D and as a consequence possibly too many constraints between them. Note, however, that a fully declarative model can be obtained by using 1 for e. Declare constraints mined for single activities are always included in the log.

## Algorithm 1. The Fusion Miner algorithm

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:  $L, A_{L}$   ▷ The event log L with Activities  $A_{L}$ 
Input: P ▷ The parameters for Heuristics Miner (Heur. Min.) and Declare Miner (DecMin)
Input: e ▷ The entropy parameter value
1: procedure MINEMIXED-PARADIGMMODEL(L, P, e)
2:    $(DG, DS, L2L, LDD) \leftarrow \text{HeuristicsMiner}(L, P) \triangleright \text{Mine dependency info with Heur. Min.}$ 
3:    for  $a \in A_{L}$  do
4:    $AE_{a} := \frac{\sum_{b, a \neq b \land DS_{ab} &lt; P.getDepThres()^{DSab}}}{|DS_{ab} &lt; P.getDepThres()| - 1}$ 
5:    sort(AE)
6:    $E \leftarrow AE.top(A_{L} * (1 - e)) \triangleright \text{Take the } |A_{L}| * (1 - e) \text{ activities with the highest } AE \text{ value}$ 
7:    while  $\frac{E_{i}}{E_{i+1}} &lt; \frac{1}{e} \lor i \leq |E|$  do ▷ Stop when gap between entropy values is too big
8:    $D \leftarrow e_{i}$  ▷ Add e to the set of entropic activities D
9:    $i + +$ 
10:    $DecMap = DeclareMiner(L, A_{L}, D, P)$  ▷ Mine the Declare constraints
11:    Optional:  $DecMap = prune(DecMap)$  ▷ Optional pruning of the Declare model
12:    MixedParadigmNet = MergeModels(DecMap, DG, D,  $A_{L}$ )
13:    return MixedParadigmNet
</div>

## Algorithm 2. Merge models algorithm

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: procedure MERGEMODELS(DM, F, D,  $A_{L}$ )

2: for  $e : A_{L} \times A_{L} \in DM$  do ▷ Loop over the edges in the Declare model

3: if  $e_{source} \in D$  then

4: if  $e_{target} \in D$  then

5:  $DD \leftarrow e$ 

6: else

7:  $DL \leftarrow e$ 

8: else ▷ The case of  $e_{target} \wedge e_{source} \notin D$  cannot occur

9:  $LD \leftarrow e$ 

10: for  $e : A_{L} \times A_{L} \in F$  do ▷ Loop over the edges in the dependency net

11: if  $e_{source}, e_{target} \notin DD \cup DL \cup LD$  then

12:  $LL \leftarrow e$ 

13: return  $DD \cup DL \cup LD \cup LL$
</div>

e influences the discovery process thus in two ways. First of all, the higher e, the more activities will be put in D. Secondly, it will dampen the effect of considering activities as entropic when there is little evidence for this. Hence, the algorithm reacts differently to logs containing very procedural behavior, very flexible behavior, or a mixture of both. In the first case, e will have less effect, where only higher values of e (N0.5) will introduce many declarative activities (and constraints), which is reversely true for the second case. In the latter case, e is the most sensitive, churning different results for the full interval of [0, 1]. Therefore, one can use e to determine the extent to which the log is flexible and change e to retrieve different results. By first using a higher value of e of over 0.7, the log will reveal the very entropic activities, and the user can change e according to his needs.

## 3.2.2. Pruning and constraint choice

After the results of both miners are retrieved, an optional manipulation of the outcome is performed which cuts and adds some constraints, extending the approach proposed in Ref. [25]. (Alternate) Precedence and Response constraints (see Table A1) are transformed into Succession constraints when the antecedents and consequents involved appear exactly once, and Co-existence is removed when both activities appear at least once. The Alternate precedence constraints are reduced to Precedence when the consequent only appears once, etc. After this pruning phase, a check for transitivity is performed, as, for example, newly introduced Precedence constraints might be in a transitive relation with other Precedence constraints, while their superior Alternate Precedence predecessors were not.

Also, since the Declare constraint set contains over 20 entries and we combine this set with a procedural model, some constraints become obsolete or less relevant:

• The Chain Response/Precedence/Succession() constraints are captured by direct succession constraints in the procedural model.

• The Choice() constraints are captured by the XOR- and AND-joins and -splits in the procedural model. Furthermore, Declare constraints often implicitly invoke such constraints.

• Negative constraints are left out by default, but can be included. These constraint templates tend to introduce a lot of constructs as everything that is not supported is captured by these constraints, but often add little extra insight into the model.

## 3.2.3. Performance and noise

The Fusion Miner algorithm utilizes two other algorithms that bound the performance. First of all, the very scalable Heuristics Miner algorithm is used, which is fast and resilient to noise [4]. Since every run of Fusion Miner mines the log fully with Heuristics Miner, it serves as a lower bound for calculation time (see Algorithm 1, line 2), t<sub>HeurMin</sub>. Through lines 3 to 9, simple calculations are made which have a negligible effect on performance, with a complexity of $\frac { | A _ { L } | ( | A _ { L } | - 1 ) } { 2 } , t _ { D C a l c } .$ Next, Declare Miner is applied. Depending on the size of AE, Declare Miner will calculate all binary constraints $( D = A _ { L } )$ or only between D and D and D and P. In the latter case, no constraints are mined for P to P, which can reduce the calculation effort $t _ { D e c M i n }$ significantly. Finally, the merging of both models is also linear to the number of arcs in the model (2), t<sub>MergMod</sub>. Hence, the calculation time resides in between the interval $[ t _ { H e u r M i n } , t _ { H e u r M i n } + t _ { D C a l c } + t _ { D e c M i n } + t _ { M e r g M o d } ] .$

Both algorithms have been proven to be capable of dealing with noise [8,26]. Most notably, Heuristics Miner has parameters that can be fine-tuned to disregard infrequent behavior and rare relationships by using the dependency threshold. Declare Miner can do the same by disregarding certain activities by using high confidence and percentage of instances settings [26]. Furthermore, the Fusion Miner algorithm also disregards behavior by pruning entropic activities (lines 6–9).

## 3.3. Fitness and precision of mixed-paradigm models

In order to fully assess the results of Fusion Miner, the fitness and precision of models derived from event logs should be evaluated to show how well the algorithm is capable of not only retrieving, but also narrowing down the behavior as described in the previous sections. Conformance metrics have been studied extensively, and numerous techniques exist. For a comprehensive overview of conformance metrics and techniques, the authors refer to Ref. [27].

As previously explained, Fusion Miner tries to fit the event log with different explanatory models. Hence, the overall fitness is often high, with a precision that outperforms techniques that are commonly used to achieve a fitness of 1, such as ILP Miner [11]. Note that, when the Declare model is able to capture most of the flexible behavior which was hard to represent in a procedural net with a high Declare constraint support, the model will naturally end up with a high fitness value, oftentimes also reaching a perfect value of 1.

The authors have implemented a preliminary fitness evaluation technique which tries to find an alignment of the log and the model. By traversing the state space, the model gets replayed in a best-first fashion. The technique creates the automaton of the Declare model (which is not as large as a Declare-only model when $e < 1$ and due to pruning) and makes the product with the Petri net state space while traversing the trace during replay. Precision can be calculated during replay. The approach used here is based on artificially generated negative events, which was proposed in Ref. [18] and later improved in Ref. [28]. A metric for precision is proposed, which is called Behavioral Precision $p _ { B } .$ The basic setup consists of the generation of artificial negative events, which, simply put, are inserted when there can be no evidence found in the log for their occurrence at a certain trace index. The evidence is based on the prefix of the event, which can be configured to take into account a certain window size. Afterwards, the wellknown precision evaluation of statistical and data mining models can be applied, and $\begin{array} { r } { p _ { B } = \frac { T n e \ P o s i t i v e s } { T n e \ P o s i t i v e s + F a l s e \ P o s i t i v e s } . } \end{array}$

## 4. Experimental evaluation of Fusion Miner

To illustrate the problems many traditional single-paradigm miners face, three examples are given below to illustrate where improvements can be achieved by Fusion Miner. Some basic metrics regarding the event logs used are provided in Table 2. The first log contains a straightforward workflow which is distorted by the nearly random occurrence of an activity. The second example deals with a textbook case of a log with different layers of flexibility. The last one is a real-life log, previously used in Refs. [27,8], which contains an incident-management process. The main insights are summarized at the end of this section in a list of contributions the Fusion Miner algorithm offers.

The first two logs are simulated using CPN Tools [29], which is able to execute mixed-paradigm models as indicated above. The logs were checked afterwards for temporary violations of Declare constraints and other issues that can arise, as explained in Ref. [21].

Mixed-paradigm models displayed in the text are represented as a combination of a dependency net and Declare constraints. However, the corresponding Petri net is also offered as an output. In the examples used in this paper, the following representation is used in the figures:

• The full arcs represent the procedural behavior as introduced by Heuristics Miner. They form the dependency net of the model.

• The checkered activities exceed the entropy threshold.

• The activities filled with a dark (red) shade fulfill the Exactly1 constraint.

• The activities filled in light gray fulfill the Existence constraints.

• The striped arrows represent Declare constraints, which are labeled with the template's name.

• The rectangular activities represent activities fulfilling the Init and Last constraints.

## 4.1. Example 1: A loosely connected activity

The first log of which the simulation model can be found in Fig. 2, represents a standard process with AND-split and -join which is repeated. Procedural discovery algorithms such as Alpha Miner and Heuristics Miner are perfectly capable of retrieving such procedural process behavior. However, introducing an activity which is only roughly tied to a strict position in the workflow such as Z, leaves the procedural miners guessing at its location in the process, as explained below. The activity is only connected to activity C with a Precedence constraint, and to activity D with an Alternate Precedence constraint.

## 4.1.1. Issues with currently available miners

Heuristics Miner places Z in a separate self-loop before the last activity, as can be seen in Fig. 3. The result of ILP Miner, depicted in Fig. 4 recognizes that Z is hard to fit into the workflow and adds many self loop places to the model to deal with the flexible nature of this activity. Note that Heuristics Miner is known for mining relatively general models and ILP Miner for precise models. Hence, most procedural miners will have similar outcomes or results in between the ones of these miners.

Basic metrics describing the event log used for the evaluation of Fusion Miner.

<table><tr><td>Event log</td><td>Loosely connected activity</td><td>PhD process</td><td>Incident management log</td></tr><tr><td>Number of activities</td><td>7</td><td>6</td><td>20</td></tr><tr><td>Number of cases</td><td>20</td><td>30</td><td>956</td></tr><tr><td>Number of events</td><td>786</td><td>402</td><td>9306</td></tr><tr><td>Number of distinct traces</td><td>10</td><td>30</td><td>212</td></tr></table>

![](/api/attachments/B92SMBA2/fulltext/images/3a9d71c8686c0aee228232e6bd7a2d5008893b08ecab40eedf3c388d86213d1e.jpg)  
Fig. 2. A Petri net containing a procedural workflow based around an AND-split and -join, extended with activity Z which can occur in numerous positions in the process. It is connected to activity C with a Precedence constraint, and to activity D with an Alternate Precedence constraint.

![](/api/attachments/B92SMBA2/fulltext/images/d1e52593e52335bb3b33506dd9aaf9b3f229459c55b789559398ce7b026001be.jpg)  
Fig. 3. Result of Heuristics Miner (default settings) for the log of example 1.

The result includes thus only a very general way of enabling Z in the form of a loop.

Mining a log with a declarative, constraint-based miner such as Declare Miner would result in a correct deriving of temporal relationships, however, the strict control flow that is present between the activities other than Z is very hard to discern as can be seen in Fig. 5. The overall readability of a declarative process model is one of its main drawbacks, as extensively researched and shown in Ref. [30].

The implementation of Ref. [23] cuts activity E out of the log to be put on a lower hierarchical level, however, mining this with Heuristics Miner or ILP Miner churns the same results as what the techniques provided in Figs. 3 and 4.

## 4.1.2. Discovery with Fusion Miner

Fusion Miner is capable of mining the dependency net and merge it with Declare constraints. This way, it enlightens the unclear sequence information of activity Z, which was not possible in Heuristics Miner, and still retains the very procedural behavior of the rest of the net, which was hidden in the Declare model due to the large amount of constraints. Much like the explaining of extra residual value in statistics, Fusion Miner tackles the unknown by fitting the data selectively by using characteristics of both process model types. In this example, the infinite loop enabling activity Z all the time was better explained by introducing Declare constraints with Fusion Miner to reduce the state space of the model around Z, resulting in a more precise model as illustrated in Fig. 6. The Petri net resulting from the dependency net in the mixedparadigm model is shown in Fig. 7.

## 4.1.3. Fitness and precision

The results of Heuristics Miner, ILP Miner, Declare Miner, and Fusion Miner all fit the log 100%. We selected a trace in the log that clearly shows where the result of Fusion Miner improves upon the three previous ones. The results for all miners are included and can be found in Table 3. The cases for which Fusion Miner will be more precise than the outcome of Heuristics Miner, are the ones in which Z appears before C, due to the Precedence constraint and especially where Z appears before D, due to the Alternate Precedence constraint. For example, because Z does not show up until just before the second D, there are less false positives compared to the Petri net. If we look at the behavioral precision scores, the following results are obtained: $\begin{array} { r } { p _ { B _ { H M } } = \frac { 1 8 } { 3 2 } = 0 . 5 6 2 5 , } \end{array}$ $\begin{array} { r } { p _ { B _ { I L P } } = \frac { 1 9 } { 4 4 } = 0 . 4 3 1 8 } \end{array}$ and $\begin{array} { r } { p _ { B _ { F M } } = \frac { 1 8 } { 3 0 } = 0 . 6 . \mathrm { A } } \end{array}$ slight increase is achieved by using Fusion Miner, while improving vastly in terms of comprehensibility compared to Declare Miner. Since Z occurs in an almost random fashion, there is not a huge gain in terms of precision, but Fusion Miner is still better capable of representing all the information that can be extracted from the log. Surprisingly, ILP Miner, known for its inclination towards fit but precise models, has a lower precision value.

![](/api/attachments/B92SMBA2/fulltext/images/430ba45c372bbf2805320122c54fab3de76f3ca41081ede7e45a658d3c294fb8.jpg)  
Fig. 4. Result of ILP Miner (default settings) for the log of example 1.

![](/api/attachments/B92SMBA2/fulltext/images/d91f3a8e4d0dd00a073532d8b708e57d3bab49402bb987364e56a51c049a2813.jpg)  
Fig. 5. Result of Declare Miner for a support of 100% for the log of example 1. The Not Chain Succession constraints are excluded for readability.

## 4.2. Example 2: PhD process

As another example, we provide the simple mixed-paradigm process model in Fig. 8. Both Declare constraints and more sequentially-based Petri nets are combined to resemble the progress of a PhD student throughout his career, which contains the strict order of a first and second seminar followed by the defense. Meanwhile, he/she creates content which is subsequently published in journals or presented at a conference, resembled by the Alternate Precedence constraints. This constraint expresses that both Journal Paper and Conference can happen after Content Creation, and again only after the next occurrence of the Content Creation activity. The first seminar cannot happen before a first contribution to a conference and the second seminar has to be preceded by a journal publication. Note that, while the mixed-paradigm model is fairly simple and understandable, the simulated event log presents characteristics that are typically found in real-life logs originating from complex processes.

## 4.2.1. Issues with currently available miners

If one mines the log with Heuristics Miner, the algorithm is unable to retrieve the exact position and relation of the three activities Content

![](/api/attachments/B92SMBA2/fulltext/images/8e0e431ea0e97eacf80a7cfbe8c28ea4654c9c650a2b422c02a5ce1cdbb2c168.jpg)  
Fig. 6. Result of Fusion Miner for example 1 with a support of 100% and $e = 0 . 4 .$

![](/api/attachments/B92SMBA2/fulltext/images/e7815e98e622ea44c1063fdab7da12f566f6ad34da49551693ba65816ccb8b55.jpg)  
Fig. 7. Petri net derived from the dependency net in Fig. 6, containing the procedural behavior in the model.

Table 3  
The precision calculation for model 1 for all mining outcomes, based on artificially generated negative events. The false positives are indicated in bold. The mixed-paradigm model clearly enables less activities throughout the replaying of the trace, while still retaining maximal fitness.

<table><tr><td>Ind.</td><td>Act.</td><td colspan="3">Enabled MPM</td><td colspan="3">Enabled HM</td><td colspan="4">Enabled ILP</td><td colspan="6">Negative events</td></tr><tr><td>1</td><td>Start</td><td colspan="3">Start</td><td colspan="3">Start</td><td colspan="4">Start</td><td>D</td><td>E</td><td>A</td><td>B</td><td>C</td><td>Z</td></tr><tr><td>2</td><td>A</td><td>Z</td><td>A</td><td></td><td>A</td><td>Z</td><td></td><td>Z</td><td>A</td><td>D</td><td>E</td><td>D</td><td>E</td><td>Start</td><td>B</td><td>C</td><td></td></tr><tr><td>3</td><td>Z</td><td>Z</td><td>B</td><td></td><td>Z</td><td>B</td><td>C</td><td>Z</td><td>B</td><td>C</td><td>D</td><td>D</td><td>E</td><td>Start</td><td>A</td><td>C</td><td></td></tr><tr><td>4</td><td>C</td><td>Z</td><td>B</td><td>C</td><td>Z</td><td>B</td><td>C</td><td>Z</td><td>B</td><td>C</td><td>D</td><td>D</td><td>E</td><td>Start</td><td>A</td><td>B</td><td></td></tr><tr><td>5</td><td>Z</td><td>Z</td><td>B</td><td></td><td>Z</td><td>B</td><td></td><td>Z</td><td>B</td><td>D</td><td></td><td>D</td><td>E</td><td>Start</td><td>A</td><td>B</td><td>C</td></tr><tr><td>6</td><td>B</td><td>Z</td><td>B</td><td></td><td>Z</td><td>B</td><td></td><td>Z</td><td>B</td><td>D</td><td></td><td>D</td><td>E</td><td>Start</td><td>A</td><td>C</td><td>Z</td></tr><tr><td>7</td><td>Z</td><td>Z</td><td>D</td><td></td><td>Z</td><td>D</td><td></td><td>Z</td><td>D</td><td></td><td></td><td>D</td><td>E</td><td>Start</td><td>A</td><td>B</td><td>C</td></tr><tr><td>8</td><td>D</td><td>Z</td><td>D</td><td></td><td>Z</td><td>D</td><td></td><td>Z</td><td>D</td><td></td><td></td><td>E</td><td>Start</td><td>A</td><td>B</td><td>C</td><td></td></tr><tr><td>9</td><td>A</td><td>Z</td><td>A</td><td>E</td><td>Z</td><td>A</td><td>E</td><td>Z</td><td>A</td><td>D</td><td>E</td><td>D</td><td>E</td><td>Start</td><td>B</td><td>C</td><td>Z</td></tr><tr><td>10</td><td>B</td><td>Z</td><td>B</td><td>C</td><td>Z</td><td>B</td><td>C</td><td>Z</td><td>B</td><td>C</td><td>D</td><td>D</td><td>E</td><td>Start</td><td>A</td><td>C</td><td>Z</td></tr><tr><td>11</td><td>C</td><td>Z</td><td>C</td><td></td><td>Z</td><td>C</td><td></td><td>Z</td><td>D</td><td>C</td><td></td><td>D</td><td>E</td><td>Start</td><td>A</td><td>B</td><td>Z</td></tr><tr><td>12</td><td>Z</td><td>Z</td><td></td><td></td><td>Z</td><td>D</td><td></td><td>Z</td><td>D</td><td></td><td></td><td>D</td><td>E</td><td>Start</td><td>A</td><td>B</td><td>C</td></tr><tr><td>13</td><td>D</td><td>Z</td><td>D</td><td></td><td>Z</td><td>D</td><td></td><td>Z</td><td>A</td><td>D</td><td>E</td><td>E</td><td>Start</td><td>A</td><td>B</td><td>C</td><td>Z</td></tr><tr><td>14</td><td>E</td><td>Z</td><td>E</td><td>A</td><td>Z</td><td>E</td><td>A</td><td>Z</td><td>A</td><td>D</td><td>E</td><td>D</td><td>Start</td><td>A</td><td>B</td><td>C</td><td>Z</td></tr></table>

![](/api/attachments/B92SMBA2/fulltext/images/eab8f200f4d8dac15efc8fd86da0befbdc3be400eca43fd4e9ee853019202877.jpg)  
Fig. 8. Workflow with different layers of flexibility representing the progress of a PhD student.

Creation, Conference and Journal Paper as shown in Fig. 9. While Heuristics Miner captures loops and invisible events to support the quite random appearance of Content Creation, it fails to capture the relation of Journal Paper and Second Seminar. Furthermore, the model is cumbersome to read due to the large number of invisible tasks needed to express the flexible nature of the relations.

Note that for Heuristics Miner it is possible to use other configurations, e.g. one with a lower dependency threshold. This would result in a model that better captures the behavior in the event log, but this solution would include a very generic model in which every transition can be executed in any order. Flexible parts of a log that are not captured (well) by procedural models (as they remained either too restrictive or too general) can be represented with declarative constraints to retrieve them in a more correct and readable way. Although capturing flexible behavior might be possible with procedural models, the sequential information would end up in a very convoluted and unstructured graph of loops, splits and joins, and arrows pointing every direction due to the ad-hoc appearance of activities as can be seen in Fig. 9. Since most Declare constraints represent behavior that can be labeled as non-trivial token games, they are better able to represent such parts of an event log. For example, expressing Alternate Response in a Petri net is a challenging task, leading to the usage of artificial model constructs to approximate the same state space.

Again, Declare Miner mines a fitting (for a support of 100%) model with low comprehensibility. The result is shown in Fig. 10. The technique of Ref. [23] puts Defense on a lower hierarchical level, and thus is not able to recognize the flexible activities.

## 4.2.2. Discovery of the PhD process with Fusion Miner

Figs. 11 and 12 show the discovered mixed-paradigm models in ProM. An overview of the different activity entropy values can be

![](/api/attachments/B92SMBA2/fulltext/images/40aa48c8ecb315c222df08c13664c1f4d1685e13738097bcc690a4ab674c581d.jpg)  
Fig. 9. Result of Heuristics Miner for log 2 in Fig. 8 (Default settings and with reduced invisible activities)

![](/api/attachments/B92SMBA2/fulltext/images/badc94b442cd16e016fe9e9fef3fd4398a1c0c13da38df7f17960628c54f31b9.jpg)  
Fig. 10. Result of Declare Miner for log 2. The support used is 100%.

found in Table 4. Even for a small entropy value e = 0.2, the $A _ { L } { } ^ { * } \left( 1 - e \right)$ pruning step, and a constraints support of 100%, the activity Content Creation becomes subject to Declare constraint mining (Fig. 11). By its constant enabledness it can appear anywhere in the workflow and clutter up a sequential process. By retrieving a few constraints for the activity, we are able to represent it in a sense-making way in a mixed model. The model is already capable of capturing the initial model more correctly, as the relationships between ContentCreation and the other activities are correct. The arc between SecondSeminar and JournalPaper is still incorrect.

![](/api/attachments/B92SMBA2/fulltext/images/bfc9e016875c50494a4e9b114bf347401a22d0bafdac060a80e0747c8b0f048a.jpg)  
Fig. 11. Result of Fusion Miner with e = 0.2 for log 2. The activity on the left is the only entropic one and is connected with Declare constraints to the other five. The arrow between Second Seminar and Journal Paper is still incorrect, but the Alternate precedence constraints are better capable of capturing the behavior in a clear way.

![](/api/attachments/B92SMBA2/fulltext/images/5affa4b31c067a8059ed0257d0dbf03e1cb082df26f25fe6aa1b7e53d123bd5a.jpg)  
Fig. 12. Result of Fusion Miner with e = 0.5 for log 2. When raising the entropy level in the miner's con guration, Conference and Journal Paper get included in the declarative part of the model. The relations between the activities are now all captured correctly.

Table 4  
The activity entropy values for the PhD example to illustrate the workings of the algorithm. For e = 0.2, only CC is taken into account, due to the $A _ { L } ^ { \ast } \left( 1 - e \right)$ pruning step of AE. For $e = 0 . 5 , J { \ / F }$ and CO are also included in D.

<table><tr><td>Activity</td><td>Activity entropy</td><td>Eligible for e = 0.2</td><td>Eligible for e = 0.5</td></tr><tr><td>Content Creation (CC)</td><td>0.561</td><td>Yes</td><td>Yes</td></tr><tr><td>Journal Paper (JP)</td><td>0.557</td><td>No</td><td>Yes</td></tr><tr><td>Conference (CO)</td><td>0.52</td><td>No</td><td>Yes</td></tr><tr><td>Second Seminar (SS)</td><td>0.38</td><td>No</td><td>No</td></tr><tr><td>First Seminar (FS)</td><td>0.242</td><td>No</td><td>No</td></tr><tr><td>Defense (DE)</td><td>0</td><td>No</td><td>No</td></tr></table>

By raising the entropy level (Fig. 12), more activities are added to the declarative set D, in this case Conference and Journal Paper. This makes sense given the model. Only constrained by the appearance of Content Creation, these activities are also rather unpredictable. Note that the procedural part of the model is becoming smaller and smaller, while the Declare constraints offer the same behavior and more.

If we position this approach in Fig. 1, it would be categorized as an attempt to mine behavior more closely by retrieving the intersection of both outcomes, depicted in Fig. 1b.

## 4.2.3. Fitness and precision

In Table 5, the second result (for e = 0.5) of Fusion Miner (represented as Declare and Petri net in Fig. 13) is compared to ILP Miner's result for the PhD example, which can be found in Fig. 14. Again, the false positives are indicated in bold. Notice that, even for a dependency measure of 0, Heuristics Miner was unable to derive a perfectly fitting model for the event log and is not used in the comparison.

For this trace in particular, the precision scores are $\begin{array} { r } { p _ { B _ { I L P } } = \frac { 2 2 } { 1 3 + 2 2 } = 0 } \end{array}$ 629 and $\begin{array} { r } { p _ { B _ { M P M } } = \frac { 1 9 } { 1 9 + 5 } = 0 . 7 9 2 } \end{array}$ for e = 0.5.

As shown in Table 5, it is clear that ILP Miner's Petri net keeps a lot more activities enabled throughout the replay of the trace, while Fusion Miner's result enables less activities and thus triggers less false positives, resulting in a higher precision value. Note that, since this trace is short, the prefix window for negative event generation is small, resulting in artificial negative event generation only after some activities, punishing ILP Miner only towards the end. For longer traces, ILP Miner's outcome would produce even more false positives throughout the trace. Compared to the first example, it is clear that Fusion Miner outperforms traditional procedural mining algorithms especially for logs with different layers of flexibility.

The result of Declare Miner, as shown in Fig. 10, also has a fitness of 1 and a high precision, but the comprehensibility is really low. Furthermore, while Declare models usually aim for high flexibility, the outcome of this model is very strict, surpassing the purpose of Declare. Finally, the precision result of Fusion Miner as depicted in Table 5 is the same as the one of Declare Miner, as the resulting Declare model enables the same activities as the mixed-paradigm model during replay.

## 4.3. The incident management log

This real-life example contains different steps of an incident management process, which starts off with the assignment of a help desk resource Status Assigned. This activity can be succeeded by numerous other activities, such as the installment of a Status Work In Progress status, a Pending status, or the use of a special resource such as Group GPC CORK or Group ORS MS BACKOFFICE.

## 4.3.1. Issues with currently available miners

The result of Heuristics Miner with default settings is given in Fig. 15.<sup>3</sup> The dependency net is large, as it tries to fit most of the log variants, which results in a spaghetti-like model. The result of Declare Miner is not included, as it was unreadable due to the enormous amount of constraints (over 100 constraints for a support of 100% and 150 for a support of 75%), which cannot be represented easily in a process map. Furthermore, it did not contain a lot of sequential information, such as (Alternate) Precedence/Succession results. Declare Miner oftentimes has a hard time dealing with real-life logs, which is supported by the fact that UnconstrainedMiner (correctly) found numerous such constraints. However, the result of UnconstrainedMiner includes all supported constraints, hence not a Declare model for a certain support.

## 4.3.2. Discovery with Fusion Miner

Fusion Miner depends on Declare Miner's result, which did not include many Declare constraints kept for mining in the Fusion Miner algorithm. However, by using various Declare constraint support values, it becomes possible to quickly derive various well- and less-supported flows in the dependency net. The result shown in Fig. $1 6 ^ { \hat { 3 } }$ for a support of 75% and e = 0.5, shows many activities only executed once. In combination with the Succession constraints which yield the obligatory execution of the consequent, the main flow can be read from the figure. This highlights another benefit of using Fusion Miner: scrutinizing the log for frequent and less frequent workflow behavior.

## 4.3.3. Fitness and precision

Since the model does not fit the log for 100%, the replaying algorithm cannot enact the model as the move-on-model and move-on-log concept are not integrated yet. Through visual inspection, however, it was clear that for certain Declare constraint support values, the result was very precise, as the combination of Exactly1 and Succession constraints clearly delineated the workflow.

In general, Fusion Miner can cope with real-life and complex logs by building on top of two robust algorithms that can deal with noise (as explained in Section 3.2.3) and are always capable of retrieving a somewhat fitting model (Heuristics Miner) and a model with a varying level of fitness (Declare Miner through its support parameter). Furthermore, real-life logs often consist of behavior that is at least somewhat flexible but still contains some structured sequences. In other cases, Fusion Miner can be used with settings that lean towards procedural and declarative by using parameter e. Furthermore, Fusion Miner will never come up with more convoluted models, which follows from the way the models are merged. The number of arcs found by Heuristics Miner and the fact that Declare constraints are hierarchical, provide an upper bound for the number of arcs found by Fusion Miner.

## 4.4. Summary

The previous examples have shown the main issues that traditional miners face when dealing with different layers of flexibility. The benefits that can be provided by Fusion Miner and its main use cases are:

• More precise models: Fig. 1b shows how a Declare model can cut off parts of a procedural model, resulting in a more precise model. Fusion Miner exploits this intersection because:

\- Declare constraints have different semantics that are better suited to capture flexible behavior. They provide, e.g., richer semantics for loops (e.g. the Alternate Precedence constraint) and duplicate tasks.

\- Declare constraints are derived via constraint support on trace level. As such, they are, reinforced by their non-local sequence semantics, better capable of capturing long-distance relationships. Furthermore, they are mined for a certain support level which ensures the presence of the constraint, while many procedural miners use heuristics which cannot guarantee the end result to be a true reflection of the behavior in the event log.

Table 5  
The precision calculation for the PhD example for ILP Miner (default settings) and Fusion Miner. As can be seen in the Enabled columns, there are a lot of activities enabled all the time in the Petri net of ILP Miner, resulting in lower precision, which is punished by the high false positive rate (negative events indicated in bold) Fusion Miner's model enables much less activities while retaining the same fitness value. The abbreviations of the activities can be found in Table 4.

<table><tr><td>Ind.</td><td>Act.</td><td colspan="7">Enabled ILP</td><td colspan="4">Enabled MPM</td><td colspan="5">Negative events</td></tr><tr><td>1</td><td>CC</td><td>CC</td><td></td><td></td><td></td><td></td><td></td><td></td><td>CC</td><td></td><td></td><td></td><td>CO</td><td>JP</td><td>FS</td><td>SS</td><td>DE</td></tr><tr><td>2</td><td>CO</td><td>CC</td><td>CO</td><td>JP</td><td>SS</td><td></td><td></td><td></td><td>CC</td><td>CO</td><td>JP</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>JP</td><td>CC</td><td>JP</td><td>FS</td><td>SS</td><td></td><td></td><td></td><td>CC</td><td>JP</td><td>FS</td><td></td><td>CO</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>CC</td><td>CC</td><td>FS</td><td></td><td></td><td></td><td></td><td></td><td>CC</td><td>FS</td><td></td><td></td><td>CO</td><td>JP</td><td></td><td></td><td></td></tr><tr><td>5</td><td>CO</td><td>CC</td><td>CO</td><td>JP</td><td>FS</td><td>SS</td><td>DE</td><td></td><td>CC</td><td>CO</td><td>JP</td><td>FS</td><td>SS</td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>FS</td><td>CC</td><td>JP</td><td>FS</td><td>SS</td><td>DE</td><td></td><td></td><td>CC</td><td>JP</td><td>FS</td><td></td><td>CO</td><td>SS</td><td>DE</td><td></td><td></td></tr><tr><td>7</td><td>SS</td><td>CC</td><td>JP</td><td>FS</td><td>SS</td><td>DE</td><td></td><td></td><td>CC</td><td>JP</td><td>SS</td><td></td><td>CC</td><td>CO</td><td>JP</td><td>FS</td><td>DE</td></tr><tr><td>8</td><td>JP</td><td>CC</td><td>JP</td><td>FS</td><td>SS</td><td>DE</td><td></td><td></td><td>CC</td><td>JP</td><td>DE</td><td></td><td>CC</td><td>CO</td><td>FS</td><td>SS</td><td>DE</td></tr><tr><td>9</td><td>DE</td><td>CC</td><td>FS</td><td>DE</td><td></td><td></td><td></td><td></td><td>CC</td><td>DE</td><td></td><td></td><td>CC</td><td>CO</td><td>JP</td><td>FS</td><td>SS</td></tr></table>

![](/api/attachments/B92SMBA2/fulltext/images/0b2702963799549f9f9c39d748e88a149421615e246215145f6dfa9422ef36e4.jpg)  
Fig. 13. Mixed-paradigm model with e = 0.5 from Fig. 12, for which the dependency net is translated into a Petri net.

There often exists a trade-off between precision and generalization [27]. In the case of Fusion Miner, the option for more precise rather than general models was made. However, more general models can be mined by lowering dependency thresholds in Heuristics Miner, and adding less constraints such as Alternates to the constraint set in Declare Miner.

• More fitting models: As illustrated in Section 3.1, Declare models often capture only the rough part of the work flow, depending on the support level they are granted and the templates that are used. While procedural models such as Petri nets can be relaxed to include more behavior by introducing extra connections and, e.g., invisible activities, resulting in an overly general model, Declare constraints can still capture rough or even very fitting information about the parts of the log that are rather flexible and would result in a very generic procedural model. Fig. 1c illustrates this as the dark gray mixed model which represents the combination of a procedural and declarative model can cover extra parts where the light gray procedural model was not able to go.

By combining both, thus using Declare constraints where flexibility is needed while retaining procedural fragments, Fusion Miner can keep a high fitness value by relaxing procedural models with (precisely) fitting Declare constraints.

• More comprehensible models: Model comprehension is influenced by numerous factors [31,32]. By combining paradigms suited for different granularities of flexibility, mixed-paradigm models are capable of representing processes in the form most suited to their nature. For example, parts of an event log which would typically be captured by a Petri net containing invisible activities, can perhaps better be explained by using some Declare constraints. Furthermore, Declare models can be presented in a simpler way for readers with procedural constructs which offer stricter models where possible. As shown in the previous examples, mined Declare models are often incomprehensible and use a vast amount of constraints of which many are redundant.

![](/api/attachments/B92SMBA2/fulltext/images/24ca4c4896230a0d0a8fb1f6363f1b5e238782311f62a43f5d1a00e7b5a7e9d0.jpg)  
Fig. 14. Result of ILP Miner for the PhD example log (default settings).

![](/api/attachments/B92SMBA2/fulltext/images/ff734d550b255627c364a29b974e998af99f93f2aeca549ea389e5334b5364c5.jpg)  
Fig. 15. The result of Heuristics Miner (default settings) for the real-life log. The model displays most of the process variants, which results in a convoluted model in which a main proces flow is hard to discern.

The basic idea boils down to the exploitation of the stronger semantics of Declare constraints in procedural models in order to introduce more flexibility, while maintaining a procedural part in which strict sequences are still present where the process in the log does not need extra flexibility. Very loose or very procedural logs are not the target of the approach, but can be mined by choosing the correct settings. For example, by choosing an entropy level e of 0 or 1, one mines a fully procedural or fully declarative process model respectively. As such, Fusion Miner provides a framework to incorporate any level of flexibility, which can also be used for log exploration.

The three pillars of process mining are supported as follows. First of all, Fusion Miner can contribute by discovering a new type of model that combines constraints and sequences. The results can be crosschecked with managers' believes of current as-is models. This gives rise to a new set of conformance checking techniques, which might include pinpointing non-fitting or imprecise behavior to either the procedural part or declarative part. Based on this, changes can be made to current models in place in the information system focusing on, e.g., certain constraints or certain sequences.

## 5. Conclusions and future work

In this paper, the authors address the challenge of mixed-paradigm process mining. Fusion Miner was proposed, an algorithm to mine for procedural and declarative process model constructs simultaneously to represent workflow behavior in an event log. Results show that this approach yields more precise models, especially in environments with multiple layers of flexibility, and more comprehensive models, as recapitulated in Section 4.4.

Future work includes a more in-depth approach to compliance, as a preliminary replaying algorithm is used for conformance checking.

![](/api/attachments/B92SMBA2/fulltext/images/2ecf5d57c970ec4a8a94bb7600e52ab8972c205753e216f3ffb99cdb67055855.jpg)  
Fig. 16. The mixed-paradigm result of Fusion Miner for the real-life example with e = 0.5 and a support of 75%. The main ow is clearly visible through the main Declare constraints, model variants can be deduced from the remaining procedural process constructs.

Furthermore, the possibility of applying other declarative process model algorithms should be investigated, as recent technique have vastly improved in terms of performance and correctness. Furthermore, the tuning of the parameters (e, Declare constraint support) used in the models can be further investigated. Also, the approach used for deciding upon the inclusion of activities in set D could be elaborated more extensively, as numerous other valid ways such as activity clustering, pattern recognition, etc., might yield different and possibly better results.

Finally, a hierarchical approach to mixed-paradigm models can be introduced to capture constraints and fixed procedures throughout multiple layers of a process log, similar to Ref. [23].

## Acknowledgments

## Appendix A

This research is funded by FWO (Fonds voor Wetenschappelijk Onderzoek) Project G0804 13N.

An overview of Declare constraint templates  
Table A1

<table><tr><td>Template</td><td>LTL formula</td><td>Description</td></tr><tr><td>Existence(A)</td><td> $\diamond A$ </td><td>Activity A appears at least once.</td></tr><tr><td>Existence(A, n)</td><td> $\diamond (A \land \bigcirc (existence(n - 1, A)))$ </td><td>Activity A appears at least n times.</td></tr><tr><td>Absence(A, n)</td><td> $\neg existence(n, A)$ </td><td>Activity A can happen at most n times.</td></tr><tr><td>Exactly(A, n)</td><td> $existence(n, A) \land absence(n + 1, A)$ </td><td>Activity A has to be executed at least n times.</td></tr><tr><td>Init(A)</td><td>A</td><td>Each instance has to start with activity A.</td></tr><tr><td>Last(A)</td><td> $\square (A \Rightarrow \neg X \neg A)$ </td><td>Each instance has to end with activity A.</td></tr><tr><td>Responded existence(A, B)</td><td> $\diamond A \Rightarrow \diamond B$ </td><td>If A happens at least once then B has to happen or happened before A.</td></tr><tr><td>Co — existence(A, B)</td><td> $\diamond A \Longleftrightarrow \diamond B$ </td><td>If A happens then B has to happen or happened after A and vice versa.</td></tr><tr><td>Response(A, B)</td><td> $\square (A \Rightarrow \diamond B)$ </td><td>Whenever activity A is executed, activity B has to be executed afterwards eventually.</td></tr><tr><td>Precedence(A, B)</td><td> $(\neg BUA) \lor \square (\neg B)$ </td><td>Activity B has to be preceded by activity A.</td></tr><tr><td>Succession(A, B)</td><td> $response(A, B) \land precedence(A, B)$ </td><td>Both Response (A,B) and Precedence (A,B) hold.</td></tr><tr><td>Alternate precedence(A, B)</td><td> $precedence(A, B) \land \square (B \Rightarrow \bigcirc (precedence(A, B))$ </td><td>Activity B cannot happen before A. After it happens, it cannot happen before the next A again.</td></tr><tr><td>Alternate response(A, B)</td><td> $\square (A \Rightarrow \bigcirc (\neg AUB))$ </td><td>After each activity A, at least one activity B is executed. Another A can be executed again only after the first B.</td></tr><tr><td>Alternate succession(A, B)</td><td> $alternate\ response(A, B) \land alternate\ precedence(A, B)$ </td><td>Both alternate precedence (A,B) and alternate response (A,B) hold.</td></tr><tr><td>Chain precedence(A, B)</td><td> $\square (\bigcirc B \Rightarrow A)$ </td><td>B can get executed only directly after A.</td></tr><tr><td>Chain response(A, B)</td><td> $\square (A \Rightarrow \bigcirc B)$ </td><td>After A the next activity has to be B.</td></tr><tr><td>Chain succession(A, B)</td><td> $\square (A \Longleftrightarrow \bigcirc B)$ </td><td>A and B can happen only next to each other.</td></tr><tr><td>Not co — existence(A, B)</td><td> $\neg (\diamond A \land \diamond B)$ </td><td>Only one of the two tasks A or B can be executed, but not both.</td></tr><tr><td>Not succession(A, B)</td><td> $\square (A \Rightarrow \neg (\diamond B))$ </td><td>Before B there cannot be A and after A there cannot be B.</td></tr><tr><td>Not chain succession(A, B)</td><td> $\square (A \Rightarrow \bigcirc (\neg B))$ </td><td>A and B can never get executed next to each other where A is executed first and B second.</td></tr><tr><td>Choice(A, B)</td><td> $\diamond A \lor \diamond B$ </td><td>At least one A or B has to be executed.</td></tr><tr><td>Exclusive choice(A, B)</td><td> $(\diamond A \lor \diamond B) \land \neg (\diamond A \land \diamond B)$ </td><td>A or B has to happen, but not both.</td></tr></table>

## References

[1] W.M. van der Aalst, Process Mining: Discovery, Conformance and Enhancement of Business Processes, Springer, 2011.

[2] R. Gopal, J.R. Marsden, J. Vanthienen, Information mining—reflections on recent advancements and the road ahead in data, text, and media mining, Decision Support Systems 51 (4) (2011) 727–731.

[3] W.M. van der Aalst, T. Weijters, L. Maruster, Workflow mining: discovering process models from event logs, IEEE Transactions on Knowledge and Data Engineering 16 (9) (2004) 1128–1142.

[4] A. Weijters, W.M. van der Aalst, A.A. De Medeiros, Process mining with the heuristics miner-algorithm, TU Eindhoven, Tech. Rep. (2006) 166

[5] T. Murata, Petri nets: properties, analysis and applications, Proceedings of the IEEE 77 (4) (1989) 541–580.

[6] F.M. Maggi, R.J.C. Bose, W.M. van der Aalst, Efficient discovery of understandable declarative process models from event logs, Advanced Information Systems Engineering, Springer 2012, pp. 270–285.

[7] J. De Smedt, J. De Weerdt, J. Vanthienen, Multi-paradigm process mining: retrieving better models by combining rules and sequences, On the Move to Meaningful Internet Systems, Springer 2014, pp. 446–453.

[8] J. De Weerdt, M. De Backer, J. Vanthienen, B. Baesens, A multi-dimensional quality assessment of state-of-the-art process discovery algorithms using real-life event logs, Information Systems 37 (7) (2012) 654–676

[9] S.-Y. Hwang, W.-S. Yang, On the discovery of process models from their instances, Decision Support Systems 34 (1) (2002) 41–57.

[10] C.W. Günther, W.M. van der Aalst, Fuzzy mining–adaptive process simplification based on multi-perspective metrics, Business Process Management, Springer 2007, pp.328-343.

[11] J.M.E. van der Werf, B.F. van Dongen, C.A. Hurkens, A. Serebrenik, Process discovery using integer linear programming, Applications and Theory of Petri Nets, Springer 2008, pp. 368–387.

[12] M. Pesic, H. Schonenberg, W.M. van der Aalst, Declare: Full support for looselystructured processes, Enterprise Distributed Object Computing Conference, IEEE 2007. pp. 287-298.

[13] C. Di Ciccio, M. Mecella, A two-step fast algorithm for the automated discovery of declarative workflows, Computational Intelligence and Data Mining (CIDM). 2013 IEEE Symposium on, IEEE 2013, pp. 135 142.

[14] M. Westergaard, C. Stahl, H.A. Reijers, UnconstrainedMiner: Efficient discovery of generalized declarative process models, 2013.

[15] F. Chesani, E. Lamma, P. Mello, M. Montali, F. Riguzzi, S. Storari, Exploiting inductive logic programming techniques for declarative process mining, Transactions on Petri Nets, Springer 2009, pp. 278–295.

[16] Y.-H. Hu, Y.-L. Chen, Mining association rules with multiple minimum supports: a new mining algorithm and a support tuning mechanism, Decision Support Systems 42 (1) (2006) 1–24.

[17] M. Alberti, F. Chesani, M. Gavanelli, E. Lamma, P. Mello, P. Torroni, Verifiable agent interaction in abductive logic programming: the sciff framework, ACM Transactions on Computational Logic 9 (4) (2008) 29.

[18] S. Goedertier, D. Martens, J. Vanthienen, B. Baesens, Robust process discovery with artificial negative events, The Journal of Machine Learning Research 10 (2009) 1305–1340.

[19] S. Sadiq, W. Sadiq, M. Orlowska, Pockets of flexibility in workflow specification, Conceptual ModelingER 2001, Springer 2001, pp. 513–526.

[20] M. Adams, A.H. Ter Hofstede, D. Edmond, W.M. van der Aalst, Worklets: a serviceoriented implementation of dynamic flexibility in workflows, On the Move to Meaningful Internet Systems, Springer 2006, pp. 291–308.

[21] M. Westergaard, T. Slaats, Mixing paradigms for more comprehensible models, Business Process Management, Springer 2013, pp. 283–290.

[22] A. Kumar, W. Yao, Process materialization using templates and rules to design flexible process models, Rule Interchange and Applications, Springer 2009, pp. 122–136.

[23] F.M. Maggi, H.A. Reijers, T. Slaats, The automated discovery of hybrid processes, Business Process Management. 2014

[24] A. Duret-Lutz, D. Poitrenaud, Spot: an extensible model checking library using transition-based generalized büchi automata, MASCOTS, IEEE 2004, pp. 76-83.

[25] F.M. Maggi, R.J.C. Bose, W.M. van der Aalst, A knowledge-based integrated approach for discovering and repairing declare maps. Advanced Information Systems Engineering, Springer 2013, pp. 433–448

[26] F.M. Maggi, A.J. Mooij, W.M. van der Aalst, User-guided discovery of declarative process models, Computational Intelligence and Data Mining (CIDM), 2011 IEEE Symposium on, IEEE 2011, pp. 192–199.

[27] S. vanden Broucke, J. De Weerdt, J. Vanthienen, B. Baesens, A comprehensive benchmarking framework for conformance analysis between procedural process models and event logs in prom, CIDM, IEEE 2013, pp. 254–261.

[28] S. vanden Broucke, J. De Weerdt, J. Vanthienen, B. Baesens, Determining process model precision and generalization with weighted artificial negative events, IEEE TKDE 26 (8) (2013) 1877–1889.

[29] M. Westergaard, CPN Tools 4: multi-formalism and extensibility, Application and Theory of Petri Nets and Concurrency, Springer 2013, pp. 400–409.

[30] C. Haisjackl, I. Barba, S. Zugal, P. Soffer, I. Hadar, M. Reichert, J. Pinggera, B. Weber, Understanding declare models: strategies, pitfalls, empirical results, Software & Systems Modeling (2014) 1–28.

[31] J. Mendling, M. Strembeck, J. Recker, Factors of process model comprehension—findings from a series of experiments, Decision Support Systems 53 (1) (2012) 195–206.

[32] K. Figl, J. Recker, J. Mendling, A study on the effects of routing symbol design on process model comprehension, Decision Support Systems 54 (2) (2013) 1104–1118.

![](/api/attachments/B92SMBA2/fulltext/images/e15df976bb39a886e761e288c70e414f5ea54caf2b4f45faf32b3f876556ffc3.jpg)  
Johannes De Smedt received his MSc degree in Information Systems Engineering from KU Leuven and is currently performing research as a PhD candidate at the Department of Decision Sciences and Information Management, KU Leuven. His scientific interests include business process management, modeling, mining, and simulation, and context-aware workflow systems.

![](/api/attachments/B92SMBA2/fulltext/images/771c23bb4d512f9059b936ae4475c906fd553eef5d985bf0272720532eaac73f.jpg)

![](/api/attachments/B92SMBA2/fulltext/images/60701f2252692aac368202fc321cbf27b0d6489afbbfe0b19d0164e1be4c4479.jpg)

Jochen De Weerdt is an Assistant Professor of Information Systems in the Department of Decision Sciences and Information Management, KU Leuven. His research interests include business process management, process mining, data mining, artificial intelligence, learning analytics and web analytics. Previously, he has been working as a Research Fellow at the Information Systems School of the Queensland University of Technology (QUT) in Brisbane. His research has been published in internationally renowned journals and conferences.

Jan Vanthienen is a full professor of Information Systems in the Department of Decision Sciences and Information Management, KU Leuven. He received the PhD degree in ap plied economics from KU Leuven, Belgium, and has authored or co-authored numerous papers published in international journals and conference proceedings. His current research interests include modeling and mining business rules and decisions, process analytics, and information and knowledge management. Jan received an IBM Faculty Award in 2011 and the Belgian Francqui Chair 2009 at FUNDP. He is co-founde and president-elect of the Benelux Association for Information Systems (BENAIS).
