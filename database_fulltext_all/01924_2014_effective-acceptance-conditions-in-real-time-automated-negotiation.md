---
otero_id: 1924
otero_key: "KN6KECMC"
title: "Effective acceptance conditions in real-time automated negotiation"
authors: "Tim Baarslag; Koen Hindriks; Catholijn Jonker"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.021"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Tim Baarslag ⁎, Koen Hindriks, Catholijn Jonker

Interactive Intelligence Group, Delft University of Technology, Mekelweg 4, Delft, The Netherlands

a r t i c l e i n f o

Available online 5 June 2013

Keywords: Automated negotiation Real-time bilateral negotiation Acceptance criteria Acceptance conditions When to accept

## a b s t r a c t

In every negotiation with a deadline, one of the negotiating parties must accept an offer to avoid a break off. As a break off is usually an undesirable outcome for both parties, it is important that a negotiator employs a pro<sup>fi</sup>cient mechanism to decide under which conditions to accept. When designing such conditions, one is faced with the acceptance dilemma: accepting the current offer may be suboptimal, as better offers may still be presented before time runs out. On the other hand, accepting too late may prevent an agreement from being reached, resulting in a break off with no gain for either party, Motivated by the challenges of bilateral negotiations between automated agents and by the results and insights of the automated negotiating agents competition (ANAC), we classify and compare state-of-the-art generic acceptance conditions. We perform extensive experiments to compare the performance of various acceptance conditions in combination with a broad range of bidding strategies and negotiation scenarios. Furthermore we propose new acceptance conditions and we demonstrate that they outperform the other conditions. We also provide insight into why some conditions work better than others and investigate correlations between the properties of the negotiation scenario and the ef<sup>fi</sup>cacy of acceptance conditions.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Negotiation is an important process to reach trade agreements, and to form alliances or resolve con<sup>fl</sup>icts. The <sup>fi</sup>eld of negotiation originates from various disciplines including arti<sup>fi</sup>cial intelligence, economics, social science, and game theory (e.g., [2,20,25]). The strategic-negotiation model has a wide range of applications, such as resource and task allocation mechanisms, con<sup>fl</sup>ict resolution mechanisms, and decentralized information services [20,32].

A number of successful negotiation strategies have already been established both in literature and in implementations, (e.g. [6,8,9,14,15,22]). And more recently, in 2010 seven new negotiation strategies were created to participate in the <sup>fi</sup>rst automated negotiating agents competition (ANAC 2010) [3] in conjunction with the Ninth International Conference on Autonomous Agents and Multiagent Systems (AAMAS-10). During post tournament analysis of the results, it became apparent that different agent implementations use various conditions to decide when to accept an offer. It is important for every negotiator to employ such a mechanism to decide under which conditions to accept, because in every negotiation with a deadline, one of the negotiating parties has to accept in order to avoid a break off. However, designing a proper acceptance condition is a dif<sup>fi</sup>cult task: accepting too late may result in the break off of a negoti ation, while accepting too early may result in suboptimal agreements.

The importance of choosing an appropriate acceptance condition is con<sup>fi</sup>rmed by the results of ANAC 2010 (see Table 1). Agents with simple acceptance criteria were ranked at the bottom, while the more sophisticated time- and utility-based criteria obtained a higher score. For instance, the low ranking of Agent Smith was due to a mistake in the implementation of the acceptance condition [33].

Despite its importance, the theory and practice of acceptance conditions has not yet received much attention. The goal of this paper is to classify current approaches and to compare acceptance conditions in an experimental setting. Thus in this paper we will concentrate on the <sup>fi</sup>nal part of the negotiation process: the acceptation of an offer. We focus on decoupled acceptance conditions: i.e., generic acceptance conditions that can be used in conjunction with an arbitrary bidding strategy. The reason for this is straightforward: we want to be able to re-incorporate the acceptance conditions that have been found most effective into new agent designs; therefore, the acceptance conditions under investigation should not be coupled with a speci<sup>fi</sup>c agent implementation.

Our contribution is fourfold:

1. We give an overview and provide a categorization of current decoupled acceptance conditions.

2. We introduce a formal negotiation model that supports the use of arbitrary acceptance conditions.

3. We compare a large selection of current generic acceptance conditions and evaluate them in an experimental setting.

An overview of the rank of every agent in ANAC 2010 and the type of acceptance conditions that they employ. Agents using time and utility based acceptance conditions were ranked at the top, except for Agent Smith, which had a faulty acceptance mechanism.

<table><tr><td>Rank</td><td>Agent</td><td>Acceptance condition</td></tr><tr><td>1</td><td>Agent K</td><td>Time and utility based</td></tr><tr><td>2</td><td>Yushu</td><td>Time and utility based</td></tr><tr><td>3</td><td>Nozomi</td><td>Time and utility based</td></tr><tr><td>4</td><td>IAMHaggler</td><td>Utility based only</td></tr><tr><td>5</td><td>FSEGA</td><td>Utility based only</td></tr><tr><td>6</td><td>IAMcrazyHaggler</td><td>Utility based only</td></tr><tr><td>7</td><td>Agent Smith</td><td>Time and utility based</td></tr></table>

4. We propose new acceptance conditions and test them against established acceptance conditions, using varying types of bidding techniques.

The remainder of this paper is organized as follows. Section 2 de<sup>fi</sup>nes the model of negotiation that we employ and provides an overview of current acceptance conditions. In Section 3, we also consider combinations of acceptance conditions. Section 4 discusses our experimental setup and results, which demonstrate that some combinations outperform traditional acceptance conditions. Finally, Sections 6 and 7 outline our conclusions and our plans for further research on acceptance strategies.

## 2. Acceptance conditions in negotiation

This paper focuses on acceptance conditions (also called acceptance criteria) that are decoupled: i.e. generic acceptance conditions that are not tied to a speci<sup>fi</sup>c agent implementation and hence can be used in conjunction with an arbitrary bidding strategy. We <sup>fi</sup>rst describe a general negotiation model that <sup>fi</sup>ts current decoupled acceptance conditions. We have surveyed existing negotiation agents to examine the acceptance criteria that they employ. We then categorize them according to the input that they use in their decision making process.

## 2.1. Negotiation model

We consider bilateral negotiations, i.e. a negotiation between two parties or agents A and B. The agents negotiate over issues that are part of a negotiation domain, and every issue has an associated range of alternatives or values. A negotiation outcome consists of a mapping of every issue to a value, and the set Ω of all possible outcomes is called the outcome space. The outcome space is common knowledge to the negotiating parties and stays <sup>fi</sup>xed during a single negotiation session.

We further assume that both parties have certain preferences prescribed by a preference profile over Ω. These preferences can be modeled by means of a utility function U, which maps a possible outcome $\omega \in \Omega$ to a real-valued number in the range [0, 1]. In contrast to the outcome space, the preference pro<sup>fi</sup>le of the agents is private information.

Finally, the interaction between negotiating parties is regulated by a negotiation protocol that de<sup>fi</sup>nes the rules of how and when proposals can be exchanged. We use the alternating-offers protocol [29] for bilateral negotiation, in which the negotiating parties exchange offers in turns.

As in [31], we assume a common global time, represented here by $\tau = [ 0 , 1 ] . \mathsf { W } \epsilon$ e supplement the alternating-offers protocol with a deadline at $t = 1 ,$ , at which moment both agents receive utility 0. This is the same setup as [10], with the exception that issues are not necessarily real-valued and both agents have the same deadline equal to $t = 1$ We represent by ${ \boldsymbol { x } _ { A } ^ { t } } _ {  B }$ the negotiation outcome proposed by agent A to agent B at time t. A negotiation thread (cf. [8,31]) between two agents A and B at time $t \in \tau$ is de<sup>fi</sup>ned as a <sup>fi</sup>nite sequence

$$
H _ {A \leftrightarrow B} ^ {t} := \left(x _ {p _ {1} \rightarrow p _ {2}} ^ {t _ {1}}, x _ {p _ {2} \rightarrow p _ {3}} ^ {t _ {2}}, x _ {p _ {3} \rightarrow p _ {4}} ^ {t _ {3}}, \dots , x _ {p _ {n} \rightarrow p _ {n + 1}} ^ {t _ {n}}\right),\tag{1}
$$

which satis<sup>fi</sup>es the following constraints:

1. $t _ { k } \leq t _ { l } \mathrm { f o r } k \leq l ,$ the offers are ordered over time $\tau .$

2. $p _ { k } = p _ { k + 2 } \in \{ A , B \}$ for all k, the offers are alternating between the agents,

3. All $t _ { i }$ represent instances of time , with $t _ { n } \leq t ,$

4. ${ \boldsymbol { x } } _ { p _ { k }  p _ { k + 1 } } ^ { t _ { k } } { \in } \Omega { \mathrm { ~ f o r ~ } } k \in \{ 1 , . . . , n \}$ , the agents exchange complete offers.

Additionally, the last element of ${ \bf \dot { \boldsymbol { H } } } _ { A  B } ^ { t }$ may be equal to one of the particles {Accept, End}. We will say a negotiation thread is active if this is not the case.

When agent A receives an offer $x _ { B  A } ^ { t }$ from agent B sent at time t, it has to decide at a later time $t ^ { \prime } > t$ whether to accept the offer, or to send a counter-offer $\quad x _ { A  B } ^ { t ^ { \prime } } .$ Given a negotiation thread $H _ { A } ^ { t } \gets B$ between agents A and B, we can formally express the action performed by A with an action function $X _ { A } { \mathrm { : } }$

