---
otero_id: 10382
otero_key: "CRW5VW3S"
title: "Selection of optimal countermeasure portfolio in IT security planning"
authors: "Tadeusz Sawik"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Selection of optimal countermeasure portfolio in IT security planning

Tadeusz Sawik ⁎

AGH University of Science & Technology, Department of Operations Research and Information Technology, Al.Mickiewicza 30, 30-059 Kraków, Poland

## a r t i c l e i n f o

Article history: Received 19 February 2012 Received in revised form 10 December 2012 Accepted 2 January 2013 Available online 11 January 2013

Keywords: Information security Risk management Countermeasure selection Conditional value-at-risk Mixed integer programming Multi-criteria decision making

## a b s t r a c t

This paper deals with the optimal selection of countermeasures in IT security planning to prevent or mitigate cyber-threats and a mixed integer programming approach is proposed for the decision making. Given a set of potential threats and a set of available countermeasures, the decision maker needs to decide which countermeasure to implement under limited budget to minimize potential losses from successful cyber-attacks and mitigate the impact of disruptions caused by IT security incidents. The selection of countermeasures is based on their effectiveness of blocking different threats, implementation costs and probability of potential attack scenarios. The problem is formulated as a single- or bi-objective mixed integer program and a conditional value-at-risk approach combined with scenario-based analysis is applied to control the risk of high losses due to operational disruptions and optimize worst-case performance of an IT system. The bi-objective trade-off model provides the decision maker with a simple tool for balancing expected and worst-case losses and for shaping of the resulting cost distribution through the selection of optimal subset of countermeasures for implementation, i.e., the selection of optimal countermeasure portfolio. The selected portfolio explicitly depends on preferred con<sup>fi</sup>dence level and cost/risk preference of the decision maker. Numerical examples are presented and some computational results are reported to compare the risk-averse solutions that minimize conditional value-at-risk with the risk-neutral ones that minimize expected cost

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The objective of IT security planning is to protect an asset against a compromise in the area of con<sup>fi</sup>dentiality, integrity or availability, where asset types may include systems and applications, networks, end-user systems, and off line media and devices, e.g. [3]. The various actions developed to prevent intrusions or to mitigate the impact of successful breaches are called controls or countermeasures. In view of the variety of methods used by attackers to in<sup>fi</sup>ltrate IT infrastructures and disrupt operations, a wide range of different countermeasures are developed. Some countermeasures are used to limit physical access to an IT infrastructure (e.g., key entry systems, retinal or <sup>fi</sup>nger print scans), other block access or protect privacy over networks (e.g., <sup>fi</sup>rewalls, data encryption, or virus and spyware scanners), while additional countermeasures are designed to permit recovery after a successful intrusion (e.g., backing up important <sup>fi</sup>les on a frequent basis).

The National Institute of Standards and Technology classi<sup>fi</sup>es information security controls (NIST SP800-53) into the three categories: technical, operational, and management controls [31,33], in which the last two categories can become as critical as the <sup>fi</sup>rst one. For example, operational countermeasures include monitoring and logging procedures, business continuity/incident response procedures, backup and recovery procedures, while management countermeasures include periodic employee training, periodic testing and review procedures, network auditing, and protection for all sensitive informational assets. In practice, even the most sophisticated countermeasures cannot be expected to completely block attacks as new attack pro<sup>fi</sup>les proliferate and the time and cost required to adapt to them the implemented countermeasures are not negligible. The potential threats, however, cannot be ignored and without countermeasures the losses resulting from many more breaches could easily excess the costs of countermeasure implementations.

The problem of a right choice of countermeasures for implementation under limited budget is not an easy task (for example, see [2] for the results of surveyed 349 industry and government respondents, or [34]). The choice not only depends on reliable data on potential cyber-threats and losses but also requires a good security risk planning tool, e.g., [3,5]. Most of IT security planning models in the literature are qualitative. For example, in [1] a system called OCTAVE was developed which utilizes qualitative information to assess security risk. A qualitative approach for the selection of security countermeasures to protect an IT system from attacks was proposed in [6]. The security scenarios are modeled by using defense trees and preferences over countermeasure using conditional preference networks (cp-nets). In [7] methods for identi<sup>fi</sup>cation of the assets, the threats, the vulnerabilities of the ICT systems were introduced and a procedure is proposed that enables selection of the optimal investment of the necessary security technology based on the quanti<sup>fi</sup>cation of the values of the protected systems. In [11] a checklist in table form was developed to help decision maker planning a coverage strategy. In a related research stream, current research <sup>fi</sup>ndings in enterprise risk and security management using mining techniques were discussed in [9].

In contrast to qualitative approaches, the literature on quantitative methods for selection of countermeasures to block or mitigate security attacks is very limited. For example, [18] proposed a hybrid expert system combined with discrete dynamic programming for Pareto optimal selection of countermeasures that enables the user to choose the best security solution depending on the available resources. The approach was illustrated with an example from the banking security. In [13] the countermeasure selection was analyzed in relation to residual vulnerabilities, which are represented as uncovered vulnerabilities. The idea behind their approach was to maximize the coverage of existing vulnerabilities by implementing a set of countermeasures, and thus, minimizing the residual vulnerability (uncovered). In [21] a decision support system was proposed for calculating the uncertain risk faced by an organization under cyber attack as a function of uncertain threat rates, countermeasure costs, and impacts on its assets. The system uses a genetic algorithm to search for the best combination of countermeasures, allowing the user to determine the preferred tradeoff between the cost of the portfolio and resulting risk. Based on NIST SP800-30 guidelines, in [33] a risk assessment and optimization model was developed to satisfy organizational security needs in a cost-effective manner, The security countermeasure selection problem was formulated as a multi-objective optimization problem, where variables such as <sup>fi</sup>nancial cost and risk may affect the <sup>fi</sup>nal solution. A tailored multi-objective tabu searchbased heuristic approach was constructed to solve the proposed multi-objective optimization problem and asses the qualities of its solutions with respect to optimal ones. In [10] a linear generalized network <sup>fl</sup>ow model that quanti<sup>fi</sup>es IT security risk in the supply chain was developed. It was shown how to <sup>fi</sup>nd solutions for optimal risk reduction under several de<sup>fi</sup>nitions of optimality: minimizing upstream risk, minimizing downstream risk, and minimizing global supply chain risk. Then, following the mathematical models proposed in [10], an integer programming model was developed in [20], for optimally choosing a subset of countermeasures to block or mitigate security attacks in the presence of a given threat level pro<sup>fi</sup>le. The model was used to examine the two different types of scenarios: under expected threat levels and under worst-case levels. The authors illustrated the tradeoffs in optimal security planning when expected threats are used to parameterize the model versus worst-case values for threat outcomes. To demonstrate the trade-off which occurs if decision makers divert budgets away from planning for ordinary risk in an effort to mitigate the effects of potential high-impact outcomes, budget-dependent risk curves were developed.

This work has been inspired by paper [20]. However, in contrast to risk modeling approach used in [20], the two popular in <sup>fi</sup>nancial engineering percentile measures of risk, value-at-risk (VaR) and conditional value-at-risk (CVaR), are applied. VaR and CVaR have been widely used in <sup>fi</sup>nancial engineering in the <sup>fi</sup>eld of portfolio management (e.g. [25]). CVaR is used in conjunction with VaR and is applied for estimating the risk with non-symmetric cost distributions. A new approach to select a portfolio with the reduced risk of high losses was introduced in [22,23,32]. This approach combined with scenario analysis was applied, for example, to risk-averse selection of customer orders [8] or to risk-averse supplier selection and order quantity allocation in make-to-order environment in the presence of supply chain disruption risks [27,29]. In [35] a model of information security investments was built and value-at-risk method was applied to evaluate different investment tradeoffs. In [19] value-at-risk method was applied in the context of pricing IT services on demand and to address uncertainty in services pricing decisions the price-at-risk approach was introduced. The latter methodology was also applied in [14] in the context of IT service contract design and the authors introduced the concept of pro<sup>fi</sup>t-at-risk, the maximum expected pro<sup>fi</sup>t that can be achieved in the presence of risk. The pro<sup>fi</sup>t-at-risk and operational risk modeling approaches were next applied in [16] to develop a profit optimization model for customer information security investments and to provide guidance on the trade-off between risk and return. It was shown that optimal investment decisions for information security protection depend on the trade-off between the cost to implement the information security service and the resulting risk mitigation. Moreover, a minimum information security protection level was de-<sup>fi</sup>ned that needs to be achieved in order to make investment in a customer privacy protection effective.

