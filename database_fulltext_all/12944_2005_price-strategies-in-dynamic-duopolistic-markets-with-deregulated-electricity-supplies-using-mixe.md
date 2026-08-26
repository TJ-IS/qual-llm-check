---
otero_id: 12944
otero_key: "K5FCSF3G"
title: "Price strategies in dynamic duopolistic markets with deregulated electricity supplies using mixed strategies"
authors: "Jose B. Cruz; Xiaohuan Tan"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Price strategies in dynamic duopolistic markets with deregulated electricity supplies using mixed strategies

Jose B. Cruz Jr. $^{*}$ , Xiaohuan Tan

Department of Electrical and Computer Engineering, The Ohio State University, 205 Dreese Laboratory, 2015 Neil Avenue, Columbus, OH 43210-1272, USA

Available online 10 July 2004

## Abstract

While effective competition can force service providers to seek economically efficient methods to reduce costs, the deregulated electricity supply industry still allows some generators to exercise market power at particular locations, thereby preventing the deregulated power market to be perfectly competitive. In this paper, we investigate the interdependence of pricing mechanisms and strategy behaviors of the suppliers. A multiperiod dynamic profit-maximizing problem is converted to a bimatrix game that is solved in the framework of mixed strategies. By this procedure, we have at least one Nash solution. Instead of considering only perfectly competitive price and monopoly price, we introduce other prices between these two to simulate the real market better. Numerical examples show that the new entrant that maximizes its profit will not choose the perfectly competitive price even as an entry price.
© 2004 Published by Elsevier B.V.

Keywords: Mixed strategies; Price strategies; Deregulated electricity supplies

## 1. Introduction

While effective competition can force service providers to seek economically efficient methods to reduce costs, the deregulated electricity supply industry still allows some generators to exercise market power at particular locations, thereby preventing the deregulated power market to be perfectly competitive. The principal source of market power is due to the natural monopoly characteristics of transmission.

A series of conceptual analyses by Schuler $[2,3]$ and Schuler and Hobbs $[4]$ has identified a second likely source of market power to be the slow response of consumers to lower price supply options offered by new entrants in the deregulated markets. The interdependence between pricing mechanisms and strategy behaviors of the suppliers has been examined, given different initial market shares of the suppliers and lagged customer response to the price difference. A multiperiod dynamic profit-maximizing duopoly was formulated. This is a difficult nonlinear programming duopoly problem. He approximated this by a simpler bimatrix game. However, in Refs. [2-4], only marginal price and monopoly price, which are 0 and 1 after normalization, are considered at each temporal stage such that in a three time period problem, there are only four available price sequences to be chosen from. Besides, there is no guarantee that a pure Nash solution may exist for all cases.

In this paper, we first generalize Schuler's work and extend the problem by introducing more discrete prices while maintain the advantage of bimatrix games. Instead of considering only extreme prices, we introduce 2 other predetermined fixed price levels between the static perfect competition price and the static monopolistic price such that we have 4 price alternatives at each temporal stage, thus 16 price sequences for the same problem mentioned above. Distinguished from previous work, we propose to solve the problem in the framework of mixed strategies instead of pure strategies. By this procedure, we guarantee to have at least one Nash equilibrium and no mixed solution will be missed.

The paper is organized as follows: In Section 2, we describe the general problem for a nonzero sum non-cooperative game; in Section 3, we explain the formation of a bimatrix game; in Section 4, we define the Nash equilibrium for mixed strategies and describe the methodology used to find the possible equilibrium. Numerical examples are given in Section 5 and conclusions are drawn in the last section.

## 2. A general problem of non-zero-sum non-cooperative game

Suppose there are two non-cooperative power suppliers, P1 and P2, in the market. The total demand over T periods is Q and the demand for period t is weighted by $\alpha_{t}$ , such that

$$
\alpha_ {t} \cdot Q = Q _ {t}
$$

where $Q_{t}$ is the total demand over period $t$ . It is clear that $\sum_{t=1}^{T} \alpha_{t} = 1$ .

Assume that a linear demand function for supplier $i \in \{P1, P2\}$ over period t is of the form

$$
q _ {t} ^ {i} = A _ {t} ^ {i} - B _ {t} ^ {i} p _ {t} ^ {i}
$$

where $A_{t}^{i}$ , $B_{t}^{i}$ are constants. For a certain period t, the total demand for the suppliers is constrained by

$$
q _ {t} ^ {i} + q _ {t} ^ {j} = Q _ {t}
$$

Let the cost function for supplier P2 be the form of

$$
h _ {t} ^ {i} \left(q _ {t} ^ {i}\right) = \frac {1}{2} c _ {i} \left(q _ {t} ^ {i}\right) ^ {2} + K _ {i} ^ {2}
$$

where $c_{i}$ and $K_{i}$ are constants. The profit function for firm i over period t is then written as

$$
\begin{array}{r l} & {\pi_ {t} ^ {i} = p _ {t} ^ {i} q _ {t} ^ {i} - h _ {t} ^ {i} (q _ {t} ^ {i})} \\ & {\quad = p _ {t} ^ {i} (A _ {t} ^ {i} - B _ {t} ^ {i} p _ {t} ^ {i}) - \frac {1}{2} c _ {i} (A _ {t} ^ {i} - B _ {t} ^ {i} p _ {t} ^ {i}) ^ {2} - K _ {i} ^ {2}} \end{array}
$$

in which price is the only variable. For simplicity, all prices are normalized in the following way:

$$
p = \frac {p _ {\mathrm{act}} - p _ {\mathrm{mar}}}{p _ {\mathrm{mon}} - p _ {\mathrm{mar}}}
$$

where $p, p_{act}, p_{mar}, p_{mon}$ denote normalized price, actual price, marginal price and monopoly price, respectively. By this means, all prices stay between 0 and 1, which stand for marginal cost and monopoly price, respectively. Thus, the profit is considered per unit per MW h per dollar.

Suppose the market share of supplier P1 over period t is $S_{t}^{i}$ , the logistic adjustment mechanism is

$$
S _ {t + 1} ^ {i} - S _ {t} ^ {i} = \lambda \big (p _ {t} ^ {j} - p _ {t} ^ {i} \big) \big (1 - S _ {t} ^ {i} \big) S _ {t} ^ {i}
$$

where $\lambda$ is the adjustment rate which is constant for multiperiod. Similarly, for supplier j, the market share is determined by

$$
S _ {t + 1} ^ {j} - S _ {t} ^ {j} = \lambda \left(p _ {t} ^ {i} - p _ {t} ^ {j}\right) \left(1 - S _ {t} ^ {j}\right) S _ {t} ^ {j}
$$

In any case, the market share is constrained by $0 \leq S \leq 1$ .

Each supplier will then attempt to set its prices in each period to maximize the net present value of its profits $\Pi_{1}^{i}$ and $\Pi_{1}^{j}$ , respectively, over the time horizon as below

$$
\Pi_ {1} ^ {i} = \sum_ {t = 1} ^ {T} \left(\beta^ {t - 1} S _ {t} ^ {i} \pi_ {t} ^ {i}\right)
$$

$$
\Pi_ {1} ^ {j} = \sum_ {t = 1} ^ {T} \left(\beta^ {t - 1} S _ {t} ^ {j} \pi_ {t} ^ {j}\right)
$$

