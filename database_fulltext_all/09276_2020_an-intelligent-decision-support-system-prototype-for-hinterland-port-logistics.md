---
otero_id: 9276
otero_key: "XGAYJ2WV"
title: "An intelligent decision support system prototype for hinterland port logistics"
authors: "Elnaz Irannezhad; Carlo G. Prato; Mark Hickman"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113227"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

An intelligent decision support system prototype for hinterland port logistics

Decision Support Systems

Elnaz Irannezhad, Carlo G. Prato, Mark Hickman

![](/api/attachments/XGAYJ2WV/fulltext/images/1e85ea8c655b1bbbc7b848673330cde8bfeb1257d82d6a7abf664543dcac7031.jpg)

PII: S0167-9236(19)30256-8

DOI: https://doi.org/10.1016/j.dss.2019.113227

Reference: DECSUP 113227

To appear in: Decision Support Systems

Received date: 13 May 2019

Revised date: 26 November 2019

Accepted date: 26 November 2019

Please cite this article as: E. Irannezhad, C.G. Prato and M. Hickman, An intelligent decision support system prototype for hinterland port logistics, Decision Support Systems (2018), https://doi.org/10.1016/j.dss.2019.113227

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2018 Published by Elsevier.

# An intelligent decision support system prototype for hinterland port logistics

Elnaz Irannezhad<sup>a\*</sup>, Carlo G. Prato<sup>b</sup>, Mark Hickman<sup>b</sup>

<sup>a</sup> Australian Institute of Business and Economics, University of Queensland, Australia

<sup>b</sup> School of Civil Engineering, University of Queensland, Australia

\*Corresponding author: e.irannezhad@uq.edu.au, Australian Institute of Business and Economics, University of Queensland, Brisbane, QLD, Postcode 4072, Australia, Tel: (+61)432 712 822.

Declarations of interest: none

# An intelligent decision support system prototype for hinterland port logistics

## ABSTRACT

Port logistics is characterised by a high degree of fragmentation, uncertainty and complexity. In a context with these characteristics, decision support can be of significant value. This study presents the prototype of an intelligent decision support system (DSS) that leads to horizontal and vertical cooperation among freight agents involved in port logistics. A multi-agent simulation model is presented where heterogeneous actions are enabled as a result of an adaptive reinforcement learning algorithm that is inspired by human decision-making strategies. The model combines optimisation modelling and decision theory to operate in a dynamic environment characterised by information asymmetry among agents and dynamic changes over time. A simulation demonstrates the dynamics and convergence to equilibrium of the interactions of heterogeneous agents for delivery and pick up of import/export shipments.

In particular, we answer two specific research questions. What is the likely impact of an intelligent DSS in hinterland container transport as a value-added service of port community system (PCS)? How can an optimum cooperative strategy be formulated to meet the dynamic demand and supply of freight agents in hinterland container transport and achieve agility in the age of hyper-competition?

By addressing these two research questions we make a specific contribution by developing an agent-based simulation model in a real-world and large-scale case study, by using a reinforcement learning model based on probability matching theory that allows simulating realistically the adaptive behaviour of agents. The results of the simulation of two weeks of container movements indicate huge savings in total transport costs and distance travelled as well as higher utilisation of trucks from the sharing of resources. Moreover, we show that it is strictly better for smaller freight agents to cooperate – a conclusion generated endogenously inside the model as a trade-off between exploration and exploitation. As a result of this prototype simulation, major freight agents will not necessarily benefit from the DSS mainly because they are already using the economies of scale.

KEYWORDS: agent-based model; port community system; vehicle routing problem; reinforcement learning; freight transportation.

## 1. Introduction

Fragmentation in port-land operations and between hinterland logistics operators brings about extra trips, higher logistics costs, longer delays, and customer dissatisfaction. One consequence of this fragmentation is that logistics operators seek to ‘do their own thing’ in terms of planning and timetabling their operations, with little interest or ability to interact with their competitors. Given the numerous actors involved in joint logistics operations in import/export trade, an integrated and coordinated logistics system helps in managing interdependencies among activities. Several studies and successful empirical cases showed that inter-firm coordination brings about significant benefits across the supply chain [1-6]. As the primary interface in the import/export industry, ports can play an important role to reduce the inefficiencies in supply chains by providing a concerted and coordinated logistics solution, affecting positively the end-users, and thus having a direct influence on the wider economy [7].

The solution consists in information sharing that can be provided via an online system called J “Business Intelligence”, supported by a port authority where information becomes available to freight actors in a multi-level system. Business Intelligence is defined as an instrument to provide enterprise operations view and achieves competitive advantage by making the right decisions at the right time as one of its elements, the so-called Decision Support System (DSS). In the context of this study, the Business Intelligence is referred to as a Port Community System (PCS), with examples such as Virtuele Haven in the Port of Rotterdam, DIVA in the Port of Hamburg, CCS Dakosy in the Port of Antwerp, and Portnet Trade Exchange in the Port of Singapore.

PCS applications have evolved in recent years from serving as an information hub [8] to DSS, generating value-added logistics solutions while the main objective remains encouraging horizontal and vertical cooperation among freight agents [9]. According to the European Commission [10], horizontal cooperation is defined as the concerted practice between agents at the same level, while vertical cooperation is a form of integration between parties across the logistics chain. In the context of maritime and hinterland container transportation, horizontal cooperation enhances the service quality of shipping lines and carriers by increasing the geographic span of services while maintaining optimum resources, and vertical cooperation provides well-integrated transport and logistics services across the supply chain.

The freight agents’ decision on cooperation depends on gains resulted from economies of scale and scope in a dynamic market. Major freight agents (e.g., shippers or carriers) should see the benefit of horizontal cooperation with smaller agents or their large competitors, without losing their market position.

The main body of the PCS literature looks at optimizing the flow of information and customs activities [7, 11, 12], mainly because port and customs-related document submissions are the most important reasons for users to adopt a PCS [13], and are most likely considered as the early steps of PCS implementation. However, little documented proof of concept exists with regards to the role of DSS as one of the features of PCS.

Most existing studies investigating PCS either adopted a descriptive approach [14, 15] or defined indicators to evaluate the PCS efficiency [16, 17]. Other studies quantified the PCS multiple features by adopting a multiple-criteria decision making method [18]. Recently, Aydogdu and Aksoy [19] estimated the time savings of various administrative processes after adopting a PCS, based on the average and the maximum time that were provided by various agents in the status quo. Even more recently, Carlan, Sys and Vanelslander [9] conducted a review of PCS cost-benefit studies and proposed a framework for further analysis.

## Journal Pre-proof

Value-added services of PCS are considered as co-innovation, namely a new form of innovation where several stakeholders participate together to create new knowledge, insight and opportunities for cooperation [20]. Co-innovation enables digital tools to tackle supply chain inefficiencies and provide connectivity, collaboration, and integration among actors. The role of such initiatives becomes vital particularly for competing ports located in close geographical markets such as North Western ports [9]. In fact, improving the hinterland transport is essential when considering that it can account for up to 80% of the total freight transport cost, despite being the shorter distance segment of freight trips [21]. Accordingly, improving hinterland transport is essential for distant ports competing for business in overlapping hinterlands [22]. Notably, quantitative studies on the hinterland cooperation are scarce [23], and given that the hinterland transport costs are generally higher than the maritime costs, not to mention externalities such as road congestion, atmospheric pollution, and road safety risks [24, 25], there is a need to study the benefits of implementing an intelligent DSS in this use case.

With the objective of filling the aforementioned gaps, this research aims to quantify the likely impacts of an intelligent DSS implemented by PCS on a real size hinterland container transport network. We focus on two salient questions:

i. What is the likely impact of an intelligent DSS in hinterland container transport as a value-added service of PCS?

ii. How can an optimum cooperative strategy be formulated to meet the dynamic demand and supply of freight agents in hinterland container transport and achieve agility in the age of hyper-competition?

To address these two questions, a multi-agent system is simulated where freight agents experience logistics outcomes from the PCS, earn their gains and losses from the past experience via a reinforcement learning method, and then decide whether to use the PCS service or not.