In this paper an exact solution approach is developed to incorporate risk, that uses CVaR via scenario analysis. For a <sup>fi</sup>nite number of scenarios, CVaR allows the evaluation of worst-case losses from successful cyber attacks and shaping of the resulting cost distribution through the selection of optimal subset of countermeasures for implementation, $\mathrm { i . e . }$ , the selection of optimal countermeasure portfolio. The problem of selection of optimal portfolio is modeled as a single- or bi-objective mixed integer program, similar to that developed in [20], and the countermeasure portfolio is optimized by calculating VaR and minimizing CVaR simultaneously. The resulting scenario-based optimization problem under uncertainty can be easily solved using commercially available software for mixed integer programming. In particular, the biobjective trade-off model provides the decision maker with a simple tool for balancing expected and worst-case losses and for shaping of the resulting cost distribution through the selection of countermeasure portfolio that explicitly depends on preferred con<sup>fi</sup>dence level and cost/risk preference.

The paper is organized as follows. In Section 2 description of countermeasure selection problem in IT security planning is provided. The mixed integer programs for a risk-neutral or risk-averse selection of countermeasure portfolio are developed in Section 3. A weighted-sum program for a bi-objective selection of countermeasures is presented in Section 4. Numerical examples and some computational results are provided in Section 5, and <sup>fi</sup>nal conclusions are made in the last section.

## 2. Problem description

Let $I { = } \{ 1 , { \ldots } m \}$ be the set of m threats and $J { = } \{ 1 , { \ldots } n \}$ the set of n countermeasures (for notation used, see Table 1). Denote by $p _ { i }$ the probability of threat i, i.e., attack episode of threat i occurs with probability $p _ { i } ,$ or not at all with probability $( 1 - p _ { i } )$ . Let $P _ { k }$ be the probability that attack scenario k is realized, where each scenario $k { \in } K$ is comprised of a unique subset $I _ { k } \subset I$ of threats that appear in the cyberattack, and $K = \left\{ 1 , . . . , g \right\}$ is the index set of all scenarios (note that there are a total of $g = 2 ^ { m }$ potential scenarios). The probability of attack scenario k in the presence of independent threat events is

$$
P _ {k} = \prod_ {i \in I _ {k}} p _ {i} \cdot \prod_ {i \notin I _ {k}} (1 - p _ {i}).
$$

Let $r _ { i j } { \in } [ 0 , 1 ]$ be the proportion of threats i that survive if countermeasure j is implemented, where $r _ { i j } = 0$ indicates that countermeasure j totally prevents successful attacks of threat i, whereas $r _ { i j } = 1$ denotes that countermeasure j is totally incapable of mitigating threat i.

Note, that even the most sophisticated countermeasures, in practice are rarely expected to completely block attacks, and hence the survival proportions $r _ { i j }$ are rarely equal to 0.

The blocking effectiveness of each countermeasure is assumed to be independent whether or not it is used alone or together with other countermeasures, and the proportion of successful attacks of threats type i that survive all countermeasures in the subset $J S \subseteq J$ of selected countermeasures is a multiplication of proportions $r _ { i j } , j \in J S .$ Let $\Pi _ { j \in J S } r _ { i j }$ be the proportion of threats i that survive if subset $J S$ of countermeasures is implemented. Note that the expected proportion of successful attacks of threat type i for the subset JS of selected countermeasures is $p _ { i } \prod _ { j \in J S } r _ { i j } .$

```txt
Table 1
Notation.

Indices
i = threat, i∈I={1,...,m}
j = countermeasure, j∈J={1,...,n}
k = attack scenario, k∈K={1,...,g}
l = countermeasure implementation level, l∈L={0,1} (l=0-off, l=1-on)

Input parameters
a_i = cost of a successful attack episode of threat i
B = available budget for countermeasures
c_j = cost of countermeasure j
I_k = subset of threats in scenario k
p_i = probability of threat i
P_k = ∏_{i∈I_k} p_i · ∏_{i∈I_k} (1-p_i) - probability of attack scenario k
r_ij = proportion of threats i that survive if countermeasure j is implemented
s_ijl = max{1-l,r_ij}-proportion of threats i that survive if countermeasure j is implemented at level l (s_ij0=1 and s_ij1=r_ij)
α = confidence level

Variables
T_k = the tail cost for attack scenario k, i.e., the amount by which costs in scenario k exceed VaR
VaR = value-at-risk
x_ijl = proportion of surviving occurrences of threat i to be addressed by countermeasure j at level l
y_jl = 1, if countermeasure j is implemented at level l, otherwise y_jl=0
z_ij = proportion of surviving occurrences of threat i that passed countermeasures 1 through j
Z_i = proportion of successful attacks of type i
```

Denote by $c _ { j }$ the cost of implementing countermeasure j, and by $a _ { i }$ the cost of (loss from) a successful attack episode of threat i. The available budget B for selected countermeasures implementation is limited. The subset of selected countermeasures $J S \subseteq J$ must satisfy the available budget constraint, $\sum { _ { j \in J S } } c _ { j } \leq B ,$ i.e., the total expenditures on the selected countermeasures cannot exceed the available budget B. Furthermore, the selected countermeasures are assumed to be feasible with respect to various additional constraints, e.g., they cannot contain mutually exclusive countermeasures or they must contain all countermeasures contingent on each other, etc.

The decision maker needs to decide which countermeasures to select to minimize losses from surviving occurrences of threats under limited budget for countermeasures implementation.

## 3. Models for selection of optimal countermeasure portfolio

In this section mixed integer programming models are proposed for a risk-neutral or risk-averse selection of optimal countermeasure portfolio, i.e., the selection of optimal subset of countermeasures for implementation in a risk-neutral or risk-averse environment.

Let L={0,1} be the set of implementation levels of each countermeasure, where l=0 denotes that a particular countermeasure is not selected for implementation, otherwise l=1. The decision whether or not to select a particular countermeasure will be represented by a binary variable $y _ { j l } , j \in J , l \in L ,$ where $y _ { j l } = 1$ , if countermeasure j is implemented at level l, otherwise $y _ { j l } = 0 ,$ that is, countermeasure j is selected for implementation $\mathrm { i f } y _ { j 1 } = 1$ and $y _ { j 0 } = 0 ,$ , otherwise $y _ { j 1 } = 0 { \mathrm { a n d } } y _ { j 0 } = 1$ . The above de<sup>fi</sup>nition implies that each countermeasure j is selected at exactly one level, i.e., $\scriptstyle \sum { \imath \in { \cal L } } y _ { j l } = 1$

Denote by $s _ { i j l } { = } m a x \{ 1 - l , r _ { i j } \}$ the proportion of threats i that survive if countermeasure j is implemented at level l, that is $s _ { i j 0 } = 1$ and $s _ { i j 1 } = r _ { i j } .$

## 3.1. Nonlinear model for minimization of expected cost

In a risk-neutral operating condition the overall quality of the selected countermeasure portfolio can be measured by the expected cost of losses from successful attacks.

