---
otero_id: 5952
otero_key: "ATZH979H"
title: "Trust based decisions in supply chains with an agent"
authors: "Xiao Fu; Ming Dong; Shaoxuan Liu; Guanghua Han"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.11.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Xiao Fu <sup>a</sup>, Ming Dong <sup>a,</sup>⁎, Shaoxuan Liu <sup>a</sup>, Guanghua Han

<sup>a</sup> Antai College of Economics & Management, Shanghai Jiao Tong University, Shanghai 200030, PR China <sup>b</sup> School of International and Public Affairs, Shanghai Jiao Tong University, Shanghai 200030, PR China

## a r t i c l e i n f o

Article history: Received 24 October 2013 Received in revised form 18 November 2015 Accepted 18 November 2015 Available online 4 December 2015

Keywords: Information sharing Trust update Simulation Agent

## a b s t r a c t

In this paper, we propose a quantitative method to study the trust relationship between a retailer (he) and an agent (she) in the supply chain. The retailer seeks private demand forecast information from the agent before procuring the optimal order quantity (OOQ) of a product from a supplier. To earn more profit, the agent has an incentive to inflate her forecast. However, the decisions of the agent has impact on her immediate gains as well as her future credibility as the retailer updates his trust in the agent at the end of each demand period. We study how the repeated interaction and updated trust influence decisions of the retailer and the agent and their impacts on the supply chain performance. We also investigate how social characteristics of the agent affect the decisions and supply chain performances. In particular, we consider two types of agents: a benevolent agent who seeks to maximize the retailer's profit and a selfish agent who cares only her own profit. The simulation results and analyses of this paper show, that trust updating model effectively embodies the idea of punishment for opportunism and maliciously recommended behavior which are brought about under the influence of the selfish commission agent; that trust value will decline rapidly when consecutive trading failure occurs or the commission agent begins to have opportunistic behavior, i.e. the retailer's predicted demand is more accurate than commission agent's; and that to restore trust value has to undergo a lengthy process which will take commission agent a long time and greater effort to earn trust back.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Solectron used to be one of the biggest electronics contract manufacturers in the world. In 2000, company officials said that they were concerned about overcapacity in telecom equipment. However, their big customers such as Cisco, Ericsson and Lucent, were very optimistic and predicted rapid increase in wireless phones and networking gear market. Despite Selectron's concerns, big telecom companies pushed Solectron and other contractors to build up capacities and produce more products. And they promised to pay for the excess material. But when the order dropped, it was too late for Solectron to stop orders from its 4000 suppliers, which finally caused a \$4.7 billion write-off in inventory. This case shows that distrust between corporations in the upstream and downstream of a supply chain can result in increase of inventory and decrease of profits.

When entering a new market, many companies rely on local agents to gather market information, as local agents possess better demand information than the retailer because of their local connections. For instance, BMW commissioned its sale of cars in China to South Industries Motors, a local company in southern China. BMW obtained knowledge of Chinese consumers' tastes, market size and demand information through the agent. The agent not only helped BMW sell its products and facilitates the establishment of reputation of its products, but also laid the foundation for BMW to build factories to manufacture cars, which not only reduced the cost and risk but also obtained great benefits. In addition, many corporations of international wine brands sell their products through the one-agent and severalretailers model. These cases show that the agents play a crucial role in the trust of the supply chain. The trust issue exists in those decision processes. Similarly, in a field study of a major automotive manufacturer [10] they found that the dealer and the salesperson (who serves as the agent) were willing to share their forecasts of demand even if formal contract about information sharing did not exist. In addition, almost all of the salespersons they interviewed indicated that the key to success was a trusting and mutually beneficial relationship with the dealers. In this paper, we specifically examine the roles of trust, length of relationship, and demand forecast accuracy of the agent and the retailer in the information sharing mechanism.

Information asymmetry is common in supply chain because the information holder has the intention to share unreal information to maximize his (her) profit. Thus, the information receiver may distrust the received information. Therefore, trust has been recently introduced into the supply chain information sharing process to mitigate the information receivers' potential loss. Trust has also been proven to be helpful for supply chain cooperation [19]. Trust reflects the enterprise's reliability, integrity, and ability to dynamically change over time based on transaction history. Trust varies in a wide range of levels from a full trust to a complete distrust. A trust value can represent these levels.

This paper studies the effectiveness of trust in a three-tier supply chain. The agent (she) forecasts the market demand and recommends an order quantity to the retailer. At the same time, the retailer (he) also makes the market forecasting. Once the retailer receives the agent's recommended order quantity (ROQ), he has to decide to what degree he should trust the agent then he updates his forecasting about the market demand combing both the agent's and his own forecast by using a trust model (we will introduce the trust model in Section 3) and places an order. The manufacturer produces and delivers the product quantities according to the retailer's orders. Because the agent's profit is positively affected by the retailer's order quantity, she may overstate the demand forecast.

In practice, trust is accumulated gradually based on past experiences. Therefore, in this paper, we study the information sharing process with trust in multi-periods. To model the dynamic of the retailer's attitudes towards the agent's trustworthiness, the retailer's trust level of the agent is assumed to change over periods based on historical transactions, and the agent must make her decisions of ROQ taking into account retailer's trust level. The optimal ROQ in each period is thereby calculated. We find that our proposed trust updating model can motivate the agent to make better decisions and improve the whole supply chain's performance.

The contributions of the paper are twofold. First, a trust updating model is proposed to formulate the retailer's trust changing process across different transaction periods. In the extant literature, trust was often considered a constant [7,18] that never changed over periods. However, trust is usually adjusted according to the information sender's past actions. Trust can also be affected by the information accuracy when the information receiver obtains information from multiple sources. Thus, the proposed trust model also takes this fact into consideration. Second, in our paper the level of trust is quantified and studied under a multi-period model wherein three parties (i.e., a supplier, a retailer and an agent) share information. Since the multi-period information sharing problem seldom considers the trust issue, this paper explores the evolution of trust and its impacts on the information sharing and decisions of different parties in a supply chain. Some managerial insights are derived based on our model analysis and extensive simulation studies.

The rest of the paper is organized as follows: in Section 2, we review the related literature; in Section 3, we formulate the multi period trust updating model; in Sections 4 and 5, we design the experiment and run many simulations. Then the simulation results are analyzed. In the last section, we conclude the paper as well as consider any future work.

## 2. Literature review

This paper studies the demand information sharing problem in a three-tier supply chain. A trust model is proposed to model the evolution of the retailer's trust levels about the agent. Due to information asymmetry, the agent has intention to report unreal information to maximize her own profit [6]. The multi-period trust updating model is very critical and enables the retailer to adjust his trust level about the agent and reduce risk. From as early as 1990s there were scholars who conducted research on the concept of trust between enterprises. For example, Doney and Cannon [21], Carney [2], and Morgan and Hunt [16] used game theory, methods of transaction costs, principal-agent method, and etc., to study the dynamic trust between enterprises in the supply chain. Selnes [24] used credit standing theory which holds that trust always has something to do with past behavior or events, and that the good credit standing of the seller will enhance the buyer's trust. Ganesan [9] claimed that the good credit standing of the seller is based on the reliability and consistency of past behavior. Johnson and Houston [14] believed that the supplier that has good credit has the motive to fulfill honest and consistent behavior in the market. Moreover, trust is not only associated with corporate goodwill but is also closely related to other factors of the transaction object [12]. The previous research studied what factors affect trust, our paper differs from this stream of literature as we focus on examining how the evolution of trust affects the decisions of different players in a supply chain and their performances.

