---
otero_id: 10590
otero_key: "PBBRQETY"
title: "Corporate dashboards for integrated business and engineering decisions in oil refineries: An agent-based approach"
authors: "W. Hu; A. Almansoori; P.K. Kannan; S. Azarm; Z. Wang"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.019"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Corporate dashboards for integrated business and engineering decisions in oil re<sup>fi</sup>neries: An agent-based approach

W. Hu <sup>a</sup>, A. Almansoori <sup>b</sup>, P.K. Kannan <sup>c,</sup>⁎, S. Azarm <sup>a</sup>, Z. Wang

<sup>a</sup> Department of Mechanical Engineering, A. J. Clark School of Engineering, University of Maryland, College Park, MD, 20742, USA

<sup>b</sup> Department of Chemical Engineering, The Petroleum Institute, P.O. Box 2533, Abu Dhabi, UAE

<sup>c</sup> Department of Marketing, Robert H. Smith School of Business, University of Maryland, College Park, MD, 20742, USA

## a r t i c l e i n f o

Article history: Received 29 September 2010 Received in revised form 4 November 2011 Accepted 18 November 2011 Available online 1 December 2011

Keywords: Decision Support System (DSS) Knowledge management Re<sup>fi</sup>nery Oil markets Non-linear optimization Agent-based modeling Simulation

## a b s t r a c t

It is generally very challenging for an oil re<sup>fi</sup>nery to make integrated decisions encompassing multiple functions based on a traditional Decision Support System (DSS), given the complexity and interactions of various decisions. To overcome this limitation, we propose an integrated DSS framework by combining both business and engineering systems with a dashboard. The dashboard serves as a human–computer interface and allows a decision maker to adjust decision variables and exchange information with the DSS. The proposed framework provides a two-stage decision making mechanism based on optimization and agent-based models. Under the proposed DSS, the decision maker decides on the values of a subset of decision variables. These values, or the <sup>fi</sup>rst-stage decision, are forwarded through the dashboard to the DSS. For the given set of <sup>fi</sup>rst-stage decision variables, a multi-objective robust optimization problem, based on an integrated business and engineering simulation model, is solved to obtain the values for a set of second-stage decision variables. The two-stage decision making process iterates until a convergence is achieved. A simple oil re<sup>fi</sup>nery case study with an example dashboard demonstrates the applicability of the integrated DSS.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

An oil re<sup>fi</sup>nery is a complex and continuous processing system with a series of highly nonlinear and strongly coupled subsystems [27]. Such a system presents considerable dif<sup>fi</sup>culties for enterprise management, operational optimization and process control, especially in uncertain environments [15]. Managerial decisions for an oil re-<sup>fi</sup>nery need to take into account capital investments, production, sales, material supply, product transportation, inventory, product developments and improvements, <sup>fi</sup>nancial markets and market risks [3,7,29]. It is crucial that decision and information <sup>fl</sup>ow at different hierarchical levels of the company be considered as a whole to account for uncertainties in demand, raw material procurements, product quality and other market changes while achieving effective integration of business and engineering decisions [19].

Managing the inherent tradeoffs in decisions in business and engineering processes are most essential to an oil re<sup>fi</sup>nery's success and pro<sup>fi</sup>tability. A typical oil re<sup>fi</sup>nery business process consists mainly of crude procurement, sales, inventory, transportation (delivery), and others [20]. While business decisions are made at the upper level of the overall re<sup>fi</sup>nery operations, the lower-level engineering decisions are focused on transforming crude oil into various intermediate and end products in an energy-ef<sup>fi</sup>cient manner [17] while meeting the speci<sup>fi</sup>cations demanded by the upper-level business processes. Several commercial decision support tools in the context of oil re<sup>fi</sup>nery operations are available, e.g., GRTMPS by Haverly Systems [9], RPMS by Honeywell [10] and PIMS by Aspen Technology [2]. However, these commercial tools are predominantly focused either on business process and supply chain management, e.g., GRTMPS, or on engineering and process control, e.g., RPMS and PIMS, while taking little consideration of the interactions and integration of business and engineering processes. Consequently, a signi<sup>fi</sup>cant gap exists between the upper-level business and the lower-level engineering decision processes, while the problems of adaptability of an engineering department in response to market <sup>fl</sup>uctuations have become increasingly prominent [35]. In order to improve operational ef<sup>fi</sup>ciency and enterprise pro<sup>fi</sup>tability, it is necessary to achieve integration between the business and engineering decisions by making full use of the information <sup>fl</sup>ow between them.

In recent years, with an increasingly competitive global market, decisions in oil re<sup>fi</sup>nery business and engineering processes are frequently in<sup>fl</sup>uenced by the market <sup>fl</sup>uctuations and uncertainties. Matching demand and output of a re<sup>fi</sup>nery is a delicate balance, and a signi<sup>fi</sup>cant mismatch can be the difference between pro<sup>fi</sup>t and loss. The management of this delicate balance has often led to comments such as “Oil production creates wealth, but oil re<sup>fi</sup>ning has often destroyed it” [23]. The commercially available decision support tools (e.g., [2,9,10]) are typically developed with deterministic models and could suggest decisions which are sensitive to the uncertainty. Under such circumstances, it is desirable for business and engineering decisions to take into account the uncertain factors and obtain robust (or insensitive) decisions in midst of the <sup>fl</sup>uctuating global markets and uncertain environments. The proposed DSS in this paper is aimed at obtaining optimally robust decisions for products and/or processes, that is, solutions that are optimum and relatively insensitive to uncertainty.

A variety of DSS methodologies and frameworks have been developed with real-world applications [30,31]. Kim et al. [16] evaluated the enterprise information portal systems in the context of knowledge management activities. Their framework can be used to improve knowledge integration and information <sup>fl</sup>ow and facilitate ef<sup>fi</sup>cient operations in large scale enterprises. The related literature also reports on an active intelligent DSS to support complex system decision making [32]. Various information structures for team decision making are also considered for business decisions [33]. While many of these developments are common to oil re<sup>fi</sup>nery systems, oil re<sup>fi</sup>nery problems are characterized by volatile input and market conditions that make it particularly challenging for DSS development.

Focusing on business decisions in an oil and petrochemical system, Chryssoloouris et al. [3] presented a simulation-based approach to tackle short-term re<sup>fi</sup>nery scheduling problem. Their approach is able to handle discrete decision variables in a short decision-making time frame thus handling the uncertainties using a shorter planning horizon. Paolucci et al. [26] considered the problem of allocating the crude oil loads of tanker ships to port and re<sup>fi</sup>nery tanks. Pitty et al. [18,28] used Matlab [21] to model the integrated re<sup>fi</sup>nery supply chain taking into consideration the activities of each component of the chain. They were able to model various business decisions and policies and to monitor the impact on the company's business performance. Clark [4] showed the possibility for a re<sup>fi</sup>nery company to monitor its supply chain in real-time or near real-time using advanced forecasting, planning and scheduling tools. Pinto et al. [27] investigated optimization of a multi-product plant and proposed modeling of multi-product plant assuming that the <sup>fl</sup>uctuations in market demand characteristics provide opportunity to de<sup>fi</sup>ne new operating points that increases the production of more valuable products. Gattu et al. [6] identi<sup>fi</sup>ed integration of yield accounting with SAP [34] for inventory management and order ful<sup>fi</sup>llment and allocation. Their approach is based on an online (real time) optimization of the whole re<sup>fi</sup>nery. Jackson et al. [12] used nonlinear optimization in the planning of multi-plant production site, where nonlinear models are used at the plant level to determine monthly production and inventory levels to meet demand forecast and maximize pro<sup>fi</sup>t. Zhang and Zhu [37] proposed a two-level decomposition approach for optimizing a large-scale re<sup>fi</sup>nery plant. The main advantage of this technique is the <sup>fl</sup>exibility to adapt different optimizers for different subsystems.

While the majority of literature focus on re<sup>fi</sup>nery business decisions as presented above, optimization models for engineering decisions have also been studied [1,5]. For example, Gadalla et al. [5] focused on optimization of an existing distillation process by changing key engineering variables. Micheletto et al. [22] developed a mix-integer mathematical model for operational variables to minimize re<sup>fi</sup>nery utility costs. However, none of the previous work has considered both business and engineering decisions in a larger enterprise such as an oil re<sup>fi</sup>nery.

This paper proposes to integrate business and engineering decisions with a dashboard based on an agent-based approach and a two-stage decision-making process. Under the proposed decision support framework, dashboard serves as a human–computer interface which allows a decision maker to adjust decision variables and exchange information with the DSS. During the decision-making process, the <sup>fi</sup>rst-stage decision variables are determined by the decision maker and forwarded through the dashboard to the DSS. For a given set of <sup>fi</sup>rst-stage decision variables, the DSS simulates the business and engineering performances of the re<sup>fi</sup>nery as a function of the second-stage decision variables. Essentially, the second-stage decision-making process is posed as a multi-objective (both business and engineering objectives are considered) optimization problem which is solved to obtain a set of optimum solutions from which a preferred one is selected by the decision maker. Upon observing the selected solution in the oil re<sup>fi</sup>nery and its performance, the decision maker is able to re<sup>fi</sup>ne and adjust the <sup>fi</sup>rst-stage values of decision variables in order to achieve certain goals. Finally, the <sup>fi</sup>rst-stage decision variables are updated through the dashboard and optimization of the second-stage decision variables is repeated. With the help of dashboard, the decision maker is able to interact with the DSS until a desired re<sup>fi</sup>nery performance is achieved. To demonstrate the proposed integration framework, a simple oil re<sup>fi</sup>nery case study is developed, in which the decision maker is modeled as an intelligent agent. The values of the <sup>fi</sup>rst-stage decision variables are generated from a distribution pro<sup>fi</sup>le function and updated using a no-regret learning algorithm [8] according to the pro<sup>fi</sup>t. The oil re<sup>fi</sup>nery simulation model was developed to simulate the business and engineering performances using an agent-based simulation tool NetLogo [25] and a commercial simulation software HYSYS [2], respectively. In the case study, a multi-objective robust optimization approach is applied to solve the integrated business and engineering optimization problem. As we show in the paper, the integrated DSS framework considerably improves ef<sup>fi</sup>ciency and effectiveness of decision support and information-processing capability for oil re<sup>fi</sup>nery decision making under uncertainty.

