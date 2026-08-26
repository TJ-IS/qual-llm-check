---
otero_id: 26923
otero_key: "7ESFSJ6R"
title: "Identity Management and Tradable Reputation1"
authors: "Hong Xu; Jianqing Chen; Andrew B. Whinston"
year: "2018"
journal: "MIS Quarterly"
doi: "10.25300/misq/2018/13634"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identity Management and Tradable Reputation

Hong Xu<sup>†</sup>, Jianqing Chen<sup>‡</sup>, Andrew B. Whinston<sup>∗</sup>

Forthcoming in MIS Quarterly, June 2018

## Abstract

Online reputation trading is a new phenomenon facilitated by the prosperity of e-commerce and social networks. Whether reputations will be reliable when people can purchase rather than build them originally is a natural concern and also a challenge to online marketplaces. In the present study, we examine a reputation market in an infinitely repeated game setting, where agents sell products and trade their online reputations. Agents exert efort to provide products, and their reputations are updated based on consumer feedback. High-type agents have a lower cost of efort than low types. In addition to reputation system, we consider products that are randomly audited, and agents do not receive payment for products that fail the audit. Our analysis depicts a separating equilibrium: high-type agents can be sorted out from low-type agents by their reputations, which contrasts with the results in Tadelis (2002). In a separating equilibrium, reputations become a perfect indicator of agents’ types, efort levels, and product quality. We demonstrate the key role of auditing in separating diferent types of agents, and reveal the substitution efect between auditing frequency and harshness of reputation systems. We also study the design of the reputation system and the audit mechanism in order to achieve diferent equilibria in the reputation market. By proposing online reputations as an asset, our paper generates implications for establishing reliable online environments and promoting efective online interactions. Keywords: reputation, online community, audit, identity management, electronic market

## 1. Introduction

One of the most important characteristics of online environments is anonymity. Online users talk, write, buy, and sell behind the mask of online identities. As summarized by a New Yorker cartoon in 1993, “On the Internet, nobody knows you’re a dog.” With the lack of face-to-face, personal, and recurring interactions, reputation has become a widespread mechanism to regulate individuals online activities and, most importantly, to accommodate the prosperity of electronic commerce. eBay credits its success in consumer-to-consumer business to its feedback system, which allows sellers to establish a reputation through buyers’ feedback. In the present paper, we examine a relatively new phenomenon, reputation trading, and its impact on both sellers’ behaviors and the informativeness of online reputations.

Reputation trading is essentially enabled by online anonymity. For example, a reputation on eBay is simply a record of past activities, and selling such a reputation requires only the exchange of the account and associated password for money. Note that the exchange of reputations does not involve transferring the quality resources that belong to the sellers. A new owner of a reputation brings in his own quality resources that may be diferent from the previous owner’s. Therefore, reputation trading poses a new challenge to online consumers; that is, to what extent can consumers expect consistent quality from a certain level of reputation? Meanwhile, this new phenomenon also brings up a few theoretical questions. First, what are agents’ reputation choices and efort choices when a reputation market exists? In other words, will incapable agents take advantage of the reputation market to purchase good reputations and cheat on consumers with low quality products? Second, how should the reputation system be designed in order to induce favorable agents’ behaviors in the reputation market and product market? We aim to demonstrate the benefits of reputation trading to the reliability of online reputations, and we also ofer a unique angle of designing an online reputation system to regulate sellers’ cheating behaviors.

Reputation trading takes place in many diferent forms. We have observed people selling their eBay accounts through online classifieds, and an account with a distinguished feedback profile can be sold for thousands of dollars.<sup>12</sup> Potential reputation buyers may also initiate the trading by specifying on freelancing websites the level of reputation they want<sup>3</sup> and invite freelancers to bid on the price of building such a reputation. For Taobao.com, the largest consumer-to-consumer online marketplace in China, various platforms have been created for users to trade their sellers’ accounts.<sup>4</sup> Even in social communities such as Twitter, users nowadays can easily find out the monetary worth of their accounts through websites like SocialSellouts, SNpros, and Twirth. Reputation trading also happens in our ofline life under certain circumstances. Restaurants experience shifts of ownership or chef, while maintaining the same restaurant name and reputation (Tadelis 2002). Movie producers implicitly “purchase” stars’ reputations, so as to increase their movies’ publicity. Mutual fund companies may close funds with a bad reputation and start a new fund containing the same investment portfolio under a new name. The private equity industry also provides a great model of reputation trading, since private equity firms often take over companies while keeping their brand names and replacing the management team.

Reputation trading facilitates a more eficient online community in several aspects. First, reputation, as a resource, can be better allocated in a reputation market, which can improve market eficiency. Good reputation in online communities is often related to a better belief regarding the user, such as selling high-quality products on eBay, being an influential user on Twitter, or posting insightful content on Slashdot. Without a reputation market, all users must start a business with a new reputation, which is generally discounted by the community. With a reputation market, users have the option to buy a reputation that matches their capabilities. Second, a reputation market serves as a medium to reward good reputation and good online behavior. A common concern for online reputations is the dificulty of punishing misbehaving users: downgrading a user’s reputation incurs only indirect punishment to the user; furthermore, the user also has the option to abandon the bad reputation and create a new account at no cost. However, with a reputation market, users experience a price drop once their reputations get downgraded, and this monetary loss imposes a direct punishment on their misbehavior. In addition, a reputation market acts as a succession plan for users. When existing users decide to leave the community, in the absence of reputation market they may have the incentive to exploit their established good reputations before leaving, because there is no other way to benefit further from them. A reputation market can eliminate such end-of-game efect, because users can sell their good reputations, incentiving them to improve or maintain their reputations until the last minute.

However, a reputation market can undermine the reliability of a reputation mechanism if it does not separate low-type agents from high-type agents. For example, if a low-type seller purchases a good reputation in the market, future buyers might pay high price due to the good reputation, while receiving low quality products because the low-type seller is not motivated to provide good quality products. A non-separated market can lose consumers’ trust, since sellers with a good reputation can be incapable of satisfying consumers’ expectation for that reputation. As a remedy, in practice, online marketplaces often employ diferent additional warranty policies to mitigate the uncertainty facing consumers. For example, eBay buyers can obtain refunds under eBay’s Money Back Guarantee, provided the products are not-as-described, damaged, or have not been received. A warranty policy imposes a contingent contract between sellers and buyers, and grants buyers the option to audit product quality and make payments based on their audit results. We use the term auditing to refer to any mechanism that imposes a contingent contract between sellers and buyers in an online marketplace, such as the commonly observed warranty policies in online marketplaces, which is seen to give sellers incentive to exert efort in order to receive payment.

In this paper, we consider the online world as a community with high and low types of agents, who have diferent capabilities to exert efort to fulfill the role as an online seller. We examine a reputation market in an infinitely repeated game setting, where agents sell products and trade their online reputations. Agents exert efort to provide products, and high-type agents have a lower cost of efort than low types. Products are randomly audited, and agents do not receive payment for products that fail the audit. Reputations are determined by consumer feedback, and reputation trades occur at the beginning of each period. Under this setting, we investigate potential equilibrium scenarios based on agents’ choices of reputation and the efect of auditing and reputation measure on the equilibrium outcome.

One of our key findings is that a reputation market can lead to an equilibrium where high-type agents choose high reputations, and low-type agents choose low reputations. In this scenario, reputations of the same level deliver products with consistent quality, despite the fact that these products may be produced by diferent sellers. Furthermore, reputations become perfect indicators of sellers’ capabilities, because consumers know the true type of a seller by observing his reputation. In addition, we illustrate the key role that auditing plays in separating agents: for a commonly observed reputation measure, no separation can be sustained as equilibrium without auditing; separation can occur only under properly designed auditing policy. Further analysis reveals the substitution relationship between auditing frequency and harshness of reputation systems in separation: both auditing and reputation regulate agents in the marketplaces and provide them incentive to exert suitable efort; increasing auditing frequency or increasing harshness of reputation measure can be used as substitutes for inducing separation.

Under the separating equilibrium, both the auditing frequency and reputation measure afect agents’ efort choices. Increasing auditing frequency can increase high-type agents’ efort, while decreasing low-type agents’ efort. In the meantime, sellers’ reputation and efort choices are also afected by how the reputation system evaluates their successes and failures. A strict reputation system where failures are heavily punished through reputation downgrades, or successes are rarely rewarded through reputation upgrades, not only directly motivates sellers for efort, but also imposes an indirect impact on sellers’ eforts through the market value of reputations. Lastly, increasing the proportion of high-type sellers in the market leads to higher efort from both types of sellers.

Our study contributes to the literature in several ways. First, our study provides a roadmap for discussing the benefits of reputation trading to online communities. Previous studies have already established that a market for reputations is sustainable but, in the meantime, concluded that good reputations may be purchased by low-type sellers (Tadelis 1999, 2002). Our study takes this stream of research one step further and demonstrates that the market is not only sustainable but also beneficial to both consumers and sellers. In our separating equilibrium, consumers face little uncertainty or risk in making purchases because the reputations are reliable enough to give them precise information on agents’ types. Besides, high-type sellers can efectively distinguish themselves from the low-type sellers, and their high eforts can be properly rewarded through high payment from the consumers. Second, our model has included several unique aspects of online reputations; therefore, we are able to ofer suggestions to a market owner on how to achieve the desirable outcome. Online marketplaces often have multiple mechanisms in place to motivate their sellers. One such common mechanism is a warranty policy that assures buyers a refund upon sellers misbehaviors and, in turn, influences sellers’ strategies. Our results show the importance of having a warranty policy as well as the diferent scenarios that may occur when a warranty policy favors

the buyers or the sellers.

Our study also contributes to the literature by proposing a solution to the end-of-game efect in repeated games. Holmstrom’s career concern model (Holmstrom 1999) depicted a scenario where agents are concerned about their future careers when determining their current period efort, and the concern disappears at the end of the agent’s life horizon. The same issue persists with online reputation, and sellers have incentive to cheat on buyers before they leave the online community for various reasons. In our model, reputations become a tradable asset, and agents are concerned about their future in every period. Agents’ eforts contribute to the reputation they carry for that period, and the contribution can be converted into payment by selling the reputation. Therefore, agents are motivated to work hard as long as they are in the product and reputation market. Even on the day they decide to retire and leave, they will behave as if they are still concerned about the future. Meanwhile, the potential for agents with high reputations to misbehave and then return to the market with a new name (Friedman and Resnick 2001) is also eliminated with reputation trading. Misbehavior incurs a loss in reputation value, which is essentially a punishment, especially for those with high reputations. In fact, agents in our model are motivated to exert higher efort at higher reputations, which consumers rationally expect.

The rest of the paper is organized as follows: We present a review of related literature in the following section. In Section 3, we introduce our main model, and in Section 4 we analyze the equilibrium outcomes. In Section 5, we examine a more complicated reputation system to demonstrate that our results are robust to diferent reputation systems. We conclude in Section 6 with comments on the implications of our results, as well as future directions.

## 2. Literature Review

Studies on reputations in information systems have contributed greatly to understanding the role of reputation in sustaining online trust and improving online economic eficiency. Previous research has shown that a good reputation that is accumulated over time in the form of text comments and rating scores can increase consumers’ trust in e-commerce transactions (Chellappa 2012; Yang et al. 2007; Pavlou and Dimoka 2006) and create price premium for online sellers (Ba and Pavlou 2002). It has also been shown that the eficiency of an online market is always bounded away from the first-best case since sellers cannot credibly commit to the first-best efort level under a reputation mechanism (Dellarocas 2005). Furthermore, many existing reputation systems fail to provide sustained incentives for sellers to behave honestly (Fan et al. 2005). Our paper aims to improve the online economic eficiency by proposing a reputation market in which agents can buy and sell their reputations. We show that a reputation market can enhance the credibility of reputation since a failure for sellers to fulfill their commitment results in a loss in their reputations’ market value.

Our model of reputation as an infinite repeated game follows the economic literature (Kreps et al. 1982; Fudenberg and Levine 1989, 1992). A large body of economic literature on reputation has focused on the incentive issue in the choice of reputation (Friedman and Resnick 2001; Mailath and Samuelson 2001) or the long run performance of reputation (Cripps et al. 2004). These studies share the common critical assumption that a long-lived agent exists and bears the reputation. In our examination of a reputation market, this assumption is relaxed since reputation experiences constant change of ownership: Before one short-lived, high-type agent leaves the market, she can sell her reputation and, thus, it carries on with another agent. Moreover, our separating equilibrium guarantees that the new owner of the reputation is the same type as the leaving agent, so the activities of that reputation will be consistent after the agent leaves. These two properties ensure that in our separated reputation market, the features of reputation defined in previous studies continue to hold with short-lived agents.

Our study also presents a unique contribution to the literature on reputation trading, by showing that reputations can be reliable and deliver consistent performance when there is an audit. Mailath and Samuelson (2001) examined the situation of reputation replacement, where one agent can sell reputation to a group of competitive buyers at the end of a period. They focused on the price of reputation as determined by competition. The idea of a reputation market can be viewed as the generalization of reputation replacement to multiple sellers and multiple buyers. Tadelis (2002) raised the notion of a reputation market in the context of ownership change for restaurants and established that a market for reputation is sustainable. However, the aforementioned study also concluded that it is not possible to sort out diferent types of agents when restaurant names can be traded; therefore, consumers will experience inconsistent quality from the same restaurant after the takeover of a new owner. Our present paper is the first to demonstrate the existence of a separating equilibrium in a reputation market. Under separation, consumers can expect consistent performance from the same level of reputation, despite the ownership change. We achieved this by introducing a random audit scheme that checks on agents’ performance and imposes a contingent contract based on the audit outcome. Such contingent contracts, such as return policies or buyer protection program, are commonly observed on e-commerce websites nowadays. They can efectively reduce low-type agents’ incentive to purchase a good reputation and cheat, while increasing high-type agents’ incentive to work hard. They also allow us to achieve a separation of agents in the reputation market. Furthermore, in contrast with Xu et al. (2008), we not only demonstrate separation under various reputation mechanisms, but also investigate the essential components of a reputation mechanism that are critical to induce separation. Thus, this paper also generates insights new to the design of reputation systems in online communities.

## 3. Model

We consider an infinitely repeated game with two entities, agents and consumers, and two markets, a reputation market and a product market.

There is a continuum of agents. Each agent exerts efort to produce one unit of product in each period. The quality of the product is determined by an agent’s efort level. To exert a certain level of efort, some agents incur a higher cost, whereas others have a lower cost. We call the former type of agents the low type, and the latter the high type. To produce a product with efort w, a low-type agent incurs cost $k _ { l } w ^ { 2 }$ , and a high-type agent incurs cost $k _ { h } w ^ { 2 }$ , where $0 < k _ { h } < k _ { l } < 1$ The resulting product has a probability of w to be successful, and ${ 1 - w }$ to be a failure. We assume that $\lambda _ { h }$ of the agents are high types, and $\lambda _ { l }$ are low types, where $\lambda _ { h } + \lambda _ { l } = 1$ . In the case that existing agents may leave and new agents join the market, we assume the inflow and outflow of agents are equal and the proportions of high type and low types stay the same over time. Agents types are their private information.

