---
otero_id: 15178
otero_key: "FG3UPVF4"
title: "Reservation price reporting mechanisms for online negotiations"
authors: "Seungwoo Kwon; Byungjoon Yoo; Jinbae Kim; Wei Shang; Gunwoong Lee"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Reservation price reporting mechanisms for online negotiations

Seungwoo Kwon <sup>a,1</sup>, Byungjoon Yoo <sup>b,</sup>⁎, Jinbae Kim <sup>a,2</sup>, Wei Shang <sup>c,3</sup>, Gunwoong Lee <sup>d,4</sup>

<sup>a</sup> Korea University Business School, Anam-dong, Seongbuk-gu, Seoul 136-701, South Korea <sup>b</sup> Graduate School of Business, Seoul National University, 599 Gwanangro, Shinlim9-dong, Gwanakgu, Seoul 151-916, South Korea <sup>c</sup> Institute of Systems Science, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Room429, SiYuan Building. No.55, East Zhongguancun Rd. Haidian Dist. Beijing, 100190, China

<sup>d</sup> Krannert School of Management, Purdue University, West Lafayette, IN 47907-2056, USA

## a r t i c l e i n f o

Available online 20 November 2008

Keywords: Online negotiation Reservation price

## a b s t r a c t

To facilitate online negotiations, this paper proposes a reservation price reporting mechanism (RPR) and its extended version (ERPR), in which negotiators are invited to report their reservation price to a third-party system before initiating negotiations. Analyses using analytical models show that sellers and buyers report their true reservation prices under certain conditions with respect to the back-dragging costs. Analytical models also show that total social welfare can be increased by two reservation price reporting mechanisms. Then lab experiments are conducted to compare the performance of RPR, ERPR and the traditional direct bargaining (TDB). Consistent with the analytical models, results of the lab experiments show that RPR and ERPR reduce the number of negotiation rounds before reaching an agreement and increase negotiators' social welfare. These lab results testify to the ef<sup>fi</sup>ciency of RPR and ERPR over TDB.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Modern information technologies facilitate convenient information exchange with less temporal and geographical restrictions and provide decision support functions with higher expected pro<sup>fi</sup>ts. Online negotiations may enable negotiators to achieve better payoffs by facilitating information exchange, even though the information provided is somewhat noisy [1]. Online negotiations can be conducted directly between participants by means of information technology such as emails or virtual meetings. However, one of the most promising ways is third-party mediated online negotiation. A third party may neutrally serve as a mediator or host of an e-marketplace. Buyers and sellers get together at a third-party website to negotiate with each other. Practitioners perceive that internet-based online negotiation can be useful, but still have low con<sup>fi</sup>dence in pure online negotiation especially when risks are involved [7].

Online negotiation can be classi<sup>fi</sup>ed according to the number of parties involved in: bilateral negotiations and multilateral auctions [10]. Mechanisms for e-auctions are widely discussed. Most e-auction mechanisms are designed on the basis of existing auction mechanisms, such as English Auction or Vickery Auction. Trust and shillbidding are among the main issues to be resolved in terms of mechanism design [14]. However, there is little research on mechanism design for bilateral electronic negotiations.

Another way to use information technology for negotiation is the Negotiation Support System (NSS). NSS has been evolved from the Decision Support System (DSS). NSS is a man-machine interaction system that assists negotiators in analyzing and solving negotiation problems by helping them structure their preferences and view data regarding negotiations [15]. NSS, as a result, leads negotiators to make better decisions and maximize pro<sup>fi</sup>ts (e.g., Negotiator [2], Negoisst [12]). Existing NSSs mostly try to imitate the traditional face-to-face (F2F) negotiations or decision support throughout the process of online negotiation [5]. The suggested bene<sup>fi</sup>ts of using NSS mainly include helping negotiators construct their interests and offering them some kind of post-transaction settlement [3] or the automation of a negotiation process without human agents by using intelligent agents [4]. Although issues such as preference elicitation and con<sup>fl</sup>ict resolution have been studied extensively, very few studies employ mechanisms beyond the frame of traditional F2F negotiation. Specially designed negotiation mechanisms are indispensable for more effective online negotiations.

This paper focuses on designing a negotiation support mechanism to support bilateral business negotiations between agents. Two new mechanisms, reservation price reporting mechanism (RPR) and extended reservation price reporting mechanism (ERPR), are proposed. We examine analytical models under the proposed mechanisms from an economic perspective. Then, we assess the proposed mechanisms in the laboratory from a psychological perspective.

## 2. Economic models for bilateral negotiation

Economic models on negotiations originated to explain people's behavior and predict the outcome of game theory [13]. People's behaviors in negotiations are usually modeled as players' strategies, which are indicated by sequences of bidding prices. A negotiator's payoffs are generally calculated by the differences of the deal price and their costs or reservation prices. Expected outcome of a negotiation is predicted by the equilibrium of a particular game. Sophisticated economic models of bilateral negotiations have been developed. For the circumstance that two parties bid in turn and both suffer a certain amount each round, both parties' bidding strategies and <sup>fi</sup>nal solutions can be predicted by Rubinstein's model [11]. Based on this model, there are further studies on one-sided incomplete information settings [8] and two-sided information settings [6].

Most economic negotiation models consider only one issue of price, since price can always be generalized as a utility function in a multi-issue negotiation problem according to utility theory. This simpli<sup>fi</sup>cation is necessary when we focus mainly on the bidding strategy and <sup>fi</sup>nal outcomes. Contextual factors which in<sup>fl</sup>uence the process of negotiation are usually studied in behavioral negotiation studies [9] and are beyond our economic approach. Therefore, without losing any generality, the price bargaining between a buyer and seller is taken as the context of the bilateral negotiation model in this study.

Since negotiators engage in negotiations for their own interest, how much they can get from the negotiation is the most important factor in<sup>fl</sup>uencing their behavior. As a result, a negotiator's gain is usually referred to as his payoff. For the simplest case of price bargaining from an economic perspective, the seller's payoff can be calculated by the <sup>fi</sup>nal deal price minus his/her cost and the buyer's payoff can be measured by his/her budget price minus the <sup>fi</sup>nal deal price.

To ensure minimum payoffs, the negotiator always has a baseline or resistance point, which means he or she will not continue a deal if it is under this baseline. For example, a seller has a minimum price to accept in mind. This minimum price is the seller's baseline. The buyer's baseline is the highest price he or she is willing to pay for the object being negotiated. This baseline is referred to as the buyer's willingness-to-pay (or seller's reservation price). When the buyer's willingness-to-pay is lower than the seller's reservation price, then there is almost no chance of a deal. This kind of situation is referred to as a negative bargaining zone. In each round of negotiation, costs such as time, money and labor are involved in the bidding. If a negotiator rejects an offering but continues to drag the partner(s) into another round of negotiations, bidding costs as well as opportunity loss will be incurred by both sides. Bidding cost and opportunity loss are referred to as back-dragging cost.

## 3. Mechanism design for online negotiations

## 3.1. Reservation price reporting mechanism

In the RPR mechanism, negotiators are asked to report their reservation prices (from sellers) or willingness-to-pay (from buyers) to a third-party before they start negotiations. Speci<sup>fi</sup>cally, a buyer is asked to report the highest price that she can accept and a seller is asked to report the lowest price that she can accept. When a buyer's willingness-to-pay is higher than a seller's reservation price (i.e., the negotiation is in a negative bargaining zone), there is no possibility that an agreement can be reached. Therefore, from a theoretical perspective, revelation of the reservation price can allow negotiators to avoid wasting time and energy in a negotiation with a negative bargaining zone. In practice, however, revelation of the reservation price and willingness-to-pay could be risky, since the other party will attain more negotiation power by capturing private information.

In the RPR mechanism, negotiators report reservation price or willingness-to-pay to the electronic third-party. The electronic thirdparty is regarded as more neutral and more reliable by negotiation participants than the physical third-party. Therefore, negotiators can avoid useless negotiations in the negative bargaining zone using the RPR mechanism. It should be noted that ‘reservation price’ in this study does not have the same meaning as ‘reservation price’ in an auction where the reservation price is known to bidders. In reality, the seller's reservation price or the buyer's willingness-to-pay is rarely announced in negotiations. If the reservation price or willingness-topay is known to the opposite party, then the party who released the information would be placed at a disadvantage in the negotiations.