Although most of previous research in operations management on trust has been empirical work, analytical research on trust has received attention in operations management area. There is a growing body of work that studies supply chain trust issues using both modeling and simulation methods. Taylor and Plambeck [26] developed a model in which a buyer and a supplier had an informal agreement on required capacity. They concluded that the buyer would honor such an agreement because of the future value of cooperation. Ren et al. [23] considered a supply chain where a buyer shares his demand forecast with a supplier to facilitate the supplier's decisions in building manufacturing capacity. While the buyer has incentive to inflate the demand forecast in an attempt to ensure future supply, the supplier may respond by underinvesting in capacity. The authors showed that if the relationship is long term, it is optimal for the buyer to report the true forecast to the supplier to gain the supplier's trust. Özer et al. [19] studied the applications of trust in the information sharing process between the supplier and the manufacturer and proved that the manufacturer can effectively make capacity plans by levels of trust. And the higher the goodwill of the retailer, the more confidence the supplier has in the retailer's information.

![](/api/attachments/ATZH979H/fulltext/images/4745daea8770233d9c8e46ea790cffbdf47070c9c9020cb7f22d5306700fd243.jpg)  
Fig. 1. The operation framework of the three-tier supply chain.

With the rise of internet technology, the trust mechanism of online service and e-commerce became an important research area in recent years. Kim et al. [5] formulated a model to study the effects of trust antecedents. They identified user satisfaction, perceived reputation, disposition to trust and information quality as the key antecedents of trust belief. Wierzbicki et al. [27] proposed a sophisticated computational trust management system for Internet auctions. Midha [17] examined how perceptions of trust differ between genders and showed that empowerment has a stronger positive effect on trust for males than for females. Based on a large scale online transaction dataset, Özpolat and Jank [20] demonstrated that four variables moderate the effectiveness of consumer trust in e-commerce on their likelihood of purchase. Chiu et al. [4] examined the role of trust on online repeated purchasing. They found that a higher level of online shopping habit reduced the effect of trust on repeat purchase intention. Fang et al. [8] proposed a multi-faceted trust-aware recommendation system that incorporates both interpersonal and impersonal aspects of trust. Their experimental results showed that the proposed model outperformed other existing recommendation system in predictive accuracy. Jøsang et al. [11] provided a review of literature that studied trust and reputation systems for online services.

The research most closely related to our work is Ebrahim-Khanjari et al. [6]. They assumed that the retailer and salesperson use Bayes rule to forecast demand and they make a general observation that two kinds of salesperson compensation scheme depend on her social characteristics. In our model, we use similar model of demand forecast and utility function of the salesperson. However, unlike Ebrahim-Khanjari et al. [6], we propose a more reasonable mechanism of trust value updating in multiple-period transactions. Moreover, the focus of Ebrahim-Khanjari et al. [6] is to find a compensation mechanism, our paper considers a variety of other issues. For example, we study the impacts of demand forecast accuracy, the initial trust value (credit standing) and we also study how product characteristics affect the decisions of different parties in the supply chain.

## 3. Model formulation

To study the role of trust in a supply chain, we develop a model which consists of a supplier, a retailer and an agent. The retailer sells the product in multiple periods. In the beginning of each period, the sequence of events takes place as follows: (1) Retailer predicts order quantity $f ^ { r }$ based on historical demand and figures out the optimal order quantity $q ^ { r } ( f ^ { r } )$ to maximize his utility. The agent also predicts order quantit $\boldsymbol { J } ^ { f s }$ based on historical demand and figures out the optimal order quantity $q ^ { s } ( f ^ { s } )$ to maximize her utility. (2) The agent makes demand forecast and decides on the recommendation, which is affluence by her social preferences (similar to Ebrahim-Khanjari, we consider four types of preferences). (3) The agent recommends an order quantity, denoted by $Q ^ { s } ,$ to the retailer. Remember, due to asymmetrical information, the agent has incentive to report unreal information to maximize her own profit. (4) The retailer adjusts the order quantity and decides on the final actual order quantity $Q ^ { r }$ (FAOQ). The decision is made based on his own optimized order quantity $q ^ { r } ( f ^ { r } )$ , the agent's recommended order quantity Q<sup>s</sup>, and his trust in the agent.

(5) The retailer submits the order quantity $Q ^ { r }$ to the manufacturer through the agent. (6) The manufacturer produces the products and delivers them to the retailer. (7) The retailer figures out the profit and compares the difference value between the recommended quantity $Q ^ { s }$ and the actual demand d, with the difference value between the optimized quantity $q ^ { r } ( f ^ { r } )$ and the actual demand d at the end of the period. The difference value is used to update the trust value for the next period. Fig. 1 depicts the decision making processes of the three players within the supply chain.

## 3.1. Demand prediction and profit model

We use similar assumptions to model market demand and demand forecasting as Ebrahim-Khanjari et al. [6]. Market demand D is a discrete random variable $D \in$ d; $\underline { d } + 1 , \underline { d } + 2 , . . . , \overline { d } \}$ that is subject to the uniform distribution $G ( \cdot )$ and the probability density function $g ( \cdot ) .$ . Therefore, d and $\overline { d }$ are the lower limit and the upper limit of the market demand, respectively. Since this paper focuses on the role of trust, we assume that demand is independent across periods.

The retailer's predicted order quantity (POQ) is assumed to be a discrete random variable, and it is subject to $F ^ { r } { \in } \{ \underline { { d } } , \underline { { d } } + 1 , . . . , \overline { { d } } \}$ When the market demand equals to $\mathsf { d } , \mathsf { D } = \mathsf { d } ,$ , the c.d.f (cumulative probability distribution) of the retailer's POQ is $G ^ { r } ( \cdot | d ) .$ , the retailer's POQ follows beta distribution, and its standard deviation is assume to be $\sigma _ { r } .$ . σ measures the degree of accuracy of the retailer's prediction. The conditional probability density function is denoted by $g ^ { r } ( \cdot | d )$ (see [6]).

$$
\operatorname * {P r} (D = d \mid F ^ {r} = f ^ {r}) = \frac {g ^ {r} (f ^ {r} \mid d) g (d)}{\sum_ {i = 0} ^ {n - 1} g ^ {r} (f ^ {r} \mid \underline {{d}} + i) g (\underline {{d}} + i)}\tag{1}
$$

Therefore, $n = ( \overline { d } - \underline { d } + 1 )$ . It is assumed that the agent can observe <sup>¼ ð þ Þ</sup>all historical market demand. Therefore, the agent can also predict the order quantity from the market demand in history, and the conditional probability density function is g<sup>s</sup>(⋅|d) (see [6]).

$$
\operatorname * {P r} (D = d \mid F ^ {s} = f ^ {s}) = \frac {g ^ {s} (f ^ {s} \mid d) g (d)}{\sum_ {i = 0} ^ {n - 1} g ^ {s} (f ^ {s} \mid \underline {{d}} + i) g (\underline {{d}} + i)}\tag{2}
$$

$G ^ { r } ( \cdot | d )$ and $G ^ { s } ( \cdot | d )$ follow beta distributions. We use the beta distribution because it has a very flexibly shaped distribution and is also amenable to Bayesian updating. If $\sigma _ { s } < \sigma _ { r }$ , the agent's prediction is more

![](/api/attachments/ATZH979H/fulltext/images/60d47890cc2f79bbb48745d65770318cbed9937a51bd78942df4f41aa6f582da.jpg)  
Fig. 2. Trust and prediction accuracy with benevolent agent.

Table 1

![](/api/attachments/ATZH979H/fulltext/images/9a96c2489e337a25c078a3b94ebb94668d13671e8bfe833982ab0c3f6ce2f148.jpg)  
Fig. 3. Increment and total expected utility with benevolent agent.

accurate than the retailer's. If $\sigma _ { s } > \sigma _ { r }$ the retailer's prediction is more accurate than the agent's.

There are some price parameters in our model: $p _ { c }$ is production cost from manufacturer; $p _ { m }$ is wholesale price that manufacturer sales to retailer; p<sub>r</sub> is retailer's selling price, $p _ { r } { > } p _ { m } { > } p _ { c } ; h _ { r } \mathrm { i }$ s salvage of one product; s is shortage cost, these are all known constants.

When the order quantity is q and the demand is d, the retailer's profit function can be written as:

$$
\prod^ {R} (q, d) = p _ {r} \min \{q, d \} - p _ {m} q + h _ {r} [ q - d ] ^ {+} - s _ {r} [ d - q ] ^ {+}.\tag{3}
$$

The manufacturer's profit function is:

$$
\prod^ {M} (q) = (p _ {m} - p _ {c}) q.\tag{4}
$$

The agent's profit is based on the number of selling goods. And agent gets the commission from the manufacturer. Where, a is commission coefficient.

$$
\prod^ {S} (q) = a q\tag{5}
$$

Because the retailer intends to maximize his profit, the retailer's OOQ is [6]:

$$
\begin{array}{l} q ^ {r} \left(f ^ {r}\right) = \arg \max _ {q} E \left[ \prod^ {R} (q, d) | F ^ {r} = f ^ {r} \right] \\ = \arg \max _ {q} \sum_ {i = 0} ^ {n - 1} \prod^ {R} (q, \underline {{d}} + i) \operatorname * {P r} \left(D = \underline {{d}} + i | F ^ {r} = f ^ {r}\right) \end{array}\tag{6}
$$

Total utility as a function of increment and credit standing.

<table><tr><td> $\theta$  (%)</td><td>0.25</td><td>1.00</td><td>2.00</td><td>3.00</td><td>5.00</td><td>10.00</td><td>13.75</td></tr><tr><td> $W_0 = 0.1$ </td><td>1.43</td><td>1.41</td><td>1.43</td><td>1.40</td><td>1.32</td><td>1.05</td><td>0.92</td></tr><tr><td> $W_0 = 0.25$ </td><td>1.32</td><td>1.33</td><td>1.34</td><td>1.34</td><td>1.31</td><td>1.14</td><td>0.92</td></tr><tr><td> $W_0 = 0.5$ </td><td>1.27</td><td>1.28</td><td>1.29</td><td>1.28</td><td>1.27</td><td>1.19</td><td>1.01</td></tr><tr><td> $W_0 = 0.75$ </td><td>1.25</td><td>1.26</td><td>1.27</td><td>1.28</td><td>1.27</td><td>1.17</td><td>1.05</td></tr><tr><td> $W_0 = 0.95$ </td><td>1.24</td><td>1.25</td><td>1.27</td><td>1.28</td><td>1.27</td><td>1.17</td><td>1.05</td></tr></table>

where P $\operatorname { r } ( D = d | F ^ { s } = f ^ { s } )$ is given in Eq. (1). For the same scenario, the OOQ of the agent is [6]:

$$
\begin{array}{l} q ^ {s} (f ^ {s}) = \arg \max _ {q} E \left[ \prod^ {R} (q, d) | F ^ {s} = f ^ {s} \right] \\ = \arg \max _ {q} \sum_ {i = 0} ^ {n - 1} \prod^ {R} (q, \underline {{d}} + i) \operatorname * {P r} (D = \underline {{d}} + i | F ^ {s} = f ^ {s}) \end{array}\tag{7}
$$

where $\operatorname* { P r } ( D = d | F ^ { s } = f ^ { s } )$ is given in Eq. (2). Note that $q ^ { r } ( f ^ { r } )$ and $q ^ { s } ( f ^ { s } )$ depend on f<sup>r</sup> and $f ^ { s } ,$ respectively

As the agent also intends to overstate the demand, there is also an increment in the ROQ Q<sup>s</sup> that the agent provides for the retailer; the increment can be formulated as $Q ^ { s } = q ^ { s } ( f ^ { s } ) + \theta .$ . Generally, the agent will report a higher order quantity than the OOQ to increase her own profit [10]. The ROQ of the agent is affected by many factors, such as the agent's roles (benevolent or selfish), under stock cost and overstock cost. The increment θ here can also be considered as an indicator of agent's likelihood of telling lies. If the agent is selfish and shortsighted, the value of θ is large as the likelihood of telling lies is very high; the value of θ is small if the agent is benevolent and far-sighted, her likelihood of telling lies is not high. Note that in the following numerical calculation, θ represents the incremental percentage (%) of the agent's ROQ.

Now we introduce the way we model the evolution of trust. In period t, the retailer relies on his trust of the agent and decides on the FAOQ according to his own POQ and the agent's ROQ. As suggested by Stone [25] and Clemen and Winkler [3], the retailer's FAOQ is written as,

$$
Q _ {t} ^ {r} = (1 - w _ {t}) q _ {t} ^ {r} \left(f _ {t} ^ {r}\right) + w _ {t} Q _ {t} ^ {s}.\tag{8}
$$

The more the retailer trusts the agent, the more weight he puts on her recommendation. The more the agent's ROQ increases the retailer's profit in the short term, the more trust a retailer gains as an agent. Hence, we use the retailer's POQ and the agent's ROQ to analyze the weight as a measure of the retailer's trust in the agent.

Charness and Rabin [1] argued that people were willing to sacrifice their own payoff to benefit a low payoff player or to punish unfair players. To incorporate such social characteristics in our model, we assume that the Agent's Utility Model is:

(a) σs/or=0.4  
![](/api/attachments/ATZH979H/fulltext/images/8ce8c0ca0f895d4428f4368893ad81187cb4770bfba579b08468286bc064ea4a.jpg)

![](/api/attachments/ATZH979H/fulltext/images/e4d79ba6970da51d17d56618d1044354eed8e5b40f4b5bc869c2004a8e8b4de0.jpg)  
Fig. 4. Changes of retailer's trust under different initial trust levels.

(c) σs/or=2.5  
![](/api/attachments/ATZH979H/fulltext/images/a0ffec2bd6b67143288214a8d1cb35070742b05806824f0ed0b7ae7a49b4050a.jpg)

![](/api/attachments/ATZH979H/fulltext/images/70c0af4334a69e06377a5ae2b5a77c13533b167582c1ca4c303ee31f3e12aa19.jpg)  
Fig. 5. The total utility and increment under benevolent agent's different credit standings

$$
U _ {t} ^ {S} \left(Q _ {t} ^ {r}, d _ {t}\right) = \alpha \prod_ {t} ^ {S} \left(Q _ {t} ^ {r}\right) + (1 - \alpha) \rho \left[ \beta \prod_ {t} ^ {M} \left(Q _ {t} ^ {r}\right) + (1 - \beta) \prod_ {t} ^ {R} \left(Q _ {t} ^ {r}, d _ {t}\right) \right]\tag{9}
$$

where $\alpha \in [ 0 , 1 ]$ is the selfish variable of agent. This represents the relationship between the agent's concern about one's own interest and his concern about the other members' interest in the supply chain. β ∈ [0, 1] is the agent's loyal variable; it represents whose interest (retailer's or manufacturer's) the agent is more concerned about. $\rho \in [ 0 , 1 ]$ is the scale coefficient. As the agent's profit is much lower than the retailer's and manufacture $\mathrm { \Delta } ^ { \because } { \sf S } ,$ the significance of ρ is used to adjust the order of magnitudes of ∏<sup>S</sup>, ∏<sup>R</sup>,and $\bar { \prod _ { t } ^ { M } }$

At period T, the total expected utility of the agent is:

$$
\sum_ {t = 1} ^ {T} U _ {t} ^ {S} (Q _ {t} ^ {r}, d _ {t}) = \sum_ {t = 1} ^ {T} \Bigl \{\alpha \prod_ {t} ^ {S} \bigl (Q _ {t} ^ {r} \bigr) + (1 - \alpha) \rho \Bigl [ \beta \prod_ {t} ^ {M} \bigl (Q _ {t} ^ {r} \bigr) + (1 - \beta) \prod_ {t} ^ {R} \bigl (Q _ {t} ^ {r}, d _ {t} \bigr) \Bigr ] \Bigr \}.\tag{10}
$$

![](/api/attachments/ATZH979H/fulltext/images/b8a9b0c5b14b0d24ab7a780ff573105e12e088fe993911f6a2ee645cc82e98cf.jpg)  
Fig. 6. The total utility and increment under benevolent agent's different predictive accuracies

## 3.2. Trust model

