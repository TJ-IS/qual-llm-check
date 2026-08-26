---
otero_id: 17672
otero_key: "6BRPM3CV"
title: "Schedule management: An object oriented approach"
authors: "Guus Wolf"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90082-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Schedule management: An object oriented approach

Guus Wolf

Eindhoven University of Technology, Eindhoven, Netherlands

In this paper we discuss the design of decision support systems, usable in several planning situations. We consider resource-constrained time-dependent scheduling problems with time as the important planning component. Instead of dealing with optimization aspects of the planning problem, we concentrate on schedule management, i.e. stepwise planning with respect to primitive functions, like handling single decisions or constraints.

The design of these systems is based on a mathematical model, giving a formal characterization of a class of scheduling problems and allowing generic descriptions of scheduling objects like processors, operations, decisions and constraints. The model is applied to various scheduling problems, like resource constrained project scheduling, car routing, the construction of time tables both for schools and for nursery in hospitals.

An object oriented implementation of the model, based on the natural hierarchy of scheduling problems, turns out to lead to a clear separation between the generic and the domain specific components of the schedule manager, minimizing redundant code and resulting in software with a high degree of maintainability.

Keywords: Decision support system; Scheduling; Object oriented design

## 1. Introduction

Most decision support systems can not be used in more than one planning situation. The software for these systems is very sensitive to change requests. A minor change in the underlying model or in the limiting conditions can make it necessary to redesign the whole system. There are hardly reusable components. The claim for a more flexible DSS-design is uttered by many authors $[2,6,10,18]$ .

The reason for this inflexibility can be found among others in the fact, that conventional DSS-systems are dominated by the algorithmic aspect. Although it is stated, that the software components of a DSS should relate to both information management and optimization $[3,6,15]$ , more attention is paid to the latter aspect, especially in the first design phase. Mostly mathematicians working in the field of operations research were involved in the software development. In spite of the mathematical relevance of algorithmic aspects, the software dealing with it plays a minor role related to other software components like the management of decisions and the user interface.

![](/api/attachments/6BRPM3CV/fulltext/images/7d26140a705e8f83eb691ec29a0701788e60e7d0525bbe9cda1a180647f8a3bf.jpg)

Guus Wolf, born in Amsterdam in 1950, studied mathematics at the ETH in Zürich, Zwitserland (1968–1973). Afterwards he worked as researcher at the department of mathematical statistics at the ETH, where he received in 1977 his Ph.D. degree in mathematics on a thesis in the field of robust statistics. Since 1980 he worked as software engineer in industry (BBC, Baden, Switzerland and Philips, Apeldoorn, the Netherlands) in areas like database management, compilers and optical filing. In addition he worked as a lecturer in computer science at the polytechnics of Enschede and Eindhoven in the Netherlands. Since 1990 he joined the department of computer science at the university of technology in Eindhoven. His research interests include decision support systems, software engineering and database management.

In view of the fact, that software maintainability is our highest objective in this paper, the following requirements can be formulated:

\- the software should contain reusable modules, that can be applied to a wider class of planning problems;

\- the software architecture should allow a clear separation between the generic components and the domain specific components of the software;

\- the software should be a platform with respect to the implementation for both generic algorithms (simulated annealing, genetic algorithms, etc.) [1] and powerful domain specific optimization procedures;

\- the software should be flexible with respect to changes in the (domain specific) model and it should be easy to add or to change constraints.

Although several attempts have been made to increase flexibility of optimization components by using general search methods applicable in a wide range of planning situations $[10]$ , we concentrate in this paper on data manipulation aspects, particularly oriented towards scheduling problems. The basic system functionality is schedule management. Primitive functions should be provided to support stepwise planning $[14]$ . The user should have among others the possibility to add (and delete) scheduling objects like “decisions” and “constraints”; the system should calculate the consequences of user actions and check feasibility. Optimization is not relevant in this context.

Scheduling is the allocation of resources over time to perform certain tasks $[5]$ . Scheduling problems can be formulated as sequencing problems with time as the important planning component. Moreover, we require that all feasibility constraints and schedule evaluation criteria can be expressed as measures of time. The class of these scheduling problems is rather extensive and does include job-shop planning, car routing, school time tables and time tables for nursery in hospitals. We will give a formal definition of this class. Although several models exist $[5,9,12]$ , which are suitable to formulate algorithms for scheduling problems, they are not flexible enough for our purposes.

Because we need the flexibility of generic models as well as the power of problem specific models, modelling on more abstraction levels is necessary. This implies a software architecture consisting of generic and domain specific modules $[18]$ . A specific schedule manager is built up by linking the generic modules with the relevant group of domain specific modules.

Because of our high requirements for software maintainability, system implementation is based on an object oriented design $[16,17]$ . The use of object oriented techniques for DSS-software has been up to now rather limited $[8,11]$ . There are however many reasons, that plead for their application:

\- the concept of encapsulation, to specify objects both by their attributes and by their methods, is a powerful mechanism to represent scheduling objects like processors, operations, decisions and constraints;

\- the concept of inheritance (and abstract datatyping), to formalize IS-A relationships between classes and subclasses, is necessary to represent the natural hierarchy of scheduling problems and scheduling objects to get a clear separation between the generic and the domain specific components;

\- polymorphism, i.e. the possibility to use object methods in different subclasses under the same name, but with specific functionalities, will enlarge the flexibility of the software.

## 2. Notations

We will follow some notational conventions. Let A and B be sets:

$[A \to B]$ : the set of functions from $A$ to $B$ ;

$A^{*}$ : the set of strings of elements from set $A$ ;

$\mathcal{P}(A)$ : the powerset of $A$ (set of all subsets of $A$ );

