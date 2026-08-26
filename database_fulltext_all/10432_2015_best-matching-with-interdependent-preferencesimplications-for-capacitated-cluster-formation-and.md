---
otero_id: 10432
otero_key: "XMPBT7CT"
title: "Best-matching with interdependent preferences—implications for capacitated cluster formation and evolution"
authors: "Mohsen Moghaddam; Shimon Y. Nof"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.08.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Best-matching with interdependent preferences—implications for capacitated cluster formation and evolution

Mohsen Moghaddam ⁎, Shimon Y. Nof

PRISM Center and School of IE, Purdue University, 315 N. Grant St., West Lafayette, IN 47907, USA

## a r t i c l e i n f o

Article history: Received 16 December 2014 Received in revised form 19 August 2015 Accepted 19 August 2015 Available online 28 August 2015

Keywords: Quadratic assignment problem Genetic algorithm Evolutionary algorithm Association/dissociation Emergence Collaborative control theory

## a b s t r a c t

Generalized best-matching refers to matching the elements of two or more sets, on a many-to-one or many-tomany basis, with respect to their mutual preferences and capacity requirements/limits. Generalized bestmatching problem (BMP) has a variety of applications in areas such as team and network design, scheduling, transportation, routing, production planning, facility location, allocation, and logistics. The problem is indeed analogous to the capacitated clustering problem, where a set of individuals are partitioned into disjoint clusters with certain capacities. This work defines, formulates, and analyzes an important behavior associated with the generalized BMP: The mutual influence of the elements of the same set on each other’s preferences, if matched to the same element of the other set. Such preferences are referred to as interdependent preferences (IP). A binary program is developed to formulate the problem and provide the basis for analyzing the impact of IP on generalized best-matching decisions from two perspectives: Optimal cluster formation (fixed sets) and evolution (emergent sets). A set of evolutionary algorithms is then developed to handle the complexity of the cluster formation problem, and enable the network of clusters to autonomously adapt to random changes, recover, and evolve. Results from several experiments indicate (a) significant impact of IP on the optimality of cluster formation and evolution decisions, and (b) efficiency of the developed evolutionary algorithms in handling the problem’s complexity, and the emergent behavior of matching.

Published by Elsevier B.V.

## 1. Introduction

## 1.1. Significance and motivation

Generalized best-matching problem (BMP) [1] is the problem of finding the best match between the elements of two or more sets, on a many-to-one or many-to-many basis, considering certain criteria and conditions. Applications of the generalized BMP range from network design (e.g., supply/sensor networks) to scheduling (e.g., machine/grid scheduling, batching), clustering, transportation and routing (e.g., vehicle routing problem, traveling salesman problem), production planning (e.g., batch loading, group technology, order selection), facility location, allocation (e.g., interns to hospitals; students to schools), logistics (e.g., demand partitioning, sourcing, market clearing), team formation and social networking [2–4]. The ultimate goal of all these (and similar) applications is to form optimally matched, capacitated clusters.

The original instance of generalized BMP, i.e., the many-to-one BMP, is analogous to the capacitated clustering problem—the problem of partitioning a number of individuals into disjoint clusters with certain capacities. That is, capacitated clustering can be recast as a problem of finding the best two-sided match between the set of individuals (set I) and the set of clusters (set J). For instance, customers, tasks, and interns may represent the sets of individuals to be respectively matched to suppliers, machines, and hospitals, each representing a specific cluster with limited capacity (e.g., a supplier can serve a limited number of customers; a machine can process a limited number of tasks; a hospital can admit a limited number of interns). The difference between the many-to-one BMP and the capacitated clustering problem, however, is in their objectives. The objective of the many-to-one BMP is to maximize a set of matching criteria subject to certain capacity limits and requirements, while the capacitated clustering problem merely ensures that the clusters’ capacities are not violated [5].

Matching criteria are diverse, from cost to distance (e.g., between suppliers and customers), performance (e.g., machines processing tasks with different speeds), quality (e.g., dimensional tolerance of assembly products), and stability, depending on the application and scope. Without loss of generality, however, matching criteria can be formalized as preferences of the elements of different sets for each other. Such preferences may or may not be fixed and independent of environmental and decisional factors. The purpose of this work is to investigate an important behavior associated with the generalized BMP: The potential influences of best-matching decisions on the individuals’ preferences. Specifically, the motivation is to investigate two-sided matching instances between sets I and J, where the preference of i ∈ I for j ∈ J may be influenced by and represented as a function of matching $i ^ { \prime } \in I , i ^ { \prime } \neq i ,$ to j ∈ J (see Fig. 1).

```csv
Nomenclature
Acronyms
BMP best-matching problem
GA genetic algorithm
QAP quadratic assignment problem
EA evolutionary algorithm
IP interdependent preferences
Indices
i,k set I
j,l set J
Parameters
Mj capacity of j ∈ J
Pij mutual preference of i ∈ I and j ∈ J
c chromosome
αii' influence of i' ∈ I on the mutual preference of i ∈ I and j ∈ J
pi → j preference of i ∈ I for j ∈ J
Pij IP of i ∈ I and j ∈ J
cm modified chromosome
Variable
χij 1, if i ∈ I and j ∈ J are matched; 0, otherwise
```

To better comprehend the notion of interdependencies among preferences in best-matching, consider the following example. Suppose you have just arrived at a social gathering and are going to choose a table to sit at (Guests: Set I; Tables: Set J). Besides your initial preference for each individual table (e.g., location; food), your choice may be influenced by the people who are already sitting at each table. It is a natural phenomenon; we have different perceptions and attitudes about different people. The preferences, as described earlier, are merely an abstraction of various matching criteria, and thus, such interdependencies may have certain implications in different application domains. Some practical examples are:

• Enterprise collaboration. The “profitability” of a particular coalition for an enterprise may be influenced (increased/decreased) by the members (i.e., other enterprises) of that coalition

• Wireless sensor networks. The choices of an individual sensor for different clusters in terms of “energy consumption” may be influenced by the type, number, and energy level of the sensors in each cluster.

• Swarm robotics. The “efficiency” of an individual robot may be influenced by its assignment to different teams, depending on the depending on the type, number, and functionality of the robots in each team.

• Scheduling. The optimal allocation of a task to a machine in terms of “makespan” or “cost” may be influenced by the processing and/or setup requirements of the tasks that are already in process or in the queue of each machine.

• Storage assignment. The best storage location for a particular product in terms of “total movement time” of material handling devices may be influenced by its affinity with the already allocated products.

Interdependencies among preferences can dramatically influence best-matching decisions and lead to non-optimal or even paradoxical decisions, if disregarded. The notion of Interdependent Preferences (IP), coined by Gaertner [6] and Pollak [7] in the 1970s, has been extensively investigated in utility theory, as an indication of the dependencies of the individuals’ preferences on the consumption or well-being of other individuals in their neighborhood [8–13]. Also known as peer influence, neighborhood effect, bandwagon effect, and conformity [14], IP leads to either altruistic or envious behaviors—instead of considering their own absolute payoffs, individuals tend to evaluate their payoffs relative to those of others [15,16]. In social sciences and psychology, the notion of IP is known as interpersonal relations/behaviors/emotions (e.g., mutual trust [17,18]), and is proven to have significant impacts on social interactions and team/group activities [19,20]. Examples include success/failure of collaborative marketing and sales teams [21], conflicts, job satisfaction, effectiveness, and turnover of interactive nursing units [22], efficiency and rate of errors/ miscommunication in surgical units and operating rooms [23,24], performance, throughput, and cost of construction projects [25], all influenced by certain mutual interactions among individuals.

The major motivations of this study are (a) the widespread applications of IP, (b) the lack of generic and formal analysis in BMP literature, and (c) the impact of IP on capacitated cluster formation and evolution. Accordingly, this work defines, formulates, and analyzes an extension of the generalized BMP with IP (henceforth, BMP-IP), where the elements of the same set influence each other’s preferences for the elements of the other set(s), if matched to the same element.

## 1.2. Outline

For the sake of simplicity and without loss of generality, a many-toone BMP-IP with two sets is considered, where each element of set I can be matched to up to one element from set J, considering interdependencies among the preferences of the elements of set I (see Fig. 1). The BMP-IP under study is indeed a capacitated clustering problem—each element of set J can be matched to a limited number of elements from set I. The clustering must be performed with respect to the mutual preferences of I's and J's, the capacity limits of J’s, and the influences of I's on each other’s preferences.

The BMP-IP is first investigated from the cluster formation perspective: Sets I and J are fixed, and all elements are matched simultaneously, given their preferences and respective IP, capacity requirements and limits. The outcome of the capacitated many-to-one BMP is a set of clusters, each corresponding to a specific element of set J (e.g., j and j in Fig. 1). Those clusters may not be necessarily disjoint and may interact and collaborate with each other; e.g., demand-capacity sharing among suppliers [26]; tool sharing among machines [27]; task sharing enterprises [28]. The problem is formulated as a binary program, with IP defined as a linear combination of binary best-matching variables (Section 2). Accordingly, the BMP-IP turns into a Quadratic Assignment Problem (QAP), which is known as an NP-hard problem [29]. Therefore, a Genetic Algorithm (GA) is developed to handle the inherent complexity of the BMP-IP (Section 3).