Each agent is represented by an online identity in the product market, and has a reputation, j, associated with the identity. We assume that online identities with the same reputation level are treated as the same by the consumers; hence, we use the terms “online identity” and “reputation” interchangeably throughout the paper. Agents can trade reputations by exchanging the associated

online identity login information.

Consumers are homogeneous and risk-neutral. They benefit with value 1 from a successful product, and with 0 from a failed product. Because consumers cannot observe the product quality or the agents’ types, they determine their willingness to pay according to agents’ reputation levels. We denote $\tilde { w } _ { j }$ as the expected efort from an agent with reputation $j ,$ , which is also the expected success rate of the product and consumers’ willingness to pay. Following Tadelis (1999), we assume the price for a product is determined competitively and consumers are on the long side of the product market; that is, the measure of the continuum of the consumers is larger than the measure of the continuum of the agents. In a market with greater demand than supply, buyers pay their willingness-to-pay and thus the equilibrium price will be $\tilde { w } _ { j }$ . After receiving and consuming the product, consumers give positive feedback for successful product, and negative feedback for a failed product.

A reputation system records and evaluates all feedback each agent has received and provides an overall evaluation as “Good” (g) or “Bad” (b); that is, $j \in \{ g , b \}$ . At the end of each transaction, each agent’s reputation is reevaluated and updated according to their current reputation and the newly received feedback, following a set of transition rules: $p ( g | g , + ) = 1 , p ( b | g , - ) = p _ { g b } \in [ 0 , 1 ]$ ， $p ( b | b , - ) = 1$ , and $p ( g | b , + ) \stackrel { } { = } p _ { b g } \in [ 0 , 1 ]$ . Specifically, $p ( g | g , + )$ refers to the probability that a Good reputation remains Good after an additional positive feedback, and $p ( b | g , - )$ is the chance of a Good reputation being downgraded to a Bad reputation after a negative feedback. The other two transition rules can be interpreted in a similar fashion. We interpret $p _ { g b }$ as the system’s tolerance to failures, and $p _ { b g }$ as the strictness of the system in granting Good reputations. In the special case of $p _ { g b } = p _ { b g } = 1$ , an agent’s reputation is simply based on the feedback from the most recent period; that is, if the feedback from the recent period is positive (negative), an agent’s reputation becomes Good (Bad), regardless of its current reputation status. In that case, the reputation system has no tolerance for failures and grants Good reputations easily since it remembers only the most recent feedback. We let $p ( g | g , + ) = 1$ and $p ( b | b , - ) = 1$ because the additional feedback received enhances the current assessment.

Notice that agents within the same reputation category may have diferent feedback profiles (such as the number of positive and negative feedback, or the details of the feedback). We assume that users share the same belief about transitions between the two reputation categories, because users often lack the expertise or resources to process a large amount of feedback, or they may not know the exact criteria the system uses to evaluate them.<sup>5</sup>

In the product market, each product ex post might be verified with probability α. If the product is verified as a failure, the payment will be revoked. We call such verification an audit scheme, which essentially imposes a contingent contract between sellers and buyers, and the term audit can refer to any procedure in a marketplace that imposes quality control and regulates sellers. For example, the audit can be carried out by buyers themselves through product returns or a money-back-guarantee policy. The audit probability α reflects characteristics of the products, the buyers, and the product market. When the product is relatively cheap, some buyers choose not to request a refund, even when they are unsatisfied with the products, because of the cost involved—for example, the time and efort to supply evidence of the unsatisfactory product, arranging a shipment to send the item back, and sometimes even the shipping cost for the return. The return or refund policies in an online marketplace can also afect whether a buyer initiates an audit. For instance, eBay allows its sellers to include as many as 100 restrictions limiting a buyer’s eligability to file for a refund. The more restrictions there are, the less likely a refund takes place, which leads to a lower α. Furthermore, α also varies for diferent products, depending on how costly it is to verify the quality. For instance, electronics and clothing serve as two very diferent categories in this aspect. It is generally easier to verify whether the quality of a digital camera is as described. The quality of a piece of clothing, on the other hand, is highly subjective to the buyer’s judgment in terms of the fabric quality, the fit, or the color, and is dificult to verify.

In the reputation market, agents can sell their existing reputation and purchase another reputation from others. We denote the price for reputation j as v<sub>j</sub>. Trade of reputation occurs at the beginning of each period, before an agent conducts a transaction in the product market. In certain cases, an agent may find it more beneficial to continue with his existing reputation, which can be deemed as buying its own reputation. With reputation trading, in addition to choosing its optimal efort level, each period an agent optimally buys a reputation to maximize its profit, considering the payment for the product produced from the period and market price of the reputation at the end of the period.

The time line of events in each period is as follows. At the beginning of each period, agents choose their reputation levels by trading their identities in the reputation market. Based on its reputation decision, an agent then chooses the efort level to produce a product. The products are sold on the product market to consumers at their willingness to pay $\tilde { w } _ { j }$ , for products from reputation $j \in \{ g , b \}$ . With probability α, an audit occurs. If a product fails an audit, the payment is revoked. At the end of the period, consumers provide their feedback on whether the product is successful, and agents’ reputations are updated accordingly.

We are concerned with a steady state equilibrium, in which agents’ equilibrium efort $w _ { j }$ and reputation values $v _ { j }$ do not vary across all periods. Steady state allows us to focus on the influence of the reputation market on the product market in the long run. While both markets experience adjustments in agents’ behaviors before they arrive to a steady state, it is not in our interest to examine such temporary efects. We denote $\beta$ as the discount factor. Under the steady state, we can formulate a θ-type agent’s expected payof from purchasing a Good or Bad reputation for one investment cycle—starting from purchasing a reputation in the current period to selling the reputation the next period as follows, $\theta \in \{ h , l \}$ :

$$
\pi_ {\theta} = \max \left\{\pi_ {\theta g}, \pi_ {\theta b} \right\} = \max _ {j \in \{g, b \}} \left[ \max _ {w \in (0, 1)} \alpha w \tilde {w} _ {j} + (1 - \alpha) \tilde {w} _ {j} - k _ {\theta} w ^ {2} + \beta V _ {j} (w) - v _ {j} \right],\tag{1}
$$

where $V _ { j } ( w )$ is the agent’s expected value of its reputation at the end of the period when the starting reputation is $j ,$ which is a function of its efort level w and can be defined as

$$
V _ {j} (w) = \left\{ \begin{array}{l l} [ 1 - (1 - w) p _ {g b} ]   v _ {g} + (1 - w) p _ {g b} v _ {b} & \text { if } j = g \\ w p _ {b g} v _ {g} + (1 - w p _ {b g}) v _ {b} & \text { if } j = b \end{array} \right..\tag{2}
$$

At the beginning of each period, an agent faces an investment decision of whether to invest in a Good or Bad reputation: with an initial investment $v _ { j }$ on reputation $j ,$ , the agent receives returns from both selling product and the change in reputation value. The first term on the right-hand side of Equation (1) is an agent’s expected payment if its product gets audited and passes. Note that, when its product fails the audit, an agent receives 0 payment. The second term is the expected payment when its product is not audited. The third term is the agent’s cost of efort. The fourth term is the expected value of its reputation at the end of the period discounted by $\beta ,$ since the objective is formed at the beginning of the period. The last term is the price an agent pays to obtain its reputation at the beginning of the period. When an agent continues to use its own reputation from the previous period, the cost can be deemed as the opportunity cost. In other words, an agent keeping its own reputation is interpreted as selling the reputation to itself. Note that, while the last term does not afect an agent’s choice of efort w, it proves critical in an agent’s reputation choices, as we shall demonstrate later in the equilibrium analysis.

The expected value of a reputation at the end of the period, $V _ { j } ( w )$ , is derived based on the possible changes in the reputation. For example, when the agent chooses a Good reputation and exerts efort w, with probability $1 - w .$ , he generates a failure product and receives a negative feedback, upon which with probability $p _ { g b }$ its Good reputation will be downgraded to a Bad reputation. In other words, the probability for this agent to have a Bad reputation at the end of the period is $( 1 - w ) p _ { g b }$ . When its reputation is not downgraded upon a negative feedback (with probability $( 1 - w ) ( 1 - p _ { g b } ) )$ , or when the agent produces a successful product (with probability w), its reputation remains Good by the end of the period. In other words, the probability for this agent to have a Good reputation at the end of the period is $( 1 - w ) ( 1 - p _ { g b } ) + w = [ 1 - ( 1 - w ) p _ { g b } ]$ ], which leads to $V _ { g } ( w )$ in Equation (2). Similarly, we can derive $V _ { b } ( w )$

It is worth highlighting that Equation (1) characterizes an agent’s optimal investment decision of whether to invest in a Good or Bad reputation for each period, which also characterizes the agent’s optimal reputation and efort choices for its whole life periods. Under steady state, an agent’s investment decision in any investment cycle is independent of its investment decision in the following investment cycle. For example, we consider the investment cycle across periods t and $t + 1$ . At the beginning of period t, whether an agent has a Good or Bad reputation, because the value of its reputation is fixed, the agent faces the same investment decision—whether to invest in a Good reputation or a Bad reputation for production in period t. The expected return until the point of selling its reputation at the beginning of period t + 1 is captured by Equation (1). Then, if we consider the next investment cycle, starting from purchasing a reputation at the beginning of period t + 1 to selling the reputation at the beginning of period $t + 2$ , regardless of the outcome of the previous investment cycle, the agent’s optimal investment decision remains the same as in the previous investment cycle, which is again captured by Equation (1). Therefore, an agent’s investment choice in one investment cycle is independent of the investment choice in the following investment cycle. As a result, maximizing an agent’s payof in each investment cycle (by choosing the optimal reputation and optimal efort) also maximizes the agent’s total payof in its whole life cycle. In other words, an agent’s investment choice is independent of the length of lives for this agent, but rather only depends on the agent’s type and current reputation level.

We assume that $2 k _ { \theta } - 1 > 0$ throughout the paper. When the opposite is true $( \mathrm { i . e . , 2 } k _ { \theta } - 1 < 0 )$ the marginal cost of production is less than consumers’ marginal benefit from the product, even at the highest efort level $w = 1$ , and thus the case becomes trivial. In other words, this assumption allows us to focus on the more interesting case, where agents have incentive to shirk, and it is critical to impose additional mechanisms, such as reputation system and audit, to motivate agents for efort.

## 4. Equilibrium Analysis

In this section, we examine agents’ behaviors in both the product market and the reputation market under diferent equilibrium scenarios. We derive conditions under which various equilibria exist and investigate the impact of the audit and the reputation measure on agents’ strategies. Our main analysis concerns a separating equilibrium, in which a high-type (low-type) agent chooses a Good (Bad) reputation. In this case, the reputation market enhances the reliability of the reputation system because reputations are perfect signals of agents’ types, despite reputation trading. The common concern regarding reputation trading—that incapable agents may purchase Good reputations to fool the consumers—no longer exists. We also extend the analysis to semi-separating equilibria, where reputations reveal partial information about agents’ types.

## 4.1. Separating Equilibrium

We consider the case where high types choose Good reputations and low types choose Bad reputations. If we think of reputations as a resource, this resource is allocated according to agents’ capabilities in a separating equilibrium; that is, Good reputations are allocated to the more capable agents, whereas Bad reputations are allocated to the less capable ones.<sup>6</sup> Furthermore, consumers can directly learn agents’ types from their reputations; that is, agents with Good reputations must be high types, and agents with Bad reputations must be low types. To ensure such allocation of reputations, it is crucial to design an incentive-compatible reputation market such that less capable agents cannot aford Good reputations while more capable agents are not interested in Bad reputations. We denote the equilibrium efort for high-type (low-type) agents as $w _ { h } \mathrm { ~ } ( w _ { l } )$ , and consumers’ willingness to pay for the products from agents with Good (Bad) reputations as $\tilde { w } _ { g } \ \left( \tilde { w } _ { b } \right)$ , which again is consumers’ expected efort from agents with Good (Bad) reputations. We formally define a separating equilibrium below.

Definition 1 A separating equilibrium consists of a set of values $\{ v _ { j } , w _ { j } \} , j \in \{ g , b \}$ that satisfy the following conditions:

(a) Incentive compatibility (IC): choosing Good (Bad) reputations is a dominant strategy for high-type (low-type) agents;

(b) Rational expectations (RE): consumers’ expected efort from agents is equal to agents’ equilibrium efort; that is, $\tilde { w } _ { g } = w _ { h }$ and $\tilde { w } _ { b } = w _ { l } ,$

(c) Market clearance $( M C ) \colon \lambda _ { h } [ 1 - ( 1 - w _ { h } ) p _ { g b } ] + \lambda _ { l } w _ { l } p _ { b g } = \lambda _ { h } .$

Condition (a) states the incentive compatibility conditions for both types of agents; that is, given high types’ choice of efort and reputation, a low-type agent finds it more profitable to choose a Bad reputation than a Good reputation, and vice versa. Condition (b) indicates that consumers’ ex ante belief on efort is consistent with agents’ actual efort decisions in equilibrium. The concept of Rational Expectation has been well established and widely used across diferent disciplines, and is also intuitive to understand: if an agent’s actual efort is lower than consumers’ expected efort, consumers will adjust their willingness to pay for the product in the long run. Condition (c) is a market clearing condition for the reputation market. In other words, the equilibrium level of reputation prices, $v _ { g }$ and $v _ { b } .$ , are determined in such a fashion that the demand for Good (Bad) reputations equals the supply of Good (Bad) reputations. Specifically, the left-hand side is the supply of Good reputations and the right-hand side is the demand. Note that the supply of Good reputations comes from both high and low types of agents.

We first rewrite both types of agents’ objective functions under a separating equilibrium using Equation (1) as

$$
\pi_ {h g} = \max _ {w} \alpha w \tilde {w} _ {g} + (1 - \alpha) \tilde {w} _ {g} - k _ {h} w ^ {2} + \beta [ (1 - (1 - w) p _ {g b}) v _ {g} + (1 - w) p _ {g b} v _ {b} ] - v _ {g},\tag{3}
$$

$$
\pi_ {l b} = \max _ {w} \alpha w \tilde {w} _ {b} + (1 - \alpha) \tilde {w} _ {b} - k _ {l} w ^ {2} + \beta [ w p _ {b g} v _ {g} + (1 - w p _ {b g}) v _ {b} ] - v _ {b}.\tag{4}
$$

We define $v _ { d }$ as the value diference between a Good and Bad reputation; that is, $v _ { d } = v _ { g } - v _ { b }$ We next take high types as an example to illustrate how we can drive the equilibrium. First, the agents’ equilibrium efort level is characterized by the first-order condition of Equation (3) as $\alpha \tilde { w } _ { g } - 2 k _ { h } w _ { h } + \beta p _ { g b } v _ { d } = 0$ , where $\tilde { w } _ { g } = w _ { h }$ in equilibrium according to Condition (b). Applying the same analysis for low types, we have the equilibrium levels of efort from both types as

