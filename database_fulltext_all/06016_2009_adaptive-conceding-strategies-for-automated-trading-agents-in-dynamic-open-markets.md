---
otero_id: 6016
otero_key: "NDTEY7P6"
title: "Adaptive conceding strategies for automated trading agents in dynamic, open markets"
authors: "Fenghui Ren; Minjie Zhang; Kwang Mong Sim"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Adaptive conceding strategies for automated trading agents in dynamic, open markets

Fenghui Ren <sup>a,</sup>⁎, Minjie Zhang <sup>a</sup>, Kwang Mong Sim <sup>b</sup>

<sup>a</sup> School of Computer Science and Software Engineering, University of Wollongong, Wollongong NSW 2522, Australia

<sup>b</sup> Dept. of Information and Communications, Gwangju Institute of Science and Technology, Gwangju 500-712, Republic of Korea

## a r t i c l e i n f o

Article history: Received 22 November 2007 Received in revised form 29 October 2008 Accepted 5 November 2008 Available online 19 November 2008

Keywords: Automated negotiation Bargaining Negotiation agents Multi-lateral negotiation E-markets

## a b s t r a c t

One of the crucial issues of automated negotiation in multi-agent systems is how to reach an agreement when a negotiation environment becomes open and dynamic. Even though some strategies have been proposed by researchers, most of them can only work within a static negotiation environment. In this paper, we present a model for designing a strategy for agents that makes adjustable rates of concession by negotiating according to the changes of environments with uncertain and dynamic outside options. This proposal is based on the market-driven agents (MDAs) model, and is guided by four factors in order to determine the degree of concession. These factors are trading opportunity, trading competition, trading time and strategy, and eagerness. The contribution of this paper is extending the MDAs model to an open and dynamic negotiation environment by considering both the current and potential changes of the environment.

© 2008 Elsevier B.V. All rights reserved

## 1. Introduction

Automated negotiation [20] has been an active research area in recent years. Research on negotiation agents [13,16] has received a great deal of attention in the areas of multi-agent systems and ecommerce [11,8]. Currently, one of the most crucial issues for automated negotiation is how to reach an agreement when the negotiation environment becomes open and dynamic. Although some agent-based systems [19,3,2,10,9,26,17] have been proposed and implemented successfully by researchers, agents involved in these systems usually can only adopt predetermined strategies to negotiate with others. Therefore, when the negotiation environment is open and dynamic, such as more products and services becoming available and negotiators either entering or leaving the negotiation dynamically, agents cannot provide reasonable responses to changes in the negotiation environment by adopting their current negotiation strategies straightway. Furthermore, negotiators may also be bounded by restrictions such as deadlines and resource limitations. Agents may need to modify their negotiation strategies too when the pressure from these restrictions changes. The Market-Driven Agents (MDAs) model [22,24,23,18] is one strategy which takes into account the relationship between agents' negotiation strategies and the negotiation environment. Through comparing the MDAs model [23,22,25] and other negotiation strategies [19,3,2,10,9,26], the ef<sup>fi</sup>cient perfor mance of the MDAs model has been illustrated. In the MDAs model, agents are guided by four concession factors, and these factors determine how much concession agents can give during the negotiation based on the environment. These concession factors are trading opportunity (see Section 2.2), trading competition (see Section 2.3), trading time and strategy (see Section 2.4) and eagerness (see Section 2.5).

However, even though the MDAs model considers the relationship between agents' strategies and the negotiation environment, it does not take into account the situation when the negotiation environment becomes open and dynamic. In an open and dynamic environment, agents may enter into and leave off the negotiation freely, and so the uncertainty of the negotiation may be increased too. In order to have a broad view on the negotiation environment, we adopt Sycara's model [14,15] to classify negotiations according to the complexity of their environment. The model is illustrated in Fig. 1, and according to this model, negotiations are divided into three levels. The negotiation which is processed within the simplest environment is named singlethreaded negotiation. In this level, the negotiation is carried out between only two agents without any outside options. None of the negotiators can leave off the negotiation before an agreement is reached or a deadline is met, and also no agent can enter into the negotiation during the process. The second level is named synchronized multi-threaded negotiations, in which the negotiation is processed among multiple agents. Therefore, agents need more complex negotiation strategies in order to reach an agreement when they face more than one negotiators. As with the <sup>fi</sup>rst level, all negotiators are still not allowed to leave off and enter into the negotiation freely. Therefore, in this level, agents make any decision in the negotiation based on the current negotiation environment only. The third level is named dynamic multi-threaded negotiations. In this level, all negotiators can leave and enter the negotiation dynamically. Therefore, agents should think about not only the current situation but also possible changes to the negotiation environment. According to the classi<sup>fi</sup>cation, in the current stage, the MDAs model can work well on the <sup>fi</sup>rst two levels, but cannot handle negotiation on the third level. In order to address this issue, in this paper, we propose to extend the MDAs model to third level negotiation by considering the uncertain and dynamic outside options.

![](/api/attachments/NDTEY7P6/fulltext/images/8374a68a2735fcc8527b2066e52fa839d380cdf5b1c7edf7c3882bbffeacd995.jpg)  
Fig. 1. A nested view of general negotiation models [14].

The rest of this paper is organized as follows. In Section 2, the principle of the MDAs model is introduced brie<sup>fl</sup>y. Section 3 introduces the proposed mechanisms to extend the MDAs model. Section 4 illustrates the experimental results. Section 5 discusses related works. Section 6 concludes this paper and outlines our future work.

## 2. A model for market-driven agents

In this section, the principle of the MDAs model [24] is recalled brie<sup>fl</sup>y and in particular all four concession factors in MDA are also recapped. Finally, we discuss the limitations of the MDAs model in order to highlight the motivation of this paper.

## 2.1. Principle of MDAs model

In order to make reasonable negotiation strategies according to the negotiation environment, agents may need to modify the spread k that is de<sup>fi</sup>ned as the difference between an agent's proposal and the counterproposal of its trading partner. For example, if the price of a car is \$10,000, and the buyer would only like to pay \$9000, then the spread k for both seller and buyer is \$1000. In general, when k is large, the probability that agents may complete the negotiation will be decreased, and conversely when k is small, the probability will be increased. Therefore, by modifying the spread $k ,$ agents can maintain the bene<sup>fi</sup>ts gained from their partners and increase the likelihood of completing the negotiation. Let k′ denote the spread in the next negotiation round, then k′ is determined by assessing current negotiation situation as follows:

$$
k ^ {\prime} = O (n, \omega_ {i}, v) C (m, n) T (t, t ^ {\prime}, \tau , \lambda) E (\varepsilon) k\tag{1}
$$

where $O ( n , w _ { i } , \nu )$ is the factor for trading opportunity that determines the amount of concession according to agents' expectations about the negotiation, the number of partners and their partners' offers (see Section 2.2); and $C ( m , n )$ is the factor for trading competition, which is determined by the probability that an agent is ranked as the most preferred trader by at least one of its partners (see Section 2.3); T(t, t′, $\tau , \lambda )$ is the factor for trading time and strategy that determines agents' rates on concession by considering time constraints (see Section 2.4); $E ( \varepsilon )$ is the factor for eagerness that determines the amount of concession by considering agents' eagerness to <sup>fi</sup>nish the negotiation (see Section 2.5). The Formula (1) assumes that all concession factors are independent (see our previous papers [22,24,23,18] for detailed explanation of this formula). In the following subsections, each of these concession factors will be discussed in detail, respectively.

## 2.2. Trading opportunity

In MDAs, the following factors are considered in order to determine the trading opportunity:

• the number of partners n;

• the spread k between an agent and its partners; and

• the probability p of completing the negotiation.

Let $p$ and $p ^ { \prime }$ present the probabilities of an agent completing the negotiation in the current and next negotiation round, respectively. Let k and k′ be values of the current and next spreads, respectively. If the distance between p and $p ^ { \prime }$ is large, in order to keep a reasonable probability of <sup>fi</sup>nishing the negotiation, agents may increase the distance between k and k′. By contrast, if the distance between p and $p ^ { \prime }$ is small, agents may decrease the distance between k and k′ in order to maintain their bene<sup>fi</sup>ts. The relationship between these four factors is represented as follows:

$$
k ^ {\prime} = \frac {p}{p ^ {\prime}} \times k\tag{2}
$$

Suppose in a negotiation round, agent $B _ { 1 } " s$ last offer is represented as a utility vector $v = ( v _ { b } , v _ { s } )$ and its partner S 's offer is a utility vector $\omega = ( \omega _ { b } , \omega _ { s } ) . B _ { 1 } ^ { \prime } s$ last offer generates a payoff of $v _ { b }$ for itself and $v _ { s }$ for $S _ { 1 } ;$ and $S _ { 1 } " s$ offer generates a payoff of ω for itself and $\omega _ { b }$ for $B _ { 1 } .$ Let $c _ { b }$ denote the worst possible utility (conflict utility) for $B _ { 1 } .$ If the subjective probability of $B _ { 1 }$ obtaining $c _ { b }$ is $p _ { c } ,$ we have:

$$
[ (1 - p _ {c}) v _ {b} + p _ {c} c _ {b} ] \leq \omega_ {b}\tag{3}
$$

