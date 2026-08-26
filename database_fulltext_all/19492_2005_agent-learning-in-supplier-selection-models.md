---
otero_id: 19492
otero_key: "QNP6C9C3"
title: "Agent learning in supplier selection models"
authors: "A VALLURI; D CROSON"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00141-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Agent learning in supplier selection models

Annapurna Valluri <sup>a,</sup>\*, David C. Croson<sup>b,1</sup>

<sup>a</sup> Department of Operations and Information Management, The Wharton School of the University of Pennsylvania, Suite 500 Jon M. Huntsman Hall, 3730 Walnut Street, Philadelphia, PA 19104-6340, USA <sup>b</sup> Department of Management Science, Center for eBusiness, Sloan School of Management, MIT, NE60-336 (Three Cambridge Center), Cambridge, MA 02142, USA

Available online 29 November 2003

## Abstract

We use agent-based modeling to study the performance of a supplier selection model, originally proposed by Croson and Jacobides [Small Numbers Outsourcing: Efficient Procurement Mechanisms in a Repeated Agency Model, Working Paper #99- 05-04 Department of Operations and Information Management, The Wharton School of the University of Pennsylvania (1999)], which displays a complicated reward and punishment profile under incomplete information. We document the dynamics and convergence to equilibrium of the interactions of a single buyer with a heterogeneous group of sellers, which results in both separation of sellers capable of producing high-quality goods from those incapable of doing so, and continuing incentives for high-quality-capable sellers to produce at the maximum quality possible. We model two methods of determining exploration reference points—an ‘‘auction-style’’ model focusing on probability of success and a ‘‘newsvendor-style’’ model focusing on profitability. Our simulation shows that (1) the tournament structure suffices to reach convergence at high-quality levels whenever the number of suppliers exceeds three, (2) punishment length and number of suppliers are substitutes, and (3) shorter punishments improve learning speed of convergence. Moreover, we show that it is strictly better for the buyer to transact with relatively few suppliers—a conclusion generated endogenously inside the model as a tradeoff between exploration and exploitation, rather than through assumptions that explicitly penalize supplier proliferation. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Supplier management; Reinforcement learning; Agent learning; Moral hazard; Incomplete contracts

## 1. Introduction

The twin challenges of how to choose capable suppliers and of how to motivate capable suppliers once they have been chosen are central problems in the management of the modern firm. In this paper, we study a game-theoretic supplier selection model originally proposed by Croson and Jacobides [1] where neither the suppliers nor the buyer possesses full information. We use agents to model suppliers who learn to produce at their optimal quality levels through a prespecified system of rewards and punishments administered by the buyer. We also demonstrate how the process of repeated optimality-seeking updates to the actions of the heterogeneous suppliers results in the sellers capable of producing high-quality goods distinguishing themselves from those sellers incapable of doing so (addressing adverse selection), while producing at the highest possible level of quality (addressing moral hazard). Furthermore, using multiple related simulation environments, we can address the question of ‘‘how many suppliers is it optimal to employ?’’ Supporting both previous theoretical literature [6,7,10,28] and corroborating evidence from the Japanese automotive market [1–3], we show that it is optimal for the buyer to transact with relatively few suppliers, a conclusion generated endogenously inside the model rather than forced to happen through assumptions which penalize supplier proliferation per se. We also evaluate the results from the perspective of benefit to society and the costs incurred by the sellers.

In Section 2, we discuss the intersection of the IS and supplier-management literatures. In Section 3, we present our motivation for carrying out an agent-based approach on a solved game-theoretic problem. Section 4 provides an overview of the specific outsourcing model on which we focus. In Section 5, we describe the precise agent-based technique we employ. Our experiments and results are summarized in Section 6. Section 7 concludes and provides suggestions for future work.

## 2. Literature review

Over the past 15 years, IS researchers have been trying to predict the net effect of IT on the attractiveness of outsourcing. Malone et al. [22] reason that by reducing coordination costs proportionally, whether producing in-house or using the market, IT would encourage a greater shift of firms to make use of markets, where coordination costs’ as a percentage of total costs in markets is higher than in firms. Gurbaxani and Whang [20] study the effect of IT from a transaction-cost and agency-theory perspective, but no claim is made about the direction of the shift for either in-house production or use of markets. Although reduction in coordination costs due to IT has paralleled a tremendous increase in outsourcing, they [20] note that the shift has empirically been in the direction of long-term contracting with only a few suppliers, rather than continuous recontracting on the spot market.

Bakos and Brynjolfsson [6,7] both document and explain this seeming paradox by combining coordination costs with the incentives for suppliers to make non-contractible relationship-specific investments. They illustrate the relationship between the number of suppliers and the intensity of noncontractible investments by suppliers, showing that increases in the supplier base reduce the bargaining power of suppliers and thus decreases the incentive of each supplier to make investments in the continuation of the relationship. When these noncontractible relationship-specific investments play a large role in value creation, the buyer has an incentive to limit the proliferation of suppliers even though he must thereby pay higher prices. Their analysis is restricted to observable but unverifiable variables. The authors claim that to provide strong investment incentives for the suppliers, the number of suppliers the buyer should contract with should be small. However, the question of providing incentives comes after the decision of which suppliers to hire: if product quality is unobservable, the buyer’s first concern must be to determine the suppliers capable of (and willing to) produce high-quality products.

Dyer et al. [16] describe the supplier-management practices in the automobile industry in the US, Japan and Korea. Traditionally, the practice in the US has been that of an arm’s length relationship, where a company contracts with several suppliers, thus minimizing dependence on any particular supplier and maximizing buyer bargaining power. In Japan, however, the practice has been of maintaining close relationships with suppliers in ‘‘partner’’-type relationships. In fact, Japanese automakers maintain three tiers of suppliers. Tier I consists of direct suppliers providing strategic components, in whom the buyer generally holds large equity stakes. The suppliers comprising Tier II provide customized components, where the buyer has a small equity stake, and those suppliers that provide competition for the first-tier suppliers. Finally, Tier III consists of suppliers who make more standardized parts such as tires, spark plugs, etc. where presumably cost and continuous predictable supply play a more important role than the provision of noncontractible quality. Recent years have seen a convergence of supplier-management practices in the US, Japan, and Korea to a mixture of partnerships and arm’s length relationships. The authors conclude that to achieve advantages of the two kinds of relationships, the suppliers should be segmented into different groups based on the inputs they provide, whether strategic or standard. The different groups can then be managed optimally without the constraint that they be managed similarly. The enormous costs associated with sinking investments into inefficient suppliers, however, first requires an initial selection of suppliers based on their capabilities before any reciprocal relationship-specific investments can be made.

Croson and Jacobides [12] present a game-theoretic model under unobservable quality (described further in Section 4) that addresses two essential issues: (i) of selecting the suppliers capable of producing high-quality products (adverse selection), and (ii) of providing the right incentives to these suppliers to sustain the production of high-quality products (moral hazard). Extensions of this model predict cross-shareholdings, short recontracting periods, and the comparative-static effects of higher buyer margins, sellers costs, and seller patience on the optimal number of suppliers. This model is discussed in more detail in Section 4.

## 3. Motivation

Supply-chain management has not only caught the attention of researchers in the operations and management science area but recently, it has attracted researchers from the areas of machine learning and agent-based technology. Preliminary yet positive results were found, for example, by Eric Bonabeau of BiosGroup and IcoSystem, who used Swarm intelligence, an artificial intelligence (AI) methodology, to study supply-chain networks (see also Ref. [31]). The agent-based approach has gained enough popularity to become an active sub-area of the computational economics community, which uses agentbased modeling as both a descriptive and normative approach to optimizing complex, non-differentiable situations. Agent-based modeling’s descriptive value stems from understanding why certain global behaviors might evolve and persist through repeated local interactions of autonomous agents; in other words, to study global patterns from the aggregation of many independent bottom-up processes [32], a methodology similar to the well-established approach of studying the microfoundations of macroeconomic behavior by examining aggregation of individual choices [33]. We believe that agent-based modeling approach is capable of providing useful insights as a substitute for or complement to formal theory in the IS area as well.

Purely game-theoretic models are certainly not free from drawbacks; critiques of game theory in political science [26], economics [4], computer science [29], and the popular press [25] focus on simple boundedrationality arguments, claiming in effect that, in the real world, ‘‘people don’t think that way.’’ Aumann [4] argues that most economic agents are not maximizers, in the sense that they do not fully scan the choice set and consciously pick the maximal element from it. In place of such optimization, individuals learn rules of thumb, which get reinforced if fruitful and discarded if irrelevant. Strict maximizations are often difficult, especially in the midst of uncertainty, even to operations-research experts. According to Simon [29], given human beings’ computational limits, the only feasible solution is to find a satisficing solution: a decision-making technique that sets an aspiration level, searches until an alternative is found that is satisfactory by the aspiration level criterion, and selects that alternative.

Many of these criticisms of hyper-rationality can be overcome by agent-based modeling, where the specific form of bounded rationality can be built explicitly into agent design rather than either imprecisely modeled or assumed away entirely. Ref. [5] proposes the use of agents as an emerging methodology in its own right. Agents can be used to complement formal theory, or refute its generality through the finding of a counterexample [21]. Computation techniques can also provide information about patterns which analytical theory would have great difficulty discerning or expressing. It may be relatively easier and cheaper to use computationally intensive methods to help the analytical theorist in initial explorations to determine relationships between the various features in the model, and discern the important quantitative features, in preparation for describing the final elegant theoretical model. The ability of agent-based models to study dynamics, and the dynamic history with which equilibria are reached (if one or more exist), also makes them extremely attractive in practice, whereas dynamical analysis of mathematical models is difficult to achieve except in highly stylized fashion fraught with restrictive assumptions [5]. These assumptions can, however, be relaxed in agent-based models;

dependence on parameter ranges can also be identified and corrected without much difficulty.

## 4. The underlying model of supplier selection

We follow the game-theoretic small numbers outsourcing (SNO) model of repeated contracting with a revolving base of suppliers introduced in Ref. [12]. In this model, a single firm faces a supplier pool composed of N suppliers who are capable of producing high-quality products and a large number who are capable only of low-quality production. The value to the buyer of the sourced good is increasing and convex in quality $q \in [ 0 , 1 ]$ and costs to the high-quality suppliers are also increasing and convex but proportionally lower than the value to the buyer. In a key informational assumption, Croson and Jacobides model a situation in which buyers’ information about quality is sharply limited: they cannot observe quality directly, nor can they make a cardinal evaluation of how high a given seller’s quality is. They can, however, ordinally rank suppliers’ output in decreasing order of quality provided. The initially uninformed buyer, facing both problems of (a) how to select suppliers based on their quality type and (b) having selected suppliers, how to motivate them to deliver consistently highquality products, uses a tournament system to reward the provision of high-quality of a seller relative to his rivals. Suppliers who defined (or tied with) the highest quality of Grade I goods produced in round t get a larger share of the market in round t + 1, wherein they receive a price that exceeds their costs. The ‘‘losers’’—those suppliers in Grade I who fail to meet the quality standards in period t—are punished for x rounds $( 1 < \omega < N )$ by assigning them to a lessprestigious contracting task in Grade II, in which they are paid only their costs. The buyer then completes the incentive system by paying a price to Grade I suppliers, substantially in excess of their costs, to reward them and therefore encourage them to stay in Grade I, which they can do only by matching or overcutting their rivals in quality. Croson and Jacobides proceed to show that the unique Nash equilibrium for supplier-quality choices is for all high-quality suppliers to produce at quality level, $q = 1$ , and for all low-quality suppliers to produce at quality level, $q = 0 ,$ and that the buyer will offer a price to high-quality suppliers just sufficient that high-quality suppliers neither collude at quality levels $\hat { q } < 1$ nor defect and suffer x periods of punishment for their attempts to economize on costs in period t.

Croson and Jacobides note that the SNO model is designed to fit with the supplier selection and management processes, and not simply the outcomes, of the so-called Japanese model of supplier contracting [1 –3]. These studies approach the extensively studied automotive industry and the less-examined electronics sector. In particular, (Ref. [2]: 1026 – 1031) suggests that different types of suppliers inhabit clearly distinct suppliership grades. As Asanuma reports,

. . .[T]he buyer does not apply exactly the same policy to all the suppliers . . . Based on the ratings that the purchasing division exercises as to the abilities of the individual supplier and the degree of importance of the item supplied, each of the incumbent suppliers is given some rank. Thus suppliers are classified (as). . .excellent subcontractors. . .and common subcontractors. . .Based on this ranking system, the buyer applies his effort to develop relationships selectively. (Ref. [2]: 1027).

Note that the two criteria for grade classification are the ability of the subcontractor to provide the desired quality (which we have decomposed into their technological capability and their willingness to deliver), and the importance of the noncontractible effort—the latter depending on the nature of the item supplied. Asanuma continues by observing that

[e]xcellent suppliers are supposed to be suitable candidates with which the core plant should seek to build close and long-standing relationships, subject to repeated reappraisal (Ref. [2]: 1027, emphasis added).

He then (see also Ref. [1]) observes that

Among large manufacturers there exists one common tendency in their purchasing attitude. That is, they prefer to keep and develop many sources of supply for the items they have decided to procure from outside. . . [t]he motive for this is to keep competitive stimuli. (Ref. [2]: 1038, emphasis added).

In the Croson and Jacobides [12] model, given that the buyer does not have well-defined criteria for what ‘‘quality’’ actually is, and resets his expectations dynamically based on seller performance, it may be overly optimistic to expect sellers to determine their optimal strategy or intuit the equilibrium of the entire system-particularly as they try to determine through their actions how much quality must be produced to stay in Grade I, attempt to form collusive groups to stay in Grade I and collect the bonus despite producing q < 1, and occasionally serve an x-period sentence for shirking (whether inadvertently or deliberately). Evidence of individuals solving stochastic dynamic programs in parallel, or other complex mathematical tasks in real time, is thin, but such processes are frequently assumed for modeling purposes [18] ‘‘as if’’ such an optimization were occurring in real time. Realistically, the sellers would conduct a trial-and-error search to calculate the optimal quality at which to produce, given the actions of their competitors. Hence, this game provides an ideal test ground for agent learning. The next section describes our agent-based methodology used to bridge this gap.

## 5. Methodology

Several learning models have been studied in the computational economics and artificial intelligence literatures. They can be broadly classified into belief-based models and reinforcement-based models. In belief-based models, players keep track of the history of play of the other players and form beliefs about these opponents’ likely future play. The players actions are then chosen to maximize the expected payoffs given these beliefs. In reinforcement-based models, players consider only the payoffs that the strategies yielded in the past, omitting the beliefformation process. Reinforcement-based and beliefbased models outperform one another under different conditions [17], but in almost all cases, they converge faster than the Nash equilibrium strategies. Camerer and Ho [9] develop a general model of ‘‘experiencedweighted attraction learning’’, which includes beliefbased and reinforcement-based models as special cases, and show that their unconstrained model works better than its two components by fitting model parameters using maximum likelihood estimation. (Note that it is wholly unsurprising from an optimization perspective that the unconstrained maximumlikelihood model outperforms its two constrained subproblems.) In the SNO model, sellers do not have explicit information regarding the actions chosen by the other sellers in any period of play; they cannot observe their rivals’ quality any better than the buyer can. In other words, although a supplier has access to the identity of the better-performing competitors, he does not know the extent of the cardinal difference between his product’s quality and those of the better performing suppliers, but only his own ordinal rank. Therefore, the only concrete information available to suppliers is the success or failure of their own actions. As a result, the key information required to support a belief-based model is not available to the agent, making a different model more suitable in our case.

Our methodology in this paper is one borrowed from the field of artificial intelligence, known as reinforcement learning (RL) [30]. Our reasons for choosing this method over others in machine learning are its property of not needing a model of the environment and its capability for on-line learning. RL is a technique of learning how to map situations to actions, while maximizing a numerical reward signal. Two features of RL are trial-and-error search and delayed rewards. The learning agent is not told which actions to take in any given situation/state, but must discover (through exploration) which of them will generate the maximum payoff in the long run. Since chosen actions can affect not only the immediate reward but also subsequent rewards, RL faces a challenge of the tradeoff between exploration and exploitation [13,23]. In other words, the agent must exploit what it already knows, yet explore to refine its understanding of the rewarding actions available. Moreover, as stated in (Ref. [8]: 171), ‘‘reinforcement learning processes seem more appropriate to contexts involving large populations where the complexity of modeling and tracking the behavior of all the other participants is too great to justify devoting significant cognitive resources to such activities.’’ This situation neatly summarizes the complex strategic decisions faced by each seller in the SNO situation described above.

<table><tr><td>0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/QNP6C9C3/fulltext/images/371ba0775c4e29146cdd3cf7fa32a751a77c0d9eb90f9b148f8c521917dc054e.jpg)