$$
w _ {h} = \frac {\beta p _ {g b} v _ {d}}{2 k _ {h} - \alpha},\tag{5}
$$

$$
{w _ {l}} = {\frac {\beta p _ {b g} v _ {d}}{2 k _ {l} - \alpha}.}\tag{6}
$$

We define

$$
f _ {h} = \frac {p _ {g b}}{2 k _ {h} - \alpha} \mathrm{and} f _ {l} = \frac {p _ {b g}}{2 k _ {l} - \alpha}\tag{7}
$$

which measure each type’s marginal increase in equilibrium efort because of increase in the reputation value diference. Then we can rewrite $w _ { h } = \beta f _ { h } v _ { d }$ and $w _ { l } = \beta f _ { l } v _ { d } .$

Notice that Condition (c) can be rewritten as $\begin{array} { r } { \frac { w _ { l } p _ { b g } } { ( 1 - w _ { h } ) p _ { g b } } = \frac { \lambda _ { h } } { \lambda _ { l } } } \end{array}$ . Substituting in Equations (5) and (6), we can derive $v _ { d }$ as:

$$
v _ {d} = \frac {1}{\beta (\frac {\lambda_ {l}}{\lambda_ {h}} \frac {p _ {b g}}{p _ {g b}} f _ {l} + f _ {h})}.\tag{8}
$$

With solutions for $v _ { d } , ~ w _ { h }$ , and $w _ { l } .$ , we can revisit Condition (a) to see whether these values are incentive compatible for both types of agents. We take low-type agents as an example. The objective for a low type deviating to purchasing a Good reputation is

$$
\pi_ {l} ^ {\prime} = \max _ {w} \alpha w w _ {h} + (1 - \alpha) w _ {h} - k _ {l} w ^ {2} + \beta \left[ (1 - (1 - w) p _ {g b}) v _ {g} + (1 - w) p _ {g b} v _ {b} \right] - v _ {g}.
$$

The optimal deviating efort can be solved through the first-order condition as $\begin{array} { r } { w _ { l } ^ { \prime } = \frac { k _ { h } } { k _ { l } } w _ { h } } \end{array}$ . The corresponding profit under deviation is therefore

$$
\pi_ {l} ^ {\prime} = \frac {k _ {h} ^ {2}}{k _ {l}} (\beta f _ {h} v _ {d}) ^ {2} + (1 - \alpha) \beta f _ {h} v _ {d} + \beta [ (1 - p _ {g b}) v _ {g} + p _ {g b} v _ {b} ] - v _ {g}.\tag{9}
$$

When $\pi _ { l } ^ { \prime } \leq \pi _ { l }$ , the incentive compatibility for low-type agents is satisfied. Applying the same steps for high types, we can derive their deviating efort and profit $( \mathrm { i } . \mathrm { e } . , w _ { h } ^ { \prime }$ and $\pi _ { h } ^ { \prime } )$ correspondingly. $\pi _ { l } ^ { \prime } \leq \pi _ { l }$ and $\pi _ { h } ^ { \prime } \leq \pi _ { h }$ together lead to the conditions for the existence of a separating equilibrium.

We first consider an often used class of reputation systems that have a relatively lenient reputation measure and no audit $( \mathrm { i . e . , } p _ { g b } \leq p _ { b g }$ and $\alpha = 0 )$ . In particular, one special case with $p _ { g b } = p _ { b g }$ in this class characterizes a symmetric reputation system, which is consistent with many reputation systems in practice, where a positive or negative feedback leads to the same amount of increase or decrease in an agent’s reputation score. For instance, on eBay, a seller’s feedback score goes up by 1 upon a positive feedback and goes down by 1 upon a negative feedback. Previous studies on reputation trading have also established their results under a symmetric reputation system (Tadelis 1999, 2002); therefore, this special case allows us to draw comparisons between our findings and theirs. Under this special case, we find that a separating equilibrium does not exist, which is consistent with the findings from Tadelis (1999) and Tadelis (2002). More generally, we find that no separating equilibrium exists for the class of relatively lenient reputation systems without auditing. Without auditing, low-type agents have incentive to mimic the reputation choice of the high types because they can receive a high payment even when they deliver low quality products, whereas the corresponding expected reputational loss from a failed transaction is not too high because of the lenient reputation system. Furthermore, we find that, when the reputation system becomes very lenient, such that $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } \leq \frac { k _ { l } \left( 2 k _ { h } - \alpha \right) } { k _ { h } \left( 2 k _ { l } - \alpha \right) } } \end{array}$ , a separating equilibrium does not exist for any level of auditing intensity. When the reputation is very lenient, even in the presence of auditing, low-type agents have incentive to purchase good reputations because good reputations are seldom downgraded upon audit failures. These two findings together demonstrate the critical role of auditing, as well as the importance of a carefully designed reputation system in inducing separation in a reputation market. We present our finding formally in the following proposition.

Proposition 1 (a) In the absence of auditing $( i . e . , \alpha = 0 )$ , no separating equilibrium exists under a relatively lenient reputation system with $\frac { p _ { g b } } { p _ { b g } } \leq 1$

(b) Under a very lenient reputation system with $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } \leq \frac { k _ { l } \left( 2 k _ { h } - \alpha \right) } { k _ { h } \left( 2 k _ { l } - \alpha \right) } } \end{array}$ , a separating equilibrium does not exist regardless of the auditing scheme.

We next examine the impacts of auditing and reputation system design on the existence of separation and the associated agents’ behaviors. In the presence of auditing, many factors, such as the discount factor $\beta ,$ the reputation system’s tolerance, and the relative proportion of high and low types, may all afect the existence of a separating equilibrium. The following proposition establishes the set of conditions for the existence of a separating equilibrium.

Proposition 2 (a) When $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } \ > \ \underline { { p } } , \ \underline { { \beta } } \ \le \ \beta \ \le \ 1 } \end{array}$ , and $\begin{array} { r } { \underline { { \lambda } } \le \frac { \lambda _ { l } } { \lambda _ { h } } \le \bar { \lambda } } \end{array}$ , there exists a separating equilibrium, where

$$
{\underline {{p}}} {=} {\frac {2 k _ {h} - \alpha}{2 k _ {l} - \alpha} \frac {2 k _ {l} ^ {2}}{\sqrt {(1 - \alpha) ^ {2} k _ {h} ^ {2} + 4 k _ {l} ^ {2} k _ {h} (1 - k _ {h})} - (1 - \alpha) k _ {h}}}\tag{10}
$$

$$
{\underline {{\beta}}} {=} {\frac {f _ {h} k _ {h}}{[ (k _ {h} f _ {h}) ^ {2} - (k _ {l} f _ {l}) ^ {2} ] + (1 - p _ {g b}) f _ {h} k _ {h} + (1 - \alpha) (f _ {h} - f _ {l}) f _ {h} k _ {h}}}\tag{11}
$$

$$
{\underline {{\lambda}}} {=} {\frac {p _ {g b} \beta [ (k _ {h} f _ {h}) ^ {2} - (k _ {l} f _ {l}) ^ {2} ]}{k _ {l} p _ {b g} f _ {l} [ 1 - \beta (1 - p _ {g b}) - (1 - \alpha) \beta (f _ {h} - f _ {l}) ]} - \frac {p _ {g b} f _ {h}}{p _ {b g} f _ {l}}}\tag{12}
$$

and $\begin{array} { r } { \bar { \lambda } = \frac { k _ { l } } { k _ { h } } \underline { { \lambda } } - \left( \frac { k _ { l } } { k _ { h } } - 1 \right) \frac { p _ { g b } f _ { h } } { p _ { b g } f _ { l } } } \end{array}$

(b) The equilibrium reputation value diference $v _ { d }$ is as in Equation (8), and the equilibrium eforts are

$$
{w _ {h}} = {\frac {f _ {h}}{(\frac {\lambda_ {l}}{\lambda_ {h}} \frac {p _ {b g}}{p _ {g b}} f _ {l} + f _ {h})}}\tag{13}
$$

$$
{w _ {l}} = {\frac {f _ {l}}{(\frac {\lambda_ {l}}{\lambda_ {h}} \frac {p _ {b g}}{p _ {g b}} f _ {l} + f _ {h})}}\tag{14}
$$

where $f _ { h }$ and $f _ { l }$ are defined in Equation (7).

This proposition shows that separation can arise as an equilibrium under some conditions. The conditions $\begin{array} { r } { \frac { \lambda _ { l } } { \lambda _ { h } } \le \bar { \lambda } } \end{array}$ and $\begin{array} { r } { \underline { { \lambda } } \le \frac { \lambda _ { l } } { \lambda _ { h } } } \end{array}$ ensure high-type and low-type agents are incentive compatible, respectively; that is, $\pi _ { h } ^ { \prime } \leq \pi _ { h }$ and $\pi _ { l } ^ { \prime } \leq \pi _ { l }$ . In other words, when these two conditions hold, hightype (low-type) agents have no incentive to choose a Bad (Good) reputation in equilibrium and, therefore, the reputations tell the types of the reputation owners. Conditions $\frac { p _ { g b } } { p _ { b g } } > \underline { { p } }$ and $\underline { { \beta } } \le \beta \le 1$ together ensure that the range $[ \underline { { \lambda } } , \bar { \lambda } ]$ indeed exists $( \mathrm { i . e . , } \lambda \leq \bar { \lambda } )$ , and a composition of sellers exists such that the corresponding $\frac { \lambda _ { l } } { \lambda _ { h } }$ falls into the range [λ, λ<sup>¯</sup>].

This result highlights a few important factors for the implementation of a reputation market in practice: the discount factor, the reputation system’s tolerance, and the relative proportion of high and low types all afect the existence of a separating equilibrium. To allow for a separation, the proportion ratio of the two types of agents, $\frac { \lambda _ { l } } { \lambda _ { h } }$ , has to be moderate. When the proportion ratio is too high, a separation cannot sustain because there are too many low types who supply Good reputations and too few high types who demand them. As a result, the price of Good reputations goes down, and low types can be better of by purchasing Good reputations. On the other hand, when the proportion ratio is too low, the demand for Good reputations is high but the supply is low, which drives up the price of Good reputations and induces high types to purchase Bad reputations.

In the meantime, the discount factor has to be relatively high to allow for a separating equilibrium. The discount factor reflects the relative importance of payment from the current period to payment from future. When agents discount future heavily (i.e., when $\beta$ is small), separating equilibrium is unlikely to be sustained, because the current period payment becomes more important to the agents. In particular, the future reputation value is no longer enough to induce low-type agents to choose Bad reputations; instead, they have strong incentive to purchase Good reputations for a higher payment in the current period.

While both the discount factor and the proportion ratio afect agent behavior, it is worth highlighting that the design of the reputation system is critical to the equilibrium outcome in the reputation market. In particular, separation can occur only if the reputation system is harsh enough, meaning that, as compared with the likelihood of an agent’s being upgraded from a Bad reputation to a Good reputation because of a recent success, it is plausible enough for an agent to be downgraded from a Good reputation to a Bad reputation because of a recent failure. Under a harsh reputation system, agents are motivated to exert high efort because otherwise they may receive a Bad reputation at the end of the period. When the reputation system is lenient—that is, Good reputations are not relatively easy to downgrade—agents’ incentive to exert high efort becomes low. Low-type agents may prefer Good reputations, since they can receive a high payment while having a favorable chance to sustain their Good reputations, even with low efort. In other words, online marketplaces need to impose higher standards (by having high $p _ { g b }$ and low $p _ { b g } )$ in order to provide proper incentives to agents and to sustain a reliable reputation system in the presence of reputation trading.

Proposition 3 The threshold p in Equation (10) is decreasing in α; that is, $\begin{array} { r } { \frac { \partial \underline { { p } } } { \partial \alpha } < 0 } \end{array}$

This result, combined with Proposition 2, illustrates the substitution efect between auditing and reputation. Proposition $2 ( \mathrm { a } )$ indicates that only if the reputation is harsh enough $( \mathrm { i . e . , } \ \frac { p _ { g b } } { p _ { b g } } > \underline { { p } } )$ can the separating equilibrium be sustained. Proposition 3 shows that increasing the auditing frequency can loose the requirement of the reputation harshness and thus can substitute the regulating role of reputation systems to some extent. Intuitively, auditing can regulate an agent’s behavior because it afects the agent’s current period payof from selling a product, and the reputation system regulates an agent’s behavior by afecting the agent’s future payof from selling its updated reputation in the next period. When the auditing probability is high, audit mechanism can easily reveal an agent’s efort level. As a result, auditing provides strong incentive for agents to exert appropriate efort according to their capabilities, such that high types exert higher efort level than low types: Thus auditing also acts as a screening device to diferentiate agents. Even a lenient reputation system would separate high-type agents from low-type agents.

The substitution efect between auditing and reputation underscores the importance of properly designed reputation systems for the marketplace. In the presence of the reputation market, simply using a harsh reputation measure or increasing auditing alone may not necessarily eliminate lowtype agents’ opportunistic behavior of purchasing good reputation and pooling with high-type agents. In addition, when the two regulating devices work together, increasing the regulating power of one (by increasing the auditing frequency or the harshness of reputation measure) can substitute that of the other. Our result thus sheds light on the choice between auditing and reputation measure and calls for the cost and benefit analysis for each device, to properly design a cost-efective reputation mechanism to regulate agents on a marketplace.

Next, we discuss how the design of each device afects the agents’ equilibrium behavior.

Corollary 1 In a separating equilibrium, more frequent audit leads to lower reputation value difference $( v _ { d } )$ , lower efort from low-type agents $( w _ { l } )$ , and higher efort from high-type agents $( w _ { h } )$ When the auditing probability is high and the audit mechanism monitors agents’ behavior closely, the reputation measure plays a relatively less important role, thus decreasing the reputation value diference. Meanwhile, high-type and low-type agents react to the increased audit probability diferently. Having cost advantage, high-type agents welcome an audit and hope to prove their eforts to consumers. With increased audit probability, they increase their efort level. In contrast, low-type agents have cost disadvantage and are negatively afected by increased audit probability, which makes them exert less efort in equilibrium.

In the meantime, when the reputation system tightens up, diferent types of agents show varying responses as well. In particular, changes in the reputation system afect agents’ efort through two aspects. On the one hand, $\frac { p _ { g b } } { p _ { b g } }$ reflects the probability of obtaining Good reputations at the end of the period for both types of agents, which has a direct efect on agents’ behavior. On the other hand, $\frac { p _ { g b } } { p _ { b g } }$ changes the reputation value $v _ { d }$ through changing the market demand and supply for Good reputations, which has an indirect efect on agents’ behavior. How the reputation system design afects agents’ behavior is jointly determined by these two efects, which is described in the following corollary.

