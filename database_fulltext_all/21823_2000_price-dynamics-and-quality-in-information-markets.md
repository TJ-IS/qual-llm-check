---
otero_id: 21823
otero_key: "JKHWSMYZ"
title: "Price dynamics and quality in information markets"
authors: "Jakka Sairamesh; Jeffrey O Kephart"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00073-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Price dynamics and quality in information markets

Jakka Sairamesh, Jeffrey O. Kephart

IBM T.J. Watson Research Center, Hawthorne, NY 10532, USA

## Abstract

We explore the price dynamics of a vertically differentiated market in which two or more sellers compete to provide an information good or service to a population of buyers. Each seller offers the good or service at a fixed level of ‘‘quality’’, and attempts to set its price in such a way that it maximizes its own profit. Five different seller pricing strategies, ranging widely from ones that require perfect knowledge and unlimited computational power to ones that require very little knowledge or computational capability, are employed in two different buyer populations. The resulting collective dynamics are studied using a combination of analysis and simulation. In a population of quality-sensitive buyers, all pricing strategies lead to a price equilibrium predicted by a game-theoretic analysis. However, in a population of price-sensitive buyers, most pricing strategies lead to large-amplitude cyclical price wars. The circumstances under which cyclical price wars occur can be explained in terms of the topology of an underlying ‘‘profit landscape’’ J.O. Kephart, J.E. Hanson, J. Sairamesh, Price<sup>w</sup> and niche wars in a free-market economy of software agents, Artificial Life Journal, 4 1 , 1998, 1–23 .Ž .  q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Price dynamics; Information market; Product quality

## 1. Introduction

In the coming years, the explosive growth in electronic commerce can be expected to continue, fueled in large part by increasing automation. Much of this automation will be cast in the form of autonomous software agents. Matchmaking and advertising agents will help people and other agents to find customers or suppliers. Agents will help negotiate prices, product parameters, and terms of contracts, and then carry out the transactions. Agents will encapsulate data-mining and other technologies that allow various forms of transaction postprocessing, enabling better-targeted advertising, for example. We envision a world a decade or two hence in which billions of software agents will act as economic players in their own right, exchanging information goods and services with humans and with other agents 4,6,7 .<sup>w</sup> <sup>x</sup>

It is quite conceivable that the inclusion of large numbers of software agents as economic players will have a strong effect upon the global economy, giving rise to collective phenomena that are rare or even unknown in today’s economy. We believe this because software agents differ from human agents in a number of economically relevant ways. They are capable of making decisions of orders of magnitude faster than humans make, and can potentially base those decisions on greater volumes of much fresher information. Within limited domains, they are, in some cases, more capable than humans. In general, however, they are considerably less intelligent and flexible. Our previous work on an economy of information-filtering agents has shown that these differences, coupled with the reduced friction that one expects to find in agent-based information economies, can engender rampant price wars in which sellers prices undergo periodic oscillations that can be harmful to sellers and buyers alike 4,6,7 .<sup>w</sup> <sup>x</sup>

Another important distinguishing feature of software economic agents is that they are fundamentally more consistent and understandable in their individual behavior than their human counterparts. Understanding and modeling the decision-making behavior of individual humans is notoriously difficult. Mathematical utility functions are often used to model human choices, but this can only be taken to be a rough approximation. In contrast, the behavior of a software agent is codified completely in the form of a computer program. Thus, models of software agents can be regarded as proposals for, rather than mere approximate descriptions of, the behavior of boundedly rational individuals. This permits a different research emphasis. Rather than measuring our success in terms of our ability to understand individual and societal behavior, our goal is to design an agent economy that will work well from the perspective of the individual agents that participate in it. Our study of the collective dynamics of large number of economic software agents 4–7 is not an end in itself; it is motivated by the hope that we can derive principles that will help us design effective agent strategies, interaction protocols, and market mechanisms <sup>w</sup> <sup>x</sup> <sub>9</sub> <sub>.</sub>

The information-filtering economy that we have studied previously is an example of a horizontally differentiated <sup>w</sup> <sup>x</sup> 15 market: an article that is worthless to one consumer may be priceless to another. However, in a broad information economy of the sort we envision, there will also be a number of markets in which information goods and services are Õertically differentiated, i.e., there is near-universal agreement among consumers of what constitutes higher or lower quality.

For example, a population of human or softwareagent consumers of network services will have diverse requirements, and network providers will jockey for position in the market by offering a variety of tradeoffs between price and quality of service QoS . Note that, in general, quality may beŽ . a multi-dimensional concept 1,2,14,15 . An agent<sup>w</sup> <sup>x</sup> representing a multimedia application might require a transmission rate of 1.5–3.0 Mb<sup>r</sup>s in order to support compressed real-time video MPEG-II orŽ JPEG . Additionally, it might require a maximum . packet-loss probability of 1% and a maximum packet delay of 20 ms in order to support a minimum guaranteed viewing quality. Suppose that a given provider can meet these basic requirements for a certain fee. The multimedia agent might still prefer to patronize a higher-priced supplier that offers a higher transmission rate, a lower packet-loss probability, or a smaller packet delay. The degree to which it is willing to pay for extra quality in any of these three dimensions depends on how that extra quality will translate into improvements in the quality of the service that the multimedia agent can offer to its customers, and how much more it could charge for this improved service. As the demands placed on the multimedia agent may vary from one moment to the next, so in turn will the demands that it makes upon the network service providers. A network services market will be expected to offer multiple services at multiple rates, with low costs and latencies for switching from one service type to another. Market mechanisms capable of supporting these requirements are a topic of active research 8,10 .<sup>w</sup> <sup>x</sup>

As a second example, consider a market in which information brokers compete to provide information-filtering services. As has been discussed, the varied preferences among users for different categories of information induce horizontal differentiation. However, there may be several vertical dimensions as well. Different brokers could offer different response times. One broker could, by using a faster processor or a much clever algorithm, implement a more sophisticated and accurate filtering algorithm than another.

Numerous works in the economics literature treat various aspects of the behavior of horizontally and vertically differentiated markets 1–3,11–13,15,16 .<sup>w</sup> <sup>x</sup> In Ref. 1 , price and quality equilibria are discussed<sup>w</sup> <sup>x</sup> under specific oligopolistic settings. This paper differs from these previous works in that it presents a comparative study of non-equilibrium price dynamics resulting from a wide range of different individual pricing strategies that might be employed by software agents. This paper also differs from our own previous work in that it considers a vertically — rather than a horizontally — differentiated market. We are particularly interested in determining whether vertically differentiated markets are vulnerable to the same pathological, cyclical price wars that we have observed previously in a horizontally differentiated market, in which seller agents offer filtered streams of news articles to buyer agents 4,6 . <sup>w</sup> <sup>x</sup>

