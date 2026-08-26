---
otero_id: 22174
otero_key: "PSUUPBH4"
title: "Business process integration as a solution to the implementation of supply chain management systems"
authors: "Takashi Kobayashi; Masato Tamaki; Norihisa Komoda"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00102-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Business process integration as a solution to the implementation of supply chain management systems

Takashi Kobayashi<sup>a,\*</sup>, Masato Tamaki<sup>a</sup>, Norihisa Komoda<sup>b</sup>

<sup>a</sup>Business Solution Systems Division, Hitachi Ltd., 890 Kashimada, Saiwai, Kawasaki, Kanagawa 212-8567, Japan <sup>b</sup>Department of Multimedia Engineering, Graduate School of Information Science and Technology, Osaka University, 2-1 Yamadaoka, Suita, Osaka 565-0871, Japan

Received 3 February 2002; received in revised form 10 August 2002; accepted 13 October 2002

## Abstract

In the domain of supply chain management (SCM), various software packages have been developed for planning business strategies. To solve the problem of system productivity in applying planning packages, we propose a solution concept, business process integration (BPI), which fuses workflow and enterprise application integration (EAI) technology. Two characteristic policies are included in BPI. The first is to design the minimum set of business processes for real-time information sharing with planning packages without changing other processes. The second is to integrate several systems with EAI technology and to manage their execution with a workflow tool. Based on these policies, we propose various design templates and integration adapters. Our evaluation shows that using BPI, a target system can be developed with less manpower, in less time, and with higher quality than previous methods.

<sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Supply chain management; Business process; Workflow; Enterprise application integration; Information sharing; Design template; Integration adapter

## 1. Introduction

Internet technology has drastically changed our way of doing business. Using the World Wide Web, any valuable business information can easily be accessed anywhere and anytime. As a consequence, the need for designing new business processes has increased; this is sometimes called an e-process [10], with the assumption that there are no barriers between departments and enterprises. On the other hand, the internet has also changed the status of the market place. Product information can be exchanged instantly, and market competition is becoming global in scope. This situation drastically shortens the product life cycle, which is the time between the release of a product and the end of its sales. As a result, it is necessary to develop flexible business processes that are easily adaptable to market change [7,9].

Much attention has been focused on the management methodology of supply chain management (SCM), which integrates business processes from suppliers to consumers and manages various tasks, such as sales, manufacturing, logistics, and finance. A number of software packages have been developed for planning business strategies according to this methodology [8,15]. To apply the planning packages, two work elements are necessary: (1) a total optimal design of the business process to organize the supply chain, and (2) an integration of the design of the planning packages and the legacy systems. In general, a great deal of manpower is required for this.

Here, we discuss the problem of system productivity in developing SCM system. To solve this, we propose a solution: business process integration (BPI) which fuses workflow and enterprise application integration (EAI) technology.

## 2. Traditional techniques

## 2.1. System productivity problems

In traditional production systems where product demand is relatively stable, it is sufficient to study local optimization only for such isolated tasks as sales, manufacturing, logistics, and finance, and to merge them into a total planning scheme using batch processing. Recently, it has become difficult to adapt to radical changes in demand using only local optimization. It is necessary to share real-time business information and to synchronize all tasks using transaction processing. Supply chain planning (SCP) is a software package developed for this situation; it can quickly and correctly coordinate the demand (from the sales side) with the supply (from the production side) [2]. With SCP, we can repeatedly develop production/sourcing plans according to changes in business status and select the optimal set of actions from the viewpoint of the total supply chain. One of the most important points for applying SCP is a real-time response to obtain realtime sales, production, sourcing, and inventory information and to send planning results rapidly to the field [1]. The other important need is for flexible system construction to develop the appropriate system according to changes of the business environment.

Therefore, the central themes in applying SCP are:

(1) a business process design problem: to design the optimal business process so that tasks organizing the supply chain can synchronize in real-time;

(2) an information system design problem: to design, as quickly as possible, an integrated system for sharing business information and managing the business process.