Corollary 2 In a separating equilibrium, high types’ efort is increasing in $\frac { p _ { g b } } { p _ { b g } }$ , and low types’ efort is increasing in $\frac { p _ { g b } } { p _ { b g } }$ when $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } < \sqrt { \frac { \lambda _ { l } } { \lambda _ { h } } \frac { 2 k _ { h } - \alpha } { 2 k _ { l } - \alpha } } } \end{array}$ , while decreasing in $\frac { p _ { g b } } { p _ { b g } }$ when $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } > \sqrt { \frac { \lambda _ { l } } { \lambda _ { h } } \frac { 2 k _ { h } - \alpha } { 2 k _ { l } - \alpha } } } \end{array}$

The intuition for these results can be understood through two special cases. When $p _ { b g }$ remains unchanged, increasing $p _ { g b }$ gives high-type agents more incentive to exert efort because they face an increasing chance of being downgraded to Bad reputations, which is the direct efect. Meanwhile, increasing $p _ { g b }$ also has an indirect efect via changing the reputation value, which in turn is determined by the supply of Good reputations. The supply of Good reputations is increasing in high-type agents’ efort but decreasing in the probability $p _ { g b }$ . As a result, the reputation value $v _ { d }$ exhibits a reversed U-shape when $p _ { g b }$ increases; that is, $v _ { d }$ is increasing in $p _ { g b }$ when $p _ { g b }$ is small, and is decreasing in $p _ { g b }$ when $p _ { g b }$ is large. Since low types have the same probability, $p _ { b g }$ , of being upgraded to Good reputations, their reaction to changes in $\frac { p _ { g b } } { p _ { b g } }$ also exhibits a reversed U-shape. Similarly, when $p _ { g b }$ remains the same, decreasing $p _ { b g }$ per se gives low-type agents less incentive for efort (the direct efort), which reduces the supply of Good reputations (the indirect efect) and drives up the reputation value $v _ { d }$ . As a result, high-type agents have more incentive to exert efort because of the increased potential loss from downgrading their Good reputations $( v _ { d } )$ . For low types, their reaction again exhibits a reversed U-shape, because they face a decreasing probability of being upgraded to Good reputations but an increasing gain from having Good reputations. The second force dominates when $\frac { p _ { g b } } { p _ { b g } }$ is relatively low, whereas the first force dominates when $\frac { p _ { g b } } { p _ { b g } }$ becomes high enough.

Furthermore, agents’ behavior is also afected by the composition of high- and low-type agents. When the proposition of high types goes up,<sup>7</sup> more high-type agents demand Good reputations, and fewer low-type agents sell these Good reputations. As a result, the reputation value $v _ { d }$ increases, and both types of agents have more reputational incentive to exert high efort.

Corollary 3 In a separating equilibrium, the reputation value $( v _ { d } )$ and the efort levels of both types $( w _ { h }$ and $w _ { l } )$ are all decreasing in the proportion of low-type agents $\left( \lambda _ { l } \right)$ .

## 4.2. Semi-Separating Equilibria

In this section, we examine two types of semi-separating equilibria. In a semi-separating equilibrium, one category of reputation (i.e., Good or Bad) is chosen by one type of agents only, but the other category of reputation is chosen by both types of agents. Accordingly, consumers can infer the type of agents behind the first category of reputation, but cannot be sure about the type of agents behind the second category. In our setting with two types of agents, two such semi-separating equilibria might occur: one in which low-type agents choose Bad reputations while high-type agents may choose Good or Bad reputations, and another with high-type agents choosing Good reputations while low types may choose Good or Bad reputations.

## Semi-separating equilibrium with high-type agents playing mixed strategies

We start by studying the first type of semi-separating equilibrium. We denote the proportion of high-type agents choosing Good reputations as $m ,$ the efort level by high types with a Good (Bad) reputation as $w _ { h } \ ( w _ { h b } )$ , the efort level by low types as $w _ { l }$ , and the average efort level from Bad reputations as $w _ { b }$ . Agents’ objectives remain the same as in Equation (1). For agents with Good reputations, in equilibrium, consumers know that these agents are high types, and their willingnessto-pay equals these agents’ efort level $w _ { h }$ , which can be solved by taking first-order condition of equation (3) as $w _ { h } = \beta v _ { d } f _ { h }$ . For agents with Bad reputations, consumers’ belief of them being high (low) types is $\frac { ( 1 - m ) \lambda _ { h } } { 1 - m \lambda _ { h } } ~ \bigl ( \frac { 1 - \lambda _ { h } } { 1 - m \lambda _ { h } } \bigr )$ , and their willingness-to-pay becomes the average efort level from both types of agents; that is,

$$
w _ {b} = \frac {\lambda_ {h} (1 - m) w _ {h b} + (1 - \lambda_ {h}) w _ {l}}{1 - m \lambda_ {h}}.\tag{15}
$$

The equilibrium level of efort for agents with bad reputations is characterized by the first-order condition of Equation (4) as $\alpha w _ { b } - 2 k _ { \theta } w + \beta p _ { b g } v _ { d } = 0$ . We can then derive high types’ efort at Bad reputations as $\begin{array} { r } { w _ { h b } = \frac { \alpha w _ { b } + \beta p _ { b g } v _ { d } } { 2 k _ { h } } } \end{array}$ and low types’ efort as $\begin{array} { r } { w _ { l } = \frac { \alpha w _ { b } + \beta p _ { b g } v _ { d } } { 2 k _ { l } } } \end{array}$ . The equilibrium price of reputations $v _ { d }$ is determined by a market clearance condition; that is,

$$
\lambda_ {h} m = \lambda_ {h} (1 - m) w _ {h b} p _ {b g} + (1 - \lambda_ {h}) w _ {l} p _ {b g} + \lambda_ {h} m [ 1 - (1 - w _ {h}) p _ {g b} ].\tag{16}
$$

The design of the reputation system, the composition of diferent types of agents, as well as the discount factor for future continue to afect the existence of this type of semi-separating equilibrium. To make high-type agents play a mixed strategy and be indiferent in choosing Bad and Good reputations, the return on investing in a Bad reputation must be comparable to that in a Good reputation. Several possible reasons can lead high types to choose a mixed strategy. For instance, too many high types and too few low types can result in a high demand and, consequently, a high price for Good reputations. The other plausible reason is that the reputation system is too strict, and thus high types have to exert very high efort in order to maintain their Good reputations. Both of these aspects add to the cost of investing in a Good reputation, and make Bad reputations equally attractive to high-type agents. We apply the same procedure from the previous subsection to analyze the incentive compatibilities for both types of agents, and summarize the equilibrium conditions formally in the following proposition.

Proposition 4 When $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } > \frac { k _ { l } ( 2 k _ { h } - \alpha ) \left( 1 - m \lambda _ { h } \right) } { 2 k _ { l } k _ { h } \left( 1 - m \lambda _ { h } \right) - \alpha \left[ k _ { l } \left( 1 - m \right) \lambda _ { h } + k _ { h } \left( 1 - \lambda _ { h } \right) \right] } , \beta _ { 1 } < \beta < \beta _ { 2 } } \end{array}$ , and $\frac { \lambda _ { l } } { \lambda _ { h } } < \lambda _ { 1 }$ , there exists a semi-separating equilibrium such that Bad reputations are shared by both types of agents and Good reputations are owned by high types only, where

$$
{\frac {1}{\beta_ {1}}} = {1 - p _ {g b} + (1 - \alpha) (f _ {h} - f _ {l}) + \frac {\lambda_ {h} p _ {g b} [ (k _ {h} f _ {h}) ^ {2} - (k _ {l} f _ {l}) ^ {2} ]}{k _ {h} [ \lambda_ {h} p _ {g b} f _ {h} + (1 - \lambda_ {h}) p _ {b g} f _ {l} ]},}\tag{17}
$$

$$
\frac {1}{\beta_ {2}} = 1 - p _ {g b} + (1 - \alpha) \left[ f _ {h} - \frac {2 k _ {l} - \alpha}{\frac {2 k _ {h} k _ {l}}{\lambda_ {h} k _ {l} + (1 - \lambda_ {h}) k _ {h}} - \alpha} f _ {l} \right],\tag{18}
$$

$$
\lambda_ {1} = \frac {p _ {g b} [ (k _ {h} f _ {h}) ^ {2} - (k _ {l} f _ {l}) ^ {2} ]}{k _ {h} p _ {b g} f _ {l} [ p _ {g b} - (1 - \alpha) (f _ {h} - f _ {l}) ]} - \frac {p _ {g b} f _ {h}}{p _ {b g} f _ {l}}.\tag{19}
$$

Such a semi-separating equilibrium with high-type agents playing a mixed-strategy is likely to emerge when the reputation system is strict and the proportion of high types is high. Intuitively, when the reputation system is strict, it is dificult to pursue Good reputations for both high and low types, which limits the supply of Good reputations in the reputation market. In the meantime, the high proportion of high-type agents leads to a high demand for Good reputation in the reputation market. These two forces together contribute to high-type agents’ indiference between Good and Bad reputations: high-type agents face a high probability of losing their Good reputations at the end of a period, and the price to purchase Good reputations in the market is high. It is also worth noting that, the discount factor in this equilibrium must be relatively small, which contrasts with the previous finding in Proposition 2 that a separating equilibrium is unlikely to sustain when the discount factor is low.

In an online community, if the proportion of high-quality agents is high, it becomes dificult for the marketplace to separate diferent types of sellers according to Proposition 2. In this case, our result in Proposition 4 shows that the marketplace can achieve semi-separation. One key design to achieve this objective is that the marketplace should make the reputation system strict such that Good reputations are hard to obtain. This type of reputation system prevents low-type agents from choosing Good reputation and cheating the consumers.

## Semi-separating equilibrium with low-type agents playing mixed strategies

We now turn to the second type of semi-separating equilibrium, where high-type agents choose Good reputations only, and low-type agents may choose Good or Bad reputations. We denote the proportion of low types choosing Good reputations as n, the average efort level from Good reputations as $w _ { g }$ , the efort level by low types with a Bad (Good) reputation as $w _ { l } \mathrm { ~ } ( w _ { l g } )$ , and the efort level by high types as $w _ { h }$ . For agents with Bad reputations, consumers know that they must be low types, and their willingness-to-pay equals these agents’ efort, $w _ { l }$ , which can be derived through the first-order condition of Equation (4) as $w _ { l } = \beta v _ { d } f _ { l }$ . For agents with Good reputations, consumers can infer the probability of them being high (low) types as $\begin{array} { r } { \frac { \lambda _ { h } } { \lambda _ { h } + ( 1 - \lambda _ { h } ) n } ~ ( \frac { ( 1 - \lambda _ { h } ) n } { \lambda _ { h } + ( 1 - \lambda _ { h } ) n } ) } \end{array}$ and form their willing-to-pay according to the average efort level from both types of agents; that is, $\begin{array} { r } { w _ { g } \ = \ \frac { \lambda _ { h } w _ { h } + ( 1 - \lambda _ { h } ) n w _ { l g } } { \lambda _ { h } + ( 1 - \lambda _ { h } ) n } } \end{array}$ . The equilibrium level of efort for agents with Good reputations is characterized by the first-order condition of Equation (3): $\alpha w _ { g } - 2 k _ { \theta } w + \beta p _ { g b } v _ { d } = 0$ . Therefore, high types’ efort is $\begin{array} { r } { w { \tiny h } = \frac { \alpha w _ { g } + \beta p _ { g b } v _ { d } } { 2 k _ { h } } } \end{array}$ , and low types’ efort is $\begin{array} { r } { w _ { l g } = \frac { \alpha w _ { g } + \beta p _ { g b } v _ { d } } { 2 k _ { l } } } \end{array}$ . Similarly, we show the existence of such an equilibrium in the following proposition.

Proposition 5 When $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } < \frac { \lambda _ { h } k _ { l } ( 2 k _ { h } - \alpha ) + ( 1 - \lambda _ { h } ) n k _ { h } ( 2 k _ { l } - \alpha ) } { k _ { h } ( 2 k _ { l } - \alpha ) [ \lambda _ { h } + ( 1 - \lambda _ { h } ) n ] } , \beta _ { 3 } < \beta < \beta _ { 4 } } \end{array}$ , and $\frac { \lambda _ { l } } { \lambda _ { h } } > \lambda _ { 2 }$ , there exists a semi-separating equilibrium such that Good reputations are shared by both types of agents and Bad reputations are owned by low types only, where

$$
{\frac {1}{\beta_ {3}}} = {1 - p _ {g b} + (1 - \alpha) (f _ {h} - f _ {l}) + \frac {\lambda_ {h} p _ {g b} [ (k _ {h} f _ {h}) ^ {2} - (k _ {l} f _ {l}) ^ {2} ]}{k _ {l} [ \lambda_ {h} p _ {g b} f _ {h} + (1 - \lambda_ {h}) p _ {b g} f _ {l} ]},}\tag{20}
$$

$$
{\frac {1}{\beta_ {4}}} = {1 - p _ {g b} + (1 - \alpha) (K f _ {h} - f _ {l}) - \frac {k _ {l}}{K f _ {h}} (f _ {l} ^ {2} - (\frac {k _ {h} K f _ {h}}{\lambda_ {h} k _ {l} + (1 - \lambda_ {h}) k _ {h}}) ^ {2}),}\tag{21}
$$

$$
\lambda_ {2} = \frac {(k _ {h} f _ {h}) ^ {2} - (k _ {l} f _ {l}) ^ {2}}{k _ {l} f _ {l} [ p _ {g b} - (1 - \alpha) (f _ {h} - f _ {l}) ]} - \frac {p _ {g b} f _ {h}}{p _ {b g} f _ {l}},\tag{22}
$$

with $\begin{array} { r } { K = \frac { ( 2 k _ { h } - \alpha ) [ \lambda _ { h } k _ { l } + ( 1 - \lambda _ { h } ) k _ { h } ] } { 2 k _ { h } k _ { l } - \alpha [ \lambda _ { h } k _ { l } + ( 1 - \lambda _ { h } ) k _ { h } ] } } \end{array}$

When low-type agents play a mixed-strategy and choose not only Bad reputations but also Good reputations in equilibrium, the payof from operating under Good reputations must be high enough to be comparable with that of Bad reputations for low types, which is contrary to a separating equilibrium where Good reputations are inferior to Bad reputations for low-type agents. The high payof from choosing Good reputations comes from two sources. First, the reputation system is lenient such that Good reputations are easy to pursue for both types of agents. In this case, lowtype agents have a good chance to sustain their Good reputations. Second, when the proportion of low types is high, meaning a high supply and low demand for Good reputations, the price of Good reputations is not very high in comparison with that of Bad reputations. As the price diference between Good and Bad reputations decreases, low-type agents are more likely to enjoy a high payof under Good reputations. Both of these aspects together lead to low-type agents’ indiference between Good and Bad reputations.

In an online marketplace with a high proportion of low-quality sellers, it is also dificult to fully separate the two types of agents based on their reputation choices, as demonstrated in Proposition 2. Instead, according to Proposition 5, the marketplace can achieve a semi-separating equilibrium by implementing a lenient reputation system such that Good reputations are not too costly to obtain. This type of reputation system motivates low types for efort whether they have a Good reputation or a Bad reputation.

