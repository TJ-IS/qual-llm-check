---
otero_id: 10920
otero_key: "WV22FW7T"
title: "Agent-based demand forecast in multi-echelon supply chain"
authors: "Wen-Yau Liang; Chun-Che Huang"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.01.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Agent-based demand forecast in multi-echelon supply chain

Wen-Yau Liang <sup>a</sup>, Chun-Che Huang <sup>b,T</sup>

<sup>a</sup> Department of Information Management, National Changhua University of Education, Changhua, Taiwan, ROC <sup>b</sup> Department of Information Management, National Chi-Nan University, Pu-Li, Na-Tau, Taiwan, ROC

Available online 12 March 2005

## Abstract

Supply chain management (SCM) is an emerging field that has commanded attention and support from the industrial community. Demand forecast taking inventory into consideration is an important issue in SCM. There are many diverse inventory systems, in theory or practice, which are operated by entities (companies) in a supply chain. In order to increase supply chain effectiveness, minimize total cost, and reduce the bullwhip effect, integration and coordination of these different systems in the supply chain (SC) are required using information technology and effective communication. The paper develops a multi-agent system to simulate a supply chain, where agents operate these entities with different inventory systems. Agents are coordinated to control inventory and minimize the total cost of a SC by sharing information and forecasting knowledge. The demand is forecasted with a genetic algorithm (GA) and the ordering quantity is offered at each echelon incorporating the perspective of <sup>b</sup>systems thinking<sup>Q</sup>. By using this agent-based system, the results show that total cost decreases and the ordering variation curve becomes smooth.

Keywords: SCM; Demand forecast; Inventory management; Genetic algorithm; Rough set theory; Agent-based system

## 1. Introduction

Supply chain management (SCM) is an emerging field that has commanded attention and support from the industrial community. SC is defined as the chain linking each entity of the manufacturing and supply process from raw materials through to the end user [30,37]. A supply chain comprises many systems, including various manufacturing, storage, transportation, and retail systems [10,29,43]. Gavirneni et al. [8] showed that managing any one of these systems involves a series of complex trade-offs between different business function costs. For example, to efficiently run a manufacturing operation, the cost must compromise with the costs of inventory and raw materials [4,7,39]. To integrate different SC systems, entities must be coordinated incorporating the <sup>b</sup>systems’ thinking<sup>Q</sup> perspective [19].

Global optimization is the central issue of systems thinking. All managers’ best interest is to ensure that the overall cost is reduced and operations among various systems are integrated through coordination.

Literature shows that reducing overall system cost and understanding how these savings are deployed among the SC entities are of the best interest [20,21,39,41]. When the system is not coordinated, that is, each entity in the supply chain does what is best for that entity, it results in local optimization. Each supply chain entity optimizing its own operation without considering the impact on other entities often results in larger variation of inventory and demand in the entire SC. To have good coordination, managers need to communicate in detail, which is often a timeconsuming process. In addition, ineffective communication affects material flows and creates long lead times [19]. To solve this problem and to make communication effective, information must be available and transparent using information technology [22]. Agent technology provides the distributed environment a great promise of effective communication [23,40]. An agent is a program that performs a specific task intelligently without any human supervision and agents can communicate with each other cooperatively. Therefore, agent technology is suitable to solve communication concerns for a distributed environment. Recent researches also show that the multi-agent approach plays a significant role in supply chain management, for example Fu et al. [7], Kimbrough et al. [16], and Swaminathan et al. [40].

This paper focuses on demand forecast with information sharing and on systems’ thinking, which is an important coordination and communication issue in SC inventory management [35,45]. This paper applies agent technology to simulate a SC and control entities’ inventory. Agents in the supply chain use the Real-coded Genetic Algorithm (RGA) [27] to calculate the optimal demand ordering quantity for every echelon. Each entity communicates and shares demand information with the others to achieve global cost minimization. Managers in each entity are assumed here to be willing to share information truthfully. With this approach, the supply chain’s total cost is mini mized. In addition, agents explore and store the knowledge of managers, operationalized as rules and reuse the rules while facing similar problems later. This paper is organized as follows; in Section 2, the literature on supply chain demand forecast and agent technology is reviewed; in Section 3, the SC model is illustrated; Section 4 proposes the GA solution approach incorporated with rough set theory. System architecture, agent role and simulation scenarios are presented in Section 5, where a scenario design is developed and the analysis results are discussed to validate the proposed solution approaches. Section 6 concludes the paper.

## 2. Literature review of related approaches

To improve the supply chain’s performance under demand uncertainty, Lee et al. [24] suggested that companies in the supply chain must share information and coordinate orders. Chen et al. [4] compared an exponential-smoothing forecasting model and a moving-average model, and also compared a correlated demand with a demand with linear trend. Zhao and Lee [44] studied the double exponential smoothing (DES) [6] and Winter’s exponential method (WIN) [42]; they found that although Winter’s method produced a lower bias and standard deviation of forecasting error, it resulted in higher total costs and schedule instability. However, these forecasting methods are based on large previous data and they forecast market demand of period t + 1 without considering the total cost of supply chain in period t. The literature review shows:

<sup>!</sup> Traditionally, supply chain entities do not share the type and status of their inventory system with other entities, resulting in the bullwhip effect and difficulty in the control and forecast of inventories.

<sup>!</sup> Most research related to demand forecasting only focuses on a single echelon of the supply chain and research related to multi-echelon inventory management always assumes that all entities use the same inventory system, for example, Kimbrough et al. [16], McBurney et al. [26], Chen et al. [4,5]. Little research focuses on the multi-echelon supply chain involving various inventory management systems.

<sup>!</sup> Traditional forecasting methods, for example, simple moving-averages, moving-average model and Winter’s exponential, are based on large previous data and forecast the demand of period t + 1 without considering the total cost of the supply chain at period t. In order to solve this problem, a heuristic approach, e.g., the genetic algorithm (GA) is required, because large data are not required and the minimal total cost is simply the objective function in GA. In genetic code format every bit represents a demand order for each entity. Consequently, the demand order of every entity is considered during the evolution process and total cost control in the supply chain is optimized globally.

<sup>!</sup> The traditional GA approach does not incorporate with knowledge [13]. Using prior knowledge, e.g. expert knowledge, to limit the dimensionality of the search space and identify the most important design parameters is helpful to increase the convergence speed [31]; or incorporation of problem-specific knowledge, such as constraint-handling based knowledge, guiding the genetic search for good and feasible solutions and increasing the efficiency of evolutionary processes [3]. Hence, incorporating knowledge-based mechanisms, e.g., rule-bases, is considered as a way to improve an evolutionary algorithm’s performance [14].

<sup>!</sup> In traditional rule-bases in expert systems, rules are determined by using quantitative methods and knowledge is stored mainly in the dorm of rules, as are problem-solving procedures. These rulebases, are not used to reduce information-preserving data, represent uncertain or imprecise knowledge, identify and evaluate data dependencies, reason with uncertainty approximate pattern classification, nor to discover hidden data patterns [1]. Thus, a knowledge discovery approach, e.g., rough set approach, is required [9,18,34]. It specially induces some rules to large turbulent data. With the rules, the forecast result is more accurate and effective.

## 3. A supply chain model