![](/api/attachments/PSUUPBH4/fulltext/images/b5bc17d9c2ae481e19032dc6012ec3f06af9303cd3546a21ba08f5e4c50cb560.jpg)  
Fig. 1. Business process design problem.

## 2.2. Business process design

Business process design is a kind of optimization problem. As shown in Fig. 1, business process design sets the relations between tasks, orders, and actors so that the target business will achieve its goal under the given constraints [11,12]. The tasks are function units that divide the business into multiple actors. Thus, the function levels to be assigned are changed according to each actor’s organizational size and ability. The orders are task execution sequences, including parallel and sequential relations. Its goal is to increase the speed of delivery and the quality and reduce the cost for supplying products or services to customers. The constraints may be classified into following.

\- Rule constraints including laws, company rules, and customs.

\- Organizational constraints including the authorities and duties of the organization.

\- Resource constraints including the human and information resources available for executing business processes.

The business process design problem usually cannot be solved because the constraints are too strict. Thus, to design a business process to achieve a new goal, the constraints have to be relaxed. Similar approaches are taken in coordination theory [14,17]. The components of this are goals, activities, actors, and interdependences. The activities indicate the tasks and the interdependences show both the task orders and the constraints.

Business process design requires skill and manpower and must be executed by three types of specialists— business experts, consultants, and information engineers. In our case studies, business design took about 20% of the total development effort. A well-known solution is the reference model, used by SCP venders; it is a set of recommendations with examples developed from experiences when applying SCP [3,16]. It generally consists of business process and data models and is intended to make the cost of business process design less than that of designing from scratch. In the real world, however, a trade-off approach is adopted, finding a compromise point between the reference model and the current business process, because goals and constraints are different for each user. Namely, the current business process is changed according to the reference model or it is customized according to the current business process. This coordination process requires inspection, analysis, and discussion by business experts, consultants, and information engineers. In general, because such specialists are very busy, these activities become a bottleneck and greatly prolong the project schedule.

## 2.3. Information system design

SCM is the total optimization of multiple business processes by introducing computer systems. Moreover, each business process has generally been partly com puterized. Developing a SCM system from scratch requires time and money. This approach therefore usually leads to frustration and sometimes to failure.

A well-known solution is EAI technology, which was recently proposed [4]. EAI integrates various applications and shares information among them with differences in execution environments, programming languages, operation policies, etc. EAI is generally categorized by the system architecture into message and data integration.

\- Message integration is messaging and data transformation technology enabling all applications used in a real-time processing style to communicate by messaging. It is used to exchange data between the outer channel and inner core business systems. A type of middle-ware called a message broker is usually used.

\- Data integration is a file transport and data transformation technology enabling all applications in a batch processing style to communicate through the database. It is used to exchange data among the inner core business systems in different departments. A type of middle-ware called ETL (extract transform loader) is usually used.

These integration technologies mainly focus on data exchange among multiple applications, and almost all the integration middle-wares provide a variety of adapters—message/data transformation functions. By using these middle-wares, the development cost for integration programs can be reduced to some degree. However, an SCM system cannot be developed by using only adapter programs. It is necessary to develop a business process management system, which monitors the start/stop timing of every application and executes the adapter programs. It is also necessary to split/join the transactions in moving from one task to another, because each task generally has its own transaction size. Developing such a business process management program requires enormous manpower and reduces maintainability.

## 3. BPI solution

To solve these problems, we propose a solution we call BPI (business process integration), which fuses workflow and EAI technology. Two characteristic policies are included in BPI. First, we propose two key technologies: a business process modeling method, and a workflow-based EAI architecture. Then, we describe the components of a BPI solution.

## 3.1. The business process modeling method

There is a clear reason why it takes much manpower to compromise between the reference model and the existing business process or ‘as-is business process.’ The problem is that essential and trivial business processes are often mixed without there being any priority specified for each. Consequently, the reference model includes constraints about enterprise rules, organizations, and resources that are too detailed. In applying SCP, complete business process re-engineering is generally useless. As the goal of SCP is real-time information sharing between the demand side and the supply side of various resources, it is important to clarify who should share the information and to design the minimum set of task execution order for the interactions between them. There are two ways of applying SCP.