According to Eq. (3), the highest con<sup>fl</sup>ict probability that $B _ { 1 }$ may encounter is the maximum value of $p _ { c }$ as follows:

$$
p _ {c} = \frac {\mathbf {v} _ {b} - \boldsymbol {\omega} _ {b}}{\mathbf {v} _ {b} - c _ {b}} = \frac {k}{\mathbf {v} _ {b} - c _ {b}}\tag{4}
$$

Consequently, the aggregated con<sup>fl</sup>ict probability that $B _ { 1 }$ may encounter by considering all partners is:

$$
P _ {c} = \prod_ {i = 1} ^ {n} p _ {i} = \prod_ {i = 1} ^ {n} \frac {k _ {i}}{\mathfrak {v} _ {b} - c _ {b}} = \frac {\prod_ {i = 1} ^ {n} (\mathfrak {v} _ {b} - \boldsymbol {\omega} _ {i})}{(\mathfrak {v} _ {b} - c _ {b}) ^ {n}}\tag{5}
$$

where $k _ { i }$ is the spread between $B _ { 1 } " s$ offer and S 's offer, and n is the number of $B _ { 1 } " s$ partners. Therefore, the probability $p$ that $B _ { 1 }$ will obtain a utility $v _ { b }$ with at least one partner is:

$$
p = 1 - P _ {c} = 1 - \frac {\prod_ {i = 1} ^ {n} (\boldsymbol {v} _ {b} - \boldsymbol {\omega} _ {i})}{(\boldsymbol {v} _ {b} - \boldsymbol {c} _ {b}) ^ {n}}\tag{6}
$$

From Formulas $( 2 )$ and (6), we get the relationship between current and next negotiation round as follows:

$$
k ^ {\prime} = \frac {1}{p ^ {\prime}} \left(1 - \frac {\prod_ {i = 1} ^ {n} \left(\boldsymbol {v} _ {b} - \boldsymbol {\omega} _ {i}\right)}{\left(\boldsymbol {v} _ {b} - c _ {b}\right) ^ {n}}\right) k\tag{7}
$$

Then the function to represent the concession factor trading opportunity is:

$$
O (n, \omega_ {i}, v) = \frac {1}{p ^ {\prime}} \left(1 - \frac {\prod_ {i = 1} ^ {n} (\boldsymbol {v} - \boldsymbol {\omega} _ {i})}{(\boldsymbol {v} - c) ^ {n}}\right)\tag{8}
$$

## 2.3. Trading competition

The concession factor trading competition in the MDAs model is calculated by taking into account the probability that an agent will not be considered as the most preferred partner by its partners. Suppose that the agent $B _ { 1 }$ has m−1 competitors $B _ { 2 } , . . . , B _ { m }$ and n partners $S _ { 1 } , . . . ,$ $S _ { n } .$ The probability that $B _ { 1 } { \mathrm { { i s } } }$ not considered as the most preferred partner by all $\begin{array} { r l } { S _ { i } \mathrm { i } s } & { { } \left( \frac { m - 1 } { m } \right) ^ { \prime } } \end{array}$ . Hence, the concession factor trading competition is de<sup>fi</sup>ned in Formula (9), which indicates the probability that $B _ { 1 }$ is considered as the most preferred partner by at least one of $\cdot _ { S _ { i } . }$

$$
C (m, n) = 1 - \left(\frac {m - 1}{m}\right) ^ {n}\tag{9}
$$

## 2.4. Trading time and strategy

To enable agents to change their negotiation strategies during the negotiation to get better outcomes, Fatima et al. [5] designed negotiation strategies such as:

1) To complete the negotiation as quickly as possible, agents make large concession at the beginning of the negotiation, and small concession when the deadline is approaching;

2) To guarantee their bene<sup>fi</sup>ts, agents make small concession at early stages of the negotiation. However, when the deadline is approaching, in order to avoid negotiation failure, agents will make large concession;

3) To process negotiation in a smooth way, agents make constant concessions throughout the negotiation.

4) To act on behalf of some human users who are obstinate, agents keep their original offers throughout the negotiation without any concession.

In general, the concession strategies mentioned above can be formulated by considering the time constraints as follows [5]:

$$
k ^ {\prime} = \left[ 1 - (t / \tau) ^ {\lambda} \right] \times k _ {0}\tag{10}
$$

where $k _ { 0 }$ is the initial spread, t is the current negotiation time, τ is the negotiation deadline (t ≤ τ) and λ is a nonnegative temporal sensitivity factor that decides agents' negotiating strategies as shown in Fig. 2.

1) When $\lambda { > } 1 ,$ the rate of change in the slope is increasing, corresponding to smaller concession in the early stage of negotiation but large concession in the later stage.

2) When $0 < \lambda < 1 ,$ the rate of change in the slope is decreasing, corresponding to large concession in the early stage but smaller concession in the later stage.

![](/api/attachments/NDTEY7P6/fulltext/images/9e5b66a16624a26377730a8ff1fd341bcb4a5066bf14e45be836fe82e0ca3094.jpg)  
Fig. 2. Modeling different rates of concession.

3) When $\lambda = 1 ,$ , the rate of change in the slope is zero, corresponding to making constant concession throughout the negotiation.

4) When $\lambda { = } 0 ,$ the rate of change of the slope and the slope itself are always zero, corresponding to not making any concession throughout the whole negotiation.

Let the spread at t (when the last bid/offer was made) be $k ,$ and the next spread at time t′ (when the next bid/offer will be made) be $k ^ { \prime } .$ From Formula (10), it follows that $\begin{array} { r } { k _ { 0 } = \frac { k } { 1 - ( t / \tau ) ^ { \lambda } } } \end{array}$ and $k ^ { \prime } { = } \left[ 1 { - } ( t ^ { \prime } / \tau ) ^ { \lambda } \right]$ k<sub>0</sub>. <sup>ð</sup> <sup>Þ</sup>  With other market factors unchanged, an agent's next spread is:

$$
k ^ {\prime} = \frac {1 - \left(\frac {t ^ {\prime}}{\tau}\right) ^ {\lambda}}{1 - \left(\frac {t}{\tau}\right) ^ {\lambda}} k\tag{11}
$$

Thus, concession factor trading time and strategy is formed by considering the changes of the spread current negotiation time t and the next negotiation round t′ as follows:

$$
T (t, t ^ {\prime}, \tau , \lambda) = \frac {1 - \left(\frac {t ^ {\prime}}{\tau}\right) ^ {\lambda}}{1 - \left(\frac {t}{\tau}\right) ^ {\lambda}}\tag{12}
$$

## 2.5. Eagerness

Concession factor eagerness considers an agents' desire to complete the negotiation and to make concession during the negotiation. Let ε $( 0 \leq \varepsilon \leq 1 )$ represent the percentage of convergence of the spread k, then the spread $k ^ { \prime }$ in the next negotiation round is given by $k ^ { \prime } = ( 1 - \varepsilon ) \times k .$ ε corresponds to an agent's desire to make concession to narrow the differences between itself and others in each negotiation iteration, independent of the current trading time, number of competitors, and trading partners. The greater the value of $\varepsilon ,$ the more desire by the agent to make concession. In MDAs, ε is supplied by the user and is assumed to be a constant. The concession factor eagerness is represented as follows:

$$
E (\varepsilon) = 1 - \varepsilon\tag{13}
$$

## 2.6. Limitations of MDAs

In the above, we recapped the basics of MDAs. Now we disclose its limitations that may impact the negotiation outcomes. Even though MDAs has shown good performance [23,22,25], there still exist some limitations which may restrict its application in the real world. In fact, in the current form MDAs cannot handle negotiations in situations where the negotiation environment becomes open and dynamic, and the outside options become uncertain. The main reason is that the current MDAs model does not employ any mechanism to handle possible changes on the negotiation environment. Therefore, when the potential outside options become available in the future, agents cannot make reasonable responses to these changes, and cannot update their negotiation strategies according to these changes. For example, the concession factor trading opportunity is assessed by the total number of partners and spreads between agents' offers and their partners' offers (see Formula (8)). However, it does not involve the forecast that partners may enter or leave the negotiation dynamically. Therefore, if the negotiation is processed with uncertain outside options, using these strategies agents cannot make effective decisions to changes of partners. Also, concession factor trading competition cannot handle the situation when the number of partners and competitors are changed in the future. Thus, if the negotiation environment is changed, Formula (9) cannot represent the probability that an agent is being considered as the most preferred partner by all of their partners correctly anymore. Furthermore, for concession factors trading time and strategy and eagerness, it will be more ef<sup>fi</sup>cient for agents to change their negotiation strategies and eagerness dynamically rather than keep these factors as constants when the potential outside options are available. Therefore, in order to remove the limitations mentioned above, an extended MDAs model is proposed in this paper. Ways of modifying all concession factors are introduced in detail in the following section.

## 3. MDAs with uncertain and dynamic outside options

