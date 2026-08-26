---
otero_id: 21391
otero_key: "4X5EA7KN"
title: "Building an organizational decision support system for Korea Telecom: A process redesign approach"
authors: "Young-Gul Kim; Hee-Woong Kim; Jae-Wook Yoon; Ho-seong Ryu"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00066-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building an organizational decision support system for Korea Telecom: A process redesign approach

Young-Gul Kim $^{a,*}$ , Hee-Woong Kim $^{a}$ , Jae-Wook Yoon $^{b}$ , Ho-Seong Ryu $^{b}$

$^{a}$ Korea Advanced Institute of Science and Technology, 207-43 Cheongryangri, Seoul, 130-012, South Korea $^{b}$ Korea Telecom Research Center, 17 Woomyeon, Seoul, 137-792, South Korea

Accepted 3 October 1996

## Abstract

Organizational decision support systems (ODSSs) are a new type of decision support systems (DSSs) focusing on organization-wide issues rather than individual, group, or departmental issues. Because of its organization-wide scope, a typical ODSS cuts across organizational functions or hierarchical layers. Thus, seamless integration with organization's diverse IS applications running on heterogeneous platforms becomes a critical issue for building a successful ODSS. In this paper, we analyzed the Korea Telecom's (KT) Operations & Maintenance (O&M) division focusing on its investment strategies. We developed a conceptual framework through process redesign, which links O&M investment decisions to performance of its operational branches across the nation. To support the above framework, we also developed a prototype for the KTOM-ODSS with an EIS-like user-friendly interface. When a complete ODSS is implemented on top of various KT transaction processing systems, it will become a critical component of the O&M Integrated Decision Support Environment (IDSE). © 1997 Elsevier Science B.V.

Keywords: Organizational decision support systems; Process redesign; Network communication; ODSS architecture

## 1. Introduction

With the opening trends of the international telecommunications service market, significant changes are taking place in the Korean telecommunications industry. Responding to the ever increasing customer demand for higher quality, Korean telecommunications companies are stepping up their quality-based competition. Korea Telecom (KT), which had monopolized the domestic telecommunications service market until recently, needs to shake up its old operating mode drastically to improve its customer service and sustain its competitive advantage. Thanks to Korea's telecommunication modernization drive started in the early 1980s, the hardware part of the KT's telecommunications infrastructure (electronic switching devices, fiber-optic communication lines, etc.) has improved significantly over the years. It is now the software part (operations and maintenance) of KT that needs to be the focus of the KT's new drive for improving its customer service quality.

In this study, we introduce a prototype Organizational Decision Support System (ODSS) to support the investment performance management process within KT's Operations & Maintenance (O&M) division. This ODSS is built upon the integration of KT's numerous transaction processing systems across the country and will be used by not only the O&M headquarters office but also the ten district business offices (hierarchically) and other related departments (horizontally). Instead of just supporting the current decision process, we proposed to 'reengineer' the process first to better meet KT's internal and external customer needs. With KT management's agreement, we then developed the ODSS prototype to support the reengineered O&M process.

The rest of the paper proceeds as follows. In Section 2, we will introduce KT, KT's O&M division, and KT O&M division's motivation to develop an ODSS. Section 3 provides an overview of the ODSS literature relevant to our study. Section 4 describes the KT O&M division's investment performance management process and how we reengineered it. Section 5 illustrates the architecture of the O&M ODSS and Section 6 explains how we implemented its prototype. In Section 7, we draw the conclusion of the paper and suggest future research directions related to extending the current ODSS.

## 2. Background

Korea Telecom (KT) is Korea's largest telecommunications service company, which is a semi-private company whose stock is owned partly by the government and partly by the public. KT provides a broad set of telecommunication services, including phone and data communication, with its nation-wide communication network. In 1995, it had more than six billion dollars in revenue. It has about 60,000 employees and has ten district business offices, which in turn are in charge of 360 local phone offices.

Operations & Maintenance (O&M) division is one of KT's 12 business divisions. It is the most labor-intensive division, employing 30,000 of the KT's 60,000 employees. These are the people who work closest to KT customers. The major O&M tasks are installation of new phone lines, change of customer phone services, troubleshooting and restoration of failed phone services, and day to day operation and maintenance of various hardware and software communication facilities.

To maintain high customer service quality, the O&M division must make continued investments, spending 15% of the KT's total annual budget. The investment means the budgeting for the O&M process of KT, which is not for generating revenue but for raising the communication service quality. To make these investment decisions effectively, performance of each district business office and local phone office needs to be evaluated. In the past, these performance related data had to be collected and processed manually from the local phone offices and submitted to the headquarters through the district business offices. At the headquarters, the data were scattered over different division offices. The whole process was very time-consuming and the data collected were often incomplete, incorrect, and hard to integrate. As a result, O&M management felt the need to establish a systematic investment performance management process, utilizing integrated decision support system capabilities based on O&M database, network, and various transactions processing systems.