\- Coordination between the demand of the sales side and the supply of the production side in making a production plan.

\- Coordination between the demand of the production side and the supply of the suppliers in making the sourcing plan.

These two processes are termed a business process template.

The method of business process modeling is to model the business process in a hierarchical structure, depending on the strength of the processes related to the goal, as shown in Fig. 2. The highest level of the business process consists only of direct interactions between the original customer and the original performer of the target problem. This is the ‘main process.’ The hierarchical levels of business processes become lower as the problem is decomposed into separate elements and they are subcontracted to other people as ‘sub-processes.’ Generally, the main process has a stable structure, because the main process is generated by the interaction of two people—the original customer and performer—and the effect of the rule, organizational, and resource constraints becomes small enough to be ignored. On the other hand, the subprocess has variable structure according to a variety of constraints. In order to design the business process template, it should be extracted from the main process. SCP was developed for sharing real-time information between the demand side and the supply side of various resources. The main process defines the inter-departmental actions and these are improved by using SCP. However, the sub-process defines the intra-departmental actions and these show in detail how to provide the input data to SCP and use the output data from SCP.

By extracting the main process as the business process template, it can be reused among various enterprises and the manpower of the business process design can be reduced. For the sub-processes that are impossible or very hard to reuse, as-is processes and legacy systems can be substituted.

For example, the business process template for a sourcing solution can be constructed for the process shown in Fig. 3. This solution overcomes the challenge of balancing the product demand forecast and the resource supply capacity in real-time with a high speed material requirement planning (MRP) package: MRP is one kind of SCP used to calculate when and how many parts will be needed. MRP enables quicker and more correct sourcing planning. In general, the input data to MRP is the master production schedule, material inventory, and material backlog. The output data is its material requirements. Because MRP plays the central role in the sourcing solution, the business process template for the solution has only to include the minimum set of interaction sequences between persons who must share the input/output information in real-time.

![](/api/attachments/PSUUPBH4/fulltext/images/4c5719d3992d85e141c05dd0a8cc3af2adc5f880b0c1271e311ee14017ef500e.jpg)  
Fig. 2. Business process hierarchy.

![](/api/attachments/PSUUPBH4/fulltext/images/8a7ed05e4d3651f7f565e9f686c0d9c347a8185356bca6f062c439be9697c2f9.jpg)  
Fig. 3. Business process template for sourcing process.

Here, the production planning main process involves setting the weekly production plan though the process is executed monthly. The customer is the sales department and the performer is the production department. The interaction between them consists of three basic tasks: ‘forecast demand,’ ‘balance demand with supply,’ and ‘plan production.’ The first is the task in which the sales department prepares the product demand information and requests production planning to the production department. The second is the task in which the sales department and the production department negotiate the gap between the product demand forecast and the resource supply capacity. MRP is used to calculate the material requirements based on the production demand forecast and estimates the product supply based on the material supply capacity. The last is the task in which the production department makes the production plan based on the negotiation result. Shared information is as follows.

\- input: product demand, material inventory, and material backlog;

\- output: production plan (weekly).

The next step is in planning the main process where the daily sourcing plan is produced. This process is executed weekly. In this process, the customer is the production department and the performer is the sourcing department. The sourcing planning process consists of: ‘identify material requirements,’ ‘balance requirements with resources,’ and ‘plan sourcing. The first is the task in which the production department requests sourcing planning to the sourcing department based on the production plan. The second is the task in which the production and the sourcing department negotiate the gap between the material demand forecast and the material supply capacity. MRP is used to calculate the material requirement based on the result of production planning. The last is the task in which the sourcing department makes the plan based on the negotiation result. The shared information is:

\- input: production plan (weekly), material inventory, and material backlog;

\- output: sourcing plan (daily).