In this section, an extended MDAs model is introduced. The major approaches to modify the concession factors trading opportunity (see Section 3.1) and trading competition (see Section 3.2) are: 1) to handle possible changes (i.e. uncertainties when negotiators will enter into or leave off the negotiation) on the negotiation environment; 2) to generate the corresponding reactions for each possible change; and 3) to make the <sup>fi</sup>nal decision by combining all reactions based on their individual probabilities. The concession factors of trading time and strategy (see Section 3.3) and eagerness (see Section 3.4) are modi<sup>fi</sup>ed based on the consideration that agents may change their negotiation strategies and their eagerness to reach an agreement.

## 3.1. Trading opportunity

This subsection details how to modify concession factor trading opportunity in an open and dynamic negotiation environment by considering the three cases: 1) negotiating partners are allowed to enter negotiation only; 2) negotiating partners are allowed to leave negotiation only; and 3) negotiating partners are allowed to enter into and leave off negotiation at their will.

1) Partners enter into negotiation only:

• Only one partner enters into the negotiation:

When only one partner enters the negotiation in the next round of negotiation, according to Formula (5) the aggregated con<sup>fl</sup>ict probability is:

$$
P _ {c} ^ {1} = \prod_ {i = 1} ^ {n} p _ {i} \times p _ {n + 1}\tag{14}
$$

Since $p _ { i } ( i \in [ 1 , n ] )$ is already known, then the key point is how to get the con<sup>fl</sup>ict probability $p _ { n + 1 }$ for the new incoming partner. Because $p _ { n + 1 }$ is unknown until the next negotiation round, so we will determine an approximate value to replace $p _ { n + 1 }$ based on the situation of current negotiation round. Let $p _ { n + 1 } ^ { c }$ be the most approximate value o $p _ { n + 1 }$ in all $p _ { i } ,$ then any $p _ { i }$ has the same possibility $\left( { \frac { 1 } { n } } \right)$ to be $p _ { n + 1 } ^ { c }$ . Thus the mathematical expectation of $\textstyle p _ { n + 1 } ^ { c } \mathrm { i } s \sum _ { i = 1 } ^ { n } p _ { i } / n .$ Because $p _ { n + 1 } ^ { c }$ is the approximation of $p _ { n + 1 } ,$ then Formula (14) can be rewritten as:

$$
P _ {c} ^ {1} = \prod_ {i = 1} ^ {n} p _ {i} \times \frac {\sum_ {i = 1} ^ {n} p _ {i}}{n}\tag{15}
$$

Therefore, according to Formula (6), the extended trading opportunity, in the case of only one partner entering into the negotiation, is:

$$
O (n, \omega_ {i}, v) = \frac {1}{p ^ {\prime}} \left(1 - \prod_ {i = 1} ^ {n} p _ {i} \times \frac {\sum_ {i = 1} ^ {n} p _ {i}}{n}\right)\tag{16}
$$

• Only s partners enter into the negotiation:

Similar to Formula (14), when exactly s number of partners enter the negotiation in the next round, under the independent assumption the aggregated con<sup>fl</sup>ict probability is:

$$
P _ {c} ^ {s} = \prod_ {i = 1} ^ {n} p _ {i} \times p _ {n + 1} \times \dots \times p _ {n + s}\tag{17}
$$

The $p _ { i } ( i \in [ 1 , n ] )$ is known and each new incoming partner's $( s _ { n + k } ,$ $k \in [ 1 , s ] )$ con<sup>fl</sup>ict probability $p _ { n + k }$ can be approximated by $\Sigma _ { i = 1 } ^ { n + k - 1 }$ p<sub>i</sub>/ $\left( n + k - 1 \right)$ (same reason as $p _ { n + 1 } ^ { c } )$ . Thus Formula (17) can be expanded as:

$$
P _ {c} ^ {s} = \prod_ {i = 1} ^ {n} p _ {i} \times \prod_ {k = 1} ^ {s} p _ {n + k} = \prod_ {i = 1} ^ {n} p _ {i} \times \prod_ {k = 1} ^ {s} \frac {\sum_ {i = 1} ^ {n + k - 1} p _ {i}}{n + k - 1}\tag{18}
$$

Therefore, trading opportunity can be rewritten when exactly s partners enter the negotiation, as follows:

$$
O (n, \omega_ {i}, v) = \frac {1}{p ^ {\prime}} \left(1 - \prod_ {i = 1} ^ {n} p _ {i} \times \prod_ {k = 1} ^ {s} \frac {\sum_ {i = 1} ^ {n + k - 1} p _ {i}}{n + k - 1}\right)\tag{19}
$$

It can be seen that when $k = 1 ,$ Formula (19) will be exactly the same as Formula (16).

• At most m partners enter into the negotiation:

When there are at most m partners (the actual number of new incoming partners could be in section $\left[ 0 , m \right] )$ enter into the negotiation in the next round, if the probability of each partner entering the negotiation is $p _ { i n } ,$ then the extended concession factor trading opportunity is:

$$
O (n, \omega_ {i}, v) _ {\text {in}} = \frac {1}{p ^ {\prime}} \sum_ {i = 0} ^ {m} \left[ C _ {m} ^ {i} (p _ {\text {in}}) ^ {i} (1 - p _ {\text {in}}) ^ {m - i} \times \left(1 - \prod_ {j = 1} ^ {n} p _ {j} \times \prod_ {k = 1} ^ {i} \frac {\sum_ {j = 1} ^ {n + i - 1} p _ {j}}{n + i - 1}\right) \right]\tag{20}
$$

where $C _ { m } ^ { i } \left( p _ { i n } \right) ^ { i } \left( 1 - p _ { i n } \right)$ is the probability that exactly i partners enter into the negotiation in the next round. Thus, Formula (20) includes all possible cases when at most m partners are allowed to enter the negotiation in the next round freely.

2) Partners leave off negotiation only:

• Only one partner leaves off the negotiation:

When only one partner, say partner j leaves the negotiation in the next round, according to Formula (5) the aggregated con<sup>fl</sup>ict probability is $\prod _ { i = 1 , ~ i \neq j } ^ { n } p _ { i } .$ . Because any one of the existing partners has the same probability (1/n) to leave off the negotiation, then the aggregated con<sup>fl</sup>ict probability is:

$$
p _ {c} ^ {1} = \sum_ {i = 1} ^ {n} \frac {\prod_ {j = 1 , i \neq j} ^ {n} p _ {j}}{n}\tag{21}
$$

Therefore, according to Formula (6), the extended trading opportunity, in the case of only one partner leaving off the negotiation, is:

$$
O (n, \omega_ {i}, v) = \frac {1}{p ^ {\prime}} \left(1 - \sum_ {i = 1} ^ {n} \frac {\prod_ {j = 1 , i \neq j} ^ {n} p _ {j}}{n}\right)\tag{22}
$$

• Only s partners leave off the negotiation:

When there are exactly s number of (0≤ s ≤ n) partners leaving off the negotiation in the next round, let p be the set of all existing partners in the current round, $\varphi _ { s }$ be the set of leaving partners and $\bar { \varphi } _ { s }$ be the set of staying partners in the next round $\left( \varphi _ { s } \cup \bar { \varphi } _ { s } = \mathbf { p } \right.$ and $\varphi _ { s } \cap \bar { \varphi } _ { s } = \theta )$ . According to Formula (5), the aggregated con<sup>fl</sup>ict probability, when exactly s number of partners (φ ) leave off the negotiation, is $\prod _ { i \in \bar { \varphi } _ { S } } p _ { i \cdot }$ Thus the extended trading opportunity, by considering exactly s number of partners leaving off the negotiation, is:

$$
O (n, \omega_ {i}, v) = \frac {1}{p ^ {\prime}} \left(1 - \sum_ {i = 1} ^ {C _ {n} ^ {s}} \frac {\prod_ {j \in \overline {{\varphi}} _ {s} ^ {i}} p _ {j}}{C _ {n} ^ {s}}\right)\tag{23}
$$

where $C _ { n } ^ { s }$ is the number of possible combinations from the set p with n elements. It can be seen that when $s { = } 1 ,$ , Formula (23) will be exactly the same as Formula (22).

• At most m partners leave off the negotiation:

When there are at most m number of (0≤m≤n) partners leave off the negotiation in the next round (the actual number of leaving partners could be between 0 and n), if the probability of each partner leaving the negotiation is $p _ { \mathrm { o u t } } ,$ then the concession factor trading opportunity is:

$$
O (n, \omega_ {i}, v) _ {\text { out }} = \frac {1}{p ^ {\prime}} \sum_ {i = 0} ^ {m} \left[ C _ {m} ^ {i} (p _ {\text { out }}) ^ {i} (1 - p _ {\text { out }}) ^ {m - i} \times \left(\frac {1 - \sum_ {j = 1} ^ {C _ {m} ^ {i}} \prod_ {k \in \varphi_ {i}} p _ {k}}{C _ {m} ^ {i}}\right) \right]\tag{24}
$$

where $C _ { m } ^ { i } ( p _ { o u t } ) ^ { i } ( 1 - p _ { o u t } ) ^ { m - i }$ is the probability that exactly i number of partners leave the negotiation in the next round. Therefore, Formula (24) includes all possible situations when at most m partners leave off the negotiation.

3) Partners enter into and leave off negotiation freely:

When there are at most m number of partners entering into the negotiation and/or leaving off the negotiation as they wish, the extended trading opportunity, by considering all situations mentioned above (i.e. Formulas (20) and (24)) is:

$$
O (m, \omega_ {i}, v) _ {\mathrm{all}} = O (n, \omega_ {i}, v) _ {\mathrm{in}} \times w _ {\mathrm{in}} + O (n, \omega_ {i}, v) _ {\mathrm{out}} \times w _ {\mathrm{out}}\tag{25}
$$

where $w _ { i n } { \in } [ 0 , ~ 1 ] , ~ w _ { \mathrm { o u t } } { \in } [ 0 , ~ 1 ] ,$ and ${ w _ { \mathrm { i n } } } + { w _ { \mathrm { o u t } } } = 1$ , represent the signi<sup>fi</sup>cance of each individual situation. Usually, both of them are simply assigned as 0.5 to indicate that same attention is paid to both incoming and outgoing changes.

## 3.2. Trading competition

In this subsection, we extend the concession factor of trading competition by following a similar method to extending trading opportunity. There are three cases that need to be considered, namely: (1) only competitors changes; (2) only partners changes; and (3) both competitors and partners change.

## 1) Only competitors change:

In the <sup>fi</sup>rst instance, we will consider the situation when the number of competitors change during the negotiation only.

• At most q competitors enter into the negotiation:

Because of space limitations, we omit a discussion about the situation when only one and exactly q competitors enter the negotiation, and just start from the case when at most q number of competitors enter into the negotiation. Actually, the way to process the <sup>fi</sup>rst two cases is similar to that of extending trading opportunity. So when at most q competitors enter the negotiation, the probability that the agent is considered as the most preferred trader by at least one of their partners (see Section 2.3) is:

$$
C _ {\text { cin }} (m, n) = \sum_ {i = 0} ^ {q} \left[ C _ {q} ^ {i} (p _ {\text { in }}) ^ {i} (1 - p _ {\text { in }}) ^ {q - i} \times \left(1 - \left(\frac {m + i - 1}{m + i}\right) ^ {n}\right) \right]\tag{26}
$$

where $1 - \left( { \frac { m + i - 1 } { m + i } } \right) ^ { n }$ is the factor of trading competition when exactly i $( i \in [ 0 , q ] )$ competitors enter the negotiation

## • At most p competitors leave off the negotiation:

When there are at most p competitors leaving the negotiation, then the probability that the agent is considered as the most preferred trader by at least one partner is:

$$
C _ {\mathrm{cout}} (m, n) = \sum_ {i = 0} ^ {p} \left[ C _ {p} ^ {i} (p _ {\mathrm{out}}) ^ {i} (1 - p _ {\mathrm{out}}) ^ {p - i} \times \left(1 - \left(\frac {m - i - 1}{m - i}\right) ^ {n}\right) \right]\tag{27}
$$

where $1 - \left( { \frac { m - i - 1 } { m - i } } \right) ^ { n }$ is the factor of trading competition when exactly i $( i \in [ 1 , p ] )$ competitors leave off the negotiation.

• Competitors enter into and leave off the negotiation freely:

Based on the considerations about the two situations mentioned above (see Formulas (26) and (27)), when competitors are allowed to enter into and leave off the negotiation freely, the trading competition is represented as:

$$
C _ {c} (m, n) = C _ {\text { cin }} (m, n) w _ {\text { in }} + C _ {\text { cout }} (m, n) w _ {\text { out }}\tag{28}
$$

where $w _ { \mathrm { i n } }$ and $w _ { \mathrm { o u t } }$ are weights. The default values are 0.5 for equal weighting.

2) Only partners change:

In the second stage, we keep the number of competitors unchanged, but take into account the situation when the number of partners change.

• At most w partners enter into the negotiation:

When there are at most w partners entering the negotiation, then the probability that the agent is considered as the most preferred partner by at least one partner is:

$$
C _ {\mathrm{pin}} (m, n) = \sum_ {i = 0} ^ {w} \left[ C _ {w} ^ {i} (p _ {\mathrm{in}}) ^ {i} (1 - p _ {\mathrm{in}}) ^ {w - i} \times \left(1 - \left(\frac {m - 1}{m}\right) ^ {n + i}\right) \right]\tag{29}
$$

where $1 - \left( { \frac { m - 1 } { m } } \right) ^ { n + i }$ is the factor of trading competition when exactly i partners enter the negotiation.

• At most v partners leave off the negotiation:

When there are at most v partners leaving off the negotiation, the concession factor of trading competition is:

$$
C _ {p \text {out}} (m, n) = \sum_ {i = 0} ^ {v} \left[ C _ {v} ^ {i} (p _ {\text {out}}) ^ {i} (1 - p _ {\text {out}}) ^ {v - i} \times \left(1 - \left(\frac {m - 1}{m}\right) ^ {n - i}\right) \right]\tag{30}
$$

where $1 - \left( { \frac { m - 1 } { m } } \right) ^ { n - i }$ is the factor of trading competition when exactly i partners leave off the negotiation.

## • Partners enter into and leave off the negotiation freely:

Based on the two considerations mentioned above (see Formulas (29) and (30)), by considering the change of partners only, the concession factor of trading competitor is:

$$
C _ {p} (m, n) = C _ {\text { pin }} (m, n) w _ {\text { in }} + C _ {\text { pout }} (m, n) w _ {\text { out }}\tag{31}
$$

where $w _ { \mathrm { i n } }$ and $w _ { \mathrm { o u t } }$ are weights. The default values are 0.5 for equal weighting.

## 3) Both competitors and partners change:

In the last stage, we combine all situations together and allow both competitors and partners to change freely. Then the probability that the agent is considered as the most preferred trader by at least one of their partners is:

$$
C (m, n) = C _ {c} (m, n) w _ {c} + C _ {p} (m, n) w _ {p}\tag{32}
$$

where $C _ { c } \left( m , n \right)$ is de<sup>fi</sup>ned by Formula $( 2 8 ) , C _ { p } \ : ( m , n )$ is de<sup>fi</sup>ned by Formula (31), and $w _ { c }$ and $w _ { p }$ are the weights on each term.

## 3.3. Trading time and strategy

In this subsection, the concession factor trading time and strategy is extended by considering changes of the parameter λ. According to the explanation of λ (see Formula (10)), the bigger the value of λ, the smaller the concession agents will give in the early negotiation round, and the larger the concession agents will give in the later negotiation round, and vice versa. Furthermore, if the value of concession factors of trading opportunity and trading competition changes, the amount of concession should also be changed. Therefore, the parameter λ should be determined by both trading opportunity and trading competition. Accordingly, the extended trading time and strategy is:

$$
T (t, t ^ {\prime}, \tau , \lambda_ {t}) = \frac {1 - \left(\frac {t ^ {\prime}}{\tau}\right) ^ {\lambda_ {t ^ {\prime}}}}{1 - \left(\frac {t}{\tau}\right) ^ {\lambda_ {t}}}\tag{33}
$$

where $\lambda _ { t }$ is calculated by:

$$
\lambda_ {t} = \lambda_ {0} \times O _ {t} (n, \omega_ {i}, v) \times C _ {t} (m, n)\tag{34}
$$

where the $\lambda _ { 0 }$ is the initial value of the concession, and is assigned by the user. $O _ { t } \left( n , \omega _ { i } , v \right)$ is the factor of trading competition at negotiation round t (see Formula (32)), and $C _ { t }$ (m, n) is the factor of trading opportunity at negotiation round t (see Formula (25)). Formula (34) indicates that when the number of partners is greater than the number of competitors during a negotiation (positive to the agent), in order to maximize its pro<sup>fi</sup>t, the agent should decrease its concession. However when the number of partners is less than the number of competitors, the agent should give more concession in order to keep its partners.

## 3.4. Eagerness

In this subsection, the concession factor of eagerness is extended by considering changes in the negotiation environment. The general idea of the extension is that: according to economists, people's eagerness to complete a trade should be directly related to their bene<sup>fi</sup>ts. So it is proposed to extend eagerness by considering agents' bene<sup>fi</sup>ts. In each negotiation round, when an agent's bene<sup>fi</sup>ts are changed by partners offers, the agent's eagerness to reach an agreement should also be changed. Let br $( \mathrm { b r } _ { t } > 0 )$ denote the ratio between an agent's maximal bene<sup>fi</sup>ts in two conjoint negotiation rounds, so $ { \mathrm { b r } } _ { t }$ can be calculated as:

$$
\mathrm{br} _ {t} = \frac {\mathrm{mb} _ {t}}{\mathrm{mb} _ {t ^ {*}}}\tag{35}
$$

where mb is the agent's maximal bene<sup>fi</sup>t in the current round, and mb is the maximal bene<sup>fi</sup>t in the last round. Both mb and mb can be easily gained from the negotiation records. Then the factor of trading eagerness is extended as:

$$
E (\varepsilon_ {t}) = 1 - \varepsilon_ {t}\tag{36}
$$

where

