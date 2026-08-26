---
otero_id: 12378
otero_key: "QQZ4EXG3"
title: "A DSS to manage platelet production supply chain for regional blood centers"
authors: "Parviz Ghandforoush; Tarun K. Sen"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.06.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS to manage platelet production supply chain for regional blood centers

Parviz Ghandforoush <sup>a,</sup>⁎, Tarun K. Sen <sup>b,1</sup>

<sup>a</sup> Business Information Technology, Virginia Polytechnic Institute and State University, 7054 Haycock Road, Suite 341, Falls Church, VA 22043, United States <sup>b</sup> Accounting and Information Systems, Pamplin College of Business, 7054 Haycock Road, Virginia Tech, Falls Church, VA 22043, United States

## a r t i c l e i n f o

Article history: Received 16 January 2009 Received in revised form 4 June 2010 Accepted 18 June 2010 Available online 30 June 2010

Keywords: Platelet supply management DSS Integer nonlinear programming Blood bank DSS

## a b s t r a c t

This paper presents a prototype decision support system for platelet production and blood mobile scheduling for a regional blood center. Unlike whole blood cells, platelets have a very short shelf life, which requires matching demand and supply closely. This is achieved by an ef<sup>fi</sup>cient supply chain DSS that is optimized for delivery of platelets from production centers to transfusion centers, typically hospitals. One of the critical elements of the DSS is an embedded non-convex integer optimization model that assists the regional blood center manager to schedule the shuttle transportation of whole blood from collection sites to the regional processing center. The proposed non-convex integer model is transformed to a linear 0–1 problem using a two-step conversion process. The transformed model is successfully solved and the optimal solution is reached for the test data. An application of the integrated DSS using data from a regional blood center is described. The results suggest that the proposed DSS better meets the daily demand by producing a superior production plan and mobile assignment schedule.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Blood, a living tissue, carries nutrients to and waste away from all parts of the body. Some of the components of blood are red and white blood cells, platelets, coagulation factors, and plasma. Many of these components of whole blood can be mechanically separated. Since each component is used to meet a different patient transfusion need, one unit or pint of whole blood can be divided into two to <sup>fi</sup>ve different component products. Different components prepared from a single unit are then transfused into different patients.

Platelets are a very important component of today's therapies including those related to bone marrow transplants, chemotherapy, radiation treatment and organ transplants [36]. Unlike whole blood, platelets have a very short shelf life, typically 5 days, and sometimes extendable to 7 days [18]. This necessitates a close matching of platelet collection from donors and the subsequent transfusion demand for platelets at hospital centers. Platelets are usually separated from whole blood collected from multiple donors and are a relatively low yield process. Through a technique called apheresis it can be directly collected from a single donor increasing yield, however the process is time consuming and expensive. In either case, the availability and ef<sup>fi</sup>cient use of platelets are critical to health services. Shortages and wastages carry substantial costs.

An effective supply chain system, coupled with an optimized blood mobile scheduling system can enhance the matching of supply and demand for platelets. Rautonen's [32] study on the Finnish Red Cross Blood Service identi<sup>fi</sup>es three components of an ef<sup>fi</sup>cient supply chain for blood supply: cost ef<sup>fi</sup>cient and reliable, manage blood delivery according to hospital needs, and optimized internal management of the blood supply system. In this paper we describe a prototype supply chain system integrated with a decision support component that streamlines the supply of blood for platelet production at regional blood bank centers. The matching of demand and collection of blood coupled with an optimized bloodmobile transportation schedule shows a marked improvement in the overall costs of production of platelets.

Analytical decision models have been used extensively to solve problems of blood management. In particular, models have been developed to study two distinct management problems, i.e., the hospital blood bank operation and the regional blood center operation. At the hospital level the majority of the research has been directed toward a) forecasting the stochastic demand and supply functions for blood [4,9,11,13,21,33] and b) setting standard hospital inventory levels [2,5–7,14,17,19,20,27]. Other research includes the development of information systems and decision support systems to better manage the information related to the distribution of blood groups among the donors and recipients and the inventory levels of each blood type [3,24,25].

At the regional blood center level, although operational functions are more complex than that of a hospital blood bank, the primary concerns remain the same, i.e., forecasting demand and supply, and determining blood inventory levels. Outdates and shortages of blood continue to be a problem. In 2006, 492 hospitals cancelled elective surgery on one or more days due to blood inventory shortages, ultimately affecting 412 patients [36]. Matching supply and demand is an especially challenging task for platelets due to their short shelf life. In 2006, 22% of the platelets produced were outdated [36].

Additionally, blood centers are concerned with the scheduling of bloodmobiles and the distribution of blood to regional hospitals to match likely demand of platelets to supply. Very little research has been reported addressing the operational functions of the regional blood center [31]. Prastacos [29,30] and Federgruen et al. [12] examined the distribution scheduling problems, while Cumming et al. [9] developed a collection planning model to assist the blood center management in reducing imbalances in both supply and demand of blood using a Markovian population model.

## 2. The supply chain for platelet collection and transfusion

Blood is collected at regional blood centers, hospital blood banks and bloodmobiles. Bloodmobiles are sent out each morning from a central location to geographically dispersed donor sites. Annual blood collections in the U.S. are estimated to be 16 million units, some of which are converted into approximately 13 million units of platelet concentrates [36].

Platelet concentrates are the most perishable and the most expensive component produced from whole blood. On an average platelets derived from whole blood costs \$84 per unit and apheresis platelets are considerably more expensive at \$538 per unit. Platelets expire in 5 days, while red blood cells expire in 35 days and fresh frozen plasma and cryoprecipitate expire in one year. Due to the production expense and the limited life span of platelet concentrates, it is not possible or practical to build large inventories during periods of low demand or when the supply of donors is high. As a result, production must closely mirror demand and large blood centers attempt to minimize platelet production costs.

The production of platelet concentrates is the driving force behind overall component production costs. This is a result of several factors. The 6-hour limit on the separation of platelet-rich plasma from red blood cells necessitates periodic shuttling of blood back to the blood center prior to the return of the bloodmobiles. If platelets are not produced and only fresh frozen plasma and cryoprecipitate are produced the number of shuttles would be greatly reduced. The short life span of platelets imposes the requirement to produce platelets <sup>fi</sup>ve or 6 days a week regardless of daily demand or the number of units available for production. In addition, daily demand for transfusion and daily minimum production level (the lower limit on platelet production which is determined by hospital policies and other users) do not mirror each other. Daily transfusion demand varies by day of the week and to some extent by season of the year. In some centers the production level gradually increases from Monday through Friday while in other centers the reverse is true. The production of platelets is also related to the platelet transfusion policies of the hospitals routinely served by the blood center. Some hospitals have very strict policies regarding the shelf life of the platelets used in transfusion in their institution. This requires that a surplus of platelets be maintained, which adds to the cost of staf<sup>fi</sup>ng and maintaining suf<sup>fi</sup>cient equipment to meet peak demand.