Let $A(i)$ and $a(i)$ be indexed sets resp. real numbers and let $P(i)$ be predicates:

$\Sigma (a(i)|P(i))$ : the sum of all $a(i)$ , for which $P(i)$ holds.

Let Time be a finite interval on the positive real axis $R_{+}$ .

$B(Time)$ : the set of unions of subintervals of Time.

$\mu (H)$ : the length of an element $H$ of $B(Time)$

(i.e. the sum of the lengths of its disjunct subintervals).

Let $A$ be an entitytype with attributes $A_1, \ldots, A_n$ , i.e. $A = A_1 \times \ldots \times A_n$ , and let $t \in A$ be an entity of that type. With $A_i(t)$ we denote the projection of $t$ to $A_i$ .

## 3. A basic general model

We restrict ourselves to resource-constrained time-dependent planning problems with the property, that schedules can be represented as Gantt charts. This problem class is very wide and includes the general jobshop problem, car routing and the construction of time tables both for schools and for nursery in hospitals.

A precise mathematical formulation of these scheduling problems and schedules is necessary. Usually this is needed to describe algorithms and their properties. However in our case it is the foundation to design data structures and object definitions properly.

Existing models for scheduling problems are either too specific with regard to constraints $[5,9,12]$ or too general to be powerful enough to characterize the time aspects of scheduling problems properly $[10,13]$ . For this reason we present in this section a basic general model to characterize our problem class; extensions and problem specific interpretations follow later. Our object definitions (see section 7) will be based on this model.

## 3.1. Scheduling problems

A class of scheduling problems can be characterized by the following tuple

$$
(P, O, D, p r, o p, S, f, g, t _ {\max}) \text { with }
$$

\- $P$ , the set of all possible processors (or resources);

\- $O$ , the set of all possible operations (or tasks) to be allocated to processors;

\- $D$ , the set of all possible decisions; we have $D = D_{+} \cup D_{0}$ , with $D_{+}$ being the set of decisions, that allocate an operation to a processor (real decisions) and $D_{0}$ being the set of decisions, that put a processor in the waiting state (idle decisions);

\- the function $pr: D \to P$ assigning the processor, involved in a decision;

\- the function $op: D_{+} \to O$ assigning the operation, involved in a real decision;

\- $S$ , the set of all possible states, that a processor can have with the function $s_0: P \to S$ assigning the initial states;

\- the function $f: D \times S \to S$ describing a state transition, being the effect of a decision with respect to a processor;

\- the function $g: D \times S \to \mathbb{R}_+$ to determine the duration, that a certain decision will be active;

\- $t_{max}$ , a positive real number, defining the scheduling interval Time = (0, $t_{max}$ ).

## 3.2. Schedules

Scheduling problems are distinguished from other planning problems by the aspect of time. All time aspects should be handled in the generic part of the system.

Let $p_i$ be a processor from a finite subset of $P$ and let $\{d_{ij}\}_{j=1,n_i}$ be a finite sequence of decisions with respect to $p_i$ . The decision $d_{i,j}$ is effectuated at the time $t_{i,j}$ and is active till $t_{i,j+1}$ , the time, that the next decision with respect to $p_i$ will be effectuated. We call $t_{i,j}$ a decision-point. Let $s_{i,j}$ be the state of processor $p_i$ after decision $d_{i,j}$ ( $j > 0$ ). Then we have the following equations

$$
s _ {i, 0} = s _ {0} (p _ {i}),
$$

$$
s _ {i, j} = f \big (s _ {i, j - 1}, d _ {i, j} \big), \quad j > 0,
$$

$$
t _ {i, 1} = 0,
$$

$$
t _ {i, j} = t _ {i, j - 1} + g \left(s _ {i, j - 2}, d _ {i, j - 1}\right), \quad j > 1.
$$

We call $s_{\mathrm{fin}}(p_i) = s_{i,n_i}$ the final state of processor $p_i$ , which is the state after the last decision.

We can define a schedule as a tuple $(P_S, O_S, F_S)$ with

\- $P_{S}$ a finite subset of $P$ ,

\- $O_{s}$ a finite subset of $O$ ,

\- a function $F_{S}: P_{S} \to D^{*}$ assigning a finite sequence of decisions to every processor of $P_{S}$ ,

$$
F _ {S}: p _ {i} \mapsto \left\{d _ {i, j} \right\} _ {j = 1, n _ {i}}, \quad p _ {i} \in P _ {S}; d _ {i, j} \in D \text { with }
$$

$$
p r \left(d _ {i, j}\right) = p _ {i}, \quad o p \left(d _ {i, j}\right) \in O _ {S} \text {or} d _ {i, j} \in D _ {0} \text {and}
$$

$$
\sum \left(g \left(d _ {i j}, s _ {i j}\right) | 0 <   j \leq n _ {i}\right) \leq t _ {\max}.
$$

As a consequence of this definition only one operation at a time can be allocated to a processor, whereas more processors can be assigned to the same operation simultaneously.

## 3.3. Constraints

Constraints are used to define the feasibility of schedules. It is important to have the flexibility to add and to change constraints dynamically. To realize this we should represent planning knowledge and especially, constraints declaratively in a domain independent way. Several ideas and concepts going in this direction, can be found in the literature $[7,11,18]$ .

Although we assume a certain homogeneity with respect to scheduling objects like resources, operations and decisions, this is not the case with constraints. On the domain specific level various subclasses (types) of constraints may be defined (deadline constraints, precedence constraints, etc.). It is therefore important to distinguish which properties are adherent to constraint classes and which to constraint instances.

