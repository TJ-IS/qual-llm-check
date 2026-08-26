---
otero_id: 17076
otero_key: "BMM6G5T7"
title: "Decision support for massive personnel assignment"
authors: "Panos Constantopoulos"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90015-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support for Massive Personnel Assignment

Panos CONSTANTOPOULOS

Institute of Computer Science-FORTH, Heraklion, Crete, Greece

The design of a decision support system for assigning large numbers of personnel to jobs according to multiple criteria is presented. The system comprises the following decision modules: (a) Utility assessment, which determines feasible assignments and then applies rules on personnel data to produce a utility index for each one of those. (b) Ordinary assignment, which produces a default “optimal” assignment when no special conditions or exceptions apply. (c) Special assignment, which handles all exceptional cases and provides means for overriding the ordinary assignment procedure.

![](/api/attachments/BMM6G5T7/fulltext/images/d109c324621706a839ec9f8d9241e521dba89d4c6fdfc339423642fd7bcdc1c0.jpg)

Panos Constantopoulos is Assistant Professor of Computer Science at the University of Crete and Researcher at the Institute of Computer Science, Foundation of Research and Technology – Hellas, both in Heraklion, Crete, Greece. His main research interests are in the areas of decision support systems, office information systems and computer-aided software engineering. He has a Dipl. Eng. in Electrical and Mechanical Engineering, National Technical University of

Athens, 1978, a M.S. in Electrical Engineering, Carnegie-Mellon University, 1979, and a Sc.D. in Operations Research, MIT, 1983.

## 1. Introduction

In developing systems for supporting manpower allocation in organisations, the issues of capturing organisational complexity and the multitude of objectives and pertinent rules, providing flexibility and ensuring accessibility and usefulness to higher levels of management are of great importance $[1,2,3]$ . In fact, the decision environment in which such decision support systems are meant to operate will be rather reluctant to use them unless they deal with the above issues successfully.

The setting assumed here is a large organisation, such as the military or a public service organisation where large numbers of new personnel periodically join. This incoming population is usually diverse in terms of education, prior occupation, age, etc.. Here we disregard the case of people applying for a single post and turn our attention to those who, after joining, will be considered for assignment to a range of posts (here called “jobs”). The managers or officers responsible for this assignment are faced with the task of attaining the maximum overall benefit to the organisation within the framework of established policies and procedures and the limits imposed by the composition of the incoming population. Although the objective of attaining some sort of “optimal” assignment is clear, defining appropriate quality measures and finding the “best” assignment is not always a straightforward exercise. In fact a number of criteria for the assessment of assignment exist, some of which are systematically employed, while other are ad hoc rules with limited scope, and exceptional cases calling for special treatment often arise.

Personnel assignment is a decision of the semi-structured type [6]. The existing structure is represented as a list of assignment criteria, along with their relative importance, which can be incorporated into an objective assignment procedure. On top of this structure, subjective judgement according to ad hoc, or even unarticulated criteria, finally determines an overall “best” assignment.

Structure is revealed by systematic analysis and understanding of the objectives of the organisation and detailed job descriptions. However, depending on the organisation, there is a point beyond which the search for structure is either impossible or valueless.

A decision support system for personnel assignment aims at facilitating and enhancing the effectiveness of the invariably iterative, unstructured, judgmental part of the process by undertaking the execution of the structured procedures and providing critical as well as supplementary information. Regardless of the way in which it captures the structure of the decision process, the decision support system has to fulfill the following requirements:

(a) Provide data base management functions, furnishing all sorts of screened, yet raw information on the new personnel.

(b) Provide various predefined, or user-definable statistics of personnel data.

(c) Prepare a rational personnel assignment plan and provide the means for easily altering it, imposing restrictions and repeating the procedure.

The first two functions provide information input to the subjective decision process as well as a convenient reporting mechanism. The third one undertakes the structured part of the decision but in such a way as to never contest the authority of the user. This point is critical for the acceptance of the system in a real organisation.

In this paper we present the design of an interactive system for supporting massive personnel assignment decisions as described above, involving populations in the order of 2000–3000 people and about 100 jobs. Simplicity, flexibility, easy calibration and accommodation of ad hoc in addition to systematic criteria have been the major design goals. The system comprises the following decision modules: (a) Utility assessment, which applies rules on personnel data to produce a utility index for each possible assignment. (b) Ordinary assignment which produces a default “optimal” assignment when no special conditions or exceptions apply. (c) Special assignment, which handles all exceptional cases and provides means for overriding the ordinary assignment procedure.

