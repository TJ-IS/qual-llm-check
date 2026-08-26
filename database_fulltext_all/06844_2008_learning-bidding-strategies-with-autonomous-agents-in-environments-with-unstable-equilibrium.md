---
otero_id: 6844
otero_key: "G3YAH8PY"
title: "Learning bidding strategies with autonomous agents in environments with unstable equilibrium"
authors: "Riyaz T. Sikora; Vishal Sachdev"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.05.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Learning bidding strategies with autonomous agents in environments with unstable equilibrium<sup>☆</sup>

Riyaz T. Sikora ⁎, Vishal Sachdev

Department of Information Systems, College of Business, University of Texas at Arlington, P.O. Box 19437, Arlington, TX 76019, United States

## a r t i c l e i n f o

Article history: Received 19 July 2006 Received in revised form 6 May 2008 Accepted 26 May 2008 Available online 2 July 2008

Keywords: Strategic interactions Automated agents Reinforcement learning Evolutionary learning Bidding strategies Unstable equilibrium

## a b s t r a c t

The role of automated agents for decision support in the electronic marketplace has been growing steadily and has been attracting a lot of research from the arti<sup>fi</sup>cial intelligence community as well as from economists. In this paper, we study the ef<sup>fi</sup>cacy of using automated agents for learning bidding strategies in contexts of strategic interaction involving multiple sellers in reverse auctions. Standard game-theoretic analysis of the problem assumes completely rational and omniscient agents to derive Nash equilibrium seller policy. Most of the literature on use of learning agents uses convergence to Nash equilibrium as the validating criterion. In this paper, we consider a problem where the Nash equilibrium is unstable and hence not useful as an evaluation criterion. Instead, we propose that agents should be able to learn the optimal or best response strategies when they exist (rational behavior) and should demonstrate low variance in pro<sup>fi</sup>ts (convergence). We present rationally bounded, evolutionary and reinforcement learning agents that learn these desirable properties of rational behavior and convergence.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

The role of automated agents for decision support in the electronic marketplace has been growing steadily and has been attracting a lot of research from the arti<sup>fi</sup>cial intelligence community as well as from economists [33]. The auction mechanism studied in this paper, the reverse auction, is very commonly used by companies while sourcing. With the advent of e-commerce, a lot of companies are using online exchanges or e-marketplaces to meet their requirements, though the auctions may be conducted manually. Industry observers have identi<sup>fi</sup>ed a growing trend among Original Equipment Designers (OEDs) and Electronic Manufacturing Service (EMS) providers conducting online procurement through reverse auctions. For example, Dell Computer Corp.

has broadened its online procurement to include commodity parts such as capacitors and resistors. Sun is now using reverse auctions with its EMS providers. It awards not just printed circuit board assemblies, but entire systems, including servers and mass storage units, to contract manufacturers through reverse auctions [7]. A joint study by the Institute for Supply Management, Tempe, Ariz. and Forrester Research Inc., Cambridge, Mass., found that 72% of the organizations that buy more than \$100 million a year used online procurement.

E-marketplaces were initially developed with the objective of facilitating information exchange among buyers and sellers and allowing more of them to interact with one another. Though the kinds of services have proliferated, human intervention is still required to complete these transactions [16]. Automating these auctions, which may involve customizable products, requires intelligent agents programmed with multiple constraints from the buyers' perspective and the ability to handle interactions with constrained seller agents [11]. Adding learning capabilities to these automated agents would considerably increase their potential for practical use, especially in domains that involve repeated auctions. The reverse auctions involving OEDs and EMS providers are examples of such repeated auctions. Suppliers who take part in these auctions could bene<sup>fi</sup>t from the use of intelligent agents that can learn better bidding strategies over time.

Another domain that involves repeated auctions and can make use of automated learning agents is the electricity market. With the increasing trend towards electricity deregulation in markets across the world, simulating electricity markets before implementing them is a useful evaluation criterion. For example, Nicolaisen et al. [24] use a modi<sup>fi</sup>ed Roth-Erev algorithm [13] to implement learning agents for electricity markets with discriminatory double-auction. Richter and Sheble [26] use genetic algorithms to simulate multiple generating companies (sellers) with a single distribution company (buyer). The buyer bids a constant amount in each round with the sellers evolving strategies over successive generations, which is quite similar to the framework presented in this paper. In a re-<sup>fi</sup>nement to their work, Richter et al. [27] propose a combination of genetic algorithms with data structures that combine genetic programming and <sup>fi</sup>nite state automata, to develop adaptive strategies. Several studies [9,20,36,30] have dealt with learning strategies in repeated auctions, such as the California-type dayahead markets, where a series of 24 hourly auctions are continuously conducted everyday. Such auctions are analogous in structure to in<sup>fi</sup>nitely repeated games, a scenario for which the learning capabilities of agents presented in this paper are eminently suitable.

Autonomous trading agents have also been gaining in popularity. Although they have been around for many years, they are now becoming far more sophisticated, and make trades worth tens of billions of dollars every day. In equity markets, where they are used to buy and sell shares, they already appear to be outperforming their human counterparts [12]. Kephart et al. [17] argue that economically motivated software agents can be independent and equipped with algorithms to interact with humans or other agents to maximize utility on behalf of the humans they represent. In a subsequent publication, Kephart [16] presents results of experiments pitting humans against agents programmed with algorithms, demonstrating that agents consistently outperform humans in a multiunit continuous double auction.

In this paper, we consider the problem of homogeneous sellers of a single raw material or component vying for business from a single large buyer, and present arti<sup>fi</sup>cial agents that learn increasingly effective seller strategies. Standard game-theoretic analysis of the problem assumes completely rational and omniscient agents to derive the Nash equilibrium seller policy. Most of the literature on the use of intelligent agents in strategic interactions focuses on validating the effectiveness of the agents by showing agent behavior converging to Nash equilibrium. For example, Kimbrough et al. [19] present experiments to test whether arti<sup>fi</sup>cial agents can <sup>fi</sup>nd good ordering strategies for the supply chain, in both stationary and non-stationary environments in the famous ‘Beer Game’ problem. They conclude that arti<sup>fi</sup>cial agents <sup>fi</sup>nd optimal solutions that are also Nash equilibria. Jafari [15] shows that the outcome of multi-agent learning in repeated games using ‘no-regret’ algorithms is a Nash equilibrium in constant-sum and general-sum 2×2 games. Reeves et al. [25] consider evolutionary search methods to devise bidding strategies for agents participating in market-based scheduling of a resource and show that in a restricted set of cases, the strategies converge to the Nash equilibrium. However, we show that in our problem such an equilibrium is unstable, and therefore cannot be considered a solution. Instead, we propose the two desirable properties of rational behavior and convergence that the agents should exhibit as a means of evaluating their performance. We demonstrate rational behavior by showing the agents learning optimal or best response strategies when they exist. We show convergence by showing low variance in pro<sup>fi</sup>ts when the agents are playing against each other.

A game of strategic interaction involving multiple agents is in effect a problem of learning a “moving target.” Since the other agent in our problem is also adapting, the “best response” or the optimal policy may be changing as the agent is learning. Compounding this problem is the fact that in real world scenarios involving such strategic interactions we will not know what learning strategies the other agents are using. To address this problem of validating the effectiveness of any learning agent, we design a small group of learning agents using various learning algorithms and test their performance by playing them against each other. Since our main goal is to study the effectiveness of very simple learning agents, all the agents in our study are rationally bounded with incomplete information. This work has the potential to be used in automating bidding agents in online procurement auctions. One of the important contributions of the paper is in showing the ef<sup>fi</sup>cacy of using very simple learning agents in an unstable domain. Although the learning agents that we present are very simple, in real applications the agents might be designed with more domainspeci<sup>fi</sup>c knowledge built in.

The rest of the paper is organized as follows. The ensuing section de<sup>fi</sup>nes the problem for the game of reverse auction considered in this study, followed by some analytical results that demonstrate why the problem is dif<sup>fi</sup>cult. Next, we discuss the design of evolutionary and reinforcement learning agents that can learn better bidding strategies. The results of the experiments playing the agents against each other are then presented. Subsequently, we modify the agents to make them more <sup>fl</sup>exible in learning ef<sup>fi</sup>cient bidding strategies and show the improvement in performance for all the agents. The paper concludes with some directions for future research.

## 2. Problem de<sup>fi</sup>nition

