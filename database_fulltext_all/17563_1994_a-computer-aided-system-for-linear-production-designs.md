---
otero_id: 17563
otero_key: "PZA6N3HE"
title: "A computer-aided system for linear production designs"
authors: "Yong Shi; Po L. Yu; Changqing Zhang; Dazhi Zhang"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90012-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A computer-aided system for linear production designs \*

Yong Shi

University of Nebraska at Omaha, Omaha, NE 68182, USA

Po L. Yu

University of Kansas, Lawrence, KS 66045, USA

Changqing Zhang

University of Kansas, Lawrence, KS 66045, USA

and

Dazhi Zhang

Iona College, New Rochelle, NY 10801, USA

Given a design problem of production systems with multiple criteria and multiple levels of resource availability, we want to select the best subset from a set of possible products as the optimal production system for production and to construct the corresponding optimal contingency plans for coping with the changes of decision parameters. In this paper, by using the multi-criteria and multi-constraint-level (MC $^{2}$ ) simplex method, we develop a computer-aided system for identifying the optimal production systems and their corresponding optimal contingency plans for production.

Keywords: MC $^{2}$ -Simplex method; Optimal linear production systems; Optimal contingency plans; Augmented model; Solution procedure; Computer-aided system

## 1. Introduction

To select (design) an optimal linear production system means to select the best subset of products from a set of possible products for commitment which may include building the facility and distribution channels, production, marketing, and making profit. If a given problem of linear production systems has a single criterion and a single resource availability level, then it can be solved by using linear programming (see Koopmans [11], Charnes and Cooper [2], and Churchman [4]). If a

![](/api/attachments/PZA6N3HE/fulltext/images/366b87306e067a96cfaf112504805f87ce7eda8536b367756682b0ef6167e037.jpg)

Yong Shi is Assistant Professor of ISQA at the College of Business Administration, the University of Nebraska at Omaha. He received his B.S. in mathematics from the Southwestern Petroleum Institute, China in 1982 and a Ph.D. in management science from the University of Kansas in 1991. His Ph.D. dissertation title is "Optimal Linear Production Systems: Models, Algorithms, and Computer Support Systems." In 1983 he studied at the Chinese National Center for

Industrial Science & Technology Management Development cosponsored by China and the United States. Dr. Shi's current research interests are optimal production system designs, multiple criteria decision making, multiple criteria decision support systems. He has published in various journals including Management Science, Operation Research Letters, Computer and Operations Research, Mathematical and Computer Modelling, and Decision Support Systems. He is a member of DSI, ORSA, and TIMS.

![](/api/attachments/PZA6N3HE/fulltext/images/885a7cf78d991bd4c25827ab23538f4e2231bdbc1215a648fbc40de79ebd40be.jpg)

Po L. Yu has been the Carl A. Scupin Distinguished Professor in the School of Business at the University of Kansas, since 1977. He graduated from the National Taiwan University in 1963 and received his Ph.D. in operations research and industrial engineering from the Johns Hopkins University in 1969. Before taking up his position in Kansas, he taught at the University of Rochester and the University of Texas at Austin. In addition to optimal design problems, his research interests have included optimal control, differential games, multiple criteria decision making and system science in areas related to human behavior such as psychology and philosophy. He has published six books and over seventy professional articles.

![](/api/attachments/PZA6N3HE/fulltext/images/ad9a126d179ef196b2260685b3f0ec55b102d25a75582d3dd181b7b9f62c1cce.jpg)  
Fig. 1. A general procedure of selecting optimal linear production systems.

given problem of linear production systems has multiple criteria and a single resource availability level, then it can be solved by using De Novo programming (see Zeleny [20,21]). However, many problems of selecting optimal linear production systems involve multiple criteria and multiple levels of resource availability. The selected production system, for instance, must maximize the total profit, cash flow, and market share, etc. subject to

![](/api/attachments/PZA6N3HE/fulltext/images/feaa17cf237972bcb544e39d13b8e355630b2378ebde9212bc4db9ffe8a9e756.jpg)  
interference.

Changqing Zhang is a Ph.D. candidate in the Department of Economics at the University of Kansas. He received his M.S. in Mathematics from Beijing Normal University, China. He currently works on his dissertation which uses fuzzy linear binary regression to deal with censored data. His research interests are preference framework, subjective inference, operations research, game theory, fuzzy sets, artificial intelligence and the process of censored data with human

![](/api/attachments/PZA6N3HE/fulltext/images/4fdbeda2baaecdfb048773f8bb7be728a8974c8d4b09ea71ad34c9c4441bdc22.jpg)

Dazhi Zhang is Assistant Professor of Management Science and Systems at the Hagan School of Business, Iona College. He received his M.S. in Mathematics from Beijing Normal University, China and Ph.D. in Business from the University of Kansas. His current interests in research include optimal production system design, competence set analysis and forming winning strategies, expert systems and artificial intelligence, multiple criteria decision making, and fuzzy sets and possibility theory. Dr. Zhang has published more than thirty research articles.

fluctuation of resource availability over situations due to supply, demand, or incomplete information. Given an optimal production system, as the decision parameters (criterion coefficients and resource availability levels) can vary with situations, the corresponding optimal contingency plans must be prepared to cope with the various decision situations.

According to Lee, Shi and Yu [12], Shi [14], Shi and Yu [15], and Shi and Yu [16], the problems of the production systems with multiple criteria and multiple resource availability levels can be solved by using the multi-criteria and multi-constraint-level (MC $^{2}$ ) simplex method, derived by Sciford and Yu [13] and Yu [18] (the difference between the MC $^{2}$ method and the multi-criteria (MC) method of Yu and Zeleny [19] and Yu [18] is that in the right hand side the MC $^{2}$ method has a matrix, while the MC method has a vector). A general procedure of solving the problem of the production systems (see Figure 1) is sketched as follows:

(i) With certain criteria, we first select some good subsets of the possible product set as candidates for optimal production systems.

(ii) We then prepare the corresponding contingency plans for each candidate. Contingency plans may have flexibility to use all possible slack resources, purchase additional resources, or change production mixes to cope with uncertainty or variations of decision parameters.

(iii) We finally select the optimal production systems from the set of candidates and their corresponding contingency plans by considering the expected payoff of these systems and/or using other known techniques of decision making under uncertainty.

Note that preparing contingency plans for a production system differs from postoptimal analysis or sensitivity analysis for vectorparametric programming (see Gal [8]). The purpose of preparing contingency plans is to ensure the feasibility and optimality over decision situations for an undertaken production system, while the postoptimal analysis identifies the new optimal solution of the given system as estimates of some system data become available.

