---
otero_id: 12784
otero_key: "YTMVNRY5"
title: "A reinforcement learning model for supply chain ordering management: An application to the beer game"
authors: "S. Kamal Chaharsooghi; Jafar Heydari; S. Hessameddin Zegordi"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.03.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A reinforcement learning model for supply chain ordering management: An application to the beer game

S. Kamal Chaharsooghi ⁎, Jafar Heydari, S. Hessameddin Zegordi

Industrial Engineering Department, School of Engineering, Tarbiat Modares University, Tehran, Iran

a r t i c l e i n f o

Article history: Received 18 July 2006 Received in revised form 18 March 2008 Accepted 26 March 2008 Available online 8 April 2008

Keywords: Supply chain Ordering policy Multi-agent systems Beer game Reinforcement learning

## a b s t r a c t

A major challenge in supply chain ordering management is the coordination of ordering policies adopted by each level of the chain, so as to minimize inventory costs. This paper describes a new approach to decide on ordering policies of supply chain members in an integrated manner. In the first step supply chain ordering management has been considered as a multi-agent system and formulated as a reinforcement learning (RL) model. In the <sup>fi</sup>nal step a Q-learning algorithm is proposed to solve the RL model. Results show that the reinforcement learning ordering mechanism (RLOM) is better than two other known algorithms.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Supply chain management (SCM) literature covers wide range of areas such as logistics, production, scheduling, facility location, procurement, inventory management, ordering management, and so on. Supply chain ordering management (SCOM), which is the main concern of this paper is an integrated approach to determine the ordering size of each actor of SC to the upstream actor aiming to minimize inventory costs of the whole supply chain. SCOM is ultimately focused on the demand of the chain aiming to reduce inventory holding costs, lower slacks, improve customer services, and increase the bene<sup>fi</sup>ts throughout the entire supply chain.

In this paper, the supply chain is considered as a combination of various multi-agent systems collaborating with each other. Thus, SCOM can be viewed as a multi-agent system, consisting of ordering agents. Each ordering agent tries to make decisions on ordering size of the relevant echelon by considering the entire supply chain. Agents interact and cooperate with each other based on a common goal. For example, in a linear supply chain with four echelons (as considered in this paper), there are four ordering agents in SCOM system, each of which is responsible for ordering decisions in its particular echelon. The main objective of ordering agents is to minimize long-term system-wide total inventory cost of ordering from immediate supplier. This is a complex task because of the uncertainty embedded in the system parameters (e.g. customer demand and lead-times) and demand ampli<sup>fi</sup>cation effect [4], known as ‘bullwhip effect’[13].

This paper has focused on the ordering agents of the supply chain and aims to make a proper learning mechanism for these agents. Under learning mechanism, agents learn how to react to the changing environment.

The type of considered supply chain is serial with four levels: retailer, distributor, manufacturer, and supplier respectively. A classical example of supply chain ordering management is the MIT beer game [24], which has attracted much attention from supply chain management researchers. In the MIT beer game, actor of each level attempts to minimize the whole supply chain inventory costs. The decision of ordering size depends on various factors such as supply chain inventory level, environment parameters, downstream ordering size, and so on. Since, companies face global markets and highly turbulent environments, complexity of production and business processes is increased. In such complex conditions a <sup>fi</sup>xed ordering rule cannot achieve the system's goal and therefore supply chain actors must make their decisions based on the system's state. Previous related works proposed <sup>fi</sup>xed ordering rules with no attention to the uncertainties of the environmental factors and their impacts on ordering policy of the chain. The current research addresses this problem by considering environment state in producing ordering policy in each time step. In our proposed model, environmental uncertainties include customer demand and lead-times as two common uncertainties in real world supply chains.

The paper is organized in the following way. Section 2 provides a brief literature review. Section 3 generally describes the reinforcement learning problem. Section 4 describes the problem and its modeling in the form of the reinforcement learning model. Section 5 is about validity of proposed model (RLOM) by comparing it with two other known algorithms (1-1 algorithm and GA-based algorithm was proposed in 2002 by Kimbrough et al. [11]).

## 2. Literature review

Studies on supply chain inventory management generally recognize three stages, namely supply, production and distribution [3,5]. In a few cases, the researchers' focus is placed on the coordination and integration of inventory policies between more than three stages [11,16]. When there is no coordination among supply chain partners, each entity makes decision based on its own criteria, which results in local optimization as opposed to global optimum. Models for coordinated supply chain management are classi<sup>fi</sup>ed in three parts: buyer–vendor coordination, production–distribution coordination and inventory–distribution coordination. Firms have an opportunity to reduce operating costs while simultaneously improving customer service by coordinating the planning of these stages [31]. In the literature it is clearly shown that consideration of the entire supply chain including suppliers, manufacturers, distributors, and retailers, especially in cases with more than one actor in each level, is so complicated.

The bullwhip effect [13] is a critical issue in the supply chain management. As clari<sup>fi</sup>ed in the literature [13,18], a small variance in the demands of the downstream customers may cause very high variance in the procurement quantity of upstream suppliers due to the bullwhip effect. The distortion of demand information can be viewed as a major factor in the formation of the bullwhip effect because of three related phenomena: (1) bias demand information from the downstream actors, (2) delay on information transferring between chain members, and (3) inappropriate logistical supports through the chain members [22].

In many researches, integration of all actors of supply chain is emphasized [5,10]. Simultaneous enhancement of ef<sup>fi</sup>ciency and responsiveness needs coordination and integration of the whole supply chain partners. When the decision making processes of the supply chain partners are independent from each other, the received orders may not lead to a favorable supply policy for the upstream. The coordination of order and supply policies in two-echelon supply chain is investigated via bargaining models [26]. Also more strategies has been introduced in the literature for coordinating order and supply, one of most applicable is vendor managed inventory (VMI), in which, the retailers delegate the ordering and replenishment decisions to the manufacturer. Recently, integration of SC members under VMI initiative has been investigated by Yao et al. [33]. In a study on coordination among supply chain partners, the impact of order decision on reducing lead-times has been investigated in two-echelon supply chain. It is shown that, decreasing the order variability received by upstream, generates shorter and less variable lead-times. This introduces a compensating effect on the downstream inventory level by decreasing the order variability received by upstream [2].

Environment uncertainties intensify the need for coordination among chain members. The uncertainties can happen in various aspects. Main aspects of uncertainty investigated in literature, are demand uncertainty [5,6,8,10,11,21], and leadtimes uncertainty [5,11,20]. Also beyond these two common types of uncertainties, some other types of uncertainties have been considered; e.g. impact of environmental uncertainties including customer uncertainty, supplier uncertainty, and technology uncertainty on information sharing and information quality has been considered [15]. An integrated system for managing inventories in a multi-echelon spare parts SC has been analyzed when chain involved very variable and lumpy demand: in which basic idea was separation of demand in two series (stable and irregular demand patterns) and adoption of proper forecast technique for each of them separately [10]. By capturing the trade-off between customer demand satisfaction and production costs, it has been shown service level can be improved for a reasonable increase in the total SC costs [8]. Concept of echelon stock for integrating inventory management in supply chain in a three levels SC has been considered in an environment with two uncertainty aspects: market demand and inventory holding and backorder costs [6]. Variability of lead-times between successive stages of the chain has a great effect on the coordination of supply chain. In one study [20] reducing both LT mean and variance in a two-echelon dual-sourced supply chain as an investment has been investigated. It has been shown coordinating the chain members in reduction of lead time reduce the total SC costs. One of the most crucial effects of demand uncertainties is the increasing inventory level and decreasing customer service, simultaneously [10]. Sheu addresses the issues regarding the uncertainty and complexity of the distortion of demand-related information existing broadly among supply chain members for ef<sup>fi</sup>cient supply chain coordination [22].