We first looked into the traditional decision support system (DSS) and the more recent group decision support systems (GDSSs) research and practices. Both were found not very well-suited to our purpose. DSS implementations to date were mostly for the individual decision makers $[6,18,28]$ and GDSSs have also been used typically to support a group of people, gathered in a specially equipped decision room or on a local area network, solving a common problem during a designated group meeting $[4,16,28]$ . Thus, the organization wide scope and integration requirements of the O&M decision support environment led us to the development of an organizational decision support system (ODSS) for the O&M division's investment performance management process. ODSS is characterized by its organization-wide decision support scope and organizational activity support with communication network $[2,5,8,25,26,28,30]$ .

For the development of the system, we adopted the development procedure of the Issue-Based DSS and Business Process Redesign (BPR) [3]/Business Reengineering (BR) [10] perspective for the more effective implementation. The next section will provide a brief overview of what an ODSS is and the BPR approach to ODSS development will be explained in Section 4.

## 3. Organizational decision support system (ODSS)

Since the 1980s, as the scope of decision making widens over the entire organization, many perceived the need for the organization-level decision support mechanism [11]. Philippakis [26] introduced the term, Organization-wide Decision Support System, as an integrated decision support tool at the organizational level, differentiating it from the more traditional decision support system (DSS) to support individuals within a certain organizational unit. Watson [31] defined ODSS to be a system for supporting the cross-functional decision process to achieve organizational goals, utilizing computer and communication technologies. Swanson [27] interpreted ODSS to be a system to support the distributed decision making across the organization and used the term, DDSS (Distributed Decision Support System). Considering all these definitions, we can say that organizational decision support systems (ODSSs) are a new class of decision support systems focusing on the organization-wide issues rather than individual, group, or departmental issues.

According to George [8] and Aggarwal and Mirani [1,2], ODSS deals with a decision process which involves multiple organizational units and influences the entire organization, necessitating the use of an integrated communication network. Table 1 compares DSS, GDSS, and ODDS in terms of their goal, target decision maker, decision scope, and major technology components. While DSSs and GDSSs focus on individual and group-level decision making, ODSS focuses on organization-wide decision support. And while DSS is characterized by its modelbase and database components and GDSS is characterized by its coordination tool for decision support, ODSS is characterized by the enterprise-wide communication network and integration of modelbase, database, and protocols used.

Based on the above definitions and characteristics, many kinds of ODSS architectures have been suggested. Each architecture has its own characteristics and elements. Philippakis and Green [26] categorized the components of the ODSS into organization-level DSS functions and DSS resources. Here DSS functions include CPS (Corporate Planning System) to support strategic planning process, EIS (Executive Information System) to support top management, FDSS (Functional DSS) to support function-level decision making, and LDSS (Local DSS) to support the FDDSs. DSS resources were human resource, software/hardware, model/tool, and database. Watson [31] suggested an ODSS architecture in the form of an extended GDSS. His architecture consists of decision database, expertise database, corporate database, public database, and knowledge base, all integrated through a Meeting Support System operating on a corporate-wide network. Miller and Nilakanta's [24] ODSS architecture differentiate the three DSS components (knowledge subsystem, database subsystem, model subsystem) into internal/external and private/public dimensions. Miller [23] later proposed an ODSS architecture where the model subsystem, knowledge subsystem, and database subsystem exist in the framework of the organizational information environment, interconnected through the various communication interfaces. Because of the diversities of ODSS architecture, we should consider the business processes as well as the characteristics of each ODSS architecture when we build an ODSS environment [9,12].

Comparison of DSS, GDSS, and ODSS

<table><tr><td></td><td>DSS</td><td>GDSS</td><td>ODSS</td></tr><tr><td>System goal</td><td>Improving individual decision making</td><td>Enhancing group decision making performance</td><td>Facilitating organizational decision process</td></tr><tr><td>Decision maker</td><td>Individual</td><td>Group</td><td>Individual and group</td></tr><tr><td>Decision scope</td><td>Personal</td><td>Team/department</td><td>Organization-wide</td></tr><tr><td rowspan="3">Major technology component</td><td>Model base</td><td>Coordination tool</td><td>Integration tool</td></tr><tr><td>Database</td><td>Decision room</td><td>Enterprise-wide communication network</td></tr><tr><td>User interface</td><td>Local network</td><td></td></tr></table>

## 4. Investment performance management (IPM) at KT's O&M division

## 4.1. Reengineered IPM process

One of the major decision making tasks within the Korea Telecom O&M division's Investment Performance Management (IPM) process has been how to allocate its annual facility budget among the nationwide district business offices and local phone offices most fairly and effectively. Here ‘fairly’ means the use of open and objective criteria in the budget allocation process upon which all lower level offices can agree. ‘Effectively’ suggests how to maximize performance gains out of its investment.

