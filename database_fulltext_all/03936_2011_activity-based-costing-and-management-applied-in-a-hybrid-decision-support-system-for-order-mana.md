---
otero_id: 3936
otero_key: "U3NX3Y2W"
title: "Activity-Based Costing and Management applied in a hybrid Decision Support System for order management"
authors: "Amir H. Khataie; Akif A. Bulgak; Juan J. Segovia"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.06.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Activity-Based Costing and Management applied in a hybrid Decision Support System for order management

Amir H. Khataie <sup>a,</sup>⁎, Akif A. Bulgak <sup>a</sup>, Juan J. Segovia

<sup>a</sup> Department of Mechanical and Industrial Engineering, Concordia University, 1515 St. Catherine St. West, Montréal (Québec), Canada, H3G 1M8 (office EV 13–105) <sup>b</sup> John Molson School of Business, Concordia University, Montreal, Canada, 1450 Guy Street, Montréal (Québec), Canada, H3G 1M8 (office MB 14–229)

## a r t i c l e i n f o

Article history: Received 8 July 2010 Received in revised form 25 February 2011 Accepted 10 June 2011 Available online 25 June 2011

Keywords: Activity-Based Costing and Management Decision Support System Mixed-Integer Programming System Dynamics Supply chain management Cost control

## a b s t r a c t

This article introduces a new Cost Management and Decision Support System (DSS) applicable to Order Management. This model is better <sup>fi</sup>t and compatible with today's competitive, and constantly changing, business environment. The presented Pro<sup>fi</sup>table-To-Promise (PTP) approach is a novel modeling approach which integrates System Dynamics (SD) simulation with Mixed-Integer Programming (MIP). This Order Management model incorporates Activity-Based Costing and Management (ABC/M) as a link to merge the two models, MIP and SD. This combination is introduced as a hybrid Decision Support System. Such a system can evaluate the pro<sup>fi</sup>tability of each Order Ful<sup>fi</sup>llment policy and generate valuable cost information. Unlike existing optimization-based DSS models, the presented hybrid modeling approach can perform on-time cost analysis. This will lead to better business decisions based on the updated information.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Decision Support Systems (DSSs) play a crucial role in today's rigorous global competition business environment. By providing ontime and reliable information, DSS assist management decision making in rendering the company more pro<sup>fi</sup>table, leaner, more responsive, and agile. In the area of Supply Chain Order Management, DSSs can be formulated through three different theoretical modeling approaches: Available-To-Promise (ATP), Capable-To-Promise (CTP), and Pro<sup>fi</sup>table-To Promise (PTP).

The <sup>fi</sup>rst two modeling approaches emphasize the capacity availability in order to decide whether to accept or reject an order, whereas the PTP approach considers the opportunity cost of accepting or rejecting an order as a main decision evaluation factor. In fact, PTP examine decisions based on the possibility of assigning the available capacity by not accepting an order today to another order with higher pro<sup>fi</sup>t margin which has been predicted to take place in the future.

Regardless of the modeling approach used, management requires a complementary tool that can assist them to analyze the impact of the decision implemented on the business status changes. For instance, with respect to ATP and CTP, management needs to know the availability of their production resources after ful<sup>fi</sup>lling each order. However, PTP management needs to monitor and control the costs and pro<sup>fi</sup>t changes after taking any decision dynamically. The traditional optimization-based models cannot ful<sup>fi</sup>ll this requirement. They are only able to provide relevant information based on the business static status.

Moreover, the PTP model needs to be developed based on an accounting approach which can accurately estimate the value of consumed resources. Generally, a production process requires three inputs: Direct Labor, Direct Material, and Manufacturing Overhead (MOH). The <sup>fi</sup>rst two are categorized as direct costs, which are traceable to a speci<sup>fi</sup>c cost object (e.g. service, product, order). The latter represents a mixture of both direct and indirect costs (e.g. maintenance, security, safety) which represents a challenge to assign them to the cost objects.

The Traditional Cost Accounting (TCA) allocates, as opposed to assigning, MOH costs either by using a plant-wide rate or departmental rates; either case may distort the <sup>fi</sup>nal production cost amount. Especially in a case where there is a highly customized and low volume production process. Unrealistic cost estimation, may lead to mispricing and compromise the <sup>fi</sup>rm's growth and pro<sup>fi</sup>tability.

Activity-Based Costing and Management (ABC/M) is a relatively new cost accounting and management approach that enhances the level of understanding about business operation costs; especially MOH costs. ABC/M is an accounting approach which assigns, instead of allocating, MOH costs to the activities. Although the application of ABC/M does not eliminate MOH costs allocation, it can reduce it to some facility-level costs (e.g. facility utility costs, facility managing costs).

The importance of hybrid Supply Chain DSSs has been shown comprehensively in a recent study presented by Martinez-Olvera [24]. “As real-life business environments have become really complex, supply chains members have been forced to use hybrid business models (that is, the integration of features of two different business models).” The other three studies which have paid attention to this subject are: [19], [20], and [26]. Martinez-Olvera [24] also discussed the optimization-based simulation models as a potential future work.

This article explains how ABC/M can be utilized as a powerful approach to develop a hybrid Mixed-Integer Programming (MIP) and System Dynamics (SD) Decision Support System for Order Management problems. It also introduces a new approach in integrating ABC/M information with SD simulation modeling technique, which results in a more reliable and precise cost monitoring tool.

The rest of this article is organized as follows: Section 2 provides a brief literature review, Section 3 elaborates the discussed general Order Management problem, Section 4 incorporates the ABC/M-based Mixed-Integer programming (MIP) decision support model, and Section 5 provides an illustrative numerical example for the developed MIP model. The System Dynamics (SD) cost monitoring model and the hybrid DSS all are explained in Section 6. In Section 7 the relevant conclusion and future work are explained. Finally, the SD model variables' information is given in Appendix.

## 2. Background

ABC/M is a two-stage process, (1) associating cost to resource (activity), and (2) selecting an appropriate activity measurement (activity cost driver), [6]. Kee [14] named the two steps as; (1) breaking overhead costs into different cost pools and (2) assigning overhead costs through different activity cost drivers to products or orders. As a result, a more accurate overhead costs assignment is achieved.

ABC/M supporters highlight two principal objectives, [11] and [27]: (1) to provide detailed information about the costs and consumption of activities in a speci<sup>fi</sup>c process and (2) to provide accurate information for managers to improve decisions. This has also been corroborated by Gosselin [7] regarding a pilot and full ABC/M implementation studies. However, the use of ABC/M has been limited to a cost accounting approach, rather than as a managerial technique (Gosselin [7]; Kaplan and Anderson [13]; Gosseling [8]).

ABC/M advantages, and constructive effects, on a <sup>fi</sup>rm's performance have been determined through numerous studies and dissertations. Kennedy and A<sup>fl</sup>eck-Graves [15], Ittner et al. [12], and Cagwin and Bouwman [5] attested ABC/M as a preferable accounting approach compared to the TCA systems. Some studies such as; Novićević and Antić [25] and Cagwin and Barker [4] showed evidence of a positive impact of ABC/M on lean manufacturing components like Just-In-Time (JIT) and Total Quality Management (TQM).

The preeminence of ABC/M in providing detailed cost information represents a potential powerful approach for developing PTP Supply Chain Decision Support Systems. Malik and Sullivan [22] developed an ABC/M-based Mixed-Integer Programming (MIP) decision support model for product mix problems. Kee [14] integrated some aspects of the Theory of Constraints (TOC) in ABC/M-based MIP modeling for the product mix problem and named it “Expanded ABC/M model.” The model identi<sup>fi</sup>es the <sup>fi</sup>rm's optimal product mix by evaluating simultaneously the resources and product cost, the production resources availability, and the business marketing opportunities.

In Supply Chain Order Management, [17] and [18] presented a PTP– MIP model for accepting or rejecting orders by implementing ABC/M homogeneous cost pools' structure originally introduced by Cooper and Kaplan [6]. The purpose of the model was to gain insight into how signi<sup>fi</sup>cant Order Management decisions are in maximizing pro<sup>fi</sup>tability when the <sup>fi</sup>rm has insuf<sup>fi</sup>cient production resources to satisfy all the demand. Khataie et al. [16] added the possibility of pursuing two main different goals simultaneously, reducing the residual capacity and increasing the pro<sup>fi</sup>tability to the previous models.

A powerful PTP Order Management tool assists management to monitor, analyze, and foresee the consequences and outcomes of each decision, and monitors their business competitiveness factors dynamically. SD is a simulation approach that was developed in the mid 50s by J. Forrester from Massachusetts Institute of Technology (MIT) to understand the dynamic behavior and status alternation of complex systems over a certain period of time with learning ability.

Lately, SD has been applied on numerous diverse areas of research by upcoming the advanced generation of SD simulation software. However, the survey presented by Braines and Harrison [3] showed the limitations of SD modeling in the manufacturing sector from the business and/or operational perspective. This represented a diversi<sup>fi</sup>cation from its original purpose, which was to serve as a decision support tool for manufacturing processes at the operational level. Instead, and according to the survey, SD have been broadly used in the modeling of resource management at national and global level decision support processes, and in the service sector at operational levels.

A limited number of studies using SD approach for <sup>fi</sup>nancial decisions have been reported. Abdel Hamid and Madnick [1] used SD for software development cost estimation. They implemented the SD simulation technique to see the effects of multi-variable changes in the model. Marquez and Blanchar [23] applied SD to support investment decisions in high-technology business. Macedo et al. [21] developed a real-time cost monitoring model for the reengineering process of a gelatinous substance at the microbiology laboratory by integrating the ABC/M and SD. However, the developed model was acting as a real-time cost calculator rather than a System Dynamics model. There were no positive or negative learning loops in the proposed model.