## 5. Extension: Cumulative Reputation

In the baseline model, we capture reputation change by $p _ { g b }$ and $p _ { b g } ;$ that is, agents’ reputations are updated according to their efort with a probability. In this extension, we consider a reputation system that captures more details of agents’ historical performance, and demonstrate that a reputation market continues to be efective and can separate diferent types of agents based on their reputation choices. We denote reputation as a non-negative number $j \in \mathcal N$ , and a reputation $j$ is updated to $j + 1 \ ( j - 1 )$ with a positive (negative) feedback from consumers. Note that we assume reputation $j = 0$ remains to be 0 upon a negative feedback, considering that an agent always has the option to create a new identity of reputation 0 with negligible cost. Let $w _ { j }$ be the efort level of agents with reputation $j , v _ { j }$ be the market value of reputation $j ,$ , and $\pi _ { j }$ be the profit for agents with reputation $j$ . We also introduce $\tilde { w } _ { j }$ as consumers’ expected product quality from reputation $j ,$ , which is also their willingness-to-pay. For ease of exposition, we assume that agents do not discount future payofs $\left( \mathrm { i . e . , ~ } \beta = 1 \right)$ . This assumption simplifies the algebra without imposing limitations on our main result, especially because we have already shown in Proposition 2 that the discount factor has to be large enough for a separating equilibrium to exist. The timeline of events and the reputation market in this extension remain the same as in the main model in Section 3.

Agents’ objective function is in the following form:

$$
\pi^ {\theta} = \max _ {j \in \mathcal {N}} \left[ \max _ {w \in (0, 1)} \alpha w _ {j} \tilde {w} _ {j} + (1 - \alpha) \tilde {w} _ {j} - k _ {\theta} w _ {j} ^ {2} + w _ {j} v _ {j + 1} + (1 - w _ {j}) v _ {j - 1} - v _ {j} \right].\tag{23}
$$

As in the baseline model, the first two terms in the objective function above are the expected payment from selling the product. With probability $\alpha ,$ , a product is audited, and the agent receives payment $( \tilde { w } _ { j } )$ only when its product passes the audit (with probability $w _ { j } )$ ). With probability $1 - \alpha$ , the product is not audited and the agent receives consumers’ willing-to-pay, $\tilde { w } _ { j }$ , based on its reputation. The third term is the cost for exerting efort level $w _ { j }$ , and the fourth term is the expected value of the agent’s reputation at the end of the period. The last term, $v _ { j } ,$ is the agent’s cost to purchase reputation $j$ at the beginning of the period. Similar to the baseline model, the above objective function reflects agents’ expected payof from purchasing a reputation $j$ for one investment cycle—starting from purchasing a reputation in the current period to selling the reputation the next period. We define a separating equilibrium as below.

Definition 2 A separating equilibrium consists of a set of values $\{ v _ { j } , w _ { j } , \lambda _ { j } \} , j \in \mathcal { N }$ , and a threshold reputation $h \in \mathcal N$ , that satisfy the following conditions: $( a )$ Incentive compatibility $( I C ) \colon h i g h \cdot$ type agents always choose reputation $j \geq h$ and are indiferent between any reputation $j \geq h ,$ low-type agents choose reputation $j < h$ and are indiferent to any reputation $j < h ; \mathit { \Omega } ( b )$ Rational Expectations (RE): w˜<sub>j</sub> = w<sub>j</sub> ; (c) Market Clearance $( M C ) \colon \lambda _ { j } = \lambda _ { j - 1 } w _ { j - 1 } + \lambda _ { j + 1 } \bigl ( 1 - w _ { j + 1 } \bigr )$ , where $\lambda _ { j }$ is the proportion of agents at reputation $j$ .

The incentive compatibility condition states that, given low-type agents’ efort and reputation decisions, high-type agents prefer to purchase reputations $j \geq h$ and obtain the same profit from any reputation $j \geq h$ , and vice versa for low types. The rational expectation condition indicates that consumers’ ex ante belief on efort is consistent with agents’ actual efort decision in equilibrium. The market clearance condition specifies that the equilibrium level of reputation price for reputation j, $j \in \mathcal N$ , is determined in such a fashion that the demand for reputation $j$ equals the supply of reputation $j .$ . Specifically, the left-hand side of the condition is the demand of reputation $j ,$ and the right-hand side is the supply. Note that we have introduced an additional variable in the definition of a separating equilibrium, the threshold reputation $h \in \mathcal N$ . Diferent from the baseline model where there are two levels of reputations for two types of agents to choose from, in the extended model, there are more reputation levels than types of agents. Consequently, there can be multiple separating equilibria, depending on the threshold reputation.

For each threshold reputation $h ,$ we can derive high-type agents’ efort as $\begin{array} { r } { w _ { j } \ = \ \frac { v _ { j + 1 } - v _ { j - 1 } } { 2 k _ { h } - \alpha } } \end{array}$ for $j \geq h ,$ and low-type agents’ efort as $\begin{array} { r } { w _ { j } \ = \ \frac { v _ { j + 1 } - v _ { j - 1 } } { 2 k _ { l } - \alpha } } \end{array}$ for $0 ~ < ~ j ~ < ~ h$ and $\begin{array} { r } { w _ { 0 } \ = \ \frac { v _ { 1 } - v _ { 0 } } { 2 k _ { l } - \alpha } } \end{array}$ for $j = 0$ . Consumers can also directly learn agents’ types from their reputations; that is, agents with reputations $j \geq h$ must be high types, and agents with reputations $0 < j < h$ must be low types. Based on the three conditions as defined above and the requirement that $\sum _ { j \geq h } \lambda _ { j } = \lambda _ { h }$ and $\textstyle \sum _ { j } \lambda _ { j } = 1$ , we have just enough equations to solve for the equilibrium variables $\{ v _ { j } , w _ { j } , \lambda _ { j } \}$ $j \in \mathcal N$ . In the following proposition, we describe one such separating equilibrium to demonstrate the existence of separation under this new reputation system.

Proposition 6 When $\textstyle { \frac { 2 } { 3 } } \leq \alpha \leq 1$ and $\textstyle { \frac { 3 } { 2 } } \alpha - 1 \leq k _ { h } \leq { \frac { 4 } { 5 } }$ , there exists a separating equilibrium where low-type agents choose reputation 0 and high-type agents choose reputations $j \geq 1$

This proposition shows that our main results from the previous section continue to hold in a more general reputation system. First, a separating equilibrium continue to exist in the cumulative reputation system. The cumulative reputation system allows more room for high-type and low-type agents to separate themselves from each other at diferent threshold reputations. The proposition demonstrates one way to separate the agents, and we will show with a numerical example later that agents can separate themselves at other thresholds with $h > 1$ . More importantly, our earlier result—that auditing is critical to inducing separation—also holds in the cumulative reputation system. The condition ${ \begin{array} { l } { { \frac { 2 } { 3 } } \leq \alpha \leq 1 } \end{array} }$ from the aforementioned proposition states that the separating equilibrium requires not only auditing but also a high enough auditing frequency. When the auditing probability is high, low-type agents prefer to choose lower reputations, $j < h$ , because their chance of passing the audit is low even if they purchase higher reputations. Overall, although the cumulative reputation system demonstrates more variations in the transition among diferent reputations, we can draw the same conclusion regarding the existence of separation, and our insight about the importance of auditing remains consistent with that in the baseline model.

While Proposition 6 formally proved the existence of a separating equilibrium, many such separating equilibria can exist for $h > 1$ . We provide a numerical example of such an equilibrium with $h = 2$

Example. We consider an equilibrium where low-type agents choose reputation 0 and 1, and high-type agents can choose any reputation $j \geq 2$ . We set the following values for the parameters: $k _ { h } = 0 . 8 5 , k _ { l } = 0 . 9 5 , \alpha = 0 . 8 , \lambda _ { h } = 0 . 1 0 8$ , and $\beta = 1$ . For simplification, we look for an equilibrium with $v _ { j } - v _ { j - 1 } = b , \ j > 2$ , meaning the reputation value diference is the same for reputations chosen by high types. We also denote the reputation value diference for low types as $v _ { 1 } - v _ { 0 } = a _ { 0 }$ and $v _ { 2 } - v _ { 1 } = a _ { 1 }$ . The equilibrium efort level at reputation $j$ can be solved from the first-order condition of Equation (23) as $\begin{array} { r } { w _ { 0 } = \frac { a _ { 0 } } { 1 . 1 } , w _ { 1 } = \frac { a _ { 0 } + a _ { 1 } } { 1 . 1 } , w _ { 2 } = \frac { a _ { 1 } + b } { 0 . 9 } } \end{array}$ , and $\begin{array} { r } { w _ { j \geq 3 } = \frac { 2 b } { 0 . 9 } } \end{array}$ . The incentive compatibility condition for low types $( \mathrm { i . e . , ~ } \pi _ { 0 } = \pi _ { 1 } )$ leads to the following equation:

$$
a _ {0} = \frac {a _ {1} [ (1 - \alpha) (2 k _ {l} - \alpha) + a _ {1} k _ {l} ]}{(2 k _ {l} - \alpha) ^ {2} - 2 k _ {l} a _ {1}} = \frac {a _ {1} (0 . 2 2 + 0 . 9 5 a _ {1})}{1 . 2 1 - 1 . 9 a _ {1}}.\tag{24}
$$

The incentive compatibility for high types $\left( \mathrm { i . e . , } \ \pi _ { 2 } = \pi _ { j \geq 3 } \right)$ leads to the following equation:

$$
b = \frac {(2 k _ {h} - 1) (2 k _ {h} - \alpha)}{3 k _ {h}} - \frac {a _ {1}}{3} = \frac {0 . 6 3}{2 . 5 5} - \frac {a _ {1}}{3}.\tag{25}
$$

Applying the market clearance condition, we can write the proportions of low-type agents as $\begin{array} { r } { \lambda _ { 1 } ~ = ~ \lambda _ { 0 } \frac { w _ { 0 } } { 1 - w _ { 1 } } } \end{array}$ , and the proportions of high-type agents as $\begin{array} { r } { \lambda _ { 2 } ~ = ~ \lambda _ { 0 } \frac { w _ { 0 } } { 1 - w _ { 1 } } \frac { w _ { 1 } } { 1 - w _ { 2 } } } \end{array}$ , and $\lambda _ { j \geq 3 } ~ =$ $\begin{array} { r } { \lambda _ { 0 } \frac { w _ { 0 } } { 1 - w _ { 1 } } \frac { w _ { 1 } } { 1 - w _ { 2 } } \frac { w _ { 2 } } { 1 - w _ { 3 } } \big ( \frac { w _ { 3 } } { 1 - w _ { 3 } } \big ) ^ { j - 3 } } \end{array}$ . The proportions of low-type agents also have to satisfy that $\lambda _ { 0 } + \lambda _ { 1 } =$ $1 - \lambda _ { h }$ , or equivalently,

$$
\lambda_ {0} \left(1 + \frac {a _ {0}}{1 . 1 - \left(a _ {0} + a _ {1}\right)}\right) = 0. 8 9 2.\tag{26}
$$

The proportions of high-type agents have to satisfy $\textstyle \sum _ { j = 2 } ^ { + \infty } \lambda _ { j } = \lambda _ { h }$ , which is equivalent to

$$
\lambda_ {0} \frac {w _ {0}}{1 - w _ {1}} \frac {w _ {1}}{1 - w _ {2}} + \sum_ {j = 3} ^ {+ \infty} \lambda_ {0} \frac {a _ {0}}{1 . 1 - a _ {0} - a _ {1}} \frac {0 . 9 (a _ {0} + a _ {1})}{1 . 1 (0 . 9 - a _ {1} - b)} \frac {a _ {1} + b}{0 . 9 - 2 b} (\frac {2 b}{0 . 9 - 2 b}) ^ {j - 3} = 0. 1 0 8.\tag{27}
$$

With Equations (24)-(27), we get the following solutions $a _ { 0 } = 0 . 0 8 1 , a _ { 1 } = 0 . 1 8 , b = 0 . 1 8 7$ , and $\lambda _ { 0 } = 0 . 8 1 3$ . We can further derive the solutions for all other variables as $\lambda _ { 1 } = 0 . 0 7 9 , \lambda _ { 2 } = 0 . 0 3 2$ 2 $\lambda _ { 3 } = 0 . 0 2 2 , w _ { 0 } = 0 . 0 7 4 , w _ { 1 } = 0 . 2 3 8 , w _ { 2 } = 0 . 4 0 8$ , and $w _ { 3 } = w _ { j > 3 } = 0 . 4 1 6$ . The corresponding profit for low types is $\pi _ { l } = 0 . 0 2$ , and the profit for high types is $\pi _ { h } = 0 . 0 4 3$ . For example, a low-type agent chooses to purchase a reputation $j = 3$ , its deviating efort becomes $\frac { k _ { h } } { k _ { l } } w _ { 3 }$ , and the deviating profit is $\begin{array} { r } { \frac { k _ { h } } { k _ { l } } \left[ k _ { h } w _ { 3 } ^ { 2 } + ( 1 - \alpha ) w _ { 3 } \right] - b = 0 . 0 1 9 } \end{array}$ , which is less than its profit at reputation 0 or 1. If a high-type agent chooses reputation $j = 1$ , its deviating efort is ${ \frac { k _ { l } } { k _ { h } } } w _ { 1 }$ , and deviating profit is $\begin{array} { r } { \frac { k _ { l } } { k _ { h } } \left[ k _ { l } w _ { 1 } ^ { 2 } + ( 1 - \alpha ) w _ { 1 } \right] - a _ { 0 } = 0 . 0 3 2 } \end{array}$ , which is also less than its profit from reputations $j \geq 2$ Similarly, we can show that high-type agents have no incentive to deviate to purchasing reputation $j = 0$ , and low-type agents have no incentive to deviate to purchasing reputation $j \geq 3$ . Therefore, we have shown with an example that a separating equilibrium exists with $h = 2$

In a complex reputation system, such as the cumulative reputation system, an online marketplace can continue to use a reputation market to regulate diferent types of agents’ reputation and efort choices. We have demonstrated the existence of a separating equilibrium under the cumulative reputation system in Proposition 6.

## 6. Conclusion and Discussion

In this paper, we apply the general equilibrium theory to study reputation trading in e-commerce. Our focus is to show that a market for reputation, if properly designed, can increase agents’ incentive to behave well, rather than give them an opportunity to cheat on consumers. We demonstrate the existence of a separating equilibrium in which agents with higher capability choose to purchase higher levels of reputations, whereas agents with lower capability choose to purchase lower levels of reputations. In this case, the reputation system provides consumers with precise information on the type of agents behind any reputation. We discover that both auditing and the reputation measure are critical in inducing a separating equilibrium. Without auditing, a separating equilibrium cannot occur under commonly used reputation systems. In the presence of auditing, these two incentive mechanisms work together as substitutes: increasing auditing frequency or increasing harshness of reputation measure can be used as a substitute to induce separation. Auditing, such as the prevalent warranty policies in e-commerce marketplaces, imposes a contingent contract on agents’ payof from the product market; that is, good reputations lead to high payment for products only if the agents can pass the audit. Meanwhile, the reputation measure contributes to agents’ payof from the reputation market. When the reputation system is strict, agents sufer a reputational loss because their reputations are likely to be downgraded upon failures. These two incentive mechanisms, auditing and the reputation measure, together motivate agents to choose reputations that suit their capability level. We consider diferent reputation systems and arrive at the same conclusion that a reputation market with properly designed auditing can promote favorable behaviors from agents.

