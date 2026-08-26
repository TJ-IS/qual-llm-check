---
otero_id: 21864
otero_key: "9J993Q8R"
title: "Brokerage between buyer and seller agents using Constraint Satisfaction Problem models"
authors: "Jong-Jin Jung; Geun-Sik Jo"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00093-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Brokerage between buyer and seller agents using Constraint Satisfaction Problem models

Jong-Jin Jung, Geun-Sik Jo

Department of Computer Science and Engineering, Inha UniÕersity, Inchon 402-751, South Korea

## Abstract

We have proposed a two-layered multi-agent framework for brokerage between buyers and sellers. The brokerage is processed in two layers for efficient linking between buyers and sellers: the competition layer and the constraint satisfaction layer. In the competition layer, we match the constituents of brokerage process to agents and use a functional relationship of a multi-agent framework for the communication among them. The seller agents, as requested by the buyer agents, are selected through the competition in the competition layer. In the constraint satisfaction layer, we model the relationship between buyer agents and seller agents in Constraint Satisfaction Problems CSP . The CSP solver finds an optimal solutionŽ . by choosing the best brokerage to satisfy various preferential requirements for users. We have implemented a prototype system for dealing in real estate on the Internet by applying the proposed framework. Finally, we have modeled the brokerage system using CSP and have shown the experimentation about the satisfaction level of users regarding their preferences. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Electronic commerce; Multi-agent framework; Constraint satisfaction problems; Agent-based brokerage

## 1. Introduction

Recently, as the Internet has become more widely used, electronic commerce EC has emerged andŽ . has developed a high-level business environment. EC refers to commercial transactions using computers in virtual environments through computer networks. The computer system should deal with a variety of goods such as products, services and information on EC. In

EC, the system gathers useful information about goods to buy or sell and proposes efficient ways of making a contract to help users make the right decisions. The system should maintain reliability for service instead of reducing the user’s role 6 . For<sup>w</sup> <sup>x</sup> that purpose, the system must have the characteristics of intelligence. Many researchers have studied the intelligence of software in AI, and have tried to apply agent technologies to EC applications 6,11,12 .<sup>w</sup> <sup>x</sup>

An agent is a software, which has the characteristics of intelligent behavior that will assist users through communication. These characteristics make intelligent agents one of the most important technologies for EC. Recently, some prototypes of agent-based EC systems have been developed by researchers. Traditional systems, however, often had limitations. They could only consider a few of the user’s requirements for specific goods on EC. They have dealt with goods through the competitive relationship of one certain point of these goods between buyers and sellers 2,6,11,12 . The system, however,<sup>w</sup> <sup>x</sup> has to consider the various features of the goods and the buyer’s requirements for the best contract. For example, in the case of dealing on EC in computers, the sellers show the merits of their products such as the price, the conditions after being serviced, computing power, and the specifications of the computer on the Internet. Each buyer has a different point of view when he wants to buy a computer. If he is a novice, he will preferentially consider the conditions after being serviced. If he is an expert on the computer, he will probably consider computing power as one of the most important conditions for buying. To satisfy various points of the user’s requirements, supplementary coordination steps should be added to the traditional competitive mechanism. A multi-agent framework can be applied to the EC transaction to improve the user’s satisfaction. The multi-agent framework, however, focuses on the cooperative relationship among agents in contrast with the competitive relationship among agents in EC applications. Therefore, the cooperation has to be revised to include a coordination which handles the competition of agents on EC.

In this paper, we propose a two-layered framework which includes a competition layer and a constraint satisfaction layer for brokerage between buyers and sellers on EC. In the competition layer, we use a functional relationship of a multi-agent framework for the competition of agents. We also apply Constraint Satisfaction Problem CSP technique to Ž . the constraint satisfaction layer for the brokerage, which optimally satisfies the user’s requirements. We have also developed an application system for dealing in real estate under the proposed framework.

## 2. Agent technologies in EC applications

An agent is a computer program which can assist users by performing intelligent tasks. It differs from traditional software in that it is autonomous, pro-active, adaptive and intelligently cooperative with others 13 . Recently, agent technologies have been<sup>w</sup> <sup>x</sup> applied to various applications of EC to reduce search and transaction costs. Instead of human beings, intelligent agents can select books and other goods. These agents search goods in online stores and compare these goods to satisfy the needs of the buyer. Stanford’s Informaster 8 has advanced searching capabilities. Informaster provides a form to fill out, which states user’s specifications for types of goods to buy and returns information about goods which match the user’s specifications. BargainFinder <sup>w</sup> <sup>x</sup> 2 provides valuable information for the buyers through price comparison in online stores.

Multi-agent technology can be applied to EC transactions in brokerage situations such as auction and bidding. The multi-agent framework is similar to the EC framework from the viewpoint of the functional relationship of the constituents. In a multi-agent framework, agents share their information and cooperate with other agents to achieve a global goal through the communication channel, dialoguing method, and control mechanism 5,9 . Many re-<sup>w</sup> <sup>x</sup> searchers have developed an EC framework using multi-agent technologies. Kasbah is the marketplace architecture for buying and selling goods 4 . In<sup>w</sup> <sup>x</sup> Kasbah, the buying agent autonomously contacts and negotiates with the selling agent on a one-to-one correspondence. This system makes the best possible offerings for both the buyers and the sellers. UNIK-AGENT is the structure of intelligent agents for the game of electronic marketing 11,12 . UNIK-AGENT<sup>w</sup> <sup>x</sup> is designed as an extension of expert systems with additional capabilities of communication control and meta-problem-solving. Therefore, the buyer can select a product which is best matched to the buyer’s requirements from the bidders because of UNIK-AGENT’s problem-solving methods such as forward chaining or a case-based reasoning mechanism. Our proposed agent uses CSP solver for the best possible deal between buyers and sellers. We have focused on the agent-based framework for brokerage between buyers and sellers, whereas the above researches have focused on the agent-based electronic marketing. The buyer agents autonomously negotiate with the seller agents through the intermediation of the broker agent. The buyer agents also select the best goods from the seller agents by evaluation of CSP solver in the proposed framework.