In the next section, a background on multi-objective robust opti mization and the agent based approach is provided. In Section 3, a general framework for an integrated DSS is proposed. A case study which presents the speci<sup>fi</sup>cs of the system constructed on the basis of the proposed framework is presented in Section 4. Section 5 concludes the paper by providing the advantages of the integrated framework, limitations, and avenues for future research.

## 2. Problem de<sup>fi</sup>nition and background

## 2.1. Problem definition

This section <sup>fi</sup>rst presents the problem de<sup>fi</sup>nition and then presents the background for the proposed framework.

Consider an enterprise such as an oil re<sup>fi</sup>nery company where the values for a set of business and engineering decisions need to be determined in order to achieve certain goals, e.g., to maximize pro<sup>fi</sup>t and to maximize product quality. The decision variables are divided into two subsets, each of which contains both business and engineering decisions. The <sup>fi</sup>rst set of decisions, as represented by $x _ { 1 }$ (a vector), consists of the values of decision variables which are set by the decision makers. A decision maker can be the manager or an expert in the company who makes critical and strategic decisions and can set such values based on his/her expertise and experience. The second set of decisions, as represented by $x _ { 2 }$ (also a vector), includes decision variables considered for optimization. Categorization of decision variables to either $x _ { 1 }$ or $x _ { 2 }$ is based on the following rules: (1) the decision space (number of decision variables) for $x _ { 1 }$ is limited because it is dif-<sup>fi</sup>cult for a human decision maker to consider too many decisions; decisions on $x _ { 1 }$ typically consist of variables that decision maker has expertise/intuition and experience in setting; and (2) there is almost no limit on the number of decision variables in $x _ { 2 }$ unless restricted by the size of optimization problem and computation costs.

In this study, an oil re<sup>fi</sup>nery is characterized by a series of models which de<sup>fi</sup>nes the functional relationships between the inputs and the outputs. The inputs to the oil re<sup>fi</sup>nery include a set of decision variables which are controlled by the decision maker and some parameters which are <sup>fi</sup>xed at their nominal values. For example, a parameter such as the price of phthalic anhydride (an end product) is <sup>fi</sup>xed at its nominal value of 1200 \$/ton. The outputs include intermediate and end product <sup>fl</sup>ows, utility costs, performance and characteristics of process units and so on. The outputs from the re<sup>fi</sup>nery are used to calculate Key Performance Indicators (KPIs) as well as the objective and constraint functions in the optimization problem. It is assumed that the lower and upper bounds of all decision variables are known a priori. Further, both decision variables and parameters can have interval uncertainty whose lower and upper limits are assumed to be known. Before introducing the proposed DSS framework, we present a brief introduction of two techniques used in the DSS system next.

## 2.2. Background

## 2.2.1. Multi-objective robust optimization under interval uncertainty

Robust optimization aims at obtaining optimum solutions which are relatively insensitive to uncertainty. The formulation of a multiobjective robust optimization problem under interval uncertainty can be given as in Eq. (1):

$$
\begin{array}{l} \underset {x} {\min} f _ {m} (x, p), m = 1, \dots , M \\ s. t.: | f _ {m} (x, p + \Delta p) - f _ {m} (x, p) | \leq a _ {m}, m = 1, \dots , M \\ g _ {j} (x, p + \Delta p) \leq b _ {j}, j = 1, \dots , J \\ \forall \Delta p \in \left[ \Delta p ^ {L}, \Delta p ^ {U} \right] \\ x ^ {L} \leq x \leq x ^ {U} \end{array}\tag{1}
$$

where $f _ { m }$ represents the mth objective function, $\scriptstyle { m = 1 , \ldots , M }$ and $g _ { j }$ is the jth constraint function, $j = 1 , \hdots J .$ The quantities x and p (both are row vectors) denote decision variables and nominal values of parameters, respectively. $\Delta p$ is a vector of uncertain variations in parameters. $a _ { m }$ is a user de<sup>fi</sup>ned acceptable range for the variation in the mth objective function value, and $b _ { j }$ is the goal for the jth constraint function. In Eq. (1), optimization is done with respect to decision variables with their values bounded by the lower $x ^ { L }$ and upper bounds $x ^ { U } .$ The lower and upper limits of uncertainties in parameters are represented by $\Delta p ^ { L }$ and $\Delta p ^ { U }$ , respectively. Optimization of Eq. (1) produces a set of robust solutions whose variations in the objective and constraint functions are within an acceptable range under uncertainty while multi-objectively optimum in the sense that the value of none of the objective functions can be decreased without increasing at least one other objective function.

A previously developed [11] ef<sup>fi</sup>cient Approximation-Assisted Multi-Objective Robust Optimization (AA-MORO) technique is used in the paper. Approximation is used to replace a computationally expensive analysis model for (objective and/or constraint) function calculation with an inexpensive one (or meta-model) during the optimization. AA-MORO obtains optimal values of decision variables from an upper-level sub-problem as shown in Eq. (2) and then evaluates the robustness for these optimal solutions using a lower-level sub-problem in Eq. (3):

Upper level

$$
\begin{array}{l} \min _ {x} f _ {m} (x, p), m = 1,..., M \\ \text { s.t.: } | f _ {m} (x, p + \Delta p _ {n}) - f _ {m} (x, p _ {n}) | \leq a _ {m}, m = 1,..., M, n = 1,..., N \\ g _ {j} (x, p + \Delta p _ {n}) \leq b _ {j}, j = 1,..., J,, n = 1,..., N \\ \Delta p _ {n} \in S _ {p} \\ x ^ {L} \leq x \leq x ^ {U} \end{array}\tag{2}
$$