In Lee, Shi, and Yu [12], the MC $^{2}$ -simplex method as a primary tool is used to derive a basic procedure for selecting optimal production systems and their corresponding contingency plans. In this procedure, the subsets of a given possible product set that can optimize the model of production systems under certain changes of decision parameters are first selected as Potentially Good Systems (or simply PGS's) for optimal production systems. Then for each PGS, its related contingency plans are prepared. Finally, by considering the expected payoff and/or using other known techniques of decision making under uncertainty the optimal production systems are selected from the set of all PGS's (candidates) and their corresponding contingency plans. However, the basic procedure uses the only product and slack variables involved in a given PGS for constructing its related contingency plans. It ignores the flexibility to use other slack variables. Also the basic procedure restricts the set of possible candidates for optimal production systems to the set of all PGS's. In Shi [14], the MC $^{2}$ -simplex method is extensively used to develop several procedures for selecting optimal production systems and their corresponding contingency plans. In these procedures, one can not only use the product variables involved in a given PGS and all possible slack variables to flexibly construct the optimal contingency plans for the PGS, but also generate a new linear system that contains products involved in some of the possible unions of subsets of the set of all PGS's as the candidate for optimal production systems. Such a new linear system is called the Generalized Good System (GGS in short), because it generalizes the previous concept of PGS's.

The MC $^{2}$ -simplex method involves five subroutines in each iteration: pivoting, determining primal feasibility and dual feasibility, and determining the effective constraints for the primal parameter set and the dual parameter set [Chapter 8,17]. Developing a data structure for efficient computation of locating all PGS's and GGS's, and their corresponding contingency plans is a challenge. For small problems of selecting optimal production systems, we can use computer software of Chien, Shi and Yu [3]. But for the medium- and large-size problems, the computation and bookkeeping can be enormous. Without an efficient data structure and programs, locating the entire set of PGS's and GGS's and constructing the corresponding contingency plans can be prohibitive. In this paper, we propose a framework to develop a Computer-Aided System (CAS) for solving the problem of selecting optimal production systems. We will address relevant computer programs as well as the related data structure. Note that our focus is on the computer programs and the data structure, not on the geometry of a product design as shown by Dilworth [7] and Heizer and Render [9] using Computer-Aided Design (CAD).

In order to facilitate our discussion, in the next section, we sketch the known results of how to use the MC $^{2}$ -simplex methods to formulate and solve the problem of selecting optimal production systems. Specifically, in section 2.1, we demonstrate how to identify the set of all PGS's for the given production system problem by using the MC $^{2}$ -simplex method. In section 2.2, we outline different mathematical models for constructing the optimal contingency plans for all PGS's and GGS's. In section 3, we study an augmented model for building a theoretical framework for the CAS. The theoretical results are derived to facilitate computation of selecting optimal production systems. In section 4, by integrating the results of sections 2 and 3, we first propose a procedure for solving the problem of selecting optimal production systems (section 4.1). An illustrative example is given in the Appendix. Then we describe the CAS for selecting optimal production systems, in which the flowcharts of the algorithm (section 4.2), a top-down design of the CAS (section 4.3), and a pseudo-language program (section 4.4) are provided. Conclusions and remaining research problems are given in section 5.

## 2. Optimal linear production systems: A preview

## 2.1. Potentially good systems (PGS)

A known mathematical model of selecting optimal linear production systems can be sketched as follows. (For the details, the reader can refer to [12,14,15,16]).

Given a planning horizon, let $N = \{1, \ldots, n\}$ be n products or opportunities under consideration. The model of selecting optimal production systems can be formulated by

$$
\begin{array}{l l} \max & \lambda^ {t} C x \\ \text { s.t. } & A x \leq D \gamma \\ & x \geq 0, \end{array}\tag{M1}
$$

where $C \in R^{qxn}$ is the contribution matrix whose q rows are the coefficients of q criteria; $A \in R^{mxn}$ is the unit consumption matrix of resources; and $D \in R^{mxp}$ is the matrix of resource availability levels whose p columns are p resource availability levels; $x \in R^{n}$ is the product variables; and both $\gamma$ , called the resource parameter, and $\lambda$ , called the contribution parameter, are normalized; that is,

$$
\gamma \in R ^ {p} \text { with } \gamma_ {k} \geq 0 \text { and } \sum_ {k = 1} ^ {p} \gamma_ {k} = 1
$$

$$
\text { and } \lambda \in R ^ {q} \text { with } \lambda_ {k} \geq 0 \text { and } \sum_ {k = 1} ^ {q} \lambda_ {k} = 1.
$$

Observe that with the above model, if parameters $(\gamma, \lambda)$ are known ahead of decision time, we can select the best k products from possible n products as the optimal system for production by employing linear programming techniques (see [2] and Dantzig [6]). However, when the parameters $(\gamma, \lambda)$ cannot be known ahead of time, the linear programming approach would not be effective because there are infinitely many possible combinations of $(\gamma, \lambda)$ . In addition, the change of $\gamma$ may make the original choice infeasible, and the change of $\lambda$ can render the choice not optimal. Thus, contingency plans need to be prepared to overcome the difficult decision situations. In the following, assuming that $(\gamma, \lambda)$ are unknown we describe how to use the MC $^{2}$ -simplex method to solve the problem of the production systems.

By adding slack variables s (note that we let the contribution coefficients associated with s be

zero) to Model (M1), we obtain the following simplex tableau:

<table><tr><td>x</td><td>s</td><td>RHS</td></tr><tr><td>A</td><td>I</td><td>Dγ</td></tr><tr><td>-λtC</td><td>0</td><td>0</td></tr></table>

(1)

(2)

Note that the first and second block of columns are the coefficients associated respectively with the original and slack variables. Equation (1) represents constraints while equation (2) is the objective function.  
Let $J$ be the index set of the basic variables (without confusion, $J$ is also called a basis). Given a $J$ with the basic variables denoted by $x(J)$ , we define the associated basis matrix $B_{J}$ as the submatrix of $A$ with column index in $J$ (i.e., column $j$ of $A$ is in $B_{J}$ iff $j \in J$ ), and the associated objective function coefficient $C_{J}$ as the submatrix of $C$ with column index in $J$ . Equations (1)-(2) can be rewritten as:

<table><tr><td>x</td><td>s</td><td>RHS</td></tr><tr><td> $B_{J}^{-1}A$ </td><td> $B_{J}^{-1}$ </td><td> $B_{J}^{-1}D\gamma$ </td></tr><tr><td> $\lambda^{t}C_{J}B_{J}^{-1}A - \lambda^{t}C$ </td><td> $\lambda^{t}C_{J}B_{J}^{-1}$ </td><td> $\lambda^{t}C_{J}B_{J}^{-1}D\gamma$ </td></tr></table>

(3)

(4)

Note that (3)-(4) is a typical simplex tableau with $B_{I}$ as a basis, and

(3) $= B_{J}^{-1}\cdot (1)$ (i.e., premultiply (1) by $B_{J}^{-1}$ ), and

(4) $= \lambda^i C_j\cdot (3) + (2).$

(3) and (4) imply that $x(J, \gamma) = B_J^{-1}D\gamma$ is a basic solution associated with $(J, \gamma)$ and its objective value is given by $\lambda^t C_J B_J^{-1}D\gamma$ when $\lambda$ is specified.

By dropping $(\gamma, \lambda)$ from (3)-(4), we obtain a typical MC $^2$ -simplex tableau with basis $B_J$ as follows:

<table><tr><td>x</td><td>s</td><td>RHS</td></tr><tr><td> $B_{J}^{-1}A$ </td><td> $B_{J}^{-1}$ </td><td> $B_{J}^{-1}D$ </td></tr><tr><td> $C_{J}B_{J}^{-1}A - C$ </td><td> $C_{J}B_{J}^{-1}$ </td><td> $C_{J}B_{J}^{-1}D$ </td></tr></table>

(5)

(6)

Definition 2.1. Given a basis $J$ for Model (M1), define its corresponding

(i) primal parameter set by

$$
\Gamma (J) = \{\gamma \geq 0 | B ^ {- 1} D \gamma \geq 0 \}; \text { and }
$$

(ii) dual parameter set by

$$
\begin{array}{l} \Lambda (J) = \{\lambda \geq 0 | \lambda^ {t} [ C _ {J} B _ {J} ^ {- 1} A - C, C _ {J} B _ {J} ^ {- 1} ] \\ \geq 0 \}. \end{array}
$$

The following is well known (see [Pages 243-248 of Chapter 8, 18] for details).

Statement 2.1.

(i) The resulting solution $x(J, \gamma) = B_J^{-1}D\gamma \geq 0$ and $J$ is a feasible basis iff $\gamma \in \Gamma(J)$ .

(ii) The solution $x(J, \gamma)$ is optimal iff $\gamma \in \Gamma(J)$ and $\lambda \in \Lambda(J)$ .

(iii) $J$ is a primal potential basis iff $\Gamma(J) \neq \emptyset$ .

(iv) $J$ is a dual potential basis iff $\mathcal{A}(J)\neq\emptyset$ .

(v) $J$ is a potential basis iff $\Gamma(J) \times \Lambda(J) \neq \emptyset$ .

Note that the condition $\Gamma(J) \times A(J) \neq \emptyset$ in (v) of Statement 2.1 is similar to the critical region of vectorparametric programming (see [Pages 220-231, Chapter 7,8]).

Definition 2.2. The optimal situation set for a given potential basis $J$ is defined by

$$
S (J) = \left\{\left(\gamma , \lambda\right) \mid \gamma \in I ^ {\prime} (J), \lambda \in A (J) \right\}.
$$

By Definition 2.2, whenever $(\gamma, \lambda) \in S(J)$ , $J$ is the optimal basis for Model (M1). When there is no confusion, $S(J)$ may simply be denoted by $S$ .

In order to use the MC $^{2}$ -simplex method to search for all PGS's associated with certain ranges of $(\gamma, \lambda)$ , the following assumptions are imposed in [12] (The assumption will be removed shortly):

Assumption 2.1.

(i) The number of products, k, in each PGS for Model (M1) should not exceed the number of resources under consideration, m.

(ii) The selected k products should be able to “optimize” Model (M1) under some possible range of $(\gamma, \lambda)$ .

Remark 2.1. From (i)-(v) of Statement 2.1, we see that, if a PGS is a potential basis, then it satisfies both (i) and (ii) of Assumption 2.1; conversely, a PGS which satisfies both (i) and (ii) of Assumption 2.1 with some specific $(\gamma, \lambda)$ can be represented by a potential basis. Thus, the method to search for all potential bases by the $\mathbf{MC}^2$ -simplex method can be readily used to search for all PGS's. For this reason, we call a potential basis associated with Model (M1) a potentially good system (PGS) for Model (M1). The products associated with the PGS are those that can be potentially selected for production.

For the ease of presentation, in this paper we assume that for any $(\gamma, \lambda)$ , Model (M1) either has no feasible solution or has a bounded optimal solution. The following example illustrates how to locate all PGS's for a given problem of selecting optimal production systems.

Example 2.1.

$$
\max \left(\lambda_ {1}, \lambda_ {2}\right) \left( \begin{array}{c c c c c} 3 & 2 & 1 & 1 & 0 \\ 0 & 1 & 2 & 3 & 3 \end{array} \right) \left( \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ x _ {5} \end{array} \right)
$$

$$
\mathrm{s.t} \left( \begin{array}{c c c c c} 1 & 0 & 2 & 1 & 0 \\ 0 & 1 & 1 & 2 & 2 \\ 1 & 1 & 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ x _ {5} \end{array} \right) \leq \left( \begin{array}{c c} - 1 0 & 2 0 \\ 4 0 & 2 0 \\ 3 0 & 4 0 \end{array} \right) \binom {\gamma_ {1}} {\gamma_ {2}}
$$

$$
x _ {j} \geq 0, j = 1, 2, 3, 4, 5.
$$

Let $s_1, s_2$ , and $s_3$ be slack variables for constraints 1, 2, and 3 respectively. Then, by using a software of the MC $^{2}$ -simplex method [3], we find the set of all potential bases (or PGS's), denoted by $\mathcal{J} = \{ J_1, J_2, J_3, J_4, J_5 \}$ as listed in Table 1.

In table 1, $J_{1}$ has $(x_{1}, x_{2}, s_{3})$ as the basic variables. If $J_{1}$ is chosen, then products $\{x_{1}, x_{2}\}$ are the ones that we are going to produce while $s_{3}$ is a slack variable. When $\gamma_{1}$ and $\lambda_{1}$ are given, $\gamma_{2}$ and $\lambda_{2}$ are uniquely specified due to $\gamma_{1} + \gamma_{2} = 1$ and $\lambda_{1} + \lambda_{2} = 1$ (For $\gamma \in R^{p}$ and $\lambda \in R^{q}$ with $p, q > 2$ , when $\gamma_{k}, k = 1, \ldots, p - 1$ , and $\lambda_{t}, t = 1, \ldots, q - 1$ , are given, $\gamma_{p}$ and $\lambda_{q}$ can be uniquely specified). From Table 1, we see that $J_{1}$ is optimal whenever $0 \leq \gamma_{1} \leq 2/3$ and $1/5 \leq \lambda_{1} \leq$

Potentially good systems

<table><tr><td>Potentially good system</td><td>Basic variables</td><td> $\Gamma(J_i)$ </td><td> $\Lambda(J_i)$ </td></tr><tr><td> $J_1$ </td><td> $(x_1, x_2, s_3)$ </td><td> $0 \leq \gamma_1 \leq 2/3$ </td><td> $1/5 \leq \lambda_1 \leq 1$ </td></tr><tr><td> $J_2$ </td><td> $(x_1, x_2, x_4)$ </td><td> $0 \leq \gamma_1 \leq 2/3$ </td><td> $1/4 \leq \lambda_1 \leq 1$ </td></tr><tr><td> $J_3$ </td><td> $(x_1, x_2, x_5)$ </td><td> $0 \leq \gamma_1 \leq 2/3$ </td><td> $1/5 \leq \lambda_1 \leq 1/4$ </td></tr><tr><td> $J_4$ </td><td> $(x_1, x_5, s_3)$ </td><td> $0 \leq \gamma_1 \leq 2/3$ </td><td> $1/11 \leq \lambda_1 \leq 1/5$ </td></tr><tr><td> $J_5$ </td><td> $(x_3, x_5, s_3)$ </td><td> $0 \leq \gamma_1 \leq 2/3$ </td><td> $0 \leq \lambda_1 \leq 1/11$ </td></tr></table>

1. However, if $2/3 < \gamma_{1} \leq 1$ , then $J_{1}$ becomes infeasible and if $0 \leq \lambda_{1} < 1/5$ , then $J_{1}$ is not optimal. We need to prepare the corresponding contingency plans for $J_{1}$ when $2/3 < \gamma_{1} \leq 1$ and/or $0 \leq \lambda_{1} < 1/5$ . Similarly, $J_{2}, J_{3}, J_{4}$ , and $J_{5}$ can be explained.

By Definition 2.2, we obtain the following optimal situation sets (where $S(J_i)$ is denoted by $S_i$ for simplicity):

$$
S _ {1} = \{(\gamma_ {1}, \lambda_ {1}) | 0 \leq \gamma_ {1} \leq 2 / 3, 1 / 5 \leq \lambda_ {1} \leq 1 \},
$$

$$
S _ {2} = \left\{\left(\gamma_ {1}, \lambda_ {1}\right) \mid 0 \leq \gamma_ {1} \leq 2 / 3, 1 / 4 \leq \lambda_ {1} \leq 1 \right\},
$$

$$
S _ {3} = \left\{\left(\gamma_ {1}, \lambda_ {1}\right) \mid 0 \leq \gamma_ {1} \leq 2 / 3, 1 / 5 \leq \lambda_ {1} \leq 1 / 4 \right\},
$$

$$
\begin{array}{l} S _ {4} = \left\{\left(\gamma_ {1}, \lambda_ {1}\right) \mid 0 \leq \gamma_ {1} \leq 2 / 3, 1 / 1 1 \leq \lambda_ {1} \leq \right. \\ \left. 1 / 5 \right\}, \text { and } \end{array}
$$

$$
S _ {5} = \{(\gamma_ {1}, \lambda_ {1}) | 0 \leq \gamma_ {1} \leq 2 / 3, 0 \leq \lambda_ {1} \leq 1 / 1 1 \},
$$

where $(\gamma, \lambda)$ defined in S of Definition 2.2 reduce to $(\gamma_{1}, \lambda_{1})$ .

Note that in table 1, PGS $J_1$ overlaps $J_2$ and $J_3$ since $S_1 = S_2 \cup S_3$ . ( $J_j$ is said to overlap $J_i$ , $i \neq j$ , if $\text{int}(S_j) \cap \text{int}(S_j) \neq \emptyset$ , where $\text{int}(S_j)$ is the interior of $S_j$ .) This means when $0 \leq \gamma_1 \leq 2/3$ and $1/5 \leq \lambda_1 \leq 1/4$ , both $J_1$ and $J_3$ are optimal; and when $0 \leq \gamma_1 \leq 2/3$ and $1/4 \leq \lambda_1 \leq 1$ , both $J_1$ and $J_2$ are optimal. From table 1, we also see that when $2/3 < \gamma_1 \leq 1$ , Model (M1) has no feasible solution since the value of the first resource level for the first constraint is negative (which is -10).

Remark 2.2. (i) Given a problem of selecting optimal production systems, let $\mathcal{J} = \{J_1, \ldots, J_g\}$ be the set of all PGS's identified by the MC²-simplex method. Recall that each PGS of $\mathcal{J}$ satisfies both (i) and (ii) of Assumption 2.1. In order to remove or relax this assumption, we can generate generalized good systems (GGS's) by taking unions of subset of given $\mathcal{J}$ (see [14]). An algorithm developed by Shi, Yu, Zhang and Zhang [17] can be applied to efficiently search for all GGS's based on $\mathcal{J}$ .

(ii) Once a PGS J is determined for the production system, then all other products $j \notin J$ are rejected or not produced. Given a PGS J with basic variables $x(J)$ , recall that when $\gamma \notin \Gamma(J)$ , J is not feasible, and when $\lambda \notin A(J)$ , J is not optimal. Thus, we need to prepare the corresponding contingency plans for each J to cope with the difficulties (i.e., to make the production feasible and optimal in some sense) by building the related submodels of Model (M1). We shall outline the methods of constructing the optimal contingency plans for a given PGS (or GGS) in the next subsection.

(iii) Given all PGS's and GGS's together with their corresponding optimal contingency plans, since $(\gamma, \lambda)$ are unknown at the design time, the problem of selecting the final optimal production systems is reduced to a decision problem under uncertainty with a finite number of choices; that is, PGS's and GGS's. Solving this problem involves the assessment of the likelihood of $(\gamma, \lambda)$ to occur at the various points of its range. With proper assumptions, the uncertainty may be represented by random variables with some known probability distribution. A number of known criteria of decision making under uncertainty can be used to solve the problem (see [12], [18], Ziemba and Vickson [22], and Keeney and Raiffa [10]). This is illustrated in the example provided in the Appendix. An analysis of using various criteria to choose the final optimal production systems is referred to [Chapter 4,14].

In the following subsection, we shall sketch the submodels of Model (M1) that can be used in constructing the optimal contingency plans for all PGS's and GGS's for developing the CAS.

## 2.2. Submodels and augmented model

Given the set of all PGS's and GGS's, we may construct two kinds of corresponding optimal contingency plans for each of the PGS's and GGS's. One kind is called the rigid contingency plans and the other kind the flexible contingency plans. By a rigid contingency plan for a candidate (PGS or GGS), we mean that one which contains only those basic variables and slack variable of the candidate and which "optimizes" the sub-model related to the candidate under certain ranges of $(\gamma, \lambda)$ . Note that the rigid contingency plan has no flexibility to use other possible slack variables which are not in the candidate. In contrast, a flexible contingency plan for the candidate can contain not only the selected basic variables, but also some possible slack variables of Model (M1).

Now let us outline all mathematical models involved with constructing the two kinds of optimal contingency plans for each PGS and GGS. We then use an augmented model to integrate them. For the details of building these models, the reader can refer to $[14,15,16]$ .

To construct the rigid contingency plans for a given PGS J, we can solve the following sub-model:

$$
\begin{array}{l l} \max & \lambda^ {t} C _ {J} x (J) \\ \text { s.t. } & B _ {J} x (J) = D \gamma \\ & x (J) \leq 0, \end{array}\tag{M2}
$$

where $C_{J}$ and $B_{J}$ are the submatrices derived respectively from $[C, 0]$ and $[A, I]$ of Model (M1) be deleting those $j \notin J$ , D is known in Model (M1), and $(\gamma, \lambda)$ are presumed.

By using the MC $^{2}$ -simplex method, we can identify the set of potential solutions for Model (M2) which is called the set of rigid contingency plans selected by (M2) for the given PGS J. If for any ( $\gamma$ , $\lambda$ ), there is such a contingency plan which “optimizes” Model (M2), then we say the set of potential solution for Model (M2) is the set of all optimal rigid contingency plans for PGS J. If for some $\gamma$ , Model (M2) has no feasible solution, then the rigid contingency plans that satisfy feasibility and maximize the net payoff for PGS J can be formulated as:

$$
\begin{array}{l l} \max & \lambda^ {t} C _ {J} x (J) - \alpha^ {t} y \\ \text { s.t } & B _ {J} x (J) - y = D \gamma \\ & x (J), y \geq 0, \end{array}\tag{M3}
$$

where $y = (y_{1}, \ldots, y_{m})^{t}$ are the additional resources needed to convert infeasibility of Model (M2) into feasibility and $\alpha^{t} = (\alpha_{1}, \ldots, \alpha_{m})$ is the given unit price of purchasing y.

For a given PGS J, let $\mathcal{K}(J)=\{K_{1}(J),\ldots,K_{h}(J)\}$ be the set of all potential solutions obtained from Model (M3) by using the MC $^{2}$ -simplex method. We call $\{K_{1}(J),\ldots,K_{h}(J)\}$ the rigid contingency plans selected by (M3) for PGS J. Note that by increasing y if necessary, Model (M3) always has feasible solutions. Thus, be using Model (M3) we can always have feasible rigid contingency plans for all possible situations of $(\gamma,\lambda)$ .

If the given candidate is GGS $\Omega$ , then the corresponding rigid contingency plans can be constructed by solving the following submodel:

$$
\begin{array}{l l} \max & \lambda^ {t} C _ {\Omega} x (\Omega) \\ \text { s.t } & A _ {\Omega} x (\Omega) = D \gamma \\ & x (\Omega) \geq 0, \end{array}\tag{M4}
$$

where $C_{\Omega}$ and $A_{\Omega}$ are the submatrices derived respectively from $[C, 0]$ and $[A, I]$ of Model (M1) by deleting those $j \notin \Omega$ , D is known in Model (M1), and $(\gamma, \lambda)$ are presumed.

Given GGS $\Omega$ , let $\{G_1(\Omega), \ldots, G_d(\Omega)\}$ be the set of all potential solutions obtained from Model (M4) by using the MC $^2$ -simplex method. Then, the set $\{G_1(\Omega), \ldots, G_d(\Omega)\}$ is called the set of rigid contingency plans selected by (M4) for a given GGS $\Omega$ . If for any ( $\gamma$ , $\lambda$ ), there is a rigid contingency plan which “optimizes” Model (M4), then $\{G_1(\Omega), \ldots, G_d(\Omega)\}$ is the set of all optimal rigid contingency plans for GGS $\Omega$ . If for some $\gamma$ , Model (M4) has no feasible solution, then the rigid contingency plans that satisfy feasibility and maximize the net payoff for GGS $\Omega$ can be identified by solving the following model:

$$
\begin{array}{l l} \max & \lambda^ {t} C _ {\Omega} x (\Omega) - \alpha^ {t} \gamma \\ \text { s.t. } & A _ {\Omega} x (\Omega) - y = D \gamma \\ & x (\Omega), y \geq 0, \end{array}\tag{M5}
$$

where $\alpha^t = (\alpha_1, \ldots, \alpha_m)$ is the given unit price of purchasing additional resources $y = (y_1, \ldots, y_m)'$ .

Given GGS $\Omega$ , we call the set of all potential solutions obtained from Model (M5) the rigid contingency plans selected by (M5) for $\Omega$ . Note that Model (M5) always has feasible solutions by increasing y if necessary. This means that the rigid contingency plans selected by (M5) can always be feasible for all possible situations of $(\gamma, \lambda)$ . Furthermore, when a proper level of $\alpha$ value is given, the rigid contingency plans selected by Model (M5) for GGS $\Omega$ are the set of all optimal rigid contingency plans for GGS $\Omega$ .

To construct the flexible contingency plans for a given PGS J with basic variables $x(J)$ which may contain some slack variables, we denote the corresponding nonbasic variables by $x(J')$ . Decompose $x(J')$ into $x^{1}(J')$ and $x^{2}(J')$ , where $x^{1}(J')$ is the set of nonbasic slack variables consisting of those slack variables that are not involved in J, and $x^{2}(J')$ is the set of nonbasic product variables consisting of those product variables of N which are not involved in J. Then, we can construct the flexible contingency plans for PGS J by solving the following submodel:

$$
\begin{array}{l l} \max & \lambda^ {t} C _ {J} x (J) \\ \text {s.t.} & B _ {J} x (J) + R ^ {1} x ^ {1} (J ^ {\prime}) = D \gamma \\ & x (J), x ^ {1} (J ^ {\prime}) \geq 0, \end{array}\tag{M6}
$$

where $C_{J}$ and $B_{J}$ are the submatrices of [C, 0] and [A, I] of Model (M1) corresponding to $x(J)$ , $R^{1}$ is the submatrix of [A, I] corresponding to $x^{1}(J')$ , D is known in Model (M1), and $(\gamma, \lambda)$ are presumed.

For a given PGS J, let $\{U_{1}(J),\ldots,U_{r}(J)\}$ be the set of all potential solutions obtained from Model (M6) by using the MC $^{2}$ -simplex method. We call $\{U_{1}(J),\ldots,U_{r}(J)\}$ the flexible contingency plans selected by (M6) for PGS J. If for any $(\gamma,\lambda)$ , there is a contingency plan that “optimizes” Model (M6), then we say $\{U_{1}(J),\ldots,U_{r}(J)\}$ is the set of all optimal flexible contingency plans for PGS J. If for some $\gamma$ , Model (M6) has no feasible solution, then the flexible contingency plans that satisfy feasibility and maximize the net payoff for PGS J can be formulated as:

$$
\begin{array}{l l} \max & \lambda^ {t} C _ {J} x (J) - \alpha^ {t} y \\ \text {s.t.} & B _ {J} x (J) + R ^ {1} x ^ {1} (J ^ {\prime}) - y = D \gamma \\ & x (J), x ^ {1} (J ^ {\prime}), y \geq 0, \end{array}\tag{M7}
$$

where $y = (y_{1}, \ldots, y_{m})^{t}$ are the needed additional resources that can be purchased by paying $\alpha^{t} = (\alpha_{1}, \ldots, \alpha_{m})$ for each unit.

Given a PGS J, we call the set of all potential solutions obtained from Model (M7) by using the MC $^{2}$ -simplex method the flexible contingency plans selected by (M7) for PGS J. Note that by increasing y if necessary, Model (M7) always has feasible solutions. Thus, by using Model (M7) we can always have feasible flexible contingency plans for all possible situations of ( $\gamma$ , $\lambda$ ).

If a GGS $\Omega$ with basic variables $x(\Omega)$ is given as a candidate, then we denote the corresponding non-selected product variables and slack variables by $x(\Omega')$ . We decompose $x(\Omega')$ into $x^{1}(\Omega')$ and $x^{2}(\Omega')$ , where $x^{1}(\Omega')$ is the set of non-selected slack variables and $x^{2}(\Omega')$ is the set of non-selected product variables with respect to $\Omega$ . The flexible contingency plans for given GGS $\Omega$ can be identified by solving the following sub-model:

$$
\begin{array}{l l} \max & \lambda^ {t} C _ {\Omega} x (\Omega) \\ \text { s.t. } & A _ {\Omega} x (\Omega) + A _ {\Omega^ {\prime}} ^ {1} x ^ {1} (\Omega^ {\prime}) = D \gamma \\ & x (\Omega),   x ^ {1} (\Omega^ {\prime}) \geq 0, \end{array}\tag{M8}
$$

where $C_{\Omega}$ and $A_{\Omega}$ are respectively the submatrices of $[C,0]$ and $[A,I]$ of Model (M1) corresponding to $x(\Omega)$ , $A_{\Omega'}^{1}$ is the submatrix of $[A,I]$ corresponding to $x^{1}(\Omega')$ , D is known in Model (M1), and $(\gamma, \lambda)$ are presumed.

Given GGS $\Omega$ , let $\{E_1(\Omega), \ldots, E_c(\Omega)\}$ be the set of all potential solutions obtained from Model (M8) by using the MC $^2$ -simplex method. Then, we call $\{E_1(\Omega), \ldots, E_c(\Omega)\}$ the flexible contingency plans selected by (M8) for GGS $\Omega$ . If for any ( $\gamma, \lambda$ ), there is a flexible contingency plan that “optimizes” Model (M8), then $\{E_1(\Omega), \ldots, E_c(\Omega)\}$ is the set of all optimal flexible contingency plans for GGS $\Omega$ . If for some $\gamma$ , (M8) has no feasible solution, then the flexible contingency plans which maintain feasibility and maximize the net payoff for GGS $\Omega$ can be constructed by solving the following model:

$$
\begin{array}{l l} \max & \lambda^ {t} C _ {\Omega} x (\Omega) - \alpha^ {t} y \\ \text { s.t. } & A _ {\Omega} x (\Omega) + A _ {\Omega^ {\prime}} ^ {1} x ^ {1} (\Omega^ {\prime}) - y = D \gamma \\ & x (\Omega), x ^ {1} (\Omega^ {\prime}), y \geq 0. \end{array}\tag{M9}
$$

where $y = (y_{1}, \ldots, y_{m})^{t}$ are the needed additional resources and $\alpha^{t} = (\alpha_{1}, \ldots, \alpha_{m})$ is the given unit price of purchasing y.

Given GGS $\Omega$ , we call the set of all potential solutions obtained from Model (M9) the flexible contingency plans selected by (M9) for $\Omega$ . Note that by increasing y if necessary, the submodel (M9) always has feasible solutions; that is, the flexible contingency plans selected by (M9) can always be feasible for all possible situations of $(\gamma, \lambda)$ . Furthermore, these contingency plans can ensure both the feasibility and optimality if a proper value of the price $\alpha$ is chosen.

Because of the close relationship among Models (M2)-(M9) and the initial model (M1), the augmented model developed in [11] can be used to facilitate effective computation of locating all PGS's and GGS's and their corresponding contingency plans.

In the augmented model we try to identify the potential bases from both product variables of x and the additional resource variables of y. The model is given as follows:

$$
\begin{array}{l l} \max & \lambda^ {t} C x - \alpha^ {t} y \\ \text { s.t. } & A x - y \leq D \gamma \\ & x, y \geq 0. \end{array}\tag{AM}
$$

We observe that all Models (M1)-(M9) are submodels of Model (AM).

First let us add slack variables s to Model (AM); then we observe:

(i) We can obtain Model (M1) by deleting the columns of y from Model (AM). Thus Model (M1) is a submodel of Model (AM).

(ii) From Model (AM), we can obtain Model (M2) by deleting the columns of both $x(J')$ and y, Model (M3) by deleting the columns of $x(J')$ , Model (M4) by deleting the columns of both $x(\Omega')$ and y, and Model (M5) by deleting the columns of $x(\Omega')$ . Thus, Models (M2)–(M5) are submodels of Model (AM).

(iii) From (AM), we can obtain Model (M6) by deleting the columns of both $x^2(J')$ and $y$ , Model (M7) by deleting the columns of $x^2(J')$ , Model (M8) by deleting the columns of both $x^2(\Omega')$ and $y$ , and Model (M9) by deleting the columns of $x^2(\Omega')$ . Thus, Models (M6)-(M9) are also sub-models of Model (AM).

The above discussion indicates that developing an effective procedure to solve the augmented model (AM) is the key to developing a CAS for selecting optimal production systems. We shall study properties of Model (AM) in the next section.

## 3. Some theoretical results for the augmented model

For convenience, we rewrite Model (AM) as follows:

$\max \lambda^t [C, - \mathbb{1}_q\alpha^t ]\binom{x}{y}$

$$
\text { s.t. } \quad [ A, - I ] \binom {x} {y} \leq D \gamma
$$

$$
\binom {x} {y} \geq 0.
$$

$$
\text { Let } \mathbb {C} (\alpha) = \left[ C, - \mathbb {1} _ {q} \alpha^ {t} \right], \mathbb {A} = [ A, - I ],
$$

and $\chi=\begin{pmatrix}x\\y\end{pmatrix}.$

Then, Model (AM) becomes

$$
\begin{array}{l l} \max & \lambda^ {t} \mathbb {C} (\alpha) \chi \\ \text { s.t. } & \mathbb {A} \chi \leq D \wedge \\ & \chi \geq 0. \end{array}\tag{7}
$$

After adding slack variables $\omega$ to Model (7), we obtain the initial tableau:

<table><tr><td> $\chi$ </td><td> $\omega$ </td><td>RHS</td></tr><tr><td> $\mathbb{A}$ </td><td>1</td><td> $D\gamma$ </td></tr><tr><td> $-\lambda^{t}\mathbb{C}(\alpha)$ </td><td>0</td><td>0</td></tr></table>

(8)

(9)

Note that the first and second block columns are the coefficients associated respectively with variables $\chi$ and slack variables $\omega$ . Equation (8) represents the constraints while equation (9) is for the objective function.

Let $\mathbb{J}$ be a basis for Model (7) with the basic variables denoted by $\chi(\mathbb{J})$ . We define its associated basis matrix $\mathbb{B}_{\mathbb{J}}$ as the submatrix of $\mathbb{A}$ with column index in $\mathbb{J}$ , and its associated objective function coefficient $\mathbb{C}_{\mathbb{J}}(\alpha)$ as the submatrix of $\mathbb{C}(\alpha)$ with column index in $\mathbb{J}$ . Equation (8)-(9) can be rewritten as:

<table><tr><td> $\chi$ </td><td> $\omega$ </td><td>RHS</td></tr><tr><td> $\mathbb{B}_{\mathbb{J}}^{-1}\mathbb{A}$ </td><td> $\mathbb{B}_{\mathbb{J}}^{-1}$ </td><td> $\mathbb{B}_{\mathbb{J}}^{-1}D\gamma$ </td></tr><tr><td> $\gamma^{t}\mathbb{C}_{\mathbb{J}}(\alpha)$ </td><td> $\lambda^{t}\mathbb{C}_{\mathbb{J}}(\alpha)$ </td><td> $\lambda^{t}\mathbb{C}_{\mathbb{J}}(\alpha)$ </td></tr><tr><td> $\mathbb{R}_{\mathbb{J}}{}^{1}\mathbb{A}$ </td><td> $\mathbb{B}_{\mathbb{J}}{}^{1}$ </td><td> $\mathbb{R}_{\mathbb{J}}{}^{-1}D\gamma$ </td></tr><tr><td> $-\lambda^{t}\mathbb{C}(\alpha)$ </td><td></td><td></td></tr></table>

(10)

(11)

Note that (10)-(11) is a simpler tableau with $\mathbb{B}_{\mathfrak{p}}$ as basis, and

$$
(1 1) = \lambda^ {t} \mathbb {C} _ {\mathrm{J}} (\alpha) \cdot (1 0) + (9).
$$

By dropping $(\gamma, \lambda)$ from (10)-(11), we obtain a $\mathbf{MC}^2$ -simplex tableau with parameter $\alpha$ and basis $\mathbb{B}_{\mathbb{J}}$ as follows:

<table><tr><td> $\chi$ </td><td> $\omega$ </td><td>RHS</td></tr><tr><td> $\mathbb{B}_{\mathfrak{j}}^{-1}\mathbb{A}$ </td><td> $\mathbb{B}_{\mathfrak{j}}^{-1}$ </td><td> $\mathbb{B}_{\mathfrak{j}}^{-1}D$ </td></tr><tr><td> $\mathbb{C}_{\mathfrak{j}}(\alpha)\mathbb{B}_{\mathfrak{j}}^{-1}\mathbb{A}$ </td><td> $\mathbb{C}_{\mathfrak{j}}(\alpha)\mathbb{B}_{\mathfrak{j}}^{-1}$ </td><td> $\mathbb{C}_{\mathfrak{j}}(\alpha)\mathbb{B}_{\mathfrak{j}}^{-1}D$ </td></tr><tr><td> $-\mathbb{C}(\alpha)$ </td><td></td><td></td></tr></table>

(12)

(13)

We rewrite (12)-(13) as

<table><tr><td> $\mathbb{Y}$ </td><td> $\mathbb{W}$ </td></tr><tr><td> $\mathbb{Z}(\alpha)$ </td><td> $\mathbb{Y}(\alpha)$ </td></tr></table>

(14)

(15)

where $\mathsf{Y} = [\mathbb{B}_{\mathbb{J}}^{-1}\mathbb{A},\mathbb{B}_{\mathbb{J}}^{-1}]$ , $\mathsf{W} = \mathbb{R}_{\mathbb{J}}^{-1}D$ , $\mathbb{Z}(\alpha) = [\mathbb{C}_{\mathbb{J}}(\alpha)\mathbb{B}_{\mathbb{J}}^{-1}\mathbb{A} - \mathbb{C}(\alpha),\mathbb{C}_{\mathbb{J}}(\alpha)\mathbb{B}_{\mathbb{J}}^{-1}]$ , and $\mathsf{V}(\alpha) = \mathbb{C}_{\mathbb{J}}(\alpha)\mathbb{B}_{\mathbb{J}}^{-1}D$ .

The following discussion is similar to that of [Pages 243-255 of Chapter 8,18]. We shall not provide the proofs for the corresponding theorems, as they can be readily derived with slight modifications, from Theorem 8.18, Remark 8.21, Remark 8.22, Theorem 8.19, Remark 8.23, Theorem 8.23, and Remark 8.28 of [18].

Let $\mathbb{W}(\mathbb{J})$ and $\mathbb{Z}(\mathbb{J},\alpha)$ be the submatrices of the tableau associated with the basis $\mathbb{J}$ .

Definition 3.1. Given a basis $\mathbb{J}$ of Model (7), (i) $\mathbb{J}$ is a primal potential basis iff

$I^{*}(\mathbb{J}) = \{\gamma \geq 0 | \mathbb{W}(\mathbb{J})\gamma \geq 0\}$ is not empty;

(ii) $\mathbb{J}$ is a dual potential basis iff

$A(\mathbb{J}) = \{\lambda \geq 0, \alpha \geq 0 \mid \lambda^r\mathbb{Z}(\mathbb{J}, \alpha) \geq 0\}$ is not empty;

(iii) $\Gamma(\mathbb{J})$ and $\Lambda(\mathbb{J})$ are known as primal and dual parameter sets respectively.

From Definition 3.1, we have:

Theorem 3.1. $\mathbb{J}$ is a potential solution iff $\Gamma(\mathbb{J}) \times \Lambda(\mathbb{J}) \neq \emptyset$ .

Definition 3.1 and Theorem 3.1 correspond to Theorem 8.18 of [18]. Theorem 3.1 is a generalization of (v) of Statement 2.1, which is also similar to the critical region of vectorparametric programming ([Pages 220–231, Chapter 7,8]).

Furthermore, we have:

Remark 3.1. Comparing (10)-(11) with (12)-(13), we see that

(i) the resulting solution $\chi (\mathbb{J},\gamma) = \mathbb{W}(\mathbb{J})\gamma \geq 0$ and $\mathbb{J}$ is a feasible basis iff $\gamma \in \Gamma (\mathbb{J})$ ;

(ii) the solution $\chi(\mathbb{J},\gamma)$ is optimal iff $\gamma\in\Gamma(\mathbb{J})$ and $(\lambda,\alpha)\in A(\mathbb{J})$ ; and

(iii) the objective value corresponding to $\mathbb{J}$ is $\lambda^{\prime}\mathbb{V}(\alpha)\gamma$ , which is involved with three parameters $\alpha, \gamma$ , and $\lambda$ .

Theorem 3.2. For a given basis $\mathbb{J}$ ,

(i) if $\mathbb{W}_j(\mathbb{J}) > 0$ , then $\mathbb{J}$ is a primal potential basis, where $j$ is the $j^{th}$ column of $\mathbb{W}(\mathbb{J})$ ; and

(ii) if $\mathbb{Z}^{i}(\mathbb{J},\alpha)>0$ , for some $\alpha\geq0$ , then J is a dual potential basis with respect to $\alpha$ , where i is the $i^{th}$ row of $\mathbb{Z}(\mathbb{J},\alpha)$ .

Theorem 3.3. (i) Basis $\mathbb{J}$ is not a primal potential basis if $W^{i}(\mathbb{J}) \leq 0$ , for some $i$ , where $i$ is the $i^{th}$ row of $\mathbb{W}(\mathbb{J})$ .

(ii) Basis $\mathbb{J}$ is not a dual potential basis with respect to $\alpha \geq 0$ if $\mathbb{Z}_j(\mathbb{J},\alpha)\leq 0$ , for some $j$ , where $j$ is the $j^{th}$ column of $\mathbb{Z}(\mathbb{J},\alpha)$ .

Remark 3.2. Both Theorems 3.2 and 3.3 are useful in developing the CAS. Theorem 3.2 helps us to efficiently check whether the primal and/or dual parameter sets exist for a basis. Without Theorem 3.2, we have to solve $\mathbb{W}(\mathbb{J})\gamma \geq 0$ for $\Gamma (\mathbb{J})$ and solve $\lambda^t\mathbb{Z}(\mathbb{J},\alpha)\geq 0$ for $\Lambda (\mathbb{J})$ . If the condition (i) of Theorem 3.3 holds, we use the “dual pivot” to find another primal potential basis. If the condition (i) of Theorem 3.3 holds, we use the “primal pivot” to find a dual potential basis. (See [Remark 8.22, 18] for the definitions of the dual pivot and primal pivot.) In either case, we do not need to find $\Gamma(\mathbb{J})$ by solving $\mathbb{W}(\mathbb{J})\gamma \geq 0$ or $\Lambda(\mathbb{J})$ by solving $\lambda' \mathbb{Z}(\mathbb{J}, \alpha) \geq 0$ .

The subroutines to determine the primal feasibility regarding the parameter set $\Gamma(\mathbb{J})$ and the dual feasibility regarding the parameter set $\nabla(\mathbb{J})$ are based on the following theorem.

Theorem 3.4.

(i) $\Gamma (\mathbb{J})\neq \emptyset$ iff $w_{\mathrm{max}} = 0$ for

max $w = \mathbb{I}_p^r$ e

$$
\begin{array}{l l} \text { s.t. } & y ^ {t} \mathbb {W} (\mathbb {J}) + \mathbf {e} = 0 \\ & y \geq 0,   \mathbf {e} \geq 0, \end{array}\tag{16}
$$

where $y \in R^m$ , $\mathbb{I}_p = (1, \ldots, 1)^t$ , $e \in R^p$ .

(ii) $\Lambda (\mathbb{J})\neq \emptyset$ for some $\alpha$ iff $w_{\max}^{\prime} = 0$ for

$$
\begin{array}{l l} \max & w ^ {\prime} = \mathbb {1} _ {q} ^ {t} e ^ {\prime} \\ \text { s.t. } & \mathbb {Z} (\mathbb {J}, \alpha) y ^ {\prime} + e ^ {\prime} = 0 \\ & y ^ {\prime} \geq 0, e ^ {\prime} \geq 0, \end{array}\tag{17}
$$

where $y' \in R^n$ , $\mathbb{1}_q = (1, \ldots, 1)^t$ , $c' \in R^q$ .

Remark 3.3 From Theorem 3.4, the related simplex tableau to verify the primal feasibility is

<table><tr><td>y</td><td>e</td><td>RHS</td></tr><tr><td> $\mathbb{W}(\mathbb{J})^{t}$ </td><td>I</td><td>0</td></tr><tr><td> $\mathbb{I}_{\mathrm{p}}^{t}\mathbb{W}(\mathbb{J})^{t}$ </td><td>0</td><td>0</td></tr></table>

(18)

where the last row of (18) is used to check the optimality condition for (16).

The related simplex tableau to verify the dual feasibility is

<table><tr><td> $y'$ </td><td> $e'$ </td><td>RHS</td></tr><tr><td> $\mathbb{Z}(\mathbb{J},\alpha)$ </td><td> $I$ </td><td>0</td></tr><tr><td> $\mathbb{I}_{q}^{t}\mathbb{Z}(\mathbb{J},\alpha)$ </td><td>0</td><td>0</td></tr></table>

(19)

where the last row of (19) is used to check the optimality condition for (17).

For the purpose of pivoting, we define effective and null constraints of the primal and dual parameter sets, respectively, as follows.

Definition 3.2. Let $\mathbb{J}$ be a primal potential basis. For $i\in\{1,\ldots,m\}$ , $\mathbb{W}^{i}(\mathbb{J})$ is said to be an effective constraint of $\Gamma(\mathbb{J})$ if $\mathbb{W}^{i}(\mathbb{J})\neq0$ and there exists $\gamma^{0}\in\Gamma(\mathbb{J})$ such that $\mathbb{W}^{i}(\mathbb{J})\gamma^{0}=0$ ; and $\mathbb{W}^{i}(\mathbb{J})$ is said to be a null constraint of $\Gamma(\mathbb{J})$ if $\mathbb{W}^{i}(\mathbb{J})=0$ .

Definition 3.3. Let $\mathbb{J}$ be a dual potential basis with respect to $\alpha^0$ and $\mathbb{J}'$ the set of corresponding nonbasic vectors. For $j \in \mathbb{J}'$ , $\mathbb{Z}_j(\mathbb{J}, \alpha^0)$ is said to be an effective constraint of $\Lambda(\mathbb{J})$ at $\alpha^0$ if $\mathbb{Z}_j(\mathbb{J}, \alpha^0) \neq 0$ and there exists $\lambda^0 \in \Lambda(\mathbb{J})$ such that $\lambda^0 \mathbb{Z}_j(\mathbb{J}, \alpha^0) = 0$ ; and $\mathbb{Z}_j(\mathbb{J}, \alpha^0)$ is said to be a null constraint of $\Lambda(\mathbb{J})$ at $\alpha^0$ if $\mathbb{Z}_j(\mathbb{J}, \alpha^0) = 0$ .

The following theorem allows us to find the effective or null constraints.

## Theorem 3.5.

(i) $\mathbb{W}^i (\mathbb{J})$ is an effective constraint of $\Gamma (\mathbb{J})$ iff there exists $(v,w)\geq 0$ such that $\mathbb{W}(\mathbb{J})v + \mathbb{W}(\mathbb{J})\mathbb{1}_p = w$ with $w_{i} = 0$ , where $v,\mathbb{1}_p\in \mathbf{R}^p$ , and $w\in \mathbf{R}^m$ .  
(ii) $\mathbb{Z}_j(\mathbb{J},\alpha^0)$ is an effective constraint of $\Lambda (\mathbb{J})$ at $\alpha^0$ iff there exists $(v',w')\geq 0$ such that $v'^t\mathbb{Z}(\mathbb{J},\alpha^0)$ $+\mathbb{1}_q^\prime \mathbb{Z}(\mathbb{J},\alpha^0) = w'$ with $w_{j}^{\prime} = 0$ , where $v^{\prime},\mathbb{1}_q\in \mathbf{R}^q$ , and $w^{\prime}\in \mathbf{R}^{n}$ .

Remark 3.4. From Theorem 3.5, to verify the condition of effective constraints of $\Gamma(\mathbb{I})$ , we use the initial tableau:

<table><tr><td> $v$ </td><td> $w$ </td><td>RHS</td></tr><tr><td> $-\mathbb{W}(\mathbb{J})$ </td><td> $I$ </td><td> $\mathbb{W}(\mathbb{J})\mathbb{I}_{p}$ </td></tr></table>

(20)

If $\mathbb{W}(\mathbb{J})\mathbb{I}_p$ has negative entries, we could use dual pivot to find a feasible tableau and then verify the relevant condition.

To verify the condition of effective constraints of $\Lambda(\mathbb{J})$ at $\alpha^{0}$ , we use the initial tableau:

$$
\begin{array}{c c} \hline v ^ {\prime} & w ^ {\prime} \text {RHS} \\ \hline - \mathbb {Z} (\mathbb {J}, \alpha^ {(1)}) ^ {t} I & \mathbb {Z} (\mathbb {J}, \alpha^ {(1)}) ^ {t} \mathbb {I} _ {q} \end{array}\tag{21}
$$

If $\mathbb{Z}(\mathbb{J},\alpha^{0})^{t}\mathbb{1}_{q}$ has negative entries, we could use dual pivot to find a feasible tableau and then verify the condition.

Remark 3.5. There are five basic subroutines for solving Model (7). The first one is to compute Tableau (12)-(13). The second and third are to test the primal and dual parameter sets by using Tableaus (18) and (19), respectively (see Theorem 3.4). The fourth and fifth are to check the primal and dual effective constraint by using Tableaus (20) and (21), respectively (see Theorem 3.5). These subroutines can be designed as computer procedures in the CAS.

## 4. A computer-aided system

In this section, by integrating sections 2 and 3, we first propose a procedure to solve a problem of selecting optimal production systems (section 4.1). Then we describe a design of a CAS for selecting optimal production systems. Instead of studying how to write and implement the program of the CAS by using some particular computer language, we shall focus on exploring the related flowcharts of the algorithms for the CAS (section 4.2), a top-down design of the CAS (section 4.3), and the pseudo-language programs (section 4.4).

## 4.1. A solution procedure

From our discussion in previous sections, a procedure for solving problems of selecting optimal production systems can be described as follows:

## Procedure 4.1.

Step 1. Find all primal potential solutions for the augmented model (AM) by applying (i) of Definition 2.1. Denote the set of such solutions by $\epsilon = \{E_1, \ldots, E_r\}$ . Without confusion, $E$ will generically denote such a basis, and its corresponding basic variables in $x$ and $y$ will be denoted by $x(E)$ and $y(E)$ respectively. Note that $x(E)$ can contain slack variables $s$ .

Step 2. Find all potential solutions or PGS's for Model (M1) by Definition 2.1. Denote the set of such solutions by $\mathcal{J} = \{J_1, \ldots, J_g\}$ . Note that we can obtain the primal potential solutions by dropping those $E \in \epsilon$ which contain some $y_i$ , $i = 1, \ldots, m$ . Then from the primal potential solutions, we use (ii) of Definition 2.1 to identify the dual potential solutions and use Statement 2.1 to obtain the entire $\mathcal{J}$ . Without confusion, $J$ will generically denote such bases, and the corresponding basic variables will be denoted by $x(J)$ . Note the $x(J)$ can contain slack variables s.

Step 3. Applying the algorithm of [17], find all GGS's for Model (M1). Denote the set of such GGS's by $\{\Omega_1, \ldots, \Omega_k\}$ . Note that a GGS $\Omega$ can contain slack variables $s$ .

Step 4. If we want to prepare the rigid contingency plans for each candidate (J or $\Omega$ ), then do the following:

(a) For each $J$ , identify all potential solutions for Model (M2) by applying Definition 2.1 from its corresponding tableaus. The primal potential solutions can be found by dropping those $E \in \epsilon$ which contain some $s_i$ of $x(J')$ and/or some $y_i$ of $y$ . Then we apply (ii) of Definition 2.1 to check the optimality condition for the primal potential solutions. Denote the resulting subset of $\epsilon$ by $\epsilon^2(J)$ . For each $E^2$ of $\epsilon^2(J)$ , $x(E^2(J), \gamma)$ is the rigid contingency plan selected by Model (M2) for PGS $J$ . If for any $(\gamma, \lambda)$ , there is $E^2$ in $\epsilon^2(J)$ that "optimizes" Model (M2), then $\epsilon^2(J)$ is the set of all rigid contingency plans for PGS $J$ and we go to Step 6. Otherwise, for each PGS $J$ of Step 2, identify those $E \in \epsilon$ of Step 1 for which $x(E) \subseteq x(J)$ (i.e., the set of basic variables $x(E)$ is contained in $x(J)$ ). Denote the resulting subset of $\epsilon$ by $\epsilon^3(J)$ . This step can be accomplished by dropping those $E \in \epsilon$ which contain some $s_i$ of $x(J')$ . Note that for each of such $E^3$ of $\epsilon^3(J)$ , $x(J)$ , $(x(E^3(J), \gamma), y(E^3, \gamma))$ offers a primal potential solution of Model (M3) for $J$ . With a given level of $\alpha$ value, applying (ii) of Definition 2.1, we can find the set of optimal rigid contingency plan selected by Model (M3) for PGS $J$ .

(b) For each $\Omega$ , identify all potential solutions for Model (M4) by applying Definition 2.1 from its corresponding tableaus. The primal potential solutions can be found by dropping those $E \in \epsilon$ which contain some $s_i$ of $x(\Omega')$ and/or some $y_i$ of $y$ . Then applying (ii) of Definition 2.1 we check the optimality condition for the primal potential solutions. Denote the resulting subset of $\epsilon$ by $\epsilon^4(\Omega)$ . For each $E^4$ of $\epsilon^4(\Omega)$ , $x(E^4(\Omega), \gamma)$ is the rigid contingency plan selected by Model (M4) for GGS $\Omega$ . If for any $(\gamma, \lambda)$ , there is $E^4$ in $\epsilon^4(\Omega)$ that "optimizes" Model (M4), then $\epsilon^4(\Omega)$ is the set of all rigid contingency plans for GGS $\Omega$ and we go to Step 6. Otherwise, for each GGS $\Omega$ of Step 3, identify those $E \in \epsilon$ of Step 1 for which $x(E) \subseteq x(\Omega)$ (i.e., the set of basic variables $x(E)$ is contained in the set of variables $x(\Omega)$ . Denote the resulting subset of $\epsilon$ by $\epsilon^5 (\Omega)$ . This step can be done by dropping those $E\in \epsilon$ which contain some $s_i$ of $x(\Omega')$ . Note that for each of such $E^5$ of $\epsilon^5 (\Omega), x(E^5 (\Omega),\gamma),y(E^5,\gamma))$ is a primal potential solution of Model (M5) for $\Omega$ . With a given level of $\alpha$ value, we then apply (ii) of Definition 2.1 to find the set of optimal rigid contingency plan selected by Model (M5) for GGS $\Omega$ .

Step 5. If we want to prepare the flexible contingency plans for each candidate (J or $\Omega$ ), then do the following:

(a) For each $J$ , identify all potential solutions for Model (M6) by applying Definition 2.1 from its corresponding tableaus. The primal potential solutions can be found by dropping $E \in \epsilon$ which contain some $s_i$ of $x^2(J')$ and/or some $y_i$ of $y$ . Then by applying (ii) of Definition 2.1 we check the optimality condition for the primal potential solutions. Denote the resulting subset of $\epsilon$ by $\epsilon^6(J)$ . For each $E^6$ of $\epsilon^6(J)$ , $(x(E^6(J), \gamma), x^1(E^6(J'), \gamma))$ is the flexible contingency plan selected by Model (M6) for PGS $J$ . If for any $(\gamma, \lambda)$ , there is $E^6$ in $\epsilon^6(J)$ which “optimizes” Model (M6), then $\epsilon^6(J)$ is the set of all flexible contingency plans for PGS $J$ and we go to Step 6. Otherwise, for each PGS $J$ of Step 2, identify those $E \in \epsilon$ of Step 1 for which $x(E) \subseteq (x(J), x^1(J'))$ (i.e., the set of basic variables $x(E)$ is contained in the set of variables $(x(J), x^1(J'))$ ). Denote the resulting subset of $\epsilon$ by $\epsilon^7(J)$ . This step can be accomplished by dropping those $E \in \epsilon$ which contain some $s_i$ of $x^2(J')$ . Note that for each of such $E^7$ of $\epsilon^7(J), (x(E^7(J), \gamma), x^1(E^7(J'), \gamma), y(E^7, \gamma))$ is a primal potential solution of Model (M7) for $J$ . With a given level of $\alpha$ value, applying (ii) of Definition 2.1, we can find the set of optimal flexible contingency plan selected by Model (M7) for PGS $J$ .