![](/api/attachments/XMPBT7CT/fulltext/images/fe72b26cd401283cef13eaa9f2212930a3bcda685cc61b9ee567e5df544c1ebc.jpg)  
Fig. 1. Generalized BMP (many-to-one) with Interdependent Preferences (IP); The preferences of i ∈ I for j ∈ J and j ∈ J may vary, depending on which other elements of set I have already been matched to j and $j _ { 2 } .$ For instance, matching i to j may increase, decrease, or not change the preference of i for j (and vice versa).

Following the formation, a mechanism is developed for real-time administration and control of the dynamic changes in the structure of the capacitated clusters. In this work, evolution or emergence [30] of the networked clusters refers to association of new individuals or dissociation of existing individuals (to/from either set I or J). These behaviors are formalized by two principles of the collaborative control theory [31]: association/dissociation and emergent lines of collaboration and command. Such evolutionary behaviors are influenced by two main characteristics of the BMP-IP: The limited capacities of clusters and the interdependencies among the individuals’ preferences. For instance, when a new individual is associated to set I, its feasible choices and preferences may vary depending on the current matching of the I’s to the J’s, and the available capacity of each individual element of set J. An Evolutionary Algorithm (EA) is therefore developed to model and analyze the impact of IP on the real-time administration, optimization, and control of the evolution of the networked clusters (Section 4).

Several experiments are performed on various test-problems to investigate the impact of IP on the formation and evolution of capacitated clusters, the sensitivity of best-matching decisions to the intensity of interdependencies among preferences, and the computational efficiency of the developed algorithms (Section 5).

## 2. Preliminaries

## 2.1. BMP—a synopsis

Best matching is a fundamental problem in the design and control of distributed and networked systems, with respect to certain requirements, conditions, and criteria. BMP (a.k.a., the assignment problem; [32]) has been investigated from various perspectives, and several exact, approximation, and heuristic algorithms have been developed for solving different classes of this problem [2–4]. In this section, a concise taxonomic framework, the “PRISM taxonomy of BMP”, is presented, in order to characterize and formalize different classes of BMP with respect to 3 + 1 dimensions (Fig. 2). The goal is to provide an overview of BMP and highlight the scope BMP-IP, as a particular class of BMP investigated in this work. The 3 + 1 dimensions of BMP are as follows:

D1 Sets. This dimension formalizes the individuals to be matched and their pairwise relations, and classifies them into two or more sets. More specifically, D1 defines:

• Number of the sets. Individuals may be classified into two (e.g., tasksprocessors; students-schools) or more (e.g., jobs-machines-operators) sets.

• Pairwise relationships. The number of individuals in each set may be equal (e.g., bolt-nut [33]) or different (e.g., interns-hospitals [34]). Each individual may be matched to one or more individuals from the other set(s). Specifically, the pairwise relationships between two sets of individuals may be one-to-one (e.g., organs-patients [35]), many-to-one (e.g., tasks-computing resources [36]), or many-to-many (e.g., suppliers-customers).

D2 Conditions. This dimension addresses various conditions that BMP may potentially involve. Examples of D2 include:

• Resource constraints. Restrictions on matching in terms of time, capacity, budget, space, etc.

• Precedence relationships. A.k.a., categorized BMP (e.g., assembly line balancing [27]).

• Resource sharing. As a sub-class of the resource-constrained BMP, this condition refers to instances where the elements of the same set (with limited resources) are allowed to share resources while being matched to the elements of the other set(s). Examples include enterprise collaboration through demand-capacity sharing [26], collaborative assembly through tool sharing [27], and collaborative e-Service through task sharing [28].

• Layered matching. This condition refers to multiple levels or layers of matching that are interrelated, where the outcomes of two or more parallel matching processes at a certain level must be matched at the next level (e.g., assembly of subassemblies).

• Interdependencies. This condition refers to instances where two individuals that belong to the same set influence each other’s preferences for an individual in another set, if both are matched to it (in many-to-one/many-to-many BMP).

D3 Criteria. This dimension defines and formalizes (a) the matching criteria, and (b) formulation of the objective function(s). Matching criteria are diverse, ranging from classic cost and time factors to quality of service [36], dimensional tolerance [33], stability [35,37], and more. The objective function may be formulated in a variety of ways such as weighted sum, minimum deviation, quadratic, or cubic functions, and based on single criterion or multiple criteria [2].

![](/api/attachments/XMPBT7CT/fulltext/images/68f01eab9e25b3e418836eaa762dd0f5393f6b105564cebeaf6375212551c114.jpg)  
Fig. 2. The PRISM taxonomy of BMP.

D+ Time. All main dimensions of BMP may be influenced by time, as an additional dimension. Indeed, the inherent dynamicity and emergence associated with the nature of matching may considerably influence the other three dimensions of BMP realtime; $e . g . ,$ dynamic updates in the sets of subassembly parts with various dimensional tolerances [33]; dynamic allocation of tasks to different assembly workstations based on their varying processing times [27]. This additional dimension (D+) requires effective real-time optimization and control mechanisms to uphold the quality of matching over time.

According to the PRISM taxonomy of BMP, the BMP-IP can be characterized as follows:

D1 Two sets I and J are considered, with different sizes and many-toone pairwise relation, in that order.

D2 The BMP under study is resource-constrained (set J), and involves IP (set I).

D3 The matching criteria are simplified as normalized preference scores, and the objective is to maximize the overall satisfaction of preference scores.

D+ The BMP-IP is analyzed from two different perspectives: (a) Cluster formation with fixed, static sets (without $\mathsf { D } + \mathsf { ) } ;$

(b) Cluster evolution with emergent sets (with D+).

## 2.2. BMP-IP—definitions and mathematical formulation

Consider a best-matching between sets I and J on a many-to-one basis; i.e., each element i ∈ I can be matched to up to one element j ∈ J, while each element $\cdot j \in J$ can be matched to up to a limited number of elements of set I, denoted by $M _ { j } \left( M _ { j } \geq 1 \right)$ . Note that this definition considers equal “weights” (i.e., required capacities) for all elements of set I, which may not be true in some practical applications (e.g., customers with different demand rate; jobs with different processing time). This assumption, however, is made for the sake of simplicity and can be simply relaxed without any major modifications in the developed methodology. To better exemplify the BMP-IP logic as well as the evolutionary algorithms, dynamic coalition formation in enterprise networks is used as an illustrative example throughout the article, where set I refers to the set of enterprises, and set J refers to the set of coalitions, each with a limited capacity $M _ { j }$

## Definition 1. Best-matching variables

A best-matching X between sets I and J is a mapping from I∪J to itself, denoted by incident vector $\pmb { \chi } \in \{ 0 , 1 \} ^ { | I | \times | I | } ,$ , where

