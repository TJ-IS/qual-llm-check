---
otero_id: 9870
otero_key: "DF6N3S4R"
title: "Algorithmic determination of the maximum possible earnings for investment strategies"
authors: "Olivier Brandouy; Philippe Mathieu; Iryna Veryzhenko"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.09.020"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Algorithmic determination of the maximum possible earnings for investment strategies

Olivier Brandouy <sup>a,</sup>⁎, Philippe Mathieu <sup>b</sup>, Iryna Veryzhenko <sup>c</sup>

<sup>a</sup> GREGOR, EA 2474, Sorbonne Graduate Business School (IAE de Paris), 21 rue Broca, F-75005, Paris, France

<sup>b</sup> CNRS-LIFL (UMR 8122), Computer Science Department, University of Lille 1, Cité Scientifique, F-59655, Villeneuve d'Ascq Cedex, France

<sup>c</sup> ESSCA School of Management, LUNAM University, 55 quai Alphonse Le Gallo, F-92513, Boulogne-Billancourt Cedex, France

## a r t i c l e i n f o

Article history: Received 4 June 2012 Received in revised form 9 August 2012 Accepted 9 September 2012 Available online 5 October 2012

Keywords: Optimization Algorithm Graph Investment strategy

## a b s t r a c t

This paper proposes a new method for determining the upper bound of any investment strategy's maximum profit, applied in a given time window [0,T]. This upper bound is de<sup>fi</sup>ned once all the prices are known at time T and therefore represents the ex-post maximum ef<sup>fi</sup>ciency of any investment strategy determined during the relevant time interval. This approach allows us to gauge in absolute terms those behaviors de<sup>fi</sup>ned through atomic “buy” and “sell” actions, and can be extended to more complex strategies. We show that, even in the ex-post framework, establishing this upper bound when transaction costs are implemented is extremely complex. We <sup>fi</sup>rst describe this problem using a linear programming framework. Thereafter, we propose to embed this question in a graph theory framework and to show that determining the best investment behavior is equivalent to identifying an optimal path in an oriented, weighted, bipartite network or a weighted, directed, acyclic graph. We illustrate this method using real world data and introduce a new theory about absolute optimal behavior in the <sup>fi</sup>nancial world © 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Performance gauging in Finance is a complicated issue that generates a series of methodological questions (Jensen [10], Sharpe [19], Elton et al. [6] or Malkiel [14]). In assessing the performance of a sequence of investment/divestment actions relating to a <sup>fi</sup>nancial asset over time (for example a particular tracker fund), two frameworks can be considered.

The <sup>fi</sup>rst option is to adopt an ex-ante evaluation point of view, answering the following question: “Were the choices of the investor, given his knowledge of the future at that time, optimal or not when they were realized?”. This point of view acknowledges that investment occurs in a stochastic context and that a poor ex-post result does not necessarily indicate that bad decisions were made ex-ante, or during the decision process. Notice that this ex-ante performance assessment requires an awareness of the investor's conception of the future at each stage in the process, and is therefore dif<sup>fi</sup>cult to achieve in practice.

The second option is to adopt an ex-post evaluation approach, which considers only the statistical result of a given investment strategy over time, once price motions are perfectly known. This approach is widely used in professional asset management. For example, the performance of various investment styles is gauged using this technique. Financial journals use this ex-post approach to create yearly rankings and to report on the performance of asset managers and funds. In the latter case, performance is evaluated using a relative comparison among funds, as it is impossible to know what would have been the best behavior during the relevant period, or how the best output compares with the performance upper bound.

This paper can provide, in the ex-post framework previously described, the upper bound to any investment strategy in a given time window, for the trading of a single <sup>fi</sup>nancial asset. We do not address strategic/tactical allocation questions (for the use of decision support systems in this context, see Beraldi et al. [1]) or the operational process that allows fund managers to identify states in the market where buying or selling is particularly appropriate (for example in exploiting results delivered by neural network forecasting, see Lam [11] or Chen and Leung [2], rough sets Shen and Loh [20] or stock cherting Leigh et al. [12]). Neither do we propose a method that ranks various strategies in terms of risk-return performance (although our approach might be extended to this bicriteria framework; for an example of heuristic algorithm allowing to optimize complex risk-return investment problems, see for instance Liu et al. [13]). Instead, we offer a computational characterization of the pro<sup>fi</sup>ts upper bound that might have been reached, by chance or skill, in trading a single <sup>fi</sup>nancial asset during a given time-window.

Computing this limit allows the determination of an ex-post optimal strategy S that actually delivers the upper bound. We call this problem the S -determination, and show that it is far from trivial, despite its similarity to many popular models that have frequently proved completely inef<sup>fi</sup>cient. Our new method delivers an absolute performance indicator geared towards the ex-post evaluation of a wide range of trading strategies.

This upper bound can be characterized using a linear programming framework and solved with a simplex approach or with dynamic programming formalism. Nevertheless, if these methods are theoretically correct, they suffer from severe limitations in terms of computability (in the worst case, the underlying algorithm being non-polynomial for the simplex). We therefore propose to embed this question in a graph theory framework and to show that determining the best investment behavior is equivalent to identifying an optimal path in an oriented, weighted, bipartite network. We illustrate these results with real data as well as simulated algorithmic trading methods.

This paper is organized as follow. We <sup>fi</sup>rst formalize the framework we start from, de<sup>fi</sup>ne explicitly the S -determination problem, and give some illustrations of the complexity of the optimization task delivering S (Section 2). We then present the mathematical frameworks related to these questions (Section 3) and a new algorithm geared at identifying the S strategy (Section 4). In the last section we illustrate this latter algorithm and provide some practical implementations to gauge the ex-post absolute performance of a few trading strategies (Section 5).

## 2. Elements of the game, formalizations and examples

## 2.1. Elements of the game

Consider the situation in which one investor has realized a sequence of investments/divestments for a given <sup>fi</sup>nancial asset (a stock, an index or a portfolio) during a given time window $[ t = 0 ,$ t=n]. At time t=n, her actions (for example Buy, Sell) and the prices at which they were undertaken (that is, the historical price series $\stackrel {  } { p } = \{ p _ { t } | t \in [ 0 , n ] \} )$ ) are perfectly known. We do not focus on “how” <sup>¼ f j g½ -</sup>the investor behavior has been formed (for example, this investor should have generated trading rules with genetic programming, see Potvin et al. [17]), or on the relevant information that are needed to do so. We rather focus on the decisions it delivered as data and that lead to a speci<sup>fi</sup>c pro<sup>fi</sup>t (or loss) at time t=n.

This investor has the opportunity to assess her performance with respect to the best possible behavior in this time window. This assessment can be made checking whether or not her behavior matches the absolutely optimal set of actions that could have had realized. Notice this optimal set can theoretically be computed at time t=n since all the prices are known.

This comparison requires some hypotheses to be respected. The following “rules of the game” present these hypotheses and describe a formal framework in which the actual set of undertaken, compared actions can be matched against any other set of trades pertaining to the same conditions, and speci<sup>fi</sup>cally, to the absolutely optimal set of actions.

## 2.1.1. Market liquidity

Let's assume that the prices in [t=0,t=n],n-ℕ are those at which this investor has had the opportunity to rebalance her portfolio. We posit a price-taker framework, i.e.. The agent's decisions cannot affect these prices; suf<sup>fi</sup>cient liquidity at these prices is assumed.

## 2.1.2. The “all or nothing” general constraint

