---
otero_id: 17040
otero_key: "KTUMB74S"
title: "A procedure for negotiating efficient and non-efficient compromises"
authors: "Gregory E. Kersten"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90126-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Procedure for Negotiating Efficient and Non-Efficient Compromises

Gregory E. KERSTEN \*

Decision Support System Research Laboratory, School of Business, Carleton University, Ottawa, Ont. K1S 5B6, Canada

An interactive procedure for group decision-making problems is presented in this paper. The procedure is based on the aspiration theory and utilizes both satisficing and optimizing approaches. The possibility of decision-makers forming coalitions is taken into account. The outcome of the modelled decision process is a compromise decision which can fulfil fairness and equity criteria. The compromise may also be an efficient solution. The procedure can be the basis for a group decision support system and such a system for a microcomputer network is discussed. An example of negotiations between management and trade union is presented.

Keywords: Group Decision Support System, Negotiation Support System, Group Decision-making, Negotiations, Conflict Resolution, Multiple-criteria Decision-making, Goal Programming, Microcomputer Applications.

![](/api/attachments/KTUMB74S/fulltext/images/b25db82ac47941ce9e7c9e72876da3b7843bbf067801214802c9adfe8f729dcd.jpg)

Gregory E. Kersten is an Assistant Professor at the Carleton University School of Business. Until 1984 he was an Assistant Professor in the Management Organization and Development Institute in Warsaw. He received Ph.D. in Economic Science-Operations Research from the Central School of Planning and Statistics in Warsaw. He is a co-funder of the Decision Support Systems Research Laboratory. His research interests include decision-making, negotiations, decision support tools, and artificial intelligence. He has published articles in Information and Management, European Journal of Operational Research, Information Processing and Management, and Przeglad Statystyczny among others.

\* I want to thank Tony Bailetti and Geoff Mallory for their stimulating and constructive discussions. This work was supported by the National Science and Engineering Council of Canada, Grant #A6755.

## 1. Introduction

The majority of real-world decision-making problems involve many decision-makers. Therefore, formalized procedures describing group decision-making and negotiation problems are of growing interest. Several interactive procedures, based on multicriteria decision analysis, have been proposed in [4], [7], [15] and [22]. The procedures assume rational behavior on the part of decision-makers: they possess all the information about the decision-making problem, and they are consistent and coherent in the decision process. Thus, the problem lies in the determination of individual, and then group, utility functions. Once these are determined, a compromise decision can be found. The compromise is an efficient (Pareto optimal) solution.

The rational behavior of a decision-maker in individual decision-making has not yet been proved, and there are numerous examples in which people systematically violate the requirements of consistency and coherence, and which indicate that their preferences may be intransitive, e.g., [5], [14], [25].

Decision-making in a social setting, such as negotiation, introduces new aspects. Decision-makers can evaluate a decision not only from the point of view of its objective performance levels, but from the point of view of its fairness and equity. Decision-makers who take into account fairness and/or equity may obtain a non-efficient compromise [10], [12].

In group decision-making, in contrast to individual decision-making, decision-makers may incorporate different and varying strategies. A decision-maker may initially incorporate the objectives of another decision-maker to improve his/her negotiation position. Irrelevant alternatives may influence the chosen compromise [16]. It means that utility functions are non stationary. This is because, in real group decision-making, different standards with respect to rationality arise, in contrast to the normative views of decision-making [3], [17]. Often decision-makers do not like to disclose their real interests (objectives) [2]. Hence, it may be impossible to determine a group utility function.

All the above aspects of decision-makers' behavior undermine the traditional, utility-based approach to modelling group decision-making and negotiations. The emerging approaches either assume nonstationary of the individual utility functions, or replace utility with aspirations. In these approaches the focus shifts from determining 'the best' compromise (optimal, efficient) on the basis of the initial input of decision-makers, to supporting the determination of a compromise on the basis of the initial input of decision-makers, to supporting the determination of a compromise on the basis of the iterative and changing input of decision-makers [1]. This enables decision-makers to change their goals, preferences and requirements (aspirations), and also enables to support creativity and communication during the decision process.

The use of a dynamic system to model conflict resolution has been proposed [18]. While, in general case, we may assume that both the decision set and the outcome (goal) set change during the decision process, an effective support in such a situation leads to difficulties with the decision-makers' control over the decision space. Quantitative modelling does not provide means for easy, effective but also flexible support and control of interactively derived repetitive representations of the ill-structured problems. Therefore, support systems that allow changes in decision-makers' preferences assume a given and constant decision set [8], [9].

The approach proposed here is based on the aspiration theory [20] which is a generalization of the satisficing approach [13]. It does not require a definition of utility functions or a ranking of alternatives, and it aims at supporting the decision process in a group setting and not at solving a group decision problem. This approach allows strategic interaction [23], i.e. dependence of individual choices of one decision-maker on choices and perceived interests of other decision-makers.