The utility assessment module considers for each individual, the kind and duration of prior occupation, the associated learning effect, the education, the relative importance assignment, the rank and expected duration of the assignment, in order to determine: (1) the feasibility of each potential assignment and (2) an index, between 0 and 1, representing the utility (or value) [4] of each feasible assignment to the organisation with respect to the above criteria.

The ordinary assignment module casts the problem in the form of a Hitchcock problem.

The special assignment module may be called upon both before and after ordinary assignment. The operations of this module include enforcing or forbidding individual as well as class assignments, where classes are defined via ad hoc rules.

Underlying the entire assignment process is a graph model. Special assignment actually edits the graph, whereas utility assessment puts weights on the links and ordinary assignment solves a utility maximisation problem on the edited, directed graph.

In section 2 we outline the method of the entire personnel assignment process. In sections 3, 4 and 5 we discuss the utility assessment, the special assignment and the ordinary assignment modules respectively. Finally in section 6 we point out further work on the subject.

## 2. Modelling the Personnel Assignment Process

Personnel assignment proceeds in a sequence of steps. First must be determined which jobs each new person can be a candidate for. Then candidates for each position must be compared. One way of making this comparison is to define a priority over the set of selection criteria and then to rank the candidates for each job according to the defined, preemptive list of criteria. Some rule is also needed for resolving conflicts among jobs competing for good candidates. Another approach, taken here, is to define a quantitative measure for each feasible person-to-job assignment, based on the selection criteria, which represents the utility of the particular assignment to the organisation. The comparison of candidates can now be made on the basis of these utility indices.

Having established a basis for comparing candidates, we are in a position to make a rational assignment. Without any other considerations, the natural step is to apply the mechanism for comparison vis-a-vis the demand for each job to produce an overall “optimal” assignment. However, there may be assignments of individuals or even classes of people which must be enforced or forbidden for reasons known to the decision maker, regardless of the objective utility index. This necessity leads to a first round of special assignment, serving such special needs, followed by ordinary assignment which simply applies the routine selection procedure to the remaining candidates.

As soon as all candidates are assigned, the complete assignment is evaluated. This global check has three possible outcomes:

(a) The assignment is considered satisfactory and the process ends.

(b) It is felt that certain persons would better fit in different positions or that specific exchanges of personnel between jobs should take place. These are specific corrections which can be made by repeating the special assignment step, followed if necessary, by ordinary assignment.

(c) The assignment misses some (or all) of the goals and requirements of the organisation. In contrast with the previous case (b), this is a systematic error which calls for changes in the procedure which determines the utility of feasible assignment. Therefore, a step of model calibration is taken and the entire process is then resumed from the beginning.

The process described above is schematically shown in fig. 1. Note that the main three decision modules, i.e. utility assessment, special assignment and ordinary assignment, access two data repositories: the personnel data base and the assignment graph. The personnel data base contains the records of all the personnel, from which relevant information in drawn in order to determine the utility index of each feasible assignment as well as to make a special assignment. As soon as the assignment process ends, the job assigned to each person is entered in the personnel data base. The assignment graph, on the other hand, is an auxiliary data structure which supports the mathematical model of the assignment described below. At this point it suffices to mention that the assignment graph accepts parameter values from the system user (personnel requirements) and the utility assessment module (utility indices); it gets edited by the special assignment module; and it provides the input to the ordinary assignment module.

![](/api/attachments/BMM6G5T7/fulltext/images/5a86b67461bc826c4a1078f2a311828455684c954ec04824ba16f6508f6fff10.jpg)  
Fig. 1. Model of the Personnel Assignment Process.

The development of the decision modules is based on a network model of the assignment. Suppose that personnel and jobs are represented by the index sets

$$
I = \left\{i _ {1}, i _ {2}, \dots , i _ {m} \right\} \quad \text { and } \quad J = \left\{j _ {1}, j _ {2}, \dots , j _ {n} \right\},
$$

respectively. Also suppose that each job $j \in J$ can absorb $d_{j}$ people. This demand should be met, if possible, but need not be exceeded. Clearly,

$$
D = \sum d _ {j}
$$

