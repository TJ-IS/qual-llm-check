---
otero_id: 684
otero_key: "4P4AEDVR"
title: "An agent-based decision support system for wholesale electricity market"
authors: "Toshiyuki Sueyoshi; Gopalakrishna R. Tadiparthi"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An agent-based decision support system for wholesale electricity market

Toshiyuki Sueyoshi <sup>a,b,⁎</sup>, Gopalakrishna R. Tadiparthi <sup>c</sup>

<sup>a</sup> Department of Management, New Mexico Institute of Mining and Technology, Socorro, NM 87801, USA

<sup>b</sup> Department of Industrial and Information Management, National Cheng Kung University, Tainan, Taiwan

<sup>c</sup> Department of Computer Science, New Mexico Institute of Mining and Technology, Socorro, NM 87801, USA

Received 19 October 2006; accepted 10 May 2007 Available online 18 May 2007

## Abstract

Application software has been developed for analyzing and understanding a dynamic price change in the US wholesale power market. Traders can use the software as an effective decision-making tool by modeling and simulating a power market. The software uses different features of a decision support system by creating a framework for assessing new trading strategies in a competitive electricity trading environment. The practicality of the software is confirmed by comparing its estimation accuracy with those of other methods (e.g., neural network and genetic algorithm). The software has been applied to a data set regarding the California electricity crisis in order to examine whether the learning (convergence) speed of traders is different between the two periods (before and during the crisis). Such an application confirms the validity of the proposed software. © 2007 Elsevier B.V. All rights reserved.

Keywords: Decision support software; Agent-based approach; Electricity market; Machine learning

## 1. Introduction

Human decision-making is vital for the growth of an economy. Traders, who make various trading decisions, consist of an important component in a market. The bidding decision of a trader affects the profit of business. Among many different markets, the wholesale power market is a volatile market where a trader's bidding decision may affect the gain of a utility firm. The power industry is recently becoming competitive, unlike in the past where it was controlled by monopolistic utilities. A decentralized market environment is replacing the traditional centralized-operation approach. This business trend is called “deregulation of the electricity market.” [The importance of the electric power industry in research on decision support systems can be found in the special issue of this journal ([15] Vol. 40, Issues 3–4) organized by Oren and Jiang in 2005. The special issue contains 16 articles under the title of “Challenge of Restructuring the Power Industry” that have explored analytical aspects of the electric power industry.]

The deregulation allows new players to compete for providing wholesale electricity services by setting their own prices in an auction format, rather than negotiating with state regulators on a fixed price. Many wholesale power markets are directed towards liberalization and competition in the world. Along with the deregulation, many corporate leaders and policy makers face a difficulty in both predicting and understanding a price change of the wholesale electricity. The price change occurs due to many uncontrollable factors such as a change in weather condition, a demographic change and different trading strategies among traders. Software tools are needed for players in the power industry to predict the price change, to understand such market activities and to aid in their decision-making activities.

Many software systems have been developed for the purpose of aiding a trader in a wholesale electricity market. The shortcomings of existing systems are that they do not incorporate a transmission system in these algorithms and lack an estimation capability of the price fluctuation of electricity. To overcome the methodological difficulties, this study develops a decision support system (DSS), referred to as “MAIS (Multi Agent Intelligent Simulator)”, where software agents represent market entities such as generators, wholesalers, a market administrator, a network operator, and a policy regulator. The software agents have their own trading objectives and strategies. They can adjust their trading strategies in the simulation process based on previous trading efforts' success or failure. They also constantly observe current market price of electricity.

The proposed DSS provides a simulation-based numerical capability. That is the purpose of this study. This type of research is not present in the special issue (2005) organized by Oren and Jiang. [See Sueyoshi and Tadiparthi [28,29] for a detailed description on the computer algorithm. Their research efforts are further extended in [30] that can investigate how a capacity limit on transmission influences the wholesale price of electricity.]

The structure of this article is organized as follows: The next section conducts a literature survey that indicates the position of the proposed DSS by comparing itself with other studies concerning on-line trading auctions. Section 3 describes both the architecture of MAIS and the software. Section 4 describes a market clearing algorithm that is incorporated into the proposed simulator. Section 5 documents the practicality of the proposed simulator, using a data set regarding the California electricity market. A concluding comment and future extensions are summarized in Section 6.

## 2. Previous works and existing software systems

Recently, Artificial Intelligence (AI) methods have been employed predominantly to solve various problems in decision making under uncertainty. Furthermore, many software systems have been developed to aid traders in their decision making in power trading. This section is subdivided into two parts. The first part surveys

AI techniques used in the construction of DSS. The second part evaluates some of the software systems used for electricity trading.

## 2.1. Artificial intelligence for decision support systems

Based on AI methods used, DSS can be classified into the following categories:

## 2.1.1. Soft computing techniques

This group of techniques uses the concepts related to rough set theory, fuzzy logic, neural networks and genetic algorithms. Many researchers use fuzzy and rough set theory as a basis for reasoning with existing data [2,9,18,26,33]. Neural Networks (NN) have been widely used for prediction and classification. Wilson and Sharda [34] use NN as an effective tool to predict bankruptcy. See [22] for a discussion on various problems in NN and the scope of improvements. Soft-computing techniques can be combined with one another to form hybrid approaches. Zeleznikow and Nolan [36] use a combination of fuzzy reasoning and NN to build an efficient DSS. Many research studies indicate that the combination of rough sets and NN provided a better analysis tool [3,8,35]. Combinations of Genetic programming and rough sets are also successfully employed in classification problems [13].

## 2.1.2. Knowledge engineering techniques

With an increasing use of information systems in organizations, knowledge management has become a challenge in maintaining data. New data is stored as facts and the knowledge base contains rules based on the facts. These new requirements led to the creation of knowledge-based systems and expert systems. Beynon et al. [5] discussed expert system modeling as a new paradigm in DSS. The use of knowledge-based systems can be found in [16]. Expert systems have been developed widely for the use of managers and decision-makers [7]. Sung and Lee [31] demonstrated the use of a knowledgebased management system to price thousands of items based on other constraints and policies.

## 2.1.3. Agent-based techniques

Agent-based modeling is widely used to represent complex social systems. Agent-based systems have been used for many applications that are ranging from stock market trading [12] to financial portfolio management and logistics [32]. Bui and Lee [6] have presented taxonomy for agent-based systems in decision making. Liang and Huang [11] have proposed a threelayered architecture of intelligent agents for electronic trading. See [4,17,25] for a detailed discussion on design and development of agent-based systems.

This study uses a combination of all the techniques mentioned above to build an intelligent decision making tool. The proposed software uses soft-computing techniques such as probabilistic reasoning and reinforcement learning. The software uses a knowledge-base to fully utilize knowledge on a wholesale market of electricity. Each player in the wholesale market is represented by an intelligent agent.

## 2.2. Existing software for power trading

PowerWeb, developed at Cornell University, is designed to understand various power markets with human decision makers who interact with each other in a web-based tool [37]. Generators are each modeled by a human trader. This model considers a single uniform auction in a Day Ahead (DA) market with a constant demand. This software does not have flexibility to model and simulate the behavior of a trader. This software ignores Real Time (RT) and Long Term (LT) markets.

Agentbuilder uses software agents to buy and sell electricity [1]. It utilizes decision theory and uses three strategies for buying and selling. All these strategies are described by smooth curves (monotonically increasing/ decreasing) that represent the bidding behavior of an agent. The drawback of this model is that the agents cannot adapt or change these bidding behaviors during a simulation process. This model ignores the presence of a system operator and implements only Dutch auction.

SEPIA (Simulator for Electrical Power Industry Agents), developed at University of Minnesota, uses adaptive agents and object oriented modeling techniques [21]. These adaptive agents use discovery informatics to develop and identify patterns in an environment. The model uses evolutionary learning techniques like incremental genetic algorithms. Even though the agents are equipped with learning capabilities, the market is not modeled to handle complex scenarios like an occurrence of congestion on transmission. Furthermore, this software does not consider auction markets like DA and RT. It only considers the LT market.

MASCEM (Multi Agent Simulation system for Competitive Electricity Markets) is a market simulator that makes use of Open Agent Architecture (OAA) to create a rule-based system [19]. The agent's bidding strategies are represented by monotonically increasing/ decreasing functions. This design does not implement the transmission system. The OAA does not provide for inbuilt customized GUIs (Graphic User Interfaces).

EMCAS (Electricity Market Complex Adaptive System), developed at Argonne National Laboratory, uses a complex adaptive system approach to represent agent learning and adaptation. It tests regulatory structures using genetic algorithms [14]. The agent's objectives are characterized by a utility function. A shortcoming of this tool is that it does not provide a predictive capability on market dynamics.

Table 1 compares the software models described above. Each model is evaluated from the perspective of five capabilities: (a) Prediction (Estimation), (b) Transmission, (c) Decision-making, (d) Analysis, and (e) Intelligence. The proposed MAIS and the existing software models can be functionally distinguished by the following five capabilities: First, none of the existing models (from PowerWeb to EMCAS) has a capability to predict market price of electricity. Meanwhile, the MAIS has an estimation capability to predict the price fluctuation of electricity. Second, the existing software models do not have a numerical capability regarding how a capacity limit on transmission influences the wholesale price of electricity. The MAIS incorporates such a numerical capability. Third, most of the agent models use a probabilistic model in order to investigate agent's bidding decision and a monotonically increasing/decreasing utility function to represent decision making capability. Fourth, it is important to have an analytical capability that can explore a power market by changing parameters related to the market. Finally, AI technique has to be incorporated for agent's adaptive behavior.

Table 1  
Comparison among different electricity trading software

<table><tr><td></td><td>Estimation</td><td>Transmission</td><td>Decision making</td><td>Analysis</td><td>Intelligence</td></tr><tr><td>PowerWeb</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Agentbuilder</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>SEPIA</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>MASCEM</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>EMCAS</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>MAIS</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Note: MAIS (Multi Agent Intelligence Simulator) is proposed in this study.

Comparing the previous research works on on-line trading and related software developments for the power industry, this study identifies the following unique features of MAIS: First, the wholesale power market incorporated in the simulator is functionally separated into two markets (DA and RT). Each trader in the simulator can make his bidding decision in DA and then make another decision in RT, depending upon the win/lose result in the DA market. Thus, Two-Settlement System (TSS) auctions are incorporated into the proposed simulator. Such a research effort cannot be found in the previous research works. Second, each trader is designed to have his own learning capability. The learning capability is based upon a sigmoid function that provides a winning probability from previous bidding results. Such a learning capability cannot be found in the previous research. Third, a zonal market is represented by means of a transmission system in the simulator. Finally, traders can communicate with each other through a network capability incorporated into the proposed software.

## 3. Multi agent intelligent simulator

The MAIS consists of many software agents that interact with each other. They also interact with a power market (as an environment) by observing a price fluctuation of wholesale electricity.