After presenting the model in Section 2, we shall find in Sections 3 and 4 that, under some circumstances, the model does exhibit cyclical price wars. In Section 5, we discuss the mechanisms that underlie these dynamics, and conclude that, just as in our previous work, much can be attributed to the topology of the sellers’ profit landscapes. Finally, we summarize our findings and point out directions for future work in Section 6.

## 2. Model

The model, illustrated in Fig. 1, consists of S sellers and B buyers. Each seller offers a single product or service henceforth referred to generically Ž as a unit . The unit may have a number of different. attributes, each with several discrete possible values, or a continuous range of possible values. However, we shall make the simplifying assumption that the preferences of the buyers are correlated in such a way that there exists a universally agreed-upon mapping that transforms a unit’s set of attributes and values, however complex this may be, into a simple scalar quality. <sup>1</sup>

![](/api/attachments/JKHWSMYZ/fulltext/images/b541c14c2d47dedaf47b10f9172d4ed8f9ba0cea7a00b501859205ef26b1cfc2.jpg)  
Fig. 1. Vertically differentiated market economy of software agents.

Through some mechanism such as a bulletinŽ board , all buyers are informed about the price. $P _ { s }$ and quality $Q _ { s }$ of units offered by each seller s. The qualities $Q _ { s }$ may be reported by the sellers assumed Ž to be honest , or alternatively they could be mea-. sured or derived and then reported by an independent, trusted third party.

For simplicity, we assume that time is discrete. Ž . This is not an essential aspect of the model. At any given moment t, each buyer purchases a unit from at most one of the sellers — either the one it perceives to be the best choice given its understanding of the prices and qualities, or none if no seller’s offer is sufficiently attractive. Note that a buyer’s understanding of the prices and qualities may be imperfect and delayed because it may not have the resources or ability to continuously monitor them.

We model a buyer’s decision-making process as follows. Each buyer b has a utility function $u _ { b } ( \hat { P } ;$ $\hat { Q } )$ , which is a single-valued function of the perceived price $\hat { P }$ and perceived quality $\hat { Q }$ of a prospective supplier. The buyer b will select the single seller s for which $u _ { b } ( \mathinner { \hat { P } } , \hat { Q } )$ is maximized, so long as that maximal utility is positive, and purchase a unit at the actual price $P _ { s }$ . If the maximal utility is zero or negative, the buyer does not purchase a unit from any seller. In this paper, we will take the utility functions to have the simple form

$$
\begin{array}{r l} u _ {b} & = \left(\gamma_ {b} (q - \bar {q} _ {b}) + (1 - \gamma_ {b}) (\bar {p} _ {b} - p)\right) \\ & \times \Theta (\bar {p} _ {b} - p) \Theta (q - \bar {q} _ {b}) \end{array}\tag{1}
$$

where $\overline { { p } } _ { b }$ is the buyer’s price ceiling the maximumŽ price it is willing to pay ,. $\overline { { q } } _ { b }$ Ž is its quality floor the minimum quality it is willing to accept ,. $\gamma _ { b }$ is a parameter in the range 0,1 , and<sup>w</sup> <sup>x</sup> $\Theta ( x )$ represents the step function: 1 for $x > 0$ and 0 otherwise. A buyer with $\gamma _ { b } = 0$ is at the extreme limit of price sensitivity: it will choose the seller with the lowest price, just so long as its quality is no less than the quality floor $\overline { { q } } _ { b }$ . A buyer with $\gamma _ { b } = 1$ is at the extreme limit of quality sensitivity: it will choose the seller with the highest quality, just so long as its price is no more than the price ceiling $\bar { p } _ { b }$

For a given set of assumptions about how the estimated prices and qualities $\hat { P _ { s } }$ and $\hat { Q } _ { s }$ are obtained from the actual values $P _ { s }$ and $Q _ { s }$ , a buyer $^ b$ can be characterized completely by its set of three parameters $( \overline { { p } } _ { b } , \overline { { q } } _ { b } , \gamma _ { b } )$

The sellers are somewhat more complex in behavior. At time t, several events may occur. Firstly, at most one randomly selected seller is given the opportunity to revise and publicize its price $P _ { s }$ and<sup>r</sup>or quality $Q _ { s }$ . There is no cost for doing so. Then, each buyer is given the opportunity to receive and make use of this updated information if it wishes toŽ . revise its choice of seller. Finally, each seller receives $P _ { s }$ from each buyer that has selected it, and pays a cost $c ( Q _ { s } )$ Žassumed to increase monotonically with $\boldsymbol { Q } _ { s } )$ to produce this good and deliver it to the buyer.

When a seller has the opportunity to modify its price and<sup>r</sup>or quality, its decision is based upon an attempt to maximize its own profit. Various assumptions may be made about the nature and accuracy of information available to the seller, as well as its computational capability. In this paper we will consider the following five strategies that cover a broad range of assumptions.

<sup>Ø</sup> A game-theoretic strategy can be used in the limit of perfect knowledge about the entire market, including all buyers and sellers and their strategies, and unlimited computational capability.

<sup>Ø</sup> A myoptimal, or ‘‘myopically optimal’’ strategy requires virtually unlimited computational capability and full information about the consumer population’s desires and the prices and qualities of competitors. However, the strategies of the competitors are unknown, and the myoptimal seller simply assumes that the status quo will be maintained i.e.,Ž the other sellers will not change their parameters before the seller has another opportunity to reset its parameters . The myoptimal seller performs an ex- . haustive search over all of the parameters over which it has control. For each potential setting of parameters, it computes the expected profit per unit time under the assumption that no other sellers change their parameters. It chooses the parameter setting that yields the highest expected profit.

<sup>Ø</sup> A computationally limited myoptimal strategy, which is like the myoptimal strategy except that the computational capabilities are weaker: an exhaustive search of all possible new parameter settings is replaced with a tighter search in the neighborhood of the current parameter set, with a few random forays further afield. From this smaller set of candidate parameter settings, the one yielding the highest expected profit is chosen.