The RPR mechanism is conducted in three steps: 1) Potential sellers and buyers report their reservation prices or willingness-topay to the mediation system. 2) The system checks whether a positive bargaining zone exists between pairs of buyers and sellers. If so, then a negotiation session is initiated. Otherwise, the process terminates. 3) If a negotiation session begins, the buyer and the seller bid in turn until a proposal is accepted by both sides or one side quits. In our study, we focused on price negotiations, which may be generalized to multi-criteria cases when the utility of different issues can be calculated in one dimension.

To illustrate how the RPR mechanism works, an example of trading used cars is presented as follows. Suppose that used cars are traded on a website and the website requires all participants to submit their reservation prices or willingness-to-pay to the system. A used car seller <sup>fi</sup>rst advertises the car on the website. The seller submits a reservation price, say \$1200, and other product information to the system. The reservation price of the seller is not revealed to potential buyers. Potential buyers can visit the website and freely review the product information. If a buyer is interested in the used car, he is required to report his willingness-to-pay to the system. The buyer's willingness-to-pay is not revealed to the seller. Suppose the buyer submits a willingness-to pay of \$1100. Then the buyer's willingnessto-pay is lower than the seller's reservation price of \$1200, which means there is no possibility of agreement. The system noti<sup>fi</sup>es this fact to both participants and the negotiations do not start.

Now suppose that the buyer submits a willingness-to-pay of \$1500. Then the maximum price the buyer is willing to pay is higher than the seller's reservation price, which means that there is a positive bargaining possibility. The system lets the two parties start negotiations. The seller makes the <sup>fi</sup>rst bid at \$1550. The buyer cannot accept this price, but is aware that the lowest possible selling price is lower than his willingness-to-pay. Therefore, the buyer refuses the <sup>fi</sup>rst proposal and makes a counterbid of \$1250. While this bid is within the seller's acceptable price range, the seller wants a higher pro<sup>fi</sup>t. Hoping that the buyer will accept a higher price, the seller proposes \$1350. The buyer accepts the proposed price because the price is within the acceptable range and does not want to continue bargaining. However, even when the seller's reservation price is lower than the buyer's willingness-to-pay, it is possible that a deal can not be made. For example, after a number of rounds of bids, the buyer or seller may decide that continuing the negotiation is not worthwhile and terminate the negotiation without reaching a deal.

## 3.2. Extended RPR mechanism

Offering more information may lead to higher ef<sup>fi</sup>ciency. For example, Priceline.com, an online site, sometimes provides bidders extra information, such as a message, “Your bid is too far from acceptable.” With this message, the bidder has an option of increasing the bid price. This extra piece of information makes the whole negotiation process quicker without revealing too much private information, such as reservation price or willingness-to-pay.

Bidders tend to bid far from the baseline, especially at the early stages of negotiation, to ensure more room to negotiate. This strategy, however, is not ef<sup>fi</sup>cient because if there is a larger bargaining zone, it will take more time for the negotiators to reach an agreement. Thus, both sides will incur greater costs in terms of bidding and time. Therefore, we designed a guiding mechanism during negotiations, which is similar to the message in Priceline.com. Before a bid is submitted, the user has a chance to alter it with the system's advice. For example, if the bidder decides to bid \$1000, he receives the system's advice to bid higher, because \$1000 is much lower than the seller's reservation price. That is, the system informs the bidder that the price \$1000 is too low and a higher price may have a greater chance to be accepted. Given this information, the bidder may increase the bid to get a quicker deal or the bidder may not change the bid if he is not eager to make a deal right away.

The guiding mechanism should be carefully designed, otherwise the bidder may <sup>fi</sup>nd out the seller's reservation price by analyzing the pattern of the system's advice. Therefore, the following considerations should be taken into account when editing the guiding mechanisms: First, the advice must be given only once each time. Second, the criteria should be designed based on some random coef<sup>fi</sup>cients. More details on this will be presented in Section 5.

## 4. Analytical models

## 4.1. Basic model for the RPR mechanism

## 4.1.1. Assumptions

In order to assess the proposed RPR mechanism, we examine a simpli<sup>fi</sup>ed basic model in this section. Some basic assumptions on the negotiation process under the RPR mechanism are as follows:

A1. Two agents, a buyer and a seller, are involved in price bargaining. A positive bargaining zone exists, where the deal price must be decided within the zone.

A2. Each agent tries to maximize his or her own utility. Payoffs can be calculated by the difference between agreed price and reservation price.

A3. The seller's own reservation price, the minimum price to sell, or the buyer's willingness-to-pay, the maximum price to pay, is exogenous and held privately, but since the probability distribution of all agents' reservation prices and willingnessto-pay are uniformly distributed between $\mathrm { P _ { m i n } }$ and $\mathrm { \sf P } _ { \mathrm { m a x } }$ , the knowledge about the distribution of reservation prices and willingness-to-pay is considered as common knowledge.

A4. Agents bid in turn. Each agent's bidding price sequence is monotonic.

A5. Time is precious. Failure to make a deal at a certain round will cost both agents a <sup>fi</sup>xed amount.

A6. Each agent is risk averse.

## 4.1.2. Payoff structure

Without losing generality, we examine the seller's payoff structure. Suppose $\mathrm { P } _ { \cal S } ( \mathrm { t } )$ is the price proposed by the seller at time t. Seller's utility of $\mathrm { P } _ { \cal S } ( \mathrm { t } )$ is represented by function $\mathrm { U } _ { \mathrm { S } } ( \mathrm { P } _ { \mathrm { S } } ( \mathrm { t } ) , \mathrm { t } ) ,$ if buyer accepts $\mathrm { P } _ { \cal S } ( \mathrm { t } ) .$ . However, the buyer has two more options, one of which is to quit. If the buyer quits the negotiation, then the seller can only have $\mathrm { U } _ { \mathrm { S } } ^ { 0 } ( \mathrm { t } )$ for leaving the negotiation at time t. The buyer's third option is to bargain. Suppose that the buyer is not satis<sup>fi</sup>ed with the seller's proposed price, yet he is con<sup>fi</sup>dent of making a better deal at a later time. Then the buyer will choose to bargain, which means $\mathrm { P } _ { \cal S } ( \mathrm { t } )$ is rejected and a new price $\mathrm { P _ { B } } ( \mathrm { t } + 1 )$ is proposed. The process will accordingly continue to the next round and it is the seller's turn to make the decision whether to accept, quit or bargain. Seller's utility in the next round can be denoted by EU (t+1).

Since the seller is not certain whether the other party will accept, reject, or bargain in response to the proposed price $\mathrm { { P } } _ { \cal { S } } ( \mathrm { t } ) ,$ a subjective probability may be adopted to model the seller's belief about the buyer's reaction. Herewith, the seller's expected utility of price $\mathrm { P } _ { \cal { S } } \left( \mathrm { t } \right)$ time t is:

$$
\begin{array}{c} \mathrm{EU} _ {S} (\mathrm{P} _ {S} (t), t) = \mathrm{U} _ {S} (\mathrm{P} _ {S} (t), t) \cdot \operatorname * {P r} (\text {buyer   accepts}) + \mathrm{EU} _ {S} (t + 1) \\ \times \operatorname * {P r} (\text {buyer   bargains}) + \mathrm{U} _ {S} ^ {0} (t) \cdot \operatorname * {P r} (\text {buyer   quits}) \\ \text {and} \operatorname * {P r} (\text {buyer   accepts}) + \operatorname * {P r} (\text {buyer   bargains}) + \operatorname * {P r} (\text {buyer   quits}) = 1 \end{array}\tag{1}
$$

