---
otero_id: 17139
otero_key: "AJBV76RQ"
title: "An interactive procedure for multiobjective optimization using nash bargaining principle"
authors: "V. Venugopal; T.T. Narendran"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90019-n"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Interactive Procedure for Multiobjective Optimization Using Nash Bargaining Principle

V. VENUGOPAL and T.T. NARENDRAN
Indian Institute of Technology, Madras-600 036, India

This paper outlines an interactive procedure for finding a 'satisfactory' solution to the multiobjective optimization problems using Nash Bargaining Principle. The concept of 'measure of conflict' has been introduced to elicit tradeoffs between the objectives. The suggested procedure has been implemented on a personal computer and its performance has been compared with the GDF procedure reported in the literature.

Keywords: Multiobjective optimization, Decision making, Nash principle, Decision support.

![](/api/attachments/AJBV76RQ/fulltext/images/7295397f76697484208ef4b8891315b155e73a6a9e8a4dc263991b37a2917ebc.jpg)

![](/api/attachments/AJBV76RQ/fulltext/images/768f37cf3e02c1084b560801966dac3dafe3ac40317d2f0f9bf3064080d75021.jpg)

T.T. Narendran took his PhD in Industrial Engineering from the Indian Institute of Technology, Madras, India in 1984. His professional experience includes teaching and research at I.I.T., Madras in the fields of Operations Research, Operations Management and Computer Simulation. His current areas of interest include Group Technology, Flexible Manufacturing Systems, Scheduling, Multiobjective Decision Making and Discrete Event Simulation.

V. Venugopal took his M.S. in Industrial Management from the Indian Institute of Technology, Madras, India in 1987. He is currently a Research Scholar at I.I.T., Madras. He was a senior Software Engineer at INFOSYS CONSULTANTS Private Ltd. Areas of interest include Multi-objective Decision Making, Decision Support Systems, and Flexible Manufacturing Systems.

## 1. Introduction

## 1.1. Introduction

Multiobjective optimization problems are generally complex and do not admit ‘optimal’ solutions easily. A ‘satisfactory’ solution, in general, is all that can be found. There may be a number of acceptable solutions for such problems; yet control over the selection of a ‘satisfactory’ solution requires the active participation of the decision maker. In view of this requirement, there is an increasing acceptance of interactive procedures, where the decision maker is actively involved in reaching a satisfactory solution.

Amongst the many interactive procedures that have been developed, the GDF procedure $[3]$ was a pioneering effort. It finds the solution using a series of linear approximations coupled with interaction with the decision maker to elicit local tradeoffs. Subsequently a number of procedures emerged, all of them using the idea of interaction with the decision maker(s). The GDF procedure has served as a benchmark for all subsequent interactive methods that have been developed for MODM problems. Most methods have been compared with the GDF procedure for evaluation of their relative performance. We now briefly report other interactive methods that have been developed, to solve MODM problems.

Zionts and Wallenius [15] procedure consists of generating a series of extreme points by minimizing the weighted sum of objective functions. Sadagopan and Ravindran [11] developed an extended procedure to solve the non-linear case, using the Generalized Reduced Gradient algorithm. Marcotte and Soland [8] and Karwan, Zionts and Villarreal [6] proposed interactive procedures for situations involving integer decision variables as well. Zeleny [14] proposed an interactive procedure using the independent concept of the 'displaced ideal'. In this paper, we present an interactive system which uses the Nash principle of bargaining [5] to obtain the ‘satisfactory solution’ (also known as Best Compromise solution in the literature).

## 1.2. Problem Statement

The following multiobjective optimization problem has been considered in this paper:

$$
\underset {X \in S} {\text { maximize }} f = \left\{f _ {1} (X), f _ {2} (X) \dots , f _ {K} (X) \right\},\tag{1}
$$

where X is an n-dimensional vector of decision variables $\{x_{1}, x_{2} \ldots x_{n}\}$ , S is the feasible region defined by a set of constraints and f is the vector of k independent objective functions defined over S. It is assumed that atleast one of the satisfactory solutions is efficient (or non-inferior or non-dominated as otherwise known) so that our search is limited to efficient solutions only.