One of the most widely pursued RL algorithms is Q-learning [35]. Q-learning rewards actions that turn out to be positive and penalizes those that yield negative results. The value to the seller, at time $t ,$ of producing at a quality level $a _ { i }$ is represented by $Q _ { t } ( a _ { i } )$ . When a seller produces at a quality-level $a _ { i } ,$ the value associated with producing at this quality level is updated by the following equation at time t + 1:

$$
Q _ {t + 1} (a _ {i}) = Q _ {t} (a _ {i}) + \alpha [ P _ {t + 1} (a _ {i}) - Q _ {t} (a _ {i}) ]\tag{1}
$$

Eq. (1) is the single-state Q-learning equation where the discount factor between periods is assumed for simplicity to be 1 (Croson and Jacobides [12] derive a lower bound on this discount factor for their equilibrium to hold at $q = 1 ;$ the folk theorem of repeated games with discounting [19] guarantees that the small-numbers outsourcing game will have an equilibrium at $q = 1$ under our assumed conditions). The learning rate, a´, captures the recency effect that weights recent rewards more heavily than past ones—a crucial feature in a dynamic environment. $P _ { t + 1 } ( a _ { i } )$ is the profit earned by the seller who chooses quality $a _ { i } .$ The state space for this Markov decision process consists of the different quality levels at which a supplier can produce. Consequently, if the different quality levels that sellers can produce at range from 0 to 1 in increments of 0.1, then a seller capable of producing up to quality level 0.8 will have exactly nine states (quality levels) at which he can produce, namely {0, 0.1, 0.2, . . ., 0.8}.

