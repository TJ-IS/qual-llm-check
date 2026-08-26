---
otero_id: 12392
otero_key: "2Y9AHHK8"
title: "Improving inventory effectiveness in RFID-enabled global supply chain with Grey forecasting model"
authors: "S.-J. Wang; W.-L. Wang; C.-T. Huang; S.-C. Chen"
year: "2011"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2011.03.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving inventory effectiveness in RFID-enabled global supply chain with Grey forecasting model

S.-J. Wang ⇑, W.-L. Wang, C.-T. Huang, S.-C. Chen

Department of Industrial Engineering and Management, National Chin-Yi University of Technology, Taiping City, Taichung County 411, Taiwan, ROC

a r t i c l e i n f o

Article history: Received 15 May 2010 Received in revised form 21 March 2011 Accepted 22 March 2011 Available online 6 May 2011

Keywords: RFID Global supply chain Grey forecasting Simulation Multi-agents

## a b s t r a c t

A RFID-enabled global TFT–LCD supply chain associated with Grey forecasting model (GM) of Company A has been simulated and analyzed in this research. Three key performance indicates (KPI) including total inventory cost, inventory turnover and bullwhip effect are analyzed in the simulation experiments in order to compare the effectiveness of five different supply chain inventory models. The effectiveness of integrated system which is composed of supply chain operation, Grey short-term forecasting model and RFID system has been examined by aforementioned three KPIs. According to the result of Taguchi experiments, RFID-enabled R-SCI supply chain model which integrates the GM(1,1) forecasting model based on (s, Q) pull-based replenishment policy reduces 43.36% of the total inventory cost compared with that of the non-RFID SCI model. It apparently shows that a great improving effectiveness of supply chain inventory cost can be conducted while RFID system is incorporated with the GM(1,1) forecasting model.

\- 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

There has been fierce competition between companies under the trend of globalization of industries. Therefore, the problems of reducing the length of product lifecycle, tightening shipment date and quick delivery of products are faced by the industries. In order to achieve the ultimate value of integrated operations, industries are going to focus on the integration of supply chain. The interrelated networks of supply chain consist of manufacturers, suppliers, distributors, wholesalers, retailers and customers. The volume of demand forecasted by upstream suppliers is usually greater than the actual market demand, for the lack of transparent information and communication channel. The wrong decisions on inventory and produc tion are caused by the distorted information on purchasing products. Thus, the increased inventory cost in the upstream channels leads to the enlargement of the total cost of entire supply chain, which creates the bullwhip effect.

Lee et al. (1997) considers demand forecasting, lead time, price variation and batch orders as factors of bullwhip effect. He thinks one of the ways to weaken bullwhip effect is to avoid repeated demand forecasting. To lessen the problem of bullwhip effect, the sharing and exchanging of supply chain information is needed. For achieving this goal, one way is to utilize the Radio Frequency Identification System (RFID). With the real-time product visibility and traceability of RFID, the amount of on-hand inventory across supply chain tiers can be precisely calculated, and the lead time of product delivery can be shortened. Moreover, the impact which results from errors in demand forecasting can be reduced, and the effectiveness of supply chain management can thus increase. In order to cope with the instant RFID-enabled information sharing capabil ity, the Grey forecasting model can be appropriately adopted based on merely four pieces of short-term historical data.

Therefore, there is a great opportunity for integrating the real-time data retrieval capability of RFID with short-term forecasting merit of GM to achieve the quick response in the operation of supply chain.

The purpose of this research is to establish a simulation model of global supply chain, which integrates the Grey shortterm forecasting model and specific service level as basic pull-based inventory replenishment policy for the TFT–LCD Company A, to prove that the implementation of RFID system can best improve the inventory cost effectiveness.

The remainder of this paper is organized as follows: Section 2 provides a literature review on the RFID applications, supply chain simulation and Grey forecasting model. The global TFT–LCD RFID-enabled supply chain of Company A and simulation modeling is presented in Section 3. The Taguchi methods/design of experiments and verification by simulation are described in Section 4. In Section 5, the experiment results of simulation KPI output are analyzed and compared. The conclusion of this research is shown in Section 6.

## 2. Literature review

## 2.1. RFID applications in supply chain

Saygin et al. (2007) design methods for establishing a RFID-enabled nonlinear supply chain system and emphasize the communications infrastructure necessary to provide seamless data and information flow in order to achieve RFID databased decision-making at all levels of supply chain. By providing visibility, effective RFID implementation in a supply chain can bridge the gap between the shop floor and higher level operations. Mills-Harris et al. (2007) conducted a simulated study on the inventory management of time-sensitive materials, based on data collected by RFID. They provide three inventory models which rely on RFID data and design the trend-adjusted inventory forecast model in accordance with five estimating indicators. The result shows that a proper adjustment of the two smoothing parameters (a and b) can achieve the system performance demanded. Moreover, in January 2005, a successful trial of the RFID/EPC system on tagged pallets and cases was done by Wal-Mart and its top 100 suppliers. The University of Arkansas analyzes Wal-Mart’s success and finds that after adopting the RFID/EPC system, there’s a 16% decrease in the out-of-stock rate (MHM, 2005). Hardgrave et al. (2005) did research on 24 retailers of Wal-Mart, which are divided into two groups, and each group consists of 12 retailers. The result shows that the group which implements RFID has a 26% decrease in the out-of-stock rate and has improved by 63% compared to the group without RFID. Delen et al. (2007) analyze the RFID data collected from retailers and suppliers in supply chain and want to know how to estimate the time needed from the logis tics center to retailers through RFID. Lee et al. (2004) of the IBM prove the potential effectiveness of RFID in decreasing the inventory and enhancing the service level with simulation methods based on real data, and the model is a three-tier sup ply chain.

These studies above only involve parts of the supply chain tiers, but do not take the interrelation of the entire supply chain into account. Therefore, this research takes Company A’s global supply chain of TFT–LCD as an example, designs a simulation model to mimic the operation process of RFID-enabled global supply chain, and uses experimental design methods to prove the potential effectiveness of RFID in improving the supply chain inventory management.

Visich et al. (2009) conduct an investigation of actual benefits generated by RFID system on supply chain performance through empirical evidence. The research work of RFID in supply chain is divided into three areas: RFID overview, empirical studies and analytical studies. This study shows that automational effects of RFID on operational processes include reduced cost, improved shipping and receiving efficiency, improved inventory control, reduced inventory cost and reduced throughput time. One of the major automational effects is in the area of inventory control. Ngai et al. (2008) organize RFID research into four main categories: technological issues, applications areas, policy and security issues, and other issues. Supply chain management is one sub-category for RFID applications. They conclude that there has been relatively little work done on impacts on the sales and marketing.

Sarac et al. (2010) also conclude that potential benefits, inventory inaccuracy problems, the bullwhip effect and replenishment policies are the major research on the impact of RFID on supply chain management. Simulations study is one major reviewed methodology. Zelbst et al. (2010) construct a structural model to assess the impacts on the supply chain performance based on the utilization of RFID technology and supply chain information sharing. Kok and Shang (2007) develop an inspection adjusted base-stock (IABS) policy for inventory replenishment in the single-period problem to optimize the inventory cost. They indicate that the IABS heuristic can achieve a significant value of accurate inventory information provided by RFID systems.

The motivation of this research is stemmed from those above research findings. We mainly focus on the evaluation of impacts on the satisfaction of customer requirements and reduced total inventory cost in RFID-enabled supply chain. Therefore, this research has integrated the Grey short-term customer orders forecasting model with different pull-based replenishment policies within RFID-enabled supply chain and simulated its effectiveness on the total supply chain inventory cost.

## 2.2. RFID-enabled supply chain simulation

Kleijnen (2005) surveys four types of supply chain simulation: spreadsheet, system dynamics (SD), discrete-event dynamic system (DEDS), and business games. The survey concludes that the DEDS simulation is an important method in supply chain management (SCM). Borshchev and Filippov (2004) suggest that the system being modeled contains active objects (people, products, stocks, business units, etc.) with timing and event ordering and it is suitable to add agent-based model to DEDS simulation background. Mustafa et al. (2007) establish a four-tier supply chain. The supply chain is a dynamic system model which evaluates eight different scenarios by simulation. The performance evaluated is mainly based on inventory, the WIP level, backlogged orders, and customer satisfaction. Liang and Huang (2006) establish a multi-agent system in supply chain, and the inventory system is operated through different agents. With the genetic algorithm (GA) method, forecast of demand and orders through system thinking is provided by every tier. The result of the agent-based system shows reduction of total cost and the smoothing of orders variation curve.

Sari (2010) constructs a four-echelon supply chain simulation model to verify the impact of RFID technology on supply chain performance. He concludes that integrating RFID within supply chain provides greater benefits based on the intensive collaboration between the partners. Karagiannaki and Pramatari (2010) adopt a discrete event simulation approach to redesign a RFID-enabled supply chain process. They find that the object identification level and RFID labeling responsibility are identified as key decision factors. Sarac et al. (2008) simulate a RFID-enabled three-level supply chain to evaluate their economical impacts and to conduct ROI analyses. They find that the economical impacts of RFID on supply chain depend on the chosen technology, the tagging level and the product. Mehrjerdi (2009) applies computer simulation techniques for evaluating three large cases of RFID-enabled supply chain. He suggests that management must be committed to high level of performance including competitive lead times, reduced inventories, product quality, and reduced process so that the supply chain can successfully operate. Ustundag and Tanyas (2009) construct a simulation model to estimate the potential benefits of an integrated RFID system on a three-echelon supply chain. The study indicates that the lead time and demand uncertainty directly affect the performance of the integrated RFID supply chain in terms of cost factors at each tiers level. The simulation and evaluation of the impacts on RFID-enabled supply chain performance in terms of total inventory cost have been conducted with pull-based inventory replenishment policies and ARIMA long-term demand forecasting model (Wang et al., 2008, 2010).