## 1.3. Outline of the paper

The concepts underlying the proposed procedure are presented in section 2. After reviewing the Nash principle briefly, its relationship to multiobjective optimization problem is outlined. The concept of ‘measure of conflict’ is introduced. Section 3 contains the procedure in detail along with a numerical illustration. Section 4 compares the performance of the procedure with the GDF interactive method reported in the literature. Section 5 summarizes the major contribution of this paper.

## 2. Conceptual development of the procedure

## 2.1. Nash Bargaining Principle

A basic assumption in multi-person game theory is that all the participants wish to maximize their gains; whenever this is not possible, at least a satisfactory solution is sought. The classical additive model $[10]$ can lead to a high measure of satisfaction for some players, yet leave some other players dissatisfied. Naturally, it does not give an individual participant the power to reject a solution if it is found unsatisfactory. Highlighting this point, Nash $[9]$ developed a procedure to satisfy all the participants involved in a bargaining game, using preference functions of the individuals.

The Nash solution computes the gain relative to a base value (otherwise known as security level) that would apply if no agreement were reached. Denoting the payoff to individual i as $p_{i}$ and the base value as $d_{i}$ , the individual with the least to lose if the bargain falls through, poses the greatest threat to striking the bargain and has the highest level of $d_{i}$ . The Nash group decision rule [1] is to

$$
\text { Maximize } \prod_ {i = 1} ^ {k} U _ {i} (p _ {i} - d _ {i}),\tag{2}
$$

where $U_{i}(\cdot)$ is the utility function for the ith participant so that $U_{i}(0)=0$ .

## 2.2. Nash Principle in Multiobjective Optimization

Each objective in the multiobjective optimization problem can be treated as a participant in the bargaining problem. By optimizing the objectives individually, a payoff matrix can be generated, the elements of the matrix being the attainment levels of the individual scalar optimization problems with respect to the different objective functions. The payoff can be treated as outcomes to each participant in the bargaining problem. The minimum level attained for the individual objective functions can be used in the place of base value (or security level). Viewed in this manner the Nash bargaining problem for the multiobjective optimization problem is to

$$
\begin{array}{l l} \text { Maximize } & \prod_ {i = 1} ^ {k} U _ {i} \big [ f _ {i} (X) - f _ {i} ^ {I} \big ] \\ \text { subject   to } & X \in S \\ & f _ {i} (X) \geqslant f _ {i} ^ {I} \quad \forall i, \end{array}\tag{3}
$$

where $f_{i}^{l}$ is the minimum level required for ith objective. To apply the Nash principle to multiobjective optimization without knowing the preference function we first consider the following relaxed problem

$$
\begin{array}{l l} \text { Maximize } & \prod_ {i = 1} ^ {k} \left(f _ {i} (X) - f _ {i} ^ {l}\right) \\ \text { subject   to } & X \in S \\ & f _ {i} (X) \geqslant f _ {i} ^ {l} \quad \forall i. \end{array}\tag{4}
$$

If the decision maker is satisfied with the solution we stop; otherwise, we interact with the decision maker, modify the problem, solve it again and continue until a ‘satisfactory’ solution is reached.

## 3. The procedure

## 3.1. Assumptions

The interactive procedure developed here makes use of the following assumptions:

(a) The decision maker's preference function is not explicitly known; it evolves during the course of interaction process.

(b) The feasible region defined by the constrained set is convex.

(c) The decision maker is willing to specify the information required consistently during the course of interaction.

(d) The preference function is increasing with respect to every objective function, i.e., the decision maker wants to maximize all the objectives (without loss of generality).

## 3.2. Measure of conflict