According to A2 and A5, an agent's utility of price P at time t can be calculated by the difference between agreed price and reservation price $( \mathtt { R } _ { \mathtt { S } } )$ minus the back-dragging cost $( \mathsf { C } _ { \mathsf { S } }$ per round) at time t. Reservation price here is the minimum price at which the seller is willing to sell the item under negotiation. Thus, the seller's utility function is $\begin{array} { r } { \mathrm { U } _ { \mathrm { S } } ( \mathrm { P } _ { \mathrm { S } } ( \mathrm { t } ) , \mathrm { t } ) { = } \mathrm { P } _ { \mathrm { S } } ( \mathrm { t } ) { - } \mathrm { R } _ { \mathrm { S } } { - } ( \mathrm { t } - 1 ) { \cdot } \mathrm { C } _ { \mathrm { S } } . } \end{array}$ Since quitting the negotiation does not bring either party any bene<sup>fi</sup>t, but results in both parties incurring costs, the payoff of ‘quit' option can be denoted as: $\mathrm { U } _ { \mathrm { S } } ^ { 0 } ( \mathrm { t } ) =$ $- ( \mathrm { t } - 1 ) { \cdot } \mathsf { C } _ { \mathrm { S } }$ and $\mathsf { U } _ { \mathrm { B } } ^ { 0 } ( \mathrm { t } ) { = } { - } ( \mathrm { t } { - } 1 ) { \cdot } \mathsf { C } _ { \mathrm { B } }$

For the expected utility of the next round, the best outcome is for the parties to make a deal at $\mathrm { P } _ { \cal S } ( \mathrm { t } )$ and the worst is for the buyer to quit the negotiation. Therefore, we $\mathrm { h a v e - t . } C _ { S } \leq \mathrm { E U } _ { S } \ ( \mathrm { t } + 1 ) \leq \mathrm { P } _ { S } ( \mathrm { t } ) - \mathrm { R } _ { S } - \mathrm { t } \cdot C _ { S }$

Let α be the coef<sup>fi</sup>cient of risk preferences, as follows:

$$
\begin{array}{c} \mathrm{EU} _ {S} (t + 1) = (- t \cdot C _ {S}) \cdot (1 - \alpha) + (\mathrm{P} _ {S} (t) - \mathrm{R} _ {S} - t \cdot C _ {S}) \cdot \alpha = - t \cdot C _ {S} + (\mathrm{P} _ {S} (t) - \mathrm{R} _ {S}) \\ \times \alpha , (0 \leq \alpha \leq 1). \end{array}
$$

For simplicity of analysis, we assume totally risk averse agents, and α here is supposed to be 0, which refers to the seller's expected utility gain from the worst case where the buyer quits the negotiation. With this simpli<sup>fi</sup>cation, a closed form solution for optimal strategies can be induced, and it is expected that all the results would hold even when α is non-zero. The utility function is then as follows:

$$
\begin{array}{r l} \mathrm{EU} _ {S} (P _ {S} (t), t) & = \mathrm{U} _ {S} (P _ {S} (t), t) \cdot \operatorname * {P r} (\text { buyer   accepts }) + \mathrm{EU} _ {S} (t + 1) \\ & \quad \times \operatorname * {P r} (\text { buyer   bargains }) + \mathrm{U} _ {S} ^ {0} (t) \cdot \operatorname * {P r} (\text { buyer   quits }) \\ & = (P _ {S} (t) - R _ {S} - (t - 1) \cdot C _ {S}) \cdot \operatorname * {P r} (\text { buyer   accepts }) - t \cdot C _ {S} \\ & \quad \times \operatorname * {P r} (\text { buyer   bargains }) - (t - 1) \cdot C _ {S} \cdot \operatorname * {P r} (\text { buyer   quits }) \\ & = - (t - 1) C _ {S} + (P _ {S} (t) - R _ {S}) \cdot \operatorname * {P r} (\text { buyer   accepts }) - C _ {S} \\ & \quad \times \operatorname * {P r} (\text { buyer   bargains }). \end{array}\tag{2}
$$

## 4.1.3. Bidding strategy

In economic models, all subjects are supposed to maximize their utility. That is:

$$
\begin{array}{r l} \underset {P _ {S} (t)} {\text { MaxEU}} _ {S} (P _ {S} (t), t) = & - (t - 1) C _ {S} + \underset {P _ {S} (t)} {\text { Max }} \left[ (P _ {S} (t) - R _ {S}) \cdot \operatorname * {P r} (\text { buyer   accepts }) \right. \\ & \left. - C _ {S} \cdot \operatorname * {P r} (\text { buyer   bargains }) \right] \cdot \end{array}\tag{3}
$$

The fundamental trade-off of our model is in accordance with the general bargaining situation. If a higher $\mathrm { P } _ { \cal { S } } ( \mathrm { t } )$ is proposed, the seller may possibly obtain a higher pro<sup>fi</sup>t; however, the possibility of buyer acceptance would be lower.

Given the seller's proposed price $\mathrm { P } _ { \cal S } ( \mathrm { t } )$ , the buyer will choose an action which makes him better off according to the payoff structure:

$$
\left\{ \begin{array}{l l} U _ {B} (P _ {S} (t), t) & , \text {   accept   } \\ E U _ {B} (P _ {B} (t + 1), t + 1) & , \text {   bargain   }. \\ U _ {B} ^ {0} (t) & , \text {   quit   } \end{array} \right.\tag{4}
$$

Based on the model proposed above, truth revelation and ef<sup>fi</sup>ciency of the RPR mechanism are examined in the following part of this section.

## 4.2. Truth revelation in the RPR mechanism

Whether the reported reservation price is the same as the actual one is crucial to the performance of the RPR mechanism. We therefore examine the agents' strategies and a possible equilibrium and then analyze truth revelation in a risk-averse situation.

## 4.2.1. One-round bidding

In the context of one-round bidding, each side bids only once. If the bidding price of one side is acceptable to the other side, a deal is made at this price. Otherwise, the negotiation breaks down. Pmin is the minimum price for the item in the market and Pmax is the maximum price for the item in the market. As stated above in assumption $\mathsf { A 3 } ,$ suppose all the reservation prices of the seller $( \mathsf { R } _ { \mathsf { S } } )$ and the willingness-to-pay of the buyer $\left( \mathbb { R } _ { \mathrm { B } } \right)$ are expected to be in the range $[ \mathrm { P _ { m i n } } , \mathrm { P _ { m a x } } ]$ and uniformly distributed, and all the traders, including the seller and the buyer, know $\mathrm { P } _ { \mathrm { m a x } }$ and $\operatorname { P } _ { \operatorname* { m i n } } .$ . Suppose all the bidding prices are in the range $[ \mathrm { P } _ { \operatorname* { m i n } } , \mathrm { P } _ { \operatorname* { m a x } } ] ,$ , then a negotiator will accept the other party's offer. RPR informs negotiators about the existence of a positive bargaining zone, which means that the willingness-to-pay of the buyer $\left( \mathsf { R } _ { \mathrm { B } } \right)$ is greater than the reservation price of the seller $( \mathbb { R } _ { \mathbb { S } } ) .$ In this case, if both negotiators are rational, the probability of quitting the negotiation is theoretically zero because ‘quitting' is not a rational strategy. When there is a positive bargaining zone, negotiators can reach an agreement at the price that is less than the buyer's willingness-to-pay and more than the seller's reservation price. In this case, it is rational to reach an agreement since both the seller and the buyer can bene<sup>fi</sup>t. According to Eq. (3), in order to maximize his expected utility, the seller's bidding price $\mathrm { P } _ { \cal S }$ should satisfy:

$$
\begin{array}{r l} \max _ {P _ {S}} E U _ {S} (P _ {S}) & = (P _ {S} - R _ {S}) \cdot \operatorname * {P r} (R _ {B} \geq P _ {S}) - C _ {S} \cdot \operatorname * {P r} (R _ {B} <   P _ {S}) \\ & = (P _ {S} - R _ {S}) \cdot f _ {P _ {S}} ^ {P _ {\max}} f _ {B} (R _ {B}) d R _ {B} - C _ {S} \cdot f _ {R _ {S}} ^ {P _ {S}} f _ {B} (R _ {B}) d R _ {B} \\ & = (P _ {S} - R _ {S}) \cdot \frac {P _ {\max} - P _ {S}}{P _ {\max} - R _ {S}} - C _ {S} \cdot \frac {P _ {S} - R _ {S}}{P _ {\max} - R _ {S}} \end{array}\tag{5}
$$

then,

$$
\mathrm{P} _ {S} = \frac {\mathrm{P} _ {\max} + \mathrm{R} _ {S} - \mathrm{C} _ {S}}{2}.\tag{6}
$$

The chance of a deal is the probability that seller's bidding price is smaller than or equal to the buyer's willingness-to-pay, i.e.,

$$
\begin{array}{r l} \operatorname * {P r} (\text { dealing   at   first   round }) & = \operatorname * {P r} (R _ {B} \geq P _ {S}) = \frac {P _ {\max} - P _ {S}}{P _ {\max} - R _ {S}} \\ & = \frac {P _ {\max} - \frac {P _ {\max} + R _ {S} - C _ {S}}{2}}{P _ {\max} - R _ {S}} \\ & = \frac {P _ {\max} - R _ {S} + C _ {S}}{2 (P _ {\max} - R _ {S})}. \end{array}\tag{7}
$$

Similarly, the buyer's bidding price can be inferred. Then, the chance to reach a deal is the probability of the buyer making a counteroffer, as in Eq. (9).

$$
\mathrm {P_ {B}} = \frac {\mathrm {P_ {min}} + \mathrm {R_ {B}} + \mathrm {C_ {B}}}{2}.\tag{8}
$$

$$
\begin{array}{r l} \operatorname * {P r} (\text { dealing   at   second   round }) & = (1 - \operatorname * {P r} (R _ {B} \geq P _ {S})) \cdot \operatorname * {P r} (R _ {S} \leq P _ {B}) \\ & = \frac {P _ {B} - P _ {\min}}{R _ {B} - P _ {\min}} \cdot \frac {\frac {P _ {\min} + R _ {B} + C _ {B}}{2} - P _ {\min}}{R _ {B} - P _ {\min}} \\ & = \frac {R _ {B} - P _ {\min} + C _ {B}}{2 (R _ {B} - P _ {\min})}. \end{array}\tag{9}
$$

## 4.2.2. Equilibrium for risk-averse agents

Risk-averse agents perceive minimal expected utility on future rounds under the condition that no deal is made in the current round.

Therefore, if the proposed price of the seller is considered the maximum possible deal price Pmax, and the minimum possible deal price is Pmin of the buyer, then the situation is the same as that of a one-shot bid within a single round. The pricing strategy of the seller and buyer at time t (tN1) can be induced from the previous section:

$$
P _ {S} (t) = \frac {R _ {S} + P _ {S} (t - 1) - C _ {S}}{2}\tag{10}
$$

$$
P _ {B} (t) = \frac {R _ {B} + P _ {B} (t - 1) + C _ {B}}{2}.\tag{11}
$$

If the <sup>fi</sup>rst bidding price is known, then the recursive expression of bidding strategy can be resolved as a dependent variable of the <sup>fi</sup>rst bidding price and time t:

$$
P _ {S} ^ {*} (t) = \frac {1}{2 ^ {t}} P _ {\max} + \left(R _ {S} - C _ {S}\right) \left(1 - \frac {1}{2 ^ {t}}\right)\tag{12}
$$

$$
P _ {B} ^ {*} (t) = \frac {1}{2 ^ {t}} P _ {\min} + \left(R _ {B} + C _ {B}\right) \left(1 - \frac {1}{2 ^ {t}}\right).\tag{13}
$$

According to the reservation-price-deal rule, a seller will accept any offer that is higher than or equal to his or her reservation price and a buyer will accept any offer that is lower than or equal to his or her willingness-to-pay. According to the proposed mechanism, the <sup>fi</sup>nal deal price can be proposed by either the seller or buyer. Suppose there are equal chances for each case:

$$
\begin{array}{l} \mathrm{EP} ^ {*} (t) = \mathrm{P} _ {\mathrm{S}} ^ {*} (\mathrm{t}) \cdot \operatorname * {P r} (\text { Seller   proposes   the   final   dealing   price }) \\ \qquad + \mathrm{P} _ {\mathrm{B}} ^ {*} (\mathrm{t}) \cdot \operatorname * {P r} (\text { Buyer   proposes   the   final   dealing   price }) \\ \qquad = \frac {\mathrm{R} _ {\mathrm{S}} + \mathrm{P} _ {\mathrm{S}} ^ {*} (\mathrm{t} - 1) - \mathrm{C} _ {\mathrm{S}}}{2} \cdot \frac {1}{2} + \frac {\mathrm{R} _ {\mathrm{B}} + \mathrm{P} _ {\mathrm{B}} ^ {*} (\mathrm{t} - 1) + \mathrm{C} _ {\mathrm{B}}}{2} \cdot \frac {1}{2}. \end{array}\tag{14}
$$

Suppose the extreme case where the bargaining zone is so small that the maximum turns are needed before a price within the reservation prices is proposed by one side. In this case, a deal is made when t→∞, and we can assume $\mathsf { P } ^ { * } ( \mathsf { t } ) { \approx } \mathsf { P } ^ { * } ( \mathsf { t } - 1 )$ . If this is substituted into Eq. (14), we have:

$$
\mathrm{EP} ^ {*} (t) = \frac {R _ {S} + R _ {B} - C _ {S} + C _ {B}}{2}.\tag{15}
$$

If a seller proposes the <sup>fi</sup>nal deal price with probability $\gamma ,$ and the buyer proposes with probability $1 - \gamma ,$ , then the expected deal price is: $\begin{array} { r } { \mathrm { E P ^ { * } \left( t \right) } = ( \mathrm { R } _ { \mathrm { S } } - \mathrm { C } _ { \mathrm { S } } ) { \cdot } \gamma + \left( \mathrm { R } _ { \mathrm { B } } + \mathrm { C } _ { \mathrm { B } } \right) ( 1 - \gamma ) . } \end{array}$

If the back-dragging costs are the same for the two sides, the expected deal price under the given mechanism is in accordance with the $" f a 1 r "$ allocation rule in common system-mediated mechanisms, i.e., dividing the cake into two equal parts.

## 4.2.3. Proof of truth revelation

According to Eq. (15), if the reservation price is truthfully reported, then the seller's expected utility is:

$$
\begin{array}{r l} \mathrm{EU} _ {S} ^ {\mathrm{T}} & = (\mathrm{EP} ^ {*} - R _ {S}) \cdot \operatorname * {P r} (\text { positive   bargaining   zone }) - C _ {S} \\ & \times \operatorname * {P r} (\text { negative   bargaining   zone }) \\ & = \left(\frac {R _ {S} + R _ {B} - C _ {S} + C _ {B}}{2} - R _ {S}\right) \cdot \frac {P _ {\max} - R _ {S}}{P _ {\max} - P _ {\min}} - C _ {S} \cdot \frac {R _ {S} - P _ {\min}}{P _ {\max} - P _ {\min}}. \end{array}\tag{16}
$$

If the reservation price is falsely reported by increasing the reservation price $\Delta \ R _ { S } { > } 0 ,$ , then the seller's expected utility is:

$$
\begin{array}{l} \mathrm{EU} _ {S} ^ {\mathrm{F}} = \left(\frac {\left(R _ {S} + \Delta R _ {S}\right) + R _ {B} - C _ {S} + C _ {B}}{2} - R _ {S}\right) \cdot \frac {P _ {\max} - \left(R _ {S} + \Delta R _ {S}\right)}{P _ {\max} - P _ {\min}} - C _ {S} \\ \times \frac {\left(R _ {S} + \Delta R _ {S}\right) - P _ {\min}}{P _ {\max} - P _ {\min}}. \end{array}\tag{17}
$$

Comparing the expected utility:

$$
\mathrm{EU} _ {\mathrm{S}} ^ {\mathrm{T}} - \mathrm{EU} _ {\mathrm{S}} ^ {\mathrm{F}} = \frac {\Delta R _ {\mathrm{S}} ^ {2} + \left(R _ {\mathrm{B}} + C _ {\mathrm{B}} + C _ {\mathrm{S}} - P _ {\max}\right) \cdot \Delta R _ {\mathrm{S}}}{2 \left(P _ {\max} - P _ {\min}\right)}.\tag{18}
$$

Therefore, if the buyer's back-dragging cost is large enough to satisfy $\mathsf { C } _ { \mathsf { B } } + \mathsf { C } _ { \mathsf { S } } \geq \mathsf { P } _ { \operatorname* { m a x } } - \mathsf { R } _ { \mathsf { B } }$ (i.e., $\mathrm { R } _ { \mathrm { B } } { + } \mathrm { C } _ { \mathrm { B } } { + } \mathrm { C } _ { S } { - } \mathrm { P } _ { \mathrm { m a x } } { \geq } 0 )$ , then there is no need for the seller to report a false reservation price (as shown in Fig. 1), since Eq. (18) will always be greater then zero, which means truth-telling may bring more expected utility to the seller.

If $\mathsf { C } _ { \mathsf { B } } + \mathsf { C } _ { \mathsf { S } } { < } \mathsf { P } _ { \operatorname* { m a x } } { - } \mathsf { R } _ { \mathsf { B } }$ (as the dashed curve in Fig. 1.), then the seller will increase his reservation price by $\begin{array} { r } { \Delta \mathsf { R } _ { \mathsf { S } } = \frac { \mathsf { P } _ { \operatorname* { m a x } } - \mathsf { R } _ { \mathsf { B } } - \mathsf { C } _ { \mathsf { B } } - \mathsf { C } _ { \mathsf { S } } } { 2 } } \end{array}$ for maximum expected utility. When the seller makes the decision of whether to tell the truth, he does not know the buyer's exact willingness-to-pay, which is needed in order to evaluate whether truth telling is more pro<sup>fi</sup>table. Since the possible price range of the product in the market is common knowledge, however, the expected value of the buyer's willingness-to-pay can be estimated by $\mathrm { E } \dot { \mathrm { R _ { B } } } = \frac { \mathrm { P _ { \mathrm { m a x } } } + \mathrm { P _ { \mathrm { m i n } } } } { 2 }$ according to A3. And the truth telling decision condition will be $\mathsf { \bar { C } _ { B } } + \mathsf { C _ { S } } \ge \frac { \mathsf { P _ { m a x } } - \mathsf { P _ { m i n } } } { 2 }$ . If this condition is not met, then the seller will report a false reservation price by $\begin{array} { r } { \Delta \mathsf { R } _ { \mathsf { S } } = \frac { \mathrm { P } _ { \mathrm { m a x } } - \mathrm { P } _ { \mathrm { m i n } } - \mathrm { C } _ { \mathrm { B } } - \mathrm { C } _ { \mathrm { S } } } { 2 } , } \end{array}$ . The higher the sum of the back-dragging cost, the less likely it is that a fake amount will be reported.

Similarly, we may infer that the buyer will also have an incentive to tell the truth on this condition. If this condition does not hold, then the likelihood of a false report will be $\Delta \mathrm { R _ { B } } = \frac { \mathrm { P _ { m a x } } - \mathrm { P _ { m i n } } - \mathrm { C _ { B } } - \mathrm { C } _ { S } } { 2 }$ . Therefore, we propose the following:

Proposition 1. If the sum of the buyer's and the seller's back-dragging cost is no less than half of the difference between the maximum and minimum prices, then both sides will report their true reservation price or willingnessto-pay for the item. $( \left\{ \begin{array} { l l } { \Delta \mathrm { R } _ { \mathrm { S } } = 0 } \\ { \Delta \mathrm { R } _ { \mathrm { B } } = 0 } \end{array} \right.$ ; when $\mathsf C _ { \mathrm B } + \mathsf C _ { \mathrm S } \geq \ \frac { \mathsf P _ { \mathrm { m a x } } - \mathsf P _ { \mathrm { m i n } } } { 2 } )$ In addition, both sides will be more honest if the sum of the back-dragging cost is relatively higher. $( \left\{ \begin{array} { l l } { \Delta \mathrm { R } _ { \mathrm { S } } { > } \Delta \mathrm { R } _ { \mathrm { S } } ^ { ' } } \\ { \Delta \mathrm { R } _ { \mathrm { B } } { > } \Delta \mathrm { R } _ { \mathrm { S } } ^ { ' } } \end{array} \right.$ ; if $\mathsf C _ { \mathrm { B } } + \mathsf C _ { \mathrm { S } } { < } \mathsf C _ { \mathrm { B } } ^ { ' } + \mathsf C _ { \mathrm { S } } ^ { ' } )$

## 4.3. Increased social welfare in the RPR mechanism

The RPR mechanism is superior to the traditional bargaining mechanism because it may increase dealings by ensuring a positive bargaining zone before the negotiation starts. Further, overall social welfare is also expected to increase by decreasing total back-dragging cost.

## 4.3.1. Decrease of the expected number of rounds

Deals may increase through the RPR mechanism by 1) terminating the negotiation process before the <sup>fi</sup>rst round, if there is a negative bargaining zone; 2) facilitating trust among agents based on a positive bargaining zone and truth-telling incentives. The free bargaining case will be further examined and compared with the RPR mechanism in the next section.

![](/api/attachments/FG3UPVF4/fulltext/images/6d47acfcfb888129f2b6671a3b5e4fc1542235296ceb704e51ae103569382d87.jpg)  
Fig. 1. Difference on expected utility.

Aside from acceptance and rejection by rational agents, there is a third possibility of termination (i.e., negotiation terminates without further communication) in free bargaining without a deal guarantee in RPR. Expected utility function in the context of free bargaining is as shown in the following function. For one-round bidding, we have:

$$
\begin{array}{r l} \max _ {P _ {S}} E U _ {S} (P _ {S}) & = (P _ {S} - R _ {S}) \cdot \operatorname * {P r} (R _ {B} \geq P _ {S}) - C _ {S} \cdot \operatorname * {P r} (R _ {S} \leq R _ {B} <   P _ {S}) + U _ {S} ^ {0} \cdot \operatorname * {P r} (R _ {B} <   R _ {S}) \\ & = (P _ {S} - R _ {S}) \cdot \int_ {P _ {S}} ^ {P _ {\text {max}}} f _ {B} (R _ {B}) d R _ {B} - C _ {S} \cdot \int_ {R _ {S}} ^ {P _ {S}} f _ {B} (R _ {B}) d R _ {B} \\ & + U _ {S} ^ {0} \cdot \int_ {P _ {\min}} ^ {R _ {S}} f _ {B} (R _ {B}) d R _ {B} \\ & = (P _ {S} - R _ {S}) \cdot \frac {P _ {\text {max}} - P _ {S}}{P _ {\text {max}} - P _ {\text {min}}} - C _ {S} \cdot \frac {P _ {S} - R _ {S}}{P _ {\text {max}} - P _ {\text {min}}} + U _ {S} ^ {0} \cdot \frac {R _ {S} - P _ {\text {min}}}{P _ {\text {max}} - P _ {\text {min}}} \end{array} \tag {19}
$$

$$
\mathrm{P} _ {S} = \frac {\mathrm{P} _ {\max} + \mathrm{R} _ {S} - \mathrm{C} _ {S}}{2}.\tag{20}
$$

As shown above, the pricing strategy is not different with the RPR mechanism. However, the chance of a deal is different from that of the RPR mechanism:

$$
\begin{array}{r l} \operatorname * {P r} _ {\text { FREE }} (\text { dealing   at   first   round }) & = \operatorname * {P r} (R _ {B} \geq P _ {S}) = \frac {P _ {\max} - P _ {S}}{P _ {\max} - P _ {\min}} \\ & = \frac {P _ {\max} - R _ {S} + C _ {S}}{2 (P _ {\max} - P _ {\min})}. \end{array}\tag{21}
$$

Suppose the possible range of deal prices [Pmin, Pmax] and the backdragging costs are the same in free bargaining and RPR; we may compare this with Eq. (7):

$$
\left\{ \begin{array}{l l} \operatorname * {P r} _ {\text { FREE }} (\text { dealing   at   first   round }) \leq \operatorname * {P r} _ {\text { RPR }} (\text { dealing   at   first   round }) & , \mathrm{P} _ {\min} \leq \mathrm{R} _ {S} \\ \operatorname * {P r} _ {\text { FREE }} (\text { dealing   at   first   round }) > \operatorname * {P r} _ {\text { RPR }} (\text { dealing   at   first   round }) & , \mathrm{P} _ {\min} > \mathrm{R} _ {S} \end{array} \right.\tag{22}
$$

This equation shows that when con<sup>fl</sup>ict is low $( \mathrm { i } . \mathrm { e } . , \ \mathrm { P } _ { \mathrm { m i n } } { > } \mathrm { R } _ { S } )$ , free bargaining has a higher probability of reaching a deal in the <sup>fi</sup>rst round. On the other hand, when con<sup>fl</sup>ict is high $( \mathrm { i } . { \bf e } . , \ \mathrm { P } _ { \mathrm { m i n } } { \leq } \mathrm { R } _ { \mathrm { S } } ) ,$ negotiations under RPR have a higher probability of reaching a deal in the <sup>fi</sup>rst round. Further, the probability of reaching a deal in later rounds is higher under the RPR mechanism than free bargaining when con<sup>fl</sup>ict is relatively high.

Therefore, compared to free bargaining as in the TDB mechanism, the RPR mechanism facilitates a higher chance of obtaining a deal. At the same time, the expected payoffs for agents under the RPR mechanism are not lower than under free bargaining, since the pricing strategy is almost the same in both cases. Therefore, we may conclude that the RPR mechanism can function as an incentive for rational agents.

As we have already proved above in Eqs. (21) and (22), the chance of a deal in each round is increased using the RPR mechanism. Therefore, under the RPR mechanism, the total expected number of rounds will decrease accordingly. We propose the following:

Proposition 2. When seller's reservation price and buyer's willingnessto-pay are within the range of the minimum price and the maximum price, negotiations under the RPR mechanism will have fewer rounds than those under the TDB mechanism. (Et ≥Et , when $R _ { S } , R _ { B } { \in } [ \operatorname* { P } _ { \operatorname* { m i n } } , \operatorname* { P } _ { \operatorname* { m a x } } ] ) .$

## 4.3.2. Overall increase in return

According to our assumptions, in a certain round, bargaining under the RPR mechanism can be considered as a zero-sum game, in which one side's gain is the other side's lost. However, from the view of the whole negotiation process, if a deal is not made in a certain round, both sides will incur some amount of back-dragging cost.

$$
\mathrm{U} _ {\text {social}} = \mathrm{U} _ {S} + \mathrm{U} _ {B} = \left(\mathrm{P} ^ {*} - \mathrm{R} _ {S} - \mathrm{C} _ {S} \cdot \mathrm{Et} ^ {*}\right) + \left(\mathrm{R} _ {S} - \mathrm{P} ^ {*} - \mathrm{C} _ {B} \cdot \mathrm{Et} ^ {*}\right) = - \left(\mathrm{C} _ {S} + \mathrm{C} _ {B}\right) \cdot \mathrm{Et} ^ {*}\tag{23}
$$

It has been proved that $\operatorname { E t } ^ { * }$ decreases under the RPR mechanism. Therefore, we expect an average increase in terms of social welfare.

An overall increase in return is obtained under the RPR mechanism as a result of: 1) eliminating occasions of a negative bargaining zone which will lead to no deal; 2) setting up reservation-price deal rules that help agents save time, since any bid that is between the reservation price and willingness-to-pay is likely to end the negotiation without the need for further rounds.

