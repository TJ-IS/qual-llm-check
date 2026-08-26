---
otero_id: 21135
otero_key: "5927MBYC"
title: "Agent-based merchandise management in Business-to-Business Electronic Commerce"
authors: "Jae Heon Park; Sang Chan Park"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00111-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Agent-based merchandise management in Business-to-Business Electronic Commerce

Jae Heon Park\*, Sang Chan Park

Department of Industrial Engineering, Korea Advanced Institute of Science and Technology, 373-1, Guseong-dong, Yuseong-gu, Daejeon 305-701, Republic of Korea

Accepted 1 April 2002

## Abstract

Currently, there is cutthroat competition in the retail industry, and retail companies struggle for survival. Merchandise management—selecting desirable merchandise, disposing of slow-selling goods and ordering and distributing them—is important to a retailer’s success because merchandise is the basis of retailing. Particularly because in an Electronic Commerce (EC) environment, customer preferences are very diverse and their merchant loyalty level is very low, companies should acknowledge the changes in customer demand patterns quickly and respond to them appropriately. However, until now, most retailers have depended on humans for merchandise management. Because there are too many merchandise and brands, it is impossible for merchandise managers to evaluate, compare, select and dispose of merchandise effectively. Retailers need a system that can perform merchandise managers’ jobs autonomously, continuously and efficiently. In this paper, we propose an agent-based system for merchandise management, which performs evaluating and selecting merchandise and predicting seasons and building purchase schedules autonomously in place of human merchandise managers under a Business-to-Business (B2B) EC environment. In order to facilitate the agent’s intelligent behavior, several analysis tools such as Data Envelopment Analysis (DEA), Genetic Algorithm (GA), Linear Regression and Rule Induction Algorithm are incorporated into the system. Lastly, the proposed system is verified in its application to a duty-free shop. The proposed system would accomplish merchandise management timely, autonomously and efficiently, and the effective merchandise management would reduce the inventory level while increasing sales and profits. The agent-based merchandise management system will enhance a retail company’s potential for success. Moreover, it will be necessary for survival in the B2B EC. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Merchandise management; Intelligent software agent; Business-to-Business Electronic Commerce; Retail industry; Data Envelopment Analysis; Genetic Algorithm; Rule Induction Algorithm

## 1. Introduction

The major activities of merchandise management, including selecting, ordering and distributing merchandise, are important to a retailer’s success because merchandise is the basis of retailing. Especially, retailers should select popular merchandise and dispose of unpopular ones. Though there have been a lot of systems supporting the replenishment of merchandise, selecting goods have been carried out by human beings in most retail companies. Retailers need a new system that can undertake merchandise managers’ jobs—evaluating and selecting merchandise and searching for new, popular merchandise, and accomplishing those tasks autonomously. Moreover, the automation of those tasks will be an indispensable condition for retailers to survive in the Electronic Commerce (EC) environment, in which transactions are growing very rapidly with a great increase of Internet usage, because customer demand patterns change quickly. Because in the EC environment, customer preferences are very diverse and their merchant loyalty level is very low, companies should acknowledge the changes of the patterns quickly and respond to them appropriately. Currently, however, merchandise management, including evaluating, selecting and ordering, is almost entirely driven by human beings, and it will not be possible for retailers to cope effectively with the dynamic changes of customer demand patterns in the EC environment without intelligent and autonomous merchandise management systems.

The automation of tasks can be realized by intelligent software agents because autonomy is the most important property of intelligent software agents, and the concept of the intelligent software agent is useful for developing a software system, especially for solving difficult, time-consuming problems. Moreover, in a virtual marketplace in the Business-to-Business (B2B) EC, buying and selling of products between companies are carried out by autonomous agents, and, therefore, other related tasks of retailers such as evaluating, selecting, and ordering merchandise also need to be placed in the hands of intelligent agents for a successful operation of the whole process of retailing.

We will propose an agent-based system for merchandise management under the B2B EC environment, which performs the functions of evaluating and selecting merchandise and building schedules for tasks. For that purpose, this research achieves the following objectives.

1. To analyze and configure processes of merchandise management.

2. To design and develop an agent-based system for merchandise management and the architecture and the knowledge of each agent in the system.

The proposed system will perform merchandise management autonomously and continuously in place of a human merchandise manager. In order to facilitate the agent’s intelligent behavior, several tools such as Data Envelopment Analysis (DEA), Genetic Algorithm (GA), Linear Regression and Rule Induction Algorithm are incorporated into the system.

This paper consists of five sections. Section 1 introduces background, motivation and objectives of this research. Section 2 explains previous works related to merchandise management systems and supply chain management. Section 3 describes the components of the proposed system and the architecture and functions of agents. Section 4 shows an application of the system using data from a real retail company. In Section 5, we conclude with limitations of this study and further works.

## 2. Literature review

## 2.1. Merchandise management system

Merchandise management consists of three major functions—Demand Forecasting, which involves Determining Needs; Purchasing, which includes Select Supplier and Negotiate Purchase; and Evaluating and Selecting, which includes Follow-up, from a functional point of view as shown in Fig. 1. In this section, we will explain those functions and introduce previously proposed systems by other researchers for each function.

## 2.1.1. Demand forecasting

The aim of demand forecasting is to estimate the amount of product and accompanying services that customers will require at some point in the future by using subjective analyses and/or conducting scientific statistical studies on the relevant historical data of the product [25]. Forecasting techniques can be grouped into three categories—qualitative methods, time series methods and casual methods [12]. Qualitative methods use qualitative data such as expert opinion and special information to forecast future needs. The Delphi technique is an example of a qualitative method. Time series methods are statistical techniques that are used when historical sales data are available with relatively clear and stable relationships and trends. However, because it assumes that the future will be similar to the past, it is effective only for shortterm forecasting. Examples of time series methods are moving averages, exponential smoothing, extended smoothing and adaptive smoothing. The casual methods use refined and specific information concerning variables to develop a relationship between a lead event and the event being forecasted. Regression analysis is a typical example [12].

![](/api/attachments/5927MBYC/fulltext/images/c8bf49faeab5dd0f466bea66cfbc8b5e8c04826c2cacd8d17afc2f463217bd1a.jpg)  
Fig. 1. Major functions of merchandise management and related work.

Before a forecasting technique can be exercised, one has to select the appropriate techniques that can make the best use of available data to achieve the required purpose [15]. Tammy Lo [15] illustrated an application of expert systems for the decision making of forecasting techniques selection. Lo explains professional heuristics and the reasoning process used in the selection problem and builds an expert system that captures the skill and aims to act as an advisor for choosing suitable demand forecasting techniques for use under various general business circumstances. Lo says that with expert systems as the consultation tools to perform the judgmental tasks, business people can generate desirable forecasts without the help of an expert forecaster. Korpela and Tuominen [12] proposed a decision support system of an Analytic Hierarchy Process (AHP)-based approach. AHP is a problem-solving framework and a systematic procedure for representing the elements of any problem [23]. Their decision support system offers many improvements compared with traditional methods and enables decision makers to avoid the problems inherent in traditional forecasting methods.

## 2.1.2. Purchasing

As shown in Fig. 1, purchasing includes Select Supplier and Negotiate Purchase processes. Merchandise managers should select the best supplier with respect to price and discounts, quality, reliability, services and accessibility and negotiate on cost price of the items, discounts, datings and transportation charges [17]. Research on purchasing assisting systems has been mainly for the manufacturing industry because the purchasing function has been recognized as making a significant contribution to a manufacturer’s success. However, the systems can also be good examples of purchasing of retailers because purchasing of manufacture’s is also done on the basis of the same factors as retailers consider in purchasing [6]. McIvor et al. [18] proposed a hybrid knowledge-based system that can assist in the area of strategic purchasing. The authors of the system claim that the proposed system act as a decision aid for a cross-functional team involved in the make or buy evaluation process and enhance the decisionmaking process in a core component of strategic purchasing.

## 2.1.3. Evaluating and selecting

Merchandise managers should evaluate merchandise and select desirable merchandise. These functions are very important to a retailer’s success but are timeexhaustive and difficult because a retailer usually handles a lot of items. Hence, retailers need a system that assists or undertakes the functions. Until now, most retailers depend on merchandise managers or a supportive staff for evaluating and selecting. They suggest the types of merchandise in each line that are likely to be bestsellers and those types that have no fashion appeal and are ready for removal [3].

## 2.2. Supply chain management

A supply chain is a network of facilities that procure raw materials, transform them into intermediary goods and then into final products and deliver the products to the customer through a distribution system [13]. However, because some retailers do not produce any product but just receive merchandise from their suppliers, there is no need for considering production issues in SCM. Instead of this, the retailer must make short-term and long-term plans for being supplied with merchandise [11]. Increasing competition and consumer awareness are forcing retailing firms to confront the challenging scenario of increasing revenues and decreasing operating costs at the same time [1]. Thus, there has been a lot of work in SCM by researchers in operational research. Starr and Miller [24] and Graves et al. [9] studied and developed models for inventory control. Gold [7] and others have discussed interactions between inventory problems and pricing. Chen and Min [5], Bhattacharjee and Ramesh [1] and others suggested dynamic pricing policies. Some research has attempted to synthesize the marketing –production interaction in some specific scenarios [1,22], and some recent research applied information technology to SCM. T.H. Kim [11] provided a management framework for retail companies under a SCM environment. S.H. Ha et al. [10] proposed a research framework that uses the methodology incorporated with data mining in achieving the objectives of identifying customers needs and consequently satisfying them. We propose a new approach to retail supply chain management by incorporating data mining tools such as GA, DEA and decision trees into merchandise management, which is a part of retail supply chain management.