We consider a modi<sup>fi</sup>ed version of the problem presented by Bandyopadhyay et al. [5,6]. The problem involves 2 homogeneous sellers x and y, each with production capacity of k and a variable cost of c, vying for business from a single buyer with a reserve price of r and a total demand of Q such that the following two conditions are satis<sup>fi</sup>ed: $Q { > } k$ and $2 k { > } Q .$ The seller bidding the lowest price sells to capacity with the residual demand going to the seller with the higherbid. Bandyopadhyay et al. [5,6] and others have shown that there is no pure Nash equilibrium for this problem. They also show that sellers should not bid below a certain price point $p { > } c ,$ given by

$$
p = c + \frac {(r - c) (Q - k)}{k}\tag{1}
$$

The mixed strategy equilibrium in terms of a probability density function over the continuous price range [p, r] is given by:

$$
F (g) = \frac {(g - c) k - (r - c) (Q - k)}{(g - c) (2 k - Q)}.\tag{2}
$$

Using the above CDF, one can derive the Nash payoff $( \mathrm { i . e . , }$ the expected payoff if both the players are at Nash) given by:

$$
\text { Nash   payoff } = \frac {(r - c) (r - p) (Q - k) ^ {2}}{(2 k - Q) (p - c)}.\tag{2.5}
$$

We modify the above problem in two ways. Our motivation in this paper is to study whether rationally bounded agents with incomplete information can learn effective bidding strategies. We do not make the assumption that the sellers know anything about each other (i.e., the existence of other sellers or their capacity). So, the effective price range in which the sellers can bid pro<sup>fi</sup>tably in our formulation is [c, r]. The problem becomes intractable if an agent has to learn a continuous distribution. Moreover, since the density function has a zero point mass, an agent cannot apply it in determining a precise price bid. It is therefore reasonable to assume that a bidding agent considers price bands or intervals when trying to learn an effective bidding strategy. There is also support for the use of price bands in the literature [8,10]. We modify the problem by splitting the effective price range [c, r] into n equally sized price bands. The problem can now be analyzed as a discrete two-player symmetric game with n actions available to each player. Each action involves selecting a bid price from the respective price band with a uniform distribution. Introduction of price bands fundamentally changes the problem and the cumulative probability density function for the mixed strategy equilibrium presented in Bandyopadhyay et al. [5,6] no longer applies.

Using notations from standard game theory, the expected pro<sup>fi</sup>t for both the sellers can be represented in an n×n payoff matrix, where the sellers are represented as row and column players. Let A be the n×n payoff matrix for seller x, assuming that x is the row player. Note that since this is a symmetric game, the payoff matrix for the column player y will be A<sup>T</sup>. For illustration purposes, consider the problem with the following values: Q=100, k=65, c=40, and r=80. We consider n= 10, so the price bands are [40, 44], [44, 48], … [76, 80]. It is straightforward to calculate the non-diagonal values of the payoff matrix. For example, a =expected pro<sup>fi</sup>t for seller x bidding in the price range [60, 64] playing against seller y bidding in the price range [64, $6 8 ] = ( 6 2 - c ) \times k = 1 4 3 0$

For the diagonal elements of the matrix, the payoff is given as follows:

a =expected pro<sup>fi</sup>t for seller x bidding in the price band i, playing against seller y bidding in the same price band i. =E[ (pro<sup>fi</sup>t for seller x | x's bid N y's bid). Pr(x's bid N y's bid) + (pro<sup>fi</sup>t for seller x | x's bid b y's bid) . Pr(x's bid b y's bid) ]. Formally,

$$
\begin{array}{l} a _ {i, i} = \int_ {g = l _ {i}} ^ {u _ {i}} \int_ {h = l _ {i}} ^ {g} \frac {(Q - K) (g - c)}{(u _ {i} - l _ {i}) ^ {2}} d g d h \\ + \int_ {g = l _ {i}} ^ {u _ {i}} \int_ {h = g} ^ {u _ {i}} \frac {K (g - c)}{(u _ {i} - l _ {i}) ^ {2}} d g d h \end{array}\tag{3}
$$

where $[ l _ { i } , u _ { i } ]$ is the price band i:

The values of the 10 ×10 payoff matrix are given in the appendix. It is clear from the payoff matrix that the pure strategies, 1 through 5, are strictly dominated. From the remaining 5×5 payoff matrix for strategies 6 to 10, it is also clear that there is no pure strategy Nash equilibrium. Therefore, we need to <sup>fi</sup>nd the Nash equilibrium in mixed strategies.

The following notation for mixed strategies and their utilities will be used throughout the paper. Let x and y be the mixed strategies of players x and y, given by an n×1 vector of probabilities, where x and $y _ { i }$ are the probabilities of taking action i for players x and y respectively. Note that

$$
\sum_ {i = 1} ^ {n} x _ {i} = 1, \text {   and   } \sum_ {i = 1} ^ {n} y _ {i} = 1.\tag{4}
$$

Let a pure strategy of playing action i be denoted by $\mathbf { e _ { i } } ,$ a n×1 vector with a 1 at position i and 0 every where else. Note that any strategy x is a convex combination of the pure strategies, i.e.,

$$
\mathbf {x} = \sum_ {i} x _ {i} \mathbf {e} _ {\mathrm{i}}.\tag{5}
$$

Let $U _ { \mathbf { x } / \mathbf { y } }$ denote the expected utility or payoff of playing strategy x against strategy y. Let $U _ { \mathbf { i } / \mathbf { y } }$ denote the expected utility or payoff of playing pure strategy e<sub>i</sub> against strategy y. It follows that,

$$
U _ {x / y} = \mathbf {x} ^ {T} \mathbf {A} \mathbf {y}
$$

$$
U _ {i / y} = (\mathbf {A} \mathbf {y}) _ {i}.\tag{6}
$$

ð<sup>7</sup>Þ

Combining the above equations we get,

$$
U _ {x / y} = \sum_ {i} x _ {i} U _ {i / y}\tag{8}
$$

i.e., $U _ { \mathbf { x } / \mathbf { y } }$ is a convex linear combination of $U _ { \mathbf { i } / \mathbf { y } }$

Let $( \mathbf { x } ^ { * } , \mathbf { y } ^ { * } )$ be the Nash equilibrium. By de<sup>fi</sup>nition, $\mathbf { x } ^ { * }$ is the best response to $\mathbf { y } ^ { * }$ and vice versa. In other words,

$$
U _ {x ^ {*} / y ^ {*}} \geq U _ {x / y ^ {*}} \forall \mathbf {x}.\tag{9}
$$

From Eq. (8) above we also get

$$
U _ {x ^ {*} / y ^ {*}} \leq U _ {i / y ^ {*}} \forall \mathbf {e} _ {\mathbf {i}}, i = 1, \dots n.\tag{10}
$$

The only way the above two inequalities can be satis<sup>fi</sup>ed is if they are equalities. In other words, any strategy (including pure strategy) receives the same payoff playing against the Nash equilibrium. Formally,

$$
U _ {i / y ^ {*}} = U _ {j / y ^ {*}} \forall \mathbf {e} _ {\mathrm{i}}, \mathbf {e} _ {\mathrm{j}} i \neq j\tag{11}
$$

From Eqs. (7) and (11), it follows that

$$
\left(\mathbf {A} \mathbf {y} ^ {*}\right) _ {i} = \left(\mathbf {A} \mathbf {y} ^ {*}\right) _ {j} \forall i \neq j.\tag{12}
$$

Solving the above set of linear equations, we get the unique Nash equilibrium $\mathbf { y } ^ { * }$ . Note that, by the same argument we can <sup>fi</sup>nd $\mathbf { x } ^ { * }$ , and since the problem is symmetric, both $\mathbf { x } ^ { * }$ and $\mathbf { y } ^ { * }$ will be the same. The values of the unique Nash equilibrium strategy for the above problem are reported in the appendix. These values are different from the ones obtained using the Nash equilibrium formula given in Eq. (2), since we have altered the problem by introducing price bands. Plugging the values of the Nash equilibrium mixed strategy in Eq. (12) above yields the payoff of any strategy playing against the Nash at u=1344.80. We will refer to this as the Nash payoff throughout the paper. Note that the Nash payoff for the original problem given by the Eq. (2.5) is 1400.