The proportion of successful attacks of threats type i that survive all selected countermeasures is a multiplication of individual proportions of the selected countermeasures and can be expressed as

$$
\prod_ {j \in J} \left(\sum_ {l \in L} s _ {i j l} y _ {j l}\right).
$$

As a result, the expected cost of losses from successful attacks is given by a nonlinear formula

$$
\sum_ {k \in K} \sum_ {i \in I _ {k}} P _ {k} a _ {i} \left(\prod_ {j \in J} \left(\sum_ {l \in L} s _ {i j l} y _ {j l}\right)\right).\tag{1}
$$

The 0–1 nonlinear programming program NSP\_E for selection of optimal subset of countermeasures in a risk-neutral environment is formulated below.

Model NSP\_E: Selection of countermeasure portfolio to minimize expected cost.

Minimize Expected Cost (1) subject to

## 1. Countermeasure selection constraints:

– each countermeasure is selected at exactly one level (i.e., implemented or not implemented),

– the expenditures on selected countermeasures cannot exceed available budget,

$$
\sum_ {l \in L} y _ {j l} = 1; j \in J.\tag{2}
$$

$$
\sum_ {j \in J} c _ {j} y _ {j 1} \leq B.\tag{3}
$$

## 2. Integrality conditions:

$$
y _ {j l} \in \{0, 1 \}; j \in J, l \in L.\tag{4}
$$

The nonlinear integer program NSP\_E is computationally hard for solving, even for small size instances of the problem. The next subsection describes a recursive procedure that is capable of computing the nonlinear objective function (1) using a set of linear equations.

## 3.2. Linearizing the selection problem using a recursive technique

The nonlinear objective function (1) can be replaced with a for mula

$$
E (y) = \sum_ {k \in K} \sum_ {i \in I _ {k}} P _ {k} a _ {i} Z _ {i},\tag{5}
$$

where

$$
Z _ {i} = \prod_ {j \in J} \left(\sum_ {l \in L} s _ {i j l} y _ {j l}\right); i \in I,\tag{6}
$$

is the proportion of successful attacks of type i.

In order to compute $Z _ { i }$ for each threat i, a recursive procedure is proposed below.

Denote by

$$
z _ {i j} = \prod_ {k \in J: k \leq j} \left(\sum_ {l \in L} s _ {i k l} y _ {k l}\right); i \in I, j \in J,\tag{7}
$$

the proportion of surviving occurrences of threat i that passed countermeasures 1 through j. Note that (cf. Eqs. (6) and (7))

$$
Z _ {i} = z _ {i n}; i \in I.\tag{8}
$$

For each threat i∈I and countermeasure $j \in J ,$ , z can be calculated recursively as follows.

The initial condition that explicitly prescribes the <sup>fi</sup>rst term is

$$
z _ {i 1} = \sum_ {l \in L} s _ {i 1 l} y _ {1 l}; i \in I.\tag{9}
$$

The recurrence formula by means of which the remaining terms are determined inductively is

$$
z _ {i j} = \left(\sum_ {l \in L} s _ {i j l} y _ {j l}\right) z _ {i j - 1}, i \in I, j \in J.\tag{10}
$$

In order to eliminate nonlinear terms in the right-hand side of Eq. (10), de<sup>fi</sup>ne an auxiliary variable

$$
x _ {i j l} = y _ {j l} z _ {i j - 1}; i \in I, j \in J, l \in L,\tag{11}
$$

where $z _ { i 0 } = 1$ for all i, i.e., all threat events of each type i are capable of attacking IT infrastructure. Note that $x _ { i j l }$ represents the proportion of surviving occurrences of threat i to be addressed by countermeasure j at level l (cf. network <sup>fl</sup>ow model in [10] and [20]).

Substituting $x _ { i j l } = y _ { j l } z _ { i j - 1 }$ into Eq. (10) yields

$$
z _ {i j} = \sum_ {l \in L} s _ {i j l} x _ {i j l}; i \in I, j \in J,\tag{12}
$$

and, in particular, for $j = n ,$

$$
z _ {i n} = \sum_ {l \in L} s _ {i n l} x _ {i n l}; i \in I,\tag{13}
$$

where $z _ { i n } { = } Z _ { i }$ for all i ∈ I, Eq. (8).

On the other hand, replacing j with j + 1 in Eq. (11) gives

$$
x _ {i, j + 1, l} = y _ {j + 1, l} z _ {i j}; i \in I, j \in J: j <   n.\tag{14}
$$

Summing both sides of Eq. (14) on l for each i and j, and using the fact that $\textstyle \sum _ { l \in L } y _ { j + 1 , l } = 1 ; j \in J ,$ Eq. (2), yields

$$
\sum_ {l \in L} x _ {i, j + 1, l} = z _ {i j}; i \in I, j \in J: j <   n.\tag{15}
$$

Comparison of Eqs. (12) and (15) produces to the following relation

$$
\sum_ {l \in L} s _ {i j l} x _ {i j l} = \sum_ {l \in L} x _ {i, j + 1, l}; i \in I, j \in J: j <   n,\tag{16}
$$

that is, for each threat i, the proportion of occurrences which survive countermeasure j are addressed by countermeasure $j + 1$

Finally, setting j=1 and summing both sides of Eq. (11) on l, using the fact that $z _ { i 0 } = 1$ for all i and $\sum { } _ { l \in L } y _ { 1 l } = 1$ , Eq. (2), yields

$$
\sum_ {l \in L} x _ {i 1 l} = 1; i \in I,\tag{17}
$$

that is, all threat events of each type i are addressed by countermeasure $j = 1$

The above procedure eliminates all variables $z _ { i j }$ for each i, except for $z _ { i n } .$ . Summarizing, the proportion of successful attacks $Z _ { i } = z _ { i n }$ for each threat i can be calculated recursively, using Eqs. (17), (16) and (13) with $z _ { i n }$ replaced by $Z _ { i \cdot }$

Note that the linearizing procedure would not be possible if the implementation level l∈L={0,1} of each countermeasure $j \in J$ was not introduced and the variable y was replaced with a simple binary selection variable $y _ { j } \in \{ 0 , 1 \}$ , denoting whether or not countermeasure j is selected. In the latter case the proportion of threats i that survive whether or not countermeasure j is selected, is max{ $1 - y _ { j } , r _ { i j } \}$ , i.e., the survival proportions would depend nonlinearly on the selection variables $y _ { j } .$ In contrast to constant survival proportions $s _ { i j l } = m a x$ $\{ 1 - l , r _ { i j } \}$ for variables $y _ { j l } ,$ the survival proportions for variables y<sub>j</sub> could not be expressed by constant coef<sup>fi</sup>cients in the constraints.

The linearized version SP\_E of model NSP\_E is shown below (see also, network <sup>fl</sup>ow model in [10] and [20]).

Model SP\_E: Selection of countermeasure portfolio to minimize expected cost.

Minimize Expected Cost (5) subject to

1. Countermeasure selection constraints: Eqs. (2) and (3).

2. Surviving threats balance constraints:

$$
\sum_ {l \in L} x _ {i 1 l} = 1; i \in I.\tag{18}
$$

$$
\sum_ {l \in L} s _ {i j l} x _ {i j 1} = \sum_ {l \in L} x _ {i j + 1 l}; i \in I, j \in J: j <   n.\tag{19}
$$

$$
\sum_ {l \in L} s _ {i n l} x _ {i n l} = Z _ {i}; i \in I.\tag{20}
$$

$$
x _ {i j l} \leq y _ {j l}; i \in I, j \in J, l \in L.\tag{21}
$$

3. Non-negativity and integrality conditions:

$$
x _ {i j l} \geq 0; i \in I, j \in J, l \in L.\tag{22}
$$