(b) For each $\Omega$ , identify all potential solutions for Model (M8) by applying Definition 2.1 from its corresponding tableaus. The primal potential solutions can be found by dropping those $E \in \epsilon$ which contain some $s_i$ of $x^2(\Omega')$ and/or some $y_i$ of $y$ . Then applying (ii) of Definition 2.1 we check the optimality condition for the primal potential solutions. Denote the resulting subset of $\epsilon$ by $\epsilon^8(\Omega)$ . For each $E^8$ of $\epsilon^8(\Omega)$ , $(x(E^8(\Omega), \gamma), x^1(E^8(\Omega'), \gamma))$ is the flexible contingency plan selected by Model (M8) for GGS $\Omega$ . If for any $(\gamma, \lambda)$ , there is $E^{8}(\Omega)$ that “optimizes” Model (M8), then $\epsilon^{8}(\Omega)$ is the set of all flexible contingency plans for GGS $\Omega$ and we go to Step 6. Otherwise, for each GGS $\Omega$ of Step 3, identify those $E \in \epsilon$ of Step 1 for which $x(E) \subseteq (x(\Omega), x^{1}(\Omega'))$ (i.e., the set of basic variables $x(E)$ is contained in the set of variables $(x(\Omega), x^{1}(\Omega'))$ ). Denote the resulting subset of $\epsilon$ by $\epsilon^{9}(\Omega)$ . This step can be done by dropping those $E \in \epsilon$ which contain some $s_{i}$ of $x^{2}(\Omega')$ . For each of such $E^{9}$ of $\epsilon^{9}(\Omega)$ , $(x(E^{9}(\Omega), \gamma), x^{1}(E^{9}(\Omega'), \gamma), y(E^{9}, \gamma))$ is a primal potential solution of Model (M9) for $\Omega$ . With a given level of $\alpha$ value, applying (ii) of Definition 2.1 we find the set of optimal flexible contingency plan selected by Model (M9) for GGS $\Omega$ .