## 3. Multi-agent interaction framework for brokerage between buyers and sellers

## 3.1. Competition of agents for 1–N relationship

There are three members in the brokerage process: the buyer, the seller, and the broker. The broker is often called the facilitator, which intermediates the relationship between the buyer and the seller. The types of brokerage are different depending on the distribution ratio of the members. If there is one seller and many buyers for goods, it is called an ‘‘auction’’ which focuses on the seller. On the other hand, if there are many sellers and one buyer for goods, it is called ‘‘bidding’’ which focuses on the buyer.

In this paper, we consider the brokerage for bidding. The brokerage process can be implemented by the different agents in the agent-based EC framework. The broker agent controls buyer agents and seller agents for brokerage; i.e., it matches buyer agents to seller agents through the brokerage process. Seller agents maintain a competitive relationship for a buyer agent during the brokerage process. When seller agents show the goods they want to sell, the broker agent evaluates them and selects one which has the most satisfactory qualities based on the buyer’s requirements. The broker agent matches the selected seller agent to the buyer agent for the goods. This is required for competition between distributed agents. For that purpose, we define the high-level communication protocol among the distributed agents. The agents should also have a communication channel, a dialoguing method, and a control mechanism. Traditional communication protocols like TCP<sup>r</sup>IP support a low-level communication environment. The protocols offer a structure whereby agents can transmit bit streams for dialogue between each other. The contract net protocol is well known as one of the most important high-level communication protocols which involve problem-solving communication and control structure for the distributed agents 15,16 . However, contract net protocol fo-<sup>w</sup> <sup>x</sup> cuses on the distributed control of the cooperative task execution with an internode communication mechanism. In this paper, we partially apply the contract net protocol to the competitive nature of distributed agents. We define the framework for brokerage between a buyer and sellers by applying the contract net protocol to the process bidding in Fig. 1.

As shown in Fig. 1, when a buyer want to buy goods, he asks for the brokerage by sending buyer’s requirements with a buy req<sub>–</sub> message to an agent. The agent becomes a buyer agent after receiving the message. The user can qualify an agent as a buyer agent or seller agent according to the type of message, which he sends. The buyer agent then sends the message to the broker agent for the brokerage with sellers. On the other hand, a seller sends specifications for goods with a sell req <sub>–</sub> message to a local agent. When the broker agent accepts the message from the buyer agent, it announces the buyer’s requirements with an announcement message to local agents, meaning the seller agents. If a local agent has goods to satisfy a buyer’s requirements, it will submit a bid with a bid specification<sub>–</sub> message. We will introduce the detailed description of the abovementioned messages in Fig. 5. After the broker agent accepts all bids from the local agents within the given time, an agents group is constituted for the buyer. For the members of the group, the broker evaluates the accepted bids. Finally, the broker selects the best goods and proposes them to the buyer. The brokerage is processed by a competitive mechanism among agents.

![](/api/attachments/9J993Q8R/fulltext/images/d4c1deeb5a754b5c25858a85467abe4b131c6eb0392773d1ab363710a8ad3f9a.jpg)  
Fig. 1. Agents framework for brokerage between a buyer and sellers.

3.2. Agent coordination framework for N–M relationship

The competitive framework of agents is incomplete for the brokerages between buyers and sellers. If there are many buyers for a specific type of goods, it is necessary for additional coordination steps to link buyers to sellers fulfilling their needs. It is different from each buyer’s preferential point of view for the specific goods. Some of seller agents are selected through the competition process for buyers. The selected seller agents should be evaluated based on the buyers’ terms because the seller agents have different specifications for goods based on the buyer’s requirements and preferential points. The buyers can then be efficiently linked to sellers by the results of the evaluation.

In this paper, we propose a two-layered coordination framework which has a competition layer and a constraint satisfaction layer to improve user satisfaction. The proposed framework is showed in Fig. 2.

In Fig. 2, the competition process from the sellers for each buyer can be done simultaneously in the competition layer. A buyer sends buying requirements with a buy req <sub>–</sub> message to an agent. The agent becomes a buyer agent and sends the message to the broker agent. When the broker agent accepts the message from the buyer agent, it announces the buyer’s requirements with an announcement message to local agents. If a local agent has goods to satisfy a buyer’s requirements, it will submit a bid with a bid specification<sub>–</sub> message. After the broker agent accepts all the bids from the local agents within the given time, an agents group is constituted for the buyer. After finishing the competition process, there are two dynamic groups: the group of buyers and the group of sellers based on the buyer’s requirements.

The brokerage can be concluded if the buyer’s requirements match the seller’s specifications for goods at a certain point in the constraint satisfaction layer. The constraint satisfaction process has to be done among the members of two groups for the best satisfaction of the requirements. The constraint satisfaction process can be modeled in CSP. It is necessary to have some kinds of messages in concluding the brokerage in the constraint satisfaction layer. The messages are described in Fig. 5.

3.3. Applying CSP for brokerage between buyers and sellers

We can consider the brokerage process between $n ( n \geq 1 )$ Ž . buyers and m m<sup>G</sup>1 sellers as the dynamic allocation problem. The brokerage is to match buyers with sellers for a certain type of goods in order to satisfy the requirements of both. If the set of buyers or sellers available for allocation does not change during the given time, the process is called static. On the other hand, if new buyers or sellers arise during the given time, the process is called dynamic. The brokerage process is dynamic because buyers or sellers can be changed during the processing time. Traditionally, static models have proven more tractable than dynamic models and have been subjected to more extensive study 1 . The brokerage<sup>w</sup> <sup>x</sup> process can also be considered as an optimization problem because the goal of the brokerage process is to find the set of optimal pairs, which most satisfy buyers and sellers in terms of their requirements. These characteristics of brokerage make it possible to apply CSP techniques to the process. CSP techniques have recently been applied to many compli cated problems in application areas such as operations research, hardware design and artificial intelligence. CSP techniques are very efficient in solving difficult problems, especially discrete combinatorial problems, which are mostly NP-complete <sup>w</sup> <sup>x</sup> <sub>7</sub> <sub>.</sub>