## 4.4. The ERPR mechanism

Given the guidance such as ‘your bid is good' or ‘your bid is not reasonable’, the agents may alter their bids before submission. According to A4 and $\mathsf { A } 5 ,$ after viewing the system's guidance, the seller will lower his or her price or not change it and the buyer will increase his or her bid or not change it. Suppose the seller will alter his or her bid by $\Delta \mathsf { P } _ { S } \ ( \Delta \mathsf { P } _ { S } { \leq } 0 )$ , then the seller's bidding price will be $\mathrm { P } _ { S } + \Delta \mathrm { P } _ { S } .$ If the new bidding price is substituted in (7), then $\mathrm { P r } _ { \mathrm { E R P R } } |$ dealing at first round $\mathbf { \mu } = \frac { \mathrm { P _ { m a x } } - \mathrm { R } _ { S } + \mathrm { C } _ { S } - 2 \Delta \mathrm { P } _ { S } } { 2 ( \mathrm { P _ { m a x } } - \mathrm { R } _ { S } ) } ,$ . Since $\Delta  { \mathrm { P } } _ { S }$ is no greater than zero, the result is $\mathrm { P r } _ { \tt E R P R }$ (dealing at <sup>fi</sup>rst round)≥ $\operatorname { P r } _ { \mathrm { R P R } }$ (dealing at <sup>fi</sup>rst round). Similar to previous discussion, the negotiations under the ERPR mechanism were found to have fewer expected rounds than those under the RPR mechanism since the chance of acceptance is greater in each round under the ERPR mechanism.