Step 6. Evaluate each PGS J and GGS Ω and their corresponding contingency plans from either Step 4 or Step 5 in terms of a criterion preferred by the decision makers (recall (iii) of Remark 2.2). The final optimal production systems are selected based on these results of evaluation.

An illustrative example of applying Procedure 4.1 is given in the Appendix.

## 4.2. Flowcharts of the algorithm

Based on Procedure 4.1, a heuristic algorithm of the CAS for selecting optimal production systems is presented in Figures 2–4. Figure 2 is the main flowchart of the algorithm. Figure 3 is a subflowchart that explains box (2) of Figure 2 in detail. Furthermore, the details of box (5) in Figure 3 are shown by Figure 4. By modifying Figure 4, the flowchart for box (6) in Figure 3 can be similarly drawn (see Remark 4.1). Note that Figures 3–4 explain the process of locating all PGS's and GGS's with their rigid contingency plans. The process of locating all PGS's and GGS's with their flexible contingency plans (i.e., box (3) of Figure 2) can be similarly explained.

![](/api/attachments/PZA6N3HE/fulltext/images/afadb41b4a82265eae9811e2fea06c6865e12ec4f6b2123455313160ef2bbf73.jpg)  
Fig. 2. Main flowchart of CAD for selecting optimal production systems.