![](/api/attachments/9J993Q8R/fulltext/images/1e3ba64f4a97ce83aa7132f01af021931eceabc8fe1f00dcdf053918f563cde7.jpg)  
Fig. 2. Agents framework for brokerage between buyers and sellers.

In this paper, we propose the CSP model for the constraint satisfaction process where n buyers are assigned to m sellers. The brokerage between n buyers and m sellers can be defined as CSP as shown in Table 1.

CSP has two types of finite domain variables: variables of buyers, $\{ B _ { 1 } , B _ { 2 } , \dots B _ { n } \} , n \ge 1$ , and variables of sellers, $\{ S _ { 1 } , S _ { 2 } , \ldots S _ { m } \} , m \geq 1$ . The variables take their values, respectively, from their finite domains. The variable of buyer $B _ { i } ( 1 \leq i \leq n )$ has the discrete domain values of sellers, $\{ S _ { 1 } , S _ { 2 } , \ldots S _ { m } \}$ and the variable of seller $S _ { i } ( 1 \leq i \leq m )$ has the discrete domain values of buyers, $\{ B _ { 1 } , B _ { 2 } , \ldots B _ { n } \}$ . Both buyers and sellers can be either variables or domain values. If the CSP focuses on buyers, buyers are variables and sellers are domain values. If the CSP focuses on sellers, sellers are variables and buyers are domain values. Finally, constraints are related to variables.

Table 1  
Relationship between buyers and sellers in CSP

<table><tr><td></td><td> $S_{1}$ </td><td> $S_{2}$ </td><td> $S_{3}$ </td><td>...</td><td> $S_{m}$ </td></tr><tr><td> $B_{1}$ </td><td></td><td> $C_{12}$ </td><td></td><td></td><td></td></tr><tr><td> $B_{2}$ </td><td> $C_{21}$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $\vdots$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $B_{n}$ </td><td></td><td></td><td></td><td></td><td> $C_{nm}$ </td></tr></table>

We can consider constraints for a variable to check node consistency as buyer’s requirements which are important factors to purchase goods. For examples, if a buyer requires that the price of a computer is less than 2 million won, the variable of the buyer has the node constraint, $B _ { \mathrm { p } } < 2 { , } 0 0 0 { , } 0 0 0$ . In the case of real estate, a buyer considers buying requirements such as price, moving time, the location of the house, traffic conditions and living condi tions, then we can represent the requirements of node constraints in CSP. These constraints are divided into two kinds of constraints: hard constraints and soft constraints. Hard constraints are represented in the form of an ‘‘equal $_ { \mathrm { t o } } \ ' \ '$ notation. Soft constraints are represented in the form of inequality and the constraints can be relaxed within the given scope of values. For example, if a buyer considers the size of goods as the most important factor in decision-making, he wants to buy goods with a fixed size. We can represent the constraint for the size as $B _ { \mathrm { s } } = 2 0$ . If another buyer places more consideration on the functionality than the size, he can accept variable size as a buying requirement instead of requiring specific functions of goods. We can represent the constraint for the size with the notation, $1 5 \leq B _ { \mathrm { s } } \leq 2 5$ . The former has a hard constraint and the latter has a soft constraint in terms of the size. The sellers show the positive selling points of goods being sold such as the price, the size, the color and the other specifications of goods. We can evaluate the buyer’s satisfaction with the goods by using preferential weights according to the degrees of the buying requirements. The more positively the selling points satisfy the requirements, the better the CSP solver can process the brokerage of the goods.

There are constraints between two variables to check arc consistency shown by $B _ { i } \neq B _ { j }$ . For an example, two buyers cannot make a contract for the same house simultaneously. If $B _ { 1 }$ made the contract, $C _ { 1 2 }$ , with $S _ { 2 } , \boldsymbol { B } _ { 2 }$ could not make a contract with $S _ { 2 }$ The arc constraints have to be considered in the case of brokerage for reselling when there is only one item to buy or sell. If sellers can provide one more item of the same kind of goods, we need not consider the constraints.

The broker agent employs the CSP solver to satisfy constraints. In the CSP model, we can prune the search space with a constraint propagation method and a heuristic search algorithm 7,14 . We can find<sup>w</sup> <sup>x</sup> the optimal solution using an evaluation function by formulating preferential weights in CSP. The CSP solver has to be processed for goods at a specific time by the broker agent.

## 4. An example: brokerage for dealing in real estate

## 4.1. The multi-agent framework for dealing in real estate

In this paper, we proposed an EC framework for brokerage between buyers and sellers on the Internet. The framework is for two types of brokerages. One is for a 1–N relationship such as an auction and bidding. The other is for an N–M relationship where there are many buyers and many sellers for a specific type of goods. The framework is very efficient for the brokerage in an N–M relationship because the CSP solver can optimally link the buyers with the sellers. In the case of an N–M relationship, we have supposed that there is only one item to buy or sell.

We have built a prototype of a brokerage system for dealing in real estate to test the feasibility of our proposed framework. The system processes the brokerage on the Web environment, but does not, at this time, support the entire process of the contract between buyers and sellers. The brokerage for dealing in real estate is of the type N–M relationship when the system links N buyers to M sellers within the given time. The system processes the brokerage based on the condition that there is only one house per seller. When a buyer wants to make a contract for a new house, he considers several important factors such as price, moving time, the location of house, traffic conditions and living conditions. A seller, on the other hand, shows the conditions such as price, moving time and the specifications of his house. We have implemented the brokerage process by using agents.