where discount rate $\beta=1/(1+r)$ , r=discount rate. It can be seen from two logistic adjustment equations that when the initial market share and adjustment rate $\lambda$ have been predetermined by the market structure, market share in the following period is a function of prices of previous periods alone. Hence, the above profit equation can be written as

$$
\Pi_ {1} ^ {i} = f \big (p _ {1} ^ {i},..., p _ {T - 1} ^ {i}, p _ {T} ^ {i}, p _ {1} ^ {j},..., p _ {T - 1} ^ {j}, p _ {T} ^ {j} \big)
$$

$$
\Pi_ {1} ^ {j} = g \big (p _ {1} ^ {i},..., p _ {T - 1} ^ {i}, p _ {T} ^ {i}, p _ {1} ^ {j},..., p _ {T - 1} ^ {j}, p _ {T} ^ {j} \big)
$$

A Nash equilibrium $[(p_{1}^{i})^{*},\ldots,(p_{T}^{i})^{*},(p_{1}^{j})^{*},\ldots(p_{T}^{j})^{*}]$ exists if the follow inequalities are satisfied for all pricing alternatives $(p_{1}^{i},\ldots,p_{T}^{i},p_{1}^{j},\ldots,p_{T}^{j})$

$$
f \left[ (p _ {1} ^ {i}) ^ {*}, \dots , (p _ {T} ^ {i}) ^ {*}, (p _ {1} ^ {j}) ^ {*}, \dots , (p _ {T} ^ {j}) ^ {*} \right] \geq
$$

$$
f \left[ p _ {1} ^ {i}, \dots , p _ {T} ^ {i}, (p _ {1} ^ {j}) ^ {*}, \dots , (p _ {T} ^ {j}) ^ {*} \right]
$$

$$
g \big [ (p _ {1} ^ {i}) ^ {*},..., (p _ {T} ^ {i}) ^ {*}, (p _ {1} ^ {j}) ^ {*},..., (p _ {T} ^ {j}) ^ {*} \big ] \geq
$$

$$
g \big [ (p _ {1} ^ {i}), \dots , (p _ {T} ^ {i}) ^ {*}, p _ {1} ^ {j}, \dots , p _ {T} ^ {j} \big ]
$$

In fact, it is extremely complicated to find a solution for such a non-zero sum non-cooperative game. To focus on the impact of initial market share on the choice of pricing mechanism, we will simplify the problem in the following sections. In Section 3, we will first form the entries of the bimatrix game.

## 3. Formation of bimatrix game

Taking a discretization in price $p^{i}$ and $p^{j}$ and choosing a set of specific prices arbitrarily, we have m alternatives for supplier P1 and n alternatives for supplier P2. Meanwhile, it can be observed from logistic adjustment mechanism that the market shares are determined at the beginning of each period by prices in the previous periods. Since in the end of the time horizon, the market share has been determined by prices in previous periods, the optimal price for this last period is the then highest available price. Therefore, we only need to consider the pricing mechanism over the first T-1 period which maximizing the present value of profit $(\Pi_{1}^{i},\Pi_{1}^{j})$ . With m and n alternatives for P1 and P2, respectively, we have $m^{T-1}$ and $n^{T-1}$ possible pricing mechanisms for P1 and P2, respectively.

Now consider the profit matrix $A=\{a_{ij}\}$ for supplier P1, which is of $n^{T-1}$ rows and $m^{T-1}$ columns. Entry $a_{ij}$ represents the net present value of profit of P1 when P1 adopts strategy i and P2 choosing strategy j, where $i\in(1,\ldots,m^{T-1})$ , $j\in(1,\ldots,n^{T-1})$ . $a_{ij}$ is then calculated using Eq. (1) after determining the corresponding set of market shares of P1 over T periods. Similarly, we obtain the profit matrix $B=\{b_{ij}\}$ for supplier P2. Then, we form a bimatrix game pair $(A,B)$ , with each pair of entries $(a_{ij},b_{ij})$ denoting the outcome of the game corresponding to a particular pair of decisions made by the suppliers.

## 4. Mixed strategy problem

In this case, both of P1 and P2 are trying to maximize their own profit by taking into the other's decision into account. A pair $\{y^{*},z^{*}\}$ is said to constitute a non-cooperative Nash equilibrium solution to $(A,B)$ in mixed strategies, if the following inequalities are satisfied for all $y\in Y$ and $z\in Z$

$$
y ^ {* \prime} A z ^ {*} \leq y ^ {\prime} A z ^ {*}, \text {   for   } y \in Y
$$

$$
y ^ {* \prime} B z ^ {*} \leq y ^ {\prime} B z, \text {   for   } z \in Z
$$

where y and z are the probability distribution vectors defined by

$$
\begin{array}{l} y = (y _ {1}, \dots , y _ {m}) ^ {\prime} \\ z = (z _ {1}, \dots , z _ {n}) ^ {\prime} \end{array}
$$

and the pair $[J_{1}(y,z),J_{2}(y,z)]=(y^{*}Az^{*},y^{*}Bz^{*})$ is called a non-cooperative Nash equilibrium outcome of the bimatrix game in mixed strategies.

Then, the problem is converted to that both suppliers P1 and P2 wish to maximize their outcome $J_{1}(y,z)$ and $J_{2}(y,z)$ by an appropriate choice of a probability distribution vector $y\in Y$ , $z\in Z$ , where the sets Y and Z are, respectively, the m- and n-dimensional simplexes, i.e.,

$$
Y = \left\{y \in R ^ {m} \colon y \geq 0, \sum_ {i = 1} ^ {m} y _ {i} = 1 \right\}
$$

$$
Z = \left\{z \in R ^ {n} \colon z \geq 0, \sum_ {j = 1} ^ {n} z _ {j} = 1 \right\}
$$

According to theoretic-game theory [1], a pair $\{y^{*},z^{*}\}$ constitutes a mixed-strategy Nash equilibrium solution to the bimatrix game $(A,B)$ with the objective of minimizing the cost, if and only if, there exists a pair $(p^{*},q^{*})$ such that $\{y^{*},z^{*},p^{*},q^{*}\}$ is a solution of the following bilinear programming problem:

$$
\min _ {y, z, p, q} \left[ y ^ {\prime} A z + y ^ {\prime} B z + p + q \right]
$$

subject to the inequality constraints

$$
A z \geq - p 1 _ {m}
$$

$$
B ^ {\prime} y \geq - q 1 _ {n}
$$

$$
0 \leq y \leq 1
$$

$$
0 \leq z \leq 1
$$

and equality constraints

$$
y ^ {\prime} 1 _ {m} = 1
$$

$$
z ^ {\prime} 1 _ {n} = 1
$$

where

$$
1 _ {m} = (1, \dots , 1) ^ {\prime} \in R ^ {m}
$$

$$
1 _ {n} = (1,..., 1) ^ {\prime} \in R ^ {n}
$$

In our case where the objective is to maximize the profit, the problem is converted to minimize the negative value of the profit. Denote the known profit bimatrix by $(P_{1}, P_{2})$ , the objective function to be minimized is then

$$
J (y, z, p, q) = \min _ {y, z, p, q} \left[ - y ^ {\prime} P _ {1} z - y ^ {\prime} P _ {2} z + p + q \right]
$$

Let vector $X$ be

$$
\begin{array}{c} X = (x _ {1}, x _ {2}, x _ {3}, x _ {4}, x _ {5}, x _ {6}, x _ {7}, x _ {8}, x _ {9}, x _ {1 0}) ^ {\prime} \\ = (y _ {1}, y _ {2}, y _ {3}, y _ {4}, z _ {1}, z _ {2}, z _ {3}, z _ {4}, p, q) ^ {\prime} \end{array}
$$

