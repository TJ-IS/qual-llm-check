---
otero_id: 17551
otero_key: "QWXNV6HB"
title: "Fractional piecewise linear optimization of the business process including investments"
authors: "Ivan Meško; Tjaša Meško"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90005-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fractional piecewise linear optimization of the business process including investments

Ivan Meško \*

University of Maribor, Department of Economics, Maribor, Slovenia

## Tjaša Meško

University of Ljubljana, Faculty of Electrical and Computer Engineering, Ljubljana, Slovenia

The paper deals with the problem of choosing the most appropriate combination of investment projects which maximizes the rate of return. The considered investments concern the improvement or the expansion of the given business process. The maximization of the increase of the difference between income and costs per invested monetary unit by means of a fractional piecewise linear optimization model is explained along with an example from the metallurgic industry. The obtained model is transformed into a linear mixed integer programming problem.

Keywords: Business process optimization; Investments; Mixed integer programming; Fractional programming

## 1. Introduction

To solve a multi-phase business process optimization problem, we usually have to determine the process parameters which ensure the maximal difference between income and variable costs considering the technological and market constraints. Simple optimization problems can be solved by means of linear programming. If piecewise linear functions appear in the optimization model, it can be transformed into a linear mixed integer programming problem $[3]$ . However, such a programming problem is not applicable as soon as the selection of the investment projects is taken into consideration. The efficiency of investment combinations is namely measured according to the rate of return which is expressed in a form of a quotient. In this contribution we deal with investments concerning the modernization of the technological process, the enhancement of the market share, and the adjustment of the business process to the technological changes and to the changes in market conditions.

![](/api/attachments/QWXNV6HB/fulltext/images/d68cde9fbb510dd56f941b07ba80e18468753b8a39e1843ae390efcd004b9035.jpg)

We have limited ourselves to the selection of investments that give the largest rate of return in the first year of the first period after realization. We construct two optimization models. The first one is meant to determine the maximal differ-

tions Research Institute. He used to be a programme committee member of the former Yugoslav Symposium on Operations Research. His current research activities are in the operations research field, namely business optimization and piecewise linear optimization.

Ivan Meško was born in 1933. He received the B.Sc. degree in mathematics from the University of Ljubljana, Department of Mathematics in 1961 and the M.Sc. and Ph.D. degrees from the University of Ljubljana, Department of Economics in 1971 and 1974, respectively. He joined the faculty of the Department of Economics, University of Maribor in 1968. He is Professor in that department since 1975 and since 1990 he is a director of the department's Operaence between income and costs before the realization of the investments. In the second one, all feasible investment projects are considered as well and the best combination of them is selected. This combination results in the maximal increase of the difference between income and costs per invested monetary unit. To each feasible investment project a zero-one variable belongs in the second model. Its value is 1 if the adequate investment is realized. In this way we obtain a fractional piecewise linear programming problem which can be transformed into a linear mixed integer programming problem. Namely, first a Charnes–Cooper transformation [1] is applied in order to obtain a quadratic mixed integer programming problem containing apart from linear terms, also products between zero-one and continuous variables. Such products can easily be linearized [3].

![](/api/attachments/QWXNV6HB/fulltext/images/a08d4046bd53577d476a615d7fa6839472a8c45b4ef445dc0772629c2e09f30d.jpg)  
Tjaša Meško was born in 1967. She received the B.Sc. and the M.Sc. degrees in computer science from the University of Ljubljana, Faculty of Electrical and Computer Engineering in 1989 and 1992, respectively. She is currently a Ph.D. student at the Faculty of Electrical and Computer Engineering, University of Ljubljana. Her interests include optimization problems by means of classical approaches as well as neural networks. She is also dealing with classification problems using neural networks.

In the following section, the optimization model is described. The third section describes the transformations of the original programming problem into a linear mixed integer one. In the fourth section, the described method is illustrated by a simplified metallurgy application.

## 2. Optimization model

In order to determine the optimal investments combination, the following optimization model is obtained,

$$
\max \frac {s - \sum_ {i} \sum_ {k} C _ {i k} u _ {i k} - z _ {0}}{\sum_ {i} \sum_ {k} g _ {i k} u _ {i k}}\tag{1}
$$