Our findings provide important insights from a market owner’s point of view. First of all, our study suggests several benefits of reputation trading for a market owner. When reputation becomes an asset and can be exchanged for money in a reputation market, users have a monetary incentive to maintain and improve their online identities. The primary concern with reputation trading is that the role of reputation could be undermined because of the easy acquisition and disposal of reputation, which creates the risk of fraud and deception. Our model predicts that a reputation market can efectively facilitate transactions in online marketplaces. A market for reputations not only serves the purpose of eficient allocation of resource (i.e., reputations) based on agents’ types, but also increases the informativeness of reputations to consumers. In addition, as a marketplace develops over time, the users (or agents) may encounter the need to exit the marketplace for diferent reasons (e.g., retiring from the business). In this situation, a reputation market provides a succession plan for the exiting agents and, in turn, gives more incentive to the existing agents to improve their reputations. Second, we suggest a market owner incorporate warranty policies that protect customers from fraudulent transactions. Our study shows that ofering warranties not only increases customers’ satisfaction, but also promotes favorable behaviors from the agents. In particular, warranty policies that ofer good protection to customers correspond to an intensive auditing process that can efectively regulate agents’ cheating behaviors. Lastly, our findings also suggest that the market owner adopt a strict reputation system, which puts more weight on failures than successes when calibrating agents’ reputation scores. Under such a reputation system, good reputations are no longer favorable to all because low capability agents find it dificult to maintain these good reputations.

Our analysis can be generalized to other industries that involve name trading, such as the private equity business. We can identify two sources of revenue for a private equity firm, according to our separation results. One major source of revenue to private equity agents is the improvement of firm reputation, which leads to an increase in the market value of the firm. In practice, many firms indeed recognize and utilize the connection between firm reputation and firm market value. A 2005 study on United Technologies Corp. (UTC) concluded that 27 percent of UTC’s stock market value was attributable to intangibles such as its reputation (Engardio and Arndt 2007). Meanwhile, to establish a better reputation, the firm itself is likely to better perform in the industry, which generates profit to private equity agents who run the firm for that period. Also, if we view private equity agents as high types (Jackson 2007) and the previous owners as low types, then private equity agents earn a profit from their higher ability to operate the firm. Our results also suggest that private equity agents will not take over firms with reputations that exceed their ability, because they will not be able to sustain that reputation, and thus make less profit than what they can receive from operating a lower reputation firm.

This study can be extended in a few directions for future research. First, it may be interesting to incorporate the cost of auditing for consumers. After all, obtaining a refund may involve monetary and time cost to file relevant documents, to ship the defected products back to the sellers, or to wait for a certain period of time to receive the refund. Such costs may vary for diferent consumers and, as a result, diferent consumers may adopt diferent auditing intensities. Some consumers may even strategically choose auditing intensities according to agents’ reputations. From agents’ perspective, their reputation choice not only afects the direct payment from consumers, but also determines what types of consumers they may encounter and how likely they are to be audited. Another extension is to study the competition among multiple marketplaces. One possible scenario is that if one marketplace adopts more frequent auditing, or strict reputation measure, high capability agents may choose this marketplace over the others. Consequently, the composition of agents in a particular marketplace will adapt to the market owner’s policy choices in the long run. These extensions can potentially enhance our understanding of the long-term impacts of reputation trading. It is also interesting to examine other impacts of reputations on agents’ behaviors. For instance, a good reputation might benefit a seller via product price or volume of transactions. While this study focuses on its efect on price, the efect of reputation on volume of transactions is another interesting research direction.

## References

Ba, Sulin, Paul A. Pavlou. 2002. Evidence of the efect of trust building technology in electronic markets: Price premiums and buyer behavior. MIS Quarterly 26(3) 243–268.

Chellappa, Ramnath K. 2012. Consumers’ trust in electronic commerce transactions: The role of perceived privacy and perceived security. Working Paper .

Cripps, Martin W., George J. Mailath, Larry Samuelson. 2004. Imperfect monitoring and impermanent reputations. Econometrica 72(2) 407–432.

Dellarocas, Chrysanthos. 2005. Reputation mechanism design in online trading environments with pure moral hazard. Information Systems Research 16(2) 209–230.

Engardio, Pete, Michael Arndt. 2007. What price reputation? Business Week July 9th.

Fan, Ming, Yong Tan, Andrew B. Whinston. 2005. Evaluation and design of online cooperative feedback mechanisms fo reputatin management. IEEE Transactions on Knowledge and Data Engineering 17(3) 244–254.

Friedman, Eric J., Paul Resnick. 2001. The social cost of cheap pseudonyms. Journal of Economics and Management Strategy 10(2) 173–199.

Fudenberg, Drew, David K. Levine. 1989. Reputation and equilibrium selection in games with a patient player. Econometrica 57(4) 759–778.

Fudenberg, Drew, David K. Levine. 1992. Maintaining a reputation when strategies are imperfectly observed. The Review of Economic Studies 59(3) 561–579.

Holmstrom, Bengt. 1999. Managerial incentive problems: A dynamic perspective. The Review of Economic Studies 66(1) 169–182.

Jackson, Tony. 2007. Private equity shows the way on intelligence. Financial Times April 4th.

Kreps, David M., Paul R. Milgrom, John Roberts, Robert J. Wilson. 1982. Rational cooperation in the finitely repeated prisoners’ dilemma. Journal of Economic Theory 27(2) 245–252.

Mailath, George J., Larry Samuelson. 2001. Who wants a good reputation? The Review of Economic Studies 68(2) 415–441.

Pavlou, Paul A., Angelika Dimoka. 2006. The nature and role of feedback text comments in online marketplaces: Implications for trust building, price premiums, and seller diferentiation. Information Systems Research 17(4) 392–414.

Yang, Jian, Xiaorui Hu, Han Zhang. 2007. Efects of a reputation feedback system on an online consumer-to-consumer auction market. Decision Support Systems 44(1) 93–105.

## A. Appendix

## A.1. Proof of Propositions 1 and 2

We first analyze the incentive compatibility condition for low types. Notice that the objective for a low-type agent deviating to purchasing a Good reputation is formulated in Equation (9). The first-order condition of Equation (9) is $\alpha w _ { h } - 2 k _ { l } w _ { l } ^ { \prime } + \beta p _ { g b } v _ { d } = 0$ , which leads to the deviating efort as $\begin{array} { r } { w _ { l } ^ { \prime } = \frac { k _ { h } } { k _ { l } } w _ { h } } \end{array}$ . The deviating profit and equilibrium profit for low types become

$$
\begin{array}{r c l} \pi_ {l} ^ {\prime} & = & k _ {l} \frac {k _ {h} ^ {2}}{k _ {l} ^ {2}} (\beta f _ {h} v _ {d}) ^ {2} + (1 - \alpha) \beta f _ {h} v _ {d} + \beta [ (1 - p _ {g b}) v _ {g} + p _ {g b} v _ {b} ] - v _ {g}; \\ \pi_ {l} & = & k _ {l} (\beta f _ {l} v _ {d}) ^ {2} + (1 - \alpha) \beta f _ {l} v _ {d} + \beta v _ {b} - v _ {b}. \end{array}
$$

Incentive compatibility for low types requires $\pi _ { l } ^ { \prime } \leq \pi _ { l }$ , which is equivalent to

$$
k _ {l} \left(\frac {k _ {h} ^ {2}}{k _ {l} ^ {2}} f _ {h} ^ {2} - f _ {l} ^ {2}\right) \beta^ {2} v _ {d} ^ {2} + (1 - \alpha) (f _ {h} - f _ {l}) \beta v _ {d} + (\beta (1 - p _ {g b}) - 1) v _ {d} \leq 0.
$$

Dividing both sides by $v _ { d } .$ , we can reorganize the condition as $M _ { 2 } \beta v _ { d } \le k _ { l } M _ { 1 }$ , where

$$
M _ {1} = 1 - \beta (1 - p _ {g b}) - (1 - \alpha) \beta (f _ {h} - f _ {l}),
$$

$$
{M _ {2}} = {\beta [ (k _ {h} f _ {h}) ^ {2} - (k _ {l} f _ {l}) ^ {2} ].}
$$

Similarly, we can establish that $\begin{array} { r } { w _ { h } ^ { \prime } = \frac { k _ { l } } { k _ { h } } w _ { l } } \end{array}$ . The corresponding deviating profit and equilibrium profit for high types are

$$
\begin{array}{r c l} \pi_ {h} ^ {\prime} & = & k _ {h} \frac {k _ {l} ^ {2}}{k _ {h} ^ {2}} (\beta f _ {l} v _ {d}) ^ {2} + (1 - \alpha) \beta f _ {l} v _ {d} + \beta v _ {b} - v _ {b}; \\ \pi_ {h} & = & k _ {h} (\beta f _ {h} v _ {d}) ^ {2} + (1 - \alpha) \beta f _ {h} v _ {d} + \beta [ (1 - p _ {g b}) v _ {g} + p _ {g b} v _ {b} ] - v _ {g}. \end{array}
$$

Incentive compatibility condition for high types requires $\pi _ { h } ^ { \prime } \leq \pi _ { h }$ , which is equivalent to

$$
k _ {h} [ f _ {h} ^ {2} - \frac {k _ {l} ^ {2}}{k _ {h} ^ {2}} f _ {l} ^ {2} ] \beta^ {2} v _ {d} ^ {2} + (1 - \alpha) (f _ {h} - f _ {l}) \beta v _ {d} + (\beta (1 - p _ {g b}) - 1) v _ {d} \geq 0.
$$

Further simplify the above by dividing both sides with $v _ { d } .$ , and we have the condition as $M _ { 2 } \beta v _ { d } \geq$ $k _ { h } M _ { 1 }$

Combining the two IC conditions leads to $k _ { h } M _ { 1 } \leq M _ { 2 } \beta v _ { d } \leq k _ { l } M _ { 1 }$ . We first notice $M _ { 1 } > 0$ To see this, notice the equivalent condition is $\begin{array} { r } { \beta < \frac { 1 } { 1 - p _ { g b } + ( 1 - \alpha ) ( f _ { h } - f _ { l } ) } } \end{array}$ , where the right-hand side is greater than 1. Furthermore, the sign of $M _ { 2 }$ is consistent with $k _ { h } f _ { h } - k _ { l } f _ { l }$ . Therefore, if $k _ { h } f _ { h } <$ $k _ { l } f _ { l }$ , or, equivalently, if $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } < \frac { k _ { l } \left( 2 k _ { h } - \alpha \right) } { k _ { h } \left( 2 k _ { l } - \alpha \right) } } \end{array}$ , then $M _ { 2 } < 0$ and thus no separating equilibrium can be sustained, which proves the result in Proposition 1(b). Part (a) is a special case of Part (b) with $\alpha = 0$

We next focus on a strict reputation system with $k _ { h } f _ { h } > k _ { l } f _ { l }$ such that both $M _ { 1 }$ and $M _ { 2 }$ are

positive. We substitute in $\begin{array} { r } { v _ { d } = \frac { 1 } { \beta ( \frac { \lambda _ { l } } { \lambda _ { h } } \frac { p _ { b g } } { p _ { g b } } f _ { l } + f _ { h } ) } } \end{array}$ to reorganize the IC conditions as

$$
\frac {M _ {2}}{k _ {l} M _ {1}} \leq \frac {\lambda_ {l}}{\lambda_ {h}} \frac {p _ {b g}}{p _ {g b}} f _ {l} + f _ {h} \leq \frac {M _ {2}}{k _ {h} M _ {1}}.
$$

Define $\underline { { \lambda } }$ and $\bar { \lambda }$ as the values of $\frac { \lambda _ { l } } { \lambda _ { h } }$ that make the two IC conditions binding; that is, $\pi _ { l } ^ { \prime } =$ $\pi _ { l }$ and $\pi _ { h } ^ { \prime } = \pi _ { h }$ . We can derive $\underline { { \lambda } }$ as in Equation (12) and $\bar { \lambda }$ as in the proposition. For any separating equilibrium that satisfies the above condition, the corresponding proportion ratio $\frac { \lambda _ { l } } { \lambda _ { h } }$ must be between λ and $\bar { \lambda } ;$ that is, $\begin{array} { r } { \underline { { \lambda } } \le \frac { \lambda _ { l } } { \lambda _ { h } } \le \bar { \lambda } } \end{array}$ . Furthermore, in order to find a λ that satisfies the above conditions, it sufices to show that $\begin{array} { r } { \frac { p _ { g b } M _ { 2 } } { k _ { h } M _ { 1 } } \geq \frac { p _ { g b } M _ { 2 } } { k _ { l } M _ { 1 } } } \end{array}$ and $\frac { M _ { 2 } } { k _ { h } M _ { 1 } } > f _ { h }$ . The first condition is apparently true, and the second condition can be simplified as

$$
\beta > \underline {{\beta}} = \frac {f _ {h} k _ {h}}{[ (k _ {h} f _ {h}) ^ {2} - (k _ {l} f _ {l}) ^ {2} ] + (1 - p _ {g b}) f _ {h} k _ {h} + (1 - \alpha) (f _ {h} - f _ {l}) f _ {h} k _ {h}}.
$$

In addition, because $\beta \in [ 0 , 1 ]$ , a separating equilibrium requires $[ ( k _ { h } f _ { h } ) ^ { 2 } - ( k _ { l } f _ { l } ) ^ { 2 } ] - p _ { g b } f _ { h } k _ { h } + ( 1 -$ $\alpha ) ( f _ { h } - f _ { l } ) f _ { h } k _ { h } \ge 0$ , which can be rewritten as $\frac { p _ { g b } } { p _ { b g } } \geq \underline { { p } }$ with p as in Equation (10).

Substituting $f _ { \theta }$ in Equation (7) and $v _ { d }$ in Equation (8) into Equations (5)and (6), we can derive $w _ { \theta }$ as in Equations (13) and (14).

## A.2. Proof of Proposition 3

Notice that $\begin{array} { r } { \frac { 2 k _ { h } - \alpha } { 2 k _ { l } - \alpha } = 1 - \frac { 2 k _ { l } - 2 k _ { h } } { 2 k _ { l } - \alpha } } \end{array}$ is decreasing in α. We can verify that the second fraction in $\underline { { p } } \ ( \mathrm { i . e . }$ $\frac { 2 k _ { l } ^ { 2 } } { \sqrt { ( 1 - \alpha ) ^ { 2 } k _ { h } ^ { 2 } + 4 k _ { l } ^ { 2 } k _ { h } ( 1 - k _ { h } ) } - ( 1 - \alpha ) k _ { h } } \Big )$ is also decreasing in α. Therefore, $\underline { { \boldsymbol { p } } }$ is decreasing in α.

