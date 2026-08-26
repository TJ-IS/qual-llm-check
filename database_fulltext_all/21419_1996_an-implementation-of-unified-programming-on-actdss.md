---
otero_id: 21419
otero_key: "A7GTQP2M"
title: "An implementation of unified programming on actDSS"
authors: "Yasuhiko Takahara; Naoki Shiba; Hirokazu Tanaka"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80004-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An implementation of unified programming on actDSS

Yasuhiko Takahara $^{*}$ , Naoki Shiba, Hirokazu Tanaka

Department of Management and Systems Engineering, Tokyo Institute of Technology, 2-12-1 Ookayama, Meguro-ku, Tokyo 152, Japan

## Abstract

A unified programming environment is implemented on our DSS generator, called actDSS, which is a general platform for constructing intelligent specific systems. The architecture of the implemented unified programming is a hierarchical connection of a numerical solver and a non-numerical evaluator. The former produces an optimum solution of a problem and the latter evaluates the solution heuristically, controlling the total model that encompasses the former by modifying the constraint and the parameter value. A job assignment problem is used as a demonstration of the architecture, which is formulated as a mixed integer programming problem. In this paper, a general scheme of the unified programming is introduced. Its feasibility on actDSS is demonstrated and finally we discuss how the implementation was possible in the system.

Keywords: DSS (decision support system); DSS generator; Unified programming; Job assignment problem

## 1. Introduction

Our group has been engaging in development of an intelligent DSS generator which is called actDSS $[3,4]$ . This paper reports how a unified programming can be realized on actDSS. We emphasize that actDSS is not developed to solve a specific problem but to provide a general platform to construct an intelligent specific DSS. The implementation of the unified programming presented in this paper is, therefore, one illustration to show a basic scheme for realization but not a unique one for our system.

Ideally, no assumption should be made about the ability of a user of the system. However, this is not practical if we seriously want to develop a meaningful intelligent system at the current stage of technology. It is assumed that the most desirable user of the current implementation has some capability to handle a simple model description language and a simple logic programming language like Prolog which is used as a “system” language. We assume that this assumption reflects the necessary computer literacy of a DSS user.

It must be remarked, however, that in actDSS once a usable specific system is built by a capable user, it can be saved by the configuration function of actDSS and can be used effectively by a user without any technical knowledge.

In this paper we first present a general architecture of our unified programming system with its formulation and then demonstrate its feasibility on actDSS by applying the architecture to a job assignment problem. The problem requires a non-linear integer programming algorithm as well as qualitative evaluation and control of the solution process to be solved satisfactorily. Finally we discuss how the implementation is supported technically on actDSS.

## 2. A general architecture of the unified programming on actDSS

Fig. 1 shows a general architecture of the unified programming system realized on actDSS. The basic strategy of the realization is that the system is constructed by a hierarchical composition of a numerical solver and a non-numerical solution evaluator. The numerical solver yields an optimum solution for a specific objective function subject to given constraints.

The objective function and the constraints are given by table models, by the problem formulator and by the constraint base which will be explained later. The table model formulator, the problem formulator and the numerical solver are organized as a complex model. The organization is done by linking variables of submodels. Then the complex model is represented by one composite model, called total composite model. The constraints are selected from the constraint base by the numerical solver.

![](/api/attachments/A7GTQP2M/fulltext/images/9081fbb5ce316b602ff14090923a6628a216939cd90b01d2b6cd429eb529868a.jpg)  
Fig. 1. General architecture.

The solution evaluator changes the constraint selection and/or modifies parameters in the table models in order to make the problem feasible, if there is no feasible solution, or to make the optimum solution satisfy qualitative requirements. It should be noticed that the solution evaluator is not simply cascaded to the numerical solver but hierarchically connected to the total composite model and sends a message to the total composite model so that the numerical solver produces a satisfactory solution. This function is realized by using the composite model building feature of actDSS. The user can also evaluate the result and modifies the constraint base and model parameters and controls the constraint selection to get a better solution.

This architecture may look similar to the most popular strategy for a unified programming system $[1,2]$ . In reality, however, it is different from the conventional one in the sense that the solution evaluator is hierarchically connected to the other submodels and flexible modifications of the solver problem are allowed. These are supported by the basic features of actDSS which will be discussed in Section 4.

As the figure shows the architecture consists of 7 components; table model formulator, problem formulator, numerical solver, solver, constraint base, total composite model and solution evaluator.

The table model formulator is a submodel consisting of a family of tables which represents the real world situation including objectives and problem boundaries in accordance with the user's image. The family of tables provides connection from the real world to the problem to be solved by the numerical solver. The user mainly controls and interprets the problem solving process through this representation, giving it the name table model. Therefore, the output of the table model formulator is not a formalized model to which a solution technique is directly applicable.

The problem formulator is a submodel which transforms a family of table models into a class of atomic concepts (or parameters) from which a real analytical problem can be constructed and on which qualitative arguments of the solution evaluator are developed.

The numerical solver is a submodel which constructs a mathematical programming problem combining the atomic concepts given by the problem formulator and produces an optimum solution using the associated solver.

The solver is a submodel which yields an optimum solution with respect to a specific performance function subject to a family of constraints. ActDSS has many kinds of solvers, from a standard one like an LP-solver to a specialized heuristic one like the solver developed for the job assignment problem in this paper.

The constraint base is a kind of KB (knowledge base) which stores qualitative requirements for a satisfactory solution. Not every constraint is used by the solver. The constraint selection is made by the information from both the user and the solution evaluator. If necessary, the user can create new constraints while working interactively with the system.

The total composite model represents an independent model composed of the submodels. We can automatically execute all the submodels in a proper way by executing the total model.

The solution evaluator is a submodel which evaluates the solution given by the numerical solver or the solver. If the solution is not satisfactory with respect to a criterion which is embedded into the solution evaluator by the user or the system developer, the submodel modifies the constraint selection to be used by the solver and re-executes the total model in order to make the solver yield a solution which satisfies the criterion.

Commonly, if the number of constraints to be satisfied is increased, it becomes more and more difficult for the solver to find a feasible solution. If no feasible solution can be found, the solution evaluator will modify parameter values of the table models so that the solver can find a feasible solution. If the modified values of the parameters do not reflect the real world situation, the modified values are to be understood as suggestions from the system to the user.