where $s = \sum_{i} \sum_{k} p_{ik} z_{ik} - \sum_{i} \sum_{k} c_{ik} y_{ik} - \sum_{j} m_{j} x_{j}$ and therefore defines the contribution, subject to the non-negative variables $x_{j}$ , $z_{ik}$ and $y_{ik}$ , zero-one variables $u_{ik}$ and

$$
\sum_ {j \in R _ {i}} r _ {i j} x _ {j} + \sum_ {k} y _ {i k} - \sum_ {j \in Q _ {i}} q _ {i j} x _ {j} - \sum_ {k} z _ {i k} \geq 0, \quad \forall i\tag{2}
$$

$$
d _ {i k} \leq z _ {i k} \leq D _ {i k} + \delta_ {i k} u _ {i k}, \quad \text { for   some } \quad i, k\tag{3}
$$

$$
b _ {i k} \leq y _ {i k} \leq B _ {i k} + \beta_ {i k} u _ {i k}, \quad \text { for   some } \quad i, k
$$

$$
\sum_ {i} \sum_ {k} g _ {i k} u _ {i k} \leq G.\tag{4}
$$

(5)

The description of parameters and variables used in the model is as follows,

$z_{ik}$ – the amount of the ith element sold to the kth customer,

$p_{ik}$ – the sales price of the ith element for the kth customer,

$y_{ik}$ – the amount of the ith element purchased in the kth source,

$c_{ik}$ - the purchase price of the $i$ th element in the $k$ th source,

$x_{i}$ - quantity of the $j$ th production activity,

$m_{j}$ – the marginal costs of the jth production activity not related to the elements considered in the model,

$u_{ik}$ – a zero-one decision variable assigned to the investment which has the impact on the expansion of the kth source capacity or kth selling ability of the ith element,

$C_{ik}$ - semi-fixed costs caused by the adequate investment,

$z_{0}$ – the maximal difference between the income and variable costs before the realization of the investments,

$g_{ik}$ - capital needed for the realization of the adequate investment,

$r_{ij}$ – the amount of the ith element produced per unit of the jth production activity,

$R_{i}$ – the index set of activities for producing the ith element,

$q_{ij}$ - the consumed amount of the $i$ th element per unit of the $j$ th production activity,

$Q_{i}$ - the index set of activities for processing the $i$ th element,

$d_{ik}$ – the obligatory amount of selling the ith element to the kth customer,

$D_{ik}$ – the maximal possible amount of selling the ith element to the kth customer,

$\delta_{ik}$ – the increase of the ability of selling the ith element to the kth customer caused by the corresponding investment,

$b_{ik}$ – the obligatory amount of purchasing the ith element from the kth source,

$B_{ik}$ – the maximal possible amount of purchasing the ith element from the kth source,

$\beta_{ik}$ – the increase of the capacity of the kth source for purchasing the ith element, caused by the corresponding investment,

G - maximal available capital for all the investments.

The objective function is constructed as follows. The first sum in the definition of the contribution, s, in (1) is the income. By the second and third sum we consider the variable costs and the fourth sum represents the semi-fixed costs arising due to investing. The denominator of the fraction represents the sum of the invested means. It is positive if at least one investment is realized. The value of $z_{0}$ is determined as the maximum of the following linear programming problem,

$$
\max \sum_ {i} \sum_ {k} p _ {i k} z _ {i k} - \sum_ {i} \sum_ {k} c _ {i k} y _ {i k} - \sum_ {j} m _ {j} x _ {j}
$$

subject to (2) and,

$$
\begin{array}{l l} d _ {i k} \leq z _ {i k} \leq D _ {i k} & \text { for   some } \quad i, k \\ b _ {i k} \leq y _ {i k} \leq B _ {i k} & \text { for   some } \quad i, k. \end{array}
$$

Let us now describe the constraints beginning with (2). The first and second sum represent the produced and purchased quantity of the ith element, respectively. The sum of the first two sums of (2) is therefore the amount of the ith element available for processing and for selling. The last two sums represent the processed and sold amount of the ith element, respectively. It is obvious that the difference between the first two and the second two sums has to be non-negative. In some cases, for a given element one or two sums can be absent. The constraint (2) is constructed for any element, which means for production elements and for products of all production phases. For the production elements that have no limitations in purchasing we do not construct constraint (2). The variable costs corresponding to the consumption of such elements is considered by the third sum in the definition of the contribution. The inequalities of the form (3) and (4) express the market constraints. We can also consider the limitations of production capacities in a similar form as inequality (4). The constraint (5) is optional. It is included in case the investment funds are limited. In a similar way some other financial conditions can be considered.