The current budget allocation process is perceived to be neither fair nor effective. As can be seen in Fig. 1, the most critical problem was the lack of a link between the investment decision (budget allocation) and the performance evaluation. Budget allocation was done mostly based on the hardware facility status [20], while performance evaluation centered on quality of service (QOS) index. Since fair evaluation of hardware facility status was very difficult due to the lack of any agreed-upon measurement standards, budget allocation decisions were frequently subject to internal and external influences and complaints. On the performance evaluation side, data collected for the QOS index was often incomplete or incorrect for the following reasons. First, people at the local phone offices found it too time consuming to enter

QOS data reflected in the budget allocation process at headquarters since it was not directly linked to the budget allocation decision. Second, they were reluctant to have their performance judged solely on QOS data without any mechanism to account for the difficulty of their operating environments.

When the target process is unstable like this, developing an ODSS without first stabilizing the process may not help much. So, we proposed a new, 'reengineered' IPM process model as in Fig. 2. The model consists of O&M budget, O&M operations, CDI (Context Difficulty Index) and QOS (Quality of Service) of the local office. Each of these constructs will be explained in more detail in the following sections. The major changes from Fig. 1 are: first, context difficulty of each local office's operating environment is formally evaluated as CDI, second, both CDI and QOS are incorporated into the performance evaluation, third, performance evaluation results become the basis for the budget allocation decisions. The proposed redesign was discussed with KT managers in charge to assess whether the model is realistic. This reengineered IPM process model will be the conceptual framework upon which O&M ODSS will be built.

## 4.2. Quality of service: QOS

According to the International Telecommunication Union whitebook [15], QOS is defined as “the overall influence of the service performance which determines the service user’s satisfaction.” For a phone service company, QOS is an important index which indicates the extent to which its current phone network matches an ideal network performance. KT has initiated intensive research since 1988 to establish its QOS framework, which consists of network performance quality and operations quality as shown in Fig. 3 [7,17,21,22].

![](/api/attachments/4X5EA7KN/fulltext/images/e3beb4f0b570c5a035543df045f91f55a0866c90c3d14fdbe3f4f6977679c9da.jpg)  
Fig. 1. Current O&M budget investment allocation.

![](/api/attachments/4X5EA7KN/fulltext/images/8505c2a2f06f7a458fb0bfc2f052b9c7cfea78d5bf4e5e4cbe2f410617c6b909.jpg)  
Fig. 2. Proposed O&M IPM process model.

Network performance quality measures the level of successful transmission of data (voice and non-voice) and connection throughout the network. Currently, non-voice services on the phone network include data transmission through modem, videotex, and fax transmission. Quality of voice service breaks down into transmission quality which is affected by transmission loss and line noise and connection quality which occurs when one subscriber tries to be connected with the other subscriber. To evaluate and manage this network performance quality, NPMS (Network Performance Management System) is under the development in KT.

Operations quality is measured through many service items whose data are gathered from the operation of the phone network. These items are: rate of billing errors, average failure rate, average rate of normal repairing, average rate of normal installation, and normal 114 response rate. Here normal service means a service which was provided within the pre-specified time limit. These data consisting operations quality are managed by OMAS (Operations & Maintenance Administration System) [19]. We developed QOS function only about operations quality as in Appendix A because it directly affects customer satisfaction and the network performance quality cannot be evaluated yet.

## 4.3. Context difficulty index: CDI

QOS is an important means of evaluating performance of the O&M operations at local and district offices. Over the years, however, while QOS was treated as the major criteria on evaluating O&M performance, analysis of what factors caused or contributed to such QOS values was virtually ignored. This, in turn, led to wide-spread concern and complaints among the local offices over the fairness of their performance evaluation results. To address this problem and evaluate the O&M performance on a more reasonable basis, we introduced the concept of Context Difficulty Index (CDI) which will be used to evaluate each local or district office's O&M operating environment.

![](/api/attachments/4X5EA7KN/fulltext/images/cf256cf4626b8259925a5ea6feee2444489ec8d503cf0e529657102abd7d752f.jpg)  
Fig. 3. KT's QOS framework.

![](/api/attachments/4X5EA7KN/fulltext/images/2264bea3e5202de5af57e83ad6d3784dfee969d14752b667a658f3825c363e5a.jpg)  
Fig. 4. Context difficulty index components.

CDI, which represents the difficulty of the O&M operating environment, consists of four components as in Fig. 4. Level of backbone installation has two items: backbone deficiency rate and level of no-backbone area where backbone (mostly made of copper cable or fiber optics) refers to portion of the telephone line which starts from the local phone office and ends where it branches into the general subscriber's phone lines. Backbone deficiency rate indicates the relative rate of backbone deficiency compared to its demand at the area. Level of no-backbone area refers to the rate of no-backbone area among the entire area serviced by a local phone office. Level of underground cabling specifies the ratio of the underground cabling among the entire cabling. Manpower supply status reveals the over/under staffing of the O&M personnel at a given local office. Facility status represents the obsoleteness of various facilities (switches, lines, etc.)