We now de<sup>fi</sup>ne a set of “rules” for this investor, in other words, a series of constraints on her behavior. These simpli<sup>fi</sup>cations are useful in allowing rigorous comparisons between sets of actions (strategies) undertaken during a given period. In this article, these rules de<sup>fi</sup>ne an “all or nothing” behavior: whether the investor is totally invested in the risky asset or has realized all her wealth in cash:

• At the initialization stage (i.e. at t = 0), the initial wealth $W _ { 0 }$ of the investor is composed of a certain amount of cash $\left( C _ { 0 } \right)$ and no stock $( A _ { 0 } = 0 ) \colon W _ { 0 } = A _ { 0 } + C _ { 0 } .$ . At date t=1 (the beginning of the game) we posit $C _ { 1 }$ to be equal to the <sup>fi</sup>rst price of the considered time series.

• The investor must decide for each $t \epsilon ( 1 , n )$ one speci<sup>fi</sup>c action with regard to the composition of her portfolio: Buy, Sell or Remain unchanged (respectively coded B, S and U). In other terms, the investor has to compose a “sentence” of size n using characters in B, S,U. The interpretation of each of these actions is as follows:

– Buy: One can write B if and only if $\cdot w _ { t - 1 } = C _ { t - 1 } .$ If B is written at date t; all the investor's cash is converted into assets (delivering a new quantity for $A _ { t } \neq 0 )$ , assuming transaction costs at a c% rate,

$$
A _ {t} = \frac {W _ {t - 1}}{p _ {t} \times (1 + c)}
$$

Additionally, the <sup>fi</sup>rst character in any sentence must be a B.

– Sell: if and only $i f A _ { t - 1 } \neq 0$ , the investor can write S and convert her position into cash. Considering an identical rate of transaction costs c,

$$
C _ {t} = A _ {t - 1} \times (p _ {t} \times (1 - c))
$$

– Remain unchanged: Whatever the nature of $W _ { t } .$ (cash or assets), she can also decide to write U and let her position remain unchanged at date $t \colon W _ { t } = W _ { t - 1 }$

• This “sentence” is one investment strategy S over p<sup>→</sup> chosen in a set of strategies {S}. Notice, that in this framework Card{S}=2<sup>n</sup>.

Note that these “rules of the game” can be used by the investor without knowing the future prices (she performs ex-ante decisions by de<sup>fi</sup>nition) and will deliver different results: each instance of $S _ { i }$ can be gauged in terms of relative performance with respect to any other strategy $S _ { j , j \neq 1 }$ (and reciprocally). Among these strategies, the best possible one in terms of maximum pro<sup>fi</sup>t, denoted by S , can be determined ex-post the realization of the price sequence (when t=n). Consequently, the objective function is:

$$
S _ {*} \rightarrow m a x (W _ {t + n} - W _ {t})\tag{2.1}
$$

Thus, it can be generated by an investor acting in the “ex-ante” framework by chance or skill (the latter alternative is not discussed here). In any case, S is the upper bound in terms of absolute performance in {S} and therefore a much more interesting parameter for gauging any strategy S . As we will show later, the best strategy is relatively easy to identify when transaction costs are not implemented. When transaction costs alter pro<sup>fi</sup>ts, this identi<sup>fi</sup>cation is far more complex.

## 2.2. Basic illustration

Let's consider the following (arbitrarily chosen) price series (see Table 1 and Fig. 1):

This example illustrates simply that, when transaction costs are minor (or absent), the best strategy consists in accumulating all positive spreads (i.e. positive slopes) observed in Fig. 1. This strategy is denoted $S 1 ^ { * }$ in Table 2 (see also Fig. 1). When transaction costs are implemented, the same strategy becomes far less interesting (see S3, Table 2). Some trades are simply not pro<sup>fi</sup>table in the context of high transaction costs. The optimal strategy when such costs are supported is $S 2 ^ { * }$ (see the same Figure and Table). It does not consist of realizing all pro<sup>fi</sup>table trades as soon as they are observed in the price sequence (for example “Buy” in position 9 and “Sell” in position 10). It is clearly different from the situation in which there are no transaction costs, and does not match trivial formulations such as the following, which would lead to S5 in Table 2:

Basic arti<sup>fi</sup>cial time series.

<table><tr><td>t</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td> $p_t$ </td><td>100</td><td>120</td><td>90</td><td>160</td><td>126</td><td>150</td><td>140</td><td>160</td><td>110</td><td>170</td><td>168</td><td>180</td></tr></table>

![](/api/attachments/DF6N3S4R/fulltext/images/e4c8fbc82f38fb8af5414151f7294c83e78871202c86832a093d4e839a44caf8.jpg)  
Fig. 1. Basic arti<sup>fi</sup>cial time series and some strategies.

“capture the biggest spread in the price sequence (thus, here “Buy at time $3 "$ and “Sell at time $1 2 " )$ , then eliminate all impossibilities in further trades implied by the rules of the game (thus, it remains one potential trade between time 1 and $2 \ldots { \bar { ) } } ,$ , and repeat this loop until all net positive trades are realized ( trade between times 1 and 2 would not be realized here because it is not pro<sup>fi</sup>table with 10% TC)”.

Note that S2, which is similar to $S 3 ^ { * }$ in a transaction-cost free framework, is not as interesting as $S 1 ^ { * } .$ An easy way to solve this problem when transaction costs are implemented is to generate all possible sentences and to use these to compute the net earning and identify $S * _ { * }$ This set is of <sup>fi</sup>nite size $2 ^ { n }$ and thus exponential. As we will now show, there are at least two ways to improve ef<sup>fi</sup>ciently the computation of the optimal strategy S , whatever the level of transaction costs. One is based on a simplex method, another relies on locating an optimal path in an oriented bipartite network.

## 3. Mathematical models: linear programming method and search in graphs