## 3. Transformation of the model

The optimization model (1)-(5) can be transformed into the linear mixed integer programming problem. The variables $t$ , $Y_{ik}$ , $Z_{ik}$ and $X_{ik}$ are introduced by the Charnes-Cooper transformation [1] in order to eliminate the fraction. Namely, the denominator of (1) is positive and therefore we can take

$$
\sum_ {i} \sum_ {k} g _ {i k} t u _ {i k} = 1,
$$

where t is a positive variable. Furthermore we introduce new variables,

$$
y _ {i k} t = Y _ {i k}, \quad z _ {i k} t = Z _ {i k}, \quad x _ {j} t = X _ {j}.
$$

By means of this transformation we obtain a quadratic mixed integer programming problem,

$$
\begin{array}{l} \max \sum_ {i} \sum_ {k} p _ {i k} Z _ {i k} - \sum_ {i} \sum_ {k} c _ {i k} Y _ {i k} - \sum_ {j} m _ {j} X _ {j} \\ - \sum_ {i} \sum_ {k} C _ {i k} t u _ {i k} - z _ {0} t, \end{array}
$$

subject to

$$
\sum_ {i} \sum_ {k} g _ {i k} t u _ {i k} = 1
$$

$$
\sum_ {j \in R _ {i}} r _ {i j} X _ {j} + \sum_ {k} Y _ {i k} - \sum_ {j \in Q _ {i}} q _ {i j} X _ {j} - \sum_ {k} Z _ {i k} \geq 0, \quad \forall i
$$

$$
d _ {i k} t \leq Z _ {i k} \leq D _ {i k} t + \delta_ {i k} t u _ {i k}
$$

$$
b _ {i k} t \leq Y _ {i k} \leq B _ {i k} t + \beta_ {i k} t u _ {i k}
$$

$$
\sum_ {i} \sum_ {k} g _ {i k} t u _ {i k} \leq G t.
$$

By a straightforward proof, we can see that each quadratic term $tu_{ik}$ can be replaced by a nonnegative variable $v_{ik}$ , subject to

$$
\begin{array}{l} t = v _ {i k} + w _ {i k} \\ 0 \leq s v _ {i k} \leq u _ {i k} \\ 0 \leq s w _ {i k} \leq 1 - u _ {i k}. \end{array}
$$

Here, s is a suitable, small enough positive constant and $w_{ik}$ is an additionally introduced non-negative variable. As a result, the linear mixed integer programming problem is obtained. For each zero-one variable, three new constraints and two new non-negative variables are introduced. It is of importance that due to the described transformation techniques the total number of constraints does not increase considerably because there are normally only a few feasible investment projects. Such a programming problem can therefore be solved also for large-scale models by available computer programs.

## 4. Example

We will consider a simplified example from metallurgy. Let us first describe the business process before the realization of investments. In a rolling mill, alu sheets are produced from the ingots. It is possible to buy at the most 50 tons of ingots in one week. The price of a ton is 12 monetary units. Let us assign the decision variable $y_{1}$ to the quantity of purchased ingots. At the most 20 tons of ingots can be rolled per day and the mill operates 5 days per week. The energy needed for each operating day costs 8 monetary units. The decision variable $y_{2}$ represents the amount of operating days per week. From one ton of ingots 0.8 ton of alu sheets and 0.2 ton of cuttings are produced. Cuttings are sold for 7 monetary units per ton. Let the value of the decision variable $z_{4}$ be the amount of sold cuttings in tons and $x_{1}$ the amount of production activity rolling. It is given in tons of consumed ingots. Due to the rolling process, an additional variable cost of 3 monetary units per unit of consumed ingots arises. Alu sheets can be sold to two customers. The first customer pays 20 and the second one pays 18 monetary units per ton. The obligatory amount which has to be sold to the first customer is 4 tons and the maximal amount is 6 tons per week. To the second customer, at most 30 tons can be sold per week. Let $z_{31}$ and $z_{32}$ be the belonging decision variables.

