---
otero_id: 7586
otero_key: "VWAE22UB"
title: "Bilateral single-issue negotiation model considering nonlinear utility and time constraint"
authors: "Fenghui Ren; Minjie Zhang"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.018"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bilateral single-issue negotiation model considering nonlinear utility and time constraint

Fenghui Ren ⁎, Minjie Zhang

School of Computer Science and Software Engineering, University of Wollongong, Australia

a r t i c l e i n f o

Available online 5 June 2013

Keywords: Agent negotiation Nonlinear utility function Negotiation decision function Offer generation function

## a b s t r a c t

Bilateral agent negotiation is considered as a fundamental research issue in autonomous agent negotiation, and was studied well by researchers. Generally, a prede<sup>fi</sup>ned negotiation decision function and utility function are used to generate an offer in each negotiation round according to a negotiator's negotiation strategy, preference, and restrictions. However, such a negotiation procedure may not work well when the negotiator's utility function is nonlinear, and the unique offer is dif<sup>fi</sup>cult to be generated. That is because if the negotiator's utility function is non-monotonic, the negotiator may <sup>fi</sup>nd several offers that come with the same utility at the same time; and if the negotiator's utility function is discrete, the negotiator may not <sup>fi</sup>nd an offer to satisfy its expected utility exactly. In order to solve such a problem, we propose a novel negotiation model in this paper. Firstly, a 3D model is introduced to illustrate the relationships between an agent's utility function, negotiation decision function and offer generation function. Then two negotiation mechanisms are proposed to handle two types of nonlinear utility functions respectively, i.e. a multiple offer mechanism is introduced to handle non-monotonic utility functions, and an approximating offer mechanism is introduced to handle discrete utility functions. Lastly, a combined negotiation mechanism is proposed to handle nonlinear utility functions in general situations by considering both the non-monotonic and discrete. The experimental results demonstrate the effectiveness and ef<sup>fi</sup>ciency of the proposed negotiation model.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Agent negotiation is one of the most signi<sup>fi</sup>cant research issues in multi-agent systems (MASs). Many works have been done to solve challenges in agent negotiation. To list a few of them, Narayanan and Jennings [13,14] adopted a Markov chain framework to model bilateral negotiation and employed Bayesian learning to enable agents to learn an optimal strategy in incomplete information settings. Fatima et al. [4] investigated the negotiation outcomes in incomplete information settings through the comparison of the difference between two agent's negotiation deadlines, and proposed an agendabased framework to help self-interested agents to maximize their utilities. Brzostowski and Kowalczyk [1] proposed an approach to predict the opponent's behaviors based only on the historical offers of the current negotiation. They claimed that time and imitation are two main factors which in<sup>fl</sup>uence an agent's behaviors during negotiation. Ren et al. [16] proposed a market-based model to handle the uncertainty and concurrency in open and dynamic negotiation environments. However, most existing approaches are based on the assumption that all negotiators employ monotonic continuous linear utility functions, and not much work has been done on negotiations in which agents employ non-monotonic and/or discrete nonlinear utility functions. According to our studies, agents may employ such nonlinear utility functions in many real-world negotiations [11,12]. For example, as shown in Fig. 1, in a scheduling problem for task allocation, an employee feels happy to be assigned work between 9 AM– 12 AM and 1 PM–3 PM, but feels unhappy to work hard during the <sup>fi</sup>rst one or last 2 h of a day. The employee's temper in a working day is a non-monotonic function. In Fig. 2, a potential car purchaser may have different preferences on a car's color. Because each model of a car only has limited colors, the car purchaser's preference on a car's color is a discrete function.

In a negotiation with time constraint, an agent usually de<sup>fi</sup>nes a negotiation strategy to make concessions throughout a negotiation. Firstly, according to the negotiation decision function, agents can calculate the possible maximal utility they can gain at a certain moment. Then, according to the offer generation function, agents can <sup>fi</sup>nd a particular offer to reach their expected utility. Because most negotiation models assume that agents employ monotonic and continuous utility functions, a particular offer can always be found to satisfy agents expected utilities at any negotiation round. Also, it can be guaranteed that the concessions from opponent's offers are always consistent, i.e., always monotonically increasing or decreasing the agents' utilities. However, when agents employ non-monotonic and/ or discrete utility functions, it cannot be guaranteed that the opponent's offers are always in an ascending or descending order. Also, the particular offer which can exactly match the expected utility may not be found. Therefore, when the utility function is nonmonotonic, agents may have multiple options on offers in order to reach the expected utility. As shown in Fig. 1, in order to ensure that an employee's happiness is $p ( p \in [ 0 , 1 ] ) ,$ , a job can be assigned to the employee at either 9 AM or 12 AM. Also, when the utility function is discrete, an agent perhaps cannot <sup>fi</sup>nd an offer to satisfy the expected utility exactly. As shown in Fig. 2, none of the available colors can make a car purchaser's happiness equal to $\textit { 1 } ( q \in [ 0 , 1 ] )$ exactly.

![](/api/attachments/VWAE22UB/fulltext/images/48e66fa52aef73d6e59954ece666153eac2256e3bced62b0701524fc09b03420.jpg)  
Fig. 1. An employee's temper for a day

In order to solve the offer generation problem when agents employ nonlinear utility functions, we propose a novel negotiation model in this paper, which can handle both the situations when agents have non-monotonic and/or discrete utility functions. Speci<sup>fi</sup>- cally, for negotiations involving non-monotonic utility functions, the multiple offer mechanism is introduced to allow agents to generate equivalent offers in a negotiation round; for negotiations involving discrete utility functions, the approximating offer mechanism is introduced to allow agents to generate an offer to approximate their expected utilities. Eventually, the two mechanisms are combined to solve general situations in negotiations involving nonlinear utility functions. Furthermore, when utility functions are non-monotonic, the existing alternating offer protocol [15] may become inef<sup>fi</sup>cient in enlarging agents' pro<sup>fi</sup>ts. That is because the existing alternating offer protocol assumes an agent has a consistent evaluation on offers' changes, i.e., when an agent gradually makes concessions to decrease own pro<sup>fi</sup>t, the opponent's pro<sup>fi</sup>t will be gradually increased, and vice versa. However, such an assumption is not held when agents employ non-monotonic utility functions. In order to help agents to make decisions on trade off in such a situation, a new negotiation protocol is proposed based on the alternating offer protocol.

The rest of this paper is organized as follows. Section 2 brie<sup>fl</sup>y introduces a general bilateral single issue negotiation model with linear utility functions. Section 3 introduces our 3D negotiation model, the multiple offer mechanism to handle non-monotonic utility functions, the approximating offer mechanism to handle discrete utility functions, and the combined mechanism to handle general nonlinear utility functions. In Section 4, the Rubinstein's alternating offer protocol is modi<sup>fi</sup>ed to <sup>fi</sup>t the situation caused by non-monotonic and/or discrete utility function. Section 5 demonstrates a negotiation between two agents having nonlinear utility functions. Section 6 compares our work with some related work on handling negotiations with nonlinear utility functions. Section 7 concludes this paper and explores our future work.

![](/api/attachments/VWAE22UB/fulltext/images/d46c55bf865409f0a24a88915ba464b8771fbcf9ab1b671917ef0d0c39281d7e.jpg)  
Fig. 2. A customer's <sup>fl</sup>avor on a car's color.

## 2. A general negotiation model for linear utility function

Before we introduce the negotiation model for nonlinear utility functions, we would like to brie<sup>fl</sup>y introduce a general negotiation model for linear utility functions by considering time constraints. A general bilateral single issue negotiation is performed between two agents on a good's price. Let b denote the buyer, s denote the seller, and let $[ I P ^ { a } , R P ^ { a } ]$ denote the range of values for prices that are acceptable to Agent a, where $a \in \{ b , s \} . I P ^ { a }$ is Agent a's initial price and $R P ^ { a }$ is Agent a's reservation price. Usually, for a buyer agent $I P ^ { b } \leq R P ^ { b }$ , and for a seller agent $I P ^ { b } \ge R P ^ { b }$ . We use a^ to denote Agent a's opponent, $\scriptstyle { \hat { a } } \in \{ b , s \}$ . Obviously, an agreement can be reached between Agent a and its opponent a^ only when there is an intersection between their price ranges. If the buyer agent's reservation price is smaller than the seller agent's reserved price $( \mathrm { i . e . , } R P ^ { b } < R P ^ { s } )$ , an agreement will not be achieved.