For our agent-based implementation of the SNO model, sellers alone (regardless of their quality capabilities) are endowed with this learning capability. We use a slightly modified version of this Q-learning algorithm, proposed in Ref. [24], to obtain faster convergence. Note that we ran our experiments with both the traditional Q-learning algorithm as well as the modified Q-learning algorithm, and confirmed that the only difference between the two algorithms for our example is the difference in convergence rates to the optimal strategies. With the original algorithm, if a seller-agent meets the criterion for producing Grade I goods, we supplement only the specific quality level $a _ { i }$ chosen; under the modified version, we reward all quality levels above the chosen level as well (as in Fig. 1a, where 0.5 is the quality level chosen and all higher levels are also rewarded). Similarly, we penalize the chosen quality level and all lower ones if the threshold for reward is not met, rather than penalizing only the quality level chosen. This is illustrated in Fig. 1b below, where 0.5 is the quality level chosen and all lower levels are also penalized.

The rationale behind extending the reward or penalty to more extreme action states is that if the seller succeeds in meeting the threshold with his chosen quality level, he would have also done so with any higher level (with a gain of share in the next period as a bonus). Also, if he fails to meet the threshold, he would also have failed with any lower level. The reinforcement whether positive or negative, on the additional levels not chosen varies, taking into account the difference in costs (and therefore the potential profits) of producing at the different levels. The negative reinforcement associated with the punishment stage is implicit in the SNO model because Croson and Jacobides concentrate on the chosen quality levels for Grade I goods; they assume sellers producing Grade II goods get zero profits even when they produce $q = 1$ , in contrast to their positive profits in Grade I. The foregone efficiency wages that are not earned by a seller eliminated from Grade I are the ‘‘punishment’’—an opportunity cost, rather than an explicit one. Furthermore, in accordance with the assumptions of unobservable quality, we allow the seller-agent to produce at a quality level of 0, exploiting his temporary sinecure with certainty if it is the only Grade I seller in a particular period, as there are no rivals to overcut.

Fig. 1. (a – b) Reinforcement learning under the modified learning algorithm.

The exploration of sellers is guided by a popular probabilistic function called Softmax. By applying this function, actions that have high values (rewards) associated with them have a greater probability of selection at any given time. The probability of choosing a particular action $a _ { i , { p _ { t } } } ( a _ { i } )$ , at time $t ,$ is:

$$
P _ {t} (a _ {i}) = \frac {\mathrm{e} ^ {\frac {Q _ {t} (a)}{\tau}}}{\sum_ {i = 0} ^ {n} \mathrm{e} ^ {\frac {Q _ {t} (a)}{\tau}}}\tag{2}
$$

where $\tau { > } 0$ is a positive parameter usually called ‘‘temperature’’ and n is the total number of possible actions When the temperature value is high, all actions have equal probability of being chosen; with low values of s, the more highly evaluated actions are highly favored; finally, a zero value corresponds to no exploration but full exploitation [23] of gathered knowledge. With the passage of time, the temperature value is gradually decreased, causing the learning algorithm to slow and eventually stop exploration while increasingly exploiting past experiences. Hence, the temperature value, along with the payoff values associated with actions, controls the tradeoff between exploration and exploitation.

In the course of play, a seller-agent’s behavior could converge to a suboptimal level and thus a particular high-quality seller could get punished more often than would be expected for a typical supplier of his quality capacity. Other potential reasons for unexpected punishment are that rivals may have changed their behaviors or the dynamic composition of the supplier pool may have shifted as previously ‘‘incarcerated’’ high-quality sellers, having finished their sentences, return to Grade I.

Fig. 2 depicts the average quality levels chosen by the groups of 10 capable and 5 incapable sellers during the course of 500 periods of play.

As can be observed in Fig. 2, the average quality level in the capable seller group fluctuates between 0.95 (approximately) and 1.0. In other words, some of the sellers in this group have learned to play at quality level 1 (group A), whereas others have learned to play at levels such as 0.9 (group B). Our model setup penalizes group B sellers in the presence of group A sellers who are producing at a level of 1 in the same period: the strict ordinal ranking of sellers’ qualities will result in group B getting punished for a fixed amount of time before they are allowed to produce again. Since group B is going to be punished even if they produce at relatively high levels of quality (as long as it is not higher than that of group A), and costs are increasing in quality, a fully rational B seller could secure more profits by playing at the lowest possible quality in a particular period. One explanation of this suboptimal play by our boundedly rational group B participants is fallacious interpretation of exploration behavior as equilibrium behavior. Note that, owing to the way that punishments are delivered, the various sellers have different learning histories and are thus at different (path-dependent) stages of learning over the course of play. Low initial choices by group A might persuade group B to find quality levels of 0.9 to be more lucrative than quality levels of 1. After the initial period, the two groups’ exploration periods may not perfectly coincide; group B sellers could be concluding their exploration stage when group A sellers are starting a new exploration phase. As a result, group B sellers will, in effect, mistake the exploration behavior of group A sellers for group A’s optimal choices in the exploitation periods. Moreover, group B, due to its termination of exploration from initial success, will have learned to play suboptimally and not have a chance to rectify its mistake.

![](/api/attachments/QNP6C9C3/fulltext/images/31bf31bac0fbc0808cb9a4a5e13208a7df2c9761f8e8e83d71b1877037184a43.jpg)  
Fig. 2. Quality using the modified Q-learning algorithm (averaged over 5000 runs).

