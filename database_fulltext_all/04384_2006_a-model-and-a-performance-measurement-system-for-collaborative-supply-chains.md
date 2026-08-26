---
otero_id: 4384
otero_key: "NP8CDABS"
title: "A model and a performance measurement system for collaborative supply chains"
authors: "Bernhard J. Angerhofer; Marios C. Angelides"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.12.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A model and a performance measurement system for collaborative supply chains

Bernhard J. Angerhofer, Marios C. Angelides T

Department of Information Systems and Computing, Brunel University, Uxbridge, Middlesex UB8 3PH, United Kingdom

Available online 19 February 2005

## Abstract

Modeling the constituents of a collaborative supply chain, the key parameters they influence, and the appropriate performance measures in a decision support environment enables prior understanding of the impact on the performance of a collaborative supply chain as a result of changes in the constituents and key parameters. In turn, this allows pinpointing of those areas where the actual supply chain can be improved and hence manage the chain’s performance. This paper shows how the constituents, key parameters and performance indicators are modelled into the environment and through a case study illustrates how the decision support environment may be used to improve the performance of a collaborative supply chain by pinpointing areas for improvement.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Collaborative supply chain; Performance measurement

## 1. Introduction

The objective of a collaborative supply chain is to gain competitive advantage, by improving overall performance through taking a holistic perspective of the supply chain [5]. Overall logistics control is to be designed that all <sup>d</sup>players<sup>T</sup> are beneficiaries [50]. In order to be efficient and cost effective across the entire system, total costs have to be minimized and activities have to be aligned from the strategic level through the managerial to the operational level [43]. By considering a supply chain from a collaborations point of view, several constituents have to be brought together (e.g. [2–4,7,8,13,14,16,17,19,21,23,25,27,28,31,34, 35,42,48,50,51]).

Akkermans et al. [2] propose an <sup>d</sup>exploratory causal model<sup>T</sup> which contains stakeholders, business strategy, processes and enabling technology. Stakeholders refers to the primary <sup>d</sup>players<sup>T</sup> of the supply chain, therefore the term describes a particular group that is part of or takes an interest in a supply chain. Each stakeholder often stands in multiple relationships to all other stakeholders and may comprise of more than one firm in real life. Stakeholders are the supplier, manufacturer, wholesaler, retailer and customer [23,40,44] but also third parties involved in the flow of good along a supply chain.

Business strategy consists of the competitive mission, the core operations strategy, and the player’s business goals [40]. Competitive mission may be derived from two generic competitive strategies [38], lowest-cost production and product differentiation. The aim of a core operations strategy is to support the positioning and measuring of the success of products and hence ensure optimum use of all firm’s resources. Each player’s business goals, since they may be different, need to be aligned with those of the collaborative supply chain. The alignment may be achieved through a performance trade-off balancing strategy that aims to achieve a balance between individual and collaborative supply chain business goals.

The four core supply chain processes are <sup>d</sup>Plan<sup>T</sup>, <sup>d</sup>Source<sup>T</sup>, <sup>d</sup>Make<sup>T</sup> and <sup>d</sup>Deliver<sup>T</sup> [42]. <sup>d</sup>Plan<sup>T</sup> defines the planning activities involved in running the other three collaborative supply chain processes. It contains sub-processes dealing with resource planning, demand planning, capacity planning, production planning, inventory planning, and distribution planning. <sup>d</sup>Source<sup>T</sup> relates to processes on the supplier side and contains two sub-processes, material acquisition and the management of the sourcing infrastructure. The <sup>d</sup>Make<sup>T</sup> process comprises production execution and the management of the <sup>d</sup>Make<sup>T</sup> infrastructure. <sup>d</sup>Deliver<sup>T</sup> consists of four management subprocesses: order, warehouse, transportation and delivery.

Collaborative supply chain information systems can be divided into Transaction Processing Systems (TPS), Management Information Systems (MIS), and Executive Information Systems (EIS). TPS are designed to carry out defined functions, transactions, or routine business activity [20], typical examples include communication and production systems. MIS provide relevant, timely and useful information for management control; in order to support planning and coordination of resources. EIS systems are designed to provide clear, summarized information to highlight weaknesses and opportunities for the collaborative supply chain. The information provides supports senior executives in their decisions on facility location, capital investment and restructuring of the chain.

Whilst the Akkerman model is able to provide an explanation of success or failure in international supply chain management, it does not capture the full complexity of collaborative supply chains. Above all, topology is required to show the material flow between the primary players in a supply chain, where processes may be linked within and between companies. Also, the absence of levels of collaboration leads to a lack of explanation of the interactions of players in a supply chain.

Supply chain topology describes the configuration of the supply chain based on three basic flow patterns: single route flow, convergent flow, and divergent flow [49]. By combining these basic flow patterns, complex supply chain networks can be described. This represents the topology of material flow between the primary players in a supply chain, where processes may be linked within and between companies.

Collaboration takes many different forms, including strategic alliances, joint ventures, third party logistics, short- and long-term contracts, partnership sourcing, and retailer–supplier partnerships. Collaboration at the strategic level is concerned with decisions that influence the future direction of the collaborative supply chain, for example, capital investment and restructuring the supply network through acceptance or exclusion of players. At the managerial level, the main concern is the optimization of the flow of goods and involves forecasting, planning and resource control. The operational level encompasses routine and repetitive tasks such as production or transportation scheduling and stock control.

A model by Anderson et al. [4] includes stakeholders in the form of three firms and addresses business strategy through policy development, but it does not contain enabling technology. The model demonstrates that one player’s production capacity limitation causes demand fluctuation. However, the management of collaborative supply chain processes is supported through enabling technology. As Lewis et al. [33] point out, enabling technology is essential to the ultimate success of the supply chain. This is due to support of effective management and control of material flows across the boundaries between companies, and the provision of an information flow that is accurate, timely and accessible to all players in the chain. Hence, without considering enabling technology the simulation results of Anderson’s model [4] are limited in scope.

The Supply Chain Operations Reference model [42] provides a detailed view of supply chain processes, along with enabling technology and stakeholders, but lacks the business strategy constituent. The model, therefore, is able to capture the operational and managerial aspects of a collaborative supply chain; nevertheless it falls short in providing an explanation of the impact of the business strategy on the setup and the success of the collaborative supply chain in the marketplace. As business strategy is developed according to the type of competitive environment entered, it has a great impact on supply chain operations, goals and performance measurement, and, therefore, needs to be considered in a model of a collaborative supply chain.

