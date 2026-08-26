---
otero_id: 5128
otero_key: "XGNRH6W6"
title: "A single issue negotiation model for agents bargaining in dynamic electronic markets"
authors: "Fenghui Ren; Minjie Zhang"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.020"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A single issue negotiation model for agents bargaining in dynamic electronic markets

Fenghui Ren ⁎, Minjie Zhang

School of Computer Science and Software Engineering, University of Wollongong, Australia

a r t i c l e i n f o

Available online 5 June 2013

Keywords: Agent negotiation Agent bargain Electronic marketplace Dynamic negotiation environment

## a b s t r a c t

Electronic Commerce has been a signi<sup>fi</sup>cant commercial phenomenon in recent years, and brings more bene-<sup>fi</sup>ts to people by comparison with the traditional market in aspects of cost, convenience and ef<sup>fi</sup>ciency. The use of agent technology in e-markets for automatic bargains between buyers and sellers further increases the advantages of the e-market. However, most of existing agent-based bargain strategies assume a <sup>fi</sup>xed number of negotiation participants, which may fail to enlarge agents' pro<sup>fi</sup>ts or to lead a bargain to a success when these strategies are applied in the e-market-based agent negotiations straightway. Problems such as unexpected changes on negotiation participants, possible changes on agents' expected negotiation outcomes, and unexpected switching in-between the buyer's and seller's markets need to be considered in order to guarantee agents' bene<sup>fi</sup>ts and the success of negotiations. This paper proposes a novel agent negotiation model to help agents to perform a more effective bargain in e-markets by considering the objectiveness of the e-markets and the subjectiveness of the agents. The e-market situation by considering the number of bargain participants is proposed to re<sup>fl</sup>ect the objectiveness of the e-markets, and the agents' negotiation attitudes is introduced to indicate agents' responses to possible changes of the e-markets. Both the objectiveness of e-markets and the subjectiveness of agents are taken into account in negotiation procedures such as offer evaluation, negotiation decision making and counter-offer generation. Experimental results on a simulated e-market illustrate the bene<sup>fi</sup>ts and ef<sup>fi</sup>ciency of the proposed negotiation model in handling agents bargain problem in complex and dynamic e-market environments.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Electronic market (e-market) has changed signi<sup>fi</sup>cantly the traditional way of doing business in recent years and has become a very important commercial phenomenon [2]. By comparing with the traditional marketplaces, the bene<sup>fi</sup>ts of e-market are the lower operation cost and higher ef<sup>fi</sup>ciency. By trading through an e-market, merchants can save their budgets on business maintenance by avoiding physical shops and shop assistants. Also, shoppers do not need to visit shops in person which can save costs on traf<sup>fi</sup>c and time. The e-market is also more ef<sup>fi</sup>cient in reaching deals than the traditional marketplace. That is because all participants of an e-market can collect information about their concerned items and communicate with potential trading partners in a timely manner. Furthermore, the usage of autonomous agents in e-market trading makes the e-market more ef<sup>fi</sup>cient [24,29]. By employing autonomous agents, participants of an e-market do not need to perform the repeated work, such as the information retrieval and the price bargaining, but just let the agents know of their preferences and expectations during a trading [20,22]. Then the agents can perform the automatic item searching and price bargaining with the potential trading partners, and reach a reasonable agreement according to the participants' expectations. Usually, the agent negotiation is employed by agents for bargaining.

Agent negotiation has been an important research topic in agent and multi-agent systems for many years. The literature indicates achievements from researchers. Faratin et al. [7,28] proposed a well-known negotiation decision function by considering time constraints and de<sup>fi</sup>ned a number of strategies and tactics for different negotiation purposes in service oriented applications. Lai et al. [17,18] employed a third party, i.e., a non-biased mediator, into agent negotiation to help agents to solve the decision making problem caused by incomplete information on negotiation opponents, so as to lead the negotiation to the Pareto optimality. Fatima et al. [8–10] also studied negotiation models in incomplete information settings in different negotiation scenarios and illustrated equilibrium solutions in different negotiation agendas and procedures.

Besides the above works on static negotiation environments, some works on dynamic negotiation environments have also been developed. Fatima et al. [11] proposed several negotiation strategies to help agents to achieve approximately optimal outcomes in dynamic negotiation environments through improving computational ef<sup>fi</sup>ciency and a little bit of loss in negotiation equilibrium. Mason et al. [21] proposed price prediction strategies to help agents to estimate possible changes in markets, and the consequences of these changes. The authors demonstrated that the proposed prediction strategies can help agents to improve their pro<sup>fi</sup>ts in dynamic markets. Kurbel et al.

[16] introduced a model with fuzzy constraints on an e-job market. A negotiation protocol and several negotiation strategies were proposed to address the challenges of multiple party negotiations in complex e-markets. Furthermore, Li et al. [19] proposed a con<sup>fi</sup>dence-based negotiation model for negotiations in complex environments. Agents would keep the con<sup>fi</sup>dence information about the negotiation opponents, and apply different strategies and/or procedures in negotiating with opponents in different con<sup>fi</sup>dence levels.

Although the above related works have reached great achievements in agent negotiation, challenges of e-market negotiation still exist. For example, most of existing agent negotiation models require agents to prede<sup>fi</sup>ne reservation offers on negotiation outcomes before negotiations start, and agents' actions during a negotiation are decided mostly by the reservation offers [4]. However, according to our studies on several models of e-markets [5,6,23], and the real world e-markets, it is noticed that in an open and dynamic e-market, changes of a market situation such as the number of sellers and buyers may impact agents' expectations on negotiation outcomes. In a dynamic e-market, agents do not necessarily need to <sup>fi</sup>x their reservation offers throughout a negotiation, but may modify them during a negotiation dynamically when the e-market situation changes. We further noticed that if agents <sup>fi</sup>x reservation offers in dynamic e-markets, their pro<sup>fi</sup>ts might be damaged. The reasons are: (1) agents may have no clear idea about e-market situations before a negotiation, and the reservation offer is usually given by agents without considering the e-market situations; and (2) the evaluation results based on the <sup>fi</sup>xed reservation offers may fail in indicating an item's real value in different market situations. For example, if an inexperienced house purchaser prede<sup>fi</sup>nes his/her reservation offer without careful investigation of the real-estate market, it may lead the purchaser to two possible disadvantageous outcomes, i.e., (i) the house purchaser may undervalue properties' values in the market and not accept any price higher than the reservation offer, so the potential purchaser may not <sup>fi</sup>nd any satis<sup>fi</sup>ed property in the market and negotiations between all property sellers might fail; and (ii) the house purchaser may overvalue properties' values in the market. Even though the purchaser can <sup>fi</sup>nally <sup>fi</sup>nd a property in the market, his/her pro<sup>fi</sup>t will be damaged as well. In order to solve such an issue in dynamic e-markets by consid ering the relationship between demand and supply, we propose a negotiation model in this paper to dynamically modify agents' negotiation behaviors based on changes of the number of an e-market's participants and agent's motivation on accomplishment of a negotiation. The work presented in this paper is based on our previous work in [25]. In this paper, we extend the modeling approach of an e-market to provide a better offer evaluation function and counter-offer generation function in an open and dynamic e-market. Also, we extend the experiment from <sup>fi</sup>ve agents to <sup>fi</sup>fty agents, and provide much more explanations on the experimental results.

The rest of this paper is organized as follows. Section 2 introduces the proposed negotiation model, which includes an offer evaluation approach, a counter-offer generation approach and a negotiation protocol. Section 3 illustrates experimental results of the proposed model in different market situations. Section 4 compares the proposed model with some related works, and Section 5 concludes the paper and introduces our future work.

## 2. Desire-based negotiation model

In this section, we introduce a negotiation model for agents bargaining in open and dynamic e-markets. The proposed model can capture the dynamic changes of e-markets, and allows agents to modify their negotiation behaviors based on their desires in completing a negotiation. Because agents' desires play as an important factor in deciding agents' negotiation behaviors, we name the model as the desire-based negotiation model.

## 2.1. Principle

Through our studies, we notice that in the real world, although people can prede<sup>fi</sup>ne reservation offers in advance, in most cases it is not necessary for them to insist on their reservation offers throughout the negotiation [27]. For example, in a dynamic market, a hesitant buyer may look forward to gain more bene<sup>fi</sup>t when he/she notices that his/her original expectation can be satis<sup>fi</sup>ed easily by most sellers. On the other hand, a ‘rushing’ buyer may accept an offer even if the offer is worse than his/her reservation offers. However, most existing agent negotiation models do not take these situations into account. The motivation of this research is to introduce a sophisticated negotiation model to advice agents how to modify their negotiation behaviors in open and dynamic negotiation environments.

In our proposed negotiation model, agents do not need to prede<sup>fi</sup>ne their expectations on negotiation outcomes as the reservation offers, because agents' expectations may be changed when the market situation changes. Contrary to that, agents express their eagerness to complete the negotiations as a desire (∈[0,1]), and use the desire to make negotiation decisions. The higher the desire, the more eager the agent wants to complete the negotiation. In comparison with the reservation offer, the desire re<sup>fl</sup>ects an agent's eagerness to complete a negotiation and has the following advantages: (1) agents' desires are independent on the e-market situations, but the reservation offer selection needs to consider the e-market situations. Therefore, the desire is more suitable for a dynamic e-market; (2) it is more practical for agents to prede<sup>fi</sup>ne a desire to express their eagerness to complete a negotiation than to prede<sup>fi</sup>ne an expected bene<sup>fi</sup>t when the bene<sup>fi</sup>t could be greatly impacted by the dynamics of an e-market; and (3) the negotiation process in an e-market is usually completed in a short time, and the agents almost have no time to update their expectations on negotiation outcome manually, the use of desire can solve this problem because agents' eagerness to complete a negotiation can easily be decided by agents in advance and do not change during the negotiation.