Optimal play could be determined in a multi-agent system with exploration for hundreds of thousands of periods—but this luxury of extended exploration is obviously unacceptable for a real-world buyer–seller system. Moreover, simultaneous learning by multiple agents is difficult and optimal play may not be quickly learned. In Ref. [27], two learning agents playing the iterated prisoners’ dilemma game were unable to learn to cooperate in spite of an extremely long exploration period. On the other hand, the idea of a satisficing solution in non-stationary environments seems more promising [29]—an idea that requires periodic reevaluation of previously obtained solutions to seek improvements, suggesting an exploitation process interspersed with exploration (as in Ref. [23]). For example, Japanese subcontracting practices (Ref. 16]: 70) show that buyers reopen competition for their business to all sellers (even those previously rejected) after a certain interval of time ‘‘to ensure that their long-term suppliers still have the lowest costs and best capabilities.’’

We, therefore, choose to model wherein the sellers employ a two-step process, with the first step being the exploration stage and the second being the review stage. We assume that after the end of the initial exploration stage, a seller enters the review stage. The seller then reviews his optimal quality choice at the end of every review stage using a threshold policy: if the optimal quality choice produces profit in excess of a given threshold value during the review stage, the review process is restarted (note, there is no exploration during this stage); otherwise, the previously optimal quality choice is discarded and the seller starts the exploration process ab initio, using the same parameters as during the initial exploration. One might argue that aspiration-based reinforcement learning [8] has an element of review of learned choice against an aspiration level, similar to our notion of review of learned choice against a threshold value. Models of aspiration-based reinforcement learning require agents to adapt by comparing payoffs achieved from actions chosen in the past with an aspiration level. The range of initial aspiration levels, however, is extremely important for the sustenance of cooperation in cooperative games, and results may be very sensitive to the specific choice of the aspiration level. Moreover, by choosing aspiration levels that promote cooperation or a particular action, we as modelers risk implicitly incorporating our knowledge of the model into the learning process of the agents, thereby steering the claimed results in the direction of our choice. Our method, on the other hand, does not require the input of such parameters and determines optimality of the learned quality level based only on common knowledge of the distribution of the quality-producing capabilities of the various sellers.

We use two methods to determine these threshold values: an ‘‘auction-style’’ method and a ‘‘newsvendor-style’’ method. Each method assumes that a seller believes that each of his N  1 competitors will choose a quality level drawn from a uniform distribution $( U [ 0 , \bar { q } _ { i } ] )$ , where ${ \bar { q } } _ { i }$ is competitor i’s maximum quality level. Note that these conjectured reference levels are not the levels actually chosen by the seller, but rather hypothetically achievable levels to which the seller compares his actual results, and decides thereby whether to continue with his current strategy or to begin exploration anew.

## 5.1. The auction-style method

The first method we analyze is an ‘‘auction-style’’ approach, in which the seller calculates his quality ‘‘bid’’ to maximize expected surplus by increasing the proportion of times that he ‘‘wins’’ (is retained in Grade I) given that he produces quality levels $q _ { \mathrm { r } } < 1$

Suppose the length of the review period is E. E is the sum of the number of periods in which a seller is punished (where he produces Grade II goods with zero profit) and the number of periods in which he is rewarded (during which he produces Grade I goods profitably). Let x denote the length of punishment period for shirking sellers and $q _ { \mathrm { r } }$ be the quality level at which our reviewing seller currently produces. The seller knows his own maximum possible quality $\bar { q }$ and the distribution of other sellers’; thus, he can compute the number of sellers who have capabilities equal to or higher than $q ,$ and thus, the probability with which he himself will meet the threshold for retention in Grade I (i.e., the probability that no other seller will produce at a quality level strictly greater than $q _ { \mathrm { r } } )$

Let k denote the number of suppliers whose maximum quality is strictly less than $q _ { \mathrm { r } }$ . The probability that $q _ { \mathrm { r } }$ exceeds the quality choice of any given one of the $N - \lambda - 1$ rivals with maximum achievable quality ${ \bar { q } } _ { i }$ is equal to the cumulative distribution function (cdf) of $\tilde { q } _ { i } \mathrm { : }$

$$
P r [ U [ 0, \bar {q} _ {i} ] <   q _ {\mathrm{r}} ] = \frac {q _ {\mathrm{r}}}{q _ {i}}\tag{3}
$$

given that any rival whose maximum achievable quality is less than $q _ { \mathrm { r } }$ can be ignored.

The probability that $q _ { \mathrm { r } }$ exceeds all of these rivals quality choices is thus:

Prob ðThreshold is met; given $q _ { \mathrm { r } }$ is chosenÞ

$$
= \frac {\bar {q}}{q _ {\mathrm{r}}} \prod_ {i = \lambda + 1} ^ {N} \left(\frac {q _ {\mathrm{r}}}{\bar {q} _ {i}}\right)\tag{4}
$$

The length of the reward period for choosing policy $q _ { \mathrm { r } }$ is simply the expected number of consecutive successes until the first failure, a geometric random variable $\tilde { R }$ with expectation<sup>2</sup>

$$
E [ \tilde {R} ] = \frac {1}{1 - \frac {\bar {q}}{q _ {\mathrm{r}}} \prod_ {i = \lambda + 1} ^ {N} \left(\frac {q _ {\mathrm{r}}}{\bar {q} _ {i}}\right)}\tag{5}
$$

Note that ‘‘success’’ in this context means $^ { 6 6 } \mathrm { r e } -$ tention in Grade I’’ and ‘‘failure’’ means ‘‘banishment to Grade $\operatorname { I I } , \stackrel { \triangledown } { }$ in contrast with the traditional probabilistic definitions of ‘‘failure’’ (continuation of the streak) and ‘‘success’’ (termination of the streak). The expected number of punishment periods (which occur in blocks of x after each streak terminates) per streak of successes is simply x. Thus, since the geometric distribution is memoryless, the number of expected reward–punishment cycles in a review period of length E is $E / ( E [ \tilde { R } ] + \omega )$ , the expected number of rewards is $( E [ \tilde { R } ] E ) / ( E [ \tilde { R } ] + \omega )$ , and the expected number of punishment periods is (xE)/ $( E [ \tilde { R } ] + \omega )$ . The seller can use these proportions as reference levels: in particular, he can compare their actual number of reward and punishment periods to the numbers predicted by the auction-style model and begin exploration if the predicted results exceed the actual results.

## 5.2. The newsvendor-style method

The second, and more complex, method is derived from the well-known and extensively studied critical –fractile method (the ‘‘newsvendor’’ method of Ref. [34]) used to determine optimal inventory levels. We adopt the method’s reasoning to calculate the expected profit a seller can make using the best quality level established so far. In newsvendor decision problems, sellers tradeoff costs of ‘‘overage,’’ $c _ { \mathrm { o } }$ (excess stock) and ‘‘underage,’’ $c _ { \mathrm { u } }$ (opportunity losses from missed sales), to determine the optimal decision, which is to choose the decision variable $q _ { \mathrm { r } } ^ { * }$ such that

$$
F \left[ q _ {\mathrm{r}} ^ {*} \right] = \frac {c _ {\mathrm{u}}}{c _ {\mathrm{u}} + c _ {\mathrm{o}}}, \text { where } q _ {\mathrm{r}} ^ {*} = \operatorname{argmax} E [ \tilde {\pi} (q _ {\mathrm{r}}) ]\tag{6}
$$

According to the critical –fractile ‘‘newsvendor’’ logic described above, the value of $q _ { \mathrm { r } }$ which maximizes expected profit, $\tilde { \pi } ,$ is implicitly characterized by

$$
F \left[ q _ {\mathrm{r}} ^ {*} \right] = \frac {\omega (p - c \left(q _ {\mathrm{r}}\right))}{c ^ {\prime} \left(q _ {\mathrm{r}}\right) + \omega (p - c \left(q _ {\mathrm{r}}\right))}\tag{7}
$$

