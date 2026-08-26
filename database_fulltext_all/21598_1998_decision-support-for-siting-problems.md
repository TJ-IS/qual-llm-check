---
otero_id: 21598
otero_key: "Y7UHF3X7"
title: "Decision support for siting problems"
authors: "V. Maniezzo; I. Mendes; M. Paruccini"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00042-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for siting problems

V. Maniezzo <sup>a,)</sup>, I. Mendes <sup>b</sup>, M. Paruccini <sup>b</sup>

<sup>a</sup> Scienze dell’Informazione, UniÕersity of Bologna, Õia Sacchi 3, 47023 Bologna, Cesena Italy

<sup>b</sup> European Commission, Joint Research Center, Institute for Systems Engineering and Informatics, TP 650, I-21020 Ispra, VA , Italy ( ) Accepted 1 July 1998

## Abstract

Despite the development of mathematics of location theory and its obvious economic impact, few applications have been developed and are actually in use to support decision makers in siting decisions. The obstacles that hinder a more widespread exploitation of mathematical results are twofold: the intrinsic difficulties of the relevant problems and the tradeoff to be balanced between the different objectives. The article presents the results obtained in the implementation of a Decision Support system applied to the problem of locating installations for industrial waste management. This DSS is based on multicriteria decision analysis for the best siting of plants, minimizing costs and environmental impacts. The proposed approach identifies a hierarchy of objectives, where at the top level we solve a 0<sup>r</sup>1 fixed cost transportation problem Ž . FCTP . This is an NP-hard combinatorial optimization problem that can only be solved heuristically for real world problem sizes. A number of good solutions of the single objective problem are combined to produce efficient alternatives, to be further evaluated by means of multicriteria methods. Computational results both of the FCTP and of the whole systems are provided. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Spatial decision support systems; Multi-criteria decision analysis; Combinatorial optimization

## 1. Introduction

The purpose of a siting problem is to identify particular locations for a given type of facilities or services. Within any region of interest, there are often several potential locations for a certain type of facility. The desirability of one location relative to another depends on a multitude of factors like economic and socioeconomic concerns, health and safety concerns, environment and public attitudes.

Considering the siting of industrial waste treatment and disposal facilities, which has become one of the most pressing problems in local government, various difficulties arise in setting up industrial waste disposal systems. A reduction of some objective obstacles will depend on the capacity of decision makers for justifying adequately the choice of areas that, because of their characteristics, are the most suitable for plants with considerable environmental and social impact.

In this context, the development of a decision support system DSS for the siting of industrialŽ . waste treatment and disposal facilities, seems appropriate. The work presented here documents certain aspects of the setting up of such system.

The problem faced raises both theoretical and architectural concerns. From a theoretical viewpoint it is in fact well-known that the location and transportation problems that we have to face can be modeled only by means of complex integer or mixed-integer programming techniques: this bars the possibility of a thorough analysis of large-sized problem instances such as the one under consideration <sup>w</sup> <sup>x</sup>20 , let alone in a multicriteria framework.

From the architectural standpoint, the need to integrate spatial data with advanced algorithmic techniques has given rise to a research niche in the context of DSSs, considering so-called Spatial Decision Support Systems SDSS; Refs. 6,7 , concernedŽ <sup>w</sup> <sup>x</sup>. with how to integrate spatially referenced information in a decision making environment in order to positively affect the performance of an individual decisionmaker. In particular, in recent years it has been shown how, by these means, spatially integrated DSS can be used to bridge the gap between policy makers and complex computerized models <sup>w</sup> <sup>x</sup> 1,8 . It is in this framework that we analyzed and designed a system to support public policymakers in the study of alternative facility location plans.

The main goal of the developed system is to reduce, as much as possible, the overall impacts— economic, environmental and human—associated with the installation of the necessary waste disposal and treatment facilities in the region of concern Ž . Lombardia, in northern Italy .

One of the main issues of the system as provi-Ž sionally outlined in Ref. 18 is the definition of<sup>w</sup> <sup>x</sup>. feasible alternatives scenarios , which represent al- Ž . ternatives for the treatment and disposal of industrial waste. The definition of an alternative scenarioŽ . requires the identification of a combination of locations for disposal and treatment facilities, and the identification of the users of each of the facilities, which in our case are the municipalities of the region. Each alternative should respect two important constraints:

<sup>Ø</sup> the whole combination must be able to treat and dispose of the total regional waste production;

<sup>Ø</sup> all locations should respect an existing regional list of feasible locations for waste disposal and treatment facilities.

The formulation of the problem as a multicriteria decision problem comes in a natural way, using the scenarios as alternatives and indices quantifying the different impacts of each scenario as problem criteria.

The implemented system Fig. 1 is architec- Ž . turally composed of a data base management system, a models management system and a user interface system 24 . The data base management system is <sup>w</sup> <sup>x</sup> responsible for the retrieval, update and adaptation of all types of information required, the model management system is the component that provides sophisticated multicriteria analysis and interpretation capabilities, and, finally, the user interface is the portion of the decision support system designed to satisfy interface requirements and data representation and control.

For the region selected for the case study, even though there are shortfalls in the disposal of industrial waste, plants already exist and anyway there are regional plans defining possible locations for future plants. The decision module was thus designed to help the decision maker in evaluating a restricted number of planned alternatives, all well specified within it. These alternatives were constructed on the basis of the list of proposed locations for future plants.

However, the set of possible alternatives for the discrete cases only represents the search space of the problem. The question becomes how to select a reduced set of viable alternatives to present to the decision maker to be compared against each other. This requires the balancing of the time and effort required to carefully carry out the task, avoiding the possibility that more cursory procedures may inadvertently eliminate some or all of the good alternatives.

In our view, the reduced viable set of alternatives could be determined by an analysis of the problem, which could lead to the establishment of a hierarchy of objectives. We implemented this approach in the Decision Support System described in this paper.

