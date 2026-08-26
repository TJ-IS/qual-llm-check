---
otero_id: 21861
otero_key: "XQESVRVW"
title: "A sales agent for part manufacturers: VMSA"
authors: "Hyung Rim Choi; Hyun Soo Kim; Young Jae Park; Kyoung Hwan Kim; Myung Ho Joo; Hyung Soo Sohn"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00094-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com<sup>r</sup>locate<sup>r</sup>dsw

# A sales agent for part manufacturers: VMSA

Hyung Rim Choi <sup>a,)</sup>, Hyun Soo Kim <sup>a</sup>, Young Jae Park <sup>a</sup>, Kyoung Hwan Kim <sup>b</sup>, Myung Ho Joo <sup>c</sup>, Hyung Soo Sohn <sup>a</sup>

Department of MIS, Dong-A UniÕersity, 840 Hadan-dong, Saha-gu, Pusan 604-714, South Korea <sup>b</sup> Techmate R&D Center CALS Team, DA-501, Bundang Industrial Town, Sungnam-si, Kyunggi-do, South Korea Kongkwan Protech, P.C.N. 137-073 Seochotown B<sup>r</sup>D 4F, 1521-2 Seocho-3dong, Seocho-Gu, Seoul, South Korea

## Abstract

The sales activity of most parts manufacturing companies is based on orders of buyers. The process of promotion, receipt and selection of orders of the parts manufacturers is closely coupled with the load status of the production lines. On deciding whether to accept an order or not, as well as negotiating with buyers, sales persons need information such as load and schedule of production lines, and manufacturability of the order. Manufacturability analysis, process planning, and scheduling are therefore key features in developing an agent of sales activity for the parts manufacturing business. In this paper, an intelligent agent, a virtual manufacturing-based sales agent VMSA with multi-agent architecture is proposed to Ž . support the sales activity for the parts manufacturers in the Internet environment. A VMSA has an integrated architecture of agent and virtual manufacturing. The prototype of VMSA has been developed for a machine parts manufacturing company that has lathe machines, drilling machines, cutting machines, and milling machines. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Business-to-business EC; Virtual manufacturing; Multi-agent; Sales agent

## 1. Introduction

## 1.1. Background of research

As the customers on the Internet can order a small amount of products online, the manufacturers should be adaptive to the order-based manufacturing system.

However, most manufacturers, particularly small and medium ones, are not ready to accommodate the change of back-end requirement. The back-end manufacturing management should be integrated with the salesman’s order taking process, which needs to check the availability of inventory within the due date and to negotiate the price to win the bid. As the number of online transactions explodes, this process needs systematic support of software agents. This is the goal of this research.

The target domains of this study are machine parts manufacturing companies that have lathe machines, drilling machines, cutting machines, and milling machines. A typical product manufactured by these companies is shown in Fig. 1, which requires drilling, slot milling, and end milling for manufacturing.

![](/api/attachments/XQESVRVW/fulltext/images/b98e79f0f85580e481ee69b10bfde8be55093083ac5817e435edcde7aed98ff8.jpg)  
Fig. 1. A lever bracket.

To meet this goal, we first explore the transaction process of online sales for parts manufacturing companies. Second, we define the roles and functions of multiple agents — named Virtual Manufacturingbased Sales Agents VMSA .Ž .

Third, the parts sales process is coupled with the virtual manufacturing facility to exploit the inventory, and capacity and availability of information during the negotiation and proposal generation process.

Finally, we suggest the architecture of VMSA, and illustrate the process of how the VMSA performs the search of buyers, advertising products, proposal-making, capacity of virtual manufacturing facility assessment, and negotiation.

## 2. Literature review

## 2.1. Electronic commerce and intelligent agent

In this section, let us briefly review the definition of electronic commerce EC and an intelligent agent.Ž . There are a variety of definitions of EC; however, because the definition is ever changing and expanding to include more and more sectors of the economy <sup>w</sup> <sup>x</sup> 7 , a consensus has yet to be reached.

Kalakota and Whinston 12 define it as a modern<sup>w</sup> <sup>x</sup> business methodology that addresses the needs of organizations, merchants, and consumers to cut costs while improving the quality of goods and services, and increasing the speed of service delivery. The term also applies to the use of computer networks to search for and retrieve information in support of human and corporate decision-making.

EC was not connected with the Internet when the term EC first appeared. So, the dawn of EC was not based on the Internet but based on electronic markets like electronic data interchange EDI , TELCOT 15 ,Ž . <sup>w</sup> <sup>x</sup> etc.

The definition of an intelligent agent has not yet reached consensus either. Franklin and Graesser 10<sup>w</sup> <sup>x</sup> explained that the reason for the variety of definitions is that each of them grew out of the set of examples of agents that the definer had in mind.

Generally, the definition of an agent is based upon its attributes. The attributes of an intelligent agent given below are summarized by Nissen 16 to<sup>w</sup> <sup>x</sup> differentiate them from other types of software applications.