Using inventory management policies such as order batching can distort the customer demand in upstream levels [14]. Ordering policies have a critical role in the inventory related costs and provided service level throughout the supply chain. In cases of deterministic demand with penalty cost (for unsatis<sup>fi</sup>ed orders) the optimal order for every member of the chain is the so-called “pass order” or “one for one” policy. According to 1-1 policy, each actor of chain orders to upstream whatever is ordered from downstream [11]. 1-1 policy is an ordering strategy appropriate for deterministic environments. Some ordering policies are introduced in literature in the uncertain environments [5,11]. Also, reinforcement learning model in three-level supply chain with periodic inventory policy is applied by Giannoccaro and Pontrandolfo [5]. Although, there are some similarities between their work and this study in using reinforcement learning, nevertheless there are major differences such as action space, cost structure, and solving algorithm.

The Beer game [24] is a well-known example of supply chain which has attracted much attention from practitioners as well as academic researchers. Optimal parameters of the beer game ordering policy, when customers demand increases, have been analyzed in two different situations. It has been shown that minimum cost of the chain (under conditions of the beer game environment) is obtained when the players have different ordering policies rather than a single ordering policy [25]. Indeed, most of previous works on order policy of beer game use genetic algorithms as optimization technique [11,25]. But, in this study a reinforcement learning model is applied for determining beer game ordering policy. One ordering policy based on genetic algorithm under conditions of the Beer game environment was introduced [11]; we call that GA-based algorithm in this paper. GA-based algorithm has some degrees of freedom contrary to 1-1 algorithm; In the GA-based algorithm, each actor of chain can order based on its own rule and learns its own ordering policy in coordination with other members with the aim of minimizing inventory costs of the whole supply chain. One limitation of GA-based algorithm is the constraint of <sup>fi</sup>xed ordering rule for each member through the time. We have addressed this limitation by the proposed model (RLOM).

## 3. Reinforcement learning model

Learning techniques are often divided into supervised, unsupervised and reinforcement learning (RL) methods. Supervised learning requires the explicit provision of input– output pairs and the task is constructing or mapping from one to the other. Unsupervised learning do not require target data, this method only performs processing on the input data. In contrast, RL uses a reward signal to evaluate input–output pairs and hence discover the optimal outputs for each input [23].

Reinforcement learning (RL) is learning what to do – how to map situations to actions – so as to maximize a numerical reward signal. The learner is not told which actions to perform in each situation, as in most forms of machine learning, but instead must <sup>fi</sup>nd which actions yield the most reward by trying them in each state [27]. In another word, RL is the study of programs that improve their performance by receiving reward and punishments from the environment [28].

Basic idea of reinforcement learning is base on constant interaction between the learning agent and environment. The agent select an action and the environment respond to it and present a new situations to the agent [27]. Fig. 1 shows the agent–environment interaction in RL models.

As shown in Fig. 1 in the time step t agent takes action $a _ { t }$ based on the environment state. One time step later, in part as a consequence of its action, the agent receives a numerical reward $r _ { t + 1 }$ and <sup>fi</sup>nd itself in the new state $S _ { t + 1 } .$ Reward $r _ { t + 1 }$ can be the criterion of selecting action $a _ { t }$ in state $s _ { t }$ but is not suf<sup>fi</sup>cient criterion because of the problem is long-term and rewards can only consider short-term consequences.

![](/api/attachments/YTMVNRY5/fulltext/images/e131f763413a85f034ee0b982cdad0fd8e43ff2b6f30cc1a300c1554ae81a878.jpg)  
Fig. 1. Agent–environment interaction in RL models

RL framework is simple and <sup>fl</sup>exible thus it is possible to apply it to many different problems in many different ways [27]. In RL models the purpose or the goal of agent (or multiagent system) is formalized in terms of a special reward signal passing from the environment to the agent (or multi-agent system) [27].

This learning method uses the agent's experience to improve the performance index with respect to a particular task [12]. Applications of RL methods are abound, mostly in the <sup>fi</sup>elds of game playing [29,30], robotics [19], scheduling [34] and inventory control [5,17].

Although the convergence property of RL has been widely investigated by machine learning researchers, but its applications to practical problems are still constrained by the curse of dimensionality [1].

## 3.1. Markov decision process

Many real-life decision making problems are found in stochastic environments, in these cases the uncertainty of environment state adds to the complexity of their analysis and create very complicated problems. A subset of these stochastic problems can be formulated as Markov or semi-Markov decision problems [7].

In the RL framework, the agent makes its decisions as a function of a signal from the environment called the environment state. A state signal that succeeds in holding all relevant decision making information is said to be Markov, or to have Markov property. Formal de<sup>fi</sup>nition of Markov property is [27]:

$$
\begin{array}{l} P r \{s _ {t + 1} = s ^ {\prime}, \quad r _ {t + 1} = r | s _ {t}, a _ {t}, r _ {t}, s _ {t - 1}, a _ {t - 1}, r _ {t - 1}, \dots , s _ {0}, a _ {0}, r _ {0} \} \\ = P r \{s _ {t + 1} = s ^ {\prime}, \quad r _ {t + 1} = r | s _ {t}, a _ {t} \}. \end{array}\tag{1}
$$

In another word, if the state signal has Markov property then the environment's response at time step t+1 depends only on the state and action representations at time step t, thus any relevant information for decision making is retained.

A reinforcement learning task satisfying the Markov property is called a Markov Decision Process, or MDP [27]. Standard RL theory has provided a comprehensive framework to solve Markov decision problems.

## 3.2. Parameters of RL model

In Markov environment, P(sV|s,a) gives the probability of arriving state $s ^ { \prime }$ by selecting action a at state s [9]. States in basic RL model should have Markov property but, even when the state is non-Markov, it is still appropriate to consider it as an approximation to a Markov state [27].

In reinforcement learning, rewards must represent the goals, which means, by maximizing the rewards, RL will improve the system toward its goals.

Q(s,a) is de<sup>fi</sup>ned as action-value function (or Q-function). The value function de<sup>fi</sup>nes the summation of the discounted rewards accumulated toward the future [9].

If the $Q ( s , a )$ was suf<sup>fi</sup>ciently large then selecting action a in state s is proposed by RL mechanism.

De<sup>fi</sup>nition of $Q ( s , a )$ is:

$$
Q (s, a) = E \{R _ {t} | s _ {t} = s, a _ {t} = a \}\tag{2}
$$

That:

$$
R _ {t} = \sum_ {k = 0} ^ {\infty} \gamma^ {k} r _ {t + k + 1}.\tag{3}
$$

Value of taking action a in state s is de<sup>fi</sup>ned as the expected reward starting from s and taking the action a. γ is the discount rate and de<sup>fi</sup>ned between 0 and 1.