At the top level, the k best solutions of the problem of optimizing a chosen criterion is computed by heuristically solving a combinatorial optimization location problem. Our choice is based on the assumption that efficient alternatives for the siting problem under study can only be found among those in which the total distance to be traveled to dispose of the industrial waste is relatively small. The problem of finding the best compromise alternatives in the sense of the criteria used in the system is therefore split in two steps.

The first step determines several alternatives with short routes the single criteria used is distance mini-Ž mization connecting the source and destination nodes. in a given transport network, schematized by a graph.

![](/api/attachments/Y7UHF3X7/fulltext/images/3db44ab950fa0e5d2e12707674bb2f8bdb7b2404ad71d3e739f4e0babcf97912.jpg)  
Fig. 1. Components of the developed DSS.

In the second step, a multicriteria approach basedŽ on costs, risks and environmental impacts is applied. to the selected alternatives for the final ranking.

The remainder of the paper is structured as follows: Section 2 presents the main algorithmic issues faced. Specifically, it presents the top-level singlecriterion problem, the identification of efficient solutions and the formulation of the multicriteria problem to be solved by advanced off-the-shelf techniques. Section 3 introduces the real-world case study we faced and presents the computational results we obtained. Section 4 contains a discussion of the conclusions we have drawn from our experience.

## 2. Mathematical formulation of the problem

The problem is thus to define a set of alternative plans for the disposal of industrial wastes of a given region. In particular, we want to define a set S of alternatives $( | S | \cong 1 0 )$ to propose to a decision maker, among which to choose one final solution.

Input data denotes: the number of disposal technologies $( t = 1 , \ldots , \ T )$ ; the number of available waste disposal plants for each technology $( j _ { t } =$ $1 , \ldots , J ^ { t } )$ and the relative capacities $( b _ { i } ^ { t } ) _ { i }$ ; the number of waste generators municipalities, Ž $i \overset { \^ } { = } 1 , \ldots , I )$ and the relative amount of generated waste, provided per disposal technology $( a _ { i } ^ { t } )$ . Moreover, we have the distances between each municipality i and each disposal plant $j _ { t } , \quad d _ { i j _ { t } } , , \quad ( i j _ { t } ) \in H ^ { t } = [ 1 , . ~ . ~ . ~ , I ] \times$ $[ 1 , \ldots , J ^ { t } ]$

The definition of the set S comes from three subsequent refinement steps.

Step 1 Ž . Set A : restrict the set of all feasible solutions to a set $A ~ \left( \left| A \right| \cong 1 0 0 \right)$ , by ranking the solutions according to a single-objective function. The problem to solve in this case has been reduced to a chaining of a k-best 0–1 Knapsack Problem with a Pure Fixed Charge Transportation Problem.

Step 2 Ž . Set P : evaluate the solutions in A according to several preference criteria and possibly determine the Pareto-set, P, of A;

Step 3 Ž . Set S : filter the solutions in P according to four general objectives Environmental Impact, Ž Risk of Major Accidents, Transportation Risk and Cost , thus obtaining the set. S.

2.1. Step 1: construction of the reduced set A of feasible solutions, ranking the solutions according to a single objectiÕe function

## 2.1.1. Single objectiÕe high-leÕel formulation

The single objective function initially considered at this stage comprises both the total length of the routes needed to transport waste to the disposal plants and the cost associated to opening new disposal plants. It is in fact supposed that the existing plants are not sufficient for disposing of all the forecast waste amount. The different technologies give rise to different problem instances, which share data relative to municipality locations but differ with respect to number, location and opening costs of the disposal plants.

Interaction with decisionmakers lead us to discard the straightforward possibility of modeling the problem to be solved as a direct variant of a capacitated p-median problem, which would probably be the most obvious mathematical formulation of a siting problem 3,20 . In particular, the most meaningful <sup>w</sup> <sup>x</sup> deviation from standard location problems was the fact that transportation costs were computed only on the length of the routes used from municipalities to disposal plants, independently of the amount of waste that was to be sent along the routes.

The objective function therefore consists of two terms, the first of which refers to the arcs already used and the second to opening costs. It has the same structure for each of the disposal technologies which must be considered.

Specifically, the problems to solve, for each technology $t = 1 , \ldots , T ,$ , can be formulated as follows.

Let $\xi _ { i j , } ~ ( i = 1 , \ldots , ~ I , ~ j _ { t } = 1 , \ldots , ~ J ^ { t } )$ be a set of 0–1 binary variables whose value is 1 if municipality i has to send its waste of type Ž .t to plant $j _ { t } ,$ 0 otherwise; let $x _ { i j _ { t } }$ be a set of non-negative variables quantifying the amount of waste of typeŽ .t that municipality i sends to plant $j _ { t }$ and let $y _ { j _ { t } } \left( j _ { t } = 1 , \ldots , \right.$ $J ^ { t } )$ be a set of 0–1 binary variables specifying whether plant $j _ { t }$ is open or not. Opening costs are expressed by the quantities $F _ { j _ { t } }$ . The problem is:

$$
\text { Problem } S ^ {t} z _ {s} = \min \sum_ {i j _ {t} \in H ^ {t}} \xi_ {i j _ {t}} d _ {i j _ {t}} + \sum_ {j _ {t} \in J ^ {t}} F _ {j _ {t}} y _ {j _ {t}}\tag{1}
$$

$$
\text { s.t. } \sum_ {j _ {t} \in J ^ {t}} x _ {i j _ {t}} = a _ {i} ^ {t}, \quad i = 1, \dots , I\tag{2}
$$

$$
\sum_ {i \in I} x _ {i j _ {j}} \leq y _ {j _ {t}} b _ {j} ^ {t}, \quad j _ {t} = 1, \dots , J ^ {t}\tag{3}
$$

$$
M \xi_ {i j _ {t}} \geq x _ {i j _ {t}}, \quad i = 1, \dots , I; j _ {t} = 1, \dots , J ^ {t}\tag{4}
$$

$$
\xi_ {i j _ {t}} \in \{0, 1 \}, \quad i = 1, \dots , I; j _ {t} = 1, \dots , J ^ {t}\tag{5}
$$