The maximal difference between the income and variable costs before the realization of investments is obtained by solving the following programming problem,

max $20z_{31} + 18z_{32} + 7z_4 - 12y_1 - 8y_2 - 3x_1,$ subject to

$$
y _ {1} - x _ {1} \geq 0, \quad y _ {1} \leq 5 0
$$

$$
y _ {2} - 0. 0 5 x _ {1} \geq 0, \quad y _ {2} \leq 5
$$

$$
0. 8 x _ {1} - z _ {3 1} - z _ {3 2} \geq 0, \quad 4 \leq z _ {3 1} \leq 6, \quad z _ {3 2} \leq 3 0
$$

$$
0. 2 x _ {1} - z _ {4} \geq 0.
$$

The obtained optimal value of the objective function is 30 monetary units.

There are three possible investments. The equipment for producing alu foil from alu sheets can be purchased. Again, cuttings appear as well being a result of the alu foil producing process. It is possible to sell at most 15 tons of foil per week at a price of 26 monetary units per ton. Further, a market research can be carried out to enable selling unlimited quantities of alu foil at a price of 28 monetary units per ton. Moreover, in order to process the cuttings, a foundry can be built to reproduce the ingots. At the most 5 tons of ingots can be produced by the foundry per day. The corresponding daily energy cost is 7 monetary units. The belonging decision zero-one variable for the first investment is $u_5$ , for the second one is $u_{62}$ and for the third one is $u_7$ . The capital required for investing is 3000, 800 and 2000 monetary units, respectively.

All necessary data is given in Table 1 and in Figure 1. The figure can be interpreted as the following example shows. One unit of ingots and 0.05 unit of the plate rolling mill capacity are consumed and 0.8 unit of alu sheets and 0.2 unit of cuttings are produced per one unit of production activity $X_{1}$ . Additional variable costs per unit of this production activity are 3 monetary units.

Fixed costs that arise weekly are increased by one percent of the invested capital.

![](/api/attachments/QWXNV6HB/fulltext/images/879a3405aefe1d45b067a36911d3b7b07fda06c4fb12fdb26917aeb0bc9e8d06.jpg)  
Fig. 1. Technological data.

Table 1
Market data

<table><tr><td colspan="2">Element</td><td rowspan="2">Source Customer</td><td rowspan="2">Price Cost</td><td rowspan="2">Minimal quantity</td><td rowspan="2">Maximal quantity</td></tr><tr><td>Symbol</td><td>Name</td></tr><tr><td>E1</td><td>Ingots</td><td> $y_{1}$ </td><td>12</td><td></td><td>50</td></tr><tr><td>E2</td><td>Rolling nill</td><td> $y_{2}$ </td><td>8</td><td></td><td>5</td></tr><tr><td rowspan="2">E3</td><td rowspan="2">Alu sheets</td><td> $z_{31}$ </td><td>20</td><td>4</td><td>6</td></tr><tr><td> $z_{32}$ </td><td>18</td><td></td><td>30</td></tr><tr><td>E4</td><td>Cuttings</td><td> $z_{4}$ </td><td>7</td><td></td><td></td></tr><tr><td>E5</td><td>Foil producing machine</td><td> $y_{5}$  $u_{5}$ </td><td>3000</td><td></td><td>5</td></tr><tr><td rowspan="3">E6</td><td rowspan="3">Foil</td><td> $z_{61}$ </td><td>26</td><td></td><td>15</td></tr><tr><td> $z_{62}$ </td><td>28</td><td></td><td></td></tr><tr><td> $u_{62}$ </td><td>800</td><td></td><td></td></tr><tr><td rowspan="2">E7</td><td rowspan="2">Foundry</td><td> $y_{7}$ </td><td>7</td><td></td><td>5</td></tr><tr><td> $u_{7}$ </td><td>2000</td><td></td><td></td></tr></table>

The obtained programming problem is therefore,

$$
\max \frac {s - 3 0 u _ {5} - 8 u _ {6 2} - 2 0 u _ {7} - 3 0}{3 0 0 0 u _ {5} + 8 0 0 u _ {6 2} + 2 0 0 0 u _ {7}},
$$

