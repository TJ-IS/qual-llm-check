---
otero_id: 26582
otero_key: "VU6759EP"
title: "Analyzing Frictions in Generalized Second-Price Auction Markets"
authors: "Karthik Kannan; Vandith Pamuru; Yaroslav Rosokha"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1187"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analyzing Frictions in Generalized Second-Price Auction Markets

Karthik Kannan,<sup>a,</sup>\* Vandith Pamuru,<sup>b</sup> Yaroslav Rosokha<sup>c</sup>

<sup>a</sup> Eller College of Management, University of Arizona, Tucson, Arizona 85721; <sup>b</sup> Indian School of Business, Hyderabad 500 111, India; <sup>c</sup> Krannert School of Management, Purdue University, West Lafayette, Indiana 47907

Contact: kkarthik@arizona.edu, https://orcid.org/0000-0002-9861-0717 (KK); vandith\_pamuru@isb.edu, https://orcid.org/0000-0002-8572-5099 (VP); yrosokha@purdue.edu, https://orcid.org/0000-0002-8567-659X (YR)

Received: August 9, 2019 Revised: December 21, 2020; May 31, 2022; September 26, 2022 Accepted: October 12, 2022 Published Online in Articles in Advance: December 14, 2022

https://doi.org/10.1287/isre.2022.1187

Copyright: © 2022 INFORMS

Abstract. We investigate the role of frictions in determining the efficiency and bidding behavior in a generalized second-price auction—the most preferred mechanism for sponsored-search advertisements. In particular, we take a twofold approach of Q-learning–based computational simulations in conjunction with human-subject experiments. We find that the lower valued advertisers (who do not win the auction) exhibit highly exploratory behavior. Moreover, we find the presence of market frictions moderates this phenomenon and results in higher allocative efficiency. These results have implications for policymakers and auction-platform managers in designing incentives for more efficient auctions.

History: Ahmed Abbasi, Senior Editor; Idris Adjerid, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.1187.

Keywords: auctions • generalized second-price auctions • human-subject experiments • Q-learning • machine learning • reinforcement learning

## 1. Introduction

The online ad market has grown enormously over the last two decades. For example, Google Ads platform revenue grew from \$70M in 2001 to \$209B in 2021 (Statista 2022). Search-ad platforms have also evolved. Initially, human involvement in the decision-making process on these platforms was quite high. Over the years, however, advances in artificial intelligence (AI), including automation (e.g., Google’s automated bidding) and data-analytics tools (e.g., Google’s auction insights reports), have contributed to a substantial reduction in human involvement in day-to-day bidding and data analysis. Despite the technological advances, the search-ad marketplace continues to be highly complex and dynamic with bidders (advertisers) not being aware of their competitors, their valuations, or their bids; in some cases, the demand may be seasonal (e.g., roses for Valentine’s Day) or eventdriven (e.g., masks during COVID). So both entities— humans and software agents—deal with a significant amount of learning. For example, humans must learn to set parameters, such as the maximum bid and budget; the software agents must learn to bid effectively.

Advertisers in the online ad markets face various forms of frictions, including participation costs, model evaluation and estimation costs, and bid-adjustment costs. Generally, the technological advances have reduced these costs, allowing more advertisers to enter these markets.

Although conventional wisdom suggests reduction in frictions is good, in many instances, some level of friction is needed for stability and to prevent welfare destruction. For example, frictions—in the form of circuit breakers to stop stock prices from dropping more than 7%, 13%, and 20%—are designed to prevent software bots from wreaking havoc in financial markets. That said, the impact of frictions on welfare in search-auction contexts is at best unclear. So we are motivated to study the research question regarding how the allocative efficiency changes with friction in search-auction markets.

We frame our research question in the context of the generalized second-price (GSP) auction, which is the most preferred mechanism for sponsored-search advertisements. GSP is a highly dynamic, complex system that, as alluded to earlier, involves cascades of decisionmaking entities engaged in learning and exploration. At one level, the automated software agents learn to bid within the confines of restrictions imposed by humans. At a second level, humans learn to define the parameters and boundaries of the software agents (e.g., extent of exploration, maximum bid, budget, and duration). If field experiments were ideally feasible, one would control the costs for humans to participate to fine-tune the parameters and similarly the cost for the software agents to quickly respond. However, without the knowledge about the bidder’s private information (e.g., valuations and costs), the analysis of the data from field experiments becomes quite difficult. Note that the seminal theoretical work by Edelman et al. (2007), which demonstrates that advertisers bid at most their value in a weakly dominant equilibria, employs an extremely simplified representation of GSP. However, in reality, GSP is a complex system, and obtaining a closed-form solution for such complex systems is generally hard. Furthermore, no theory exists for studying the impact of frictions on exploration and learning by the advertisers in the dynamic GSP setting.

The sponsored-search platforms and policymakers can best observe and influence the bid-adjustment costs; hence, we primarily study the role of this cost when studying the role of frictions. To understand why a reduction in frictions may lead to lower allocative efficiency, consider the behavior of the lowest valued advertisers, who are often “assumed away” during the theoretical analysis. In particular, behavior by the lowest valued advertisers may be different for two reasons. First, in GSP, the exploration–exploitation trade-off is different depending on whether the bidder has a high or low value. Specifically, a high-valued bidder is likely to stick to a higher but still profitable bid, whereas a low-valued agent is likely to explore because the agent is earning a zero profit (associated with not getting a slot). The second reason is that the design of the GSP introduces different levels of information asymmetry, depending on whether a bidder wins a slot. Specifically, an advertiser who is winning one of the available slots not only knows the advertiser’s bid, but also knows the next highest bid. However, an advertiser who does not win any slot does not know anything regarding the behavior of others. So the only way the advertiser can learn this information is by exploring with higher bids. Both of these reasons may lead the lowest valued agent to revise the agent’s bids in the absence of bid-adjustment frictions. Given the complexity and interdependence of the GSP, excessive adjustments by the lowest valued agents may lead high-valued agents to do the same and, thus, exacerbate the amount of exploration in the market, leading to suboptimal allocation outcomes. Such unexpected negative effects of reduction in frictions are not yet studied in the context of GSP, and we aim to investigate them.

Three particular aspects related to friction costs challenge the assumptions underlying the existing theoretical models and the validity of the results. First, GSP allocates constrained resources over an infinite series of auctions, in which the submitted bids are used as the default until changed. Because bidders may change their bids at any time and in an uncoordinated fashion, the payoffs realized and responses are also uncoordinated. So modeling such asynchronous decision making is quite challenging in theoretical models. Yet adopting a dynamic perspective as highlighted with empirical evidence by Zhang and Feng (2011) is important. The second related aspect is that bidders in GSP lack complete knowledge of the environment (e.g., they are usually unaware of the valuations of other bidders and the efficacy of different bids that they can make). In other words, in reality, bidders face the associated exploration–exploitation trade-offs when learning.<sup>1</sup> And, finally, the experimental literature on GSP as well as the broader experimental literature on auctions (e.g., Cooper and Fang 2008, Sheremeta 2010, Kamijo 2013, Noti et al. 2014, McLaughlin and Friedman 2016) shows participants regularly overbid (i.e., bid more than their own valuations), which is contrary to theoretical assumptions. So accounting for such nonstandard behaviors only complicates the analyses. Although a few papers focus on deviations from the basic theoretical model (e.g., Jerath et al. 2011, Simonov et al. 2018), none analyzes the role of frictions in mitigating commonly observed deviations (e.g., overbidding).

Instead of studying the complex problem involving both human and AI entities interacting within the GSP, we break up and study the effect of friction on each entity separately. Our twofold strategy is as follows. First, we use reinforcement-learning computational agents for conducting a computational experiment to study the effect of frictions for the AI agents. These agents implement a version of Q-learning (Sutton and Barto 1998) and participate in an environment akin to Edelman et al. (2007).<sup>2</sup> Second, we use human-subject experiments. For our experimental approach, we run controlled laboratory experiments with human decision makers. In both cases, we use the frameworks to study the effect of friction costs. We discover the effect of frictions is largely consistent across both approaches. In particular, we show frictions may have a stabilizing effect in highly interdependent auction mechanisms, leading to the following key result: allocative efficiency increases in the presence of frictions. Note that our results with Q-learning agents may be viewed as involving decision makers without the psychological characteristics, whereas the second set of results from behavioral economic experiments incorporate the vast heterogeneity of behaviors and psychologi cal factors. By combining the two approaches, we are able to get a better sense of the key role of exploration that leads to lower allocative efficiency when friction costs are reduced. Importantly, by establishing the results for both computational agents and human subjects, we are confident our results hold for various levels of human involvement in the GSP from the manual bidding for niche keywords (Hutchings 2014) to the highly automated AI agents on the other extreme of the spectrum.

The rest of the paper is organized as follows: In Section 2, we outline the previous literature that relates to our paper. In Section 3, we present details of the auction environment and the results of our agent-based computational simulations. In Section 4, we present the design, the data, and the main results of the humansubject experiment. In addition to the two main studies, we conduct two additional studies (presented in Sections 5 and 6) to provide insights regarding the role of frictions in GSP. Finally, in Section 7, we summarize our research findings, discuss limitations, and outline future research directions.

## 2. Literature

Our study contributes to three streams of literature. First, we contribute to the literature on sponsored-search advertisement and auction mechanisms. Second, we contribute to a growing body of literature in information systems (IS) that uses economic experiments. And, third, we contribute to the emerging literature that uses machine learning models to study market outcomes. Next, we provide a brief review of each of the three streams of literature.

## 2.1. Sponsored-Search Keyword Auctions

The sponsored-search auctions have attracted considerable interest in the IS literature. Several empirical studies focus on the evolution of bidding strategies and the resulting impact on sponsored-search metrics (e.g., Ghose and Yang 2009; Animesh et al. 2010, 2011). The bidding strategies are also the focus of Zhang and Feng (2011), who introduce a dynamic model to study cyclic bidding by advertisers. A number of theoretical papers expand on the works of Edelman et al. (2007) and Varian (2007) to improve the auction outcomes (e.g., Filiz-Ozbay and Ozbay 2007, Varian 2009, Chen et al. 2010, Edelman and Schwarz 2010, Amaldoss et al. 2015) or evaluate alternative mechanisms (e.g., Feng et al. 2007). Though most of the works consider the auction for an individual keyword, some studies explore the bidding for multiple keywords (e.g., Du et al. 2017) and the interaction between organic results and the sponsoredsearch results as competing information sources (e.g., Xu et al. 2012, Agarwal et al. 2015). Furthermore, recent works investigate more advanced variations of the auction environment, including auctions with unknown click-through rates (Devanur and Kakade 2009, Gatti et al. 2012), auctions with dependent click-through rates (Kempe and Mahdian 2008, Deng and Yu 2009, Simonov et al. 2018), and auctions with budget constraints (Zhou et al. 2008, Arnon and Mansour 2011). Qin et al. (2015) provide a comprehensive review of the sponsored-search-auction literature.

Our paper contributes to this vast literature by studying the GSP auction outcomes and bidding behavior in the presence of market frictions. In particular, recent advances in technology have resulted in significantly reduced informational frictions in the sponsored-search auctions. Further, the proliferation of AI tools (e.g., autobidders) further contribute to the reduction of frictions. Although frictions are studied in different contexts, including trade (Hou and Moskowitz 2005, Allen 2014), stock markets (Capasso 2008), housing markets (Anenberg 2016), and labor markets (Bassi and Nansamba 2017), we aim to study frictions in the context of sponsored-search auctions. In particular, we incorporate these frictions into the model presented in Edelman et al. (2007). We then employ a twofold strategy of investigating the auction outcomes, using machine learning computational agents in combination with human-subject experiments. We next present a brief review of the literature on economic experiments and computational methods.

## 2.2. Economic Experiments in IS