## 2. The Group Decision Problem

We consider here a group decision-making problem which can be represented in terms of certain functions with known properties. A group of decision-makers wants to reach consensus in a choice of a decision which is represented as vector $x, x \in R^{n}$ . The process of choice is iterative and particular decision-makers submit their compromise proposals and counterproposals for group consideration. The decision process is terminated when (i) all decision-makers agree on one decision, i.e., a compromise; (ii) a subgroup of decision-makers agree on one decision and this subgroup has enough power to implement the chosen decision (e.g., majority-type compromise); or (iii) a group reached deadlock and no decision is chosen.

A framework which can be used in describing different negotiation and group decision-making problems is presented in [11]. The proposed framework allows for the different behavior of decision-makers and changes in their strategies, and does not assume the existence of individual and group utility functions. It does not require that a decision-maker discloses his/her interests to another decision-maker, but allows a combination of the satisficing and optimizing approaches.

In decision-making, decision-makers often form aspiration levels to secure their interests or formulate compromise proposals. The latter can also be defined by aspiration levels. Decision-makers may also have their own objectives and want to achieve them on the highest/lowest possible levels. While aspiration levels define acceptable alternatives, objectives allow their comparison.

We assume here that aspiration levels take the form of right-hand sides (RHSs) of constraints which are controlled by decision-makers. These constraints are called soft constraints because decision-makers can change (replace) these constraints, or only their RHSs, when their interests or strategy change.

Group decision-making is a dynamic process. The process begins at the moment t = 0 when soft constraints, the RHSs (aspiration levels) of chosen constraints and/or a compromise proposal are chosen. Then decision-makers at moments $t = 1, 2, \ldots$ simultaneously or subsequently reformulate their aspiration levels, compromise proposals and/or search for spheres where mutual agreement is possible. The process ends at t = T when a compromise is achieved or the group reaches deadlock.

Let us formalize the last statements. Assuming for the sake of simplicity that all possible soft constraints are known a priori, we can define soft constraints for decision-maker (DM) m, i.e.,

$$
\begin{array}{l} g _ {i m} (x) \geq a _ {i m} (t), \quad i \in I _ {m}; \quad m \in M; \\ t = 0, \dots , T - 1, \end{array}\tag{1}
$$

where $a_{im}(t) \in R$ is the aspiration level defined by DM $m$ at the moment $t$ , $I_m$ is the set of soft constraint indices of DM $m$ and $M$ is the index set of decision-makers. Function $g_{im}(.)$ is assumed to be continuous and it transforms the alternative's characteristics into the aspiration value ( $g: R^n \to R$ ).

Some or all left-hand sides (LHSs) of (1) may describe objectives of DM m, so we can consider them as objective functions; at the moment t set $J_{m}(t)(J_{m}(t)\subset I_{m})$ is the set of indices of objectives chosen by DM m. For the sake of simplicity, we assume here that decision-makers want to achieve their objectives on the highest possible levels, and the vector of the aspiration levels $a_{m}(t)=[a_{im}(t)]$ of DM m describes the lower bounds of vector function $g_{m}(.)=[g_{im}(.)]$ .

Group decision-making is always conducted in a given setting, and decision-makers are assumed to have no influence on it. The setting is described by hard constraints. Alternative x is feasible, if it satisfies the set of hard constraints

$$
X = \left\{x: h (x) = 0 \right\},\tag{2}
$$

where $X \subset R^{n}$ , h is the vector function, $h: R^{n} \to R^{k}$ , and O is the null k-vector.

An alternative which is feasible and acceptable to DM m is called an m-feasible alternative. The set of m-feasible alternatives is

$$
X _ {m} (t) = \left\{\boldsymbol {x}: \boldsymbol {x} \in X \wedge \mathbf {g} _ {m} (\boldsymbol {x}) \geq \boldsymbol {a} _ {m} (t) \right\}.\tag{3}
$$

The compromise decision is an alternative which is m-feasible for every $m \in M$ . Thus, the intersec-

![](/api/attachments/KTUMB74S/fulltext/images/eef64e96bf5b020620ecd4ccd8a698ce36f17113df5dbc47861d18e9cc65f5e4.jpg)  
a. Empty $M$ -feasible set  
Fig. 1. m-feasible and M-feasible sets.

tion of m-feasible sets

$$
X (t) = \bigcap_ {m \in M} X _ {m} (i),
$$

(4)

b. Non-empty M-feasible set  
![](/api/attachments/KTUMB74S/fulltext/images/72e70ad896726beb0fe5512cdb1bb881f031bb0b982b2f6ded47d678b2e8c984.jpg)