operated by the local office. Based on these index components, we developed the CDI function as in Appendix B. CDI will be higher if a phone office has less backbone, less underground cabling, understaffing, and more obsolete facilities. More detailed explanation on CDI items and their measurement can be found in [17].

## 4.4. O & M budget allocation

O&M budgets are broken into regular and facility budgets. A regular budget is a budget for maintaining facilities and is used for electric facility management, communication network management, line facility maintenance, etc. A facility budget is a budget for installing new and replacing old facilities and is allocated according to KT's long-term facility planning. These budgets are first allocated among the district business offices, where the regular budget is allocated among the local phone offices while the facility budget is sent to and managed by the construction department. At each local office, the regular budget is divided into allocations for machines, lines, transmission, and electricity.

The relationship among QOS, CDI, and O&M budget and the allocation procedures are shown in Fig. 5. In Fig. 5, CDI and QOS are evaluated once at each local phone office and secondly at each district business office, comprising the two-dimensional performance evaluation of O&M operations. Based on these evaluation results, O&M management at the headquarters will be able to make O&M investment decisions in a fair and effective way.

![](/api/attachments/4X5EA7KN/fulltext/images/36dc3c182ff5e20317d1fea06ee853a8082713c9109bdf1736ce69101bff0024.jpg)  
Fig. 5. Relationships between CDI, QOS, and O&M budget allocation.

![](/api/attachments/4X5EA7KN/fulltext/images/8f9b4b31b81f1267b64898e184b37bb81cc66de9abac6d6647517783973e264e.jpg)  
Fig. 6. Relationship between QOS and CDI.

Performance evaluation of O&M operations can be done, utilizing the Pareto curve between QOS and CDI as in Fig. 6. Fig. 6 shows that QOS and CDI move in opposite directions from each other. That is, in general, when CDI is high (difficult operating environment), QOS is likely to be low, and vice versa. Most offices will be found around the Pareto curve. But, there can be exceptions. For instance, if a phone office is located in the 'A' quadrant of Fig. 6, it means they are delivering high quality service to their customers despite the difficult operating environments, implying exceptional management capability. On the other hand, a phone office found inside the 'C' quadrant away from the Pareto curve signals a potential management problem since its service quality is low while it operates in a favorable environment.

Based on this two-dimensional O&M performance evaluation, fair and effective O&M budget allocation now seems possible. First, for offices located in the 'A' area, allocate extra budgets on the first priority so that their operating conditions can improve, thus they can move to area 'B'. This may create the double effect of rewarding 'A' offices as well as stimulating 'D' offices to improve their QOS so that they can also operate under better conditions. Second, offices in the 'D' quadrant will receive extra budgets on the second priority so that they can move toward the 'B' quadrant over time. Third, offices in the 'B' quadrant may continue to receive the current level of budgets. Finally, offices in the 'C' quadrant first need to receive a special diagnosis of its management process to identify the cause of low service quality despite the favorable operating environment.

## 5. KTOM-ODSS: Organizational framework

## 5.1. KTOM-ODSS: Integrated network perspective

To implement the reengineered O&M IPM process in the most systematic and effective way, we decided to develop an ODSS, named KTOM-ODSS. In Fig. 7, KTOM-ODSS is shown to interact with many KT business processes and their supporting systems horizontally while vertically integrating with the lower level O&M transaction processing systems such as OMAS and NPMS [19]. On the horizontal side, interaction takes place in the form of data exchange over the network. For instance, Employee Management performed at the personnel management section and Facility Management performed at the facility management section provide CDI data to KTOM-ODSS, while the KTOM-ODSS provides crucial evaluation data to Task Management and investment data to Accounting Management.

On the vertical integration side, all the O&M management data at district business offices and local phone offices are entered into the O&M business database through the OMAS server located at each of the ten district business offices. The OMAS server performs data file reception from local phone offices, database management at the district level, and creation-analysis-evaluation of QOS data for each local office. NPMS is a system to measure the connection and transmission quality of a phone network. NPMS provides QOS' network performance quality data for input into the O&M database.

Through the enterprise-wide network communication, performance evaluation of O&M operations and budget allocations are conducted based on the procedures as in Fig. 5. Each local telephone office manages its O&M related data from the QOS and CDI perspectives. Based on the O&M database, each district business office measures its O&M performance. At the O&M headquarters office, O&M budget is allocated among district business offices based on the QOS and CDI data of 10 district business offices from the distributed O&M databases and those related data from other transaction processing systems. Each district business office allocates its arranged budget among its telephone offices based on the guidelines from the QOS and CDI relationships in Fig. 6.