In our system, agents process business trading for real estate through a two-layered coordination mechanism as shown in Fig. 2. In the competition layer, sellers give the price and the specifications of the houses with the applet for sale requested by a local agent. The agent converts the contents of the applet into the sell req<sub>– –</sub>message as the same type of buy req message shown in Fig. 5. Then the agent saves the information of the message to the database for later bidding. Buyers describe the condition with the applet for buy request in the local agent. The agent converts the contents of the applet into the buy req <sub>–</sub> message and sends the message to the broker agent. The broker agent interprets the message and registers it to the bulletin board. Then the broker agent announces all local agents with the announcement message. The local agents submit the bid specifications to the broker agent at the acceptable time if they have houses to sell.

In the constraint satisfaction layer, the broker agent evaluates the accepted bids by giving preferential weights to them according to the buyer’s preferences. Each bid has different characteristics in terms of the buyer’s preferences. The broker agent efficiently considers several important factors of trading in the constraint satisfaction layer. For the process, the broker agent employs the CSP solver. The CSP solver in the broker agent processes the coordination to satisfy the user’s preferences between the buyer agents and the seller agents. The solver can produce the optimal solution with the evaluation function by assigning preferential weights according to the degrees of the user’s preferences. The algorithm of CSP solver is described below in Fig. 3.

As shown in Fig. 3, inconsistent values in domains for variables are removed before the CSP solver processes the assignment. The inconsistency propagation for the inconsistent values of both discrete and continuous problem domains is researched in Ref. 10 . However, the variables we are dealing <sup>w</sup> <sup>x</sup> with here are the finite discrete domains. The solver has filtered the sellers, which do not have adequate houses for the buyer’s requirements through the bidding request. Thereby, each buyer has acceptable domain values of sellers for the houses in the competition layer. When the CSP solver assigns a variable

```txt
// assign sellers to buyers in CSP which has variables of buyers and domain values of sellers
OPTIMIZATION_BROKERAGE()
BEGIN
    Give preferential weight by estimating user's preferences from buy spec;
    Give preferential weight by estimating user's preferences from sell spec;

    // evaluation is the current evaluation value, optimum is the best evaluation value
    evaluation, optimum;
    feasible list, optimal list; // feasible list is the current solution list, optimal list is the best solution
    start in state 0;    // termination state
    DO
    first select a buyer which has a small sized domain of seller elements;
    DO    // assign a seller to a buyer checking node constraints and arc constraints;
    select a seller which has the highest weight value in domain;
    assign a seller to the buyer;
    remove the seller from the domain;
    propagate constraints by AC-4;
    IF the other domain is empty by AC-4 THEN
    undo the constraint propagation;
    ELSE
    update feasible list and evaluation;
    IF the assigned buyer is last THEN    // there are no more buyers to assign
    IF optimum is less than evaluation THEN
    Update feasible list to optimal list;
    Update evaluation to optimum;
    END IF;
    backtrack to previous buyer selection state;
    END IF;
    END IF;
    WHILE (assignment fails OR a buyer domain is not empty);
    WHILE (do not backtrack to state 0);
END
```  
Fig. 3. CSP algorithm for the brokerage of real estate.

to a value of its domain, the constraints of the variable are propagated by the AC-4 14 . The CSP<sup>w</sup> <sup>x</sup> solver reduces the domains of variables by AC-4 algorithm and processes the search by backtracking. The optimal pairs between buyers and sellers will be listed and transmitted to the user. Finally, the broker agent announces it to the other agents, which do not participate in the process after producing the optimal solution to avoid conflict.

![](/api/attachments/9J993Q8R/fulltext/images/32269eeee50b657e04df586825cf1236d2c724e0a3e4a0bab96b04142754630b.jpg)  
Fig. 4. Architecture of agents and their connections.

## 4.2. The architecture of agents and their connection

We implemented two kinds of agents which have different components according to their roles and functions. Each structure of an agent and its connection to the other agents is shown in Fig. 4.

## 4.2.1. Broker agent

The broker agent controls the local agents with the Agent Name Server ANS . It consists of aŽ . communication module and a problem-solving module. The communication module has components which are necessary to communicate with the other agents. It deals with incoming messages from the other agents and outgoing messages to them. The message generator analyzes the contents of applet and generates the adequate message form<sub>–</sub> . The message queue determines the order of the incoming messages. The message router sends a message to local agents and receives results from the broker agent. The message interpreter parses the received message and extracts the contents of the message for the next process. The Buy&Sell CSP solver makes a solution for brokerage between the buyer agents and the seller agents. It produces an optimal solution with an evaluation function.

