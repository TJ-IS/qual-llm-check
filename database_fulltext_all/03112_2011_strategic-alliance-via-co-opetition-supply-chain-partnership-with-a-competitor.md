---
otero_id: 3112
otero_key: "PU8SB2V7"
title: "Strategic alliance via co-opetition: Supply chain partnership with a competitor"
authors: "Jie Zhang; Gregory V. Frazier"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic alliance via co-opetition: Supply chain partnership with a competitor

Jie Zhang ⁎, Gregory V. Frazier

Department of Information Systems and Operations Management, The University of Texas at Arlington, Arlington, TX 76019, United State

a r t i c l e i n f o

Available online 7 February 2011

Keywords: Co-opetition Partnership Alliance Nash bargaining Two-part tariff contract Learning

## a b s t r a c t

Why do two competitors form an alliance yet still compete with each other in the marketplace? Consider Yahoo's recent alliance with Microsoft to use its Bing search engine, yet both companies will compete with each other to sell search ads. In this paper we study dynamic alliance formation among competing <sup>fi</sup>rms with a multi-period model. In each period, there is a two-stage game of co-opetition. In Stage 1, two competing <sup>fi</sup>rms decide on forming a partnership by negotiating a contractual agreement; and in Stage 2, all <sup>fi</sup>rms in the market engage in price competition. We formulate the economic incentives and costs of the cooperation, propose the optimal contract and discuss the reasons for a temporary co-opetition and a delayed co-opetition. The results of the paper shed light on <sup>fi</sup>rms' strategic decision on co-opetition and provide implications to public policy makers.

© 2011 Elsevier B.V. All rights reserved.

“You have to compete and cooperate at the same time.” − Ray Noorda, Novell

## 1. Introduction

It is no longer the case that <sup>fi</sup>rms perform all the vital functions inhouse to build and maintain competitive advantages rather than partnering with other <sup>fi</sup>rms to execute some of the business activities. The boundary of <sup>fi</sup>rms traditionally being explained as a result of transaction cost [20,35] and competitive advantages [30,31] has been changed in the networked world. Collaborations and alliances among different business entities arise in various markets. This paper studies the formation of a speci<sup>fi</sup>c type of “co-opetition” [5], a supply chain partnership between competing <sup>fi</sup>rms with different competencies through a contractual agreement to meet each other's strategic objectives such as expanding market share, enhancing ef<sup>fi</sup>ciency, entry to a new channel, etc.

Numerous such supply chain partnerships exist in the retail and service industries. For example, after Amazon.com developed an innovative IT-enabled supply chain, Borders sought to leverage it instead of trying to match it since Borders would have had a harder time achieving similar ef<sup>fi</sup>ciencies with a smaller consumer base. The Borders Group partnered with Amazon.com under a long-term contract in 2001. Under the agreement Amazon.com provided design and underlying technology to its rival bookseller's Web site, took over customer service and order ful<sup>fi</sup>llment, and was compensated by sharing a portion of the sales from Borders.com. Toys ‘R’ Us and Target also formed a similar form of collaboration with Amazon.com in 2000 and 2001, respectively. The Walt Disney Company partnered with eBay.com to build a co-branded shopping website in 2000; and Yahoo partnered with Microsoft's Bing in 2010 to use its search engine. Those successful co-opetition cases result in a win–win situation for both partners. They leveraged synergies with each other, gained quicker entry into the online markets, and developed new competencies [9]. This collaborative relationship, however, may not always sustain. Borders ended the collaboration with Amazon and launched a new Web site to sell to its online customers in early 2008. Toys ‘R’ Us terminated the collaboration of building a co-branded online store with Amazon.com before the end of the ten-year contract and started to run its retail website independently in 2006. Disney ended their partnership with eBay and moved the Disney Auction website under its own banner as of fall of 2006.

Speci<sup>fi</sup>cally, we examine in an oligopolistic market a high-cost <sup>fi</sup>rm that partners with a low-cost <sup>fi</sup>rm based on a contract so that the lowcost <sup>fi</sup>rm produces goods or provides services for the high-cost <sup>fi</sup>rm for a payment. Firms negotiate the contract by bargaining the surplus from the alliance [25]. Subsequent to the contract negotiation, both <sup>fi</sup>rms proceed to engage in a price competition that also involves a third “outside” competitor that takes no part in the alliance. Following the contracting literature [32], we model the contract as a two-part tariff form (a <sup>fi</sup>xed payment plus a unit payment), which is consistent with business practices. For example, Amazon.com and Toys ‘R’ Us partnered based on such contractual terms that, “Under the terms of the 10-year agreement, Amazon.com will be compensated through a combination of periodic <sup>fi</sup>xed payments, per unit payments and single-digit percentage of revenue. All parties, including Toys ‘R’ Us, Inc., will market the cobranded store to their respective customers.”

In addition, we also inspect the possible effects of intertemporal ef<sup>fi</sup>ciency gains on optimal contracting with a dynamic model. Considering the learning-by-doing effect (i.e. it becomes increasingly ef<sup>fi</sup>cient over time through learning from its own experiences or spillovers from the alliance), we <sup>fi</sup>nd it may be optimal for the high-cost <sup>fi</sup>rm to terminate a partnership at some point in time and subsequently move to self-suf<sup>fi</sup>cient production or services, or to delay the alliance after an initial period of self production or services.

Based on the above setting, we intend to examine the following research questions:

1) Why and when should a high-cost <sup>fi</sup>rm overcome the ef<sup>fi</sup>ciency disadvantage by forming an alliance with a low-cost competitor? Is the low-cost <sup>fi</sup>rm interested in forming the alliance given that it already enjoys a substantial cost-advantage?

2) What are the factors that affect the optimal co-opetition contract?

3) What are the implications of the co-opetition on the partner <sup>fi</sup>rms as well as on the outside competitor? Does such a co-opetition hurt consumers? What is the impact of the co-opetition on social welfare?

The paper is organized as follows. Section 2 reviews the relevant literature. Section 3 presents a single-period competitive model and characterizes the strategic behavior of <sup>fi</sup>rms in the market with and without collaboration. It provides the incentive and tradeoffs for <sup>fi</sup>rms to partner. The decision process is analyzed with a two-stage game with each stage discussed in Subsections 3.1 and 3.2, respectively, and the impacts of a co-opetition practice on market competition and economic welfare are investigated in Subsection 3.4. Section 4 examines the optimal timing and duration of co-opetitions in a dynamic setting. Section 5 summarizes the major results and discusses the insights and implications. Conclusion and further research directions are provided in Section 6. All proofs to the propositions and corollaries are provided in the Appendix A.

## 2. Literature review

The model setting of this paper is relevant to the literature on licensing of cost-reducing innovations [14,21,32], where subsequent to the license contract of a cost-reducing technology (with both a <sup>fi</sup>xed fee and a per-unit royalty) in an oligopolist market, the licensee and licensor <sup>fi</sup>rms, which produce imperfect substitute goods, proceed to engage in a price competition. However, due to the difference in market structure, the licensing contracts in prior studies are based on either an auction mechanism [32] or a take-it-or-leave-it offer by the licensor [14,21], while our supply chain co-opetition contract is based on bargaining between the partners. We also contribute to the general licensing theory by examining an expanded market setting with an outside competitor and a repeated licensing game.

Research on supply chain coordination through contracts proposes contracts of various formats (See Cachon [6] and Kouvelis et al. [22] for detailed literature reviews): buy-back contracts [29], quantity <sup>fl</sup>exibility contracts [33], revenue sharing contracts [7], VMI with revenue sharing contracts [15], and information sharing [36]. All those contractual relationships are examined under a vertical supply chain environment, e.g. between a supplier and an assembler, as are most other supply chain partnership studies [8,10,13,19]. We, however, study a revenue sharing contract in a horizontal supply chain, that is, between two competitors in the same market.

Some related works should be further mentioned. Granot and Sosic [16], Nagarajan and Sosic [26] and Granot and Yin [17] have also analytically studied cooperation of competing <sup>fi</sup>rms in a market. This paper differs from them in the following ways: 1) We consider a more complete problem including endogenizing alliance contract negotiation and discussing the renewal/breakup of the alliance in a dynamic setting; 2) The co-opetition in this paper is formed based on a mutually agreed contract, whereas Granot and Sosic [16] simplify the impact of a coalition on each member as an exogenously determined and reduced wholesale price, and Nagarajan, and Sosic [26] assume that all coalition members tacitly agree to set the same price; 3) We assume that partners remain competitors and have control over their own pricing (and quantity) decisions, whereas Granot and Sosic [16] and Nagarajan, and Sosic [26] explicitly model the within-coalition pricing/inventory decisions as a cooperative result; 4) In contrast to the results in Granot and Sosic [16] and Oum et al. [28], we <sup>fi</sup>nd that the “outsider” may not be worse off after the formation of the alliance of its competitors.

This paper differs from Long and Soubeyran [23] who model a twostage game of <sup>fi</sup>rm co-opetition in the following ways: 1) Long and Soubeyran does not consider a speci<sup>fi</sup>c contractual relationship like this paper but rather abstracts the cooperation mechanism with a costsaving parameter e which directly affects <sup>fi</sup>rms' costs; 2) while the marginal costs of <sup>fi</sup>rms are either collusively determined or under the direct in<sup>fl</sup>uence of a dominant actor (cost manipulation) in Long and Soubeyran, they are endogenously determined by a Nash Bargaining game in this paper; 3) Long and Soubeyran does not consider the multiperiod game of repeated co-opetitions as in this paper.

## 3. Model of the co-opetition game

Consider three <sup>fi</sup>rms competing in the same market selling substitutable goods that are horizontally differentiated in product attributes, brand names, company images, or customer relationships. Demandof <sup>fi</sup>rm $i , q _ { i } ,$ is a function of its own price ${ \mathrm { . } p } _ { i } ,$ , and the competitors' prices, $p _ { - i }$ . Following Vives [34], we de<sup>fi</sup>ne the demand function as

$$
q _ {i} (p _ {i}, p _ {- i}) = a - p _ {i} + d \left(p _ {j} + p _ {k}\right), \quad i, j, k = 1, 2, 3 \text {   and   } i \neq j \neq k\tag{1}
$$

in which a represents the total market size, and d denotes the degree of demand substitution (the effect that one <sup>fi</sup>rm's price change has on the demand of the other <sup>fi</sup>rms). To render the interpretation meaningful, we impose the <sup>fi</sup>nite market restriction that $0 { < } d { < } \frac { 1 } { 2 }$ such that the substitutability is limited — the three products cannot perfectly substitute for each other or one for the combination of the other two. We assume that the functional form of each <sup>fi</sup>rm's demand remains the same after forming the alliance to eliminate the demand externality as the incentive for <sup>fi</sup>rms to collaborate. We further assume a linear cost function and a sunk <sup>fi</sup>xed cost to rule out economy of scale as a motive for the alliance. Instead we focus on incentives that arise solely from sharing complementary competence.

Suppose two of the three <sup>fi</sup>rms are more ef<sup>fi</sup>cient in certain operational or marketing activities than the other <sup>fi</sup>rm; let's say they are more experienced and advanced in supply chain management, order ful<sup>fi</sup>llment or in customer services. We label the ef<sup>fi</sup>cient <sup>fi</sup>rms as Firm 1 and Firm 2 and normalize their marginal costs to zero; while Firm 3 has a relatively higher marginal cost $c > 0 .$ Firm 2 is a representative “outsider” that only competes with the other <sup>fi</sup>rms in the market but does not participate in the alliance. Firm 1 and Firm 3 have complementary needs: Firm 3 has incentive to share Firm 1's advantages in those activities and Firm 1 aims at Firm 3's market share. Firm 1 incurs a cost of $\dot { c } _ { 1 }$ for each unit of goods produced or sold for Firm 3, which is lower than Firm 3's marginal cost, that is, $0 { \leq } c _ { 1 } { \leq } c .$ In addition, Firm 1 and Firm 3 each incur a cost in forming and monitoring the alliance, denoted by $c _ { k 1 }$ and $c _ { k 3 }$ respectively.

We model the co-opetition game as a multi-period dynamic process: for each round of alliance, we envisage a two-stage game: Firms 1 and 3 decide whether to collaborate through negotiating a contract in stage I before all <sup>fi</sup>rms engage in price competition in stage II; at the end of an alliance, the two partner <sup>fi</sup>rms decide whether to renew or discontinue the relationship according to their updated status (Fig. 1).

The alliance contract speci<sup>fi</sup>es that Firm 1 will provide certain manufacturing or service activities for Firm 3 and will receive payment $R ( q )$ based on quantity produced or sold q. We assume the transfer payment is in the form of a two part tariff which incorporates a <sup>fi</sup>xed fee f and a per unit payment $r ,$ that is, $R ( q ) = r q + f  \cal $ . This two-part tariff contract is more general than the exclusive unit $( f { = } 0 )$ or <sup>fi</sup>xed fee $( r { = } 0 )$ payment contract because they are both reduced forms of a twopart tariff contract.

<table><tr><td>Stage I</td><td>Stage II</td></tr><tr><td>Firms 1 and 3 collaborate by negotiating a contract with payment (r, f).</td><td>If successful, then Firm 1 takes over certain manufacturing or service activities for Firm 3 and receives payment according to the contract.</td></tr></table>

Fig. 1. Sequence of events

We start with a one-period co-opetition game and examine the renewal decision in Section 4. As the model is solved backwards, the analysis starts by considering the price competition stage in Subsection 3.1 before we go back to the contracting stage in Subsection 3.2.

## 3.1. Stage II — price competition

Depending on the result of the cooperative contracting stage, there are two scenarios of price competition in the second stage: Case 1) If the alliance is not formed between Firm 1 and Firm 3, then the three <sup>fi</sup>rms engage in an oligopoly price competition — each <sup>fi</sup>rm makes its own pricing decision independently to maximize pro<sup>fi</sup>t, taking the other <sup>fi</sup>rms' responses into account. Case 2) Otherwise, all <sup>fi</sup>rms will consider the alliance contract when making price decisions.