Due to the interrelated trading and time-based business communication between partners within the supply chain, the traditional static management approaches have difficulty in solving the problems of the supply chain. Therefore, the alternative of system simulation is appropriately adopted. The dynamic system simulation method is used in this research for establishing a RFID-enabled supply chain model, which consists of agents for planning management, stock control and executive operation. Moreover, the RFID agent and the Grey forecasting agent are added in order to figure out the most appropriate replenishment policy and demand forecasting method for the RFID-enabled supply chain.

## 2.3. Grey forecasting model

The GM which is originally developed by Deng (1982) is applied in this research. Only four pieces of historical data are required in the Grey model. There is no strict hypothesis for the distribution of parent data. The main purpose of GM is to execute the short-term forecasting operation. The fundamental model of Grey prediction is the GM(1,1), a first-order differential model with only one input variable. The GM(1,1) model uses the most up-to-date data to predict future values. Chen et al. (2008) develop a GM(1,1) forecasting model to predict the future development for Chunghwa Telecom 3G market, associated with the solutions to market obstacles. They find that the Grey forecasting model is suitable for 3G market forecasting with only four-term historical data. Li et al. (2008) proposed a new prediction model which combines GM(1,1) model with time series ARIMA from statistics theory. A 3-points average model and Markov chain model are also applied in the research Wang and Hsu (2008) develop an improved method to forecast the output and trends of high technology industries in Taiwan. The Grey theory is combined with GA in the proposed model. The former is used to forecast the outputs of high tech nology industries and the latter is used to estimate the parameters of a forecasting model based on forecasting errors. They conclude that the proposed GA-based Grey model can be used to effectively reduce the errors in the forecasting process. Wu et al. (2006) indicate that the types of historical data are smoothing and nonlinear. Wu suggest a 4-points rolling GM(1,1|a) in the Verhulst model with several values of parameter a to reduce absolute forecasting errors. Chang et al. (2005) construct a rolling Grey forecasting model (RGM) to forecast Taiwan’s annual semiconductor production. They find that the yearly sur vey of anticipated industrial production growth rates in Taiwan and the yearly percent changes in real GDP by US manufacturing industry are highly correlated. A Grey–Markov chain forecasting model is proposed by Tien (2005). The deterministic Grey dynamic model DGDM(1,1,1) is combined with the Grey–Markov chain forecasting model to predict the time for which the deviation is over the limit of the tolerance. The result showed that high machining accuracy of forecasting can be achieved by the proposed DGDM(1,1,1). Hsu (2003) examines the precision of the Grey forecasting model applied to samples based on sales and demand in the global integrated circuit (IC) industry. The results indicate that the Grey model is better suited to the short-term predictions than to mid- and long-term predictions.

In conclusion, these studies all show that the Grey forecasting model can improve the degree of accuracy based on merely four pieces of historical data. Therefore, there is a great opportunity for integrating the real-time data retrieval capability of RFID with short-term forecasting merit of GM in the operation of supply chain. However, these studies do not take the integration of RFID and the factor of real-time information sharing into consideration. Hence, this research combines supply chain with the real-time and fast-responding character of RFID in expectation of enhancing the effectiveness of GM-based demand forecasting model.

## 3. Global TFT–LCD supply chain and simulation modeling

## 3.1. TFT–LCD industry in Taiwan

According to Materialsnet (2008), the Industry Economic Knowledge Center of the Industrial Technology Research Institute in Taiwan made a statistic showing that the total production value of flat display panel in Taiwan is 40.3 billion USD in the vear of 2007, which overtakes the 34 5 billion USD in South Korea and the 22 5 billion USD in Japan, This in fact makes Taiwan the biggest flat display manufacturer around world. DisplaySearch (2010) reported that the consolidated sales revenue in the TFT–LCD from the four major Taiwan panel makers reached NTD 91.767 billion, a 17.8% increase month by month and also an increase of 177.64% compared with the same period of 2009. The aggregate large-sized panel shipments in March 2010 were up by 15.2% to 22,723 million units. The architectures of the upstream, midstream, and downstream of the TFT–LCD industry are quite complex. The components manufactured in the upstream include crystal, glass substrate, color filter, driver IC, polarizer, and back light. They are fabricated in the midstream, and after that they can be applied in electronic appliance, consumer products, communication, transportation, computer, and business products.

## 3.1.1. Background of Company A

In Fig. 1, the global sites owned by Company A have eight branch warehouses, three regional distribution centers, five LCD monitor manufactories and four LCD panel manufactories. Its global inventory is computed every day, and the data is transmitted to the headquarters in Taiwan to be organized. Considerations are made on the basis of the inventory of each branch and the customer demand of each shipment location. Thus, the shipment decision on which manufactories or branch warehouses can be made accordingly. Company A collects the stock units and orders information of each tier in its information management center in order to integrate the information and centralize the distributions. Therefore, the replenishment demand is set depending on the allocated proportion. Under limitations of capacity, stock level distribution capability, and storage space, it seeks the optimal level of the throughput in each period, the distribution units, raw materials on-hand units, and times of purchasing.

![](/api/attachments/2Y9AHHK8/fulltext/images/68d0d9ead8cb0d408fdee52c5ad5220e2929a57079a9467126a825a4014fcbe0.jpg)  
Fig. 1. The architecture of global supply chain of Company A.

Currently, the life cycle of TFT–LCD has already positioned in the maturity stage. The market competition among the individual companies should be transferred to the level of the entire supply chain. However, most companies still handle the transactions of product data manually, which leads to inaccurate and old information across the upstream and downstream in the supply chain. Therefore, the actual TFT–LCD components inventory status in Company A still cannot be instantly transmitted to the upstream suppliers. The TFT–LCD products shipment status in the downstream distributors also cannot be timely sent to the Company A. As a result, the purchasing orders issued to the upstream suppliers have to be made according to the inaccurate and obsolete historical sales data. In order to deal with the customer unstable demand and batch production mode, there must be redundant inventory on hand.

Therefore, in order to solve the problem of inventory management in the supply chain, this research establishes a GM short-term demand forecasting model based on inventory replenishment policy with certain service level. The main goal is to upgrade the level of customer service and to reduce the amount of inventory generated by the capability of real-time data transmit in RFID system.

## 3.2. Global supply chain simulation modeling

## 3.2.1. Multi-agents simulation functions

This research adopts AnyLogic, a dynamic system simulation tool, to establish a mechanism of RFID-enabled supply chain simulation associated with a GM-based demand forecasting model. The simulation interface of the $R – S C I _ { G M }$ (RFID-enabled supply chain inventory demand forecasting model) established in this research is shown in Fig. 2. In this model, the mechanism of inventory replenishment simulation is operated through functions of agents to monitor the entire supply chain system and collect instant information with RFID. The agents can be sorted into three categories: planning, stock control, and executive operation. The planning agents can be sorted into two categories: supply chain planning and supply chain management. It publishes the inventory replenishment policies $( \mathbf { e . g . } , ( s , Q ) )$ , proportion of demand order, reorder point s and ordering goal of members in the five main tiers of the global supply chain system. The stock control agents play the role of communication and logical condition judgment for the information of demands, on-hand units and production units generated by each member of the supply chain system. It can be sorted into four categories: order management, stock units monitoring, production management and demand forecasting. The executive operation agents can be sorted into four cate gories: order check, purchased goods, production and finished goods. The agent of executive operation is the executor of the entire supply chain system. The multi-agents pull-based simulation flow chart for $R – S C I _ { G M }$ model is depicted in Fig. 3 and also is briefly described as follows:

![](/api/attachments/2Y9AHHK8/fulltext/images/de16701e4364fcc9910e867c72824df0edd652cd57afb52874a52392f12b9c1c.jpg)  
Fig. 2. The simulation main screen of $R – S C I _ { G M }$ model.

![](/api/attachments/2Y9AHHK8/fulltext/images/8b7e839b9d1a081ba93e55a0b39eb55dfc59067ad4b3a62f858f5c138e7cf880.jpg)  
Fig. 3. The pull-based multi-agents simulation flow chart for $R – S C I _ { G M }$ model.

– Once a number of units for customer weekly demand are generated by the system with Weibull distribution, the order check agent (OCA) will notify the demand forecasting agent (DFA) to process the calculation of forecasted demand based on GM(1,1) and then provide the number of forecasted units to the upper order management agent (OMA).

– The OMA then asks the finished goods agent (FGA) to release finished goods with required forecasted units. The outof-stock units of the finished goods will be recorded by the OMA and production management agent (PMA) notified by the stock units monitor agent (SUMA). The SUMA gets real-time transactions information regarding the finished goods on-hand units through the RFID agent (RFIDA) simultaneously.

– If the on-hand units are found to be smaller than the re-ordering points s, the requirements of replenishment Q is sent to the upper tier’s supplier in the supply chain by OMA. When the replenished raw materials arrive, the SUMA of each tier will receive the information of the gaining of on-hand units sent by the RFIDA and the purchased unit agent (PUA).

– When the PMA of the manufacturing plant tier receives the information of an out-of-stock in the finished goods stock, it will ask the production agent (PA) to start the production process. The units of finished goods will increase at the end of production process.