## 3. Agent-based merchandise management system

Retail is the sale of goods or commodities in small quantities directly to consumers, and retailers act as intermediaries in the channels of distribution [17]. The retail cycle represents the following cycling sequential processes: Determine Inventory Need, Select, Order, Receive, Accept, Mark, Distribute, Receive, Display and Sell. These processes can be divided into three groups—merchandise management, merchandise processing management and store management. Merchandise management includes Determine Inventory Need, Select and Order. Processes from Receive to Distribute are those of merchandise processing management. The others are included in store management [14]. Merchandise management has been well represented by Mason et al. [17] as the buying cycle. The buying cycle has the following four processes [17].

. Determining Needs: The goal of this process is to establish or maintain inventory at the lowest possible level and still have a sufficient variety of colors, sizes, or models available from which customers can choose.

. Follow-up: This consists of continuous checking to find more desirable suppliers, merchandise, and buying and merchandise control practices.

. Select Supplier: After determining the merchandise needs, the merchandise manager must find a vendor or vendors who can supply the merchandise. If there are multiple suppliers, the merchandise manager should select the best supplier because some suppliers may be excellent, some acceptable and some less than desirable. Factors to be considered in determining the best supplier are price and discounts, quality, reliability, services and accessibility.

. Negotiate Purchase: In this process, the buyer has to try to get the best deal. For the best deal, he must negotiate on the cost price of the items, discounts, datings and transportation charges.

In Select Supplier and Negotiate Purchase, merchandise managers need to contact other suppliers and compare them and, thus, we call them external processes. On the contrary, Determining Needs and Follow-up are internal processes. In Determining Needs, the merchandise managers should predict how many of each item of merchandise will be needed and decide the optimal purchasing time simultaneously. In the Follow-up process, the merchandise managers should evaluate all the merchandise and select well-selling merchandise.

In B2B EC, an agent-based merchandise management system needs six agents—a Follow-up Agent, a Need-Determining Agent, a Supplier-Selecting Agent, a Purchase-Negotiating Agent, a Merchandise-Searching Agent and a Supervisor Agent. These agents can be classified into two groups—internal agents and external agents—according to their action domains.

Internal agents: The Supervisor Agent, Follow-up Agent and Need-Determining Agent do their jobs only in a company’s system, They do not meet or contact any other company’s agents. The Supervisor Agent supervises and controls all agents of the merchandise management system. It orders agents to execute their jobs. It receives information or knowledge from agents and stores and sends them to agents. The Follow-up Agent has knowledge of how to evaluate merchandise. It evaluates desirability, popularity, profitability, etc. of each merchandise. The Need-Determining Agent decides how many of each item of merchandise will be needed for selling and the optimal purchase time.

External agents: They travel in the B2B EC environment. These agents contact agents of other companies, request information on merchandise and suppliers and negotiate with them about purchase conditions. The Supplier-Selecting Agent searches vendors or suppliers who can supply the needed merchandise. It evaluates price and discounts, quality, reliability, services and accessibility of vendors and compares each vendor with the others. The Purchase-Negotiating Agent negotiates price, delivery and every related element with suppliers determined by the Supplier-Selecting Agent. The Merchandise-Searching Agent searches newly coming merchandise. It always searches for merchandise that has not been sold before at its store.

The proposed system in this paper consists of three agents and one module. The agents constituting the system correspond to the internal agents— the Supervisor Agent, Follow-up Agent and Need-Determining Agent. They cover the two internal process, Follow-up and Determining Needs among the four processes of the buying cycle. The module is Season Period Updating Module, which updates season period data using the sales history of each item of merchandise. The updated season period data are used by other agents.

The major functions of the proposed system are ‘evaluating and selecting merchandise’ and ‘predicting seasons and scheduling’.

Evaluating and selecting merchandise: The merchandise manager should clear out slow-selling merchandise and follow up bestsellers [3]. Moreover, he must search for new fast-selling merchandise. In other words, the merchandise manager should select fast-selling or desirable merchandise among existing ones and among newly suggested merchandise, respectively, in order to maintain as many fast-selling and desirable merchandise as possible at the store. The proposed system performs selecting merchandise functions autonomously and continuously.

Predicting seasons and scheduling: Seasonal merchandise is in demand at certain times of the year. Although some seasonal merchandise can be acquired during a high-demand season, many items cannot be obtained quickly enough at this time. Hence, seasonal merchandise is best bought well in advance of the season [17]. So the prediction of seasons is necessary for accurate demand forecasting and should be the beginning of the ordering process. The proposed system predicts the beginning point and the end point of high-demand seasons of each item of merchandise with its sales history using Genetic Algorithm [8]. After that, the system builds not only schedules of evaluation, replenishment and supplier selecting, but it also arranges the next scheduling point based on the predicted season time. Agents in the system perform their jobs according to the schedules. Demand forecasting for seasonal merchandise should also be based on the predicted season time. The system forecasts the demand quantity of each item of merchandise during every predicted season using forecasting techniques introduced in Section 2.1.

Agents in the system perform the functions collaboratively. Evaluating and selecting merchandise are performed by the Follow-up Agent through its functions—merchandise evaluation, merchandise classification and updating knowledge of merchandise classification. Predicting season and scheduling are performed by the Need-Determining Agent through its functions—predicting season periods and building a replenishment schedule. The Supervisor Agent manages the other agents according to schedules that are updated by the Need-Determining Agent and the Supervisor Agent. The Season Period Updating Module supports the agents by updating season period data.

## 3.1. The architecture of intelligent software agents

Since the late 1980s, the concept of an agent has become important both in Artificial Intelligence (AI) and in mainstream of computer science [27]. Moreover, intelligent agent is a new paradigm for developing software applications and is being used in an increasingly wide variety of applications [20].

The intelligent agent has 10 characteristic properties that differentiate them from traditional software programs. The characteristics of intelligent agents can be grouped into the two larger categories of internal and external properties. Internal properties are those that form the ‘internal being’ of an agent, that is, the properties that determine the actions within the agent. Internal properties include Autonomy, Learning, Productivity, Goal-Orientedness, Reactivity and Mobility. External properties include all those characteristics that affect the interaction of several agents or human –agent communication. These are Communication, Cooperation and Coordination. The Character of an agent, for which significant parts determine the internal behavior of an agent but which also plays an important role in the external communication, belongs to both groups [2].

Agent architecture deals with the construction of computer systems that satisfy the properties specified by agent theorists [27]. More specifically, agent architecture is defined as a ‘Particular methodology for building [agents]. It specifies how. . .the agent can be decomposed into the construction of a set component modules and how these modules should be made to interact. . .An architecture encompasses techniques and algorithms that support this methodology’ [16]. Existing agent architectures can be grouped into three categories—Deliberative Architecture, Reactive Architecture and Hybrid Architecture. Deliberative Architecture is a classical approach to building agents, namely, a particular type of knowledge-based system and is defined to be one that contains an explicitly represented symbolic model of the world. Decisions in it are made via logical reasoning based on pattern matching and symbolic manipulation [27]. The modeling of the environment is the main component of the deliberative agent’s knowledge base but because of the high complexity of representation of such an environment, deliberative agents have only limited suitability for use in dynamic environments. Deliberative agents are usually represented by a BDI (belief, desire, intention) agent [2]. The deliberative agent has two major problems. Its structure is too rigid for it to work in very dynamic environments [2], and it seems hard to build useful symbol manipulation algorithms that will be guaranteed to terminate with useful results in an acceptable fixed time boundary [27]. Reactive Architecture is defined to be one that does not include any kind of central symbolic world model and does not use complex symbolic reasoning [27]. Reactive agents are compact, error-tolerant and flexible and suffice to precisely observe the environment and to recognize a range of simple principles or dependencies. The principles and dependencies are used to develop task-specific modules that are capable of continuously checking their environment for the occurrence of specific situations and to initiate a direct reaction when such a situation occurs [2]. However, unlike deliberative agents, reactive agents cannot use their internal knowledge base to dynamically generate and follow new goals. This bears the question whether, and if yes, to what extent, reactive agents are capable of demonstrating a goal-oriented behavior [2]. Many researchers agree that neither a completely deliberative nor completely reactive approach is suitable for building agents, and they have attempted to combine the two previous approaches [27]. The result is Hybrid Architecture. Hybrid Architecture possesses both a reactive component and a deliberative one. The reactive one usually interacts with the environment and the deliberative one builds plans and makes decisions. Hybrid systems are normally designed as a hierarchical architecture with an increasing degree of abstraction [2]. Combining multiple interaction subsystems is the major problem of this approach. It is not clear that current hybrid architectures can manage different levels of abstract behavior [27].