We distinguish hard and weak constraints. Hard constraints should never be violated. The feasibility of a schedule with respect to hard constraints is guaranteed by the schedule manager. However a slight violation of a weak constraint is admissible, but in that case the user should be warned by signalization. With respect to weak constraints it is not the system, but the user, who is ultimately responsible for feasibility.

It is possible, that some constraint-instances of a certain type are hard, whereas other instances of the same type are weak. We mean by the hardness of a constraint-instance its property to be hard or weak.

We require, that constraint violations can be expressed by time intervals, denoting the period, when the constraint is violated or when decisions should be effectuated to undo the constraint violation. This is just a generalization of the convention to specify constraints by Boolean functions. This is done for the following reasons:

\- the time aspect of the constraint violation is more emphasized, which is rather important for scheduling problems;

\- we have a measure of infeasibility with respect to constraints, which is important for weak constraints;

\- a wide class of schedule quality measures can be formulated as simple expressions of critical regions, belonging to the same class of constraints (make span, earliness and tardiness for the job-shop problem, etc.).

Now we come to a formal definition of constraints. Let Sch be the set of all schedules with respect to a certain problem class. We define a constraint-type c by its specific domain and its evaluator, i.e. a pair $(Z_{c}, eval_{c})$ with $Z_{c}$ a set and $eval_{c}$ a (penalty) function with

$$
e v a l _ {c}: S c h \times Z _ {c} \rightarrow B (T i m e).
$$

A constraint instance of type c can be defined as a pair $(z_{c}, hd)$ with $z_{c} \in Z_{c}$ and hd, being a Boolean to specify the hardness of a constraint instance.

Evaluation of the penalty function $eval_{c}$ for a particular constraint instance and schedule will produce a subset of the scheduling interval Time to indicate the time period, when the constraint is violated or when decisions should be effectuated to undo the constraint violation. This time period, which we call the critical region, can be represented as a finite set of disjunct intervals. The critical region can be empty in the case of feasibility or contain just the whole time interval as extreme cases.

In Section 4 this definition will be illustrated by a variety of examples.

## 3.4. Quality measures

Beside constraints, that define the feasibility of schedules, there are quality measures for comparison of schedules. These criteria are often defined as penalty functions, mapping a schedule to a real value $[12]$ . It makes sense to couple quality measures to constraints or sets of constraints by measuring the extent of violation with respect to these constraints. For the most common quality measures (make span, total or weighted tardiness, etc.) corresponding constraints can be defined.

The relation between constraints and quality measures will be formalized by the following definition. A quality measure can be defined by a pair (Clist, agg) with Clist being a finite list of constraints and agg being a real (aggregate) function defined on the set of strings of real numbers

$$
a g g: \mathbb {R} ^ {*} \rightarrow \mathbb {R}.
$$

Examples of such aggregate functions are $sum(X)$ , $max(X)$ , $variance(X)$ , etc. with X a sequence of reals.

The constraint list mentioned above will contain often all constraint instances of a certain type, but this is not necessary.

Given a particular schedule a quality value q with respect to a quality measure (Clist, agg) can be calculated by applying the specified aggregate function to the list of the lengths of the critical time regions, defined by the constraint evaluation functions corresponding to the specified list of constraints. See Figure 1.

For example we can define the make span of a schedule for the job-shop problem by (virtual) deadline constraints (with deadlines equal to zero) and the aggregate function giving the maximum of a string of real numbers.

![](/api/attachments/6BRPM3CV/fulltext/images/c3093e81a148f1d3a72601f9b6115b7c36f10f0b8ba69c193c97a68266c13720.jpg)  
Fig. 1. Calculation of the quality value of a schedule.

## 3.5. Extended schedules

Let $(P, O, D, pr, op, S, f, g, t_{max})$ be a class of scheduling problems and let C be the set of all possible constraints for this class. We define an extended schedule by a tuple $(P_s, O_s, F_s, C_s, Q_s)$ with $(P_s, O_s, F_s)$ being a schedule, $C_S$ a subset of C and $Q_s$ a set of quality measures with $c \in C_S$ for every constraint instance c being involved in $Q_s$ (i.e. c an element of some Clist with (Clist, agg) ∈ $Q_s$ ).

## 3.6. Expressions

In this section we assume a fixed given schedule $(P_{s}, O_{s}, F_{s})$ . The set $D_{S}$ of decisions involved is determined by

$$
D _ {s} = \left\{d _ {i, j} \mid d _ {i, j} = \left(F _ {S} (p _ {i})\right) _ {j}, p _ {i} \in P _ {S}, 0 <   j \leq n _ {i} \right\}.
$$

We can now introduce some expressions, that are needed in the following paragraphs:

\- the start time of decision $d_{i,j}$ :

$$
\begin{array}{l} \text { start } (d _ {i, j}) = \sum (g (s _ {i, k - 1}, d _ {i, k}) | 0 <   k <   j), \quad j > 1 \\ \text { start } (d _ {i, 1}) = 0 \end{array}
$$

\- the end time of decision $d_{i,j}$ :