In this section, we show that the identi<sup>fi</sup>cation of S can be described as a linear programming problem with a classical simplex solution. Unfortunately, this approach is relatively inef<sup>fi</sup>cient since the simplex algorithm is non-polynomial in the worst case (i.e.; one may lack the necessary computing resources to obtain a result immediately, as soon as the size of $\vec { p }$ becomes important.

## 3.1. Initial simplification

Before formal results are presented, we introduce the two theorems necessary for solving the problem. These preliminary elements aim to simplify the solution we propose.

First simplification: <sup>fi</sup>ltering the price sequence.

Let's consider the price vector $\vec { p }$ consisting of three consecutive prices $p _ { t } , p _ { t + 1 } , p _ { t + 2 }$ and the function

$$
R (x, y) = y (1 - c) - x (1 + c)\tag{3.1}
$$

In $\operatorname { E q . } \left( 3 . 1 \right)$ , the $R ( x , y )$ , function computes the net earnings of suc cessive buy and sell actions with c% transaction costs. In this equation, x denotes the price at which one buys and $y$ the price at which one sells. By de<sup>fi</sup>nition, y appears later in the time sequence than x. We show that S in ${ \vec { p } } , \mathsf { a s }$ de<sup>fi</sup>ned on page 3, can be identi<sup>fi</sup>ed in a subset of $\vec { p }$ denoted $\overrightarrow { f p , }$ consisting of the extreme points in the price sequence (peaks and troughs) and ignoring any intermediary points (here, $p _ { t + 1 } )$ . We assume $p _ { t + 2 } \geq p _ { t + 1 } \geq p _ { t }$ . Therefore $R ( p _ { t } ,$ $p _ { t + 2 } \big ) > R \big ( p _ { t } , p _ { t + 1 } \big )$ and $R ( p _ { t } , p _ { t + 2 } ) > R ( p _ { t + 1 } , p _ { t + 2 } )$ . In this latter case, $p _ { t + 2 }$ is a peak while $p _ { t }$ is a trough.

Theorem 1. Ignoring intermediary points: Identifying S<sub>\*</sub>, $p _ { t + 1 }$ can be ignored.

## Proof 1. Reductio ad absurdum/proof by contradiction:

If it were not the case, since buying and selling on the same date is not allowed: $R ( p _ { t + 1 } , p _ { t + 2 } ) > R ( p _ { t } , p _ { t + 2 } )$

Therefore: $p _ { t + 2 } ( 1 - c ) - p _ { t + 1 } ( 1 + c ) > p _ { t + 2 } ( 1 - c ) - p _ { t } ( 1 + c )$

Which can be simpli<sup>fi</sup>ed: $- p _ { t + 1 } > - p _ { t }$

Thus, $p _ { t + 1 } < p _ { t }$ since, by de<sup>fi</sup>nition $p _ { t + 1 } > p _ { t }$

Q.E.A

Note that an analogous demonstration can be made in the case where $p _ { t + 2 } { \le } p _ { t + 1 } { \le } p _ { t }$ . As a consequence, if $p _ { t + 1 }$ is an intermediary point, as revealed previously; it is unnecessary to identify $S _ { * , }$ In other words, if one considers a complete price sequence $\vec { p }$ , only peaks and troughs should be used to identify S (that is, $\overrightarrow { f p ) }$

Lemma 1. No inclusion of losses: To identify S , one can ignore all situations in which $R ( x , y ) < 0$

In other words, no trade with negative net earnings can be included in the best strategy, which also excludes situations in which the socalled “buy and hold” strategy is unpro<sup>fi</sup>table.

3.1.1. Determining two subsets of prices for potential “buy” and “sell” actions

From Theorem 1 we know that it is necessary and suf<sup>fi</sup>cient for determining S to focus on extreme points in the price sequence. We now show that $\overrightarrow { f p }$ can itself be divided into two separate sub-vectors of peaks and troughs corresponding to two independent potential buy and sell positions in $\vec { p }$ (resp. denoted $\overrightarrow { f p _ { B } }$ and $\overrightarrow { f p _ { S } } )$ .

Table 2  
Some strategies among all $2 ^ { 1 2 }$ potential sentences.

<table><tr><td></td><td> $\frac{t}{p_t}$ </td><td> $\frac{1}{100}$ </td><td> $\frac{2}{120}$ </td><td> $\frac{3}{90}$ </td><td> $\frac{4}{160}$ </td><td> $\frac{5}{126}$ </td><td> $\frac{6}{150}$ </td><td> $\frac{7}{140}$ </td><td> $\frac{8}{160}$ </td><td> $\frac{9}{110}$ </td><td> $\frac{10}{170}$ </td><td> $\frac{11}{168}$ </td><td> $\frac{12}{180}$ </td><td> $W_{12}-W_1$ </td></tr><tr><td rowspan="2">TC=0.0</td><td>S1*</td><td>B</td><td>S</td><td>B</td><td>S</td><td>B</td><td>S</td><td>B</td><td>S</td><td>B</td><td>S</td><td>B</td><td>S</td><td>480.61</td></tr><tr><td>S4</td><td>U</td><td>U</td><td>B</td><td>S</td><td>B</td><td>U</td><td>U</td><td>S</td><td>B</td><td>U</td><td>U</td><td>S</td><td>369.41</td></tr><tr><td rowspan="3">TC=0.1</td><td>S2*</td><td>U</td><td>U</td><td>B</td><td>S</td><td>B</td><td>U</td><td>U</td><td>S</td><td>B</td><td>U</td><td>U</td><td>S</td><td>202.33</td></tr><tr><td>S3</td><td>B</td><td>S</td><td>B</td><td>S</td><td>B</td><td>S</td><td>B</td><td>S</td><td>B</td><td>S</td><td>B</td><td>S</td><td>144.17</td></tr><tr><td>S5</td><td>U</td><td>U</td><td>B</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>S</td><td>163.64</td></tr></table>

Let's consider four consecutive prices $p _ { t } , p _ { t + 1 } , p _ { t + 2 } , p _ { t + 3 }$ such as $p _ { t + 1 } > p _ { t } , p _ { t + 3 } > p _ { t + 2 }$ and $p _ { t + 2 } { < } p _ { t + 1 }$ . In the latter case, we do not consider a situation in which $p _ { t + 2 } > p _ { t + 1 }$ , as it is equivalent to the initial simpli<sup>fi</sup>cation case discussed previously.

Theorem 2. To identify $S _ { \ast , }$ none of the $\overrightarrow { f p _ { B } }$ can be associated with a decision S and none of the $\overrightarrow { f p _ { S } }$ can be associated with a decision B.

Proof 2.

(i) Since $p _ { t + 1 } { > } p _ { t } { \Rightarrow } R ( p _ { t } , p _ { t + 3 } ) { > } R ( p _ { t + 1 } , p _ { t + 3 } )$ . Then $p _ { t } {  } B { \succ } p _ { t + 1 } {  } B$ with $"  "$ denoting “can be associated with a decision $\cdots ^ { \mathfrak { n } }$ and $" \succ "$ the preference operator.

(ii) Similarly, since $p _ { t + 2 } { < } p _ { t + 1 } { \Rightarrow } R ( p _ { t + 2 } , p _ { t + 3 } ) > R ( p _ { t + 1 } , p _ { t + 3 } )$ . Then $p _ { t + 2 } {  } B { \succ } p _ { t + 1 } {  } B$

From Lemma 1 we know that the situation in which $p _ { t + 3 } < p _ { t }$ can be omitted.

Therefore, from (i), (ii) and Lemma 1:

– whether $p _ { t } \gets B$ and $p _ { t + 1 } \gets U$ from (ii); thus $p _ { t + 2 } \gets \{ U \}$ and $p _ { t + 3 }  \{ U o r S \}$

– or $p _ { t } \gets U$ and $p _ { t + 1 } \gets U ;$ thus $p _ { t + 2 } \gets \{ U o r B \}$ and $p _ { t + 3 }  \{ U o r S \}$

$$
(p _ {t}, p _ {t + 2}) \leftarrow \{U o r B \}; \overrightarrow {f p _ {B}} = \left\{p _ {t}, p _ {t + 2} \right\}
$$

$$
(p _ {t + 1}, p _ {t + 3}) \leftarrow \{U o r S \}; \overrightarrow {f p _ {S}} = \left\{p _ {t + 1}, p _ {t + 3} \right\}
$$

Q.E.D

This theorem does not state where to buy or to sell in the subsets $\overrightarrow { f p _ { B } }$ and $\overrightarrow { f p _ { S } }$ to identify S . It uniquely states that it is not worth buying in any element of $\overrightarrow { f p _ { B } }$ or selling in any element of ${ \overrightarrow { f p _ { S } } } .$

## 3.2. A linear programming method for the identification of S

A <sup>fi</sup>rst way to solve the S -determination problem is to use a linear programming method. The basic idea here is to maximize an objective function subject to a set of constraints formalizing the rules in which this problem is embedded. We will now explain how this program should be written

Let $a ( i , j )$ denote the potential bene<sup>fi</sup>t one can obtain if $\cdot _ { p _ { i } \in \overrightarrow { f p _ { B } } }$ and $p _ { i } { \in } \overrightarrow { f p _ { S } }$ . Notice $a ( i , j )$ is computed using Eq. (3.1). To be more explicit:

$$
a (i, j) = p _ {j} (1 - c) - p _ {i} (1 + c), \text { with } p _ {i} \in \overrightarrow {f p _ {B}} \text { and } p _ {j} \in \overrightarrow {f p _ {S}}\tag{3.2}
$$

Let x(i,j) be a dummy variable coding 0 or 1 that will be used to ignore (identify) transitions between any two prices $p _ { i }$ and $p _ { j } .$ If $p _ { i } \gets U \mathrm { o r } p _ { j } \gets U$ then $x ( i , j ) = 0$ , else $x ( i , j ) = 1$ . The S strategy consists in increasing an initial wealth $W _ { t }$ to obtain the maximum terminal wealth $W _ { t + n }$ in selecting an optimal set of trading actions at $p _ { i }$ and $p _ { j } .$ Using the notations de<sup>fi</sup>ned above, the identi<sup>fi</sup>cation of S can be done solving the following linear problem:

$$
m a x \sum_ {(i, j) \in \overrightarrow {f p _ {B}} \cup \overrightarrow {f p _ {S}}} a (i, j) x (i, j)\tag{3.3}
$$

$$
\sum_ {(i, j) \in S _ {*}} ^ {(s. t.)} x (i, j) \leq n\tag{3.4}
$$

$$
\sum_ {(i, j) \in \overrightarrow {f p _ {B}} \cup \overrightarrow {f p _ {S}}} x (j, i) + x (i, j) \leq 1, \forall i \in \overrightarrow {f p _ {B}}\tag{3.5}
$$

$$
\sum_ {i, k \in f p _ {B}} x (i, k) + \sum_ {j, k \in f p _ {S}} x (j, k) = 0\tag{3.6}
$$

$$
\sum_ {i > j} x (i, j) + \sum_ {j > i} x (j, i) = 0, \forall i \in \overrightarrow {f p _ {B}}, j \in \overrightarrow {f p _ {S}}\tag{3.7}
$$

$$
0 \leq x (i, j) \leq 1, \forall i \in \overrightarrow {f p _ {B}}, j \in \overrightarrow {f p _ {S}}\tag{3.8}
$$

Literally, the objective function (3.3) states that one seeks to maximize the total bene<sup>fi</sup>ts in trading (that is, to identify S ). Note that the program in Eq. (3.3) to Eq. (3.8) is equivalent to Eq. (2.1).

Constraint (3.4) implies that S cannot be composed of more than n prices (if the graph has n nodes) while constraint (3.5) requires that the number of matching edges incident to vertex i not exceed one.

Constraint (3.6) guarantees the absence of any connection inside buy and sell subsets.

Constraint (3.7) does not allow reversed price series with respect to their sequential ordering.

Constraint (3.8) requires that $x ( i , j ) = 1$ if a trade occurs between position i and j in $\overrightarrow { f _ { p } } ,$ otherwise, $x ( i . j ) = 0$ (this constraint requires that each edge $( i , j )$ not be used in the matching more that once). The latter constraint means that the problem can be solved by the simplex method.

However, it is virtually impossible to explicitly enumerate all these constraints when $\overrightarrow { f _ { p } }$ is of moderate size. It is also recognized that the simplex algorithm is exponential even if it can be solved for certain cases in polynomial time. Provided the problem does not involve integers ,<sup>1</sup> an underlying matrix of dimension (m,n) (where n is number of variables and m, the number of constraints) will lead to an exponential computational time ${ \cal { O } } ( n ^ { m } )$ which means that any computation of such an algorithm for large price sequences will have signi<sup>fi</sup>cant computing elapsed time.

## 3.3. Embedding the identification of S<sub>\*</sub> in a graph structure

Let each price in $\overrightarrow { f p }$ be depicted as a vertex in a network. The cardinality of this subset is equal to k. Each vertex is indexed with an integer with respect to its place in the price series. We show now how to construct a bipartite, oriented and weighted network $\mathcal { N } \Big ( E , \overrightarrow { f p _ { B } } , \overrightarrow { f p _ { S } } \Big )$ connecting points in $\overrightarrow { f p _ { B } }$ and ${ \overrightarrow { f p _ { S } } } .$

De<sup>fi</sup>nition. Let $\aleph _ { X }$ represent the subset of vertices succeeding vertex X. The network is de<sup>fi</sup>ned by the successors of each vertex.

## 3.3.1. Graph construction

The initial situation from which we start is: $\forall X { \in } \overrightarrow { f p } \kappa , \mathrm { x } { = } \emptyset$ . From this situation, two different kinds of edges can be built:

• Trading edge $\left( T E _ { i , j } \right) ;$ : for any two vertices i∈ $\overrightarrow { f p _ { B } }$ and $| j { \in } \overrightarrow { f p _ { S } } ,$ vertex j-א if and only if:

1. $j { > } i$ (to ensure temporal consistency)

2. c being the rate of transaction costs,

$$
R _ {i, j} = p _ {j} (1 - c) - p _ {i} (1 + c) \geq 0\tag{3.9}
$$

• Forward edge $( F E _ { m , n } ) \colon$ for any two vertices m∈ $\overrightarrow { { f p } _ { S } }$ and n $\overrightarrow { \mathsf { f } p _ { B } } ,$ , n-א if and only if:

1. n>m (which ensure temporal consistency),

$$
2. \kappa_ {X} = \emptyset .
$$

Notice we impose a time consistency rule, similar to Eqs. (3.6) and (3.7), to avoid backward connections in this bipartite oriented graph. This means that a starting vertex $p _ { t + k }$ cannot be connected to an ending vertex $p _ { \mathrm { t + 1 } }$ with $k \geq l .$

The rule presented in Eq. (3.9) obviously determines a pro<sup>fi</sup>t as in Eq. (3.1). For any two vertices, these pro<sup>fi</sup>ts can be analyzed as weights for the corresponding edges of .

<sup>N</sup>Consequently, we receive a balanced quasi-bipartite, weighted and directed network. We propose to interpret weights computed with 10 as distances between two vertices.

In the construction of ${ \mathcal { N } } ,$ one can see that the number of edges depends upon the level of transaction costs c:

• The greater c makes the network sparser and the solution of the problem easier.

• When $\mathsf { c n o , }$ , the number of edges increases and makes the network dense. For a speci<sup>fi</sup>c threshold, θ, is a complete antisymmetric network (with respect to the time consistency rule). θ can be computed linearly; for any two consecutive prices in $f p , p _ { i } { \in } \overrightarrow { f p _ { B } }$ and $p _ { i } { \in } \overrightarrow { f p _ { S } } .$

$$
\theta = \min \left(p _ {j} - p _ {i}\right) / \left(p _ {j} - p _ {i}\right), \forall (i, j)\tag{3.10}
$$

In the example provided in Section 2.2 (see Table 1), this threshold is 3%.

Proposition 1. If $c < \theta ,$ then the S -determination problem is the maximum number of edges appearing in the path.

When cb θ, is completely antisymmetric. In this situation, we can derive Theorem 3.

Theorem 3. If c bθ and any 4 consecutive prices $p _ { t } , p _ { t + 1 } , p _ { t + 2 } , p _ { t + 3 }$ in a filtered price series such as $\overrightarrow { f p }$ (see Section 3.1) with $R ( t , t + 1 ) > 0 ,$ $R ( t , t + 3 ) > 0 , R ( t + 2 , t + 3 ) > 0$ then:

$$
R (t, t + 1) + R (t + 2, t + 3) > R (t, t + 3)
$$

Proof 3. We make the difference between $R ( t , t + 1 ) + R ( t + 2 , t + 3 )$ and $R ( t , t + 3 )$ to show that this difference is positive.

$$
\begin{array}{l} - p _ {t} (1 + c) + p _ {t + 1} (1 - c) - p _ {t + 2} (1 + c) + p _ {t + 3} (1 - c) + p _ {t} (1 + c) - p _ {t + 3} (1 - c) = \\ p _ {t + 1} (1 - c) - p _ {t + 2} (1 + c) = \\ \left(p _ {t + 1} - p _ {t + 2}\right) - c \left(p _ {t - 1} - p _ {t + 2}\right) \end{array}
$$

From that point it is clear that if: $c = \frac { p _ { t + 2 } - p _ { t + 1 } } { p _ { t + 2 } + p _ { t + 1 } } { \Rightarrow } p _ { t + 1 } ( 1 - c )$ $- p _ { t + 2 } ( 1 + c ) = 0$ and i $\cdot c < \frac { p _ { t + 2 } - p _ { t + 1 } } { p _ { t + 2 } + p _ { t + 1 } } o r c < \theta , \Rightarrow p _ { t + 1 } ( 1 - c ) - p _ { t + 2 } ( 1 + c )$ > 0, thus R(t, t+1)+R(t+2, t+3)>R(t, t+3)

Thus, if cbθ, computing the longest path taking into account the pro<sup>fi</sup>ts made at each Trading Edge is similar to computing the longest path in terms of number of edges appearing in the path: $\forall c < \theta , S ^ { * } =$ $\begin{array} { r } { \sum _ { i = 1 } ^ { k - 1 } T E _ { i , j = ( i + 1 ) } . } \end{array}$ In other terms, when cbθ, it is proved that S is the path connecting all the edges as they appear in sequential order (see Fig. 2(a)). S connect all the vertices.

When cbθ, this result cannot be established and the longest path taking into account the pro<sup>fi</sup>ts made at each Trading Edge is not similar to computing the longest path in terms of the number of edges on it. For example, in Fig. 3, we posit c such as $R ( t + 2 , t + 3 ) { < } 0 ;$ one cannot follow a path in the price series connecting all vertices; several potential and interesting paths can be discovered (see Fig. 3) and therefore must be compared to determine S . One way to tackle this problem might be to compute all possible paths, thus delivering an exponential algorithm.

![](/api/attachments/DF6N3S4R/fulltext/images/8f28f6d925a42c40807ff991450440efa70932f3f4d57de80c2c3b460ec4f1aa.jpg)  
Fig. 3. Evolution of complexity and computing time.

Notice (i) that the maximum complexity of the task appears when $c = \theta + \varepsilon$ and decreases gradually beyond this threshold (see Fig. 3); (ii) a numerical illustration of the graph construction is provided in Appendix A.

We now show how to solve this computational problem using algorithms to determine S in this graph formalism.

## 4. The S<sub>\*</sub>-determination algorithms

In order to make this paper self-contained, we present two different algorithmic solutions for the S -determination problem. The <sup>fi</sup>rst derives from a technique demonstrated by Floyd [7] (see also Shier [22]); the other is an algorithm for searching of the longest paths in a directed acyclic graph (DAG). We have chosen to emphasize the <sup>fi</sup>rst algorithm, as it is very ef<sup>fi</sup>cient, simply programmed, and widely used (Papadimitriou and Steigleitz [16]). Although the Floyd algorithm is outperformed by the DAG longest path algorithm in running time, its pedagogical bene<sup>fi</sup>ts outweigh its drawbacks. The other advantage of the DAG longest path algorithm is that it takes into account the number of both vertices and edges as parameters for characterizing algorithmic complexity. This assumption is very important as the number of edges may vary greatly with changes of transaction costs, making the graph dense (c⤳0) or sparse (c⤳1).

## 4.1. Floyd algorithm approach

In the Floyd algorithm for the shortest-path problem, most steps consist of pairwise comparisons and additions of integers. When the Floyd algorithm is performed with a maximization instead of a minimization procedure, it produces the maximum longest path that corresponds, in our formalism, to S\*. However, we must consider that the absence of an edge between two vertices must be interpreted as a length −∞, whereas in the shortest-path problem this absence is interpreted as a length of +∞. To simplify the algorithm, we can convert a multisource problem into a single-source problem by adding zero-weight edges between the <sup>fi</sup>rst vertex from subset $\overrightarrow { f p _ { B } }$ and other elements in this subset. This convention is needed to <sup>fi</sup>nd the longest path, not between every pair of vertices in the graph, but

(a) Complete Bipartite Network

## (b) Incomplete Bipartite Network

![](/api/attachments/DF6N3S4R/fulltext/images/701897346d93fe1f131d0992cdaffdcd908e3ff00977f81d10162970e70c45c7.jpg)

![](/api/attachments/DF6N3S4R/fulltext/images/ba6932c2f03f97ff1ca3b7c19a73bcc8d92f07b9b1d0e9b8ae0c0341c98499bb.jpg)  
Fig. 2. Different paths related to different levels of c regarding .

between the <sup>fi</sup>rst vertex in $\overrightarrow { f p _ { B } }$ and every other vertex. The other modi<sup>fi</sup>cation introduced is the prohibition of backward loops in the network (see Appendix A for a numerical illustration). The pseudo-code of the S -determination algorithm is presented in Algorithm 1.

Algorithm 1. S -determination algorithm: Floyd algorithm approach.

```lua
for k = 1 to n do
    for j = k to n do
    | path[0][j] = max(path[0][j], path[0][k] + path[k][j])
    end
end
```

The complexity of the S -determination with modi<sup>fi</sup>ed Floyd algorithm must now be established. The longest path from vertex 1 to every other vertex is searched. During the <sup>fi</sup>rst iteration one must go over n−1 vertices. Hence, n−1 additions and n−1 minimizations have to be processed; the <sup>fi</sup>rst iteration consists of $2 ( n - 1 )$ operations. Similarly, it is possible to show that the second iteration consists of $2 ( n - 2 )$ operations, the third $2 ( n - 3 )$ , and so on. The following formula de<sup>fi</sup>nes the total number of operations carried out by the S -determination algorithm:

$$
\sum_ {i = 1} ^ {1 = n} 2 (n - i) = n (n - 1)\tag{4.1}
$$

Thus the S -determination algorithm based on Floyd has $\mathfrak { a } O ( n ^ { 2 } )$ running time and belongs to the PSPACE group (algorithms necessitating a memory of polynomial space). Note that the complexity of the classical formulation of the Floyd algorithm for the shortestpath problem comprises $O ( n ^ { 3 } )$ arithmetic operations. As there is no reverse in the graph studied in this research, the main loop of the Floyd can be ignored, decreasing complexity to a level of $O ( n ^ { 2 } )$ .

We can build other longest-path algorithms able to take into account the sort of constraints presented by the solutions proposed by Dantzig [4] and Shier [21]. The <sup>fi</sup>rst solution resembles Floyd [7], although the order in which the calculations are performed is different. The second algorithm, known as the double-sweep algorithm, <sup>fi</sup>nds the k shortest path lengths between a speci<sup>fi</sup>ed vertex and all other vertices in the graph and can be applied to our problem. The longest path in a directed acyclic network can be easily found using a suitable modi<sup>fi</sup>cation of the Dijkstra shortest-path algorithm Dijkstra [5].

## 4.2. DAG longest path algorithm

In this subsection, we consider S -determination as a longestpaths problem in a directed weighted acyclic graph $( \mathrm { D A G } ) \ G = ( V , E )$ $V { = } f p _ { B } { \cup } f p _ { S }$ . We then apply the linear-time DAG longest path algorithm (Sedgewick and Wayne [18]) to solve this problem. The <sup>fi</sup>rst task is to con<sup>fi</sup>rm that a given DAG has no directed cycles. A depth-<sup>fi</sup>rst search can be used to formally analyze cycle existence. If a directed graph has a cycle, then a back edge will always be encountered in any depth-<sup>fi</sup>rst search of the graph. Since the considered graph has no back edges, cycles are excluded by the graph construction assumptions.

The key element for effective solution of the longest-paths problem in DAG is topological ordering, which allows us compute the longest path for each vertex without having to revisit any decisions. We pass just once over the vertices in topologically sorted order. As we process each vertex, we relax each edge that leaves the vertex. By relaxing the edges of a weighted DAG $G = ( V , E )$ , according to a topological ordering of its vertices, we can compute the longest paths from a single source in $O ( \left| V \right| + \left| E \right| )$ time (Sedgewick and Wayne [18]).

In line with the assumptions described, we also consider the single source longest path problem. We add a dummy source vertex s plus a dummy sink vertex t, such that for all $i { \in } \overrightarrow { f p _ { B } } , \left( s , i \right) { \in } E$ and the weight $R ( s , i )$ is zero; and for all $j { \in } \overrightarrow { f p _ { S } } , \ ( j , t ) { \in } { \cal E } , \ R ( j , t ) { = } 0$ . Hence, the S -determination problem can be de<sup>fi</sup>ned as longest path from s to t in $G ( V , E )$ . Vertices must be numbered in such a way that an edge (i,j) is always directed from a vertex numbered i to a higher numbered vertex j. The source s is then numbered 0 and the sink t numbered $n + 1 .$ . Vertex j is associated with l(j), the longest path from 0 to j, where $l ( j ) = m a x _ { i : ( i , j ) \in E } [ l ( i ) + R ( i , j ) ]$ ]. Vertex j+1 can be labeled using the same equation, and so on until the <sup>fi</sup>nal vertex $n + 1$ is labeled with $l ( n + 1 )$ . Initially l(0) is set to zero. The label $l ( n + 1 )$ represents the length of the longest path from 0 to n+1. Algorithm 2 shows the pseudocode of this algorithm. This method requires the vertices to be processed in topological order. Thus, any topological ordering algorithm can be adapted to solve the longest path problem in DAGs.