In order to update his trust in the agent, first the retailer needs to compare the absolute value of the deviation obtained by subtracting his own POQ from the actual market demand with the absolute value of the deviation that is obtained by subtracting the agent's ROQ. Then, the retailer finds out whose ROQ is more accurate, and can finally choose the trust updating model to update his trust. If the agent's ROQ is more accurate he will earn more trust from the retailer. We call this a “successful” transaction. An unsuccessful transaction occurs when the agent's forecast is less accurate than the retailer. In this case, the agent will lose certain degree of retailer's trust in next demand period. Jonker and Treur [13] proposed that there were several levels in the state of trust, and the transition from one state of trust to the other depends on the comprehensive effect of trust-negative and trustpositive experiences of the agent. Similarly, whether the transaction is successful or not can be measured by the accuracy of the ROQ. Motivated by Jonker and Treur's findings, we propose a new trust updating model, which is different from the model formulation of Ebrahim-Khanjari et al. [6]. We believe that our trust updating model is more realistic, thus the results derived from the model analysis generate new managerial insights. Specifically, our trust updating model can be formulated as:

$$
w _ {t} = \left\{ \begin{array}{l l} w _ {t - 1} \big (1 + w _ {d c a, t - 1} \times \delta^ {g} \times (\Delta_ {d q, t} - \Delta_ {d Q, t}) / (\Delta_ {d q, t} + \Delta_ {d Q, t}) \big) & \text {   if   } \Delta_ {d q, t} \geq \Delta_ {d Q, t} \\ w _ {t - 1} \Big (1 + w _ {d c a, t - 1} \times \sigma^ {l} \times (\Delta_ {d q, t} - \Delta_ {d Q, t}) / (\Delta_ {d q, t} + \Delta_ {d Q, t}) \Big) & \text {   if   } \Delta_ {d q, t} \leq \Delta_ {d Q, t}. \end{array} \right.\tag{11}
$$

Since credit standing (named as the initial trust value), is the accumulative amount over the past years, w is a constant.

Define $w _ { d c , t - 1 } = | w _ { t - 1 } - 0 . 5 |$ | is the distance between trust value $w _ { t - 1 }$ to its center. $w _ { d c a , t - 1 } = | w _ { d c , t - 1 } - 0 . 5 |$ is the adjusted distance $w _ { d c , t \mathrm { ~ - ~ } 1 }$ to shift away from 0 for not making the second component in Eq. (11) into zero. $w _ { d c a , t - 1 }$ represents the impact of the previous transaction on the current trust value. As we have discussed above, $W = \rho _ { W _ { 0 } }$ $W _ { 0 } + \rho _ { W _ { c } } W _ { C } , W _ { 0 }$ is the initial trust value, $\rho _ { W _ { 0 } }$ means the weight of the initial trust value, W represents retailer's cumulative trust which is obtained from records of historical transactions, and $\rho _ { W _ { C } }$ is the weight of cumulative trust, Therein $\rho _ { W _ { 0 } } + \rho _ { W _ { C } } = 1$ . It can be easily inferred that the Trust Centre would appear when $\rho _ { W _ { 0 } } = \rho _ { W _ { C } } = 0 . 5$ . In other words. trust between the two parties during the transaction would arrive at a state of balance in which there would be no complete trust or complete distrust [22]. $w _ { d c , t \mathrm { ~ - ~ } 1 }$ represents the distance between the current trust value and the Trust Center, and $w _ { d c a , t \mathrm { ~ - ~ } 1 }$ is to avoid the situation in which the trust value reaches 0.5, yet the overall trust value is 0. For example, when $w _ { t \mathrm { ~ - ~ } 1 } = 0 . 5 , w _ { d c a , t \mathrm { ~ - ~ } 1 } = 0 . 5$ , this shows that the trust value will remain unchanged. When $w _ { t - 1 } = 0 . 1$ $w _ { d c a , t - 1 } = 0 . 1$ , this shows that the decreasing rate of the trust value will become lower when the previous trust value is approaching the minimal. When $w _ { t \mathrm { ~ - ~ } 1 } = 0 . 9 , w _ { d c a , t \mathrm { ~ - ~ } 1 } = 0 . 1$ , this shows that the increasing rate will become smaller when the previous trust value is approaching the maximal. Therefore, $w _ { d c a , t \mathrm { ~ - ~ } 1 }$ embodies how if the time is closer to the present, the feedback information will be more credible. It will be a long process to reach a high credit level, and it will also need a long time to recover a high credit value when it falls down to a very low level.

δ ∈ (0, 1) is the sensitivity parameter, representing the speed at which the retailer gains or loses trust towards the agent at a period t. Setting the values of $\cdot \delta ^ { g }$ and $\delta ^ { l }$ can reflect that gaining trust needs quite a few successful transactions yet losing trust only needs very few failure transactions. The literature on trust suggests that the rates of gain or loss of trust may not be symmetric [15,28]. Typically, trust is more likely to be lost through negative experiences than gained back through positive experiences.

![](/api/attachments/ATZH979H/fulltext/images/7868f438dc83e21566f46c601b1cb5d799aa928cfffc644e2c08b0b6a714d9b8.jpg)

![](/api/attachments/ATZH979H/fulltext/images/9825ac1e1f44a494ce5b59adffadda4893610020d34d8c9c00c173fb33b8ada8.jpg)

![](/api/attachments/ATZH979H/fulltext/images/1636b4224e2448bc833836343734e831b8c1a88753d75a621a5e2c1e0971cfd2.jpg)

![](/api/attachments/ATZH979H/fulltext/images/9f53e4de78b0d42ba7662de5d817b7a26fa2e364d82b0cc9c761f8f90ff4e3b7.jpg)

![](/api/attachments/ATZH979H/fulltext/images/9dbd9c13c710560c1488356f270befc8238bcb33cedcb204ea073cf80da454d8.jpg)

![](/api/attachments/ATZH979H/fulltext/images/e9719392eaf7f34cb1770a5e240aa8e6db11cb3d60ed14bbaf4d650d4bf8eeaa.jpg)  
Fig. 7. The relationship between trust, increment and period under benevolent agent's different credit standings.

Note that $\Delta _ { d q , t } = | d _ { t } - q _ { t } ^ { r } |$ is the gap between the real demand (at time t) and retailer's predicted demand. Similarly, $\Delta _ { d Q , t } = | d _ { t } - Q _ { t } ^ { s } |$ is the gap between the real demand (at time t) and agent's predicted demand. $\Delta _ { d q , t } - \Delta _ { d Q , i }$ will be more than $[ - 1 , 1 ]$ obviously, so $( \Delta _ { d q , t } - \Delta _ { d Q , t } ) / ( \dot { \Delta } _ { d q , t } + \dot { \Delta } _ { d Q , t } )$ can ensure access to $[ - 1 , 1 ] . ( \Delta _ { d q , t } -$ $\Delta _ { d Q , t } ) / ( \Delta _ { d q , t } + \Delta _ { d Q , t } )$ reflects the influence on the trust value in each phase that the absolute value of what is obtained minus the predictive value of the agent from the actual demand and the absolute value of what is obtained minus the predictive value of the retailer and the actual demand; the bigger the difference value is between the absolute value of what is obtained minus the predictive value of the agent from the actual demand and the absolute value of what is obtained minus the predictive value of the retailer and the actual demand, the smaller the degree of the retailer's trust is towards the agent, and vice versa. For example, when $d _ { t } = 5 0 , q _ { t } ^ { r } = 5 2$ , and $Q _ { t } ^ { s } =$ $5 5 , ( \Delta _ { d q , t } - \Delta _ { d Q , t } ) / ( \Delta _ { d q , t } + \Delta _ { d Q , t } ) = - 3 / 7$ which shows that if the retailer predictsmore accurately, the retailers would not trust the agent, so the ratio would be negative and the trust value would decrease. When $d _ { t } = 5 0 , q _ { t } ^ { r } = 5 5 ,$ and $Q _ { t } ^ { s } = 5 2 , ( { \Delta _ { d q , t } } - { \Delta _ { d Q , t } } ) / ( { \Delta _ { d q , t } } + { \Delta _ { d Q , t } } ) = 3 / 7 ,$ shows that if the agent predicts more accurately, the retailer would trust the agent so that the ratio would be positive and the trust value would increase.

![](/api/attachments/ATZH979H/fulltext/images/61848930a5f17c5d523be4b8153798fe8dbd47ffc75e57944db5db722f600c7a.jpg)

## 4. Design of simulation experiments

To demonstrate the effects of the trust updating model, we conduct a series of numerical simulations to analyze the behavior of the agent, the retailer and the resulting profits of each party in the supply chain under different social roles played by the agent. The values of the relevant parameters are set in the following.

The values of the other parameters are: agent's prediction accuracy $1 / \sigma _ { s } \in \{ 0 . 1 , 0 . 1 5 , 0 . 2 5 \}$ , where the normalized standard deviation is $\sigma _ { s } /$ $( \overline { { d } } - \underline { { d } } )$ ; retailer's prediction accuracy $1 / \sigma _ { r } \in \{ 0 . 1 , 0 . 1 5 , 0 . 2 5 \}$ }, where the normalized standard deviation is $\sigma _ { r } / ( \overline { d } - \underline { d } )$