<sup>Ø</sup> A trial-and-error strategy, in the extreme limit where sellers have no knowledge of one another and no knowledge of the consumer population. In the trial-and-error approach, new prices are generated randomly and tried out for a short period. If profits are found to improve after the adoption of a new price, that price is retained. Otherwise, the previous price is reinstated.

<sup>Ø</sup> A deriÕatiÕe-following strategy, in the extreme limit where sellers have no knowledge of one another and no knowledge of the consumer population. A derivative follower simply experiments with its parameters, continuing to change them in the same direction until the observed profitability is reduced, at which point the direction of change is reversed.

For example, consider the case in which the derivative follower adjusts its price only. Then the new price at time t can be expressed in terms of the prices and average profits per unit time at earlier times $t ^ { \prime }$ and $t ^ { \prime \prime }$ via:

$$
p _ {t} = p _ {t ^ {\prime}} + \delta \mathrm{sign} (\pi_ {t ^ {\prime}} - \pi_ {t ^ {\prime \prime}}) \mathrm{sign} (p _ {t ^ {\prime}} - p _ {t ^ {\prime \prime}})\tag{2}
$$

where $\pi _ { \mathrm { t ^ { \prime } } }$ and $\pi _ { t ^ { \prime \prime } }$ represent the average profits made during the time intervals $\left( t ^ { \prime } , \ t \right)$ and $\left( t ^ { \prime \prime } , ~ t ^ { \prime } \right)$ , respectively. The price increment is chosen from a uniform distribution between 0 and a small positive value. Experimentation has shown that randomizing can be very advantageous, as it greatly reduces the likelihood of getting caught in small depressions in the profit landscape that arise in systems of finite size.

There are numerous questions that one might ask about the collective behavior that arises in such a model under various assumptions about the consumer population, including the accuracy of the buyers’ estimates of current prices and qualities, the joint distribution of consumer parameter sets $( { \bar { p } } , { \bar { q } } $ $\gamma ) _ { : }$ , the sellers’ parameter update strategies, etc. Can a reasonable, stable equilibrium set of prices be reached under conditions of information delay and uncertainty? Are there reasonable price-adjustment or quality-adjustment strategies for sellers to pursue, even when they have imperfect, incomplete information and<sup>r</sup>or limited computational capabilities? If an equilibrium is reached, how favorable is it for the various sellers and buyers in the system?

This work addresses only a subset of these questions. We restrict ourselves to the study of two consumer populations generated by widely different consumer parameter distributions. First, we study a population of buyers that are quality sensitiÕe, i.e., each buyer seeks the highest quality seller whose price does not exceed that buyer’s budget. The second population of buyers is price sensitiÕe, i.e., each buyer seeks the cheapest seller that meets that buyer’s minimum quality requirement. For each of these populations, we perform five experiments. In each experiment, we assume that each seller adopts a given one of the five price adjustment algorithms outlined above, and we observe the resulting price dynamics.

## 3. Price dynamics for quality-sensitive buyers

Assume that each buyer b has $\gamma _ { b } = 1$ and $\overline { { q } } _ { b } = 0 ;$ that is, it is extremely quality-sensitive, seeking the highest-quality seller for which the price does not exceed $\overline { { p } } _ { b }$ . Assume that the number of buyers $B $ $^ \infty ,$ and that $\overline { { p } } _ { b }$ is distributed uniformly in the inverval 0,1 . Furthermore, assume that every buyer has Ž . access to perfect, completely up-to-date information about the sellers’ prices and qualities. Finally, assume that each seller s’s quality $Q _ { s }$ is immutable, so that the sellers are only free to set their prices. This allows the cost for seller s to be abbreviated as a fixed constant $c _ { s } \equiv c ( Q _ { s } )$

Now we can compare the behavior of the system under several different assumptions about the profitmaximization strategies employed by the sellers. Without loss of generality, we can order the sellers such that $s = 1$ is the seller with the highest quality, $s = 2$ is the seller with second-highest quality, etc. Then seller 1 will attract all buyers for which $P _ { 1 } \leq$ $\overline { { p } } _ { b } \leq 1$ , and in general taking Ž $P _ { 0 } = 1 )$ seller s will attract all buyers for which $P _ { s } \leq \bar { p } _ { b } \leq P _ { s - 1 }$ . Thus, the profit for seller s will be

$$
\Pi_ {s} = \big (P _ {s} - c _ {s} \big) \big (P _ {s - 1} - P _ {s} \big)\tag{3}
$$

provided that $P _ { s } > c _ { s }$ and $P _ { s } < P _ { s ^ { \prime } }$ for all $s ^ { \prime } < s .$ . IfŽ the first condition were not satisfied, then seller s would lose money on each sale because it would be charging less than the marginal cost. If the second condition were not satisfied, $\varPi _ { s } = 0$ because s would be undersold by a higher-quality seller..

First, suppose that the sellers behave game-theoretically. Seller $s = 1$ is free to set its price at will because any buyer that is willing to pay its price $P _ { 1 }$ Ži.e., $\overline { { p } } _ { b } > P _ { 1 } )$ will prefer it, since no other seller offers higher quality. Taking the derivative of Eq. 3 with respect to $P _ { 1 }$ and setting equal to zero easily yields the conclusion that the optimal price $P _ { 1 } ^ { * } =$ $1 / 2 ( 1 + c _ { 1 } )$ . Once $s = 1$ has set its price, $s = 2$ can determine its price using the same technique, and so on. In general, we find that $P _ { s } ^ { * } = 1 / 2 ( P _ { s - 1 } + c _ { s } ) .$ or $P _ { s } ^ { * } = 1 / 2 ( P _ { s - 1 } ^ { * } + c _ { s } )$ . Recursive substitution yields a simple closed-form expression:

$$
P _ {s} ^ {*} = 2 ^ {- s} + \sum_ {j = 1} ^ {s} 2 ^ {- j} c _ {s + 1 - j}\tag{4}
$$

The same analysis holds for myoptimal sellers. The highest quality seller is completely unaffected by the prices charged by its competitors. It can act as though it is the only seller in the market, compute its optimal price, and ignore the rest of the sellers because none can compete on quality. Once s<sup>s</sup>1 has established its price, the seller with the second highest quality concedes the premium buyers to $s =$ 1, and acts as the highest quality seller in the remaining market, and so on recursively, resulting in exactly the same equilibrium prices as are given in Eq. 4.