<sup>Ø</sup> Autonomy: The intelligent agent must have the capability to take actions leading to the completion of task s or objective s , without or impetus from Ž . Ž . the end-user. There must be an element of independence on the agent.

<sup>Ø</sup> Communication ability: The intelligent agent must, in the course of achieving their objectives, access information from third party sources about the current ‘‘state’’ of the external environment. This requires an ability to communicate with the repositories of this information. These may be other agents or gatekeepers of information stores.

<sup>Ø</sup> Capacity for cooperation: A natural extension of the communication attributes is cooperation. Intelligent agents must have a collaborative ‘‘sprit’’ to work together.

<sup>Ø</sup> Capacity for reasoning: The ability to perform reasoning is one of the key aspects of intelligence that distinguishes intelligent agents from other more ‘‘robotic’’ agents.

<sup>Ø</sup> Adaptive behavior: To maintain autonomous and reasoning capabilities, the agent must have some mechanism for assessing the current state of its external domain and incorporating this into its ‘‘decision’’ about future action.

<sup>Ø</sup> Trustworthiness: Essential to the acceptance of agency is a strong sense of trust that the agent can accurately represent the user, its client. This holds equally true for intelligent agents on the World Wide Web WWW .Ž .

Based on the above attributes, we can define an intelligent agent as a software that learns, infers, and cooperates with other agents or systems, if necessary, to solve given problems actively, autonomously and distinctively.

Nissen 16 also classified the current application<sup>w</sup> <sup>x</sup> of an agent on the Internet into the following five types, which reflect different characteristics of an intelligent agent.

<sup>Ø</sup> Watcher agents: Watcher agents operate autonomously, looking for specific information or events. When information relevant to the user is found, the agent can either notify the user directly Ž . e.g., with a news flash or store the information for future access e.g., for a personalized newspaper . Ž . The most interesting example of an intelligent newspaper is MIT’s Fishrap http: Ž <sup>rr</sup>fishtrap-docs.www. media.mit.edu<sup>r</sup>docs ..

<sup>Ø</sup> Learning agents: A learning agent is capable of tailoring its performance to an individual’s preferences by learning from a user’s past behavior. A number of Internet applications claim to have this learning ability. Probably the most well known is the Firefly http:Ž . <sup>rr</sup>www.firefly.net music recommendation system.

<sup>Ø</sup> Shopping agents: Shopping agents are capable of doing comparative shopping and finding the best price for an item. Retailers can protect themselves from this sort of competition by giving their products unique names as is done by Virtual Vineyards Ž Ž http:<sup>rr</sup>www.wine.com or by blocking access from .. search agents as is happening to the Bargain Ž Finder http: Ž .. <sup>rr</sup>bf.cstar.ac.com<sup>r</sup>bf<sup>r</sup> .

<sup>Ø</sup> Information retrieval agents: Information retrieval agents are capable of searching information in an intelligent fashion. The most obvious example is an Internet search agent, which can conduct complex searches by interpreting the search criteria defined by a user. An example of this type of agent is Architext Software’s Excite search engine http: Ž <sup>rr</sup> www.jango.com ..

<sup>Ø</sup> Helper agents: Helper agents perform tasks autonomously, without human interaction. Most of the helper agents that we find are used for network management. These are less likely to be intelligent and should be considered infobots.

Generally, intelligent agents in EC are used to support the consumers’ buying activities. Typical agent categories are shopping comparison agents, bidding and auction agents, and transaction support agents.

The representative agents for shopping comparison agents are Anderson Consulting’s BargainFinder <sup>w</sup> <sup>x</sup> 5 , which compares information about music CDs, Curtin University’s BargainBoat 3 , which compares<sup>w</sup> <sup>x</sup> information about books, and University of Washington’s ShopBoat 9 , which compares information<sup>w</sup> <sup>x</sup> about music CDs and S<sup>r</sup>W.

Generally, a few difficulties arise when developing strategies of negotiation. The possibility of an agent ‘‘discovering’’ the negotiation strategy of another should be controlled in such a way that negotiations don’t break down. Building up a related ontology that defines the vocabulary in the communication of agents is another difficulty. The methodologies developed to solve these problems are decision support systems DSS , negotiation support systems Ž . Ž . Ž . NSS , distributed artificial intelligence DAI , and genetic algorithms GA 4 . The representative agentŽ . <sup>w</sup> <sup>x</sup> for electronic negotiation on the WWW is MIT Media Lab’s Kasbah 6 , which negotiates prices of<sup>w</sup> <sup>x</sup> products between buyers and sellers through a cyber-market called Kasbah. But Kasbah has limitations that it doesn’t compare buyers’ offers simultaneously, only individually. The representative agents of auctions are Onsale http:Ž <sup>rr</sup>www.onsale. com . UNIK-AGENT 14 is an agent for automating. <sup>w</sup> <sup>x</sup> competitive contract process such as bids and auctions.

## 2.2. Virtual manufacturing system