$$
y _ {j l} \in \{0, 1 \}; j \in J, l \in L.\tag{23}
$$

$$
Z _ {i} \geq 0; i \in I.\tag{24}
$$

Constraint (21) (cf. Eq. (11)) ensures that threats can only by addressed by the implemented countermeasures.

Note that the expected proportion of successful attacks of threat type i is $p _ { i } Z _ { i } .$

Model SP\_E will be used to compare the risk-neutral results with those obtained by applying a risk aversive decision making model described in the next subsection.

## 3.3. Minimization of expected worst-case cost

In this subsection a risk-averse selection of optimal countermeasure portfolio is considered with the two popular in <sup>fi</sup>nancial engineering percentile measures of risk, VaR and CVaR, applied to control the risk of high losses. VaR and CVaR, are brie<sup>fl</sup>y de<sup>fi</sup>ned and compared below, see [25].

• Value-at-Risk (VaR) at a 100α% con<sup>fi</sup>dence level is the targeted cost of the portfolio such that for 100α% of the scenarios, the outcome will not exceed VaR. In other words, VaR is a decision variable based on the α-percentile of costs, i.e., in 100(1−α)% of the scenarios, the outcome may exceed VaR.

• Conditional Value-at-Risk (CVaR) at a 100α% con<sup>fi</sup>dence level is the approximate or exact (under certain conditions, e.g., [25]) expected cost of the portfolio in the worst 100(1−α)% of the cases. In other words, we allow 100(1−α)% of the outcomes to exceed VaR, and the mean value of these outcomes is represented by CVaR.

In other words, VaR is the acceptable cost level above which the number of outcomes should be minimized and CVaR considers those portfolio outcomes, where costs exceed VaR.

When selecting the optimal risk-averse countermeasure portfolio, the decision maker controls the risk of high losses caused by operational disruptions by choosing the con<sup>fi</sup>dence level α. The greater the con<sup>fi</sup>dence level α, the more risk aversive is the decision maker and the smaller percent of the highest cost outcomes is focused on. The risk aversive decision maker wants to minimize the expected worst-case costs exceeding VaR, by minimizing CVaR, given available budget B for selected countermeasures.

De<sup>fi</sup>ne $T _ { k }$ as the tail cost for attack scenario k, where tail cost is de-<sup>fi</sup>ned as the amount by which costs in scenario k exceed VaR. The countermeasure portfolio will be optimized by calculating VaR and minimizing CVaR simultaneously. By measuring CVaR, the magnitude of the tail costs is considered to achieve a more accurate estimate of the risks of minimizing cost. The mixed integer program SP\_CV for selection of countermeasure portfolio to reduce the risk of high costs is formulated below.

Model SP\_CV: Selection of countermeasure portfolio to minimize expected worst-case cost.

Minimize

$$
C V a R (y) = V a R + (1 - \alpha) ^ {- 1} \sum_ {k \in K} P _ {k} T _ {k}\tag{25}
$$

subject to

1. Countermeasure selection constraints: Eqs. (2)–(3).

2. Surviving threats balance constraints: Eqs. (18)–(21).

3. Risk constraints:

\- the tail cost for scenario k is de<sup>fi</sup>ned as the nonnegative amount by which costs in scenario k exceed VaR,

$$
T _ {k} \geq \sum_ {i \in I _ {k}} a _ {i} Z _ {i} - V a R; k \in K.\tag{26}
$$

4. Non-negativity and integrality conditions: Eqs. (22)–(24).

$$
T _ {k} \geq 0; k \in K.\tag{27}
$$

Note that VaR is a decision variable based on the α-percentile of costs, i.e., in 100(1−α)% of the attack scenarios, the outcome may exceed VaR. The decision maker is willing to accept only subsets of countermeasures for which the total probability of scenarios with costs greater than VaR is not greater than 1−α. While the con<sup>fi</sup>dence level α is speci<sup>fi</sup>ed by the decision maker, the targeted cost level VaR is optimized within the model. As $T _ { k }$ is constrained of being positive, the model tries to decrease VaR and hence positively impact the objective function. However, large reduction in VaR may result in more scenarios with positive tail costs, counterbalancing this effect, e.g. [8].

Instead of CVaR, a decision maker may decide to minimize expected loss for a given α and VaR, which may sometimes result in an infeasible solution or to maximize con<sup>fi</sup>dence level α for a given VaR, subject to an upper bound on expected loss, e.g., [4,26,28].

Models SP\_E and SP\_CV can be enhanced for simultaneous optimization of the expenditures on countermeasures and the cost of losses from successful attacks. Then, the budget constraints (3) should be removed from the models and the <sup>fi</sup>xed cost of selected countermeasures, $\sum _ { j \in J } c _ { j } y _ { j 1 }$ , added to the objective function.

De<sup>fi</sup>ne the <sup>fi</sup>xed cost of selected countermeasures as the required budget, B(y),

$$
B (y) = \sum_ {j \in J} c _ {j} y _ {j 1}.\tag{28}
$$

The enhanced models SP\_E+B and SP $\mathbf { C V } + \mathbf { B }$ for simultaneous optimization of <sup>fi</sup>xed cost of countermeasures and variable cost of losses from successful attacks are presented below.

Model SP $\mathbf { E } + \mathbf { B } \mathbf { \hat { \varepsilon } }$ Selection of countermeasure portfolio to minimize the required budget and expected cost.

Minimize Required Budget and Expected Cost

$$
B (y) + E (y)\tag{29}
$$

subject to Eqs. (2), (18)–(24) and (28).

Model SP\_CV+B: Selection of countermeasure portfolio to minimize the required budget and expected worst-case cost.

Minimize Required Budget and CVaR

$$
B (y) + C V a R (y)\tag{30}
$$

subject to Eqs. (2) and (18)–(28).

## 4. Bi-objective selection of countermeasures

In the single objective approach the countermeasure portfolio is selected by minimizing either the expected loss (plus the required budget) or the expected worst-case loss (plus the required budget). Since the probability of worst-case loss outcomes is usually very low, the expected cost function that aims at optimizing an average performance of IT security system, virtually neglects the worst-case losses. In contrast, CVaR that aims at optimizing worst-case performance, focuses on the low probability, high loss outcomes, and as the con<sup>fi</sup>dence level α increases a more risk-averse decision making focuses on a smaller set of the highest loss outcomes.

In this section the two con<sup>fl</sup>icting objectives are considered simultaneously, and a bi-objective selection of countermeasures is presented aimed at minimizing both objective functions to balance the required budget and expected cost with the risk tolerance. This trade-off model, known as the mean-risk model (e.g., [17]), is formulated as the optimization of a convex combination of the expected cost and the CVaR as a risk measure.

The nondominated solution set of the bi-objective countermeasure portfolio can be found by the parameterization on λ the weighted-sum program WSP. The scalarizing mixed integer program is based on SP $\mathbf { C V } + \mathbf { B }$ model with the addition of objective (5) of model SP\_E+B.

Model WSP: Bi-objective selection of countermesaure portfolio to minimize weighted sum of expected cost plus required budget and expected worst-case cost.

Minimize

$$
\lambda (B (y) + E (y)) + (1 - \lambda) C V a R (y)\tag{31}
$$

where $0 \leq \lambda \leq 1$ , subject to Eqs. (2), (5) and (18)–(28)

Now, the decision maker controls both the risk of high losses from successful cyber-attacks by choosing the con<sup>fi</sup>dence level α as well as the trade-off between expected and worst-case losses by choosing the trade-off parameter λ. Using the latter parameter, the level of risk allowed into the solution can be controlled. In particular, a decision maker may decide to minimize expected loss while requiring the percentile worst-case losses to be not greater than some parameter. In other words, she/he may use WSP model with λ=1 and include an upper bound on CVaR. However, when α increases so that the worst possible outcomes are considered only, imposing a strict bound on CVaR may always result in an infeasible solution, e.g., [8].