The use of laboratory experiments to test theoretical insights and guide the design of systems has gained substantial traction in the IS field. Following the early work, which includes the development of the technology acceptance model by Bagozzi et al. (1992) and the evalu ation of the task-technology fit model by Goodhue and Thompson (1995), recent literature expands the use of experiments to a variety of IS applications, including privacy (e.g., Tsai et al. 2011, Brandimarte et al. 2013), bundle pricing (e.g., Goh and Bockstedt 2013), and recommender systems (e.g., Adomavicius et al. 2013a, 2014). In a recent review of the experimental literature in IS, Gupta et al. (2018) argue that experiments can yield meaningful results that overcome the limitations that empirical and theoretical studies face. In the context of our study, to make any conclusions about allocative efficiency or bidding behavior, we must observe the private valuations of the auction advertisers, which is not possible using real-world data.

The experimental approach is particularly fruitful in studying auctions (e.g., Adomavicius et al. 2006, 2012, 2013b; Bapna et al. 2010; Cason et al. 2011; Sanyal 2016). Several early experiments on behavior in auctions report that subjects rarely choose the dominant strategy (Kagel et al. 1987, 1995; Kagel and Levin 2001). In particular, the robust finding in this literature is that human subjects regularly bid higher than their value. Closest to our paper are five recent studies that investigate GSP auc tions experimentally: Fukuda et al. (2013), Noti et al. (2014), McLaughlin and Friedman (2016), Che et al. (2017), and Bae and Kagel (2019). With the exception of McLaughlin and Friedman (2016), these studies find significant overbidding behavior by the participants. The primary question in all of these studies, however, is different from ours. Whereas prior studies focus on the comparison of GSP with VCG mechanisms, we investigate the role of frictions in improving outcomes of the GSP auction. In particular, we focus on how the presence of market frictions may mitigate overbidding behavior and lead to higher allocative efficiency. In addition, the use of machine learning agents in combination with human-subject experiments is a distinctive feature of this paper.

## 2.3. Agent-Based Computational Models

In addition to theoretical, empirical, and experimental approaches, agent-based simulations are successfully used to provide insights in the context of allocation problems. For example, Guo et al. (2012) analyze bundletrading markets for distributed resource allocations. Ketter et al. (2012) study trading-agent competition in a supply chain context in which a need exists to make product-pricing and inventory-resource-allocation decisions in real time. In the context of auctions, Bichler et al. (2013) study the efficiency of combinatorial clock auctions, Kiose and Voudouris (2015) study power auctions, and Guerci et al. (2014) investigate sequential Dutch auctions.

For our study, we employ Q-learning (Watkins and Dayan 1992), a reinforcement-learning approach, to model the behavior of advertisers in the GSP environment. We chose Q-learning for several reasons. First, it is used to investigate learning in multiple-agent environments $( \mathrm { e . g . } ,$ Littman 1994, Sandholm and Crites 1996, Bowling and Veloso 2001, Greenwald et al. 2003, Calvano et al. 2020). Second, Q-learning is used to match behavioral regularities observed in human-subject experiments (Rosokha and Younge 2020). More broadly, previous studies, including Silvetti and Verguts (2012), Botvinick et al. (2009), and Shteingart and Loewenstein (2014), show the similarity between the human- and reinforcement-learning approaches. Third, Q-learning algorithms are successfully applied to investigate the efficacy of information revelation and structural properties in a variety of auctions (Greenwald et al. 2010). Finally, the reinforcementlearning approach is not new to the GSP. Chen et al. (2016b) establish a connection between machine learning models and the game-theoretic properties of a system, using real data from a sponsored-search-advertising platform.

## 3. Computational Analysis

In this section, we first present the environment (Section 3.1); second, we present details of our implementation of the agent-based model (Section 3.2); and, finally, we state the main results of our simulations (Section 3.3).

## 3.1. Core GSP Model

To study the problem in a structured manner, we build from a theoretical model. However, we are not aware of any universally accepted theoretical model in GSP because certain assumptions are shown to be violated. Therefore, we consider a specialization of, arguably, the most well-known paper—Edelman et al. (2007)—and incorporate elements related to frictions. In particular, the GSP environment contains J advertisers, each with a unit demand, participating in an auction for K ad slots. We assume $J { > } \bar { K } . ^ { 3 }$ Each advertiser submits only one bid.

The advertisers may be placed in either of the K slots. Let $\alpha _ { k }$ represent the click-through rate for the kth ad slot.

Conditional on the click-through, advertiser j realizes a value $v ^ { j } ,$ and without loss of generality, we assume $v ^ { j } > v ^ { j + 1 } \{ \forall j \}$ . In our implementation, we assume that the valuations are private information and drawn from a uniform distribution.<sup>4</sup> We define a rank function $j \to ( k )$ that maps an advertiser j to an ad slot k based on the descending order of bids.<sup>5</sup> Therefore, we represent the valuation realized by the kth highest bidding advertiser as $v ^ { ( k ) }$ and the advertiser’s corresponding bid as $b ^ { ( k ) }$ . The key element of the GSP is that each winning advertiser pays an amount equal to the next highest bid. Therefore, the payoff for the kth highest bidding advertiser (allotted $\alpha _ { k } ( v ^ { ( k ) } - b ^ { ( k + 1 ) } ) .$ 6 to the kth slot) is given by

In this paper, we focus on two metrics of interest. The first metric of interest is the allocative efficiency of the auction. This metric captures the amount of realized social welfare relative to the maximum possible value. In particular, given the preceding setup, we define the allocative efficiency as

$$
\Psi = \frac {\sum_ {k = 1} ^ {K} \alpha_ {k} v ^ {(k)}}{\sum_ {j = 1} ^ {K} \alpha_ {j} v ^ {j}}.\tag{1}
$$

The second metric of interest is the bid-to-value ratio for each of the advertisers, and it captures the individual level behavior. Specifically, the bid-to-value ratio for the advertiser of rank j is

$$
\Omega^ {j} = \frac {b ^ {j}}{v ^ {j}}.\tag{2}
$$

Note that, whereas $\Omega ^ { j }$ is calculated at the individual level, Ψ is calculated at the market level.

We model frictions as an additional cost $C ^ { j }$ incurred by advertiser j from revising the advertiser’s bids. That is, the payoff for advertiser j who places the kth highest bid is

$$
\pi^ {j} = \alpha_ {k} (v ^ {j} - b ^ {(k + 1)}) - C ^ {j},\tag{3}
$$

where $C ^ { j }$ could, for example, correspond to implicit costs, such as the efforts the advertisers take to repeatedly change their bids, or explicit costs, such as fees charged by the platforms. Note that, in the latter case, the allocative efficiency is equivalent to the overall efficiency of the market.

Next, we follow Edelman et al. (2007) and study a specific case with $J = 3$ and $K = 2$ . Without loss of generality, we assume $\alpha _ { 1 } = 1 > \alpha _ { 2 } = \alpha > \alpha _ { 3 } = 0 . ^ { 7 }$ That is, the third slot is assumed to have a zero click-through rate, and α captures the similarity between the top two ad slots. The equilibrium analysis from Edelman et al. (2007) provides several theoretical predictions for the case in which $C ^ { j } = 0$ . In particular, regarding the allocative efficiency, the theory predicts that the outcome of the auction is fully efficient $( \mathrm { i . e . , } \Psi = 1 )$ ). Regarding the bid-to-value ratio, the theory does not make a precise prediction because infinitely many equilibria are possible. Nevertheless, the assumption that the lowest valued advertisers bid their true value $( \mathrm { i . e . , } \Omega ^ { 3 } = 1 )$ , which is a weakly dominant strategy for those players, is common. This assumption, in turn, leads to a prediction regarding the bid-to-value ratio and the slot-similarity parameter for the medium-valued advertisers $( \mathrm { i } . \mathrm { e } . , j = 2 )$ Specifically, it is straightforward to derive that $\Omega ^ { 2 }$ is decreasing in $\alpha . ^ { 8 }$ Crucially, theory makes no predictions regarding the behavior of the highest valued advertisers $( \mathrm { i } . \mathrm { e } . , j = 1 )$ and is at odds with experimental evidence on overbidding mentioned earlier. Furthermore, extant theory does not incorporate friction costs for the case of $C ^ { j } > 0$ . Therefore, we turn to a computational and experimental approach to shed light on the outcomes of the GSP auctions with frictions.

## 3.2. Agent-Based Implementation of the GSP Environment

Consistent with the theoretical underpinning, we allow a group of $J = 3$ agents to compete for $\bar { K } = 2$ ad slots. The agents learn how to bid using the Q-learning model, described next.

3.2.1. Q-Learning Model Details. Prior literature utilizes variants of Q-learning to extensively study sponsoredsearch auctions (Chen et al. 2016b), Cai et al. 2017, Wu et al. 2018). However, their focus is different in that they aimed at designing better autobidders that optimize an advertiser’s payoff under different constraints. None considers frictions or the market-level outcomes, such as allocative efficiency. Furthermore, we combine this method with human-subject experiments, which is unique and novel.

Fundamental to the algorithm are the Q-values, denoted as $Q ( s , a ) ,$ , which represent the value of taking an action a in state $s .$ The Q-values are learned over time using a reinforcement-learning process. Specifically, suppose that, at time $t ,$ the agent selects an action $a _ { t } ,$ observes a reward $\pi _ { t } ,$ and enters a state $s _ { t + 1 }$ . Then, the Q-value is updated as follows:

$$
Q ^ {n e w} (s _ {t}, a _ {t}) \leftarrow (1 - \delta) Q (s _ {t}, a _ {t}) + \delta (\pi_ {t} + \gamma m a x _ {a} Q (s _ {t + 1}, a)),\tag{4}
$$

where $0 \leq \delta \leq 1$ is the learning rate and $0 \leq \gamma \leq 1$ is the discount factor. Although the objective of a Q-learning agent is to learn an optimal policy that maximizes the expected reward, the agent also faces ongoing performance pressure. In other words, when choosing to revise an action (i.e., bid), the agent has to balance exploration versus exploitation. To operationalize this trade-off, we use the Boltzmann softmax policy function, which is common in the literature.<sup>9</sup> Specifically, the action is determined using the Boltzmann probability distribution: $e ^ { \lambda Q ( s , a ) } / { \sum _ { a _ { i } } e ^ { \lambda \breve { Q } ( s , a _ { i } ) } } ~ \forall a _ { i } \in A ( s )$ , where A(s)

is the set of actions available in state s and λ captures the amount of exploration.<sup>10</sup> In this way, Q-learning is a type of stochastic learning model that selects more profitable actions more often but still may select less profitable actions occasionally, thus ensuring all of the bidding space is explored.

We implement the Q-learning algorithm in our GSP context as follows. A group of $J = 3$ agents compete for $K = 2$ ad slots over $\bar { M } \bar { = } 2 , \bar { 0 0 0 }$ matches. Each match lasts $T = 1 0 0$ time periods, indexed by t. At the beginning of each match $( t ~ = ~ 0 )$ , private values $v ^ { j }$ are randomly drawn from $\mathcal { U } \{ 1 , 1 0 \} . ^ { 1 \bar { 1 } }$ The values are retained for the duration of the match. For every $t ,$ the agent chooses to place a bid $b _ { t } ^ { j }$ from $\mathcal { U } \{ 0 , 1 0 \}$ . As mentioned earlier, the chosen bid depends on the state s in which the agent is. In our implementation of the GSP environment, the state $s _ { t }$ is the agent’s private valuation $v ^ { j . 1 2 }$ That is, agent j decides on a bid $b _ { t }$ based on the private value, $v ^ { j } .$ . Importantly, we assume that the friction cost of C is incurred every time the agent changes the bid from period t – 1 to $t \left( \mathrm { i . e . , i f } b _ { t } \neq b _ { t - 1 } \right)$ and this cost is a constant and the same across all agents. After all the bids are submitted at time $t ,$ the slots are allocated in the order of the bids (with ties broken randomly). Each agent is assumed to gain $\alpha _ { k } v ^ { j }$ but incurs $\alpha _ { k } b ^ { k }$ as payment to the intermediary and $C ^ { j }$ as the bid-adjustment cost (if any). At the end of the match $( t = 1 0 0 )$ , the bids and the outcomes (bid-to-value ratio and allocative efficiency) are recorded.