## 3. General illustrative problem

A Flexible Manufacturing System is selected as a pilot production facility in a simpli<sup>fi</sup>ed three-echelon Supply Chain including supplier, producer, and customers. The system can set up two different production processes or models: Basic and Deluxe. Direct material is similar for both models and there is no restriction for direct material supply. The manufacturing process, Fig. 1, starts by injecting the common direct material into the system. Second, the FMS alternates between two types of setup based on the assigned production plan. Lastly, the manufacturing products are stored for shipping to the customers.

The <sup>fi</sup>rm's management follows a pull-production strategy, therefore it develops the aggregate production plan (AP) based on the received orders per month. Not all the orders can be ful<sup>fi</sup>lled completely due to machining hour capacity per period; as a result, the <sup>fi</sup>rm's management has to choose the ful<sup>fi</sup>llment rate of each order. The Order Management policy is ful<sup>fi</sup>lling completely, or partially, or rejecting the orders according to the production system availability and order's pro<sup>fi</sup>tability factors.

The problem and parameters have been extracted from a managerial accounting educational business case study known as “Willow Company” from [10]. The production costs have been split into two groups; prime costs (which include Direct Materials and Direct Labor) and overhead costs. The latter is divided into <sup>fi</sup>ve homogeneous cost pools with a particular activity cost driver for each one. The case study assumes that the overhead unit-level costs are completely traceable and are included in the prime costs.

There are two different batch-level cost pools introduced in the case study; material handling and setups. Their respective cost drivers are: number of moves and number of setups. The case also presents two order-level cost pools: administrative cost pool with activity cost driver of number of orders and engineering supports cost pool with activity cost driver of maintenance hours. The last pool is facility-level which has a unit-level activity cost driver, machining hours, based on the hint given in the case study. Fig. 2 shows the activity-based cost <sup>fl</sup>ow down diagram for Willow Company.

![](/api/attachments/U3NX3Y2W/fulltext/images/2738d12d06ee99e94e08eed6ceab7290263915300a46e49989dd578e6ca6a03e.jpg)  
Fig. 1. Manufacturing process <sup>fl</sup>ow.

## 4. Order Management MIP decision support model

The objective of the Order Management DSS is to <sup>fi</sup>nd the most pro<sup>fi</sup>table and optimal combination of the ful<sup>fi</sup>lling ratio of the received orders. This should be accomplished by taking into account the orders' pro<sup>fi</sup>tability, the production resources productivity and availability. In ABC/M the overhead cost charged to each product is determined by identifying the actual consumption of the activity by each product, and then multiplying it by its respective unit cost driver.

For the purpose of modeling the <sup>fi</sup>rst part of DSS, we implemented the technique that was introduced by [16], solving the Order Management problem by integrating the ABC/M and MIP optimization techniques. The integration can be done by applying Cooper and Kaplan [6] homogenous cost pooling structure. According to their structure, the overhead costs can be assigned to four speci<sup>fi</sup>c homogenous cost pools; unit, batch, product, and facility level activities' cost pool.

The unit-level activities (machine time, direct material, direct labor, etc) cost pool includes the overhead costs that vary directly with the number of units produced. The batch-level activities (planning and tactical management, material handling, setup, etc.) cost pool which are the overhead costs invoked whenever a batch is processed. The product-level activities (process engineering, manufacturing equipments maintenance, product design, etc.) cost pool which are overhead costs incurred whenever a particular product is produced. In this study, the product-level is replaced by order-level which is overhead costs incurred whenever a particular order is processed. The facility sustaining activities' cost pool includes overhead costs such as rent, utilities, and facility management. Integrating the ABC/M approach into the Order Management DSS shows and clari<sup>fi</sup>es the role, importance, and source of each overhead cost in a production process in a more precise and reliable manner as compared to the TCA approach.

The developed mathematical Order Management Decision Support model pursues two goals: maximizing the pro<sup>fi</sup>t and minimizing the residual capacity. These two goals are incorporated into the model by applying Weighted Goal Programming (WGP) techniques. The general objective function is maximizing the pro<sup>fi</sup>t (sales revenue −production resources costs − holding costs) and minimizing the residual capacity simultaneously, subject to different constraints like production resources constraints, order commitment constraints, management discretionary constrains, and inventory constraints. The management discretionary factor is also added to the model by using a constraint that ful<sup>fi</sup>lls a certain number of orders completed.

The generic model is developed based on the following assumptions: processing times are deterministic, each product is manufactured in equal-size batches under a pull system, and each order consists of just one type of product. There is a possibility to satisfy the orders partially, completely, or even reject them.

In this study, the general homogenous costs' pooling structure, which has been used in previous studies, is replaced by a more detailed homogeneous costs' pooling structure. Instead of grouping all the batchlevel activities in one cost pool, we are dealing with two different batchlevel overhead cost pools; similarly for order-level activities. In addition, the facility-level overhead costs' pool is also considered in this case study. As mentioned before, for the Willow Company case study, the unit-level overhead activities' resources and costs are integrated into the prime costs. The applied notations are as follows:

i product index

t period of time index

o order index

j activities at unit-level index

k activities at batch-level index

l activities at order-level index

$r$ activity at facility-level index $d _ { l } ^ { + }$ amount of over capacity production (capacity surplus variable)

$d _ { l } ^ { - }$ amount of under capacity production (capacity slack variable)

![](/api/attachments/U3NX3Y2W/fulltext/images/9ca637a4f211d45b6fffa1746ef1670b49e2f3d6244262583706d5aa99390d07.jpg)  
Fig. 2. Activity-based cost <sup>fl</sup>ow diagram for Willow Company.

$p r _ { i }$ prime cost of product i

$a _ { k }$ batch-level k pool rate

$y _ { l }$ order-level l pool rate

$c _ { r }$ facility-level r pool rate

$h _ { i }$ holding cost of product i per period

$q _ { i j r }$ consumption rate of performing activity r at facility-level related to activity j at unit-level for product i

$u _ { i j k }$ consumption rate of performing activity k at batch-level related to activity j at unit-level for product i

$f _ { i l }$ consumption rate of performing activity l for product i

$b _ { i j }$ batch size of product i at activity j

$p _ { i }$ sales price of product i

$m _ { I }$ cost of stretching the production capacity

$m _ { 2 }$ cost of not using whole capacity

$m _ { 3 }$ preference coef<sup>fi</sup>cient of maximizing pro<sup>fi</sup>t

$m _ { 4 }$ preference coef<sup>fi</sup>cient of minimizing residual capacity

$O$ number of orders which should be ful<sup>fi</sup>lled completely

$D _ { i o t }$ demand quantity of product i in order o due in period t

$Q _ { j t }$ total available time to perform activity j in period t

$U _ { k t }$ total available time to perform activity k in period t

$F _ { l }$ total available time to perform activity l

$I _ { i t }$ inventory level of product i in period t

$P _ { i t }$ amount of product i produced in period i

$S _ { i o t }$ quantity of product i from order o sold in period t

$B _ { i j t }$ number of batches of product i produced in machine j in period t

$Y _ { i o t }$ the proportion of accepted order o from product i in period t $Y B _ { i o t }$ the binary form of $Y _ { i o t }$

In order to develop the multi-objective function we used WGP technique. Eq. (1) represents the objective function, which consists of two parts that pursue two different goals of the Decision Support model. The $m _ { i }$ represents each goal's signi<sup>fi</sup>cance or management preference coef<sup>fi</sup>cient for each goal. The <sup>fi</sup>rst part calculates the pro<sup>fi</sup>t, which is the revenue (multiplication of sales by the product price) minus the production process costs. The production process costs is the addition of the prime costs, overhead costs (batch-level, orderlevel, and facility-level) and product's holding costs. The second part of the objective function minimizes the residual capacity. According to this term any violation from the available Order Ful<sup>fi</sup>llment capacity has a certain penalty cost.

$$
\operatorname{Max} z = m _ {3} \times (\sum_ {t} \sum_ {o} \sum_ {i} p _ {i} \times S _ {i o t} - \sum_ {t} \sum_ {i} p r _ {i} \times\tag{1}
$$

$$
P _ {i t} - \sum_ {t} \sum_ {i} \sum_ {j} \sum_ {k} a _ {k} \times u _ {i j k} \times B _ {i j t} -
$$

$$
\sum_ {t} \sum_ {o} \sum_ {i} \sum_ {l} y _ {l} \times f _ {i l} \times Y _ {i o t} - \sum_ {t} \sum_ {o} \sum_ {i} \sum_ {j} \sum_ {r} c _ {r} \times
$$

$$
q _ {i j r} \times S _ {i o t} - \sum_ {i} \sum_ {t} h _ {i} \times I _ {i t}) - m _ {4} \times \left(\sum_ {l} m _ {1} d _ {l} ^ {+} + m _ {2} d _ {l} ^ {-}\right)
$$

Constraints (2) and (3) ensure that the available Order Ful<sup>fi</sup>llment resource capacity at unit-level and batch-level capacity, respectively, are not exceeded. Constraints (4) allow the diversity in batch sizes to exist.

$$
\sum_ {i} q _ {i j y} \times P _ {i t} \leq Q _ {j t} \quad \forall j, r, t
$$

$$
\sum_ {i} \sum_ {j} u _ {i j k} \times B _ {i j t} \leq U _ {k t} \quad \forall k, t\tag{2}
$$