Note that for mixed integer programs, there may be portions of the nondominated set (nearby weakly nondominated solutions) that the above approach is unable to compute, even if the complete parameterization on λ is attempted, e.g., [30].

## 5. Computational examples

In this section some computational examples are presented to illustrate possible applications of the proposed scenario-based mixed integer programming approach for the selection of countermeasures to mitigate the impact of disruptions caused by IT security incidents. The following parameters have been used for the example problems:

• m=n, the number of threats and the number of countermeasures, were equal to 10, and the corresponding numbe $g = 2 ^ { m }$ of potential attack scenarios, was equal to 1024;

• a , loss from a successful attack of each threat i (in \$1000): $a _ { 1 } = 2 4$ $a _ { 2 } = 1 2 2 , a _ { 3 } = 3 5 0 , a _ { 4 } = 5 , a _ { 5 } = 2 5 0 , a _ { 6 } = 2 0 , a _ { 7 } = 2 0 , a _ { 8 } = 2 5 , a _ { 9 } =$ $3 0 , a _ { 1 0 } = 1 0 0 0 0 ;$

• c<sub>j</sub>, cost of each countermeasure j (in \$1000): c<sub>1</sub>=40, c<sub>2</sub>=28, c<sub>3</sub>= $\dot { 8 } 0 , c _ { 4 } = 2 4 , c _ { 5 } = 7 0 , c _ { 6 } = 5 0 , c _ { 7 } = 4 0 , c _ { 8 } = 4 5 , c _ { 9 } = 5 0 , c _ { 1 0 } = 8 0 ;$

• p<sub>i</sub>, probability of each threat i: p<sub>1</sub>= 0.35, p<sub>2</sub>= 0.25, p<sub>3</sub>= 0.15, p<sub>4</sub>= 0.25, p<sub>5</sub>= 0.20, p<sub>6</sub>= 0.25, p<sub>7</sub>=0.50, p<sub>8</sub>=0.35, p<sub>9</sub>= 0.40, $p _ { 1 0 } =$ 0.003;

• $r _ { i j } ,$ surviving proportions for each threat i and countermeasure j:

<table><tr><td>i/j</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1</td><td>0.01</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>1</td><td>0.04</td><td>1</td><td>1</td><td>0.6</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>1</td><td>1</td><td>0.01</td><td>0.8</td><td>1</td><td>0.8</td><td>0.9</td><td>0.95</td><td>0.9</td><td>1</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td>0.25</td><td>1</td><td>0.8</td><td>0.9</td><td>0.95</td><td>0.9</td><td>0.8</td></tr><tr><td>5</td><td>1</td><td>0.5</td><td>1</td><td>0.8</td><td>0.02</td><td>0.8</td><td>0.9</td><td>0.95</td><td>0.9</td><td>1</td></tr><tr><td>6</td><td>1</td><td>0.6</td><td>1</td><td>1</td><td>1</td><td>0.1</td><td>0.6</td><td>0.65</td><td>0.6</td><td>1</td></tr><tr><td>7</td><td>1</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>0.5</td><td>0.15</td><td>0.2</td><td>0.25</td><td>1</td></tr><tr><td>8</td><td>1</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>0.55</td><td>0.2</td><td>0.25</td><td>0.3</td><td>1</td></tr><tr><td>9</td><td>1</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>0.5</td><td>0.15</td><td>0.2</td><td>0.35</td><td>1</td></tr><tr><td>10</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.2</td></tr></table>

1. α, the con<sup>fi</sup>dence level, was equal to 0.50, 0.75, 0.90, 0.95 or 0.99; 2. B, available budget for countermeasures (in \$1000) was equal to 150, 300 or $\sum { } _ { j \in J } c _ { j } = 5 0 7$

The above data set is similar to the one presented in [20], which was based on the threat set reported on IT security forum EndpointSecurity.org [12]. Note that threat i =10 is a high-impact and low-probability threat with the cost of loss from successful attack equal to $a _ { 1 0 } = \$ 10$ M and the probability of occurrence equal to $p _ { 1 0 } { = } 0 . 0 0 3$ . Such a serious and rarely occurring event might be a compromise of customer-private data such as bank account numbers or social security numbers. The remaining threats are more typical such as viruses, data damages, or information disclosures, occurring more frequently and resulting in lower costs of losses from successful attacks. The off-diagonal surviving proportions $r _ { i j } , i \neq j$ , less than one, indicate that some countermeasures work against their primary threat as well as against other threats. For example, countermeasures $j = 2 , 6 , 7 , 8 , 9$ may represent strong security policies focused on particular threats and simultaneously showing bene<sup>fi</sup>ts across the other threats. In contrast, countermeasures j=1,3 reduce the survival proportions of a single threat only.

For the risk-neutral models SP\_E and SP\_E+B, solution results are shown in Table 2, and for the risk-averse models SP\_CV and SP\_CV+B with different con<sup>fi</sup>dence levels, in Tables 3 and 4. In addition to VaR and CVaR, for comparison with risk-neutral solutions, Tables 3 and 4 show the corresponding expected cost for the optimal risk-averse countermeasure portfolios. In the tables all costs are expressed in thousands of dollars.

For the risk-neutral models, Table 2 indicates that when SP\_E model is applied, the greater the available budget, the more countermeasures are selected to minimize expected cost. If, however, model SP\_E+B is used, a single countermeasure is selected only to minimize expenditures on countermeasures and expected cost of losses from successful attacks. For SP\_E model, Fig. 1 shows the probability mass function of optimal cost for the available budget $B { = } 1 5 0 ,$ , with the tail of cost distribution presented in a separate chart. Similarly, for SP\_E+B model with a variable budget, the probability mass function of optimal cost is shown in Fig. 2, where the tail of cost distribution is also presented in a separate chart.

Table 2  
Solution results for SP\_E and SP\_E+B models

<table><tr><td>Model</td><td colspan="3">SP_E</td><td>SP_E+B</td></tr><tr><td>Budget B</td><td>150</td><td>300</td><td>507</td><td>28</td></tr><tr><td>Expected cost</td><td>63.842</td><td>17.079</td><td>7.589</td><td>132.545</td></tr><tr><td>Selected countermeasures</td><td>2, 3, 7</td><td>2, 3, 5, 7, 10</td><td>1-10</td><td>2</td></tr></table>

For the risk-averse models, Tables 3 and 4 demonstrate that the number of selected countermeasures increases with the available budget, which indicates that the impact of disruption risks is mitigated by providing a more secure environment. When α increases, a more risk averse decision making focuses on a smaller set of outcomes, however the number of selected countermeasures is not increasing. For a limited budget, when α increases, the more expensive countermeasures against high-impact, low probability threats are more frequently selected. As a result the total number of all selected countermeasures decreases with α. The latter result is partly due to the parameter settings for which the countermeasure implementation costs do not always dominate the losses from successful cyber-threats. For example, costs of countermeasures 1, 4, 6, 7, 8 and 9 are higher than the losses from a single successful attack of the corresponding threats.

Note that for SP\_CV model, VaR becomes smaller than expected cost for all budget levels B, when $\alpha { = } 0 . 5 0$ and $\alpha { = } 0 . 7 5$ , and for all con<sup>fi</sup>dence levels α, when the highest budget level $B { = } \$ 507$ ,000 allows for the selection of all countermeasures, (see Table 3).

