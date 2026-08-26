---
otero_id: 17668
otero_key: "UV54XWGT"
title: "A decision engine based on rational aggregation of heuristic knowledge"
authors: "Didier Dubois; Jean-Luc Koning"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90080-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision engine based on rational aggregation of heuristic knowledge

Didier Dubois and Jean-Luc Koning

Université Paul Sabatier, Toulouse Cedex, France

Constraint propagation is a matter of logical deduction, but this is not usually sufficient to reach a solution to a problem. Heuristic knowledge is usually needed to go on with the solution search when logical deduction becomes inefficient. The way this second type of knowledge is handled has more to do with decision rather than deduction. In this paper we suggest a mechanism to handle heuristic knowledge based on social choice theory. An analogy is proposed between the cooperation among heuristics expressed as decision rules and the voting problem. This analogy allows to define and justify aggregation modes for results provided by each decision rule, with a view to providing a global decision ranking. An application to job-shop scheduling has been carried out.

Keywords: Decision tables; Social choice; Rule-based systems; Constraint satisfaction; Fuzzy sets; Scheduling

![](/api/attachments/UV54XWGT/fulltext/images/d8e1d4b54479afd20f3ba2a5a392ee881ec4fe65ab901e2f21615639e8ba96c6.jpg)

Didier Dubois (Engineer degree (1975) and Doctor-Engineer degree (1977), Ecole Nationale Supérieure de l'Aéronautique et de l'Espace, Toulouse, France; "Doctorat d'Etat", University of Grenoble, 1983; "Habilitation à Diriger des Recherches", University of Toulouse, 1986) is a full-time researcher at the National Center for Scientific Research (C.N.R.S.). From 1980 till 1983, he worked as a research engineer at the Centre d'Etudes et de Recherches de

Toulouse, in the Production Research area. He co-authored with Henri PRADE two books on fuzzy sets and possibility theory, in 1980 and 1985 respectively and has co-edited a volume on Non-Standard Logics and several special issues of scientific journals. He belongs to the Editorial board of several journals such as Fuzzy Sets and Systems, International Journal of Approximate Reasoning, the French Revue d'Intelligence Artificielle, the International Journal of General Systems and the ORSA Journal on Computing. His main topics of interest are the modelling of imprecision and uncertainty, the representation of knowledge and approximate reasoning for expert systems, operations research and decision analysis. He is the author or co-author of numerous publications, especially in the field of fuzzy sets and their applications to operations research and artificial intelligence.

## 1. Introduction

Pieces of knowledge used in Artificial Intelligence systems are not always dedicated to inference purposes. Parts of them aim at helping in choice processes. There are several examples of such situations:

\- A diagnosis system usually not only tries to determine causes that can explain observations of some faulty behavior, but also suggests remedies that could improve the current situation. This latter part is a choice problem rather than a matter of deduction;

\- A constraint propagation system, used for planning purposes for instance, is not always able to discover a unique solution that obeys the constraints. Moreover, strategies for constraint propagation are not always complete, i.e. the set of solutions they discover when propagation stops may still contain infeasible ones, since for complexity reasons exhaustive search is not always tractable. In both cases, decision processes may be at work in heuristics that give preference to some solutions over others, thus triggering the constraint propagation again;

\- Meta-knowledge, i.e. knowledge about how to manipulate pieces of knowledge often consists of heuristic choice rules that control the inference process.

![](/api/attachments/UV54XWGT/fulltext/images/8ec12ec11676418df29f1670a6fbcb27a61fa17cb35d4c11879035425193a790.jpg)

Jean-Luc Koning received his Ph.D. in computer science from the University of Toulouse (France) in 1990. His thesis work developed a model of heuristic aggregation for constraints satisfaction systems. He then was Visiting Scientist at the Center for Integrated Manufacturing Decision Systems at Carnegie Mellon University (Pittsburgh, USA) in 1991. He worked with Katia Sycara on a case-based reasoning system for the design of mechanical artifacts. He is currently working as Assistant Professor in computer science in a four year college in Valence, France. His research interests include knowledge based systems, case-based reasoning, fuzzy set theory, negotiating models for multi-agent systems.

Correspondence to: Didier Dubois, I.R.I.T. Université Paul Sabatier, 118 route de Narbonne, 31062 Toulouse Cedex, France.

The second example stresses a case frequently encountered when using AI techniques to tackle industrial problems like design, planning or scheduling. Some subproblems have algorithmic solutions; however, no single algorithmic solution exists for the problem in its entirety. Human expertise is required to integrate the subproblems, provide the missing pieces, and guide the search process by making decisions (see for instance (Bachant and McDermott, 1984) for an example of knowledge based system that makes design decisions). Those problems are usually addressed by means of constraint satisfaction systems.

## 2. Constraint satisfaction systems

## 2.1. General behavior

Constraint satisfaction systems are designed to find the values of variables satisfying given constraints. These constraints apply to a set of incompletely specified variables. They appear in the form of logical expressions to be satisfied, of inequalities between numerical parameters, etc. They convey links between variables of the problem. To exploit these relationships, production rules-called constraint propagation rules-are used. They enable the authorized range for each variable to be updated from what is known on the other variables. Modifications come down either to a domain reduction on certain variables, or to the addition of new deduced constraints.

In order to find a set of solutions which meets all the constraints, an algorithm based on a forward chaining inference mechanism successively exploits all applicable constraint propagation rules (Davis, 1987). At each step, new logical deductions result in a reduced domain for the set of solutions. When this constraint propagation algorithm stops three cases may occur:

\- The final solution set is empty. One can then conclude the initial state was inconsistent, i.e. variables domains were too limited and/or constraints were too restrictive;

\- An admissible solution (or set of solutions) has been found. The search succeeds;

\- Constraints can no longer be propagated, even though the set of solutions arrived at is not yet admissible (i.e. the set may still contain infeasible solutions).

In this third situation the end of the propagation is caused by two factors. One factor is that the constraint propagation rules usually only express necessary conditions of admissibility. The other factor is the inability of the individual propagation of constraints to take the interaction between constraints into account. To cope with this issue, search techniques either with or without heuristics are generally contemplated like:

1. Applying the classical Backtrack algorithm (Mackworth, 1977). It consists in choosing a variable at random and in picking (at random too) one of its possible values. In this case ‘random’ usually means ‘the first available’ when variables and their value domain are taken as ordered sets;

2. Applying general heuristics for choosing the next variable to instantiate and choosing its value (Freuder, 1982; Dechter and Pearl, 1988). This approach suits toy problems particularly well but seems to fail when applied in realistic problems. This is usually because these heuristics are generally too simple and do not account for the high connectivity of the constraints. Sadeh proposes different heuristics which improve search efficiency in the domain of job-shop scheduling (Sadeh, 1991);

3. Building a Decision Support System that guides the search for feasible solutions through an aggregation of recommendations about the expected solution—here “aggregation” is synonym to ‘cooperation’.

Clearly, the first technique is poorly efficient in case of large search spaces with few solutions. The two others come down to the same concept. They bring into play a new type of knowledge to enable the search to continue. In the following we will focus on the third alternative.

## 2.2. The necessity for a decision process

There is usually more than one solution for a set of constraints. As a matter of fact, it often happens that some admissible solutions are better than others according to points of view not expressed in constraint propagation rules. Nevertheless these criteria informally exist as advice, heuristics, etc. The interest of such knowledge is to be able to take into account supplementary objectives when the problem seems underconstrained.

![](/api/attachments/UV54XWGT/fulltext/images/5ee4967f13bdbd2530316c4d2244ef065564057e1bb3dfa1286ee30cb970b84b.jpg)  
Fig. 1. A constraint satisfaction system.

This kind of heuristic knowledge is specific to the problem at hand. If put to work in a decision mechanism, it allows advice on the form of the solution to be put forward. The constraint propagation algorithm can then start again. This type of decisions is not logical in the sense that it is not deduced from the constraints. It attempts to determine more quickly a set of admissible solutions that are of particular interest to the user. However, if such a set is found it will not necessarily contain all the admissible solutions since a choice has been made; an alternative choice may have possibly led to other admissible solutions. Similarly, when a dead-end is reached, it may still be possible to find a feasible solution after undoing some earlier (not forced) decisions. When a dead-end state is encountered another heuristic decision must be adopted. Each time a dead-end is reached this procedure is repeated on the last decision that can still be replaced. Dependency-directed backtracking versus simple chronological backtracking consists in selecting a decision other than the previous one (Le Pape, 1988). The absence of solution is only detected when every possible alternative has been considered.

Figure 1 illustrates the connection between a heuristic decision mechanism and a constraint propagation system. Knowledge is represented within circles and reasoning procedures by rectangles. A constraint satisfaction system contains three main components. Loop (I) corresponds to an inference algorithm. When it cannot run any more, and the solutions set arrived at is not admissible, loop (II) is then activated. It makes a decision that modifies the search state and starts loop (I) again. As far as it is concerned, the backtracking mechanism is only called upon when choices produced by loop (II) have to be reconsidered. Issues raised by loops (I) and (III) have been extensively studied (see Le Pape, 1988 for instance). We specifically deal here with loop (II), i.e. with the local decision-making module. Representation of heuristic knowledge is discussed in details in Section 3.

## 2.3. The example of job-shop scheduling problems

Job-shop scheduling problems aim at scheduling a set of jobs on a set of physical resources. Each job consists of a set of operations to be scheduled according to a process plan that specifies a partial ordering among these operations. This problem can typically be formulated as a constraint satisfaction problem (CSP) (Mackworth, 1977). The variables are then the starting times of jobs, constraints are their due dates and the requirement that each machine processes one operation at a time. See (Le Pape and Smith, 1987) for a survey about constraint propagation in factory scheduling.

![](/api/attachments/UV54XWGT/fulltext/images/3f34b9909eaecaaabc08c4a6702fd67c36921604abb4b20a46efb1c9079a0933.jpg)  
Fig. 2. Initial execution intervals.

Let us explain how a constraint satisfaction system would operate using a simplistic scheduling example. Let A, B and C be three operations that have to be processed on the same machine. Duration of $A(d_{A})$ equals 3 time units and the domain of possible values for the starting time of $A(s_{A})$ is [0,4], $d_{B}=3$ and $s_{B}\in[2,5]$ , $d_{C}=2$ and $s_{C}\in[3,8]$ . The corresponding Gantt chart is given in Figure 2 when rectangles show durations and horizontal lines execution intervals.

Suppose that problem solving starts with a constraint propagation step. Loop (I) of Figure 1 is able to produce the new state: $s_A \in [0,2]$ , $s_B \in [3,5]$ and $s_C \in [3,8]$ . Two constraints are found: $A$ before $B$ and $A$ before $C$ . The logical knowledge brought into play in loop (I) refers to handling time intervals. It aims at satisfying the capacity constraints: $(s_X + d_X) \leq s_Y) \vee (s_Y + d_Y \leq s_X)$ . If both parts of this generic disjunction are found to be false than it is impossible to schedule operations $X$ and $Y$ without violating time constraints. If one part only is found to be false then $X$ 's and $Y$ 's domain of value are to be updated (i.e. the earliest and latest starting times, $es$ and $ls$ ). For instance, from the initial state the impossibility of $B$ before $A$ ( $s_B + d_B \not\leq s_A$ ) may be immediately derived, thus $es_B = es_A + d_A$ and $ls_A = lf_B - d_B$ , where $lf_B$ is the latest finishing time of operation $B$ . This update implicitly imposes that operation $B$ should follow operation $A$ . The same reasoning leads to finding that $C$ should follow $A$ . The new Gantt chart is shown in Figure 3.