However, to save the space, we shall not do so. Although the CAS is self-explanatory, in the following we provide a description of the algorithm to emphasize connections between the CAS and Procedure 4.1.

In Figure 2, given a production system prob-

![](/api/attachments/PZA6N3HE/fulltext/images/9e140134fba27f76d0377c2773092d87c258153660c7dc6c4f908ad3a16e1f95.jpg)  
Fig. 3. Flowchart corresponding to box (2) of Figure 2.

lem, box (1) deals with all possible input data including the number of possible product variables, the number of criteria, the number of resource levels, the number of constraints, matrices C, A, D, the price of additional resources $\alpha$ , the probability distributions related to $(\gamma, \lambda)$ , etc.

![](/api/attachments/PZA6N3HE/fulltext/images/fb836d5742cd6935e9d0bac5fa29f662ff5499d04c89acd25813cd4e34f2109e.jpg)  
Fig. 4. Finding all rigid contingency plans for each PGS corresponding to box (5) of Figure 3.

According to the information of box (1), we can either locate the set of all PGS's and GGS's with the corresponding rigid contingency plans (box (2)), or locate the set of all PGS's and GGS's with the corresponding flexible contingency plans (box (3)). The detailed discussion for box (2) is provided to Figure 3.

After optimal production systems have been selected from both boxes (2) and (3), the decision makers will judge them in box (4). If the decision makers are not satisfied with the result, box (5) revises the data for box (1). The process is not terminated at box (6) until the decision makers are satisfied with the selected optimal production systems.