In the computational experiments with risk-averse models, the con<sup>fi</sup>dence level α is set at <sup>fi</sup>ve levels of 0.5, 0.75, 0.90, 0.95, and 0.99, which means that focus is on minimizing the highest 50%, 25%, 10%, 5%, and 1% of all scenario outcomes, i.e., costs of losses from successful attacks. For SP\_CV model, Fig. 3 shows the probability mass function of optimal cost for the available budget B=150 and con<sup>fi</sup>- dence level $\alpha { = } 0 . 9 9$ , with the tail of cost distribution presented in a separate chart. For SP\_CV+B model with a variable budget and con-<sup>fi</sup>dence level α=0.99 the probability mass function of optimal cost is shown in Fig. 4, where the tail of cost distribution is also presented in a separate chart. Figs. 1–4 indicate that the probability measure is concentrated in <sup>fi</sup>nitely many points, which is typical for the scenario-based optimization under uncertainty. (e.g., in Fig. 1, the probability measure is concentrated in four points). Moreover, the tail of cost distribution shows that the high cost probability is very low. As a result the expected cost for the optimal risk-neutral portfolio and CVaR for the optimal risk-averse portfolio are much lower than the corresponding worst-case cost outcomes.

Comparison of tails of the cost distributions for the corresponding risk-neutral and risk-averse solutions (i.e., Fig. 1 vs. Fig. 3 and Fig. 2 vs. Fig. 4) indicates that the optimal risk-averse countermeasure portfolio positively shapes the cost distribution, i.e., signi<sup>fi</sup>cantly reduces the worst-case cost outcomes. For example, the worst-case cost of \$10.6 M for the risk-neutral portfolio determined using SP\_E+B model is reduced to \$2.06 M, when the risk-averse portfolio is applied, determined using SP\_CV+B model.

For the bi-objective approach, the subsets of nondominated solutions were computed by parameterization on λ∈{0.01,0.10,0.25, 0.50,0.75,0.90,0.99} the weighted-sum program WSP. The results obtained for the con<sup>fi</sup>dence level $\alpha { = } 0 . 9$ are presented in Table 5. The trade-off between the required budget and expected cost, and CVaR is clearly shown in Fig. 5, where the convex ef<sup>fi</sup>cient frontier of Mean cost-CVaR model with $\alpha { = } 0 . 9$ is presented. The results emphasize the effect of varying cost/risk preference of the decision maker. The higher the weight λ for the required budget and expected cost, the smaller the number of selected countermeasures. When λ increases from 0.01 to 0.99, the size of the optimal countermeasure portfolio decreases from nine to one selected countermeasure. At the same time the required budget and expected cost decreases from \$464,908 to \$160,545, while CVaR increases from \$65,049 to \$710,691.

Table 4  
Table 3  
Solutions results for SP\_CV model.

<table><tr><td>Confidence level α</td><td colspan="4">0.50</td><td colspan="4">0.75</td></tr><tr><td>Budget B</td><td colspan="2">150</td><td>300</td><td>507</td><td>150</td><td colspan="2">300</td><td>507</td></tr><tr><td>CVaR</td><td colspan="2">121.130</td><td>29.154</td><td>14.839</td><td>224.294</td><td colspan="2">44.849</td><td>27.798</td></tr><tr><td>VaR</td><td colspan="2">13.500</td><td>10.128</td><td>1.078</td><td>23.780</td><td colspan="2">16.428</td><td>2.965</td></tr><tr><td>Expected cost</td><td colspan="2">63.842</td><td>17.079</td><td>7.589</td><td>63.842</td><td colspan="2">17.079</td><td>7.589</td></tr><tr><td>Selected countermeasures</td><td colspan="2">2, 3, 7</td><td>2, 3, 5, 7, 10</td><td>1-10</td><td>2, 3, 7</td><td colspan="2">2, 3, 5, 7, 10</td><td>1-10</td></tr><tr><td>Confidence level α</td><td colspan="2">0.90</td><td colspan="2">0.95</td><td colspan="4">0.99</td></tr><tr><td>Budget B</td><td>150</td><td>300</td><td>507</td><td>150</td><td>300</td><td>150</td><td>300</td><td>507</td></tr><tr><td>CVaR</td><td>393.775</td><td>84.185</td><td>64.597</td><td>478.204</td><td>145.744</td><td>124.985</td><td>921.449</td><td>624.627</td></tr><tr><td>VaR</td><td>302.500</td><td>21.450</td><td>3.769</td><td>318.880</td><td>24.178</td><td>4.663</td><td>414.500</td><td>29.028</td></tr><tr><td>Expected cost</td><td>92.045</td><td>17.079</td><td>7.589</td><td>92.045</td><td>17.079</td><td>7.589</td><td>92.045</td><td>17.079</td></tr><tr><td>Selected countermeasures</td><td>2, 4, 10</td><td>2, 3, 5, 7, 10</td><td>1-10</td><td>2, 4, 10</td><td>2, 3, 5, 7, 10</td><td>1-10</td><td>2, 4, 10</td><td>2, 3, 5, 7, 10</td></tr></table>

Solutions results for SP\_CV+B model.

<table><tr><td>Confidence level α</td><td>0.50</td><td>0.75</td><td>0.90</td><td>0.95</td><td>0.99</td></tr><tr><td>CVaR</td><td>144.008</td><td>67.089</td><td>109.323</td><td>172.808</td><td>652.214</td></tr><tr><td>VaR</td><td>29.380</td><td>34.500</td><td>42.928</td><td>49.500</td><td>59.000</td></tr><tr><td>Expected cost</td><td>80.570</td><td>31.332</td><td>31.332</td><td>31.332</td><td>31.332</td></tr><tr><td>Required budget</td><td>108</td><td>258</td><td>258</td><td>258</td><td>258</td></tr><tr><td>Selected countermeasures</td><td>2, 3</td><td>2, 3, 5, 10</td><td>2, 3, 5, 10</td><td>2, 3, 5, 10</td><td>2, 3, 5, 10</td></tr></table>

Note that the nondominated solutions of the weighted-sum program WSP with λ=1 and λ=0 are identical with the optimal solutions to single objective models SP\_E+B (Table 2) and SP\_CV with unlimited (the highest) budget B=\$507,000 (Table 3), respectively.

The computational experiments were performed using the AMPL programming language and the Gurobi 5.0.1 solver on a laptop MacBookPro 6.2 with Intel Core i7 processor running at 2.66 GHz and with 8 GB RAM. The Gurobi solver was capable of <sup>fi</sup>nding proven optimal solutions within CPU seconds for all examples.

Examples of the proposed mixed integer programs size for different numbers m=n of threats and countermeasures are shown in

![](/api/attachments/CRW5VW3S/fulltext/images/35c5927ab1795e6ef865a479dfca636badaeff96592effdfab41f138e0134344.jpg)

![](/api/attachments/CRW5VW3S/fulltext/images/ce16121c40d53728c97d2a6a455df874bccdcf0f466d8c5542c13821919a04ee.jpg)  
Fig. 1. Probability mass function for risk-neutral model SP\_E with B=\$150,000: Expected cost = \$63 842

Table 6. The size of the risk-neutral model SP\_E+B and the riskaverse model SP\_CV+B is represented by the total number of variables, Var., number of binary variables, Bin., and number of constraints, Cons. The CPU time in seconds required to prove optimality of the solution was ranging from fraction of a second to several hundred seconds. Note that the number of variables and constraints in the risk-averse model SP\_CV+B grows exponentially in the number m of threats, when all potential attack scenarios are considered. As a result, CPU time increases rapidly when the number of threats increases from m=10 to m=20.

## 6. Conclusion

The proposed scenario-based mixed integer programming approach for the selection of optimal countermeasure portfolio in IT security planning has allowed the two popular in <sup>fi</sup>nancial engineering percentile measures of risk, value-at-risk (VaR) and conditional value-at-risk (CVaR), to be applied. The resulting scenario-based optimization problem under uncertainty can be solved using commercially available software for mixed integer programming. The risk-averse countermeasure portfolio aimed at minimization of CVaR of losses from successful