$$
\begin{array}{l} \text {(Lower level)} \\ f _ {w c v} = \max _ {i} \max _ {\Delta p} (r _ {i} (x, p + \Delta p)), i = 1,..., J + M \\ s. t.: \Delta p ^ {L} \leq \Delta p \leq \Delta p ^ {U} \\ r _ {i} = \left\{ \begin{array}{l} \frac {| f _ {i} (x , p + \Delta p) - f _ {i} (x , p) |}{a _ {i}} - 1, i = 1,..., M \\ \frac {g _ {i} (x , p + \Delta p)}{b _ {i - M}} - 1, i = M + 1,..., M + J \end{array} \right. \end{array}\tag{3}
$$

The upper-level sub-problem in Eq. (2) optimizes the objective functions $f _ { m }$ by changing the decision variables x. In Eq. (2), S contains a set of Δp values, $\mathrm { i . e . , } S _ { p } = \{ \Delta p _ { n } \} , n = 1 , . . . , N .$ The optimum solutions from the upper-level sub-problem are forward to the lower-level subproblem Eq. (3) where the robustness of each optimum solution can be determined by checking the condition: $f _ { w c v } { \le } 0 .$ . To obtain the value of $f _ { w c v } ,$ the lower-level sub-problem applies a worst-case analysis on the variations in the objective and constraint functions. In other words, the lower-level sub-problem evaluates the variations in the objective and/or constraint functions for different realizations of $\Delta p ,$ , as shown in Eq. (3). Therefore, while solving the Eq. (3) which is also posed as an optimization sub-problem, the values of decision variables x must be <sup>fi</sup>xed and only the values of Δp are allowed to be changed. Furthermore, the optimized $\Delta p$ from the lower-level sub-problem are accumulated in $S _ { p }$ and used for solving the upper-level sub-problem.

As mentioned before, an approximation assisted approach is used to solve the upper- and lower-level sub-problems iteratively. To construct the approximation, the actual (presumably computationally expensive) objective and constraint function values at a few selected (or sample) points are calculated. These points are then used to construct meta-models for approximation. As AA-MORO iterates between the upper- and lower-level sub-problems and obtains optimum solutions, these solutions are used to generate additional sample points. AA-MORO then combines the additional sample points with the previous ones and updates the meta-models. Compared to an approximation approach which uses a <sup>fi</sup>xed number of sample points, AA-MORO requires considerably less number of sample points to achieve a required level of accuracy [11].

## 2.2.2. Agent-based approach

An agent is an entity (software, model or individual) that performs a speci<sup>fi</sup>c task without intervention of users or other agents [13,14]. The most essential characteristic of an agent lies in its capability of making independent decisions. An agent can be responsive to and learn from the environment which is usually referred to as the adaptive behavior in an agent-based approach. In the proposed DSS framework, the agent-based approach is used to model the business process and the interaction between decision maker and dashboard, as elaborated next.

In simulating the re<sup>fi</sup>nery business model, the re<sup>fi</sup>nery, its inventory and the customers are each modeled as an agent. During a simulation cycle, each customer agent determines the quantity of product it is willing to purchase. This could be based on a realization from the distribution of the demand and sometimes updated based on a customer modifying its preferences based on other customers' preferences (learning from others). When a customer agent places its order, the re<sup>fi</sup>nery and inventory agents will respond and decide how to ful<sup>fi</sup>ll the order based on a prede<sup>fi</sup>ned protocol. For instance, an end product is always delivered to a customer agent directly from the re<sup>fi</sup>nery whenever the production meets the demand; also the remaining products by the end of each simulation cycle are stored in the inventory. An inventory agent incurs a holding cost based on the amount of stock in inventory. There is also a “stock-out” penalty cost when stock in the inventory runs out or is not enough to ful<sup>fi</sup>ll an order. Since the rate of penalty cost is typically higher than the holding cost, the inventory agent should strike a balance between keeping too much stock, which runs up inventory holding-costs, and too little stock, which brings a greater risk of running out of stock and incurring excessive penalty cost.

In general, the decision maker uses the dashboard to determine the values of some decision variables (x ) and then selects the values of the rest of the decision variables $\left( x _ { 1 } \right)$ and vice versa. On the other hand, by taking the values of the decision variables $x _ { 1 }$ from the decision maker, the dashboard uses the optimization model to obtain a new set of decision alternatives $x _ { 2 }$ for the decision maker. This action–reaction process between the decision maker and the dashboard would eventually align with an improvement in the corporate pro<sup>fi</sup>t such as pro<sup>fi</sup>t. In the case study, the decision maker and a multi-objective optimization assisted dashboard are each modeled as an agent. The decision making agent is responsible for deciding on $x _ { 1 } ,$ , while the dashboard agent generates a set of values for $x _ { 2 } .$ These two agents interact by observing decisions made by each other and gradually learn to improve the decisions. In particular, a “no-regret learning” algorithm is used to model a “simulated decision maker” in the case study. The detail of the interaction between the decision maker and dashboard is discussed in Section 3.4 and the “no-regret learning” algorithm in Section 4.4.

## 3. An integrated decision support system

The main components in the business and engineering domains are presented <sup>fi</sup>rst. An integration framework is presented next which considers both business and engineering domains. Finally, a dashboard is developed as a decision support tool for the proposed DSS framework.

## 3.1. The business domain

An oil re<sup>fi</sup>nery's business domain is characterized by a network of retailers, distributors, transporters, storage facilities, and suppliers that participate in the sale, delivery, and production of a series of fuel and petrochemical products. The business domain in a typical oil re<sup>fi</sup>nery has the following components:

1. Procurement: request and track crude oil supply, and maintain crude supply records.

2. Demand planning: create an overall demand forecast for the oil re<sup>fi</sup>nery.

3. Capacity planning: evaluate the long-term and short-term capacity of the re<sup>fi</sup>nery to meet customers' demand.

4. Material requirements planning: determine crude quality requirements to support the production plan.

5. Inventory management: develop inventory policies and decisions based on the primary inventory cost.

6. Distribution planning: select the most cost-effective route and inventory movements based on customers' demand, transportation and inventory costs.

The oil re<sup>fi</sup>nery business domain serves to collect and process data concerning customers, orders, market <sup>fl</sup>uctuations, distributors and services. An important function of oil re<sup>fi</sup>nery business is to determine market demands with respect to actual customer orders and estimate market trends by applying forecasting techniques. Based on the market information, the business decision variables such as how much crude oil to be purchased, what type of end products to produce and the quality requirements of these end products, are made to maximize pro<sup>fi</sup>t for a given time period. The formulation of pro<sup>fi</sup>t is given in Eq. (7):

$$
\text { profit } = \sum_ {i \in S I} F _ {i} c _ {i} - \sum_ {k \in S K} F _ {k} c _ {k} - \sum_ {r \in S R} C _ {r}\tag{7}
$$

where $c _ { i }$ is the unit price of products and $c _ { k }$ is the unit cost of feed material. $F _ { i }$ and $F _ { k }$ are the quantities of product sales and feed <sup>fl</sup>ow rate respectively. $C _ { r }$ represents other costs such as the capital cost, operating and utility costs, labor cost, inventory cost and so on. SI denotes different types of products and SK represents various components of feeding stream. SR includes resources that the petrochemical process requires, e.g., human resources, cooling water, electricity and so on. Notice that the feed <sup>fl</sup>ow rate $F _ { k }$ is a business decision variable in Eq. (7). However, there are other business decision variables in an oil re<sup>fi</sup>nery that are not explicitly expressed in Eq. (7). For example, the quantity of an intermediate product used for production of an end-product is a short-term business decision variable not given in Eq. (7). Such a decision variable could affect the output capacity. On the other hand, end-product quantity and quality also depend on engineering decision variables such as the operational settings in the process units. Therefore, the quantity on product sales $F _ { i }$ is a result of both business and engineering decision variables. On the other hand, if we consider the difference between the internal and external markets, product sales can be divided into internal market sales and external market sales as in Eq.(8):

$$
\sum_ {i \in S I} F _ {i} c _ {i} = \sum_ {i \in S I I} F _ {I, i} c _ {I, i} + \sum_ {i \in S I E} F _ {E, i} c _ {E, i}\tag{8}
$$

where $F _ { I , i }$ and $F _ { E , i }$ represent quantity of products sold to the internal and external markets respectively. $c _ { I , i }$ and $c _ { E , i }$ represent the unit price of products in the internal and external markets respectively. In both Eqs. (7) and (8), the unit price/cost of product and feed such as $c _ { i }$ (including $c _ { I , i }$ and $c _ { E , i } ) , c _ { k }$ and $C _ { r }$ are business parameters whose values can be assumed known. However, these parameters might have uncertainties. The uncertainties in business parameters are considered in the proposed DSS framework using the AA-MORO approach presented in Section 2.1, while the detail will be discussed later in this paper. In the next section, the components of the oil re<sup>fi</sup>nery engineering domain are presented.

## 3.2. The engineering domain

The oil re<sup>fi</sup>nery's engineering domain starts from the supply of crude oil. Crude oil is separated in the Crude Distilling Unit (CDU) into kerosene, naphtha, gas oil, petroleum gases, and others. These intermediate products are further processed and blended into fuel (e.g., gasoline, kerosene) and other petrochemical products. The objectives of an engineering department are to maximize the purity of the products that they produce while keeping the utility (energy, electricity, cooling water and so on) cost at a minimum level. Engineering is also responsible for collecting, accessing, and analyzing production data, and forwarding the critical information to the management. In order to meet business goals and comply with an oil company's overall plan, decision maker in an engineering department need to consider a few critical factors as in the following:

1. Operation setting: adjust operation parameters in the process equipment, for example feed <sup>fl</sup>ow rate, re<sup>fl</sup>ux ratio, boil-up ratio, and utility in CDU.

2. Production scheduling: develop a feasible production schedule for a product, given demand, production plan, capacity, and material availability.

3. Speci<sup>fi</sup>cations: determine the quality speci<sup>fi</sup>cation of end products according to the law, standards, and regulations, taking into account customer requirements.

4. Quality management: monitor variations in the intermediate and end product quality through the enforcement of quality control criteria

5. Maintenance: optimize equipment operations to reduce utility cost, malfunctioning and equipment maintenance fee.

Typically, engineering decisions are focused on the operational variables in the process equipments and thus calculating product purity for a set of engineering decision variables involves solving a series of complicated nonlinear equations. In practical applications, this can be accomplished with the help of chemical process simulation software such as Aspen HYSYS [2].

In a re<sup>fi</sup>nery, all facilities need to operate in an equilibrium state de<sup>fi</sup>ned by the nominal values of the engineering process variables. However, uncertainty in the operating environment and variance in crude oil composition and properties tends to cause <sup>fl</sup>uctuations in the engineering process, which could affect the quality and speci<sup>fi</sup>cation of the products. In the proposed DSS framework, AA-MORO is used to consider such uncertainty in engineering parameters. On the other hand, the engineering departments are at the lower echelons of decision making in an oil re<sup>fi</sup>nery and are rarely involved in the upper-level business/management decision-making process. If the engineering department can only make adjustment on the process variables based on the decisions made solely by the business process, the overall performance of the oil re<sup>fi</sup>nery can suffer as a result of the disconnect between business and engineering. This limitation is expected to be overcome by integration of business and engineering decisions, as presented in the next section.

## 3.3. Integration of business and engineering decisions

The roadmap for integration of business and engineering decisions is shown in Fig. 1. It contains two primary <sup>fl</sup>ows: decisions <sup>fl</sup>ow mainly from the top decision maker to the business and engineering simulation models, and information <sup>fl</sup>ows in the opposite direction. Both decision and information <sup>fl</sup>ows pass through the dashboard which assists decision maker in implementing decisions and visualizing information for decision making. At the top of the roadmap, decision maker has certain goals to achieve during the decision-making process. These goals can include but not limited to maximizing pro<sup>fi</sup>t, complying with market laws, regulations and etc. At the bottom of the roadmap, a robust optimization problem is formulated based on an integrated business and engineering simulation model.

The business and engineering models each is capable of predicting respective business and engineering performances for a given set of decision variables and parameters. In this integrated model, the business decision and its impact on the business model may affect engineering model through a coupling variable, and vice versa. The coupling variable is represented by the business/engineering outputs between the two models. To achieve the optimal decision, it is desirable to connect business and engineering models, taking into account the coupling variables between them. In an oil re<sup>fi</sup>nery, many coupling variables exist between business and the engineering domains. For example, the feed <sup>fl</sup>ow rate which is determined by a business department will be used as an input by the engineering department. The engineering department, on the other hand, returns the operating (utility) cost and product <sup>fl</sup>ow rate to the business department for calculating pro<sup>fi</sup>t. The values of these coupling variables must be agreed upon by both business and engineering departments. Identifying the coupling variables to reach a mutual agreement without the support of a DSS system is a delicate task which typically involves many trials and errors. In the proposed DSS framework, however, a consistency constraint is enforced for each coupling variable such that if there are any discrepancies on a coupling variable, the differences will lead to a violation of the corresponding consistency constraint. Consequently, the optimizer tries to minimize the inconsistency as much as possible to retain model feasibility. When the optimal decision are obtained, the approach will guarantee the business and engineering analysis models to agree upon each other while achieving the optimal objectives.

![](/api/attachments/PBBRQETY/fulltext/images/2999a1935ded9a3386e8e01a637a7c9e3cdd4e6ffb5afc4b39a34e28c4724ac1.jpg)  
Fig. 1. Roadmap for integration of business and engineering decisions.

Based on the integrated business and engineering model and considering both business and engineering objective and constraint functions, the optimization of business and engineering decision variables is formulated as a multi-objective problem as follows:

$$
\begin{array}{l} \min _ {x _ {2}} f _ {B} (x _ {2}, p _ {B} + \Delta p _ {B}) \\ \min _ {x _ {2}} f _ {E} (x _ {2}, p _ {E} + \Delta p _ {E}) \\ s. t.: g _ {B, j} (x _ {2}, p _ {B} + \Delta p _ {B}) \leq 0, j = 1,..., J _ {B} \\ g _ {E, j} (x _ {2}, p _ {E} + \Delta p _ {E}) \leq 0, j = 1,..., J _ {E} \\ x _ {2} ^ {L} \leq x _ {2} \leq x _ {2} ^ {U} \\ \forall \Delta p _ {B} \in \left[ \Delta p _ {B} ^ {L}, \Delta p _ {B} ^ {U} \right]; \forall \Delta p _ {E} \in \left[ \Delta p _ {E} ^ {L}, \Delta p _ {E} ^ {U} \right] \end{array}\tag{9}
$$

where $f _ { B }$ and $g _ { B , j }$ represent business objective and business constraints, respectively, such as inventory capacity, limitation on the type and volume of products that can be produced, and so on. $f _ { E }$ and $g _ { E , j }$ represent engineering objective and engineering constraints, respectively, considering equipment processing capacity, maximum allowable vessel pressure and temperature for safety and other restrictions. $x _ { 2 }$ is a vector consisting of business and engineering decision variables in optimization, as de<sup>fi</sup>ned earlier in Section 2.1. $p _ { B }$ and $p _ { E }$ represent uncertain business and engineering parameters while $\Delta p _ { B }$ and $\Delta p _ { E }$ represent the variation in those parameters.

Note that in $\operatorname { E q . }$ (9), evaluation of each objective and constraint function such as $f _ { B } ,$ f , g , $g _ { E } ,$ requires a simulation run of either the business or engineering model. Therefore, it could result in a large number of function calls and present computational dif<sup>fi</sup>culties. However, in the proposed DSS framework, the AA-MORO approach introduced in Section 2.1 is employed to ef<sup>fi</sup>ciently solve Eq. (9). On the other hand, in practice, the optimization problem in Eq. (9) may include many decision variables from both business and engineering domain, which poses another challenge to the decision maker of an oil re<sup>fi</sup>nery to observe and make decisions. To improve the ef<sup>fi</sup>ciency of decision-making process and quality of the decisions, an interactive user interface, or dashboard is constructed in the proposed DSS framework. The main function and role of dashboard is presented in the next section.

## 3.4. Dashboard: management decision support system

Dashboard is a human–computer interface. In the proposed framework, dashboard connects the decision maker and the integrated business and engineering simulation and optimization model to facilitate presentation of information to top-level decision maker of the re<sup>fi</sup>nery.

The layout of a conceptual dashboard for oil re<sup>fi</sup>nery performance management is shown in Fig. 2. One important capability of dashboard is to visualize KPIs. For example, pro<sup>fi</sup>t from sales of an end product is an indicator of how ef<sup>fi</sup>cient the company is in turning investment into net income and which products are driving pro<sup>fi</sup>ts. Similarly, stock-out cost and production informs the decision maker how well the oil re<sup>fi</sup>nery's production capacity can meet market demands. With the current and historical KPIs presented on dashboard, the decision maker is able to observe oil re<sup>fi</sup>nery's performance <sup>fi</sup>rst hand. In addition, the dashboard allows decision makers across various departments in an oil re<sup>fi</sup>nery to coordinate and implement decisions. When there is a signi<sup>fi</sup>cant deviation of KPIs from their normal value, the decision maker can take actions by changing the decision variables through the sliders on dashboard. Because an oil re<sup>fi</sup>nery may involve many decision variables, it is typically dif<sup>fi</sup>cult for a decision maker to control all decision variables manually on the dashboard. Therefore, the proposed DSS framework also integrates multi-objective optimization to obtain optimum decision variables as shown in Fig. 2.

![](/api/attachments/PBBRQETY/fulltext/images/b7e6c3cf353995fb80f388670cc089ad4bd2f39cd0c7975269c0bd6ca9f36495.jpg)  
Fig. 2. Layout of a conceptual dashboard for oil re<sup>fi</sup>nery performance management.

Fig. 3 shows decision support role of a dashboard where $x _ { 1 }$ and $x _ { 2 }$ represent decision variables controlled by the decision maker and optimizer, respectively. Particularly, the values of $x _ { 1 }$ are determined according to decision maker's expertise and previous experience while the value of $x _ { 2 }$ is selected based on the optimum solutions obtained from AA-MORO. When making decisions, decision maker needs to evaluate the information shown on the dashboard. The decision maker has certain goals to achieve such as maintain all the KPIs in the oil re<sup>fi</sup>nery at their normal level and ensure that the re<sup>fi</sup>nery is pro<sup>fi</sup>table. It should be noted, however, that any decision from the decision maker must comply with market regulations and other constraints. On the other hand, the objective functions in AA-MORO need to be consistent with the goal of decision maker. For example, maximizing pro<sup>fi</sup>t from sales and maximizing the purity of an endproduct are the two primary goals in the case study presented in Sec tion 4.

With the help of dashboard, the decision-making process starts with an initial set of decision variables $\left( x _ { 1 } \right)$ by the decision maker. These decision variables $\left( x _ { 1 } \right)$ are then re<sup>fl</sup>ected (update previous decision variables) on the dashboard and then passed on to the integrated business and engineering simulation in the ‘Optimization’ block. Next, AA-MORO searches for the robust optimum solutions using the simulation model for the given set of decision variables (x ) made by the decision variable maker. The optimum decision variables, represented by $x _ { 2 } ^ { * } ( x _ { 1 } )$ , are forwarded to the oil re<sup>fi</sup>nery where $\prod ( x _ { 1 } , x _ { 2 } ^ { * } ( x _ { 1 } ) )$ ) represents <sup>fi</sup>rm-market assessment (for example, profit) function. Based on the optimum decision variables x<sup>⁎</sup>(x ) and current values of decision variables $x _ { 1 } ,$ , the KPIs of the oil re<sup>fi</sup>nery are observed and sent to the dashboard. By observing the KPIs on dashboard, decision maker needs to update the decision strategy function $s ( x _ { 1 } )$ . According to the updated strategy function, decision maker makes a new decision on $x _ { 1 }$ and updates the decision variables on the dashboard. The integrated simulation-based AA-MORO is then repeated. After the new set of optimum decision variables are obtained and implemented in the re<sup>fi</sup>nery, it may impact the current KPIs according to the <sup>fi</sup>rm-market assessment. As a result, these KPIs may be changed and are shown on the dashboard again, through which the decision maker continue to update decision variables until plant performance reaches an equilibrium state with desired values of KPIs.