$$
y _ {j _ {t}} \in \{0, 1 \}, \quad j _ {t} = 1, \dots , J ^ {t}\tag{6}
$$

$$
x _ {i j _ {t}} \geq 0, \quad i = 1, \dots , I; j _ {t} = 1, \dots , J ^ {t}\tag{7}
$$

For each technology, constraints 2 impose that allŽ . the waste generated by each municipality must be disposed of, constraints 3 that the plants that willŽ . eventually be open can accept at most an amount of waste equal to their capacity $b _ { j } ^ { t } ,$ constraints 4 thatŽ . if some waste is routed through an arc, no matter its amount the arc will get a fixed cost in the objective function 1 ; Ž . M is a large positive constant. Finally, constraints 5 through 7 specify that an arc can be Ž . Ž . used or not, that a plant can be open or closed and that waste can be sent only in positive quantities.

Problem $S ^ { t }$ differs from some clustering problems described in the literature, such as the capacitated p-median problem or capacitated sum-of-stars clustering 3,14 in that the waste originated by a munici-<sup>w</sup> <sup>x</sup> pality may be split among several disposal plants, while the usual assumption is that all the waste originated in a location and pertaining to the same technology must be routed to the same disposal point. In our case, this results in a mixed-integer problem, and not in a 0–1 integer problem.

Problem $S ^ { t }$ is NP-hard, being a generalization of the pure fixed-charge transportation problem which will be described in Section 2.1.2, and very difficult to solve to optimality, especially for the problem dimensions that we have to face. Therefore we decided to use an heuristic approach for its solution.

Heuristic solutions for a given problem can be generated following two main approaches: the use of problem-specific or of general-purpose heuristics.

During the last years, the OR community has in fact witnessed a flourishing of new general-purpose heuristic algorithms, such as tabu search 10,11 ,<sup>w</sup> <sup>x</sup> genetic algorithms 12 or the ant system 5 . These<sup>w</sup> <sup>x</sup> <sup>w x</sup> algorithms have proved effective for several combinatorial optimization problems, thus receiving increasing attention from the research community.

Notwithstanding this, we decided to go for a problem-specific heuristic design. This because a simple and computationally inexpensive problemspecific heuristic approach to problem $S ^ { t }$ is manifest.

The additive structure of the objective function Ž . 1 suggests reducing problem $S ^ { t }$ to two interrelated sub-problems, one essentially defined over the $y _ { j _ { t } }$ variables, the second over the $x _ { i j _ { t } }$ and $\xi _ { i j _ { t } }$ variables.

If, in fact, we separately optimize the two components of function 1 , we find that the second compo-Ž . nent is constrained only by inequalities 3 and con- Ž . straints 6 . The dependency on the rest of the prob- Ž . lem is given by variables $x _ { i j _ { t } }$ in inequalities 6 . A Ž . surrogate relaxation of these inequalities leads to the following problem KS<sup>t</sup>:

$$
\text { Problem   KS } ^ {t} z _ {\mathrm{KS}} = \min \sum_ {j _ {t} \in J ^ {t}} F _ {j _ {t}} y _ {j _ {t}},\tag{8}
$$

$$
\text { s.t. } \sum_ {j _ {t} \in J ^ {t}} y _ {j _ {t}} b _ {j} ^ {t} \geq \sum_ {i j _ {t} \in H ^ {t}} x _ {i j _ {t}},\tag{9}
$$

$$
y _ {j _ {t}} \in \{0, 1 \}, \quad j _ {t} = 1, \dots , J ^ {t}
$$

Ž Ž .. from Eq. 6 .As the right hand side of inequality Ž . 9 is a known constant, we are left with a 0–1 knapsack problem to solve. This is a very well-known optimization problem 16 which, despite its NP-<sup>w</sup> <sup>x</sup> hardness, can be efficiently solved even for large size instances.

Once fixed the $y _ { j _ { t } }$ variables to the optimal values $\boldsymbol { \bar { y } } _ { j _ { t } } .$ , with $\begin{array} { r } { \overline { { B } } = \sum _ { j _ { t } \in J ^ { t } } \overline { { y } } _ { j _ { t } b _ { i } ^ { t } } } \end{array}$ , as obtained in the solution of problem $\mathrm { K } \dot { \mathbf { S } } ^ { t }$ , and accordingly modified constraints 3 , the remaining problem to solve is a pure Ž . fixed charge transportation problem 9,13 , which <sup>w</sup> <sup>x</sup> can be formulated as follows:

$$
\text { Problem   PFCT } ^ {t} z _ {\text { PFCT }} = \min \sum_ {i j _ {t} \in H ^ {t}} \xi_ {i j _ {t}} d _ {i j _ {t}}\tag{10}
$$

$$
s. t. \sum_ {j _ {t} \in J ^ {t}} x _ {i j _ {t}} = a _ {i} ^ {t}, i = 1, \dots , I
$$

Ž Ž .. from Eq. 2 ,