Fig. 1 depicts the architecture of MAIS. There are five types of agents in MAIS: market administration, supplyside, demand-side, network operation, and utility policy making. The main objectives of an electricity market are to ensure the security of the power system, its efficient operation and further to decrease the cost of electricity through competition [23]. The market environment typically consists of a pool market for DA and RT. (Note that the proposed simulator does not include a bilateral contract between a generator and a wholesaler because the market price setting scheme is not clear.)

![](/api/attachments/4P4AEDVR/fulltext/images/5dfffd1944fcf44b01644a3e9a4b6566d7c1d91b07ce08f603bf241413bff69d.jpg)  
Fig. 1. Architecture of MAIS.

## 3.1. Market administrator

The electricity industry is functionally separated into the four divisions: (a) generation, (b) transmission, (c) distribution and (d) retailing. The MAIS incorporates a pool market scheme where electricity-generating companies submit their bidding amounts and prices, while wholesale companies submit consumption bids. A market operator, like ISO (Independent System Operator like PJM which controls the area of Pennsylvania– New Jersey–Mainland), regulates the pool market using a market clearing system to determine the market price of electricity. The pool market is considered as an efficient market scheme and a clearing tool for the market is an auction mechanism [10,24].

The US wholesale power market is functionally separated into a transmission market and a power exchange market. The US wholesale power exchange market is further functionally broken down into a RT market, an hour-ahead market, a DA market and a LT market. Each market has unique features in terms of an auction/exchange process and transmission agreement.

The software mainly focuses upon trading strategies for both DA and RT markets, because the bidding behaviors of traders in both DA and RT have a close linkage between them. Moreover, the two markets are important in the investigation of a price fluctuation in the wholesale power market. In this study, RT implies not only the real time market but also the hour-ahead market, because the two are functionally similar and decided on the same day. All traders enter the market to correspond to actual power flows. Hence, the aspect of financial speculation is very limited in RT. Thus, RT can be considered as a physical market. In the RT market, traders need to make their decisions within a limited time. So, it can be considered as a spot market in this study. Meanwhile, the DA market can be considered as a financial market, because a decision for the market is for the next day power delivery, so that there is a time for making a decision based upon demand forecasting and speculation.

Fig. 2 depicts the output window of a market mechanism controlled by a market administrator. The window is divided into four graphs: DA Curve, RT Curve, Price vs. Iterations, and Volume vs. Iterations. The DA Curve shows a demand–supply curve in the DA market. The RT Curve shows the market clearing scheme for RT. The Price vs. Iterations graph depicts a price fluctuation, during every run, in the DA and RT market. Volume vs.

![](/api/attachments/4P4AEDVR/fulltext/images/452a873297ec83aa08d2a11f2f9905a90d566a0512cce1279c5c536760cf933c.jpg)  
Fig. 2. Computer monitor.

Iterations exhibits a volume fluctuation and volume share of DA and RT, which gives a simulation outline on how much the volume fluctuates during a whole simulation.

## 3.2. Supply-side agent

Generators form supply-side agents. They use a knowledge base to store bidding values and results. The knowledge base contains all previous data used by each generator. An exponential utility function is used to represent his risk-averseness behavior. Mathematically, the utility function is expressed by $1 - \mathrm { E X P } ( - \zeta \times \mathrm { R e } .$ ward). Here, $\zeta$ is the risk-aversion factor. The bidding decision of the i-th generator $( i { = } 1 , 2 , . . . , n )$ is made by an adaptive learning algorithm which can be specified for DA and RT as follows:

(a) The i-th generator bids $( s _ { i t } ^ { 1 } , p _ { i t } ^ { 1 } )$ for DA where $s _ { i t } ^ { 1 }$ is the bidding amount of power generation in Kilowatt Hours (KWH) and $p _ { i t } ^ { 1 }$ is the bidding price measured by a unit price of electricity (\$/ KWH). The superscript $^ { \ \mathfrak { s } } 1 ^ { \mathfrak { s } }$ indicates DA and the subscript $\mathbf { \ddot { \Gamma } } ^ { 6 6 } t ^ { 5 }$ indicates the t-th period of the power delivery.

(b) The bidding amount is expressed by $s _ { i t } ^ { 1 } { = } { \alpha } _ { i t } { \times } s _ { i t } ^ { m } ,$ where $\alpha _ { i t } \left( 0 \leq \alpha _ { i t } \leq 1 \right)$ is a bidding rate to express the ratio of bidding amount of electricity to the maximum generating capacity of the i-th generator and $s _ { i t } ^ { m }$ is the maximum power generation capacity of the i-th generator.

(c) The bidding price is given by $p _ { i t } ^ { 1 } { = } \mathbf { M } \mathbf { C } _ { i t } ^ { 1 } / ( 1 { - } \beta _ { i t } )$ Marginal Cost (MC<sup>1</sup>) of generation is defined as an operations and maintenance cost of the generating plant that is needed to supply the immediate demand for electricity and is usually listed on the web site of ISO. $\beta _ { i t } ( 0 \le \beta _ { i t } < 1 )$ is a mark-up rate. The mark-up rate is used to express a ratio of the bidding price from the marginal cost. The mark-up rate reflects the trader's pricing strategy.

(d) In RT market, the i-th generator bids $( s _ { i t } ^ { 0 } , p _ { i t } ^ { 0 } )$ for RT where $s _ { i t } ^ { 0 }$ is the bidding amount of power generation (KWH) and $p _ { i t } ^ { 0 }$ is the bidding price that is measured by per unit electricity (\$/KWH). The superscript $\ " { 0 } ^ { \ast }$ indicates RT. The bidding amount $( s _ { i t } ^ { 0 } )$ is expressed as the remaining amount of power that the generator can produce after the allocation in the DA market ${ ( s _ { i t } ^ { 0 } \bar { = } s _ { i t } ^ { m } - \hat { s } _ { i t } ^ { 1 } ) }$ ). The bidding price $( p _ { i t } ^ { 0 } )$ is expressed in terms of the marginal cost $( \mathrm { M C } _ { i t } ^ { 0 } )$ . It is given by $p _ { i t } ^ { 0 } { = } \mathrm { M C } _ { i t } ^ { 0 } / ( 1 { - } \eta _ { i t } )$ . Here, $\eta _ { i t }$ $( 0 \leq \eta < 1 )$ is a mark-up rate.

Fig. 3 depicts a computer monitor on which a user can input the maximum supply and marginal cost either in the form of a text file or a constant value. The data, if supplied in a text file, should be in the form of a “tab limited text file” with the first column representing the price and the second column representing the quantity.

The user can either decide to include learning or not, depending upon a simulation model he is trying to build. If the user chooses an adaptive learning generator, he can specify the knowledge accumulation period (btotal number of iterations) and the minimum probability of success (a value between 0 and 1). Each generator has a trader identification number. Optionally, the user can also enter the names of the generators each one corresponding to the ID. The user can specify the number of generators of this kind of settings and create them by pressing the “Create” button. This action will create the specified number of generator agents in the simulator.

The model assumes that all traders exhibit risk-averse behavior and uses an exponential utility function to represent such risk-averseness. The user can also enter his choice of risk aversion factor.

## 3.3. Demand-side agent

Wholesalers form demand-side agents. As shown in Fig. 1, the wholesaler has additional functional capabilities in addition to those that are present in the supply-side. The wholesaler needs to estimate a price and forecast a load from the previous data. The bidding decision of the j-th wholesaler $( j = 1 , 2 , . . . , k )$ is made by an adaptive learning algorithm, which can be specified for DA and RT as follows:

![](/api/attachments/4P4AEDVR/fulltext/images/d233841083efe53fe9eb5aff84f23589263b6f44aa967131027a6aae668752b1.jpg)  
Fig. 3. Generator creation wizard.

(a) The j-th wholesaler bids $( d _ { j t } ^ { 1 } , p _ { j t } ^ { 1 } )$ for DA where $d _ { j t } ^ { 1 }$ is the bidding amount of power (KWH). $p _ { j t } ^ { 1 }$ is the bidding price of the wholesaler which is measured by a unit price of electricity (\$/KWH).

(b) The wholesaler uses his demand-forecasting algorithm to predict the demand on a particular day. Let $e _ { j t }$ be the demand estimated by the j-th wholesaler or ISO.

(c) The bidding amount $( d _ { j t } ^ { 1 } )$ is expressed by $d _ { j t } ^ { 1 } { = } \delta _ { j t } e _ { j t } ,$ where $\delta _ { j t } ( 0 \leq \delta _ { j t } \leq 1 )$ is a bidding rate to express the strategic reduction of each bid from the demand estimate $( e _ { j t } )$

(d) The bidding price $( p _ { j t } ^ { 1 } )$ is expressed by $p _ { j t } ^ { 1 } { = } \lambda _ { j t } w _ { j t } ^ { 1 } .$ Here, $\lambda _ { j t } ( 0 \leq \lambda \leq 1 )$ is a decision parameter for price adjustment from the estimated price. The wholesaler predicts a price estimate $( w _ { j t } ^ { 1 } )$ by using an inverse function (IF) of demand, i.e. $w _ { j t } ^ { 1 } { = } \mathrm { I F }$ $( e _ { j t } )$

(e) $r _ { j t }$ is the real demand on the delivery period (t). Then, the wholesaler needs to specify the demand procured from the RT market in order to satisfy the real demand that is computed by $d _ { j t } ^ { 0 } { = } r _ { j t } { - } \dot { { d } } _ { j t } ^ { 1 }$ the bidding amount for RT of the j-th wholesaler.

Fig. 4 depicts a computer monitor on which a user can configure and create a wholesaler based on demand-side agent. It specifies a real demand that is given in the form of a text file or a formula. The user can select the appropriate option. The user can choose a historical file which contains previous consumptions for the wholesaler. A historical data set on demand is plotted as a graph to facilitate the visualization of the usage in the past. The user can create his price estimation graph, as depicted in Fig. 5. The yellow colored line segment represents the price function for residential customers and the red colored line segment represents the price function for commercial customers. The slope of these lines and the functions can be modified by changing the parameters in the Price Estimation tab of Fig. 4. Since the wholesaler has learning capabilities, the Learning tab shows the different learning options available on a monitor. The Learning algorithms are the same as available in the supply-side agent. The parameters are the same as explained in the previous section. As depicted in Fig. 4, there are four options for choosing a forecasting method on a computer monitor. They are “Moving Average”, “Exponential Smoothing”, “Random” and “Average”. Choosing the respective option will prompt for the corresponding required parameters. The user also needs to enter the retail price (expressed in dollars) of the wholesaler throughout this simulation. The exponential utility function expresses the risk-averse behavior of the wholesaler. The user can input the risk aversion factor to denote the level of risk-averseness of the wholesaler.

![](/api/attachments/4P4AEDVR/fulltext/images/a3c07ebe6454e088592df1ffc7e2d3f8bd537dc220836e17b543b2ca88dcf105.jpg)  
Fig. 4. Wholesaler creation wizard.