$$
\varepsilon_ {t} = \left\{ \begin{array}{l l} \varepsilon_ {0} & t = 0 \\ \varepsilon_ {t - 1} \times \mathrm{br} _ {t} & t > 0 \end{array} \right.\tag{37}
$$

where $\varepsilon _ { 0 }$ is the initial value of eagerness and is assigned by the user. From Formulas (37) and (35), it can be seen that the more bene<sup>fi</sup>ts the agent gains than the last negotiation round, the more eagerness that the agent wants to reach an agreement for the negotiation. For example, when $\mathsf { b r } _ { t } { > } 1$ , it indicates that the agent's bene<sup>fi</sup>t is increased in the current round, so the agent will have more eagerness to complete the trading; when $0 < \mathsf { b r } _ { t } < 1$ , it indicates that the agent's bene<sup>fi</sup>t is decreased in the current round, so the agent will decrease its eagerness to complete the trading; and when br =1, it indicates that the agent's bene<sup>fi</sup>t does not change in the current round, so the agent will not change its eagerness. The purpose of this updating strategy on $\varepsilon _ { t }$ is to help agents modify its eagerness as the negotiation environment changes.

In this section, we introduced the extended MDAs model by considering the dynamic changes of the negotiation environment. By comparison with the original MDAs model, each concession factor has been extended as follows:

## • Trading opportunity

By employing the extended MDAs model, the agent calculates the trading opportunity in the current negotiation round, and can also handle changes of trading opportunity. The agent can handle the opportunity of completing the negotiation in future rounds. Then the agent can modify its negotiation strategy in order to maximize self pro<sup>fi</sup>ts and ensure an agreement can be achieved successfully as well.

## • Trading competition

The agent can handle the future situations of competition in the dynamic negotiation environment. In multi-lateral negotiation, competition is a very signi<sup>fi</sup>cant issue, and impacts on both the negotiation strategy and the result. By employing the extended MDAs model, an agent can gain more advantages during competitions.

## • Trading time and strategy

In the original MDAs model, the agent's negotiation strategy is prede<sup>fi</sup>ned by the client and will not be changed throughout the negotiation. However, in an open and dynamic negotiation environment, a constant negotiation strategy cannot respond to changes of the environment, so the agent may face loss of pro<sup>fi</sup>ts or negotiation partners. In the extended MDAs model, we improve this factor and agents are allowed to modify their negotiation strategies according to a changing environment. Therefore, the agent will get more advantages in open and dynamic negotiation by employing the extended MDAs model rather than the original MDAs model;

## • Eagerness

In the original MDAs model, the eagerness of an agent to complete a negotiation is also prede<sup>fi</sup>ned by the client. However, in reality, an agent's eagerness to complete the negotiation should be impacted by the negotiation environment and the bene<sup>fi</sup>ts the agent can gain. Usually, agents prefer the trading of higher bene<sup>fi</sup>ts. So in the extended MDAs model, we take account of this situation and allow an agent to modify its eagerness as the negotiation environment changes.

## 4. Experiments

In this section, we illustrate our experimental results based on each of the four concession factors. These are trading opportunity (see Section 4.2), trading competition (see Section 4.3), trading time and strategy (see Section 4.4) and eagerness (see Section 4.5). In Section 4.6, experimental results by combining all concession factors are illustrated.

## 4.1. Setup of experiments

Firstly, we brie<sup>fl</sup>y introduce the setup of our experiments:

1) Negotiation participators are divided into two types, namely “partnersq and “competitorsq; the initial numbers for both are 5.

2) The maximum number of agents that can enter or leave the negotiation is between 0 and 5, which is from 0% to 100% of the initial number.

3) The probability that an agent will enter into or leave off the negotiation is assigned to 0.5.

4) The maximum negotiation round is assigned to 10.

5) It is only assumed that both the number of partners and number of competitors are always greater than 0; there is no assumption about agents' strategies and protocols.

## 4.2. Experiment 1: Trading opportunity

According to Section 3.1, the concession factor trading opportunity only considers changes of partners. In this subsection, experiments are illustrated to test the performance of the proposed extension approach on trading opportunity.

## • Partners can only enter into the negotiation:

In this experiment, partners are only allowed to enter the negotiation. The experimental results are displayed in Fig. 3. The xaxis indicates the negotiation round, while the y-axis is the value of trading opportunity. The higher the value of trading opportunity, the more possibility that agents can <sup>fi</sup>nish the negotiation. When only one partner (10% of initial partners) enters the negotiation, the negotiation success rate increases signi<sup>fi</sup>cantly. As the number of entering partners increases, the success rate also increases. However, the increment becomes slow. The reason is that no matter how many prospective partners exist, only one agreement can be reached with one partner. Therefore, it is noticed that there is a bottleneck between the number of prospective partners and the negotiation success rate. When the number of prospective partners is higher than a threshold (60% of initial partners), its effect will not be so signi<sup>fi</sup>cant as it used to be. In this case, agents have to seek another approach to increase their negotiation success rate. Furthermore the experimental result indicates that in a negotiation, especially in an open and dynamic environment, agents do not need to undertake a comprehensive investigation of all prospective partners. A reasonable search for prospective partners within the local society is adequate to keep the negotiation success rate at a desirable level.

![](/api/attachments/NDTEY7P6/fulltext/images/2cab016601b8cfbd3feac007781028e42da3a5e45161481c40cf12138ce03456.jpg)  
Fig. 3. Trading opportunity when partners enter freely

![](/api/attachments/NDTEY7P6/fulltext/images/21cb89b6c9561de5927ce02fa1432be93533fcb3888c6b4a78ebb91b428cd0b1.jpg)  
Fig. 4. Trading opportunity when partners leave freely.

## • Partners can only leave off the negotiation:

In this experiment, partners are only allowed to leave off the negotiation. The experimental results are displayed in Fig. 4. It can be seen that as the number of leaving partners increases, the negotiation success rate keeps decreasing. When only one partner (10% of initial partners) leaves the negotiation, the negotiation success rate decreases by more than one third. As the number of leaving prospective partners increases, the negotiation success rate drops quickly. When the number of leaving partners is larger than three (60% of initial partners), the success rate decreases very little compared to the original one. Therefore, the experimental result indicates that in order to ensure the success of the negotiation, agents should keep the number of prospective partners to a reasonable level.

## • Partners can enter into and leave off the negotiation:

In this experiment, partners can enter into and leave off the nego tiation freely. In Fig. 5, it can be seen that as the number of entering and leaving prospective partners increases, the negotiation success rate decreases. However, even for the most complex situation, at most <sup>fi</sup>ve prospective agents (100% of initial partners) can enter and leave the negotiation freely, the decrease in negotiation success rate is only 10%. This experimental result indicates that in an open and dynamic environment, when the number of prospective partners <sup>fl</sup>uctuates, negotiation success will be impacted only minimally. The reason could be that (1) when the new incoming partners replace existing ones, the uncertainty of the new incoming partner's bids will impact on the negotiation success rate; and (2) since competitors also exist during the negotiation, the new incoming partners may have more interest in other competitors. Therefore, the experimental result indicates that the <sup>fl</sup>uctuation of the environment may have very little impact on the negotiation success rate. In order to maintain the success rate, agents should retain their prospective agents as much as they can.

![](/api/attachments/NDTEY7P6/fulltext/images/64513ba88ff89826740e3745b6b1bc96a5a1d6badc671618bd0cc8e87a82220b.jpg)  
Fig. 5. Trading opportunity when partners enter and leave freely.

According to the experimental results in this subsection, it can be seen that the proposed approach successfully handle uncertainties in the negotiation environment, and helps agents to update their negotiation strategies to increase the negotiation success rate.

## 4.3. Experiment 2: Trading competition

According to Section 3.2, both partners and competitors can impact on the value of trading competition. Therefore, we tested the extended approach on trading competition by considering changes on both partners and competitors.

## 1) Considering partners only:

In this part, only changes of partners is considered, and the number of competitors is kept as a constant.

## • Partners can only enter into the negotiation

In this experiment, partners are only allowed to enter the negotiation. The experimental results are displayed in Fig. 6. The higher the value of trading competition, the less competition the agent will meet during negotiation. In Fig. 6, it can be seen that as the number of prospective partners increases, the agent will face less competition during the negotiation. When two prospective partners (40% of initial partners) enter the negotiation, the value of trading competition is increased by more than 50%. However, when the number of incoming partners is bigger than three (60% of initial partners), the value of trading competition is not increased signi<sup>fi</sup>- cantly. This experiment result is very similar to the experiment on trading opportunity. It indicates that when the number of prospective partners is bigger than a threshold, the increase in the number of partners will have little impact on agent competition. In this case, the method of eliminating existing competitors will have more effect on decreasing agents' competition in the negotiation.

![](/api/attachments/NDTEY7P6/fulltext/images/4fe009faa5948a60f8960c75863aa37fc43bb0916c1adcdad55c3b0bf682713e.jpg)  
Fig. 6. Trading competition when partners enter freely.

![](/api/attachments/NDTEY7P6/fulltext/images/12ed44df47525853cc1cd733931b14cd3fb1cfeebdc6ba592fa73bc74d66a914.jpg)  
Fig. 7. Trading competition when partners leave freely.

## • Partners can only leave off the negotiation

