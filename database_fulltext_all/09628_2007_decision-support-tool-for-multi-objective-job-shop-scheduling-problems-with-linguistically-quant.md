---
otero_id: 9628
otero_key: "QUYYYKYK"
title: "Decision support tool for multi-objective job shop scheduling problems with linguistically quantified decision functions"
authors: "Dobrila Petrovic; Alejandra Duenas; Sanja Petrovic"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support tool for multi-objective job shop scheduling problems with linguistically quantified decision functions

Dobrila Petrovic <sup>a,⁎</sup>, Alejandra Duenas <sup>a</sup>, Sanja Petrovic b

<sup>a</sup> Control Theory and Applications Centre (CTAC), Faculty of Engineering and Computing, Coventry University, Coventry, United Kingdom <sup>b</sup> Automated Scheduling, Optimisation and Planning Research Group (ASAP), School of Computer Science and IT, University of Nottingham, Nottingham, United Kingdom

Accepted 9 June 2006 Available online 24 July 2006

## Abstract

This paper presents a new tool for multi-objective job shop scheduling problems. The tool encompasses an interactive fuzzy multi-objective genetic algorithm (GA) which considers aspiration levels set by the decision maker (DM) for all the objectives. The GA's decision (fitness) function is defined as a measure of truth of a linguistically quantified statement, imprecisely specified by the DM using linguistic quantifiers such as most, few, etc., that refer to acceptable distances between the achieved objective values and the aspiration levels. The linguistic quantifiers are modelled using fuzzy sets. The developed tool is used to analyse and solve a real-world problem defined in collaboration with a pottery company. The tool provides a valuable support in performing various what-if analyses, for example, how changes of batch sizes, aspiration levels, linguistic quantifiers and the measure of acceptable distances affect the final schedule.

Keywords: Job shop scheduling; Fuzzy sets; Linguistic quantifiers; Multi-objective optimisation; Genetic algorithms

## 1. Introduction

Scheduling problems have a vital role in most manufacturing and production systems. They concern allocation of scarce resources to tasks over a period of time [17]. These problems are generally defined as decision-making problems with the aim of optimising one or more scheduling criteria. The diversity of scheduling problems, large-scale dimensions and their dynamic nature make scheduling problems computationally very complex and difficult to solve.

A job shop scheduling problem is described by a number of jobs to be processed on a number of machines, each job consisting of a set of operations to be processed in a predetermined order. The aim of the job shop scheduling problem is to find the best sequence of operations on each machine in order to minimise or maximise a specific objective or a set of objectives. This problem is NP-complete; hence, various heuristic approaches have been developed to solve it. Local search methods such as simulated annealing [1,21], tabu search [18], genetic algorithms (GA) [16,22,26] and hybrid GAs [11] have been successfully applied to job shop problems yielding good results.

Although most scheduling investigations have been focused on single objective scheduling problems, in practice, most often these problems are multi-objective. Hoogeveen [14] presented a survey of multi-criteria scheduling problems where the most common scheduling performance criteria were identified. The author surveyed different approaches to solving single machine, parallel machine, job shop and open shop bi-criteria scheduling problems. Recently, a number of approaches have been proposed to solving multi-objective job shop scheduling problems [19]. For example, Itoh et al. [15] proposed a twofold look-ahead search to solve a bicriteria job shop scheduling problem. Fonseca and Fleming [8] developed a generic multi-objective genetic optimiser that presents a set of points to the DM for evaluation in each generation of the GA. After the assessment is made, the DM communicates his or her preferences to the GA, and the GA proceeds with the next generation. Brandimarte and Maiocco [6] solved a bi-criteria job shop scheduling problem by developing suitable neighbourhood structures. Esquivel et al. [7] studied the influence of different evolutionary algorithm's parameter combinations and chromosome representations in diverse multi-objective optimisation problems including the multi-objective job shop problem. Baykasoglu et al. [4] developed a multi-objective tabu search combined with a Giffler and Thompson's priority rule-based heuristic to solve a flexible job shop problem. Gorczyca et al. [12] proposed a new approach to multi-objective job shop scheduling problems in the presence of limited resources, based on priority dispatching rules with two objectives, namely minimisation of makespan and minimisation of resource consumption. They developed a multi-objective genetic algorithm based on a two-component chromosome that represented weights associated with the priority dispatching rules and proportions of resources allocated to operations. Bagchi [3] discussed multi-objective GAs-based approaches to a variety of scheduling problems.

In order to solve multi-objective problems considering imprecise nature of DM's judgements, optimisation techniques have been combined with concepts of fuzzy sets theory. Bellman and Zadeh [5] introduced a framework for solving both single and multi-objective optimisation problems in fuzzy environments. They defined a single decision function that aggregates degrees of satisfaction achieved with respect to both fuzzy objectives and fuzzy constraints. In this context, operator minimum has been most often used as an aggregation operator [27].

This paper presents a new approach to solving multi-objective job shop scheduling problems taking into consideration the DM preferences. They are expressed using aspiration levels where the aspiration levels represent “attainment levels of the objectives which the DM personally desires to achieve” [10]. The GA's fitness function is defined as a measure of truth of a linguistically quantified statement expressed in terms of distances between the achieved objective values and the corresponding aspiration levels, such as ‘many distances are acceptable’, ‘most distances are acceptable’ and so on. An algebraic method is used to evaluate the degree of truth of the linguistically quantified statement. The new approach is applied to a real life job shop scheduling problem identified in collaboration with a manufacturing pottery company.

The paper is organised as follows. A multi-objective job shop scheduling problem is defined in Section 2. In Section 3, the new multi-objective GA for the multiobjective job shop problem is described including the GA's fitness function, the job shop problem representation scheme and the GA's operators. Additionally, Section 4 introduces a real-world scheduling problem and analysis of results obtained by using the multiobjective GA. Main conclusions and directions for future work are presented in Section 5.

## 2. Multi-objective job shop scheduling problem

A problem of K jobs, $J _ { k } , k { = } 1 , { \ldots } K ,$ , to be scheduled on M machines $M _ { m } , m { = } 1 , { \ldots } M ,$ is considered, where each job consists of a specific set of operations that have to be processed in a predetermined sequence. The number of operations of job $J _ { k }$ is denoted by $\mathbf { n o } _ { k }$ and $O _ { k , m }$ denotes the operation of job $J _ { k }$ that has to be processed on machine $m .$ Each operation $O _ { k , m }$ has a fixed processing time $p _ { k , m } .$ . It is assumed that each machine can process at most one operation at a time. A job is processed on a machine only once and it is not necessarily processed on every machine. In order to consider that each job is processed on all the machines, additional dummy operations with processing times equal to zero are defined. It is also assumed that there are no preemptions.

The problem is to find a schedule of jobs taking into consideration N objectives to be optimised where a vector of the scheduling objectives is defined as $Z =$ $[ z _ { 1 } , . . . , z _ { n } , . . . , z _ { N } ]$

## 3. Multi-objective genetic algorithm

A new GA for solving the multi-objective job shop scheduling problem outlined in the previous section is developed. Its main characteristic is that it allows consideration of the DM's preferences defined through aspiration levels, i.e., objective values that the DM desires to achieve. Moreover, the advantage of considering aspiration levels is that it allows an interaction between the DM and the GA whereby the aspiration levels can be modified every time the GA is performed, as illustrated in Fig. 1.

A GA is a search algorithm, inspired by natural selection and genetics [2], that uses a population of possible solutions (candidate solutions) instead of a single solution. The candidate solutions are usually represented as strings (chromosomes) and they are evaluated by an objective (fitness) function. Search is iterative, where better solutions are generated in each iteration. Generally, a GA has three operators that are applied to generate new solutions: (1) reproduction, which is used to select solutions to be copied to the next generation, where solutions with higher fitness function values have more probability of being selected; (2) crossover, which is used to combine (mate) the reproduced solutions randomly, where each pair of strings swaps their characters (genes), starting from a position in the strings that is randomly selected; and (3) mutation, which is used to alter one or more genes. Crossover and mutation operators are usually employed with pre-determined probabilities (called crossover and mutation rates, respectively).

## 3.1. Definition of the fitness function

Since a multi-objective problem is considered, the fitness function has to take into consideration all the objectives. In practice, instead of using rigid quantitative terms, the DM may find convenient to define the fitness function using natural language expressions, i.e., linguistic terms. In this paper, the fitness function is defined based on a Yager's method for aggregation of multi-objectives into a unique decision function using linguistically quantified statements such as ‘a solution satisfies many objectives’, ‘a solution satisfies most objectives’, etc. [23]. Generally, having a class of objects, a linguistic quantifier enables defining statements about properties of the class which have the following form: “Q Y's are $F ^ { \prime } { } _ { ; }$ , where Q is a linguistic quantifier, for instance, ‘most’, ‘few’, ‘about half’, ‘at least one’, ‘all’, etc., Y is a class of objects and F is a property associated with the objects. Yager developed an algebraic approach to determining the truth of such quantified statements.