Given the dynamic nature of the transport market, agent-based models have an advantage over purely optimisation models to understand why certain behaviours might evolve and persist through repeated local interactions of autonomous agents. Agent-based models are widely applied in integrating business information systems with coordinating behaviour of a collection of autonomous intelligent agents [26]. The adequacy of agent-based models, particularly under uncertainty, comes from the fact that individuals and economic agents use rules of thumb rather than strict maximisation. These rules of thumb are learnt through reinforcement, continuing if they have been profitable and abandoning otherwise [27, 28]. Accordingly, this modelling technique can capture the explicit decision making of various agents in a dynamic environment by representing their resource management and time constraints and capturing their reaction to policies.

This study contributes to the PCS literature by applying an agent-based simulation model that uses a linear reinforcement learning (RL) algorithm based on probability matching theory in order to simulate the adaptive behaviour of freight agents to experience the benefits and costs of cooperation through a PCS prototype. In this study we consider two main RL strategies: (i) agents diversify in their first few choices and gradually converge to a single preferred option; (ii) freight agents learn the probabilities of different outcomes and then are more likely to adopt in the future actions that were more successful in the past. In this latter approach, agents predict their future reward in a multi-step task while learning from their previous experiences. The assumption is that the agents’ beliefs change according to the accumulated knowledge based on their previous experiences of gains and losses. The result of individuals’ decisions implies dynamism in the market and payoff variability. Accordingly, the decision of freight agents to use a PCS is determined based on the probability of saving in the logistics costs in past experiences on a similar day with similar shipment characteristics.

The remainder of the paper is organised as follows. Section 2 presents the research background and model rationale. Section 3 presents data and methodology of this study, with emphasis on model formulation and specification. Section 4 shows the results of the model simulation. Finally, Section 5 draws conclusions from this study and provides managerial implications and ideas for future studies.

## 2. Literature review and research background

Agent-based models have been adopted in several domains, such as the interactions of economic agents in financial markets [29-32], supply chain management [33-35], fleet management for both scheduling [36] and dispatching [37], terminal management [38], and intermodal transportation [39, 40]. For freight transport systems, this approach seems very suitable to illustrate competition and interaction among various agents. INTERLOG [41], FREMIS [42], and TAPAS-Z [43] are examples of agent-based freight transport models at the regional level.

In addition to simulating the current situation, agent-based models can be applied to examine various policies by changing the environment and observing how agents would learn and behave in the new environment. For example, Taniguchi, Yamada and Okamoto [44] developed a multiagent-based model (including shippers, carriers, and administrators) on a small test network to study the effects of road pricing on shippers’ and carriers’ strategies. Abdul-Mageed [45] examined a coordinated truck assignment system for five trucking companies, comparing direct competition with cooperation by sharing vehicles. Results showed that the coordinated assignment system improved the transport process in terms of decreasing the number of empty trips and the number of late arrivals.

The aforementioned literature on agent-based modelling either assume a set of if-then rules (so-called belief-based models) or a probabilistic RL method to model agents’ behaviour (socalled reinforcement-based models). Experiments in cognitive decision making show that decision makers have a toolbox of heuristics specific to each environment, and a learning rule may arise from simple heuristics where the choice probability changes as a function of the encountered instances and the payoff variability [46].

RL is a model of learning that captures these heuristics and has been found to be one of the main driving forces of human behaviour in iterative decision problems where the probabilities of “success” or “gain” are unknown to the decision maker [27, 34]. Experiments confirm that the percentage of adaptive behaviours is much higher than that of analytical behaviours (utility maximisers, loss avoiders or asset conservers) [47]. Specifically, probability matching is reported in experimental economics as an innate human heuristic whereby, if a strategy leads to a desirable outcome, the probability that it is used again increases, while an undesired outcome has the environments where the payoff of the unchosen action is observed by an individual under RL, the probability of choosing an option converges to the probability of that option being the best alternative.

However, learning does not necessarily lead to the maximisation of gains for all agents and, particularly with the increase in payoff variability, choice behaviour tends to random decisions [51]. Even though optimal behaviour clearly suggests that agents should follow a rational rule of “assess the chance of success of each action and choose the most likely one”, experimental results show that they diversify their choices. For example, Rubinstein and Tversky [52] observed in an experiment that individuals employed rules to play a game while also diversified the rules they used during a sequence of games. Later on, Rubinstein [48] reported the results of multiple decision problems in a fixed set of alternatives. In these experiments, although the best strategy was choosing the action that is most likely to achieve success, individuals diversified their choices. Moreover, diversification was stronger when faced with an uncertain situation where there was no explicit information about the chances of success, but weaker for real-life actions where individuals were aware of the action probabilities. Diversification can be explained as an instinct to seek information and learn about the environment. Accordingly, the RL implies the diversification in decision making by introducing a random decision under the probability concept. In the context of this study, as a higher number of freight agents use the PCS, more resources, bundling and back-loading opportunities become available for all users and there would be more savings in the logistics cost. On the other hand, with the withdrawal of some big agents from the system, the payoff for the other agents would be less than expected.

## 3. Methods

## 3.1. Dataset and variables

The case study focuses on container shipments passing through the Port of Brisbane (Australia). The dataset was provided by the Import/Export Logistics Chain Study by the Port of Brisbane Pty Ltd [53] and included two weeks of individual movements of full and empty containers in import and export chains (23,833 records). The details of the movements include identification numbers, timestamps of arrival and departure, postcodes and types of origin and destination, weight of the shipment and size of the container. Detailed variable definitions for the proposed agent-based model are provided in Table 1.

## Table 1

Notation.

<table><tr><td></td><td>Variable</td><td>Description</td></tr><tr><td rowspan="5">Sets</td><td>A</td><td>Set of actions  $a$ , where  $A = \{a_1: \text{maintaining the status quo}; a_2: \text{signing up for an individual optimum delivery/pickup plan}; a_3: \text{signing up for a cooperative optimum delivery/pickup plan}\}$ </td></tr><tr><td>E</td><td>Set of learning episodes  $e$ , where  $E = \{0,1,...,e,...,e_{max}\}$  (assuming  $e_{max} = 100$ )</td></tr><tr><td>K</td><td>Set of vehicles  $k$ , where  $K = \{1,2,...,k,...\}$  ( $k$  is either a semitrailer or a B-double trailer)</td></tr><tr><td>L</td><td>Set of time-varying links, where four time-dependent travel times (AM peak, noon, PM peak, night) are associated with each link</td></tr><tr><td>N $N_0$ </td><td>Set of nodes on the service network of import/export agentsSet of nodes and the port (as the depot of transport operators and stevedores),  $N_0 = N \cup [54]$ </td></tr><tr><td rowspan="2"></td><td>S</td><td>Set of states  $s_e$ , where  $S = \{s_{e,1},...,s_{e,14}\}$  (14 days planning horizon in each learning episode e)</td></tr><tr><td> $O_{ans(e)}$ </td><td>Set of orders of agent n choosing action a in state  $s_e$  for learning episode e, which is a set of pickup  $p_j$  and delivery  $d_j$  of node j on the service network of agent n</td></tr><tr><td rowspan="13">Parameters</td><td> $[t_{1i},t_{2i}]$ </td><td>Time-window constraint of node i</td></tr><tr><td> $[t_{1k},t_{2k}]$ </td><td>Time-window constraint of vehicle k</td></tr><tr><td> $c_{ijk}$ </td><td>Operational costs of vehicle k for a trip between nodes i and j, consisting of the cost associated with the waiting, service, and travel time</td></tr><tr><td> $C_{ans(e)}$ </td><td>Total operational costs of agent n for taking action a in the state  $s_e$  in learning episode e which is the summation of calculated operational cost  $c_{ijk}$  for all of its shipments</td></tr><tr><td> $d_j$ </td><td>Delivery of node j (two-dimensional “weight, TEU”)</td></tr><tr><td> $f_k$ </td><td>Fixed costs of vehicle k</td></tr><tr><td> $p_j$ </td><td>Pickup of node j (two-dimensional “weight, TEU”)</td></tr><tr><td> $q_k$ </td><td>Capacity of vehicle k (two-dimensional “weight, TEU”)</td></tr><tr><td> $t_{ijk}$ </td><td>Travel time of vehicle k between nodes i and j</td></tr><tr><td> $t_{ik}$ </td><td>Arrival time of vehicle k to node i</td></tr><tr><td> $h_{ik}$ </td><td>Service time node i by vehicle k, which is proportional to deliver/pick-up loads</td></tr><tr><td> $W_{max}$ </td><td>Number of vehicles that can be serviced simultaneously by stevedores at wharf</td></tr><tr><td>α</td><td>Learning speed</td></tr><tr><td rowspan="2"></td><td> $\pi_{ans(e)}$ </td><td>Payoff of action a by agent n in state  $s_e$  for learning episode e</td></tr><tr><td> $P_{an(e)}$ </td><td>Set of probability of taking action a by agent n for learning episode e</td></tr><tr><td rowspan="3">Decision variables</td><td> $x_{ijk}$ </td><td>{1: if vehicle k travels directly from node i to node j; 0: otherwise}</td></tr><tr><td> $y_{ijk}$ </td><td>Total pick-up load by vehicle k while travelling between nodes i and j</td></tr><tr><td> $z_{ijk}$ </td><td>Total delivery load by vehicle k while travelling between nodes i and j</td></tr></table>