One of the criticisms of (classical) game theory that has been raised by many [4,18] is that it focuses mainly on statics (i.e. equilibria) rather than on the dynamics. Even though the concept of Nash equilibrium is in itself an important one, it does not say anything about how agents arrive at such an equilibrium, especially if the agents are rationally bounded. More importantly, the concept of equilibrium has little relevance to the behavior of realistic agents if it is: a) not attainable by boundedly rational agents; b) obtained asymptotically but not realized over long periods; or c) unstable [4]. For our study, we will focus on the last point. Stability is an important concept that has been extensively studied in the context of complex systems [35]. An equilibrium point is said to be stable if, when the state is moved slightly away from that point, it tends to return to it (asymptotic stability) or does not keep moving further away (Liapunov stability) [21].

We empirically demonstrate the instability of the above Nash equilibrium. To do so, we use the concept of replicator dynamics (RD) from evolutionary game theory [34]. RD studies the dynamics of a population of pure strategies that replicates based on its payoff. The state of the population at any time can be interpreted as a mixed strategy learned by the population. The component $x _ { \mathrm { i } }$ of the strategy x is simply given by the proportion of individuals in the population who are playing the pure strategy e . At each generation, every strategy in the population plays against all strategies in the population (including itself) and the resulting payoff it receives is its <sup>fi</sup>tness. Strategies breed true from one generation to the next and they breed in proportion to their <sup>fi</sup>tness. One can therefore analyze RD as a set of difference equations.

Let N be the total number of pure strategies in the population and n be the number of pure strategies $\mathbf { e _ { i \cdot } }$ It follows that

$$
\sum_ {i = 1} ^ {n} n _ {i} = N.\tag{13}
$$

Let $U _ { i }$ be the expected average payoff for pure strategy e playing against the entire population. Using Eqs. (6) and (8), it follows that

$$
U _ {i} = \frac {\sum_ {j = 1} ^ {n} U _ {i / j} n _ {j}}{N} = \sum_ {j = 1} ^ {n} U _ {i / j} x _ {j} = \sum_ {j = 1} ^ {n} \left(\mathbf {e} _ {\mathrm{i}} ^ {\mathrm{T}} \mathbf {A e} _ {\mathrm{j}}\right) x _ {j} = (\mathbf {A x}) _ {i}.\tag{14}
$$

If the individual pure strategies in the population replicate proportional to their expected payoff, then the number of pure strategy $\mathbf { e _ { i } }$ at the next time period is given by:

$$
n _ {i} ^ {t + 1} = \frac {U _ {i} ^ {t} n _ {i} ^ {t}}{\sum_ {j} U _ {j} ^ {t} n _ {j} ^ {t}} N\tag{15}
$$

where t is the superscript for the time period. Dividing the above equation by the population size N, we get the following for the state of the population at the next time period, if its state at time t is represented by the mixed strategy ${ \bf x } ^ { t } .$

$$
x _ {i} ^ {t + 1} = \frac {U _ {i} ^ {t} x _ {i} ^ {t}}{\sum_ {j} U _ {j} ^ {t} x _ {j} ^ {t}} = \frac {\left(\mathbf {A x} ^ {t}\right) _ {i}}{\mathbf {x} ^ {t ^ {\mathrm{T}}} \mathbf {A x} ^ {t}}   x _ {i} ^ {t}   \forall i = 1, \ldots n.\tag{16}
$$

Note that the denominator in the above equation is the payoff that strategy x receives playing against itself, which is same as the average payoff of the population. The numerator of the co-ef<sup>fi</sup>cient is the payoff of pure strategy $\mathbf { e _ { i } }$ playing against the strategy x (i.e., average payoff of $\mathbf { e _ { i } }$ playing against the entire population). From the above equation, it is clear that the proportion of a pure strategy in the population will increase if its payoff is more than the average payoff of the population. If x were x<sup>⁎</sup> (i.e., Nash), then it follows that

$$
x _ {i} ^ {t + 1} = x _ {i} ^ {t} \quad \forall i = 1, \dots n.\tag{17}
$$

Once the population reaches a state that represents the mixed-strategy Nash equilibrium, then the proportion of all pure strategies in the population will no longer change. Treating the above equation as a set of iterative equations, one can plot the n components of the strategy represented by the population from one time period to the next. Using the values of the payoff matrix A and the Nash equilibrium $\mathbf { x } ^ { * }$ from the appendix, we plot the values of the last <sup>fi</sup>ve components of the mixed strategy (since ${ { \chi } _ { 6 } } \mathrm { - } { { \chi } _ { 1 0 } }$ are the only non-zero components). If we use the actual Nash values, reported in the appendix, with a 64-bit double precision as the initial values of the mixed strategy components, the proportions stay the same from one time period to the next indicating an equilibrium state. To study the stability of the equilibrium, we simply perturb the initial values by rounding the Nash values to 6 decimal places. As shown in Fig. 1 the proportions oscillate and eventually move away from the Nash equilibrium, never to return. This shows that even a very small perturbation leads the system away from the Nash equilibrium.

Another concept from evolutionary game theory that is related to the stability of an equilibrium strategy is that of an evolutionary stable strategy (ESS), <sup>fi</sup>rst proposed by Maynard Smith [29]. In the context of evolutionary game theory, a strategy is ESS if an entire population consisting of the same strategy cannot be invaded by a group of any other mutant strategy. It has been shown that a strict Nash equilibrium strategy (i.e., a stable Nash equilibrium where a player making a small change away from the equilibrium becomes worse off) also implies an ESS [34]. In our case, we show that the unique mixed Nash equilibrium reported earlier in Eq. (11) is not an ESS.

Consider a population consisting of only Nash equilibrium strategies, $\mathbf { x } ^ { * } .$ Let a small set of mutant strategies m be introduced in the above population so that their proportion in the population is ε. The proportion of the mutant strategies in the bimorphic population (two distinct strategies present) will increase only if their average payoff (when playing against the entire population) is greater than the average payoff of the Nash strategy $\mathbf { x } ^ { * }$ in the population. Let $U _ { \mathbf { x } ^ { * } }$ and $U _ { \mathbf { m } }$ denote the average payoff received by the strategies $\mathbf { x } ^ { * }$ and m respectively. To show that $\mathbf { x } ^ { * }$ is not an ESS, we need to show that

![](/api/attachments/G3YAH8PY/fulltext/images/87d4a014810c20a8cc303d60a6c4b9b9413423e8afe40bc1063c82237ab394d2.jpg)  
Fig. 1. Mixed Strategy Components in RD Starting at Nash Values Rounded to 6 Decimals.

a m s:t: $U _ { x ^ { * } } < U _ { m }$

<sub>ð</sub><sup>18</sup><sub>Þ</sub>

From Eq. (11) we know that every strategy receives the same payoff playing against the Nash $\mathbf { \dot { x } } ^ { * }$ . In other words,

$$
U _ {\mathrm{x} / \mathrm{x} ^ {*}} = u \forall \mathrm{x}.\tag{19}
$$

The payoffs of the two strategies in the above bimorphic population is therefore given by

$$
\begin{array}{l} U _ {x ^ {*}} = \varepsilon U _ {x ^ {*} / m} + (1 - \varepsilon) U _ {x ^ {*} / x ^ {*}} = \varepsilon U _ {x ^ {*} / m} + (1 - \varepsilon) u \\ U _ {m} = \varepsilon U _ {m / m} + (1 - \varepsilon) U _ {m / x ^ {*}} = \varepsilon U _ {m / m} + (1 - \varepsilon) u \end{array} .\tag{20}
$$

Substituting Eq. (20) in Eq. (18) above, we get the condition for $\mathbf { x } ^ { * }$ not being an ESS as

a m s:t: $U _ { \mathrm { x ^ { * } / m } } < U _ { \mathrm { m / m } } .$

<sub>ð</sub><sup>21</sup><sub>Þ</sub>

From the values of the payoff matrix A given in the appendix it is easy to show that

$$
U _ {x ^ {*} / i} <   U _ {i / i} \quad \forall i = 6, \dots 1 0.\tag{22}
$$

For e.g., $U _ { \mathbf { x } ^ { * } / \mathbf { 6 } } = 1 0 5 0 . 8$ which is less than $U _ { \mathbf { 6 / 6 } } = 1 0 9 0$ . In other words, any of the <sup>fi</sup>ve pure strategies $\mathbf { e _ { i } } , i = 6 ,$ .. 10 can invade and take over a population of Nash strategies $\mathbf { x } ^ { * }$ . Note that the above conclusion does not even depend on the initial proportion ε of mutant strategies. Even a single copy of any of the above pure strategies can invade and take over a population of Nash equilibrium strategies. However, a population consisting of the same pure strategy is also not stable, as it cycles through a loop of pure strategies $\bf { e _ { 6 } }$ to $\bf { e _ { 1 0 } }$