There are three major cost categories or system costs: the cost of producing platelets at the blood center, cost arising because of platelet loss at the blood center, and transportation cost. The <sup>fi</sup>rst of these three has <sup>fi</sup>ve components: recruitment of blood donors, collection of blood, production of platelets, testing and distribution of blood components.

The production cost is dependent on a number of variables, such as the number of component production staff that must be available at any one time, the space required for production, the number of centrifuges, the number of <sup>fl</sup>ash freezers for the fresh frozen plasma and the number of environmental chambers for the platelet concentrates. The type and number of components to be produced from each unit of whole blood have a direct impact on many of these variables.

Another cost is associated with the loss of products (cost of yield losses). These losses are a result of production, either through breakage or the contamination of non-red cell components (plasma and platelet concentrates) with red cells; and losses due to testing and delays in timely delivery of platelets to the blood center from collection sites. More speci<sup>fi</sup>cally, yield loss cost components include: 1) cost of performing additional tests on contaminated blood, 2) cost of breakage during production, 3) additional costs associated with the separation of platelet-rich plasma from red blood cells due to untimely delivery from collection sites to the blood center — including additional staff needed to meet the 6-hour limit for separation of platelets, and 4) production costs associated with testing errors requiring further analysis.

The periodic transporting of blood from the collection sites back to the component production laboratory also contributes to the total system cost. The number of trips is dependent on the number of platelets to be produced and the collection goals of the bloodmobiles that are within shuttling distance of the blood center. In addition, a shuttle to one bloodmobile cannot visit other bloodmobiles since, in general, the bloodmobiles are either widely dispersed or the traf<sup>fi</sup>c logistics conditions prohibit sharing of shuttle services. While many large blood centers primarily use volunteer drivers and thus incur only mileage costs, others must pay staff or courier services to transport the blood back to the production facility.

## 3. The DSS architecture

The prototype DSS is based on the collection operations of a regional blood center that collects blood using blood mobiles that shuttle between donor sites and the blood center. Platelet production is achieved at the donor center using the whole blood collected. These platelets are then sent to hospitals to meet transfusion demand. The supply chain for platelets is described in Fig. 1.

An effective supply chain system for platelet production and scheduling involves the following components:

• Planning blood center collections using bloodmobiles at donor centers

• Demand schedule for platelets at the regional blood center

• Production of platelets and other components at the regional blood center

• Distribution of platelets to hospitals

• Transfusion of platelets and possible redistribution based on hospital inventories and demand variations.

To implement a prototype optimized supply chain DSS for platelets, the system components involve: a database, an ILP solver, a user interface, and data interfaces to hospitals and donor centers. The architecture for the prototype DSS is shown in Fig. 2. In the prototype implementation the hospital and donor center interfaces are not automated, i.e., inputs and outputs from these interfaces are keyed in. The database is created using MS Access and the ILP solver is an adapted Excel-based spreadsheet.

![](/api/attachments/QQZ4EXG3/fulltext/images/33be321cba1a5c9aa182810c2f3426b9fc59dbb354381dd24c7df1c6cc3cafa4.jpg)  
Fig. 1. Platelet production supply chain.

![](/api/attachments/QQZ4EXG3/fulltext/images/e2217460f68ae8da827cca8f23db7886668de65e6b80ac13a2b0f20bdb5a9e69.jpg)  
Fig. 2. DSS architecture.

The entity relationship model for the regional blood center database is shown in Fig. 3 and the associated relations are shown in Fig. 4. The Entity Relationship (ER) model mimics the supply chain model shown in Fig. 2 very closely. The data requirements match the information requirements at each node of the supply chain.

## 3.1. The user interface

The user interface is a critical element of the DSS. User involvement in the development of the interface is necessary as it often necessitates process changes. The user interface manages the donor center database, the data interface between the database and the solver, the demand schedule interface between the database and the hospital's platelet requirements data, the collection data from bloodmobiles, and donor center information. The interface is divided into a data management component, a reporting component, and a query interface for ad hoc queries.

Sample interfaces for collection and bloodmobile transportation schedules are shown in Fig. 5. In the collection data interface, the user inputs a unique collection ID for the donor. The user also records the date of the donation, the number of units donated, the center ID, the blood type, and screening level. In the transport schedule interface, the user inputs a unique schedule ID, the date, the mobile VIN, the Center ID, the Facility ID, the trip number, and the quantity collected.

The maximum number of trips and the quantity of blood collected should match the schedules laid out by the optimization solver [37].

A weekly platelet collection plan based on the demand schedule is shown in Fig. 6. The minimum and maximum collection capacities for a given center is input by the regional blood center manager based on information obtained from hospitals and other transfusion centers. Also based on bloodmobile availability, the maximum number of trips is provided to the system. These inputs are used by the ILP solver to produce the optimized transportation schedule.

## 4. The ILP solver: an integer nonlinear programming model

The ILP solver component of the DSS includes solving a nonlinear integer model formulated as problem (P1). The objective of problem (P1) is to determine the minimum cost platelet production schedule for the regional blood center for each day of the week. Essentially, the number of platelets produced and the numbers of shuttles made are interdependent and thus have a nonlinear relationship. In addition, platelets are produced and shuttles are made in integer quantities.

## 4.1. Decision variables

We use the following notations to formulate and describe the platelet production problem.

## Variables

X<sub>j</sub> Number of platelet concentrates produced at the blood center per shuttle trip from blood collected by bloodmobile j.

![](/api/attachments/QQZ4EXG3/fulltext/images/b26ffa9c613bc71a97271c611c2d2ae6e191704f41466af736ddb64503ff379d.jpg)  
Fig. 3. The entity relationship model.

![](/api/attachments/QQZ4EXG3/fulltext/images/8208f47bee10645e539a900d6d64bee520a9500fb9e5b5dbe21472bdba4da7ba.jpg)  
Fig. 4. The relational model.

$\Upsilon _ { j }$ Number of shuttle round trips from the blood center to bloodmobile j.

$\Upsilon _ { a j }$ Auxiliary variable belonging to $\Upsilon _ { j }$ where,