By observing the suggestions, by the solution evaluator as well as by examining the produced solution of the problem, the user is expected to have some deeper insight into his problem. This improvement of insight is the target of actDSS [4]. If he is not satisfied with the solutions, as mentioned above, he has the complete authority to modify the parameters and the constraints. He can get the result of his modification by execution of the total model and re-modify until he gets a better solution.

![](/api/attachments/A7GTQP2M/fulltext/images/74303b40f99bdcb44a5a652dd6958f6421812f095c4bcc57d51159e711c24c3e.jpg)  
Fig. 2. Example of table model.

Let us formulate the general architecture. The table model formulator is a mapping $T\_M\_F$ which assigns a class of relations to a given DB (data base), i.e.,

$$
T \_ M \_ F: D B \mapsto \left\{R _ {i} (\alpha_ {i}, \beta_ {i}) \mid i \in I \right\},
$$

where $I=\{1,2,\ldots,n\}$ is an index set and $R_{i}(\alpha_{i},\beta_{i})\subset V_{i_{1}}\times\ldots\times V_{i_{m}}$ , where $V_{i_{k}}$ is the set of values of the kth attribute of $R_{i}(\alpha_{i},\beta_{i})$ . $R_{i}(\alpha_{i},\beta_{i})$ is a formulation of the table model. The families of attributes are specified by the user according to his image about the real world. $\alpha_{i}$ and $\beta_{i}$ are parameters controlled by the user and the solution evaluator, respectively. Their modification corresponds to the size or values of $R_{i}$ . Modification of the size means creation or deletion of entries of $R_{i}$ .

Fig. 2 shows two relations, “man.s” and “job.s”. The relation man.s has four attributes, “name”, “paylevel”, “ablelevel” and “maxtime”. The size of man.s is currently four. The user, however, can add another entry or delete one of the entries to change the size. Furthermore, the values of, for instance, “paylevel” can be changed by the user and the solution evaluator as shown in the program of "soleval3.m" in Appendix A.

![](/api/attachments/A7GTQP2M/fulltext/images/2c007b89089584b7df95ee913d556a40635192f72e9a0add0bf064816465e616.jpg)  
Fig. 3. Example of problem formulator.

The problem formulator is a mapping $P_{F}$ which transforms the class of relations into a list of parameters, i.e.,

$$
P \_ F: \left\{R _ {i} (\alpha_ {i}, \beta_ {i}) \mid i \in I \right\} \mapsto \left\{P _ {j} \mid j \in J \right\} \equiv P,
$$

where $J=\{1,2,\ldots,l\}$ is an index set. As mentioned above, P provides the basic concepts on which the problem formulation and the problem analysis are carried out. In Fig. 3 P\_F is given by the model “probform2.m” whose inputs are job.s and man.s. It produces seven atomic concepts, “mname”, “mclassT”, “mclassA”, “mclassP”, “jname”, “jclassT” and “jclassL”. The concept “mname” has a list “[m1.m, m2.m, m3.m, super]” as its value.

The numerical solver $P_{-}S$ is a submodel which formulates a numerical solver problem (an optimization problem) from P and a given constraint information, and solves it using the associated solver to produce an optimum solution, $m^{*}$ and its associated data, $D^{*}$ , i.e.,

$$
P \_ S: (P, \text { Constraint\_Inf }) \mapsto (m ^ {*}, D ^ {*}).
$$

In Fig. 4 P\_S is given by the model “probsol.m”, where Constraint\_Inf consists of two components, “cnstrnt” and “cnstrntN”. The first component specifies the selection of prepared constraints in the constraint base. For example, the current value of cnstrnt is “[ability, time]”, meaning two constraints are selected. The second component supplies the name of the constraint specification program which the user creates in MDL (a model description language of actDSS which will be discussed in Section 4) while processing the problem. The current value of “cnstrntN” is “nil” which implies that the user has not created a new constraint yet.

The real task of the numerical solver is done by the submodel solver Sol which is usually written in a third generation language such as C.

In principle, every model is written in our model description language MDL and hence Sol must be called by P\_S in MDL as a subroutine. (P, Constraint\_Inf) is transformed into an optimization problem $\langle f(P,m),\Phi(P,m)\rangle$ in Sol, where m is the decision variable, $f(P,m)$ is the performance function and $\Phi(P,m)$ is the predicate representing the constraint. Then,

$$
\begin{array}{c} S o l: (P, C o n s t a r a i n t \_ I n f) \mapsto \langle f (P, m), \Phi (P, m) \rangle \\ \mapsto (m ^ {*}, D ^ {*}). \end{array}
$$

The solution $m^*$ is given by the following procedure:

1. Generate a solution candidate.

2. If the generation fails go to 8 else go to 3.

3. Evaluate the candidate with respect to the constraint given by “cnstrnt”.

4. If the evaluation is unsatisfactory go to 1 else go to 5.

5. Evaluate the candidate with respect to the constraint given by “cnstrntN”.

6. If the evaluation is unsatisfactory go to 1 else go to 7.

7. Update the solution set and go to 1. The solution set saves the best solutions discovered so far.

![](/api/attachments/A7GTQP2M/fulltext/images/154b751f7123068a68afc411a87b2d9529252643f2395d733484a1e667ab9990.jpg)  
Fig. 4. Example of numerical solver.

8. If the solution set is empty go to infeasible exit else go to successful exit.

As mentioned, the constraint predicate consists of two predicates, “cnstrnt” and “cnstrntN”.

Since Sol is a subroutine of $P\_S$ , it is not illustrated in Fig. 4. In $P\_S$ 's representation for “prob-sol.m”, $m^*$ and $D^*$ are given by sol = [‘‘super’’, ‘‘super’’, ‘‘m2.m’'] and totalpay = 50.25, respectively.

In Fig. 5 the submodels, “man.s” and “job.s”, “probform2.m” and “probsol.m” are encircled by a rectangle. As mentioned above, this means that those models are integrated as one composite model whose name is “total.c.”

The solution evaluator is a mapping $S\_E$ , i.e.,

$$
S \_ E: (P, M n a m e, m ^ {*}, D ^ {*})
$$

$$
\mapsto \big (\beta , C o n s t r a i n t \_ I n f ^ {*}, m ^ {* *}, E v D \big),
$$

where Mname is the name of the total composite model, $\beta$ is a new vector of the parameter values $(\beta_{i} \mid i \in I)$ in $\{R_{i}(\alpha_{i}, \beta_{i}) \mid i \in I\}$ , Constraint\_Inf\* is a new value of Constraint\_Inf, $m^{**}$ is a new solution with respect to $\beta$ and Constraint\_Inf\*. EvD represents statements of evaluation results. In Fig. 6 Mname = total.c.