## A.3. Proof of Corollaries 1, 2, and 3

Notice that Equations (13) and (14) can be reorganized as

$$
w _ {h} = \frac {1}{\frac {\lambda_ {l}}{\lambda_ {h}} \frac {p _ {b g} ^ {2}}{p _ {g b} ^ {2}} \frac {2 k _ {h} - \alpha}{2 k _ {l} - \alpha} + 1} \mathrm{and} w _ {l} = \frac {1}{\frac {\lambda_ {l}}{\lambda_ {h}} \frac {p _ {b g}}{p _ {g b}} + \frac {p _ {g b}}{p _ {b g}} \frac {2 k _ {l} - \alpha}{2 k _ {h} - \alpha}}
$$

Proof of Corollary 1: Because $\frac { 2 k _ { h } - \alpha } { 2 k _ { l } - \alpha }$ is decreasing in $\alpha ,$ it is easy to see that $v _ { d }$ increases in $\alpha _ { \mathrm { { ; } } }$ , $w _ { h }$ increases in $\alpha ,$ and $w _ { l }$ decreases in α.

Proof of Corollary 2: First, we can verify that $w _ { h }$ increases in $\frac { p _ { g b } } { p _ { b g } }$ . For $w _ { l } .$ , we take derivative of the denominator with respect to $\frac { p _ { g b } } { p _ { b g } }$ and obtains $\begin{array} { r } { \frac { 2 k _ { l } - \alpha } { 2 k _ { h } - \alpha } - \frac { \lambda _ { l } } { \lambda _ { h } } \frac { p _ { b g } ^ { 2 } } { p _ { q b } ^ { 2 } } } \end{array}$ . When $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } > \sqrt { \frac { 2 k _ { h } - \alpha } { 2 k _ { l } - \alpha } \frac { \lambda _ { l } } { \lambda _ { h } } } } \end{array}$ , the denominator decreases and $w _ { l }$ increases in $\frac { p _ { g b } } { p _ { b g } }$ ; when $\begin{array} { r } { \frac { p _ { g b } } { p _ { b g } } < \sqrt { \frac { 2 k _ { h } - \alpha } { 2 k _ { l } - \alpha } } \frac { \lambda _ { l } } { \lambda _ { h } } } \end{array}$ , the denominator increases and $w _ { l }$ decreases in $\frac { p _ { g b } } { p _ { b g } }$

Proof of Corollary 3: Note that $\begin{array} { r } { \frac { \lambda _ { l } } { \lambda _ { h } } = \frac { \lambda _ { l } } { 1 - \lambda _ { l } } } \end{array}$ is increasing in $\lambda _ { l } .$ It follows directly from the expressions of $v _ { d } , w _ { l }$ , and $w _ { h }$ that they are all decreasing in $\frac { \lambda _ { l } } { \lambda _ { h } }$ and $\lambda _ { l }$ .

## A.4. Proof of Proposition 4

The equilibrium satisfies the following conditions

$$
\begin{array}{r c l} {w _ {b}} & = & {\frac {(1 - m) \lambda_ {h} w _ {h b} + (1 - \lambda_ {h}) w _ {l}}{1 - m \lambda_ {h}};} \\ {w _ {h b}} & = & {\frac {\alpha w _ {b} + \beta p _ {b g} v _ {d}}{2 k _ {h}};} \\ {w _ {l}} & = & {\frac {\alpha w _ {b} + \beta p _ {b g} v _ {d}}{2 k _ {l}};} \\ {w _ {h}} & = & {\frac {\beta p _ {g b} v _ {d}}{2 k _ {h} - \alpha};} \\ {\lambda_ {h} m} & = & {\lambda_ {h} (1 - m) w _ {h b} p _ {b g} + (1 - \lambda_ {h}) w _ {l} p _ {b g} + \lambda_ {h} m (1 - (1 - w _ {h}) p _ {g b}).} \end{array}\tag{28}
$$

The first three equations lead to

$$
w _ {b} = \frac {\beta p _ {b g} v _ {d}}{\frac {1}{M} - \alpha};\tag{29}
$$

$$
w _ {h b} = \frac {\beta p _ {b g} v _ {d}}{2 k _ {h} (1 - \alpha M)};\tag{30}
$$

$$
{w _ {l}} = {\frac {\beta p _ {b g} v _ {d}}{2 k _ {l} (1 - \alpha M)},}\tag{31}
$$

where $M = \frac { \frac { ( 1 - m ) \lambda _ { h } } { 2 k _ { h } } + \frac { 1 - \lambda _ { h } } { 2 k _ { l } } } { 1 - m \lambda _ { h } }$

High types at Good and Bad reputations must be indiferent; that is, $\pi _ { h } = \pi _ { h b }$ , which leads to

$$
k _ {h} (w _ {h} ^ {2} - w _ {h b} ^ {2}) + (1 - \alpha) (w _ {h} - w _ {b}) + (\beta (1 - p _ {g b}) - 1) v _ {d} = 0.
$$

Substituting in Equations (29) to (31), $v _ { d }$ can be represented as

$$
\beta v _ {d} = \frac {\frac {1}{\beta} - (1 - p _ {g b}) - (1 - \alpha) (\frac {p _ {g b}}{2 k _ {h} - \alpha} - \frac {p _ {b g}}{\frac {1}{M} - \alpha})}{k _ {h} [ (\frac {p _ {g b}}{2 k _ {h} - \alpha}) ^ {2} - (\frac {p _ {b g}}{2 k _ {h} (1 - \alpha M)}) ^ {2} ]}.\tag{32}
$$

The equilibrium levels of $v _ { d }$ and m can be solved through (28) and (32).

For low types, denote their deviating efort and profit as $w _ { l } ^ { \prime }$ and $\pi _ { l } ^ { \prime } .$ . If they deviate to a Good reputation, their incentive can be described through the first-order condition as $\alpha w _ { h } - 2 k _ { l } w _ { l } ^ { \prime } +$ $\beta p _ { g b } v _ { d } = 0$ , which leads to $\begin{array} { r } { w _ { l } ^ { \prime } = \frac { k _ { h } } { k _ { l } } w _ { h } } \end{array}$ . For low types to prefer Bad reputations to Good reputations, we need $\pi _ { l } ^ { \prime } < \pi _ { l } .$ , or equivalently