Table 1  
Input parameters of (R, s, S) and (R, S) replenishment policy for Company A.

<table><tr><td>Tier&#x27;s name</td><td>LCD panel manufactories</td><td>LCD monitor manufactories</td><td>Regional DCs</td><td>Branch warehouses</td><td>Retailers</td><td>Unit</td></tr><tr><td>D</td><td>14,763</td><td>11,694</td><td>19,286</td><td>7165</td><td>7094</td><td>piece/week</td></tr><tr><td>σ</td><td>76</td><td>60</td><td>100</td><td>37</td><td>37</td><td>piece/week</td></tr><tr><td>L</td><td>0.5</td><td>0.4</td><td>0.2</td><td>0.1</td><td>0.1</td><td>week</td></tr><tr><td>R</td><td>0.3</td><td>0.4</td><td>0.4</td><td>0.6</td><td>0.5</td><td>week</td></tr><tr><td>DL+R</td><td>11,811</td><td>9355</td><td>11,578</td><td>5015</td><td>4256</td><td>piece/week</td></tr><tr><td>σL+R</td><td>68</td><td>54</td><td>77</td><td>31</td><td>28</td><td>piece/week</td></tr><tr><td>SL</td><td>95%</td><td>95%</td><td>95%</td><td>95%</td><td>95%</td><td></td></tr><tr><td>ss</td><td>113</td><td>89</td><td>127</td><td>51</td><td>47</td><td>piece/week</td></tr><tr><td>s</td><td>11,923</td><td>9444</td><td>11,705</td><td>5066</td><td>4303</td><td>piece</td></tr><tr><td>Q</td><td>1955</td><td>1630</td><td>2423</td><td>1448</td><td>1187</td><td>piece</td></tr><tr><td>S</td><td>14,876</td><td>11,783</td><td>19,424</td><td>7216</td><td>7140</td><td>piece</td></tr></table>

## 3.2.2. Simulation input parameters

The case of Company A is a multi-tiers global supply chain model. The product for simulation is the 17-in. TFT–LCD of Company A. The simulation period T is set to be 52 weeks. The real historical demand in 52 weeks of the 17-in. TFT–LCD of Company A is collected as experimental database. A statistics distribution model analysis tool named Stat:Fit is adopted. The analytic result shows the customer demand statistics distribution of Company A approximates the Weibull (min = 6980 piece/week, $\alpha = 4 . 1 3 , \beta = 1 2 8 )$ . In this research, the inventory replenishment policies include the continuous review (s, Q), (s, S) and the periodic review $( R , s , S ) , ( R , S )$ , in reference to the formulas designed by Chopra and Meindl (2001) and Simchi-Levi et al. (2000), with the prerequisite of the desired cycle service level to be 95%. The periodic review policies of (R, s, S), (R, S) are calculated as follows and shown in Table 1:

$$
\begin{array}{l} D _ {L + R} = D \times (L + R) \\ \sigma_ {L + R} = \sqrt {L + R} \times \sigma \\ s s = Z (C S L) \times \sigma \times \sqrt {L + R} \\ s = D _ {L + R} + s s \\ S = M A X (D, D _ {L + R}) + Z (C S L) \times \sigma \times \sqrt {L + R} \\ Q = \sqrt {\frac {2 \times D \times P C}{C C}} \end{array}
$$

where D is the average weekly demand by each tier member; r the standard deviation of weekly demand; L the lead time for replenishment; R the cycle counting periods; $D _ { L + R }$ the average weekly demand during lead time plus cycle counting periods; $\sigma _ { L + R }$ the standard deviation of weekly demand during lead time plus cycle counting periods; ss the safety stock; s the reorder point; S the order-up-to-level; PC the purchasing cost (e.g., retailer = 27 \$/piece); CC the carrying cost (e.g., retailer = 0.272 \$/piece); Q is the quantity of replenishment (purchasing) order.

## 3.3. Derivation of Grey forecasting model

The market demand of high technology industries has seriously been affected by the weakening consumer capability since 2008. The long-term demand cannot be forecasted with the traditional static forecasting models. In particular, the Grey model requires only four pieces of historical data with which the Grey model can be constructed. Therefore, the Grey model is suitable for application in the current high technology industries. This research adopts the GM(1,1) to forecast mainly the end customer demand occurring at the most downstream as depicted in Fig. 1. The historical sales data provided by Company A have been manipulated as the fundamental database for GM(1,1) derivation. Meanwhile, the value of generation parameter a in GM(1,1) will be set as 0.01, 0.5, 0.7 and 0.99. The six steps for deriving the model of GM(1,1) is shown in Fig. 4 and also illustrated as follows:

Step 1: Collect the time series 52 weeks demand $x ^ { ( 0 ) }$ for Company A as follows:

$$
\begin{array}{l} x ^ {(0)} = (x ^ {(0)} (1), x ^ {(0)} (2), x ^ {(0)} (3), \ldots , x ^ {(0)} (n)) = (x ^ {(0)} (k); k = 1, 2, 3, \ldots , n); n \geqslant 4 \\ \quad = \left(x ^ {(0)} (1), x ^ {(0)} (2), x ^ {(0)} (3), \ldots , x ^ {(0)} (1 7), x ^ {(0)} (1 8), x ^ {(0)} (1 9), \ldots , x ^ {(0)} (5 0), x ^ {(0)} (5 1), x ^ {(0)} (5 2)\right) \\ \quad = (6 9 8 0, 7 1 3 8, 7 0 7 4, \ldots , 7 0 7 6, 7 1 4 5, 7 0 8 1, \ldots , 7 0 3 6, 7 1 1 3, 7 0 7 7) \end{array}\tag{1}
$$

![](/api/attachments/2Y9AHHK8/fulltext/images/e30d7d82c4f51f77ea694af28c06a379f586fb0e4a052606c3e8f92075bb0810.jpg)  
Fig. 4. The flow chart of Grey forecasting model.

Step 2: Generate $x ^ { ( 1 ) } ( K )$ time series data from the original data by using accumulated generating operation (AGO) technique as follows:

$$
\begin{array}{l} x ^ {(1)} (k) = \left(\sum_ {k = 1} ^ {1} x ^ {(0)} (k), \sum_ {k = 1} ^ {2} x ^ {(0)} (k), \dots , \sum_ {k = 1} ^ {n} x ^ {(0)} (k)\right) \\ = \left(\sum_ {k = 1} ^ {1} x ^ {(0)} (1), \sum_ {k = 1} ^ {2} x ^ {(0)} (2), \sum_ {k = 1} ^ {3} x ^ {(0)} (3), \dots , \sum_ {k = 1} ^ {5 0} x ^ {(0)} (5 0), \sum_ {k = 1} ^ {5 1} x ^ {(0)} (5 1), \sum_ {k = 1} ^ {5 2} x ^ {(0)} (5 2)\right) \\ = (6 9 8 0, 1 4 1 1 8, 2 1 1 9 2, \dots , 1 2 0 4 9 6, 1 2 7 6 4 1, 1 3 4 7 2 2, \dots , 3 5 4 6 7 6, 3 6 1 7 8 9, 3 6 8 8 6 6) \end{array}\tag{2}
$$

where the new series data $x ^ { ( 1 ) } ( K )$ is a monotone increasing sequence associated with an exponential function.

Step 3: Formulate the basic first-order differential equation of GM(1,1) as follows:

$$
\frac {d x ^ {(1)} (k)}{d k} + a x ^ {(1)} (k) = b\tag{3}
$$

where parameter a is a developing coefficient, and parameter b is a control variable named Grey input. Because the solution of GM(1,1) is to be an exponential curve, we can predict that the geographic diagram for the results of forecasting will be a smoothing curve. Thus, the Grey pseudo difference equation is derived through white process as follows:

$$
x ^ {(0)} (k) + a z ^ {(1)} (k) = b, \quad \forall k = 1, 2, 3, \dots , n,\tag{4}
$$

where the new series data $z ^ { ( 1 ) } ( K )$ can be partially generated from $x ^ { ( 1 ) } ( K )$ . It is an averaged generation while the parameter $\mathcal { X } = 0 . 5$

$$
\begin{array}{l} z ^ {(1)} (k) = \alpha x ^ {(1)} (k) + (1 - \alpha) x ^ {(1)} (k - 1), \quad k = 1, 2, 3, \ldots , n - 1 \\ \qquad = 0. 5 x ^ {(1)} (k) + 0. 5 x ^ {(1)} (k - 1), \quad k = 1, 2, 3, \ldots , n - 1 \\ z ^ {(1)} (2) = 0. 5 \times x ^ {(1)} (2) + 0. 5 \times x ^ {(1)} (1) = 1 0, 5 4 9 \\ z ^ {(1)} (3) = 0. 5 \times x ^ {(1)} (3) + 0. 5 \times x ^ {(1)} (2) = 1 7, 6 5 5 \\ z ^ {(1)} (4) = 0. 5 \times x ^ {(1)} (4) + 0. 5 \times x ^ {(1)} (3) = 2 4, 7 4 0 \\ \dots \end{array}\tag{5}
$$

$$
z ^ {(1)} (5 2) = 0. 5 \times x ^ {(1)} (5 2) + 0. 5 \times x ^ {(1)} (5 1) = 3 6 5, 3 2 7. 5
$$

Step 4: Construct the parameters matrix based on Eq. (4) as follows:

$$
\left[ \begin{array}{l} x ^ {(0)} (2) \\ x ^ {(0)} (3) \\ \dots \\ x ^ {(0)} (n) \end{array} \right] = \left[ \begin{array}{l l} - z ^ {(1)} (2) & 1 \\ - z ^ {(1)} (3) & 1 \\ \dots \\ - z ^ {(1)} (n) & 1 \end{array} \right] \quad \left[ \begin{array}{l} a \\ b \end{array} \right] \Rightarrow \left[ \begin{array}{l} 7 1 3 8 \\ 7 0 7 4 \\ c l d o t s \\ 7 0 7 7 \end{array} \right] = \left[ \begin{array}{l l} - 1 0, 5 4 9 & 1 \\ - 1 7, 6 5 5 & 1 \\ \dots \\ - 3 6 5, 3 2 7. 5 & 1 \end{array} \right] \quad \left[ \begin{array}{l} a \\ b \end{array} \right]
$$

This matrix is solved by the least square method and is denoted as:

$$
\left[ \begin{array}{c} a \\ b \end{array} \right] = (B ^ {T} B) ^ {- 1} B ^ {T} Y _ {n},\tag{6}
$$

where

$$
B = \left[ \begin{array}{c c} - z ^ {(1)} (2) & 1 \\ - z ^ {(1)} (3) & 1 \\ \dots \\ - z ^ {(1)} (n) & 1 \end{array} \right] Y _ {n} = \left[ \begin{array}{c} x ^ {(0)} (2) \\ x ^ {(0)} (3) \\ \dots \\ x ^ {(0)} (n) \end{array} \right]
$$

The second solution for Eq. (6) is generated by using the polynomial equation for deriving the intermediate parameters C, D, E, F from the following formulation. The detailed calculation process is described as follows:

$$
a = \frac {C D - (n - 1) E}{(n - 1) F - C ^ {2}} = 0. 0 0 0 0 1 9 7 1 2 5 0 3 4 4, \quad b = \frac {D F - C E}{(n - 1) F - C ^ {2}} = 7 0 9 9. 5 0 8 9 5 2
$$

where $\begin{array} { r } { C = \sum _ { k = 2 } ^ { n } z ^ { ( 1 ) } ( k ) = 9 , 5 8 5 , 6 1 9 , D = \sum _ { k = 2 } ^ { n } x ^ { ( 0 ) } ( k ) = 3 6 1 , 8 8 6 , } \end{array}$

$$
E = \sum_ {k = 2} ^ {n} z ^ {(1)} (k) x ^ {(0)} (k) = 6 8, 0 0 6, 7 0 2, 7 7 8, \quad F = \sum_ {k = 2} ^ {n} z ^ {(1)} (k) ^ {2} = 2, 3 5 8, 1 5 4, 1 6 6, 5 6 0
$$

Step 5: To solve the above differential equation Eq. (3), we use the discrete sequence whitening equation to generate the special solution of forecasting model:

$$
\hat {x} ^ {(1)} (k + 1) = \left[ x ^ {(0)} (1) - \frac {b}{a} \right] e ^ {- a k} + \frac {b}{a}, \quad \text { where } x ^ {(1)} (1) = x ^ {(0)} (1)
$$

Because the Grey forecasting model is formulated using the data of AGO rather than the original data, it is necessary to adopt inverse accumulated generating operation (IAGO) to recover the actual forecasting value. Therefore, the GM-based demand forecasting equation for TFT–LCD of Company A is denoted as:

$$
\begin{array}{r l} \hat {x} ^ {(0)} (k) & = \hat {x} ^ {(1)} (k) - \hat {x} ^ {(0)} (k - 1) = \left[ x ^ {(0)} (1) - \frac {b}{a} \right] (1 - e ^ {a}) e ^ {- a (k - 1)}, \quad k = 1, 2, 3, \dots , n \\ & = \left[ x ^ {(0)} (1) - \frac {7 0 9 9 . 5 0 8 9 5 2}{0 . 0 0 0 0 1 9 7 1 2 5 0 3 4 4} \right] (1 - e ^ {0. 0 0 0 0 1 9 7 1 2 5 0 3 4 4}) e ^ {- 0. 0 0 0 0 1 9 7 1 2 5 0 3 4 4 (k - 1)}. \end{array}
$$

The above equation has been embedded into the simulation module.

Step 6: The difference between the forecasted value and the original value can be compared based on the residual check ing process. The average residual r generated by the GM(1,1) model is 0.3963%, which is evaluated on the excellence level. Furthermore, we also use rolling check approach to evaluate the accuracy of the GM(1,1) model. The value of errors e(k + 1) generated by forecasting is calculated as follows:

$$
x _ {1} ^ {(0)} (4) \equiv (x ^ {(0)} (1), x ^ {(0)} (2), \dots , x ^ {(0)} (4)) = (6 9 8 0, 7 1 3 8, 7 0 7 4, 7 0 9 6)
$$

$$
\begin{array}{l} e (k + 1) = \frac {x ^ {(0)} (k + 1) - \hat {x} ^ {(0)} (k + 1)}{x ^ {(0)} (k + 1)} \times 100\%, \quad k + 1 \leqslant n \\ e (2) = \frac {7138 - 7123.7142}{7138} \times 100\% = 0.2001\% \\ e (3) = \frac {7074 - 7102.6406}{7074} \times 100\% = -0.4049\% \\ e (4) = \frac {7096 - 7081.6294}{7096} \times 100\% = 0.2025\% \end{array}
$$

The average error generated by rolling check method is calculated as:

$$
e = \frac {1}{n - 2} \sum_ {k = 4} ^ {n - 1} | e (k + 1) | \times 100 \% = \frac {1}{5 - 2} (| 0. 2 0 1 1 | + | - 0. 4 0 4 9 | + | 0. 2 0 2 5 |) = 0. 2 6 9 2 \%
$$

Finally, the average accuracy e is derived as:

$$
\varepsilon = (1 - e) \times 100 \% = (1 - 0.2692) \times 100 \% = 99.73 \%
$$

## 3.4. The key performance indicators in supply chain model

This research considers the total inventory cost, the inventory turnover rate and the bullwhip effect as key performance indicators. The subjects for simulation are the five tiers in the supply chain of Company A, and the length for simulation run is 52 weeks. The KPI equation is as follows:

– Total inventory cost = production cost + inventory replenishment cost + backorder cost + delivery cost

$$
\begin{array}{l} T I C = \sum_ {n = 1} ^ {N} \sum_ {t = 1} ^ {T} \left\{R S Q _ {n t} \left(R C _ {n} + R S C _ {n}\right) + M C _ {n} \times P W M Q _ {n t} + \left(P W Q _ {n t} + I E S Q _ {n t}\right) S g C _ {n} \right\} + \sum_ {n = 1} ^ {N} \sum_ {t = 1} ^ {T} \left(U R C _ {n} \times O M R Q _ {n t} + W A C _ {n} \times E S Q _ {n t}\right) + \sum_ {n = 1} ^ {N} \sum_ {t = 1} ^ {T} \left(U O C _ {n} \times E S O Q _ {n t}\right) + \sum_ {n = 1} ^ {N} \sum_ {t = 1} ^ {T} \left(U T C _ {n} \times S M Q _ {n t}\right) \end{array}\tag{7}
$$

where N = 5, and $T = 5 2$

– Inventory turnover rate = sales amount  inventory cost

$$
I T R = \frac {\sum_ {n = 1} ^ {N} \sum_ {t = 1} ^ {T} S g C _ {n} \times D _ {n t}}{\sum_ {n = 1} ^ {N} \sum_ {t = 1} ^ {T} P W M Q _ {n t} \times M C _ {n} + R S Q _ {n t} \times R C _ {n} + E S E Q _ {n t} \times E C _ {n}}\tag{8}
$$

– Bullwhip effect by Simchi-Levi et al. (2000):

$$
B E = \frac {\operatorname{Var} (Q ^ {N})}{\operatorname{Var} (D)},\tag{9}
$$

where $V a r ( Q ^ { N } )$ represents the deviation of demand orders issued by the N tier in the supply chain. Var(D) represents the deviation of end customer demand.

The following notations are used in the global supply chain simulation model.

N = the set of members in each tier of the supply chain.

$P W Q _ { n t } =$ the throughput units of manufacturer n in period t.

$I E S Q _ { n t }$ = the issued units of finished goods of manufacturer n in period t.

$S g C _ { n } =$ the unit sale price of finished goods produced by manufacturer n.

$R S Q _ { n t }$ = the raw materials on-hand units of manufacturer n in period t.

$R C _ { n } =$ the raw materials unit cost of manufacturer n.

$R S C _ { n } =$ = the raw materials carrying cost per unit of manufacturer n.

PWMQ = the work-in-process units of manufacturer n in period t.

$M C _ { n } =$ the work-in-process cost per unit of manufacturer n.

$W A C _ { n }$ = the issuing activity unit cost of manufacturer n.

$O M R Q _ { n t }$ = the raw materials purchased units of manufacturer n in period t.

$U R C _ { n } =$ the raw materials purchasing unit cost of manufacturer n.

$E S O Q _ { n t }$ = the backorder units of manufacturer n in period t.

$U O C _ { n }$ = the backorder unit cost of the finished goods of manufacturer n.

$S M Q _ { n t }$ = the scheduled shipping units of manufacturer n in period t.

$U T C _ { n }$ = the shipping cost per unit of manufacturer n.

$\boldsymbol { E S E Q _ { n t } = }$ the amount of finished goods of manufacturer n in period t.

$E C _ { n }$ = the finished goods unit cost of manufacturer n.

$D _ { n t } =$ the demand units of manufacturer n in period t.

## 4. Factorial experiments in RFID-enabled supply chain simulation