![](/api/attachments/CRW5VW3S/fulltext/images/4d9d0a29acde50efed5fba15bbba16fa8fa6b78b8431709093bd587bba69cca8.jpg)

![](/api/attachments/CRW5VW3S/fulltext/images/83a5b07454f6cb0961ffce456907edfec5477a3260b62042d6576dc7a284a04b.jpg)  
Fig. 2. Probability mass function for risk-neutral model SP\_E+B: required budget= \$28 000 and expected cost= \$132 545.

![](/api/attachments/CRW5VW3S/fulltext/images/7cae95246640504b2cadf8b0e9441551a182b77fb4c97df8637fefbe1f72cbd2.jpg)

![](/api/attachments/CRW5VW3S/fulltext/images/92d35bf0fd437520b4277e849fef093dbaa76b07169f4ec5b7c5b0fae09dfeba.jpg)  
Fig. 3. Probability mass function for risk-averse model SP\_CV with B=\$150,000: α= 0.99. CVaR=\$921.449. VaR= \$414.500 and expected cost= \$92.045

breaches, optimizes the worst-case performance of an IT system, while a risk-neutral solution that minimizes expected losses does not suf<sup>fi</sup>ciently account for low-probability and high-impact cyber-threats. The riskaverse portfolio positively shapes cost distribution, i.e., signi<sup>fi</sup>cantly reduces the worst-case cost outcomes. While a single objective approach is capable of <sup>fi</sup>nding an optimal risk-neutral or risk-averse countermeasure portfolio that minimizes either mean cost or CVaR, respectively, a subset of nondominated portfolios can be found using the trade-off Mean cost-CVaR model. The trade-off model provides the decision maker with a simple tool for balancing expected and worst-case losses and for shaping of the resulting cost distribution through the selection of optimal countermeasure portfolio. The decision maker is capable of controlling both the risk of high losses from successful cyber-attacks by choosing the con<sup>fi</sup>dence level α as well as the trade-off between expected and worst-case losses by choosing the trade-off parameter λ that represents his/her cost vs. risk preference. Using the latter parameter, the level of risk allowed into the solution can be controlled.

![](/api/attachments/CRW5VW3S/fulltext/images/098bf03a093e634f19eef35d9f918673ff073c5690d19c28e46b0eb659588d0b.jpg)

![](/api/attachments/CRW5VW3S/fulltext/images/17dc3edda0962f8653170287cb0f360aac78f4900c866bf3cad4d17042fbc6ff.jpg)  
Fig. 4. Probability mass function for risk-averse model SP\_CV+B: α=0.99, CVaR= \$652 214 VaR= \$59 000 required budget= \$258 000 and expected cost=\$31.332

![](/api/attachments/CRW5VW3S/fulltext/images/f3be1f78739bceccd6e6450d0fed18c1232aa9e3747e1a3905e54db8d0fd1f87.jpg)  
Fig. 5. Ef<sup>fi</sup>cient frontier of Mean cost-CVaR model WSP: α=0.9

The higher the budget available and the higher the con<sup>fi</sup>dence level, the more risk-oriented is the countermeasure portfolio selected. In most cases the number of selected countermeasures increases with the available budget, and for a limited budget decreases with the con<sup>fi</sup>- dence level. For a limited budget and lower con<sup>fi</sup>dence level α, the expensive countermeasures against low-probability, high-impact threats are rarely selected, and as a result the total number of all selected countermeasures is usually greater than that for a higher α, when the more expensive countermeasures against high-impact threats are chosen.

The computational experiments prove that for a limited number of attack scenarios considered, the optimal risk-averse portfolio can be found within CPU seconds, using the Gurobi solver for mixed integer programming. However, when all potential attack scenarios need to be considered, the test examples were limited to 20 types of threats (and countermeasures) only, which sometimes may be insuf<sup>fi</sup>cient to consider larger size practical cases. For problem sizes with more types of threats and countermeasures the scenario-based mixed integer programs proposed may become intractable using Gurobi, if suf<sup>fi</sup>- cient memory for a branch-and-cut procedure is not available.

A critical issue that needs to be considered before any practical application of the proposed models is attempted, however, is the estimation of probabilities and the resulting losses associated with each type of threats and countermeasures. In practice, threat likelihood estimates are provided by security experts (e.g., [24]) and complete distributional information is not available. However, the proposed scenario-based approach does not require such a complete information to be available and only assumes independence of different threat events. In many cases they are independent of each other, but in principle might have a joint probability distribution. The future research should also consider selection of a countermeasure portfolio under the less restrictive assumptions on a joint probability of different cyber-threats. However, relaxation of the assumption of independent threat events may signi<sup>fi</sup>cantly complicate the problem of building potential attack scenarios. Various approaches have been proposed in the literature to correlate intrusion events and build attack scenarios from them, e.g., [15]. For example, modeling of attack scenarios with correlated threat events represented by Bernoulli random variables may require constructing of the corresponding correlated probability distribution, i.e., a correlated binomial distribution instead of the binomial distribution used in this paper.

Table 5  
Nondominated solutions of the weighted-sum program WSP for $\alpha { = } 0 . 9$

<table><tr><td>λ</td><td>0.01</td><td>0.10</td><td>0.25</td><td>0.50</td><td>0.75</td><td>0.90</td><td>0.99</td></tr><tr><td>CVaR</td><td>65.049</td><td>68.145</td><td>84.185</td><td>109.323</td><td>218.193</td><td>633.842</td><td>710.691</td></tr><tr><td>Expected cost</td><td>7.908</td><td>9.718</td><td>17.079</td><td>31.332</td><td>56.320</td><td>116.108</td><td>132.545</td></tr><tr><td>Required budget</td><td>457</td><td>388</td><td>298</td><td>258</td><td>188</td><td>52</td><td>28</td></tr><tr><td>Selected countermeasures</td><td>1-8, 10</td><td>1-3, 5-7, 10</td><td>2, 3, 5, 7, 10</td><td>2, 3, 5, 10</td><td>2, 3, 10</td><td>2, 4</td><td>2</td></tr></table>

Table 6  
Examples of mixed integer program size and CPU time.

<table><tr><td>m</td><td> $2^{ma}$ </td><td>Var. $^b$ </td><td>Bin.</td><td>Cons.</td><td>CPU $^c$ </td></tr><tr><td colspan="6">Risk-neutral model SP_E + B</td></tr><tr><td>10</td><td>1024</td><td>231</td><td>20</td><td>321</td><td>&lt;1</td></tr><tr><td>15</td><td>32,768</td><td>496</td><td>30</td><td>766</td><td>&lt;1</td></tr><tr><td>20</td><td>1,048,576</td><td>861</td><td>40</td><td>1241</td><td>&lt;1</td></tr><tr><td colspan="6">Risk-averse model SP_CV + B</td></tr><tr><td>10</td><td>1024</td><td>1256</td><td>20</td><td>1345</td><td>&lt;1</td></tr><tr><td>15</td><td>32,768</td><td>33,265</td><td>30</td><td>33,474</td><td>5</td></tr><tr><td>20</td><td>1,048,576</td><td>1,049,438</td><td>40</td><td>1,049,817</td><td>416</td></tr></table>

<sup>a</sup> m = number of threats (number of countermeasures) and 2<sup>m</sup> = number of attack scenarios.

<sup>b</sup> Var. = number of variables, Bin. = number of binary variables, and Cons. = number of constraints.

<sup>c</sup> CPU seconds for proving optimality on a MacBookPro 6.2, Intel Core i7, 2.66 GHz, RAM 8 GB/Gurobi 5.0.1.

## Acknowledgments

The author is grateful to two anonymous reviewers for their comments which helped to improve this paper. This work has been par tially supported by NCN research grant and by AGH.

## References