where $s = 20z_{31} + 18z_{32} + 7z_{4} + 26z_{61} + 28z_{62} - 12y_{1} - 8y_{2} - 7y_{7} - 3x_{1}$ , subject to zero-one variables $u_{5}$ , $u_{62}$ and $u_{7}$ ; other variables are non-negative, and subject to the following constraints,

$$
y _ {1} + x _ {3} - x _ {1} \geq 0, \quad y _ {1} \leq 5 0
$$

$$
y _ {2} - 0. 0 5 x _ {1} \geq 0, \quad y _ {2} \leq 5
$$

$$
0. 8 x _ {1} - x _ {2} - z _ {3 1} - z _ {3 2} \geq 0, \quad 4 \leq z _ {3 1} \leq 6,
$$

$$
z _ {3 2} \leq 3 0
$$

$$
0. 2 x _ {1} + 0. 1 x _ {2} - x _ {3} - z _ {4} \geq 0
$$

$$
y _ {5} - 0. 2 x _ {2} \geq 0, \quad y _ {5} \leq 5 u _ {5}
$$

$$
0. 9 x _ {2} - z _ {6 1} - z _ {6 2} \geq 0, \quad z _ {6 1} \leq 1 5,
$$

$$
z _ {6 2} \leq 5 0 u _ {6 2}\tag{6}
$$

$$
y _ {7} - 0. 2 x _ {3} \geq 0, \quad y _ {7} \leq 5 u _ {7}
$$

$$
u _ {5} + u _ {6 2} + u _ {7} = 1.\tag{7}
$$

In the constraint (6), the coefficient belonging to $u_{62}$ is an arbitrarily chosen large enough constant. The constraint (7) enables the selection of exactly one investment.

This model is transformed into a linear mixed integer programming problem as described in section 2. Solving the programming problem, the following values for zero-one variables turn out to be optimal,

$$
u _ {5} = 1, \quad u _ {6 2} = u _ {7} = 0.
$$

This means that investing in equipment for producing foil ensures the largest rate of return. In case the constraint (7) is omitted we obtain,

$$
u _ {5} = u _ {6 2} = 1, \quad u _ {7} = 0.
$$

The optimal investment combination therefore includes a market research along with investing in the foil producing equipment.

## 5. Discussion

The hereby explained optimization technique is used for evaluating the combinations of investment projects. It finds the best combination according to the rate of return in the first year after realization of the projects. However, if a longer period is considered there are factors that affect the rate of return. Namely, the amount of invested capital decreases due to the amortization which is included in the semi-fixed costs. This increases the rate of return be it that the other conditions remain unchanged. On the other hand, the rate of return can decrease due to the changes of the market and the technological conditions.

In order to compare the rate of return of the investments discussed in this paper with investing into common stocks and other securities, both mentioned effects have to be considered. One can approximately determine the increase of the rate of return by adapting the coefficients belonging to the zero-one variables in the nominator of the objective function. However, the technological progress is more difficult to consider. Talmor and Thompson have for example adapted Krouse's model [4]. In our case, it is more important to take into account the decrease of the rate of return arising due to the fact that the investment projects grow out of date. However, this surpasses the purpose of this work.

The risk can be estimated by the standard deviation of the rate of return [2]. One could estimate it by performing a simulation of the business process after the realization of selected investment projects simulating the values of the parameters which depend on random influences. For each simulated realization, an optimization model without zero-one variables is obtained because the investment projects are already selected. In case the basic optimization model is linear, for each simulation a linear programming problem has to be solved. As a result, the rates of return for each simulation are obtained and one can estimate the standard deviation.

## References

[1] A. Charnes and W.W. Cooper, Programming with Linear Fractional Functionals, Naval Research Logistic Quarterly 9 (1962) pp. 181–186.

[2] R.A. Haugen, Modern Investment Theory, Second Edition (Prentice-Hall, New Jersey, 1990).

[3] I. Meško, Piecewise Linear Approximations in $\mathfrak{R}^n$ , Operations Research Proceedings 1986 (Springer, Berlin, 1987) pp. 618-625.

[4] E. Talmor and H.E. Thompson, Technology, Dependent Investments, and Discounting Rules for Corporate Investment Decisions, Managerial and Decision Economics 13 (1992) pp. 101–109.