The architecture of the agents in the proposed system can be regarded as a Deliberative Architecture, but it is simpler than the BDI structure. The intelligence of an agent is formed from three main components: its internal knowledge base, the reasoning capabilities based on the contents of the knowledge base and the ability to learn or to adapt to changes to the environment (adaptive behavior) [2]. The two main facilities of the proposed agents are Operation Facility (Reasoning Facility) and Knowledge Base. The adaptive behavior of the proposed agents is actualized by Operation Facility and Knowledge Base for adaptation. The architecture of the proposed agents in this paper is similar to that of the Intelligent Decision Support Agents proposed by Wang [26]. Fig. 2 is the description of our agent architecture.

Agents perform their allocated functions, which are described in their own knowledge base, continually. If it is needed, they update some part of their knowledge base according to methods that are also described in their own knowledge base. When carrying out functions, the agents read, add, update and delete data in the database. The database is divided into five sub-data sets —Schedules, Season Periods, Histories, Merchandise Profiles and Merchandise Code Structure. The Schedules data set includes the starting points of all major functions of the agents. The Season Periods data set has information on season periods of merchandise. In the Histories data set, Sales Histories and Inventory Histories of merchandise are stored. Merchandise Profiles include the lead times and references of merchandise. Merchandise Code Structure is the retail shop’s rules for putting codes on merchandise.

## 3.2. Agent-based merchandise management system

The proposed system consists of three agents and one module as shown in Fig. 3. We introduced their roles briefly when describing the internal agents of the agent-based merchandise management system in B2B EC. In this section, we will explain their functions in detail.

## 3.2.1. Season Period Updating Module

This module updates season periods—the beginning points and the end points of all seasons—using the sales history of each item of merchandise. The updating process consists of two steps, Segmenting and Classifying.

3.2.1.1. Segmenting. In this step, the module segments sales records of each item of the merchandise into several intervals in each of which sales records show a linear trend, as shown in Fig. 4. For segmenting, Genetic Algorithm and regression analysis are used.

![](/api/attachments/5927MBYC/fulltext/images/751b873d01bbb4082497e28e3fcb16c1d147bd75957f25b7dd905e6efb640122.jpg)  
Fig. 2. The architecture of agent.

![](/api/attachments/5927MBYC/fulltext/images/cde09993b488b531eb3df1e83ced96e17853645f1d56988231ac1af9b70d8830.jpg)  
Fig. 3. Agent-based merchandise management system.

The left graph of Fig. 4 shows the change of sales according to time. Intuitively, one can see that the sales records can be partitioned into four intervals. However, machines do not have such an ability. Genetic Algorithm and Linear Regression are applied to provide this ability to this module.

Genetic Algorithm evolves a population of solutions by applying genetic operators such as selection, crossover and mutation to search for an optimal solution. At every generation, GA calculates the fitness value for each solution in the population with which the genetic operators are applied and is optimized by GA through generations. Eq. (1) is the definition of the fitness function of Genetic Algorithm, which is used in the segmenting step of the Season Period Updating Module.

$$
\begin{array}{l} \text { Fitness } = \alpha \sum_ {i = 1} ^ {\mathrm{NI}} R _ {i} ^ {2} w _ {i} + \beta F (\mathrm{NI}) \\ \mathrm{NI} = \text { no.   of   intervals } \quad w _ {i} = \frac {\text { no.   of   periods   in   the   ith   interval }}{\text { no.   of   whole   periods }} \\ R _ {i} ^ {2} = R ^ {2} \text {   of   the   ith   interval } \\ F (\mathrm{NI}) \propto \frac {1}{\mathrm{NI}}, 0 \leq F (\mathrm{NI}) \leq 1 \quad 0 \leq \alpha \leq 1, 0 \leq \beta \leq 1, \alpha + \beta = 1 \end{array} \tag {1}
$$

A solution in the population is a possible way for segmenting the sales records and is encoded into a binary format. For example, the sales records consist of 15 points in Fig. 4. In this case, each solution is represented by 15 binary digits. The right graph of Fig. 4 is one of the solutions and the binary representation is $( 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 )$ , which means that the solution segments the sales records into four intervals and the first, second, third and fourth intervals are from the 1st to 5th point, from the 5th to 8th point, from the 8th to 12th point and from the 12th to 15th point, respectively.

![](/api/attachments/5927MBYC/fulltext/images/5af4b123b84740b00cbdd42bb98fc363e915f9bc81a57316c7f5df0e826d67bf.jpg)  
Fig. 4. Segmenting sales records.

The first term of Eq. (1) estimates the linearity of the sales trend of each interval by $R ^ { 2 }$ and calculates the weighted sum of the $R ^ { 2 }$ values of all intervals. The $w _ { i }$ is the weight of the ith interval and is the ratio of the length of the interval to the length of all of the periods. A period is the distance between two adjacent points and the sales records of Fig. 4 includes 14 periods because it has 15 points. Therefore, the first term shows the weighted sum of the linearity of every interval. However, if the sales records are segmented so that every period becomes an interval, then the sales records are divided into 14 intervals and $R ^ { 2 }$ values of all intervals become 1, and the first term of Eq. (1) has the maximum value, a. This is why the second term of Eq. (1) exists. It estimates the efficiency of segmenting. Because it is in inverse proportion to the number of intervals, it becomes the smallest when every period becomes an interval. Therefore, the best solutions in the population segment the sales records as sparsely as possible. a and b are the weight values for those two terms. These values should be determined so that the fitness values from Eq. (1) can accurately represent the appropriateness of the solutions for specific problems. By the effects of the two terms of Eq. (1), the solutions in the population evolve to segment the sales records into as small the number of intervals, each of which has a linear trend, as possible.

3.2.1.2. Classifying. In this step, the module classifies the segmented intervals into two classes, highdemand seasons and low-demand seasons. For that purpose, first, the average sales of each interval should be computed. If the average sales of an interval are greater than that of the total records, then it is a high-demand season. If the average sales are lower than those of the total records, it is a low-demand season.

## 3.2.2. Supervisor Agent

The Supervisor Agent supervises and manages all the processes of the proposed system. The Supervisor Agent has three functions—merchandise evaluation management, scheduling and new merchandise management.

3.2.2.1. Merchandise evaluation management. According to the Merchandise Evaluation Schedule, the Supervisor Agent carries out and manages the process of merchandise evaluation. Through this process, merchandise purchasing decision for the next period is made.

The agent observes the Merchandise Evaluation Schedule and when it is time for the evaluation on items of merchandise, the Supervisor Agent executes the process of evaluating. Before evaluating, the Supervisor Agent requests the Season Period Updating Module to update the season period data of the merchandise because season period data, which include the beginning points and the end point points of seasons, are needed for the evaluation. After updating of the season period data, the Supervisor Agent orders the Follow-up Agent to evaluate the desirability of the merchandise. Then the Follow-up Agent evaluates the desirability and delivers the results to the Supervisor Agent. With the evaluation results, the Supervisor Agent decides whether to buy the merchandise next time or not. If repurchase of it is rejected, the Scheduling Schedule of the merchandise will be deleted. This process is described in Fig. 5 in detail.

3.2.2.2. Scheduling. The Supervisor Agent manages scheduling of all processes. There are four schedules—a Merchandise Evaluation Schedule, a Scheduling Schedule, a Replenishment Schedule and a Supplier-Selecting Schedule. The Replenishment Schedule represents when and how many of each item of merchandise should be delivered to the company’s warehouse. The Supplier-Selecting Schedule informs when the Supplier-Selecting Agent should find appropriate suppliers for the merchandise. Each item of merchandise should be evaluated for the system to determine whether to buy it or not. The evaluation is accomplished according to the Merchandise Evaluation Schedule. After the evaluation, a Replenishment Point, a Supplier-Selecting Point and a Next Merchandise Evaluating Point are determined at the reserved Scheduling Point in the Scheduling Schedule and the Next Scheduling Point is also reserved after all those schedules are built. Fig. 6 shows an example of schedules.

![](/api/attachments/5927MBYC/fulltext/images/501281fd73dd9f321568f7d1acf59468d28538e957a18804d9653b4693226f1a.jpg)  
Fig. 5. Merchandise evaluation management.

Fig. 7 describes the scheduling process in detail. The Supervisor Agent orders the Need-Determining Agent to build the Replenishment Schedule and builds itself a Supplier-Selecting Schedule according to the Scheduling Schedule. The Replenishment Schedule should be decided because other schedules are built based on it. The Supervisor Agent orders the Need-Determining Agent to build the Replenishment Schedule. Then, the Supervisor Agent builds the Supplier-Selecting Schedule taking the Replenishment Schedule into account. The Supplier-Selecting

![](/api/attachments/5927MBYC/fulltext/images/fd4428885dd700ef9b8f6484f27baee9ccc48f2b2efd5668f680be541fdeccd3.jpg)  
Fig. 6. An example of schedules.

![](/api/attachments/5927MBYC/fulltext/images/b501ed27b04a12406d2c84b081eb064869ebb7f1da554485a97d0be2d352cf88.jpg)  
Fig. 7. Scheduling.