The research directions of concurrent engineering are turning to virtual manufacturing VM to solveŽ . several practical problems. Concurrent engineering researchers are using rapid prototyping to build a virtual manufacturing environment within the computer. The virtual manufacturing environments are based on similar models of real ones. For example, manufacturing models, manufacturing factory models and machining models are built using the data of a real manufacturing environment. The virtual manufacturing environment can simulate manufacturing activities 13 .<sup>w</sup> <sup>x</sup>

On the CAD system side, researchers of 3-dimensional representations are trying to add manufacturing process information to the product design model by adopting the concept of a feature, which attempts to model the relationship between the local geometric and topological configurations of a design and the higher-level abstractions. Feature-based modeling Ž . FBM of design information has long been viewed as vital for design analysis and data exchange. Significant work has been directed towards defining sets of features to serve as a means of communication between design and manufacturing. At present, however, most researchers are convinced that no single set of features can satisfy the requirements of every possible domain of design and manufacturing 17 . In<sup>w</sup> <sup>x</sup> practice, it was applied to the development of airplanes and automobiles, and is now being applied in other areas as well. CAD systems that support virtual manufacturing are IBM’s CATIA, SDRC’s IDEAS, PTC’s Pro<sup>r</sup>Engineer, and DIVISION’s dVISE. IBM’s CATIA was used in the development of Boeing’s 777 and Opel’s automobiles. Opel substituted virtual prototypes for physical prototypes and reduced manufacturing costs and time 11 .<sup>w</sup> <sup>x</sup>

## 2.3. Virtual manufacturing agent

In the manufacturing industry, there are several VM agents using multi-agent architecture such as Balasubramanian’s agent-based concurrent design environment ABCDE , Parunak’s autonomousŽ . agents for rock island arsenal AARIA , and Chuter’sŽ . virtual environment for construction and analysis of manufacturing VECA . Each agent has its own fea- Ž . tures and architecture. The ABCDE system was developed for the integration of design, manufacturing, and shop floor control activities using multi-agent architecture. This is based on cooperating intelligent entities in the sub-domains. The entities make decisions through negotiation, using domain specific knowledge, both distributed among the entities and accessible to them. Using this architectural framework, an agent-based concurrent design environment system has been developed for feature-based design, manufacturability evaluation and dynamic process planning 2 . The AARIA project demonstrates how <sup>w</sup> <sup>x</sup> agent technologies and the Internet communication can support this expanded vision. That project discussed a way of creating an agile network of suppliers that are truly responsive to individual customer desires 1 . VECA is built to be flexible enough to<sup>w</sup> <sup>x</sup> support research efforts in scheduling, planning, and behavior modeling 8 . <sup>w</sup> <sup>x</sup>

## 2.4. Architectural characteristics of VMSA

Much research has been done on an agent for EC. However, most research focuses on buyer activity, not seller activity. Existing research could hardly be found on agents to support manufacturers or even approaches to combining virtual manufacturing with agents to support manufacturing businesses.

The existing studies on virtual manufacturing have had great success and have been used inside and outside of the laboratory. However, they only focus on manufacturing itself rather than its connection to EC. There is little research on combining EC and virtual manufacturing. This virtual manufacturing with a sales agent, we call it as VMSA, is the main object of our research. The characteristics of VMSA are as follows:

<sup>Ø</sup> Focus on Seller’s Activity for Parts Manufacturers: Most researches on EC are concerned with final products rather than parts products. And, conventional agent applications related to EC are usually for buyers or end-customer support. However, VMSA is a sales agent to support sellers’ activities for parts manufacturers.

<sup>Ø</sup> Integration of EC, Agent, and VM: Until now, most research areas have been studied separately; however, VMSA has the integrated architecture of EC, agent, and virtual manufacturing to extend the reach in the Internet environment.

<sup>Ø</sup> Supporting Business-to-Business EC: Most researches on EC are mainly for the business-tocustomer EC category. The VMSA supports business-to-business EC, especially parts manufacturing businesses.

## 3. Process of parts sales transactions

In this paper, we try to respond to the actual processes in transactions between manufacturing businesses and to implement them using EC. The ultimate objective of this research is to support these businesses by developing agents. The detailed functions of agents to support the parts selling processes on EC for a parts seller are summarized below:

![](/api/attachments/XQESVRVW/fulltext/images/7686dbf0390ef58188f25104ab9c1115462e7271a895c736b17bac72c70b5ac9.jpg)  
Fig. 2. The overall architecture of VMSA.

Step 1: Search

Seller: Search for potential buyers on the Internet and execute periodical advertising activities.

<sup>ª</sup>Searching for a buyer’s URL and indexing it, sending e-mail or an electronic catalog to buyers.

Buyer: Search for manufacturing firms selling parts, and storing them in the index base.

<sup>ª</sup>Searching for a seller’s URL and indexing it.

Step 2: Selection

Buyer: Ordering from a seller.

<sup>ª</sup>FTP, e-mail, and communication functions between agents.