Although our primary goal is to study the effect of frictions, an economic insight on the effect of α is important. For one, the platform can somewhat control α (by making sure that the likelihood of ads in other slots are also at the same level as the first slot). As ad slots become more similar, the advertisers no longer need to learn the differences between ad slots, which can interact with the role friction. Therefore, to derive comparative static predictions, we execute all these steps for various combinations of C and $\alpha ,$ specifically, $\bar { C } \in \{ 0 . 0 , 0 . 5 , 1 . 0 \}$ } and $\alpha \in \{ 0 . 2 , 0 . 5 , 0 . 8 \}$ . A summary of variables and parameters for our algorithm are presented in Table 1. For details on our implementation of the Q-learning model as well as robustness checks for different parameter values, see Online Appendix A.

Table 1. Summary of Q-Learning Variables and Parameters for GSP

<table><tr><td colspan="2">States and actions</td></tr><tr><td>State:  $s_{t}^{j} \rightarrow$ </td><td> $v^{j}$ </td></tr><tr><td>Action:  $a_{t}^{j} \rightarrow$ </td><td> $b_{t}^{j}$ </td></tr><tr><td>Reward:  $\pi_{t}^{j} \rightarrow$ </td><td> $\alpha_{k}(v^{j} - b_{t}^{(k+1)}) - C^{j}$ </td></tr><tr><td colspan="2">Environment parameters</td></tr><tr><td> $\delta \rightarrow$ </td><td>0.1</td></tr><tr><td> $\gamma \rightarrow$ </td><td>0.99</td></tr><tr><td> $\lambda \rightarrow$ </td><td>1</td></tr><tr><td colspan="2">Treatment variables</td></tr><tr><td> $C \rightarrow$ </td><td> $\{0.0, 0.5, 1.0\}$ </td></tr><tr><td> $\alpha \rightarrow$ </td><td> $\{0.2, 0.5, 0.8\}$ </td></tr></table>

Note. Recall that a rank function j → (k) maps agent j to the $k ^ { \mathrm { { t h } } }$ ad slot.

Table 2. Number of Bid Adjustments

<table><tr><td rowspan="2"></td><td colspan="3">(a) Highest valued agent</td><td colspan="3">(b) Medium valued agent</td><td colspan="3">(c) Lowest valued agent</td></tr><tr><td>C = 0.0</td><td>C = 0.5</td><td>C = 1.0</td><td>C = 0.0</td><td>C = 0.5</td><td>C = 1.0</td><td>C = 0.0</td><td>C = 0.5</td><td>C = 1.0</td></tr><tr><td>α = 0.2</td><td>46.3(0.5)</td><td>20.3(0.3)</td><td>7.7(0.2)</td><td>47.7(1.1)</td><td>19.5(0.5)</td><td>7.9(0.2)</td><td>64.4(1.4)</td><td>46.8(0.8)</td><td>28.2(0.4)</td></tr><tr><td>α = 0.5</td><td>48.6(0.8)</td><td>26.0(0.2)</td><td>10.2(0.2)</td><td>43.2(1.3)</td><td>15.1(0.6)</td><td>7.5(0.3)</td><td>54.7(1.5)</td><td>30.3(1.0)</td><td>19.2(0.5)</td></tr><tr><td>α = 0.8</td><td>52.4(0.9)</td><td>31.6(0.3)</td><td>19.9(0.2)</td><td>41.4(1.4)</td><td>14.4(0.7)</td><td>7.2(0.4)</td><td>51.6(1.5)</td><td>27.6(1.3)</td><td>16.7(0.8)</td></tr><tr><td>Average</td><td>49.1(0.7)</td><td>25.9(0.3)</td><td>11.9(0.2)</td><td>44.1(1.3)</td><td>16.3(0.6)</td><td>7.5(0.3)</td><td>56(1.5)</td><td>34.9(1.1)</td><td>21.4(0.6)</td></tr></table>

Notes. Results are rounded to the nearest decimal. The maximum number of adjustments can be 100.

## 3.3. Agent-Based Simulation

This section presents results of our learning-model simulations. Sections 3.3.1 and 3.3.2 consider individuallevel outcomes, whereas in Section 3.3.3, we present the market-level outcomes.

3.3.1. Exploratory Behavior. First, we look at the number of bid adjustments made by each agent, which reflects the agent’s exploratory behavior. Table 2 presents the number of bid adjustments that agents make, on average, across $n = 1 0 0 , 0 0 0$ simulations. The three panels of Table 2 present the number of bid adjustments for each of the three agents, $j \in \{ 1 , 2 , 3 \}$ , sorted based on their private values and labeled as the highest, medium, and lowest valued agents, respectively.<sup>13</sup> The rows correspond to different values of $\alpha ,$ whereas the columns within each panel correspond to different values of C.

The key takeaway from Table 2 is that the number of bid adjustments decreases as the friction costs increase. This finding is expected and intuitive; when the exploration becomes costlier, the agents explore less. We summarize this takeaway with Result 1.

Result 1. Lower costs lead to more exploration.

3.3.2. Bidding Behavior. Table 3 presents outcomes in terms of the bid-to-value ratios. Similar to Table 2, the three panels of Table 3 present the average bidto-value ratios for each of the three agents, $j \in \left\{ { 1 , 2 , 3 } \right\}$ sorted based on their private values. Again, the rows correspond to different values of $\alpha ,$ whereas the columns within each panel correspond to different values of C.

Table 3 offers three takeaways. The first is that the bid-to-value ratios are highest for the lowest valued agents, who tend to overbid (i.e., these agents submit bids more than their valuation, resulting in bid-to-value ratios greater than 1.0 on average). The main reason for overbidding in the computational simulations is that agents implement the softmax action-selection policy, which means that actions with similar payoffs are chosen with similar probability. Thus, given that bids over the true value are likely to yield an expected payoff that is comparable to bidding the true value or below, the overbidding observation is not surprising. The practical intuition for this result is that the lowest valued agents are likely to explore the action space to try to find a prof itable bid, which can only occur if they bid higher than the medium valued agents. We summarize these observations with Result 2.

Result 2. The bid-to-value ratio is higher for lower valued agents.

Table 3. Bid-to-Value Ratios

<table><tr><td rowspan="2"></td><td colspan="3">(a) Highest valued agent</td><td colspan="3">(b) Medium valued agent</td><td colspan="3">(c) Lowest valued agent</td></tr><tr><td>C = 0.0</td><td>C = 0.5</td><td>C = 1.0</td><td>C = 0.0</td><td>C = 0.5</td><td>C = 1.0</td><td>C = 0.0</td><td>C = 0.5</td><td>C = 1.0</td></tr><tr><td>α = 0.2</td><td>0.839(0.020)</td><td>0.848(0.023)</td><td>0.849(0.021)</td><td>0.918(0.040)</td><td>0.919(0.050)</td><td>0.904(0.046)</td><td>1.293(0.100)</td><td>1.258(0.119)</td><td>1.116(0.114)</td></tr><tr><td>α = 0.5</td><td>0.757(0.022)</td><td>0.758(0.023)</td><td>0.762(0.021)</td><td>0.827(0.037)</td><td>0.832(0.040)</td><td>0.831(0.032)</td><td>1.101(0.092)</td><td>1.072(0.094)</td><td>1.028(0.081)</td></tr><tr><td>α = 0.8</td><td>0.691(0.022)</td><td>0.694(0.024)</td><td>0.688(0.023)</td><td>0.781(0.029)</td><td>0.777(0.035)</td><td>0.772(0.032)</td><td>0.993(0.067)</td><td>0.972(0.079)</td><td>0.945(0.075)</td></tr><tr><td>Average</td><td>0.762(0.021)</td><td>0.766(0.024)</td><td>0.767(0.022)</td><td>0.842(0.036)</td><td>0.843(0.042)</td><td>0.835(0.038)</td><td>1.129(0.087)</td><td>1.101(0.099)</td><td>1.029(0.092)</td></tr></table>

Note. Ω<sup>j</sup> > 1 means that agent j is overbidding.

The second takeaway from Table 3 is that costs play a role in the bid-to-value ratios only for the lowest valued agents. Specifically, conditional on $\alpha ,$ the bid-to-value ratios of the highest and medium valued agents stay remarkably consistent, whereas the bid-to-value ratios for the lowest valued agents drop by approximately 10% as costs increase from $C = 0 . 0$ to 1.0. The intuition for this result is that frictions have the biggest impact on the exploration–exploitation trade-off for the lowest valued agents (i.e., the benefit of exploring bids above own true value in order to have a chance for a small profit no longer justifies the cost of bid adjustment). Thus, frictions moderate overbidding by the lowest valued advertisers. We summarize this takeaway with Result 3.

## Result 3. For the lowest valued agents, the bid-to-value ratio increases as friction decreases.

The last takeaway from Table 3 concerns the role of $\alpha .$ As described in Endnote $^ { 8 , }$ theory suggests $\Omega ^ { 2 }$ is decreasing in $\alpha .$ Note that this theoretical prediction is only true for the middle-valued agent. We notice a similar relationship from our computational agents as well. In particular, the table shows that as α increases, the bidto-value ratio decreases for all agents regardless of their respective private-value ranks. Intuitively, because the slots tend to become similar (i.e., α tends toward one), the value from exploring in order to move to the better slot is reduced. Thus, as the exploration decreases, their interest in overbidding also decreases. We summarize this takeaway with Result 4.

## Result 4. The bid-to-value ratio decreases as α increases.

3.3.3. Allocative Efficiency. Panel (a) of Figure 1 presents the evolution of the allocative efficiency, Ω, over

Figure 1. (Color online) Allocative Efficiency the learning horizon, whereas panel (b) of the figure presents a more detailed breakdown of the converged outcomes.<sup>14</sup> Figure 1(a) shows that, initially, allocative efficiency is the same across the three cost treatments (around 0.85). However, as agents learn, the efficiency increases and differences among the three cost scenarios appear. In particular, the main observation from the figure is that allocative efficiency is higher with higher costs.<sup>15</sup> Figure 1(b) shows this finding is true regardless of α although, when alpha is low, the increase is higher. We summarize these observations with Result 5.

(a)  
![](/api/attachments/VU6759EP/fulltext/images/337bcfe63700a9f4b162ed9ab8dae0a3f88c68aa8a038657e23168696e6d1510.jpg)

## Result 5. Allocative efficiency of the market increases as friction costs increase.

Several points are important to reiterate. First, with the exception of Result $^ { 4 , }$ the theory of Edelman et al. (2007) does not provide predictions that correspond to those obtained with our agent-based model. Second, the predictions obtained in this section are not intended as point predictions; instead, the takeaways from the tables should be qualitative in nature. Third, the predictions are based on a relatively simple learning framework that is independent of the other behavioral factors that may also play a role when humans participate in the auction. Thus, although we expect the general trends observed in the computational model to hold in a human-subject experiment, psychological factors, such as auction fever (Adam et al. 2011), spite (Cooper and Fang 2008), and joy of winning (Cooper and Fang 2008, Sheremeta 2010) among nonwinners also can strengthen or weaken these results. Finally, in this study, we focus on allocative efficiency of the auction and abstract away from whether friction costs are lost (i.e., time and effort) or collected by the platform (e.g., fees). In Online $\mathrm { A p \mathrm { - } }$ pendix ${ \mathrm { F } } ,$ we show that, if all friction costs are lost, the revenue by the platform is decreasing in costs. However, if the platform collects the friction costs, as is the case with fees, the revenue may increase.

(b)