To underscore the fact that the instability of the Nash equilibrium is not an artifact of the discretization of the problem, we performed a sensitivity analysis by varying the number of price bands (and hence varying their size). Even when we moved closer to the continuous problem space by doubling the number of price bands to 20, the system exhibited similar instability.

In contexts with stable Nash equilibrium we should expect learning agents to converge to the Nash equilibrium. Since the Nash equilibrium in our case has been shown to be unstable, a rationally bounded agent that is trying to maximize its payoff by learning from past payoffs will never be able to <sup>fi</sup>nd and stay at the Nash equilibrium. In such a situation, agent-based modeling provides a natural setting to study the dynamics of seller interactions, since game theoretic analysis doesn't shed any light on the dynamics. We use the aforementioned desirable properties of rational behavior and convergence to evaluate the agents' performance, and use the Nash payoff as a benchmark in comparing the effectiveness of the agents. In the next section, we present simple evolutionary and reinforcement learning agents for our problem and evaluate their performance.

## 3. Evolutionary and reinforcement learning agents

Genetic Algorithms (GAs) [14] combine survival of the <sup>fi</sup>ttest among string structures with a structured yet randomized information exchange to form a search algorithm. GAs have been used before in formation of strategies in dynamic ‘Prisoner's Dilemma’ games [3]. The use of GA as a mechanism for agent learning is popular in the Economics literature. Andreoni and Miller [1] used a two population GA to simulate human behavior in different types of auctions. Tesfatsion [32] uses GAs to enable trade bots to learn trade strategies in an iterated Prisoners dilemma game. Arifovic [2] uses GAs to model competitive behavior of <sup>fi</sup>rms in a single good market, where the algorithm updates the decision rules about production and sales in the next period. They contend that GAs exhibit behavior similar to those of experimental human subjects. A comprehensive discussion on the use of genetic algorithms in Economics can be found in Dawid [11]. GAs have also been used in optimizing other learning techniques, such as neural networks [28].

In our case, the GA implements a mixed strategy for the seller as an individual member of the population. Each population member is therefore a vector of probabilities for each action, that all add up to 1.0. Based on some initial set of experiment runs we chose the following operators and parameter values for the GA. We used tournament selection of size 2 as the selection operator, a standard one-point crossover operator, and a mutation operator where one value from the vector of probabilities for an individual is randomly changed by a small amount. When an operator creates an invalid strategy, i.e., whose probabilities do not add up to 1.0, we simply normalize the vector by dividing each probability value by the sum of probabilities. We used a population size of 30 and the probabilities of crossover and mutation as 0.7 and 0.1 respectively. The GA was run for 3000 generations. The evaluation of each population member is done by playing that strategy against another strategy. Each such game involves playing the two strategies against each other 10 times. The <sup>fi</sup>tness of each strategy is then calculated to be the average payoff from all such games.

Reinforcement learning (RL) methods involve learning what to do so as to maximize (future) payoffs. RL agents use trial and error in formulating the best actions (i.e., learning strategies) to take based on the past rewards received for different actions. Sutton and Barto (Sutton and Barto, 1998) provide an excellent overview of RL. RL methods have been extensively used in various contexts of strategic interaction. Moody and Saffell [23] present methods for optimizing portfolios, asset allocations, and trading systems based on direct reinforcement (DR). Instead of estimating value functions, the DR approach discovers strategies directly. In related work, Moody et al. [22] propose a generalization of the DR method called the Stochastic Direct Reinforcement (SDR) policy gradient algorithm. They incorporate the aspect of recurrent memory for policy gradient RL and demonstrate the superior performance of recurrent SDR and non-recurrent SDR players against Q-type learners for a variety of games.

All RL methods are based on estimating action-values $Q ( a ) - \mathrm { i } . \mathrm { e } .$ , the estimated reward for taking action a. In our problem each action for the seller agent corresponds to selecting a price band to bid. In our experiments we use the time-weighted method where the action value estimates are the weighted average of past observed rewards, with recent rewards getting a higher weight. If an action a has been taken k times in the past then the (k + 1)th estimate of the action-value will be given by the following:

$$
Q _ {k + 1} (a) = Q _ {k} (a) + \alpha [ r _ {k + 1} (a) - Q _ {k} (a) ]\tag{23}
$$

where $r _ { i } ( a )$ is the actual reward received when taking action a for the ith time, and α is the learning rate. Note that the RL agent has to keep track of only $Q _ { k }$ for each action.

There are several action-selection methods that an RL agent can use in deciding the next action to take based on the estimated action-values. Each method assigns a probability distribution over the actions based on the estimated actionvalues. The probability distribution assigned by the actionselection methods can be considered the mixed strategy learned by the RL agent. We consider the Sample Average, ε- Greedy and Softmax action-selection methods [31]. In sample average, the probabilities for the actions are simply proportional to their action-values. In ε-greedy, the best action is taken most of the time (i.e., with probability $1 - \varepsilon )$ , but with a small probability (ε) any of the remaining actions are chosen randomly. Softmax uses a Gibbs or Boltzmann distribution. The three probability distribution functions are respectively given below.

$$
\operatorname * {P r} (a) = \frac {Q (a)}{\sum_ {i = 1} ^ {n}} Q (i)\tag{24}
$$

$$
\begin{array}{l l} \operatorname * {P r} (a) = (1 - \varepsilon) & \text { if } a = \arg \max _ {i} (Q (i)) \\ = \frac {\varepsilon}{n - 1} & \text { else } \end{array}\tag{25}
$$

$$
\operatorname * {P r} (a) = \frac {e ^ {Q (a) / \tau}}{\sum_ {i = 1} ^ {n} e ^ {Q (i) / \tau}} \quad \text { where } \tau > 0.\tag{26}
$$

All the RL methods are biased by their initial estimates of $Q _ { 0 } .$ . However, for the time-weighted average action-value method that we use, this bias decreases over time and eventually disappears. The initial action value can still be useful in encouraging exploration in the beginning if they are selected optimistically. For all our experiments, we therefore use an optimistic initial value of $\scriptstyle Q _ { 0 } = 2 0 0 0$ since the maximum pro<sup>fi</sup>t an agent can make is \$2600. For the Softmax method the parameter $\tau$ is known as temperature. At higher temperatures the method becomes a random search with all the actions selected equiprobably. At very low temperatures the method approaches a greedy search where it always selects the best action. Ideally in a static environment, the Softmax method should start out with a high temperature value so that it can explore all the actions, but over time it should slowly reduce the temperature so that it can exploit the best actions learned. Our problem environment is however not static since it involves strategic interaction between two players. The best action for an agent at any given time depends on the action taken by the other agent. and that requires an agent to constantly explore for better actions even as it exploits the current best action. Since the optimistic choice for $Q _ { O }$ already encourages exploration in the beginning, we need to select a value of τ that can strike a proper balance between exploration and exploitation at all times. We ran experiments with three values for $\tau = 5 ,$ , 50, and 500 that each differ by an order of magnitude, and found that $\tau = 5 0$ provided the best tradeoff. For the ε-Greedy method we use a value of $\varepsilon { = } 0 . 1$ . The value of ε should be large enough to allow for some exploration in each game. Since each game in our design includes 10 interactions between the two sellers, using a value of $\varepsilon { = } 0 . 1$ ensures that, on average, a non-greedy action will be explored by the method once during a game. Henceforth, we will refer to our ε-Greedy method as 0.1Greedy.

All the above learning agents were implemented in Java J2SE 1.4.2. The iterations are successive rounds of interactions between the agents. Each iteration involves the execution of the strategies selected by the agents against each other. Both the sellers determine their bid using their respective strategies and the seller bidding the lowest price sells to capacity with the residual demand going to the seller with the higher-bid. Both sellers calculate and report their pro<sup>fi</sup>ts (i.e., rewards) and update their respective strategies at the end of each iteration. For the GA agent playing against an RL agent, each iteration involves each member of the GA population playing against the RL agent. After each iteration, RL agents update their action value estimates using Eq. (23) and then update the action probabilities using either Eqs. (25) or (26). For the GA agent, updating the strategies after each iteration involves applying the genetic operators and creating a new population of strategies.