persons are needed in total. It can be reasonably expected that D = m, although we need not make such an assumption here. Personnel assignment can be represented by the following network model (fig. 2): Consider a bipartite directed graph consisting of a set of origin nodes I, a set of destination node J and a set of directed arcs A. The sets I and J are the personnel and job sets respectively. Each node $i \in I$ has a supply of 1, representing the availability of one person, while each node $j \in J$ has a demand $d_{j}$ , representing the maximum staffing requirement of job j. The set A contains one arc $(i, j)$ for each feasible assign-

Personnel

Jobs

![](/api/attachments/BMM6G5T7/fulltext/images/f471b8ea6e4a287b034bfa2fe8b5a5cfdc2cd4c085d3c2c6243ddc97b3e3527f.jpg)  
Fig. 2. Network Model of Assignment.

ment of person $i$ to job $j$ . In general $A \subset I \times J$ since not all assignments are always feasible. Furthermore, with each arc $(i, j) \in A$ a utility index $a_{ij}$ is associated, representing the utility of the particular assignment to the organisation, as well as a decision variable $x_{ij}$ which takes the value 0 or 1 depending on whether the assignment $(i, j)$ is made or not.

Now the graph, here called assignment graph, represents the set of feasible assignments along with staffing requirements. The set of arcs with $x_{ij}=1$ represents the actual assignment with total utility to the organisation equal to

$$
\sum_ {(i, j) \in A} a _ {i j} x _ {i j}.
$$

Finding the “best” assignment corresponds to solving the following utility maximisation problem:

$$
\begin{array}{l} \max \sum_ {(i, j) \in A} a _ {i j} x _ {i j} \\ \sum_ {j} x _ {i j} = 1, \qquad i \in I, \\ \sum_ {i} x _ {i j} \leq d _ {j}, \qquad j \in J, \\ x _ {i j} = 0 \quad \text { or } \quad 1. \end{array}\tag{1}
$$

As we shall see in section 4, when special assignment takes place, certain nodes i (i.e. people) are dropped from consideration in problem (1) since their assignment becomes a restriction rather than a decision variable. Accordingly, some $d_{j}$ change. Therefore, the sets I, J, A and the demands $d_{j}$ are dynamically determined in the course of the iterative assignment process outlined earlier.

## 3. Utility Assessment

The purpose of the utility assignment module is to assess the value of each potential assignment through a two-stage process:

(1) Determine the feasibility of each potential assignment, i.e. construct the arc set $A$ of the assignment graph. This involves checking eligibility tables as well as possible restrictions which apply for each person $i \in I$ . The eligibility tables are boolean tables which determine the eligibility of each profession group, education group and health group for each job $j \in J$ . The composition of profession, education and health groups is discussed further below. Here it suffices to mention that the definition of these groups is fairly stable as well as the eligibility tables, reflecting general personnel assignment policies.

(2) Determine a utility index $a_{ij}$ for each feasible assignment $(i, j) \in A$ , representing the utility (or value [4]) of the assignment to the organisation. This index is a number between 0 and 1 and is determined by evaluating the corresponding assignment with respect to the following criteria:

(a) Prior occupation of the individual.

(b) Duration of this occupation and the associated learning effect.

(c) Education of the individual.

(d) Relative importance of prior occupation and education for the particular assignment.

(e) Organisational rank and expected duration of the assignment.

We regard the above to be a minimal set of non-preemptive criteria pertaining to the assignment problem. It could certainly be augmented by career path and individual preference considerations and by specifying preemptive criteria (e.g. see [3]), however at the expense of model simplicity.

## 3.1. Computing the Utility Indices

Let us now turn to the computation of the utility indices.

A general formula for the computation of the utility index is:

$$
a _ {i j} = c _ {i j} \left(\lambda_ {j} a _ {i j} ^ {0} + (1 - \lambda_ {j}) a _ {i} ^ {e}\right), \quad i \in I, j \in J,\tag{2}
$$

where $a_{ij}^{0}$ is the occupation index; $a_{i}^{e}$ is the education index; $\lambda_{j}$ is the occupation relevance; and $c_{ij}$ is the commitment index.