<table><tr><td></td><td>C=0.0</td><td>C=0.5</td><td>C=1.0</td></tr><tr><td>α=0.2</td><td>0.944(0.009)</td><td>0.952(0.011)</td><td>0.959(0.009)</td></tr><tr><td>α=0.5</td><td>0.951(0.007)</td><td>0.956(0.010)</td><td>0.961(0.009)</td></tr><tr><td>α=0.8</td><td>0.951(0.009)</td><td>0.957(0.007)</td><td>0.961(0.006)</td></tr><tr><td>Average</td><td>0.948(0.008)</td><td>0.955(0.009)</td><td>0.961(0.008)</td></tr></table>

Notes. (a) Evolution of allocative efficiency throughout the learning horizon (for α � 0:5). (b) Allocative efficiency in converged markets (matche 1,800–2,000).

## 4. Experimental Analysis

This section describes the experimental design for the auction presented in Section 3.2.1. The nomenclature used is consistent with our usage when conducting the experiments and is somewhat different from earlier. In particular, we use language in the experiment that is more intuitive for the human-subject participants. Specifically, we refer to the advertisers as participants in the experiment, the ad slots as goods on which the participants bid, and the auction as a match in which participants bid. As is the norm with economic experiments, the amount of money that participants make at the end of the experiment depends on their performance in the experiment.

## 4.1. Treatments

Our primary objective is to investigate the role of friction costs on the outcomes of the GSP. Therefore, the two main treatments of the experiment concern the costs of the bid adjustments imposed on the participants. Specifically, the experiment consisted of two between-subjects treatments with respect to the cost of adjustment, C. We also set out to vary α to establish the generality of the result (recall that α determines the similarity between the value of the top two slots). However, because the similarity of ad slots is not our main focus, we varied α within subjects. That is, during the experiment, each participant was likely to experience multiple α’s but the same C. Table 4 presents a summary of the two treatment dimensions.

The between-subjects treatments were costless (C � 0) and costly (C � 0.1) bid adjustments. In the costless treatment, subjects incurred a cost of C � 0.0 for changing their bid during the match. In the costly treatment, subjects incurred a cost of C � 0.1 for changing their bid during the auction. In both cases, however, subjects could place the initial bid at no cost. Because subjects incurred the cost every time they changed their bid, they could incur multiple costs in the same match. In particular, a subject could make as many adjustments as the subject wanted until the time for the match expired. The withinsubjects treatments were low (α � 0:2), medium (α � 0:5), and high (α � 0:8) correlation. All participants in a group had the same $\alpha \in \{ 0 . 2 , 0 . 5 , 0 . 8 \}$ for the duration of each match.

## 4.2. Matches

Each session consisted of M � 10 matches. At the begin ning of each match, participants were randomly split into groups of three (J � 3) and remained so until the end of the match. The regrouping for the next match was random to avoid any systematic learning about participant behaviors. Earnings for the experiment were the sum of payoffs across all 10 matches.

To avoid the end-of-match effects associated with the fixed duration of a match, we opted for random termination. Specifically, each match lasted at least 20 seconds, after which the chance of the match terminating each second was 1%. Thus, the expected duration of each match was two minutes. To ensure a valid comparison across sessions, we used the same sequence of seconds across matches in every session.<sup>16</sup> We summarize this design choice with Remark 1.

## Remark 1. We used a random-termination protocol.

For each match, the participants were provided with randomly drawn private values for good 1. We then obtained the value of good 2 by multiplying the value of good 1 and α. Parameters for the initial four matches were drawn at random without any restriction. However, in matches 5–10, we aimed to provide a clean comparison among the treatments. Therefore, we used common seeds to generate the same random values across the two treatment dimensions. This approach ensured that any learning that took place in the early matches was not systematically biased and allowed us to compare across different values of α using the later matches. We summarize this design choice with Remark 2.

Remark 2. We used common random numbers in matches 5–10 such that, for each match,

• $m \in \{ 5 , \ldots , 1 0 \}$ , all groups had the same three valuations $\{ v _ { m } ^ { 1 } , v _ { m } ^ { 2 } , v _ { m } ^ { 3 } \}$

$m \in \{ 5 , \ldots , 1 0 \}$ , there was at least one group for each value of α.

## 4.3. Auction Details

At the beginning of a match, each participant j submitted a bid b<sup>j</sup> at no cost. Participants could then revise their bids in continuous time during the match. Participants could lock the bids to see the associated outcome and payoff with the current combination of bids. Specifically, if a participant’s bid, b<sup>j</sup>, was the highest (i.e., j → (1)), then the participant would get the first good and pay the amount equal to the second-highest bid

Table 4. Treatments Summary

<table><tr><td>Treatments</td><td>Parameter varied</td><td>Description</td></tr><tr><td>Between – Subjects</td><td> $C \in \{0.0, 0.1\}$ </td><td>Costless or costly bid adjustment within matches</td></tr><tr><td>Within – Subjects</td><td> $\alpha \in \{0.2, 0.5, 0.8\}$ </td><td>Value of the second good as a fraction of the first good</td></tr></table>

Value of good 2 is determined by multiplying 0.5 and value of good 1 (rounded to the nearest 0.1)

![](/api/attachments/VU6759EP/fulltext/images/2c2eeb962e76b0b6841e8c2f393baa2c862adbdc04d7e223bcec17ec5e5720d2.jpg)

minus the friction cost incurred during the match, $( v ^ { ( 1 ) }$ $- b ^ { ( 2 ) } ) - C ^ { ( 1 ) } . ^ { 1 7 }$ If the participant’s bid was the second highest, then the participant would get the second good and pay the amount equal to the third-highest bid times α minus the friction cost incurred during the match, that is, $\alpha ( v ^ { ( 2 ) } - b ^ { ( 3 ) } ) - C ^ { ( 2 ) }$ . If the participant’s bid was the lowest, the participant would not receive any good and would pay only the friction cost incurred. We announced that α would be the same for all participants in the group during the instructions and had a reminder on the screen to ensure its common knowledge.

## 4.4. Experimental Interface