ð<sup>3</sup>Þ

$$
P _ {i t} = b _ {i j} \times B _ {i j t} \quad \forall i, j, t\tag{4}
$$

Constraints (5) make sure that the production quantity meets the sales commitments of each order. Constraints (6) are the order-level activities capacity variation constraints. They ensure that we accept the orders considering the order-level activities available capacity.

The ratio of Order Ful<sup>fi</sup>llment is represented with the proportion ful<sup>fi</sup>llment decision variables $( Y _ { i o t } )$ . These decision variables can take any real number between 0 and 1, which represents the acceptance portion of each order.

$$
S _ {i o t} = D _ {i o t} \times Y _ {i o t}
$$

$$
\forall i, o, t\tag{5}
$$

$$
\sum_ {i} \sum_ {o} \sum_ {t} f _ {i l} \times Y _ {i o t} - d _ {l} ^ {+} + d _ {l} ^ {-} = F _ {l} \quad \forall l\tag{6}
$$

Constraints (7) incorporate the management discretionary factor into the model, which represents the number of orders (O) that management decides to ful<sup>fi</sup>ll completely. Constraints (8) ensure that if a speci<sup>fi</sup>c order is selected to be ful<sup>fi</sup>lled completely then the relevant ful<sup>fi</sup>llment ratio $( Y _ { i o t } )$ is equal to 100%. Constraints (9) make sure that the feasible area only includes the orders that exist. Accordingly, if the demand of a certain order from certain product at certain period $( D _ { i o t } )$ is equal to 0 then $Y _ { i o t }$ of that order must be equal to zero.

$$
\sum_ {i} \sum_ {o} \sum_ {t} Y B _ {i o t} \geq 0\tag{7}
$$

$$
Y _ {i o t} \geq Y B _ {i o t} \quad \forall i, o, t\tag{8}
$$

$$
D _ {i o t} \geq Y _ {i o t} \quad \forall i, o, t\tag{9}
$$

Constraints (10) and (11) determine the inventory level for each product type at the end of each period of time.

$$
I _ {i 0} = 0 \quad \forall i\tag{10}
$$

$$
I _ {i (t - 1)} + P _ {i t} - I _ {i t} = \sum_ {o} S _ {i o t} \quad \forall i, t \geq 1\tag{11}
$$

Finally, constraints (12) to (14) are the non-negativity constraints, and constraints (15) are the binary constraints.

$$
P _ {i t} \geq 0 \quad \forall i, t\tag{12}
$$

$$
B _ {i j t} \geq 0 \quad \forall i, j, t\tag{13}
$$

$$
0 \leq Y _ {i o t} \leq 1 \quad \forall i, o, t\tag{14}
$$

$$
Y B _ {i o t} = 0 \text { or } 1 \quad \forall i, o, t\tag{15}
$$

The model has an illustrative emphasis on the effect of overhead costs in the decision making process by replacing the homogenous order and batch-level overhead costs pool with a more detailed and activity oriented overhead cost pools. It also integrates the facilitylevel activities overhead costs pool. In fact, the model elaborates on how the signi<sup>fi</sup>cant role of overhead costs are in the procedure of Order Management decision making in a better way as compared to the previous MIP Order Management models. In the following section the model is validated by using a numerical example.

## 5. Numerical example

In this case study, management is required to make decisions regarding sixteen received orders over the next twelve periods of time (months). The list of the received orders and their speci<sup>fi</sup>cations are shown in Table 1. Each order consists of only one type of product either the Deluxe or the Basic model. The objective is to <sup>fi</sup>nd the optimal combination of Order Ful<sup>fi</sup>llment ratio, the combination that maximizes the pro<sup>fi</sup>t and minimizes the residual capacity for the system. All the required <sup>fi</sup>nancial and operational parameters are extracted from the Willow Company case study.

Even though the Willow Company case study does not include holding costs, we decided that such a variable is important in a realistic scenario. Therefore, a holding cost has been assigned to each product. An applicable holding cost (h ) is assumed to be equal to 5% of the ABC/M-based unit manufacturing cost as indicated in reference [10]. Therefore, the amounts used in the MIP model are 4.22 and 9.06 for the Basic and the Deluxe models, respectively, in dollar/unit month. A further elaboration of holding costs requires incorporating inventory-related activities into the model structure.

Table 1  
Order speci<sup>fi</sup>cations.

<table><tr><td>Order number</td><td>Product type</td><td>Period due</td><td>Quantity</td></tr><tr><td>1</td><td>Basic</td><td>1</td><td>3500</td></tr><tr><td>2</td><td>Basic</td><td>2</td><td>4600</td></tr><tr><td>3</td><td>Deluxe</td><td>2</td><td>2500</td></tr><tr><td>4</td><td>Basic</td><td>2</td><td>3000</td></tr><tr><td>5</td><td>Deluxe</td><td>3</td><td>2500</td></tr><tr><td>6</td><td>Basic</td><td>5</td><td>3200</td></tr><tr><td>7</td><td>Basic</td><td>5</td><td>4700</td></tr><tr><td>8</td><td>Deluxe</td><td>5</td><td>1900</td></tr><tr><td>9</td><td>Deluxe</td><td>6</td><td>4000</td></tr><tr><td>10</td><td>Basic</td><td>8</td><td>4500</td></tr><tr><td>11</td><td>Deluxe</td><td>9</td><td>3000</td></tr><tr><td>12</td><td>Basic</td><td>10</td><td>3500</td></tr><tr><td>13</td><td>Basic</td><td>11</td><td>3000</td></tr><tr><td>14</td><td>Basic</td><td>12</td><td>5000</td></tr><tr><td>15</td><td>Deluxe</td><td>12</td><td>2700</td></tr><tr><td>16</td><td>Deluxe</td><td>12</td><td>5000</td></tr></table>

The manufacturing facility can produce the Basic and the Deluxe models in batch sizes of 100 and 170 units, respectively, based on the given projected production amount and the number of setups for each product. The resource annual capacity at different level has been determined based on the cumulative forecasted annual resource consumption given in the case study for producing the projected amount for each product. The preference coef<sup>fi</sup>cients (m to m ) are equal to 1, 0.5, 1, and 2, respectively given from [16]. According to this combination the goal of minimizing the residual capacity has higher signi<sup>fi</sup>cance compared to the pro<sup>fi</sup>t maximization goal.

The model is coded with the optimization software Lingo Version 10 and applied to the different scenarios, different desirable number of orders (O) which should be satis<sup>fi</sup>ed completely, on a 3.00 GHz Pentium-4 processor with 1 GB of RAM. The average computational time for the presented model is less than 5 s.

As discussed before, the goal is to <sup>fi</sup>nd the optimal combination of ful<sup>fi</sup>lling ratio of the received orders by taking into account the production resources capacity availability and pro<sup>fi</sup>tability factor for each order. According to the results shown in Table 2, the optimal value is \$3,694,067.00 which considers all the costs, including the facility-level costs (<sup>fi</sup>xed overhead costs) by relaxing the constraint of ful<sup>fi</sup>lling a certain number of orders completely.

The related optimal solution is by ful<sup>fi</sup>lling <sup>fi</sup>ve orders completely and six orders partially. The table also shows the effect of integrating the management discretionary factor into the model where a certain number of orders have to be ful<sup>fi</sup>lled completely. Management strategy for reaching higher customer satisfaction may require more number of orders to be ful<sup>fi</sup>lled completely. According to Table 2, demanding more than <sup>fi</sup>ve completely ful<sup>fi</sup>lled orders diminishes the company's pro<sup>fi</sup>t. In fact, management would sacri<sup>fi</sup>ce the short-term pro<sup>fi</sup>t for having a higher customer satisfaction level and long-term pro<sup>fi</sup>t. This is the consequence of having the set of constraints (7) as a binding constrain.

The developed PTP model, by integrating the ABC/M information into the mathematical Order Management Decision Support model, elaborates more on the role of costs and especially overhead costs in the Order Management process compared to the more traditional CPT and ATP models. However, the presented MIP model solely cannot provide an ontime detailed cost analysis for the different Order Ful<sup>fi</sup>llment scenarios because of its static nature. In fact, it does not take advantage of all the information generated by applying ABC/M cost structure. Therefore, there is a need for a complementary decision support model.

The Decision Support System presented in this paper can be used as a cost monitoring and cost analysis tool with the ability to evaluate and foresee the effects of each taken decision on the system status. The next steps explain how the output of the MIP model can be used as an input of the System Dynamics-based cost analysis model and how ABC/M is used as a common approach to link these two models and introduces them as a hybrid DSS.

## 6. System Dynamics decision support model

The main advantage of System Dynamics as a continuous simulation approach versus a discrete event simulation approach is its ability to continuously update the system variables after each decision is taken (simulation run). Within this optic the next simulation run will be based on the updated variables from the previous run. SD has been applied in a wide range of areas; corporate planning and policy design, biological and medical modeling, energy and environment, software engineering, and supply chain management, according to the study of Angerhofer and Angelides [2].

Gregoriades and Karakostas [9] presented a framework to show how SD can integrate with business objects and act as a powerful simulation approach to help organizations in pursuing their goals and monitoring their processes. We believe the ability of SD in on-time evaluation of the system status can be used in cost monitoring process as well. The remaining of this study is focused on presenting a novel cost monitoring model for Order Management problems and the combination with the developed MIP model. The combination of these two models creates the hybrid Decision Support System. Fig. 3 dashed lines show the <sup>fl</sup>ow of information.