Fig. 8. Trust and prediction accuracy with selfish agent.  
![](/api/attachments/ATZH979H/fulltext/images/b86e3ca4bc41901fbdc92ab51ef0f75732d1a4ba6cb978c77098b51935f9b67e.jpg)  
Fig. 9. Increment and expected utility with selfish agent.

![](/api/attachments/ATZH979H/fulltext/images/2bfd3144bf898cb98e3520a58b389404015b05938f10b4e07c3c90ac60ad7157.jpg)

![](/api/attachments/ATZH979H/fulltext/images/2e7ecb24632ca085df654fa3ba9306684cc9884d96c0bd885cc369faf7c407a3.jpg)  
Fig. 10. The relationship between manufacturer's commission payments, retailer's trust value and total expected utility with the cost rate of $C R = 2 .$

Under stock cost is $p _ { r } - p _ { m } + s _ { r }$ , and overstock cost is $p _ { m } - h _ { r }$ . Under stock cost represents the loss of the retailer due to a unit shortage, whereas overstock cost represents the unit loss of the retailer if he has leftover inventory. We define $C R \ = \ ( p _ { r } \ - \ p _ { m } \ + \ s _ { r } ) / ( p _ { m } \ - \ h _ { r } )$ $C R \in \{ 2 , 1 , 0 . 5 \}$ as the cost rate. It is the critical ratio formula of the newsvendor problem, and this formula is used to describe the relationship between the order quantity and the corresponding cost. $C R = 2$ represents that manufacturer sells high-margin products, high under stock cost will bring high penalty costs so that the prediction demand will be low. $C R = 0 . 5$ represents that manufacturer sells low-margin products, high overstock cost will boost prediction demand.

## 5. Experimental results

Since our multi-period model considers both the dynamic evolution of trust based on past transaction experience and different types of social characteristics of the agent, the structure of the model is very complicated. It turned out that the optimal policy is difficult to solve. As many researchers, we resort to numerical studies. Despite the lack of analytical solution, we believe that the observations derived from our extensive simulation studies shed some light on the impact of dynamic trust updating and agent's social characteristics, thus provide some managerial insights for the practitioners. In this section, we carry out extensive numerical simulations. Specifically, we investigate the following issues: (1) Factors that incentivize the agent to tell lies. (2) The impact of the initial trust level (credit standing) on the retailer's trust value; (3) the impact of the different social preferences (benevolent or selfish) of the agent on the retailer's trust; (4) the different roles (benevolent or selfish) of the agent on the utility; (5) whether or not the agent can gain the retailer's highest trust value when his own profits is maximized.

## 5.1. Benevolent agent

The benevolent agent is that the retailer's favor for the agent's decision is more likely to increase the retailer's profits. In this section, we will explore on: (1) the influence of the accuracy of the agent's prediction, the initial trust value (credit standing), and the cost rate influence on the trust value, (2) whether the benevolent agent also tells lies and increases the increment of ROQ, and (3) what strategy the benevolent agent makes to maximize the total expected utility.

Observation 1. The accuracy of the POQ of a benevolent agent has significant impact on the change of trust value.

This is when the agent's selfish variable α = 0, his loyal variable $\beta =$ 0, the initial trust value $w _ { 0 } = 0 . 5 , \mathrm { t h e p e r i o d } T = 2 4$ , the cost rate $C R = 2$ sensitivity parameter δ's trust gaining coefficient $\delta ^ { g } = 0 . 5 , \delta ^ { \prime } s$ trust losing coefficient $\delta ^ { l } = 1$ , the analysis of the relationship between $\sigma _ { s } / \sigma _ { r }$ , and the trust value w is given in Fig. 2. Fig. 2 shows that the retailer's trust value towards the agent is on an upward tendency when the agent's prediction is more accurate. Moreover, the retailer's trust value towards the agent is on a downward tendency when the retailer's demand prediction is more accurate.

Fig. 3 illustrates the relationship between the increment θ and the total optimized expected utility U. The x-axis represents the incremental ratio of each ROQ and the y-axis represents the total optimized expected utility in the whole period 24. These curves show that when the agent is benevolent, the slight and appropriate rising of θ can make the total optimized expected utility maximal. When the increment θ is less than 10%, the total optimized expected utility increases with the raising of θ. But with the increment becoming larger and larger, the retailer's trust value on the agent will decrease because of the selfadaption of the trust updating formula, and the retailer's profit will thereupon decrease. We can know from Eq. (8) that when the trust value decreases to zero, the retailer's ROQ is her optimal POQ. Then through Eq. (10) the total expected utility can be only obtained by calculating the retailer's profit. Therein $\sigma s / \sigma r = 0 . 4$

![](/api/attachments/ATZH979H/fulltext/images/e4b5b0d345587db7a30b99fe915b8c47395fd9b617e64bd674134c6dba5c2c85.jpg)

![](/api/attachments/ATZH979H/fulltext/images/d6f784f6d38ebef7f3aa0954ec4aae2e0a5bff45e22a6dcf39a88f77e380b868.jpg)  
Fig, 11. The relationship between manufacturer's commission payments, retailer's trust value and total expected utility with the cost rate of $C R = 0 . 5 .$

![](/api/attachments/ATZH979H/fulltext/images/4c51665365c573b47ccbb8e1b042f783da1b5f035015bd6cac18c746baa96d2e.jpg)  
Fig. 12. Cost rate and trust with selfish agent.

Observation 2. A benevolent agent's prediction accuracy exerts more influence on the trust value than the credit standing does.

When the agent is benevolent, the increment $\theta = 0 ,$ and the case is of a relatively long period $( T = 6 0 )$ , the different cost rates under the same prediction level have no big influence on the trust value. So we assume $C R = 2$ and analyze the relationship between the initial trust value $w _ { 0 }$ and the trust value w. In the three sub-figures of Fig. 4, five curves represent the initial trust values 0.1, 0.25, 0.5, 0.75, and 0.95, respectively. From Fig. 4, credit standing's influence on the trust value is not greater than the predictive accuracy's, since the retailer can automatically adjust the trust value of the transactions in later periods and accordingly adjusting the POQ. Although the initial credit standing has a certain effect on trust for a short period, after a long-term transaction $( T = 6 0 )$ the trust value is mainly influenced by the agent's predictive accuracy.

In the case of a relatively short period (T ≤ 24), the agent's initial trust value $W _ { 0 }$ equals to 0.1, and while this prediction is more accurate, the retailer's trust value has only changed a little bit. Only after a longer period $( T > 2 4 )$ will the retailer's trust value have a big change. It will take a long time for a bad credit agent to gain trust back through successful transactions.