In this experiment, partners are only allowed to leave the negotiation. The experimental results are displayed in Fig. 7. It can be seen that as the number of prospective partners decreases, agents will face more competition during the negotiation. In general, each 20% loss of prospective partners will increase similar pressure on agent competition.

## • Partners enter into and leave off the negotiation

In this experiment, partners can enter and leave the negotiation freely. In Fig. 8, it can be seen that as the number of prospective partners <sup>fl</sup>uctuates, the agent's competition will increase slightly on average, but will also <sup>fl</sup>uctuate. The more changes in the negotiation environment, the more <sup>fl</sup>uctuation will occur. Also this experiment obtains a similar result as the experiment on trading opportunity, which is that <sup>fl</sup>uctuation of perspective partners in the negotiation environment has very little impact on agent competition during negotiation.

## 2) Considering competitors only:

In this part, only changes of competitors are considered; the number of partners remains constant.

![](/api/attachments/NDTEY7P6/fulltext/images/114f47a1d8983b4e154d026efba5cb750a6462126bbd3469b3a09cfa751b206f.jpg)  
Fig. 8. Trading competition when partners enter and leave freely.

![](/api/attachments/NDTEY7P6/fulltext/images/9d5df55b7f7d3475112b891f4efb52b39a349219457573aa17735f0bb14541c9.jpg)  
Fig. 9. Trading competition when competitors enter freely.

## • Competitors can only enter into the negotiation

In this experiment, competitors are only allowed to enter the negotiation. The experimental results are displayed in Fig. 9, which indicates that the more competitors that enter the negotiation, the more competition agents will face. A 40% increase in the number of competitors can increase competition by more than 50% during negotiation.

## • Competitors can only leave off the negotiation

In this experiment, competitors are only allowed to leave the negotiation. The experimental results are displayed in Fig. 10. They indicate that as the number of competitors decreases, the competition between agents also decreases. Each 20% loss of the number of competitors will release agents' pressure to a similar level.

## • Competitors enter into and leave off the negotiation

In this experiment, competitors can enter and leave the negotiation freely. The experimental results are displayed in Fig. 11. In contrast to the experimental results on partners, the <sup>fl</sup>uctuation on the number of competitors has considerable impact on agent competition. The more competitors that are allowed to enter and leave the negotiation freely, the less competition agents will meet during the negotiation. The leaving competitors can release pressure immediately, but the incoming competitors cannot exert more pressure to the existing agents in a short time. Therefore, changes in the number of competitors can take bene<sup>fi</sup>ts to both the negotiation participators and the whole market.

![](/api/attachments/NDTEY7P6/fulltext/images/6417bb6c6e7a3919dbce65840039b01eb7b6c52983f836f46f8be877796ebc2b.jpg)  
Fig. 10. Trading competition when competitors leave freely.

![](/api/attachments/NDTEY7P6/fulltext/images/013f8499e470cc20e9e73986e2597c70a022bd312ed82a2e5977d33a189b0027.jpg)  
Fig. 11. Trading competition when competitors enter and leave freely.

## 3) Considering both partner and competitor:

In this part, both changes of partners and competitors are considered. As shown in Fig. 12, when both partners and competitors can enter and leave during the negotiation freely, the values of trading competition <sup>fl</sup>uctuate relatively to the original value. The more changes of negotiation participators, the more complex the situation will be and the bigger the <sup>fl</sup>uctuation. It can be seen that our experimental results, which indicate the relationship between negotiation environment and agent pressure, are reasonable. This relationship can be employed by agents to modify their negotiation strategies when the negotiation environment changes.

## 4.4. Experiment 3: Trading time and strategies

According to Section 3.3, both the number of partners and competitors can impact on the value of trading time and strategy. What is more, the values of trading time and strategy are also dependent on the parameter λ and the remaining time. Therefore, we test the proposed approach in terms of changes of partners and competitors respectively.

## 1) Considering partners only

In this part, only changing of partners is considered, and not the changing of competitors

## • Partners can only enter into the negotiation

In this experiment, partners are only allowed to enter the negotiation. The experimental results are displayed in Fig. 13. The xaxis indicates the negotiation time, while the y-axis is the value of λ (see Section 2.4). The higher the value of λ, the less concession the agent will be made in the early round, and conversely. As shown in Fig. 13, when the number of prospective partners increases, much less concession will be made in the early rounds. That is because the agents' trading opportunity is increased and trading competition is decreased. Therefore agents make a decision to decrease their concession in order to enlarge their bene<sup>fi</sup>ts. The more prospective partners that enter the negotiation, the less concession the agent concedes.

![](/api/attachments/NDTEY7P6/fulltext/images/c5710b11e3cafa7ee2b468777de6510614e3c918866f364d638ead9024ccefb1.jpg)  
Fig. 12. Trading competition when both partners and competitors enter and leave freely.

![](/api/attachments/NDTEY7P6/fulltext/images/f116a0d0a30f991d0dddd7aedb077982e4c3ac460a03e9ff357c252b6bc7bc40.jpg)  
Fig. 13. Trading strategy when partners enter freely.

## • Partners can only leave off the negotiation

By contrast, while partners are only allowed to leave the negotiation, agents should enlarge their concession in order to increase the negotiation success rate. The experimental results are displayed in Fig. 14. It can be seen that as the number of prospective partners decreases, much larger concession will be made during the early rounds.

## • Partners can enter into and leave off negotiation

In this experiment, partners can enter into and leave off the negotiation freely. The experimental results are displayed in Fig. 15. It can be seen that as the number of prospective partners <sup>fl</sup>uctuates, the value of λ will be slightly decreased. The reason for this is that when the number of prospective partners is changed, the agent's trading opportunity is decreased (see experiments on trading opportunity) and its trading competition is increased (see experiments on trading competition). Therefore agents have to enlarge their concession to respond to such changes.

![](/api/attachments/NDTEY7P6/fulltext/images/c8b816cdbbddd100ca9b4fa7d35d77c5ce02879f3449fd9fd002c25aec428674.jpg)  
Fig. 14. Trading strategy when partners leave freely.

![](/api/attachments/NDTEY7P6/fulltext/images/3d13e0ac9cf94925ec018f7a154b2b5c680e06c8558be8de30033ef1c0ad31b1.jpg)  
Fig. 15. Trading strategy when partners enter and leave freely.

## 2) Considering competitors only

In this part, only changes of competitors is considered, not changes of partners.

## • Competitors can only enter into the negotiation

In this experiment, competitors are only allowed to enter the negotiation. In Fig. 16, it can be seen that the results are very similar to the situation when partners are only allowed to leave the negotiation freely. When the total number of competitors increases, agents tend to enlarge their concession from the early negotiation round.

## • Competitors can only leave off the negotiation

In this experiment, competitors are only allowed to leave the negotiation. In Fig. 17, it can be seen that as the total number of competitors decreases, agents tend to give less concession during the early rounds of the negotiation. This is very similar to the situation when prospective partners are allowed to enter the negotiation freely.

## • Competitors enter into and leave off the negotiation

When competitors can enter and leave the negotiation freely, the experimental results are displayed in Fig. 18. It can be seen that as the total number of competitors <sup>fl</sup>uctuates, agents will increase the value of λ and decrease their concession from the early round. Similar to the experiments on trading competition, the explanation of these results is that the leaving competitors can release the pressure from agents immediately, but incoming competitors cannot take more pressure to agents in the short term. Therefore, agents tend to decrease their concession level.

![](/api/attachments/NDTEY7P6/fulltext/images/db1ce4282c3610735bac1e2c0b2760cc4aab02d53682d3bb11d0252a8db3c26a.jpg)  
Fig. 16. Trading strategy when competitors enter freely.

![](/api/attachments/NDTEY7P6/fulltext/images/8c2057609e1aa4e31a5b3d04ceab3c6496687b9ee34c47b0a2fbadd149673c7c.jpg)  
Fig. 17. Trading strategy when competitors leave freely.

## 3) Considering both partner and competitor

In this part, changes of both partners and competitors are considered. As shown in Fig. 19, when both partners and competitors can enter and leave the negotiation freely, agents' strategies on the amount of concession also <sup>fl</sup>uctuate relatively to their initial values. The more changes in the number of participators, the bigger the <sup>fl</sup>uctuation will be. Therefore, in an open and dynamic environment, agents need a proper approach to estimate the potential changes of the negotiation environment and to make reasonable responses.

## 4.5. Experiment 4: Eagerness

In this subsection, we perform experiments to test the proposed approach on eagerness. According to Section 3.4, the value of eagerness will be impacted by bene<sup>fi</sup>t ratio br . In order to simplify the experiment, we set br to 0.5, 1 and 2 respectively, and compare the experimental results. In fact, the value of $ { \mathbf { b r } } _ { t }$ is changed dynamically in each negotiation round.

In Fig. 20, it can be seen that as the value of bene<sup>fi</sup>t ratio increases, the value of eagerness also increases and the agents are more eager to <sup>fi</sup>nish the negotiation. Therefore, it can be seen that the proposed approach successfully adjusts the value of eagerness according to agents' negotiation environment.

## 4.6. Experiment 5: Combining all factors