where, in accordance with the newsvendor intuition, we can think of $c ^ { \prime } ( q _ { \mathrm { r } } )$ as the cost of overage— producing slightly more quality than required to win, with a wasted cost of $c ^ { \prime } ( q _ { \mathrm { r } } )$ —and $\omega ( p - c ( q _ { \mathrm { r } } ) )$ as the cost of underage (where $p$ is price and c the marginal cost of producing a unit at quality $q _ { \mathrm { r } } ) -$ producing slightly less than required to win, and losing the opportunity for x periods of profitable sales. When the realization of the random variable underlying $F [ \bullet ]$ is higher than $q _ { \mathrm { r } } ,$ the seller incurs opportunity losses (as another competitor has overcut his quality, triggering x periods of punishment), whereas when its realization is lower, more quality than necessary to win has been produced.

Continuing the newsvendor intuition, $F [ \bullet ]$ is the cdf of the order statistic representing the quality choice of the highest-quality competitor, corresponding to the ‘‘random demand’’ usually invoked in newsvendor models. Calculating the exact distribution of $F [ \bullet ]$ requires several steps. The probability density function (pdf) of the nth order statistic $f _ { n } ( x )$ of n independent random variables $X _ { 1 } , \dots X _ { N }$ (not necessarily identically distributed) with pdf $P _ { i } ( x )$ and cdf $p _ { i } ( x )$ is (Ref. [14]: 20 – 21)

$$
f _ {n} (x) = \left[ \prod_ {i = 1} ^ {n} P _ {i} (x) \right] \sum_ {i = 1} ^ {n} \left(\frac {p _ {i} (x)}{P _ {i} (x)}\right)\tag{8}
$$

Under the assumptions that the $k { = } N { - } \lambda { - } 1$ rivals’ quality capabilities follow the distribution stated above, the rivals’ quality choices can be represented as $X _ { 1 } , \dots X _ { k }$ independent random variates, respectively distributed with pdf $f _ { i } ( x ) = 1 / { \bar { q } } _ { i }$ and cdf $F _ { i } ( x ) =$ $P r [ \tilde { q } _ { i } < x ] = x / \bar { q } _ { i }$ . Thus, the pdf of the kth order statistic (i.e., for the highest quality chosen by the sellers’ k rivals) is

$$
\begin{array}{l} f _ {k} (x) = \left[ \prod_ {i = 1} ^ {k} P _ {i} (x) \right] \sum_ {i = 1} ^ {k} \left(\frac {p _ {i} (x)}{P _ {i} (x)}\right) = \left[ \prod_ {i = 1} ^ {k} \frac {x}{\bar {q} _ {i}} \right] \sum_ {i = 1} ^ {k} \binom {\frac {1}{\bar {q} _ {i}}} {\frac {x}{\bar {q} _ {i}}} \\ = \left[ x ^ {k} \prod_ {i = 1} ^ {k} \frac {1}{\bar {q} _ {i}} \right] \frac {k}{x} = k x ^ {k - 1} \prod_ {i = 1} ^ {k} \frac {1}{\bar {q} _ {i}} \end{array} \tag {9}
$$

evaluated at $x { = } q _ { \mathrm { r } } { . } ^ { 3 }$ Given our assumption that all k rivals are capable of producing higher levels of quality than $q _ { \mathrm { r } } , \bar { q } _ { 1 } , . . . . , \bar { q } _ { k } \geq q _ { \mathrm { r } } ,$ follows. The cdf of this kth order statistic is, by definition,

$$
\begin{array}{l} F _ {k} (x) = P r [ x _ {k} <   x ] = \int_ {0} ^ {x} \left(k y ^ {k - 1} \prod_ {i = 1} ^ {k} \frac {1}{\bar {q} _ {i}}\right) \mathrm{d} y \\ = x ^ {k} \prod_ {i = 1} ^ {k} \frac {1}{\bar {q} _ {i}} \end{array}\tag{10}
$$

Thus, the seller following the newsvendor policy should choose the level $q _ { \mathrm { r } } ^ { * }$ such that

$$
F [ q _ {\mathrm{r}} ^ {*} ] = (q _ {\mathrm{r}} ^ {*}) ^ {k} \prod_ {i = 1} ^ {k} \frac {1}{\bar {q} _ {i}} = \frac {\omega (p - c (q _ {\mathrm{r}}))}{c ^ {\prime} (q _ {\mathrm{r}}) + \omega (p - c (q _ {\mathrm{r}}))}\tag{11}
$$

and thus

$$
q _ {\mathrm{r}} ^ {*} = \left[ \frac {\omega (p - c (q _ {\mathrm{r}})) \prod_ {i = 1} ^ {k} \bar {q} _ {i}}{c ^ {\prime} (q _ {\mathrm{r}} + \omega (p - c (q _ {\mathrm{r}})))} \right] ^ {\frac {1}{k}}\tag{12}
$$

The seller can use the profits yielded by the choice of $q _ { \mathrm { r } } ^ { * }$ as a reference level: in particular, he can compare his actual profit to that predicted by the newsvendor-style model and begin exploration if the predicted results exceed the actual results.

## 6. Simulation and results

All simulations are run with two groups of sellers: the high-quality-capable (hence, capable) group and the low-quality-only (hence, incapable) group. We assume 11 discrete levels of quality ranging from 0 to 1 (in increments of 0.1) and use a common constant learning rate of 0.25. Our temperature value (exploration) decreases at a constant rate over a certain number of periods, which is a function of the maximum quality level at which a seller can produce. We vary this exploration period for a seller depending on the number of possible quality levels at which he can produce, allowing two periods of exploration for each level. In our simulation runs, the capable sellers can produce up to quality level 1 and the incapable sellers can produce only up to a quality level of

0.4, making their exploration periods approximately, 22 periods and 10 periods long, respectively.

The calculation of the appropriate initial temperature value is a less straightforward, requiring trial and error [27]. The initial s value for the capable type of seller was determined by the profit he would make if he were to produce at the highest possible quality level and were the sole producer, alone in the market. For the incapable type of seller: we calculated the profit to the seller if he were to produce at the minimum possible quality level, and where the number of goods produced were divided by the total number of sellers.

To allow comparison of results across simulations, we normalize the cost function values to fall between 0 and 1. The value to the buyer is set at 3.5 times the cost to the seller,<sup>4</sup> and the per-unit price is set to 2. This price is well in excess of the required price to induce the highest possible quality from capable suppliers, provided that at least two high-quality suppliers are currently in Grade I. The amount of the good procured through the SNO is set at 360,360 units.<sup>5</sup> Grade I goods are divided equally among all the suppliers producing them at any given time. The evaluation interval (review stage) is 18 periods, with the number of punishment periods set to 5 (to correspond to the example calculated in Ref. [12]), and the threshold method used varies between the auction and the newsvendor method as analyzed above.

We run our multi-agent system for 500 periods, noting the quality levels produced by each seller group in each round of play. All simulation runs are conducted 5000 times (for a total of 2.5 million sample periods per treatment), with a different seed for the random number generator each time, on a dual Ultra-SPARC-III 900-MHz processor computer with 2048 MB RAM. The following analysis shows how the resultant quality levels vary over time, demonstrating both the dynamics of the sellers’ learning process and its economic implications for the buyer. We also analyze the benefits and drawbacks of larger and smaller numbers of SNO participants by varying the number of high-quality (‘‘capable’’) sellers from 2 to 15 so that we are able to provide direct comparisons of the merits and drawbacks of increasing the size of the capable seller pool over a broad range.

In the SNO model we implement, where quality is both noncontractible and difficult to measure, we are interested both in identifying the high-quality capable sellers and providing them with incentives to produce at high-quality levels. Fig. 3 shows a 500-period simulation with 10 capable and 5 incapable sellers using the newsvendor-style method of determining exploration reference points, averaged over 5000 runs. Due to exploration by both types of sellers, there is substantial quality fluctuation in the initial periods. The opportunity for an individual agent to gather greater profits by producing at higher levels than his rivals, combined with the threat of punishment if his rivals outperform, results in a quality war, with the capable agents increasing their levels of quality until they reach q¯ (here, 1.0). The incapable sellers, in turn, learn the impossibility of avoiding punishment due to their quality-capacity constraints and learn to produce at levels close to 0, which minimizes their costs. The simulation thus shows the power of the SNO model to address not only the challenge of segregating the capable sellers from the incapable sellers but also the incentive problem of inducing the capable sellers to produce at their highest possible quality level.