![](/api/attachments/PBBRQETY/fulltext/images/954edbfb335ea1ef82f9b0f24da2a26d78172512ab53f5402f6e72f7a425a4f5.jpg)  
Fig. 3. The decision support role of dashboard.

In the next section, we use a case study to demonstrate how the above mentioned approach works for an example dashboard.

## 4. An oil re<sup>fi</sup>nery case study

In this case study, the focus is on (1) identifying the KPIs that help better represent the interactions among the market forces, the management policies and business and engineering decisions, (2) designing the measurement schemes across various business and engineering departments that will encompass the areas of marketing metrics, <sup>fi</sup>nancial measures, and key engineering performance measures, and (3) designing simulation studies to test these measures under different product market (ranging from products being substitutes to products being complements among the <sup>fi</sup>rms) scenarios, and the sensitivity of these measures to policy changes and actions. Based on the KPIs, the measurement schemes and simulations, a dashboard that integrates data of the market, the company, and those KPI's is devised.

The schematic of the supply, production, and marketing activities involved in the case study is shown in Fig. 4. In the <sup>fi</sup>gure, “Murban” refers to a particular type of crude oil. The internal market consists of local customers, while the external market is composed of other customers not considered in the internal market, e.g., foreign customers. The schematic starts with the crude oil (Murban) extraction in the oil <sup>fi</sup>eld where the oil re<sup>fi</sup>nery purchases Murban from the oil extraction company. The majority of the purchased Murban is transported to the oil re<sup>fi</sup>nery plant for producing fuel and petrochemical products, which are sold in both internal and external market. In addition to supply internal and external market for petroleum product demand, the oil re<sup>fi</sup>nery in the case study can also sell some portion of crude oil directly in the external crude oil market, as shown in Fig. 4.

