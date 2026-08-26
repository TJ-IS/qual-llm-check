---
otero_id: 11740
otero_key: "2JH67C55"
title: "Intelligent agents for e-marketplace: Negotiation with issue trade-offs by fuzzy inference systems"
authors: "Chi-Bin Cheng; Chu-Chai Henry Chan; Kun-Cheng Lin"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.02.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent agents for e-marketplace: Negotiation with issue trade-offs by fuzzy inference systems

Chi-Bin Cheng <sup>\*,1</sup>, Chu-Chai Henry Chan, Kun-Cheng Lin

Department of Industrial Engineering and Management, Chaoyang University of Technology, 168 Gifeng E. Raad, Wufeng, Taichung County, Taiwan

Available online 26 May 2005

## Abstract

Automated negotiation by autonomous agents has become increasingly important since the advent of e-marketplace. In this study, automated negotiation is viewed as a search process in which negotiators jointly search for a mutually acceptable contract in a multidimensional space formed by negotiable issues. This search is formulated as a multiple-objective decision making problem and is solved through an iterative process of generating offers by fuzzy inference systems. These fuzzy inference systems serve as a search heuristic and are formulated based on the strategy of issue trade-offs. Five experiments are conducted to evaluate the performance of the proposed automated negotiation algorithm. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Automated negotiation; e-marketplace; Issue trade-offs; Fuzzy inference systems; Multiple-objective decision making

## 1. Introduction

The e-marketplace is a trading forum on the Internet in which multiple buyers and suppliers exchange goods and services. In traditional marketplaces, intercompany transactions are conducted between affiliated companies, or between companies with mutual trading relations. Many of these transactions are limited to a particular geographic area. Although an emarketplace eliminates the geographic obstacles to a certain extent, the barriers of culture, ego, and pride associated with human-based negotiations [13] can still constrain the efficiency of the marketplace. Moreover, the sheer number of participants in the e-marketplace introduces difficulties when attempting to find, and negotiate with, potential buyers or suppliers.

Negotiation has long been recognized as a timeconsuming process since all parties involved look to pursue their own interests in the face of conflicting goals. Furthermore, even in the most simple of negotiations, individuals frequently reach sub-optimal (or so-called Pareto-inferior) agreements [10]. The implementation of automated negotiations conducted by labor-saving and emotion-free software agents in the e-marketplace may alleviate the difficulties inherent in human negotiations.

Beam and Segev [1] classified automated negotiation into two major categories depending on an agent’s learning ability. Agents in the first category have no learning ability and are initially created with a complete set of strategies already in place. A wellknown example of the use of agents of this type is the Kasbah e-marketplace created by Chavez and Maes [2]. At Kasbah, users provide agents with instructions detailing how the desired price is to be changed over a time frame. A review of other negotiation agents in this category can be found in Beam and Segev [1].

The second category of automated negotiation employs agents with learning abilities to acquire experience from previous negotiations. Learning mechanisms used in this type of automated negotiation include Bayesian theory, neural network learning, and genetic programming. As an example, Zeng and Sycara [15] modeled the negotiation process as a sequential decision making task, and used Bayesian probability to guess the opponent’s reserved values. Hung [6] used supervised neural network learning to approximate the preference structure of an opponent such that the agent could calculate the similarity of its own offer to that of the opponent and could then counterpropose the most similar and beneficial offer. The disadvantage of this approach is that the neural network requires the provision of a very large volume of data during the training stage if it is to learn the opponent’s preference correctly. Genetic algorithms have also been applied to automated negotiations by some researchers. For example, Oliver [9] and Choi et al. [3] used genetic algorithms to find offers for agents to negotiate with one another. Beam and Segev [1] commented that the major disadvantage of genetic programming is that it requires many trials to achieve good strategies in each round of negotiation.

The negotiation agents discussed above deal mainly with competitive negotiation. However, this paper, which attempts to enhance the efficiency of automated negotiations, proposes software agents that negotiate in a cooperative manner. It is assumed that the trading is conducted in an e-marketplace with multiple negotiable issues.<sup>2</sup> Participants in this e-marketplace are requested to reveal their importance levels assigned to all issues, but are permitted to keep their issues’ utility functions private. The information relating to the importance levels of issues is used by agents throughout the negotiation process. The agents considered in this paper are not only endowed with negotiation strategies, but also possess the capability to learn from their opponent’s offers. The agent’s strategies are represented by fuzzy rules based on the concept of issue trade-offs, and the agent can learn from the history of offers in order to identify tighter negotiable ranges as the negotiation proceeds.

## 2. Automated negotiation

Automated negotiation can be viewed as a search process [3,9] in which negotiation agents jointly search for an agreement in a multidimensional space, where each dimension corresponds to a negotiable issue.

## 2.1. Negotiation with issue trade-offs

Corporate procurement generally involves many issues other than price. For example, product quality, payment terms, and delivery conditions are also commonly treated as negotiable items. The importance levels, or weights,<sup>3</sup> assigned to these issues may vary between the two parties involved in the negotiation, and hence trade-offs can be made between different issues such that both parties can reach a mutually beneficial agreement.

Faratin et al. [5] proposed an automated negotiation mechanism based on the concept of issue tradeoffs. Their algorithm performed an iterated hillclimbing search in a landscape of possible contracts. Although Faratin et al. established an appropriate model of issue trade-off-based agent negotiations, their search algorithm failed to reflect one highly important characteristic of a trade-off, namely that parties concede on their less important issues in exchange for achieving their bargaining goals on more important issues. This deficiency in their algorithm was due to the absence of the opponent’s issue weighting information.

The current study argues that if this weighting information is available to all parties, the issue trade-offbased agent negotiation will be more efficient. However, this approach requires all parties to surrender part of their privacy (i.e., to reveal their weighting information to their opponents). Based on the assumption that the parties are willing to do so, this paper proposes a novel approach for automated negotiation based on issue trade-offs.

## 2.2. Model of the proposed automated negotiation mechanism

Suppliers and buyers enter the e-marketplace and submit offers characterized by a set of predefined issues. The participants are requested to describe their offers in terms of the desired value, importance level (i.e., weight) and utility function of each issue. The desired values and weights of the issues are revealed to the opponents. However, the utility functions are kept private.

In our automated negotiation mechanism, two kinds of agents exist, namely matching agents and negotiation agents. The matching agent matches buyers and suppliers by finding the M most similar proposals to each participant. In this manner, each negotiation agent need only negotiate with the few opponents considered to be the most promising. The matching concept is based on the assumption that a dyad with a high matching degree is likely to reach an agreement more efficiently in further negotiation. Negotiating only with promising opponents minimizes the occurrence of pointless negotiations and hence increases the rate of successful contracts.

Once the matching agent notifies a participant of a set of candidate opponents and their offers, the participant launches its negotiation agent to contact all of these candidates. The agent either accepts an opponent’s offer or counterproposes a new offer to the opponent. During the negotiation, the agents respond autonomously to each other’s offers by: (1) evaluating the opponent’s offer with a utility function, and (2) generating a counteroffer by a heuristic represented in terms of fuzzy rules if the opponent’s offer is not acceptable. This process repeats until a specified stop criterion is met. When the agents reach an agreement, they send messages to the human participants, who then make the final decision of whether or not to accept the candidate contracts.

## 3. Matching of buyers and suppliers

