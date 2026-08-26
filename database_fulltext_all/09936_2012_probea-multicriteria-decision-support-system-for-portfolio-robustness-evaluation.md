---
otero_id: 9936
otero_key: "T3PUXJWG"
title: "PROBE—A multicriteria decision support system for portfolio robustness evaluation"
authors: "João Carlos Lourenço; Alec Morton; Carlos A. Bana e Costa"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# PROBE—A multicriteria decision support system for portfolio robustness evaluation

João Carlos Lourenço <sup>a,</sup>⁎, Alec Morton <sup>b</sup>, Carlos A. Bana e Costa <sup>a</sup>

<sup>a</sup> Centre for Management Studies of Instituto Superior Técnico (CEG-IST), Technical University of Lisbon, Av. Rovisco Pais 1, 1049-001 Lisbon, Portugal <sup>b</sup> Management Science Group, Department of Management, London School of Economics, London WC2A 2AE, United Kingdom

## a r t i c l e i n f o

Article history: Received 11 August 2009 Received in revised form 30 June 2012 Accepted 3 August 2012 Available online 17 August 2012

Keywords: Portfolio decision analysis Resource allocation Portfolio robustness Restricted ef<sup>fi</sup>ciency DSS

## a b s t r a c t

This paper addresses the problem of selecting a robust portfolio of projects in the context of limited resources, multiple criteria, different project interactions and several types of uncertainty. A portfolio of projects is considered an undoubtedly robust choice if for a given uncertainty domain that affects the costs and/or the bene<sup>fi</sup>ts of the projects there is no other portfolio that does not cost more and simultaneously may provide more overall bene<sup>fi</sup>t. We present a new decision support system, PROBE (Portfolio Robustness Evaluation), and the algorithms it implements. PROBE identi<sup>fi</sup>es all ef<sup>fi</sup>cient portfolios and depicts the respective Pareto frontier within a given portfolio cost range, and permits users to analyze, in depth, the robustness of selecting a proposed portfolio. The robustness evaluation starts by identifying competitor portfolios to the proposed portfolio, its similarities and differences in project composition to its competitors, and the regret a decision-maker may have by selecting the proposed portfolio instead of a competitor.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Suppose that a manager is considering several indivisible projects, each expected to add value to his organization, but does not have the funds to capitalize all of them. Faced with this constraint, the manager would like to select the portfolio of projects that provides the organization with the best value for money. An exhaustive analysis of all possible portfolios, from the empty portfolio (in which no projects are funded and no bene<sup>fi</sup>ts are realized) to the full portfolio (which would require all projects to be funded), would be impractical even if the number of projects were not too large. For example, a small sample set of just 20 projects could result in more than one million portfolios (precisely, 2<sup>20</sup>=1,048,576).

A less strenuous and more practical selection strategy would be to prioritize the projects in decreasing order of bene<sup>fi</sup>t-to-cost ratios (assuming that there are no interactions and hence it is meaningful to assess costs and bene<sup>fi</sup>ts for each project) and proceed down the list until the available budget were exhausted [7,16,22,34,36,45,56,62]. The portfolio selected by this approach would produce the highest bene<sup>fi</sup>t for the money spent, but would not necessarily deliver the maximum bene<sup>fi</sup>t for the money available. Alternatively, the manager could pursue an optimization approach, in which the portfolio with the highest bene<sup>fi</sup>t for the budget available would be found by solving a (knapsack) mathematical programming problem [33,48] that maximizes cumulative bene<sup>fi</sup>t without exceeding the budget constraint [28–31,34,37,53,64].

It is well known that the portfolio selected by each of these two approaches (for the same <sup>fi</sup>xed budget) would always be the same if all projects were not only independent but also “completely divisible with constant returns to scale” [65, p. 151] (see also [21]). This is not true when the projects are indivisible, as is assumed in this paper (see Section 2), or when projects interdependences and other types of constraints are present (see Section 3.2). Portfolios selected through the prioritization approach exclude any project with a bene<sup>fi</sup>t-to-cost ratio that is lower (that is, a less “productive” or “profitable” project [13,19]) than the bene<sup>fi</sup>t-to-cost ratio of an unselected project. The same is not necessarily true of portfolios selected through the optimization approach. The aforementioned exclusion makes the former approach appear to be an “intuitive, approximate approach to solving the optimization problem” [18, p. 260]. Kirkwood [34, Chapter 8.1] and Kleinmuntz [37] brie<sup>fl</sup>y discuss pros and cons of these two approaches. Complementary arguments favoring each one of them are presented in Section 2.

Resource allocation decisions often require managers to consider multiple quantitative and qualitative bene<sup>fi</sup>t dimensions (or criteria). In a previous paper [46], we studied commercial off-the-shelf software for multicriteria portfolio analysis that aggregates multiple bene<sup>fi</sup>t criteria additively: Equity [17], HiPriority [40], Logical Decisions Portfolio [44], and Expert Choice Resource Aligner [25]. Of these, Equity and HiPriority follow the prioritization approach, Expert Choice Resource Aligner follows the optimization approach, while Logical Decisions Portfolio implements both approaches.

Section 3 introduces PROBE (Portfolio Robustness Evaluation), a new decision support system for multicriteria portfolio analysis that implements the optimization approach and also <sup>fi</sup>nds the solutions given by the prioritization approach. When several bene<sup>fi</sup>t criteria are de<sup>fi</sup>ned, PROBE calculates the bene<sup>fi</sup>t value of each project through an additive value model. Therefore, the basic project inputs for a multicriteria portfolio analysis are each project's cost and value scores on the bene<sup>fi</sup>t criteria, and the weights that capture tradeoffs between criteria (see Section 3.1). For a resource allocation model de<sup>fi</sup>ned with the data inputted by the user, PROBE identi<sup>fi</sup>es all ef<sup>fi</sup>cient portfolios and depicts the respective Pareto frontier distinguishing the convex from the non-convex ef<sup>fi</sup>cient portfolios, through the algorithms presented in Section 4.1. Various types of constraints can also be incorporated (see Section 3.2) to account for project interactions or interdependencies and other programmatic issues, although model builders should be careful because a temptation for managers is to use constraints to protect existing spend and hence “more and more constraints keep an organisation pumping resources into the status quo, thereby preventing the organisation from moving in new strategic directions” [56, p. 55].

In real-world resource allocation contexts, several sources of uncertainty can affect the precision of some of the model's inputs. Often, a “best” portfolio is selected on the basis of “best guess” input data only. Therefore, to avoid the trap of “false precision” [62] it is wise to evaluate the robustness of the “best” portfolio by simultaneously considering data uncertainties affecting the costs and bene<sup>fi</sup>ts of the portfolios (i.e., imprecise project costs, project bene<sup>fi</sup>t values and criteria weights). Portfolio robustness evaluation (see Section 4.2) has been the core motivation for the conception of PROBE. Our above mentioned study of commercial packages for multicriteria resource allocation and portfolio selection [46] revealed that none of them permit users to perform an a posteriori sensitivity analysis on several inputs simultaneously. The example in Section 5 illustrates how this type of robustness analysis can be conducted with the DSS PROBE within a given uncertainty domain, and <sup>fi</sup>nally the example in Section 6 describes brie<sup>fl</sup>y an application of PROBE to health service planning in Northern Lisbon, which demonstrates the usefulness of the software and the approach. This new DSS extends the original PROBE software [2,9] (which was limited to the preference robustness evaluation of projects) to portfolio decision analysis.