In the case of a relatively long period $( T = 6 0 )$ , the agent's initial trust value is 0.95 and as the retailer's prediction is more accurate than the agent's the retailer's trust value will gradually decrease. It indicates that even if there are many deceptions from the agent with quite a good credit standing in the transactions for a long period, the retailer's trust value towards her can gradually decrease.

The changes of the total utility and increment under selfish agent's different credit standings.

<table><tr><td>θ (%)</td><td>0.10</td><td>0.50</td><td>10.00</td><td>15.00</td><td>20.00</td><td>30.00</td><td>40.00</td></tr><tr><td> $W_0 = 0.1$ </td><td>1.089</td><td>1.094</td><td>1.093</td><td>1.103</td><td>1.101</td><td>1.106</td><td>1.109</td></tr><tr><td> $W_0 = 0.25$ </td><td>1.067</td><td>1.088</td><td>1.106</td><td>1.096</td><td>1.101</td><td>1.102</td><td>1.107</td></tr><tr><td> $W_0 = 0.5$ </td><td>1.069</td><td>1.114</td><td>1.122</td><td>1.100</td><td>1.096</td><td>1.096</td><td>1.098</td></tr><tr><td> $W_0 = 0.75$ </td><td>1.049</td><td>1.110</td><td>1.141</td><td>1.112</td><td>1.097</td><td>1.090</td><td>1.091</td></tr><tr><td> $W_0 = 0.95$ </td><td>1.013</td><td>1.080</td><td>1.146</td><td>1.145</td><td>1.110</td><td>1.089</td><td>1.095</td></tr></table>

![](/api/attachments/ATZH979H/fulltext/images/afa833fb4f222d059723ce3d55507650e4d0515c84cf193869e8f0bba974e2de.jpg)  
Fig. 13. The total utility and increment under selfish agent's different credit standings

Observation 3. The more accurate a benevolent agent's prediction is, the higher the total expected utility she earns.

When $C R = 2 , \sigma s / \sigma r = 0 . 4 ,$ and $T = 6 0$ , we analyze the relationship between the total expected utility U and the increment θ of the benevolent agent's ROQ. In the case of different initial trust values, the changes of the total expected utility U (unit 10<sup>4</sup>) according to the changes of the increment θ of the agent's ROQ are shown in Table 1. We can find when the range of θ is between 2% and 3%, the total expected utility is maximized.

From Fig. 5, we can see that the total expected utility, with the increase of the increment of the benevolent agent's ROQ, firstly rapidly increases and then slowly decreases. But the total expected utility will always reach the maximal point when the increment $\theta \leq 3 \% ,$ regardless of the initial trust value. Since the purpose of the benevolent agent is to establish a long-term cooperative relationship with the retailer, he mainly considers how to make the retailer's trust value remain at a high level $( W > 0 . 9 )$ , and how to maximize the retailer's profit. Thus the agent's lying level will be very low, or in other words, the increment of the agent's recommended quantity will be a relatively small value.

When CR = 2, W = 0.5, and T = 60, we analyze the relationship between the total expected utility U and predictive accuracy. Fig. 6 shows that there is a clear gap between the case of the agent predicting more accurately and the case of the retailer predicting more accurately. But when the agent predicts more accurately than the retailer, the total expected utility will be greater. This indicates that the predictive accuracy has an apparent influence on the total expected utility.

Observation 4. A benevolent agent can adopt the “first slowly increasing increment in order to obtain the trust of the retailer, later suddenly expanding the increment” approach to obtain the maximal total expected utility.

When $C R = 2 , \sigma s / \sigma r = 0 . 4 ,$ and $T = 6 0$ , we study the relationship between the increment θ, time T, and trust value w. In the case of different initial trust values, the changes of the retailer's trust value according to the changes of the increment θ of the agent's ROQ are shown in Fig. 7. When $\theta < 1 0 \% ,$ the trust value always stays at a high level (T N 0.5).

Fig. 7 shows how after 60 periods the increment $\theta = 1 0 \ \% ,$ the retailer's trust value can always reach the maximal point regardless of the initial trust value. Meanwhile, when the trust values are at the same contour line the values will change if the increment θ of the agent's ROQ changes. So the benevolent agent can adopt this strategy to get the maximum total expected utility. In the early period of transaction $( T > 6 0 )$ , the increment of the agent's ROQ can slowly increase. In order to keep the trust on a high level, the upper limit of the increment is 10%. In the later period of transaction $( T < 6 0 ) ,$ , the agent can suddenly increase the increment to increase the total expected utility. At this situation, the increment will locate in the range [10%, 15%].

![](/api/attachments/ATZH979H/fulltext/images/a54d89f6dcb1c49ec782105921c6227b895227dd43356140729bb4db630bee59.jpg)

![](/api/attachments/ATZH979H/fulltext/images/17a2ee3f79878c18ab329b841709f9b255c42a7e350e9993c759502c3fc36422.jpg)

![](/api/attachments/ATZH979H/fulltext/images/7f6a2c7fe4fe397e12f0e44833616f6d03b62cccafecf45210d38afea5a03742.jpg)  
Fig. 14. The relationship between trust, increment and period under selfish agent's different cost rates.

In practice, for example, BMW dealer in China (the benevolent agent), who wants to improve her trust level in the market, needs to improve her prediction accuracy concerning the market demand in the first place. It has been observed from experiments that prediction accuracy has greater effect on the trust level than cost rate and initial credit standing, thereby affecting the total utility. To maintain a good credit standing already obtained, the benevolent agent needs to utilize her competence in accurate prediction and slowly raise the order quantity to obtain the trust of the downstream retailer. When the trust stabilizes at a fairly high level, the agent can increase appropriately the increment to maximize the total profits.

## 5.2. Self-serving agent

We believe that the selfish agent will report a higher ROQ and try to lead the retailer to expand the FAOQ. The near-sighted selfish agent will provide as large of a ROQ as possible without taking the retailer's trust into consideration. The far-sighted selfish agent will first balance his own profits and the retailer's trust value, and then only at the right time in later transactions will he expand the ROQ. So the complex case of the selfish agent is analyzed in this section.

Observation 5. In the case of the selfish agent, the more accurate the retailer's prediction is, the more rapidly the trust value decreases.

The changes of trust and increment under selfish agent's different credit standings.

<table><tr><td>θ (%)</td><td>0.10</td><td>0.50</td><td>10.00</td><td>15.00</td><td>20.00</td><td>30.00</td><td>40.00</td></tr><tr><td> $W_0 = 0.1$ </td><td>0.26</td><td>0.16</td><td>0.11</td><td>0.06</td><td>0.05</td><td>0.03</td><td>0.03</td></tr><tr><td> $W_0 = 0.25$ </td><td>0.92</td><td>0.70</td><td>0.28</td><td>0.10</td><td>0.06</td><td>0.04</td><td>0.03</td></tr><tr><td> $W_0 = 0.5$ </td><td>1.00</td><td>0.94</td><td>0.56</td><td>0.13</td><td>0.07</td><td>0.05</td><td>0.04</td></tr><tr><td> $W_0 = 0.75$ </td><td>1.00</td><td>1.00</td><td>0.76</td><td>0.26</td><td>0.08</td><td>0.05</td><td>0.04</td></tr><tr><td> $W_0 = 0.95$ </td><td>1.00</td><td>1.00</td><td>0.93</td><td>0.53</td><td>0.12</td><td>0.05</td><td>0.04</td></tr></table>

When the agent's selfish variable is $\alpha = 1$ , the agent's loyal variable equals to $\alpha = 1$ , and the initial trust value is $w _ { 0 } = 0 . 5$ , the period is $T = 2 4$ . When the cost rate is $C R = 2 ,$ , the sensitivity parameter δ's gaining trust coefficient is $\delta ^ { g } = 0 . 5$ , and the sensitivity parameter δ's losing trust coefficient is $\delta ^ { l } = 1$ , then the relationship between $\sigma _ { s } / \sigma _ { r }$ and trust value w is depicted by Fig. 8. When the selfish agent's predicted demand is more accurate, the retailer's trust value is stable at the state above the initial trust value. Meanwhile, the more accurate the retailer's prediction demand is, the more rapidly the retailer's trust value decreases.