$$
k _ {l} (w _ {l} ^ {' 2} - w _ {l} ^ {2}) + (1 - \alpha) (w _ {h} - w _ {b}) + (\beta (1 - p _ {g b}) - 1) v _ {d} <   0.
$$

Note that $\begin{array} { r } { w _ { l } ^ { \prime } = \frac { k _ { h } } { k _ { l } } w _ { h } } \end{array}$ and $\begin{array} { r } { w _ { l } = \frac { k _ { h } } { k _ { l } } w _ { h b } . } \end{array}$ , and $\begin{array} { r } { \frac { k _ { h } } { k _ { l } } \ < \ 1 } \end{array}$ . The above IC condition holds as long as $w _ { l } ^ { \prime } > w _ { l }$ , which can be simplified to the condition on $\frac { p _ { g b } } { p _ { b g } }$ in Proposition 4.

We also need to ensure that $m \in [ 0 , 1 ]$ in equilibrium. First, notice that both M and $\beta v _ { d }$ are decreasing in $m$ . We then rearrange Equation (28) as

$$
\lambda_ {h} m (1 - w _ {h}) p _ {g b} = \lambda_ {h} (1 - m) w _ {h b} p _ {b g} + (1 - \lambda_ {h}) w _ {l} p _ {b g}
$$

Note that the left-hand side (LHS) of this equation is increasing in m while the right-hand side (RHS) of the equation is decreasing in m. In order for m to be between 0 and 1, it sufices to show that (1) when $m \ : = \ : 0 , \ : L H S \ : < \ : R H S$ in Equation (28); and (2) when $m = 1$ $L H S ~ >$ RHS in Equation (28). When $m \ = \ 0$ , we have $\begin{array} { r } { M \ = \ \frac { \lambda _ { h } } { 2 k _ { h } } + \frac { 1 - \lambda _ { h } } { 2 k _ { l } } } \end{array}$ , $L H S \ = \ 0 .$ , and $R H S =$ $\begin{array} { r } { \big ( \frac { \lambda _ { h } } { 2 k _ { h } ( 1 - \alpha M ) } + \frac { 1 - \lambda _ { h } } { 2 k _ { l } ( 1 - \alpha M ) } \big ) p _ { b g } ^ { 2 } \beta v _ { d } } \end{array}$ . The condition that $R H S > L H S = 0$ is equivalent to $\beta v _ { d } > 0$ or $\beta < \beta _ { 2 }$ , where $\beta _ { 2 }$ is defined as in Equation (18). Similarly, when $m = 1$ , we have $\begin{array} { r } { M = \frac { 1 } { 2 k _ { l } } } \end{array}$ $\begin{array} { r } { L H S = \lambda _ { h } ( 1 - \frac { p _ { g b } } { 2 k _ { h } - \alpha } \beta v _ { d } ) p _ { g b } } \end{array}$ , and $\begin{array} { r } { R H S = \frac { 1 - \lambda _ { h } } { 2 k _ { l } - \alpha } p _ { b g } ^ { 2 } \beta v _ { d } } \end{array}$ . The condition $L H S > R H S$ is equivalent to $\begin{array} { r } { \beta v _ { d } < \frac { \lambda _ { h } p _ { g b } } { \frac { \lambda _ { h } } { 2 k _ { h } - \alpha } p _ { g b } ^ { 2 } + \frac { 1 - \lambda _ { h } } { 2 k _ { l } - \alpha } p _ { b g } ^ { 2 } } } \end{array}$ , or $\beta > \beta _ { 1 }$ , where $\beta _ { 1 }$ is defined as in Equation (17). It is easy to show that $\beta _ { 1 } < \beta _ { 2 }$ because

$$
\frac {\lambda_ {h} k _ {h} [ (\frac {p _ {g b}}{2 k _ {h} - \alpha}) ^ {2} - (\frac {p _ {b g}}{2 k _ {h} - \frac {k _ {h}}{k _ {l}} \alpha}) ^ {2} ]}{\frac {\lambda_ {h}}{2 k _ {h} - \alpha} p _ {g b} ^ {2} + \frac {1 - \lambda_ {h}}{2 k _ {l} - \alpha} p _ {b g} ^ {2}} > 0
$$

In addition, we also need to ensure $\beta _ { 1 } < 1$ , which leads to condition $\frac { \lambda _ { l } } { \lambda _ { h } } < \lambda _ { 1 }$ where $\lambda _ { 1 }$ is defined

as in Equation (19).

## A.5. Proof to Proposition 5

The equilibrium satisfies the following conditions:

$$
\begin{array}{r c l} {w _ {g}} & = & {\frac {\lambda_ {h} w _ {h} + (1 - \lambda_ {h}) n w _ {l g}}{\lambda_ {h} + (1 - \lambda_ {h}) n};} \\ {w _ {h}} & = & {\frac {\alpha w _ {g} + \beta p _ {g b} v _ {d}}{2 k _ {h}};} \\ {w _ {l g}} & = & {\frac {\alpha w _ {g} + \beta p _ {g b} v _ {d}}{2 k _ {l}};} \\ {w _ {l}} & = & {\frac {\beta p _ {b g} v _ {d}}{2 k _ {l} - \alpha};} \\ {(1 - \lambda_ {h}) (1 - n) w _ {l} p _ {b g}} & = & {\lambda_ {h} (1 - w _ {h}) p _ {g b} + (1 - \lambda_ {h}) n (1 - w _ {l g}) p _ {g b}.} \end{array}\tag{33}
$$

The first three equations lead to

$$
w _ {g} = \frac {\beta p _ {g b} v _ {d}}{\frac {1}{N} - \alpha};\tag{34}
$$

$$
w _ {h} = \frac {\beta p _ {g b} v _ {d}}{2 k _ {h} (1 - \alpha N)};\tag{35}
$$

$$
{w _ {l g}} = {\frac {\beta p _ {g b} v _ {d}}{2 k _ {l} (1 - \alpha N)},}\tag{36}
$$

where $\begin{array} { r } { N = \frac { \frac { \lambda _ { h } } { 2 k _ { h } } + \frac { ( 1 - \lambda _ { h } ) n } { 2 k _ { l } } } { \lambda _ { h } + ( 1 - \lambda _ { h } ) n } } \end{array}$

Low types at Good and Bad reputations must be indiferent; that is, $\pi _ { l } = \pi _ { l g }$ , which leads to

$$
k _ {l} (w _ {l g} ^ {2} - w _ {l} ^ {2}) + (1 - \alpha) (w _ {g} - w _ {l}) + (\beta (1 - p _ {g b}) - 1) v _ {d} = 0.
$$

We can solve for $v _ { d }$ by substituting in Equations (34) to (36) as

$$
\beta v _ {d} = \frac {- \frac {1}{\beta} + (1 - p _ {g b}) + (1 - \alpha) (\frac {p _ {g b}}{\frac {1}{N} - \alpha} - \frac {p _ {b g}}{2 k _ {l} - \alpha})}{k _ {l} [ (\frac {p _ {b g}}{2 k _ {l} - \alpha}) ^ {2} - (\frac {p _ {g b}}{2 k _ {l} (1 - \alpha N)}) ^ {2} ]}.\tag{37}
$$

The equilibrium level of $v _ { d }$ and n are determined by (33) and (37).

For high types, denote their deviating efort and profit as $w _ { h } ^ { \prime }$ and $\pi _ { h } ^ { \prime }$ . If they deviate to a Bad reputation, their incentive can be described through the first-order condition as αw<sub>l</sub> −

$2 k _ { h } w _ { H } ^ { \prime } + \beta p _ { b g } v _ { d } = 0$ , which leads to $\begin{array} { r } { w _ { h } ^ { \prime } = \frac { k _ { l } } { k _ { h } } w _ { l } } \end{array}$ . For high types to prefer Good reputations to Bad reputations, we need $\pi _ { h } ^ { \prime } < \pi _ { h }$ , or equivalently

$$
k _ {h} (w _ {h} ^ {' 2} - w _ {h} ^ {2}) + (1 - \alpha) (w _ {l} - w _ {g}) - (\beta (1 - p _ {g b}) - 1) v _ {d} <   0.
$$

Note that $\begin{array} { r } { w _ { h } ^ { \prime } = \frac { k _ { l } } { k _ { h } } w _ { l } } \end{array}$ and $\begin{array} { r } { w _ { h } = \frac { k _ { l } } { k _ { h } } w _ { l g } . } \end{array}$ , and $\begin{array} { r } { \frac { k _ { l } } { k _ { h } } > 1 } \end{array}$ . The above IC condition holds as long as $w _ { h } ^ { \prime } > w _ { h }$ , which can be simplified to the condition on $\frac { p _ { g b } } { p _ { b g } }$ in Proposition 5.

We also need to ensure that in equilibrium $n \in [ 0 , 1 ]$ . First, notice that both N and $\beta v _ { d }$ are decreasing in $n ,$ which can be verified with simple algebra. We then rearrange Equation (33) as

$$
(1 - \lambda_ {h}) (1 - n) w _ {l} p _ {b g} = \lambda_ {h} (1 - w _ {h}) p _ {g b} + (1 - \lambda_ {h}) n (1 - w _ {l g}) p _ {g b},\tag{38}
$$

Notice that the left-hand side of this equation is decreasing in n while the right-hand side is increasing in n. For the equilibrium n to be between 0 and 1, it must satisfy two conditions: (1) when $n = 0$ , Equation (38) becomes an inequality with the left-hand side (LHS) greater than the right-hand side (RHS); and (2) when $n = 1$ , Equation (38) becomes an inequality with the left-hand side less than the right-hand side. At $\begin{array} { r } { n \ = \ 0 , \ N \ = \ \frac { 1 } { 2 k _ { h } } \ , \ L H S \ = \ \frac { ( 1 - \lambda _ { h } ) p _ { b g } ^ { 2 } } { 2 k _ { l } - \alpha } \beta v _ { d } } \end{array}$ , and $\begin{array} { r } { R H S = \lambda _ { h } p _ { g b } ( 1 - \frac { \beta p _ { g b } v _ { d } } { 2 k _ { h } - \alpha } ) } \end{array}$ . The equivalent condition of $L H S > R H S$ is

$$
\beta v _ {d} = \frac {- \frac {1}{\beta} + (1 - p _ {g b}) + (1 - \alpha) (\frac {p _ {g b}}{2 k _ {h} - \alpha} - \frac {p _ {b g}}{2 k _ {l} - \alpha})}{k _ {l} [ (\frac {p _ {b g}}{2 k _ {l} - \alpha}) ^ {2} - (\frac {p _ {g b}}{2 k _ {l} - \frac {k _ {l}}{k _ {h}} \alpha}) ^ {2} ]} > \frac {\lambda_ {h} p _ {g b}}{\frac {(1 - \lambda_ {h}) p _ {g b} ^ {2}}{2 k _ {l} - \alpha} + \frac {\lambda_ {h} p _ {g b} ^ {2}}{2 k _ {h} - \alpha}}
$$

Similarly, when $n = 1$ , then $\begin{array} { r } { N = { \frac { \lambda _ { h } } { 2 k _ { h } } } + { \frac { 1 - \lambda _ { h } } { 2 k _ { l } } } , L H S = 0 } \end{array}$ , and $R H S > 0$ is equivalent to

$$
\beta v _ {d} = \frac {- \frac {1}{\beta} + (1 - p _ {g b}) + (1 - \alpha) (\frac {p _ {g b}}{\frac {1}{N} - \alpha} - \frac {p _ {b g}}{2 k _ {l} - \alpha})}{k _ {l} [ (\frac {p _ {b g}}{2 k _ {l} - \alpha}) ^ {2} - (\frac {p _ {g b}}{2 k _ {l} (1 - \alpha N)}) ^ {2} ]} <   \frac {1}{(\frac {\lambda_ {h}}{2 k _ {h} (1 - \alpha N)} + \frac {1 - \lambda_ {h}}{2 k _ {l} (1 - \alpha N)}) p _ {g b}}
$$

The corresponding condition in terms of $\beta$ becomes $\beta _ { 3 } < \beta < \beta _ { 4 }$ , where $\beta _ { 3 }$ and $\beta _ { 4 }$ are defined as in Equations (20) and (21). We can verify that $\beta _ { 3 } < \beta _ { 4 }$ . In addition, we also need to ensure $\beta _ { 3 } < 1$ and $\beta _ { 4 } > 0$ , for which it sufices to show that $\begin{array} { r } { \frac { 1 } { \beta _ { 3 } } > 1 } \end{array}$ , or equivalently, $\frac { \lambda _ { l } } { \lambda _ { h } } > \lambda _ { 2 }$ where $\lambda _ { 2 }$ is defined as in Equation (22).

## A.6. Proof of Proposition 6

Consider an equilibrium where (1) low types own reputation $j = 0 ,$ , and high types have all the rest; (2) the reputation value diference is such that $v _ { 1 } - v _ { 0 } = a$ , and $v _ { j } - v _ { j - 1 } = b { \mathrm { ~ f o r ~ } } j \geq 2$ . The corresponding equilibrium eforts and profits are

$$
\begin{array}{r c l} {w _ {0}} & = & {\frac {a}{2 k _ {l} - \alpha};} \\ {\pi_ {0}} & = & {k _ {l} w _ {0} ^ {2} + (1 - \alpha) w _ {0};} \\ {w _ {1}} & = & {\frac {a + b}{2 k _ {h} - \alpha};} \\ {\pi_ {1}} & = & {k _ {h} w _ {1} ^ {2} + (1 - \alpha) w _ {1} - a;} \\ {w _ {j \geq 2}} & = & {\frac {2 b}{2 k _ {h} - \alpha};} \\ {\pi_ {j \geq 2}} & = & {k _ {h} w _ {j} ^ {2} + (1 - \alpha) w _ {j} - b.} \end{array}\tag{39}
$$

The separating equilibrium has to satisfy the following five conditions.

Condition 1: $\pi _ { 1 } = \pi _ { j \geq 2 }$ , which leads to

$$
a + 3 b = \frac {(2 k _ {h} - 1) (2 k _ {h} - \alpha)}{k _ {h}}.\tag{40}
$$

Condition 2: the proportion of reputation 0 is $\lambda _ { 0 } = 1 - \lambda _ { h }$

Condition 3: the proportion of all the other reputations are such that $\begin{array} { r } { \lambda _ { 1 } = \lambda _ { 0 } \frac { \frac { 2 } { 2 k _ { l } - \alpha } } { 1 - \frac { a + b } { 2 k _ { h } - \alpha } } , \lambda _ { 2 } = } \end{array}$ $\lambda _ { 1 } \frac { a + b } { 2 k _ { h } - \alpha - 2 b }$ , and $\begin{array} { r } { \lambda _ { j \ge 3 } = \lambda _ { j - 1 } \frac { 2 b } { 2 k _ { h } - \alpha - 2 b } } \end{array}$ . The aggregate of these proportions must be $\lambda _ { h } ;$ ; that is,

$$
\frac {\frac {2}{2 k _ {l} - \alpha}}{1 - \frac {a + b}{2 k _ {h} - \alpha}} (1 + \frac {a + b}{2 k _ {h} - \alpha - 4 b}) = \frac {\lambda_ {h}}{1 - \lambda_ {h}}.\tag{41}
$$

Condition 4 (ICH): H-types prefer $j \geq 1$ to $0 ;$ that is,

$$
k _ {h} (\frac {2 b}{2 k _ {h} - \alpha}) ^ {2} + (1 - \alpha) \frac {2 b}{2 k _ {h} - \alpha} - b \geq \frac {k _ {l}}{k _ {h}} \left[ k _ {l} (\frac {a}{2 k _ {l} - \alpha}) ^ {2} + (1 - \alpha) \frac {a}{2 k _ {l} - \alpha} \right].\tag{42}
$$

This is equivalent to $\begin{array} { r } { \pi _ { h } \geq \frac { k _ { l } } { k _ { h } } \pi _ { l } } \end{array}$

Condition 5 (ICL): L-types prefer $0 \mathrm { ~ t o ~ } j \geq 1 ;$ ; that is,

$$
k _ {l} (\frac {a}{2 k _ {l} - \alpha}) ^ {2} + (1 - \alpha) \frac {a}{2 k _ {l} - \alpha} \geq \frac {k _ {h}}{k _ {l}} \left[ k _ {h} (\frac {2 b}{2 k _ {h} - \alpha}) ^ {2} + (1 - \alpha) \frac {2 b}{2 k _ {h} - \alpha} \right] - b,\tag{43}
$$

which is equivalent to $\begin{array} { r } { \pi _ { l } \geq \frac { k _ { h } } { k _ { l } } \pi _ { h } - ( 1 - \frac { k _ { h } } { k _ { l } } ) b } \end{array}$

We prove the existence of such an equilibrium in two steps.

Step 1: We want to show that Equation (41) simply moves the equilibrium along the line described by Equation (40). In other words, as $\frac { \lambda _ { h } } { 1 - \lambda _ { h } }$ varies from 0 to ∞, the corresponding variations of a and b covers every single point in Equation (40).

First, substitute Equation (40) into Equation (41) and rewrite the latter as a function of b only.

$$
\lambda \equiv \frac {\lambda_ {h}}{1 - \lambda_ {h}} = \frac {M - 3 b}{N - 4 b} \frac {N + M - 6 b}{N - M + 2 b},
$$

where $\begin{array} { r } { M = \frac { ( 2 k _ { h } - \alpha ) ( 2 k _ { h } - 1 ) } { k _ { h } } } \end{array}$ , and $N = 2 k _ { h } - \alpha$ . Notice that

$$
\frac {\partial \lambda}{\partial b} = \frac {6 0 N b ^ {2} + (3 6 N ^ {2} - 2 0 M N + 1 6 M ^ {2}) b + (7 M ^ {2} N - 4 M N ^ {2} - 3 N ^ {3} - 4 M ^ {3})}{(N - 4 b) ^ {2} (N - M + 2 b) ^ {2}}
$$

and $6 0 N > 0 , 3 6 N ^ { 2 } - 2 0 M N + 1 6 M ^ { 2 } > 0$ , and $7 M ^ { 2 } N - 4 M N ^ { 2 } - 3 N ^ { 3 } - 4 M ^ { 3 } < 0 . ^ { 8 }$ Hence, λ decreases in b when b is small, and increases in b when b is large.

We also need to check whether Equation (41) itself implies any restrictions on the variations of b. The only condition that has to be satisfied is $\lambda \ge 0$ . Note that, $2 k _ { h } - \alpha - ( a + b ) > 0$ is equivalent to $\begin{array} { r } { 2 b > \frac { ( 2 k _ { h } - \alpha ) ( k _ { h } - 1 ) } { k _ { h } } } \end{array}$ , which is always true because $k _ { h } - 1 < 0$ . Similarly, $2 k _ { h } - \alpha - 3 b + a \ge 0$ leads to $\begin{array} { r } { 2 a \ge \frac { ( 2 k _ { h } - \alpha ) ( k _ { h } - 1 ) } { k _ { h } } } \end{array}$ , which is also true for all $a \geq 0$ . Lastly, $2 k _ { h } - \alpha - 4 b > 0$ leads to $\begin{array} { r } { b < \frac { 2 k _ { h } - \alpha } { 4 } } \end{array}$ , which is equivalent to $\begin{array} { r } { a \ge \frac { ( 2 k _ { h } - \alpha ) ( \frac { 5 } { 4 } k _ { h } - 1 ) } { k _ { h } } } \end{array}$ because $\begin{array} { r } { b = \frac { ( 2 k _ { h } - 1 ) ( 2 k _ { h } - \alpha ) } { 3 k _ { h } } - \frac { a } { 3 } } \end{array}$ . Note that, if $\begin{array} { r } { k _ { h } \le \frac { 4 } { 5 } } \end{array}$ , the inequality always holds. Otherwise, Equation (41) imposes the additional condition that $\begin{array} { r } { b > \frac { 2 k _ { h } - \alpha } { 4 } } \end{array}$

So, when $k _ { h } \le \frac { 4 } { 5 } , \lambda$ first decreases and then increases in $b ,$ as b goes up. In this case, every point on the line in (40) can be reached at a certain λ, and we only need to find one point on (40) to demonstrate the existence of separation. When $\begin{array} { r } { k _ { h } > \frac { 4 } { 5 } } \end{array}$ , λ first decreases and then increases in $b ,$ and goes to infinity as b approaches $\frac { 2 k _ { h } - \alpha } { 4 }$ . This way, Equation (41) covers only part of the line in (40); that is, $\begin{array} { r } { 0 \leq b < \frac { 2 k _ { h } - \alpha } { 4 } } \end{array}$ . We need to find a point within this range that satisfies the ICs to show the existence of separation.

Step 2: Reorganizing the ICH and ICL by substituting in $a = M - 3 b$ , we have

$$
k _ {h} b \leq (\frac {2 b k _ {h}}{2 k _ {h} - \alpha}) ^ {2} - (\frac {(M - 3 b) k _ {l}}{2 k _ {l} - \alpha}) ^ {2} + (1 - \alpha) (\frac {2 b k _ {h}}{2 k _ {h} - \alpha} - \frac {(M - 3 b) k _ {l}}{2 k _ {l} - \alpha}) \leq k _ {l} b
$$

We denote the middle expression as $T ( b )$ . Notice that

$$
\frac {\partial T}{\partial b} = (\frac {k _ {h}}{2 k _ {h} - \alpha}) ^ {2} 8 b + (\frac {k _ {l}}{2 k _ {l} - \alpha}) ^ {2} 6 (M - 3 b) + (1 - \alpha) (\frac {2 k _ {h}}{2 k _ {h} - \alpha} + \frac {3 k _ {l}}{2 k _ {l} - \alpha}) > 0,
$$

$T ( 0 ) < 0 .$ , and $T ( M / 3 ) > 0$ . Hence, as long as $T ( b \ : = \ : M / 3 ) \ : \geq \ : k _ { h } b$ when $k _ { h } ~ \le ~ \frac { 4 } { 5 }$ , or $T ( b =$ $\frac { 2 k _ { h } - \alpha } { 4 } ) \geq k _ { h } b$ when $\begin{array} { r } { k _ { h } > \frac { 4 } { 5 } } \end{array}$ , a separation must exist. When $\begin{array} { r } { k _ { h } \le \frac { 4 } { 5 } } \end{array}$ , substituting in $\begin{array} { r } { b = \frac { M } { 3 } } \end{array}$ , we need $\begin{array} { r } { ( \frac { 2 b k _ { h } } { 2 k _ { h } - \alpha } ) ^ { 2 } + ( 1 - \alpha ) \frac { 2 b k _ { h } } { 2 k _ { h } - \alpha } - k _ { h } b \geq 0 } \end{array}$ , which leads to $\begin{array} { r } { k _ { h } \geq \frac { 3 } { 2 } \alpha - 1 } \end{array}$ . In order for $\begin{array} { r } { 0 \leq k _ { h } \leq \frac { 4 } { 5 } } \end{array}$ , α has to satisfy that $\textstyle { \frac { 2 } { 3 } } \leq \alpha \leq 1$ . Therefore, when $\begin{array} { r } { \frac { 2 } { 3 } \leq \alpha \leq 1 } \end{array}$ and $\textstyle { \frac { 3 } { 2 } } \alpha - 1 \leq k _ { h } \leq { \frac { 4 } { 5 } }$ , there exists a separating equilibrium.