is the compromise set also called the set of M-feasible alternatives at the moment t. Depending on the aspiration levels defined by decision-makers, $X(t)$ can be an empty or a non-empty set. The two cases are presented in fig. 1. The soft constraints of decision-makers: DM 1, DM 2 and DM 3 are respectively $s_{1}$ , $s_{2}$ and $s_{3}$ . In fig. 1a the M-feasible set is empty. Changes of the soft constraints of the three decision-makers lead to non-empty M-feasible set, as indicated in Fig. 1b.

Usually decision-makers define such aspiration levels at the beginning of the decision process in which the M-feasible set is empty. In this case they lower some or all of their aspiration levels to expand the m-feasible sets. Expansion of the sets does not mean that some alternatives may not be dropped. However, new alternatives have to be added, so that eventually the expansion process leads to a non-empty M-feasible set. The expansion process is presented in fig. 2a. DM 1 added new alternatives to his/her feasible set. DM 2, through redefining the aspiration level, dropped some old alternatives and added new ones; DM 3 did not change his/her feasible set.

When the M-feasible set is non-empty, the negotiating problem is to choose one element from it. Faced with this choice, decision-makers will increase their aspiration levels to contract the compromise set to a single point. By contraction we mean the dropping of some alternatives in the M-feasible set. The addition of new alternatives is also possible, but repeated contraction leads to a one-element set - a compromise. The contraction is presented in fig. 2b. Comparing the M-feasible sets in fig. 1b and in fig. 2b we can see that some new alternatives have been added and some old ones dropped. This was caused by changes in the aspiration levels introduced by DM 2 and DM 3.

![](/api/attachments/KTUMB74S/fulltext/images/69947b3364b859ab5ab9957993f342ed4eea83af31fc203ec82314d990c4eacf.jpg)  
Fig. 2. The process of changes of m- and M-feasible sets.

From the above, it is clear that the group decision-making process is an iterative process of changes in aspiration levels aimed at achieving a compromise or a deadlock. The process is controlled by decision-makers and changes in aspiration levels reflect the decision-makers' attitudes to maximizing objective performance levels, their understanding of fairness and equity, their applied strategy and their evaluation of unused resources for a given alternative. One should note here that if decision-makers take into account only objective performance levels, the utility approach is appropriate.

## 3. The Interactive Procedure

Group decision-making can be considered as a two-stage process. In the first stage (for t = 0) one or more decision-makers formulate a compromise proposal, i.e., an alternative which he/she considers a possible compromise. Since this is an individual decision of a decision-maker, we do not consider this stage here. A decision-maker may use any procedure in individual decision-making.

In the second stage of the process decision-makers interact, make concessions and try to reach consensus. For this stage we present the procedure in a step-by-step manner; the procedure describes group decision-making problems but in this section we do not consider its applications, i.e., we do not consider its computational complexity. If the procedure is to be used to design a group decision support system (GDSS), as we propose in section 4, it is necessary to specify the properties of the functions and algorithms for solving problems formulated in the particular steps. We assume here that the formulated problems can be solved.

We assume that (i) during the first stage decision-makers learn about the problem, and identify some ‘optimal’ alternatives and the initial aspiration levels, (ii) decision-makers exchange information on aspiration levels and/or compromise proposals, and (iii) decision-makers may not want to share with others information about their objectives, about the aspiration levels of all or some of the soft constraints and about the soft constraints in themselves.

The outcome of the first stage is set $N(0)$ ( $N(0) \subset M$ ) of decision-makers who have defined aspiration levels in this stage and sets $X_{m}(0) \neq \varnothing$ , $m \in N(0)$ of m-feasible alternatives.

Step 1. Let $t$ be the iterations index and set $t = 1$ .

Step 2. If $|N(t)| = 1$ ( $|N(t)|$ is the number of decision-makers who have defined aspiration levels at least once in iterations 0, 1, ..., t - 1) then the determined proposal is presented to decision-makers.

If $|N(t)| \geqslant 2$ solving goal programming (GP) problem

$$
\min f (t) = \sum_ {m \in N (t)} L \left(\mathbf {g} _ {m} (\mathbf {x}), \mathbf {a} _ {m} (t)\right)
$$

$$
\mathbf {s . t .} \boldsymbol {x} \in X,\tag{5}
$$

where $L(.,.)$ is a distance function check if

$$
\bigcap_ {m \in N (t)} X _ {m} (t) \neq \varnothing .
$$

Let $(f^{*}(t), x^{*}(t))$ be the optimal solution of (5). The alternative $x^{*}(t)$ fulfils 'as closely as possible' the aspiration levels of all those decision-makers who have defined them in iteration t. We call this alternative an $N(t)$ -compromise proposal. f is the measure of 'distance' between the present state of negotiation and consensus for $|N(t)|$ decision-makers.