$$
\sum_ {i \in I} x _ {i j _ {t}} = \bar {y} _ {j _ {t}}, j _ {t} = 1, \dots , J ^ {t}\tag{\( (3') \}
$$

$$
M \xi_ {i j _ {t}} \geq x _ {i j _ {t}}, i = 1, \dots , I; j _ {t} = 1, \dots , J ^ {t}
$$

Ž Ž .. from Eq. 4 ,

$$
\xi_ {i j _ {t}} \in \{0, 1 \} i = 1, \dots , I; j _ {t} = 1, \dots , J ^ {t}
$$

Ž Ž .. from Eq. 5 ,

$$
x _ {i j _ {t}} \geq 0 i = 1, \dots , I; j _ {t} = 1, \dots , J ^ {t}
$$

Ž Ž .. from Eq. 7 .

This problem will be described in more detail in the following subsection. Here, we want to point out that problems ${ \bf K } { \bf S } ^ { t }$ and $\mathrm { P F C T } ^ { t }$ show an inherent hierarchical structure, in the sense that the solution of $\mathrm { P F C T } ^ { t }$ must follow that of ${ \bf K } { \bf S } ^ { t } .$ . This suggests an easy way to provide a set of efficient solutions for the overall multi-objective problem we want to solve. The solutions correspond to different solutions of problem ${ \bf K } { \bf S } ^ { t }$ , specifically to its k best solutions, where the number k of solution to consider is a user-defined parameter.

## 2.1.2. Pure fixed charge transportation

The problem that we have to solve in correspondence to each ${ \bf K } { \bf S } ^ { t }$ solution is thus a pure fixed-charge transportation problem PFCT . This is a NP-hard Ž . problem which can be solved to optimality only for small size problems 13 , closely akin to the better<sup>w</sup> <sup>x</sup> known fixed-charge transportation problem 2,20 ,<sup>w</sup> <sup>x</sup> but with no linear cost appended to arcs.

Exact and heuristic algorithms have been proposed for problem PFCT, approaching it via branch and bound techniques, Lagrangean decomposition or constraint generation 9,13 . However, these ap- <sup>w</sup> <sup>x</sup> proaches have been applied only to small size cases, at most $2 0 \times 2 0$ . Since our instances are much bigger, we resorted to a much simpler heuristic.

The linear relaxation of constraints 5 of problem Ž . PFCT reduces it to a standard transportation problem TP.

$$
\text { Problem   TP } ^ {t} z _ {\mathrm{TP}} = \min \sum_ {i j _ {t} \in H ^ {t}} x _ {i j _ {t}} d _ {i j _ {t}}\tag{\( (10') \}
$$

$$
\text { s.t. } \sum_ {j _ {t} \in J ^ {t}} x _ {i j _ {t}} = a _ {i} ^ {t}, \quad i = 1, \dots , I
$$

Ž Ž .. from Eq. 2

$$
\sum_ {i \in I} x _ {i j _ {t}} = \overline {{y}} _ {j _ {t}}, \qquad j _ {t} = 1, \ldots , J ^ {t}
$$

Ž Ž <sup>X</sup> from Eq. 3 ..

$$
x _ {i j _ {t}} \geq 0 i = 1, \dots , I; j _ {t} = 1, \dots , J ^ {t}
$$

Ž Ž .. from Eq. 7 .

From linear programming theory, we know that a solution of TP has exactly $J ^ { t } + I - 1$ basis variables, each of which corresponds to a used arc, thus to a non-zero $\xi _ { i j _ { t } }$ variable of PFCT. Since the instances we want to solve have $J ^ { t } \gg I , \ \forall t$ , and since obviously a PFCT solution must have at least $J ^ { t }$ non-zero $\xi _ { i j _ { t } }$ variables, we are sure that using the optimal TP solution as an heuristic solution for PFCT will lead to an error which is at most equal to the contribution given by the I<sup>y</sup>1 variables corresponding to a double plant assignment for as many municipalities. The percentage error so induced vanishes for large $J ^ { t } ,$ , as it is in our case.

We decided therefore to use a standard Hungarian code for solving the problem instances corresponding to each KS<sup>t</sup> solution.

We stress here that this heuristic is viable only for PCFT problems structured like the ones we must face, that is with far more columns then rows. In cases where $J ^ { t }$ is comparable to I better heuristics can be designed.

The solutions so obtained for every technology are then combined to yield scenarios. All possible solution combinations, containing one solution for every technology, generate the set A of feasible scenarios.

## 2.2. Step 2: construction of problem Pareto-set of solutions

This module analyzes the elements of set A in order to reduce their number by eliminating solutions which show obvious deficiencies. Note that the denotation ‘Pareto-set’ is quite improper, especially since the criteria used in this phase are not yet those at the basis of multicriteria analysis see Section 2.3 , butŽ . correspond to general considerations, which do not require sophisticated computational models. Step 2 implements in fact a ‘quick-and dirty’ pruning phase aimed at reducing to a manageable set the alterna tives to be thoroughly analyzed by more advanced models. Specifically, the scenarios in A are evaluated according to the following criteria:

1. Prioritize smaller plants;

2. Prioritize bigger plants;

3. Equidistribution of disposed wastes over the population;

4. Geographical equidistribution of disposed wastes;

5. Prioritize the municipalities corresponding to the major producers.

Criterion 1 ranks better the solutions which consist of smaller plants, while criterion 2 does just the opposite. This is because there are opposing reasons backing each of these choices; the nonlinearity of the objective functions associated to each of the two criteria makes sensible the implementation of the two.

Criteria 3 and 4 favor solutions which spread the plant sites over the territory in such a way that no group of inhabitants and no geographical area, respectively, is penalized with respect to others. Finally, criterion 5 favors the solutions that locate new plants in the territory of the municipalities which produce comparatively larger amounts of waste.

When each of these criteria was translated into a numerical function to optimize maximize , the prob-Ž . lem of Step 2 became that of determining a Paretooptimal set P for a multicriteria decision problem. Note that all five criteria can be directly translated into numerical functions, since criteria 1 and 2 simply involve considering the capacities of the plants to be opened, criteria 3 and 4 involve computing a distribution index—we computed the basin of attraction of each plant, in terms of municipality areas and populations, respectively—and criterion 5 is based on yearly waste production data.

To determine nondominated solutions, we simply compared the indices obtained for the scenarios obtained in step 1, the determination of the Pareto-optimal set P is then immediate. Finally, to constrain the number of scenarios to a pre-defined value ) —assuming $| P |$ to be greater than  ) as it has always been in our tests—we used a reference point <sup>w</sup> <sup>x</sup> 25,26 procedure. Specifically we identified the reference point of the problem also called its Ž utopia solution and we computed the distance between . each scenario and the reference point. The distance was computed simply as an Euclidean distance between the points representing the solutions in the space of the criteria, where the co-ordinates associated to the criteria were normalized into 0,1 in such a way that the maximum distance between any solution and the reference point was set to 1. The set P was then reduced maintaining only its  ) solutions closest to the reference point.

## 2.3. Step 3: solution of the multicriteria problem

From the available discrete multicriteria methods, it was decided to use one based on outranking techniques, whose adaptability to the type of application under study has been carefully analyzed 21 .<sup>w</sup> <sup>x</sup>

From these the MAPPAC method 17 was cho-<sup>w</sup> <sup>x</sup> sen. The method MAPPAC is based on the comparison of pairs of feasible actions taking into account all possible pairs of criteria. It has been preferred to better known methods, such as the ELECTRE 22,23<sup>w</sup> <sup>x</sup> or PROMETHEE 4 , because it relies on no prede-<sup>w</sup> <sup>x</sup> fined evaluation of the importance of the criteria: this augments the necessary CPU times, but permits to make more explicit partial dominance information, preferences and discordances. Moreover, a strong motivation to use it was the type of preferences modeling it offers. In fact, the possibility of defining compensation factors and convenient indifference areas for each pair of discordant criteria permits to manage partial dominance with a great flexibility.

Four scenario evaluation models were implemented. Details of these modules can be found in Ref. 19 .<sup>w</sup> <sup>x</sup>

## 2.3.1. Costs eÕaluation

Essentially, costs considerations are derived from the previous analysis. We considered explicitly both investment and running costs, moreover we added an estimate of the cost of downstream treatments, of the income from sales of possible recovered resources, of the costs associated to fund management for site clean-up expenses when the plant stops operation. The sum of all costs and revenues for each location yields the cost index of a scenario.

## 2.3.2. Risk of major accident

To estimate the risk of a major accident in a plant, we used a set of empirical factors which are related to the frequency and magnitude of potential accidents, taking into account risk from fire and explosion, toxic risk, and site vulnerability. The indices calculated for each separate risk cause and each separate plant are then combined in the overall plant risk index. The scenario risk index is then computed as a combination of the risk indices of the plants proposed by the scenario.

## 2.3.3. EnÕironmental impact

The relevant index quantifies the compatibility of a particular site with the characteristics of the geographic area where the facility is to be located. A vector of potential impacts on the environment is associated with each type of facility. Examples of potential impact are: pollution of surface and deep waters, atmospheric pollution, soil pollution, noise, smells, change of the land use. The environmental impact index associated to a site is obtained as a weighted average of the indices obtained for each of the impact vectors. The environmental impact index of a given scenario is obtained calculating the simple arithmetic mean of the environmental impact indices found for each of the scenario sites.

## 2.3.4. Transportation risk

The transportation risk evaluation estimates for each type of transportation the probability of an accidental release of polluting waste. These indices are then summed over all transportation modes to give a scenario transportation risk index.

The four numerical indices obtained by the listed modules for each scenario consist of real numbers, which are used as a basis for multicriteria analysis. The result of this analysis consists of the definition of an outranking relation among the different scenarios contained in set P. A graphic representation of the resulting relation is presented to the decisionmaker by means of the user interface, some of whose windows are presented in Section 3.

## 3. Case study

The specific case study concerned the Lombardy region, in northern Italy. The 1536 municipalities of this region were defined as the basic spatial units to which all the georeferenced information should refer. The georeferenced information includes the production of wastes of industrial origin and the location of present and future plants and disposal facilities in the area, as well as the strictly geographical data.

The geographical data considered includes the contour of the region, of the provinces and of the municipalities, the location, land use and population of each municipality, the road and the water resources networks, the location of sites of special interest for nature conservation, and the soil hydrogeology. We refer to Ref. 18 for more detailed<sup>w</sup> <sup>x</sup> information about the database structures and the use of GIS-based data.

The main source of information of the system was the draft Plan for the disposal of special, toxic and noxious waste of the Lombardy Region 15 . This<sup>w</sup> <sup>x</sup> document provided data concerning the amount and spatial location of the industrial waste produced in Lombardy and the description of the existent waste treatment and disposal facilities, and did indicate the potential locations for future similar facilities. This data is classified in terms of treatment and<sup>r</sup>or dis posal technological type of destination.

However, for each class of waste there are various technological possibilities for disposal and<sup>r</sup>or treatment, and so, in order to identify a unique destination a choice had to be made. The choice made was based on the opinion of the specialists who drew up the plan mentioned, and resulted in the adoption of the following seven technological waste treatment and disposal possibilities $\left( T = 7 \right)$ :

1. Biological Treatment

2. Chemical–Physical Treatment

3. Inertisation

4. Incineration

5. Controlled Landfill type II-A

6. Controlled Landfill type II-B

7. Controlled Landfill type II-C

Data concerning the production of wastes and the availability of waste treatment<sup>r</sup>disposal is classified in seven different waste disposal classes, for each of the municipalities of the reference region. In particular, the data concerning the production of industrial wastes is classified in categories of hazard, toxicity and flammability, for each of the destination types.

## 3.1. The multicriteria model

We solved a ${ S } ^ { t } , t = 1 , . . . , 7 .$ , problem for each of the disposal technologies. This implied the solution of a combined KS<sup>r</sup>PFCT for some technologies Ž . specifically, for technologies 4 and 6 , and of simply a PCFT for the remainder technologies 1, 2, 3, Ž 5, 7 because for these last technologies the existing . plants were sufficient to treat all the forecast waste.

Different scenarios are constructed by combining different alternatives for the considered technologies. In particular, we generated 10 knapsack solutions for technology 4 $( \mathrm { K S ^ { 4 } } )$ and as many for technology 6 $( \mathrm { K S } ^ { 6 } )$ ; the combination of these solutions with the fixed ones for the other technologies gives rise to a set A of 100 alternatives for further consideration in the remaining stages of the decision process.

The computational results obtained are summarized in Table 1, where column labels have the following meaning:

PROBL: problem identifier;

TECN: considered technology $t ~ ( t = 1 , \dots , 7 ) ;$

Ž <sup>t</sup> NDEP: number of possible plants J .;

NOP: number of opened plants in brackets theŽ number already existing. $\begin{array} { r } { ( \sum _ { j \in J ^ { t } } \bar { y } _ { j _ { t } } ) ; } \end{array}$

REQ: waste amount, in tons, to dispose $( \Sigma _ { i \in I } a _ { i } ^ { t } ) \Sigma$ ; $\mathbf { C A P } \mathbf { : }$ disposal capacity, in tons, for this solution Ž . B ;

Table 1  
Computational results on the Lombardy KS<sup>r</sup>PFCT problem

<table><tr><td>PROBL</td><td>TECN</td><td>NDEP</td><td>NOP</td><td>REQ</td><td>CAP</td><td>PFCT</td><td>CPU</td></tr><tr><td>1</td><td>2</td><td>12</td><td>12(12)</td><td>259080</td><td>449300</td><td>30514</td><td>19</td></tr><tr><td>2</td><td>3</td><td>19</td><td>5(5)</td><td>102834</td><td>250000</td><td>30152</td><td>30</td></tr><tr><td>3</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>206585</td><td>27327</td><td>59</td></tr><tr><td>4</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>206585</td><td>27319</td><td>116</td></tr><tr><td>5</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>206585</td><td>27363</td><td>105</td></tr><tr><td>6</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>206585</td><td>27248</td><td>114</td></tr><tr><td>7</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>206585</td><td>28872</td><td>130</td></tr><tr><td>8</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>206585</td><td>28878</td><td>131</td></tr><tr><td>9</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>196585</td><td>31138</td><td>113</td></tr><tr><td>10</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>196585</td><td>31175</td><td>113</td></tr><tr><td>11</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>196585</td><td>30663</td><td>112</td></tr><tr><td>12</td><td>4</td><td>25</td><td>10(8)</td><td>183736</td><td>231585</td><td>29072</td><td>112</td></tr><tr><td>13</td><td>6</td><td>14</td><td>2(1)</td><td>227928</td><td>310000</td><td>53275</td><td>44</td></tr><tr><td>14</td><td>6</td><td>14</td><td>2(1)</td><td>227928</td><td>250000</td><td>52337</td><td>30</td></tr><tr><td>15</td><td>6</td><td>14</td><td>2(1)</td><td>227928</td><td>310000</td><td>51665</td><td>23</td></tr><tr><td>16</td><td>6</td><td>14</td><td>3(1)</td><td>227928</td><td>370000</td><td>49479</td><td>73</td></tr><tr><td>17</td><td>6</td><td>14</td><td>3(1)</td><td>227928</td><td>390000</td><td>45530</td><td>47</td></tr><tr><td>18</td><td>6</td><td>14</td><td>3(1)</td><td>227928</td><td>430000</td><td>48705</td><td>34</td></tr><tr><td>19</td><td>6</td><td>14</td><td>3(1)</td><td>227928</td><td>340000</td><td>48064</td><td>32</td></tr><tr><td>20</td><td>6</td><td>14</td><td>3(1)</td><td>227928</td><td>430000</td><td>49758</td><td>84</td></tr><tr><td>21</td><td>6</td><td>14</td><td>3(1)</td><td>227928</td><td>430000</td><td>47759</td><td>34</td></tr><tr><td>22</td><td>6</td><td>14</td><td>3(1)</td><td>227928</td><td>370000</td><td>46247</td><td>38</td></tr><tr><td>23</td><td>7</td><td>1</td><td>1(1)</td><td>51427</td><td>60000</td><td>70936</td><td>1</td></tr></table>

Table 2  
Alternatives suggested by different heuristic criteria

<table><tr><td rowspan="2">Heuristic</td><td colspan="7">Technology</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Prioritize smaller plants</td><td>0</td><td>1</td><td>2</td><td>3</td><td>0</td><td>17</td><td>23</td></tr><tr><td>Prioritize bigger plants</td><td>0</td><td>1</td><td>2</td><td>12</td><td>0</td><td>13</td><td>23</td></tr><tr><td>Equidistribution of disposed wastes over the population</td><td>0</td><td>1</td><td>2</td><td>3</td><td>0</td><td>16</td><td>23</td></tr><tr><td>Geographical equidistribution of disposed wastes</td><td>0</td><td>1</td><td>2</td><td>10</td><td>0</td><td>16</td><td>23</td></tr><tr><td>Prioritize the municipalities corresponding to the major producers</td><td>0</td><td>1</td><td>2</td><td>7</td><td>0</td><td>14</td><td>23</td></tr></table>

PCFT: cost in Km of the relative PCFT solutionŽ . z ; <sub>PCFT</sub>

CPU: CPU time seconds spent for solving thisŽ . problem.

The CPU time was obtained running the program on a PC<sup>r</sup>486, 66 MHz running under Windows. Technologies 1 and 5 are not explicitly considered in the table since the outcome for them did not require any modification of the currently implemented allocation<sup>r</sup>transportation solution.

The final phase of step 1 consists in the determination of set A. As specified in Section 2.1, this is simply done by juxtaposing one solution for each technology and considering all possible such combinations of the solutions presented in Table 1.

Subsequently, step 2 was started in order to determine the Pareto-optimal set P. The results, obtained by the application of the different heuristics introduced in Section 2.2, are presented in Table 2, where each combination heuristic<sup>r</sup>technology specifies which is the solution, among those presented in Table 1, which was rated as the best for that technology by that heuristic.

By combining the solutions suggested in Table 2, it is possible to reduce the set of solutions presented in Table 1 to construct the Pareto-optimal set P for the problem to solve. In particular, the combination of the undominated solutions, from the viewpoint of the heuristic criteria used, spotlights 11 solutions Žnumber 1, 2, 3, 7, 10, 12, 13, 14, 16, 17, 23, respectively which will be used for the construction . of the set P. Table 1 reports as highlighted lines the solutions which will give rise to the Pareto-optimal set P.

![](/api/attachments/Y7UHF3X7/fulltext/images/b9df58b412e5c0ab0a9459144105ca40c0aca9e87d54e92c7c792fee286a086d.jpg)  
Fig. 2. Assessment of the alternative scenarios.

![](/api/attachments/Y7UHF3X7/fulltext/images/99add875ae7171cce9ab0cc31ff2892810d63535bf55fe3be9d4397f456341c0.jpg)  
Fig. 3. Interface for the visualization of the users of the different sites of a scenario.

The Pareto-optimal set is in fact made up of scenarios, obtained by different chainings of the efficient solutions of Table 1. The total number of considered scenarios is thus reduced to 16, obtained as all possible combinations of the single efficient solutions obtained for technologies 2, 3 and 7 and of the four efficient solutions obtained both for technology 4 and for technology 6. These 16 alternatives are subjected to multicriteria analysis, as described in Section 2.3. The results of this analysis in presented to the decision maker, by means of the GUI outlined in Section 3.2.

## 3.2. The user interface

We implemented, using Visual C 4.0, a user interface aimed at providing the user with a tool that permits him to observe each step of the described analysis and to interact manually, modifying parameters, forcing choices, etc. As the interface is not substantially different from that presented in Ref. <sup>w</sup> <sup>x</sup> 18 , here we will only sketch an overview.

After the problem loading phase, the analysis is started up to generate the scenarios. This phase contains the single-objective optimization described in Section 4, which does not allow any user direction. When scenarios are generated, they are evaluated according to the indices introduced in Section 2.

Fig. 2 presents the window displaying intermediate results of the evaluation of each non-dominated scenario by means of indices which will then be combined to evaluate the criteria introduced in Section 2.3, used in the MCDA phase.

After the computation of the indices, it is possible to start the multicriteria analysis phase. As mentioned in Section 2.3, this has been done by means of a package based on the MAPPAC method, a method that provides the basis for making explicit outranking relations.

Finally, Fig. 3 presents a sample output interface window, showing a scenario and specifically the proposed plant locations together with the cluster of municipalities associated to a particular plant.

## 4. Final remarks

There are generally two main aims in constructing decision support systems. The first aim concerns the improvement of the quality of the decisions taken. This is attained in various ways. First, all the analytical structuring of the problem can stimulate constructive comparisons and provide a reference framework for identifying and solving the conflicts. Furthermore, they can produce a deeper knowledge of the problem, not obvious given its complex nature. Another important function is that of supplying a framework for integrating specialist information relative to the various disciplines involved in the problem. In a certain sense, the decision support system plays the role of the non-existent overall expert.

The second aim of a formalized decision study is to supply technical documentation in support of decisions both in front of authorities and of public opinion. Decision support systems not only indicate what information was used and where it came from, but also how the information has been used and why this means that the decision taken is the best. In fact, decision support systems are not intended to replace the decision maker in solving the problem: they are constructed to help the user to make responsible and clearly documented decisions, which use the potential available as much as possible.

The system described in the paper has been developed making both these elements clear. We present a fully developed system integrating advanced computational functionalities with complex database management, graphic presentation and interaction procedures. This paper specifically deals with the algorithmic issues faced in the project, while the data management and presentation elements have been proposed in Ref. 18 . The main point we like to stress<sup>w</sup> <sup>x</sup> is the decomposition of the efficient set identification procedure into two steps. This was possible given the almost hierarchical nature of the different objectives that had to be considered, a situation common to several real-world applications where financial considerations are prominent but not all-inclusive.

Our work testifies to the feasibility of the decomposed approach, the possibility to integrate advanced combinatorial optimization modules with off-theshelf MCDA systems in order to provide full-featured decision support and the effectiveness of the resulting architecture in a complex real-world application.

Current work involves the application of the general architecture described in the paper to waste disposal problems arising in different regions in Europe, both relative to industrial and urban waste disposal. While in all cases the general architecture will be the same, the specific cases will require different routines, both as a single-objective highlevel function and as heuristics for determining the Pareto-optimal set.

## References

<sup>w</sup> <sup>x</sup> 1 D.J. Abel, S.K. Yap, R. Ackland, M.A. Cameron, D.F. Smith, G. Walker, Environmental decision support system project: an exploration of alternative architectures for geographic information systems, International Journal of Geographic Information Systems 6 1992 193–204.Ž .

<sup>w</sup> <sup>x</sup> 2 M.L. Balinski, Fixed-cost transportation problems, Naval Research Logistic Quarterly 8 1961 41–54.Ž .

<sup>w</sup> <sup>x</sup> 3 J.E. Beasley, An algorithm for solving large capacitated warehouse assignment problems, European Journal of Operational Research 33 1988 314–325.Ž .

<sup>w</sup> <sup>x</sup> 4 J.P. Brans, Ph. Vinke, A preference ranking organization method, Management Science 31 1985 647–656.Ž .

<sup>w</sup> <sup>x</sup> 5 A. Colorni, M. Dorigo, V. Maniezzo, Distributed optimization by ant colonies, IEEE Transactions on Systems, Man, and Cybernetics—Part B 26 1 1996 29–41.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 D.F. Cooke, Spatial decision support systems: not just another GIS, Geo Info Systems 2 1992 46–49.Ž .

<sup>w</sup> <sup>x</sup> 7 M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decision Support Systems 14 1995 219–235.Ž .

<sup>w</sup> <sup>x</sup> 8 K. Fedra, F.R. Reitsma, Decision support and GIS, in: H.J. Scholten, J.C.H. Stillwell Eds. , GIS for Urban and RegionalŽ . Planning, Kluwer Academic Publ. 1990 pp. 177–186.Ž .

<sup>w</sup> <sup>x</sup> 9 J. Fisk, P.G. McKeown, The pure fixed charge transportation problem, Naval Research Logistic Quarterly 26 1979 631–Ž . 641.

<sup>w</sup> <sup>x</sup> 10 F. Glover, Tabu search, Part 1, ORSA Journal on Computing 1 1989 190–206.Ž .

<sup>w</sup> <sup>x</sup> 11 F. Glover, Tabu search, Part 2, ORSA Journal on Computing 2 1990 4–32.Ž .

<sup>w</sup> <sup>x</sup> 12 D. Goldberg, Genetic algorithms in search, Optimization and Machine Learning, Wiley 1989 . Ž .

<sup>w</sup> <sup>x</sup> 13 M. Gothe-Lundgren, T. Larsson, A set covering reformula- ¨ tion of the pure fixed charge transportation problem, Discrete Applied Mathematics 48 1994 245–259.Ž .

<sup>w</sup> <sup>x</sup> 14 P. Hansen, B. Jaumard, E. Sanlaville, Weight constrained minimum sum-of-star clustering, GERAD Technical Report G-93-38 1994 .Ž .

<sup>w</sup> <sup>x</sup> 15 Lombardia Risorse, Plan for the Disposal of Special, Toxic and Noxious Waste in the Lombardy Region in Italian , Ž . Region of Lombardy, Milano 1990 .Ž .

<sup>w</sup> <sup>x</sup> 16 S. Martello, P. Toth, Knapsack Problems, Wiley 1990 . Ž .

<sup>w</sup> <sup>x</sup> 17 B. Matarazzo, Multicriterion analysis preferences by means of pairwise actions and criterion comparisons MAPPAC , Ž .

Applied Mathematics and Computation 18 2 1986 119–Ž . Ž . 141.

<sup>w</sup> <sup>x</sup> 18 I. Mendes, The Engineering of a Decision Support System for Industrial Waste Management, European Union Publications Office, EUR 15886 1994 .Ž .

<sup>w</sup> <sup>x</sup> 19 I. Mendes, A. Gadda, G. Granero, P. Haastrup, M. Mattarelli, F. Mazzeo, M. Paruccini, V. Maniezzo, Implementation of a Computer-based Decision Support System for Waste Management on a Sub-regional Area in Italian , P.O.P. Sicily,Ž . Project C—Pollution and Soil Erosion, ISIS Institute, TAsector report 1996 .Ž .

<sup>w</sup> <sup>x</sup> 20 G.L. Nemhauser, L.A. Wolsey, Integer and Combinatoria Optimization, Wiley Interscience 1988 .Ž .

<sup>w</sup> <sup>x</sup> 21 M. Paruccini, A. Zenie, Multicriteria decision support system ´ for environmental management: an European experience, Journal of Information Science and Technology 2 2Ž . Ž .1993 .

<sup>w</sup> <sup>x</sup> 22 B. Roy, Methodologie multicritere d’aide a la decision, Economica, Paris 1985 .Ž .

<sup>w</sup> <sup>x</sup> 23 B. Roy, Decision aid and decision making, presented at 3rd International Summer School on MCDA, Monte Estoril, Portugal 1988 . Ž .

<sup>w</sup> <sup>x</sup> 24 A.P. Sage, Decision Support Systems Engineering, Wiley Interscience 1991 .Ž .

<sup>w</sup> <sup>x</sup> 25 A. Wierzbicki, The use of reference objectives in multiobjective optimization, in: G. Fandel, T. Gal Eds. , MCDMŽ . Theory and Application, Springer-Verlag 1980 pp. 468– Ž . 486.

26 A. Wierzbicki, A mathematical basis for satisfying decision making, Mathematical Modelling 3 1982 391–405. Ž .

![](/api/attachments/Y7UHF3X7/fulltext/images/e341eb12706aa0577ed15acac406f53e5bb4960ada18e1822b1972701c8363fd.jpg)

Vittorio Maniezzo was born in Ferrara Ž .Italy on February 9, 1962. He graduated in electrical Engineering at the Polytechnic of Milan in 1986 with full grades. After some experiences as a software analyst and consultant, he attended the courses for the PhD in Computer Science at the Polytechnic of Milan, obtaining the title in 1993. He won a contest for a postdoctoral position at the Institute for Systems, Informatics and Security formerly ISEI at the Joint Re-Ž .

search Center of the European Commission, in Ispra Italy , whereŽ . he remained until he won a contest for a position as researcher at the University of Bologna, where he is currently tenural assistan professor. The research interest of V. Maniezzo are focused on decision support systems, both from the architectural and the algorithmic viewpoints. He contributed to the design and implementation of several running systems, based on heuristic methods for combinatorial optimization. He authored many scientific publications, mainly on international journals.

Maria Isabel Lopes Mendes Gieb was born in Lisbon in 1959. She obtained in 1982 the BSc Diploma and in 1990 the MSc Diploma on Statistics and Operational Research department from the ‘Universidade Classica de Lisboa’, Lisbon. She worked as Analyst´ Programmer for the Lisbon Public Transport and as Applications Analyst<sup>r</sup>Project Leader for the Sociedade Portuguesa de Celulose. In 1987, she joined the Technology Assessment sector of the ISEI Institute of the European Commission Joint Research Centre as System Programmer. Currently she works as system designer and programmer of original prototypes of decision support systems for environmental management, and contributes to the third-party work activities assigned to the sector.

![](/api/attachments/Y7UHF3X7/fulltext/images/ae56902d9d36b5979f6d60a6bf5fbba440ac22ea5e69e13397eefa747d12599e.jpg)

Massimo Paruccini was born in 1940 and obtained his degrees in Mathematics and Philosophy from the Universities of Rome and Milan. Currently, he acts as Scientific Officer of the European Commission. He is Sector Head of the ‘Decision Support and Integrated Assessment’ sector. His institutional tasks are related to the environmental management and its human dimensions, sustainable evolution and integrated assessment. This can serve for creation of and

collaboration in international scientific networks and for advising decision-makers, from local to international levels, preparing a scientific basis for taking decision. These activities imply: theoretical studies and the development of decision support computer models; and evaluating the integrated assessment methodology for the environmental management. The scientific relevance of the activity is showed by papers presented to conferences, publications in scientific journals, links and collaborations with external academic and research bodies EuroWorking Group on MultiCri-Ž teria Decision Analysis, International Society for Economics, close collaboration with different Universities, etc. , and the participa-. tion to several actions of education EAEME, Eurocourses, PhDŽ and PostDoc tutorship ..