$$
X _ {A} \Big (t ^ {\prime}, x _ {B \to A} ^ {t} \Big) = \left\{ \begin{array}{l l} E n d & \text { if } t ^ {\prime} \geq 1 \\ A c c e p t & \text { if } \mathbf {A C} _ {A} \Big (t ^ {\prime}, x _ {A \to B} ^ {t ^ {\prime}}, H _ {A \leftrightarrow B} ^ {t} \Big) \\ O f f e r x _ {A \to B} ^ {t ^ {\prime}} & \text { otherwise. } \end{array} \right.\tag{2}
$$

Note that we extend the setting of [10,31] by introducing the acceptance condition $\pmb { { \cal A } } \pmb { \mathbb { C } } _ { A }$ of an agent A. When used in this way, the model enables us to study arbitrary decoupled acceptance conditions. The acceptance condition $\pmb { { \cal A } } \pmb { \mathbb { C } } _ { A }$ takes as input

$$
\mathcal {I} = \left(t ^ {\prime}, x _ {A \rightarrow B} ^ {t ^ {\prime}}, H _ {A \leftrightarrow B} ^ {t}\right),\tag{3}
$$

the tuple containing the current time t′, the offer $x _ { A  B } ^ { t ^ { \prime } }$ that the agent considers as a bid (in line with the bidding strategy the agent uses), and the ongoing negotiation thread $H _ { B } ^ { t } \gets A \cdot$

The resulting action given by the function $X _ { A } ( t ^ { \prime } , x _ { B } ^ { t }  A )$ is used to extend the current negotiation thread between the two agents. If the agent does not accept the current offer, and the deadline has not been reached, it will prepare a counter-offer $x _ { A  B } ^ { t ^ { \prime } }$ by using a bidding strategy or tactic to generate new values for the negotiable issues. Tactics can take many forms, e.g. time-dependent, resource dependent, imitative, and so on [31]. In our setup we will consider the tactics as given and try to optimize the accompanying acceptance conditions.

## 2.2. Acceptance criteria

Let an active negotiation thread

$$
H _ {A \leftrightarrow B} ^ {t} = \left(x _ {p _ {1} \rightarrow p _ {2}} ^ {t _ {1}}, x _ {p _ {2} \rightarrow p _ {3}} ^ {t _ {2}}, \dots , x _ {A \rightarrow B} ^ {t _ {n - 1}}, x _ {B \rightarrow A} ^ {t _ {n}}\right),
$$

be given at time $t ^ { \prime } > t = t _ { n } ,$ so that it is agent A's turn to perform an action.

As de<sup>fi</sup>ned by Eq. (1) in our negotiation model, the action function $X _ { A }$ of an agent A uses an acceptance condition $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { A } ( \mathcal { T } )$ to decide whether to accept. In practice, most agents do not use the full negotiation thread to decide whether it is time to accept. For instance many agent implementations, such as [10,11,31], use the following implementation of $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { A } ( \mathcal { T } )$

$$
\mathbf {A C} _ {A} \left(t ^ {\prime}, x _ {A \rightarrow B} ^ {t ^ {\prime}}, H _ {A \leftrightarrow B} ^ {t}\right) \Longleftrightarrow U _ {A} \left(x _ {B \rightarrow A} ^ {t}\right) \geq U _ {A} \left(x _ {A \rightarrow B} ^ {t ^ {\prime}}\right).
$$

That $\mathrm { i } s , A$ will accept when the utility $U _ { A }$ for the opponent's last offer at time t is greater than the value of the offer agent A is ready to send out at time t′. The acceptance condition above depends on the agent's upcoming offer $x _ { A  B } ^ { t ^ { \prime } } .$ For $\alpha , \beta { \in } \mathbb { R }$ this may be generalized as follows:

$$
\mathbf {A C} _ {\text { next }} ^ {\mathcal {I}} (\alpha , \beta) \stackrel {{\text { def }}} {{\Longleftrightarrow}} \alpha \cdot U _ {A} \left(x _ {B \rightarrow A} ^ {t}\right) + \beta \geq U _ {A} \left(x _ {A \rightarrow B} ^ {t ^ {\prime}}\right).\tag{4}
$$

We can view α as the scale factor by which we multiply the opponent's bid, while $\beta$ speci<sup>fi</sup>es the minimal ‘utility gap’ [15] that is suf<sup>fi</sup>cient to accept.

Analogously, we have acceptance conditions [7,12,15,35] that rely on the agent's previous offer $x _ { A - } ^ { t _ { n } . }$ <sup>−1</sup> :

$$
\mathbf {A C} _ {\text { prev }} ^ {\mathcal {I}} (\alpha , \beta) \stackrel {{\text { def }}} {{\Longleftrightarrow}} \alpha \cdot U _ {A} \left(x _ {B \to A} ^ {t}\right) + \beta \geq U _ {A} \left(x _ {A \to B} ^ {t _ {n - 1}}\right).\tag{5}
$$

Note that this acceptance condition does not take into account the time that is left in the negotiation, nor any offers made previous to time t. However, it is important to bear in mind that the behavior of the acceptance condition may still be in<sup>fl</sup>uenced implicitly by these factors, because of the possibility that the bidding strategy takes such factors into account.

Other acceptance conditions may rely on other measures, such as the remaining negotiation time or a utility threshold. For example, there is a very simple acceptance criterion [7,33,35] that only compares the opponent's previous offer with a threshold α:

$$
\mathbf {A C} _ {\text { const }} ^ {\mathcal {I}} (\alpha) \stackrel {{\text { def }}} {{\Longleftrightarrow}} U _ {A} \left(x _ {B \to A} ^ {t}\right) \geq \alpha .\tag{6}
$$

Last but not least, instead of considering utility, agents (such as [33]) may employ a time-based condition to accept after a certain amount of time $T \in \tau$ has passed:

$$
\mathbf {A C} _ {\text { time }} ^ {\mathcal {I}} (T) \stackrel {{\text { def }}} {{\Longleftrightarrow}} t ^ {\prime} \geq T.\tag{7}
$$

We will omit the superscript in Eqs. (4) to (7) when it is clear from the context. We will use these general acceptance conditions to classify existing acceptance mechanisms in the next section.

## 2.3. Existing acceptance conditions

We give a short overview of decoupled acceptance conditions used in literature and current agent implementations. We are primarily interested in acceptance conditions that are not speci<sup>fi</sup>cally designed for a single agent. We do not claim the list below is complete; however it serves as a good starting point to categorize current decoupled acceptance conditions. We surveyed the entire pool of agents of ANAC 2010, including Agent K, Nozomi [16], Yushu [1], IAM(crazy)Haggler [35], FSEGA [7], and Agent Smith [33]. We also examined well-known agents from literature, such as the Trade-off agent [9], the Bayesian learning agent [12], ABMP [15], equilibrium strategies of [11], and time dependent negotiation strategies as de-<sup>fi</sup>ned in [28], i.e. the Boulware and Conceder tactics.

Listed in Table 2 is a selection of generic acceptance conditions found.

Some agents also use logical combinations of different acceptance conditions at the same time. This explains why some agents are listed multiple times in the table. For example, both IAMHaggler and IAMcrazyHaggler [35] accept precisely when

$$
\mathbf {A C} _ {\text { const }} (0. 8 8) \vee \mathbf {A C} _ {\text { next }} (1. 0 2, 0) \vee \mathbf {A C} _ {\text { prev }} (1. 0 2, 0).
$$

We will not focus on the many possible combinations of all acceptance conditions that may thus be obtained; we will study the basic acceptance conditions in isolation with varying parameters. However in addition to this we study a small selection of combinations in Section 3. We leave further combinations for future research.

A selection of existing decoupled acceptance conditions found in literature and current agent implementations.

<table><tr><td>AC</td><td> $\alpha$ </td><td> $\beta$ </td><td>Agent</td></tr><tr><td rowspan="4"> $\mathbf{AC}_{\text{prev}}(\alpha,\beta)$ </td><td>1.03</td><td>0</td><td>FSEGA, Bayesian Agent</td></tr><tr><td>1</td><td>0</td><td>Agent Smith</td></tr><tr><td>1.02</td><td>0</td><td>IAM(crazy)Haggler</td></tr><tr><td>1</td><td>0.02</td><td>ABMP</td></tr><tr><td rowspan="3"> $\mathbf{AC}_{\text{next}}(\alpha,\beta)$ </td><td>1</td><td>0</td><td>FSEGA, Boulware, Conceder, Trade-off, Equilibrium strategies</td></tr><tr><td>1.02</td><td>0</td><td>IAM(crazy)Haggler</td></tr><tr><td>1.03</td><td>0</td><td>Bayesian Agent</td></tr><tr><td rowspan="4"> $\mathbf{AC}_{\text{const}}(\alpha)$ </td><td>1</td><td>-</td><td>FSEGA</td></tr><tr><td>0.9</td><td>-</td><td>Agent Smith</td></tr><tr><td>0.88</td><td>-</td><td>IAM(crazy)Haggler</td></tr><tr><td>T</td><td></td><td></td></tr><tr><td> $\mathbf{AC}_{\text{time}}(T)$ </td><td>0.92</td><td>-</td><td>Agent Smith</td></tr></table>

As can be seen from Table 2, in our sample the most commonly used acceptance condition is $\mathbf { A C } _ { \mathrm { n e x t } } = \mathbf { A C } _ { \mathrm { n e x t } } ( 1 , 0 )$ , which is the familiar condition of accepting when the opponent's last offer is better than the planned offer of the agent. The function $\beta \mapsto \mathsf { \mathbf { A C } } _ { \mathrm { p r e v } } ( 1 , \beta )$ can be viewed as an acceptance condition that accepts when the utility gap [15] between the parties is smaller than $\beta .$ We denote this condition by ${ \pmb { \mathrm { A C } } } _ { \mathrm { g a p } } ( \beta )$

## 3. Combined acceptance conditions

We de<sup>fi</sup>ne three acceptance conditions that are designed to perform well in conjunction with an arbitrary bidding strategy. This will incorporate all ideas behind the traditional acceptance conditions we have described so far. We will show in Section 4 that they work better than the majority of simple generic conditions listed in Table 2.

From a negotiation point of view, it makes sense to alter the behavior of an acceptance condition when time is running short. For example, many ANAC agents such as Yushu, Nozomi and FSEGA [1,7,16] split the negotiation into different intervals of time and apply different sub-strategies to each interval.

The basic idea behind combined acceptance conditions ${ \pmb { \mathrm { A } } } { \bf { C } } _ { \mathrm { { c o m b i } } }$ is similar. In case the bidding strategy plans to propose a deal that is worse than the opponent's offer, we have reached a consensus with our opponent and we accept the offer. However, if there still exists a gap between our offer and time is short, the acceptance condition should wait for an offer that is not expected to improve in the remaining time. Thus ${ \tt A C } _ { \mathrm { c o m b i } }$ is designed to be a proper extension of $\pmb { { \cal A } } \pmb { \mathbb { C } } _ { \mathrm { n e x t } }$ , with adaptive behavior based on recent bidding behavior near the deadline.

To de<sup>fi</sup>ne $\mathbf { A C } _ { \mathrm { c o m b i } } ,$ suppose an active negotiation thread

$$
H _ {A \leftrightarrow B} ^ {t} = \left(x _ {p _ {1} \rightarrow p _ {2}} ^ {t _ {1}}, x _ {p _ {2} \rightarrow p _ {3}} ^ {t _ {2}}, \dots , x _ {A \rightarrow B} ^ {t _ {n - 1}}, x _ {B \rightarrow A} ^ {t _ {n}}\right),
$$

is given at time $t ^ { \prime } { > } t = t _ { n } { > } \frac { 1 } { 2 }$ near the deadline, when it is agent A's turn. Note that there is $r = 1 - t ^ { \prime }$ time remaining in the negotiation, which we will call the remaining time window. A good sample of what might be expected in the remaining time window consists of the bids that were exchanged during the previous time window $W = [ t ^ { \prime } - r , t ^ { \prime } ] T$ of the same size.

$$
H _ {B \rightarrow A} ^ {W} = \left\{x _ {B \rightarrow A} ^ {s} \in H _ {A \leftrightarrow B} ^ {t} | s \in W \right\}
$$

denote all bids offered by B to A in time window W. We can now formulate the average and maximum utility that was offered during the previous time window in the negotiation thread $H = H _ { B \to A } ^ { W } :$

$$
\operatorname{MAX} ^ {W} = \max _ {x \in H} U _ {A} (x),
$$

and

$$
\mathrm{AVG} ^ {W} = \frac {1}{| H |} \sum_ {x \in H} U _ {A} (x).
$$

We let $\mathbf { A C } _ { \mathrm { c o m b i } } ( T , \alpha )$ accept at time t′ exactly when the following holds: $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { \mathrm { n e x t } }$ indicates that we have to accept, or we have almost reached the deadline $\left( t ^ { \prime } \geq T \right)$ and the current offer suf<sup>fi</sup>ces (i.e. better than α) given the remaining time:

$$
\begin{array}{c} \mathbf {A C} _ {\text { combi }} (T, \alpha) \\ \stackrel {{\text { def }}} {{\Longleftrightarrow}} \\ \mathbf {A C} _ {\text { next }} \vee \mathbf {A C} _ {\text { time }} (T) \wedge \left(U _ {A} \left(x _ {B \to A} ^ {\mathrm{t}}\right) \geq \alpha\right). \end{array}\tag{8}
$$

Note that Eq. (8) de<sup>fi</sup>nes $\mathbf { A C } _ { \mathrm { { c o m b i } } } ( T , \alpha )$ in such a way that it splits the negotiation time into two phases: [0,T) and [T,1], with different behaviors in both cases.

We will consider three different combined acceptance conditions:

1. $\mathbf { A C _ { \mathrm { { c o m b i } } } } ( T , \mathrm { { M A X } } ^ { W } )$ : the current offer is good enough when it is better than all offers seen in the previous time window W,

2. $\mathbf { A C _ { \mathrm { c o m b i } } } ( T , \mathbf { A V G } ^ { W } )$ : the offer is better than the average utility of offers during the previous time window W,

3. $\mathbf { A } \mathbf { C } _ { \mathrm { c o m b i } } \left( T , \mathbf { M A X } ^ { \mathcal { T } } \right)$ : the offer should be better than any bid seen before.

## 4. Experiments

In order to experimentally test the ef<sup>fi</sup>cacy of an acceptance condition, we considered a negotiation setup with the following characteristics. We equipped a set of agents (as de<sup>fi</sup>ned later) with an acceptance condition, and measured the result against other agents in the following way. Suppose agent A is equipped with acceptance condition $\pmb { \mathsf { A } } \pmb { \mathsf { C } } _ { A }$ and negotiates with agent B. The two parties may reach a certain outcome $\omega \in \Omega ,$ , for which A receives the associated utility $U _ { A } ( \omega )$ . The score for A is averaged over all trials on various domains (see Section 4.1.2), alternating between the two preference pro<sup>fi</sup>les de<sup>fi</sup>ned on that domain. E.g., on the negotiation scenario between England and Zimbabwe, A will play both as England and as Zimbabwe against all others. This average utility score is then an indication of the ef<sup>fi</sup>cacy of $\pmb { \Lambda } \pmb { C } _ { A } .$

For our experimental setup we employed GENIUS (General Environment for Negotiation with Intelligent multi-purpose Usage Simulation) [24]. This environment, which is also used in ANAC, helps to facilitate the design and evaluation of automated negotiators' strategies. It can be used to simulate tournaments between negotiating agents in various negotiation scenarios, such as the setup described in this section. It supports the alternating offer protocol with a real-time deadline as outlined in our negotiation model. The default negotiation time in GENIUS and in the setup of ANAC is 3 min per negotiation session; therefore we use the same value in our experiments.

## 4.1. Detailed experimental setup

## 4.1.1. Agents

We use the negotiation tactics that were submitted to the Automated Negotiating Agents Competition (ANAC 2010) [3]. ANAC is a negotiation competition aiming to facilitate and coordinate the research into pro<sup>fi</sup>cient negotiation strategies for bilateral multi-issue negotiation, similar to what the Trading Agent Competition (TAC)

has achieved for the trading agent problem [34]. The seven agents that participated in ANAC 2010 have been implemented by various international research groups of negotiation experts. We used these strategies in our experiments as they are representative of the state-of-the-art in automated negotiation at the time of writing. Firstly, we removed the built-in acceptance mechanism from this representative group of agents; this left us with its pure bidding tactics. As outlined in our negotiation model, this procedure allowed us to test arbitrary acceptance conditions in tandem with any ANAC tactic.

We aimed to tune our acceptance conditions to the top performing ANAC 2010 agents. Therefore we have selected the top 3 of ANAC agents that were submitted by different research groups, namely Agent K, Yushu and IAMHaggler (we omitted Nozomi as the designing group also implemented Agent K, cf. Table 1). For the set of opponents, we selected all agents from ANAC 2010, for the acceptance conditions should be tested against a wide array of strategies. The opponents also had their built-in acceptance conditions removed (and hence were not able to accept), so that differences in results would depend entirely on the acceptance condition under consideration. To test the ef<sup>fi</sup>cacy of an acceptance condition, we equipped the top 3 tactics with this condition and compared the average utility obtained by the three agents when negotiating against their opponents.

## 4.1.2. Domains

The speci<sup>fi</sup>cs of a negotiation domain can be of great in<sup>fl</sup>uence on the negotiation outcome [13]. Acceptance conditions have to be assessed on negotiation domains of different size and complexity. Negotiation results also depend on the opposition of the parties' preferences. The notion of weak and strong opposition can be formally de<sup>fi</sup>ned [17]. Strong opposition is typical of competitive domains, when a gain for one party can be achieved only at a loss for the other party. Conversely, weak opposition means that both parties achieve either losses or gains simultaneously.

With this in mind, we aimed for a good spread of negotiation characteristics by selecting four different negotiation scenarios with two preference pro<sup>fi</sup>les each (see Table 3 and Fig. 1). We picked two domains from the three that were used in ANAC 2010 (cf. [3,5]). We have also taken two negotiation scenarios from the ANAC 2011 competition [4] to include both a smaller and a larger domain to our experimental setup.

Some agents participating in ANAC 2010 did not scale well and could not deal with very large bid spaces; therefore, we omitted the even larger domains that featured in ANAC 2010 and 2011, as the agents had too many dif<sup>fi</sup>culties with them to make them reliable testing domains. Additionally, in contrast to the 2010 competition, ANAC 2011 introduced discount factors for some of the scenarios. We removed these discount factors to ensure compatibility with the ANAC 2010 agents.

Our smallest scenario is called Laptop. In this scenario, a seller and a buyer are negotiating the speci<sup>fi</sup>cations of a laptop. An agreement in the negotiation reconciles their differences and results in a purchase. The scenario has three issues: the laptop brand, the size of the hard disk, and the size of the external monitor. Each issue has only three options, making it a very small scenario with only 27 possible outcomes. Unbeknownst to each other, the buyer and seller actually both prefer to buy (and sell, respectively) a laptop with a small screen. The buyer prefers this because it is cheaper, and the seller prefers to sell laptops with small screens because s/he has more of those in stock. If the two parties are able to <sup>fi</sup>nd the outcomes that are mutually bene<sup>fi</sup>cial to both, then they are happy to do business together with high utility scores on both sides. This can be con<sup>fi</sup>rmed in Table 3: the scenario has the highest arithmetic mean utility, and the most favorable Nash and Kalai-Smorodinsky point.

Our second scenario is taken from [18], which describes a buyer–seller business negotiation. It involves representatives of two companies: Itex Manufacturing, a producer of bicycle components, and Cypress Cycles, a builder of bicycles. There are four issues that both sides have to discuss: the price of the components, delivery times, payment arrangements and terms for the return of possibly defective parts. The opposition between the parties is strong in this domain, as the manufacturer and consumer have naturally opposing requirements. Even the Nash point utilities are quite low for both parties. Altogether, there are 180 potential offers that contain all combinations of values for the four issues.

Table 3  
The eight preference pro<sup>fi</sup>les used in the experiments, as used in ANAC 2010 [3] and ANAC 2011 [4]. The rows indicate respectively: the size of the outcome space, the level of opposition, the arithmetic mean utility that can be obtained in the scenario, and the location of the Nash point and Kalai-Smorodinsky point.

<table><tr><td></td><td>Laptop</td><td>Itex-Cyp</td><td>Zim-Eng</td><td>Grocery</td></tr><tr><td>Size</td><td>27</td><td>180</td><td>576</td><td>1600</td></tr><tr><td>Opposition</td><td>Weak</td><td>Strong</td><td>Medium</td><td>Medium</td></tr><tr><td>Mean utility</td><td>0.67</td><td>0.48</td><td>0.58</td><td>0.44</td></tr><tr><td>Nash point</td><td>(1.00, 0.82)</td><td>(0.72, 0.67)</td><td>(0.91, 0.73)</td><td>(0.84, 0.90)</td></tr><tr><td>K-S point</td><td>(0.87, 0.87)</td><td>(0.72, 0.67)</td><td>(0.82, 0.79)</td><td>(0.84, 0.90)</td></tr></table>

Third, the domain taken from [21,23] involves a case where England and Zimbabwe negotiate an agreement on tobacco control. The leaders of both countries must reach an agreement on <sup>fi</sup>ve issues. England and Zimbabwe have contradictory preferences for the <sup>fi</sup>rst two issues, but the other issues have options that are jointly preferred by both sides. The domain has a total of 576 possible agreements.

Our <sup>fi</sup>nal negotiation case concerns the Grocery scenario, which models a shopping negotiation in a local supermarket. The negotiation is between two persons having different tastes, who wish to buy groceries together. The discussion is about <sup>fi</sup>ve product categories: bread, fruit, snacks, spreads, and vegetables. Each category consists of four to <sup>fi</sup>ve possible options, resulting in a scenario with 1600 possible outcomes. Apart from their differences in taste, the two parties also differ in what category of product they <sup>fi</sup>nd more important. The preferences are modeled in such a way that a good outcome is achievable for both, so the Nash and Kalai-Smorodinsky point utilities are high for both parties; however, the outcome space is scattered (resulting in a relatively low mean utility), so agents must explore it considerably to <sup>fi</sup>nd the jointly pro<sup>fi</sup>table ones.

To compensate for any utility differences in the preference pro-<sup>fi</sup>les, the agents play both sides of every scenario.

## 4.1.3. Acceptance conditions

For each acceptance condition we tested all $3 \times 7 = 2 1$ pairings of agents, playing with each of the 8 different preference pro<sup>fi</sup>les. We ran every experiment a total of N = 15 times, so that altogether each acceptance condition was tested $2 1 \times 8 \times 1 5 = 2 5 2 0$ times in total. This resulted in running as many negotiations, and as every negotiation lasts 3 min, the experiments took 126 h of cpu time. We selected a wide range of 102 acceptance conditions for experimental testing, as shown in Table 4. The different values of parameters will be discussed in the section below.

Additionally, we ran <sup>fi</sup>ve more experiments with agents having their original, built-in acceptance mechanism in place. That is, we also tested the original agents' coupled acceptance mechanism for comparison purposes. As we cannot for example, equip Agent K with the coupled acceptance condition of Yushu, we tested the built-in mechanism by having each agent employ its own mechanism.

![](/api/attachments/KN6KECMC/fulltext/images/f6ad7940b178652ea3d62d6e851801dfa8cc1471e42817643fbe9a0bbd0e88d3.jpg)

![](/api/attachments/KN6KECMC/fulltext/images/55ea5657000d34b01bfe3e37c4b18d0e7c737d5789399332a8c9cc3c9c879e26.jpg)

![](/api/attachments/KN6KECMC/fulltext/images/5d49264aa0a2589bdcf6c66628cc4863af989f2f369b426a0575f76d6eaca5b6.jpg)  
(c) England–Zimbabwe

(b) Itex–Cypress  
![](/api/attachments/KN6KECMC/fulltext/images/707bf272baa8722afb862060ece18a149d45464155918ebb10fbd8cef02f0f59.jpg)  
(d) Grocery  
Fig. 1. The Pareto frontier of the outcome space of the four scenarios used in the experiments.

Table 5  
Table 4  
The selected ranges and increments for the parameters of different acceptance conditions in the experimental setup.

<table><tr><td>AC</td><td>Ranges</td><td>Increments</td></tr><tr><td> $\mathbf{AC}_{\text{prev}}(\alpha,\beta),$ and  $\mathbf{AC}_{\text{next}}(\alpha,\beta)$ </td><td> $\alpha \in [1, 1.05),$ and  $\beta \in [0, 0.1)$ </td><td>For  $\alpha$ : 0.01,and for  $\beta$ : 0.02</td></tr><tr><td> $\mathbf{AC}_{\text{const}}(\alpha)$ </td><td> $\alpha \in [0, 1)$ </td><td>0.05 increments</td></tr><tr><td> $\mathbf{AC}_{\text{time}}(T)$ </td><td> $T \in [0, 1)$ </td><td>0.05 increments</td></tr><tr><td> $\mathbf{AC}_{\text{combi}}(T,\text{MAX}^W),$ and  $\mathbf{AC}_{\text{combi}}(T,\text{AVG}^W)$ </td><td> $T \in [0.95, 1)$ </td><td>0.01 increments</td></tr><tr><td> $\mathbf{AC}_{\text{combi}}(T,\text{MAX}^T)$ </td><td> $T = 0.99$ </td><td>-</td></tr></table>

## 4.2. Hypotheses and experimental results

The experiments considered here are designed to discuss the main properties and drawbacks of the acceptance conditions listed above. We formulate several hypotheses with respect to the acceptance conditions we have discussed.

To evaluate the hypotheses below, we have carried out a large number of experiments. A small selection of the results is summarized in Table 5. The table shows the average utility obtained by the agents, and the standard deviation (of the $N = 1 5$ experiments), when equipped with several acceptance conditions. The “average utility of agreements” column represents the average utility obtained by the agent given the fact that they have reached an agreement. When they do not reach an agreement (due to reaching the deadline), they get zero utility. Thus, as a general observation, the following holds:

## The acceptance dilemma Total average utility Agreement percentage × Average utility of agreements:

This formula captures the essence of the acceptance dilemma: accepting bad to mediocre offers yields more agreements of relatively low utility; while accepting only the best offers produces less agreements, but of higher utility.

A small selection of the various acceptance conditions that were tested, together with average utility obtained and standard deviation, The utility of the best scoring AC of each category is in bold. The two right-hand side columns show agreement percentages and the utility obtained when an agreement is reached.

<table><tr><td>AC</td><td> $\alpha$ </td><td> $\beta$ </td><td>Util</td><td>SD</td><td>Agt %</td><td>Agt util</td></tr><tr><td rowspan="4"> $\mathbf{AC}_{\text{prev}}(\alpha,\beta)$ </td><td>1</td><td>0</td><td>0.680</td><td>0.0084</td><td>80%</td><td>0.851</td></tr><tr><td>1</td><td>0.04</td><td>0.711</td><td>0.0094</td><td>84%</td><td>0.842</td></tr><tr><td>1</td><td>0.08</td><td>0.722</td><td>0.0076</td><td>87%</td><td>0.827</td></tr><tr><td>1.02</td><td>0.04</td><td>0.723</td><td>0.0085</td><td>86%</td><td>0.837</td></tr><tr><td rowspan="4"> $\mathbf{AC}_{\text{next}}(\alpha,\beta)$ </td><td>1</td><td>0</td><td>0.683</td><td>0.0112</td><td>81%</td><td>0.843</td></tr><tr><td>1</td><td>0.04</td><td>0.727</td><td>0.0067</td><td>87%</td><td>0.833</td></tr><tr><td>1</td><td>0.08</td><td>0.731</td><td>0.0057</td><td>89%</td><td>0.819</td></tr><tr><td>1.02</td><td>0.04</td><td>0.737</td><td>0.0060</td><td>89%</td><td>0.830</td></tr><tr><td rowspan="4"> $\mathbf{AC}_{\text{const}}(\alpha)$ </td><td>0.20</td><td>-</td><td>0.492</td><td>0.0025</td><td>100%</td><td>0.492</td></tr><tr><td>0.55</td><td>-</td><td>0.619</td><td>0.0027</td><td>92%</td><td>0.671</td></tr><tr><td>0.80</td><td>-</td><td>0.501</td><td>0.0078</td><td>60%</td><td>0.842</td></tr><tr><td>0.90</td><td>-</td><td>0.343</td><td>0.0080</td><td>36%</td><td>0.952</td></tr><tr><td>Built-in mechanism</td><td>-</td><td>-</td><td>0.737</td><td>0.0057</td><td>89%</td><td>0.774</td></tr><tr><td></td><td colspan="6">T</td></tr><tr><td rowspan="4"> $\mathbf{AC}_{\text{time}}(T)$ </td><td>0.10</td><td>-</td><td>0.533</td><td>0.0035</td><td>100%</td><td>0.533</td></tr><tr><td>0.40</td><td>-</td><td>0.548</td><td>0.0064</td><td>100%</td><td>0.548</td></tr><tr><td>0.70</td><td>-</td><td>0.602</td><td>0.0062</td><td>100%</td><td>0.602</td></tr><tr><td>0.95</td><td>-</td><td>0.648</td><td>0.0063</td><td>100%</td><td>0.648</td></tr><tr><td rowspan="3"> $\mathbf{AC}_{\text{combi}}(T,\text{MAX}^W)$ </td><td>0.97</td><td>-</td><td>0.756</td><td>0.0019</td><td>100%</td><td>0.756</td></tr><tr><td>0.98</td><td>-</td><td>0.762</td><td>0.0031</td><td>100%</td><td>0.764</td></tr><tr><td>0.99</td><td>-</td><td>0.761</td><td>0.0046</td><td>98%</td><td>0.776</td></tr><tr><td rowspan="3"> $\mathbf{AC}_{\text{combi}}(T,\text{AVG}^W)$ </td><td>0.97</td><td>-</td><td>0.739</td><td>0.0050</td><td>100%</td><td>0.739</td></tr><tr><td>0.98</td><td>-</td><td>0.754</td><td>0.0037</td><td>100%</td><td>0.757</td></tr><tr><td>0.99</td><td>-</td><td>0.759</td><td>0.0056</td><td>98%</td><td>0.774</td></tr><tr><td> $\mathbf{AC}_{\text{combi}}(T,\text{MAX}^T)$ </td><td>0.99</td><td>-</td><td>0.737</td><td>0.0083</td><td>93%</td><td>0.796</td></tr></table>

Our <sup>fi</sup>rst hypothesis is about the simplest condition, ${ \pmb { \mathrm { A } } } { \pmb { \mathrm { C } } } _ { \mathrm { c o n s t } } ( \alpha )$ and reads as follows:

Hypothesis 1. There is no single choice for α that makes ${ \pmb { \mathrm { A } } } { \pmb { \mathrm { C } } } _ { \mathrm { c o n s t } } ( \alpha )$ an effective acceptance condition; this is mainly because the optimal choice of α is very domain-dependent.

First, consider ${ \bf A C } _ { \mathrm { c o n s t } } ( 0 . 9 )$ and ${ \bf A C } _ { \mathrm { c o n s t } } ( 0 . 8 )$ by consulting Table 5. When they reach an agreement, they receive a very high utility (at least 0.9 or 0.8 respectively), but this happens so infrequently (resp. 60% and 36% of all negotiations), that they are ranked at the bottom when we consider total average utility. On the other hand, choosing a low value for α, such as using $\mathbf { A C } _ { \mathrm { c o n s t } } ( 0 . 2 )$ , will always result in an immediate agreement, but with one of the lowest possible scores of 0.492.

The best possible choice for α should therefore be somewhere in the middle between zero and one, and is found to be 0.55 (see Fig. 2), yielding a payoff of 0.619. Firstly, this is still a suboptimal outcome compared to other $\mathsf { A C } \mathsf { s } ,$ such as the $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { \mathrm { n e x t } }$ and ${ \tt A C } _ { \mathrm { c o m b i } }$ variants.

Moreover, it is worth noting that this optimal value may be best on average, but in this case, averaging over all scenarios also hides a lot of information. When we break down our analysis and look at the four domains separately (see the four <sup>fi</sup>gures of Fig. 3), we see that the optimal range of α differs greatly per domain. For example, on Itex vs. Cypress, the optimal choice for α is around 0.6, while on Grocery, the best performing value is in the range of [0.7,0.8]. On the Laptop domain, any choice for $\alpha \in [ 0 , 0 . 8 ]$ is the best ${ \pmb { \mathrm { A } } } { \pmb { \mathrm { C } } } _ { \mathrm { c o n s t } } ( \alpha )$ can do in this scenario, and will cause the agent to instantly accept most offers.

We conclude that our hypothesis is con<sup>fi</sup>rmed: in isolation, ${ \pmb { \mathrm { A } } } { \pmb { \mathrm { C } } } _ { \mathrm { c o n s t } } ( \alpha )$ is not very advantageous to use. The main reason is that the choice of the constant α is highly domain-dependent. A very cooperative scenario may have multiple win–win outcomes with utilities above α. ${ \pmb { \mathrm { A } } } { \bf C } _ { \mathrm { c o n s t } } ( \alpha )$ would then accept an offer which is relatively bad, i.e. it could have done much better. On the other hand, in highly competitive domains, it may simply ‘ask for too much’ and may rarely obtain an agreement. Its value lies mostly in using it in combination with other acceptance conditions such as $\pmb { \mathrm { A C } } _ { \mathrm { n e x t } } .$ It can then bene<sup>fi</sup>t the agent by accepting an unexpectedly good offer or a mistake by the opponent.

As we discussed earlier in Section 2.3, the acceptance conditions $\mathbf { A C } _ { \mathrm { p r e v } } ( \alpha , \beta )$ and $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( \alpha , \beta )$ are standard in literature for $\alpha \in [ 1 , 1 . 0 3 ]$ and $\beta \in [ 0 , 0 . 2 ]$ . Many agents tend to use these acceptance conditions, as they are well-known and easy to implement. We have formed the following hypothesis about them:

![](/api/attachments/KN6KECMC/fulltext/images/7593ffd47c73dcb142fc04a17dcdf0821075508402cb7d7941cb9c83cbf9dd09.jpg)  
Fig. 2. The average utility obtained by agents using ${ \pmb { \mathrm { A c } } } _ { \mathrm { c o n s t } } ( { \alpha } ) .$ . The vertical errors bars indicate one standard deviation to the mean.

![](/api/attachments/KN6KECMC/fulltext/images/a0877883c388e1677946d3b0136eb958f3e7f1a5575f04afc7bd9b2891cf65d2.jpg)  
(a) Laptop

![](/api/attachments/KN6KECMC/fulltext/images/5b97605146dd7fe3a02e5dda6cee9f297b8b2e9e18786ccfe57d101dcad19ccd.jpg)

![](/api/attachments/KN6KECMC/fulltext/images/1f307ac1b44e505a1cfbadc1c322a770707266722c3c2142cb37f4f1848ae987.jpg)  
(c) England-Zimbabwe

(b) Itex-Cypress  
![](/api/attachments/KN6KECMC/fulltext/images/edcd4d4c0e780e324fbdf4e6cc9a86f5f8117d90262af0c3394c1596fa896bef.jpg)  
(d) Grocery  
Fig. 3. The average utility of ${ \pmb { \mathrm { A c } } } _ { \mathrm { c o n s t } } ( \alpha )$ per negotiation scenario, for $\alpha \in [ 0 , 1 )$

Hypothesis 2. $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( \alpha , \beta )$ will outperform $\mathbf { A C } _ { \mathrm { p r e v } } ( \alpha , \beta )$ for all and $\beta .$ However, both conditions will perform worse than combined acceptance conditions, which also take the remaining time into account.

To test this hypothesis, we considered many different values for α and $\beta$ in our experiments, with ranges chosen around the values we had found in existing agents (cf. Table 2).

Consulting Table 5, the <sup>fi</sup>rst observation is that $\mathbf { A C } _ { \mathrm { p r e v } } ( \alpha , \beta )$ as well as $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( \alpha , \beta )$ already perform much better than ${ \bf A } { \bf C } _ { \mathrm { c o n s t } }$ for all tested values of α and $\beta .$ Higher values for α and $\beta$ generally yield a better result, although the differences are quite small. However, given that we average the utility over 15 runs, we are able to statistically distinguish the performance for different values of α and $\beta .$ We have found $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( \alpha , \beta )$ does indeed outperform $\pmb { \mathrm { A C } } _ { \mathrm { p r e v } } ( \alpha , \beta )$ for all tested values of α and β, except for $\beta = 0$ (two-tailed t-test, $p < 0 . 0 1 $ , thereby partially con<sup>fi</sup>rming the hypothesis.

As an example, we have plotted $\begin{array} { r } { \pmb { A } \pmb { C } _ { \mathrm { n e x t } } ( 1 , \beta ) = \pmb { A } \pmb { C } _ { \mathrm { g a p } } ( \beta ) } \end{array}$ and $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( 1 , \beta )$ for $\beta \in [ 0 , 1 )$ in Fig. 4. We can con<sup>fi</sup>rm that $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( 1 , \beta )$ obtains scores that are signi<sup>fi</sup>cantly higher (using $p < 0 . 0 1 )$ scores than $\mathbf { A C } _ { \mathrm { p r e v } } ( 1 , \beta )$ , for $\beta \neq 0 .$

It makes sense that comparing the opponent's offer to our upcoming offer is more bene<sup>fi</sup>cial than comparing it to our previous offer, as $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { \mathrm { n e x t } }$ is always ‘one step ahead’ of $\mathbf { A C } _ { \mathrm { p r e v } } .$ In general, $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { \mathrm { n e x t } }$ is never worse than $\mathbf { A } \mathbf { C } _ { \mathrm { p r e v } }$ , and therefore there seems no reason to use the latter.

One of the top choices for both $\pmb { \mathrm { \pmb { A } } } \pmb { \mathrm { C } } _ { \mathrm { n e x t } }$ and $\mathbf { A C } _ { \mathrm { p r e v } } ,$ is setting $\alpha = 1 . 0 2$ and $\beta = 0 . 0 4$ (interestingly, IAM(crazy)Haggler makes the same choice for α, cf. Table 2). However, even for this choice, the combined acceptance conditions $\mathbf { A C } _ { \mathrm { c o m b i } } ( T , \mathbf { M A X } ^ { W } )$ outperform both of them for all tested values of T (two-tailed t-test, $p < 0 . 0 1 $ . This also settles the second part of the hypothesis.

The reason for the relatively bad performance of $\pmb { \mathrm { A C } } _ { \mathrm { n e x t } }$ and $\pmb { \mathrm { A C } } _ { \mathrm { p r e v } }$ is that many bidding strategies focus on the ‘negotiation dance’ [27].

![](/api/attachments/KN6KECMC/fulltext/images/8a010a1b1675ea9aa7509b716a4de92f9dfc7a358818d140fab006e4aa94c941.jpg)  
Fig. 4. The average utility obtained by agents using $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( 1 , \beta )$ (in black), and $\mathbf { A C } _ { \mathrm { p r e v } } ( 1 , \beta )$ (in white). The vertical error bars indicate one standard deviation to the average utility of $N = 1 5$ different runs.

That is, modeling the opponent, trying to make equal concessions and so on. When a strategy does not explicitly take time considerations into account when making an offer, this poses a problem for these two standard acceptance conditions: they rely completely on the bidding strategy to concede to the opponent before the deadline occurs. When the agent or the opponent does not concede enough near the deadline, the standard conditions lead to poor performance.

Our third hypothesis with respect to the time-dependent condition is as follows:

Hypothesis 3. ${ \pmb { \mathrm { A } } } { \pmb { \mathrm { C } } } _ { \mathrm { t i m e } } ( T )$ always reaches an agreement, but of relatively low utility. This utility improves when T gets closer to the deadline.

To evaluate this hypothesis we tested ${ \mathbf { A C } } _ { \mathrm { t i m e } } ( T )$ for many possible values of $T \in [ 0 , 1 )$ , a selection of which can be examined in Table 5. We have found that the obtained utility increases monotonously with larger T, i.e.: it is optimal to choose the value of T suf<sup>fi</sup>ciently close to the deadline, while still allowing enough time to reach a win–win agreement. The fact that one has to accept as late as possible when using $\mathbf { A C } _ { \mathrm { t i m e } } ( T )$ clearly stems from the fact that we are dealing with undiscounted domains only; see Section 7 for a discussion on possible extensions in this regard.

From observing the acceptance probability of $\mathbf { A C } _ { \mathrm { t i m e } } ( T )$ in the experimental results, we see that the agent will always reach an agreement, therefore we consider this part of the hypothesis con<sup>fi</sup>rmed.

Regarding the utility of the agreement, ${ \pmb { \mathrm { A } } } { \pmb { \mathrm { C } } } _ { \mathrm { t i m e } } ( T )$ with T b 1 is a sensible criterion to avoid a break off at all costs. It is rational to prefer any outcome over a break off of zero utility. However, the resulting deal can be anything. As we can see from the table, this is the reverse situation of $\mathbf { A C } _ { \mathrm { c o n s t } } ( 0 . 9 ) \colon \mathbf { A C } _ { \mathrm { c o n s t } } ( 0 . 9 )$ rarely gets a deal, but when it does, it is of high utility. Conversely, ${ \pmb { \mathrm { A } } } { \pmb { \mathrm { C } } } _ { \mathrm { t i m e } } ( T )$ yields a low agreement score (0.648 for $T = 0 . 9 5 )$ , but with certainty of agreement. The overall score is the same (0.648), but it is interesting to note that this score is worse than all scores by either $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { \mathrm { n e x t } }$ or $\pmb { \mathrm { A C } } _ { \mathrm { p r e v } }$ (two-tailed t-test, $p < 0 . 0 1 )$ . This phenomenon can again be explained by the acceptance dilemma: by accepting any offer near the deadline, it reaches more agreements, but of relatively low utility.

This insight led us to believe that more consideration has to be given to the remaining time when deciding to accept an offer. The combined acceptance conditions evaluated in the next chapter expand upon this idea to get better deals near the deadline.

## 4.2.1. Evaluating $\mathbf { A C } _ { c o m b i } ( T , \alpha )$

When evaluating $\mathbf { A C } _ { \mathrm { c o m b i } } ( T , \alpha )$ , we expected the following characteristics. First, $\mathbf { A C } _ { \mathrm { c o m b i } } ( T , \alpha )$ is an extension of $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { \mathrm { n e x t } }$ in the sense that it will accept under broader circumstances. It alleviates some of the mentioned drawbacks of $\pmb { \mathrm { A } } \pmb { \mathrm { C } } _ { \mathrm { n e x t } }$ by also accepting when the utility gap between the parties is positive. Also note that in addition to the parameters that current acceptance conditions use, such as my previous bid $x _ { A  B } ^ { t _ { n - 1 } } ,$ my next bid $x _ { A  B } ^ { t ^ { \prime } } ,$ the remaining time, and the opponent's bid $x _ { B  A } ^ { t } ,$ this condition employs the entire bidding history $H _ { A } ^ { t } \gets B$ to compute the acceptability of an offer. Therefore we expect better results than with t, with more agreements, and when it agrees, we expect a better deal than by using $\mathbf { A C _ { \mathrm { t i m e } } } ( T )$

We capture this last statement in our <sup>fi</sup>nal hypothesis:

Hypothesis 4. The combination $\mathbf { A C } _ { \mathrm { c o m b i } } ( T , \alpha )$ outperform other acceptance conditions, such as ${ \pmb { \mathrm { A } } } { \pmb { \mathrm { C } } } _ { \mathrm { t i m e } } ( T )$ and $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( \alpha , \beta )$ , primarily by getting deals of higher utility.

As is evident from the experimental results, there are two acceptance conditions that dominate the others, namely $\mathbf { A C } _ { \mathrm { c o m b i } } ( T , \mathrm { M A X } ^ { W } )$ as well as $\mathbf { A C _ { \mathrm { c o m b i } } } ( T , \mathbf { A V G } ^ { W } )$ with T close to the deadline. The results are not statistically different for the different values of T, but any of the tested values performs quite well. One of the best AC's of the test is $\mathbf { A C _ { \mathrm { c o m b i } } } ( 0 . 9 8 , \mathrm { M A X } ^ { W } )$ with a score of 0.762, which is even better than the built-in mechanisms of the agents, and also surpasses the performance of $\pmb { \mathrm { A c } } _ { \mathrm { n e x t } } ( \alpha , \beta )$ for any α and $\beta$ (signi<sup>fi</sup>cantly so, using a two-tailed t-test, p b 0.01). In particular, it is at least 12% better than $\pmb { \mathrm { A C } } _ { \mathrm { n e x t } }$ (two-tailed t-test, $p < 0 . 0 1 )$ .

Similar to $\mathbf { A C } _ { \mathrm { t i m e } } ,$ the combined conditions still get a deal almost every time, but with a higher payoff. However, the average utility of an agreement is not the highest: the built-in mechanisms and several ${ \pmb { \mathrm { A } } } { \bf C } _ { \mathrm { c o n s t } } ( \alpha )$ conditions get better agreements. But again, we can observe that their agreement rate is also lower, resulting in a higher overall score for the combined criteria. This settles our last hypothesis.

Finally, aiming for the highest utility that has been offered so far (i.e., using $\mathbf { A d } _ { \mathrm { c o m b i } } \left( T , \mathbf { M A X } ^ { T } \right) )$ is not as successful, mostly due to a big decrease in agreements. The higher utility that is obtained with this condition does not compensate for the loss of utility that is caused by a break off.

## 5. Related work

All existing negotiation agent implementations deal with the problem of when to accept. In many cases, the agent accepts a proposal when the value of the offered contract is higher than the offer it is ready to send out at that moment in time. Examples include the time dependent negotiation strategies de<sup>fi</sup>ned in [28] (e.g. the Boulware and Conceder tactics). The same principle is used in the equilibrium strategies of [11] and for the Trade-off agent [9], although this concerns a setting where the deadline can be different for both agents. In our work, we consider strategies that do not always reach an agreement, and we have concentrated on acceptance conditions that yield better results in such cases.

Of all ANAC 2010 participants, we shortly discuss Agent $K \left[ 1 6 \right]$ as it employs the most sophisticated method to decide when to accept. Its acceptance mechanism is based on the mean and variance of all received offers. It then tries to determine the best offer it might receive in the future and sets its proposal target accordingly. In contrast to our approach, this mechanism is not fully decoupled from the bidding strategy as it directly in<sup>fl</sup>uences its bid target. Furthermore, it does not restrict its scope to the remaining or previous time window. Finally, we note that Agent K performs better in our experimental setup (cf. Table 5) when equipped with our combined acceptance conditions than with its built-in mechanism.

This work builds upon earlier research [5], which also experimentally tested various acceptance conditions, albeit in a more limited setting. In this paper, we extend results in [5] and gain additional insights by exploring a larger class of acceptance conditions in a wider range of negotiation scenarios. Although we do not focus on negotiation tactics and convergence results, our negotiation model also builds upon the model of [31]. However, in this model, the action function of an agent only takes into account the offer it is ready to send out at that moment in time. Moreover, the focus of the paper is not on comparing acceptance conditions as only one speci<sup>fi</sup>c instance is studied. We take a more general approach in which the agent utilizes a generic acceptance mechanism, in which the current time and the entire bidding history is considered.

## 6. Conclusion

In this paper, we aimed to classify current approaches to generic acceptance conditions and to compare a selection of acceptance conditions in a real-time setting. We presented the challenges and proposed new solutions for accepting offers in current state-of-the-art automated negotiations. The focus of this paper is on decoupled acceptance conditions (i.e.: general conditions that do not depend on a particular bidding strategy), for which we have de<sup>fi</sup>ned a formal negotiation model.

Designing an effective acceptance condition is challenging because of the acceptance dilemma: better offers may arrive in the future, but waiting for too long can result in a break off of the negotiation, which is undesirable for both parties.

We have presented and classi<sup>fi</sup>ed many of the standard acceptance criteria that are currently used by negotiating agents, including $\mathbf { A C } _ { \mathrm { n e x t } } , \mathbf { A C } _ { \mathrm { p r e v } } ,$ and ${ \pmb { \cal A } } { \bf C } _ { \mathrm { c o n s t } } .$ . From our results, it is apparent that they do not always yield optimal agreements, and we established that they perform worse than more sophisticated acceptance conditions.

In addition to classifying and comparing existing acceptance conditions, we have devised three new acceptance conditions by combining existing ones. This included two acceptance conditions that estimate whether a better offer might occur in the future based on recent bidding behavior. These conditions obtained the highest utility in our experiments and hence performed better than the other conditions we have investigated. In particular, they outperform the acceptance mechanisms that are used by the top ANAC 2010 agents.

## 7. Discussion and future work

We have examined the effectivity of acceptance conditions in a setting with two key elements: a bilateral alternating offers protocol, and a real-time deadline. We brie<sup>fl</sup>y discuss our results and possible lines of future work in light of different negotiation contexts.

The adoption of the alternating offers protocol imposes an important restriction on the negotiation process, because the agents only exchange information in one of three possible forms: an offer, an accept, or a withdrawal. Normally it is irrational to withdraw from a negotiation (i.e., by sending a message ending the negotiation) without any outside options, as it leaves the agent with nothing. However, recently there has been interest [4] in real-time settings with reservation values and discount factors. When both contract utility and outside options devaluate with the passing of time, novel acceptance conditions are required that give more consideration to the negotiation timeline. For example, it can be advantageous for an agent to end the negotiation prematurely and receive its reservation value, rather than continuing an exchange of offers while the contract diminishes in value. This adds an additional dimension to the acceptance dilemma, as prolonging the negotiation does not necessarily increase the agent's chances of a good outcome.

In a multi-party setting, the problem of when to accept is even more complex, as the outside options become dynamic; however, the presence of a mediator can reduce some of the complexity by taking over the role of <sup>fi</sup>nding acceptable agreements, for example through letting the agents vote on whether a proposed contract is acceptable [19]. It may then be suf<sup>fi</sup>cient for an agent to simply accept anything above its reservation value. In the same way, when richer protocols are employed (e.g., when communication is possible, for instance in persuasive, or argumentation-based negotiation [26,32]), the acceptance dilemma may be easier to resolve, as agents have more knowledge about the acceptability of offers. Lastly, in traditional negotiation protocols such as ours, once a contract is settled upon, it is binding. However, a more general approach is to allow decommitment, i.e. backing out of the negotiation after <sup>fi</sup>nding a superior option elsewhere, usually at the cost of a penalty [30]. This requires complex acceptance strategies for committing and decommitting to agreements in a concurrent way; there has been recent work in the same negotiation setting that we employ, which opens up possible research in this area [36].

Finally, the real-time setting presents an additional challenge to <sup>fi</sup>nding effective acceptance mechanisms. For example, in a roundbased setting, results are usually less ambiguous, as this usually concerns bargaining games with perfect information where a unique subgame-perfect equilibrium exists. An optimal acceptance strategy can then be adopted through backward inductive reasoning; the most well-known solution being that agreement is reached immediately in the <sup>fi</sup>rst round [29]. In a real-time setting, it is generally unknown when the last offer has been made, and this makes it dif<sup>fi</sup>cult to <sup>fi</sup>nd optimal acceptance conditions for this setting; this is why our approach is heuristic in essence.

For future work, we plan to test acceptance conditions in more dy namic settings with more agents and on more complex scenarios, using the resources of ANAC 2011 and 2012.

Secondly, a suggestion for future research would be to explore the many possible combinations of acceptance conditions that may be obtained using conjunction and disjunction (and possibly negation). Some agents already use a logical combination of different acceptance conditions at the same time. For example, the IAM(crazy)Haggler agents accept when

$$
\mathbf {A C} _ {\text { const }} (0. 8 8) \vee \mathbf {A C} _ {\text { next }} (1. 0 2, 0) \vee \mathbf {A C} _ {\text { prev }} (1. 0 2, 0).
$$

A suitable combination of acceptance conditions could provide a considerable improvement over current acceptance conditions. We plan to examine such extensions in future work.

## Acknowledgments

This research is supported by the Dutch Technology Foundation STW, Applied Science Division of NWO and the Technology Program of the Ministry of Economic Affairs. It is part of the Pocket Negotiator project with grant number VICI-project 08075.

## References

[1] Bo An, Victor Lesser, Yushu: a heuristic-based agent for automated negotiating competition, in: Takayuki Ito, Minjie Zhang, Valentin Robu, Shaheen Fatima, Tokuro Matsuo (Eds.), New Trends in Agent-based Complex Automated Negotiations, Series of Studies in Computational Intelligence, Springer-Verlag, Berlin, Heidelberg.2012 pp. 145-149

[2] In: R.J. Aumann, S. Hart (Eds.), Handbook of Game Theory with Economic Applications vol., 1 Elsevier March 1992

[3] Tim Baarslag, Koen Hindriks, Catholijn M. Jonker, Sarit Kraus, Raz Lin, The <sup>fi</sup>rst automated negotiating agents competition (ANAC 2010), in: Takayuki Ito, Minjie Zhang, Valentin Robu, Shaheen Fatima, Tokuro Matsuo (Eds.), New Trends in Agent-based Complex Automated Negotiations, Series of Studies in Computation al IntelligenceSpringer-Verlag, Berlin, Heidelberg, 2012, pp. 113–135.

[4] Tim Baarslag, Katsuhide Fujita, Enrico H. Gerding, Koen Hindriks, Takayuki Ito, Nicholas R. Jennings, Catholijn Jonker, Sarit Kraus, Raz Lin, Valentin Robu, Colin R. Williams, Evaluating practical negotiating agents: results and analysis of the 2011 international competition. Artificial Intelligence 198 (2013) 73–103.

[5] Tim Baarslag, Koen Hindriks, Catholijn Jonker, Acceptance conditions in automated negotiation, in: Takayuki Ito, Minjie Zhang, Valentin Robu, Tokuro Matsuo (Eds.), Complex Automated Negotiations: Theories, Models, and Software Competitions, Studies in Computational Intelligence, volume 435, Springer, Berlin/Heidelberg 2013. pp. 95–111.

[6] Chi-Bin Cheng, Chu-Chai Henry Chan, Kun-Cheng Lin, Intelligent agents for e-marketplace: negotiation with issue trade-offs by fuzzy inference systems, Decision Support Systems 42 (2) (2006) 626–638.

[7] Liviu Dan Serban, Gheorghe Cosmin Silaghi, Cristian Marius Litan, Agent FSEGA — time constrained reasoning model for bilateral multi-issue negotiations, in: Takayuki Ito, Minjie Zhang, Valentin Robu, Shaheen Fatima, Tokuro Matsuo (Eds.), New Trends in Agent-based Complex Automated Negotiations, Series of Studies in Computational IntelligenceSpringer-Verlag, Berlin, Heidelberg, 2012, pp. 159–165.

[8] P. Faratin, C. Sierra, N.R. Jennings, Negotiation decision functions for autonomous agents, Robotics and Autonomous Systems 24 (3–4) (1998) 159–182.

[9] P. Faratin, C. Sierra, N.R. Jennings, Using similarity criteria to make negotiation trade-offs, Journal of Arti<sup>fi</sup>cial Intelligence 142 (2) (2003) 205–237.

[10] S. Shaheen Fatima, Michael Wooldridge, Nicholas R. Jennings, Optimal negotiation strategies for agents with incomplete information, Revised Papers from the 8th International Workshop on Intelligent Agents VIII, ATAL '01, Springer-Verlag, London, UK, UK, 2002, pp. 377–392

[11] Shaheen S. Fatima, Michael Wooldridge, Nicholas R. Jennings, Multi-issue negotiation under time constraints, AAMAS '02: Proceedings of the First International Joint Conference on Autonomous Agents and Multiagent SystemsACM, New York NY USA 2002 pp. 143-150

[12] Koen V. Hindriks, Dmytro Tykhonov, Opponent modelling in automated multi-issue negotiation using Bayesian learning, Proceedings of the 7th International Joint Conference on Autonomous Agents and Multiagent Systems — Volume 1, AAMAS '08. International Foundation for Autonomous Agents and Multiagent Systems, Richland SC 2008 pp. 331–338

[13] KoenV. Hindriks, Dmytro Tykhonov, Towards a quality assessment method for learning preference pro<sup>fi</sup>les in negotiation, in: Wolfgang Ketter, Han Poutré, Norman Sadeh, Onn Shehory, William Walsh (Eds.), Agent-mediated Electronic Commerce and Trading Agent Design and Analysis, Lecture Notes in Business In: formation Processing, volume 44, Springer, Berlin Heidelberg, 2010, pp. 46–59.

[14] Takavuki Ito Hiromitsu Hattori, Mark Klein, Multi-issue negotiation protocol for agents: exploring nonlinear utility spaces, Proceedings of the 20th International

Joint Conference on Arti<sup>fi</sup>cial Intelligence, IJCAI'07Morgan Kaufmann Publisher Inc., San Francisco, CA, USA, 2007, pp. 1347–1352.

[15] Catholijn Jonker, Valentin Robu, Jan Treur, An agent architecture for multiattribute negotiation using incomplete preference information, Autonomous Agents and Multi-Agent Systems 15 (2007) 221–252.

[16] Shogo Kawaguchi, Katsuhide Fujita, Takayuki Ito, Compromising strategy based on estimated maximum utility for automated negotiating agents, in: Takayuki Ito, Minjie Zhang, Valentin Robu, Shaheen Fatima, Tokuro Matsuo (Eds.), New Trends in Agent-based Complex Automated Negotiations, Series of Studies in Computational IntelligenceSpringer-Verlag, Berlin, Heidelberg, 2012, pp. 137–144.

[17] G.E. Kersten, S.J. Noronha, Rational agents, contract curves, and inef<sup>fi</sup>cient compromises, Trans. Sys. Man Cyber. Part A 28 (3) (May 1998) 326–338.

[18] Gregory E. Kersten, Grant Zhang, Mining inspire data for the determinants of successful internet negotiations. InterNeg Research Papers INR 04/01 Central European, Journal of Operational Research 11 (3) (2003) 297–316.

[19] Mark Klein, Peyman Faratin, Hiroki Sayama, Yaneer Bar-Yam, Negotiating complex contracts, Group Decision and Negotiation 12 (2003) 111–125, http://dx.doi.org/ 10.1023/A:1023068821218.

[20] Sarit Kraus, Strategic Negotiation in Multiagent Environments, MIT Press, October 2001.

[21] Raz Lin, Sarit Kraus, Jonathan Wilkenfeld, James Barry, Negotiating with bounded rational agents in environments with incomplete information using an automated agent, Arti<sup>fi</sup>cial Intelligence 172 (6–7) (2008) 823–851.

[22] Raz Lin, Yinon Oshrat, Sarit Kraus, Investigating the bene<sup>fi</sup>ts of automated negotiations in enhancing people's negotiation skills, AAMAS '09: Proceedings of the 8th International Conference on Autonomous Agents and Multiagent Systems, 2009, pp. 345–352.

[23] R. Lin, S. Kraus, D. Tykhonov, K. Hindriks, C.M. Jonker, Supporting the design of general automated negotiators, Proceedings of the Second International Workshop on Agent-based Complex Automated Negotiations (ACAN'09), vol. 319, Springer, Springer, 2011, pp. 69–87.

[24] Raz Lin, Sarit Kraus, Tim Baarslag, Dmytro Tykhonov, Koen Hindriks, Catholijn M. Jonker, Genius: an integrated environment for supporting the design of generic automated negotiators, Computational Intelligence (2012).

[25] Martin J. Osborne, Ariel Rubinstein, Bargaining and Markets (Economic Theory, Econometrics, and Mathematical Economics), Academic Press, April 1990.

[26] Iyad Rahwan, Sarvapalic Ramchurn, Nicholas R. Jennings, Peter McBurney, Simon Parsons, Liz Sonenberg, Argumentation-based negotiation, The Knowledge Engineering Review 18 (04) (2003) 343-375

[27] H. Raiffa, The Art and Science of Negotiation, Harvard University Press, 1982.

[28] Raquel Ros, Carles Sierra, A negotiation meta strategy combining trade-off and concession moves, Autonomous Agents and Multi-Agent Systems 12 (2006) 163–181.

[29] Ariel Rubinstein, Perfect equilibrium in a bargaining model, Econometrica 50 (1) (1982) 97–109.

[30] Tuomas Sandholm, Victor R. Lesser, Advantages of a leveled commitment contracting protocol, in: William J. Clancey, Daniel S. Weld (Eds.), Proceedings of the Thirteenth National Conference on Arti<sup>fi</sup>cial Intelligence and Eighth Innovative Applications of Arti<sup>fi</sup>cial Intelligence Conference, AAAI 96, IAAI 96, Portland, Oregon, August 4–8, 1996, vol. 1, AAAI Press/The MIT Press, 1996, pp. 126-133.

[311 C. Sierra. P. Faratin. N.R. Jennings. A service-oriented negotiation model between autonomous agents, in: M. Boman, W. van de Velde (Eds.). Proceedings of the 8th European Workshop on Modelling Autonomous Agents in Multi-Agent World. MAAMAW'97, Lecture Notes in Artificial Intelligence, volume 1237, Springer-Verlag, 1997, pp. 17–35.

[32] Katia P. Sycara, Machine learning for intelligent support of con<sup>fl</sup>ict resolution, Decision Support Systems 10 (2) (1993) 121–136.

[33] Niels van Galen Last, Agent Smith: opponent model estimation in bilateral multi-issue negotiation, in: Takayuki Ito, Minjie Zhang, Valentin Robu, Shaheen Fatima, Tokuro Matsuo (Eds.), New Trends in Agent-based Complex Automated Negotiations, Series of Studies in Computational IntelligenceSpringer-Verlag, Berlin, Heidelberg, 2012, pp. 167–174.

[34] Michael P. Wellman, Peter R. Wurman, Kevin O'Malley, Roshan Bangera, Shou de Lin, Daniel Reeves, William E. Walsh, Designing the market game for a trading agent competition, IEEE Internet Computing 5 (2) (2001) 43–51.

[35] Colin R. Williams, Valentin Robu, Enrico H. Gerding, Nicholas R. Jennings, IAMhaggler: a negotiation agent for complex environments, in: Takayuki Ito, Minjie Zhang, Valentin Robu, Shaheen Fatima, Tokuro Matsuo (Eds.), New Trends in Agent-based Complex Automated Negotiations, Series of Studies in Computational IntelligenceSpringer-Verlag, Berlin, Heidelberg, 2012, pp. 151–158.

[36] Colin R. Williams, Valentin Robu, Enrico Gerding, Nick Jennings, Towards a platform for concurrent negotiations in complex domain, Proceedings of the Fifth International Workshop on Agent-based Complex Automated NegotiationsACAN, 2013(in press).

![](/api/attachments/KN6KECMC/fulltext/images/d8655836adc757ddc85c4d22c04132b93954e6cd851fe9833f53be9e78008331.jpg)

Tim Baarslag is a PhD researcher at the Faculty of Electrical Engineering, Mathematics and Computer Science of the Delft University of Technology, where he works in the Interactive Intelligence group on the topic of intelligent decision support systems for automated negotiation. He obtained his MSc degree in Mathematics and a BSc degree in Computer Science from Utrecht University. Tim's prior research involved the foundations of mathematics and the complexity analysis of recursive algorithms. His present research interests include arti<sup>fi</sup>cial intelligence, game theory, decision making, and machine learning.

![](/api/attachments/KN6KECMC/fulltext/images/efef6eb6a84341d8f235405f52b7cede2820ae2c435398bbdeb8be9367dc860b.jpg)

Koen Hindriks is Assistant Professor at the Interactive Intelligence group at the Faculty of Electrical Engineering, Mathematics and Computer Science of the Delft University of Technology. He studied computing science, and completed his PhD at Utrecht University on agent programming languages. He has published more than 100 papers on agent technology and organized various events in this area including the 2012 Dagstuhl Seminar Engineering Multi-Agent Systems. His main research interests are cognitive agent technology and coordination models for effective multi-agent interaction. His research focuses on the analysis, modeling, and development of agent technology that integrates different aspects of intelligence such as reasoning, decision-making, planning, learning and interaction but also integrates aspects such as emotional intelligence. This multi-agent technology has been applied, among others, in micro-simulation of domains such as traf<sup>fi</sup>c, logistics and supply chain management, serious gaming, negotiation, socio-cognitive robotics, and user modeling. He has designed and developed the agent programming languages 3APL and GOAL and worked on the veri<sup>fi</sup>cation and speci<sup>fi</sup>cation of agent programs.

![](/api/attachments/KN6KECMC/fulltext/images/d447397d96bd407db3987619d829ae7be81103c22fbebeaf451f2142b7c92450.jpg)

Catholijn Jonker is full professor of Man–machine Interaction at the Faculty of Electrical Engineering, Mathematics and Computer Science of the Delft University of Technology. She studied computer science, and did her PhD studies at Utrecht University. After a post-doc position in Bern, Switzerland, she became assistant (later associate) profes sor at the Department of Arti<sup>fi</sup>cial Intelligence of the Vrije Universiteit Amsterdam. From September 2004 until September 2006 she was a full professor of Arti<sup>fi</sup>cial Intelligence/Cognitive Science at the Nijmegen Institute of Cognition and Information of the Radboud University Nijmegen. She chaired De Jonge Akademie (Young Academy) of the KNAW (The Royal Netherlands Society of Arts and Sciences) in 2005 and 2006, and she was a member of the same organization from 2005 to 2010. She is a board member of the National Network Female Professors (INVH) in The Netherlands Since 2013 she is a member of the Academia Europae.