Figure 3 integrates the process of locating the set of all PGS's and GGS's with the corresponding rigid contingency plans described in Procedure 4.1. Box (1) of Figure 3, corresponding to

Step 1 in Procedure 4.1, solves Model (AM) and obtains the set of all primal potential solutions for Model (AM). Box (2) of Figure 3, corresponding to Step 2 in Procedure 4.1, identifies the set of all PGS's, J, for Model (M1) based on the tableaus of Model (AM). Then, box (3) of Figure 3 will check whether Model (M1) has an unbounded solution. If yes, box (5) of Figure 2 revises the data for box (1) of Figure 2. Otherwise, box (4) of Figure 3, which corresponds to Step 3 of Procedure 4.1, executes the efficient algorithm of [16] for locating all GGS's. Then, box (6) of Figure 3 uses (b) of Step 4 in Procedure 4.1 to identify all corresponding rigid contingency plans for each GGS Ω (see Remark 4.1). Similarly, box (5) of Figure 3 uses (a) of Step 4 in Procedure 4.1 to locate the corresponding rigid contingency plans for each PGS J (see Figure 4 for details). The results from both box (5) and box (6) of Figure 3 are evaluated in box (7) of Figure 3. In the box (7), which corresponds to Step 6 in Procedure 4.1, the criterion preferred by the decision makers and the information about the probability distributions related to $(\gamma, \lambda)$ (see (iii) of Remark 2.2) are used for selecting optimal production systems. The final result is printed out by box (8) of Figure 3 for box (4) of Figure 2.

![](/api/attachments/PZA6N3HE/fulltext/images/d80da880a3b16276da04bfb1f17de85995da74a163493dee5cb10b8a1562ae78.jpg)  
Fig. 5. Top-down design of CAS.

Figure 4, which is related to (a) of Step 4 in Procedure 4.1, describes the detailed execution of box (5) of Figure 3. In Figure 4, Boxes (a), (b), (c), (d), (g), (h), and (i) identify the set of rigid contingency plans selected by Model (M2) for each PGS J and check if all rigid contingency plans for PGS J are found. If for some $\gamma$ , Model (M2) has no feasible solution, then Boxes (d), (e), (f), (g), and (i) in Figure 4 find the set of all rigid contingency plans selected by Model (M3) for PGS J such that for any $(\gamma, \lambda)$ , there is a rigid contingency plan that “optimizes” Model (M3).

Remark 4.1. To obtain the flowchart of using (b) of Step 4 in Procedure 4.1 to identify the set of rigid contingency plans for each GGS $\Omega$ , we can simply replace Model (M2) by Model (M4) and Model (M3) by Model (M5) in Figure 4. Then the resulting flowchart can explain the detailed execution of box (6) of Figure 3.

## 4.3. A top-down design

The top-down design is a well-known technique to develop a large and complex computer program. It divides all tasks of solving a target problem by levels in terms of a “tree structure.” The target problem is put on the top level. Then, each subproblem is put on a lower level. The tasks on a higher level are broader, while the tasks on a lower level are more specific. Once the tasks on the lower level are accomplished or the subproblems are solved, we can solve the subproblems on the higher level and eventually solve the target problem. Thus, the date structures of a computer program for solving the target problem can be developed from the lower levels to the higher levels (see Dale and Orshalick [5]).

A top-down design of the CAS for selecting the optimal production systems is proposed in Figure 5. The first level of Figure 5 is the Target Production System Problem (box 1). The second level has three tasks: Input (box 2), Computation (box 3), and Output (box 4). On the third level, Read Data (box 5) and Revise Data (box 6) are subtasks of Input; Solve Submodels (box 7) and Evaluation (box 8) are subtasks of Computation; and Tableau (box 9) and Expected Payoff (box 10) are subtasks of Output. Continuing in this manner we get a picture containing every detailed subtask needed to develop the CAS as in Figure 5. Note that box (11) of Figure 5 contains four parallel tasks: Solve Model (M2), Solve (M3), Solve (M6), and Solve (M7). Since they have similar subtasks, we put them together without confusion. Similarly, box (12) means the following four tasks: Solve (M4), Solve (M5), Solve (M8), and Solve (M9). Thus, Solve Submodels (box 7) has eight subtasks on the fourth level.

According to Figure 5, we can develop a series of computer procedures for developing the entire CAS for selecting the optimal production systems. The following are some of the computer procedures needed in the CAS.

(i) Procedures that have an error-check capability to read the given data of a target production system problem (box 5) and to revise or update the data (box 6).

(ii) Procedures to test the primal potential solution (box 26) and the primal effective and null constraints (box 27).

(iii) Procedures to process the primal pivoting (box 23) and the dual pivoting (box 25).

(iv) Procedures to identify dual potential solutions for Model (M1), and Models (M2)-(M9), respectively (boxes 18, 20, and 22).

(v) Procedures to search for a set of all GGS's (box 19). (Note that the algorithm of [17] can be applied here).

(vi) Procedures to evaluate the set of all PGS's and GGS's with their corresponding contingency plans for choosing optimal production systems as the final decision (box 8).

(vii) Procedures to print out the basic variables, the primal and dual parameter sets, the payoff matrix, and the expected payoff value for each of optimal production systems (boxes 13, 14, 15, 16, and 10).

## 4.4. A pseudo-language program

Based on the discussion in section 3, 4.1, 4.2, and 4.3, the whole program of the CAS for selecting the optimal production systems can be carried out by using a pseudo-language. The pseudo-language program can be converted into any particular computer language for implementation through a series of stepwise refinements. (For reference, see [1]). For illustrative purposes, in the following, we write a sub pseudo-language program for selecting optimal production systems with optimal rigid contingency plans (refer to boxes (1), (2), (4), (5), and (6) of Figure 2, Figure 3, and Figure 4).

Program of Selecting Optimal Production Systems with Optimal Rigid Contingency Plans;
Begin
    Date\_Change: = True;
    While Date\_Change do
    Begin
    Read Data;
    Print Simplex Tableau;
    Augment: = True;
    While Augment do
    Begin
    If Primal Pivoting needed then
    Repeat
    Primal Pivoting;
    Print Result
    Until done;
    If Primal Potential Testing needed then
    Repeat
    Primal Potential Testing;
    Print Result
    Until done;
    If Finding Primal Effective and Null Constraint needed then
    Repeat
    Primal Effective and Null Constraint Testing;
    Print Result
    Until done;
    If all Primal Solutions of Model (AM) found then
    Augment: = False
    cnd;
    Repeat
    Identify Simplex Tableau of Model (M1);
    Print Tableau
    Until all Tableaus of Model (M1) found;
    If Model (M1) has unbounded solutions then go to Read Data;

For each PGS J do
Begin
Repeat
    Identify Simplex Tableau of Model (M2);
    Print Tableau
Until all Tableaus of Model (M2) found;
If Model (M2) has unbounded solutions then
go to Read Data;
If some γ, (M2) has no feasible solution for
PGS J
then
    Begin
    Repeat
    Identify Simplex Tableau of Model
(M3);
    Print Result
    Until all Tableaus of Model (M3)
found;
    If Model (M3) has unbounded solu-
tions then
    go to Read Data
    end
end;
Evaluate the contingency plans for all PGS's;
Print Expected Payoff;
Find all GGS's;
For each GGS Ω do
Begin
    Repeat
    Identify Simplex Tableau of Model
(M4);
    Print Tableau
Until all Tableaus of Model (M4) found;
If Model (M4) has unbounded solutions
then
    go to Read Data;
If some γ, (M4) has no feasible solution
for GGS Ω
then
    Begin
    Repeat
    Identify Simplex Tableau of Model
(M5);
    Print Tableau
Until all Tableaus of Model (M5)
found;
    If Model (M5) has unbounded solu-
tions then
    go to Read Data
end
end;

Evaluate the contingency plans for all GGS's; Print Expected Payoff;

end;

If Data does not need to be revised then

Data\_Change:=False

end;

Note that if we want to select optimal production systems with optimal flexible contingency plans, the corresponding sub pseudo-language program can be obtained by changing Model (M2) to Model (M6), Model (M3) to Model (M7), Model (M4) to Model (M8), and Model (M5) to Model (M9), respectively in the above pseudo-language program. Also, from the main flowchart in Figure 2, we can write the entire pseudo-language program of the CAS for selecting optimal production systems by merging these two sub pseudo-language programs.

Based on the above discussion about the flowcharts of the algorithm (section 4.2), the top-down design (section 4.3), and the pseudo-language program (section 4.4), professional programmers should be able to implement the CAS.

## 5. Conclusions

Given a problem of selecting optimal linear production systems with multiple criteria and multiple resource availability levels, it is challenging to develop a computer-aided decision support system for efficiently and systematically solving the problem. Using the MC $^{2}$ -simplex method, this paper has provided a computer-aided system for selecting the optimal production systems.

There are a number of research problems remaining to be explored. For instance, we may call the optimal contingency plans constructed by Procedure 4.1 for a given potentially good system (or generalized good system) the primal optimal contingency plans, since these contingency plans can overcome the difficult situation where the model of selecting optimal production systems has no feasible solutions for some value of the resource parameter $\gamma$ . However, for some values of the contribution parameter $\lambda$ , the basic solution corresponding to the potentially good system (or generalized good system) may not satisfy the optimality condition. By market promotion or persuasion, for instance, the $\lambda$ value may change. As the parameters $(\lambda, \gamma)$ can vary from period to period, how can we prepare the dual optimal contingency plans for a given potentially good systems (or generalized good system) to ensure optimality?

Instead of using the known criteria of decision making under uncertainty mentioned in (iii) of Remark 2.2, one could use computer simulation to simulate the distribution of the parameters $(\gamma, \lambda)$ for finding the final optimal production systems.

These problems are important and deserve a careful study. We shall report significant results in the near future.

## Appendix. An illustrative example of selecting optimal production systems

Based on the model of production systems in Example 2.1, let $y_{1}$ , $y_{2}$ , and $y_{3}$ by the additional resource variables with the corresponding unit price $\alpha_{1}$ , $\alpha_{2}$ , $\alpha_{3}$ , respectively. We use Procedure 4.1, step by step, to select optimal production systems with optimal flexible contingency plans as follows.