In order to realize the sourcing solution, two addi tional business processes are indispensable: production and sourcing management. The production management process makes product based on the production plan and manages the product inventory and product backlog. The sourcing management process acquires material based on the sourcing plan and manages the material inventory and material backlog. These two are the sub-processes, because they do not contribute to the goal of SCP, real-time information sharing, and they only create the input information and use the output information of the main processes. Therefore it is not useful to make specifications of these processes.

Only the minimum set of business processes, the framework of the solution, is defined as the business process template. The lower level business processes can be designed freely. Therefore, it is sufficient to incorporate as-is business processes or legacy systems at this level. For example, the internal process of ‘forecast demand’ task above was not defined in the template, so the legacy sales management system can be substituted for its internal process. Therefore, rather than attempting a total optimization requiring enormous manpower and time, we can improve the business process step-by-step with smaller risk and larger effect.

When the essential business process for real-time information sharing is designed as the business process template, the data model for the shared information can be defined as the input/output data of the tasks in the business process template. An example of a data model template is shown in Fig. 4; the boxes show the data entities of the shared information, the diamonds show the relations between the data entities, and the loops show individual data items for each data entity [5]. The data model template is used as the intermediate format for data transformation.

## 3.2. Workflow-based EAI architecture

Workflow-based EAI is a system architecture that implements EAI according to the business process, as shown in Fig. 5, and consists of three elements: business process, adapters, and applications. The business process includes tasks, actors, arrows, and control nodes [13]. The tasks are the logical steps, which show the execution states of application. The arrows and control nodes show the state transition among tasks. The integration workflow controls the execution of tasks according to the business process model. In this architecture, all the communication between each application and the workflow or among the applications is executed through the adapters. Through these, each task function is linked to a variety of applications: the as-is business process, the legacy system, and SCP. Because the execution timing and data flow of the applications are controlled by the workflow, the flowspecific properties are removed from the applications and left to the business process model. Therefore, the system productivity and maintainability are improved.

![](/api/attachments/PSUUPBH4/fulltext/images/0414e91c44542259fc35dac055ed33a60d33634504805a28390caf66e01135a7.jpg)  
Fig. 4. Data model template for sourcing process.

![](/api/attachments/PSUUPBH4/fulltext/images/538d997181976baf7b98970a34cc95a396db13005883a86dff13cdfd08c72a32.jpg)  
Fig. 5. Workflow-based EAI architecture.

The adapters fall into three categories: application initiator, status detector, and data transformer. Appli cation initiator is the adapter to initiate applications by data condition, timer, or alarm. Status detector is the adapter to detect the occurrence of various events; for example the completion of the applications and the change of application states. These events are acquired by monitoring periodically the data items that the applications update. Data transformer is the adapter to extract the data from the source applications, transform the data format, and load the data to the target applications. Fig. 6 shows the structure of the adapter, which consists of the input interface, output interface, converter, and middle-ware interface. Input interface is the function to get the data from the source applications. For example, if the application is RDB (relational data base), the interface is implemented with structured query language (SQL) and if the application is enterprise resource planning (ERP), the interface is implemented with an application program interface (API). Output interface is the function to put the data to the target applications. This interface is also implemented with SQL or API. Converter is the function to convert the input data format to the output data format. The data format includes the number of digits, data type, character code, and so on. Middle-ware interface is the function to transfer the control data from the applications to the workflow or from the workflow to the applications. By using these adapters, it is not necessary to change any application program in integrating multiple systems.

The integration workflow, three types of adapters, and a development support tool are bundled in a CORBA-based application server.

## 3.3. BPI solution components

A BPI solution consists of products, knowledge, and services for developing the business system and is based on the two methods described before: the business process modeling method, and the workflow-based EAI architecture.

![](/api/attachments/PSUUPBH4/fulltext/images/ef5328e0c3d089bce08f372eddf5e656795407f6c063ac1e5f654367943942c4.jpg)  
Fig. 6. Structure of adapter.