Point should be determined so that replenishment (or delivery) of the merchandise should not be late. In this regard, the lead time should be considered because the supplier-selecting point is the beginning point of the ordering process, which includes selecting an appropriate supplier, negotiating with the supplier and ordering merchandise. Merchandise evaluation should be performed just after the end of the season of the merchandise and because of that, when building the Merchandise Evaluating Schedule, the predicted season period should be taken into account. In addition, the Next Scheduling Point should be reserved so that it can be carried out directly after the merchandise evaluation.

3.2.2.3. New merchandise management. Whenever new merchandise is suggested, the Supervisor Agent carries out the process of predicting the desirability of it, namely, predicting whether it will sell well or not and decides whether to buy it or not (Fig. 8). The Follow-up Agent evaluates the desirability of it and makes the decision based on the evaluation results. If buying the new merchandise is rejected, its profile will be deleted. If buying the new merchandise is accepted, the Replenishment Schedule, Supplier-Selecting Schedule, Merchandise Evaluating Schedule and Next Scheduling Schedule will be built in the same way as the scheduling of existing merchandise is carried out.

## 3.2.3. Follow-up Agent

The Follow-up Agent evaluates the desirability of existing merchandise and predicts that of new merchandise. Functions of the Follow-up Agent include merchandise evaluation, merchandise classification and updating knowledge of merchandise classification.

3.2.3.1. Merchandise evaluation. The measures commonly used for evaluating desirability of merchandise are Sales Results, Inventory Results and Margin Results [3]. Sales Results may be measured in dollars, in units of merchandise (or in number of sales transactions) or in sales per square foot of selling space, and increase is commonly a more important factor than actual volume. Inventory Results are revealed by Stockturn, the proportion of old stock carried over to the new season or year, and merchandise shortage and its percentage to sales. Stockturn is defined as ‘‘sales for a period divided by the average amount of inventory during the period’’. The period most commonly used is 1 year, although it is sometimes computed for half-yearly periods, or on a monthly basis. Margin Results include four levels of profit—Initial Markup (aggregate original retail price less aggregate invoice costs), Gross Margin Realized (final selling price less cost of goods sold, commonly reflecting cash discounts and alteration costs), Controllable Margin Realized (gross margin less direct department expenses) and Operating Profit Realized (gross margin less all expense chargeable to the selling department).

![](/api/attachments/5927MBYC/fulltext/images/1cd3f5ff0008336106cfe590c0b041534c98204007a6ba1fe906158aa2557c74.jpg)  
Fig. 8. New merchandise management.

The three factors that must be covered in the evaluation—Sales Results, Inventory Results and Margin Results—can be represented by the past sales history and inventory history. The Follow-up Agent considers five measures for the evaluation—the sales revenue during the last season, the sales volume during the last season, the inventory at the beginning of the last season, the amount paid for purchasing merchandise sold during the last season and Trend of Sales, which can be extracted from the past sales history or inventory history. Trend of Sales is the degree of the increase of sales. If the sales of the last season are greater than that of the same season of the preceding, then Trend of Sales will be greater than 1, and if less, it will be less than 1.

The desirability of merchandise represents whether it has sold well or not and whether it will sell better or not in the future. For determining the former, its sales during a high-demand season and its inventory at the beginning of the season must be considered. If the sales were large, the merchandise is selling well. Though the sales were small, we cannot say that it is selling poorly if the inventory was small and it was sold out during the season. Furthermore, for determining whether merchandise will sell better or not, its trend of sales must be considered. If the sales are increasing, the merchandise gets a higher desirability point. This is why Trend of Sales is considered in the evaluation of the desirability of merchandise.

DEA is used as the evaluation tool. DEA estimates the relative technical efficiency of units involving multiple inputs and outputs. In contrast to parametric approaches whose object is to optimize a single regression plane through the data, DEA optimizes on each individual observation with an objective of calculating a discrete piecewise frontier determined by the set of Pareto-efficient decision-making units (DMUs) where DMUs are the observations in the given population. DEA calculates a maximal performance measure for each DMU relative to all other DMUs in the observed population with the sole requirement that each DMU lie on or below the extremal frontier. The Pareto-efficient DMUs are the most efficient observations in terms of the given inputs and outputs. For each inefficient DMU (one that lies below the frontier), DEA identifies the sources and level of inefficiency for each of the inputs and outputs. The level of inefficiency is determined by comparison to a single referent DMU or a convex combination of other referent DMUs located on the efficient frontier that utilize the same level of inputs and produce the same or a higher level of outputs [4].

The inventory at the beginning of the season and the total amount of money used for buying the merchandise are inputs, and the sales quantity and total sales revenue during the season and the sales trend are outputs of DEA analysis. With those inputs and outputs, DEA compares merchandise and shows the efficiency of each item of merchandise. The efficiency value ranges from 0 to 1. The lower the input value is, the higher the efficiency is, and the higher the output value is, the higher the efficiency is. If the efficiency of merchandise is high, the merchandise is selling well or its sales are increasing. For that reason, the efficiency from DEA can be used as the measure of the desirability of merchandise. Table 1 is an example of DEA results.

We can see in Table 1 that DMU-2 and DMU-3 are on the efficient frontier because their relative efficiency evaluated by DEA is 1, which is the maximum value. This means that the items corresponding to them are most desirable in respect to the cost, the inventory, the sales revenue, the sales volume and the trend because DEA considered the five measures simultaneously during the evaluation process. The item corresponding to the DMU-2 shows extremely fast growth in sales though it does not have superiority in other measures. The item of the DMU-3 also has a relatively large positive trend value, namely sales increase. Though the sales increase of the item of the DMU-3 is much lower than that of the DMU-2, the price of the item of DMU-3 is much higher than that of the DMU-2. In other words, the item of the DMU-3 is more profitable than that of DMU-2. Dividing sales revenue by sales volume shows simple comparison of the profitability of DMUs. This is why DMU-3 is on the efficient frontier with DMU-2, together. Although the trend of DMU-9 is similar to that of the DMU-3, the efficiency of the DMU-9 is very low. This is because the profitability of DMU-9 is much lower than that of the DMU-3. This can also be confirmed by dividing the sales revenue by the sales volume for each DMU.

An example of DEA results

<table><tr><td>DMU</td><td>Cost ($)</td><td>Inventory(no.)</td><td>Sales ($)</td><td>Sales(no.)</td><td>Trend</td><td>Efficiency</td></tr><tr><td>1</td><td>38156</td><td>4102</td><td>42734</td><td>4032</td><td>0.63</td><td>0.929294</td></tr><tr><td>2</td><td>2594</td><td>478</td><td>2803</td><td>478</td><td>28.12</td><td>1</td></tr><tr><td>3</td><td>1453</td><td>18</td><td>2116</td><td>18</td><td>3</td><td>1</td></tr><tr><td>4</td><td>678251</td><td>4554</td><td>771470</td><td>4554</td><td>0.43</td><td>0.12292</td></tr><tr><td>5</td><td>264721</td><td>2340</td><td>281871</td><td>2340</td><td>0.58</td><td>0.592888</td></tr><tr><td>6</td><td>11932</td><td>269</td><td>17660</td><td>269</td><td>1.63</td><td>0.990514</td></tr><tr><td>7</td><td>309479</td><td>2935</td><td>336709</td><td>2935</td><td>1.19</td><td>0.541719</td></tr><tr><td>8</td><td>87296</td><td>3180</td><td>116705</td><td>3180</td><td>1.15</td><td>0.895442</td></tr><tr><td>9</td><td>252206</td><td>6354</td><td>313547</td><td>6354</td><td>2.28</td><td>0.690965</td></tr><tr><td>10</td><td>8089</td><td>155</td><td>11076</td><td>155</td><td>1.89</td><td>0.99151</td></tr><tr><td>11</td><td>227106</td><td>1578</td><td>233190</td><td>1578</td><td>1.11</td><td>0.635986</td></tr></table>

3.2.3.2. Merchandise classification. As explained before, existing merchandise can be evaluated based on the five measures. However, the five measures cannot be used for new merchandise because the system does not have any sales history, inventory history or purchasing history. So the Follow-up Agent predicts the desirability of new merchandise using the knowledge of merchandise classification, which is extracted from sales, inventory and purchasing histories of existing merchandise and is usually represented as rules. After prediction of the desirability of merchandise, the system selects desirable merchandise from new goods based on the predicted desirability.

The agent uses rules for predicting the desirability of each item of merchandise. These rules are represented as a decision tree, as in Fig. 9.

The decision tree in Fig. 9 shows how to classify merchandise according to its merchandise code. If the merchandise code consists of eight digits in which the first four digits represent Brand and the next two parts of digits represent Department and Style, respectively, then merchandise of a code ‘12073116’, would be included in Class 3 in Fig. 9. Each class is a homogeneous merchandise group with respect to desirability.

![](/api/attachments/5927MBYC/fulltext/images/1af743b0404bde3e7ff590b71624b78f7cb22eac194a10cdd56d1951dfd9a112.jpg)  
Fig. 9. An example of knowledge of merchandise classification.

3.2.3.3. Updating knowledge of merchandise classification. Knowledge of merchandise classification, namely the rules such as Fig. 9, has to be updated because the desirability of merchandise changes as time goes. The Follow-up Agent updates its knowledge of merchandise classification in order to adapt to the changes. The updating process has two steps, clustering merchandise according to their desirability and building rules for classification.

