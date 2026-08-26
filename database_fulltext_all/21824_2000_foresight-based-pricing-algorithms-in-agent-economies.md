---
otero_id: 21824
otero_key: "X6W7V5XZ"
title: "Foresight-based pricing algorithms in agent economies"
authors: "Gerald J. Tesauro; Jeffrey O. Kephart"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00074-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Foresight-based pricing algorithms in agent economies

Gerald J. Tesauro <sup>)</sup>, Jeffrey O. Kephart

IBM T.J. Watson Research Center, 30 Saw Mill RiÕer Rd., Hawthorne, NY 10532, USA

## Abstract

We propose several heuristic approaches to the development of pricing algorithms for software agents that incorporate foresight, i.e., an ability to model and predict responses by competitors. In the absence of foresight, prior work has shown that, in an economy of myopic software agents, undesirable system behaviors such as endless price wars can frequently occur Kephart, 1998 . We show how the introduction of even the smallest amount of lookahead in the agents’ pricing Ž . algorithms can significantly reduce or eliminate the occurrence of price wars. We also investigate two approaches to developing algorithms that are capable of deep lookahead, while avoiding the classic problem of infinite recursion of opponent models. The two approaches are based on adaptations of i the classic minimax fixed-depth search algorithmsŽ . used in two-player games such as chess; ii dynamic programming DP -style algorithms that have recently been extended Ž . Ž . to the domain of two-player zero-sum Markov games Littman, 1994 .Ž . q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Adaptive multi-agent systems; Agent foresight; Minimax search; Dynamic programming

## 1. Introduction

Economies of interacting software agents may exist on a large scale in the very near future. In prior work 6,9 , it has been shown that such economies <sup>w</sup> <sup>x</sup> can exhibit pathological collective behaviors. For example, the potential exists for unending cyclical price wars, in which long episodes of repeated undercutting among the sellers alternate with large jumps in price. Such price wars are often disastrous for the sellers 6 although not universally 5 , and<sup>w</sup> <sup>x</sup> Ž <sup>w</sup> <sup>x</sup>. under some conditions they can harm the buyers as well. <sup>1</sup> Price wars have the potential to be more rampant in agent economies than what we have observed in human economies due to a number of differences between agent and human economic players, such as 1 the greater ability of humans to Ž . predict long-term consequences of their price-setting actions; 2 reduced frictional effects such as con-Ž . sumer inertia in agent economies; and 3 reducedŽ .

localization effects due to much greater connectivity offered by the Internet.

In this paper, we focus specifically on the first of these factors, and explore how to endow agents with foresight to help them anticipate retaliatory responses by other agents. Very generally, we can expect even a modest ability to predict the behavior of the system or of other agents to improve an individual economic agent’s profitability. After all, in many competitive game-like domains, one commonly finds that strategies that use deeper lookahead outperform strategies with shallow or zero lookahead. This by itself justifies exploring predictive techniques tailored to economic software agents. Furthermore, it seems plausible that, if predictive algorithms are adopted by a reasonable fraction of agents, then certain types of pathological collective effects might be ameliorated or even eliminated. Consider for example the specific case of price wars. Previous work has shown that a ‘‘myopic optimal’’ agent experiences a short-term benefit when it undercuts its competitors’ prices, but retaliatory undercutting by its competitors quickly places the agent in an even less profitable position than it was in originally. Intuitively, one might expect that an agent capable of modeling and predicting its competitors’ behavior could realize the futility of undercutting if it were to average its expected return over a medium- or longterm horizon. Implementing foresight mechanisms on a large-scale throughout an agent economy might then lead to radically different system behavior, and price wars might be greatly reduced or eliminated.

In considering algorithmic approaches to agent foresight, one set of issues that arises has to do with which type of algorithms will enable agents to make the most accurate predictions, given the constraints of a limited information set and limited computational resources. An additional set of issues has to do with what sort of collective system behaviors result when a significant fraction of the agents base their actions on predictions. Will a society of machine learners converge to something like a game-theoretic solution for example, a Nash equilibrium , or will Ž . they just endlessly chase one another’s tails? The former question has been studied, for example, in Refs. 2 and 8 , while the latter issues are beginning<sup>w x</sup> <sup>w x</sup> to be addressed, for example, in Refs. 4,10 and<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 11 .

In the present work, we are primarily concerned with issues of the depth and accuracy of agent lookahead. That is to say, how far ahead in time can an agent reliably predict those aspects of the future system behavior that are relevant to their current decisions, and how much lookahead is necessary to avoid pathological behavior? Is shallow lookahead sufficient, or is it necessary for agents to engage in deep lookahead in order to avoid price wars? Likewise, how accurately an agent can predict, and how much accuracy is needed to avoid pathological behavior? For example, perhaps we would find thatŽ each agent required only a coarse prediction based on the likelihood of being undercut in the next time step in order to avoid price wars..

Our proposed algorithms for agent foresight are designed to avoid the classic problem of infinite recursion of opponent models. That is to say, when modeling other agents, one needs to take into account the fact that those other agents are themselves using models of other agents, and that those models need to take into account that the other agents are using models, etc. This can lead not only to logical problems in setting up the agent models, but also to greatly increasing levels of computational complexity with the depth of recursion. For example, in Ref. <sup>w</sup> <sup>x</sup> 11 , a recursive modeling scheme is proposed in which 0-level agents do no opponent modeling, 1- level agents model the other agents as being 0-level agents, 2-level agents model the other agents as being 1-level agents, etc. In this scheme, the computational requirements greatly increase with the level of modeling, and furthermore, there is no adequate way for an agent to model other agents as being at the same level of depth.