From this integrated network perspective and the procedures, we can know KTOM-ODSS is a kind of distributed computing system, which is a collection of autonomous computers interconnected through a communication network to achieve a business function $[29]$ . The main characteristic of a distributed computing system is that a user can perform some functions on a local computer, while still accessing remotely located databases and computers $[29]$ . The system supports cooperation horizontally and vertically between different KT processes, offices, and systems to share information and computing resources. And, as the basic ingredients – autonomous and coordination – of distributed computing system, KTOM-ODSS at each office operates autonomously and those systems cooperate to achieve the investment-performance management function through the enterprise-wide communication network.

## 5.2. KTOM-ODSS: Architectural perspective

Before developing the KTOM-ODSS architecture, we investigated the characteristics of the O&M process. The main characteristics of the KT O&M process are process-hierarchy (headquarters, district business office, telephone office) and interrelationships with other internal processes (task management, employee management, accounting management, etc.). Considering these aspects and previous redesign ideas, we selected an ODSS architecture suggested by Philippakis and Green [26]. The architecture took the form of a pyramid, into which were organized the four types of DSS they had delineated: corporate planning systems (CPSs), executive information systems (EISs), and local DSS (LDSS). CPSs have a corporate-wide scope, a long-term horizon, and high organizational level of the end users [8,26]. EISs focus on the short term and performance, which assist top level executives in the conduct of ad hoc analysis of current performance and projected operations [8,26]. CPSs and EISs are on top of the pyramid because they cut across organizational functions. FDSSs provide support in a functional area, and LDSSs are locally developed and controlled, with little formal structure. The FDSSs and LDSSs are distributed within functions because they are limited to particular functions, run by individuals or teams within them. All four types of DSS functions draw on organizational DSS resources, which include human resources, software/hardware, models/tools, and databases.

![](/api/attachments/4X5EA7KN/fulltext/images/42a4b9841a6b2576b13d9aa79e7002813ef9596ad00070b6551b0b8d95ea95ef.jpg)  
Fig. 7. KTOM-ODSS: Integrated network perspective.

But, the architecture needed some modifications for real implementation. First, we considered the requirement of group communications between high level of end users in the CPS because the planning decision is seldom set by one manager. For this reason, the CPS requires somewhat GDSS form. Second, we considered not only a centralized database but a distributed database as well (O&M database at the O&M headquarters office, local O&M database at each district business office, each management related database) that is interfaced through the network. Finally, although Philippakis [26] applied each FDSS and LDSS to different functions in the architecture, we applied it to the same function (O&M) but different district/telephone offices. These modifications could reflect the investment performance management process of KT more adequately.

Based on the above modifications and redesign ideas, we developed an ODSS architecture as in Fig. 8. At the lowest level of the DSS function, the functional and local DSSs are designed to support the within-function tasks. FDSSs are distributed over the 10 district business offices. Within a function (district business area), LDSSs are distributed over several telephone offices. LDSS enables managers at each telephone office to evaluate its O&M operations with QOS/CDI models and O&M data. These O&M data and evaluation data consist local O&M database. And those LDSSs at telephone offices are integrated through the network at each district business office. Based on the integration between LDSSs, FDSS enables managers to analyze and evaluate O&M operations of telephone offices with the local O&M database and QOS/CDI model.

At the second DSS function level (EIS), we designed O&M Investment–Performance Management to analyze the target business process and its performance. In this level, those FDSSs at each district business office are integrated through the network. Based on the network connection between district offices, local O&M databases at district offices consist the main O&M database. This O&M database and QOS/CDI models enable executives to analyze the investment performance and O&M operations of each district office. This analysis and evaluation data become the basis for the O&M Strategy Planning.

![](/api/attachments/4X5EA7KN/fulltext/images/b6a5322d31bf0e73220b12221847b1cf5f3d8c629341a7f6f6b4ba25fa37fc18.jpg)  
Fig. 8. KTOM: Architectural perspective.

For the organization-wide planning or strategy development (CPS) at the highest DSS function level, the KTOM-ODSS has O&M Strategy Planning in the area of investment performance management. In the KT O&M case, the main job of the Strategy Planning is the planning of QOS and CDI levels to pursue. Also, the amount of yearly O&M budget is arranged in this level. For this planning, high level managers in the O&M division and other related divisions communicate to each other because this plan affects each division and its subfunctions.

Organizational DSS resources involve database, model/tool, software/hardware, and human resources [26]. In KTOM-ODSS, we have the O&M database which collects and stores O&M data from district and local offices through the network. One of the core components of the KTOM-ODSS is the investment performance evaluation model (QOS and CDI models), and OMAS and NPMS correspond to the software/hardware DSS resources. Lastly, all the O&M personnel involved in the data entry, hardware/software operation and maintenance, database and network administration, and final use of the ODSS models will comprise the human resource category of DSS resource.