As discussed earlier, the modified Q-learning algorithm without re-exploration or a reference level (hereafter, referred to as the ‘‘no-reference’’ method) results in some of the capable sellers producing at sub-optimal levels. Fig. 4 compares the course of play for both sellers groups, under both the newsvendor method and the no-reference method. Unsurprisingly, the newsvendor method performs better for both groups. From the perspective of the capable sellers, the newsvendor method guarantees that the capable sellers are neither producing below the quality levels of the other capable sellers (and thus losing out on possible revenue) nor are they getting punished while producing at high-qualitylevels (and thus needlessly incurring extra cost instead of producing at the lowest possible quality-level). Given that incapable sellers will get punished regardless of the quality level at which they produce at as long as there is some capable seller producing at a higher level, the newsvendor method shows them to produce at lower quality levels, economizing on costs. Thus, the newsvendor method clearly improves the profitability of both types of sellers over the levels achievable by the no-reference method.

![](/api/attachments/QNP6C9C3/fulltext/images/5e44bf0d2587a843d1a695a0040ec119789df233a4eb4d1b22ad74a4541ed557.jpg)  
Fig. 3. Quality from 5 incapable and 10 capable sellers using the Newsvendor method

Fig. 5 shows the differences in social surplus obtained from the use of the newsvendor reference method and the no-reference method. Societal surplus is larger in the newsvendor reference level as compared to the no-reference method for the entire analyzed range of capable sellers.

Buyer surplus is also greater with the newsvendor method than the no-reference method, as shown in Fig. 6. Given that the buyer’s value is convex in quality, he benefits greatly when the capable sellers converge quickly to q = 1 (even though the buyer does not explicitly value the convergence of the incapable sellers).

Of the two threshold methods that we employ which improve on the no-reference method, the newsvendor method seems to perform better than the auction-style method not only in terms of speed of convergence to optimal play but also in terms of total buyer and social surplus. The newsvendor method, with its emphasis on profitability, outperforms the auction-style method, with its emphasis in winning the quality war, on all relevant dimensions. Fig. 7 shows the average quality levels of the capable seller group under the two threshold methods, clearly showing that the newsvendor method produces faster convergence of both seller groups to the Nash equilibrium levels. Under the auction-style method, the average quality level of the capable seller group fluctuates between two high levels of quality, implying the persistence of a few capable sellers who continue to produce at non-Nash quality levels, within the observed period of 500 rounds.

Figs. 8 and 9 show the magnitude of the benefit of using the newsvendor method over the auction-style method (for three or more capable sellers), from the perspective of the buyer and society.

![](/api/attachments/QNP6C9C3/fulltext/images/19bd38182f03eefd314c15365c86994d29ef377af64713a8c2c509865c857693.jpg)  
Fig. 4. Performance of the newsvendor method vs. the no-reference method for five incapable sellers.

Fig. 10 shows the number of episodes it takes for a given number of capable sellers to be producing at the Nash quality level 99% of the time when in a production (reward) period. When there are only two capable sellers, their behavior does not converge to the Nash qualities even around the 2500th period.

![](/api/attachments/QNP6C9C3/fulltext/images/30a1c3c83cba45b8e4ca48b3b3d60fcdf2ce12019b61d6a72455514fbc5cd197.jpg)  
Fig. 5. Difference in total social surplus between the newsvendor method and the no-reference method (five incapable sellers).

![](/api/attachments/QNP6C9C3/fulltext/images/eeee3427f99e342a7f52e7633f884eea029d7754e7b640ba89836785826d4d1f.jpg)  
Fig. 6. Difference in total buyer surplus between the newsvendor method and the no-reference method (five incapable sellers).

Instead, they tend to tacitly collude at lower levels such as 0.8 or 0.9, which is not very profitable for the buyer. On the other hand, when there are three capable sellers, convergence at $q = 1$ seems to take place around period 850. Although the three-seller case does converge eventually, the four-seller case converges much faster. Hence, the marginal benefits to the buyer of contracting with this fourth supplier are significant. Convergence is fastest with four capable sellers; thereafter, time to convergence increases in a stepwise fashion, limiting the buyer’s gains from further supplier proliferation.

![](/api/attachments/QNP6C9C3/fulltext/images/85fce352b637cdb3e50a99a19014fcdde7f64ed8c55cc6bc90e1dcc32a03ce82.jpg)  
Fig. 7. Quality from 5 incapable and 10 capable sellers using the two threshold methods.

![](/api/attachments/QNP6C9C3/fulltext/images/1323754b25463f250d2ca32f20c9a10715f28b0b4322d73a2d4a6e100d9d950a.jpg)  
Number of Capable Sellers  
Fig. 8. Difference in total buyer surplus between the newsvendor and the auction-style methods.

The initial decrease in the convergence rate is due to the increase in the intensity of the quality war among the different capable sellers. While the addition of an extra seller increases the quality war among the sellers, the probability of any seller getting punished (at least initially) also increases. Since in effect, the overall punishment period gets longer with each additional capable supplier, and no learning occurs during the punishment period, the convergence to the Nash strategy gets delayed as the number of suppliers increases. When the buyer’s primary motivation is to encourage high quality (and thus to get sellers ‘‘trained’’ to produce q = 1 as quickly as possible), and the opportunity costs of continued supplier experimentation are large, a network of four suppliers would seem to be broadly optimal.

Even though convergence is fastest when there are only four capable sellers, the buyer’s actual surplus as a percentage of his ideal surplus is maximized under our sample parameters when there are about 10 capable sellers (Fig. 11). Moreover, the buyer’s marginal percentage surplus, as shown in Fig. 12, is a convex graph which drops very sharply to 0. When there are more than five capable sellers, the marginal surplus of adding an additional seller is less than 1%. Even if the marginal surplus is calculated on an absolute basis as the increase in total buyer surplus from n + 1 sellers over the total buyer surplus for n capable sellers, the marginal surplus drops below 1% when there are nine or more capable sellers.

![](/api/attachments/QNP6C9C3/fulltext/images/6de683629233825b67b9cb7ee4a8fbd5e285d9bc492ba5069095878b8111c80b.jpg)  
Fig. 9. Difference in total social surplus between the newsvendor and auction-style methods.

![](/api/attachments/QNP6C9C3/fulltext/images/fbe7c0ab6a41d8aa00c9fd2a7a3fc4c45d2a8453aa32b726143e6eacfdec7087.jpg)  
Fig. 10. Convergence of capable sellers to the maximum quality-level under the newsvendor threshold method by varying the number of capable sellers.

Fig. 13 graphs the actual social surplus as a percentage of ideal social surplus against the number of capable sellers. Although actual social surplus keeps increasing, when analyzed as a percentage of ideal surplus, it reaches a maximum at nine capable sellers. For completeness, we also show Fig. 13’s complement, representing deadweight loss as a percentage of ideal surplus (Fig. 14).

Fig. 15 shows the buyer’s surplus in relation to the degree of convexity of the sellers’ cost function: quadratic vs. cubic vs. quadric. Increasingly convex cost functions both (a) discourage extremely high choices of quality and (b) result in concave seller profit functions which discourage random exploration. Buyer losses from increased cost convexity occur for two reasons. First, higher seller costs also imply that the buyer must offer higher prices to suppliers, which reimburse sellers’ costs for q = 1 plus an efficiencywage component. Second, higher marginal costs of increasing quality to high levels discourage suppliers from raising their quality levels all the way to q = 1 until they have explored (and been punished at) many lower levels. In all of these formulations, the buyer is unprofitable for very low numbers of capable sellers (regardless of the sellers’ cost function). The buyer receives an increasingly large amount of surplus as the number of capable sellers increases, up to a local maximum in the range of 10–12 (when analyzed as a percentage of ideal buyer surplus). Social surplus is maximized in the range of 8 –9 capable sellers.