such that our problem can be rewritten as:

$$
\begin{array}{r l} J (X) = & \min _ {X} [ - (x _ {1}, x _ {2}, x _ {3}, x _ {4}) P _ {1} (x _ {5}, x _ {6}, x _ {7}, x _ {8}) ^ {\prime} \\ & - (x _ {1}, x _ {2}, x _ {3}, x _ {4}) P _ {2} (x _ {5}, x _ {6}, x _ {7}, x _ {8}) ^ {\prime} + x _ {9} + x _ {1 0} ] \end{array}
$$

subject to inequality constraints

$$
0 \leq x _ {i} \leq 1, \quad \text { for } i = 1,..., 8
$$

$$
- P _ {1} (x _ {5}, x _ {6}, x _ {7}, x _ {8}) ^ {\prime} \leq x _ {9} \cdot 1 _ {m}
$$

$$
- P _ {2} ^ {\prime} (x _ {1}, x _ {2}, x _ {3}, x _ {4}) ^ {\prime} \leq x _ {1 0} \cdot 1 _ {n}
$$

and equality constraints

$$
\sum_ {i = 1} ^ {4} x _ {i} = 1
$$

$$
\sum_ {i = 5} ^ {8} x _ {i} = 1
$$

## 5. Numerical solutions to the mixed strategy game

Here, we first consider a three period time horizon with two suppliers. Supplier P1 is always trying to enter the market with a lower price compared to the incumbent supplier P2. Considering the fact that marginal cost/benefit is typically between US\$10 and US\$35/MWh, we treat these two prices as the perfect competitive price and monopoly price, respectively. Besides, we set the other two pricing alternatives to be US\$15.00 and US\$20.00/MW h. Thus, for each supplier, there are four alternatives to choose, that is, (10, 15, 20, 35). Refer to Section 3, we are going to have a pair of 16 by 16 profit matrices for supplier P1 and P2. In the following tables, the upper value of each entry is the profit of P1 and the lower value is the profit of P2.

Numerical examples are provided for three different market structures with different initial market share for both suppliers. Suppose $S_{1}^{1}=0.1$ , 0.3, 0.5, which corresponds to $S_{1}^{2}=0.9$ , 0.7, 0.5. Also suppose the discount factor is $\beta=0.971$ and the adjustment parameter $\lambda=2$ .

Table 1
Profit matrix when $S_{1}^{1}=0.1$

Case 1 ( $S_{1}^{1}=0.1$ ). As it can be seen from Table 1, there is a unique solution of the mixed strategy game when initial market share $S_{1}^{1}=0.1$ , that is, the probability distribution vectors are

$$
y = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
$$

$$
z = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
$$