As shown in Table 1, products, knowledge, and services are provided in each development phase: business design, system design, or implementation. In the business design phase, the business process template and data model template are provided for each business domain. Therefore, activities for busi ness process re-engineering, business process design, and data model design can be executed without any experts. The system integration template—the linkage map of the business process template, the adapters, and typical applications—is provided in the system design phase. The typical applications include de facto standards such as ERP (enterprise resource planning) packages, relational databases, and so on. The data transformation template—the standard intermediate format for data transformation—is also provided. In the implementation phase almost all the program code of the adapter, workflow, and database are automatically generated by each definition tool, based on the design results from the system design phase.

## 4. System development procedure

The system development procedure consists of three phases: the business design, system design, and implementation. The designing activities are categorized into the process related and the data related ones. In each phase, two BPI key technologies—the business process modeling method and the workflowbased EAI architecture—are applied. The outline of the system development procedure is shown in Fig. 7.

Table 1 BPI solution components

<table><tr><td>Development phase</td><td>Products</td><td>Knowledge</td><td>Services</td></tr><tr><td>Business design</td><td>SCP functionWorkflow definition toolDatabase definition tool</td><td>Business process templateData model template</td><td>BPR serviceBusiness process design serviceData model design service</td></tr><tr><td>System design</td><td>SCP specificationWorkflow definition toolDatabase definition toolAdapter definition tool</td><td>System integration templateData transformation templateScreen program specification</td><td>System integration design serviceApplication interface design serviceApplication design service</td></tr><tr><td>Implementation</td><td>AdapterSCPWorkflow management systemDatabase management system</td><td>Sample program</td><td>SCP introduction serviceApplication development service system</td></tr></table>

![](/api/attachments/PSUUPBH4/fulltext/images/76311163fbf4e3b7bcb38ae22e7a1da224410e2ca4454203aea7e10a5fdfb196.jpg)  
Fig. 7. System development procedure of BPI.

## 4.1. The business design phase

In this phase, the requirements of the new business process are clarified and the business process and data model are designed. Here, the business process modeling method is applied to realize two important themes: real-time response and flexible system construction.

\- Business specification clarification: to clarify the goal, scope, constraints, and related organizations of the new business process, decide functions to be implemented as new business processes, select the best solution, and study its specifications.

\- Business process design: to design the essential business process to realize the requirements using the business process template, assign applications in the current business systems (legacy systems, as-is business processes, and SCP) to each task of the business process template, and study the feasibility.

\- Data model design: to design the data model of the information to be shared in the business process using the data model template, assign files, databases, and messages in the current business system to each entity in the data model template, and study the feasibility.

## 4.2. The system design phase

In this phase, the information system specifications are designed based on the business design result. Here, the workflow-based EAI architecture is applied to execute legacy systems, as-is processes, and SCP according to the new business process.

\- Input/output design: to design the input/output data flow among applications.

\- Reuse decision: to decide to make or reuse the applications and databases which are clarified in the business process design and data model design.

\- Interface design: to design the specifications of the adapter for initiating applications and detecting their completion.

\- Data specification design: to design the specifications of the adapter for transforming data formats among applications.

![](/api/attachments/PSUUPBH4/fulltext/images/429afae5d77c21a926ff71efc4383033334eeb0dcd13612a03d6be3e77151727.jpg)  
Fig. 8. System image of sourcing system.

## 4.3. The implementation phase

In this phase, the code of adapters, workflow, databases, and applications is generated based on the system design result. Here, the automatic code generation is realized by integrating various definition tools.

\- Adapter implementation: to automatically generate a set of interface programs with the adapter definition tool according to the adapter specifications described above.

\- System implementation: to implement a set of business process templates as a computer code with the workflow definition tool, convert a set of data model templates to physical tables with a database definition tool, and connect applications using adapters.

## 5. Case study