## 3.1.1. Case 1: oligopoly competition

When no alliance is formed and the three <sup>fi</sup>rms separately compete with each other on price, Firm i $( i = 1 , 2 , 3 )$ maximizes its own pro<sup>fi</sup>t, taking into account the other <sup>fi</sup>rms' responses. (Table 1 provides a list of variable descriptions.)

$$
\begin{array}{l} \max _ {p _ {i}} \Pi_ {i} = (p _ {i} - c _ {i}) q _ {i} (p _ {i}, p _ {- i}) \\ \text { s.t. } \qquad q _ {i} (p _ {i}, p _ {- i}) \geq 0 \end{array}\tag{2}
$$

Due to the demand substitution among the three <sup>fi</sup>rms, Firm 3 can successfully stay active in the market only if its cost is below a certain level, $\frac { ( 2 + d ) a } { 2 - d - 2 d ^ { 2 } } .$ . Otherwise, it cannot price above its marginal cost and earn positive demand at the same time. We summarize the oligopoly equilibrium results (with a superscript O) in Lemma 1.

Lemma 1. When $c { \leq } \frac { ( 2 + d ) a } { 2 { - } d { - } 2 d ^ { 2 } } ,$ , there exists a unique Bertrand-Nash equilibrium: all firms charge prices higher than their marginal cost $\dot { p _ { i } ^ { 0 } } = \frac { a ( 2 + d ) + d c } { 2 ( 2 - d - d ^ { 2 } ) } , p _ { 3 } ^ { 0 } = \frac { \dot { a } ( 2 + d ) ^ { 2 } + ( 2 - d ) c } { 2 ( 2 - d - d ^ { 2 } ) } .$ Their demands are $q _ { i } ^ { o } = p _ { i } ^ { o } ( i = 1 , 2 ) , q _ { 3 } ^ { o } = p _ { 3 } ^ { o } - c .$ With an increase of firm 3's cost, all firms raise prices, Firms 1 and 2 are better off and Firm 3 is worse off.

In this equilibrium, Firms 1 and 2 have more market power with the increase of Firm 3's cost c: they increase their prices and get more demands; but Firm 3 has to increase its price to cover the cost and it incurs a lower margin and lower demand. Thus the increase of Firm 3's cost makes the other <sup>fi</sup>rms better off, while Firm 3 loses the competency and becomes worse off.

## 3.1.2. Case 2: co-opetition

When the collaboration is formed between Firm 1 and Firm 3 in Stage I, they cooperate only to the extent of the alliance contract and remain competitors in the market. That is, Firm 3 has Firm 1 take over the production/marketing activities at a cost (a <sup>fi</sup>xed price f and a per unit price r) to improve ef<sup>fi</sup>ciency, and in return Firm 1 receives the payment which is equivalent to getting Firm 3's demand indirectly. In the price competition stage, <sup>fi</sup>rms decide their own prices while taking the alliance contract (r, f) into account.

The <sup>fi</sup>rms compete on price by maximizing their respective pro<sup>fi</sup>t functions

$$
\begin{array}{l} \max _ {p _ {1}} \Pi_ {1} = p _ {1} q _ {1} (p _ {1}, p _ {2}, p _ {3}) + (r - c _ {1}) q _ {3} (p _ {1}, p _ {2}, p _ {3}) + f - c _ {k 1} \\ s. t. \qquad q _ {1} (p _ {1}, p _ {2}, p _ {3}) \geq 0 \\ \max _ {p _ {2}} \Pi_ {2} = p _ {2} q _ {2} (p _ {1}, p _ {2}, p _ {3}) \\ s. t. \qquad q _ {2} (p _ {1}, p _ {2}, p _ {3}) \geq 0 \end{array}\tag{3}
$$

ð<sup>4</sup>Þ

$$
\begin{array}{l} \max _ {p _ {3}} \Pi_ {3} = p _ {3} q _ {3} (p _ {1}, p _ {2}, p _ {3}) - r q _ {3} (p _ {1}, p _ {2}, p _ {3}) - f - c _ {k 3} \\ s. t. \qquad q _ {3} (p _ {1}, p _ {2}, p _ {3}) \geq 0 \end{array}\tag{5}
$$

Given Firm j's price, Firm i's pro<sup>fi</sup>t function is concave in its own price $( i \neq j , i , j = 1 , 2 , 3 )$ , therefore the equilibrium exists by satisfying the following simultaneous <sup>fi</sup>rst-order-conditions:

$$
\left\{ \begin{array}{c} p _ {1} \frac {\partial q _ {1}}{\partial p _ {1}} + q _ {1} + (r - c _ {1}) \frac {\partial q _ {3}}{\partial p _ {1}} = 0 \\ p _ {2} \frac {\partial q _ {2}}{\partial p _ {2}} + q _ {2} = 0 \\ p _ {3} \frac {\partial q _ {3}}{\partial p _ {3}} + q _ {3} - r \frac {\partial q _ {3}}{\partial p _ {3}} = 0 \end{array} \right.\tag{6}
$$

Table 1

List of variables used in the paper.

<table><tr><td>Variables</td><td>Meanings</td></tr><tr><td> $q_i$ </td><td>Demand of firm  $i (i=1,2,3)$ </td></tr><tr><td> $p_i$ </td><td>Price of firm  $i (i=1,2,3)$ </td></tr><tr><td> $\Pi_i$ </td><td>Profit of firm  $i (i=1,2,3)$ </td></tr><tr><td> $\pi_i^A$ </td><td>Firm  $i$ &#x27;s profit in the co-opetition before the fixed-fee payment  $f$  and contracting cost ( $i=1,3$ )</td></tr><tr><td> $a$ </td><td>The total market size in the demand function</td></tr><tr><td> $d$ </td><td>Degree of demand substitution in the demand function</td></tr><tr><td> $c$ </td><td>Firm 3&#x27;s marginal cost</td></tr><tr><td> $c_A$ </td><td>Firm 3&#x27;s marginal cost in period 2 if it forms a co-opetition in period 1</td></tr><tr><td> $c_N$ </td><td>Firm 3&#x27;s marginal cost in period 2 if it does not form a co-opetition in period 1</td></tr><tr><td> $c_1$ </td><td>Firm 1 incurs a cost of  $c_1$  for each unit of goods produced or sold for Firm 3</td></tr><tr><td> $c_{ki}$ </td><td>cost in forming and monitoring the alliance ( $i=1,3$ )</td></tr><tr><td> $r$ </td><td>Unit payment term in the co-opetition contract</td></tr><tr><td> $f$ </td><td>Fixed-fee term in the co-opetition payment contract</td></tr><tr><td> $R(q)$ </td><td>Co-opetition payment contract based on the quantity</td></tr><tr><td> $\lambda$ </td><td>Firm 1&#x27;s bargaining power.  $1-\lambda$  is Firm 2&#x27;s bargaining power.</td></tr><tr><td> $s$ </td><td>The surplus is of Firm 1 and Firm 3 under the co-opetition with that in the oligopoly equilibrium</td></tr><tr><td> $v$ </td><td>The total profits of Firm 1 and Firm 3</td></tr><tr><td> $c^f$ </td><td>Firm 3&#x27;s marginal cost that solves  $f(r^*,c)=0$ </td></tr><tr><td> $r_\lambda$ </td><td>The unit payment that solves  $f(r_\lambda)=0$ .</td></tr><tr><td> $cs$ </td><td>Consumer surplus</td></tr><tr><td> $w$ </td><td>Social welfare</td></tr><tr><td> $\delta$ </td><td>The discount factor</td></tr></table>

We observe two effects from the simultaneous Eq. (6):

Effect (1). In the co-opetition case, Firm 1 has to consider the effect of its price change on Firm 3's demand $\frac { \partial q _ { 3 } } { \partial p _ { 1 } } = d > 0$ in choosing its optimal price. Since Firm 1 receives the transfer payment based on Firm 3's demand, it has the incentive to price less aggressively. This is the cooperative effect of the co-opetition on market equilibrium. With this effect alone, Firm 1 has the tendency to raise its price from the oligopoly optimum to increase the demand of Firm 3; Firm 2's demand also increases due to the substitutability of its product with Firm 1's; As a consequence Firm 1's demand drops; Firm 2 and 3 increases their prices due to reduced market competition. This cooperative effect increases with the degree of demand substitution d between Firms 1 and 3 and the unit transfer payment r, and decreases with Firm 1's marginal cost c in servicing Firm 3.

Effect (2). In addition to the cooperative effect, co-opetition also has an ef<sup>fi</sup>ciency improving effect in that Firm 3 reduces its marginal cost to r which is lower than its true cost c by paying a <sup>fi</sup>xed fee f. This effect alone leads to a lower equilibrium price for Firm 3, higher demand for Firm 3, lower demands for the other two <sup>fi</sup>rms, and lower prices for the other two <sup>fi</sup>rms. A higher marginal cost $( c )$ of Firm 3 increases the ef<sup>fi</sup>ciency improving effect, while a higher cost of $\dot { \boldsymbol { c } } _ { 1 }$ reduces this effect.

The two effects have opposite impacts on most of the market outcomes but consistent impacts on Firm 1 and Firm 3's demands. Using superscript A to denote the co-opetitive equilibrium and $\pi _ { i } ^ { A }$ $( i = 1 , 3 )$ to represent Firm i's pro<sup>fi</sup>t before considering the <sup>fi</sup>xed-fee payment f and contracting cost $c _ { k i }$ in the alliance, we summarize the equilibrium in Proposition 1.

## Proposition 1. Bertrand Equilibrium of the co-opetition Game

There exists a unique co-opetition equilibrium in which firms charge prices $\begin{array} { r } { p _ { 1 } ^ { A } ( r ) = \frac { ( 2 + d ) a - ( 2 - d ) d \overline { { c } } _ { 1 } + ( 3 - d ) d \overline { { r } } } { 2 ( 2 - d - d ^ { 2 } ) } , p _ { 2 } ^ { A } ( r ) = \frac { ( 2 + d ) a - d ^ { 2 } c _ { 1 } + ( 1 + d ) d } { 2 ( 2 - d - d ^ { 2 } ) } } \end{array}$ and $\begin{array} { r } { p _ { 3 } ^ { A } ( r ) = \frac { ( 2 \mathrm { ~ + ~ } d ) a - d ^ { 2 } c _ { 1 } \mathrm { ~ + ~ } \left( 2 - d \mathrm { ~ + ~ } d ^ { 2 } \right) r } { 2 ( 2 - d - d ^ { 2 } ) } . } \end{array}$ Compared with the oligopoly competition equilibrium, in the co-opetition equilibrium all firms charge lower prices if and only if c is large; Firm 3 has higher demand, Firm 1 has lower demand under any alliance contract with $c _ { 1 } { \leq } r { \leq } c$ and Firm 2 has lower demand when Firm 3's cost is high $c - r { > } d ( r - c _ { 1 } )$ .

The cooperative effect increases <sup>fi</sup>rms' prices while the ef<sup>fi</sup>ciency improving effect decreases their prices. The relative strength of the two effects depends on the cost asymmetry of Firm 3 with the other two <sup>fi</sup>rms. When c is large, the ef<sup>fi</sup>ciency improving effect reduces the prices more than the cooperative effect increases the prices. Thus, the market is more competitive.

Both effects increase Firm 3's demand but decrease Firm 1's demand. The ef<sup>fi</sup>ciency improving effect reduces Firm 2's demand, while the cooperative effect increases its demand. The net effect depends on the relative marginal size of the two effects $( c - r )$ and $d ( r - c _ { 1 } )$

We next examine the impact of co-opetition on the <sup>fi</sup>rms equilibrium pro<sup>fi</sup>ts and summarize in Corollary 1.

Corollary 1. (i) When $c _ { 1 } \leq r \leq c$ and $f { \le } \pi _ { 3 } ^ { A } ( r ) - { \cal { I } } I _ { 3 } ^ { o } - c _ { k 3 } ,$ , co-opetition is always preferable to Firm 3. (ii) Firm 1 may lower its own demand from the alliance when Firm 3's cost is large but is compensated from the transfer payment. (iii) Firm 2 is worse off from the alliance if and only $i f c - r { > } d ( r - c _ { 1 } )$

Firm 3 increases ef<sup>fi</sup>ciency and competency from the alliance with Firm 1. Therefore, Firm 3 prefers the alliance as long as its gains can offset the <sup>fi</sup>xed payment f and the contracting cost $c _ { k 3 }$ (the individual rationality condition).

Due to the substitutability of the goods and the cooperative effect, the alliance, however, may hurt Firm 1's own business when the ef<sup>fi</sup>ciency gap between Firm 1 and Firm 3 is very large. In that case, Firm 1 will participate in the alliance only if the losses can be compensated by the transfer payment. When the goods are not highly substitutable (d is small), Firm 1 will receive a higher margin from serving Firm 3 than producing/selling its own goods.

Firm 2's pro<sup>fi</sup>t depends on the relative size of the two effects. When Firm 3's cost disadvantage is not very large, the cooperative effect outweighs the ef<sup>fi</sup>ciency improving effect. Hence, as an outsider, Firm 2 bene<sup>fi</sup>ts more from the alliance than in the oligopoly competition. However, with the increase of this cost difference, Firm 2 gets worse off due to the increased ef<sup>fi</sup>ciency improving effect. As a result, Firm 2 would prefer no alliance when it is much more ef<sup>fi</sup>cient than Firm 3.

## 3.2. Stage I — contract negotiation

In the <sup>fi</sup>rst stage, Firm 1 and Firm 3 negotiate the contract and decide whether to enter the alliance. To make the contract enforceable, either of the participating <sup>fi</sup>rms has to at least maintain its pro<sup>fi</sup>t from status quo. We model the negotiation process by the cooperative bargaining process — Nash Bargaining ([18], [25] and [27]) in which both partners split the surplus “pie” from the alliance. The surplus is de<sup>fi</sup>ned as the difference of the total pro<sup>fi</sup>t of Firm 1 and Firm 3 under the alliance with that in the oligopoly equilibrium

$$
S (r) = \left(\Pi_ {1} ^ {A} (r) + \Pi_ {3} ^ {A} (r)\right) - \left(\Pi_ {1} ^ {0} + \Pi_ {3} ^ {0}\right).\tag{7}
$$

The two partner <sup>fi</sup>rms bear the bene<sup>fi</sup>t and cost from the alliance together and divide them according to the sharing rule determined by their bargaining power. We use a parameter $\lambda \in [ 0 , 1 ]$ to represent the bargaining power of Firm 1, and 1 — λ to be the bargaining power of Firm $3 . { } ^ { 1 } \operatorname { L e t } \Lambda = 1$ when Firm 1 has the dominant power in negotiating the contract, and $\lambda = 0$ vice versa. By Theorem 4.1 in Nagarajan and Bassok [25], the pro<sup>fi</sup>ts of the two participating <sup>fi</sup>rms are

$$
\Pi_ {1} ^ {A} = \Pi_ {1} ^ {O} + \lambda \max _ {r} S (r)\tag{8}
$$

$$
\text { and } \Pi_ {3} ^ {A} = \Pi_ {3} ^ {O} + (1 - \lambda) \max _ {r} S (r).\tag{9}
$$

Eqs. (8) and (9) suggest that both <sup>fi</sup>rms have a consistent objective in choosing the unit transfer payment r, because the changes of their pro<sup>fi</sup>ts from the oligopoly market are both proportional to the surplus $S ( r )$ . Thus the optimal r, denoted as $r ^ { * } ,$ , is obtained by maximizing the “surplus $\mathsf { p i e } ^ { \prime \prime } S ( r )$ . The <sup>fi</sup>xed payment f can be expressed as a function of the bargaining power λ and the pro<sup>fi</sup>ts of the two <sup>fi</sup>rms.

## Proposition 2. Optimal Alliance Contract

If an alliance can be formed between Firm 1 and Firm 3, then there exists an optimal two-part tariff contract (r, f). The fixed fee $f { = } \lambda ( \pi _ { 3 } ^ { A } ( r ) - \bar { \cal I } _ { 3 } ^ { o } - c _ { k 3 } ) - ( 1 - \lambda ) ( \pi _ { 1 } ^ { A } ( \bar { r } ) - \bar { \cal I } _ { 1 } ^ { o } - c _ { k 1 } )$ depends on the bargaining power λ of the two partners. The unit payment r is independent of λ and is set to maximize the joint profit of the partner firms, that $i s , r ^ { * } = \ a r g \ m a x _ { r } S ( r ) = \ a r g \ m a x _ { r } \pi _ { 1 } ^ { A } ( r ) + \pi _ { 3 } ^ { A } ( r )$

Given our linear demand function as de<sup>fi</sup>ned in Eq. (1), the optimal contract has

$$
\begin{array}{l} r ^ {*} = \frac {a d (1 + d) (2 + d) + (2 - d) \Big (2 - 3 d + d ^ {2} - 2 d ^ {3} \Big) c _ {1}}{2 \big (2 - 4 d + 4 d ^ {2} - 5 d ^ {3} + d ^ {4} \big)} \text {and} \\ f (r ^ {*}) = \lambda \Big (\pi_ {3} ^ {A} (r ^ {*}) - \Pi_ {3} ^ {O} - c _ {k 3} \Big) - (1 - \lambda) \Big (\pi_ {1} ^ {A} (r ^ {*}) - \Pi_ {1} ^ {O} - c _ {k 1} \Big). \end{array}
$$

The optimal contract terms given by Proposition 2 are derived under the condition that a mutually agreeable contract is achieved and an alliance is formed. Now we explore the possibility of an alliance agreement between Firm 1 and Firm 3. Both partners in the alliance have to be at least not worse off after signing the alliance contract, which requires a nonnegative surplus $S ( r ^ { * } )$ . That is, the alliance decision is conditional on whether the surplus $S ( r ^ { * } )$ is nonnegative, which depends on whether the total gains of the two partners in sales can offset the total contracting costs. Let $V ^ { A } ( r ^ { * } ) { = } I I _ { 1 } ^ { A } ( r ^ { * } ) { + } I I _ { 3 } ^ { A } ( r ^ { * } )$ represent the total pro<sup>fi</sup>ts of the alliance partners and let $\begin{array} { r } { V ^ { O } ( c ) = \prod _ { 1 } ^ { O } ( c ) + \prod _ { 3 } ^ { O } ( c ) } \end{array}$ represent their total pro<sup>fi</sup>ts in the oligopoly market. We summarize the condition for a co-opetition alliance to be formed in Corollary 2.

Corollary 2. The sufficient and necessary condition for the alliance to be formed between Firm 1 and Firm 3 is that the surplus S(r\*) is nonnegative, that is, $V ^ { A } ( r ^ { * } ) \geq V ^ { O } ( c )$

Since $V ^ { A } = m _ { r } ^ { A } [ \Pi _ { 1 } ^ { A } ( r ) + \Pi _ { 3 } ^ { A } ( r ) ] { \geq } [ \Pi _ { 1 } ^ { A } ( r ) + \Pi _ { 3 } ^ { A } ( r ) ] \big | _ { r = c _ { 1 } } = V ^ { 0 } ( c _ { 1 } ) -$ $( c _ { k 1 } + c _ { k 3 } )$ , we obtain the suf<sup>fi</sup>cient condition for the alliance formation which focuses solely on the properties of the function $V ^ { o } ( c ) { : } V ^ { o } ( c _ { 1 } ) - V ^ { o }$ $( c ) { \geq } c _ { k 1 } + c _ { k 3 } .$ .This suf<sup>fi</sup>cient condition implies that $V ^ { o } ( c )$ is decreasing in c and that the increase in the ef<sup>fi</sup>ciency of Firm 3 should increase the joint pro<sup>fi</sup>t of Firm 1 and Firm 3 more than the total friction costs in alliance formation. Because

$$
\begin{array}{l} \frac {d V ^ {o} (c)}{d c} = p _ {1} ^ {o} \left(\frac {\partial q _ {1} ^ {o}}{\partial p _ {2}} \frac {\partial q _ {2} ^ {o}}{\partial c} + \frac {\partial q _ {1} ^ {o}}{\partial p _ {3}} \frac {\partial q _ {3} ^ {o}}{\partial c}\right) \\ \quad + \left(p _ {3} ^ {o} - c\right) \left(\frac {\partial q _ {3} ^ {o}}{\partial p _ {1}} \frac {\partial q _ {1} ^ {o}}{\partial c} + \frac {\partial q _ {3} ^ {o}}{\partial p _ {2}} \frac {\partial q _ {2} ^ {o}}{\partial c}\right) - q _ {3} ^ {o} \end{array}\tag{10}
$$

the suf<sup>fi</sup>cient condition may not be satis<sup>fi</sup>ed for any two <sup>fi</sup>rms with any general demand and cost levels of certain <sup>fi</sup>rms. This condition implies the following reasons that could possibly hinder an alliance between competitors:

1) There is not enough ef<sup>fi</sup>ciency difference between Firm 1and Firm 3, which limits the potential gains from the alliance.

2) There is a high substitution effect among the goods of the three <sup>fi</sup>rms, so that the alliance bene<sup>fi</sup>ts the outsider more than the partners.

3) Large friction costs of bargaining, contracting, and monitoring the alliance will eliminate some potential alliances.

The other reasons for two <sup>fi</sup>rms with complementary competencies failing to form an alliance are further discussed in Section 4 with a multi-period setting.

## 3.3. Nonnegative fixed fee payment contract

The case that the <sup>fi</sup>xed fee transfer payment f is negative is often ruled out in Katz and Shapiro [21] for the reason that Firm 1 “may bribe Firm 3 to exit the industry… and would likely to be illegal by antitrust authorities.” We next discuss the optimal contract in a two <sup>fi</sup>rm alliance when this constraint is added. The condition for an alliance to form (Corollary 2) and the optimal contract speci<sup>fi</sup>ed in Proposition 2 are modi<sup>fi</sup>ed for this constrained case and presented in Proposition 3.

Proposition 3. Optimal alliance contact with nonnegative <sup>fi</sup>xed payment

If a nonnegative fixed payment restriction is imposed,

(i) when $f ( r ^ { * } )$ is nonnegative $( \mathrm { i } . \mathbf { e } . , c \geq c ^ { f } ) ,$ , the sufficient and necessary condition for a co-opetition is as in Corollary 2 and the optimal bargaining contract is as in Proposition 2;

(ii) Otherwise, the sufficient and necessary conditions for a coopetition are $I I _ { 1 } ^ { A } ( r _ { \lambda } ) { \geq } I I _ { 1 } ^ { O }$ and $I I _ { 3 } ^ { A } ( r _ { \Lambda } ) \ge I I _ { 3 } ^ { O } ,$ , where the contract terms $f { = } 0$ and the unit payment $r _ { \lambda }$ is set by solving $f ( r _ { \lambda } ) = 0 .$

Proposition 3 posits the optimal contract structure given the restriction on the <sup>fi</sup>xed payment: $r = r ^ { * } \propto \mathrm { e r } r _ { \lambda }$ and $f { = } \operatorname* { m a x } \{ \lambda ( \pi _ { 3 } ^ { A } ( r _ { \lambda } ) { - } I I _ { 3 } ^ { o } { - } c _ { k 3 } ) { - }$ $( 1 - \lambda ) ( \pi _ { 1 } ^ { A } ( r _ { \lambda } ) - { \cal I } { \cal I } _ { 1 } ^ { O } - c _ { k 1 } ) , 0 \}$ . When $c { < } c ^ { f } ( c ^ { f }$ solves $f ( r ^ { * } , c ) = 0 ) , f$ is forced to be zero. When $f ( r ^ { * } ) { < } 0 , S ( r _ { \lambda } ) { \ge } 0$ is not a suf<sup>fi</sup>cient condition, but only a necessary condition for the co-opetition. When a negative <sup>fi</sup>xed transfer payment is prohibited and when $f ( r ^ { * } ) { < } 0 , \ \mathrm { i f } \ \mathrm { ~ a ~ }$ coopetition is formed, then a lower unit payment $r _ { \lambda }$ is reached under which $S ( r _ { \lambda } ) { < } S ( r ^ { * } )$