Proposition 3. With extended bid information, the buyer and seller tend to make greater concessions and rounds will be fewer in number under the ERPR mechanism than under the RPR mechanism. $( E t _ { R P R } \geq E t _ { E R P R } ) .$

## 5. Experimental design

We conducted an experiment to test the effectiveness of the TDB, RPR and ERPR mechanisms in a controlled negotiation context. Combinations of buyer's willingness-to-pay and seller's reservation price and back-dragging costs were designed to prove the three propositions in our analytical model.

## 5.1. A prototype NSS

We developed a prototype NSS for the experiments. This system should: 1) generate experimental negotiation sessions; 2) support the TDB, RPR and ERPR mechanisms; 3) randomlyassign buyers and sellers to one negotiation session. Subjects who participated in the experiment were asked to log into the NSS. Then, the system matched negotiation pairs and informed the subjects about the reservation prices and willingness-to-pay for the items up for negotiation. The system was designed as a three-layered browser/server based architecture. Persistent data entities, process handlers and interface presentations were independent of each other so that modi<sup>fi</sup>cation of the system would be easier. We implemented the system using a Java framework, which has been used in several other applications and has beenproved to be reliable.

## 5.2. Methodology

## 5.2.1. Participants and design

Sixty-seven undergraduate students, enrolled in introductory courses in management sciences, participated in the experiment. Participants received extra course credit in exchange for their participation. In addition, participants received cash rewards based on their performance in the experiment. The experiment design was a

2×3 factorial, with back-dragging costs (high vs. low) and types of negotiation support system mechanism (TDB, RPR, ERPR).

## 5.2.2. Manipulations

5.2.2.1. NSS mechanism. There were 3 types of NSS mechanisms. First, the TDB mechanism led negotiators to take turns bidding through the website. Second, the RPR mechanism informed subjects of their reservation price or willingness-to-pay. Then, subjects were asked to report their true reservation price or willingness-to-pay to the system. The subjects were warned that reporting a false reservation price or willingness-to-pay might prevent the start of a negotiation session. Third, the ERPR mechanism extended the RPR mechanism by providing negotiators with advice on their bidding in addition to reporting their reservation price or willingness-to-pay to the system. If bids were too far from the reasonable range (25% range with respect to the middle point of the seller's reservation price and the buyer's willingness-to-pay), the system informed bidders that their bids were not reasonable. Negotiators received the system's advice on their bids before they were actually delivered to the negotiation partner. Therefore, negotiators had one chance to alter their bids.

5.2.2.2. Back-dragging cost. There were 2 types of back-dragging cost conditions. In the high back-dragging cost condition, each negotiator (i.e., seller and buyer) lost 4% of the size of the bargaining zone when an additional round was added. In the low back-dragging cost condition, each negotiator lost 1% of the size of the bargaining zone when an additional round was added.

## 5.2.3. Task and procedure

We adopted the scenario of trading laptop computers as presented in the third section. Subjects were randomly assigned to one of the NSSs (TDB, RPR, ERPR) and the role of buyer or seller by prototype NSS. The system generated four negotiation sessions for each subject. The <sup>fi</sup>rst two sessions were practice sessions for subjects to get familiar with the operation of the website. The next two sessions were real and the <sup>fi</sup>nal reward was calculated based on the results of these two sessions. One of the real experiments was a high back-dragging cost condition (4% of the size of the bargaining zone for seller and buyer each) and the other was low back-dragging cost condition (1% of the size of the bargaining zone). A negotiator did not know who his or her negotiating partner was. Onlya three digit user ID was revealed to the negotiating partner. Prior to the bidding, the experimenters explained the process to the subjects. Based on the pro<sup>fi</sup>ts made during the real sessions, participants were rewarded with cash after the experiment.