The effect of the BPI solution can be demonstrated by applying it for the sourcing process in an assembly manufacturer. Because the introduction speed of new models is increased and product life cycle has shortened, this manufacturer had a serious dilemma in trying to reduce its inventory and acquiring necessary material in appropriate time. Therefore, a high-speed MRP package, HITACHI SCPLAN, was used to improve the sourcing planning frequency and quality [6]. In the legacy system, the sourcing planning was executed monthly. With the new system, however, this planning was executed weekly and the results were sent to every related department in real time. The legacy system included the SAP R/3<sup>1</sup> sales management module, an inventory management module, and an order-made production management system on a UNIX server. It was necessary to integrate these application systems into the sourcing process using SCPLAN. Therefore, the BPI solution was used to develop the new sourcing system.

Fig. 8 shows the new sourcing system. This consists of two sets of business processes. One is the sourcing planning process to input the material inventory, material backlog, and production plan to SCPLAN, to calculate what and how much material is required, and to output the sourcing plan. The other is the sourcing management process to order the required material to the suppliers based on the sourcing plan. The former process is one of the sourcing solution templates previously described and the latter process is the sub-process that uses the sourcing plan calculated by the sourcing solution template. These business processes were implemented with the integration workflow, Workcoordinator. The legacy applications developed on RDB and SAP R/3 were mapped along the business processes and linked to Workcoordinator by way of the adapters.

These applications were integrated into the progress of the business processes. Firstly, according to the sourcing process, the production plan on RDB and the material inventory and backlog on R/3 were converted to the CSV (comma separated value) format. SCPLAN then inputs this information, calculates the required material, and outputs the sourcing plan. The sourcing plan is converted to the order information and loaded on RDB. Next, in the sourcing management process, the order form is created and approved on R/3, and sent to the suppliers.

To develop the sourcing system, the business process template, the data model template, the integration template, the adapters, and the screen program specification are all used. The business process template includes one main process. The data model template includes 28 data entities and 245 data items. The adapters include one application initiator, 35 status detectors, and nine data transformers. The transformers are R/3-RDB adapters and RDB-CSV adapters. The integration template defines the linkage map among the business process template, the adapters, and the applications. The screen program specification includes 13 sets of specifications for the screen layout and the program procedure.

The manpower required for system development using the BPI solution was compared with the previous method in Fig. 9. The manpower for the BPI solution is actual data, and the manpower shown for the previous method is calculated on the assumption of standard system development from scratch. From these results, the BPI solution reduces the manpower required for system development to about one third that of the previous method. There are three reasons for this improvement.

![](/api/attachments/PSUUPBH4/fulltext/images/1b7ba639145c499485a387a35192e8b47adb2ab7cf7ca3f3d91accd7c9a80079.jpg)  
Fig. 9. Effect of BPI solution.

(1) Advantage in the business design: BPI reduces the manpower required for the business design from four man-mouths to one man-mouth. In BPI, it takes one man-month for the business design team members to understand the business process and data model templates, compare them with the as-is process, and agree to adopt them. Because the business process template for a sourcing solution is the minimum essential set of the business process as described before, it is almost useless to customize them according to individual specifications. Though, some customization is needed, especially in the data model template.

(2) Advantage in the system design: BPI reduces the manpower required for the system design from 12 man-months to three man-months using the system integration template. It takes three manmonths to inspect the legacy systems, judge whether to reuse parts or to develop new applications, and design the specifications for adapters and new applications. By using the integration template, it is not necessary to design the data and event flow specifications.

(3) Advantage in the implementation: BPI reduces the manpower required for the implementation from 12 man-months to 4.7 man-months by using the adapters (mainly to implement the screen programs). Because adapters are automatically generated with the adapter definition tool from the specifications in the system design, it is not necessary to write adapter programs manually.

## 6. Conclusions

By using the BPI solution proposed here, the essential parts of the business process for applying SCP can be designed with the business process, data model, and system integration templates. For the detailed parts of the business process, as-is business processes and legacy systems can be substituted by using the adapters. Therefore, our solution reduces the manpower required for system development to about one third that of the previous method. In addition, the BPI solution allows complex and huge information systems, such as an SCM system, to be developed stepby-step. The BPI solution can be applied to other systems in which the business process can be clearly defined, such as the service order system in the telecom industry and the settlement system in the finance industry.