## 4.1. Simulation model infrastructure

This research is focused on the simulation of the global TFT–LCD supply chain operation embedded with RFID systems in Company A. Because of the huge transactions for transmitting tagged EPC products data by real-time RFID systems, it is impossible to establish a real RFID-enabled supply chain for study. Therefore, the RFID-enabled supply chain infrastructure is mimicked and simulated based on the conceptual network structure shown in Fig. 5. The receiving and shipping point of each tier is equipped with RFID system, including one reader and two antennas. When products are loaded into trucks and transported to downstream warehouses, the antenna of the RFID system read the EPC tags affixed on the cases, retrieve the embedded information, and transform the data to the readers. The tagged EPC data of each product, affiliated with RFID tagged records like the receiving time and shipping time, are immediately transmitted to the reader. Through the Internet connection, transactions of stocks can be monitored at any time.

![](/api/attachments/2Y9AHHK8/fulltext/images/49f0b665facd879adede84cf980487169bbccee57e059299f6c9fa3deeebf19b.jpg)  
Fig. 5. The conceptual network structure of RFID-enable supply chain

The RFID mechanism in the global supply chain simulation model of Company A established by Anylogic will be gradually simulated with reference to the conceptual network structure.

## 4.2. RFID system implementation cost

The capital investment of RFID equipments installed in the supply chain should be included in the cost of supply chain operations. In this research, RFID equipments, including two antennas and a reader, are set in the receiving and shipment location of each supply chain tier. The commercial price of each antenna (M/A-COM MAANAT0123) is about \$290, and the commercial price of each reader (ThingMagic Mercury 5) is about \$995. The proposed life cycle of RFID is 5 years, the salvage value is 10%, the simulation time is 1 year, the maintenance expense of RFID is 12%, and the operation cost is 15%. The RFID equipment cost of each supply chain tier is $2 \times 5 2 9 0 + 1 \times 5 9 9 5 = { \ S } 1 5 7 5 , { \mathrm { t h e ~ } } { \mathrm { s a l v a g e } } = { \ S } 1 5 7 5 \times 1 0 { \% } = { \ S } 1 5 7 . 5 ,$ the maintenance cos $\tau = \mathfrak { S } 1 5 7 5 \times 1 2 \% = \mathfrak { S } 1 8 9$ , the operation ${ \mathrm { c o s t } } = \ S 1 5 7 5 \times 1 5 \% = \ S 2 3 6 . 2 5$ , and the depreciation cost = \$ $( 1 5 7 5 - 1 5 7 . 5 ) \times [ ( 5 - 1 + 1 ) / ( 1 + 2 + 3 + 4 + 5 ) ] = 8 4 7 2 . 5$ . Thus, the total cost of 1-year simulation for a set of RFID equipments = the maintenance cost + the operation cost + the depreciation $\mathrm { c o s t } = \ S 1 8 9 + \ S 2 3 6 . 2 5 + \ S 4 7 2 . 5 = \ S 8 9 7 . 7 5$ . The commercial cost of one RFID tag (Alien EPC Gen 2) is about \$1, and the average simulated throughput in 1 year of LCD panel factories is 2952,116. The attached tags are for entire usage of the supply chain, so the cost of RFID tags is about 2952,116 - \$1 = \$2952,116. The individual RFID cost of each tier is: LCD panel manufacto-$\mathrm { r i e s } = \ S 8 9 7 . 7 5 \times 4 \times 1 + \ S 2 9 5 2 , 1 1 6 = \ S 2 9 5 5 , 7 0 7$ , LCD monitor manufactories = \$897.75 - 5 - 2 = \$8977.5, regional distribution $\mathrm { c e n t e r s } = { \ S } { 8 9 7 . 7 5 } \times 3 \times 2 = { \ S } { 5 3 8 6 . 5 } ,$ , branch ${ \mathrm { w a r e h o u s e s } } = \ S 8 9 7 . 7 5 \times 8 \times 2 = \ S 1 4 { , } 3 6 4 ,$ and $\mathrm { r e t a i l e r s } = \$ 89 7.75 \times$ $8 \times 2 = \$ 14,364$

## 4.3. Taguchi experiments for simulation

This research adopts the Taguchi method to carry out simulation experiments. The Taguchi method can acquire information effectively with fewer combinations of experiments. There are three phases in the Taguchi Method: planning, implementation, analysis and confirmation of the output.

## 4.3.1. Experimental planning phase

In the case of Company A, due to the impact of replenishment policies, demand forecasting methods and the non-immediacy of information, there is an increase in the total inventory cost. Therefore, this research intends to decrease the total inventory cost by implementing appropriate demand forecasting methods and replenishment policies under the RFID environment. The quality characteristic of the global supply chain model of Company A is the total inventory cost. Its characteristic is the smaller-the-better, meaning that the cost should be smaller. The definition of the smaller-the-better signal-tonoise (SN) ratio is as follows:

$$
S N = - 1 0 \times \log_ {1 0} (M S D) = - 1 0 \times \log_ {1 0} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i} ^ {2}\right)
$$

where MSD is the mean square deviation, $y _ { i }$ is the output value.

This research focuses on replenishment policies, demand forecasting methods and the variation of total inventory cost. The impact of noise is not taken into consideration. The control factors and their levels are listed in Table 2. There are two level-4 factors and one level-2 factor, which is a $L _ { 1 6 } ( 4 ) ^ { 3 }$ combination generated by Minitab

## 4.3.2. Experiments implementation phase

The 16 combinations determined by the Minitab are experimented and replicated for 40 times, and the total simulation experiment runs are $1 6 \times 4 0 = 6 4 0$ times. The partial experiments output data are shown in Table 3.

## 4.3.3. Experiments output analysis and confirmation

The first step for data analysis is to transform the observed values of each experiment combination into the SN ratio. The result is shown in the last column of Table 3, and the total average of the 16 SN ratios is:

Table 2  
Control factors and levels in Taguchi simulation experiments.

<table><tr><td rowspan="2">Factors</td><td colspan="4">Levels</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>A. Replenishment policy</td><td>(s, Q)</td><td>(s, S)</td><td>(R, s, S)</td><td>(R, S)</td></tr><tr><td>B. Grey forecasting</td><td>α = 0.01</td><td>α = 0.5</td><td>α = 0.7</td><td>α = 0.99</td></tr><tr><td>C. RFID</td><td>Yes</td><td>None</td><td></td><td></td></tr></table>

Table 3  
Partial experiments output data.

<table><tr><td rowspan="2">#</td><td colspan="3">Control factors</td><td colspan="5">Observation values (total inventory cost)</td></tr><tr><td>A</td><td>B</td><td>C</td><td>1</td><td>2</td><td>...</td><td>40</td><td>SN</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>721,749,803</td><td>721,643,635</td><td>...</td><td>725,190,761</td><td> $\eta_1 = -177.185$ </td></tr><tr><td>2</td><td>1</td><td>2</td><td>2</td><td>1,184,110,620</td><td>1,176,051,312</td><td>...</td><td>1,193,296,640</td><td> $\eta_2 = -186.837$ </td></tr><tr><td>3</td><td>1</td><td>3</td><td>3</td><td>554,773,075</td><td>564,598,676</td><td>...</td><td>524,869,552</td><td> $\eta_3 = -174.714$ </td></tr><tr><td>4</td><td>1</td><td>4</td><td>4</td><td>1,272,557,106</td><td>1,267,463,267</td><td>...</td><td>1,292,377,062</td><td> $\eta_4 = -182.183$ </td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>15</td><td>4</td><td>3</td><td>2</td><td>1,761,556,854</td><td>1,741,001,403</td><td>...</td><td>1,804,279,657</td><td> $\eta_{15} = -191.055$ </td></tr><tr><td>16</td><td>4</td><td>4</td><td>1</td><td>918,767,722</td><td>986,621,533</td><td>...</td><td>978,046,115</td><td> $\eta_{16} = -184.081$ </td></tr></table>

$$
\overline {{{T}}} = \frac {1}{1 6} \sum_ {i = 1} ^ {1 6} \eta_ {i} = \frac {1}{1 6} (- 1 7 7. 8 5 - 1 8 6. 8 3 7 - \dots - 1 9 1. 0 5 5 - 1 8 4. 0 8 1) = - 1 8 4. 0 4 6 4
$$

The average SN ratio of level-1 factor A is $\overline { { A } } _ { 1 } = - 1 8 0 . 2 ;$ the average SN ratio of level-3 factor B is $\overline { { B } } _ { 3 } = - 1 8 3 . 6 ;$ the average SN ratio of level-3 factor Cis $\overline { { { C } } } _ { 3 } = - 1 7 8 . 6 ,$ and the others likewise. The main purpose of carrying out the matrix experiment is to determine the optimal level of each factor. According to the definition of the SN ratio, the larger the SN ratio is, the better the quality is. Therefore, the optimal level combination of this research is determined as $A _ { 1 } B _ { 3 } C _ { 3 } .$ Using the factor main effects graphs to subjectively judge the significance of each factor, we find that factor A and C are significance factors, and factor B is not a significant factor and is to be merged as errors. Moreover, the SN ratio under the optimal conditions is calculated as follows:

$$
\widehat {S N} = \overline {{T}} + (\overline {{A}} _ {1} - \overline {{T}}) + (\overline {{C}} _ {3} - \overline {{T}}) = \overline {{A}} _ {1} + \overline {{C}} _ {3} - \overline {{T}} = - 1 8 0. 2 + (- 1 7 8. 6) - (- 1 8 4. 0 4 6 4) = - 1 7 4. 7 5 3 6
$$