Inside the oil re<sup>fi</sup>nery plant in Fig. 4, Murban is <sup>fi</sup>rst processed in the Crude Distillation Unit (CDU), where the output of CDU includes among others some naphtha. Naphtha is then used to produce o-xylene and processed in a reactor-distillation unit. One output product from the reactor-distillation unit is phthalic anhydride, an industrial chemical for production of plasticizers for plastics. In our case study, it is assumed that phthalic anhydride is the end product sold in the market.

In the case study, we make various other assumptions. One assumption is that phthalic anhydrides can be sold directly to the internal and external customers if the production from the re<sup>fi</sup>nery is equal or greater than the quantity of demands. Note in reality, the products from re<sup>fi</sup>nery are <sup>fi</sup>rst stored in a short-term inventory whenever they are produced. The products that are stored in the short-term inventory are then delivered to customers, depending on their demands. In the case study, however, the short-term inventory is not considered and the transportation and short-term inventory costs are ignored. After satisfying customer demands, the remaining (excessive) products are forwarded and stored in the designated long-term inventory to meet future customer demands. Long-term inventory costs are considered in the case study. In case the production from the re<sup>fi</sup>nery is less than demand, the product previously stored in the long-term inventory is used to ful<sup>fi</sup>ll the demand. However, if a combination of the re<sup>fi</sup>nery production and inventory still fails to meet the demand, a stock-out penalty cost has to be assessed.

The decision variables in the case study are summarized in Table 1. Among these decision variables, the amount of daily crude oil purchase (variable $x _ { 1 } )$ is determined by the decision maker and a few selected engineering and business decision variables $( x _ { 2 , i } , i = 1 , . . . , 5 )$ are determined by AA-MORO (optimization). In general, both $x _ { 1 }$ and $x _ { 2 }$ are de<sup>fi</sup>ned as vectors and include engineering as well as business decision variables. In the case study $x _ { 1 }$ is a scalar and contains only one business decision variable for simplicity but $x _ { 2 }$ includes two business decision variables $\left( x _ { 2 , 1 } \right.$ and $x _ { 2 , 2 } )$ and three engineering decision variables $\left( x _ { 2 , 3 } , x _ { 2 , 4 } , x _ { 2 , 5 } \right)$ as shown in Table 1.

In the case study, it is also assumed that both engineering and business parameters can have interval uncertainties. For example, the temperature of feed stream to phthalic distillation column is an uncertain engineering parameter and the selling price of phthalic anhydride in external market is an uncertain business parameter. The nominal values of uncertain parameters and their lower and upper limits of uncertainties are shown in Table 2.

The objective of AA-MORO is to maximize pro<sup>fi</sup>t that the re<sup>fi</sup>nery generates through the sale of phthalic anhydride and maximize the purity of phthalic anhydride. The optimization problem needs to satisfy certain constraints such as capacity of inventory, limitation of pressure and temperature in the oil re<sup>fi</sup>ning process and so on. It is subject to the lower and upper bounds on the decision variables as speci<sup>fi</sup>ed in Table 2. In order to obtain robust optimal solutions, an acceptable variation range for each objective is de<sup>fi</sup>ned. In the case study, the acceptable range for each objective is assumed to be $\pm 5 \%$ of the nominal objective function value. By solving the bi-objective optimization problem, AA-MORO obtains a set of Pareto optimum solutions from which the decision maker can choose. The selected values for optimum decision variables $\left( x _ { 1 } \right)$ are assumed to be used or implemented in the oil re<sup>fi</sup>nery and accordingly the decision maker obtains the KPIs from the dashboard (as presented later) that will help him/her to adjust decision variables on $x _ { 1 }$

![](/api/attachments/PBBRQETY/fulltext/images/92295498f7333b67e18190fdb843536d2fe3d4018da204fc9decbf38089c1ba0.jpg)  
Fig. 4. Schematic of case study model.

Table 2  
Table 1  
Decision variables in the oil re<sup>fi</sup>nery case study

<table><tr><td>Description</td><td>Variable</td><td>Unit</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td>Daily crude oil purchase</td><td> $x_{1}$ </td><td>bbl/day</td><td> $9.0 \times 10^{4}$ </td><td> $10.0 \times 10^{4}$ </td></tr><tr><td>Percentage of crude oil sold to external market</td><td> $x_{2,1}$ </td><td>N/A</td><td>0%</td><td>100%</td></tr><tr><td>Percentage of inventory storage sold to external market</td><td> $x_{2,2}$ </td><td>N/A</td><td>0%</td><td>100%</td></tr><tr><td>Mass flow rate of feed air</td><td> $x_{2,3}$ </td><td>kg/s</td><td>24</td><td>27</td></tr><tr><td>Pressure of cooled mixture</td><td> $x_{2,4}$ </td><td>kPa</td><td>100</td><td>104</td></tr><tr><td>Phthalic column reflux ratio</td><td> $x_{2,5}$ </td><td>N/A</td><td>0.3</td><td>2.0</td></tr></table>

## 4.1. Engineering and business simulation

The engineering model focuses on the reactor-distillation process for producing phthalic anhydride from naphtha. The process is simulated in Aspen HYSYS [2], as shown in Fig. 5. In the simulated reactor-distillation process, the raw materials are air and o-xylene. The vaporized o-xylene and hot air are <sup>fi</sup>rst combined and then fed to the reactor. In the reactor, o-xylene is oxidized to form phthalic anhydride but some maleic anhydride may also be formed. The reactor ef<sup>fl</sup>uent enters the switch condenser to remove light gases and water. From the switch condenser, the remaining anhydride and unreacted o-xylene are fed to a series of two distillation columns to separate and obtain phthalic anhydride. The phthalic distillation column separates phthalic anhydride from the feed stream and the maleic distillation column separate maleic anhydride from the remaining components. The top stream from the maleic column contains mostly unreacted o-xylene with a small amount of maleic anhydride and water. In the simulation, the unreacted o-xylene is recycled and combined with the o-xylene as feed material.

The business model is simulated using the agent-based software NetLogo [25]. The business model characterizes the crude oil and end-product markets by simulating oil re<sup>fi</sup>nery supply and the customer demand. The customers, including the internal and external customers are modeled using the customer agents which can be distributors or downstream chemical companies. The internal and external markets for phthalic anhydride each have <sup>fi</sup>ve customer agents. The demand by each customer agent is assumed to be normally distributed. The mean and standard deviation of demand for internal and external customer agents are summarized in Table 3. Notice that the probabilities for customers in both internal and external markets making purchases are presumed to follow truncated normal distribution as per empirical observations. The mean and standard deviation of the probability are also shown in Table 3. Particularly, the external crude oil market is characterized by one customer agent with a 100% probability of purchasing. That is, no matter how much the company decides to sell to the crude oil external market, all quantity will be purchased by the crude oil market customer agent.

Fig. 6 shows the simulation window of the business model in NetLogo. The business parameter and their descriptions in the Netlogo simulation are de<sup>fi</sup>ned in Table 4, where the nominal values of business parameters are <sup>fi</sup>xed. The two circles shown in the center of the simulation window represent the re<sup>fi</sup>nery agent and inventory agent. The black and white agents in the simulation window represent the internal customer agents and external customer agents, respectively. According to the interactions between the markets and the oil re<sup>fi</sup>nery, the pro<sup>fi</sup>t from end-product sales can be obtained as an output from the business model.

The input to the engineering simulation includes three decision variables (Table 1) such as mass <sup>fl</sup>ow rate of feed air, pressure of cooled mixture, phthalic column re<sup>fl</sup>ux ratio, one uncertain parameter such as temperature of feed stream to phthalic distillation column (Table 2) and the feed <sup>fl</sup>ow rate of o-xylene (obtained as a output from the business simulation). The output to the engineering simulation includes the purity and <sup>fl</sup>ow rate of phthalic anhydride. The input to the business simulation includes three decision variables (Table 1) such as daily crude oil purchase, percentage of crude oil sold to external market, percentage of inventory storage sold to external market, one uncertain parameter: price of phthalic anhydride in external market (Table 2) and the <sup>fl</sup>ow rate of phthalic anhydride (obtained as a output from the engineering simulation). The output of the business simulation includes pro<sup>fi</sup>t and the feed <sup>fl</sup>ow rate of o-xylene. In the case study, the engineering and business simulations are connected through an interface program developed in Matlab, which is used to run both simulations programmatically and exchange information between Netlogo and Aspen HYSYS.

## 4.2. Formulation of multi-objective robust optimization

Based on the engineering and business simulations, a multiobjective optimization problem is formulated to maximize pro<sup>fi</sup>t (business objective) and maximize purity of phthalic anhydride (engineering objective), as de<sup>fi</sup>ned in the following:

Maximize : Profit objective1

Maximize : Purity of phthalic anhydride objective2

$$
\begin{array}{l} \text { Subjectto: Business constraints (e.g. inventory) } \\ \text { Engineering constraints (e.g.pressure) } \\ \text { Uncertainty in parameters (e.g.price, temperature) } \\ \text { Lower and upper bounds on x_{2,i},i = 1,\ldots,5} \end{array}\tag{10}
$$