<table><tr><td>(evaluate</td><td></td><td></td><td>(evaluate</td><td></td><td></td><td>(reply</td><td></td><td></td></tr><tr><td>:sender</td><td>KangdongLocal</td><td></td><td>:sender</td><td>SeoulBroker</td><td></td><td>:sender</td><td>KangnamLocal</td><td></td></tr><tr><td>:receiver</td><td>SeoulBroker</td><td></td><td>:receiver</td><td>KangnamLocal</td><td></td><td>:receiver</td><td>SeoulBroker</td><td></td></tr><tr><td>-reply-with</td><td>KangdongLocal19971101120520</td><td></td><td>:language</td><td>psudoKQML</td><td></td><td>:language</td><td>psudoKQML</td><td></td></tr><tr><td>:language</td><td>psudoKQML</td><td></td><td>-reply-with</td><td>SeoulBroker19971101120600</td><td></td><td>:in-reply-to</td><td>SeoulBroker19971101120600</td><td></td></tr><tr><td>:ontology</td><td>real_estate</td><td></td><td>:ontology</td><td>real_estate</td><td></td><td>:ontology</td><td>real_estate</td><td></td></tr><tr><td>:content</td><td>(buy_req</td><td></td><td>:content</td><td>(announcement</td><td></td><td>:content</td><td>(bid_specification</td><td></td></tr><tr><td></td><td>:b_accepted_id</td><td>001000001</td><td></td><td>:b_broker</td><td>SeoulBroker</td><td></td><td>:b_broker</td><td>SeoulBroker</td></tr><tr><td></td><td>:b_buy_type</td><td>Sell</td><td></td><td>:b_accepted_id</td><td>1001000001</td><td></td><td>:b_accepted_id</td><td>1001000001</td></tr><tr><td></td><td>:b_region_1</td><td>Seoul</td><td></td><td>:b_buy_type</td><td>Sell</td><td></td><td>:s_accepted_id</td><td>1002000011</td></tr><tr><td></td><td>:b_region_2</td><td>Kyoungki</td><td></td><td>:b_region_1</td><td>Seoul</td><td></td><td>:s_addr</td><td>Kangnam Seocho</td></tr><tr><td></td><td>:b_region_3</td><td>Empty</td><td></td><td>:b_region_2</td><td>Kyoungki</td><td></td><td>:s_region</td><td>Seoul</td></tr><tr><td></td><td>:b_type_1</td><td>APT</td><td></td><td>:b_region_3</td><td>Empty</td><td></td><td>:s_type</td><td>APT</td></tr><tr><td></td><td>:b_type_2</td><td>House</td><td></td><td>:b_type_1</td><td>APT</td><td></td><td>:s_size</td><td>22</td></tr><tr><td></td><td>:b_type_3</td><td>Tenement</td><td></td><td>:b_type_2</td><td>House</td><td></td><td>:s_build_day</td><td>1995</td></tr><tr><td></td><td>:b_type_4</td><td>Empty</td><td></td><td>:b_type_3</td><td>Tenement</td><td></td><td>:s_security</td><td>G</td></tr><tr><td></td><td>:b_size</td><td>20</td><td></td><td>:b_type_4</td><td>Empty</td><td></td><td>:s_far_subway</td><td>10</td></tr><tr><td></td><td>:b_size_from</td><td>18</td><td></td><td>:b_size</td><td>20</td><td></td><td>:s_far_bus</td><td>5</td></tr><tr><td></td><td>:b_size_to</td><td>25</td><td></td><td>:b_size_from</td><td>18</td><td></td><td>:s_price</td><td>3200</td></tr><tr><td></td><td>:b_price</td><td>30000</td><td></td><td>:b_size_to</td><td>25</td><td></td><td>:s_price_from</td><td>3100</td></tr><tr><td></td><td>:b_price_from</td><td>28000</td><td></td><td>:b_price</td><td>30000</td><td></td><td>:s_price_to</td><td>3400</td></tr><tr><td></td><td>:b_price_to</td><td>33000</td><td></td><td>:b_price_from</td><td>28000</td><td></td><td>:s_day</td><td>1997/12/1</td></tr><tr><td></td><td>:b_day</td><td>1997/11/20</td><td></td><td>:b_price_to</td><td>33000</td><td></td><td>:s_day_from</td><td>1997/11/20</td></tr><tr><td></td><td>:b_day_from</td><td>1997/11/14</td><td></td><td>:b_day</td><td>1997/11/20</td><td></td><td>:s_day_to</td><td>1997/12/31</td></tr><tr><td></td><td>:b_day_to</td><td>997/12/15</td><td></td><td>:b_day_from</td><td>1997/11/14</td><td></td><td>:s_preference</td><td>Price</td></tr><tr><td></td><td>:b_preference_1</td><td>Price</td><td></td><td>:b_day_to</td><td>1997/12/15</td><td></td><td>:s_notice</td><td>very nice view ) )</td></tr><tr><td></td><td>:b_preference_2</td><td>Traffic</td><td></td><td>:b_preference_1 Price</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>:b_preference_3</td><td>Region</td><td></td><td>:b_preference_2 Traffic</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>:b_preference_4</td><td>Environment ) )</td><td></td><td>:b_preference_3 Region</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>:b_preference_4 Environment ) )</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="3">(achieve</td><td colspan="3">(tell</td><td colspan="3">(reply</td></tr><tr><td>:sender</td><td colspan="2">SeoulBroker</td><td>:sender</td><td colspan="2">KangnamLocal</td><td>:sender</td><td colspan="2">SeoulBroker</td></tr><tr><td>:receiver</td><td colspan="2">KangnamLocal</td><td>:receiver</td><td colspan="2">SeoulBroker</td><td>:receiver</td><td colspan="2">KangdongLocal</td></tr><tr><td>:reply-with</td><td colspan="2">SeoulBroker1997110112100620</td><td>:in-reply-to</td><td colspan="2">SeoulBroker1997110112100620</td><td>:in-reply-to</td><td colspan="2">KangdongLocal19971101120520</td></tr><tr><td>:language</td><td colspan="2">pseudoKQML</td><td>:language</td><td colspan="2">pseudoKQML</td><td>:language</td><td colspan="2">pseudoKQML</td></tr><tr><td>:ontology</td><td colspan="2">real_estate</td><td>:ontology</td><td colspan="2">real_estate</td><td>:ontology</td><td colspan="2">real_estate</td></tr><tr><td>:content</td><td colspan="2">(lock_request</td><td>:content</td><td colspan="2">(lock_answer</td><td>:content</td><td colspan="2">(contract_candidate</td></tr><tr><td></td><td>:b_broker</td><td>SeoulBroker</td><td></td><td>:b_broker</td><td>SeoulBroker</td><td></td><td>:b_accepted_id</td><td>1001000001</td></tr><tr><td></td><td>:b_accepted_id</td><td>1001000001</td><td></td><td>:b_accepted_id</td><td>1001000001</td><td></td><td>:s_accepted_id</td><td>2002000011</td></tr><tr><td></td><td>:s_accepted_id</td><td>1002000011</td><td></td><td>:s_accepted_id</td><td>1002000011</td><td></td><td>:b2_accepted_id</td><td>3011000211</td></tr><tr><td></td><td>:s_lock</td><td>lock))</td><td></td><td>:s_lock</td><td>lock))</td><td></td><td>:b2_price</td><td>20000</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:b2_day</td><td>1997/11/31</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_region</td><td>Kyoungki</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_type</td><td>APT</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_size</td><td>22</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_build_day</td><td>1995</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_security</td><td>G</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_far_subway</td><td>10</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_far_bus</td><td>5</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_price</td><td>3200</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_day</td><td>1997/12/1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>:s_notice</td><td>a very nice view))</td></tr></table>

