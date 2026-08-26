---
otero_id: 17095
otero_key: "S664V9VZ"
title: "A DSS oriented method for multiobjective linear programming problems"
authors: "J. Siskos; D.K. Despotis"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90027-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS Oriented Method for Multiobjective Linear Programming Problems

J. SISKOS \* and D.K. DESPOTIS \*\*

\* Technical University of Crete, 73100 Chania, Greece and
\*\* Piraeus Graduate School of Industrial Studies, Department of Statistics and Computer Science, 185 32 Piraeus, Greece

Most of practical linear programming problems involve multiple and conflicting objectives. The paper presents an interactive method to approach this kind of problems. The main original aspect of this method lies in the fact that it combines the advantageous features of both the paradigms of Satisfactory Goals and Multiattribute Utility Assessment. It is a DSS oriented approach providing a 'two level' interaction: (1) interactive assessment of the decision maker's utility function using the UTA ordinal regression model; (2) interactive modification of the satisfaction levels. Piecewise linear optimization techniques are used to determine, at each iteration, a new compromise solution over the set of efficient solutions.

Keywords: Multiple Criteria Decision Making, Linear Programming.

![](/api/attachments/S664V9VZ/fulltext/images/3e8f802d98887b2aaff8952adec774e33cc1dbe12b1607766d6a4affc284a749.jpg)

Yannis Siskos received a D.E.A. (1977) and a Doctorat 3 $^{e}$ Cycle (1979) in computer science and operational research from the university 'Pierre et Marie Curie' and his Doctorat d'Etat (1984) in management science from the University 'Paris-Dauphine' in France. He is currently professor at the Technical University of Crete. Between 1982–84 has been Maitre-Assistant at the University Paris-Dauphine. His research interests fall into the areas of multiple criteria decision making and the design and development of decision support systems for large scale managerial tasks. He is the author of over 40 articles in several journals.

## 1. Introduction and Background

Whenever a decision is to be made, the objectives involved in the decision problem are multiple and in most cases competitive. However, simultaneous optimization of these objectives within the frame of Multiple Objective Mathematical programming (MOMP) is usually unattainable due to their conflicting nature.

According to Simon's [24], Keen's and Scott Morton's [19] classification of decision tasks, MOMP problems are in fact semistructured in nature and call for implicit or explicit trade-off decisions in order to attain the best compromise solution. Texts and surveys on MOMP and its applications can be found in Zeleny [30], Hwang and Masud [14], Goicoechea et al. [11], Chankong and Haimes [4], Evans [7], Roy [22], Cohon and Marks [6] and Choo and Atkins [5].

The decision situation dealt with in this paper is defined as follows:

(a) There are m continuous decision variables $\underline{x} = (x_{1}, x_{2}, \ldots, x_{m})$ .

(b) There is a polyhedral set of alternatives A, which is implicitly dictated by a set of well defined linear constraints.

(c) There are n explicitly defined linear objectives $g_1, g_2, \ldots, g_n$ , all real valued functions of $\underline{x}$ .