The experiment was conducted using an interface programmed by the authors. The interface implements the continuous-time feature of the auction with participants being able to make bid adjustments in real time. Figure 2 presents the screenshot of the interface. The participant’s screen summarized information provided for that match (#1 in Figure 2) as well as the current action and the outcome associated with this action (#2 in Figure 2). To place or revise the bid, participants had to use the scale displayed on the left side of the screen (#3 in Figure 2).

Our design can be viewed as an infinite sequence of auctions in which bidders commit to a bid for each auction. Each second, the auction could end, which means that each bid carries an expected profit/loss. However, the actual compensation in each match is based on the last auction in a sequence. The incentive compatibility of this compensation mechanism is established by Chandrasekhar and Xandri (2022, p. 1): “Paying participants for the last (randomly occurring) round robustly implements the predicted outcomes for any infinite horizon dynamic game.” We summarize this design choice with Remark 3.

Remark 3. We used a last (randomly occurring) period compensation mechanism.

We anticipated a potential problem involving mouse clicks. Specifically, mouse clicks could be used as a source of additional information about the behavior of other participants in this experiment. For example, a bid adjustment by subject i, if heard by subject j, could lead to subject j trying to check whether new profitable adjustments were available by making one or more adjustments, which, in turn, could lead to many more clicks. This issue is particularly relevant because such exploration is central to the mechanism that we are proposing and, as described earlier, is one of the key differences between the treatments for which we were looking; therefore, comparing sessions that contained a large number of clicks (which could be clearly heard in the room) with sessions that did not could be problematic. To resolve this issue, we implemented a silent protocol. Specifically, instead of clicking to select a new bid, subjects placed and adjusted their bids by moving

Figure 2. (Color online) Experimental Interface

To revise your bid, use the scale above

Notes. The screenshot shows the following: (1) Match information. This information is provided prior to the beginning of the match. (2) Action and the outcome associated with this action. The outcomes are updated live and depend on the actions of all three participants in the group. (3) Scale that is used to place and revise bids. (4) Scales for the other two participants. These scales remain blank until the match is over, at which point the actions of the other participants are revealed. (5) Reminders about the rules of the experiment.

the mouse back and forth across the scale border. This approach resulted in a quiet room throughout the experiment. Thus, subjects could not detect bid changes other than through the information provided on the screen.<sup>18</sup> We summarize this design choice with Remark 4.

Remark 4. We used a silent protocol.

## 4.5. Experiment Administration

For the experiment, we recruited 138 participants using ORSEE software (Greiner 2015) on the campus of Purdue University. We administered eight sessions of the experiment with 15–18 participants in each session.<sup>19</sup> Upon entering the laboratory, participants were assigned to a computer terminal. All terminals were separated by physical barriers such that participants could not see choices made by other participants in the room. Participants remained anonymous throughout the experiment.

To ensure that subjects understood the interface and the bid-adjustment process, we took several steps. First, subjects received a handout containing the instructions (Online Appendix L). An experimenter read them out loud to ensure common knowledge of the environment. Second, subjects had to complete six practice tasks that dealt with placing and modifying the bid. Subjects could proceed to the next task only after correctly completing the previous task. Third, the subjects had to go through five examples, which, to eliminate any bias, were generated at random. In the examples, subjects could practice placing and revising their bids for hypothetical actions by the opponents. Finally, subjects were provided with a calculator, pen, and paper for the duration of the instructions and the experiment. Thus, they were able to verify calculations in the instructions and practice tasks. Furthermore, subjects could make any necessary calculations during the experiment.

These steps took approximately 20 minutes. Then, prior to each match, subjects were given time to review information for that match. Only after they were ready did they place their initial bids. Once everyone placed the initial bid, the match began. The 10 matches took approximately 30 minutes to complete, after which subjects were paid in cash.

## 4.6. Experimental Results

In this section, we present results from our main experiments. We maintain the order of the presentation and begin with the analysis of exploratory behavior in Section 4.6.1, followed by the analysis of the bid-to-value ratio in Section 4.6.2, and conclude with the analysis of allocative efficiency in Section 4.6.3.

4.6.1. Exploratory Behavior. Table 5 presents the average number of bid adjustments made in each treatment (with bootstrapped standard errors in parentheses). In particular, given our design, we focus on matches 5–10. The table is split into three panels based on the rank of the private value of the participant, similar to the simulation results in Section 3.3. That is, the participant with the highest private value among the three is labeled as the highest valued, the participant with the secondhighest private value among the three is labeled as the medium valued, and the participant with the lowest private value among the three is labeled as the lowest valued. The columns within each panel vary the costs of bid adjustments. The rows vary the similarity of the two slots.

Table 5. Subject Bid Adjustments

<table><tr><td rowspan="2"></td><td colspan="3">(a) Highest-valued</td><td colspan="3">(b) Medium-valued</td><td colspan="3">(c) Lowest-valued</td></tr><tr><td colspan="2">C = 0.0</td><td>C = 0.1</td><td colspan="2">C = 0.0</td><td>C = 0.1</td><td colspan="2">C = 0.0</td><td>C = 0.1</td></tr><tr><td rowspan="2"> $\alpha = 0.2$ </td><td>31.125(5.002)</td><td>0.0 $\gg$ </td><td>3.438(0.76)</td><td>51.292(5.324)</td><td>0.0 $\gg$ </td><td>3.458(0.454)</td><td>65.583(8.988)</td><td>0.0 $\gg$ </td><td>3.083(0.525)</td></tr><tr><td>0.657</td><td></td><td>0.45</td><td>0.084</td><td></td><td>0.596</td><td>0.204</td><td></td><td>0.583</td></tr><tr><td rowspan="2"> $\alpha = 0.5$ </td><td>34.167(4.238)</td><td>0.0 $\gg$ </td><td>2.667(0.279)</td><td>38.646(4.77)</td><td>0.0 $\gg$ </td><td>3.125(0.359)</td><td>51.583(6.065)</td><td>0.0 $\gg$ </td><td>2.708(0.349)</td></tr><tr><td>0.74</td><td></td><td>0.044</td><td>0.053</td><td></td><td>0.327</td><td>0.938</td><td></td><td>0.346</td></tr><tr><td rowspan="2"> $\alpha = 0.8$ </td><td>36.857(6.744)</td><td>0.0 $\gg$ </td><td>1.929(0.221)</td><td>26.69(3.372)</td><td>0.0 $\gg$ </td><td>2.571(0.329)</td><td>52.333(6.996)</td><td>0.0 $\gg$ </td><td>4.024(1.222)</td></tr><tr><td>0.503</td><td></td><td>0.029</td><td>0.0</td><td></td><td>0.135</td><td>0.266</td><td></td><td>0.536</td></tr><tr><td> $\alpha = 0.2$ </td><td>31.125(5.002)</td><td></td><td>3.438(0.76)</td><td>51.292(5.324)</td><td></td><td>3.458(0.454)</td><td>65.583(8.988)</td><td></td><td>3.083(0.525)</td></tr><tr><td>Average</td><td>33.928(3.076)</td><td>0.0 $\gg$ </td><td>2.71(0.29)</td><td>39.406(2.793)</td><td>0.0 $\gg$ </td><td>3.072(0.224)</td><td>56.681(4.37)</td><td>0.0 $\gg$ </td><td>3.239(0.435)</td></tr></table>

Notes. Panel (a) presents the average number of bid adjustments made by the highest valued participants in each group. Panel (b) presents the average number of bid adjustments made by the medium valued participants in each group. Panel (c) presents the average number of bid adjustments made by the lowest valued participants in each group. The unit of observation is a subject per match. Bootstrapped standard errors are in parentheses. > , ≫, and ⋙ denote significance at the 0.10, 0.05, and 0.01 level, respectively. p-values are determined using two-tailed permutation tests (Good 2013).

Table 6. Subject Bid-to-Value Ratios

<table><tr><td rowspan="2"></td><td colspan="3">(a) Highest-valued</td><td colspan="3">(b) Medium-valued</td><td colspan="3">(c) Lowest-valued</td></tr><tr><td colspan="2">C = 0.0</td><td>C = 0.1</td><td colspan="2">C = 0.0</td><td>C = 0.1</td><td colspan="2">C = 0.0</td><td>C = 0.1</td></tr><tr><td rowspan="2">α = 0.2</td><td>0.952(0.032)</td><td>0.209~</td><td>0.901(0.025)</td><td>0.951(0.037)</td><td>0.453~</td><td>0.913(0.031)</td><td>2.826(0.377)</td><td>0.003≫</td><td>1.668(0.191)</td></tr><tr><td>∀0.018</td><td></td><td>∀0.011</td><td>∀0.605</td><td></td><td>2.85</td><td>2.372</td><td></td><td>2.194</td></tr><tr><td rowspan="2">α = 0.5</td><td>0.839(0.033)</td><td>0.316~</td><td>0.793(0.032)</td><td>0.92(0.044)</td><td>0.329~</td><td>0.863(0.034)</td><td>3.815(0.889)</td><td>0.0≫</td><td>1.341(0.155)</td></tr><tr><td>∀0.041</td><td></td><td>2.209</td><td>∀0.003</td><td></td><td>2.192</td><td>2.307</td><td></td><td>2.802</td></tr><tr><td rowspan="2">α = 0.8</td><td>0.725(0.044)</td><td>0.942~</td><td>0.729(0.039)</td><td>0.734(0.045)</td><td>0.39~</td><td>0.789(0.044)</td><td>2.646(0.61)</td><td>0.006≫</td><td>1.284(0.153)</td></tr><tr><td>∀0.0</td><td></td><td>∀0.0</td><td>∀0.0</td><td></td><td>2.023</td><td>2.816</td><td></td><td>2.13</td></tr><tr><td>α = 0.2</td><td>0.952(0.032)</td><td></td><td>0.901(0.025)</td><td>0.951(0.037)</td><td></td><td>0.913(0.031)</td><td>2.826(0.377)</td><td></td><td>1.668(0.191)</td></tr><tr><td>Average</td><td>0.844(0.023)</td><td>0.283~</td><td>0.811(0.019)</td><td>0.874(0.026)</td><td>0.635~</td><td>0.858(0.021)</td><td>3.115(0.387)</td><td>0.0≫</td><td>1.438(0.097)</td></tr></table>

Notes. Panel (a) presents the average bid-to-value ratio per match across subjects with the highest private value in each group. Panel (b) presents the average bid-to-value ratio per match across subjects with the second highest private value in each group. Panel (c) presents the average bid to-value ratio per match across subjects with the lowest private value in each group. The unit of observation is a subject per match. Bootstrapped standard errors are in parentheses. > , ≫, and ⋙ denote significance at the 0.10, 0.05, and 0.01 level, respectively. p-values are determined using two-tailed permutation tests (Good 2013).

We find that the number of bid adjustments in the C � 0.0 treatment is an order of magnitude greater than in the $C = 0 . 1$ treatment. Consistent with Result 1, we find that lower costs lead to more exploration in the GSP auction. We also observe that the lowest valued agents explore more than the medium and highest valued agents. We summarize these observations with Result 6.

Result 6. Lower costs lead to more exploration.

4.6.2. Bid-to-Value Ratios. Table 6 presents the average bid-to-value ratios in each treatment. We highlight three main results. First, comparing panels (a)–(c), we find that the lowest valued participants substantially overbid compared with the other participants. This finding is consistent with Result 2.

Result 7. The bid-to-value ratio is higher for lower valued agents.

Second, by comparing columns C � 0.0 and $C = 0 . 1$ from panel (c), we find that the bid-to-value ratio for the lowest valued participants is significantly higher when frictions are absent. This finding is consistent with Result 3.

Result 8. For the lowest valued agents, the bid-to-value ratio increases as friction decreases.

Finally, for the bid-to-value ratios across the different values of $\alpha ,$ we find partial support for Result 4. In particular, for four (out of six) cases, the bid-to-value ratios for $\alpha = 0 . 2$ are significantly higher than for $\alpha = 0 . 8 ,$ which is consistent with Result 4; for the other two cases, the differences are directionally consistent but are not significant. Note that both cases correspond to the lower valued agents. This finding could be a result of outliers, such as when the private values are very low but the agents overbid by a small amount, which translates into large bid-to-value ratio.

Result 9. The bid-to-value ratio decreases as α increases for medium and highest valued agents.

4.6.3. Allocative Efficiency. Table 7 presents the allocative efficiency in our experiment. Recall that we focus on the outcomes in matches 5–10 to eliminate concerns about initial learning about the environment by the human subjects.<sup>20</sup> In addition, for each match m ∈ $\{ { \bar { 5 } } , \dots , 1 0 \}$ , private values across groups in sessions 1–4 and 5–8 were the same, allowing for a clean comparison across treatments.

Table 7 shows that allocative efficiency is significantly higher when the costs are $C = 0 . 1$ . This result is consistent with Result 5 and leads to the conclusion that frictions in the GSP market can help improve efficiency and, therefore, overall social welfare.

Result 10. Allocative efficiency of the market increases as friction costs increase.

To summarize the computational and experimental results, we find behavior by the lowest valued participant (as captured by the number of bid adjustments and bidto-value ratios) is key to the outcomes of the GSP. As presented in Tables 5 and $^ { 6 , }$ in the presence of frictions, the agents rarely explore and experiment with higher bidding strategies. However, in the absence of friction costs, the exploration increases substantially. The exploratory behavior manifests in the form of substantial overbidding by the lowest valued participants (as presented in Table 6). Such overbidding further impacts the higher valued agents by either pushing them to increase their bids or stay put and be less likely to win the auction, which, in turn, may lead to an inefficient allocation.

Table 7. GSP Efficiency

<table><tr><td></td><td>C = 0.0</td><td></td><td>C = 0.1</td></tr><tr><td> $\alpha = 0.2$ </td><td>0.926(0.021) $^{0.84}$ </td><td> $^{0.113}$ </td><td>0.967(0.014) $^{0.196}$ </td></tr><tr><td> $\alpha = 0.5$ </td><td>0.93(0.023) $^{0.204}$ </td><td> $^{0.016}$ </td><td>0.987(0.005) $^{0.912}$ </td></tr><tr><td> $\alpha = 0.8$ </td><td>0.967(0.014) $^{0.132}$ </td><td> $^{0.184}$ </td><td>0.988(0.007) $^{0.259}$ </td></tr><tr><td> $\alpha = 0.2$ </td><td>0.926(0.021)</td><td></td><td>0.967(0.015)</td></tr><tr><td>Average:</td><td>0.94(0.012)</td><td> $^{0.001}$ </td><td>0.98(0.006)</td></tr></table>

Notes. Average allocative efficiency for the last bid that subjects placed in each match. Unit of observation is a group of three subjects. Bootstrapped standard errors are in parentheses. > , ≫, and ⋙ denote significance at the 0.10, 0.05, and 0.01 level, respectively. p-values are determined using two-tailed permutation tests (Good 2013).

## 5. Experiment to Study the Underlying Mechanism

Our previous analysis indicates that the agents use the bidding process to explore and learn, and this exploration decreases the allocative efficiency. To further strengthen our understanding of the underlying mechanism, we designed and conducted an alternative experiment. In this new experiment, we ask what happens to the bidders’ behavior and allocative efficiency if the information needed for learning is made available by design. In addition, when conducting this experiment, we also evaluated the robustness of our main results to the experimental design.

One could claim the following features of our experimental design encourage excessive exploration for $C =$ 0.0. First, subjects make bid adjustments in continuous time. Second, upon a bid adjustment, subjects obtain immediate feedback. Third, the only way to evaluate the consequence of a new bid is to adjust the bid. That is, without actively changing your own bid, assessing how bids would have performed isn’t possible. Because of these three features, bidders carry out “instantaneous” checks of various bids, and thus, our results may be an artifact of these choices. To address these concerns and facilitate the understanding of the underlying mechanism, we run a new set of experiments in which we consider a discrete-time setting and introduce an additional option to purchase information regarding counterfactual outcomes. Specifically, the information consisted of an interactive plot (see screenshots in Online Appendix N.2) that displayed possible payoffs for any bid conditional on the other two group members holding the bids as they did in the previous period. The treatment variation included the cost of accessing this plot. Specifically, in the costly information treatment, subjects incurred a cost of \$0:5 every period in which they accessed this information, whereas in the free information treatment, subjects did not incur any cost.

Regarding the design for new experiments, we implemented a 2 × 2 factorial design in which we varied the cost of bid adjustment (as is the main treatment variation in the original set of experiment) and the cost of the information. For all four treatments, we fixed the same α � :5. The differences from the original experiments include (i) discrete-time setup, (ii) duration of the interaction, (iii) multiple duration realizations, and (iv) independent random draws for each subject in each match. Specifically, in the discrete-time setting, subjects faced an uncertain number of decision periods. Within each period, they had unlimited time to make a desired bid adjustment (if any). Once all participants in their group submitted their decisions, each saw the outcome for that period. Although the original set of experiments could be thought of as 120 one-second periods in expectation, subjects could not stop the progress of the interaction or take the time to think more carefully about their bid revision. To make the discrete-time setup feasible within the time constraints offered by the laboratory experiment, we reduced the number of expected interactions to 10 (i.e., probability of termination was 0.1 instead of 0.01). In addition, to ensure that one specific sequence of match durations did not bias the results, we now consider four sequences of supergame length (see Online Table N.1). Finally, to ensure that one particular combination of privately drawn values did not influence the results, we did not fix or match the private values in the new experiment. Instead, private values were drawn at random at the beginning of each match for each participant.

Our goal with the new treatment dimension (free versus costly information) was twofold. First, similar to Cooper and Fang (2008), we set out to understand the relationship between information acquisition and overbidding. Specifically, by allowing subjects to observe all possible counterfactual payoffs in the free information treatment, we reduced the need to actively explore to acquire information about the profitability of alternative actions. Second, we set out to test whether costly bid adjustments improve the allocative efficiency independent of the information component.

Table 8. Subject Bid Adjustments

<table><tr><td rowspan="2"></td><td colspan="3">Highest-valued</td><td colspan="3">Medium-valued</td><td colspan="3">Lowest-valued</td></tr><tr><td>C = 0.0</td><td></td><td>C = 0.1</td><td>C = 0.0</td><td></td><td>C = 0.1</td><td>C = 0.0</td><td></td><td>C = 0.1</td></tr><tr><td>NoInfoCosts</td><td>2.903(0.341)</td><td>0.0 $\gg$ </td><td>0.732(0.133)</td><td>3.484(0.397)</td><td>0.0 $\gg$ </td><td>1.211(0.199)</td><td>2.935(0.371)</td><td>0.003 $\gg$ </td><td>1.493(0.301)</td></tr><tr><td>InfoCosts</td><td>3.442(0.374)</td><td>0.0 $\gg$ </td><td>1.519(0.294)</td><td>5.273(0.527)</td><td>0.0 $\gg$ </td><td>1.659(0.242)</td><td>5.156(0.545)</td><td>0.0 $\gg$ </td><td>2.134(0.281)</td></tr><tr><td>Average:</td><td>3.201(0.258)</td><td>0.0 $\gg$ </td><td>1.511(0.173)</td><td>4.475(0.352)</td><td>0.0 $\gg$ </td><td>1.451(0.159)</td><td>4.165(0.358)</td><td>0.0 $\gg$ </td><td>1.837(0.208)</td></tr></table>

Notes. Panel (a) presents the average number of bid adjustments made by the highest valued participants in each group. Panel (b) presents the average number of bid adjustments made by the medium valued participants in each group. Panel (c) presents the average number of bid adjustments made by the lowest valued participants in each group. The unit of observation is a subject per match. Bootstrapped standard error are in parentheses. > , ≫, and ⋙ denote significance at the 0.10, 0.05, and 0.01 level, respectively. p-values are determined using two-tailed permutation tests (Good 2013).

For the new experiments, we recruited 183 participants on the campus of Purdue University who had not participated in the original set of experiments. The new experiment was programmed in oTree software (Chen et al. 2016a). Instructions and decision screens are presented in Online Appendix N.1. Next, we present results of the new experiments. We opt to keep the same order of presentation and analysis and start with the evidence of exploratory behavior. Table 8 presents the average number of bid adjustments made in each of the four treatments in the second half of the experiment. As before, the table is split into three panels based on the rank of the private value of the participant.

Consistent with the computational simulations and original experiments, we find the number of bid adjustments is significantly greater when C � 0.0 than when C � 0.1. We also find that when information costs are present, the number of bid adjustments is significantly greater than when the information is free. These results are consistent with our expectation that some of the bid adjustments serve to gather information regarding potential profitability of alternative bids.

Next, we consider the bid-to-value ratios (Table 9). Again, consistent with the agent-based simulations and the original set of experiments, we find the lowest valued agents tend to have the highest bid-to-value ratio, and in the case of costly information but no bid-adjustment costs, they significantly overbid. These results indicate that the exploration noted earlier is often done in the overbidding domain. When the information costs are present, bid-adjustment costs tend to substantially mitigate the overbidding as in Section 4.6.2.

Finally, we turn to the allocative efficiency (Table 10). We find that, across both the free and costlyinformation treatments, bid adjustments tend to improve the allocative efficiency of the GSP. Although the results for C � 0.0 and 0.1 for the costly information treatment are expected based on our original experiments, we also find that, even when the counterfactual information is free, some amount of bid-adjustment frictions lead to higher allocative efficiency, albeit at a weaker level of significance. These findings indicate that, although overbidding is associated with inefficiency, the original cause is the exploratory behavior. When the information about the negative consequences of overbidding is readily available, subjects still may explore, which, in the context of the highly dynamic and interdependent environment, such as the GSP, may lead to inefficient 21 outcomes.

Table 9. Subject Bid-to-Value Ratios

<table><tr><td rowspan="2"></td><td colspan="3">Highest-valued</td><td colspan="3">Medium-valued</td><td colspan="3">Lowest-valued</td></tr><tr><td>C = 0.0</td><td></td><td>C = 0.1</td><td>C = 0.0</td><td></td><td>C = 0.1</td><td>C = 0.0</td><td></td><td>C = 0.1</td></tr><tr><td>NoInfoCosts</td><td>0.741(0.038)</td><td> $^{0.107}_{\sim}$ </td><td>0.841(0.046)</td><td>0.821(0.049)</td><td> $^{0.547}_{\sim}$ </td><td>0.877(0.068)</td><td>1.336(0.187)</td><td> $^{0.738}_{\sim}$ </td><td>1.519(0.375)</td></tr><tr><td>InfoCosts</td><td>0.727(0.03)</td><td> $^{0.321}_{\sim}$ </td><td>0.771(0.032)</td><td>0.828(0.034)</td><td> $^{0.123}_{\sim}$ </td><td>1.002(0.101)</td><td>2.148(0.58)</td><td> $^{0.028}_{\gg}$ </td><td>1.103(0.124)</td></tr><tr><td>Average:</td><td>0.733(0.024)</td><td> $^{0.056}_{<}$ </td><td>0.804(0.027)</td><td>0.825(0.028)</td><td> $^{0.101}_{\sim}$ </td><td>0.944(0.063)</td><td>1.784(0.333)</td><td> $^{0.211}_{\sim}$ </td><td>1.297(0.193)</td></tr></table>

Notes. Panel (a) presents the average bid-to-value ratio per match across subjects with the highest private value in each group. Panel (b) presents the average bid-to-value ratio per match across subjects with the second highest private value in each group. Panel (c) presents the average bid to-value ratio per match across subjects with the lowest private value in each group. The unit of observation is a subject per match. Bootstrapped standard errors are in parentheses. > , ≫, and ⋙ denote significance at the 0.10, 0.05, and 0.01 level, respectively. p-values are determined using two-tailed permutation tests (Good 2013).

Table 10. GSP Efficiency

<table><tr><td rowspan="2"></td><td colspan="3">Bid adjustment costs</td></tr><tr><td>C = 0.0</td><td></td><td>C = 0.1</td></tr><tr><td rowspan="2">NoInfoCosts</td><td>0.96</td><td> $^{0.06}$ </td><td>0.982</td></tr><tr><td>(0.01)</td><td></td><td>(0.006)</td></tr><tr><td rowspan="2">InfoCosts</td><td>0.943</td><td> $^{0.048}$ </td><td>0.968</td></tr><tr><td>(0.011)</td><td></td><td>(0.006)</td></tr><tr><td rowspan="2">Average:</td><td>0.951</td><td> $^{0.005}$ </td><td>0.975</td></tr><tr><td>(0.008)</td><td></td><td>(0.004)</td></tr></table>

Notes. Average allocative efficiency for the last bid that subjects placed in each match of the second half of the experiment. Unit of observation is a group of three subjects. Bootstrapped standard errors are in parentheses. > , ≫, and ⋙ denote significance at the 0.10, 0.05, and 0.01 level, respectively. p-values are determined using two-tailed permutation tests (Good 2013).

To summarize, we ran additional experiments to achieve two goals. First, we explored the robustness of our experimental results to various design choices that we made. Second, our design allowed us to isolate some of the reason subjects overbid. Across the new experiments, we find results that are remarkably consistent with the initial set of experiments. In particular, the allocative efficiency of the auction is higher in the presence of bid-adjustment costs. The new experiments highlight the importance of exploration and learning by the subjects in a highly interdependent environment of the GSP, and the frictions tend to dampen excessive exploration.

## 6. Additional Insights

In addition to the second human-subject experiment, we conduct two computational studies using the agentbased model calibrated to the data.<sup>22</sup> The two simulations provide further evidence on the mechanism underlying the main result of the paper.

First, it is not immediately obvious that the behavior of the lowest valued agents leads to market inefficiency. After all, the lowest valued agent can overbid but still not win any slots. To check the extent to which overbidding by the lowest valued agents influences allocative efficiency, we conduct a computational experiment in which we explicitly restrict the lowest valued agents from overbidding. More concretely, we consider the case of $\alpha = 0 . 5 ,$ ${ \cal C } = 0 . { \bar { 5 , } } J = 3 ,$ , and K � 2 and restrict $b ^ { 3 } \leq v ^ { 3 }$ . We find that the restriction improves the allocative efficiency of the auction from 0.951 to 0.958. Although this improvement may not seem large, it actually accounts for approximately 5% of the relevant range.<sup>23</sup> The improvement in allocative efficiency is consistent with the improvement observed in the free information treatments of the new experiment (which was also associated with the reduction in overbidding by the lowest valued agents).

Second, we consider what happens to the bid-to-value ratios and allocative efficiency if the number of lowvalued advertisers increases. Such an increase could happen if, for example, the entry cost is lowered and a new set of low-valued advertisers enters the market. According to the theory of Edelman et al. (2007), an increase in low-valued advertisers should not affect the bidding behavior or efficiency of the auctions because the nonwinning participants submit their values and do not win. However, if, as we show empirically, the lowest valued advertisers are likely to overbid, an increase in the number of lowest valued advertisers might further affect our auction metrics. To add more specifics, we hold α � 0:5, C � 0.5, and K � 2 and vary $J \in \{ 3 , 4 , 5 , 6 \}$ Importantly, we retain the same valuation for the top two advertisers and restrict values of advertiser j to be less than $v ^ { j } \leq v ^ { 3 } \forall j > 3$ . Thus, although participation costs and the entry decision are not explicitly modeled, we can shed new light on what happens as participation costs decrease.

Figure 3 presents the efficiency and bid-to-value ratios when we vary the number of advertisers from three to six. We find the following: as the number of advertisers increases, (i) the efficiency of the auction decreases (panel (a) of Figure 3), (ii) the lowest valued agents overbid (panel (a) of Figure 3), and (iii) the overbidding by the low-valued agents cascades into bids by the firstand second-highest valued advertisers. Importantly, the main result of our paper—allocative efficiency increases with an increase in friction costs—holds across different market sizes. Note that these results regarding the additional agents in the market indicate that allocative efficiency does not change linearly.

The two analyses in this section provide valuable insights regarding the mechanism that determines allocative efficiency of the GSP auction. In particular, the key contribution is that we calibrated the machine learning model using the human-subject experiments and then used the calibrated model to provide additional insights. We are unaware of any prior work in the IS area that demonstrates the similarity in behaviors between computational and experimental agents. Building on these simulations, we conduct several additional simulation exercises in the online appendix. In particular, we consider an increase in the supply of ad slots by the platform, which can help resolve the overbidding even if the extra slots are not of high value. Across all of the scenarios, we find that bid-adjustment friction costs play a consistent role in determining allocative efficiency of the GSP auction. Specifically, allocative efficiency with costs is generally higher than without costs.

## 7. Conclusion

In this research, we investigate the role of frictions fo GSP outcomes. First, we used Q-learning-based agents to computationally replicate the GSP environment. We then used the same environment to run an economic experiment with human subjects. In both cases, we find that agents with the lowest private valuations are the most likely to explore their bidding strategies in the overbidding domain, contradicting the assumption made in the theory of GSP. The excessive exploration, which hinders the market’s ability to discover the optimal allocation, can be moderated with bid-adjustment frictions. In other words, we demonstrate systematically, using both the computational and human-subject experiments, that reducing frictions in highly interdependent markets, such as GSP, does not necessarily translate into improving social welfare. Thus, we should be cognizant of the potential impact of reducing frictions associated with technological advances.

Figure 3. (Color online) Increasing Number of Advertisers  
(a)  
![](/api/attachments/VU6759EP/fulltext/images/01b5285490dbed06b9c43e5baceaa40a71dee99af8edbabb5bbf5af06010cf8b.jpg)

(b)  
![](/api/attachments/VU6759EP/fulltext/images/d5a3d99d467dfd05fc7b87619145d956e4766f616c56e4cda7000e6ce4a910da.jpg)  
3 Agents 4 Agents 5 Agents 6 Agents  
Notes. (a) Allocative efficiency. (b) Bid-to-value ratios. The simulation results are for $\alpha = 0 . 5$ and K � 2 ad slots. Values for δ and λ ar calibrated from the experiment data to be 0.05 and 0.9, respectively. Because the experiment does not have a scenario with c � 0.1, we us the parameters calibrated for c � 0. Private values of the first, second, and third highest valued agents are held the same. Private values for the remaining agents are restricted to be at most the value of the third highest valued agent. For the bid-to-value-ratio simulation, the bid-adjustment cost is set to C � 0.5.

Our research is not without limitations. In particular, we consider a simplified version of the GSP in which the rank is determined solely by the advertiser’s bid. In recent years, however, sponsored-search-advertising platforms have started to include other factors (e.g., ad quality and advertiser’s history) to determine the rank of the bid. Future research could incorporate these factors and ranking methods to understand the properties of the new auction mechanisms.<sup>24</sup> The second limitation is that, in this paper, we assume all advertisers face the same cost for bid adjustments. In practice, however, vast heterogeneity exists among advertisers in terms of costs they incur for both participating in the market and making bid adjustments. Our agent-based model and experiments can be adapted to account for cost heterogeneity by, for example, randomly drawing agentspecific costs. Furthermore, additional costs may be incurred at the point of running decision models before adjustments are made. Although our additional experiments shed light on the potential impact of the modelevaluation step, future work should explore this topic in more detail. The third limitation is that, in ou research, we consider two end points of the spectrum: either computational agents make all the decisions or human agents make all decisions. Future research could extend our work to scenarios in which agents choose among a set of AI tools that make bids for them. In particular, developing mechanisms that are robust to the presence of both types of bidders in the market is important. Finally, in this paper, we primarily focus on the role of friction (bid-adjustment cost) in the context of online ad markets. More broadly, understanding the role of friction in other types of online marketplaces (e.g., e-commerce, dating, ride sharing) is important.

## Acknowledgments

The authors thank the editor, Ahmed Abbasi; associate editor, Idris Adjerid; and three anonymous referees for providing many useful comments and suggestions that improved the paper. This paper also benefited from comments by participants at the 2018 Conference on Information Systems and Technology, Phoenix; 2018 Statistical Challenges in Electronic Commerce Research, Rotterdam; 2018 Workshop on Experimental and Behavioral Econom ics In Information Systems, Arlington; 2019 Barcelona School of Economic’s Workshop on Computational and Experimental Economics; 2019 Economic Science Association World Meetings; 2019 INFORMS Annual Conference, Seattle; 2019 Workshop on Information Technology Systems Munich; and seminar participants at Purdue University, McGill University, Michigan State University, Indian

School of Business, and The University of Texas at Dallas. Authors are listed in alphabetical order of last name.

## Endnotes

<sup>1</sup> For example, in a practitioner-oriented article, Dudharejia (2018) outlines ways to optimize AdWords campaigns. Among them is “recognizing changes in the bidding landscape,” which implicitly places a value on exploration over the whole range of bidding values.

<sup>2</sup> Q-learning is extensively used in machine learning and deep learning applications, including Google’s Deepmind solving AlphaGo.

${ } ^ { 3 } \operatorname { I f } J < K ,$ every advertiser wins the auction. In general, these markets, even the niche ones, tend to have more advertisers than ad slots.

<sup>4</sup> In Online Appendix C.3, we show that the computational predictions also hold for the exponential distribution.

<sup>5</sup> Note that search engines have evolved to calculate a quality score based on the previous performance of the ads and the bid amount placed by the advertiser. These quality scores are used to determine the slot to be assigned to the advertiser. In the main paper, we consider a simplified case in which the slot allocation is based only on bids. In Online Section E.1, we extend our model to include the quality of the ad in the allocation decision.

<sup>6</sup> For ease of notation, we assume $b ^ { ( K + 1 ) } = 0 .$

<sup>7</sup> Anecdotally, ads in the higher slots tend to receive more clicks, making them more attractive to advertisers.

$^ { 8 } \mathrm { I n }$ the constructed equilibrium, the second advertiser submits a bid satisfying the following condition: $\alpha ( v ^ { 2 } - b ^ { 3 } ) = v ^ { 2 } - b ^ { 2 }$ . By assuming $b ^ { 3 } = v ^ { 3 }$ (as is done for their equilibrium derivation), we obtain $\begin{array} { r } { \frac { b ^ { 2 } } { v ^ { 2 } } = 1 + \alpha \Big ( \frac { v ^ { 3 } } { v ^ { 2 } } - 1 \Big ) } \end{array}$ , where $\textstyle \frac { v ^ { 3 } } { v ^ { 2 } } < 1$ by construction.

<sup>9</sup> We chose the Q-learning with Boltzmann distribution for two main reasons. First, it is the most common implementation of the model (Gao and Pavel 2017). Second, the Boltzman distribution has a close link to the logit model used to explain data from humansubject experiments. In Online Appendix B.4, we also consider the ɛ-greedy approach to operationalize exploration–exploitation, similar to Wu et al. (2018).

<sup>10</sup> The parameter λ is often used to capture the degree of bounded rationality in stochastic choice models (e.g., Chen et al. 2012).

<sup>11</sup> Note that uniform distribution is only a starting point. Starting with an alternate distribution, such as normal distribution, only leads to a faster convergence in terms of the learning. Our approach of using a uniform distribution initially is, therefore, conservative.

<sup>12</sup> In Online Appendix $C ,$ we consider two alternative, more complex state-space specifications. In particular, in Online Section C.1, the state space includes the private valuation and the allocation in the previous period, and in Online Section C.2, the state space includes the private valuation and the previous bid placed by the agent. In both cases, the main predictions presented in Section 3.3 hold.

<sup>13</sup> For example, if the three participants were assigned private values of $7 , 4 ,$ and $^ { 2 , }$ then the participant with the private value of 7 is considered the highest valued, the participant with the private value of 4 is considered the medium valued, and the participant with the private value of 2 is considered the lowest valued.

<sup>14</sup> The relatively slow learning process is a well-known artifact of basic reinforcement-learning models. One way to speed up the learning is to include indirect learning via simulated experience as in Rosokha and Younge (2020). Another is to use generalization as in Romero and Rosokha (2019).

<sup>15</sup> Note the economic significance of an increase of 1% should be considered in the context of 15% (� 100%�85%). That is, the relevant range for learning is beyond the average allocative efficiency when agents bid randomly. In addition, given the large size of the potential market $( \mathrm { e . g . , }$ a market for online ads is of the order of 100 billion USD), the impact could be very large.

<sup>16</sup> Online Table M.1 presents the match duration for each of the 10 matches.

<sup>17</sup> Recall that $\alpha _ { 1 } = 1 .$

<sup>18</sup> The experimental laboratory was set up with dividers so that each participant could see only the participant’s own desk and monitor. And, although participants may have had a periphera view of their neighbor, the bid adjustments could be carried out with minimal mouse movements that were hardly noticeable.

19 After running the first four sessions (two for $C = 0 . 0$ and two for $C = 1 . 0 )$ , we discovered an error in the way the software generated random seeds (recall that the seeds were used in the generation of common values across the groups in matches 5–10). The error was that, for matches 5–10, the seed was incremented by one rather than three. So, for each group in period $t + 1 ,$ , two values were the sam as in period $t ,$ and one value was new (instead of three). The values were then randomly reassigned within the group. Therefore, the chance of a given subject having the same value in two consecutiv matches was approximately 20%, and the chance of a subject having the same value in matches t and $t + 2$ was approximately 10%. The bug was the same across the treatments, so in terms of a comparison of $C = 0 . 0$ with $C = 1 . 0$ or across $\alpha ^ { \prime } \mathbf { s } ,$ no systematic effect should exist between treatments. For the results, however, this error mean that subjects had more learning opportunities about the same values, which makes our findings about excessive experimentation and overbidding conservative. We present the data broken down by the first and last four sessions in Online Appendix M. As expected, we find the results obtained using data from sessions 1–4 to be consistent with results obtained using data from sessions 5–8.

<sup>20</sup> For robustness, instead of focusing on the last six matches, we run the same analysis for the last three matches. We present these results in Online Appendix M. We find that the results for the last three matches are consistent with findings presented in Online Tables M.5–M.7.

<sup>21</sup> Results from our second set of experiments may be interpreted from the perspective of the model-evaluation and estimation costs. In particular, before changing the bid, the bidder may run analyses to estimate what the best bid should be (obtaining results equiva lent to the information available for purchase in the new treatments). Alternatively, the bidder may change bids to find the best bid through exploration. As such, these two can be viewed as substitutes. Interestingly, as the model evaluation costs decrease, decision makers shift away from learning through exploration, which could serve as a stabilizing factor and improve the allocative efficiency. However, given a fixed level of model-evaluation costs, as the frictions to the learning through exploration decrease, agents increase their exploration, which creates a noisier environment and decreases welfare.

<sup>22</sup> We calibrate the learning model based on bid-to-value ratios (Table 6) and the allocative efficiency (Table 7). Because human subjects coming to the laboratory have the ability to extrapolate their learning from outside the laboratory to other contexts more easily than the computational agents, we did not try to match the learning time frames between the computational and laboratory experiments. Further details of the calibration exercise are presented in Online Appendix J.

<sup>23</sup> Recall that, from Figure 1, we know the minimum average allocative efficiency in this market is approximately 85%. This number corresponds to the average allocative efficiency when agents act randomly.

$^ { 2 4 } \mathrm { I n }$ Online Appendix E, we provide some preliminary results regarding the impact of ad quality on the outcomes of GSP. In addition, we highlight how varying the quality score can enable the study of multiobjective goals by a search engine.

## References

Adam MT, Kra¨mer J, Ja¨hnig C, Seifert S, Weinhardt C (2011) Understanding auction fever: A framework for emotional bidding. Electronic Marketing 21(3):197–207.

Adomavicius G, Gupta A, Sanyal P (2006) Computational feedback mechanisms for iterative multiunit multiattribute auctions. 16th Workshop Inform. Tech. Systems (Social Science Research Net work), 205–210.

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2013a) Do recommender systems manipulate consumer preferences? A study of anchoring effects. Inform. Systems Res. 24(4):956–975.