![](/api/attachments/4P4AEDVR/fulltext/images/a92cb40165b74447a313554d8cc66c26ebc1c6666b288cdb7ee0dafd3fad279e.jpg)  
Fig. 5. Price forecasting function. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

## 3.4. Network operator

The network operator manages a whole transmission grid system. He is responsible to oversee that a load is satisfied within each zone. A transmission control flow algorithm is used to control the flow of electricity within the grid system. The network operator executes the market clearing algorithm to determine the market price under a capacity limit on transmission. See Appendix A that discusses the market clearing process under the capacity limit on transmission.

Fig. 6 provides a graphical canvas for a user to design a transmission system. The user can draw different elements in a wholesaler market with the help of a mouse. The different generators and loads can be labeled on a computer monitor. The transmission lines are drawn and the limits can be specified. If no limit is specified, then it is assumed that there is no limit on the link. The zones are drawn using dotted red-colored lines.

Fig. 7 depicts a computer monitor that visually describes a dispatch scheduling process among generators. The monitor is for the zone (2) which obtains electricity from not only itself but also the other zones (e.g., Zones 1 and 3). For a visual description, Fig. 7 depicts a monitor from 4 AM to 7 PM. The monitor depicts a dispatch schedule of each generator on the 24-hour framework. The number listed within each color indicates the amount of generation. Fig. 8 depicts a computer monitor for a total amount of daily-based generation for a specific zone within the 24-hour framework.

## 3.5. Utility policy administrator

The administrator provides policy makers and federal/ local regulatory agencies with a set of tools to query and modify (if necessary) policy rules related to the operation of wholesale power trading. A user of the administrator can query a market data set in order to observe whether any of the participants behave inappropriately (e.g., the execution of a market power). They also ensure a smooth operation of the wholesale market of electricity.

## 4. Market clearing algorithms

The market clearing process incorporated in the proposed simulator is structured by TSS. This type of auction process is used by PJM. Fig. 9 depicts the TSS at the t-th period that contains DA and RT along with these market components (fundamentals):

![](/api/attachments/4P4AEDVR/fulltext/images/489f6dd6b0bc7831de9b5f31d843b494489e0045e73b2747a8e3c2e4351fdaed.jpg)  
Fig. 6. Computer monitor for grid system. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

<table><tr><td colspan="17">Schedule of Generators</td></tr><tr><td>Gen / Time</td><td>4:00</td><td>5:00</td><td>6:00</td><td>7:00</td><td>8:00</td><td>9:00</td><td>10:00</td><td>11:00</td><td>12:00</td><td>13:00</td><td>14:00</td><td>15:00</td><td>16:00</td><td>17:00</td><td>18:00</td><td>19:00</td></tr><tr><td>Gen I-1</td><td></td><td></td><td></td><td>250</td><td>250</td><td></td><td></td><td>100</td><td>100</td><td>100</td><td>100</td><td></td><td></td><td></td><td>50</td><td>50</td></tr><tr><td>Gen I-2</td><td></td><td></td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td></td><td></td><td></td><td>50</td><td>70</td><td>50</td><td></td><td></td></tr><tr><td>Gen I-3</td><td>100</td><td>100</td><td></td><td></td><td></td><td>250</td><td>250</td><td>250</td><td>250</td><td>250</td><td>250</td><td></td><td></td><td></td><td></td><td>150</td></tr><tr><td>Gen I-4</td><td></td><td></td><td></td><td></td><td></td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>156</td><td>150</td><td>150</td><td>150</td></tr><tr><td>Gen I-5</td><td></td><td></td><td>150</td><td>150</td><td></td><td></td><td></td><td></td><td>50</td><td>50</td><td>50</td><td>50</td><td></td><td></td><td></td><td></td></tr><tr><td>Gen II-1</td><td>250</td><td>250</td><td>250</td><td>250</td><td>250</td><td>240</td><td>250</td><td>250</td><td>250</td><td>250</td><td>250</td><td>250</td><td>270</td><td>250</td><td>254</td><td>250</td></tr><tr><td>Gen II-2</td><td>50</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>104</td><td>100</td><td>100</td><td>100</td></tr><tr><td>Gen II-3</td><td></td><td></td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>109</td><td>100</td><td>100</td><td></td></tr><tr><td>Gen III-1</td><td></td><td></td><td></td><td>50</td><td>50</td><td>50</td><td></td><td></td><td></td><td></td><td></td><td>100</td><td>120</td><td>100</td><td>100</td><td>100</td></tr><tr><td>Gen III-2</td><td></td><td></td><td></td><td>100</td><td>100</td><td>100</td><td></td><td></td><td></td><td>100</td><td>100</td><td></td><td></td><td>50</td><td>50</td><td></td></tr><tr><td>Gen III-3</td><td></td><td>150</td><td>100</td><td>100</td><td>100</td><td>95</td><td>100</td><td></td><td></td><td>100</td><td>100</td><td>100</td><td>110</td><td></td><td></td><td></td></tr><tr><td>Gen III-4</td><td>50</td><td>50</td><td>50</td><td></td><td></td><td></td><td>150</td><td>150</td><td>150</td><td></td><td></td><td>150</td><td>169</td><td>150</td><td>150</td><td>150</td></tr><tr><td>Gen III-5</td><td>50</td><td></td><td></td><td></td><td>200</td><td>195</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td></td><td></td><td></td><td></td></tr><tr><td>Gen III-6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>100</td><td>80</td><td>80</td><td>80</td><td>80</td><td>100</td><td></td><td></td></tr><tr><td>Total</td><td>500</td><td>650</td><td>900</td><td>1250</td><td>1300</td><td>1430</td><td>1450</td><td>1450</td><td>1450</td><td>1480</td><td>1480</td><td>1330</td><td>1188</td><td>1050</td><td>954</td><td>950</td></tr></table>

Fig. 7. Computer monitor for dispatch scheduling. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

## 4.1. Market clearing algorithm for DA

Let the pair $( s _ { i t } ^ { 1 } , p _ { i t } ^ { 1 } )$ represent the bid submitted by the i-th generator in the DA market. Let the pair $( d _ { j t } ^ { 1 } , p _ { j t } ^ { 1 } )$ represent the bid submitted by the j-th wholesaler. The market clearing algorithm at the t-th period is specified as below:

1. Sort the pairs $( s _ { i t } ^ { 1 } , ~ p _ { i t } ^ { 1 } )$ in the ascending order with respect to $p _ { i t } ^ { 1 }$

2. Calculate the cumulative supply for the i-th generator $( i { = } 1 . . . n )$ . The cumulative supply is the sum of supply quantities (including its own supply) whose corresponding bidding prices are less than the bidding price of i-th generator. The cumulative supply (CS) of the i-th generator is represented by $\begin{array} { r } { \mathbf { C S } _ { i t } ^ { 1 } \big ( = \sum _ { a = 1 } ^ { i } s _ { a t } ^ { 1 } \big ) } \end{array}$

<sup>¼ ¼</sup>3. Sort the pairs $( d _ { j t } ^ { 1 } , p _ { j t } ^ { 1 } )$ in the descending order with respect to $p _ { j t } ^ { 1 } .$

4. Calculate the cumulative demand for the j-th wholesaler $( j { = } 1 . . . k )$ . The cumulative demand is the sum of demand quantities (including its own demand) whose corresponding bidding prices are greater than the bidding price of the j-th wholesaler. The cumulative demand (CD) of the j-th wholesaler is represented by $\begin{array} { r } { \mathrm { C D } _ { j t } ^ { 1 } ( = \sum _ { b = 1 } ^ { j } d _ { b t } ^ { 1 } ) } \end{array}$

<sup>¼ ¼</sup>5. Find an equilibrium point by comparing the cumulative supply (CS) with the cumulative demand (CD). If there is the equilibrium point, go to step 6. If there is no equilibrium point, the market clearing price is set to 0 and no trading was possible in the DA market. Go to step 8.

6. A projection of the equilibrium point on the Yaxis gives the market clearing price $\hat { p } _ { t } ^ { 1 }$ of the DA market.

7. Allocate electricity for the t-th period. All generators with $p _ { i t } ^ { 1 } { \le } \hat { p } _ { t } ^ { 1 }$ can supply power $( s _ { i t } ^ { 1 } )$ to the DA market with the market price $\hat { p } _ { t } ^ { 1 }$ and all wholesalers with $p _ { j t } ^ { 1 } { \geq } \hat { p _ { t } ^ { 1 } }$ can receive power $( d _ { j t } ^ { 1 } )$ with the same market price $\hat { p } _ { t } ^ { 1 }$ from the DA market.

8. Stop.

## 4.2. Market clearing algorithm for RT

In RT market, only generators bid and wholesalers have to accept the price decided by the market clearing algorithm. Let $( s _ { i t } ^ { 0 } , ~ p _ { i t } ^ { 0 } )$ be the bid posted by i-th generator in the RT market. Let $d _ { j t } ^ { 0 }$ be the quantity required by the j-th wholesaler in the RT market. The market clearing algorithm can be described as below:

![](/api/attachments/4P4AEDVR/fulltext/images/550f7e4df935e972df7afecda62555ccf147e2b779e1953e3940e87918137b03.jpg)  
Fig. 8. Computer monitor for total generation.

1. Sort the pairs $( s _ { i t } ^ { 0 } , ~ p _ { i t } ^ { 0 } )$ in the ascending order with respect to $p _ { i t } ^ { 0 }$

2. Calculate the cumulative supply for each generator (i = 1 to n). The cumulative supply of i-th generator is $\textstyle \mathbf { C S } _ { i t } ^ { 0 } ( = \sum _ { a = 1 } ^ { i } s _ { a t } ^ { 0 } )$

3. Calculate the aggregate demand of all wholesalers at the t-th period. The total demand of the supply side is $\textstyle \operatorname { C D } _ { t } ^ { 0 } { \biggl ( } = \sum _ { j = 1 } ^ { m } d _ { j t } ^ { 0 } { \biggr ) }$

4. If $\textstyle \mathbf { C D } _ { t } ^ { 0 } { \leq } \sum _ { i = 1 } ^ { n } s _ { i t } ^ { 0 }$ , then go to step 5. Otherwise, go to step 7.

5. The equilibrium point is determined via comparing the cumulative supply (CS) by the total demand.

6. Allocate the electricity. Let $\hat { p } _ { t } ^ { 0 }$ be the market clearing price that is obtained from the equilibrium point. Then, all generators with $p _ { t } ^ { 0 } { < } \hat { p } _ { t } ^ { 0 }$ can supply power $( s _ { i t } ^ { 0 } )$ for price $\hat { p } _ { t } ^ { 0 }$ to the RT market and all wholesalers receive power $( d _ { j t } ^ { 0 } )$ for the same price $\hat { p } _ { j t } ^ { 0 }$ from the RT market. 7. Stop.