In this subsection, we illustrate the experimental results by combining all concession factors in Fig. 21. It can be seen that when only 1 (i.e., 20%) or 2 (i.e., 40%) negotiation participator/s enters/enter into or leaves/leave off the negotiation freely, the agent can decrease its concession by comparison with original MDAs. The reason behind this result is that when few negotiation participators can enter into or leave off the negotiation freely, the agent will get more chances to <sup>fi</sup>nd a ‘better’ negotiation partner. Even though the existing negotiation partner may leave off the negotiation as well, the negotiation partners with higher opportunity may not leave off the negotiation, so the agent will not be impacted too much from existing partners' leaving. On the other hand, pressure from the negotiation competitors is not so heavy because as shown in Fig. 8, when at most 1 (i.e., 20%) or 2 (i.e., 40%) competitor/s enters/enter into or leaves/leave off the negotiation freely, the agent will not get too much competition in the environment. However, when there are more than 3 (i.e., 60%) negotiation participators who enter into or leave off the negotiation freely, the situation changes. The agent has to face more pressure from competitors, and the existing partners with higher opportunity may also leave off the negotiation, so in order to ensure that the negotiation can reach an agreement, the agent has to increase its concession. It can be seen from the curve that for each increment (10% of all negotiation participators) on the changing on negotiation participator's number, the agent has to increase its concession value by 10% of its maximum concession on average. At the extreme, when at most 5 participators can enter into or leave off the negotiation, the agent has to make 20% more concession to its negotiation partners compared with the original MDAs in order to ensure that negotiation agreement can be reached successfully.

![](/api/attachments/NDTEY7P6/fulltext/images/7b6f5c2e9f06d2a1d89fc28acf2e1b74c430f9603eb7f02333956e6b260c69b8.jpg)  
Fig. 18. Trading strategy when competitors enter and leave freely.

![](/api/attachments/NDTEY7P6/fulltext/images/2ba8d516d463ca5775c4623a5611a4f45b9ef1021ba3f7f15152cfa65d8bec83.jpg)  
Fig. 19. Trading strategy when both partners and competitors enter and leave freely

![](/api/attachments/NDTEY7P6/fulltext/images/ca3dfc4fc012727945a7c14a7be4484fe3a69932211d99d687d5f24e5c2bfe9c.jpg)

![](/api/attachments/NDTEY7P6/fulltext/images/15ff9f972b9856e7345d413df3a00c9cadfb8dd35506c747b8cd763344a31d77.jpg)  
Fig. 21. Combine all factors.

In this section, we illustrate the experimental results on each individual concession factors, as well as the combined factor. In general, from the experimental results, it can be seen that when less than 40% of negotiation participators may enter into or leave off the negotiation, the agent's negotiation strategy does not necessarily need much updating. Furthermore, a little change of the negotiation environment may make some advantages to most negotiation participators. However, when more than 40% of negotiation participators may enter into or leave off the negotiation, the agent has to modify its strategy in order to reach an agreement. Usually, a big change in the negotiation environment has a negative impact on most negotiation participators.

## 5. Related work

Some related works also take into account the relationship between negotiators' behaviors and the negotiation environment. This section discusses the differences between these related works and our work.

He et al. [12] proposed a very successful model for trading agents in solving issues in supply chain management. Firstly, the customer agent in their model collected customer requests and sorted them by agent's pro<sup>fi</sup>ts gained from each customer. Then according to customers' requirements, such as type of item, reserved price, penalty and due time, the customer agent makes a decision about the order of servers. In order to increase the trading agent's pro<sup>fi</sup>t, the component agent predicts customers' requests in both the near term and distant future. According to the prediction results, the trading agent keeps its own inventory in an appropriate level in order to ensure that adequate components can be provided for daily regular offers, as well as minimize the storage expenditure. Finally, by employing the prediction results and fuzzy reasoning, the trading agent can successfully handle issues of offer generation, components booking and assembly, and PCs delivery. One signi<sup>fi</sup>cant difference between He's model and our proposed model is that in the former model, competitions from other trading agents are not taken into account. By contrast, in our proposed model, we consider both trading opportunity and competition in real time. Therefore, He's model is very suitable to solve issues in supply chain management, while our model can yield ef<sup>fi</sup>ciencies in dynamic multilateral bargaining.

Sycara et al. [15] proposed a model for bilateral negotiation by considering uncertain and dynamic outside options. It is argued that the outside options can impact agents' negotiation strategies. According to the complexity of outside options in negotiation, normal negotiation is further divided into three levels, these being single-thread negotiation, synchronized multi-thread negotiation and dynamic multi-thread negotiation. Single-thread negotiation is only processed between two agents without outside options. Synchronized multi-thread negotiation is based on the single-thread negotiation model, and also considers concurrently existing outside options. Dynamic multi-thread negotiation is expanded from synchronized multi-thread negotiation by considering uncertain outside options which may occur dynamically in the future. Sycara's model gives a very novel classi<sup>fi</sup>cation and description on general negotiation. The approach proposed in this paper focuses on solving issues in dynamic multi-thread negotiation, and extending the MDAs model by considering uncertain and dynamic outside options.

Seghrouchni and Cartault [21] proposed a model to control multiagent's plans in dynamic aircraft simulation. In order to guide agent's plans and behaviors, a comprehensive state map is given by the system designer which lists all possible situations during the simulation. Then each agent should <sup>fi</sup>nd a local optimal path from its initial state to its goal. The selection is constrained by its partially ordered task and the resources. Finally, all local paths are synchronized to generate a feasible map from the initial state to the global goal. This approach is suited to work in environments where the number of steps from the initial state to the goal is not very large. However, in the real world, when the environment is open and dynamic, this approach cannot be widely employed because of this limitation. In our proposed approach, we do not restrict agents' behaviors. All concession factors are real-time and dynamic. Therefore, compared to Seghrouchni and Cartault's work, our proposed approach is more suitable for use in dynamic and unpredictable environments.

Brzostowski and Kowalczyk [1] proposed a non-linear regression approach to model negotiators behaviors based on previous offers. According to agents' strategies in the negotiation, such as time dependency, behavior dependency and imitation dependency, the authors gave different solutions. For a given strategy, through analyzing the history of offers, the proposed functions can predicate opponents' behaviors and generate corresponding counter-offers. Compared to this work, our proposed approach has the following merits: (1) agents do not need to record previous offers; all predictions are based on the current situation of the negotiation environment. (2) our strategies still work well even without others' strategy information. And (3) our proposed approach can handle uncertainties in dynamic environments based not only on negotiation partners' behaviors, but also taking into account negotiation competitors' behaviors.

Gal and Pfeffer [6] proposed a statistical learning approach to predict people's bidding behaviors in negotiation. The authors proposed several algorithms for learning from the collected data. However, all of the proposed algorithms can only work in bilateral negotiation and also make the assumption that the negotiation does not contain any outside option. Our work can perform multi-lateral negotiation, with no such limitation.

Dasgupta and Hashimo [4] proposed an approach to address the problem of dynamic pricing in a competitive online economy where a product is differentiated by buyers and sellers on multi-issue. Agents may have incomplete knowledge of the negotiation parameters. A seller employs a collaborative <sup>fi</sup>ltering algorithm to determine temporal consumer's purchase preferences and a dynamic pricing algorithm to determine a competitive price for the product. The limitation of this work is that it only pays attention to the seller, but does not consider the situation of the buyer. In this paper, the proposed strategies are suitable to be applied on both sellers and buyers.

Gregg and Walczak [7] proposed a decision support system for online-auction. Besides buyer agents and seller agents, authors also created several assistant agents, such as information retrieval agents, data-analysis agents and information agents, to help auction participants to improve the quality of their decision making. The assistant agents can ef<sup>fi</sup>ciently collect data related to the online auction, make further statistical calculations and recommendations for the auction, and generate additional auction rules by using data mining strategies. Both simulated and real purchases at online auction indicate the bene<sup>fi</sup>t that auction participants achieve by employing this auction advisor system.

By comparing with the above related works, the contributions of the proposed approach are as follows. (1) It can work under open and dynamic negotiation environments. (2) The proposed approach does not have any restriction on agent negotiation protocols; it can be employed by agents with different negotiation protocols (e.g., double action). (3) The proposed approach does not have any restriction on either agent's number or issue's number, so it can be used in the multiissue negotiation and multi-lateral negotiation.

## 6. Conclusion and future work

In this paper, four concession factors in MDAs (namely trading opportunity, trading competition, trading time and strategy and eagerness) are modi<sup>fi</sup>ed by taking into account uncertain and dynamic outside options. In an open and dynamic negotiation environment, negotiators are allowed to enter and leave a negotiation freely. Through analyzing the uncertain negotiation environment, the proposed approach can generate reasonable decisions to update agents' strategies in a dynamic environment. The experimental results also illustrate both the ef<sup>fi</sup>ciency and accuracy of the proposed approach.

In the future work, we are going to pursue more studies on multi issue negotiation, because both the number of negotiation issues and agents' preferences will impact agents' attitudes to make concession during the negotiation. Also when the negotiation environment changes, agents' preferences will likely change. Therefore, we are trying to capture this fact and extend our approach by considering agents' preferences on each negotiation issue as the environment changes.

## Acknowledgement