The following curve demonstrates the relationship between the increment θ and the total optimized expected utility U in Fig. 9. The xaxis represents the incremental ratio of each ROQ; the y-axis represents the total optimized expected utility. When the increment θ is 1%, the total optimized expected utility will suddenly increase with θ. But later, the retailer finds that the increment of the agent's ROQ is becoming unreasonably larger and larger, thus the retailer's trust value of the agent gradually decreases. Meanwhile, the total optimized utility starts to decrease gradually. We can know from Eq. (8) that when the trust value decreases to zero, the retailer's ROQ is her optimal POQ. Through Eq. (10), the total expected utility can only be obtained by calculating the retailer's profit. Therein $\sigma s / \sigma r = 0 . 4 .$

Through two simulation experiments, we study the relationships between commission and trust value, as well as commission and total expected utility. The results are depicted by Figs. 10 and 11. We let the prediction accuracies of both agent and retailer be the same, i.e., σ / $\sigma _ { r } = 1$ . In the sub-figures of Figs. 10 and 11, three curves represent the commission payments at 0.5, 0.3, and 0.1, respectively.

When the cost rate CR equals 2, it means that agent sells highmargin products. From Fig. 10, we can see that the more commission is given, the less lies the agent would tell. And the higher the retailer's trust value is, the greater the total expected utility will be.

When the cost rate CR equals 0.5, it means that agent sells lowmargin products. From Fig. 11, we can see that the higher the commission is, the greater the total expected utility will be. However, under the three situations, the retailer's trust values have the same decreasing rate, which indicates that the agent is motivated to tell lies facing low-margin products in order to increase the recommended order quantity.

Observation 6. When the agent's predicted demand is more accurate, the cost rate's influence on the trust value is greater.

![](/api/attachments/ATZH979H/fulltext/images/137597727be8c402c4bd92629c467a1178e129b606b364a6ab0573e7fcc889dc.jpg)

![](/api/attachments/ATZH979H/fulltext/images/db7f9d096dd53c7cdce2276468429e52a58ad1ee05bd96f11daad390a39d39ce.jpg)

![](/api/attachments/ATZH979H/fulltext/images/0d9a8aa7fe74592b5d95dd5a897bf61f96af3e14edd5a4d8617577313766483d.jpg)

![](/api/attachments/ATZH979H/fulltext/images/cc3e63f651a6859990d877cc8b19717fa1395d2a1089a76a36c46358f11c6e18.jpg)

![](/api/attachments/ATZH979H/fulltext/images/bcc58e9d90741cc166cbe55ae2d7e34e499f569ac74e12542c0e66caae0def6e.jpg)

![](/api/attachments/ATZH979H/fulltext/images/c873d06949a829f23e83ed39baacaf9355fc169826e33328a87b08ca079700f7.jpg)  
Fig. 15. The relationship between trust, increment and period under selfish agent's different credit standings.

Fig. 12 represents the relationship between the cost rate $C R = ( p _ { r } -$ $p _ { w } + s _ { r } ) / ( p _ { w } - h _ { r } )$ and the trust value when the initial trust value is $w _ { 0 } = 0 . 5 ,$ , the increment is $\theta = 4 0 ,$ , and T = 60. Fig. 10 shows that when the agent's predicted demand is more accurate than the retailer's $( o s / o r = 0 . 4 \mathrm { a n d } o s / o r = 0 . 6 )$ the cost rate's influence on the trust value is more obvious.

Observation 7. When the cost rate is low, the selfish agent is allowed to appropriately and slightly raise the increment of the ROQ.

When $C R = 2 , \sigma s / \sigma r = 0 . 4 ,$ and $T = 6 0 ,$ , the relationship between the total expected utility and the increment of the selfish agent's ROQ is analyzed. In many cases when the initial trust equals different values, the corresponding total expected utility U (unit 10<sup>4</sup>) and the increment of the agent's ROQ are represented in Table 2.

![](/api/attachments/ATZH979H/fulltext/images/5545f6fba221ea6f684204b0092e48eaaefed9e23dfe06fbaf9ae3679ca1fc79.jpg)  
Fig. 16. The relationship between the utility increment level, loyalty and selfishness variable

As shown in Fig. 13, the total expected utility curve is first in an upward tendency and then a downward tendency along with the increment of the selfish agent's ROQ. When the increment is 10%–15%, the total expected utility is maximized. The main purpose of the selfish agent other than to gain a high level trust value $( W > 0 . 9 )$ is to gain more profits. Therefore, the selfish agent only needs to make the retailer's trust value equal 0.5. This means that there is more room for lying, which also means that there is more space for the increment of the agent's recommended quantity to grow larger.

If the trust values are in the same niveau line within the same period, slightly changing the increment θ of the agent's ROQ will not change the trust value. From Fig. 14, we can see that when the cost rate is relatively small within the same period, the agent can raise the increment of the ROQ, but the trust value of the retailer will still remain unchanged. That is because the increment of the agent's ROQ happens to meet the retailer's increment of the demand caused by a high underage cost and a low cost rate. Thus, the trust value gains an increment in such an unusual way to offset the trust should be decrement.

Observation 8. The selfish agent can use “shortening the transaction period, improving the initial trust value, keeping the increment of the ROQ very small and making a more accurate prediction” approach to obtain the maximal total expected utility.

When $C R = 2 , \sigma s / \sigma r = 0 . 4 ,$ , and $T = 6 0 ,$ , the relationship among the increment θ, the time T, and the trust value w is analyzed. In the cases of different initial trust values, the changes of the retailer's trust value along with the changes of the increment θ of the agent's ROQ are shown in Table 3. Table 3 shows that when the initial trust value is over 0.5 and $\theta < 1 0 \% ,$ the trust value keeps at a higher level $\left( T > 0 . 4 5 \right)$ When the initial trust value is below 0.5, the trust value decreases rapidly $\left( T < 0 . 3 \right)$ . This phenomenon demonstrates that it is impossible for the low credit agent with a high index of telling lies to make further cooperation with the retailer.

Fig. 15 indicates that if the selfish agent with the initial trust value greater than 0.5 wants to make the retailer's trust value remain at 0.5, his optimal increment should be less than 10% of the total demand. At the same time, if the selfish agent wants to make the retailer's trust value remain above 0.9, his optimal increment should be less than 5%. So the selfish agent can adopt the following strategy to increase the expected utility of agent: after shortening the transaction period $( T \leq 2 4 )$ the agent can make a sudden increase of the increment of the ROQ to increase the expected utility of agent. Even at this time the trust value sharply becomes small, and the increment in this case can be greater than 10%. In a fairly long-time transaction period $( T > 2 4 )$ , the agent with a high initial trust value might also set the increment of the ROQ at a low level $( \theta < 5 0 \% )$ . According to Observation 6, improving the agent's predictive accuracy will slow down the retailer's trust value from further decreasing.

In practice, the wine dealer, who cares more about her own profit (the selfish agent), also needs a good credit standing and makes a more precise order quantity prediction, and slowly raises the level of order quantity, to obtain higher profits. However, near-sighted selfish agent would recommend an order quantity as large as she can in the short run without considering the change of retailer's trust value. The trust model proposed in this paper enables the retailer to figure out the agent's speculating act, and therefore, is of value to the retailer. Far-sighted selfish agent will first balance her own profit and the retailer's trust value, and use price control and properly increase the order quantity to maximize her profits.

## 5.3. The optimal agent (find the optimal values of α and β)