## 4. Experiment results and discussion

As mentioned earlier, the ability of learning agents to <sup>fi</sup>nd the Nash equilibrium has been the sine qua non for validating and justifying their use. Since the Nash equilibrium in our case has been shown to be unstable, we use the two desirable properties of rational behavior and convergence that the agents should exhibit as a means of evaluating their performance. We demonstrate rational behavior by showing the agents learning optimal or best response strategies when they exist. We show convergence by showing low variance in pro<sup>fi</sup>ts when the agents are playing against each other.

To test whether the agents exhibit rational behavior, we have the learning agents play against a pure strategy to see whether they can learn known optimal strategies. We choose pure strategies $\mathbf { e } _ { 6 }$ and ${ \bf e } _ { 1 0 }$ for the test, i.e., pure strategies bidding in the price range [60, 64] and [76, 80]. From the payoff matrix A given in appendix, it is clear that the best response to $\mathbf { e } _ { 6 } \mathrm { i } s \mathbf { e } _ { 1 0 } \mathrm { i } . \mathbf { e } _ { \cdot _ { 1 } }$ , to bid in the price range [76, 80] which returns an expected payoff of \$1330, and the best response to $\mathbf { e } _ { 1 0 } \mathrm { i } s \mathbf { e } _ { 9 } \mathrm { i } . \mathbf { e } .$ to bid in the next lower price band [72, 76] which returns an expected payoff of \$2210. Figs. 2 and 3 show the results of playing the learning agents against the pure strategies mentioned above. All the results are averages of 10 different runs using different random seeds. All the learning agents, except for Sample Average, learn the appropriate best response in both cases as their payoffs converge to the optimal expected payoff. Since Sample Average method of action selection does not exhibit rational behavior, we drop it from further consideration. Note that the RL agents using Softmax and 0.1Greedy are faster in learning than the GA, since they explore all the actions early on and start exploiting the best response. By their very de<sup>fi</sup>nition, both Softmax and 0.1Greedy tend to perform best when learning pure strategies. Since the Boltzmann distribution in Softmax uses an exponential function, it becomes highly discriminatory towards the price band with higher payoff. In contrast, the Sample Average method can never learn a pure strategy when multiple actions receive nonzero payoff. The 0.1Greedy RL agent has more variance than either Softmax or GA. This is expected as, by de<sup>fi</sup>nition, a 0.1Greedy agent can only bid from the best response price band with a probability of 0.9 and bids randomly from other price bands the rest of the time.

In the second set of experiments we test the agents for convergence properties. We do this by playing a learning agent not only against itself (self-play) but also against the other agents. This is meant to provide robustness to the results since in reality we cannot assume what learning strategy the other player may be using. Ideally, we would like the agents to have consistent and good convergence properties playing against all types of agents. As before, each experiment involves 3000 iterations. We repeat the experiments 10 times with different random number seeds and all the results reported are averages of the 10 runs. To study the convergence properties of the agents, we look at the variance in pro<sup>fi</sup>ts and policies during the last 1000 iterations of the experiments, assuming that the agents had enough time in the <sup>fi</sup>rst 2000 iterations to learn. We study the dynamics of agent learning in the policy space by looking at the Euclidean distance<sup>1</sup> between the policy learned by the agent and the Nash equilibrium policy. The smaller the distance the closer the policies are to the Nash. Note that the pure strategies form the vertices of the 10-dimensional policy space and the maximum distance between any two points in the policy space is the distance between the vertices, which is fififi2<sup>p</sup> or 1.414. We also study how the learning agents perform when playing against the stationary Nash policy.

![](/api/attachments/G3YAH8PY/fulltext/images/78301e4a694009ef30e910b55011bdae7f614aad23c7585921742b15c94a6afb.jpg)  
Fig. 2. Playing against the pure strategy e .

![](/api/attachments/G3YAH8PY/fulltext/images/8ad2ab31bcd6d4ee5227d14dd92f766896aae6e87730131953fcecc490a541bc.jpg)  
Fig. 3. Playing against the pure strategy e<sub>10</sub>.

Tables 1–4 present the results of this set of experiments. They give the average value for the pro<sup>fi</sup>t and the distance of the Nash policy from the policy learned together with the standard deviation. All the results for the GA-based agent are presented taking an agent-centric view of the GA, where the GA is considered to represent one strategy that is the average of its population.

The GA-based agent consistently shows the best convergence properties. It has the smallest variance in pro<sup>fi</sup>t playing against all types of agents. The policies it learns also have the smallest variance and are closer to Nash than those learned by the other agents. The RL agents in contrast, have inconsistent results. RL agents exhibit better rational behavior and are faster in learning. However, they have the largest variance in pro<sup>fi</sup>ts playing against the RL agents. The policies learned by the RL agents also display higher variance. Interestingly, all agents realize excellent pro<sup>fi</sup>t convergence playing against the GA. The Nash policy also has inconsistent performance playing against the other three agents. It has a high variance in pro<sup>fi</sup>t playing against both the

## Table 1

Performance of GA playing against others

<table><tr><td rowspan="2">Playing against</td><td colspan="2">Profit</td><td colspan="2">Policy dist. from Nash</td></tr><tr><td>Avg.</td><td>Std. Dev</td><td>Avg.</td><td>Std. Dev</td></tr><tr><td>GA</td><td>1381.30</td><td>40.53</td><td>0.24</td><td>0.07</td></tr><tr><td>Softmax</td><td>1508.72</td><td>88.58</td><td>0.33</td><td>0.04</td></tr><tr><td>0.1Greedy</td><td>1505.54</td><td>168.99</td><td>0.32</td><td>0.03</td></tr><tr><td>Nash</td><td>1330.23</td><td>18.69</td><td>0.44</td><td>0.06</td></tr></table>

Performance of Softmax playing against others

<table><tr><td rowspan="2">Playing against</td><td colspan="2">Profit</td><td colspan="2">Policy dist. from Nash</td></tr><tr><td>Avg.</td><td>Std. Dev</td><td>Avg.</td><td>Std. Dev</td></tr><tr><td>GA</td><td>1418.53</td><td>34.40</td><td>0.68</td><td>0.20</td></tr><tr><td>Softmax</td><td>1800.52</td><td>224.85</td><td>0.99</td><td>0.21</td></tr><tr><td>0.1Greedy</td><td>1640.41</td><td>259.24</td><td>0.90</td><td>0.23</td></tr><tr><td>Nash</td><td>1339.79</td><td>82.42</td><td>0.64</td><td>0.14</td></tr></table>

Table 3  
Performance of 0.1Greedy playing against others

<table><tr><td rowspan="2">Playing against</td><td colspan="2">Profit</td><td colspan="2">Policy dist. from Nash</td></tr><tr><td>Avg.</td><td>Std. Dev</td><td>Avg.</td><td>Std. Dev</td></tr><tr><td>GA</td><td>1390.21</td><td>53.56</td><td>0.88</td><td>0.14</td></tr><tr><td>Softmax</td><td>1651.65</td><td>257.22</td><td>0.92</td><td>0.13</td></tr><tr><td>0.1Greedy</td><td>1536.07</td><td>256.94</td><td>0.91</td><td>0.14</td></tr><tr><td>Nash</td><td>1304.42</td><td>77.18</td><td>0.99</td><td>0.07</td></tr></table>

Table 4  
Performance of Nash playing against others

<table><tr><td rowspan="2">Playing against</td><td colspan="2">Profit</td></tr><tr><td>Avg.</td><td>Std. Dev</td></tr><tr><td>GA</td><td>1250.49</td><td>32.47</td></tr><tr><td>Softmax</td><td>1504.26</td><td>185.94</td></tr><tr><td>0.1Greedy</td><td>1686.00</td><td>171.38</td></tr></table>

RL agents and it derives pro<sup>fi</sup>ts below the Nash payoff playing against the GA.

The difference in performance between the GA agents and RL agents is primarily because GA agents are population based. Since RL agents deal with only one strategy, they are faster in adapting it in response to the feedback received from the environment. In contrast, the GA agents are population based. It takes the GA population as a whole longer to respond to the feedback received. For the same reason, the GA agents exhibit less variance, and hence better convergence properties.

## 4.1. Non-stationary environment