K. M. Sim gratefully acknowledges <sup>fi</sup>nancial support by the Hong Kong Baptist University for funding Minjie Zhang's visit in 2006 under project code: FRG/05-06/II-30. Also we would like to thank Prof. John Fulcher from the University of Wollongong and all the reviewers for their insightful suggestions and valuable comments to improve the quality of this paper. This research is partially supported by a university postgraduate scholarship from the University of Wollongong.

## References

[1] J. Brzostowski, R. Kowalczyk, Predicting Partner's Behaviour in Agent Negotiation, 5th International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS 2006) ACM Hakodate, Japan May 2006 pp. 355–361.

[2] A. Chavez, D. Dreilinger, R. Guttman, P. Maes, A real-life experiment in creating an agent marketplace, Lecture Notes in Computer Science 1198 (2) (2001) 160–179.

[3] A. Chavez, P. Maes, Kabash: An Agent Marketplace for Buying and Selling Goods, First International Conference on the Practical Application of Intelligent Agents and Multi-Agent Technology (PAAM'96), Practical Application Company, London, U. K., 1996, pp. 75–90.

[4] P. Dasgupta, Y. Hashimoto, Multi-attribute Dynamic Pricing for Online Markets Using Intelligent Agents, 3rd International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS 2004), ACM, New York, USA, July 2004, pp. 277–284.

[5] S. Fatima, M. Wooldridge, N. Jennings, An agenda-based framework for multi-issue fi <sub>–</sub>

[6] Y. Gal, A. Pfeffer, Predicting Peoples Bidding Behavior in Negotiation, 5th International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS 2006, ACM, Hakodate, Japan, May 2006, pp. 370–376.

[7] D. Gregg, S. Walczak, Auction advisor: an agent-based online-auction decision support system, Decision Support Systems 41 (2) (2006) 449–471.

[8] A. Gupta, B. Su, Z. Walter, Risk pro<sup>fi</sup>le and consumer shopping behavior in electronic and traditional channels, Decision Support Systems 38 (3) (2004) 347–367.

[9] R. Guttman, P. Maes, Cooperative vs. Competitive Multiagent Negotiations in Retail Electronic Commerce, Proc. 2nd Int. Workshop on Cooperative Information Agents (CIA'98), July 1998, pp. 135–141, Paris, France.

[10] R. Guttman, P. Maes, Agent-mediated integrative negotiation for retail electronic commerce, Lecture Notes in Computer Science 1571 (2) (1999) 70–90

[11] M. He, N. Jennings, H. Leung, On agent-mediated electronic commerce, IEEE Transaction on Knowledge and Data Engineering 15 (4) (2003) 985–1003.

[12] M. He, A. Rogers, X. Luo, N. Jennings, Designing A Successful Trading Agent for Supply Chain Management, 5th International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS 2006), ACM, Hakodate, Japan, May 2006, pp.1159–1166.

[13] N. Jennings, P. Faratin, A. Lomuscio, S. Parsons, C. Sierra, M. Wooldridge, Automated negotiation: prospects, methods, and challenges, International Journal of Group Decision and Negotiation 10 (2) (2001) 199–215.

[14] C. Li, J. Giampapa, K. Sycara, Bilateral negotiation decisions with uncertain dynamic outside options. IEEE Transactions on Systems, Man and Cybernetics. Part C Applications and Reviews 36 (1) (2006) 31–44.

[15] C. Li, K. Sycara, J. Giampapa, Dynamic Outside Options in Alternating-offers Negotiations, HICSS, IEEE Computer Society, 2005, pp. 1–10.

[16] A. Lomuscio, M. Wooldridge, N. Jennings, A classi<sup>fi</sup>cation scheme for negotiation in electronic commerce, International Journal of Group Decision and Negotiation 12 (1) (2003) 31–56.

[17] X. Luo, N.R. Jennings, N. Shadbolt, H. Leung, J.H. Lee, A fuzzy constraint based model for bilateral multi-issue negotiations in semi-competitive environments, Arti<sup>fi</sup>cial Intelligence Journal 148 (1–2) (2003) 53–102.

[18] F. Ren, K. Sim, M. Zhang, Market-Driven Agents with Uncertain and Dynamic Outside Options, Sixth International Joint Conference on Autonomous Agents and Multi-Agent Systems (AAMAS07), IFAAMAS, Honolulu, Hawaii, May 2007, pp. 721–723.

[19] J. Rodríguez-Aguilar, F. Martín, P. Noriega, P. Garcia, C. Sierra, Toward a testbed for trading agents in electronic auction markets, AI Communications: European Journal on Arti<sup>fi</sup>al Intelligence 11 (1) (1998) 5–19.

[20] J. Rosenschein, G. Zlotkin, Rules of Encounter: Designing Conventions for Automated Negotiation Among Computers, MIT Press, Cambridge, MA, 1994.

[21] A. Seghrouchni, I. Cartault, F. Marc, Modelling, Control and Validation of Multi-Agent Plans in Dynamic Context, 3rd International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS 2004), ACM, New York, USA, July 2004, pp. 44–51.

[22] K. Sim, A Market-driven Model for Designing Negotiation Agents, Computational Intelligence, Special issue in Agent Technology for E-commerce 18 (4) (2002) 618–637

[23] K. Sim, Negotiation Agents that Make Prudent Compromises and are Slightly Flexible in Reaching Consensus, Computational Intelligence, Special issue on Business Agents and the Semantic Web, Nov 2004, pp. 643–662

[24] K. Sim, C. Choi, Agents that React to Changing Market Situations, IEEE Transaction on Systems, Man and Cybernetics, Part B: Cybernetics, vol. 33, April 2003, pp. 188–201.

[25] K. Sim, E. Wong, Towards Market-driven Agents for Electronic Auction, IEEE Transaction on Systems, Man and Cybernetics, Part A: Systems and Humans, vol. 31, Nov 2001, pp. 474–484.

[26] P. Wurman, M. Wellman, W. Walsh, The Michigan Internet AuctionBot: A Con<sup>fi</sup>gurable Auction Server for Human and Software Agents, Proc. 2nd Int. Conf. Autonomous Agents, ACM Press, Minneapolis, MN, May 1998, pp. 301–308, New York.

![](/api/attachments/NDTEY7P6/fulltext/images/433c3d2285af8e736f72cf97859e3ee057406425271e203352d7c49657366854.jpg)  
Fenghui Ren received his Bachelor of Science (in Compute Science) from XIDIAN University, China in 2003, and his Master by Research degree (in Computer Science) from University of Wollongong, Australia 2006. Currently, he is a PhD candidate in the School of Computer Science and Software Engineering at University of Wollongong, Australia His research interests include multi-agent systems, agentbased modeling and simulation, and multi-issue negotiation strategies.

![](/api/attachments/NDTEY7P6/fulltext/images/36b40cd9076bf24c2405f3c6840c4aa2e4c7b0b2a1da4b362471053edbdfecbf.jpg)

Minjie Zhang received her Bachelor of Science (in Computer Science) from Fudan University, China in 1982, and her PhD degree from the University of New England, Australia in 1996. Currently she is an associate professor in the School of Computer Science and Software Engineering and the director of Intelligent Systems Research Center, at University of Wollongong, Australia. She was a co-chair for the First Paci<sup>fi</sup>c Rim International Workshop on Electronic Commerce in 2006, and an organization chair, for the International Workshop on Rational, Robust, and Secure Negotiation Mechanisms in Multi-Agent Systems (RRS05, RRS06, and RRS07) a tutorial chair of the International Conference on Complex Open Distributed Systems in 2007 and a chair for

International Conference on Complex Open Distributed Systems in 2008. As a program committee member, she served/is serving for more than thirty international conferences. She is a member of editorial board of System and Information Sciences Notes and the International Journal of Knowledge and Systems Sciences. Dr Minjie Zhang is an active researcher and published over ninety research papers. She is the chief investigator for more than 10 different research grants including an ARC (Australia Research Council) Discovery grant and an ARC International Linkage Grant. She is a member of IEEE and the International Association of Computer and Their Applications. Her research interests include multi-agent systems, distributed information retrieval, agent-based modeling and simulation, and data mining and knowledge discovery.

![](/api/attachments/NDTEY7P6/fulltext/images/8b7e45616cb53174c404885d2fdd188a0bced00057cc99f2bd957198def4bf21.jpg)

Kwang Mong Sim is an Associate Editor for the JEEF Transactions on Systems, Man and Cybernetics-Part C, and the International Journal of Applied Systemic Studies, and an editorial/advisory board member of the International Journal of Hybrid Intelligent Systems and the System and Information Sciences Notes. He is also the Guest Editor of five (IEEE) journal special issues in agent-based Grid computing and automated negotiation, including a special issue on Grid Resource Management in the IEEE Systems Journal (IEEE Systems Council). Currently he is with the Hong Kong Baptist University He served as a referee for several national research grant councils including the National Science Foundation in USA, and as Area Chair, Session Chairman

and PC Member in many conferences. He supervised over 20 researchers/graduate students. He received his PhD and MSc from the University of Calgary, AB. Canada, and graduated Summa Cum Laude with a BSc(Hon) from the University of Ottawa, ON, Canada.