Adomavicius G, Bockstedt J, Curley SP, Zhang J (2014) De-biasing user preference ratings in recommender systems. RecSys 2014 Workshop on Joint Workshop Interfaces Human Decision Making Recommender Systems (IntRS 2014), 2–9.

Adomavicius G, Curley SP, Gupta A, Sanyal P (2012) Effect of infor mation feedback on bidder behavior in continuous combinato rial auctions. Management Sci. 58(4):811–830.

Adomavicius G, Curley SP, Gupta A, Sanyal P (2013b) Impact of information feedback in continuous combinatorial auctions: An experimental study of economic performance. Management Inform. Systems Quart. 37(1):55–76.

Agarwal A, Hosanagar K, Smith MD (2015) Do organic results hel or hurt sponsored search performance? Inform. Systems Res. 26(4):695–713.

Allen T (2014) Information frictions in trade. Econometrica 82(6):2041–2083.

Amaldoss W, Desai PS, Shin W (2015) Keyword search advertising and first-page bid estimates: A strategic analysis. Management Sci. 61(3):507–519.

Anenberg E (2016) Information frictions and housing market dynamics. Internat. Econom. Rev. 57(4):1449–1479.

Animesh A, Ramachandran V, Viswanathan S (2010) Research note—Quality uncertainty and the performance of online sponsored search markets: An empirical investigation. Inform. Sys tems Res. 21(1):190–201.