All models above contain stakeholders and processes, which are the essential constituents of any supply chain, as stakeholders are the primary players of the supply chain and are linked together via collaborative supply chain processes. Absence of stakeholders would not yield a collaborative supply chain in the first place, and absence of processes makes the supply chain a black box whose contents could not be optimized.

The models discussed above suggest six constituents that account for the complexity inherent in a CSC, a system consisting of integrated processes and multiple relationships within and between the stakeholders. In order to truly assess the performance of a CSC, we need to bring together all six constituents in a single model.

Henceforth, the objective of this paper is to model all six constituents of a CSC and the key parameters they influence, and develop appropriate performance measures, with which we can assess the impact of constituent and parameter changes on the performance of the CSC. The structure of the paper is as follows. Firstly, we build a model of a collaborative supply chain (CSC) that comprises of all the constituents as a <sup>d</sup>Weltanschauung<sup>T</sup> (individual worldview) [15]. Secondly, we derive a suitable performance indicator. Thirdly, we incorporate both the model and the indicator in a decision support environment (DSE) which we use to test the performance of a real collaborative supply chain and attempt to pinpoint areas for possible improvement. Finally, the paper concludes.

## 2. Building the model

A CSC model which encompasses all six constituents as a <sup>d</sup>Weltanschauung<sup>T</sup> is a system of interlinkages (i.e. topology) and inter-relationships (i.e. levels of collaboration) of the stakeholders along with the processes undertaken, its supporting technology and the business strategy employed. Fig. 1 gives an overview of the proposed collaborative supply chain model. The following section discusses each constituent and the key parameters it influences in detail.

## 2.1. Stakeholders

The stakeholders in a collaborative supply chain each play a particular role [12,40]: The supplier provides raw material and acts as component integrator and single point-of-contact vendor. Integration into the manufacturer’s inventory planning and scheduling allow fast cycle times. The primary role of the manufacturer is the development and production of goods for industry or end customer. In many cases, manufacturers take the responsibility for designing and managing the supply chain. The wholesaler, if present in a collaborative supply chain, acts as a middleman in order to consolidate goods from various sources. Retailers form the end of the supply chain and perform the role of selling goods directly to nonbusiness customers. In the past, customers were only viewed as recipients of goods produced by the manufacturers, but in recent years there has been a shift towards the customers becoming the driving force [41] (see Fig. 2).

The customer is considered the <sup>d</sup>drain<sup>T</sup>, the receiver of goods, whereas the other players are considered the <sup>d</sup>source<sup>T</sup>, the provider of goods. Hence, the customer influences the Sales Quantity (SQ), Revenue (R) and Profit ( P) via Customer Demand (CD). CD is an external variable determined by market conditions. Product Quality (PQ) and Stock Outs (SO), the total unsatisfied customer demand, influence Customer Satisfaction (CS) independently. Upstream the supply chain, the remaining players are responsible for the production and distribution of the goods. Any changes in any number of these may have a drastic effect on the performance of the collaborative supply chain [36].

![](/api/attachments/NP8CDABS/fulltext/images/8d2a5d78a80206feeecd40c4776cc6314bb2bee5927c3b8469bd78dbddd65188.jpg)  
Fig. 1. A model of a collaborative supply chain.

Adding players influences Costs (C). The supply chain may become more difficult to manage, which is reflected in higher costs and more Information Delay (ID), the amount of time an order requires to <sup>b</sup>travel<sup>Q</sup> upstream through all stages of the supply chain. There also is an influence on Forecast Accuracy (FA) and Time To Market (TTM) via additional information delays. Forecast accuracy measures how close the expected customer demand (ECD) is to the actual customer demand and time to market gives the time interval from order generation until arrival of the product at the retailer and is measured in days. However, if new players are well integrated and their business strategy is well aligned to that of the whole collaborative supply chain, then the positive impact on collaborative supply chain performance may dominate. Additional players may reduce the risk of stock outs and affect supply chain flexibility to give a better overall performance.

![](/api/attachments/NP8CDABS/fulltext/images/2479a474c175eb648f56f91d275cb9e75898ed8e235f937195406defd98bb208.jpg)  
Fig. 2. Stakeholders.

## 2.2. Topology

Based on the choice of stakeholders, certain topology configurations become possible. For example, if there is one manufacturer, then the type of link between supplier and manufacturer must be either single route or convergent as shown in Fig. 3.

Establishing more than one link between manufacturer and wholesalers may increase costs, but on the other hand could decrease the total time until products reach a retailer and thus time to market may go down. Also, if a retailer receives goods from more than one warehouse, the risk of stock outs at the retailer is reduced, thus ensuring that the fulfillment of customer demand is improved. This at the same time may have a positive impact on supply chain flexibility. Additional links will incur an additional cost, for example for extra planning and transportation of goods, which may cause the costs to increase. Extra investment in enabling technology might be necessary to cope with more requirements in demand planning. However, reduced stock outs lead to higher customer satisfaction.

## 2.3. Enabling technology

There are always costs involved in implementing and using enabling technology, generally implementa tion and maintenance costs. Implementation costs may consist of the cost of hardware and software itself, but also possible costs involved in changing business processes and user training. The potential benefits of enabling technology are extensive [30] at every level.

At the operational level, transaction processing systems provide support to supply chain processes and enable an effective communication infrastructure. For example, an Electronic Data Interchange (EDI) system may allow for fast and reliable data exchange between supply chain players, thus it may provide the basis for appropriate supply and demand planning. At the managerial level, planning and coordination activities are supported by management information systems, which can provide relevant and accurate information in a timely manner. For instance, an integrated ERP system may lead to better Capacity Utilization (CU) and, therefore, reduce costs. Together with improved forecast accuracy this may lead to better product availability at the retailer, therefore, reducing the risk of stock outs.

At the strategic level, executive information systems aim at supporting decision-makers in strategic decisions that predominantly have long-term effects. By providing clear and summarized information [40] they enable decision-makers to choose the right course of action in order to improve supply chain performance whilst ensuring medium- to long-term success. EIS may have an indirect effect on most of the performance variables in the collaborative supply chain, though this effect will show normally only after a certain time. For example, a decision-maker may find through an ad hoc enquiry that many stock outs occurred whilst Capacity Utilization was at a high level but below maximum. Thus, a project could be started to determine whether an additional manufacturing site could help overcome this problem. Based on the outcome of this investigation, production capacity may be increased, but this might only be available after a certain period of time. Fig. 4 maps technology against the organizational level.