Given the suf<sup>fi</sup>cient conditions for the alliance to be formed $I I _ { 1 } ^ { A } ( r _ { \lambda } ) { \geq } I I _ { 1 } ^ { O }$ and $I I _ { 3 } ^ { A } ( r _ { \lambda } ) { \ge } { \Pi } _ { 3 } ^ { O }$ , we have $0 { \le } S ( r _ { \lambda } ) { < } S ( r ^ { \ast } )$ , which satis<sup>fi</sup>es the suf<sup>fi</sup>cient condition for a co-opetition to be formed. However, this inference cannot be reversed. Thus, the restriction of a nonnegative <sup>fi</sup>xed transfer payment reduces the chances of an alliance between some <sup>fi</sup>rms without a big ef<sup>fi</sup>ciency gap. Fewer co-opetitions will be formed under this restriction, which is further justi<sup>fi</sup>ed by the welfare analysis next.

## 3.4. Impacts of the co-opetition

This section analyzes the impacts of a co-opetition on <sup>fi</sup>rm pro<sup>fi</sup>ts, consumer surplus and social welfare.

The numerical example in Fig. 2 compares the pro<sup>fi</sup>ts of the <sup>fi</sup>rms under the oligopoly and co-opetition equilibria under the scenario of $a = 5 , d = 0 . 5 , c _ { 1 } = 0$ and $\lambda { = } 0 . 8$

## Proposition 4. Viability of the alliance

(i) Firm 1 and Firm 3 are no worse off in the co-opetition equilibrium than in the oligopoly equilibrium. The amount of profit increase depends on the firm's bargaining power.

(ii) It is better to be in the alliance if and only if the alliance partner Firm 1 can achieve higher profit than the non-alliance Firm 2, that is, $\Pi _ { 1 } ^ { A } { \geq } I I _ { 2 } ^ { A } .$ . The gap between the two profits increases with the cost of Firm 3 c, Firm 1's bargaining power λ and decreases with the friction costs in alliance formation $c _ { k } , a n d$ the substitution relationship between the goods of Firm 1 and Firm 3.

![](/api/attachments/PU8SB2V7/fulltext/images/eb067c29a0841ec2311f09046bb00bb9996919b45b1d89292cb5fa5aca693412.jpg)  
Fig. 2. Comparison of <sup>fi</sup>rm pro<sup>fi</sup>ts under the oligopoly and co-opetition equilibria given. $a = 5 , d = 0 . 5 , c _ { 1 } = 0 , \lambda = 0 . 8 .$

Corollary 2 suggests that both Firm 1 and Firm 3 will choose the coopetition strategy if their joint pro<sup>fi</sup>t in the alliance weakly dominates that in the oligopoly competition. Based on the Nash Bargaining equilibrium, each partner's pro<sup>fi</sup>t under the alliance is the sum of its pro<sup>fi</sup>t in the oligopoly equilibrium and a fraction (determined by bargaining power) of the total surplus after the cooperation. Hence, Proposition 4 suggests that both partners are no worse off under the optimal contract if an alliance is formed (as shown in Fig. 2).

Proposition 4 also proposes when an ef<sup>fi</sup>cient <sup>fi</sup>rm should participate in the alliance rather than being an outsider and “free-riding” the cooperation of the other <sup>fi</sup>rms. The numerical example in Fig. 2 supports it by showing that the outsider (Firm 2) gains more pro<sup>fi</sup>t from the alliance when c is small and being an insider (Firm 1) is a better choice for the ef<sup>fi</sup>cient <sup>fi</sup>rms when c is large. A larger cost asymmetry or smaller alliance costs increase the surplus of the alliance such that both partners bene<sup>fi</sup>t from the larger $" \mathrm { p i e } "$ . Keeping the surplus <sup>fi</sup>xed, the greater bargaining power of Firm 1 also helps it gain a larger share of the surplus. A higher substitution of the goods of Firm 1 and Firm 3 increases the impact of Firm 3's demand increase on Firm 1's demand. Therefore, Firm 1 is hurt more by this impact than Firm 2. If it is better to be an insider, being an outsider incurs opportunity cost. Therefore, a preemptive alliance should be a sensible strategy for a high-ef<sup>fi</sup>ciency <sup>fi</sup>rm if its bargaining power is not too small and the friction costs are not too large.

Consumer surplus is de<sup>fi</sup>ned as

$$
C S = U (q _ {1}, q _ {2}, q _ {3}) - \sum_ {i = 1} ^ {3} p _ {i} q _ {i}\tag{11}
$$

11 <sup>ð Þ</sup>where the partial derivative of the utility function equals the inverse demand function of those goods: ${ \frac { \partial { U ( q _ { 1 } , \bar { q } _ { 2 } , q _ { 3 } ) } } { \partial q _ { i } } } = p _ { i } ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) .$

Proposition 5. The Impact of Alliance on Consumer Welfare

Consumers are better off from the co-opetition when the costs of Firms 1 and 3 are not too close, or the goods are not highly substitutable.

Consumer surplus in the oligopoly market decreases as Firm 3's marginal cost c increases. While consumer surplus in the co-opetition market increases with Firm 1's alliance marginal cost $c _ { 1 }$ and decreases as the unit transfer payment r increases given the <sup>fi</sup>xed fee payment f. When a negative <sup>fi</sup>xed payment in the alliance contract is prohibited and the cost of Firm 3 is small, a lower unit transfer payment is reached in the alliance contract. Thus, this constraint bene<sup>fi</sup>ts consumers by increasing their surplus.

Social welfare is de<sup>fi</sup>ned as the total <sup>fi</sup>rm pro<sup>fi</sup>ts and consumer surplus:

$$
W = \sum_ {i = 1} ^ {3} \Pi_ {i} + C S.\tag{12}
$$

When the costs of <sup>fi</sup>rms are close, oligopolistic competition would drive down market prices and bene<sup>fi</sup>t the consumers. In contrast, an alliance prevents the <sup>fi</sup>erce competition by <sup>fi</sup>xing the high cost <sup>fi</sup>rm's cost at the optimal unit payment level for the partners. When the costs dispersion is high, both the partner <sup>fi</sup>rms and consumers will bene<sup>fi</sup>t from the co-opetition but it may hurt the other competitor's pro<sup>fi</sup>t. Therefore there is no general result when comparing the social welfare under the oligopoly and the co-opetition market equilibria. However, we can still examine the social impact of the policy of restricting negative <sup>fi</sup>xed fee payment in co-opetition alliances.

Corollary 3. It is socially optimal to prevent a negative fixed payment in the alliance contract when the costs of forming an alliance $c _ { k 1 }$ and $c _ { k 3 }$ are both close to zero.

If the <sup>fi</sup>xed payment f is allowed to be negative, losses in consumer surplus from the alliance cannot be compensated enough through the increase in <sup>fi</sup>rm pro<sup>fi</sup>ts, resulting in lower social welfare under the alliance. Therefore, the restriction on the <sup>fi</sup>xed payment may be necessary from the social welfare point of view.

## 4. A dynamic model

The co-opetition alliance allows a <sup>fi</sup>rm to improve ef<sup>fi</sup>ciency by contracting out one or some of the functional areas to its competitor. The analysis of the feasibility and impacts of this kind of alliance with a single-period game in Section 3 ignores the learning effect on future performance of the <sup>fi</sup>rm. Learning can only take place through the attempt to solve a problem and therefore only takes place during activities [4]. Alliances, however, hinder <sup>fi</sup>rms from learning and thus render the <sup>fi</sup>rm an opportunity loss in ef<sup>fi</sup>ciency improvement. To capture the learning effects, we extend the above one-shot coopetition problem into a multi-period decision problem in this section. We investigate whether the myopic decision derived above could sustain over time and examine the best timing for <sup>fi</sup>rms to enter an alliance.

Speci<sup>fi</sup>cally, we consider two periods and describe the pathdependent decision tree in Fig. 3. In each period, Firm 1 and Firm 3 may form an alliance based on a contract agreed upon by both parties, and the <sup>fi</sup>rms then compete in the market. In the <sup>fi</sup>rst period, each <sup>fi</sup>rm decides whether to start the alliance, taking into account its expected value of the alliance in the subsequent period. In the second period, if they have formed an alliance in the <sup>fi</sup>rst period (at node B in Fig. 3), the partner <sup>fi</sup>rms choose whether to continue/renew (node D) or to end the partnership (node E); otherwise (at node C) Firm 1 and Firm 3 choose whether to start an alliance (node F), or to continue operating independently (node G). The subgame equilibrium achieved at the second level of the decision tree (the subtrees under nodes B and C) has been solved in the single period game in Section 3. In the <sup>fi</sup>rst period, the partner <sup>fi</sup>rms will consider the expected pro<sup>fi</sup>ts in the second period when negotiating the contract terms f and r. Yet, the <sup>fi</sup>rst period prices are independent of the second period prices and contract terms.

Firms 1 and 2 are on the ef<sup>fi</sup>ciency frontier and their costs are normalized to zero for both periods. The cost for Firm 1 to produce or sell for Firm $3 c _ { 1 }$ also keeps constant over the two periods. However, the learning effect distinguishes Firm 3's cost in the second period as $c _ { A }$ or $c _ { N } ,$ depending on whether it partners with Firm 1 or not in the previous period. Prior works [2,3,24] report signi<sup>fi</sup>cant effects of learning on cost reduction. They also show that learning by doing and using has stronger and more signi<sup>fi</sup>cant effect on <sup>fi</sup>rm ef<sup>fi</sup>ciency improvement than learning by inter-industry spillovers from other competitors. Thus, considering the effects of learning from selfexperiences and learning from the spillovers from competitors, we have $c _ { N } { < } c _ { A } { < } c$ . Our major conclusions hold under the alternative assumption (discussed in Section 5).

![](/api/attachments/PU8SB2V7/fulltext/images/86dc690406343564c40897ca9d9ec069d0ce43d9ef861f187f8064f29d955a44.jpg)  
Fig. 3. The decision tree of the <sup>fi</sup>rms two-period alliance game.

We next examine the conditions of the two interesting equlibria among the four described in Fig. 3: a temporary co-opetition (ABE) and a delayed co-opetition (ACF).

## 4.1. The temporary co-opetition

Co-opetition is often used as a short-term strategy for <sup>fi</sup>rms to achieve certain goals and can be terminated when the status of the <sup>fi</sup>rms is changed. This case is described by the strategy ABE in Fig. 3. Doorley [12] studies 880 alliances and reports that 60% had a fouryear survival rate while less than 20% enjoyed a ten-year anniversary. Here we analyze the reasons for a <sup>fi</sup>rm to adopt the temporary coopetition strategy by seeking the conditions for it to be a subgame perfect strategy in the two-period game.

By backward induction, we <sup>fi</sup>rst examine the second period equilibrium taking the decision in the <sup>fi</sup>rst period as given. By Corollary 2, the condition for no-alliance (node E) being the subgame equilibrium given the <sup>fi</sup>rst period decision is alliance (node B) is that the surplus $S ( r ^ { * } ) { < } 0$ is negative, that is, $V ^ { A } ( r ^ { \ast } ) < V ^ { O } ( c _ { A } )$ . This may be caused by the learning of Firm 3 from its partner in the alliance that greatly improves its ef<sup>fi</sup>ciency. If the learning effect from experiencing is greater than that from observing, that is, $c _ { N } { < } c _ { A } ,$ , then when $V ^ { A } ( r ^ { * } ) { < } \bar { V } ^ { O } ( \bar { c } _ { A } )$ , noalliance (node G) is also a subgame equilibrium given the <sup>fi</sup>rst period decision is no alliance (node C) because $V ^ { O } ( c )$ is decreasing in c.

We now move back to the <sup>fi</sup>rst period to compare the total discounted pro<sup>fi</sup>ts of Firm 1 and Firm 3 under a short-term alliance (ABE) and no alliance (ACG). Assume the discount factor is $\delta \in ( 0 , 1 )$ The condition for the alliance to be formed in the <sup>fi</sup>rst period is:

$$
\text { Payoff } _ {A B E 1} = \pi_ {1} ^ {A} (r) + f - c _ {k 1} + \delta \Pi_ {1} ^ {O} (c _ {A}) \geq \text { Payoff } _ {A C G 1} = (1 + \delta) \Pi_ {1} ^ {O}\tag{13}
$$

$$
\text { Payoff } _ {A B E 3} = \pi_ {3} ^ {A} (r) - f - c _ {k 3} + \delta \Pi_ {3} ^ {O} (c _ {A}) \geq \text { Payoff } _ {A C G 3} = \Pi_ {3} ^ {O} (c) + \delta \Pi_ {3} ^ {O} (c _ {N}).\tag{14}
$$

In the alliance of the <sup>fi</sup>rst period, partners negotiate over the contract terms to optimize their total discounted payoffs considering the outside option (no alliance). This yields the optimal contract terms

$$
\begin{array}{c} f = \lambda \Bigl (\pi_ {3} ^ {A} (r) - \Pi_ {3} ^ {O} (c) - c _ {k 3} - \delta \Bigl (\Pi_ {3} ^ {O} (c _ {N}) - \Pi_ {3} ^ {O} (c _ {A}) \Bigr) \Bigr) \\ - (1 - \lambda) \Bigl (\pi_ {1} ^ {A} (r) - \Pi_ {1} ^ {O} - c _ {k 1} - \delta \Bigl (\Pi_ {3} ^ {O} (c _ {A}) - \Pi_ {3} ^ {O} (c _ {N}) \Bigr) \Bigr); \end{array}\tag{15}
$$

and the optimal unit payment term r is decided by maximizing the total discounted payoff $r = r ^ { * }$ given the <sup>fi</sup>xed fee payment term.

Thus we need both of the following conditions for the temporary equilibrium (ABE) to exist:

$$
V ^ {A} (r ^ {*}) \geq V ^ {O} (c) + \delta \left(V ^ {O} \left(c _ {N}\right) - V ^ {O} \left(c _ {A}\right)\right)\tag{C1}
$$

$$
\text { and } V ^ {A} (r ^ {*}) <   V ^ {O} (c _ {A})\tag{C2}
$$

Condition (C1) requires the partner <sup>fi</sup>rms to take into account the impact of their <sup>fi</sup>rst-period decision on their future pro<sup>fi</sup>tability. Since the learning-by-doing effect is stronger than the spillover effect $- c _ { N } { < } C _ { A } ,$ the alliance decision in the two-period model has stricter requirements than in a single-period model: the total gain in the alliance not only has to satisfy the single period suf<sup>fi</sup>cient and necessary condition, but also has to offset the loss due to missing the opportunity of learning by doing. Condition (C2) ensures the second period equilibrium. The above conditions can be satis<sup>fi</sup>ed when Firm 3 is a weak competitor at the beginning $c > > c _ { 1 } .$ , but it increases its ef<sup>fi</sup>ciency signi<sup>fi</sup>cantly through the alliance with Firm $1 - c _ { A } { < } { < } c _ { 1 }$ . In this scenario, an alliance does not sustain because the learning narrows the ef<sup>fi</sup>ciency gap between the two partner <sup>fi</sup>rms.

While strategic alliances have been proven to be a strategy for growth and competitiveness, they may not sustain in the long run. The above analysis demonstrated that the spillover effect and the learning effect in the alliance can be a reason for the alliance to dissolve over time. Rather than remaining inef<sup>fi</sup>cient, a <sup>fi</sup>rm is able to become more ef<sup>fi</sup>cient through learning from its partner. This new knowledge and experience can motivate the <sup>fi</sup>rm to withdraw from the alliance and take over the previously outsourced activities.

## 4.2. Timing of the co-opetition

Co-opetition also involves risks and trade-offs. An alliance may reduce the less ef<sup>fi</sup>cient <sup>fi</sup>rm's learning and internalization, hence reducing the negotiating position of the <sup>fi</sup>rm in the future. When a <sup>fi</sup>rm decides whether to seek a partner to facilitate its business, it needs to trade off the bene<sup>fi</sup>t of enhanced competence via the alliance with the opportunity cost of not gaining <sup>fi</sup>rst-hand experience with the activity. Therefore, Firm 3 may be better off to delay the alliance and handle the activities on its own in the <sup>fi</sup>rst period, so that it becomes more competitive in the second period due to the learning by doing effect. We investigate this strategy by analyzing the equilibrium of ACF in Fig. 3.

When $V ^ { A } ( r ^ { * } ) \geq V ^ { O } ( c _ { N } )$ and by the assumption that $V ^ { o } ( c )$ is decreasing in c and $c _ { N } { < } c _ { A } ,$ the alliance is the dominant strategy in the second period, that is, the second period equilibria under node B and C are D and F, respectively. Therefore, we can reduce the equilibrium paths by only comparing the total discounted payoffs of strategies ABD and ACF:

$$
\begin{array}{l} \text {Payoff} _ {A B D 1} = \pi_ {1} ^ {A} (r ^ {*}) + f - c _ {k 1} + \delta \Big (\Pi_ {1} ^ {O} (c _ {A}) + \lambda \Big (V ^ {A} (r _ {A} ^ {*}) - V ^ {O} (c _ {A}) \Big) \Big) \\ \text {Payoff} _ {A C F 1} = \Pi_ {1} ^ {O} (c) + \delta \Big (\Pi_ {1} ^ {O} (c _ {N}) + \lambda \Big (V ^ {A} (r _ {N} ^ {*}) - V ^ {O} (c _ {N}) \Big) \Big) \\ \text {Payoff} _ {A B D 3} = \pi_ {3} ^ {A} (r ^ {*}) - f - c _ {k 3} + \delta \Big (\Pi_ {3} ^ {O} (c _ {A}) + (1 - \lambda) \Big (V ^ {A} (r _ {A} ^ {*}) - V ^ {O} (c _ {A}) \Big) \Big). \\ \text {Payoff} _ {A C F 3} = \Pi_ {3} ^ {O} (c) + \delta \Big (\Pi_ {3} ^ {O} (c _ {N}) + (1 - \lambda) \Big (V ^ {A} (r _ {N} ^ {*}) - V ^ {O} (c _ {N}) \Big) \Big) \end{array}
$$

Without any restriction on the <sup>fi</sup>xed fee payment f, the sum of the payoffs of Firm 1 and Firm 3 under ABD always dominates that under ACF with the assumption of $c _ { N } { < } C _ { A } { < } C .$ . Therefore the equilibrium of a delayed alliance ACF cannot occur without a restriction on the <sup>fi</sup>xed fee. If the restriction of $f { \geq } 0$ is imposed on the contract form, when

$$
\delta \Bigl (\lambda \Bigl (\Pi_ {3} ^ {0} (c _ {N}) - \Pi_ {3} ^ {0} (c _ {A}) \Bigr) + (1 - \lambda) \Bigl (\Pi_ {1} ^ {0} (c _ {A}) - \Pi_ {1} ^ {0} (c _ {N}) \Bigr) \Bigr) \geq \pi_ {3} ^ {A} (r ^ {*}) - \Pi_ {3} ^ {0} (c) - c _ {k 3},
$$

a feasible alliance contract does not exist in period 1. That is, when Firm 3 can get a higher level ef<sup>fi</sup>ciency through learning by doing rather than through partnering with another <sup>fi</sup>rm $. - c _ { N } { < } { < } c _ { 1 }$ , it is optimal for Firm 3 not to get into an alliance with Firm 1 in the <sup>fi</sup>rst period.

In this case, when learning-by-doing has a much greater effect on <sup>fi</sup>rm performance than learning from the partner and the restriction on the contract terms is applied, Firm 3's delaying the alliance gives it a better position in bargaining the alliance contract and therefore a higher pro<sup>fi</sup>t than starting the partnership in period 1. From a different perspective, while the restriction of a nonnegative <sup>fi</sup>xed fee can increase social welfare in the single period model as discussed in

Section 3.3, it may also prohibit a potential socially optimal alliance in the <sup>fi</sup>rst period.

## 5. Discussion

In this paper we investigate the cooperation of competitors via a horizontal supply chain. Through investigating different <sup>fi</sup>rms' interests in the two stages of co-opetition, we can gain a better understanding of <sup>fi</sup>rms' preferences and decisions related to the alliance. We show that each <sup>fi</sup>rm's strategic preference toward the alliance depends on certain factors such as cost differences among <sup>fi</sup>rms, bargaining power, substitutability of goods, contract fees, friction cost of alliance, and learning effects. In this section we summarize in simpler terms the key aspects of the co-opetition process, decisions, and implications from our research.

As a baseline for examining the impacts of co-opetition, we <sup>fi</sup>rst consider the behavior of three <sup>fi</sup>rms competing independently in an oligopoly competition. In this case a unique Bertrand-Nash equilibrium exists, with all <sup>fi</sup>rms charging a price greater than their marginal cost. If one <sup>fi</sup>rm's cost increases, this <sup>fi</sup>rm would tend to raise price to cover the higher cost, thereby lowering its demand. This action allows the other <sup>fi</sup>rms to gain demand and also gives them an opportunity to raise their prices and increase pro<sup>fi</sup>ts.

The high-cost <sup>fi</sup>rm has motivation to form an alliance with one of its competitors to take advantage of their cost ef<sup>fi</sup>ciencies (a coopetition). Let Firm 1 represent a low cost competitor, Firm 3 the high-cost competitor, and Firm 2 a competitor that is not part of the alliance and that represents all other competitors outside the alliance.

Stage I of the co-opetition process consists of Firms 1 and 3 negotiating an agreement where Firm 1 receives a <sup>fi</sup>xed payment plus a per unit payment to manufacture goods or provide services for Firm 3. The two <sup>fi</sup>rms negotiate how to divide the surplus pro<sup>fi</sup>ts resulting from Firm 3's output being produced at a lower cost by Firm 1. We model this negotiation as a Nash Bargaining process and posit that the <sup>fi</sup>xed payment depends on the bargaining power of each <sup>fi</sup>rm and the per unit payment is independent of bargaining power and is set to maximize joint pro<sup>fi</sup>t of the two <sup>fi</sup>rms. This insight allows the <sup>fi</sup>rms to better focus most of their negotiating efforts on the <sup>fi</sup>xed payment rather than the per unit payment.

We posit that a suf<sup>fi</sup>cient and necessary condition for the alliance to be formed is that the surplus is nonnegative. Several reasons could result in a negative surplus, such as not enough ef<sup>fi</sup>ciency difference between the two <sup>fi</sup>rms, large friction costs to create and maintain the alliance, and high substitution effect among the goods of the three <sup>fi</sup>rms so that the alliance bene<sup>fi</sup>ts the outside <sup>fi</sup>rm more than the partner <sup>fi</sup>rms.

Firms 1 and 3 are no worse off in the co-opetition equilibrium than in the oligopoly equilibrium. Firm 2 (the outside <sup>fi</sup>rm) gains more than Firm 1 when the cost difference between Firms 1 and 3 is small and when the friction cost of the alliance is large. This insight motivates the outside <sup>fi</sup>rm to encourage an alliance between other <sup>fi</sup>rms in certain circumstances.

The greater the cost difference between the alliance <sup>fi</sup>rms and the less substitutable their goods are, the greater is the consumer surplus. Also, net impacts of the alliance on social welfare are dif<sup>fi</sup>cult to predict. However, it is socially optimal to prevent a negative <sup>fi</sup>xed payment when the friction costs of forming an alliance are negligible.

As co-opetition alliances evolve over time, learning can improve the ef<sup>fi</sup>ciency of Firm 3. In fact, Firm 3 can improve its ef<sup>fi</sup>ciency over time in two ways through learning, if a multi-period dynamic model is considered. On one hand, if Firm 3 does not form an alliance then it learns through <sup>fi</sup>rst-hand experience in producing the good itself, becoming more ef<sup>fi</sup>cient at the task (learning effect). On the other hand, through an alliance Firm 3 can learn by observing how Firm 1 produces the good more ef<sup>fi</sup>ciently. Firm 3 can use this new knowledge to reduce its own production costs if it later decides to discontinue the alliance and produce the good itself, thereby becoming more ef<sup>fi</sup>cient at the task (spillover effect). In general, a <sup>fi</sup>rm can improve its ef<sup>fi</sup>ciency more through <sup>fi</sup>rst-hand experience than through observations of other <sup>fi</sup>rms doing the work, although this depends on the technical and creative nature of the work.

In a two-period model, after forming an alliance in Period 1, Firm 3 must decide whether to continue the alliance or discontinue it and use the new knowledge it learned from working with Firm 1 to produce on its own (temporary co-opetition strategy). A temporary coopetition strategy might be best when Firm 3 lacks knowledge about a critical production process step. This critical knowledge may be gained from Firm 1 in Period 1 as a spillover effect, allowing Firm 3 to produce ef<sup>fi</sup>ciently on its own in Period 2.