## 3.2. Multi-agent simulation model

A simulation experiment was designed to represent the real-world system and understand the decision strategies by autonomous freight agents affected by the PCS. In our model, agents have different states and have a utility function that quantifies their degree of preference across alternatives. Also, each agent learns independently and needs to update the expected value after receiving the payoff from an action. These agents are called self-interested and distributed agents [55]. The agents in the proposed model consist of importers, exporters, transport operators, container terminals and stevedores at the wharf. We assume there exist several activity nodes (stops) on the importer and exporter service network for loading, unloading, and storage. These nodes consist of the origin/destination nodes and intermediate nodes (e.g. distribution centres, container parks, and transport yards). Accordingly, we define nodes as the physical entities of the agents’ supply chain, which are not necessarily exclusive to one agent. The model layout is presented in Table 2. The states consist of shipments to be delivered daily over a planning horizon of 14 days.

The environment consists of a physical road network that considers time-dependent travel times and presents a limitation in that only 49% of the links allow B-doubles to operate. In some cases, this means that the trailer of a B-double has to be detached at a designated location and then moved separately. Accordingly, travel time and distance on links that do not allow B-double trailers are represented by three values to capture this real-world behaviour.

The environment is dynamic where it is unclear for every agent what other agents will do. Thus, agents are allowed to learn and choose the best possible action through an RL method in a dynamic environment. This scenario implies that using the PCS service is optional for users and, accordingly, an optimal solution is provided only for those who signed up. Thus, as more agents use the PCS, more resources, back-loading and shipment bundling opportunities become available for all users, and there will be more savings in terms of logistics costs. On the other hand, with the withdrawal of some big agents from the PCS, the payoff for the other agents will be lower than expected.

## Table 2

Model layout.

<table><tr><td></td><td>Description</td></tr><tr><td>Agents</td><td>Stevedores (working 24/7, located at the wharf)Container terminals (available time windows and geographic locations)Importers/exporters (available time windows and geographic locations)Transport operators (unlimited number of vehicles)</td></tr><tr><td>States</td><td>Shipments to be delivered daily in the planning horizon of 14 days</td></tr><tr><td>Actions</td><td> $a_1$ : Maintaining the status quo $a_2$ : Signing up for an individual optimum delivery/pickup plan $a_3$ : Signing up for a cooperative optimum delivery/pickup plan (shipment bundling where each agent pay the partial transport cost of a tour instead of a two-way trip)</td></tr><tr><td>Payoff</td><td>Saving in hinterland transport cost of shipment delivery/pickup</td></tr><tr><td>Environments</td><td>Physical road network with time-dependent travel timesTwo vehicle types, namely semi-trailers and B-double trailers, with different</td></tr></table>

Accordingly, agents learn through the following RL method, presented in Fig. 1 and Fig. 2. Consider an agent that, at every learning episode e, can choose to use the PCS to either shift the deliveries to off-peak period or bundle shipments with other agents. The payoff $\pi _ { a n s ( e ) }$ of agent n from learning episode e depends on action a taken in the state $s _ { e }$ and on the other agents’ actions, which are unknown. With providing the centralised decision support tool in the PCS, agents can be coordinated and provided benefit from a more efficient delivery plan in both actions $a _ { 2 }$ and $a _ { 3 }$ . It should be noted that the number of learning episodes determines the long-term decisions whereas states represent the dynamic of the market regarding the varying number of shipments in different days. In this setting, it is assumed that the action in every learning episode e is consistent across all 14 states $s _ { e } ,$ representing two weeks of delivery plan. However, in every learning episode e, agents try different actions while progressively seeking the higher payoff based on their accumulated experience in the previous learning episodes.

![](/api/attachments/XGAYJ2WV/fulltext/images/605514eb80ecc7f2f3dcc1da3e1887494fb10c432a63452edc4bf02ffdcf976a.jpg)

## Fig. 1. Decision support system structure.

The payoff $\pi _ { a n s ( e ) }$ of agent n in the state $s _ { e }$ of the learning episode e is the percentage savings in transport costs as a result of action a compared to the status quo (as the benchmark). The calculation of transport costs considers time-based and distance-based operational costs $c _ { i j k }$ as well as the fixed cost $f _ { k }$ of vehicles. The rental cost of vehicles per time unit was assumed as the fixed cost of the vehicle, and the working rate of drivers for a time unit and fuel price for a distance unit were considered respectively as the time-based and the distance-based costs. The payoff $\pi _ { a n s ( I ) }$ in the initial step is calculated on the basis of choosing a random action. In the following learning steps (up to $e _ { m a x } )$ , we assume that agents adopt a learning rule suggested by Rivas [50] which is a generalisation of linear RL pioneered by the psychologists Bush and Mosteller [56]. Let $P _ { a n ( e ) }$ be the probability with which agent n takes action a in learning episode e. Then, the learning rule for agent n at the next learning episode (e+1) is given by the probability $P _ { a n ( e + I ) }$ in eq. (1), where α is the learning speed $( 0 \leq \alpha \leq 1 )$ and $a r g m a x _ { a } ( \sum _ { s ( e ) } \pi _ { a n s } )$ is the highest payoff among all the three actions in set A. An optimal policy (i.e., action a) for agent n is determined by the argument argmax $_ { a } ( \sum _ { s ( e ) } \ \pi _ { a n s ( e ) } )$ which maximises the accumulated payoff function $\pi _ { a n s ( e ) }$ for all states $s _ { e } \in S .$