Table 2  
Comparison table for ful<sup>fi</sup>lling rates.

<table><tr><td colspan="7">Minimum desirable amount of orders which should be satisfied completely</td></tr><tr><td>Order</td><td>5 or less fulfilling rate %</td><td>6 Fulfilling rate %</td><td>7 Fulfilling rate %</td><td>8 Fulfilling rate %</td><td>9 Fulfilling rate %</td><td>10 Fulfilling rate %</td></tr><tr><td>1</td><td>86</td><td>86</td><td>86</td><td>60</td><td>31</td><td>No feasible solution</td></tr><tr><td>2</td><td>65</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>3</td><td>14</td><td>14</td><td>14</td><td>14</td><td>8</td><td></td></tr><tr><td>4</td><td>-</td><td>100</td><td>100</td><td>100</td><td>100</td><td></td></tr><tr><td>5</td><td>27</td><td>27</td><td>6</td><td>27</td><td>-</td><td></td></tr><tr><td>6</td><td>72</td><td>72</td><td>72</td><td>100</td><td>100</td><td></td></tr><tr><td>7</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td></td></tr><tr><td>8</td><td>45</td><td>45</td><td>100</td><td>30</td><td>100</td><td></td></tr><tr><td>9</td><td>17</td><td>17</td><td>17</td><td>-</td><td>-</td><td></td></tr><tr><td>10</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td></td></tr><tr><td>11</td><td>68</td><td>68</td><td>68</td><td>100</td><td>100</td><td></td></tr><tr><td>12</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td></td></tr><tr><td>13</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td></td></tr><tr><td>14</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td></td></tr><tr><td>15</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>16</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td></td></tr><tr><td>Profit $</td><td>3,694,067.00</td><td>3,693,925.00</td><td>3,681,280.00</td><td>3,650,092.00</td><td>3,614,196.00</td><td></td></tr></table>

The SD model is developed based on the earlier variables as de<sup>fi</sup>ned in the MIP model and with respect to the similar applied ABC/M structure. This represents ABC/M as a common approach between the MIP and SD decision support models. These two models are linked through a spreadsheet generated by the MIP model. The main objective of the SD model is to estimate real-time selling price and adjust pool rates in each month, based on the previous months' Order Ful<sup>fi</sup>llment policy received from the MIP model.

Basically, management decides about the scenario of the Order Ful<sup>fi</sup>llment, number of orders that should be ful<sup>fi</sup>lled completely, and the MIP model provides the optimal solution for the desirable scenario; this includes the Order Ful<sup>fi</sup>llment rates for each order, as can be observed in Table 2. In the next step, the output of MIP model is used as the input for SD model in order to have the possibility of ontime monitoring of related costs and to de<sup>fi</sup>ne the minimum products' selling price in each period regarding the previous decisions and desirable markup.

The SD model structure contains level variables, rate variables, and auxiliary variables which are all related to each other within and without <sup>fl</sup>ows. Level or stock variables are represented by rectangles and they show the level of discussed unit (e.g. products or money) in the system at different periods of time. The combination of level variables normally de<sup>fi</sup>nes the status of the system at different times. Rate variables control the pace of change in a speci<sup>fi</sup>c level variable and are represented by valves in the model; in fact, they determine the <sup>fl</sup>ow. The auxiliary variables, which are shown with clear boxes, simplify the model and make it easier to understand. The clouds play the role of source and sink nodes for the in and out <sup>fl</sup>ows. This means the <sup>fl</sup>ow comes from or goes to outside boundaries of the model. The variables within single left and right-pointing angle quotes are shadow variables. They are substitute of any level, rate, or auxiliary variables to avoid the model to be crowded and unclear. The SD model is developed in Vensim software with the similar legends discussed in [28] and it includes six different parts.

## 6.1. First part

The <sup>fi</sup>rst part of the SD model, Fig. 4, calculates the total holding cost separately for each product by getting the exact level of inventory for each type of product in each period and the related holding fractional ratio for each case. All the initial pool rates and the other related constants (e.g. batch sizes, markups, holding cost) are similar to the MIP model. The Order Ful<sup>fi</sup>llment rate, production rates and shipping rates are extracted from the output of MIP part of the hybrid model. As mentioned before, the SD part can read the MIP model output from the spreadsheet generated by LINGO.

## 6.2. Second to sixth part

All the <sup>fi</sup>ve learning loops that determine and adjust the pool rates are shown in Figs. 5 to 9. The pool rates' adjustment loops help the model to de<sup>fi</sup>ne the selling price based on the actual Order Ful<sup>fi</sup>llment costs. For the batch-level-1 (material handling), Fig. 5, the loops are batch-level-1 cost rate for the Deluxe model → total bacth-level-1 cost for Deluxe model → total batchlevel-1 cost → batch-level-1 pool rate and the same loop for the Basic model. These two loops adjust the batch-level-1 pool rate in each period based on the material handling activity resource consumption in the previous periods. The batch level-1 pool rate is also related to the total consumption of batch-level-1 cost pool activity driver. This level variable is estimated via batch level-1 activity cost driver consumption ratio for the Basic and Deluxe models, which eventually depends on the products' batch size, production rate, and batch-lelvel-1activity consumption ratio.

Fig. 6 shows the relations for the batch-level-2 (Setup). The pool rate adjustment loops are similar to the batch-level-1 loops. The total consumption of bacth-level-2 cost pool activity driver is estimated in each period of time via the product's production rate, batch size, and batch-level-2 activity driver consumption ratio, which is similar to the previous cost pool.

Hybrid MIP-SD Decision Support System  
![](/api/attachments/U3NX3Y2W/fulltext/images/0c5859ed5aca4ccbbdd74489b74bd0fe2ece673e3ae4df372d2f28030ba23bde.jpg)  
Fig. 3. Hybrid Order Management Decision Support System.

![](/api/attachments/U3NX3Y2W/fulltext/images/a5b403a58387df8ece694f0cb81877c7636525c07ecc3a6e80e7677ac780179c.jpg)  
Fig. 4. Inventory level and holding cost approximation.

The relations for order-level-1, which is a homogenous cost pool, contain their different MOH costs; procurement material, paying supplier, and receiving goods; it is presented in Fig. 7. In this case the pool rate adjustment loops are order-level-1 cost rate for Deluxe model→ total order-level-1 cost for Deluxe model→total cost of orderlevel-1cost pool→cost-level-1 pool rate and the same loop for the Basic model. In the order-level-1 cost pool, the MOH costs are estimated via order ful<sup>fi</sup>llment rates for the Deluxe and Basic models and orderlevel-1 activity cost driver consumption ratio.

![](/api/attachments/U3NX3Y2W/fulltext/images/3baf7332e44e11eb64a656362b1efcde1f51076951b1d9747beff8db8ed8be2d.jpg)  
Fig. 5. Batch-level-1 pool rates adjustment loops.

![](/api/attachments/U3NX3Y2W/fulltext/images/f2bbb41b1dc8d40f804bebe1564ff43aaa902db9e83c9aef279c8dbcde5e0283.jpg)  
Fig. 6. Batche-level-2 pool rates adjustment loops.

![](/api/attachments/U3NX3Y2W/fulltext/images/56d2f726a2ee5f2d17e7138c9c8ea6a3b695d1718d0948e906eeac117f71e9d4.jpg)  
Fig. 7. Order-level-1 pool rates adjustment loops.

![](/api/attachments/U3NX3Y2W/fulltext/images/6118bad2c731bdb63d0c8241dec23301cb2eda9d815661ad3db3a9607b64d5e0.jpg)  
Fig. 8. Order-level-2 pool rates adjustment loops.

For the order-level-2 homogeneous cost pool, engineering and maintenance, the relations between variables are presented in Fig. 8. The relevant adjustment loops are designed similar to the order-level-1 MOH costs for the Basic and Deluxe models. The total consumption of order-level-2 cost pool activity driver is estimated through order ful<sup>fi</sup>llment rates for each product model and the order-level-2 activity cost driver consumption ratio.

Fig. 9 presents the relations between variables involved estimating the facility-level MOH cost. The pool rate adjustment loops are similar to the previous cost pools. We are considering the facility-level activity cost driver consumption ratio and the orders' shipping rates in order to estimate the total consumption of the related activity cost driver.

![](/api/attachments/U3NX3Y2W/fulltext/images/3855ff16a6e6fdb42d88d5dba1a7f89e993ab95239f4f2a43af3f3fb4cea8056.jpg)  
Fig. 9. Facility-level pool rates adjustment loops.

![](/api/attachments/U3NX3Y2W/fulltext/images/d61ad8e2e02885f42e282cf203c36f4cf257e14764283939b20843e7f77006ae.jpg)  
Fig. 10. Selling price and product cost estimation

## 6.3. Seventh part

The prime costs, overhead costs, cost of goods manufactured, and selling price for each product type are determined in Fig. 10. The prime costs are calculated based on the production rates and fractional production ratios which are the same as the prime costs per unit projected in the Willow Company case study. The overhead cost for each model is equal to the summation of all the overhead costs at batch, product, and facility level for the speci<sup>fi</sup>c product. Adding this amount to the related holding costs and prime costs provides the cost of goods manufactured. The selling price for each product is estimated by adding the speci<sup>fi</sup>c markup for each product to the related cost of goods manufactured per unit for that product. The related equations to the SD model variables are presented in alphabetical order in the Appendix.