The main purpose of carrying out the experiment confirmation is to verify the correction of the conclusion generated by the analysis of data. In order to effectively estimate the observed values, the confidence interval (CI) must be calculated. The confirmation of the expected average value of experiments is:

$$
C I = \sqrt {F _ {\alpha ; 1 , \nu_ {2}} \times V _ {e} \times \left(\frac {1}{n _ {\text {eff}}} + \frac {1}{r}\right)} = \sqrt {5 . 1 2 \times 4 . 2 1 0 1 \times \left(\frac {7}{1 6} + \frac {1}{5}\right)} = 3. 7 0 7
$$

It can be concluded with 95% confidence in this research that the boundary of the expected SN ratio is $- 1 7 4 . 7 5 3 6 \pm 3 . 7 0 7 .$ The average SN ratio generated by the five $A _ { 1 } B _ { 3 } C _ { 3 }$ experiments is 174.9472, which falls in the confidence interval above. This means that the selected factor A and C and their levels are adequate. Finally, the optimal Company A’s global supply chain system simulation specification is to implement the (s, Q) replenishment policy and GM(1,1) with $\mathcal { X } = 0 . 7$ forecasting method associated with the RFID-enabled system. It is called the $R – S C I _ { G M }$ (RFID-enabled Supply Chain Inventory Demand Forecasting: GM).

## 5. Simulation output analysis

## 5.1. The compared global supply chain models

Besides the four replenishment policies: $( s , Q ) , ( s , S ) , ( R , S ) , ( R , s , S )$ , the global supply chain of Company A also adopts demand forecasting methods. From the result of the Taguchi experiment, it is known that the $( s , Q )$ replenishment policy is the optimal. Therefore, this research intends to verify if the $R – S C I _ { G M }$ model is the optimal model among five global supply chain inventory management models.

## 5.1.1. Supply chain inventory (SCI)

This model represents the current manufacturing environment and simulates the current inventory operation of Company A. The current operation implements the (s, Q) replenishment policy and checks the weekly inventory level of supply chain tier’s member to update the purchasing orders to the baseline Q units (Wang et al., 2008).

## 5.1.2. RFID-enabled supply chain inventory (RFID-SCI)

This model supposes each inventory item is recorded on RFID tag, and its visibility is 100%. The fixed baseline is similar to that of the SCI model, and RFID is only for the purpose of monitoring rather than modifying the inventory level (Wang et al., 2008).

## 5.1.3. RFID-enabled supply chain inventory demand forecasting: ARIMA $( R - S C I _ { A R I M A } )$

This model improves demand management with the real-time function of RFID in addition to using ARIMA long-term forecasting method. Customer demand can be forecasted and information of demand can be retrieved at any time based on the RFID-enabled supply chain (Wang et al., 2010).

## 5.1.4. Supply chain inventory demand forecasting: $G M ( 1 , 1 ) \left( S C I _ { G M } \right)$

This model implements the (s, Q) pull-based replenishment policy and the Grey short-term forecasting method. It adopts GM to forecast the future demand in order to reduce the inventory cost by decreasing variation of customer orders.

## 5.1.5. RFID-enabled supply chain inventory demand forecasting: GM(1,1) (R-SCI<sub>GM</sub>)

This model improves demand management with the real-time capability of RFID in addition to using GM forecasting method. Customer demand can be forecasted and information of demand can be retrieved at any time based on the RFIDenabled supply chain. However, the time of simulation process is very short, and the RFID tagged data that can be retrieved is quite large. The virtual method is adopted in the simulation model.

## 5.2. Significance test

In order to test the differences between $R – S C I _ { G M }$ and $S C I _ { G M } ,$ the fitness of their total inventory costs and inventory turnover rates to normal distribution will be tested before the Bernoulli experiment is carried out. As the result of the analysis of the normal distribution graph with Minitab, the total inventory costs and inventory turnover rates of $R – S C I _ { G M }$ and $S C I _ { G M }$ fall in the 95% confidence interval, which is fit to the normal distribution. The Bernoulli experiment is carried out in order to test the difference between the average total inventory costs of $R – S C I _ { G M }$ and $S C I _ { G M } ,$ and the statistic is as follows:

$$
\begin{array}{l} \sigma_ {\bar {x} _ {1} - \bar {x} _ {2}} = \sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}} = \sqrt {\frac {(1 3 8 5 6 9 8 3 . 8) ^ {2}}{4 0} + \frac {(1 1 2 4 7 0 8 8 . 5 1) ^ {2}}{4 0}} = 2 8 2 1 8 4 7. 7 7 9 \\ Z = \frac {(\bar {x} _ {1} - \bar {x} _ {2}) - (\mu_ {1} - \mu_ {2})}{\sigma_ {\bar {x} _ {1} - \bar {x} _ {2}}} = \frac {(5 4 5 , 3 6 7 , 3 0 6 - 9 6 2 , 0 9 4 , 2 8 6) - 0}{2 8 2 1 8 4 7 . 7 7 9} = - 1 4 7. 6 7 8 8 \end{array}
$$

Under the 95% confidence level $( \alpha = 0 . 0 5 ) , Z = - 1 4 7 . 6 7 8 8$ , which is less than $Z ( \alpha = 0 . 0 5 ) = - 1 . 9 6$ and falls in the reject area. Therefore, we accept the alternative hypothesis H : there are differences between the total inventory costs of the two groups. Moreover, the Bernoulli experiment is also carried out in order to test the difference between the average inventory turnover rates of $R – S C I _ { G M }$ and $S C I _ { G M } ,$ and the test statistics is as follows:

$$
\begin{array}{l} \sigma_ {\bar {x} _ {1} - \bar {x} _ {2}} = \sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}} = \sqrt {\frac {(0 . 0 4 6 3 8) ^ {2}}{4 0} + \frac {(0 . 0 0 8 2 4) ^ {2}}{4 0}} = 0. 0 0 7 4 4 8 \\ Z = \frac {(\bar {x} _ {1} - \bar {x} _ {2}) - (\mu_ {1} - \mu_ {2})}{\sigma_ {\bar {x} _ {1} - \bar {x} _ {2}}} = \frac {(0 . 9 9 9 1 8 3 8 0 7 - 0 . 4 8 7 7 4 4 0 3) - 0}{0 . 0 0 7 4 4 8} = 6 8. 6 6 7 9 \end{array}
$$

$Z = 6 8 . 6 6 7 9 ,$ which is larger than 1.96 and falls in the reject area, so we does not accept the null hypothesis $\operatorname { H } _ { 0 } { \mathrm { : } }$ no difference exists in the average inventory turnover rate of the two models. In conclusion, under a 95% confidence level, there are differences between the inventory turnover rates of the two models.

## 5.3. The comparison of KPIs

## 5.3.1. The total inventory cost

From the simulation outputs shown in Table 4, based on the experiment output of $R – S C I _ { G M } ,$ it can be known that the $R – S C I _ { G M }$ is the best of the five models. It has the lowest production cost, replenishment cost, backorder cost, delivery cost and total inventory cost. We can find that compared to the $S C I _ { G M }$ or the $R – S C I _ { A R I M A }$ model, the $R – S C I _ { G M }$ model has a $4 3 . 3 2 \% = ( 5 4 5 , 3 6 7 , 5 9 0 - 9 6 2 , 9 0 3 , 7 9 9 ) / 9 6 2 , 9 0 3 , 7 9 9$ decrease and a ${ } 8 . 5 6 \% = ( 5 4 5 , 3 6 7 , 5 9 0 - 5 9 6 , 4 4 3 , 5 5 5 ) / 5 9 6 , 4 4 3 , 5 5 5$ decrease, respectively in the total inventory cost.

The simulation results of five models

<table><tr><td>Model name</td><td>Production cost</td><td>Replenishment cost</td><td>Backorder cost</td><td>Delivery cost</td><td>Total inventory cost</td></tr><tr><td> $R-SCI_{GM}$ </td><td>542,277,655</td><td>16,595</td><td>837</td><td>3,072,503</td><td>545,367,590</td></tr><tr><td> $SCI_{GM}$ </td><td>958,976,477</td><td>16,750</td><td>935</td><td>3,909,637</td><td>962,903,799</td></tr><tr><td> $R-SCI_{ARIMA}$ </td><td>593,077,452</td><td>18,052</td><td>1045</td><td>3,347,006</td><td>596,443,555</td></tr><tr><td>R-SCI</td><td>675,954,816</td><td>18,003</td><td>1057</td><td>3,336,281</td><td>679,310,157</td></tr><tr><td>SCI</td><td>1,091,657,485</td><td>18,886</td><td>1375</td><td>3,507,069</td><td>1,095,184,815</td></tr></table>

Table 5  
The summarized $R – S C I _ { G M }$ vs. $S C I _ { G M }$ improved costs by tier’s member.

<table><tr><td>Cost items</td><td>LCD panel manufactories (%)</td><td>LCD monitor manufactories (%)</td><td>Regional DCs (%)</td><td>Branch warehouses (%)</td><td>Retailers (%)</td></tr><tr><td>Production</td><td>-52.11</td><td>-51.01</td><td>-40.26</td><td>-52.47</td><td>-35.77</td></tr><tr><td>Replenishment</td><td>-0.68</td><td>-0.97</td><td>-0.96</td><td>-0.85</td><td>-1.13</td></tr><tr><td>Delivery</td><td>-0.49</td><td>-0.81</td><td>-0.94</td><td>-0.65</td><td>-1.08</td></tr><tr><td>Backorder</td><td>-0.69</td><td>-8.18</td><td>-7.34</td><td>-9.34</td><td>-25.58</td></tr></table>