Using the AA-MORO approach, $x _ { 2 , i } , i = 1 , . . . , 5$ (including both business and engineering decision variables in Table 1) is robustly optimized.

## 4.3. Dashboard

Dashboard in the case study is developed using the Graphical User Interface capability in Matlab. It includes three main functional panels: “Key Performance Indicator”, “Decision Control” and “Optimum Decision”, as shown in Fig. 7. The daily crude oil purchase (x ) is controlled by the decision maker and a set of <sup>fi</sup>ve engineering and business decision variables $( x _ { 1 , i } , i { = } 1 , . . . , 5 )$ are considered for optimization by AA-MORO. Pro<sup>fi</sup>t is used as a key performance indicator in the case study, as shown in “Key Performance Indicator” panel. The decision maker can observe current KPI as well as the data in the previous iterations. Based on the observation, decision maker then updates his/her decisions in the “Decision Control” panel when necessary. The history (simulation steps) of decisions made by the decision maker are recorded and shown as well. On the right-hand side, the “Optimum Decision” panel presents the multi-objective (Pareto) optimum solutions to the decision maker. The decision maker can select a preferred solution from the Pareto solutions. The table in the lower half of the “Optimum Decision” panel indicates the optimum values of selected solution.

Uncertain parameters in the oil re<sup>fi</sup>nery case study.

<table><tr><td>Description</td><td>Nominal</td><td>Unit</td><td>Lower limit</td><td>Upper limit</td></tr><tr><td>Price of phthalic anhydride in external market</td><td>1,200</td><td>$/ton</td><td>-5%</td><td>5%</td></tr><tr><td>Temperature of feed stream to phthalic distillation column</td><td>75.27</td><td>°C</td><td>-5%</td><td>5%</td></tr></table>

Table 3  
![](/api/attachments/PBBRQETY/fulltext/images/55d3619384a97fc0622df1010a6de8b9a49c08a9e1054de6c5259abee30ac98a.jpg)  
Fig. 5. Process <sup>fl</sup>ow diagram of engineering simulation

Decision making based on dashboard is an iterative process. In the following paragraph, we brie<sup>fl</sup>y explain how dashboard facilitates such a process:

Initially, the daily crude oil purchase $\left( x _ { 1 } \right)$ is determined according to previous settings in the oil re<sup>fi</sup>nery. Decision maker adjusts the slider bar in the “Decision Control” panel for an initial value of $\langle x _ { 1 } .$ . Dashboard forwards the value of $\dot { \boldsymbol { x } } _ { 1 }$ to the integrated business and engineering simulation model. When decision maker engages the “optimization” button on dashboard, AA-MORO start running multi-objective robust optimization based on the integrated engineering and business simulations for a <sup>fi</sup>xed value of $x _ { 1 }$ (as determined by the decision maker earlier). After optimization completes, AA-MORO obtains a set of multiobjective optimum solutions. These solutions are presented in the “Optimum Decision” panel, as shown in Fig. 7. From these optimum solutions, the decision maker is required to select one solution per his/her preference. The optimum values of the decision variables $\left( x _ { 2 , i } \right.$ $i = 1 , . . . , 5 )$ for the selected solution are shown in the table in the lower half of the ‘Optimum Decision’ panel. These optimum values of $x _ { 2 } ,$ along with $x _ { 1 }$ are then implemented in the oil re<sup>fi</sup>nery. According to engineering operation and the <sup>fi</sup>rm–market interaction, the actual values of re<sup>fi</sup>nery's performance are obtained. Afterwards, decision maker engages the “Update KPIs” button on dashboard to refresh the current value of KPI in the ${ } ^ { \mathfrak { u } } \mathrm { K e y }$ Performance Indicators” panel.

By observing the KPI, the decision maker can adjust the previous values of decision variables on dashboard. The adjustment on $x _ { 1 }$ is forwarded to the integrated simulations by dashboard. Once again, decision maker engages the “Optimization” button on dashboard to run AA-MORO and select an optimum solution for implementation in the oil re<sup>fi</sup>nery. Finally, the current KPIs may be changed and re<sup>fl</sup>ected on the dashboard after decision maker engages “Update KPIs”. Consequently, the decision maker updates $x _ { 1 }$ after observing new data of KPI, and the procedure is repeated until a desired reading of KPI is achieved.

## 4.4. No-regret learning

In the case study, it is assumed that the decision maker has a decision strategy function, as represented by $s ( x _ { 1 } )$ . A decision maker's strategy function is essentially a probability distribution pro<sup>fi</sup>le (or probability density function) of the decision variable $x _ { 1 } .$ The decisionmaking process is comparable to drawing a sample from the strategy function. A change of the strategy function re<sup>fl</sup>ects a change of belief of the decision maker about a decision made previously. In simulating the decision-making process by the decision maker, a no-regret learning algorithm [8] is used in the case study. We assume that the decision maker exhibits learning behavior, i.e., updating his/her decision strategy by iteratively making decisions and observing payoffs. We de<sup>fi</sup>ne “action” as the decision, i.e. $, x _ { 1 } ^ { k } ,$ , made in the k'th iteration. Additionally, we de<sup>fi</sup>ne “strategy”, i.e., s(x ), as a probability density function representing the likelihood that the decision maker chooses an action $x _ { 1 } .$ . By letting the decision maker exhibit learning behavior, we account for the fact that the decision maker may deviate from making optimal deci sion by anticipating the future [24].

Parameter of customer agents in the oil re<sup>fi</sup>nery case study.

<table><tr><td rowspan="2">Description</td><td rowspan="2">Number of agents</td><td colspan="2">Demand (kg/day)</td><td colspan="2">Probability</td></tr><tr><td>Mean</td><td>Std.</td><td>Mean</td><td>Std.</td></tr><tr><td>Internal market</td><td>5</td><td>30,000</td><td>500</td><td>100%</td><td>10%</td></tr><tr><td>External market</td><td>5</td><td>25,000</td><td>1000</td><td>100%</td><td>10%</td></tr><tr><td>External crude oil market</td><td>1</td><td>-</td><td>-</td><td>100%</td><td>-</td></tr></table>

![](/api/attachments/PBBRQETY/fulltext/images/850ba32e60c340c24cd59be89606b2b33f088990000fab420337eafcfd46a1cd.jpg)  
Fig. 6. Agent-based business simulation window in Netlogo.

The no-regret learning algorithm is adapted to simulate the process that the decision maker uses to gradually develop his/her decision strategy by interacting with the dashboard. The no-regret learning algorithm was previously applied to represent a dynamic procedure of action–reactions among multiple players [36]. In the case study study, we consider the decision maker and the optimizer (presenting the optimization results in the dashboard) who make decisions collectively to affect the <sup>fi</sup>rm's pro<sup>fi</sup>t. The decision maker's decision is made by learning from the past whereas the optimizer (AA-MORO) searches and obtains decisions to optimize its objectives.

Let $\prod ( x _ { 1 } , x _ { 2 } )$ denote the pro<sup>fi</sup>t function for the <sup>fi</sup>rm. The decision maker's payoff function is set to be identical to pro<sup>fi</sup>t. In every iteration, the decision maker <sup>fi</sup>rst computes a regret function R de<sup>fi</sup>ned as (k is the iteration counter):

$$
R ^ {k} \left(x _ {1}\right) = \frac {1}{k} \sum_ {t = 1} ^ {k} \left(\Pi \left(x _ {1}, x _ {2} ^ {t}\right) - \Pi \left(x _ {1} ^ {t}, x _ {2} ^ {t}\right)\right)\tag{4}
$$

The regret function re<sup>fl</sup>ects the average increase in pro<sup>fi</sup>t if an action has been always played in previous iterations. The strategy function, i.e., the probability of playing $x _ { 1 }$ in the following iteration, is proportional to the regret:

$$
s ^ {k} (x _ {1}) = \frac {\left[ R ^ {k} (x _ {1}) \right] ^ {+}}{\sum_ {x _ {1} \in X _ {1}} \left[ R ^ {k} (x _ {1}) \right] ^ {+}}\tag{5}
$$

in which:

$$
\left[ R ^ {k} (x _ {1}) \right] ^ {+} = \left\{ \begin{array}{l l} 0, & i f R ^ {k} (x _ {1}) \leq 0 \\ R ^ {k} (x _ {1}), & i f R ^ {k} (x _ {1}) > 0 \end{array} \right.\tag{6}
$$

The above equations assume that the decision variable $x _ { 1 }$ is discrete. In case x<sub>1</sub> is continuous, the summation in Eq. (5) is replaced with an integral. When the decision maker makes a decision, i.e., playing an action, it essentially draws a sample from the updated strategy function.

## 4.5. Dashboard demo

Two case study scenarios are considered. In both scenarios, the range for crude oil input $\left( x _ { 1 } \right)$ is pre-speci<sup>fi</sup>ed based on unit capacity as $9 . 0 \times 1 0 ^ { 4 } \leq x _ { 1 } \leq 1 . 0 \times 1 0 ^ { 5 }$ (bbl/day). In the <sup>fi</sup>rst scenario, the decision maker controls the dashboard manually based on his/her experience. In the second scenario, the decision-making process and the control of dashboard is automated by using a no-regret learning algorithm, which is essentially used to simulate a decision maker.

## 4.5.1. Scenario 1: x<sub>1</sub> is determined by decision maker

In scenario 1, the value of daily crude oil input $\left( x _ { 1 } \right)$ is determined by decision maker. For demonstration, it is assumed that decision maker randomly selects four discrete values for $\times _ { 1 } \colon 9 . 2 \times 1 0 ^ { 4 }$ $9 . 4 \times 1 0 ^ { 4 } , ~ 9 . 6 \times 1 0 ^ { 4 }$ and $9 . 8 \times 1 0 ^ { 4 }$ bbl/day. The decisions on daily crude oil that are selected by the decision maker are used to run the simulation. In each iteration, the decision maker <sup>fi</sup>rst adjusts the decision control bar on dashboard. The value of daily crude oil input $\left( x _ { 1 } \right)$ is sent by dashboard as <sup>fi</sup>xed value to the integrated engineering and business simulation. Next, decision maker engages the “optimization”

## Table 4

Descriptions of business parameters in Netlogo.

<table><tr><td>Description</td><td>Parameter</td><td>Nominal value</td><td>Unit</td></tr><tr><td>Price of crude oil in external market</td><td>pmur</td><td>70</td><td>$/bbl</td></tr><tr><td>Percentage of inventory storage released to internal market</td><td>finv-to-local</td><td>52%</td><td>N/A</td></tr><tr><td>Price of phthalic anhydride in internal market</td><td>p4</td><td>900</td><td>$/ton</td></tr><tr><td>Inventory storage expense of phthalic anhydride</td><td>inv-level-penalty</td><td>4</td><td>$/ton/day</td></tr><tr><td>Inventory stock-out penalty of phthalic anhydride</td><td>stock-out-penalty</td><td>400</td><td>$/ton</td></tr><tr><td>Yield of naphtha from crude distillation</td><td>ynaf</td><td>34%</td><td>N/A</td></tr><tr><td>Yield of oxylene from naphtha</td><td>yoxy</td><td>22%</td><td>N/A</td></tr></table>

![](/api/attachments/PBBRQETY/fulltext/images/e2dfe2615d17e6283487d5c60c4b6b14f22b8498e2921d53bbc041513094a5fa.jpg)  
Fig. 7. A Matlab GUI based dashboard in the case study

level on dashboard to initiate AA-MORO to obtain the multi-objective robust optimal solutions. Finally, decision maker is required to select one desirable solution from a set of optimum solutions based on its objective values. In addition, the optimum values for the decision variables corresponding to the optimum solution are implemented in the oil re<sup>fi</sup>nery by the dashboard.

Fig. 8 shows the optimum solutions for each iteration in the objective function space. In Fig. 8, it can be seen that the two objective functions are con<sup>fl</sup>icting and therefore as pro<sup>fi</sup>t increases (its negative value decreases), the purity of phthalic anhydride decreases (its negative value increases). Comparing different iterations with different values of daily crude oil input, the range on product purity is similar. However the largest pro<sup>fi</sup>t is achieve in iteration 3 when the amount of daily crude oil input is $9 . 6 \times 1 0 ^ { 4 }$ bbl/day.

![](/api/attachments/PBBRQETY/fulltext/images/c512b2cb32ad40e96910a7f1764b7f80cc3fcf2fb4197f78418e0c0ceff9aba8.jpg)  
Fig. 8. Optimum design solution for case study scenario 1.

## 4.5.2. Scenario 2: x<sub>1</sub> is determined by no-regret learning

In scenario 2, instead of the decision maker manually determining the value of daily crude oil input (decision on x ), a no-regret learning algorithm is used to simulate (mimic) the decision making process. Based on the no-regret learning, a total of 300 iterations are simulated. In each iteration, a sample is <sup>fi</sup>rst drawn from the strategy function s(x ) which is characterized by a distribution pro<sup>fi</sup>le (PDF). The procedure of drawing a sample is comparable to the decision maker making a new decision. Dashboard is informed of the new decision and forwards it to the integrated simulation model. Similar to Scenario 1, AA-MORO obtains robust optimum solutions and again the decision maker selects a solution with maximum pro<sup>fi</sup>t. When the selected solution is implemented, the outcome pro<sup>fi</sup>t is used to update the strategy function from which another sample (decision) is drawn and the iteration continues.

The simulated distribution pro<sup>fi</sup>le (PDFs) for $s ( x _ { 1 } )$ in iteration 10, 50, 150 and 300 are shown in Fig. 9. It can be seen that initially (i.e., in iteration 10), the distribution pro<sup>fi</sup>le is diffusive because the decision maker has no information about the past. By iteratively making decisions through interacting with the dashboard and observing the outcome (pro<sup>fi</sup>t), the decision maker gradually shift his/her decision to a more pro<sup>fi</sup>table position, as represented by the shift of distribution of the PDFs. Furthermore, the shrinkage of the distribution pro<sup>fi</sup>le re<sup>fl</sup>ects that the decision maker strengthens her/her belief on the more pro<sup>fi</sup>table decisions.

In Scenario 2, it is noticed that the shape of the distribution pro<sup>fi</sup>le and the observed pro<sup>fi</sup>t remain unchanged (converged) after 300 iterations. As the no-regret learning algorithm is driven by pro<sup>fi</sup>t, the value of pro<sup>fi</sup>t is maximized when the simulation is converged. A closer look at Fig. 9 reveals that the maximum pro<sup>fi</sup>t in Scenario 2 corresponds to the peak of the PDF where the amount of daily crude oil input is between $9 . 5 \times 1 0 ^ { 4 }$ and $9 . 6 \times 1 0 ^ { 4 }$ (bbl/day). This observation appears consistent with the result from Scenario 1 where pro<sup>fi</sup>t is maximum at $\chi _ { 1 } = 9 . 6 \times 1 0 ^ { 4 }$ (bbl/day) among four discrete choices.

![](/api/attachments/PBBRQETY/fulltext/images/9016192f2a1db704f04df5845c6fbaeb1883a691ea5ffb400d1b292a870c48a2.jpg)  
Fig. 9. Simulated distribution pro<sup>fi</sup>le (PDFs) of daily crude oil input.

It should be noted that a variety of other learning algorithms are also applicable to modeling the decision-making process. However, the simulation in Scenario 2 is primarily aimed at demonstrating how a human decision maker and an automated decision agent (i.e., AA-MORO) can interact and collectively improve a <sup>fi</sup>rm's performances (e.g., pro<sup>fi</sup>t). We leave a comparison and appropriateness of learning algorithms to a future study.

## 5. Conclusion

The traditional oil re<sup>fi</sup>nery DSS is built around a single decision maker and based on either business or engineering decisions. but not on both. Under the traditional DSS, business and engineering decision makers make decisions only considering their own domains, and there is no connection/discussion between them. A signi<sup>fi</sup>cant limitation of the traditional DSS scheme is that both business and engineering decisions could drive to optimize their own local functional objective. The decisions made in this way could be con<sup>fl</sup>icting or suboptimal. In this study, we show that when the business and engineering decisions are combined, an integrated DSS can be more effective in supporting the management to make critical decisions. This integrated DSS is based on an “all-at-once” multi-objective robust optimization scheme where business and engineering analysis models are integrated and considered as a whole. Using the proposed integration framework, an oil re<sup>fi</sup>nery is able to obtain a global optimal solution and better decisions than otherwise.

Complexities and problems of non-linearity that are inherent to any re<sup>fi</sup>nery supply chain optimization, and to which multi-objective optimizers have been proposed, can be ef<sup>fi</sup>ciently combined as a backbone of the dashboard with the help of simulation software like NetLogo. The power of NetLogo resides in the ability to represent every single customer, their interactions, and the element of the supply chain and its interactions, and model these appropriately. In the context of stochastic demand data, by varying decision variables, we were able to monitor the company's performance and ultimately tune those decisions to meet our objective of maximum pro<sup>fi</sup>t. Also visible through the simulation were the changes to the elements that would constitute the dashboard, and the set of key performance indicators critical to the health of the company. We use a simple case study to show the decision support role of dashboard and how it can be used to coordinate across various departments in decision making. It is observed that a maximum simulated pro<sup>fi</sup>t can be achieved in the two case study scenarios. This study and the integration framework are in the context of oil and petrochemical industries. The proposed framework is applicable to many <sup>fi</sup>rms with similar business and engineering sectors and it can also accommodate other market variables such as interest rate and exchange rate <sup>fl</sup>uctuations.

As a preliminary study on integrating business and engineering decisions, our current study focuses on small scale models. The interaction and relationship between business and engineering decisions for real-world and larger scale <sup>fi</sup>rms need to be further studied and understood, in order to take advantage of the proposed integration framework. Moreover, as the size of the business and engineering models grows, the proposed optimization based framework could have some computational dif<sup>fi</sup>culties and issues. Such a limitation should be addressed in a future work.

## Acknowledgements

The work presented in this paper was supported in part by The Petroleum Institute (PI), Abu Dhabi, United Arab Emirates, as part of the Education and Energy Research Collaboration (EERC) agreement between the PI and University of Maryland, College Park. Such support does not constitute an endorsement by the funding agency of the opinions expressed in the paper. The authors would like to thank Philippe Kamaha for an earlier development of the model in the case study.

## References

[1] G.K. Al-Sharrah, I. Alatiqi, A. Elkamel, E. Alper, Planning an integrated petrochemical industry with an environmental objective, Industrial & Engineering Chemis try Research 40 (9) (2001) 2103–2111.

[2] Aspen HYSYS and Aspen PIMS, Aspen Technology, 2009http://www.aspentech. com/core.

[3] G. Chryssolouris, N. Papakostas, D. Mourtzis, Re<sup>fi</sup>nery short-term scheduling with tank farm, inventory and distillation management: an integrated simulation based approach, European Journal of Operational Research 166 (3) (2005) 812–827.

[4] S. Clark, Supply Chain Logistics Challenges, PTQ, 2005, pp. 1–4.

[5] M. Gadalla, M. Jobson, R. Smith, Optimization of existing heat-integrated re<sup>fi</sup>nery distillation systems, Chemical Engineering Research and Design 81 (1) (2003) 147–152.

[6] G. Gattu, S. Palavajjhala, D.B. Robertson, Are oil re<sup>fi</sup>neries ready for non-linear control and optimization, International Symposium on Process Systems Engineering and Control, (Mumbai, India, 2003.

[7] I. Grossmann, Enterprise-wide optimization: a new frontier in process system engineering, AIChE Journal 51 (7) (2005) 1846–1857.

[8] S. Hart, A. Mas-Colell, A simple adaptive procedure leading to correlated equilibrium, Econometrica 68 (5) (2000) 1127–1150.

[9] Haveerly GRTMPS, Haverly Systems, http://www.haverly.com/grtmps.htm2003

[10] Honeywell Re<sup>fi</sup>nery and Petrochemical Modeling System (RPMS), Honeywell, 2006 http://www.hpsweb.honeywell.com/ Cultures/en-US/Products/ OperationsApplications/PlanningScheduling/RPMS/default.htm.

[11] W. Hu, M. Li, S. Azarm, A. Almansoori, Multi-Objective Robust Optimization under Interval Uncertainty Using Online Approximation and Constraint Cuts, Journal of Mechanical Design 133 (6) (2011) 061002 9 pages.

[12] J.R. Jackson, I.E. Grossmann, Temporal decomposition scheme for nonlinear multisite production planning and distribution models, Industrial & Engineering Chemistry Research 42 (13) (2003).3045–3055

[13] N. Julka, I. Karimi, R. Srinivasan, Agent-based supply chain management–2: a re-<sup>fi</sup>nery application, Computers & Chemical Engineering 26 (12) (2002) 1771-1781.

[14] N. Julka, R. Srinivasan, I. Karimi, Agent-based supply chain management–1: framework, Computers & Chemical Engineering 26 (12) (2002) 1755–1769.

[15] C.S. Khor, A. Elkamel, K. Ponnambalam, P.L. Douglas, Two-stage stochastic programming with <sup>fi</sup>xed recourse via scenario planning with economic and operational risk management for petroleum re<sup>fi</sup>nery planning under uncertainty, Chemical Engineering and Processing: Process Intensi<sup>fi</sup>cation 47 (9–10) (2008) 1744-1764.

[16] Y.J. Kim, A. Chaudhury, H.R. Rao, A knowledge management perspective to evaluation of enterprise information portals, Knowledge and Processs Management 9 (2) (2002) 57–71.

[17] E. Kondili, N. Shah, C.C. Pantelides, Production planning for the rational use of energy in multiproduct continuous plants, Computers & Chemical Engineering 17 (Supplement 1) (1993) 123–128.

[18] L.Y. Koo, A. Adhitya, R. Srinivasan, I.A. Karimi, Decision support for integrated re-<sup>fi</sup>nery supply chains: Part 2, Design and operation, Computers & Chemical Engineering 32 (11) (2008) 2787–2800.

[19] N.-S. Koutsoukis, G. Mitra, C. Lucas, Adapting on-line analytical processing for decision modelling: the interaction of information and decision technologies, Decision Support Systems 26 (1) (1999) 1–30.

[20] H. Lee, J.M. Pinto, I.E. Grossmann, S. Park, Mixed-integer linear programming model for re<sup>fi</sup>nery short-term scheduling of crude oil unloading with inventory management, Industrial & Engineering Chemistry Research 35 (5) (1996) 1630–1641.

[21] Matlab, ver. 2010a, Mathworks, , 2010http://www.mathworks.com.

[22] S.R. Micheletto, M.C.A. Carvalho, J.M. Pinto, Operational optimization of the utility system of an oil re<sup>fi</sup>nery, Computers & Chemical Engineering 32 (1–2) (2008) 170–185.

[23] J. Mouaward, Chilly Climate for Oil Re<sup>fi</sup>ners, The New York Times, 2009.

[24] D.B. Montgomery, M.C. Moore, J.E. Urbany, Reasoning about competitive reactions: evidence from executives, Marketing Science 24 (1) (2005) 138–149.

[25] Netlogo, U. Wilensky, Netlogo, Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL, 1999http://www.ccl. northwestern.edu/netlogo.

[26] M. Paolucci, R. Sacile, A. Boccalatte, Allocating crude oil supply to port and re<sup>fi</sup>nery tanks: a simulation-based decision support system, Decision Support Systems 33 (1) (2002) 39–54.

[27] J.M. Pinto, M. Joly, L.F.L. Moro, Planning and scheduling models for re<sup>fi</sup>nery operations, Computers & Chemical Engineering 24 (9–10) (2000) 2259–2276.

[28] S.S. Pitty, W. Li, A. Adhitya, R. Srinivasan, I.A. Karimi, Decision support for integrated re<sup>fi</sup>nery supply chains: Part 1, Dynamic simulation, Computers & Chemical Engineering 32 (11) (2008) 2767–2786.

[29] A. Pongsakdi, P. Rangsunvigit, K. Siemanond, M.J. Bagajewicz, Financial risk management in the planning of re<sup>fi</sup>nery operations, International Journal of Produc tion Economics 103 (1) (2006) 64–86.

[30] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (3) (2007) 1044–1061.

[31] S. Raghunathan, A structured modeling based methodology to design decision support systems, Decision Support Systems 17 (4) (1996) 299–312.

[32] H.R. Rao, R. Sridhar, S. Narain, An active intelligent decision support system – architecture and simulation, Decision Support Systems 12 (1) (1994) 79–91.

[33] H.R. Rao, A. Chaudhury, M. Chakka, Modeling team processes: issues and a specific example, Information Systems Research 6 (3) (1995) 255–285.

[34] SAP, SAP, 2010. http://www.sap.com/index.epx.

[35] C. Wang, Enterprise Integration of Management and Automation in a Re<sup>fi</sup>nery, in: E. Arai, J. Goossenaerts, F. Kimura, K. Shirase (Eds.), Knowledge and Skill Chains in Engineering and Manufacturing Information infrastructure in the Era of Global Communications, Springer, 2005, pp. 321–328.

[36] Z. Wang, S. Azarm, P.K. Kannan, Strategic Design Decisions for Uncertain Market Systems Using an Agent Based Approach, Journal of Mechanical Design 133 (4) (2011) 041003 11 pages.

[37] N. Zhang, X.X. Zhu, A novel modelling and decomposition strategy for overall re-<sup>fi</sup>nery optimisation, Computers & Chemical Engineering 24 (2–7) (2000) 1543–1548

Weiwei Hu is a Ph.D. candidate and research assistant in the Design and Decision Support Laboratory at University of Maryland, College Park. He received his M.S. in Mechanical Engineering from Michigan Technology University in 2007, and B.S. in Automotive Engineering with honor in 2000 from Zhejiang University. His current research focuses on multi-objective optimization and decision making under uncertainty.

A. Almansoori obtained his Bachelor in Chemical Engineering from Florida Institute of Technology and PhD in Chemical Engineering from Imperial College, London. At Imperial, he conducted research on the development of mathematical optimization frameworks that can support strategic decisions in designing and operating the future hydrogen supply chain network. He is currently an Assistant Professor in the Department of Chemical Engineering at the Petroleum Institute in Abu Dhabi. He works on understanding and <sup>fi</sup>nding optimal solutions to some of the problems encountered by ADNOC operating companies utilizing his background in process simulation, modeling and optimization. Additionally, he conducts general research in the area of hydrogen and fuel cell technology.

P. K. Kannan is Ralph J. Tyser Professor of Marketing Science, Smith School of Business, University of Maryland, College Park, Maryland, and he is the Chair of the Department of Marketing. His current research stream focuses on new product/service development, design and pricing of digital products and product lines, marketing and product development on the Internet, e-service, and customer relationship management (CRM) and customer loyalty. He has received several grants from National Science Foundation (NSF), Mellon Foundation, SAIC, and PricewaterhouseCoopers for his work in this area. His research has also won the John Little Best Paper Award (2008) and the INFORMS Society for Marketing Science Practice Prize Award (2007). Professor Kannan's research has also been selected as a <sup>fi</sup>nalist for the Paul Green Award (2008).

Shapour Azarm is Professor of Mechanical Engineering and Director of Design Decision Support Lab at the University of Maryland, College Park. His research interests are in multi-objective design optimization, multi-attribute decision analysis, and integration of engineering design with marketing for product design. Dr. Azarm has served as an Associate Editor and Guest Editor of numerous journals. He received the 2007 ASME Design Automation Committee Award: “For his sustained and meritorious contributions to research in Design Automation: Speci<sup>fi</sup>cally in computational design optimization and engineering design decision making." With two of his former PhD students, he received the Best Paper Award in the 2009 ASME Design Automation Conference. Dr. Azarm is a Fellow of the American Society of Mechanical Engineers.

Zhichao Wang is a Ph.D. candidate and research assistant in the Design and Decision Support Laboratory at University of Maryland, College Park, where he also obtained his Master of Science degree in Mechanical Engineering. His research interest is to support product design decisions by modeling customer preference, market competition and retail channels.