The matching of buyers (denoted by B) and suppliers (denoted by S) is based on a similarity measure. Assume that there are m issues in each offer, and that the weights of issue i assigned by a supplier and by a buyer are $w _ { i } ^ { \mathrm { S } }$ and $w _ { i } ^ { \mathrm { B } }$ , respectively. These weights are expressed on a scale of 1–9, where the higher the number, the more important the issue. The overall similarity between two offers from the supplier and the buyer, respectively, is defined by a nearest-neighbor matching function [4] as:

$$
\operatorname{sim} (S, B) = \frac {\sum_ {i = 1} ^ {m} v _ {i} \zeta_ {i}}{\sum_ {i = 1} ^ {m} v _ {i}},\tag{1}
$$

where $\zeta _ { i }$ is the similarity measure for the ith issue (i.e., the greater the value of $\zeta _ { i } ,$ the more similar the two offers) and $\nu _ { i }$ is the geometric mean of the two weights $( w _ { i } ^ { \mathrm { S } }$ and $w _ { i } ^ { \mathrm { B } } )$ , that is,

$$
v _ {i} = \sqrt {w _ {i} ^ {\mathrm{S}} w _ {i} ^ {\mathrm{B}}}.\tag{2}
$$

The joint weight, $\nu _ { i } ,$ is used to reflect the simultaneous importance of issue i to both parties.

The issues relating to an offer are divided into two categories (i.e., quantitative issues, whose values can be measured on a numerical scale, and qualitative issues, which can only be assigned nominal values). Examples of quantitative issues include price, delivery time, penalties, etc., while examples of qualitative issues include color, currency, quality, etc. Since the nature of the quantitative and qualitative issues are different, the similarity measures designed for these two categories must also be different.

## 3.1. Similarity measures for quantitative issues

Let $x _ { i } ^ { \mathrm { S } }$ and $x _ { i } ^ { \mathrm { B } }$ be the supplier’s and the buyer’s desired values of issue $i ,$ respectively, and assume that $x _ { i } ^ { \mathrm { S } } { > } 0$ and $x _ { i } ^ { \mathrm { B } } { > } 0$ . The similarity measure for this issue is defined as:

$$
\zeta_ {i} = 1 - \frac {| x _ {i} ^ {\mathrm{S}} - x _ {i} ^ {\mathrm{B}} |}{\max \{x _ {i} ^ {\mathrm{S}} , x _ {i} ^ {\mathrm{B}} \}} = \frac {\min \{x _ {i} ^ {\mathrm{S}} , x _ {i} ^ {\mathrm{B}} \}}{\max \{x _ {i} ^ {\mathrm{S}} , x _ {i} ^ {\mathrm{B}} \}}.\tag{3}
$$

From Eq. (3), it is seen that $0 < \zeta _ { i } \le 1$

## 3.2. Similarity measures for qualitative issues

A binary measure (i.e., matched or not matched) is defined for the similarity measure of qualitative issues, that is,