The model proposed in this paper is based on beer game four echelons [38], but assumes a single entity at each echelon (Fig. 1). Four echelons including suppliers, manufacturers, distributors and retailers are allowed to use different inventory systems. In general, there are three types of independent-demand inventory systems, (1) Periodic Review system (P system), (2) Continuous Review system (Q system), and (3) Optional system [17].

## 3.1. Periodic review system

The P system is the periodic review system, sometimes called a fixed interval reorder system or periodic reorder system, in which an item’s inventory position is reviewed periodically rather than continuously. Such a system can simplify delivery scheduling because it establishes a routine. A new order is always placed at the end of each review, and the time between orders (TBO) is fixed at P. Demand is a random variables, so total demand between reviews varies. An example of a periodic review system is that of a soft-drink supplier making weekly rounds of grocery stores. Each week, the supplier reviews the store’s inventory of soft drinks and restocks the store with enough items to meet demand and safety stock requirements until the next week [17]. The constraints and basic assumptions of the P system are described as follows:

(R, S) system: check inventory’s state in a fixed period (R), and decide the ordering quantity Q at every check process. Q is a variable that makes the inventory arrive at stock level. Therefore, Q is used to control the inventory quantity, which is the difference between inventory position and stock level (S).

The stock level and ordering quantity is formulated as follows:

$$
S = \mathrm{AVGL} \times \mathrm{AVG} + z \times \mathrm{STD} \times \sqrt {\mathrm{AVGL}}
$$

$$
\mathrm{IP} = \mathrm{OH} + \mathrm{SR} - \mathrm{BO}
$$