which means that P1 would choose pricing strategy (0.4, 0.4, 1.0) deterministically, while P2 would choose strategy (1.0, 1.0, 1.0). In terms of unnormalized prices, the strategies adopted by P1 and P2 are (20, 20, 35) and (35, 35, 35), respectively. Given the pricing strategies, the market shares of P1 increase as (0.100, 0.208,

<table><tr><td rowspan="3"></td><td colspan="17">P2&#x27;s price strategies and profits</td></tr><tr><td>P1</td><td>0, 0</td><td>0, 0.2</td><td>0, 0.4</td><td>0, 1</td><td>0.2, 0</td><td>0.2, 0.2</td><td>0.2, 0.4</td><td>0.2, 1</td><td>0.4, 0</td><td>0.4, 0.2</td><td>0.4, 0.4</td><td>0.4, 1</td><td>1, 0</td><td>1, 0.2</td><td>1, 0.4</td><td>1, 1</td></tr><tr><td>P2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="32">P1&#x27;s</td><td>0, 0</td><td>-0.11</td><td>-0.11</td><td>-0.11</td><td>-0.10</td><td>-0.13</td><td>-0.13</td><td>-0.12</td><td>-0.11</td><td>-0.15</td><td>-0.15</td><td>-0.14</td><td>-0.13</td><td>-0.21</td><td>-0.20</td><td>-0.19</td><td>-0.17</td></tr><tr><td></td><td>-1.02</td><td>-0.69</td><td>-0.47</td><td>-0.42</td><td>-0.66</td><td>-0.34</td><td>-0.13</td><td>-0.09</td><td>-0.41</td><td>-0.10</td><td>0.10</td><td>0.13</td><td>-0.30</td><td>-0.04</td><td>0.14</td><td>0.16</td></tr><tr><td>0,</td><td>-0.08</td><td>-0.08</td><td>-0.07</td><td>-0.06</td><td>-0.09</td><td>-0.08</td><td>-0.08</td><td>-0.07</td><td>-0.09</td><td>-0.09</td><td>-0.08</td><td>-0.07</td><td>-0.11</td><td>-0.10</td><td>-0.10</td><td>-0.08</td></tr><tr><td>0.2</td><td>-1.02</td><td>-0.69</td><td>-0.46</td><td>-0.42</td><td>-0.65</td><td>-0.34</td><td>-0.13</td><td>-0.09</td><td>-0.40</td><td>-0.10</td><td>0.10</td><td>0.14</td><td>-0.29</td><td>-0.03</td><td>0.15</td><td>0.17</td></tr><tr><td>0,</td><td>-0.06</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.03</td><td>-0.05</td><td>-0.04</td><td>-0.03</td><td>-0.01</td></tr><tr><td>0.4</td><td>-1.01</td><td>-0.68</td><td>-0.46</td><td>-0.42</td><td>-0.65</td><td>-0.34</td><td>-0.12</td><td>-0.08</td><td>-0.40</td><td>-0.10</td><td>0.11</td><td>0.14</td><td>-0.28</td><td>-0.02</td><td>0.15</td><td>0.17</td></tr><tr><td>0, 1</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.03</td><td>-0.04</td><td>-0.04</td><td>-0.04</td><td>-0.02</td></tr><tr><td></td><td>-1.01</td><td>-0.68</td><td>-0.45</td><td>-0.41</td><td>-0.65</td><td>-0.33</td><td>-0.11</td><td>-0.07</td><td>-0.39</td><td>-0.09</td><td>0.12</td><td>0.16</td><td>-0.27</td><td>-0.01</td><td>0.17</td><td>0.19</td></tr><tr><td>0.2,</td><td>-0.06</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.08</td><td>-0.07</td><td>-0.07</td><td>-0.06</td><td>-0.09</td><td>-0.09</td><td>-0.09</td><td>-0.07</td><td>-0.15</td><td>-0.14</td><td>-0.14</td><td>-0.12</td></tr><tr><td>0</td><td>-1.04</td><td>-0.69</td><td>-0.46</td><td>-0.41</td><td>-0.68</td><td>-0.35</td><td>-0.12</td><td>-0.08</td><td>-0.42</td><td>-0.11</td><td>0.11</td><td>0.14</td><td>-0.31</td><td>-0.04</td><td>0.14</td><td>0.17</td></tr><tr><td>0.2,</td><td>-0.03</td><td>-0.03</td><td>-0.03</td><td>-0.03</td><td>-0.04</td><td>-0.04</td><td>-0.04</td><td>-0.03</td><td>-0.05</td><td>-0.04</td><td>-0.04</td><td>-0.03</td><td>-0.07</td><td>-0.06</td><td>-0.05</td><td>-0.04</td></tr><tr><td>0.2</td><td>-1.04</td><td>-0.69</td><td>-0.46</td><td>-0.41</td><td>-0.67</td><td>-0.34</td><td>-0.12</td><td>-0.08</td><td>-0.42</td><td>-0.11</td><td>0.11</td><td>0.15</td><td>-0.31</td><td>-0.04</td><td>0.15</td><td>0.18</td></tr><tr><td>0.2,</td><td>-0.02</td><td>-0.02</td><td>-0.02</td><td>-0.01</td><td>-0.02</td><td>-0.02</td><td>-0.01</td><td>0.0</td><td>-0.02</td><td>-0.01</td><td>-0.01</td><td>0.0</td><td>-0.01</td><td>0.0</td><td>0.0</td><td>0.02</td></tr><tr><td>0.4</td><td>-1.03</td><td>-0.69</td><td>-0.46</td><td>-0.41</td><td>-0.67</td><td>-0.34</td><td>-0.12</td><td>-0.07</td><td>-0.42</td><td>-0.10</td><td>0.11</td><td>0.15</td><td>-0.30</td><td>-0.03</td><td>0.16</td><td>0.18</td></tr><tr><td>0.2,</td><td>-0.02</td><td>-0.02</td><td>-0.02</td><td>-0.01</td><td>-0.02</td><td>-0.02</td><td>-0.02</td><td>-0.01</td><td>-0.01</td><td>-0.01</td><td>-0.01</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.02</td></tr><tr><td>1</td><td>-1.03</td><td>-0.69</td><td>-0.45</td><td>-0.40</td><td>-0.67</td><td>-0.34</td><td>-0.11</td><td>-0.07</td><td>-0.41</td><td>-0.09</td><td>0.12</td><td>0.16</td><td>-0.29</td><td>-0.02</td><td>0.17</td><td>0.20</td></tr><tr><td>0.4,</td><td>-0.01</td><td>-0.01</td><td>-0.01</td><td>-0.01</td><td>-0.03</td><td>-0.03</td><td>-0.03</td><td>-0.02</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.03</td><td>-0.11</td><td>-0.10</td><td>-0.09</td><td>-0.08</td></tr><tr><td>0</td><td>-1.06</td><td>-0.70</td><td>-0.45</td><td>-0.40</td><td>-0.70</td><td>-0.35</td><td>-0.12</td><td>-0.07</td><td>-0.44</td><td>-0.11</td><td>0.11</td><td>0.15</td><td>-0.33</td><td>-0.05</td><td>0.15</td><td>0.18</td></tr><tr><td>0.4,</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>-0.01</td><td>-0.01</td><td>-0.01</td><td>0.0</td><td>-0.02</td><td>-0.01</td><td>-0.01</td><td>0.0</td><td>-0.03</td><td>-0.03</td><td>-0.02</td><td>-0.01</td></tr><tr><td>0.2</td><td>-1.06</td><td>-0.70</td><td>-0.45</td><td>-0.40</td><td>-0.69</td><td>-0.35</td><td>-0.12</td><td>-0.07</td><td>-0.44</td><td>-0.11</td><td>0.11</td><td>0.16</td><td>-0.33</td><td>-0.04</td><td>0.15</td><td>0.18</td></tr><tr><td>0.4,</td><td>0.0</td><td>0.0</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.04</td></tr><tr><td>0.4</td><td>-1.05</td><td>-0.70</td><td>-0.45</td><td>-0.40</td><td>-0.69</td><td>-0.35</td><td>-0.11</td><td>-0.06</td><td>-0.44</td><td>-0.11</td><td>0.12</td><td>0.16</td><td>-0.32</td><td>-0.04</td><td>0.16</td><td>0.19</td></tr><tr><td>0.4,</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.04</td></tr><tr><td>1</td><td>-1.05</td><td>-0.70</td><td>-0.45</td><td>-0.40</td><td>-0.69</td><td>-0.34</td><td>-0.11</td><td>-0.06</td><td>-0.43</td><td>-0.10</td><td>0.12</td><td>0.17</td><td>-0.32</td><td>-0.02</td><td>0.18</td><td>0.21</td></tr><tr><td>1, 0</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.04</td><td>-0.04</td><td>-0.04</td><td>-0.03</td></tr><tr><td></td><td>-1.07</td><td>-0.70</td><td>-0.45</td><td>-0.39</td><td>-0.73</td><td>-0.36</td><td>-0.11</td><td>-0.05</td><td>-0.49</td><td>-0.13</td><td>0.13</td><td>0.19</td><td>-0.39</td><td>-0.06</td><td>0.16</td><td>0.21</td></tr><tr><td>1,</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>-0.01</td><td>-0.01</td><td>0.0</td><td>0.01</td></tr><tr><td>0.2</td><td>-1.07</td><td>-0.70</td><td>-0.45</td><td>-0.39</td><td>-0.73</td><td>-0.36</td><td>-0.11</td><td>-0.05</td><td>-0.49</td><td>-0.13</td><td>0.13</td><td>0.19</td><td>-0.39</td><td>-0.06</td><td>0.17</td><td>0.21</td></tr><tr><td>1,</td><td>0.001</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.03</td></tr><tr><td>0.4</td><td>-1.07</td><td>-0.70</td><td>-0.45</td><td>-0.39</td><td>-0.73</td><td>-0.36</td><td>-0.11</td><td>-0.05</td><td>-0.49</td><td>-0.13</td><td>0.13</td><td>0.19</td><td>-0.38</td><td>-0.05</td><td>0.17</td><td>0.21</td></tr><tr><td>1, 1</td><td>0.001</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td></tr><tr><td></td><td>-1.07</td><td>-0.70</td><td>-0.45</td><td>-0.39</td><td>-0.73</td><td>-0.36</td><td>-0.11</td><td>-0.05</td><td>-0.49</td><td>-0.13</td><td>0.13</td><td>0.19</td><td>-0.38</td><td>-0.05</td><td>0.18</td><td>0.22</td></tr></table>

Remark: bold entry denotes pure Nash equilibrium.

0.406) and P2's market shares decrease as (0.900, 0.792, 0.594), and net present value of profit of P1 is 0.04 and the one for P2 is 0.19. Suppose the energy is sold at 100K per unit per dollar, the profit 0.04 stands for 0.04×US\$(35-10)×100,000=US\$100,000.

This result makes sense since when P1 enters the market with a low initial market share, P1 would like to win more market share at the expense of lower price. When P1 has won enough market shares over the first period, it would increase its price for more profit. At the same time, the incumbent supplier P2 is nearly monopolistic in the initial stage. Due to a certain adjustment parameter of market, it is not possible for P2 to lose most of its market shares immediately no matter how low the price offered by P1 is. With dominantly large market shares at the beginning, P2 would stick to the higher price for more profit over the first two periods even though it will loss some market shares to P1. Different from the result in Refs. [2-4], even the new entrant is not going to choose perfectly competitive price at the very beginning.

Case 2 ( $S_{1}^{1}=0.3$ ). For the second case where the initial market share for supplier P1 is 0.3, it can be observed that there are two pure Nash equilibria, that is,

$$
y _ {1} = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
$$

$$
z _ {1} = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
$$

Table 2  
Profit matrix when $S_{1}^{1}=0.3$