The basic procedure of the solution evaluator is as follows:

1. Get the solution $m^{*}$ from the numerical solver.

2. If the solution is empty (infeasible), go to 3, else go to 5.

3. Specify parameter modification in $\{\beta_i | i \in I\}$ and suggest it to the user.

4. Go to exit.

5. Evaluate the solution with respect to criteria.

6. If the solution is satisfactory, go to 4.

7. Modify parameters in $\{\beta_{i} \mid i \in I\}$ and/or change the constraint in “cnstrnt”.

8. Execute the total model to produce $m^{**}$ and go to 4.

It must be emphasized that the above procedure is not the best but one realization of the solution evaluator. This realization is made to show the basic functions of actDSS which allows many kinds of the realization of a solution evaluator in general.

<table><tr><td colspan="6">TOOLBOX</td></tr><tr><td>2</td><td>exit</td><td>help</td><td>abort</td><td>trace</td><td>initial</td></tr><tr><td></td><td>undo</td><td>uconfig</td><td>autocal</td><td>window</td><td>graph</td></tr><tr><td></td><td>ntable</td><td>sheet</td><td>sscontrol</td><td>ssrange</td><td>sscopy</td></tr><tr><td></td><td>selectcpy</td><td>ssclear</td><td>ssfile</td><td>alarm</td><td>protect</td></tr><tr><td></td><td>average</td><td>variance</td><td>distribute</td><td>sttsts_93</td><td>sttsts_Gr</td></tr><tr><td></td><td>random.t</td><td>nax</td><td>nin</td><td>sum</td><td>sqrt</td></tr><tr><td></td><td>sort_row</td><td>sort_col</td><td>goalseek.p</td><td>risk.p</td><td>setbpint</td></tr><tr><td></td><td>resetpint</td><td>setkpint</td><td>resetkpint</td><td>setrvrs</td><td>resetrvrs</td></tr><tr><td></td><td>sheetnap</td><td>prvlg</td><td>prdchck</td><td>geometry</td><td>nns.p</td></tr><tr><td></td><td>test1</td><td>test2</td><td>invest.p</td><td>invest6.p</td><td>testlist</td></tr><tr><td></td><td>testlist</td><td>testfront</td><td>es.p</td><td>prof_t2.p</td><td>smodeling</td></tr><tr><td></td><td>stmodel</td><td>script.p</td><td>nytask.k</td><td>visEUL.p</td><td>test3</td></tr><tr><td></td><td>test4</td><td>empress</td><td>anprplan</td><td>nenuspace</td><td>nenu.nn</td></tr><tr><td></td><td>app</td><td>feedmix</td><td>app1</td><td>nenu1.nn</td><td>nodelspace</td></tr><tr><td></td><td>app2</td><td>hirota.nn</td><td>test</td><td>tanaka</td><td>tanaka1</td></tr><tr><td></td><td>append</td><td>erase</td><td>replace</td><td>transfer</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/A7GTQP2M/fulltext/images/76b7fbf0e75125d7e209125daaa7c770dfcbdfb9dc213f56a13ab4d592163ab0.jpg)  
Fig. 5. TOOLBOX and model space.

![](/api/attachments/A7GTQP2M/fulltext/images/8657c28fb62b8174f64464bb5e94067fe14a71777572f39a024295af9657cabd.jpg)  
Fig. 6. Example or solution evaluator.

EvD of Fig. 6 consists of two components, “action” and “mT”. The fact that “action” is “[“TMODEL MODIFIED”]” means the original solution $m^{*}$ dose not satisfy the criteria, “Load Equality”, so the parameters in the table models are modified by “soleval3.m”. $\beta$ and Constraint\_Inf\* are not illustrated in “soleval3.m” (Fig. 6) but are displayed in the table models (Fig. 2) and in “probsol.m” (Fig. 4).

## 3. Application of the general architecture to a job assignment problem

Let us apply the general scheme to a job assignment problem. Suppose there are n available persons and l jobs to be fulfilled. The problem is to allocate the persons to the jobs in an optimum way.

For the sake of simplicity, suppose the persons are characterized by four attributes, name, ability level, pay level and maximum workable time, or the ith person is represented by $(man(i,N), man(i,A), man(i,P), man(i,T))$ . Similarly, the jobs are characterized by three attributes, name, difficulty level and required time, or the jth job is represented by $(job(j,N),job(j,L),job(j,T))$ . Furthermore $man(i,X)$ and $job(j,Y)$ , except the name attributes, are assumed to be numerically valued.

Suppose the performance criterion is to minimize the total payment. Let $m = (m(1), \ldots, m(l))$ be a decision variable, where $i = m(j) \in \{1, \ldots, n\}$ means that the jth job is assigned to the ith person. Let an auxiliary variable $x(i, j)$ be:

$$
x (i, j) = \left\{ \begin{array}{l l} 1 & \text {if} m (j) = i \\ 0 & \text {otherwise.} \end{array} \right.
$$

Then, the objective function is:

$$
\sum_ {i} \sum_ {j} x (i, j) \operatorname{job} (j, T) \operatorname{man} (i, P) \rightarrow \min.
$$

The following are obvious constraints:

\- Time constraint:

$$
\sum_ {j} x (i, j) \operatorname{job} (j, T) \leq \operatorname{man} (i, T) \text {   for   any   } i.
$$

\- Ability constraint:

$$
\begin{array}{r l} & \max \bigl \{x (i, j) j o b (j, L) | j = 1, \dots , l \bigr \} \\ & \quad \leq m a n (i, A) \text {   for   any   } i. \end{array}
$$

The first constraint requires that a person can not work more than his maximum workable time. The second means that a job should not be assigned to a person whose ability is lower than the job difficulty level.

The above constraints are fundamental ones which should not be violated. There are many other constraints which are related with welfare or morale of the persons. For instance:

\- Load equality constraint: Let

$$
a v T = a v e r a g e \left(\left\{\sum_ {j} x (i, j) \operatorname{job} (j, T) \mid i = 1, 2, \dots , n \right\}\right),
$$

where average is an operator to calculate the average of a set. Then

$$
\left| \sum_ {j} x (i, j) \operatorname{job} (j, T) - a v T \right| <   a v T \cdot r \text {   for   any   } i,
$$

where $0 < r < 1$ .

• Minimum payment constraint:

$$
\sum_ {j} x (i, j) \operatorname{job} (j, T) \operatorname{man} (i, P) > M i n \text {   for   any   } i,
$$

where $Min(>0)$ is a minimum payment.

Many other constraints can be proposed but it is not the purpose of this paper to try to present a complete list of possible constraints. These constraints are to be saved in the constraint base. In our implementation it is assumed that the time and the ability constraints must always be satisfied while the others may be selected by the solution evaluator and the user.

As the above formulation shows, the job assignment problem of this paper is a mixed integer programming and not a simple one, as indicated by the ability constraint. The construction of the numerical solver, therefore, requires a heuristic technique, in particular, in the generation of a solution candidate. Its detailed discussion is out of the scope of this paper.

Figs. 2–6 show the real implementation of the job assignment problem on actDSS. In the illustration, the following correspondences are obvious:

$$
\begin{array}{l l} n & = 4 \text {   or   four   persons   and   } l = 3 \text {   or   three   jobs; } \\ R _ {1} & = \text { man.s   and   } R _ {2} = \text { job.s; } \\ P \_ F & = \text { probform2.m; } \\ P \_ S & = \text { probsol.m; } \\ S \_ E & = \text { soleval3.m. } \end{array}
$$

The outcomes of $P\_F$ , $P\_S$ and $P\_E$ are listed in the output part of the corresponding model representations of Figs. 2–6. The model representation will be called “IORep” (input output representation) of the corresponding model. $P$ consists of seven parameters as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$P_{1} = mname = [man(1,N),man(2,N),man(3,N),man(4,N)] = [m1.m,m2.m,m3.m,super].$ $P_{2} = mclassT = [man(1,T),man(2,T),man(3,T),man(4,T)] = [2,3,4,100].$ $P_{3} = mclassA = [man(1,A),man(2,A),man(3,A),man(4,A)] = [9,4,1,10].$ $P_{4} = mclassP = [man(1,P),man(2,P),man(3,P),man(4,P)] = [4.12,3.50,3.12,4.25].$ $P_{5} = jname = [job(1,N),job(2,N),job(3,N)] = [j1.m,j2.m,j3.m].$ $P_{6} = jclassT = [job(1,T),job(2,T),job(3,T)] = [7,4,1].$ $P_{7} = jclassL = [job(1,L),job(2,L),job(3,L)] = [9,5,3].$
</div>

Two constraints, ability and time, are initially used for “cnstrnt”. Under the data given by man.s and job.s and the constraints, there exists an obvious optimum solution, sol = [‘‘super’’, ‘‘super’’, ‘‘m2.m’’](m \* = [4,4,2]), whose total payment equals 50.25.

Let us consider the procedure how the job assignment problem was solved on actDSS using Figs. 2–6. ActDSS is realized on a UNIX WS with X-window.

Step 1. Based on the formulation of the problem, the class of atomic concepts P is specified as the class of seven parameters $P_{1},\ldots,P_{7}$ as above. The values of n and l are not important and can be changed flexibly by the user while working on the system.

Step 2. The programs of the three submodels, “probform2.m”, “probsol.m” and “soleval3.m” are constructed using the MDL of actDSS. The programs are the realization of the formulations in

Section 2. MDL descriptions of “probform2.m”, “probsol.m” and “soleval3.m” are presented in Appendix A. The solver is written in C and is called by “probsol.m”. The MDL will be discussed in Section 4 [5]. These submodels are stored as UNIX files.

Step 3. The “modelspace” which is the platform for model manipulation of actDSS is opened by clicking the mouse at the entry “modelspace” of the window “TOOLBOX” [6]. Fig. 5 shows the “TOOLBOX” window. Initially the “modelspace” is empty. Then, by selecting the menu command “model” of the “modelspace” and clicking the mouse at an appropriate place in the “modelspace”, we create a model box at the place. Next, selecting the menu command “label” and clicking the mouse in the box, we enter into the state where we can type a model name in the box. In this way we can define a model on the “modelspace”. Fig. 5 shows that 5 submodels, “ man.s", "job.s", "probform2.m", "probsol.m" and "soleval3.m" are registered on the space ("total.c" is a total composite model and explained later).

Step 4. For each submodel, by clicking the mouse at its name being displayed on the space, we “compile and load” the submodel. On the screen we have the IORep of the submodel as the outcome of “compile and load” as shown in Figs. 2–6. At the same time the operation creates the internal representation of the submodel which will be used for execution. At this stage most of the value part of the variables are empty. Some variables are, however, initialized in the program, as indicated by initial(cnstrt, [ability, time]) in MDL description of “prob-sol.m”.

Step 5. At this stage the submodels are to be linked to produce one organized model. The link operation can be easily done. For instance, suppose we want to link the output variable “mclassT” of “probform2.m” to the input variable “mclassTO” of “probsol.m”. In this case we have only to click the mouse first at the value part of “mclassT” in the IORep of “probform2.m” and then do so at the value part of “mclassTO” in the IORep of “prob-sol.m”. Then a function “var(probform2.m, mclassT)” is entered by the system in the value part of “mclassTO”. Its evaluation, the value of “mclass T”, is to be displayed at the value part of “mclass TO”, while the function is kept behind it. This is not a static data link operation as realized in a conventional spread sheet but a dynamic model link operation supported by the model management system of actDSS. We can, for instance, execute a submodel of the organized model independently. Links among variable have been built to accommodate the mentioned model link. This link operation between any variables is possible “syntactically” due to the feature of actDSS that every model variable is typeless. It should be noticed that there is no type declaration in the MDL model definitions. The link relationships among the variables are aggregated into link relationships among submodels which show dependency relations among submodels and are displayed by the dotted arrows on the “modelspace”. This aggregated information is used to determine a correct execution sequence of the submodels when the submodels are integrated into a total composite model [6].

Step 6. Necessary data are loaded onto the table models “man.s” and “job.s” as shown in Fig. 2. Data are taken, in general, from the data base using a procedure in actDSS similar to QBE (query by example).

Step 7. The submodels, “man.s”, “job.s”, “prob-form2.m” and “probsol.m” are integrated as one total composite model, “total.c”, using the menu command “link” of the “modelspace”. To do this, after selecting “link” we click the mouse twice at two positions on the “modelspace”. Then, the system draws a rectangular specified by the two positions on the space and recognizes that the submodels surrounded by the rectangle are to be integrated as one model. The name of the integrated model should have “.c” for its extension. Notice that a total composite model is treated as one independent model while the organized model is not. The total composite model also has its IORep whose variables are submodel names. Then, if the user executes “total.c” (or clicks the mouse on “GO” of the IORep of “total.c”), the submodels are executed in the correct order,

“man.s”→“job.s”→“probform2.m”

→“probsol.m”.

The proper execution order is determined by the system using the aggregated link relationships as mentioned.

Step 8. The submodel “soleval3.m” is to be linked to “total.c”. In reality the variable “mname” is to be linked to “total.c”. This is done by clicking the mouse at the window identification of “total.c” and then by doing so at the value part of “mname”. The other variables can be linked as mentioned in Step 5.

Step 9. The integrated model “total.c” is executed. Each submodel of “total.c” is executed using its internal representation to assign values to variables. The results are displayed on the value parts of the corresponding variable names.

Step 10. “soleval3.m” is executed. In “soleval3.m”, MDL statements are used as interfaces to the other submodels and the real information processing (action210 of MDL description in “soleval3.m”) is written in Prolog. Since MDL statements can be used as interfaces, linkages among symbolic processing and numeric processing can be realized without any difficulty. In actual execution, “soleval3.m” which is a symbolic processor gets the optimum solution from “probsol.m” which is a numerical processor and evaluates it with respect to the evaluation criteria, such as the “Load Equality” criterion. If it finds the solution unsatisfactory, it modifies the numeric and/or symbolic parameters of the table models or the constraint selection. After modification, it executes “total.c” to get a new solution.

Step 11. If the user finds the solution satisfactory, his job is over. In general, in order to improve the solution, he may have to modify parameters, change the constraint selection (change the value of “cnstrnt” of “probsol.m”), or he may have to create a new constraint and insert its name into the value part of “cnstrntN” of “probsol.m” so that it is used by the numerical solver. In particular, if there is no feasible solution, he may have to increase the manpower introducing a new person into “man.s”, that is, n is increased. Even if there is a change of n, “probform2.m” can work without any modification which comes from the feature that a variable is typeless. Notice that there is no statement about n in the “probfrom2.m” in Appendix A. Then the user goes to Step 9 and finally gets a satisfactory solution.

Step 12. For the sake of a future use, the whole structure of the specific DSS of Figs. 2–6 may be saved as a [6]. This can be easily done by clicking the mouse on the command “wconfig” of the “TOOLBOX” in Fig. 5. In the present case the task is saved as “test2”. (The name specification is made by communication between the user and the system through the dialog subsystem and the name is automatically listed on the “TOOLBOX”). When a user clicks the mouse on “test2” of the “TOOLBOX” in the future, the system will reproduce the whole structure of Fig. 5 instantly. Then, he can use the reproduced specific DSS as it is or modify it to produce a new one by changing data or submodels.

## 4. Internal structure of actDSS

In this section we will discuss how implementation of the general architecture of Section 2 is possible on actDSS.

First, let us consider briefly about the basic structure and operation of actDSS.

Fig. 7 shows the implementation structure of actDSS. It is implemented in the UNIX environment. The most basic component of actDSS is its Prolog interpreter [7]. The Prolog of actDSS is an extension of the conventional Prolog. Most of the key predicates for realization of a DSS are defined in C and the actDSS Prolog calls them as subroutines.

The process operations of actDSS are specified in the Prolog, due to its descriptive convenience, its interpretative and non-procedural execution nature, as well as its typeless property. Precisely speaking, on the 4th layer, actOS or the operating system of actDSS is written in the Prolog.

The 5th layer consists of the basic functional components of actDSS including an MMS (model management system). The skeletons of the functional components are also written in the Prolog due to the reasons mentioned above.

Fig. 8 shows the functional structure of actDSS. Traditionally, a DSS is considered to be consisting of three components, dialogue system, MMS and DBMS. ActDSS has, in addition to them, two other components, model space and actOS. They play essential roles for realization of the general architecture as will be mentioned below.

![](/api/attachments/A7GTQP2M/fulltext/images/f51d235dc59b7a469c70b7556e95026207c3b42beda05993c5cda85ff0af3207.jpg)  
Fig. 7. Implementation structure of actDSS.

![](/api/attachments/A7GTQP2M/fulltext/images/47b4f1dbdc152d97d72c4c6e688ccc8fcc8401ec11f37e07edd4faccaaa79006.jpg)  
Fig. 8. Functional structure of actDSS.

Fig. 9 shows the process mechanism of actDSS. A user input is accepted by the window manager. The window manager is defined as one predicate. The input is handled in two ways. When it is a simple input, it is processed by the window manager and a response to the input is produced by the window manager. Most of the operations related with the spread sheet of actDSS are directly processed by the window manager.

When the input requires a complicated operation, the window manager transfers the system's control to the core of actOS. The transfer is called interrupt.

When the core of actOS receives an interrupt signal, it processes the input using an appropriate handling routine and yields a response to the input. The MMS is a typical process handling routine. Then it returns the control to the window manager which, then, waits for a next input.

![](/api/attachments/A7GTQP2M/fulltext/images/e0adfcda16b05fef8a6c0b67a49eaa6b6eb8abbf7c6e78a885fe58f5f8458ec6.jpg)  
Fig. 9. Process mechanism of actDSS.

Let us consider the model creation operations on the “modelspace” using Fig. 9 [6]. When a user clicks the mouse on the menu command “model” of the “modelspace” window (see Fig. 5), the input (the action of the mouse operation) is sent to the window manager with its categorization tag. The manager determines whether or not it can process the input by itself using the categorization information. Since every command (input) associated with the “modelspace” is categorized as one which is handled by the core of actOS, the system’s control is transferred to the core, which then calls the model management system which gets necessary information to deal with the input (for example, where is the model to be displayed on the model space?). The core communicates interactively with the user as mentioned in Section 3 and displays the model box on the “modelspace” using graph drawing routines of the graph management system.

The idea of “compile and load” of actDSS is shown in Fig. 10 [5]. In actDSS every program or model description is transformed into a Prolog program, which is the internal representation, by the compiler of actDSS and attached to the actOS Prolog program. The operation of the attachment is called load. Since Prolog is non-procedural, this mechanism makes a real time loading and deleting of models possible and hence flexible model management operations become feasible. For instance, we can replace an old “soleval3.m” of Fig. 5 by a new one in a real time fashion.

![](/api/attachments/A7GTQP2M/fulltext/images/851dda4f22a5e04ec9050af32844319015c1b04cdc1c91339c36a5840c608915.jpg)  
Fig. 10. Compile and load.

The reason why an easy implementation of the general architecture is possible on actDSS comes from the following facts:

1. MDL of actDSS can represent both a numerical solver and a symbolic solver in a uniform way, and hence they can be defined on the one platform “modelspace” and can be combined seamlessly. This fact is supported by fact 3 to be mentioned below.

2. Every model written in MDL has its IORep produced by MMS, where all variables used in the model are displayed and classified as input or output. That is, the IORep plays the role of interface among models. (Notice that a variable of the form \_<string> is not displayed in the IORep. It is treated as a hidden variable.) Consequently, with the help of the load structure, a real model integration approach is realized in actDSS.

3. Every variable of MDL is typeless or the system has one “frame” called “exp” for a variable. Therefore, any two variables can be linked in the syntactical sense.

4. The model composition feature exists.

In order to realize the unified programming of this paper, we have to first represent all models, numerical or symbolic, in MDL. This is possible due to 1. Then, due to 2 the system produces their IOReps automatically. An IORep teaches us what variables exist and how they are used in a model. Then due to 3 and due to the link mechanism we can connect models dynamically to produce a desired organized model at will. Finally, due to 4 we can produce a total composite model as one model. This is necessary for $S\_E$ , the solution evaluator.

Let us discuss the above features.

As Appendix A shows, the MDL of actDSS has the following characteristics:

1. It is a functional language.

2. Variables are typeless.

3. It can call a program in the Prolog as a subroutine in a seamless way. Therefore, a Prolog program can be, in fact, on the model space.

4. The Prolog can call a program written in 3rd generation languages in a seamless way. Therefore, a 3rd generation language program can be also, in fact, registered on the model space.

5. Since it is translated into a Prolog program to be executed, it is a non-procedural language.

The typeless property is essential for the link operation among submodels as mentioned above, and it makes the language flexible and easy to be used by a user. Let us consider the variable “mname0” in “probsol.m”. It is supposed to represent the name list of persons as shown in Fig. 4. But the user does not have to declare that its value is a list, and its size declaration is also unnecessary. If he modifies the data model “man.s”, for instance if he adds another person to the table, the value “mname0” changes its dimension automatically. This flexibility comes from the fact that every object including a variable is internally represented as a unique Prolog object which is ultimately defined as a structure called “exp” in C. All objects or concepts of actDSS are constructed based on the type “exp”. Conversely, “exp” is designed to be able to represent all types of objects necessary for DSS model description or DSS concept description, that is, an “exp” can be an integer, a real, a text, a constant, a variable of the Prolog, function, a predicate, a rule of the Prolog or a list. “exp” can be considered a kind of frame whose contents are specified by the system depending on the context. The same variable, then, can take different types of values depending on the context. A user need not worry about the type of a variable or specify its semantics rigidly beforehand, but the system takes care of it. Every subroutine in C of actDSS is constructed in the way that it processes only one data structure, “exp”.

Appendix B shows the translation of “probsol.m” into its Prolog form. This example shows how a function of the MDL can be realized as a Prolog subroutine (see “getlinkmname”). For instance, suppose we want to define the following new function f for an MDL model:

$$
y = f (x)
$$

where y and x are variable names of the MDL. Then, as its internal representation, the above statement is translated into the following Prolog statement:

$$
\mathrm{y} (\mathrm{Yy}): - \mathrm{x} (\mathrm{Xx}), \mathrm{f} (\mathrm{Xx}, \mathrm{Xf}), \mathrm{Yy} \text { is } \mathrm{Xf},!,
$$

where

$$
\mathrm{TYf} (\mathrm{Xx}, \mathrm{Yf}) \Leftrightarrow \mathrm{Yf} = f (\mathrm{Xx}).
$$

Therefore, we have only to define the following Prolog rule for realization of $f$ :

$$
f (X x, X f): - \dots
$$

The value of the variable y is given by that of Yy. Since the Prolog is strong enough to describe any necessary function of actDSS, this mechanism also makes it possible for the MDL to describe any symbolic solver.

The actDSS Prolog can call a subroutine of 3rd generation languages. Process procC("assignjob", [...] , [...] ) in "probsol.m" is a subroutine call of a C program "assignjob" from the Prolog. Data can be transmitted between them directly as the program of "probsol.m" shows. The user need not worry about the data structure transformation of a variable. This feature also comes from the fact that every variable is represented as an "exp" whether it is one of the MDL level, or of the Prolog level or of C level. Since MDL can call a Prolog subroutine seamlessly, it is able to describe any numerical solver.

The composite model building function is given by MMS of actDSS [6]. When the model composition operation is required, MMS expands the link relations among the submodels into a tree form and determines the execution sequence of submodels in the total composite model by expanding the tree by the depth first strategy. The execution sequence as well as the tree structure is saved as one of the internal representations of the total composite model and is used when the total composite model is executed.

## 5. Conclusion

As mentioned in Section 1, we explained in this paper how a unified programming can be implemented on our general platform actDSS using a job assignment problem as an example.

Even though our system does not have a special model building scheme which accepts a semantic definition of a model, table models are substitutes for it. Our experiences tell us that the model integration approach realized in our system and the table form model description provide an adequate environment for implementation of a unified programming.

## Appendix A

A.1. MDL description of “probform2.m”

//probform2.m

// This model extracts a family of atomic concepts to construct a problem

```txt
jclassT=matrix(job.data,"undef","time")
jclassL=matrix(job.data,"undef","level")
```

## A.2. MDL description of “probsol.m”

```txt
//
// probsol.m
//
// This model formulates a job assignment problem and produces
// an optimal solution of it.
// The real computation of optimization is carried out in "assignjob"
// written in C.
// This model is to be linked to soleval3.m

// initialization of the variable cnstrnt
// initial(cnstrnt, ['ability', 'time'])

// call "assignjob"; compute an optimum solution
// [mname0, ..., cnstrnt] is an input data to the solver
// _j_mout = [sol, totalpay] is the output of the model
_j_mout = assignjob(mname0, jname0, mclassT0, mclassA0, mclassP0, jclassT0, jclassL0, _cmname, cnstrntN, cnstrnt)

// value of cnstrntN = Prolog constraint rule name
// to which model is cnstrntN linked?
_mname = getlinkmname('cnstrntN')
_cmname = if _mname = 'nil' then 'nil' else project(_mname, 1)

// output:solution
sol = project(_j_mout, 1)
totalpay = project(_j_mout, 2)

// following is a family of Prolog subroutines called by MDL program
/% 
getlinkmname(CnstrntP, Mname): - !,
procC("getlinkmname", [CnstrntP], [Mname]);

assignjob(Mname0, Jname0, MclassT0, MclassA0, MclassP0, JclassT0, JclassL0, CMname, CnstrntP, Cnstrnt, J_Mout): - !,
procC("assignjob", [Mname0, Jname0, MclassT0, MclassA0, MclassP0, JclassT0, JclassL0, CMname, CnstrntP, Cnstrnt, J_Mout): - !,
procC("assignjob", [Mname0, Jname0, MclassT0, MclassA0, MclassP0, JclassT0, JclassL0, CMname, CnstrtP, Cnstrnt], [J_Mout]);
%
```

## A.3. MDL description of “soleval3.m”

```txt
//
// soleval3.m
//
// main statement
//
// _fsbltycon=feasibility condition check
// _action10=check load equality and pay equality conditions and
// modify data and/or change constraint
// _action21="OK"
action=if _fsbltycon="NO" then _action10 else _action21

// mname=target name
// m.t=data model name for man
_action21=action210(mname,m.t,mclassA0,mclassT0,mclassP0,jclassL0,jclassT0,sol0,_mT,tpay)

// check feasibility
_fsbltycon=fsbltycheck(sol0)

// change data to make the problem feasible
_action10=action1(mclassA0,jclassL0)

// _manmap=job assignment list of men
_manmap=amap(mname0,sol0)

// get required time
_mT=_manmap*jclassT0
mT=_mT

// start Prolog specifications of MDL functions
/% 
/*Prolog specification of action210*/
action210(Mname,M.t,MA,MT,MP,JL,JT,Sol,Mtime,Tpay,X):-!,
    ldcheck(MA,MT,MP,JL,JT,Sol,Mtime,Tpay,LdX),
    if LdX="NO"
    then
    action2(Mname,M.t,MA,MP,JL,X2)
end,

    paycheck(MA,MP,PayX),
    if PayX="NO"
    then
    action3(Mname,M.t,MA,MP,X3)
end,
    X:=[X2,X3];
```

```txt
/*feasibility check*/
fsbltycheck(Sol,X):- !,
    if Sol = nil
    then
    X:="NO"
else
X:="YES";

/*action for feasibility condition*/
action1(MA, JL, X):- !,
    xwriteln(0, "DATA MUST BE CHANGED!!"),
    functor(MA, Name, Num),
    assign(reg200, 1),
    assign(undertime, []),
    repeat,
    reg200(I),
    undertime(L),
    append(L, [I], LL),
    assign(undertime, LL),
    II:≈I + 1,
    assign(reg200, II),
    II>Num, !,
    retract([reg200]),

    undertime(UT),
    suggest2(MA, JL, UT, D, X);

action2(Mname, M.t, MA, MP, JL, X):- !,
    exp_to_text(Mname, MN),

    undertime(UT),
    overtime(OT),

    if UT = [] and OT < > []
    then
    suggest1(MN, M.t, MA, MP, X)
    else
    if UT < > [] and OT = []
    then
    suggest2(MA, JL, UT, D, X)
    else
    if UT < > [] and OT < > []
    then
    suggest1(MN, M.t, MA, MP, X)
    end
    end
    end;
end;
```

```txt
/*load quality check*/
ldcheck(MA,MT,MP,JL,JT,Sol,Mtime,Tpay,X):~!,
AvT:=average(Mtime),
assign(overtime,[]),
assign(undertime,[]),
assign(reg100,1),
functor(Mtime,Mtype,Mnum),
repeat,
reg100(I),
project(Mtime,I,MtimeI),
if MtimeI>AvT*1.2
then
overtime(L),
append(L,[I],LL),
assign(overtime,LL)
else
if MtimeI < AvT*0.8
then
undertime(L1),
append(L1,[I],LL1),
assign(undertime,LL1)
end
end,
II:=I+1,
assign(reg100,II),
II>Mnum, !,
retract([reg100]),
undertime(UT),
overtime(OT),

if UT=[] and OT=[]
then
X:="YES"
else
X:="NO";

/*pay equality check*/
paycheck(MA,MP,R):
Ind:=MA/MP,
X:=max(Ind),
Y:=min(Ind),
Z:=(X-Y)/X,
/*there is inequality*/
if Z>0.5
then
R:="NO"
```

```txt
else
    R:="YES";

/*modify pay data and execute task once*/
action3(Mname,M.t,MA,MP,R):
    xwriteln(0,"THERE IS PAY INEQUALITY PROBLEM!!"),
    xwriteln(0,"May I change pay level?(y/n)"),
    xread(0,Ans),
    /*modify pay data in m.t*/
    if Ans="y"
    then
    AvMA=average(MA),
    AvMP=average(MP),
    /*3=mimimum payment*/
    K:=(AvMP-3)/AvMA,
    MP2:=MA*K+3,
    procC("matrix",[M.t,"undef","paylevel",MP2],[]),
    R:="TMODEL MODIFIED",
    /*execute task once*/
    exp_to_text(Mname,MN),
    mmodelfname(Wp,MN,T),
    procC("go2",[Wp],[]);
/*change constraint and execute task once*/
suggest1(Mname,M.t,MA,MP,X):
    xwriteln(0,"THERE IS LOAD INEQUALITY!!"),
    xwriteln(0,"MAY I RESOLVE WITH LOADEQUALITY CONDITION?(y/n)"),
    xread(0,Ans),
    /*change constraint*/
    if Ans="y"
    then
    X:="LdEq included",
    /*get current constraint list*/
    Cnst1:=var(probsol.m,cnstrnt,0),
    /*append load equality constarint to the current*/
    union(Cnst1,[ldequality],Cnst2),
    /*new constraint list is stored in 'cnstrnt */
    var(probsol.m,cnstrnt,0):=Cnst2,
    /*execute the task under the new constraint*/
    mmodelfname(Wp,Mname,T),
    procC("go2",[Wp],[])
    else
    X:="";
suggest2(MA,JL,UT,D,X):
    MinL:=min(JL),
    assign(done,0),
    assign(reg100,UT),
```

```txt
repeat,
    reg100([I|Is]),
    project(MA,I,MAI),
    if MAI < MinL
    then
    X:="change condition",
    xwriteln(0,"conditions are infeasible!!!");
    xwriteln(0,"ability of ",I,"must be increased!!!");
    assign(done,1),
    end,
    assign(reg100,Is),
    done(Done),
    Done=1 or Is=[],!,
done(D),
    retract([done,reg100]);
suggest3();

amap(Mname,[],[[0,0,0],[0,0,0]]):-!;
amap(Mname,Mlist,X):-!,
assign(reg10,Mname),
assign(reg11,[]),
functor(Mlist,F,Size),
D:=constantlist(0,Size),
repeat,
    reg10([M1|Ms]),
    exp_to_text(M1,M),
    project(Mlist,L,M,"l"),
    replace(D,L,1,D1),
    reg11(Z),
    append(Z,[D1],Z1),
    assign(reg11,Z1),
    assign(reg10,Ms),
    Ms=[],!,
    reg11(X),
    retract([reg10,reg11]);
/%
```

## Appendix B

B.1. Translation of “probsol.m” into Prolog

```txt
initial(cnstrt, [ability, time]) :- !;

_j_mout(Y_j_mout):
    mname0(Xmname0), jname0(Xjname0), mclassT0(XmclassT0),
    mclassA0(XmclassA0), mclassP0(XmclassP0),
    jclassT0(XjclassT0),
    jclassL0(XjclassL0), _cmname(X_cmname), cnstrtN(XcnstrtN),
```

```prolog
cnstrnt(Xcnstrnt),
assignjob(Xmname0, Xjname0, XmclassT0, XmclassA0, XmclassP0, XjclassT0,
XjclassL0, X_cmname, XcnstrntN,
Xcnstrnt, X0assignjob),
Y_j_mout := X0assignjob, !;

_mname(Y_mname):
getlinkmname(cnstrntN, X0getlinkmname), Y_mname := X0getlinkmname, !;

_cmname(Y_cmname):
if _mname(X_mname), X_mname = nil
then Y_cmname := nil
else_mname(X_mname), project(X_mname, 1, X0project), Y_cmname := X0project, !;

sol(Ysol):
_j_mout(X_j_mout), project(X_j_mout, 1, X0project), Ysol := X0project, !;

totalpay(Ytotalpay):
_j_mout(X_j_mout), project(X_j_mout, 2, X0project), Ytotalpay := X0project, !;

getlinkmname(CnstrntP, Mname) : - !,
procC("getlinkmname", [CnstrntP], [Mname]);

assignjob(Mname0, Jname0, MclassT0, MclassA0, MclassP0, JclassT0, JclassL0,
CMname, CnstrntP, Cnstrnt, J_Mout) : - !,
procC("assignjob", [Mname0, Jname0, MclassT0, MclassA0, MclassP0, JclassT0,
JclassL0, CMname, CnstrntP, Cnstrnt], [J_Mout]);
```

## References

[1] H.J. Greenberg, A Natural Language Discourse Model to Explain Linear Programming Models and Solutions, Decision Support Systems 3 (1987) 333–342.

[2] J.K. Lee and M.Y. Kim, Knowledge-Assisted Optimization Model Formulation: UNIK-OPT, Decision Support Systems 13, No. 2 (1995) 111–132.

[3] Y. Takahara, J. Iijima and N. Shiba, A Hierarchy of Decision Making Concepts: Conceptual Foundation of Decision Support Systems, International Journal of General Systems 20, No. 2 (1992) 359–378.

[4] Y. Takahara et al., A New Paradigm of DSS and its Implementation, Journal of Office Automation 13, No. 3 (1992) 49–58 (in Japanese).

[5] Y. Takahara et al., Model Description Language and its Implementation in actDSS(III), Journal of the Japan Society

for Management Information 2, No. 3 (1994) 21–37 (in Japanese).

[6] Y. Takahara, J. Iijima and N. Shiba, A Model Management System and its Implementation, Systems Science 19, No. 4 (1993) 17–33.

[7] Y. Takahara, J. Iijima and N. Shiba, DSS as a System (submitted to International Journal of General Systems).

[8] Y. Takahara et al., An Operating System for Decision Support Systems – A Third Generation DSS, Journal of the Japan Society for Informatics 1, No. 1 (1991) 21–32 (in Japanese).

[9] Y. Takahara, J. Iijima and N. Shiba, User Interface in Decision Support System and its Control Support, Journal of the Japan Society for Management Information 1, No. 3 (1993) 45–60 (in Japanese).

[10] Y. Takahara and N. Shiba, Systems Theory and Systems Implementation – Case of DSS (to be published in Proceedings of the CAST Conference, Ottawa, 1994).

![](/api/attachments/A7GTQP2M/fulltext/images/7c5d2e91cf06c473d24c5eb018e0c904451cab6cf937af00d2fa56112e97f09a.jpg)  
Yasuhiko Takahara is a professor emiritus of Tokyo Institute of Technology, and a professor of Management and Systems Engineering, Chiba Institute of Technology. He received his B.S. in Applied Physics from the University of Tokyo in 1959, his M.S in Electrical Engineering and Ph.D. in Systems Science from the Case Western Reserve University in 1965 and 1967, respectively. His research interest is in mathematical general systems theory and its

![](/api/attachments/A7GTQP2M/fulltext/images/9d6b2fd5b404518e95361ab1bbaa61e60d6e6b6795c234c1599e0ea362ff81ca.jpg)  
Hirokazu Tanaka is a senior consultant of the Sakura Institute of Research and has joined the Department of Management and System Engineering at the Tokyo Institute of Technology since 1993. His research interests are in applying the technology of decision support systems to actual problem situations of organizations emphasizing organizational culture and business process. He has published widely in this area and recently completed a Ph.D. on this subject.

application to information systems, in particular, to decision support systems.  
![](/api/attachments/A7GTQP2M/fulltext/images/938a99f6d856f28882a1f4a427a49b519d92532b3cb0761d1c09e7b9527da452.jpg)

Naoki Shiba is an assistant professor of the Department of Management and Systems Engineering, Tokyo Institute of Technology. He received his B.E. in Control Engineering from the Tokyo Institute of Technology in 1986. He received his M.S. and Ph.D. in Systems Science from the Tokyo Institute of Technology in 1988 and 1993, respectively. His major research interests are systems theory and decision support systems.