## 6. KTOM-ODSS: Prototype implementation

A prototype of KTOM-ODSS was developed on a 486 PC under the Windows 3.1 environment, using the FOCUS [13] and FOCUS/EIS [14] tools. Execution of the prototype requires a minimum memory of 8 MB. The FOCUS language was selected because of its non-procedural nature and to facilitate the integration with the KT O&M division's main transaction processing system (OMAS) which was devel-

![](/api/attachments/4X5EA7KN/fulltext/images/0dd875b3308e0a021b858730193589cee6461606574746cebb657e3efd8c72a6.jpg)  
Fig. 9. System configuration.

oped in FOCUS. The KTOM-ODSS system has been designed based on the suggested ODSS framework from the network perspective – organization wide network connection - in Fig. 7 and the architectural perspective - ODSS function and resource - in Fig. 8.

![](/api/attachments/4X5EA7KN/fulltext/images/d5e68b9b83b91a96ff3fd96e0411207f2dde997f0d4c521337e8028682c3c87d.jpg)  
Fig. 10. Performance evaluation.

![](/api/attachments/4X5EA7KN/fulltext/images/f40e88f5ca429a72f50ca8137fcf0dc7a92d37987be82f7551958c3be79c7f19.jpg)

The KTOM-ODSS is divided into two divisions: main system and transaction processing system (TPS) as in Fig. 9. Other transaction management systems are integrated horizontally with the KTOM-ODSS. In addition to these TPS, O&M transaction processing systems such as OMAS for data management and NPMS for the network performance evaluation are connected to the data management (O&M database) module of the main system. The O&M database is designed as in Appendix C.

The main system has four main modules: Target Selection, Investment Support, Performance Evaluation, and Data Management. The target selection module supports the selection of a district or local office by name or list search. This module enables managers at headquarters office to manage and evaluate district offices. Also, it enables managers at each district business offices to manage and evaluate their telephone offices. At each local telephone office, the system supports managers to evaluate and manage their O&M operations. The investment support module contains historical and current information on the regular and facility budget of each local and district office. It will be extended to include the performance forecasting function that enables users to forecast performance (QOS and CDI) for a given investment (regular and facility budget) amount and total portfolio.

The performance evaluation module calculates QOS and CDI data of all offices and displays their statistical distribution in both text and graphic forms along with a budget allocation strategy. Fig. 10 shows that the ‘Gwanghwamoon Office in Seoul Business Area’ is evaluated on its performance of O&M works. The Gwanghwamoon office received 93.02% QOS point and 4 CDI level. The distribution reveals that the office obtained high QOS score in a poor O&M environment. And, if the ‘Action’ menu were selected, another screen (Fig. 11) will display QOS and CDI distributions with Gwanghwamoon office’s status and the suggested investment action. The data management module interacts with the various transactions processing systems to retrieve, convert, and transmit the O&M investment and performance related data from the other business departments and local/district offices.

For the O&M Strategy Planning level of the architecture in Fig. 8, this system supports high level managers to infer the relationship between the budget amount and the O&M performance through the Investment Support and Performance Evaluation modules. Based on the relationship between them, they plan O&M strategy such as QOS and CDI level and decide total budget amount and allocate it among 10 district offices. For the O&M Investment-Performance Management level of the architecture, this system enables users to analyze the performance of each district business office and the allocated budget amount with Investment Support and Performance Evaluation modules. For the FDSS level of the architecture, this system enables users to analyze performance of each telephone office and context difficulty with the Performance Evaluation and Data Management modules. Also, managers at each district office can allocate the arranged budget among its telephone offices based on these two modules. For the LDSS level of the architecture, this system enables users to manage its O&M related data which consist local O&M database with Data management module.

## 7. Conclusion and future directions

Research and practical implementations of ODSS concepts are not as mature or active as those of DSS or GDSS. But, with more and more organizations integrating their departmentalized information systems into an organization-wide one based on the sophisticated communication network, the importance of ODSS will continue to grow. This paper reports on the implementation of an ODSS prototype for the Korea Telecom company. As a stand-alone prototype system itself, it is fairly small and simple. But when it is fully integrated with its surrounding transaction processing systems in the future, it will become a very powerful model case of an ODSS which will affect the entire nation's phone network operations and maintenance.

The very nature of a phone service company providing service to any customer connected to its phone network seems to fit nicely with the ODSS philosophy of providing decision support to the decision makers at headquarters and each district business office connected to the integrated corporate network. Applying the ‘reengineering’ principle to our target decision process was very crucial. Without it, we might have created an ODSS which would support the ‘unfair’ and ‘ineffective’ decision process to run more ‘efficiently’.