<table><tr><td rowspan="2"></td><td colspan="17">P2&#x27;s price strategies and profits</td></tr><tr><td>P1</td><td>0, 0</td><td>0, 0.2</td><td>0, 0.4</td><td>0, 1</td><td>0.2, 0</td><td>0.2, 0.2</td><td>0.2, 0.4</td><td>0.2, 1</td><td>0.4, 0</td><td>0.4, 0.2</td><td>0.4, 0.4</td><td>0.4, 1</td><td>1, 0</td><td>1, 0.2</td><td>1, 0.4</td><td>1, 1</td></tr><tr><td rowspan="32">P1&#x27;s</td><td rowspan="2">0, 0</td><td>-0.34</td><td>-0.33</td><td>-0.33</td><td>-0.31</td><td>-0.38</td><td>-0.38</td><td>-0.37</td><td>-0.35</td><td>-0.43</td><td>-0.42</td><td>-0.41</td><td>-0.39</td><td>-0.56</td><td>-0.55</td><td>-0.54</td><td>-0.53</td></tr><tr><td>-0.79</td><td>-0.54</td><td>-0.37</td><td>-0.35</td><td>-0.48</td><td>-0.26</td><td>-0.12</td><td>-0.10</td><td>-0.26</td><td>-0.07</td><td>-0.06</td><td>-0.06</td><td>-0.09</td><td>0.01</td><td>0.08</td><td>0.08</td></tr><tr><td>0,</td><td>-0.24</td><td>-0.23</td><td>-0.22</td><td>-0.20</td><td>-0.25</td><td>-0.24</td><td>-0.23</td><td>-0.21</td><td>-0.26</td><td>-0.25</td><td>-0.25</td><td>-0.22</td><td>-0.30</td><td>-0.29</td><td>-0.28</td><td>-0.27</td></tr><tr><td>0.2</td><td>-0.79</td><td>-0.53</td><td>-0.36</td><td>-0.34</td><td>-0.48</td><td>-0.26</td><td>-0.11</td><td>-0.09</td><td>-0.25</td><td>-0.06</td><td>0.07</td><td>0.07</td><td>-0.08</td><td>0.02</td><td>0.08</td><td>0.08</td></tr><tr><td>0,</td><td>-0.17</td><td>-0.16</td><td>-0.15</td><td>-0.13</td><td>-0.16</td><td>-0.15</td><td>-0.14</td><td>-0.12</td><td>-0.15</td><td>-0.14</td><td>-0.14</td><td>-0.11</td><td>-0.12</td><td>-0.12</td><td>-0.11</td><td>-0.09</td></tr><tr><td>0.4</td><td>-0.78</td><td>-0.53</td><td>-0.36</td><td>-0.34</td><td>-0.47</td><td>-0.25</td><td>-0.10</td><td>-0.09</td><td>-0.24</td><td>-0.05</td><td>0.07</td><td>0.08</td><td>-0.07</td><td>0.02</td><td>0.09</td><td>0.09</td></tr><tr><td rowspan="2">0, 1</td><td>-0.16</td><td>-0.16</td><td>-0.16</td><td>-0.14</td><td>-0.15</td><td>-0.15</td><td>-0.14</td><td>-0.12</td><td>-0.15</td><td>-0.14</td><td>-0.13</td><td>-0.11</td><td>-0.10</td><td>-0.09</td><td>-0.09</td><td>-0.07</td></tr><tr><td>-0.77</td><td>-0.51</td><td>-0.34</td><td>-0.32</td><td>-0.45</td><td>-0.23</td><td>-0.08</td><td>-0.06</td><td>-0.22</td><td>-0.03</td><td>0.10</td><td>0.10</td><td>-0.05</td><td>0.04</td><td>0.11</td><td>0.11</td></tr><tr><td>0.2,</td><td>-0.18</td><td>-0.18</td><td>-0.17</td><td>-0.16</td><td>-0.23</td><td>-0.22</td><td>-0.21</td><td>-0.19</td><td>-0.27</td><td>-0.26</td><td>-0.25</td><td>-0.23</td><td>-0.40</td><td>-0.39</td><td>-0.38</td><td>-0.37</td></tr><tr><td>0</td><td>-0.84</td><td>-0.55</td><td>-0.36</td><td>-0.33</td><td>-0.53</td><td>-0.27</td><td>-0.10</td><td>-0.08</td><td>-0.30</td><td>-0.08</td><td>0.07</td><td>0.08</td><td>-0.13</td><td>0.0</td><td>0.08</td><td>0.09</td></tr><tr><td>0.2,</td><td>-0.11</td><td>-0.10</td><td>-0.10</td><td>-0.08</td><td>-0.12</td><td>-0.11</td><td>-0.11</td><td>-0.09</td><td>-0.13</td><td>-0.13</td><td>-0.12</td><td>-0.10</td><td>-0.17</td><td>-0.16</td><td>-0.16</td><td>-0.14</td></tr><tr><td>0.2</td><td>-0.83</td><td>-0.55</td><td>-0.35</td><td>-0.32</td><td>-0.52</td><td>-0.27</td><td>-0.10</td><td>-0.08</td><td>-0.29</td><td>-0.07</td><td>0.07</td><td>0.09</td><td>-0.12</td><td>0.01</td><td>0.09</td><td>0.09</td></tr><tr><td>0.2,</td><td>-0.06</td><td>-0.05</td><td>-0.05</td><td>-0.03</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.02</td><td>-0.05</td><td>-0.04</td><td>-0.03</td><td>-0.01</td><td>0.02</td><td>-0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>0.4</td><td>-0.82</td><td>-0.54</td><td>-0.35</td><td>-0.32</td><td>-0.51</td><td>-0.26</td><td>-0.09</td><td>-0.07</td><td>-0.29</td><td>-0.07</td><td>0.08</td><td>0.09</td><td>-0.11</td><td>0.01</td><td>0.10</td><td>0.10</td></tr><tr><td>0.2,</td><td>-0.05</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.02</td><td>-0.04</td><td>-0.04</td><td>-0.03</td><td>-0.01</td><td>0.0</td><td>0.0</td><td>0.01</td><td>0.03</td></tr><tr><td>1</td><td>-0.82</td><td>-0.53</td><td>-0.33</td><td>-0.30</td><td>-0.50</td><td>-0.24</td><td>-0.07</td><td>-0.05</td><td>-0.27</td><td>-0.04</td><td>0.10</td><td>0.12</td><td>-0.09</td><td>0.04</td><td>0.12</td><td>0.12</td></tr><tr><td>0.4,</td><td>-0.06</td><td>-0.06</td><td>-0.05</td><td>-0.04</td><td>-0.10</td><td>-0.10</td><td>-0.09</td><td>-0.08</td><td>-0.15</td><td>-0.14</td><td>-0.13</td><td>-0.11</td><td>-0.28</td><td>-0.27</td><td>-0.26</td><td>-0.24</td></tr><tr><td>0</td><td>-0.88</td><td>-0.56</td><td>-0.35</td><td>-0.31</td><td>-0.57</td><td>-0.29</td><td>-0.09</td><td>-0.06</td><td>-0.34</td><td>-0.09</td><td>0.08</td><td>0.10</td><td>-0.17</td><td>-0.01</td><td>0.09</td><td>0.10</td></tr><tr><td>0.4,</td><td>-0.02</td><td>-0.01</td><td>-0.01</td><td>0.0</td><td>-0.03</td><td>-0.02</td><td>-0.02</td><td>0.0</td><td>-0.04</td><td>-0.04</td><td>-0.03</td><td>-0.01</td><td>-0.08</td><td>-0.07</td><td>-0.07</td><td>-0.04</td></tr><tr><td>0.2</td><td>-0.88</td><td>-0.56</td><td>-0.34</td><td>-0.30</td><td>-0.56</td><td>-0.28</td><td>-0.09</td><td>-0.06</td><td>-0.34</td><td>-0.09</td><td>0.08</td><td>0.10</td><td>-0.16</td><td>-0.01</td><td>0.10</td><td>0.10</td></tr><tr><td>0.4,</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.03</td><td>0.02</td><td>0.02</td><td>0.03</td><td>0.05</td><td>0.03</td><td>0.03</td><td>0.04</td><td>0.06</td><td>0.05</td><td>0.06</td><td>0.07</td><td>0.09</td></tr><tr><td>0.4</td><td>-0.87</td><td>-0.56</td><td>-0.34</td><td>-0.30</td><td>-0.56</td><td>-0.28</td><td>-0.08</td><td>-0.05</td><td>-0.33</td><td>-0.08</td><td>0.09</td><td>0.11</td><td>-0.16</td><td>0.0</td><td>0.11</td><td>0.11</td></tr><tr><td>0.4,</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.04</td><td>0.03</td><td>0.03</td><td>0.04</td><td>0.06</td><td>0.06</td><td>0.07</td><td>0.07</td><td>0.10</td></tr><tr><td>1</td><td>-0.87</td><td>-0.55</td><td>-0.33</td><td>-0.29</td><td>-0.55</td><td>-0.26</td><td>-0.07</td><td>-0.04</td><td>-0.32</td><td>-0.06</td><td>0.11</td><td>0.13</td><td>-0.13</td><td>0.02</td><td>0.13</td><td>0.13</td></tr><tr><td rowspan="2">1, 0</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.01</td><td>-0.13</td><td>-0.12</td><td>-0.12</td><td>0.10</td></tr><tr><td>-0.95</td><td>-0.58</td><td>-0.33</td><td>-0.27</td><td>-0.68</td><td>-0.31</td><td>-0.06</td><td>0.0</td><td>-0.47</td><td>-0.12</td><td>0.11</td><td>0.17</td><td>-0.30</td><td>-0.05</td><td>0.12</td><td>0.14</td></tr><tr><td>1,</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>-0.03</td><td>-0.02</td><td>-0.01</td><td>0.01</td></tr><tr><td>0.2</td><td>-0.95</td><td>-0.58</td><td>-0.33</td><td>-0.27</td><td>-0.68</td><td>-0.31</td><td>-0.06</td><td>0.0</td><td>-0.47</td><td>-0.12</td><td>0.12</td><td>0.17</td><td>-0.30</td><td>-0.04</td><td>0.13</td><td>0.15</td></tr><tr><td>1,</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.06</td><td>0.08</td></tr><tr><td>0.4</td><td>-0.95</td><td>-0.58</td><td>-0.33</td><td>-0.27</td><td>-0.68</td><td>-0.31</td><td>-0.06</td><td>0.0</td><td>-0.47</td><td>-0.12</td><td>0.12</td><td>0.17</td><td>-0.29</td><td>-0.04</td><td>0.13</td><td>0.15</td></tr><tr><td rowspan="2">1, 1</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.07</td></tr><tr><td>-0.95</td><td>-0.58</td><td>-0.33</td><td>-0.27</td><td>-0.68</td><td>-0.31</td><td>-0.06</td><td>0.0</td><td>-0.47</td><td>-0.12</td><td>0.12</td><td>0.17</td><td>-0.28</td><td>-0.02</td><td>0.15</td><td>0.17</td></tr></table>