Seller: Sorting and prioritizing the received orders based on the history of transactions and manufacturing capacity evaluated by the virtual manufacturing system.

Comparison and selection functions.

Step 3: Negotiation

Negotiate with buyers whose orders need to be adjusted.

<sup>ª</sup>Communication and negotiation functions between agents.

## 4. Roles and functions of VMSA

To support the process of transactions in EC, agents need a variety of functions. Our approach is to designate agents for various functions and to support the sales activities of small and medium-sized manufacturing firms.

We call the set of agents, which is a multi-agent system coupled with virtual manufacturing, as VMSA. VMSA consists of a search agent, an advertisement<sup>r</sup>suggestion agent, a selection agent, and a negotiation agent.

![](/api/attachments/XQESVRVW/fulltext/images/1950398fbb24268e4c3cd8ae5286bdf6bc1bd59218fb28a6ac1ff77f65f14b39.jpg)  
Fig. 3. The common architecture of each agent.

A search agent uses search functions on the Internet to find potential buyers and stores them in an index base. An advertisement<sup>r</sup>suggestion agent sends a catalog and e-mail to the potential buyers to actively promote sales. They also suggest proposals and send them to buyers who request proposals. A selection agent prioritizes the orders of buyers by analyzing past purchase history and credit level; then, it analyzes the manufacturing constraints of a production line and announces reasonable due date by linking with the virtual manufacturing system. These functions will likely raise the level of buyer satisfaction and confidence. The negotiation agent lets both sellers and buyers reach satisfactory conditions among themselves. The agent makes the result known to sellers in case of either a success or a failure in the negotiation. The last decision-maker is the seller, who is informed by the agent about the results. The agent keeps records of all the events in the process of negotiation and makes it possible to utilize them in the next negotiation step.

The other important subsystem of VMSA is the virtual manufacturing system. The virtual manufacturing system makes it possible to reduce the cost and effort of making prototypes and satisfying customer needs by ‘‘virtually’’ manufacturing and considering all of the real manufacturing conditions. Our virtual manufacturing system is a cooperative multiagent system that is composed of a database DB , aŽ . manufacturability analysis agent, a process planning agent, and a scheduling agent. The role of the manufacturability analysis agent is to decide whether the order received from the selection agent can be manufactured or not on the basis of manufacturing technology. When a certain order turns out to be manufacturable, then, the process planning agent generates the optimal process plans, which utilize all the related machines and manpower efficiently and reduce the manufacturing costs. Then, the scheduling agent calculates the expected finishing date of the order, taking into account the current status of the production line.

## 5. Architecture of VMSA

The VMSA has a multi-agent architecture to support the various functions mentioned in Section 4. Using knowledge query and manipulation language

![](/api/attachments/XQESVRVW/fulltext/images/f25d44a98075e76d3e9fedd128977ff17b6da24225965cbc826d9d45d63b278e.jpg)  
Fig. 4. The architecture of the search agent.

Ž . KQML , which is the representative communication language among agents, VMSA can resolve the heterogeneity of agents. The communications between external agents, as well as internal agents, are made through a controller, who has roles of agent name service ANS , message routing, mediation, andŽ . matchmaking between agents. Fig. 2 shows the overall architecture of VMSA.

Each agent has a common architecture, as shown in Fig. 3: a communication part, an agent dependent reasoning engine, a virtual knowledge base and a user interface.

The functions of internal modules of the communication part are as follows:

<sup>Ø</sup> Message converter: Every message is transmitted through the message converter and the message is changed to TCP<sup>r</sup>IP protocols. It also controls the connection with other agents.

<sup>Ø</sup> Message queuing: Manages outbound and inbound messages, permitting only valid messages to pass.

<sup>Ø</sup> Message manager: Inspects message forms based on all the hierarchies of KQML. Initializes the reasoning engine to generate the response message according to the query message.

## 5.1. Search agent

The right-hand side of Fig. 4 is the search agent suggested in this paper.

<sup>Ø</sup> The index base has URLs and e-mail addresses generated by an index generator or inputted by users.

<sup>Ø</sup> The search engine is composed of several search algorithms such as a keyword search algorithm that searches for addresses that other agents or users request.

Network  
![](/api/attachments/XQESVRVW/fulltext/images/7c51d794e4bee59fcd80920102bcb4554d7ef6e7335967d33f1a939b9f049978.jpg)  
Fig. 5. The architecture of a virtual manufacturing system.

The left-hand side of Fig. 4 shows a resource finding robot that is generally used for search engines. The general actions of a robot are simultaneous to move around multiple servers based on URL DBs and collected pages. The collected pages are transformed into meaningful data by an index generator and stored in the index base.

## 5.2. AdÕertisement<sup>r</sup>suggestion agent

The major components of the advertisement<sup>r</sup> suggestion agent are a document generator and a knowledge base.

<sup>Ø</sup> The document generator elicits documents elec-Ž tronic catalogs, proposals and sends them to the. e-mail addresses stored in the URL DB of the search agent.