When $C R = 2 , o s / o r = 0 . 4 , W _ { 0 } = 0 . 5 ,$ , and $T = 6 0$ , we analyze the relationship between α, $\beta$ and total expected utility U (see Fig. 14). It is shown that: (1) the total expected utility with the agent is more than that without the agent. In other words, even the selfish agent can contribute to the increase of the total expected utility, as the curve demonstrates that the increments of the total expected utility are all more than 105%. (2) The total expected utility increases with the selfish variable, and the total expected utility is more with the benevolent agent than with the selfish agent. (3) In order to maximize the total expected utility, two optimal values of α and β exist. The first one is the case in the upper-left of Fig. 14, which demonstrates that the agent is more concerned about the manufacturer's profit and the benevolent agent can obtain the maximal total expected utility. The second one is the case in the lower left of Fig. 16, which demonstrates that the agent is more concerned about the retailer's profit and the benevolent agent is able to obtain the maximal total expected utility.

## 6. Conclusions

The multi-period information sharing problem in a three-tier supply chain is studied in this paper. In the supply chain, the agent reports a ROQ to the retailer, and the retailer makes the order decision based on the agent reported information and his own estimated demand. The manufacturer is assumed to have enough capacity to satisfy the retailer's order. Because of the asymmetric information, the retailer does not fully trust the agent reported information. Thus, a trust updating model is proposed and is effectively used to evaluate the agent's trustworthiness over periods. It is found that the trust model can dynamically update the retailer's trust and that trust is proven to be inflective of the supply chain partner's decisions. In this paper, the agent can take different roles (benevolent and selfish), and her optimal recommended order strategies are investigated by simulations. The simulation shows that the agent does not need to make a forcible expansion of the order quantity to obtain her maximum utility when the agent is benevolent. The maximum utility of a benevolent agent can be achieved when she gains a high trust level. However, an opportunistic behavior selfish agent is to be punished. It is observed that the retailer's trust on this selfish agent will decease rapidly and a longtime period will be needed to earn back that trust.

In real-world supply chains, an agent usually faces to multiple retailers, so a model of one agent with multi-retailers will be considered in the future. In addition, as information asymmetry may engender the loss of trust, thus another interesting future research direction is to study how information asymmetry affects the trust and its updating process.

## Acknowledgments

This work was supported in part by the Specialized Research Fund for the Doctoral Program of Higher Education of China (20120073110029), Interdiscipline Foundation of Shanghai Jiao Tong University (No. 14X190040048, No. 11JCZ02), National Natural Science Foundation of China (No. 71371123, 71131005), and Europe–China High Value Engineering Network (EC-HVEN Project Number: 295130).

## References

[1] G. Charness, M. Rabin, Understanding social preferences with simple tests, The Quarterly Journal of Economics 117 (3) (2002) 817–869.

[2] M. Carney, The competitiveness of net worked production: the role of trust and asset specificity, Journal of Management Studies 35 (4) (1998) 457–479.

[3] R. Clemen, R. Winkler, Combining probability distributions from experts in risk analysis, Risk Analysis 19 (2) (1999) 187–203.

[4] C.M. Chiu, M.H. Hsu, H. Lai, C.M. Chang, Re-examining the influence of trust on online repeat purchase intention: the moderating role of habit and its antecedents, Decision Support Systems 53 (4) (2012) 835–845

[5] D.J. Kim, D.L. Ferrin, H.R. Rao, A trust-based consumer decision-making model in electronic commerce: the role of trust, perceived risk, and their antecedents, Decision Support Systems 44 (2008) 544–564.

[6] N. Ebrahim-Khanjari, W. Hopp, S.M.R. Iravani, Trust and information sharing in supply chains, Production and Operations Management 21 (3) (2012) 444–464.

[7] G. Elofson, Developing trust with intelligent agents: an exploratory study, Trust and Deception in Virtual Societies1998 125–139.

[8] H. Fang, G. Guo, J. Zhang, Multi-faceted trust and distrust prediction for recommender systems, Decision Support Systems 71 (2015) 37–47.

[9] S. Ganesan, Determinants of long-term orientation in buyer–seller relationships, Journal of Marketing 58 (4) (1994) 1–19.

[10] W. Hopp, S.M.R. Iravani, Z. Liu, The role of wholesale-salespersons and incentive plans in promoting supply chain performance, Working Paper, 2010.

[11] A. Jøsang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision Decision Support Systems 43 (2007) 618–644

[12] A. Jøsang, S. Presti, Analyzing the relationship between risk and trust, Trust Management 2995 (2004) 135–145

[13] C. Jonker, J. Treur, Formal analysis of models for the dynamics of trust based on experiences, Multi-agent System Engineering Lecture Notes in Computer Science 1647 (1999) 221–231.

[14] S.A. Johnson, M.B. Houston, Buyer–supplier contracts versus joint ventures: determinants and consequences of transaction structure, Journal of Marketing Research 37 (1) (2000) 1–15.

[15] D.H. McKnight, N.L. Chervany, The meanings of trust, Working Paper, 1996.

[16] R.M. Morgan, S.D. Hunt, The commitment–trust theory of relationship marketing Journal of Marketing 58 (1997) 20–38.

[17] V. Midha, Impact of consumer empowerment on online trust: an examination across genders, Decision Support Systems 54 (2012) 198–205.

[18] J. Ousterhout, Virtual roundtable, Internet Computing On-line Journal (1997) (July-August issue).

[19] Ö. Özer, Y.C. Zheng, K.Y. Chen, Trust in forecast information sharing, Management Science 57 (6) (2011) 1111–1137.

[20] K. Özpolat, W. Jank, Getting the most out of third party trust seals: an empirical analysis, Decision Support Systems 73 (2015) 47–56.

[21] P.M. Doney, J.P. Cannon, An examination of the nature of trust in buyer–seller relationships, The Journal of Marketing 61 (2) (1997) 35–51.

[22] S. Paul, Risk perception and trust, Fundamentals of Risk Analysis and Risk Management. , Lewis Publishers, Boca Raton, Fl., USA, 1997 233–245.

[23] Z.J. Ren, M.A. Cohen, T.H. Ho, C. Terwiesch, Information sharing in a long-term supply chain relationship: the role of customer review strategy, Operations Research 58 (1) (2010) 81–93.

[24] F. Selnes, Antecedents and consequences of trust and satisfaction in buyer–seller relationships, European Journal of Marketing 32 (3/4) (1995) 305–321

[25] M. Stone, The opinion pool, Annals of Mathematical Statistics 32 (4) (1961) 1339–1342.

[26] T.A. Taylor, E.L. Plambeck, Supply chain relationships and contracts: the impact of repeated interaction on capacity investment and procurement, Management Science 53 (10) (2007) 1577–1593.

[27] A. Wierzbicki, T. Kaszuba, R. Nielek, P. Adamska, A. Datta, Improving computational trust representation based on Internet auction traces, Decision Support Systems 54 (2013) 929–940.

[28] LS. Wrightsman, Interpersonal trust and attitudes toward human nature, Measures of Personality and Social Psycho-logical Attitudes vol, 1 Academic Press, San Diego CA 1991.

Xiao Fu is a Ph.D. candidate in Antai College of Economics & Management, Shanghai Jiao Tong University. He received his Master degree in Software Engineering from Shanghai Jiao Tong University. His research deals with trust issues in supply chain management, supply chain finance and risk management.

Ming Dong is a Professor in the Department of Operations Management, Antai College of Economics & Management, Shanghai Jiao Tong University. He received the M.S. and Ph.D. degrees from Tianjin University, Tianjin, China, respectively, all in mechanical engineering, and the Ph.D. degree in industrial engineering from Virginia Polytechnic Institute and State University. His research and teaching interests are in the areas of data-driven decisions, operations optimization and supply chain management.

Shaoxuan Liu is an Associate Professor in the Department of Operations Management, Antai College of Economics & Management, Shanghai Jiao Tong University. He received his Ph.D. degree in Operations Management from The Paul Merage School of Business, University of California, Irvine. His research and teaching interests are in the areas of decision support and operations management.

Guanghua Han is an Assistant Professor in the School of International and Public Affairs Shanghai Jiao Tong University. He has published research articles in international journals such as International Journal of Production Research and International Journal of Production Economics. His current research activities focus on behavior analysis in information sharing.