If $f^{*}(t)=0$ and $|N(t)|=|M|$ the group has reached consensus. In the last case go to Step 13. Step 3. Formulate and solve $|N(t)|$ GP problems

$\min f_m(t) = L(x, x^*(t))$

$$
\begin{array}{l l} \text { s.t. } & g _ {m} (x) \leq a _ {m} (t), \\ & x \in X, \end{array}\tag{6}
$$

where L(.,.) is a distance function.

Let $(f_{m}^{*}(t), x_{m}^{*}(t))$ be the optimal solution of (6). The alternative $x_{m}^{*}(t)$ is as 'close as possible' to the $N(t)$ -compromise proposal. $f_{m}^{*}(t)$ is the measure of distance between the $N(t)$ -compromise proposal and the m-acceptable alternative.

Step 4. Present the actual state of the group decision process described by $a_{m}(t), x_{m}^{*}(t)$ and $x^{*}(t), m \in N(t)$ to all the decision-makers and ask them to define/redefine their aspiration levels. Let $N'(t + 1)$ be the set of decision-makers who want to define/redefine their aspiration levels. If $N'(t + 1) = \emptyset$ the process has reached deadlock because there is no decision-maker who wants to present a new compromise proposal. If this is the case decision-makers have to choose as a compromise one of the previously determined alternatives, redefine the set of hard constraints, or break the decision process. End.

Step 5. Set $t = t + 1$ and update set $N(t)$ ; $N(t) = N(t - 1) \vee N'(t)$ .