At this point, no new inferences can be made by the constraint propagation module since both $(s_{B} + d_{B} \leq s_{C})$ and $(s_{C} + d_{C} \leq s_{B})$ can be true. Loop (II) of Figure 1 is then activated. Using some heuristic knowledge via a decision process, this module either suggests B before C or C before B. One notices that decision B before C preserves slack time for the processing of both B and C which is not the case with the other ordering. This is the type of heuristic advice (“preserve slack time”) one may want to take into account and that will typically be found in loop (II). Usually there may be more than one such piece of heuristic knowledge available, and they may contradict one another.

The rest of this paper is devoted to the handling of this possibly conflicting heuristic knowledge. We will come back to this example later on in Section 3.2 and also in Section 3.5.

## 3. Modelling heuristic knowledge

## 3.1. Heuristics as decision tables

As seen previously, constraint satisfaction systems take into account two types of knowledge: (1) logical knowledge that conveys constraint propagation rules, and (2) domain specific heuristic knowledge. This second sort corresponds to information coming from various points of view on how to solve the problem: each point of view provides specific suggestions in a given search state. They may be put in the form of correspondence tables between several mutually exclusive conditions and several antagonistic decisions.

A table $T_{j}$ will be represented with a set of production rules:

$$
\begin{array}{l l} T _ {j} \colon (w _ {j}) & \langle \text {condition} j _ {0} \rangle \\ & \text {if} \langle \text {condition} j _ {1} \rangle \quad \text {then} \langle \text {decision} \delta_ {1} \rangle \\ & \text {else if} \langle \text {condition} j _ {2} \rangle \quad \text {then} \langle \text {decision} \delta_ {2} \rangle \\ & \vdots \\ & \text {else if} \langle \text {condition} j _ {r - 1} \rangle \text {then} \langle \text {decision} \delta_ {r - 1} \rangle \\ & \text {else} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \langle \text {decision} \delta_ {r} \rangle . \end{array}
$$

Fig. 3. Execution intervals after applying logical knowledge.  
![](/api/attachments/UV54XWGT/fulltext/images/8b1bf54fabdf4c0ed8d1558f8938c169f0175523679e567479467046584da88d.jpg)

Let $\langle$ decision $\delta_1\rangle \ldots \langle$ decision $\delta_r\rangle$ be decisions viewpoint $j$ contemplates. Each decision corresponds to adding a new constraint suggested by the viewpoint, i.e. usually reducing a variable range. $T_{j}$ 's first line - $\langle$ condition $j_0\rangle$ - expresses the general application condition of viewpoint $j$ . When it is not satisfied no production rule of table $T_{j}$ may be triggered. $T_{j}$ 's $i$ th condition is a description of the situation required by standpoint $j$ in order to apply decision $\delta_i$ . $w_{j}$ is the weight expressing the importance of the point of view conveyed by table $T_{j}$ . $T_{j}$ 's last line may correspond to the case where the decision is to add no constraint on the variables referred to in $\langle$ condition $j_0\rangle$ . Viewpoint $j$ then acknowledges its own lack of relevance in the current situation and abstains from participating to the final decision in situation $j_{r}$ . This situation corresponds to the case where condition $j_0$ is satisfied but all conditions $j_1\ldots j_{r-1}$ fail.

## 3.2. Examples of decision tables

The simple scheduling problem introduced in Section 2.3 would typically require the firing of several points of view. We now present two of them in the decision table formalism.

Shortest Processing Time (SPT):

General condition: X and Y are two concurrent operations on the same machine,

Rule 1: if duration of $X$ is significantly smaller than duration of $Y$ then $X$ precedes $Y$ .

Rule 2: if duration of X is significantly greater than duration of Y then Y precedes X.

Rule 3: else no precedence constraint between X and Y.

This heuristic conveys a point of view that favors the early processing of short operations. This point of view is relevant when there is a substantial difference in duration operation X and operation Y; rule 3 shows that otherwise this table does not suggest any specific decision. Notice that by “concurrent operations on the same machine” we mean two operations that can possibly overlap in time, but are not allowed to.

Earliest Finishing Time (EFT):

General condition: X and Y are two concurrent operations on the same machine,

Rule 1: if latest finishing time of $X$ is significantly smaller than $Y$ 's then $X$ precedes $Y$ .

Rule 2: if latest finishing time of X is significantly greater than Y's then Y precedes X.

Rule 3: else no precedence constraint between X and Y.

This heuristic conveys a point of view that favors the processing of the operation that must end first. Again this point of view is relevant when there is a substantial difference between both latest finishing times; rule 3 shows that otherwise this table suggests no decision.

Notice that:

\- Domain specific heuristics are easy to express within the decision table formalism;

\- In the general case all the tables do no necessarily suggest the same decisions. Each of them may partition the set of situations differently (cf. Section 3.4);

\- Logical knowledge is rather general (e.g. knowledge about time intervals) whereas decision knowledge is much more problem dependent (job-shop dependent here).

Decision tables may represent pieces of advice on the way to guide the constraint propagation process toward a solution. They may also represent necessary conditions to be satisfied by the problem variables in order to meet some problem constraints (conditions that cannot be directly derived by the constraint propagation module). Both types of knowledge will not be treated the same way. Different pieces of advice conveying heuristics will generally suggest different decisions, possibly incompatible ones. On the other hand, necessary admissibility conditions are imperative and cannot be questioned (Dubois, 1989).

## 3.3. Fuzzy decision tables

In most rule-based systems preconditions are expressed in a rigid manner, they apply only when the data correspond exactly to the description of the situation. To take into account the imprecise nature of the knowledge on a problem and also to be able to describe the typical situations in a quantified manner, fuzzy set theory (Zadeh, 1965) is used here. This theory allows more or less typical situations to be represented in terms of fuzzy sets on the attributes handled by the table. The way the table conditions are expressed by means of fuzzy sets is detailed hereafter.

![](/api/attachments/UV54XWGT/fulltext/images/519022f6c32defe4ad877b90d51b34eeefa936ee126eef1dc52028634b99a708.jpg)  
Fig. 4. The duration of an operation of about $3\frac{1}{2}$ time units.

A line of a decision table will be encoded as a rule:

$$
\text { if } x _ {1} \in A _ {1} \land x _ {2} \in A _ {2} \land \dots \land x _ {k} \in A _ {k}
$$

$$
\wedge x _ {1} ^ {1} \mathcal {R} _ {1} x _ {2} ^ {1} \wedge \dots \wedge x _ {1} ^ {m} \mathcal {R} _ {m} x _ {2} ^ {m} \text {   then   } \langle \text { decision } \rangle
$$

where the $x_{i}$ , $x_{1}^{j}$ , $x_{2}^{j}$ are data of the problem or parameters that describe the current situation, $A_{1}\ldots A_{k}$ are fuzzy sets and $R_{1}\ldots R_{m}$ are fuzzy relations. Logic connectives ‘∧’ can be replaced by ‘∨’, and negation can also be used. These conjunction, disjunction and negation operators are easy to implement in fuzzy logic, respectively by means of union, intersection or complementation operations between fuzzy sets (Dubois and Prade, 1988).

## 3.3.1. Fuzzy unary predicates