## 2.4. Levels of collaboration

The decision on which level(s) collaboration is suitable and beneficial is determined by the market environment and business strategy. Collaboration at the operational level may take the form of a routine task such as transportation scheduling. For instance, wholesalers and retailers could work together closely to improve the delivery of goods to the various retailers based on actual stocking levels and expected demand at the individual retailer. This may cause some extra costs, but the benefits in terms of increased flexibility and fewer stock outs may outweigh those costs. More collaboration at the managerial level could lead to better planning and forecasting. Through enhanced information flow between the players in the collaborative supply chain, information delay could be decreased and forecast accuracy improved; the sharing of capacity and inventory information may lead to lower inventories and at the same time an increased supply chain flexibility. Managerial decisions typically work on a short to medium time frame; therefore, the effect of changes may not be visible immediately.

![](/api/attachments/NP8CDABS/fulltext/images/84dd1dda8157e146f89fe678a96b9c9a9198821c3ef4742dcaaafbd2313cecca.jpg)  
Fig. 3. Topology.

![](/api/attachments/NP8CDABS/fulltext/images/b29d9b1cda1562879c319d0b8353196ad39164f3238f4fffa6039625456eda17.jpg)  
Fig. 4. Enabling technology.

Collaboration at the strategic level may involve decisions that will have medium- to long-term effects. Examples are decisions that have major impacts on the collaborative supply chain, such as capital investment or restructuring of the supply chain. Collaboration at the strategic level also may involve giving visibility to internal figures or structural details of the individual players. Hence, higher levels of collaboration, whilst normally associated with additional costs, should have a positive effect on key performance variables in the collaborative supply chain. There is, however, a certain risk involved for each player. For example, the information shared could be used by one of the players to its sole advantage, but if well managed the positive effect may prevail.

Fig. 5 shows an example of a possible collaboration at every level between a supplier and a manufacturer.

Higher levels of collaboration thus have a direct impact on forecast accuracy, information delay and supply chain flexibility, which in turn may improve time to market and customer satisfaction. There is a cost with collaboration, which is due to the increased effort in administration and necessary compromising for each of the players.

## 2.5. Business strategy

Whilst players may want to retain a certain amount of individuality, the competitive mission, core operations strategy and the players’ business goals [40] must be closely aligned with those of the supply chain [27] (see Fig. 6).

![](/api/attachments/NP8CDABS/fulltext/images/a946bc30160005ec823f1177d9bc5612de9bafff6694753a6e7b6e35aeffdbb9.jpg)  
Fig. 5. Levels of collaboration.

![](/api/attachments/NP8CDABS/fulltext/images/b2b171f80f37de41da9482473df7d68bee404ae93692e2ca9c53071651cbd37a.jpg)  
Fig. 6. Business strategy.

Level of Alignment (LA) measures how close the individual players’ business strategy is to that of the collaborative supply chain. The higher the level of alignment, the better centralized control can be approached. This may lead to reduced information delay, increased forecast accuracy and thus reduce the risk of stock outs. The level of alignment is a qualitative measure that indicates how close the individual players’ business strategy is to that of the collaborative supply chain. According to the competitive environment, an appropriate Unit Selling Price (USP) can be chosen, which in turn will prompt a response in customer demand.

## 2.6. Processes

The players of the collaborative supply chain take shared responsibility of the four core supply chain processes, Plan, Source, Make and Deliver [42,46], as shown in Fig. 7.

The performance of those processes influences the performance of the whole collaborative supply chain. Each of the four core processes is influenced by changes in the other constituents as well. For example, an increased use of enabling technology may improve operations through better production and distribution planning. Better collaboration may improve information visibility and, therefore, lead to better planning. The performance of the processes has a direct effect on several key variables. Improvements in the <sup>d</sup>Make<sup>T</sup> process may lead to better product quality, and shorter time to market through improved cycle time [1]. With improved performance in the <sup>d</sup>Source<sup>T</sup> process this may lead to better capacity utilization and hence reduce costs, which in turn could increase profit. The <sup>d</sup>Deliver<sup>T</sup> process may benefit from better collaboration and use of enabling technology and reduce time to market, the risk of stock outs and increase supply chain flexibility. Improvements in the <sup>d</sup>Plan<sup>T</sup> process could lead to a better forecast accuracy and allow a better estimate for required production capacity.

![](/api/attachments/NP8CDABS/fulltext/images/4d0ea1bb09768d2780d25f21c4b933c34289b41e50154dcc73c76336d747a2d5.jpg)  
Fig. 7. Processes.

## 2.7. Model quantification through constituent inter-linkages

Table 1 shows which variables are influenced by which constituent based on the review of the models presented in Section 1 and the discussion of each constituent in the previous sections.

The table shows that changes in different constituents may influence the same variable in a variety of ways. The choice of variables used in determining the effect of changes in any of the six constituents on the collaborative supply chain performance will depend on the nature of the specific collaborative supply chain. This means that there may be numerous ways in which changes could be made to influence the value of a key variable or performance indicator.

Sales Quantity and Profit can be quantified as