The model can be applied to the different Order Ful<sup>fi</sup>llment scenarios in order to appraise the attributes of each Order Ful<sup>fi</sup>llment policy and evaluate the effect of the management discretionary factor on the manufacturing cost and subsequently on the selling price (selling price =(1+markup)×cost of goods manufactured per unit). The variation in the selling price based on the number of orders that should be ful<sup>fi</sup>lled completely is shown in Table 3. The indicated prices in period one are the prices used by the MIP model.

The selling prices estimated by the SD model are calculated through the actual manufacturing cost. The estimated prices are used as a reference price in implementing the Order Ful<sup>fi</sup>llment policy, instead of the selling price used by MIP model. The calculated selling prices for each product per period are indeed a lower limit for the products selling price. Thus, if management is willing to achieve the desirable projected pro<sup>fi</sup>t, it should charge the customer no less than the calculated selling price per period for each type of product. According to the SD model output, Table 3, ful<sup>fi</sup>lling more orders completely would require to increase the selling price.

Table 3 Selling price variation  
Minimum desirable amount of orders which should be satis<sup>fi</sup>ed completely

<table><tr><td rowspan="2">Period</td><td colspan="2">5 or less selling price $</td><td colspan="2">6 Selling price $</td><td colspan="2">7 Selling price $</td><td colspan="2">8 Selling price $</td><td colspan="2">9 Selling price $</td></tr><tr><td>Basic</td><td>Deluxe</td><td>Basic</td><td>Deluxe</td><td>Basic</td><td>Deluxe</td><td>Basic</td><td>Deluxe</td><td>Basic</td><td>Deluxe</td></tr><tr><td>1</td><td>180.000</td><td>360.000</td><td>180.000</td><td>360.000</td><td>180.000</td><td>360.000</td><td>180.000</td><td>360.000</td><td>180.000</td><td>360.000</td></tr><tr><td>2</td><td>178.755</td><td>347.461</td><td>178.755</td><td>347.461</td><td>178.755</td><td>347.461</td><td>178.361</td><td>347.461</td><td>177.923</td><td>347.461</td></tr><tr><td>3</td><td>178.429</td><td>356.987</td><td>178.461</td><td>356.987</td><td>178.461</td><td>356.987</td><td>179.591</td><td>356.955</td><td>180.829</td><td>356.999</td></tr><tr><td>4</td><td>178.051</td><td>350.247</td><td>178.075</td><td>350.247</td><td>178.075</td><td>349.049</td><td>179.933</td><td>350.215</td><td>181.999</td><td>350.852</td></tr><tr><td>5</td><td>179.361</td><td>349.443</td><td>179.378</td><td>349.443</td><td>179.624</td><td>352.819</td><td>181.482</td><td>349.415</td><td>184.531</td><td>356.819</td></tr><tr><td>6</td><td>183.081</td><td>350.344</td><td>183.096</td><td>350.344</td><td>182.746</td><td>361.395</td><td>185.620</td><td>349.962</td><td>188.559</td><td>366.354</td></tr><tr><td>7</td><td>182.259</td><td>349.392</td><td>182.272</td><td>349.392</td><td>181.913</td><td>358.145</td><td>184.460</td><td>350.457</td><td>186.896</td><td>363.199</td></tr><tr><td>8</td><td>182.703</td><td>348.386</td><td>182.715</td><td>348.386</td><td>182.426</td><td>355.685</td><td>184.658</td><td>354.435</td><td>186.817</td><td>364.481</td></tr><tr><td>9</td><td>184.298</td><td>350.759</td><td>184.309</td><td>350.759</td><td>184.138</td><td>356.718</td><td>186.064</td><td>360.160</td><td>188.079</td><td>368.187</td></tr><tr><td>10</td><td>184.254</td><td>356.031</td><td>184.263</td><td>356.031</td><td>184.106</td><td>360.747</td><td>185.858</td><td>368.390</td><td>187.668</td><td>374.675</td></tr><tr><td>11</td><td>184.859</td><td>355.623</td><td>184.867</td><td>355.623</td><td>184.756</td><td>360.227</td><td>186.271</td><td>367.541</td><td>187.871</td><td>373.705</td></tr><tr><td>12</td><td>185.142</td><td>355.856</td><td>185.150</td><td>355.856</td><td>185.061</td><td>360.302</td><td>186.403</td><td>367.384</td><td>187.828</td><td>373.380</td></tr><tr><td>Average</td><td>181.766</td><td>352.544</td><td>181.778</td><td>352.544</td><td>181.672</td><td>356.628</td><td>183.225</td><td>356.865</td><td>184.917</td><td>363.009</td></tr></table>

Table 4  
Total cost of goods manufactured per model.

<table><tr><td colspan="6">Minimum desirable amount of orders which should be satisfied completely</td></tr><tr><td>Product</td><td>5 or less cost of goods manufactured$</td><td>6 Cost of goods manufactured$</td><td>7 Cost of goods manufactured$</td><td>8 Cost of goods manufactured$</td><td>9 Cost of goods manufactured$</td></tr><tr><td>Basic</td><td>2,343,900.00</td><td>2,344,000.00</td><td>2,256,110.00</td><td>2,359,860.00</td><td>2,289,830.00</td></tr><tr><td>Deluxe</td><td>883,103.00</td><td>883,103.00</td><td>986,631.00</td><td>911,711.00</td><td>1,022,440.00</td></tr></table>

Table 5  
Total production per model.

<table><tr><td colspan="6">Minimum desirable amount of orders which should be satisfied completely</td></tr><tr><td>Product</td><td>5 or less total production unit</td><td>6 Total production unit</td><td>7 Total production unit</td><td>8 Total production unit</td><td>9 Total production unit</td></tr><tr><td>Basic</td><td>27,000</td><td>27,000</td><td>26,000</td><td>27,000</td><td>26,000</td></tr><tr><td>Deluxe</td><td>4930</td><td>4930</td><td>5440</td><td>4930</td><td>5440</td></tr></table>

Table 6  
Total overhead cost per model.

<table><tr><td colspan="6">Minimum desirable amount of orders which should be satisfied completely</td></tr><tr><td>Product</td><td>5 or less total overhead cost $</td><td>6 Total overhead cost $</td><td>7 Total overhead cost $</td><td>8 Total overhead cost $</td><td>9 Total overhead cost $</td></tr><tr><td>Basic</td><td>94,247.20</td><td>94,338.00</td><td>90,696.40</td><td>94,114.10</td><td>90,173.30</td></tr><tr><td>Deluxe</td><td>71,830.60</td><td>71,830.60</td><td>79,327.80</td><td>71,762.50</td><td>79,090.50</td></tr></table>

The rise in the average products' selling price could be the consequence of an increase in the total cost of goods manufactured (that could be the result of changes in the total overhead costs, total prime costs, and/or total holding costs) and/or an increase in the manufacturing system residual capacity (this could be the result of changes in the production rate).Table 4 exhibits the total cost of goods manufactured for each model. Table 5 shows the related production amount and Table 6 displays the total overhead costs for each product type. Similar tables can be extracted from the model output for the other variables.

![](/api/attachments/U3NX3Y2W/fulltext/images/3e0ee31bb47a5b4e925fb869d92e971a85882c78bf72d6fbd571e68c0082e249.jpg)  
Fulfilling 5,6, or 7 Orders Completely  
Fulfilling 8 Orders Completely  
Fulfilling 9 Orders Completely

The variations in the cost amounts are because of the selected order ful<sup>fi</sup>llment policy, which de<sup>fi</sup>nes the inventory policy and the production rates. For example, in the case of 6 orders to be completely ful<sup>fi</sup>lled, the total production amount according to the Table 5 for the Deluxe model is 4930 units and for the cases of 7 and 8 orders to be completely ful<sup>fi</sup>lled are 5440 and 4930 units respectively. Therefore, the increases in both MOH and the manufacturing costs from 6 to 7 as well as the decreases from 7 to 8 can be justi<sup>fi</sup>ed.

However, the production amount is not the only reason in cost variations. The other reason is due to the changes in the pool rates. The model adjusts the pool rates after each run. This justi<sup>fi</sup>es the difference between the MOH costs for the Basic model from the case of 5 to the case of 6, although the total production amount remains the same. The other reason for the cost changes is due to the inventory cost which is different for each order ful<sup>fi</sup>llment policy.

The model also has the ability to adjust the pool rates. Fig. 11 reveals the adjustment for the order-level activities pool rates in different Order Ful<sup>fi</sup>llment scenarios. The disparity between the order-level pool rates under different ful<sup>fi</sup>llment scenarios is because

![](/api/attachments/U3NX3Y2W/fulltext/images/cd0e410b234ad99dc0aad7835a4bf145b35f09f4ca1f21fe2d0dd0a40a9da051.jpg)  
Fig. 11. Order-level activities pool rates.

![](/api/attachments/U3NX3Y2W/fulltext/images/8b58702d4bedf25d1bb595a187b2d75380699c132c480c19df1c7f98c53be8b9.jpg)  
Fulfilling 5,6, or 7 Orders Completely Fulfilling 8 Orders Completely Fulfilling 9 Orders Completely

![](/api/attachments/U3NX3Y2W/fulltext/images/fa5a762452cb3003d633d232a1b346db563aa297e9458d74ffa04ee75f454121.jpg)  
Fulfilling 5,6, or 7 Orders Completely Fulfilling 8 Orders Completely Fulfilling 9 Orders Completely

![](/api/attachments/U3NX3Y2W/fulltext/images/3c2e57a9e0ca602a16c70c92785a1bb94d518030e3ee298b58d3802114b679f8.jpg)  
Fulfilling 5,6, or 7 Orders Completely Fulfilling 8 Orders Completely Fulfilling 9 Orders Completely