Pioneering work on robustness in multicriteria portfolio analysis was conducted by J. Liesiö, P. Mild and A. Salo [42,43] in the development of RPM, Robust Portfolio Modeling, <sup>fi</sup>rstly outlined in [61] and implemented in the non-commercial software RPM-Decisions (http:// www.rpm.tkk.<sup>fi</sup>/rpm-software.html). However, contrary to PROBE, the multicriteria decision-aid provided by RPM is not concerned with analyzing the “stability” [12] of a solution (or selection). The idea of robustness analysis shared by RPM turns the ex-post sensitivity analysis perspective “upside down” [59], by incorporating uncertainty a priori as “incomplete information” in the formulation of the problem and looking for “good” portfolios: “This incomplete information is modeled through sets of feasible parameter values and decision recommendations are given based on the computation of non-dominated portfolios” $[ 4 1 , { \mathsf { p } } . 1 2 ] .$ There is therefore a basic procedural difference between the robustness approaches of RPM and PROBE (see Section 4.2).

## 2. Basic concepts and portfolio selection approaches

In this paper, portfolio selection is only concerned with a set $X =$ $\{ j : j = 1 , . . . , m \}$ of m projects that are worth funding; it assumes that project proposals that are not worth funding were screened out in a previous phase of the selection process. Conceptually, the bene<sup>fi</sup>t value of a project that does not add value to a portfolio should be zero; consequently, the bene<sup>fi</sup>t value of a project that is worth funding should be de<sup>fi</sup>ned as the value that the project adds to the portfolio [50]. Let $c _ { j } > 0$ and $v _ { j } > 0$ represent, respectively, the cost and the bene<sup>fi</sup>t value of project j of X and B the budget available, and assume there is no cost associated with not funding project j $( j = 1 , . . . , m )$ [18]. (Situations where there are costs associated with not selecting projects are discussed in Section 3.1). Let $r _ { j } = \nu _ { j } / c _ { j }$ be the bene<sup>fi</sup>t-to-cost ratio of projec $\cdot j ( j = 1 , . . . , m )$ . For simplicity, without loss of generality, also assume that the m projects of X are presented in decreasing order by their bene<sup>fi</sup>t-to-cost ratios such that $r _ { j } { \ge } r _ { j + 1 } , j { = } 1 , . . . , m - 1$ , as the four projects (1, 2, 3, and 4) in Table 1 are.

In the ensuing, we will frequently suppose that the value of projects is given by a multiattribute value model. In this case, let $\nu _ { i j }$ be the value score of project j on the bene<sup>fi</sup>t criterion $i , i { = } 1 , { \ldots } , { \dot { n } }$ $\left( n { \ge } 1 \right)$ and w<sub>i</sub> $( w _ { i } \ge 0 )$ the weight of criterion $i , \ i = 1 , . . . , n$ (with $\begin{array} { r } { \sum _ { i = 1 } ^ { n } w _ { i } = 1 ) } \end{array}$ . The bene<sup>fi</sup>t value $\nu _ { j }$ of project j is given by

$$
v _ {j} = \sum_ {i = 1} ^ {n} w _ {i} v _ {i j}.\tag{1}
$$

We will now introduce some concepts which are standard in the literature [24,60], but which we formally de<sup>fi</sup>ne here in our context.

De<sup>fi</sup>nition 1. A portfolio p is a subset of projects of X $( p \subseteq X )$ . It may be that not all combinations of projects are possible as portfolios (e.g. “expand service $S "$ and “contract service $S "$ cannot be done simultaneously as a matter of simple logic) and so their number may be less than $2 ^ { m }$ (see Section 3.2 for more details).

Let $c ^ { p }$ and $\boldsymbol { v } ^ { p }$ be the cost and the bene<sup>fi</sup>t of portfolio p given by, respectively

$$
c ^ {p} = \sum_ {j \in p} c _ {j}\tag{2}
$$

and

$$
v ^ {p} = \sum_ {j \in p} v _ {j} = \sum_ {j \in p} \sum_ {i = 1} ^ {n} w _ {i} v _ {i j}.\tag{3}
$$

De<sup>fi</sup>nition 2. A portfolio p dominates another portfolio d if $c ^ { p } { \leq } c ^ { d }$ and $\nu ^ { p } > \nu ^ { d } ,$ or if $c ^ { p } { < } c ^ { d }$ and $\nu ^ { p } { \geq } \nu ^ { d } .$ A portfolio is efficient (Pareto-ef<sup>fi</sup>cient, Pareto-optimal or non-dominated) when no other portfolio dominates it.

Fig. 1 shows all $( 1 6 = 2 ^ { 4 } )$ portfolios that can be formed with the four projects of Table 1 (including the empty portfolio {}). There are seven ef<sup>fi</sup>cient portfolios, shown as squared dots in Fig. 1; they form the ef<sup>fi</sup>cient or Pareto frontier.

De<sup>fi</sup>nition 3. An ef<sup>fi</sup>cient portfolio p is a convex efficient portfolio if, and only if, there exists a real number $u \in ] 0 , 1 [$ such that for every portfolio d with at least one of $\boldsymbol { v } ^ { d } \neq \boldsymbol { v } ^ { p }$ and $c ^ { d } \neq c ^ { p } , \ u \nu ^ { p } - ( 1 - u )$ $\begin{array} { r } { \dot { c } ^ { p } > u \nu ^ { d } - ( 1 - u ) c ^ { d } . } \end{array}$

De<sup>fi</sup>nition 4. An ef<sup>fi</sup>cient portfolio p is a non-convex efficient portfolio if, and only if, there exist two other ef<sup>fi</sup>cient portfolios l and h with costs $c ^ { l }$ and $c ^ { h } ,$ and bene<sup>fi</sup>ts $\nu ^ { l }$ and $\boldsymbol { v } ^ { h } ,$ and $\mathsf { a } \ \lambda { \in } ] 0 , 1 [$ such that $( \mathrm { i } ) \ c ^ { p } \geq \lambda c ^ { h } + ( 1 - \lambda ) c ^ { l }$ and (ii) $\nu ^ { p } \leq \lambda \nu ^ { h } + ( 1 - \lambda ) \nu ^ { l }$ with at least one of these inequalities strict (that is, p is dominated by a linear combination of l and h).

Proposition 1. No efficient portfolio can be both convex efficient and non-convex efficient.

Proof. Suppose such a portfolio existed. Then it must be the case that there exist ef<sup>fi</sup>cient portfolios l and h, and $\mathsf { a } \lambda { \in } ] 0 , 1 [$ such that $c ^ { p } \geq \lambda c ^ { h } + ( 1 - \lambda ) c ^ { l } ( 4 )$ and $\nu ^ { p } \leq \lambda \nu ^ { h } + ( 1 - \lambda ) \nu ^ { l }$ (5) with at least one inequality strict, and moreover, for some real u∈ $\mathbb { J } 0 , 1 [ , u \nu ^ { p } -$ $( 1 - u ) c ^ { \bar { p _ { > } } } u \nu ^ { \bar { h } } - ( 1 - u ) c ^ { h } \left( 6 \right)$ and $u \nu ^ { p } - ( 1 - u ) c ^ { p } > u \nu ^ { l } - \bar { ( 1 - u ) } c ^ { l } ( 7 )$

Table 1 Bene<sup>fi</sup>t values, costs and bene<sup>fi</sup>t-to-cost ratios of four projects.

<table><tr><td>Projects j</td><td> $v_j$ </td><td> $c_j$ </td><td> $v_j/c_j$ </td></tr><tr><td>1</td><td>3</td><td>4</td><td>0.75</td></tr><tr><td>2</td><td>4</td><td>8</td><td>0.50</td></tr><tr><td>3</td><td>3</td><td>10</td><td>0.30</td></tr><tr><td>4</td><td>2</td><td>8</td><td>0.25</td></tr></table>

![](/api/attachments/T3PUXJWG/fulltext/images/fa9c8e4bc3f980705d49dc881b5b82ce66a64cdfdb70088dc0fb2aa441ff347c.jpg)  
Fig. 1. Chart showing the portfolios that can be formed with the four projects. Ef<sup>fi</sup>cient portfolios are represented by squared dots and dominated portfolios by triangular dots. The composition of each portfolio is shown in brackets next to the corresponding dot.

Multiplying Eqs. (4) and (5) by $- ( 1 - u )$ and u respectively gives − $( 1 - u ) c ^ { p } \leq - \lambda ( 1 - u ) c ^ { h } - ( 1 - \lambda ) ( 1 - u ) c ^ { l }$ and $u \nu ^ { p } { \leq } \lambda u \nu ^ { h } + ( 1 - \lambda ) u \nu ^ { l }$ with one inequality strict, and adding these, and combining with Eqs. (6) and (7) and simplifying gives both $u \nu ^ { l } - ( 1 - u ) c ^ { l } > u \nu ^ { h } -$ $( 1 - u ) c ^ { h }$ and $u \nu ^ { l } - ( 1 - u ) c ^ { \bar { l } } < u \bar { \nu } ^ { h } - ( \bar { 1 } - u ) c ^ { h }$ which is a contradiction.

De<sup>fi</sup>nitions 2, 3 and 4 illustrate the managerial arguments in favor of or against selecting convex versus non-convex ef<sup>fi</sup>cient portfolios. If a decision-maker feels that there is some approximately constant marginal value of money (because she has a good idea of the alternative uses to which unused funds can be put within her organization), so that expenditure c associated with a portfolio (suitably scaled) can be deducted from the bene<sup>fi</sup>t-value v of that portfolio to come up with an overall index $u \nu - ( 1 - u ) ($ of portfolio attractiveness, then she would restrict her focus to convex ef<sup>fi</sup>cient portfolios as de<sup>fi</sup>ned in De<sup>fi</sup>nition 3. If on the other hand, the decision-maker has no such conception of marginal value for money—perhaps because money is made available on an “use it or lose $\mathrm { i t " }$ basis, and if unspent cannot be diverted to other worthwhile purposes [34, p. 205]—then any ef<sup>fi</sup>- cient portfolio (even those which are non-convex ef<sup>fi</sup>cient according to De<sup>fi</sup>nition 4) maximizes value within some budget constraint (by De<sup>fi</sup>nition 2), and so may be a contender for selection.

In Fig. 1, {}, {1}, {1, 2}, {1, 2, 3}, and {1, 2, 3, 4} are convex ef<sup>fi</sup>cient portfolios (they form the convex ef<sup>fi</sup>cient frontier), and {2} and {1, 2, 4} are non-convex ef<sup>fi</sup>cient portfolios.

Non-convex ef<sup>fi</sup>ciency has the following interesting interpretation. For any non-convex ef<sup>fi</sup>cient portfolio $p ,$ we can suppose without loss of generality that $c ^ { l } { < } c ^ { p } { < } c ^ { h }$ and $\scriptstyle { \boldsymbol { \nu } } ^ { l } < { \boldsymbol { \nu } } ^ { p } < { \boldsymbol { \nu } } ^ { h }$ (for each of h and l, either the costs are less or the bene<sup>fi</sup>ts are greater than those of $p ,$ otherwise the inequalities of De<sup>fi</sup>nition 4 cannot hold, and if, for either of h or l, both the costs are less and the bene<sup>fi</sup>ts are greater, then the ef<sup>fi</sup>ciency of p is contradicted). Rearranging (i) and (ii) from De<sup>fi</sup>nition 4 gives $c ^ { p } - c ^ { l } \geq \lambda ( c ^ { h } - c ^ { l } )$ and $\nu ^ { p } - \nu ^ { l } { \le } \lambda ( \nu ^ { h } - \nu ^ { l } )$ (with at least one inequality strict) and dividing the latter inequality by the former gives $\dot { \nu ^ { h } } - \nu ^ { l } \dot { ) / }$ $( c ^ { h } - c ^ { l } ) > ( \nu ^ { p } - \nu ^ { l } ) / ( c ^ { p } - c ^ { l } )$ , which is to say, the marginal bene<sup>fi</sup>t of exchanging h for l is always greater than the marginal bene<sup>fi</sup>t of exchanging p for l. By a similar reasoning $( c ^ { h } - c ^ { p } ) / ( \nu ^ { h } - \nu ^ { p } ) { < } ( c ^ { h } - c ^ { l } ) /$ $( \nu ^ { h } - \nu ^ { l } )$ always holds, by de<sup>fi</sup>nition, whatever constraints are present; i.e. the marginal cost of an additional bene<sup>fi</sup>t unit when selecting h instead of $p$ is always lower than the marginal cost of an additional bene<sup>fi</sup>t unit when selecting h instead of l, which may be a relevant piece of information for decision-making.

Given a <sup>fi</sup>xed budget B, the prioritization approach selects the portfolio formed by the projects $j , j { = } 1 , . . . , k$ with $k \leq m ,$ such that $\textstyle \sum _ { j = 1 } ^ { k } c _ { j } \leq B$ and $\begin{array} { r } { \sum _ { j = 1 } ^ { k + 1 } c _ { j } > B . } \end{array}$ This approach implicitly assumes besides <sup>¼ ¼</sup>the budget constraints no other constraints are binding and that all combinations of projects are possible. It can be easily seen that portfolios built in this way for increasing values B will be ef<sup>fi</sup>cient (because in such a portfolio substituting a project $j { \le } k$ with a set of projects with lesser total cost can only lead to a reduction in overall bene<sup>fi</sup>t), but it can also be easily seen from the observation of the previous paragraph that the non-convex ef<sup>fi</sup>cient portfolios will be omitted, hence the only portfolios formed by this method are convex ef<sup>fi</sup>cient ones. Hence, in the prioritization approach the notion of “value-for-money” of a project [7,55,56] or its “bang-for-the-buck” [13,16,20] is associated with the slope of each project's bene<sup>fi</sup>t-tocost triangle, as shown in Fig. 2 for the four projects of Table 1. The last column of Table 1 shows that the order of selection by prioritization would be: <sup>fi</sup>rst project 1, then project 2, followed by project 3, and <sup>fi</sup>nally project 4. When the budget increases from 0 to 30 (see Fig. 2), the sequence of portfolios selected through the prioritization, from the empty portfolio {} to the full portfolio {1, 2, 3, 4}, starts with portfolio {1} for $4 \le B < 1 2$ , followed by portfolio {1, 2} for $1 2 \leq B < 2 2$ and then portfolio {1, 2, 3} for $2 2 \leq B < 3 0$ (therefore ignoring the non-convex ef<sup>fi</sup>cient portfolios {2} and {1,2,4}).

Alternatively, the portfolio selected by the optimization approach is the optimal solution of the following binary integer programming problem (known as the “0–1 knapsack problem” [47]):

$$
\begin{array}{l l} \text {maximize} & \sum_ {j = 1} ^ {m} v _ {j} x _ {j}, \\ \text {subject to :} & \sum_ {j = 1} ^ {m} c _ {j} x _ {j} \leq B, \\ & x _ {j} \in \{0, 1 \}, j = 1,..., m, \end{array}\tag{8}
$$

where $x _ { j }$ is a binary variable such that $x _ { j } = 1$ if project j is in the optimal portfolio and $x _ { j } = 0$ otherwise.

For the four projects in Table 1 and a budget $B = 2 0$ , the optimal portfolio is {1, 2, 4} with a bene<sup>fi</sup>t of 9 for a cost of 20 (see Fig. 1), whereas the portfolio selected by the prioritization approach, for the same budget, would be {1, 2} with a bene<sup>fi</sup>t of 7 for a cost of 12 (see Fig. 2). Fig. 1 shows that both portfolios are ef<sup>fi</sup>cient, but it seems that optimization identi<sup>fi</sup>es a better portfolio than prioritization, in the sense that {1, 2, 4} is a higher bene<sup>fi</sup>t portfolio which is nevertheless still affordable. However, note that portfolio {1, 2, 4} includes project 4, which is “less productive” than the non-selected project 3 (because $r _ { 4 } < r _ { 3 } ;$ see Table 1), and in this sense one could argue that {1, 2} is a more attractive portfolio.

It is also important to stress that often managers are not only interested in <sup>fi</sup>nding the best solution for a speci<sup>fi</sup>ed resource amount but also in exploring a budget band, namely when a <sup>fi</sup>xed budget is not known at the time of the analysis or is expected to change. In these cases, a conservative argument favors resource allocation processes by order of priority, because additional resources are allocated to projects not yet selected without removing previously selected projects from the “best” portfolio, whereas using the optimization approach may disrupt previous selections. For example, for a budget range of $2 0 \pm 2 ,$ in Fig. 1, portfolio {1, 2} is optimal for $1 8 < B < 2 0 ,$ , then project 4 enters the optimal portfolio when $2 0 { \leq } B { < } 2 2$ , but for $B = 2 2$ project 4 is replaced by project 3. This is because the optimization approach may select any portfolio that is ef<sup>fi</sup>cient, whereas the prioritization approach will only select portfolios that are convex ef<sup>fi</sup>cient. When the optimal solution of the knapsack problem (8) is a convex ef<sup>fi</sup>cient portfolio, the portfolio selected by prioritization is the same, but, when the optimal solution of problem (8) is a non-convex ef<sup>fi</sup>cient portfolio, the portfolio selected by prioritization is the <sup>fi</sup>rst convex ef<sup>fi</sup>- cient portfolio at its left in the convex ef<sup>fi</sup>cient frontier. This portfolio could be found by constraining the knapsack problem in such a way that the optimal solution does not include any project with a lower bene<sup>fi</sup>t-to-cost ratio than a non-selected project. (The prioritization procedure is also known as the “greedy algorithm for the knapsack problem” [33,39]).

![](/api/attachments/T3PUXJWG/fulltext/images/3348ac9d42cdd0dcec05b0f099d3e630a25ae9155d25a59c31b0afee9b4aa646.jpg)  
Fig. 2. Cumulative cost versus cumulative bene<sup>fi</sup>t chart showing the portfolios formed by the bene<sup>fi</sup>t-to-cost ratio approach. The value-for-money of each project is given by the slope of its bene<sup>fi</sup>t-to-cost triangle. The arrow in the value-for-money slopes box shows the direction of improvement of the bene<sup>fi</sup>t-to-cost value of the projects.

The conservative property of convex ef<sup>fi</sup>cient portfolios allows for the de<sup>fi</sup>nition of a funding strategy by order of priority of the projects “that is independent of the funding constraint so that the entire funding decision does not have to be revised every time the funding constraint changes” [15], as it is often desired in both public and private organizational decision contexts (e.g. the case-studies described in [7] and [56] respectively). Unfortunately, this property can be lost when in the presence of project interactions or other constraints (see Section 3.2). Regardless, in this sense convex ef<sup>fi</sup>cient portfolios are less volatile than non-convex ef<sup>fi</sup>cient ones; nevertheless, we consider that this does not justify showing only the former to the decisionmakers, while hiding the latter, nor adopting a “heuristic project prioritization” [38].

Finally, it is worthwhile to raise a technical issue. If there are at least two projects with the same bene<sup>fi</sup>t-to-cost ratio, some convex ef<sup>fi</sup>cient portfolios are not identi<sup>fi</sup>ed by the prioritization approach. For example, if there are only two projects a and b with the same bene<sup>fi</sup>t-to-cost ratios the prioritization approach either selects portfolio {a} followed by portfolio {a, b}—therefore missing portfolio $\{ b \} { - } 0 \mathrm { r }$ it selects portfolio {b} followed by portfolio $\{ a , b \}$ —therefore missing portfolio {a}. The prioritization approach can, however, easily deal with a large number of projects, contrary to knapsack optimization algorithms. Indeed, the knapsack problem (8) is technically dif<sup>fi</sup>cult to solve despite its straightforward structure, due to the integrality constraints $x _ { j } \in \{ 0 , 1 \} , j = 1 , \ldots ,$ m. The knapsack problem is considered to be a nondeterministic polynomial-time hard (NP-hard) problem [26] (a signi<sup>fi</sup>cant number of exact and approximate resolution algorithms for this problem have been thoroughly studied [33,48]).

## 3. Introducing the DSS PROBE

## 3.1. The MCDA and PDA components and basic input data

PROBE is a multicriteria decision support system for portfolio robustness evaluation that integrates two main architectural components: a multicriteria decision analysis (MCDA) component and a portfolio decision analysis (PDA) component.

The MCDA component allows the user to structure the bene<sup>fi</sup>t criteria in the form of a value tree and input data for the costs of the projects and their bene<sup>fi</sup>t scores on each bottom-level criterion of the value tree. Let X be a speci<sup>fi</sup>c set of projects j $( j = 1 , . . . , m )$ de<sup>fi</sup>ned by the user. Even when uncertainty is present, PROBE always asks the user to input, for each project j, a (“best guess”) cost $c _ { j }$ and (“best guess”) bene<sup>fi</sup>t value scores $\nu _ { i j }$ on each bottom-level criterion $i , \ i = 1 , . . . , n \ ( n = 1$ if only one bene<sup>fi</sup>t dimension, such as NPV, is de<sup>fi</sup>ned). For a value tree with only one level of $n > 1$ benefit criteria $i ( i { \bf = } 1 , . . . , n )$ , (“best guess”) weights $w _ { i } ( i { = } 1 , . . . , n )$ should be introduced and PROBE computes the bene<sup>fi</sup>t value v of each project $\textit { i } ( j { = } 1 , . . . , m )$ by applying the non-hierarchical additive model (1). If the value tree has two or more levels below the root node, speci<sup>fi</sup>c weights are de<sup>fi</sup>ned for the criteria at each level and PROBE uses a hierarchical value model to compute an aggregate bene<sup>fi</sup>t value $\nu _ { j }$ for each project j $( j = 1 , . . . , m )$ ) by applying model (1) bottom-up successively. If a branch of risk criteria is included in the value tree set of criteria, the $\nu _ { j }$ of each project j is more adequately designated by “risk-adjusted bene<sup>fi</sup>t” [56]. For the sake of simplicity, without loss of generality, all programs and algorithms presented in this paper assume a non-hierarchical bene<sup>fi</sup>t model, which can be easily extended to the corresponding generic hierarchical formulation implemented in PROBE.

For the given positive project costs $c _ { j }$ and bene<sup>fi</sup>t scores $\nu _ { j } ( j = 1 , \ldots ,$ m), the PDA component solves the knapsack optimization problem (8)—with or without additional linear constraints added by the user to model project interactions (see Section 3.2)—for any <sup>fi</sup>xed budget $B ,$ <sup>fi</sup>nds all ef<sup>fi</sup>cient portfolios, distinguishes convex from non-convex ones (see Section 4.1)—a functionality not included in the software packages analyzed in [46]—and displays the portion of the Pareto frontier for a user-de<sup>fi</sup>ned limited portfolio cost range <sub>X</sub>B; <sup></sup>B  (see Section 4.1). When the number of projects of X is compatible with a reasonable computational time (see Appendix $\mathsf { A } )$ , PROBE can display the full ef<sup>fi</sup>cient frontier, assuming by default $\underline { { B } } = 0$ and $\begin{array} { r } { \bar { B } = \sum _ { j = 1 } ^ { m } c _ { j } . } \end{array}$

<sup>¼ ¼</sup>If there are costs associated with not selecting projects, the total cost of the projects not selected should be subtracted from the budget. This can be modeled by replacing in problem (8) the budget constraint $\begin{array} { r } { \sum _ { j = 1 } ^ { m } c _ { j } x _ { j } \le B } \end{array}$ by $\begin{array} { r } { \sum _ { j = 1 } ^ { m } c _ { j } x _ { j } \le B - \sum _ { j = 1 } ^ { m } c _ { j } ^ { 0 } \big ( 1 - x _ { j } \big ) } \end{array}$ where $c _ { j } ^ { 0 }$ is the cost of not selecting project $j ,$ which is equivalent to $\begin{array} { r } { \sum _ { j = 1 } ^ { m } \left[ c _ { j } x _ { j } + c _ { j } ^ { 0 } \bigl ( 1 - x _ { j } \bigr ) \right] \leq B \mathrm { \ ( s e e \ [ \ 1 8 , 3 5 ] ) } } \end{array}$

Concerning the modeling of uncertainty, PROBE allows the user to input: a set $\Re _ { c }$ of plausible cost ranges $\prod _ { j = 1 , \ldots , m } \left[ \underline { { { c _ { j } } } } , \bar { c } _ { j } \right]$ such that $\underline { { c } } _ { j } \leq$ $c _ { j } \leq \bar { c } _ { j } ( j = 1 , . . . , m ) ;$ ; a set $\Re _ { v }$ <sup>¼</sup>of plausible bene<sup>fi</sup>t scores ranges $\prod _ { j = 1 , \ldots , m i = 1 , \ldots , n } \prod _ { i = 1 , \ldots , n } \left[ \underline { { { \nu } } } _ { i j } , \bar { \nu } _ { i j } \right]$ such that $\underline { { \nu } } _ { i j } \le \nu _ { i j } \le \bar { \nu } _ { i j } ( i { = } 1 , . . . , n ; j { = } 1 , . . . , m ) ;$ and a system of (non-strict) linear inequalities or equalities on the weights (e.g. weights rankings and/or weights ranges) de<sup>fi</sup>ning a polyhedron $\Re _ { w }$ of feasible weights such that $\textstyle w \in { \mathfrak { R } } _ { w } .$ . Observe that as the inequalities are non-strict $\Re _ { w }$ is closed and as the weights are by assumption non-negative and sum to unity $\Re _ { w }$ is bounded, hence $\Re _ { w }$ is compact. The MCDA component uses the additive model to calculate by optimization the feasible bene<sup>fi</sup>t value range $\left[ \underline { { \boldsymbol { \nu } } } _ { j } , \bar { \boldsymbol { \nu } } _ { j } \right]$ de<sup>fi</sup>ned by $\Re _ { v }$ and $\Re _ { w }$ for each project j $( j = 1 , . . . , m )$ as follows: $\underline { { \nu } } _ { j } = \operatorname* { m i n } _ { w \in \Re _ { w } } \sum _ { i = 1 } ^ { n } w _ { i } \underline { { \nu } } _ { i j }$ and $\bar { \nu } _ { j } = \operatorname* { m a x } _ { w \in \mathfrak { R } _ { w } } \sum _ { i = 1 } ^ { n } w _ { i } \bar { \nu } _ { i j } .$ It is within a user-de<sup>fi</sup>ned uncertainty domain ℜ, comprising $\Re _ { c } , \Re _ { \mathfrak { l } }$ and $\Re _ { w }$ that portfolio robustness evaluation takes place (see Section 4.2).

PROBE is coded in the C++ programming language [63], using the C++ Builder development software having Microsoft Windows as its target environment. PROBE requires the user: to create a value tree by adding criteria nodes, which is graphically shown as an inverted tree where the user can easily drag-and-drop nodes; to input criteria weights and to input the data concerning the projects (names, costs and bene<sup>fi</sup>t value scores on each of the bottom-level criteria). PROBE reads and writes its own data <sup>fi</sup>les and can easily exchange pieces of information between its visual components or between its visual components and other programs using the Windows clipboard with cut-and-paste and copy-and-paste functionalities. PROBE uses the mixed integer linear programming (MILP) solver lp\_solve 5.5.2.0 (available at http://sourceforge.net/projects/lpsolve/) to solve the optimization problems included in the PROBE algorithms presented in Section 4. This solver is based on the revised simplex method and on the branch-and-bound algorithm to deal with integer variables. Despite being a user-friendly decision support system, PROBE requires users to have some knowledge of portfolio decision analysis.

## 3.2. Inputting data for modeling project interactions

## 3.2.1. Synergies among projects

To address a synergy between the costs and/or the bene<sup>fi</sup>ts of two projects s and t, an auxiliary project s,t must be added to X together with the synergistic effect on cost $c _ { s , t }$ and the synergistic effect on the bene<sup>fi</sup>t values $\nu _ { i , s , t }$ on each bene<sup>fi</sup>t criterion $i , i { = } 1 , . . . , n$ . PROBE then automatically de<sup>fi</sup>nes an extra binary variable $\boldsymbol { \chi } _ { s , t }$ such that $x _ { s , t } = 1$ if both projects are selected for the portfolio, or $x _ { s , t } = 0$ otherwise, and adds the following three constraints to problem (8):

$$
\begin{array}{l} x _ {s, t} - x _ {s} \leq 0, \\ x _ {s, t} - x _ {t} \leq 0, \\ x _ {s} + x _ {t} - x _ {s, t} \leq 1. \end{array}\tag{9}
$$

Synergies between more than two projects imply adding more constraints. Let us see an example with three projects s, t, and u that synergize only when the three of them are simultaneously included in a portfolio (and they do not synergize when only two are in the portfolio). In this case, an auxiliary project s,t,u must be added to $X ,$ together with their synergistic effect on cost $C _ { S , t , u }$ and on the bene<sup>fi</sup>t values $\nu _ { i , s , t , u }$ on each bene<sup>fi</sup>t criterion $i , i { = } 1 , . . . , n .$ PROBE then de<sup>fi</sup>nes an additional binary variable $\chi _ { s , t , u }$ such that $x _ { s , t , u } = 1$ if the three projects are selected for the portfolio, $\ y _ { 1 } x _ { s , t , u } = 0$ otherwise, and adds the following four additional constraints to problem (8):

$$
\begin{array}{l} x _ {s, t, u} - x _ {s} \leq 0, \\ x _ {s, t, u} - x _ {t} \leq 0, \\ x _ {s, t, u} - x _ {u} \leq 0, \\ x _ {s} + x _ {t} + x _ {u} - x _ {s, t, u} \leq 2. \end{array}\tag{10}
$$

## 3.2.2. Constraints on projects

Besides synergy effects, PROBE also allows the user to add other well known types of constraints to problem (8), to model different types of project interactions, such as: include project $j , x _ { j } = 1 ;$ exclude $\mathrm { p r o j e c t } j , x _ { j } = 0 ;$ dependency between two projects i and j (i can only be selected $\mathrm { i f } \ j$ is also selected), $x _ { i } - x _ { j } \leq 0 ;$ any portfolio including i must also include j and vice versa, $x _ { i } - x _ { j } = 0 ;$ mutual exclusivity of two projects i and $j , x _ { i } + x _ { j } \le 1 ;$ group constraints on a subset G of m<sub>G</sub> projects $( 1 \leq m _ { G } \leq m )$ , such as (with $\begin{array} { l l } { 0 { \leq } q { \leq } m _ { G } ) , } & { \sum _ { j \in G } x _ { j } = q , } \end{array}$ $\textstyle \sum _ { j \in G } x _ { j } \geq q ,$ ; and $\textstyle \sum _ { j \in G } x _ { j } \leq q$

PROBE includes an interface that allows the user to add to problem (8) any other type of linear constraints [14,27,30], e.g. to tackle multi-period budgeting problems. A feasible portfolio is a portfolio that respects all of the constraints introduced by the user.

Henceforth, we will write x P to indicate that x is a member of a subset of $\{ 0 , 1 \} ^ { m }$ de<sup>fi</sup>ned by a family of constraints of the type discussed in this section. We suppose that P captures the set of all 0–1 vectors corresponding to possible portfolios.

## 4. PROBE innovative functionalities

## 4.1. Finding all efficient portfolios within a given portfolio cost range

For project costs $c _ { j }$ and bene<sup>fi</sup>t scores $\nu _ { j } ( j { = } 1 , . . . , m )$ given by the MCDA component, and supposing for now that no project interaction constraints were de<sup>fi</sup>ned, the PDA component starts searching for the ef<sup>fi</sup>cient portfolios, within a given portfolio cost range B; <sup></sup>B , by solving problem (8) with $B = \bar { B }$ : Next, problem (8) is again solved with B equal to the cost of the optimal portfolio previously found minus a small enough amount $\varepsilon ,$ and so on while $\begin{array} { r } { B \geq \underline { { B } } . } \end{array}$ The algorithm designed to implement this process, FindEfficientPortfolios, presented in Fig. 3, is also capable of identifying all possible multiple optimal solutions. Finally, PROBE uses another algorithm, FindConvexEfficientPortfolios, presented in Fig. 4, to differentiate convex ef<sup>fi</sup>cient from non-convex ef<sup>fi</sup>cient portfolios. Additional linear constraints of the types described in Section 3.2 can easily be added to algorithm FindEfficientPortfolios to take project interactions into account when <sup>fi</sup>nding ef<sup>fi</sup>cient portfolios.

We make the following observations.

Proposition 2. With ε sufficiently small, the algorithm FindEfficientPortfolios finds all and only the efficient portfolios within a given portfolio cost range <sub>X</sub>B; <sup></sup>B .

Proof. The algorithm makes repeated calls to the optimization problem opt1, and <sup>fi</sup>nds optimal portfolios $x ^ { * }$ and writes them and the associated bene<sup>fi</sup>ts and costs to a matrix mEP. By the optimality of $x ^ { * } ,$ , the only way $x ^ { * }$ can fail to be ef<sup>fi</sup>cient is if there is a portfolio with the same bene<sup>fi</sup>t but lower cost: however such an $x ^ { * }$ would have been be deleted from $m E P$ by the corresponding while statement. Hence, at the termination of the algorithm, the only entries in mEP will be the ef<sup>fi</sup>cient portfolios along with their bene<sup>fi</sup>ts and costs. It remains to show that the algorithm <sup>fi</sup>nds all ef<sup>fi</sup>cient portfolios (given suf<sup>fi</sup>ciently small ε). To see this, denote the set of all ef<sup>fi</sup>cient portfolios with costs in the range <sub>X</sub>B; <sup></sup>B  by E. Without loss of generality index the portfolios in E as $p ^ { 1 } , . . . , \bar { p } ^ { k }$ such that $c ( p ^ { 1 } ) { \geq } . . . { \geq } c ( p ^ { k } )$ , where $\nu ( p ^ { 1 } ) , . . . , \nu ( p ^ { k } )$ and $c ( p ^ { 1 } ) , . . . , c ( p ^ { k } )$ are the total bene<sup>fi</sup>ts and costs associ ated with these portfolios. Observe that by the assumption of ef<sup>fi</sup>ciency, $\nu ( p ^ { 1 } ) { \geq } . . . { \geq } \nu ( p ^ { \bar { k } } )$ and moreover that for any pair of successive ef<sup>fi</sup>cient portfolios $i , i + 1 ; c ( p ^ { i } ) { = } c ( p ^ { i + 1 } )$ , then $\nu ( p ^ { i } ) { = } \nu ( p ^ { i + 1 } )$ . Partition E into subsets with portfolios p′and $p ^ { \prime \prime }$ in the same subset if and only if the corresponding costs and bene<sup>fi</sup>t values are equal. Denote these subsets as $E _ { 1 } , . . . , E _ { q }$ where the indices of the subsets are congruent with the indices of the contained portfolios (i.e. higher indexed portfolios belong to higher indexed subsets). If the algorithm <sup>fi</sup>nds a portfolio in some subset $E _ { i } ,$ the duplicate checking subroutine will ensure that all such portfolios are written to mEP. The reader will note that the NRS constraints $\left\{ \textstyle \sum _ { j = 1 } ^ { m } x _ { j } x _ { j } ^ { * } \leq \textstyle \sum _ { j = 1 } ^ { m } x _ { j } ^ { * } - 1 \right\}$ ensure that this subroutine does not cycle and so terminates in <sup>fi</sup>nite time. We can observe that appending this constraint to opt1 will only eliminate, besides $x ^ { * } ,$ , portfolios which contain $x ^ { * }$ and so which could not have been feasible at the previous iteration (since, being higher value than $x ^ { * } ,$ they would have been an optimal solution at this iteration). Once the algorithm has exhausted the equivalence class $E _ { i } ,$ opt1 will become infeasible, and the else if statement will be invoked; assuming ε is suf<sup>fi</sup>ciently small, the next solution of opt1 will be a member of $E _ { i + 1 }$ . These remarks, combined with the observation that on initialization, the <sup>fi</sup>rst solution of opt1 will <sup>fi</sup>nd a member of the equivalence class $E _ { 1 } ,$ , demonstrate the truth of Proposition 2. □

Proposition 3. The algorithm FindConvexEfficientPortfolios finds all and only the convex efficient portfolios within a given set of efficient portfolios.

Proof. The algorithm operates on the matrix mEP, of cost–bene<sup>fi</sup>t pairs of all ef<sup>fi</sup>cient portfolios, which at the conclusion of FindEfficientPortfolios has been sorted by increasing order of cost. By Proposition 1, every ef<sup>fi</sup>cient portfolio can be classi<sup>fi</sup>ed as either convex ef<sup>fi</sup>cient or non-convex ef<sup>fi</sup>cient. To see that the algorithm <sup>fi</sup>nds convex ef<sup>fi</sup>cient portfolios, consider the following. The maxSlope generated at the earlier iterations will be nonstrictly greater than the later iterations. To see this, suppose it is not the case that the slopes strictly decline between two iterations. Then there must be points in the cost bene<sup>fi</sup>t space associated with portfolios $i - 1 , \ i , \ i + 1 ; \ ( c ^ { i - 1 } , \nu ^ { i - 1 } ) , \ ( c ^ { i } , \nu ^ { i } ) ,$ $( \stackrel { \cdot } { c } ^ { i + 1 } , \stackrel { i + 1 } { v } ^ { i + 1 } )$ picked out by the algorithm in succession with $c ^ { i - 1 } < c ^ { i } < c ^ { i + 1 }$ and $\ v { V } ^ { i - 1 } < \ v { V } ^ { \dot { i } } < \ v { V } ^ { i + 1 }$ (inequalities can be assumed to be strict because by construction points correspond to distinct ef<sup>fi</sup>cient portfolios) and $( { \nu } ^ { i + 1 } - { \nu } ^ { i } ) / ( { c } ^ { i + 1 } - { c } ^ { i } ) > ( { \nu } ^ { i } \dot { - } { \nu } ^ { i - 1 } ) / ( { c } ^ { i } - { c } ^ { i - 1 } )$ . Because we know the sign of the denominators we can cross-multiply and simplifying gives $\nu ^ { i + 1 } c ^ { i } + \nu ^ { i } c ^ { i - 1 } + \nu ^ { i - 1 } c ^ { i + 1 } > \nu ^ { i } c ^ { i + 1 } + \nu ^ { i - 1 } c ^ { i } + \breve { \nu } ^ { i + 1 } c ^ { i - 1 } .$ . However, it must also be the case that $( \nu ^ { i + 1 } - \nu ^ { i - 1 } ) / ( c ^ { i + 1 } - c ^ { i - 1 } ) { \le } ( \nu ^ { i } - \nu ^ { i - 1 } ) /$ $( c ^ { i } - c ^ { i - 1 } )$ (otherwise the algorithm would have skipped i) and we can likewise cross-multiply that to get $\begin{array} { r } { \nu ^ { i + 1 } c ^ { i } + \nu ^ { i } c ^ { i - 1 } + \stackrel { \bullet } { \nu } ^ { i - 1 } c ^ { i + 1 } \leq \nu ^ { i } c ^ { i + 1 } + } \end{array}$ $\boldsymbol { \nu } ^ { i - 1 } \boldsymbol { c } ^ { i } + \boldsymbol { \nu } ^ { i + 1 } \boldsymbol { c } ^ { i - 1 }$ , and so we have derived a contradiction, so the slopes between consecutive points do indeed nonstrictly decline – we will use this fact later on, so call it (A). We also observe that since slopes between consecutive points decline, then if we have any three points $( c ^ { l } , \nu ^ { l } )$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm FindEfficientPortfolios(c, v, B, B)

Given the cost  $c_{j}$  and benefit value  $v_{j}$  of each project j (j=1,...,m) of a set X of m projects, this algorithm finds the whole set of efficient portfolios for a given portfolio cost range, defined by its lower and upper bounds B and B, respectively. The “solve” call returns “true” when an optimal solution is found, otherwise returns “false”. The  $x \in P$  in “opt1” indicates that x is a member of a subset of  $\{0,1\}^{m}$  defined by a family of constraints of the type discussed in Section 3.2. The efficient portfolios found by the algorithm are stored in matrix mEP with a number of rows equal to the number of efficient portfolios and a number of columns equal to  $m+2$ . Each row stores the data of one efficient portfolio, with its cost inserted in the first cell, its benefit value in the second one, and each of the other m cells corresponding to each project j, j=1,...,m, in such a way that 1 is inserted in cell j+2 if project j is included in the portfolio, or 0 otherwise. When searching for multiple optimal portfolios with the same cost some constraints are added to optimization problem; the set of these constraints is designated by NRS. At the end, the efficient portfolios stored in matrix mEP are sorted by increasing order of cost. The  $\varepsilon$  used in the algorithm should be assigned a small enough positive real number but not smaller than that.

initialization

B :=  $\overline{B}$ ; stop := false; isSearchingMOP := false; r := 0; NRS :=  $\varnothing$ ;  $\varepsilon$  := small enough positive real number

search for efficient portfolios

while (stop = false) do

    opt := solve(opt1) where opt1 = [z := max_x ∑_{j=1}^m v_j x_j, s.t. ∑_{j=1}^m c_j x_j ≤ B, NRS, x ∈ P]

    x* := argmax(opt1)

    if (opt = true and ∑_{j=1}^m c_j x_j* ≥ B) then

    while (z = mEP[r][2] and ∑_{j=1}^m c_j x_j &lt; mEP[r][1] and r &gt; 1) do

    delete row r from mEP; r := r - 1

    end while

    add one row to mEP; r := r + 1

    mEP[r][1] := ∑_{j=1}^m c_j x_j*

    mEP[r][2] := z

    for (j := 1 to m) do

    mEP[r][j + 2] := x_j*

    end for

    if (isSearchingMOP = false) then

    isSearchingMOP := true

    NRS := NRS ∪ {∑_{j=1}^m c_j x_j = ∑_{j=1}^m c_j x_j*}

    NRS := NRS ∪ {∑_{j=1}^m v_j x_j = ∑_{j=1}^m v_j x_j*}

    end if

    NRS := NRS ∪ {∑_{j=1}^m x_j x_j* ≤ ∑_{j=1}^m x_j* - 1}

    else if (isSearchingMOP = true) then

    B := mEP[r][1] -  $\varepsilon$ 

    if (B &lt; B) then

    stop := true

    else

    NRS :=  $\varnothing$ ; isSearchingMOP := false

    end if

    else

    stop := true

    end if

end while

reverse the order of portfolios in mEP

return mEP
</div>

Fig. 3. Algorithm FindEfficientPortfolios.

$( c ^ { p } , \nu ^ { p } ) , ( c ^ { h } , \nu ^ { h } )$ picked out by the algorithm with $c ^ { l } \leq c ^ { p } \leq c ^ { h }$ and $\nu ^ { l } \le \nu ^ { p } \le \nu ^ { h }$ , then it must be the case that $( \nu ^ { h } - \nu ^ { p } ) / ( c ^ { h } - c ^ { p } ) > ( \nu ^ { h } - \nu ^ { l } ) /$ $( c ^ { h } - c ^ { l } )$ (this is an consequence of the elementary arithmetic observation that with a, b, c, d all positive, c/dba/b⇔bcbad⇔ bc+cdbad+cd⇔c/ $d < ( a + c ) / ( b + d ) )$ . We call this fact (B).

Now the proof is by induction. First we establish the base case. The <sup>fi</sup>rst point (i.e. the cost and bene<sup>fi</sup>t associated with the <sup>fi</sup>rst portfolio) $( c ^ { 0 } , \dot { \nu } ^ { 0 } )$ must be convex ef<sup>fi</sup>cient (e.g. by checking the de<sup>fi</sup>nition of non-convex ef<sup>fi</sup>ciency: it obviously cannot be non-convex ef<sup>fi</sup>cient and so by Proposition 1 must be convex ef<sup>fi</sup>cient). To deal with the inductive case we suppose that all points found by the algorithm up to the ith point (which we denote as (c<sup>i</sup>,v<sup>i</sup>)) have been demonstrated convex ef<sup>fi</sup>cient. We now proceed to show that the (i+1)th point $( c ^ { i + 1 } , \boldsymbol { \nu } ^ { i + 1 } )$ is also convex ef<sup>fi</sup>cient, which we do by demonstrating that $1 / [ 1 \dot { + } ( \nu ^ { i + 1 } - \nu ^ { i } ) / ( c ^ { i + 1 } - c ^ { i } ) ]$ is a value of u as speci<sup>fi</sup>ed in De<sup>fi</sup>nition 3. If this number does not ful<sup>fi</sup>ll the conditions of De<sup>fi</sup>nition 3, there exists a point $( c ^ { * } , \nu ^ { * } )$ such that $\nu ^ { * } - [ ( \nu ^ { i + 1 } - \nu ^ { i } ) /$ $( c ^ { i + 1 } - c ^ { i } ) ] c ^ { * } > \nu ^ { i + 1 } - [ ( \nu ^ { i + 1 } - \nu ^ { i } ) / ( c ^ { i + 1 } - c ^ { i } ) ] c ^ { i + 1 } \quad ( 1 1 )$ . We will assume Eq. (11) holds and seek a contradiction. We know that $c ^ { * } \neq c ^ { i }$ because then $\boldsymbol { v } ^ { * } = \boldsymbol { v } ^ { i }$ as noted in the proof of the previous proposition, and so we can restrict our attention to two cases.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm FindConvexEfficientPortfolios(mEP)

Given a matrix mEP of efficient portfolios found with algorithm FindEfficientPortfolios, algorithm FindConvexEfficientPortfolios finds which ones are convex efficient. A new column is added to mEP in position  $m+3$  to register which portfolios (one in each row) are, or are not, convex efficient, in such a way that 1 is inserted in cell  $m+3$  if the corresponding portfolio is convex efficient or 0 otherwise.

initialization

stop := false; pos := 1; lastCol :=  $m + 3$ ; endPos := number of rows of the matrix mEP

add one column filled with zeros to mEP in position lastCol

mEP [1][lastCol] := 1 stores the first efficient portfolio as convex efficient

if (endPos = 1) then if there is only one efficient portfolio the algorithm stops

stop := true

end if

search for convex efficient portfolios

while (stop = false) do

maxSlope := -1; maxIter := -1

for (iter := pos + 1 to endPos) do

if (mEP [iter][1] - mEP [pos][1] = 0) then

maxIter := iter

exit for

else

slope := (mEP [iter][2] - mEP [pos][2]) / (mEP [iter][1] - mEP [pos][1])

if (slope &gt; maxSlope) then

maxSlope := slope; maxIter := iter

end if

end if

end for

mEP [maxIter][lastCol] := 1 stores the convex efficient portfolio found

if (maxIter = endPos) then

stop := true

else

pos := maxIter

end if

end while

return mEP
</div>

Fig. 4. Algorithm FindConvexEfficientPortfolios.

Case 1. If $c ^ { * } > c ^ { i } ,$ we can multiply Eq. (11) through by $( c ^ { i + 1 } - c ^ { i } )$ to get $\begin{array} { r } { \nu ^ { * } c ^ { i + 1 } + \nu ^ { i } c ^ { * } + \nu ^ { i + 1 } c ^ { i } > \nu ^ { i + 1 } c ^ { * } + \nu ^ { i } c ^ { i + 1 } + \nu ^ { * } c ^ { i } } \end{array}$ . However, we know that $( c ^ { i + 1 } , \boldsymbol { \nu } ^ { i + 1 } )$ was chosen to have maximal slope from $( c ^ { i } , \nu ^ { i } )$ and so $( \nu ^ { * } - \nu ^ { i } ) / ( c ^ { * } - c ^ { i } ) { \le } ( \nu ^ { i + 1 } - \nu ^ { i } ) / ( c ^ { i + 1 } - c ^ { i } )$ . Both denominators are positive, so we can cross multiply and get $\nu ^ { * } c ^ { i + 1 } + \nu ^ { i } c ^ { * } + \nu ^ { i + 1 } c ^ { i } \leq \nu ^ { i + 1 } c ^ { * } +$ $\nu ^ { i } c ^ { i + 1 } + \nu ^ { * } c ^ { i }$ , so we have a contradiction and we can conclude that there exists no such point $( c ^ { * } , \nu ^ { * } )$ and $( c ^ { i + 1 } , \boldsymbol { \nu } ^ { i + 1 } )$ is convex ef<sup>fi</sup>cient.

Case 2. ${ \mathrm { I f ~ } } c ^ { * } < c ^ { i } ,$ there must be a k, k+1 with $k + 1 \leq i ; c ^ { k } < c ^ { * } < c ^ { k + 1 }$ and $\nu ^ { k } < \nu ^ { * } < \nu ^ { k + 1 } .$ . Fact (B) tells us that $( \nu ^ { i + 1 } - \nu ^ { i } ) / ( c ^ { i + 1 } - c ^ { i } ) < ( \nu ^ { i + 1 } -$ $\nu ^ { k + 1 } ) / ( c ^ { i + 1 } - c ^ { k + 1 } )$ . Rearranging this give us $\dot { \nu } ^ { k + 1 } - [ \dot { ( \nu } ^ { i + 1 } - \nu ^ { i } ) /$ $( c ^ { i + 1 } - c ^ { i } ) ] c ^ { k + 1 } { < } v ^ { i + 1 } - [ ( \nu ^ { i + \stackrel {  } { 1 } } - \nu ^ { i } ) / ( c ^ { i + \stackrel {  } { 1 } } - c ^ { i } ) ] c ^ { i + 1 }$ and combining this with Eq. (11) gives us $\nu ^ { * } - [ ( \stackrel { . } { \nu } ^ { i + 1 } - \nu ^ { i } ) / ( c ^ { i + 1 } - c ^ { i } ) ] c ^ { * } > \nu ^ { k + 1 } -$ $[ ( \nu ^ { i + 1 } - \nu ^ { i } ) / ( \stackrel { \cdot } { c } ^ { i + 1 } - \stackrel { \cdot } { c } ^ { i } ) ] c ^ { k + 1 } ( 1 2 )$ . Now, we know from the inductive hypothesis that $\nu ^ { * } - [ ( \nu ^ { k + 1 } - \dot { \nu } ^ { k } ) / ( c ^ { k + 1 } - c ^ { k } ) ] c ^ { * } \leq \nu ^ { k + 1 } - [ ( \nu ^ { k + 1 } -$ $\bar { \nu ^ { k } ) } / ( c ^ { k + 1 } - c ^ { k } ) ] c ^ { k + 1 } \ \bar { ( 1 3 ) }$ . We can subtract Eq. (12) from Eq. (13) to get $c ^ { * } [ ( \nu ^ { \dot { k } + 1 } - \nu ^ { \dot { k } } ) / ( c ^ { k + 1 } - c ^ { k } ) - ( \nu ^ { i + 1 } - \dot { \nu } ^ { i } ) / ( c ^ { i + 1 } - c ^ { i } ) ] \stackrel { . } { > } c ^ { k + \frac 1 2 }$ $[ ( \nu ^ { k \stackrel {  } { + } 1 } - \nu ^ { k } ) / ( c ^ { k + 1 } - c ^ { \dot { k } } ) ^ {  } - ( \nu ^ { i + 1 } - \nu ^ { i } ) / ( c ^ { i + 1 } - c ^ { i } ) ]$ . We are now going to use fact (A) which tells us that (because the difference in ratios which appears on both sides is positive) we can divide both sides and the direction of the inequality remains unchanged, so we get $c ^ { * } > c ^ { k + 1 }$ . But this contradicts the de<sup>fi</sup>nition of $c ^ { k + \widetilde { 1 } }$ , so we reject the existence of $( c ^ { * } , \nu ^ { * } )$

From inspection of these two cases, we conclude that $( c ^ { i + 1 } , \nu ^ { i + 1 } )$ is optimized by the line $\nu - [ ( \nu ^ { i + 1 } - \nu ^ { i } ) / ( c ^ { i + 1 } - c ^ { i } ) ] c$ , hence it is convex ef<sup>fi</sup>cient.

To see that the algorithm <sup>fi</sup>nds all convex ef<sup>fi</sup>cient portfolios, suppose that we have convex ef<sup>fi</sup>cient portfolios $l , p ,$ h: $c ^ { l } { < } c ^ { p } { < } c ^ { h }$ and $\nu ^ { l } < \nu ^ { p } < \nu ^ { h }$ and the algorithm skips p. Then, for the algorithm to skip $p ,$ it must be the case that $( \nu ^ { h } \dot { - } \nu ^ { l } \dot { ) } / ( c ^ { h } - c ^ { l } ) > ( \nu ^ { p } - \nu ^ { \overline { { l } } } ) / ( c ^ { p } - c ^ { l } )$ But $c ^ { l } { < } c ^ { p } { < } c ^ { h }$ we can <sup>fi</sup>nd $\lambda ^ { o } { : } c ^ { p } = \lambda ^ { o } c ^ { h } + ( 1 - \lambda ^ { o } ) c ^ { l } .$ . Substituting this into the inequality on the gradients, cross-multiplying and simplifying yields $\nu ^ { p } { < } \lambda ^ { o } \bar { \nu } ^ { h } + \bar { ( 1 - \lambda ^ { o } ) } \nu ^ { \bar { l } } ,$ , so p is non-convex ef<sup>fi</sup>cient by De<sup>fi</sup>nition 4 which is a contradiction. □

## 4.2. Portfolio robustness evaluation

For the given costs $c _ { j }$ and bene<sup>fi</sup>t scores $\nu _ { j } \ ( j { = } 1 , . . . , m )$ of the projects, let $p ^ { * }$ , with cost $c ^ { p ^ { * } }$ and bene<sup>fi</sup>t $\nu ^ { p ^ { * } }$ , be a speci<sup>fi</sup>c ef<sup>fi</sup>cient portfolio selected by the user, either by asking PROBE to <sup>fi</sup>nd the optimal solution of problem (8) for a <sup>fi</sup>xed budget B or by inspection of the ef<sup>fi</sup>cient portfolios found by PROBE within a portfolio cost range B; <sup></sup>B . In one situation or the other, the user may be concerned with the robustness of the choice of $p ^ { * }$ in the face of an uncertainty domain ℜ (comprising $\Re _ { c } , \Re _ { v }$ and $\Re _ { w }$ see Section 3.1), within which $c ^ { p ^ { * } } { \leq } c ^ { p ^ { * } } { \leq } \bar { c } ^ { \bar { p } ^ { * } }$ and $\nu ^ { p ^ { * } } { \leq } \nu ^ { p ^ { * } } { \leq } \bar { \nu } ^ { p ^ { * } }$

De<sup>fi</sup>nition 5. Given an uncertainty domain ℜ, we say that portfolio p′ is restricted efficient relative to $p ^ { * } \operatorname { i f }$ and only if (i) $\begin{array} { r } { \sum _ { j \in p ^ { \prime } \backslash p ^ { * } \underline { { C } } _ { j } \leq \sum _ { j \in p ^ { * } \backslash p ^ { \prime } } \overline { { C } } _ { j } } } \end{array}$ and (ii) there is a combination of feasible weights w and of feasible bene<sup>fi</sup>t value scores v such that $\begin{array} { r } { \sum _ { i = 1 } ^ { n } w _ { i } \big ( \sum _ { j \in p ^ { * } p ^ { \prime } } \nu _ { i j } - \sum _ { j \in p ^ { \prime } \backslash p ^ { * } } \nu _ { i j } \big ) < 0 , } \end{array}$

<sup>¼</sup>The motivation for this restricted ef<sup>fi</sup>ciency concept is that—having formed the expectation that he will purchase p\*—the decision-maker is only interested in portfolios which may cost less than $p ^ { * }$ and of these possibly cheaper portfolios he is only interested in those which may also be better than $p ^ { * } .$ This differs from the standard ef<sup>fi</sup>ciency or non-dominated concept of multiobjective programming, in which the relevant solution concept is the set of all portfolios which could either be better or be cheaper than $p ^ { * } .$ However, that solution concept is both well-studied and, more importantly, not relevant in our context, since large numbers of irrelevant portfolios would qualify as ef<sup>fi</sup>cient or non-dominated in that standard sense (e.g. the empty portfolio containing no projects).

Using algorithm FindCandidates, described in Fig. 5, PROBE identi<sup>fi</sup>es a set of portfolios which contains the set of restricted ef<sup>fi</sup>cient portfolios. Next, PROBE uses algorithm FindRestEfficientPortfolios, described in Fig. 6, to <sup>fi</sup>nd which candidate portfolios $p ^ { \prime }$ are restricted ef<sup>fi</sup>cient relative to the proposed portfolio $p ^ { * }$

Proposition 4. The algorithms FindCandidates and FindRestEfficientPortfolios find all and only the portfolios which are restricted efficient relative to $p ^ { * } .$

Proof. First we show that FindCandidates <sup>fi</sup>nds all the restricted ef<sup>fi</sup>- cient portfolios relative to $p ^ { * } .$ . According to De<sup>fi</sup>nition $5 ,$ conditional ef<sup>fi</sup>ciency has two parts, a cost condition (i) and a bene<sup>fi</sup>t condition (ii). Using the notation of the algorithm, observe that for any portfolio $p ^ { \prime }$ which ful<sup>fi</sup>lls condition (ii), by de<sup>fi</sup>nition there exist $w ^ { o }$ and $ { \boldsymbol { v } } ^ { o }$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm FindCandidates( $\Re, p^{*}$ )

Algorithm FindCandidates selects “candidate portfolios”  $p'$  that may be restricted efficient relative to  $p^{*}$  given an uncertainty domain  $\Re$ . The candidate portfolios  $p'$  are stored in matrix mCP with a number of rows equal to the number of candidate portfolios and a number of columns equal to m. Each row stores the data of one candidate portfolio, with each of the m cells corresponding to each project j, j=1,...m, in such a way that 1 is inserted in cell j if project j is included in the portfolio, or 0 otherwise. When an optimal solution is found the “solve” call returns “true”, otherwise returns “false”. NRS denotes the set of constraints that are used to prevent finding repeated portfolios.

initialization

 $\tilde{v}_{S} := M$ $\tilde{v}_{S}$  is the upper benefit bound and M denotes a huge positive real number

stop := false; NRS := ∅

 $\overline{c}^{p^{*}} := \sum_{j \in p^{*}} \overline{c}_{j}$  stores the maximum cost of portfolio  $p^{*}$  given  $R_{c}$ 

solve(opt1) where opt1 = [z := min_w ∑_{j∈p^{*}} ∑_{i=1}^{n} w_i y_{ij}, s.t. w ∈  $R_w, ∑_{i=1}^{n} w_i = 1$ ]

 $\underline{v}^{p^{*}} = z$ 

stores the minimum benefit of portfolio  $p^{*}$  given  $R_v$  and  $R_w$ 

w* := argmin(opt1) stores the criteria weights that originated  $\underline{v}^{p^{*}}$ 

for (each  $j \in p^{*}$ ) do stores the benefit values of project  $j \in p^{*}$  when the benefit of  $p^{*}$  is minimum

 $\underline{v}_{j} := \sum_{i=1}^{n} w_i^*.\underline{v}_{ij}$ 

end for

for (each  $j \notin p^{*}$ ) do computes the maximum benefit values of projects  $j \notin p^{*}$  given  $R_v$  and  $R_w$ 

solve(opt2) where opt2 = [ $\overline{v}_{j} := \max ∑_{i=1}^{n} w_i \overline{v}_{ij}, s.t. w ∈ R_w, ∑_{i=1}^{n} w_i = 1$ ]

end for

search for candidate portfolios

while (stop = false) do

opt := solve(opt3) where opt3 = [z := max_x ∑_{j∈p^{*}}  $\overline{v}_{j} x_{j} + ∑_{j∈p^{*}} v_{j} x_{j},$ 

s.t.  $\sum_{j∉p^{*}} c_j x_j + \sum_{j∈p^{*}} \overline{c}_j x_j ≤ \overline{c}^{p^{*}}, ∑_{j∉p^{*}} \overline{v}_j x_j + ∑_{j∈p^{*}} v_j x_j ≤ \tilde{v}_S, ∑_{j=1}^{m} x_j x_j^* ≤ ∑_{j=1}^{m} x_j^* - 1, NRS, x \in P)$ $x' := argmax(opt3)$ 

if (opt = true and  $z ≥ \underline{v}^{p^{*}}$ ) then

add one row to mCP; r = r + 1

for (j := 1 to m) do stores the candidate portfolio ( $p'$ ) found

mCP[r][j] :=  $x'_j$ 

end for

if ( $z &lt; \tilde{v}_S$ ) then

 $\tilde{v}_S := z$  lowers the upper benefit bound

NRS :=  $\left\{\sum_{j=1}^{m} x_j x'_j ≤ \sum_{j=1}^{m} x'_j - 1\right\}$  sets NRS to one constraint

else

NRS := NRS ∪  $\left\{\sum_{j=1}^{m} x_j x'_j ≤ \sum_{j=1}^{m} x'_j - 1\right\}$  adds a new constraint to NRS

end if

else

stop := true

end if

end while

return mCP
</div>

Fig. 5. Algorithm FindCandidatePortfolios.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm FindRestEfficientPortfolios($\Re_v, \Re_w, p^*, mCP$)
Algorithm FindRestEfficientPortfolios searches for portfolios that are restricted efficient (the competitor portfolios) relative to $p^*$ (the proposed portfolio) given an uncertainty domain $\Re$. The algorithm analyzes the matrix mCP of candidate portfolios $p'$ previously found by algorithm FindCandidates. The restricted efficient portfolios $p''$ are stored in matrix mRE with a number of rows equal to the number of restricted efficient portfolios and a number of columns equal to $m+1$. Each row stores the data of one restricted efficient portfolio, with the minimum difference in benefit between $p^*$ and $p''$ in the first cell and each of the other m cells corresponding to each project $j, j=1,...m$, in such a way that 1 is inserted in cell $j+1$ if project $j$ is included in the portfolio, or 0 otherwise. When an optimal solution is found the solve call returns “true”, otherwise returns “false”.

initialization
$r := 0$

search for restricted efficient portfolios
for ($k := 1$ to the number of rows of mCP) do
    $p' := mCP[k]$    the candidate portfolio in row k defines $p'$
    opt := solve(opt1) where opt1 = [ $\underline{z} := \min_x \sum_{i=1}^{n} w_i \left( \sum_{j \in p^*,p'} v_{ij} - \sum_{j \in p' \setminus p^*} \overline{v}_{ij} \right)$, s.t. $x \in P, w \in \Re_w, \sum_{i=1}^{n} w_i = 1$] 
    $x'' := \arg\min(opt1)$
    if (opt = true and $\underline{z} &lt; 0$) then    if portfolio $p'$ is restricted efficient relative to $p^*$
    add one row to mRE; $r := r + 1$
    mRE[r][1] := $\underline{z}$    stores the result
    for ($j := 1$ to m) do    stores the competitor portfolio $p''$
    mRE[r][j + 1] := $x_j''$
    end for
    end if
end for
return mRE
</div>

Fig. 6. Algorithm FindRestEfficientPortfolios.

with $\begin{array} { r } { \sum _ { i = 1 } ^ { n } w _ { i } ^ { o } \left( \sum _ { j \in p ^ { * } \backslash p ^ { \prime } } \nu _ { i j } ^ { o } - \sum _ { j \in p ^ { \prime } \backslash p ^ { * } } \nu _ { i j } ^ { o } \right) < 0 , } \end{array}$ , and, because by optimality $\begin{array} { r } { \sum _ { j \in p ^ { \prime } \backslash p ^ { * } } \bar { \nu } _ { j } \geq \sum _ { i = 1 } ^ { n } w _ { i } ^ { o } \sum _ { j \in p ^ { \prime } \backslash p ^ { * } } { \nu } _ { i j } ^ { o } } \end{array}$ and $\begin{array} { r } { \sum _ { i = 1 } ^ { n } w _ { i } ^ { o } \sum _ { j \in p ^ { * } \backslash p ^ { \prime } } v _ { i j } ^ { o } \geq \underline { { \nu } } ^ { p ^ { * } } - } \end{array}$ $\sum _ { j \in p ^ { \prime } \cap p ^ { * } \ J _ { \sim } ^ { \nu _ { j } } }$ , it is also the case that $\begin{array} { r } { \sum _ { j \in p ^ { \prime } \backslash p ^ { * } } \bar { \nu } _ { j } > \underline { { \nu } } ^ { p ^ { * } } - \sum _ { j \in p ^ { \prime } \cap p ^ { * } \backslash j } , } \end{array}$ although the reverse implication does not hold. Call $\begin{array} { r } { \sum _ { j \in p ^ { \prime } \backslash p ^ { * } } \bar { \nu } _ { j } > } \end{array}$ $\begin{array} { r } { \underline { { \nu } } ^ { p ^ { * } } - \sum _ { j \in p ^ { \prime } \cap p ^ { * } \succsim } \nu _ { j } } \end{array}$ , condition (ii′). Hence, if we can enumerate all portfolios which ful<sup>fi</sup>ll (i) and (ii′), we have a superset of the restricted ef<sup>fi</sup>cient portfolios. Associate with each portfolio $p ^ { \prime }$ in this superset a valuation of $p ^ { \prime }$ according to the function $\begin{array} { r } { \sum _ { j \in p ^ { \prime } \backslash p ^ { * } } \bar { \nu } _ { j } + \sum _ { j \in p ^ { \prime } \cap p ^ { * } \backslash j } } \end{array}$ and call this valuation $\nu ( p ^ { \prime } ) .$ . This gives us an ordering on the superset (not necessarily strict). FindCandidates proceeds down this list from high to low $\nu ( p ^ { \prime } )$ through successively solving opt3. The constraint set ensures condition (i) is met by the constraint $\begin{array} { r } { \sum _ { j \not \in p ^ { * } \underline { { C } } _ { j } } x _ { j } + \sum _ { j \in p ^ { * } } \bar { C } _ { j } x _ { j } \leq \bar { c } ^ { p ^ { * } } } \end{array}$ -. p\* itself is eliminated by the constraint $\textstyle \sum _ { j = 1 } ^ { m } x _ { j } x _ { j } ^ { * } { \leq } \sum _ { j = 1 } ^ { m } x _ { j } ^ { * } - 1$ . Cycling is prevented by <sup>¼ ¼</sup>means of the NRS constraints, and growth in the NRS constraint set is managed by tightening the bound $\tilde { \nu } _ { S }$ which makes at least one of constraints in NRS redundant. The NRS constraints also ensure that where there are multiple portfolios with equal valuations, all will be enumerated, in a manner similar to that of FindEfficientPortfolios (as was discussed in the proof of Proposition 2). The termination criterion ensures that condition (ii′) is ful<sup>fi</sup>lled. Hence, FindCandidates <sup>fi</sup>nds all restricted ef<sup>fi</sup>- cient portfolios (as well, perhaps, as some others). The algorithm FindRestEfficientPortfolios directly checks each portfolio $p ^ { \prime }$ found by FindCandidates against $p ^ { * }$ using De<sup>fi</sup>nition 5 in order to establish whether $p ^ { \prime }$ is restricted ef<sup>fi</sup>cient, thus ensuring that only restricted ef<sup>fi</sup>cient portfolios $\left( p ^ { \prime \prime } \right)$ are retained. □

The computational time for robustness evaluation depends on the number of projects taken into account and on the uncertainty domain de<sup>fi</sup>ned (the effects of the uncertainty on the computational times using trials with 50, 75 and 100 projects are shown in Appendix A).

We say that the choice of $p ^ { * }$ is undoubtedly robust when no portfolio $p ^ { \prime \prime }$ exists which is restricted ef<sup>fi</sup>cient relative to $p ^ { * }$ . Otherwise, for each restricted ef<sup>fi</sup>cient portfolio $p ^ { \prime \prime }$ PROBE solves problem (14)

$$
\bar {z} := \max \sum_ {i = 1} ^ {n} w _ {i} \left(\sum_ {j \in p ^ {*} \backslash p ^ {\prime}} \bar {v} _ {i j} - \sum_ {j \in p ^ {\prime} \backslash p ^ {*}} v _ {- i j}\right)
$$

subject to : w∈R :

14

The result z is the upper bound of the range of variation of the difference between the bene<sup>fi</sup>t value of the proposed portfolio $p ^ { * }$ and the bene<sup>fi</sup>t value of the competitor portfolio $p ^ { \prime \prime }$ in the uncertainty domain ℜ, with the lower bound z calculated by algorithm FindRestEfficientPortfolios (see Fig. 6). Finally, using expressions (15) and (16), PROBE calculates the lower bound d and upper bound <sup></sup>d of the range of variation of the difference between the costs of $p ^ { * }$ and $p ^ { \prime \prime }$ in ℜ.

$$
\underline {{d}} = \sum_ {j \in p ^ {\prime \prime} \backslash p ^ {*}} \underline {{c}} _ {j} - \sum_ {j \in p ^ {*} \backslash p ^ {\prime \prime}} \bar {c} _ {j}\tag{15}
$$

$$
\bar {d} = \sum_ {j \in p ^ {\prime \prime} \backslash p ^ {*}} \bar {c} _ {j} - \sum_ {j \in p ^ {*} \backslash p ^ {\prime \prime}} c _ {j}\tag{16}
$$

The user is then able to analyze the differences in cost and bene<sup>fi</sup>t between the proposed portfolio $p ^ { * }$ and each competitor portfolio $p ^ { \prime \prime }$ as illustrated with an example in Section 5. Finally, “core projects” can be identi<sup>fi</sup>ed as those projects that are common to the proposed portfolio $p ^ { * }$ and all of its competitors.

## 5. Example

In this section we present an example, which has been constructed to illustrate the key functionality of PROBE. A manager has to allocate resources to 12 projects from four departments, totaling €14 million (see Table 2), greatly exceeding the €5 million available. The manager and the four department directors constitute the decision making group (DMG) that develops a portfolio decision analysis with the support of PROBE. The DMG evaluates the added value of each project on each one of four bene<sup>fi</sup>t criteria (B1, B2, B3 and B4). The respective bene<sup>fi</sup>t value scores of the projects are shown in columns B1 to B4 in Table 2. Using this data and the criteria weights indicated in the last row of Table 2, the MCDA component of PROBE computes the bene<sup>fi</sup>t values of the projects shown in the last column of Table 2.

Table 2  
Basic input data for the 12 projects and MCDA output.

<table><tr><td rowspan="2">Project</td><td rowspan="2">Dept.</td><td rowspan="2">Cost (€106)</td><td colspan="4">Benefit value scores</td><td rowspan="2">Benefit value</td></tr><tr><td>B1</td><td>B2</td><td>B3</td><td>B4</td></tr><tr><td>P01</td><td>A</td><td>1.1</td><td>67</td><td>40</td><td>30</td><td>50</td><td>47.57</td></tr><tr><td>P02</td><td>A</td><td>1.9</td><td>55</td><td>37</td><td>40</td><td>20</td><td>39.88</td></tr><tr><td>P03</td><td>A</td><td>0.9</td><td>100</td><td>90</td><td>80</td><td>90</td><td>90.20</td></tr><tr><td>P04</td><td>A</td><td>0.9</td><td>90</td><td>80</td><td>70</td><td>95</td><td>83.35</td></tr><tr><td>P05</td><td>B</td><td>1.8</td><td>48</td><td>35</td><td>40</td><td>33</td><td>40.06</td></tr><tr><td>P06</td><td>B</td><td>1.3</td><td>43</td><td>32</td><td>25</td><td>44</td><td>35.90</td></tr><tr><td>P07</td><td>B</td><td>1.3</td><td>42</td><td>64</td><td>80</td><td>55</td><td>59.93</td></tr><tr><td>P08</td><td>B</td><td>1.1</td><td>40</td><td>50</td><td>44</td><td>20</td><td>38.86</td></tr><tr><td>P09</td><td>C</td><td>0.9</td><td>80</td><td>90</td><td>78</td><td>66</td><td>78.38</td></tr><tr><td>P10</td><td>C</td><td>1.3</td><td>88</td><td>66</td><td>80</td><td>70</td><td>77.72</td></tr><tr><td>P11</td><td>D</td><td>0.7</td><td>41</td><td>48</td><td>49</td><td>25</td><td>41.29</td></tr><tr><td>P12</td><td>D</td><td>0.8</td><td>86</td><td>88</td><td>90</td><td>72</td><td>84.60</td></tr><tr><td></td><td></td><td>Σ=14</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Weights</td><td></td><td></td><td>0.31</td><td>0.19</td><td>0.29</td><td>0.21</td><td></td></tr></table>

Fig. 7 is a snapshot of the main window of PROBE, displayed by the PDA component for the basic input data in Table 2. The portfolio selected by the optimization approach, solving the knapsack problem (8) for a budget of €5 million, is the ef<sup>fi</sup>cient portfolio (4.8, 414.25),<sup>1</sup> indicated by a star dot in the graph, with a cost of €4.8 million, a bene<sup>fi</sup>t of 414.25, and composed of <sup>fi</sup>ve projects, P03 and P04 from dept. A, P09 and P10 from dept. C, and P12 from dept. D, as highlighted in the tables above the graph.

This optimal portfolio (4.8, 414.25) is convex ef<sup>fi</sup>cient; therefore, it is also the one selected by the prioritization approach, as shown in Table 3.

The director of dept. B argues against the selection of portfolio (4.8, 414.25) because it does not include any project from his department. The DMG decides to analyze the potential loss of bene<sup>fi</sup>t associated to imposing that at least one project from each department be selected if possible. Accordingly, four constraints of type $\textstyle \sum _ { j \in G } x _ { j } \geq q$ with q=1 are added to PROBE, giving rise to the new results shown in Fig. 8.

The optimal portfolio is now (4.8, 396.46), which coincidentally costs the same as portfolio (4.8, 414.25) but offers 17.79 less units of bene<sup>fi</sup>t: the result of having replaced P10 with P07, as well-noted by the director of dept. C.

The robustness of selecting portfolio (4.8, 396.46) is then evaluated for an uncertainty domain ℜ de<sup>fi</sup>ned by all bene<sup>fi</sup>t value scores of all projects on all criteria varying ±10 units and all weights varying within the bounds indicated in Table 4 simultaneously, subjected to a normalization constraint.

Fig. 9 is a snapshot of the robustness analysis window of the PDA component of PROBE, showing that the only competitor of the proposed portfolio (4.8, 396.46) is portfolio (4.6, 375.39), because it is the only restricted ef<sup>fi</sup>cient portfolio relative to the proposed portfolio. The top-right table in Fig. 9 shows that the two portfolios only differ on one project, with project P07 of dept. B, included in the proposed portfolio, being replaced in the competitor portfolio by project P08, also of dept. B.

Some doubts are raised about the cost of project P08 being smaller than the cost of project P07. The cost of P08 is then allowed to vary within the range [€1.1 million, €1.5 million] and this uncertainty is added to the previous uncertainty domain. The top-left table in Fig. 10 shows that there is no new competitor portfolio and the only limit that changes is, obviously, the maximum difference in cost between the proposed and the competitor portfolios (“MaxDifCost”).

The ranges of variation of the differences in cost and bene<sup>fi</sup>t between these two portfolios are plotted in the top-right graph in Fig. 10. There are two areas shaded in this graph: the proposed portfolio is better both in cost and bene<sup>fi</sup>t in the “robustness” area at the right (displayed in red in PROBE) where those two differences are positive, whereas the competitor portfolio is better in the “regret” area at the left (displayed in blue in PROBE) where the two differences are negative.

## 6. Case study

In this section, we describe brie<sup>fl</sup>y an application of PROBE to health service planning in Northern Lisbon [52,57], which demonstrates the usefulness of the software and the approach. It is widely recognized that multicriteria portfolio approaches have considerable potential in the planning of health services [1]. This is partly because the bene<sup>fi</sup>ts of investment in healthcare are inherently multidimensional and dif<sup>fi</sup>cult to assess and tradeoff, but also because delivery requires the participation of members of multiple clinical specialties, and so approaches to decision aiding which facilitate stakeholder engagement are particularly appropriate.

The client in this case study was the Clinical Board of the Group of Health Centers (GHC) of Northern Lisbon, a collective organization comprising Health Centers for the districts of Lumiar, Sete Rios, Ben<sup>fi</sup>ca and Alvalade. The Board was faced with the task of planning a new Community Care Division (CCD) within each Health Center. Analysis of the action plan for each CCD showed that the Health Centers were not adequately staffed to deliver all the community care projects which they wished to. Hence a decision had to be taken about which projects to undertake.

In order to support the client, a multicriteria portfolio decision analysis was conducted through a series of working modeling meetings or decision conferences [56] with the Clinical Board and the Executive Director of the GHC. Four criteria (effective health gains, equity, achievement of GHC goals, and fit with existing services and community needs) were de<sup>fi</sup>ned and project bene<sup>fi</sup>t was assessed against these criteria using the MACBETH approach [3,5] (detailed descriptions of MACBETH applications can be found, e.g., in [5,8,10]).

Here we focus on the Sete Rios action plan, which was composed of 14 possible projects. The core constraint was the shortfall in available nursing hours: to do all projects would require 18,450 nursing hours, but only 17,460 nursing hours were available, and hiring more nurses was not possible. Additionally, <sup>fi</sup>ve other constraints were also de<sup>fi</sup>ned: one of the projects, the situation diagnosis project, should be included in the selected portfolio and the hours available of other health service professionals should not be exceeded, namely, 1665 social service of<sup>fi</sup>cer hours, 990 psychologist hours, 810 oral hygienist hours and 570 general practitioner hours. The cost–bene<sup>fi</sup>t plot for Sete Rios under this scenario is shown in Fig. 11. The gap in the display between the bottom left and top right clusters of points is due to the existence of a very large project, integrated long-term care (which, after discussion, the Board decided to implement).

The most attractive portfolio (the “proposed” portfolio in PROBE terminology) costs 15,300 nursing hours and gives 636.86 bene<sup>fi</sup>t units (it is marked with a star dot on the graph in Fig. 11). Although the proposed portfolio is not using the available nursing hours as much as possible (2160 nursing hours still are available), the Clinical Board and the Executive Director of the GHC did not want to select more “costly” portfolios because they were felt to add little bene<sup>fi</sup>t for their added expenditure in nursing hours.

![](/api/attachments/T3PUXJWG/fulltext/images/e042d8e973c58a60802428b8247e06e7ff630991c64f26f09eb53bb49cdd6a99.jpg)  
Fig. 7. PROBE analysis of ef<sup>fi</sup>cient portfolios. Each row of the top-left table shows information about one ef<sup>fi</sup>cient portfolio: a 1 or a 0 in column CE indicates whether the portfolio is convex ef<sup>fi</sup>cient or non-convex ef<sup>fi</sup>cient, respectively; a 1 or a 0 in each one of the columns P01 to P12 indicates whether the respective project is included or not, respectively, in the portfolio. The top-right table window shows the projects structured within areas (the four departments). Each ef<sup>fi</sup>cient portfolio is represented by a dot in the bottom graph (wher the star dot indicates the selected portfolio), with the convex ef<sup>fi</sup>cient ones linked by a dotted line.

The robustness of the proposed portfolio was tested under conditions of uncertainty on the part of the Clinical Board, modeled by intervals on the criteria weights, which were allowed to vary within these intervals. Also, the bene<sup>fi</sup>t value scores on effective health gains and achievement of GHC goals were allowed to vary within ranges to re<sup>fl</sup>ect both individual uncertainty and interpersonal disagreement between the Clinical Board and the team from the CCD.

Projects ranked by decreasing bene<sup>fi</sup>t-to-cost ratio (order of priority).

<table><tr><td>Project</td><td>Benefit</td><td>Cost</td><td>Ratio</td><td>Cumulative cost</td></tr><tr><td>P12</td><td>84.60</td><td>0.8</td><td>105.8</td><td>0.8</td></tr><tr><td>P03</td><td>90.20</td><td>0.9</td><td>100.2</td><td>1.7</td></tr><tr><td>P04</td><td>83.35</td><td>0.9</td><td>92.6</td><td>2.6</td></tr><tr><td>P09</td><td>78.38</td><td>0.9</td><td>87.1</td><td>3.5</td></tr><tr><td>P10</td><td>77.72</td><td>1.3</td><td>59.8</td><td>4.8</td></tr><tr><td>P11</td><td>41.29</td><td>0.7</td><td>59.0</td><td>5.5</td></tr><tr><td>P07</td><td>59.93</td><td>1.3</td><td>46.1</td><td>6.8</td></tr><tr><td>P01</td><td>47.57</td><td>1.1</td><td>43.2</td><td>7.9</td></tr><tr><td>P08</td><td>38.86</td><td>1.1</td><td>35.3</td><td>9.0</td></tr><tr><td>P06</td><td>35.90</td><td>1.3</td><td>27.6</td><td>10.3</td></tr><tr><td>P05</td><td>40.06</td><td>1.8</td><td>22.3</td><td>12.1</td></tr><tr><td>P02</td><td>39.88</td><td>1.9</td><td>21.0</td><td>14.0</td></tr></table>

The PROBE robustness analysis showed that given uncertainty about criterion weights and project bene<sup>fi</sup>t there were 28 competitor portfolios. It emerged in the course of analysis and discussion within the group that none of these competitor portfolios included the project integrated long-term care. The group agreed that it was not worthwhile losing this project, and so the proposed portfolio could be considered a robust choice. We note that unused nursing hours are not wasted: unused nurses can be released to other tasks not considered in this analysis or might be assigned to reformulated versions of non-selected projects.

The Clinical Board seems to have found that the analysis was useful to them in arriving at a decision about what to do, and also that it challenged them to develop their own information system to provide more decision-relevant information. Moreover, the case study has received broad recognition in the professional community, being awarded the best paper prize at the 12th Conference of the Portuguese Association of Health Economics.

## 7. Conclusion

Although the PROBE decision support system has many features in common with the commercial portfolio decision analysis software analyzed in [46], it goes a step forward because it identi<sup>fi</sup>es all convex ef<sup>fi</sup>cient and non-convex ef<sup>fi</sup>cient portfolios and enables users to perform in-depth robustness checks on proposed portfolios.

![](/api/attachments/T3PUXJWG/fulltext/images/329c77a0dad2a5d1cbba73c4af08af4e72c96d2380833173e44ac62f080b6069.jpg)  
Fig. 8. PROBE analysis of ef<sup>fi</sup>cient portfolios with group constraints.

In the RPM approach, referred to in Section 1, the decision-maker “is advised to start with loose preference statements, which imply large feasible sets of the parameter values and typically result in a large number of non-dominated portfolios” [43, p. 683]. The decision-maker is then invited to narrow the initial uncertainty domain, therefore reducing the number of non-dominated portfolios, and decision rules “can be consulted to recommend one of the remaining non-dominated portfolios” [43, p. 683]. In contrast, PROBE supposes the decision-maker can use best-guess parameter values to <sup>fi</sup>nd an attractive proposed portfolio, and then offers a form of robustness analysis in which the proposed portfolio is compared to competitors in its neighborhood.

Table 4 Uncertainty on the weights.

<table><tr><td>Criterion</td><td>Weight</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td>B1</td><td>0.31</td><td>0.26</td><td>0.36</td></tr><tr><td>B2</td><td>0.19</td><td>0.14</td><td>0.24</td></tr><tr><td>B3</td><td>0.29</td><td>0.24</td><td>0.34</td></tr><tr><td>B4</td><td>0.21</td><td>0.16</td><td>0.26</td></tr></table>

Despite the simplicity of the illustrative example presented in Section 5, PROBE can deal with complex portfolio decision analysis problems that involve a signi<sup>fi</sup>cant number of projects (see Appendix A) and many interactions among them. When the user de<sup>fi</sup>nes a large uncertainty domain (giving rise to a signi<sup>fi</sup>cant number of competitor portfolios, and therefore rendering inconclusive the analysis of robustness of the portfolio choice) the user may be invited, as in RPM, to progressively reduce the uncertainty domain, a reasoning called “progressive reduction of incomparability” in [11, Section 3.2] and already present in [58, p. 258]. The identi<sup>fi</sup>cation of the projects common to the proposed and the restricted ef<sup>fi</sup>cient portfolios—the “core projects” of PROBE and RPM—is in our view one of the most important outputs of a portfolio robustness analysis.

It is usually advantageous to <sup>fi</sup>rst run PROBE without adding constraints to the simple model (8); indeed, this will permit highlighting the best strategic portfolio choices [30,56]. Subsequently, structural, operational, programmatic or planning constraints [30,37,53] can be added interactively, as necessary, to make the model more realistic and satisfy the requirements [54] for selecting a robust portfolio. Our experience in using the EQUITY software to support portfolio decision analysis [4,6,7,56] has revealed that although several types of constraints can be built in manually and visually [15,56] into an EQUITY model, this is not always an easy task and occasionally not even possible. Consequently, although portfolio robustness evaluation has been

![](/api/attachments/T3PUXJWG/fulltext/images/680482cd31543e652679b0291e4704607075f1f02a1de7e32d4a785f08e04e74.jpg)  
Fig. 9. First portfolio robustness evaluation. Each row of the top-left table shows information about one competitor portfolio (i.e., a restricted ef<sup>fi</sup>cient portfolio relative to the pro posed portfolio): the four leftmost columns show the minimum and the maximum differences in cost and in bene<sup>fi</sup>t between the proposed portfolio and each competitor portfolio; a 1 or a 0 in each one of the columns P01 to P12 indicates whether the respective project is included or not, respectively, in the competitor portfolio. The top-right table window shows the projects included in the proposed portfolio; the projects included in the competitor portfolio highlighted in the table at the left and indicated by a surrounding circle in the graph; the projects common to both portfolios; and the projects that are not common to both portfolios and their respective areas (departments in our example).

![](/api/attachments/T3PUXJWG/fulltext/images/a19357ab17e7645d2dd5878803c666c0636a8db5e48e6fb2ed24bfa67f8e5ac1.jpg)  
Fig. 10. Second portfolio robustness evaluation

Cost vs Benefit

![](/api/attachments/T3PUXJWG/fulltext/images/f85014102eb63c58e6cef40f7c4215a738cfc78de7a93d736e2a6cb3e51cd9f8.jpg)  
Fig. 11. Cost–bene<sup>fi</sup>t graph for Sete Rios.

the core motivation for the conception of PROBE, its ability to formally accommodate project interactions and other constraints has been an important complementary software design objective.

We anticipate continuing to develop PROBE and to do so will raise interesting methodological and conceptual challenges. For example, in the version of PROBE reported in this paper, we do not deal with the question of how to analyze projects where there are bene<sup>fi</sup>ts associated with not doing a project (a discussion on this topic is presented in [18]). One can envisage different ways of modeling such a situation; some approaches (e.g. replacing the objective function in Eq. (8) with $\begin{array} { r } { \operatorname* { m a x } { \sum _ { j = 1 } ^ { m } \left\lceil \nu _ { j } x _ { j } + \nu _ { j } ^ { 0 } \left( 1 - x _ { j } \right) \right\rceil } } \end{array}$ where $\nu _ { j } ^ { 0 }$ is the bene<sup>fi</sup>t value of not selecting project j [18,35]) might require modi<sup>fi</sup>cation of the PROBE software and algorithms. We leave the question of how best to model and handle this case for further study, however.

The importance of carefully structuring the resource allocation problem [49], wisely assessing the bene<sup>fi</sup>t values of the projects, namely to escape from the “semi-global” scaling effect [51, p. 270], and correctly weighting the bene<sup>fi</sup>t criteria, should also be emphasized as essential prerequisites for a successful multicriteria portfolio analysis based on additive value measurement [8,34]. In particular, it is fundamental to avoid the “most common critical mistake” [32, p. 147], which is unfortunately made by many popular weighting procedures that assign weights to criteria simply on the basis of the intuitive notion of “importance”; this is why PROBE includes a module that guides the user through a step-by-step procedure to swing weighting the criteria [23]. In addition, we should prevent the use of outputs from an additive value model as bene<sup>fi</sup>t inputs for the portfolio analysis without <sup>fi</sup>rst de<sup>fi</sup>ning the meaning of the zero bene<sup>fi</sup>t value for a portfolio (see [7,18,30]). Last but not least, we emphasize that the technical component provided by the decision support system PROBE cannot, by itself, avoid all of the aforementioned traps; this is why facilitators of social-technical multicriteria portfolio selection processes [56] should be not only experienced in working with groups but also skillful in decision analysis technical principles.

## Acknowledgments

The authors thank Ana Respício, João Oliveira Soares, Manuel Pedro Chagas, Mónica Duarte Oliveira, Teresa Cipriano Rodrigues and participants in the New York meeting of the International Decision Conferencing Forum for their helpful comments. The authors acknowledge the referees for their careful review and useful comments. The authors would also like to thank the members of the Clinical Board of the North Lisbon Group of Health Centers that participated in the development and application of the model of the case study, brie<sup>fl</sup>y described in this paper. The authors gratefully acknowledge the support of the RAMS grant from the Council of Rectors of Portuguese Universities and the British Council under the Treaty of Windsor program. João C. Lourenço and Carlos A. Bana e Costa gratefully acknowledge the support of the FCT (Portuguese National Science Foundation) under project PTDC/GES/73853/2006.

## Appendix A

## Specifications

The running times presented in this section were obtained while using a single thread in a computer with an Intel Core 2 Duo T7800 2.60 GHz CPU, 4 GB of RAM and Windows 7 Professional 64 bit. The MILP solver lp\_solve 5.5.2.0 was used by the algorithms FindEfficientPortfolios, FindCandidates and FindRestEfficientPortfolios. The input data used in the trials were generated in a Microsoft Excel worksheet using the function “RANDBETWEEN(a,b)”, which returns an uniformly distributed pseudo-random integer number between the lower bound a and the upper bound b speci<sup>fi</sup>ed by the user. The costs of the projects were integers generated between 1 and 10 and the bene<sup>fi</sup>t value scores of the projects on four bene<sup>fi</sup>t criteria were integers generated between 1 and 100. The data used in the trials were generated for 100 projects, with no interactions among them. The projects were divided into three sets: Set no. 1—includes the <sup>fi</sup>rst 50 projects listed on the worksheet; Set no. 2—includes the <sup>fi</sup>rst 75 projects listed; Set no. 3—includes the 100 projects listed. The weights of three bene<sup>fi</sup>t criteria (w , w and w ) were integers generated between 1 and 30 and divided by 100, which resulted in $w _ { 1 } =$ 0.19, w =0.30 and $w _ { 3 } = 0 . 2 7$ , and the weight of the fourth criterion was calculated as $w _ { 4 } = 1 - ( w _ { 1 } + w _ { 2 } + w _ { 3 } ) = 0 . 2 4$

## Computation of the efficient frontier

Table 5 shows the running times of the PROBE algorithm FindEfficientPortfolios, which was used to <sup>fi</sup>nd the complete ef<sup>fi</sup>cient frontier, including possible multiple optimal portfolios, for each of the three sets of projects. The ε in algorithm FindEfficientPortfolios is automatically set by PROBE based on the number of signi<sup>fi</sup>cant <sup>fi</sup>gures to which the costs are expressed: in this case since the costs of the projects are integer numbers between 1 and 10 the minimum difference in cost that may occur between portfolios is 1, and hence the ε was automatically set by PROBE to 1. The running times of the algorithm FindConvexEfficientPortfolios are not referred to in Table 5, because it took less than one second to <sup>fi</sup>nd all the convex ef<sup>fi</sup>cient portfolios in the three trials.

Table 5  
Running times of algorithm FindEfficientPortfolios

<table><tr><td>Set no.</td><td>Number of projects</td><td>Sum of the costs of all projects</td><td>Sum of the benefits of all projects</td><td>Number of efficient portfolios found</td><td>Running time</td></tr><tr><td>1</td><td>50</td><td>278</td><td>2587.59</td><td>238</td><td>1 s</td></tr><tr><td>2</td><td>75</td><td>399</td><td>3945.16</td><td>366</td><td>4 s</td></tr><tr><td>3</td><td>100</td><td>555</td><td>5143.37</td><td>536</td><td>11 s</td></tr></table>

## Robustness evaluation

Table 6 shows the running times of the PROBE algorithms FindCandidates and FindRestEfficientPortfolios for the three sets of projects used in the trials. Uncertainties regarding the bene<sup>fi</sup>t value scores of the projects, the costs of the projects and the criteria weights were de<sup>fi</sup>ned as follows. The uncertainty on the bene<sup>fi</sup>t value $\nu _ { i j }$ of each project j on each bene<sup>fi</sup>t criterion i was de<sup>fi</sup>ned as an interval such that $\nu _ { i j } - \alpha _ { \nu } \leq \nu _ { i j } \leq \nu _ { i j } + \alpha _ { \nu } \ \mathrm { ( w i t h ~ } 1 \leq \nu _ { i j } \leq 1 0 0 \mathrm { ) }$ , for all i and $j ;$ the uncertainty on the cost c of each project j was de<sup>fi</sup>ned as an interval such that $\left( 1 - \alpha _ { c } \right) c _ { j } \leq c _ { j } \leq \left( 1 + \alpha _ { c } \right)$ c , for all j; and the uncertainty on the bene<sup>fi</sup>t criterion weight w<sub>i</sub> was de<sup>fi</sup>ned as an interval such that $( 1 - \alpha _ { w } ) w _ { i } \leq w _ { i } \leq ( 1 + \alpha _ { w } )$ w , for all i. For each of the three sets of projects used in the trials, the robustness of the convex ef<sup>fi</sup>cient portfolio was evaluated with the cost near to (but not higher than) one third of the sum of the costs of all projects in that set (see Table 5). The robustness evaluations were performed for the convex ef<sup>fi</sup>cient portfolios of Set no. 1, Set no. 2 and Set no. 3, respectively, with the following costs and bene<sup>fi</sup>ts: (89, 1467.27); (132, 2356.11); (181, 3016.75).

## Final notes

Due to the combinatorial nature of the knapsack problem the running times of the PROBE algorithms increase greatly with a small increment in the number of projects, e.g. in our trials it took 11 s to <sup>fi</sup>nd the ef<sup>fi</sup>cient frontier for 100 projects whereas for 50 projects it only took 1 s (see Table 5). The ε in algorithm FindEfficientPortfolios may also have a signi<sup>fi</sup>cant impact in the running times, e.g. if we had $\mathsf { s e t \thinspace } \varepsilon = 0 . 1$ in the trial with the 100 projects reported in Table 5 PROBE would have taken 1 min and 38 s to <sup>fi</sup>nd the entire ef<sup>fi</sup>cient frontier instead of the 11 s it took with ε=1; thus, ε should be set to a number small enough to allow <sup>fi</sup>nding all ef<sup>fi</sup>cient portfolios but not lower than that. The robustness evaluation is (obviously) affected by the number of projects in the trials, by the uncertainty ranges of its parameters (wider uncertainties imply increased running times), and by the simultaneous uncertainty on several parameters of the model; e.g. in the trial with Set no. 3 the algorithm FindCandidates took 30 s to <sup>fi</sup>nd all candidate portfolios when consid ering simultaneous variations on the bene<sup>fi</sup>t value scores of the projects on the four criteria of $\alpha _ { \nu } = 2 . 5$ and on the costs of all projects of $\alpha _ { c } = 0 . 0 2 5$ , whereas when variations on the weights of the four bene<sup>fi</sup>t criteria of $\alpha _ { w } = 0 . 0 2 5$ were added, the algorithm took 3 min and 37 s to complete (see Table 6) – a more dramatic increase in the running time was found when α was increased to 3 (the algorithm FindCandidates took 1 h 20 min and 42 s to complete). In contrast, these changes in parameters have no noticeable impact on the running times of the algorithm FindRestEfficientPortfolios (see Table 6).

In order to reduce the PROBE running times or to address more complex problems (i.e. problems with more projects and/or with wider uncertainty domains) and taking advantage of multiple core computers, we could run several instances of the PROBE algorithms in parallel using multiple threads (namely the most time consuming algorithms,

Table 6  
PROBE running times for robustness evaluation.

<table><tr><td rowspan="2">Set no.</td><td colspan="3">Uncertainty parameters</td><td rowspan="2">No. of candidate portfolios found</td><td rowspan="2">Time spent searching for candidate portfolios (a)</td><td rowspan="2">No. of restricted efficient portfolios found</td><td rowspan="2">Time spent searching for restricted efficient portfolios (b)</td><td rowspan="2">Total running time</td></tr><tr><td> $\alpha_w$ </td><td> $\alpha_v$ </td><td> $\alpha_c$ </td></tr><tr><td rowspan="8">1</td><td>0.025</td><td>0</td><td>0</td><td>1</td><td>&lt;1 s</td><td>1</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>2.5</td><td>0</td><td>1</td><td>&lt;1 s</td><td>1</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>0</td><td>0.025</td><td>0</td><td>&lt;1 s</td><td>0</td><td>0 s</td><td>&lt;1 s</td></tr><tr><td>0.025</td><td>2.5</td><td>0</td><td>6</td><td>&lt;1 s</td><td>3</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0.025</td><td>0</td><td>0.025</td><td>1</td><td>&lt;1 s</td><td>1</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>2.5</td><td>0.025</td><td>1</td><td>&lt;1 s</td><td>1</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0.025</td><td>2.5</td><td>0.025</td><td>9</td><td>1 s</td><td>3</td><td>&lt;1 s</td><td>1 s</td></tr><tr><td>0.025</td><td>3</td><td>0.025</td><td>16</td><td>2 s</td><td>8</td><td>&lt;1 s</td><td>2 s</td></tr><tr><td rowspan="8">2</td><td>0.025</td><td>0</td><td>0</td><td>1</td><td>&lt;1 s</td><td>1</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>2.5</td><td>0</td><td>1</td><td>&lt;1 s</td><td>1</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>0</td><td>0.025</td><td>0</td><td>&lt;1 s</td><td>0</td><td>0 s</td><td>&lt;1 s</td></tr><tr><td>0.025</td><td>2.5</td><td>0</td><td>8</td><td>&lt;1 s</td><td>4</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0.025</td><td>0</td><td>0.025</td><td>1</td><td>&lt;1 s</td><td>1</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>2.5</td><td>0.025</td><td>1</td><td>&lt;1 s</td><td>1</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0.025</td><td>2.5</td><td>0.025</td><td>13</td><td>3 s</td><td>4</td><td>&lt;1 s</td><td>3 s</td></tr><tr><td>0.025</td><td>3</td><td>0.025</td><td>42</td><td>22 s</td><td>13</td><td>&lt;1 s</td><td>22 s</td></tr><tr><td rowspan="8">3</td><td>0.025</td><td>0</td><td>0</td><td>0</td><td>&lt;1 s</td><td>0</td><td>0 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>2.5</td><td>0</td><td>2</td><td>&lt;1 s</td><td>2</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>0</td><td>0.025</td><td>0</td><td>&lt;1 s</td><td>0</td><td>0 s</td><td>&lt;1 s</td></tr><tr><td>0.025</td><td>2.5</td><td>0</td><td>5</td><td>&lt;1 s</td><td>4</td><td>&lt;1 s</td><td>&lt;1 s</td></tr><tr><td>0.025</td><td>0</td><td>0.025</td><td>0</td><td>&lt;1 s</td><td>0</td><td>0 s</td><td>&lt;1 s</td></tr><tr><td>0</td><td>2.5</td><td>0.025</td><td>46</td><td>30s</td><td>46</td><td>&lt;1 s</td><td>30s</td></tr><tr><td>0.025</td><td>2.5</td><td>0.025</td><td>126</td><td>3 m 57 s</td><td>110</td><td>&lt;1 s</td><td>3 m 57 s</td></tr><tr><td>0.025</td><td>3</td><td>0.025</td><td>717</td><td>1 h 20 m 42 s</td><td>585</td><td>&lt;1 s</td><td>1 h 20 m 43 s</td></tr></table>

Note. Running times for the algorithms (a) FindCandidates and (b) FindRestEfficientPortfolios.

FindEfficientPortfolios and FindCandidates, although that would require making some adjustments on the algorithms herein presented), and/or we could replace the lp\_solve solver by an industrial strength solver capable of generating multiple threads (e.g. the CPLEX solver, http://www-01.ibm.com/software/integration/optimization/cplexoptimizer/). However, as the free lp\_solve solver delivers acceptable solution times for realistic problems, we have retained the former option for PROBE.

## References

[1] M. Airoldi, A. Morton, Portfolio decision analysis for population health, in: A. Salo, J. Keisler, A. Morton (Eds.), Portfolio Decision Analysis: Improved Methods for Resource Allocation, Springer, New York, 2011, pp. 359–381.

[2] C.A. Bana e Costa, The use of multi-criteria decision analysis to support the search for less con<sup>fl</sup>icting policy options in a multi-actor context: Case study, J. Multi-Criteria Decis. Anal. 10 (2001) 111–125.

[3] C.A. Bana e Costa, M.P. Chagas, A career choice problem: An example of how to use MACBETH to build a quantitative value model based on qualitative value judgments, Eur. J. Oper. Res. 153 (2004) 323–331.

[4] C.A. Bana e Costa, M.L. Costa-Lobo, I.A.J. Ramos, J.C. Vansnick, Multicriteria approach for strategic town planning: The case of Barcelos, in: D. Bouyssou, E. Jacquet-Lagrèze, P. Perny, R. Slowinsky, D. Vanderpooten, P. Vincke (Eds.), Aiding Decisions with Multiple Criteria: Essays in Honour of Bernard Roy, Kluwer Aca demic Publishers, Dordrecht, 2002, pp. 429–456.

[5] C.A. Bana e Costa, J.M. De Corte, J.C. Vansnick, MACBETH, Int. J. Inf. Technol. Decis. Mak. 11 (2012) 359–387.

[6] C.A. Bana e Costa, L. Ensslin, E.C. Corrêa, J.C. Vansnick, Decision support systems in action: Integrated application in a multicriteria decision aid process, Eur. J. Oper. Res. 113 (1999) 315–335.

[7] C.A. Bana e Costa, T.G. Fernandes, P.V.D. Correia, Prioritisation of public investments in social infrastructures using multicriteria value analysis and decision conferencing: A case study, Int. Trans. Oper. Res. 13 (4) (2006) 279–297.

[8] C.A. Bana e Costa, J.C. Lourenço, M.P. Chagas, J.C. Bana e Costa, Development of reusable bid evaluation models for the Portuguese Electric Transmission Company, Decis. Anal. 5 (2008) 22–42.

[9] C.A. Bana e Costa, J.C. Lourenço, J.O. Soares, An interval weighting assignment model for credit analysis, J. Financ. Decis. Mak. 3 (2007) 1–9.

[10] C.A. Bana e Costa, C.S. Oliveira, V. Vieira, Prioritization of bridges and tunnels in earthquake risk mitigation using multicriteria decision analysis: Application to Lisbon, Omega 36 (2008) 442–450.

[11] C.A. Bana e Costa, P. Vincke, Measuring credibility of compensatory preference statements when trade-offs are interval determined, Theory Decis. 39 (1995) 127–155.

[12] D. Bouyssou, T. Marchant, M. Pirlot, A. Tsoukiàs, P. Vincke, Evaluation and Decision Models with Multiple Criteria: Stepping Stones for the Analyst, Springer, New York, 2006.

[13] R.A. Brealey, S.C. Myers, Principles of Corporate Finance, 7th ed. McGraw-Hill/Irwin, Boston, 2003.

[14] G.G. Brown, R.F. Dell, A.M. Newman, Optimizing military capital planning, Interfaces 34 (2004) 415–425.

[15] D. Buede, T. Bresnick, Decision analysis for resource allocation decisions, IDI Technical Report, Innovative Decisions, Inc., Vienna, VA, 2000.

[16] D.M. Buede, T.A. Bresnick, Applications of decision analysis to the military systems acquisition process, in: W. Edwards, R.F. Miles Jr., D. von Winterfeldt (Eds.), Advances in Decision Analysis: From Foundations to Applications, Cambridge University Press, Cambridge, 2007, pp. 539–563.

[17] Catalyze Ltd., Equity (version 3.4), http://www.catalyze.co.uk, 2008.

[18] R.T. Clemen, J.E. Smith, On the choice of baselines in multiattribute portfolio analysis: A cautionary note, Decis. Anal. 6 (2009) 256–262.

[19] R.G. Cooper, S.J. Edgett, E.J. Kleinschmidt, New product portfolio management: Practices and performance, J. Prod. Innov. Manage. 16 (1999) 333–350.

[20] R.G. Cooper, S.J. Edgett, E.J. Kleinschmidt, Portfolio Management for New Products, 2nd ed. Perseus Books, Cambridge, MA, 2001

[21] G.B. Dantzig, Discrete-variable extremum problems, Oper. Res. 5 (1957) 266–277.

[22] W. Edwards, How to use multiattribute utility measurement for social decisionmaking, IEEE Trans. Syst. Man Cybern. 7 (1977) 326–340.

[23] W. Edwards, F.H. Barron, SMARTS and SMARTER: Improved simple methods for multiattribute utility measurement, Organ. Behav. Hum. Decis. Process. 60 (1994) 306–325.

[24] M. Ehrgott, Multicriteria Optimization, 2nd ed. Springer, Berlin, 2005.

[25] Expert Choice, Expert Choice (version 11.4 with the Resource Aligner extension), http://www.expertchoice.com, 2007.

[26] M.R. Garey, D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, Freeman, San Francisco, 1979.

[27] F. Ghasemzadeh, N.P. Archer, Project portfolio selection through decision support, Decis. Support Syst. 29 (2000) 73–88.

[28] K. Golabi, Selecting a portfolio of nonhomogeneous R&D proposals, Eur. J. Oper. Res. 21 (1985) 347–357.

[29] K. Golabi, Selecting a group of dissimilar projects for funding, IEEE Trans. Eng. Manage. 34 (1987) 138–145.

[30] K. Golabi, C.W. Kirkwood, A. Sicherman, Selecting a portfolio of solar energy projects using multiattribute preference theory, Manage. Sci. 27 (1981) 174–189.

[31] P. Gunther, Use of linear programming in capital budgeting, J. Oper. Res. Soc. Am. 3 (1955) 219–224.

[32] R.L. Keeney, Value-Focused Thinking: A Path to Creative Decisionmaking, Harvard University Press, Cambridge, MA, 1992.

[33] H. Kellerer, U. Pferschy, D. Pisinger, Knapsack Problems, Springer, Berlin, 2004.

[34] C.W. Kirkwood, Strategic Decision Making: Multiobjective Decision Analysis with Spreadsheets, Duxbury Press, Belmont, CA, 1997.

[35] C.W. Kirkwood, How to take account of the value of not selecting an alternative, http://www.public.asu.edu/\~kirkwood/SDMBook/Not\_selecting\_an\_alternative. pdf, 2009.

[36] C.E. Kleinmuntz, D.N. Kleinmuntz, A strategic approach to allocating capital in healthcare organizations, Healthc. Financ. Manage. 53 (1999) 52–58

[37] D.N. Kleinmuntz, Resource allocation decisions, in: W. Edwards, R.F. Miles Jr., D. von Winterfeldt (Eds.), Advances in Decision Analysis: From Foundations to Applications, Cambridge University Press, Cambridge, 2007, pp. 400–418

[38] A. Koç, D.P. Morton, E. Popova, S.M. Hess, E. Kee, D. Richards, Prioritizing project selection, Eng. Econ. 54 (2009) 267–297.

[39] B. Korte, J. Vygen, Combinatorial Optimization: Theory and Algorithms, 3rd ed. Springer, Berlin, 2006.

[40] Krysalis, HiPriority (version 3), http://www.krysalis.co.uk, 2007.

[41] J. Liesiö, Portfolio Decision Analysis for Robust Project Selection and Resource Allocation, PhD Thesis, Department of Engineering Physics and Mathematics, Systems Analysis Laboratory, Helsinki University of Technology, Espoo, 2008.

[42] J. Liesiö, P. Mild, A. Salo, Preference programming for robust portfolio modeling and project selection, Eur. J. Oper. Res. 181 (2007) 1488–1505.

[43] J. Liesiö, P. Mild, A. Salo, Robust portfolio modeling with incomplete cost information and project interdependencies, Eur. J. Oper. Res. 190 (2008) 679–695.

[44] Logical Decisions, Logical Decisions Portfolio (with Logical Decisions, version 6.1), http://www.logicaldecisions.com, 2008.

[45] J.H. Lorie, L.J. Savage, Three problems in rationing capital, J. Bus. 28 (1955) 229–239.

[46] J.C. Lourenço, C.A. Bana e Costa, A. Morton, Software packages for multi-criteria resource allocation, Proceedings of the IEEE International Engineering Management Conference, IEMC-Europe 2008, Estoril, Portugal, 2008.

[47] S. Martello, P. Toth, The 0–1 knapsack problem, in: N. Christo<sup>fi</sup>des, A. Mingozzi, P. Toth, C. Sandi (Eds.), Combinatorial Optimization, John Wiley & Sons, Chichester, 1979, pp. 237–279.

[48] S. Martello, P. Toth, Knapsack Problems: Algorithms and Computer Implementations, John Wiley & Sons, Chichester, 1990

[49] G. Montibeller, L.A. Franco, E. Lord, A. Iglesias, Structuring resource allocation decisions: A framework for building multi-criteria portfolio models with areagrouped options, Eur. J. Oper. Res. 199 (2009) 846–856.

[50] A. Morton, On the choice of baselines in portfolio decision analysis, Working Paper LSEOR 10.128, London School of Economics, London, 2010. http://www. lse.ac.uk/collections/operationalResearch/research/workingPapers.htm.

[51] A. Morton, B. Fasolo, Behavioural decision theory for multi-criteria decision analysis: A guided tour I Oper, Res, Soc, 60 (2009) 268–275

[52] M.D. Oliveira, T.C. Rodrigues, C.A. Bana e Costa, A. Brito de Sá, Prioritizing health care interventions: A multicriteria resource allocation model to inform the choice of community care programmes, in: E. Tànfani, A. Testi (Eds.), Advanced Decision Making Methods Applied to Health Care, Springer, Milan, 2012, pp. 141–154.

[53] G.S. Parnell, G.E. Bennett, J.A. Engelbrecht, R. Szafranski, Improving resource allocation within the National Reconnaissance Of<sup>fi</sup>ce, Interfaces 32 (2002) 77–90.

[54] L.D. Phillips, A theory of requisite decision models, Acta Psychol. 56 (1984) 29–48.

[55] L.D. Phillips, Decision conferencing, in: W. Edwards, R.F. Miles Jr., D. von Winterfeldt (Eds.), Advances in Decision Analysis: From Foundations to Applications, Cambridge University Press, Cambridge, 2007, pp. 375–399.

[56] L.D. Phillips, C.A. Bana, e Costa, Transparent prioritisation, budgeting and resource allocation with multi-criteria decision analysis and decision conferencing, Ann. Oper. Res. 154 (2007) 51–68.

[57] T.C. Rodrigues, Modelo Multicritério de Afectação de Recursos Humanos em Projectos de Cuidados à Comunidade, MSc Thesis, Instituto Superior Técnico - Universidade Técnica de Lisboa, Faculdade de Medicina da Universidade de Lisboa, Lisboa, 2010.

[58] B. Roy, Problems and methods with multiple objective functions, Math. Program. 1 (1971) 239–266.

[59] B. Roy, A missing link in OR-DA: Robustness analysis, Found. Comput. Decis. Sci 23 (1998) 141–160.

[60] A. Salo, J. Keisler, A. Morton (Eds.), Portfolio Decision Analysis: Improved Methods for Resource Allocation, Springer, New York, 2011.

[61] A. Salo, P. Mild, T. Pentikäinen, Exploring causal relationships in an innovation program with robust portfolio modeling, Technol. Forecast. Soc. Change 73 (2006) 1028–1044.

[62] P. Sharpe, T. Keelin, How Smithkline Beecham makes better resource-allocation decisions Hary, Bus, Rev, 76 (1998) 45-57

[63] B. Stroustrup, The C++ Programming Language, 3rd ed. Addison-Wesley, Reading, MA, 1997.

[64] H.M. Weingartner, The excess present value index—A theoretical basis and critique, J. Account. Res. 1 (1963) 213–224.

[65] M. Weinstein, R. Zeckhauser, Critical ratios and ef<sup>fi</sup>cient allocation, J. Public Econ. 2 (1973) 147–157.

![](/api/attachments/T3PUXJWG/fulltext/images/381cd1ccc2ec4bec46f5d344cb21758facf59b7232ab977b02e1bc8ef9cdf645.jpg)

![](/api/attachments/T3PUXJWG/fulltext/images/f8653a6ef60bb9580d071fff3f999109f202a6deba6f08d0e3a759b485f21d52.jpg)  
João C. Lourenço is Assistant Professor of decision analysis, operational research, and production and operations management at the Technical University of Lisbon, School of Engineering (IST), Department of Engineering and Management. Before joining IST, he worked for seven years as a decision analyst for a consultancy company. He graduated in Applied Mathematics, he holds an MSc in Operational Research and Systems Engineering, and a PhD in Industrial Engineering and Management. He is a member of the Center for Management Studies of IST. His research has been published in Decision Analysis, the European Journal of Operational Research, and the Journal of Financial Decision Making. He has been involved in consulting projects in Portugal and Brazil, and also for the European Commission.

Alec Morton is Senior Lecturer in Management Science in the Department of Management at the London School of Economics and Political Science. He teaches courses in decision analysis, simulation, and statistics, and his research interests are in the application of decision analysis to planning problems, especially in healthcare; in Multicriteria Decision Analysis and Multiobjective Optimization; in the normative foundations of health economics, and in games of attack and defence. With Ahti Salo and Jeff Keisler, he is an ed itor of "Portfolio Decision Analysis: Improved Methods for Resource Allocation" published in Springer's International Series in Operations Research & Management Science. He is a graduate of the Universities of Manchester and Strathclyde, and before joining the LSE, worked at Singapore Airlines and th National University of Singapore.

![](/api/attachments/T3PUXJWG/fulltext/images/449abe7c96ab923ed021faa710fba3f286a96c35d1fad5f09b7a06e16d086c6a.jpg)

Carlos A. Bana e Costa is Full Professor of Decision and Information at the Technical University of Lisbon, School of Engineering (IST), Department of Engineering and Management, and he was Visiting Professor of Decision Sciences at the London School of Economics and Political Science, Department of Management (1999-2010). He is also head of research projects at the Center of Management Studies of IST. His primary interests have been in the <sup>fi</sup>elds of Management and Decision Sciences, namely Multicriteria Decision Analysis and Decision Conferencing. He has published widely in these areas and he is co-author of the MACBETH approach for decision-aiding (http://www.m-macbeth.com). He has also been developing consultation in public strategic decision-making processes, policy appraisal, and bid and suppliers’ performance evaluation throughout the world, following the socio-technical facilitation perspective shared by the members of the International Decision Conferencing Forum. He is also a senior partner of BANA Consulting (http://www.bana-consulting.pt).