Step 1. By using the program of [3], we solve the corresponding augmented problem:

$$
\max (\lambda_ {1}, \lambda_ {2}) \left( \begin{array}{c c c c c} 3 & 2 & 1 & 1 & 0 \\ 0 & 1 & 2 & 3 & 3 \end{array} \right) \left( \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right)
$$

$$
- \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{l} y _ {1} \\ y _ {2} \\ y _ {3} \end{array} \right)
$$

$$
\text {s.t.} \left( \begin{array}{c c c c c} 1 & 0 & 2 & 1 & 0 \\ 0 & 1 & 1 & 2 & 2 \\ 1 & 1 & 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ x _ {5} \end{array} \right)
$$

$$
- \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c} y _ {1} \\ y _ {2} \\ y _ {3} \end{array} \right)
$$

$$
\leq \left( \begin{array}{c c} - 1 0 & 2 0 \\ 4 0 & 2 0 \\ 3 0 & 4 0 \end{array} \right) \binom {\gamma_ {1}} {\gamma_ {2}}
$$

$x_{j} \geq 0, j = 1, 2, 3, 4, 5; \text{and } y_{i} \geq 0, i = 1, 2, 3.$

Table A.1  
Primal potential solutions for Augmented Model (AM)

<table><tr><td>Primal Potential Bases</td><td>Basic Variables</td><td>Primal Potential Bases</td><td>Basic Variables</td></tr><tr><td> $E_1$ </td><td> $(x_1, s_2, s_3)$ </td><td> $E_{23}$ </td><td> $(x_2, s_1, s_3)$ </td></tr><tr><td> $E_2$ </td><td> $(x_1, x_3, y_1)$ </td><td> $E_{24}$ </td><td> $(x_3, s_2, s_3)$ </td></tr><tr><td> $E_3$ </td><td> $(x_1, x_4, s_3)$ </td><td> $E_{25}$ </td><td> $(x_3, y_1, s_3)$ </td></tr><tr><td> $E_4$ </td><td> $(x_1, x_4, y_1)$ </td><td> $E_{26}$ </td><td> $(x_3, x_5, y_2)$ </td></tr><tr><td> $E_5$ </td><td> $(x_1, x_2, y_1)$ </td><td> $E_{27}$ </td><td> $(x_3, x_4, s_3)$ </td></tr><tr><td> $E_6$ </td><td> $(x_1, x_2, y_2)$ </td><td> $E_{28}$ </td><td> $(x_4, x_5, s_3)$ </td></tr><tr><td> $E_7$ </td><td> $(x_1, x_2, y_3)$ </td><td> $E_{29}$ </td><td> $(y_1, s_2, s_3)$ </td></tr><tr><td> $E_8$ </td><td> $(x_1, x_2, s_1)$ </td><td> $E_{30}$ </td><td> $(x_4, y_1, s_3)$ </td></tr><tr><td> $E_9$ </td><td> $(x_1, x_2, s_2)$ </td><td> $E_{31}$ </td><td> $(x_4, x_5, y_2)$ </td></tr><tr><td> $E_{10}$ </td><td> $(x_1, x_2, x_3)$ </td><td> $E_{32}$ </td><td> $(x_4, y_2, s_3)$ </td></tr><tr><td> $E_{11}$ </td><td> $(x_2, x_3, y_1)$ </td><td> $E_{33}$ </td><td> $(x_4, s_1, s_3)$ </td></tr><tr><td> $E_{12}$ </td><td> $(x_2, x_3, y_2)$ </td><td> $E_{34}$ </td><td> $(x_4, s_2, s_3)$ </td></tr><tr><td> $E_{13}$ </td><td> $(x_2, x_3, s_3)$ </td><td> $E_{35}$ </td><td> $(x_5, s_1, s_3)$ </td></tr><tr><td> $E_{14}$ </td><td> $(x_1, x_5, y_2)$ </td><td> $E_{36}$ </td><td> $(x_5, y_2, s_1)$ </td></tr><tr><td> $E_{15}$ </td><td> $(x_1, x_5, y_1)$ </td><td> $E_{37}$ </td><td> $(x_5, y_1, y_2)$ </td></tr><tr><td> $E_{16}$ </td><td> $(x_1, y_1, s_2)$ </td><td> $E_{38}$ </td><td> $(x_5, y_1, s_3)$ </td></tr><tr><td> $E_{17}$ </td><td> $(x_2, y_2, s_1)$ </td><td> $E_{39}$ </td><td> $(x_2, x_4, y_1)$ </td></tr><tr><td> $E_{18}$ </td><td> $(x_2, x_5, y_1)$ </td><td> $E_{40} = J_1$ </td><td> $(x_1, x_2, s_3)$ </td></tr><tr><td> $E_{19}$ </td><td> $(x_2, x_4, y_2)$ </td><td> $E_{41} = J_2$ </td><td> $(x_1, x_2, x_4)$ </td></tr><tr><td> $E_{20}$ </td><td> $(x_2, x_4, s_3)$ </td><td> $E_{42} = J_3$ </td><td> $(x_1, x_2, x_5)$ </td></tr><tr><td> $E_{21}$ </td><td> $(x_2, y_1, s_2)$ </td><td> $E_{43} = J_4$ </td><td> $(x_1, x_5, s_3)$ </td></tr><tr><td> $E_{22}$ </td><td> $(x_2, y_1, y_3)$ </td><td> $E_{44} = J_5$ </td><td> $(x_3, x_5, s_3)$ </td></tr></table>

We obtain the set of all primal potential solutions, denoted by $\epsilon=\{E_{1},\ldots,E_{44}\}$ as listed in Table A.1, where $E_{40}=J_{1}$ , $E_{41}=J_{2}$ , $E_{42}=J_{3}$ , $E_{43}=J_{4}$ , and $E_{44}=J_{5}$ .

Step 2. By dropping those E in $\epsilon$ which contain some $y_{i}, i=1,2,3$ , in Table A.1, we identify all potential solutions (or PGS's) for Model (M1). Denote the set of such solutions by $J=\{J_{1}, J_{2}, J_{3}, J_{4}, J_{5}\}$ , which are listed in Table 1 of Example 2.1.

Step 3. Given $\mathcal{J} = \{J_1, \ldots, J_5\}$ , we take unions of subsets of $\mathcal{J}$ . There are $2^5 - 1 - 5 (= 26)$ possible unions of subsets of $\mathcal{J}$ that need to be checked in order to generate all GGS's. By applying the efficient algorithm of [17], we obtain all GGS's which are the distinct unions as in Table A.2.

Contingency plans for $J_{2}$  
Table A.2
Generalized good systems

<table><tr><td>Generalized good system</td><td>Basic variables</td></tr><tr><td> $\Omega_1$ </td><td> $(x_1, x_2, x_4, s_3)$ </td></tr><tr><td> $\Omega_2$ </td><td> $(x_1, x_2, x_4, x_5, s_3)$ </td></tr><tr><td> $\Omega_3$ </td><td> $(x_1, x_2, x_3, x_4, x_5, s_3)$ </td></tr><tr><td> $\Omega_4$ </td><td> $(x_1, x_2, x_5, s_3)$ </td></tr><tr><td> $\Omega_5$ </td><td> $(x_1, x_2, x_3, x_5, s_3)$ </td></tr><tr><td> $\Omega_6$ </td><td> $(x_1, x_2, x_4, x_5)$ </td></tr><tr><td> $\Omega_7$ </td><td> $(x_1, x_3, x_5, s_3)$ </td></tr></table>

Step 5. For each $J_j$ , $j = 1, \ldots, 5$ of Step 2, we identify all flexible contingency plans for Model (M6). For illustrative purposes, we denote the set of all flexible contingency plans for $J_2$ by $\epsilon^6(J_2) = \{J_2, J_1, E_3, E_{20}\}$ . Let $\Gamma_6(E_i(J_2))$ be the primal parameter set of $E_i(J_2)$ and $A_6(E_i(J_2))$ be the dual parameter set of $E_i(J_2)$ . Then, the flexible contingency plans selected by Model (M6) for $J_2$ are listed in Table A.3.

Table A.3 can be explained as follows: If PGS $J_{2}$ is chosen, (i) whenever $0 \leq \gamma_{1} \leq 2/3$ and $1/7 \leq \lambda_{1} \leq 1$ , $J_{2}$ and $J_{1}$ overlap. Thus we can either use $J_{2}$ to produce products $\{x_{1}, x_{2}, x_{3}\}$ and no slack resource is left over, or use $J_{1}$ to produce $\{x_{1}, x_{2}\}$ (note that $s_{3}$ is the amount of the slack resource left over from constraint 3); whenever $0 \leq \gamma_{1} \leq 1/4$ and $0 \leq \lambda_{1} \leq 1/7$ , we can use $E_{3}$ to produce $\{x_{1}, x_{4}\}$ ; and whenever $1/4 \leq \gamma_{1} \leq 2/3$ and $0 \leq \lambda_{1} \leq 1/7$ , we can use $E_{20}$ to produce $\{x_{2}, x_{4}\}$ . Therefore, we have two alternative contingency plan sets for $J_{2}$ : $\{J_{2}, E_{3}, E_{20}\}$ and $\{J_{1}, E_{3}, E_{20}\}$ .

<table><tr><td> $\epsilon^{6}(J_{2})$ </td><td> $\Gamma_{6}(E_{i}(J_{2}))$ </td><td> $\Lambda_{6}(E_{i}(J_{2}))$ </td><td>Payoff  $V(*|J_{2})$ </td></tr><tr><td> $x(J_{2})=(x_{1},x_{2},x_{4})$ </td><td> $0\leq\gamma_{1}\leq2/3$ </td><td> $1/7\leq\lambda_{1}\leq1$ </td><td> $(\lambda_{1},\lambda_{2})\begin{pmatrix}50&100\\40&20\end{pmatrix}\begin{pmatrix}\gamma_{1}\\ \gamma_{2}\end{pmatrix}$ </td></tr><tr><td> $x(J_{1})=(x_{1},x_{2},s_{3})$ </td><td> $0\leq\gamma_{1}\leq2/3$ </td><td> $1/7\leq\lambda_{1}\leq1$ </td><td> $(\lambda_{1},\lambda_{2})\begin{pmatrix}50&100\\40&20\end{pmatrix}\begin{pmatrix}\gamma_{1}\\ \gamma_{2}\end{pmatrix}$ </td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

The flexible contingency plans selected by Model (M6) for PGS's $J_{j}$ , j = 1, 3, 4, 5, can be similarly listed.

Similarly, for each $\Omega_{i}, i=1,\ldots,7$ of Step 3, we can identify all flexible contingency plans for Model (M8).

Since for any $2/3 \leq \gamma_1 \leq 1$ , Model (M6) for PGS's $J_j$ , $j = 1, \ldots, 5$ , has no feasible solution, we identify those $E \in \epsilon$ of Step 1 for which $x(E) \subseteq (x(J_j), x^1(J_j'))$ . These subsets of $\epsilon$ is defined as $\epsilon^7(J_j)$ , $j = 1, \ldots, 5$ . We have:

$\epsilon^7 (J_1) = \{J_1,E_1,E_5,E_6,E_7,E_8,E_9,E_{16},E_{17},$ $E_{21},E_{22},E_{23},E_{29}\} ;$ $\epsilon^7 (J_2) = \{J_2,E_1,E_3,E_4,E_5,E_6,E_7,E_8,E_9,$ $E_{16},E_{17},E_{19},E_{20},E_{21},E_{22},E_{23},E_{29},$ $E_{30},E_{32},E_{33},E_{34},E_{39}\} ;$ $\epsilon^7 (J_3) = \{J_3,E_1,E_5,E_6,E_7,E_8,E_9,E_{14},E_{15},$ $E_{16},E_{17},E_{18},E_{21},E_{22},E_{23},E_{29},E_{35},$ $E_{36},E_{37},E_{38}\} ;$ $\epsilon^7 (J_4) = \{J_4,E_1,E_{14},E_{15},E_{16},E_{29},E_{35},E_{36},$ $E_{37},E_{38}\} ;$ $\epsilon^7 (J_5) = \{J_5,E_{24},E_{25},E_{26},E_{29},E_{35},E_{36},E_{37},$ $E_{38}\} .$

Using MC $^{2}$ -simplex tableaus of Model (AM), we can read out $\Gamma_{7}(E_{i}(J_{j}))$ and $\Lambda_{7}(E_{i}(J_{j},\alpha))$ for all $E_{i}$ and $J_{j}$ , as functions of $\alpha_{i}, i=1,2,3$ . For illustration, let $\alpha_{i}^{0}=4, i=1,2,3$ for all $E_{i}$ and $J_{j}$ . That is, $\alpha^{0}=(4,4,4)$ . Then, we obtain all flexible contingency plans selected by Model (M7), as functions of $(\gamma_{1},\lambda_{1})$ , for PGS's $J_{1}, J_{2}, J_{3}, J_{4}, J_{5}$ .

As an illustration, the flexible contingency plans selected by Model (M7) for $J_{2}$ is listed in