Fig. 12. Batch-level and facility-level activities pool rates

of the correlation between the Order Ful<sup>fi</sup>llment ratios and the orderlevel activities. In contrast, in Fig. 12 there is no correlation between batch-level and facility-level activities' pool rates and the Order Ful<sup>fi</sup>llment scenario. Accordingly, the pool rates have not changed for those activities at different Order Ful<sup>fi</sup>llment scenarios.

## 7. Conclusion and future work

This study introduces a novel modeling approach by integrating System Dynamics and MIP programming in order to develop a powerful hybrid PTP Decision Support System for the Supply Chain Order Management problem. The developed DSS system assists management in monitoring, analyzing and foreseeing the consequences and outcomes of each decision and monitors their business competitiveness factors. In the <sup>fi</sup>rst step, we developed a mathematical Decision Support model based on the ABC/M cost structure. In the MIP model a more detailed and activity-oriented cost structure is used to enhance the model accuracy.

As a second step, the ABC/M-based SD model presented a complementary tool to the MIP model. This model identi<sup>fi</sup>es the interconnections and correlations between the Order Management decision making variables. The SD model helps management to investigate and examine the further consequences of executing the different Order Ful<sup>fi</sup>llment decision scenarios expansively. The model adjusts the pool rates based on the actual costs, de<sup>fi</sup>nes the on-time selling price based on the Order Management ful<sup>fi</sup>llment policy, and can also serve as a cost monitoring tool with the purpose of checking the costs behavior at different levels and for different products. ABC/M, as a common modeling approach, makes two models work together as a hybrid Decision Support System.

The hybrid DSS output indicates that ful<sup>fi</sup>lling more orders actually decreases the company's pro<sup>fi</sup>t (MIP part output), and requires adjusting the product selling price (SD part output). Depending on the product type and applied Order Ful<sup>fi</sup>llment scenario, the selling price could be decreased or increased compared to the initial selling price used in the MIP model. Reducing the selling price can give more satisfaction to the customer if the level of order ful<sup>fi</sup>llment remains the same. However, increasing the selling price may result in a lower or higher customer satisfaction level. This depends on the customer's understanding and the value given to a better order ful<sup>fi</sup>llment service. Thus, it should be considered that the result of ful<sup>fi</sup>lling more orders completely actually may con<sup>fl</sup>ict with the original intention of increasing customer satisfaction.

This study can be further expanded by integrating the cost of backlog among the decision making factors, which improves the model accuracy level. Illustrating the role of raw material suppliers and raw material inventory into the hybrid system through the integration of the supplier selection decision based on the supplier costs analysis and raw material holding costs could enhance the model legitimacy level. Another potential extension of this research is by using a similar approach to evaluate the inventory cost. Moreover, a comprehensive design of experiments can be used to analyze the model output and price variations.

## Appendix

1. Basic model cost of goods manufactured=total overhead cost for Basic model + Total Prime Cost of Basic Model+ Total Holding Cost of Basic Model Units: Dollar

2. Basic model cost of goods manufactured per unit=IF THEN ELSE (Total Production of Basic ModelN0, Basic model cost of goods manufactured/Total Production of Basic Model, 84.4) Units: Dollar/Unit

3. Basic model holding cost coef<sup>fi</sup>cient=0.05−Units: 1/Month

4. Basic model markup=1.1327−Units: Dmnl

5. Basic model order ful<sup>fi</sup>llment rates: = GET XLS DATA(‘FB.xls’, ‘Sheet1’, ‘1’, ‘B3’)−Units: Order/Month

6. Basic Model Production Rate: = GET XLS DATA(‘PB.xls’, ‘Sheet1’, ‘1’, ‘B3’) Units: Unit/Month

7. Basic model selling price=(1+Basic model markup)∗Basic model cost of goods manufactured per unit−Units: Dollar/Unit

8. Basic Model Shipping Rate: =GET XLS DATA(‘SB.xls’, ‘Sheet1’, ‘1’, ‘B3’) − Units: Unit/Month

9. batch size of Basic model=1000−Units: Unit/Batch

10. batch size of Deluxe model=170−Units: Unit/Batch

11. “batch-level-1 (material handling) pool rate”=IF THEN ELSE(“total batch-level-1 (material handling) cost”N0, “total batch-level-1 (material handling) cost”/“Total Consumption Batch-Level-1 Cost Pool Activity Driver (Number of Moves)”, 20)−Units: Dollar/Move

12. “batch-level-1 activity cost driver (number of moves) consumption ratio by Basic model”=Basic Model Production Rate/batch size of Basic model∗ “batch-level-1 activity cost driver consumption ratio by each batch of Basic model”−Units: Move/Month

13. “batch-level-1 activity cost driver (number of moves) consumption ratio by Deluxe model”=Deluxe Model Production Rate/ batch size of Deluxe model∗“batch-level-1 activity cost driver consumption ratio by each batch of Deluxe model”−Units: Move/Month

14. “batch-level-1 activity cost driver consumption ratio by each batch of Basic model”=100−Units: Move/Batch

15. “batch-level-1 activity cost driver consumption ratio by each batch of Deluxe model”=66.67−Units: Move/Batch

16. “Batch-Level-1 Cost (Material Handling) Rate for Basic Model”=“batch-level-1 activity cost driver (number of moves) consumption ratio by Basic model” “batch-level-1(material handling) pool rate”−Units: Dollar/Month

17. “batch-level-2 (equipments setup) pool rate”=IF THEN ELSE (“total batch-level-2 (equipments setup) cost” N0, “total batchlevel-2 (equipments setup) cost”/“Total Consumption Batch-Level-2 Cost Pool Activity Driver (Number of Setups)”, 1200) −Units: Dollar/Setup

18. “batch-level-2 activity cost driver (number of setups) consumption ratio by Basic model”=Basic Model Production Rate/ batch size of Basic model ∗ “batch-level-2 activity cost driver consumption ratio by each batch of Basic model” − Units: Setup/Month

19. “batch-level-2 activity cost driver (number of setups) consumption ratio by Deluxe model”=Deluxe Model Production Rate/batch size of Deluxe model∗“batch-level-2 activity cost driver consumption ratio by each batch of Deluxe model” Units: Setup/Month

20. “batch-level-2 activity cost driver consumption ratio by each batch of Basic model”=1 Units: Setup/Batch

21. “batch-level-2 activity cost driver consumption ratio by each batch of Deluxe model”=1−Units: Setup/Batch

22. “Batch-Level-2 Cost (Equipments Setup) Rate for Basic Model” =“batch-level-2 (equipments setup) pool rate” ∗ “batchlevel-2 activity cost driver (number of setups) consumption ratio by Basic model”−Units: Dollar/Month

23. “Batch-Level-2 Cost (Equipments Setup) Rate for Deluxe Model” = “batch-level-2 (equipments setup) pool rate” ∗ “- batch-level-2 activity cost driver (number of setups) consumption ratio by Deluxe model”−Units: Dollar/Month

24. “Batch-Level-l Cost (Material Handling) Rate for Deluxe Model” =“batch-level-1 (material handling) pool rate” ∗ “batchlevel-1 activity cost driver (number of moves) consumption ratio by Deluxe model”−Units: Dollar/Month

25. Deluxe model cost of goods manufactured=total overhead cost for Deluxe model+Total Prime Cost of Deluxe Model+Total Holding Cost of Deluxe Model−Units: Dollar

26. Deluxe model cost of goods manufactured per unit=IF THEN ELSE(Total Production of Deluxe ModelN0,Deluxe model cost of goods manufactured/Total Production of Deluxe Model, 181.21) Units: Dollar/Unit

27. Deluxe model holding cost coef<sup>fi</sup>cient=0.05−Units: 1/Month

28. Deluxe model markup=0.9866−Units: Dmnl

29. Deluxe model order ful<sup>fi</sup>llment rates:=GET XLS DATA(‘FD.xls’, ‘Sheet1’, ‘1’, ‘B3’) -Units: Order/Month

30. Deluxe Model Production Rate:=GET XLS DATA(‘PD.xls’, ‘Sheet1’, ‘1’, ‘B3’) − Units: Unit/Month

31. Deluxe model selling price=(1+Deluxe model markup)∗Deluxe model cost of goods manufactured per unit−Units: Dollar/ Unit

32. Deluxe Model Shipping Rate:=GET XLS DATA(‘SD.xls’, ‘Sheet1’, ‘1’, ‘B3’) − Units: Unit/Month

33. “Facility-Level (Providing Space) Cost Rate for Basic Model”=“- facility-level (providing space) pool rate” ∗ “facility-level activity cost driver (machining hours) consumption ratio by Basic model”−Units: Dollar/Month

34. “Facility-Level (Providing Space) Cost Rate for Deluxe Model” = “facility-level (providing space) pool rate” ∗ “facility-level activity cost driver (machining hours) consumption ratio by Deluxe model”−Units: Dollar/Month

35. “facility-level (providing space) pool rate”=IF THEN ELSE(“total cost of facility-level (providing space) cost pool” N 0, “total cost of facility-level (providing space) cost pool”/“Total Consumption Facility-Level Cost Pool Activity Driver (Machining Hours)”, 2) Units: Dollar/MachiningHr

36. “facility-level activity cost driver (machining hours) consumption ratio by Basic model”=Basic Model Shipping Rate∗“- facility-level activity cost driver consumption ratio by each unit of Basic model” Units: MachiningHr/Month