$$
P _ {a n (e + 1)} = \left\{ \begin{array}{l l} P _ {a n (e)} + \alpha \left(1 - P _ {a n (e)}\right) \frac {e ^ {\arg \max _ {a} \left(\sum_ {s _ {e} \in S} \pi_ {a n s (e)}\right)}}{\sum_ {a \in A} e ^ {\sum_ {s _ {e} \in S} \pi_ {a n s (e)}}} & \text {if} \sum_ {s _ {e} \in S} \pi_ {a n s (e)} = \operatorname{argmax} _ {a} \left(\sum_ {s _ {e} \in S} \pi_ {a n s (e)}\right), a \in A \\ P _ {a n (e)} - \alpha P _ {a n (e)} \frac {e ^ {\arg \max _ {a} \left(\sum_ {s _ {e} \in S} \pi_ {a n s (e)}\right)}}{\sum_ {a \in A} e ^ {\sum_ {s _ {e} \in S} \pi_ {a n s (e)}}} & \text {otherwise} \end{array} \right.\tag{1}
$$

The decision support tool provided by the PCS entails coordination and alignment between the agents with the aim of minimising the total logistics costs. The total logistics costs and optimum fleet are realised by solving an optimisation problem at every state $s _ { e }$ and learning episode e that allows approximating the optimal global policy. For the next learning episode (e+1), the action a for agent n is derived according to the probability $P _ { a n ( e + I ) } .$ . According to the action, the order list of each agent $O _ { a n s ( e + I ) }$ will be updated. The order list includes the set of pickup $p _ { j }$ and delivery d<sub>j</sub> on the service network of agent n and their associated time windows $[ t _ { I j } , t _ { 2 j } ]$ . It should be noted that each individual agent may have multiple orders to be either delivered or picked up from various locations. Also, the time windows change according to the action: for example, if agent n chooses action type $a _ { 2 }$ (i.e. individual optimum plan) the time windows constraints will be softer. The input of the optimisation model include: (i) two aggregated sets of orders $\sum _ { n } O _ { a n s ( e ) }$ for two types of actions $( \mathrm { i } . { \mathsf { e } } . , a _ { 2 }$ and $a _ { 3 } ) ;$ (ii) vehicle list of two types, with their associated cost attributes including fixed cost $f _ { k } ,$ , time-based and distance-based costs, two-dimensional capacity $q _ { k } ,$ and time windows $[ t _ { I k } , t _ { 2 k } ]$ of operation; (iii) service time $h _ { i k }$ that is proportional to the delivery/pick up load and type of vehicle; and (iv) the maximum number $W _ { m a x }$ of vehicles that can be serviced $e ,$ the optimisation problem is solved separately for two aggregated sets of orders where only orders of the cooperative agents can be bundled together.

For the optimisation, we used a dynamic vehicle allocation and routing problem in a timevarying network with time-window (DVCRPTW) constraints, two-dimensional capacity, and simultaneous pickup and delivery. Accordingly, the DCVRPTW determines the minimum total travel impedance while also selecting the minimum number of vehicles of the two types necessary to serve a set of pickup/delivery demands, while also considering the capacity constraints of vehicles and the demand and time windows of the orders. It should be noted that both capacity and demand in our case-study have two dimensions (weight and size), and both dimensions of demand should meet the two capacity constraints. The dynamics of this problem is incorporated by considering time-of-day travel times in the road network, time-of-day constraints on the use of some road segments by larger trucks, and constraints on the time-dependent service rate at the stevedores. The optimisation model is formulated as follows:

$$
\operatorname{Min} \left(\sum_ {k \in K} \sum_ {j \in N} f _ {k} x _ {0 j k} + \sum_ {k \in K} \sum_ {i \in N _ {0}} \sum_ {j \in N _ {0}} c _ {i j k} x _ {i j k}\right)\tag{2}
$$

Subject to:

$$
\sum_ {k \in K} \sum_ {j \in N _ {0}} x _ {i j k} = 1 \quad \forall i \in N\tag{3}
$$

$$
\sum_ {i \in N _ {0}} \sum_ {k \in K} y _ {j i k} - \sum_ {i \in N _ {0}} \sum_ {k \in K} y _ {i j k} = p _ {j} \quad \forall j \in N\tag{4}
$$

$$
\sum_ {i \in N _ {0}} \sum_ {k \in K} z _ {i j k} - \sum_ {i \in N _ {0}} \sum_ {k \in K} z _ {j i k} = d _ {j} \quad \forall j \in N\tag{5}
$$

$$
y _ {i j k} + z _ {i j k} \leq q _ {k} x _ {i j k} \quad \forall i \in N _ {0}, \forall j \in N _ {0}, \forall k \in K\tag{6}
$$

$$
\sum_ {i \in N} \sum_ {k \in K} y _ {i 0 k} = \sum_ {i \in N} p _ {i}\tag{7}
$$

$$
\sum_ {i \in N} \sum_ {k \in K} z _ {0 i k} = \sum_ {i \in N} d _ {i}\tag{8}
$$

$$
\sum_ {j \in N} x _ {0 j k} = 1 \quad \forall k \in K\tag{9}
$$

$$
\sum_ {i \in N} x _ {i 0 k} = 1 \quad \forall k \in K\tag{10}
$$

$$
\sum_ {i \in N _ {0}} x _ {i h k} - \sum_ {j \in N _ {0}} x _ {h j k} = 0 \quad \forall k \in K, \forall h \in N\tag{11}
$$

$$
t _ {1 i} \leq t _ {i k} \leq t _ {2 i} \quad \forall i \in N, \forall k \in K\tag{12}
$$

$$
t _ {1 k} \leq h _ {i k} + \sum_ {i \in N _ {0}} \sum_ {j \in N _ {0}} x _ {i j k} t _ {i j k} \leq t _ {2 k} \quad \forall i \in N, \forall k \in K\tag{13}
$$

$$
t _ {i k} + h _ {i k} + t _ {i j k} - M \left(1 - x _ {i j k}\right) \leq t _ {j k} \quad \forall i, j \in N, \forall k \in K\tag{14}
$$

$$
\sum_ {k \in K} \sum_ {j \in N} x _ {0 j k} \leq W _ {\max}\tag{15}
$$

$$
x _ {i j k} \in \{0, 1 \} \quad \forall i, j \in N _ {0}, \forall k \in K\tag{16}
$$

$$
y _ {i j k}, z _ {i j k}, t _ {i k} \geq 0 \quad \forall i, j \in N _ {0}, \forall k \in K
$$

## (17)

The objective function in eq. (2) minimises the fixed and operational costs of vehicles. The constraint in eq. (3) imposes that, in a given time horizon, all customers are visited only once. The constraints in eqs. (4-5) imply the flow equations for pick-up and delivery. Eq. (6) is a capacity constraint, and as aforementioned the capacity and demand in this study have two dimensions (weight and number of TEUs) that should be both matched to the demand and service supplied. The constraints in eqs. (7-8) guarantee that the sum of the inflow to the depot equals the total pickup and delivery, respectively. The depot of the fleet (the port) is at the source node 0, so the constraints in eqs. (9-10) force all vehicles to leave the depot and return to the depot, respectively. The constraint in eq. (11) forces each customer is visited and left by the same vehicle.

The constraints in eqs. (12-13) specify the time window limitations of customers and vehicle drivers, respectively. Given the operating hours of the wharf at the port (24/7 in our case), we only impose the time-window constraint on vehicles and customers. Accordingly, some vehicles are assumed to work only during the night shift, and others to work only during the day shift. The constraints in eq. (14) implies that a vehicle k cannot arrive at the next customer before the minimum duration, which is the summation of arrival time and service time of the first customer and travel time between two consecutive customers. Also, the stevedores at the wharf have a limited service rate $W _ { m a x }$ where only a limited number of vehicles can be serviced simultaneously, and the constraints in eq. (15) represent this service rate (obtained from the observations of a typical day). Finally, the constraints in eqs. (16-17) represent the nature of decision variables.

Simulation algorithm: Pseudocode

1. e←1; initial learning step(episode)

2. For every agent choose a random action from $A { = } \{ a _ { I } , a _ { 2 } , a _ { 3 } \}$

3. Initialise the stevedores’ specifications; {location, working hours, hourly service rate}

4. Initialize Vehicle list K; {a set of two-dimensional capacity “weight, $T E U ^ { \mathrm { s } }$ , with timewindows specifications $[ t _ { I k } , \ t _ { 2 k } ]$ , and cost attributes (including fixed cost, time-based cost, distance-based cost)}

5. Initialise time-varying network of N nodes and L links; {a vector of time-dependent travel times of each link L for each of four time periods for weekdays and weekends (AM peak, noon, PM peak, night)}

## 6. For each state $s _ { e } \in S$

 Initialize two aggregated order lists $[ \sum _ { n } O _ { a n s ( e ) } ]$ for $a \ \epsilon \ \{ a _ { 2 } , a _ { 3 } \}$ ; {a set of twodimensional demands “weight, $T E U ^ { \mathrm { { , } } }$ with time-windows specification of nodes $\left[ t _ { I i } , t _ { 2 i } \right]$ , and pickup/delivery geographic locations along the network}

 Solve DCVRPTW for each of two Order lists $[ \sum _ { n } O _ { a n s ( e ) } ]$ for $a \in \{ a _ { 2 } , a _ { 3 } \}$ (Tabu Search algorithm): while not termination do (where termination is to service all orders satisfying all constraints)

Set the constraints of time-windows of orders, the capacity of vehicles, network constraints on B-doubles, sequence of orders, max operating hours of vehicles, and service rate of stevedores

Generate the shortest-path cost matrix between all order list $[ O _ { n } ]$ and stevedores for vehicle list K

\- Construct an initial solution by using the cost matrix by inserting the orders one at a time

\- Improve the solution by resequencing the orders on each route, as well as moving orders from one route to another, and exchanging orders between routes until the optimum solution is achieved

\- End while

\- Return global optimum delivery/pickup routing plan, including type of

fleet, distance, and travel time.

 Calculate the cost list of each agent resulted in the global optimum plan $[ C _ { a n s ( e ) } ] ;$ {cost of freight agent n based on the travel time and distance travelled and the fixed cost of vehicle on the time-varying network as a result of action a in the state $s _ { e }$ }

 Calculate the payoff list $[ \pi _ { a n s ( e ) } ] ;$ {a set of the percentage of saving in logistics cost compared to the status quo}

## 7. End for

8. While not termination do; (where termination is the maximum learning episodes)

$_ { e  e + l }$

$[ P _ { a n ( e + I ) } ] ;$ (the probability of using PCS for agent n in the next learning episode according to eq. (1))

 For every agent choose an action from $A = \{ a _ { I } , a _ { 2 } , a _ { 3 } \}$ with the calculated probability of $P _ { a n ( e + I ) }$

 Repeat steps 6-7, and update cost list $[ C _ { a n s ( e ) } ]$ , payoff list $[ \pi _ { a n s ( e ) } ]$ , and probability list $\left[ P _ { a n ( e + I ) } \right]$

## 9. End while

## Fig. 2. Simulation Algorithm.

## 4. Results

Port authorities are interested in understanding freight agents’ decision on using the PCS and quantifying their gains resulted from economies of scale and scope in a dynamic market. With the aim of facilitating this, our simulation model provides outputs that allow the port to observe the autonomous agents’ decisions using RL in a dynamic environment.

The results of the RL strategy were generated by using a self-developed simulation program. The simulation was coded in Python, calling the geo-processing tools of ArcGIS to solve the optimisation problem. The software ran on a Windows PC having a 3.4 GHz i7 processor and 16

GB of RAM. The VRP solver in ArcGIS [57] is based on a Tabu search algorithm that is widely considered as the best approach to solve large vehicle routing problems [58, 59]. The estimated travel times at various times-of-day for a typical weekday and weekend were extracted for each roadway link using the Google Map Distance Matrix API, using the “gmapsdistance” library developed for the R language [60].

The performance measures of the agent-based simulation model after 100 learning episodes is shown in Fig. 3. Measures focused on the total transport costs (including the time-based and distance-based costs), the total time and distance, the number of the two types of vehicles (measuring the shipment bundling), and the total number of trips. The benchmark is the status quo which was built from the observed data. The comparison between these measures with as a result of either providing the individual optimum plan (i.e. shipment bundling plans for each agent and shifting the shipments to the off-peak period) or adopting cooperation strategies.

Interestingly, the best results will be obtained if all agents sign up for a cooperative optimum plan. This result is expected because of economies of scale of operation where different shipments can be bundled by using larger vehicles (B-doubles), while the total distance travelled and the total logistics costs are at their minimum values, and the associated costs of each agent in each segment of the chain are shared.

As a result of RL after the learning period, some agents would continue cooperating through the PCS, while others would prefer individual operations over cooperation but are still more likely to use the PCS to get a higher profit as a result of the individual optimum plan. Interestingly, those agents who prefer individual operations are the major freight actors who have already used the economies of scale. For these agents, cooperation does not reduce the transport costs but would impose extra costs related to the violation of time-windows constraints or extra travelled distance to make a tour.

Given that the time-based and distance-based costs were calculated in the same way for both scenarios, the decrease in costs associated with the distance and time, and consequently the total transport costs, is estimated to be more than 50% if all agents sign up for the optimum solution. Considering that these results reflect changes across only 14 days, the savings in the long-term are expected to be major. Moreover, it should be noted that many other logistics processes are not considered explicitly in this study, and it is possible that introducing the PCS would improve these processes as well. In order to fully evaluate the economic feasibility of the PCS, other considerations such as costs associated with delay and administrative costs could also be taken into account. However, it should be noted that it is often difficult to draw conclusions solely based on the evaluation of transport costs without considering other costs, challenges, limitations, and other businesses’ needs.

Furthermore, the agent-based simulation using RL allows to observe which agents continue using PCS and which ones stop using that. The diagrams in Fig. 4 provide a graphical illustration of the transport cost of 272 agents in 14 states. Fig. 4(a) presents the transport cost of each agent in 14 states in the final learning episode (e = 100) where some agents chose to use PCS and adopted either an individual optimum plan or a cooperative plan, and a few others chose to maintain the status quo. This result was benchmarked against the status quo, depicted in Fig. 4(b). Fig. 4(c) presents the scenario where all agents sign up for the optimum plan, and Fig. 4(d) shows the transport costs for the scenario where all agents sign up for an individual optimum plan.

![](/api/attachments/XGAYJ2WV/fulltext/images/1d9bc693fceffb94e71d36e68bd721e4a18c1999368a95773ec53d31482235fc.jpg)  
Fig. 3. Performance measures.

Furthermore, two different scenarios were simulated by including different configurations of the PCS users. Fig. 4(e) presents a scenario where only ten major agents (i.e., those who have more shipments to be delivered) cooperate through the PCS, and Fig. 4(f) shows a scenario where all agents except the top ten sign up for a cooperative plan. The creation of these scenarios was motivated by the recent horizontal merging practices and large consortia that are spread between three large sections of the market: traditional maritime services, hinterland services, and freight handling services (Wen et al., 2019). The use of agent-based simulation allows to foresee and evaluate various scenarios before the implementation stage, as depicted in the diagrams in Fig. 4.

![](/api/attachments/XGAYJ2WV/fulltext/images/7c098045d754cb87af4e132255f048893237a0b00080a672d44d40b825875da6.jpg)

![](/api/attachments/XGAYJ2WV/fulltext/images/0c6fa3618ba80bfa0e9732e5da46d40b94e1e0a7b2f237daa0752cee3b477a30.jpg)

![](/api/attachments/XGAYJ2WV/fulltext/images/e5488a927eb66d49e75bfa46743ea3d079c6436535061e9c4cf05dbe75d59d04.jpg)

![](/api/attachments/XGAYJ2WV/fulltext/images/5d8a8207adcc977dfdd54140daa3b5e9c089687e0cc548bc0e4ad3d26f73264f.jpg)

![](/api/attachments/XGAYJ2WV/fulltext/images/452fcc99acbfe8791073df7806daa430a44b07b816e56938942ac01c647a6259.jpg)  
Fig. 4. Transport costs of agents in each state

![](/api/attachments/XGAYJ2WV/fulltext/images/e139b7b7de49bb9c1d632a9db371e551c9bd8d4fee16ee0166572ba2af945c7a.jpg)

Fig. 5 shows the transition of the probability of using the PCS during the learning period with various learning rates. The learning rate varies between 0 and 1 where a higher value presents faster learning. It controls how much agents are adjusting their actions with respect to the payoff in the previous learning episodes. The lower the value of learning rate, the slower the convergence would be, while too large learning rates can also lead to super-convergence (Smith and Topin, 2019). Accordingly, we tested three values (specifically, $\alpha = 0 . 2 , 0 . 5 , 0 . 8 )$ and the results showed that $a = 0 . 5$ would converge for 100 learning episodes. Typically, learning rates are configured naively at random by the user. However, the value used for learning rate can be calibrated and chosen based on the agents’ actual behavior, or using an adaptive variable learning rate (see e.g. (Tan et al., 2009; Gershman, 2015)).  
![](/api/attachments/XGAYJ2WV/fulltext/images/7b82fb59a6246c988dd5b4880e34dea66a1f2db5f986fc5eb38eb7d5398f834b.jpg)  
(a)

(b)  
![](/api/attachments/XGAYJ2WV/fulltext/images/c1ceea49f8a719738141092aa7148bf4b358f34e1814effcf418ced8ec3027eb.jpg)

![](/api/attachments/XGAYJ2WV/fulltext/images/5199c828ead77a9ffc5ba032bf6cce4cbbf731be26e8fadc5d1bf19f572b92b1.jpg)  
(c)  
Fig. 5. Transition of the probability of using PCS during the learning period with different learning rates (a) α=0.2, (b) α=0.5 and (c) α=0.8.

## 5. Implications and conclusions

The use of multi-agent simulations in DSS has proven to be very attractive for integrating multiple distributed work systems of a business enterprise where there is information asymmetry among decision makers [26]. Port logistics is an example of such system with various information, financial, physical, and liability flows among various agents. In this context, the objectives of autonomous and decentralised agents can be modelled as software agents in digitally enabled tools such as PCS. Although a PCS is often initiated to serve as an information hub and a tool to facilitate the exchange of information and administrative tasks, the main objective remains to encourage the cooperation among agents to increase efficiency, profit, and infrastructure utilisation. A PCS can provide both horizontal integrations through collaboration across agents of the same type, and vertical integration between different logistics providers across the supply chain. This study provides insights into the role of intelligent DSS as one of the PCS features in order to improve logistics performance in hinterland container transport.

In this study, we examined the role of an intelligent DSS prototype for port logistics through agent-based simulation. Generally, the use of multi-agent simulation was motivated by the following considerations: (i) the system is a decentralized and distributed system and agents have incomplete information about the global view of the system; (ii) there are dependencies between agents’ actions mainly due to limited resources (e.g., vehicles, timeslots) in the system and a coordination model resolves these dependencies; (iii) the cooperation among individual agents results in a more efficient solution. In this study, the environment was modelled as historydependent, episodic, dynamic (non-deterministic), and a finite set of discrete states - each state representing one day.

A self-learning decision support algorithm was developed using RL and an NP-hard optimisation problem in each learning episode. Using a metaheuristic algorithm (Tabu search), this prototype proves to be able to provide the optimum solution in a dynamic and large-scale environment with reasonable running times. The software architecture we envisaged for our prototype includes several layers. The long-term and full information of orders and active fleets (i.e. demands and supplies) are stored in the enterprise resource planning (ERP) system of the importer/exporter and the transport company. Agents who have signed up for PCS, submit each day the new list or changes to the existing one to the central PCS server via a web-service for planning for the next day. The central server runs the optimisation and matching algorithm and uses a web service to retrieve the tour and transportation plans.

The decision of the logistics providers to use the PCS should consider some kind of a pilot project, experiencing the gains and losses in a dynamic market, where heterogeneous agents have a degree of freedom to experience their output through the system, learn and decide whether use the service. Accordingly, the agent-based model developed in this study enables heterogeneous actions as a result of an adaptive RL algorithm inspired by human decision making strategies.

The results of the simulation of two weeks container movements indicates huge savings in total transport costs, distance travelled and higher utilisation of trucks from the resource sharing that is provided as a solution by DSS prototype. The results prove that the cooperation between agents in sharing vehicles through the PCS can decrease the total travel distance and total logistics costs as well as improve vehicle utilization. Although this result is explicitly expected, the amount of savings in logistics costs is required to be quantified in order to provide a robust proof of concept for port managers and to investigate which freight agents might be willing to use the PCS. Accordingly, we show that it is strictly better for the minor agents to use this – a conclusion generated endogenously inside the model as a trade-off between exploration and exploitation.

In practice, developing such intelligent DSS has intrinsic challenges related to information/service sharing, commitment binding, and adoption process. Agents may not like to share private information with others for business advantage. Furthermore, they might be afraid of a long-term binding commitment. It is also important to recognize that integration does not come without costs and the adoption process of PCS will require an extensive amount of coordination and cooperation. As the PCS needs communicating and integrating across business boundaries, the complexity of the adoption process, and the associated coordination costs and potential for opportunistic behaviour that can damage the adoption process, are heightened. Coordination issues of transport chains have been studied by applying a conceptual frameworks or transaction costs economic theory [61-64].

The lack of empirical evaluations of the existing PCSs imposed a limitation upon this study, meaning the evaluation of agents’ decisions towards the PCS could only be performed in a simulated environment. Even though the results of simulation showed that the PCS does not give a direct benefit regarding the transport costs for some agents, other indirect economic benefits can be further explored in future research. Evaluating whether the freight actors see a benefit in adopting cooperation strategies through a PCS needs to be investigated in a broader concept of their strategic behaviour and the designed mechanism. Hence, a behavioural preference elicitation mechanism can be designed within the context of the PCS, accounting for all business requirements on various attributes (e.g. cost, time, type of service), and being incentive compatible. Behavioural mechanism design would ensure the incentive compatibility and nonnegative pricing strategy. The incentive compatibility in a behavioural designed mechanism would allow users to detail truthfully their business requirements and their so-called “inconvenience factors”. Customised non-negative pricing strategy would also indicate that the platform provider can gain revenue while the users’ maximum willingness-to-pay will never be exceeded the actual price they will pay.

In this study, we have shown the practicality of this proof of concept for two-week data of hinterland transport for the Port of Brisbane. This model can be improved by expanding the number of states (i.e., longer planning horizon), considering seasonal or yearly trends, and generally incorporating greater variation. In this way, it could be possible to better observe the accumulated experience of agents while assuming the possibility of monthly, seasonal, or yearly integrating both sea and land transport agents and their interactions, something that was not possible in this study due to lack of data on the sea transport. Also, due to the lack of information about the other involved costs, this study looks at the savings in the transport costs as the only criterion to use a PCS. The model presented in this study can be improved by incorporating other involved costs such as storage, handling, and administrative costs.

Future research could incorporate more advanced behaviour of agents such as proactiveness or social ability. In our study, the agents were assumed to have reactiveness ability, meaning that agents were able to evaluate their actions and respond to their evaluation. Instead, agents with proactiveness ability would not be driv solely by payoff results and would be able to recognise long-term opportunities and take various initiatives [55]. Also, the social ability of agents is not limited only to exchanging information but rather could include market mechanisms such as negotiations, contracting, auction, and merging [55]. Due to dominant transport agents and the merger of the transport operators’ industry, the behaviour of agents exhibits oligopolistic nature [65]. Hence, game-theoretic approaches seem very relevant in simulating the interactions between agents and their intention to use decision support tools provided by PCS in oligopolistic markets. A study by Dai and Chen [66] is an example of Game-theory approach and auction mechanism to model the decentralised and self-interested agents in the logistics outsourcing problem.

## 6. Acknowledgements

We are grateful for the support provided by the port partnership program between the Port of Brisbane Pty Ltd (PBPL) and the University of Queensland. We are particularly thankful for the data provided by Andrew Rankine from the Port of Brisbane Pty Ltd (PBPL). We are also grateful for the comments of two reviewers that have significantly contributed to improve an earlier version of the manuscript.

## 7. References

[1] S. Gavirneni, R. Kapuscinski, S. Tayur, Value of information in capacitated supply chains, Management science, 45(1) (1999) 16-24. https://www.jstor.org/stable/2634919.

[2] H.L. Lee, K.C. So, C.S. Tang, The Value of Information Sharing in a Two-Level Supply Chain, Management Science, 46(5) (2000) 626-643. https://search.proquest.com/docview/213243953?accountid=14723.

[3] H. Zhou, W.C. Benton, Supply chain practice and information sharing, Journal of Operations Management, 25(6) (2007) 1348-1365. https://doi.org/10.1016/j.jom.2007.01.009.

[4] F. Sahin, E.P. Robinson, Information sharing and coordination in make-to-order supply chains, Journal of Operations Management, 23(6) (2005) 579-598. https://doi.org/10.1016/j.jom.2004.08.007.

[5] R. Kaipia, J. Holmström, J. Småros, R. Rajala, Information sharing for sales and operations planning: Contextualized solutions and mechanisms, Journal of Operations Management, 52(2017) 15-29. https://doi.org/10.1016/j.jom.2017.04.001.

[6] S.D. Pathak, Z. Wu, D. Johnston, Toward a structural view of co-opetition in supply networks, Journal of Operations Management, 32(5) (2014) 254-267. https://doi.org/10.1016/j.jom.2014.04.001.

[7] F. Córdova, C. Durán, A Business Model Design for the Strategic and Operational Knowledge Management of a Port Community, Annals of Data Science, 1(2) (2014) 191-208. https://10.1007/s40745-014-0014-8.

[8] F.J. Srour, M. van Oosterhout, P. van Baalen, R. Zuidwijk, Port community system implementation: Lessons learned from international scan, in: 87th Transportation Research Board Annual Meeting, Transportation Research Board, Washington DC, 2008.

[9] V. Carlan, C. Sys, T. Vanelslander, How port community systems can contribute to port competitiveness: Developing a cost–benefit framework, Research in Transportation Business & Management, 19(2016) 51-64. https://doi.org/10.1016/j.rtbm.2016.03.009.

[10] European Commission, Guidelines on the applicability of Article 101 of the Treaty on the Functioning of the European Union to horizontal co-operation agreements, Official Journal of the European Union, 11(2011) 1-72.

[11] M.P. Van Oosterhout, A. Veenstra, M. Meijer, N. Popal, J. Van den Berg, Visibility platforms for enhancing supply chain security: a case study in the Port of Rotterdam, in: Proceeding of the International Symposium on Maritime Safety, Security and Environmental Protection, Athens, 2007, pp. 20-21.

[12] Y. Keceli, A proposed innovation strategy for Turkish port administration policy via information technology, Maritime Policy &amp; Management, 38(2) (2011) 151-167. https://10.1080/03088839.2011.556676.

[13] Y. Keceli, H.R. Choi, Y.S. Cha, Y.V. Aydogdu, A Study on Adoption of Port Community Systems According to Organization Size, in: 2008 Third International Conference on Convergence and Hybrid Information Technology, 2008, pp. 493-501.

[14] E. Sweeney, Port community learning needs: analysis and design, Pomorski zbornik, 43(1) (2005) 27-43.

[15] D. Tsamboulas, P. Moraiti, A. Lekka, Performance evaluation for implementation of port community system, Transportation Research Record, 2(2273) (2012) 29-37. https://10.3141/2273-04.

[16] D. Claudia, C. Felisa, Conceptual Analysis for the Strategic and Operational Knowledge Management of a Port Community, Informatica Economica, 16(2) (2012) 35-44. https://search.proquest.com/docview/1030278722?accountid=14723.

[17] T. Edvard, A. Adrijana, H. Bojan, The Necessity of Port Community System Implementation in the Croatian Seaports, Promet (Zagreb), 24(4) (2012) 305-315. https://10.7307/ptt.v24i4.444.

[18] M. Ghazanfari, S. Rouhani, M. Jafari, A fuzzy TOPSIS model to evaluate the Business Intelligence competencies of Port Community Systems, Polish Maritime Research, 21(2) (2014) 86-96. https://10.2478/pomr-2014-0023.

[19] Y.V. Aydogdu, S. Aksoy, A study on quantitative benefits of port community systems, Maritime Policy and Management, (2013) 1-10. https://10.1080/03088839.2013.825053.

[20] T. Vanelslander, C. Sys, J.S.L. Lam, C. Ferrari, A. Roumboutsos, M. Acciaro, R. Macário, G. Giuliano, A serving innovation typology: mapping port-related innovations, Transport Reviews, 39(5) (2019) 611-629. https://10.1080/01441647.2019.1587794.

[21] T.E. Notteboom, J.-P. Rodrigue, Port regionalization: towards a new phase in port development, Maritime Policy & Management, 32(3) (2005) 297-313. https://doi.org/10.1080/03088830500139885.

[22] ITF, Integration and competition between transport and logistics businesses, ITF Round Tables, No. 146 ed., OECD Publishing, Paris, 2010. https://doi.org/10.1787/9789282102619-en.

[23] E. van de Voorde, T. Vanelslander, Market Power and Vertical and Horizontal Integration in the Maritime Shipping and Port Industry, Paris, 2010. https://10.1787/9789282102619-3-en.

[24] G. Giuliano, T. O’Brien, Reducing port-related truck emissions: The terminal gate appointment system at the Ports of Los Angeles and Long Beach, Transportation Research Part D: Transport and Environment, 12(7) (2007) 460-473. https://doi.org/10.1016/j.trd.2007.06.004.

[25] F. Schulte, R.G. González, S. Voß, Reducing port-related truck emissions: coordinated truck appointments to reduce empty truck trips, in: International Conference on Computational Logistics, Springer, 2015, pp. 495-509. https://doi.org/10.1007/978-3-319-24264-4\_34.

[26] R. Kishore, H. Zhang, R. Ramesh, Enterprise integration using the agent paradigm: foundations of multi-agent-based integrative business information systems, Decision Support Systems, 42(1) (2006) 48-78. https://doi.org/10.1016/j.dss.2004.09.011.

[27] A. Valluri, D.C. Croson, Agent learning in supplier selection models, Decision Support Systems, 39(2) (2005) 219-240. https://doi.org/10.1016/j.dss.2003.10.008.

[29] C. Xu, Z. Chi, Pattern-oriented agent-based modeling for financial market simulation, in: International Symposium on Neural Networks, Springer, 2007, pp. 626-631. https://doi.org/10.1007/978-3-540-72383-7\_74.

[30] E. Bonabeau, Agent-based modeling: Methods and techniques for simulating human systems, in: National Academy of Sciences, 2002, pp. 7280-7287. https://doi.org/10.1073/pnas.082080899.

[31] D. Taghawi-Nejad, Modelling the economy as an agent-based process: ABCE, a modelling platform and formal language for ACE, Journal of Artificial Societies and Social Simulation, 16(3) (2013) 1. https://10.18564/jasss.2150.

[32] D. Eilers, C.L. Dunis, H.-J. von Mettenheim, M.H. Breitner, Intelligent trading of seasonal effects: A decision support algorithm based on reinforcement learning, Decision Support Systems, 64(2014) 100-108. https://doi.org/10.1016/j.dss.2014.04.011.

[33] W.Y. Liang, C.C. Huang, Agent-based demand forecast in multi-echelon supply chain, Decision Support Systems, 42(1) (2006) 390-407. https://doi.org/10.1016/j.dss.2005.01.009.

[34] S.K. Chaharsooghi, J. Heydari, S.H. Zegordi, A reinforcement learning model for supply chain ordering management: An application to the beer game, Decision Support Systems, 45(4) (2008) 949-959. https://doi.org/10.1016/j.dss.2008.03.007.

[35] R. Sprenger, L. Mönch, A decision support system for cooperative transportation planning: Design, implementation, and performance assessment, Expert Syst Appl, 41(11) (2014) 5125- 5138. https://doi.org/10.1016/j.eswa.2014.02.032.

[36] M. Bouzid, On-line transportation scheduling using spatio-temporal reasoning, in: 10th International Symposium on Temporal Representation and Reasoning, and Fourth International Conference on Temporal Logic., IEEE, Cairns, Queensland, Australia, 2003, pp. 17-25. https://10.1109/TIME.2003.1214876.

[37] H.J. Burckert, P. Funk, G. Vierke, An intercompany dispatch support system for intermodal transport chains, in: 33rd Annual Hawaii International Conference on System Sciences, IEEE, Maui, HI, USA, 2000, pp. 10 pp. https://10.1109/HICSS.2000.926672.

[38] L. Henesey, Multi-agent container terminal management, in, Blekinge Institute of Technology, 2006. https://diva2:837142.

[39] J.w. Dong, Y.J. Li, Agent-based design and organization of intermodal freight transportation systems, in: Machine Learning and Cybernetics, 2003 International Conference on, IEEE, 2003, pp. 2269-2274. https://10.1109/ICMLC.2003.1259885.

[40] D. Baindur, J.M. Viegas, An agent based model concept for assessing modal share in interregional freight transport markets, Journal of Transport Geography, 19(6) (2011) 1093-1105. https://10.1016/j.jtrangeo.2011.05.006.

[41] G. Liedtke, Principles of micro-behavior commodity transport modeling, Transport Res E-Log, 45(5) (2009) 795-809. https://10.1016/j.tre.2008.07.002.

[42] M.J. Roorda, R. Cavalcante, S. McCabe, H. Kwan, A conceptual framework for agent-based modelling of logistics services, Transportation Research Part E: Logistics and Transportation Review, 46(1) (2010) 18-31. https://doi.org/10.1016/j.tre.2009.06.002.

[43] J. Holmgren, M. Dahl, P. Davidsson, J.A. Persson, Agent-based simulation of freight transport between geographical zones, Procedia Computer Science, 19(2013) 829-834. https://10.1016/j.procs.2013.06.110.

[44] E. Taniguchi, T. Yamada, M. Okamoto, Multi-agent modelling for evaluating dynamic vehicle routing and scheduling systems, Journal of the Eastern Asia Society for Transportation Studies, 7(2007) 933-948. https://doi.org/10.11175/easts.7.933.

[45] L. Abdul-Mageed, An Agent-based Approach for Improving the Performance of Distributed Business Processes in Maritime Port Community, in: School of Computing, Communications and Electronics, Faculty of Science and Technology, University of Plymouth, Research Theses Main Collection, 2012. http://hdl.handle.net/10026.1/1239.

[46] G. Gigerenzer, P.M. Todd, Fast and frugal heuristics: The adaptive toolbox, in: Simple heuristics that make us smart, Oxford University Press, 1999, pp. 3-34.

[47] B. Munier, R. Selten, D. Bouyssou, P. Bourgine, R. Day, N. Harvey, D. Hilton, M. Machina, P. Parker, J. Sterman, E. Weber, B. Wernerfelt, R. Wensley, Bounded Rationality Modeling, A Journal of Research in Marketing, 10(3) (1999) 233-248. https://10.1023/A:1008058417088.

[48] A. Rubinstein, Irrational diversification in multiple decision problems, European Economic Review, 46(8) (2002) 1369-1378. https://doi.org/10.1016/S0014-2921(01)00186-6.

[49] W. Gaissmaier, L.J. Schooler, The Smart Potential behind Probability Matching, Cognition, 109(3) (2008) 416-422. https://10.1016/j.cognition.2008.09.007.

[50] J. Rivas, Probability matching and reinforcement learning, Journal of Mathematical Economics, 49(1) (2013) 17-21. https://doi.org/10.1016/j.jmateco.2012.09.004.

[51] J.R. Busemeyer, J.T. Townsend, Decision Field Theory: A Dynamic-Cognitive Approach to Decision Making in an Uncertain Environment, Psychological Review, 100(3) (1993) 432-459. https://10.1037//0033-295X.100.3.432.

[52] A. Rubinstein, A. Tversky, Naive strategies in zero-sum games, Tel Aviv University, Sackler Institute of Economic Studies, 1993.

[53] Port of Brisbane Pty Ltd, Import/Export Logistics Chain Study, 2013.

[54] A.M. Villamizar, J.R. Montoya-Torres, A.A. Juan, J. Caceres-Cruz, A simulation-based algorithm for the integrated location and routing problem in urban logistics, in: 2013 Winter Simulations Conference (WSC), 2013, pp. 2032-2041. http://dl.acm.org/citation.cfm?id=2676128.2676236.

[55] M. Wooldridge, An introduction to multiagent systems, John Wiley & Sons, 2009.

[56] R.R. Bush, F. Mosteller, A mathematical model for simple learning, Psychological Review, 58(5) (1951) 313-323. https://10.1037/h0054388.

[57] ESRI, ArcGIS desktop: Release 10.4, in, Environmental Systems Research Institute, 2017.

[58] M. Gendreau, An introduction to tabu search, in: F. Glover, G.A. Kochenberger Eds. Handbook of Metaheuristics, Springer US, Boston, MA, 2003, pp. 37-54. https://10.1007/0-306- 48056-5\_2.

[59] M. Gendreau, A. Hertz, G. Laporte, A Tabu Search Heuristic for the Vehicle Routing Problem, Management Science, 40(10) (1994) 1276-1290. https://10.1287/mnsc.40.10.1276.

[60] R.A. Melo, D. Zarruk, gmapsdistance : Distance and travel time between two points from google maps, in, 2016, pp. R programming package.

[61] P. Franc, M. Van der Horst, Understanding hinterland service integration by shipping lines and terminal operators: a theoretical and empirical analysis, Journal of Transport Geography, 18(4) (2010) 557-566. https://doi.org/10.1016/j.jtrangeo.2010.03.004.

[62] V. Reis, A new theoretical framework for integration in freight transport chains, Transport Reviews, 39(5) (2019) 589-610. https://10.1080/01441647.2019.1573860.

[63] M.R. van Der Horst, L.M. van Der Lugt, An Institutional Analysis of Coordination in Liberalized Port-related Railway Chains: An Application to the Port of Rotterdam, Transport Reviews, 34(1) (2014) 68-85. https://10.1080/01441647.2013.874379.

[64] D. Jaffee, Kink in the intermodal supply chain: interorganizational relations in the port economy, Transportation Planning and Technology, 39(7) (2016) 730-746. https://10.1080/03081060.2016.1204093.

[65] H. Lee, M. Boile, S. Theofanis, S. Choo, K.-D. Lee, A freight network planning model in oligopolistic shipping markets, The Journal of Networks, Software Tools and Applications, 17(3) (2014) 835-847. https://10.1007/s10586-013-0314-3.

[66] B. Dai, H. Chen, A multi-agent and auction-based framework and approach for carrier collaboration, Logistics Research, 3(2) (2011) 101-120. https://10.1007/s12159-011-0046-9.

## Author contribution

Elnaz Irannezhad: Conceptualization, Methodology, Writing—Original draft preparation and Reviewing.

Carlo G. Prato: Conceptualization, Methodology, Writing—Reviewing and Editing

Mark Hickman: Conceptualization, Methodology, Writing—Reviewing and Editing

![](/api/attachments/XGAYJ2WV/fulltext/images/e7f1eae3c9969f5ae86ae6d7b5b3d58af9c10fe3aea3ad76365a66f61c763ca9.jpg)

Elnaz Irannezhad is a postdoctoral research fellow at the Australian Institute of Business and Economics, at the University of Queensland. Dr Irannezhad is engaged with the Port of Brisbane partnership project to deliver cutting-edge research supporting port growth. Her research investigates the role of decision making of freight agents in the international trade and emerging technologies and solutions to support the logistics operations of the port logistics.

![](/api/attachments/XGAYJ2WV/fulltext/images/94f54d6b7b2eedc0fde226f26442a13a501784ffb4f397690f3e0808e9eb2002.jpg)

Carlo G. Prato is a professor of Transport Engineering within the School of Civil Engineering at the University of Queensland and the head of discipline. Prof. Prato has taught courses and performed research in transport modelling, statistics and econometrics. His expertise and research interest include survey design, behavioural transport modelling, agent-based modelling, and methodological innovation.

![](/api/attachments/XGAYJ2WV/fulltext/images/3c9757c624bdd02533c85c176d8e9051702537649655fec6782c1d77385da404.jpg)

Mark Hickman is a professor of Transport Engineering within the School of Civil Engineering at the University of Queensland and the TAP Chair. Prof. Hickman has taught courses and performed research in public transit planning and operations, travel demand modeling, and traffic engineering. His areas of research interest and expertise include public transit planning and operations, urban transportation planning, and the application of remote sensing technology for traffic management.

# Journal Pre-proof

Graphical abstract

![](/api/attachments/XGAYJ2WV/fulltext/images/de2f958e85f9d56a101152f8ec79b1796f08bcc30c470934aaa5cd8823ef6ff6.jpg)

## Highlights:

 We simulate a prototype of an intelligent decision support tool for port logistics.

 A multi-agent simulation with optimisation algorithm enables heterogeneous actions.

 We present a reinforcement learning, inspired by human decision-making strategies.

 The simulation demonstrates the dynamics of delivery and pick up of shipments.

 Reinforcement learning shows the DSS is attractive for smaller freight agents.