Table 6  
The summarized $R – S C I _ { G M }$ vs. $R – S C I _ { A R I M A }$ improved costs by tier’s member.

<table><tr><td>Cost items</td><td>LCD panel manufactories (%)</td><td>LCD monitor manufactories (%)</td><td>Regional DCs (%)</td><td>Branch warehouses (%)</td><td>Retailers (%)</td></tr><tr><td>Production</td><td>-20.68</td><td>-4.56</td><td>21.23</td><td>55.42</td><td>-24.04</td></tr><tr><td>Replenishment</td><td>-8.58</td><td>-8.46</td><td>-7.79</td><td>-9.55</td><td>-6.28</td></tr><tr><td>Delivery</td><td>-8.87</td><td>-8.49</td><td>-7.90</td><td>-11.25</td><td>-6.53</td></tr><tr><td>Backorder</td><td>-7.19</td><td>-3.05</td><td>-61.39</td><td>11.19</td><td>-30.56</td></tr></table>

Table 7  
The improved inventory turnover rate of each tier by $R – S C I _ { G M }$ vs. $S C I _ { G M }$

<table><tr><td></td><td>LCD panel manufactories</td><td>LCD monitor manufactories</td><td>Regional DC</td><td>Branch warehouses</td><td>Retailers</td></tr><tr><td> $R-SCI_{GM} (1)$ </td><td>0.9789</td><td>1.0072</td><td>0.6651</td><td>1.8880</td><td>0.4557</td></tr><tr><td> $SCI_{GM} (2)$ </td><td>0.4696</td><td>0.4930</td><td>0.3979</td><td>0.8856</td><td>0.1974</td></tr><tr><td>Improved rate (1)-(2) (%)</td><td>50.93</td><td>51.42</td><td>26.72</td><td>100.24</td><td>25.83</td></tr></table>

## Table 8

The comparison of bullwhip effect by $R – S C I _ { G M }$ vs. $S C I _ { G M }$ and $R – S C I _ { A R I M A } .$

<table><tr><td></td><td>End customer</td><td>Retailers</td><td>Branch warehouses</td><td>Regional DC</td><td>LCD monitor manufactories</td><td>LCD panel manufactories</td></tr><tr><td colspan="7"> $R-SCI_{GM}(1)$ </td></tr><tr><td> $Var(Q^{k})\times 10^{3}$ </td><td>19,343</td><td>179,871</td><td>13,305</td><td>42,472</td><td>83,791</td><td>648,643</td></tr><tr><td>BW a</td><td>1</td><td>9.30</td><td>1.21</td><td>2.20</td><td>4.33</td><td>33.53</td></tr><tr><td colspan="7"> $SCI_{GM}(2)$ </td></tr><tr><td> $Var(Q^{k})\times 10^{3}$ </td><td>18,408</td><td>252,049</td><td>37,040</td><td>60,505</td><td>230,427</td><td>1,032,714</td></tr><tr><td>BW b</td><td>1</td><td>13.69</td><td>2.01</td><td>3.29</td><td>12.52</td><td>56.10</td></tr><tr><td colspan="7"> $R-SCI_{ARIMA}(3)$ </td></tr><tr><td> $Var(Q^{k})\times 10^{3}$ </td><td>26,869</td><td>300,147</td><td>33,121</td><td>62,146</td><td>121,854</td><td>904,600</td></tr><tr><td>BW c</td><td>1</td><td>11.17</td><td>1.23</td><td>2.31</td><td>4.54</td><td>33.67</td></tr><tr><td>(1) vs. (2) = [(b-a)/b]*100</td><td>32.86</td><td>-19.03</td><td>33.20</td><td>65.39</td><td>40.23</td><td></td></tr><tr><td>(1) vs.(3) = [(c-a)/c]*100</td><td>16.76</td><td>2.26</td><td>5.07</td><td>4.48</td><td>0.40</td><td></td></tr></table>

Table 9  
The sensitivity analysis of total inventory cost by lead time.

<table><tr><td>Total inventory cost (×103)</td><td>LCD panel manufactories</td><td>LCD monitor manufactories</td><td>Regional DCs</td><td>Branch warehouses</td><td>Retailers</td></tr><tr><td>LT + 5% (1)</td><td>82,159</td><td>83,585</td><td>109,466</td><td>32,197</td><td>287,220</td></tr><tr><td>LT (2)</td><td>81,102</td><td>83,454</td><td>99,588</td><td>27,373</td><td>285,769</td></tr><tr><td>LT - 5% (3)</td><td>79,409</td><td>81,597</td><td>96,575</td><td>23,322</td><td>285,495</td></tr><tr><td>RFID cost (4)</td><td>2,955,707</td><td>8977.5</td><td>5386.5</td><td>14,364</td><td>14,364</td></tr><tr><td>LT + 5% [(1) - (2) - (4)]/(2) (%)</td><td>-2.36</td><td>0.15</td><td>9.91</td><td>17.57</td><td>0.50</td></tr><tr><td>LT - 5% [(3) - (2) - (4)]/(2) (%)</td><td>-5.73</td><td>-2.24</td><td>-3.03</td><td>-14.85</td><td>-0.10</td></tr></table>

Table 5 shows that the costs of each item are improved resulting from the comparison of the $R – S C I _ { G M }$ and $S C I _ { G M }$ models. Among them, the improvement rates of production cost and backorder cost increase a lot. Take LCD panel manufactories fo example. In the $R – S C I _ { G M }$ model, the production cost has a 52.11% decrease and the replenishment cost has a 0.68% decrease

Table 6 also shows that the costs of each item are improved resulting from the comparison of the $R – S C I _ { G M }$ and $R – S C I _ { A }$ RIMA models. Take retailers for example. In the $R – S C I _ { G M }$ model, the production cost has a 24.04% decrease and the backorder cost has a 30.56% decrease. The fitness for implementing a GM short-term forecasting model in the RFID-enabled supply chain can be thus demonstrated.

Table 10  
The sensitivity analysis of inventory turnover rate by lead time.

<table><tr><td>Inventory turnover rate</td><td>LCD panel manufactories</td><td>LCD monitor manufactories</td><td>Regional DCs</td><td>Branch warehouses</td><td>Retailers</td></tr><tr><td>LT + 5% (1)</td><td>0.769699</td><td>0.968169</td><td>0.780442</td><td>2.840962</td><td>0.234352</td></tr><tr><td>LT (2)</td><td>0.773500</td><td>0.972788</td><td>0.852247</td><td>3.316264</td><td>0.237599</td></tr><tr><td>LT - 5% (3)</td><td>0.780013</td><td>1.026480</td><td>0.902687</td><td>3.939564</td><td>0.240358</td></tr><tr><td>LT + 5% [(1) - (2)]/(2) (%)</td><td>-0.49</td><td>-0.48</td><td>-8.43</td><td>-14.33</td><td>-1.37</td></tr><tr><td>LT - 5% [(3) - (2)]/(2) (%)</td><td>0.84</td><td>5.52</td><td>5.92</td><td>18.79</td><td>1.16</td></tr></table>

Table 11  
The comparison of backorder cost by service levels.

<table><tr><td>Backorder risk</td><td>Low</td><td></td><td>Medium</td><td></td><td>High</td></tr><tr><td>Service level (%)</td><td>99</td><td>97</td><td>95</td><td>93</td><td>90</td></tr><tr><td> $R-SCI_{GM}$  ($/year)</td><td>1072</td><td>1082</td><td>1104</td><td>1117</td><td>1168</td></tr></table>

## 5.3.2. Inventory turnover rate

Table 7 shows that the inventory turnover rate in every tier are improved from the comparison of the $R – S C I _ { G M }$ and $S C I _ { G M }$ models. Take LCD panel manufactories for example, the inventory turnover rate has a 50.93% increase. Take retailers for example, the inventory turnover rate has a 25.83% increase. This shows the critical effectiveness generated from the implementation of the GM forecasting method in the RFID-enabled supply chain. Therefore, the importance of the implementation of RFID in the supply chain can be thus illustrated.

## 5.3.3. Bullwhip effect

Based on the definition of the bullwhip effect (BW), the bullwhip effect values of the $R – S C I _ { G M } , S C I _ { G M } ,$ and $R – S C I _ { A R I M A }$ model are calculated in Table 8. In the $R – S C I _ { G M }$ model, take retailers for example, the bullwhip effect value = retailers demand varjation ÷ end customer order deviatior $1 = 1 7 9 , 8 7 1 / 1 9 , 3 4 3 = 9 . 3$ This means that the demand variation enlarges 9 3 times when retailers are disseminating demand information. In conclusion, the RFID system and GM forecasting model both being implemented together in the supply chain can achieve a significant low degree of bullwhip effect.

## 5.3.4. Sensitivity analysis

This research carries out the analysis of the sensitivity of lead time (LT) and service level (SL) with the optimal model: the $R – S C I _ { G M }$ model. The lead time is analyzed by the method of the original setting $\mathrm { L T } \pm 5 \% ,$ , which affects the reorder point (s). From the comparison of total inventory costs in Table 9, it can be known that if the lead time increases, the cost increases. On the contrary, if the lead time decreases, the cost decreases. From the comparison of inventory turnover rates in Table 10, it can be known that the variation of the result is the same as that of the total inventory cost. The increase and decrease of the lead time affect the variation of reorder points and the inventory turnover rate. Take the branch warehouse for example, if the lead time has a 5% increase, then its total inventory cost will have a 17.57% increase, and its inventory turnover rate will have a 14.33% decrease. If the lead time has a 5% decrease, then its total inventory cost will have a 14.85% decrease, and its inventory turnover rate will have a 18.79% increase.