![](/api/attachments/4P4AEDVR/fulltext/images/814d4129d653153b9c78d3e1cc0d81a85d33df55a62a744890c3ab13050d381d.jpg)  
Fig. 9. Two settlement system.

## 4.3. Example

The difference between DA and RT is depicted in Figs. 10 and 11. Fig. 10 visually describes the market clearing mechanism for DA. In Fig. 10, ISO allocates the generation amount $( s _ { 1 t } ^ { 1 } )$ of the first generator to satisfy the demand $( d _ { 1 t } ^ { 1 } )$ of the first wholesaler. Such a power allocation is continued until an Equilibrium Point (EP) is found in DA. In Fig. 10 the equilibrium point is identified as EP, where the five generators are used to satisfy the demand required by the three wholesalers. Consequently, $p _ { 5 t } ^ { 1 }$ (the bidding price of the fifth generator) becomes the market clearing price $( \hat { p _ { t } } ^ { 1 } )$ for DA.

Fig. 11 depicts the market clearing mechanism for RT. Wholesalers submit only their demands, but not bidding prices, because the demand of end users must be always satisfied. In Fig. 11, ISO accumulates the generation amounts until the total demand is satisfied. In the figure, $D _ { t } ^ { 0 }$ is such a point and an equilibrium point is identified as EP, where four generators are used to satisfy the total demand required by wholesalers. Consequently, $p _ { 4 t } ^ { 0 }$ (the bidding price of the four generators) becomes the market clearing price $( \hat { p } _ { t } ^ { 0 } )$ for RT.

## 5. Application

## 5.1. Structure of California electricity market

To document the practicality of the proposed MAIS, this study applies the simulator to a data set regarding the California electricity market from 1st April 1998 to 31st January 2001. The California electricity crisis occurred during the observed period. The market is divided into three zones for the purposes of pricing:

![](/api/attachments/4P4AEDVR/fulltext/images/6406a02d2edc906ec4efd98c80cbba3228e799618b7f4cc59c51c9a84d995deb.jpg)  
Fig. 10. Equilibrium point in DA.

![](/api/attachments/4P4AEDVR/fulltext/images/c5f4eb9efe910778d2801cf27f3f9e4f465298e40342184c94b4b31da5551929.jpg)  
Fig. 11. Equilibrium point in RT.

NP15 is in the north, SP15 is in the south, and ZP26 is in the center of the state. The central zone (ZP26) has only 2 transmission links, one to Northern path (NP15) and one to Southern path (SP15). The Northern path and Southern path are not directly connected to each other. If they need excess electricity, they have to import it from other states. The data set consists of all information such as transaction time, transaction date, price at each zone in DA and HA (hour-ahead) markets, unconstrained price and quantity of the system, import/export quantities in each zone and prices of various auxiliary services. We obtain the data set on the California electricity market from the University of California Energy Institute web site www.ucei.berkeley.edu/datamine/uceidata/uceidata.zip). The California ISO does not have RT trading as found in PJM, but it has HA trading. Both are functionally the same, as mentioned previously. Hence, RT is replaced by HA, hereafter, to adjust our description to the California ISO. The DA trading was stopped after 31st January 2001.

Table 2 describes the data set for the three California wholesale zones (DA and HA). Each sample represents hourly prices representing 24 h per day. SP-15 DA and HA represent the hourly market price of southern zone of California for DA market and HA market, respectively, from 1st April 1998 to 31st January 2001. NP-15

Table 2  
California market price

<table><tr><td>Market</td><td>Mean</td><td>Median</td><td>Skewness</td><td>Kurtosis</td></tr><tr><td>SP-15 DA</td><td>56.11</td><td>29.65</td><td>7.63</td><td>142.60</td></tr><tr><td>SP-15 HA</td><td>53.24</td><td>27.31</td><td>3.54</td><td>19.87</td></tr><tr><td>NP-15 DA</td><td>62.36</td><td>30.35</td><td>6.60</td><td>107.57</td></tr><tr><td>NP-15 HA</td><td>63.05</td><td>30.08</td><td>2.90</td><td>13.25</td></tr><tr><td>ZP-26 DA</td><td>106.00</td><td>65.98</td><td>6.10</td><td>89.68</td></tr><tr><td>ZP-26 HA</td><td>100.76</td><td>68.40</td><td>2.06</td><td>8.03</td></tr></table>

DA and HA represent the hourly market price of northern zone of California for DA and HA, respectively, from 1st April 1998 to 31st January 2001. ZP-26 DA and HA represent the hourly market price of central zone of California for DA and HA, respectively, from 1st February 2000 to 31st January 2001. For all the DA markets, a maximum price of \$2499.58 was observed at 7 PM on 21st January 2001. All the HA markets had a maximum price of \$750 starting from 26th June 2000. It was observed that prices started rising steadily from the summer of 2000.

## 5.1.1. Market composition