## 6. Results and discussions

Table 1 summarizes the bidding records as well as the <sup>fi</sup>nal results of each negotiation session.

Summary of results

<table><tr><td></td><td>TDB</td><td>RPR</td><td>ERPR</td></tr><tr><td>Total number of Sessions</td><td>38</td><td>53</td><td>32</td></tr><tr><td>Success rate (%)</td><td>0.97</td><td>0.91</td><td>0.88</td></tr><tr><td colspan="4">Successful sessions</td></tr><tr><td>Number</td><td>37</td><td>48</td><td>28</td></tr><tr><td>Average number of rounds</td><td>4.0</td><td>3.1</td><td>2.4</td></tr><tr><td>Standard deviation</td><td>3.20</td><td>2.08</td><td>1.57</td></tr><tr><td>Average total profit</td><td>92.32</td><td>92.91</td><td>96.04</td></tr><tr><td colspan="4">Failed sessions</td></tr><tr><td>Number</td><td>1</td><td>5</td><td>4</td></tr><tr><td>Average number of rounds</td><td>5.0</td><td>3.4</td><td>1.3</td></tr><tr><td>Standard deviation</td><td></td><td>2.30</td><td>1.26</td></tr><tr><td>Average total profit</td><td>-18.00</td><td>-5.00</td><td>-2.00</td></tr></table>

Table 2 Truth revelation

<table><tr><td>Data</td><td>High back-dragging cost</td><td>Low back-dragging cost</td></tr><tr><td>Number of reports</td><td>70</td><td>79</td></tr><tr><td>Deviation ratio</td><td>6.9%</td><td>8.2%</td></tr><tr><td>Number of rounds</td><td>2.50</td><td>3.18</td></tr><tr><td>Statistical significance</td><td>p&lt;.10 (p=.06)</td><td></td></tr></table>

Since the payoff structures were not the same, we normalized all records to make them comparable to each other. Table 1 reports the success rates, the average number of rounds to reach agreement, and the average total pro<sup>fi</sup>t the subjects achieved using each of the three mechanisms. Negotiators had positive bargaining zones; therefore reaching an agreement was possible. However, some negotiators could not reach an agreement under all three mechanisms. In this section, the results are discussed in terms of the number of rounds to reach an agreement, truth revelation, and fairness.

## 6.1. Number of rounds and social welfare

Generally, the fewer the number of rounds to reach an agreement and the higher the joint pro<sup>fi</sup>ts (i.e., the sum of two negotiators pro<sup>fi</sup>ts), the more ef<sup>fi</sup>cient the negotiation sessions were. We compared three mechanisms (TDB, RPR and ERPR) in terms of the number of rounds in successful sessions, because fewer rounds brought more social welfare as a result of lower back-dragging costs.<sup>5</sup>

Planned contrast was used to determine whether the RPR and ERPR mechanisms shortened the number of rounds compared with the TDB mechanism (proposition 2) [5]. Planned contrast indicated that the RPR and ERPR mechanisms led negotiators to reach an agreement faster than the TDB mechanism (t=2.488, pb.01). Compared with TDB, both RPR and ERPR are more effective in reducing the number of rounds. Therefore, Proposition 2 of the analytical model is supported.

To test Proposition 3, we compared 2 NSSs (RPR vs. ERPR). The result of the t-test shows that there was a signi<sup>fi</sup>cant difference between the number of rounds of ERPR and RPR (t=1.440, pb.10, ERPR: 2.4 vs. RPR: 3.1). That is, participants reached an agreement faster under the ERPR system rather than under the RPR system. Therefore, Proposition 3 was supported.

## 6.2. Truth revelation

Proposition 1 of our analytical model was empirically tested; that is, we tested whether negotiators were more honest when the sum of back-dragging costs was relatively higher. In our experiment, the extent of truth revelation was calculated by the average deviation ratio (See Table 2 for results). We measured the deviation ratio by calculating how much a negotiator's reporting price deviated from the reservation price. The reservation price of the seller is the actual cost of the item and that of the buyer is the true amount of money he or she is willing to pay for the item. For example, the average deviation ratio of a seller is lower when the reporting price is closer to the actual cost of the item, while the average deviation ratio of a buyer is lower when the reporting price is closer to the true amount of money he or she is willing to pay. Therefore, the lower the average deviation ratio, the higher is the level of truth revelation. We found that the average deviation ratio of reporting price with high back-dragging cost (6.9%) was lower than with low back-dragging cost (8.2%) with statistical signi<sup>fi</sup>cance (p=.06). Therefore, Proposition 1 regarding truth revelation was supported.

## 6.3. Fairness

In our experiment, sellers placed bids before buyers. That is, sellers initiated the negotiation. In the TDB and RPR conditions, there were no differences in terms of payoffs between initiators (i.e., sellers) and followers (i.e., buyers). In the ERPR mechanism condition, however, buyers' payoffs were much higher than sellers' (buyer: 61.9, seller: 34.2, t=5.08, pb.001).

This result was interesting since it was not expected in our analytical model. With the examination of subjects' bidding behaviors, we found that the information provided in the ERPR sessions resulted in less aggressive starting bids by the sellers. The sellers in the TDB and RPR conditions made extreme <sup>fi</sup>rst offers and used those as anchors. In contrast, the sellers in the ERPR condition did not make extreme <sup>fi</sup>rst offers. Their offers were closer to their reservation price or willingness-to-pay than those of TDB and RPR. As a result, the sellers in ERPR sold the object at cheaper prices. Future study should investigate how to reduce the unfairness resulting from the information provided in the ERPR mechanism.

## 7. Conclusion

Two new mechanisms (RPR and ERPR) were proposed to support online negotiations by asking negotiators to report their reservation price or willingness-to-pay to the NSS. In the RPR mechanism, negotiators should report their reservation price or willingness-topay to the NSS at the start of a negotiation. Negotiations would be initiated only when a positive bargaining zone was detected by the NSS. The ERPR mechanism provided negotiators with information on how far their bids were from the acceptable range before delivering this bid information to the negotiation partners.

An analytical model was developed to <sup>fi</sup>nd the equilibrium points and assess the performance of the mechanisms. Under the assumption of uniformly distributed reservation prices or willingness-to-pay and risk aversion, the agents were shown to have incentives to reveal their actual reservation price or willingness-to-pay to the NSS. When the agents did not reveal the truth, higher back-dragging costs (resulting from more rounds) led to smaller pro<sup>fi</sup>ts. The RPR mechanism was found to be more ef<sup>fi</sup>cient than the traditional free bargaining system in that negotiators in RPR achieved higher social welfare than those in TDB. By the same token, the ERPR mechanism was more ef<sup>fi</sup>cient than the RPR mechanism.

In our lab experiment, the average social welfare level generated by the three mechanisms was ordered as expected in our analytical model. In addition, negotiators were more honest in the high back-dragging cost conditions rather than in the low back-dragging cost conditions. We found an interesting phenomenon in terms of fairness, which was not considered in our analytical model. That is, the ERPR mechanism was less favorable to the initiators of the negotiation compared with the followers. The advice provided by the ERPR system discouraged the initiator from opening the negotiation with an extreme offer. As a result, the agreed price was favorable to the follower. In sum, the ERPR mechanism resulted in an issue of fairness between the initiator and the follower, even though higher levels of social welfare were engendered compared with the RPR mechanism.

We conclude that the RPR mechanism helped negotiators achieve better performance levels compared with the traditional TDB mechanism. Therefore, the RPR or ERPR negotiation support system is recommended when designing an online negotiation mechanism. The introduction of the RPR and ERPR mechanisms would be revolutionary for the existing e-business trading mechanisms. The RPR and ERPR mechanisms could be used successfully for electronic negotiations where trusted third parties (e.g., e-marketplaces and intermediaries) exist. Established e-commerce sites or e-marketplaces may introduce

[1] A. Barua, C.H. Kriebel, T. Mukhopadhyay, MIS and information economics: augmenting rich descriptions with analytical rigor in information systems design, Proceedings of 10th International Conference on Information Systems, Boston, 1989.