In general, an urgent agent will have a high desire to complete a negotiation, but a hesitant agent will have a low desire to complete a negotiation. During the negotiation, when the e-market situation changes, the actual evaluation on the opponent's offer and the counter-offer generation are also modi<sup>fi</sup>ed by taking the e-market changes into account, and the desire plays as a criterion (i.e., independent on e-market situations) to help the agent to make decision on actions from possible options. For example, once a buyer agent decides its desire to complete the negotiation with car seller agents, without changing the desire, the buyer agent can automatically modify its negotiation behaviors when the market situation changes, i.e., the buyer agent will give more concession to the seller agents and accept a seller's price when the market is the seller's market. However, when the market becomes the buyer's market, the buyer agent will give less concession and may reject the same offer. That is because when the market situation changes, the previous attractive offers may become not attractive anymore, and the proposed model can take this dynamic changing into account. In the following subsections, the proposed model will be introduced in aspects of offer evaluation, counter-offer generation, and negotiation behavior decision.

## 2.2. Offer evaluation

In this subsection, we introduce an offer evaluation approach by considering both e-markets' and agents' situations. The consideration on e-markets' situations includes the number of buyers, the number of sellers and the agent's role; while the consideration on agents situations includes agents' initial offers, and the subjective attitude on the e-market change.

## 2.2.1. Consideration of market situation

Before we introduce the offer evaluation approach, we de<sup>fi</sup>ne some notations. Let tuple $< s , c , o _ { i n i } , d , \tau , \alpha , \beta , \lambda >$ be an indicator employed by agents during negotiation, where $s \ ( s > 0 )$ denotes the number of sellers, c $( c > 0 )$ denotes the number of buyers, $o _ { i n i }$ denotes the agent's initial offer, and d $( 0 \leq d \leq 1 )$ denotes the agent's desire. When $d = 0 ,$ it indicates that the agent is not interested in completing a negotiation, and when $d = 1$ , it indicates that the agent must complete a negotiation and reach an agreement. τ is the negotiation deadline. α denotes the agent's role in the negotiation, where $\alpha = - 1$ for buyers and $\alpha = 1$ for sellers. $\beta$ denotes the agent's attitude on the e-market changes and λ indicates the agent's bargaining strategy. In this paper, we only consider the single issue negotiation in an e-market and assume that the quantity of the negotiated item between a buyer agent and a seller agent is one. However, the number of buyers and sellers could be more than one and dynamically changes.

Firstly, by considering the number of buyer and seller agents in an e-market, the relationship between supply and demand of the e-market at a certain moment is represented as follows:

$$
\Phi (s, c, \alpha) = \frac {c - s}{c + s} \times \alpha .\tag{1}
$$