and

$$
y _ {2} = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
$$

$$
z _ {2} = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
$$

Correspondingly, the profit pairs are (0.0590, 0.1112) and (0.0973, 0.1324), which are bold in Table 2.

If players were to select strategies $(y_{1},z_{1})$ , which are actual prices (20, 20, 35) for P1 and (20, 35, 35) for P2, the market shares vary as (0.30, 0.30, 0.552) and (0.70, 0.70, 0.448), respectively. This implies that the incumbent supplier P2 is now adopting a lower price over the first period, then a higher price over the second period, since the new entrant P1 is now with a larger initial market shares while offering a lower price. To keep its current market shares as well as the profit, it makes sense for P2 to decrease its price in the first period. Meanwhile, for P1, it has to keep setting a lower price in the second period to gain enough market share in the following periods.

If players were to select strategies $(y_{2}, z_{2})$ , which are actual prices (20, 35, 35) for P1 and (35, 35, 35) for P2, the market shares change as (0.30, 0.552, 0.552) and (0.70, 0.448, 0.448), respectively. When P2 sticks its price at monopoly level all the time, it is possible for P1 to gain enough market shares only in the first period by providing a lower price. After that, P1 would like to use monopoly price too to obtain more profit.

Table 3
Profit matrix when $S_{1}^{1}=0.5$