Since we cannot access information related to an exact composition between generators and wholesalers from 1998 to 2001, we use the information provided by California Energy Commission on the web site for the year of 2005. The web site (http://www.energy.ca.gov/ maps/electricity\_market.html) provides an approximate composition of the generators. Thus, this study considers that there are 964 generators in California among which 343 are hydroelectric with 20% market capacity, 44 are geothermal with 3% market capacity, 373 are oil/gas with 58% market capacity, 17 are coal with 6% market capacity, 94 are wind with 4% market capacity, 80 are WTE with 2% market capacity, 2 are nuclear with 7% market capacity, 11 are solar with 1% market capacity. Meanwhile, the wholesaler composition is estimated from the web site: http://www.energy.ca.gov/ electricity/electricity\_consumption\_utility.html. There are a total of 48 wholesalers. Pacific Gas and Electric has 30% of the share, San Diego Gas & Electric has 7% of the share, Southern California Edison has 31% of the share, LA Department of Water and Power has 9% of the share. Sacramento Municipal Utility District has 4% of the share, California Department of Water Resources has 3% of the share, and other 41 utilities have a 12% share. Self-generating agencies account for 4% of the share.

## 5.2. Evaluation criterion and alternate approaches

## 5.2.1. Evaluation criterion

An evaluation criterion is the estimation accuracy (%) which is defined as

$$
1 - \frac {1}{N} \sum_ {t = 1} ^ {N} \left| \frac {\text { Real   Market   Price } (t) - \text { Estimated   Market   Price } (t)}{\text { Average   Real   Market   Price } (t)} \right|
$$

Here, N stands for the number of evaluation periods. This criterion is suggested by Shahidehpour et al. [23].

## 5.2.2. Neural Network (NN)

The first alternative is NN whose use for price estimation has been recommended by many researchers (e.g., [23]). We use Radial Basis Function Neural Networks (RBFNN) to forecast the market price of electricity. [See, for example, MATLAB Neural Network Toolbox, Version 6.1.0.450 Release12.1, that is listed in a web site: http://www.mathworks.com/products/neuralnet/).] The RBFNN is widely used for finding an approximation of a non-linear function as well as for finding interpolation values of a function that is defined only on a finite subset of real numbers. As found in many NN methods, the structure of the proposed use of NN is separated into an input layer, an output layer and a hidden layer(s). The hidden layer consists of neurons with a Gaussian activation function. There is a non-linear mapping from the input layer to the hidden layer and there is a linear mapping from the hidden layer to the output layer.

The NN operation used for the comparison consists of the following two steps: Training and Testing. For SP-15DA, SP-15HA, NP-15DA, and NP-15HA, the first 6216 data points (259 days×24 h) are used for training and the next 18,672 data points (778 days×24 h) are used for testing. The most commonly used NN is a feed forward NN because it uses less number of neurons. In the case of a radial basis network, the number of neurons used in the input layer and hidden layer is equal to the number of input vectors. In this experiment, we use a radial basis network because of its prediction accuracy. We create the radial basis network with the function ‘newrbe’. We initialize the bias to be 0.8326 (sqrt(− ln(0.5))), i.e., the spread is set to 1.

The inputs of NN for predicting SP-15DA, NP-15DA, ZP-26DA price are day-of-the-week, temperature, and DA demand. When predicting the SP-15RT, NP-15RT, ZP-26RT price, inputs of NN are day-of-the-week, temperature, RT demand, and corresponding DA market price. For each of these predictions, 1556 neurons (778 neurons in input layer + 778 neurons in hidden layer) are used. Even though a standard feed forward NN would use fewer neurons, we chose RBFNN because of its better prediction capability and lesser training time.

## 5.2.3. Genetic algorithm (GA)

The other alternative is GA which has been recommended by Richter et al. [20]. GA Toolbox for MATLAB, developed at the Department of Automatic Control and Systems Engineering of The University of Sheffield, UK, is used for this study [source:http://www. shef.ac.uk/acse/research/ecrg/gat.html]. The parameters used in the GA are specified as follows: population size = 168, crossover probability = 0.8, mutation probability =0.001 and maximum generation =16,800. The objective of each artificial trader is to maximize the total profit obtained after n iterations. Therefore, the objective function of the GA is to maximize the total profit obtained by agents.

Each individual in the population is encoded by a 9-bit binary number. This encoding represents the day-of-the week (three bits), temperature (two bits), and demand (four bits). The day-of-the-week may be any value in the range: Monday through Friday. The temperature is divided into three categories, Low, Mild, and High. The demand (x) is categorized into eight divisions: (a) x b mean−3SD, (b) mean−3SDbxb mean−2SD, (c) mean−2SDbxb mean −SD, (d) mean − SD bx bmean, (e) mean b x b mean+SD, (f) mean+SDbxbmean+2SD, (g) mean+ 2SDbxbmean+3SD, and (h) mean+3SDbx. Here, SD stands for a standard deviation of demand. The genetic algorithm is initialized with a random population size of 168 (7 day-of-the week× 3 temperature categories× 8 demand categories) individuals. The maximum generation is set to 16,800 as this termination condition produces the best result for the above specified encoding. The crossover probability and mutation probability are set to arbitrary values of 0.8 and 0.001. It is observed that these variables do not affect the performance of the genetic algorithm for the data set used in this study.

## 5.3. Estimation results

There was no data about the capacity limit on California transmission links. To determine a capacity limit on the lines between zones, we calculate the difference between import and export quantity to the whole market. After observing the data set used for this study, a transmission limit of 11,752 GWH (maximum difference) was applied on the transmission link between central zone and northern zone. The same limit was applied between the transmission link between central and southern zones, as well.

Table 3 summarizes the estimation accuracy of the three approaches. The estimation accuracy regarding each power zone is further separated into two: the one before and the one during the California electricity crisis. For example, SP-15 and NP15 have 18,312 and 6576 data points before the crisis and during the crisis, respectively. Meanwhile, ZP-26 has the number of data points before the crisis and during the crisis which are 2208 and 6576, respectively. The weighted average estimation accuracy of each zone is computed by [(average estimation accuracy before crisis) × (# of observations before crisis) + (average estimation accuracy during crisis) × (# of observations during crisis)] / (# of all observations before and during crisis). The average (84.33%) of MAIS for all markets is computed by the total weighted averages (=85.76% +… +89.12%) divided by 6 (the number of markets).

Estimation accuracy (%) of three approaches (line limit: 11,752GWH)

<table><tr><td rowspan="2">Market</td><td colspan="9">Estimation accuracy</td></tr><tr><td>GA</td><td></td><td></td><td>NN</td><td></td><td></td><td>MAIS</td><td></td><td></td></tr><tr><td>SP-15 DA</td><td>10.12</td><td>[13.06]</td><td>(1.95)</td><td>83.12</td><td>[88.37]</td><td>(68.50)</td><td>85.76</td><td>[90.54]</td><td>(72.45)</td></tr><tr><td>SP-15 HA</td><td>16.08</td><td>[21.26]</td><td>(1.67)</td><td>80.40</td><td>[89.62]</td><td>(54.72)</td><td>86.89</td><td>[91.90]</td><td>(72.93)</td></tr><tr><td>NP-15 DA</td><td>15.55</td><td>[20.68]</td><td>(1.26)</td><td>79.26</td><td>[82.19]</td><td>(71.10)</td><td>75.19</td><td>[81.82]</td><td>(56.72)</td></tr><tr><td>NP-15 HA</td><td>19.67</td><td>[26.25]</td><td>(1.33)</td><td>77.35</td><td>[79.03]</td><td>(72.67)</td><td>79.32</td><td>[85.59]</td><td>(61.91)</td></tr><tr><td>ZP-26 DA</td><td>65.12</td><td>[83.12]</td><td>(59.08)</td><td>87.29</td><td>[92.34]</td><td>(85.59)</td><td>89.71</td><td>[95.81]</td><td>(87.66)</td></tr><tr><td>ZP-26 HA</td><td>53.42</td><td>[81.67]</td><td>(43.93)</td><td>90.10</td><td>[91.45]</td><td>(89.64)</td><td>89.12</td><td>[96.41]</td><td>(86.67)</td></tr><tr><td>Mean</td><td>29.99</td><td>[41.01]</td><td>(18.20)</td><td>81.755</td><td>[87.17]</td><td>(73.70)</td><td>84.33</td><td>[90.35]</td><td>(73.06)</td></tr></table>

Note: [ ] and ( ) indicate an average estimation accuracy before the California electricity crisis and the one during the crisis, respectively.

Finding 1 Table 3 indicates that the proposed MAIS (average estimation accuracy= 84.33%) estimates the dynamic price fluctuation of electricity as well as the other two well-known methods (GA: 29.99% and NN: 82.98%). This result indicates that MAIS performs as well as NN in terms of price estimation.

Finding 2 Richter et al. [20] have reported that GA is useful only when the power market is not volatile. The low estimation accuracy (=18.20%) of GA in Table 3 is because there is large price volatility during the California electricity crisis. This study confirms their finding on GA.

Finding 3 The average estimation accuracy of MAIS before the electricity crisis is 90.35%, while the estimation accuracy during the crisis is 73.06%. The difference can be found in NN, as well. There is a big estimation gap between the two periods. This indicates that there is a significant difference between observed market prices and MAIS estimates during the electricity crisis period.

As a visual illustration, Fig. 12 compares the fluctuation of observed electricity prices with the estimated ones obtained by MAIS in the SP-15 (DA) before the electricity crisis (before May 2000). Fig. 13 depicts such a comparison during the crisis (after May 2000).

The difference (73.06% and 90.35%) in the estimation accuracy of MAIS can be visually confirmed in Figs. 12 and 13. Both figures compare the price fluctuation of observed prices with that of the price estimates in the two periods (before and during the crisis). It is important to note that the price range of Fig. 12 (from \$25/MWH to \$40/MWH) is much smaller than that of Fig. 13 (from \$30/MWH to \$700/MWH).

5.4. Learning speed (convergence) of bidding rates and mark-up rates

Figs. 14–18 depict the learning (convergence) speed of the bidding rate and mark-up rates of the 121st generator and those of the 20th wholesaler as an illustrative example.

![](/api/attachments/4P4AEDVR/fulltext/images/cccdadb8297b9d5d0cfc529ea8bd1849799e94f9f9b2cc884b48acfe93ebfce8.jpg)  
Fig. 12. Observed price of SP-15 (DA) and MAIS estimate (before crisis).

![](/api/attachments/4P4AEDVR/fulltext/images/966d7095ef41087fd386270667d51f6449cf5c1cc76d9e6ebbd4ff871d7c75e1.jpg)

Fig. 13. Observed price of SP-15 (DA) and MAIS estimate (during crisis).  
![](/api/attachments/4P4AEDVR/fulltext/images/814b86cca75ba1e034e0e44ced4209301621154e01421cefcbb04aeeaab808c5.jpg)  
Fig. 14. Learning speed of α (generator's bidding rate in DA).

Finding 4 All the five decision bidding rates and markup rates fluctuate and then gradually converge before the California energy crisis.

Those parameters fluctuate drastically during the electricity crisis (after May 2000).

Table 4 summarizes the average learning (convergence) speed and the volatility of each bidding rate and mark-up rate before and during the California electricity crisis. The average and volatility of iterations are listed in Table 4, as well. Here, the averages of the first three (α, β, η) imply the means of 964 generators and the averages of the remaining two (δ, λ) imply the means of 48 wholesalers.

![](/api/attachments/4P4AEDVR/fulltext/images/5fadf8bb9a31c2ec0ae9782edfe6cf8c0421e5ee087215c183486e32e1340c1d.jpg)  
Fig. 15. Learning speed of β (generator's mark-up rate in DA).

![](/api/attachments/4P4AEDVR/fulltext/images/30cc35e17716a4ddfd2ff23864ca9c6de1610da33d3a814b0316c4a6243ae438.jpg)  
Fig. 16. Learning speed of η (generator's mark-up rate in RT).

![](/api/attachments/4P4AEDVR/fulltext/images/83c969df4aa22a6a7eeb2c0cb670634cf844fe1999913faef7acce91fe4454e5.jpg)  
Fig. 17. Learning speed of δ (wholesaler's bidding rate in DA).

![](/api/attachments/4P4AEDVR/fulltext/images/08a6e6ca5800aab769ef6bcb32dd847891c88bb02c359dd74798f38c939adbcb.jpg)  
Fig. 18. Learning speed of λ (wholesaler's mark-up rate in DA).

Finding 5 The values of the bidding rates and mark-up rates before the electricity crisis are lower than those during the crisis in terms of these final values, averages and volatilities. This indicates that all the traders during the crisis have made higher bidding prices and amounts than their bids before the crisis.

Finding 6 A convergence rate of the bidding rates and mark-up rates indicates the learning speed of each trader. The learning speeds during the electricity crisis are almost twice as long as those before the crisis. This implies that traders have experienced a difficult time to adjust themselves to the drastic change of market price during the California electricity crisis.

## 6. Conclusion and future extension

MAIS can be used for analyzing and understanding a dynamic price change in the US wholesale power market. Traders can use the software as an effective DSS tool by modeling and simulating a power market. The software uses various features of DSS by creating a framework for assessing new trading strategies in a competitive electricity trading environment. The practicality of the software is confirmed by comparing its estimation accuracy with those of other methods (e.g., neural network and genetic algorithm). The software has been applied to a data set regarding the California electricity crisis in order to examine whether the learning (convergence) speed of traders is different between the two periods (before and during the crisis). Thus, the applicability of the proposed simulator is confirmed in this study.

There are some research issues related to the proposed simulator (MAIS), all of which need to be explored in the future. First, the learning algorithm incorporated into the simulator needs to be further extended by incorporating the Bayes theory into the proposed learning process of traders. Second, a game theoretic approach adds another perspective on the learning capabilities addressed in this study. Finally, the proposed simulator should be extended to network capabilities so that a market operator exists in one place and traders exist physically in other places. They are linked on Internet, as designed in the software. An important task to be explored in the network-based research extension is to investigate how traders build consensus on the market clearing prices under the price monitoring process of regulatory authority. These issues are important future research tasks of this study.

## Acknowledgement

This research is supported by Telecommunication Advancement Foundation.

## Appendix A. Market clearing scheme for multiple zones

In this study, a wholesale power exchange market is separated into multiple zones based on the geographic location of nodes and transmission grid structure. Each zone consists of several generators and loads. There are two types of transmission connections in the power market: intra-zonal link and inter-zonal link. Intra-zonal links are connections that exist among generators and wholesalers within a zone. Inter-zonal links are connections that exist between zones. A common MCP (Market Clearing Price) may exist if these zones are linked with each other. However, if these zones are functionally separated by a capacity limit on an interconnection line or an occurrence of congestion, then these zones have different LMPs (Locational Marginal Prices) as MCP.

Table 4  
Learning speed (convergence) of bidding rates and mark-up rates

<table><tr><td rowspan="3"></td><td colspan="5">Before crisis</td><td colspan="5">During crisis</td></tr><tr><td rowspan="2">Final value</td><td colspan="2">Values</td><td colspan="2"># of iterations</td><td rowspan="2">Final value</td><td colspan="2">Values</td><td colspan="2"># of iterations</td></tr><tr><td>AVG</td><td>Volatility</td><td>AVG</td><td>Volatility</td><td>AVG</td><td>Volatility</td><td>AVG</td><td>Volatility</td></tr><tr><td>α</td><td>0.59</td><td>0.39</td><td>0.22</td><td>62.49</td><td>21.98</td><td>0.72</td><td>0.43</td><td>0.34</td><td>119.24</td><td>23.27</td></tr><tr><td>β</td><td>0.76</td><td>0.54</td><td>0.25</td><td>69.27</td><td>17.53</td><td>0.83</td><td>0.69</td><td>0.40</td><td>142.37</td><td>20.33</td></tr><tr><td>η</td><td>0.59</td><td>0.49</td><td>0.17</td><td>60.25</td><td>23.44</td><td>0.91</td><td>0.64</td><td>0.33</td><td>153.12</td><td>10.21</td></tr><tr><td>δ</td><td>0.75</td><td>0.53</td><td>0.24</td><td>53.16</td><td>12.33</td><td>0.85</td><td>0.59</td><td>0.22</td><td>106.82</td><td>19.24</td></tr><tr><td>λ</td><td>0.73</td><td>0.54</td><td>0.22</td><td>66.03</td><td>16.77</td><td>0.93</td><td>0.67</td><td>0.25</td><td>161.74</td><td>5.34</td></tr></table>

Considering a capacity limit on a transmission link, this study pays attention to the following concerns:

(a) The MCP is determined by supply–demand even if a transmission link is limited. That is important because we need to pay attention to only the supply–demand relationship in estimating the wholesale market price of electricity, even under an occurrence of congestion. [It is assumed that all physical losses are ignored and all voltage magnitudes are equal in the proposed simulator. The reality is different from this assumption. However, the engineering issues are not explored in this study, because this study limits itself to the economics on power trading. See Chapter 3–4 of [27] for a detailed description on ancillary services (e.g., voltage stability, transmission security and economic dispatch).]

(b) A line limit on transmission or an occurrence of congestion influences the selection of generators that can participate in a market clearing process of each zone. When the capacity limit exists on links, ISO often selects expensive generator(s) for power supply. An expensive generator(s) is usually excluded from a supply side if a line limit or congestion does not occur in transmission. As a consequence of selecting an expensive generator, a MCP is usually increased from the one without congestion.

Fig. A-1 illustrates an algorithm for clearing a wholesale market with multiple zones. This algorithm can be applied to both DA and RT. In the algorithm, a wholesale market is separated into Z zones $( z { = } 1 , 2 , . . . , Z )$ . The algorithm considers, first, that all links are not limited (so, no congestion) and every zone is connected to one another by means of a link. Then, we drop this assumption to investigate the influence of a capacity limit on the market clearing scheme. Hereafter, we incorporate the subscript “z” into each symbol to indicate the z-th zone.

As a preprocessing step, ISO forecasts a total demand $( D _ { ( z ) t } )$ for the z-th zone at the t-th period. The total demand can be specified as $\begin{array} { r } { D _ { ( z ) t } = \sum _ { j } d _ { j ( z ) t } , } \end{array}$ where $d _ { j ( z ) t }$ is the demand forecast from the j-th wholesaler in the z-th zone at the t-th period. The total supply $( \sum S _ { ( z ) t } )$ is obtained from all generators in each zone via $\begin{array} { r } { S _ { ( z ) t } { = } \sum _ { i } s _ { i ( z ) t } ^ { m } , } \end{array}$ where $s _ { i ( z ) t } ^ { m }$ is the maximum generation capacity of the i-th generator in the z-th zone at the t-th period. As mentioned previously, this study assumes that the total sum of generation capacities $( \sum S _ { ( z ) t } )$ should be larger than or equal to that of total consumptions $( D _ { ( z ) t } )$ . An excess amount of power supply in the z-th zone can be specified by $E _ { ( z ) t } { = } S _ { ( z ) t } { - } D _ { ( z ) t } .$ A zone is said to be cleared in a market if all the load requirements of the zone are satisfied for the market. If $S _ { ( z ) t } { \geq } D _ { ( z ) t } ,$ then the z-th zone can be cleared like a self-maintained market entity. Otherwise $( S _ { ( z ) t } { < } D _ { ( z ) t } )$ , the z-th zone is not cleared. In this case, the zone needs to generate an additional amount of electricity by using extra (usually expensive) generators within its own zone and/or obtaining electricity from other linked zone(s). In the former case, ISO needs to re-examine a problem of generator selection and dispatch scheduling within a zone. In the latter case, ISO needs to examine whether unused generators are available in other zones.

This initial clearing process of Fig. A-1 continues sequentially for all zones, as depicted in the upper part (above the dotted line) of the figure. In the figure, AG represents a set of generators that are allocated for current generation. UAG represents a set of generators which are not allocated for current generation. C represents a set of cleared zones. NC represents a set of zones that are not cleared. At the end of this initial market clearing process, all the zones are classified into either cleared (C) or notcleared (NC). Note that a “win” of a generator implies that the generator bids in a market and obtained a generation opportunity.

After the initial clearing process is completed, ISO needs to clear all zones where demand is larger than supply. All these zones belong to the set (NC). Hereafter, the market clearing process depends upon whether there is any capacity limit on the links. First, we describe an algorithm under no line limit on transmission. See the south-west corner (no line limit) of Fig. A-1. To clear the z-th zone in NC, ISO prepares a market for the notcleared zone where all unused generators in UAG may participate in its bidding process. Since there is no line limit on transmission, the bidding process of those generators works as a single market entity.

The south-east corner (under line limit) of Fig. A-1 indicates an algorithmic process within ISO when the z-th zone is not cleared and a link between the not-cleared zone and other zones have a capacity limit on its transmission. To clear the market in the not-cleared zone, ISO identifies not only all generators in the not-cleared zone (NC) but also unallocated generators (UAG) in other zones. Such a group of generators is expressed by PG (Participating Generators). In this case, ISO needs to consider both (a) whether a link connects between the notcleared z-th zone and the other zones and (b) whether the link has a capacity limit.

An issue (all generators should be connected to the notcleared z-th zone through a link) is solved by identifying a group of generators whose zones have a link to the notcleared zone. This group of generators is expressed by TCG (Transmission Connected Generators). Consequently, a group of generators, which can participate into the market clearing process of the z-th zone, is selected from

MCPG (Market Clearing Participating Generators) that is expressed by an intersection between PG and TCG. Thus, the z-th zone is cleared by using all generators in MCPG.

Based upon the market clearing result, the four sets (C, NC, AG, and UAG) are updated in the data base within the proposed simulator, as depicted in Fig. A-1.

![](/api/attachments/4P4AEDVR/fulltext/images/1f594205cdc922733d26e287eee7a3692389e8bd460f094ce7b7695662501578.jpg)  
Fig. A-1: Market Clearing Scheme for Multiple Zones. Legend: AG (Allocated Generator), UAG (Unallocated Generator), C (Cleared Zone), NC (Not Cleared Zone), PG (Participating Generator), TCG (Transmission Connected Generator) and MCPG (Market\_Clear Participating Generator).

## Appendix B. Adaptive Behavior of Traders Equipped with Learning Capabilities

In the proposed simulator, each market consists of many artificial traders who can accumulate knowledge from their bidding results in order to adjust their proceeding bidding strategies. Their adaptive learning process is separated into (a) a Knowledge Accumulation (KA) process and (b) an Own-Bidding (OB) process. The KA process provides each trader with not only a forecasted estimate on wholesale power price and amount, but also a win–loss experience from their biddings. The KA process can be considered as a training process for each trader. After the learning process in the KA process is completed, each trader starts his bidding decisions based upon previous trading experience. All traders constantly update and accumulate their knowledge (experiences) at each trade. The bidding and learning process is considered as the OB process. The bidding experience in the OB process is incorporated into the KA process as updated information.

Reward to Trader: Table A-1 summarizes a reward of the i-th generator. Each cell of Table A-1 indicates a winning reward of the generator. For example, $\mathrm { i f } \hat { p } _ { ( z ) t } ^ { 1 } { < } p _ { i ( z ) t } ^ { 1 } ,$ then the generator cannot have any chance to generate electricity, so having no reward in the DA market. Conversely, if $\hat { p _ { ( z ) t } } { \geq } \bar { p _ { i ( z ) t } } ,$ , then the generator receives a reward $( \hat { p } _ { ( z ) t } ^ { 1 } - \mathbf { M } \mathbf { C } _ { i ( z ) t } ^ { 1 } ) \hat { s } _ { i ( z ) t } ^ { 1 } ,$ , as listed in the cell under $\mathrm { \Delta ^ { 6 6 } } \mathrm { B A } ^ { \prime \prime }$ and “within the $z { \mathrm { - } } Z { \mathrm { 0 n e } } ^ { \prime 3 }$ . In a similar manner, if $\hat { p } _ { ( z ) t } ^ { 0 } { \geq } p _ { i ( z ) t } ^ { 0 }$ in RT, then the generator obtains $( \hat { p } _ { ( z ) t } ^ { 0 } - \mathrm { M C } _ { i ( z ) t } ^ { 0 } )$ $\hat { s } _ { i ( z ) t } ^ { 0 } .$

In addition to the sale within the z-th zone, the generator sells electricity to another zone (i.e., the z′-th zone). The generator can obtain a reward from the z′-th zone. In this case, the reward becomes $( \hat { p } _ { ( z ^ { \prime } ) t } ^ { 1 } - \mathbf { M } \mathbf { C } _ { i ( z ) t } ^ { 1 } )$ $\hat { S } _ { i ( z  z ^ { \prime } ) t } \}$ in DA and $( \hat { p } _ { ( z ^ { \prime } ) t } ^ { 0 } - \mathbf { M } \mathbf { C } _ { i ( z ) t } ^ { 0 } ) \hat { s } _ { i ( z  z ^ { \prime } ) t } ^ { \bar { 0 } }$ in RT. Here, $\hat { s } _ { i ( z  z ^ { \prime } ) t } ^ { 1 }$ and $\hat { s } _ { i ( z  z ^ { \prime } ) t } ^ { 0 }$ are the amount of electricity transmitted in DA and RT, respectively, from the z-th zone to the $z ^ { \prime } { \mathrm { - t h } }$ zone at the t-th period. The transmission from the z-th zone to the z′-th zone is associated with a transmission cost that is listed as $\mathrm { T C } _ { ( z  z ^ { \prime } ) t }$ . The total reward $( R _ { i ( z ) t } )$ is determined by subtracting the transmission cost (under an occurrence of the inter-transmission) from a sum of these sales. This study considers that the transmission cost within a same zone is zero. Here, $\mathrm { T C } _ { ( z  z ^ { \prime } ) t }$ stands for a unit transmission cost (\$/MWH) that is associated with physical losses, ancillary services and others related to transmission services from the z-th zone to $z ^ { \prime } { \mathrm { - t h } }$ zone. The cost in Table A-1 indicates a total transmission cost (\$).

Table A-1  
Reward for generator

<table><tr><td colspan="2">Reward = Sale - Cost</td><td>DA</td><td>RT</td></tr><tr><td rowspan="2">Sale</td><td>Within the z-zone</td><td> $\left\{ \hat{p}_{(z)t}^{1} - \text{MC}_{i(z)t}^{1} \right\} \hat{s}_{i(z)t}^{1}$ </td><td> $\left\{ \hat{p}_{(z)t}^{0} - \text{MC}_{i(z)t}^{0} \right\} \hat{s}_{i(z)t}^{0}$ </td></tr><tr><td>Transmission (z→z&#x27;)</td><td> $\left\{ \hat{p}_{(z')t}^{1} - \text{MC}_{i(z)t}^{1} \right\} \hat{s}_{i(z \rightarrow z')t}^{1}$ </td><td> $\left\{ \hat{p}_{(z')t}^{0} - \text{MC}_{i(z)t}^{0} \right\} \hat{s}_{i(z \rightarrow z')t}^{0}$ </td></tr><tr><td>Cost</td><td></td><td colspan="2"> $\left\{ \hat{s}_{i(z \rightarrow z')t}^{1} + \hat{s}_{i(z \rightarrow z')t}^{0} \right\} \text{TC}_{(Z \rightarrow Z')t}$ </td></tr></table>

Next, a reward to the j-th wholesaler in the z-th zone at the t-th period can be specified as follows: $\operatorname { I f } { \hat { p } } _ { ( z ) t } ^ { 1 } >$ $p _ { j ( z ) t } ^ { 1 } ,$ then the wholesaler cannot access electricity through the DA market. Conversely, if $\hat { p } _ { ( z ) t } ^ { 1 } { \le } p _ { j ( z ) t } ^ { 1 } ,$ then the wholesaler can obtain electricity from the DA market and sell the electricity to end users. Similarly, if $\hat { d } _ { j ( z ) t } ^ { 0 } 2 0$ , then the wholesaler can access electricity in the RT market. An opposite case can be found i $\mathrm { \partial } \cdot \hat { d } _ { j ( z ) t } ^ { 0 } { = } 0$ The wholesaler usually provides electricity whose retail price is ruled by a regulatory agency(s). Hence, let $p ( R ) _ { ( z ) t }$ be the retail price of the z-th zone at the t-th period. Then, the reward for the wholesaler can be specified in Table A-2.

Table A-2  
Reward for wholesaler

<table><tr><td>Reward</td><td>DA</td><td>RT</td></tr><tr><td></td><td>$ \left\{p(R)_{(z)t}-\hat{p}_{(z)t}^{1}\right\}\hat{d}_{j(z)t}^{1} $</td><td>$ \left\{p(R)_{(z)t}-\hat{p}_{(z)t}^{0}\right\}\hat{d}_{j(z)t}^{0} $</td></tr></table>

Adaptive Sigmoid Decision Rule: In the adaptive learning process of the proposed simulator, each trader constantly looks for an increase in an estimated winning probability. In other words, the trader looks for a combination of unknown bidding rates and markup rates that can increase a winning probability. The win or lose of a trade is considered as a binary response. To express an occurrence of the binary response, a sigmoid model is widely used to predict a winning probability. Mathematically, the probability cumulative function of the sigmoid model is expressed by $\begin{array} { r } { F ( \sigma ) = \int _ { - \infty } ^ { \sigma } e ^ { u } / ( 1 + e ^ { u } ) ^ { 2 } d u = 1 / ( 1 + e ^ { - \sigma } ) } \end{array}$ The <sup>-</sup>win or loss status of the i-th generator of the z-th zone at the t-th period is predicted by the following linear probability model:

$$
R _ {i (z) t} = c _ {0} + c _ {1} \alpha_ {i (z) t} + c _ {2} \beta_ {i (z) t} + c _ {3} \eta_ {i (z) t} + \varepsilon\tag{A - 1}
$$

Here, $R _ { i ( z ) t }$ is a reward obtained by the i-th generator. Parameters to be estimated are denoted by c. An observational error is listed as ε. The parameters are unknown and hence, need to be estimated by OLS (Ordinary Least Squares) regression. The winning probability (Prob) can be specified as follows:

$$
\begin{array}{r l} \operatorname{Prob} (\text { WIN }) & = \operatorname{Prob} (R _ {i (z) t} \geq 0) \\ & = \frac {\operatorname{EXP} (\hat {c} _ {0} + \hat {c} _ {1} \alpha_ {i (z) t} + \hat {c} _ {2} \beta_ {i (z) t} + \hat {c} _ {3} \eta_ {i (z) t})}{1 + \operatorname{EXP} (\hat {c} _ {0} + \hat {c} _ {1} \alpha_ {i (z) t} + \hat {c} _ {2} \beta_ {i (z) t} + \hat {c} _ {3} \eta_ {i (z) t})}. \end{array} \tag {A-2}
$$

The symbol (^) indicates a parameter estimate obtained by OLS. The above equations suggest that the winning probability can be predicted immediately from the parameter estimates of the sigmoid model.

The reward of the j-th wholesaler of the z-th zone at the t-th period can be estimated by the following linear probability model:

$$
R _ {j (z) t} = c _ {0} + c _ {1} \delta_ {j (z) t} + c _ {2} \lambda_ {j (z) t} + \varepsilon .\tag{A - 3}
$$

Hence, the winning probability is specified as

$$
\begin{array}{l} \text { Prob } (\text { WIN }) = \text { Prob } (R _ {j (z) t} \geq 0) \\ = \frac {\text { EXP } (\hat {c} _ {0} + \hat {c} _ {1} \delta_ {j (z) t} + \hat {c} _ {2} \lambda_ {j (z) t})}{1 + \text { EXP } (\hat {c} _ {0} + \hat {c} _ {1} \delta_ {j (z) t} + \hat {c} _ {2} \lambda_ {j (z) t})}. \end{array}\tag{A - 4}
$$

The KA process of the wholesaler provides three parameter estimates of the sigmoid model. Two $( \hat { c } _ { 1 }$ and $\hat { c } _ { 2 } )$ of the three parameter estimates are important in determining the bidding strategies of the wholesaler. If the parameter estimate is positive, the wholesaler should increase its corresponding decision variable in order to enhance a winning probability. Conversely, an opposite strategy is needed if the estimate is negative. Thus, the sign of each parameter estimate provides information regarding which decision variable needs to be increased or decreased. However, the winning probability, obtained from the sigmoid model, does not immediately imply that the trader can always win in a wholesale market with the estimated probability. That is a theoretical guess. The win or lose is determined through the DA and RT market mechanism.

Exponential Utility function: It is assumed that all the traders have an exponential utility function. The utility function represents a risk aversion preference. Mathematically, the exponential utility function employed in this study is expressed by $U ( R _ { j ( z ) t } ) { = } 1 - \mathrm { E X P } ( - \zeta R _ { j ( z ) t } )$ on $R _ { j ( z ) t } { \geq } 0$ , where $\zeta$ indicates a parameter to express the level of risk aversion. The utility function is a smooth concave function. Different $\zeta$ values represent different risk-hedge behaviors of traders.

Returning to Eq. (A-3), the utility value $( \phi _ { j ( z ) t } )$ for a reward $( R _ { j ( z ) t } )$ of the wholesaler is given by $\phi _ { j ( z ) t } = 1$ $- \mathrm { E X P } ( - \zeta \tilde { R _ { j ( z ) t } } )$ . Hence, given $\phi _ { j ( z ) t } ,$ the reward is expressed by

$$
\begin{array}{c} R _ {j (z) t} = - \mathrm{ln} (1 - \phi_ {j (z) t}) / \zeta \\ = \hat {c} _ {0} + \hat {c} _ {1} \delta_ {j (z) t} + \hat {c} _ {2} \lambda_ {j (z) t}, \end{array}\tag{A - 5}
$$

where $^ { \circ } \mathrm { l n } ^ { \circ }$ stands for a natural logarithm. After obtaining the parameter estimates of the sigmoid model, along with a given utility value or its range; the wholesaler considers a bidding strategy for the next period. In this study, the bidding strategy for the next period (t + 1) is specified as follows: $\lambda _ { j ( z ) t } + 1 \underset { \circ } {  } \lambda _ { j ( z ) t }$ $+ \tau \Delta _ { j ( z ) t } ^ { \lambda } )$ and $\delta _ { j ( z ) t + 1 } \longrightarrow \delta _ { j ( z ) \underline { { { t } } } } + \tau \Delta _ { j ( z ) t } ^ { \delta } ,$ where $\Delta _ { j ( z ) t } ^ { \lambda } { = } \lambda _ { j ( z ) }$ ${ \bf \Xi } _ { t } ^ { \mathrm { U } } - \bar { \lambda } _ { j ( z ) t } ^ { \mathrm { L } ^ { ' } }$ and $\Delta _ { j ( z ) t } ^ { \delta } { = } \delta _ { j ( z ) t } ^ { \mathrm { U } } { - } \delta _ { j ( z ) t } ^ { \mathrm { L } }$ . The prescribed quantities $( \lambda _ { j ( z ) t } ^ { \mathrm { U } }$ and $\lambda _ { j ( z ) t } ^ { \mathrm { L } } )$ indicate the upper and lower bounds on $\lambda _ { j ( z ) t } ,$ respectively. The other prescribed quantities $( \delta _ { j }$ ${ { \bf \Lambda } _ { ( z ) t } } ^ { \mathrm { ~ U ~ } }$ and $\lambda _ { j ( z ) t } ^ { \mathrm { L } ^ { - } } )$ also indicate the upper and lower bounds on $\delta _ { j ( z ) t } .$ . In this case, we need to identify these quantities from the upper and lower bounds of previous bidding amounts. An unknown parameter (τ) indicates the magnitude of such a bidding change. Along with the changes and given $\phi _ { j ( z ) t + 1 } , \mathrm { E q . } \ ( \mathrm { A } { - } 5 )$ becomes

$$
\begin{array}{r l} - \ln (1 - \phi_ {j (z) t + 1}) / \zeta & = \hat {c} _ {0} + \hat {c} _ {1} (\delta_ {j (z) t} \\ & \quad + \tau \Delta_ {j (z) t} ^ {\delta}) + \hat {c} _ {2} (\lambda_ {j (z) t} \\ & \quad + \tau \Delta_ {j (z) t} ^ {\lambda}). \end{array}\tag{A-6}
$$

From Eq. (A-6), the magnitude variable is determined by

$$
\begin{array}{l} \tau = - \left(\ln (1 - \phi_ {j (z) t + 1}) / \zeta + \hat {c} _ {0} + \hat {c} _ {1} \delta_ {j (z) t} + \hat {c} _ {2} \lambda_ {j (z) t}\right) \\ \div \left(\hat {c} _ {1} \Delta_ {j (z) t} ^ {\delta} + \hat {c} _ {2} \Delta_ {j (z) t} ^ {\lambda}\right) \end{array} \tag {A}\tag{A - 7}
$$

Thus, we can determine the magnitude of a bidding change (τ) along with a previously determined strategic direction. Different utility values produce different magnitudes of $\tau ,$ consequently generating different bidding prices and amounts for the j-th wholesaler. [The description on the utility function of the wholesaler can be extended to that of the i-th generator in a similar manner.]

Algorithm: Based upon the signs of parameter estimates of the sigmoid model obtained from the KA process, the j-th wholesaler in the z-th zone has nine different bidding strategies (with t = 1 as the start):

Step 1: Set initial bidding variables from the KA process. A forecasting method (e.g., moving average and exponential smoothing) with different time periods is used to compute the initial bidding variables. Also, set the upper $( \delta _ { j ( z ) t } ^ { \mathrm { U } }$ and $\lambda _ { j ( z ) t } ^ { \mathrm { U } } )$ and lower $( \delta _ { j ( z ) t } ^ { \mathrm { L } }$ and $\lambda _ { j ( z ) t } ^ { \textrm { L } } )$ limits from the KA process.

Step 2: Use OLS to obtain parameter estimates of the sigmoid model from the KA process. Obtain the magnitude of a bidding change (τ) from an exponential utility function.

Step 3: Based upon the signs of parameter estimates, the decision variables on bidding are changed as follows:

$$
\begin{array}{l} \text {(a) If} \hat {c} _ {1} > 0 \& \hat {c} _ {2} > 0, \text {then} (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ = \Big \{\delta_ {j (z) t} + \tau \Delta_ {j (z) t} ^ {\delta}, \lambda_ {j (z) t} + \tau \Delta_ {j (z) t} ^ {\lambda} \Big \}. \end{array}
$$

$$
\begin{array}{l} \text {(b) If} \hat {c} _ {1} > 0 \& \hat {c} _ {2} = 0, \text { then } (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ = \Big \{\delta_ {j (z) t} + \tau \Delta_ {j (z) t} ^ {\delta}, \lambda_ {j (z) t} \Big \}. \end{array}
$$

$$
\begin{array}{l} \text {(c) If} \hat {c} _ {1} > 0 \& \hat {c} _ {2} <   0, \text {then} (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ = \Big \{\delta_ {j (z) t} + \tau \Delta_ {j (z) t} ^ {\delta}, \lambda_ {j (z) t} - \tau \Delta_ {j (z) t} ^ {\lambda} \Big \}. \end{array}
$$

$$
\begin{array}{l} \text {(d) If} \hat {c} _ {1} = 0 \& \hat {c} _ {2} > 0, \text { then } (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ \qquad = \Big \{\delta_ {j (z) t}, \lambda_ {j (z) t} + \tau \Delta_ {j (z) t} ^ {\lambda} \Big \}. \end{array}
$$

$$
\begin{array}{l} \text {(e) If} \hat {c} _ {1} = 0 \& \hat {c} _ {2} = 0, \text {then} (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ \qquad = \big \{\delta_ {j (z) t}, \lambda_ {j (z) t} \big \}. \end{array}
$$

$$
\begin{array}{l} \text {(f) If} \hat {c} _ {1} = 0 \& \hat {c} _ {2} <   0, \text {then} (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ \qquad = \Big \{\delta_ {j (z) t}, \lambda_ {j (z) t} - \tau \Delta_ {j (z) t} ^ {\lambda} \Big \}. \end{array}
$$

$$
\begin{array}{l} \text {(g) If} \hat {c} _ {1} <   0 \& \hat {c} _ {2} > 0, \text {then} (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ = \Big \{\delta_ {j (z) t} - \tau \Delta_ {j (z) t} ^ {\delta}, \lambda_ {j (z) t} + \tau \Delta_ {j (z) t} ^ {\lambda} \Big \}. \end{array}
$$

$$
\begin{array}{l} \text {(h) If} \hat {c} _ {1} <   0 \& \hat {c} _ {2} = 0, \text { then } (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ = \Big \{\delta_ {j (z) t} - \tau \Delta_ {j (z) t} ^ {\delta}, \lambda_ {j (z) t} \Big \}. \end{array}
$$

$$
\begin{array}{l} \text {(i) If} \hat {c} _ {1} <   0 \& \hat {c} _ {2} <   0, \text {then} (\delta_ {j (z) t + 1}, \lambda_ {j (z) t + 1}) \\ = \Big \{\delta_ {j (z) t} - \tau \Delta_ {j (z) t} ^ {\delta}, \lambda_ {j (z) t} - \tau \Delta_ {j (z) t} ^ {\lambda} \Big \}. \end{array}
$$

Step 4: Compute $d _ { j ( z ) t } ^ { 1 }$ and $p _ { j ( z ) t } ^ { 1 } ,$ using $( \delta _ { j ( z ) t } , \lambda _ { j ( z ) t } ) .$ and submit the bids to the DA market. $\operatorname { I f } t = T ,$ then stop. Otherwise, go to Step 5.

Step 5: If the wholesaler loses, then drop information on the current bidding variables and go to Step 1. If the wholesaler wins, then go to Step 6.

Step 6: Add information on the current bidding variables into the KA process and go to Step 1.

Note that (a) even if a trader keeps the same strategy, his/her market result may be different from the previous one, because the wholesale market determines the price and amount of power allocation. (b) In Step 3 for each generator, the generator has $2 7 \ \left( = 3 \times 3 \times 3 \right)$ bidding strategies, as structured for the wholesaler. The three parameters need to be considered in the algorithmic steps for the generator. (c) The algorithm proposed for DA can be applied to the bidding price and quantity of a generator for RT in a similar manner.

## References

[1] I. Acronymics, Agentbuilder 1.4, Acronymics, Inc., 2004.

[2] K.J. Adams, D.A. Bell, L.P. Maguire, J. McGregor, Knowledge discovery from decision tables by the use of multiple-valued logic, Artificial Intelligence Review 19 (2) (2003) 153–176.

[3] B.S. Ahn, S.S. Cho, C.Y. Kim, Integrated methodology of rough set theory and artificial neural network for business failure prediction, Expert Systems with Applications 18 (2) (2000) 65–74.

[4] F. Bellifemine, A. Poggi, G. Rimassa, Developing multi-agent systems with a FIPA-compliant agent framework, Software, Practice and Experience 31 (2) (2001) 103–128.

[5] M. Beynon, S. Rasmequan, S. Russ, A new paradigm for computer-based decision support, Decision Support Systems 33 (2) (2002) 127–142.

[6] T. Bui, J. Lee, Agent-based framework for building decision support systems, Decision Support Systems 25 (3) (1999) 225–237.

[7] C. Changchit, C.W. Holsapple, D.L. Madden, Supporting managers' internal control evaluations: an expert system and experimental results, Decision Support Systems 30 (4) (2001) 437–449.

[8] R.R. Hashemi, L.A. Le Blanc, C.T. Rucks, A. Rajaratnam, A hybrid intelligent system for predicting bank holding structures, Journal of Operational Research 109 (2) (1998) 390–402.

[9] K.J. Kim, I. Han, The extraction of trading rules from stock market data using rough sets, Expert Systems 18 (4) (2001) 194–202.

[10] P. Klemperer, Auction theory: a guide to the literature, Journal of Economic Surveys 13 (3) (1999) 227–286.

[11] T.P. Liang, J.S. Huang, Framework for applying intelligent agents to support electronic trading, Decision Support Systems 28 (4) (2000) 305–317.

[12] Y. Luo, K. Liu, D.N. Davis, A multi-agent decision support system for stock trading, IEEE Network 16 (1) (2002) 20–27.

[13] T.E. McKee, T. Lensberg, Genetic programming and rough sets: a hybrid approach to bankruptcy classification, European Journal of Operational Research 138 (2) (2002) 436–451.

[14] M. North, G. Conzelmann, V. Koritarov, C. Macal, P. Thimmapuram, T. Veselka, E-laboratories: agent-based modeling of electricity markets, Proceedings of the 2002 American Power Conference, Chicago, IL, 2002.

[15] S. Oren, J.N. Jiang, Challenges of restructuring the power industry. Decision Support Systems. 40, 3–4 (2005), 407–408 and 505–506.

[16] M. Ozbayrak, R. Bell, A knowledge-based decision support system for the management of parts and tools in FMS, Decision Support Systems 35 (4) (2003) 487–515.

[17] S. Park, V. Sugumaran, Designing multi-agent systems: a framework and application, Expert Systems with Applications 28 (2) (2005) 259–271.

[18] Z. Pawlak, AI and intelligent industrial applications: the rough set perspective, Cybernetics and Systems 31 (3) (2000) 227–252.

[19] I.R. Praca, C. Ramos, Z. Vale, M. Cordeiro, Mascem: a multiagent system that simulates competitive electricity markets, IEEE Intelligent Systems 18 (6) (2003) 54–60.

[20] C.W. Richter, G.B. Sheble, D. Ashlok, Comprehensive bidding strategies with genetic programming/finite state automata, IEEE Transactions on Power Systems 14 (1999) 1207–1212.

[21] T. Samad, S.A. Harp, SEPIA 1, Honeywell Technology Center, 1996.

[22] S. Schocken, G. Ariav, Neural networks for decision support: problems and opportunities, Decision Support Systems 11 (5) (1994) 393–414.

[23] M. Shahidehpour, H. Yamin, Z. Li, Market Operations in Electric Power Systems: Forecasting, Scheduling and Risk Management, John Wiley & Sons, 2002.

[24] G.B. Sheblâe, Computational Auction Mechanisms for Restructured Power Industry Operation, Kluwer, Boston, 1999.

[25] Z. Shi, H. Zhang, Y. Cheng, Y. Jiang, Q. Sheng, Z. Zhao, MAGE: an agent-oriented software engineering environment, Proceedings of the Third IEEE International Conference on Cognitive Informatics, ICCI 2004, 2004, pp. 250–257.

[26] R. Slowinski, D. Vanderpooten, A generalized definition of rough approximations based on similarity, IEEE Transactions on Knowledge and Data Engineering 12 (2) (2000) 331–336.

[27] S. Stoft, Power System Economics. IEEE Press. (2002) John Wiley & Sons.

[28] T. Sueyoshi, G. Tadiparthi, A wholesale power trading simulator with learning capabilities, IEEE Transactions on Power Systems 20 (3) (2005) 1330–1340.

[29] T. Sueyoshi, G. Tadiparthi, Agent-based approach to handle business complexity in US wholesale power, IEEE Transactions on Power Systems 22 (2) (2007) 532–544.

[30] T. Sueyoshi, G. Tadiparthi, Wholesale Power Price Dynamics under Transmission Line Limits: a Use of Agent-based Intelligent Simulator, IEEE Transactions on Systems, Man, and Cybernetics-Part C: applications and reviews, in press.

[31] N.H. Sung, J.K. Lee, Knowledge assisted dynamic pricing for large-scale retailers, Decision Support Systems 28 (4) (2000) 347–363.

[32] K. Sycara, M. Paolucci, M. Van Velsen, J. Giampapa, The RETSINA MAS infrastructure, Autonomous Agents and Multi-Agent Systems 7 (1–2) (2003) 29–48.

[33] Y.F. Wang, Mining stock price using fuzzy rough set system, Expert Systems with Applications 24 (1) (2003) 13–23.

[34] R.L. Wilson, R. Sharda, Bankruptcy prediction using neural networks, Decision Support Systems 11 (5) (1994) 545–557.

[35] M.E. Yahia, R. Mahmod, N. Sulaiman, F. Ahmad, Rough neural expert systems, Expert Systems with Applications 18 (2) (2000) 87–99.

[36] J. Zeleznikow, J.R. Nolan, Using soft computing to build real world intelligent decision support systems in uncertain domains, Decision Support Systems 31 (2) (2001) 263–285.

[37] R. Zimmerman, R. Thomas, D. Gan, C. Sanchez, A web-based platform for experimental investigation of electric power auctions, Decision Support Systems 24 (3–4) (1999) 193–205.

Toshiyuki Sueyoshi is a full professor for Department of Management at New Mexico Institute of Mining and Technology in USA. He is also a visiting full professor for Department of Industrial and Information Management at National Cheng Kung University in Taiwan. He obtained his Ph.D. from University of Texas at Austin. He has published more than 150 articles in well-known international journals.

Gopalakrishna Reddy Tadiparthi received a B.E. degree in Computer Science from University of Madras, India, in 1999 and worked as a Network Engineer at Satyam Infoway Limited (SIFY), India till 2002. He received a M.S. degree in Computer Science from New Mexico Institute of Mining and Technology in 2003 and is currently a Ph.D. candidate in the Department of Computer Science.