Preconditions are of the form $x_{i} \in A_{i}$ . They are expressed as unary predicates called fuzzy when the prescribed range of the attribute value forms a set with no precise bounds – a fuzzy set in fact. In a fuzzy assertion like $x_{i} \in A_{i}$ – or equivalently $x_{i}$ is $A_{i}$ – the predicate $A_{i}$ represents the relevant values of attribute $x_{i}$ . The fuzziness of the predicate expresses that among values of $x_{i}$ , some are more or less relevant than others. For instance, in the assertion “duration of operation X is about $3\frac{1}{2}$ time units” $x_{i}$ is the duration of operation X and $A_{i}$ the fuzzy set “about $3\frac{1}{2}$ time units”. The fuzzy set concept generalizes the ordinary set concept. A fuzzy set $A_{i}$ on a universe $\Omega$ is characterized by its membership function $\mu_{A_{i}}: \Omega \to [0,1]$ . $\forall \omega \in \Omega$ , $\mu_{A_{i}}(\omega)$ represents to what extent $\omega$ belongs to $A_{i}$ . If $\mu_{A_{i}}(\omega) = 0$ it does not belong to $A_{i}$ at all, if $\mu_{A_{i}}(\omega) = 1$ it totally belongs to $A_{i}$ , if $\mu_{A_{i}}(\omega) \in ]0,1[$ membership is more or less complete. A representation of the characteristic function $\mu_{A_{i}}$ , of fuzzy set $A_{i}$ (“about $3\frac{1}{2}$ time units”) is shown on Figure 4. In this case $\Omega$ represents the duration of an operation. $\mu_{A_{i}}$ is an easy way of encoding a preference relation on a subset of $\Omega$ .

## 3.3.2. Fuzzy comparators

The condition part refers also to fuzzy comparators (of the form $x_{1}^{j}\mathcal{R}_{j}x_{2}^{j}$ ). A comparator is a binary predicate that measures a difference of magnitude between two attribute values. Similarly to fuzzy predicates, this difference of magnitude can be represented by means of fuzzy sets. In the condition “duration of X is significantly smaller than duration of Y” (see decision table exhibited in Section 2.3) the fuzzy comparator $R_{j}$ stands for ‘significantly smaller than’. It concerns $x_{1}^{j}$ and $x_{2}^{j}$ which are in this case the durations of operations X and Y. This comparator will apply when the value of the first attribute is significantly smaller (according to the user’s definition) than the second attribute value.

![](/api/attachments/UV54XWGT/fulltext/images/c9fa8db2eb6e8db7837517239304f0376152b12f3a0774e86a9b21037916d6f7.jpg)  
Fig. 5. Fuzzy comparators appearing in decision table SPT.

There are two ways of defining a comparator whether the magnitude difference between both attributes is expressed (1) in a relative way, or (2) in an absolute way. It depends on how the attributes are to be compared:

1. In the relative case one is interested in the value of the ratio x/y were x and y relate to the two attribute values (we then assume x and y are of same sign);

2. In the absolute case one takes into account the difference $(x - y)$ .

The notion of fuzzy comparator then comes down to the one of a unary fuzzy predicate. Indeed, in the absolute case a comparator is specified by $(x_{1}^{j}-x_{2}^{j})\in B_{j}$ , and in the relative case by $x_{1}^{j}/x_{2}^{j}\in B_{j}$ , where $B_{j}$ is a fuzzy set on the reference domain. The representation of the membership function associated to the comparator ‘significantly smaller than’ is shown in Figure 5 in the absolute mode. In this case $\Omega$ refers to the domain of possible values for the difference of the durations of two operations.

## 3.4. Fuzzy pattern matching and decision tables

This way of representing situations descriptions in terms of fuzzy sets requires that decision tables be exploited by means of fuzzy pattern matching. When prototypical situations are described by vague specifications (patterns), the matching between the description of the prototypical situation and the data is not all or nothing any more. In this case a decision can be more or less recommended. In (Cayrol et al., 1982) and (Dubois et al., 1988) a fuzzy pattern matching technique based on possibility and necessity measures on the [0,1] interval is given. Those measures assess the compatibility between possibly imprecise data and what is required by the pattern. With this approach each component of the data and each elementary requirement are respectively associated to a possibility distribution and a fuzzy set.

Here the state of progress in the problem resolution state s is assumed to be described in a precise way, and the prototypical situation to be described by a fuzzy set F built from the elementary rule conditions by means of fuzzy logic connectives. Then possibility and necessity degrees coincide with the membership degree $\mu_{F}(s)$ that weights the relevance of the decision suggested in situation F. Once linked to the decision, this number – which is never a degree of uncertainty – becomes close to a utility degree, as well as the table weight $w_{j}$ . The value $\mu_{F}(s)$ refers to what will be called $x_{ij}$ in Section 4. The application of fuzzy pattern matching techniques to decision tables has already been considered in the framework of data bases (Francioni and Kandel, 1988).

In the classical case (not fuzzy), conditions of a decision table can only be respected in an all or nothing manner. Since they induce a partition over the set of situations, one and only one rule is satisfied at a time, and thus one and only one decision is put forward at a time. The risk of such an approach is that a slight change in the current situation might lead to a very different decision. When conditions are conveyed by means of fuzzy sets, a matching degree between the current situation and the one described by the condition is computed (cf. Section 3.5). These degrees (one per table rule) take their value in [0,1] were 0 represents incompatibility and 1 total compatibility (when fuzzy sets are normalized). With this notation the classical setting is found again when one prevents the degrees from being shaded, i.e. to lie strictly between 0 and 1.

A fuzzy partition $\{F_{1}, F_{2}, \ldots, F_{n}\}$ of a set is such that for each element x of the set the sum of the membership grades $\mu_{F_{i}}(x)$ is equal to one. This notion is due to Ruspini (see Dubois and Prade, 1980). In the following, decision tables are forced to decompose the set of situations into a fuzzy partition. Of course this partition may vary from one table to another. This exactly reflects the variety of points of view. In this case, the summation of degrees obtained from each rule in the table equals 1; this means the encountered situation is entirely taken into account by the concerned viewpoint (see Figure 5). If the summation of degrees was greater than 1 it would mean that the conditions of the table significantly overlap. Since several degrees may be different from 0 several decisions are proposed. The extent to which they are recommended corresponds to the compatibility degree between the situation described by the corresponding condition and the current situation. In the scope of multiple points of view, the fuzzy set approach enables a clear cut choice of the decision to be obviated when meaningless for a given decision table. Only these preferences will be input to the aggregation module.

## 3.5. Example of fuzzy pattern matching

We now illustrate the fuzzy pattern matching procedure with an example. For this purpose, the decision table SPT introduced in Section 3.2 is taken up. The membership function of the comparator that appears in the second rule of this table can be represented by the left side of a trapezoid as seen in Figure 5. It enables the relation ‘significantly greater than’, to be characterized by two thresholds $a_{1}$ and $a_{2}$ :

\- $a_1$ is the value of $(d_X - d_Y)$ – in absolute mode – from which a value $d_X$ begins to be significantly greater than a value $d_Y$ . $d_X$ and $d_Y$ are respectively the durations of operations $X$ and $Y$ ;

\- $a_{2}$ is the value of $(d_X - d_Y)$ – in absolute mode – from which a value $d_X$ is considered fully significantly greater than a value $d_Y$ .

Let us suppose $a_{1}$ equals 0.5 and $a_{2}$ equals 2 which means that when the difference between two durations is less than or equal to half a time unit the comparator ‘significantly greater than’ will be false and when this difference is greater or equal to 2 time units it will be true. Figure 5 shows the membership function thus built. The dual relation ‘significantly smaller than’ can be deduced by symmetry. The corresponding two thresholds $b_{1}$ and $b_{2}$ are then respectively equal to -0.5 and -2. This means the duration of operation X is definitely significantly smaller than duration of operation Y when $(d_{X}-d_{Y})$ is less than or equal to -2, and is not at all significantly smaller than duration of operation Y when $(d_{X}-d_{Y})$ is greater than or equal to -0.5. One may notice the fuzzy set attached to the implicit condition of the 'else' rule (rule number 3 of table SPT) can be found by complementation. Indeed, it intuitively corresponds to the fact that this rule becomes relevant when no other is. Because of the fuzzy representation, the 'else rule' gradually becomes relevant as the other rules become less relevant. The corresponding membership function is shown in dotted line on Figure 5.

Table SPT is now completely defined. Let us apply the fuzzy pattern matching procedure to the situation arrived at in Section 2.3 where the scheduling of operations B and C still need to be done. $d_{B}$ (duration of operation B) equals 3 and $d_{C}$ equals 2. Since $(d_{B}-d_{C})$ equals 1, one can see on Figure 5 that the assertion “B is significantly greater than C” is partially true (to the extent of 1/3) whereas the assertion “B is significantly greater than C” is false. The pattern matching degree that corresponds to the “else” condition is 2/3. As explained in Section 3.4 these degrees express to what extent the various decisions are recommended.

The fuzzy pattern matching provides a dynamic assessment of similarity between the situations described by the table and the considered state. Thus it is possible to rank (for each table) the decision it advocated according to the induced grading given by this assessment. Here, the alternative that has the highest pattern matching degree is the “indifference (of decision table SPT) between both ways of scheduling B and C”. The decision to schedule C before B is weakly suggested (the pattern matching degree equals 1/3), and scheduling B before C is not suggested at all (the pattern matching degree equals 0).

At the end of the triggering of all the rules of all the tables, there will be as many valued decisions rankings as points of view. The problem now is to combine the various points of view in order to determine the best decision(s) to apply. It is a matter of finding the most rational ways of aggregating the decisions rankings.

## 4. Aggregation of preference patterns using a social choice framework

This section tackles the points of view aggregation problem, set in terms of votes. This analogy, previously put forward by the authors (Dubois and Koning, 1989), appears more distinctly when decision tables are identified with voters and decisions with candidates for whom to vote. Section 4.2 outlines a major result of collective choice theory. Then an application to the aggregation of preference rankings is made in Section 4.3, and new results found in the fuzzy set setting are exhibited in Section 4.4. Let us first review the current literature regarding the use of decision-making techniques in problem solving.

## 4.1. Decisional aspects in knowledge-based systems

Despite the pervading presence of decision processes in Artificial Intelligence, not so much work has been devoted to a proper modeling and implementation of decision-oriented heuristics. The literature dealing with this topic is rather recent and preliminary. Yet, as pointed out by Doyle (1990) preference plays a significant role in reasoning, and logic alone often provides little guidance to put heuristic methods on a sound theoretical basis.

A first approach to the selection of decisions in knowledge-based systems is to use some criterion that selects the best decision table (or heuristic) among those applicable and to let this table suggest a decision. This is typical of conflict resolution methods in expert systems. An alternative is to rank decision tables according to some priority and to try to apply the table ranked first insofar as it applies, then try to apply the next one if the first one fails, and so forth. These methods are rather crude because decisions are made according to a single point of view. It is difficult to let the solution reflect the preferences of a user with these strategies.

A second approach is to appeal to some form of multiple-criteria decision-making approach. Keeney (1988) has advocated the usefulness of utility theory for driving the inference process of expert systems. Langlotz and Shortliffe (1989) implement multiple-attribute value functions in a planning system. Adiga and Cochran (1985) rather advocate Saaty's analytic hierarchy framework. Pinson (1987) uses results in cognitive psychology where several modes of aggregations of criteria have been laid bare (linear additive; conjunctive, disjunctive and lexicographic). These modes of aggregation combine importance weights and risk coefficients provided in a qualitative way by the user. This framework is more flexible than the one of Klein and Shortliffe (1990) since the latter only uses the linear additive mode of aggregation. Hierarchies of criteria can be modeled in the software for controlling manufacturing systems devised by Hintz and Zimmermann (1989), in the setting of fuzzy set theory.

A third approach, that has not yet been widely explored with reasoning systems is social choice theory. This theory, elaborated by economists and social scientists (Moulin, 1988), aims at studying voting procedures. It supplies interesting results that can be applied for decisionmaking. In our work we have developed a strong analogy between handling conflicting decision rules and social choice theory, where voters have to choose among candidates. In the classical case, each voter ranks the candidates according to his preferences. To obtain a global ranking of the candidates, the individual rankings are aggregated. The way to aggregate the rankings is defined according to the properties one may want the voting procedure to satisfy.

Some outcomes of social choice theory – on which there exists an abundant literature – are relevant for handling heuristic knowledge in constraint-directed systems. The core idea is that a set of heuristics may behave like a set of individuals who have to vote and that finding the best solution in the sense of a group of possibly antagonistic rules is analogous to a social choice problem. Similar considerations can be found in very recent works by Doyle and Wellman (1991) for the choice of an extension in default reasoning. They come up with negative results regarding the possibility of improving over the rigid lexicographic priority mechanisms that have been proposed for conflict resolution. In our work we try to cope with these difficulties using fuzzy set theory to represent preference in a more expressive way than with qualitative linear orders.

## 4.2. Social choice theory: some classical results

Arrow has proposed conditions every voting procedure should satisfy (Arrow, 1963). He also proved a number of theorems. Before recalling one of them, let us specify the terminology used in the following.

An individual vote is the ranking of all the candidates by decreasing order of preference for the elector. It is not only the expression of the preferred candidate. The notion of individual preference corresponds to what is called sometimes weak preference. We write $x \geq y$ to mean that an individual prefers candidate x at least as much as candidate y. This weak preference relation can be split into two sub-relations: x > y means the candidate x is strictly preferred to candidate $y (y \neq x)$ , and $x \sim y$ means the voter is indifferent between the two alternatives ( $x \geq y$ and $y \geq x$ ). By definition weak preference is a complete preorder.

A voting procedure is a function that provides a collective ranking from the individual rankings given by the voters. For instance, (1) the plurality rule takes into account the number of times a candidate is at the top of any individual ranking. The greater this number the higher the candidate is in the global ranking. (2) The intensity rule gives a candidate as many tokens as the number of candidates he outranks in an individual ranking. The tokens a candidate receives for each individual ranking are added and this total score determines the position of the candidate in the global ranking. (3) In the majority rule, a candidate x is preferred over another candidate y if and only if the number of individuals ranking x before y is at least as large as the number of individuals ranking y before x. In the case of a panel of two candidates these voting procedures are equivalent. For three or more alternatives, possible ambiguities arise; none of these voting procedures is completely satisfactory.

Arrow tackled this issue by stating the properties a voting procedure should satisfy when there are at least 3 candidates x, y and z:

Completeness: The voting procedure ranks each pair of candidates (i.e. it does not exist two candidates for whom one does not know the weakly preferred one): $x \geq y$ or $y \geq x$ .

Transitivity: In the final collective ranking the preference relation must be transitive: if $x \geq y$ , $y \geq z$ then $x \geq z$ .

Unrestricted domain: The voting procedure is defined whatever the individual votes are.

Unanimity: If each individual strictly prefers candidate x to candidate y, the collective ranking must then strictly prefer x to y.

Independence of irrelevant alternatives: The collective ranking of any pair of candidates only depends upon individual rankings of the candidates from this pair. For instance, if one was to find out whether a group of people prefers coffee or tea, individual preferences between tea and coke must not influence this choice.

After having defined and justified these properties, Arrow showed in the theorem bearing his name, that the only voting procedure that verifies them is the dictatorship (i.e. one individual imposes his choice on the others) in the case of three or more candidates. In our application, because of this result, seeking a way to aggregate results coming from various points of view that satisfy these five properties is vain. It will consist in selecting a particular point of view and rejecting the others if one takes into account only the ranking induced on the decisions. Similar conclusions are emphasized by Doyle and Wellman (1991) in non-monotonic reasoning. So as to avoid the conclusion of Arrow's theorem, one may want either to abandon or weaken one or several properties and find a voting procedure compatible with this new set of axioms. Unfortunately, relaxing the initial properties make the voting procedures counterintuitive or little decisive (e.g. they allow preference intransitivity in the collective ordering), as long as they are not anti-democratic. The ideal voting procedure thus does not exist.

The right of veto of an individual is defined as the possibility to object to a strict collective preference different from his own. A voting procedure that would allocate a right of veto to each voter in order to distribute in an egalitarian way the power, would rarely be decisive since two opposite preferences on a pair of candidates result in indifference or conflict. An oligarchy is a set of voters that has, as a group, the power to impose on the remaining voters, its strict and unanimous preference for any pair of candidate. Moreover, each oligarchy member, as an individual, has the power to impose its veto against a strict collective preference different from his own. When an oligarchy contains only one individual it is a dictatorship. The more members it contains, the more egalitarian the power distribution. However, an increase in the size of an oligarchy increases indecisiveness at the same time.

In a decision table-based system, it seems interesting to keep these notions of veto and oligarchy. Indeed, unlike with individuals, giving greater importance to certain viewpoints against others may be desirable. Tables that make advice-like decisions will have less priority than those making imperative-like decisions. When an imperative table votes in a certain way without being contradicted by the others, this decision is made without taking care of votes from tables providing opposite advice. Furthermore, if a table providing imperative decisions eliminates a certain decision, it is legitimate to prevent this decision from being chosen. This intuitive operation mode of imperative decision tables totally fits the oligarchy's definition.

## 4.3. Aggregation of antagonistic preferences for decision tables

Let us analyze our problem in terms of the voting theory. A decision table can be considered as an elector and a decision as a candidate to vote for. A table vote then corresponds to the list of ranked decisions it will have been able to make. A table represents a point of view. Each point of view may have an opinion on a decision that differs from the others or even have no opinion at all on certain decisions. Consequently, decision rankings given by the tables do not necessarily contain the very same decisions even though some of them may be encountered in many lists. This means several rules pronounced in favor of a decision.

Arrow's impossibility theorem shows it is not sufficient to bring into play rankings in order to obtain satisfactory preference aggregation modes (i.e. different from dictatorship and nevertheless meeting the five properties stated in Section 4.2). The expressive power of the preference intensity vectors being greater than mere partial preorders, one may hope to somehow escape the theorem's conclusions by adding to the preference rankings an intensity measure. This approach meets Yager's (1989) for whom aggregating a group of preferences becomes possible when a ranking scale, more meaningful than a mere preorder, is introduced. He also expresses preferences by means of fuzzy sets that convey to what extent candidates satisfy a voter. In our case one tries to express to what extent a decision is advocated by a table. This enables a vote to be represented by a ranked and valued list of decisions. Those valuations can be obtained owing to the gradual – fuzzy - character of decision tables as seen in Section 3.3.

Let $\Delta = \{\delta_1, \ldots, \delta_m\}$ be a finite non-empty set of alternatives that are to be evaluated by a board of experts $\mathcal{T} = \{T_1, \ldots, T_n\}$ . Each expert is supposed to rank each alternative according to a continuous scale that is, by convention, the unit interval [0,1]. Let $x_{ij}$ be the rating for alternative $a_i$ given by expert $T_j$ . For instance $\Delta$ is a set of artists the board of examiners $\mathcal{T}$ has to rank according to their skill, by using (as often made) a numerical grading scale. Each expert comes up with a ranking $F_j$ that may be considered as a fuzzy set whose membership function $\mu_{F_j}$ is such that $x_{ij} = \mu_{F_j}(\delta_i)$ . $F_j$ is the discrete fuzzy set of alternatives preferred by expert $T_j$ , $x_{ij}$ may be seen as the matching degree between $a_i$ and an ideal alternative according to $T_j$ . In the case of decision tables, $\Delta$ is the set of all possible decisions and $\mathcal{T}$ a set of n tables. In a vote, decisions are ranked by decreasing order of degree ( $x_{ij}$ ) to which the tables advocate them. In the following, this coefficient will be represented by $x_{ij}$ that grades the interest of a decision $\delta_i$ for a table $T_j$ . By definition $x_{ij} = 1$ conveys maximal preference, $x_{ij} = 0$ rejection, and $x_{ij} = 0.5$ indifference about $\delta_i$ . With this definition the vote of a table $T_j$ can be represented by a fuzzy set $F_j$ on $\Delta$ . Note that in the case when $\mu_{F_j}(\delta_i)$ comes from $T_j$ , one should have that $\sum_i \mu_{F_j}(\delta_i) = 1$ because the fuzzy conditionparts of rules in $T_j$ form a fuzzy partition of the state space. However this condition is not requested in the general social choice framework.

Once the decision rankings are replaced by fuzzy sets as just defined, it is interesting to carry the rationality properties (given in Section 4.2) over to this formalism in order to find the fuzzy voting procedures satisfying them. This study has been accomplished in a systematic manner on Arrow's properties but also on different conditions which a voting procedure may satisfy in (Dubois and Koning, 1991). This same reference deals with aggregation functions (here operations on fuzzy sets) that are to be applied in order to satisfy a particular set of conditions. The main results are recalled now.

## 4.4. Axioms and fuzzy aggregation functions

The voting problem with decision tables becomes now a problem of aggregating n fuzzy sets on a set $\Delta$ into a fuzzy set F. It is a matter of finding f such that $f(F_{1}, F_{2}, \ldots, F_{n}) = F$ . Let us see some of the conditions an aggregation function f should satisfy.

## 4.4.1. Axioms

All the possible axioms are not required with the same strength, and do not pertain to the same purpose. They can be classified in three groups:

\- Imperative conditions whose violation leads to obviously counterintuitive aggregation modes,

\- Technical conditions that just facilitate the representation or the calculation of the aggregation function,

\- Optional conditions that naturally apply in special circumstances but are not necessarily universally accepted. They are acceptable as soon as they do not lead to impossibility results, or restrict too much the range of admissible aggregations.

Insofar as a democratic aggregation is assumed, the imperative conditions are:

Unanimity in rejection, acceptance and indifference: If every voter is indifferent with respect to a decision then the final decision ranking also is $(\exists\delta_{i}, \forall j, x_{ij}=0.5 \Rightarrow \mu_{F}(\delta_{i})=0.5)$ ; the same for acceptance $(x_{ij}=1 \Rightarrow \mu_{F}(\delta_{i})=1)$ and rejection $(x_{ij}=0 \Rightarrow \mu_{F}(\delta_{i})=0)$ .

Positive association of social and individual values in its non-strict form: If an individual increases his preference intensity for $\delta_{i}$ then the social preference for $\delta_{i}$ cannot decrease. It means that if $F_{j}^{\prime}$ and $F_{j}$ are such that $\mu_{F_{j}} \leq \mu_{F_{j}^{\prime}}$ (i.e. in fuzzy set terms, $F_{j} \subseteq F_{j}^{\prime}$ ) then $f(F_{1} \ldots F_{j} \ldots F_{n}) \subseteq f(F_{1} \ldots F_{j}^{\prime} \ldots F_{n})$ i.e. $f$ is monotonic with set-inclusion.

Minimal democracy: No one has absolute veto nor is a dictator in every situation.

Neutrality with respect to alternatives: The aggregation function does not depend upon the alternatives. If $\delta_{i}$ and $\delta_{i'}$ are such that $x_{ij} = x_{i'j}$ , $\forall j \in \{1, \ldots, n\}$ then $\mu_{f(F_1 \ldots F_n)}(\delta_i) = \mu_{f(F_1 \ldots F_n)}(\delta_{i'})$ . Neutrality with respect to the intensity scale: Assume that the alternatives are rated in terms of distaste intensities instead of preference intensities. Then the social distaste pattern should be built from individual distaste function with the same aggregation function as preferences. Indeed distaste and preference are just a matter of naming the assessment criterion (i.e. choosing the good or the bad alternatives) and the aggregation function should not depend on this name.

Continuity: An infinitesimal modification in the individual preference intensities only induces an infinitesimal modification in the collective preferences.

One technical condition would be the independence of irrelevant alternatives (cf. fifth Arrow's condition in Section 4.2) which requests that the social preference intensity for $\delta_{i}$ only depends on the individual preference intensity for $\delta_{i}$ , and not for $\delta_{i'}$ , $i' \neq i$ . Together with the neutrality of alternatives it enables the aggregation function to be represented by a mapping $\phi: [0,1]^n \to [0,1]$ such that

$$
\forall \delta_ {i}, i \in \{1, \dots , m \},
$$

$$
\mu_ {F} (\delta_ {i}) = \phi (x _ {i 1}, x _ {i 2}, \dots , x _ {i n}) \stackrel {\text { def }} {=} x _ {i}.
$$

## 4.4.2. Aggregation functions

If this technical condition is added to the imperative ones then the qualified class of fuzzy set operators for voting-like aggregation procedures is the class of symmetric sums that has been introduced in fuzzy set theory by Silvert (see Silvert, 1979; Dubois and Prade, 1988). On the whole, the results of our investigation can be compared with those that have been found following Arrow. Namely in classical choice theory there is no social choice rule that can be at the same time democratic, decisive and rational. Here rational means “obeying Arrow’s axioms”. Moreover three rules satisfy only two of these requirements: (1) the majority rule is democratic and decisive, (2) the unanimity rule is democratic and rational, (3) dictatorship is decisive and rational. In the fuzzy set setting the following families of aggregation operations are many-valued counterparts of these three rules. The median and the minimum operations match with the unanimity rule, the arithmetic mean matches with the majority rule, the maximum operation and the associative symmetric sums match with more or less tough dictatorships.

Associative symmetric sums: Those functions admit the following properties:

\- Negative individual opinions result in reinforced social negative opinion and the same for positive opinion, while contradictory opinions compensate. If $x_{ij} < 0.5 < x_{ik}$ then $\phi(x_{ij}, x_{ij}) < x_{ij}$ , $\phi(x_{ik}, x_{ik}) > x_{ik}$ and $\phi(x_{ij}, x_{ik}) \in [x_{ij}, x_{ik}]$ ;

\- Social choice is forbidden by the existence of extreme conflict between two individuals in a society. If $\exists x_{ij}$ , $x_{ik}$ such that $x_{ij} = 0$ , $x_{ik} = 1$ , $\forall k \neq j$ then $\phi(x_{i1}, \ldots, x_{in})$ is undefined. Arrow's third axiom (unrestricted domain) is thus violated;

\- An indifferent vote does not modify the collective choice, $\phi(x_{ij}, x_{ik}, 0.5) = \phi(x_{ij}, x_{ik})$ ;

\- Any individual has a right of veto against others when they do not oppose him completely. If $\exists x_{ij} = 0$ and $x_{ik} < 1$ , $\forall k \neq j$ then $\phi(x_{i1}, \ldots, x_{in}) = 0$ ;

\- Any individual can be a dictator if other individuals do not completely reject his choice. If $\exists x_{ij} = 1$ and $x_{ik} > 0$ , $\forall k \neq j$ then $\phi(x_{i1}, \ldots, x_{in}) = 1$ .

An example of such functions is:

$$
\begin{array}{r l} & {\phi (x _ {i 1}, \dots , x _ {i n})} \\ & {\qquad = [ x _ {i 1} \cdot x _ {i 2} \cdot \dots \cdot x _ {i n} ] / [ x _ {i 1} \cdot x _ {i 2} \cdot \dots \cdot x _ {i n}} \\ & {\qquad + (1 - x _ {i 1}) \cdot (1 - x _ {i 2}) \cdot \dots \cdot (1 - x _ {i n}) ].} \end{array}
$$

Associativity belongs to the set of optional conditions and is not always desirable because it leads to weight the opinion of a group of n - 1 individuals in the same way as the opinion of the nth individual. This state of fact is not acceptable when individual veto or dictatorship is rejected.

Means: Those functions are the counterparts of the majority rule. They admit the following properties:

\- Idempotence: This is a strong unanimity condition that does not the enable reinforcement effect in preference intensities. If $x_{i1} = x_{i2} = \ldots = x_{in} = x_i$ then $\phi(x_i, x_i, \ldots, x_i) = x_i$ .

\- Adding or withdrawing an indifferent vote modifies the global result by approaching or getting away from the collective indifference. If $x_{ij} < 0.5$ (resp.: $x_{ij} > 0.5$ ) then $\phi(x_{ij}, 0.5) \in [x_{ij}, 0.5]$ (resp.: [0.5, $x_{ij}$ ]).

The typical operation of this kind is the arithmetic mean:

$$
\phi (x _ {i 1}, \dots , x _ {i n}) = \frac {x _ {i 1} + x _ {i 2} + \dots + x _ {i n}}{n}
$$

which is a well known utilitarian aggregation (Moulin, 1988).

The only associative symmetric sum that is a mean is the median:

$$
\begin{array}{l} \phi (x _ {i 1}, \dots , x _ {i n}) \\ = \operatorname{med} \left(\min _ {j} (x _ {i j}), \max _ {j} (x _ {i j}), 0. 5\right), \end{array}
$$

but this function is not very decisive since it leads to indifference as soon as there is some contradiction in the group, i.e. as soon as $\exists x_{ij} \leq 0.5$ , $x_{ik} \geq 0.5$ . This rule is the counterpart of the unanimity in social choice theory (Fung and Fu, 1975).

Minimum and maximum: These operations respectively express the right of veto and the right of dictatorship for any individual. They are more anti-democratic, although they do respect the minimal democracy axiom.

With the minimum operation, collective acceptance is hard to reach but collective rejection is attained as soon as there exists an individual rejection. In other respects, the veto (resp.: dictatorship) effect attached to the minimum (resp.: maximum) can be softened by defining the collective rejection (resp.: acceptance) as the rejection (resp.: acceptance) by a certain number of individuals. This number can be given in an approximate way by means of fuzzy quantifiers (Dubois and Koning, 1991).

## 5. A "decision engine" concept

Inference engines are systems that perform logical deductions, i.e. inferences. In our case, we intend to build a system capable of making antagonistic heuristic knowledge cooperate in order to obtain new pieces of information, i.e. decisions. In the following we call such a mechanism a decision engine. This section deals with the various types of knowledge that might be present in that system, and their associated aggregation modes. It also presents the software architecture arrived at, and finally DEBORA's user interface is outlined. It consists in two parts: the acquisition of new decision tables and the specification of a hierarchy of decision modules.

## 5.1. Typology of decision tables

In Section 3 we chose to represent heuristic knowledge by means of decision tables. Two categories exist: (1) those that should be imperatively obeyed, and (2) those providing pieces of advice (Dubois, 1989).

1. The category of imperative decision tables can be divided into two classes: tables that impose their choice on the others, and tables that eliminate certain decisions. The first express necessary admissibility conditions and will be called “imperative tables” in the following. The latter help in selecting a subset of possible decisions among which a choice still needs to be operated; they will be called “focus tables”. They focus on a smaller space search by postponing weakly relevant decisions. Because of the strict nature of the decisions put forward by imperative and focus tables no compensation effect is allowed for aggregating their decisions. Two totally opposite decisions lead to a conflict. Especially, two tables providing conflicting decisions correspond to a problem without solution; it is a failure situation.

2. On the contrary, in case of non-imperative tables, one tries to make all the viewpoints cooperate for choosing decisions. The compensation effect is thus desired. If two antagonistic non-imperative decisions are put forward, it seems coherent to adopt an intermediate decision, when it exists. If both points of view are completely opposed for choosing a certain decision, it must not lead to a conflict but result in indifference. In this case, the intermediate decision corresponds to abstention from deciding on the basis of the conflicting decision tables. Moreover, the voting procedure should be democratic; tables should possess neither a right of veto nor a right of dictatorship.

In summary, one will distinguish three types of decision tables: imperative tables that impose their choices, focus tables that postpone choices, and advice tables that suggest choices. In this last category establishing differences between tables according to the importance of their pieces of advice and their meaning is conceivable. The aggregation model of these three table categories must take into account their difference in nature.

## 5.2. Aggregation modes

The aggregation functions quoted in Section 4.4.2 are preferentially intended for one of the three table categories.

\- Imperative table results expressing necessary admissibility conditions will be aggregated with the maximum operation;

\- Focus table results will be aggregated with the minimum operation, it allows the expression of a conjunction of requirements for selecting potential decisions;

\- Advice table results will be aggregated with democratic-type operators. The choice between associative symmetric sums and arithmetic mean depends upon the role one may want indifference ( $x_{ij} = 0.5$ ) to play. If idempotence of the aggregation operation ( $f(F, \ldots, F) = F$ ) is admitted then associative symmetric sums are prohibited. If the social choice has only to reflect non-indifferent opinions, arithmetic mean is rejected.

Definition of decision tables given in Section 3.1 brings into play a coefficient $w_{j}$ that conveys the importance of table $T_{j}$ . This weight may be interpreted in at least two ways:

1. Each individuals is viewed as a subgroup and the weight reflects the relative size of this subgroup. In the case of homogeneous groups $w_{j}=1/n$ , $\forall j$ . In the general case $\sum_{j=1,n} w_{j}=1$ only. This view of the weights as reflecting subgroup sizes fits nicely with majority rules.

2. The weight may reflect the relevance of an individual in the group. This level of relevance acts as a constraint on the preference intensities that an individual can express. Being antidemocratic in essence, this type of weight is not adapted to majority-type of rules, but may be useful to limit the influence of a dictator or a veto.

The weighted aggregation functions that can be used are the following (see Dubois and Prade, 1988):

Minimum: With normalization condition $\min(w_1, \ldots, w_n) = 0$

$$
\phi \left(\left(x _ {i 1}, w _ {1}\right), \dots , \left(x _ {i n}, w _ {n}\right)\right) = \min _ {j} \max \left(w _ {j}, x _ {i j}\right)
$$

Maximum: With normalization condition $\max(w_1, \ldots, w_n) = 1$

$$
\phi \left(\left(x _ {i 1}, w _ {1}\right), \dots , \left(x _ {i n}, w _ {n}\right)\right) = \max _ {j} \min \left(w _ {j}, x _ {i j}\right)
$$

Arithmetic mean: With normalization condition $\sum_{j=1,n}w_j = 1$

$$
\phi \big ((x _ {i 1}, w _ {1}), \dots , (x _ {i n}, w _ {n}) \big) = \sum_ {j = 1, n} w _ {j} \cdot x _ {i j}
$$

Associative symmetric sum: With normalization condition $\sum_{j=1,n} w_j = n$

$$
\begin{array}{r l} & {\phi (x _ {i 1}, w _ {1}), \ldots , (x _ {i n}, w _ {n}))} \\ & {\quad = [ x _ {i 1} ^ {w _ {1}} \cdot x _ {i 2} ^ {w _ {2}} \ldots x _ {i n} ^ {w _ {n}} ]} \\ & {\qquad \times [ x _ {i 1} ^ {w _ {1}} \cdot x _ {i 2} ^ {w _ {2}} \ldots x _ {i n} ^ {w _ {n}} + (1 - x _ {i 1}) ^ {w _ {1}}} \\ & {\qquad \cdot (1 - x _ {i 2}) ^ {w _ {2}} \ldots (1 - x _ {i n}) ^ {w _ {n}} ] ^ {- 1}.} \end{array}
$$

## 5.3. The DEBORA architecture

The aim of a decision engine is to produce one decision or a sequence thereof so as to start again the constraint propagation. This section describes the organization of a decision engine shell. It is called DEBORA which stands for: Decision Engine Based On Rational Aggregation.

## 5.3.1. Decision modules

As seen in Section 5.1, the various tables do not have the same importance and this corresponds to the various ways of aggregating their results. This statement naturally leads to separate the decision task into modules. A decision module consists of a set (possibly a singleton) of decision tables of the same nature and a choice aggregation procedure. The way it operates is represented in Figure 6. A module receives as input a group of candidate decisions (1) that are drawn from the current data state (2). Once the decision module is activated (3), each decision table it embodies (4) individually votes. The preference intensity vectors they induce are aggregated via the procedure attached to the decision module (5). According to the knowledge present in the module and also according to the collective decision ranking arrived at one or many decisions are held (6).

![](/api/attachments/UV54XWGT/fulltext/images/c870ccda2ee053c23851d5e608bbb263625628bed760dfc65f630703879b9de4.jpg)  
Fig. 6. Functional representation of a decision module.

## 5.3.2. Decision engine architecture

DEBORA's goal is to provide decisions that affect the problem solving state and allows a constraint propagation algorithm to start again (cf. Section 2). In a similar situation an individual would generally first solicit imperative information and try to make a decision from it. When it cannot lead to a decision then less imperative information is brought into play. The imperativeness of the knowledge suggests a hierarchical structure for the decision engine architecture as shown in Figure 7. The basic components of this architecture are the decision modules. When the inference mechanism stops performing deductions and needs some advice, the highest decision module is invoked. If this module is able to produce a single decision then this decision is given to the constraint propagation device otherwise a lower decision module is activated and the decisions not rejected by the previous module are given to it as input. The three types of modules involved in this hierarchy are:

![](/api/attachments/UV54XWGT/fulltext/images/78501c315979b891a6fc05cebc0faf31152809857cb4eb4b28397b095abedceb.jpg)  
Fig. 7. Decision engine architecture.

Dictatorship module: This first module to be activated is endowed with a rather dictatorial aggregation method since the concerned tables are imperative. At the end of this stage the decision set obtained contains either mandatory actions that short-circuit the following modules, or decisions of abstention that let tables of lower levels choose.

Veto module: When no imperative decision can be put forward only pieces of advice can be given. A veto module usually intervenes (but it is not compulsory) to restrain the space of candidate decisions, for instance, by postponing the evaluation of potential decisions weakly relevant at the current step of constraint satisfaction.

Democracy module: The third stage brings into play advice tables. They are combined by means of a democratic method that makes them all intervene and prevents veto and dictatorship. This stage provides, as output, decisions that have the greatest collective support. Several democracy modules may be used one after the other. In case of indecisiveness of one module a second one takes over. In that case a democracy module plays the role of an oligarchy for the lower levels.

This decision module hierarchy is not imposed. The user can define his own organization (cf. Section 5.4). The dictatorship module may not exist but if it exists it seems reasonable to give it the role corresponding to the semantics of decisions it makes. If not made, those decisions lead to violate imperative constraints. Therefore the dictatorship module should be put in first place in order to prevent non-imperative decisions from being made when imperative ones are possible. Veto modules are optional, their purpose is to provide democracy modules with a smaller subset of candidate decisions.

## 5.3.3. Dictatorship module

The dictatorship module contains imperative decision tables. Not applying their choices entails a search failure. When they suggest a decision with maximal level of preference it must absolutely be applied and the constraints it implies must be propagated in order to carry on the inference process. The behavior of an imperative table differs from other tables in that it may force backtracking. Indeed, it may express the case where the current solution is infeasible. The other tables are not allowed to draw such a conclusion since they only convey pieces of advice. An example of such an imperative table could be as follows: consider a machine which admits a limited amount of overlapping between consecutive operations, and that the tolerated overlapping is flexible.

## Imperative table:

General condition: $X$ and $Y$ are two concurrent operations on the same machine,

Rule 1: if $X$ cannot but significantly overlap $Y$ then backtrack till the last piece of advice.

Rule 2: if X significantly overlaps Y when processed before then Y precedes X.

Rule 3: if Y significantly overlaps X when processed before then X precedes Y.

Rule 4: else no precedence constraint between X and Y.

The phrase “X significantly overlaps Y when processed before” means that after processing operation X the execution interval of operation Y proves to be smaller than its duration. ‘Significantly overlapping’ is here considered as a fuzzy notion. Aggregation of preferences given by these tables is performed by the (possibly weighted) maximum operation. In the case of dictatorship module, preferences have certain similarities to necessity degrees (Dubois and Prade, 1988). A decision whose rating is 1 is equivalent to say that a different decision is impossible. A rating strictly between 0 and 1 indicates the decision is more or less forced. Given a set of imperative tables $T_{j}$ a decision $\delta_{i}$ will be evaluated by the degree of imperativeness $I(\delta_{i}) = \max_{j} \min(w_{j}, \mu_{ij}(s))$ where s is the current situation, $w_{j}$ is the priority of table $T_{j}$ and $\mu_{ij}(s)$ is the degree of matching between the current situation s and the prototypical situation in the condition part of rule i of table $T_{j}$ . Rules of imperative tables generalize production rules used in the GARI planning system (Descottes and Latombe, 1985). These rules have priority weights with the same semantics as here but their condition parts are not fuzzy ( $\mu_{ij}(s)$ is 0 or 1). Priority weights are also aggregated by the maximum (see Dubois 1989).

The global rating of a decision may be also interpreted as the degree to which the corresponding constraint is violated if not applied. A global preference in ]0,1[ means a partial violation of the constraint. Consequently, this decision module forces all decisions that are essential. One possible procedure is

1. As soon as a ‘backtrack’ decision gets a non-zero global preference degree, this decision is immediately applied whatever preference degrees is attached to the other decisions. In this case, the preference degree is not interpreted the usual way. When not totally rejected this decision is chosen.

2. If a decision of abstention (i.e. a conclusion of an ‘else’ rule, e.g. “no precedence between operations A and B”) has a global preference degree greater than those of the decisions referring to the same constraint (“A precedes B” and “B precedes A”) then no decision relative to this table is made.

3. When an applicable decision (i.e. not a decision of abstention, for instance “A precedes B”) receives a global preference degree greater than the other decisions relative to the same table (“B precedes A” and “no precedence between operations A and B”) then it is chosen. In other words, this decision is the one that would most violate the corresponding constraint if not applied.

Backtracking may appear in case 1 but also when among the decisions selected by various imperative tables, at least two are contradictory (e.g. “A precedes B”, “B precedes C” and “C precedes A”).

## 5.3.4. Veto modules

A veto module plays the role of a decision filter for the following democracy modules. Those latter modules contain pieces of advice that are hardly ever relevant in all circumstances. The veto modules temporarily postpone decisions in order to make democracy modules focus on interesting candidate decisions. The decision architecture may contain several sequences: veto module + democracy module(s). It enables the search to be divided into distinct steps. In the job-shop scheduling domain for instance, rather than trying to schedule all the operations on all the machines, it is sometimes more appropriate to schedule first the operations relative to a particular set of machines, and then to schedule the rest of them.

Veto modules contain focus tables. The two sorts of decision they make aim at keeping or rejecting candidate decisions. An example of such a table is:

## Focus table:

General condition: X and Y are two unsequenced concurrent operations on the same machine,

Rule 1: if earliest starting time of operation X and earliest starting time of operation Y are small

then sequence operations X and Y.

Rule 2: else do not sequence operations X and Y.

This table focuses on sequencing pairs of operations of small earliest starting time.

The preference intensity degrees $\mu_{ij}(s)$ produced by the focus tables are aggregated via the weighted minimum operation. These degrees can be viewed as degrees of possibility (Dubois and Prade, 1988) since a global weight 0 will block the consideration of the concerned decision. The n first decisions with positive global preference degree are kept. They determine a set of candidate decisions which the next table will evaluate. If this set is empty, then many alternatives can be contemplated whether one considers (1) focus tables were too restrictive, thus not adjusted to the current data state, or (2) the following democracy modules are not concerned by the remaining candidate decisions. In the first case, the veto module is not taken into account and all the candidate decisions are given in input to the following modules. In the latter case, the democracy modules just following the veto module are not triggered and all the candidates decisions are given to the next veto module.

## 5.3.5. Democracy modules

These modules handle tables whose decisions are pieces of advice. The interest of such modules is to intervene when the problem is underconstrained, i.e. when no imperative decision is essential. The type of knowledge then activated consists of heuristics on the way to guide the search. In order to reach the solution in the fewest steps possible only one decision should be made and imperative knowledge should be activated again. In fact, when the problem is underconstrained, making only one decision may lead to the repeated activation of imperative knowledge in vain, several decisions are needed before it becomes sufficiently constrained to enable the constraint propagation algorithm to be productive.

The opposite approach would entail applying too many pieces of advice, i.e. advising decisions that may turn out to be infeasible. The optimal behavior lies in the selection of the optimal number of pieces of advice so as to preserve feasibility while making the constraint propagation algorithm productive. This number of pieces of advice to apply can only be estimated. A good way to compute this estimated number consists in taking into account the current efficiency of the propagation algorithm at solving constraints by considering for instance the amount of constraints yet to be solved (Bel et al., 1989b). Then use the following heuristic: the more productive is the constraint propagation, the more constrained is the problem, the less pieces of advice should be simultaneously given by the democracy modules.

Two aggregation modes have been proposed for finding the global preferences: the arithmetic mean and the associative symmetric sums. The preference degrees are thus aggregated in an additive-like manner and are more akin to probabilities, while they behave respectively like degrees of necessity and possibility in dictatorship and veto modules. Once the collective decision ranking is done, the selected pieces of advice will be the actual decisions with the highest degree of preference – but not a decision of abstention. If there are too many such decisions with similar preference degrees and another decision module follows, then those decisions are passed over to this module in order to be settled. Choosing a decision at random only occurs as a last resort when too many pieces of advice are left unsorted by the last decision module of the hierarchy. This case reflects a lack of knowledge on the way to decide, i.e. calls for more decision tables.

## 5.4. User interface

In Section 2 it has been seen that constraint satisfaction systems were ruled by both logic and heuristic knowledge. The first type helps in performing deductions. It is not supposed to vary once the application domain is defined. For instance, in the job-shop scheduling domain, operating knowledge on the way to handle time intervals remains the same whichever class of job-shop is taken into account. On the other hand, the second type of knowledge conveys heuristics. For a single problem, various heuristics may be contemplated. For instance, in one job-shop class certain heuristics may be interesting and not in another. Thus, it seems desirable, to provide the user with the opportunity to specify the contents of this knowledge and his way of using it, to a certain extent. The first part of this section is devoted to a technique of acquiring this knowledge with the decision table formalism (Koning, 1990). The second part deals with the definition of a decisional architecture in DEBORA.

## 5.4.1. Acquisition of fuzzy decision tables

As seen in Section 3.3 a decision table consists in rules and a rule consists in a condition and conclusion part. The condition parts give a description of a set of situations. They appeal to several notions: attributes, unary predicates, comparators and possibly quantifiers. Some condition parts refer mostly to relations between variables. The SPT advice table given in Section 3.2 for instance, involves the attribute ‘duration’, the variable ‘operation X’, the fuzzy comparator ‘significantly smaller than’, the non-fuzzy predicate ‘two concurrent operations on the same machine’ and the relation ‘precedes’.

A DEBORA user is allowed to introduce his own decision tables. For this, he has access to a library of attributes, predicates, comparators and relations. Moreover he can define compound attributes, fuzzy predicates and fuzzy comparators. Attributes like: the duration of an operation, its earliest starting time (est), its latest finishing time (lft), the resource on which it must be processed, etc., are basic attributes; they are predefined. But sometimes, it is desirable to compare more complex attributes within a condition of a decision table, as for instance, the execution interval of operations. This kind of compound attribute may be defined by a user by means of arithmetic operators. A name for the new attribute needs to be given as well as its formal expression and the variables it concerns. For instance the attribute "length of execution interval" that applies on an operation X may stand for lft(X)-est(X). New fuzzy predicates and fuzzy comparators can easily be acquired. As mentioned in Section 3.5 it only requires the user to provide two or four thresholds since the associated fuzzy sets can be represented by means of a trapezoid. They also may be defined from other predicates or comparators by combining them.

The conclusion parts of a decision table can be predefined for each type of application, and a particular system behavior attached to them. In a scheduling application there are for instance relations like ‘precedes’, ‘immediately precedes’, and the actions ‘backtrack’ and ‘abstention’. The two first relations impose a ranking between two operations. The ‘backtrack’ actions stops the current search and starts it in an other direction. The ‘abstention’ intervenes in the behavior of decision modules.

Defining a new decision table consists in filling a structure whose fields are: the table name, a description in natural language of the table purpose, the weight, the general condition, a list of rules, the 'else' conclusion. A rule is a structure embodying a condition and a conclusion part. A minimal table contains at least one rule.

5.4.2. Acquisition of a decision engine architecture using DEBORA

Acquiring a complete architecture for DEBORA requires to:

\- Define a set of decision tables (cf. Section 5.4.1).

• Gather the tables in several groups.

\- Give to each group a decision strategy (i.e. create the decision modules).

\- Define a hierarchy among these modules.

A decision module is completely specified by its name, a non-empty list of table names and the name of an aggregation function. The user chooses such a function by replying to questions about the characteristics it should possess. The first question concerns whether the nature of the decisions made by the module have certain similarities to imperative decisions or pieces of advice. The answer enables the set of operations to be split into two groups:

1. Minimum and maximum connective that respectively convey veto and dictatorship attitudes.

2. Arithmetic mean and associative symmetric sums that convey more democratic attitudes.

If the first set of operations has been chosen, the next question asks if the operation should impose or dismiss decisions. In the first case the maximum operation is chosen otherwise it is the minimum operation. If the second set of operations is chosen the next question concerns the role played by indifferent opinions, and by similar opinions. When indifferent opinions should not intervene in the global opinion and similar opinions reinforce themselves then the class of associative symmetric sums is adopted. If the answer indicates indifferent opinions affect the global determination then the arithmetic mean is chosen. Once the decision modules are totally specified a decision, architecture can be set up, i.e. the module sequence. Since it may be interesting to test several hierarchies, the user is offered the possibility to define a catalog of architectures. He provides an architecture name and a list of decision module names ranked in the way they will be triggered. Clearly all modes of aggregation used by Pinson (1987) in the CREDEX system are present in DEBORA. The lexicographic mode corresponds to putting one decision table in each module of a chain of modules. However, aggregation based on associative symmetric sums is not present in CREDEX.

## 6. A testbed for DEBORA

The interest of such an architecture like DEBORA is that it can be added to a constraint propagation system (cf. Section 5.3). Certain domains particularly suit this cooperation. It is notably the case of the job-scheduling area where a classical expert system approach is not adapted (Badie et al., 1990). DEBORA has been connected to the OPAL scheduling system (Bel et al., 1989a). The first part of this section presents OPAL and shows how it has become more flexible because of the various decision strategies allowed. Then an example is described in detail.

## 6.1. Application to a job-shop scheduler

## 6.1.1. The OPAL system

OPAL is a software system dedicated to industrial job-shop scheduling problems (Bensana et al., 1988; Bel et al., 1989b). It aims at scheduling operations for each machine in a job-shop so that the due dates associated with the jobs are respected. OPAL's solving process relies on the notion of 3-tuples (operation 1, operation 2, resource) which means 'operation 1' and 'operation 2' must be processed on the same 'resource'. When their execution intervals can overlap they will be called "conflicting 3-tuples". In a first step, OPAL builds the stack of all possible 3-tuples from a data file that describes parts to be processed in the job-shop, i.e. operations durations, machines, earliest starting times, etc. It also generates a graph representing the problem solution where vertices denote operations to be processed and edges precedence relations. Some information is associated with each vertex, for instance the earliest starting time of the operation and its latest finishing time that are updated each time an edge departs from or arrives at this vertex.

The solving method alternatively triggers two mechanisms, both dedicated to the completion of the graph. The first one aims at scheduling operations based on necessary admissibility conditions the solution must satisfy, i.e. meeting the due dates. It consists in a succession of sequencing steps, i.e. adding a necessary edge (a precedence relation between operations) and updating steps modifying the information attached to vertices this edge concerns directly or indirectly, such as possibly determining a new earliest starting time or latest finishing time.

When this inference process is not any longer able to reduce the stack of 3-tuples, the decision process brings into play various heuristics. The sequencing preferences suggested by these heuristics are aggregated by a unique procedure (a weighted arithmetic mean). One or more decisions are made according to whether the number of 3-tuples still in the stack is small or large. The inference process is then triggered again. The decision process builds a search tree. Each time it finds a precedence between two operations of a 3-tuple a new vertex of the search tree is created. This vertex corresponds to a tentative search step – a decision made by the inference process does not lead to a new vertex in this tree since it is considered as a necessary decision. To each vertex of the search tree is associated the current scheduling graph before the decision was applied so that the search tree be immediately restored in case of backtracking.

One notices a 3-tuple corresponds to two potential sequencing decisions: “operation 1 precedes operation 2” or “operation 2 precedes operation 1”. The first backtrack to a vertex in the search tree consists in applying the antonym decision. A second backtrack to this vertex eliminates it from the search tree, the previous decision is then called into question.

## 6.1.2. Implementing DEBORA

Constraint analysis in OPAL has a twofold purpose. On the one hand it makes imperative sequencing decisions and on the other hand it propagates the constraints. The implementation of DEBORA has consisted in:

1. translating the sequencing part of OPAL as an imperative decision table so that it could be handled within a dictatorship module. Such a table is similar to the one in Section 5.3.3;

2. replacing the heuristic part of OPAL by veto and democracy modules.

The general structure of OPAL has been kept, especially the search tree, the scheduling graph and the 3-tuples stack. The constraint propagation part has also been entirely kept. The data structures have been very little modified. The basic structure on which DEBORA relies is a stack of decision modules that corresponds to the module hierarchy as defined by the user (cf. Section 5.4). If the uppermost module is a dictatorship module then it is activated and stays active as long as it provides decisions, namely reduces the 3-tuples stack. Each decision is immediately propagated.

When a dictatorship module is no longer deci-

![](/api/attachments/UV54XWGT/fulltext/images/7ea7f6758314dc41e04236dcc6ff40b0271eae8154400f7b8bf16ccc80890dcb.jpg)  
Fig. 8. Initial Gantt chart.

sive the other modules of the hierarchy are activated. At most one decision is made. It gives rise to creating a vertex in the search tree. Backtracking in the search tree is identical to OPAL's. Coupled with DEBORA, OPAL becomes a much more flexible scheduling system. Indeed it becomes possible to declare some new types of constraints, different from the sole requirement of meeting due dates. For instance, one may take into account limitations in the in-process storage capacity in the job-shop when deriving a feasible schedule; with OPAL, this cannot be taken into account as a hard constraint since the heuristic knowledge in the decision module of OPAL was not considered as containing imperative rules.

![](/api/attachments/UV54XWGT/fulltext/images/d56731b6052288802e8b43bee17ba071932266225907bc45910784f2d0c8c947.jpg)

## 6.2. Example

The example outlined here is drawn from the field of job-shop scheduling (cf. Section 2.3). It is meant to illustrate how a decision engine obtained through DEBORA works. Let A, B and C be three operations that have to be sequentially processed on the same machine M. The initial Gantt chart is given in Figure 8 where rectangles show operation duration and horizontal lines execution intervals.

Fig. 9. Decision module hierarchy.  
![](/api/attachments/UV54XWGT/fulltext/images/3916f63f3464ed39d06cbd285a36e9fa948dfca0b9fc11db8c59cee66f7e3935.jpg)  
Fig. 10. Fuzzy comparators appearing in decision tables SPT and EFT.

## 6.2.1. The decision engine architecture

The decision hierarchy used to solve this example consists of three modules (see Figure 9). The first module is a dictatorship module containing a single table, the one given in Section 5.3.3. This choice is realistic. Indeed, in job-shop scheduling, meeting the due dates is the number one priority. As long as temporal constraints infer some sequencing actions, these actions are performed. Once the temporal constraints stop deducing new sequencing other types of constraints are usually invoked. This description of temporal constraints totally fits the semantics of the dictatorship table mentioned earlier. The second module is a veto module. It contains a table that focuses on sequencing pairs of operation of small earliest starting time. Let us assume the predicate small is Boolean. This table discards operations that cannot begin before time 3. The third module is a democracy module containing two decision tables and its associated aggregation strategy is the associative symmetric sum given in Section 4.4.2. The two tables are the ones given in Section 3.2. The first one (called SPT) favors the early processing of short operations, the other one (called EFT) favors the processing of the operations that must end first. These two tables involve the comparators 'significantly smaller than' and 'significantly greater than' which can be defined in a fuzzy way, like in Figure 10. According to this definition, $x$ begins to be significantly smaller (resp.: greater) than $y$ when $x < y$ (resp.: $x > y$ ) is true, and $x$ fully becomes significantly smaller (resp.: greater) than $y$ when $x < y - 3$ (resp.: $x > y + 3$ ) is true. The last module is only called in case that the previous one reaches indecisiveness. It contains one decision table which favors the sequencing of two operations in a way that preserves the largest slack time.

## 6.2.2. Solving step 1

The first call to the dictatorship module doesn't lead to any decision, the veto module is thus triggered. The focus table discards the 3-tuples $\langle A, C, M \rangle$ and $\langle B, C, M \rangle$ since only operations $A$ and $B$ begin during the three first time units. Because of the Boolean nature of the predicate 'small' the 3-tuple $\langle A, B, M \rangle$ gets a rating of 1 and the others 0.

The 3-tuple $\langle A, B, M \rangle$ is passed to the democracy module. Table SPT gives the rating $\frac{1}{3}$ to the decision “A precedes B” because duration of A is smaller than duration of B by one time unit (see Figure 10), and 0 to the decision “B precedes A”. Table EFT gives the rating $\frac{1}{3}$ to decision “A precedes B” because finishing time of A (11) is smaller than the finishing time of B (12) by one time unit, and 0 to the decision “B precedes A”. After aggregation, the global ratings are:

$$
0 = \frac {0 \times 0}{0 \times 0 + (1 - 0) \times (1 - 0)} \text { for } B \text { precedes } A
$$

$0.20 = \frac{\frac{1}{3} \times \frac{1}{3}}{\frac{1}{3} \times \frac{1}{3} + (1 - \frac{1}{3})(1 - \frac{1}{3})}$ for $A$ precedes $B$ .

Thus decision “A precedes B” is applied and the constraint propagation algorithm is run. The updated Gantt chart is shown in Figure 11.

## 6.2.3. Solving step 2

The dictatorship module cannot yet help make a decision, and the veto module is called. Unfortunately none of the 3-tuples satisfy the precondition of the focus table, and the result of this table is thus not taken into account. Both 3-tuples $\langle A, C, M \rangle$ and $\langle B, C, M \rangle$ are passed to the democracy module.

Table SPT assigns rating $\frac{2}{3}$ to decision “C precedes B" because the difference between durations of operation B and operation C is equal to two time units, and rating 0 to decision "B precedes C". It assigns rating $\frac{1}{3}$ to decision "C precedes A" because the difference between the duration of the two operations is one time unit, and rating 0 to decision "A precedes C". Table EFT assigns rating 1 to decision "C precedes B" and 0 to decision "B precedes C" since finishing time of C (9) is smaller than finishing of B (12) by three time units. It assigns $\frac{1}{3}$ to "A precedes C" and 0 to "C precedes A" since finishing time of A (8) is smaller than finishing time of C (9) by one time unit. The results are summarized in Table 1.

![](/api/attachments/UV54XWGT/fulltext/images/a73c9c529d1f111b16e153a2388df020ff7da3571ca4f99aee18964a23d9d37f.jpg)  
Fig. 11. Gantt chart after one call to the decision engine.

![](/api/attachments/UV54XWGT/fulltext/images/a9711588229839c7c0a5cbd5513ce4735896b3a85a7d90ba65d1ccfe499156a0.jpg)  
Fig. 12. Gantt chart after a second call to the decision engine.

After aggregating the individual ratings, decision “C precedes B” gets the highest rating. Therefore this decision is made and the constraint propagation algorithm started again. The new Gantt chart is shown in Figure 12.

Votes from the decision tables of the first democracy module

<table><tr><td></td><td>SPT</td><td>EFT</td><td>aggregation</td></tr><tr><td>“A precedes C”</td><td>0</td><td> $\frac{1}{3}$ </td><td>0</td></tr><tr><td>“C precedes A”</td><td> $\frac{1}{3}$ </td><td>0</td><td>0</td></tr><tr><td>“B precedes C”</td><td>0</td><td>0</td><td>0</td></tr><tr><td>“C precedes B”</td><td> $\frac{1}{3}$ </td><td>1</td><td>1</td></tr></table>

## 6.2.4. Solving step 3

The only 3-tuple left now is $\langle A, C, M \rangle$ . Since both $A$ and $C$ have the same finishing time now, decision table EFT gives rating 0 to decisions “ $A$ precedes $C$ ” and “ $C$ precedes $A$ ”. Therefore, due to the aggregation strategy of the democracy module (associative symmetric sum) the global rating for both of these decisions is 0. Hence, the second democracy module is called and decision “ $A$ precedes $C$ ” is chosen because it preserves the greatest slack time – there would have been no slack time at all with operation $C$ preceding $A$ . The final Gantt chart is shown in Figure 13.

## 7. Conclusion

This paper has proposed a formal framework for representing and handling decision rules which are basically ill-formalized, multiple and possibly antagonistic. It has shown that results from social choice theory may be relevant in this framework. A decision engine concept has been elaborated. The starting point of this work lies in a strong analogy between the problem of selecting a best decision in the presence of several viewpoints and preference (or vote) aggregation in social choice theory. Indeed, a way of deciding may consist in making the heuristics vote on all the candidate decisions in the view of ranking them. This approach has been studied, generalized and justified on the basis of social choice theory. It has produced two kinds of results:

![](/api/attachments/UV54XWGT/fulltext/images/7255a0553e93441819e7644329e831bfb094b38f8ae95a0ebd473fd17c0433fa.jpg)  
Fig. 13. Gantt chart after a third call to the decision engine.

\- At the theoretical level: determination of the contribution of social choice theory for handling local decision rules (heuristics). Implications of this theory for managing decision systems has been demonstrated. It has been shown that certain impossibilities are alleviated when preference intensities are taken into account. Furthermore, various ways of aggregating preference intensities have been provided based on fuzzy set theory;

\- At the software level: design and implementation of an architecture for local decision systems, and also of a user interface for acquiring decision tables and strategies that exploit these tables. The software has been encoded in Common Lisp and tested in conjunction with a job-shop scheduling system.

The decision engine DEBORA presented here is a general machinery for local decision making that can be used in conjunction with a constraint propagation system. DEBORA's structure being strongly modular, it is very easy to test various aggregation strategies with various pieces of heuristic knowledge. The most interesting hierarchies of decision tables for certain problems may thus be determined. In other respects, necessary admissibility conditions of the solution have not been permanently encoded within the constraint propagation part but under the form of imperative decision tables. This allows a greater software flexibility. Imperative knowledge may be turned into advice (and vice versa).

DEBORA may also be viewed as a self-standing system which can be periodically queried. This approach can be applied, for instance, to real time production control problems where a system like DEBORA could be useful to react to event occurrence and to put forward a proposed action.

DEBORA is a shell that could also possibly be used to take into account meta-knowledge in expert systems. Meta-knowledge is knowledge about knowledge. It is fundamental for systems that not only use their knowledge base just as it is, but are also able to reason about it, structure it, generalize it and decide in which case it may be useful. As a general rule, meta-knowledge may be expressed as viewpoints on the way to handle knowledge. It is often complex and possibly antagonistic. Moreover, most of the time it is formalized as rules, called meta-rules. Usually these meta-rules are invoked in an exclusive manner: only one is activated. It is conceivable to use a DEBORA-like system and make them cooperate.

One way to extend DEBORA's architecture consists in adding meta-knowledge in it. As the solution state evolves it may be possible that certain modules (not the dictatorship module) become no longer relevant; their activation may then penalize the search time. An example of meta-knowledge could be: "if the number of candidate decisions is fairly small then veto modules are not any longer called upon". This kind of meta-knowledge dynamically modifies the decision module hierarchy. One may contemplate handling it also via decision modules.

## Acknowledgements

This work is the result of a cooperation between Institut de Recherche en Informatique de Toulouse (France) and Centre d'Etude et de Recherche de Toulouse (France) in the framework of the PROMIP Regional Consortium. The writing was done while the second author was visiting at the Robotics Institute, Carnegie Mellon University, Pittsburg, PA. A preliminary draft has been presented at the 2nd Annual Conference on AI, Simulation and Planning in High Autonomy Systems, Cocoa Beach (Florida), April 1991. The research has been partially supported by the PROMIP Consortium, Toulouse, and the second author by a scholarship from INRIA, France. We wish to thank Gérard Bel and Eric Bensana who have contributed many ideas and substantial time to the creation of DEBORA, and its connection to the OPAL scheduling system.

## References

Adiga S., Cochran J. (1985) A decision analysis approach to modeling conflicting and inexact reasoning in rule-based systems. Proc. of the IEEE Conf. on Systems, Man and Cybernetics, Tucson, Arizona, 983–987.

Arrow K.J. (1963) Social Choice and Individual Values. (2nd edition) Wiley, New York.

Bachant J., McDermott J. (1984) R1 revisited: four years in the trenches. AI Magazine, 5(3), 21–32.

Badie C., Bel G., Bensana E., Verfaillie G. (1990) Operations research and artificial intelligence cooperation to solve scheduling problems: the OPAL and OSCAR systems. Proc. of the 1st Inter. Conf. on Expert Planning Systems, Brighton, UK, 1–5.

Bel G., Bensana E., Dubois D., Koning J.L. (1989a) Handling fuzzy priority rules in a job-shop scheduling system. Proc. of the 1st Inter. Fuzzy Systems Association (IFSA) Congress (J.C. Bezdek, ed.), 200–203.

Bel G., Bensana E., Dubois D., Ershler J., Esquirol P. (1989b) A knowledge-based approach to industrial job-shop scheduling. In: Knowledge-Based Systems in Manufacturing (A. Kusiak, ed.), Taylor & Francis, 207–246.

Bensana, E., Bel G., Dubois D. (1988) OPAL: a multi-knowledge-based system for industrial job-shop scheduling. Int. J. of Production Research, 26(5), 795–819.

Cayrol M., Farreny H., Prade H. (1982) Fuzzy pattern matching. Kybernetes, 11, 103–116.

Davis E. (1987) Constraint propagation with interval labels. Artificial Intelligence, 32(3), 281–331.

Dechter R., Pearl J. (1988) Network-based heuristics for constraint satisfaction problems. Artificial Intelligence, 34(1), 1–38.

Descottes Y. Latombe J.C. (1985) Making compromises among antagonistic constraints in a planner. Artificial Intelligence, 27, 183–217.

Doyle J. (1990) Rationality and its roles in reasoning. Proc. of the 8th National Conf. on Artificial Intelligence (AAAI'90), 1093–1100.

Doyle J., Welman M.P. (1991) Impediments to universal preference-based default theories. In: Knowledge Representation, Special Issue of Artificial Intelligence.

Dubois D. (1989) Fuzzy knowledge in an artificial intelligence system for job-shop scheduling. In: Applications of Fuzzy Set Methodologies in Industrial Engineering (G. Evans et al., eds.), Elsevier, 73–79.

Dubois D., Koning J.L. (1989) Règles de décision antagonistes dans les systèmes à base de connaissances. Actes du 7ème Congrès AFCET Reconnaissance des Formes et Intelligence Artificielle (RFIA), 1647–1659.

Dubois D., Koning J.L. (1991) Social Choice axioms for fuzzy set aggregation. Fuzzy Sets and Systems, 44(1), 1–18.

Dubois D., Prade H. (1980) Fuzzy Sets and Systems, Theory and Applications. Academic Press, New-York.

Dubois D., Prade H. (1988) Possibility Theory: an Approach

to Computerized Processing of Uncertainty. Plenum Press, New York.

Dubois D., Prade H., Testemale C. (1988) Weighted fuzzy pattern matching. Fuzzy Sets and Systems, 28, 313–331.

Francioni J.M., Kandel A. (1988) A software engineering tool for expert system design. IEEE Expert, Tools and Techniques, 3(1), 33–41.

Freuder E.C. (1982) A sufficient condition for backtrack-free search. J. of the ACM, 29(1), 24–32.

Fung L.W., Fu K.S. (1975) An axiomatic approach to rational decision making in a fuzzy environment. In: Fuzzy Sets and their Applications to Cognitive and Decision Processes (L.A. Zadeh et al., eds.), Academic Press, New York, 227–256.

Hintz G.W., Zimmermann H.J. (1989) A method to control flexible manufacturing systems. Europ. J. of Operational Research, 41(3), 321–334.

Keeney R. (1988) Value-driven expert systems for decision support. Decision Support Systems, 4, 405–412.

Klein D.A., Shortliffe E.H. (1990) Integrating artificial intelligence and decision theory in heuristic process control system. Proc. of the 10th Inter. Workshop on Expert Systems and their Applications, Special Volume on Second Generation Expert Systems, Avignon, EC2, Nanterre, 165–177.

Koning J.L. (1990) A user interface for acquiring fuzzy decision tables. Proc. of the Inter. Conf. on Human Machine Interaction and Artificial Intelligence in Aeronautics and Space, Toulouse, France, Teknea, 225–239.

Langlotz C.P., Shortliffe E.H. (1989) Logical and decision-theoretic methods for planning under uncertainty. AI Magazine, 10(21), 39–47.

Le Pape C. (1988) Des systèmes d'ordonnancement flexibles et opportunistes. PhD Thesis, Université Paris XI, Orsay, France.

Le Pape C., Smith S.F. (1987) Management of temporal constraints for factory scheduling. Proc. of the Working Conf. on Temporal Aspects in Information Systems, Paris, France, AFCET and IFIP Technical Committee TC8, North-Holland.

Mackworth A.K. (1977) Consistency in networks of relations. Artificial Intelligence, 8(1), 99–118.

Moulin H. (1988) Axioms of Cooperative Decision-Making. Cambridge University Press, Cambridge, UK.

Pinson S. (1987) A multi-attribute approach to knowledge representation for loan granting. Proc. of the 9th Inter. Joint Conf. on Artificial Intelligence (IJCAI'87), 588–591.

Sadeh N. (1991) Look-ahead techniques for micro-opportunistic job-shop scheduling. PhD Thesis, Carnegie Mellon University, School of Computer Science, Pittsburgh, PA.

Silvert W. (1979) Symmetric summation: a class of operations on fuzzy sets. IEEE Trans. on Systems, Man and Cybernetics, 9, 657–669.

Yager R.R. (1989) On the logical representation of social choice (multi-agent aggregation). Tech. Rep. #No. MII-811, Machine Intelligence Institute, Iona College, New Rochelle, NY.

Zadeh L.A. (1965) Fuzzy sets. Information and Control, 8, 338–353.
