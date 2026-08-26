---
otero_id: 4462
otero_key: "ED8MW36U"
title: "Social network-embedded prediction markets: The effects of information acquisition and communication on predictions"
authors: "Liangfei Qiu; Huaxia Rui; Andrew Whinston"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Social network-embedded prediction markets: The effects of information acquisition and communication on predictions

Liangfei Qiu <sup>a,</sup>⁎, Huaxia Rui <sup>b</sup>, Andrew Whinston <sup>c</sup>

<sup>a</sup> Department of Economics, University of Texas at Austin, Austin, TX 78712, USA

<sup>b</sup> Simon School of Business, University of Rochester, Rochester, NY 14627, USA

<sup>c</sup> McCombs School of Business, University of Texas at Austin, Austin, TX 78712, USA

## a r t i c l e i n f o

Available online xxxx

Keywords: Prediction market Social network Information acquisition

## a b s t r a c t

Information aggregation mechanisms are designed explicitly for collecting and aggregating dispersed information. An excellent example of the use of this “wisdom of crowds” is a prediction market. The purpose of our social network-embedded prediction market is to suggest that carefully designed market mechanisms can elicit and gather dispersed information that can improve our predictions. Simulation results show that our network-embedded prediction market can produce better predictions as a result of the information exchange in social networks and can outperform other non-networked prediction markets. It is shown that forecasting errors decrease with the cost of acquiring information in a network-embedded prediction market. We also develop an information system that combines the power of prediction markets with the popularity of Twitter.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Predicting outcomes is essential to business decision making. But how do we assess the probability of future events in a world full of uncertainties? The two most popular approaches for producing reliable forecasts are experts' predictions and “the wisdom of crowds” (i.e., collecting and aggregating dispersed information from a large population). In the experts' prediction approach, a regression model forecasts future events based on known past events. For example, specialists' forecasting in econometrics might predict the opening price of a stock based on its past performance. There are several disadvantages to this approach; for instance, identifying the true experts can be hard work.<sup>1</sup> Even if we can identify the experts, the questions of how to elicit the knowledge quickly and of how to combine experts' differing opinions remain. One can rarely conclusively infer that the expert was intentionally deceptive, even if the realized outcome departs signi<sup>fi</sup>cantly from the expert's prediction.

The other approach, “the wisdom of crowds,” is based on the assumption that information and knowledge in social systems frequently exist only as dispersed opinions, and that aggregating dispersed information can produce accurate predictions [23,25]. A prediction market illustrates effective use of the wisdom of crowds. In a prediction market, assets are created whose <sup>fi</sup>nal value is tied to a particular event, such as whether the next U.S. president will be a Republican or a Democrat. People “place bets” on events that they think are most likely to happen, thus revealing in a sense the nature of their private information and subsequent posterior beliefs. The market mechanisms provide a method of “putting your money where your mouth is” [10]. Prediction markets can also immediately incorporate new information and provide a real-time forecast. The hope is that by aggregating the private information of a large population, a prediction market can generate fairly accurate predictions of future events. Financial Times reported a voting application on Facebook, which has some features of a prediction market. Producer Endemol used Facebook's Credits system of micropayments to let fans vote for their favorite contestants via a Facebook application.<sup>2</sup> The fans must put money into their credits accounts, thus voting for the favorite contestants is a typical way of “putting your money where your mouth is.” By aggregating the information from voting, the company could obtain a more accurate prediction of the contestants' potentials to be celebrities. It is also important to note that Facebook network plays a role in online voting. Unlike traditional phone and textmessage voting, each vote cast is shared with friends on the site, and the fans could exchange views on Facebook social network.

In prediction markets, prediction decisions rely on information that participants gather through communication with friends, neighbors, and co-workers. Twitter is a good example of such a network.

L. Qiu et al. / Decision Support Systems xxx (2013) xxx–xxx

Launched in 2006, the closely held Twitter boasts of more than 200 million accounts as of March 2011, that, in total, post an average of 150 million messages, known as tweets, a day.<sup>3</sup> Providing an example of how Twitter has been used for information exchange, CNBC News reported that farmers used their Twitter accounts to post a message, or to tweet, about a particularly robust corn crop. Tweeting with fellow farmers has become a way for the participants in a far-<sup>fl</sup>ung and isolated business to compare notes on everything from weather conditions to new fertilizers.<sup>4</sup> The use of tweets by a growing network of farmers and traders is transforming how this multi-trillion dollar industry does business. These tweets are dramatically accelerating the <sup>fl</sup>ow of information, giving investors an edge in the commodities market. Generally speaking, people connected by Twitter network create important conduits of information. Thus, natural questions about these information exchanges arise, such as how farmers' trading decisions are affected by the <sup>fl</sup>ow of information transmitted through the Twitter network. More precisely, what is the effect of these connections on farmer's trading decisions?

In this paper, a prediction market is a betting market where individuals place bets on the outcome of future events. We study a social network-embedded prediction market, modeled as an incomplete information network game. Each player observes her number of friends, but does not know the structure of the network on which she plays. For example, people only pay attention to the close friends in the Facebook and Twitter networks given their limited cognitive resources. Therefore, they don't know whom their friends pay attention to. This setup is also motivated by the privacy issues of social media. For instance, on Google Plus, people put their friends into different Circles. Every time they share information and thoughts, they can specify exactly which Circles receive them. People know the number of friends who share information with them, but they don't know the whole network of information sharing.<sup>5</sup>

In the network game, the degree of a player is the number of friends she has. We show that the equilibrium action of information acquisition is non-increasing in the degree. There is a symmetric Bayes–Nash Equilibrium, where all players use a simple cut-off strategy involving the threshold degree. The inef<sup>fi</sup>ciency of information acquisition is caused by free-riding. In the equilibrium, higher degree players exert lower efforts in acquiring information but earn a higher payoff compared to their less connected peers. This implies that social connections confer personal advantage.

We conduct a variety of simulations of agents trading in prediction markets and demonstrate that, in a network-embedded prediction market, the forecasting errors increase along with the cost of acquiring information. The implication is similar to the efficient market hypothesis. As more and more players acquire information, the prediction market price fully incorporates all available information and thus yields better forecasts. We further demonstrate that, compared to the prediction markets without social networks, the forecasting errors are lower in a network-embedded prediction market when the cost of information acquisition is not too high.