One of the interesting properties of contexts of strategic interactions, like the 2-seller problem considered here, is the dynamic nature of its environment even when the problem itself is static. The best response by any player at any given point depends on the strategy being used by the other player, and vice versa. Since the players are constantly learning and adapting to one another, this creates a dynamic environment. To be successful in such an encounter, an agent should be able to track and respond to the changing environment. To better test this ability for dynamic learning, we introduce explicit dynamism by making the problem non-stationary. We do this by varying the total demand Q with time. In order to satisfy the two inequalities of QNk and 2kNQ, presented earlier in section 2, we cycle the total demand from 70 to 120 and back to 70, in unit increments. Since the agents in our study are not given the information about total demand, they have to track this change in demand from the pro<sup>fi</sup>ts they derive and adapt their strategies accordingly.

We test the performance of the three agents in self-play mode (i.e., both sellers using the same learning agent). The demand is varied linearly from 70 to 120 and back to 70 in 3000 iterations and the experiment is run for a total of 6000 iterations. The results are presented in Fig. 4. As before the results are averaged over 10 different runs. To display the dynamic nature of the environment, we plot the Nash payoff given by Eq. (2.5) for the original problem formulation as an upper bound to the Nash payoff in our formulation. As can be seen from the results, all the three agents are able to track the dynamic environment consistently.

![](/api/attachments/G3YAH8PY/fulltext/images/20fb9f2c9c96442cc61583f9f61be7dc6534bc804d4d9d18f43ad55e246c69ea.jpg)  
Fig. 4. Self-play performance of the agents in non-stationary environment.

## 5. Modifying learning agents with sliding price bands

One of the drawbacks of all the learning agents presented above is that they use a <sup>fi</sup>xed and pre-determined set of price bands in learning their bidding strategies. Although the use of price bands had been justi<sup>fi</sup>ed in this paper, the use of pre-determined and <sup>fi</sup>xed price bands can lead to inef<sup>fi</sup>cient strategies being learned by the agents, especially if different agents playing the game are using price bands of different granularity. For example, in our problem, the <sup>fi</sup>rst <sup>fi</sup>ve price bands are not pro<sup>fi</sup>table (as discussed earlier) and the agents learn this quickly by assigning close to 0 probability to these price bands in their mixed strategy. In terms of the search space for mixed strategies, this implies that close to half the total search space is not useful for the learning agents using the <sup>fi</sup>xed price band representation. Moreover, the use of the same price bands by competing agents is not realistic. To overcome these problems we modify all our learning agents by making them learn price bands of varying granularity. The basic idea is to let the agents dynamically modify the width of the price bands by exploring promising price bands with <sup>fi</sup>ner intervals and consolidating weaker price bands with coarser intervals. We refer to the algorithm used by the agents in varying the price bands as the sliding window protocol. Every time an agent changes the price bands it is in effect changing the underlying problem, with the payoff matrix presented in the appendix also changing.

The sliding window protocol is presented in $\mathrm { F i g . } 5 .$ . The three constraints of $\delta _ { \mathrm { { m i n } } } ,$ υ , and $v _ { \mathrm { m a x } }$ are used mainly to keep the agent computation tractable and <sup>fi</sup>nite. They simply control the extent to which the price bands can be split or combined. Note that the sliding window protocol does not change the number of price bands but only varies their granularity. For all our experiments we use the following values for the three constraints: $\delta _ { \operatorname* { m i n } } = 0 . 5 , \boldsymbol { v } _ { \operatorname* { m i n } } = 0 . 2 , \mathrm { a n d } \boldsymbol { v } _ { \operatorname* { m a x } } = 0 . 1$ . The following example illustrates how the sliding window protocol works

Consider a sample mixed strategy vector with the following values that is learned by the GA:

$$
\begin{array}{c} \left[ 4 0, 4 4 \right] \left[ 4 4, 4 8 \right] \left[ 4 8, 5 2 \right] \left[ 5 2, 5 6 \right] \left[ 5 6, 6 0 \right] \left[ 6 0, 6 4 \right] \left[ 6 4, 6 8 \right] \left[ 6 8, 7 2 \right] \left[ 7 2, 7 6 \right] \left[ 7 6, 8 0 \right]. \\ 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0. 0 5 \quad 0. 3 8 \quad 0 \quad 0. 4 7 \quad 0. 1 0 \end{array}
$$

The <sup>fi</sup>rst two price bands could be merged since their combined value is 0 which is less than $v _ { \mathrm { m a x } } .$ The price band [64, 68] could be split since its value, 0.38, is greater than $v _ { \mathrm { m i n } }$ and its interval length $\left( \lvert 6 4 - 6 8 \rvert = 4 \right)$ is greater than $\delta _ { \mathrm { m i n } } .$ . After merging and splitting the respective price bands, we get the following mixed strategy vector, where the newly created price bands are highlighted.

$$
\begin{array}{c} \left[ 4 0, 4 8 \right] \left[ 4 8, 5 2 \right] \left[ 5 2, 5 6 \right] \left[ 5 6, 6 0 \right] \left[ 6 0, 6 4 \right] \left[ 6 4, 6 6 \right] \left[ 6 6, 6 8 \right] \left[ 6 8, 7 2 \right] \left[ 7 2, 7 6 \right] \left[ 7 6, 8 0 \right]. \\ 0 \quad 0 \quad 0 \quad 0 \quad 0. 0 5 \quad 0. 1 9 \quad 0. 1 9 \quad 0 \quad 0. 4 7 \quad 0. 1 0 \end{array}
$$

Repeating the above steps for three more iterations results in the following successively re<sup>fi</sup>ned mixed strategy vectors.

$$
\begin{array}{c} \left[ 4 0, 5 2 \right] \left[ 5 2, 5 6 \right] \left[ 5 6, 6 0 \right] \left[ 6 0, 6 4 \right] \left[ 6 4, 6 6 \right] \left[ 6 6, 6 8 \right] \left[ 6 8, 7 2 \right] \left[ 7 2, 7 4 \right] \left[ 7 4, 7 6 \right] \left[ 7 6, 8 0 \right] \\ 0 \quad 0 \quad 0 \quad 0. 0 5 \quad 0. 1 9 \quad 0. 1 9 \quad 0 \quad 0. 2 4 \quad 0. 2 4 \quad 0. 1 0 \end{array}
$$

$$
\begin{array}{c} \left[ 4 0, 5 6 \right] \left[ 5 6, 6 0 \right] \left[ 6 0, 6 4 \right] \left[ 6 4, 6 6 \right] \left[ 6 6, 6 8 \right] \left[ 6 8, 7 2 \right] \left[ 7 2, 7 3 \right] \left[ 7 3, 7 4 \right] \left[ 7 4, 7 6 \right] \left[ 7 6, 8 0 \right] \\ 0 \quad 0 \quad 0. 0 5 \quad 0. 1 9 \quad 0. 1 9 \quad 0 \quad 0. 1 2 \quad 0. 1 2 \quad 0. 2 4 \quad 0. 1 0 \end{array}
$$

$$
\begin{array}{c} \left[ 4 0, 6 0 \right] \left[ 6 0, 6 4 \right] \left[ 6 4, 6 6 \right] \left[ 6 6, 6 8 \right] \left[ 6 8, 7 2 \right] \left[ 7 2, 7 3 \right] \left[ 7 3, 7 4 \right] \left[ 7 4, 7 5 \right] \left[ 7 5, 7 6 \right] \left[ 7 6, 8 0 \right]. \\ 0 \quad 0. 0 5 \quad 0. 1 9 \quad 0. 1 9 \quad 0 \quad 0. 1 2 \quad 0. 1 2 \quad 0. 1 2 \quad 0. 1 2 \quad 0. 1 2 \quad 0. 1 0 \end{array}
$$

At this point no further splitting can be done since there is no price band whose value is greater than $v _ { \mathrm { m i n } } .$ . Comparison of the <sup>fi</sup>nal policy vector with the initial one shows the improvement brought on by the sliding window protocol. A total of 8 out of the 10 possible actions are now effectively utilized, compared to only 4 that were utilized in the initial policy vector, In all our experiments the sliding window protocol is applied every 100 iterations, during which the agents can improve on the values of the mixed strategy vector.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let
x be a mixed strategy or policy vector of size n x 1,
 $[l_{i}, u_{i}] \forall i = 1 \ldots n$ , be the n price bands or intervals,
 $\delta_{min}$  be the minimum price interval size that can be split,
 $v_{min}$  be the minimum policy vector value that can be split, and
 $v_{max}$  be the maximum combined value of two adjacent policy vector values that can be merged.