37. “facility-level activity cost driver (machining hours) consumption ratio by Deluxe model”=Deluxe Model Shipping Rate∗ “- facility-level activity cost driver consumption ratio by each unit of Deluxe model”−Units: MachiningHr/Month

38. “facility-level activity cost driver consumption ratio by each unit of Basic model”=0.25−Units: MachiningHr/Unit

39. “facility-level activity cost driver consumption ratio by each unit of Deluxe model”=0.5 -Units: MachiningHr/Unit

40. FINAL TIME=12−Units: Month

41. fractional prime cost ratio for Basic model=80−Units: Dollar/Unit

42. fractional prime cost ratio for Deluxe model=160−Units: Dollar/Unit

43. Holdeing Cost Rate of Deluxe Model=holding cost fractional ratio for Deluxe model ∗Inventory Level of Deluxe Model −Units: Dollar/Month

44. holding cost fractional ratio for Basic model=Basic model holding cost coef<sup>fi</sup>cient Basic model cost of goods manufactured per unit−Units: Dollar/(Unit ∗Month)

45. holding cost fractional ratio for Deluxe model=Deluxe model holding cost coef<sup>fi</sup>cient∗Deluxe model cost of goods manufactured per unit−Units: Dollar/(Month∗ Unit)

46. Holding Cost Rate of Basic Model=holding cost fractional ratio for Basic model∗Inventory Level of Basic Model−Units: Dollar/ Month

47. INITIAL TIME=1 Units: Month

48. Inventory Level of Basic Model=INTEG (Basic Model Production Rate-Basic Model Shipping Rate,0)−Units: Unit

49. Inventory Level of Deluxe Model = INTEG (Deluxe Model Production Rate-Deluxe Model Shipping Rate,0) − Units: Unit

50. Prime Cost Rate of Basic Model =Basic Model Production Rate fractional prime cost ratio for Basic model Units: Dollar/Month

51. Prime Cost Rate of Deluxe Model=Deluxe Model Production Rate∗fractional prime cost ratio for Deluxe model −Units: Dollar/Month

52. “order-level-1 activity cost driver (number of orders) consumption ratio by Basic model”=Basic model order ful<sup>fi</sup>llment rates ∗ “order-level-1 activity cost driver consumption ratio by each order of Basic model” Units: Order/Month

53. “order-level-1 activity cost driver (number of orders) consumption ratio by Deluxe model”=Deluxe model order ful<sup>fi</sup>llment rates ∗ “order-level-1 activity cost driver consumption ratio by each order of Deluxe model”−Units: Order/Month

54. “order-level-1 activity cost driver consumption ratio by each order of Basic model”=1−Units: Dmnl

55. “order-level-1 activity cost driver consumption ratio by each order of Deluxe model”=1−Units: Dmnl

56. “Order-level-1 Cost Rate for Basic Model”=“order-level-1 pool rate” ∗ “order-level-1 activity cost driver (number of orders) consumption ratio by Basic model”−Units: Dollar/Month

57. “Order-level-1 Cost Rate for Deluxe Model”=“order-level-1 activity cost driver (number of orders) consumption ratio by Deluxe model”∗“order-level-1 pool rate”−Units: Dollar/Month

58. “order-level-1 pool rate”=IF THEN ELSE(“total cost of orderlevel-1 cost pool” N0,“total cost of order-level-1 cost pool”/“Total Consumption Order-level-1 Cost Pool Activity Driver (Number of Orders)”, 173.33)− Units: Dollar/Order

59. “order-level-2 activity cost driver (maintenances hours) consumption ratio by Basic model”=Basic model order ful<sup>fi</sup>llment rates ∗ “order-level-2 activity cost driver consumption ratio by each order of Basic model”−Units: MaintenanceHr/Month

60. “order-level-2 activity cost driver (maintenances hours) consumption ratio by Deluxe model”=“order-level-2 activity cost driver consumption ratio by each order of Deluxe model”∗Deluxe model order ful<sup>fi</sup>llment rates Units: MaintenanceHr/Month

61. “order-level-2 activity cost driver consumption ratio by each order of Basic model”=4−Units: MaintenanceHr/Order

62. “order-level-2 activity cost driver consumption ratio by each order of Deluxe model”=6−Units: MaintenanceHr/Order

63. “Order-level-2 Cost Rate for Basic Model”=“order-level-2 activity cost driver (maintenances hours) consumption ratio by Basic model”∗“order-level-2 pool rate”−Units: Dollar/Month

64. “Order-level-2 Cost Rate for Deluxe Model”=“order-level-2 activity cost driver (maintenances hours) consumption ratio by Deluxe model”∗“order-level-2 pool rate”−Units: Dollar/Month

65. “order-level-2 pool rate”=IF THEN ELSE(“total cost of orderlevel-2 cost pool” N 0, “total cost of order-level-2 cost pool”/“Total Consumption Order-level-2 Cost Pool Activity Driver (Maintenances Hours)”, 58.5)−Units: Dollar/MaintenanceHr

66. SAVEPER=TIME STEP−Units: Month (The frequency with which output is stored.)

67. TIME STEP=1 Units: Month (The time step for the simulation.)

68. “Total Batch-Level-1 (Material Handling) Cost for Basic Model”=INTEG (“Batch-Level-1 Cost (Material Handling) Rate for Basic Model”,0) −Units: Dollar

69. “Total Batch-Level-1 (Material Handling) Cost for Deluxe Model”=INTEG (“Batch-Level-l Cost (Material Handling) Rate for Deluxe Model”,0)−Units: Dollar

70. “total batch-level-1 (material handling) cost”=“Total Batch-Level-1 (Material Handling) Cost for Basic Model”+“Total Batch-Level-1 (Material Handling) Cost for Deluxe Model” -Units: Dollar

71. “Total Batch-Level-2 (Equipments Setup) Cost for Basic Model”=INTEG (“Batch-Level-2 Cost (Equipments Setup) Rate for Basic Model”,0) Units: Dollar

72. “Total Batch-Level-2 (Equipments Setup) Cost for Deluxe Model”=INTEG (“Batch-Level-2 Cost (Equipments Setup) Rate for Deluxe Model”,0) Units: Dollar

73. “total batch-level-2 (equipments setup) cost”=“Total Batch-Level-2 (Equipments Setup) Cost for Basic Model”+“Total Batch-Level-2 (Equipments Setup) Cost for Deluxe Model”−Units: Dollar

74. “Total Consumption Batch-Level-1 Cost Pool Activity Driver (Number of Moves)”=INTEG (“Total Consumption Ratio of Batch-Level-1 Activity Cost Driver (Number of Moves)”, 1)−Units: Move

75. “Total Consumption Batch-Level-2 Cost Pool Activity Driver (Number of Setups)”= INTEG (“Total Consumption Ratio of Batch-Level-2 Activity Cost Driver (Number of Setups)”, 1)−Units: Setup

76. “Total Consumption Facility-Level Cost Pool Activity Driver (Machining Hours)”=INTEG (“Total Consumption Ratio of Facility-Level Activity Cost Driver (Machining Hours)”, 1) −Units: MachiningHr

77. “Total Consumption Order-level-1 Cost Pool Activity Driver (Number of Orders)”=INTEG (“Total Consumption Ratio of Order-level-1 Activity Cost Driver (Number of Orderss)”, 1) Units: Order

78. “Total Consumption Order-level-2 Cost Pool Activity Driver (Maintenances Hours)”=INTEG (“Total Consumption Ratio of Order-level-2 Activity Cost Driver (Maintenances Hours)”, 1) −Units: MaintenanceHr

79. “Total Consumption Ratio of Batch-Level-1 Activity Cost Driver (Number of Moves)” =“batch-level-1 activity cost driver (number of moves) consumption ratio by Basic model”+“batchlevel-1 activity cost driver (number of moves) consumption ratio by Deluxe model”−Units: Move/Month

80. “Total Consumption Ratio of Batch-Level-2 Activity Cost Driver (Number of Setups)”=“batch-level-2 activity cost driver (number of setups) consumption ratio by Basic model”+“batchlevel-2 activity cost driver (number of setups) consumption ratio by Deluxe model”−Units: Setup/Month

81. “Total Consumption Ratio of Facility-Level Activity Cost Driver (Machining Hours)” =“facility-level activity cost driver (machining hours) consumption ratio by Basic model” +“facilitylevel activity cost driver (machining hours) consumption ratio by Deluxe model”−Units: MachiningHr/Month

82. “Total Consumption Ratio of Order-level-1 Activity Cost Driver (Number of Orderss)” = “order-level-1 activity cost driver (number of orders) consumption ratio by Basic model”+“order-level-1 activity cost driver (number of orders) consumption ratio by Deluxe model”−Units: Order/Month

83. “Total Consumption Ratio of Order-level-2 Activity Cost Driver (Maintenances Hours)” = “order-level-2 activity cost driver (maintenances hours) consumption ratio by Basic model”+“order-level-2 activity cost driver (maintenances hours) consumption ratio by Deluxe model” Units: MaintenanceHr/Month

84. “total cost of facility-level (providing space) cost pool”=“Total Facility-Level (Providing Space) Cost for Basic Model”+“Total Facility-Level (Providing Space) Cost for Deluxe Model” Units: Dollar

85. “total cost of order-level-1 cost pool” =“Total Order-level-1 Cost for Basic Model”+“Total Order-level-1 Cost for Deluxe Model” − Units: Dollar

86. “total cost of order-level-2 cost pool” =“Total Order-level-2 Cost for Basic Model”+“Total Order-level-2 Cost for Deluxe Model” − Units: Dollar