$$
\begin{array}{l} S Q (t) = \int_ {t _ {0}} ^ {t} s a l e s (s) \mathrm{d} s + \mathrm{SQ} (t _ {0}) \text {   where } \\ s a l e s (s) = \left\{ \begin{array}{l l} C D (s), & C D (s) \leq \mathrm{RI} (s) \\ \mathrm{RI} (s), & C D (s) > \mathrm{RI} (s) \end{array} \right. \end{array}\tag{1}
$$

$$
P = R - C\tag{2}
$$

where RI is the Retailer Inventory and R=USP\*SQ.

Customer Satisfaction is both a qualitative and a nonlinear measure [45] and is a function of product quality and stockouts. It can be quantified as

$$
\mathrm{CS} (t) = \int_ {t _ {0}} ^ {t} \operatorname{net} _ {-} \mathrm{CS} (s) \mathrm{d} s + \mathrm{CS} (t _ {0})\tag{3}
$$

where

$$
\begin{array}{c} \text { net\_CS} (s) = (\text { CS } (s) - \text { min\_CS }) * (1 - \text { saturation } (s)) \\ * \text { ref\_CS} (s) \end{array}
$$

$$
\begin{array}{l} \text { saturation } (s) = \frac {\text { CS } (s)}{\text { max\_CS }} \\ \text { ref\_CS } (s) = \text { PQ\_on\_CS } + \text { SO\_on\_CS } (s) \end{array}
$$

The non-linear behaviour of CS is modelled by net\_CS(s) with ref\_CS(s) driving the change in CS between min\_CS and max\_CS. Hence, ref\_CS(s) represents the combined influence of PQ\_on\_CS, the influence of PQ on CS, and SO\_on\_CS(s), the influence of SO on CS over time.

Cost can be qualified as

$$
\begin{array}{l} C = \text { Variable   Cost(VC) } + \text { Fixed   Cost(FC) } \\ \text { where } \end{array}\tag{4}
$$

$$
\mathrm{VC} = \text { Unit   Variable   Cost   (UVC) } * \text { Total   Production   (TP) }
$$

$$
+ \text {   Repair   Cost   (RC)   }
$$

FC is independent of the number of units produced and is determined by the time interval passed. VC is determined on a per unit basis and is calculated based on the total number of units produced. Thus, C is measured as cost per unit or as an aggregate cost over a specific time interval, whereby the time interval must be the same for the whole supply chain.

The constituents impact on variables

<table><tr><td></td><td>Stakeholders</td><td>Topology</td><td>Levels of collaboration</td><td>Enabling technology</td><td>Business strategy</td><td>Processes</td></tr><tr><td>Capacity Utilization</td><td></td><td></td><td></td><td>✓</td><td></td><td>✓</td></tr><tr><td>Cost</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Customer Demand</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Customer Satisfaction</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Forecast Accuracy</td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Information Delay</td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>Level of Alignment</td><td></td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Product Quality</td><td></td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td>Production Capacity</td><td></td><td></td><td></td><td>✓</td><td></td><td>✓</td></tr><tr><td>Profit</td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td>Revenue</td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales Quantity</td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Stock Outs</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Supply Chain Flexibility</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Time to Market</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Unit Selling Price</td><td></td><td></td><td></td><td></td><td>✓</td><td></td></tr></table>

Forecast Accuracy and Time to Market can be quantified as

$$
F A = \frac {a b s (E C D - C D)}{C D}\tag{5}
$$

$$
T T M = I D + \text { PTMT   where } I D = \sum_ {i} \mathrm{id} _ {i}\tag{6}
$$

${ \mathrm { i d } } _ { i }$ denotes the Information Delay between stages i in the supply chain and PTMT measures the time from production start until the goods are available at the Retailer Inventory.

StockOuts measures the total unsatisfied Customer Demand in number of units and can be quantified as

$$
\begin{array}{l} S O (t) = \int_ {t _ {0}} ^ {t} s o (s) \mathrm{d} s + S O (t _ {0}) \text {   where } \\ s o (s) = \left\{ \begin{array}{l l} 0, & \mathrm{RI} (s) \geq C D (s) \\ C D (s) - \mathrm{RI} (s), & \mathrm{RI} (s) <   C D (s) \end{array} \right. \end{array}\tag{7}
$$

Finally, Capacity Utilization can be quantified as

$$
\mathrm{CU} (t) = \frac {\text { production } (t)}{\mathrm{PC}}\tag{8}
$$

Supply chain performance has been traditionally assessed by measurement of key supply chain processes, such as the <sup>d</sup>Source<sup>T</sup>, <sup>d</sup>Make<sup>T</sup> and <sup>d</sup>Deliver <sup>T</sup> supply chain processes [6,22,32,42,46], by single measure such as demand amplification [4,47], or by a composite performance indicator [26,49]. Most authors agree that a measurement system should use each type of measure, resource (RM), output (OM) and flexibility (FM) [10].

Resource measures, which generally measure costs, will help towards improving supply chain performance by minimising costs, or if they measure efficiency, help towards improving supply chain performance by maximising resource utilization. Examples of resource measures are production costs, equipment utilization, or demand amplification. Resource measures constitute the most widely used measures in supply chain performance measurement [9,28], and are typically used in form of performance indicators such as total cost, distribution cost, manufacturing cost and inventory cost [6,22,29,32, 42,46,49].

The goal of resource measures is to achieve a high level of cost efficiency. If resource measures were missing in a performance measurement system, the collaborative supply chain would constitute an unconstrained system, allowing to realize 100% service levels and total flexibility at the same time, at any cost. Therefore, the results of any performance measurement, where resource measures are omitted, lead to local optimization and consequently are meaningless in the context of a collaborative supply chain. For example, resource measures are required to measure the impact of the <sup>d</sup>enabling technology<sup>T</sup> constituent on collaborative supply chain performance.

Output measures, which measure the outputs of a supply chain, attempt to provide means to optimise performance. Examples are sales and profit, cycle time, and customer related measures such as service level. As an output measure, customer service level defines the service and performance level that will be provided to a customer. Service level is defined commonly as type 1 or type 2 service level [24]: Type 1 service level measures the proportion of periods in which all demand is met, type 2 service level measures the proportion of demand satisfied immediately from inventory.

Without output measures no assessment of the operational performance of a collaborative supply chain is possible. A collaborative supply chain exists to produce some output, therefore, output measures are essential in measuring collaborative supply chain performance. Furthermore, the absence of output measures would render resource measures worthless, as any efforts in terms of costs and efficiency would not be reflected in the inter-relationship between costs and output levels. For example, the impact of the <sup>d</sup>process<sup>T</sup> constituent on collaborative supply chain performance could not be determined without output measures like cycle time or number of products shipped.

Flexibility measures are used to measure the supply chain’s ability to cope with volume and schedule variations from customers as well as suppliers. For instance, flexibility may be measured in terms of by how much an ordered volume can be changed during specific time periods after the order date or before the delivery date. Thus, flexibility measures determine the potential behaviour of a collaborative supply chain, whereas resource and output flexibility measure the actual performance of a collaborative supply chain. The degree of importance of flexibility to a collaborative supply chain depends on the market environment in which it operates. Regardless, flexibility needs to be measured to assess its impact on collaborative supply chain performance.

Resources affect the output of a collaborative supply chain, whilst the output is important in determining the flexibility [10]. The absence of flexibility measures will prevent to gain a complete picture of supply chain performance. Without flexibility measures there is no means by which the response of a collaborative supply chain to demand schedule and volume variations could be assessed. Measuring the potential to adjust to a changing environment, however, is essential as it reflects the performance trade-off inherent in a complex system such as a collaborative supply chain.

RM, OM and FM can be quantified as:

$$
\mathrm{RM} = C\tag{9}
$$

$$
\mathrm{OM} = P ^ {*} C S\tag{10}
$$

$$
\mathrm{FM} = \frac {\mathrm{PCratio} ^ {*} \mathrm{RIratio}}{\mathrm{TTM}}\tag{11}
$$

where

$$
\mathrm{PC} \text { ratio } = (2 - \mathrm{CU})
$$

$$
\begin{array}{r l} \text { RI   ratio } & = 1 + \frac {\mathrm{RI}}{\text { Total   Inventory }} \\ & = 1 + \frac {\mathrm{RI}}{\mathrm{MI} + \mathrm{WI} + \mathrm{RI}} \end{array}
$$

PC ratio is a measure for the remaining production capacity and PC ratio<sup>a</sup>[1,2) to avoid the term becoming 0 in the case of CU reaching 100%. The greater PC ratio is, the greater the long-term flexibility of the supply chain is. MI is the Manufacturer Inventory, WI is the Wholesaler Inventory and RI is the Retailer Inventory. RI ratio is a measure that expresses the relationship of retailer inventory to the total inventory. The greater RI ratio is, the higher the shortterm flexibility of the supply chain. TTM measures the time from order generation until the goods reach the retailer. Therefore, the greater the term 1/TTM is, the quicker the supply chain can react to changes in demand and hence, the greater the flexibility is.

A performance measurement indicator (CSCPI) combining RM, OM and FM can be quantified as:

$$
\begin{array}{r l} \text { CSCPI } & = \frac {\beta \mathrm{OM} ^ {*} \gamma \mathrm{FM}}{\alpha \mathrm{RM}} \text { with   weighting   factors } \\ & \alpha , \beta , \gamma \in [ 0. 5, 1. 5) \end{array}\tag{12}
$$

Each of the three may be adjusted by an individual weighting factor such as $\alpha , \beta , \gamma { \in } [ 0 . 5 , 1 . 5 )$ which must remain the same throughout the duration of a measurement exercise. For instance, in order to reflect the higher degree of importance of costs we set $\beta , \gamma { = } 1$ and a=1.1 in order to give a higher weighting to the resource measure.

The CSCPI is not an absolute performance metric at a particular point in time but a comparative performance indicator over a period of time. Its main purpose is to measure the potential impact of changes over time. Hence what is important is the consistent use of the numerical values of the weighting factors before and after any adjustment across different scenarios when assessing a particular supply chain, and not the choice of numerical value used [11].

In the next section we implement the model and indicator in a DSE which we use to test the performance of a real collaborative supply chain and to pinpoint areas for improvement.

## 3. Case study

In order to demonstrate the application of both the model and the performance indicator, a simple case study involving an existing collaborative supply chain is used. The collaborative supply chain under investigation produces and delivers mobile communication equipment. It consists of one supplier, two manufacturers, one wholesaler and one retailer. The boundaries of the system are production start using raw materials on the upstream, and sales to customers on the downstream. The supply chain is capacity-constrained with long production lead times and an increasingly dynamic market in combination with decreasing product life cycles. This puts pressure on time to market, product quality and supply chain flexibility.

We use the System Dynamics (SD) methodology in Powersimk Studio 2003 to simulate this collaborative supply chain and to implement the performance measurement indicator. With SD, a problem situation is represented in terms of processes, information flows, feedback and delays, boundaries and strategies/policies. The modelling process comprises of several (iterative) steps, forming a loop rather than a linear progression [39]: problem definition and model purpose, system conceptualization, model formulation, and simulation and policy analysis (Fig. 8).

The focus with SD is on a problem rather than on a system, therefore defining the problem and the purpose of the model is always the first step. Conceptualising a system is then generally accomplished in a visual way through a Flow Diagram (Stock and Flow Map). This step also involves the definition of the boundaries of the problem situation. After model conceptualization, the mathematical equations for all the relationships in the model are specified and the model parameters are quantified. Simulation is then used to trace the behaviour of variables over time. This helps to understand the model behaviour and assess the effect of different decision policies on the behaviour over time of key variables.

The problem as perceived by the stakeholders is capacity utilization. Fig. 9 shows the Sales figures from January 2000 to December 2000, the Production Starts and the average Production to Market Time.

Fig. 10A and B shows the conceptualization of the model as a Stock and Flow Map. In SD delays are commonly modelled explicitly. In order to reduce the visual complexity of the Stock and Flow Map, delays are modelled implicitly in this model. In the NW region in Fig. 10A the material flow through the collaborative supply chain begins with raw material from Supplier, then Manufacturer Inventory to Wholesaler Inventory and finally to Retailer Inventory. The top left corner shows how Capacity Utilization is influenced by Production Capacity and Production. The calculation of StockOuts is shown in the top right hand corner. The bottom half of NW demonstrates the influence of the choice of Stakeholders, the Level of Alignment and Forecast Accuracy on how demand is perceived in the form of Expected Demand. This also influences Information Delay and Time to Market. In the SW region in Fig. 10A it is shown how Customer Satisfaction is determined from Product Quality and StockOuts. The top left of the NE region in Fig. 10B shows how Cost, Revenue and Profit are calculated. Revenue is determined from Sales Quantity and the Unit Selling Price. Cost is made up of Variable Cost and Fixed Cost, whereby Variable Cost is calculated from Total Production and Repair Cost. The bottom right of NE shows the results from a simulation run of the SD model during which the Collaborative Supply Chain Performance Indicator together with the Output, Resource and Flexibility Measures are calculated according to the settings set by each of the constituents. In the SE region in Fig. 10B the calculation of

![](/api/attachments/NP8CDABS/fulltext/images/844a88fa879fe9e00de873a970a0aa3fd67fab97f91b2a6a3711cc26895ae0f6.jpg)  
Fig. 8. The SD modeling approach.

Fixed Cost is shown. Fixed Cost accumulates on a day-to-day basis and is affected by Level of Alignment, Choice of Stakeholders, Collaboration, Production Capacity and the use of Enabling Technology. On the right-hand side of SE the calculation of the Total Inventory is shown.

We then introduce the formulas and performance indicators defined in Section 2.7 into the SD model and quantify the initial parameters for the simulation run. We include two simulation runs that trace the behaviour of key variables over time. The results from these simulation runs pinpoint potential areas for improving the performance of the real collaborative supply chain.

Fig. 11 shows the behaviour over a period of time of key variables throughout the simulation run and its current CSCPI value. <sup>d</sup>Demand and Production<sup>T</sup> shows Customer Demand together with retailer and wholesaler orders and the resulting Production. Next to that, <sup>d</sup>Shipments and Sales<sup>T</sup> to customers are shown. The <sup>d</sup>Expected Demand<sup>T</sup> time graph allows assessment of the differences in the various stages of the collaborative supply chain. <sup>d</sup>Inventories<sup>T</sup> shows Manufacturer, Wholesaler and Retailer Inventory in comparison to the desired Manufacturer Inventory.

The graphs to the right of that show Time to Market and Customer Satisfaction. Under <sup>d</sup>Production Capacity<sup>T</sup> and <sup>d</sup>Capacity Utilization<sup>T</sup> the under-utilization of capacity is demonstrated, whereas the next graph shows the accumulation of <sup>d</sup>StockOuts<sup>T</sup> over time. The left-hand side of the table displays the input variables whose values are set during model calibration, and the shaded part tabulates the values of the output variables at the end of the simulation run. The last entry on the table shows the value of the CSCPI achieved during this run.

To determine a <sup>b</sup>best<sup>Q</sup> solution for all the stakeholders, we need to do a series of variable changes which are valid for the supply chain under investigation, and then perform simulation runs and compare the results. The weightings given to a, b or c for RM, OM and FM reflect the assumptions made by the stakeholders regarding their current priorities.

For example, let us consider a 20% increase in customer demand. To cope with this, the production capacity could be increased by increasing each manufacturer’s individual capacity or by adding another manufacturer, which is the change which we are going to consider in this exercise. The third manufacturer is set to produce at the same level as the existing manufacturers. We then perform a simulation run and see the result on performance as a result of the constituent changes.

![](/api/attachments/NP8CDABS/fulltext/images/4c72672f0b8987c4c09d130c53bf9aa19d7993bb6759525824d31ea0dbab0f64.jpg)  
Fig. 9. Sales, production starts and production to market time.

Fig. 12 shows the performance of the collaborative supply chain as a result of the above changes. With the production capacity increased by 50%, the supply chain is not stretched to the maximum capacity utilization. In turn, this enables the supply chain to cope with sudden fluctuations in demand without having to increase the percentage level of production per manufacturer. The consequence of this is an increase in supply chain flexibility. After <sup>b</sup>warming up<sup>Q</sup> the inventory levels are sustained consistently at a higher level than in the existing supply chain. The obvious trade-off between just-in-time manufacturing and warehousing calls for further analysis on the costs of keeping extra stock vs. the costs of lost sales and customer loyalty. The addition of a third manufacturer, despite of increasing fixed cost and inventory, results in increased number of sales, higher revenue and profit. This is a result of satisfying the increased customer demand. Consequently, the CSCPI increased by 35%. Adding a manufacturer is one alternative for coping with increased demand and increasing profit in this collaborative supply chain.

A  
![](/api/attachments/NP8CDABS/fulltext/images/417450c59927a293a9416ee633328e707d9ab1e7451c00e19285623b3c1653eb.jpg)  
Fig. 10. (A) A system dynamics model of the collaborative supply chain (NW, SW). (B) A system dynamics model of the collaborative supply chain (NE, SE).

![](/api/attachments/NP8CDABS/fulltext/images/96174f2a458f5478d34b317fa1e08a5656ec8e9fd22e22a9d72415d43176f9c4.jpg)  
Fig. 10 (continued).

Fig. 11. Results from the simulation run of the SD model of the existing CSC.

<table><tr><td>Demand and Production</td><td>Shipments &amp; Sales</td><td>Expected Demand</td></tr><tr><td>Inventories</td><td>Time To Market</td><td>Customer Satisfaction</td></tr><tr><td>Production Capacity</td><td>Capacity Utilisation</td><td>Stock Outs</td></tr></table>

<sub>rat</sub>i<sub>ve</sub> <sub>Supp</sub>l<sub>y</sub> C<sup>ha</sup>i<sup>n</sup> <sup>Perfor</sup>

<table><tr><td>USP (€)</td><td>LA (%)</td><td>FA (%)</td><td>PTMT chng (%)</td><td>PC (unit/da)</td><td>PQ (%)</td><td>avg CU (%)</td><td>avg TTM (da)</td><td>SO (unit)</td><td>avg PPU (€)</td><td>Sales (unit)</td><td>Profit (€)</td><td>CS</td><td>CSCPI</td></tr><tr><td>14.00</td><td>46.67</td><td>533 %.</td><td>0.00</td><td>4,200.00</td><td>90.00</td><td>96.17</td><td>134.96</td><td>135,267.26</td><td>2.69</td><td>1,448,833.74</td><td>3,896,568.48</td><td>9.87</td><td>3.24</td></tr></table>

<sub>rat</sub>i<sub>ve</sub> <sub>Supp</sub>l<sub>y</sub> C<sup>ha</sup>i<sup>n</sup> <sup>Perfor</sup>

<table><tr><td>Demand and Production</td><td>Shipments &amp; Sales</td><td>Expected Demand</td></tr><tr><td>Inventories</td><td>Time To Market</td><td>Customer Satisfaction</td></tr><tr><td>Production Capacity</td><td>Capacity Utilisation</td><td>StockOuts</td></tr></table>

<sub>New</sub> <sub>pe</sub>r<sup>formance</sup> <sup>indicator</sup> <sup>simulat</sup>

<table><tr><td>USP (€)</td><td>LA (%)</td><td>FA (%)</td><td>PTMT chng (%)</td><td>PC (unit/da)</td><td>PQ (%)</td><td>avg CU (%)</td><td>avg TTM (da)</td><td>SO (unit)</td><td>avg PPU (€)</td><td>Sales (unit)</td><td>Profit (€)</td><td>CS</td><td>CSCPI</td></tr><tr><td>14.00</td><td>46.67</td><td>8.78 %</td><td>0.00</td><td>6,300.00</td><td>90.00</td><td>79.66</td><td>134.96</td><td>153,002.37</td><td>3.94</td><td>1,747,918.63</td><td>6,888,733.26</td><td>9.72</td><td>4.37</td></tr></table>

To find the most realistic or at least the most acceptable solution for all stakeholders, we must perform several simulation runs and then choose the most appropriate solution for implementation according to the preferences of the stakeholders. The stakeholders may not be looking to adopt the solution with the highest CSCPI at any cost, but a solution which reflects as closely as possible their priorities. The DSE at its worst will pinpoint those areas where the actual supply chain performance can be improved and hence enable the stakeholders to make informed decisions, which are not based on guesswork, about managing the supply chain’s performance.

## 4. Concluding discussion

In the 1970s the Club of Rome ran simulations that <sup>b</sup>predicted<sup>Q</sup> that we would have already run out of resources by now and, of course, we have not. As a consequence, forecast simulations got a bad name. Economists worldwide use past performance and present indicators to predict economic growth, unemployment rate, GDP growth, etc. But then an unforeseen world event such as 9/11, whose consequences are not normally part of any such simulation run, causes chaos and makes our simulation forecasts behave erratically. A system dynamics based simulation will never be able to predict the future, but it may help to prepare for it.

Collaborative supply chains are complex, unique and continuously evolving systems, and what works well for one collaborative supply chain may contravene the stakeholders’ priorities in another. Furthermore, refining the collaborative supply chain for the purpose of improving it could be continued almost ad nauseam. It can be argued that the use of optimization and conditioning techniques may help to decide the best combination of changes in constituents and key parameters [37,52]. However, this form of automation may result in solutions that do not address adequately the priorities of the stakeholders. Hence, DSE should neither be viewed as generic nor as solution provider but rather as a decision testing and management support environment. In that respect, a high level of human input is required in order to calibrate the DSE whilst observing the priorities of the stakeholders and avoid ing refinements that contravene stakeholder priorities. Ultimately, the final decision rests neither with the DSE nor the modeler but with the stakeholders.

A company which engages in a CSC must realize that its individual efficiency and competitiveness depends heavily on strengthening its working relationship with their business partners [18], on improving the performance of the entire CSC, not just their own, and on innovating. In order to improve the working relationships between the stakeholders of the CSC and hence the entire CSC, the key factors and how they influence the performance of a CSC, in general, and their CSC, in particular, must be understood. This will enable stakeholders to pinpoint areas through which performance improvements must be made.

## References

[1] H.A. Akkermans, Renga: a systems approach to facilitating inter-organizational network development, System Dynamics Review 17 (3) (2001).

[2] H.A. Akkermans, P. Bogerd, B. Vos, Virtuous and vicious cycles on the road towards international supply chain management, International Journal of Operations and Production Management 19 (5/6) (1999).

[3] D.L. Anderson, H.L. Lee, Synchronised Supply Chains: The New Frontier, 1999.

[4] E.G. Anderson Jr., C.H. Fine, G.G. Parker, Upstream volatility in the supply chain: the machine tool industry as a case study, Production and Operations Management 9 (3) (2000).

[5] B.J. Angerhofer, M.C. Angelides, System Dynamics Modelling in Supply Chain Management: Research Review, in: J.A. Joines, R.R. Barton, K. Kang, P.A. Fishwick (Eds.), Winter Simulation Conference, (ACM/IEEE/SCSI, Orlando (FL), USA, 2000).

[6] APQC, Supply Chain Performance Metrics Survey, American Productivity and Quality Center, 2000.

[7] G. Baourakis, M. Stroe, The optimization of the distribution system in the context of supply chain management development, in: P.M. Pardalos, V.K. Tsitsiringos (Eds.), Financial Engineering, E-Commerce and Supply Chain, Kluwer, Dordrecht, 2002.

[8] Y. Barlas, A. Aksogan, Product Diversification and Quick Response Order Strategies in Supply Chain Management, International System Dynamics Conference, Cambridge, (MA), USA, 1996.

[9] B.M. Beamon, Supply chain design and analysis: models and methods, International Journal of Production Economics 55 (1998) 281–294.

[10] B.M. Beamon, Measuring supply chain performance, International Journal of Operations and Production Management 19 (3) (1999) 275–292.

[11] B.M. Beamon, V.C.P. Chen, Performance analysis of conjoined supply chains, International Journal of Production Research 39 (14) (2001) 3195–3218.

[12] P.D. Berger, A. Gerstenfeld, A.Z. Zeng, How many suppliers are best? A decision-analysis approach, Omega 32 (2004) 9–15.

[13] D. Berry, The Analysis, Modelling and Simulation of a Re-Engineering PC Supply Chain, PhD Thesis, University of Wales, Cardiff, 1994.

[14] D. Berry, G.N. Evans, R. Mason-Jones, D.R. Towill, The BPR SCOPE concept in leveraging improved supply chain performance, Business Process Management Journal 5 (3) (1999) 254–274.

[15] P. Checkland, Systems Thinking, Systems Practice, John Wiley & Sons, 1981.

[16] P. Childerhouse, J. Aitken, D.R. Towill, Analysis and design of focused demand chains, Journal of Operations Management 20 (6) (2002) 675–689.

[17] J. Dejonckheere, S.M. Disney, M.R. Lambrecht, D.R. Towill, Transfer function analysis of forecasting induced bullwhip in supply chains, International Journal of Production Economics 78 (2) (2002) 133–144.

[18] J. Dejonckheere, S.M. Disney, M.R. Lambrecht, D.R. Towill, The impact of information enrichment on the bullwhip effect in supply chains: a control engineering perspective, European Journal of Operational Research 152 (2004) 727–750.

[19] S.M. Disney, M.M. Naim, D.R. Towill, Dynamic simulation modelling for lean logistics, International Journal of Physical Dis tribution and Logistics Management 27 (3/4) (1997) 174–196.

[20] G. Elliott, S. Starkings, Business Information Systems: Systems, Theory and Practice, Longman, London, 1998.

[21] G.N. Evans, M.M. Naim, The Dynamics of Capacity Constrained Supply Chains, International System Dynamics Conference, Stirling, Scotland, 1994.

[22] G.N. Evans, M.M. Naim, D.R. Towill, Application of a simulation methodology to the redesign of a logistical control

system, International Journal of Production Economics 56–57 (1998) 157–168.

[23] J.W. Forrester, Industrial dynamics: a major breakthrough for decision makers, Harvard Business Review 36 (4) (1958) 37–66.

[24] S.C. Graves, K.A.H.G. Rinnooy, P.H. Zipkin, Logistics of production and inventory, in: G.L. Nemhauser, K.A.H.G. Rinnooy (Eds.), Handbooks in Operations Research and Management Science, Elsevier, Amsterdam, 1993.

[25] K. Hafeez, M. Griffiths, J. Griffiths, M.M. Naim, Systems design of a two-echelon steel industry supply chain, International Journal of Production Economics 45 (1996) 121–130.

[26] J. Hammant, S.M. Disney, P. Childerhouse, M.M. Naim, Modelling the consequences of a strategic supply chain initiative of an automotive aftermarket operation, International Journal of Physical Distribution and Logistics Management 29 (9) (1999) 535–550.

[27] A. Harrison, C. New, The role of coherent supply chain strategy and performance management in achieving competitive advantage: an international survey, Journal of the Operational Research Society 53 (2002) 263–271.

[28] R. Hieber, Collaborative performance measurement in logistics networks—the model, approach and assigned KPIs, Logistik Management 2 (2) (2002) 13–21.

[29] H.J. Johansson, P. McHugh, A.J. Pendlebury, W.A. Wheeler, Business Process Re-Engineering, John Wiley & Sons, Chichester, 1993.

[30] G.G. Kelley, A case study of an ERP implementation: promises, phantoms, and prugatory, in: T. Boone, R. Ganeshan (Eds.), New Directions in Supply-Chain Management: Technology, Strategy, and Implementation, AMACOM, New York, NY, 2002.

[31] U.H. K<sup>f</sup>nig, Simulating Multidimensional Supply Chains—a Vensim Based Model, Industrieseminar der Universit<sup>7</sup>t Mannheim, Mannheim, 1997.

[32] H.L. Lee, V. Padmanabhan, S. Whang, The bullwhip effect in supply chains, Sloan Management Review 38 (3) (1997) 93–102.

[33] J.C. Lewis, M.M. Naim, D.R. Towill, An integrated approach to re-engineering material and logistics control, International Journal of Physical Distribution and Logistics Management 27 (3/4) (1997) 197–209.

[34] R. Mason-Jones, D.R. Towill, Total cycle time compression and the agile supply chain—the integrated supply chain logistics, International Journal of Production Economics 62 (1) (1999) 61–73.

[35] A. Mavrommati, A. Migdalas, From logistics to collaborative logistics—a theoretical approach, in: P.M. Pardalos, V.K. Tsitsiringos (Eds.), Financial Engineering, E-Commerce and Supply Chain, Kluwer, Dordrecht, 2002.

[36] G.G. Parker, E.G. Anderson Jr., Supply chain integration: putting humpty dumpty back together again, in: T. Boone, R. Ganeshan (Eds.), New Directions in Supply-Chain Management: Technology, Strategy, and Implementation, AMACOM, New York, NY, 2002.

[37] C.C. Poirier, The Supply Chain Manager’s Problem-Solver, St. Lucie Press, Boca Raton, FL, 2003.

[38] M.E. Porter, Competitive Advantage: Creating and Sustaining Superior Performance, Free Press, New York, NY, 1985.

[39] G.P. Richardson, A.L. Pugh III, Introduction to System Dynamics Modeling, Productivity Press, Portland, OR, 1981.

[40] D.F. Ross, Competing Through Supply Chain Management: Creating Market-Winning Strategies Through Supply Chain Partnerships, Kluwer, Chicago, IL, 2000.

[41] R. Sankar, Inventory Management Across The Retail Supply Chain, Supply Chain Management Review, Winter 1998 (1998) 56–63.

[42] SCC, Supply-Chain Operations Reference-Model V5.0, Supply-Chain Council, 2001.

[43] D. Simchi-Levi, P. Kaminsky, E. Simchi-Levi, Designing and Managing the Supply Chain: Concepts, Strategies, and Case Studies, McGraw-Hill, Boston, MA, 2000.

[44] J.D. Sterman, Misperceptions of Feedback in Dynamic Decision Making, Organizational Behavior and Human Decision Processes 43 (1989) 301–335.

[45] J.D. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World, McGraw-Hill, Boston, MA, 2000.

[46] B.O. Szuprowicz, Supply Chain Management for E-Business Infrastructures, Computer Technology Research Corporation, Charleston, SC, 2000.

[47] D.R. Towill, Industrial dynamics modelling of supply chains, Logistics Information Management 9 (4) (1996) 43–56.

[48] D.R. Towill, Time compression and supply chain management—a guided tour, Supply Chain Management 1 (1996) 15–27.

[49] D.R. Towill, The seamless supply chain—the predator’s strategic advantage, International Journal of Transport Management Special Issue on Strategic Cost Management (1997) 37–56.

[50] D.R. Towill, M.M. Naim, Partnership sourcing helps smooth supply chain dynamics, Journal of the Institute of Purchasing and Supply Management (1993 (July–August)) 38–42.

[51] B. Vos, Redesigning international manufacturing and logistics structures, International Journal of Physical Distribution and Logistics Management 27 (7) (1997) 377–394.

[52] R.D.H. Warburton, S.M. Disney, D.R. Towill, J.P.E. Hodgson, Further insights into the stability of supply chains, International Journal of Production Research 42 (3) (2004) 639–648.

![](/api/attachments/NP8CDABS/fulltext/images/d110ede1370bee8a08d95c51deac4809e71cca5d4458e04a81e5da33587acf74.jpg)

Bernhard J. Angerhofer is a management consultant specializing in product development processes. He received his MSc in Information Systems Engineering from London South Bank University and his PhD in Information Systems and Computer Science from Brunel University. His interests include supply chain collaboration, business modeling and management information systems.

![](/api/attachments/NP8CDABS/fulltext/images/1b9908829fc87e6724bbf583a5ec3c4b3cfcda823720853dc5b8df7cc2711589.jpg)

Marios C. Angelides is Professor of Computing in the Department of Information Systems and Computing at Brunel University. He holds a BSc in Computing and a PhD in Information Systems both from the London School of Economics, where he begun his career as lecturer in information systems. He is a member the ACM, the IEEE Computer Society and the British Computer Society. For over 10 years, he has been researching multimedia

information systems on which he has published extensively in Information and Management, Decision Support Systems, Data and Knowledge Engineering, Multimedia Tools and Applications, Computers and Education. He guest edited for the Journal of Multimedia Tools and Applications, on which he is an editorial board member, and IEEE Multimedia.