<sup>Ø</sup> The electronic catalogs and CAD documents received from buyers are stored in the knowledge base.

## 5.3. Selection agent

<sup>Ø</sup> Comparison and selection engine: This prioritizes the orders by accepting parameters from the user interface and utilizing the knowledge base to compare the orders.

<sup>Ø</sup> Knowledge base: Knowledge for comparison and selection, history of orders, and meta knowledge are stored in the knowledge base.

## 5.4. Negotiation agent

<sup>Ø</sup> Negotiation strategy builder: This accepts parameters from users, initializes negotiation strategy and transmits results at each stage of strategy development.

<sup>Ø</sup> Negotiation reasoning engine: This matches the parameters revealed in the buyers’ and sellers strategy and announces the results to users whether the negotiation is resolved or not.

<sup>Ø</sup> Knowledge base: This consists of knowledge necessary for reasoning and meta knowledge.

## 5.5. Virtual manufacturing system

A virtual manufacturing system consists of four agents: a DB agent, a manufacturability analysis agent, a processes planning agent, and a scheduling agent. The architecture of a virtual manufacturing system is illustrated in Fig. 5.

The role of each agent in the virtual manufacturing system is described as follows:

<sup>Ø</sup> VM controller: The VM controller does ANS, message routing, mediation and matchmaking. The VM controller sends information that comes from VM agents to the VMSA controller. The VM controller receives lots of information that comes from the VMSA controller and then sends it to VM agents.

<sup>Ø</sup> Database: All the information and the production environment, such as factory shop models, machining models, and part models, are stored in this DB.

Table 1  
Parameters of VMSA

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td>Company_code</td><td>Product buyer&#x27;s company code</td></tr><tr><td>Company_name</td><td>Product buyer&#x27;s company name</td></tr><tr><td>url_addrs</td><td>Product buyer&#x27;s URL address</td></tr><tr><td>Email_addrs</td><td>Product buyer&#x27;s e-mail address</td></tr><tr><td>Product_code</td><td>Code of product that buyer sends</td></tr><tr><td>Product_name</td><td>Name of product that buyer sends</td></tr><tr><td>Product_data</td><td>Geometric product data (CAD files, etc.)</td></tr><tr><td>Manufacturability (true,false)</td><td>Result of manufacturability evaluation</td></tr><tr><td>Proposal_due_date</td><td>Date that seller has to submit the proposal</td></tr><tr><td>Wanted_due_date</td><td>Date that buyer wants to receive the product</td></tr><tr><td>Wanted_dd_nego</td><td>Negotiable state for due date</td></tr><tr><td>Expected_due_date</td><td>Date that seller expects to deliver the product</td></tr><tr><td>Wanted_price</td><td>Unit price that buyer wants to pay</td></tr><tr><td>Wanted_p_nego</td><td>Negotiable state for price</td></tr><tr><td>Expected_price</td><td>Unit price that seller expects to be paid</td></tr><tr><td>Wanted_quantities</td><td>Quantity of product wanted by buyer</td></tr><tr><td>Wanted_q_nego</td><td>Negotiable state for quantities</td></tr><tr><td>Expected_quantities</td><td>Minimum quantity of seller to produce</td></tr><tr><td>Delivery_place</td><td>Place that buyer wants to receive the product</td></tr><tr><td>Payment_method</td><td>Method that buyer wants to pay</td></tr></table>

<sup>Ø</sup> Manufacturability analysis agent: When a computerized representation of the design and a set of manufacturing resources are received from the sales agent, it determines, using FBM, whether the product design is feasible or not. If it is feasible, the manufacturability analysis agent calculates the manufacturing rating using FBM.

<sup>Ø</sup> Process planning agent: This generates a feature set from the FBM, and determines the optimal operation sequences.

<sup>Ø</sup> Scheduling agent: This generates operation schedules based on process planning, taking into account the various manufacturing environments. It calculates the expected finishing date of the order, taking into account the current status of the production line.

## 6. Parameters and expressions for VMSA

There may be some differences among the parameters being used in the manufacturing business according to the characteristics of the manufacturers. In this paper, we define the parameters needed in VMSA Ž .see Table 1 .

We have identified the procedures of sales transactions in VMSA and the detailed process of each agent involved in VMSA. Fig. 6 shows the procedures of sales transactions in VMSA.

Ž . 1 The controller plays the role of sending the parameters to each agent in VMSA. Company name,<sub>–</sub> URL addrs, product name, product data, wanted<sub>– – – –</sub> due date, wanted price, wanted quantities, pay- <sub>– – –</sub> ment method are received from the user interface.<sub>–</sub> Among the parameters, product data is transferred <sub>–</sub> via FTP protocol, and input parameters received from the buyer DONGA are represented in theŽ . following expression. Fig. 7 shows the example screen of the controller’s user interface