In a multiobjective problem, any objective can be improved upon only at the cost of one or more of the other objectives. The process of improving one objective and its impact on other objectives can be characterized heuristically by measuring Spearman's rank correlation coefficient $r_{ij}$ [2], between the pair of objectives $i\&j$ . The value of $r_{ij}$ is computed using the column entries in the payoff matrix Y where $Y_{ij}$ measures the attainment with respect to objective j, when objective i is maximized individually. The correlation coefficients indicate the measure of conflict between objectives i and j; The least value of $r_{ij}$ indicating the highest level of conflict. One way to make a rapid search for a 'satisfactory' solution is to identify the most conflicting objective, whenever an objective is to be improved upon. In our procedure, we assume that, at each stage of interaction, the decision maker can identify the ordered set J of objectives that need to be improved beyond the current levels; in other words, the level of attainment of the current solution with respect to objectives in set J, is clearly not satisfactory. Corresponding to every member of J, the most conflicting objective is determined using the measure of conflict. This ordered set is denoted as $\bar{J}$ . Using $\bar{J}$ and through interaction with the decision maker the base values $f_{i}^{l}$ are modified and the problem (4) solved again to find an improved efficient solution. This process is continued until a ‘satisfactory’ solution is reached.

## 3.3.Description

Based on the ideas developed in the previous sub-section our interactive procedure is outlined as follows:

## step 0 (initialization step)

Determine the base values for each objective, $f_{i}^{l}$ , either directly from the decision maker or by solving a set of scalar optimization problems where the individual objectives are minimized. Similarly determine the maximum attainable levels for each objective $f_{i}^{h}$ by solving a set of scalar optimization where the individual objectives are maximized. Construct the payoff matrix $Y$ from the solution of the scalar maximization problems. Set $k = 0$ . Construct the symmetric matrix $R$ of the measure of conflict between all pairs of objectives. Set $k = k + 1$ . Solve (4). Let $X^{k}$ be the solution to (4).

## step 1 (Interaction step)

Interact with the decision maker. If the decision maker is satisfied with $X^{k}$ stop; else obtain the ordered set J of objectives not satisfied. Using the matrix R, identify $\bar{J}_{i}$ indicating the most conflicting objective corresponding to the ith member of J.

## 2 (updating step)

Interact with the decision maker to elicit an updated value for attainment levels of objectives in J. To facilitate interaction, scale the objectives so that

$$
f _ {i} ^ {s} = \frac {f _ {i} (X ^ {k}) - f _ {i} ^ {l}}{f _ {i} ^ {h}},\tag{5}
$$

and request the decision maker to specify $\beta_{\bar{J}_i}$ , a range $0 \leqslant \beta_{\bar{J}_i} < f_{\bar{J}_i}^s$ , $i \in J$ , by which $f_{\bar{J}_i}$ can be decreased; if $\beta_{\bar{J}_i} = 0$ , replace $\bar{J}_i$ with the next most conflicting objective. If $\beta_{\bar{J}_i} = 0$ , $\forall \bar{J}_i$ stop; if for some $i$ , $\beta_{\bar{J}_i} \neq 0$ then update $f_{\bar{J}_i}^l = (f_{\bar{J}_i}^s - \beta_{\bar{J}_i}) f_{\bar{J}_i}^h + f_{\bar{J}_i}^l \forall i \in J$ and $f_i^l = f_i(X^k) \quad \forall i \in \bar{J}^c$ .

step 3 Solve a modified Nash Bargaining problem, viz.,

$$
\begin{array}{l l} \text { Maximize } & \prod_ {i \in J} \left(f _ {i} (X) - f _ {i} ^ {l}\right) \\ \text { subject   to } & X \in S \\ & f _ {i} (X) \geqslant f _ {i} ^ {l} \quad \forall i = 1, 2, \ldots , k. \end{array}\tag{6}
$$

Set $k = k + 1$ ; Let the solution to (6) be $X^K$ ; go to step (1).

Note: In the actual implementation, to elicit $\beta_{\bar{J}_{i}}$ from the decision maker (step 2), an interval halving procedure over $[0, f_{\bar{J}_{i}}^{s}]$ is used.

## 3.4. Further Details

Existence of Nash solution and the fact that the procedure generates an efficient (non-dominated) solution at each step can be easily established [12]. By our assumptions, a ‘satisfactory’ solution in the search region exists and the procedure will converge to that solution, as long as the decision maker gives consistent information during the interaction [4].