Animesh A, Viswanathan S, Agarwal R (2011) Competing “creatively” in sponsored search markets: The effect of rank, differentiation strategy, and competition on performance. Inform. Systems Res. 22(1):153–169.

Arnon A, Mansour Y (2011) Repeated budgeted second price ad auc tion. Internat. Sympos. Algorithmic Game Theory (Springer), 7–18.

Bae J, Kagel JH (2019) An experimental study of the generalized second price auction. Internat. J. Indust. Organ. 63:44–68.

Bagozzi RP, Davis FD, Warshaw PR (1992) Development and test of a theory of technological learning and usage. Human Relations 45(7):659–686.

Bapna R, Barua A, Mani D, Mehra A (2010) Research commentary—Cooperation, coordination, and governance in multisourcing: An agenda for analytical and empirical research. Inform. Systems Res. 21(4):785–795.

Bassi V, Nansamba A (2017) Information frictions in the labor market: Evidence from a field experiment in Uganda. Working paper, University College London.

Bichler M, Shabalin P, Ziegler G (2013) Efficiency with linear prices? A game-theoretical and computational analysis of the combina torial clock auction. Inform. Systems Res. 24(2):394–417.

Botvinick MM, Niv Y, Barto AG (2009) Hierarchically organized behavior and its neural foundations: A reinforcement learning perspective. Cognition 113(3):262–280.