<table><tr><td colspan="2">(tell</td></tr><tr><td>:sender</td><td>DONGA</td></tr><tr><td>:receiver</td><td>controller</td></tr><tr><td>:language</td><td>KQML</td></tr><tr><td>-reply-with</td><td>RFP1234</td></tr><tr><td colspan="2">:contents</td></tr><tr><td>(company_name</td><td>DONGA,</td></tr><tr><td>url_addrs</td><td>www.buyer.co.kr,</td></tr><tr><td>product_name</td><td>Lever_Bracket,</td></tr><tr><td>proposal_due_date</td><td>1998-07-15,</td></tr><tr><td>wanted_due_date</td><td>1998-07-30,</td></tr><tr><td>wanted_dd_nego</td><td>YES,</td></tr><tr><td>wanted_price($)</td><td>30,</td></tr></table>

![](/api/attachments/XQESVRVW/fulltext/images/c1e0a6869c89505315885d28a1974b8b4201269f825aa654d37b3dbca30cf5bb.jpg)  
Fig. 6. The procedure of Sales transactions in VMSA.

![](/api/attachments/XQESVRVW/fulltext/images/1cc4b5e531b869a659ebeab473fa25812427fe603ce7f09e407608dcf676bc46.jpg)  
Fig. 7. A Screen of user interface.

wanted p nego<sub>– –</sub> YES, wanted quantity<sub>–</sub> 50, wanted q nego<sub>– –</sub> YES, payment method<sub>–</sub> CASH..

Ž . 2 Company name, URL addrs, email addrs of<sub>– – –</sub> the buyer’s DONGA input parameters receivedŽ . from the user interface are sent to the search agent with the help of the controller. Otherwise, the results from the robot agent are stored in the index base. When the advertisement<sup>r</sup>suggestion agent sends the resources to the buyer, it refers to information in the index base. The following are the illustrated parameters sent to the search agent.

Žtell

:sender

:receiver

controller

:language

Search Agent

:contents

KQML

Žcompany name<sub>–</sub> DONGA, url addrs www.buyer.co.kr, email addrs<sub>–</sub> donga@buyer.co.kr..

Ž . 3 Product name, product data, wanted due<sub>– – – –</sub> date, wanted price, wanted quantities are sent to <sub>– –</sub> the virtual manufacturing system with the help of the controller, and product data of these are transferred<sub>–</sub> via FTP protocol. The virtual manufacturing system generates output parameters of manufacturability, expected due date, expected price, expected quanti- <sub>– – – –</sub> ties after using input parameters, and these parameters are sent to the selection agent. The following are the input and output expressions in the virtual manufacturing system. Fig. 8 shows the example screen of the input expressions of the virtual manufacturing system.

Žask-one

:sender

controller

![](/api/attachments/XQESVRVW/fulltext/images/9d5b75932254d0d803479125c9e4f10e737cd079447e5fcd0cc8bfd117f4ad13.jpg)  
Fig. 8. A Screen of VMS Controller Interface.

<table><tr><td>:receiver</td><td>VMController</td></tr><tr><td>:language</td><td>KQML</td></tr><tr><td>-reply-with</td><td>RFP1234</td></tr><tr><td>:contents</td><td></td></tr><tr><td>(product_name</td><td>Lever_Bracket,</td></tr><tr><td>proposal_due_date</td><td>1998-07-15</td></tr><tr><td>wanted_due_date</td><td>1998-07-30,</td></tr><tr><td>wanted_price($)</td><td>30,</td></tr><tr><td>wanted_amount</td><td>50))</td></tr></table>

Žproduct name<sub>–</sub> Lever Bracket, manufacturability YES, expected due date<sub>– –</sub> 1998-07-30, expected price \$Ž . <sub>–</sub> 32, expected quantity<sub>–</sub> 50..

Ž . 4 Product name, wanted due date, wanted<sub>– – – –</sub> dd\_nego, wanted price, wanted p nego, wanted <sub>– – – –</sub> quantities, wanted q nego of parameters, which <sub>– –</sub> were inputted by the buyer DONGA , are sent to theŽ . selection agent with the help of the controller.

The output expressions of the virtual manufacturing system are as follows:

Žtell

Žreply

:sender

VMController

:sender

controller

:receiver

SelectAgent

:receiver

SelectAgent

:language

KQML

:language

KQML

:reply-with

RFP1234

:in-reply-to

RFP1234

:contents

:contents

Žcompany name<sub>–</sub>

DONGA

<table><tr><td>product_name</td><td>Lever_Bracket,</td></tr><tr><td>proposal_due_date</td><td>1998-07-15,</td></tr><tr><td>wanted_due_date</td><td>1998-07-30,</td></tr><tr><td>wanted_dd_nego</td><td>YES,</td></tr><tr><td>wanted_price($)</td><td>30,</td></tr><tr><td>wanted_p_nego</td><td>YES,</td></tr><tr><td>wanted_quantity</td><td>50,</td></tr><tr><td>wanted_q_nego</td><td>YES))</td></tr></table>