## 3.5. Illustrative Example

In order to facilitate verification of results and comparison with the GDF method, problems already addressed in the literature and solved by other methods are chosen as examples. One such problem solved by Sadagopan and Ravindran [12] is given below for illustration:

$$
\begin{array}{l} \text { Maximize } \left\{f _ {1} (X), f _ {2} (X), f _ {3} (X) \right\}, \quad \text { where } \\ f _ {1} (X) = 3 x _ {1} + x _ {2} + 2 x _ {3} + x _ {4}, \\ f _ {2} (X) = x _ {1} - x _ {2} + 2 x _ {3} + 4 x _ {4}, \\ f _ {3} (X) = - x _ {1} + 5 x _ {2} + x _ {3} + 2 x _ {4} \end{array}\tag{7}
$$

$$
\begin{array}{l} \text { subject   to } \\ 2 x _ {1} + x _ {2} + 4 x _ {3} + 3 x _ {3} \leqslant 6 0, \\ 3 x _ {1} + 4 x _ {2} + x _ {3} + 2 x _ {4} \leqslant 6 0, \\ x _ {1}, x _ {2}, x _ {3}, x _ {4} \geqslant 0. \end{array}\tag{8}
$$

In the place of the decision-maker who participates in the interactive procedure, we have an assumed preference function that can be termed a ‘simulated decision-maker’, viz.,

$$
\begin{array}{r l} & U \left[ f _ {1}, f _ {2}, f _ {3} \right] \\ & = - \left(f _ {1} (X) - 6 6\right) ^ {2} - \left(f _ {2} (X) - 8 0\right) ^ {2} \\ & \quad - \left(f _ {3} (X) - 7 5\right) ^ {2}. \end{array}\tag{9}
$$

The satisfactory solution should be the point where U attains its maximum viz., $f^{*} = (26.98, 65.26, 59.30)$ at $X^{*} = (1.49, 5, 26, 0, 17.26)$ as reported in Sadagopan and Ravindran [12] procedure.

A sample session with the decision support system demonstrating the interaction with the simulated decision maker through the preference function (9) is given in appendix 1. Convergence of the method to the satisfactory solution has also been demonstrated.

## 4.1. Implementation

The proposed procedure has been implemented in the form of a decision support system on an IBM-PC compatible computer using BASIC language. The system uses GINO [7] to solve the optimization step of the procedure. On a limited experience with a large number of small-sized problems, the procedure has been successful. The software has been designed to handle a maximum of 50 objectives. More, if needed, can be accommodated by suitable modification of the program. Since it uses the GINO package, the limits of the package will also have to be imposed on any MODM problem to be solved. This study used a version of GINO that can handle 50 variables and 30 constraints. However, versions with higher capabilities do exist and these could be used if the MODM problem consists of larger number of variables and constraints than what is specified here. An experiment to compare the relative performance of the procedure with the successful GDF procedure was conducted using the problems given in appendix 2 and the results are reported in table 1. As can be seen from the results of table 1, our method compares favorably with the GDF procedure.

Relative Performance of the Proposed Procedure with GDF Procedure.

<table><tr><td>Problem</td><td> $U^{*}$ </td><td> $U_{GDF}$ </td><td> $U_{PROPOSED}$ </td><td> $T_{GDF}$ </td><td> $T_{PROPOSED}$ </td></tr><tr><td>1</td><td>-56675.00</td><td>-56675.00</td><td>-56818.68</td><td>0</td><td>0.002</td></tr><tr><td>2</td><td>19.36</td><td>19.35</td><td>19.36</td><td>0.001</td><td>0</td></tr><tr><td>3</td><td>198.00</td><td>198.00</td><td>197.82</td><td>0</td><td>0.001</td></tr><tr><td>4</td><td>-1968.62</td><td>-2782.00</td><td>-1990.00</td><td>0.400</td><td>0.001</td></tr></table>