We also develop an information system that combines the power of prediction markets with the popularity of Twitter. Players in the prediction market are connected by a Twitter network, and they make forecasts based on the information gathered through the network. It is a socially embedded prediction market based on Twitter network. Our Twitter-embedded prediction market has a signi<sup>fi</sup>cant advantage in forecasting and can produce a fairly accurate prediction as a result of the information exchange in social networks.

## 2. Literature review

A number of empirical studies show that prediction markets have been successfully used to predict outcomes in many areas [26]. In the political domain, Berg, Forsythe, Nelson, and Reitz [1] document that prediction markets outperform polls for longer horizons. In the Iowa Electronic Market, the most famous prediction market, traders buy and sell contracts that pay \$1 if a given candidate wins the election. In business practice, Hewlett-Packard uses prediction markets to forecast sales, as well as <sup>fi</sup>nancial and accounting results. The predictions consistently beat the of<sup>fi</sup>cial HP forecasts [7]. In Berg et al. [2], prediction markets are designed to forecast market capitalization prior to an initial public offering. Castro and Cramton [9] propose a prediction market as a way to forecast future demand for electricity. Guo, Fang, and Whinston [17] propose a macro prediction market to effectively elicit and aggregate useful information about systematic demand risk and show that such information can be used to achieve accurate demand forecast sharing and better channel coordination in the supply chain system. All these examples share the following characteristic: Small bits and pieces of relevant information exist in the opinions and intuitions of diverse individuals. Most previous papers focus on how to elicit dispersed private information. For example, Fang, Stinchcombe, and Whinston [10] propose a betting mechanism that elicits agents' private information, as well as the precision of the information. In their work, the information of all the players is independent. However, in our network-embedded prediction market, the information players possess is correlated with that of their neighbors.

Burggen et al. [5] design an experiment under laboratory conditions to compare the forecasting accuracy of the prediction market approach and that of the traditional combined judgmental approach. However, lab experiments in isolation have limited relevance in predicting <sup>fi</sup>eld outcomes. In this experiment by Burggen et al., upper level undergraduates and MBA students participated in the study. Although students are often the standard subject pool because they are a convenient sample for academics, the primary drawback is evident: The information sources of the students are very similar. Our Twitter-embedded prediction market is different from a lab experiment in many ways. In the <sup>fi</sup>eld, subjects bring certain information to their trading activities in addition to their knowledge of the trading institution. In abstract settings, the importance of this information is diminished, which can lead to behavioral changes. Field experience also can play a major role in helping individuals develop heuristics for speci<sup>fi</sup>c tasks [18]. In the Twitter-embedded prediction market, we are recruiting subjects in the <sup>fi</sup>eld rather than in the classroom and are using a <sup>fi</sup>eld context rather than abstract instructions. The environment of this experiment thus can provide a context for suggesting strategies and heuristics that a lab setting might not provide.

This study is related to the work on social networks. The role of social networks in <sup>fi</sup>nding jobs is a leading example of networked markets [15]. Calvo-Armengol and Jackson [6] develop a model where players obtain information about job opportunities through a social network to examine how the network structure can affect employment and wage dynamics. Golub and Jackson [14] consider the wisdom of crowds in social networks. They discuss how network structure in<sup>fl</sup>uences the spread of information and show that all opinions in a large society converge to the truth if and only if the in<sup>fl</sup>uence of the most in<sup>fl</sup>uential agent vanishes as the society grows. Galeotti, Goyal, Jackson, Vega-Rendondo, and Yariv [12] provide a framework to analyze strategic interactions in an incomplete information network game.

Our model can also be viewed as an extension of Grossman and Stiglitz [16]. Their paper discusses information acquisition in a competitive market. Prices re<sup>fl</sup>ect the information of informed individuals who are isolated from each other. However, interactions among market participants are common. A series of questions arise. Does the use of networked markets affect information acquisition and ef<sup>fi</sup>ciency of a market? What is the effect of social connections on players' incentives to acquire information? Do players with more connections earn more, compared to their less connected peers? How does the cost of acquiring information affect forecasting errors in the prediction markets? Our work provides a game-theoretic framework to analyze these questions.

The rest of the paper is organized as follows. Section 3 presents the model of social network-embedded prediction markets. In Section 4, we discuss some simulation results of forecast performance. Section 5 describes the design of our Twitter-embedded prediction markets. We summarize and conclude in Section 6.

## 3. A theoretical model

## 3.1. Model setup

In this section, we set up a theoretical model of a network prediction market. Players are linked to each other according to a social network, and information is transmitted over the network.

We <sup>fi</sup>rst outline an economic model of prediction markets. A principal wants to forecast a random variable V, and v is the realization of V. In reality, V could be a movie box of<sup>fi</sup>ce revenue, a future demand for electricity, or stock prices. The principal resorts to n risk-averse agents to obtain an accurate prediction. Principal and agents share a common prior on the distribution of V, given by:

$$
V \sim N (V _ {0}, 1 / \rho_ {v}).
$$

Each agent can bet on an asset tied to V in the prediction market, which means that the agents who know they have more accurate information are generally willing to bet more money on it. The agents payoffs depend on the realization of V. For simplicity, we assume that an agent's payoff from betting is an exponential utility function with a constant coef<sup>fi</sup>cient of absolute risk aversion, γ:

$$
E [ - \exp [ - \gamma x _ {i} (V - p) ] - c m _ {i} + a | I _ {i} ],\tag{1}
$$

where p is the market price of the asset tied to $V , x _ { i }$ is the demand for the risky asset, m is an indicator function indicating whether or not the agent acquires a signal at a utility cost c, and a is a positive constant that keeps the utility positive. I is agent i's information set, which includes the information she acquires and the information passed to her from the social network $\boldsymbol { { \cal T } } = ( N , L )$ , where $N = \{ 1 , 2 , . . . ,$ n} is a <sup>fi</sup>nite set of nodes and a L N×N is a set of links. The connections between the agents are described by an n×n-dimensional matrix denoted by $g { \in } \{ 0 , 1 \} ^ { n \times n }$ , such that<sup>6</sup>