Fig. 9 shows the sample screen of the selection agent’s request for proposal RFP list received from Ž . the controller.

After comparing the parameters from the virtual manufacturing system and the parameters from the buyer, the selection agent determines the priorities for processing the orders or RFPs, as shown in Fig. 10.

Ž . 5 The advertisement<sup>r</sup>suggestion agent sends the electronic catalog and the proposal. Product name, <sub>–</sub> expected due date, expected price, expected quan- <sub>– – – –</sub> tities of the product are sent to the buyer DONGAŽ . referring to the e-mail addresses. The KQML messages are represented as follows:

<table><tr><td colspan="2">(tell</td></tr><tr><td>:sender</td><td>Advertisement/ Suggestion_Agent</td></tr><tr><td>:receiver</td><td>DONGA</td></tr><tr><td>:language</td><td>KQML</td></tr><tr><td>:in-reply-to</td><td>RFP1234</td></tr><tr><td colspan="2">:contents</td></tr><tr><td>(product_name</td><td>Lever_Bracket,</td></tr><tr><td>expected_due_date</td><td>1998-07-30,</td></tr><tr><td>expected_price($)</td><td>32,</td></tr><tr><td>expected_quantities</td><td>50))</td></tr></table>

Ž . 6 The negotiation agent supports the buyer to get the best terms from the product seller. And the

![](/api/attachments/XQESVRVW/fulltext/images/350ca1d032dffa0cc328407e23edc838843124ff1a2971aed2915a5106baaea9.jpg)  
Fig. 9. A Screen of Selection agent’s RFP list received from Controller and KQML Message View.

![](/api/attachments/XQESVRVW/fulltext/images/4b0c346c6292805b2d9327f49edb4e88f0381244ae76be7ea610a62b5f1777d2.jpg)  
Fig. 10. A Screen of Selection Agent’s result.

product seller also can negotiate with the buyer using the intelligent agents for these purposes.

## 7. Conclusions

Promotion, receipt, and selection of orders are very important activities from the standpoint of the parts manufacturing business. However, most of parts manufacturing businesses are generally suffering from lack of marketing and sales manpower who are in charge of such activities. On deciding whether to accept an order or not, as well as negotiating with buyers, sales persons need information such as load and schedule of production lines, manufacturability of the order, etc.

To solve this problem, we have proposed an intelligent agent, a VMSA with multi-agent architecture, which is composed of five agents: search agent, advertisement<sup>r</sup>suggestion agent, selection agent, negotiation agent, and virtual manufacturing agent.

The prototype of the VMSA was developed for a machine parts manufacturing company that has lathe machines, drilling machines, cutting machines, and milling machines to justify the architecture suggested in this paper.

## Acknowledgements

The authors wish to acknowledge the financial support of the Korea Research Foundation made in the Program Year 1997.

## References

<sup>w</sup> <sup>x</sup> 1 A.D. Baker, H.V.D. Parunak, K. Erol, Manufacturing over the Internet and into Your Living Room: Perspectives from the AARIA Project, 1997. http<sup>rr</sup>www.erim.org<sup>r ;</sup> van<sup>r</sup> papers.htm, Jan. .Ž .

<sup>w</sup> <sup>x</sup> 2 S. Balasubramanian, D.H. Norrie, A Multi-Agent Intelligent Design System Integrating Manufacturing And Shop-Floor Control, http:<sup>rr</sup>ksi.cpsc.ucalgary.ca<sup>r</sup>projects<sup>r</sup>mediator.

<sup>w</sup> <sup>x</sup> 3 A. Bassum, Agent Technology in Electronic Commerce and Information Retrieval on Internet, 1996. http:<sup>rr</sup>www.ece. curtin.edu.au<sup>r ;</sup>saounb<sup>r</sup>bargainbot<sup>r</sup>paper<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 4 C. Beam, A. Segev, J.G. Hanthinkumer, Electronic negotiation through Internet-based auction, in: CITM Working paper 96-WP-1019, 1996.

<sup>w</sup> <sup>x</sup> 5 J.J. Calabrese, E.D. Mather, New Intelligent Agent Tackles Internet Privacy Issues: Andersen Consulting experiment examines how electronic merchants can better target customers in cyberspace,1996. http:<sup>rr</sup>www.ac.com<sup>r</sup>news<sup>r</sup>1996-7archives<sup>r</sup>news archives 082796.html.<sub>– –</sub>

<sup>w</sup> <sup>x</sup> 6 A. Chavez, P. Maes, Kasbah: An Agent Marketplace for Buying and Selling Goods, 1996.

<sup>w</sup> <sup>x</sup> 7 S.Y. Choi, D.O. Stahl, A.B. Whinston, The Economics of Electronic Commerce, Macmillan, 1997.

8 C.J. Chuter, S. Ramaswamy, K.S. Barber, A Virtual Environment for Construction and Analysis of Manufacturing Prototypes, http:<sup>rr</sup>www.cs.umd.edu<sup>r ;</sup>regli<sup>r</sup>asme.ps.