$$
e n d \left(d _ {i, j}\right) = \left\{ \begin{array}{l} s t a r t \left(d _ {i, j}\right) + g \left(s _ {i, j - 1}, d _ {i, j}\right) \\ s t a r t \left(d _ {i, j + 1}\right) (j <   n _ {i}) \end{array} \right.
$$

\- the activity interval of decision $d_{i,j}$ :

$$
i n t e r v a l \big (d _ {i, j} \big) = \big (s t a r t \big (d _ {i, j} \big), e n d \big (d _ {i, j} \big) \big ]
$$

\- the time period, when processor $p$ executes operation $o$ :

$$
p r - o p - s e t (p, o) = \cup \left(i n t e r v a l \left(d _ {i, j}\right) \mid p r \left(d _ {i, j}\right) = p, o p \left(d _ {i, j}\right) = o, d _ {i, j} \in D _ {S}\right)
$$

\- the executing period of operation o:

$$
o p - e x e c - s e t (o) = \bigcup (p r - o p - s e t (p _ {i}, o) \mid p _ {i} \in P _ {S})
$$

\- the start time of operation o:

$$
\text { start - op } (o) = \left\{ \begin{array}{l} \min \big (\text { start } (d _ {i, j}) | o p (d _ {i, j}) = o, d _ {i, j} \in D _ {S} \big) \\ \quad \text { if   } \text { op - exec - set } (o) \neq \emptyset \\ t _ {\max} \text { otherwise } \end{array} \right.
$$

\- the end time of operation o:

$$
e n d - o p (o) = \left\{ \begin{array}{l} \max \bigl (e n d \bigl (d _ {i, j} \bigr) | o p \bigl (d _ {i, j} \bigr) = o, d _ {i, j} \in D _ {S} \bigr) \\ \text { if } o p - e x e c - s e t (o) \neq \emptyset \\ t _ {\max} \text { otherwise } \end{array} \right.
$$

\- the finishing time of processor $p$ :

$$
e n d - p r (p) = \sum \left(g \left(d _ {i, j}, s _ {i, j - 1}\right) \mid p r \left(d _ {i, j}\right) = p, d _ {i, j} \in D _ {S}\right)
$$

\- the allocation of processor $p$ to operation $o$ at time $t$ :

$$
b u s y (p, o, t) = \left\{ \begin{array}{l l} \top & \text { if } t \in p r \text {-} o p \text {-} s e t (p, o) \\ \bot & \text { otherwise } \end{array} \right.
$$

\- the cumulative activity time of decision $d_{i,j}$ at time $t$ :

$$
d u r \left(d _ {i, j}, t\right) = \left\{ \begin{array}{l} e n d \left(d _ {i, j}\right) - s t a r t \left(d _ {i, j}\right) \text {if} t \geq e n d \left(d _ {i, j}\right) \\ t - s t a r t \left(d _ {i, j}\right) \text {if} s t a r t \left(d _ {i, j}\right) <   t <   e n d \left(d _ {i, j}\right) \\ 0 \text {otherwise} \end{array} \right.
$$

\- the cumulative allocation time of processor $p$ to operation $o$ at time $t$ :

$$
p r - o p - d u r (p, o, t) = \sum \left(d u r \left(d _ {i, j}, t\right) \mid p r \left(d _ {i, j}\right) = p, o p \left(d _ {i, j}\right) = o, d _ {i, j} \in D _ {S}\right)
$$

## 4. Domain specific interpretations of the generic model

In this section we give two domain specific interpretations of the model. The basic model may be extended with domain specific parameters. We specify attributes of the relevant entities and give specifications of the relevant functions. Constraints are defined by their specific domain and their evaluators (see section 3.3).

## 4.1. Job-shop

Problem description: We consider general job-shop scheduling with job splitting and preemption. Operations (tasks) may be allocated several times to processors (resources). An operation has a size, i.e. the total resource capacity necessary to complete the task. Processors can execute operations with different speeds. To execute operations certain abilities of processors are required. The sequence of task execution is restricted by precedence constraints. Deadline and release time constraints are related to the finishing and starting times of operations. Processors are only at certain time windows available.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Domain specific model parameters:
A - a set of abilities.

Processors:
id : identifier
abilset : set of abilities
speed : executing velocity
 $P = \mathbb{N} \times \mathcal{P}(A) \times \mathbb{R}_{+}$ 

Operations:
id : identifier
req-abilset : set of required abilities
size : processing capacity
 $O = \mathbb{N} \times \mathcal{P}(A) \times \mathbb{R}_{+}$ 

Real decisions:
pr : processor reference
op : operation reference
time : duration
 $D_{+} = P \times O \times R_{+}$ 

Idle decisions:
pr : processor reference
wait : waiting time
 $D_{0} = P \times R_{+}$
</div>

States (of a processor):

exectime: the total executing time of a processor (till a decision point)

$$
S = \mathbb {R} _ {+}
$$

Initial state (of a processor):

$$
s _ {0} (p) = 0 \forall p \in P
$$

State transition:

$$
f (s t a t e, d e c) = \left\{ \begin{array}{l} \text { exctime } (s t a t e) + \text { time } (d e c) \text { if } d e c \in D _ {+} \\ \text { exctime } (s t a t e) \text { if } d e c \in D _ {0} \end{array} \right.
$$

Duration of decision:

$$
g (s t a t e, d e c) = \left\{ \begin{array}{l} t i m e (d e c) \text {if} d e c \in D _ {+} \\ w a i t (d e c) \text {if} d e c \in D _ {0} \end{array} \right.
$$

Constraints:

\- release time constraints: $Z_{c} = O \times \mathbb{R}_{+}$

$$
e v a l _ {c} (s c h, o, r l) = \{t \in T i m e | t <   r l \} \cap o p - e x e c - s e t (o)
$$

\- deadline constraints: $Z_{c} = O \times \mathbb{R}_{+}$

$$
e v a l _ {c} (s c h, o, d l) = \{t \in T i m e | t > d l \} \cap o p - e x e c - s e t (o)
$$

\- tasks should be completed: $Z_{c} = O$

let compl(o) be the completed part of an operation:

$$
\operatorname{compl} (o) = \sum \left(p r - o p - d u r \left(p _ {i}, o, t _ {\max}\right) * s p e e d \left(p _ {i}\right) \mid p _ {i} \in P _ {S}\right)
$$

and let $\alpha = t_{max} * compl(o) / size(o)$

$$
e v a l _ {c} (s c h, o) = \left\{ \begin{array}{l} \emptyset \text {   if   } c o m p l (o) \geq s i z e (o) \\ (\alpha , t _ {\max} ] \text {   otherwise } \end{array} \right.
$$

\- avoiding superfluous task execution: $Z_{c} = O$

$$
\begin{array}{r l} \text {eval} _ {c} (s c h, o) & = \text {op - exec - set} (o) \cap \left\{t \in \text {Time} \mid \sum (p r - o p - d u r (p _ {i}, o, t) * s p e e d (p _ {i}) > s i z e (o) \mid p _ {i} \in P _ {S}) \right\} \end{array}
$$

\- required processor abilities for task execution: $Z_{c} = P \times O$

$$
e v a l _ {c} (s c h, p, o) := \left\{ \begin{array}{l} \emptyset \text {if} a b i l s e t (p) \cap r e q - a b i l s e t (o) \neq \emptyset \\ p r - o p - s e t (p, o) \text {otherwise} \end{array} \right.
$$

\- generalized precedence constraints: $Z_{c} = O \times O \times \mathbb{R}_{+}$

$$
\operatorname{eval} _ {c} \left(\text { sch }, o _ {1}, o _ {2}, \text { waiting }\right) := \left\{t \in \text { Time } \mid t <   \text { end - op } (o _ {1}) + \text { waiting } \right\}
$$

$$
\cap \left\{t \in T i m e \mid t > s t a r t - o p (o _ {2}) \right\} \quad \text { with } \quad o _ {1} \neq o _ {2}
$$

\- processor unavailability: $Z_{c} = P \times B(\text{Time})$

$$
\operatorname{eval} _ {c} (\text {   sch,   } p, \text {   period   }) := \text {   period   } \cap \left(\bigcup \left(\text {   pr - op - set   } (p, o _ {k}) \mid o _ {k} \in O _ {S}\right)\right)
$$

## 4.2. Car routing

Problem description: Cargo (operations) has to be transported by trucks (processors) from one location to another. Transport time is dependent on the distance of the locations, the speed of a truck and the loading resp. unloading time. The amount of cargo that is transported simultaneously is restricted by a maximum volume, which is truck specific. Starting points may be different. Loading or unloading is only possible in specific time windows.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Domain specific model parameters:
L - a set of locations.
dist:  $L \times L \rightarrow R_{+}$ , a distance function.
Processors:
id : car-identifier
start-loc : start location
speed : speed of the truck
maxvolume : maximal total volume
 $P = N \times L \times R_{+} \times R_{+}$ 
Operations:
id : cargo-identifier
from-loc : place of depart
to-loc : destination
load-time : time to load or to unload
volume : volume of the cargo
 $O = N \times L \times L \times R_{+} \times R_{+}$ 
Real decisions:
pr : processor reference
op : operation reference
loading : loading or unloading
 $D_{+} = P \times O \times \{\top, \bot\}$ 
Idle decisions:
pr : processor reference
wait : waiting time
 $D_{0} = P \times R_{+}$ 
States (of a processor):
loc: the location of the truck
vol: the total volume of the cargo
 $S = L \times R_{+}$ 
Initial state (of a processor):
 $s_{0}(p) = (\text{start-loc}(p), 0) \forall p \in P$ 
State transition:
 $f(\text{state}, \text{dec}) = \begin{cases} (\text{from-loc}(\text{op}(\text{dec})), \text{vol}(\text{state}) + \text{volume}(\text{op}(\text{dec}))) &amp; \text{if } \text{dec} \in D_{+}, \text{loading}(\text{dec}) = \top \\ (\text{to-loc}(\text{op}(\text{dec})), \text{vol}(\text{state}) - \text{volume}(\text{op}(\text{dec}))) &amp; \text{if } \text{dec} \in D_{+}, \text{loading}(\text{dec}) = \bot \\ \text{state if } \text{dec} \in D_{0} \end{cases}$ 
Duration of decision:
 $g(\text{state}, \text{dec}) = \begin{cases} dist(\text{loc}(\text{state}), \text{from-loc}(\text{op}(\text{dec})) * speed(\text{pr}(\text{dec})) + load-time(\text{op}(\text{dec}))) &amp; \text{if } \text{dec} \in D_{+}, \text{loading}(\text{dec}) = \top \\ dist(\text{loc}(\text{state}), \text{to-loc}(\text{op}(\text{dec})) * speed(\text{pr}(\text{dec})) + load-time(\text{op}(\text{dec}))) &amp; \text{if } \text{dec} \in D_{+}, \text{loading}(\text{dec}) = \bot \\ wait(\text{dec}) \text{ if } \text{dec} \in D_{0} \end{cases}$
</div>

Constraints:

\- an operation is executed by one processor only: $Z_{c} = \mathbf{O}$

$$
e v a l _ {c} (s c h, o) = \left\{ \begin{array}{l} o p - e x e c - s e t (o) \text {   if   } \# \{i \mid p r - o p - s e t (p _ {i}, o) \neq \emptyset \} > 1 \\ \emptyset \text {   otherwise   } \end{array} \right.
$$

\- operations should be completed: $Z_{c} = 0$

$$
e v a l _ {c} (s c h, o) = \left\{ \begin{array}{l} \emptyset \text {   if   } o p - e x e c - s e t (o) \neq \emptyset \\ (0, t _ {\max} ] \text {   otherwise } \end{array} \right.
$$

\- release time constraints: see job-shop

\- deadline constraints: see job-shop

\- loading/unloading is not allowed in certain time period: $Z_{c} = L \times B(\text{Time})$

$$
\begin{array}{c} e v a l _ {c} (  s c h,   l o c,   p e r i o d) = p e r i o d \cap \Big (\bigcup \big (e n d \big (d _ {i, j} \big) - l o a d t i m e \big (o p \big (d _ {i, j} \big) \big),   e n d \big (d _ {i, j} \big) \big ] \mid \\ d _ {i j} \in D _ {+},   \left(f r o m \text {-loc} \big (o p \big (d _ {i, j} \big) \big) = l o c\right) \\ \vee \Big (t o \text {-loc} \big (o p \big (d _ {i, j} \big) \big) = l o c \Big) \Big) \end{array}
$$

\- trucks should not be overloaded: $Z_{c} = P$

$$
e v a l _ {c} (s c h, p) = \bigcup \left(\text { interval } \left(d _ {i, j}\right) \mid d _ {i, j} \in D _ {+}, \quad p r \left(d _ {i, j}\right) = p, v o l \left(s _ {i, j}\right) > s u p v o l\right)
$$

\- trucks should return to their starting points: $Zc = P$

let $\text{returntime}(p)$ be the time necessary to return from the final location back to the starting point:

$$
\text { returntime } (p) = \text { speed } (p) * \text { dist } \left(\text { loc } \left(s _ {\text { fin }} (p)\right), \text { start - loc } (p)\right)
$$

and let $\alpha = \text{maximum}(0, t_{max} - \text{returntime}(p))$

$$
e v a l _ {c} (s c h, p) = \left\{ \begin{array}{l} \emptyset \text {   if   } l o c (s _ {f i n} (p)) = s t a r t - l o c (p) \\ [ \alpha , t _ {m a x} ] \text {   otherwise } \end{array} \right.
$$

\- two (or no) decisions are related to a processor and an operation: $Z_{c} = P \times O$

$$
e v a l _ {c} (s c h, p, o) = \left\{ \begin{array}{l} p r - o p - s e t (p, o) \text {if} \# \left\{(i, j) \mid d _ {i, j} \in D _ {+}, \quad p r \left(d _ {i, j}\right) = p, o p \left(d _ {i, j}\right) = o \right\} = 2 \\ \emptyset \text {otherwise} \end{array} \right.
$$

\- cargos should be loaded before being unloaded: $Z_{c} = P \times O$

$$
e v a l _ {c} (s c h, p, o) = \left\{ \begin{array}{l} p r - o p - s e t (p, o) \text {if} \exists i, \quad j _ {1}, j _ {2}: j _ {1} <   j _ {2}, d _ {i, j _ {1}}, d _ {i, j _ {2}} \in D _ {+}, \\ \quad p r \left(d _ {i, j _ {1}}\right) = p r \left(d _ {i, j _ {2}}\right) = p, \quad o p \left(d _ {i, j _ {1}}\right) = o p \left(d _ {i, j _ {2}}\right) = o, \\ \quad \left(l o a d i n g \left(d _ {i, j _ {1}}\right) = \bot \quad \vee l o a d i n g \left(d _ {i, j _ {2}}\right) = \top\right) \\ \emptyset \text {otherwise} \end{array} \right.
$$

## 5. System functionality and user actions

A prototype has been implemented based on our model with a primitive user interface. This system supports step-wise planning. The user can perform user actions by evoking interactively primitive functions like adding or deleting “scheduling objects” like processors, operations, decisions or constraints. The system will evaluate these user actions, compute their consequences and do some feasibility checking.

These primitive functions are grouped with respect to the relevant object classes. After the choice of the relevant class (schedule, processor, etc.) the user may evoke a function (find, insert, etc.). The system will execute that function and perform state transitions if necessary.

A transaction is a sequence of user actions followed by a commit. After a commit command all constraint instances will be evaluated resulting in a set of critical regions. Moreover quality values will be calculated for all defined quality measures. In the case that any hard constraint is violated all actions performed since the last commit are rolled back.

Grouping of user actions by means of the transaction concept is necessary, because a single user action may result in an infeasible schedule (some decisions may be effectuated at the same time involving different processors). To avoid the violation of hard constraints, possibly constraint checking should be done with respect to more than one user action.

With respect to the scheduling objects processor, operation, decision and constraint the following primitive functions are defined:

find, insert, update, delete

With the function find a specific object instance is made current within his class. Several options of this command are possible: find direct, find first, find next, find last and find previous. Direct search is always based on the object identifier. Sequential search for processors, operations and constraints is based on the order of the object identifiers; sequential search for decisions is based on the chronological order of their decision points. By means of the options find within processor, find within operation and find within constraint type the search process for decisions or constraints may be restricted.

The functions update and delete are related to scheduling objects, which are made current by previous find functions. When processors or operations are deleted, all related decisions and constraints are removed from the schedule as a side effect.

The function insert is rather obvious for processors and operations. To insert a constraint instance the relevant constraint type should be specified by the user. Before inserting a decision, first a processor, an operation and a decision should be made current by appropriate find functions. The new decision is inserted chronologically after the current decision and is related to the current processor and the current operation.

With respect to schedules we have the following primitive functions:

load, save, show, commit

With the function show the schedule will be represented on the screen. With the function load and save schedules can be loaded from or written to files, specified by the user.

By executing the function commit constraint instances will be evaluated and all previous user actions may be rolled back if any hard constraint is violated (see above).

It is important to observe, that the system can be used to manipulate decisions as well as processors, operations and constraints dynamically. The distinction between strategic, tactical and operational planning $[4]$ is less strict in this context.

## 6. Architecture and implementation

## 6.1. Architecture

The architecture of a specific DSS is defined by an hierarchy of modules. On the top level we have generic modules. In these modules the superclasses of all scheduling objects (resource, decision, constraint, etc.) including their operators are defined. Only those attributes and methods that are common for all subclasses are defined here. Also time handling, schedule evaluation and feasibility checking belong to this level.

On a lower level we have domain-specific modules, containing the definitions of all relevant sub-classes of scheduling objects, with their specific attributes and operators. For example, in the job-shop case we can distinguish various constraints, like precedence-, deadline- and release time constraints. Also problem specific optimization routines could be defined in these modules eventually.

Table 1 Reusability factors.

<table><tr><td>#c</td><td>Jobshop</td><td>Car-routing</td><td>Time-table for schools</td><td>Time-tables for nursery</td></tr><tr><td>0</td><td>0.66</td><td>0.68</td><td>0.69</td><td>0.73</td></tr><tr><td>1</td><td>0.63</td><td>0.66</td><td>0.66</td><td>0.70</td></tr><tr><td>2</td><td>0.61</td><td>0.64</td><td>0.63</td><td>0.67</td></tr><tr><td>3</td><td>0.59</td><td>0.62</td><td>0.61</td><td>0.64</td></tr><tr><td>4</td><td>0.57</td><td>0.60</td><td>0.59</td><td>-</td></tr><tr><td>5</td><td>0.55</td><td>0.58</td><td>0.57</td><td>-</td></tr><tr><td>6</td><td>0.53</td><td>0.56</td><td>-</td><td>-</td></tr><tr><td>7</td><td>0.52</td><td>0.54</td><td>-</td><td>-</td></tr><tr><td>8</td><td>0.51</td><td>-</td><td>-</td><td>-</td></tr></table>

Constraint types are defined in separate modules. This makes it possible to change and add constraint-types easily. As a consequence constraint types can be used in several planning situations.

A problem-specific DSS is generated by linking the generic modules with the relevant domain-specific modules.

Finally object-instances are supplied by the end user by means of the primitive actions, described in the last section. It is important to observe, that the manipulation of object instances by the end-user is related to decisions as well as to resources, operations and constraints.

The classification of “stakeholders” [18] involved in the development and the use of DSS in three groups (toolsmith, designer and manager) corresponds with the different levels of abstraction in the DSS-architecture: generic modules (superclasses), domain specific modules (subclasses) and object instances. Each group is on exactly one abstraction level involved in the development or the use of the system.

## 6.2. Implementation

A set of modules is implemented in $C_{++}$ resulting in decision support systems for several planning problems, like job-shop planning, car routing, the construction of time tables both for schools and for nursery in hospitals. These systems run on UNIX and have the basic functionality as described in the last section.

To have a simple measure of the reusability of a certain DSS, we take the ratio of generic software within the whole system. As module size we use the number of lines of pure source code. Table 1 shows reusability factors of systems for different planning situations, depending on the number of implemented constraints (indicated by #c). The numbers are smoothed to eliminate the influence of the order of the constraints. Furthermore we consider all modules as specific, that can be used in several but not all planning situations. Especially this applies to modules describing constraint-types. Though matters are rather simplified, the table gives a rough idea, in how far our approach can lead to software reusability and code reduction.

## 7. Object definitions

In this section we give some relevant object definitions based on our model by means of a pseudo-language. We will define both generic and domain specific object classes with respect to the job-shop problem. The definitions are simplified for the sake of clarity.

## 7.1. Object representation

To describe our objects and to write pseudocode we use in this paper a fictive pascallike object-oriented pseudolanguage. To define classes we have in this language structures called objects. Objects are comparable with records, with the difference that object-components can be both attributes and object-methods (functions or procedures):

## object figure

size: integer;

colour: colourtype;

method moveto(x, y: integer);

method draw

end;

To define subclasses we can construct hierarchies of objects. An object is denoted as descendant of an other object in a hierarchy by specifying the name of the ancestor in parentheses (after the object name); attributes and methods of the higher class are inherited:

## object triangle(figure)

If in the declaration of an object the name of a method is followed by the keyword virtual, this means that this method can be used in different subclasses under the same name, but with specific functionality (polymorphism). The semantics of such a method are not determined until run-time, when the method is invoked (dynamic binding).

We use the pseudo language structure list of to specify sequences of elements of a certain type

real\_sequence = list of real

Moreover, we assume the following type as predefined

```txt
interval = record
    left, right: real;
    end;
```

## 7.2. Generic object classes

In this section we define the generic object classes:

```vhdl
schedule = object
sch_processors : list of processor;
sch_operations : list of operation;
sch_decisions : list of decision;
sch_constraints : list of constraint;
method schedule_evaluate: boolean;
method schedule_show;
end;

scheduling_object = object
s_id: integer; (*object identifier *)
method s_insert (s: schedule); virtual;
method s_delete (s: schedule); virtual;
method s_retrieve (s: schedule); virtual;
method s_update (s: schedule); virtual;
end;
```

```vhdl
processor = object (scheduling_object)
    p_initstate: state;
end;

operation = object (scheduling_object)
end;

state = object
    state_time: real;
    method state_transition (dec: decision); virtual;
    method state_show; virtual;
end;

decision = object (scheduling_object)
    d_pr : processor;
    d_op : operation;
    d_state : state;
    d_idle : boolean;
    method d_getduration: real; virtual;
    method d_getdecisionpoint: real;
    method d_evaluate;
end;

real_decision = object (decision)
end;

idle-decision = object (decision)
end;

time-region = object
    crit_timeset = list of interval;
    method crit_length: real; (*total length*)
end;

constraint = object (scheduling object)
    c_hard : boolean;
    c_critreg : time_region;
    method c_evaluate (s: schedule); virtual;
    method c_show_critical_region;
end;

quality-measure = object (scheduling object)
    q_list : list of constraint; (*list of constraints*)
    q_value : real;
    method q_aggregate (rlist: list of real): real; virtual;
    method q_calculate_value (s: schedule);
end;
```

One of the most important methods is the function schedule \_evaluate belonging to the object-class schedule, which checks the feasibility of a schedule by evaluating all its constraints. Constraint evaluation on its turn is performed by the method c-evaluate belonging to the object-class constraint. The semantics of the latter method are not determined until run\_time, when the method is invoked and the constraint is initialized. This property is called dynamic binding and it is above all this property, which makes it possible to treat constraints so generically.

## 7.3. Domain specific object classes (job-shop)

In this subsection we define the domain specific object classes for the job-shop problem.

```txt
ability = (a1, ..., an);

rcps_processor = object (processor)
    p_abilset : set of ability;
    p_speed : real;
end;

rcps_operation = object (operation)
    o_abilset : set of ability;
    o_size : real;
end;

rcps_real_decision = object (real-decision)
    d_duration: real; (*duration of assignment*)
    method d_getduration: real; virtual;
end;

rcps_idle_decision = object (idle_decision)
    d_waiting: real; (*waiting time*)
    method d_getduration: real; virtual;
end;

rcps_state = object (state)
    busytime: real;
    method state_transition (dec: decision); virtual;
    method state_show; virtual;
end;

deadline_constraint = object (constraint)
    c_op : rcps_operation;
    c_deadline : real;
    method c_evaluate (s: schedule); virtual;
end;

precedence_constraint = object (constraint)
    c_op1, c_op2 : rcps-operation;
    c_waiting : real
    method c_evaluate (s: schedule); virtual;
end;

availability_constraint = object (constraint)
    c_pr : rcps_processor;
    c_intervals : list of interval;
    method c_evaluate (s: schedule); virtual;
end;
```

## 8. Conclusions and extensions

Although scheduling problems vary a lot with respect to their optimization aspect, they have much more in common, when we restrict ourselves to stepwise planning. When designing a decision support system in a more generic way, we should start therefore with components for pure schedule management. Algorithmic components may be implemented later in layers on top of the basic software. This may be the case both for flexible generic optimization procedures (like simulated annealing) as for powerful problem specific algorithms.

In view of the natural hierarchy of scheduling problems, an object oriented implementation seems to be suitable. It leads to a clear separation between the generic and the domain specific components of the schedule manager, minimizing redundant code and resulting in software with a high degree of maintainability and modularity.

In this paper we made a simplification by assuming only two levels of abstraction. The classification tree of scheduling problems has in fact more levels, which should reflect in the system architecture. Software modules should correspond always to a specific node in that tree. Another simplification is the assumed homogeneity of resources, operations and decisions, which may be not always realistic.

We have to emphasize again, that the optimality of schedules is not an objective in this paper. Important is the optimality of the software in the sense of maintainability, flexibility and reusability.

## References

[1] Aarts, E.H.L., A.E. Eiben, K.M. van Hee (1989), A General Theory of Genetic Algorithms, Computer Science Notes, Eindhoven University of Technology.

[2] Alter, S.L. (1980), Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley.

[3] Anthonisse, J.M., J.K. Lenstra, M.W.P. Savelsbergh (1988), Behind the Screen: DSS from an OR Point of View; Decision Support Systems 4, Elsevier Science Publishers (North-Holland).

[4] Anthony, R.N. (1965), Planning and Control Systems: A Framework for Analysis; Harvard University Press, Studies in Management Control, Cambridge Mass.

[5] Baker, K.R. (1974), Introduction to Sequencing and Scheduling, J. Wiley, New York.

[6] Bennet, J.L. (ed.) (1983), Building Decision Support Systems, Addison-Wesley.

[7] Bonczek, R.H., C.W. Holsapple, A.B. Whinston (1983), Specification of Modelling Knowledge in Decision Support Systems; Processes and Tools for Decision Support (Ed. H.G. Sol), North-Holland Publishing Company.

[8] Bots, P.W.G., A. Verbraeck (1989), Object Oriented Task Description: Concepts, Tools and Applications; paper presented at the Session on Object Oriented Approaches in Information System Design, at the 15th IFIP WG 8.1 meeting, June 7th, 1989, in Sesimbra, Portugal.

[9] Coffman, E.G. (1976), Computer and Job Shop Scheduling Theory, J. Wiley, New York.

[10] Eiben, A.E., K.M. van Hee (1990), Knowledge Representation and Search Methods for Decision Support Systems; Data, Expert Knowledge and Decisions (eds. W. Gaul, M. Schader), NATO ASI Series, Vol. F61, Springer-Verlag.

[11] Fox, M.S., S.F. Smith (1984), ISIS – a Knowledge-based System for Factory Scheduling; Expert Systems, Vol. 1, No. 1.

[12] French, S. (1982), Sequencing and Scheduling, J. Wiley, New York.

[13] Hee, K.M. v., A. Lapinski (1989), OR and AI Approaches to Decision Support Systems; Decision Support Systems Vol. 4.

[14] Jansen, A., L. Klieb, C. Noorlander, G. Wolf (1990), 'PLATE', a Decision Support System for Resource Constrained Project Scheduling Problems, Designing Decision Support Systems Notes, NFI 11.90/03, Eindhoven University of Technology.

[15] Keen, P.G.W., M.S. Scott Morton (1978), Decision Support Systems: an Organizational Perspective, Addison-Wesley.

[16] Kim, W., F.H. Lochovsky (Eds.) (1989), Object-Oriented Concepts, Databases and Applications; ACM Press, Addison-Wesley.

[17] Meyer, B. (1988), Object Oriented Software Construction, Prentice-Hall.

[18] Sprague, R.H., E.D. Carlson (1982), Building Effective Decision Support Systems, Prentice-Hall.