The KTOM-ODSS introduced in this study demonstrates the main ODSS characteristics. First, it supports the organizational task (Budget allocation with O&M investment performance) that affects several organizational units (O&M division, 10 district business offices, 360 local telephone offices, other related sections). Second, it cuts across organizational functions (personnel management section, facility management section, accounting section, etc.) and hierarchical layers (headquarters, district business offices, local telephone offices). Third, there are multiple decision makers at headquarters and 10 district business offices interconnected through the organization-wide communication network. They can perform investment-performance evaluation and make budget allocation decisions about each business area with the help of the performance evaluation model and corporate O&M database.

For the future extension of our KTOM-ODSS, three directions seem promising. First, we need to develop diverse decision models (e.g., performance forecasting) and knowledge-based components to make the system behave more ‘intelligently’. Second, we plan to establish the actual network connection between the KTOM-ODSS and its surrounding transaction processing systems and other KT databases. Third, we consider the application of data warehousing in ODSS development. Data warehousing is characterized by its on-line analytic processing (OLAP) function and its transaction processing function.

## Appendix A. QOS function

QOS = {(100 - Rate\_of\_billing\_error) + (100 - Average\_failure\_rate) + Average\_rate\_of\_normal\_repairing + Average\_rate\_of\_normal\_installation + Normal\_114\_response\_rate}/5,

## where

Rate\_of\_billing\_error = (number\_of\_billing\_errors / number\_of\_billings) × 100;

Average\_failure\_rate

$= (\text{number\_of\_failures} / \text{number\_of\_members}) \times 100;$

Average\_rate\_of\_normal\_repairing = (repairing\_rate\_in\_time/number\_of\_failures\_registered) × 100;

Average\_rate\_of\_normal\_installation

=(number\_of\_installation\_in\_time/total\_number\_of\_installation)

×100;

Normal\_114\_response\_rate

$= (\text{number\_of\_responses\_in\_time} / \text{number\_of\_114\_requests}) \times 100.$

## Appendix B. CDI function

CDI = Level\_of\_backbone\_installation + Level\_of\_underground\_cabling + Man\_power\_supply\_status + Facility\_deterioration\_status,

## where

Level\_of\_backbone\_installation = (Deficiency\_rate\_of\_backbone + No\_backbone\_area\_rate)/2;

Deficiency\_rate\_of\_backbone = (number\_of\_deficient\_pairs × 100)/total\_number\_of\_pairs;

No\_backbone\_area\_rate

$= (\text{No\_backbone\_area} \times 100) / \text{total\_area\_in\_charge};$

Level\_of\_underground\_cabling = (underground\_cabling\_length × 100) / total\_cabling\_length;

Man\_power\_supply\_status = (number\_of\_employees\_in\_excess\_or\_deficiency × 100)/

required\_number\_of\_employees;

Facility\_deterioration\_status = (number\_of\_facilities × Deterioration\_rate)/total\_number\_of\_facilities;

Deterioration\_rate

$= (\text{time\_in\_usage} \times 100) / \text{available\_usage\_time}$ .

Appendix C. Entity-relationship diagram for the O&M database

![](/api/attachments/4X5EA7KN/fulltext/images/a54a1ab0691b2de513b112cd39426549103ec7078f6ddcd45753190294c4071a.jpg)

## References

[1] A.K. Aggarwal and R. Mirani, Macro issues in the development of organizational decision support systems, in: Proc. of the 28th Annual Hawaii International Conference on System Sciences 3 (1995) 917–926.

[2] A.K. Aggarwal and R. Mirani, Policy implications of organizational decision support systems, in: Proc. of the 29th Annual Hawaii International Conference on System Sciences 4 (1996), 48–53.

[3] T. Davenport and J.E. Short, The new industrial engineering: Information technology and business process redesign, Sloan Management Review (1990) 11–27.

[4] G. DeSanctis and B. Gallupe, A foundation for the study of group decision support systems, Management Science 33(5) (1987) 589–609.

[5] C. Dubraka, Organizational activity support systems, Decision Support Systems 12 (1994) 365–379.

[6] M.C. Er., Decision support systems: A summary, problems, and future trends, Decision Support Systems 4 (1988) 355-363.

[7] ETRI, A study of the integrated strategic investment management, Project Report, 1993.

[8] J.F. George, The conceptualization and development of organizational decision support systems, Journal of Management Information Systems 8(3) (1991–1992) 109–125.

[9] J.F. George, J.F. Nunamaker and J. Valacich, ODSS: Information technology for organizational change, Decision Support Systems 8 (1992) 307–315.

[10] M. Hammer, Reengineering work: Don't automate, obliterate, Harvard Business Review (1990) 104–112.

[11] G.P. Huber, The nature of organizational decision making and the design of decision support systems, MIS Quarterly 5(2) (1981) 1–10.

[12] S. Illiaifar, S. Nilakanta and G.M. Prabhu, Technology imperatives of BPR and their effect on organizational decision

support, in: Proc. of the 28th Annual Hawaii International Conference on Systems Sciences 4 (1995) 941–946.