Algorithm 2. S -determination algorithm: DAG longest path. $S 1 ^ { * }$ stores the length of the best path we have found so far from s to

```txt
// topologically sort the vertices of G
l[s] = 0

forall j ∈ V \ {s} do
    |    l[j] = -∞
end

foreach i ∈ V \ {s} do
    // in topological order
    foreach j : (i, j) ∈ E do
    if l[i] + R(i, j) > l[j] then
    // relax each outgoing edge from i
    l[j] = l[i] + R(i, j)
    end
    end
end
```

The running time of this algorithm is easy to analyze. Assuming that the DAG is represented using an adjacency list, we can process each vertex in constant time, with an additional time proportional to the number of its outgoing edges. The topological ordering of the vertices in G can be carried out in $O ( \left| V \right| + \left| E \right| )$ time. Thus, the entire algorithm runs in $O ( \left| V \right| + \left| E \right| )$ time. DAG longest path algorithm is faster than Dijkstra algorithm by a factor proportional to the cost of priority-queue operations in Dijkstra algorithm (Sedgewick and Wayne [18]).

4.3. Extension of the S -determination problem in a context where the risk-free rate is available

Let's now consider a (more realistic) situation where the investor retains cash because the potential buy positions all lead to negative or zero pro<sup>fi</sup>ts. This investor is offered an opportunity to invest her cash in a risk-free asset (such as short-term US Treasury Bills) delivering interests at the rate r between t and t+ 1. When Remain unchanged is chosen after a Sell action, for a given timeframe ranging between t and $t + k ,$ , her wealth increases according to the following formula:

$$
\Delta W = W _ {t + k} - W _ {t} = W _ {t} (1 + r) ^ {k} - W _ {t}\tag{4.2}
$$

This new cash reinvestment rule substantially modi<sup>fi</sup>es the graph construction.

## 4.3.1. Graph modifications

First of all, edge selection should be adapted; according to Lemma 1, all situations where $R ( x , y ) < 0$ are ignored. But when the risk-free rate is available, the condition of Lemma 1 is no longer relevant. Each trade must provide higher pro<sup>fi</sup>ts in relation to the one-step, risk-free interest r. Consequently, only situations with

$$
\frac {y (1 - c) - x (1 + c)}{x (1 + c)} > r\tag{4.3}
$$

are accepted. In this formula, x denotes the price at which one buys and y – the price at which one sells. After such modi<sup>fi</sup>cations, the S -determination approach provides the same kind of information as in its initial formulation (without a risk-free rate): when to enter the market and when to leave it. According to this new reinvestment rule, the forward edges (de<sup>fi</sup>ned above), leading from $\overrightarrow { f p _ { S } }$ to $\overrightarrow { f p _ { B } } ,$ will no longer be zero-weighted. Weights for such edges must be calculated according to the formula (4.2).

## 5. Numerical illustrations and conclusive remarks