$$
g _ {i j} = \left\{ \begin{array}{l l} 1 & \text { if } (i, j) \in L \\ 0 & \text { otherwise } \end{array} \right..
$$

Let ${ N _ { i } } ( g ) = \{ j \in N : g _ { i j } = 1 \}$ represent the set of neighbors of i. The degree of agent i is the number of i's neighbors, $k _ { i } ( g ) = \lvert N _ { i } ( g ) \rvert$

Agents exchange information over the social network: we assume that they can observe their direct neighbors' information, but not their second order neighbors' (neighbor's neighbor) information. For example, people may know their friends quite well, but they don't know much about their friends' friends. If agent i does acquire information from her private source $( m _ { i } = 1 )$ , she observes a private signal, which is independent conditional on $V ,$ and passes it to her neighbors<sup>7</sup>:

$$
S _ {i} = V + \varepsilon_ {i}, \varepsilon_ {i} {\sim} N (0, 1 / \rho_ {\varepsilon}),
$$

where $\rho _ { \varepsilon }$ is the precision of player i's information for $i = 1 , 2 , . . . , N .$ ε<sub>i</sub> is an error term that is independent across agents.

In the following sections, we call an agent a player. Each player joins a two-stage network game. The time line is summarized in Fig. 1. In stage 1, all players decide whether to acquire information simultaneously, so there is a simultaneous move network game. In the second stage, a player makes use of her information to choose the optimal demand for the risky asset. In Section 3.2, we mainly focus on the optimization problem in the second stage. The incomplete information network game is analyzed in Section 3.3.

## 3.2. Security trading in prediction markets

From the moment-generating function of a normal distribution, we know:

$$
E [ \exp (t X) ] = \exp \left(t \mu + \frac {1}{2} \sigma^ {2} t ^ {2}\right),
$$

where X is a random variable that follows a normal distribution with mean μ and variance $\sigma ^ { 2 } .$ . Applying the above results, maximizing $\operatorname { E q . } \left( 1 \right)$ is equivalent to maximizing the following function of x<sub>i</sub>:

$$
- \exp \left[ - \gamma x _ {i} (E [ V | I _ {i} ] - p) + \frac {1}{2} \operatorname{Var} [ V | I _ {i} ] \gamma^ {2} x _ {i} ^ {2} \right] + a - m _ {i} c.
$$

Hence, player i's optimization problem becomes:

$$
\underset {x _ {i}} {\text { Max }} \gamma x _ {i} (E [ V | I _ {i} ] - p) - \frac {1}{2} \text { Var } [ V | I _ {i} ] \gamma^ {2} x _ {i} ^ {2}.\tag{2}
$$

From the <sup>fi</sup>rst-order condition, we obtain

$$
x _ {i} ^ {*} = \frac {E [ V | I _ {i} ] - p}{\gamma V a r [ V | I _ {i} ]}.
$$

Note that if the conditional expectation is greater than the price, the demand for the risky asset is positive. If the risk aversion γ increases, people become more risk averse, and the absolute value of demand decreases. If conditional variance increases, the asset is more risky, and the absolute value of demand also decreases.

The price p is endogenously determined by the market clearing condition: $\sum _ { i = 1 } ^ { n } { x _ { i } } ^ { * } = 0$ . Market clearing condition means that the <sup>¼</sup>total demand for the risky asset equals to the supply, which is normalized to 0.

In the second stage, player i's optimal demand for risky asset ${ x _ { i } } ^ { * }$ depends on whether player i and her neighbors acquire information, and thus ${ x _ { i } } ^ { * }$ is a function of m and $m _ { N _ { i } ( g ) } .$ , where $m _ { N _ { i } ( g ) }$ is the action <sup>ð Þ ð Þ</sup>pro<sup>fi</sup>le of player i's neighbors, and it represents whether player i's friends acquire information.

Thus, player i's payoff can be written as:

$$
u \left(m _ {i}, m _ {N _ {i} (g)}\right) = E \left[ - \exp \left[ - \gamma x _ {i} ^ {*} \left(m _ {i}, m _ {N _ {i} (g)}\right) (V - p) \right] - c m _ {i} + a | I _ {i} \right],
$$

L. Qiu et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/ED8MW36U/fulltext/images/3c4ef178434f4b0e45cd8d9592f5477b857a77b572f509c58c39d625699ff3df.jpg)  
Fig. 1. Time line.

where $m _ { N _ { i } ( g ) } \in \{ 0 , 1 \} ^ { k _ { i } }$ is the action pro<sup>fi</sup>le of player i's neighbors. The <sup>ð Þ</sup>payoff function depends on whether player i and her neighbors acquire information. Following [12], the payoff function depends on the player's degree $k _ { i }$ but not on her identity i. Therefore, any two players who have the same degree have the same payoff function. It is also evident that u depends on the vector $m _ { N _ { i } ( g ) }$ in an anonymous way; thus, a permutation of $m _ { N _ { i } ( g ) }$ <sup>ð Þ</sup>does not change the payoff.

<sup>ð Þ</sup>We say that a payoff function exhibits strategic substitutes if an increase in others' actions lowers the marginal returns from a player's own action: For all $k , m _ { i } > m$ <sub>i</sub> and $m _ { \ : N _ { i } ( g ) } ^ { ' } { \geq } m _ { \ : N _ { i } ( g ) } { : }$

$$
u \left(m _ {i} ^ {\prime}, m _ {N _ {i} (g)} ^ {\prime}\right) - u \left(m _ {i}, m _ {N _ {i} (g)} ^ {\prime}\right) \leq u \left(m _ {i} ^ {\prime}, m _ {N _ {i} (g)}\right) - u \left(m _ {i}, m _ {N _ {i} (g)}\right).
$$

When a payoff function exhibits strategic substitutes, a player's incentive to take a given action decreases as more neighbors take that action.

Lemma 1. The payoff function in the network-embedded prediction market exhibits strategic substitutes.

Proof. Applying Bayesian updating, we can obtain the best mean square predictor of V based on $S _ { i } { \mathrm { : } }$

$$
E [ V | S _ {i} ] = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} S _ {i}.
$$

Similarly, we can obtain the best mean square predictor of V based on other information sets. Assume that for $m _ { N _ { i } ( g ) } ,$ , there are $k _ { a }$ of $\mathsf { p l a y - }$ er i's neighbors (among the total number $k _ { i } )$ <sup>ð Þ</sup>who acquire information. In other words, for vector $m _ { N _ { i } ( g ) } .$ , there are $k _ { a }$ elements of 1 and $k _ { i } - k _ { a }$ <sup>ð Þ</sup>elements of 0. For player i's action, $m _ { i } = 0$ , and $m _ { i } ^ { \prime } = 1$ , we can obtain:

$$
\begin{array}{l} \frac {\partial}{\partial k _ {a}} \left[ u \left(m _ {i} ^ {\prime}, m _ {N _ {i} (g)}\right) - u \left(m _ {i}, m _ {N _ {i} (g)}\right) \right] \\ = - E \left[ \frac {\rho_ {\varepsilon} ^ {2} (V - P) ^ {4}}{4} \exp \left[ - \frac {\rho_ {\varepsilon} k _ {a}}{2} (V - V _ {0}) ^ {2} - (\rho_ {V} + \rho_ {\varepsilon} k _ {a}) (V - V _ {0}) (V _ {0} - P) - \left(\frac {\rho_ {\varepsilon} k _ {a}}{2} + \rho_ {V}\right) (V _ {0} - P) ^ {2} \right] \right] \\ <   0. \end{array}
$$

Therefore, the payoff function exhibits strategic substitutes. ■

## 3.3. Equilibrium results

We assume that players do not know the global structure of the network on which they play but are informed of only their own degrees. Thus, we relax the assumption of complete information on the social networks. Each player observes her own degree $k _ { i }$ (her type), but does not observe the degree of any other player in the network. Her beliefs about the degrees (types) of her neigh bors,<sup>8</sup> given her own degree $k _ { i } ,$ are equal to

$$
P (\cdot | k _ {i}) \in \Delta \{1, \dots , k _ {\max} \} ^ {k _ {i}},
$$

where $k _ { \mathrm { m a x } }$ is the maximal possible degree, and $\{ 1 , . . . , k _ { \mathrm { m a x } } \} ^ { k _ { i } }$ is the set of probability distributions on $\{ 1 , . . . , k _ { \mathrm { m a x } } \} ^ { k _ { i } }$ <sup>f g</sup>. For simplicity, we assume that neighbors' degrees are all stochastically independent.<sup>9</sup>

Assumption 1. The degree distributions of neighboring nodes are independent.

A strategy is a function σ: $\{ 1 , . . . , k _ { \mathrm { m a x } } \} \to \Delta \{ 0 , 1 \}$ , and we focus on symmetric Bayes–Nash equilibria, where all players follow the same strategy σ. The expected payoff of player i with degree $k _ { i }$ and action m is equal to

$$
U (m _ {i}, \sigma ; k _ {i}) = \sum_ {m _ {N _ {i} (g)}} \pi \Big (m _ {N _ {i} (g)}, \sigma ; k _ {i} \Big) u \Big (m _ {i}, m _ {N _ {i} (g)} \Big),
$$

where $\pi \big ( m _ { N _ { i } ( g ) } \sigma ; k _ { i } \big )$ is the probability distribution over $m _ { N _ { i } ( g ) }$ induced by $P ( \cdot | k _ { i } )$ <sup>ð Þ ð Þ</sup>and σ. Recall that player i's strategy σ is non-increasing $\mathrm { i f } \sigma ( k _ { i } )$ <sup>fi</sup>rst-order stochastically dominates $\sigma ( { k _ { i } } ^ { \prime } )$ for each $k _ { i } ^ { \prime } > k _ { i } .$ In our context, this simply implies that high-degree players will randomize their actions with less probability in $m _ { i } = 1$ and greater probability in $m _ { i } = 0 .$

Proposition 1. If Assumption 1 holds, there exists a symmetric equilibrium that is non-increasing in degrees in the social network embedded prediction market: There exists some threshold $k ^ { * } \in \{ 0 , 1 , 2 , \ldots \}$ , such that the probability $\sigma ( m _ { i } = 1 | \cdot )$ of choosing to acquire information in the unique, non-increasing symmetric equilibrium strategy σ satisfies:

$$
\sigma (m _ {i} = 1 | k _ {i}) = \left\{ \begin{array}{l l} 1 & \text { for } k _ {i} \leq k ^ {*} \\ 0 & \text { for } k _ {i} > k ^ {*} \end{array} \right..
$$

<sup>8</sup> This particular formulation is not standard. Notice that a player does not have beliefs about all players in the network, but only about the degrees of the players connected to him. We assume that plavers' beliefs about the rest of the network are summarized by a probability distribution over the degrees of their neighbors

<sup>9</sup> Actually, our model can allow correlation between neighbors' degrees. This implies that the conditional distributions concerning neighbors' degrees can vary with a player's degree. The results also hold when higher degrees for a given player are correlated with lower degrees of all his neighbors. This assumption is inappropriate for some networks, including those of scienti<sup>fi</sup>c collaborations or actor collaboration, which display signi<sup>fi</sup>cant positive degree correlation [21]. However, we can argue that the degrees of two neighbors are approximately independently distributed for large networks such as Twitter

Please cite this article as: L. Qiu, et al., Social network-embedded prediction markets: The effects of information acquisition and communication on predictions, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.007

Proof. In our context, the player's payoffs depend on the neighbors' strategies and the payoff function satis<sup>fi</sup>es the following general property discussed in [12]:

$$
\begin{array}{l} \text { Property   1. } u (m _ {i}, (m _ {N _ {i} (g)}, 0)) = u (m _ {i}, m _ {N _ {i} (g)}) \text { for   any } (m _ {i}, m _ {N _ {i} (g)}) \in \\ \{0, 1 \} ^ {k + 1}. \end{array}
$$

Suppose that Property 1 and Assumption 1 hold. Consider a player whose degree is $k _ { i } + 1$ , and the action pro<sup>fi</sup>le of his neighbors is $( m _ { N _ { i } ( g ) } , \mathrm { ~ } 0 )$ , which means that he has k neighbors who take exactly the same action as the action pro<sup>fi</sup>le of player i's neighbors, $m _ { N _ { i } ( g ) } .$ and the $( k _ { i } + 1 ) !$ <sup>ð Þ</sup>h neighbor chooses action 0. Property 1 implies that this player's payoff is equal to player i's payoff, given the action pro-<sup>fi</sup>le. Under Property 1, adding a link to a neighbor who chooses action 0 is payoff equivalent to not having an additional neighbor. Property 1 is true in this prediction network game.

Since the payoff function exhibits strategic substitutes, the payoffs $U ( m _ { i } , \sigma ; k _ { i } )$ have decreasing differences in $m _ { i }$ and $k _ { i \cdot }$ For $m _ { i } { ' } > m _ { i }$ and $k _ { i } ^ { \prime } > k _ { i } \mathrm { : }$

$$
U \left(m _ {i} ^ {\prime}, \sigma ; k _ {i} ^ {\prime}\right) - U \left(m _ {i}, \sigma ; k _ {i} ^ {\prime}\right) \leq U \left(m _ {i} ^ {\prime}, \sigma ; k _ {i}\right) - U (m _ {i}, \sigma ; k _ {i}).
$$

Let $\Sigma ^ { \mathrm { d e c } }$ be the set of non-increasing strategies. By the Topkis Theorem, each best response is non-increasing. Thus, we can apply the proof of the existence theorem (the Kakutani <sup>fi</sup>xed point theorem, see [12]) to the best response correspondence on $\Sigma ^ { \mathrm { d e c } }$ . The correspondence is non-empty and convex-valued, and it satis<sup>fi</sup>es the standard continuity conditions. Then, the existence of a symmetric equilibrium follows from the standard existence proof. ■

The intuition is that, under independence, degree k and degree $k _ { i } + 1$ players have the same beliefs about the degree of each of their neighbors. If the $( k _ { i } + 1 )$ th neighbor is choosing $m _ { i } = 0 ,$ , then because Property 1 holds in our game, the degree $k _ { i } + 1$ players still will choose the same best response as the degree $k _ { i }$ player. If the $( k _ { i } + 1 ) \mathrm { t h }$ neighbor chooses $m _ { i } = 1$ , then strict strategic substitutes imply that the degree $k _ { i } + 1$ players' best response is with a lower action. From Proposition 1, we know that there is a unique symmetric equilibrium strategy σ involving a threshold in the network game.

Proposition 1 has very clear implications. The player's equilibrium action is weakly decreasing in her degree. In other words, the more neighbors she has, the less willing she will be to acquire information. Higher degree players expect that they will receive more information from their neighbors; thus, they have less incentive to acquire costly information by themselves. The players can “free-ride” on the costly information acquisition of their neighbors. If player i has more neighbors, she is more likely to bene<sup>fi</sup>t from the signals passed by her neighbors. Because the marginal effects of signals in forecasting are decreasing, players with more neighbors are less willing to acquire costly information.

A few remarks are made here. Since all players adopt a threshold strategy, player i believe that the probability of acquiring information for a randomly chosen neighbor is $q = \mathrm { P r } ( k _ { j } \le k ^ { * } ) , \ j { \in } N _ { i } ( g )$ . player i's belief about the number of informed neighbors follows a binomial distribution given by

$$
f (k _ {a}; k _ {i}, q) = \binom{k _ {i}}{k _ {a}} q ^ {k _ {a}} (1 - q) ^ {k _ {i} - k _ {a}}.
$$

Knowing the belief of player i, we can obtain the expected payoff $U ( m _ { i } , \sigma ; k _ { i } )$ . Since $k ^ { * }$ is a threshold, it is determined by the following inequalities:

$$
\begin{array}{l} U (m _ {i} = 1, \sigma ; k ^ {*}) \leq U (m _ {i} = 0, \sigma ; k ^ {*}) \\ U (m _ {i} = 1, \sigma ; k ^ {*} + 1) > U (m _ {i} = 0, \sigma ; k ^ {*} + 1). \end{array}
$$

Corollary 1. In symmetric equilibrium, the expected payoffs are non-decreasing in degree.

## Proof. The result directly follows from Proposition 1. ■

In the corollary, we emphasize that in our network-embedded prediction market, players with more neighbors earn higher payoffs under the monotone equilibrium. Here, higher degree players exert lower effort, but they earn a higher payoff compared to their less connected peers because of free riding. The nonincreasing property of equilibrium actions implies that social connections create personal advantage. In the network-embedded prediction market, well-connected players earn more than poorly connected players.

## 4. Simulation results

We conduct a variety of agent-based simulations of agents trading in prediction markets to examine the forecasting performance of the social network-embedded prediction market. In every simulation round, we generate a random social network with 100 agents, by using a 100×100-dimensional matrix. The probability of a link between two agents is $p r { = } 0 . 7$ . The results are robust for other parameter values. Without loss of generality, we set the realization of future event $\nu = 5 0$ , the common prior

$$
V \sim N (V _ {0}, 1 / \rho_ {v}) = N (4 0, 1 0 0),
$$

and the noise of the signa $\varepsilon _ { i } { \sim } N ( 0 , \ 1 / \rho _ { \varepsilon } ) { = } N ( 0 , 1 0 0 )$

For each cost level of information acquisition, we do 100 simulations. Fig. 2 shows the dispersion of prediction market prices at different cost levels. The implication is similar to the efficient market hypothesis. As the cost of information decreases and more and more agents acquire information, the prediction market prices fully incorporate all available information, and the price dispersion becomes smaller; the prediction market yields good forecasts around $\nu = 5 0$ It demonstrates that when threshold $\overrightharpoon { k ^ { * } }$ is high (which implies that more agents acquire information), the forecasting performance of the network-embedded prediction market is better. Fig. 2 also reveals an interesting pattern: When only a small proportion of agents acquire information, an agent would receive very little information from her neighbors, and she would mainly use the prior information to generate a forecast. Therefore, the price dispersion is small at <sup>fi</sup>rst and is around the mean of the prior $V _ { 0 } = 4 0$ . As more and more agents acquire information, the agent receives differential information from the network, and with differences of opinions, price dispersion increases. When most of the agents acquire information, information is abundant in the social network, and the price dispersion becomes small again.

In Fig. 3, the forecasting errors decrease with the cost of acquiring information in our network-embedded prediction market. For prediction accuracy, we use the measure of averaged standard forecasting error, $\begin{array} { r } { \sqrt { \frac { 1 } { 1 0 0 } \sum _ { j = 1 } ^ { 1 0 0 } \left( P _ { j } - \nu \right) ^ { 2 } } } \end{array}$ , where $P _ { j }$ is the price of each simulation round. We also <sup>fi</sup>nd that the gain from reducing the prediction error is not signi<sup>fi</sup>cant as the cost decreases. The policy implication is important and straightforward. When the cost to acquire information is not high, a reduction in cost does not have a signi<sup>fi</sup>cant effect on market ef<sup>fi</sup>ciency.

The simulated forecasting errors in a prediction market without social networks are shown in Fig. 4. Compared to the social network-embedded markets, the network-embedded prediction market outperforms the non-networked prediction market in prediction performance when the cost is not too high. Example 1 shows this result analytically in a special social network structure: a circle network.

Please cite this article as: L. Qiu, et al., Social network-embedded prediction markets: The effects of information acquisition and communication on predictions, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.007

L. Qiu et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/ED8MW36U/fulltext/images/02289b69723e894a25810c5b11176a12a7f10965f8c7ff178e6e4067f5a0ac59.jpg)  
Fig. 2. Prediction market price and information acquisition.

## Example 1. A circle network

From Lemma 1, it is known that the marginal value of acquiring information in producing a more reliable forecast is decreasing. If player i does not receive any signals passed by other players in the social network, the marginal value of the <sup>fi</sup>rst signal is $M V _ { 1 } .$ Similarly, we can obtain the marginal value of the r-th signal: $M V _ { r }$ . The marginal value of the information is decreasing, so we have:

$$
M V _ {1} > M V _ {2} > \dots > M V _ {r} > \dots
$$

Consider a network-embedded prediction market, and we assume that $M V _ { 3 } > c > 0$ . In a circle network (see $\mathrm { F i g . } 5 ) ,$ , the unique Nash equilibrium is that all players acquire information. In this network-embedded prediction market, the price is given by:

$$
P _ {S N} = \frac {\rho_ {V}}{3 \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {3 \rho_ {\varepsilon}}{3 n \rho_ {\varepsilon} + n \rho_ {V}} \sum_ {i = 1} ^ {n} S _ {i},
$$

and the forecasting errors by:

$$
V a r [ P _ {S N} - V ] = \frac {9 \rho_ {\varepsilon} + n \rho_ {V}}{n (3 \rho_ {\varepsilon} + \rho_ {V}) ^ {2}}.
$$

![](/api/attachments/ED8MW36U/fulltext/images/fa23ff2483986b5d6e017bfff654bd3468fcdbf0722e39093d540c0ed0b00737.jpg)  
Fig. 3. Forecasting errors and information acquisition in a network-embedded prediction market

Please cite this article as: L. Qiu, et al., Social network-embedded prediction markets: The effects of information acquisition and communication on predictions, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.007

![](/api/attachments/ED8MW36U/fulltext/images/0eb12aeb1c3fdb5e577f9c2c1331b14ebb6bd05584292f4e253e369fe5be1ba9.jpg)  
Fig. 4. Forecasting errors and information acquisition in a prediction market without networks

Now let's consider a non-networked prediction market. Because $M V _ { 3 } > c > 0$ , each player acquires information in a non-networked prediction market, and the best forecast for player i is

$$
\frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} S _ {i}.
$$

The price can be obtained by the market-clearing condition:

$$
P _ {N} = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} \frac {1}{n} \sum_ {i = 1} ^ {n} S _ {i}.
$$

And the forecasting errors:

$$
\operatorname{Var} \left[ P _ {N} - V \right] = \frac {\rho_ {\varepsilon} + n \rho_ {V}}{n \left(\rho_ {\varepsilon} + \rho_ {V}\right) ^ {2}}.
$$

We can obtain:

$$
\operatorname{Var} \left[ P _ {N} - V \right] > \operatorname{Var} \left[ P _ {S N} - V \right].
$$

In other words, the forecasting errors in the network-embedded prediction market are smaller than those in the non-networked prediction market. Example 1 thus shows that the network-embedded prediction market outperforms the non-networked prediction market in the circle network when the cost is low.

![](/api/attachments/ED8MW36U/fulltext/images/28356735de76174244aea5a0178d075258bd3b5ea5ebdc113d2c3764d10632e1.jpg)  
Fig. 5. A circle network.

## 5. The design of Twitter-embedded prediction markets

Because the network-embedded prediction market might outperform the non-networked prediction market, a carefully designed network-embedded prediction market could generate more precise predictions. In this section, we design a Twitter-based prediction market by using a pari-mutuel betting mechanism. In the theoretical model, players are linked to each other as in a social network. In our information system design, a social network refers to a Twitter network. In the model, players exchange information with their neighbors. In the same way, information sharing on Twitter relies on voluntary user contributions. On Twitter, people can <sup>fi</sup>nd opinions and information on a broad range of topics posted by their peers almost in real time. “Neighbors" in the theoretical model can be interpreted as followers in the Twitter network.

The power of the prediction markets derives from the fact that the mechanisms provide incentives for truthful revelation, as well as for research and information discovery, and the market provides an algorithm for aggregating opinions. Refs. [3] and [4] discuss how a Bayesian learner updates his or her belief over a long period of time. As time goes to in<sup>fi</sup>nity, the Bayesian learner assigns a posterior probability of one to the correct hypothesis. However, our question focuses on how we can elicit dispersed information from a large number of people in <sup>fi</sup>nite periods. Fang, Stinchcombe, and Whinston [11] show that under very general conditions, some strict scoring rules exist that elicit the expert's true beliefs as probabilistic forecasts.

Many different prediction market mechanisms are available, including double auction, pari-mutuel betting, and a market maker mechanism. For our purposes in the Twitter-embedded prediction markets, we adopt a pari-mutuel betting mechanism. This option is widely used in sports betting; for instance, all bettings on horse races in the United States are pari-mutuel. Here, participants buy bets on each of the S possible states. Each bet costs one virtual dollar, and a participant spends all of his or her virtual endowment on buying bets. The total number of bets of each type that have been purchased is displayed publicly. The odds are updated by using budget balance conditions after each transaction. If W is the total budget and $h _ { s }$ is the total quantity of state-s bets purchased, then the odds for state-s are given by $O _ { s } { = } W /$ $h _ { s } ,$ which implies that if a participant buys ten \$1 bets on state $s ,$ he will receive $1 0 \cdot 0 _ { s }$ dollars when the realized state is s.

Please cite this article as: L. Qiu, et al., Social network-embedded prediction markets: The effects of information acquisition and communication on predictions, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.007

![](/api/attachments/ED8MW36U/fulltext/images/04448e99df604f541c3653e2ceffa420c9babb5442e6f95f0f9413eb5c4b2ba1.jpg)  
Fig. 6. A twitter-embedded prediction market.

Generally speaking, for pari-mutuel betting, the total amount of money bet on all outcomes is placed in a common pool. The money is returned to those who bet on the winning outcome. Pari-mutuel betting differs from <sup>fi</sup>xed-odds betting in that the odds are updated in real time, and the <sup>fi</sup>nal payout is not determined until the market is closed.

We set up a master account to follow all the participants of the prediction market on Twitter and designed a simple language that participants could use to place bets and to query information by sending tweets. We also collected participants' demographic information by using a pre-experiment survey. (See Appendix A, Pre-experiment survey.) One possible use of our Twitter-embedded prediction market – called IBET – is to forecast movie box of<sup>fi</sup>ce revenues, as shown in Fig. 6. When a player signs up, he receives some initial virtual money.<sup>10</sup>

Fig. 7 shows the betting intervals and odds for movies. If a player thinks “Sucker Punch” is an excellent movie, he can bet most of his virtual money on interval 4, which means that he predicts the box of<sup>fi</sup>ce revenue to be above \$40 million. Like the traditional prediction market, we still offer a website that allows participants to undertake their betting through the web interface. However, with our Twitter-integrated system, Twitter users can easily participate in our prediction market simply by sending us a direct message. When people are waiting or chatting and they come across some new information, they can take out their smart phones and place their bets accordingly. The purpose of such an easily accessible mechanism is to induce people to provide the information as soon as they have time and before they forget it. As more people participate and provide more information in a more timely manner, our prediction market potentially could outperform traditional prediction markets.

Because of the complexity and challenge of handling natural language processing, we have designed the language between the participants and our master account to be simple and straightforward. For example, a participant may send a direct message, “bet 10 1 green hornet,” to bet \$10 on interval 1 for the movie, “Green Hornet.” Our master account receives this tweet through Twitter, processes it, and then updates the participant's betting portfolio accordingly. On the other hand, if a participant sends a direct message, “query portfolio green hornet,” our master account sends a message back to the participant with her betting portfolio information. Similarly, users can query their balance by sending a message.

Fig. 8 shows the prediction market result for the movie, “Hall Pass.” The amount bet on interval 1 is \$194; on interval 2, \$474; on interval 3, \$238; on interval 4, \$70; and on interval 5, \$10. Therefore, participants think the box of<sup>fi</sup>ce revenue is more likely to be between \$10 million and \$20 million. The true opening weekend box of<sup>fi</sup>ce revenue was \$13,535,374, so the Twitter-embedded prediction market did a pretty good job. Based on our theoretical model, the use of networked markets affects information acquisition and improves the ef<sup>fi</sup>ciency of prediction markets.

## 6. Conclusions and future research directions

In this paper, we study a social network-embedded prediction market and show that participants adopt a threshold strategy in the Bayes–Nash equilibrium. We also demonstrate that the forecasting errors could be smaller in a social network-embedded prediction market. The managerial implication is that a networked prediction market can produce better predictions as a result of information exchange in social networks. As an application, we design a Twitterembedded prediction market that can induce people to provide information as soon as they have the time and before they forget it. Given that sending direct messages from smart phones is a more convenient mode of communication, we expect that, with more people participating and providing more information in a more timely manner, our prediction market potentially can outperform other prediction markets. Simulation results show that the Twitter-embedded prediction markets produce better predictions than the prediction markets without social networks.

Using a social network-embedded prediction market allows us to conduct <sup>fi</sup>eld experiments to study social learning and to measure the social distance of the participants by using network data. Coval and Moskowitz [8] <sup>fi</sup>nd that social networks help fund managers earn above-normal returns in nearby investments: The average fund manager generates an additional 2.67% return per year from local investments, relative to nonlocal holdings. Their results suggest that investors trade local securities at an informational advantage in the social networks, indicating a strong geographic link between mutual fund investment and performance. Generally speaking, investors in the same local, social network structure would exhibit similar local holdings and local performance. One explanation is that investors located near a <sup>fi</sup>rm can visit the <sup>fi</sup>rm's operations, talk to suppliers and employees, and gain access to private information [8]. However, Ref. [8] did not have data to measure the networks and social distance between investors and local corporate executives. Still unclear is how social learning of local investors occurs and how it varies in different social networks. Our Twitter-embedded prediction market exhibits similar characteristics to these social networks. As we collect more and more data from the embedded prediction markets, our future work is to test whether participants in the same local structure exhibit similar bets and prediction performance.

![](/api/attachments/ED8MW36U/fulltext/images/053b76dd79048d25b3224b9d1c620d480b697109b006c99a981318dd7b858aff.jpg)  
Fig. 7. Betting for movie box of<sup>fi</sup>ce revenue.

With Twitter-embedded prediction markets, future research can also examine the famous “strength of weak ties” theory [15]. The gist of the hypothesis is that we often get novel information from acquaintances instead of close friends. Strong ties usually result in informational redundancy, while weak ties are more likely to be the bridge for novel information to pass. Another future research direction is to examine the incentives for sharing information in a social network. In the current setup, we assume that people exchange information according to reciprocity and norms of fairness, rather than focusing on the incentives for sharing information. However, whether people have incentives to share information, and what those incentives are, remain open questions. A well-developed literature of “value of information” and “information sharing” has been generated in the setup without networks. For example, Gal-Or [13] shows that no information sharing is the unique equilibrium in an oligopolistic market. In addition, Prendergast [22] demonstrates the disadvantages of shared information: Individuals tend to conform to the opinions of others in a way that can be inef<sup>fi</sup>cient. Studying the incentives for sharing information in a social network would be an interesting extension of information sharing.

![](/api/attachments/ED8MW36U/fulltext/images/3c40489492f94b6245ecf811e249ddcc0fdfc352b70f60e4e099283370aba2a2.jpg)  
Fig. 8. A twitter-embedded prediction market for “Hall Pass”.

## Appendix A. Pre-experiment survey

We collected players' demographic information by a pre-experiment survey.

1. What is your gender?

a. Female b. Male

2. How old are you?

a. Under 15 b. 15–19 c. 20–29 d. 30–39 e. 40–49 f. 50 or above

3. How many years of formal education have you completed? (For example, if you have completed high-school, you may write 12; if you have completed college, you may write 16).

4. Please select the occupational category below that best describes your profession:

a. Executive, administrative, and managerial occupations

b. Engineers and engineering technicians

c. Teachers and instructors, counselors, and college faculty

d. Lawyers and judicial workers or health diagnosticians

e. Marketing and sales occupations

f. Service occupations

g. Students

h. Others

5. What is your email address?

6. How much time do you think you will devote to playing the prediction game per day?

a. Less than 5 min b. 5–10 min c. 10 min–30 min d. 30 min– 1 h e. more than 1 h.

Thank you for completing this survey! You will now be redirected back to the prediction game.

Please cite this article as: L. Qiu, et al., Social network-embedded prediction markets: The effects of information acquisition and communication on predictions, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.007

## References

[1] J. Berg, R. Forsythe, F. Nelson, T. Rietz, Results from a dozen years of election futures markets research, in: C.R. Plott, V.L. Smitt (Eds.), Handbook of Experimental Economics Results, North-Holland, 2008, pp. 742–751.

[2] J.E. Berg, G.R. Neumann, T.A. Rietz, Searching for Google's value: using prediction markets to forecast market capitalization prior to an initial public offering, Management Science 55 (3) (2009) 348–361.

[3] L. Blume, D. Easley, Evolution and market behavior, Journal of Economic Theory 58 (1) (1992) 9–40.

[4] L. Blume, D. Easley, If you're so smart, why aren't you rich? Belief selection in complete and incomplete markets, Econometrica 74 (4) (2006) 929–966.

[5] G. Burggen, M. Spann, G. Lilien, B. Skiera, Prediction markets as institutional forecasting support systems, Decision Support Systems 49 (4) (2010) 404–416.

[6] A. Calvo-Armengol, M.O. Jackson, The effects of social networks on employment and inequality, American Economic Review 94 (3) (2004) 426–454

[7] K. Chen, C. Plott, Information aggregation mechanisms: concept, design and implementation for a sales forecasting problem, California Institute of Technolog Social Science Working Paper No. 1131, 2002.

[8] J.D. Coval, T.J. Moskowitz, The geography of investment: informed trading and asset prices, Journal of Political Economy 109 (4) (2001) 811–841.

[9] P. Cramton, L.I. de Castro, Prediction markets to forecast electricity demand, Working Paper, University of Maryland, 2009.

[10] F. Fang, M. Stinchcombe, A.B. Whinston, Putting your money where your mouth is — betting mechanism design for better prediction, Review of Network Economics 6 (3) (2007) 214–238.

[11] F. Fang, M. Stinchcombe, A.B. Whinston, Proper scoring rules with arbitrary value functions, Journal of Mathematical Economics 46 (6) (2010) 1200–1210.

[12] A. Galeotti, S. Goyal, M.O. Jackson, F. Vega-Rendondo, L. Yariv, Network games, The Review of Economic Studies 77 (1) (2010) 218–244

[13] E. Gal-Or, Information sharing in oligopoly, Econometrica 53 (2) (1985) 329–343.

[14] B. Golub, M. Jackson, Naive learning in social networks and the wisdom of crowds, American Economic Journal: Microeconomics 2 (1) (2010) 112–149.

[15] M. Granovetter, The strength of weak ties, The American Journal of Sociology 78 (6) (1973) 1360–1380.

[16] S. Grossman, J. Stiglitz, On the impossibility of informationally ef<sup>fi</sup>cient markets, American Economic Review 70 (3) (1980) 393–408

[17] Z. Guo, F. Fang, A.B. Whinston, Supply chain information sharing in a macro prediction market, Decision Support Systems 42 (3) (2006) 1944–1958.

[18] G. Harrison, J.A. List, Field experiments, Journal of Economic Literature 42 (4) (2004) 1009–1055.

[19] M.O. Jackson, Social and Economic Networks, Princeton University Press, Princeton, NJ, 2008.

[20] W. Olszewski, A. Sandroni, Manipulability of future-independent tests, Econometrica 76 (6) (2008) 1437–1466.

[21] W. Olszewski, A. Sandroni, A nonmanipulable test, The Annals of Statistics 37 (2) (2009) 1013–1039.

[22] C. Prendergast, A theory of yes men, American Economic Review 83 (4) (1993) 757–770.

[23] L. Qiu, H. Rui, A.B. Whinston, A twitter-based prediction market, Proceedings of the 32th International Conference on Information Systems (ICIS), 2011.

[24] E. Servan-Schreiber, J. Wolfers, D. Pennock, B. Galebach, Prediction markets: does money matter? Electronic Markets 14 (3) (2004) 243–251.

[25] J. Surowiecki, The Wisdom of Crowds: Why The Many are Smarter than the Few and How Collective Wisdom Shapes Business, Economies, Societies, and Nations, Doubleday, New York, NY, 2004.

[26] J. Wolfers, E. Zitzewitz, Prediction markets, Journal of Economic Perspectives 18 (2) (2004) 107–126.

Liangfei Qiu is a Ph.D. candidate in the Department of Economics, University of Texas at Austin. He holds an M.S. in economics from the University of Texas at Austin. His current research focuses on the theoretical and empirical studies of social networks, prediction markets, procurement auctions, and applied game theory.

Huaxia Rui is an Assistant Professor at Simon School of Business, University of Rochester. Dr. Rui got his Ph.D. in information systems, risk, and operation management from McCombs School of Business, the University of Texas at Austin. His research interests include the study of social media, online advertising, securitization, and operation management.

Andrew Whinston is the Hugh Roy Cullen Centennial Chair in Business Administration, Professor of Information Systems, Computer Science and Economics, and Director of the Center for Research in Electronic Commerce at the University of Texas at Austin He is the co-author or co-editor of 23 books and over 300 articles. Dr. Whinston re ceived his Ph.D. from Carnegie Mellon University.