the RPR/ERPR mechanisms as an option for their customers who are willing to report their reservation price or willingness-to-pay in order to <sup>fi</sup>nd a more reasonable bargaining partner.

However, for wider application of this study, assumptions of the analytical model need to be eased in order to represent more general cases, such as arbitrary reservation price distribution cases and risk neutral or risk seeking cases. In a future study, we plan to consider the various levels of agent risk preferences and further factors. Also, further experiments on fairness and truth revelation with different conditions are expected to reveal more detailed suggestions on NSS design.

## Acknowledgements

The authors would like to thank the reviewers and editors for their helpful comments and suggestions. Byungjoon Yoo thanks Management Research Center at Seoul National University College of Business Administration for grant funding. Jinbae Kim and Seungwoo Kwon appreciate the <sup>fi</sup>nancial support of a Korea University Grant. This research was partially supported by the Natural Science Foundation of China (NSFC Project Number: 70471027, 70801059), and the China Postdoctoral Science Foundation for Wei Shang.

## Appendix A

## Summary of notations

Notations Description $\overline { { \mathrm { P } _ { \mathrm { S } } } }$ The bidding price of seller in t (Endogenous variable) $\mathrm { { P _ { B } } }$ The bidding price of buyer in t (Endogenous variable) $\mathtt { R } _ { \mathtt { S } }$ The reservation price of seller (Exogenous variable) $\mathtt { R _ { B } }$ The buyer's willingness-to-pay (Exogenous variable) $\Delta \mathrm { R } _ { S }$ The false report amount (Endogenous variable) $\mathrm { I f } \ \Delta \mathrm { R } _ { S } { = } 0 ,$ , it means a seller truthfully reports the reservation price $\Delta \mathrm { R _ { B } }$ The false report amount (Endogenous variable) $\mathrm { I f } \Delta \mathrm { R _ { B } } { = } 0 ,$ it means a buyer truthfully reports the willingness-to-pay for item ${ \sf C } _ { \sf S }$ The back-dragging cost of seller (Exogenous variable) $C _ { \mathrm { B } }$ The back-dragging cost of buyer (Exogenous variable) $\mathrm { P _ { m a x } }$ The maximum price for the item in the market (Exogenous variable) $\mathrm { P _ { m i n } }$ The minimum price for item in the market. (Exogenous variable) $\mathrm { E R s }$ The expected value of seller's reservation price $\mathrm { E R _ { B } }$ The expected value of buyer's reservation price α The coef<sup>fi</sup>cient of risk preferences EP The expected <sup>fi</sup>nal deal price EU<sup>t</sup> The seller's expected utility in t EU<sub>B</sub><sup>t</sup> The buyer's expected utility in t

## References

[2] T. Bui, Building DSS for negotiators: a three-step design process, Proceedings of the 25th Hawaii International Conference on System Sciences, Hawaii, 1992.

[3] T. Bui, M.F. Shakun, Negotiation processes, evolutionary systems design, and negotiator, Group Decision and Negotiation 5 (4-6) (1996).

[4] C. Cheng, C.H. Chan, K. Lin, Intelligent agents for e-marketplace: negotiation with issue trade-offs by fuzzy inference systems, Decision Support Systems 42 (2006).

[5] D.K.W. Chiu, S.C. Cheung, P.C.K. Hung, S.Y.Y. Chiu, A.K.K. Chung, Developing e-Negotiation support with a meta-modeling approach in a web services environment, Decision Support Systems 40 (2005).

[6] P. Cramton, Strategic delay in bargaining with two-sided uncertainty, Review of Economic Studies 59 (1) (1992).

[7] Q. Dai, R.J. Kauffman, Business models for Internet-based E-procurement systems and B2B electronic markets: an exploratory assessment, Proceedings of the 34th Hawaji International Conference on System Sciences. 2001.

[8] S.J. Grossman, M. Perry, Sequential bargaining with one-sided incomplete information, Journal of Economic Theory 39 (1) (1986).

[9] M.A. Neale, G.B. Northcraft, Behavioral negotiation theory — a framework of conceptualizing dynamic bargaining, Research in Organizational Behavior 13 (1991).

[10] H. Raiffa, The Art and Science of Negotiation,Harvard University Press, Cambridge,1982.

[11] A. Rubinstein, A bargaining model with incomplete information about time preference, Econometrica 53 (1985).

[12] M. Schoop, A. Jertila, T. List, Negoisst: a negotiation support system for electronic business-to-business negotiations in e-commerce, Data and Knowledge Engineering 47 (3) (2003).

[13] J. Von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, Princeton University Press, 1953.

[14] W. Wang, H. Zoltán, A.B. Whinston, Shill bidding in multi-round online auctions— system sciences, Proceedings of the 35th Hawaii International Conference on System Sciences. 2002

[15] D. Wei, Electronic Business-Oriented Negotiation Support System (PhD dissertation, Harbin Institute of Technology, 2001).

![](/api/attachments/FG3UPVF4/fulltext/images/9d7e658045d1d47b217635ea81c9386656f3fc28404ac4d4a77f09e98b512157.jpg)

Kwon, Seungwoo is an associate professor of management at Korea University Business School. He received his Ph.D. in Organizational Behavior and Theory from Carnegie Mellon University. His articles have been published in journals such as Journal of Personality and Social Psychology, Journal of Applied Psychology and Human Resource Management. He received outstanding article award from the International Association for Con<sup>fl</sup>ict Management (2002) and was nominated for the best paper based on dissertation (Con<sup>fl</sup>ict Management Division) at the Academy of Management conference (2002). His current research interests include con<sup>fl</sup>ict management, negotiation, compensation, and justice in organizations.

![](/api/attachments/FG3UPVF4/fulltext/images/52ed8838f18803954504e60818f422f785b49a7d777e55c1845fafd29385d64b.jpg)

Yoo, Byungjoon is working for Graduate School of Business at Seoul National University as an assistant professor. Before he joined Seoul National University, he worked at Korea University and Hong Kong University of Science and Technology. He received a Ph.D. in Information Systems from Carnegie Mellon University. His research interests are on B2B e-commerce, online auctions and pricing strategies of digital goods such as software products and online games. He has published on these topics in journals such as Management Science, Journal of Management Information Systems, and Journal of Organizational Computing and Electronic Commerce. He has consulting experiences with

Korea Stock Exchange, Korea Game Industry Agency and other companies.

![](/api/attachments/FG3UPVF4/fulltext/images/8b4bf2d3dbeda7f18f6c391ad8d82fb4d8b24d8919a69016d0994a6d7f66ebdd.jpg)

Kim, Jinbae is a professor at Korea University Business School. Before he joined Korea University, he had been an assistant professor at Boston University. He received an MBA from the University of Chicago and a Ph.D. from Carnegie Mellon University. His research interests are on empirical tests of the agency model, performance-reward relation and corporate governance. He has published various papers in journals including Accounting Research Journal, Journal of Accounting and Auditing Research. Asia-Pacific Journal of Accounting and Economics and Asia-Paci<sup>fi</sup>c Management Accounting Journal.

![](/api/attachments/FG3UPVF4/fulltext/images/57eac000364364d85bb7021e5a5da839eff247f9d1ceb9da8ff24056c5791f15.jpg)

Shang, Wei is now a postdoctoral researcher at Institute of Systems Science, Academy of Mathematics and Systems Science, Chinese Academy of Sciences. She got her Ph.D. Degree from Harbin Institute of Technology and visited Korea University for a year as a visiting student. Her research interests include Negotiation Support Systems, Group Decision Making, Macroeconomics Analysis Systems, and Software Engineering She has published papers in major conferences and journals and participated in several national supported research projects related to Negotiations and Group Decision-Making Systems

![](/api/attachments/FG3UPVF4/fulltext/images/44d3849b8ebe9714dfc0d88ea01da654c57250cb96a0f6d49655fd73ed2af219.jpg)

Lee, Gunwoong is a Ph.D. student at Krannert School of Management at Purdue University. Before his Ph.D. program, he worked at Korea Association of Game Industry as a research fellow. His research focuses on online reputation systems and information economics. He has a MSc in Management Information Systems, and a BSc in Computer Science from Korea University.