[1] C.J. Alberts, A.J. Dorofee, Managing Information Security Risks: The OCTAVE Approach, Addison Wesley Professional, 2002

[2] W. Baker, L. Wallace, Dependable Computing: Is Information Security Under Control? IEEE Security & Privacy, January/February 2007, pp. 24–32.

[3] W.H. Baker, L.P. Rees, P. Tippett, Necessary measures: metric-driven information security risk assessment and decision making, Communications of the ACM 50 (10) (2007) 101–106.

[4] S. Benati, R. Rizzi, A mixed integer linear programming formulation of the optimal mean/value-at-risk portfolio problem, European Journal of Operational Research 176 (2007) 423–434.

[5] S. Berinato, The state of information security, CIO Magazine 17 (2) (2003) 1–3.

[6] S. Bistarelli, F. Fioravanti, P. Peretti, Using cp-nets as a guide for countermeasure selection, Proceedings of the 2007 ACM Symposium on Applied Computing, Seoul, Korea, 2007, pp. 300–304.

[7] R. Bojanc, B. Jerman-Blazic, An economic modelling approach to information security risk management, International Journal of Information Management 28 (2008) 413–422.

[8] K. Chahara, K. Taaffe, Risk averse demand selection with all-or-nothing orders, Omega: International Journal of Management Science 37 (5) (2009) 996–1006.

[9] H. Chen, M. Chau, S. Li, Enterprise risk and security management: data, text and web mining, Decision Support Systems 50 (2011) 649–650

[10] J.K. Deane, C.T. Ragsdale, T.R. Rakes, L.P. Rees, Managing supply chain risk and disruption from IT security incidents, Operations Management Research 2 (1) (2009) 4–12.

[11] M. Egan, The Executive Guide to Information Security, Symantec Press, Indianapolis, 2005.

[12] Endpoint security, security breaches and the cost of downtime, http://www. endpointsecurity.org/Documents/Security\_Breaches\_and\_the\_Cost\_of\_Downtime.pdf.

[13] M. Gupta, J. Rees, A. Chaturvedi, J. Chi, Matching information security vulnerabilities to organizational security pro<sup>fi</sup>les: a genetic algorithm approach, Decision Support Systems 41 (2006) 592-603

[14] R.J. Kauffman, R. Sougstad, Risk management of contract portfolios in IT services: the pro<sup>fi</sup>t-at-risk approach, Journal of Management Information Systems 25 (1) (2008) 17–48.

[15] In: V. Kumar, J. Srivastava, A. Lazarevic (Eds.), Managing Cyber Threats: Issues, Approaches and Challenges, Kluwer Academic Publisher, 2004.

[16] Y.J. Lee, R.J. Kauffman, R. Sougstad, Pro<sup>fi</sup>t-maximizing <sup>fi</sup>rm investments in customer information security, Decision Support Systems 51 (2011) 904–920.

[17] W. Ogryczak, A. Ruszczynski, Dual stochastic dominance and related mean-risk models, SIAM Journal on Optimization 13 (2002) 60–78.

[18] A. Ojamaa, E. Tyugu, J. Kivimaa, Pareto-optimal situation analysis for selection of security measures, Proceedings of IEEE Military Communications Conference, MILCOM 2008, 2008, pp. 1–7, http://dx.doi.org/10.1109/MILCOM.2008.4753520.

[19] G.A. Paleologo, Price-at-risk: a methodology for pricing utility computing services, IBM Systems Journal 43 (1) (2004) 20–31.

[20] T.R. Rakes, J.K. Deane, L.P. Rees, IT security planning under uncertainty for high-impact events, Omega: International Journal of Management Science 40 (1) (2012) 79–88.

[21] L.P. Rees, J.K. Deane, T.R. Rakes, W.H. Baker, Decision support for cybersecurity risk planning, Decision Support Systems 51 (2011) 493–505.

[22] R.T. Rockafellar, S. Uryasev, Optimization of conditional value-at-risk, The Journal of Risk 2 (3) (2000) 21–41

[23] R.T. Rockafellar, S. Uryasev, Conditional value-at-risk for general loss distributions, Journal of Banking and Finance 26 (7) (2002) 1443–1471.

[24] J.J.C.H. Ryan, T.A. Mazzuchi, D.J. Ryan, J.L. de la Cruz, R. Cooke, Quantifying information security risks using expert judgment elicitation, Computers and Operations Research 39 (2012) 774–784.

[25] S. Sarykalin, G. Serraino, S. Uryasev, Value-at-risk vs. conditional value-at-risk in risk management and optimization, Tutorials in Operations Research, INFORMS 2008.2008. pp.270-294

[26] B. Sawik, Lexicographic and weighting approach to multi-criteria portfolio optimization by mixed integer programming chapter in: in: K.D. Lawrence, G. Kleinman (Eds.), Applications of Management Science: Financial Modeling Applications and Data Envelopment Applications, vol.13, Emerald, Bingley UK, 2009, pp. 3–18.

[27] T. Sawik, Selection of supply portfolio under disruption risks, Omega: The International Journal of Management Science 39 (2) (2011) 194–208.

[28] B. Sawik, Bi-criteria portfolio optimization models with percentile and symmetric risk measures by mathematical programming, Przeglad Elektrotechniczny 88 (10B) (2012) 176–180.

[29] T. Sawik, Selection of resilient supply portfolio under disruption risks, Omega: The International Journal of Management Science 41 (2) (2013) 259–269.

[30] R.E. Steuer, Multiple Criteria Optimization: Theory, Computation and Application, Wiley, New York, 1996.

[31] G. Stoneburner, A. Goguen, A. Feringa, Risk Management Guide for Information Technology Systems, Nat'l Inst. of Standards and Technology, US Dept of Commerce, 2002. (http://csrc.nist.gov/publications/nistpubs/800-30/sp800-30.pdf.).

[32] S. Uryasev, Conditional value-at-risk: optimization algorithms and applications Financial Engineering News 14 (2) (2000)

[33] V. Viduto, C. Maple, W. Huang, D. Lopez-Perez, A novel risk assessment and optimisation model for a multi-objective network security countermeasure selection problem, Decision Support Systems 53 (2012) 599–610.

[34] S. Wagner, C. Bode, An empirical examination of supply chain performance along several dimensions of risk, Journal of Business Logistics 29 (2008) 307–326.

[35] J. Wang, A. Chaudhury, H.R. Rao, A value-at-risk approach to information security investment, Information Systems Research 19 (1) (2008) 102–120.

![](/api/attachments/CRW5VW3S/fulltext/images/fb7e5582d3b44a731e9d2b70429c43de4386ed989e2768101d24fd9474df4a01.jpg)

Tadeusz Sawik is Professor of Industrial and Systems Engineering and Head of the Department of Operations Research and Information Technology at AGH University of Science and Technology in Kraków, Poland. He received the MS degree in mechanical engineering, the PhD degree in control engineering and the ScD (habilitation) degree in operations research, all from AGH University. He has served as a research advisor of Motorola and <sup>fi</sup>ve times received Scienti<sup>fi</sup>c Achievement Award from the Minister of Science and Higher Education. His current research interests are in the area of supply chain optimization, risk management, scheduling and integer programming. He has published numerous books (including Production Planning and Scheduling in Flexible Assembly Systems, Springer, 1998

and Scheduling in Supply Chains Using Mixed Integer Programming, Wiley, 2011), and more than 150 individual articles in refereed journals. His articles have appeared in Computers &τ Operations Research. Furopean Journal of Operational Research Internation: al Journal of Production Economics, International Journal of Production Research, Journal of Electronics Manufacturing, Journal of the Operational Research Society, Mathematical and Computer Modelling, Omega, and others. He is currently the Editor-in-Chief of Deci sion Making in Manufacturing and Services (AGH University Press).