![](/api/attachments/QNP6C9C3/fulltext/images/577904186486ca81a3d86d40e2fc0de088d1205bd64b404273fbc3f28cde08e4.jpg)  
Fig. 11. Buyer’s actual surplus (as % of ideal) vs. number of capable sellers.

![](/api/attachments/QNP6C9C3/fulltext/images/c5822d9728c5c2187410249b2a5156944681102aa2d336cb36a3b5d62b9e8d87.jpg)  
Fig. 12. Buyer’s marginal surplus (as % of ideal) vs. number of capable suppliers.

The net effect on buyer surplus from a change in punishment length has two interesting components. First, longer punishments lead to longer times required for convergence, which we define as the number of periods required before capable sellers are producing at their highest possible quality level 99% of the time that they are producing Grade I goods. Secondly, while the severity of punishment when choosing low-quality-levels increases (giving an incentive to choose higher quality-levels), the length of time before this learning can be put into effect also increases. Since the time spent ‘‘in jail’’ does not contribute to learning per se, this effect makes a capable agent take a greater number of periods to learn to produce at quality level ${ \bar { q } } _ { i } .$ This effect can be seen in Fig. 16 showing a supplier pool of four capable and five incapable sellers. All else equal, slower convergence harms the buyer, who receives lower quality for longer periods of time; thus, the buyer must exercise moderation in punishment to improve profitability. A punishment policy of three periods converges faster than either one- or fiveperiod punishments.

This harmful effect of slower convergence, however, can be at least partially offset by stronger incentives given to capable sellers. Fig. 17 shows the net effect of increasing punishment length on buyer surplus. Buyer surplus associated with four capable sellers is higher with a five-period punishment length than a three-period. However, convergence to Nash equilibrium quality-levels for the same parameter setting is faster with three-period punishment length.

![](/api/attachments/QNP6C9C3/fulltext/images/f08b65d1f05736e10bb22c86a90139434825c15f526f0d826dd56a8d39dc8ece.jpg)  
Fig. 13. Actual social surplus (as % of ideal surplus) vs. number of capable sellers.

![](/api/attachments/QNP6C9C3/fulltext/images/1a247b0a05e0ba9e87c9fa3d23422f2ed539cf6f0843080444179b72d1c6e9a5.jpg)  
Fig. 14. Deadweight loss (as % of ideal surplus) vs. number of capable sellers.

This illustration leads to an interesting set of results: we see that one-period punishments are never optimal, in spite of faster convergence, because the weak threat of punishment hampers the capable sellers’ incentives to produce high quality. In addition, the incapable sellers tend to be rewarded more often than necessary. However, when considering three-and five-period punishments, we notice that the length of punishment and number of suppliers are substitutes: with three sellers, buyer profits are higher with five-period punishments than with threeperiod punishments. At N = 9, however, the faster learning from three-period punishments outweighs the added incentives from stronger five-period (x) punishments. We identify that five-period punishments are best for up to four sellers, and three-period punishments for larger numbers. For all three simulated parameters of punishment lengths, buyer profitability is maximized in the range of 8–9 capable sellers; for our sample cost and price parameters, the global optimum is achieved at eight capable sellers and three-period punishments.

A significant advantage of simulation techniques over traditional mathematical approaches is the rela-

![](/api/attachments/QNP6C9C3/fulltext/images/1105e7434a830595feb2b65a9bf63798592233218a4f20ceba348c6a44f726b6.jpg)  
Fig. 15. Buyer surplus under different levels of cost function convexity.

![](/api/attachments/QNP6C9C3/fulltext/images/8e60ed9072fd81da4a4b64432d547577c5cfb5195f8d2979981f73214856ab37.jpg)  
Fig. 16. Increasing punishment length slows convergence.

tive ease of testing the change in the dependent variables of interest while systematically varying one (or, for that matter, two or more) independent variables. To test the robustness of our results, we conducted sensitivity analysis on various parameters (as shown in Table 1). To address the buyer’s problem of how many suppliers to contract with, we are primarily interested in observing the effect of parameter changes on the optimal number of capable suppliers from the perspective of the buyer and, to a lesser extent, from the buyer –seller system as a whole. The optimal number of suppliers from the latter perspective is defined as the number at which the ratio of actual social surplus to ideal social surplus is maximized. To get a single-valued maximizer for the buyer’s profit function, we defined the optimal number of suppliers from the buyer’s perspective as the lowest number of suppliers at which the marginal benefit of adding an additional supplier is less than 1%. The observed range of optimal suppliers to transact with from the buyer’s profitmaximization perspective reliably falls within 6–8, and from the system perspective it reliably falls within 7–9. Table 1 demonstrates that our results are stable over different parameter values and reinforces the general principle promulgated in Refs. [6,7,10,12,28] that buyers should transact with only a modest number of suppliers.

![](/api/attachments/QNP6C9C3/fulltext/images/2957be285112cb6a1bb41904f2bedb53c794ec515b0c0d88e09ccd8ede577cae.jpg)  
Fig. 17. Buyer surplus as a function of punishment length and number of sellers.

Table 1  
Sensitivity analysis on optimal number of capable sellers

<table><tr><td>Variable changed</td><td>Range of values explored</td><td>Profit-maximizing # of capable suppliers</td><td>Social surplus-maximizing # of capable suppliers</td></tr><tr><td>Number of exploration periods for capable and incapable sellers</td><td>{11, 22, 44}—Capable {5, 10, 20}—Incapable</td><td>6–7</td><td>8–9</td></tr><tr><td>Number of incapable sellers in the pool</td><td>{3, 5, 7}</td><td>6</td><td>8–9</td></tr><tr><td>Price of the good</td><td>{1.5, 2.0, 2.5}</td><td>6–8</td><td>7–9</td></tr><tr><td>Maximum quality level of incapable (low-quality) sellers</td><td>{0.2, 0.4, 0.6}</td><td>6–7</td><td>7–9</td></tr><tr><td>Review periods</td><td>{18, 30}</td><td>6</td><td>8–9</td></tr></table>

## 7. Conclusions and future work

In this paper, we use reinforcement learning to study the SNO model proposed by Croson and Jacobides [12] for supplier selection. We study the dynamics of high-quality and low-quality seller interactions and test whether sellers capable of producing high-quality goods can be distinguished from sellers capable of only producing low-quality goods;

and be forced to produce at high-quality levels. Our results show that capable sellers, when three or more, do distinguish themselves from incapable sellers and produce at high levels of quality, with the rate of convergence being faster for smaller numbers of sellers (and weaker punishments) in our example. Buyer surplus was increasing in the number of sellers up to a point (four to nine capable sellers for our sample parameters); it reached a global optimum at eight suppliers with three-period punishments. These results are interesting and corroborate previous theoretical and empirical literature on outsourcing, as well as being consistent with casually observed evidence in the market (as documented in Ref. [7] that few buyers use more than four to five suppliers for the same item). We thus showed through simulation that it is optimal for the buyer to outsource to only a relatively small number of suppliers, as any more or fewer would result in a decrease in the buyer’s total surplus. From a social perspective, it is similarly optimal for the buyer to outsource to only a few suppliers, as the deadweight loss from wasteful exploration increases exponentially with an increase in the number of highquality suppliers.

In future work, it would be interesting to explicitly incorporate the switching costs incurred by the buyer when she changes suppliers. Japanese automakers, do not experience very high switching costs in practice since the supplier base per se does not change: only the grade (or tier) to which the supplier belongs and the amount of margin left to the supplier changes, not the supplier’s identity. US automakers (particularly in the 1980s) experienced high and frequent switching costs as they rotated suppliers to get lower prices [16]. We expect that an SNO model that incorporates a cost of bringing suppliers back from punishment periods would both deter the buyer from punishing for small transgressions (to avoid this re-entry cost) and make longer punishments credible when punishment occurred (to economize on the frequency with which this re-entry cost would be incurred for a given supplier).