Table A.4. Note that the payoff, as a function of $(\gamma_{1}, \lambda_{1})$ and the contingency plan $E_{i}$ , denoted by $V(E_{i}|J_{2})$ , is given in the 4th column of Table A.4. From Table A.4, we also see that there are two alternative contingency plan sets; $\{J_{2}, E_{3}, E_{20}, E_{21}\}$ and $\{J_{1}, E_{3}, E_{20}, E_{21}\}$ , since $J_{2}$ and $J_{1}$ overlap.

We explain Table A.4 as follows:

If PGS $J_{2}$ is chosen and $\{J_{2}, E_{3}, E_{20}, E_{21}\}$ is implemented, (i) when $0 \leq \gamma_{1} \leq 2/3$ and $1/7 \leq \lambda_{1} \leq 1$ occur, we use $J_{2}$ to produce products $\{x_{1}, x_{2}, x_{4}\}$ , which yields the payoff $V(J_{2}|J_{2})$ , and no slack resource is left over; (ii) when $0 \leq \gamma_{1} \leq 1/4$ and $0 \leq \lambda_{1} \leq 1/7$ occur, we use $E_{3}$ to produce $\{x_{1}, x_{4}\}$ , which yields the payoff $V(E_{3}|J_{2})$ (note that $s_{3}$ is the amount of the slack resource left over from constraint 3); (iii) when $1/4 \leq \gamma_{1} \leq 2/3$ and $0 \leq \lambda_{1} \leq 1/7$ occur, we use $E_{20}$ to produce $\{x_{2}, x_{4}\}$ , which yields the payoff $V(E_{20}|J_{2})$ ; (iv) when $2/3 \leq \gamma_{1} \leq 1$ and $0 \leq \lambda_{1} \leq 1$ occur, we use $E_{21}$ , which means that we use the additional resource $y_{1}$ as well as the original resources to produce $x_{2}$ , which yields the payoff $V(E_{21}|J_{2})$ (note that $s_{2}$ is the amount of the slack resource left over from constraint 2).

Alternatively, if $\{J_1, E_3, E_{20}, E_{21}\}$ is implemented, (i) when $0 \leq \gamma_1 \leq 2/3$ and $1/7 \leq \lambda_1 \leq 1$ occur, we use $J_1$ to produce products $\{x_1, x_2\}$ , which yields the payoff $V(J_1|J_2)$ ; (ii) when $0 \leq \gamma_1 \leq 1/4$ and $0 \leq \lambda_1 \leq 1/7$ occur, we use $E_3$ to produce $\{x_1, x_4\}$ , which yields the payoff $V(E_3|J_2)$ ; (iii) when $1/4 \leq \gamma_1 \leq 2/3$ and $0 \leq \lambda_1 \leq 1/7$ occur, we use $E_{20}$ to produce $\{x_2, x_4\}$ , which yields the payoff $V(E_{20}|J_2)$ ; and (iv) when $2/3 \leq \gamma_1 \leq 1$ and $0 \leq \lambda_1 \leq 1$ occur, we use $E_{21}$ , which means that we use the additional resource $y_{1}$ as well as the original resources to produce $x_{2}$ , which yields the payoff $V(E_{21}|J_2)$ .

Table A.4  
Contingency plans for $J_{2}$ with $\alpha^{0} = (4, 4, 4)$

<table><tr><td> $\epsilon^7(J_2)$ </td><td> $\Gamma_7(E_i(J_2))$ </td><td> $\Lambda_7(E_i(J_2))$ </td><td>Payoff  $V(*|J_2)$ </td></tr><tr><td> $x(J_2)=(x_1,x_2,x_4)$ </td><td> $0\leq\gamma_1\leq2/3$ </td><td> $1/7\leq\lambda_1\leq1$ </td><td> $(\lambda_1,\lambda_2)\begin{pmatrix}50 & 100 \\40 & 20\end{pmatrix}\begin{pmatrix}\gamma_1\\ \gamma_2\end{pmatrix}$ </td></tr><tr><td> $x(J_1)=(x_1,x_2,s_3)$ </td><td> $0\leq\gamma_1\leq2/3$ </td><td> $1/7\leq\lambda_1\leq1$ </td><td> $(\lambda_1,\lambda_2)\begin{pmatrix}50 & 100 \\40 & 20\end{pmatrix}\begin{pmatrix}\gamma_1\\ \gamma_2\end{pmatrix}$ </td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

Since for any $(\gamma_{1}, \lambda_{1})$ , there is a contingency plan in $\{J_{2}, J_{1}, E_{3}, E_{20}, E_{21}\}$ which “optimizes” Model (M3), $\{J_{2}, J_{1}, E_{3}, E_{20}, E_{21}\}$ is the set of all flexible contingency plans for $J_{2}$ .

We also know that for each $\Omega_{i}, i=1,\ldots,7$ of Step 3, Model (M8) has no feasible solution when $2/3\leq\gamma_{1}\leq1$ . Similarly, we can use Model (M9) to identify all flexible contingency plans for each $\Omega_{i}$ .

Step 6. For illustrative purposes, let us use the maximizing expected payoff as the criterion to determine the optimality.

We assume that $\gamma_{1}$ is independent of $\lambda_{1}$ , and $(\gamma_{1}, \lambda_{1})$ have the joint and uniform probability distribution $F(\gamma_{1}, \lambda_{1})$ .

Given the option $\{J_2, E_3, E_{20}, E_{21}\}$ for PGS $J_2$ , to find the expected payoff $EV(J_2)$ we have:

$$
\begin{array}{r l} E V (J _ {2}) & = \int_ {R _ {1}} V (J _ {2} | J _ {2}) \mathrm{d} F (\gamma , \lambda) \\ & + \int_ {R _ {2}} V (E _ {3} | J _ {2}) \mathrm{d} F (\gamma , \lambda) \\ & + \int_ {R _ {3}} V (E _ {2 0} | J _ {2}) \mathrm{d} F (\gamma , \lambda) \\ & + \int_ {R _ {4}} V (E _ {2 1} | J _ {2}) \mathrm{d} F (\gamma , \lambda), \end{array}
$$

$$
\text { where } V (J _ {2} \mid J _ {2}) = (\lambda_ {1}, \lambda_ {2}) \left( \begin{array}{c c} 5 0 & 1 0 0 \\ 4 0 & 2 0 \end{array} \right) \binom {\gamma_ {1}} {\gamma_ {2}},
$$

$$
V \left(E _ {3} \mid J _ {2}\right) = \left(\lambda_ {1}, \lambda_ {2}\right) \left( \begin{array}{c c} - 7 0 & 4 0 \\ 6 0 & 3 0 \end{array} \right) \binom {\gamma_ {1}} {\gamma_ {2}},
$$

$$
V \left(E _ {2 0} \mid J _ {2}\right) = \left(\lambda_ {1}, \lambda_ {2}\right) \left( \begin{array}{c c} 1 1 0 & - 2 0 \\ 3 0 & 4 0 \end{array} \right) \binom {\gamma_ {1}} {\gamma_ {2}}, \text { and }
$$

$$
V \left(E _ {2 1} \mid J _ {2}\right) = \left(\lambda_ {1}, \lambda_ {2}\right) \left( \begin{array}{c c} 4 0 & 1 2 0 \\ 1 0 & 8 0 \end{array} \right) \binom {\gamma_ {1}} {\gamma_ {2}},
$$

where $F(\gamma_{1}, \lambda_{1})$ is the cumulative uniform probability distribution function of $(\gamma_{1}, \lambda_{1})$ as assumed; and

$$
R _ {1} = \left\{\left(\gamma_ {1}, \lambda_ {1}\right) \mid 0 \leq \gamma_ {1} \leq 2 / 3 \text { and } 1 / 7 \leq \lambda_ {1} \leq 1 \right\}
$$

$$
R _ {2} = \left\{\left(\gamma_ {1}, \lambda_ {1}\right) | 0 \leq \gamma_ {1} \leq 1 / 4 \text { and } 0 \leq \lambda_ {1} \leq 1 / 7 \right\},
$$

$$
R _ {3} = \left\{\left(\gamma_ {1}, \lambda_ {1}\right) \mid 1 / 4 \leq \gamma_ {1} \leq 2 / 3 \right.
$$

and $0 \leq \lambda_{1} \leq 1 / 7\}$ , and

$$
R _ {4} = \left\{\left(\gamma_ {1}, \lambda_ {1}\right) | 2 / 3 \leq \gamma_ {1} \leq 1 \text { and } 0 \leq \lambda_ {1} \leq 1 \right\}
$$

(see Definition 2.2).

Then, the direct computation offers that $EV(J_{2})=59.83$ . If we use the other options for $J_{2}$ , we get the same result.

Similarly, we have that $EV(J_1) = 59.45$ ; $EV(J_3) = 55.44$ ; $EV(J_4) = 48.05$ ; and $EV(J_5) = 21.66$ , $EV(\Omega_1) = 78.04$ ; $EV(\Omega_2) = 55.64$ ; $EV(\Omega_3) = 58.21$ ; $EV(\Omega_4) = 55.64$ ; $EV(\Omega_5) = 58.21$ ; $EV(\Omega_6) = 55.64$ ; and $EV(\Omega_7) = 35.74$ .

Thus, in view of maximizing expected payoff, $\Omega_{1}$ is the best candidate and can be recommended. If the decision makers agree, then $\Omega_{1}$ is the final optimal production system for production. Otherwise, we need to revise the data about A, C, D, $\alpha$ , and the probability distribution of $(\gamma, \lambda)$ and go back to Step 1 of Procedure 4.1 (see box (9) in Figure 2).

Note that if we use Procedure 4.1 to select optimal production systems with optimal rigid contingency plans, the analysis can be similar done.

## References

[1] A.V. Aho, J.E. Hopcroft and J.D. Ullman, Data Structures and Algorithms (Addison-Wesley, Massachusetts, 1987).

[2] A. Charnes and W.W. Cooper, Management Models and Industrial Applications of Linear Programming Vol. 1 & 2 (Wiley, New York, 1961).

[3] I.S. Chien, Y. Shi and P.L. Yu, MC $^{2}$ Program: A Pascal Program run on PC (revised version), School of Business, University of Kansas, Lawrence KS 66045 (Aug. 1989).

[4] C.W. Churchman, The Systems Approach (Delacorte Press, New York 1968).

[5] N. Dale and D. Orshalick, Introduction to Pascal and Structured Design (D.C. Heath and Company, Massachusetts, 1983).

[6] G.B. Dantzig, Linear Programming and Extensions (Princeton University Press, Princeton, New Jersey, 1963).

[7] J.B. Dilworth, Production and Operations Management (Random House, New York, 1989).

[8] T. Gal, Postoptimal Analyses, Parametric Programming, and Related Topics (McGraw-Hill, New York, 1979).

[9] J. Heizer and B. Render, Production and Operations Management (Allyn and Bacon, Massachusetts, 1991).

[10] R.L. Keeney and H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs (Wiley, New York, 1976).

[11] T.C. Koopmans, Analysis of Production as An Efficient Combination of Activities, in: T.C. Koopmans, Ed., Activity Analysis of Production and Allocation (Wiley, New York, 1951).

[12] Y.R. Lee, Y. Shi and P.L. Yu, Linear Optimal Designs and Optimal Contingency Plans, Management Science 36, No. 9 (Sept. 1990).

[13] L. Seiford and P.L. Yu, Potential Solutions of Linear Systems: The Multi-criteria Multiple Constraint Level Program, Journal of Mathematical Analysis and Applications 69, No. 2 (1979).

[14] Y. Shi, Optimal Linear Production Systems: Models, Algorithms, and Computer Support Systems, Ph.D. Dissertation, School of Business, University of Kansas (Aug. 1991).

[15] Y. Shi and P.L. Yu, An Introduction to Selecting Linear Optimal Systems and Their Contingency Plans, in: G. Fandel and H. Gehring, Eds., Operations Research (Springer-Verlag, Berlin, 1991).

[16] Y. Shi and P.L. Yu, Selecting Optimal Linear Production Systems in Multiple Criteria Environments, Computer and Operations Research 19, No. 7 (1992).

[17] Y. Shi, P.L. Yu, C. Zhang and D. Zhang, Generating New Ideas Using Union Operations over Primitives, Working Paper No. 92-4, College of Business Adminis

tration, University of Nebraska at Omaha, Omaha, NE 68182 (1992).

[18] P.L. Yu, Multiple Criteria Decision Making: Concepts, Techniques and Extensions (Plenum, New York, 1985).

[19] P.L. Yu and M. Zeleny, The Set of All Nondominated solutions in Linear Cases and A Multi-Criteria Simplex Method, Journal of Mathematical Analysis and Applications 49, No. 2 (1975).

[20] M. Zeleny, An External Reconstruction Approach (ERA) to Linear Programming, Computer and Operations Research 13, No. 1 (1986).

[21] M. Zeleny, Optimizing Given Systems vs. Designing Optimal Systems: The De Novo Programming Approach, International Journal of General Systems 17, (1990).

[22] W.T. Ziemba and R.G. Vickson, Eds., Stochastic Optimization Models in Finance (Academic Press, New York, 1975).