<sup>w</sup> <sup>x</sup> 9 B. Doorenbos, O. Etzioni, D. Weld, ShopBoat, http:<sup>rr</sup>www.cs.washington.edu<sup>r</sup>homes<sup>r</sup>bobd<sup>r</sup>shopbot.htm.

<sup>w</sup> <sup>x</sup> 10 S. Franklin, A. Graesser, Is it an Agent or just a Program? A Taxonomy for Autonomous Agents, in: Proceedings of the 3rd International Workshop on Agent Theories, Architecture, and Language, 1996.

<sup>w</sup> <sup>x</sup> 11 IBM CATIA-CADAM Solutions, Success Stories listed by industry, http:<sup>rr</sup>www.catia.ibm.com<sup>r</sup>custsucc<sup>r</sup>success.html.

<sup>w</sup> <sup>x</sup> 12 R. Kalakota, Whinston, Frontiers of Electronic Commerce, Addison Wesley, 1996.

<sup>w</sup> <sup>x</sup> 13 Lawrence Associates, Virtual Manufacturing User Workshop,1995. http:<sup>rr</sup>www.isr.umd.edu<sup>r</sup>Labs<sup>r</sup>CIM.

<sup>w</sup> <sup>x</sup> 14 J.K. Lee, W.K. Lee, An intelligent agent based competitive contract process: UNIK-AGENT, International Journal of Intelligent System in Accounting, Finance & Management Ž . 1998 91–105.

<sup>w</sup> <sup>x</sup> 15 D. Lindsey, P. Cheney, G. Kasper, R. Ives, TELCOT: An Application of Information Technology for Competitive Advantage in the Cotton Industry, MIS Quarterly 1990 Dec. .Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 M. Nissen, Intelligent Agent: A Technology and Business Application Analysis, 1995.

<sup>w</sup> <sup>x</sup> 17 W.C. Regli, Geometrical Algorithms for Recognition of Features from Solid Model, 1995. http:<sup>rr</sup>www.cs.umd.edu<sup>r ;</sup> regli.

![](/api/attachments/XQESVRVW/fulltext/images/b6d629806f54f38f554b42436f5f30f2df94d7b710076a385aa97110f99b0616.jpg)

![](/api/attachments/XQESVRVW/fulltext/images/1f4beddedfaf2858373827b0e618e9b1f277f77772240b9a594a11f01f7f1f44.jpg)

Hyung Rim Choi is a professor of Management Information Systems at the Dong-A University in Korea. He received his BBA from Seoul Nationa University, an MS and a PhD in management science from the Korea Advanced Institute of Science and Technology. His major research interests include AI for electronic commerce, automation of process planning and scheduling in manufacturing domain, and intelligen manufacturing systems. Now he is inter-

![](/api/attachments/XQESVRVW/fulltext/images/6bd59565f952d0238afc3155354e17497f2b3ddec82d504f1dc3200e93ed14ba.jpg)

![](/api/attachments/XQESVRVW/fulltext/images/25cafc139fcb368b624fa7ac3e28aba522a096da6f3ac1403bdc013ba10806fc.jpg)

ested in the research area of port and logistics systems. He is a member of the American Association for Artificial Intelligence.

Hyun Soo Kim is a professor of Management Information Systems at the Dong-A University in Korea. He received his BBA from Seoul Nationa University, an MS and a PhD in management science from the Korea Advanced Institute of Science and Technology. His current research interests lie in data mining in digital product companies and virtual market.

![](/api/attachments/XQESVRVW/fulltext/images/ac6aa1c1d0bb178357ab3e3991d5007f08fe840c7c6637cb83f70d27b608c00b.jpg)

![](/api/attachments/XQESVRVW/fulltext/images/e2eff8693a6e78026647cfdc62f750446a8e803a32e0b965e6dbfdc9f670e2d5.jpg)

Young Jae Park is a graduate student of Management Information Systems at the Dong-A University in Korea. He received his BBA from Pusan University of Foreign Studies and majored in management information system. His major research interests include AI for electronic commerce, decision support system<sup>r</sup>expert system, agent applications, and management information system. Now he is interested in the research area of port and logistics systems.

Kyoung Hwan Kim is a graduate student of Management Information Systems at the Dong-A University in Korea. He received his BE from Dong-A University and majored in Computer Engineering. His major research areas are electronic commerce on the Internet and agent technologies. Now he is interested in the research area of multimedia application service.

Myung Ho Joo is a graduate student of Management Information Systems at the Dong-A University in Korea. He received his BS from Dong-A University and majored in Physics. His major research interests include AI for electronic commerce, automation of process planning and scheduling in manufacturing domain, and intelligent manufacturing systems.

Hyung Soo Shon is a graduate student of Management Information Systems at the Dong-A University in Korea. He received his BBA from Dong-A University. His major research interests include electronic commerce on the Internet and agent applications. Now he is interested in the research area of port and logistics systems.