Fig. 5. Examples of messages in the system.

## 4.2.2. Local agents

The local agents communicate with the broker agent for buyer’s requirements or for bids from sellers. It consists of a communication module and an information processing module. The communication module has the same components as the broker agent except for the ANS. The informationprocessing module has two parts which are a database to manage the seller’s house and a buy and sell applet to communicate with the users. The local agent accesses the database using built-in functions for query processing in the information-processing engine. The local agent communicates with the user through the applets on the Web environment. The applets contain user requirements and the specifications of house to buy or sell.

## 4.3. Transaction flow by message-driÕen communication

In our system, agents exchange different types of messages in each step of the brokerage process. There are seven types of messages in the framework for dealing in real estate. The competition layer involves the messages: buy req <sub>– –</sub>, sell req, announcement and bid specification <sub>–</sub> . The constraint satisfaction layer involves the messages: lock re <sub>–</sub> - quest, lock answer <sub>– –</sub>and contract candidate. We briefly explain the functions of the messages here:

<sup>Ø</sup> buy req <sub>–</sub> : used when a buyer agent sends buying requirements for house to the broker agent;

<sup>Ø</sup> sell req<sub>–</sub> : used when a seller agent sends specifications for house to a local agent;.

<sup>Ø</sup> announcement: used when the broker agent announces a buy req <sub>–</sub> message to local agents;

![](/api/attachments/9J993Q8R/fulltext/images/8ec87497895755bdbe68e23d1bccc3928f63fdf903f593b29c146f8e0ce6cb64.jpg)  
Fig. 6. Transaction flow by message exchange.

<sup>Ø</sup> bid specification<sub>–</sub> : used when local agents show acceptable houses to the broker agent in response to the announcement;

<sup>Ø</sup> lock request<sub>–</sub> : used when the CSP solver requests the local agent not to offer the house to others;

<sup>Ø</sup> lock answer <sub>–</sub> : used when the local agent responds to the lock request<sub>–</sub> ; and

<sup>Ø</sup> contract candidate<sub>–</sub> : used when the broker agent proposes the contract to the buyer with the result of the CSP solver.

These messages are represented in the form of a KQML message 17 . KQML is one of the most<sup>w</sup> <sup>x</sup> general agent communication languages and has been widely used by researchers. We have also employed our own content language similar to KQML in terms of the specification, which is called pseudoKQML. The language has structures useful in representing and processing the query for the database. The example messages are shown in Fig. 5.

Even though the brokerage flow has different steps according to the kinds of transactions, we show the general case of the flow in Fig. 6.

## 5. Experimental results

We have implemented the agent-based brokerage system in applying CSP for dealing in real estate with JATLite v. 0.4 Beta 3 . JATLite is a set of Java<sup>w</sup> <sup>x</sup> packages that supports facilities to exchange KQML messages. It also provides basic communication tools and templates based on TCP<sup>r</sup>IP. We have also implemented the CSP solver in ILOG solver 4.1 for the Windows 95 platform. ILOG solver is a C <sup>q</sup> library, which includes the useful functions and classes for constraint programming.

![](/api/attachments/9J993Q8R/fulltext/images/a8f4ea8983bff4e7750e807d5d2aeef7d876401c6665ac95469eee54341d1236.jpg)  
Fig. 7. Example of a buying request form.

We have experimented and analyzed the results of brokerage for dealing in real estate using the CSP solver. We have evaluated the results of the CSP solver, which have satisfied various user’s preferences. At this point, the user’s preferences are focused on the buyer’s conditions for a house; i.e., when the buyer tries to buy a house, he considers these important factors: price, moving time, location of the house, traffic conditions and living conditions. We show the example of the buy and sell applet for a buying request form in Fig. 7. As shown in Fig. 7, a buyer writes his required conditions for a house in fields of the applet.

The CSP solver internally represents the buyer’s required conditions based on different types of constraints. For example, if a buyer wants to show the scope of values for the price of a house, he will write the conditions in two fields which are labeled ‘‘price from’’ meaning the available minimum price to Ž buy and ‘‘size to’’ meaning the available maximum. Ž price to buy in Fig. 7. A seller also writes the scope . of values for the price to sell, as does the buyer. Let us label the minimum price to buy $\ddot { } \stackrel { \cdot } { } \delta _ { \mathrm { p _ { \mathrm { m i n } } } } \stackrel { } { } \mathrm { , } $ and the maximum price to buy $\ddot { } \dot { } B _ { \mathrm { p _ { \mathrm { m a x } } } } \dag ,$ , respectively. And let us label the minimum price to sell $\cdots  S _ { \mathrm { p _ { \mathrm { m i n } } } }  , $ and the maximum price to sell $\mathbf { \ddot { \rho } } \otimes _ { \operatorname { p _ { m a x } } } , \mathbf { \vec { \rho } } ,$ , respectively. Then, we can represent the conditions of the two constraints as follows:

$$
B _ {\mathrm{p} _ {\min}} \leq B _ {\mathrm{p}} \leq B _ {\mathrm{p} _ {\max}},
$$

$$
S _ {\mathrm{p} _ {\min}} \leq S _ {\mathrm{p}} \leq S _ {\mathrm{p} _ {\max}}.
$$

As a result, these constraints are represented to the practical constraint as follows:

$$
B _ {\mathrm{p} _ {\max}} \geq S _ {\mathrm{p} _ {\min}}.
$$

The constraint is propagated by the CSP solver to remove inconsistency in the domain. We show the following ILOG expression to process the above constraint:

<sub>IlcPost</sub> <sub>Buyer</sub> <sub>i</sub> <sub>-</sub> <sub>Ž</sub> w x w x ) <sub>getMaxPriceŽ</sub> <sub>.</sub> )s <sub>Seller</sub> <sub>i</sub> <sub>-</sub>) getMinPrice . Ž . <sub>.</sub>

We have evaluated the results of the CSP solver. For the exact results of testing, we suppose that the sizes of houses are the same and the prices of houses depend on the sellers. We also suppose that all buyers can buy one of the houses but each buyer has different preferences for a house. We compared the results of the CSP solver with the results of the naive mechanism, which considered only price as the user’s preference. The result of testing CSP is shown in Table 2.

Table 2  
Results of applying CSP

<table><tr><td></td><td> $b_0$ </td><td> $b_1$ </td><td> $b_2$ </td><td> $b_3$ </td><td> $b_4$ </td><td> $b_5$ </td><td> $b_6$ </td><td> $b_7$ </td><td> $b_8$ </td><td> $b_9$ </td></tr><tr><td rowspan="2"> $h_0$ </td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td></tr><tr><td>98</td><td>88</td><td>90</td><td>50</td><td>45</td><td>75</td><td>70</td><td>65</td><td>75</td><td>75</td></tr><tr><td rowspan="2"> $h_1$ </td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td></tr><tr><td>95</td><td>85</td><td>91</td><td>53</td><td>60</td><td>75</td><td>65</td><td>63</td><td>80</td><td>80</td></tr><tr><td rowspan="2"> $h_2$ </td><td>152</td><td>152</td><td>152</td><td>152</td><td>152</td><td>152</td><td>152</td><td>152</td><td>152</td><td>152</td></tr><tr><td>93</td><td>80</td><td>95</td><td>65</td><td>80</td><td>82</td><td>80</td><td>70</td><td>78</td><td>79</td></tr><tr><td rowspan="2"> $h_3$ </td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td></tr><tr><td>90</td><td>90</td><td>91</td><td>71</td><td>75</td><td>80</td><td>77</td><td>70</td><td>75</td><td>88</td></tr><tr><td rowspan="2"> $h_4$ </td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td></tr><tr><td>86</td><td>70</td><td>85</td><td>67</td><td>77</td><td>68</td><td>65</td><td>90</td><td>68</td><td>90</td></tr><tr><td rowspan="2"> $h_5$ </td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td><td>160</td></tr><tr><td>87</td><td>82</td><td>85</td><td>80</td><td>58</td><td>65</td><td>65</td><td>74</td><td>69</td><td>95</td></tr><tr><td rowspan="2"> $h_6$ </td><td>162</td><td>162</td><td>162</td><td>162</td><td>162</td><td>162</td><td>162</td><td>162</td><td>162</td><td>162</td></tr><tr><td>85</td><td>75</td><td>82</td><td>80</td><td>70</td><td>85</td><td>82</td><td>82</td><td>65</td><td>92</td></tr><tr><td rowspan="2"> $h_7$ </td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td></tr><tr><td>81</td><td>75</td><td>80</td><td>85</td><td>86</td><td>79</td><td>79</td><td>82</td><td>65</td><td>86</td></tr><tr><td rowspan="2"> $h_8$ </td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td></tr><tr><td>80</td><td>82</td><td>80</td><td>70</td><td>85</td><td>75</td><td>88</td><td>75</td><td>60</td><td>85</td></tr><tr><td rowspan="2"> $h_9$ </td><td>190</td><td>190</td><td>190</td><td>190</td><td>190</td><td>190</td><td>190</td><td>190</td><td>190</td><td>190</td></tr><tr><td>60</td><td>55</td><td>50</td><td>72</td><td>95</td><td>50</td><td>52</td><td>60</td><td>48</td><td>69</td></tr></table>

As shown in Table 2, there are 10 houses offered by sellers and 10 buyers. Let us call the first buyer accepted by the CSP solver in the broker agent $\mathsf { b } _ { 0 } ,$ the second buyer $\mathbf { b } _ { 1 }$ , the ith buyer $\mathbf { b } _ { i }$ . Each buyer $\mathbf { b } _ { i }$ can buy one of 10 houses; $\mathbf { h } _ { 0 } , \mathbf { h } _ { 1 } , \ldots , \mathbf { h } _ { 9 }$ . In Table $^ { 2 , }$ each row represents a house, which has two different values for a buyer; the upper one represents the price and the lower one represents the result of the evaluation of matching a buyer and a seller in terms of the optimal function. The evaluation score for a specific house depends on the buyer’s preferences. For example, $\mathbf { h } _ { 0 }$ costs 150 million won and has 98 points for $\mathbf { b } _ { 0 } . \mathbf { h } _ { 0 }$ has 88 points for $\mathbf { b } _ { 1 }$ because $\boldsymbol { \mathbf { b } } _ { 0 }$ considers the price as the most important factor, whereas $\mathbf { b } _ { 1 }$ considers the traffic conditions as a more important factor than the price.

As shown in Table 2, the underlined numbers make two types of successful pairings between buyers and houses. For example, if the system processes the brokerage considering only price, then buyer ${ \sf b } _ { 8 }$ buys $\mathtt { h } _ { 8 }$ . If, however, the system processes the brokerage using the CSP solver with buyer’s preferences, ${ \sf b } _ { 8 }$ can buy $\mathbf { h } _ { 1 }$ . In the former case, the brokerage will easily fail in a real environment because of the higher price of $\mathbf { h } _ { 8 } .$ . In the latter case, the brokerage can be successful in a real environment because ${ \sf b } _ { 8 }$ has the highest score for $\mathbf { h } _ { 1 }$ when compared with the other houses. It means that ${ \sf b } _ { 8 }$ will be satisfied with $\mathbf { h } _ { 1 }$ in terms of preferential weights such as traffic conditions, moving time, location of the house and living conditions. Therefore, the system can make valid results of brokerage using the CSP solver.