An alternative strategy is for Firm 3 to produce on its own in Period 1, in the process reducing its costs through the <sup>fi</sup>rst-hand-experience learning effect, and then being in a stronger position with lower cost as it negotiates an alliance with Firm 1 in Period 2 (delayed coopetition strategy). A delayed co-opetition strategy might be best when Firm 3 plans to stay in the alliance for the long term but wants to initially negotiate the most favorable <sup>fi</sup>nancial arrangement it can. Having lower costs when negotiating would likely result in more preferable terms for Firm 3.

From the perspective of Firm 1, an alliance can increase its pro<sup>fi</sup>ts due to Firm 3's payments. The downside to Firm 1 is that Firm 3 becomes more competitive as its ef<sup>fi</sup>ciency increases through learning. Increased competition might lower Firm 1's pro<sup>fi</sup>ts in the long term. Another factor that Firm 1 must consider is how much competitive advantage it derives from its proprietary approaches to doing the work, and how much of its competitive advantage would be lost if the proprietary approaches are shared with Firm 3.

The above results are obtained under the assumption that learning-bydoing effect is stronger than learning from spillover effect. The opposite assumption, that is, $c _ { A } < c _ { N } ,$ does not change our major conclusions. In the temporal co-opetition equilibrium (path ABE) in Section 4.1, the condition for the subgame perfect equilibrium (path BE) $V ^ { A } ( r ^ { \ast } ) < V ^ { O } ( c _ { A } )$ leads to two possibilities: $V ^ { \bar { A } } ( r ^ { * } ) { < } V ^ { O } ( c _ { N } ) { < } V ^ { O } ( c _ { A } )$ or $V ^ { O } ( C _ { N } ) { < } V ^ { A } ( r ^ { * } ) { < } V ^ { O } ( C _ { A } )$ . The previous results also apply to the <sup>fi</sup>rst case. Under the second scenario, it is obvious that the payoffs of Firms 1 and 3 under the path of alliance at period 1 only (ABE) is greater than that under the path of alliance at period 2 only (ACF). Therefore we do not need further restrictions for ABE to be the equilibrium other than $V ^ { A } ( r ^ { \ast } ) < V ^ { O } ( c _ { A } )$ , which is condition C2. In the delayed co-opetition equilibrium (path ACF) in Section 4.2, the assumption of a dominant learning-by-observing effect contradicts with the condition for the subgame perfect equilibrium (path CF) without the restriction on a nonnegative <sup>fi</sup>xed fee payment. The same result applies.

We do not consider the holdup problems in contracting with capacity investment. For example, Dixit [11] has shown that <sup>fi</sup>rms use capacity investments strategically in order to deter entry of potential competitors into their turf. Since Firm 1 (e.g. Amazon.com) will often need to expand its capacity (servers, support staff, etc.) in order to service a partnership with a large competitor, a termination of this partnership can result in excess capacity for Firm 1. Therefore investment in those assets gives Firm 1 more incentive to stay in the co-opetition relationship and may reduce Firm 1's bargaining power in contract negotiation.

## 6. Conclusions

Competitive relationships have been traditionally thought of as the ways in which prices, for example, emerge out of the competitive struggle between businesses [1]. This paper, however, proposes that even in very competitive industries, co-opetition can still exist as a certain kind of inter<sup>fi</sup>rm relationship. We exposit economic reasons behind co-opetition through a game theoretic model.

A <sup>fi</sup>rm can contract out some of its weak business functions to a competing <sup>fi</sup>rm to gain ef<sup>fi</sup>ciency instead of doing everything alone.

The ef<sup>fi</sup>cient partner can increase product lines or services without any effort in marketing to generate the demand. We derive the suf<sup>fi</sup>cient and necessary conditions for the co-opetition to be built. We <sup>fi</sup>nd that alliances of this kind can make both partner <sup>fi</sup>rms better off even without equity sharing and ignoring economy of scale and demand externality. These <sup>fi</sup>ndings suggest that outsourcing weak activities to a competitor to create a horizontal supply chain partnership may be a desirable option under certain conditions.

Firms should consider the double effects co-opetition has on the <sup>fi</sup>rms in the market: ef<sup>fi</sup>ciency effect and cooperative effect. They both bene<sup>fi</sup>t the low ef<sup>fi</sup>ciency <sup>fi</sup>rm through enhancing its competence and the cooperation from the partner. The alliance increases the weak <sup>fi</sup>rm's performance to the detriment of its competitors by lowering their competitive advantage. The ef<sup>fi</sup>cient partner gets compensated for its activities in the cooperation, yet the outsider could be worse off depending on the relative strength of the two effects and the reaction of the partner <sup>fi</sup>rms.

We examine whether a co-opetition will sustain over time and a delayed alliance with a two-period dynamic model. It turns out with the learning of the weaker <sup>fi</sup>rm, the partnership formed in the <sup>fi</sup>rst period may not be renewed in the second period.

Our results have important implications for public policy makers. The co-opetition increases consumer welfare and social welfare when the ef<sup>fi</sup>ciency effect outweighs the cooperative effect. The <sup>fi</sup>xed fee payment in the two-part tariff contract is usually constrained to be nonnegative by antitrust laws. We derive the optimal contract under this restriction and <sup>fi</sup>nd that by doing this, social welfare can be enhanced in a single period when the costs associated with the alliance formation are negligible. This conclusion, however, does not necessarily hold in the two period model, in which the second period pro<sup>fi</sup>t is taken into account when the <sup>fi</sup>rms negotiate the contract terms.

Opportunities for future related research abound. One avenue for extension of this research is to investigate the life expectancy of a coopetition alliance as a function of the expected learning rate by the less ef<sup>fi</sup>cient <sup>fi</sup>rm. Another future research path is to examine the impact of the alliance on Firm 1's production capacity management and the risks involved with expanding its capacity to accommodate Firm 3's goods. Yet another future research direction is to analyze how the life expectancy of the goods or services impacts the optimal strategies in forming an alliance.

## Appendix A

Proof of Lemma 1. Firms compete with each other on price to maximize their own pro<sup>fi</sup>ts.

$$
\begin{array}{l} \max _ {p _ {i}} \Pi_ {i} = p _ {i} q _ {i} (p _ {1}, p _ {2}, p _ {3}) \\ s. t. \qquad q _ {i} (p _ {1}, p _ {2}, p _ {3}) \geq 0 \qquad (i = 1, 2) \end{array}\tag{A1}
$$

$$
\begin{array}{l} \max _ {p _ {3}} \Pi_ {3} = (p _ {3} - c) q _ {3} (p _ {1}, p _ {2}, p _ {3}) \\ s. t. \qquad \qquad \qquad q _ {3} (p _ {1}, p _ {2}, p _ {3}) \geq 0 \end{array}\tag{A2}
$$

Note that given Firm j's price, Firm i's pro<sup>fi</sup>t function is concave in its own price. When the cost difference is not large, there exists an equilibrium that consists of interior solutions to the optimization problems. The equilibrium exists by simultaneously satisfying the following response functions