(a) Clustering merchandise: To divide merchandise into classes according to their efficiency level, DEA is performed iteratively. First, perform DEA with the whole merchandise and extract merchandise of efficiency 1. This is the most desirable merchandise (Class 1). Then perform DEA again with the remaining merchandise and then extract merchandise of efficiency 1 from them again. These are less desirable merchandise than those of Class 1. Continue this process until there are no remaining merchandise or the number of remaining items of merchandise becomes less than a given minimum number. Merchandise, which remain until the end of the process, are the least desirable goods.

(b) Building rules for classification: Through the clustering step, merchandise are divided, namely they are classified into several classes so that members of each class have a similar desirability value and the classes have different desirability levels. In Fig. 10, M1 and M4 are in the most desirable merchandise class, and M5 and M8 are in the least desirable one.

The agent builds rules for classification with the clustering results like Fig. 10 and attributes of merchandise such as merchandise code. In most retail shops, each item of merchandise is linked to its unique merchandise code according to their merchandise code structures. The merchandise code has the most important information of each item such as the item’s brand, department, style and so on. The agent prepares a training data set for building the rules by integrating merchandise information known by the merchandise code and the clustering results, which show the desirability level of each merchandise. Based on the training data set, the agent builds rules for classifying merchandise into several classes of different desirability levels according to the merchandise code. Fig. 11 is an example of training data set.

![](/api/attachments/5927MBYC/fulltext/images/9ce4b86510e0468b97c1ac55e0ac726b665078a480c14a3f4a98326ffa268bee.jpg)  
Fig. 10. Clustering merchandise with DEA.

In order to build such rules with the training data set, inductive inference methods can be applied. In this paper, we used C5.0, one of the decision tree learning methods [21]. Decision tree learning is one of the most widely used and practical methods for inductive inference. It approximates discrete-valued target functions, in which the learned function is represented by a decision tree. Decision tree learning methods have been successfully applied to a broad range of tasks from learning to diagnose medical cases to learning to assess credit risk of loan applicants [19]. Fig. 9 is an example of rules for merchandise classification represented by a decision tree.

## 3.2.4. Need-Determining Agent

The Need-Determining Agent builds Replenishment Schedules of all merchandise and predicts the season periods, namely the beginning points and the end points of all seasons, and updates the predicted season periods of merchandise in the database.

3.2.4.1. Predicting season periods. The Need-Determining Agent should predict merchandise season periods before building the Replenishment Schedule, which is made based on the predicted season periods. Each of the season periods is represented by its beginning and end points. After predicting season periods, the sales quantity during the season can also be predicted by forecasting techniques.

(a) Predicting season periods of existing merchandise: In this case, season periods of previous years, which are updated by the Season Period Updating Module, are used for predicting or determining the next season period. One of the following three methods can be used. $b _ { 1 }$ and $e _ { 1 }$ are the beginning and end points, respectively, of a season period of the last year, and $b _ { 2 }$ and $e _ { 2 }$ are those of the year previous to that.

![](/api/attachments/5927MBYC/fulltext/images/a067c1b5b97af42a6a4b3b9ad8857fd417b89b7add066387d14a96ce9b3c272f.jpg)  
Fig. 11. An example of training data set.

(1) Determine the season period as the last year’s season period. ! b = b1, e = e1

(2) Set the season period as the average of the past several years’ season periods. !b=(b1+b2)/2, $\scriptstyle \mathtt { e } = ( { \mathrm { e } } 1 + { \mathrm { e } } 2 ) / 2$

(3) Set the beginning point of the season period as the earliest beginning point of those of the past several years’ season periods and the end point of the season as the latest end point of those of the past several years’ season periods. !b = min{b1, b2}, e = max{e1, e2}

(b) Predicting season periods of new merchandise: In this case, the Need-Determining Agent has to predict the season period using similar merchandise season periods. The agent must look for similar merchandise using the merchandise code structure, in other words, it must search for existing merchandise with the most similar code to that of the new one and then use its predicted season period as that of the new one.

3.2.4.2. Building a replenishment schedule. The Need-Determining Agent builds the Replenishment Schedule of merchandise given by the Supervisor Agent. It determines when the replenishment of the merchandise should be finished, in other words the time until which the ordered merchandise is delivered to the retailer’s warehouse. Though the decision depends on the inventory strategies of the company, we can suggest a simple general strategy for seasonal merchandise: Seasonal merchandise must be delivered until the season begins. Moreover it is better for the delivery to be just before the beginning of the season. Thus, the Replenishment Schedule should be built based on the predicted season periods.

After the Replenishment Schedule is determined by the Need-Determining Agent, the Supervisor Agent determines the Supplier-Selecting Schedule based on theReplenishmentScheduleandthemaximumleadtime of the merchandise. According to the Supplier-Selecting Schedule, the Supervisor Agent orders the Supplier-Selecting Agent to select an appropriate supplier.

## 4. Application

We evaluated our system with data from an existing duty-free shop. The merchandise manager of the duty-free shop handles tens of thousands of items of merchandise and hundreds of brands. Hence, it has been very difficult for him to determine which merchandise should be ordered, when to order and how many units of each items of merchandise should be ordered. Moreover he needs to find deteriorating merchandise and dispose of them and has to predict whether new merchandise suggested by suppliers will sell well or not. Until now, he has depended on simple reports on merchandise sales, proposals of sale representatives and his own experience. However, these are very time-consuming and inaccurate methods. In this chapter, we will show that those tasks of the merchandise manager can be performed by the proposed intelligent software agents by testing the functions of the agents with the real data from the duty-free shop.

## 4.1. Merchandise code structure

The left portion of Fig. 12 represents the base merchandise code structure of the duty-free shop. Boxes are attributes of the code structure. In each of the boxes, there is an attribute name and the number in parentheses is the size of the attribute in the code structure. For example, the ‘Brand’ attribute and the ‘Department’ attribute consist of four digits and two digits, respectively. ‘Brand’ is the maker of each item of merchandise and ‘Division’ indicates whether it is domestic or not. ‘Group’ is for classifying merchandise into merchandise groups. ‘Department’ is for more refined classification than ‘Group’. The five types explain features of the merchandise, and these are defined for each item of merchandise independ ently. The types are usually used for color, material, style, size, shape, sex, etc. The right portion of Fig. 12 is an example of a merchandise code. The code of the merchandise is ‘1163F17540302120105’. It means that the merchandise is of ‘Fendi’ and imported. It is included in the ‘Wear’ merchandise group, more specifically in ‘Sunglasses’. It is of ‘Sport’ style and lenses are ‘Solid Tint, Polarized and Plastic’. The frame of the sunglasses is ‘Silver and Full Frame’. Colors of lenses and frame are ‘Black’ and ‘Brown’, respectively. However, the duty-free shop has not used the merchandise code structure entirely. ‘Brand’, ‘Division’, ‘Group’ and ‘Department’ have been set correctly, but types has not. For that reason, we will use just the first nine digits of the merchandise code in this paper.

![](/api/attachments/5927MBYC/fulltext/images/9ec30f96b97138c877caac4df07dd9fe5ad80e4d09df921019287b54331bad82.jpg)  
a) Base Code Structure b) An example of merchandise code  
Fig. 12. Merchandise code structure.

## 4.2. Merchandise evaluation

The main functions of the merchandise evaluation process are updating season period and evaluating merchandise as described in Sections 3.2.1 and 3.2.3, respectively. In this section, we will show practices of those two functions with the real data.

## 4.2.1. Updating season period data

We used sales data from 1998/10/1 to 1999/9/30 in the database of the duty-free shop for testing the functions of Season Period Updating Module proposed in Section 3.2.1. We segmented the sales data so that sales records of each segment have a linear trend and classifies each of the segments into highdemand season or low-demand season, as explained in Section 3.2.1. Fig. 13 is an example of the segmenting results.

Fig. 13 shows the sales records of the merchandise group of ‘1163F1721’, of which the brand is ‘Fendi’, the division is ‘Foreign’, the group is ‘Wear’ and the department is ‘Bag’, for every week from 1998/10/1 to 1999/9/30, along with the results of segmenting the sales records. The sales records were divided into 13

![](/api/attachments/5927MBYC/fulltext/images/54487575d26196e1cc9d623b79af2327254e65ce8105b22ddd3909aa802a6165.jpg)  
Fig. 13. Sales records of ‘1163F1721’ from 1998/10/1 to 1999/9/30 and the results of segmenting.

Table 2