$$
\zeta_ {i} = \left\{ \begin{array}{l l} 1, & \text { if } x _ {i} ^ {\mathrm{S}} = x _ {i} ^ {\mathrm{B}}, \\ 0, & \text { if } x _ {i} ^ {\mathrm{S}} \neq x _ {i} ^ {\mathrm{B}}. \end{array} \right.\tag{4}
$$

In the stage of negotiation, a negotiation agent can obtain better similarity measures than a matching agent since the negotiation agent is aware of the preferential orders of an issue’s values assigned by its owner. Therefore, a negotiation agent can define the similarity measure as (assuming a supplier agent):

$$
\zeta_ {i} = \left\{ \begin{array}{l l} 1, & \text { if } u _ {i} ^ {\mathrm{S}} (x _ {i} ^ {\mathrm{S}}) \leq u _ {i} ^ {\mathrm{S}} (x _ {i} ^ {\mathrm{B}}) \\ 1 - \left[ u _ {i} ^ {\mathrm{S}} (x _ {i} ^ {\mathrm{S}}) - u _ {i} ^ {\mathrm{S}} (x _ {i} ^ {\mathrm{B}}) \right], & \text { otherwise } \end{array} \right.\tag{5}
$$

where $u _ { i } ^ { \mathrm { S } } ( \cdot )$ is the supplier’s utility function for issue i. Since $0 { \leq } u _ { i } ^ { \mathrm { S } } ( \cdot ) { \leq } 1$ , then $0 \leq \zeta _ { i } \leq 1$

Once the similarity measures between each pair of offers have been obtained by Eq. (1), the user chooses the first M opponents having the highest similarity measures with which to negotiate.

## 4. Negotiation with issue trade-offs by fuzzy inference systems

Since the behavior of a buyer agent is symmetrically opposite to that of a supplier agent, for convenience, the automated negotiation process is formulated only from the perspective of the supplier’s negotiation agent.

## 4.1. Evaluation of offers

The supplier agent initially responds to the receipt of a buyer agent’s offer by evaluating the offer with an overall utility function. The utility function expresses the user’s preference by assigning values to alternatives. A detailed investigation of the utility function can be referred to Keeney and Raiffa [7]. In this study, it is assumed that the utilities of individual issues are independent of each other, and hence the overall utility of an offer is defined as a weighted average of the utilities of m individual issues, that is,

$$
U ^ {\mathrm{S}} \left(x ^ {\mathrm{B}}\right) = \frac {\sum_ {i = 1} ^ {m} w _ {i} ^ {\mathrm{S}} u _ {i} ^ {\mathrm{S}} \left(x _ {i} ^ {\mathrm{B}}\right)}{\sum_ {i = 1} ^ {m} w _ {i} ^ {\mathrm{S}}},\tag{6}
$$

where $U ^ { \mathrm { S } } ( \mathbf { x } ^ { \mathrm { B } } )$ is the supplier’s overall utility for the buyer’s offer $\mathbf { x } ^ { \mathrm { B } } \ ( = [ x _ { 1 } ^ { \mathrm { B } } , \cdot . . , x _ { m } ^ { \mathrm { B } } ] ^ { \mathrm { T } } )$ and $u _ { i } ^ { \mathrm { S } } ( \cdot )$ is the individual utility function for issue i. The individual utility function expresses the degree of satisfaction with an issue. The value of this function lies in the interval [0, 1], where a utility of 0 indicates infeasibility and a utility of 1 is optimum.

For a qualitative issue, the user directly assigns a utility to each possible value based on his or her particular preference. For example, the qualitative issue <sup>b</sup>color of car<sup>Q</sup> $\mathrm { c a r } ^ { \mathrm { * } }$ may have three possible values {red, yellow, black}, and the user can assign the utilities of these three values as {0.5, 1.0, 0.2}. Clearly, more elaborate methods such as the analytic hierarchy process (AHP) [11] can also be used to construct such utility functions.

Meanwhile, quantitative issues can be classified into two types, namely the benefit type (in which the larger, the better) and the cost type (in which the smaller, the better). Typical utility functions proposed for these two types of issues are illustrated in Fig. 1.

In this figure, a cost issue is parameterized by $l _ { \mathrm { a } }$ and $l _ { \mathrm { b } } ,$ and a benefit issue is parameterized by $h _ { \mathrm { a } }$ and $h _ { \mathrm { b } }$ . For example, <sup>b</sup>price<sup>Q</sup> is a benefit issue for a supplier. By setting $h _ { \mathrm { a } } { = } 1 0 0 0$ and $h _ { \mathrm { b } } { = } 1 8 0 0$ , the supplier is indicating that a price below 1000 is unacceptable while a price higher than 1000 is satisfactory and 1800 is the very highest expectation. Clearly, the lower limit of a benefit issue and the upper limit of a cost issue impose constraints on the acceptable values of an issue.

![](/api/attachments/2JH67C55/fulltext/images/14ef74504500ffce883361c5914e919712dba2225adc648501221aebd6f217d3.jpg)  
Fig. 1. Utility functions of quantitative issues.

## 4.2. Generation of new offers

In order to propose offers that are likely to be accepted by the opponent, Faratin et al. suggested finding offers that are similar to the opponent’s latest offer in each negotiation round. This strategy is based on the assumption that if an offer is similar to the opponent’s offer, then it will have a greater chance of being accepted by that opponent.

The present study implements the similarity concept advocated by Faratin et al. [5] in developing an automated negotiation system. In striving to reach a mutually acceptable agreement, a negotiation agent’s objective is to find the offer that is most beneficial to itself while at the same time is most similar to the opponent’s offer. The agent’s strategy can be formulated (from the perspective of a supplier agent) as the following multiple-objective decision making (MODM) problem:

Maximize $U ^ { \mathrm { S } } ( \mathbf { x } ^ { \mathrm { S } } )$ 9

ð7Þ

$$
\text { Maximize   } \text { sim } (\mathbf {x} ^ {\mathrm{S}}, \mathbf {x} ^ {\mathrm{B}}),\tag{8}
$$

subject to

$$
u _ {i} ^ {\mathrm{S}} \left(x _ {i} ^ {\mathrm{S}}\right) > 0, \quad i = 1, \dots , m.\tag{9}
$$

In the formulation above, the first objective is to find the most beneficial offer, $\mathbf { x } ^ { \mathrm { { S } } } .$ , and the second objective is to maintain a high similarity of such an offer to that of the buyer agent. Eq. (9) constrains the feasibility of an offer.

The max–min approach of Zimmermann [16] can be used to find the solution that balances these two conflicting objectives. Adopting this approach, the MODM presented above is rewritten as the following max–min problem:

Maximize k

subject to

$$
U ^ {\mathrm{S}} \left(\mathbf {x} ^ {\mathrm{S}}\right) \geq \lambda ,
$$

sim $\scriptstyle ( \mathbf { x } ^ { \mathrm { S } } , x ^ { \mathrm { B } } ) \geq \lambda$

0VkV1;

Eq. (9)

This formulation implies that $\lambda { = } \operatorname* { m i n } \{ U ^ { \mathrm { S } } ( \mathbf { x } ^ { \mathrm { S } } )$ 2 $\sin ( \mathbf { x } ^ { \mathrm { S } } , \mathbf { x } ^ { \mathrm { B } } ) \}$

Rather than solving the above max–min problem directly, k is heuristically improved by a negotiation process. The following automated negotiation algorithm is formulated to optimize k.

Automated negotiation algorithm:

Step 0: Set the negotiation round counter $t \gets 0$

Step 1: Evaluate the buyer’s offer by the utility function, $U ^ { \mathrm { S } } ( \mathbf { x } _ { t } ^ { \mathrm { B } } )$ .

Step 2: Stop criteria. If true then go to Step (5); otherwise, go to Step (3).

Step 3: Search for a new offer, $\mathbf { x } _ { t + 1 } ^ { \mathrm { { S } } } . \mathrm { ~ I f ~ } \lambda _ { t + 1 } \geq \lambda _ { t } ,$ , then go to Step (4); otherwise, go to Step (2).

Step 4: Counterpropose $\mathbf { x } _ { t + 1 } ^ { \mathrm { { S } } }$ to the opponent. $t \gets t + 1$ go to Step (1).

Step 5: Stop and notify the agents’ owners.

The stop criteria in Step (2) include the following situations: (1) accepting the opponent’s offer if $U ^ { \mathrm { S } } ( \mathbf { x } _ { t } ^ { \mathrm { B } } )$ is greater than a threshold h, which is predetermined by the user, or (2) accepting the opponent’s offer if the agent is unable to find any new offer that yields $\lambda _ { t + 1 } \geq \lambda _ { t } ,$ , or (3) withdrawing from the negotiation if the opponent’s offers are infeasible for a certain number of successive negotiation rounds, where this number is specified by the user.

The search for new offers in Step (3) is conducted in a multidimensional space in which each dimension corresponds to a negotiable issue. In the search algorithm proposed in this study, each issue is treated separately and is investigated using an independent fuzzy inference system. Each fuzzy inference system consists of a set of fuzzy rules, which explicitly express the actions to be taken in response to the opponent’s offer.

The proposed heuristic method works as follows. The offers made in the early rounds of a negotiation generally reflect high utilities to the proposing agent, and are unlikely to closely match the opponent’s offer. By making trade-offs between issues, an agent may find new offers that close the gap between the utility measure and the similarity measure and hence gradually improve the value of k.

## 4.2.1. Fuzzy inference systems for quantitative issues

Let $\Delta x _ { i }$ be the amounts of change for issue i between two successive rounds. The new value of this issue proposed for the next round of negotiation is therefore given by:

$$
x _ {i, t + 1} ^ {\mathrm{S}} = x _ {i, t} ^ {\mathrm{S}} + \Delta x _ {i}.\tag{10}
$$

Negotiation tactics are expressed by a set of fuzzy rules, which together comprise a fuzzy inference system to determine the value of $\Delta x _ { i }$ . The negotiation tactics are formulated based on the principle of trade-offs as follows: (1) for an issue which is important to both parties, the room for concession is very small; (2) for an issue which is important to one party but less so to the other, the former can demand more; and (3) for an issue which is unimportant to one party but important to the other, the former will concede by a wide margin in striving to reach agreement.

The fuzzy rule that expresses these tactics has the following format: If $w _ { i } ^ { \mathrm { S } }$ is $L _ { 1 }$ and $w _ { i } ^ { \mathrm { B } }$ is $L _ { 2 } .$ , then $\Delta x _ { i }$ is $C ,$ where $L _ { 1 }$ and $L _ { 2 }$ are linguistic terms, and C is the consequent amount of $\Delta x _ { i }$ . The linguistic terms are qualitative descriptions of the importance levels and are treated as fuzzy sets for computational purposes. Fuzzy set theory [14] directly addresses the limitation of the sharp boundaries found in classical set theory and hence fuzzy sets are well suited to quantify linguistic terms. A fuzzy set is defined by a membership function that maps objects in a domain of concern to their membership value in the set. The degree of membership in a set is expressed as a smooth and gradual transition from 0 to 1. Such a transition yields fuzzy set flexibility in modeling linguistic expressions. It is generally difficult for a user to assign precisely an importance level to an issue. However, fuzzy sets are more robust when dealing with imprecise importance levels due to their smooth transition between importance levels.

In the current fuzzy rules, the importance levels are graded to three linguistic terms (i.e., <sup>b</sup>important,<sup>Q</sup> <sup>b</sup>neutral,<sup>Q</sup> and <sup>b</sup>unimportant<sup>Q</sup>). Their membership functions are denoted as l<sub>important</sub>, $\mu _ { \mathrm { n e u t r a l } } .$ and l<sub>unimportant</sub>, respectively, and are depicted in Fig. 2, in which the membership functions are defined on the universe of weight.

The consequence, C, in a rule is related to two factors (i.e., the difference between the respective offers of the two parties, $\boldsymbol { x } _ { i , t } ^ { \ \mathrm { ~ d ~ } } { = } | \boldsymbol { x } _ { i , t } ^ { \ \mathrm { ~ S ~ } } { - } \boldsymbol { x } _ { i , t } ^ { \ \mathrm { ~ B ~ } } |$ , and a tolerance rate of concession, which is determined through the respective weights of an issue assigned by the two parties. By taking $( 1 0 - w _ { i } ^ { \mathrm { S } } )$ and $( \mathrm { i } 0 - { w } _ { i } ^ { \mathrm { B } } )$ to indicate the concession degrees of the supplier agent and the buyer agent, respectively, the tolerance rate, $c _ { \mathrm { r } } ,$ for a supplier agent can be defined as:

$$
c _ {\mathrm{r}} = \frac {1 0 - w _ {i} ^ {\mathrm{S}}}{\left(1 0 - w _ {i} ^ {\mathrm{S}}\right) + \left(1 0 - w _ {i} ^ {\mathrm{B}}\right)}.\tag{11}
$$

The tolerance rate $0 . 1 { \leq } c _ { \mathrm { r } } { \leq } 0 . 9$ is used to regulate the concession range (i.e., the concession range of the supplier agent is specified as $c _ { \mathrm { r } } x _ { i , t } ^ { \mathrm { ~ d ~ } } )$

The sign of $\Delta x _ { i }$ indicates an action of concession or aggression. For a benefit issue, a negative $\Delta x _ { i }$ implies a concession, while a positive $\Delta x _ { i }$ indicates that more is demanded on this issue. Table 1 presents a fuzzy inference system containing nine fuzzy if–then rules for determining negotiation actions on issue i based on the importance levels of that issue (from the supplier agent’s perspective).

The first rule in Table 1 is read as <sup>b</sup>If $w _ { i } ^ { \mathrm { S } }$ is important and $w _ { i } ^ { \mathrm { B } }$ is important, then $\Delta x _ { i } { = } - \mathrm { r a n d } ( 0 _ { \cdot }$ $c _ { \mathbf { r } } { \bar { \mathbf { \phi } } } ^ { \mathrm { d } } ) ^ { \flat }$ for a benefit issue, or ${ } ^ { 6 6 } \mathrm { I f } \ w _ { i } ^ { \mathrm { S } }$ is important and $w _ { i } ^ { \mathrm { B } }$ is important, then $\Delta x _ { i } { = } \mathrm { r a n d } ( 0 , \ c _ { \mathrm { r } } x _ { t } ^ { \mathrm { d } } ) ^ { , }$ for a cost issue, where rand(0, $c _ { \mathrm { r } } x _ { t } ^ { \mathrm { d } } )$ is a random number drawn from the interval $[ 0 , c _ { \mathrm { r } } x _ { t } ^ { \mathrm { d } } ]$ . The other rules in this table are read in the same way. The rationale behind the nine rules in Table 1 can be explained as follows:

![](/api/attachments/2JH67C55/fulltext/images/ab2b05064935a4468aa1abd8d2a0bdf72c4ade80b6e9284c0f75785151daeab4.jpg)  
Fig. 2. Membership functions of three importance levels.

Table 1  
Fuzzy inference system for determining actions on issue i (quantitative issue) from supplier agent’s perspective

<table><tr><td rowspan="2">Rule</td><td rowspan="2"> $w_i^S$ </td><td rowspan="2"> $w_i^B$ </td><td colspan="2">C</td></tr><tr><td>Benefit</td><td>Cost</td></tr><tr><td>1</td><td>Important</td><td>Important</td><td>-rand(0,  $c_r x_{i,t}^d$ )</td><td>rand(0,  $c_r x_{i,t}^d$ )</td></tr><tr><td>2</td><td>Important</td><td>Neutral</td><td>-rand(0,  $k_1 c_r x_{i,t}^d$ )</td><td>rand(0,  $k_1 c_r x_{i,t}^d$ )</td></tr><tr><td>3</td><td>Important</td><td>Unimportant</td><td>rand(0,  $c_r x_{i,t}^d$ )</td><td>-rand(0,  $c_r x_{i,t}^d$ )</td></tr><tr><td>4</td><td>Neutral</td><td>Important</td><td>-rand(0,  $k_2 c_r x_{i,t}^d$ )</td><td>rand(0,  $k_2 c_r x_{i,t}^d$ )</td></tr><tr><td>5</td><td>Neutral</td><td>Neutral</td><td>rand(- $k_1 c_r x_{i,t}^d$ ,  $k_1 c_r x_{i,t}^d$ )</td><td>rand(- $k_1 c_r x_{i,t}^d$ ,  $k_1 c_r x_{i,t}^d$ )</td></tr><tr><td>6</td><td>Neutral</td><td>Unimportant</td><td>rand(0,  $k_1 c_r x_{i,t}^d$ )</td><td>-rand(0,  $k_1 c_r x_{i,t}^d$ )</td></tr><tr><td>7</td><td>Unimportant</td><td>Important</td><td>-rand(0,  $k_3 c_r x_{i,t}^d$ )</td><td>rand(0,  $k_3 c_r x_{i,t}^d$ )</td></tr><tr><td>8</td><td>Unimportant</td><td>Neutral</td><td>-rand(0,  $k_2 c_r x_{i,t}^d$ )</td><td>rand(0,  $k_2 c_r x_{i,t}^d$ )</td></tr><tr><td>9</td><td>Unimportant</td><td>Unimportant</td><td>rand(- $c_r x_{i,t}^d$ , $c_r x_{i,t}^d$ )</td><td>rand(- $c_r x_{i,t}^d$ , $c_r x_{i,t}^d$ )</td></tr></table>

rand(a, b) is a random number between a and b.

Rule 1: Since both parties consider this issue to be important, the supplier agent will concede on this issue and the degree of concession is randomly selected from the range 0 to $c _ { \mathrm { r } } x _ { i , t } ^ { \mathrm { ~ d ~ } } .$

Rule 2: Since the buyer agent is neutral on the importance of this issue, the supplier agent will choose its concession from a smaller range. A constant $k _ { 1 } ,$ which is subjectively determined from the range $0 < k _ { 1 } < 1$ , is used to regulate the maximum degree of concession and hence the concession is chosen randomly from the interval $[ 0 , k _ { 1 } c _ { \mathrm { r } } x _ { i , t } ]$

Rule 3: Since the supplier agent’s importance level on this issue is much higher than that of the buyer agent, the supplier agent will raise its demand on this issue. It is seen in Table 1 that $\Delta x _ { i }$ is positive in this rule for a benefit issue.

Rule 4: Since the supplier agent considers this issue to be less important, it will concede a rather large amount on this issue. A constant $k _ { 2 }$ (slightly greater than 1, generally $1 < k _ { 2 } \le 1 . 2 )$ is used to augment the concession.

Rule 5: Since both parties are neutral on this issue, the supplier agent will randomly choose either to concede or to raise its demand on this issue. The constant $k _ { 1 }$ is used to regulate the margin $( \mathrm { i } . \mathrm { e } . , \Delta x _ { i }$ is chosen randomly from the interval $[ - k _ { 1 } c _ { \mathrm { r } } x _ { i , t } ^ { \mathrm { ~ d ~ } } , k _ { 1 } c _ { \mathrm { r } } x _ { i , t } ^ { \mathrm { ~ d ~ } } ] )$ ).

Rule 6: Since the buyer agent does not care about this issue, the supplier agent will raise its demand. However, the supplier agent does not regard this issue as important either, and hence it will demand only a small amount, chosen randomly from the interval $[ 0 , k _ { 1 } c _ { \mathrm { r } } x _ { i , t } ]$

Rule 7: The supplier agent does not care about this issue but the buyer agent considers it to be important. Therefore, the supplier agent will concede a rather larger amount on this issue than in Rule (4) (i.e., the concession is augmented by a constant $k _ { 3 } ,$ where $k _ { 3 } > k _ { 2 } > 1 )$

Rule 8: Similar to Rules (4) and (7).

Rule 9: Similar to Rule (5).

In the fuzzy inference system, multiple rules are active at the same time with different degrees of firing strength. The concluding value of $\Delta x _ { i }$ is aggregated from all the rules based on approximate reasoning [14]. The firing strength $( z _ { j } , j { = } 1 , . . . , 9 )$ of each rule is determined by applying a fuzzy $\mathrm { \tilde { \Delta } a n d } , \mathrm { \tilde { \Delta } }$ which is defined as a t-norm operator, 	, to the condition of each rule. For instance, the firing strength of Rule (1), denoted by $z _ { 1 } ,$ , in Table 1 is defined as:

$$
z _ {1} = \mu_ {\text { important }} \left(w _ {i} ^ {\mathrm{S}}\right) \otimes \mu_ {\text { important }} \left(w _ {i} ^ {\mathrm{B}}\right).
$$

The current approach assigns an algebraic product to the operation of a t-norm, that is,

$$
z _ {1} = \mu_ {\mathrm{important}} \big (w _ {i} ^ {\mathrm{S}} \big) \mu_ {\mathrm{important}} \big (w _ {i} ^ {\mathrm{B}} \big).\tag{12}
$$

Moreover, $C _ { j } , \ j { = } 1 , . . . , 9$ represents the consequence of each rule. Accordingly, $\Delta x _ { i } ,$ which is derived from the fuzzy inference system, can be defined as a weighted average of $C _ { j }$ [12], that is,

$$
\Delta x _ {i} = \frac {\sum_ {j = 1} ^ {9} z _ {j} C _ {j}}{\sum_ {j = 1} ^ {9} z _ {j}}.\tag{13}
$$

## 4.2.2. Fuzzy inference systems $f o r$ qualitative issues

The fuzzy inference system, which determines actions for a qualitative issue, is comprised of rules with the following format: If $w _ { i } ^ { \mathrm { S } }$ is $L _ { 1 }$ and $w _ { i } ^ { \mathrm { B } }$ is $L _ { 2 } .$ then $x _ { i , t + 1 } ^ { \mathrm { S } }$ is $C .$

As shown in Table 2, the complete fuzzy inference system again consists of nine rules. For a qualitative issue, a concession implies moving downward along the player’s preferential order. Let $\phi _ { \mathrm { { S } } } ( { \cdot } )$ denote the supplier agent’s preferential order function of a qualitative issue. For example, if the supplier agent’s preferential order of the issue <sup>b</sup>color of $\boldsymbol { \mathrm { c a r } ^ { \circ } }$ is red, blue, and black, then $\phi _ { \mathrm { S } } ( \mathrm { r e d } ) { = } 1 , ~ \phi _ { \mathrm { S } } ( \mathrm { b l u e } ) { = } 2$ , and $\phi _ { \mathrm { S } } ( \mathrm { b l a c k } ) { = } 3$ . From the supplier agent’s perspective, the difference between the supplier agent’s offer and the buyer agent’s offer is defined as:

$$
x _ {i, t} ^ {\mathrm{d}} = \left\{ \begin{array}{l l} 0, & \text { if } \phi_ {\mathrm{S}} \Big (x _ {i, t} ^ {\mathrm{B}} \Big) \leq \phi_ {\mathrm{S}} \Big (x _ {i, t} ^ {\mathrm{S}} \Big), \\ \phi_ {\mathrm{S}} \Big (x _ {i, t} ^ {\mathrm{B}} \Big) - \phi_ {\mathrm{S}} \Big (x _ {i, t} ^ {\mathrm{S}} \Big), & \text { if } \phi_ {\mathrm{S}} \Big (x _ {i, t} ^ {\mathrm{B}} \Big) > \phi_ {\mathrm{S}} \Big (x _ {i, t} ^ {\mathrm{S}} \Big). \end{array} \right.\tag{14}
$$

As before, the tolerance rate, $c _ { \mathrm { r } } ,$ is used to regulate the concession range.

Rule (1) in Table 2 can be interpreted as follows. If the buyer agent’s offer $( x _ { i , t } ^ { \mathrm { ~ B ~ } } )$ exceeds the supplier agent’s expectation $( x _ { i , t } ^ { \mathrm { ~ S ~ } } ) .$ , the supplier agent will accept that offer. Conversely, if a difference exists between the two respective offers, the supplier agent will concede to an inferior position in its preferential order. This inferior position is determined by randomly choosing a position between $\phi _ { \mathrm { { S } } } ( x _ { i , t } \mathrm { { S } } )$ and $\phi _ { \mathrm { { S } } } ( x _ { i , t } \mathrm { { S } } )$ + $c _ { \mathrm { r } } x _ { i , t } ^ { \mathrm { ~ d ~ } } .$ The inverse function, $\phi _ { \mathrm { S } } ^ { - 1 } ( \cdot )$ , then converts the chosen position to a value of the issue. Similarly, the remainder rules in Table 2 are formulated based on the relative importance of issues between the two parties.

The resultant value of $\cdot _ { x _ { i , t + 1 } ^ { \mathrm { S } } }$ derived from the fuzzy inference system in Table 2 is defined as:

$$
x _ {i, t + 1} ^ {\mathrm{S}} = C _ {l}, \text {   with   } l = \arg \max _ {j} \left\{z _ {j} \right\}, j = 1,..., 9.\tag{15}
$$

## 4.3. Adjustment of a newly generated offer

In Step (3) of the automated negotiation algorithm presented in Section 4.2, if a newly generated offer is unable to yield a value of $\lambda _ { t + 1 }$ , which is greater than or equal to $\lambda _ { t } ,$ then this offer must be adjusted to meet that requirement, unless such an adjustment is impossible. Making this adjustment involves first locating the issue that prevents maximization of k, and then changing the value of this issue slightly in order to increase the offer’s utility or similarity, depending on which is applicable. If the adjusted offer is still unable to satisfy the requirement, the above procedure is repeated until $\lambda _ { t + 1 } \geq \lambda _ { t } .$ or until the search has exhausted all possibilities.

The adjustment procedure can be described as follows. Let issue h be the issue responsible for producing the greatest difference between the utility and similarity measures, that is,

Table 2  
Fuzzy inference system for determining actions on issue i (qualitative issue) from supplier agent’s perspective

<table><tr><td>Rule</td><td> $w_{i}^{\text{S}}$ </td><td> $w_{i}^{\text{B}}$ </td><td>C</td></tr><tr><td>1</td><td>Important</td><td>Important</td><td> $\phi_{\text{S}}^{-1}(\min\{\phi_{\text{S}}(x_{i,t}^{\text{B}}),rand(\phi_{\text{S}}(x_{i,t}^{\text{S}}),\phi_{\text{S}}(x_{i,t}^{\text{S}})+c_{\text{r}}x_{i,t}^{\text{d}}\})$ </td></tr><tr><td>2</td><td>Important</td><td>Neutral</td><td> $\phi_{\text{S}}^{-1}(\min\{\phi_{\text{S}}(x_{i,t}^{\text{B}}),rand(\phi_{\text{S}}(x_{i,t}^{\text{S}}),\phi_{\text{S}}(x_{i,t}^{\text{S}})+c_{\text{r}}x_{i,t}^{\text{d}}$ )</td></tr><tr><td>3</td><td>Important</td><td>Unimportant</td><td> $\phi_{\text{S}}^{-1}(\min\{\phi_{\text{S}}(x_{i,t}^{\text{B}}),\phi_{\text{S}}(x_{i,t}^{\text{S}})\})$ </td></tr><tr><td>4</td><td>Neutral</td><td>Important</td><td> $\phi_{\text{S}}^{-1}(\min\{\phi_{\text{S}}(x_{i,t}^{\text{B}}),rand(\phi_{\text{S}}(x_{i,t}^{\text{S}}),\phi_{\text{S}}(x_{i,t}^{\text{S}})+x_{i,t}^{\text{d}}\})$ </td></tr><tr><td>5</td><td>Neutral</td><td>Neutral</td><td> $\phi_{\text{S}}^{-1}(\min\{\phi_{\text{S}}(x_{i,t}^{\text{B}}),rand(\phi_{\text{S}}(x_{i,t}^{\text{S}}),\phi_{\text{S}}(x_{i,t}^{\text{S}})+c_{\text{r}}x_{i,t}^{\text{d }}\})$ </td></tr><tr><td>6</td><td>Neutral</td><td>Unimportant</td><td> $\phi_{\text{S}}^{-1}(\min\{\phi_{\text{S}}(x_{i,t}^{\text{B}}),\phi_{\text{S}}(x_{i,t}^{\text{S}})\})$ </td></tr><tr><td>7</td><td>Unimportant</td><td>Important</td><td> $x_{i,t}^{\text{B}}$ </td></tr><tr><td>8</td><td>Unimportant</td><td>Neutral</td><td> $\phi_{\text{S}}^{-1}(\min\{\phi_{\text{S}}(x_{i,t}^{\text{B}}),rand(\phi_{\text{S}}(x_{i,t}^{\text{S}}),\phi_{\text{S}}(x_{i,t}^{\text{S}})+x_{i,t}^{\text{d}}\})$ </td></tr><tr><td>9</td><td>Unimportant</td><td>Unimportant</td><td> $rand\{x_{i,t}^{\text{S}},x_{i,t}^{\text{B}}\}\phi_{\text{S}}$ </td></tr></table>

rand(a, b) is a random integer number between a and $b ;$ rand{a, b} is either a or $b .$

$$
h = \arg \max _ {i} \left\{\left| \frac {w _ {i} ^ {\mathrm{S}}}{\sum_ {g = 1} ^ {m} w _ {g} ^ {\mathrm{S}}} u _ {i} ^ {\mathrm{S}} (x _ {i} ^ {\mathrm{S}}) \right. \right.
$$

$$
\left. - \frac {v _ {i}}{\sum_ {g = 1} ^ {m} v _ {g}} s _ {i} \right| \Bigg \}, \quad i = 1,.., m.\tag{16}
$$

$\begin{array} { r } { \mathrm { I f } \frac { w _ { i } ^ { \mathrm { S } } } { \sum _ { g = 1 } ^ { m } w _ { g } ^ { \mathrm { S } } } u _ { i } ^ { \mathrm { S } } \big ( x _ { i } ^ { \mathrm { S } } \big ) > \frac { \nu _ { i } } { \sum _ { g = 1 } ^ { m } \nu _ { g } } s _ { i } } \end{array}$ then $x _ { \mathrm { h } } ^ { \mathrm { S } }$ is changed in the direction which increases $s _ { k } ;$ otherwise, it is changed in the direction which increases $u _ { \mathrm { h } } ^ { \mathrm { S } } ( x _ { \mathrm { h } } ^ { \mathrm { S } } )$

## 5. Experiments and performance evaluation

Five experiments were undertaken to evaluate the performance of the proposed automated negotiation procedure.

## 5.1. Experiment 1: performance evaluation

This experiment involved six groups of automated negotiations, with each group containing different numbers of participants, as shown in Table 3. Five replications of the negotiation simulation were conducted for each negotiation dyad formed in the five groups, resulting in a total of 2005 negotiations. This experiment considered three issues (two quantitative and one qualitative) in each negotiation. The agents’ initial proposals were generated by randomly choosing values for the three issues from the following ranges: Issue 1, [5000, 10,000]; Issue 2, [30, 90]; and Issue 3, three nominal values. The utility function for each quantitative issue was set by appropriately choosing the lower and the upper limits of the issue with the reference of that issue’s initial value, and the utilities assigned to the qualitative issue were randomly generated. The agents’ importance levels for each issue were also randomly generated. The parameters used in the automated negotiation were set as follows: maximum number (M) of similar opponents, 1; utility threshold (h) at which to stop searching for new offers, $0 . 7 ;$ and parameters in Table 1 , $k _ { 1 } { = } 0 . 8 , k _ { 2 } { = } 1 . 1$ , and $k _ { 3 } = 1 . 2$ . It is noted that these parameter setups were applied throughout all five experiments.

Table 3  
Success rate of negotiations among different groups

<table><tr><td>Group (supplier × buyer)</td><td>Number of negotiation dyads</td><td>Average success rate (%)</td><td>Average number of offers exchanged</td></tr><tr><td>10 × 10</td><td>17</td><td>96.47</td><td>7.02</td></tr><tr><td>20 × 20</td><td>36</td><td>93.99</td><td>7.28</td></tr><tr><td>30 × 30</td><td>57</td><td>94.04</td><td>7.14</td></tr><tr><td>40 × 40</td><td>77</td><td>94.81</td><td>6.72</td></tr><tr><td>50 × 50</td><td>97</td><td>92.35</td><td>6.58</td></tr><tr><td>60 × 60</td><td>117</td><td>94.18</td><td>6.54</td></tr><tr><td>Average</td><td>-</td><td>94.31</td><td>6.88</td></tr></table>

The third column in Table 3 indicates the average rate of successful negotiations over the total number of negotiations in each group. The final column indicates the negotiation length, which is defined as the number of offers exchanged between the supplier agent and the buyer agent. An example of the offer exchange process is shown in Fig. 3, which presents the payoffs from the supplier agent and the buyer agent in a two-dimensional utility space, where each axis represents the level of utility for one of the two parties. In the offer exchange process, the supplier agent and the buyer agent take turns to make their respective offers. The numbers adjacent to the plotting symbols in Fig. 3 indicate the sequence in which the offers are made. It can be seen that in the sixth round of negotiation (i.e., the 12th offer), the two parties reach an agreement, which is close to the Pareto-frontier.

Three criteria, which were suggested by Mumpower [8], are used to evaluate the negotiation results:

1) Efficiency: This criterion distinguishes optimal from sub-optimal negotiated contracts. Efficiency is defined as nearness to the Pareto-frontier. The Pareto-frontier is a curve in the utility space (as shown in Fig. 3). For agreements falling on this curve, modifying the agreement to achieve a better payoff for one party necessarily implies a sacrifice on the part of the other [3]. The criterion of efficiency is measured as:

$$
\text { Nearness } = \min \{d _ {1}, d _ {2} \},
$$

where $d _ { 1 }$ is the horizontal distance from the negotiated contract to the frontier and $d _ { 2 }$ is the vertical distance. The Pareto-frontier of each negotiation is found by enumerating 10,000 possible contracts from the negotiation and then approximately plotting the frontier curve in the utility space.

![](/api/attachments/2JH67C55/fulltext/images/cb70090a9ca8e8704607e23e7caa5dc7eb20a71ff95dd6050da456472e342a01.jpg)  
Fig. 3. Utility space of supplier agent and buyer agent.

2) Joint utility: This criterion measures the social welfare of the two parties. The joint utility is calculated as the sum of the individual utilities.

3) Equality: This criterion is used to measure the fairness of a negotiated contract. A fair contract implies the prospective advantage of a long-term partnership. This measure is defined as:

Equality $= | U ^ { \mathrm { S } } ( { \bf x } ) - U ^ { \mathrm { B } } ( { \bf x } ) |$

where x is the negotiated contract. When Equality equals 0, the contract is considered to be perfectly fair to both parties.

Table 4 presents part of the performance evaluation for the 57 conducted negotiations in the $3 0 \times 3 0$ group. It be seen that, on average, the joint utilities of the negotiated contracts reach 94% of their optima, and the majority of them are very close to the Pareto frontier.

## 5.2. Experiment 2: low similarity vs. high similarity

The aim of the second experiment was to test the following assumption:

Hypothesis 1. A dyad with a higher similarity is more effective in reaching an agreement.

Table 4  
Performance evaluation of automated negotiation

<table><tr><td rowspan="2">Negotiation</td><td colspan="3">Joint utility</td><td>Equality</td><td>Nearness to frontier</td></tr><tr><td> $U^{\mathrm{S}}(\mathbf{x})+U^{\mathrm{B}}(\mathbf{x})$ </td><td>Optimal joint utility</td><td>% of achieving optimum</td><td> $|U^{\mathrm{S}}(\mathbf{x})-U^{\mathrm{B}}(\mathbf{x})|$ </td><td> $\min\{d_1,d_2\}$ </td></tr><tr><td>1</td><td>1.542</td><td>1.589</td><td>97.06</td><td>0.148</td><td>0.00</td></tr><tr><td>2</td><td>1.484</td><td>1.607</td><td>92.32</td><td>0.203</td><td>0.06</td></tr><tr><td>3</td><td>1.484</td><td>1.611</td><td>92.13</td><td>0.173</td><td>0.03</td></tr><tr><td>4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>5</td><td>1.409</td><td>1.545</td><td>91.15</td><td>0.244</td><td>0.10</td></tr><tr><td>6</td><td>1.645</td><td>1.758</td><td>93.56</td><td>0.120</td><td>0.02</td></tr><tr><td>7</td><td>1.576</td><td>1.701</td><td>92.66</td><td>0.113</td><td>0.00</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>51</td><td>1.600</td><td>1.669</td><td>95.91</td><td>0.162</td><td>0.03</td></tr><tr><td>52</td><td>1.487</td><td>1.718</td><td>86.51</td><td>0.190</td><td>0.13</td></tr><tr><td>53</td><td>1.226</td><td>1.352</td><td>90.68</td><td>0.041</td><td>0.07</td></tr><tr><td>54</td><td>1.453</td><td>1.586</td><td>91.66</td><td>0.271</td><td>0.01</td></tr><tr><td>55</td><td>1.378</td><td>1.462</td><td>94.25</td><td>0.218</td><td>0.04</td></tr><tr><td>56</td><td>1.392</td><td>1.698</td><td>81.97</td><td>0.200</td><td>0.00</td></tr><tr><td>57</td><td>1.380</td><td>1.433</td><td>96.29</td><td>0.088</td><td>0.04</td></tr><tr><td>Average</td><td>1.491</td><td>1.588</td><td>93.86</td><td>0.156</td><td>0.04</td></tr></table>

Table 5  
Negotiation results for low similarity dyads vs. high similarity dyads

<table><tr><td rowspan="2">Group</td><td rowspan="2">Success rate of negotiations (%)</td><td rowspan="2">Average number of offers exchanged</td><td colspan="2">Joint utility</td></tr><tr><td>Average joint utility</td><td>% of achieving optimal joint utility</td></tr><tr><td>Low similarity</td><td>76.36</td><td>7.69</td><td> $1.159^a$ </td><td>73.01</td></tr><tr><td>High similarity</td><td>96.49</td><td>6.77</td><td> $1.491^a$ </td><td>93.86</td></tr></table>

<sup>a</sup> Excluding failed negotiations.

This experiment involved a total of 30 supplier agents and 30 buyer agents. The negotiation dyads were divided into two groups: one group of 55 dyads with low similarities (an average of 0.35) and a second group of 57 dyads with high similarities (an average of 0.72). The negotiation results are shown in Table 5.

The results presented in Table 5 confirm that the group with high similarity has a higher success rate than the group with low similarity. Applying the t-test with a significance level of 0.05, the number of offers exchanged is not significantly different between the two groups $( t = 1 . 5 4 , p = 0 . 0 6 )$ . However, the percentage of negotiations achieving the optimal joint utility is significantly higher in the group with high similarity than in the group with low similarity (t = 16, $p \approx 0 . 0 0 )$ . Hence, the results of Table 5 support Hypothesis (1).

## 5.3. Experiment 3: effect of weight information

The third experiment aimed to justify the usefulness of the issue weighting information in the negotiation process. For comparison purposes, automated negotiations with no weight information were also conducted. When the issue weighting information is unavailable, the automated negotiation algorithm proposed in this paper cannot be employed. Therefore, a similar algorithm to the one presented by Faratin et al. [5] is used to generate offers for this case.

Hypothesis 2. The availability and utilization of the opponent’s issue weighting information in a negotiation can enhance the effectiveness of the negotiation.

Thirty supplier agents and 30 buyer agents were formed into 57 negotiation dyads. The negotiation results are shown in Table 6.

From Table 6, it is seen that although the average joint utility is approximately equal in the two groups $( t = 0 . 0 6 , p = 0 . 4 7 )$ , the average number of offers exchanged in the group with visibility of the weight information is significantly less than that in the group without weight information (t = 3.37, $p { = } 0 . 0 0 1 )$ . Therefore, Hypothesis (2) is supported.

## 5.4. Experiment 4: effect of the number of issues

To examine the effects of the number of issues on the negotiation results, negotiations with different number of issues were simulated. The number of issues was gradually increased from 3 to 10. For simplicity, all the issues involved in this experiment were of a quantitative nature, and the initial value of each issue was drawn randomly from the range [5000, 10,000].

Hypothesis 3. The number of issues does not affect the performance of the proposed automated negotiation approach.

Thirty supplier agents and 30 buyer agents were formed into 57 negotiation dyads. The negotiation results are shown in Table 7. Using the F-test with a significance level of 0.05, the results of Table 7 indicate that the number of issues has no significant influence on the joint-utility or nearness-to-frontier aspects. However, the effect of the number of issues on the equality and number-of-offers-exchanged measures is clearly significant. Therefore, Hypothesis (3) is only partially true.

Results of negotiations with and without provision of weight information

<table><tr><td>Group</td><td>Average number of offers exchanged</td><td>Average joint utility</td></tr><tr><td>With weight information</td><td>6.7</td><td>1.468</td></tr><tr><td>Without weight information</td><td>10.0</td><td>1.471</td></tr></table>

Table 7  
Results of negotiations with different numbers of issues

<table><tr><td rowspan="2">Number of issue</td><td colspan="3">Joint utility</td><td>Equality</td><td>Nearness to frontier</td><td rowspan="2">Average number of offer exchanged</td></tr><tr><td> $U^{\mathrm{S}}(\mathbf{x})+U^{\mathrm{B}}(\mathbf{x})$ </td><td>Optimal joint utility</td><td>% of achieving optimum</td><td> $|U^{\mathrm{S}}(\mathbf{x})-U^{\mathrm{B}}(\mathbf{x})|$ </td><td> $\min\{d_1,d_2\}$ </td></tr><tr><td>3</td><td>1.247</td><td>1.304</td><td>95.5</td><td>0.084</td><td>0.03</td><td>7.93</td></tr><tr><td>5</td><td>1.179</td><td>1.233</td><td>95.6</td><td>0.107</td><td>0.03</td><td>8.96</td></tr><tr><td>8</td><td>1.228</td><td>1.251</td><td>96.5</td><td>0.134</td><td>0.02</td><td>15.53</td></tr><tr><td>10</td><td>1.200</td><td>1.222</td><td>95.6</td><td>0.154</td><td>0.03</td><td>31.74</td></tr><tr><td>F-test</td><td></td><td></td><td>F=2.32,p=0.076</td><td>F=4.83,p=0.003</td><td>F=1.40,p=0.242</td><td>F=38.40,p=0.000</td></tr></table>

## 5.5. Experiment 5: quantitative issues vs. qualitative issues

In order to examine the effect of the nature of the issues on the negotiation result, negotiations with three qualitative issues were conducted and the results compared to the case where the negotiations involved three quantitative issues. The initial value of each qualitative issue was chosen randomly from a set of 10 nominal values.

Hypothesis 4. The nature (i.e., quantitative or qualitative) of the issue does not affect the performance of the proposed automated negotiation approach.

The negotiation results are compared in Table 8. It can be seen that the results of the negotiations with purely qualitative issues are better than those of the negotiations with purely quantitative issues. Hence, the results do not support Hypothesis (4). This outcome is reasonable since the searching space of qualitative issues is finite and discrete, and is therefore much smaller than that of quantitative issues.

## 6. Conclusions and future research

This paper has presented a formal heuristic model for making trade-offs in automated negotiations in a third-party-driven e-marketplace. The tactics that the agents are to employ when making trade-offs are explicitly formulated as fuzzy inference systems, which are used to infer new offers at each round of negotiation. The experimental results demonstrate that the proposed automated negotiation algorithm is efficient in terms of the number of offers exchanged, the joint utility obtained, and the Pareto-efficiency of the negotiated contracts.

The automated negotiations formulated in this study do not consider the quantities that a buyer demands or the quantities that a supplier can provide. However, in practice, a supplier sells products to many buyers and a buyer may distribute its demand among many suppliers. The issue of quantity can complicate the decisions in a negotiation since it generally interacts with other issues such as price. For example, quantity discounts and shipping costs can both affect the procurement decision. It is the current authors’ intention to address the issue of quantity in a future study. Although the approach proposed in this paper allows the agent to negotiate with multiple opponents at the same time, each negotiation is treated independently. However, it would be more advantageous if an agent could apply the information from one negotiation to another negotiation. The feasibility of doing so will also be explored in future research.

Results of negotiations with different nature of issue

<table><tr><td rowspan="2">Nature of issue</td><td colspan="3">Joint utility</td><td>Equality</td><td>Nearness to frontier</td><td rowspan="2">Average number of offer exchanged</td></tr><tr><td> $U^{\mathrm{S}}(\mathbf{x})+U^{\mathrm{B}}(\mathbf{x})$ </td><td>Optimal joint utility</td><td>% of achieving optimum</td><td> $|U^{\mathrm{S}}(\mathbf{x})-U^{\mathrm{B}}(\mathbf{x})|$ </td><td> $\min\{d_1,d_2\}$ </td></tr><tr><td>Quantitative</td><td>1.247</td><td>1.304</td><td>95.5</td><td>0.084</td><td>0.03</td><td>7.93</td></tr><tr><td>Qualitative</td><td>1.910</td><td>1.23</td><td>99.3</td><td>0.068</td><td>0.01</td><td>8.96</td></tr><tr><td>t-test</td><td></td><td></td><td> $t=-7.85,$  $p=0.000$ </td><td> $t=1.38,$  $p=0.085$ </td><td> $t=4.06,$  $p=0.000$ </td><td> $t=4.35,$  $p=0.000$ </td></tr></table>

The form of the utility function used in the present approach is rather simple and inflexible. The appropriateness of the utility function has a direct influence on the result of the automated negotiation. In the current approach, a bad contract is prevented by setting a minimum acceptable value for each issue, as indicated in Eq. (9). To make the proposed approach rather more useful in the real B-to-B environment, more sophisticated techniques should be used to refine the user’s utility function.

## References

[1] C. Beam, A. Segev, Electronic catalogs and negotiations, CITM Working Paper 96-WP-1016.

[2] A. Chavez, P. Maes, Kasbah: an agent marketplace for buying and selling goods, Proceedings of the 1st International Conference on the Practical Application of Intelligent Agents and Multi-Agent Technology, London, 1996.

[3] S.P.M. Choi, J. Liu, S.-P. Chan, A genetic agent-based negotiation system, Computer Networks 37 (2001) 195– 204.

[4] R. Duda, P. Hart, Pattern Classification and Scene Analysis, Wiley, New York, NY, 1973.

[5] P. Faratin, C. Sierra, N.R. Jennings, Using similarity criteria to make issue trade-offs in automated negotiations, Artificial Intelligence 142 (2002) 205 – 237.

[6] C.-A. ung, Learning in multi attribute bilateral negotiation under bounded number of message, Master’s Thesis, Depart ment of Computer Science, National Tsing Hua University, Taiwan, June 2001.

[7] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Wiley, New York, 1976.

[8] J.L. Mumpower, The judgment policies of negotiators and the structure of negotiation problems, Management Science 37 (10) (1991) 1304– 1324.

[9] J.R. Oliver, A machine-learning approach to automated negotiation and prospects for electronic commerce, Jour

nal of Management Information Systems 13 (3) (1997) 83– 112.

[10] H. Raiffa, The Art and Science of Negotiation, Harvard University Press, Cambridge, MA, 1982.

[11] T.L. Satty, The Analytic Hierarchy Process, Analytic Hierarchy Process, McGraw-Hill, New York, NY, 1980.

[12] T. Takagi, M. Sugeno, Fuzzy identification of systems and its application to modeling and control, IEEE Transactions on Systems, Man, and Cybernetics 15 (1985) 116 – 132.

[13] R.E. Walton, R.B. McKersie, A Behavioral Theory of Labor Negotiation, McGraw-Hill, New York, 1965.

[14] L.A. Zadeh, The concept of a linguistic variable and its application to approximate reasoning, Information Science 8 (1975) 199–249.

[15] D. Zeng, K. Sycara, Bayesian learning in negotiation, working notes of the AAAI 1996 Stanford spring symposium series on adaptation, co-evolution, and learning in multiagent systems (1996).

[16] H.-J. Zimmermann, Fuzzy programming and linear programming with several objective functions, Fuzzy Sets and Systems 1 (1978) 45–55.

Chi-Bin Cheng is an Assistant Professor in the Department of Industrial Engineering and Management at Chaoyang University of Technology, Taiwan. He received his BS from Chung Yuan Christian University, Taiwan, and his PhD from Kansas State University. His main research interests are in the fields of soft computing, swarm intelligence, group decision-making, multi-agent systems, and supply chain management. Cheng<sup>T</sup>s work has appeared in Fuzzy Sets and Systems, European Journal of Operational Research, Computers and Mathematics with Applications, among others.

Chu-Chai Henry Chan received his PhD degree from Iowa State University. He is currently an Associate Professor in the Department of Industrial Engineering and Management at Chaoyang University of Technology, Taiwan. His research interests focus on neural networks, e-commerce, supply chain management, and automated negotiation. Dr. Chan has been a consultant to many companies in Taiwan on the implementation of ERP and knowledge management systems.

Kun-Cheng Lin received his BS in 2001 from the Department of Industrial Engineering at Feng Chia University, Taiwan, and his MS in 2003 from the Department of Industrial Engineering and Management at Chaoyang University of Technology, Taiwan. His research interest is automated negotiation by agents.