## 6. Conclusion and further research

We have proposed a two-layered multi-agent framework for brokerage between buyers and sellers on EC. The brokerage process of the framework is divided into the competition layer and the constraint satisfaction layer for completion of the brokerage process. We have defined different agents to play roles instead of buyers, sellers and brokers. We have also defined the message-driven communication among the agents in the framework. For the brokerage between buyers and sellers, the constraint satisfaction process among the agents is necessary for user satisfaction in addition to the traditional competition process. We have implemented the constraint satisfaction process by applying CSP. The CSP solver can make an optimal solution for the brokerage by means of satisfying various preferences of the user. Finally, we have implemented the prototype system for dealing in real estate on EC using the proposed framework.

However, the proposed framework has obstacles that may arise when implemented in the real world. At first, the framework does not fully support the negotiation process between buyers and sellers. For the reliability of the brokerage, the buyer agent should negotiate with the seller agent on a one-to-one correspondence to establish the condition requirements after the CSP solver has produced the pairs of buyers and sellers. Now, we are developing the agents, which have more intelligent abilities for a one-to-one negotiation. Second, the broker agent of our system does not make a contract among participators and supports only the resulting group of acceptable candidates in order to make a contract. For implementation in the real environment, the framework should be extended to support the total contract process including authorization.

## 7. Uncited reference

<sup>w</sup> <sup>x</sup> <sub>13</sub>

## Acknowledgements

This work was supported by grant no. 981-0919- 101-2 from the Core Research program of the Korea Science and Engineering Foundation.

## References

<sup>w</sup> <sup>x</sup> 1 K. Baker, Introduction to Sequencing and Scheduling, Wiley, 1974.

<sup>w</sup> <sup>x</sup> 2 BargainFinder, http:<sup>rr</sup>bf.cstar.ac.com<sup>r</sup>bf<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 3 Center For Design Research, JATLite v. 0.4 Beta Release Note, http:<sup>rr</sup>java.stanford.edu<sup>r</sup>java agent <sub>–</sub> <sup>r</sup>html<sup>r</sup>JATLiteBeta.html.

<sup>w</sup> <sup>x</sup> 4 A. Chavez, P. Maes, Kasbah: an agent marketplace for buying and selling goods, in: Proceedings of the First International Conference on the Practical Application of Intelligent Agents and Multi-Agent Technology, London, UK, 1996.

<sup>w</sup> <sup>x</sup> 5 P. Cohen, A. Cheyer, M. Wang, S. Baeg, An open agent architecture, in: Working Notes of AAAI Spring Symposium on Software Agents, 1994.

<sup>w</sup> <sup>x</sup> 6 R.B. Doorenbos, O. Etzioni, D.S. Weld, A scalable comparison — shopping agent for the World-Wide Web, in: 1st International Conference on Autonomous Agent,1997.

<sup>w</sup> <sup>x</sup> 7 P.V. Hentenryck, in: Constraint Satisfaction in Logic Programming, The MIT Press, 1989.

<sup>w</sup> <sup>x</sup> 8 Informaster, http:<sup>rr</sup>informaster.stanford.edu:4000<sup>r</sup>ASK<sup>r</sup> RENTAL.

<sup>w</sup> <sup>x</sup> 9 N.R. Jennings, N.R. Pople, Design and implementation of ARCHON’s coordination module, in: Proceedings of the Workshop on Cooperating Knowledge-Based Systems, Keele, UK, 1992.

<sup>w</sup> <sup>x</sup> 10 G.S. Jo, K. McAloon, Anticipatory pruning networks and forward checking in CLP over continuous domains, Decision Support Systems 18 1996 327–340.Ž .

<sup>w</sup> <sup>x</sup> 11 J.K. Lee, W. Lee, Intelligent agent-based contract process in electronic commerce: UNIK-AGENT approach, in: Proceedings of the 30th Hawaii International Conference on System Science, 1997, pp. 230–241.

<sup>w</sup> <sup>x</sup> 12 J.K. Lee, W. Lee, An intelligent agent-based competitive contract process: UNIK-AGENT, International Journal of Intelligent System in Accounting, Finance and Management 7 1998 91–105.Ž .

<sup>w</sup> <sup>x</sup> 13 P. Maes, Agents that reduced work and information overload, Communications of the ACM 37 7 1994 July. Ž . Ž .

14 R. Mohr, T. Henderson, Arc and path consistency revisited, Artificial Intelligence 28 1986 .Ž .

<sup>w</sup> <sup>x</sup> 15 T. Sandholm, V. Lesser, Issues in automated negotiation and electronic commerce: extending the contract net framework, ICMAS-95 1995 .Ž .

<sup>w</sup> <sup>x</sup> 16 R.G. Smith, The contract net protocol: high-level communication and control in a distributed problem solver, IEEE Transactions on Computers C 29 12 1980 1104–1113,Ž . Ž . December.

<sup>w</sup> <sup>x</sup> 17 The ARPA knowledge sharing initiative external interfaces working group, Draft specification of the KQML agent communication language plus example agent polices and language, Technical Report of ARPA Knowledge Sharing Effort Group, June 15, 1993.

Jong-Jin Jung received his BS degree from the Department of Computer Science, Inha University in 1992, and his MS degree from the Department of Computer Science, Inha University in 1995. He is currently a PhD student in the Department of Computer Science and Engineering, Inha University in Inchon, Korea. His research interests include intelligent scheduling, intelligent agent, and electronic commerce.

Geun-Sik Jo received his BS degree in Computer Science, Inha University in 1982, his MS in Computer Science from Queens College<sup>r</sup>CUNY in 1985, and his PhD in Computer Science from the City University of New York in 1991. He is currently Associate Professor in the Department of Computer Science and Engineering, Inha University, Korea. His research interests include CLP languages, intelligent scheduling, and expert systems.