repeat
{
    find two adjacent values,  $x_{i} \&amp; x_{i+1}$ , on the policy vector x
    s.t.  $x_{i} + x_{i+1} &lt;= v_{max}$ 

    find a value  $x_{j}$  on the policy vector to split
    s.t.  $x_{j} &gt;= v_{min}$  and  $|l_{j} - u_{j}| &gt;= \delta_{min}$ 

    if and only if,  $\exists x_{i}, x_{i+1}$  and  $x_{j}$ , do the following:
    combine the price bands &amp; policy vector values i and i+1,
    split the price band and policy vector value j
}

until (no more price bands can be combined/split)
</div>

Fig. 5. The sliding window protocol.

![](/api/attachments/G3YAH8PY/fulltext/images/c631369042f12c3c2267205b39bc2e61a28ad5941f34bbc49e78287a49f5979e.jpg)  
Fig. 6. Agents using sliding window protocol playing against pure strategy $\mathbf { e } _ { 6 } .$

![](/api/attachments/G3YAH8PY/fulltext/images/f7ff470ed7285f1e43ceb83b5893040b2885681bc72c00084eda64b417b09644.jpg)  
Fig. 7. Agents using sliding window protocol playing against pure strategy ${ \bf e } _ { 1 0 } .$

![](/api/attachments/G3YAH8PY/fulltext/images/c3eb7495fb5e8d18f6b56ffb7798b80530efc08b965e3be5f7110c3036620631.jpg)  
Fig. 8. Self-play performance of the agents using the sliding window protocol.

To test the effectiveness of the sliding window protocol we test the modi<sup>fi</sup>ed agents for the same two desirable properties of rational behavior and convergence. We begin by testing all the three modi<sup>fi</sup>ed agents against the same pure strategies of ${ \bf { e } } _ { 6 }$ and $\mathbf { e } _ { 1 0 } .$ We use the expected optimal pro<sup>fi</sup>t when using <sup>fi</sup>xed price bands, as shown in Figs. 2 and 3, to show the improvement brought on by the modi<sup>fi</sup>ed agents. We also plot the upper bound of the pro<sup>fi</sup>t for both the cases. For e.g., playing against $\mathbf { e } _ { 6 }$ maximum pro<sup>fi</sup>t can be achieved by bidding at the reserve price, which results in a payoff of \$1400. Results for both the experiments are presented in Figs. 6 and 7. All the three agents improve upon their performance by deriving pro<sup>fi</sup>ts higher than the expected optimal when using <sup>fi</sup>xed price bands. They also come very close to converging to the upper bound in the both the cases. Note that since the agents are still using price bands, they can never completely converge to the upper bound in either case. Though Softmax still converges to the old expected optimal when playing against $\mathbf { e } _ { 6 } ,$ its variation in output is considerable less than that in Fig. 2.

Having shown an improvement in the rational behavior of the modi<sup>fi</sup>ed agents, we now test for their convergence properties. We carry out the same experiments as before for 3000 iterations but only for self-play $( { \mathrm { i . e . } }$ , both the sellers using the same learning algorithm). As before, we use the values from the last 1000 iterations and plot the spread of pro<sup>fi</sup>t values around the sample mean in Fig. 8. The same results are presented in Table 5. For comparison purposes we also show the values obtained without the use of the sliding protocol. For all the three agents, the sliding window protocol results in a signi<sup>fi</sup>cant reduction in the spread, and hence an improvement in the convergence of the values. Using the sliding window protocol thus makes the learning agents more widely applicable since it eliminates the need to pre-select the price bands precisely.

## 6. Conclusions and future work

With the tremendous increase in the use of B2B web auctions, there is a growing need for using automated agents that can learn better bidding strategies over time. In this paper, we presented a variety of learning agents for the problem of learning bidding strategies in a game of strategic interaction modeling reverse auctions. Most of the literature on the use of agents in contexts of strategic interaction uses convergence to Nash equilibrium as the evaluation criterion for the agents. We focused on a special case of the general problem involving two sellers in reverse auction, and presented analytical and empirical results showing the instability of the Nash equilibrium. Results from the experiments showed that the evolutionary and reinforcement learning agents, with incomplete information, displayed the desirable properties of rational behavior and convergence even in the absence of stable equilibrium. All the agents were also successful in learning strategies in a non-stationary problem environment. We further modi<sup>fi</sup>ed the agents by developing a sliding window protocol, where the agents dynamically modify the price bands by exploring promising price bands with <sup>fi</sup>ner intervals and consolidating weaker price bands with coarser intervals. Results showed improvement in both the rational behavior of the agents and their convergence properties.

Self-play performance using the sliding window protocol

<table><tr><td rowspan="2">Self-play</td><td colspan="2">Profit (with slide)</td><td colspan="2">Profit (w/o slide)</td></tr><tr><td>Avg.</td><td>Std. Dev</td><td>Avg.</td><td>Std. Dev</td></tr><tr><td>GA</td><td>1393.70</td><td>30.99</td><td>1381.30</td><td>40.53</td></tr><tr><td>Softmax</td><td>1725.17</td><td>145.32</td><td>1800.52</td><td>224.85</td></tr><tr><td>0.1Greedy</td><td>1844.27</td><td>142.52</td><td>1536.07</td><td>256.94</td></tr></table>

Since we wanted to focus on studying the ef<sup>fi</sup>cacy of using simple learning agents in learning bidding strategies in unstable environments, we only considered a special instance of the reverse auction problem involving 2 sellers. In reverse auctions involving a large buyer (for e.g., Dell buying commodity components like capacitors from suppliers), the buyer usually prefers to buy from more than one supplier (to minimize disruptions and to generate competition), but at the same time prefers to deal with only a small group of sellers (to minimize quality variance). In such scenarios, a 2-seller problem might not be very unrealistic. We plan to extend this work to a general scenario involving many sellers and non-stationary environment where the number of sellers keeps changing. This work has the potential to be used in automating bidding agents in online procurement auctions. One of the important contributions of the paper is in showing the ef<sup>fi</sup>cacy of using very simple learning agents in an unstable domain. Although the learning agents we presented were very simple, in real applications the agents might be designed with more domain-speci<sup>fi</sup>c knowledge built in. Though we were able to show the ef<sup>fi</sup>ciency of the learning agents in an unsupervised environment, it is possible that such agents would be used more often under partial human control. That scenario raises the following question: Can the ef<sup>fi</sup>ciency of these algorithms be increased by human inputs? It is likely that human inputs may assist in reducing the search space making the search more ef<sup>fi</sup>cient. However, it may also lead to some counterproductive actions by the human participants. We would like to investigate such questions about the performance of autonomous learning agents in scenarios involving a mix of human subjects and arti<sup>fi</sup>cial agents.

## Appendix A

Payoff matrix A and mixed strategy Nash equilibrium

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1</td><td>90</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td></tr><tr><td>2</td><td>210</td><td>290</td><td>390</td><td>390</td><td>390</td><td>390</td><td>390</td><td>390</td><td>390</td><td>390</td></tr><tr><td>3</td><td>350</td><td>350</td><td>490</td><td>650</td><td>650</td><td>650</td><td>650</td><td>650</td><td>650</td><td>650</td></tr><tr><td>4</td><td>490</td><td>490</td><td>490</td><td>690</td><td>910</td><td>910</td><td>910</td><td>910</td><td>910</td><td>910</td></tr><tr><td>5</td><td>630</td><td>630</td><td>630</td><td>630</td><td>890</td><td>1170</td><td>1170</td><td>1170</td><td>1170</td><td>1170</td></tr><tr><td>6</td><td>770</td><td>770</td><td>770</td><td>770</td><td>770</td><td>1090</td><td>1430</td><td>1430</td><td>1430</td><td>1430</td></tr><tr><td>7</td><td>910</td><td>910</td><td>910</td><td>910</td><td>910</td><td>910</td><td>1290</td><td>1690</td><td>1690</td><td>1690</td></tr><tr><td>8</td><td>1050</td><td>1050</td><td>1050</td><td>1050</td><td>1050</td><td>1050</td><td>1050</td><td>1490</td><td>1950</td><td>1950</td></tr><tr><td>9</td><td>1190</td><td>1190</td><td>1190</td><td>1190</td><td>1190</td><td>1190</td><td>1190</td><td>1190</td><td>1690</td><td>2210</td></tr><tr><td>10</td><td>1330</td><td>1330</td><td>1330</td><td>1330</td><td>1330</td><td>1330</td><td>1330</td><td>1330</td><td>1330</td><td>1890</td></tr><tr><td colspan="11"> $x^{*T} = \left[ 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad \frac{1586}{6329} \quad \frac{9477}{25316} \quad \frac{2353}{25316} \quad \frac{6473}{25316} \quad \frac{669}{25316} \right].$ </td></tr></table>