Usually, a negotiation should consider time constraint, and each agent has a negotiation deadline. If an agreement cannot be achieved before an agent's deadline, then the agent has to quit the negotiation, and the negotiation fails. Let $T ^ { a }$ denote Agent a's deadline. A negotiation can be started by either the buyer or seller. During the negotiation, the buyer and the seller will send alternating offers to each other until both sides agree on an offer together, or one side quits the negotiation. This negotiation protocol is known as the alternating offer protocol [15]. Let $p _ { \hat { a } \to a } ^ { t }$ denote the price sent from Agent a^ to Agent a at time t. Once Agent a receives the offer, it will map the price in the offer to a utility value by using its utility function U<sup>a</sup>. A general linear utility function used by Agent a is shown in Eq. (1).

$$
U ^ {a} \left(p _ {\hat {a} \rightarrow a} ^ {t}\right) = \frac {p _ {\hat {a} \rightarrow a} ^ {t} - R P ^ {a}}{I P ^ {a} - R P ^ {a}}\tag{1}
$$

It can be seen that a general linear utility function normalizes a price to a utility value in-between [0,1] by using the prede<sup>fi</sup>ned initial price $( I P ^ { a } )$ and reservation price $( R P ^ { a } )$ . The utility value indicates the pro<sup>fi</sup>t that the agent can gain by accepting the offer $p _ { \hat { a } \to a } ^ { t } .$ . In general, for Agent a, if $U ^ { a } ( p _ { \hat { a } \to a } ^ { t } )$ is greater than the value of the counteroffer Agent a is ready to send in the next negotiation round $t ^ { \prime } ,$ i.e., $U ^ { a } ( p _ { \hat { a } \to a } ^ { t } ) { \geq } U ^ { a } \left( p _ { a \to \hat { a } } ^ { t ^ { \prime } } \right)$ , then Agent a will accept Agent a^'s offer at round t and the negotiation completes successfully with the agreement $p _ { \hat { a } \to a } ^ { t } .$ Otherwise, the counter-offer $p _ { a \to \hat { a } } ^ { t ^ { \prime } }$ will be sent from Agent a to Agent a^. Such a procedure will be repeated until an agreement is achieved or one agent reaches its deadline. Thus, the action, $A ^ { a } ,$ , that Agent a takes at each negotiation round t is usually de<sup>fi</sup>ned as follows:

$$
A ^ {a} \Big (p _ {\hat {a} \to a} ^ {t} \Big) = \left\{ \begin{array}{l l} \text { Quit } & \text { if } t > T ^ {a}, \\ \text { Accept } p _ {\hat {a} \to a} ^ {t} & \text { if } U ^ {a} \Big (p _ {\hat {a} \to a} ^ {t} \Big) \geq U ^ {a} \Big (p _ {a \to \hat {a}} ^ {t ^ {'}} \Big), \\ \text { Offer } p _ {a \to \hat {a}} ^ {t ^ {'}} & \text { otherwise }. \end{array} \right.\tag{2}
$$

If Agent a does not accept the price $p _ { \hat { a } \to a } ^ { t }$ and its deadline is not achieved, then it will send a counter-offer $p _ { a \to \hat { a } } ^ { t }$ to Agent a^ as a response. Usually, agents may employ different negotiation tactics [3] to generate counter-offers based on different criteria, such as time, resources, and previous counter-offers. The time-dependent tactic is the most popular criteria when agents generate their counter-offers by considering the time constraint. In the time-dependent tactic, the predominant factors used are the decision to which price should be offered in round t, and variation of the offer by considering the round t and the deadline $T ^ { a } .$ Usually, the counter-offer made by Agent a at round t $( 0 \leq t \leq T ^ { a } )$ is modeled as a function $\Phi ^ { a }$ as follows:

$$
p _ {a \to \hat {a}} ^ {t} = \left\{ \begin{array}{l l} I P ^ {a} + \Phi^ {a} (t) \big (R P ^ {a} - I P ^ {a} \big) & \text { for } a = b, \\ R P ^ {a} + \big (1 - \Phi^ {a} (t) \big) \big (I P ^ {a} - R P ^ {a} \big) & \text { for } a = s. \end{array} \right.\tag{3}
$$

where function $\phi ^ { a } ( t )$ is called the negotiation decision function (NDF) [3] and is de<sup>fi</sup>ned as follows:

$$
\Phi^ {a} (t) = k ^ {a} + \left(1 - k ^ {a}\right) \left(\frac {t}{T ^ {a}}\right) ^ {1 / \psi}\tag{4}
$$

where $k ^ { a }$ is the initial utility and $k ^ { a } \in [ 0 , 1 ] . \operatorname { I f } k ^ { a } = 0 ,$ then at the beginning of a negotiation the initial price $I P ^ { a }$ will be selected, and when the deadline is reached the reserved price $R P ^ { a }$ will be selected.

Theoretically, the NDF has an in<sup>fi</sup>nite number of possible tactics when ψ $( \psi \geq 0 )$ has different values. However, in Fig. 3 three extreme cases show different patterns of behaviors when ψ is located in different ranges.

• Conceder: When $\psi > 1 ,$ the rate of change in the slope is decreasing. It represents a negotiation behavior where the agent will give larger concessions during the early stages of the negotiation, but smaller concessions during the later stages of the negotiation.

• Linear: When $\psi = 1$ , the rate of change in the slope is zero. It represents a negotiation behavior where the agent will give a constant concession throughout the negotiation.

• Boulware: When $0 < \psi < 1$ , the rate of change in the slope is increasing. It represents a negotiation behavior where the agent will give smaller concession during the early stages of the negotiation, but larger concessions during the later stages of the negotiation.

In this section, we brie<sup>fl</sup>y introduced a general bilateral singleissue negotiation model. However, such a model is based on an the assumption that all agents employ linear utility functions, i.e., Eq. (1) is monotonic and continuous. Therefore, during a negotiation, a unique offer can be generated to reach an agent's utility indicated by the negotiation decision function (see Eq. (4)). However, if the utility functions employed by agents are non-monotonic and/or discrete, this general model cannot guarantee to produce correct offer/s to reach the expected utility, and agents' reactions (see Eq. (2)) during negotiations which may become inef<sup>fi</sup>cient in enlarging agents utilities. In the following sections, we will introduce several negotiation mechanisms to handle the situation when agents employ nonmonotonic and/or discrete utility functions.

![](/api/attachments/VWAE22UB/fulltext/images/7a1059994c1d345e1a741c1b163c3b66e873254fc70c6dd5fb314415e608aaf1.jpg)  
Fig. 3. Negotiation decision functions for the buyer [4].

## 3. Offer generation considering non-monotonic utility function

When agents employ non-monotonic utility functions, the relationships between offers and utilities are not one-to-one mapping anymore, but more than one offer may contribute to the same utility. In this subsection, we <sup>fi</sup>rstly propose a multiple offer mechanism to handle such a problem when agents employ non-monotonic utility functions.

## 3.1. 3-Dimensional model

In order to well illustrate the relationship among an agent's negotiation decision functions, utility function, and counter-offer generation function, we proposed a 3D model. As displayed in Fig. 4, the front surface (Surface $\mathsf { A } )$ is the negotiation strategy surface (NS Surface). It illustrates the relationship between the negotiation round and the agent's expected utility. Let the x-axis indicate the negotiation round (t) and z-axis indicate the agent's utility (u), then the mapping displayed on NS surface is summarized in Eq. (5). So the negotiation decision function introduced in Eq. (4) (see Section 2) belongs to this class.

$$
\phi_ {t} ^ {a} = \Phi^ {a} (t)\tag{5}
$$

The side surface (Surface B) is the utility function surface (UF Surface). It illustrates the relationship between the real value of the negotiating issue and the agent's utility. Let y-axis indicate the real value of the negotiating issue, then the mapping displayed on UF Surface could be summarized in Eq. (6).

$$
u _ {o} ^ {a} = U ^ {a} (o)\tag{6}
$$

where o indicates an offer, $U ^ { a } ( \cdot )$ is Agent a's utility function, and $u _ { o } ^ { a }$ is Agent a's evaluation on offer o.

The bottom surface (Surface C) is the offer generation surface (OG surface). It illustrates the relationship between the negotiation round and the agent's offers. In Eq. (7), we summarized such a relationship.

![](/api/attachments/VWAE22UB/fulltext/images/dfb572eee5ec43ce7245d35519fd09cf8d199599a325fa830d75751afc677775.jpg)  
Fig. 4. Negotiation model for non-monotonic continuous utility function.

$$
o _ {t} ^ {a} = \Psi^ {a} (t)\tag{7}
$$

where $\Psi ^ { a } ( t )$ is Agent a's offer generation function, and $o _ { t } ^ { a }$ is the offer generated by Agent a at round t.

During a negotiation, agents should have such an offer generation function to create a counter-offer in each negotiation round once the opponent's offer is not acceptable. For example, Eq. (3) de<sup>fi</sup>nes a general offer generation function by considering the initial offer, reservation offer and time constraint. However, Eq. (3) is based on the assumption that the agent employs a linear utility function, so a unique offer can be selected in each negotiation round to <sup>fi</sup>t the expected utility. When agents employ non-monotonic and/or discrete utility, the one-to-one mapping between the negotiation round and the offer may not exist anymore. In the following subsections, three mechanisms will be introduced to solve such a problem.

## 3.2. Multiple offer mechanism

In this subsection, we propose a multiple offer mechanism to solve the offer generation problem when agents employ non-monotonic utility functions. Let $U ^ { a } ( o )$ be the non-monotonic utility function that Agent a employs, and $\boldsymbol { \phi } ^ { a } ( t )$ be Agent a's decision making function by considering time constraint, then the problem is how to create the offer generate function $\Psi ^ { a } ( t )$ by using $U ^ { a } ( o )$ and $\phi ^ { a } ( t ) .$

Let ϕ<sup>a</sup> be Agent a's expected utility at round $t , U ^ { ( - 1 , a ) } ( \bullet )$ be the inverse function of the non-monotonic utility function $U ^ { a } ( o )$ , then the offers (O) which contribute equivalent pro<sup>fi</sup>t as the expected utility $\phi _ { t } ^ { a }$ can be calculated as follows.

$$
\mathbf {0} _ {\mathbf {t}} ^ {\mathbf {a}} = U ^ {(- 1, a)} \left(\phi_ {t} ^ {a}\right)\tag{8}
$$

where $\phi _ { t } ^ { a }$ is decided by the negotiation decision function $\boldsymbol { \phi } ^ { a } ( t )$ , and O<sup>a</sup> contains the offers that Agent a should send to the opponent at round t.

Because the utility function $U ^ { a } ( o )$ is not a monotonic function, so the inverse function ${ U ^ { ( - 1 , a ) } ( \phi _ { t } ^ { a } ) }$ is not a one-to-one mapping function and may generate more than one counter-offers for the same expected utility. Finally, Agent a's offer generation function by considering time constraint is defined as follows.

$$
\Psi^ {a} (t) = U ^ {(- 1, a)} \big (\Phi^ {a} (t) \big)\tag{9}
$$

where $\boldsymbol { \phi } ^ { a } ( t )$ is Agent a's negotiation decision function, and a general $\boldsymbol { \phi } ^ { a } ( t )$ is de<sup>fi</sup>ned in Eq. (4).

As shown in Fig. 4, Curve X on Plane A is the negotiation decision function, Curve Y on Plane B is the utility function. Both the negotiation decision function and the utility function are known by Agent a. The proposed 3D model indicates well how to produce the offer generation function (Curves Z and K on Plane C) based on these two known functions when the utility function is non-monotonic. For example, at the negotiation round t, according to the negotiation decision function, Agent a expects a utility of 0.8, and according to the utility function (Line Y), two offers can reach the expected utility (Points m and n). Then, by employing Eq. (8), the two offers (offers b and $p )$ are found by Agent a. Finally, Agent a generates two counter-offers (Points e and $f )$ at round t to its opponent. By employing such a multiple offer mechanism at each negotiation round, Agent a's counter-offer generation function can be drawn on

Surface C. It can be seen that Agent a's counter-offers during the negotiation are illustrated by Curves Z and K.

Based on the above description, in order to create the offer generation function when agents employ the non-monotonic utility function, the following three steps are highlighted. The detailed algorithm is given in Algorithm 1.

Step 1 According to an agent's negotiation decision function, the agent calculates its expected utility at the negotiation round t;

Step 2 According to the agent's non-monotonic utility function, the agent discovers value/s on the negotiation issue. From these discovered values, the agent should gain exact same pro<sup>fi</sup>t as its expected utility at the round t;

Step 3 The agent makes a decision whether to accept the opponent's offer or to send the counter-offer (see Section 4 for detail). Once the counter-offer needs to be sent, all the equivalent offers are sent at the same time as a package to the opponent.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Offer generation when agents employ non-monotonic utility function

Input: Agent a's negotiation decision function  $\Phi^{a}(t)$ , utility function  $U^{a}(o)$  and all possible offers O

Output: Agent a's counter-offer/s  $O_{c}$  at the negotiation round t

 $O_{c} \leftarrow \emptyset, \phi_{t}^{a} \leftarrow \Phi^{a}(t)$ $O_{t} \leftarrow U^{(-1,a)}(\phi_{t}^{a})$ 

for all  $o_{t,i} \in O_{t}$  do

if  $o_{t,i} \in O$  then

 $O_{c} \leftarrow \{o_{t,i}\} \cup O_{c}$ 

end if

end for

return  $O_{c}$
</div>

As shown in Algorithm 1, in order to generate the multiple offers, the solutions of the agent's inverse utility function should be calculated <sup>fi</sup>rstly, and then the solutions should be compared with the offer candidate set for validity checking. Therefore, the complexity of the offer generation, when the non-monotonic utility function is used, is $T ( n ) \stackrel { - } { = } O ( U ^ { ( - 1 , a ) } ) + 2 n + 2 .$

## 3.3. Approximating offer mechanism

In some situations, agents may employ discrete utility functions. Because the number of offers is limited when agents use discrete functions, the agents may not <sup>fi</sup>nd offers to satisfy their expected utilities exactly. In order to handle such a problem in discrete utility functions, we propose an approximating offer mechanism in this subsection.

Let set $\mathbf { 0 } = \{ o _ { i } | i \in [ 1 , I ] \}$ be the all possible offers that Agent a can choose during a negotiation, and notation $u _ { o _ { i } } ^ { a }$ be the utility of Offer $o _ { i } .$ At the negotiation round t, Agent a <sup>fi</sup>rstly employs the negotiation decision function to calculate its expected utility, i.e., ϕ<sup>a</sup> (see Eq. (4)). The value of $\phi _ { t } ^ { a }$ indicates the maximal utility that Agent a may gain in the remaining negotiation rounds. Because Agent a employs a discrete utility function, a particular offer which can generate the exact value as the expected utility may not exist. Therefore, Agent a should select another offer which can generate a utility to approximate the expected utility as much as possible. Let $d _ { t , o _ { i } } ^ { a }$ indicate the distance between the expected utility ϕ<sup>a</sup> and the offer $0 _ { i } { ' } S$ utility $u _ { o _ { i } } ^ { a }$ for Agent a at round t. Intuitively, $d _ { t , o _ { i } } ^ { a }$ should be greater than 0, because $\phi _ { t } ^ { a }$ is Agent a's best expectation at round t. So $d _ { t , o _ { i } } ^ { a }$ is de<sup>fi</sup>ned as follows:

$$
d _ {t, o _ {i}} ^ {a} = \phi_ {t} ^ {a} - u _ {o _ {i}} ^ {a}\tag{10}
$$

Then, the counter-offer that Agent a should select is indicated by notation $o _ { c } ,$ and $o _ { c }$ is decided as follows.

$$
o _ {c} = \forall o _ {i} \in \mathbf {0}, \exists o _ {c} \in \mathbf {0} \Rightarrow d _ {t, o _ {c}} ^ {a} <   d _ {t, o _ {i}} ^ {a} \cap d _ {t, o _ {c}} ^ {a} \geq 0\tag{11}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Offer generation when agents employ discrete utility function
Input: Agent a's negotiation decision function  $\Phi^{a}(t)$ , utility function  $U^{a}(o)$  and all possible offers O
Output: Agent a's counter-offer  $o_{c}$  at the negotiation round t

 $O_{t} \leftarrow \emptyset, \phi_{t}^{a} \leftarrow \Phi^{a}(t), d_{min} \leftarrow +\infty$ 

for all  $o_{i} \in O$  do

 $u_{o_{i}} \leftarrow U^{a}(o_{i})$ $d_{t,o_{i}}^{a} \leftarrow \phi_{t}^{a} - u_{o_{i}}^{a}$ 

if  $d_{t,o_{i}}^{a} \geq 0$  then

 $O_{t} \leftarrow \{o_{i}\} \cup O_{t}$ 

if  $d_{t,o_{i}}^{a} &lt; d_{min}$  then

 $d_{min} \leftarrow d_{t,o_{i}}^{a}$ 

end if

end if

end for

for all  $o_{t,i} \in O_{t}$  do

 $u_{o_{t,i}}^{a} \leftarrow U^{a}(o_{t,i})$ $d_{t,o_{t,i}}^{a} \leftarrow \phi_{t}^{a} - u_{o_{t,i}}^{a}$ 

if  $d_{t,o_{t,i}}^{a} == d_{min}$  then

 $o_{c} \leftarrow d_{t,o_{t,i}}^{a}$ 

return  $o_{c}$ 

end if

end for
</div>

Eq. (11) represents an approximating approach for counter-offer generation when agents employ discrete utility functions. It is guaranteed that the offer which can mostly satisfy an agent's expected utility will be found from its candidate offers. In Fig. 5, we illustrate an example to show the process in detail. Curve X is an agent's negotiation decision function, and located on Plane A. The agent's possible offers are distributed discretely on Plane B, and indicated by triangles. And the agent's offer generation function is Curve Z on Plane C. Because the agent's utility function is a discrete function, so the offer generation function is a piecewise function. For example, as shown in Fig. 5, at round t, the agent's expected utility is 0.8. However, none of the agent's offers can bring 0.8 utility to the agent exactly. Then, by employing the approximating offer mechanism, Point h is found as the closest utility to 0.8, and Offer q is selected as the counter-offer. Finally, the agent sends the counter-offer q at round t, which is indicated by Point d on Curve Z.

![](/api/attachments/VWAE22UB/fulltext/images/5bbd1a5126eaa54501db65420b18abcc6727ed14fc4f7d47976542740d61526c.jpg)  
Fig. 5. Negotiation model for discrete utility function.

Based on the above description, the offer generation algorithm by considering the discrete feature of utility functions is de<sup>fi</sup>ned in Algorithm 2, and the three major steps are summarized as follows.

Step 1 According to an agent's negotiation decision function, the agent calculates its expected utility at the negotiation round t;

Step 2 According to the agent's discrete utility function, the agent <sup>fi</sup>nds the offer which can reach the expected utility as much as possible from its offer candidates;

Step 3 The agent makes a decision whether to accept the opponent's offer (see Section 4 for detail), and send the counter-offer in necessary.

As shown in Algorithm 2, when the agent employs discrete utility function, the counter-offer generation approach does not use the inverse utility function, so as to greatly decrease the complexity. Therefore, the complexity of the offer generation, when the discrete utility function is used, is $T ( n ) = 1 7 n + 3 .$

## 3.4. Combined mechanism

Subsection 3.2 proposed a multiple offer mechanism for agents employing non-monotonic utility functions, and Subsection 3.3 proposed an approximating offer mechanism for agents employing discrete utility functions. In a more general situation, agents' utility functions may be a mixture of non-monotonic and discrete functions.

For example, as shown in Fig. 6, an agent employs a non-monotonic and discrete utility function. At round t, the agent's expected utility is indicated by Point $0 , \mathrm { i . e . , } 0 . 6 5 .$ . However, according to the agent's utility function, none of the agent's offers can satisfy its expectation exactly. So the agent should employ the approximating offer mechanism to <sup>fi</sup>nd the closest offer/s to its expectation. Because the agent's utility function is non-monotonic, so two points (i.e., Points m and n) having the similar distance to the agent's expected utility are found. So by employing the multiple offer mechanism, two counter-offers (Offers e and f) are sent at negotiation round t.

![](/api/attachments/VWAE22UB/fulltext/images/6b17cc8f2cf0fc809b46c52a1b5631e49bc7fb3cd336dd9c3e5882069eb8dd36.jpg)  
Fig. 6. Negotiation model for general nonlinear utility function.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 3 Offer Generation When Agents employ non-monotonic and discrete utility function

Input: Agent a's negotiation decision function  $\Phi^{a}(t)$ , utility function  $U^{a}(o)$  and all possible offers O
Output: Agent a's decision at the negotiation round t

 $O_{c} \leftarrow \emptyset, \phi_{t}^{a} \leftarrow \Phi^{a}(t)$ $O_{t} \leftarrow U^{(-1,a)}(\phi_{t}^{a})$ 

for all  $o_{t,i} \in O_{t}$  do

if  $o_{t,i} \in O$  then

 $O_{c} \leftarrow \{o_{t,i}\} \cup O_{c}$ 

end if

end for

if  $O_{c} == \emptyset$  then

 $O_{t} \leftarrow \emptyset, d_{min} \leftarrow +\infty$ 

for all  $o_{i} \in O$  do

 $u_{o_{i}} \leftarrow U^{a}(o_{i})$ $d_{t,o_{i}}^{a} \leftarrow \phi_{t}^{a} - u_{o_{i}}^{a}$ 

if  $d_{t,o_{i}}^{a} \geq 0$  then

 $O_{t} \leftarrow \{o_{i}\} \cup O_{t}$ 

if  $d_{t,o_{i}}^{a} &lt; d_{min}$  then

 $d_{min} \leftarrow d_{t,o_{i}}^{a}$ 

end if

end for

for all  $o_{t,i} \in O_{t}$  do

 $u_{o_{t,i}}^{a} \leftarrow U^{a}(o_{t,i})$ $d_{t,o_{t,i}}^{a} \leftarrow \phi_{t}^{a} - u_{o_{t,i}}^{a}$ 

if  $d_{t,o_{t,i}}^{a} == d_{min}$  then

 $O_{c} \leftarrow \{o_{t,i}\} \cup O_{c}$ 

end if

end for

end if

return  $O_{c}$
</div>

Let set $\mathbf { 0 } = \{ o _ { i } | i \in [ 1 , I ] \}$ be all possible offers that Agent a can choose during a negotiation, set $\mathbf { 0 } _ { \mathbf { c } } = \{ o _ { j } ^ { c } | j \in [ 1 , J ] \}$ contains Agent a's all possible counter-offers at round t, and $\mathbf { 0 } _ { \mathbf { c } } \subseteq \mathbf { 0 } .$ . Then the counter-offer $o _ { j } ^ { c }$ is selected as follows.

$$
o _ {j} ^ {c} = \forall o _ {i} \in \mathbf {0}, \exists o _ {j} ^ {c} \in \mathbf {0} \Rightarrow d _ {t, o _ {j} ^ {c}} ^ {a} <   d _ {t, o _ {i}} ^ {a} \cap d _ {t, o _ {j} ^ {c}} ^ {a} \geq 0\tag{12}
$$

and

$$
\forall o _ {k} ^ {c} \in \mathbf {0} _ {\mathbf {c}}, \forall o _ {j} ^ {c} \in \mathbf {0} _ {\mathbf {c}}, k \neq j \Rightarrow d _ {t, o _ {k} ^ {c}} ^ {a} = d _ {t, o _ {j} ^ {c}} ^ {a}\tag{13}
$$

where function $d _ { t , o _ { i } } ^ { a }$ indicates the distance between Agent a's expected utility $\phi _ { t } ^ { a }$ and the offer $0 _ { i } { ' } S$ utility $u _ { o _ { i } } ^ { a }$ at the negotiation t.

Based on the above description, the offer generation function by considering both the non-monotonic and discrete utility function is given in Algorithm 3, and the three major steps are given below as well.

Step 1 According to an agent's negotiation decision function, the agent calculates its expected utility at the negotiation round t;

Step 2 According to the agent's nonlinear utility function, <sup>fi</sup>rstly the agent tries to <sup>fi</sup>nd the offers which can bring the exact same pro<sup>fi</sup>t as its expected utility. If such offers cannot be found, then the agent tries to <sup>fi</sup>nd the offer/s which can reach the expected utility as much as possible from its offer candidates;

Step 3 The agent makes a decision whether to accept the opponent's offer (see Section 4 for detail), and send the counter-offer/s in necessary.

As shown in Algorithm 3, when the agent employs the nonmonotonic and discrete utility function, the complexity of counteroffer generation is the combination of Algorithms 1 and 2. Therefore, the complexity for Algorithm 3 is $T ( n ) \stackrel {  } { = } O ( U ^ { ( - 1 , a ) } ) + 1 2 n + 6 .$

## 4. Negotiation protocol considering nonlinear utility function

In this subsection, a negotiation protocol for agents with nonlinear utility functions is proposed based on Rubinstein's alternating offers protocol [3]. In Section 2, it introduced how an agent makes a decision on whether the counter-offer should be sent to the opponent by considering time constraint. The basic idea is that Agent a compares the utility gained from the opponent $\hat { a } ^ { \prime } s$ offer at the negotiation round $t ( U ^ { a } ( p _ { { \hat { a } }  a } ^ { t } ) )$ and the maximum utility the agent may gain in the following negotiation round $t ^ { \prime } ( U ^ { a } ( p _ { a  \hat { a } } ^ { t ^ { \prime } } ) )$ . If Agent a has the chance to gain more pro<sup>fi</sup>t in the round t′, i.e., $U ^ { a } ( p _ { a  \hat { a } } ^ { t ^ { \prime } } ) > U ^ { a } ( p _ { \hat { a }  a } ^ { t } )$ , then Agent a will reject opponent a^'s offer $p _ { \hat { a } \to a } ^ { t }$ and send the counter-offer $p _ { a  \hat { a } } ^ { t ^ { \prime } } .$ Otherwise, Agent a will accept opponent a^'s offer and gain $U ^ { a } ( p _ { \hat { a } \to a } ^ { t } )$ utility. However, such a decision making procedure is based on an assumption that all negotiation agents employ the linear utility functions, and may not maximize agents' pro<sup>fi</sup>ts when the nonmonotonic utility functions are employed. In this section, we extends the Rubinstein's alternating offer protocol to make it suitable in negotiations when non-monotonic utility functions are employed by agents. Basically, agents may have three typical actions in each negotiation, $\mathrm { i . e . , }$ quit the negotiation, accept the opponent's offer, and send the counter-offer. Eq. (14) indicates how an agent selects its actions in each negotiation round by considering negotiation round, opponent's offer, and its counter-offer.

$$
A c t ^ {a} (t) = \left\{ \begin{array}{l} \mathbf {Q u i t}, \text {when} t = \tau^ {a} \wedge \max \Big (U ^ {a} \Big (\mathbf {p} _ {\tilde {a} \to \mathbf {a}} ^ {\mathbf {t}} \Big) \Big) <   0, \\ \mathbf {A c c e p t} p _ {\tilde {a} \to a} ^ {* t}, \text {when} t \leq \tau^ {a} \wedge U ^ {a} \Big (p _ {\tilde {a} \to a} ^ {* t} \Big) \geq \Phi^ {a} (t + 1), \\ \mathbf {O f f e r} \mathbf {p} _ {\mathbf {a} \to \tilde {\mathbf {a}}} ^ {\mathbf {t} + 1}, \text {when} t + 1 \leq \tau^ {a} \wedge U ^ {a} \Big (p _ {\tilde {a} \to a} ^ {* t} \Big) <   \Phi^ {a} (t + 1). \end{array} \right.\tag{14}
$$

where $\tau ^ { a }$ is the Agent a's negotiation deadline, $U ^ { a } ( \bullet )$ is the Agent a's utility function, set $\mathbf { p _ { a  a } ^ { t } }$ contains all offers from the opponent a^ to the Agent $a , p _ { \hat { a } \to a } ^ { * t }$ is the best offer from the opponent and is de<sup>fi</sup>ned in Eq. (15).

$$
p _ {\hat {a} \rightarrow a} ^ {* t} = \forall p _ {\hat {a} \rightarrow a} ^ {t} \in \mathbf {p} _ {\hat {\mathbf {a}} \rightarrow \mathbf {a}} ^ {\mathbf {t}}, \exists p _ {\hat {a} \rightarrow a} ^ {* t} \Rightarrow U ^ {a} \left(p _ {\hat {a} \rightarrow a} ^ {t *}\right) \geq U ^ {a} \left(p _ {\hat {a} \rightarrow a} ^ {t}\right)\tag{15}
$$

$\mathbf { p } _ { \mathbf { a } \to \hat { \mathbf { a } } } ^ { \mathbf { t } + 1 }$ contains all counter-offer/s from the Agent a to the opponent a^ at round $t + 1$ , and are calculated by the offer generation algorithm 3. The detail action selection procedure is introduced in Algorithm 4.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4 Negotiation protocol considering nonlinear utility function

Input: Agent a's utility function  $U^{a}(\cdot)$ , negotiation decision function  $\Phi^{a}(t)$ , offer generation function  $\Psi^{a}(t)$ , negotiation deadline  $\tau^{a}$ , and the offer/s from opponent  $\hat{a}$  at round t ( $p_{\hat{a}\to a}^{t}$ ).
Output: Agent a's counter-action at the negotiation round t.

 $u_{max}^{t} \leftarrow 0, p_{\hat{a}\rightarrow a}^{*t} \leftarrow nil$ 

for all  $p_{\hat{a}\rightarrow a}^{t} \in p_{\hat{a}\rightarrow a}^{t}$  do

 $u^{t} \leftarrow U^{a}(p_{\hat{a}\rightarrow a}^{t})$ 

if  $u^{t} &gt; u_{max}^{t}$  then

 $u_{max}^{t} \leftarrow u^{t}, p_{\hat{a}\rightarrow a}^{*t} \leftarrow p_{\hat{a}\rightarrow a}^{t}$ 

end if

end for

 $\phi_{t+1}^{a} \leftarrow \Phi^{a}(t+1)$ 

if  $t &lt; \tau$  then

if  $u_{max}^{t} \geq \phi_{t+1}^{a}$  then

return Accept  $p_{\hat{a}\rightarrow a}^{*t}$ 

else

 $p_{a\rightarrow\hat{a}}^{t+1} \leftarrow \Psi^{a}(t+1)$ 

return Reject and send  $p_{a\rightarrow\hat{a}}^{t+1}$ 

end if

else if  $u_{max}^{t} \geq \phi_{t+1}^{a}$  then

return Accept  $p_{\hat{a}\rightarrow a}^{*t}$ 

else

return Quit

end if
</div>

Based on the above description, the extended negotiation protocol when agents employ nonlinear utility functions are summarized as follows:

Step 1 An agent assigns negotiation parameters before a negotiation starts, i.e., the initial offer, reservation offer, utility function, negotiation deadline, and negotiation decision function.

Step 2 The agent calculates its best offer according to the offer generation approach introduced in Section 3 by considering time constraints, and sends offer/s to its opponent.

Step 3 If the opponent accepts any offer, then the negotiation is completed. Otherwise, the opponent will send back the counteroffer/s, and wait for the agent's response. If the current negotiation round is the agent's deadline, then the procedure goes to Step 4. Otherwise, the procedure goes to Step 5.

Step 4 The agent evaluates the opponent's counter-offer/s. If the opponent's counter-offer/s can bring any pro<sup>fi</sup>t to the agent, then the agent will accept the opponent's counter-offer, and the negotiation succeeds with an agreement. If none of the opponent's counter-offer/s can bring any bene<sup>fi</sup>t to the agent, then the agent will reject all the opponent's offer/s, and the negotiation fails.

Step 5 The agent calculates its offer for the next negotiation round according to the offer generation approach introduced in Section 3. If the opponent's counter-offer can bring more profit to the agent than the agent's offer for the next round, then the agent will accept the opponent's offer, and the negotiation succeeds with an agreement. If none of the opponent's counteroffer/s can exceed the agent's offer for the next round, then the agent will send the offers to the opponent, and the negotiation procedure goes back to Step 3.

## 5. Experiment

In this section, we demonstrate the negotiation procedure by employing the proposed negotiation approach between two agents with nonlinear utility functions.

## 5.1. Setting

We simulate the negotiation between a female patient and her dentist on appointment making. Both the patient and the dentist have their own preferences on schedule, and their preferences distribute nonlinearly in a day. Brie<sup>fl</sup>y speaking, a female patient wants to make an appointment with her dentist. The patient usually needs to deliver her children to school in the morning (9:00–9:30) and picks up them from school in the afternoon (16:00–16:30). So she prefers not to make an appointment during school hours. However, if her dentist's timetable is full, and she has no other options, she will also accept an appointment during the school hours, and ask her neighbor to give a lift to her children. Also, she prefers to avoid lunch time (12:30–1:30), and the time during her favorite TV program (14:00–14:30). Therefore, this patient's preference for an appointment time is a nonlinear function, which is illustrated in Fig. 7. During the negotiation, the patient is represented by Agent p.

![](/api/attachments/VWAE22UB/fulltext/images/27ee0d5b3f185e264a605eec7a07b871b974b3bde3f94a492e1004467849a1e3.jpg)  
Fig. 7. The patient's preference on her timetable.

![](/api/attachments/VWAE22UB/fulltext/images/f9c0c5d66999a8b04902a93ed966d086d7d5f817ef7a7306955673973fab073b.jpg)  
Fig. 8. The dentist's preference on his timetable.

On the other hand, the dentist's working hours are between 8:00 and 18:00. But he tries to avoid appointments in the early morning (8:00–9:00), lunch time (13:00–14:00), and late afternoon (17:30– 18:00). Also, he already had two appointments at 10:00–11:00 and 14:00–16:00. Therefore, the dentist's preference for the appointment time is a nonlinear and discrete function, which is illustrated in Fig. 8. During the negotiation, the dentist is represented by Agent d.

In order to simplify the negotiation procedure, both Agents p and d employ linear negotiation decision functions (the correctness of the proposed mechanism is independent on the selection of the negotiation decision function), and set their negotiation deadlines to the 10th round. By employing the proposed multiple offer mechanism and the approximating offer mechanism, Agents p and d can ef<sup>fi</sup>ciently generate and exchange their offers during the negotiation. Both the patient agent's and the dentist agent's offers in each negotiation round are generated and displayed in Figs. 10 and 11, respectively. It can be seen that because both agents' utility functions are non-monotonic, they send multiple offers in each negotiation round. The detailed negotiation procedure is displayed in Fig. 9.

In Fig. 9, the x-axis indicates the patient agent's utility, and the y-axis indicates the dentist agent's utility. The solid line indicates the dentist agent's offers in each round, and the negotiation round is marked by the Greek numerals (I, II, III, …). The broken line indicates the patient agent's offers, and the negotiation round is marked by the Roman numerals (1, 2, 3, …). According to the patient agent's offer generation function (Fig. 10), the patient agent sends two offers (i.e., 11:00 and 15:00) in the <sup>fi</sup>rst negotiation round. These two offers bring the same utility (i.e., utility equals 1.0) to the patient agent, but different utilities to the dentist agent. According to the dentist agent's utility function (Fig. 8), the <sup>fi</sup>rst offer (11:00) can bring him a utility value of 0.6, while the utility value of the second offer (15:00) is zero. However, since both offers from the patient agent failed in reaching the dentist agent's expectation, the dentist agent rejected them, and sent counter-offers, i.e., 10:00 and 16:00. Both the counteroffers can bring 0.8 utility to the dentist and 0.6 utility to the patient agent. Because the patient's expected utility in the following negotiation round is 0.9, so the patient rejects the dentist's counter-offers, then the negotiation goes into the second round.

![](/api/attachments/VWAE22UB/fulltext/images/9a06f6c01e5a6b2dc91bd9591d4ea856f5cd2bb0059a9326c15b826eed63956c.jpg)  
Fig. 9. The comparison between the dentist's utilities and the patient's utilities.

![](/api/attachments/VWAE22UB/fulltext/images/313878df5811fbc67d29b3dd4d100dd0d6cd189c7b6a5fa8406c43c101fca9ce.jpg)  
Fig. 10. The patient's offers in each negotiation round.

In the second round, the patient agent sent four offers together (i.e., 10:45, 11:15, 14:45 and 15:15) to the dentist agent. Except the offer 11:15 takes 0.575 utility to the dentist agent, the other three offers' utilities for the dentist are 0. Because 0.575 is smaller than the dentist agent's expectation in the second round (i.e., 0.9 utility), the dentist agent rejected the four offers and still sent 10:00 and 16:00 as counter-offers to the patient agent. It should be mentioned that the dentist agent sent the same counter-offers as in the <sup>fi</sup>rst round because the dentist's utility function is discrete and these two counter-offers maximized the dentist's utility in the <sup>fi</sup>rst three rounds. Because the patient agent's utility function is still nonlinear, even though the dentist agent's counter-offers are rejected by the patient agent in the <sup>fi</sup>rst negotiation round, they still may be accepted by the patient in the second round. Therefore, in a negotiation when nonlinear utility functions are considered, agents should be allowed to send the same offers to the opponents in different negotiation rounds. In this experiment, the patient agent rejected these two counter-offers again because their utilities are smaller than the patient's expected utility in the third round, i.e., 0.8 utility. Therefore, the negotiation goes into the third round.

In the third round, the patient agent sent another four offers to the dentist agent, i.e., 10:30, 11:30, 14:30 and 15:30. Only the offer 11:30 can bring 0.55 utility to the dentist agent, and the dentist cannot get any utility from the other three offers. However, because 0.55 is still smaller than the dentist's expected utility (i.e., 0.8) in the this round, the dentist agent denied all the four offers and send the similar counter-offers as it did in the <sup>fi</sup>rst two negotiation rounds. Again, the dentist agent's counter-offers (i.e., 10:00 and 16:00) can only bring 0.6 utility, and fails to reach the patient's expected utility (i.e., 0.7) in the fourth negotiation round. Therefore, the patient agent rejects the dentist agent's two counter-offers, and the negotiation proceeded to the fourth round.

In the fourth round, the patient agent modi<sup>fi</sup>ed its offers and send them to the dentist agent, i.e., 10:15, 11:45, 14:15 and 15:45. These offers bring 0.7 utility to the patient, and maximally bring 0.525 utility to the dentist. Because the dentist agent's expected utility in this round is 0.6, so the dentist agent rejected these four offers, and sent two counter-offers (i.e., 9:30 and 16:30). The dentist agent's counter-offers can only bring 0.35 utility to the patient agent, which is smaller than the patient agent's expected utility (i.e., 0.6) in the <sup>fi</sup>fth negotiation round. Therefore, the dentist agent rejected these two counter-offers, and the negotiation proceeded to the <sup>fi</sup>fth round.

![](/api/attachments/VWAE22UB/fulltext/images/f9e8aa48ae342b3c21f3d68865dd2e174201890f4b2fe45941a136464d2f77be.jpg)  
Fig. 11. The dentist's offers in each negotiation round.

Table 1  
Ten samplings for the dentist and the patient.

<table><tr><td colspan="2">Patient</td><td colspan="2">Dentist</td></tr><tr><td>Offer</td><td>Utility</td><td>Offer</td><td>Utility</td></tr><tr><td>8:30</td><td>0.35</td><td>8:30</td><td>0.5</td></tr><tr><td>9:30</td><td>0.35</td><td>9:30</td><td>0.7</td></tr><tr><td>10:30</td><td>0.8</td><td>10:30</td><td>0</td></tr><tr><td>11:30</td><td>0.8</td><td>11:30</td><td>0.55</td></tr><tr><td>12:30</td><td>0.4</td><td>12:30</td><td>0.45</td></tr><tr><td>13:30</td><td>0.4</td><td>13:30</td><td>0.2</td></tr><tr><td>14:30</td><td>0.8</td><td>14:30</td><td>0</td></tr><tr><td>15:30</td><td>0.8</td><td>15:30</td><td>0</td></tr><tr><td>16:30</td><td>0.3</td><td>16:30</td><td>0.7</td></tr><tr><td>17:30</td><td>0.3</td><td>17:30</td><td>0.4</td></tr></table>

Finally, the agreement was reached at the 5th negotiation round. In the 5th negotiation round, the patient agent sent four equivalent offers to the dentist agent, i.e., 10:00, 12:00, 14:00 and 16:00. All these four equivalent offers bring the same utility (0.6) to the patient agent, but different utilities to the dentist agent. According to the dentist agent's utility function (see Fig. 8), two of the patient agent's offers (10:00 and 16:00) brought the utility value of 0.8 to the dentist agent. Because the dentist agent's expected utility in the 5th round is only 0.6, so the dentist agent would take either one of these two offers as the agreement. The detail negotiation process is illustrated in Fig. 9, and each agent's offers and evaluations are listed in Table 2.

We also compare our proposed approach with two related approaches in literature. Firstly, we employed Ito et al.'s approach [8] on the above scheduling problem. According to the Ito's approach, we <sup>fi</sup>rstly select ten samplings for both the dentist and the patient. The samplings are displayed in Table 1. Then a mediator agent was employed to explore the table to search for the sampling candidates which could bring the maximal utility by considering both the dentist and patient. Finally, the offer 11:30 was selected as the agreement because it brings the largest pro<sup>fi</sup>t (i.e., 0.8 for the patient, 0.55 for the dentist, and 1.35 as total) by considering both dentist and patient. By comparing the agreements (i.e., 10:00 and 16:00) achieved by using our proposed approach, the agreement achieved by using Ito's approach brought higher pro<sup>fi</sup>t to the patient $( 0 . 8 > 0 . 6 )$ , but lower pro<sup>fi</sup>ts to the dentist $( 0 . 5 5 < 0 . 8 )$ . Therefore, the overall pro<sup>fi</sup>t generated by our approach is better than Ito's approach, i.e., $1 . 4 > 1 . 3 5 .$ However, Ito's approach is greatly impacted by the selection of samplings. If suitable samplings could be found, Ito's approach could also theoretically reach the same agreement as our approach. Nevertheless, the selection of suitable samplings and non-bias mediator agent are not easy in real-world applications, and our approach avoids these two procedures.

In the second comparison, we employed the approach proposed by Fatima et al. [5], i.e., to approximate the dentist and the patient's nonlinear utility functions to linear utility functions, then use the well-known NDF approach teFaratin: 1998: NDF to <sup>fi</sup>nd the agreement. For the patient, the approximated linear utility function is $U ( x ) = - 0 . 0 9 x + 1 . 7 2$ ; and for the dentist, the approximated linear utility function is $U ( x ) = 0 . 0 6 x - 0 . 2 8$ . We set the negotiation deadline for both dentist and patient as the 10th round, and employed the NDF approach to <sup>fi</sup>nd the agreement. In this experiment, the <sup>fi</sup>nal agreement reached by using Fatima's approach is 13:20. According to the original utility functions of the dentist and the patient, such an agreement only can bring around 0.27 utility to the patient and around 0.3 utility to the dentist. Obviously, the result generated by approximating nonlinear utility function to linear utility function is worse than Ito's and our proposed approaches. Therefore, the approximating approach should be avoided when an agent's utility function has high nonlinear relationship between the issue's value and the utility.

Table 2  
Negotiation process between the patient and dentist agents.

<table><tr><td>Round</td><td>Agent</td><td>Expected utility</td><td>maximal gained</td><td>Counter-offers</td></tr><tr><td rowspan="2">1</td><td>Patient</td><td>1.0</td><td>0.0</td><td>11:30, 15:00</td></tr><tr><td>Dentist</td><td>1.0</td><td>0.6</td><td>10:00, 16:00</td></tr><tr><td rowspan="2">2</td><td>Patient</td><td>0.9</td><td>0.6</td><td>10:45, 11:15, 14:45, 15:15</td></tr><tr><td>Dentist</td><td>0.9</td><td>0.575</td><td>10:00, 16:00</td></tr><tr><td rowspan="2">3</td><td>Patient</td><td>0.8</td><td>0.6</td><td>10:30, 11:30, 14:30, 15:30</td></tr><tr><td>Dentist</td><td>0.8</td><td>0.55</td><td>10:00, 16:00</td></tr><tr><td rowspan="2">4</td><td>Patient</td><td>0.7</td><td>0.6</td><td>10:15, 11:45, 14:15, 15:45</td></tr><tr><td>Dentist</td><td>0.7</td><td>0.525</td><td>9:30, 16:30</td></tr><tr><td rowspan="2">5</td><td>Patient</td><td>0.6</td><td>0.35</td><td>10:00, 12:00, 14:00, 16:00</td></tr><tr><td>Dentist</td><td>0.6</td><td>0.8</td><td>Agreement (10:00 or 16:00)</td></tr></table>

## 5.2. Discussion

In this section, we demonstrate the negotiation procedure between two agents with nonlinear utility functions by employing the proposed negotiation model. It was shown that the proposed negotiation model can ef<sup>fi</sup>ciently handle the negotiations when agents employ the nonlinear utility functions, and successfully help agents to reach the agreement.

During the experiment, two interesting phenomenons were noticed by us and worth to be discussed here. The <sup>fi</sup>rst phenomenon is the repeating offer. It can be seen from the Table 2 that the offers 10:00 and 16:00 were exchanged between the dentist agent and the patient agent for several times before the both agents agreed on these offers. It is known that in a general negotiation, where all agents employ linear utility functions, the same offer will not be repeated by an agent. That is because if an offer is rejected by an opponent, then the same offer will de<sup>fi</sup>nitely be rejected again by the same opponent in the following negotiation rounds. However, when agents employ the non-monotonic utility functions, the situation was changed. An agent may reject an offer in one negotiation round, but accept the same offer latter. That is because the relationship between the value of an offer and the utility gained from the offer is non-monotonic. When agents make negotiation decision based on the negotiation decision function, a rejected offer may be accepted later when agents modify their expected utility. Researches on how to eliminate or decrease such a repeat when non-monotonic utility functions are employed may be a possible consideration to improve the ef<sup>fi</sup>ciency of agent negotiation in nonlinear domains.

The second interesting phenomenon is the multiple agreement candidates. It can be seen from Table 2 that two equivalent agreement candidates (i.e., 10:00 and 16:00) are reached <sup>fi</sup>nally, and agents can choose either one as the <sup>fi</sup>nal agreement. Of course, such a problem does not exist when agents generate only one offer. However, when agents employ nonlinear utility functions, multiple equivalent offers may exchanged between agents, then how to make a reasonable selection between equivalent offers may become another interesting research topic. Besides the utility gained from an offer, other judgments may be considered to maximize the agent's overall utility. For example, regarding to the case shown in this experiment, the dentist may choose a candidate as the <sup>fi</sup>nal agreement by considering future possible appointments with other patients; while the patient may select between the equivalent agreement candidates by considering other possible new activities or changes on her timetable.

## 6. Related work

Many works on agent negotiation considering nonlinear utility have been done by other researchers. To list a few of them, Fatima et al. [6] studied bilateral multi-issue negotiation between selfinterested agents whose utility functions are nonlinear. The authors argued that even though the package deal procedure led multiple negotiations to Pareto optimal, however computing the equilibrium for the package deal procedure is not always easy, especially for nonlinear utility functions. In order to solve such a problem, the authors introduced two approaches: (i) to approximate nonlinear utility functions by linear functions, then an approximate equilibrium can easily be reached based on the approximate linear function; and (ii) to use the simultaneous procedure to negotiate issues in parallel but independently. By employing these two approaches, the approximate equilibrium can be found in polynomial time. This paper also showed that although the package deal procedure is known to generate Pareto optimal outcomes, the simultaneous procedure outperforms in some cases by considering economic properties. By comparing with Fatima's work, the advantages of our work are that we distinguished the differences between non-monotonic and discrete utility functions. However, we did not consider the multiple issue negotiation in this paper.

Ito and Klein [7] proposed a negotiation protocol for multi-issue negotiation and extended it for nonlinear utility domains. The protocol is based on a combinatorial auction protocol. In [8,9], Ito et al. proposed an auction-based negotiation protocol among nonlinear utility agents. This model considered nonlinear utility functions, and interdependency among multi-issue. In order to reach Pareto ef<sup>fi</sup>ciency, a sampling process is <sup>fi</sup>rstly performed on each negotiator's utility space, and these samples were adjusted in order to get more feasible contracts. Then each negotiator makes bids, and a mediator is employed to <sup>fi</sup>nd combinations of bids and to maximize the total value of the bids. The experimental results indicated good performance compared with other negotiation methods. By comparison with Ito's work, the advantage of our work is that we did not employ a third-part for decision making during negotiation. However, the disadvantage of our work is that we did not take the multi-issue negotiation into account.

Klein et al. [10] proposed a simulated annealing based negotiation model to consider multiple inter-dependent issues and large contract spaces. In order to achieve near-optimal social welfare for negotiation with binary issue dependencies, a negotiation approach was proposed to make substantial progress towards achieving a “win–win” negotiation outcome. An annealing mediator was employed to analyze negotiators' feedback on their opponents' offers, and to make new proposals to increase the social welfare. The difference between Klein's work and our work is that we proposed a model to bridge the gap between linear utility agents and nonlinear utility agents and a mechanism for offer generating, so as to increase the utilities for both negotiators.

Robu et al. [17] proposed an agent strategy for bilateral negotiations over multi-issue with inter-dependent valuations. The authors employed ideas inspired by graph theory and probabilistic in<sup>fl</sup>uence networks to derive ef<sup>fi</sup>cient heuristics for multi-issue negotiations. A utility graph was employed to represent complex utility functions, and the best counter-offer was generated through searching the whole utility graph. The experimental results indicated that their proposed utility graph approach can successfully handle interdependent issues, and navigate the contract space to reach Pareto ef<sup>fi</sup>ciency ef<sup>fi</sup>ciently. However, their work is based on an assumption that the utility functions employed by agents are decomposable. We do not make any assumption on agent utility functions in this paper.

Carbonneau et al. [2] proposed a pairwise issue modeling to predict the opponent's counter-offers during a negotiation. Issues in different types, such as continuous, discrete and ordinal, are considered. The authors employed the multiple linear regression approach to handle the counter-offer prediction when issues are continuous, and the neural network to handle the counter-offer prediction when issues are discrete and ordinal. Firstly, the negotiation issues are divided into pairs, i.e., a primary issue and a secondary issue, according to the permutations of all issues. Then for each pair, by using the historical offers and the pairwise neural network, the expected counter-offer on the primary issue in a pair can be predicted. This paper pointed out a possible solution for us when we try to extend our work to the multiple issue negotiation.

Luo et al. [12] proposed a multiagent-based solution to the nonmonotonic utility negotiation in meeting scheduling problem by using the Fuzzy constraints. Firstly, a coordinator agent was employed to generate a proposal time slot to all meeting participator by considering the membership function of each constraint in the scheduling and the priority of each participator. Secondly, each participator agent responded to the proposal based on their own timetable, constraints and preferences. Thirdly, the coordinator agent combined all other agents' responses to a single value by using the proposed fusion operators and made the <sup>fi</sup>nal decision on the timetable. By comparison with our approach, a coordinator agent is required in Luo's approach to take all work on proposal generation and evaluation, and decision making. As the number of participator become large, the complexity of scheduling will dramatically increase and the coordinator agent will have dif<sup>fi</sup>culties to generate the proposals in an ef<sup>fi</sup>cient way. However, our approach employs decentralized decision making strategy, and each agent manages self's negotiation plan and behaviors.

## 7. Conclusion and future work

In this paper, a bilateral single-issue negotiation model was proposed to handle nonlinear utility functions. A 3D model was proposed to illustrate the relationships between an agent's utility function, negotiation decision function, and time constraint. A multiple offer mechanism was introduced to handle non-monotonic utility functions, and an approximating offer mechanism was introduced to handle discrete utility functions. Finally, these two mechanisms were combined to handle nonlinear utility functions in more general situations. The procedure of how an agent generated its counter offers by employing the proposed 3D model and negotiation mechanisms was also introduced. The experimental results indicated that the proposed negotiation model and mechanisms can ef<sup>fi</sup>ciently handle nonlinear utility agents, and successfully lead the negotiation to an agreement.

The future work of this research will pay attention to multiple issue negotiations with nonlinear utility functions. The negotiation model and mechanisms presented in this paper will be further extended by considering an agent's nonlinear preference on negotiated issues. Lastly, an extended negotiation protocol will be developed to search for Pareto ef<sup>fi</sup>ciency in multi-issue negotiation between nonlinear utility agents.

## References

[1] J. Brzostowski, R. Kowalczyk, Predicting partner's behaviour in agent negotiation, Proc. of 5th Int. Conf. on Autonomous Agents and Multiagent Systems (AAMAS06), 2006.pp.355-361.

[2] R. Carbonneau, G. Kersten, R. Vahidov, Pairwise issue modeling for negotiation counteroffer prediction using neural networks, Decision Support Systems (2011) 449-459.

[3] P. Faratin, C. Sierra, N. Jennings, Negotiation decision functions for autonomous agents, Journal of Robotics and Autonomous Systems 24 (3–4) (1998) 159–182.

[4] S. Fatima, M. Wooldridge, N. Jennings, An agenda-based framework for multiissue negotiation, Arti<sup>fi</sup>cial Intelligence 152 (1) (2004) 1–45.

[5] S. Fatima, M. Wooldridge, N. Jennings, Approximate and online multi-issue negotiation, Proc. of 6th Int. Conf. on Autonomous Agents and Multi-Agent Systems (AAMAS07), 2007, pp. 947–954.

[6] S. Fatima, M. Wooldridge, N. Jennings, An analysis of feasible solutions for multi-issue negotiation involving nonlinear utility functions, Proc. of 8th Int Conf. on Autonomous Agents and Multiagent Systems (AAMAS09), 2009, pp. 1041–1048.

[7] T. Ito, M. Klein, A multi-issue negotiation protocol among competitive agents and its extension to a nonlinear utility negotiation protocol, Proceedings of the 5th Int. Conf. on Autonomous Agents and Multiagent Systems (AAMAS2006), 2006, pp. 435–437.

[8] T. Ito, H. Hattori, M. Klein, Multi-issue negotiation protocol for agents: exploring nonlinear utility spaces, Proceedings of the 20th Int. Conf. on Arti<sup>fi</sup>cial Intelligence, 2007, pp. 1347–1352.

[9] T. Ito, M. Klein, H. Hattori, A multi-issue negotiation protocol among agents with nonlinear utility functions, Multiagent and Grid Systems 4 (1) (2008) 67–83.

[10] M. Klein, P. Faratin, H. Sayama, Y. Bar-Yam, Negotiating complex contracts, Group Decision and Negotiation 12 (2) (2003) 111–125.

[11] X. Luo, N. Jennings, A spectrum of compromise aggregation operators for multi-attribute decision making, Arti<sup>fi</sup>cial Intelligence 171 (2) (2007) 161–184.

[12] X. Luo, H. Leung, J. Lee, Theory and properties of a sel<sup>fi</sup>sh protocol for multi-agent meeting scheduling using fuzzy constraints, Proceedings of the 14th European Conference on Arti<sup>fi</sup>cial Intelligence, 2000, pp. 373–377.

[13] V. Narayanan, N. Jennings, An adaptive bilateral negotiation model for e-commerce settings, Proceedings of the Seventh IEEE Int. Conf. on E-Commerce Technology, 2005, pp. 34–41.

[14] V. Narayanan, N. Jennings, Learning to negotiate optimally in non-stationary environments, Proceedings on the 10th Int. Workshop on Cooperative Information Agents, Springer, 2006, pp. 288–300.

[15] M. Osborne, A. Rubenstein, A Course in Game Theory, The MIT Press, Cambridge, Massachusetts, 1994.

[16] F. Ren, M. Zhang, K. Sim, Adaptive conceding strategies for automated trading agents in dynamic, open markets, Decision Support Systems 46 (3) (2009) 704–716.

[17] V. Robu, D. Somefun, J. Poutré, Modeling complex multi-issue negotiations using utility graphs, Proceedings of the 4th Int. Conf. on Autonomous Agents and Multiagent Systems (AAMAS05), 2005, p. 287.

![](/api/attachments/VWAE22UB/fulltext/images/783973de05da995df859cca8a19cd4dc31cf23715b6258ceb7d8ac6b60a1048d.jpg)  
Dr. Fenghui Ren (www.uow.edu.au/\~fren) received his MCompSc-Res. and Ph. D. from the University of Wollongong in 2006 and 2010, respectively. He received his BCompSc from the Xidian University in 2003. Currently, he is the Vice Chancellor's Fellow in the School of Computer Science and Software Engineering at the University of Wollongong. Dr. Ren is an active researcher and published 38 research papers in reputable journals and conferences. His research interests include agent-based modeling, simulation, reasoning and learning, agent coordination, negotiation and opti mization.

![](/api/attachments/VWAE22UB/fulltext/images/79d251e577f684e3ea391c2b1b17ba846dd7d351a4949a52136665cc9012e9ec.jpg)

Dr Minjie Zhang is an associate professor in School of Computer Science and Software Engineering and the Director of Intelligent System Research Group in the Faculty of Informatics, at University of Wollongong, Australia. She received a BSc degree from Fudan University China in 1982, and her PhD degree from the University of New England, Australia in 1996. Dr Zhang is an active researcher and published over 130 research papers. She is a program chair for a number of international workshops and conferences. As a guest editor, Dr Zhang jointly edited 5 special issues and 6 books. She is the chief investigator for more than 10 different research grants including an ARC (Australia Research Council) Discovery grant and an ARC Linkage Grants. Her research interests include multi-agent systems,

agent-based simulation and modeling in complex domains, agent-based mart grids and knowledge discovery and data mining.