$^{a}$ $U_{i}=Value of U(\cdot) of alternative selected by i th procedure.$  
$U^{*} = \text{Value of } U(\cdot)$ of the most preferred solution.  
$T_{i} = \text{Ratio } |U_{i} - U^{*}| / U^{*}|$ showing the deviation of the solution obtained by the procedure $i$ from the most preferred solution.

## 5. Conclusion

A general purpose interactive procedure for solving MODM problems has been developed in this paper. Capable of solving any deterministic MODM problem with linear and non-linear objectives and constraints, the method can succeed as long as it does not encounter an irrational/inconsistent decision maker as a participant. The procedure has been verified by solving problems already reported in the literature. The cost of the method is comparable to that of GDF with respect to specific problems, whenever $T_{PROPOSED}$ is lower. It has been developed in all details including a computer implementation in the form of a Decision Support System. The method is useful to top level executives who face the problem of making decisions involving multiple objectives in areas such as production planning, manufacturing, capital budgeting and health care planning system. In our opinion the method is fairly successful and must be a welcome addition to the interactive procedure in vogue.

## Appendix 1

Interactive Decision Making Process

## References

[1] Bodily, S.E. (1985), Modern Decision Making, McGraw Hill.

[2] Leach, C. (1983), Introduction of Statistics -- A Nonparametric Approach for the Social Sciences, John Wiley & Sons, New York.

[3] Geoffrion, A.M., Dyer, J.S., and Feinberg, A. (1972), An interactive approach for multi criterion optimization, with an application to operation of an academic department, Management Science 19 (4), 357–368.

[4] Henig, M.I., Ritz, Z. (1986), Multiplicative decision rules for multiobjective decision problems. European Journal of Operational Research 26, 134–141.

[5] Jones, A.J. (1980), Game Theory: Mathematical models of conflict, Halsted press: a division of John Wiley & Sons, New York.

[6] Karwan, M.H., Zionts, S., and Villareal, B. (1982), An improved interactive multicriteria integer programming algorithm, Working paper no. 530, School of Management, State University of New York at Buffalo.

[7] Leibman, J., Lasdon, L. Schrage, L., Waren, A. (1986), Modelling and Optimization with GINO, The Scientific Press.

[8] Marcotte, O., and Soland, R.M. (1981), An interactive Branch and Bound algorithm for multiple criteria optimization, Report no. T-442, George Washington University.

[9] Nash, J.F. (1950), The bargaining problem, Econometrica 21, 155–162.

[10] Roth, A.E. (1979), Axiomatic Models of Bargaining, Springer, Berlin.

[11] Sadagopan, S., and Ravindran, A. (1986), Interactive algorithm for multiple criteria non-linear programming problems, European Journal of Operational Research 25, 247–257.

[12] Sadagopan, S., Multiple Criteria Mathematical Programming - A unified Interactive Approach, Unpublished Ph.D dissertation, School of Industrial Engineering, Purdue University, West Lafayette Indiana, December 1979.

[13] Venugopal, V. (1987), An interactive algorithm for multi-objective decision making, Unpublished M.S Thesis, I.I.T., Madras, India.

[14] Zeleny, M. (1974), Linear multiobjective programming, Springer Verlag, New York, 378–380.

[15] Zionts, S., and Wallenius, J. (1976), An interactive programming method for solving multiple criteria problem, Management Science 22, 652–653.