<table><tr><td colspan="5">(a) The results of classifying the segmenting results in Fig. 13</td></tr><tr><td>Period</td><td>Beginning week</td><td>End week</td><td>Average sales</td><td>Season</td></tr><tr><td>1</td><td>1</td><td>6</td><td>453</td><td>High</td></tr><tr><td>2</td><td>6</td><td>8</td><td>979.3</td><td>High</td></tr><tr><td>3</td><td>8</td><td>10</td><td>1863.7</td><td>High</td></tr><tr><td>4</td><td>10</td><td>16</td><td>49.7</td><td>Low</td></tr><tr><td>5</td><td>16</td><td>18</td><td>59</td><td>Low</td></tr><tr><td>6</td><td>18</td><td>21</td><td>1027.2</td><td>High</td></tr><tr><td>7</td><td>21</td><td>22</td><td>1902</td><td>High</td></tr><tr><td>8</td><td>22</td><td>25</td><td>800.2</td><td>High</td></tr><tr><td>9</td><td>25</td><td>30</td><td>649.7</td><td>High</td></tr><tr><td>10</td><td>30</td><td>31</td><td>371</td><td>High</td></tr><tr><td>11</td><td>31</td><td>36</td><td>140.2</td><td>Low</td></tr><tr><td>12</td><td>36</td><td>50</td><td>98.5</td><td>Low</td></tr><tr><td>13</td><td>50</td><td>53</td><td>255.5</td><td>Low</td></tr></table>

(b) Season period

<table><tr><td>Code</td><td>From</td><td>To</td><td>Demand</td><td>Average</td><td>Total</td></tr><tr><td>1163F1721</td><td>1997/10/1</td><td>1997/11/17</td><td>High</td><td>423</td><td>2960</td></tr><tr><td>1163F1721</td><td>1997/11/19</td><td>1998/2/7</td><td>Low</td><td>25</td><td>299</td></tr><tr><td>1163F1721</td><td>1998/2/9</td><td>1998/5/16</td><td>High</td><td>436</td><td>6099</td></tr><tr><td>1163F1721</td><td>1998/5/18</td><td>1998/9/30</td><td>Low</td><td>33</td><td>618</td></tr><tr><td>1163F1721</td><td>1998/10/1</td><td>1998/12/5</td><td>High</td><td>840</td><td>8401</td></tr><tr><td>1163F1721</td><td>1998/11/28</td><td>1999/1/30</td><td>Low</td><td>47</td><td>332</td></tr><tr><td>1163F1721</td><td>1999/2/1</td><td>1999/5/06</td><td>High</td><td>631</td><td>8818</td></tr></table>

intervals. The average sales volume during the term is 370.9 (units). The Season Period Updating Module classifies every period during which the average sale volume is greater than 370.9 into a high-demand season and other periods into low-demand seasons. Table 2(a) shows the results of the classifying. There are two high-demand seasons from 1998/10/1 to 1999/ 9/30. The first high-demand season is from the 1st to the 10th week, namely from about 1998/10/1 to about 1998/12/5. The second high-demand season is from the 18th to the 31st week, in other words, from about 1999/1/25 to about 1999/5/1. The Season Period Updating Module inserts these season period data into the database like Table 2(b). In Table 2(b), we did not add the season period from the 31st to the 53rd week because we could not decide the end point of the season period from the segmenting results in Fig. 13. As you can see in Table 2(b), the newly acquired season period data of the merchandise group ‘1163F1721’ during the term from 1998/10/1 to 1999/9/30 are added to the previous season period data until 1998/9/30.

## 4.2.2. Merchandise evaluation

The performance during the last high-demand season, which is acquired in Section 4.2.1 of each item of merchandise of the duty-free shop, is evaluated by the method proposed in Section 3.2.3. As explained in Section 3.2.3, the five measures—the inventory at the beginning of the season, the total amount of money used for buying the merchandise, the sales quantity, the total sales revenue during the season and the sales trend—are retrieved from the database in the duty-free shop and are used in the DEA analysis.

Table 3 shows the results of merchandise evaluation. As explained before, the desirability, namely the efficiency in DEA, of each item of merchandise represents popularity and profitability of the item. In Table 3, we can see that ‘1163F1721’ is one of the most desirable because its desirability is 1, which is the maximum. On the other hand, ‘1084F1721’ has relatively low desirability.

## 4.3. Determining needs and scheduling

## 4.3.1. Predicting season period

After the last high-demand season, from 1999/02/ 01 to 1999/05/06, the Need-Determining Agent should predict the next high-demand season. In Table 2(b), the second highest demand season had begun at 1997/10/1 and had ended at 1997/11/17 in 1997. In 1998, the second highest demand season was from 1998/10/1 to 1998/12/5. As explained in Section 3.2.4, there are several predicting methods. Here, we chose the second method among the three introduced in Section 3.2.4. It computes the average of the beginning and end points of the second seasons of the previous years. So the predicted next high-demand season is from 1999/10/1 to 1999/11/26 and the merchandise, of which the merchandise code is ‘1163F1721’, must be replenished before 1999/10/1. Thus, we determined 1999/10/1 as the replenishment point.

Table 3  
Desirability

<table><tr><td>Brand</td><td>Division</td><td>Group</td><td>Department</td><td>Desirability</td></tr><tr><td>1042</td><td>F</td><td>17</td><td>21</td><td>0.966483</td></tr><tr><td>1078</td><td>F</td><td>17</td><td>21</td><td>0.993698</td></tr><tr><td>1058</td><td>F</td><td>17</td><td>21</td><td>0.998482</td></tr><tr><td>1061</td><td>F</td><td>17</td><td>21</td><td>0.91316</td></tr><tr><td>1060</td><td>F</td><td>17</td><td>21</td><td>0.930298</td></tr><tr><td>1083</td><td>F</td><td>17</td><td>21</td><td>0.999602</td></tr><tr><td>1084</td><td>F</td><td>17</td><td>21</td><td>0.632905</td></tr><tr><td>1099</td><td>F</td><td>17</td><td>21</td><td>0.983956</td></tr><tr><td>1100</td><td>F</td><td>17</td><td>21</td><td>0.921565</td></tr><tr><td>1139</td><td>F</td><td>17</td><td>21</td><td>0.998744</td></tr><tr><td>1135</td><td>F</td><td>17</td><td>21</td><td>0.991983</td></tr><tr><td>1163</td><td>F</td><td>17</td><td>21</td><td>1</td></tr><tr><td>1207</td><td>F</td><td>17</td><td>21</td><td>0.945103</td></tr><tr><td>1200</td><td>F</td><td>17</td><td>21</td><td>0.585098</td></tr><tr><td>1262</td><td>F</td><td>17</td><td>21</td><td>0.997035</td></tr><tr><td>1340</td><td>F</td><td>17</td><td>21</td><td>0.987671</td></tr><tr><td>1378</td><td>F</td><td>17</td><td>21</td><td>0.954844</td></tr><tr><td>1380</td><td>F</td><td>17</td><td>21</td><td>0.997859</td></tr><tr><td>1370</td><td>F</td><td>17</td><td>21</td><td>0.988552</td></tr><tr><td>1374</td><td>F</td><td>17</td><td>21</td><td>0.975069</td></tr><tr><td>1462</td><td>F</td><td>17</td><td>21</td><td>0.824283</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr></table>

![](/api/attachments/5927MBYC/fulltext/images/ed5f479b780818e1a2684e645b8b075c64caf858be039897880cd2725d71cafa.jpg)  
Fig. 14. Schedules.

The quantity of the merchandise to be replenished includes the predicted sales quantity during the next high-demand season and low-demand season because replenishment only for a low-demand season is not performed. In 1997, the sales quantity during the high-demand season corresponding to the next highdemand season was 2960 and that of the next lowdemand season was 299. In 1998, 8401 units of the merchandise were sold during the corresponding highdemand season and 332 units during the next lowdemand season. The replenishment quantity should be decided on the basis of previous sales and other knowledge. Simply, the average sales of the previous seasons can be used as the predicted sales or any other forecasting models can be used to forecast the sales during the relevant periods, the next high-demand season and low-demand season.

## 4.3.2. Scheduling

After the replenishment point is determined by the Need-Determining Agent, the supplier-selecting point, the evaluation point and the next scheduling point should be determined by the Supervisor Agent. Fig. 14 shows each of them for ‘1163F1721’.

The supplier-selecting point is at the lead time of the merchandise from the replenishment point. The lead time of ‘1163F1721’ is 2 months and, hence, the supplier-selecting point is ‘1999/08/01’. The merchandise evaluation point is at some days, here a week, after the end point of the high-demand season. The scheduling point is just after the evaluation point.

Results of clustering