The occupation index, $a_{ij}^{0}$ , measures the utility of assigning person i to job j on the basis of the kind and duration of prior occupation alone. The education index, $a_{i}^{e}$ , is an index of merit for person i on the premises that education is invariably an advantage, regardless of specialisation. Nevertheless, for many jobs special training and experience are absolutely necessary, or at least very important, whereas the general level of education is a secondary consideration. Conversely, some jobs do not require high specialisation or experience, while education in general is adequate warranty that the person in question will quickly adapt to the job and learn its tricks. The relative importance of prior occupation (understood to include special training) and level of education for some assignment is captured by the occupation relevance, $\lambda_{j}$ , $0 \leq \lambda_{j} \leq 1$ , and its complementary education relevance, $1 - \lambda_{j}$ , which depend only on the job j and act as weights on the occupation and education index respectively.

Finally, the commitment index, $c_{ij}$ takes into account the expected duration as well as the organisational rank of the assignment. If person i can only be assigned to job j for a short time while the associated learning effect is long or the organisational rank high, then $c_{ij}$ acts as a discount factor on the utility of the assignment.

The utility index, $a_{ij}$ , has both multiplicative and additive terms. Underlying the additive term is the hypothesis of preferential independence [4] of prior occupation and education, which, in the author's experience, is verified in practical situations. The terms $c_{ij}$ , $a_{ij}^{0}$ , $a_{i}^{e}$ lie between 0 and 1 and admit themselves a utility function interpretation.

The occupation, education and commitment indices can further be determined from primary information as follows. Occupation index:

$$
a _ {i j} ^ {0} = \left\{ \begin{array}{l} \big ((1 - \beta_ {j}) + \beta_ {j} m (i) \\ \quad / M (p (i)) \big). \gamma (p (i), j) \\ \text {if} \quad m (i) \leq M (p (i)) \\ \gamma (p (i), j) \quad \text {else}. \end{array} \right.\tag{3}
$$

The basic term here is $\gamma(p, j)$ which measures the utility of assigning a person from profession group p to job j. It is recognised that similar professions can be grouped together and treated identically. This grouping reflects the “resolution”, or level of detail, at which the organisation examines the professional background of new personnel. Thus, each person i belongs to a certain profession group $p(i)$ and each profession group p has affinity $\gamma(p, j), 0 \leq \gamma \leq 1$ , with job j. The values of $\gamma(p, j)$ are tabulated. In the extreme, a profession group may include just one profession. The term

$$
\left(1 - \beta_ {j}\right) + \beta_ {j} m (i) / M (p (i))
$$

provides a piecewise linear model of the learning effect. In particular, $m(i)$ is the number of months of professional experience of person i, $M(p(i))$ represents some conventional maximum learning period for the profession group $p(i)$ , and $\beta_{j}$ , $0 \leq \beta_{j} \leq 1$ , expresses the importance of the learning effect (slope of the learning curve) for job j.

![](/api/attachments/BMM6G5T7/fulltext/images/9612bec5a8759aa8f24183f581a28cd6838b72619740d1b0fab85d75deadbe38.jpg)  
Fig. 3. Learning Effect in the Occupation Index.

The occupation index as a function of professional experience is shown in fig. 3. Education index:

$$
a _ {i} ^ {e} = e (i) / E.\tag{4}
$$

Each individual i belongs to an education group $e(i) \in \{0, 1, \ldots, E\}$ . Thus the education groups correspond to some classification of educational credentials with 0 representing illiteracy and E the highest level of education. Then the education index is an index of merit for person i assuming for simplicity a linear dependence on the level of education. It should be noted that the education index reflects only the level of education, whereas specialty acquired through this education is accounted for in the occupation index. Commitment index:

$$
c _ {i j} = c (d (i), r (i), j),\tag{5}
$$

where $d(i)$ is the expected duration and $r(i)$ the rank of the assignment of person i. As mentioned earlier, $c_{ij}$ acts as a discount factor, $0 \leq c_{ij} \leq 1$ . The values $c(d, r, j)$ are tabulated.

Finally, there is a comment to be made regarding health groups, though these are considered in determining feasible assignments rather than utility indices. Each individual i is classified in a health group on the basis of medical tests, just as (s)he is classified in profession and education groups. If membership in a certain health group implies some disability then, according to an established practice, this is taken into account as a prohibitive factor for certain jobs, but is not further considered in evaluating feasible assignments. Therefore, health groups are only considered in the construction of eligibility tables.

## 3.2. Initialisation of the Assessment Process

The first stage of utility assessment, i.e. determining feasible assignments, is based on the eligibility tables. As these tables reflect long term personnel assignment policies, they are rarely updated.

The second stage, determining the utility indices, can be automatically carried out using formulas (2)-(5) provided values for $\lambda_{j}$ , $\beta_{j}$ , $M(p)$ , $\gamma(p, j)$ and $c(d, r, j)$ . The parameters $\beta_{j}$ and $M(p)$ describing the learning effect are expected to undergo very few updates, if at all, after a thoughtful first setting. Initially, tables must also be constructed for the values of $\lambda_{j}$ , $\gamma(p, j)$ and $c(d, r, j)$ . Questionnaires asking for preference rankings on, say, a five point scale [4], can be used to assess the entries of the tables. These tables must be checked for consistency and endorsed by all levels of management involved in the assignment of new personnel.

## 3.3. Model Calibration

Once the mentioned tables of values are made, the assessment of utility indices requires no human intervention. Nevertheless, after these automatically generated indices have been used in the ordinary assignment process, the resulting assignment may be unsatisfactory. In particular, certain jobs may systematically receive less preferred personnel or certain professional or educational groups may be systematically assigned in unexpected ways. Such incidents reveal errors in the original tables of values. The relevant values should then be altered and the ordinary assignment process repeated until no systematic dissatisfaction with the assignment arises. The iterative process is called model calibration. Random cases of poor assignment may still exist. These should be attributed to the inherent imperfection of the model and be directly corrected by the manager in charge.

The corrected tables should be tried again in the next few personnel assignments. After a hopefully short series of calibrations, they will stabilise and be labelled as a new version of the original ones. The versions of tables created in this fashion will reflect changes in personnel assignment policies.

## 4. Special Assignment

Rational assignment ideally corresponds to solving the utility maximisation problem (1). This is undertaken by the ordinary assignment module, as explained in the next section. In practice, subjective managerial judgment overrides established “objective” procedures and marks each new personnel assignment as a unique decision problem. Facing elegantly this reality is an imperative requirement of any prospective decision support system. Besides, human intervention is also required to compensate the inherent imperfections of the decision model.

In the present system, the assignments which can be made according to a routine procedure are left to the automatic ordinary assignment module while all the rest, deserving special attention, are handled by the manager through the special assignment module. Regardless of the reasons underlying the manager's choice, this turns out to be a sequence of four basis selections: enforce or forbid the assignment of individual persons or of classes of persons. The definition of a class of persons is easily effected in an ad hoc manner using the query facility of the data base management system.

To ensure consistency and resolve possible conflicts, a priority over the basic selections is defined, shown in fig. 4. The rule is that positive are stronger than negative assertions and individual are stronger than class decisions. Of course, any kind of special assignment is stronger than ordinary assignment.

<table><tr><td></td><td>INDIVIDUAL ASSIGN.</td><td>CLASS ASSIGNMENT</td></tr><tr><td>ENFORCE</td><td>1</td><td>3</td></tr><tr><td>FORBID</td><td>2</td><td>4</td></tr><tr><td colspan="2">ORDINARY ASSIGNMENT</td><td>5</td></tr></table>

Fig. 4. Special Assignment Priorities.

Class assignment decisions may involve the entire class or fraction of it. In general, they take the following form: from class X assign (or not assign) n persons (or x%) to job j. When n (or x%) does not cover the entire class, a random selection from the members of the class is made. If satisfying this requirement is infeasible, a message is sent to the user who can then either remain satisfied with the closest possible approximation to the specified number n (or x%), or attempt to achieve it by supplementary individual decisions.

As mentioned, special assignment overrides ordinary assignment. Therefore, $(i, j)$ pairs selected or excluded by special assignment can be dropped from consideration in solving problem (1). Equivalently, the constraint set must be augmented with $x_{ij}=0$ or $x_{ij}=1$ constraints. So, special assignment effectively performs the following editing functions on the assignment graph:

(a) Enforce assignment $(i,j)(x_{ij} = 1)$ :

(1) Register the assignment $(i,j)$ ;

(2) Remove node $i$ and all links $(i, j)$ ;

(3) Reduce $d_{j}$ by one.

(b) Forbid assignment $(i, j)(x_{ij} = 0)$ ;

Remove link $(i, j)$ .

(c) Enforce or forbid class assignment: Perform (a) or (b) respectively for each member of the class.

## 5. Ordinary Assignment

The ordinary assignment module performs automatically those assignments which can be carried out by a routine procedure. According to the author's experience with Greek organisations, more than 70% of the assignments are routine cases, which implies the practical importance of

Personnel

Jobs

![](/api/attachments/BMM6G5T7/fulltext/images/c345f3feb6e61b8ec445348fad8a54b19429e0f707fdc31083fc4f6b4d513fdb.jpg)  
Fig. 5. Augmented Network Model.

the ordinary assignment and the utility assessment modules.

Since ordinary follows special assignment, the ordinary assignment module solves the utility maximisation problem (1) on the assignment graph edited by the special assignment module. We shall use the notation $I'$ , $J'$ , $A'$ , $d_{j}'$ to denote the edited node sets I, J, arc set A and personnel requirement $d_{j}$ . Since each time $d_{j}$ is changed it is reduced by one, it may eventually become zero. If this happens, node j is removed from the graph.

We now transform problem (1) into a network flow problem which will enable the use of efficient network optimisation algorithms for its solution.

Let us augment the node sets I and J by a dummy source node s and a dummy terminal node t respectively, and the arc set A by arcs $(s, j)$ , $j \in J$ and $(i, t)$ , $i \in I$ , all with utility indices

$$
a _ {s j} = a _ {i t} = 0, \quad i \in I, j \in J.\tag{6}
$$

Moreover, let the supply at node s be equal to the total personnel requirement D and the demand at node t equal to the available new personnel m. The augmented network is shown in fig. 5.

Problem (1) can now be equivalently formulated on the augmented network as follows:

$$
\max \sum_ {(i, j) \in A} a _ {i j} x _ {i j}
$$

subject to

$$
\sum_ {j \in J} x _ {i j} = e _ {i}, \quad i \in I,\tag{7}
$$

$$
\sum_ {i \in I} x _ {i j} = d _ {j}, \quad j \in J,
$$

$$
x _ {i j} \geq 0,
$$

where $I, J, A$ are augmented as above and

$$
\begin{array}{l} e _ {i} = 1, \qquad i \in I - \{s \}, \\ e _ {s} = D = \sum d _ {j}, \\ d _ {t} = m. \end{array}\tag{8}
$$

The integrality of the decision variables has been relaxed, as it is guaranteed by the form of the constraint matrix and the right hand side values being integers [5].

The equivalence of (7) to (1) follows from (6), (8) and the definition of the augmented sets I, J, A.

Problem (7) is in the form of the well known Hitchcock problem [5] which can be solved by a number of efficient algorithms.

Ordinary assignment then consists of solving (7) with I, J, A, $d_{j}$ replaced by $I'$ , $J'$ , $A'$ , $d_{j}'$ . Each time special assignment is performed, a new edited assignment graph is produced. The fact that the edited graph is smaller than the original one improves the efficiency of ordinary assignment in terms of both time and memory.

## 6. Further Work

In this paper we have presented the design of a decision support system for massive personnel assignment. We currently concentrate our effort on the efficient implementation of the ordinary assignment module.

The target problem size of 2000–3000 persons and approximately 100 jobs is large, even if the graph is sparse, as expected (each person is usually fit only for a small number of jobs). Even though this is not the kind of decision problem that one requires to have an instant solution for, speed still is an important consideration. We are currently implementing a primal-dual algorithm and a problem feasible algorithm along with suitable, easily maintainable, data structures.

In parallel, a user interface to support utility assessment and model calibration is being developed.

## Acknowledgment

I am grateful to Dr. Michael Kavvadas for the initial stimulus for this work as well as for long informative discussions.

## References

[1] J.L. Huttinger, M. Berger (1986), An Expert System-Linear Programming Approach to Organisation Manpower Allocation. ORSA/TIMS Joint National Meeting, Miami.

[2] M. Pina JR., M.S. Semerson (1987), Evaluation of Processing and Classification of Enlistees (PACE) Operational Prototype. ORSA/TIMS Joint National Meeting, New Orleans.

[3] D. Klingman, N.V. Philips (1984), Topological and Computational Aspects of Preemptive Multicriteria Military Personnel Assignment Problems, Management Science, Vol. 30, pp. 1362–1375.

[4] R.L. Keeney, M. Raiffa (1976) Decisions with Multiple Objectives: Preference and Value Tradeoffs. John Wiley.

[5] C.P. Papadimitriou, K. Steiglitz (1982), Combinatorial Optimization: Algorithms and Complexity. Prentice-Hall.

[6] P.G.W. Keen, M.S. Scott Morton (1978), Decision Support Systems: An Organizational Perspective. Addison-Wesley.