![](/api/attachments/JKHWSMYZ/fulltext/images/ece9b642047db79f6a3a107dd177bbbb9ba81f7ca2a37d412f860808bdb68a38.jpg)  
Fig. 2. Simulation of five myoptimal sellers. All buyers are quality-sensitive.

As an example, we now examine the behavior of a system with five sellers with fixed qualities $Q _ { 1 } =$ 1.0, $Q _ { 2 } = 0 . 9$ $Q _ { 3 } = 0 . 5 ,$ $Q _ { 4 } = 0 . 3 5$ , and $Q _ { 5 } = 0 . 2 5$ The cost of producing a unit of quality Q is taken to be a simple linear function: $c ( Q ) = 0 . 1 + 0 . 1 Q .$ . If the five sellers behave in a game-theoretic manner and the number of buyers is infinite, then the resultant prices can be computed from Eq. 4: $P _ { 1 } = 0 . 6 0 0$ $P _ { 2 } = 0 . 3 9 5$ $P _ { 3 } = 0 . 2 7 3$ $P _ { 4 } = 0 . 2 0 4$ , and $P _ { 5 } = 0 . 1 6 4$ Now suppose that the sellers use the myoptimal strategy. In other words, when it is a seller’s turn to re-evaluate its price, it does an exhaustive search over all possible candidate prices as follows. For each candidate price, it uses its knowledge of its competitors prices and qualities and its knowledge of the individual parameters of each of the buyers to compute the expected profit for that candidate price. ŽEquivalently, an oracle could perform this computation on the seller’s behalf. It chooses the candidate. price that maximizes its expected price, assuming that no competitor will alter its price in response.

Fig. 2 illustrates a typical simulation run for a population of five myoptimal sellers and 1000 buyers. After just a few time steps, the simulated system reaches an equilibrium in which the prices are very close to the game-theoretic values: $P _ { 1 } = 0 . 6 2 7 1 5 7$ $P _ { \mathrm { 2 } } = 0 . 3 9 2 5 0 6$ $P _ { 3 } = 0 . 2 6 6 3 9 9$ $P _ { 4 } = 0 . 1 8 9 8 6 2$ , and $P _ { 5 } = 0 . 1 6 5 1 5 0$ The small discrepancies can be attributed to the fact that the number of buyers in the simulated system is finite rather than infinite.

Computationally limited myoptimal sellers have access to the same unlimited information that myoptimals do, but are more limited in computational capability. They differ from myoptimals only in that they do not perform an exhaustive search over all possible prices. Instead, they randomly generate a small set of candidate prices, use their perfect knowledge of all competitors and individual buyers or anŽ oracle to compute the expected profit for each can- . didate price, and select the best price. In our implementation, computationally limited myoptimals consider the current price and 10 other randomly generated candidate prices. With probability 0.9, the candidate prices are generated from a Gaussian distribution with standard deviation 0.02 centered about the current price. With probability 0.1, the proposed price is chosen from a uniform distribution in the interval 0,1 . A typical simulation run is illustrated Ž . in Fig. 3. After 5000 time steps, the equilibrium prices were 0.627156, 0.384965, 0.252813, Ž 0.189860, 0.163891 — again, reasonably close to. the game-theoretic values.

It is useful to consider the opposite extreme, in which sellers are uninformed about their competitors and the buyer population. In this case, the sellers must use some sort of trial and error, perhaps coupled with memory and $/ \mathrm { o r }$ learning. One extremely simple approach is to use the trial-and-error strategy: when it is time to re-evaluate price, with a small small-jumping probability 0.05 , generate a newŽ . price by adding a small random increment drawn from a zero-mean Gaussian distribution with a small standard deviation 0.02 . Even less frequently, with Ž . some very small big-jumping probability 0.001 ,Ž .

![](/api/attachments/JKHWSMYZ/fulltext/images/6fd163667915bd7c3d81c3565b76909c254ad195570047fdfdee7c33a8f3f8b9.jpg)  
Fig. 3. Simulation of five computationally limited myoptimal sellers. All buyers are quality-sensitive.

generate a new price by drawing it from a uniform distribution in the interval 0,1 . If the price has justŽ . undergone a small or big jump, the profit that accrues until the next opportunity for a price adjustment is measured. The profit per unit time is compared to what it was prior to the jump. If it is higher, then the new price is retained. If it is not, then the price reverts to what it was before.

A typical simulation run is shown in Fig. 4. Again, the prices tend towards an approximate equilibrium, although it is impossible for them to settle completely due to the nature of the algorithm. Averaging over the last 1000 time steps, the approximate equilibrium price vector was 0.6271, 0.3889, 0.2518,Ž 0.1849, 0.1434 , which is fairly close to the com-. puted game-theoretic equilibrium.

A second algorithm that can be used in situations where sellers have no direct knowledge of competitors or buyers is the derivative-following algorithm. A derivative follower starts by measuring its profitability and then perturbing its price up or down by a random amount. If, when the seller next reevaluates its price, it finds that the profit per unit time has increased, it will modify the price in the same direction as before; otherwise, it will reverse the direction of the price change. We have found it helpful to use a random step size; this avoids entrapment at ‘‘false’’ local maxima in the profit curve that exist in systems with a finite number of buyers.

A typical simulation run with step size chosen uniformly between 0 and 0.02 is shown in Fig. 5. An average over the last 1000 time steps yields a price vector 0.6292, 0.4028, 0.2689, 0.2050, 0.1701 ,Ž . which is again fairly close to the computed gametheoretic value.

![](/api/attachments/JKHWSMYZ/fulltext/images/8a7fe38c49fe8e98cf1cdc5b8fb904a195dfa20871d5e0fb5bcfbbf6a1d70bef.jpg)  
Fig. 4. Simulation of five sellers, each of which employs the trial-and-error pricing policy. All buyers are quality-sensitive.

![](/api/attachments/JKHWSMYZ/fulltext/images/0c299ee7836c4fe95a383c162b5a5514349f29061e8583afbd3930efd6361dcc.jpg)  
Fig. 5. Simulation of five derivative-following sellers. All buyers are quality-sensitive.

## 4. Price dynamics for price-sensitive buyers

Now consider the opposite extreme, in which the buyers are completely price sensitive: provided that a certain minimal quality level $\overline { { q } } _ { b }$ is met, b seeks the least expensive seller. This limit is obtained by setting $\gamma _ { b } = 0$ for all b. We shall again assume that $\overline { { p } } _ { b }$ is distributed uniformly in the interval 0,1 . WeŽ . make the further assumption that the price ceiling and quality floor are perfectly correlated: buyers that require high quality are more tolerant of paying a higher price for that quality. This can be achieved Ž . for example by setting $\overline { { q } } _ { b } = \overline { { p } } _ { b }$