[13] Information Builders, FOCUS for Windows, 1993.

[14] Information Builders, FOCUS/EIS for Windows release 3.3, 1993.

[15] ITUT (International Telecommunication Union) -T (Telecommunication), White Book, 1992.

[16] L.M. Jessup and J. Valacich, eds., Group Support Systems: New Perspectives (Macmillian, 1993).

[17] KAIST, Building an investment-performance management DSS for supporting KT O&M strategy development, Project Report RL4D001, 1994, 12.

[18] P.G.W. Keen and R.D. Hackthorn, Decision support systems and personal computing, MIS Quarterly 5(3) (1981) 21–27.

[19] Korea Telecom, OMAS/L user's manual, 1994.

[20] Korea Telecom, O&M budget allocation manual, 1994.

[21] Korea Telecom Research Lab., A study on network service quality, 1993.

[22] KTA Research Center, A study on the economy analysis model for QOS management and the planning for the implementation of integrated operation and maintenance network, Project Report, 1988–1989.

[23] L.L. Miller, Organizational decision support systems, Decision Support Systems 9 (1993) 201–215.

[24] L.L. Miller and S. Nilakanta, Design of organizational decision support systems: The use of a data extraction scheme to facilitate model-database communication, in: Proc. of the 24th Annual Hawaii International Conference on System Sciences 4 (1991) 65–72.

[25] M. Pagani and A. Belluci, An organizational decision support system for Teletra's top management, in: R.M. Lee, A.M. McCosh and P. Migliarese, eds., Organizational Decision Support Systems (North-Holland, 1988) 3–13.

[26] A.S. Philippakis and G.I. Green, An architecture for organization-wide decision support systems, in: Proc. of Ninth International Conference on Information Systems (1988) 257–263.

[27] E.B. Swanson, Distributed decision support systems: A perspective, in: Proc. of the 23rd Annual Hawaii International Conference on System Sciences 3 (1990) 129–136.

[28] E. Turban, Decision Support and Expert Systems: Management Support Systems, 3rd Edition (Macmillan, 1993).

[29] A. Umar, Distributed Computing and Client-Server Systems (Prentice Hall, 1993).

[30] W.E. Walker, Differences between building a traditional DSS and An ODSS: Lessons from the Air Force's enlisted force management system, in: Proc. of the 23rd Annual Hawaii International Conference on System Sciences 3 (1990) 120–128.

[31] R.T. Watson, A design for an infrastructure to support organizational decision-making, in: Proc. of the 23rd Annual Hawaii International Conference on System Sciences 3 (1990) 137–142.

![](/api/attachments/4X5EA7KN/fulltext/images/d339c4112df56e654ec66e305829696b6b12d3e4a38e49ef8781137c2bb07412.jpg)

Young-Gul Kim is an associate professor at the Graduate School of Management of the Korea Advanced Institute of Science and Technology in Seoul. He received his B.S. and M.S. degree in Industrial Engineering from the Seoul national University, Korea and Ph.D. Degree in MIS from the University of Minnesota. His active research areas are: IS Architecture Development, Business Modeling, and IS management. He has published in CACM, Information and

Management, Database, Journal of MIS, and Information Systems Management. Also, he presented several papers at ICIS, HICSS, and DSI conferences.

![](/api/attachments/4X5EA7KN/fulltext/images/b4a76908468d4729c4df761d3d7cff8c2ac6e80f2e74eff9927706575e7ad095.jpg)

Hee-Woong Kim is a Ph.D. student at the Graduate School of Management of the Korea Advanced Institute of Science and Technology in Seoul. He received his B.S. and M.S. degree in Industrial Engineering from the Pohang University of Science and Technology, Korea. His research areas are: IS Architecture Development, Business Process Modeling, and Simulation. He has published in the Journal of MIS Research and presented several papers at HICSS, DSI confer-

ence, and European Simulation Symposium.

![](/api/attachments/4X5EA7KN/fulltext/images/55d8ecf28449754ab284e902102ffb1df8a0d988b1108d0c16c2394993890b70.jpg)

Jae-Wook Yoon is a senior member of technical staff in the network quality research team of Korea Telecom Research Labs. Received Ph.D. In Industrial and Operations Engineering from the University of Michigan, M.S. in Management Science from Korea Advanced Institute of Science and Technology, B.S. in Industrial Engineering from Seoul National University. Interest areas are Quality Management, Management Information Systems, and Telecommunications.

![](/api/attachments/4X5EA7KN/fulltext/images/bfeb20e1c4d39160cf441a471b146dbbbf30bf42a156a2e0f861ed6ec5549f67.jpg)

Ho-Seong Ryu is a member of technical staff in the network quality research team of Korea Telecom Research Labs. Received M.S. in Engineering Economy from Seoul National University, B.S. in Industrial Engineering from Seoul National University. Interests areas are Quality Management and Telecommunications.