<table><tr><td>No.</td><td>Brand</td><td>Division</td><td>Subdivision</td><td>Department</td><td>Class</td></tr><tr><td>1</td><td>8005</td><td>D</td><td>11</td><td>35</td><td>6</td></tr><tr><td>2</td><td>8710</td><td>D</td><td>11</td><td>35</td><td>3</td></tr><tr><td>3</td><td>8708</td><td>D</td><td>11</td><td>35</td><td>1</td></tr><tr><td>4</td><td>1014</td><td>F</td><td>11</td><td>35</td><td>8</td></tr><tr><td>5</td><td>1032</td><td>F</td><td>11</td><td>35</td><td>5</td></tr><tr><td>6</td><td>1083</td><td>F</td><td>11</td><td>35</td><td>9</td></tr><tr><td>7</td><td>1084</td><td>F</td><td>11</td><td>35</td><td>4</td></tr><tr><td>8</td><td>1109</td><td>F</td><td>11</td><td>35</td><td>5</td></tr><tr><td>9</td><td>1135</td><td>F</td><td>11</td><td>35</td><td>3</td></tr><tr><td>10</td><td>1163</td><td>F</td><td>11</td><td>35</td><td>6</td></tr><tr><td>11</td><td>1160</td><td>F</td><td>11</td><td>35</td><td>8</td></tr><tr><td>12</td><td>1207</td><td>F</td><td>11</td><td>35</td><td>8</td></tr><tr><td>13</td><td>1261</td><td>F</td><td>11</td><td>35</td><td>11</td></tr><tr><td>14</td><td>1475</td><td>F</td><td>11</td><td>35</td><td>9</td></tr><tr><td>15</td><td>8005</td><td>D</td><td>17</td><td>21</td><td>4</td></tr><tr><td>16</td><td>8818</td><td>D</td><td>17</td><td>21</td><td>9</td></tr><tr><td>17</td><td>8708</td><td>D</td><td>17</td><td>21</td><td>1</td></tr><tr><td>18</td><td>1031</td><td>F</td><td>17</td><td>21</td><td>12</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td>308</td><td>1100</td><td>F</td><td>17</td><td>31</td><td>9</td></tr><tr><td>309</td><td>8435</td><td>D</td><td>14</td><td>53</td><td>3</td></tr><tr><td>310</td><td>1163</td><td>F</td><td>11</td><td>23</td><td>8</td></tr><tr><td>311</td><td>1375</td><td>F</td><td>11</td><td>52</td><td>1</td></tr><tr><td>312</td><td>1100</td><td>F</td><td>11</td><td>51</td><td>2</td></tr><tr><td>313</td><td>1130</td><td>F</td><td>12</td><td>41</td><td>5</td></tr><tr><td>314</td><td>8005</td><td>D</td><td>17</td><td>22</td><td>6</td></tr><tr><td>315</td><td>8710</td><td>D</td><td>17</td><td>32</td><td>7</td></tr><tr><td>316</td><td>1100</td><td>F</td><td>17</td><td>54</td><td>5</td></tr><tr><td>317</td><td>1065</td><td>F</td><td>15</td><td>11</td><td>3</td></tr><tr><td>318</td><td>1433</td><td>F</td><td>15</td><td>11</td><td>9</td></tr></table>

```txt
BRAND = 1001: 6 (1.0)
BRAND in {1002,1004,1006,1009,1012,1013,1015,1030,1034,1039,1040,1068,1071,1072,
    1079,1080,1086,1102,1103,1107,1108,1111,1131,1138,1161,1169,1205,1206,
    1210,1212,1231,1237,1238,1260,1300,1330,1333,1335,1336,1360,1369,1373,
    1376,1377,1473,1474,1500,1502,1505,1529,1530,1532,1533,1536,1538,1560,
    1569,1570,1620,1621,1622,1641,1642,8104,8107,8112,8113,8120,8122,8125,
    8204,8208,8209,8210,8302,8306,8402,8403,8405,8410,8411,8413,8427,8428,
    8431,8434,8437,8503,8504,8602,8709,8801,8822,8823,8903,8904,8905,8906,
    8907,8908,8909,8910,8911,8912,8913,8914}: 6 (0.0)

BRAND = 1008: 6 (1.0)
BRAND = 1014: 8 (4.0/1.0)
BRAND = 1031: 12 (4.0/2.0)
BRAND = 1032: 10 (7.0/4.0)
BRAND = 1033: 12 (1.0)
BRAND = 1036: 12 (1.0)
BRAND = 1037: 13 (1.0)
BRAND = 1038: 10 (1.0)
BRAND = 1041: 11(1.0)
BRAND = 1042: 6 (3.0/2.0)
BRAND = 1043: 2 (1.0)
BRAND = 1058: 2 (4.0/3.0)
BRAND = 1060: 7 (9.0/5.0)
BRAND = 1062: 1 (2.0)
BRAND = 1064: 4 (1.0)
BRAND = 1065: 3 (2.0)
BRAND = 1066: 5 (1.0)

BRAND = 8710: 3 (5.0/4.0)
BRAND = 8719: 2 (1.0)
BRAND = 8818: 9 (1.0)
BRAND = 8821: 4 (3.0/2.0)
BRAND = 8901: 7 (2.0/1.0)
BRAND = 1061:
...GROUP in {11, 13, 14, 16}: 9 (0.0)
: GROUP = 12: 1 (2.0/1.0)
: GROUP = 15: 9 (2.0/1.0)
: GROUP = 17: 11 (5.0/3.0)
BRAND = 1084:
...GROUP = 11: 4 (2.0/1.0)
: GROUP in {12, 13, 14, 16}: 4 (0.0)
: GROUP = 15: 8 (1.0)
: GROUP = 17: 5 (6.0/4.0)
BRAND = 1200:
...GROUP = 11: 6 (2.0/1.0)
: GROUP = 12: 3 (1.0)
: GROUP in {13, 14, 16}: 2 (0.0)
: GROUP = 15: 3 (2.0/1.0)
: GROUP = 17: 2 (8.0/5.0)
BRAND = 1400:
...GROUP = 11: 2 (1.0)
GROUP = 12: 7 (2.0/1.0)
GROUP in {13, 14, 16}: 12 (0.0)
GROUP = 15: 10 (1.0)
GROUP = 17: 12 (2.0)
```  
Fig. 15. Classification knowledge.

Table 5  
An example of prediction

<table><tr><td>No.</td><td>Brand</td><td>Division</td><td>Group</td><td>Department</td><td>Code</td><td>Class</td></tr><tr><td>1</td><td>Delicato</td><td>Domestic</td><td>Accessory</td><td>Pen</td><td>8909D1123</td><td>6</td></tr><tr><td>2</td><td>Channel</td><td>Foreign</td><td>Beauty</td><td>Perfume</td><td>1062F1241</td><td>1</td></tr><tr><td>3</td><td>Barrie</td><td>Foreign</td><td>Wear</td><td>Clothing</td><td>1037F1731</td><td>13</td></tr><tr><td>4</td><td>Baume and Mercier</td><td>Foreign</td><td>Jewelry</td><td>Watch</td><td>1033F1511</td><td>12</td></tr><tr><td>5</td><td>Han&#x27;s Raft</td><td>Domestic</td><td>Wear</td><td>Clothing</td><td>8908D1731</td><td>6</td></tr><tr><td>6</td><td>Calvin Klein</td><td>Foreign</td><td>Beauty</td><td>Perfume</td><td>1085F1241</td><td>2</td></tr><tr><td>7</td><td>Kimex</td><td>Domestic</td><td>Wear</td><td>Belt</td><td>8912D1724</td><td>6</td></tr><tr><td>8</td><td>Hermes</td><td>Foreign</td><td>Wear</td><td>Tie</td><td>1230F1733</td><td>7</td></tr><tr><td>9</td><td>Celine</td><td>Foreign</td><td>Accessory</td><td>Key chain</td><td>1084F1123</td><td>4</td></tr><tr><td>10</td><td>Celine</td><td>Foreign</td><td>Jewelry</td><td>C. Jew</td><td>1084F1514</td><td>8</td></tr></table>

## 4.4. New merchandise evaluation

In this section, we will show the functions for new merchandise evaluations, merchandise classification and updating knowledge of merchandise classification, which are explained in Section 3.2.3.

## 4.4.1. Updating knowledge of merchandise classification

Table 4 shows the result of clustering merchandise of applying DEA iteratively according to the method described in Fig. 10. The number of merchandise groups used in clustering is 318. Those are sold in the duty-free shop from 1998/10/1 to 1999/9/30. The 318 merchandise groups are clustered into 13 classes. Members of classes of low numbers are more desirable than those of classes of high numbers. Therefore, members of Class 1 are the most desirable merchandise groups, and those of Class 13 are the least desirable ones.

We extracted merchandise classification knowledge from the clustering results by the method introduced in the updating knowledge of merchandise classification function in Section 3.2.3. Fig. 15 shows the merchandise classification knowledge represented by a decision tree. For example, if the brand code of one of the items of merchandise is ‘1062’, which means ‘Channel’, then the merchandise is included in Class 1, the most desirable one. Merchandise with the brand code of ‘1601’, which means ‘Christian Dior’, and a group code of ‘12’, which means a ‘Beauty group, is also included in Class 1. The ‘Beauty’ group includes ‘Perfume’ and ‘Cosmetic’ departments. However, the ‘17’ group of that brand, namely the ‘Wear’ group of ‘Christian Dior’ is not desirable because it is included in Class 11.

## 4.4.2. Predicting the desirability of new merchandise

We can predict the desirability of new merchandise with the knowledge of merchandise classification. Let us assume that ‘Nina Ricci’, which has a brand code ‘1400’, suggested a new ‘Key Chain’. The Division, Group and Department of the ‘Key Chain’ are ‘Foreign’, ‘Accessory’ and ‘Key Chain’, respectively, and their codes are ‘F’, ‘11’ and 23’. So the merchandise code of the suggested merchandise is ‘1400F1123’. It is included in Class 2 by classification knowledge in Fig. 15. Table 5 shows other examples of prediction.