$$
\left\{ \begin{array}{c} B R _ {1} (p _ {2}, p _ {3}) = \frac {a + d (p _ {2} + p _ {3})}{2} \\ B R _ {2} (p _ {1}, p _ {3}) = \frac {a + d (p _ {1} + p _ {3})}{2} \\ B R _ {3} (p _ {1}, p _ {2}) = \frac {a + c + d (p _ {1} + p _ {2})}{2} \end{array} \right.\tag{A3}
$$

The <sup>fi</sup>rms' reaction functions slope upwards. That is, Firm i's optimal price is an increasing function of Firm j's price. By solving the best response functions simultaneously, we obtain the equilibrium prices (Bertrand-Nash) in the oligopoly competition.

When the cost difference is not large, i.e. $c \leq \frac { ( 2 + d ) a } { 2 - d - 2 d ^ { 2 } } ,$ all <sup>fi</sup>rms are active. The equilibrium is

$$
\begin{array}{l} p _ {i} ^ {0} = q _ {i} ^ {0} = \frac {a (2 + d) + d c}{2 (2 - d - d ^ {2})} (i = 1, 2); \\ p _ {3} ^ {0} = \frac {a (2 + d) + (2 - d) c}{2 (2 - d - d ^ {2})}; \\ q _ {3} ^ {0} = p _ {3} ^ {0} - c; \\ \Pi_ {i} ^ {0} = \left(q _ {i} ^ {0}\right) ^ {2} (i = 1, 2, 3). \\ \frac {\partial p _ {i} ^ {0}}{\partial c} = \frac {d}{2 (2 - d - d ^ {2})} > 0 (i = 1, 2); \\ \frac {\partial p _ {3} ^ {0}}{\partial c} = \frac {(2 - d)}{2 (2 - d - d ^ {2})} > 0; \\ \frac {\partial \Pi_ {i} ^ {0}}{\partial c} = \frac {(a (2 + d) + d c) d}{2 (2 - d - d ^ {2}) ^ {2}} > 0 (i = 1, 2); \\ \frac {\partial \Pi_ {3} ^ {0}}{\partial c} = - \frac {(a (2 + d) - (2 - d - 2 d ^ {2}) c) (2 - d - 2 d ^ {2})}{2 (2 - d - d ^ {2}) ^ {2}} <   0; \end{array}
$$

Proof of Proposition 1. Solving the simultaneous best response equations in (6) yields the optimal prices given the unit payment in the contract

$$
\begin{array}{l} p _ {1} ^ {A} (r) = \frac {(2 + d) a - (2 - d) d c _ {1} + (3 - d) d r}{2 (2 - d - d ^ {2})}, \\ p _ {2} ^ {A} (r) = \frac {(2 + d) a - d ^ {2} c _ {1} + (1 + d) d r}{2 (2 - d - d ^ {2})} \text { and } \\ p _ {3} ^ {A} (r) = \frac {(2 + d) a - d ^ {2} c _ {1} + (2 - d + d ^ {2}) r}{2 (2 - d - d ^ {2})}. \end{array}
$$

Because $\begin{array} { r } { p _ { 1 } ^ { A } \ – p _ { 1 } ^ { O } = \frac { d ( ( 3 - d ) r - c - ( 2 - d ) c _ { 1 } ) } { 2 ( 2 - d - d ^ { 2 } ) } , p _ { 2 } ^ { A } \ – p _ { 2 } ^ { O } = \frac { d ( ( 1 + d ) r - c - d c _ { 1 } ) } { 2 ( 2 - d - d ^ { 2 } ) } } \end{array}$ and $\begin{array} { r } { p _ { 3 } ^ { A } - p _ { 3 } ^ { o } = \frac { \left( 2 - d + d ^ { 2 } \right) r - ( 2 - d ) c - d ^ { 2 } c _ { 1 } } { 2 ( 2 - d - d ^ { 2 } ) } , p _ { i } ^ { A } - p _ { i } ^ { o } } \end{array}$ for any <sup>fi</sup>rm i if c is greater than $\{ ( 3 - d ) r - ( 2 - d ) c _ { 1 } , ( 1 + d ) r - d c _ { 1 } , ( 2 - d + d ^ { 2 } ) r - d ^ { 2 } c _ { 1 } \}$

Plugging the above equilibrium prices into the demand functions (1), we get the equilibrium quantities.

$$
\begin{array}{l} q _ {1} ^ {A} (r) = \frac {(2 + d) a + (2 - d - 2 d ^ {2}) d c _ {1} - (1 - d - 2 d ^ {2}) d r}{2 (2 - d - d ^ {2})}; \\ q _ {2} ^ {A} (r) = \frac {(2 + d) a - d ^ {2} c _ {1} + (1 + d) d r}{2 (2 - d - d ^ {2})}; \\ q _ {3} ^ {A} (r) = \frac {(2 + d) a - d ^ {2} c _ {1} - (2 - d - 3 d ^ {2}) d r}{2 (2 - d - d ^ {2})}. \end{array}
$$

Comparing the demand of the three <sup>fi</sup>rms in the oligopoly market and in the alliance, $\begin{array} { r } { q _ { 1 } ^ { A } - q _ { 1 } ^ { o } = - \frac { \left( 2 - d - 2 d ^ { 2 } \right) d ( r - c _ { 1 } ) + d ( c - r ) } { 2 ( 2 - d - d ^ { 2 } ) } < 0 , } \end{array}$ and $q _ { 3 } ^ { A } - q _ { 3 } ^ { O } =$ $\frac { \left( 2 - d - 2 d ^ { 2 } \right) ( c - d r ) + d ^ { 2 } ( d r - c _ { 1 } ) } { 2 ( 2 - d - d ^ { 2 } ) } > 0$ given $c _ { 1 } \leq r \leq c$ . When $c - r { > } d ( r - c _ { 1 } )$ q<sup>A</sup><sub>2</sub>−q<sup>O</sup><sub>2</sub> = d<sub>ð</sub> <sub>Þ</sub> <sub>ð</sub> <sub>Þ</sub> 1 + d r−c−dc<sub>1</sub> □ 2 2−d−d<sup>2</sup>

Proof to Corollary 1.

(i) $\Pi _ { 3 } ^ { A } - \Pi _ { 3 } ^ { O } = \pi _ { 3 } ^ { A } ( r ) - f - c _ { k 3 } - \Pi _ { 3 } ^ { O } .$ . When $f { \le } \pi _ { 3 } ^ { A } ( r ) - { \cal { I } } I _ { 3 } ^ { o } - c _ { k 3 } ,$ $\Pi _ { 3 } ^ { A } { \geq } { \cal I } { \cal I } _ { 3 } ^ { O } .$

(ii) $\Pi _ { 1 } ^ { A } - \Pi _ { 1 } ^ { O } = \pi _ { 1 } ^ { A } ( r ) + f - c _ { k 1 } - \Pi _ { 1 } ^ { O } ( c ) \leq \pi _ { 1 } ^ { A } ( r ) + \pi _ { 3 } ^ { A } ( r ) - ( \Pi _ { 1 } ^ { O } ( c ) +$ $\Pi _ { 3 } ^ { O } ( c ) ) - c _ { k 1 } - c _ { k 3 } .$ . Since $\partial ( { \cal I } _ { 1 } ^ { o } ( c ) + { \cal I } _ { 3 } ^ { o } ( c ) ) / \partial c > 0 ,$ , there exists a $c _ { 0 }$ such that $\pi _ { 1 } ^ { A } ( r ) + \pi _ { 3 } ^ { A } ( r ) - ( \Pi _ { 1 } ^ { 0 } ( c _ { 0 } ) + \Pi _ { 3 } ^ { 0 } ( c _ { 0 } ) ) - c _ { k 1 } - c _ { k 3 } =$ 0. Therefore, when 0 $c { > } c _ { 0 } , I I _ { 1 } ^ { A } { < } I I _ { 1 } ^ { O } .$

(iii) Π<sup>A</sup> $- \Pi _ { 2 } ^ { 0 } = \left( q _ { 2 } ^ { A } \right) ^ { 2 } - \left( q _ { 2 } ^ { O } \right) ^ { 2 } = \left( q _ { 2 } ^ { A } + q _ { 2 } ^ { O } \right) . \frac { d ( ( 1 + d ) r - c - d c _ { 1 } ) } { 2 ( 2 - d - d ^ { 2 } ) } ,$ . When $c - r { > } d ( r - c _ { 1 } ) , I I _ { 2 } ^ { A } { < } I I _ { 2 } ^ { O } .$

Proof of Proposition 2. Based on the Nash Bargaining result, Firm 1 receives from the <sup>fi</sup>xed fee payment f its share in Firm 3's pro<sup>fi</sup>t increase before the <sup>fi</sup>xed fee payment $\overset { \cdot } { \lambda } ( \pi _ { 3 } ^ { A } ( \overset { \cdot } { r } ) - I I _ { 3 } ^ { O } - c _ { k 3 } )$ , withholding Firm 3's share of Firm 1's pro<sup>fi</sup>t gain before the <sup>fi</sup>xed fee paymen $\cdot ( 1 - \lambda ) ( \pi _ { 1 } ^ { A } ( r ) -$ $I I _ { 1 } ^ { O } { - } c _ { k 1 } )$ . Thus the <sup>fi</sup>xed fee can be expressed as

$$
f = \lambda \left(\pi_ {3} ^ {A} (r) - \Pi_ {3} ^ {O} - c _ {k 3}\right) - (1 - \lambda) \left(\pi_ {1} ^ {A} (r) - \Pi_ {1} ^ {O} - c _ {k 1}\right).\tag{A4}
$$

The optimal r is obtained by maximizing the “surplus $\mathsf { p i e } ^ { \prime \prime }$ :

$$
\begin{array}{l l} r ^ {*} = & \arg \underset {r} {\max} S (r) \\ = & \arg \underset {r} {\max} \Pi_ {1} ^ {A} (r) + \Pi_ {3} ^ {A} (r) - \Big (\Pi_ {1} ^ {O} + \Pi_ {3} ^ {O} \Big) \\ = & \arg \underset {r} {\max} \pi_ {1} ^ {A} (r) + \pi_ {3} ^ {A} (r) - c _ {k 1} - c _ {k 3} - \Big (\Pi_ {1} ^ {O} + \Pi_ {3} ^ {O} \Big). \\ = & \arg \underset {r} {\max} \pi_ {1} ^ {A} (r) + \pi_ {3} ^ {A} (r) \end{array}
$$

which is independent of λ and is consistent to both <sup>fi</sup>rms' objectives.

Proof of Corollary 2. The suf<sup>fi</sup>cient and necessary conditions for a coopetition to exist are $\Pi _ { 1 } ^ { A } { \geq } \Pi _ { 1 } ^ { O }$ and $\Pi _ { 3 } ^ { A } { \geq } { I I _ { 3 } ^ { O } } .$ . Proposition 2 suggests that these conditions are equivalent to $S ( r ^ { * } ) { \ge } 0 .$ . Given the de<sup>fi</sup>nition of S(r) in Eq. $( 7 ) , V ^ { A } ( r ^ { * } ) = { \cal I } { } _ { 1 } ^ { \bar { A } } ( r ^ { * } ) + { \cal I } { } _ { 3 } ^ { A } ( r ^ { * } )$ and $\begin{array} { r } { V ^ { O } ( c ) = \prod _ { 1 } ^ { O } ( c ) + \prod _ { 3 } ^ { O } ( c ) } \end{array}$ $S ( r ^ { * } ) { \ge } 0$ is equivalent to $V ^ { A } ( r ^ { * } ) { \geq } V ^ { O } ( c )$ □

Proof of Proposition 3. If the demand functions and the cost levels of the <sup>fi</sup>rms satisfy the suf<sup>fi</sup>cient condition in Corollary 1, then given the bargaining power λ exogenous,

$$
\frac {\partial f}{\partial c} = (1 - \lambda) \frac {\partial \Pi_ {1} ^ {0} (c)}{\partial c} - \lambda \frac {\partial \Pi_ {3} ^ {0} (c)}{\partial c} = \frac {\partial \Pi_ {1} ^ {0} (c)}{\partial c} - \lambda \frac {\partial V ^ {0}}{\partial c} > 0.\tag{A5}
$$

Therefore, when the suf<sup>fi</sup>cient condition in Corollary 1 is satis<sup>fi</sup>ed and we impose the nonnegative restriction on f, f can be de<sup>fi</sup>ned as inProposition 2 only when c is larger than a value c<sup>f</sup> which solves $\lambda ( \pi _ { 3 } ^ { A } ( r ^ { * } ) - { \cal T } { } _ { 3 } ^ { O } - c _ { k 3 } \dot { ) } - ( 1 - \lambda ) ( \pi _ { 1 } ^ { A } ( r ^ { * } ) - { \cal T } { } _ { 1 } ^ { O } - c _ { k 1 } ) = 0 .$ . When $c { < } c ^ { f } , f \mathrm { i }$ is forced to be zero, the optimal solution to the bargaining game has to be on the boundary. When Firm 1 has all the bargaining power $( \lambda = 1 ) , f { < } 0$ implies $\pi _ { 3 } ^ { A } ( r ^ { * } ) - c _ { k 3 } { < } { \cal { I } } { \cal { I } } _ { 3 } ^ { O }$ , that is, Firm 3 would be worse off if it agrees on the alliance contract with $r = r ^ { * }$ . In this case, $r _ { \lambda = 1 }$ is set to solve $\pi _ { 3 } ^ { A } ( r _ { \lambda = 1 } ) - c _ { k 3 } = { \cal { I I } } _ { 3 } ^ { O }$ . Firm 1 would take away all the surplus from the alliance and keep Firm 3 at the same pro<sup>fi</sup>t level as before the alliance. Similarly, when Firm 3 has all the bargaining power $( \lambda = 0 ) , \ r _ { \lambda = 0 }$ is set to solve $\pi _ { 1 } ^ { A } ( r _ { \lambda = 0 } ) - c _ { k 1 } = { \cal { I I } } _ { 1 } ^ { O } .$ When $0 < \lambda < 1$ and $f | _ { r = r ^ { * } } { < } 0$ , then the contract is signed only when $S ( r _ { \lambda } ) { \ge } 0$ with $r _ { \lambda }$ solves $\lambda ( \pi _ { 3 } ^ { A } ( r _ { \lambda } ) - { \cal T } { } _ { 3 } ^ { 0 } - c _ { k 3 } ) - ( 1 - \bar { \lambda ( } ) ( \pi _ { 1 } ^ { A } ( r _ { \lambda } ) - { \cal T } { } _ { 1 } ^ { 0 } - c _ { k 1 } ) = 0 .$ Because $\frac { \partial r _ { \lambda } } { \partial \lambda } = \frac { S ( r _ { \lambda } ) } { ( 1 - \lambda ) \frac { \partial \pi _ { 1 } ^ { A } } { \partial r } - \lambda \frac { \partial \pi _ { 3 } ^ { A } } { \partial r } } > 0$ , by Intermediate Value Theorem,

$r _ { \lambda }$ lies in between $r _ { \lambda = 0 }$ and $r _ { \lambda = 1 } .$

Proof of Proposition 4.

(i) By Eqs. (8) and (9) $\Pi _ { 1 } ^ { A } = \operatorname* { m a x } _ { r } \Pi _ { 1 } ^ { O } + \lambda S ( r )$ and $\Pi _ { 3 } ^ { A } = \operatorname* { m a x } _ { r } \Pi _ { 3 } ^ { O } +$ $( 1 - \lambda ) S ( r )$ and the suf<sup>fi</sup>cient and necessary condition in Corollary $2 \ S ( r ) { > } 0 ,$ , we have $I I _ { 1 } ^ { A } { \geq } I I _ { 1 } ^ { O }$ and $I I _ { 3 } ^ { A } { \geq } I I _ { 3 } ^ { O }$ when the co-opetition alliance is formed. The pro<sup>fi</sup>t increases are proportional to their own bargaining power λ and $1 - \lambda$

(ii) By the suf<sup>fi</sup>cient condition in Corollary $1 , { \frac { d ( \Pi _ { 1 } ^ { A } - \Pi _ { 2 } ^ { A } ) } { d c } } = { \frac { d f } { d c } } =$ $( 1 - \lambda ) \frac { d \Pi _ { 1 } ^ { o } } { d c } - \lambda \frac { d \Pi _ { 3 } ^ { o } } { d c } > 0 .$ . Therefore, a larger c would increase the total surplus and consequently the <sup>fi</sup>xed fee payment Firm 1 receives.

$$
\frac {d \left(\Pi_ {1} ^ {A} - \Pi_ {2} ^ {A}\right)}{d c _ {k i}} = - \lambda <   0 (i = 1, 3).
$$

By the suf<sup>fi</sup>cient and necessary condition in Corollary $2 , \frac { d ( \Pi _ { 1 } ^ { A } - \Pi _ { 2 } ^ { A } ) } { d \lambda } =$ $S > 0 .$

By the suf<sup>fi</sup>cient condition in Corollary $1 , ~ \frac { \partial \Pi _ { 1 } ^ { A } / \partial \Pi _ { 2 } ^ { A } } { \partial q _ { 3 } / \partial p _ { 1 } } =$ $\frac { \partial \Pi _ { 1 } ^ { A } / \partial q _ { 3 } } { \partial \Pi _ { 2 } ^ { A } / \partial p _ { 1 } } < 0$ . So a smaller substitution relationship between goods

Proof of Proposition 5. According to Vives [34], the linear demand functions in (1) can be derived from the consumers' utility function

$$
U (q _ {1}, q _ {2}, q _ {3}) = \alpha \sum_ {i = 1} ^ {3} q _ {i} - \beta \sum_ {i = 1} ^ {3} (q _ {i}) ^ {2} - \gamma \sum_ {i \neq j} q _ {i} q _ {j},\tag{A6}
$$

$$
\text {   Where   } \alpha = \frac {a}{1 - 2 d}, \beta = \frac {1 - d}{2 (1 + d) (1 - 2 d)} \text {   and   } \gamma = \frac {d}{(1 + d) (1 - 2 d)}.
$$

Consumer surplus in both kinds of market structures can be calculated by plugging this utility function into Eq. (11):

$$
\begin{array}{l} C S ^ {A} = \alpha \sum_ {i = 1} ^ {3} q _ {i} ^ {A} - \beta \sum_ {i = 1} ^ {3} \left(q _ {i} ^ {A}\right) ^ {2} - \gamma \sum_ {i \neq j} q _ {i} ^ {A} q _ {j} ^ {A} - \sum_ {i = 1} ^ {3} p _ {i} ^ {A} q _ {i} ^ {A} \\ = \frac {3 a ^ {2} (2 + d) ^ {2}}{8 (1 - 2 d) (2 - d - d ^ {2}) ^ {2}} + \frac {(1 - 2 d)}{8 (1 - 2 d) (2 - d - d ^ {2}) ^ {2}} \\ \times \left[ c _ {1} d ^ {2} (4 - 4 d - 5 d ^ {2} + 2 d ^ {3}) - 2 c _ {1} d ^ {2} r ^ {*} (4 - 5 d - 7 d ^ {2} + 2 d ^ {3}) \right. \\ \left. - 2 a (2 + d) ^ {2} ((1 + d) r ^ {*} - d c _ {1}) \right. \\ \left. + r ^ {* 2} (1 + d) (4 - 8 d + 7 d ^ {2} - 1 1 d ^ {3} + 2 d ^ {4}) \right] \end{array}
$$

$$
\begin{array}{l} C S ^ {O} = \alpha \sum_ {i = 1} ^ {3} q _ {i} ^ {O} - \beta \sum_ {i = 1} ^ {3} \left(q _ {i} ^ {O}\right) ^ {2} - \gamma \sum_ {i \neq j} q _ {i} ^ {O} q _ {j} ^ {O} - \sum_ {i = 1} ^ {3} p _ {i} ^ {O} q _ {i} ^ {O} \\ \quad = \frac {3 a ^ {2} (2 + d) ^ {2}}{8 (1 - 2 d) (2 - d - d ^ {2}) ^ {2}} \\ \quad + \frac {(1 - 2 d)}{8 (1 - 2 d) (2 - d - d ^ {2}) ^ {2}} \Big [ c ^ {2} \big (4 - 4 d - 5 d ^ {2} + 2 d ^ {3} \big) - 2 a c (2 + d) ^ {2} \Big ] \end{array}
$$

We take the derivative of consumer surplus in the oligopoly market with the marginal cost of Firm 3

$$
\frac {d \left(C S ^ {A} - C S ^ {O}\right)}{d c} = \sum_ {i = 1} ^ {3} \frac {\partial p _ {i} ^ {O}}{\partial c} q _ {i} ^ {O} > 0
$$

given $\frac { \partial p _ { i } ^ { 0 } } { \partial c } > 0 ( i = 1 , 2 , 3 )$ by Proposition 2.

The alliance increases consumer surplus more than in the oligopoly equilibrium only if Firm 3's cost c is greater than a value $c ^ { \prime } ,$ which is increasing with d. When the substitutability of the goods is high, that is, d is very large, c’ is also very large, resulting in lower consumer surplus in the alliance case. □

Proof of Corollary 3. Eq. (12) de<sup>fi</sup>nes the social welfare as $W = \sum _ { i = 1 } ^ { ^ { \cal { S } } } \Pi _ { i } + C S \cdot$

With the restriction on the <sup>fi</sup>xed fee payment, no feasible alliance will be formed when c is small enough to make $f ( r ^ { * } ) { < } 0$ , hence social welfare may not be distorted by alliances between <sup>fi</sup>rms.

This restriction may also prevent potential alliances that bene<sup>fi</sup>t both Firm 1 and Firm 3 but their gains cannot offset the losses of Firm 2 and consumer surplus. However, we <sup>fi</sup>nd that when $c _ { k 1 }$ and $c _ { k 3 }$ are both close to zero, this will not happen. By Proposition $^ { 3 , }$ the smallest cost c we can have to sustain a feasible alliance and the corresponding unit payment r in the contract are found by solving the simultaneous equations

$$
\left\{ \begin{array}{l} \pi_ {1} ^ {A} (r) - c _ {k 1} = \pi_ {1} ^ {O} (c) \\ \pi_ {3} ^ {A} (r) - c _ {k 3} = \pi_ {3} ^ {O} (c) \end{array} \right.\tag{A7}
$$

If $c _ { k 1 } = c _ { k 3 } = 0 ,$ the solution is $c = r = c _ { 1 } < r ^ { * } ,$ , under which we have $f ( r ^ { * } , c ) { < } 0$ . So under the restriction $\operatorname { o f } f \geq 0 ,$ The contract terms are $f { = } 0 ,$ and $r = c .$ The market condition under this scenario is the same as that without a partnership. Hence, the social welfare under this con<sup>fi</sup>guration $\boldsymbol { W } ^ { A } ( \boldsymbol { r } , \boldsymbol { f } )$ is the same as $W ^ { o } ( c )$ , and is larger than the social welfare under the partnership without the restriction on $f - W ^ { A } ( r ^ { * } , f ( r ^ { * } , c ) )$ When $c _ { 1 } \mathrm { i } s$ small enough and given $W ^ { 0 }$ decreases with c, the difference between $W ^ { A }$ and $W ^ { 0 }$ increases with c. Therefore, $W ^ { A } { \geq } W ^ { O } { \mathrm { f o r } } c \geq c _ { 1 } .$ □

## References

[1] P.W. Andrews, Industrial economics as a specialist subject, Journal of Industrial Economics I (1) (1952) 72–79.

[2] L. Argote, S.L. Beckman, D. Epple, The persistence and transfer of learning in industrial settings, Management Science 36 (2) (1990) 140–154.

[3] L. Argote, B. McEvily, R. Reagans, Managing knowledge in organizations: an integrative framework and review of emerging themes, Management Science 49 (4) (2003) 571–582.

[4] K. Arrow, The economic implications of learning by doing, Review of Economics Studies 29 (1962) 155–174.

[5] A. Brandenburger, B. Nalebuff, Co-opetition: a revolution mindset that combines competition and cooperation, Harvard Business Press, Cambridge, MA, 1996.

[6] G.P. Cachon, Supply chain coordination with contracts, in: A.G. Kok, S.C. Graves (Eds.), Supply Chain Management: Design, Coordination and Operation, Elsevier Amsterdam, 2003, pp. 229–340.

[7] G.P. Cachon, M. Lariviere, Supply chain coordination with revenue sharing: strength and limitations, Management Science 51 (1) (2005) 30–44.

[8] H.K. Chan, F.T.S. Chan, Comparative study of adaptability and <sup>fl</sup>exibility in distributed manufacturing supply chains, Decision Support Systems 48 (2) (2010) 331–341.

[9] S.H. Chan, J.W. Kensinger, A.J. Keown, J.D. Martin, Do strategic alliances create value? Journal of Financial Economics 46 (2) (1997) 199–221.

[10] J.M. Cruz, The impact of corporate social responsibility in supply chain management: multicriteria decision-making approach, Decision Support Systems 48 (1) (2009) 224–236.

[11] A. Dixit, The role of investment in entry-deterrence, The Economic Journal 90 (357) (1980) 95–106.

[12] T.L. Doorley III, Teaming up for success, Business Quarterly 57 (1993) 99–103.

[13] T.C.-T. Du, H.-M. Lee, A. Chen, Constructing federated databases in coordinated supply chains, Decision Support Systems 36 (1) (2003) 49–64.

[14] N.T. Gallini, R.A. Winter, Licensing in the theory of innovation, The Rand Journal of Economics 16 (2)(1985) 237-252

[15] Y. Gerchak, Y. Wang, Revenue-sharing vs. wholesale price contracts in assembly systems with random demand, Production and Operations Management 13 (1) (2004) 23–33.

[16] D. Granot, G. Sosic, Formation of alliances in internet-based supply exchanges, Management Science 51 (1) (2005) 92–105.

[17] D. Granot, S. Yin, Competition and cooperation in decentralized push and pull assembly systems, Management Science 54 (4) (2008) 733–747.

[18] H. Gurnani, M. Shi, A bargaining model for a <sup>fi</sup>rst-time interaction under asymmetric beliefs of supply reliability, Management Science 52 (6) (2006) 865–880.

[19] H. Gurnania, M. Erkocb, Y. Luo, Impact of product pricing and timing of investment decisions on supply chain co-opetition, European Journal of Operational Research 180 (1) (2007) 228–248.

[20] B. Holmstrom, J. Roberts, The boundaries of the <sup>fi</sup>rm revisited, The Journal of Economic Perspectives 12 (4) (1998) 73–94.

[21] M. Katz, C. Shapiro, On the licensing of innovations, The Rand Journal of Economics 16 (1985) 504–520.

[22] P. Kouvelis, C. Chambers, H. Wang, Supply chain management research and pom: review, trends, and opportunities, Production and Operations Management 15 (3) (2006) 449–469.

[23] N.V. Long, A. Soubeyran, Cost manipulation games in oligopoly, with costs of manipulating, International Economic Review 42 (2) (2001) 505–533.

[24] F. Malerba, Learning by <sup>fi</sup>rms and incremental technical change, Economic Journal 102 (1992) 845–859.

[25] M. Nagarajan, Y. Bassok, A bargaining framework in supply chains: the assembl problem, Management Science 54 (8) (2008) 1482–1496.

[26] M. Nagarajan, G. Sosic, Stable farsighted coalitions in competitive markets, Management Science 53 (1) (2007) 29–45.

[27] J.F. Nash, The bargaining game, Econometrica 18 (2) (1950) 155–162.

[28] T.H. Oum, J.-H. Park, A. Zhang, Globalization and strategic alliances: the case of the airline industry, Elsevier Science, Amsterdam, the Netherlands, 2000.

[29] B. Paternack, Optimal pricing and returns policies for perishable commodities, Marketing Science 4 (2) (1985) 166–176.

[30] M.E. Porter, The competitive advantage of nations, Harvard Business Review 68 (2) (1990).

[31] M.E. Porter, Don't collaborate, compete, The Economist, June 9 1990.

[32] D. Sen, Y. Tauman, General licensing schemes for a cost-reducing innovation? Games and Economic Behavior 59 (1) (2007) 163–186.

[33] A. Tsay, Quantity–<sup>fl</sup>exibility contract and supplier–customer incentives, Management Science 45 (10) (1999) 1339–1358.

[34] X. Vives, Oligopoly pricing — old ideas and new tools, MIT Press, Cambridge, 1999.

[35] O. Williamson, Transaction-cost economics: the governance of contractual relations, Journal of Law and Economics 22 (1979) 233–271

[36] H. Zhang, Vertical information exchange in a supply chain with duopoly retailers, Production and Operations Management 11 (4) (2002) 531–546.

![](/api/attachments/PU8SB2V7/fulltext/images/17bdbe5c7fd73f1ef2ddd81dd4f5137dbceaee105b739ceca6e820f1fb0581fc.jpg)  
Jie (Jennifer) Zhang is an Assistant Professor of Information Systems in the College of Business Administration at the University of Texas at Arlington. She received her Ph.D. in Computer Information Systems from William E. Simon Graduate School of Business in the University of Rochester. She employs analytical and empirical techniques to examine a number of issues in electronic retail channels, online reputation and feedback systems, software pricing and licensing models, online search behaviors, and website designs. Her research appears in Journal of Management Information Systems, Journal of Economics and Management Strategies, Decision Support Systems, Communications of the ACM, Information Resources Management Journal, and ation Systems

Journal of Computer Information Systems.  
![](/api/attachments/PU8SB2V7/fulltext/images/c6bc45eefc004f8ad87c43cdf75cf5e58ea4125d2554ae0d70414639634ee9ba.jpg)

Gregory V. Frazier is professor of operations management at The University of Texas at Arlington. He received a Ph.D in production and operations management, an MBA, and a BS in mechanical engineering from Texas A&M University, and is a Certi<sup>fi</sup>ed Fellow in Production and Inventory Management (CFPIM). He has published in Journal of Operations Management, European Journal of Operational Research, International Journal of Production Research, IIE Transactions, International Journal of Operations and Production Management, International Journal of Production Economics, Journal of Productivity Analysis, Supply Chain Management: An International Journal, Quality Management Journal, Production and Inventory Management Journal,

Industrial Management & Data Systems, and Business Horizons, among others. He is also coauthor of the textbook Operations Management, 9th edition, with Norman Gaither.