$$
\chi_ {i j} = \left\{ \begin{array}{l l} 1, & \text { if   } i \text {   and   } j \text {   are   matched } \\ 0, & \text { otherwise } \end{array} \right., \quad \forall (i, j) \in I \times J.\tag{1}
$$

## Definition 2. Mutual preferences

The mutual preference of i ∈ I and j ∈ J is formulated as

$$
P _ {i j} = \frac {p _ {i \rightarrow j} + p _ {j \rightarrow i}}{2}, \quad \forall (i, j) \in I \times J,\tag{2}
$$

where $p _ { i \to j }$ and $p _ { j \to i }$ respectively denote the preferences of i ∈ I for j ∈ J and $j \in J \operatorname { f o r } i \in I .$ To ensure consistency, all preferences are normalized between zero (no preference) and one (full preference).

In Definition 2, the mean value of individual preferences of two individuals is considered as their mutual preference. Depending on the nature of the problem, however, the mutual preferences may be defined in different ways. It is assumed that there are interdependencies between the individuals’ preferences, i.e., the preference of i ∈ I for j ∈ J and/or j ∈ J for $i \in I$ (and thus their mutual preference) may be changed, ${ \mathrm { i f ~ } } i ^ { \prime } \in I , i ^ { \prime } \neq i$ is matched to $j \in J .$ For instance, the preference of Enterprise A for a specific coalition may be changed depending on whether Enterprise B is a member of that specific coalition or not.

## Definition 3. Interdependent preferences

In case of interdependencies between preferences, the mutual pref erence of i ∈ I and $j \in J$ is formulated as

$$
\hat{P}_{ij} = P_{ij}\left(1 + \sum_{\substack{i^{\prime}\in I\\ i^{\prime}\neq i}}\alpha_{i i^{\prime}}\chi_{i^{\prime}j}\right),\quad \forall (i,j)\in I\times J,\tag{3}
$$

where $\alpha _ { i i ^ { \prime } }$ denotes the influence of $i ^ { \prime } \in \mathbb { I }$ I on the mutual preference of i ∈ I and j ∈ J, if i' is matched to j. Note that the influences are not necessarily bilateral, $i . e . , \exists i , i ^ { \prime } \in I , i ^ { \prime } \not = i , \alpha _ { i i ^ { \prime } } \not = \alpha _ { i ^ { \prime } i }$

## Definition 4. Mutual influences on preferences. i ∈ I is

1. Altruistic about $i ^ { \prime } \in I , i ^ { \prime } \neq i , \operatorname { i f } \alpha _ { i i ^ { \prime } } { > } 0 ,$

2. Envious about $i ^ { \prime } \in I , i ^ { \prime } \ne i , \mathrm { i f } \alpha _ { i i ^ { \prime } } { < } 0 ,$

3. Neutral about $i ^ { \prime } \in I , i ^ { \prime } \not = i , \mathrm { i f } \alpha _ { i i ^ { \prime } } = 0 .$

In this context, altruism/envy/neutralism refers to the situations where the mutual preference of two elements of sets I (e.g., enterprises) and J (e.g., coalitions) is increased/decreased/not changed, if another element of set I is matched to the same element of set J. The parameter α denotes the ratio of increase or decrease in the mutual preferences.

## Definition 5. BMP-IP

The objective of BMP-IP is to maximize the overall satisfaction of the preferences, taking into account the capacity limits and IP.

$$
\begin{array}{l l} \max & \sum_ {i \in I} \sum_ {j \in J} \hat {P} _ {i j} \chi_ {i j}, \\ \text {s.t.} & \sum_ {i \in I} \chi_ {i j} \leq M _ {j}, \quad \forall j \in J, \\ & \sum_ {j \in J} \chi_ {i j} \leq 1, \quad \forall i \in I, \\ & \chi_ {i j} \in \{0,   1 \}, \quad \forall (i, j) \in I \times J. \end{array}\tag{BMP - IP}
$$

According to the definition of IP, i.e. $\operatorname { E q } . \left( 3 \right)$ , the objective function of (BMP-IP) can be reformulated as

$$
\max \sum_{i\in I}\sum_{j\in J}P_{ij}\chi_{ij} + \sum_{i\in I}\sum_{j\in J}\sum_{\substack{i^{\prime}\in I\\ i^{\prime}\neq i}}P_{ij}\alpha_{ii^{\prime}}\chi_{ij}\chi_{i^{\prime}j},\tag{4}
$$

which is a quadratic function of binary variables. Accordingly, the BMP-IP is a special case of the QAP [38], a binary quadratic program with a quadratic function of variables in the objective function along with a set of linear constraints.

## 3. Cluster formation

The QAP is NP-hard [29], and thus is the BMP-IP. Several exact and heuristic approaches have been developed and examined in literature for solving the QAP [3,4,39], among which Ant Systems [40–42], and GA [43–45] are the most common techniques. In this work, GA is applied due to its simplicity and capability of solution representation and regeneration, ability to work with multiple solution sets, and compatibility with unique specification of different problems in terms of encoding and decoding schemes. GA, introduced by John H. Holland in the 1970s, is a powerful mechanism applied for solving a variety of combinatorial optimization and control problems. The notion of GA is based on the evolution through natural selection, which is the foundation for the evolutionary mechanisms developed in this work. To avoid the infeasibility of the solutions (in terms of capacity limits) and increase the efficiency of the algorithm, (1) a greedy heuristic is developed for generation of the initial population, and (2) a reproduction scheme based on path re-linking method [46] is developed for reproduction through crossover and mutation, as described in the following subsections.

## 3.1. Encoding

In any GA, each potential solution set is encoded as a chromosome. The efficiency and performance of the algorithm, in general, and the reproduction functions, in particular, depend on the applied encoding scheme. For the BMP-IP, a natural encoding scheme is applied: an array of length |I|, where each specific gene of a chromosome c corresponds to a specific element of set I, and each allele of each gene takes a value in J (Fig. 3). Note that if the overall capacity of set J is less than the size of set I, some elements of set I may remain unmatched. In the proposed encoding scheme, the alleles of the unmatched genes (if any) take zero values.

In the dynamic enterprise coalition formation example, the above encoding scheme is interpreted as follows: A chromosome that assigns a particular gene to each individual enterprise (i.e., set I), where the allele of each gene denotes the corresponding coalition (i.e., set J) of the respective enterprise. Note that due to the limitations on the number and capacity of the coalitions, a generated chromosome (as a potential configuration for the entire network of enterprises and coalitions) may not be feasible. Therefore, a greedy heuristic is developed for initialization of the algorithm, as described next.

## 3.2. Initialization

The performance of a GA substantially depends on the initial population generation, in terms of diversity, fitness, and, in this case, feasibility of chromosomes. To ensure these qualifications in the initial population, a greedy heuristic is developed, which generates each chromosomes of the initial population through the following steps:

Step 1. Generate a random permutation of the elements of I and store them in R in that order.

Step 2. Set $\begin{array} { r } { \hat { P } _ { i j } \gets P _ { i j } , \forall i , j . } \end{array}$

Step 3. Pick the first element of R, denote it by k, and assign it to l ∈ J such that

$$
\hat {P} _ {k l} = \max _ {j \in J} \left\{\hat {P} _ {k j} \right\}.
$$

![](/api/attachments/XMPBT7CT/fulltext/images/bf5766ba8fb70cf953be302ffe420b4f106b1893487c02d87fc4bf95b2317d3d.jpg)  
Fig. 3. Chromosomes (c) representation.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 4. Set $M_l \leftarrow M_l - 1$, and $R \leftarrow R \backslash \{k\}$.

Step 5. Set $\mathbf{c}(k) = l$, $\chi_{kl} = 1$, and update all $\hat{P}_{ij}$'s using Eq. (3).

Step 6. If $M_l &gt; 0$, go to the next step. Otherwise, set $J \leftarrow J \backslash \{l\}$, and then go to the next step.

Step 7. If
a) $R = \varnothing$, stop.
b) $R \neq \varnothing$ and $J = \varnothing$, set $\mathbf{c}(i) = 0$, $\forall i \in R$, and stop.
c) $R \neq \varnothing$ and $J \neq \varnothing$, return to Step 3.
</div>

The diversity of the initial solution is guaranteed by random ordering of I’s during while generating each chromosome (Step 1). In addition, the generated chromosomes are expected to have acceptable fitness values, because each individual is matched to its most preferred “available” match (Step 3). The generation also avoids capacity violation (i.e., infeasibility) in each chromosome by eliminating full J’s from the list of potential choices for the next I’s (Steps 6 and 7-b). If the available capacity of J's is less than the number of I's, the alleles of some genes take zero values in the chromosome. In the dynamic coalition formation example, a gene with an allele equal to zero means that its respective enterprise is not affiliated with any coalition.

## 3.3. Fitness evaluation

The fitness of each chromosome c is calculated using Eq. (4), where