We now propose one application of the S -determination method on a real-world <sup>fi</sup>nancial series drawn from the daily Dow Jones Index (DJI). This series records each day's closing of the New York stock exchange (NYSE) from December 2, 1980 to February 20, 2009 (i.e. 7156 observations). The unpredictability of future price changes (a cornerstone of modern <sup>fi</sup>nance) can be deduced from the randomness of <sup>fi</sup>nancial returns. On December 2, 1980, no economic agent could have predicted with accuracy the next 7156 DJI closing prices. Even if this had been possible, making use of this knowledge under the constraints enumerated in Section 2 would have been impossible without the S -determination algorithm. Any additional element of uncertainty (unpredictable prices for example) simply increases this initial complexity. However, any strategy for trading a DJI tracker in this time window could be matched against the optimal set of actions identi<sup>fi</sup>ed through the S -determination method.

Using approaches based on the Floyd algorithm (Subsection 4.1) and the DAG longest-path algorithm (Subsection 4.2), we determine the best behavior with transaction costs c respectively at 0% and 5%. The maximum wealth obtainable in these two cases is greater than 1.10E+015 in the <sup>fi</sup>rst case and $1 . 8 3 \mathrm { E } + 0 1 0$ in the second. These <sup>fi</sup>gures seem extraordinarily high; one must keep in mind that they are impossible to obtain because of the global unpredictability of the market at date t with regard to information available on this date. In Fig. 4, we present the evolution of the wealth of an investor who found (by chance or skill) the $S ^ { * }$ set of actions in both contexts.

Some agents claim to be able to predict future prices with some accuracy or at least to identify dates when investors should enter the market or shorten their positions. Technical traders claim to detect signals in past prices (based on patterns) associated with potential market reversals. If the perceived signals indicate at date t a further increase in stock prices, such investors buy stocks immediately until they receive a new signal, dated t+T, associated with the next decrease in prices. Then the technical traders will shorten their positions to avoid losses.

One popular model compares two moving averages based on past prices: the moving average with i lags MM is equal to $\bar { \left( \right)} ^ { 1 } / _ { i }  \bar { \sum _ { i } } \left( p _ { \left( t - i + 1 \right) } \right)$ . One is computed over the long-term L, the other <sup>ð Þþ</sup>on a short timeframe s. If MM crosses MM from the top to the bottom, technical traders will predict a further decrease in stock prices and try to sell their holdings immediately. Alternatively, if these moving averages cross from the bottom to the top, the signal will be interpreted as buy signal.