The range of Formula (1) is in-between $[ - 1 , 1 ]$ , and represents the status of an e-market. Intuitively, $[ \mathbf { f } \mathbf { 0 } < \mathbf { \Phi } \leq 1$ , the e-market is a bene<sup>fi</sup>cial market $( \mathrm { i . e . } ,$ , agents whose role is α will have advantages in such a market); $\mathrm { i f } - 1 \le \Phi < 0 ,$ the e-market is an inferior market (i.e., agents whose role is α will have disadvantages); if $\Phi = 0 ,$ the e-market is an equitable market (i.e., all agents do not have any advantages or disadvantages). Objectively, Formula (1) represents the relationship between supply and demand in an e-market at a certain moment. For agents in different roles, their market situations are also different. For example, when buyers are more than sellers $( c > s )$ , for sellers $( \alpha = 1 )$ , because $\Phi ( s , c , \alpha ) > 0 \quad$ , the market is bene<sup>fi</sup>cial to sellers. But for buyers $( \alpha = - 1 )$ , because $\Phi ( s , c , \alpha ) < 0$ , the market is inferior.

Objectively, Eq. (1) represents the relationship between supply and demand in the negotiation environment at a certain moment. However, even for the same e-market situation, agents may also have their own considerations based on individual judgments. Therefore, we generate a graph (see Fig. 1) to indicate the relationship between an e-market's situation and an agent's response. In Fig. 1, the x-axis represents situations of the e-market (Φ), and the y-axis indicates the agent's response. In general, when the e-market situation shifts away from the equitable state to the bene<sup>fi</sup>cial or the inferior state, the agent's response will move from calmness to vehemence. In detail, it can be seen that agents may have three typical attitudes in response to changes of the e-market.

• Cautious $( \beta > 1 )$ : when the e-market situation shifts away from equitable to bene<sup>fi</sup>cial or inferior, the agent's response is calm when changes of the e-market are not signi<sup>fi</sup>cant. However, when the changes of the e-market become evident, the agent's response becomes more vehement.

• Acuminous $( 1 > \beta > 0 )$ : when the e-market situation shifts away from equitable to bene<sup>fi</sup>cial or inferior, the agent performs sensitively even though the change in the environment is not obvious. However, the agent must control the strength of its response due to objective reasons such as the agent cannot make further concession anymore.

• Normal $( \beta = 1 )$ : when the e-market situation shifts away from equitable to bene<sup>fi</sup>cial or inferior, the agent's response is also moved from calmness to vehemence reposefully.

Even though the above three typical responses cannot cover all possible situations of an agent's response on e-market changes, the types of responses can still be expressed. Based on the above description, we generate the following mapping function from an e-market's state to an agent's response:

![](/api/attachments/XGNRH6W6/fulltext/images/a79fd3c32801a3d38e4369542018a3b37c8c7afc73b722e3bea6060bdf94a0ab.jpg)  
Fig. 1. Negotiants' responses to markets' situations

$$
\Psi (s, c, \alpha , \beta) = \left\{ \begin{array}{l l} \Phi (s, c, \alpha) ^ {\beta}, & \Phi (s, c, \alpha) \geq 0 \\ - [ - \Phi (s, c, \alpha) ] ^ {\beta}, & \Phi (s, c, \alpha) <   0 \end{array} \right.\tag{2}
$$

where $\Psi \in [ - 1 , 1 ] , s , c$ and α are de<sup>fi</sup>ned in Eq. (1). The result of Ψ indicates an agent's individual judgment about the e-market's situation. Different agents may have different judgments on the same e-market. When Ψ $\mathrm { ~  ~ \cdot ~ } > 0 ,$ , an agent estimates the e-market in a bene<sup>fi</sup>cial state, when $\Psi = 0 ,$ , an agent estimates the e-market in an equitable state, and when $\Psi < 0 ,$ an agent estimates the e-market in an inferior state.

However, because Ψ only takes into account an e-market situation, we also propose the following function to consider the agent's individual situation in the offer evaluation

## 2.2.2. Consideration of negotiant's situation

Let o<sub>l</sub> denote an offer from an opponent and $o _ { i n i }$ denote an agent's initial offer, then o is <sup>fi</sup>rstly evaluated as a utility by the agent as follows:

$$
\Lambda (o _ {l}, o _ {i n i}, \gamma) = \mathbf {t h} \left(\frac {o _ {l} - o _ {i n i}}{o _ {i n i}} \times \gamma\right) + 1\tag{3}
$$

where $\gamma = - 1$ indicates that the agent prefers a lower value than the initial offer, $\gamma = 1$ indicates that the agent prefers a greater value than the initial offer, and th(x) is de<sup>fi</sup>ned as follow.

$$
\mathbf {t h} (x) = \frac {e ^ {x} - e ^ {- x}}{e ^ {x} + e ^ {- x}}\tag{4}
$$

where $\begin{array} { r } { \mathbf { t h } ( x ) = \frac { e ^ { x } - e ^ { - x } } { e ^ { x } + e ^ { - x } } } \end{array}$ is the Hyperbolic Tangent Function $( { \bf t h } ( 0 ) = 0$ $\mathbf { t h } ( x )$ <sup>þ</sup>limits to 1 when x approaches in<sup>fi</sup>nite, and th(x) limits to −1 when x approaches negative in<sup>fi</sup>nite). The reason for selecting the Hyperbolic Tangent Function to map an offer to a utility value is that it can effectively map any value to a value in-between the range [ 1, 1], and the mapping function also accords with human's nonlinear attitude on value changes.

The result of Eq. (3) $( \Lambda { \in } ( 0 , 2 ) )$ indicates how a negotiant's initial offer is satis<sup>fi</sup>ed by the opponent's offer $o _ { l } .$ For example, if the negotiant plays as a buyer $( \mathrm { i } . \mathrm { e } . , \alpha = - 1 )$ , when $o _ { l } = o _ { i n i } ,$ then $\Lambda = 1$ . It means that the buyer's original expectation is fully satis<sup>fi</sup>ed. When $o _ { l } > 0 _ { i n i }$ then $0 \leq \Lambda < 1$ , it indicates that the buyer's original expectation can only be partially achieved. And when $o _ { l } < o _ { i n i }$ then $1 < \Lambda < 2 ,$ , it implies that the buyer's expectation is overachieved. It must be pointed out that the traditional offer evaluation approach [12] actually normalizes a given offer within interval [0, 1] by using the initial offer and the reservation offer. However, our evaluation approach does not use the reservation offer, because agents may dynamically change their reservations when the e-market situation changes. Such a feature also accords with a human's habit in many real-world situations.

## 2.2.3. Considerations of both market and negotiant's situation

Because Eq. (3) only evaluates an offer based on an agent's initial offer but does not take the e-market situation into account, the evaluation result may not accord with the market. Therefore, we modify the offer evaluation function by considering both market and negotiant situations as follows:

$$
\Theta (o _ {l}, s, c, o _ {i n i}, \alpha , \beta , \gamma) = \Lambda (o _ {l}, o _ {i n i}, \gamma) * (1 - \Psi (s, c, \alpha , \beta))\tag{5}
$$

where the result of $\operatorname { E q . }$ (5) indicates the negotiant's utility by accepting the offer o in a certain market. If it is an equitable market $( \Psi = 0$ and $\Theta = \Lambda )$ , then the offer $o _ { l }$ is evaluated unbiasedly. If it is in a bene<sup>fi</sup>cial market $( 0 < \Psi < 1$ and $\Theta < \Lambda )$ , then the offer o is undervalued. And if it is in an inferior market $( - 1 < \Psi < 0$ and $\Theta > \Lambda )$ , then the offer $o _ { l }$ is overvalued.

For example, a potential car purchaser's initial offer is \$6000 and the seller's offer price is \$6500. Without consideration of the market situation, the buyer's evaluation result on the offer \$6500 is $\Lambda = 0 . 9 2$ , i.e., the buyer is 92% satis<sup>fi</sup>ed with the seller's offer. However, when taking the market situation into account, results might be different. If the market is a buyer's market (for example, 5 buyers and 10 sellers, then $\Psi =$ 0.33), the buyer's satisfaction on the offer \$6500 will decrease to 61% and the buyer may reject the offer. That is because in the buyer's market, a buyer has opportunities to make greater pro<sup>fi</sup>ts. On the other hand, if the market is a sellers' market (for example, 10 buyers and 5 sellers, then $\Psi = - 0 . 3 3 )$ ), the buyer's satisfaction on the offer \$6500 will increase to 122%. It indicates that the buyer is very happy about the offer \$6500 in a disadvantageous market and may accept the offer. During negotiation, desire-based agents will make decisions on their actions based on the result in Eq. (5) and their desire (see Section 2.4 for details). In the following, we simplify the expression in Eq. (5) to $\Theta ( o _ { l } )$

## 2.3. Counter-offer generation

In the previous subsection, we introduce the approach to evaluate opponent's offers by considering both the market's and the agent's situations. In this subsection, we introduce a counter-offer generation approach. The counter-offer generation approach also takes both the market's and the agent's situations into account. Before we introduce this approach, we de<sup>fi</sup>ne some notations.

Let set $\vec { O } _ { t }$ denote all offers that an agent received from its opponents in round $t ,$ o<sup>b</sup> denotes the ‘best’ offer in $\vec { O } _ { t }$ (i.e., the offer brings the highest pro<sup>fi</sup>t to the agent, $o _ { t } ^ { b } = \arg \operatorname* { m a x } _ { o _ { t } \in \vec { O } _ { t } } \{ \Theta ( o _ { t } , s , c , o _ { i n i } , \alpha , \beta , \gamma ) \} )$ $o _ { t } ^ { w }$ denotes the ‘worst’ offer in $\vec { O } _ { t }$ (i.e., the offer brings the lowest pro<sup>fi</sup>t to the agent, $o _ { t } ^ { b } = \arg \operatorname* { m i n } _ { o _ { t } \in \vec { O } _ { t } } \{ \Theta ( o _ { t } , s , c , o _ { i n i } , \alpha , \beta , \gamma ) \} ,$ , o<sup>m</sup> denotes the average of $\begin{array} { r } { \cdot \overrightarrow { O } _ { t } \left( \mathrm { i . e . , } o _ { t } ^ { m } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } o _ { t } ^ { i } \right. } \end{array}$ and N is the size of set $\vec { ( } _ { } , \vec { } _ { } ) , \vec { } _ { } ^ { b } ,$ denotes <sup>¼</sup>the estimated best offer in the next round $t ^ { \prime } , c o _ { t }$ denotes the agent's latest counter-offer, and $c o _ { t }$ <sub>′</sub> denotes the agent's counter-offer for the next round. Then if an agent plays as a buyer, one possible situation of the counter-offer generation procedure in the negotiation round t is illustrated in Fig. 2.

In Fig. 2, the x-axis stands for prices and the y-axis stands for the occurrence density on each price. The solid curve indicates the distribution of set $\dot { O _ { t } }$ in the round $t ,$ which may differ from case to case, and the dotted line is the estimated distribution of set $\dot { 0 }$ in the next round. We make the assumption that the shape of the distribution curve of set $\smash { \dot { O } } _ { t }$ is similar to $O _ { t } s ,$ but just the domain is changed.

![](/api/attachments/XGNRH6W6/fulltext/images/9156939715d6324aea237f2500c3c3cb9615b667570edf482dd2c0ae80fca47f.jpg)  
Fig. 2. Counter-offer generation.

Because the agent plays as a buyer, so the market represented in Fig. 2 is a bene<sup>fi</sup>cial market. In a bene<sup>fi</sup>cial market, for buyers, $\dot { O }$ is estimated to be smaller than $\dot { O _ { t } }$ on average. The distance between the current counter-offer $c o _ { t }$ and the estimated ‘best’ offer $o _ { t ^ { \prime } } ^ { b }$ in the next round is the bargaining area. The new counter-offer $c o _ { t ^ { \prime } }$ is generated within this area according to the agent's negotiation strategy, the e-market's situation, and the time constraint.

Firstly, we estimate the ‘best’ offer $o _ { t ^ { \prime } } ^ { b }$ in the next round t′ by considering both the distribution of $\dot { O } _ { t }$ and the e-market's situation as follows:

$$
o _ {t ^ {\prime}} ^ {b} = o _ {t} ^ {b} + \Psi (s, c, \alpha , \beta) \times 3 \sqrt {D (\vec {O} _ {t})} \times \gamma\tag{6}
$$

$$
D \left(\vec {O} _ {t}\right) = \sum_ {i = 1} ^ {N} \left(o _ {t, i} - E \left(\vec {O} _ {t}\right)\right) ^ {2} p _ {i}\tag{7}
$$

where $D \Big ( \vec { O } _ { t } \Big )$ indicates the variance of $\vec { O } _ { t } , \gamma = - 1$ for issues which an agent prefers a lower value and $\gamma = 1$ for issues which an agent prefers a greater value, $E { \bigg ( } { \vec { O } } _ { t } { \bigg ) }$ indicates the mathematical expectation of $\vec { O } _ { t } , p _ { i }$ indicates the distribution of $o _ { t , i }$ and $\Psi ( s , c , \alpha , \beta )$ indicates the agent's response to the e-market's situation. We set the maximal possible change of the expected best offer to $3 \sqrt { D \Big ( \vec { O } _ { t } \Big ) }$ because 99% of observed value locates in interval $\left[ - 3 \sqrt { D \Big ( \vec { O } _ { t } \Big ) } , ~ 3 \sqrt { D \Big ( \vec { O } _ { t } \Big ) } \right]$ in mathematics. Usually, when the distribution of $\vec { O } _ { t }$ is a Gaussian distribution, then $\begin{array} { r } { E \bigg ( \vec { O } _ { t } \bigg ) = o _ { t } ^ { m } , p _ { i } = \frac { 1 } { N } } \end{array}$ and Eq. (7) is speci<sup>fi</sup>ed as:

$$
D \left(\vec {O} _ {t}\right) = \frac {\sum_ {i = 1} ^ {N} \left(o _ {t , i} - o _ {t} ^ {m}\right) ^ {2}}{N}.\tag{8}
$$

Then the counter-offer $c o _ { t ^ { \prime } }$ <sub>′</sub> for the following negotiation round is generated as follows:

$$
c o _ {t ^ {\prime}} = \left\{ \begin{array}{l l} o _ {i n i}, & \text { when } t = 0, \\ c o _ {t} + \left(o _ {t ^ {\prime}} ^ {b} - c o _ {t}\right) \times \left(\frac {1}{\tau}\right) ^ {\lambda}, & \text { when } 0 <   t \leq \tau . \end{array} \right.\tag{9}
$$

where $o _ { i n i }$ is the agent's initial offer, $c o _ { t }$ is the agent's current counter-offer, $o _ { t ^ { \prime } } ^ { b }$ is the estimated ‘best’ offer in the next round, and we simply adopt parameter λ in Faratin et al.'s model [7] to represent the agent's bargaining strategies.

In Fig. 3, it can be seen that when the e-market becomes more bene<sup>fi</sup>cial to the buyer agent, it is possible that $o _ { t ^ { \prime } } ^ { b }$ bco and $c o _ { t ^ { ' } } { < } c o _ { t }$ . So in the desire-based negotiation model, we propose a decommitment mechanism which allows agents to reject previous offers if the offers are not formally accepted by any opponents. The reason that we propose such a mechanism is because in the desire-based negotiation model, both the offer evaluation approach and counter-offer generation approach are impacted by the e-market's situation. So when the e-market's situation changes, agents may change their considerations on both the offer evaluation procedure and the counter-offer generation procedure in order to gain more pro<sup>fi</sup>ts. For example, buyers may generate disadvantageous counter-offers when the e-market is inferior. However, when buyers notice that the e-market may become bene<sup>fi</sup>cial and if previous counter-offers are not accepted by any seller, buyers can reject the previous disadvantageous counter-offers and re-generate advantageous counter-offers in order to enlarge their pro<sup>fi</sup>ts. On the other hand, if sellers notice that the e-market may become inferior for them in advance, they may accept buyers' current offers in order to avoid losses in the future.

![](/api/attachments/XGNRH6W6/fulltext/images/d1561f5a2cfbfa5bb7c476e16ad2b78273a67ea1d3c224573fb852de700c2599.jpg)  
Fig. 3. Counter-offer generation.

Also, the e-market may become inferior for buyers. In Fig. 4, it can be seen that when a market is inferior for buyers, the estimated ‘best offer for the following round is worse than the ‘best’ offer in the round t, i.e. $o _ { t ^ { ' } } ^ { b } > o _ { t } ^ { b } .$ . During negotiations, if the new counter-offer in the round $\bar { t ^ { \prime } }$ can bring more pro<sup>fi</sup>ts to the agent than the ‘best’ offer in the current round $t , \mathrm { i . e . } \Theta ( c o _ { t ^ { \prime } } ) > \Theta \bigl ( o _ { t } ^ { b } \bigr )$ , the agent will keep <sup>ð Þ</sup>on bargaining with opponents and send out the new counter-offer $c o _ { t ^ { ' } }$ . However, if the new counter-offer is worse than the ‘best’ offer, i.e. $\Theta ( c o _ { t ^ { \prime } } ) { < } \Theta \bigl ( o _ { t } ^ { b } \bigr )$ , (see the case shown in Fig. 4), the agent will not send the new counter-offer $c o _ { t ^ { \prime } }$ , but make its <sup>fi</sup>nal decision about the negotiation based on the comparison between the ‘best’ offer $\left( o _ { t } ^ { b } \right)$ from opponents and the agent's desire (d). The detailed encounter rule of the desire-based negotiation model is introduced in the following subsection.

## 2.4. Negotiation protocol

Since both the offer generation approach and the counter-offer evaluation approach have some differences from the classic negotiation models [7,15,28], we propose a negotiation protocol for our desire-based negotiation model based on Rubinstein's alternating offers protocol [7] as follows.

![](/api/attachments/XGNRH6W6/fulltext/images/22f30096323368b5167d285b39548736613b1066e9d9bafc8c6d5388fbb9c442.jpg)  
Fig. 4. Counter-offer generation.

• Step 1 The agent assigns negotiation parameters, i.e., initial offer $\left( { { o } _ { i n i } } \right)$ desire $( d ) ,$ , negotiation deadline (τ), role in negotiation $( \alpha )$ , attitude on e-market's situation changes (β) and bargaining strategy (λ). The number of consumers (c) and suppliers (s) can be obtained from the e-market directly. Also the agent initializes t to 0 and $c o _ { t } t 0 o _ { i n i } .$

• Step 2 The agent broadcasts co to all opponents and waits for responses.

• Step 3 Once the agent gets responses, if any opponent accepts $c o _ { t } ,$ , the negotiation is completed. Otherwise, if $t > \tau ,$ the procedure goes on to Step 4; and ${ \mathrm { i f } } t \leq \tau ,$ , the procedure goes on to Step 5.

• Step 4 Because the agent does not have time for further bargaining, it has to make a <sup>fi</sup>nal decision on the ‘best’ offer $o _ { t } ^ { b }$ in the last round. The criterion of the decision making is the agent's desire. A higher desire indicates more eagerness to complete a negotiation, and the agent would like to make more concession in order to reach an agreement. To the contrary, a lower desire indicates less eagerness to complete a negotiation, and the agent would like to get more bene<sup>fi</sup>t from an agreement. Therefore, the comparison between the evaluation on the ‘best’ offer o<sup>b</sup> $\left( \Theta ( o _ { t } ^ { b } ) \right)$ and the agent's threshold on its pro<sup>fi</sup>t for a particular desire $( 1 - d )$ should be considered. If $\Theta ( o _ { t } ^ { b } ) ^ { 1 } \geq 1 - d ,$ the agent will accept o<sup>b</sup> and the negotiation is completed. Otherwise, the negotiation fails.

• Step 5 Because the agent still has time for further bargaining, so the agent will generate a new counter-offer $c o _ { t ^ { \prime } }$ for the next round. In this situation, the agent should compare its pro<sup>fi</sup>t from the ‘best’ offer o<sup>b</sup> $( \mathrm { i } . \mathsf { e } . , \Theta ( o _ { t } ^ { b } ) )$ , the pro<sup>fi</sup>t from its counter-offer co <sub>′</sub> $\left( \mathrm { i } . \mathbf { e } . , \Theta ( c o _ { t ^ { ' } } ) \right)$ , and its minimal acceptable pro<sup>fi</sup>t for desire $l \left( { \mathrm { i . e . , } } 1 - d \right)$ <sup>ð Þ</sup>before making the decision. For details, if max $\left( \Theta \big ( o _ { t } ^ { b } \big ) , \Theta ( c o _ { t ^ { \prime } } ) , 1 - d \right) = \Theta \big ( o _ { t } ^ { b } \big )$ , the offer o<sup>b</sup> will <sup>ð Þ ¼</sup>be accepted by the agent and the negotiation is completed. If max $\begin{array} { r } { ( \Theta ( o _ { t } ^ { b } ) , \Theta ( c o _ { t ^ { \prime } } ) , 1 - d ) = 1 - d , } \end{array}$ the agent will leave off the proce-<sup>ð Þ Þ ¼</sup>dure and the negotiation fails. If max $( \Theta ( o _ { t } ^ { b } ) , \Theta ( c o _ { t ^ { \prime } } ) , 1 - d ) = \Theta ( c o _ { t ^ { \prime } } )$ the procedure goes on to Step 6.

• Step 6 The agent updates t to $t ^ { \prime } ,$ co to $c o _ { t ^ { \prime } }$ and parameters $c ,$ and s according to the current market situation, then the procedure goes back to Step 2.

Based on the above procedure, the agent's action in round t is de-<sup>fi</sup>ned as follows:

$$
\Omega (t) = \left\{ \begin{array}{l} \mathbf {Q u i t}, t \geq \tau \wedge \Theta \left(o _ {t} ^ {b}\right) <   1 - d \mathbf {o r} \\ t <   \tau \wedge \max \left(\Theta \left(o _ {t} ^ {b}\right), \Theta (c o _ {t ^ {\prime}}), 1 - d\right) = 1 - d, \\ \mathbf {A c c e p t} o _ {t} ^ {b}, t \geq \tau \wedge \Theta \left(o _ {t} ^ {b}\right) \geq 1 - d \mathbf {o r} \\ t <   \tau \wedge \max \left(\Theta \left(o _ {t} ^ {b}\right), \Theta (c o _ {t ^ {\prime}}), 1 - d\right) = \Theta \left(o _ {t} ^ {b}\right), \\ \mathbf {O f f e r} c o _ {t ^ {\prime}}, t <   \tau \wedge \max \left(\Theta \left(o _ {t} ^ {b}\right), \Theta (c o _ {t ^ {\prime}}), 1 - d\right) = \Theta (c o _ {t ^ {\prime}}). \end{array} \right.\tag{10}
$$

In Eq. (10), it can be seen that the <sup>fi</sup>nal agreement reached by the proposed model is Pareto ef<sup>fi</sup>cient. That is because if an agent accepts its opponent's offer as an agreement, then according to the acceptance condition, the opponent's offer must be better than the agent's all counter-offers in the remaining negotiation rounds. Therefore, the agent's pro<sup>fi</sup>t by accepting the opponent's offer is the maximal pro<sup>fi</sup>t that the agent may get from the negotiation, and it is impossible to further enlarge the agent's pro<sup>fi</sup>t without damaging the opponent's pro<sup>fi</sup>t. Because there are no other offers that will make the agent better off without making the opponent worse off, the <sup>fi</sup>nal agreement generated by the proposed model is Pareto optimal.

In this section, we introduced a desire-based model for e-market negotiation by considering the dynamic changes of supply and demand in an e-market. Firstly, a fair evaluation of an e-market was proposed to indicate the objective supply and demand situation in the e-market. Both buyers and sellers were equally considered in the evaluation, and played the same importance. Secondly, each agent's subjective response was calculated by considering the agent's attitude on the e-market situation changes, and was taken into account in both offer evaluation and counter-offer generation procedures. Lastly, a fair negotiation protocol was proposed to ensure the equilibrium of the negotiation between buyers and sellers. Therefore, the proposed desire-based model is a non-bias negotiation model, and played fairly in-between buyers and sellers.

## 3. Experiments

In this section, we illustrate the experimental results of our desirebased negotiation model, and compare the results with the classic NDF negotiation model [7]. Section 3.1 introduces the experimental setup. Section 3.2 demonstrates the experimental results. In Section 3.3, we analyze the experimental results and present further discussion on the proposed model.

## 3.1. Experiment setting

In order to mimic situations of an e-market, we set the maximal agent number to 50, including 25 buyer agents and 25 seller agents. In order to mimic a dynamic e-market, the negotiation agents' number for both buyers and sellers are randomly selected in between 1 and 25, and are dynamically changed during the negotiation. Therefore, the rates of buyers and sellers vary in between 1 : 25 and 25 : 1. The negotiation issue is cars' prices. For the buyer agents, their initial prices are randomly selected between \$1500 and \$4500, reservation prices are randomly selected between \$5000 and \$15,000. For the seller agents, their initial prices are randomly selected between \$5000 and \$15,000, reservation prices are randomly selected between \$1500 and \$4500. For all negotiation agents, parameters for their negotiation strategy are randomly selected in interval [0, 2], their negotiation deadlines are randomly selected in interval [15, 25]. The <sup>fi</sup>nal negotiation parameters for 25 buyers are displayed in Fig. 5, and the <sup>fi</sup>nal negotiation parameters for 25 sellers are displayed in Fig. 6. In order to clearly show the performance of negotiation models, we analyze six experimental results, in terms of the buyers' average utility (BAU), the sellers' average utility (SAU), all negotiation agents' average utility (AAU), average negotiation rounds (ANR), average negotiation time (ANT, in millisecond), and average agreement number (AAN). The BAU, SAU, and AAU are calculated as follows.

![](/api/attachments/XGNRH6W6/fulltext/images/749b609a461f37da3f10d909b9744d08a2ff8ed1836917121f52e950f3151005.jpg)

$$
B A U = \frac {\text { Sum   of   all   successful   buyers'   utilities }}{\text { Number   of   agreements }}
$$

![](/api/attachments/XGNRH6W6/fulltext/images/87f6e58ab58f16056977a7aa4602ec0acf663a7146198e307af49dc711c644d3.jpg)

11

$$
S A U = \frac {\text { Sum   of   all   successful   sellers'   utilities }}{\text { Number   of   agreements }}\tag{12}
$$

$$
A A U = \frac {\text { Sum   of   all   successful   agents'   utilities }}{\text { Number   of   agreements }}.\tag{13}
$$

## 3.2. Experimental results

In order to display the performance of our negotiation model, we will carry out three experiments. In the <sup>fi</sup>rst experiment, both the buyer and seller agents employ the classic NDF negotiation model [7] (that cannot handle the dynamics of e-market situations); and in the second experiment, the buyer agents will employ our negotiation model, but the seller agents still employ the classic negotiation model; and in the third experiment, both the buyer and seller agents will employ our negotiation model. In all experiments, both the buyer agents' and the seller agents' numbers are started from 1, and gradually increased to 25.

## 3.2.1. All agents employ the classic model

In Fig. 7, we illustrate the <sup>fi</sup>rst experimental results. The x-axis indicates the buyer agent's number, and the y-axis indicates the seller agent's number. It can be seen that by comparing with the SAU (see Fig. 7(b)), the BAUs (see Fig. 7(a)) are relatively low. Such differences are caused by different negotiation parameters between buyer and seller agents, i.e., initial prices, reservation prices, negotiation strategies, and deadlines. The AAUs (see Fig. 7(c)) are the sum of the buyer and seller agents' utilities. Generally, when the e-markets become more complex, i.e., the agents' number increases, agents will spend more ANR (see Fig. 7(d)) and ANT (see Fig. 7(e)) in order to achieve agreements. Also, the AAN will be increased when the agents' number becomes large (see Fig. 7(f)).

![](/api/attachments/XGNRH6W6/fulltext/images/23de6b2673a18a3389ce496cc84c49ce6c9ff3eeaf2ec65ce3c1af0d4512b6e0.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/b2ab318ea8ba03e973302ed35e338e13ba80ef952cded43423d46922c8ab7ae5.jpg)  
Fig. 5. Buyer agents' negotiation parameters.

![](/api/attachments/XGNRH6W6/fulltext/images/8589bb5c2796233677cf92c522cb77edbfbce0c003728fab663b0e208335b82c.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/e931dab0989c12ba95f33945a1d4f21d86b174310398fb1d5ed31cfe7aeefb46.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/63fd1a80195a63ab6b449bb3e8d7e71fa24fff6017e5b4e256ebfc2def0798ea.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/83e08af093d70dd4212896acf7bd6d16205c10c9ba9ece21246d57ed02202d7c.jpg)  
Fig. 6. Seller agents' negotiation parameters.

Furthermore, in order to help readers to understand agent's negotiation behaviors, in Fig. 8 we display the detailed negotiation process in different e-market's situations (i.e., the bene<sup>fi</sup>cial market, the equitable market, and the inferior market) when the maximum agent number is six (i.e., three buyer agents and three seller agents). The x-axis indicates the negotiation round, and the y-axis indicates agents' offer on the car's price. The legend nb indicates the buyer agents employing the classic negotiation model, and the legend ns indicates the seller agents employing the classic negotiation model. Both the buyer agent and the seller agent's numbers are gradually increased from 1 to 3. It can be seen in Fig. 8 that when the negotiation environment changes, both the buyer agents and the seller agents fail to capture the e-market changes, and cannot adapt their negotiation behavior dynamically. For example, the <sup>fi</sup>nal agreements achieved between the buyer agent nb1 and the seller agent ns1 are exactly the same (i.e., 8476) in different e-market's situations (see Fig. 8(a) and (b)). Also, the <sup>fi</sup>nal agreements achieved between the buyer agent nb2 and the seller agent ns1 are exactly the same (i.e., 10,843) in different e-market's situations (see Fig. 8(d), (e), (g) and (h)).

## 3.2.2. Only buyer agents employ our model

In the second experiment, all buyer agents employ our negotiation model, and all seller agents employ the classic negotiation model. In order to ensure all buyer agents would like to complete negotiations, we set the buyer agents' desire to the highest level $( \mathrm { i } . \mathsf { e } . , \varepsilon = 1 )$ . In order to simplify the experiment, we set the buyer agents' attitudes on market changes to normal (i.e., β = 1). Because our negotiation model uses different offer evaluation approaches from the classic negotiation model, in order to easily compare the experimental results, we employ the classic offer evaluation approach to re-evaluate the <sup>fi</sup>nal agreements achieved by using our negotiation model. So the experimental results illustrated in Figs. 7, 9, and 11 can be compared directly.

![](/api/attachments/XGNRH6W6/fulltext/images/3a571e368486d35aeaae091fafe263eddf4b5b462ca39c017b213d4aadf7b9dc.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/f8835aaccd498f1e3c4f3357e7cc8e5afe1b10135262c23026fdcb445b4b8e0c.jpg)  
Fig. 7. Negotiation results of the classic negotiation model.

![](/api/attachments/XGNRH6W6/fulltext/images/af9c9047a0c31c4d98a22a68de9d64eb38b22fba149f233c9095def27f30e82c.jpg)

b  
![](/api/attachments/XGNRH6W6/fulltext/images/d3f86a2edd56e6e4baf01234cbab420903398350c227980af39df959d4a20cb0.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/9e37eaf0bce7973b0d60f23621e0a132b17656b8b11a84543446061e4c01e67f.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/bba3ba2342d1ae08f26f6c20996ad6c23d3023bb377bffccf1543525e8462184.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/8275252a66ed6854493cca7bbe3b3e5d33bb85810955e649de917c836dd9e318.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/1ebdda8f9eea9edc05c972fb66441ae44c610c4e04851446674c108542a8b09c.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/2fbb90e192a7c064954003c25c4e1cfbb8887b703a4c535c6f7302287c3444e6.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/e64fb665f6e0f093b6e1f1e219761223a9104aac9a1eb30e709a194dce146922.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/bb99bbfb4a790d211aa5e2dd570cb50757320eb02b9ed1e47ccf26caa643a6ca.jpg)  
Fig. 8. Negotiation results of the classic negotiation model.

The second experimental results are illustrated in Fig. 9. It can be seen that BAUs (see Fig. 9(a)) show different values in different market situations. When it is an equitable market (i.e., buyer number = seller number), BAUs are similar as the values gained in the <sup>fi</sup>rst experiment. However, when the market becomes more bene<sup>fi</sup>cial to the buyers (i.e., buyer number b seller number), BAUs increase gradually. The maximum BAU is around 1, and appears when there are 25 sellers but only 1 buyer in the market. On the other hand, when the market becomes inferior to the buyers (i.e., buyer number > seller number), BAUs decrease gradually. In the extreme case, when the market contains only 1 seller but 25 buyers, BAU is minimized and almost equals to 0.5 (i.e., the <sup>fi</sup>nal agreement is worse than the reservation offer in the classic model). The reason for such differences is because the buyer agents adapt their negotiation behaviors when the e-market's situation changes, and try to enlarge pro<sup>fi</sup>ts in bene<sup>fi</sup>cial markets, but to give more concessions in inferior e-markets.

Even though the seller agents cannot adapt their negotiation behaviors initiatively, SAUs (see Fig. 9(b)) are also varied in different market situations with the changes of the buyer agents' behaviors. In general, SAU is increased from 0 to 1 when the e-market changes from an extreme buyer's market to an extreme seller's market. In a buyer's market, since the buyer agents know their advantages, they would not make big concessions, and so the seller agents have to. By contrast, in order to reach agreements, the buyer agents have to make great concessions in a seller's market, so the seller agents' pro<sup>fi</sup>ts are increased.

AAUs (see Fig. 9(c)) are increased around 0.2 on average by comparison with the outcomes of classic negotiation model (see Fig. 7(c)). Such an increment implies that our negotiation model can improve the outcome of the whole market in different e-market situations.

In a buyer's market, the buyer agents would like to spend more time on bargaining in order to maximize their pro<sup>fi</sup>ts, and so ANRs (see Fig. 9(d)) are increased in the second experiment. However, when the buyer agents try to prevent pro<sup>fi</sup>ts loss and to guarantee successes in a seller's market, they would like to reach agreements as quick as possible, and so ANRs are decreased. Nevertheless, no matter in a buyer's market or in a seller's market, because the buyer agents need extra time to analyze the market situation and accordingly select their following actions in each negotiation round, our negotiation model could spend more time than the classic negotiation model (see Fig. 9(e)).

According to the experimental setup, since the bargain areas exist between all buyer and seller agents, the classic negotiation model can reach agreements between all buyer agents and seller agents theoreti cally. However, by employing our negotiation model, the buyer agents will adapt their offer evaluation results in different market situations. Especially, in a buyer's market, the seller agents' offers are usually under-valued by the buyer agents, so the buyer agents' requirements are not easy to be satis<sup>fi</sup>ed. That is the reason for the slight decrement on AAN by using our negotiation model (see Fig. 9(f)).

In Fig. 10, we also display the detailed negotiation process for six agents. Legend db indicates the buyer agent employing our desirebased negotiation model. It can be seen that when the negotiation contains only two agents (see Fig. 10(a)), the agreement reached between the buyer agent db1 and the seller agent ns1 is 7745. When the

![](/api/attachments/XGNRH6W6/fulltext/images/0e8fe0a8616f6594aae9c2ea7b1e2e07d1b7d51f506600e029a0d2974e646a35.jpg)

b  
![](/api/attachments/XGNRH6W6/fulltext/images/b161da7c9325d309b05957cbdd5e1277188f46bde5604b5f0e1d75576e72ec09.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/0d00f2cedfdb5669c06e31be5c3f18a2246a10d94559f7778b0d683d1f4b4b0d.jpg)

d  
![](/api/attachments/XGNRH6W6/fulltext/images/19f91fddb9dcdfbb070bce08cd2137b28f15da6e1d832b24763da86a4493f3e8.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/c317e66d93db0be43a7f07675d9ee647aa6a107758290cc9bf37012893653b4e.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/4a99218de9fb4f96711e32c0bd90ae9303922629a87c3a02d034de9690c8ce88.jpg)  
Fig. 9. Negotiation results of our negotiation model.

negotiation contains one more seller agent (see Fig. 10(b)), the buyer agent db1 notices such a change in the e-market, and makes less concession in each negotiation round. The <sup>fi</sup>nal agreement reached between the buyer agent db1 and the seller agent ns1 is 7589. Obviously, the buyer agent's pro<sup>fi</sup>t is increased in a bene<sup>fi</sup>cial market. Furthermore, when the market becomes more bene<sup>fi</sup>cial (see Fig. 10(c)), the buyer agent db1's <sup>fi</sup>nal agreement is only 3798. Such a result justi<sup>fi</sup>es that our negotiation model can help agents to increase pro<sup>fi</sup>ts in the bene<sup>fi</sup>cial markets by comparison with the classic negotiation model.

![](/api/attachments/XGNRH6W6/fulltext/images/23930d8a5a159c13ed8b0b2087fa0b8011b927fe170364f495d5f18eb055d728.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/a485dffed1219b894048db19515561cd03584f5a044964b66e88b45335eefae8.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/82cfd0724b11a87461a502a5ca6bfd33cc7a6e4a429e21c4a5934cd21933791d.jpg)

d  
![](/api/attachments/XGNRH6W6/fulltext/images/3ec7f6f7b5ff94beaa8d8522a4051857ee66a7e567bf2fa2b03cb3ce063676c3.jpg)

e  
![](/api/attachments/XGNRH6W6/fulltext/images/e34867b1c4be9212d854f7442e5d16688aaee9045105039b8076a29a57db38b5.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/6aa1de5c503cde87d216d1b606d65487ecca5a431c0c13b5db184fcab6d4ccfe.jpg)

g  
![](/api/attachments/XGNRH6W6/fulltext/images/db68de20936fb12ecae97a3291ee314f91705228e300f575102b60b8e680f9ef.jpg)

h  
![](/api/attachments/XGNRH6W6/fulltext/images/20534f287b22c30e2eaa710011049ba817d73a52f0a7ea30b9f576e2b123bce4.jpg)  
Fig. 10. Negotiation results of the classic negotiation model.

![](/api/attachments/XGNRH6W6/fulltext/images/1748f383db1da87e604b37b744600a90f92e3208bd5b50d869410e04b42688c4.jpg)

However, when the market becomes inferior, the buyer agents need to pay more in order to compete with other buyers. For example, in Fig. 10(h) the market contains three buyer agents and two seller agents, by using the classic negotiation model, the agreement reached between the buyer agent nb2 and the seller agent ns1 is 10,843; the agreement reached between the buyer agent nb3 and the seller agent ns2 is 7796; and the buyer agent nb1 fails the negotiation. By using our negotiation model (see Fig. 10(h)), the agreement reached between the buyer agent db2 and the seller agent ns1 becomes 12,298 (i.e., the buyer agent db2 loses pro<sup>fi</sup>t by comparing to the buyer agent nb2); the agreement reached between the buyer agent db1 and the seller agent ns2 becomes 8832; and the buyer agent db3 fails the negotiation. It can be seen that by employing our negotiation model, the buyer agent db1 beats the buyer agent db3 through making more concession to the seller agent ns2 (original, the buyer agent nb3 beats the buyer agent nb1 in the classic negotiation model).

## 3.2.3. All agents employ our model

In the third experiment, all agents employ our negotiation model, and the experimental results are illustrated in Fig. 11. Legend ds indicates the seller agents employing our desire-based model. It can be seen that after both buyer and seller agents employ our negotiation model, the BAU (see Fig. 11(a)) is increased more in the buyer's market and decreased more in the seller's market. That is because both the buyer and seller agents are aware of the e-market's situation change, and try to maximize their pro<sup>fi</sup>ts in the bene<sup>fi</sup>cial e-markets, and to give more concessions in the inferior e-markets. By contrary, for the same reason, the SAU (see Fig. 11(b)) is increased more in the seller's market and decreased more in the buyer's market. The AAU (see Fig. 11(c)) becomes more balanced between the buyer's and the seller's market by comparing with the result in the second experiment (see Fig. 9(c)). The ANR (see Fig. 11(d)) shows a big difference by comparing with the previous result (see Fig. 9(d)). The ANR increases in both the buyer's and the seller's market, and the maximal ANR appears in the equitable market. That is because in order to increase pro<sup>fi</sup>ts, the buyer agent would like to negotiate more in the buyer's market, the seller agent would like to negotiate more in the seller's market, and both the buyer and seller agents need to bargain more in the equitable market. Because agents need more negotiation rounds before agreements can be achieved, they will spend more time in negotiations as well. It can be seen that the ANT (see Fig. 9(e)) is increased on average, and is maximized in the most complex market situation (i.e., the market contains 50 agents). Finally, Fig. 11(f) shows the ANN. It can be seen that by using our negotiation model, the ANN is improved by comparison with the previous two experiments (see Fig.s. 7(f) and 9(f)), and reaches the maximal value in all market situations.

In Fig. 12, the detailed negotiation procedures for maximal six agents are illustrated. Both the buyer and the seller agents employ our negotiation model. By comparison with the previous experiment results (see Fig. 10), the buyer agents' pro<sup>fi</sup>ts are improved in the buyer's market, and the seller agents' pro<sup>fi</sup>ts are improved in the seller's market. Such a result accords with the result displayed in Fig. 11(a) and (b). For example, when the market contains only 1 buyer agent and 3 seller agents (i.e., a buyer's market), if all agents employ the classic negotiation model, the agreement achieved between the buyer agent nb1 and the seller agent ns3 is only 6474 (see Fig. 8(c)); if only the buyer agent employs our negotiation model, the agreement achieved between the buyer agent db1 and the seller agent ns2 is improved to 3798 (see Fig. 10(c)); and if all agents employ our negotiation model, the agreement achieved between the buyer agent db1 and the seller agent ds2 is further improved to 3057 (see Fig. 12(c)). Therefore, the buyer agent db1's pro<sup>fi</sup>t is increased in the buyer's market by using our negotiation model. On the other hand, when the market contains 3 buyer agents and only 1 seller agent (i.e., a seller's market), if all agents employ the classic negotiation model, the agreement achieved between the buyer agent nb2 and the seller agent ns1 is only 10,843 (see Fig. 8(g)); if only the buyer agent employs our negotiation model, the agreement achieved between the buyer agent db2 and the seller agent ns1 is improved to 12,339 (see Fig. 10(g)); if all agents employ our negotiation model, the agreement achieved between the buyer agent db2 and the seller agent ds1 is further improved to 13,631 (see Fig. 12(g)). Therefore, the seller agent ds1's pro<sup>fi</sup>t is increased in the seller's market by using our negotiation model.

![](/api/attachments/XGNRH6W6/fulltext/images/64e48385dfe08248bebe1dbfe945d3706fafdeab7e1086294beda64c5d44bf9c.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/34ada49b466055f8fe6ff01dbd42f462c9348a2d28899488a0cbf76d065ad320.jpg)  
e

![](/api/attachments/XGNRH6W6/fulltext/images/79c1c5653f45d497c02c431cabcc435551c99fefd35956440cf3b5cf48fe2779.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/7d9c2617574900e8c81746f4f149870f976d662f0fbbd00e188704d698cf2fe1.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/9ec0c131b071edd01769148c40c868a1723dd334dd15a08c5f5438231aa1d7cc.jpg)  
Fig. 11. Negotiation results of our negotiation model.

![](/api/attachments/XGNRH6W6/fulltext/images/fd04e8e8b6e813e6654d51e1d0aaec96d1647a2a215cc2ac7ca9fa8a4f4e765e.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/72ba3cdb05da9a94912acbac0d06cba12ba8d760435e249abafb8dcc828070dc.jpg)

b  
![](/api/attachments/XGNRH6W6/fulltext/images/0b4364756fb9fba03360af984799512985822bebd7c4e572e822cdc0786c1e3c.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/083194a2b6d029523017c0093162f553915a898d70eac57a02030d9e5496f89f.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/7f15585f671b5dd0c15e0d88ce5ba3913c4214d365bbc2bdc2059e03b89b890b.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/7afce2e5b5baa3c2cf5fa3d4e5d55d754bd32aea76f5f15605da44abc1f0de07.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/a3cba725aa2736a946e8f1d1a9a94fb5d14777b76e01ed9180b1bc9773c10e39.jpg)

g  
![](/api/attachments/XGNRH6W6/fulltext/images/f5f8eab06c6487a91e60d36c5977de21fe54e6a7b01e3dbde92ed6bc67f5ab12.jpg)

h  
![](/api/attachments/XGNRH6W6/fulltext/images/d0d078e7aaf1d32b16f0bf14b2dec28c2b0d5c02350966ac99c7e2804dc81286.jpg)

![](/api/attachments/XGNRH6W6/fulltext/images/4ea08020ba3d859462c485e4eb72bea511983962180875b1576b2c98c08fddc8.jpg)  
Fig. 12. Negotiation results of the classic negotiation model.

## 3.3. Discussions

In the previous subsection, we illustrated experimental results in different market situations. It can be seen that when the e-market's situations change, our negotiation model can help agents to modify their negotiation behaviors dynamically. Also, even for the same e-market's situation, agents' behaviors may also be different when they have different desires on trading. Therefore, both e-market's situations and agents' desires will impact negotiation results. In this subsection, we discuss how these two factors affect agents' behaviors in negotiations.

In Fig. 13, we illustrate a model to demonstrate how the e-market's situation and the agent's desire impact agents' behaviors in negotiations. The x-axis denotes the e-market's situation (refer to Eq. (1)), the y-axis denotes the agent's desire, and the z-axis denotes the agent's evaluation on an offer (refer to Eq. (3)). Then by setting both negotiation parameters $\beta$ and λ to 1 (i.e., normal attitude on market change and linear negotiation strategy), a trading surface for the desire-based negotiation model can be formulated as follows:

$$
\Gamma (\Phi , d) = \left\{ \begin{array}{l} (1 + \Phi) * (1 - d), \text {   when   } - 1 \leq \Phi \leq 0, \\ (\Phi - 1) * d + 1, \text {   when   } 0 <   \Phi \leq 1 \end{array} \right.\tag{14}
$$

where $d \in [ 0 , 1 ]$ and Φ∈[−1,1].

The trading surface de<sup>fi</sup>nes a set of thresholds on agent's pro<sup>fi</sup>ts. During the negotiation, agents will accept offers above or on the surface, but reject offers below the surface. For the trading surface of our desire-based negotiation model, in an extreme case, when Φ $\ c = - 1$ or $d = 1$ the threshold is $\Gamma ( \Phi , d ) = 0 ,$ , so the agent will accept the ‘best’ offer from its opponents <sup>fi</sup>nally in order to make the deal. That is because when $\Phi = - 1$ , the market is extremely disadvantageous for the agent, so any offer will be considered as a ‘good’ offer based on the market situation; and when $d = 1$ , the agent needs to complete the negotiation extremely, so the agent will accept the ‘best’ offer from its opponents <sup>fi</sup>nally. In another extreme case, when $\Phi = 1$ or $d = 0 ,$ the threshold is $\Gamma ( \Phi , d ) = 1$ , so the agent will reject any offer which cannot satisfy its initial offer. That is because when $\Phi = 1$ , the e-market is extremely advantageous for the agent, so any offer below the agent's initial offer will be considered as a ‘bad’ offer; and when $d = 0 ,$ the agent's motivation for completing the negotiation is very low, so any offer worse than the agent's initial offer de<sup>fi</sup>nitely will be rejected by the agent. In a normal case, such as $\Phi = 0$ and $d = 0 . 5$ (i.e. an equitable market and the agent hesitates about trading), the agent will not accept any offer which cannot meet its satisfaction by 50%.

![](/api/attachments/XGNRH6W6/fulltext/images/be547388d0479fc9722b28dd35e297e0e665c47b31ac431f35586b66ac91df96.jpg)  
Fig. 13. Trading surface of negotiation models.

Also, we display another trading surface for the classic negotiation model. In comparison with the desire-based model, the classic model's trading surface is just a plane surface. That means the agent in the classic model will <sup>fi</sup>x its thresholds in all situations into a constant, and does not consider changes of markets and agent's desires for trading. It can be seen in Fig. 13 that an instance of the trading surface for the classic model $( \Lambda = 5 0 \% )$ is partially below the trading surface of our model and partially above our model. For agents using the classic model, they will accept all offers on this surface. However, for agents using our model, situations are more complex. When Φ > 0 (i.e., a bene<sup>fi</sup>cial market) and $d < 0 . 5 \ ( \mathrm { i . e . , }$ agents do not really want to make a deal), agents will not accept offers which are located on the classic model's trading surface. On the other hand, when Φ b 0 (i.e., an inferior market) and $d > 0 . 5 ( \mathrm { i . e . }$ , agents want to make a deal), agents will accept offers which locate on the classic model's trading surface.

## 4. Related work

Some related works also take into account agent negotiation in complex environments. This section discusses differences between these related works and our model.

An et al. [1] proposed a concurrent negotiation model to coordinate interrelated negotiations in Electronic Commerce markets where agents need to negotiate with different opponents for multiple resources. During a concurrent negotiation, an agent negotiates with different opponents on different resources, and adjusts its negotiations according to the market conditions and negotiation situations. If it is necessary, the agent can also decommit its tentative agreements by paying a penalty. Because the agent may have different deadlines and expectations on different resource negotiations, both the time constraints and the expected agreement prices are considered for each negotiation. Also, the maximum number of <sup>fi</sup>nal agreements is considered to evaluate the overall negotiation. By comparison with their work, our paper considers the supply and demand of an e-market and the multiple preferences on negotiation issues.

He et al. [14] proposed a very successful model for trading agents in solving issues in supply chain management. Firstly, the customer agent in their model collected customer requests and sorted them by agent's pro<sup>fi</sup>ts gained from each customer. Then according to customers' requirements, such as type of item, reserved price, penalty and due time, the customer agent makes a decision about the order of servers. In order to increase the trading agent's pro<sup>fi</sup>t, the component agent predicts customers' requests in both the near term and distant future. According to the prediction results, the trading agent keeps its own inventory in an appropriate level in order to ensure that adequate components can be provided for daily regular offers, as well as minimize the storage expenditure. Finally, by employing the prediction results and fuzzy reasoning, the trading agent can successfully handle issues of offer generation, component booking and assembly, and PC delivery. One signi<sup>fi</sup>cant difference between He's model and our proposed model is that in the former model, competitions from other trading agents are not taken into account. By contrast, in our proposed model, we consider both trading opportunity and competition in real time. Therefore, He's model is very suitable to solve issues in supply chain management, while our model can yield ef<sup>fi</sup>ciencies in dynamic multilateral bargaining.

Gregg and Walczak [13] proposed a decision support system for online-auction. Besides buyer agents and seller agents, authors also created several assistant agents, such as information retrieval agents, data-analysis agents and information agents, to help auction participants to improve the quality of their decision making. The assistant agents can ef<sup>fi</sup>ciently collect data related to the online auction, make further statistical calculations and recommendations for the auction, and generate additional auction rules by using data mining strategies. Both simulated and real purchases at online auction indicate the bene<sup>fi</sup>t that auction participants achieve by employing this auction advisor system.

Ren et al. [26,27] proposed a market-driven model to help agents to make concessions in negotiation. Four concession factors, namely trading opportunity, trading competition, trading time and strategy and eagerness, are introduced to represent both market and agent situations. Each concession factor impacts an agent's concession from a certain consideration. All concession factors are updated by the agent according to the market's dynamic situation. But agents' judgments on offers and expectations on negotiation outcomes are still <sup>fi</sup>xed. In this paper, we model markets by considering both market situations and agent desires. During negotiations, agents make concessions based on both objective and subjective considerations in the negotiation.

By comparison with the above related works, our negotiation model has the following merits. It models negotiations in e-markets by considering (1) both objective situations of markets and subjective desires of agents, (2) both concurrent and future possible situations of e-markets, and (3) both agents' individual pro<sup>fi</sup>t and trade-offs of whole e-market.

## 5. Conclusion and future work

In this paper, we proposed a desire-based negotiation model to help agents to perform adaptive negotiation behaviors in e-markets by considering both the e-market's situation and the agent's desire. In our model, the offer evaluation approach and counter-offer generation approach take both the objective situation of e-markets and the subjective situation of agents into account. Offers from opponents are evaluated relatively by considering the e-market's situation and counter-offers are generated through estimating the possible changes of the e-market. Also, a negotiation protocol was proposed to de<sup>fi</sup>ne the negotiation procedure in e-markets. In the experiment, we illustrate the performance of the proposed negotiation model in different e-market situations. The experimental results well demonstrated that our negotiation model can effectively capture the e-market situation changes, and modify agents' negotiation behaviors accordingly. Furthermore, based on experimental results, we proposed the concept of ‘trading surface’ and discovered that the trading surface of our negotiation model is more applicable than the classic model's in e-markets.

Our future work will focus on two aspects. The <sup>fi</sup>rst consideration is to extend the existing model from single issue negotiation to multiple issue negotiation by considering both numerical and categorical issues. The second consideration is to employ the Fuzzy and/or Neural network approaches [3] to help agents to perform more adaptive negotiation behaviors in e-markets.

## References

[1] B. An, V. Lesser, K. Sim, Strategic agents for multi-resource negotiation, Autonomous Agents and Multi-Agent Systems 23 (1) (2011) 114–153.

[2] Y. Bakos, The emerging role of electronic marketplaces on the Internet, Communications of the ACM 41 (8) (1998) 35–42

[3] R. Carbonneau, G. Kersten, R. Vahidov, Pairwise issue modeling for negotiation counteroffer prediction using neural networks, Decision Support Systems (2011) 449–459.

[4] H. Chandrashekhar, B. Bhasker, Quickly locating ef<sup>fi</sup>cient, equitable deals in automated negotiations under two-sided information uncertainty, Decision Support Systems 52 (1) (2011) 157–168.

[5] C. Cheng, C. Chan, K. Lin, Intelligent agents for e-marketplace: negotiation with issue trade-offs by fuzzy inference systems, Decision Support Systems 42 (2) (2006) 626-638

[6] S. Das The Effects of Market-Making on Price Dynamics 7th Int, Conf, on Autonomous Agents and Multiagent Systems (AAMAS08). 2008 pp. 887-894

[7] P. Faratin, C. Sierra, N. Jennings, Negotiation decision functions for autonomous agents, Journal of Robotics and Autonomous Systems 24 (3–4) (1998) 159–182.

[8] S. Fatima, M. Wooldridge, N. Jennings, Multi-Issue Negotiation Under Time Constraints, 1st Int. Conf. on, Autonomous Agents and Multi-Agent Systems (AAMAS02), 2002, pp. 143–150.

[9] S. Fatima, M. Wooldridge, N. Jennings, An agenda-based framework for multi-issue negotiation.Artificial Intelligence 152 (1) (2004).1–45

[10] S. Fatima, M. Wooldridge, N. Jennings, Optimal negotiation of multiple issues in incomplete information settings, 3rd Int. Conf. on Autonomous Agents and Multiagent Systems(AAMAS04), 2004, pp. 1080–1087.

[11] S. Fatima, M. Wooldridge, N. Jennings, Approximate and online multi-issue negotiation, 6th Int. Conf. on, Autonomous Agents and Multi-Agent Systems (AAMAS07) 2007, pp. 947–954.

[12] S. Fatima, M. Wooldridge, N. Jennings, An analysis of feasible solutions for multi-issue negotiation involving nonlinear utility functions, Proc. of 8th Int. Conf. on Autonomous Agents and Multiagent Systems (AAMAS09), 2009, pp. 1041–1048

[13] D. Gregg, S. Walczak, Auction Advisor: an agent-based online-auction decision support system, Decision Support Systems 41 (2) (2006) 449–471.

[14] M. He, A. Rogers, X. Luo, N. Jennings, Designing a successful trading agent for supply chain management, 5th International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS 2006), ACM, Hakodate, Japan, 2006, pp. 1159–1166.

[15] N. Jennings, P. Faratin, A. Lomuscio, S. Parsons, C. Sierra, M. Wooldridge, Automated negotiation: prospects, methods, and challenges, International Journal of Group Decision Negotiation 10 (2) (2001) 199–215.

[16] K. Kurbel, I. Loutchko, A model for multi-lateral negotiations on an agent-based job marketplace, Electronic Commerce Research and Applications 4 (3) (2005) 187–203.

[17] G. Lai, C. Li, K. Sycara, A general model for Pareto optimal multi-attribute negotiations, 2nd Int. Workshop on Rational, Robust, and Secure Negotiations in Multi-Agent Systems (RRS06), 2006, pp. 55–76.

[18] G. Lai, K. Sycara, C. Li, A. Pareto, Optimal model for automated multi-attribute negotiations, 6th Int. Conf. on, Autonomous Agents and Multi-Agent Systems (AAMAS07), 2007, pp. 1040–1042.

[19] X. Li, L. Soh, Adaptive, con<sup>fi</sup>dence-based strategic negotiations in complex multiagent environments, 9th Int. Florida Arti<sup>fi</sup>cial Intelligence Research Society Conf., 2006, pp. 80–85.

[20] M. Ma, Agents in E-commerce, Communications of the ACM 42 (3) (1999) 78–80

[21] J. MacKie-Mason, A. Osepayshvili, D. Reeves, M. Wellman, Price prediction strategies for market-based scheduling, 4th Int. Conf. on Automated Planning and Scheduling (ICAPS04), 2004, pp. 244–252.

[22] P. Maes, R. Guttman, A. Moukas, Agents that buy and sell, Communications of the ACM 42 (3)(1999)(81-ff)

[23] J. Niu, K. Cai, S. Parsons, E. Gerding, P. McBurney, Characterizing effective auction mechanisms: insights from the 2007 TAC Market Design Competition 7th Int, Conf on Au tonomous Agents and Multiagent Systems (AAMAS08), 2008, pp. 1079–1086.

[24] M. Papazoglou, Agent-oriented technology in support of E-business, Communications of the ACM 44 (4) (2001) 71–77.

[25] F. Ren, M. Zhang, Desire-based negotiation in electronic marketplaces, Innovations in Agent-Based Complex Automated Negotiations (2011) 27–47.

[26] F. Ren, K. Sim, M. Zhang, Market-driven agents with uncertain and dynamic outside options, 6th Int. Conf. on, Autonomous Agents and Multi-Agent Systems (AAMAS07), 2007, pp. 721–723.

[27] F. Ren, M. Zhang, K. Sim, Adaptive conceding strategies for automated trading agents in dynamic, open markets, Decision Support Systems 46 (3) (2009) 704–716.

[28] C. Sierra, P. Faratin, N. Jennings, A service-oriented negotiation model between autonomous agents, 8th European Workshop on Modeling Autonomous Agents in a Multi-Agent World (MAAMAW97), 1997, pp. 17–35.

[29] Y. Tan, W. Thoen, Toward a generic model of trust for electronic commerce, International Journal of Electronic Commerce 5 (2) (2000) 61–74.

![](/api/attachments/XGNRH6W6/fulltext/images/da3c49ce500dd6815a9ebe55b949af8dd03f78c68286feb03efe7a3d870020c8.jpg)

Fenghui Ren (www.uow.edu.au/\~fren) received his MCompSc-Res. and Ph.D. from the University of Wollongong in 2006 and 2010, respectively. He received his BCompSc from the Xidian University in 2003. Currently, he is the Vice Chancellor's Fellow in the School of Computer Science and Software Engineering at the University of Wollongong. Dr. Ren is an active researcher and published 38 research papers in reputable journals and conferences. His research interests include agent-based modeling, simulation, reasoning and learning, agent coordination, negotiation and optimization.

![](/api/attachments/XGNRH6W6/fulltext/images/2f5e20aff856852e17d2b4d01764b83f25370bc1cefccdd4cb416a298a53864f.jpg)

Minjie Zhang is an associate professor in the School of Computer Science and Software Engineering and the Director of Intelligent System Research Group in the Faculty of Informatics, at the University of Wollongong Australia. She received a BSc degree from Fudan University, China in 1982, and her PhD degree from the University of New England, Australia in 1996. Dr Zhang is an active researcher and published over 130 research papers. She is a program chair for a number of international workshops and conferences. As a guest editor, Dr Zhang jointly edited 5 special issues and 6 books. She is the chief investigator for more than 10 different research grants including an ARC (Australia Research Council) Discovery grant and an ARC Linkage Grants. Her research interests include multi-agent systems, agent-based simula-

tion and modeling in complex domains, agent-based mart grids and knowledge discovery and data mining.