<table><tr><td colspan="3">Do you have security level for each objective?</td><td>yes</td></tr><tr><td colspan="3">Type the security level for each objective</td><td></td></tr><tr><td colspan="3">0, -15, -20</td><td></td></tr><tr><td colspan="3">Solution of each single objective optimization (maximization)</td><td></td></tr><tr><td>Objective</td><td>Solution vector</td><td>Objective function value</td><td></td></tr><tr><td>1</td><td>(18, 0, 6, 0)</td><td>66</td><td></td></tr><tr><td>2</td><td>(0, 0, 0, 20)</td><td>80</td><td></td></tr><tr><td>3</td><td>(0, 15, 0, 0)</td><td>75</td><td></td></tr><tr><td colspan="3">The pay-off matrix is</td><td></td></tr><tr><td>66.0000</td><td>30.0000</td><td>-12.0000</td><td></td></tr><tr><td>Y = 20.0000</td><td>80.0000</td><td>40.0000</td><td></td></tr><tr><td>15.0000</td><td>-15.0000</td><td>75.0000</td><td></td></tr><tr><td colspan="3">The matrix of measure of conflict</td><td></td></tr><tr><td>1.000</td><td>0.500</td><td>-1.000</td><td></td></tr><tr><td>R = 0.500</td><td>1.000</td><td>-0.500</td><td></td></tr><tr><td>-1.000</td><td>-0.500</td><td>1.000</td><td></td></tr><tr><td colspan="3">Iteration 1</td><td></td></tr><tr><td colspan="2">Solution vector</td><td>Criterion vector</td><td></td></tr><tr><td colspan="2">(2.7974, 4.6013, 0, 16.6013)</td><td>(29.5948, 64.6013, 53.4177)</td><td></td></tr><tr><td colspan="3">Interaction step</td><td></td></tr><tr><td colspan="3">Are you satisfied with this result?</td><td>no</td></tr><tr><td colspan="3">Which objective function is not satisfactory?</td><td>3</td></tr><tr><td colspan="3">The most conflicting objective with respect to objective 3 is 1</td><td></td></tr><tr><td colspan="3">Updating step</td><td></td></tr><tr><td colspan="3">The % excess amount achieved over the security level with respect to ideal value for each objective is</td><td></td></tr><tr><td>Objective</td><td>%Excess</td><td></td><td></td></tr><tr><td>1</td><td>44.84%</td><td></td><td></td></tr><tr><td>2</td><td>99.50%</td><td></td><td></td></tr><tr><td>3</td><td>97.88%</td><td></td><td></td></tr><tr><td colspan="3">Interval halving routine</td><td></td></tr><tr><td colspan="3">Is the value 14.7974 of objective 1 satisfactory?</td><td>no</td></tr><tr><td colspan="3">Is the value 22.1961 of objective 1 satisfactory?</td><td>no</td></tr><tr><td colspan="3">Is the value 25.8954 of objective 1 satisfactory?</td><td>no</td></tr><tr><td colspan="3">Is the value 27.7451 of objective 1 satisfactory?</td><td>yes</td></tr><tr><td colspan="3">Can the value be reduced further?</td><td>yes</td></tr><tr><td colspan="3">Is the value 26.82029 of objective 1 satisfactory?</td><td>yes</td></tr><tr><td colspan="3">Can the value be reduced further?</td><td>no</td></tr><tr><td colspan="3">Modified Nash step</td><td></td></tr><tr><td colspan="3">Iteration 2</td><td></td></tr><tr><td colspan="2">Solution vector</td><td>Criterion vector</td><td></td></tr><tr><td colspan="2">(1.3285, 5.4174, 0.1632, 17.0909)</td><td>(26.8203, 64.6013, 60.1032)</td><td></td></tr></table>

Interaction step
Are you satisfied with this result? no
Which objective function value is not satisfactory 2
The most conflicting objective with respect to objective 2 is 3
Is the value 20.0515 of objective 3 satisfactory? no
Is the value 40.0773 of objective 3 satisfactory? no
Is the value 50.0902 of objective 3 satisfactory? no
Is the value 55.0967 of objective 3 satisfactory? no
Is the value 59.4773 of objective 3 satisfactory? yes
Can the value be reduced further? no
Modified Nash step
Iteration 3
Solution vector Criterion vector
(1.4203, 5.2595, 0, 17.3001) (26.8203, 65.3610, 59.4774)
Interaction step
Are you satisfied with this result? yes
The solution to the given MODM problem is as follows
Solution vector Criterion vector
(1.4203, 5.2595, 0, 17.3001) (26.8203, 65.3610, 59.4774)

## Appendix 2

The other problems considered for comparison of the performance of the procedure with the GDF method are as follows:

Problem 2:

Maximize $\{f_1(X), f_2(X), f_3(X)\}$ , where $f_1(X) = 4x_1 + x_2 + 2x_3$ , $f_2(X) = x_1 - 3x_2 - x_3$ , $f_3(X) = -x_1 + x_2 + 4x_3$ subject to $x_1 + x_2 + x_3 \leqslant 80$ , $2x_1 + 2x_2 + x_3 \leqslant 60$ , $x_1 - x_2 \leqslant 0$ , $x_1, x_2, x_3 \geqslant 0$ ,

The preference function used to simulate the decision maker's interaction for this problem is

Maximize $U[f_1, f_2, f_3] = -(f_1(X) - 200)^2 - (f_2(X) - 175)^2 - (f_3(X) - 400)^2$ .

The proposed procedure gives the solution

$$
X = (0. 1 3 0 2, 1 5. 0 1 0 5, 6 4. 7 1 8 7)
$$

with the corresponding

$$
\begin{array}{l} f = (1 4 4. 9 6 8 5, - 1 9. 5 5 7 0, 2 7 3. 7 5 5). \\ \text { Problem   3: } \\ \quad \text { Maximize } \left\{f _ {1} (X), f _ {2} (X), f _ {3} (X) \right\}, \quad \text { where } \\ \quad f _ {1} (X) = 3 x _ {1} + x _ {2} + 2 x _ {3} + x _ {4} \\ \quad f _ {2} (X) = x _ {1} - x _ {2} + 2 x _ {3} + 4 x _ {4} \\ \quad f _ {3} (X) = - x _ {1} + 5 x _ {2} + x _ {3} + 2 x _ {4} \\ \quad \text { subject   to } \\ \quad 2 x _ {1} + x _ {2} + 4 x _ {3} + 3 x _ {4} \leqslant 8 0, \\ \quad 3 x _ {1} + 4 x _ {2} + x _ {3} + 2 x _ {4} \leqslant 1 2 0, \\ \quad x _ {1}, x _ {2}, x _ {3}, x _ {4} \geqslant 0. \end{array}
$$

The preference function used to simulate the decision maker's interaction for this problem is

$$
\text { Maximize } U \left[ f _ {1}, f _ {2}, f _ {3} \right] = \left(f _ {1} (X)\right) ^ {0. 2} + \left(f _ {2} (X) + 3 0\right) ^ {0. 3} + \left(f _ {3} (X) + 4 0\right) ^ {0. 5}.
$$

The proposed procedure gives the solution

$$
X = (0. 0 1 3 0, 2 0. 1 1 1 3, 0. 2 3 3 5, 1 9. 6 4 0 3)
$$

with the corresponding

$$
\begin{array}{l} \text { Maximize } \left\{f _ {1} (X), f _ {2} (X), f _ {3} (X) \right\}, \quad \text { where } \\ f _ {1} (X) = 4 x _ {1} + x _ {2} + 5 x _ {3}, \\ f _ {2} (X) = - x _ {1} + 6 x _ {2} + x _ {3}, \\ f _ {3} (X) = 3 x _ {1} + x _ {2} + 2 x _ {3} \\ \text { subject   to } \\ x _ {1} + 2 x _ {2} + 3 x _ {3} \leqslant 1 6 8, \\ 4 x _ {1} + 3 x _ {2} + x _ {3} \leqslant 2 7 6, \\ x _ {1}, x _ {2}, x _ {3} \geqslant 0. \end{array}
$$

The preference function used to simulate the decision maker's interaction for this problem is

$$
\text { Maximize } U [ f _ {1}, f _ {2}, f _ {3} ] = 0. 2 5 f _ {1} (X) + 0. 4 f _ {2} (X) + 0. 3 5 f _ {3} (X).
$$

The proposed procedure gives the solution

$$
X = (9. 6 2 9 9, 7 9. 1 5 3 1, 0. 0 2 1 3)
$$

with the corresponding

$$
f = (1 1 7. 7 7 9 2, 4 6 5. 3 0 9 9, - 5 0 3 0 6 1).
$$