(d) There is a decision maker who has an implicit, unknown utility function $U$ , such that if $\underline{x}$ , $\underline{y}$ are two alternative solutions of the set $A$ , $\underline{x}$ is preferred to $\underline{y}$ iff $U(\underline{g}(\underline{x})) > U(\underline{g}(\underline{y}))$ and $\underline{x}$ is indifferent to $\bar{y}$ iff $U(\underline{g}(\underline{x}) = U(\underline{g}(\underline{y}))$ , where $\underline{g}(\underline{x}), \underline{g}(\underline{y})$ are the multiobjective consequences of the alternatives $\underline{x}$ and $\underline{y}$ respectively.

![](/api/attachments/S664V9VZ/fulltext/images/3af03c227d6589070f837eff22f30fc33e10aaf7d0b6716429a07ff5b1b9839b.jpg)  
Dimitris K. Despotis received a Doctorat from the Graduate School of Industrial Studies, Piraeus, Greece, His specialization is in Multiple Criteria Decision Making. He is currently a Lecturer of Mathematical Programming and Operations Research at the Piraeus Graduate School of Industrial Studies. His research interests include Management Information Systems and Decision Support Systems.

This is a typical Multiple Objective Linear Programming (MOLP) problem which can be summarized in the following mathematical model:

$$
\max U \left[ g _ {1} (\underline {{x}}), \dots , g _ {n} (\underline {{x}}) \right] = U \left(c _ {1} ^ {T} \underline {{x}}, \dots , \underline {{c}} _ {n} ^ {T} \underline {{x}}\right)
$$

subject to

$$
\underline {{{x}}} \in A = \left\{\underline {{{x}}} \in R ^ {m} \colon \mathscr {A} \underline {{{x}}} \leqslant \underline {{{b}}}, \underline {{{x}}} \geqslant 0 \right\},\tag{1}
$$

where $\mathcal{A}$ is the matrix of the coefficients of the constraints, $\underline{b}$ is the right-hand side of the constraints and $c_{j} = (c_{j1},\ldots ,c_{jm})$ are the coefficients of the objective $g_{j}$ .

However, if the utility function is not stated explicitly in the problem formulation, problem (1) is converted to the following Vector Maximization Problem

$$
\begin{array}{l} \max \left[ g _ {1} (\underline {{x}}), \dots , g _ {n} (\underline {{x}}) \right] \\ \text { subject   to } \\ \underline {{x}} \in A. \end{array}\tag{2}
$$

Hitherto, several interactive methods for handling such problems have been proposed. All these methods, based on a progressive articulation of preferences, aim to attain the best compromise solution, usually by means of single objective optimization related to the original MOLP. The various methods are distinguished by the kind of information required by the decision maker (i.e. implicit or explicit trade off information, ranking order alternatives, ...) as well as the type of single objective program used to estimate a new compromise solution at each iteration.

Most, if not all, of the methods seem to suffer from various kinds of drawbacks. Naslund [21], Wallenius [27], Hemming [12,13], Larichev and Nikiforov [20] and Roy [23] discuss some properties such as convergence, simplicity of information required, insensitivity to wrong estimations, efficiency of the compromise solutions, meaning and validity which provide relevant criteria to compare the various methods.

However, Jelassi [18] states that the existing methods have been implemented as 'stand-alone' systems with no support for intercommunication and information exchange. Moreover, he distinguishes five generations of multiple criteria decision support systems (MCDSS), according to their software structure and system capabilities and provides some abstract guidelines for future MCDSS development.

Some methods like Benson's Method of Satisfactory Goals [3] and most of Goal Programming techniques applied on MOLP problems, require the decision maker to set and probably reset his aspiration levels for each objective in an interactive way throughout the process (1st paradigm). Although these approaches seem to be attractive, since the final compromise lies within predetermined bounds for the objective values, the determination of initial feasible goals is rather difficult and usually time consuming. Furthermore, there is lack of rationalism for the compromise solutions obtained by this kind of methods, since the utility function of the decision maker is not stated explicitly.

Other methods exploit in a direct way the decision maker's utility function and seek the best compromise solution through successive maximization of the utility functions assessed locally at each iteration (2nd paradigm). Representative methods of this kind are the method of Zionts and Wallenius [31] and some modifications of it such as [28], which are characterized by the assumption of linearity for the utility function. However, the compromise solutions obtained are efficient extreme points in the decision space, a fact that lies against the ideas of compromise programming.

The main drawback of these latter type of methods is the fact that, although they satisfy the condition of rationalism, since the best compromise solution is reached by the maximization of a global criterion which reflects the preferences of the decision maker, the solution obtained may lie outside inherent but undetermined satisfaction levels for each objective.

The main original aspect of the method presented in this paper lies in the fact that combines both the paradigms stated above.

It is a DSS oriented method providing a 'two-level' interaction:

\- Interactive assessment of decision maker's utility function.

\- Interactive modification of the satisfaction levels.

Recently, Jacquet-Lagrèze, Meziani and Slowinski [15] presented a method which seeks a compromise solution by maximizing an overall additive utility function which is assessed using the software PREFCALC [16]. The interaction of this method is limited only to the assessment of the decision maker's utility function.

The paper is organized as follows. In section 2 the outline and the flow-chart of the method are presented. Section 3 provides a step-by-step description of the method and some analysis. Section 4 provides some computational aspects. Finally, a discussion on the proposed method an concluding remarks are provided in section 5.

## 2. Outline of the Method

The interactive method presented here is for handling MOLP problems of type (1). Its flowchart is presented in fig. 1.

The method consists of a preliminary and iterative part. In the preliminary part and in the first step, after the MOLP problem has been clearly formulated, each individual objective is optimized on the set of the feasible solutions. In this way, the ideal values (i.e. the initial upper bounds for the objectives) are calculated.

The anti-ideal values, which represent the initial lower bounds for the objectives, are obtained by minimizing each objective separately. In a second step an initial efficient solution (i.e. a solution which is not dominated by any other acceptable solution in the decision space [cf. 10]) is estimated, closest to the ideal with respect to the weighted Tchebycheff norm. The weights are calculated mechanically in a way similar to that in Step Method (STEM) of Benayoun et al. [2].

Little effort is devoted in this preliminary part to finding high-quality bounds for the objectives since the method itself enables the decision maker to modify these bounds progressively throughout the process. Thus, the decision maker is not involved in this stage.

The iterative part of the method can be resolved in four major successive stages.

## Stage 1

At each iteration throughout the process, the decision maker is faced with a new compromise solution obtained with the maximization of his utility function, except for the initial solution which is reached in a different way described above. In this stage the decision maker is asked which objective functions she/he insists on increasing. Moreover, he is asked if he intends to decrease some of the other objectives in compensation. This stage can be viewed as a learning process of the feasibility trade-offs among the objectives through the set A.

The decision maker's answers, combined with analogous answers of previous iterations, are used by the method to establish new satisfaction levels (i.e. lower bounds) for the objective functions. However, the decision maker can revise these satisfaction levels by analyzing the local trade-offs among the objectives. This possibility allows the decision maker to remove the consequences of previous answers which eventually contradict with his current desires.

The iterative process terminates, during this stage, when a best compromise solution is reached i.e. when the decision maker is not willing to decrease any objective.

## Stage II

In this stage a simple generation technique is set up to construct a reference set of decision profiles (i.e., a set of vectors of n values that might be assumed by the n objective functions). As long as none of these profiles is to be taken by the decision maker as an acceptable decision, they need not be efficient not even feasible. Thus, the set constructed consists of fictitious alternatives which will be offered later to the decision maker just to reveal his preferences toward them. The alternatives generated for this purpose are in fact equally spaced along a line running between two points of the objective space. Moreover, if the decision maker has chosen the jth objective function to increase then the jth component of the decision profile increases along the line while the others decrease. In this way, the alternatives do not dominate each other and the decision maker is protected from facing trivial situations.

This is a calculation state thus, the decision maker is not involved.

## Stage III

This stage constitutes a learning process of the decision maker's preferences.

A concave additive utility function, which reflects his preferences, is assessed by a modified version of the ordinal regression model UTA [17]. The information required of the decision maker is a weak order (i.e. an order of equivalent classes) over the set of the decision profiles generated in stage II.

![](/api/attachments/S664V9VZ/fulltext/images/bace03af242b82ecb96eceab14d8d31a6b9bd89e7031b6e5716b2de3d8e8fbe1.jpg)  
Fig. 1. The flow-chart of the method.

The UTA procedure uses the preference ranking to generate a tentative utility function; then, if the utility function is not fully consistent with the ranking (fig. 2b) the decision maker is invited to make various adjustments.

The whole interactive process for building the decision maker's utility function is integrated into the decision support system MINORA [29]. This DSS allows the decision maker to learn about any possible inconsistencies through pictorial information provided by the system. When full consistency is achieved (fig. 2a), the assessment process is complete (see [26] for a recent real world application from the venture capital decision making area).

![](/api/attachments/S664V9VZ/fulltext/images/d6472ab32dd61261b8ea9e5ba728f614fe30b1d9b7563e256b080de0bf5841e6.jpg)

![](/api/attachments/S664V9VZ/fulltext/images/023c795bef845cb6a8481196e99dabb8a4940d23bc3ad2bda7b081f59dff3721.jpg)  
Fig. 2. Ordinal regression curves. (a) Full consistency achieved. (b) Case of inconsistencies.

Stage IV

The decision maker's utility function is optimized over the set of the feasible solutions. For this purpose, piecewise linear programming techniques (see [8,9] for instance) are set up since the assessed utility function is piecewise linear in form. This is a calculation stage thus, the decision maker is not involved.

## 3. A Step-by-Step Navigation through the Method

A complete description of the method with some further analysis for each step is given below.

## Initialization

Step 1

Calculate $h_i$ and $l_i$ , for every $i = 1, \ldots, n$ as follows:

(1.1) Set $h_i = g_k(\underline{x}_k^*) = \max_{1, \ldots, n} g_i(\underline{x}), \underline{x} \in A, i = 1, \ldots, n$

(1.2) Set $g_{ij}^{*} = g_{j}(\underline{x}_{i}^{*}), i, j = 1, \ldots, n$

(1.3) Set $f_{j} = \min_{\{i\}} (g_{ij}^{*})$ , $i, j = 1, \ldots, n$

(1.4) Solve $\min g_i(\underline{x}), \underline{x} \in A, i = 1, \ldots, n$

(1.5) If LP in (1.4) is bounded for all $i$ , then set $l_{i} = \min g_{i}(\underline{x}), \underline{x} \in A, i = 1, \ldots, n$

(1.6) If LP in (1.4) is unbounded for all $i$ , then set $l_{i} = f_{i}$ , $i = 1, \ldots, n$

(1.7) If LP in (1.4) is bounded for some $i$ , then for these $i$ set $l_{i} = \min g_{i}(\underline{x}), \underline{x} \in A$ and $l_{j} = h_{j}$ $-(h_j - f_j) \cdot \max_{\{i\}} \{(h_i - l_i) / (h_i - f_k)\}$ $j = 1, \ldots, n, j \neq i$

Step 2

(2.1) Solve the linear program

min z

s.t. $\underline{x} \in A$

$$
\left(h _ {i} - q _ {i} (\underline {{{x}}})\right) m _ {i} \leqslant z, i = 1, \dots , n,\tag{3}
$$

$$
z \geqslant 0,
$$

where $m_{i} = d_{i} / \sum_{k=1}^{n} d_{k}$ and $d_{i} = (h_{i} - l_{i}) / h_{i}$ if $h_{i} > 0$ or $d_{i} = (l_{i} - h_{i}) / l_{i}$ if $h_{i} \leqslant 0$ . Let $\underline{x}^{1}$ and $\underline{g}^{1} = [g_{1}(\underline{x}^{1}), g_{2}(\underline{x}^{2}), \ldots, g_{n}(\underline{x}^{1})]$ be respectively the optimal solution of problem (3) and its multiobjective consequences. The solution $\underline{x}^{1}$ is efficient and is the closest one to the ideal in the sense of the weighted Tchebycheff norm, the weights $m_{j}$ reflecting the sensitivity of each objective in varying $\underline{x}$ .

(2.2) Set $q = 1$ and $l_i^0 = l_i$ for every $i = 1, \ldots, n$ . Here, $l_i^0$ and $h_i$ are respectively the lower and the upper bounds for the objectives, dictated initially by the problem itself.

Stage I

Step 3

Modify the satisfaction levels of the objectives as follows:

(3.1) Ask the decision maker:

'Is there any satisfactory objective value in $g^q$ ? If NO, the multiple objective problem has no satisfactory solution. Ask the decision maker to review the formulation and restart from step 1. If YES, go to (3.2) below.

(3.2) Ask the decision maker to indicate the objectives he insists on increasing. Let $G$ be the whole set of objectives, $GN$ the set of objective indicated within this step and $\tilde{G}$ the complement of $GN$ in $G$ .

(3.3) Ask the decision maker:

'Can any of the objectives in $\tilde{G}$ be decreased?' If NO, $\underline{x}^q$ is the best compromise solution and $\underline{g}_q$ its consequences. STOP. If YES, go to (3.4) below.

(3.4) Set $l_i^q = g_i^q$ for every $g_i \in GN$ . $l_i^q = l_i^{q-1}$ for every $g_i \in \tilde{G}$ .

(3.5) For every $g_k \in GN$ solve the following linear program:

$$
\begin{array}{l} \max g _ {k} (\underline {{x}}) \\ \underline {{x}} \in A, \\ g _ {i} (\underline {{x}}) \geqslant l _ {i} ^ {q}, g _ {i} \in G N, i \neq k, \\ g _ {j} (\underline {{x}}) \geqslant l _ {j} ^ {q}, g _ {j} \in \tilde {G}. \end{array}\tag{4}
$$

Let $g_{k}^{*}$ be the optimal value of the objective function $g_{k}$ in (4).

(3.6) If $g_k^* = h_k$ for every $g_k \in GN$ , go to (3.8), otherwise go to (3.7) below.

(3.7) For every $g_k \in GN$ , for which $g_k^* < h_k$ , ask the decision maker if he intends to decrease some $l_j^q$ 's in order to increase further the objective $g_k$ . This is done with the help of the dual variables associated with the binding $g_j(\underline{x})$ 's of (4). If NO, go to (3.8), otherwise ask the decision maker to indicate acceptable decrements $\Delta_j$ and set $j_j^q = l_j^q - \Delta_i$ for every decreased $l_j^q$ .

(3.8) Set $A^q = A^{q-1} \cap \{ \underline{x} \in R^m / g_i(\underline{x}) \geqslant l_i^q, i = 1, \ldots, n \}$ .

Stage II

Step 4

For a given integer $s$ and $k=0,1,\ldots,s$ generate the reference alternative profiles $g_{k}=(g_{ik}), i=1,\ldots,n$ with respective coordinates defined as follows:

$$
g _ {i k} = \left\{ \begin{array}{l l} l _ {i} ^ {q} + (k / s) * \left(h _ {i} - l _ {i} ^ {q}\right) & \text { for } g _ {i} \in G N \\ h _ {i} - (k / s) * \left(h _ {i} - l _ {i} ^ {q}\right) & \text { for } g _ {i} \in \tilde {G}. \end{array} \right.
$$

The number of the profiles generated by this procedure is $s + 1$ , but it is easy to consider any other decision profile for comparison purposes.

Stage III

Step 5

Present to the decision maker the whole set of the alternative profiles generated within step 4 and ask him to rank order them as follows:

(5.1) Select an alternative $g_{p}$ as a basis.

(5.2) Present the basis to the decision maker and for each other alternative different to $\underline{g}_p$ ask him:

'Which do you prefer, $\underline{g}_p$ , $\underline{g}_k$ or you are indifferent?'

(5.3) Get the set of the alternatives preferred to the basis and the set of the alternatives not preferred to the basis. For each of these sets with cardinal number greater than one, repeat step 5 from (5.1) to (5.3) until the initial set by partitioned into equivalent classes. The number of the pairwise comparisons made by the decision maker is strictly depended on $s$ and can be suggested by the decision maker himself. It can easily be shown that the number of comparisons leading, to a preference ranking is bounded by $s(s - 1)/2$ and takes its maximum value when, during each cycle of comparisons, no indifferences are involved and either the set of the alternatives preferred to the basis or the set of the alternatives not preferred to the basis is null. The choice of $g_p$ is made by the system by bisection.

Step 6

Assess concave additive utilities

$$
u (\underline {{g}}) = \sum_ {i = 1} ^ {n} p _ {i} u _ {i} (g _ {i}),\tag{5}
$$

satisfying the normalization relations

$$
u _ {i} \left(l _ {i} ^ {q}\right) = 0; \quad i = 1, \dots , n,\tag{6}
$$

$$
u _ {i} (h _ {i}) = 1 \quad i = 1, \dots , n,
$$

$$
\sum_ {i = 1} ^ {n} p _ {i} = 1,\tag{7}
$$

(8)

according to the UTA algorithm (see [25] for a complete description).

UTA uses a special linear programming formulation to estimate the marginal utilities $u_{i}$ according to the additive model (5)-(8). This estimation is made after having discretized each interval $[l_i^q, h_i]$ with $a_i$ breakpoints $(a_i \leqslant s + 1): [l_i^q, h_i] = [l_i^q =$ $g_{i}^{1},\ldots,g_{i}^{j},g_{i}^{j+1},\ldots,g_{i}^{ai}=h_{i}]$ . The version of UTA used here assures that the estimated marginal utilities are concave, by incorporating some additional constraints to the original model. Moreover, UTA provides some postoptimality analysis and, in case of multiple optimal solutions of the UTA linear program, finds n characteristic optimal solutions which maximize the relative weights of the utilities $u_{i}$ (cf. [17]). Thus the output of step 6 is a unique utility function, which is either an optimal one or the mean of n postoptimal utility functions.

Table 1  
Programs and their dimensions.

<table><tr><td>Stage</td><td>Purpose</td><td>Type of Program</td><td>Number of Programs</td><td>Number of Variables</td><td>Number of Constraints</td></tr><tr><td rowspan="2">Initialization</td><td>Estimation of the ideal and the anti-ideal values.</td><td>Linear</td><td>2n</td><td>m</td><td>N</td></tr><tr><td>Estimation of an initial efficient solution</td><td>Linear</td><td>1</td><td>m+1</td><td>N+n</td></tr><tr><td colspan="6">Iterative part</td></tr><tr><td>Stage I</td><td>Revision of the satisfaction levels.</td><td>Linear</td><td>IGNI</td><td>m</td><td>N+n-1</td></tr><tr><td>Stage III</td><td>Concave utility assessment</td><td>Linear</td><td>K</td><td>2(s+1)+(∑i=1na_i)-n</td><td>s+1+∑i=1(a_i-2)</td></tr><tr><td>Stage IV</td><td>Estimation of a new compromise solution</td><td>Piecewise Linear</td><td>1</td><td>m</td><td>N</td></tr></table>

## Step 7

Calculate the global utility of each alternative decision profile in the ranking and present to the decision maker the consequences of his judgment policy through the utility-ranking diagram shown in fig. 2.

(7.1) If full consistency is achieved i.e. when the preference ranking is restituted by the model, go to step 8, otherwise go to (7.2) below.

(7.2) Ask the decision maker if he intends to modify the marginal utilities dictated by the model in order to preserve his ranking. If YES, let him modify the marginal utilities and restart step 7. If NO, go to (7.3) below.

(7.3) Ask the decision maker if he intends to modify the previously established preference ranking. If YES, ask him to reorder the alternatives involved in the inconsistencies, get the new weak order and go the step 6. If NO, ask the decision maker to review the multiobjective model and restart from step 1.

## Stage IV

Step 8

Maximize the assessed utility function over the set $A^q$ of the admissible solutions. This is realized by solving a piecewise linear program, since the assessed concave utility function is piecewise linear in form (see [25] for a complete description of the related program). Set $q = q + 1$ , let $\underline{x}^q$ and $g^q$ be respectively the new compromise solution and its consequences and go to step 3.

## 4. Some Computational Aspects

The method requires: (1) A usual simplex routine to carry out the initialization stage as well as steps 3.5 and 6; (2) Piecewise linear programming techniques in order to optimize the decision maker's utility function in stage IV. As long as all marginal utility functions are concave, the algorithm by Fourier [9] could be used ensuring a global optimum. The number of programs solved at each iteration, as well as their type and their dimensions are presented in table 1.

Recall here that n, m, $s + 1$ and $a_{i}$ are respectively the number of the objectives, the number of the decision variables in the original problem, the number of decision profiles generated at each iteration and the number of discrete points taken in the interval of varying the objective $g_{i}$ . Additionally, let N be the number of the constraints in the original MOLP problem and GN (i.e. the cardinal number of GN) the number of the objectives which are to be increased, at each iteration. In stage III, a new linear program is solved whenever the decision maker alters the subjective ranking of the decision profiles. Thus, the number of programs solved within this stage depends on the number (say K) of reorderings.

## 5. Concluding Remarks

A new supportive tool for multiple objective decisions is presented in this paper. The method is built up by taking into account the facilities needed when it would be incorporated into a DSS.

The method helps the decision maker in learning his preferences by analyzing the consequences of his judgement policy. The decision maker, in turn, is free to alter his policy, throughout the process, beeing able to erase undesirable consequences emerging from wrong estimations.

It is ensured that the final compromise solution lies within satisfactory levels of each objective. Furthermore, the final decision, having been achieved by the maximization of the decision maker's utility function, is rationalized by his needs.

The method has been currently integrated into a fully interactive and user friendly system implemented on a IBM-XT microcomputer. Some first experimentation with this system, involving test problems of small sizes and hypothetical decision makers, led to encouraging results maintaining the tractability of the method (see [25] for a numerical illustration of a slightly different version of the method). Of course, much more work has to be done, i.e. testing the effectiveness of the system on large scale problems as well as a comparative evaluation with other existing methods.

## References

[1] Bazarra, M.S., C.M. Shetty, Nonlinear Programming. Wiley, New York, 1979.

[2] Benayoun, R., J. de Montgolfier, J. Tergny, O. Larichev, Linear Programming with Multiple Objective Functions: Step Method (STEM). Mathematical Programming, Vol. 1, No 3, pp. 366–375, 1971.

[3] Benson, R.G., Interactive Multiple Criteria Optimization Using Satisfactory Goals, Ph.D. Thesis, University of Iowa, 1975.

[4] Chankong, V.Y. Haimes, Multiobjective Decision Making. Theory and Methodology. North-Holland, New York, 1983.

[5] Choo, E.U., D.R. Atkins, An Interactive Algorithm for Multicriteria Programming. Compt. and Ops Res. Vol. 7, pp. 81–87, 1980.

[6] Cohon, J.L., D.H. Marks, A Review and Evaluation of Multiobjective Programming Techniques. Water Resources Research, Vol. 11, No 2, pp. 208–220, 1975.

[7] Evans, W.G., An Overview of Techniques for Solving Multiobjective Mathematical Programs. Management Science, Vol. 30, No 11, pp. 1268–1282, 1984.

[8] Fourer, R.; Piecewise Linear Programming. Report, Department of Industrial Engineering and Management Science, Northwestern University, Evanston, 1983.

[9] Fourier, R.; A Simplex Algorithm for Piecewise Linear Programming I: Derivation and Proof. Mathematical Programming, No. 33, pp 204–233, 1985.

[10] Gal, T.; On efficient Sets in Vector Maximization Problems A Brief Survey. European Journal of Operational Research, No 24, pp. 253–264, 1986.

[11] Goicoechea, A., D.R. Hansen, L. Duckstein; Multiobjective Decision Analysis with Engineering and Business Applications. Willey, New York, 1982.

[12] Hemming, T.; Multiobjective Decision Making Under Certainty. Dissertation, Stockholm, 1978.

[13] Hemming, T., Guide Lines for Testing Interactive Multicriterion Methods by Simulation. Proceedings of the VII –th International Conference on Multiple Criteria Decision Making, Vol. 1, pp. 190–199. Kyoto, Japan, 1986.

[14] Hwang C.L., A. Masud, Multiple Objective Decision Making-Methods and Applications. Springer-Verlag, Berlin, 1979.

[15] Jacquet-Lagrèze, E., R. Meziani, R. Slowinski, MOLP with an Interactive Assessment of a Piecewise Linear Utility Function. European Journal of Operational Research, Vol. 31, No 3 pp. 350–357, 1987.

[16] Jacquet-Lagrèze, E., M. Shakun, Decision Support Systems for Semi-structured Buying Decisions. European Journal of Operational Research, Vol. 16, No 1, pp. 48–58, 1984.

[17] Jacquet-Lagrèze, E., J. Siskos, Assessing a set of Additive Utility Functions for Multicriteria Decision Making: The UTA Method. European Journal of Operational Research, Vol. 10, pp. 151–164, 1982.

[18] Jelassi, M.T., MCDM - From 'Stand-Alone' Methods to Integrated and Intelligent DSS. Proceeding of the VII-th International Conference on Multiple Criteria Decision Making, Vol. 1, pp. 250-262. Kyoto, Japan, 1986.

[19] Keen, P., M. Scott-Morton, Decision Support Systems. An Organizational Perspective. Addison-Wesley, 1978.

[20] Larichev, O.I., A.D. Nikiforov, Analytical Survey of Procedures for Solving Multicriteria Mathematical Programming Problems. Proceedings of the VII –th International Conference on Multiple Criteria Decision Making, Vol. 1, pp. 400–414, Kyoto, Japan, 1986.

[21] Naslund, B., Interactive Methods in Multiple Criteria

Optimization. EFI working paper No 6004, Stockholm School of Economics, Stockholm, 1973.

[22] Roy, B., Problems and Methods with Multiple Objective Functions. Mathematical Programming, Vol. 1, No 2, pp. 239–266, 1971.

[23] Roy, B., Meaning and Validity of Interactive Procedures as Tools for Decision Making. European Journal of Operational Research, Vol. 31, pp. 297–303, 1987.

[24] Simon, H., The New Science of Management Decision. Happer and Row, New York, 1960.

[25] Siskos, J., D.K. Despotis, A Multiobjective Linear Programming Algorithm Based on Satisfactory Goals and Interactive Utility Assessment. Cahier du LAMSADE No81, University de Paris-Dauphine, Paris 1987.

[26] Siskos, J., C. Zopounidis, The Evaluation Criteria of the Venture Capital Investment Activity: An Interactive As-

sessment. European Journal of Operational Research, Vol. 31, pp. 304–313, 1987.

[27] Wallenius, J., Interactive Multiple Criteria Decision Methods: An Investigation and an Approach. The Helsinki School of Economics, Helsinki, 1975.

[28] White, D.J., Multi-objective Interactive Programming, J. Oper. Res. Soc., Vol. 31, pp. 517–523, 1980.

[29] Yannacopoulos, D., Mise en Place et Expérimentation d'un Système Interactif d'Aide à la Décision Multicritère. Thèse 3 $^{e}$ cycle, Université de Paris-Dauphine, Paris, 1985.

[30] Zeleny, M., Multiple Criteria Decision Making. McGraw-Hill, New York, 1982.

[31] Zionts, S., J. Wallenius, An Interactive Programming Method for Solving the Multiple Criteria Problem. Management Science, Vol. 22, pp. 652–663, 1976.