$$
Q = \left\{ \begin{array}{l l} S - I P, & \text { if   } \mathrm{IP} \neq S \text {   per   period } \\ 0, & \text { if   otherwise } \end{array} \right.
$$

where S: stock level; Q: ordering quantity; z: service level (z value of normal distribution); IP: inventory position of the item.; OH: number of units in on-hand inventory; SR: scheduled receipts; BO: number of units whether backordered or allocated; AVGL: average lead time per echelon; AVG: average demand per period; STD: standard deviation per period.

Physical Flow

<table><tr><td>Supplier(P system)</td><td>Manufacturer(Q System)</td><td>Distributor(P System)</td><td>Retailer(Optional System)</td></tr></table>

Information Flow  
Fig. 1. Supply chain model.

## 3.2. Continuous review system

The Q system sometimes called a reorder point system (ROP) or fixed ordering quantity system, tracks the remaining inventory of an item each time a withdrawal is made to determine whether it is time to reorder. In practice, these reviews are done frequently (e.g. daily) and often continuously (after each withdrawal), so we can say that the TBO is variable. The advent of computers and electronic cash registers linked to inventory records has made continuous reviews easy. At each review, a decision is made about an item’s inventory position. If it is judged to be too low, the system triggers a new order. The IP measures the item’s ability to satisfy future demand. It includes scheduled receipts (SR), which are orders that have been placed but not yet received, plus on-hand inventory (OH) minus backorders (BO). Sometimes scheduled receipts are called open orders. The formula as follows: $\scriptstyle \mathrm { I P = O H + S R - B O }$ . Eliminating the BO, IP and OH are different only during the lead time. When the inventory position reaches a predetermined minimum level, called the reorder point (R), a fixed quantity Q of the item is ordered. In the Q system, although the ordering quantity Q is fixed, the TBO can vary [17]. Constraints and basic assumptions of the Q system are described as follows:

(s, S) system: checks inventory’s state at any time, and can accurately control the number of on-hand inventory. If the quantity of on-hand inventory is smaller than safety stock (ss), then ordering quantity Q arrives to stock level (S). Therefore, Q is a variable and represents the difference between inventory position and stock level (S).

The stock level and safety stock can be formulated as follows:

$$
\mathrm{ss} = z \times \sqrt {\mathrm{AVGL} \times \mathrm{STD} ^ {2} + \mathrm{AVG} ^ {2} \times \mathrm{STDL} ^ {2}}
$$

$$
S = \mathrm{AVGL} \times \mathrm{AVG} + \mathrm{ss}
$$

$$
Q = \left\{ \begin{array}{l l} S - \mathrm{IP}, & \text { if } \mathrm{IP} \leq \mathrm{ss} \\ 0, & \text { if } \mathrm{IP} > \mathrm{ss} \end{array} \right.
$$

where, ss: safety stock; S: stock level; STDL: standard deviation of lead time per echelon.

## 3.3. Optional system

Sometimes called the optional review, min–max, or (s, S) system, the optional replenishment system (the O system) is much like the P system. It is used to review the inventory position at fixed time intervals and, if the position has dropped to a predetermined level, to place a variable-sized order to cover expected needs. The new order is large enough to bring the inventory position up to a target inventory. However, orders are not placed after a review unless the inventory position has dropped to the predetermined minimum level. The minimum level acts as reorder point (R) does in a Q system. If the target is 100 and the minimum level is 60, the minimum order size is 40. The optional review system is the mixed system between the Q and the P systems [17]. The constraints and basic assumptions of the O system are described as follows:

$$
Q = \left\{ \begin{array}{l l} S - \text { IP }, & \text { if   } \text { IP } <   \text { ss } \\ 0, & \text { if   otherwise } \end{array} \right.
$$

## 3.4. Comparison of these systems and assumption

Table 1 presents the distinguishing characteristics of Q, P, and O systems in several dimensions [17]:

<sup>!</sup> The Q system checks inventory’s status at any time. When the inventory position is smaller than safety stock, it must reorder new fixed quantity materials or products. It is suitable for those situations as follow: (1) the storage cost is expensive, (2) the storage space is limited, (3) the reduction of inventory cost is desired, (4) there is no routine established for ordering or transportation, (5) the inventory is more essential, (6) the demand of inventory is unstable, (7) the review cost is not significant, (8) the management cost is not significant, (9) the ordering cost is not significant, and (10) the transportation cost is not significant.

<sup>!</sup> The P system checks inventory’s status in every fixed period. At the end of each review, it must reorder new materials or products to arrive to stock level. It is suitable for those situations as follow: (1) the storage cost is not expensive, (2) the storage space is not limited, (3) the inventory cost is not very significant, (4) it needs to establish routines for ordering or transportation, (5) the inventory is not more essential, (6) the demand of inventory is stable, (7) the reduction of review cost is desired, (8) the reduction of management cost is desired, (9) the reduction of ordering cost is desired, and (10) the reduction of transportation cost is desired.

Table 1  
The differentiation of P, Q, and O systems

<table><tr><td rowspan="2">Dimensions</td><td colspan="3">Systems</td></tr><tr><td>Q system</td><td>O system</td><td>P system</td></tr><tr><td>The way of review</td><td>Continuous</td><td>Periodic (P)</td><td>Periodic (P)</td></tr><tr><td>The review rate of a product</td><td>Different</td><td>Same</td><td>Same</td></tr><tr><td>The time of ordering</td><td>When the IP has dropped to the R</td><td>When the IP has dropped to the R</td><td>At the end of each review</td></tr><tr><td>The amount of ordering</td><td>Fixed (Q)</td><td>Unfixed, to bring the IP up to the T</td><td>Unfixed, to bring the IP up to the T</td></tr><tr><td>Ordering schedules</td><td>Complex ←— → Simple</td><td></td><td></td></tr><tr><td>Transportation schedules</td><td>Complex ←— → Simple</td><td></td><td></td></tr><tr><td>Holding cost of inventory</td><td>Low ←— → High</td><td></td><td></td></tr><tr><td>Review cost</td><td>High ←— → Low</td><td></td><td></td></tr><tr><td>Management cost</td><td>High ←— → Low</td><td></td><td></td></tr><tr><td>Ordering cost</td><td>High ←— → Low</td><td></td><td></td></tr><tr><td>Transportation cost</td><td>High ←— → Low</td><td></td><td></td></tr><tr><td>Risk of inventory shortage</td><td>Low ←— → High</td><td></td><td></td></tr><tr><td>Safety stock inventory</td><td>Low ←— → High</td><td></td><td></td></tr></table>

<sup>!</sup> The O system checks inventory’s state at fixed periodicity. If the inventory position is smaller than safety stock, then ordering materials or products arrives to stock level. It is the mixed system between the Q and the P systems. It avoids continuous reviews and non-meaningful purchase so is particularly attractive when both review and ordering costs are significant.

This work presents the P system in supplier and distributor echelon, Q system in manufacturer echelon, and optional system in retailer echelon, called a (P Q P O) inventory policy, as adopted by one of the largest motherboard manufacturing SC in the world.

## 4. Solution approaches

The agent-based solution approach is presented in Section 4.1, where the multi-agent system architecture is described and different agents, as well as their specific roles are defined. In Section 4.2, a forecasting solution approach is proposed. In addition, how to apply the rough set approach to reduce rules from demand and how to operate a real-coded genetic algorithm including encoding, crossover, and mutation are detailed.

## 4.1. Agent-based solution approach

This paper proposes a multi-agent system to control the ordering quantity for every echelon and find the minimal total cost of the entire supply chain. The system architecture is shown in Fig. 2.

The main purpose of this system is to coordinate all entities of SC and minimize total cost while every entity may use different inventory systems. Each echelon has the same agent architecture, which includes different types of agents. In this research, two types of agents are employed to respond to various types of services for the entire supply chain, for example, control agents and demand forecast agents. These coordinated agents have the ability to specify both static and dynamic characteristics of various supply chain entities [22].

The control agent plays a liaison role between a supply chain manager and the system. It collects historical demand data and strategies from managers and aims at building a rule-base for supply chain management.

The demand forecast agent, which communicates with control agents, plays a role in transforming managers’ experience. In addition, it provides a forecast mechanism, which tries to minimize the total cost for the entire supply chain. In this paper, a mechanism using real-coded genetic algorithm (RGA) is introduced to forecast the optimal solution and determine ordering quantity for every echelon. These ordering quantities minimize total cost for the supply chain. The agent system is autonomous because it allows any manager to change the ordering quantity of that echelon in real time according to recalculation results when the demand of a certain echelon is changed.

![](/api/attachments/WV22FW7T/fulltext/images/c9a8296ca8b559d223005c00b999171faf3fb9d7563b535a1833f9fe461c7439.jpg)  
Fig. 2. System architecture.

## 4.1.1. Control agent

The control agent exchanges information about production status and costs, transportation costs, inventory costs, inventory levels, manufacturing capacities, ordering quantity, and customer demand. In addition, the control agent communicates with the manager and requests information from managers. It also enables the demand forecast agent to recalculate the cost while demand is changed. An inventory system formulation is built with a constraint network.

For example, in Q system,

IP=OH+SR-BO and R (reorder point)=D(average demand during lead time L)+ss.

If IP is smaller than R, then reorder takes place. It implies that a constraint, IP <sup>N</sup> R exists in the Q system. These two formulae are illustrated in Fig. 3.

Constraints are applied to different areas in the supply chain, for example, resource allocation problems, material purchasing problems, production problems, etc [2,15].

The autonomous character of an agent-based system allows managers to perform specific actions to flexibly deal with different problems. For example, the change in demand quantity at a particular echelon leads to an increase in the total cost of the supply chain. In real time, the agent-based system informs the manager at that echelon to change his ordering quantity and pushes the manager to communicate with control agents at other echelons to determine ordering quantity so as to globally minimize the total cost of the supply chain.

![](/api/attachments/WV22FW7T/fulltext/images/5feea9b77379aad47757e3de24bf9beda9720b4df7cb153ee16d9ccd94ec013c.jpg)  
Fig. 3. Constraint network for Q system.

## 4.1.2. Demand forecast agent

After being enabled by the control agent, the demand forecast agent automatically calculates the supply chain’s total cost, determines the optimal ordering quantity for period t + 1, and delivers the message back to each control agent at each echelon. In addition, this agent analyzes historical demands and sends the analytical results to all managers periodically in the supply chain.

For example, in the Q system, four factors including on-hand inventory (OH), scheduled receipts (SR), lead time (L), and backorders (BO) impact on the crossover range when the demand quantity is calculated. The impact on a rule format is shown in Table 2. The data of on-hand inventory (OH), scheduled receipts (SR), lead time (L), and backorders (BO) are collected by the control agents. The crossover range is collected and decided based on managers’ experience. Based on Table 2, rules are inducted by the rough set approach presented in Section 4.2.

The crossover range is dynamic and calculated by RGA in real time. Consequently, these crossover rules are created dynamically to further optimize ordering quantity. These rules are shared with other managers in the supply chain by the control agents.

## 4.2. Forecast method

The control agent collects information, including current on-hand inventory points, scheduled receipts, crossover range from managers, and stores them in the demand rule table. Then, the demand forecast agent applies the induction procedure (presented hereafter) to the demand rule table to obtain the reduct rules. Finally, based on the rules, the GA mechanism calculates the optimal ordering quantity using the crossover range. The solution of the quantity to be ordered at time period t + 1 is sent back to the manager by the control agent. The solution process is illustrated in Fig. 4.

## 4.2.1. Rules induction

Because the crossover range value is dynamically created by the RGA algorithm, how to induct demand rules based on previous large data is difficult. To solve this problem, rough set theory is applied [32] to induct the demand rules from the demand rule table.

The main reason for using the rough sets’ approach for rule induction is due to the qualitative nature of the data, which makes it difficult to analyze by standard statistical techniques. For example, in the Q system, L, OH, SR, and BO have different values for every entity and these factors are deployed through echelons. Therefore, statistical techniques do not consider the impact and are not adapted to this case. To incorporate the rough set approach, factors like L, OH, SR, BO and crossover range, are transformed to input and output features of the rough set, respectively (Table 3). In the demand rule table (Table 2), many experiences are formatted in rules. Each rule in Table 2 corresponds to an object in the decision table (Table 4). Several measure factors composing the rules have been used to evaluate the induced rules, for example,

Table 2  
The demand rule table of Q system

<table><tr><td>Rule</td><td>L</td><td>OH</td><td>SR</td><td>BO</td><td>Crossover range</td></tr><tr><td>1</td><td>0</td><td>20</td><td>10</td><td>0</td><td>[0–20]</td></tr><tr><td>2</td><td>0</td><td>10</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td>3</td><td>1</td><td>20</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr></table>

![](/api/attachments/WV22FW7T/fulltext/images/6816f655b62c64a4b5071ff24219cdc08101bb41d5f2ad3478e6320bbf41a20b.jpg)  
Fig. 4. The solution approach.

L, OH, SR, and BO in the demand rule table of the Q system (Table 3).

## 4.2.2. Induction procedure

According to rough set theory, $I { = \{ U , A \} }$ is an information system, where U is a finite set of objects and Ais a finite set of attributes. To every attribute $a \in$ A, a set of its values $V _ { a }$ is associated. Assume $A { = } C \cup$ $D , B \subset C$ , where Bis a subset of $C ;$ the positive region $\mathrm { P O S } _ { B } ( D ) = \{ x \in U \colon [ x ] _ { B } \subset D \}$ can be defined. The positive region $\mathrm { P O S } _ { B } ( D )$ includes all objects in U which can be classified into classes of D, in the knowledge B. The degree of dependency between B and D can be defined as $\begin{array} { r } { K ( B , D ) = \frac { c a r d ( \mathrm { P } \check { \mathrm { O S } } _ { B } ( D ) ) } { c a r d ( \mathrm { P } \mathrm { O S } _ { C } ( D ) ) } } \end{array}$ , where card yields the set cardinality. In general, if $K ( B , D ) { = } K ( C , D )$ , and $K ( B , D ) \mathcal { H } K ( B - \{ a \} , D )$ , for any $a \in B$ will hold; then B is an induct of C. Since an induct (B) preserves the degree of dependency with respect to D and an induct (B) is a minimal subset, any further removal of condition attributes will change the degree of dependency. The following procedure for determining the inducts and cases is adopted from Ref. [33].

Table 3  
Input and output feature

<table><tr><td colspan="2">Input features</td><td>Output feature (outcome)</td></tr><tr><td> $F_1$ </td><td>Lead time ( $L$ )</td><td>Crossover range</td></tr><tr><td> $F_2$ </td><td>On-hand inventory (OH)</td><td></td></tr><tr><td> $F_3$ </td><td>Scheduled receipts (SR)</td><td></td></tr><tr><td> $F_4$ </td><td>Backorders (BO)</td><td></td></tr></table>

Step 1. Initialization.

Initialize the decision table (Table 4), which is retrieved from the demand rule table and list all objects in it.

Step 2. Generate the inducts for each object for i =1 to n do

Table 4  
Partial decision table

<table><tr><td>Object no.</td><td> $F_1$ </td><td> $F_2$ </td><td> $F_3$ </td><td> $F_4$ </td><td>Crossover range</td></tr><tr><td>1</td><td>0</td><td>20</td><td>10</td><td>0</td><td>[0–20]</td></tr><tr><td>2</td><td>0</td><td>10</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td>3</td><td>1</td><td>20</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td>4</td><td>1</td><td>10</td><td>15</td><td>5</td><td>[10–20]</td></tr><tr><td>5</td><td>0</td><td>25</td><td>10</td><td>0</td><td>[0–10]</td></tr><tr><td>6</td><td>0</td><td>15</td><td>15</td><td>5</td><td>[10–20]</td></tr><tr><td>7</td><td>1</td><td>15</td><td>20</td><td>0</td><td>[10–15]</td></tr><tr><td>8</td><td>0</td><td>20</td><td>10</td><td>0</td><td>[0–20]</td></tr><tr><td>9</td><td>0</td><td>15</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td>10</td><td>0</td><td>15</td><td>10</td><td>5</td><td>[10–20]</td></tr></table>

<table><tr><td>for j=1 to m</td></tr><tr><td>if [Vij]Aj⊂ [Vik]Ok|i where k is the index number of the outcomes.</td></tr><tr><td>then the inducts for Xi is formed</td></tr><tr><td>else for j=1 to m</td></tr><tr><td>if C-Aj[Vij]Aj⊂ [Vik]Ok|i</td></tr><tr><td>then the inducts for Xi is formed</td></tr><tr><td>else the inducts for Xi is not formed</td></tr><tr><td>end for</td></tr><tr><td>end for</td></tr><tr><td>end for</td></tr></table>

Step 3. Termination: stop and make outputs of the results

Note that the $X \in U ,$ where U is a finite set of objects. $[ V _ { i j } ] A _ { j }$ represents the objects where each $A _ { j }$ attribute contains $V _ { i j } ,$ while $[ V _ { i k } ] o _ { i j }$ includes the objects with each $O _ { k | i }$ outcome (decision) attribute containing $V _ { i k } .$ . Represents the condition domain $C -$ condition attribute $A _ { j } .$ . After the aforementioned three steps, the rules are inducted as follows (Table 5).

The reduct rules generated with the rough set approach are used to constrain the crossover range of the RGA evolution process.

## 4.3. RGA forecasting method

Traditional forecasting methods, for example, simple moving-averages, moving-average model and Winter’s exponential, are based on large previous data and forecast the demand of period t + 1 without considering the total supply chain cost at period t. In order to solve this problem, a heuristic approach, e.g., the genetic algorithm (GA), is required. This is because large data are not required and the minimal total cost is simply the objective function in GA. In genetic code format every bit represents a demand order for each entity. Consequently, the demand order of every entity is considered during the evolution process and total cost control in the supply chain is optimized globally.

## 4.3.1. Representation

The proposed genetic algorithm is based on the floating-point representation and two genetic operators: crossover and mutation. In the floating-point representation, each chromosome vector is coded as a vector of floating point number of the same length as the solution vector. Each entity is initially selected so

Table 5

<table><tr><td colspan="6">Reduct rule table</td></tr><tr><td>Object no.</td><td> $F_1$ </td><td> $F_2$ </td><td> $F_3$ </td><td> $F_4$ </td><td>Crossover range</td></tr><tr><td rowspan="2">1</td><td>0</td><td>20</td><td>X</td><td>X</td><td>[0–20]</td></tr><tr><td>X</td><td>20</td><td>10</td><td>X</td><td>[0–20]</td></tr><tr><td rowspan="4">2</td><td>X</td><td>10</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td>0</td><td>X</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td>0</td><td>10</td><td>X</td><td>0</td><td>[10–15]</td></tr><tr><td>0</td><td>10</td><td>15</td><td>X</td><td>[10–15]</td></tr><tr><td>3</td><td>X</td><td>X</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td rowspan="2">4</td><td>X</td><td>X</td><td>X</td><td>5</td><td>[10–20]</td></tr><tr><td>X</td><td>X</td><td>15</td><td>5</td><td>[10–20]</td></tr><tr><td>5</td><td>X</td><td>25</td><td>X</td><td>X</td><td>[0–10]</td></tr><tr><td rowspan="2">6</td><td>X</td><td>X</td><td>X</td><td>5</td><td>[10–20]</td></tr><tr><td>X</td><td>X</td><td>15</td><td>5</td><td>[10–20]</td></tr><tr><td rowspan="2">7</td><td>X</td><td>X</td><td>20</td><td>X</td><td>[10–15]</td></tr><tr><td>X</td><td>15</td><td>X</td><td>0</td><td>[10–15]</td></tr><tr><td rowspan="2">8</td><td>0</td><td>20</td><td>X</td><td>X</td><td>[0–20]</td></tr><tr><td>X</td><td>20</td><td>10</td><td>X</td><td>[0–20]</td></tr><tr><td>9</td><td>X</td><td>X</td><td>15</td><td>0</td><td>[10–15]</td></tr><tr><td>10</td><td>X</td><td>X</td><td>X</td><td>5</td><td>[10–20]</td></tr></table>

Rule 1: IF the Lead time is 0 and On-hand inventory is 20 THEN crossover range is [0–20]  
Rule 2: IF the On-hand inventory is 20 and Scheduled receipts is 10 THEN crossover range is [0–20]  
Rule 3: IF the On-hand inventory is 10 and Scheduled receipts is 15 and Backorders is 0 THEN crossover range is [10–15]  
Rule 4: IF the Lead time is 0 and Scheduled receipts is 15 and Backorder is 0 THEN crossover range is [10–15]

Rule 5: IF the Lead time is 0 and On-hand inventory is 10 and Backorder is 0 THEN crossover range is [10–15]

Rule 6: IF the Lead time is 0 and On-hand inventory is 10 and Scheduled receipts is 15 THEN crossover range is [10–15]

Rule 7: IF the Scheduled receipts is 15 and Backorder is 0 THEN crossover range is [10–15]

Rule 8: IF the Backorder is 5 THEN crossover range is [10–15]

Rule 9: IF the Scheduled receipts is 15 and Backorder is 5 THEN crossover range is [10–20]

Rule 10: IF the On-hand inventory is 25 THEN crossover range is [0–10]

Rule 11: IF the Scheduled receipts is 20 THEN crossover range is [10–15]

Rule 12: IF the On-hand inventory is 15 and Backorder is 0 THEN crossover range is [10–15]

Rule 13: IF the Backorder is 5 THEN crossover range is [10–20]

as to be within the desired domain, and the operators are carefully designed to preserve the constraint. The precision of such an approach depends on the underlying machine, but is generally much better than that of binary representation [28]. In addition, the floatingpoint representation is capable of representing quite large domains. That is, binary representation sacrifices precision with an increase in domain size, given fixed binary length. Also, in the floating-point representation, it is much easier to design special tools for handling nontrivial constraints.

The chromosome of the example in Fig. 5 is represented with a 4-bit floating string. It is represented as (30 35 40 45), where 30 is the demand order for the supplier; 35 is the demand order for the manufacturer; 40 is the demand order for the distributor; 45 is the demand order for the retailer.

## 4.3.2. Fitness function

In GA, a fitness function determines what the best chromosome is in all generations and decides when to stop evolution. The proposed fitness object function uses the cost function. Based on Ref. [16], each entity has an ordering cost, an inventory holding cost and a transportation cost. The total cost of the supply chain after M periods (e.g., weeks) is formulated as follows:

$$
\mathrm{TC} _ {\mathrm{chain}} = \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {M} c _ {i} (t)\tag{i}
$$

$$
\begin{array}{r l} c _ {i} (t) = & \left[ \text { ordering   cost } + \text { inventory*   holding   cost } \right. \\ & \left. + \text { transportation   cost } + \text { shortage   cost } \right] \end{array}
$$

$$
c _ {i} (t) = \left[ \mathrm{Oc} _ {i} + \operatorname{In} _ {i} (t) ^ {*} h _ {i} + \mathrm{Tc} _ {i} + \mathrm{Sc} _ {i} \right]\tag{ii}
$$

where $\mathrm { T C } _ { \mathrm { c h a i n } } \mathrm { : }$ total cost of supply chain; N: number of supply chain entities; i: index of supply chain entity, $i = 1 , 2 , . . . , n ; c _ { i } ( t ) :$ : cost of entity i at period $t ; \mathrm { O c } _ { i } { \mathrm { : } }$ ordering cost of entity i per period; $\operatorname { I n } _ { i } \colon$ inventory quantity of entity i at period $t ; h _ { i } \colon$ inventory holding cost of entity i, per unit, per period.; $\operatorname { T c } _ { i } \colon$ transportation cost of entity i per period.; $\operatorname { S c } _ { i } { \mathrm { : } }$ shortage cost of entity i per period.

## 4.3.3. Crossover

Two parents $x = ( x _ { 1 } , . . . , x _ { n } )$ and $y = ( y _ { 1 } , . . . , y _ { n } )$ produce an offspring $z = ( z _ { 1 } , . . . . , z _ { n } ) .$ , where $z _ { i } = x _ { i }$ or $z _ { i } = y _ { i }$ with equal probability, called crossover probability for all $i { = } 1 , 2 , . . . . , n$ , and the second offspring is created by reversing all bits

## 4.3.4. Mutation

Mutation is defined in a traditional way: if $x _ { i } ^ { t } { = } ( \mathrm { v } _ { 1 }$ $\cdots ^ { } ( \cdot ^ { } \cdot ^ { } ) ^ { }$ is a chromosome, then each element $\nu _ { k }$ has an exactly equal chance of undergoing the mutation process. The result of a single application of this operator produces a vector $\left( \mathrm { v } _ { 1 } , . . . . , \mathrm { v k } ^ { \prime } , . . . . , \mathrm { v _ { n } } \right)$ with $1 \leq \mathbf { k } \leq \mathbf { n }$ , and $\mathbf { v } _ { \mathrm { k } } ^ { \prime } ,$ a random value from the domain of the corresponding parameter domain . That is, if domain is a closed interval $[ l _ { k } , \ u _ { k } ] .$ , then $\nu _ { k } ^ { \prime }$ is generated from the uniform distribution $U ( l _ { k } , ~ u _ { k } )$ [28].

## 4.3.5. Evolution process

In this evolution process, two agents are used: 1) the demand forecast agent’s GA mechanism applies the real-coded genetic algorithm (RGA) to calculate the optimal ordering quantity; 2) the demand forecast agent delivers results to the control agent and managers. The real-coded algorithm is described as follows:

Step 1. Initialization. Generate a population of size |P| (the number of size is defined by the user), and each chromosome has four genes, whose value was randomly generated from range [0, X]. X is a predefined value of the probably great number of order quantity in each echelon. The chromosome is formatted in Fig. 5.

Format

<table><tr><td></td><td>Supplier</td><td>Manufacturer</td><td>Distributor</td><td>Retailer</td></tr><tr><td>Parent 1</td><td>10</td><td>15</td><td>20</td><td>25</td></tr><tr><td>Parent 2</td><td>18</td><td>25</td><td>30</td><td>42</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr></table>

Fig. 5. Chromosome format.

Step 2. Evaluation. Evaluate each population member of [ P] according to the fitness function that is the total cost function.

Step 3. Selection. Select part of [ P] using the roulette wheel method [12] according to the fitness function.

Step 4. Crossover. Crossover each two members of the selected part of [ P] in turn to form a new population member with the constraints of the crossover range. The crossover range is collected by the reduct rules presented in Section 4.2. Crossover the pair with the crossover probability and place two child strings into the new population. The cutting point for exchange is randomly selected for each quantity. In this example (Fig. 5), the crossover rate is 0.7. A simple crossover method is described in Fig. 6. The cutting point is selected between supplier and manufacturer. The crossover part includes three elements: Manufacturer, Distributor, and Retailer. Reduct rules in Table 5, for example, rule 10 and rule 12 are matched corresponding to Manufacturer and Retailer. Distributor is not. Therefore, Manufacturer and Distributor’s crossover occur but Retailer’s crossover is ignored because its range is 17, which is out of the constraint range [0–10].

Step 5. Mutation. Mutate the child strings with the mutation probability and place them into the new population. The chromosome is randomly selected and its value is changed based on previous rules. In the example of Fig. 5, the mutation rate is 0.005 and the range is [S, ss], where S is the stock level and ss is a safety stock. The mutation method is described in Fig. 7.

![](/api/attachments/WV22FW7T/fulltext/images/d6edad57a775bf7ab53ab9e030e0ab8b5c3d5e0f6bc03ef69bb957b5db83f9bb.jpg)  
Fig. 7. Mutation method.

Step 6. Repeat Step 2–5 iteratively until the population converges, no better chromosome is found, or time is out. The optimal order quantity is then found, for example, the final chromosome is represented as (30 35 40 45), where 30 is the demand order for the supplier; 35 is the demand order for the manufacturer; 40 is the demand order for the distributor; 45 is the demand order for the retailer.

## 5. Validation of solution approaches

## 5.1. Scenario design

The example is illustrated and based on the proposed approach against different forecasting scenario. Four MBA students play the Beer Game with the roles of supplier, manufacturer, distributor, and retailer. Each one uses a different inventory system to control his inventory. The ordering quantity and the total cost of the supply chain is aggregated through all four echelons. Based on the type of inventory system, current stock, and current total cost, the forecast demand agent of each echelon determines its ordering quantity with the RGA mechanism such that global minimal total cost for the next period is determined.

<table><tr><td></td><td>Supplier</td><td>Manufacturer</td><td>Distributor</td><td>Retailer</td></tr><tr><td>Parent 1</td><td>10</td><td>15</td><td>20</td><td>25</td></tr><tr><td>Parent 2</td><td>18</td><td>25</td><td>30</td><td>42</td></tr><tr><td colspan="2">Crossover ranges</td><td>[10 -15]</td><td>No matched</td><td>[0 -10]</td></tr><tr><td>offspring1</td><td>10</td><td>25</td><td>30</td><td>25</td></tr><tr><td>offspring2</td><td>18</td><td>15</td><td>20</td><td>42</td></tr></table>

Fig. 6. Crossover method.

The market is assumed steady in this model and the market demand is formulated as follows: $u _ { D } + \mathrm { I n t } ( - 1 / $ $1 ^ { * } \mathrm { L o g } ( U ) )$ , where $u _ { D }$ is the mean demand and U is a random number. $\mathrm { I n t } ( - 1 / 1 ^ { * } \mathrm { L o g } ( U )$ is the mathematical transformations often used for stabilizing variation [25]. The lead time is set to one week. The additional assumptions in each echelon are made:

<sup>!</sup> Backorder cost: zero, backorder is not allowed and amounts of inventory are always positive.

<sup>!</sup> Ordering cost: depends on the ordering quantity per period.

<sup>!</sup> Holding cost: depends on the quantity of on-hand inventory.

<sup>!</sup> Transportation cost: depends on the ordering quantity.

<sup>!</sup> Shortage cost: depends on the shortage quantity.

The real-coded genetic algorithm is coded with Matlab 6.0R. The upper generation is 100, the crossover rate 0.7, and the mutation rate 0.005. The unit costs of inventory holding cost, ordering cost, transportation cost, and shortage cost are assumed in Table 6.

## 5.2. Scenario 1: RGA vs. MBA students

Four MBA students play the SCM model (Fig. 1) with the roles of supplier, manufacturer, distributor, and retailer. Each one uses a different inventory system to control his inventory. The ordering quantity and the supply chain’s total cost is aggregated through all four echelons.

On the other hand, agents replace the students to play the same game. The control agent collects inventory information from local sites and enables the demand forecast agent to calculate an optimal ordering quantity with the RGA mechanism. The agents coordinate with each other by sharing information. The process of crossover and mutation are coded with Matlab 6.0, where $x _ { 1 , } \ x _ { 2 } , \ x _ { 3 } ,$ and $x _ { 4 }$ correspond to ordering quantities of retailer, distributor, manufacturer, and supplier, respectively. The minimal total costs are found and the algorithm terminated at the 68th generation.

Table 6  
Unit cost of supply chain entity

<table><tr><td></td><td>Supplier</td><td>Manufacturer</td><td>Distributor</td><td>Retailer</td></tr><tr><td>Unit inventory holding cost ($)</td><td>4</td><td>3</td><td>2</td><td>2</td></tr><tr><td>Unit ordering cost ($)</td><td>1</td><td>1</td><td>2</td><td>2</td></tr><tr><td>Unit transportation cost ($)</td><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td>Shortage cost ($)</td><td>4</td><td>3</td><td>2</td><td>3</td></tr></table>

Agent is compared to MBA students and the result is presented in Fig. 8. Agent lowers the total cost of the supply chain without any shortage of stock. Fig. 9 shows the difference, called ordering variation between ordering quantity of P, Q, O systems and actual demand, for each week. Fig. 10 is the result corresponding to agent.

The MBA students are not allowed to get any information from other entities of the supply chain, for example, what types of inventory systems are used by other entities. The MBA students play the game and control their inventory intuitively. Consequently, the ordering quantity variability is amplified as it moves up the supply chain. Simultaneously, the total cost accumulates increasingly and a series of inventory shortages occur.

Consequently, the inventory systems’ sequence in the SC has no impact on the total cost. That is, when the MBA students play the game and control their inventory without communication and sharing information with each other, the total cost is not different.

On the other hand, the real-coded genetic algorithm (RGA) forecasts the optimal ordering quantity for period t + 1 with the sharing of information, for example, inventory quantity and crossover range. Given a population size of 100, a better policy (25, 12, 10, 5) at the 68th generation is reached. The comparison results can be summarized as follows:

<sup>!</sup> In Fig. 8, the total cost in the agent-based solution approach is 10% lesser than in the MBA students experiment.

<sup>!</sup> That ordering variation is very turbulent in MBA students, especially in the supplier and manufacturing entity. The bullwhip effect exists in the MBA students’ experiment. However, this turbulent situation is solved by the agent-based solution approach and the bullwhip is reduced.

![](/api/attachments/WV22FW7T/fulltext/images/06b3e9d65f0da0a2c5c9460cc89b537a4932e374d1d83de76278f71ed12e02c2.jpg)  
Fig. 8. Total cost curve of Agent vs. MBA students.

<sup>!</sup> In Fig. 10, the ordering variation of agent is smoother than of the ordering variation of MBA students (Fig. 9). That is, the result of forecasting with the proposed solution approach is very close to the market’s demand.

## 5.3. Scenario 2: RGA vs. moving-average forecasting model

To compare with the agent-based forecasting method, we introduce one of the conventional forecasting methods—the moving-average forecasting model. Of the quantitative techniques, the movingaverage is the most popular technique for short range and medium-range forecasts and the most popular for forecasting product line and product family sales [36]. The estimate is an excellent one (Average Forecasting Procedure) if the process is entirely steady [11]. Because of a natural reluctance to use very old data, this procedure is generally limited to young processes [11]. Rather than using very old data that may no longer be relevant, this procedure (Moving-Average Forecasting Procedure) averages the data for only the last n periods as the forecast for the next period. The moving-average estimator combines the advantages of the last value and average estimators in that it uses only recent history and multiple observations [11]. The assumption of steady market in this case is only suitable for using moving-average forecasting method.

![](/api/attachments/WV22FW7T/fulltext/images/29e17e9de0c36c96662a366f58f92b945d1d8eb5a71122b11b6633a24bed183e.jpg)  
Fig. 9. The ordering variation of MBA students.

![](/api/attachments/WV22FW7T/fulltext/images/980ccfef43ab441a9f6beef22b45ec800f1d6003310cbe73a9f57bd05bd04601.jpg)  
Fig. 10. The ordering variation of Agent.

The experimental result is presented in Fig. 11. The moving-average demand forecast method is calculated by using data from the last 5 periods. The safety stock is set to be 20 units for all 4 echelons, as in the beer game. When the inventory is lower than safety stock, the ordering quantity of the next period is added by the variance between safety stock and inventory level.

Fig. 11 shows that the total cost of the movingaverage method is higher than that of agent.

## 5.4. Scenario 3: RGA vs. exponential-smoothing forecasting model

In this section, another conventional forecasting method—exponential-smoothing forecasting is introduced. The experimental result is presented in Fig. 12. Accordingly, Fig. 12 shows that the total cost of the exponential-smoothing method is higher than that of agent. Fig. 13 includes all four different forecasting methods; agent has the best results.

![](/api/attachments/WV22FW7T/fulltext/images/3580f5a1bbc78d7c7077ba72a2db5eb54c4cef0ef8379eadb868c19c7776ff69.jpg)  
Fig. 11. Total cost curve of Agent vs. Moving-Average forecasting method.

![](/api/attachments/WV22FW7T/fulltext/images/ea698bac8eb62482eb8696855f8656b512abe87d4be36cf12d1fdae36d7292bf.jpg)  
Fig. 12. Total cost curve of Agent vs. Exponential-Smoothing forecasting method.

## 5.5. Discussion

The above example is illustrated and compared with four forecasting methods: RGA; MBA students; moving-average; exponential-smoothing. The experimental results indicate that the RGA performs the best in controlling total cost and ordering variation based on (P Q P O) inventory policy. Although the example has demonstrated the superiority of the proposed approach over conventional forecasting methods, the extent to which the sequence of inventory policy impacts the total cost must be more thoroughly evaluated.

Several specimens have been tested to evaluate the convergence of RGA. The results show good convergence but further details need to be implemented in testing the proposed RGA for stability and convergence.

![](/api/attachments/WV22FW7T/fulltext/images/5ead4798934a74e69da36a906096c2a54db5e7cdb8f46fb23e5d197218ee5a9a.jpg)  
Fig. 13. Total cost curve of Exponential-Smoothing, Moving-Average, Agent and MBA Students.

## 6. Conclusions

In this paper, a solution was developed to forecast the ordering quantity for period t + 1 in a multiechelon supply chain, where every entity was allowed to use different inventory systems. A constraint network was proposed and incorporated with agent technology to coordinate the supply chain. It adapted to environmental changes dynamically and modeled different management behaviors and systems. In addition, the paper used rough set theory to explore and induct the manager’s experience into rules. These rules were shared between supply chain entities. With the rules, the RGA approach is applied to forecast the optimal ordering quantity. Based on experimental results, this approach shows great promise in searching for a desired demand ordering quantity and globally optimizes the total cost of the supply chain. The novel contributions of the paper are summarized as follows:

<sup>!</sup> Allowing for various entities at different echelons using different inventory systems and forecasting the ordering quantity accurately as well as minimizing shortage of inventory; consequently, the total cost of a supply chain is reduced;

<sup>!</sup> Sharing information between entities of a supply chain and coordinating every entity of SC; consequently, optimization can be achieved more effectively and the bullwhip effect is reduced.

<sup>!</sup> Exploring and transforming managers’ experience into rules, this leads to a more accurate and effective inventory control by reusing the explicit rules.

The framework of this study assumes that information is shared truthfully in all entities. Therefore, the proposed method can only be applied when the supply chain partners have well aligned objectives and there is a trusting relationship among agents. In real world coordination, sharing information truthfully is problematic since intra-organizational trust cannot be easily developed. Increasing the transparency of information requires enhancing the relationship of suppliers and purchasers and collaborates with information technology. Additionally, future research has numerous challenges.

<sup>!</sup> Managers’ resistance to change. Sometimes it is difficult for managers to change the inventory policy. Often, managers establish their inventory policy by planning, or according to their experience. Although this approach may generate a better solution, the bullwhip effect exists in the supply chain due to the resistance to change by managers.

<sup>!</sup> Difficulty in capturing tacit knowledge. It is difficult for managers to share tacit knowledge. Besides, by the induction of rules with the rough set theory, how to effectively capture and externalize managers’ knowledge is an important issue.

<sup>!</sup> More entities in the same echelon. The paper just assumes a single entity in an echelon of a supply chain. The number of entities at the same echelon can be increased and with the new network, further study is required.

## Acknowledgment

This work was partially supported by funding from the Nation Science Council of the Republic of China (NSC 93-2416-H-260-004, NSC 93-2416-H-018-013).

## References

[1] M. Barbuceanu, M.S. Fox, Integrating communicative action, conversations and decision theory to coordinate agents, Proceeding of Autonomous Agents 97 (1997) 49–58.

[2] J.C. Beck, M.S. Fox, Supply chain coordination via mediated constraint relaxation, Proceeding of the First Canadian Workshop on Distributed Artificial Intelligence, 1994 (May).

[3] R. Bruns, Integration of constraint solving techniques in genetic algorithms, IEEE International Conference on Evolutionary Computation, Perth, WA, Australia, vol. 1, 1995, pp. 33– 38.

[4] F. Chen, Z. Drezner, J.K. Ryan, D. Simchi-Levi, Quantifying the bullwhip effect in a simple supply chain: the impact of forecasting, lead times, and information, Management Science 46 (3) (2000) 436–443.

[5] F. Chen, Z. Drezner, J.K. Ryan, D. Simchi-Levi, The impact of exponential smoothing forecasts on the <sup>b</sup>bullwhip<sup>Q</sup> effect, Naval Research Logistics 47 (2000) 269–286.

[6] L. Christine, M. Michael, Forecasting tourist arrivals, Annals of Tourism Research 28 (2001) 965– 977.

[7] Y. Fu, R.D. Souza, J. Wu, Multi-agent enabled modeling and simulation towards collaborative inventory management in supply chain, in: J.A. Joines, R.P. Barton, K. Kang, P.A. Fishwick (Eds.), Proceedings of the 2000 Winter Simulation Conference, 2000, pp. 1763–1771.

[8] S. Gavirneni, R. Kapuscinski, S. Tayur, Value of information in capacitated supply chains, Management Science 45 (1) (1999) 16– 24.

[9] I. Gutiı´nez Martı´nez, R.E. Bello Pe´rez, Making decision in case-based systems using probabilities and rough sets, Knowledge-Based System 16 (2003) 205– 213.

[10] D. Han, I.G. Kwon, M. Bae, H. Sung, Supply chain integration in developing countries for foreign retailers in Korea: Wal-Mart experience, Computers & Industrial Engineering 43 (2002) 111 –121.

[11] F.S. Hiller, G.J. Lieberman, Introduction to Operations Research, Mc-Graw Hill, New York, 1990, p. 810.

[12] J.H. Holland, Adaptation in Natural and Artificial Systems, MIT Press, Boston, 1992.

[13] X. Jin, R.G. Reynolds, Using knowledge-based evolutionary computation to solve nonlinear constraint optimization problems: a cultural algorithm approach, Proceedings of the 1999 Congress on Evolutionary Computation (CEC 99), Washing ton, DC, USA, vol. 3, 1999, pp. 1672– 1678.

[14] X. Jin, R.G. Reynolds, Using knowledge-based system with hierarchical architecture to guide the search of evolutionary computation, Proceedings of the 11th IEEE International Conference on Tools with Artificial Intelligence, Chicago, IL, USA, 1999, pp. 29– 36.

[15] R. Kalakota, J. Stallaert, A.B. Whinston, Implementing realtime supply chain optimization system, Proceedings of the Conference on Supply Chain Management, October, Hong Kong, 1995.

[16] S.O. Kimbrough, D.J. Wu, F. Zhong, Computers play the beer game: can artificial agents manage supply chains? Decision Support Systems 33 (2002) 323– 333.

[17] L.J. Krajewski, L.P. Ritzman, Operations Management: Strategy and Analysis, Prentice Hall, New Jersey, 2002.

[18] A. Kusiak, Rough set theory: a data mining tool for semiconductor manufacturing, IEEE Transactions on Electronics Packaging Manufacturing 24 (1) (2001) 44– 50.

[19] H.L. Lee, C. Billington, Managing supply chain inventory: pitfalls and opportunities, Sloan Management Review 33 (3) (1992) 65– 73.

[20] H.L. Lee, C. Billington, Material management in decentralized supply chains, Operations Research 41 (5) (1993) 835– 847.

[21] H.L. Lee, S. Whang, Decentralized multi-echelon supply chains: incentives and information, Management Science 45 (5) (1999) 633– 640.

[22] H.L. Lee, V. Padmanabhan, S. Whang, The bullwhip effect in supply chains, Sloan Management Review 38 (3) (1997) 93– 102.

[23] K.J. Lee, Y.S. Chang, J.K. Lee, Time-bound negotiation framework for electronic commerce agents, Decision Support Systems 28 (4) (2000) 319–331.

[24] H.L. Lee, K.C. So, C.S. Tang, Value of information sharing in two-level supply chain, Management Science 46 (5) (2000) 626– 643.

[25] S. Makridaskis, S.C. Wheelwright, R.J. Hyndman, Forecasting Methods and Application, John Wiley & Sons, New York, 1998.

[26] P. McBurney, S. Parsons, J. Green, Forecasting market demand for new telecommunications services: an introduction, Telematics and Informatics 19 (2002) 225– 249.

[27] Z. Michalewicz, Genetic Algorithm+Data Structures=Evolution Program 3rd, Springer, New York, 1996.

[28] Z. Michalewicz, M. Schoenauer, Evolutionary algorithm for constrained parameter optimization problems, Evolutionary Computation 4 (1996) 1 –32.

[29] H. Min, G. Zhou, Supply chain modeling: past, present and future, Computers & Industrial Engineering 43 (2002) 231– 249.

[30] S.J. New, P. Payne, Research frameworks in logistics: three models, seven dinners and a survey, International Journal of Physical Distribution and Logistics Management 25 (10) (1995) 60–77.

[31] M. Olhofer, Y. Jin, B. Sendhoff, Adaptive encoding for aerodynamic shape optimization using evolution strategies, Proceedings of the 2001 Congress on Evolutionary Computation, Seoul, South Korea, vol. 1, 2001, pp. 576–583.

[32] Z. Pawlak, Rough sets, Information and Computer Science 11 (5) (1982) 341– 356.

[33] Z. Pawlak, Rough Sets, Kluwer Academic Publishers, Dordrecht, The Netherlands, 1991.

[34] F. Questier, I. Rollier, B. Walczak, D.L. Massart, Application of rough set theory to feature selection for unsupervised clustering, Chemometrics and Intelligent Laboratory Systems 63 (2) (2002) 155– 167.

[35] T. Reutterer, H.W. Kotzab, The use of conjoint-analysis for measuring preferences in supply chain design, Industrial Marketing Management 29 (2000) 27– 35.

[36] N.R. Sanders, K.B. Manrodt, Forecasting practices in US corporations: survey results, Interfaces 24 (2) (1994) 92 – 99.

[37] C. Scott, R. Westbrook, New strategic tools for supply chain management, International Journal of Physical Distribution and Logistics Management 21 (1) (1991) 23– 33.

[38] P.M. Senge, The Fifth Discipline, Doubleday/Currency, New York, 1990.

[39] D. Simchi-Levi, P. Kaminsky, E. Simchi-Levi, Designing and Managing the Supply Chain Concepts, Strategies, and Case Studies, McGraw-Hill, Boston, 2000.

[40] J.M Swaminathan, S.F. Smith, N.M. Sadeh, Modeling supply chain dynamics: a multiagent approach, Decision Sciences 29 (3) (1998) 607– 632.

[41] S. Umeda, A. Jones, An integration test-bed system for supply chain management, in: D.J. Medeiros, E.E. Watson, J.S. Carson, M.S. Manivannan (Eds.), Proceedings of the 1998 Winter Simulation Conference, 1998, pp. 1377– 1385.

[42] P.R. Winters, Forecasting sales by exponentially weight moving averages, Management Science 6 (3) (1960) 324– 342.

[43] S.K. Yung, C.C. Yang, A new approach to solve supply chain management problem by integrating multi-agent technology and constraint network, Proceeding of the 32nd Hawaii International Conference on System Sciences, USA, 1999, pp. 1 –10.

[44] X. Zhao, T.S. Lee, Freezing the master production schedule in multilevel material requirements planning systems under demand uncertainty, Journal of Operations Management 11 (1993) 185 – 205.

[45] X. Zhao, J. Xie, J. Leung, The impact of forecasting model selection on the value of information sharing in a supply chain, European Journal of Operational Research 142 (2002) 321– 344.

![](/api/attachments/WV22FW7T/fulltext/images/93a6b22e369bd0faf00ca38c251e57a23c6c29a02ec022bb0693cd0017497a2f.jpg)

Wen-Yau Liang is associate professor of Information Management at National Changhua University of Education. He received his Ph.D. from the University of Iowa in 1998. His research interests are remote collaborative design for modular products, distributed design, object-oriented design, product visualization, and electronic commerce. He has published papers in Computer Aided Design, Computer Integrated Manufacturing System,

Computers in Industry, International Journal of Information Management, Concurrent Engineering, Computerized Medical Imaging and Graphics, Computer Standards and Interfaces, Journal of Intelligent Manufacturing, and International Journal of Computer Integrated Manufacturing.

![](/api/attachments/WV22FW7T/fulltext/images/218beb5700f3493ae4a554715eea9584e08d30a6b8d53c08c9bb72f7abc0d157.jpg)

Chun-Che Huang received his Ph.D. degree in Industrial Engineering from the University of Iowa, Iowa City, and his M.S. degree in Operations Research from Columbia University, New York, NY. He is a Professor in the Department of Information Engineering, National Chi-Nan University, Taiwan and directs the Laboratory of Intelligent Systems and Knowledge Management (ISKM Lab). He is interested in intelligent systems, development of modu-

lar products and systems, knowledge management, and concurrent engineering. He has published research papers in journals sponsored by various societies.