Step 6. Ask DM $m$ ( $m \in N'(t)$ ) if he/she wants to consider the possibility of forming a coalition with the others. If not, go to Step 8.

Step 7. For DM $m$ ( $m \in N'(t)$ ) solve the GP problem

$$
\min \sum_ {n \in N ^ {\prime} (t) / \{m \}} I v _ {n}
$$

$$
\begin{array}{l l} \text { s.t. } & g _ {m} (x) \geq a _ {m} (t), \\ & g _ {n} (x) - v _ {n} = a _ {n} (t), \quad n \in N (t) / \{m \}, \\ & x \in X, \end{array}\tag{7}
$$

where $I$ is $|I_m|$ -vector in which all elements equal 1.

Present to DM m values $(Iv_{n}^{*})$ ( $n \in N(t)/\{m\}$ ), where $v_{n}^{*}$ is part of the optimal solution of (7). If DM m wants to form a coalition with one or more decision-makers from $N(t)$ , present to him/her those aspiration levels which should be changed in order to decrease the distance from his/her m-feasible set to the feasible sets of the chosen decision-makers. One can use here the optimal tableau of (7).

Step 8. DM $m(m \in N'(t))$ is asked to (i) set aspiration levels $a_m(t)$ , (ii) define a set of objectives $J_m(t)$ and, optionally, (iii) set preferences (weights) $w_i(t)$ , $i \in J_m(t)$ , with regard to the objectives.

Step 9. For DM $m(m \in N'(t))$ formulate and solve the GP problem. If DM $m$ does not specify his/her objectives, the problem differs from (6) in replacing $x^{*}(t)$ with $x^{*}(t-1)$ in the objective function. Otherwise solve the GP problem

$$
\begin{array}{r l} f _ {m} (t) & = \left\{P _ {1} L (x, x ^ {*} (t - 1)) \right. \\ & \quad \left. - P _ {2} \sum_ {i \in J _ {m} (t)} w _ {i} (t) g _ {i} (x) \right\} \end{array}
$$

$$
\begin{array}{l l} \text { s.t. } & g _ {m} (x) \geq a _ {m} (t), \\ & x \in X, \end{array}\tag{8}
$$

where $P_{1} \gg P_{2}$ .

The optimal solution $f_{m}^{*}(t)$ , $x_{m}^{*}(t)$ is m-feasible and ‘as close as possible’ to the compromise proposal. If there are more much solutions, the one that meets DM m objectives on the highest levels is chosen.

We assume here that DM m formulates aspiration levels which are feasible to achieve. However, it is possible to remove this assumption and accordingly modify problem (8).

Step 10. Present DM m with $f_{m}^{*}(t)$ , $x_{m}^{*}(t)$ and ask if he/she wants to redefine his/her aspiration levels. If the answer is yes, return to Step 6.

Step 11. Calculate the coefficients of changes in the group and the individual distance from the compromise proposal,

$$
\begin{array}{l} d (t) = f ^ {*} (t - 1) / f ^ {*} (t - 2) \\ \text { and   for } m: f _ {m} ^ {*} (t - 1) \neq 0, \\ d _ {m} (t) = f _ {m} ^ {*} (t) / f _ {m} ^ {*} (t - 1). \quad m \in M. \end{array}
$$

Coefficient $d(t)$ describes the effects of concessions made by the group in two consecutive iterations. Coefficient $d_{m}(t)$ describes the change in the DM m position caused by his/her concessions and/or by the concessions of others in two consecutive iterations. When $d_{m}(t) > (<)$ 1 DM m has increased (decreased) his/her relative distance from the compromise. One should note that the coefficient describes the distance in relation to the current state of the decision process. Thus, it may happen that DM m made effective concessions with regard to a previous compromise proposal but the others made such concessions that the $d_{m}(t) > d_{m}(t-1)$ . It may also happen that DM m did not change his/her aspiration levels in iteration t-1 but, because of the changes made by others, his/her position improved, i.e., $d_{m}(t) < d_{m}(t-1)$ .

Step 12. Present coefficients $d(t)$ and $d_m(t)$ , $m \in M$ to all decision-makers and go to Step 2.

Step 13. The group has reached consensus; a non-empty M-feasible set has been determined. If the set has more than one element the procedure can be continued or any solution from the set can be chosen. The latter seems reasonable when an M-feasible set has no alternatives which decision-makers evaluate differently. To check if this is the case, we may solve an optimization problem for each decision-maker – a problem with the objective function determined by the decision-maker's objectives and with an M-feasible set as the set of feasible solutions.

If decision-makers evaluate optimal solutions of the outlined problems and do not agree on a compromise, the decision process is continued, but now decision-makers are asked to increase their aspiration levels. This should lead to contraction of the M-feasible set until a set of compromise alternatives which are acceptable to decision-makers is found.

Remark 1. If, in the step 2, $f^{*}(t) = 0$ , i.e., the intersection of sets $X_{m}(m \in N(t))$ is non-empty, $|N(t)|$ decision makers have reached consensus. They may form a coalition and from now on act as one decision-maker. Inclusion of the process of forming a coalition in the procedure requires updating of the set $M$ , and incorporating, in the objective function (5), weights reflecting coalition's size. To simplify the notation we may assume, that in the consecutive iterations the coalition members choose the same soft constraints and input the same RHS values. Thus, the power of the coalition, measured by its influence on the M-compromise proposal determined in (5), is defined by its size. A decision-maker leaves coalition when his/her compromise proposal (determined in (6)) is different from the proposals of other coalition members.

Remark 2. It is assumed that decision-makers may also use other information than the one obtained from the procedure. They may communicate with other means than those given in step 4, e.g., in forming a coalition decision-makers may define a common strategy by choosing soft constraints and aspiration levels for several consecutive iterations.

Remark 3. The procedure can be used for group decision-making with a compromise determined by a given number of decision-makers (e.g., a majority). If this is the case, we have to verify, in Steps 2 and 7, whether there is a sufficient number of decision-makers who have reached consensus and then accordingly either we choose the alternative they accept as the compromise or we continue the process.

## 4. Group Decision Support

The procedure described in Section 3 can be used in designing a GDSS. The system that can be developed for certain group decision-making problems depends on the available software for solving optimization problems. We took a similar approach in the development of the system NEGO [9]. NEGO was designed for a mainframe computer IBM 370/148. Experiments with NEGO and its verification in solving real-life problems showed shortcomings which provided feedback for the proposed procedure. We consider the procedure not flexible and open than the one on which NEGO is based. It makes it possible to support problems with a discrete set of alternatives, to assist in forming coalitions and give additional information with regard to decision-makers' relative positions. The procedure does not require decision-makers to unveil their objectives, and, contrary to NEGO, it allows independent calculations for each decision-maker separately. Decision-makers may formulate their proposals simultaneously, as in NEGO, but they can also formulate proposals subsequently, one after another, or subgroup after subgroup, either in a predetermined order or not. Thus, the procedure makes it possible to design a distributed GDSS.

![](/api/attachments/KTUMB74S/fulltext/images/1144a0a4efe13996d39be3509e44fc4e76ec46ab05e05406698dc4b1a58078b4.jpg)  
Fig. 3. Configuration of GDS1.

The distributed GDSS called Group Decision Support 1 (GDS1), based on the procedure for a network of microcomputers, has been developed. The system also provides support to decision-makers in individual decision-making; e.g., decision-makers can analyze the problem, search for acceptable or optimal or optimal alternatives and verify the impact of weights and aspiration levels on the values of decision variables. A decision-maker can use GDS1 as a tool supporting individual decision-making not only while he/she is preparing for negotiations, but also during the group decision process. The simplest case, i.e., when all functions are linear or can be represented as linear, is considered.

The configuration of GDS1 is presented in fig. 3. The system is designed to work on several IBM-compatible microcomputers in a network, with one micro serving all the others. This microcomputer may be considered as a service machine; it serves the micros used by decision-makers.

The database describing the decision problem (e.g., hard constraints and some or all soft constraints) and the programs of the procedure is set up on the service machine. Programs containing algorithms used for solving individual decision problems are set up on microcomputers used by decision-makers. The database contains information available to all decision-makers. Thus, if required, it is downloaded to the machines used by individual decision-makers and these machines may be used in a stand-alone mode (see Fig. 3). The machine is used in this mode when a decision-maker uses the modules of GDS1 which support individual decision-making. This can be done in any iteration of the decision process.

Once a decision-maker has determined feasible and acceptable aspiration levels and is convinced that these levels secure his/her interests, the information on soft constraints, weights and criteria is sent to the service machine and used to create and solve problems (5) and (7). The optimal solutions are send back to the individual machines and problems (6) and (8) are created and solved.

The information used to determine a compromise proposal of DM m is not available to others. Other decision-makers obtain compromise proposal of DM m in terms of their soft constraints together with the values of decision variables x.

Decision-makers use the integrated spreadsheet package LOTUS 1-2-3 as the interface with programs solving individual decision problems and with the programs residing in the service machine (written in Microsoft QuickBasic 2.0). LOTUS 1-2-3 is also the interface with a graphical input/output program. Part of the information sent by the service machine to decisionmakers is also input into the worksheet. The worksheet is used as a 'window' environment; it is divided into parts which can be accessed from the customized LOTUS 1-2-3 menu. One part of the worksheet is used for hard constraints description, another for soft constraints. If the user wants to determine m-feasible alternatives, or alternatives which are as close as possible to his/her aspiration levels, he/she uses a part of the worksheet which is restricted to individual decision-making. All the compromise proposals are input to the still another part of the worksheet. Also, the history of the decision process (individual and group) is recorded in the worksheet.

Other information, like decision-makers' comments, proposals for forming coalitions, requests for concessions, etc., may be sent directly to the user with the help of a communication package. GDS1 is used on the IBM Token Ring Network and decision-makers may use the IBM TRN Message System to pass information which is not included in the GDS1 (e.g., comments suggestions, remarks). The outline of the system is given in fig. 4.

![](/api/attachments/KTUMB74S/fulltext/images/d2e6df098b0ce5f18c26df754465236495078ca1f7da7c7972f6e2a544213b7d.jpg)  
Fig. 4. Outline of GDS1 system.

Fig. 4 shows the system's input and output, the modules which are set up in the user's machine, and the modules set up in the service machine. This machine can be used by the group 'facilitator' who controls the whole decision process, or by a mediator. Such a user can be supported by LOTUS in a similar way to the decision-makers. He/she can also have the prerogative to ask particular decision-makers to define their aspiration levels and to make concessions.

## 5. An Example

GDS1 was tested and experimentally used in simulation of negotiations between management and trade unions. The example was adapted from the problem of managerial compensation planning [19, pp. 504–513]. While an individual decision problem with one decision-maker having many objectives is considered in [19], here we discuss a problem with two decision-makers having one or more objectives or aspirations.

The negotiating problem involves the determination of an average increase in salaries for four groups of unionized employees and for two groups of management; each group belongs to a different job class. All possible soft constraints representing the interests of the management and the union are given in table 1. The present budget, salaries and the level of violation of relative job worth are also given in table 1. In general, the management is interested in: keeping the budget increase within limits, achieving a large reserve, and changing the structure of salaries, so that it would reflect the relative job worth. The union wants to increase the average salary for each of the unionized groups and to limit the reserve for individual salary adjustment.

An example of negotiation between the two parties using GDS1 is given in fig. 5. The left side of the figure presents the input and output of the management, and the right side presents that of the trade union. Input and output for iterations during which decision-makers independently analyze the problem and evaluate the alternatives, are represented by a screen divided into three parts describing: (i) the names of the soft constraints; (ii) the decision-maker's input (weight, signs of inequalities or criteria and aspiration levels); and (iii) the solution of the problem. Two such iterations for both decision-makers are presented in fig. 5, in the first two rows of screens.

Table 1  
Soft constraints used by the management and trade union in negotiations. $^{a}$

<table><tr><td>Name</td><td>Description</td><td>Present value</td></tr><tr><td colspan="3">Management: DM 1</td></tr><tr><td>BUDGET $</td><td>The total budget (salaries and reserve)</td><td>714.00</td></tr><tr><td>RESERVE $</td><td>The reserve for individual salary adjustment</td><td>0.0</td></tr><tr><td>BUDGET INCR $</td><td>The percentage of budget increase</td><td>-</td></tr><tr><td>AVG MGT INCR $</td><td>The average salary increase for the two non-unionized groups (i.e., management)</td><td>-</td></tr><tr><td>AVG VIOL OF RW</td><td>The average violation of relative job worth for the six job classes</td><td>3.87</td></tr><tr><td>TOT AVG INCR $</td><td>The average salary increase per one employee</td><td>-</td></tr><tr><td colspan="3">Trade Union: DM 2</td></tr><tr><td>SALARY 1</td><td>Average salary of the first unionized group</td><td>48.00</td></tr><tr><td>SALARY 2</td><td>Average salary of the second unionized group</td><td>29.00</td></tr><tr><td>SALARY 3</td><td>Average salary of the third unionized group</td><td>31.00</td></tr><tr><td>SALARY 4</td><td>Average salary of the fourth unionized group</td><td>18.50</td></tr><tr><td>RESERVE $</td><td>The reserve for individual salary adjustment</td><td>0.0</td></tr><tr><td>AVG SAL INCR $</td><td>Average salary increase per unionized employee</td><td>-</td></tr></table>

$^{a}$ All figures except BUDGET INCR % and AVG VIOL OF RW are in thousands of dollars.

A decision-maker does not have input feasible aspiration levels. In the first iteration, the management required that the reserve be greater than \$60,000, the budget be less than \$800,000, and the level of the average violation of relative worth be the minimum (for the given hard constraints the minimum level is 0.25). Because these requirements cannot be satisfied simultaneously, the budget in the proposed alternative is greater than the management's aspiration level.

![](/api/attachments/KTUMB74S/fulltext/images/c8f7a9ba98ff093e7d6a3ffc2252d5a0a790f387828aa84bf5aabba0f8ffda14.jpg)  
Fig. 5. An example of the use of GDS1 in negotiation between the management and trade union.

When decision-makers are satisfied with the alternatives obtained, the information used to determine these alternatives is sent to the service machine (see fig. 4), and the compromise proposals are determined. In the earlier version of GDS1, a decision-maker was not required to send feasible aspiration levels to prepare his/her compromise proposal. This kind of flexibility appeared to be a drawback; some users of GDS1 realized that by using infeasible aspiration levels they could manipulate M-compromise proposals. Therefore, the present version of GDS1 requires a decision-maker to proposage a compromise only if his/her aspiration levels are feasible, i.e., a feasible alternative producing these levels.

After a M-compromise is determined, and if it does not fulfil the aspiration levels of all decision-makers, individual proposals are calculated. For each decision-maker, problem (6) is created and solved. The solution of this problem is presented to all decision-makers. The third row of screens given in fig. 5 contains compromise proposals (in fig. 5, the M-compromise proposal is called GDS1). Comparing these proposals, we can see that the major issue in this negotiation is the distribution of \$20,000. The management wants to obtain a reserve of \$40,000 and a budget of \$810,000. The proposal of the union is within the budget, but the reserve is reduced to \$20,000. The union would obviously like to distribute the difference (\$20,000) among the unionized members.

GDS1 tries to satisfy both parties and to violate the weighted aspirations of both sides as little as possible. It increases the reserve proposed by the union by \$5,420 but distributes the remaining \$14,580 among the salaries. It seems, at first glance, as if GDS1 has treated the union more favorably than the management. Let us note, however, that, apart from monetary considerations, the management is also interested in reducing the violations of relative job worth. The average violation of relative job worth in the union proposal is equal to 2.28, compared with 1.9 in the GDS1 proposal and 1.9 required by the management. GDS1 uses the amount of \$14,580 to increase salaries but in such a way that the management's requirement is fulfilled.

The union (management) analyzes the proposals and introduces changes in the soft constraints. Then it may use the individual decision-making module to verify the impact of these new requirements on the decision alternatives, or it may submit the requirements to the service machine. In the first case, the union (management) will obtain an alternative which fulfils its requirements as closely as possible (as in the first two rows of screens in fig. 5). In the second case, it will obtain a new M-compromise proposal and the compromise proposal of the other party, providing that the other party also submitted its requirements.

## 6. Comments

We have presented here an approach to designing group decision support procedures and systems. It seems that the approach can facilitate group decision-making problems, which can be described both in terms of hard constraints, and when decision-makers can define their soft constraints. It does not decrease decision-makers' freedom of choice and it does not require one constant strategy.

According to the aspiration theory decision-makers make decisions using aspiration levels. This activity is modelled in the procedure. Moreover, the procedure allows incorporation of objectives, if decision-makers can formulate them. It is also possible to use utility functions when known, or to add a module for calculating individual and group utility functions. The flexibility of the approach lies in its ability to allow different decision-makers to use the procedure. Some may agree on the utility approach and try to reach consensus using it; others may negotiate through aspiration levels only. The compromise can be an efficient decision but it can also be a non-efficient one. This depends on the decision-makers' behavior and their strategies.

The existing GDSS were designed by task-driven or technique-driven strategies [6]. We believe GDS1 is an example of an activity-driven design strategy. We considered decision-makers' activities in group decision-making and tried to develop a procedure which would describe these activities. The assumption was that the system should not require other information than that used in real life, but should provide users with new information. Therefore we proposed to calculate coefficients $d(t)$ and $d_{m}(t)$ .

For similar reasons we used a spreadsheet package as the interface. The spreadsheet contains not only an optimal solution, but the optimization model and dual variables as well. Hence the user can manipulate the values of the decision variables (alternative characteristics). This should help him/her in making decisions with regard to aspiration levels. Integrated packages, such as LOTUS 1-2-3, are well known and this may facilitate the use of the system. The package is able to store the history of the decision process (alternatives, coefficients) and the user can consider this in decision-making. Since users work independently and the presence of a facilitator or a mediator is not required, familiarity with the interface seems to be important.

## References

[1] G. DeSanctis and R.B. Gallupe, 1987, A Foundation for the Study of Group Decision Support Systems, Management Science 33, No. 5, 589–609.

[2] R. Fisher and W. Ury, 1983, Getting to Yes. Negotiating Agreement Without Given In (Penguin Books, New York).

[3] F. Fogelman-Soulie et al., 1983, Bivariate Negotiations as a Problem of Stochastic Terminal Control, Management Science 29, No. 7, 840–955.

[4] M. Freimer and P. Yu, 1976, Some New Results on Compromise Solutions for Group Decision Problems, Management Science 22, No. 11, 688–693.

[5] G.H. Haines and B.T. Ratchford, 1983, A Theory of How Intransitive People Make Decisions, Advances and Practices of Marketing Science, Proceedings of ORSA/TIMS Marketing Science Conference, F.S. Zufryden, ed., Univ. of Southern California.

[6] G.P. Huber, 1984, Issues in the Design of Group Decision Support Systems, MIS Quarterly 7, No. 2, 195–204.

[7] H. Isermann, 1985, Interactive Group Decision Making

by Coalitions, in: M. Grauer and A.P. Wierzbicki, eds., Interactive Decision Analysis, (Springer-Verlag, Berlin).

[8] M. Jarke, M.T. Jelassi and M.F. Shakun, 1987, MEDIATOR: Towards a Negotiation Support System, European Journal of Operational Research 31, 314–334.

[9] G.E. Kersten, 1985, NEGO - Group Decision Support System, Information and Management 8, No. 5, 237–246.

[10] G.E. Kersten, 1987, On Two Roles Decision Support Systems Can Play in Negotiations, Information Processing and Management 23, No. 5, 605–614.

[11] G.E. Kersten and T. Szapiro, 1986, Generalized Approach to Modelling Negotiations, European Journal of Operational Research 26, No. 1, 142–149.

[12] C.W. Kirkwood, 1979, Pareto Optimality and Equity in Social Decision Analysis, IEEE Transactions on Systems, Man, and Cybernetics 9, No. 2, 89–91.

[13] J.G. March, J.G. and H.A. Simon, 1958, Organizations (Willey, New York).

[14] D. Maclean, 1985, Rationality and Equivalent Redescrptions, in: M. Grauer et al., eds., Plural Rationality and Interactive Decision Processes (Springer-Verlag, Berlin).

[15] H. Nakayama et al., 1979, Methodology for Group Decision Support with an Application to Assessment of Residential Environment, IEEE Transactions on Systems, Man, and Cybernetics 9, No. 9, 477–485.

[16] H. Raiffa, 1982, The Art and Science of Negotiation (Harvard Univ. Press, Cambridge, MA).

[17] H. Schaffers, 1985, Design of Computer Support for Multicriteria and Multiperson Decisions in Water Resource Planning, in: G. Fandel and J. Spronk, eds., Multiple Criteria Decision Methods and Applications (Springer-Verlag, Berlin).

[18] M.F. Shakun, 1981, Formalizing Conflict Resolution in Policy Making, International Journal of General Systems 7, 207–215.

[19] R.E. Steuer, 1986, Multiple Criteria Optimization: Theory, Computation, and Application (Wiley, New York).

[20] R. Tietz and O.J. Barbos, 1983, Balancing of Aspiration Levels as Fairness Principle in Negotiations, in: R. Tietz, ed., Aspiration Levels in Bargaining and Economic Decision Making (Springer-Verlag, Berlin).

[21] A. Tversky and D. Kahnemann, 1981, The Framing of Decisions and the Psychology of Choice, Science 211, 453–458.

[22] R.E. Wendel, 1980, Multiple Objective Mathematical Programming with Respect to Multiple Decision Makers, Operations Research 28, 1100–1111.

[23] O.R. Young, 1975, Bargaining. Formal Theories of Negotiation (Univ. of Illinois Press, Urbana, IL).