[12] T. Kobayashi, S. Onoda, N. Komoda, Workflow business template for application process in administration department, Journal of Information Technology & Management 3 (1/2), 2002, pp. 43–66.

[13] P. Lowrence (Ed.), Workflow Handbook, Wiley, New York, 1997.

[14] T.W. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1), 1994, pp. 87– 119.

[16] Supply-Chain Council, SCOR Supply-Chain Operation Reference-model, http://www.supply-chain.org (1999).

[15] G. Plenert, Focusing material requirements planning (MRP) towards performance, European Journal of Operational Research 119 (1), 1999, pp. 91–99.

[17] L. Yu, A Coordination-based Approach for Modeling Office Workflow, in: B. Scholz-Reiter, E. Stickel (Eds.), Business Process Modeling, Springer, New York, 1996.

[11] T. Kobayashi, S. Ogoshi, N. Komoda, A Business Process Design Method for Applying Workflow Tools, in: Proceedings of 1997 IEEE International Conference on System, Man, and Cybernetics, Orlando, 12–15 October 1997, pp. 2314– 2319.

## References

[1] J.S.K. Ang, C. Sum, L. Yeo, A Multiple-Case Design Methodology for Studying MRP Success and CSFs, Information & Management, vol. 39, Elsevier, Amsterdam, 2002, pp. 271–281.

[2] R.M. Cowdrick, Supply chain planning (SCP)—concepts and case studies, Computers & Industrial Engineering 29 (1/4), 1995, pp. 245–248.

[3] T. Curran, G. Keller, SAP R/3 Business Blueprint—Understanding the Business Process Reference Model, Prentice-Hall, Englewood Cliffs, NJ, 1998.

[4] S. David, Linthicum: Enterprise Application Integration, Addison-Wesley, Reading, MA, 1999.

[5] T. DeMarco, Structured Analysis and System Specification, Prentice-Hall, Englewood Cliffs, NJ, 1979.

[8] E.M. Goldratt, The Goal, Gower Publishing, London, 1998.

[7] S.L. Goldman, R.N. Nagel, K. Preiss, Agile Competitors and Virtual Organizations, Van Nostrand Reinhold, New York, 1995.

[6] M. Enomoto, H. Matoba, H. Morita, T. Segawa, Production Planning System Coping with Changing Customer Requirements, in Advances in Production Management Systems Perspectives and Future Challenges, Chapman & Hall, London, 1996, pp. 341–350.

[9] L. Kalakota, M.Robinson, e-Business—Roadmap for Success, Addison-Wesley, Reading, MA, 1999.

[10] P.G.W. Keen, M. McDonald, The eProcess Edge, McGraw Hill, New York, 2000.

![](/api/attachments/PSUUPBH4/fulltext/images/d5b9960b6542294e3cdd7903df26a977cc1308eef55e7a75d672de39d5ad2a48.jpg)  
Takashi Kobayashi is a chief consultant at the Business Solution Systems Division of Hitachi Ltd. He received BS and MS in mechanical engineering from Waseda University and PhD in information system engineering from Osaka University. His research interests include enterprise system modeling and system development methodology.

![](/api/attachments/PSUUPBH4/fulltext/images/181419b04f8a2c2a6fb71a5311a6ec911b9afd371cfd8fd35d09c140e9a79833.jpg)  
Masato Tamaki is a manager at the Business Solution Systems Division of Hitachi Ltd. He received BS in information engineering from Kyoto University. His research interests include solution development and requirement analysis methodologies.

![](/api/attachments/PSUUPBH4/fulltext/images/bfa74a070f2bbc20fbafae2fa96a3b9082871efce8679136e12548a0939f4ee5.jpg)

Norihisa Komoda is a professor in the Graduate School of Information Science and Technology at Osaka University. He received BS, MS, and PhD in electrical engineering from Osaka University. His research interests include system engineering and knowledge information processing.