![](/api/attachments/DF6N3S4R/fulltext/images/5216b09dae1a7a70bbfe8ac308c5b981d854343ba0419643a3b414e357c3f5e3.jpg)  
Fig. 4. S with resp. c=0% and c=0.5% and Dow–Jones Index (y axis in log scale).

In Fig. 5 we generated such signals using the same data as previously; we also computed portfolios managed with respect to the signals. For this purpose the arti<sup>fi</sup>cial investor is endowed with an amount of cash equal to the DJI value at date 1 (974.40). Note that the moving averages strategy provides an example of the “rules of the game” presented in Section 2. Concerning the signals sub<sup>fi</sup>gures, we present a limited time window for graphical clarity. The portfolio sub<sup>fi</sup>gures report the evolution of an investor's wealth using these signals in context of 0% transaction costs.

In Fig. 4, MM<sub>s</sub> is based on 10 days while MM<sub>L</sub> is based on 90 days. With these values we can generate 135 signals in the complete time window, which delivers the portfolio evolution. In Fig. 4, these moving averages are respectively based on 5 and 20 trading days that de liver 469 signals. Note that none of these strategies is interesting in any way.

One can easily rank these strategies in term of overall pro<sup>fi</sup>tability: $M M _ { 1 0 } \nu . s . M M _ { 9 0 }$ seems to perform better than $p _ { t + 1 }$ in this price sample since the <sup>fi</sup>rst delivers an overall pro<sup>fi</sup>tability of +299% (terminal value of the portfolio=3886.36) against +70% for the second (terminal value: 1657.18). One can also measure how far these two strategies are from the optimum S\*. In other words, whatever the relative performance of any trading strategy, S\* can be used to gauge its absolute performance. In our example, both $M M _ { 1 0 } \nu . s . M M _ { 9 0 }$ and $M M _ { 5 } \nu . s . M M _ { 2 0 }$ were poorly performing strategies. A simple buy and hold behavior (buying the market at date 1 and selling it at date 7156) performs far better than these two moving average techniques. Nevertheless, one assumes some automatic trading strategies could outperform this B&H strategy, especially in the context of high frequency data.

In a similar manner, the literature that deals with the forecasting of future market trends (for example with neural networks, see Motiwalla and Wahab [15], Chen et al. [3], Chen and Leung [2], or with support vector machines, see Huang et al. [9]) is geared at delivering investment tools that can be directly assessed using the same steps.

Resolving the S -determination problem does not determine the signals required by automatic trading systems, nor recommend behavior to any real-world investor. It simply establishes a boundary that was, to the best of our knowledge, largely unknown, and proposes a reference in terms of the maximum-pro<sup>fi</sup>t trajectory, against which any population of investment trajectories can be gauged.

However, the S should be re-examined to encompass complex strategies developed over a set of <sup>fi</sup>nancial securities combined in a portfolio. This extension would be far more complex because it raises questions mixing the maximum pro<sup>fi</sup>t and the level of risk with which any strategy is necessarily associated.

(a) Excerpt of signal, M $\mathsf { M } _ { 1 0 }$ v.s. M $\mathsf { M } _ { 9 0 }$  
![](/api/attachments/DF6N3S4R/fulltext/images/244b024b3de60cb711c196053cf01a6054e9637c9dc1a2339ae9e698cd81132e.jpg)

(b) Counterpart portfolio, M $\mathsf { M } _ { 1 0 }$ v.s. M $\mathsf { M } _ { 9 0 }$  
![](/api/attachments/DF6N3S4R/fulltext/images/94cd80fe6dd30bb4aa484e43974ce28ee2d9039bf4155dc87b1bd72e6d3dcb9b.jpg)  
(d) Counterpart portfolio, M $\mathsf { M } _ { 5 } \mathsf { v } . \mathsf { s } .$ . M $\mathsf { M } _ { 2 0 }$

(c) Excerpt of the signals, M $M _ { 5 }$ v.s. M $\mathsf { M } _ { 2 0 }$  
![](/api/attachments/DF6N3S4R/fulltext/images/9a020983528699d39a79fd9a6de66729c8aef6ba7bec4c1398722739b29f0cd0.jpg)

![](/api/attachments/DF6N3S4R/fulltext/images/b9a1e98b0e9112f69447a28fbc3afaf67be197f58f289d7ee4097ca4440c5f74.jpg)  
Fig. 5. Two investment strategies based on moving averages techniques.

## Appendix A. A numerical illustration

Let consider again the basic price series {100,120,90,160,126, 150,140,160,110,170,168,180} and c=10% transaction costs (see Table A.4). In order to construct the bipartite graph, we <sup>fi</sup>rst slice p<sup>→</sup> into two subsets $\overrightarrow { f p _ { B } }$ and $\overrightarrow { f p _ { S } }$ as explained in Section 3.1 (see also Table A.3).

We compute the incidence matrix of in accordance with the <sup>N</sup>rules presented above (see page 7 and Table A.4). The absence of a trading edge between two vertices, due to violation of the constraint expressed in Eq. (3.9), is interpreted as a weight (or length) of size −∞. In this matrix, the absence of a transition edge due to the backward interdiction rule is denoted as −∞. Transition edges between $\overrightarrow { f p _ { S } }$ and $\overrightarrow { f p _ { B } }$ systematically receive a weight of 0. The graphical representation of $\overrightarrow { \mathcal { N } } \Big ( \overrightarrow { E } , \overrightarrow { f p _ { B } } , \overrightarrow { f p _ { S } } \Big )$ is proposed in Fig. A.6.

<table><tr><td> $\overline{\left\{ \begin{array}{cccccc} 1 & 3 & 5 & \overrightarrow{fp_{B}}_{7} & 9 & 11 \\ 100 & 90 & 126 & 140 & 110 & 168 \end{array} \right\}}$ </td></tr><tr><td> $\left\{ \begin{array}{cccccc} 2 & 4 & 6 & \overrightarrow{fp_{S}}_{8} & 10 & 12 \\ 120 & 160 & 150 & 160 & 170 & 180 \end{array} \right\}$ </td></tr></table>

Modi<sup>fi</sup>ed incidence matrix of for the S -determination with Floyd modi<sup>fi</sup>ed algorithm.

<table><tr><td></td><td>100</td><td>120</td><td>90</td><td>160</td><td>126</td><td>150</td><td>140</td><td>160</td><td>110</td><td>170</td><td>168</td><td>180</td></tr><tr><td>100</td><td> $-\infty$ </td><td> $-\infty$ </td><td>0</td><td>34</td><td>0</td><td>25</td><td>0</td><td>34</td><td>0</td><td>43</td><td>0</td><td>52</td></tr><tr><td>120</td><td> $-\infty$ </td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td></tr><tr><td>90</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td>45</td><td>0</td><td>36</td><td>0</td><td>45</td><td>0</td><td>54</td><td>0</td><td>63</td></tr><tr><td>160</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td></tr><tr><td>126</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td>0</td><td>5.4</td><td>0</td><td>14.4</td><td>0</td><td>23.4</td></tr><tr><td>150</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td></tr><tr><td>140</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td>8</td></tr><tr><td>160</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td></tr><tr><td>110</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td>32</td><td>0</td><td>41</td></tr><tr><td>170</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td>0</td><td> $-\infty$ </td></tr><tr><td>168</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td></tr><tr><td>180</td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td></tr></table>