$$
\chi_ {i j} = \left\{ \begin{array}{l l} 1, & i f \mathbf {c c c} (i) = j \\ 0, & o t h e r w i s e \end{array} \right.
$$

The fitness value represents the overall satisfaction degree of mutual preferences/IP.

## 3.4. Reproduction

After generation of the first population and evaluation of their fitness values, the next step is to produce the next population from the existing population of chromosomes. In a GA, reproduction can be performed in a variety of manners and through different genetic operators. Parent chromosomes must be selected to produce offsprings. In the dynamic coalition formation example, each parent chromosome represents a specific configuration of the entire network of enterprises and coalitions; therefore, the reproduction operators are intended to effectively combine those network configurations in order to achieve more optimal network configurations. According to the theory of natural selection and evolution, natural reproduction must result in stronger or fitter chromosomes in the next generations. The reproduction mechanisms of the GA must then be designed in a way that mimics this trait of biological systems. In this work, in addition to the fitness of the generated offsprings, their feasibilities must also be taken into account—to uphold the performance of the algorithm, infeasible solutions must be avoided during the reproduction procedure. Hence, a reproduction scheme is developed based on path crossover and path mutation mechanisms.

## 3.4.1. Path crossover

Crossover is a major reproduction mechanism in natural evolution, which combines the genes of two (or more) parents to produce offsprings. The crossover operator is critical for the success of GA. The operator must be able to probabilistically explores new solutions (to ensure diversity), and exploits good traits of previous generations (to ensure fitness). Therefore, a modified version of the path crossover method [46] with insert transformation [43] is developed, which besides diversity and fitness, guarantees the feasibility of the produced offsprings (Fig. 4):

Step 1. Randomly select two parent chromosomes, namely $\mathbf { c } _ { 1 }$ and $\mathbf { c } _ { 2 } ,$ and fix the genes with similar alleles (exploitation of good traits of parents). Randomly select a gene, and set $Z = 0 .$

![](/api/attachments/XMPBT7CT/fulltext/images/328742293e8ba657a8fd24bc4d2f149a746ddef590130384e99dcfa159eed98a.jpg)  
Fig. 4. Example of path crossover operation on two parent chromosomes c and c [Shaded: Fixed genes].

Step 2. If the current gene is fixed, set $Z \gets Z + 1$ and go to Step 3 (no off spring is generated). Otherwise, perform insert transformation:

(a) In parent c , randomly select an unfixed gene (other than the current gene), which has the same allele as the one in the current gene of $\mathbf { c } _ { 2 } .$ If there is no such gene in c , go to Step (c) (no offspring will be generated).

(b) Insert the allele of the selected gene at the current gene of c , and shift the alleles of other unfixed genes to the right.

(c) Apply (a) and (b) to $\mathbf { c } _ { 2 } ,$ then go to the next step.

(d) Place the original parents (i.e., c and c ) and the generated offsprings (i.e., transformed parents) into the chromosome pool CP.

Step 3. $\mathrm { I f } Z = | I | ,$ , go to Step 4. Otherwise, move to the next gene, from left to right in a cyclic fashion, and return to Step 2.

Step 4. Eliminate duplicates of chromosomes from CP (if any), sort the rest according to their fitness values, and select a number of fittest ones considering the population size and the crossover rate.

## 3.4.2. Path mutation

Mutation is another major biological evolution mechanism, which makes spontaneous and random changes in the alleles to ensure diversity in offsprings. The developed path crossover mechanism—in spite of its efficiency—does not make any changes in the “consumed” capacity of J’s (e.g., coalitions), as the number of I’s (e.g., enterprises) matched to each j ∈ J is the same in both parents and offsprings. This may eliminate some potential solutions, especially if the total capacity of J's is larger than the number of I’s (i.e., at least one cluster with one idle capacity). To resolve this issue and ensure the diversity of the next generations in terms of capacity utilization, a path mutation mechanism is developed. The mutation operator, similar to the crossover operator, produces offsprings through moving along a path and making spontaneous changes in the genes in sequence. The path mutation operator is designed in a way that the capacity limits are not violated, while, near-optimal offsprings are generated. If there is no idle capacity in the entire network of clusters, however, the mutation operator is skipped. The mutation procedure is as follows (Fig. 5):

Step 1. Randomly select a parent chromosome c and a gene k ∈ I, set $Z = 0 ,$ , and generate a list of J’s with free capacity, i.e.,

$$
L = \left\{j: M _ {j} > | \{i: \mathbf {c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c} J: M _ {j} > | \{i: \mathbf {c c c c c c c c c c c c c c c c c c c c c c} j, i \in I \} |, j \in J \right\}.
$$

Step 2. Replace the allele of the current gene of c $( i . e . , k )$ with $l \in L$ where

$$
\hat {P} _ {k l} = \max _ {j \in L} \left\{\hat {P} _ {k j} \right\}.
$$

Step 3. Place the original parent and the offspring into the chromosome pool CP, and set $Z \gets Z + 1$

Step 4. I $\mathrm { f } Z < | I | ,$ , move to the next gene from left to right in a cyclic fashion (i.e., update k), and then return to Step 2. Otherwise, go to the next step.

Step 5. Eliminate duplicates of chromosomes from CP (if any), sort the rest according to their fitness values, and select a number of fittest ones according to the population size and the mutation rate.

## 3.5. Parameters setting

The parameters of the GA are set as follows:

• Population size. $2 \times | I | .$ , proportional to the size of the problem.

• Stopping criterion. The algorithm stops if there is no improvement in the best solution obtained in the last 100 generations.

• Crossover rate. 0.7, 70% of the population undergo the path crossover operation.

• Mutation rate. 0.3, 30% of the population undergo the path mutation operation.

## 4. Cluster evolution

Evolution, in the context of this work, refers to association/dissociation of individuals to/from the system over time. Due to the interdependencies between the preferences of I's and the limited capacities of J's, each single association of a new individual or dissociation of an existing one may significantly influence the optimal topology of the networked clusters. Examples include:

• I’s. Arrival/departure of a job to/from a production cell; Introduction/ declination of a new product in a market; Allocation of new interns/ students to hospitals/schools; Temporary or permanent loss of a team member or leader.

• J’s. Purchasing or salvaging facilities (e.g., machines for production or vehicles for transportation); Emergence of a new market or saturation of an existing one; Opening or closing a line in a service system such as a bank; Establishing a new school/hospital.

Fig. 6 schematically illustrates the four types of evolution associated with the generalized BMP. In the dynamic coalition formation example, evolution can take place through association of a new enterprise to the network (Fig. 6a), dissociation of an existing enterprise from the network (Fig. 6b), formation (Fig. 6c) or termination (Fig. 6d) of a coalition. In all cases, the entire network of individuals and clusters must adapt to the changes made through association/ dissociation of elements of either set I or set J in an optimal fashion. In the case of association, it is assumed that the information regarding the new individual (i.e., original preferences and mutual influences) is known. In addition, only one association/dissociation is considered at a time. This assumption, however, is made for simplicity and the developed algorithms can be modified to handle simultaneous changes.

![](/api/attachments/XMPBT7CT/fulltext/images/af0f7cef86a35c06a9e85dc4cda039084e975799a526fe38ea3dacd8ebf0d6bf.jpg)  
Fig. 5. Example of path mutation operation on parent chromosomes c, where $\hat { P } _ { 4 , 2 } { \scriptstyle > } \hat { P } _ { 4 , 3 }$ [Shaded: J’s with extra capacity; i.e., j ∈ L].

![](/api/attachments/XMPBT7CT/fulltext/images/8acbbf077f4b8cb659d56365e4dbd0d44b53100d164e3a241fcb07b49c0bce93.jpg)

![](/api/attachments/XMPBT7CT/fulltext/images/f0ab899995bf324cc2f5db0a6127c15b146d1b936e63be393f3e3f8d5340cf5f.jpg)

![](/api/attachments/XMPBT7CT/fulltext/images/89b65aab96cdd186944ddfa8c37714a68e5c9ddc0d6c25ec375d620f60d481c0.jpg)

![](/api/attachments/XMPBT7CT/fulltext/images/dff129469f3bbf9aa3cad9247273cffc098f8dbe44f4e2619878b451a84d6f63.jpg)  
Fig. 6. Evolution of a capacitated network of clusters; (a) Association of a new element to set I (i ∈ I); (b) Dissociation of an existing element from set I (i ∈ I); (c) Association of a new element to set J (j ∈ J); (d) Dissociation of an existing element from set J (j ∈ J) [Arrow: Association/dissociation].

An EA is developed to enable optimal evolution and adaptation the networked clusters to changes. The EA follows the logic of the GA developed in the previous section, except for the initialization—after each single association/dissociation, the algorithm does not treat the problem as completely new. Instead, it exploit the good traits of the former network topology, which is assumed to be optimal, while exploring new solutions, in order to adapt to the respective change in a computationally efficient manner. Consider a network of capacitated clusters with optimal configuration, represented by chromosome c (with the encoding scheme as shown in Fig. 3). After any of the four types of changes (i.e., association/dissociation of I's or J's) takes place, the EA incorporates that change in the original chromosome c through a set of heuristics, resulting in a modified chromosome c<sup>m</sup>. The modified chromosome then duplicates and reproduces itself through the path crossover and path mutation mechanisms until an initial population of chromosomes is generated. Afterwards, the first population of chromosomes evolves via the GA until the optimal configuration of networked clusters is obtained. This procedure is repeated after each single change occurs.

## 4.1. First generation

The primary assumption of the EA is that the original chromosome c (before any changes take place) represents the optimal configuration of the networked clusters. Hence, the modified chromosome must be generated in a way that upholds its optimality, i.e., maintaining its good traits, while incorporating the new changes. A set of heuristics is developed to generate the modified chromosome under the four main types of evolution in the networked clusters:

## Set I

a) Association. After association of a new individual k to set I, i.e., I ← I ∪ {k}, a new gene is appended to the original chromosome c. The new gene corresponds to k, and its allele l represents its match in set J, which satisfies the following condition in the modified chromosome c<sup>m</sup>:

$$
\hat {P} _ {k l} = \max _ {j \in L} \left\{\hat {P} _ {k j} \right\},
$$

where

$$
L = \left\{j: M _ {j} > | \{i: \mathbf {c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c} J: M _ {j} > | \{i: \mathbf {c c c c c c c c c c c c c c c c c c c c c c} j, i \in I \} |, j \in J \right\}.
$$

If L = ∅, set c<sup>m</sup>(k) = 0. The alleles of the other genes remain unchanged in the modified chromosome $\mathbf { c } ^ { \mathbf { m } }$ . The above procedure identifies the elements of set J with extra capacities, and then matches the new individual to the one with the maximum mutual preference score.

b) Dissociation. After dissociation of an existing individual k from set I, i.e., I ← I \ {k}, the gene of the corresponding individual is removed from the original chromosome c, resulting in the modified chromosome $\mathbf { c } ^ { \mathbf { m } }$

## Set J

c) Association. After association of a new individual l to set J, i.e., J ← J ∪ {l}, the modi ed chromosome c<sup>m</sup> is generated as follows:

1) c<sup>m</sup> = c. Sort the elements of set I in ascending order of $\hat { P } _ { i j }$ and place them in the temporary set T.

2) Pick the first element of T and denote it by k.

3) If $\hat { P } _ { k j } < \hat { P } _ { k l } , j = { \bf c } ^ { \bf m } ( k )$ , set $\mathbf { c } ^ { \mathbf { m } } ( k ) = l ,$ and update $\hat { P } _ { i j } ^ { \phantom { * } } \overset { \cdot } { \mathbf { S } } \left( \mathbb { E } \mathbf { q } . \mathbf { \ } ( 3 ) \right)$ Otherwise, go to Step 4.

4) $T \gets T \backslash \{ k \} . \operatorname { I f } M _ { l } = \lvert \{ i : \mathbf { c } ^ { \mathbf { m } } ( i ) = l , i \in I \} \rvert$ or T = ∅ stop. Otherwise, return to Step 2.

The above procedure identifies the least satisfied elements of set I, i.e., the ones with the lowest preference scores, and matches them, one by one, to l (the new element of Set J), in case this change increases their preference score. The procedure stops if l has no further capacity or there are no other elements in set I that prefer l to their current match in set J.

d) Dissociation. After dissociation of an existing individual l from set J, $i . e . , J  J \backslash \{ l \}$ , the modified chromosome $\mathbf { c } ^ { \mathbf { m } }$ is generated as follows:

1) $\mathbf { c } ^ { \mathbf { m } } = \mathbf { c } .$

2) Define sets L and T:

$$
L = \left\{j: M _ {j} > | \{i: \mathbf {c} ^ {\mathbf {m}} (i) = j, i \in I \} |, j \in J \{l \} \right\},
$$

$$
T = \{i: \mathbf {c} ^ {\mathbf {m}} (i) = l \}.
$$

If L = ∅ or T = ∅, go to Step 4. Otherwise, go to Step 3.

3) Find k ∈ T such that $\begin{array} { r } { \hat { P } _ { k j } = \operatorname* { m a x } _ { i \in T , ~ j \in L } \{ \hat { P } _ { i j } \} , \exists j \in L , \mathrm { s e t } ~ \mathbf { c } ^ { \mathbf { m } } ( k ) = j , } \end{array}$ and return to Step 2.

4) If $T \neq { \mathcal { O } } ,$ set $\mathbf { c } ^ { \mathbf { m } } ( i ) = 0 ,$ , ∀i ∈ T.

After removal of l, the above procedure matches its corresponding elements in set I to other elements of set J with extra capacities (if any), in a way that the overall preference score is maximized (considering no other changes). In some cases, however, the number of elements of set I corresponding to l may be larger than the total available capacity of J's (after removal of l). In such cases, some elements of set I remain unmatched due to capacity shortage.

The above heuristics may not guarantee the optimality of the modified chromosome; however, they provide satisfactory quality. Each single change, however, may significantly influence the optimal topology of the networked clusters due to the interdependencies among preferences. Therefore, it may be difficult to directly identify the required modifications after each change takes place. The modified chromosome generated by the above heuristics must therefore be evolved to obtain the optimal configuration of the capacitated network of clusters. Optimization is handled by duplicating and reproducing the modified chromosomes through the reproduction operators of the GA, as described next.

## 4.2. Evolution

After the modified chromosome is generated, it duplicates and reproduces itself using the GA operators to generate new offsprings and eventually a population of chromosomes. The duplication and reproduction mechanism is similar to the mitosis process in cell division and duplication (Fig. 7). Specifically, the modified chromosome first generates another chromosome through mutation. The two chromosomes then generate two new chromosomes through crossover. The four chromosomes then generate four new chromosomes, and the procedure continues until the number of generated chromosomes reaches a predefined population size.

The evolution, from the modified chromosome toward the optimal one, is based on the path crossover and path mutation mechanisms, and the GA developed in Section 3. The EA is therefore composed of the following steps:

Step 1. Define $C = \{ \mathbf { c } ^ { \mathbf { m } } \}$ and PS as the set of chromosomes in the first population, and population size, respectively, and

$$
L = \left\{j: M _ {j} > | \left\{i: \mathbf {c} ^ {\mathbf {m}} (i) = j, i \in I \right\} |, j \in J \right\}.
$$

Step 2. $\operatorname { I f } \left| L \right| > 0 ,$ go to Step 3, otherwise, go to Step 4.

Step 3.

a) For each chromosome c in C do path mutation until an offspring chromosome $\mathbf { c } ^ { \prime } \neq$ c is generated. $C \gets C \cup \{ { \bf c } ^ { \prime } \} . \mathrm { I f } | C | = P S ,$ , go to Step 5. Otherwise, go to Step 3-b.

b) Randomly pair the chromosomes in C. For each pair $\mathbf { c } _ { 1 }$ and $\mathbf { c } _ { 2 } ,$ do path crossover until two offspring chromosomes $\mathbf { c } _ { 1 } ^ { \prime } \neq \mathbf { c } _ { 2 } ^ { \prime } \neq \mathbf { c } _ { 1 } \neq \mathbf { c } _ { 2 }$ are generated. $C \gets C \cup \{ \mathbf { c } _ { 1 } ^ { \prime } , \mathbf { c } _ { 2 } ^ { \prime } \} . \mathrm { I f } \ | C | = P S ,$ , go to Step 5. Otherwise, return to Step 3-a.

Step 4.

a) Perform swap mutation on $\mathbf { c } ^ { \mathbf { m } }$ to generate another chromosome: $\mathbf { c ^ { \prime } } = \mathbf { c } ^ { \mathbf { m } }$ , randomly select $i , k \in I , i \neq k ,$ , and then $\mathbf { c } ^ { \prime } \left( i \right) = \mathbf { c } ^ { \mathbf { m } } ( k )$ and $\mathbf { c } ^ { \prime } \left( k \right) = \mathbf { c } ^ { \mathbf { m } } ( i ) . C \gets C \mathsf { U } \{ \mathbf { c } ^ { \prime } \} .$

b) Randomly pair the chromosomes in C. For each pair $\mathbf { c } _ { 1 }$ and $\mathbf { c } _ { 2 } ,$ do path crossover until two offspring chromosomes $\mathbf { c } _ { 1 } ^ { \prime } \neq \mathbf { c } _ { 2 } ^ { \prime } \neq \mathbf { c } _ { 1 } \neq \mathbf { c } _ { 2 }$ are generated. $C \gets C \cup \{ { \bf c } _ { 1 } { } ^ { \prime } , { \bf c } _ { 2 } { } ^ { \prime } \} . \mathrm { I f } \ | C | = P S , \mathrm { g c }$ o to Step 5. Otherwise, redo Step 4-b.

Step 5. Take C as the initial population, and do GA until the optimal configuration is obtained.

Steps 3 and 4 of the algorithm generate the first population of chromosomes. Step 3 deals with the situations where at least one element of set J has extra capacity, and applies path mutation and path crossover as reproduction mechanisms to guarantee the feasibility, diversity (through exploration of new solutions), and quality (through exploitation of good traits of parent chromosomes) of the generated chromosomes. Step 4, on the other hand, handles the situations where none of the element of set J has extra capacity. In such cases, the path mutation is not applicable. Therefore, the modified chromosome $\bar { \mathbf { c } } ^ { \bar { \mathbf { m } } }$ first generates an offspring through a single swap mutation (Step 4-a), and then the rest of the initial population is generated through path crossover (Step 4-b). After generating the first population, the GA developed in Section 3 is applied to find the optimal configuration of the evolved networked clusters.

![](/api/attachments/XMPBT7CT/fulltext/images/4a64751a6cbac8630b2494cb66dd3305b7489ab991d497f92a1b59ff0d778469.jpg)  
Fig. 7. Mitosis-like duplication and reproduction of the modi ed chromosome and generation of the rst population of chromosomes. In each reproduction step x $, 2 ^ { x }$ chromosomes are generated.

Table 1 Optimal chromosomes of S0 and S1; TP (20, 8).

<table><tr><td>S0</td><td>2</td><td>3</td><td>4</td><td>6</td><td>8</td><td>5</td><td>3</td><td>2</td><td>2</td><td>8</td><td>2</td><td>7</td><td>5</td><td>2</td><td>8</td><td>3</td><td>2</td><td>1</td><td>2</td><td>2</td></tr><tr><td>S1</td><td>3</td><td>3</td><td>4</td><td>6</td><td>8</td><td>2</td><td>1</td><td>5</td><td>2</td><td>8</td><td>2</td><td>7</td><td>5</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>8</td></tr></table>