In Table 5, the second, ‘Perfume’ of ‘Channel’, and the sixth, ‘Perfume’ of ‘Calvin Klein’, are predicted to be desirable, and the Supervisor Agent would decide to purchase them. However, ‘Clothing’ of ‘Barrie’ is included in the worst class, and the Supervisor Agent would reject purchasing it. The Supervisor Agent should decide whether to buy new merchandise or not with the desirability predicted by the Follow-up Agent.

## 5. Conclusion and further works

Merchandise management of retail companies includes selecting desirable merchandise, disposing of slow-selling ones, finding the best supplier who can supply the chosen merchandise and negotiating with them about purchasing and making an order.

Until recently, most retailers have depended on human beings for merchandise management, and, thus, retailers have employed many merchandise managers for that purpose. Nevertheless, it has been impossible for merchandise managers to evaluate and compare all of the merchandise, to find appropriate suppliers, to negotiate with them and to order efficiently. Today, however, the tasks can be taken over by intelligent software agents and, moreover, in the agent-based virtual marketplace under B2B EC, merchandise management should be in charge of agents for retailers to respond quickly to the dynamic change of customer need and interact with suppliers efficiently. The proposed agent-based system performs merchandise management autonomously and continuously. It evaluates the desirability of merchandise and selects more desirable goods. It also predicts the desirability of new merchandise. After evaluating and selecting, the system builds schedules for replenishment, selecting suppliers and negotiating. The results of this research can be summarized as following.

(1) Autonomous merchandise management by an agent-based system.

Predicting high-demand seasons autonomously: The system segments sales records according to sales patterns and finds high-demand seasons of every merchandise using Genetic Algorithm and Linear Regression. In addition, the system forecasts customer demand and builds replenishment schedules based on the predicted high-demand season.

Evaluating and selecting merchandise autonomously: The system evaluates merchandise soon after every high-demand season and selects merchandise for selling in the next high-demand season.

Predicting the desirability of new merchandise autonomously: The system predicts the desirability of new merchandise based on the knowledge of merchandise classification, which is updated autonomously by agents in the system whenever it is necessary.

Building schedules of purchasing autonomously: The system builds schedules of purchasing such as replenishment schedules and supplier-selecting schedules.

(2) Incorporating analysis tools into knowledge of intelligent software agents: In this paper, several analysis tools such as GA, DEA and C5.0 were used in order to enhance the intelligence of software agents, and it was proven to be very effective.

Merchandise management by intelligent software agents will be important in B2B EC because intelligent software agents should accomplish most transactions such as selecting suppliers, negotiating, etc., which until now have been performed by human beings. Hence, the significance of this research is that it is a new trial of developing intelligent software agents for the retail industry, especially for merchandise management in B2B EC. In B2B EC, retail companies can also utilize intelligent software agents for selecting suppliers, purchase negotiating and searching merchandise, which are the tasks of external agents, as explained in Section 3. For that purpose, however, significant related research such as a standard protocol for communication between agents and standard merchandise code structures should be performed. This is our future research.

## References

[1] S. Bhattacharjee, R. Ramesh, A multi-period profit maximizing model for retail supply chain management: an integration of demand and supply-side mechanisms, Eur. J. Oper. Res. 122 (2000) 584– 601.

[2] W. Brenner, R. Zarnekow, H. Wittig, Intelligent Software Agent—Foundation and Applications, Springer-Verlag, Berlin, 1998.

[3] R.P. Cash, J.W. Wingate, J.S. Freidlander, Management of Retail Buying, Wiley, New York, 1995.

[4] A. Charnes, W.W. Cooper, A.Y. Lewin, L.M. Seiford, Data Envelopment Analysis: Theory, Methodology and Application, Kluwer Academic Publishers, Dordrecht, 1994.

[5] C. Chen, K.J. Min, A multiproduct EOQ model with pricing consideration—T.C.E Cheng’s model revisited, Comput. Ind. Eng. 26 (1994) 787–794.

[6] D.W. Dooley, D.N. Burt, L. Lee, Purchasing and Materials Management, McGraw-Hill, New York, 1990.

[7] F. Gold, Modern Supermarket Operations, 3rd edn., Fairchild Publications, New York, 1981.

[8] D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Addison-Wesley Publishing, Reading, Massachusetts, 1989.

[9] S.C. Graves, A.H.G. Rinnooy Kan, P.H. Zipkin, Handbooks in OR&MS 4, Elsevier, Amsterdam, 1993.

[10] S.H. Ha, S.M. Bae, T.H. Kim, S.C. Park, Customer focus in supply chain management incorporated with data mining, Proceedings of the 2nd Asia – Pacific Conference on Industrial

Engineering and Management Systems, Kanazawa, Japan, JI-MA (Japan Industrial Management Association), Tokyo, 1999, pp. 401 – 404.

[11] T.H. Kim, A Study on Supply Chain Management Model Based on Critical Database, KAIST, Daejeon, Korea, 1998.

[12] J. Korpela, M. Tuominen, Inventory forecasting with a multiple criteria decision tool, Int. J. Prod. Econ. 45 (1996) 159 – 168.

[13] H.L. Lee, C. Billington, The evolution of supply-chain-management models and practice at Hewlett-Packard, Interfaces 25 (5) (1995) 42 – 63.

[14] W.J. Lee, Retailer’s Cost Savings with Quick Response Implementation: Department Store Case, Graduate School of Management, Korea Advanced Institute of Science and Technology, Daejeon, Korea, 1998.

[15] T. Lo, An expert system for choosing demand forecasting techniques, Int. J. Prod. Econ. 33 (1994) 5 – 15.

[16] P. Maes, The Agent Network Architecture (ANA), SIGART Bull. 2 (4) (1991).

[17] J.B. Mason, M.L. Mayer, H.F. Ezell, Retailing, 4th edn., IR-WIN, Homewood, IL, 1991.

[18] R.T. McIvor, M.D. Mulvenna, P.K. Humphreys, A hybrid knowledge-based system for strategic purchasing, Exp. Syst. Appl. 12 (4) (1997) 497–512.

[19] T.M. Mitchell, Machine Learning, McGraw-Hill, New York, 1997.

[20] J.P. Mueller, M. Wooldridge, N.R. Jennings, Intelligent Agents III, Lecture Notes in Artificial Intelligence, vol. 1193, Springer-Verlag, Berlin, 1997.

[21] J.R. Quinlan, C4.5: Programming for Machine Learning, Morgan Kaufmann Publishers, San Mateo, California, 1993.

[22] A. Rajan, A. Rakesh, R. Steinberg, Dynamic pricing decisions in single period inventory systems, Int. J. Prod. Econ. 23 (1992) 240 – 262.

[23] T.L. Saaty, Priority setting in complex problems, IEEE Trans. Eng. Manage. (1983) 140–155.

[24] K.M. Star, W.D. Miller, Inventory Control: Theory and Practice, Prentice-Hall, Englewood Cliffs, NJ, 1962.

[25] J.R. Stock, D.M. Lambert, Strategic Logistics Management, Irwin, Homewood, IL, 1987.

[26] H. Wang, Intelligent agent-assisted decision support systems: integration of knowledge discovery, knowledge analysis and group decision support, Exp. Syst. Appl. 12 (3) (1997) 325 – 335.

[27] M. Wooldridge, N.R. Jennings, Intelligent agent: theory and practices, Knowl. Eng. Rev. 10 (2) (1995) 23 – 36.

![](/api/attachments/5927MBYC/fulltext/images/6d355b546b191bf8ad90c1ced7a3eb727a12025d6d34532648aefb4917a59751.jpg)

Jae Heon Park is a PhD candidate at the Department of Industrial Engineering of Korea Advanced Institute of Science and Technology (KAIST). He received his BS degree in management science and MSc degree in industrial engineering from KAIST. His research interests include Artificial Intelligence, Machine Learning, Data Mining, Knowledge Based Systems,

Electronic Commerce, Customer Relationship Management.  
![](/api/attachments/5927MBYC/fulltext/images/35afe2503cea3bd00c1836a10c0c22cf1305f43fd7481890d7e36fb70aaa4bf8.jpg)

Sang Chan Park is a professor at the Department of Industrial Engineering of Korea Advanced Institute of Science and Technology (KAIST). He received his MBA degree from the University of Minnesota, Minneapolis, and his PhD degree in MIS from the University of Illinois, Urbana. He was an Assistant Professor of Information Systems Design and Analysis, School of Business at the University of

Wisconsin, Madison, before participating in the faculty of KAIST. His research specialization is in the areas of Artificial intelligence, Total Quality Management, Knowledge Based Systems, Data Warehousing, Electronic Commerce, Customer Relationship Management and Educational Engineering. His articles have appeared in Decision Support Systems, Encyclopedia of Microcomputers, IEEE Transactions on Neural Networks, Expert Systems with Applications, IEEE Transactions on Knowledge and Data Engineering, International Journal of Production Economics, Annals of Operations Research, IEEE Transactions on Robotics and Automation, Processing and Management, European Journal of Operational Research, Canadian Journal of Civil Engineering, Journal of Information Technology Management, IEEE Transactions on Systems, Man and Cybernetics, IIE Transactions—Institute of Industrial Engineering, Lecture Notes in Artificial Intelligence.