<table><tr><td rowspan="2"></td><td colspan="17">P2&#x27;s price strategies and profits</td></tr><tr><td>P1</td><td>0, 0</td><td>0, 0.2</td><td>0, 0.4</td><td>0, 1</td><td>0.2, 0</td><td>0.2, 0.2</td><td>0.2, 0.4</td><td>0.2, 1</td><td>0.4, 0</td><td>0.4, 0.2</td><td>0.4, 0.4</td><td>0.4, 1</td><td>1, 0</td><td>1, 0.2</td><td>1, 0.4</td><td>1, 1</td></tr><tr><td rowspan="32">P1&#x27;s</td><td rowspan="2">0, 0</td><td>-0.57</td><td>-0.56</td><td>-0.55</td><td>-0.53</td><td>-0.63</td><td>-0.61</td><td>-0.60</td><td>-0.59</td><td>-0.67</td><td>-0.66</td><td>-0.66</td><td>-0.65</td><td>-0.82</td><td>-0.82</td><td>-0.82</td><td>-0.82</td></tr><tr><td>-0.57</td><td>-0.39</td><td>-0.27</td><td>-0.27</td><td>-0.32</td><td>-0.18</td><td>-0.09</td><td>-0.08</td><td>-0.14</td><td>-0.04</td><td>0.03</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td></tr><tr><td>0,</td><td>-0.39</td><td>-0.38</td><td>-0.37</td><td>-0.35</td><td>-0.40</td><td>-0.40</td><td>-0.39</td><td>-0.37</td><td>-0.42</td><td>-0.41</td><td>-0.40</td><td>-0.39</td><td>-0.46</td><td>-0.46</td><td>-0.46</td><td>-0.46</td></tr><tr><td>0.2</td><td>-0.56</td><td>-0.38</td><td>-0.26</td><td>-0.26</td><td>-0.32</td><td>-0.18</td><td>-0.08</td><td>-0.08</td><td>-0.14</td><td>-0.03</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td></tr><tr><td>0,</td><td>-0.27</td><td>-0.26</td><td>-0.26</td><td>-0.23</td><td>-0.26</td><td>-0.25</td><td>-0.24</td><td>-0.22</td><td>-0.25</td><td>-0.24</td><td>-0.23</td><td>-0.21</td><td>-0.20</td><td>-0.20</td><td>-0.20</td><td>-0.20</td></tr><tr><td>0.4</td><td>-0.55</td><td>-0.37</td><td>-0.26</td><td>-0.25</td><td>-0.31</td><td>-0.17</td><td>-0.08</td><td>-0.08</td><td>-0.13</td><td>-0.03</td><td>0.04</td><td>0.04</td><td>-0.04</td><td>0.04</td><td>0.04</td><td>0.04</td></tr><tr><td rowspan="2">0, 1</td><td>-0.27</td><td>-0.26</td><td>-0.25</td><td>-0.23</td><td>-0.25</td><td>-0.24</td><td>-0.23</td><td>-0.21</td><td>-0.23</td><td>-0.22</td><td>-0.21</td><td>-0.19</td><td>-0.14</td><td>-0.14</td><td>-0.14</td><td>-0.14</td></tr><tr><td>-0.53</td><td>-0.35</td><td>-0.23</td><td>-0.23</td><td>-0.29</td><td>-0.15</td><td>-0.05</td><td>-0.05</td><td>-0.11</td><td>0.0</td><td>0.06</td><td>0.06</td><td>-0.04</td><td>0.04</td><td>0.04</td><td>0.04</td></tr><tr><td>0.2,</td><td>-0.32</td><td>-0.32</td><td>-0.31</td><td>-0.29</td><td>-0.38</td><td>-0.37</td><td>-0.36</td><td>-0.34</td><td>-0.43</td><td>-0.42</td><td>-0.41</td><td>-0.40</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td>-0.57</td></tr><tr><td>0</td><td>-0.62</td><td>-0.40</td><td>-0.26</td><td>-0.25</td><td>-0.38</td><td>-0.20</td><td>-0.08</td><td>-0.08</td><td>-0.19</td><td>-0.05</td><td>0.04</td><td>0.05</td><td>-0.01</td><td>0.02</td><td>0.05</td><td>0.05</td></tr><tr><td>0.2,</td><td>-0.18</td><td>-0.18</td><td>-0.17</td><td>-0.15</td><td>-0.20</td><td>-0.19</td><td>-0.18</td><td>-0.16</td><td>-0.21</td><td>-0.21</td><td>-0.20</td><td>-0.18</td><td>-0.25</td><td>-0.25</td><td>-0.25</td><td>-0.24</td></tr><tr><td>0.2</td><td>-0.61</td><td>-0.40</td><td>-0.25</td><td>-0.24</td><td>-0.37</td><td>-0.19</td><td>-0.07</td><td>-0.07</td><td>-0.19</td><td>-0.05</td><td>0.05</td><td>0.05</td><td>-0.01</td><td>0.03</td><td>0.05</td><td>0.05</td></tr><tr><td>0.2,</td><td>-0.09</td><td>-0.08</td><td>-0.08</td><td>-0.05</td><td>-0.08</td><td>-0.07</td><td>-0.07</td><td>-0.04</td><td>-0.07</td><td>-0.06</td><td>-0.05</td><td>-0.03</td><td>-0.03</td><td>-0.03</td><td>-0.02</td><td>-0.02</td></tr><tr><td>0.4</td><td>-0.60</td><td>-0.39</td><td>-0.24</td><td>-0.23</td><td>-0.36</td><td>-0.18</td><td>-0.07</td><td>-0.06</td><td>-0.18</td><td>-0.04</td><td>0.05</td><td>0.05</td><td>0.0</td><td>0.03</td><td>0.05</td><td>0.05</td></tr><tr><td>0.2,</td><td>-0.08</td><td>-0.08</td><td>-0.08</td><td>-0.05</td><td>-0.08</td><td>-0.07</td><td>-0.06</td><td>-0.04</td><td>-0.06</td><td>-0.05</td><td>-0.04</td><td>-0.02</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.03</td></tr><tr><td>1</td><td>-0.59</td><td>-0.37</td><td>-0.22</td><td>-0.21</td><td>-0.34</td><td>-0.16</td><td>-0.04</td><td>-0.04</td><td>-0.16</td><td>-0.02</td><td>0.08</td><td>0.08</td><td>0.01</td><td>0.04</td><td>0.06</td><td>0.06</td></tr><tr><td>0.4,</td><td>-0.14</td><td>-0.14</td><td>-0.13</td><td>-0.11</td><td>-0.19</td><td>-0.19</td><td>-0.18</td><td>-0.16</td><td>-0.25</td><td>-0.24</td><td>-0.23</td><td>-0.21</td><td>-0.40</td><td>-0.40</td><td>-0.39</td><td>-0.39</td></tr><tr><td>0</td><td>-0.67</td><td>-0.42</td><td>-0.25</td><td>-0.23</td><td>-0.43</td><td>-0.21</td><td>-0.07</td><td>-0.06</td><td>-0.25</td><td>-0.07</td><td>0.05</td><td>0.05</td><td>-0.06</td><td>0.01</td><td>0.05</td><td>0.06</td></tr><tr><td>0.4,</td><td>-0.04</td><td>-0.03</td><td>-0.03</td><td>0.0</td><td>-0.05</td><td>-0.05</td><td>-0.04</td><td>-0.02</td><td>-0.07</td><td>-0.06</td><td>-0.05</td><td>-0.03</td><td>-0.11</td><td>-0.11</td><td>-0.10</td><td>-0.09</td></tr><tr><td>0.2</td><td>-0.66</td><td>-0.41</td><td>-0.24</td><td>-0.22</td><td>-0.42</td><td>-0.21</td><td>-0.06</td><td>-0.05</td><td>-0.24</td><td>-0.06</td><td>0.06</td><td>0.06</td><td>-0.06</td><td>0.01</td><td>0.06</td><td>0.06</td></tr><tr><td>0.4,</td><td>0.03</td><td>0.04</td><td>0.04</td><td>0.06</td><td>0.04</td><td>0.05</td><td>0.05</td><td>0.08</td><td>0.05</td><td>0.06</td><td>0.06</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.10</td><td>0.11</td></tr><tr><td>0.4</td><td>-0.66</td><td>-0.40</td><td>-0.23</td><td>-0.21</td><td>-0.41</td><td>-0.20</td><td>-0.05</td><td>-0.04</td><td>-0.23</td><td>-0.05</td><td>0.06</td><td>0.07</td><td>-0.05</td><td>0.02</td><td>0.06</td><td>0.06</td></tr><tr><td>0.4,</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.06</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.08</td><td>0.05</td><td>0.06</td><td>0.07</td><td>0.09</td><td>0.12</td><td>0.12</td><td>0.13</td><td>0.14</td></tr><tr><td>1</td><td>-0.65</td><td>-0.39</td><td>-0.21</td><td>-0.19</td><td>-0.49</td><td>-0.18</td><td>-0.03</td><td>-0.02</td><td>-0.21</td><td>-0.30</td><td>0.09</td><td>0.09</td><td>-0.04</td><td>0.03</td><td>0.08</td><td>0.08</td></tr><tr><td rowspan="2">1, 0</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td><td>-0.01</td><td>-0.01</td><td>0.0</td><td>0.01</td><td>-0.06</td><td>-0.06</td><td>-0.05</td><td>-0.04</td><td>-0.22</td><td>-0.21</td><td>-0.20</td><td>-0.18</td></tr><tr><td>-0.82</td><td>-0.46</td><td>-0.20</td><td>-0.14</td><td>-0.58</td><td>-0.25</td><td>-0.03</td><td>0.01</td><td>-0.40</td><td>-0.11</td><td>0.09</td><td>0.12</td><td>-0.22</td><td>-0.04</td><td>0.08</td><td>0.08</td></tr><tr><td>1,</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.02</td><td>0.03</td><td>0.03</td><td>0.04</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.03</td><td>-0.04</td><td>-0.03</td><td>-0.02</td><td>0.09</td></tr><tr><td>0.2</td><td>-0.82</td><td>-0.46</td><td>-0.20</td><td>-0.14</td><td>-0.58</td><td>-0.25</td><td>-0.03</td><td>0.02</td><td>-0.40</td><td>-0.11</td><td>0.09</td><td>0.12</td><td>-0.21</td><td>-0.03</td><td>0.09</td><td>0.09</td></tr><tr><td>1,</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.06</td><td>0.05</td><td>0.06</td><td>0.06</td><td>0.08</td><td>0.08</td><td>0.09</td><td>0.09</td><td>0.12</td></tr><tr><td>0.4</td><td>-0.82</td><td>-0.46</td><td>-0.20</td><td>-0.14</td><td>-0.58</td><td>-0.25</td><td>-0.02</td><td>0.02</td><td>-0.39</td><td>-0.10</td><td>0.10</td><td>0.13</td><td>-0.20</td><td>-0.02</td><td>0.09</td><td>0.10</td></tr><tr><td rowspan="2">1, 1</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.06</td><td>0.05</td><td>0.06</td><td>0.06</td><td>0.08</td><td>0.08</td><td>0.09</td><td>0.10</td><td>0.12</td></tr><tr><td>-0.82</td><td>-0.46</td><td>-0.20</td><td>-0.14</td><td>-0.57</td><td>-0.24</td><td>-0.02</td><td>-0.03</td><td>-0.39</td><td>-0.09</td><td>0.11</td><td>0.14</td><td>-0.18</td><td>0.0</td><td>0.12</td><td>0.12</td></tr></table>