Just as we did for quality sensitive buyers, we assume that every buyer has access to perfect, completely up-to-date information about the sellers prices and qualities, and that each seller s’s quality $Q _ { s }$ is immutable, so that the sellers are only free to set their prices.

As before, we first compute the game-theoretic prices, and then examine the collective behavior of the system when all sellers employ the price-updating algorithms described previously. Again, we can, without loss of generality, order the sellers such that s <sup>s</sup> 1 is the seller with the highest quality, $s = 2$ is the seller with second-highest quality, etc. Then, as computed in the Appendix,

![](/api/attachments/JKHWSMYZ/fulltext/images/f681a5272e50c95b9c7fef002dc2624acc47e5a1deeabc1bfe912ff79449da53.jpg)  
Fig. 6. Simulation of five myoptimal sellers in a cyclic price war. All buyers are price-sensitive.

$$
P _ {j} ^ {*} = \max \left[ Q _ {j + 1}, \left(Q _ {j} + c _ {j}\right) / 2 \right].\tag{5}
$$

Evaluating this numerically for the set of five sellers studied in the previous section, we find that the game-theoretic price vector $( P _ { 1 } , P _ { 2 } , P _ { 3 } , P _ { 4 } , P _ { 5 } ) =$ Ž .0.9, 0.545, 0.35, 0.25, 0.1875 .

Fig. 6 shows the results of a typical simulation run of this system in the case where all five sellers are myoptimal. All parameters are identical to those used in the simulation represented in Fig. 2, except for the buyer parameters, which are exactly as described in the first paragraph of the current section. In contrast to what was found in Section 3, the system of myoptimal sellers does not reach the game-theoretic equilibrium price — in fact, it fails spectacularly to reach any equilibrium at all. The system regularly passes through a price vector that is extremely close to the game-theoretic value: $( P _ { 1 } , P _ { 2 }$ $P _ { 3 } , \ P _ { 4 } , \ P _ { 5 } ) = ( 0 . 9 0 0 , 0 . 5 2 3 , 0 . 3 5 0 , 0 . 2 5 2 , 0 . 1 8 5 )$ at times $t = 5 6 5 + 5 6 0 n$ , where $n = 0 , 1 , 2 , . . { }$ . However, on the next time step, the highest quality seller $s = 1$ realizes that it can make more profit by dropping its price from 0.900 to 0.523, the price currently charged by $s = 2$ . Although its margin drops from 0.7 per unit to 0.323 per unit the production cost isŽ $c ( Q _ { 1 } = 1 ) = 0 . 2 )$ , it steals the market formerly held by $s = 2 .$ , resulting in an increase in sales volume from 0.1 B to 0.477B. However, this gain is shortlived because $s = 2$ immediately retaliates by settings its price just slightly below that of $s = 1$ . Now $s = 1$ is reduced back to its market share of 0.1 B, and is making much less per unit than it was at the original price of 0.900. Thus $s = 1$ retaliates by matching $s = 2 ?$ s lowered price. The war between $s = 1$ and $s = 2$ continues, with the other three sellers staying at fixed prices that are essentially equal to the game-theoretic values. Eventually, the two warring sellers suddenly find it worthwhile to horn in on $s = 3 ^ { \circ } \mathrm { s }$ market. The top three sellers continue in a three-way price war, until the price becomes so depressed that $s = 1$ finally opts out and sets its price back up to 0.900. Once this price pressure is off, the other sellers all set their prices up to their game-theoretic values, but as soon as this occurs then s <sup>s</sup> 1 is tempted to instigate a new price war.

A simulation of computationally limited myoptimal sellers, shown in Fig. 7, displays very similar behavior. The price wars are somewhat faster than in the pure myoptimal case, because, while the sellers easily find that undercutting is myopically favor- Ž . able, they usually undercut by more than is absolutely necessary. There is some additional jitter introduced into the price-war period because s<sup>s</sup>1 and the other higher-quality sellers may take a little longer than pure myoptimals to realize that they should opt out of a price war.

As shown in Fig. 8, derivative followers quickly gravitate towards the game-theoretic prices, and do not engage in price-war behavior. During the interval from time 10,000 to time 50,000, the average prices are measured to be 0.89556, 0.53141, 0.35784,Ž 0.25377, 0.18556 , and tend to stay within approxi-. mately 0.03 of these values.

![](/api/attachments/JKHWSMYZ/fulltext/images/ce3de221609ea78f73fc97377655cb35d0806381f4d5eed861fb4cad1a5a5429.jpg)  
Fig. 7. Simulation of five computationally limited myoptimal sellers in a series of price wars. All buyers are price-sensitive.

![](/api/attachments/JKHWSMYZ/fulltext/images/b4d0bb1661c53b48b15454e3df072014a81bc726dbc50c4deeba52a723128466.jpg)  
Fig. 8. Simulation of five derivative followers that reach price equilibrium, computed via game theory. All buyers are price-sensitive.

It might be tempting to conclude at this point that myoptimal and nearly myoptimal sellers are too clever for their own good, and that the individual ignorance of the derivative followers is responsible for overall societal bliss at least on the part of theŽ sellers, not necessarily the consumers! However,. this is wrong on at least two counts. First, even if individual ignorance could be shown to lead to good societal behavior, this would not necessarily be a useful result because in an open, massively distributed agent economy we are very unlikely to be able to legislate an agent’s degree of intelligence. In other experiments, we have found that a single myoptimal agent introduced into a society of derivative followers can take tremendous advantage of its fellow agents. Thus, there is every incentive to create an intelligent agent rather than a stupid one. Second, it is untrue that simplistic strategies lead to stable behavior, as we are about to see.

Fig. 9 illustrates a typical simulation run with five sellers employing the trial-and-error pricing strategy. Despite a large amount of jitter due to the sellers continual random explorations, two longer-scale trends are evident: roughly metastable periods, during which the prices are roughly equal to the gametheoretic values, and price-war episodes see in par-Ž ticular the period between time 32,500 through time 40,000 . This example shows that price wars are not. an artifact of having an unrealistic amount of knowledge and computational power; they can occur even when an incredibly simplistic pricing strategy is used.