Bowling M, Veloso M (2001) Rational and convergent learning in stochastic games. Internat. Joint Conf. Artificial Intelligence, vol. 17 (Lawrence Erlbaum Associates Ltd.), 1021–1026.

Brandimarte L, Acquisti A, Loewenstein G (2013) Misplaced confidences: Privacy and the control paradox. Soc. Psych. Personality Sci. 4(3):340–347.

Cai H, Ren K, Zhang W, Malialis K, Wang J, Yu Y, Guo D (2017) Realtime bidding by reinforcement learning in display advertising Proc. 10th ACM Internat. Conf. Web Search Data Mining, 661–670.

Calvano E, Calzolari G, Denicolo V, Pastorello S (2020) Artificial intelligence, algorithmic pricing, and collusion. Amer. Econom. Rev. 110(10):3267–3297.

Capasso S (2008) Endogenous information frictions, stock market development and economic growth. Manchester School 76(2):204–222.

Cason TN, Kannan KN, Siebert R (2011) An experimental study of information revelation policies in sequential auctions. Management Sci. 57(4):667–688

Chandrasekhar AG, Xandri JP (2022) A note on payments in the laboratory for infinite horizon dynamic games with discounting. Econom. Theory, 1–38

Che Y-K, Choi S, Kim J (2017) An experimental study of sponsored search auctions. Games Econom. Behav. 102:20–43.

Chen J, Feng J, Whinston AB (2010) Keyword auctions, unit price contracts, and the role of commitment. Production Oper. Management 19(3):305–321.

Chen W, Liu T-Y, Yang X (2016b) Reinforcement learning behaviors in sponsored search. Appl. Stochastic Models Bus. Indust. 32(3):358–367.

Chen DL, Schonger M, Wickens C (2016a) oTree—An open-source platform for laboratory, online, and field experiments. J. Behav. Experiment. Finance 9:88–97.

Chen Y, Su X, Zhao X (2012) Modeling bounded rationality in capacity allocation games with the quantal response equilibrium. Management Sci. 58(10):1952–1962.

Cooper DJ, Fang H (2008) Understanding overbidding in second price auctions: An experimental study. Econom. J. (London.) 118(532): 1572–1595.

Deng X, Yu J (2009) A new ranking scheme of the GSP mechanism with Markovian users. Internat. Workshop Internet Network Econom. (Springer), 583–590.

Devanur NR, Kakade SM (2009) The price of truthfulness for payper-click auctions. Proc. 10th ACM Conf. Electronic Commerce (ACM), 99–106.

Du X, Su M, Zhang XM, Zheng X (2017) Bidding for multiple keywords in sponsored search advertising: Keyword categorie and match types. Inform. Systems Res. 28(4):711–722.

Dudharejia M (2018) Four ways you can use AI to optimize your AdWords campaigns. Accessed May 23, 2021, https://www. searchenginewatch.com/2018/06/13/four-ways-you-can-use-aito-optimize-your-adwords-campaigns/.

Edelman B, Schwarz M (2010) Optimal auction design and equilibrium selection in sponsored search auctions. Amer. Econom. Rev 100(2):597–602.

Edelman B, Ostrovsky M, Schwarz M (2007) Internet advertising and the generalized second-price auction: Selling billions of dollars’ worth of keywords. Amer. Econom. Rev. 97(1):242–259.

Feng J, Bhargava HK, Pennock DM (2007) Implementing sponsored search in web search engines: Computational evaluation of alternative mechanisms. INFORMS J. Comput. 19(1):137–148.

Filiz-Ozbay E, Ozbay EY (2007) Auctions with anticipated regret: Theory and experiment. Amer. Econom. Rev. 97(4):1407–1418.

Fukuda E, Kamijo Y, Takeuchi A, Masui M, Funaki Y (2013) Theoretical and experimental investigations of the performance of keyword auction mechanisms. RAND J. Econom. 44(3):438–461.

Gao B, Pavel L (2017) On the properties of the softmax function with application in game theory and reinforcement learning. Preprint, submitted April 3, https://arxiv.org/abs/1704.00805.

Gatti N, Lazaric A, Trovo \` F (2012) A truthful learning mechanism for contextual multi-slot sponsored search auctions with externali ties. Proc. 13th ACM Conf. Electronic Commerce (ACM), 605–622.

Ghose A, Yang S (2009) An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Sci. 55(10):1605–1622.

Goh KH, Bockstedt JC (2013) The framing effects of multipart pricing on consumer purchasing behavior of customized information good bundles. Inform. Systems Res. 24(2):334–351.

Good P (2013) Permutation Tests: A Practical Guide to Resampling Methods for Testing Hypotheses (Springer, New York).

Goodhue DL, Thompson RL (1995) Task-technology fit and individual performance. Management Inform. Systems Quart. 19(2):213–236.

Greenwald A, Hall K, Serrano R (2003) Correlated q-learning. ICML, vol. 3, 242–249.

Greenwald A, Kannan K, Krishnan R (2010) On evaluating information revelation policies in procurement auctions: A Markov decision process approach. Inform. Systems Res. 21(1):15–36.

Greiner B (2015) Subject pool recruitment procedures: Organizing experiments with ORSEE. J. Econom. Sci. Assoc. 1(1):114–125.

Guerci E, Kirman A, Moulet S (2014) Learning to bid in sequential Dutch auctions. J. Econom. Dynamic Control 48:374–393.

Guo Z, Koehler GJ, Whinston AB (2012) A computational analysis of bundle trading markets design for distributed resource allo cation. Inform. Systems Res. 23(3):823–843.

Gupta A, Kannan K, Sanyal P (2018) Economic experiments in information systems. Management Inform. Systems Quart. 42(2): 595–606.

Hou K, Moskowitz TJ (2005) Market frictions, price delay, and the crosssection of expected returns. Rev. Financial Stud. 18(3):981–1020.

Hutchings C (2014) Reasons to never use Google ads automatic bidding. Accessed March 1, 2022, https://www.wordstream.com/blog ws/2014/11/11/never-use-automatic-bidding-in-adwords.

Jerath K, Ma L, Park Y-H, Srinivasan K (2011) A “position paradox” in sponsored search auctions. Marketing Sci. 30(4):612–627.

Kagel JH, Levin D (2001) Behavior in multi-unit demand auctions: Experiments with uniform price and dynamic Vickrey auctions. Econometrica 69(2):413–454.

Kagel JH, Harstad RM, Levin D (1987) Information impact and allocation rules in auctions with affiliated private values: A laboratory study. Econometrica 55(6):1275–1304.

Kagel JH, Levin D, Harstad RM (1995) Comparative static effects of number of bidders and public information on behavior in second-price common value auctions. Internat. J. Game Theory 24(3):293–319.

Kamijo Y (2013) Bidding behaviors for a keyword auction in a sealed-bid environment. Decision Support Systems 56:371–378.

Kempe D, Mahdian M (2008) A cascade model for externalities in sponsored search. Internat. Workshop Internet Network Econom. (Springer), 585–596.

Ketter W, Collins J, Gini M, Gupta A, Schrater P (2012) Real-time tacti cal and strategic sales management for intelligent agents guided by economic regimes. Inform. Systems Res. 23(4):1263–1283.

Kiose D, Voudouris V (2015) The ACEWEM framework: An integrated agent-based and statistical modelling laboratory for repeated power auctions. Expert Systems Appl. 42(5):2731– 2748.

Littman ML (1994) Markov games as a framework for multi-agent reinforcement learning. Proc. 11th Internat. Conf. Machine Learn., vol. 157, 157–163.

McLaughlin K, Friedman D (2016) Online ad auctions: An experiment. Working Paper 16-05, Chapman University, Economic Science Institute, Orange, CA.

Noti G, Nisan N, Yaniv I (2014) An experimental evaluation of bidders’ behavior in ad auctions. Proc. 23rd Internat. Conf. World Wide Web ACM, 619–630.

Qin T, Chen W, Liu T-Y (2015) Sponsored search auctions: Recent advances and future directions. ACM Trans. Intelligent Systems Tech. 5(4):1–34.

Romero J, Rosokha Y (2019) A model of adaptive reinforcement learning. Preprint, submitted April 3, https://dx.doi.org/10 2139/ssrn.3350711.

Rosokha Y, Younge K (2020) Motivating innovation: The effect of loss aversion on the willingness to persist. Rev. Econom. Stat. 102(3):569–582.

Sandholm TW, Crites RH (1996) Multiagent reinforcement learning in the iterated prisoner’s dilemma. Biosystems 37(1–2):147–166.

Sanyal P (2016) Characteristics and economic consequences of jump bids in combinatorial auctions. Inform. Systems Res. 27(2):347–364.

Sheremeta RM (2010) Experimental comparison of multi-stage and one-stage contests. Games Econom. Behav. 68(2):731–747.

Shteingart H, Loewenstein Y (2014) Reinforcement learning and human behavior. Current Opinion Neurobiology 25:93–98.

Silvetti M, Verguts T (2012) Reinforcement learning, high-level cognition, and the human brain. Neuroimaging—Cognitive and Clini cal Neuroscience (Chapter 14) (IntechOpen), 283–296.

Simonov A, Nosko C, Rao JM (2018) Competition and crowd-out fo brand keywords in sponsored search. Marketing Sci. 37(2):200–215.

Statista (2022) Advertising revenue of Google from 2001 to 2021. Accessed March 1, 2022, https://www.statista.com/statistics/ 266249/advertising-revenue-of-google/.

Sutton RS, Barto AG (1998) Reinforcement Learning: An Introduction, vol. 1 (MIT Press, Cambridge, MA).

Tsai JY, Egelman S, Cranor L, Acquisti A (2011) The effect of online privacy information on purchasing behavior: An experimental study. Inform. Systems Res. 22(2):254–268.

Varian HR (2007) Position auctions. Internat. J. Indust. Organ. 25(6): 1163–1178.

Varian HR (2009) Online ad auctions. Amer. Econom. Rev. 99(2):430–434

Watkins CJ, Dayan P (1992) Q-learning. Machine Learn. 8(3–4):279–292.

Wu D, Chen X, Yang X, Wang H, Tan Q, Zhang X, Xu J, Gai K (2018) Budget constrained bidding by model-free reinforcement learning in display advertising. Proc. 27th ACM Internat. Conf. Inform. Knowledge Management, 1443–1451.

Xu L, Chen J, Whinston A (2012) Effects of the presence of organic listing in search advertising. Inform. Systems Res. 23(4):1284–1302.

Zhang XM, Feng J (2011) Cyclical bid adjustments in search-engine advertising. Management Sci. 57(9):1703–1719.

Zhou Y, Chakrabarty D, Lukose R (2008) Budget constrained bidding in keyword auctions and online knapsack problems. Internat. Workshop Internet Network Econom. (Springer), 566–576.