## 5. Numerical experiments

## 5.1. Design of experiments

Several experiments are performed on a set of test-problems to analyze the impact of interdependencies between preferences on bestmatching, from both cluster formation and evolution perspectives. The numerical experiments are specifically intended to illustrate

1) The role of IP in the formation of capacitated network of clusters, and the negative impact of disregarding them on the optimal configuration of clusters and the entire network.

2) Sensitivity of cluster formation decisions to the intensity of mutual influences and level of interdependencies between preferences.

3) The way capacitated clusters evolve, and the impact of IP and capacity limits on their evolution.

The following two scenarios are defined to perform the above analyses:

S0 BMP without considering IP. The same methodology is applied for cluster formation and evolution, where the influences of individuals on each other’s preferences are ignored in the optimization process $( i . e . , \alpha _ { i i ^ { \prime } } = 0 , \forall i , i ^ { \prime } \in I )$ . That is, the optimization is <sup>¼</sup>performed without considering the actual values of α's, while they are ultimately incorporated in calculating fitness values Eq. (4).

S1 BMP-IP. In both scenarios, it is assumed that there are interdependencies between the preferences of the elements of set I (e.g., enterprises) for the elements of set J (e.g., coalitions). S0, however, disregards those interdependencies. Four testproblems TP (20, 8), TP (40, 18), TP (60, 25), and TP (80, 30) are generated, where the first and second entries respectively denote |I| and |J| (the proportion between |I| and |J| in the testproblems are selected arbitrarily). In each experiment on each test-problem, the preferences $( i . e . , p _ { i  j } , p _ { j  i } , i \in I , j \in J )$ , the influences of I's the preferences of each other $( i . e . , \alpha _ { i i ^ { \prime } } , i , i ^ { \prime } \in I )$ , and the capacities of the $J ^ { \prime } s \ ( i . e . , M _ { j } , j \in J )$ are generated randomly following uniform distribution. The preferences are uniformly distributed in [0, 1], where 0 and 1 indicate no and full preference, respectively. The mutual preferences are then calculated using Eq. (2). The influences of I's on each other’s preferences are uniformly distributed in [–0.2, 0.2], i.e., i′ ∈ I may increase/decrease the preference of $\mathrm { ~ : ~ } \in I , i \neq i ^ { \prime } , \mathrm { t o } j \in \mathrm { { J } }$ J up/down to 20%, if they both are matched $\mathrm { t o } j \in J .$ The capacity limits of J's are generated randomly, where the total capacity is uniformly distributed in $[ | I | - 0 . 1 | I | , | I | + 0 . 1 | I | ]$ (to ensure consistency and cover instances with limited and extra capacities). The reason behind using uniform distribution is to maintain the randomness of each independent experiment on each test-problem; that there is no a priori information on the exact values of the parameters.

## 5.2. Cluster formation

The first two goals of the numerical experiments are addressed in this section, i.e., the impact of IP on cluster formation and the sensitivity of the results to the intensity of mutual influences between I's. Ten experiments are performed on each test-problem. All experiments are independent of each other in terms of preferences, influences of I's on each other’s preferences, and capacities of J's. Table 1 shows the optimal solutions (chromosomes) for the last experiment on TP (20, 8), under S0 and S1. The positions (genes) and their respective values (alleles) correspond to the elements of sets I and J, respectively. The two scenarios yield different network configurations with a considerable gap between their optimal fitness values, as expected. Fig. 8 shows the gap between the normalized optimal fitness values (i.e., Objective Function (4) divided by |I|) obtained from S0 and S1 for different test-problems. In all experiments, S0 and S1 yield completely different network configurations (Details are omitted for the sake of brevity). The results prove that if there are interdependencies between the preferences, disregarding them may lead to misleading and non-optimal decisions.

A paired t-test is performed to analyze the significance of the gap between the optimal fitness values of S0 and S1. The test compares the means of the two treatments (i.e., the fitness values of S0 and S1) based on the following hypotheses:

$$
\begin{array}{l} \bullet H _ {0} \colon \overline {{F}} _ {S 0} = \overline {{F}} _ {S 1} \\ \bullet H _ {1} \colon \overline {{F}} _ {S 0} \neq \overline {{F}} _ {S 1} \end{array}
$$

where F denotes the fitness values. At the significance level of 0.05 and the freedom degree of 9, the paired t-test parameter is 2.26, which is lower than the t-test estimates obtained for different test-problems: 5.63, 7.77, 9.94, and 10.26 for TP (20, 8), TP (40, 18), TP (60, 25), and TP (80, 30), respectively. The null hypothesis is therefore rejected, which implies a significant gap between the fitness values of S0 and

![](/api/attachments/XMPBT7CT/fulltext/images/c4eb99f6eb67953fc9d862a0b46c57f8dc6366116b3b2215137e8f1fb393c1ee.jpg)  
Fig. 8. The gap between the optimal normalized tness values of S0 and S1 $[ \mathrm { G a p } = { \overline { { F } } } _ { \mathrm { S 1 } } - { \overline { { F } } } _ { \mathrm { S 0 } } ] .$

![](/api/attachments/XMPBT7CT/fulltext/images/916c3af1aa7b2c0ac444f3c44b4d27abc29bbf54f848e5daf3ae253b82384bcd.jpg)  
Fig. 9. Sensitivity of the gaps between the optimal normalized fitness values of S0 and S1 to α's.

S1. Since the gap is positive in all cases, it is concluded that S1 significantly outperforms S0, where the gap, according to the t-test estimates, is almost proportional to the size of the problem.

The gap between the results of S0 and S1 is rooted in the intensity of the influences of the I's on each other's preferences (i.e., α's). The results shown in Fig. 8 are based on the default values of α's (i.e., [–0.2, 0.2]). To indicate the impact of α's on the gap between the results of S0 and S1, a sensitivity analysis is performed on each test-problem (one experiment on each), as shown in Fig. 9. The results prove that higher mutual influences of I's on each other’s preferences, positive or negative, lead to more dramatic changes in the optimal cluster formation, and disregarding such influences becomes substantially more detrimental to the optimality of matching.

## 5.3. Cluster evolution

The third goal of the numerical experiments is addressed here. The optimal network configuration obtained from the last experiment through S1 is selected as the initial state. Then, ten changes, five associations and five dissociations, are simulated and made in a cyclic fashion, i.e., a new element associates to the network, then an existing element dissociates from the network, and so on. The changes are made in sets I (e.g., enterprises) and J (e.g., coalitions) in separate and independent experiments. All the input parameters corresponding to the associating individuals (e.g., preferences, capacities) are generated in the same manner as described in Section 4.1. In all experiments, the default values of α's are used, i.e., uniformly distributed in [–0.2, 0.2]. Figs. 10, 11, 12, and 13 respectively illustrate the evolution of the capacitated networks of clusters associated with TP (20, 8), TP (40, 18), TP (60, 25), and TP (80, 30), under S0 and S1. Note that the EA is executed once, simultaneously under S0 and S1 and on the same problem setting, for each of the instances shown in Figs. 10–13. The gaps represent the differences between the fitness values obtained from S0 and S1 over time. The following conclusions are drawn based on the experimental results:

• In most cases, association/dissociation of an element to/from set I decreases/increases the fitness value (Figs. 10–13, part (a)). Set J shows an opposite behavior (Figs. 10–13, part (b)). The reason lies in the capacity limitations of J's, which may prevent some I's from being matched to their more preferable element in set J. Hence, associating an additional element to set I makes the capacity limits even more restrict, while association of a new element to set J provides additional capacities and more possibilities, and thus alleviates such limitations. The same interpretation can also be valid for the dissociation of individuals.

• In spite of the above analyses, there are some cases with completely opposite behaviors, where, for example, dissociation of an element from set I decreases the overall fitness value (see, e.g., Fig. 11a, Iteration \~250). Such behaviors may be due to the interdependencies between preferences, rather than the capacity limits. For instance, dissociation of an element from set I with high positive α values (i.e., an element with highly positive influences on the preferences of the others) can considerably diminish the overall fitness value.

• The “noisy” and “suboptimal” behavior of S0 is due to disregarding IP (Recall that the main assumption is that there are interdependencies between the preferences). That is, under S0, the clusters evolve without considering the actual values of the α's $( i . e . , \alpha _ { i i ^ { \prime } } = 0 , \forall i , i ^ { \prime } \in I )$ . Nev-<sup>¼</sup>ertheless, the values shown in Figs. 10–13 are the “actual” fitness values of the “erroneously evolved” networks of clusters (considering the actual values of α's). As shown in Figs. 10–13, disregarding such interdependencies also leads to sub-optimal evolutions, where the gap between the fitness values of the sub-optimal and optimal configurations is almost proportional to the size of the problem (see also Fig. 9).