87. “Total Facility-Level (Providing Space) Cost for Basic Model”=INTEG (“Facility-Level (Providing Space) Cost Rate for Basic Model”,0) −Units: Dollar

88. “Total Facility-Level (Providing Space) Cost for Deluxe Model”=INTEG (“Facility-Level (Providing Space) Cost Rate for Deluxe Model”,0) Units: Dollar

89. Total Holding Cost of Basic Model=INTEG (Holding Cost Rate of Basic Model,0)−Units: Dollar

90. Total Holding Cost of Deluxe Model=INTEG (Holdeing Cost Rate of Deluxe Model,0)−Units: Dollar

91. total overhead cost for Basic model =“Total Batch-Level-1 (Material Handling) Cost for Basic Model” + “Total Batch-Level-2 (Equipments Setup) Cost for Basic Model”+“Total Facility-Level (Providing Space) Cost for Basic Model”+“Total Order-level-1 Cost for Basic Model”+“Total Order-level-2 Cost for Basic Model” Units: Dollar

92. total overhead cost for Deluxe model=“Total Batch-Level-1 (Material Handling) Cost for Deluxe Model”+“Total Batch-Level-2 (Equipments Setup) Cost for Deluxe Model”+“Total Facility-Level (Providing Space) Cost for Deluxe Model”+“Total Order-level-1 Cost for Deluxe Model”+“Total Order-level-2 Cost for Deluxe Model”−Units: Dollar

93. Total Prime Cost of Basic Model=INTEG (Prime Cost Rate of Basic Model,0)−Units: Dollar

94. Total Prime Cost of Deluxe Model=INTEG (Prime Cost Rate of Deluxe Model,0)−Units: Dollar

95. “Total Order-level-1 Cost for Basic Model”=INTEG (“Orderlevel-1 Cost Rate for Basic Model”,0)−Units: Dollar

96. “Total Order-level-1 Cost for Deluxe Model”=INTEG (“Orderlevel-1 Cost Rate for Deluxe Model”,0)−Units: Dollar

97. “Total Order-level-2 Cost for Basic Model”=INTEG (“Orderlevel-2 Cost Rate for Basic Model”,0)−Units: Dollar

98. “Total Order-level-2 Cost for Deluxe Model”=INTEG (“Orderlevel-2 Cost Rate for Deluxe Model”,0)−Units: Dollar

99. Total Production of Basic Model=INTEG (Basic Model Production Rate,0) − Units: Unit

100. Total Production of Deluxe Model=INTEG (Deluxe Model Production Rate, 0) - Units: Unit

101. Total Sales of Basic Model=INTEG (Basic Model Shipping Rate,1)− Units: Unit

102. Total Sales of Deluxe Model= INTEG (Deluxe Model Shipping Rate,1) Units: Unit

## References

[1] T.K. Abdel-Hamid, S.E. Madnick, On the portability of quantitative software estimation models, Inf and Management 13 (1987) 1–10.

[2] B.J. Angerhofer, M.C. Angelides, System Dynamics Modeling in Supply Chain Management: Research Review, Proceedings of the 2000 Winter Simulation Conference, 2000, pp. 342–351.

[3] T.S. Baines, D.K. Harrison, An opportunity for system dynamics in manufacturing system modeling, Production Planning and Control 10 (1999) 542–552.

[4] D. Cagwin, K.J. Barker, Activity-based costing, total quality management and business process reengineering: their separate and concurrent association with improvement in <sup>fi</sup>nancial performance, Academy of Accounting and Financial Studies Journal 10 (2006) 49–77.

[5] D. Cagwin, M.J. Bouwman, The association between activity-based costing and improvement in <sup>fi</sup>nancial performance, Management Accounting Research 13 (2002) 1–39.

[6] R. Cooper, R.S. Kaplan, The Design of Cost Management Systems: Text, Cases and Readings, First ed. Prentice-Hall, Englewood Cliffs, 1991.

[7] M. Gosselin, The effect of strategy and organizational structure on the adoption and implementation of activity-based costing, Accounting, Organizations and Society 22 (1997) 105–122.

[8] M. Gosselin, A review of activity-based costing: technique, implementation, and consequences, Handbook of Management Accounting Research 2 (2007) 641-671.

[9] A. Gregoriades, B. Karakostas, Unifying business objects and system dynamics as a paradigm for developing decision support systems, Decision Support Systems 37 (2004) 307–311.

[10] D.R. Hansen, M.M. Mowen, N.S. Elias, D.W. Senkow, Management Accounting Canadian, Fifth ed. Nelson, Canada, 2001.

[11] J.S. Holmen, ABC vs. TOC: it's a matter of time, Management Accounting 76 (1995) 37–40.

[12] C.D. Ittner, W.N. Lanen, D.F. Larcker, The association between activity-based costing and manufacturing performance, Journal of Accounting Research 40 (2002) 711–726.

[13] R.S. Kaplan, S.R. Anderson, Time-driven activity-based costing, Harvard Business Review 82 (2004) 131–138.

[14] R. Kee, Integrating activity-based costing with theory of constraints to enhance production-related decision-making, Accounting Horizons 9 (1995) 48–61.

[15] T. Kennedy, J. Af<sup>fl</sup>eck-Graves, The impact of activity-based costing techniques on <sup>fi</sup>rm performance, Journal of Management Accounting Research 13 (2001) 19–45

[16] A. Khataie, F.M. Defersha, A.A. Bulgak, A multi-objective optimization approach for order management: incorporating Activity-Based Costing in supply chains, International Journal of Production Research 48 (2010) 5007–5020.

[17] E.T. Kirche, S.N. Kadipasaoglu, B.M. Khumawala, Maximizing supply chain pro<sup>fi</sup>ts with effective order management: integration of activity-based costing and theory of constraints with mixed-integer modeling, International Journal of Production Research 43 (2005) 1297–1311.

[18] E. Kirche, R. Srivastava, An ABC-based cost model with inventory and order level costs: a comparison with TOC, International Journal of Production Research 43 (2005) 1685–1710.

[19] D. Li, C. O'Brien, Integrated decision modeling of supply chain ef<sup>fi</sup>ciency, International Journal of Production Economics 59 (1999) 147–157.

[20] D. Li, C. O'Brien, A quantitative analysis of relationships between product types and supply chain strategies, International Journal of Production Economics 73 (2001) 29–39.

[21] J. Macedo, R. Ruiz Usano, J. Framinan Torres, A real time cost monitoring system for business process reengineering, Proceedings from IFAC Workshop (1997) 411–416.

[22] S.A. Malik, W.G. Sullivan, Impact of ABC information on product mix and costing decisions, IEEE Transactions on Engineering Management 42 (1995) 171-176

[23] A.C. Marquez, C. Blanchar, A Decision Support System for evaluating operations investments in high-technology business, Decision Support Systems 41 (2006) 472–487.

[24] C. Martinez-Olvera, Bene<sup>fi</sup>ts of using hybrid business models within a supply chain, International Journal of Production Economics 120 (2009) 501–511.

[25] B. Novićević, L. Antić, Total quality management and activity-based costing, Economics and Organization 1 (1999) 1–8.

[26] W. Sen, S. Pokharel, W.Y. Lei, Supply chain positioning strategy integration, evaluation, simulation, and optimization, Computers and Industrial Engineering 46 (2004) 781–792.

[27] C. Sheu, M.H. Chen, S. Kovar, Integrating ABC and TOC for better manufacturing decision making, Integrated Manufacturing System 14 (2003) 433–441.

[28] J.D. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World, First ed. Irwin, CF: McGraw-Hill, 2000.

Amir H. Khataie obtained his B.Sc. degree in Industrial Engineering in 2005 from Amir Kabir University of Technology (Tehran Polytechnic) consequently; he received M. Eng. degree in Engineering Management from the University of Ottawa in August 2007. Currently he is a part-time faculty and PhD candidate in the department of Mechanical and Industrial Engineering at Concordia University. Amir H. Khataie research preferences are within hybrid hard and soft OR modeling approach, supply chain management, activity-based costing. His current research is application of accounting approaches in developing supply chain cost management Decision Support Systems

Dr. Akif A. Bulgak is a professor at the Department of Mechanical and Industrial Engineering at Concordia University. He obtained his B.Sc. degree from Istanbul Technical Üniversity in Mechanical/Industrial Engineering and his M.Sc. and Ph.D. degrees from the University of Wisconsin-Madison, USA, all in Industrial Engineering Dr. Bulgak's research areas include Modeling, Performance Evaluation, Design Optimization, and Economics of Flexible Manufacturing/Assembly Systems, Stochastic Optimization, and Revenue Management, and Supply Chain Management. Dr. Bulgak is a registered professional engineer at Professional Engineers Ontario

Dr. Juan J. Segovia is currently an Associate Professor of Accountancy in the John Molson School of Business, Concordia University, Montreal, Canada. He obtained his Doctorate in Business Administration in 1979 from the University of Paris-Dauphine, France. From the same university, he obtained the Diplôme d'Études Approfondies: Business Administration (DEA). Professor Segovia obtained the degree of Bachelor of Commerce — Major: Accounting, from the Universidad de Guanajuato, Mexico. His area of research includes Accounting Education and Management Accounting. His paper have been published in various prestigious journals, e.g., The British Accounting Review, The Accounting Educators' Journal, CMA Magazine, Journal of Business and Behavioural Sciences. In addition, he has presented at several conferences both national and international. His research interests are in the areas of Accounting Education, Activity-Based Costing (ABC), Activity-Based Management (ABM), Performance Measurements, and Business Strategy.