Linguistically quantified statements are used in this research to define the fitness function, taking into consideration the distances between the aspiration levels set by the DM and objective values achieved by each of the GA's candidate solutions as follows.

The following set and vectors are defined:

a set of candidate solutions $X { = } \{ x _ { 1 } , . . . , x _ { \nu } , . . . , x _ { V } \}$ where ${ \boldsymbol { x } } _ { \nu } { \in } X , \nu { = } 1 , . . . , V$ is a candidate solution and V is the GA's population size,

– a vector of aspirations levels ${ \mathrm { A L } } = [ { \mathrm { A L } } _ { 1 } , . . . , { \mathrm { A L } } _ { n } , . . . ,$ $\mathrm { A L } _ { N } ]$ where N is the number of objectives to be optimised, and

– a vector of distances ${ \Delta } _ { x _ { \nu } } = [ { \Delta } _ { x _ { \nu } , 1 } , ~ { \Delta } _ { x _ { \nu } , n } , ~ . . . , ~ { \Delta } _ { x _ { \nu } , N } ] ,$ where $\Delta _ { x , n }$ is the distance between the aspiration level $\mathrm { A L } _ { n }$ and the value of objective $z _ { n }$ achieved by candidate solution $x _ { \nu }$

In the case when objective $z _ { n } , n { = } 1 , . . . , N ,$ has to be minimised, the distance $\Delta _ { x _ { \imath } , n } , \nu { = } 1 , . . . , V , n { = } 1 , . . . , N ,$ is defined as a normalised measure, $\Delta _ { x _ { \imath } , n } \in [ 0 , 1 ] ,$ , relative to the corresponding aspiration level $\mathrm { A L } _ { n } ,$ where $\Delta _ { x _ { v } n } = 0$ means that the achieved objective value is fully satisfactory with respect to the aspiration level, while $\Delta _ { x _ { * } , n } { = } 1$ means that the achieved value is completely not satisfactory with respect to the aspiration level:

$$
\Delta_ {x _ {v}, n} = \left\{ \begin{array}{l l} 0 & \text { if } \mathrm{AL} _ {n} \geq z _ {x _ {v}, n} \\ 1 - \frac {\mathrm{AL} _ {n}}{z _ {x _ {v} , n}} & \text { if } \mathrm{AL} _ {n} <   z _ {x _ {v}, n} \end{array} \right.\tag{1}
$$

where $\Delta _ { { x } _ { v } n }$ represents the value of objective n achieved by candidate solution $x _ { \nu }$ Similarly, the distance $\Delta _ { x _ { v } n }$ can be defined for an objective n of the maximisation type.

![](/api/attachments/QUYYYKYK/fulltext/images/d72d0b3e372c092c405cc54a82207a3b5db1617bf830e5c02646ddd7c26d07de.jpg)  
Fig. 1. Genetic optimiser with aspiration levels

The algorithm allows the DM to define an acceptable distance between the objective value and the aspiration level imprecisely. The acceptable distance is modelled by a fuzzy set A. The corresponding membership function $\mu _ { A }$ is determined subjectively and it represents degrees to which the achieved objective value $\Delta _ { x , n }$ satisfies the DM with respect to its distance from the aspiration level $\mathrm { A L } _ { n } .$ For example, the fuzzy set A may be defined as follows (see Fig. 2):

$$
\mu_ {A} (\Delta_ {x _ {v}, n}) = \left\{ \begin{array}{l l} 1 - \Delta_ {x _ {v}, n} & 0 <   \Delta_ {x _ {v}, n} \leq 0. 5 \\ 0 & 0. 5 <   \Delta_ {x _ {v}, n} \leq 1 \end{array} \right.\tag{2}
$$

In this case, the DM is fully satisfied when the achieved normalised distance from the aspiration level is 0; the degree of DM's satisfaction linearly decreases while the distance increases to 0.5 and the DM is fully unsatisfied with the distances greater than 0.5.

The fitness function D is defined as a measure of truth of a linguistically quantified statement such as ‘most distances between the achieved objective values and the aspiration levels are acceptable’, or ‘few distances between the achieved objective values and the aspiration levels are acceptable’, etc. Formally, the statement is represented as:

$$
^ \prime Q \Delta_ {x _ {v}} ^ {\prime} \text { s   are } A ^ {\prime}\tag{3}
$$

where $\mathcal { Q }$ is a linguistic quantifier, $\Delta _ { x _ { \nu } }$ is the vector of distances obtained for a candidate solution $x _ { \nu }$ and $A$ is a fuzzy set that represents an acceptable distance. Therefore, the fitness function $D \colon X { \longrightarrow } [ 0 , 1 ]$ is defined where $D ( x _ { \nu } )$ represents the degree of truth of the statement $\mathbf { \hat { \mathcal { Q } } _ { \lambda _ { x _ { \nu } } } } \mathbf { \hat { s } }$ are $A ^ { \prime }$ , i.e.

$$
D (X _ {v}) = \text { Truth } [ ^ {\prime} Q \Delta_ {x _ {v}} \text { 's   are } A ^ {\prime} ]\tag{4}
$$

Yager [23] proposed two approaches to evaluate the truth of linguistically quantified statements, an algebraic approach and substitution. The substitution approach represents the meaning of the quantified statement more accurately as it considers the level of satisfaction achieved for each individual objective, while the algebraic approach considers the total amount of satisfaction achieved for all the objectives and is easier to implement. In this paper, an algebraic approach is applied to evaluate the truth of the linguistically quantified statement:

![](/api/attachments/QUYYYKYK/fulltext/images/38586f5cc6f310f3540ed1f0803c5b4ec1f404b72edd75f90593e81d76c69cd1.jpg)  
Fig. 2. Fuzzy set A that represents an acceptable distance between the objective value and the aspiration level.

$$
\text { Truth } [ ^ {\prime} Q \Delta_ {x _ {v}} \text { 's   are } A ^ {\prime} ] = \mu_ {Q} (r _ {x _ {v}})\tag{5}
$$

where $r _ { x _ { \nu } } = \frac { 1 } { N } \Sigma _ { n = 1 } ^ { N } \mu _ { A } \big ( \Delta _ { x _ { \nu } , n } \big )$ (obviously, ${ r _ { x _ { \nu } } } ^ { = 1 }$ if the <sup>¼ N ¼</sup>aspiration levels of all the objectives are fulfilled), while $\mu _ { Q }$ represents the membership function of the linguistic quantifier $Q .$ For example, if Q is the quantifier $\cdot _ { m o s t } \cdot$ , then the membership function suggested by Yager is $\mu _ { O } ( r _ { x } ) { = } \mathrm { e } ^ { - 5 0 ( r _ { x _ { \nu } } - 1 ) ^ { 2 } }$ ; if Q is ‘about half’, then $\mathsf { \Pi } _ { \mu _ { Q } } ( r _ { x _ { \nu } } ) { = } \mathrm { e } ^ { - 5 0 ( r _ { x _ { \nu } } ^ { \nu } - 0 . 5 ) ^ { 2 } } ;$ ; if Q is $f e w ^ { \ast }$ , then $\mu _ { Q }$ $( r _ { x _ { \nu } } ) { = } \mathsf { e } ^ { - 5 0 r _ { x _ { \nu } } ^ { 2 } } ;$ and so on.

Once the linguistically quantified fitness function D is defined, the schedule (candidate solution) $x _ { \nu } ^ { * } \in X$ that maximises the corresponding degree of truth is selected:

$$
x _ {\mathcal {V}} \varepsilon \left\{x _ {v} \mid D \left(x _ {\mathcal {V}}\right) = \max _ {x _ {v} \in X} D \left(x _ {v}\right) \right\}.\tag{6}
$$

## 3.2. Representation scheme and genetic operators

Apart from the fitness function, a GA's representation scheme and the genetic operators have to be defined. In the tool developed, the representation scheme and the genetic operators proposed by Yamada and Nakano [24,25] are applied as they yielded good results for job shop scheduling problems. One of the main characteristics of this representation is that there is no need for a repair mechanism that is typically needed in GAs where the corresponding strings represent schedules. A candidate solution $x _ { \nu }$ is defined as a schedule represented by an $M \times K$ solution matrix $\mathbf { S } = [ S _ { m , i } ]$ , where $S _ { m , i } { = } k$ means that the i-th operation in the sequence of operations processed on machine $M _ { m }$ belongs to job $J _ { k } .$ The starting time and the completion time of operations $O _ { k , m } , k { = } 1 , . . . , K , m { = } 1$ $\displaystyle . . . , M ,$ , are decision variables, denoted by $s _ { k , m }$ and $c _ { k , m } ,$ respectively.

The crossover operator is defined using the Giffler and Thompson algorithm (GT) [9]. Having the set of all unscheduled operations, where each operation has an earliest possible start time and an earliest possible completion time, the GT algorithm assigns available operations to machines. An available operation is the one that belongs to the set of all unscheduled operations and can start being processed. However, it is possible that more than one operation can start being processed on the same machine generating a ‘conflict set of operations’. In the GT algorithm, the choice of an operation from the conflict set is random. The crossover operator is defined based on the binary inheritance matrix H of size $M \times K$ as follows. Two parents $P _ { 0 }$ and $P _ { 1 }$ are selected from the population and $H _ { m , i } { = } 0$ states that the i-th operation on machine m is determined by parent $P _ { 0 }$ and $H _ { m , i } { = } 1$ states that the i-th operation on machine m is determined by parent $P _ { 1 }$ . The inheritance matrix H is randomly generated. It is used in a similar way to define the mutation operator.

The new GA for job shop scheduling problems is developed as follows. First, $[ V \cdot R _ { \mathrm { c } } ]$ individuals (schedules) from the initial population are randomly selected, where [·] represents the operator that rounds a floating point number to an integer, while $R _ { \mathrm { c } }$ represents the crossover rate that can take a value from (0,1]. Generally, it is recommended that $R _ { \mathrm { c } }$ value is closer to 1 than to 0. The unselected individuals are copied directly to the new population $P ^ { \prime }$ of size V. The selected individuals are paired randomly and the GT crossover is applied to each pair generating $[ V \cdot R _ { \mathrm { c } } ]$ new individuals that become members of the new population $P ^ { \prime }$ . The mutation operator is applied with a mutation rate $R _ { \mathrm { m } }$ After generating the new population $P ^ { \prime }$ , the fitness function $D ( x _ { \nu } ) , \nu { = } 1 , . . . ,$ V is calculated for each member (schedule).

The GA generates a set of solution matrices $\mathbf { \{ S = } $ $[ S _ { m , i } ] \}$ and their corresponding sets of operations starting times $\{ s ( O _ { k , m } ) \}$ and completion times $\{ c ( O _ { k , m } ) \}$

## 4. A real-life scheduling problem

The GA developed is applied to a scheduling problem of the Denby Pottery Company Ltd., UK. The company has been involved in pottery industry for almost 200 years and manufactures a wide range of ceramic tableware products. It faces a range of scheduling problems in most stages of their manufacturing processes. Kilns are the central part of the production processes. Pottery industry usually uses two types of kilns: tunnel and intermittent kilns. Tunnel kilns are continuously fired and work 24 h a day, 7 days a week, while intermittent kilns are fired once or twice a day, 5 days a week. The production plans are defined on weekly basis and the kiln's process starts every Monday morning and finishes every Friday, in the case of the intermittent kilns, and every Sunday for the tunnel kilns. Therefore, all products to be loaded into the kilns have to be ready at the beginning of the week.

In this paper, the focus is placed on the glazing process performed on the products before they are loaded into the kilns. The scheduling time horizon in the glazing section is 5 days (from Monday to Friday). The glazing section is responsible of having the products for the kilns ready before the next Monday morning and, therefore, the scheduling of the products for glazing has to be done for the whole week in advance. The glazing scheduling problem is considered as a job shop problem that consists of a flowline with eight different machines that perform various operations including: (1) rinse, (2) slip dip, (3) dip, (4) resist dip, (5) whiff 1, (6) whiff 2, (7) band and (8) trim. A batch size for each job is defined as the number of items of a specific product to be glazed. The number of jobs can vary each week depending on the production plan. It is assumed that all operations $O _ { k , m }$ for job $J _ { k }$ have the same processing time $p _ { k , m } ,$ where $p _ { k , m }$ is determined by the time $\mathrm { s m v } _ { k }$ (standard minute value) needed to produce 100 items of that specific product and the batch size ${ \mathsf { b s } } _ { k } ,$ , of the job $J _ { k }$ as follows: $\mathbf { \Delta } _ { p _ { k , m } } ^ { \mathbf { { \sigma } _ { \mathbf { { k } } , m } ^ { \mathbf { { \sigma } } } } } = \frac { \operatorname { s m v } _ { k } \times \mathbf { { b } } \mathbf { { s } } _ { k } } { 1 0 0 }$ . The number of working hours per day is 8 (480 min).

At present, the section leader builds the schedule by hand dealing with a scheduling problem of about 10 jobs per week. Although, scheduling is currently done on weekly basis jobs' due dates are introduced in the scheduling model with the idea to improve overall efficiency of the manufacturing processes of the glazing and kiln sections. The due dates are specified in days where day 1 refers to Monday, while day 5 refers to Friday. Consequently, the penalty cost incurred per day of over time is introduced and it is set to be £1.50 per item. Table 1 presents the data used. It can be seen that a job is not necessarily processed on every machine. For this reason, some dummy operations with processing times equal to zero are defined so that the machine sequence can be considered to be the same for all the jobs, namely 1-2-3-4-5-6-7-8.

The problem under consideration is to generate a schedule that meets the following three objectives.

Job shop scheduling problem data

<table><tr><td>Job k</td><td>Number of operations no $_{k}$ </td><td>Processing times per 100 items smv $_{k}$ </td><td>Batch size bs $_{k}$ </td><td>Due date  $d_{k}$ </td></tr><tr><td>1</td><td>6</td><td>79</td><td>100</td><td>3</td></tr><tr><td>2</td><td>6</td><td>63</td><td>100</td><td>2</td></tr><tr><td>3</td><td>6</td><td>87</td><td>100</td><td>2</td></tr><tr><td>4</td><td>5</td><td>79</td><td>100</td><td>3</td></tr><tr><td>5</td><td>5</td><td>79</td><td>100</td><td>1</td></tr><tr><td>6</td><td>5</td><td>123</td><td>100</td><td>3</td></tr><tr><td>7</td><td>4</td><td>123</td><td>100</td><td>2</td></tr><tr><td>8</td><td>4</td><td>79</td><td>100</td><td>4</td></tr><tr><td>9</td><td>4</td><td>103</td><td>100</td><td>4</td></tr><tr><td>10</td><td>3</td><td>123</td><td>100</td><td>5</td></tr></table>

(1) Objective $z _ { 1 }$ is to minimise the makespan $C _ { \mathrm { m a x } }$ The makespan $C _ { \mathrm { m a x } }$ is defined as the time that takes to complete all the operations:

$$
\begin{array}{l} C _ {\max} (x _ {v}) = \max \{c _ {k, m} | k = 1, \dots , K, m = 1, \dots M \} \\ x _ {v} \in X \end{array}\tag{7}
$$

where $c _ { k , m }$ is the completion time of operation $O _ { k , m } .$

(2) Objective $z _ { 2 }$ is to minimise the number of tardy jobs λ. The tardiness $T _ { k }$ of job $J _ { k }$ in schedule $x _ { \nu }$ is defined as:

$$
T _ {k} (x _ {v}) = \max _ {m = 1, \dots M} (c _ {k, m} - d _ {k}, 0), \quad x _ {v} \in X\tag{8}
$$

where $d _ { k }$ is the due date of job $J _ { k } .$ Therefore, the number of tardy jobs λ in schedule $x _ { \nu }$ is defined as:

$$
\lambda (x _ {v}) = \sum_ {k = 1} ^ {K} U _ {k} (x _ {v}), \quad x _ {v} \in X\tag{9}
$$

where $U _ { k }$ is:

$$
U _ {k} (x _ {v}) = \left\{ \begin{array}{l l} 1 & \text { if } T _ {k} (x _ {v}) > 0 \\ 0 & \text { otherwise } \end{array} \right.\tag{10}
$$

It is worth mentioning that this objective is often used in industry, since it can be easily recorded.

(3) Objective $z _ { 3 }$ is to minimise the total schedule penalty cost, PC. The schedule total penalty cost is defined as [20]:

$$
\mathrm{PC} (x _ {v}) = \sum_ {k = 1} ^ {K} \mathrm{PC} _ {k} (x _ {v}), \quad x _ {v} \in X\tag{11}
$$

where $\mathrm { P C } _ { k }$ is job $J _ { k }$ penalty cost defined as:

$$
\mathrm{PC} _ {k} (x _ {v}) = \mathrm{bs} _ {k} \times \mathrm{ot} _ {k} \times \text { penalty / day }\tag{12}
$$

where $\mathsf { b s } _ { k }$ is the batch size (required number of items of the specific product in job $J _ { k } ) , ~ \mathrm { o t } _ { k }$ is the over time required for finishing job $J _ { k } ,$

$$
\mathrm{ot} _ {k} = \left\{ \begin{array}{l l} (d r _ {k} - d _ {k}) & \text { if } d r _ {k} > d _ {k} \\ 0 & \text { otherwise } \end{array} \right.\tag{13}
$$

$d r _ { k } = \frac { ( \mathrm { { s m v } } _ { k } \times \frac { { \mathrm { b s } } _ { k } } { 1 0 0 } ) } { ( \mathrm { { t h } } \times 6 0 ) }$ is the number of days required to <sup>¼ ð </sup>produce job $J _ { k } ^ { ' } , d _ { k }$ is the due date (given in days), smv is the standard minute value to produce 100 items of the specific product of job $J _ { k }$ (given in minutes), th is the number of working hours per day, penalty/day is the cost incurred per day of over time.

Generally, these objectives are in conflict. For example, a schedule with minimum makespan does not necessarily have the minimum number of tardy jobs; or the smaller number of tardy jobs might not lead to the lower penalty cost, if the overtime required for finishing the tardy jobs is long.

The vector of aspirations levels ${ \mathrm { A L } } = [ { \mathrm { A L } } _ { 1 } , \ { \mathrm { A L } } _ { 2 } ,$ $\mathrm { A L } _ { 3 } ]$ is determined in collaboration with the DM and has the following initial values: $\mathrm { A L } _ { 1 } { = } 2 4 0 0$ , i.e., all the jobs should be completed by the end of Friday and that is why the desired makespan is equal to the number of minutes in 5 working days; $\mathrm { A L } _ { 2 } { = } 3$ , that is the acceptable number of tardy jobs; ${ \mathrm { A L } } _ { 3 } { = } 4 3 2$ , that is the maximum cost that the DM is willing to expend.

The fuzzy set A that represents an acceptable distance between an achieved objective value and the corresponding aspiration level is defined as given in formula (2).

The fitness function D measures the degree of truth of the statement ‘most of the objective values achieved by a solution schedule are acceptable with respect to the set aspiration levels’.

## 4.1. Analysis of results

Three analyses are carried out: (1) to evaluate GA performance, (2) to investigate the effects of varying batch sizes and aspiration levels and (3) to examine the effect of small changes in defining fuzzy quantifiers and the fuzzy sets that represent acceptability of distances between objective values achieved and aspiration levels.

## 4.1.1. GA performance

The initial GA parameters used are: V = 300, GEN (number of generations), i.e., iterations = 100, $R _ { \mathrm { c } } { = } 0 . 8 3$ and $R _ { \mathrm { m } } = 0 . 0 1$ The batch size for all the jobs is considered to be 100 items initially. In this case, many satisfactory solutions that fully achieve the aspiration levels are generated. The objective that is used to determine whether a schedule is feasible or not is the makespan. It is taken into account that the maximum number of days to glaze all the products (i.e., to complete all the jobs) is 5 (i.e., 2400 min). Otherwise, if the jobs are not completed within 5 days it will be necessary to pay the labour extra time and it will not be possible to load the kilns. Hence, it is desirable that the makespan is as close as possible to 2400 min (5 days) and does not exceed this period. The solution that yields the minimum makespan is presented in Table 2.

Table 5  
Table 2  
Solution with minimum makespan

<table><tr><td>Machine m</td><td colspan="10">Schedule</td></tr><tr><td>1</td><td>2</td><td>10</td><td>9</td><td>5</td><td>7</td><td>6</td><td>3</td><td>4</td><td>8</td><td>1</td></tr><tr><td>2</td><td>10</td><td>2</td><td>9</td><td>5</td><td>7</td><td>6</td><td>4</td><td>8</td><td>1</td><td>3</td></tr><tr><td>3</td><td>10</td><td>2</td><td>9</td><td>5</td><td>7</td><td>6</td><td>4</td><td>8</td><td>1</td><td>3</td></tr><tr><td>4</td><td>2</td><td>9</td><td>10</td><td>5</td><td>6</td><td>4</td><td>1</td><td>3</td><td>7</td><td>8</td></tr><tr><td>5</td><td>3</td><td>9</td><td>8</td><td>4</td><td>10</td><td>7</td><td>6</td><td>5</td><td>2</td><td>1</td></tr><tr><td>6</td><td>3</td><td>9</td><td>8</td><td>10</td><td>4</td><td>7</td><td>5</td><td>2</td><td>1</td><td>6</td></tr><tr><td>7</td><td>3</td><td>8</td><td>4</td><td>9</td><td>10</td><td>2</td><td>1</td><td>6</td><td>7</td><td>5</td></tr><tr><td>8</td><td>3</td><td>8</td><td>4</td><td>9</td><td>10</td><td>2</td><td>7</td><td>6</td><td>5</td><td>1</td></tr><tr><td>Makespan $C_{\max }$ </td><td colspan="4">Number of tardy jobs $\lambda$ </td><td colspan="4">Penalty costPC</td><td colspan="2">D(x*)</td></tr><tr><td>1712</td><td colspan="4">3</td><td colspan="4">417</td><td colspan="2">1</td></tr></table>

The results in Table 2 show that the GA has generated the optimal solution where all the three aspiration levels $\mathrm { A L } _ { 1 } , \mathrm { A L } _ { 2 }$ and $\mathrm { A L } _ { 3 }$ are met fully and the fitness function $D ( x ^ { * } )$ reaches value 1.

The GA is run with different crossover and mutation rates, $R _ { \mathrm { c } }$ and $R _ { \mathrm { m } } ,$ , respectively. In order to find the appropriate crossover rate, the algorithm is performed with a fixed mutation rate $( R _ { \mathrm { m } } { = } 0 . 0 1 )$ and with different $R _ { \mathrm { c } }$ values. Table 3 shows the results found with $\mathrm { G E N } { = } 1 0 0 $

It can be seen that the number of tardy jobs λ is 1 in all cases, the smallest makespan value $( C _ { \mathrm { m a x } } { = } 1 8 0 7 )$ is obtained when $R _ { \mathrm { c } } = 0 . 6 7$ , and the smallest penalty cost PC =7 is obtained when $R _ { \mathrm { c } } = 0 . 7 5$ . Since the aspiration levels are: $\mathrm { A L } _ { 1 } { = } 2 4 0 0$ , AL =3, ${ \mathrm { A L } } _ { 3 } { = } 4 3 2$ , all the solutions found are fully satisfactory, i.e., $D ( x ^ { * } ) { = } 1$ . In this case, it is decided to consider the $R _ { \mathrm { c } }$ that yields the smallest makespan.

Table 4 presents the results obtained when $\mathrm { A L } _ { 1 } =$ 2400, $\mathrm { A L } _ { 2 } { = } 3$ , AL =432, R =0.67, GEN= 100 and $R _ { \mathrm { m } }$ takes different values. It can be seen that the value of $R _ { \mathrm { m } }$ that yields the best solution with respect to all three objectives is 0.2. Therefore, the parameters of the GA to be considered are $R _ { \mathrm { c } } { = } 0 . 6 7 , ~ R _ { \mathrm { m } } { = } 0 . 2$ and $\mathrm { G E N } { = } 1 0 0$

Table 3  
Solutions generated with different R , $R _ { \mathrm { m } } { = } 0 . 0 1$ and GEN=100

<table><tr><td> $R_c$ </td><td>Makespan  $C_{\text{max}}$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D(x^*)$ </td></tr><tr><td>0.9</td><td>1951</td><td>1</td><td>106</td><td>1</td></tr><tr><td>0.83</td><td>1879</td><td>1</td><td>102</td><td>1</td></tr><tr><td>0.75</td><td>1930</td><td>1</td><td>7</td><td>1</td></tr><tr><td>0.67</td><td>1807</td><td>1</td><td>74</td><td>1</td></tr><tr><td>0.5</td><td>1938</td><td>1</td><td>53</td><td>1</td></tr></table>

Table 4  
Solutions generated with different $R _ { \mathrm { m } } , R _ { \mathrm { c } } { = } 0 . 6 7$ and GEN=100

<table><tr><td> $R_{\text{m}}$ </td><td>Makespan $C_{\text{max}}$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D(x^{*})$ </td></tr><tr><td>0.01</td><td>1826</td><td>1</td><td>100</td><td>1</td></tr><tr><td>0.05</td><td>1930</td><td>1</td><td>146</td><td>1</td></tr><tr><td>0.1</td><td>1907</td><td>1</td><td>199</td><td>1</td></tr><tr><td>0.2</td><td>1885</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0.25</td><td>1751</td><td>1</td><td>279</td><td>1</td></tr><tr><td>0.3</td><td>1846</td><td>2</td><td>114</td><td>1</td></tr></table>

## 4.1.2. Analysis of batch sizes and aspiration levels

The jobs to be scheduled and the jobs' batch sizes are determined on weekly basis by the production planning department and they can vary from week to week. Analysing the results obtained with batch sizes of 100 products for all jobs leads to the conclusion that the makespans, $C _ { \mathrm { m a x } } .$ , achieved are below 2400 min (5 days). For instance, the solution presented in Table 2 has a $C _ { \mathrm { m a x } }$ equal to 1712 min, which means that all the jobs can be completed in 3.5 days, approximately. This means that the batch sizes can be increased. Table 5 shows different batch sizes for the jobs, determined in such a way as to observe their impact on the makespan. In batch size 2 and batch size 3, the batch sizes are uniformly increased, while, in batch size 4, the batch sizes of the jobs that have high processing times are decreased and vice versa.

An elitist strategy is added to the GA in such a way so that the best solution found by the GA every 10 generations is kept in the population and stored. The GA parameters considered are $R _ { \mathrm { c } } { = } 0 . 6 7 , R _ { \mathrm { m } } { = } 0 . 2$ and GEN = 100. At the end, the DM is given a list of all 10 best solutions and can select the one that reflects his or her preferences the best.

The results using batch size 2 (Table 6) show that the 10 best solutions do not meet the makespan aspiration level $( \mathrm { A L } _ { 1 } { = } 2 4 0 0 )$ and consequently no fully satisfactory solutions where $D ( x ^ { * } ) = 1$ are found. In this situation, the DM can select either one of these solutions or can change the aspiration levels. For instance, if the DM decides to modify the number of tardy jobs $\mathrm { A L } _ { 2 }$ from 3 to 5, one solution that yields $D ( x ^ { * } ) = 1$ is found (solution number 6).

Different batch sizes

<table><tr><td rowspan="2">Batch size</td><td colspan="10"> $J_k$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td>2</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td></tr><tr><td>3</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td></tr><tr><td>4</td><td>100</td><td>100</td><td>50</td><td>200</td><td>100</td><td>50</td><td>100</td><td>400</td><td>100</td><td>300</td></tr></table>

Table 6  
Results obtained using different batch sizes and different aspiration levels

<table><tr><td rowspan="2" colspan="2">Solution number</td><td colspan="4"> ${\mathrm{{AL}}}_{1} = {2400},{\mathrm{{AL}}}_{2} = 3,{\mathrm{{AL}}}_{3} = {432}$ </td><td colspan="4"> ${\mathrm{{AL}}}_{1} = {2400},{\mathrm{{AL}}}_{2} = 5,{\mathrm{{AL}}}_{3} = {432}$ </td><td colspan="4"> ${\mathrm{{AL}}}_{1} = {2400},{\mathrm{{AL}}}_{2} = 7,{\mathrm{{AL}}}_{3} = {600}$ </td></tr><tr><td>Makespan  ${C}_{\max }$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D\left( {x^{ * }}\right)$ </td><td>Makespan  ${C}_{\max }$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D\left( {x^{ * }}\right)$ </td><td>Makespan  ${C}_{\max }$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D\left( {x^{ * }}\right)$ </td></tr><tr><td rowspan="10">Batch size 2</td><td>1</td><td>2641</td><td>3</td><td>54</td><td>0.955</td><td>2440</td><td>5</td><td>60</td><td>0.999</td><td>2507</td><td>7</td><td>329</td><td>0.990</td></tr><tr><td>2</td><td>2653</td><td>3</td><td>79</td><td>0.951</td><td>2639</td><td>5</td><td>314</td><td>0.955</td><td>2489</td><td>7</td><td>273</td><td>0.993</td></tr><tr><td>3</td><td>2649</td><td>2</td><td>54</td><td>0.950</td><td>2539</td><td>5</td><td>289</td><td>0.983</td><td>2420</td><td>6</td><td>320</td><td>0.999</td></tr><tr><td>4</td><td>2659</td><td>2</td><td>41</td><td>0.949</td><td>2659</td><td>2</td><td>41</td><td>0.949</td><td>2415</td><td>5</td><td>274</td><td>≈1</td></tr><tr><td>5</td><td>2520</td><td>2</td><td>53</td><td>0.987</td><td>2520</td><td>2</td><td>53</td><td>0.987</td><td>2443</td><td>3</td><td>62</td><td>0.992</td></tr><tr><td>6</td><td>2690</td><td>3</td><td>31</td><td>0.937</td><td>2353</td><td>5</td><td>211</td><td>1</td><td>2530</td><td>5</td><td>194</td><td>0.985</td></tr><tr><td>7</td><td>2519</td><td>2</td><td>28</td><td>0.988</td><td>2517</td><td>5</td><td>273</td><td>0.988</td><td>2408</td><td>6</td><td>284</td><td>≈1</td></tr><tr><td>8</td><td>2572</td><td>2</td><td>56</td><td>0.975</td><td>2572</td><td>5</td><td>226</td><td>0.975</td><td>2476</td><td>7</td><td>302</td><td>0.995</td></tr><tr><td>9</td><td>2657</td><td>3</td><td>55</td><td>0.949</td><td>2607</td><td>3</td><td>39</td><td>0.966</td><td>2398</td><td>5</td><td>194</td><td>1</td></tr><tr><td>10</td><td>2607</td><td>3</td><td>39</td><td>0.966</td><td>2443</td><td>5</td><td>253</td><td>0.998</td><td>2576</td><td>7</td><td>300</td><td>0.974</td></tr><tr><td rowspan="10">Batch size 3</td><td>1</td><td>3942</td><td>4</td><td>520</td><td>0.026</td><td>3821</td><td>4</td><td>491</td><td>0.260</td><td>3765</td><td>4</td><td>561</td><td>0.482</td></tr><tr><td>2</td><td>4393</td><td>4</td><td>426</td><td>0.064</td><td>4280</td><td>3</td><td>402</td><td>0.342</td><td>3524</td><td>5</td><td>598</td><td>0.568</td></tr><tr><td>3</td><td>3594</td><td>4</td><td>562</td><td>0.025</td><td>4212</td><td>3</td><td>468</td><td>0.240</td><td>3444</td><td>4</td><td>572</td><td>0.600</td></tr><tr><td>4</td><td>4075</td><td>2</td><td>311</td><td>0.391</td><td>4987</td><td>3</td><td>442</td><td>0.327</td><td>3574</td><td>4</td><td>543</td><td>0.549</td></tr><tr><td>5</td><td>4277</td><td>3</td><td>290</td><td>0.343</td><td>4472</td><td>5</td><td>442</td><td>0.271</td><td>3619</td><td>5</td><td>551</td><td>0.532</td></tr><tr><td>6</td><td>4619</td><td>2</td><td>400</td><td>0.277</td><td>3619</td><td>5</td><td>551</td><td>0.183</td><td>3363</td><td>4</td><td>593</td><td>0.634</td></tr><tr><td>7</td><td>3662</td><td>3</td><td>468</td><td>0.374</td><td>3769</td><td>5</td><td>436</td><td>0.462</td><td>3535</td><td>4</td><td>583</td><td>0.564</td></tr><tr><td>8</td><td>3576</td><td>4</td><td>384</td><td>0.155</td><td>3855</td><td>3</td><td>337</td><td>0.453</td><td>3421</td><td>5</td><td>580</td><td>0.610</td></tr><tr><td>9</td><td>4237</td><td>3</td><td>460</td><td>0.258</td><td>4075</td><td>2</td><td>310</td><td>0.391</td><td>3482</td><td>5</td><td>583</td><td>0.585</td></tr><tr><td>10</td><td>3987</td><td>5</td><td>361</td><td>0.029</td><td>3482</td><td>4</td><td>402</td><td>0.585</td><td>3619</td><td>4</td><td>520</td><td>0.532</td></tr><tr><td rowspan="10">Batch size 4</td><td>1</td><td>2829</td><td>3</td><td>216</td><td>0.880</td><td>2827</td><td>2</td><td>106</td><td>0.881</td><td>2703</td><td>7</td><td>280</td><td>0.933</td></tr><tr><td>2</td><td>2827</td><td>2</td><td>421</td><td>0.881</td><td>2589</td><td>4</td><td>205</td><td>0.971</td><td>2589</td><td>4</td><td>82</td><td>0.971</td></tr><tr><td>3</td><td>2977</td><td>2</td><td>223</td><td>0.812</td><td>2909</td><td>4</td><td>203</td><td>0.844</td><td>2616</td><td>7</td><td>406</td><td>0.963</td></tr><tr><td>4</td><td>2782</td><td>2</td><td>159</td><td>0.901</td><td>2857</td><td>4</td><td>219</td><td>0.867</td><td>2709</td><td>7</td><td>481</td><td>0.930</td></tr><tr><td>5</td><td>2687</td><td>3</td><td>328</td><td>0.939</td><td>2776</td><td>4</td><td>249</td><td>0.903</td><td>2451</td><td>7</td><td>289</td><td>0.998</td></tr><tr><td>6</td><td>2857</td><td>2</td><td>209</td><td>0.867</td><td>2754</td><td>4</td><td>263</td><td>0.912</td><td>2507</td><td>7</td><td>493</td><td>0.990</td></tr><tr><td>7</td><td>2742</td><td>3</td><td>533</td><td>0.917</td><td>2494</td><td>3</td><td>197</td><td>0.992</td><td>2474</td><td>5</td><td>234</td><td>0.995</td></tr><tr><td>8</td><td>2874</td><td>3</td><td>272</td><td>0.860</td><td>2795</td><td>2</td><td>129</td><td>0.895</td><td>2494</td><td>6</td><td>276</td><td>0.992</td></tr><tr><td>9</td><td>2746</td><td>1</td><td>71</td><td>0.916</td><td>2780</td><td>5</td><td>323</td><td>0.901</td><td>2441</td><td>6</td><td>281</td><td>0.991</td></tr><tr><td>10</td><td>2972</td><td>3</td><td>346</td><td>0.814</td><td>2652</td><td>3</td><td>150</td><td>0.951</td><td>2392</td><td>7</td><td>436</td><td>1</td></tr></table>

Fully satisfactory solution

Moreover, in order to allow the DM to analyse the impact of different aspiration levels on the $\mathrm { G A } ^ { \prime } \mathbf { s }$ performance and the solutions' quality, it is decided to run the algorithm again with the following aspiration levels: ${ \mathrm { A L } } _ { 1 } { = } 2 4 0 0 , { \mathrm { ~ A L } } _ { 2 } { = } 7$ and $\mathrm { A L } _ { 3 } { = } 6 0 0$ (Table 6). In this case, all the aspiration levels are met in solution number 9. Therefore, it is concluded that the aspiration levels can be met satisfactorily and the DM's preferences can be fully achieved, i.e., $D ( x ^ { * } ) = 1$

When the batch sizes for all jobs are considered to be 200 items (batch size 3), the values of the three objectives considerably increase and the GA yields a decision function $D ( x ^ { * } )$ with a mean of 0.194 (Table 7). Comparing makespan's mean in batch size 3 (4036) with the aspiration level of 2400, an underachievement of 68% is recorded. Based on these results, it can be concluded that batch size 3 is not suitable with respect to the capacity of this production system.

However, when batch size 4 is applied, the makespan $C _ { \mathrm { m a x } }$ decreases. In Table 6, it can be seen that in the case when the aspiration levers are $\mathrm { A L } _ { 1 } { = } 2 4 0 0 , \mathrm { A L } _ { 2 } { = } 7$ and $\mathrm { A L } _ { 3 } { = } 6 0 0$ the GA finds a fully satisfactory solution, D $( x ^ { * } ) { = } 1$ (solution 10), with a makespan $C _ { \mathrm { m a x } } { = } 2 3 9 2 , 7$ tardy jobs and a penalty cost of 436. Analysing the means of the makespan $C _ { \mathrm { m a x } }$ achieved for the three sets of aspiration levels (Table 7), it can be concluded that the mean makespan decreases when the aspiration level for the number of tardy jobs increases. In this case, the DM can specify whether he or she prefers the makespan objective to be met regardless the increment of the number of tardy jobs and the penalty cost. This analysis shows that the aspiration levels play a very important role on the good performance of the fuzzy multiobjective GA developed.

Table 7  
Mean values of the objectives obtained using different batch sizes and different aspiration levels

<table><tr><td rowspan="2"></td><td colspan="4"> $\text{AL}_1=2400, \text{AL}_2=3, \text{AL}_3=432$ </td><td colspan="4"> $\text{AL}_1=2400, \text{AL}_2=5, \text{AL}_3=432$ </td><td colspan="4"> $\text{AL}_1=2400, \text{AL}_2=7, \text{AL}_3=600$ </td></tr><tr><td>Makespan  $C_{\text{max}}$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D(x^*)$ </td><td>Makespan  $C_{\text{max}}$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D(x^*)$ </td><td>Makespan  $C_{\text{max}}$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D(x^*)$ </td></tr><tr><td>Batch size 2</td><td>2617</td><td>2.5</td><td>49</td><td>0.961</td><td>2529</td><td>4.2</td><td>176</td><td>0.980</td><td>2466</td><td>5.8</td><td>253</td><td>0.993</td></tr><tr><td>Batch size 3</td><td>4036</td><td>3.4</td><td>418</td><td>0.194</td><td>4057</td><td>3.7</td><td>428</td><td>0.351</td><td>3535</td><td>4.4</td><td>568</td><td>0.566</td></tr><tr><td>Batch size 4</td><td>2829</td><td>2.4</td><td>278</td><td>0.879</td><td>2743</td><td>3.5</td><td>204</td><td>0.912</td><td>2538</td><td>6.3</td><td>326</td><td>0.976</td></tr></table>

It is worth noting that a careful analysis has to be carried out in order to examine the effects of the aspiration levels and batch sizes on the solutions. For example, when high batch sizes are set (batch size 3), none of the aspiration levels are achieved and the decision function values are close to 0, in all the three cases with different aspiration levels. Consequently, it can be concluded that the batch sizes are too high and a satisfactory solution cannot be obtained by changing the aspiration levels.

In order to determine the effect of the aspiration levels on the GA performance, the one-way ANOVA [13] is applied to the results obtained by running the GA with three different aspiration level sets and batch size 2 (see Table 6) with the significant level equal to 0.05. The null hypothesis is defined as ‘the values of the decision function are independent of the aspiration levels’, while the alternative hypothesis is ‘the effectiveness of the decision function is dependent of the aspiration levels’. The results show that the null hypothesis is not acceptable; therefore, the aspiration levels do affect the GA's performance.

## 4.1.3. Effects of changing fuzzy quantifiers and the fuzzy set that represents distance acceptability

Sensitivity analysis is carried out to investigate the effects of changes in the membership functions of the fuzzy quantifiers used to define the decision function. For example, the fuzzy quantifier ‘most’ is defined as $\mu _ { \cdot \mathrm { m o s t } } , ( r _ { x _ { \nu } } ) { = } \mathrm { e } ^ { - 5 0 ( r _ { x \nu } - 1 ) \bar { 2 } }$ , i.e., using the exponential function with factor −50. The factor is changed to −30 and −70. Previous analysis shows that batch size 2 yields feasible solutions when the aspiration levels are ${ \mathrm { A L } } _ { 1 } { = } 2 4 0 0 , { \mathrm { A L } } _ { 2 } { = } 5$ and ${ \mathrm { A L } } _ { 3 } { = } 4 3 2$ (see Table 6), and, therefore, it is decided to use these aspiration levels. The results obtained with different factors of the exponential function are presented in Table 8. It can be seen that in the case when the factor is −30 the GA finds two fully satisfactory solutions with $D ( x * ) = 1$ (solutions 5 and 10) and a nearly satisfactory solution D(x<sup>⁎</sup>) = 0.999 (solution 6). Analysing the mean values it can be seen that, in terms of the decision function, the best values are obtained when the factor is −30, although the best values for the makespan are obtained when the factor is −50.

Results obtained using different exponential function factors

<table><tr><td rowspan="2"> $\mathrm{AL}_{1} = 2400,$  $\mathrm{AL}_{2} = 5,$  $\mathrm{AL}_{3} = 432$ </td><td rowspan="2">Solution number</td><td colspan="4"> $\mu_{\text{most}}(r_{x_v}) = e^{-50(r_{x_v}-1)^2}$ </td><td colspan="4"> $\mu_{\text{most}}(r_{x_v}) = e^{-30(r_{x_v}-1)^2}$ </td><td colspan="4"> $\mu_{\text{most}}(r_{x_v}) = e^{-70(r_{x_v}-1)^2}$ </td></tr><tr><td>Makespan  $C_{\text{max}}$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D(x^*)$ </td><td>Makespan  $C_{\text{max}}$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D(x^*)$ </td><td>Makespan  $C_{\text{max}}$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D(x^*)$ </td></tr><tr><td rowspan="11">Batch size 2</td><td>1</td><td>2440</td><td>5</td><td>60</td><td>0.999</td><td>2703</td><td>5</td><td>307</td><td>0.959</td><td>2627</td><td>2</td><td>56</td><td>0.944</td></tr><tr><td>2</td><td>2639</td><td>5</td><td>314</td><td>0.955</td><td>2626</td><td>4</td><td>69</td><td>0.976</td><td>2596</td><td>3</td><td>12</td><td>0.957</td></tr><tr><td>3</td><td>2539</td><td>5</td><td>289</td><td>0.983</td><td>2592</td><td>3</td><td>35</td><td>0.982</td><td>2637</td><td>4</td><td>155</td><td>0.939</td></tr><tr><td>4</td><td>2659</td><td>2</td><td>41</td><td>0.949</td><td>2541</td><td>3</td><td>55</td><td>0.990</td><td>2415</td><td>5</td><td>274</td><td> $\approx 1$ </td></tr><tr><td>5</td><td>2520</td><td>2</td><td>53</td><td>0.987</td><td>2415</td><td>5</td><td>274</td><td> $\approx 1$ </td><td>2634</td><td>5</td><td>317</td><td>0.940</td></tr><tr><td>6</td><td>2353</td><td>5</td><td>211</td><td>1</td><td>2443</td><td>3</td><td>62</td><td>0.999</td><td>2495</td><td>5</td><td>254</td><td>0.989</td></tr><tr><td>7</td><td>2517</td><td>5</td><td>273</td><td>0.988</td><td>2530</td><td>5</td><td>194</td><td>0.991</td><td>2713</td><td>5</td><td>312</td><td>0.902</td></tr><tr><td>8</td><td>2572</td><td>5</td><td>226</td><td>0.975</td><td>2659</td><td>2</td><td>41</td><td>0.969</td><td>2575</td><td>2</td><td>47</td><td>0.965</td></tr><tr><td>9</td><td>2607</td><td>3</td><td>39</td><td>0.966</td><td>2575</td><td>2</td><td>47</td><td>0.985</td><td>2778</td><td>5</td><td>293</td><td>0.866</td></tr><tr><td>10</td><td>2443</td><td>5</td><td>253</td><td>0.998</td><td>2398</td><td>5</td><td>194</td><td>1</td><td>2440</td><td>5</td><td>60</td><td>0.998</td></tr><tr><td>Mean</td><td>2529</td><td>4.2</td><td>176</td><td>0.980</td><td>2548</td><td>3.7</td><td>128</td><td>0.985</td><td>2591</td><td>4.1</td><td>178</td><td>0.950</td></tr></table>

In order to determine the effects of the changes in the definition of the quantifier ‘most’ on the GA performance, the one-way ANOVA is used again. The null hypothesis is defined as ‘the solutions of the GA are independent of the changes in the quantifier definition’ and the alternative hypothesis is ‘the solutions of the GA are dependent of the changes in the quantifier definition’. The results of the ANOVA test show that the null hypothesis is not acceptable, i.e., the definition of the quantifier ‘most’ significantly affects the GA's performance in statistical terms.

Additionally, the effects of changing the membership function of the fuzzy set A that represents an acceptable normalised distance between an objective value and the corresponding aspiration level are examined. Three cases are defined when the acceptance limit is 0.5, 0.7 and 0.3, respectively (see formula (2)). Again, the aspiration levels $\mathrm { A L } _ { 1 } { = } 2 4 0 0$ ${ \mathrm { A L } } _ { 2 } { = } 5$ and ${ \mathrm { A L } } _ { 3 } { = } 4 3 2$ and batch size 2 are used. Results obtained are given in Table 9. The best mean value of the decision function is obtained when the acceptance limit is 0.5 and the worst mean value when the limit is 0.3.

In order to determine whether the effect of the changes in the membership function of the fuzzy set A is statistically significant for the GA performance, the oneway ANOVA is used. The null hypothesis is defined as ‘the solutions of the GA are not sensitive to small changes in the fuzzy set that represents acceptable distance’ and the alternative hypothesis is ‘the solutions of the GA are sensitive to small changes in the fuzzy set that represents acceptable distance’. The results obtained show that the null hypothesis is acceptable.

This conclusion is in a certain way expected, because in the case of batch size 2 the normalised distances between the objective values and their corresponding aspiration levels are very similar to each other (very close to 0); consequently, the degrees of acceptability of the achieved distances between the objective values and the aspiration levels are very similar to each other (very close to 1).

## 5. Conclusion

A new decision support tool for analysing and solving multi-objective job shop scheduling problems that combines GAs and fuzzy sets is developed and implemented. It is an interactive tool that allows the DM to set aspiration levels and modify them sequentially. The objectives considered are incommensurable, i.e., given in different units of measure with different scales. The objectives are handled simultaneously by introducing the normalised distance between the achieved objective values and the aspiration levels. The GA's fitness function is defined as a measure of truth of a linguistically quantified statement, specified in terms of the normalised distances between the achieved objective values and the aspiration levels. The algebraic method is used to evaluate the degree of truth of the linguistically quantified statement.

A real-world job shop scheduling problem defined in collaboration with a pottery company has been analysed and solved using the developed tool. It is shown that the tool is very flexible in different aspects and can be applied in treating real life scheduling problems. It can be applied to a problem with any number of jobs, machines and objectives to be optimised. In addition, the tool can operate with different batch sizes of the jobs and can be used to perform the what-if analysis with respect to batch sizes. It can also be used to analyse the effects of different aspiration levels on the quality of the solutions. Finally, the tool enables the DM to express preferences regarding multiple objectives using natural language expressions and linguistic qualifiers.

Results obtained using different membership functions of the fuzzy set that represent acceptable distance

<table><tr><td rowspan="2"> ${\mathrm{{AL}}}_{1} = {2400},$  ${\mathrm{{AL}}}_{2} = 5,$  ${\mathrm{{AL}}}_{3} = {432}$ </td><td rowspan="2">Solution number</td><td colspan="4">Acceptance limit 0.5</td><td colspan="4">Acceptance limit 0.7</td><td colspan="4">Acceptance limit 0.3</td></tr><tr><td>Makespan  ${C}_{\max }$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D$ (x*)</td><td>Makespan  ${C}_{\max }$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D$ (x*)</td><td>Makespan  ${C}_{\max }$ </td><td>Number of tardy jobs  $\lambda$ </td><td>Penalty cost PC</td><td> $D$ (x*)</td></tr><tr><td rowspan="11">Batch size 2</td><td>1</td><td>2440</td><td>5</td><td>60</td><td>0.999</td><td>2703</td><td>5</td><td>307</td><td>0.933</td><td>2627</td><td>2</td><td>56</td><td>0.959</td></tr><tr><td>2</td><td>2639</td><td>5</td><td>314</td><td>0.955</td><td>2626</td><td>4</td><td>68</td><td>0.960</td><td>2596</td><td>3</td><td>12</td><td>0.969</td></tr><tr><td>3</td><td>2539</td><td>5</td><td>289</td><td>0.983</td><td>2592</td><td>3</td><td>35</td><td>0.970</td><td>2637</td><td>4</td><td>155</td><td>0.956</td></tr><tr><td>4</td><td>2659</td><td>2</td><td>41</td><td>0.949</td><td>2541</td><td>3</td><td>55</td><td>0.983</td><td>2415</td><td>5</td><td>274</td><td>1</td></tr><tr><td>5</td><td>2520</td><td>2</td><td>53</td><td>0.987</td><td>2415</td><td>5</td><td>274</td><td>1</td><td>2495</td><td>5</td><td>254</td><td>0.992</td></tr><tr><td>6</td><td>2353</td><td>5</td><td>211</td><td>1</td><td>2443</td><td>3</td><td>62</td><td>0.998</td><td>2713</td><td>5</td><td>312</td><td>0.929</td></tr><tr><td>7</td><td>2517</td><td>5</td><td>273</td><td>0.988</td><td>2530</td><td>5</td><td>194</td><td>0.985</td><td>2575</td><td>2</td><td>47</td><td>0.975</td></tr><tr><td>8</td><td>2572</td><td>5</td><td>226</td><td>0.975</td><td>2659</td><td>2</td><td>41</td><td>0.949</td><td>2520</td><td>2</td><td>53</td><td>0.987</td></tr><tr><td>9</td><td>2607</td><td>3</td><td>39</td><td>0.966</td><td>2575</td><td>2</td><td>47</td><td>0.975</td><td>2778</td><td>5</td><td>293</td><td>0.902</td></tr><tr><td>10</td><td>2443</td><td>5</td><td>253</td><td>0.998</td><td>2398</td><td>5</td><td>194</td><td>1</td><td>2634</td><td>5</td><td>317</td><td>0.957</td></tr><tr><td>Mean</td><td>2529</td><td>4.2</td><td>176</td><td>0.980</td><td>2548</td><td>3.7</td><td>128</td><td>0.975</td><td>2599</td><td>3.8</td><td>177</td><td>0.963</td></tr></table>

Further work will be undertaken including:

– investigation of different linguistically quantified statements to be used in GA's fitness functions,

– development of different methods to evaluate degree of truth of the linguistically quantified statements that take into consideration the allocation of satisfaction degrees associated with the objectives, instead of the algebraic method that considers a cumulative satisfaction degree only,

– incorporation of objective weights into the GA in order to model different objective priorities,

– investigation of additional objectives that are of interest for the pottery scheduling problem under consideration, such as to maximise throughput, to minimise energy consumption, etc.

## Acknowledgements

This research was supported by Engineering and Physical Sciences Research Council (EPSRC), grant no. GR/R95326/01 and GR/R95319/01. This support is gratefully acknowledged. We also acknowledge the support of the industrial collaborator the Denby Pottery Company Ltd., UK.

## References

[1] N. Azizi, S. Zolfaghari, Adaptive temperature control for simulated annealing a comparative study, Computers & Operations Research 31 (14) (2004) 2439–2451.

[2] T. Bäck, Introduction to evolutionary algorithms, in: T. Bäck, D.B. Fogel, Z. Michalewicz (Eds.), Evolutionary Computation, vol. 1, Institute of Physics Publishing, 2000.

[3] T. Bagchi, Multiobjective Scheduling by Genetic Algorithms, Kluwer Academic Publishers, 1999.

[4] A. Baykasoglu, L. Ozbakir, A.I. Sonmez, Using multiple objective tabu search and grammars to model and solve multiobjective flexible job shop scheduling problems, Journal of Intelligent Manufacturing 15 (6) (2004) 777–785.

[5] R.E. Bellman, L.A. Zadeh, Decision-making in a fuzzy environment, Management Science 17 (4) (1970) 141–164.

[6] P. Brandimarte, M. Maiocco, Job shop scheduling with a nonregular objective: a comparison of neighbourhood structures based on a sequencing/timing decomposition, International Journal of Production Research 37 (8) (1999) 1697–1715.

[7] S.C. Esquivel, S.W. Ferrero, R.H. Gallard, Parameter settings and representations in Pareto-based optimisation for job shop scheduling, Cybernetics and Systems 33 (6) (2002) 559–578.

[8] M. Fonseca, P.J. Fleming, Genetic algorithms for multiobjective optimization: formulation, discussion and generalization, in: S. Forrest (Ed.), Proceedings of the Fifth International Conference on Genetic Algorithms, San Mateo, California, University of Illinois at Urbana-Champaign, Morgan Kaufmann Publishers, 1993, pp. 416–423.

[9] B. Giffler, G.L. Thompson, Algorithms for solving production scheduling problems, Operations Research 8 (1960) 487–503.

[10] A. Goicoechea, D.R. Hansen, L. Duckstein, Multiobjective Decision Analysis with Engineering and Business Applications, John Wiley & Sons, Inc., 1982.

[11] J.F. Gonòalves, J.J. de Magalhães Mendes, M.G.C. Resende, A hybrid genetic algorithm for the job shop scheduling problem, European Journal of Operational Research 167 (2005) 77–95.

[12] M. Gorczyca, A. Duenas, D. Petrovic, A new multi-objective genetic algorithm for job shop scheduling with limited resources, in: Z. Bubnicki, A. Grzech (Eds.), Proceedings of the XV International Conference on Systems Science, Wrocƚaw, Poland, 2004, pp. 201–210.

[13] M. Hamburg, Statistical Analysis for Decision Making, Harcourt Brace Jovanovich, Inc., 1977.

[14] H. Hoogeveen, Multicriteria scheduling, European Journal of Operational Research 167 (2005) 592–623.

[15] K. Itoh, D. Huang, T. Enkawa, Twofold look-ahead search for multi-criterion job shop scheduling, International Journal of Production Research 31 (9) (1993) 2215–2234.

[16] D.C. Mattfeld, Evolutionary Search and the Job Shop, Physica-Verlag, Heidelberg, Germany, 1996.

[17] M. Pinedo, Scheduling: Theory, Algorithms, and Systems, Prentice Hall, 2002.

[18] S.C. Ponnambalam, P. Aravindan, S.V. Rajesh, A tabu search algorithm for job shop scheduling, International Journal of Advanced Manufacturing Technology 16 (10) (2000) 765–771.

[19] S.G. Ponnambalam, V. Ramkumar, N. Jawahar, A multiobjective genetic algorithm for job shop scheduling, Production Planning and Control 12 (8) (2001) 764–774.

[20] K.S. Ravichandran, C.S.R.S. Chandra, K. Rao, R. Saravanan, The role of fuzzy and genetic algorithms in part family formation and sequence optimisation for flexible manufacturing systems, International Journal of Advanced Manufacturing Technology 19 (12) (2002) 879–888.

[21] T.Y. Wang, K.B. Wu, A revised simulated annealing algorithm for obtaining the minimum total tardiness in job shop scheduling problems, International Journal of Systems Science 31 (4) (2000) 537–542.

[22] L. Wang, D.Z. Zheng, A modified genetic algorithm for job shop scheduling, International Journal of Advanced Manufacturing Technology 20 (1) (2002) 72–76.

[23] R.R. Yager, Quantifiers in the formulation of multiple objective decision functions, Information Sciences 31 (1983) 107–139.

[24] T. Yamada, Studies on metaheuristics for jobshop and flowshop scheduling problems, Doctoral dissertation, Kyoto University, Japan, 2003.

[25] T. Yamada, R. Nakano, A genetic algorithm applicable to largescale job-shop problems, Proceedings of the Second International Conference on Parallel Problem Solving form Nature, PPSN'92, 1992, 281–290.

[26] H. Zhou, Y.C. Feng, L.M. Han, The hybrid heuristic genetic algorithm for job shop scheduling, Computers & Industrial Engineering 40 (3) (2001) 191–200.

[27] H.-J. Zimmermann, Fuzzy Set Theory—and Its Applications, Third edition. Kluwer Academic Publishers, 1996.

![](/api/attachments/QUYYYKYK/fulltext/images/c5734363c39ca6cddc48e7d6c549b3a53b1fe1c4ba11020e103f98a6ed56e9be.jpg)

Dr. Dobrila Petrovic received BSc and MSc, both in Mathematics/Computer Science, from the University of Belgrade, Yugoslavia, in 1986 and 1991, respectively, and PhD in Engineering, from the University of War wick, UK, in 1998. She is a Reader in Optimisation and Control at Faculty of Engineering and Computing, Coventry University, and a member of the Control Theory

and Applications Centre (CTAC). She has published about 20 papers in refereed scientific journals and over 60 papers in proceedings of international conferences. Her main research areas are: treating uncertainty by means of fuzzy sets in various applications including inventory, production and supply chain management and control, production scheduling, forecasting, multicriteria decision making, and biomedical computing. She has been awarded three EPSRC (Engineering and Physical Sciences Research Council, UK) research grants.

![](/api/attachments/QUYYYKYK/fulltext/images/1d933b032e8098048ff9f2433fdf67cb4b1de2f90dc0e5c08b0a0d0cc649e404.jpg)

Dr. Alejandra Duenas is a Research Fellow in the Control Theory and Applications Centre (CTAC) at Coventry University in England. She obtained her PhD from the University of Sheffield in 2003 and has been in Coventry

University since that year. Her research area is multi-criteria decision making under uncertainty with particular emphasis on production scheduling.

![](/api/attachments/QUYYYKYK/fulltext/images/27abd81ca73b192010d83c196a00ede76461d050e68e15090284aba003593b66.jpg)

Dr. Sanja Petrovic received BSc, MSc and PhD in Mathematics/Computer Science, from the University of Belgrade, Yugoslavia, in 1986, 1991 and 1997, respectively. She is a Reader in Computer Science in the School of Computer Science and IT at the University of Nottingham, and a member of the Automated Scheduling Planning and Optimisation (ASAP) Research Group. Her main area of research includes multicriteria decision analysis, casebased reasoning and modelling of uncertainties

by fuzzy sets and logic in general, and their application to scheduling problems in particular. Dr. Petrovic was awarded four grants funded by EPSRC (Engineering and Physical Sciences Research Council, UK) and acts as a co-investigator on additional 12 externally funded grants. She was a guest co-editor for a feature issue of the European Journal of Operational Research (EJOR) on “Timetabling and Rostering”, of the forthcoming special issues of the Annals of Operations Research on “Personnel Scheduling and Planning”, and of the Journal of Scheduling on “Expert Systems and Machine Learning in Scheduling”. She has published over 20 papers in international scientific journals and over 50 papers in international conference proceedings.