## References

[1] J. Andreoni, J.H. Miller, Auctions with arti<sup>fi</sup>cial adaptive agents, Games and Economic Behavio 10 (1995) 39–64.

[2] J. Arifovic, Genetic algorithm learning and the cobweb model, Journal of Economic Dynamics and Control 18 (1) (January 1994) 3–28.

[3] R. Axelrod, The Complexity of Cooperation: Agent-Based Models of Competition and Collaboration, Princeton University Press, 1997.

[4] R. Axtell, Why agents? On the Varied Motivations for Agent Computing in the Social Sciences, Center on Social and Economic Dynamics, The Brookings Institute, Working Paper No. 17, Nov. 2000.

[5] S. Bandyopadhyay, J.M. Barron, A.R. Chaturvedi, Competition among sellers in online exchanges, Information Systems Research 16 (1) (2005) 47–60.

[6] S. Bandyopadhyay, J. Rees, J.M. Barron, Simulating sellers in online exchanges, Decision Support Systems 41 (2) (2006) 500–513.

[7] J. Carbone, Sun's e-auction evolution, Purchasing Magazine (2007) (http:// www.purchasing.com/article/CA6474837.html?q=sun+microsystems).

[8] T.N. Cason, D. Friedman, Price formation in double auction markets Journal of Economic Dynamics and Control 20 (8) (August 1996) 1307–1337.

[9] A.K. David, F.S. Wen, Building optimal bidding strategies for competitive power suppliers, Proceedings of the VII Symposium of Specialists in Electric Operational and Expansion Planning (VII SEPOPE), Curitiba, Brazil, May 23-38, 2000.

[10] L. Deveaux, C. Paraschiv, M. Latourrette, Bargaining on an internet agent-based market: behavioral vs. optimizing agents, Electronic Commerce Research 1 (4) (Oct 2001) 371–401.

[11] H. Dawid, Adaptive learning by genetic algorithms: analytical results and applications to economic models, 2nd ed.Springer, Berlin, 1999.

[12] Economist, software programs that buy and sell shares are becoming ever more sophisticated, Might they replace human traders?, Sept. 15 2005.

[13] I. Erev, A.E. Roth, Predicting how people play games: Reinforcement learning in experimental games with unique, mixed strategy equilibria The American Economic Review 88 (4) (Sept. 1998) 848–881.

[14] D. Goldberg, Genetic algorithms in search, Optimization & Machine Learning, Addison Wesley, 1989.

[15] A. Jafari, A. Greenwald, D. Gondek, G. Ercal, On no-regret learning, <sup>fi</sup>ctitious play and Nash equilibrium, Proceedings of the Eighteenth International Conference on Machine Learning, 2001, pp. 226–233.

[16] J.O. Kephart, Software agents and the route to the information economy, Proceedings of the National Academy of Sciences 99 (Suppl. 3) (May 2002) 7207–7213.

[17] J.O. Kephart, J.E. Hanson, A.R. Greenwald, Dynamic pricing by software agents, Computer Networks 32 (6) (May 2000) 731–752.

[18] S.O. Kimbrough, M. Lu, Simple reinforcement learning agents: Pareto beats Nash in an algorithmic game theory study, Journal of Information Systems and eBusiness Management 3 (2005) 1–19.

[19] S.O. Kimbrough, D.J. Wu, F. Zhong, Computers play the beer game: can arti<sup>fi</sup>cial agents manage supply chains? Decision Support Systems 33 (3) (2002) 323–333.

[20] C.A. Li, A.J. Svoboda, X.H. Guan, H. Singh, Revenue adequate bidding strategies in competitive electricity markets, IEEE Transactions on Power Systems 14 (2) (1999) 492–497.

[21] D.G. Luenberger, Introduction to Dynamic Systems: Theory, Models, and Applications, John Wiley & Sons. NY, 1979.

[22] J. Moody, M. Saffell, Learning to trade via direct reinforcement, IEEE Transactions on Neural Networks 12 (4) (2001) 875–889

[23] J. Moody, Y. Liu, M. Saffell, K. Youn, Stochastic direct reinforcement: application to simple games with recurrence, Proc. of Arti<sup>fi</sup>cial Multiagent Learning, AAAI Fall Symposium, , 2004.

[24] J. Nicolaisen, V. Petrov, L. Tesfatsion, Market power and ef<sup>fi</sup>ciency in a computational electricity market with discriminatory double-auction IEEE Transactions on Evolutionary Computation (2001).

[25] D.M. Reeves, M.P. Wellman, J.K. MacKie-Mason, A. Osepayshvili Exploring bidding strategies for market-based scheduling, Decision Support Systems 39 (1) (2005) 67–85.

[26] C.W. Richter, G.B. Sheblé, Genetic algorithm evolution of utility bidding strategies for the competitive marketplace, IEEE Transactions on Power Systems 13 (1) (Feb, 1998) 256–261.

[27] C.W. Richter, G.B. Sheblé, D. Ashlock, Comprehensive bidding strategies with genetic programming/<sup>fi</sup>nite state automata, IEEE Transactions on Power Systems 14 (Nov. 1999) 1207–1212.

[28] R.S. Sexton, R.S. Sriram, H. Etheridge, Improving decision effectiveness of arti<sup>fi</sup>cial neural networks: a modi<sup>fi</sup>ed genetic algorithm approach, Decision Sciences 34 (3) (2003) 421–442.

[29] J.M. Smith, Evolution and the Theory of Games, Cambridge University Press, Cambridge, 1982.

[30] T. Sueyoshi, G.R. Tadiparthi, An agent-based decision support system for wholesale electricity market, Decision Support Systems 44 (2) (2008) 425-446

[31] R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, MIT Press, 1998.

[32] L. Tesfatsion, in: H.M. Amman, B. Rustem, A.B. Whinston (Eds.), A trade network game with endogenous partner selection, in, computational

approaches to economic problems, Kluwer Academic Publishers, 1997, pp. 249–269.

[33] L. Tesfatsion, Agent-based computational economics: growing economies from the bottom up, Arti<sup>fi</sup>cial Life 8 (2002) 55–82.

[34] J.W. Weibull, Evolutionary Game Theory, MIT Press, 1995.

[35] Bar-Yam Yaneer, Dynamics of Complex Systems, Perseus Books Group, 1997.

[36] D.Y. Zhang, Y.J. Wang, P.B. Luh, Optimization based bidding strategies in the deregulated market, Proceedings of the 1999 IEEE PES Power Industry Computer Applications Conference (PICA '99), 1999, pp. 63–68.

Riyaz Sikora is an Associate Professor of Information Systems at the College of Business at the University of Texas at Arlington. His current research interests include multi-agent systems and data mining. He has published refereed scholarly papers in journals such as Management Science, Information Systems Research, INFORMS Journal of Computing, IEEE Transactions on Engineering Management, Decision Support Systems, EJOR, IEEE Transactions on Systems, Man, and Cybernetics, and IEEE Expert. Dr. Sikora is on the editorial board of the Journal of Information Systems and e-Business Management and the Journal of Database Management. He is a co-founder and co-chair of the AIS SIG on Agent-based Information Systems. He has organized and chaired several tracks at national meetings like INFORMS, DSI, and Pre-ICIS Workshop on e-Business.

Vishal Sachdev is an Assistant Professor at the Department of Computer Information Systems at Middle Tennessee State University, Murfreesboro, TN. He received his PhD from the University of Texas at Arlington, and his Masters in International Business, from the Indian Institute of Foreign Trade in New Delhi, India. His publications include a refereed book chapter and several conference proceedings. His research interests are in social computing, outsourcing and multiagent modeling. He has teaching interests in the use of technology to enable active learning, particularly the use of multi-user virtual environments in education.