$$
Y _ {a j} = \left\{ \begin{array}{l l} 1 & \text { if } \quad Y _ {j} > 0 \\ 0 & \text { otherwise. } \end{array} \right.
$$

Z Yield loss for the system based on total production.

## Parameters

n Daily number of bloodmobiles available for dispatch to separate collection sites.

${ \mathsf { C } } _ { p }$ Production cost per platelet. ${ \mathsf { C } } _ { p }$ is the aggregate of the recruitment, collection, component production, testing, and distribution costs.

${ \mathsf { C } } _ { j }$ Shuttle transportation cost per round trip.

$C _ { f }$ Per unit cost of platelets lost in production due to testing, delays in transportation, breakage, and contamination.

D Total daily demand estimate for the blood center.

$\gamma$ Production loss rate (%).

$\mathsf { S } _ { u }$ Desired maximum number of daily shuttle trips required for all sites. This is the product of the number of bloodmobiles dispatched and the required number of shuttles per day per site based on the “less than 6-hour production” rule.

$\mathrm { L } _ { j } , \mathrm { U } _ { j }$ Minimum and maximum number of shuttle trips made from bloodmobile j to the blood center.

$\mathrm { L } _ { c j } , \mathrm { U } _ { c j }$ Minimum and maximum collection capacity for bloodmobile j per shuttle trip.

## 4.1.1. The daily cost function

The objective of the integer nonlinear programming model is to minimize the total system costs per day. System costs include production costs $\textstyle ( C _ { p } \mathrm { { X } } _ { j } \mathrm { { Y } } _ { j } )$ , which are a function of the platelets produced $( \mathsf { X } _ { j } )$ from the units collected and the number of shuttles made $\left( \Upsilon _ { j } \right)$ to collect blood; transportation costs $( \mathsf { C } _ { j } \mathsf { Y } _ { a j } ( \mathsf { Y } _ { j } - 1 ) )$ ; and the production or yield loss costs $\left( { \mathsf { C } } _ { f } { \mathsf { Z } } \right)$ . We assume that Ζ is the aggregate production loss for a given day and is determined based on the level of total production. In other words, total cost is the sum of production cost before loss, transportation cost (total number of trips to site j minus one), and the cost due to loss of platelets:

$$
\text { Min } \quad \sum_ {j = 1} ^ {n} C _ {p} X _ {j} Y _ {j} + \sum_ {j = 1} ^ {n} C _ {j} Y _ {a j} (Y _ {j} - 1) + C _ {f} Z\tag{1}
$$

In determining the number of shuttles to each collection site the objective function allows the last daily delivery to be made by the respective bloodmobile and thus reduces the number of shuttles by one. The cost function in Eq. (1) includes a <sup>fi</sup>xed cost associated with additional shuttle vehicles and drivers. For example, if shuttle service for a bloodmobile requires hiring of a courier for the day, that cost is included in the problem formulation.

![](/api/attachments/QQZ4EXG3/fulltext/images/72505d32a2a2353cf70a28532e7d17ee8495881a37e012cb15b5d5702ac2d60b.jpg)  
Fig. 5. User interface for donor and transportation data.

The second term of the cost function re<sup>fl</sup>ects the assumption that the last daily delivery from a bloodmobile site is made by the bloodmobile itself; hence there is no variable cost associated with the last daily delivery. For any site j, there are two possibilities: either $\Upsilon _ { j } { > } 0 ,$ in which case $\Upsilon _ { a j } = 1 .$ , and the contribution of site j to the transportation costs is $\mathsf C _ { j } ( \mathsf Y _ { j } - 1 )$ ; or $\Upsilon _ { j } = 0 ,$ which forces $\Upsilon _ { a j }$ to zero, and site j contributes nothing to the transportation costs.

## 4.2. Model constraints

## 4.2.1. Daily demand constraint

The number of platelets produced at the blood center $( \mathsf { X } _ { j } \mathsf { Y } _ { j } )$ is a function of estimated demand (D) per day and the number of platelets lost due to production or testing. Typically, the bloodmobile scheduling manager would estimate the daily demand based on previous blood collection activities of a site and the assumption that any surplus collection above the estimate will be converted to platelet concentrates at the blood center.

$$
\sum_ {j = 1} ^ {n} X _ {j} Y _ {j} \geq D + Z\tag{2}
$$

The estimate for D is determined using the average number of platelets produced in previous schedules plus a buffer stock to account for the error scheduling managers may make in underestimating the collection activities of sites involved. The buffer stock is usually approximated using one standard deviation above the demand and is included in D in constraint (2). An important consideration of constraint (2) is that due to the highly critical and perishable nature of platelet concentrates the production amount $( \mathsf { X } _ { j } \mathsf { Y } _ { j } )$ is required to equal or exceed the estimate for the demand.

## 4.2.2. Limit on the number of shuttle trips per site

Each collection site, based on its demand requirements and the assumption that platelets must be produced no later than 6 h after the blood is collected, is limited to U , an upper bound number of shuttles, and lower bound number of shuttles, $\mathrm { L } _ { j \ast } ~ \mathrm { L } _ { j }$ is imposed so that the minimization function does not force the lower bound in Eq. (3) to zero in situations when blood must be collected at site j despite a low demand. Constraint (3) assumes that only one shuttle at a time may visit any collection site j. That is, each bloodmobile is assigned a single shuttle.

$$
L _ {j} \leq Y _ {j} \leq U _ {j}, j = 1, \dots , n\tag{3}
$$

## 4.2.3. Limit on the number of shuttle trips for all sites

Although constraint (3) would limit the number of shuttle trips per site to $\mathrm { U } _ { j } ,$ , it is possible for the blood center to limit the aggregate total of shuttle trips for all sites to less than $\sum \mathbf { U } _ { j } .$ . For example, the blood center may limit the amount of aggregate blood collection for a day to less than the maximum possible due to a larger than expected inventory, or due to a shorter production cycle. However, in general, the aggregate total of all shuttle trips will equal $\sum \mathbf { U } _ { j } .$ . Constraint (4) represents this relationship.

![](/api/attachments/QQZ4EXG3/fulltext/images/611b7281e3f7528c9d5af07eb007350603ab60d656a15deb8970185c95148fd0.jpg)  
Fig. 6. Collection capacities for a center.

$$
\sum_ {j = 1} ^ {n} Y _ {j} \leq S _ {u}\tag{4}
$$

## 4.2.4. Production loss constraint

Production loss can occur due to testing, delays in transportation, breakage, and contamination. Usually each blood center, based on experience, can determine an expected level for component loss relative to the total daily production. Since Z is an estimate of the number of platelets lost, it is not necessary for constraint (5) to result in an integer quantity. The result for Z obtained from the model can be rounded off.

$$
Z = \gamma \sum_ {j = 1} ^ {n} X _ {j} Y _ {j}\tag{5}
$$

## 4.2.5. Limit on the number of platelets produced per shuttle trip

Blood collected at each bloodmobile is used to produce platelet concentrates at the blood center. Each bloodmobile's collection may generate up to $\mathrm { U } _ { c j }$ platelets per shuttle trip. Similarly, each bloodmobile requires an $\mathrm { L } _ { c j }$ platelets per shuttle trip so that a bloodmobile with smaller collection capacity will not be dispatched to a location where higher blood collection is projected. Constraint (6) represents this relationship.

$$
L _ {c j} \leq X _ {j} \leq U _ {c j}, j = 1, \dots , n\tag{6}
$$

## 4.2.6. Integrality constraints

Platelets are produced at the blood center in integer quantities. Similarly, the number of shuttle trips is measured in integer values. Constraint (7) guarantees this requirement and states that the auxiliary variable $\Upsilon _ { a j }$ is a binary. Relaxing these integrality conditions could result in exaggerated production and transportation values.

$$
X _ {j}, Y _ {j} \geq 0 \quad \text { and   integer; } \quad Y _ {a j} \varepsilon \{0, 1 \}\tag{7}
$$

## 4.3. An alternative formulation

Formulation (P1) contains a non-convex objective function which is dif<sup>fi</sup>cult to solve and would not guarantee convergence to optimality. Thus we simplify (P1) to achieve a better structure. The third term of the objective function (1) is the cost of lost production (yield loss) $\complement _ { f } Z ,$ where Z is de<sup>fi</sup>ned as $Z = \gamma \ \sum \ { \mathrm { X } } _ { j } { \mathrm { Y } } _ { j } .$ Z is simply a prediction of how much production would be lost and it is assumed that its integrality restrictions may be relaxed. With this assumption then Z could be eliminated and the cost of lost production could be incorporated into the cost of production by replacing $\mathsf C _ { p }$ with ${ \mathsf { C } } _ { p } + \gamma { \mathsf { C } } _ { f } .$ This would simplify the model signi<sup>fi</sup>cantly allowing for it to be reduced to a quadratic objective function which is concave and would guarantee convergence to optimality.

Table 2  
Table 1  
Weekly platelet and shuttle data.

<table><tr><td rowspan="2">Collection site</td><td rowspan="2">Cj</td><td colspan="3">Monday</td><td colspan="3">Tuesday</td><td colspan="3">Wednesday</td><td colspan="3">Thursday</td><td colspan="3">Friday</td></tr><tr><td>Lcj</td><td>Ucj</td><td>Uj</td><td>Lcj</td><td>Ucj</td><td>Uj</td><td>Lcj</td><td>Ucj</td><td>Uj</td><td>Lcj</td><td>Ucj</td><td>Uj</td><td>Lcj</td><td>Ucj</td><td>Uj</td></tr><tr><td>C</td><td>5</td><td>10</td><td>22</td><td>3</td><td>5</td><td>20</td><td>3</td><td>0</td><td>17</td><td>3</td><td>0</td><td>30</td><td>3</td><td>5</td><td>23</td><td>3</td></tr><tr><td>G</td><td>5</td><td>0</td><td>20</td><td>3</td><td>5</td><td>20</td><td>2</td><td>0</td><td>42</td><td>3</td><td>0</td><td>17</td><td>3</td><td>5</td><td>25</td><td>3</td></tr><tr><td>H</td><td>10</td><td>0</td><td>17</td><td>3</td><td>0</td><td>17</td><td>3</td><td>0</td><td>15</td><td>3</td><td>0</td><td>16</td><td>3</td><td>0</td><td>0</td><td>0</td></tr><tr><td>J</td><td>10</td><td>0</td><td>20</td><td>3</td><td>0</td><td>17</td><td>3</td><td>0</td><td>18</td><td>3</td><td>0</td><td>12</td><td>3</td><td>0</td><td>17</td><td>3</td></tr><tr><td>K</td><td>10</td><td>0</td><td>15</td><td>3</td><td>0</td><td>20</td><td>3</td><td>5</td><td>27</td><td>3</td><td>0</td><td>22</td><td>3</td><td>5</td><td>27</td><td>3</td></tr><tr><td>L</td><td>5</td><td>0</td><td>15</td><td>3</td><td>10</td><td>20</td><td>3</td><td>0</td><td>15</td><td>3</td><td>5</td><td>20</td><td>3</td><td>5</td><td>20</td><td>3</td></tr><tr><td>M</td><td>10</td><td>0</td><td>12</td><td>3</td><td>0</td><td>8</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>12</td><td>3</td><td>0</td><td>12</td><td>3</td></tr><tr><td>N</td><td>7</td><td>5</td><td>18</td><td>2</td><td>5</td><td>20</td><td>3</td><td>10</td><td>40</td><td>3</td><td>0</td><td>17</td><td>3</td><td>5</td><td>33</td><td>3</td></tr><tr><td>R</td><td>7</td><td>5</td><td>27</td><td>3</td><td>5</td><td>18</td><td>2</td><td>0</td><td>12</td><td>2</td><td>10</td><td>27</td><td>3</td><td>5</td><td>32</td><td>3</td></tr><tr><td>S</td><td>10</td><td>7</td><td>17</td><td>3</td><td>0</td><td>20</td><td>3</td><td>0</td><td>18</td><td>2</td><td>0</td><td>15</td><td>3</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Y</td><td>5</td><td>3</td><td>25</td><td>3</td><td>5</td><td>15</td><td>3</td><td>5</td><td>17</td><td>3</td><td>10</td><td>23</td><td>3</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Z</td><td>10</td><td>0</td><td>15</td><td>3</td><td>7</td><td>23</td><td>3</td><td>7</td><td>27</td><td>3</td><td>0</td><td>23</td><td>3</td><td>0</td><td>15</td><td>3</td></tr></table>

Additionally, the second term in the objective function can be linearized. $\Upsilon _ { a j }$ is de<sup>fi</sup>ned as: $\Upsilon _ { a j } = 1 \mathrm { i f } \Upsilon _ { j } { > } 0$ and $\Upsilon _ { a j } = 0$ for all other $\Upsilon _ { j } .$ De<sup>fi</sup>ning ${ \sf Q } _ { j } = { \sf m a x } \ ( 0 , \ { \sf Y } _ { j } - 1 )$ , we replace $\Sigma \ \bar { \mathsf { C } } _ { j } \ \mathsf { Y } _ { a j } \ ( \mathsf { Y } _ { j } { - } 1 )$ in the objective function with $\sum \mathrm { \bf ~ C } _ { j } \mathrm { \bf Q } _ { j }$ and add the constraints $\mathrm { Q } _ { j } \mathrm { \geq Y } _ { j } { - } 1$ $\begin{array} { r } { \mathbf { Q } _ { j } \ge \mathbf { 0 } , } \end{array}$ , and $j = 1 , . . . . , \boldsymbol { \mathrm { n } }$ , to the formulation. The resultant formulation is shown as problem (P2):

$$
\operatorname{Min} \sum_ {j = 1} ^ {n} \left(C _ {p} + \gamma C _ {f}\right) X _ {j} Y _ {j} + \sum_ {j = 1} ^ {n} C _ {j} Q _ {j}\tag{8}
$$

$$
s. t. (1 - \gamma) \sum_ {j = 1} ^ {n} X _ {j} Y _ {j} \geq D\tag{9}
$$

$$
\sum_ {j = 1} ^ {n} Y _ {j} \leq S _ {u}\tag{10}
$$

$$
Y _ {j} - Q _ {j} \leq 1\tag{11}
$$

$$
L _ {j} \leq Y _ {j} \leq U _ {j}\tag{12}
$$

$$
L _ {c j} \leq X _ {j} \leq U _ {c j}\tag{13}
$$

$$
Q _ {j} \geq 0, X _ {j}, Y _ {j} \geq 0 \quad \text { and   integer }\tag{14}
$$

## 4.4. Solution strategies

Solution of nonlinear integer programming problems is dif<sup>fi</sup>cult and often computationally impossible. There exist algorithms for solving certain classes of nonlinear integer programming problems; however, in most cases there is no guarantee of a global optimal solution. Dynamic programming has been used successfully in solving problems with separable objective functions and constraints [26]. Although this approach yields a global optimum the presence of multiple separable constraints results in multiple dimensional tables for the dynamic programming return functions. For problems with three or more state variables computer storage and computational burden has been shown to be excessive for dynamic programming to be an effective solution strategy for solving nonlinear integer programming problems [8]. Other nonlinear programming techniques such as those based on branch and bound and the approximation methods can yield only local optima unless the correct convexity conditions are met [8,23]. In particular, the majority of such algorithms are developed to solve 0–1 type nonlinear integer problems [1,15,22,34] and are not applicable to problems with general integer variables.

Comparison of planners solution to optimal model results

<table><tr><td rowspan="3">Collection site</td><td colspan="4">Monday</td><td colspan="4">Tuesday</td><td colspan="4">Wednesday</td><td colspan="4">Thursday</td><td colspan="4">Friday</td></tr><tr><td colspan="2">Actual</td><td colspan="2">Model</td><td colspan="2">Actual</td><td colspan="2">Model</td><td colspan="2">Actual</td><td colspan="2">Model</td><td colspan="2">Actual</td><td colspan="2">Model</td><td colspan="2">Actual</td><td colspan="2">Model</td></tr><tr><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td></tr><tr><td>C</td><td>22</td><td>3</td><td>20</td><td>3</td><td>19</td><td>3</td><td>20</td><td>3</td><td>15</td><td>3</td><td>0</td><td>0</td><td>30</td><td>3</td><td>30</td><td>3</td><td>22</td><td>3</td><td>22</td><td>3</td></tr><tr><td>G</td><td>13</td><td>2</td><td>0</td><td>0</td><td>18</td><td>2</td><td>18</td><td>2</td><td>42</td><td>3</td><td>40</td><td>3</td><td>17</td><td>3</td><td>13</td><td>3</td><td>25</td><td>3</td><td>21</td><td>3</td></tr><tr><td>H</td><td>0</td><td>0</td><td>0</td><td>0</td><td>13</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>16</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>J</td><td>0</td><td>0</td><td>20</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>K</td><td>14</td><td>3</td><td>15</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>27</td><td>3</td><td>24</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>27</td><td>3</td><td>27</td><td>3</td></tr><tr><td>L</td><td>15</td><td>3</td><td>0</td><td>0</td><td>17</td><td>3</td><td>20</td><td>3</td><td>12</td><td>3</td><td>0</td><td>0</td><td>20</td><td>3</td><td>20</td><td>3</td><td>20</td><td>3</td><td>20</td><td>3</td></tr><tr><td>M</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>9</td><td>3</td><td>0</td><td>0</td></tr><tr><td>N</td><td>15</td><td>2</td><td>16</td><td>2</td><td>17</td><td>3</td><td>19</td><td>3</td><td>40</td><td>3</td><td>38</td><td>3</td><td>15</td><td>3</td><td>0</td><td>0</td><td>32</td><td>3</td><td>33</td><td>3</td></tr><tr><td>R</td><td>18</td><td>3</td><td>24</td><td>3</td><td>15</td><td>2</td><td>17</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>27</td><td>3</td><td>27</td><td>3</td><td>30</td><td>3</td><td>30</td><td>3</td></tr><tr><td>S</td><td>17</td><td>3</td><td>15</td><td>3</td><td>0</td><td>0</td><td>16</td><td>3</td><td>0</td><td>0</td><td>15</td><td>3</td><td>13</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Y</td><td>25</td><td>3</td><td>23</td><td>3</td><td>10</td><td>3</td><td>0</td><td>0</td><td>15</td><td>3</td><td>15</td><td>3</td><td>22</td><td>3</td><td>23</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Z</td><td>0</td><td>0</td><td>0</td><td>0</td><td>23</td><td>3</td><td>23</td><td>3</td><td>27</td><td>3</td><td>27</td><td>3</td><td>0</td><td>0</td><td>23</td><td>3</td><td>13</td><td>3</td><td>0</td><td>0</td></tr><tr><td>D</td><td>389</td><td></td><td></td><td></td><td>363</td><td></td><td>364</td><td></td><td>534</td><td></td><td>477</td><td></td><td>480</td><td></td><td>408</td><td></td><td>534</td><td></td><td>459</td><td></td></tr><tr><td># of iterations</td><td>N/A</td><td></td><td>123</td><td></td><td>N/A</td><td></td><td>458</td><td></td><td>N/A</td><td></td><td>307</td><td></td><td>N/A</td><td></td><td>134</td><td></td><td>N/A</td><td></td><td>103</td><td></td></tr></table>

Optimization Model Plan for Platelet Production

<table><tr><td rowspan="2">Collection site</td><td colspan="2">Monday</td><td colspan="2">Tuesday</td><td colspan="2">Wednesday</td><td colspan="2">Thursday</td><td colspan="2">Friday</td></tr><tr><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td><td>Xj</td><td>Yj</td></tr><tr><td>100</td><td>20</td><td>1</td><td>20</td><td>1</td><td>40</td><td>2</td><td>17</td><td>1</td><td>25</td><td>2</td></tr><tr><td>102</td><td>20</td><td>1</td><td>16</td><td>2</td><td>18</td><td>2</td><td>10</td><td>1</td><td>15</td><td>1</td></tr><tr><td>103</td><td>15</td><td>1</td><td>20</td><td>1</td><td>20</td><td>1</td><td>20</td><td>1</td><td>25</td><td>2</td></tr><tr><td>104</td><td>22</td><td>2</td><td>20</td><td>1</td><td>15</td><td>1</td><td>30</td><td>2</td><td>20</td><td>1</td></tr><tr><td>105</td><td>10</td><td>1</td><td>20</td><td>1</td><td>15</td><td>1</td><td>20</td><td>1</td><td>20</td><td>1</td></tr></table>

Fig. 7. Results of the ILP solver: platelet production plan.

In problem (P2) the objective function is quadratic and the constraints include both quadratic and linear forms. Appendix A describes a distinct approach for reaching an optimal solution for (P2).

## 5. Application of the DSS

The DSS is tested using data from the collection operations of a regional blood center [28]. On a daily basis twelve to <sup>fi</sup>fteen bloodmobiles are dispatched to donor sites. Since some of these donor sites are located in widely dispersed areas, only nine to twelve of the bloodmobiles are available as collection sites for platelet production.

In the test data, the preplanned weekly component schedule is based on a platelet production of 350 to 475 units per day depending on the day of the week. For each collection day the daily demand is based on forecasted demand using historical information plus a buffer stock to account for error in estimation. The minimum level of production, as determined by hospital policies, is set to meet the desired inventory level for the day plus carryover inventory for the following morning. These numbers can vary almost as dramatically as the weekly demand. Since the hospital interface is not integrated with the prototype DSS, these are inputs using forms shown in Fig. 6.

Problem (P2) was solved using an Excel-based solver for the sample problem [10]. Table 1 presents the weekly platelet and shuttle data used to test problem (P2). In addition to transportation cost ${ \mathsf { C } } _ { j } ,$ the bloodmobile minimum and maximum available capacities $\mathrm { L } _ { c j }$ and $\mathrm { U } _ { c j }$ are shown for each site for 5 days of the week. Similarly, U , the upper bound number of possible shuttles is included in Table 1. We have assumed the lower bound number of shuttle trips $\mathrm { L } _ { j } = 0$ for all collection sites.

The maximum number of platelets produced at the blood center is dependent on the collection capacity of the bloodmobiles assigned. The number of shuttles possible from the blood center to a bloodmobile varies from zero, if no blood is collected at the site, to a maximum of three (see Table 1). The upper bound number of shuttles possible is determined by dividing the total hours of operation for a bloodmobile by the frequency of the shuttles, in this case every 2 h [30].

Using input data from Table 1, the transformed linear 0–1 problem (P2) is run separately for each day of the week. A spreadsheet-based large-scale LP/MIP optimization engine capable of solving a 16,000 variable by 16,000 constraint problem was used. Table 2 presents the results of the experiment. On average, each transformed problem consists of 330 variables and 376 constraints. Once the optimal solution is obtained, the spreadsheet program automatically converts the results of model (P2) consisting of $\Gamma _ { i j } , \mathrm { t } _ { i j } ,$ and $\boldsymbol { \mathsf { W } } _ { i j }$ variables back to the corresponding $\mathrm { X } _ { j }$ and $\Upsilon _ { j } .$ Optimal values of $\mathrm { X } _ { j }$ and $\Upsilon _ { j }$ are given in Table 2 along with the actual plan prepared by the donor recruitment department for each day of the week. Also included in Table 2 are the demand values used for determining the optimal solution and the number of iterations required to solve the binary variable problem (P2).

An analysis of Table 2 reveals that in some cases the plan proposed by the model uses fewer bloodmobile sites than the actual plan prepared by the donor recruitment department. For example, mobiles H and M are not dispatched by the model to any of the collection sites during the week. In comparison the planners have scheduled mobile

![](/api/attachments/QQZ4EXG3/fulltext/images/0cc50aa8b03c7a46af4d3aee1d86f88a1a91c0c63ad35e754f5e80917c879df3.jpg)  
Fig. 8. A sample query.

![](/api/attachments/QQZ4EXG3/fulltext/images/f17cd48f3afd502915c4a93a05d2713b0063f4846e26115ca614eeda35639ad6.jpg)  
Fig. 9. A sample report.

H for Tuesday and Thursday collection and mobile M for Friday collection. There also exist several cases for which the model schedules a bloodmobile for a given day of the week not planned by the planners. This is detected for mobiles J, S and Z in Table 2. In particular, mobile J is not scheduled by the planners for any day of the week, however, it is scheduled by the model for Monday. In all, the integer programming model (P2) recommends 22% fewer assignment of the bloodmobiles to collection sites.

It is also interesting to observe in Table 2 the comparison of platelets produced and the number of shuttle trips made for the actual and the model results. For example, for mobile Y on Wednesday, both the actual and the model produce identical results, i.e., 15 units of platelets produced and 3 shuttle trips made. However, for mobile R, on Monday, the actual plan produces 18 units with 3 trips, while the model recommends 24 units and the same number of trips. Comparing the total number of platelets produced for the week, planners have scheduled 2178 units versus 2091 units for the model. That is 87 units fewer or about 4% difference. This difference is not critical since the model has met or exceeded the lower bound requirement of the weekly demand imposed by the planners for platelet production.

The results of the ILP solver are imported into the DSS database and a sample table representing the results is shown in Fig. 7. The output of the ILP model shows the number of platelets to be produced by a collection center and the number of blood mobile trips required to meet the schedule.

A sample query for a speci<sup>fi</sup>ed bloodmobile's collection data for a speci<sup>fi</sup>ed day is shown in Fig. 8. A sample report of the weekly platelets production and a trip schedule for a donor center is shown in Fig. 9.

An important outcome of the application of the integer nonlinear programming model is that it permits the planners to completely remove bloodmobiles H and M from assignment to any collection site. Similarly, the results of the model reveal that mobile J is only used once per week under the conditions of optimality. Thus, it might be possible for the planners to shift demand from Monday to the rest of the week, allowing for mobile J to be removed from assignment to a site. In light of the realization that the platelet production process involves the use of critical and scarce resources any major operational adjustments, such as the reduction in the number of bloodmobiles, will have a signi<sup>fi</sup>cant effect on the management of these resources. Savings arising from elimination of staff time, transportation and maintenance costs from mobiles H, M and J can certainly have a positive effect in the operation of the remaining mobiles and the overall platelet production process.

## 6. Summary and conclusions

Production of platelet concentrates at the blood center involves a careful management of scarce recourses such as scheduling and assignment of bloodmobiles and the transportation costs associated with shuttle trips. Platelet transfusion rates, especially apheresis platelets, continue to increase. Between 2004 and 2006 there was an increase of 9% in transfusion rates of apheresis platelets [36] while the increase in transfusion rates of whole blood and red blood cells was only about 3% during the same period. Coupled with the very short shelf life of platelets managing an optimal supply of platelets is signi<sup>fi</sup>cantly more challenging than managing the supply of whole blood cells. Most of the past research has focused on the availability of whole blood cells. In this paper, a DSS that supports a supply chain of the platelet production process coupled with an optimized mobile scheduling system based on a non-convex integer programming model is proposed. To achieve optimality, the optimization problem is converted using a 0–1 linearization approach and it is successfully solved using data collected from a regional blood center. Computational experiments with the proposed model result in the elimination of some of the underutilized bloodmobiles from the transportation schedule while meeting demand requirements, thus, saving staff time, transportation, and maintenance expenses for the blood center.

A possible extension for the current research may involve experimentation with the sharing of shuttles among bloodmobiles assigned to various collection sites. This would require building a network-based model to route shuttles between the blood center and all the collection sites. The extension could also include demand data integration with the transfusion centers like hospitals and supply data integration with donor centers. This data integration is a desirable objective given the short time span between platelet collection and transfusion.

## Appendix A. A linear 0–1 integer alternative

To guarantee optimality, it is possible to transform (P2) into a linear 0–1 integer model. A two-step transformation is required to achieve this.

Step 1: Conversion of Xj and Yj to 0–1 type Suppose in an all-integer model we have available upper bounds M for each variable $\mathrm { X } _ { j }$ and $\Upsilon _ { j }$ (either explicitly stated or derivable implicitly from the problem constraints). For each $\mathrm { X } _ { j }$ and $\Upsilon _ { j }$ we can derive an equivalent expression in terms of the weighted sum of zero-one variables $\mathrm { t } _ { i j }$ and $\mathbf { W } _ { i j } ,$ respectively, as follows: $X _ { j } = \sum _ { i = 0 } ^ { k } 2 ^ { i } t _ { i j }$ and $Y _ { j } = \sum _ { i = 0 } ^ { k } 2 ^ { i } w _ { i j } ,$ where the upper bound $\mathrm { M } _ { j }$ is de<sup>fi</sup>ned as: $2 ^ { k } \leq \mathsf { M } _ { j } \leq 2 ^ { k + 1 }$ . In $( \mathsf { P 2 } )$ both $\mathrm { X } _ { j }$ and $\Upsilon _ { j }$ have explicit upper bound values of $\mathrm { U } _ { c j } , \mathrm { U } _ { j } ,$ respectively. Step 2: Conversion of nonlinear relationships to linear. Consider the problem:

Min $f ( q _ { i } , . . . . . , q _ { n } )$

$$
s. t. g _ {i} (q _ {i}, \dots .., q _ {n}) \leq b _ {i}, i = 1, \dots , m
$$

$$
q _ {j} = 0 \quad \text { or } \quad 1, j = 1,..., n
$$

Assume that f and g are polynomials with the ${ \mathrm { k } } ^ { \mathrm { t h } }$ term represented by

$$
C _ {k} \prod_ {j} ^ {n _ {k}} q _ {j} ^ {a} k j
$$

where $\mathsf { C } _ { k }$ is a constant and $\mathsf { a } _ { k j }$ is a positive constant exponent. This non-linear problem can be transformed into a 0–1 linear problem [16,35]. Since $\mathfrak { q } _ { j }$ is binary, $q _ { j } ^ { a } k j = \mathsf { q } _ { j }$ for any positive $\mathsf { a } _ { k j } .$ If $\mathsf { a } _ { k j } = 0 ,$ obviously the variable $\mathfrak { q } _ { j }$ will not be present in the ${ \mathrm { k } } ^ { \mathrm { t h } }$ term of the problem. This implies that the ${ \mathrm { k } } ^ { \mathrm { t h } }$ term may be written as $\begin{array} { r } { C _ { k } \prod _ { j = 1 } ^ { n _ { k } } ( } \end{array}$ q<sub>j</sub> when $\mathsf { a } _ { \mathrm { k j } } { > } 0 .$ . We let $\begin{array} { r } { r _ { k } = \Pi _ { j } ^ { n _ { k } } q _ { j } , } \end{array}$ , then $\Gamma _ { k }$ is also a binary variable and the ${ \mathrm { k } } ^ { \mathrm { t h } }$ term of the polynomial reduces to the linear term ${ \mathsf { C } } _ { k } ~ { \mathsf { r } } _ { k } .$ To ensure that $\boldsymbol { \mathrm { r } } _ { k } = 1$ when all $\mathsf q _ { j } = 1$ and zero otherwise, we add the following constraints for each $\Gamma _ { k } \dot { . }$

$$
\sum_ {j = 1} ^ {n k} q _ {j} - (n _ {k} - 1) \leq r _ {k}
$$

$$
\frac {1}{n _ {k}} \sum_ {j = 1} ^ {n _ {k}} q _ {j} \geq r _ {k}\tag{A.1}
$$

A:2

If all ${ \mathfrak { q } } _ { j } = 1 , \ \Sigma \ { \mathfrak { q } } _ { j } = { \mathfrak { n } } _ { k }$ and constraint (A.1) results in $\boldsymbol { \mathrm { r } } _ { k } \ge 1$ , and constraint $( \mathsf { A } . 2 )$ gives $\boldsymbol { \mathrm { r } } _ { k } \le 1 ;$ ; implying $\boldsymbol { \mathrm { r } } _ { k } = 1$ . On the other hand, if at least one ${ \mathfrak { q } } _ { j } = 0$ , then Σ $\scriptstyle , \ q _ { j } < \ n _ { k }$ and constraints (A.1) and (A.2) will return $ { \boldsymbol { \mathrm { r } } } _ { k } \geq - (  { \boldsymbol { \mathrm { n } } } _ { k } - 1 )$ and r b1, respectively, implying that $\boldsymbol { \mathrm { r } } _ { k } = 0$ Incorporating Steps 1 and 2 in (P2) will result in the following linear 0–1 integer program, where $M _ { i j }$ is a constant of the type $2 ^ { \mathrm { k } }$ for all i and j, and k is a positive exponent:

$$
\operatorname{Min} \left(C _ {P} + \gamma C _ {f}\right) \sum_ {i} \sum_ {j} M _ {i j} r _ {i j} + \sum_ {j} C _ {j} Q _ {j}
$$

$$
S. t. (1 - \gamma) \sum_ {i} \sum_ {j} M _ {i j} r _ {i j} \geq D\tag{A.3}
$$

$$
t _ {i j} + w _ {i j} - (n _ {k} - 1) \leq r _ {i j}\tag{A.4}
$$

$$
\frac {1}{n _ {k}} \left(t _ {i j} + w _ {i j}\right) \geq r _ {i j}\tag{A.5}
$$

$$
\sum_ {j} \left(\sum_ {i = 0} ^ {k} 2 ^ {i} w _ {i j}\right) \leq S _ {u}\tag{A.6}
$$

A:7

$$
\left(\sum_ {i = 0} ^ {k} 2 ^ {i} w _ {i j}\right) - Q _ {j} \leq 1\tag{A.8}
$$

$$
L _ {j} \leq \left(\sum_ {i = 0} ^ {k} 2 ^ {i} w _ {i j}\right) \leq U _ {j}\tag{A.9}
$$

$$
L _ {c j} \leq \left(\sum_ {i = 0} ^ {k} 2 ^ {i} w _ {i j}\right) \leq U _ {c j}\tag{A.10}
$$

$$
Q _ {j} \geq 0, r _ {i j}, t _ {i j}, w _ {i j} = 0, 1; i = 0, 1,..., m; j = 0, 1,..., n; n _ {\mathrm{k}} = 2\tag{A.11}
$$

## References

[1] E. Balas, Duality in discrete programming: the quadratic case, Management Science 16 (1969).

[2] E. Brodheim, G.P. Prastacos, A blood management system with prescheduled deliveries, Transfusion 19 (4) (1979).

[3] E. Brodheim, G.P. Prastacos, The Long Island blood distribution system as a prototype for regional blood management, Interfaces 9 (5) (1979).

[4] E. Brodheim, G.P. Prastacos, Demand, usage and issuing of blood at hospital blood banks, Working Paper 79-10-02 (Department of Decision Sciences, The Wharton School, University of Pennsylvania), 1980.

[5] D. Chazan, S. Gal, A Markovian model for the perishable product inventory, Management Science 23 (1977).

[6] M.A. Cohen, Analysis of single critical number ordering policies for perishable inventories, Operations Research 24 (1976).

[7] M.A. Cohen, W.P. Pierskalla, Target inventory levels for a hospital blood bank or a decentralized regional blood banking system, Transfusion 5 (1985).

[8] M.W. Cooper, A survey of methods for pure nonlinear integer programming, Management Science 27 (1981).

[9] P.D. Cumming, K.E. Kendall, C.C. Pegels, J.F. Shubsda, A collections planning model for regional blood suppliers: description and validation, Management Science 22 (1976).

[10] A. Dutta, Integrating AI and optimization for decision support: a survey, Decision Support Systems 18 (3–4) (1996).

[11] R.C. Elston, J.C. Pickrel, A statistical approach to ordering and usage policies for a hospital blood bank, Transfusion 3 (1963).

[12] A. Federgruen, G.P. Prastacos, P. Zipkin, An allocation and distribution model for perishable products, Research Working Paper 392A (Graduate School of Business, Columbia University), 1982.

[13] G.M. Frankfurter, K.E. Kendall, C.C. Pegels, Management control of blood through a short-term supply-demand forecast system, Management Science 21 (4) (1974).

[14] B. Fries, Optimal ordering policy for a perishable commodity with <sup>fi</sup>xed lifetime, Operations Research 23 (1) (1975).

[15] P. Ghandforoush, T.K. Sen, M. Wander, A decision support system for electric utilities: compliance with clean air act, Decision Support Systems 26 (1999) 261–273.

[16] F. Glover, Improved linear integer programming formulations of nonlinear integer problems, Management Science 22 (1975).

[17] R. Haijema, J. van der Wal, N.M. van Dijk, Blood platelet production: optimization by dynamic programming and simulation, Computers & Operations Research 34 (2007).

[18] S.N. Hay, C.C. Immel, L.S. McClannan, M.E. Brecher, The introduction of 7-day platelets: a university hospital experience, Journal of Clinical Apheresis 22 (2007).

[19] R. Jagannathan, T. Sen, Storing crossmatched blood: a perishable inventory model with prior allocation, Management Science 37 (3) (1991).

[20] J.B. Jennings, Blood bank inventory control, Management Science 19 (1973).

[21] K. Katsaliaki, Cost-effective practices in the blood service sector, Health 86 (2008).

[22] O. Kettani, M. Oral, Reformulating nonlinear combinatorial optimization problems for higher computational ef<sup>fi</sup>ciency, European Journal of Operational Research 58 (2) (1992).

[23] O. Kettani, M. Oral, Reformulating quadratic assignment problems for ef<sup>fi</sup>cient operations, IIE Transactions 25 (6) (1993).

[24] J.F. Kros, R.Y. Pang, A decision support system for quantitative measurement of operational ef<sup>fi</sup>ciency in a blood collection facility, Computer Methods and Programs in Biomedicine 74 (1) (2004).

[25] B.N. Li, M.C. Dong, S. Chao, On decision making support in blood bank information systems, Expert Systems with Applications 34 (2008).

[26] T.L. Morin, Computational advances in dynamic programming, in: M.L. Puterman (Ed.), Dynamic Programming and Its Applications, Academic Press, New York, 1978.

[27] S. Nahmias, Myopic approximations for the perishable inventory problem, Management Science 22 (1976)

[28] V. Plotnikov, Forecasting demand for random donor platelet concentrates in a regional blood center, Working paper (Virginia Polytechnic Institute and State University), 2003.

[29] G.P. Prastacos, Optimal myopic allocation of a product with <sup>fi</sup>xed lifetime, Journal of Operations Research Society 29 (9) (1978).

[30] G.P. Prastacos, Allocation of perishable inventory, Operations Research 29 (1) (1981).

[31] G.P. Prastacos, Blood inventory management: an overview of theory and practice, Management Science 30 (7) (1984).

[32] J. Rautonen, Redesigning supply chain management together with the hospitals, Transfusion 47 (2) (2007).

[33] G. Rock, O. Akerblom, O. Berseus, P. Herve, P. Jacobs, T. Kelly, J. MacPherson, U. Nydegger, G. Segatchian, S. Urbaniak, M. Valbonesi, The supply of blood products in 10 different systems or countries, Transfusion Science 22 (2000).

[34] T.K. Sen, L.J. Moore, T.J. Hess, An organizational decision support system for managing the DOE hazardous waste cleanup program, Decision Support Systems 29 (1) (2000).

[35] H.A. Taha, Integer Programming, Applications, and Computations, Academic Press, New York, 1975.

[36] The 2007 National Blood Collection and Utilization Survey Report (Washington, DC: Department of Health and Human Services, 2007)

[37] I.T. Yang, Utility-based decision support system for schedule optimization, Decision Support Systems 44 (3) (2008).

Parviz Ghandforoush is Professor of Business Information Technology at Virginia Polytechnic Institute and State University (Virginia Tech). He received the Ph.D. in Management Science at Texas Tech University, MBA at the University of Texas in Austin, and B.S. Electrical Engineering at the University of Texas in Austin. Dr. Ghandforoush has over 25 years of research, teaching, administrative, and professional experience in information technology and management science and is the co-author of the textbook Management Science for Decision Makers. He has published in refereed academic and professional publications in the areas of decision and optimization models, decision support systems in complex environments, sequencing and scheduling, staf<sup>fi</sup>ng models, and simulation of organizational operations. His research has appeared in such journals as, Computers & Operations Research, Journal on Computing, Decision Support Systems, Journal of Systems Management, International Journal of Production Research, International Journal of Industrial Engineering Transactions, European Journal of Operations Research, The International Journal of Management Science, Naval Research Logistics, Journal of the Operational Research Society, Computers & Information Sciences, Computers & Industrial Engineering, and others. He has extensive involvement in professional development, consulting and research activities in areas of executive decision models, ef<sup>fi</sup>ciency models and optimization, strategic implications of information technology, decision support systems, and electronic commerce. Parviz Ghandforoush is the Managing Director of the Master of Information Technology Program and Director of MBA Program at Virginia Tech.

Tarun Sen is a Professor of Management Information Systems at the Pamplin College of Business at Virginia Tech. He also served as Associate Dean for Graduate and International Programs and Director of the Pamplin MBA program. He has published extensively in reputed journals that include Management Science, INFORMS Journal on Computing, Decision Support Systems, OMEGA, Strategic Finance, IEEE Transactions on Systems Man and Cybernetics, Journal of Datawarehousing, and others. He has a B. Tech in Mechanical Engineering from IIT Kanpur, MBA from IIM Bangalore, and a Ph.D. in MIS from the University of Iowa. His research interests lie in business component-based systems design, decision support systems, and the interface between IT innovation and global business.