Besides these two pure Nash solutions, simulation also shows us a mixed solution

$$
y _ {3} = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0. 2 8, 0. 7 2, 0, 0, 0, 0)
$$

$$
z _ {3} = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0. 7 5 5, 0, 0, 0, 0. 2 4 5)
$$

which means when P1 selects strategy (20, 20, 35) at probability of 0.28 and selects strategy (20, 35, 35) at probability of 0.72, while P2 selects strategy (20, 35, 35) at probability of 0.755 and strategy (35, 35, 35) at probability of 0.245, each supplier cannot be better off if any of them deviates from this probability distribution solely. In this situation, the profit pair is (0.0663, 0.1257). Although all three solutions are Nash equilibria, we can see that pair $(y_{2}, z_{2})$ dominates other two for both suppliers, thus it is the dominant solution. As the same as in Case 1, supplier P1 still will not adopt perfectly competitive price even at the first stage.

Case 3 ( $S_{1}^{1}=0.5$ ). In Table 3 where both suppliers begin the game with equal market shares, the profit matrix is symmetric and the unique Nash equilibrium solution has both suppliers adopting

$$
y = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
$$

$$
z = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
$$

which means that both suppliers would choose pricing strategy (0.4, 1.0, 1.0), which is corresponding to (20, 35, 35). This result is expected since when P1 is able to share the market with the incumbent equally from the very beginning, and the products are identical, both suppliers are supposed to have exactly the same pricing strategies. In this case, the market shares of both suppliers fix at 0.5 over the whole time horizon, and the profits yielded are as the same as 0.09.

## 6. Conclusion

In this paper, we reviewed a dynamic model to study market power by examining the interaction between initial market shares assigned to market participants and pricing mechanism chosen by each of them. Since both suppliers are presumed to sell identical products at the same costs, the only differences between the suppliers are the assumed initial market shares and the consequent pattern of prices they set over time.

As in previous work $[2–4]$ , a multiperiod dynamic profit-maximizing duopoly is approximated by a bimatrix game to simplify the problem. Instead of considering only extreme prices, we introduced two other predetermined fixed price levels between the static perfect competition price and the static monopolistic price. To ensure the existence of Nash solution, either pure or mixed, we solved the problem in the framework of mixed strategies instead of pure strategies.

The numerical examples indicated that the Nash price sequence in all cases start at a price higher than the perfect competition price at the first stage. This means that the new entrant will not adopt a perfectly competitive price at the beginning to attract more market share at the expense of losing profits, which is different from the result in $[2-4]$ . In Case 2, we obtained three Nash solutions, including two pure solutions and one mixed solution. Though one of the pure solutions dominated the other two, all the three solutions can occur in practice where there is no cooperation between two suppliers. Thus none of the solutions should be ignored. By using the proposed procedure, we guarantee to have at least one Nash equilibrium and no mixed solution will be missed.

## References

[1] T. Basar, B.J. Olsder, Dynamic Noncooperative Game Theory, Academic Press, London, 1999.

[2] R.E. Schuler, Dynamic Price Patterns in Spatial Oligopolistic Markets: The Impact of Lagged Quantity Adjustment, Regional Science: Perspective for the Future, Macmillan, London, UK, 1997, pp. 43–69.

[3] R.E. Schuler, The dynamics of market power with deregulated electricity generation supplies, in: Proceedings of the 31st Hawaii International Conference on Systems Sciences, vol. 3, Big Island of Hawaii, Hi, USA, 1998, pp. 9–14, Jan. 6–9.

[4] R.E. Schuler, B.F. Hobbs, Price adjustments in oligopolistic markets: the impact of lags in customer response, Market Strategy and Structure, Harverster-Sheatsheaf, London, 1992.

![](/api/attachments/K5FCSF3G/fulltext/images/772e103a2adc363278b46edfcd66c3077e867b6f9376d6d7f77aea64a55c4761.jpg)

Jose B. Cruz, Jr. is the Howard D. Winbigler Chair in Engineering and Professor of Electrical Engineering at the Ohio State University OSU. He received his BS summa cum laude from the University of the Philippines in 1953, SM from the Massachusetts Institute of Technology in 1956 and the PhD from the University of Illinois in 1959, all in Electrical Engineering. He served as Dean of the College of Engineering at OSU from 1992 to 1997,

Professor of Electrical and Computer Engineering at the University of California in Irvine UCI from 1986 to 1992 and at the University of Illinois from 1965 to 1986. Dr. Cruz was elected as a member of the National Academy of Engineering in 1980. He is also a life Fellow of the Institute of Electrical and Electronics Engineers; recipient, Curtis W. McGraw Research Award of the American Society for Engineering Education 1972; recipient, Halliburton Engineering Education Leadership Award, 1981; distinguished member, IEEE Control Systems Society, designated in 1983; recipient, IEEE Centennial Medal, 1984; recipient, IEEE Richard M. Emberson Award, 1989; Fellow, American Association for the Advancement of Science elected 1989; recipient, ASEE Centennial Medal, 1993; and recipient, Richard E. Bellman Control Heritage Award, American Automatic Control Council in 1994.

![](/api/attachments/K5FCSF3G/fulltext/images/a1f7b48d8f973ebac3211b70b08ef5bc7b1ab2a47f96f1e014ace06d4a82b34a.jpg)  
Xiaohuan Tan received her BE degree in Electrical Engineering from Southeast University, Nanjing, China, in 1997 and the ME degree in Electrical and Electronic Engineering from Nanyang Technological University, Singapore, in 2001. Currently, she is pursuing the PhD degree in Electrical Engineering at the Ohio State University, Columbus, OH. Her research interests include game theory and electric power economics.