![](/api/attachments/JKHWSMYZ/fulltext/images/41b922a11f8cf6504319ebcbe758fe3f38797b34e7c382b2b9faa227c3f57b42.jpg)  
Fig. 9. Simulation of five sellers employing trial-and-error pricing strategy. All buyers are price-sensitive.

## 5. Topology and dynamics

In Section 3, all of the pricing strategies converged towards the game-theoretic equilibrium price vector, regardless of their sophistication or naivete. In Section 4, we only made a few changes to the buyers, and found that large-amplitude price wars were possible unless the sellers were derivative followers, in which case the game-theoretic analysis held. How can this behavior be explained?

As has been discussed in 4,6,7 , the profit land-<sup>w</sup> <sup>x</sup> scape is a useful construct for understanding pricewar dynamics. A seller’s profit landscape is its expected profit as a function of all of the sellers’ prices Ž . and any other parameters they may control , assuming that buyers can react instantly to any changes in the sellers’ parameters. Cyclical price wars are possible when profit landscapes contain multiple peaks and sharp cliffs.

![](/api/attachments/JKHWSMYZ/fulltext/images/5d533b4b5b37154f9a1fa8a558272d6d2dcf7d14ff3acf978775c38f8bf44b63.jpg)  
Fig. 10. Profit landscape for seller 1 in two-seller market with quality-sensitive buyers. The sellers’ qualities are $Q _ { 1 } = 1 . 0 , \ Q _ { 2 } =$ 0.9.

A typical pair of profit landscapes for a two-seller system with a population of buyers as defined in Section 3 is illustrated in Figs. 10 and 11. Analysis confirms that, for buyers of this type, profit landscapes are quite generally single-peaked and devoid of cliffs.

For the buyer population defined in Section 4, the landscapes have the following analytic form for two sellers:

$$
\begin{array}{l} \Pi_ {1} (P _ {1}, P _ {2}) \\ = \left\{ \begin{array}{l l} (Q _ {1} - P _ {1}) (P _ {1} - c _ {1}) & \text { if } 0 \leq P _ {1} \leq P _ {2} \text { or } \\ & \text { if } P _ {1} > Q _ {2} \\ (Q _ {1} - Q _ {2}) (P _ {1} - c _ {1}) & \text { if } P _ {2} <   P _ {1} <   Q _ {2} \end{array} \right. \end{array}\tag{6}
$$

$$
\begin{array}{l} \Pi_ {2} (P _ {1}, P _ {2}) \\ = \left\{ \begin{array}{l l} (Q _ {2} - P _ {2}) (P _ {2} - c _ {2}) & \text { if } 0 \leq P _ {2} <   P _ {1} \\ 0 & \text { if } P _ {2} \geq P _ {1} \end{array} . \right. \end{array}\tag{7}
$$

Fig. 12 shows an example of the profit landscape for seller 1, given $Q _ { 1 } = 1 . 0 , \ Q _ { 2 } = 0 . 9$ . Note the sharp cliff at $P _ { 1 } = P _ { 2 }$ and the two peaks, features that were shown to give rise to price wars in Ref. 5 . <sup>w</sup> <sup>x</sup>

![](/api/attachments/JKHWSMYZ/fulltext/images/36241cf463fa044b4fde66ca699c645fb33f299fb6d7f695f76c5a6dfaa4ecb0.jpg)  
Fig. 11. Profit landscape for seller 2 in two-seller market with quality-sensitive buyers. The sellers’ qualities are $Q _ { 1 } = 1 . 0 , \ Q _ { 2 } =$ 0.9.

![](/api/attachments/JKHWSMYZ/fulltext/images/7d739446065e1224b8c69f9625238ee22f41f2280b33e1dacf39ef80ad3ec987.jpg)  
Fig. 12. Seller market segments. Quality and price boundaries are indicated by solid lines, and labeled on the left and right sides of the figure, respectively. Seller prices are indicated by dashed lines, and are labeled inside the rectangle representing each segment.

To see how this gives rise to a price war, we can introduce the function $P _ { 1 } ^ { * } ( P _ { 2 } )$ , the value of $P _ { 1 }$ that optimizes $\boldsymbol { \varPi } ( P _ { 1 } , P _ { 2 } )$ , for each possible $P _ { 2 } { \mathrm { : } }$ , and the analogous function $P _ { 2 } ^ { * } ( P _ { 1 } )$ . These functions can be expressed analytically as:

$$
\begin{array}{l} P _ {1} ^ {*} (P _ {2}) \\ = \left\{ \begin{array}{l l} Q _ {2} & \text {if} 0 \leq P _ {2} <   Q _ {1} - Q _ {2} + c _ {1} \\ P _ {2} & \text {if} Q _ {1} - Q _ {2} + c _ {1} \leq P _ {2} \leq \frac {1}{2} (Q _ {1} + c _ {1}) \\ \frac {1}{2} (Q _ {1} + c _ {1}) & \text {if} P _ {2} > \frac {1}{2} (Q _ {1} + c _ {1}) \end{array} \right. \end{array}\tag{8}
$$

$$
\begin{array}{l} P _ {2} ^ {*} \left(P _ {1}\right) \\ = \left\{ \begin{array}{l l} c _ {2} & 0 \leq P _ {1} \leq c _ {2} \\ P _ {1} - \epsilon & \text { if } c _ {2} \leq P _ {1} \leq \frac {1}{2} \left(Q _ {2} + c _ {2}\right) \\ \frac {1}{2} \left(Q _ {2} + c _ {2}\right) & \text { if } P _ {1} > \frac {1}{2} \left(Q _ {2} + c _ {2}\right) \end{array} . \right. \end{array}\tag{9}
$$

A simple graphical construction involving these two functions yields the price dynamics, starting from any initial price vector $( P _ { 1 } , P _ { 2 } ) _ { : }$ , as illustrated in Fig. 13.

Now we are in a position to understand the dynamical behavior observed in Sections 3 and 4. In Section 3, the profit landscape only contained one peak, and no cliffs. Any reasonably decent pricing strategy should eventually find its way to the top of this peak, although the rates at which they do vary considerably, from instant, in the case of the myopic sellers, to very slowly for the trial-and-error strategists. In Section 4, the five-dimensional profit landscape is multi-peaked and full of cliffs. The derivative-following algorithm only does a local search. Therefore, once it finds its way to the top of a peak, it can only jitter around on the top of that peak, and has no way to find other peaks. In our case, the derivative followers found their way to the gametheoretic peak. In fact, there is a more optimal peak Ž . in the myopic sense for seller s<sup>s</sup>1, but in order to discover it the seller would have to make a large discontinuous jump. All of the other pricing strategies, including the very naive trial-and-error strategy, permits large jumps. Although the trial-and-error strategy only permits large jumps on rare occasions, eventually a large random jump will take the system from the game-theoretic peak to a location somewhere near a more myopically optimal one, trigger-Ž . ing a price war.

![](/api/attachments/JKHWSMYZ/fulltext/images/39355e902a4c4c87180428761767019231721618a591b1ccbe119b794a81412e.jpg)  
Fig. 13. Profit landscape for seller 1 in two-seller market with price-sensitive buyers. The sellers’ qualities are $Q _ { 1 } = 1 . 0 , \ Q _ { 2 } =$ 0.9.

## 6. Conclusions

In this paper, we investigated the dynamical behavior of a market consisting of simple automated sellers and buyers of a vertically differentiated product or service. We introduced a simple family of buyer utility functions that allowed for tradeoffs between price and quality, and studied two different populations of such buyers. The first population was extremely sensitive to quality, while the second was extremely sensitive to price. For each of these populations, we explored the dynamic collective behavior resulting when the sellers employed five different price-setting strategies ranging widely from perfect knowledge and unlimited computational power to almost zero knowledge and capability.

For the quality-sensitive buyer population, all pricing strategies eventually led to the same price equilibrium. However, for the price-sensitive population, we found that most pricing strategies led to large-amplitude cyclical price wars. It is possible to explain these price war dynamics and their absenceŽ in the case of the derivative-following strategy as . resulting from the underlying topology of the profit landscape, a concept that was introduced in earlier papers 4,7,6 . <sup>w</sup> <sup>x</sup>

Preliminary explorations indicate that multipeaked landscapes and price-war dynamics can occur in cases more general than were reported here. We have observed these phenomena in hybrid populations of buyers with $0 < \gamma _ { b } = 1$ , and in which $\overline { { q } } _ { b }$ and $\overline { { p } } _ { b }$ are not strictly correlated. In these cases, the nature of the price war is slightly different: a seller offering a higher quality can ‘‘undercut’’ a lowerquality seller even by offering its product at a higher price. Price wars consist of general downward trends in the sellers’ prices, with what appear to be roughly constant non-zero gaps between the prices.

Another fruitful avenue for further research is to explore the effect of inhomogeneous pricing strategies. In preliminary work along these lines, we have watched a single myoptimal take advantage of four derivative followers.

Finally, we expect the dynamics to get considerably more interesting when we permit sellers to vary their quality and their price simultaneously in an effort to maximize their profit. Similar work has been done in horizontally differentiated markets 1,3 , <sup>w</sup> <sup>x</sup> but very little has been done in understanding the price and quality equilibria in vertically differentiated markets. Previous work on an information filtering model 4–7 has revealed the existence of very<sup>w</sup> <sup>x</sup> complex price and niche wars, in which the sellers in the economy all attempt to grab the same niche at the same price, leaving a large segment of the buyer population unsatisfied. It will be interesting to see whether sellers in a vertically differentiated market will attempt to fight over some perceived optimal quality level or quality setting, leaving other quality levels abandoned. Work is currently being done in looking at supplier price and quality strategies in a market of M sellers, where each seller could either have the same cost function production function orŽ . they could have different cost functions.

## Appendix A. Computation of the price-sensitive equilibrium

We compute here the game-theoretic equilibrium price vector in the case where the buyers are all purely price sensitive.

Let the S sellers be ordered in the following fashion: $Q _ { 1 } > Q _ { 2 } > Q _ { 3 } > \ldots > Q _ { S }$ , where $Q _ { 1 } \geq$ $q _ { \mathrm { m a x } }$ . We assume that the cost to produce a unit of quality Q is given by $c _ { j } = C ( Q _ { j } )$ , which is a monotonically increasing function of quality. In addition, we assume that there is a monotonic functional relationship $\overline { { p } } _ { b } = f ( \overline { { q } } _ { b }$ .between a buyer $b ^ { \prime } s$ price ceiling $\overline { { p } } _ { b }$ and its quality floor $\overline { { q } } _ { b } \ ( \mathrm { i . e . }$ ., these parameters are perfectly correlated ..

First, note that, if all sellers act selfishly in their best interests, then the components of the equilibrium price vector, if it exists, will be ordered in just the same way as the qualities: $P _ { 1 } ^ { * } > P _ { 2 } ^ { * } > P _ { 3 } ^ { * } \ldots >$ $P _ { S } ^ { * }$ . This can be seen from the following argument. Suppose the prices are not so ordered. Then there exist at least two sellers i and $j$ for whom $Q _ { j } > Q _ { i }$ but $P _ { j } ^ { * } \leq P _ { i } ^ { * }$ , i.e., a higher quality seller is undercutting a lower quality seller in price. If this were to happen, the lower quality seller would sell nothing because any consumer would gladly pay a lower price to obtain a higher quality item. In such a situation, the lower quality seller could increase its profit from zero to some positive value by undercutting its higher-quality competitor.<sup>2</sup> Thus, the supposed equilibrium would not be an equilibrium at all! By contradiction, we can conclude that any equilibrium must satisfy the above price ordering.

![](/api/attachments/JKHWSMYZ/fulltext/images/2a67b841a58f27dab28e9cb2c68804ede78a29a90763783bdbdee2d83e7c772e.jpg)  
Fig. 14. Graphical construction of price war for two myopic sellers, $Q _ { 1 } = 1 . 0 , \ Q _ { 2 } = 0 . 9$

Due to the correlated orderings of seller quality and price, the market undergoes a natural segmentation, such that all buyers within a given segment j will either be served by seller j Žif $j ^ { \prime } s$ price is acceptable , or will opt out of the market entirely. As. shown in Fig. 14, market segment j consists of all buyers b for whom $Q _ { j + 1 } < \overline { { q } } _ { b } < Q _ { j }$ . This can be understood as follows. For a buyer with a quality floor in this range, seller $j$ is the lowest quality seller that meets the quality requirements, and since the sellers’ prices and qualities have the same rank ordering, seller $j$ is also the lowest-priced seller that meets the buyer’s requirements. The boundaries of market segment j can also be expressed on a price scale by using the assumed functional relationship between a buyer’s price ceiling and quality floor. As indicated at the right-hand side of Fig. 14, the lower price boundary of the segment j is defined as $\hat { P _ { j } } \equiv$ $f ( Q _ { j + 1 } ) _ { \cdot }$ , and the upper price boundary is $\hat { P } _ { j - 1 } \equiv$ $f ( Q _ { i } )$

Now we are prepared to compute seller $j ^ { \prime } s$ optimal price $P _ { j } ^ { * }$ . First, note that the optimal price must lie in the range $\hat { P _ { j } } \leq P _ { j } ^ { * } \leq \hat { P _ { j - 1 } }$ . By setting its price at the lower boundary, seller j will capture all buyers within its segment, so there is no benefit to setting the price lower than this. If it sets its price at, or above the upper boundary, it will capture none of the buyers in its segment. Note that if the production cost $c _ { j }$ exceeds the upper price boundary $\hat { P } _ { j - 1 }$ , then seller j cannot make a positive profit under any circumstances, and it will opt out of the market. In what follows, we shall assume that the production costs are not so high as to prevent any of the sellers from entering the market.

In order to compute an exact value for $P _ { j } ^ { * }$ , we make the simplifying assumption that the quality floor and price ceiling parameters of the buyer population are distributed uniformly between ranges $[ q _ { \mathrm { m i n } } ,$ $q _ { \operatorname* { m a x } } ]$ and $[ \boldsymbol { p } _ { \mathrm { m i n } } , \ \boldsymbol { p } _ { \mathrm { m a x } } ] .$ , respectively. Then seller $j ^ { \prime } s$ profit as a function of its price $P _ { j }$ is simply proportional to:

$$
\left(P _ {j} - c _ {j}\right) \left(\hat {P} _ {j - 1} - P _ {j}\right).\tag{10}
$$

This quadratic function of $P _ { j }$ is maximized at the value $( 1 / 2 ) ( \hat { P } _ { j - 1 } + c _ { j } )$ . If this price is between the lower and upper boundaries, then it will be the optimal price for seller $j .$ However, if the maximum of the quadratic fails to occur within these boundaries, then the true maximum within the segment must occur at one of the price boundaries. In fact, the lower boundary $\hat { P _ { j } }$ is the only option, because at the upper boundary the number of buyers served Ž . and therefore the profit is zero.

A little thought shows that these two cases can be expressed as a single equation:

$$
P _ {j} ^ {*} = \max \left[ \hat {P} _ {j}, \left(\hat {P} _ {j - 1} + c _ {j}\right) / 2 \right]\tag{11}
$$

which holds for $j = 1 , 2 , \dots , S ,$ provided that we introduce a fictitious seller $S + 1$ with quality $Q _ { S + 1 } =$ 0.

In Section 4, we set $p _ { \operatorname* { m i n } } = q _ { \operatorname* { m i n } } = 0$ and $p _ { \operatorname* { m a x } } =$ $q _ { \operatorname* { m a x } } = 1$ . In this case, the function f that associates buyers’ price ceilings and quality floors is just the identity, and $\hat { P } _ { j } = Q _ { j + 1 }$ . Thus, we obtain:

$$
P _ {j} ^ {*} = \max \left[ Q _ {j + 1}, \left(Q _ {j} + c _ {j}\right) / 2 \right]\tag{12}
$$

## References

<sup>w</sup> <sup>x</sup>1 Simon P. Anderson, Andre de Palma, J.F. Thisse, Discrete Choice Theory of Product Differentiation, MIT Press, Cambridge, MA.

<sup>w</sup> <sup>x</sup>2 J.J. Gabszewicz, A. Shaked, J. Sutton, J.F. Thisse, Segmenting the market: the monopolist’s optimal product mix, Journal of Economic Theory 39 1986 273–289.Ž .

<sup>w</sup> <sup>x</sup> 3 J.J. Gabszewicz, J.F. Thisse, Price competition, quality, and income disparities, Journal of Economic Theory 20 1979Ž . 340–359.

<sup>w</sup> <sup>x</sup> 4 J. Kephart et al., Dynamics of an information filtering economy, in: Proceedings of CIA ’98, Paris,1998.

<sup>w</sup> <sup>x</sup> 5 J.O. Kephart, J.E. Hanson, Spontaneous specialization in a free-market economy of agents, in: Proceedings of the Artificial Societies and Computational Markets workshop at Agents 98, Minneapolis<sup>r</sup>St. Paul,1998.

<sup>w</sup> <sup>x</sup> 6 J.O. Kephart, J.E. Hanson, J. Sairamesh, Price and niche wars in a free-market economy of software agents, Artificial Life Journal 4 1 1998 1–23.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 J.O. Kephart, J.E. Hanson, J. Sairamesh, Price-war dynamics in a free-market economy of software agents, in: Proceedings of Artificial Life VI, UCLA, MIT Press, 1998.

<sup>w</sup> <sup>x</sup> 8 J.K. Mackie-Mason, H.R. Varian, Pricing the internet, in: Second International Conference on Telecommunication Systems Modelling and Analysis, Nashville, TN, 1994, pp. 378–393, March.

<sup>w</sup> <sup>x</sup> 9 J. Rosenschein, G. Zlotkin, Rules of Encounter, MIT Press, Cambridge, MA, 1994.

<sup>w</sup> <sup>x</sup> 10 J. Sairamesh, D. Ferguson and Y. Yemini, An approach to pricing, optimal allocation and quality of service provisioning in high speed packet networks, Proceedings of the INFO-COM’95.

<sup>w</sup> <sup>x</sup> 11 A. Shaked, J. Sutton, Relaxing price competition through product differentiation, Review of Economic Studies 1982Ž . 3–23.

<sup>w</sup> <sup>x</sup> 12 A. Shaked, J. Sutton, Natural oligopolies, Econometrica 51 Ž . Ž . 5 1983 September.

<sup>w</sup> <sup>x</sup> 13 A. Shaked, J. Sutton, Multiproduct firms and market structure, RAND Journal of Economics 21 1 1990 Spring.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 O. Shy, Industrial Organization: Theory and Applications, MIT Press, Cambridge, MA, 1996.

<sup>w</sup> <sup>x</sup> 15 J. Tirole, The Theory of Industrial Organization, MIT Press, Cambridge, MA, 1995.

<sup>w</sup> <sup>x</sup> 16 H. Varian, Differential pricing and efficiency, First Monday Journal 1998 .Ž .