• The developed heuristics for generating the modified chromosome and the EA for generating the initial population effectively handle the evolutionary behaviors in terms of association or dissociation. As shown in Figs. 10–13, the first generations of chromosomes (i.e., iterations) generated after each single change provide acceptable fitness values. Besides, the EA enables the clusters as well as the entire network to adapt, recover, and return to the optimal/near optimal state in a timely efficient manner, after a considerably small number of iterations. The computational efficiency of the developed algorithms is investigated in the next section.

![](/api/attachments/XMPBT7CT/fulltext/images/8aee0634c6d021aca28b3f57b3a763100d5e94970f8e18bd3c33dbdf9c4a92f6.jpg)

![](/api/attachments/XMPBT7CT/fulltext/images/38b1cab5fc132636a7dc499b524b9a94a9663b577362fd31fe273e18c22d3659.jpg)  
Fig. 10. Evolution of capacitated clusters under S0 and S1 through Association (A) and Dissociation (D) of (a) I's and (b) J's; TP (20, 8).

![](/api/attachments/XMPBT7CT/fulltext/images/1152540ab29e8b6176d28bf822eca8ebaee4d460fadc6e2964f4ff448d7785a0.jpg)

![](/api/attachments/XMPBT7CT/fulltext/images/2b8d9b886142c58928ec830bd9262dae6f2aaa9e79d8e11b7061bce93322a776.jpg)  
Fig. 11. Evolution of capacitated clusters under S0 and S1 through Association (A) and Dissociation (D) of (a) I's and (b) J's; TP (40, 18)

## 5.4. Computational efficiency

This section analyzes the scalability of the developed algorithms in terms of variations in the computational time for different combinations of |I| and |J| values. Since the experiments are based on randomly generated parameters, the time required for collecting and cleaning input data is not included in the overall computational time. In some reallife applications, however, the data may be incomplete, fuzzy, or subjective, and the parameter values may need to be defined based on expert knowledge. For example, the actual gains or losses of an enterprise from joining, remaining in, or leaving a coalition is a function of various factors and dynamics such as market behavior, lifecycle of products, and political interactions with certain collaborators/competitors, and their calculation require compilation of various qualitative data such as surveys, interviews, and expert judgements into quantifiable preference scores. In such cases, however, the time required for preparing the input parameters grows polynomially with the problem size. That is, considering T(|I|, |J|) as the time required to prepare the input parameters for BMP-IP between two sets I and J, it can be shown that $T ( \left. I \right. , \left. J \right. ) =$ $O ( | I | ^ { 2 } + | I | \times | J | )$ , which is clearly polynomial in $I \times J .$ In experiments on actual data, the data must be cleaned in a way that provides the following necessary and sufficient data-points to the models: mutual preferences; influences of individuals on each other’s preferences; capacities of clusters.

(a)

Fig. 14 shows the growth rate of the computational time of the GA as a function of different values of |I| and |J|. The experiments are performed by changing the value of |I| for different values of |J|, and the recorded times represent the time laps from starting to run the algorithm until the stopping criterion is reached (see Section 3.5). The values represent the (approximate) average running time of the GA program in MATLAB on an Intel® Core™ i7 processor. The obtained experimental curves indicate a polynomial growth in the computational time, which implies feasibility of solving large-sized instances using the developed algorithms. The computational efficiency of the GA represents that of the EA, since the EA uses the same mechanism except for the mitosislike duplication and reproduction of the modified chromosome for generating the first population (see Section 4.2).

## 6. Conclusions and future research directions

In this work, the “PRISM taxonomy of the BMP” is introduced, as a taxonomic framework for formalizing BMP. The BMP-IP is defined and analyzed, as a new instance of generalized BMP where the mutual influences on and interdependencies between preferences are incorporated as determinant decisional factors. A new QAP formulation is developed to mathematically formulate the BMP-IP. A set of evolutionary algorithms is developed to effectively handle the complexity of the problem with relatively polynomial growth in the computational time as a function of problem size (see Fig. 14), and enable self-adaptation and selfevolution of networked capacitated clusters. It is shown through several experiments that IP along with capacity limits dramatically influence generalized best matching decisions—the gaps between the fitness values of S0 and S1 in optimal cluster formation (see Fig. 8), association/dissociation of individuals and clusters (see Figs. 10–13) are \~5– 15%, \~7–11%, and \~15–26%, respectively.

![](/api/attachments/XMPBT7CT/fulltext/images/aa2fa67db8069f3f8d8d26ebb38e7ca63a4ac8d9c2d04b49b1b05c11d46dc5f6.jpg)

![](/api/attachments/XMPBT7CT/fulltext/images/73100a0495ae90e7972f115181ed1fe9e688868bb1655748b181ad15706166ad.jpg)  
Fig. 12. Evolution of capacitated clusters under S0 and S1 through Association (A) and Dissociation (D) of (a) I's and (b) J's; TP (60, 25)

![](/api/attachments/XMPBT7CT/fulltext/images/62c666307ffeb052f3126c9838a484e401a0e235be8d7068f398bc3735344e79.jpg)

![](/api/attachments/XMPBT7CT/fulltext/images/5503f0cdb2492d855178b021dc0a3fc1db0719d53a22a0badcc4ba529ffacfd3.jpg)  
Fig. 13. Evolution of capacitated clusters under S0 and S1 through Association (A) and Dissociation (D) of (a) I's and (b) J's; TP (80, 30)

The observations of this work indicate that, given interdependencies among preferences, the developed methodology substantially improves the performance of any networked system with analogous features and structures—from homogenous teams of humans (e.g., pilots; soldiers; students; workers; technicians; doctors; interns; roommates) to heterogeneous teams of humans and/or machines, with applications in production, manufacturing, supply, logistics, healthcare, and transportation. The main idea is that IP, driven by interpersonal emotions among humans, technical/technological specifications and affinity attributes of machines/components, or both, is an influential and inevitable characteristic of any generalized BMP.

The aim of this work is primarily to introduce the notion of IP to BMP, formalize basic definitions and formulations at a relatively high level of abstraction, and solve the newly defined BMP-IP through efficient algorithms. It is natural that application of the developed concepts in specific domains requires further elaborations from various standpoints. Some potential directions for future research on this topic are summarized below.

1) Group- vs. self-orientation. In this work, it is assumed that the entire network of individuals and clusters are incented to collaborate. That is, all elements are group-oriented, seeking a set of common objectives that are necessarily in line with their local objectives. In some cases, however, the individuals may be self-oriented and their individual goals may contradict the common goal of the network. In such cases, the network is prone to conflicts and instability, and the developed methodology requires further modifications in order to be able to provide acceptable solutions to the BMP-IP.

2) Variable preferences and perceptions. In this work, the preferences are modeled as functions of the mutual influences of individuals on each other’s preferences, where each pair of individuals is assumed to have invariable (positive or negative) perceptions about each other. This, however, may not be true in many cases where two individuals may change their perceptions about each other after a period or dynamically. This issue increases the complexity of the BMP-IP and requires major modifications in the developed definitions, formulations, and methodology.

3) Multidimensional BMP. In this work, the basic instance of generalized BMP (i.e., 2-dimensional, many-to-one) is considered along with simplistic assumptions (e.g., equal capacity requirements of I's) for the sake of simplicity in definitions and formulations. In a similar manner, the methodology can be extended to more comprehensive and realistic instances of the BMP-IP.

4) Social networks and emotion. An important trait that differentiates networks of humans (social networks) from other types of networks is emotion. In this work, IP is formulated as a linear (increasing, altruism; decreasing, envy) function of the mutual influences of individuals on each other’s preferences. In social networks, however, such influences may not be easily quantifiable and may have nonlinear relationship with IP, due to the complexity and dynamicity of humans’ emotion in their mutual communications and interactions. Hence, the notion of IP in social networks is worthy of multidisciplinary investigation that incorporates both experimental and quan titative research.

## Acknowledgment

Research reported in this article has been developed at the PRISM (Production, Robotics, and Integration Software for Manufacturing and Management) Center at Purdue University with NSF, Indiana 21st Century Fund for Science & Technology, and industry support.

![](/api/attachments/XMPBT7CT/fulltext/images/b1069807e157b254fd34caa6a96df10c0b4c007082b9637961f1de29f7fca63a.jpg)  
Fig. 14. The experimental (approximate) curve of the polynomial growth of the GA’s computational time as a function of |I| and |J|.

[42] E.-G. Talbi, O. Roux, C. Fonlupt, D. Robillard, Parallel ant colonies for the quadratic assignment problem, Future Generation Computer Systems 17 (4) (2001) 441–449.

## References

[1] D.G. Cattrysse, L.N. Van Wassenhove, A survey of algorithms for the generalized assignment problem, European Journal of Operational Research 60 (3) (1992) 260-272.

[2] D.W. Pentico, Assignment problems: a golden anniversary survey, European Journal of Operational Research 176 (2) (2007) 774–793.