We consider two basic heuristic approaches to avoiding an infinite recursion of opponent models. The first approach is adapted from the domain of two-player zero-sum games such as chess, in which full-width minimax search to a fixed finite depth has been found to be an effective algorithm. In this case, the infinite recursion is cut off by the finite depth of the search. Minimax search is only guaranteed to find optimal moves if the search goes all the way to the end of the game; however, it does seem to work well in practice for searches of lesser depth. For example, the chess machines Deep Thought and Deep Blue give the impression of generating sophisticated positional understanding as an emergent property from deep searches plus simple positional knowledge built into the evaluation function.

The second approach that we explore is to adapt algorithms from the fields of dynamic programming Ž . Ž . DP and reinforcement learning RL ; such algorithms have been found to work well for single agents in stationary Markov environments i.e.,Ž Markov decision problems, or MDPs . The basic. idea of DP<sup>r</sup>RL is ‘‘Policy Iteration’’ 1 , in which <sup>w</sup> <sup>x</sup> one starts with an initial policy, computes the value function induced by that policy, and then computes an improved policy that is greedy with respect to that value function. Policy Iteration is guaranteed to converge to the optimal agent policy for single-agent MDPs. Recently, there has been some work generalizing DP-type algorithms to two-player Markov games. For example, Ref. 7 introduced an algo- <sup>w</sup> <sup>x</sup> rithm called minimax-Q for two-player zero-sum games in which the players alternately take turns moving, which is guaranteed to converge to the optimal policies for both players. Unfortunately, we cannot directly use minimax-Q in agent economies because the agent utilities are not strictly zero-sum. We investigate, in this paper, several heuristic DPlike approaches which can be used in arbitrary-sum games.

As a general caveat, we should point out that both classes of algorithms mentioned above seek deterministic optimal policies. Here ‘‘optimal’’ is used inŽ the game-theoretic sense of the best worst-case behavior against all possible opponent strategies.. However, it may be the case that such deterministic policies do not exist. For example, in the game of rock–paper–scissors, any deterministic policy can be defeated, and the best policies are non-deterministic and cannot be computed by these methods.

The remainder of this paper is organized as follows. Section 2 describes two economic models Ž . price–quality and information-filtering which are known to be prone to price wars when agents myopically optimize their short-term payoffs. We deliberately choose parameters to place each of these systems in a price war regime. Then, in Sections 3 and 4, we define in greater detail the two heuristic approaches to agent foresight mentioned above gener-Ž alized minimax search and generalized DP, respectively , and evaluate them on the basis of their ability .

to eliminate the price wars. Finally, Section 5 summarizes the main conclusions and discusses promising directions and challenges for future work.

## 2. Summary of the utility landscape model

While foresight-based algorithms are expected to be more generally useful beyond curing price wars, in this paper, we focus specifically on price wars as a convenient test domain. We test our proposed algorithms in situations where undesired price wars occur in the absence of foresight, and the algorithms are evaluated on the basis of their ability to eliminate or ameliorate price wars.

As a first step in the development of general foresight algorithms, we first consider the simplest possible case of two competing sellers, who alternately take turns adjusting their prices. We assume that the products offered by the two sellers are somewhat similar, leading to some potential for price competition between them, but there is also a degree of product differentiation, so that the cost and utility functions for the two sellers are, in general, asymmetric. There are several different economic models in which such asymmetries can come about. The primary model that we work with is a price–quality model that is described in detail in Ref. 9 . In this<sup>w</sup> <sup>x</sup> model, products offered by different sellers are distinguished by different values of a ‘‘quality’’ parameter, with higher-quality products being perceived as more valuable by the consumers. The consumers are modeled as trying to obtain the lowest-priced product at each time step, subject to threshold-type constraints on both quality and price, i.e., each consumer has a maximum allowable price and a minimum allowable quality.

The other model that we have studied is an information-filtering model described in detail in Ref. 6 .<sup>w</sup> <sup>x</sup> In this model, there are two competing sellers of news articles in somewhat overlapping categories. The partial overlap of the categories leads to a potential for direct price competition; however, the fact that they are not identical introduces an element of product differentiation similar to the quality differentiation in the price–quality model. This product differentiation leads to an asymmetry in the optimal pricing strategies for the two sellers. At each time step, the consumers decide to subscribe to one of the two sellers, based on price and on the consumer’s particular interest categories.

In both models mentioned above, the consumers deterministically and instantaneously choose one of the two sellers at every time step, based on the prices of the two sellers. This means that the only relevant variables in the state space description are the prices of the two sellers at each time step. The two sellers alternately take turns adjusting their prices at each time step, and then depending on the particular prices set, the resulting consumer behavior determines the amount of ‘‘profit’’ or ‘‘utility’’ obtained by each seller. The simulation can iterate forever, and there may or may not be a discounting factor for the present value of future rewards.

An example utility function that we study, taken from the price–quality model, is as follows: Let $p _ { 1 }$ and $p _ { 2 }$ represent the prices charged by seller 1 and seller 2, respectively. Let $Q _ { 1 }$ and $Q _ { 2 }$ represent their respective quality parameters, with $Q _ { 1 } > Q _ { 2 }$ . Let $c ( Q )$ represent the cost to a seller of producing an item of quality $Q .$ Then, assuming the particular model of consumer behavior described in Ref. 9 ,<sup>w</sup> <sup>x</sup> one can show analytically that in the limit of infinitely many consumers, the instantaneous utilities Ž . profits per consumer $U _ { 1 }$ and $U _ { 2 }$ obtained by seller 1 and seller 2, respectively are given by:

$$
U _ {1} = \left\{ \begin{array}{l l} (Q _ {1} - p _ {1}) (p _ {1} - c (Q _ {1})) & \text { if } \quad 0 \leq p _ {1} \leq p _ {2} \quad \text { or } \quad p _ {1} > Q _ {2} \\ (Q _ {1} - Q _ {2}) (p _ {1} - c (Q _ {1})) & \text { if } \quad p _ {2} <   p _ {1} <   Q _ {2} \end{array} \right.\tag{1}
$$

$$
U _ {2} = \left\{ \begin{array}{l l} (Q _ {2} - p _ {2}) (p _ {2} - c (Q _ {2})) & \text { if } \quad 0 \leq p _ {2} \leq p _ {1} \\ 0 & \text { if } \quad p _ {2} \geq p _ {1}. \end{array} \right.\tag{2}
$$

A plot of the utility landscape for seller 1 as a function of prices $p _ { 1 }$ and $p _ { 2 }$ is given in Fig. 1, for the following parameter settings: $Q _ { 1 } = 1 . 0 , Q _ { 2 } = 0 . 9$ and $c ( Q ) = 0 . 1 ( 1 + Q )$ Ž . These specific parameter settings were chosen because they are known to generate harmful price wars when the agents use myopic optimal pricing. We can see in this figure . that the myopic optimal price for seller 1 as a function of seller $2 \mathrm { { ' } s }$ price, $p _ { 1 } ^ { * } ( p _ { 2 } ) _ { }$ , is obtained for each value of $p _ { 2 }$ by sweeping across all values of $p _ { 1 }$ and choosing the value that gives the highest utility. We can see that for small values of $p _ { 2 }$ , the peak utility is obtained at $p _ { 1 } = 0 . 9$ , whereas for larger values of $p _ { 2 }$ , there is eventually a discontinuous shift to the other peak, which follows along the parabolic-shaped ridge in the landscape. An analytic expression for the myopic optimal price for seller 1 as a function of $p _ { 2 }$ is as follows defining Ž $x _ { 1 } = Q _ { 1 }$ $+ c ( Q _ { 1 } )$ and $x _ { 2 } = Q _ { 2 } + c ( Q _ { 2 } ) )$ :

![](/api/attachments/X6W7V5XZ/fulltext/images/cc70e0045749c3e312a3400df2fe162ebc13c4c856d29b3519416e4fd83ddd44.jpg)  
Fig. 1. Sample utility landscape for seller 1 in price–quality model, as a function of seller 1 price $p _ { 1 }$ and seller 2 price $p _ { 2 }$

$$
p _ {1} ^ {*} \left(p _ {2}\right) = \left\{ \begin{array}{l l} Q _ {2} & \text { if } \quad 0 \leq p _ {2} <   x _ {1} - Q _ {2} \\ p _ {2} & \text { if } \quad x _ {1} - Q _ {2} \leq p _ {2} \leq \frac {1}{2} x _ {1} \\ \frac {1}{2} x _ {1} & \text { if } \quad p _ {2} > \frac {1}{2} x _ {1}. \end{array} \right.\tag{3}
$$

Similarly, the myopic optimal price for seller 2 as a function of the price set by seller 1, $p _ { 2 } ^ { * } ( p _ { 1 } )$ , is given by the following formula assuming that prices are Ž discrete and that is the price discretization interval :.

$$
p _ {2} ^ {*} (p _ {1}) = \left\{ \begin{array}{l l} c (Q _ {2}) & 0 \leq p _ {1} \leq c (Q _ {2}) \\ p _ {1} - \epsilon & \text {if} \quad c (Q _ {2}) \leq p _ {1} \leq \frac {1}{2} x _ {2} \\ \frac {1}{2} x _ {2} & \text {if} \quad p _ {1} > \frac {1}{2} x _ {2}. \end{array} \right.\tag{4}
$$

We also note in passing that there are similar utility landscapes for each of the sellers in the information-filtering model 6 . In both models, it is the<sup>w</sup> <sup>x</sup> existence of multiple, disconnected peaks in the landscapes, with relative heights that can change depending on the other seller’s price that leads to price wars when the sellers behave myopically.

Regarding the information set that is made available to the sellers, we have made a simplifying assumption as a first step that the players have essentially perfect information. They can model the consumer behavior perfectly, and they also have perfect knowledge of each other’s costs and utility functions. Hence, our model is two-player perfect-information deterministic game that is very similar to games like chess. The main differences are that the utilities in our model are not strictly zero-sum, and that there are no terminating or absorbing nodes in our model’s state space. Also in our model, payoffs are given to the players at every time step, whereas in games such as chess, payoffs are only given at the terminating nodes.

As a final simplification, we constrain the prices set by the two sellers to lie in a range from some minimum to maximum allowable price. The prices are also discretized, so that one can create lookup tables for the seller utility functions $U ( p _ { 1 } , \ p _ { 2 } )$ Furthermore, the optimal pricing policies for each seller as a function of the other seller’s price, $p _ { 1 } ^ { * } ( p _ { 2 } )$ and $p _ { 2 } ^ { * } ( p _ { 1 } )$ , can also be represented in the form of table lookups.

## 3. Generalized minimax search

Recall that in two-player zero-sum games such as chess, minimax search to a fixed depth N works as follows: for a given starting position, one constructs a game tree of all possible moves, replies, counterreplies, etc., out to some fixed depth d. One then applies a heuristic evaluation function to the leaves of the tree, and one then does a minimax back-up of the values of the leaf nodes. This is done progressively starting from the bottom of the tree and working upwards, at each step applying either a min. operation or a max. operation depending on which side is moving. Another way of viewing this is that at depth 1 away from the leaves, the moves are selected based on a 1-ply search; at depth 2 away from the leaves, the selection is based on a 2-ply search; and so on, until finally at the root of the tree, the move that is selected is based on an N-ply search.

Our price-setting algorithm is analogous to this and works by building up a succession of optimal price lookup tables for successively greater depths. We begin by constructing a depth 1 optimal price table: for every possible starting price of the other seller, this table represents the best possible price that the seller can set to maximize immediate utility at the current time step. This corresponds to the myopic optimal pricing algorithm mentioned in Section 2, which was studied in detail in Ref. 6 . Since<sup>w</sup> <sup>x</sup> the state space is discretized and small, and since the consumer behavior is assumed to be a deterministic function of the prices of the two sellers, the optimal prices can be computed once for every state in the state space and stored in a table.

The next step is to construct a depth 2 optimal price table, which maximizes total utility summed over two time steps, assuming that the opponent will reply with a depth 1 optimal price. Next, we construct a depth 3 table, which maximizes total utility summed over three time steps, assuming that the opponent will reply with a depth 2 price, and that the player will reply to that with a depth 1 price. We can continue in this way to generate optimal price tables of arbitrary depth. The optimal price table at depth N maximizes utility summed over N time steps, assuming that the opponent first responds with a Ž .N<sup>y</sup>1 - step optimal price, the player then responds to that with a Ž . N<sup>y</sup>2 -step optimal price, etc. We remark that, for any finite game of length N time steps, our procedure will produce the exact game-theoretic optimal strategy for both players at each step of the game. For infinite games, the concept of ‘‘optimal’’ play is not necessarily well-defined; however, a reasonable approach is to examine the behavior of the generalized minimax calculation in the limit as N becomes arbitrarily large. If the calculated optimal price curves converge to an invariant set in the limit of large depth, one can reasonably conclude that such curves are optimal in the infinite game. If no such convergence is obtained, it may simply indicate that there is no unique well-defined optimal strategy for the infinite game.

A mathematical statement of the generalized minimax algorithm is as follows. Let Ž . x, y represent the current price pair for sellers 1 and 2, respectively. Let $U _ { 1 } ( x , \ y )$ and $U _ { 2 } ( x , \ y )$ represent the respective instantaneous i.e., 1-step lookahead utili- Ž .

ties. Let $X _ { N } ( y )$ denote the N-step optimal price table for seller 1, and $Y _ { N } ( x )$ denote the N-step optimal price table for seller 2. These are given by:

$$
X _ {N} (y) = \arg \max _ {x} U _ {1} ^ {N} (x, y)\tag{5}
$$

$$
Y _ {N} (x) = \arg \max _ {y} U _ {2} ^ {N} (x, y)\tag{6}
$$

where $U _ { 1 } ^ { N } ( x , \ y )$ and $U _ { 2 } ^ { N } ( x , \ y )$ represent the total N-step utilities for sellers 1 and 2, respectively, starting from the initial price pair $( x , \ y )$ and iterating forward in time using either $X _ { N - k } ( y )$ or $Y _ { N - k } ( y )$ as appropriate to update the price pair.

## 3.1. Generalized minimax pseudo-code

A pseudo-code representation of the calculation of $U _ { 1 } ^ { N } ( x , \ y )$ is as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$x = \text{Initial } X$ $y = \text{Initial } Y$  
Total Utility $= U_{1}(x, y)$  
FOR $k = 1$ TO $(N - 1)$  
IF (k odd)  
$y = Y_{N - k}(x)$  
ELSE IF (k even)  
$x = X_{N - k}(y)$  
ENDIF  
Total Utility $+ = \gamma^{k}U_{1}(x, y)$  
END  
$U_{1}^{N}$ (Initial $X$, Initial $Y$) = Total Utility.
</div>

We note that the above pseudo-code calculation includes the possibility of discounting future utilities by a discount parameter  lying between 0 and 1. When discounting is used, the predicted utility at k time steps in the future is weighted by a multiplicative factor of $\gamma ^ { k } .$ . While our formalism allows for discounting, in practice, most of our empirical results were obtained for the undiscounted case, which can be recovered by setting $\gamma = 1$

Of course, we do not expect the N-step trajectory predicted by this procedure to match the actual trajectory at every step. The later steps of the predicted trajectory in particular are based on smaller lookahead and therefore ought to be less accurate in matching agents using deep lookahead. However, the hope is that the first predicted step ought to give something reasonable. This is what has been found in domains such as chess — Deep Blue’s predicted principal variations of 20–30 moves are generally not matched in exact detail, but its top level move decisions are nonetheless extremely accurate and strong.

## 3.2. Results

Our basic finding is that when agents use any amount of lookahead at all, it can be sufficient to substantially curtail or eliminate the price war dynamics that result from myopic optimal pricing. An example of this, taken from the price–quality model, is shown in Fig. 5. In this figure, we have computed the optimal prices at lookahead depths 1, 2 and 3 for seller 1 $( p _ { 1 } ^ { * } , ~ p _ { 1 } ^ { * * } , ~ p _ { 1 } ^ { * * * } )$ and seller $2 ~ ( \boldsymbol { p } _ { 2 } ^ { * } , \ \boldsymbol { p } _ { 2 } ^ { * * }$ $p _ { 2 } ^ { * * * } )$ and have systemically plotted each curve for seller 1 against each curve for seller 2. The lookahead depth is indicated in parentheses in the lower left-hand corner of each plot.

In each of these plots, the system dynamics for the state $( p _ { 1 } , \ p _ { 2 } )$ can be obtained by alternately applying the two optimal price curves. This can be done by a simple iterative graphical construction, in which for any given starting point, one first holds $p _ { 2 }$ constant and moves horizontally to the $p _ { 1 } ^ { * } ( p _ { 2 } )$ curve, and then one holds $p _ { 1 }$ constant and moves vertically to the $p _ { 2 } ^ { * } ( p _ { 1 } )$ curve. For example, one can see in the upper-left plot that when both sellers behave myopically, i.e., lookahead depths 1,1 , the iterativeŽ . graphical construction leads to a never-ending cyclic price war, whose trajectory is indicated by the dashed line. In contrast, when both sellers use either 2-step or 3-step lookahead, we can see that the price war is eliminated, and that the system dynamics instead iterates to a fixed point. The case when one of the sellers is myopic and the other seller uses greater lookahead is interesting. This is shown in the topmost three plots, where seller 1 is myopic, and in the leftmost three plots, where seller 2 is myopic. In the latter case, we see that when seller 2 is myopic, the price war cycle still exists but has a diminished amplitude. In contrast, when seller 1 is myopic, we see that if seller 2 uses 2-step lookahead, i.e., seller 2 has a perfect model of seller 1, the price war is eliminated. However, if seller 2 uses 3-step lookahead, the price war re-emerges, but at a diminished amplitude. The re-emergence of the price war comes about because, even though seller 2 is looking ahead further, it is now using an incorrect model of seller 1.

The locations of the fixed points shown in Fig. 5 are also of some interest, and can be simply explained. We note that in every case where a fixed point is obtained, the price for seller 1 is given by $p _ { 1 } = 0 . 9$ , and that for the middle column of Fig. 5 Ž . corresponding to seller 2 using 2-step lookahead the price for seller 2 is $p _ { 2 } = 0 . 3 ,$ , whereas in the rightmost column where seller 2 uses 3-step looka- Ž head , seller 2’s price is instead . $p _ { 2 } = 0 . 4$ . This can be simply understood in terms of seller 2’s modeling of seller 1’s behavior. When seller 2 uses 2-step lookahead, it models seller 1 as being myopic. The choice of $p _ { 2 } = 0 . 3$ represents the highest possible price at which seller 1 will not respond myopically by undercutting. This can be seen by inspection of the utility function given in Eq. 1 ; we can see thatŽ . the profit in a single time step for seller 1 is 0.07 regardless of whether $p _ { 1 } = 0 . 9$ or $p _ { 1 } = 0 . 3$ . On the other hand, when seller 2 uses 3-step lookahead, it is modeling seller 1 as using 2-step lookahead. The resulting price for seller 2, $p _ { 2 } = 0 . 4 ,$ , corresponds to the point of indifference to undercutting for seller 1 based on a 2-step optimization. If seller 1 does not undercut, he receives a profit of 0.07 for the next two time steps, for a total profit of 0.14. If seller 1 undercuts, he receives a profit of 0.12 on the first time step, followed on the next time step by a profit only 0.02 after seller 2 retaliates with a furtherŽ undercut , again resulting in a total return over two . time steps of exactly 0.14. Thus, the calculated fixed-point price for seller 2 has shifted to a higher value with greater lookahead.

We note that these fixed points are at a lower price for seller 2 than the Nash equilibrium point calculated in Ref. 9 for the one-shot non-iterated<sup>w</sup> <sup>x</sup> Ž . game. For the specific parameter settings used here, the calculated Nash equilibrium values are $p _ { 1 } = 0 . 9$ and $p _ { 2 } = 0 . 5 4 5$ . This point corresponds to the open Ž circle in the upper-left plot of Fig. 5. In the iterated game, this point is not a stable equilibrium when the players are myopic, because seller 1 can obtain a higher short-term reward by undercutting seller 2, and will therefore initiate a price war. There are two.

reasons why the equilibrium points obtained here deviate from the Nash values. First, as mentioned previously, we are studying iterated games that repeat for some definite number of time steps, whereas the Nash calculation assumes a one-shot game. Secondly, our models employ alternating-turn dynamics, where the players alternately take turns adjusting their prices. The Nash calculation assumes that both players move simultaneously. Rather than obtaining a Nash solution, our calculation instead is equivalent to another type of equilibrium known in the game theory literature as a ‘‘subgame perfect’’ equilibrium <sup>w</sup> <sup>x</sup> 3 . This type of equilibrium arises when the game has a tree structure as ours does and when the Ž . equilibrium solution for the entire tree matches the equilibrium for any subtree.

It is also of interest to examine lookahead depths greater than 3. One might hope that the optimal price curves converge to a unique invariant pair in the limit of large depth, and that the fixed point of the system would approach an equilibrium point, possibly related to the Nash equilibrium. While we have no general proof that this will always happen, we have found empirically that, in the price–quality model, the optimal price curves for depths 4 and above turn out to be identical to the depth 3 curves.

However, we did not find this to be the case in the information-filtering model. Instead, it was found that there is a set of optimal price curves that periodically repeat with increasing depth, and that the period appears to be somewhat arbitrary, and can vary depending on the exact values of various cost parameters, etc. in the simulation. These findings were obtained regardless of whether or not discounting is used in the optimized utilities.

![](/api/attachments/X6W7V5XZ/fulltext/images/1190d37b7942c0924d75226958aa2700459f5bb40fe16d0748a6493f009f9c4c.jpg)  
Fig. 2. Plot of myopic optimal price curves for seller 1 vs. seller 2 in a sample run of the information-filtering model. The utilities for each seller were generated numerically using a simulated population of 250,000 consumers. Repeated iteration of the optimal price rules leads to a cyclic price war, as indicated by the dashed trajectory.

An example of results obtained in the information-filtering model is illustrated in Figs. 2 and 3. These results were obtained for a specific set of seller utilities that were numerically generated using a model population of 250,000 consumers. Fig. 2 shows the myopic optimal price curves, while Fig. 3 shows the optimal price curves using 3-step lookahead. We have generally found in the informationfiltering model that, for lookaheads depths of 2 or more, application of the calculated optimal curves resulted in a system dynamics in which the price war cycles were either eliminated completely, or reduced in amplitude. This can be seen in Fig. 3, where the amplitude of the price war cycle is reduced compared to that of Fig. 2.

In summary, we have shown that in two different models, the use of pricing algorithms based on N-step lookahead either eliminated or diminished the impact of price war behavior which is obtained when both sellers behave myopically. Important issues for ongoing and future research include: 1 establishing un-Ž .

![](/api/attachments/X6W7V5XZ/fulltext/images/9a68ede2784cb6b3416ce2e0614deef63b5a404156a5d2f12afc2d49c374e4e9.jpg)  
Fig. 3. Plot of optimal price curves for seller 1 vs. seller 2, each using 3-step lookahead, based on the same information filtering model used in Fig. 2. These optimal price curves still lead to price war behavior, but with diminished amplitude.

der what conditions the N-step lookahead procedure converges in the limit of large N to a stationary set of optimal price curves; 2 understanding when the Ž . implied dynamics for a given pair of optimal price curves iterates to a fixed point, and when it yields limit-cycle behavior; and 3 in those cases in whichŽ . a fixed point is obtained, whether it corresponds to a Nash equilibrium of the system.

## 4. Generalized DP algorithms

While generalized minimax search is an efficient procedure for successively generating optimal price tables of greater and greater depth, it suffers from some theoretical inconsistencies. First, the generation of an N-step optimal price table for a given seller is based on the assumption that the opponent will be using an Ž . N <sup>y</sup> 1 -step policy. This is problematic if one believes that the opponent is using a search algorithm of equal depth. Furthermore, there is no way that both sellers could be correct in assuming that the opponent is using lesser-depth search. Second, there is the problem that successive steps in the predicted trajectory are based on progressively shallower depth search, until finally at the end of the trajectory, the predicted pricing is myopic. Such predicted trajectories are unlikely to match actual trajectories, as it seems reasonable to assume that agents will use a given fixed depth search every time they are called upon to set a price.

As a way of overcoming these potential problems, we suggest that generalizing the formalism of DP from single-agent Markov decision problems to two-player arbitrary-sum games is a promising area of research. Such an approach could lead to the development of algorithms that yield optimal policies for both players that are fully accurate and self-consistent. Furthermore, DP-like approaches can be extended to large state spaces in which it is not feasible to use lookup tables for all possible states in the state space. This has been shown by numerous works in the field of RL, in which the lookup tables of DP are replaced by compact state representations and nonlinear function approximators, and the full sweeps through the state space of DP are replaced by following actual trajectories generated by agent policies.

In the normal formulation of DP, it is assumed that there is a single agent operating in a stationary environment that time is discrete and the state and action spaces are discrete and can be represented by lookup tables. Under these conditions, the Policy Iteration algorithm works as follows: Let Ž . x rep resent the agent’s current policy assumed to beŽ stationary regarding which action to choose in state . x. Given Ž . x , we can define an associated value function $V _ { \pi } ( x )$ , which represents the agent’s expected reward that will be obtained by starting in state x and following policy  for some number of steps into the future. In principle, the number ofŽ lookahead steps can be infinite as long as a discount factor $\gamma < 1$ is applied to the future rewards. We can. also define a slightly different value function $V _ { a , \pi } ( x )$ which represents the expected reward taking an arbitrary action a at the first time step, and subsequently following policy thereafter. Policy Iteration consists of repeated application of a basic Policy Improvement loop, which starting from an initial policy $\varPi ( x )$ produces an improved policy $\varPi ^ { \prime } ( x )$ via the following first-step optimization:

$$
\Pi^ {\prime} (x) = \arg \max _ {a} V _ {a, \Pi} (x).\tag{7}
$$

One can prove that $\pi ^ { \prime }$ as defined above is strictly better than , and that repeated application of Eq. Ž . 7 will converge to the optimal policy. There are two basic ways in which the improved policy is computed. In normal DP, every state in the state space is updated simultaneously. In asynchronous DP, a single point in the state space is selected randomly and updated. Either method will converge to the optimal policy with probability 1.

We propose the following generalizations of DP to multi-agent systems. For the two-seller game situation studied previously, let $\boldsymbol { \varPi } _ { 1 } ( \boldsymbol { p } _ { 2 } )$ and $\boldsymbol { \varPi } _ { 2 } ( \boldsymbol { p } _ { 1 } )$ represent the pricing policies for sellers 1 and $^ { 2 , }$ respectively. Let $U _ { 1 } ^ { N } ( { \bar { p } } _ { 1 } , p _ { 2 } )$ and $U _ { 2 } ^ { N } ( p _ { 1 } , \ p _ { 2 } )$ represent the N-step utilities for sellers 1 and 2 obtained by following policies $\boldsymbol { { \cal { I } } } \boldsymbol { I } _ { 1 }$ and $\boldsymbol { { \cal { I } } } \boldsymbol { I } _ { 2 }$ starting from the initial price pair $( p _ { 1 } , p _ { 2 } ) .$ Ž . This calculation is similar to the pseudo-code calculation of Section 3.1, except that fixed pricing curves are used at each time step.. Then our proposed algorithm, which we call alternating Policy Iteration, is to repeatedly take turns optimizing the $\boldsymbol { { \cal { I } } } \boldsymbol { I } _ { 1 }$ curve and then the $\boldsymbol { { \cal { I } } } \boldsymbol { I } _ { 2 }$ curve. We propose three possible versions of this algorithm. Two of these are straightforward, corresponding to the synchronous and asynchronous versions of normal Policy Iteration. The third version is an incremental version of the asynchronous algorithm, in which a random element is selected, and adjusted by a small increment the price discretization interval Ž . towards the calculated optimal price. This somewhatŽ resembles a gradient-style minimization of the amount of inconsistency between the two optimal price curves at each time step. As explained below, . the incremental approach has been found useful empirically in obtaining convergence.

## 4.1. Generalized DP pseudo-code

Pseudo-code representations of the above three algorithms synchronous, asynchronous, incrementalŽ asynchronous appear below. An incremental ver- . Ž sion of the synchronous algorithm has not been investigated. Note that in the incremental asyn-. chronous pseudo-code, represents the price discretization interval.

![](/api/attachments/X6W7V5XZ/fulltext/images/7e73403b7cb8fcd8b7bafd02fef0006c96d608b0d23923bf92b597a7cd515542.jpg)  
2—step DP agents; $\mathsf Q _ { 1 } = 1 . 0 , \mathsf Q _ { 2 } = 0 . 9$  
Fig. 4. Two-step optimal prices for seller 1 vs. seller 2 calculated by stochastic, asynchronous, incremental DP in the price–quality model.

Alternating Policy Iteration algorithms: Synchronous version:

END

WHILE not converged DO Ž .

Asynchronous version:

WHILE not converged DO Ž .

$$
\forall p _ {2} \Pi_ {1} ^ {\prime} (p _ {2}) = \arg \max _ {p _ {1}} U _ {1} ^ {N} (p _ {1}, p _ {2})
$$

$$
p _ {2} = \text { random() }
$$

$$
\forall p _ {2} \Pi_ {1} (p _ {2}) = \Pi_ {1} ^ {\prime} (p _ {2})
$$

$$
\tilde {\Pi} _ {1} (p _ {2}) = \arg \max _ {p _ {1}} U _ {1} ^ {N} (p _ {1}, p _ {2})
$$

$$
\forall p _ {1} \Pi_ {2} ^ {\prime} (p _ {1}) = \arg \max _ {p _ {2}} U _ {2} ^ {N} (p _ {1}, p _ {2})
$$

$$
\forall p _ {1} \Pi_ {2} (p _ {1}) = \Pi_ {2} ^ {\prime} (p _ {1})
$$

$$
p _ {1} = \text { random() }
$$

$$
\vec {\Pi} _ {2} (p _ {1}) = \arg \max _ {p _ {2}} U _ {2} ^ {N} (p _ {1}, p _ {2})
$$

![](/api/attachments/X6W7V5XZ/fulltext/images/a552bb21d9bacad7c51b10009d6ff596d547a706f6fefbcb5a13898e49c38d8e.jpg)

![](/api/attachments/X6W7V5XZ/fulltext/images/464e093141029070080cd934ecbc7b3eea9329eec49b9af76d9a5a10b9dc0582.jpg)

![](/api/attachments/X6W7V5XZ/fulltext/images/a2778594f598687d5a56e3ba0800afd985bd222a07419e7decac7b732b8ea361.jpg)

![](/api/attachments/X6W7V5XZ/fulltext/images/dad0ecfe2a82691706e3c8a03f2a376275a9417dafa19cba14845b07900199d4.jpg)

![](/api/attachments/X6W7V5XZ/fulltext/images/08c3815e5528b916455ef3586c678a8d541691c87856d00e3778d11b836e7556.jpg)

![](/api/attachments/X6W7V5XZ/fulltext/images/1a6a77574419129b4edc852939315095b96e42f729b83adab78717d3ede48233.jpg)

![](/api/attachments/X6W7V5XZ/fulltext/images/b8006ec690a5c95277d2ca5ec45f4d71ea4ffbbdc105364df81cb94ad4aca2f4.jpg)

![](/api/attachments/X6W7V5XZ/fulltext/images/5391df62e7af194d8d868bdb56e309e46c2757f532dd3693f33d86275d98a793.jpg)

![](/api/attachments/X6W7V5XZ/fulltext/images/8c1e29081e7f71ece1580ed80d8ee7dba8fc35c5d1b824f54d5526a03bdb4410.jpg)  
Fig. 5. Plot of optimal price curves for seller 1 vs. seller 2 in the price–quality model at various lookahead depths. The numbers in parentheses in the lower left-hand corner of each plot indicate search depths $( d _ { 1 } , d _ { 2 } )$ used by seller 1 and seller 2, respectively.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
END
Incremental Asynchronous version:
WHILE (not converged) DO
 $p_{2} = \text{random}( )$ $\Pi_{1}' = \arg\max_{p_{1}} U_{1}^{N}(p_{1}, p_{2})$ 
Adjust  $\Pi_{1}(p_{2})$  towards  $\Pi_{1}'$  by  $\epsilon$ .
 $p_{1} = \text{random}( )$ $\Pi_{2}' = \arg\max_{p_{2}} U_{2}^{N}(p_{1}, p_{2})$ 
Adjust  $\Pi_{2}(p_{1})$  towards  $\Pi_{2}'$  by  $\epsilon$ 
END.
</div>

## 4.2. Results

We have studied the three versions of alternating Policy Iteration listed above in both the price-quality and information-filtering models mentioned previously. So far, we have only examined the case of 2-step lookahead, i.e., each seller optimizes 2-step utility and also models the other seller as optimizing 2-step utility. Empirical results for both models were disappointing for the synchronous and asynchronous algorithms; these were not found to converge to a unique, self-consistent solution. However, we have found empirical convergence with the incremental asynchronous algorithm, in both the price–quality model and in the information-filtering model. In the price–quality model, the price curves for both sellers quickly converged to the exact same optimal price curves apart from very small random fluctuations ofŽ less than 1% as obtained by three or more looka-. head steps in the generalized minimax procedure. A plot of the DP-generated optimal price curves is shown below in Fig. 4.

We note that visually this plot appears identical to the lower right-hand plot in Fig. 5, and leads to fixed-point dynamics rather than cyclic price wars.

The same stochastic, asynchronous, incremental DP algorithm was tested in the information-filtering model, and when the number of consumers in the simulation was large 10,000 to 250,000 it gaveŽ . similarly good approximate convergence within small fluctuations to stationary optimal price curves. However, with only 1000 consumers in the model, the fluctuations were larger and it was not entirely clear whether the algorithm was converging to a stationary solution. We conjecture that this behavior may be due to differing degrees of smoothness in the utility landscapes. The analytically-defined landscapes in the price–quality model are very smooth, and are also smooth in the filtering model as the number of consumers becomes infinitely large. However, the landscapes become much more ragged with a small finite-size consumer population, and such raggedness may limit the ability of the DP-like approach to converge to a stationary solution.

An example of results using the DP-like approach in the information-filtering model is shown in Fig. 6. This figure plots the 2-step optimal price curves for seller 1 and seller 2 for the same numerically generated utilities as were used in Figs. 2 and 3. We do find good approximate convergence to stationary curves in this model. The small random fluctuations are somewhat larger than those seen in Fig. 4; most likely this is due to a coarser resolution in the optimal price tables 0.005 vs. 0.002 . In this particu- Ž . lar model, we can see that the DP-generated optimal price curves still lead to a price war that actually has a slightly larger amplitude than in the myopic case shown previously in Fig. 2. Hence, there are at least some cases in which the use of lookahead in the sellers’ pricing strategy can actually exacerbate the price war dynamics. Determining under what conditions price wars are amplified by lookahead, and under what conditions they are diminished or eliminated, is an important topic for further research.

![](/api/attachments/X6W7V5XZ/fulltext/images/c2937d49085516b9d7b63c0d3b8910482eadc28a63e19596aa566238cda2f0f3.jpg)  
Fig. 6. Two-step optimal prices for seller 1 vs. seller 2 calculated by stochastic, asynchronous, incremental DP in the same information-filtering model as shown in Figs. 2 and 3.

## 5. Conclusions

We have constructed a very simplified and restricted two-seller economy in which the instanta neous utilities of the two sellers are given either by the price–quality model of Ref. 9 , or by the of the<sup>w x</sup> information-filtering model of Ref. 6 . In both models, cyclic price wars are obtained when the sellers myopically optimize their instantaneous utilities without regard to longer-term impact of their pricing policies. By limiting the system to two sellers with fixed product differentiation i.e., quality or informa-Ž tion category , and by modeling the consumers as. giving instantaneous, deterministic responses to the current prices of the two sellers, we have essentially created a two-player, alternating-turn, arbitrary-sum Markov game. In this game, both the state-space transitions and the rewards at each time step are deterministic; furthermore, the state space is fully observable and the exact utility functions for both players are known by each player. Finally, the dis cretization of the seller prices implies if one observes other agents behaving in a way that one believes to be suboptimal, it might be worth investigating whether such apparent suboptimal behavior might possibly be exploited by some sort of inductive modification of the agent’s predictions. A number of important theoretical challenges must be faced in trying to develop such algorithms. First, there is the issue of generalization: given that we have observed the opponent behaving in a certain way at one point in state space, what can we then infer about how that opponent will behave in other parts of the state space? Second, there is the issue of exploration: it may be necessary for the agent to make suboptimal moves in order to reach new areas of state space, simply to gather more information about the oppo nents’ behaviors and strategies. Third, there are addi tional challenges if one believes that the opponents strategies are non-stationary; this is presumably much more difficult than modeling a fixed strategy. Fi nally, there are a host of gamemanship-type issues that could arise; for example, if we observe an opponent behaving suboptimally, it may be a trick — the opponent may be trying to lead us to develop an incorrect model which can then be exploited at later times.

## Acknowledgements

The authors thank J. Sairamesh for helpful discussions and Amy Greenwald for helpful comments, including relating our work to subgame perfect equilibria.

## References

<sup>w</sup> <sup>x</sup> 1 D.P. Bertsekas, Dynamic Programming and Optimal Control, Athena Scientific, Belmont, MA, 1995.

<sup>w</sup> <sup>x</sup> 2 D. Foster, R. Vohra, Regret in the on-line decision problem, Games and Economic Behavior 1998 to appear.Ž .

<sup>w</sup> <sup>x</sup> 3 D. Fudenberg, J. Tirole, Game Theory, MIT Press, Cambridge, MA, 1991.

<sup>w</sup> <sup>x</sup> 4 J. Hu, M.P. Wellman, in: Self-fulfilling bias in multiagent learning, Proceedings of ICMAS-96, AAAI Press, 1996.

<sup>w</sup> <sup>x</sup> 5 J.O. Kephart, A. Greenwald, Shopbot economics, submitted to Autonomous Agents ’99, 1998.

<sup>w</sup> <sup>x</sup> 6 J.O. Kephart, J.E. Hanson, J. Sairamesh, Price-war dynamics in a free-market economy of software agents, to appear in: Proceedings of ALIFE-VI, Los Angeles, 1998.

<sup>w</sup> <sup>x</sup> 7 M.L. Littman, in: Markov games as a framework for multiagent reinforcement learning, Proceedings of the Eleventh International Conference on Machine Learning, Morgan Kaufmann, 1994, pp. 157–163.

<sup>w</sup> <sup>x</sup> 8 P. Milgrom, J. Roberts, Adaptive and sophisticated learning in normal form games, Games and Economic Behavior 3 Ž . 1991 82–100.

<sup>w</sup> <sup>x</sup> 9 J. Sairamesh, J.O. Kephart, in: Dynamics of price and quality differentiation in information and computational markets,Proceedings of the First International Conference on Information and Computation Economics ICE-98 , ACM Press, 1998, Ž . pp. 28–36.

<sup>w</sup> <sup>x</sup> 10 T.W. Sandholm, R.H. Crites, in: On multiagent Q-Learning in a semi-competitive domain,14th International Joint Conference on Artificial Intelligence IJCAI-95 , Workshop onŽ . Adaptation and Learning in Multiagent Systems, Montreal, Canada, 1995, pp. 71–77.

<sup>w</sup> <sup>x</sup> 11 J.M. Vidal, E.H. Durfee, Learning nested agent models in an information economy, Journal of Experimental and Theoretical AI 1998 to appear. Ž .