In this model, we have allowed only relative quality evaluation (i.e., Supplier 1’s quality is higher than Supplier 2’s) but supposed that this relative ranking was 100% accurate. We would like to extend this work to evaluate both cases of imperfect relative quality inspection (i.e., Supplier 1’s quality is probably higher than Supplier 2’s) or imperfect absolute quality inspection (i.e., Supplier 1’s quality is probably high enough to meet standards, but Supplier 2’s probably isn’t). A closed-form theoretical model of such imperfect monitoring quickly becomes analytically intractable. Refs. [11,15] show conditions under which frequent or high-density sampling may reduce the agents’ incentives to produce at high quality; consequently, the optimal punishment strategy for the buyer may be quite complex under imperfect observation. Similarly, as real-world buyer – supplier relationships always include some uncertainty, creating an agent learning model to optimize the reward– punishment structure under imperfect information could contribute new insights into the benefits and costs of using small-numbers outsourcing.

Finally, in uncertain environments, it is not very practical for an individual (or a player) to expect to get good results from performing repeated static optimizations since the environment may evolve in a direction depending on the sequence of actions taken by the individual—thus causing the environment to behave in a non-stationary fashion, in which the individual has to perform dynamic optimization without an underlying model of the effects of his actions, a rather difficult task. Such an individual could still probe the environment (and its responses to his actions) by exploring different actions and trying to learn the best (near optimal) combinations of actions to balance exploration and exploitation. One promising approach in these situations is to use machine learning techniques and perform agent-based simulations of such environments to attempt to distill simple decision heuristics which are robust to environmental change.

## References

[1] B. Asanuma, Manufacturer – supplier relationships in Japan and the concept of relationship-specific skill, Journal of the Japanese and International Economies 3 (1989) 1 – 30.

[2] B. Asanuma, Interfirm relationships in the Japanese automobile industry, Rivista Internazionale di Scienze Economiche e Commerciali 40 (12) (1993 Dec.) 1019– 1040.

[3] B. Asanuma, T. Kikutani, Risk absorption in Japanese subcontracting: a microeconometric study of the automobile industry, Journal of the Japanese and International Economies 6 (1) (1992 Mar.) 1 – 29.

[4] R.J. Aumann, Rationality and bounded rationality, Games and Economic Behavior 21 (1997) 2 –14.

[5] R. Axtell, Why agents? On the varied motivations for agent computing in the social sciences, Working Paper CSED No. 17 (2000).

[6] Y.J. Bakos, E. Brynjolfsson, Information technology, incentives and the optimal number of suppliers, Journal of Management Information Systems 10 (2) (1993) 37–53.

[7] Y.J. Bakos, E. Brynjolfsson, From vendors to partners: information technology and incomplete contracts in buyer – supplier relationships, Journal of Organizational Computing 3 (3) (1993) 301– 328.

[8] J. Bendor, D. Mookherjee, D. Ray, Aspiration-based reinforcement learning in repeated interaction games: an overview, International Game Theory Review 3 (2 and 3) (2001) 159 – 174.

[9] C. Camerer, T.-H. Ho, Experience-weighted attraction learning in normal form games, Econometrica 67 (4) (1999 July) 827 – 874.

[10] E.K. Clemons, S.P. Reddi, M.C. Row, The impact of information technology on the organization of economic activity: the ‘move to the middle’ hypothesis, Journal of Management Information Systems 10 (2) (1993) 9 – 35.

[11] T. Cowen, A. Glazer, More monitoring can produce less effort, Journal of Economic Behavior and Organization 30 (1) (1996) 113– 123.

[12] D.C. Croson, M.G. Jacobides, Small numbers outsourcing: efficient procurement mechanisms in a repeated agency model, Working Paper #99-05-04 Department of Operations and Information Management, The Wharton School of the University of Pennsylvania (1999).

[14] P.A. David, Order Statistics, Wiley, New York, 1970.

[13] D. Cyert, J.G. March, A Behavioral Theory of the Firm, Prentice-Hall, Englewood Cliffs, NJ, 1963.

[15] P. Dubey, O. Haimanko, Optimal scrutiny in multiperiod promotion tournaments, Cowles Foundation Discussion Paper #1254 Yale University (2000).

[16] J.H. Dyer, D.S. Cho, W. Chu, Strategic supplier segmentation: the next ‘best practice’ in supply chain management, California Management Review 40 (2) (1998) 57 – 77.

[17] N. Feltovich, Reinforcement-based vs. belief-based learning models in experimental asymmetric-information games, Econometrica 68 (3) (2000) 605 – 641.

[18] M. Friedman, Essays in Positive Economics, University of Chicago Press, Chicago, 1953.

[19] D. Fudenberg, E. Maskin, The folk theorem for repeated games with discounting and incomplete information, Econometrica 54 (1986) 533– 554.

[20] V. Gurbaxani, S. Whang, The impact of information systems on organizations and markets, Communications of the ACM 34 (1) (1991) 59 – 73.

[21] K.L. Judd, Computational economics and economic theory: substitutes or complements, Journal of Economic Dynamics and Control 21 (1997) 907– 942.

[22] T.W. Malone, J. Yates, R.I. Benjamin, Electronic markets and electronic hierarchies: effects of information technology on market structure and corporate strategies, Communications of the ACM 30 (6) (1987) 484 – 497.

[23] J.G. March, Exploration and exploitation in organizational learning, Organization Science 2 (1) (1991) 71 – 87.

[24] E. Oliveira, J.M. Fonseca, N.R. Jennings, Learning to be competitive in the market, Proceedings of the AAAI Workshop on Negotiation: Settling Conflicts and Identifying Opportunities, 1999, pp. 30 – 37.

[25] W. Poundstone, Prisoner’s Dilemma, Doubleday, New York, 1992.

[26] A. Rapaport, Critiques of game theory, Behavioral Science, (1959) 449 – 466.

[27] T.W. Sandholm, R.H. Crites, Multiagent reinforcement learning in iterated prisoner’s dilemma, Biosystems 37 (1995) 144– 166.

[28] A. Seidmann, E. Wang, Electronic data interchange: competitive externalities and strategic implementation policies, Management Science 41 (3) (1995 March) 401– 418.

[29] H. Simon, Theories of bounded rationality, in: H. Simon (Ed.), Models of Bounded Rationality, Behavioral Economics and Business Organization, vol. 2, MIT Press, Cambridge, MA, 1982.

[30] R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, MIT Press, Cambridge, MA, 1998.

[31] J.M. Swaminathan, S.F. Smith, N. Sadeh, Modeling supply chain dynamics: a multiagent approach, Decision Sciences 29 (3) (1998 Summer) 607–632.

[32] L. Tesfatsion, Guest editorial: agent-based modeling of evolutionary economic systems, IEEE Transactions on Evolutionary Computation 5 (5) (2001).

[33] R.M. Townsend, Arrow-debreu programs as microfoundations

of macroeconomics, in: T.F. Bewley (Ed.), Advances in Economic Theory: Fifth World Congress, Econometric Society Monographs Series, vol. 12, Cambridge Univ. Press, Cambridge, 1987, pp. 379–428.

[34] H.M. Wagner, Principles of Operations Research, Prentice-Hall, Englewood Cliffs, 1969.

[35] C.J.C.H. Watkins, Learning from Delayed Rewards, PhD thesis, Cambridge University (1989).

Annapurna Valluri is a PhD student in the Department of Operations and Information Management in the Wharton School of Business, University of Pennsylvania. Her active area of research is in multiagent learning in strategic decision environments with a focus on supply-chain networks, and trust and coordination games. Annapurna’s research interests also lie in complex adaptive systems, game theory, machine learning, electronic commerce, and artificial intelligence. Her work has also appeared in the Journal of Group Decision and Negotiation. Annapurna obtained dual BS degrees in Computer Science and Finance from the University of Maryland, College Park.

David C. Croson is Visiting Professor of Management Science at the MIT Sloan School of Management, and a former Assistant Professor of Operations and Information Management and Senior Fellow at the Financial Institutions Center at the Wharton School of the University of Pennsylvania. His research focuses on strategy in high-technology industries and the economic value of information. Croson holds a PhD in Business Economics from Harvard University and BS and MS degrees from the Pennsylvania State University.