[3] T. Öncan, A survey of the generalized assignment problem and its applications, INFOR 45 (3) (2007) 123–141.

[4] R. Burkard, P. Dell-Amico, S. Martello, Assignment Problems, SIAM, 2009, ISBN 978- 1-611972-22-1.

[5] I.H. Osman, N. Christofides, Capacitated clustering problems by hybrid simulated annealing and Tabu search, International Transactions in Operational Research 1 (3) (1994) 317–336.

[6] W. Gaertner, A dynamic model of interdependent consumer behavior, Zeitschrift für Nationalökonomie 34 (3-4) (1974) 327–344.

[7] R.A. Pollak, Interdependent preferences, American Economic Review 66 (3) (1976) 309–320.

[8] N. Tomes, Income distribution, happiness, and satisfaction: a direct test of the interdependent preferences model, Journal of Economic Psychology 7 (4) (1986) 425–446.

[9] A. Postlewaite, The social basis of interdependent preferences, European Economic Review 42 (3-5) (1998) 779–800.

[10] L. Koçkesen, E.A. Ok, Evolution of interdependent preferences in aggregative games, Games and Economic Behavior 31 (2) (2000) 303–310.

[11] A.M. Bell, Locally interdependent preferences in a general equilibrium environment, Journal of Economic Behavior & Organization 47 (3) (2002) 309–333.

[12] J. Sobel, Interdependent preferences and reciprocity, Journal of Economic Literature 43 (2) (2005) 392–436.

[13] A. Cabrales, A. Calvó-Armengol, Interdependent preferences and segregating equilibria, Journal of Economic Theory 139 (1) (2008) 99–113.

[14] S. Yang, G.M. Allenby, Modeling interdependent consumer preferences, Journal of Marketing Research 40 (3)(2003) 282–294.

[15] S. Risse, Two-stage group rent-seeking with negatively interdependent preferences, Public Choice 147 (3-4) (2011) 259–276.

[16] J. Jamison, Games with synergistic preferences, Games 3 (1) (2012) 41–55.

[17] D. Lee, A.D. Stajkovic, B. Cho, Interpersonal trust and emotion as antecedents of cooperation: Evidence from Korea, Journal of Applied Social Psychology 41 (7) (2011) 1603–1631.

[18] P.P. Morita, C.M. Burns, Trust tokens in team development, Team Performance Management 20 (1) (2014) 39–64.

[19] G. Yilmaz, J. Peña, The influence of social categories and interpersonal behaviors on future intentions and attitudes to form subgroups in virtual teams, Communication Research 41 (3) (2014) 333–352.

[20] T. Manning, G. Pogson, Z. Morrison, Interpersonal influence in the workplace – Part one: An introduction to concepts and a theoretical model, Industrial and Commercial Training 40 (2) (2008) 87–94.

[21] M. Niculescu, C.R. Payne, V. Krishnan, One-to-one and one-to-many business relationship marketing: toward a theoretical framework, Journal of Business-to Business Marketing 20 (2) (2013) 51–64.

[22] K.B. Cox, The effects of unit morale and interpersonal relations on conflict in the nursing unit, Journal of Advanced Nursing 35 (1) (2001) 17–25.

[23] A. Romanowski, P. Wozniak, T. Jaworski, P. Fiderek, J. Kucharski, Modelling interpersonal relations in surgical teams with fuzzy logic, Lecture Notes in Computer Science 7629 LNAI (1) (2013) 469–479.

[24] L. Lingard, R. Reznick, I. DeVito, S. Espin, Forming professional identities on the health care team: Discursive constructions of the 'other' in the operating room, Medical Education 36 (8) (2002) 728–734.

[25] F.Y.Y. Ling, P.Q. Tran, Effects of interpersonal relations on public sector construction contracts in Vietnam, Construction Management and Economics 30 (12) (2012) 1087-1101.

[26] M. Moghaddam, S.Y. Nof, Combined demand and capacity sharing with best matching decisions in enterprise collaboration, International Journal of Production Economics 148 (2014) 93–109.

[27] M. Moghaddam, S.Y. Nof, Real-time administration of tool sharing by best matching to enhance assembly lines balanceability and flexibility, Mechatronics (2014), http://dx.doi.org/10.1016/i.mechatronics.2014.10.001

[28] M. Moghaddam, S.Y. Nof, Location-allocation decisions in collaborative networks of service enterprises Proceedings of the Industrial and Systems Engineering Research Conference Canada 2014

[29] S. Sahni, T. Gonzalez, P-complete approximation problems, Journal of the ACM 23 (3) (1976) 555–565.

[30] A.L. Barabási, R. Albert, Emergence of scaling in random networks, Science 286 (5439) (1999) 509–512.

[31] S.Y. Nof, Collaborative control theory for e-Work, e-Production, and e-Service, Annual Reviews in Control 31 (2) (2007) 281–292.

[32] H.W. Kuhn, The Hungarian method for the assignment problem, Naval Research Logistics Quarterly 2 (1-2) (1955) 83–97.

[33] J.D. Velásquez, S.Y. Nof, A best-matching protocol for collaborative e-Work and e-Manufacturing, International Journal of Computer Integrated Manufacturing 21 (8) (2008) 943–956.

[34] C. Avery, C. Jolls, R.A. Posner, A.E. Roth, The new market for federal judicial law clerks, University of Chicago Law Review 74 (2) (2007) 447–486.

[35] A.E. Roth, Deferred acceptance algorithms, history, theory, practice, and open questions, International Journal of Games Theory 36 (3-4) (2008) 537–569.

[36] F. Dong, S.G. Akl, Scheduling algorithms for grid computing, state of the art and open problems, Technical Report No. 2006-504. , School of Computing, Queen’s University, Kingston, Ontario, 2006.

[37] D. Gale, L.S. Shapley, College admission and stability of marriage, The American Mathematical Monthly 69 (1) (1962) 9–15.

[38] T.C. Koopmans, M. Beckman, Assignment problems and the location of economic activities, Econometric 25 (1) (1957) 53–76.

[39] E.D. Taillard, Comparison of iterative searches for the quadratic assignment problem, Location Science 3 (2) (1995) 87–105.

[40] L.M. Gambardella, E.D. Taillard, M. Dorigo, Ant colonies for the quadratic assignment problem, Journal of the Operational Research Society 50 (2) (1999) 167–176.

[41] V. Maniezzo, A. Colorni, The ant system applied to the quadratic assignment problem, IEEE Transactions on Knowledge and Data Engineering 11 (5) (1999) 769–778.

[43] R.K. Ahujaa, J.B. Orlinb, A. Tiwaric, A greedy genetic algorithm for the quadratic assignment problem, Computers & Operations Research 27 (10) (2000) 917–934.

[44] Z. Drezner, A new genetic algorithm for the quadratic assignment problem, IN-FORMS Journal on Computing 15 (3) (2003) 320–330.

[45] Z. Drezner, Extensive experiments with hybrid genetic algorithms for the solution of the quadratic assignment problem, Computers & Operations Research 35 (3) (2008) 717–736.

[46] F. Glover, Genetic algorithms and scatter search: unsuspected potential, Statistical Computing 4 (2) (1994) 131–140.

Mohsen Moghaddam is a PhD candidate at the School of Industrial Engineering, and a Senior Researcher at the PRISM Center, Purdue University. His research interests are in the areas of collaborative control theory, e-Work and e-Service design, best-matching, bioinspired design and control, theory of emergent networks, and decision support systems. Mohsen has published near 30 articles in peer-reviewed international journals, and is the coauthor of “Revolutionizing Collaboration through e-Work, e-Business, & e-Service”, Springer ACES Series, Automation, Collaboration, & e-Service, 2015. He has worked on various industry projects including enterprise resource planning and information management, supplier portfolio selection and risk management, distribution network design and analysis for resilience, and design of commercial decision support.

Shimon Y. Nof, Ph.D. D.H.C., is Professor of Industrial Engineering, Purdue University, and held visiting positions at MIT and at universities in Chile, EU, Hong Kong, Israel, Japan, Mexico, Philippines, and Taiwan. He is the Director of the NSF- and industry-supported PRISM Center (Production, Robotics and Integration Software for Manufacturing & Management) linked with PGRN (PRISM Global Research Network); former Chair of the IFAC Coordinating Committee "Manufacturing & Logistics Systems"; recent President, Secretary General, and current Board member of IFPR (International Federation of Production Research), Fellow of IFPR and of the IIE (Institute of Industrial Engineers), and inaugural member of Purdue’s Book of Great Teachers. He is co-inventor of three automation patents; the co-author and editor of fourteen books, including the Handbook of Industrial Robotics 1st and 2nd editions, the International Encyclopedia of Robotics, (both winners of the "Most Outstanding Book in Science and Engineering" Award,) Industrial Assembly, Springer Handbook of Automation, and Revolutionizing Collaboration Through e-Work, e-Business, and e-Service (2015).