It's possible to visualize Q-functions as a simple table of Qvalues as in Fig. 2.

Solving a reinforcement learning task means <sup>fi</sup>nding a solution (a policy) that achieves as much reward as possible over the long run (i.e. value). Since, in most real world cases, complete and accurate model of the environment's dynamics is not achievable, calculation of future rewards is not possible and therefore $Q ( s , a )$ must be estimated. Various learning methods have been developed for Q-function estimation (e.g. Q-learning [32]). After learning process is <sup>fi</sup>nished then, action with the highest Q-function is selected for each arriving state.

One of the challenges that appear in reinforcement learning and not in other kinds of learning is the trade-off between exploration and exploitation. The most important feature to distinguish RL from other types of learning is the use of training information to evaluate the actions taken rather than instructs by giving correct actions. This creates the need for proper exploratory behavior by explicit trial and error. On the other hand if RL maintains estimates of the action values, then at any given time at least one action exists whose estimated value is greatest; it is called greedy action. RL mechanism can exploit its current knowledge of the value of the action by selecting a greedy action (based on its criterion of best action). In the initial steps of learning the agents more explore, but in the next steps the probability of exploration decreases as the probability of exploitation increases. In each time step:

$$
\operatorname * {P r} _ {\text { exploration }, t} + \operatorname * {P r} _ {\text { exploitation }, t} = 1.\tag{4}
$$

Indeed, the agent in each time step has two choices: to explore (by probability $P r _ { \mathrm { e x p l o r a t i o n , t } } )$ or to exploit its knowledge (by probability $P r _ { \mathrm { e x p l o i t a t i o n , t } } ) .$ It is rational that agent mostly explores at <sup>fi</sup>rst because of lack of knowledge about environment. In the next steps, contrary to the early steps, it is essential for agent to improve its knowledge (learning the value of Q-functions for each state–action pair) by testing the actions repeatedly in each state.

Policy in RL model is a mapping from each state s and action a to the probability of taking action a when the system is in state s. Optimal policy is the mapping from each state s to the best action on this state.

## 4. Problem description and modeling

A simple linear (vs. network) supply chain is considered in this paper which consists of four levels, namely supplier, manufacturer, distributor, and retailer, with only one actor at each level. Fig. 3 shows the supply chain model and its parameters.

According to the supply chain model shown in Fig. 3 three groups of variables are speci<sup>fi</sup>ed to characterize the supply chain:

$S _ { i } ( t )$ represents inventory position of level i in the time step $t , \quad i = 1 , 2 , 3 , 4$

$O _ { i j } ( t )$ represents ordering size of level i to the upstream level $j , \quad i = 0 , 1 , 2 , 3 , 4 ; \quad j = i + 1$

$T _ { i j } ( t )$ represents distribution amount of leveli to the downstream level $, i = 1 , 2 , 3 , 4 , 5 ; j = i - 1$

As shown in Fig. 3 each actor distributes goods and services to the downstream actor. In this model $O _ { i j }$ and $T _ { i j }$ respectively represents information and material <sup>fl</sup>ows between sequenced supply chain actors. In this supply chain, customer demands must be met by retailer immediately otherwise the order is backlogged and retailer incurs the penalty cost. Also backlogged orders in each level are liable to penalty cost. The orders just received plus any backlog orders are <sup>fi</sup>lled if possible; the actor decides how much to order to replenish stock. In every level at each time step, four events happen: 1—previous orders are received (according to the lead-times) from upstream actor 2—order is received from downstream level 3—the received order is ful<sup>fi</sup>lled from onhand inventory (if possible) 4—actor decides about placing order for stock replenishment. This inventory system can be viewed as a periodic inventory review with one period cycle time (i.e. in each period, actor can place replenishment orders to the upstream after ful<sup>fi</sup>llment of the downstream order).

We de<sup>fi</sup>ned $\mathrm { L T } _ { i j }$ as lead time of level i to the level j (that j=i − 1) of the supply chain. As noted above $\mathrm { L T } _ { 1 0 } ( t ) { = } 0 .$

Order size of customer in this chain is uncertain i.e. no actor of chain knows new demand of customer before customer ordering. If retailer has suf<sup>fi</sup>cient stock then comply the customer demands, otherwise the backlog order cause penalty costs scaled to amount of backlogged orders.

<table><tr><td></td><td> ${\mathrm{S}}_{1}$ </td><td> ${\mathrm{S}}_{2}$ </td><td>...</td><td> ${\mathrm{S}}_{\mathrm{m}}$ </td></tr><tr><td> $a_1$ </td><td> $Q(s_1,a_1)$ </td><td> $Q(s_2,a_1)$ </td><td>...</td><td> $Q(s_m,a_1)$ </td></tr><tr><td> $a_2$ </td><td> $Q(s_1,a_2)$ </td><td> $Q(s_2,a_2)$ </td><td>...</td><td> $Q(s_m,a_2)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $a_n$ </td><td> $Q(s_1,a_n)$ </td><td> $Q(s_2,a_n)$ </td><td>...</td><td> $Q(s_m,a_n)$ </td></tr></table>

Fig. 2. Q-table.

![](/api/attachments/YTMVNRY5/fulltext/images/83483d2fa8919319b101154ee0c28216f6e2e81e2a594c0a2f59fbf27ac11068.jpg)  
Fig. 3. Supply chain model

Moreover in this problem we are faced with the uncertainties of lead-times. Lead time of any level of the chain except $\mathrm { L T } _ { 1 0 } ( t )$ in the time step t is uncertain $( \mathrm { L T } _ { 1 0 } ( t ) { = } 0 )$ It means that after receiving the order from downstream level to the actor of level i, if stock of level i was suf<sup>fi</sup>cient to comply the order then order is ful<sup>fi</sup>lled but – by reasons of shipment problems, logistics uncertainties and so on – there is an uncertain lag between ful<sup>fi</sup>llment of the order by actor i and its receipt by the actor $j = i \ - \ 1$ . Thus in each time step there are two uncertain parameters: 1—customer demand 2—lead-times (except consumer lead time).

The objective of supply chain ordering management is to determine quantity of $O _ { i j }$ in the way that total inventory cost of the chain consist of inventory holding cost and penalty cost of backlog orders is minimized:

$$
\text { Minimize } \sum_ {t = 1} ^ {n} \sum_ {i = 1} ^ {4} [ \alpha h _ {i} (t) + \beta C _ {i} (t) ]\tag{5}
$$

Where:

$$
h _ {i} (t) = \left\{ \begin{array}{l l} S _ {i} (t) & \quad \text { if } S _ {i} (t) > 0 \\ 0 & \quad \text { otherwise } \end{array} \right.\tag{6}
$$

$$
C _ {i} (t) = \left\{ \begin{array}{l l} | S _ {i} (t) | & \quad \text { if } S _ {i} (t) \leq 0 \\ 0 & \quad \text { otherwise } \end{array} \right.\tag{7}
$$

$h _ { i } ( t )$ is de<sup>fi</sup>ned as on-hand inventory of level i at time step t and $C _ { i } ( t )$ is de<sup>fi</sup>ned as backlog in level i at time step t. The latter is liable for the penalty cost. α and $\beta$ are de<sup>fi</sup>ned as inventory holding cost of each actor, per unit per period (e.g., in the MIT Beer Game, US\$2 per case per week) and backorder cost of each actor/unit/period (e.g., in the MIT Beer Game, US\$2/case/week), respectively[11]. n is time horizon and in our case is equal to 35 weeks. According to Eqs. (6) and (7), $h _ { i } ( t )$ and $C _ { i } ( t )$ are functions of inventory position on level i at time step t. Inventory position of each supply chain level at each time step is determined based on receiving orders from upstream (according to uncertain lead-times) and distributed amount to the downstream actor at time step t. On the other hand, both received orders from upstream and distributed amount to downstream, are functions of order size $O _ { i j }$ and therefore decision variables $O _ { i j }$ are embedded in the objective function 5.

## 4.1. Agent-based modeling of supply chain ordering system

To apply RL mechanism on the ordering management problem, described in this paper, it is necessary to formulate the problem in the form of RL models. As noted above RL models are applied in the agent-based framework, thus in the <sup>fi</sup>rst step it is essential to model the ordering problem to the agent-based framework. In the next step characteristics of RL problem are de<sup>fi</sup>ned on the designed agent-based framework.

Supply chain has various operations, each of which must be managed in the right manner. By agent-based modeling, each process (e.g. ordering) through the supply chain is considered as a multi-agent system. In the real world, each actor of the supply chain makes its own decisions autonomously about ordering size but in the case of minimizing the inventory cost of entire supply chain, it is essential for actors to cooperate, coordinate, and interact with each other. Fig. 4 shows the agent-based framework of supply chain ordering management system.

As shown in Fig. 4, to create an agent-based platform to apply RL mechanism on the ordering management problem, we consider SCOM as a multi-agent system that each ordering agent in this system is responsible for making decisions autonomously about ordering size by cooperating and interacting with other agents. Aim of this system is to achieve the common goal of minimizing the entire supply chain inventory cost. Note that in this type of modeling SCOM is one of SCM subsystems along with other subsystems such as transportation system, <sup>fi</sup>nancial system, marketing system, and so on, each of them can be modeled as a multi-agent system.

Different activity must be done in SCOM such as negotiation mechanisms, controlling the system, learning mechanism, and so on. In our model there are four ordering agents in SCOM instead of four actors of the supply chain. The ordering agent of each echelon is identical to the other echelon's ordering agents. Every four agents must make their own decisions simultaneously and inform the ordering size to the upstream actor. Information on inventory positions is shared by ordering agents which is presented as system state in the format of a four element vector. Ordering agents through the supply chain, coordinate with each other by meeting the system state and making decision through the common learning mechanism. In the next section this system has been modeled as a reinforcement learning problem.

![](/api/attachments/YTMVNRY5/fulltext/images/b142cc3fc1aa60ed4efd5cb4cb1ac6a23edccb54ba455afe20b79e299061f319.jpg)  
Fig. 4. Agent-based framework of supply chain ordering management system.

## 4.2. RL modeling of ordering problem in the supply chain

In this section, characteristics of reinforcement learning model in the SCOM problem are de<sup>fi</sup>ned and key parameters of RL model including the state variable, reward function, value function, and system policy are speci<sup>fi</sup>ed. Elements of reinforcement learning ordering mechanism (RLOM) are described here and the mechanism based on Q-learning is applied to solve the supply chain ordering problem.

## 4.2.1. State variable

As noted in previous section, if system state has the Markov property, then its one-step dynamics (see Eq. (1)) makes it possible to predict the next state and expected next reward given the current state and action. Nonetheless, while the state signal is not absolutely Markov, it is better to assume that it is approximation of Markov. In this way formulating the problem as a RL problem is possible. Since the <sup>fi</sup>nal decision in RL models has been made according to the system state, it is essential for system state to provide proper information for agents' decision making process. In the SCOM problem we de<sup>fi</sup>ne the state vector as:

$$
S (t) = \left[ S _ {1} (t), S _ {2} (t), S _ {3} (t), S _ {4} (t) \right]\tag{8}
$$

Where S(t) is the system state vector at time step t and each S (t) is the inventory position of the actor i at time step t. Thus at time step t a vector include four elements representing the system state that element kth stands for inventory position of actor k. This type of system state de<sup>fi</sup>nition has been used in the literature [5]. It is clear that each element of state vector is in<sup>fi</sup>nite, thus determining the near-optimal policy is impossible because it needs in<sup>fi</sup>nite search power. For this reason we code the state variable to the <sup>fi</sup>nite set by mapping the state vector components to the <sup>fi</sup>nite numbers. Simulation showed that a coding strategy with 9 set is proper for our case. Coding strategy has been showed in Table 1.

It is clear that we mapped the in<sup>fi</sup>nite state size to the 6561 state.

## 4.2.2. Reward function

Objective of SCOM problem is the minimization of the total inventory costs thus we de<sup>fi</sup>ne the reward function as:

$$
r (t) = \sum_ {i = 1} ^ {4} \left[ h _ {i} (t) + 2. C _ {i} (t) \right]\tag{9}
$$

Where r(t) is the reward function at time step t that is a function of holding inventory size and shortage size at time step t. Since we applied our model to the MIT beer game problem, inventory holding cost of each actor per unit per period (coef<sup>fi</sup>cient of h (t)) and backorder cost of each actor/unit/ period (coef<sup>fi</sup>cient of C (t)) must be set to 1 and 2, respectively. In this case, it is better to change the reward function to the loss function as we try to minimize it in the long term. It's clear that in each state we can simply calculate the loss function.

Coding of the system state

<table><tr><td>Actual  $S_{i}$ </td><td> $[-\infty;-6]$ </td><td> $[-6;-3]$ </td><td> $[-3;0]$ </td><td> $[0;3]$ </td><td> $[3;6]$ </td><td> $[6;10]$ </td><td> $[10;15]$ </td><td> $[15;20]$ </td><td> $[20;\infty]$ </td></tr><tr><td>Coded  $S_{i}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr></table>

![](/api/attachments/YTMVNRY5/fulltext/images/2657a74b238f98072afc342bf7f24919274b2d3b6c77d7a48f18ebcace4993f5.jpg)  
Fig. 5. Proposed algorithm based on Q-learning for solving SCOM problem.

## 4.2.3. Value function

Calculating the value function is not as simple as reward function because the next system states are uncertain as uncertainty is embedded in customer demand and lead-times. The customized version of value function applied in the RLOM is similar to general de<sup>fi</sup>nition of Q(s,a) (see Eq. (2)) in which:

$$
R _ {t} = \sum_ {k = 0} ^ {3 4 - t} \gamma^ {k} \sum_ {i = 1} ^ {4} \left[ h _ {i} (t + k + 1) + 2 \cdot C _ {i} (t + k + 1) \right].\tag{10}
$$

Since discounting is not considered in RLOM, the discount factor γ in our model is chosen to be equal to 1.

Note that $h _ { i }$ and C for future periods cannot be calculated and therefore value of $Q ( s , a )$ must be estimated. By estimating Q(s,a) for each state–action pair, the best action in each state will be speci<sup>fi</sup>ed and optimal policy can be derived. In our model, Q-functions are estimated by a mechanism based on Q-learning. It's described in the next section.

## 4.2.4. (X + Y) ordering rule

Ordering rule applied in the RLOM named X+Y [11]. According to this rule, if the agent in the current period has X unit demand from the downstream actor, it orders X+Y unit to the upstream actor. Y can be zero, negative or positive i.e.

the agent can order equal, greater or less than received order. Y is determined by learning mechanism. Simulation shows that the range [0,3] is suitable for Ys in our case. Action vector in period t is de<sup>fi</sup>ned as $\left[ Y _ { 1 t } , Y _ { 2 t } , Y _ { 3 t } , Y _ { 4 t } \right]$ , in which, $Y _ { i t }$ denotes value of Y in X+Y rule for actor i in the time step t.

## 4.2.5. Agent's policy

In the RLOM, optimal agents policy is determined according to the learned value of Q(s,a) i.e. for each state s action with greatest Q(s,a) is selected. Thus after estimation of Q(s,a) for all combination of s,a a greedy search on the Qvalues can converge the algorithm to the near-optimal policy. In the RLOM, policy can be showed as:

$$
Y _ {S} = [ Y _ {1 S}, Y _ {2 S}, Y _ {3 S}, Y _ {4 S} ]\tag{11}
$$

Where Y is the policy in the state S. $Y _ { i S }$ is the value of Y in the X+Y rule for actor i in the system state S.

To solve the problem it is necessary to determine agent polices according to the Q-values thus it is inevitable to estimate the Q-values. In the rest of this section the proposed algorithm to solve the SCOM problem is presented. This algorithm solves the reinforcement learning model of supply chain ordering problem.

Four test problem data: include main test problem [4] and three new generated test problem

<table><tr><td>Experiment</td><td>Variable</td><td>Data (35 weeks)</td></tr><tr><td rowspan="2">Main test problem</td><td>Customer demand</td><td>[15,10,8,14,9,3,13,2,13,11,3,4,6,11,15,12,15,4,12,3,13,10,15,15,3,11,13,10,10,0,0,8,0,14]</td></tr><tr><td>Lead-times</td><td>[2,0,2,4,4,4,0,2,4,1,1,0,0,1,1,0,1,1,2,1,1,4,2,2,1,4,3,4,1,4,0,3,3,4]</td></tr><tr><td rowspan="2">Test problem 1</td><td>Customer demand</td><td>[5,14,14,13,2,9,5,9,14,14,12,7,5,1,13,3,12,4,0,15,11,10,6,0,6,6,5,11,8,4,4,12,13,8,12]</td></tr><tr><td>Lead-times</td><td>[2,0,2,4,4,4,0,2,4,1,1,0,0,1,1,0,1,1,2,1,1,4,2,2,1,4,3,4,1,4,0,3,3,4]</td></tr><tr><td rowspan="2">Test problem 2</td><td>Customer demand</td><td>[15,10,8,14,9,3,13,2,13,11,3,4,6,11,15,12,15,4,12,3,13,10,15,15,3,11,13,10,10,0,0,8,0,14]</td></tr><tr><td>Lead-times</td><td></td></tr><tr><td rowspan="2">Test problem 3</td><td>Customer demand</td><td>[13,13,12,10,14,13,13,10,2,12,11,9,11,3,7,6,12,12,3,10,3,9,4,15,12,7,15,5,1,15,11,9,14,0,4]</td></tr><tr><td>Lead-times</td><td>[4,2,2,0,2,2,1,1,3,0,0,3,3,3,4,1,1,1,3,0,4,2,3,4,1,3,3,3,0,3,4,3,3,0,3]</td></tr></table>

![](/api/attachments/YTMVNRY5/fulltext/images/cc5c0d30baada9c34c6257a3e6ceeca719399f3f9048a79bc222e6f55fc5f9bd.jpg)  
Fig. 6. Accumulated cost vs. week generated by RLOM, GA-based algorithm and 1-1 policy.

## 4.3. Proposed algorithm for solving RL ordering model

In previous sections problem is described and modeled in the form of reinforcement learning problem. In this part an algorithm for solving the RL modeled problem is proposed. Proposed algorithm is based on Q-learning mechanism that is a grand temporal difference method used for solving RL models [32]. In the proposed algorithm the value of Q-functions in the iterative process has been learned, in the end of learning process best action in each state is selected as optimal ordering policy to do for the same state in the future.

Fig. 5 shows the proposed Q-learning based algorithm.

As shown in Fig. 5 the n-periodic system simulated in the speci<sup>fi</sup>c iterations (MAX-ITERATION) and the $Q ( s , a )$ is learned during iterations. Indeed, in each iteration, supply chain ordering agents run for n periods. During the run time, inventory system works and in each state that system receives, one action is selected and $Q ( s , a )$ is modi<sup>fi</sup>ed.

![](/api/attachments/YTMVNRY5/fulltext/images/4f01e9c638d210504edb1ab39f641217d4ba2277fb91d1a4644c580d25b6b289.jpg)

C  
![](/api/attachments/YTMVNRY5/fulltext/images/7e11845084b65f505593a98403cd81cbcbb8f6cd273616cd7a893128a5160283.jpg)

Probability of exploration is a function of iteration number and is reduced with increasing iteration number linearly (in our model from 98% in <sup>fi</sup>rst iteration to 10% in last iteration). Also, in each speci<sup>fi</sup>c iteration, it is reduced during period 1 to period n linearly (in our model from start probability – that is determined based on iteration number – to 2% at nth period).

Reward function during the simulation is calculated by Eq. (9). In each new state, calculation of reward function is straightforward. As shown in Fig. 5, it is possible to estimate the Q-function through the simulation by:

$$
\begin{array}{c} Q (s, a) = (1 - \alpha) Q (s, a) + \alpha \cdot [ - r (t + 1) + \max _ {a ^ {\prime}} Q (s ^ {\prime}, a ^ {\prime}) ] \\ = Q (s, a) + \alpha \cdot [ - r (t + 1) + \max _ {a ^ {\prime}} Q (s ^ {\prime}, a ^ {\prime}) - Q (s, a) ] \end{array}\tag{12}
$$

The rule (12) updates the state–action pair values. In the beginning, the agents have no knowledge about the value of each action in each state, thus the initial value of all Q-functions are set to zero for all state–action pairs. α is learning rate and must be de<sup>fi</sup>ned between 0 and 1. Learning rate controls how much weight must be given to the reward just experienced, as opposite to the old Q-estimate. Note that a very small α can throwback the convergence of algorithm and a very large α (near to 1) can also intensify the effect of a biased sample and throwback the convergence of algorithm. Simulation shows that the learning rate 0.17 is suitable for our case.

The aim of ordering management system is to minimize the inventory cost of whole supply chain. Therefore, the reward function (9) must be minimized. In the learning phase, Eq. (12) is placed in the internal loop and Q-function is estimated for each state that agent gets to. By repeating each

![](/api/attachments/YTMVNRY5/fulltext/images/3e3587202da97f3f8dc0b7b2f4744233fee9b52efa96bc611e727392ae3430dc.jpg)

D  
![](/api/attachments/YTMVNRY5/fulltext/images/90dd7c0743192f1732c00a5cfe9cbfbf8fc8b1db561176162484c9b831b0eee3.jpg)  
Fig. 7. Inventory position vs. week in each tree mechanism at each level of the chain (A: supplier inventory position B: manufacturer inventory position C: distributor inventory position D: retailer inventory position).

Table 3  
Agent's policy in the RLOM (main test problem results)

<table><tr><td rowspan="2">Period</td><td colspan="2">Retailer</td><td colspan="2">Distributor</td><td colspan="2">Manufacturer</td><td colspan="2">Supplier</td><td rowspan="2">Cost</td></tr><tr><td>IP*</td><td>Policy</td><td>IP*</td><td>Policy</td><td>IP*</td><td>Policy</td><td>IP*</td><td>Policy</td></tr><tr><td>0</td><td>12</td><td>x+2</td><td>12</td><td>x+2</td><td>12</td><td>x+2</td><td>12</td><td>x+1</td><td>-</td></tr><tr><td>1</td><td>1</td><td>x+3</td><td>12</td><td>x+1</td><td>12</td><td>x+3</td><td>12</td><td>x+3</td><td>37</td></tr><tr><td>2</td><td>-5</td><td>x+3</td><td>-1</td><td>x+0</td><td>10</td><td>x+2</td><td>10</td><td>x+0</td><td>32</td></tr><tr><td>3</td><td>0</td><td>x+1</td><td>4</td><td>x+0</td><td>1</td><td>x+0</td><td>10</td><td>x+2</td><td>15</td></tr><tr><td>4</td><td>2</td><td>x+1</td><td>-1</td><td>x+0</td><td>-6</td><td>x+2</td><td>-5</td><td>x+0</td><td>26</td></tr><tr><td>5</td><td>-7</td><td>x+2</td><td>-16</td><td>x+1</td><td>-17</td><td>x+1</td><td>-18</td><td>x+0</td><td>116</td></tr><tr><td>6</td><td>0</td><td>x+0</td><td>-19</td><td>x+1</td><td>-17</td><td>x+1</td><td>-22</td><td>x+2</td><td>116</td></tr><tr><td>7</td><td>-13</td><td>x+2</td><td>-24</td><td>x+1</td><td>-28</td><td>x+1</td><td>-38</td><td>x+0</td><td>206</td></tr><tr><td>8</td><td>3</td><td>x+3</td><td>-19</td><td>x+1</td><td>-16</td><td>x+2</td><td>-32</td><td>x+3</td><td>137</td></tr><tr><td>9</td><td>-10</td><td>x+2</td><td>-23</td><td>x+1</td><td>-30</td><td>x+1</td><td>-17</td><td>x+0</td><td>160</td></tr><tr><td>10</td><td>-14</td><td>x+2</td><td>-24</td><td>x+1</td><td>-26</td><td>x+1</td><td>-20</td><td>x+0</td><td>168</td></tr><tr><td>11</td><td>-17</td><td>x+3</td><td>-37</td><td>x+3</td><td>-21</td><td>x+2</td><td>-1</td><td>x+1</td><td>152</td></tr><tr><td>12</td><td>-21</td><td>x+3</td><td>-20</td><td>x+3</td><td>-10</td><td>x+2</td><td>-3</td><td>x+1</td><td>108</td></tr><tr><td>13</td><td>2</td><td>x+1</td><td>6</td><td>x+1</td><td>14</td><td>x+2</td><td>6</td><td>x+3</td><td>28</td></tr><tr><td>14</td><td>15</td><td>x+0</td><td>16</td><td>x+0</td><td>27</td><td>x+0</td><td>23</td><td>x+3</td><td>81</td></tr><tr><td>15</td><td>0</td><td>x+0</td><td>4</td><td>x+0</td><td>17</td><td>x+3</td><td>11</td><td>x+0</td><td>32</td></tr><tr><td>16</td><td>0</td><td>x+3</td><td>-1</td><td>x+1</td><td>17</td><td>x+1</td><td>14</td><td>x+1</td><td>33</td></tr><tr><td>17</td><td>11</td><td>x+1</td><td>14</td><td>x+0</td><td>27</td><td>x+3</td><td>24</td><td>x+0</td><td>76</td></tr><tr><td>18</td><td>7</td><td>x+0</td><td>-4</td><td>x+0</td><td>14</td><td>x+0</td><td>8</td><td>x+0</td><td>37</td></tr><tr><td>19</td><td>9</td><td>x+3</td><td>4</td><td>x+2</td><td>12</td><td>x+3</td><td>8</td><td>x+2</td><td>33</td></tr><tr><td>20</td><td>11</td><td>x+2</td><td>10</td><td>x+3</td><td>23</td><td>x+3</td><td>6</td><td>x+3</td><td>50</td></tr><tr><td>21</td><td>-2</td><td>x+0</td><td>4</td><td>x+3</td><td>9</td><td>x+2</td><td>-2</td><td>x+3</td><td>21</td></tr><tr><td>22</td><td>6</td><td>x+2</td><td>8</td><td>x+3</td><td>24</td><td>x+1</td><td>17</td><td>x+1</td><td>55</td></tr><tr><td>23</td><td>6</td><td>x+2</td><td>7</td><td>x+3</td><td>23</td><td>x+1</td><td>17</td><td>x+1</td><td>53</td></tr><tr><td>24</td><td>1</td><td>x+1</td><td>8</td><td>x+2</td><td>21</td><td>x+1</td><td>18</td><td>x+1</td><td>48</td></tr><tr><td>25</td><td>-2</td><td>x+1</td><td>-9</td><td>x+2</td><td>1</td><td>x+1</td><td>4</td><td>x+0</td><td>27</td></tr><tr><td>26</td><td>-13</td><td>x+2</td><td>-13</td><td>x+1</td><td>-18</td><td>x+1</td><td>-17</td><td>x+0</td><td>122</td></tr><tr><td>27</td><td>-6</td><td>x+2</td><td>-5</td><td>x+2</td><td>-10</td><td>x+3</td><td>-17</td><td>x+3</td><td>76</td></tr><tr><td>28</td><td>18</td><td>x+1</td><td>20</td><td>x+3</td><td>20</td><td>x+2</td><td>24</td><td>x+0</td><td>82</td></tr><tr><td>29</td><td>8</td><td>x+0</td><td>5</td><td>x+1</td><td>15</td><td>x+1</td><td>8</td><td>x+2</td><td>36</td></tr><tr><td>30</td><td>-2</td><td>x+2</td><td>-6</td><td>x+2</td><td>-3</td><td>x+2</td><td>1</td><td>x+1</td><td>23</td></tr><tr><td>31</td><td>-2</td><td>x+3</td><td>-16</td><td>x+0</td><td>-15</td><td>x+3</td><td>-18</td><td>x+3</td><td>102</td></tr><tr><td>32</td><td>16</td><td>x+3</td><td>0</td><td>x+1</td><td>-3</td><td>x+1</td><td>7</td><td>x+2</td><td>29</td></tr><tr><td>33</td><td>10</td><td>x+3</td><td>-1</td><td>x+2</td><td>10</td><td>x+3</td><td>9</td><td>x+1</td><td>31</td></tr><tr><td>34</td><td>15</td><td>x+3</td><td>3</td><td>x+0</td><td>13</td><td>x+0</td><td>22</td><td>x+1</td><td>53</td></tr><tr><td>35</td><td>1</td><td>-</td><td>0</td><td>-</td><td>0</td><td>-</td><td>15</td><td>-</td><td>16</td></tr><tr><td>Total cost=</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2417</td></tr></table>

⁎IP means inventory position

state through the simulation period, Q(s,a) for each state– action pair converges. After <sup>fi</sup>nishing the learning phase, the best action in each state is retrievable by a greedy search on each state through the Q-table (see Fig. 2).

In the next section validity of proposed model is discovered by its compare with two other known mechanisms.

## 5. Experimental result and validity of RLOM

In this section validity of the proposed model is investigated. We compare our model with two other algorithms: 1-1 algorithm and GA-based algorithm [11]. Our test problem is based on beer game that is well-known problem in the supply chain research area. The initial/starting inventories for the MIT Beer Game are 12 cases of beer in the warehouse, 8 cases in the pipeline with 4 cases in the “truck” to be delivered to the warehouse in 1 week and 4 cases in the “train” to be delivered in the warehouse in 2 weeks [24] also game period is equal to 35 weeks. In the <sup>fi</sup>rst experiment we use data from Kimbrough et al. [11]. In this test problem we are faced with both stochastic demand and stochastic lead-times, where demand is randomly generated from a known distribution, e.g., uniformly distributed between [0,15], and lead-times uniformly distributed from 0 to 4. Lead-times for all agents in the time step t are the same.

Also we generate three new test problems with parameters introduced by [11] (i.e. customer demand uniformly distributed between [0,15] and lead-times uniformly distributed from 0 to 4) and compare RLOM with two other algorithm. Table 2 shows the four test problems.

As noted above, in the <sup>fi</sup>rst test problem we use data from [11]. In this case cost of whole supply chain inventory system achieved by RLOM is 2417. This is less than 2555 obtained using GA-based algorithm [11] and much less than 7463 obtained using the 1-1 policy. Fig. 6 shows accumulated cost vs. week in the each 3 algorithms.

Comparison of inventory cost of RLOM with two other algorithms

<table><tr><td></td><td>Main test problem</td><td>Test problem 1</td><td>Test problem 2</td><td>Test problem 3</td></tr><tr><td>1-1 policy</td><td>7463</td><td>5453</td><td>8397</td><td>7826</td></tr><tr><td>GA-based algorithm</td><td>2555</td><td>3109</td><td>4156</td><td>4330</td></tr><tr><td>RLOM</td><td>2417</td><td>3169</td><td>4038</td><td>4205</td></tr></table>

As shown in Fig. 6 accumulated cost in the RLOM seem to discover a dynamic order policy that outperforms GA-based algorithm and 1-1 policy. On the other hand it's pro<sup>fi</sup>table to know about inventory positions in each time step generated by each mechanism; Fig. 7 shows such inventory position by each mechanism.

As noted in the previous section our aim is to reduce inventory costs and it is achieved by supply chain inventory positions approaching to the zero in each moment, because there are no holding inventory cost and penalty cost in inventory position zero at each level of the chain. As shown in Fig. 7 inventory position of each level of the supply chain obtained using RLOM is less than the other two algorithms. Table 3 shows policy of supply chain agents proposed by RLOM in each time step of project. It is clear that agent's policy in each period is determined based on coded state of system e.g. in period 15 system state is [0,4,17,11] thus coded state (see Table 1) is [4,5,8,7], based on this coded state, proposed ordering policy by RLOM is [0,0,3,0].

We also tested for statistical validity by running the three new test problems. Table 4 shows comparison of RLOM with two other algorithms in four test problems (main test problem [11] and three new test problems).

As shown in Table 4, RLOM is much better than 1-1 policy in each of four test problems. Also RLOM is better than GAbased algorithm in three test problem. Only in one test problem GA-based algorithm is a bit better than RLOM.

1-1 policy is a static order policy that replenishes order in each period equal to order received from downstream (i.e. always Y is equal to zero). Algorithms such as 1-1 can discover optimal policy only in deterministic environments. GA-based policy has some dynamic aspects: it uses X+Y policy with varying Yacross agents but <sup>fi</sup>xed over the time. RLOM as shown in Table 3, uses X+Y rule and discovers dynamic ordering policy with varying Y across agents as well as over time. This two dimensional dynamics in the uncertain environment as we faced in this paper, is one of the reasons that RLOM outperforms two other algorithms. Ability of RL models in ef<sup>fi</sup>cient search and use of the fact that the optimal or near-optimal policy is a function from state to action can be viewed as another advantage of the RLOM over two other algorithms.

## 6. Conclusion

In this paper the supply chain ordering management (SCOM) problem has been addressed. In the <sup>fi</sup>rst step we proposed an agent-based supply chain ordering management in which agents manage ordering system of decentralized supply chain, in an integrated manner. In the next step we modeled SCOM as a reinforcement learning problem and in the <sup>fi</sup>nal step the model was solved. Results show that proposed model (RLOM) is ef<sup>fi</sup>cient and can <sup>fi</sup>nd good policies under complex scenarios where analytical solutions are not available. This model is also adaptable to an ever-changing business environment.

In this problem we were faced with the case of stochastic demand and stochastic lead-times; in repeated simulations we paired the policy found by RLOM with 1-1 rules and GA-based algorithms [11]. We consistently found that RLOM performance is better than 1-1 and is almost better than GA-based algorithm (in three test problem RLOM found better solutions).

Our approach is based on three techniques, namely agentbased modeling, reinforcement learning and temporal difference methods for solving the RL problem. The approach has been tested on a linear supply chain model consisting of the Supplying, Manufacturing, Distributing and Retailing. The integrated ordering policy determined through the RLOM outperforms 1-1 policy and GA-based algorithm.

The summarized contributions of this paper are: (1) an agent-based supply chain ordering system is proposed. This framework is simple, <sup>fl</sup>exible and aligned with process-based systems. (2) We design learning mechanism of supply chain ordering agents based on an interactive method. This learning mechanism lets agents to interact and be autonomous. Designing of learning model is completed in 2 stages: implementing reinforcement learning theory to the supply chain ordering problem and solving the derived model.

Results show that reinforcement learning is a powerful method to solve this problem. Furthermore potential of agentbased framework in supply chain management area is illustrated.

Further research should address the issue of having a nonlinear (network) supply chain model. Furthermore, combining negotiation mechanism of agents, with better data sharing mechanism between agents and also combining the SCOM with other subsystems of SCM can be investigated in the future researches.

## Acknowledgements

The authors wish to thank two anonymous referees for their helpful comments that enhanced the presentation of this paper.

## References

[1] R.E. Bellman, Dynamic Programming, Princeton University Press, Princeton, 1957.

[2] R.N. Boute, S.M. Disney, M.R. Lambrecht, B.V. Houdt, An integrated production and inventory model to dampen upstream demand variability in the supply chain, European Journal of Operational Research 178 (2007) 121–142.

[3] S.S. Erenguc, N.C. Simpson, A.J. Vakharia, Integrated production/distribution planning in supplychains: an invited review, European Journal of Operational Research 115 (1999) 219-236

[4] J.W. Forrester, Industrial Dynamics, MIT Press, Cambridge, MA, 1961

[5] I. Giannoccaro, P. Pontrandolfo, Inventory management in supply chains: a reinforcement learning approach, International of Journal Production Economics 78 (2002) 153–161.

[6] I. Giannoccaro, P. Pontrandolfo, B. Scozzi, A fuzzy echelon approach for inventory management in supply chains, European Journal of Operational Research 149 (2003) 185–196

[7] A. Gosavi, Reinforcement learning for long-run average cost, European Journal of Operational Research 155 (2004) 654–674.

[8] A. Gupta, C.D. Maranas, C.M. McDonald, Mid-term supply chain planning under demand uncertainty: customer demand satisfaction and inventory management, Computers and Chemical Engineering 24 (2000) 2613–2621.

[9] S. Ishii, W. Yoshida, J. Yoshimoto, Control of exploitation–exploration meta-parameter in reinforcement learning, Neural Networks 15 (2002) 665-687.

[10] M. Kalchschmidt, G. Zotteri, R. Verganti, Inventory management in a multi-echelon spare parts supply chain, International of Journal Production Economics 81–82 (2003) 397–413.

[11] S.O. Kimbrough, D.J. Wu, F. Zhong, Computers play the beer game: can arti<sup>fi</sup>cial agents manage supply chains? Decision Support Systems 33 (2002) 323–333.

[12] I.S.K. Lee, H.Y.K. Lau, Adaptive state space partitioning for reinforcement learning, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 17 (2004) 577–588.

[13] H.T. Lee, J.C. Wu, A study on inventory replenishment policies in a twoechelon supply chain system, Computers & Industrial Engineering 51 (2006) 257-263.

[14] H. Lee, V. Padmanabhan, S. Whang, The Bullwhip Effect in Supply Chains, Sloan Management Review, 1997, pp. 93–102.

[15] S. Li, B. Lin, Accessing information sharing and information quality in supply chain management, Decision Support Systems 42 (2006) 1641–1656.

[16] W.Y. Liang, C.C. Huang, Agent-based demand forecast in multi-echelon supply chain, Decision Support Systems 42 (2006) 390–407.

[17] S. Mahadevan, N. Marchalleck, K.T. Das, A. Gosavi, Self-improving factory simulation using continuous-time average-reward reinforcement learning, Proceedings of the 14th International Conference on Machine Learning, 1997, pp. 202–210.

[18] R. Metters, Quantifying the bullwhip effect in supply chains, Journal of Operations Management 15 (2) (1997) 89–100.

[19] M. Riedmiller, Application of sequential reinforcement learning to control dynamic systems, Proceedings of 1996 IEEE Internationa Conference on Neural Networks, 1996, pp. 167–172.

[20] S.W. Ryu, K.K. Lee, A stochastic inventory model of dual sourced supply chain with lead-time reduction, International Journal of Production Economics 81–82 (2003) 513–524.

[21] J.D. Schwartz, W. Wang, D.E. Rivera, Simulation-based optimization of process control policies for inventory management in supply chains, Automatica 42 (2006) 1311–1320.

[22] J.B. Sheu, A multi-layer demand-responsive logistics control methodology for alleviating the bullwhip effect of supply chains, European Journal of Operational Research 161 (2005) 797–811.

[23] A.J. Smith, Applications of the self-organising map to reinforcement learning, Neural Networks 15 (2002) 1107–1124.

[24] J. Sterman, Modeling managerial behavior: misperceptions of feedback in a dynamic decision making experiment, Management Science 35 (3) (1989) 321–339.

[25] F. Strozzi, J. Bosch, J.M. Zaldívar, Beer game order policy optimization under changing customer demand, Decision Support Systems 42 (2007) 2153-2163.

[26] E. Sucky, Inventory management in supply chains: a bargaining problem, International Journal of Production Economics 93–94 (2005) 253-262.

[27] R.S. Sutton, A.G. Barto, Reinforcement Learning: an Introduction, MIT Press, Cambridge, MA. 1998.

[28] P. Tadepalli, D. Ok, Model-based average reward reinforcement learning, Artificial Intelligence 100 (1998) 177-224

[29] G.J. Tesauro, Practical issues in temporal difference learning, Machine Learning 8 (1992) 257–277.

[30] G.J. Tesauro, TD-Gammon, a self-teaching backgammon program, achieves master-level play, Neural Computation 6 (2) (1994) 215–219.

[31] D.J. Thomas, P.M. Grif<sup>fi</sup>n, Coordinated supply chain management, European Journal of Operational Research 94 (1) (1996) 1–15.

[32] C.J.C.H. Watkins, Learning from Delayed Rewards, PhD Thesis, University of Cambridge, England, (1989).

[33] Y. Yao, P.T. Evers, M.E. Dresner, Supply chain integration in vendormanaged inventory, Decision Support Systems 43 (2007) 663–674.

[34] W. Zhang, T.G. Dietterich, High-performance job-shop scheduling with a time-delay TD(l) network, in: D.S. Touretzky, M.C. Mozer, M.E. Hasselmo (Eds.), Advances in Neural Information Processing Systems 8: Proceedings of the 1995 Conference, 1996, pp. 1024–1030.

![](/api/attachments/YTMVNRY5/fulltext/images/38d0c995de7fc04dffdb0938bd33ae24fbdf3bb36e1bc1487e5f6973419b48bd.jpg)

Dr. Kamal Chaharsooghi is Associate Professor of Industrial Engineering at the Dept. of I.E., Faculty of Engineering, Tarbiat Modares University, Tehran, Iran. Dr. Chaharsooghi's research interests include: manufacturing systems, supply chain management, information systems, strategic management, international marketing strategy and systems theory. Dr. Chaharsoogh's work

has appeared in European Journal of Operational Research, International Journal of Advanced Manufacturing Technology, Scientia Iranica, Modares Journal of Engineering, Amirkabir Journal of Science and Technology, International Journal of Engineering Science. Dr. Chaharsooghi obtained his PhD from Hull University, England.

![](/api/attachments/YTMVNRY5/fulltext/images/22c855fc2313912089bafce0dc9866943fc97b316c3ff1900df5b237775e4777.jpg)

Jafar Heydari is a PhD candidate of Industrial Engineering in the School of Engineering at Tarbiat Modares University, Iran. He received his MSc from the same university in the Industrial Engineering and his BSc in industrial Engineering from Isfahan University of Technology. His main areas of research interests include agentbased modeling, learning models, supply chain management and meta-heuristics.

![](/api/attachments/YTMVNRY5/fulltext/images/f677067ba5efc894131854837d682e702488ac0f954658f1ccb5e306ebb9d3cb.jpg)

S.H. Zegordi is an Associate Professor of Industrial Engineering in the School of Engineering at Tarbiat Modares University, Iran. He received his PhD from Department of Industrial Engineering and management at Tokyo Institute of Technology, Japan in 1994. He holds an MSc in Industrial Engineering and Systems from Sharif University of Technology, Iran and a BSc in Industrial Engineering from Isfahan

University of Technology, Iran. His main areas of teaching and research interests include production planning and scheduling, multi-objective optimization problems, meta-heuristics, quality management and productivity. He has published several articles in international conferences and academic journals including European Journal of Operational Research, International Journal of Production Research, Journal of Operational Research Society of Japan, Amirkabir Journal of Science and Engineering and Scientia Iranica International Journal of Science and Technology.