<sup>N</sup>As it was mentioned above, the S -determination problem can be formulated in graph theory framework. The special distinguishing feature of this graph is that its nodes can be linearized as it shown in the Fig. A.7. We can <sup>fi</sup>nd the longest path from s to t, that represents the optimal solution, by comparing the paths (Algorithm 3):

![](/api/attachments/DF6N3S4R/fulltext/images/b199097cf5bb839fceb7e02c4a791deb43c939ab6c96a6ab93c372d827abafa3.jpg)

Algorithm 3. DAG longest path algorithm on the initial price series in Table A.3

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$l(s) = 0$ $l(100) = -\infty$ $l(100) = \max\{l(100), R(s, 100)\} = \max\{-\infty, 0\} = 0$ $l(120) = -\infty$ $l(90) = -\infty$ $l(90) = \max\{l(90), R(s, 90)\} = \max\{-\infty, 0\} = 0$ $l_1(160) = -\infty$ $l_1(160) = \max\{l_1(160), l(100) + R_1(100, 160), l(90) + R_1(90, 160)\}$ $= \max\{-\infty, 34, 45\} = 45$ $l(126) = -\infty$ $l(126) = \max\{l(126), R(s, 126), l_1(160) + R(160, 126)\} = \max\{-\infty, 0, 45\} = 45$ $l(150) = -\infty$ $l(150) = \max\{l(150), l(100) + R(100, 150), l(90) + R(90, 150)\}$ $= \max\{-\infty, 25, 36\} = 36$ $l(140) = -\infty$ $l(140) = \max\{l(140), R(s, 140), l_1(160) + R(160, 140), l(150) + R(150, 140)\}$ $= \max\{-\infty, 0, 45, 36\} = 45$ $l_2(160) = \max\{l_2(160), l(100) + R_2(100, 160), l(90) + R_2(90, 160), l(126) + R(126, 160)\} = \max\{-\infty, 35, 45, 50, 4\} = 50.4$ $l(110) = -\infty$ $l(110) = \max\{l(110), R(s, 110), l_1(160) + R_1(160, 110), l(150) + R(150, 110), l_2(160) + R_2(160, 110)\}$ $= \max\{-\infty, 0, 45, 36, 50.4\} = 50.4$ $l(170) = \max\{l(170), l(100) + R(100, 170), l(90) + R(90, 170), l(126) + R(126, 170), l(110) + R(110, 170)\}$ $= \max\{-\infty, 43, 54, 59.4, 82.4\} = 82.4$ $l(168) = -\infty$ $l(168) = \max\{l(168), R(s, 168), l_1(160) + R_1(160, 168), l(150) + R(150, 168), l_2(160) + R_2(160, 168), l(170) + R(170, 168)\}$ $= \max\{-\infty, 0, 45, 36, 50.4, 82.4\} = 82.4$ $l(180) = -\infty$ $l(180) = \max\{l(180), l(100) + R(100, 180), l(90) + R(90, 180), l(126) + R(126, 180), l(140) + R(140, 180), l(110) + R(110, 180)\}$ $= \max\{-\infty, 52, 63, 68.4, 53, 91.4\} = 91.4$ $l(t) = -\infty$ $l(t) = \max\{l(t), l_1(160) + R_1(160, t), l(150) + R(150, t), l_2(160) + R_2(160, t), l(170) + R(170, t), l(180) + R(180, t)\}$ $= \max\{-\infty, 45, 36, 50.4, 82.4, 91.4\} = 91.4$
</div>

Fig. A.6. Bipartite network from the incidence matrix.  
![](/api/attachments/DF6N3S4R/fulltext/images/3c7fefcb5fdccc097189dbb5a63c1fda5085d5fbf2cf89bcf57a349009baa2f7.jpg)  
Fig. A.7. A DAG and its topological ordering. Dummy source s and dummy sink t are separated in order to distinguish them.

## References

[1] P. Beraldi, A. Violi, F.D. Simone, A decision support system for strategic asset allocation, Decision Support Systems 51 (2011) 549–561.

[2] A.S. Chen, M.T. Leung, Regression neural network for error correction in foreign exchange forecasting and trading, Computers and Operations Research 31 (2004) 1049–1068.

[3] A.S. Chen, M.T. Leung, H. Daouk, Application of neural networks to an emerging <sup>fi</sup>nancial market: forecasting and trading the Taiwan stock index, Computers and Operations Research 30 (2003) 901–923.

[4] G. Dantzig, All Shortest Routes in a Graph, in: Theory of Graphs, International Symposium, Rome, Gordon and Breach, New York, 1966, pp. 91–92.

[5] E. Dijkstra, A note on two problems in connection with graphs, Numerische Mathematik 1 (1959) 269–271.

[6] E.J. Elton, M.J. Gruber, C.R. Blake, The persistence of risk-adjusted mutual fund performance, Journal of Business 69 (1996) 133–157.

[7] R. Floyd, Algorithm 97, shortest path algorithms, Operations Research 17 (1969) 395–412.

[8] M.R. Garey, D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, W.H. Freeman, 1979.

[9] W. Huang, Y. Nakamori, S.Y. Wang, Forecasting stock market movement direction with support vector machine, Computers and Operations Research 32 (2005) 2513–2522.

[10] M.C. Jensen, The performance of mutual funds in the period, Journal of Finance 23 (1968) 389–416.

[11] M. Lam, Neural network techniques for <sup>fi</sup>nancial performance prediction: integrating fundamental and technical analysis, Decision Support Systems 37 (2004) 567–581.

[12] W. Leigh, N. Modani, R. Hightower, A computational implementation of stock charting: abrupt volume increase as signal for movement in New York stock exchange composite index, Decision Support Systems 37 (2004) 515–530.

[13] Y. Liu, X. Wu, F. Hao, A new chance-variance optimization criterion for portfolio selection in uncertain decision systems, Expert Systems with Applications 39 (2012) 6514–6526.

[14] B. Malkiel, Can predictable patterns in market returns be exploited using real money? Journal of Port<sup>fl</sup>io Management 30 (2004) 131–141.

[15] L. Motiwalla, M. Wahab, Predictable variation and pro<sup>fi</sup>table trading of us equities: a trading simulation using neural networks, Computers and Operations Research 27 (2000) 1111–1129.

[16] C. Papadimitriou, K. Steigleitz, Combinatorial Optimization: Algorithms and Complexity, Dover Publications, Inc., Mineola. New York, 1998.

[17] J.Y. Potvin, P. Soriano, M. Vallée, Generating trading rules on the stock markets with genetic programming, Computers and Operations Research 31 (2004) 1033–1047.

[18] R. Sedgewick, K. Wayne, Algorithms, fourth edition Pearson Education, Inc., 2011.

[19] W.F. Sharpe, The arithmetic of active management, The Financial Analysts' Journal 47 (1991) 7–9.

[20] L. Shen, H.T. Loh, Applying rough sets to market timing decisions, Decision Support Systems 37 (2004) 583–597.

[21] D. Shier, Iterative methods for determining the k shortest paths in a network, Networks 6 (1973) 205–230.

[22] D. Shier, A computational study of Floyd's algorithm, Computers and Operations Research 8 (1981) 275–293.

Olivier Brandouy is Professor of Finance at Université Paris 1 Panthéon Sorbonne (IAE de Paris). His research are focused on computational <sup>fi</sup>nance and portfolio management.

Philippe Mathieu is Professor of Computer Science at Université Lille 1. His expertise is in Arti<sup>fi</sup>cial Intelligence and agent-based methods.

Iryna Veryzhenko an Assistant Professor of Finance at ESSCA School of Management. She works in quantitative and computational <sup>fi</sup>nance.