The analysis of sensitivity is carried out with service levels of 99%, 97%, 95%, 93%, and 90%, As service level increases, the risk of backorder will decrease. From Table 11, it can be known that the higher the service level is, the less the backorder cost and risk will be. On the contrary, the lower the service level is, the more the backorder cost and risk will increase.

## 6. Conclusion

From the result of the Taguchi experiments, we find that the optimal specification of $R – S C I _ { G M }$ model is to implement the (s, Q) pull-based replenishment policy, $\mathrm { G M } ( 1 , 1 ) \left( \alpha = 0 . 7 \right)$ forecasting method associated with the RFID-enabled system. Based on the Bernoulli experiment. the $R – S C I _ { G M }$ model has a 43.32% decrease in the total inventory cost in comparison to the $S C I _ { G M }$ model. This shows that the adoption of RFID technology has a significant effect on the supply chain performance. The $R – S C I _ { G M }$ has a 8.56% decrease in the total inventory cost in comparison to the $R – S C I _ { A R I M A }$ model. This also shows the adoption of the GM short-term forecasting method associated with RFID can effectively enhance the performance of forecasting function. The establishment of the $R – S C I _ { G M }$ model in Company A can weaken the degree of bullwhip effect in the supply chain.

In this research, we have successfully constructed a TFT–LCD industry-oriented simulation platform for evaluating the performance of the RFID-enabled global supply chain. The major mechanism for simulating the operations of global supply chain has been properly designed as a group of functional agents that can be sorted into ten categories. All of the input parameters of pull-based inventory replenishment policies are completely collected from Company A and then derived as decision variables using theoretical and practical equations. The GM-based customer demand forecasting model stemmed from the 52 weeks shipment data for TFT–LCD of Company A has been derived following six strict steps. We also have assessed the optimal factorial combination for pull-based replenishment policy, GM parameter and RFID utilization by adopting a well-known Taguchi experiment methodology.

Finally, the experiment shows that the integration of RFID-enabled real-time information sharing process, pull-based replenishment policy (s, Q) and GM short-term customer demand forecasting model in the global supply chain can effectively enhance the effectiveness of its inventory cost management. For industries RFID promoters, our analytical evidence presented in this research can help them identify the implementation principle: RFID adoption must be cooperated with an appropriate inventory replenishment policy and demand forecasting approach

## References

Borshchev, A., Filippov, A., 2004. From system dynamics and discrete event to practical agent based modeling: reasons, techniques, tools. In: The 22nd International Conference of the System Dynamics Society, Oxford, England, UK, July 25–29, 2004. <http://www.xjtek.com/file/142> (retrieved 15.10.07).

Chang, S.C., Lai, H.C., Yu, H.C., 2005. A variable P value rolling grey forecasting model for Taiwan semiconductor industry production. Technologica Forecasting & Social Change 72 (5), 623–640.

Chen, H.S., Yan, T.M., Kung, C.Y., 2008. Application of grey prediction theory to forecast 3G mobile phone in Taiwanese market. Journal of Grey System 11 (1), 43–48.

Chopra, S., Meindl, P., 2001. Supply Chain Management: Strategy, Planning and Operation. Irwin/McGraw-Hill, Saddle River, NJ.

Delen, D., Hardgrave, B.C., Sharda, R., 2007. RFID for Better Supply-Chain Management through Enhanced Information Visibility. ITRI-WP078-1006 Information Technology Research Institute: RFID Research Center, University of Arkansas.

Deng, J.L., 1982. Control problems of grey systems. System Control Letter 1 (5), 288–294

DisplaySearch, April 12, 2010. Shipment and Sales Revenue Update. <http://www.witsview.com/MarketTrend/Post.aspx?sectionid=2&postid=115> (retrieved 20.04.10).

Hardgrave, B.C., Waller, M., Miller, Robert., 2005. Does RFID Reduce Out of Stocks? A Preliminary Analysis. ITRI-WP058-1105. Information Technology Research Institute: RFID Research Center, University of Arkansas.

Hsu, L.C., 2003. Applying the grey prediction model to the global integrated circuit industry. Technological Forecasting & Social Change 70 (6), 563–574.

Karagiannaki, A., Pramatari, K., 2010. RFID-enabled supply chain process redesign using simulation. In: Proceedings of the 4th International Workshop on

Kleijnen, J.P.C., 2005. Supply chain simulation tools and techniques: a survey. International Journal of Simulation & Process Modeling 1 (1-2), 82–89

Kok, A.G., Shang, K.H., 2007. Inspection and replenishment policies for systems with inventory record inaccuracy. Manufacturing & Service Operations Management 9 (2), 185–205.

Lee, H.L., Padmanabhan, V., Whang, S., 1997. The bullwhip effect in supply chain. Sloan Management Review 38 (3), 93–102.

Lee, Y.M., Cheng, F., Leung, Y.T., 2004. Exploring the impact of RFID on supply chain dynamics. In: Proceedings of the 2004 Winter Simulation Conference, December 5–8, Piscataway. IEEE, NJ, USA, pp. 1145–1152.

Li, G.D., Yamaguchi, D., Nagai, M., Masuda, S., 2008. A prediction model using hybrid grey GM(1,1) model. Journal of Grey System 11 (1), 19–26.

Liang, W.Y., Huang, C.C., 2006. Agent-based demand forecast in multi-echelon supply chain. Decision Support Systems 42 (1), 390–407.

Material Handling Management, October 1, 2005. Wal-Mart Improves On-shelf Availability through the Use of Electronic Product Codes. <http:/ mhmonline.com/news/mhm\_industrynews\_4367/> (retrieved 12.12.08).

Materialsnet, 2008. The Future Trend and Technology Development of Flat Display. <http://www.materialsnet.com.tw/DocView.aspx?id=6637> (retrieved 5.01.09).

Mehrjerdi, Y.Z., 2009. RFID-enabled supply chain systems with computer simulation. Assembly Automation 29 (2), 174–183

Mills-Harris, M.D., Soylemezoglu, A., Saygin, C., 2007. Adaptive inventory management using RFID data. International Journal of Advanced Manufacturing Technology 32 (9-10), 1045–1051.

Mustafa, O., Theopisti, C.P., Melek, A., 2007. Systems dynamics modelling of a manufacturing supply chain system. Simulation Modelling Practice and Theory 15 (10), 1338–1355.

Ngai, E.W.T., Moon, K.K.L., Riggins, F.J., Yi, C.Y., 2008. RFID research: an academic literature review (1995–2005) and future research directions. Internationa Journal of Production Economics 112 (2), 510–520.

Sarac, A., Absi, N., Dauzre-Prs, S., 2008. A simulation approach to evaluate the impact of introducing RFID technologies in a three-level supply chain. In: Proceedings of 2008 Winter Simulation Conference, December 7–10. Miami. FI. USA, pp. 2741–2749.

Sarac, A., Absi, N., Dauzre-Prs, S., 2010. A literature review on the impact of RFID technologies on supply chain management. International Journal of Production Economics 128 (1), 77–95.

Sari, K., 2010. Exploring the impacts of radio frequency identification (RFID) technology on supply chain performance. European Journal of Operational Research 207 (1), 174–183.

Saygin, C., Sarangapani, J., Grasman, S.E., 2007. A systems approach to viable RFID implementation in the supply chain. Springer Series in Advanced Manufacturing: Trends in Supply Chain Design and Management Technologies and Methodologies, pp. 3–27.

Simchi-Levi, D., Kaminsky, P., Simchi-Levi, E., 2000. Designing and Managing the Supply Chain; Concepts, Strategies and Case Studies. Irwin/ McGraw-Hill, New York.

Tien, T.L., 2005. A research on the prediction of machining accuracy by the deterministic grey dynamic model DGDM(1,1,1). Applied Mathematics and Computation 161 (3), 923–945.

Ustundag, A., Tanyas, M., 2009. The impacts of Radio Frequency Identification (RFID) technology on supply chain costs. Transportation Research Part E: Logistics and Transportation Review 45 (1), 29–38.

Visich, J.K., Li, S., Khumawala, B.M., Reyes, P.M., 2009. Empirical evidence of RFID impacts on supply chain performance. International Journal of Operations and Production Management 29 (12), 1290–1315.

Wang, C.H., Hsu, L.C., 2008. Using genetic algorithms grey theory to forecast high technology industrial output. Applied Mathematics and Computation 195 (1), 256–263.

Wang, S.J., Liu, S.F., Wang, W.L., 2008. The simulated impact of RFID-enabled supply chain on pull-based inventory replenishment in TFT–LCD industry. International Journal of Production Economics 112 (2), 570–586.

Wang, S.J., Huang, C.T., Wang, W.L., Chen, Y.H., 2010. Incorporating ARIMA forecasting and service-level based replenishment in RFID-enabled supply chain. International Journal of Production Research 48 (9), 2655–2677.

Wu, C.J., Hsu, F.Y., Wen, K.L., Wu, J.H., 2006. The study of GM(1,1|a) on Verhulst model. Journal of Grey System 9 (2), 131–138

Zelbst, P.J., Green Jr., K.W., Sower, V.E., Baker, G., 2010. RFID utilization and information sharing: the impact on supply chain performance. Journal of Business and Industrial Marketing 25 (8), 582–589.
